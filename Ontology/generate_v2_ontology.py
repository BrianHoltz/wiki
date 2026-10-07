#!/usr/bin/env python3
"""Build the reviewed v2 profile from the v1 spine and WordNet candidates.

The v2 page keeps the hand-curated v1 top-level organization and adds:

* a small reviewed set of notable evolutionary examples; and
* a deterministic, source-labelled WordNet candidate layer sized for a
  one-page 5K-10K experiment.

WordNet candidates are enrichment proposals, not claims of scientific
taxonomy. Biological placement is validated by the reviewed seed layer and is
intended to be replaced or checked against a declared biological release.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import OrderedDict
from functools import lru_cache
from pathlib import Path
from typing import Any

from generate_20q_hierarchy import (
    Tree,
    branch,
    leaves,
    make_tree as make_v1_tree,
    render_html as render_v1_html,
    render_yaml as render_v1_yaml,
)
from generate_wordnet_20q import (
    choose_synsets,
    display_name,
    make_projection,
    score,
)


REVIEWED_SEEDS = {
    "marsupials_and_monotremes": {
        "parent": "Physical / Living / Animal / Vertebrate / Mammal",
        "question": "Is it a marsupial or a monotreme?",
        "source": "Open Tree of Life and Catalogue of Life review seed",
        "entries": [
            "wallaby", "wombat", "opossum", "Tasmanian devil",
            "platypus", "echidna", "bandicoot", "bilby",
        ],
    },
    "lobe_finned_and_unusual_fish": {
        "parent": "Physical / Living / Animal / Vertebrate / Fish",
        "question": "Is it an ancient lineage or an unusual fish form?",
        "source": "Open Tree of Life and Catalogue of Life review seed",
        "entries": [
            "coelacanth", "lungfish", "sturgeon", "gar", "arapaima",
            "mudskipper", "hagfish", "lamprey",
        ],
    },
    "ancient_and_unusual_reptiles": {
        "parent": "Physical / Living / Animal / Vertebrate / Reptile and amphibian",
        "question": "Is it an ancient, giant, or unusually adapted reptile?",
        "source": "Open Tree of Life and Catalogue of Life review seed",
        "entries": [
            "tuatara", "komodo dragon", "chameleon", "gecko", "iguana",
            "anaconda", "boa constrictor", "crocodile", "turtle",
        ],
    },
    "convergent_invertebrates": {
        "parent": "Physical / Living / Animal / Invertebrate",
        "question": "Does it show an unusual body plan or convergent adaptation?",
        "source": "Open Tree of Life and Catalogue of Life review seed",
        "entries": [
            "horseshoe crab", "nautilus", "chambered nautilus", "mantis shrimp",
            "tardigrade", "velvet worm", "dragon millipede",
        ],
    },
    "extinct_life": {
        "parent": "Physical / Living / Animal",
        "question": "Is it an extinct organism or major deep-time group?",
        "source": "Open Tree of Life and Catalogue of Life review seed",
        "entries": [
            "dinosaur", "tyrannosaurus", "triceratops", "stegosaurus",
            "brontosaurus", "sauropod", "pterosaur", "trilobite",
            "ammonite", "woolly mammoth", "saber-toothed cat",
            "early tetrapod",
        ],
    },
    "convergent_plants": {
        "parent": "Physical / Living / Plant",
        "question": "Is it a plant with a convergent form or unusual adaptation?",
        "source": "Open Tree of Life and Catalogue of Life review seed",
        "entries": [
            "euphorbia", "welwitschia", "venus flytrap", "pitcher plant",
            "carnivorous plant", "mangrove", "giant sequoia",
        ],
    },
}

NCBI_RANKS = {
    "superkingdom", "kingdom", "phylum", "class", "order", "family",
    "genus", "species",
}
NCBI_LIFE_ROOTS = {"2", "2157", "2759"}


def find_path(tree: Tree, path: list[str]) -> Tree:
    current = tree
    for key in path:
        actual_key = key if key in current else key.replace(" ", "_")
        child = current[actual_key]
        if child is None:
            raise KeyError("Cannot descend through leaf: " + " / ".join(path))
        current = child
    return current


def add_reviewed_seeds(tree: Tree) -> None:
    for seed in REVIEWED_SEEDS.values():
        path = seed["parent"].split(" / ")
        parent = find_path(tree, path)
        label = seed["key"] if "key" in seed else next(
            key for key, value in REVIEWED_SEEDS.items() if value is seed
        )
        parent[label.replace("_", " ").title()] = branch(
            seed["question"], leaves(*seed["entries"])
        )


def classify(synset: Any) -> str:
    names = {ancestor.name() for path in synset.hypernym_paths() for ancestor in path}
    if names & {
        "animal.n.01", "plant.n.02", "fungus.n.01", "microorganism.n.01",
        "bacterium.n.01", "virus.n.01", "protist.n.01",
    }:
        return "biological"
    if names & {"artifact.n.01", "instrumentality.n.03", "structure.n.01"}:
        return "artifacts"
    if names & {
        "location.n.01", "object.n.01", "natural_object.n.01",
        "substance.n.07", "phenomenon.n.01",
    }:
        return "natural-and-places"
    return "abstract-and-social"


def source_subtree(nodes: set[Any], children: dict[Any, list[Any]]) -> Tree:
    roots = sorted(
        (
            node for node in nodes
            if not any(parent in nodes for parent in node.hypernyms())
        ),
        key=lambda node: (display_name(node).lower(), node.name()),
    )
    result: Tree = OrderedDict()
    result["__question__"] = "Is it a kind of this WordNet candidate category?"
    used: set[str] = set()

    def add(node: Any) -> tuple[str, Tree | None]:
        base = node.lemma_names()[0].replace("_", " ")
        label = base
        if label in used:
            label = display_name(node)
        used.add(label)
        descendants = [child for child in children.get(node, []) if child in nodes]
        descendants.sort(key=lambda item: (display_name(item).lower(), item.name()))
        if not descendants:
            return label, None
        branch_node: Tree = OrderedDict()
        branch_node["__question__"] = f"Is it a kind of {base}?"
        for child in descendants:
            child_label, child_tree = add(child)
            branch_node[child_label] = child_tree
        return label, branch_node

    for root in roots:
        label, subtree = add(root)
        result[label] = subtree
    return result


def add_wordnet_candidates(tree: Tree, target: int) -> dict[str, Any]:
    selected, _ = choose_synsets(target)
    children, _ = make_projection(selected)
    groups: dict[str, set[Any]] = {
        "biological": set(),
        "artifacts": set(),
        "natural-and-places": set(),
        "abstract-and-social": set(),
    }
    for synset in selected:
        if synset.name() == "entity.n.01":
            continue
        groups[classify(synset)].add(synset)

    destinations = {
        "biological": ["Physical", "Living"],
        "artifacts": ["Physical", "Artifact"],
        "natural-and-places": ["Physical", "Natural substance"],
        "abstract-and-social": ["Abstract"],
    }
    counts: dict[str, Any] = {"selected_source_synsets": len(selected), "groups": {}}
    for name, nodes in groups.items():
        if not nodes:
            continue
        parent = find_path(tree, destinations[name])
        label = "WordNet candidate expansion"
        if label in parent:
            label = f"WordNet {name} candidates"
        parent[label] = source_subtree(nodes, children)
        counts["groups"][name] = len(nodes)
    return counts


def load_ncbi_taxonomy(taxdump: Path, target: int) -> tuple[Tree, dict[str, Any]]:
    """Select a compact, common-name-weighted NCBI life taxonomy profile."""
    nodes: dict[str, tuple[str, str]] = {}
    with (taxdump / "nodes.dmp").open(encoding="utf-8") as handle:
        for line in handle:
            fields = [field.strip() for field in line.split("|")]
            nodes[fields[0]] = (fields[1], fields[2])

    scientific: dict[str, str] = {}
    common: dict[str, str] = {}
    common_classes = {
        "common name", "genbank common name", "blast name", "equivalent name",
    }
    with (taxdump / "names.dmp").open(encoding="utf-8") as handle:
        for line in handle:
            fields = [field.strip() for field in line.split("|")]
            taxid, name, name_class = fields[0], fields[1], fields[3]
            if name_class == "scientific name":
                scientific[taxid] = name
            elif name_class in common_classes and taxid not in common:
                common[taxid] = name

    @lru_cache(maxsize=None)
    def lineage(taxid: str) -> tuple[str, ...]:
        parent = nodes[taxid][0]
        if taxid == parent:
            return (taxid,)
        return lineage(parent) + (taxid,)

    eligible: list[tuple[float, str]] = []
    for taxid, (_, rank) in nodes.items():
        if rank not in NCBI_RANKS or taxid not in scientific:
            continue
        path = lineage(taxid)
        if not set(path).intersection(NCBI_LIFE_ROOTS):
            continue
        common_name = common.get(taxid)
        familiarity = 100.0 if common_name else 0.0
        rank_weight = {
            "species": 8, "genus": 7, "family": 6, "order": 5,
            "class": 4, "phylum": 3, "kingdom": 2, "superkingdom": 1,
        }[rank]
        name_penalty = math.log1p(len(common_name or scientific[taxid]))
        eligible.append((familiarity + rank_weight - name_penalty, taxid))
    eligible.sort(key=lambda item: (-item[0], item[1]))
    selected = {taxid for _, taxid in eligible[:target]}
    for taxid in list(selected):
        selected.update(lineage(taxid))

    children: dict[str, list[str]] = {}
    for taxid in selected:
        if taxid == "1":
            continue
        parent = nodes[taxid][0]
        if parent in selected:
            children.setdefault(parent, []).append(taxid)
    for siblings in children.values():
        siblings.sort(key=lambda item: (common.get(item, scientific[item]).lower(), item))

    used: set[str] = set()
    result: Tree = OrderedDict()
    result["__question__"] = "Is it a scientifically classified kind of life?"

    def label(taxid: str) -> str:
        value = common.get(taxid) or scientific[taxid]
        if value in used:
            value = f"{value} [NCBI:{taxid}]"
        used.add(value)
        return value

    def emit(taxid: str) -> tuple[str, Tree | None]:
        name = label(taxid)
        descendants = children.get(taxid, [])
        if not descendants:
            return name, None
        subtree: Tree = OrderedDict()
        subtree["__question__"] = f"Is it a kind of {common.get(taxid, scientific[taxid])}?"
        for child in descendants:
            child_name, child_tree = emit(child)
            subtree[child_name] = child_tree
        return name, subtree

    roots = [
        taxid for taxid in selected
        if (nodes[taxid][0] not in selected or nodes[taxid][0] == "1")
        and taxid != "1"
    ]
    roots.sort(key=lambda item: (common.get(item, scientific[item]).lower(), item))
    for root in roots:
        root_name, root_tree = emit(root)
        result[root_name] = root_tree
    stats = {
        "source": "NCBI Taxonomy",
        "selected_taxa_with_common_name_or_rank": min(target, len(eligible)),
        "display_taxa_with_ancestors": len(selected),
        "candidate_taxa_available": len(eligible),
    }
    return result, stats


def count_nodes(tree: Tree) -> tuple[int, int]:
    branches = leaves_count = 0
    for key, child in tree.items():
        if key == "__question__":
            continue
        if child:
            branches += 1
            child_branches, child_leaves = count_nodes(child)
            branches += child_branches
            leaves_count += child_leaves
        else:
            leaves_count += 1
    return branches, leaves_count


def build(args: argparse.Namespace) -> None:
    tree = make_v1_tree()
    add_reviewed_seeds(tree)
    counts = add_wordnet_candidates(tree, args.wordnet_target)
    if args.ncbi_taxdump:
        ncbi_tree, ncbi_counts = load_ncbi_taxonomy(args.ncbi_taxdump, args.ncbi_target)
        living = find_path(tree, ["Physical", "Living"])
        living["NCBI life taxonomy candidates"] = ncbi_tree
        counts["ncbi_taxonomy"] = ncbi_counts
    branches, leaves_count = count_nodes(tree)
    counts.update({
        "display_branches": branches,
        "display_leaves": leaves_count,
        "display_nodes": branches + leaves_count,
        "reviewed_seed_groups": len(REVIEWED_SEEDS),
    })

    yaml_output = render_v1_yaml(tree, "20_questions_v2_noun_hierarchy")
    html_output = render_v1_html(tree, "20 Questions Noun Ontology v2")
    html_output = html_output.replace(
        "<h1>20 Questions Noun Ontology v2</h1>",
        "<h1>20 Questions Noun Ontology v2</h1>"
        '<div class="intro"><strong>V2 profile:</strong> '
        "The friendly v1 question-oriented tree is preserved and expanded with "
        "reviewed evolutionary examples plus source-labelled WordNet "
        f"candidates. Display nodes: {counts['display_nodes']:,}; "
        f"branches: {branches:,}; terminal categories: {leaves_count:,}. "
        "WordNet candidates are enrichment proposals, not scientific "
        "taxonomy. Common names are preferred; source identifiers remain in "
        "the manifest.</div>",
    ).replace("<strong>Suggested question:</strong> ", "")

    args.yaml_output.write_text(yaml_output, encoding="utf-8")
    args.html_output.write_text(html_output, encoding="utf-8")
    manifest = {
        "profile": "v2",
        "base": "20_questions_hierarchy.yaml",
        "wordnet_release": "Princeton WordNet 3.0",
        "wordnet_target": args.wordnet_target,
        "ncbi_taxdump": (
            "NCBI Taxonomy nodes.dmp and names.dmp"
            if args.ncbi_taxdump else None
        ),
        "counts": counts,
        "reviewed_seeds": REVIEWED_SEEDS,
        "policy": "WordNet candidates are enrichment proposals; biological seeds require taxonomic cross-validation.",
    }
    args.manifest_output.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(counts, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--wordnet-target", type=int, default=4500)
    parser.add_argument("--ncbi-taxdump", type=Path)
    parser.add_argument("--ncbi-target", type=int, default=3500)
    parser.add_argument("--yaml-output", type=Path, default=Path("v2_20_questions_hierarchy.yaml"))
    parser.add_argument("--html-output", type=Path, default=Path("v2.html"))
    parser.add_argument("--manifest-output", type=Path, default=Path("v2_manifest.json"))
    build(parser.parse_args())


if __name__ == "__main__":
    main()
