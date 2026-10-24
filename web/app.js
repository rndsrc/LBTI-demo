/* LBTI Assistant chat page. No build step; marked (Markdown) and DOMPurify (sanitising) are vendored. */
(() => {
  "use strict";
  const $ = (id) => document.getElementById(id);
  const el = (tag, cls, text) => Object.assign(document.createElement(tag), cls ? { className: cls } : {}, text ? { textContent: text } : {});
  let conversationId = null;
  let controller = null;

  // Manual version for the banner; example questions ask themselves when clicked.
  fetch("/api/info").then((r) => r.json()).then((info) => {
    $("version").textContent = info.pdf_version;
    $("ingested").textContent = info.ingested_at;
    $("manual").href = info.manual_url;
    $("input").maxLength = info.max_chars;
  });
  document.querySelectorAll("#examples button").forEach((b) => { b.onclick = () => { $("input").value = b.textContent; ask(); }; });

  // Render the answer as sanitised Markdown, then turn [n] markers into citation chips.
  function render(msg) {
    msg.body.innerHTML = DOMPurify.sanitize(marked.parse(msg.raw), { FORBID_TAGS: ["img", "style", "form"] });
    msg.body.querySelectorAll("a").forEach((a) => { a.target = "_blank"; a.rel = "noopener noreferrer"; });
    const walker = document.createTreeWalker(msg.body, NodeFilter.SHOW_TEXT);
    const nodes = [];
    while (walker.nextNode()) if (/\[\d+\]/.test(walker.currentNode.nodeValue) && !walker.currentNode.parentElement.closest("a, code")) nodes.push(walker.currentNode);
    for (const node of nodes) {
      const parts = node.nodeValue.split(/(\[\d+\])/);
      node.replaceWith(...parts.map((p) => {
        const src = msg.sources[Number(p.slice(1, -1)) - 1];
        if (!/^\[\d+\]$/.test(p) || !src) return p;
        const chip = el("a", "cite", p.slice(1, -1));
        chip.href = src.source;
        chip.target = "_blank";
        chip.rel = "noopener noreferrer";
        chip.append(el("span", "tip", `${src.title}\n\n${src.cited_text.join("\n…\n").slice(0, 600)}`));
        return chip;
      }));
    }
  }

  function showSources(msg) {
    if (!msg.sources.length) return;
    const list = el("ol");
    for (const s of msg.sources) {
      const a = el("a", "", s.title);
      a.href = s.source;
      a.target = "_blank";
      a.rel = "noopener noreferrer";
      const item = el("li");
      item.value = s.n;
      item.append(a);
      list.append(item);
    }
    msg.box.append(el("h4", "", "Sources"), list);
  }

  // Server-sent events from a fetch() response body.
  async function* events(response) {
    const reader = response.body.pipeThrough(new TextDecoderStream()).getReader();
    let buffer = "";
    for (;;) {
      const { value, done } = await reader.read();
      if (done) return;
      buffer += value;
      let end;
      while ((end = buffer.indexOf("\n\n")) >= 0) {
        const chunk = buffer.slice(0, end);
        buffer = buffer.slice(end + 2);
        const event = /^event: (.*)$/m.exec(chunk)?.[1];
        const data = /^data: (.*)$/m.exec(chunk)?.[1];
        if (event && data) yield [event, JSON.parse(data)];
      }
    }
  }

  async function ask() {
    const question = $("input").value.trim();
    if (!question || controller) return;
    $("welcome").hidden = true;
    $("input").value = "";
    $("messages").append(el("li", "user", question));
    const box = el("li", "assistant");
    const status = el("p", "status", "Searching the manual…");
    const msg = { box, body: el("div", "answer"), raw: "", sources: [] };
    box.append(status, msg.body);
    $("messages").append(box);
    box.scrollIntoView({ block: "end" });
    controller = new AbortController();
    $("send").disabled = true;
    $("stop").hidden = false;
    try {
      const response = await fetch("/api/chat", {
        method: "POST", headers: { "Content-Type": "application/json" }, signal: controller.signal,
        body: JSON.stringify({ message: question, conversation_id: conversationId }),
      });
      if (!response.ok) throw new Error((await response.json().catch(() => ({}))).detail || `Error ${response.status}`);
      for await (const [event, data] of events(response)) {
        if (event === "meta") conversationId = data.conversation_id;
        else if (event === "status") { status.hidden = false; status.textContent = data.text; }
        else if (event === "retract") msg.raw = "";
        else if (event === "text") { status.hidden = true; msg.raw += data.text; }
        else if (event === "sources") msg.sources = data.sources;
        else if (event === "error") throw new Error(data.message);
        render(msg);
      }
      showSources(msg);
    } catch (err) {
      status.hidden = true;
      box.append(el("p", "error", err.name === "AbortError" ? "Stopped." : err.message));
    } finally {
      controller = null;
      $("send").disabled = false;
      $("stop").hidden = true;
      $("input").focus();
    }
  }

  $("composer").onsubmit = (e) => { e.preventDefault(); ask(); };
  $("input").onkeydown = (e) => { if (e.key === "Enter" && !e.shiftKey && !e.isComposing) { e.preventDefault(); ask(); } };
  $("stop").onclick = () => controller?.abort();
  $("new-chat").onclick = () => {
    controller?.abort();
    conversationId = null;
    $("messages").replaceChildren();
    $("welcome").hidden = false;
  };
})();
