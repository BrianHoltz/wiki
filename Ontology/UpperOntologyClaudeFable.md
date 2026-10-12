# An Upper Ontology Rooted at Entity: Independent Proposal

**Model:** the session is configured for the model identifier `claude-fable-5-1` (Anthropic); the model actually serving a given turn can differ, and I cannot verify it from inside the session. **Reasoning setting:** not known to me; not stated.
**Date:** 11 October 2026.

**Independence statement.** I did not search for, open, or use any material from the requester's project, any earlier conversation, or any stored context about the requester. The only project-specific inputs were the two given in the brief: the root label *Entity* and its working definition. Nothing I retrieved during research looked like the requester's own ontology or wiki, so I have no exposure to report. Everything below is either attributed to an external source (keys in square brackets, listed in §13) or is my own design choice, and I say which.

---

## 1. Summary of the recommendation

1. **Three orthogonal dimensions, only one of which is the is-a tree.** Categorial form (what sort of thing it is) is the subclass tree. Subject domain (physical, biological, mental, social, informational, mathematical, logical, fictional) is a navigation facet. Ontic status (whether and how it is asserted to exist) is an attribute. The precedent is Husserl's separation of formal categories from material regions and Ingarden's addition of existential categories as a third dimension [SEP-Cat §1.3]. The three-way separation as applied here is my choice.
2. **First cut by instantiability:** Particular versus Predicable. This replaces abstract/concrete, which the tree never uses as a dividing line.
3. **Six kinds of particular,** distinguished by how each is individuated and what it depends on: Object, Occurrence, Feature, Region, Construct, Formal Object. Works, institutions and fictional characters get a home (Construct) that is neither "concrete" nor Platonic.
4. **A visible Predicable layer** above Property and Relation, with the arity split (Property/Relation) kept strictly separate from the metaphysical split (Kind/Phase/Role/Attribute).
5. **Tree nodes must be rigid classes.** Value, carrier, capability, pet, referent and similar notions are roles, so they appear as instances of Role and never as tree nodes above rigid classes.
6. **Fictional and impossible items are admitted once,** as Characterized Objects, with two modes of predication: what they are characterized as, and what they are instances of.

The tree has 40 nodes including the root. Its deepest displayed nodes are three subclass edges below Entity; nothing has been flattened to make it fit.

---

## 2. The root: critique and replacement definition

### 2.1 Problems with "that which can be referred to, even if nonexistent"

**(a) It quietly picks a side on reference.** On the mainstream reading, reference is a success relation: a term refers only if there is something it refers to. On that reading "can be referred to, even if nonexistent" requires that there be nonexistent relata, which is Meinong's position and is rejected by Hume, Kant, Frege and Quine [SEP-NE §1]. If instead "referred to" means *purportedly* referred to, the definition describes a feature of words and thoughts, and the phrase "that which" has nothing to pick out in the failure cases. Either way a metaphysical commitment is made without being announced.

**(b) The modal "can" is unanchored.** Referable by whom, with what language? Any language with countably many expressions leaves almost all real numbers without an individual name. Either they are not entities, or "can" is idealised until it means no more than "is something," and the definition is circular.

**(c) It gives no criterion of identity.** "The tallest spy," "a unicorn," "the average household," and "Sherlock Holmes as played in each adaptation" all purport to refer. Is there one entity per description, per name, per source? The definition cannot say, so it cannot support counting or de-duplication. Dummett's diagnosis applies: "thing," "entity" and "object" supply no identity criterion and so are not genuine sortal terms [SEP-Cat §2.3]. Aristotle's older argument that being is not a genus points the same way [SEP-Cat §1.1].

**(d) Grammar over-generates.** Noun phrases refer grammatically without there being anything suitable: *John's sake*, *the lack of rain*, *the dint* of effort. A definition keyed to referring expressions admits them.

**(e) Unrestricted admission of described items is inconsistent.** If every characterization yields an entity that has the characterizing properties, then "the existent golden mountain" exists and "the round square" is both round and not round. These are Russell's objections to Meinong's original theory [SEP-NE §4]. Every consistent successor theory restricts the principle in some way [SEP-NE §5].

**(f) "Nonexistent" lumps together different statuses.** The dodo (existed, no longer does), Vulcan (posited, refuted), Holmes (created as fiction), the round square (cannot exist), and the number 7 (existence disputed among philosophers of mathematics) are not "nonexistent" in one sense.

### 2.2 Proposed definition

> **Entity** — anything admitted as a value of the ontology's variables: an item that falls under at least one category of this ontology whose definition supplies or inherits a criterion of identity, so that it can be told apart from other items, counted, and made the subject of predication. Being an entity does not entail existing; every entity carries an explicit *ontic status*.

This is an elucidation of a root, not a definition by genus and difference, because a root has no genus. Three things it deliberately separates:

| Notion               | What it is here                                                                                                                                                                                                         | Not to be confused with                                         |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **Entityhood** | Membership in the ontology's*outer* domain: the domain the neutral quantifier ranges over.                                                                                                                            | Existence.                                                      |
| **Existence**  | An attribute (`onticStatus`), with an existence predicate E! picking out an *inner* domain relative to time. "Some entities do not exist" is written ∃x¬E!x.                                                      | A class. There is no node*Existent* or *Nonexistent*.       |
| **Reference**  | A success relation `refersTo(r, e)` from a representation *r* (a use of a Symbolic Form, or an Attitude) to an entity *e*. A term that fails to refer is a term with no referent; it does not thereby create one. | Purported reference, which is a property of the representation. |

The two-domain regimentation follows the practice of Parsons, Zalta and Jacquette as reported in [SEP-NE §1.1]; Priest's alternative is a single quantifier read as ontologically neutral. Choosing the two-domain form is my design choice. It commits the ontology to *talking about* items of every status, and to nothing about which statuses are occupied. That is the descriptivist stance described in [SEP-Cat, introduction and §1.4].

**Admission rule** (mine). An item enters the outer domain in one of three ways:

- **A1, by attestation:** it is or was encountered, measured, or recorded (this rock, the dodo, the Battle of Hastings).
- **A2, by theory:** it is a value of the variables of an accepted theory or formal system (the electron, the number 7, the empty set).
- **A3, by sourced characterization:** a source characterizes it as an object, and the entry is anchored to that source (Holmes, Vulcan, the round square). Such items are Characterized Objects (§5.6). A bare description with no anchoring source ("the tallest spy") admits nothing.

**Ontic status values** (mine; a starting list, not a class hierarchy): *exists at t* (with past, present, future); *exists atemporally according to theory T*; *exists as a construct, unsatisfied*; *posited, open*; *posited, refuted*; *impossible*; *contested*. Status can change (Planet Nine may be found); category in the tree should not, which is why status is not a class.

---

## 3. What the nodes denote, and the fixed vocabulary of ties

### 3.1 Nodes and edges

- **Every node denotes a class:** all entities of the outer domain, of any ontic status, that satisfy the node's definition.
- **Every edge in the displayed tree means subclass inclusion:** *A* is under *B* only if, necessarily, every instance of *A* is an instance of *B*. No edge means instance-of, part-of, located-in, used-for, about, or characterized-as.
- **Every tree node is rigid:** an instance cannot cease to be an instance while remaining the same entity. This is the OntoClean constraint that an anti-rigid class cannot subsume a rigid one [OntoClean], applied here as a rule for building the tree.
- **Disjointness and exhaustiveness are never implied by layout.** They are stated per sibling group in §6.

### 3.2 Classes, kinds, and the instance/subclass discipline

Each class node *C* has an intensional counterpart κ(*C*), a predicable, such that *x* is an instance of *C* exactly when *x* instantiates κ(*C*). The counterpart is itself an entity and sits in the Predicable branch. So:

- *Secretariat* `instanceOf` **Horse**. (Individual to class.)
- **Horse** `subclassOf` **Organism**. (Class to class.)
- *the kind horse* `instanceOf` **Kind**. (A predicable to a class of predicables.)
- *the kind horse* `specializes` *the kind organism*. (Predicable to predicable; mirrors the subclass edge.)

What is never written: **Horse** `subclassOf` **Kind** (that says every horse is a kind), or *Secretariat* `instanceOf` **Kind**. Taxonomic ranks are kinds of kinds: *the kind horse* `instanceOf` **Species**, and **Species** `subclassOf` **Kind**. Confusing these levels is the best-documented structural fault in large public knowledge graphs; analyses of Wikidata found many items asserted to be both an instance and a subclass of the same thing [MLT-Wikidata; Wikidata-Disarray]. OWL 2 permits one name to be used for a class and an individual ("punning"), but under its direct semantics the two are distinct things that merely share a name [OWL-Pun]. This ontology states the correspondence κ explicitly instead of relying on a shared name.

To block the property version of Russell's paradox [SEP-Prop §2.4], predicables are stratified by order: order-1 predicables apply to particulars, order-(n+1) predicables apply to order-n predicables. The nodes under Predicable are unions across orders. Stratification is a design choice; type-free alternatives exist [SEP-Prop §6.1].

### 3.3 The ties

These are primitives of the framework. They are not, by default, instances of **Relation**: treating instantiation as one more relation that itself needs instantiating starts Bradley's regress [SEP-Prop §2.3]. They may be reified when needed, and are then classified like any other relation.

| Tie                                                                         | Holds between                                            | Gloss                              |
| --------------------------------------------------------------------------- | -------------------------------------------------------- | ---------------------------------- |
| `instanceOf`                                                              | entity, class                                            | exemplification proper             |
| `subclassOf` / `specializes`                                            | class, class / predicable, predicable                    | the only tree edge                 |
| `characterizedAs`                                                         | Characterized Object, class or predicable                | "encoded," not exemplified (§5.6) |
| `inheresIn`                                                               | Feature, bearer(s)                                       | specific dependence                |
| `participatesIn`                                                          | Object, Occurrence                                       |                                    |
| `occupies` / `occursAt`                                                 | Object or Occurrence, Region                             |                                    |
| `carriedBy`                                                               | Construct, carrier                                       | generic dependence                 |
| `expresses`                                                               | Symbolic Form, Content or Proposition                    |                                    |
| `about`                                                                   | Content, Proposition or Attitude, any entity             | aboutness; may fail                |
| `specifies`                                                               | Content (a specification), predicable or Occurrence-type |                                    |
| `conformsTo`                                                              | any entity, specification                                |                                    |
| `manifests`                                                               | Occurrence, Disposition                                  |                                    |
| `hasValue`                                                                | Quality, Magnitude (at a time)                           |                                    |
| `plays`                                                                   | entity, Role (in a context)                              |                                    |
| `partOf`, `memberOf`, `constitutedBy`, `dependsOn`, `derivedFrom` | various                                                  | never tree edges                   |

### 3.4 Five things all called "realization"

The word covers five different ties, none of which is is-a:

1. **Instantiation:** Secretariat is an instance of the kind horse.
2. **Conformance:** this bridge conforms to its design; the design `specifies` a kind of bridge.
3. **Manifestation:** this shattering manifests the vase's fragility.
4. **Expression:** the 1851 English text expresses the work *Moby-Dick*.
5. **Carrying:** this paper copy carries that text.

*Realization* and *carrier* are therefore roles that entities play, not classes.

---

## 4. The upper tree

Each node has exactly one navigation parent, shown by indentation, and that parent is always a true superclass. "▸" lists deeper categories that are indicated but not expanded.

```
Entity
├── Particular
│   ├── Object
│   │   ├── Physical Object         ▸ organism, artifact, celestial body, portion of matter, particle
│   │   ├── Social Object           ▸ organization, state, community
│   │   └── Agent                   ▸ person, corporate agent, artificial agent   (overlaps both siblings)
│   ├── Occurrence
│   │   ├── Process
│   │   ├── Event
│   │   └── State
│   ├── Feature
│   │   ├── Quality
│   │   ├── Disposition             ▸ tendency, liability, power
│   │   ├── Attitude                ▸ belief, desire, intention, preference
│   │   ├── Relator                 ▸ bond, commitment, obligation, right, role-holding
│   │   └── Topological Feature     ▸ boundary, surface, hole
│   ├── Region
│   │   ├── Spatial Region
│   │   ├── Temporal Region
│   │   └── Spatiotemporal Region
│   ├── Construct
│   │   ├── Content                 ▸ work, theory, specification, norm, plan, concept
│   │   ├── Symbolic Form           ▸ expression (text, score), symbol, sign system
│   │   └── Characterized Object    ▸ fictional, mythical, posited, impossible
│   └── Formal Object
│       ├── Number
│       ├── Set
│       ├── Function
│       ├── Mathematical Structure
│       ├── Magnitude
│       └── Proposition
└── Predicable
    ├── Property                    (arity 1)
    │   ├── Kind
    │   ├── Phase
    │   ├── Role
    │   └── Attribute
    └── Relation                    (arity ≥ 2)
        ├── Internal Relation
        └── External Relation
```

### Construct expansion for comparison

This is a comparison sketch supplied by the consolidating agent, not an adopted extension or an attribution of these subclass choices to Fable. It develops the original proposal's examples and the [revised Construct branch](CritiqueByClaudeFable.md#recommended-upper-tree). Every branch proposes is-a; overlap and completeness below Content remain unasserted.

```text
Construct
├── Content
│   ├── Work
│   │   └── Narrative work
│   ├── Specification
│   │   ├── Goal specification
│   │   ├── Plan specification
│   │   ├── Norm specification
│   │   ├── Design specification
│   │   ├── Standard specification
│   │   └── Condition specification
│   └── Descriptive content
│       ├── Theory content
│       ├── Model content
│       ├── Description content
│       └── Record content
├── Symbolic Form
│   ├── Expression
│   │   ├── Linguistic expression
│   │   ├── Formal-language expression
│   │   ├── Musical score expression
│   │   └── Diagrammatic expression
│   ├── Symbol
│   └── Sign system
│       ├── Notation system
│       └── Language system
└── Characterized Object
```

**Reading the sketch:** Work identifies an origin-anchored composition independently of its wording; Narrative work organizes presented situations or happenings. Specification prescribes or specifies a target, conduct, design, standard or assessable condition. Descriptive content presents an account of a subject, rather than prescribing it. A theory or record can also be a work; the branches are not an exclusive partition. Expression identifies a sign arrangement, Symbol an individual sign-form, and Sign system an organized repertoire with conventions. These denote carrier-independent constructs, not paper copies, inscriptions, utterance events or acts of recording. All proposed descendants inherit Construct's origin-sensitive identity; a purely origin-independent formal pattern belongs under Formal Object instead. Whether language systems and every proposed expression satisfy that origin criterion needs testing.

**Comparison with Astra:** this Content branch broadly covers Astra's Directive specification and Descriptive content. Condition specification supplies a possible home for authored unary or multi-argument specifications, corresponding to Astra's Predicate, renamed Condition specification in its revision. It does not relocate Fable's Property or Relation: a condition specification describes a predicable and is not thereby that predicable. Fable's Proposition remains under Formal Object; Astra places Propositional content under Content. Fable's Symbolic Form is a sibling of Content inside Construct; Astra's Symbolic structure is under Formal entity. Thus Astra's Content does not correspond to all of Construct.

**Identity test:** two independently originated works with the same wording can be distinct constructs in Fable's account. The origin-independent wording pattern can instead be one Formal Object. Astra's interpretation-based Content definition does not itself establish that same origin-sensitive distinction. Matching labels is insufficient to establish equivalent classes.

**Characterized Object:** leave this branch unexpanded. Fictional, mythical, posited and impossible are source/status descriptions here, not proposed primary subclasses for the consolidated tree. Fable's source-anchored Holmes construct must be distinguished from Holmes considered as a human under a story's attribution. Adopting this entire Construct branch would require resolving that distinction against the [accepted admission rule](Ontology.md#accepted-decision-admission-and-actuality); the sketch does not settle it.

---

## 5. Definitions

### 5.1 Level 1

| Node                 | Definition                                                                                                                                                                                                                         |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Particular** | An entity that cannot have instances. It may have parts, members, copies, carriers or manifestations, but nothing is*an* it.                                                                                                     |
| **Predicable** | An entity that can be predicated of entities and can have instances (or, for relations, ordered groups of instances). The definition is neutral on whether predicables are universals, resemblance classes of tropes, or concepts. |

### 5.2 Level 2 under Particular

| Node                    | Definition                                                                                                                                                                                                        |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Object**        | A particular that persists as one whole through time, can change while remaining itself, bears features and takes part in occurrences, and is not itself a feature or occurrence of something else.               |
| **Occurrence**    | A particular that happens or obtains over time, has temporal phases (or is the instantaneous boundary of something that does), and depends on what takes part in it.                                              |
| **Feature**       | A particular that exists only as a feature*of* one or more specific bearers and cannot move to another bearer.                                                                                                  |
| **Region**        | A particular that is a portion of space, time or spacetime, identified by its extent and position and not by what occupies it.                                                                                    |
| **Construct**     | A particular whose identity is anchored in an origin (an act or tradition of representing) together with what is represented, and which is tied to no single carrier: it can be copied, taught, lost and revived. |
| **Formal Object** | A particular whose identity is fixed entirely by a formal definition or structural condition; origin, location and carrier play no part in what it is.                                                            |

### 5.3 Level 3 under Particular

| Node                             | Definition                                                                                                                                                                                |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Physical Object**        | An object located in space and bearing physical qualities such as mass, charge or extension.                                                                                              |
| **Social Object**          | An object whose existence and unity consist in collective recognition or constitutive rules. It is constituted by members or a material basis without being identical to them.            |
| **Agent**                  | An object of a kind whose members bear attitudes and perform actions attributable to them.                                                                                                |
| **Process**                | An occurrence that is ongoing: it can continue, speed up, pause and resume, and any phase of it is an occurrence of the same sort.                                                        |
| **Event**                  | An occurrence that is bounded and countable, with a definite start and end or a culmination; once over, it is fixed.                                                                      |
| **State**                  | An occurrence that consists in something's being a certain way throughout an interval, with no change required.                                                                           |
| **Quality**                | A feature that is fully present whenever it exists and takes a value at each time (this apple's mass, this wall's colour).                                                                |
| **Disposition**            | A feature that is a readiness to behave in a certain way under certain conditions; it can exist unmanifested (this glass's fragility).                                                    |
| **Attitude**               | A feature of an agent that is directed at a content (her belief that it will rain, his intention to resign).                                                                              |
| **Relator**                | A feature borne jointly by two or more bearers and binding them (this marriage, that employment, this debt).                                                                              |
| **Topological Feature**    | A feature that is a boundary, surface or void of a host: it has location and shape but exists only as something of the host (the hole in this wall).                                      |
| **Spatial Region**         | A region with spatial extent only (the volume this room occupies; the territory inside a border).                                                                                         |
| **Temporal Region**        | A region with temporal extent only (the year 1851; noon today).                                                                                                                           |
| **Spatiotemporal Region**  | A region with both (the space-time swept out by a flight).                                                                                                                                |
| **Content**                | A construct at the level of what is meant, presented or prescribed, independent of wording or notation (the novel as a work; a theory; a building code as a set of requirements).         |
| **Symbolic Form**          | A construct at the level of signs: a symbol or arrangement of symbols in a language or notation, independent of any one inscription (the English text of a novel; a score; the letter A). |
| **Characterized Object**   | A construct that is what a source presents as an object. Its identity is fixed by the source and the properties ascribed there, whether or not anything satisfies them.                   |
| **Number**                 | A formal object that answers "how many" or "how much," identified by its place in a number system.                                                                                        |
| **Set**                    | A formal object identified solely by its members.                                                                                                                                         |
| **Function**               | A formal object that assigns exactly one output to each admissible input, identified by its domain, codomain and assignments.                                                             |
| **Mathematical Structure** | A formal object consisting of a domain with relations or operations on it, identified by that pattern (the natural numbers under successor; the Euclidean plane).                         |
| **Magnitude**              | A formal object that is a determinate amount, degree or position in a dimension of comparison (that much mass; that shade), identified independently of units and numerals.               |
| **Proposition**            | A formal object that is true or false as a whole: what a declarative sentence says and what can be believed or denied.                                                                    |

### 5.4 Under Predicable

| Node                        | Definition                                                                                                                                                                                              |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Property**          | A predicable that applies to one thing at a time (arity 1). This is the logician's broad sense; it includes kinds.                                                                                      |
| **Relation**          | A predicable that applies to two or more things taken in an order (arity ≥ 2, including variable arity).                                                                                               |
| **Kind**              | A property that says*what* its instances are, belongs to each instance for as long as it exists, and carries a criterion for counting and re-identifying them (horse, electron, prime number, novel). |
| **Phase**             | A property that classifies its instances by a stage they pass through owing to their own condition, and which they can leave while remaining themselves (larva, adolescent, molten).                    |
| **Role**              | A property that classifies its instances by the part they play relative to something else, and which they can leave while remaining themselves (student, employer, prey, catalyst, carrier).            |
| **Attribute**         | A property that says*how* its instances are, not what they are (red, having a mass of 5 kg, fragile, taller than Socrates).                                                                           |
| **Internal Relation** | A relation that holds whenever its relata exist with the intrinsic properties they have (taller than, greater than, resembles).                                                                         |
| **External Relation** | A relation that is not settled by the existence and intrinsic properties of its relata (is 3 m from, is married to, owns, causes).                                                                      |

### 5.5 Note on labels

*Feature* here is broader than DOLCE's "feature" (holes, bumps and the like); DOLCE's sense corresponds to my Topological Feature. *Property* here is the unary predicable; the narrower, adjective-like sense is Attribute. *Construct* is a label of convenience: a reader who holds that works are discovered, not made, can read it as "origin-anchored content" without changing any edge.

### 5.6 Characterized Objects and two modes of predication

A Characterized Object is related to properties in two ways:

- `characterizedAs`: the properties its source ascribes to it. Holmes is characterized as a detective, a man, a resident of Baker Street.
- `instanceOf`: what it is. Holmes is an instance of Characterized Object; he was created by Conan Doyle; he is famous.

This is the dual-copula strategy (Mally, Zalta: "encoding" versus "exemplifying"; van Inwagen: "ascribed" versus "has") [SEP-NE §5.5]. It answers both of Russell's objections: the round square is characterized as round and as square but is an instance of neither, and "the existent golden mountain" is characterized as existing without existing. The same data can be read three ways without changing a single assertion: as a nonexistent object (Meinongian), as an existing abstract artifact created by an author (the view the SEP calls creationism [SEP-NE §3.2]), or as a bookkeeping device over the source text (the reductionist views in [SEP-NE §5.1]). The ontology does not choose among them.

---

## 6. The splits: axis, status, justification, objection, boundary case

"Asserted" means I recommend the axiom. "By definition" means it follows from the definitions. "Not asserted" means overlap is expected or the question is open.

### S0. Entity → Particular | Predicable

- **Axis:** can it have instances?
- **Status:** disjoint and exhaustive by definition, given instantiation as a primitive.
- **Justification:** it is a logical criterion that does not depend on location, matter, or mind, so it does not presuppose materialism, Platonism, or an abstract/concrete dichotomy. It is the first cut in UFO and GFO [UFO; GFO] and the second level of Lowe's scheme [SEP-Cat §1.4]. It is also the distinction the instance/subclass discipline of §3.2 needs.
- **Strongest objection:** for some entities instantiability is decided by the theory one adopts, so the ontology must stipulate. A species may be a kind with members or a historical lineage with parts. A novel may be a type with tokens or a created particular with copies. A nominalist will say the Predicable branch is empty or should be relabelled as concepts or predicates. The definition's neutrality clause reduces but does not remove this.
- **Boundary cases:** the letter *A*; the Ford Model T; *Homo sapiens*; Beethoven's Fifth. My ruling: a copy *carries* a work and does not instantiate it, so works and symbol types are Particulars (Constructs); each also determines a derived Kind ("copy of *Moby-Dick*," "token of *A*"). Galton's proposal that processes are abstract patterns realised in states and events [Galton-2012] would move Process toward Predicable; I do not adopt it but record it.

### S1. Particular → Object | Occurrence | Feature | Region | Construct | Formal Object

- **Axis:** principle of individuation together with dependence profile. Applied as an ordered series of questions: Is its identity fixed by formal definition alone? (Formal Object.) If not, is it anchored in origin plus content and free of any one carrier? (Construct.) Is it itself a location? (Region.) Does it exist only as a feature of specific bearers? (Feature.) Does it unfold in time? (Occurrence.) Otherwise: Object.
- **Status:** pairwise disjoint, asserted. Exhaustive: **not asserted**.
- **Justification:** the four middle categories are the common ground of BFO, DOLCE and UFO: persisting things, happenings, dependent features and regions [BFO-sec; DOLCE; UFO]. Construct supplies what a two-way abstract/concrete split lacks: a category for things that are created at a time, can cease, and have no single location. BFO's generically dependent continuant and CIDOC CRM's Conceptual Object recognise the same need [BFO-GDC; CRM]; Thomasson's dependence-based categories are the philosophical source [SEP-Cat §1.5]. SUMO, by contrast, makes Physical and Abstract disjoint and jointly exhaustive [SUMO], which forces a novel or a corporation into one or the other.
- **Strongest objection:** the list is not derived from a single binary principle, so its completeness cannot be proved, which is the standing objection to Aristotle's list [SEP-Cat §1.5]. Candidates with no obvious place: facts or states of affairs, possible worlds, absences ("the lack of vitamin C"), spacetime as a whole.
- **Boundary cases:** a waterfall or a hurricane (Object or Process? see §9.5); the word-sequence of a novel considered apart from its author (Formal Object) versus the authored text (Construct); a hole (Feature, Region, or Object?); an organization versus its charter.

### S2. Object → Physical Object | Social Object | Agent

- **Axis:** two axes, which is why Agent overlaps. Physical/Social divide by what grounds the object's existence and unity; Agent is defined by a capacity.
- **Status:** Physical ⟂ Social, asserted. Agent overlaps both. Exhaustive: not asserted (an immaterial, non-social mind would be an Agent only).
- **Justification:** DOLCE likewise crosses physical/non-physical with agentive/non-agentive [DOLCE]. Keeping Agent out from under Physical Object is what prevents the tree from assuming materialism about persons.
- **Strongest objection:** a mixed-axis sibling group is exactly what a clean taxonomy avoids; Agent could be removed from the tree and kept only as an additional superclass. I keep it visible because otherwise persons have no navigation parent that is metaphysically neutral.
- **Boundary cases:** a banknote is a Physical Object playing a Role, not a Social Object. A human person: Agent, with the relation to the organism recorded as `constitutedBy` or identity, left open. A crowd: a physical aggregate, not a Social Object, since no rule or recognition unifies it.

### S3. Occurrence → Process | Event | State

- **Axis:** temporal profile (ongoing and homogeneous; bounded and countable; unchanging).
- **Status:** State disjoint from the other two, asserted. Process ⟂ Event asserted as a convention: the event is the bounded whole, the process the activity that makes it up. Exhaustive, asserted.
- **Justification:** the three-way distinction is standard in the linguistic and ontological literature on occurrents and is reflected in DOLCE's perdurant subclasses [DOLCE]. Users distinguish "erosion," "the 1980 eruption" and "being dormant."
- **Strongest objection:** BFO has no State category and locates what I call states in qualities and their bearers [BFO-sec]. And one happening can be described both ways ("she was running" / "her run"), which suggests one entity with two aspects, not two classes.
- **Boundary cases:** a life; the Gulf Stream; a fever (State of having a temperature above a threshold, distinct from the temperature Quality and from any underlying disease Disposition).

### S4. Feature → Quality | Disposition | Attitude | Relator | Topological Feature

- **Axis:** how the feature characterizes its bearer: manifestly; as a readiness; by being directed at a content; by binding several bearers; by bounding or piercing.
- **Status:** Quality ⟂ Disposition, asserted. Relator disjoint from the single-bearer classes by definition. Attitude versus Disposition: **not asserted** (dispositional accounts of belief would make Attitude a subclass). Exhaustive: not asserted.
- **Justification:** Quality/Disposition tracks BFO's quality versus realizable entity [BFO-sec]. Relator is UFO's category for the truth-makers of material relations [UFO]. Attitude is needed because goals, preferences and beliefs are features of agents with contents, and no other class captures the content link.
- **Strongest objection:** the Quality/Disposition divide is contested at the root. On the "powerful qualities" view every property is both qualitative and dispositional [SEP-Prop §5.2]. And trope sceptics reject the whole branch: on a universals-only view there are only objects and predicables [SEP-Prop §1.6].
- **Boundary cases:** a hole has its own size and can be filled, which is object-like, yet cannot exist without its host; BFO treats sites as immaterial independent continuants [BFO-sec] while DOLCE treats holes as dependent features [DOLCE]. Mass: quality or disposition to resist acceleration? A contract: the Relator (the bond), the Content (its terms), the Symbolic Form (its wording) and the paper are four entities.

### S5. Region → Spatial | Temporal | Spatiotemporal

- **Axis:** which dimensions the region extends in.
- **Status:** disjoint and exhaustive, asserted, for regions of physical space and time.
- **Justification:** matches the region categories of BFO [BFO-sec]. Places and times are among the first things users browse.
- **Strongest objection:** relationism denies that regions are entities over and above relations among things; relativity makes the space/time separation frame-dependent, so only the third class is fundamental.
- **Boundary cases:** a national border and a time zone are regions fixed by convention, so their *delimitation* is institutional although they are Regions. "San Jose" names a territory (Spatial Region), a built environment (Physical Object) and a municipality (Social Object): three entities. Colour space and vector spaces are Mathematical Structures, not Regions; DOLCE instead groups quality-space regions with spatial and temporal ones under a single abstract Region class [DOLCE].

### S6. Construct → Content | Symbolic Form | Characterized Object

- **Axis:** level in the chain of representation: what is meant; the signs that mean it; the object presented.
- **Status:** pairwise disjoint, asserted. Exhaustive: not asserted.
- **Justification:** the Content/Symbolic Form split is the library world's Work/Expression distinction [LRM] and CIDOC CRM's Propositional Object versus Symbolic Object [CRM]. Characterized Object is separate because a character is neither a meaning nor a string of signs.
- **Strongest objection:** a pure piece of instrumental music or an abstract design has a form but arguably no separate "content," so the two levels collapse. And a Meinongian will object that Holmes is a nonexistent *man*, not a construct of any kind.
- **Boundary cases:** a concept (Content, or a mental particular?); a natural language (Symbolic Form as a sign system, or a social practice?); a legal statute: the norm is Content, the enacted wording is Symbolic Form.

### S7. Formal Object → Number | Set | Function | Mathematical Structure | Magnitude | Proposition

- **Axis:** what kind of formal condition fixes identity: place in a number system; membership; input–output assignment; relational pattern; place in a dimension of comparison; truth conditions.
- **Status:** disjointness **not asserted** among Number, Set, Function and Structure, because set-theoretic foundations identify all four with sets while structuralist and category-theoretic foundations do not. Magnitude and Proposition disjoint from the rest, asserted. Exhaustive: not asserted (points, vectors, proofs, formal strings belong here too and are left to the mathematics domain).
- **Justification:** these are the formal sortals the upper level itself needs: numbers for counts, sets for extensions, functions for the arity discussion, structures for value spaces, magnitudes for measurement, propositions for contents of attitudes and assertions.
- **Strongest objection:** this is a list of convenient sortals, not a partition. An intuitionist will say mathematical objects are mental constructions and belong under Construct. An *in re* structuralist will say structures are patterns that systems instantiate and belong under Predicable. And magnitudes of physical quantities are arguably not "formal" at all.
- **Boundary cases:** "group" is a Kind whose instances are particular groups; the integers under addition are a Mathematical Structure. The number 2: natural, integer, rational and real "2" are one entity or four linked by embeddings (unresolved, §12). Singular propositions about Socrates: can they exist if he never did?

### S8. Predicable → Property | Relation

- **Axis:** arity only.
- **Status:** disjoint by definition once each predicable has a declared canonical arity. Exhaustive for arity ≥ 1. Arity 0 is the limiting case: a fully saturated predicable is a proposition [SEP-Prop §1.5], which I place under Formal Object because nothing remains for it to be predicated of.
- **Justification:** arity is the one criterion on which logic, databases and ontology languages agree, and it is checkable.
- **Strongest objection:** natural-language predicates are often multigrade ("lifted the table" takes one lifter or several), so a fixed arity is partly an artefact of regimentation [SEP-Prop §1.5].
- **Boundary cases:** "are compatriots" (binary, or a unary property of a plurality?); "surround"; "is between."

### S9. Property → Kind | Phase | Role | Attribute

- **Axes:** first, classifying ("what is it?") versus characterizing ("how is it?"); then, among classifiers, rigid versus anti-rigid; then, among anti-rigid classifiers, intrinsic versus relational condition.
- **Status:** pairwise disjoint, asserted. Exhaustive: **not asserted**. Semi-rigid, negative and disjunctive properties are left unplaced directly under Property.
- **Justification:** the classifying/characterizing contrast is Aristotle's said-of versus present-in and Lowe's kinds versus attributes [SEP-Cat §1.1, §1.4]; sortal versus non-sortal properties in [SEP-Prop §1.7]. The rigid/anti-rigid layer is OntoClean and UFO [OntoClean; UFO]. UFO's finding that these distinctions apply to types of qualities and relators as well as to types of substances [UFO] is why the split sits under Property generally and not under "object types."
- **Strongest objection:** the noun/adjective contrast may be grammar, not metaphysics: "is gold" and "is golden," "is a triangle" and "is triangular." And rigidity judgments are relative to a theory: nothing forbids an ontology in which *person* is anti-rigid [OntoClean].
- **Boundary cases:** *planet* under the 2006 IAU definition includes a condition about the body's orbital neighbourhood, so it is a classifier with a relational condition, closer to a Role than its grammar suggests. *Bachelor*; *weed*; *medication* (a chemical Kind or a Role that substances play?). UFO further separates classifiers that apply across kinds (role mixins such as *customer*) [UFO]; I fold these into Role and Phase at this level.

### S10. Relation → Internal | External

- **Axis:** whether the relation's holding is settled by the existence and intrinsic properties of the relata.
- **Status:** disjoint and exhaustive by definition.
- **Justification:** it is the long-standing metaphysical division of relations [SEP-Prop §1.5], and it does real work: an External Relation typically needs a truth-maker (a Relator, an Event, a spatial arrangement), which tells the modeller what else to record.
- **Strongest objection:** this is the least secure split in the tree. Definitions of "internal" differ among authors, classification is theory-laden (is causation internal? parthood?), and users browse relations by family (spatial, temporal, causal, social, logical), which is a domain facet. A defensible alternative is to leave Relation unexpanded at this level.
- **Boundary cases:** *is the same height as* is internal given heights, but heights are frame-relative magnitudes; *is a sibling of* holds in virtue of past events.

---

## 7. Property, Relation and the Predicable layer

### 7.1 Does a visible Predicable layer earn its cost?

**Costs.** One more level before a user reaches Property or Relation. A label that is unfamiliar. And a standing risk of confusing the predicable with the *predicate*, which is a linguistic expression: predicates express properties and are not themselves properties [SEP-Prop §1.1]. In this ontology predicates are Symbolic Forms.

**Benefits.** Properties and relations share everything that matters formally: both are instantiated, both have an arity, an extension and an intension, both admit logical operations (negation, conjunction, converse, composition), both have higher-order properties (rigid, symmetric, transitive), and both can be related by derivation. The layer is the one place to state:

- the arity of every predicable and the conventions for indices;
- derivations between arities (§7.3), which by definition cross the Property/Relation line;
- metaproperties such as rigidity and sortality;
- the order stratification of §3.2.

**Verdict.** Keep it, under the name **Predicable**, and reserve "predicate" for expressions. The layer earns its place in any ontology that reifies roles, taxa, units and attribute definitions, since those are predicables that must be classified and related. It would not earn its place in a system that never treats a property or relation as a subject of statements; in such a system both nodes could hang directly under Entity with no loss.

### 7.2 Two criteria that must not be merged

|            | **Arity criterion**                          | **Metaphysical criterion**                                            |
| ---------- | -------------------------------------------------- | --------------------------------------------------------------------------- |
| Question   | How many argument places does the predicable have? | Does having it depend on anything other than the bearer?                    |
| Values     | unary / n-ary                                      | intrinsic / extrinsic (for properties); internal / external (for relations) |
| Decided by | canonical logical form                             | what makes predications true                                                |

The two cross-classify. All four cells are occupied:

|                 | Intrinsic or internal                  | Extrinsic or external                                                                                 |
| --------------- | -------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Unary** | having a mass of 5 kg; being spherical | weighing 49 N (depends on the local field); being married; being an uncle; being a planet (IAU sense) |
| **n-ary** | taller than; greater than              | 3 m from; owes money to                                                                               |

So "Property versus Relation" (arity) is not "intrinsic versus relational" (metaphysics). *Being married* is a Property by arity and relational by nature. Placing it under Relation because it "is really relational" would be a silent change of arity; placing *married to* under Property because marital status "is an attribute" would be the same error in the other direction.

### 7.3 When a relation yields a unary condition

A unary predicable may be obtained from an n-ary relation *R* by exactly these operations. In every case *R* keeps its arity and its place under Relation; the result is a **new** predicable under Property, carrying a `derivedFrom` record naming *R*, the operation, and any fixed arguments.

| Operation                                          | Form                     | Example                             | Result is typically |
| -------------------------------------------------- | ------------------------ | ----------------------------------- | ------------------- |
| **Saturation**                               | λx. R(x, a)             | taller than Socrates                | Attribute           |
| **Value-fixing** (saturation by a Magnitude) | λx. mass(x) = 5 kg      | having a mass of 5 kg               | Attribute           |
| **Existential closure**                      | λx. ∃y R(x, y)         | is married; is a parent             | Attribute or Role   |
| **Universal closure**                        | λx. ∀y R(y, x)         | is loved by everyone                | Attribute           |
| **Reflexivization**                          | λx. R(x, x)             | is self-employed                    | Attribute           |
| **Sortal restriction plus closure**          | λx. K(x) ∧ ∃y R(x, y) | student = person enrolled somewhere | Role                |

These are the ordinary complex-predicate constructions (lambda abstraction, quantified and reflexive properties) described in [SEP-Prop §4.1, §6.1]. The record-keeping requirement is mine.

**Context and index rules.**

1. **Arity counts participant places only.** Time, possible world, reference frame and standard of comparison are *indices*. Each predicable declares which indices it takes. This is a stated convention; BFO, for example, makes time an explicit argument of instantiation for continuants.
2. **A hidden parameter is not a licence to drop a place.** "Tall" is canonically *tall for* (x, comparison class). The unary "tall" is admissible only with the comparison class bound and recorded. "Simultaneous" requires a frame. "Red" may require viewing conditions, depending on one's theory of colour.
3. **Functions and relations.** An n-place function corresponds to an (n+1)-place relation that is functional in its last place: *mother of* (x) and *is mother of* (y, x). Each entry declares which form it is. The mathematical Function (a Formal Object) and the functional Relation (a Predicable) are different entities linked by `represents`.
4. **Reification is not an arity change.** Replacing *married* (a, b) by "there is a Relator *m*, a marriage, binding a and b" introduces a particular; the relation *married to* is still binary and External.

**Demonstrable errors this rules out:** classifying *parent* as an intrinsic Attribute with no recorded closure over *parent of*; treating *weight* as intrinsic; giving *citizen* no link to *citizen of*; listing *north of Paris* as a "relation."

### 7.4 Kinds, kind specifications and unary properties

Five items are easily run together. Using *horse*:

| Item                                                                            | Category                                          | Note                          |
| ------------------------------------------------------------------------------- | ------------------------------------------------- | ----------------------------- |
| the word "horse"                                                                | Symbolic Form                                     | a predicate expression        |
| the concept HORSE                                                               | Content                                           | what speakers grasp           |
| the kind*horse*                                                               | Predicable › Property ›**Kind**           | what Secretariat instantiates |
| the class**Horse**                                                        | a node; its extension at a time is a**Set** | extension of the kind         |
| a specification of the kind (a diagnosis, a breed standard, a type designation) | Construct › Content (a**specification**)   | `specifies` the kind        |

How they relate:

- **A Kind is a unary predicable** by arity. It differs from an Attribute by the metaphysical criterion of §S9: it is rigid and carries identity criteria. So Kind ⊑ Property, and Kind ⟂ Attribute.
- **Every kind determines a unary membership condition,** "being a *K*." On this ontology that condition simply *is* the kind regarded as a property; I do not posit a second entity. Lowe would object that instantiating a kind and exemplifying an attribute are different ties [SEP-Prop §2.1]; if the project wants that, add a second tie, not a second entity.
- **The converse fails.** Not every unary property determines a kind: *red* gives no criterion for counting "red things."
- **A kind specification is not the kind.** It is a Content that states conditions for membership. A kind can have no specification (natural kinds before anyone studied them), or several competing ones (rival species definitions) that `specify` the same kind or turn out to specify different ones. A specification can be defective, revised or withdrawn; the kind cannot be "revised."
- **Specifications are not limited to kinds.** A plan specifies an Occurrence-type; a standard specifies an Attribute range; a unit definition specifies a Magnitude.
- **Specified versus conforming.** An item can instantiate a kind without conforming to a given specification of it (a horse that fails the breed standard), and can conform to a specification without the specified kind being instantiable (a consistent-looking design for a perpetual-motion machine).

---

## 8. Semantic ancestry versus navigation placement

**Rules.**

- **N1.** A navigation parent must be a semantic superclass. Navigation never introduces a non-is-a edge into the tree.
- **N2.** One navigation parent per node. Where a class has several superclasses, choose the one under which its identity criterion is supplied.
- **N3.** Other superclasses are listed as "also," and reasoning uses all of them.
- **N4.** Associations (topic, part, location, use, `characterizedAs`, `specifies`) are shown as see-also links or facets, never as tree edges. Thesaurus-style "broader/narrower" links are a legitimate browsing device but do not carry subclass entailments; SKOS deliberately leaves `broader` non-transitive and weaker than class subsumption [SKOS].
- **N5.** Subject domains are a parallel index over the tree (§8.2).

### 8.1 Where navigation and semantics come apart

| Class                     | Navigation parent | Also (semantic)                            | Deliberately**not** a superclass                                                                |
| ------------------------- | ----------------- | ------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| Agent                     | Object            | overlaps Physical Object and Social Object |                                                                                                       |
| Person (deeper)           | Agent             |                                            | Organism: linked by `constitutedBy` or identity, left open, so the tree does not assume materialism |
| Organization (deeper)     | Social Object     | Agent                                      | Set of members; Content (its charter)                                                                 |
| Expression, text (deeper) | Symbolic Form     |                                            | Work: linked by `expresses`                                                                         |
| Specification (deeper)    | Content           |                                            | the Kind it specifies: linked by `specifies`                                                        |
| Role-holding (deeper)     | Relator           |                                            | Role: a role-holding is a particular; a Role is a predicable it falls under                           |
| Characterized Object      | Construct         |                                            | whatever it is `characterizedAs` (Holmes is not under Person)                                       |
| Magnitude                 | Formal Object     |                                            | Attribute; Number                                                                                     |
| Proposition               | Formal Object     |                                            | Content: a Content may `express` or contain propositions                                            |
| Function                  | Formal Object     | (Set, under set-theoretic foundations)     | Relation                                                                                              |

### 8.2 Domain facet

The subject areas named in the brief cut across the categorial tree. None is a superclass of what it indexes: *Mathematics* is a discipline (a Content and a social practice) and is not an ancestor of Number.

| Domain        | Where its subject matter sits                                                                                                                                                 |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Physical      | Physical Object; physical Processes, Events, States; Qualities and Dispositions of physical objects; Regions; Magnitudes of physical dimensions; physical Kinds and Relations |
| Biological    | Organism and its parts (under Physical Object); biological Processes; traits (Features); taxa (Kinds); life stages (Phases); ecological Roles                                 |
| Mental        | Agent; Attitude; mental Events and States; Content; concepts                                                                                                                  |
| Social        | Social Object; Relator (commitments, obligations, rights); social Events; norms (Content); offices and statuses (Roles); fiat boundaries (Regions)                            |
| Informational | Content; Symbolic Form; carriers (Physical Objects and Occurrences playing the carrier Role)                                                                                  |
| Mathematical  | Number, Set, Function, Mathematical Structure; mathematical Kinds and Relations                                                                                               |
| Logical       | Proposition; logical Relations (entailment); formal languages (Symbolic Form); proofs                                                                                         |
| Fictional     | Characterized Object; the works (Content) that characterize them                                                                                                              |

---

## 9. Stress tests

### 9.1 Properties, particular features, and values

Take "this sack has a mass of 5 kg." Five entities are involved:

| Entity                    | Category                                             |
| ------------------------- | ---------------------------------------------------- |
| *having a mass of 5 kg* | Attribute (a predicable; shared by every 5 kg thing) |
| this sack's mass          | Quality (a particular; only this sack has it)        |
| 5 kg                      | Magnitude (one position in the mass dimension)       |
| 5                         | Number                                               |
| the kilogram              | a reference Magnitude fixed by a specification       |

Schema: Quality *q* `inheresIn` sack; *q* `instanceOf` Mass; *q* `hasValue` 5 kg at *t*. The Attribute is derived by value-fixing (§7.3).

**Counterexamples that keep them apart.**

- *Feature is not Property.* Two sacks of 5 kg share one Attribute and one Magnitude but have two Qualities: when one sack is half-emptied, its mass changes and the other's does not. Likewise a rose's colour can fade; the *same* Quality takes a new value, while the Attribute *red* does not fade.
- *Value is not Property.* "5 kg is more than 3 kg" compares Magnitudes with no bearer in view. "The temperature rose by 5 K" names a difference that no object "has" as an attribute.
- *Value is not Number.* 5 kg = 5000 g: one Magnitude, two numerals, two Numbers.
- *Value is a role, not a kind.* The Number 3 is the value of "number of sides" for a triangle and is also a subject in "3 is prime." For a nominal attribute such as marital status the "value" *married* is itself an Attribute. Whatever fills the value place of an attribution plays the value role. A tree node "Value" would be anti-rigid and could not sit above Number or Magnitude. That is a demonstrable error under the rigidity rule, not a preference.

**Design choice flagged.** Treating Magnitudes as particulars follows DOLCE's qualia in quality spaces [DOLCE]. The alternative, on which 5 kg just *is* the determinate universal, is the monadic-property view of quantities [SEP-Prop §5.1]. The Quality layer is optional: a project sceptical of tropes can write *mass* (x, 5 kg, t) directly and lose only the ability to talk about a feature persisting through a change of value.

### 9.2 Dispositions and capabilities

A **Disposition** is a feature that can be manifested under triggering conditions. A **capability**, on the most developed recent account, is a disposition in whose realization some organism or group has an interest, intermediate between a mere disposition and a function; on that account every function is a capability [Capabilities; IOF].

**Counterexamples.**

- *Disposition that is no capability:* iron's disposition to rust; a vase's fragility. Nobody speaks of the vase's "capability to break."
- *Capability that is no function:* a stone's suitability for cracking nuts. The cited account explicitly sets such "task-based" cases aside [IOF], which shows they are a pressure point.
- *Function without capability:* a seized water pump still has the function of pumping and has no present ability to do so. If functions are capabilities and capabilities are dispositions, the broken pump must still bear the disposition. Either dispositions survive the loss of their physical basis, or function is not a kind of disposition.
- *Interest-relativity:* if what makes a disposition a capability is that someone has an interest in it, then a disposition can become or cease to be a capability with no change in its bearer.

**Ruling (mine).** *Capability* is a **Role** that Dispositions play relative to an interested party and a standard of success. It is not a rigid subclass of Disposition. *Function* is a normative assignment: a Relator, or an External Relation, linking a bearer to an Occurrence-type via a design specification or a selection history, typically but not necessarily backed by a Disposition. *Ability* and *skill* are Dispositions of Agents. The alternative, in which Capability and Function are subclasses of Disposition as in [Capabilities], is a reasonable design choice provided the broken-pump case is answered.

### 9.3 Purposes, goals, preferences, norms and obligations

| Notion                                         | Analysis                                                                       | Category                                                      |
| ---------------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------- |
| goal, as what is aimed at                      | a specification of a state of affairs to bring about                           | Content (or Proposition)                                      |
| having a goal                                  | an agent's intention or desire directed at that content                        | Attitude                                                      |
| purpose of an artifact or act                  | *for* (x, end, by whom or by what history): ternary                          | External Relation; "has the purpose of cutting" by saturation |
| preference                                     | an attitude whose content is a comparison of two contents                      | Attitude                                                      |
| preference ordering                            | a representation of someone's preferences                                      | Mathematical Structure                                        |
| norm                                           | prescriptive content valid within some system or community                     | Content                                                       |
| obligation (particular)                        | a bond between obligor and obligee, grounded in a norm plus a triggering event | Relator                                                       |
| type of obligation ("the duty to repay debts") |                                                                                | Kind of Relators                                              |

**Counterexamples.**

- *Goal content is not goal attitude:* two people share one goal; one abandons it. One Content, two Attitudes, one of which has ended.
- *Purpose is not a quality of the thing:* a manufactured paperweight and a physically indistinguishable found pebble differ in purpose and in nothing intrinsic.
- *Preference is not an ordering:* a person can prefer A to B, B to C and C to A. The three Attitudes exist; no ordering represents them.
- *Norm without obligation:* a speed limit on a road nobody drives binds no one at present.
- *Obligation without its norm:* a debt incurred under a statute can survive the statute's repeal.
- *Norm is not its wording:* one norm, two translations.

### 9.4 Kinds and contextual roles

**Test.** Could an instance cease to fall under the classifier and still be the same thing? If yes, it is a Phase or a Role and cannot be a tree node above a Kind.

**Counterexamples to common placements.**

- *Dog under Pet:* false for strays and wolves' cousins on farms; *pet* is a Role. Same for wheat under *food*, hammer-shaped rock under *tool*, dandelion under *weed*.
- *Person under Student:* Student is anti-rigid; Person is rigid; the edge is ruled out by [OntoClean].
- *Caterpillar and Butterfly as sibling Kinds:* one organism passes through both; they are Phases of a lepidopteran.
- *Vacant office:* the presidency exists while no one holds it. So the office (a Role, instituted by rules), the holder (an Agent) and the holding (a Relator with a start and end date) are three entities. An ontology with only "roles as classes of their players" cannot represent a vacancy.
- *Two roles, one player, different properties:* the same person as chair can call a vote and as member cannot. The powers attach to the role-holdings.
- *Roles also apply outside substances:* an Event can play the role of *cause*, a Proposition the role of *premise*, a Magnitude the role of *threshold*. This is why Role sits under Property generally [UFO].

**Hard cases.** *Planet* (see S9). *Medication*. *Evidence*. *Capital city*. A legal *person* (a Role that agents and organizations play, or a Kind?).

### 9.5 Objects, processes, states, regions and dependent features

- **Waterfall, flame, hurricane.** Each has a name, a location, a size and a history, and can move, which is object-like; each consists of nothing but ongoing activity, with complete turnover of matter. Galton and Mizoguchi argue that objects and processes depend on each other and that an object can be seen as the interface between the processes inside it and those it enacts [Galton-Mizoguchi]. **Ruling:** two entities, the Physical Object (the waterfall, which does not fall) and the Process (the falling of the water), linked by `constitutedBy`. A project that finds this double-counting can adopt a single class with an aspect attribute; that is a design choice.
- **Organism and life.** The organism is an Object; its life is a Process; its being alive is a State. "Lasted 80 years" is true of the life, "weighed 70 kg" of the organism.
- **State versus Quality.** The water's temperature (a Quality) persists while its value changes; the water's *being at 20 °C from noon to one* (a State) has those temporal bounds essentially.
- **Hole in a wall.** It has a diameter and a location, can be enlarged, can be filled; it cannot exist without the wall and moves when the wall moves. Not a Region (regions do not move with objects). Not an independent Object. **Ruling:** Topological Feature. BFO would call it a site, an immaterial independent continuant [BFO-sec]: a reasonable alternative.
- **Shadow.** An absence of light on a surface, dependent on an object, a source and a surface: I would treat it as a State of the surface, not a Feature of the caster. Uncertain.
- **Region versus object.** The Sahara is a Physical Object (sand, rock) occupying a Spatial Region. The equator is a Region fixed by convention.

### 9.6 Texts, carriers and content

For *Moby-Dick*:

| Entity                            | Category                                              | Library term [LRM] |
| --------------------------------- | ----------------------------------------------------- | ------------------ |
| the novel as a creation           | Content (a work)                                      | Work               |
| the 1851 English text             | Symbolic Form (an expression)                         | Expression         |
| a German translation              | another Symbolic Form expressing the same work        | Expression         |
| a particular edition              | a Kind of copies, with a specification (layout, ISBN) | Manifestation      |
| my paperback                      | Physical Object, playing the carrier Role             | Item               |
| the pattern of ink on its pages   | Quality of the paperback                              |                    |
| a reading aloud                   | Event, playing the carrier Role                       |                    |
| what the novel says about whaling | Propositions                                          |                    |

BFO describes the same structure: the ink arrangement on a volume concretizes the novel, which is generically dependent [BFO-GDC]. CIDOC CRM makes the related point that creating a conceptual object is conceiving its content, not producing its first carrier [CRM].

**Counterexamples.**

- *Text is not carrier:* burning my copy does not destroy the text.
- *Work is not text:* the translation is the same work in different words.
- *Text is not work:* in Borges's story, Menard composes word for word a passage of *Don Quixote*; if origin matters to the identity of a work, that is one word-sequence and two works. The bare word-sequence, with origin stripped away, is a Formal Object.
- *Carrier is a role:* a wall becomes a carrier when written on and ceases to be one when painted over.
- *Loss:* a poem of which no copy or memory survives. Being generically dependent, it no longer exists; we still refer to it. Status: *existed; no longer extant.* That is what the ontic-status attribute is for.
- *Manifestation is a Kind, not a particular:* there can be an edition of which no copy survives, and a planned edition of which none was printed.

### 9.7 Organizations and institutional entities

**Counterexamples to identifying an organization with anything simpler.**

- *Not its members:* a company survives complete turnover of staff; a committee and a club can have exactly the same members and different powers and histories.
- *Can have no members:* a dormant shell company.
- *Not its buildings:* Ryle's visitor who has seen the colleges and libraries and asks where the university is commits a category mistake [SEP-Cat §2.1].
- *Not its charter:* the charter can be amended; the organization can violate it.
- *Not a fiction in the Holmes sense:* it owns property and is sued.

**Ruling.** An organization is a **Social Object** and an **Agent**, constituted by members, grounded in collective recognition under rules.

**"Institutional entity" is not one class.** What people call institutional is distributed across the tree by form:

| Example                              | Category                            |
| ------------------------------------ | ----------------------------------- |
| a company, a state                   | Social Object                       |
| a constitution, the rules of chess   | Content (norms)                     |
| the presidency, legal tender         | Role                                |
| a specific debt, a specific marriage | Relator                             |
| an election, a wedding               | Event                               |
| a national border, a parcel of land  | Region delimited by convention      |
| the euro as a unit of account        | a reference Magnitude fixed by rule |

A single node "Institutional Entity" above these would have to be a superclass of objects, features, events, regions and predicables at once. *Institutional* is best treated as a dependence facet ("exists in virtue of collective acceptance"), alongside the domain facet.

### 9.8 Numbers and mathematical structures

- **A number is not a set.** The natural numbers can be modelled by more than one family of sets; on one construction 1 is a member of 3 and on another it is not. No fact settles which sets "are" the numbers, so I do not assert Number ⊑ Set, and I do not assert disjointness either. Set-theoretic models are linked by `represents`.
- **A number is not a numeral.** "2," "II" and "two" are Symbolic Forms.
- **A number is not a magnitude.** 2 is not 2 kg. It is also not "second": ordinals and cardinals coincide for finite cases and diverge for infinite ones.
- **Kind versus structure.** "Group" is a Kind. The integers under addition are a Mathematical Structure and an instance of that Kind. "The natural-number structure" is either one particular structure or a Kind instantiated by every system satisfying the axioms. I take the first as the entry and the second as its derived Kind.
- **Existence.** The entry for 7 carries the status *exists atemporally according to arithmetic*. A fictionalist reads that as "according to the story of arithmetic"; a Platonist reads it flatly. No edge changes.
- **Abstract/concrete.** Gets no purchase as a dividing line: Formal Objects, Constructs and Predicables are all "abstract" on some definitions and differ from one another in every respect the tree cares about.

### 9.9 Fictional and impossible referents

- **Holmes is not an instance of Person.** If he were, the class Person would have a member with no birth date, no mass and no body, and "every person has a mother who exists" would be false. He is `characterizedAs` a person.
- **Two kinds of truth about Holmes.** "Holmes is a detective" is true by characterization. "Holmes is more famous than any real detective" and "Holmes was created in the 1880s" are true by exemplification. A story operator ("according to the stories…") handles the first kind and fails for the second [SEP-NE §3.2].
- **Incompleteness.** The stories do not say whether Holmes has a mole on his left shoulder. He is characterized neither as having one nor as lacking one. No real person is indeterminate in that way, which is a further reason he is not under Person.
- **Impossible objects.** The round square is a Characterized Object, anchored in the philosophical literature, characterized as round and as square, status *impossible*. Its entry is consistent.
- **Failed posits are not fictions.** Vulcan was hypothesised to explain Mercury's orbit; nobody made it up as a story, and the SEP distinguishes it from fictitious objects on exactly this ground [SEP-NE §3.2]. It is a Characterized Object of the *posited, refuted* sort.
- **Open posits.** Planet Nine is `characterizedAs` a planet, status *posited, open*. If a planet is found, the cleanest record is a new entry for the planet, with the posit marked `satisfiedBy` it. Whether to merge the entries is editorial policy (§12).
- **Real things in fiction.** London in the Holmes stories is London; the stories' description of it is Content. No second entity is needed unless a source departs so far that it is treated as a distinct creation.
- **Characters across works.** Is the Holmes of a modern adaptation the same Characterized Object under a new characterization, or a new one `basedOn` the first? The definition (identity fixed by source and ascribed properties) favours the second; ordinary speech favours the first. Unresolved.
- **A Meinongian objection I cannot dissolve.** Someone who fears a ghost does not fear a construct [SEP-NE §5.6]. The tree records what the fear is `about` (the Characterized Object) and what the fearer takes it to be (`characterizedAs` a ghost); it does not explain the psychology.

---

## 10. Alternatives compared

### 10.1 First cut

| Option                                                      | Exemplified by                                                           | Strength                                                 | Why not chosen                                                                                                     |
| ----------------------------------------------------------- | ------------------------------------------------------------------------ | -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Abstract / Concrete                                         | SUMO's Physical/Abstract [SUMO]; Hoffman and Rosenkrantz [SEP-Cat §1.4] | Familiar                                                 | No agreed criterion; works, institutions and characters fit neither side; the brief forbids assuming it exhaustive |
| Continuant / Occurrent                                      | BFO [BFO-sec]                                                            | Sharp, well axiomatised                                  | Says nothing about predicables, formal objects or fiction; BFO is realist by design                                |
| Four-way flat list (endurant, perdurant, quality, abstract) | DOLCE [DOLCE]                                                            | Close to common sense                                    | "Abstract" is a remainder class; DOLCE is an ontology of particulars and leaves predicables outside                |
| Contingent / Necessary                                      | Chisholm [SEP-Cat §1.4]                                                 | Clean modal criterion                                    | Whether numbers or propositions exist necessarily is the disputed question                                         |
| Individual / Type (chosen, as Particular / Predicable)      | UFO, GFO, Lowe's second level [UFO; GFO; SEP-Cat §1.4]                  | Logical criterion; supports instance/subclass discipline | Abstract for browsing; theory-relative for works and species                                                       |
| Individual / Collection crossed with other partitions       | Cyc (from background knowledge, not re-checked)                          | Explicit multi-partition                                 | Many overlapping top-level partitions are hard to browse                                                           |
| No single tree; category differences only                   | Ryle, the sceptical tradition [SEP-Cat §1.5, §2]                       | Honest about pluralism                                   | Does not meet the requirement for a browsable root                                                                 |

Thomasson's observation applies to all of these: exclusive-and-exhaustive splits can be generated at will from any yes/no question, so meeting those two conditions does not single out a system [SEP-Cat §1.5]. The choice has to be argued from what the system is for. Mine is argued from three needs: keeping instance-of apart from subclass-of, avoiding a silent metaphysics of the abstract, and supporting later domain growth.

### 10.2 Other choices

| Decision               | Chosen                                        | Main alternative                                                                                        | Trade-off                                                                         |
| ---------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Predicable layer       | visible                                       | Property and Relation directly under Entity                                                             | one level saved; arity derivations and metaproperties lose their common home      |
| Kind placement         | under Property                                | Kind as a sibling of Property and Relation (Lowe-style)                                                 | keeps "instantiates" and "exemplifies" apart; mixes two axes in one sibling group |
| Works and institutions | Construct                                     | "abstract" remainder; or BFO's generically dependent continuant under Continuant                        | BFO's placement ties them to a realist continuant framework                       |
| Fiction                | Characterized Object with dual predication    | a "fictional X" shadow class beside each real class; or membership in the real class with a status flag | shadow classes double the tree; status flags break existential inferences         |
| Values                 | Magnitude as Formal Object; "value" as a role | determinate universals; or DOLCE's abstract Region                                                      | see §9.1                                                                         |
| Organizations          | Social Object                                 | aggregate of persons (a Physical Object)                                                                | fails the turnover and same-members cases                                         |
| States                 | under Occurrence                              | no State class                                                                                          | BFO-compatible; loses the State/Quality contrast                                  |
| Trope layer (Feature)  | included                                      | objects and predicables only                                                                            | simpler; cannot say "the same colour faded"                                       |

---

## 11. Demonstrable category errors versus reasonable design choices

### 11.1 Demonstrable errors

Each follows from the stated edge semantics (subclass inclusion, rigidity) and does not depend on my preferences.

1. **Instance as subclass:** Earth under Planet by a subclass edge; or a kind under Kind by a subclass edge while it also has first-order instances.
2. **Part as subclass:** Wheel under Car; Paris under France.
3. **Anti-rigid above rigid:** Person under Student; Dog under Pet; Number under Value; Paperback under Carrier.
4. **Carrier, form and content merged:** one node for a novel that has both a weight and an author's intention.
5. **Discipline above its subject matter:** Number under Mathematics; Organism under Biology.
6. **Characterized item under the real class it is characterized as:** Holmes as an instance of Person; "fictional horse" as a subclass of Horse.
7. **Existence as a class:** a node "Nonexistent Thing," whose membership changes whenever something is discovered or destroyed.
8. **Predicate for predicable:** treating the word "red" (which has three letters) as the property (which does not).
9. **Silent arity change:** filing *married* and *married to* as one entry, or filing a derived unary condition with no record of its base relation.
10. **Arity mistaken for intrinsicness:** inferring from unary form that *weight* or *being a planet* is intrinsic.
11. **Disjointness or exhaustiveness read off the layout.**
12. **Role and role-holding merged:** no way to represent a vacant office or the start date of a tenure.

### 11.2 Reasonable design choices

A competent designer could decide each of these differently.

1. Instantiability as the first cut.
2. Six particular categories, and exactly those six.
3. Including a trope layer (Feature) at all.
4. Keeping State as a kind of Occurrence.
5. Counting a waterfall as both an Object and a Process.
6. Organizations as Social Objects, not aggregates.
7. Works as Particulars with derived Kinds, not as Kinds with instances.
8. Magnitudes as particulars; Proposition under Formal Object and not under Content.
9. Capability as a Role of dispositions; Function as a normative assignment.
10. Stratifying predicables by order.
11. Kind under Property.
12. Internal/External as the only displayed split of Relation.
13. Agent as a visible overlapping sibling.
14. The two-domain treatment of existence.

---

## 12. Unresolved decisions

1. **Completeness of the six particular categories.** Facts and states of affairs, possible worlds, absences and spacetime as a whole are unplaced.
2. **Species and other taxa:** Kinds, or historical individuals (lineages)? This changes whether an organism is an instance or a part.
3. **Attitude versus Disposition:** subclass, overlap, or disjoint?
4. **Proposition:** Formal Object (as here), or Content; and whether singular propositions depend on their subjects.
5. **Magnitude:** particular or determinate universal; and whether physical magnitudes are "formal."
6. **Number identity across systems:** is the natural number 2 the real number 2?
7. **Structures:** particulars, or universals instantiated by systems?
8. **Relation subdivision:** Internal/External, or leave Relation unexpanded and index by family?
9. **Agent rigidity:** is an organism in an irreversible coma still an Agent? The definition is by kind-level capacity; that may be too generous.
10. **Characterized Object identity:** one character across works, or one per source? Merge or link when an open posit is confirmed?
11. **Orders of predicables:** stratified (as here) or type-free with restricted comprehension?
12. **Plural subjects:** are "the Beatles" one Social Object or four things referred to at once? Related to multigrade relations.
13. **Time as index or argument:** the convention in §7.3 keeps time out of arity; a project aligned with BFO may want it in.
14. **Whether Phase and Role should be grouped** under a single "contingent classifier" node, adding a level.
15. **Languages and concepts:** Constructs, practices (Processes or Social Objects), or mental particulars?

---

## 13. Sources

### 13.1 Consulted in this session

For each: what I took from it. "Secondary" means I read a description of the source, not the source itself.

- **[SEP-Cat]** Amie Thomasson, "Categories," *Stanford Encyclopedia of Philosophy*, substantive revision 22 Nov 2022. https://plato.stanford.edu/entries/categories/ — Aristotle's argument that being is not a genus; Husserl's formal/material distinction; Ingarden's existential categories; the systems of Chisholm, Grossmann, Hoffman and Rosenkrantz, and Lowe; the weakness of exclusivity and exhaustiveness as criteria; Thomasson's dependence-based categories; Ryle's university example; Dummett on "entity" and "object" as non-sortal.
- **[SEP-NE]** Maria Reicher, "Nonexistent Objects," *SEP*, substantive revision 7 Dec 2022. https://plato.stanford.edu/entries/nonexistent-objects/ — the "there is"/"exists" distinction and its regimentation with an existence predicate; Russell's objections; the nuclear/extranuclear, dual-copula and other-worlds strategies; creationism about fictional characters; internal versus external sentences about fiction; the Vulcan/fiction distinction.
- **[SEP-Prop]** "Properties," *SEP*, substantive revision 24 Nov 2025 (author metadata: Michele Paolini Paoletti). https://plato.stanford.edu/entries/properties/ — properties as predicables; predicates as linguistic; arity, multigrade predicates, propositions as the zero-place case; internal and external relations; universals versus tropes; sortals and determinables; Bradley's regress; self-exemplification and type theory; logically compound properties and lambda abstraction; dispositional versus categorical properties and "powerful qualities"; relational versus monadic theories of quantity; Lowe's distinct ties.
- **[BFO-sec]** BFO 2020 class definitions as tabulated in Beverley et al., "Capabilities: An Ontology," arXiv:2405.00183 (https://arxiv.org/pdf/2405.00183), and as described in "The Common Core Ontologies," arXiv:2404.17758 (https://arxiv.org/pdf/2404.17758). Secondary. — continuant/occurrent; independent, specifically dependent and generically dependent continuants; quality versus realizable entity; role, disposition, function; site and immaterial entity.
- **[BFO-GDC]** "Dispositions and Roles of Generically Dependent Entities," arXiv:2506.17085. https://arxiv.org/html/2506.17085v2 — the *Moby-Dick* concretization example; BFO's status as an ISO/IEC standard; functions as dispositions in BFO 2020.
- **[DOLCE]** Borgo et al., "DOLCE: A Descriptive Ontology for Linguistic and Cognitive Engineering," *Applied Ontology* 17 (2022), preprint arXiv:2308.01597 (https://arxiv.org/pdf/2308.01597); and Gangemi et al., "Sweetening Ontologies with DOLCE" (https://www.loa.istc.cnr.it/old/Papers/DOLCE-EKAW.pdf). Read in excerpt. — four basic categories; qualities inhering in bearers; quality spaces based on Gärdenfors; DOLCE as an ontology of particulars; roles and functions not formalised in the core.
- **[UFO]** Guizzardi et al., "Endurant Types in Ontology-Driven Conceptual Modeling: Towards OntoUML 2.0" (ER 2018) and Guizzardi and Fonseca et al., "Types and taxonomic structures in conceptual modeling" (*Data & Knowledge Engineering* 134, 2021), abstracts (https://philarchive.org/rec/GUITAT-3); gUFO documentation (http://purl.org/nemo/doc/gufo, read via an archive mirror). — kind, role, phase and mixin applying to endurant types generally, including relator, quality and mode types; rigid types cannot specialise anti-rigid ones; examples of kinds, phases, roles and role mixins.
- **[OntoClean]** Guarino and Welty, "An Overview of OntoClean" (https://www.loa.istc.cnr.it/wp-content/uploads/2020/03/OverviewOntoClean-compresso.pdf), read in excerpt, with the Wikipedia summary "OntoClean" for the list of metaproperties. — rigidity, identity, unity, dependence; sortals carry identity criteria; anti-rigid properties cannot subsume rigid ones; rigidity assignments are relative to the ontology.
- **[SUMO]** Niles and Pease, "Towards a Standard Upper Ontology," FOIS 2001 (https://www.ontologyportal.org/professional/FOIS.pdf), and Ševčenko, "Online Presentation of an Upper Ontology" (https://www.ontologyportal.org/pubs/Sevcenko.pdf). Read in excerpt. — Entity divided into Physical and Abstract, stated to be disjoint; Abstract's children including Quantity, Attribute and SetOrClass.
- **[GFO]** Loebe, Burek and Herre, "GFO: The General Formal Ontology," *Applied Ontology* 17 (2022), abstract (https://content.iospress.com/articles/applied-ontology/ao220264); project description (https://github.com/Onto-Med/GFO). — categories versus individuals as the backbone; universals, concepts and symbol structures as kinds of category; integration of objects and processes.
- **[LRM]** IFLA Library Reference Model (2017), via Žumer and Riva, "IFLA LRM – Finally Here" (https://dcpapers.dublincore.org/pubs/article/view/3852/0) and the Dublin Core summary (https://msi.dublincore.org/standards/ifla-lrm). Secondary. — Work, Expression, Manifestation, Item; Res as the top entity.
- **[CRM]** CIDOC Conceptual Reference Model, class pages for E28 Conceptual Object, E89 Propositional Object, E90 Symbolic Object, E55 Type. https://cidoc-crm.org/taxonomy/term/51 and https://cidoc-crm.org/node/416 — the Conceptual Object class and its subclasses; creation as conceiving content, not making the first carrier.
- **[SKOS]** Baker et al., "Key Choices in the Design of SKOS," arXiv:1302.1224 (https://arxiv.org/pdf/1302.1224); W3C SKOS semantics notes (https://www.w3.org/2006/07/SWD/wiki/SkosDesign/RdfsSemanticExtension.html). — `skos:broader` is not transitive and was not designed to support class-subsumption entailments.
- **[OWL-Pun]** W3C, "OWL 2 Web Ontology Language: New Features and Rationale" (https://www.w3.org/TR/owl2-new-features/), read as a contents listing only; and a CEUR paper on metamodelling semantics (https://www.ceur-ws.org/Vol-1350/paper-55.pdf), read in excerpt. — one name may be used for a class and an individual; under the direct semantics these are different elements.
- **[MLT-Wikidata]** Brasileiro, Almeida, Carvalho and Guizzardi, "Applying a Multi-Level Modeling Theory to Assess Taxonomic Hierarchies in Wikidata," WWW 2016 Companion. https://archives.iw3c2.org/www2016/WWW2016-Proceedings/companion/p975.pdf — problematic uses of instance-of and subclass-of.
- **[Wikidata-Disarray]** "Type or Individual? Evidence of Large-Scale Conceptual Disarray in Wikidata" (NEMO research group, 2021). https://nemo.inf.ufes.br/wp-content/papercite-data/pdf/type_or_individual_evidence_of_large_scale_conceptual_disarray_in_wikidata_2021.pdf — the anti-pattern of an item being both instance and subclass of the same item. Read in excerpt; I did not confirm the author list.
- **[Capabilities]** Beverley, Limbaugh, Merrell, Koch and Smith, "Capabilities: An Ontology," JOWO 2024, arXiv:2405.00183. https://arxiv.org/abs/2405.00183 — capability as intermediate between disposition and function; all functions are capabilities.
- **[IOF]** Industrial Ontologies Foundry Core, "capability." https://spec.industrialontologies.org/portal/release/202601/core/Capability.html — the definition in terms of an agent's interest; the exclusion of "task-based" capabilities.
- **[Galton-Mizoguchi]** Galton and Mizoguchi, "The Water Falls but the Waterfall does not Fall," *Applied Ontology* 4 (2009), abstract. https://empslocal.ex.ac.uk/people/staff/apgalton/abstracts/AO-waterfall.html
- **[Galton-2012]** Galton, "The Ontology of States, Processes, and Events" (2012), abstract. https://empslocal.ex.ac.uk/people/staff/apgalton/abstracts/InterOntology12.html

### 13.2 Relied on from prior knowledge, not re-opened in this session

These inform the argument but were not checked today; treat specific attributions as needing verification before they are quoted elsewhere.

- The standard number ISO/IEC 21838-2 for BFO 2020.
- Quine, "On What There Is" (1948). Zalta, *Abstract Objects* (1983). Parsons, *Nonexistent Objects* (1980). Priest, *Towards Non-Being* (2005). Thomasson, *Fiction and Metaphysics* (1999). (All are described in [SEP-NE] or [SEP-Cat]; I used those descriptions.)
- Lowe, *The Four-Category Ontology* (2006), via [SEP-Cat] and [SEP-Prop].
- Benacerraf, "What Numbers Could Not Be" (1965): the source of the two-reductions argument in §9.8.
- Searle, *The Construction of Social Reality* (1995): collective acceptance and constitutive rules in §S2 and §9.7.
- Vendler (1957) and Mourelatos (1978) on states, processes and events.
- Lewis on intrinsic and extrinsic properties, via [SEP-Prop §3.2].
- Gärdenfors, *Conceptual Spaces* (2000), via [DOLCE].
- Casati and Varzi, *Holes and Other Superficialities* (1994).
- Borges, "Pierre Menard, Author of the Quixote."
- The International Astronomical Union's 2006 definition of *planet* (the orbital-neighbourhood condition).
- Cyc's Individual/Collection distinction.
- BFO's time-indexed instantiation for continuants (mentioned in §7.3).
- Hohfeld on correlative rights and duties.

---

*End of independent proposal. I will wait for the project packet before comparing this with any existing design.*
