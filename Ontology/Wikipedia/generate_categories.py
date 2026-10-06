#!/usr/bin/env python3
"""Build a bounded static browser dataset from Wikimedia's category RDF dump.

The complete English Wikipedia category graph is a cyclic, multi-parent graph
with roughly two million categories reachable from the navigation roots. A
bounded snapshot keeps the browser static and usable while retaining links to
the live category pages for deeper exploration.
"""

from __future__ import annotations

import argparse
import gzip
import json
import re
import sqlite3
import tempfile
from pathlib import Path
from urllib.parse import unquote


URI = re.compile(r"<https://en\.wikipedia\.org/wiki/Category:([^>]+)>")
DEFAULT_ROOTS = ("Category:Main topic classifications", "Category:Contents")
DEFAULT_SOURCE = (
    "https://dumps.wikimedia.org/other/categoriesrdf/latest/"
    "enwiki-20261003-categories.ttl.gz"
)


def category_name(encoded: str) -> str:
    return "Category:" + unquote(encoded).replace("_", " ")


def load_edges(dump: Path, database: Path) -> None:
    connection = sqlite3.connect(database)
    connection.execute("PRAGMA journal_mode=OFF")
    connection.execute("PRAGMA synchronous=OFF")
    connection.execute("CREATE TABLE edge(child TEXT NOT NULL, parent TEXT NOT NULL)")
    connection.execute("CREATE INDEX edge_parent ON edge(parent)")
    subject: str | None = None
    collecting = False
    rows: list[tuple[str, str]] = []
    with gzip.open(dump, "rt", encoding="utf-8", errors="replace") as source:
        for line in source:
            if line.startswith("<https://en.wikipedia.org/wiki/Category:"):
                match = URI.match(line)
                subject = category_name(match.group(1)) if match else None
                collecting = False
            if not subject:
                continue
            if "mediawiki:isInCategory" in line:
                collecting = True
            if not collecting:
                continue
            for match in URI.finditer(line):
                parent = category_name(match.group(1))
                if parent != subject:
                    rows.append((subject, parent))
            if line.rstrip().endswith("."):
                collecting = False
            if len(rows) >= 50_000:
                connection.executemany("INSERT INTO edge VALUES (?, ?)", rows)
                connection.commit()
                rows.clear()
    if rows:
        connection.executemany("INSERT INTO edge VALUES (?, ?)", rows)
    connection.commit()
    connection.close()


def build_snapshot(
    database: Path,
    roots: tuple[str, ...],
    max_depth: int,
    source_url: str,
) -> dict[str, object]:
    connection = sqlite3.connect(database)
    connection.execute("CREATE TEMP TABLE roots(name TEXT PRIMARY KEY)")
    connection.executemany("INSERT INTO roots VALUES (?)", ((root,) for root in roots))
    rows = connection.execute(
        """
        WITH RECURSIVE reach(name, depth) AS (
          SELECT name, 0 FROM roots
          UNION
          SELECT edge.child, reach.depth + 1
          FROM edge JOIN reach ON edge.parent = reach.name
          WHERE reach.depth < ?
        )
        SELECT name, MIN(depth) FROM reach GROUP BY name
        """,
        (max_depth,),
    ).fetchall()
    depths = {name: depth for name, depth in rows}
    children: dict[str, list[str]] = {name: [] for name in depths}
    connection.execute("CREATE TEMP TABLE included(name TEXT PRIMARY KEY)")
    connection.executemany("INSERT INTO included VALUES (?)", ((name,) for name in depths))
    for child, parent in connection.execute(
        """
        SELECT edge.child, edge.parent
        FROM edge JOIN included ON edge.parent = included.name
        """,
    ):
        if child in depths:
            children[parent].append(child)
    connection.close()
    categories = {}
    for name, depth in sorted(depths.items(), key=lambda item: (item[1], item[0])):
        child_names = sorted(set(children[name]))
        categories[name] = {
            "depth": depth,
            "children": child_names,
            "truncated": False,
        }
    # A category at the boundary is truncated when the source has any child
    # outside the snapshot; this second query avoids storing the full graph.
    connection = sqlite3.connect(database)
    for name, record in categories.items():
        if record["depth"] != max_depth:
            record["truncated"] = False
            continue
        record["truncated"] = connection.execute(
            "SELECT 1 FROM edge WHERE parent = ? LIMIT 1", (name,)
        ).fetchone() is not None
    connection.close()
    return {
        "snapshot": {
            "source": source_url,
            "roots": list(roots),
            "max_depth": max_depth,
            "category_count": len(categories),
            "edge_count": sum(len(record["children"]) for record in categories.values()),
        },
        "roots": list(roots),
        "categories": categories,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dump", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("categories.json"))
    parser.add_argument("--max-depth", type=int, default=5)
    parser.add_argument("--source-url", default=DEFAULT_SOURCE)
    args = parser.parse_args()
    with tempfile.NamedTemporaryFile(suffix=".sqlite3") as temporary:
        load_edges(args.dump, Path(temporary.name))
        snapshot = build_snapshot(
            Path(temporary.name),
            DEFAULT_ROOTS,
            args.max_depth,
            args.source_url,
        )
    args.output.write_text(
        json.dumps(snapshot, ensure_ascii=False, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(snapshot["snapshot"], indent=2))


if __name__ == "__main__":
    main()
