#!/usr/bin/env python3
"""Generate a browsable projection of the 1911 Roget conceptual hierarchy."""

from __future__ import annotations

import argparse
import html
import re
from collections import OrderedDict
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import urlopen


SOURCE_URL = "https://www.gutenberg.org/cache/epub/10681/pg10681-images.html"
Tree = OrderedDict[str, "Tree | None"]


class AnchorParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.active_id: str | None = None
        self.text: list[str] = []
        self.anchors: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "a":
            self.active_id = dict(attrs).get("id")
            self.text = []

    def handle_data(self, data: str) -> None:
        if self.active_id is not None:
            self.text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "a" and self.active_id is not None:
            self.anchors.append((self.active_id, " ".join("".join(self.text).split())))
            self.active_id = None


def clean(value: str) -> str:
    return " ".join(html.unescape(re.sub(r"<[^>]+>", "", value)).split())


def load_source(source: str) -> list[tuple[int, tuple[str, str, str], str]]:
    parser = AnchorParser()
    parser.feed(source)
    current = ["", "", ""]
    paths: dict[int, tuple[str, str, str]] = {}
    for anchor_id, text in parser.anchors:
        if anchor_id.startswith("CLASS_TITLE"):
            current = [text, "", ""]
        elif anchor_id.startswith("SECTION_TITLE"):
            current[1:] = [text, ""]
        elif anchor_id.startswith("SUBSECTION_TITLE"):
            current[2] = text
        elif match := re.fullmatch(r"link(\d+)", anchor_id):
            paths[int(match.group(1))] = tuple(current)

    starts = list(re.finditer(r'<a id="link(\d+)">#\1\.\s*</a>', source))
    titles: dict[int, str] = {}
    for index, match in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else len(source)
        body = source[match.end() : end]
        title_match = re.search(r"<b>(.*?)</b>", body, re.DOTALL)
        if title_match:
            titles[int(match.group(1))] = clean(title_match.group(1))

    records = [
        (number, paths[number], titles[number])
        for number in sorted(paths)
        if number in titles
    ]
    return records


def make_tree(records: list[tuple[int, tuple[str, str, str], str]]) -> Tree:
    tree: Tree = OrderedDict()
    for number, path, title in records:
        branch = tree
        for label in path:
            branch = branch.setdefault(label, OrderedDict())  # type: ignore[assignment]
        branch[f"{number:04d}. {title}"] = None
    return tree


def render_html(tree: Tree, concept_count: int, source_count: int) -> str:
    def searchable(mapping: Tree) -> str:
        values: list[str] = []
        for name, child in mapping.items():
            values.append(name)
            if child:
                values.append(searchable(child))
        return " ".join(values)

    def emit(mapping: Tree, path: tuple[str, ...], level: int) -> str:
        parts: list[str] = []
        for name, child in mapping.items():
            label = html.escape(name)
            full_path = html.escape(" / ".join(path + (name,)))
            search = html.escape(searchable(child) if child else name, quote=True)
            if child:
                question = html.escape(f"Is it related to {name.lower()}?")
                opened = " open" if level == 1 else ""
                parts.append(
                    f'<details class="node" data-search="{search}"{opened}>'
                    f"<summary>{label}</summary>"
                    f'<div class="question"><strong>Suggested question:</strong> '
                    f"{question}</div>"
                    f'<div class="path">{full_path}</div>'
                    f'<div class="children">{emit(child, path + (name,), level + 1)}</div>'
                    "</details>"
                )
            else:
                number = name.split(".", 1)[0]
                href = f"{SOURCE_URL}#link{int(number)}" if number.isdigit() else SOURCE_URL
                parts.append(
                    f'<div class="leaf" data-search="{search}">'
                    f'<a href="{href}" target="_blank" rel="noopener">{label}</a>'
                    f"<small>{full_path}</small></div>"
                )
        return "\n".join(parts)

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Roget's 1911 Conceptual Tree</title>
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
.children {{ border-left: 1px solid #8c959f; margin-left: 9px; padding-left: 8px; }}
.question {{ color: var(--muted); font-size: .94em; }}
.path, .leaf small {{ color: var(--muted); font-size: .82em; }}
.leaf {{ display: flex; gap: 12px; justify-content: space-between; padding: 3px 6px 3px 25px; }}
.leaf:hover {{ background: var(--panel); }}
[hidden] {{ display: none !important; }}
</style>
</head>
<body>
<h1>Roget's 1911 Conceptual Tree</h1>
<div class="intro">
  This is a browsable version of the 1911 edition of
  <a href="{SOURCE_URL}" target="_blank" rel="noopener">Roget's Thesaurus</a>.
  It contains {concept_count:,} numbered conceptual entries organized under
  Roget's classes, sections, and subsections. These are semantic word
  neighborhoods, not a scientifically normalized noun hierarchy; the page is
  provided as prior art for improving the curated 20 Questions tree.
  The source HTML contains {source_count:,} numbered concept anchors.
</div>
<div class="question"><strong>Opening question:</strong>
  Is the answer related to one of Roget's broad conceptual classes?</div>
<div class="controls">
  <input id="search" type="search" placeholder="Search concepts...">
  <button id="expand">Expand all</button>
  <button id="collapse">Collapse all</button>
</div>
<main id="tree">{emit(tree, (), 1)}</main>
<script>
const search = document.querySelector("#search");
search.addEventListener("input", () => {{
  const query = search.value.trim().toLowerCase();
  document.querySelectorAll(".node, .leaf").forEach((node) => {{
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
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path)
    parser.add_argument("--output", type=Path, default=Path("Rogets/index.html"))
    args = parser.parse_args()
    source = (
        args.source.read_text(encoding="utf-8")
        if args.source
        else urlopen(SOURCE_URL, timeout=60).read().decode("utf-8")
    )
    records = load_source(source)
    source_count = len(
        re.findall(r'<a id="link\d+">#\d+\.\s*</a>', source)
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        render_html(make_tree(records), len(records), source_count),
        encoding="utf-8",
    )
    print(f"wrote {args.output} with {len(records)} concepts")


if __name__ == "__main__":
    main()
