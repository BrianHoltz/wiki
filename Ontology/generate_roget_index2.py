#!/usr/bin/env python3
"""Generate a Roget-enriched review view of the curated v1 tree."""

from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path

import generate_20q_hierarchy


def normalize(value: str) -> str:
    return " ".join(re.sub(r"[^a-z0-9 ]+", " ", value.lower()).split())


def annotations(crosswalk: dict[str, object]) -> dict[tuple[str, ...], list[dict[str, object]]]:
    result: dict[tuple[str, ...], list[dict[str, object]]] = {}
    for concept in crosswalk["proposals"]:
        if concept["confidence"] != "high":
            continue
        title = normalize(concept["title"])
        aliases = [
            term
            for term in concept["noun_terms"]
            if term != title
            and re.fullmatch(r"[a-z][a-z -]{1,30}", term)
            and not any(token in term for token in (" c ", " adj", " 494", " 515"))
        ][:12]
        for match in concept["v1_matches"]:
            for location in match["v1_locations"]:
                if normalize(location["label"]) != title:
                    continue
                full_path = tuple(location["path"]) + (location["label"],)
                result.setdefault(full_path, []).append(
                    {
                        "number": concept["number"],
                        "title": concept["title"],
                        "aliases": aliases,
                        "url": concept["source_url"],
                    }
                )
    return result


def render(tree: generate_20q_hierarchy.Tree, crosswalk: dict[str, object]) -> str:
    notes = annotations(crosswalk)
    annotated = len(notes)

    def search_text(label: str, path: tuple[str, ...]) -> str:
        values = [label, *path]
        for note in notes.get(path + (label,), []):
            values.extend(note["aliases"])
            values.append(note["title"])
        return html.escape(" ".join(values), quote=True)

    def emit(mapping: generate_20q_hierarchy.Tree, path: tuple[str, ...], level: int) -> str:
        parts: list[str] = []
        for name, child in mapping.items():
            if name == "__question__":
                continue
            full_path = path + (name,)
            path_text = html.escape(" / ".join(full_path))
            if child:
                question = html.escape(child.get("__question__", "Is it related to this category?"))
                parts.append(
                    f'<details class="node" data-search="{search_text(name, path)}"'
                    f'{" open" if level == 1 else ""}>'
                    f"<summary>{html.escape(name.replace('_', ' '))}</summary>"
                    f'<div class="question"><strong>Suggested question:</strong> '
                    f"{question}</div>"
                    f'<div class="path">{path_text}</div>'
                    f'<div class="children">{emit(child, full_path, level + 1)}</div>'
                    "</details>"
                )
            else:
                notes_html = []
                for note in notes.get(full_path, []):
                    aliases = ", ".join(note["aliases"]) or "no additional familiar terms extracted"
                    notes_html.append(
                        f'<small class="roget">Roget #{note["number"]}: '
                        f'<a href="{note["url"]}" target="_blank" rel="noopener">'
                        f'{html.escape(note["title"])}</a>; related vocabulary: '
                        f"{html.escape(aliases)}</small>"
                    )
                parts.append(
                    f'<div class="leaf" data-search="{search_text(name, path)}">'
                    f"<span>{html.escape(name.replace('_', ' '))}</span>"
                    f"<small>{path_text}</small>{''.join(notes_html)}</div>"
                )
        return "\n".join(parts)

    body = emit(tree, (), 1)
    counts = crosswalk["counts"]
    root_question = html.escape(tree["__question__"])
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Curated 20 Questions Tree — Roget-Enriched Review</title>
<style>
:root {{ color-scheme: light dark; --accent: #2f6feb; --background: #ffffff; --text: #1f2328; --panel: #f6f8fa; --muted: #57606a; --border: #8c959f; --roget: #8250df; }}
@media (prefers-color-scheme: dark) {{
  :root {{ --background: #0d1117; --text: #e6edf3; --panel: #161b22; --muted: #8b949e; --border: #6e7681; --roget: #d2a8ff; }}
}}
body {{ color: var(--text); background: var(--background); font: 15px/1.45 system-ui, -apple-system, sans-serif; margin: 0 auto; max-width: 1150px; padding: 24px; }}
h1 {{ margin-bottom: 6px; }}
.intro, .question {{ background: var(--panel); border-left: 4px solid var(--accent); padding: 10px 14px; margin: 10px 0; }}
.review {{ border-left-color: var(--roget); }}
.controls {{ display: flex; gap: 8px; flex-wrap: wrap; margin: 18px 0; }}
input {{ color: var(--text); background: var(--panel); flex: 1 1 280px; padding: 9px; border: 1px solid var(--border); border-radius: 6px; }}
button {{ color: var(--text); background: var(--panel); padding: 9px 12px; border: 1px solid var(--border); border-radius: 6px; cursor: pointer; }}
details {{ margin: 4px 0 4px 12px; }}
summary {{ cursor: pointer; font-weight: 650; padding: 5px; }}
summary:hover {{ background: var(--panel); }}
.children {{ border-left: 1px solid #8c959f; margin-left: 9px; padding-left: 8px; }}
.question {{ color: var(--muted); font-size: .94em; }}
.path, .leaf small {{ color: var(--muted); font-size: .82em; }}
.leaf {{ display: flex; flex-wrap: wrap; gap: 12px; padding: 3px 6px 3px 25px; }}
.leaf:hover {{ background: var(--panel); }}
.leaf .roget {{ flex-basis: 100%; color: var(--roget); padding-left: 15px; }}
[hidden] {{ display: none !important; }}
</style>
</head>
<body>
<h1>Curated 20 Questions Tree — Roget-Enriched Review</h1>
<div class="intro">
  This keeps the original 628-leaf v1 game tree intact while adding only the
  high-confidence Roget tranche as review annotations and search vocabulary.
  It adds no new categories automatically. Roget anchors and related terms are
  shown in purple; review them for vocabulary discovery, sibling ideas,
  question wording, and abstract-branch coverage.
</div>
<div class="intro review">
  High-confidence Roget concepts: {counts["high_confidence_concepts"]:,}.
  Annotated v1 locations: {annotated:,}. The complete source browser is
  <a href="index.html">Rogets/index.html</a>; the full audit manifest is
  <a href="crosswalk.json">crosswalk.json</a>.
</div>
<div class="question"><strong>Opening question:</strong> {root_question}</div>
<div class="controls">
  <input id="search" type="search" placeholder="Search v1 labels or Roget vocabulary...">
  <button id="expand">Expand all</button>
  <button id="collapse">Collapse all</button>
</div>
<main id="tree">{body}</main>
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
    parser.add_argument("--crosswalk", type=Path, default=Path("Rogets/crosswalk.json"))
    parser.add_argument("--output", type=Path, default=Path("Rogets/index2.html"))
    args = parser.parse_args()
    crosswalk = json.loads(args.crosswalk.read_text(encoding="utf-8"))
    args.output.write_text(
        render(generate_20q_hierarchy.make_tree(), crosswalk),
        encoding="utf-8",
    )
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
