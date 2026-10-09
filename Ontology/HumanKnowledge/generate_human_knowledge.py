#!/usr/bin/env python3
"""Convert the Human Knowledge book outline into normalized browser data."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ENTRY = re.compile(r"^(\s+)([0-9]+(?:\.[0-9]+)*\.?|[A-Z](?:\.[0-9]+)*\.?)\s+(.+?)\s*$")


def parse_outline(text: str) -> list[dict]:
    outline = text.split("\nOutline\n", 1)[1].split("\n0. Prologue\n", 1)[0]
    roots: list[dict] = []
    stack: list[tuple[int, dict]] = []
    for line in outline.splitlines():
        match = ENTRY.match(line)
        if not match:
            continue
        indent, number, label = match.groups()
        node = {"id": f"hk-{number.rstrip('.').replace('.', '-')}", "label": f"{number} {label}", "children": []}
        level = len(indent.expandtabs(2))
        while stack and stack[-1][0] >= level:
            stack.pop()
        if stack:
            stack[-1][1]["children"].append(node)
        else:
            roots.append(node)
        stack.append((level, node))
    return roots


def flatten(roots: list[dict]) -> list[dict]:
    result: list[dict] = []

    def visit(node: dict) -> None:
        result.append({"id": node["id"], "label": node["label"], "children": [child["id"] for child in node["children"]], "alternateParents": []})
        for child in node["children"]:
            visit(child)

    for root in roots:
        visit(root)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    roots = parse_outline(args.source.read_text(encoding="utf-8", errors="replace"))
    nodes = flatten(roots)
    payload = {
        "source": {
            "name": "Human Knowledge: Foundations and Limits",
            "author": "Brian Holtz",
            "url": "https://humanknowledge.net/Thoughts/HumanKnowledge.txt",
        },
        "root": roots[0]["id"],
        "rootNodes": [root["id"] for root in roots],
        "stats": {
            "nodeCount": len(nodes),
            "definitionCount": 0,
            "projectedEdgeCount": sum(len(node["children"]) for node in nodes),
            "multipleParentNodeCount": 0,
            "unaryNodeCount": sum(len(node["children"]) == 1 for node in nodes),
        },
        "nodes": nodes,
    }
    args.output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(payload["stats"], indent=2))


if __name__ == "__main__":
    main()
