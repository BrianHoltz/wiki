#!/usr/bin/env python3
"""Overlay SUMO data with the project's canonical ontology."""

from __future__ import annotations

import argparse
import copy
import json
from collections import defaultdict
from pathlib import Path


def node(identifier: str, label: str, definition: str, *children: dict) -> dict:
    return {
        "id": identifier,
        "label": label,
        "definition": definition,
        "children": list(children),
    }


CANONICAL = node(
    "Entity",
    "Entity",
    "That which can be referred to.",
    node(
        "Object",
        "Object",
        "A first-order entity considered apart from its properties and relations.",
        node(
            "RealizedEntity",
            "Realized entity",
            "An entity that takes no arguments and has spatiotemporal embodiment.",
        ),
        node(
            "AbstractEntity",
            "Abstract entity",
            "An entity that takes no arguments and lacks spatiotemporal embodiment.",
            node(
                "MathematicalEntity",
                "Mathematical entity",
                "An abstract entity used in mathematical description, reasoning, or construction.",
                node("Number", "Number", "An entity that specifies a count, magnitude, or position."),
                node("Set", "Set", "A collection treated as one abstract entity."),
                node("Function", "Function", "A rule or entity that assigns each allowed input a result."),
                node("LogicalEntity", "Logical entity", "An entity used to express or evaluate logical form."),
                node("AlgebraicEntity", "Algebraic entity", "An entity defined through algebraic operations or laws."),
                node(
                    "GeometricEntity",
                    "Geometric entity",
                    "An entity characterized by spatial form, location, or extension.",
                    node("Curve", "Curve", "A one-dimensional geometric entity that varies continuously."),
                    node("Circle", "Circle", "A plane curve whose points are equidistant from a center."),
                    node("Ellipse", "Ellipse", "A closed plane curve whose distances to two foci have a constant sum."),
                    node("Parabola", "Parabola", "A plane curve whose points are equidistant from a focus and a directrix."),
                    node("Hyperbola", "Hyperbola", "A curve whose points have a constant difference of distances to two foci."),
                ),
                node("TopologicalEntity", "Topological entity", "An entity defined by continuity, neighborhood, or connectedness."),
                node("AnalyticEntity", "Analytic entity", "An entity defined through limits, variation, or analytic operations."),
                node("ProbabilityEntity", "Probability entity", "An entity used to represent chance, uncertainty, or distribution."),
                node(
                    "ComputationalEntity",
                    "Computational entity",
                    "An entity used to specify, perform, or analyze computation.",
                    node("Algorithm", "Algorithm", "A finite, effective procedure for producing a result."),
                    node("ComplexityClass", "Complexity class", "A set of computational problems sharing a resource bound."),
                    node("ComputableFunction", "Computable function", "A function for which an effective computation produces each result."),
                    node("RecursiveFunction", "Recursive function", "A function defined from initial functions by recursion and composition."),
                    node("Automaton", "Automaton", "An abstract machine that changes state while processing input."),
                    node("FormalLanguage", "Formal language", "A set of strings formed according to specified symbols and rules."),
                    node("Graph", "Graph", "An entity consisting of vertices connected by edges."),
                ),
                node("PhysicalSystemModel", "Physical system model", "A mathematical entity representing a physical system."),
                node("FormalExpression", "Formal expression", "A well-formed symbolic construction in a formal language."),
                node("Proposition", "Proposition", "An entity that can be asserted and evaluated as true or false."),
                node("Theorem", "Theorem", "A proposition established by an accepted proof."),
                node("Proof", "Proof", "A finite argument that establishes a proposition from accepted premises."),
                node("Definition", "Definition", "An expression that fixes the meaning or use of a term."),
                node("MathematicalModel", "Mathematical model", "A mathematical representation of a target system or situation."),
            ),
            node(
                "InformationalEntity",
                "Informational entity",
                "An entity whose identity depends on content, evidence, or information.",
                node("Data", "Data", "Recorded content available for interpretation or processing."),
                node("Record", "Record", "A bounded account of data retained for reference."),
                node("Dataset", "Dataset", "A collection of related data items treated as a unit."),
                node("Signal", "Signal", "A perceivable variation that conveys or can convey information."),
                node("Message", "Message", "Information intended to be conveyed from a source to a recipient."),
                node("Observation", "Observation", "Information acquired by attending to an entity or event."),
                node("Measurement", "Measurement", "A reported comparison of a quantity with a scale or standard."),
                node("Fact", "Fact", "A proposition treated as supported or established."),
                node("Knowledge", "Knowledge", "Information regarded as understood, justified, or usable."),
                node("Belief", "Belief", "A proposition or representation accepted by an agent."),
            ),
            node(
                "RepresentationalEntity",
                "Representational entity",
                "An entity that encodes, expresses, preserves, or transmits content.",
                node("Symbol", "Symbol", "An entity used to stand for or evoke another entity or meaning."),
                node("Name", "Name", "A symbol or expression used to identify an entity."),
                node("Label", "Label", "A name or mark attached to an entity for identification or classification."),
                node("Notation", "Notation", "A conventional system of symbols used to express entities or relations."),
                node("Description", "Description", "A representation that conveys characteristics of an entity."),
                node("Classification", "Classification", "A representation that assigns entities to categories."),
                node("Schema", "Schema", "A formal plan for the organization of information."),
                node(
                    "OntologyRepresentation",
                    "Ontology",
                    "A structured account of kinds and relations in a domain.",
                ),
                node("Language", "Language", "A conventional system for expressing and interpreting messages."),
                node("Document", "Document", "A bounded representational work preserved for reading or reference."),
                node("Image", "Image", "A representation that conveys visual form or appearance."),
                node("Audio", "Audio", "A representation or recording of sound."),
                node("Video", "Video", "A representation or recording of moving images, usually with sound."),
                node("Software", "Software", "A program or related information used to control computation."),
                node("Model", "Model", "A representation used to describe, explain, predict, or guide."),
            ),
            node(
                "SocialEntity",
                "Social entity",
                "An entity whose persistence depends on participants, recognition, or shared practice.",
                node("Person", "Person", "An individual human being considered as a social participant."),
                node("Group", "Group", "A collection of people treated as a social unit."),
                node("Community", "Community", "People connected by shared place, identity, activity, or practice."),
                node("Relationship", "Relationship", "A socially recognized connection between participants."),
                node("Role", "Role", "A socially recognized position with associated expectations."),
                node("Status", "Status", "A socially recognized standing or condition."),
                node("Agreement", "Agreement", "A shared commitment or alignment between participants."),
                node("Convention", "Convention", "A practice or meaning maintained by social acceptance."),
                node("Practice", "Practice", "A recurring activity or method maintained by participants."),
                node("Event", "Event", "A bounded occurrence recognized as socially or otherwise significant."),
                node("Institution", "Institution", "A durable social arrangement organized around recognized practices or rules."),
            ),
            node(
                "InstitutionalEntity",
                "Institutional entity",
                "A durable rule-governed social entity with recognized functions or authority.",
                node("Organization", "Organization", "A coordinated group with a persistent identity or purpose."),
                node("Government", "Government", "An institution exercising public authority over a community or territory."),
                node("Corporation", "Corporation", "A legally recognized organization with a distinct institutional identity."),
                node("Club", "Club", "An organization formed around shared membership or activity."),
                node("School", "School", "An institution organized for teaching, learning, or scholarly activity."),
                node("Court", "Court", "An institution authorized to interpret or apply law."),
                node("Market", "Market", "An institution or arrangement for exchange among participants."),
                node("Currency", "Currency", "A socially or institutionally accepted medium of exchange."),
                node("Law", "Law", "A rule recognized and enforced by an authority or legal system."),
                node("Contract", "Contract", "An agreement recognized as creating enforceable commitments."),
                node("License", "License", "An authorization granted under specified conditions."),
                node("Policy", "Policy", "A rule or principle adopted to guide decisions or conduct."),
                node("Office", "Office", "An institutional position or the authority associated with it."),
            ),
        ),
    ),
    node(
        "Property",
        "Property",
        "An entity that takes one argument.",
        node("Quality", "Quality", "A characteristic describing how an entity is."),
        node("Quantity", "Quantity", "A property specifying how many, how much, or to what extent."),
        node("QualityValue", "Quality value", "A value that specifies a quality on a scale or comparison."),
        node("Disposition", "Disposition", "A property that makes an entity liable to behave in a certain way."),
        node("Capability", "Capability", "A property representing what an entity can do or undergo."),
        node("Function", "Function", "A use or activity an entity is suited or intended to perform."),
        node("Purpose", "Purpose", "An intended end that guides an entity or activity."),
        node("Role", "Role", "A property describing an entity's place in a context or activity."),
        node("Status", "Status", "A property describing a recognized condition or standing."),
        node("Norm", "Norm", "A rule or standard specifying expected conduct or form."),
        node("Obligation", "Obligation", "A requirement binding an agent to an action or state."),
        node("Goal", "Goal", "A desired or intended state treated as an end."),
        node("Preference", "Preference", "A disposition to favor one option or state over another."),
        node("ModalProperty", "Modal property", "A property concerning possibility, necessity, or contingency."),
        node("LogicalProperty", "Logical property", "A property defined by logical form or consequence."),
        node("MathematicalProperty", "Mathematical property", "A characteristic defined or established mathematically."),
    ),
    node(
        "Relation",
        "Relation",
        "An entity that takes more than one argument.",
        node("ClassificationRelation", "Classification relation", "A relation that assigns an entity to a kind or category."),
        node("PartWholeRelation", "Part-whole relation", "A relation between a whole and one of its parts."),
        node("SpatialRelation", "Spatial relation", "A relation concerning location, distance, direction, or containment."),
        node("TemporalRelation", "Temporal relation", "A relation concerning time, sequence, or duration."),
        node("CausalRelation", "Causal relation", "A relation in which one entity contributes to an effect."),
        node("ExplanatoryRelation", "Explanatory relation", "A relation in which one entity accounts for another."),
        node("ParticipationRelation", "Participation relation", "A relation connecting an entity with an event or process it takes part in."),
        node("SocialRelation", "Social relation", "A relation constituted by social interaction or recognition."),
        node("InstitutionalRelation", "Institutional relation", "A relation defined by an institution, rule, or office."),
        node("PerceptualRelation", "Perceptual relation", "A relation between a perceiver and what is perceived."),
        node("EpistemicRelation", "Epistemic relation", "A relation concerning knowledge, belief, evidence, or justification."),
        node("LogicalRelation", "Logical relation", "A relation defined by logical form or consequence."),
        node("SetTheoreticRelation", "Set-theoretic relation", "A relation involving sets, membership, inclusion, or ordering."),
        node("MathematicalRelation", "Mathematical relation", "A relation defined between mathematical entities."),
        node("TransformationRelation", "Transformation relation", "A relation connecting an entity to a result of changing it."),
        node("RepresentationalRelation", "Representational relation", "A relation between content and what represents, encodes, or denotes it."),
        node("IdentityRelation", "Identity relation", "A relation stating that entities are the same entity."),
        node("EquivalenceRelation", "Equivalence relation", "A relation grouping entities as interchangeable under specified criteria."),
        node("ProvenanceRelation", "Provenance relation", "A relation recording an entity's source, derivation, or history."),
    ),
)


def flatten(tree: dict, parent: str | None = None) -> tuple[dict[str, dict], dict[str, list[str]]]:
    records: dict[str, dict] = {}
    parents: dict[str, list[str]] = defaultdict(list)

    def visit(current: dict, current_parent: str | None) -> None:
        identifier = current["id"]
        if identifier in records:
            if current_parent and current_parent not in parents[identifier]:
                parents[identifier].append(current_parent)
            return
        records[identifier] = {
            "id": identifier,
            "label": current["label"],
            "definition": current["definition"],
            "definitionSource": "project editorial",
            "children": [],
            "alternateParents": [],
            "directParentCount": 0,
            "provisionalParent": None,
        }
        if current_parent:
            parents[identifier].append(current_parent)
        for child in current["children"]:
            if child["id"] in records:
                parents[child["id"]].append(identifier)
            else:
                visit(child, identifier)
                records[identifier]["children"].append(child["id"])

    visit(tree, parent)
    return records, parents


def overlay(input_path: Path, output_path: Path) -> None:
    data = json.loads(input_path.read_text(encoding="utf-8"))
    old = {item["id"]: item for item in data["nodes"]}
    physical_ids: set[str] = set()
    stack = ["Physical"]
    while stack:
        identifier = stack.pop()
        if identifier in physical_ids or identifier not in old:
            continue
        physical_ids.add(identifier)
        stack.extend(old[identifier]["children"])

    physical = {}
    for identifier in physical_ids:
        record = copy.deepcopy(old[identifier])
        record["children"] = [child for child in record["children"] if child in physical_ids]
        record["alternateParents"] = [
            parent for parent in record.get("alternateParents", []) if parent in physical_ids
        ]
        physical[identifier] = record
    physical_root = copy.deepcopy(physical.pop("Physical"))
    physical_object = physical.pop("Object", None)
    if physical_object:
        physical["Object"] = physical_object
    physical_root["id"] = "RealizedEntity"
    physical_root["label"] = "Realized entity"
    physical_root["definition"] = "An entity that takes no arguments and has spatiotemporal embodiment."
    physical_root["definitionSource"] = "project editorial"
    physical["RealizedEntity"] = physical_root

    canonical, parents = flatten(CANONICAL)
    canonical.pop("Object")
    canonical["Entity"]["children"] = ["RealizedEntity", "AbstractEntity", "Property", "Relation"]
    parents.pop("Object")
    parents["RealizedEntity"] = ["Entity"]
    parents["AbstractEntity"] = ["Entity"]
    records = {**canonical, **physical}
    records["Object"]["definition"] = "A realized entity regarded as persisting through time."
    records["Process"]["definition"] = "A realized entity regarded as occurring through time."
    for identifier, record in records.items():
        record["children"] = [child for child in record["children"] if child in records]
        record["directParentCount"] = len(parents.get(identifier, []))
        record["alternateParents"] = [
            parent for parent in parents.get(identifier, [])[1:] if parent != "Entity"
        ]
    records["RealizedEntity"]["directParentCount"] = 1
    records["RealizedEntity"]["alternateParents"] = []
    records["Entity"]["directParentCount"] = 0
    for record in records.values():
        if record.get("definitionSource") == "SUMO KIF":
            record["definitionSource"] = "source KIF"

    nodes = sorted(records.values(), key=lambda item: (item["label"].lower(), item["id"]))
    selected_edges = sum(len(item["children"]) for item in nodes)
    output = {
        "source": {
            "name": "My Ontology",
            "upperOntology": "Ontology/Ontology.md#upper-ontologies",
            "overlayPolicy": (
                "Use the project canonical Entity/RealizedEntity/AbstractEntity/Property/Relation "
                "projection with source-linked descendants."
            ),
        },
        "stats": {
            "nodeCount": len(nodes),
            "projectedEdgeCount": selected_edges,
            "multipleParentNodeCount": sum(bool(item["alternateParents"]) for item in nodes),
            "unaryNodeCount": sum(len(item["children"]) == 1 for item in nodes),
            "definitionCount": sum(bool(item.get("definition")) for item in nodes),
            "canonicalNodeCount": len(canonical),
            "physicalNodeCount": len(physical),
        },
        "root": "Entity",
        "rootNodes": ["Entity"],
        "nodes": nodes,
        "unaryNodes": [item["id"] for item in nodes if len(item["children"]) == 1],
        "organismGraft": data.get("organismGraft"),
    }
    output_path.write_text(json.dumps(output, separators=(",", ":")), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    overlay(args.input, args.output)


if __name__ == "__main__":
    main()
