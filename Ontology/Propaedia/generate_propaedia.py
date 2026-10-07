#!/usr/bin/env python3
"""Build a collapsible browser for the Propædia Outline of Knowledge.

The checked-in source.html is the downloaded Wikipedia article whose outline
reproduces the public description of the 15th-edition Propædia. The generator
keeps the numbered part/division/section labels and does not invent a new
knowledge hierarchy.
"""

from __future__ import annotations

import argparse
import html
import json
import re
from collections import OrderedDict
from html.parser import HTMLParser
from pathlib import Path
from typing import Any


class OutlineParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.heading: list[str] = []
        self.heading_active = False
        self.current_part: str | None = None
        self.parts: OrderedDict[str, list[dict[str, Any]]] = OrderedDict()
        self.frames: list[dict[str, Any]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "h4":
            self.heading = []
            self.heading_active = True
        elif tag == "li":
            self.frames.append({"text": [], "children": []})

    def handle_endtag(self, tag: str) -> None:
        if tag == "h4" and self.heading_active:
            heading = " ".join("".join(self.heading).split())
            self.current_part = heading
            self.parts.setdefault(heading, [])
            self.heading_active = False
        elif tag == "li" and self.frames:
            frame = self.frames.pop()
            label = " ".join("".join(frame["text"]).split())
            node = {"label": label, "children": frame["children"]}
            if self.frames:
                self.frames[-1]["children"].append(node)
            elif self.current_part and re.match(r"^\d+(?:\.\d+)+\b", label):
                self.parts[self.current_part].append(node)

    def handle_data(self, data: str) -> None:
        if self.heading_active:
            self.heading.append(data)
        elif self.frames:
            self.frames[-1]["text"].append(data)


def tree_from_parts(parts: OrderedDict[str, list[dict[str, Any]]]) -> OrderedDict[str, Any]:
    tree: OrderedDict[str, Any] = OrderedDict()
    tree["__question__"] = "Which broad part of human knowledge is it related to?"
    for part, entries in parts.items():
        branch: OrderedDict[str, Any] = OrderedDict()
        branch["__question__"] = f"Is it related to {part.lower()}?"

        def add(parent: OrderedDict[str, Any], entry: dict[str, Any]) -> None:
            children = entry["children"]
            if not children:
                parent[entry["label"]] = None
                return
            child_tree: OrderedDict[str, Any] = OrderedDict()
            child_tree["__question__"] = f"Is it related to {entry['label'].lower()}?"
            for child in children:
                add(child_tree, child)
            parent[entry["label"]] = child_tree

        for entry in entries:
            add(branch, entry)
        tree[part] = branch
    return tree


def count_nodes(tree: OrderedDict[str, Any]) -> tuple[int, int]:
    branches = leaves = 0
    for key, child in tree.items():
        if key == "__question__":
            continue
        if child:
            branches += 1
            child_branches, child_leaves = count_nodes(child)
            branches += child_branches
            leaves += child_leaves
        else:
            leaves += 1
    return branches, leaves


def render_html(tree: OrderedDict[str, Any], branches: int, leaves: int) -> str:
    def searchable(mapping: OrderedDict[str, Any]) -> str:
        values: list[str] = []
        for key, child in mapping.items():
            if key == "__question__":
                continue
            values.append(key)
            if child:
                values.append(searchable(child))
        return " ".join(values)

    def emit(mapping: OrderedDict[str, Any], path: tuple[str, ...], level: int) -> str:
        parts: list[str] = []
        for name, child in mapping.items():
            if name == "__question__":
                continue
            path_text = html.escape(" / ".join(path + (name,)))
            if child:
                question = html.escape(child["__question__"])
                search = html.escape(searchable(child), quote=True)
                opened = " open" if level == 1 else ""
                parts.append(
                    f'<details class="node" data-search="{search}"{opened}>'
                    f"<summary>{html.escape(name)}</summary>"
                    f'<div class="question"><strong>Suggested question:</strong> '
                    f"{question}</div>"
                    f'<div class="path">{path_text}</div>'
                    f'<div class="children">{emit(child, path + (name,), level + 1)}</div>'
                    "</details>"
                )
            else:
                parts.append(
                    f'<div class="leaf" data-search="{html.escape(name.lower(), quote=True)}">'
                    f"<span>{html.escape(name)}</span><small>{path_text}</small></div>"
                )
        return "\n".join(parts)

    body = emit(tree, (), 1)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Propædia Outline of Knowledge</title>
<style>
:root {{ color-scheme: light dark; --accent: #2f6feb; --background: #ffffff; --text: #1f2328; --panel: #f6f8fa; --muted: #57606a; --border: #8c959f; }}
@media (prefers-color-scheme: dark) {{
  :root {{ --background: #0d1117; --text: #e6edf3; --panel: #161b22; --muted: #8b949e; --border: #6e7681; }}
}}
body {{ color: var(--text); background: var(--background); font: 15px/1.45 system-ui, -apple-system, sans-serif; margin: 0 auto; max-width: 1150px; padding: 24px; }}
h1 {{ margin-bottom: 6px; }}
.intro, .question {{ background: var(--panel); border-left: 4px solid var(--accent); padding: 10px 14px; margin: 10px 0; }}
.controls {{ display: flex; gap: 8px; flex-wrap: wrap; margin: 18px 0; }}
input {{ color: var(--text); background: var(--panel); flex: 1 1 280px; padding: 9px; border: 1px solid var(--border); border-radius: 6px; }}
button {{ color: var(--text); background: var(--panel); padding: 9px 12px; border: 1px solid var(--border); border-radius: 6px; cursor: pointer; }}
details {{ margin: 4px 0 4px 12px; }}
summary {{ cursor: pointer; font-weight: 650; padding: 5px; }}
summary:hover {{ background: var(--panel); }}
.children {{ border-left: 1px solid var(--border); margin-left: 9px; padding-left: 8px; }}
.question, .path, .leaf small {{ color: var(--muted); font-size: .9em; }}
.leaf {{ display: flex; gap: 12px; justify-content: space-between; padding: 3px 6px 3px 25px; }}
.leaf:hover {{ background: var(--panel); }}
[hidden] {{ display: none !important; }}
</style>
</head>
<body>
<h1>Propædia Outline of Knowledge</h1>
<div class="intro">
  This is a browseable rendering of the public
  <a href="https://en.wikipedia.org/wiki/Propaedia" target="_blank" rel="noopener">Outline of Knowledge</a>
  for the one-volume Propædia in the 15th edition of Encyclopaedia Britannica.
  It contains {branches:,} display branches and {leaves:,} terminal outline
  topics. It is a topical framework for an encyclopedia, not a noun taxonomy.
  The downloaded source and parser are included beside this page.
</div>
<div class="question"><strong>Opening question:</strong>
  {html.escape(tree["__question__"])}</div>
<div class="controls">
  <input id="search" type="search" placeholder="Search topics...">
  <button id="expand">Expand all</button>
  <button id="collapse">Collapse all</button>
</div>
<main id="tree">{body}</main>
<script>
const all = () => [...document.querySelectorAll(".node, .leaf")];
const search = document.querySelector("#search");
search.addEventListener("input", () => {{
  const query = search.value.trim().toLowerCase();
  all().forEach((node) => {{
    const match = !query || node.dataset.search.toLowerCase().includes(query);
    node.hidden = !match;
    if (match && node.classList.contains("node") && query) node.open = true;
  }});
}});
document.querySelector("#expand").onclick = () => document.querySelectorAll(".node").forEach(n => n.open = true);
document.querySelector("#collapse").onclick = () => document.querySelectorAll(".node").forEach(n => n.open = false);
</script>
</body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path("source.html"))
    parser.add_argument("--output", type=Path, default=Path("index.html"))
    parser.add_argument("--json-output", type=Path, default=Path("outline.json"))
    args = parser.parse_args()

    parser_instance = OutlineParser()
    parser_instance.feed(args.source.read_text(encoding="utf-8"))
    tree = tree_from_parts(parser_instance.parts)
    branches, leaves = count_nodes(tree)
    args.output.write_text(render_html(tree, branches, leaves), encoding="utf-8")
    args.json_output.write_text(
        json.dumps({"parts": parser_instance.parts}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "parts": len(parser_instance.parts),
        "branches": branches,
        "leaves": leaves,
        "nodes": branches + leaves,
    }, indent=2))


if __name__ == "__main__":
    main()
