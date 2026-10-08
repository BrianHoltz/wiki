# Ontology Design Decisions and Memoranda

These notes capture the design conclusions and open questions from the latest review of `Ontology.md`. They should guide the next revision. Do **not** treat every point below as a settled ontological commitment; distinguish **decisions**, **working hypotheses**, and **questions to stress-test**.

## 1. Project Goal

The project has evolved beyond its original 20 Questions motivation.

The goal is now to develop a **general-purpose, scientifically respectable, mathematically informed, durable ontology of entities/concepts** that:

- is approachable and explorable by humans;
- is compatible with serious work in formal ontology, logic, mathematics, information science, and AI;
- avoids obvious category mistakes;
- should remain useful as AI systems become dramatically better at formal reasoning;
- can support a canonical human-readable tree without assuming reality itself is fundamentally tree-shaped;
- gets to ordinary entities such as physical objects and organisms without requiring an absurdly deep traversal through metaphysical machinery.

20 Questions discrimination efficiency is no longer a primary design criterion.

---

## 2. Fundamental Architecture: Ontology vs. Canonical Tree

**Important decision:** distinguish the underlying ontology from its canonical tree representation.

The underlying ontology should be allowed to be richer than a tree:

- graph/DAG structure;
- multiple relations among entities;
- multiple orthogonal classification dimensions;
- metadata and formal constraints;
- potentially multiple inheritance where justified.

The tree should be understood as a **privileged/canonical projection of that richer ontology**.

This is a deeper distinction than merely:

> structured source file → generated HTML

There are therefore two different senses of "projection":

1. **Implementation projection:** structured ontology data → generated HTML/UI.
2. **Ontological projection:** rich multidimensional ontology → canonical tree.

The ontology is the source of truth. The canonical tree is a deliberately chosen, privileged view of it.

Do not casually describe reality itself as necessarily tree-shaped.

---

## 3. Criteria for the Canonical Tree

Preserve these explicitly in the document as design criteria.

### 3.1 Exhaustiveness

At an intended exhaustive split, the children should collectively cover the parent:

> Every instance of the parent should fall under at least one child.

In logical language, seek **joint exhaustiveness** where the split purports to be exhaustive.

### 3.2 Mutual Exclusivity / Disjointness

Where possible and appropriate, sibling categories should be disjoint:

> An instance should not simultaneously belong to multiple siblings under the same partition.

This is **mutual exclusivity**.

Do not pretend a partition is disjoint where the subject matter does not justify it.

### 3.3 Uniform Edge Semantics

The edges used to generate the canonical tree should have a consistent meaning.

Do not casually mix relationships such as:

- `is-a`
- `instance-of`
- `part-of`
- `has-property`
- `studied-by`
- `used-for`

as though they were the same hierarchical relationship.

A major open design question is exactly **which relation generates the canonical tree**. `is-a` / subtype classification is the leading candidate.

### 3.4 Single Canonical Parent

For purposes of the canonical tree, every non-root node should have one canonical parent.

The underlying ontology may contain multiple inheritance or other relationships. The tree projection nevertheless chooses one canonical route.

### 3.5 Principled Sibling Splits

A sibling set should ideally result from **one coherent discriminating principle or dimension**.

Avoid partitions such as:

> A / B / C

where A is distinguished by material composition, B by temporal behavior, and C by epistemic status.

That creates a tree-shaped list rather than a principled taxonomy.

### 3.6 Traversal Intelligibility

A human walking from root toward an ordinary concept should encounter distinctions that make conceptual sense.

Each level should **earn its place**.

Avoid "upper-ontology bloat" in which `Dog`, `Person`, `Mountain`, etc. require traversing fifteen layers of distinctions that matter primarily to specialists.

---

## 4. Dimensions Are Not a Cop-Out

Earlier resistance to multidimensional classification should be reconsidered.

A rich ontology may legitimately classify entities along several largely independent dimensions, for example:

- concrete / abstract;
- particular / universal;
- dependent / independent;
- continuant / occurrent;
- actual / possible / fictional;
- material / informational.

These should **not yet be adopted as the canonical dimensions**. They are examples illustrating the architecture.

A useful way to evaluate candidate dimensions is to examine their Cartesian product.

For dimensions A, B, C, etc., ask:

- What does each combination mean?
- Is the combination coherent?
- Is it populated?
- If many combinations are impossible, why?
- Does that reveal a genuine constraint on reality, or merely show that the proposed dimensions were not independent?

Empty cells are not automatically defects. They may encode genuine impossibility.

However, large numbers of accidental or inexplicable empty cells are evidence that the dimensions may not be as orthogonal/fundamental as claimed.

Desired properties of dimensions include:

- coverage;
- semantic clarity;
- as much independence/orthogonality as is defensible;
- determinate applicability where the dimension claims universality.

This idea is analogous in spirit—not formally equivalent—to appreciating high-dimensional representations in modern ML: **dimensionality itself is not a defect**.

---

## 5. Reconsider the Current Entity / Property / Relation Triad

The existing top-level triad has substantial intuitive appeal:

> Entity / Property / Relation

Its attraction comes partly from predication:

- there are things we talk about;
- we say things *of* them via properties;
- we connect them to other things via relations.

This feels exhaustive from the standpoint of describing things.

However, there is a serious objection:

> This may classify **roles in representation/predication**, rather than fundamental kinds of being.

That distinction must be taken seriously.

### Property vs. Attribute

Prefer **Property** over **Attribute** for the present purpose.

"Attribute" often suggests a narrower entity–attribute–value model.

"Property" is broader and has stronger precedent in philosophy/formal ontology, although it is overloaded and must eventually be defined explicitly.

Be aware that in RDF/OWL terminology a "property" is itself effectively a relation, so terminology across disciplines is not uniform.

### Property as Unary Relation

From a logical perspective:

- a property can be modeled as a unary predicate/relation;
- ordinary relations have arity >= 2.

Thus:

> Property may be a special case of Relation/Predicate rather than a coordinate top-level category.

This suggests possible simplification:

> Object / Predicate

rather than:

> Entity / Property / Relation

But **do not adopt this dyad yet**. It requires further stress testing.

---

## 6. Entity vs. Object

`Entity` currently looks more promising as the absolute root than `Object`.

Possible working definition:

> **Entity:** anything admitted by the ontology as something about which claims can be made / over which discourse can quantify.

This deliberately permits a very broad universe.

Potential entities can include:

- physical objects;
- events;
- numbers;
- sets;
- propositions;
- properties;
- relations;
- algorithms;
- organizations;
- fictional entities, if the ontology elects to admit them.

This leads to an important recursive feature:

**Properties and relations can themselves be entities.**

For example, we should be able to assert:

- `larger-than` has arity 2;
- `larger-than` is transitive;
- `larger-than` is asymmetric;
- `larger-than` is the inverse of `smaller-than`.

Thus a relation can itself become the object of predication.

Likewise:

- properties can have properties;
- relations can participate in relations;
- propositions can have properties;
- classes can stand in relations to classes.

This recursion is not inherently a defect.

---

## 7. Kind vs. Role

This distinction should become explicit in the document.

A **kind/category** answers approximately:

> What sort of thing is this?

A **role** can instead answer:

> How is this thing functioning in this representation/relationship?

For example:

```text
Loves(Alice, Bob)
```

Here `Loves` functions as a binary predicate.

But we can reify that predicate and make claims about it:

```text
arity(Loves, 2)
symmetric(Loves, false)
```

Now `Loves` is itself functioning as an object of predication.

Therefore:

> `Predicate`, `Property`, and `Relation` may be better understood at least partly as predicative roles rather than mutually exclusive fundamental kinds of entity.

This is one of the main reasons not to commit prematurely to `Entity / Property / Relation` as three peer ontological categories.

---

## 8. Russell, Self-Reference, and Formal Discipline

Russell's paradox and the historical development from Russell/Whitehead through modern type theory are relevant as **warnings about unrestricted formal self-reference**, not as reasons to prohibit talking about relations, properties, classes, etc. as entities.

The lesson should not be:

> Relations cannot themselves be entities.

Rather:

> A sufficiently expressive system needs disciplined semantics/types/levels so that unrestricted comprehension and pathological self-reference do not make the formal system inconsistent.

The ontology should therefore be semantically generous while remaining compatible with a disciplined formalization.

Do not attempt to solve foundational mathematics inside this project.

---

## 9. Type Theory: Relevance to the Project

The software-engineering intuition about types is a legitimate entry point:

```text
42 : Int
```

Type theory generalizes this idea into foundational logic.

In dependent type theory, types can depend upon values.

The especially important conceptual leap is the Curry–Howard correspondence:

> propositions correspond to types;  
> proofs correspond to inhabitants/values of those types.

This helps explain the power of systems such as Lean.

**The project should NOT become a type-theory project or a Lean project.**

Instead, adopt the following explicit stress test:

> **Could a competent type theorist or formal logician translate our ontology/schema into a disciplined typed formalism without first having to repair fundamental category mistakes?**

That is approximately the right amount of respect to give formal methods for this project's purposes.

Formalizability is a design-quality criterion, not the project's immediate deliverable.

---

## 10. Do Not Confuse Types, Instances, Words, and Concepts

This remains an important category-error hazard.

For example:

- `Dog` as a class/type;
- Fido as an individual/instance;
- `"dog"` as a linguistic token/string;
- the concept of dog as a cognitive/semantic object.

These are not automatically the same kind of thing.

The ontology must make its intended level explicit rather than casually placing all of these in the same hierarchy.

The canonical tree therefore needs an explicit answer to:

> **What sorts of nodes does the tree contain, and what exactly does a parent→child edge mean?**

---

## 11. Avoid Fields-of-Study Taxonomies

A previous failure mode was drifting toward topics or academic disciplines.

This ontology is **not** intended to be a Dewey Decimal classification of knowledge.

Nodes should denote kinds/entities/concepts admitted by the ontology—not merely fields that study them.

For example, be suspicious of nodes such as:

- Physics;
- Biology;
- Economics;

when they actually mean "the domain studied by physics/biology/economics."

Distinguish the subject matter from the discipline studying it.

---

## 12. DOLCE-Style Four-Way Partition: Do Not Adopt Yet

A serious competing approach divides entities along lines resembling:

- endurant;
- perdurant;
- quality;
- abstract.

This has respectable provenance, particularly in DOLCE and related formal-ontology/metaphysical traditions.

It should be steelmanned, but there are concerns.

### Concern: Temporal Metaphysics

The endurant/perdurant distinction gives substantial ontological weight to persistence through time.

That may import metaphysical commitments that are inappropriate at the very top of a maximally durable ontology.

Relativity does **not** establish that time is unreal. However, the absence of a universal observer-independent present and the viability of four-dimensional/block-universe interpretations are sufficient reasons to hesitate before making persistence-through-time one of the deepest partitions in the system.

A person, for example, can be modeled as an enduring three-dimensional entity or as a four-dimensional spacetime entity with temporal parts.

A root taxonomy should ideally not accidentally prejudge that dispute.

### Concern: "Abstract" as Junk Drawer

A partition such as:

> Endurant / Perdurant / Quality / Abstract

risks making `Abstract` the bucket for everything that does not fit the first three:

- numbers;
- sets;
- propositions;
- algorithms;
- information;
- fictional entities;
- social institutions;
- currencies;
- games;
- etc.

A huge residual category is evidence that the partition may not be doing enough explanatory work for this project's purposes.

Therefore the DOLCE-like approach remains an important competitor/stress test, not the current winner.

---

## 13. Avoid Over-Indexing on Any Single Metaphysical School

The project should remain aware of the different motivations of major traditions.

Roughly:

- **BFO:** realist/formal ontology; asks what fundamental categories of reality exist.
- **DOLCE:** descriptive/cognitive/linguistic orientation; captures conceptual distinctions useful in human description.
- **SUMO:** broad AI/knowledge-representation ontology intended for practical formal coverage.
- **Type-theoretic/formal foundations:** primarily address disciplined representation, construction, inference and proof rather than simply supplying a taxonomy of reality.

These are not merely competing implementations of the exact same project.

Their differing purposes explain some of their differing top-level structures.

---

## 14. Major Open Question: What Are the Immediate Children of Entity?

This should now be treated as the central unresolved design question.

If:

> `Entity = anything admitted as an object of discourse`

then ask:

> **What, if anything, provides the most defensible mutually exhaustive immediate partition of Entity?**

Candidates to investigate include:

1. the current Entity/Property/Relation idea;
2. Object/Predicate;
3. particular/universal;
4. concrete/abstract;
5. DOLCE-style categories;
6. BFO-inspired distinctions;
7. SUMO's structure;
8. mathematically/type-theoretically informed alternatives;
9. **no mandatory exhaustive level-1 partition**, with several orthogonal dimensions instead.

Do not assume in advance that a beautiful three-way or four-way cut must exist.

---

## 15. Important Possibility: Entity May Be the Only Truly Universal Tree Node

Take seriously the possibility that the maximally rigorous underlying structure looks initially disappointing:

```text
Entity
```

followed by several orthogonal classification systems rather than one uniquely correct exhaustive partition.

The canonical tree could then choose one principled projection through those dimensions.

This would permit us to maintain:

> **There is a canonical tree**

without making the much stronger claim:

> **There is one intrinsically correct tree-shaped decomposition of reality.**

The canonical tree earns its status through explicit design criteria rather than by pretending that all ontological structure is inherently arboreal.

---

## 16. AI/Future-Proofing Criterion

Do not optimize specifically for Lean or today's LLM architectures.

Instead optimize for:

- semantic clarity;
- explicit commitments;
- formalizability;
- machine-readable structure;
- principled distinctions;
- resistance to category mistakes;
- ability to generate and test counterexamples;
- compatibility with future automated formal reasoning.

A plausible near-future frontier model should be able to ingest this ontology, formalize substantial portions of it, compare it mechanically against other ontologies, generate pathological cases, and identify inconsistent or redundant distinctions.

Design the ontology so that such systems can **leverage it rather than first repair it**.

There probably is no theorem proving the uniquely correct ontology. Some decisions will continue to involve purpose, metaphysical commitments, and taste even as automated reasoning improves dramatically.

---

## 17. Immediate Next Research Task

Do **not** start rearranging the canonical tree merely because of this discussion.

First conduct a focused comparison of candidate upper structures.

For each candidate top-level partition, require:

1. **Precise definitions** of every category.
2. **Provenance** — which serious ontology/logical tradition uses it and why.
3. **Exhaustiveness argument** — why should everything fall somewhere?
4. **Disjointness argument** — why should sibling categories not overlap?
5. **Single-principle test** — are all siblings distinguished along the same axis?
6. **Edge-case torture test** using at least:
   - physical object;
   - organism;
   - person;
   - event;
   - process;
   - spacetime region;
   - property such as redness;
   - relation such as larger-than;
   - number;
   - set;
   - proposition;
   - proof;
   - algorithm;
   - information;
   - corporation;
   - currency;
   - fictional character.
7. **Reification test** — can properties, relations, propositions, etc. themselves become objects of discourse?
8. **Physics neutrality test** — does the partition unnecessarily commit us to controversial temporal/material metaphysics?
9. **Formalization test** — could it be represented cleanly in modern typed/formal systems?
10. **Human traversal test** — how many meaningful steps separate `Entity` from ordinary concepts such as `Organism`, `Person`, and `Dog`?

The goal of this exercise is not to find whichever existing ontology we can copy.

The goal is to determine which distinctions deserve to survive into **our ontology**, and which belong instead as orthogonal dimensions, secondary relations, metadata, or alternate projections.
