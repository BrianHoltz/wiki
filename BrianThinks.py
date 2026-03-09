#!/usr/bin/env python3
"""
Build BrianThinksManually.md from BrianThinksTemplate.md and BrianThinks.md.

BrianThinks.md format:
  Line 1: heading (ignored — template supplies the page heading)
  Lines 2–N: prompt content
  ## Credits: who to know  <- everything from here onward is omitted

BrianThinksTemplate.md contains the string "## BrianThoughts" as a
placeholder inside the JS promptText template literal. That placeholder
is replaced with the (JS-escaped) prompt content extracted above.
"""

import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
THOUGHTS = HERE / "BrianThinks.md"
TEMPLATE = HERE / "BrianThinksTemplate.md"
OUTPUT = HERE / "BrianThinksManually.md"

PLACEHOLDER = "## BrianThoughts"
CREDITS_HEADING = "## Credits"


def escape_for_js_template_literal(text: str) -> str:
    """Escape text for safe embedding in a JS template literal (backtick string)."""
    text = text.replace("\\", "\\\\")   # backslashes first
    text = text.replace("`", "\\`")     # backticks
    text = text.replace("${", "\\${")   # template expressions
    return text


def build():
    template = TEMPLATE.read_text(encoding="utf-8")
    thoughts = THOUGHTS.read_text(encoding="utf-8")

    if PLACEHOLDER not in template:
        print(f"ERROR: '{PLACEHOLDER}' not found in {TEMPLATE}", file=sys.stderr)
        sys.exit(1)

    # Drop heading (line 1) and everything from ## Credits onward
    lines = thoughts.splitlines()[1:]
    for i, line in enumerate(lines):
        if line.startswith(CREDITS_HEADING):
            lines = lines[:i]
            break

    prompt_text = "\n".join(lines).strip()
    prompt_text = re.sub(r'\*\*', '', prompt_text)  # strip bold markers for plain-text prompt
    prompt_escaped = escape_for_js_template_literal(prompt_text)

    output = template.replace(PLACEHOLDER, prompt_escaped, 1)
    OUTPUT.write_text(output, encoding="utf-8")
    print(f"Built {OUTPUT} ({len(output.splitlines())} lines)")


if __name__ == "__main__":
    build()
