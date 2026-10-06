#!/usr/bin/env python3
"""Build a single-parent navigation projection of the official SUMO hierarchy."""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict, deque
from pathlib import Path

SUBCLASS_RE = re.compile(r"^\s*\(subclass\s+([^\s()]+)\s+([^\s()]+)\)")


def label(term: str) -> str:
    words = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", term)
    words = re.sub(r"([A-Za-z])([0-9])", r"\1 \2", words)
    return words.replace("_", " ")


def load_edges(source_dir: Path):
    edges = []
    order = {}
    for path in sorted(source_dir.glob("*.kif")):
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            match = SUBCLASS_RE.match(line)
            if not match:
                continue
            child, parent = match.groups()
            if child.startswith("?") or parent.startswith("?"):
                continue
            for term in (child, parent):
                order.setdefault(term, len(order))
            edges.append((child, parent))
    return list(dict.fromkeys(edges)), order


def build(source_dir: Path):
    edges, order = load_edges(source_dir)
    parents, children = defaultdict(set), defaultdict(set)
    for child, parent in edges:
        parents[child].add(parent)
        children[parent].add(child)

    root = "Entity"
    reachable = {root}
    queue = deque([root])
    while queue:
        parent = queue.popleft()
        for child in sorted(children[parent], key=lambda term: order[term]):
            if child not in reachable:
                reachable.add(child)
                queue.append(child)

    # The SUMO graph contains both a visually primary tree edge and longer
    # cross-links. KIF has no geometric edge lengths, so preserve declaration
    # order as the reproducible proxy for the PDF's primary edge ordering.
    selected, alternates = {}, {}
    for child in reachable - {root}:
        direct = [parent for parent in sorted(parents[child], key=lambda term: order[term])
                  if parent in reachable]
        if direct:
            selected[child] = direct[0]
            alternates[child] = direct[1:]

    projected = defaultdict(list)
    for child, parent in selected.items():
        projected[parent].append(child)
    for parent in projected:
        projected[parent].sort(key=lambda term: (label(term).lower(), term))

    nodes = []
    for term in sorted(reachable, key=lambda value: (value.lower(), value)):
        if term != root and term not in selected:
            continue
        nodes.append({
            "id": term,
            "label": label(term),
            "children": projected.get(term, []),
            "alternateParents": alternates.get(term, []),
            "directParentCount": len([p for p in parents[term] if p in reachable]),
        })

    unary = [node["id"] for node in nodes if len(node["children"]) == 1]
    return {
        "source": {
            "name": "Suggested Upper Merged Ontology (SUMO)",
            "repository": "https://github.com/ontologyportal/sumo",
            "root": root,
            "primaryEdgeHeuristic": (
                "Use the first direct subclass declaration as the primary "
                "tree edge; retain later direct parents as cross-links. "
                "This is a reproducible source-order proxy for the shorter "
                "primary edges in the SUMO graph PDF, not a graph-distance rule."
            ),
        },
        "stats": {
            "nodeCount": len(nodes),
            "projectedEdgeCount": len(selected),
            "multipleParentNodeCount": sum(bool(value) for value in alternates.values()),
            "unaryNodeCount": len(unary),
        },
        "root": root,
        "nodes": nodes,
        "unaryNodes": unary,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = build(args.source_dir)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, separators=(",", ":")), encoding="utf-8")
    print(json.dumps(result["stats"], indent=2))


if __name__ == "__main__":
    main()
