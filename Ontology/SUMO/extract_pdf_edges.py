#!/usr/bin/env python3
"""Extract measured primary-parent candidates from the Ontology4 SUMO PDF.

The PDF is converted to SVG and pdftotext -bbox output before this script runs:
  pdftocairo -svg SumoOntology.pdf SumoOntology.svg
  pdftotext -bbox SumoOntology.pdf SumoOntology-bbox.html
"""

from __future__ import annotations

import argparse
import html
import json
import math
import re
from collections import defaultdict
from pathlib import Path

WORD_RE = re.compile(
    r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>'
)
PATH_RE = re.compile(
    r'<path fill="none"[^>]*stroke="rgb\(0%, 0%, 100%\)"[^>]*d="([^"]+)"'
)
NUMBER_RE = re.compile(r"-?\d+(?:\.\d+)?")


def load_terms(source_dir: Path) -> tuple[set[str], dict[str, int]]:
    pattern = re.compile(r"^\s*\(subclass\s+([^\s()]+)\s+([^\s()]+)\)")
    terms, order = set(), {}
    for path in sorted(source_dir.glob("*.kif")):
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            match = pattern.match(line)
            if not match:
                continue
            for term in match.groups():
                if not term.startswith("?"):
                    terms.add(term)
                    order.setdefault(term, len(order))
    return terms, order


def load_labels(bbox: Path, terms: set[str], page_height: float):
    labels = []
    for match in WORD_RE.finditer(bbox.read_text(encoding="utf-8", errors="replace")):
        x1, y1, x2, y2, raw = match.groups()
        raw = html.unescape(raw)
        if raw[:1] in "^°.>~":
            term = raw[1:]
        else:
            continue
        if term in terms:
            labels.append(
                (term, (float(x1) + float(x2)) / 2,
                 page_height - (float(y1) + float(y2)) / 2)
            )
    return labels


def curve_points(path_data: str):
    numbers = [float(value) for value in NUMBER_RE.findall(path_data)]
    if len(numbers) < 8:
        return []
    points = [(numbers[0], numbers[1])]
    for index in range(2, len(numbers), 6):
        if index + 5 >= len(numbers):
            break
        start = points[-1]
        control_one = (numbers[index], numbers[index + 1])
        control_two = (numbers[index + 2], numbers[index + 3])
        end = (numbers[index + 4], numbers[index + 5])
        for step in range(1, 21):
            t = step / 20
            inverse = 1 - t
            points.append((
                inverse**3 * start[0]
                + 3 * inverse**2 * t * control_one[0]
                + 3 * inverse * t**2 * control_two[0]
                + t**3 * end[0],
                inverse**3 * start[1]
                + 3 * inverse**2 * t * control_one[1]
                + 3 * inverse * t**2 * control_two[1]
                + t**3 * end[1],
            ))
    return points


def nearest_label(point, labels):
    return min(labels, key=lambda item: (item[1] - point[0]) ** 2 + (item[2] - point[1]) ** 2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--svg", type=Path, required=True)
    parser.add_argument("--bbox", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--page-height", type=float, default=11643)
    args = parser.parse_args()

    terms, order = load_terms(args.source_dir)
    labels = load_labels(args.bbox, terms, args.page_height)
    parents = defaultdict(set)
    pattern = re.compile(r"^\s*\(subclass\s+([^\s()]+)\s+([^\s()]+)\)")
    for path in sorted(args.source_dir.glob("*.kif")):
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            match = pattern.match(line)
            if match and not any(term.startswith("?") for term in match.groups()):
                child, parent = match.groups()
                parents[child].add(parent)

    candidates = {}
    for path_data in PATH_RE.findall(args.svg.read_text(encoding="utf-8", errors="replace")):
        points = curve_points(path_data)
        if not points:
            continue
        source = nearest_label(points[0], labels)
        target = nearest_label(points[-1], labels)
        if source[0] == target[0] or source[0] not in parents[target[0]]:
            continue
        if math.dist(points[0], source[1:]) > 180 or math.dist(points[-1], target[1:]) > 180:
            continue
        length = sum(math.dist(a, b) for a, b in zip(points, points[1:]))
        current = candidates.get(target[0])
        if current is None or length < current["length"]:
            candidates[target[0]] = {
                "parent": source[0],
                "length": round(length, 3),
            }

    result = {
        "sourcePdf": "https://www.ontology4.us/download/dot/SumoOntology.pdf",
        "method": "Shortest measured blue directed PDF arc among direct SUMO parents",
        "candidateCount": len(candidates),
        "primaryParents": candidates,
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"candidateCount": len(candidates)}, indent=2))


if __name__ == "__main__":
    main()
