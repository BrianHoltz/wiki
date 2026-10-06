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


def build(source_dir: Path, pdf_edges: Path | None = None):
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

    measured = {}
    if pdf_edges:
        measured = json.loads(
            pdf_edges.read_text(encoding="utf-8")
        ).get("primaryParents", {})
    selected, alternates = {}, {}
    for child in reachable - {root}:
        direct = [parent for parent in sorted(parents[child], key=lambda term: order[term])
                  if parent in reachable]
        if direct:
            pdf_parent = measured.get(child, {}).get("parent")
            if pdf_parent in direct:
                selected[child] = pdf_parent
                alternates[child] = [parent for parent in direct if parent != pdf_parent]
            else:
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
                "Where the Ontology4 PDF contains the node, choose the "
                "shortest measured blue directed arc among its direct SUMO "
                "parents; otherwise use the first direct subclass declaration. "
                "All non-primary direct parents remain as cross-links."
            ),
            "pdfEdgeSource": (
                "https://www.ontology4.us/download/dot/SumoOntology.pdf"
                if pdf_edges else None
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


def build_pdf(pdf_graph: Path):
    graph = json.loads(pdf_graph.read_text(encoding="utf-8"))
    nodes = set(graph["nodes"])
    incoming = defaultdict(list)
    for edge in graph["edges"]:
        nodes.update((edge["parent"], edge["child"]))
        incoming[edge["child"]].append(edge)

    selected, alternates = {}, {}
    for child, edges in incoming.items():
        ordered = sorted(edges, key=lambda edge: (edge["length"], edge["parent"]))
        selected[child] = ordered[0]["parent"]
        alternates[child] = [edge["parent"] for edge in ordered[1:]]

    projected = defaultdict(list)
    for child, parent in selected.items():
        projected[parent].append(child)
    for parent in projected:
        projected[parent].sort(key=lambda term: (label(term).lower(), term))

    roots = sorted(nodes - set(selected), key=lambda term: (term != "Entity", label(term).lower(), term))
    records = [
        {
            "id": term,
            "label": label(term),
            "children": projected.get(term, []),
            "alternateParents": alternates.get(term, []),
            "directParentCount": len(incoming.get(term, [])),
        }
        for term in sorted(nodes, key=lambda value: (value.lower(), value))
    ]
    unary = [record["id"] for record in records if len(record["children"]) == 1]
    return {
        "source": {
            "name": "Suggested Upper Merged Ontology (SUMO), Ontology4 PDF graph",
            "pdf": graph["sourcePdf"],
            "primaryEdgeHeuristic": (
                "For every PDF node with multiple incoming arcs, remove the "
                "longest measured incoming arc repeatedly until one primary "
                "parent remains. Retain removed parents as cross-links."
            ),
        },
        "stats": {
            "nodeCount": len(records),
            "projectedEdgeCount": len(selected),
            "multipleParentNodeCount": sum(bool(value) for value in alternates.values()),
            "unaryNodeCount": len(unary),
            "rootCount": len(roots),
            "pdfEdgeCount": graph["edgeCount"],
        },
        "root": "Entity",
        "rootNodes": roots,
        "nodes": records,
        "unaryNodes": unary,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path)
    parser.add_argument("--pdf-edges", type=Path)
    parser.add_argument("--pdf-graph", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.pdf_graph:
        result = build_pdf(args.pdf_graph)
    elif args.source_dir:
        result = build(args.source_dir, args.pdf_edges)
    else:
        parser.error("one of --source-dir or --pdf-graph is required")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, separators=(",", ":")), encoding="utf-8")
    print(json.dumps(result["stats"], indent=2))


if __name__ == "__main__":
    main()
