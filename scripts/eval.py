"""Run the golden questions (evals/golden.yaml) through the chatbot and grade the answers.

    python -m scripts.eval [--ids id1,id2] [--model claude-haiku-5-5]

For each question: recall@6 (an expected section is among the first search's 6 results), whether the answer cites
an expected section, and a 1-5 grade from a Claude judge that sees the reference answer and the cited passages.
Out-of-scope questions are graded on whether the answer says the manual does not cover them.
Writes evals/last_run.json. Each full run costs roughly $1 with Claude Sonnet 5.5.
"""

from __future__ import annotations

import argparse
import asyncio
import dataclasses
import json
import re

import anthropic
import yaml

from app.config import ROOT, Config
from app.llm import Chat
from app.search import Manual

JUDGE = "claude-haiku-5-5"
GRADE = """Grade an answer from an assistant that must answer only from the LBTI User's Manual.
Question: {question}
Reference (key facts from the manual): {expected}
Passages the assistant cited: {cited}
Answer: {answer}

Score 1-5: 5 correct and complete, every number matches; 4 correct with minor omissions; 3 partly correct or
missing something important; 2 mostly wrong or unsupported; 1 wrong, invented, or refuses although the manual covers it.
Extra detail is fine if the cited passages support it. The assistant is told that the web pages are canonical and
the PDF is an older snapshot, so attributing values to either is expected. Reply with "SCORE: <n>" and a reason."""
ABSTAIN = """The LBTI manual does not cover this question: {question}
Answer: {answer}
Did the answer clearly say it is not covered, without stating facts or numbers that answer it?
Reply with "ABSTAINED: yes" or "ABSTAINED: no" and one sentence of reasons."""


async def grade(client: anthropic.AsyncAnthropic, prompt: str) -> str:
    r = await client.messages.create(model=JUDGE, max_tokens=1024, messages=[{"role": "user", "content": prompt}])
    return "".join(b.text for b in r.content if b.type == "text")


async def run_one(chat: Chat, manual: Manual, client: anthropic.AsyncAnthropic, q: dict) -> dict:
    out: dict = {}
    async for _ in chat.answer([], q["question"], out):
        pass
    expected = {manual.sections[sid]["source_url"] for sid in q.get("expected_section_ids") or []}
    row = {"id": q["id"], "question": q["question"], "answer": out["answer"], "searches": out["searches"],
           "sources": [s["source"] for s in out["sources"]]}
    if q.get("type") == "out_of_scope":
        verdict = await grade(client, ABSTAIN.format(question=q["question"], answer=out["answer"]))
        row["abstained"] = bool(re.search(r"ABSTAINED:\s*yes", verdict, re.I))
    else:
        row["recall_at_6"] = bool(expected & set(out["first_found"][:6]))
        row["cites_expected"] = bool(expected & set(row["sources"]))
        cited = "\n".join(f"[{s['title']}] {t}" for s in out["sources"] for t in s["cited_text"]) or "(none)"
        verdict = await grade(client, GRADE.format(question=q["question"], expected=q["expected_answer"],
                                                   cited=cited, answer=out["answer"]))
        row["score"] = int(m.group(1)) if (m := re.search(r"SCORE:\s*([1-5])", verdict)) else None
    row["judge"] = verdict.strip()
    return row


async def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ids", help="comma-separated question ids (default: all)")
    ap.add_argument("--model", help="model to evaluate (default: MODEL from the environment)")
    args = ap.parse_args()
    cfg = Config.from_env()
    cfg = dataclasses.replace(cfg, model=args.model) if args.model else cfg
    manual, client = Manual(cfg.index_dir), anthropic.AsyncAnthropic()
    chat = Chat(cfg, manual, client)
    questions = yaml.safe_load((ROOT / "evals" / "golden.yaml").read_text())["questions"]
    if args.ids:
        questions = [q for q in questions if q["id"] in args.ids.split(",")]
    limit = asyncio.Semaphore(3)

    async def guarded(q):
        async with limit:
            row = await run_one(chat, manual, client, q)
            print(f"{row['id']:<24} score={row.get('score', '-')} recall={row.get('recall_at_6', '-')} "
                  f"abstained={row.get('abstained', '-')}", flush=True)
            return row

    rows = await asyncio.gather(*(guarded(q) for q in questions))
    mean = lambda xs: round(sum(xs) / len(xs), 2) if xs else None  # noqa: E731
    answerable = [r for r in rows if "score" in r]
    summary = {"model": cfg.model, "questions": len(rows),
               "recall_at_6": mean([r["recall_at_6"] for r in answerable]),
               "cites_expected": mean([r["cites_expected"] for r in answerable]),
               "judge_mean": mean([r["score"] for r in answerable if r["score"]]),
               "abstentions": f"{sum(r['abstained'] for r in rows if 'abstained' in r)}/"
                              f"{sum('abstained' in r for r in rows)}"}
    print(json.dumps(summary, indent=1))
    if not args.ids:
        (ROOT / "evals" / "last_run.json").write_text(json.dumps({"summary": summary, "results": rows}, indent=1,
                                                                 ensure_ascii=False))


if __name__ == "__main__":
    asyncio.run(main())
