#!/usr/bin/env python3
"""
Build BrianThinks.md (the mdwiki-deployed page with JS copy button)
from BrianThinkz.md (clean Markdown source).

Source format:
  Everything before <!-- END PROMPT --> becomes the copyable prompt text.
  Everything after becomes the page tail (Example Starters, Credits, etc.).
"""

import sys
from pathlib import Path

HERE = Path(__file__).parent
SOURCE = HERE / "BrianThinkz.md"
OUTPUT = HERE / "BrianThinks.md"
BEGIN_PROMPT = "<!-- BEGIN PROMPT -->"
END_PROMPT = "<!-- END PROMPT -->"

PAGE_HEADER_TEMPLATE = """\
{heading}

<div id="copy-button-container"></div>

2\\. Paste into any AI
3\\. Add your question or comment

The AI will imitate Brian for the rest of the conversation. Lucky you!

<div id="prompt-container"></div>

<script>
(function() {
  var promptText = `"""

JS_FOOTER = """\
`;

  var copyButton = document.createElement('button');
  copyButton.textContent = '1. Copy Brian\\'s brain';
  copyButton.className = 'btn btn-primary';
  copyButton.style.cssText = 'display: block; margin-bottom: 15px; padding: 8px 16px; font-size: 14px;';
  copyButton.onclick = function() {
    textarea.select();
    document.execCommand('copy');
    var originalText = copyButton.textContent;
    copyButton.textContent = '\\u2713 Copied!';
    copyButton.className = 'btn btn-success';
    setTimeout(function() {
      copyButton.textContent = originalText;
      copyButton.className = 'btn btn-primary';
    }, 2000);
  };

  var textarea = document.createElement('textarea');
  textarea.value = promptText;
  textarea.readOnly = true;
  textarea.rows = 50;
  textarea.style.cssText = 'width:100%; font-family:monospace; font-size:13px; padding:10px; border:1px solid #ccc; resize:vertical; margin-top: 20px;';

  var container = document.getElementById('prompt-container');
  var buttonContainer = document.getElementById('copy-button-container');
  buttonContainer.appendChild(copyButton);
  container.appendChild(textarea);
})();
</script>

---
"""


def escape_for_js_template_literal(text: str) -> str:
    """Escape text for safe embedding in a JS template literal (backtick string)."""
    text = text.replace("\\", "\\\\")   # backslashes first
    text = text.replace("`", "\\`")     # backticks
    text = text.replace("${", "\\${")   # template expressions
    return text


def build():
    source = SOURCE.read_text(encoding="utf-8")

    if BEGIN_PROMPT not in source:
        print(f"ERROR: '{BEGIN_PROMPT}' not found in {SOURCE}", file=sys.stderr)
        sys.exit(1)
    if END_PROMPT not in source:
        print(f"ERROR: '{END_PROMPT}' not found in {SOURCE}", file=sys.stderr)
        sys.exit(1)

    pre_prompt, rest = source.split(BEGIN_PROMPT, 1)
    prompt_part, tail_part = rest.split(END_PROMPT, 1)

    # Extract heading (first non-empty line before BEGIN PROMPT)
    heading = next((l for l in pre_prompt.splitlines() if l.strip()), "# Brian Thinks")

    prompt_escaped = escape_for_js_template_literal(prompt_part.strip())
    tail = tail_part.strip()

    page_header = PAGE_HEADER_TEMPLATE.replace("{heading}", heading)
    output = page_header + prompt_escaped + JS_FOOTER + tail + "\n"
    OUTPUT.write_text(output, encoding="utf-8")
    print(f"Built {OUTPUT} ({len(output.splitlines())} lines)")


if __name__ == "__main__":
    build()
