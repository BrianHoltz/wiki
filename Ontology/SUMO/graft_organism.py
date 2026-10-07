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
        "definition": f"{years_ago // 1_000_000}Mya: {description}",
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
            "Archaeplastida (Plantae)",
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
                        node("Bryophytes (Bryophyta)", 470_000_000, "mosses, liverworts, and hornworts, generally lacking vascular tissue"),
                        node(
                            "Tracheophyta (vascular plants)",
                            430_000_000,
                            "plants with vascular tissues for transporting water and sugars",
                            node("Lycophytes", 420_000_000, "vascular plants including clubmosses and quillworts"),
                            node(
                                "Euphyllophytes",
                                390_000_000,
                                "vascular plants including ferns, horsetails, and seed plants",
                                node("Ferns and horsetails (Monilophyta)", 370_000_000, "spore-producing euphyllophytes with fronds or jointed stems"),
                                node(
                                    "Spermatophytes (seed plants)",
                                    365_000_000,
                                    "plants reproducing through seeds and pollen",
                                    node(
                                        "Gymnosperms",
                                        320_000_000,
                                        "seed plants whose ovules are not enclosed in an ovary",
                                        node("Conifers", 300_000_000, "cone-bearing gymnosperms including pines, firs, spruces, and relatives"),
                                        node("Other gymnosperms", 320_000_000, "cycads, ginkgo, and gnetophytes", node("Cycads (Cycadophyta)", 280_000_000, "palm-like gymnosperms with large cones")),
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
                                                                node(
                                                                    "Eutheria (placental mammals)",
                                                                    100_000_000,
                                                                    "mammals whose young develop through a complex placental connection",
                                                                    node(
                                                                        "Afrotheria",
                                                                        100_000_000,
                                                                        "placental mammals with African evolutionary roots",
                                                                        node("Tubulidentata", 60_000_000, "the aardvark order"),
                                                                        node("Proboscidea", 60_000_000, "elephants and their extinct relatives"),
                                                                        node("Sirenia", 50_000_000, "manatees, dugongs, and their extinct relatives"),
                                                                        node("Hyracoidea", 50_000_000, "hyraxes and their close relatives"),
                                                                    ),
                                                                    node(
                                                                        "Xenarthra",
                                                                        65_000_000,
                                                                        "placental mammals with distinctive extra spinal articulations",
                                                                        node("Cingulata", 55_000_000, "armadillos and their extinct relatives"),
                                                                        node("Pilosa", 55_000_000, "sloths and anteaters"),
                                                                    ),
                                                                    node(
                                                                        "Laurasiatheria",
                                                                        90_000_000,
                                                                        "placental mammals with deep ancestry in northern Laurasia",
                                                                        node("Eulipotyphla", 70_000_000, "modern shrews, moles, hedgehogs, and solenodons"),
                                                                        node("Pholidota", 50_000_000, "pangolins"),
                                                                        node("Perissodactyla", 55_000_000, "odd-toed ungulates including horses, rhinos, and tapirs"),
                                                                        node(
                                                                            "Carnivora",
                                                                            55_000_000,
                                                                            "carnivoran mammals including cats, dogs, bears, and seals",
                                                                            node("Pinnipedia", 30_000_000, "seals, sea lions, and walruses"),
                                                                        ),
                                                                        node("Chiroptera (bats)", 55_000_000, "mammals with powered flight"),
                                                                        node("Cetacea", 50_000_000, "whales, dolphins, and porpoises"),
                                                                        node("Cetartiodactyla (Artiodactyla)", 55_000_000, "the inclusive even-toed ungulate and whale lineage"),
                                                                    ),
                                                                    node(
                                                                        "Euarchontoglires",
                                                                        90_000_000,
                                                                        "placental mammals including rodents, lagomorphs, colugos, and primates",
                                                                        node("Rodentia", 66_000_000, "gnawing mammals including mice, squirrels, beavers, and porcupines"),
                                                                        node("Lagomorpha", 60_000_000, "rabbits, hares, and pikas"),
                                                                        node("Dermoptera", 50_000_000, "colugos or flying lemurs"),
                                                                        node(
                                                                            "Primates",
                                                                            65_000_000,
                                                                            "mammals with grasping hands or feet, nails, forward-facing eyes, and enlarged brains",
                                                                            node("Strepsirrhini", 55_000_000, "lemurs, lorises, and galagos; the modern replacement for the paraphyletic Prosimians"),
                                                                            node(
                                                                                "Haplorhini",
                                                                                55_000_000,
                                                                                "tarsiers and simians with simpler noses and greater visual specialization",
                                                                                node("Tarsiiformes", 45_000_000, "tarsiers"),
                                                                                node(
                                                                                    "Simiiformes (Anthropoidea)",
                                                                                    40_000_000,
                                                                                    "the higher primates including New World monkeys, Old World monkeys, and apes",
                                                                                    node(
                                                                                        "Platyrrhini",
                                                                                        25_000_000,
                                                                                        "New World monkeys with broad-set nostrils and many prehensile tails",
                                                                                        node("Callitrichidae", 20_000_000, "marmosets and tamarins"),
                                                                                        node("Cebidae", 20_000_000, "capuchins, squirrel monkeys, and close relatives"),
                                                                                    ),
                                                                                    node(
                                                                                        "Catarrhini",
                                                                                        25_000_000,
                                                                                        "Old World monkeys and apes with close-set nostrils",
                                                                                        node("Cercopithecoidea (Cercopithecidae)", 20_000_000, "Old World monkeys including baboons, macaques, and colobus monkeys"),
                                                                                        node(
                                                                                            "Hominoidea",
                                                                                            20_000_000,
                                                                                            "tailless apes including gibbons and great apes",
                                                                                            node("Hylobatidae", 15_000_000, "gibbons and siamangs, the lesser apes"),
                                                                                            node(
                                                                                                "Hominidae",
                                                                                                18_000_000,
                                                                                                "the great-ape family including orangutans, gorillas, chimpanzees, bonobos, and humans",
                                                                                                node("Ponginae", 15_000_000, "orangutans and their close relatives"),
                                                                                                node(
                                                                                                    "Homininae",
                                                                                                    12_000_000,
                                                                                                    "the great-ape subfamily including gorillas, chimpanzees, bonobos, and humans",
                                                                                                    node("Australopithecus", 4_000_000, "extinct African hominins close to the ancestry of Homo"),
                                                                                                    node(
                                                                                                        "Homo",
                                                                                                        2_800_000,
                                                                                                        "the hominin genus including humans and several extinct tool-using relatives",
                                                                                                        node("Homo habilis", 2_400_000, "an extinct early Homo species associated with Oldowan tools"),
                                                                                                        node("Homo erectus", 1_900_000, "an extinct widespread Homo species associated with early migrations and fire use"),
                                                                                                        node(
                                                                                                            "Homo sapiens",
                                                                                                            300_000,
                                                                                                            "the living human species",
                                                                                                            node("Homo sapiens neanderthalensis", 430_000, "the extinct Neanderthal human lineage"),
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

def find_taxon(tree: dict, label: str) -> dict:
    if tree["label"] == label:
        return tree
    for child in tree["children"]:
        try:
            return find_taxon(child, label)
        except LookupError:
            pass
    raise LookupError(label)


def augment_backbone(tree: dict) -> None:
    find_taxon(tree, "Archaeplastida (Plantae)")["label"] = "Archaeplastida (Plantae)"
    find_taxon(tree, "Bryophytes (Bryophyta)")["label"] = "Bryophytes (Bryophyta)"
    find_taxon(tree, "Ferns and horsetails (Monilophyta)")["label"] = "Ferns and horsetails (Monilophyta)"
    gymnosperms = find_taxon(tree, "Other gymnosperms")
    if not any(child["label"] == "Cycads (Cycadophyta)" for child in gymnosperms["children"]):
        gymnosperms["children"].append(
            node("Cycads (Cycadophyta)", 280_000_000, "palm-like gymnosperms with large cones")
        )

    animals = find_taxon(tree, "Animalia")
    porifera = next(child for child in animals["children"] if child["label"] == "Porifera (sponges)")
    bilateria = next(child for child in animals["children"] if child["label"] == "Bilateria")
    eumetazoa = node(
        "Eumetazoa",
        600_000_000,
        "animals with true tissues, including cnidarians and bilaterians",
        next(child for child in animals["children"] if child["label"] == "Ctenophora (comb jellies)"),
        next(child for child in animals["children"] if child["label"] == "Placozoa"),
        next(child for child in animals["children"] if child["label"] == "Cnidaria"),
        bilateria,
    )
    animals["children"] = [porifera, eumetazoa]

    eutheria = find_taxon(tree, "Eutheria (placental mammals)")
    eutheria["children"] = [
        node(
            "Afrotheria",
            100_000_000,
            "placental mammals with African evolutionary roots",
            node("Tubulidentata", 60_000_000, "the aardvark order"),
            node("Proboscidea", 60_000_000, "elephants and their extinct relatives"),
            node("Sirenia", 50_000_000, "manatees, dugongs, and their extinct relatives"),
            node("Hyracoidea", 50_000_000, "hyraxes and their close relatives"),
        ),
        node(
            "Xenarthra",
            65_000_000,
            "placental mammals with distinctive extra spinal articulations",
            node("Cingulata", 55_000_000, "armadillos and their extinct relatives"),
            node("Pilosa", 55_000_000, "sloths and anteaters"),
        ),
        node(
            "Laurasiatheria",
            90_000_000,
            "placental mammals with deep ancestry in northern Laurasia",
            node("Eulipotyphla", 70_000_000, "modern shrews, moles, hedgehogs, and solenodons"),
            node("Pholidota", 50_000_000, "pangolins"),
            node("Perissodactyla", 55_000_000, "odd-toed ungulates including horses, rhinos, and tapirs"),
            node("Carnivora", 55_000_000, "carnivoran mammals including cats, dogs, bears, and seals", node("Pinnipedia", 30_000_000, "seals, sea lions, and walruses")),
            node("Chiroptera (bats)", 55_000_000, "mammals with powered flight"),
            node("Cetacea", 50_000_000, "whales, dolphins, and porpoises"),
            node("Cetartiodactyla (Artiodactyla)", 55_000_000, "the inclusive even-toed ungulate and whale lineage"),
        ),
        node(
            "Euarchontoglires",
            90_000_000,
            "placental mammals including rodents, lagomorphs, colugos, and primates",
            node("Rodentia", 66_000_000, "gnawing mammals including mice, squirrels, beavers, and porcupines"),
            node("Lagomorpha", 60_000_000, "rabbits, hares, and pikas"),
            node("Dermoptera", 50_000_000, "colugos or flying lemurs"),
            node(
                "Primates",
                65_000_000,
                "mammals with grasping hands or feet, nails, forward-facing eyes, and enlarged brains",
                node("Strepsirrhini", 55_000_000, "lemurs, lorises, and galagos; the modern replacement for the paraphyletic Prosimians"),
                node(
                    "Haplorhini",
                    55_000_000,
                    "tarsiers and simians with simpler noses and greater visual specialization",
                    node("Tarsiiformes", 45_000_000, "tarsiers"),
                    node(
                        "Simiiformes (Anthropoidea)",
                        40_000_000,
                        "the higher primates including New World monkeys, Old World monkeys, and apes",
                        node("Platyrrhini", 25_000_000, "New World monkeys with broad-set nostrils and many prehensile tails", node("Callitrichidae", 20_000_000, "marmosets and tamarins"), node("Cebidae", 20_000_000, "capuchins, squirrel monkeys, and close relatives")),
                        node(
                            "Catarrhini",
                            25_000_000,
                            "Old World monkeys and apes with close-set nostrils",
                            node("Cercopithecoidea (Cercopithecidae)", 20_000_000, "Old World monkeys including baboons, macaques, and colobus monkeys"),
                            node(
                                "Hominoidea",
                                20_000_000,
                                "tailless apes including gibbons and great apes",
                                node("Hylobatidae", 15_000_000, "gibbons and siamangs, the lesser apes"),
                                node(
                                    "Hominidae",
                                    18_000_000,
                                    "the great-ape family including orangutans, gorillas, chimpanzees, bonobos, and humans",
                                    node("Ponginae", 15_000_000, "orangutans and their close relatives"),
                                    node(
                                        "Homininae",
                                        12_000_000,
                                        "the great-ape subfamily including gorillas, chimpanzees, bonobos, and humans",
                                        node("Australopithecus", 4_000_000, "extinct African hominins close to the ancestry of Homo"),
                                        node(
                                            "Homo",
                                            2_800_000,
                                            "the hominin genus including humans and several extinct tool-using relatives",
                                            node("Homo habilis", 2_400_000, "an extinct early Homo species associated with Oldowan tools"),
                                            node("Homo erectus", 1_900_000, "an extinct widespread Homo species associated with early migrations and fire use"),
                                            node("Homo sapiens", 300_000, "the living human species", node("Homo sapiens neanderthalensis", 430_000, "the extinct Neanderthal human lineage")),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    ]


augment_backbone(BACKBONE)

LEGACY_REPLACEMENTS = {
    "Prokaryotae (Monera)": "Bacteria + Archaea",
    "Archaebacteria": "Archaea",
    "Eubacteria": "Bacteria",
    "Protoctista (Protist)": "Major protist lineages",
    "Filicinophyta": "Ferns and horsetails (Monilophyta)",
    "Angiospermophyta": "Angiosperms (flowering plants)",
    "Parazoa": "Porifera",
    "Prosimians": "Strepsirrhini",
    "Pongidae": "Hominidae -> Ponginae + Homininae",
    "Prototheria": "Monotremata",
    "Insectivora": "Eulipotyphla",
    "Edentata": "Xenarthra",
    "Artiodactylia": "Cetartiodactyla (Artiodactyla)",
    "Cetecea": "Cetacea",
    "Agnatha": "Jawless vertebrates",
    "Chondrichthye": "Chondrichthyes",
    "Reptilia": "Sauropsida",
    "Pisces": "Gnathostomata -> Chondrichthyes + Osteichthyes",
    "Coelenterates": "Cnidaria",
}


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
        "originEstimatePolicy": "Every grafted clade definition begins with an integer Mya origin estimate",
        "legacyTaxaReplaced": LEGACY_REPLACEMENTS,
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
