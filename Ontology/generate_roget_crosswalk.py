#!/usr/bin/env python3
"""Create a reviewable Roget-to-curated-v1 crosswalk."""

from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path
from urllib.request import urlopen

import generate_20q_hierarchy
import generate_roget_20q


SOURCE_URL = generate_roget_20q.SOURCE_URL


def normalize(value: str) -> str:
    value = html.unescape(value).lower().replace("_", " ")
    value = re.sub(r"[^a-z0-9 ]+", " ", value)
    return " ".join(value.split())


def v1_leaves() -> dict[str, list[dict[str, object]]]:
    result: dict[str, list[dict[str, object]]] = {}

    def walk(tree: generate_20q_hierarchy.Tree, path: tuple[str, ...]) -> None:
        for label, child in tree.items():
            if label == "__question__":
                continue
            if child:
                walk(child, path + (label,))
            else:
                result.setdefault(normalize(label), []).append(
                    {"label": label, "path": path}
                )

    walk(generate_20q_hierarchy.make_tree(), ())
    return result


def concept_chunks(source: str) -> list[tuple[int, str]]:
    starts = list(re.finditer(r'<a id="link(\d+)">#\1\.\s*</a>', source))
    return [
        (
            int(match.group(1)),
            source[
                match.end() : starts[index + 1].start()
                if index + 1 < len(starts)
                else len(source)
            ],
        )
        for index, match in enumerate(starts)
    ]


def noun_terms(number: int, body: str) -> list[str]:
    marker = re.search(rf'<a id="link{number}N\.">N\.</a>', body)
    if not marker:
        return []
    end = re.search(rf'<a id="link{number}(?:V|Adj|Adv|Phr)\.">', body[marker.end() :])
    text = body[marker.end() : marker.end() + end.start() if end else None]
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\[[^\]]*\]", " ", html.unescape(text))
    terms: list[str] = []
    for raw in re.split(r"[;,]", text):
        term = normalize(raw)
        if term and term not in {"n", "adj", "v", "adv", "phr"} and len(term) <= 60:
            terms.append(term)
    return list(dict.fromkeys(terms))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path)
    parser.add_argument("--output", type=Path, default=Path("Rogets/crosswalk.json"))
    args = parser.parse_args()
    source = (
        args.source.read_text(encoding="utf-8")
        if args.source
        else urlopen(SOURCE_URL, timeout=60).read().decode("utf-8")
    )
    records = generate_roget_20q.load_source(source)
    paths = {number: path for number, path, _ in records}
    titles = {number: title for number, _, title in records}
    leaves = v1_leaves()
    proposals: list[dict[str, object]] = []
    concepts: list[dict[str, object]] = []

    for number, body in concept_chunks(source):
        title = titles[number]
        terms = noun_terms(number, body)
        matches: dict[str, dict[str, object]] = {}
        for evidence, candidate in [("title", normalize(title)), *[("noun_list", term) for term in terms]]:
            if candidate in leaves:
                matches[candidate] = {
                    "label": candidate,
                    "v1_locations": [
                        {
                            "label": location["label"],
                            "path": location["path"],
                        }
                        for location in leaves[candidate]
                    ],
                    "evidence": evidence,
                }
        confidence = "high" if normalize(title) in leaves else "medium" if matches else "none"
        concept = {
            "number": number,
            "title": title,
            "roget_path": paths[number],
            "source_url": f"{SOURCE_URL}#link{number}",
            "noun_terms": terms,
            "v1_matches": list(matches.values()),
            "confidence": confidence,
        }
        concepts.append(concept)
        if matches:
            proposals.append(concept)

    counts = {
        "roget_concepts": len(concepts),
        "curated_v1_leaves": sum(len(locations) for locations in leaves.values()),
        "concepts_with_exact_matches": len(proposals),
        "high_confidence_concepts": sum(c["confidence"] == "high" for c in concepts),
        "medium_confidence_concepts": sum(c["confidence"] == "medium" for c in concepts),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(
            {
                "source": SOURCE_URL,
                "target": "curated v1 tree",
                "method": "Exact normalized title or noun-list phrase matches only; all proposals require review.",
                "counts": counts,
                "proposals": proposals,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    print(json.dumps(counts, sort_keys=True))


if __name__ == "__main__":
    main()
