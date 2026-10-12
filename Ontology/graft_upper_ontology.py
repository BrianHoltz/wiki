#!/usr/bin/env python3
"""Graft accepted upper definitions onto the incumbent; preserve lower records.

Run after SUMO/overlay_canonical.py if rebuilding the legacy projection.
Definitions come from Ontology.md; placements below the accepted tier are a trial.
"""

import argparse
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OBJECT_CATEGORIES = {
    "PhysicalObject": "Physical object",
    "MaterialBody": "Material body",
    "MaterialPortion": "Material portion",
    "PhysicalAggregate": "Physical aggregate",
    "SocialEntity": "Social object",
    "InstitutionalEntity": "Institutional continuant",
    "SocialCollective": "Social collective",
}
OCCURRENCE_CATEGORIES = {
    "Process": "Process", "Event": "Event", "OccurrenceState": "State",
    "PhysicalProcess": "Physical process", "MentalProcess": "Mental process",
    "SocialProcess": "Social process", "TransitionEvent": "Transition event",
    "AchievementEvent": "Achievement event", "PhysicalState": "Physical state",
    "MentalState": "Mental state", "SocialState": "Social state",
}
FEATURE_CATEGORIES = {
    "Quality": "Quality", "Disposition": "Disposition",
    "RelationalFeature": "Relationship", "StructuralFeature": "Structural feature",
    "Attitude": "Attitude",
}
UPPER = {
    "Particular": "Particular",
    "Predicable": "Predicable",
    "Object": "Object",
    "Occurrence": "Occurrence",
    "Feature": "Feature",
    "Region": "Region",
    "Composition": "Composition",
    "FormalEntity": "Formal entity",
}
UPPER.update(OBJECT_CATEGORIES)
UPPER.update(OCCURRENCE_CATEGORIES)
UPPER.update(FEATURE_CATEGORIES)


def section(text, heading):
    tail = text.split(f"### {heading}\n", 1)[1]
    return tail.split("\n### ", 1)[0]


def accepted_definitions(text):
    six = section(text, "Accepted decision: Particular's six principal categories")
    definitions = {}
    for identifier, label in UPPER.items():
        if identifier in {"Particular", "Predicable"}:
            heading = ("Accepted decision: Particular / Predicable root split"
                       if identifier == "Particular"
                       else "Accepted decision: constitutive predicative applicability")
            body = section(text, heading)
            key = "Particular" if identifier == "Particular" else "Definition"
            definitions[identifier] = re.search(
                rf"^\*\*{key}:\*\* (.+)$", body, re.M).group(1)
        else:
            body = (section(text, "Accepted decision: Object's children and grandchildren")
                    if identifier in OBJECT_CATEGORIES else
                    section(text, "Accepted decision: Occurrence's children and grandchildren")
                    if identifier in OCCURRENCE_CATEGORIES else
                    section(text, "Accepted decision: Feature's principal categories")
                    if identifier in FEATURE_CATEGORIES else six)
            match = re.search(rf"^- \*\*{label}:\*\* (.+)$", body, re.M)
            if match:
                definitions[identifier] = match.group(1).split(" Examples:", 1)[0]
            else:
                block = body.split(f"#### {label}\n", 1)[1].split("\n#### ", 1)[0]
                parts = [re.search(rf"^- \*\*{key}:\*\* (.+)$", block, re.M).group(1)
                         for key in ("Core", "Explanation", "Example")]
                definitions[identifier] = (parts[0] + " Explanation: " + parts[1]
                                           + " Example: " + parts[2])
    return definitions


def graft(data, definitions):
    nodes = {n["id"]: dict(n) for n in data["nodes"]}
    original_ids = set(nodes)
    old_children = {i: list(n["children"]) for i, n in nodes.items()}
    parents = {}
    for node in nodes.values():
        for child in node["children"]:
            parents.setdefault(child, node["id"])
    for identifier, label in UPPER.items():
        nodes.setdefault(identifier, {"id": identifier, "children": []})
        nodes[identifier].update(label=label, definition=definitions[identifier],
                                 definitionSource="accepted project definition",
                                 provisionalParent=None)

    for identifier in ("RealizedEntity", "AbstractEntity"):
        nodes.pop(identifier, None)
        parents.pop(identifier, None)

    def move(identifier, parent, definition=None, label=None):
        if identifier not in nodes:
            return
        parents[identifier] = parent
        node = nodes[identifier]
        node["provisionalParent"] = parent
        if definition:
            node["definition"] = "Provisional graft reading: " + definition
            node["definitionSource"] = "provisional project graft"
        elif not str(node.get("definition") or "").startswith("Provisional graft"):
            node["definition"] = ("Provisional graft placement; inherited meaning requires review. "
                                  + (node.get("definition") or "No inherited definition."))
        if label:
            node["label"] = label

    # Reconnect inherited branches; deeper placements remain provisional.
    for identifier, parent in {
        "Process": "Occurrence", "Event": "Occurrence", "Practice": "SocialProcess",
        "SocialInteraction": "SocialProcess", "OrganizationalProcess": "SocialProcess",
        "Motion": "PhysicalProcess",
        "SocialEntity": "Object", "InstitutionalEntity": "SocialEntity",
        "Item": "MaterialBody", "SelfConnectedObject": "PhysicalObject",
        "Substance": "MaterialPortion", "Institution": "InstitutionalEntity",
        "Community": "SocialCollective",
        "AgeGroup": "SocialCollective", "EthnicGroup": "SocialCollective",
        "FamilyGroup": "SocialCollective", "Collection": "Object",
        "MathematicalEntity": "FormalEntity", "QualityValue": "FormalEntity",
        "InformationalEntity": "Composition", "RepresentationalEntity": "Composition",
        "AstronomicalBody": "PhysicalObject", "Hole": "StructuralFeature", "Person": "Human",
        "OrganizationUnit": "InstitutionalEntity",
        "Artifact": "Item", "Group": "Collection", "Organization": "InstitutionalEntity",
        "Government": "PoliticalOrganization", "Language": "RepresentationalEntity",
        "GeopoliticalArea": "GeographicArea",
        "Quality": "Feature", "Disposition": "Feature", "Capability": "Disposition",
        "Preference": "Attitude", "Obligation": "RelationalFeature", "Relationship": "RelationalFeature",
        "Status": "RelationalFeature", "Agreement": "RelationalFeature", "License": "RelationalFeature",
        "Contract": "RelationalFeature", "Role": "Property",
        "Purpose": "Composition", "Norm": "Composition", "Goal": "Composition",
        "Convention": "Composition", "Law": "Composition", "Policy": "Composition",
        "Proof": "Composition", "Definition": "Composition",
        "PhysicalSystemModel": "Composition", "MathematicalModel": "Composition",
        "Fact": "Proposition", "Theorem": "Proposition", "Signal": "Occurrence",
    }.items():
        move(identifier, parent)

    # Make consequential sense choices visible in the existing definition UI.
    readings = {
        "Process": "an occurrence identified through its unfolding activity, operation or change.",
        "Event": "an occurrence identified as a bounded happening under an event criterion.",
        "SocialEntity": "an Object whose identity or persistence depends on social practices, membership, recognition or constitutive rules.",
        "InformationalEntity": "origin-anchored informational content, distinguished from its carriers and from origin-independent formal subjects.",
        "RepresentationalEntity": "an origin-anchored representational product, including content, expressions and specifications; not its physical carrier or its referent.",
        "MathematicalEntity": "a Formal entity identified by mathematical conditions in a specified framework; inherited descendants need individual review.",
        "Quality": "a bearer-specific characteristic admitting a qualitative or quantitative determination; not the repeatable predicable.",
        "Disposition": "a bearer-specific feature grounding a tendency for manifestations under specified conditions.",
        "Capability": "a disposition assessed against a specified performance or task criterion.",
        "Preference": "a subject's particular orientation favoring alternatives in an evaluative context.",
        "Obligation": "a bearer's particular standing as required to act under a normative framework.",
        "Relationship": "a particular socially constituted connection dependent on its participants.",
        "Status": "a bearer's particular socially recognized standing, distinguished from its classification predicate.",
        "Agreement": "a particular shared commitment dependent on its participants.",
        "License": "a bearer's particular authorization under stated conditions, rather than a license document.",
        "Contract": "a particular agreement binding its parties, rather than the text expressing its terms.",
        "Role": "a unary predicable classifying a bearer by a contextual position, distinguished from an office and a particular occupancy.",
        "Purpose": "an origin-anchored specification of an intended end.",
        "Goal": "an origin-anchored specification of a target condition or outcome.",
        "Norm": "an origin-anchored specification of expected, permitted or required conduct.",
        "Convention": "an originated or traditionally maintained specification of a conventional practice or meaning.",
        "Law": "origin-anchored normative content recognized within a legal framework, distinguished from enactment and enforcement.",
        "Policy": "an origin-anchored specification guiding decisions or conduct.",
        "Proof": "an originated argument establishing a proposition, distinguished from an origin-independent formal derivation.",
        "Definition": "an originated expression or specification fixing a term's meaning or use.",
        "PhysicalSystemModel": "an originated representation of a physical system, distinguished from the system and its purely formal structure.",
        "MathematicalModel": "an originated mathematical representation of a target, distinguished from an origin-independent mathematical structure.",
        "Hole": "a host-dependent cavity feature, distinguished from its boundary and the region occupied at a time.",
        "Signal": "a signaling episode involving a perceivable variation; other signal senses require separation.",
        "Agent": "an Object capable of intentional action; its inherited subclasses require review.",
        "SelfConnectedObject": "an Object whose parts are connected.",
    }
    for identifier, definition in readings.items():
        move(identifier, parents[identifier], definition,
             "Social object" if identifier == "SocialEntity" else None)

    parents.update(Particular="Entity", Predicable="Entity", Object="Particular",
                   Occurrence="Particular", Feature="Particular", Region="Particular",
                   Composition="Particular", FormalEntity="Particular",
                   Property="Predicable", Relation="Predicable")
    for identifier, definition in {
        "Property": "A predicable applicable to one subject as a characterization; its subject may itself be a predicable.",
        "Relation": "A predicable applicable to two or more subjects as an ordered relational characterization.",
    }.items():
        nodes[identifier].update(definition=definition,
                                 definitionSource="provisional project graft",
                                 provisionalParent="Predicable")
    parents.update(PhysicalObject="Object", SocialEntity="Object",
                   MaterialBody="PhysicalObject", MaterialPortion="PhysicalObject",
                   PhysicalAggregate="PhysicalObject",
                   InstitutionalEntity="SocialEntity", SocialCollective="SocialEntity")
    parents.update(Process="Occurrence", Event="Occurrence", OccurrenceState="Occurrence",
                   PhysicalProcess="Process", MentalProcess="Process", SocialProcess="Process",
                   TransitionEvent="Event", AchievementEvent="Event",
                   PhysicalState="OccurrenceState", MentalState="OccurrenceState", SocialState="OccurrenceState")
    parents.update(Quality="Feature", Disposition="Feature",
                   RelationalFeature="Feature", StructuralFeature="Feature", Attitude="Feature")
    # State is the inherited territorial record; do not reuse its identity for an episode.
    if "State" in nodes:
        nodes["State"]["label"] = "State territory"
    for identifier in UPPER:
        nodes[identifier].update(definition=definitions[identifier],
                                 definitionSource="accepted project definition",
                                 provisionalParent=None)
    if "Relationship" in nodes:
        nodes["Relationship"]["label"] = "Social relationship"
    parents.pop("Entity", None)
    for identifier in nodes:
        if identifier != "Entity" and parents.get(identifier) not in nodes:
            raise ValueError(f"No retained parent for {identifier}: {parents.get(identifier)}")

    order = {"Entity": ["Particular", "Predicable"],
             "Particular": ["Object", "Occurrence", "Feature", "Region", "Composition", "FormalEntity"],
             "Predicable": ["Property", "Relation"],
             "Object": ["PhysicalObject", "SocialEntity", "Agent", "Collection"],
             "PhysicalObject": ["MaterialBody", "MaterialPortion", "PhysicalAggregate"],
             "SocialEntity": ["InstitutionalEntity", "SocialCollective"],
             "Occurrence": ["Process", "Event", "OccurrenceState"],
             "Process": ["PhysicalProcess", "MentalProcess", "SocialProcess"],
             "Event": ["TransitionEvent", "AchievementEvent"],
             "OccurrenceState": ["PhysicalState", "MentalState", "SocialState"],
             "Feature": ["Quality", "Disposition", "RelationalFeature", "StructuralFeature", "Attitude"]}
    for identifier, node in nodes.items():
        selected = [i for i, parent in parents.items() if parent == identifier]
        rank = order.get(identifier, old_children.get(identifier, []))
        node["children"] = sorted(selected, key=lambda i: (rank.index(i) if i in rank else len(rank), i))
        node["alternateParents"] = []
        node["directParentCount"] = 0 if identifier == "Entity" else 1
        if identifier in UPPER:
            node["provisionalParent"] = None

    seen = set()
    def visit(identifier):
        if identifier in seen:
            raise ValueError(f"Repeated path or cycle: {identifier}")
        seen.add(identifier)
        for child in nodes[identifier]["children"]:
            visit(child)
    visit("Entity")
    if seen != set(nodes):
        raise ValueError(f"Unreachable nodes: {set(nodes) - seen}")
    if original_ids - set(nodes) - {"RealizedEntity", "AbstractEntity"}:
        raise ValueError("An inherited nonroot record was lost")

    data["nodes"] = sorted(nodes.values(), key=lambda n: (n["label"].lower(), n["id"]))
    data.update(root="Entity", rootNodes=["Entity"])
    data["source"]["overlayPolicy"] = (
        "Accepted Particular/Predicable root, six Particular categories and Object/Occurrence/Feature branches; "
        "provisional single-parent graft of inherited descendants, with visible sense annotations.")
    data["source"]["graftDefinitions"] = "Ontology.md#accepted-decision-particulars-six-principal-categories"
    data["stats"] = {
        "nodeCount": len(nodes), "projectedEdgeCount": len(nodes) - 1,
        "multipleParentNodeCount": 0,
        "unaryNodeCount": sum(len(n["children"]) == 1 for n in nodes.values()),
        "definitionCount": sum(bool(n.get("definition")) for n in nodes.values()),
        "acceptedUpperNodeCount": len(UPPER) + 1,
        "provisionalPlacementCount": sum(bool(n.get("provisionalParent")) for n in nodes.values()),
    }
    data["unaryNodes"] = [n["id"] for n in data["nodes"] if len(n["children"]) == 1]
    data["upperGraft"] = {
        "generator": "graft_upper_ontology.py", "status": "provisional descendant placements",
        "retiredRootIds": ["RealizedEntity", "AbstractEntity"],
        "baselineSha256": data.get("upperGraft", {}).get("baselineSha256"),
        "policy": "Preserve inherited nonroot records; retain one displayed parent; review deeper inherited claims separately.",
    }
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=ROOT / "ontology.json")
    parser.add_argument("--output", type=Path, default=ROOT / "ontology.json")
    args = parser.parse_args()
    original = args.input.read_bytes()
    data = json.loads(original)
    baseline = data.get("upperGraft", {}).get("baselineSha256") or hashlib.sha256(original).hexdigest()
    output = graft(data, accepted_definitions((ROOT / "Ontology.md").read_text()))
    output["upperGraft"]["baselineSha256"] = baseline
    encoded = json.dumps(output, separators=(",", ":"), ensure_ascii=True) + "\n"
    if args.output.resolve() == args.input.resolve() and args.input.read_bytes() != original:
        raise RuntimeError("Input changed during graft; reread and retry")
    # Preserve the inode of an existing publication file.
    with args.output.open("w", encoding="utf-8") as stream:
        stream.write(encoded)
    print(json.dumps(output["stats"]))


if __name__ == "__main__":
    main()
