/* LBTI Assistant chat page: send a question, show the answer as it streams in. No build step. */
(() => {
  "use strict";
  const $ = (id) => document.getElementById(id);
  const el = (tag, cls, text) => Object.assign(document.createElement(tag), cls ? { className: cls } : {}, text ? { textContent: text } : {});
  let controller = null;

  // Show the answer as plain text.
  function render(msg) {
    msg.body.textContent = msg.raw;
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
    const status = el("p", "status", "Thinking…");
    const msg = { box, body: el("div", "answer"), raw: "" };
    box.append(status, msg.body);
    $("messages").append(box);
    box.scrollIntoView({ block: "end" });
    controller = new AbortController();
    $("send").disabled = true;
    $("stop").hidden = false;
    try {
      const response = await fetch("/api/chat", {
        method: "POST", headers: { "Content-Type": "application/json" }, signal: controller.signal,
        body: JSON.stringify({ message: question }),
      });
      if (!response.ok) throw new Error((await response.json().catch(() => ({}))).detail || `Error ${response.status}`);
      for await (const [event, data] of events(response)) {
        if (event === "text") { status.hidden = true; msg.raw += data.text; }
        else if (event === "error") throw new Error(data.message);
        render(msg);
      }
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
    $("messages").replaceChildren();
    $("welcome").hidden = false;
  };
})();
