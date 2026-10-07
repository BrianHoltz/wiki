#!/usr/bin/env python3
"""Replace SUMO's loose organism projection with a compressed clade backbone."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def node(label: str, years_ago: int, description: str, *children: dict) -> dict:
    return {
        "label": label,
        "originYearsAgo": years_ago,
        "definition": f"~{years_ago:,} years ago: {description}",
        "children": list(children),
    }


BACKBONE = node(
    "Organism",
    3_800_000_000,
    "the clade of living cellular organisms; viruses are handled separately as acellular infectious agents",
    node("Bacteria", 3_800_000_000, "cellular organisms without a nucleus, including cyanobacteria and diverse bacterial lineages"),
    node("Archaea", 3_500_000_000, "cellular organisms distinct from bacteria, including methanogens, halophiles, and Asgard archaea"),
    node(
        "Eukaryota",
        1_800_000_000,
        "organisms whose cells contain nuclei and membrane-bound organelles",
        node(
            "Archaeplastida",
            1_600_000_000,
            "eukaryotes descended from a primary cyanobacterial plastid acquisition",
            node("Rhodophyta (red algae)", 1_600_000_000, "red algae with red or blue accessory pigments"),
            node(
                "Viridiplantae (green plants)",
                1_200_000_000,
                "green algae and land plants descended from a green plastid lineage",
                node("Chlorophyta (green algae)", 1_000_000_000, "the chlorophyte green-algae lineage"),
                node(
                    "Streptophyta",
                    800_000_000,
                    "charophyte algae and their land-plant descendants",
                    node(
                        "Embryophyta (land plants)",
                        470_000_000,
                        "plants adapted to life on land, retaining a protected multicellular embryo",
                        node("Bryophytes", 470_000_000, "mosses, liverworts, and hornworts, generally lacking vascular tissue"),
                        node(
                            "Tracheophyta (vascular plants)",
                            430_000_000,
                            "plants with vascular tissues for transporting water and sugars",
                            node("Lycophytes", 420_000_000, "vascular plants including clubmosses and quillworts"),
                            node(
                                "Euphyllophytes",
                                390_000_000,
                                "vascular plants including ferns, horsetails, and seed plants",
                                node("Ferns and horsetails", 370_000_000, "spore-producing euphyllophytes with fronds or jointed stems"),
                                node(
                                    "Spermatophytes (seed plants)",
                                    365_000_000,
                                    "plants reproducing through seeds and pollen",
                                    node(
                                        "Gymnosperms",
                                        320_000_000,
                                        "seed plants whose ovules are not enclosed in an ovary",
                                        node("Conifers", 300_000_000, "cone-bearing gymnosperms including pines, firs, spruces, and relatives"),
                                        node("Other gymnosperms", 320_000_000, "cycads, ginkgo, and gnetophytes"),
                                    ),
                                    node(
                                        "Angiosperms (flowering plants)",
                                        140_000_000,
                                        "seed plants that produce flowers and enclose seeds in fruits",
                                        node("Early-diverging angiosperms and magnoliids", 140_000_000, "flowering-plant lineages outside the principal monocot and eudicot radiations"),
                                        node("Monocots", 135_000_000, "flowering plants with one embryonic seed leaf, including grasses, lilies, and palms"),
                                        node("Eudicots", 125_000_000, "the principal flowering-plant clade with pollen commonly having three apertures"),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        ),
        node(
            "Major protist lineages",
            1_200_000_000,
            "diverse eukaryotic clades that are neither animals, fungi, nor land plants",
            node("SAR", 1_200_000_000, "a major eukaryotic clade including stramenopiles, alveolates, and rhizarians"),
            node("Amoebozoa", 1_000_000_000, "amoeboid and slime-mold relatives"),
            node("Other deep eukaryote branches", 1_200_000_000, "important but incompletely resolved eukaryotic lineages retained without false precision"),
        ),
        node(
            "Opisthokonta",
            1_000_000_000,
            "the eukaryotic clade containing fungi and animals",
            node(
                "Fungi",
                1_000_000_000,
                "absorptive heterotrophs that grow as filaments or yeasts and reproduce through spores",
                node("Early-diverging fungi", 1_000_000_000, "fungal lineages outside the Dikarya, including chytrid relatives"),
                node(
                    "Dikarya",
                    700_000_000,
                    "the fungal clade containing most familiar molds, yeasts, mushrooms, rusts, and smuts",
                    node("Ascomycota", 650_000_000, "sac fungi including yeasts, molds, morels, and truffles"),
                    node("Basidiomycota", 600_000_000, "club fungi including mushrooms, puffballs, rusts, and smuts"),
                ),
            ),
            node(
                "Animalia",
                700_000_000,
                "multicellular heterotrophs that develop from an embryo",
                node("Porifera (sponges)", 650_000_000, "animals with porous bodies and no true organs"),
                node("Ctenophora (comb jellies)", 600_000_000, "marine animals propelled by rows of ciliary combs"),
                node("Placozoa", 600_000_000, "simple flattened animals with few cell types"),
                node("Cnidaria", 600_000_000, "animals with stinging cells, including corals, anemones, and jellyfish"),
                node(
                    "Bilateria",
                    600_000_000,
                    "animals with bilateral organization and a distinct head-to-tail axis",
                    node(
                        "Protostomia",
                        550_000_000,
                        "bilaterians whose first embryonic opening develops toward the mouth",
                        node(
                            "Ecdysozoa",
                            550_000_000,
                            "animals that grow by periodically shedding an external cuticle",
                            node(
                                "Arthropoda",
                                540_000_000,
                                "segmented animals with jointed appendages and an external skeleton",
                                node("Chelicerata", 540_000_000, "arthropods including spiders, scorpions, mites, and horseshoe crabs"),
                                node("Myriapoda", 520_000_000, "centipedes and millipedes"),
                                node("Pancrustacea", 520_000_000, "crustaceans and their terrestrial branch, the hexapods"),
                                node("Hexapoda", 500_000_000, "six-legged arthropods, including insects"),
                            ),
                            node("Nematoda and relatives", 550_000_000, "roundworms and other non-arthropod ecdysozoans"),
                        ),
                        node(
                            "Spiralia",
                            550_000_000,
                            "protostomes with spiral-cleaving or related developmental ancestry",
                            node("Mollusca", 540_000_000, "snails, slugs, bivalves, chitons, and cephalopods"),
                            node("Annelida", 540_000_000, "segmented worms including earthworms and leeches"),
                            node("Other spiralian lineages", 550_000_000, "brachiopods, flatworms, rotifers, and related groups"),
                        ),
                    ),
                    node(
                        "Deuterostomia",
                        600_000_000,
                        "bilaterians whose embryonic development includes a deuterostome pattern",
                        node("Echinodermata", 520_000_000, "marine animals including starfish, sea urchins, and sea cucumbers"),
                        node(
                            "Chordata",
                            540_000_000,
                            "animals with a notochord or related chordate developmental features",
                            node("Tunicates and lancelets", 540_000_000, "non-vertebrate chordates retaining key chordate features"),
                            node(
                                "Vertebrata",
                                525_000_000,
                                "chordates with a backbone or its developmental precursor",
                                node("Jawless vertebrates", 500_000_000, "lampreys, hagfish, and their close extinct relatives"),
                                node(
                                    "Gnathostomata (jawed vertebrates)",
                                    450_000_000,
                                    "vertebrates with jaws and paired appendages",
                                    node("Chondrichthyes (cartilaginous fishes)", 450_000_000, "sharks, rays, skates, and chimaeras"),
                                    node(
                                        "Osteichthyes (bony vertebrates)",
                                        425_000_000,
                                        "vertebrates with an ancestrally bony internal skeleton, including tetrapods",
                                        node("Actinopterygii (ray-finned fishes)", 420_000_000, "bony fishes whose fins are supported mainly by rays"),
                                        node(
                                            "Sarcopterygii (lobe-finned vertebrates)",
                                            425_000_000,
                                            "bony vertebrates with fleshy paired fins, including tetrapods",
                                            node("Coelacanths and lungfishes", 400_000_000, "living non-tetrapod lobe-finned vertebrates"),
                                            node(
                                                "Tetrapoda",
                                                390_000_000,
                                                "vertebrates descended from four-limbed ancestors",
                                                node("Amphibia", 370_000_000, "tetrapods with a life cycle commonly involving aquatic eggs or larvae"),
                                                node(
                                                    "Amniota",
                                                    320_000_000,
                                                    "tetrapods whose embryos develop within an amniotic membrane",
                                                    node(
                                                        "Synapsida",
                                                        320_000_000,
                                                        "amniotes on the lineage leading to mammals",
                                                        node(
                                                            "Mammalia",
                                                            225_000_000,
                                                            "synapsids with hair, mammary glands, and specialized jaw and ear bones",
                                                            node("Monotremata", 210_000_000, "egg-laying mammals including platypuses and echidnas"),
                                                            node(
                                                                "Theria",
                                                                170_000_000,
                                                                "live-bearing mammals",
                                                                node("Metatheria (marsupials)", 160_000_000, "mammals whose young complete development after birth, often in a pouch"),
                                                                node("Eutheria (placental mammals)", 100_000_000, "mammals whose young develop through a complex placental connection"),
                                                            ),
                                                        ),
                                                    ),
                                                    node(
                                                        "Sauropsida",
                                                        320_000_000,
                                                        "amniotes on the lineage leading to turtles, reptiles, and birds",
                                                        node("Lepidosauria", 240_000_000, "tuatara, lizards, and snakes"),
                                                        node("Testudines (turtles)", 230_000_000, "reptiles with a shell-bearing body plan"),
                                                        node(
                                                            "Archosauria",
                                                            250_000_000,
                                                            "the archosaur lineage containing crocodilians and dinosaurs",
                                                            node("Crocodylia", 230_000_000, "crocodilians and their living relatives"),
                                                            node(
                                                                "Dinosauria",
                                                                240_000_000,
                                                                "archosaurs with the dinosaur hip and limb architecture, including birds",
                                                                node("Aves (birds)", 160_000_000, "living feathered dinosaurs"),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    ),
)


def make_id(label: str) -> str:
    return "Bio" + re.sub(r"[^A-Za-z0-9]+", "", label.split(" (", 1)[0])


def flatten(tree: dict, parent_id: str | None = None) -> tuple[list[dict], set[str]]:
    nodes: list[dict] = []
    ids: set[str] = set()
    node_id = "Organism" if tree["label"] == "Organism" else make_id(tree["label"])
    ids.add(node_id)
    child_ids = []
    for child in tree["children"]:
        child_node_id = "Organism" if child["label"] == "Organism" else make_id(child["label"])
        child_ids.append(child_node_id)
    record = {
        "id": node_id,
        "label": tree["label"],
        "definition": tree["definition"],
        "definitionSource": "Human Knowledge 2000 taxonomy table + modern clade correction",
        "originYearsAgo": tree["originYearsAgo"],
        "children": child_ids,
        "alternateParents": [],
        "directParentCount": 1 if parent_id else 2,
        "provisionalParent": None,
        "sourceRefs": ["Human Knowledge 2000 taxonomy table", "Wikipedia clade articles"],
    }
    nodes.append(record)
    for child in tree["children"]:
        child_nodes, child_ids_set = flatten(child, node_id)
        nodes.extend(child_nodes)
        ids.update(child_ids_set)
    return nodes, ids


def graft(path: Path) -> None:
    data = json.loads(path.read_text())
    organism = next(item for item in data["nodes"] if item["id"] == "Organism")

    old_ids = set()
    pending = list(organism["children"])
    by_id = {item["id"]: item for item in data["nodes"]}
    while pending:
        current = pending.pop()
        if current in old_ids:
            continue
        old_ids.add(current)
        pending.extend(by_id.get(current, {}).get("children", []))

    data["nodes"] = [
        item
        for item in data["nodes"]
        if item["id"] not in old_ids and item["id"] != "Organism"
    ]
    graft_nodes, _ = flatten(BACKBONE)
    data["nodes"].extend(graft_nodes)
    grafted_organism = next(item for item in data["nodes"] if item["id"] == "Organism")
    grafted_organism["alternateParents"] = ["Agent"]
    grafted_organism["directParentCount"] = 2
    data["unaryNodes"] = sorted(
        item["id"] for item in data["nodes"] if len(item.get("children", [])) == 1
    )
    data["stats"]["nodeCount"] = len(data["nodes"])
    data["stats"]["projectedEdgeCount"] = sum(
        len(item.get("children", [])) for item in data["nodes"]
    )
    data["stats"]["multipleParentNodeCount"] = sum(
        1 for item in data["nodes"] if item.get("alternateParents")
    )
    data["stats"]["unaryNodeCount"] = len(data["unaryNodes"])
    data["stats"]["definitionCount"] = sum(
        1 for item in data["nodes"] if item.get("definition")
    )
    data["stats"]["definitionCountsBySource"] = {
        "SUMO KIF": sum(
            1 for item in data["nodes"] if item.get("definitionSource") == "SUMO KIF"
        ),
        "external source": sum(
            1 for item in data["nodes"] if item.get("definitionSource") == "external source"
        ),
        "project editorial": sum(
            1
            for item in data["nodes"]
            if item.get("definitionSource") != "SUMO KIF"
            and item.get("definitionSource") is not None
        ),
    }
    data["organismGraft"] = {
        "source": "Human Knowledge 2000 taxonomy table + modern Wikipedia clade corrections",
        "policy": "Monophyletic, interest-weighted backbone; specialist-only subdivisions telescoped",
        "originEstimatePolicy": "Every grafted clade definition begins with an approximate years-ago origin",
        "removedSumoDescendantCount": len(old_ids),
    }
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("sumo_json", type=Path)
    args = parser.parse_args()
    graft(args.sumo_json)


if __name__ == "__main__":
    main()
