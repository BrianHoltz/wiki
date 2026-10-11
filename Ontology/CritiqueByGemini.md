# CritiqueByGemini.md

**Repository:** `BrianHoltz/wiki` (`Thoughts/wiki/Ontology/`)  
**Commit Revision Inspected:** `7ad197d`  
**Model & Evaluation Setting:** Gemini Spark (Phase 2 Informed Repository Critique)  
**Date:** October 11, 2026  

---

## 1. Inventory, Epistemic Status, and Methodological Limits

### 1.1 Material Inspected
This critique supersedes the blind, ungrounded draft of `CritiqueByGemini.md`. The following repository artifacts, source files, and competing proposals were directly inspected:
1. **Repository Design Foundations:**
   - `OntologyDesignMemoranda.md`: Primary design memoranda, evolution beyond 20-Questions, distinction between rich multidimensional ontology and canonical navigation tree projection, criteria for canonical trees, and stress-test requirements.
   - `CriticPrompt.md`: The two-phase evaluation framework and structural critique protocol.
   - `WordsToCategorize.md`: Unclassified lexical reservoir and candidate terms.
2. **The Incumbent Omniversal Ontology:**
   - `Ontology.md`: Handcrafted v1/v1010 markdown canonical tree, principles, biological prior-art analysis, and upper ontology excerpts.
   - `ontology.json`: Active JSON machine-readable ontology (439 nodes, 444 projected edges, root `Entity`).
   - `v1010/Ontology.md` and `v1010/ontology.json`: Snapshot manifests of the baseline v1010 state.
3. **Competitor Proposals:**
   - `UpperOntologyGemini.md`: Preserved initial proposal authored by Gemini in Phase 1 under sandbox isolation (tripartite `Concrete` / `Abstract` / `Intentional`).
   - `UpperOntologyAstra.md`: Astra's independent proposal (82 KB, six open categories: `Object`, `Occurrence`, `Particular feature`, `Region`, `Content`, `Formal entity`).
   - `UpperOntologyClaudeFable.md`: Claude Fable's independent proposal (79 KB, `Particular` vs. `Predicable` root cut, rigid classes vs. non-rigid roles, UFO relators, Characterized Objects).
   - `GPT/` Proposal Package (GPT-5 / Sol):
     - `GPT/architecture.md`: Architectural rationale, dual-route `Realized entity` vs. `Abstract entity`.
     - `GPT/ontology-tree.md`: Complete canonical tree (555 defined classes, 14 maximum canonical depth).
     - `GPT/ontology.json`: JSON data model (555 nodes, definitions, primary/alternate parents).
     - `GPT/coverage-map.md` & `GPT/coverage-map.json`: Mappings of all 439 incumbent nodes.
     - `GPT/validate.py`: Automated validation test suite.
     - `GPT/stress-tests.md`: Counterexample analyses across mathematical, biological, and social domains.

### 1.2 Executable Tests Run
- `GPT/validate.py` was executed directly within the repository environment. Verification confirmed:
  - 393 validation checks passed successfully.
  - 555 canonical classes, 554 canonical tree edges, 31 alternate superclass edges, 46 defined class expressions, and 20 typed predicate examples.
  - 439 of 439 original records accounted for (340 revised, 72 disambiguated, 23 faceted, 4 merged aliases).
- Structural integrity traversals were programmatically executed across `ontology.json` (439 nodes) and `GPT/ontology.json` (555 nodes) to verify tree depth, leaf distributions, parent-child arity, and cycle freedom.

### 1.3 Methodological Limits and Unverified Claims
- External network requests are restricted by sandbox policy; external URLs referenced in `Ontology.md` (e.g., NCBI Taxonomy, OneZoom, TimeTree, Catalogue of Life APIs) were evaluated against the frozen text and JSON artifacts preserved in the repository rather than live endpoints.
- Biological phylogenetic accuracy of deeper clades (e.g., specific placement of extinct synapsid fossils and deep microbial polytomies) is verified against retrieved NCBI taxonomy tables embedded in `GPT/ontology.json`, but remains subject to ongoing paleontological revision.
- Cross-model consensus is explicitly treated as zero evidence of philosophical truth; agreements between Astra, Claude, GPT, and Gemini are analyzed on formal and structural merits alone.

---

## 2. Systematic Comparative Critique of Ontology Proposals

### 2.1 The Incumbent Omniversal Ontology (`Ontology.md` / `ontology.json`)
The incumbent Omniversal Ontology has an intuitive, browsable character, but suffers from severe foundational defects where formal ontology and software design meet.

1. **The Abstract/Realized/Property/Relation Quadrichotomy (Category Mistake at L1):**
   - *Node/Edge:* `Entity` $\rightarrow$ `Realized entity` | `Abstract entity` | `Property` | `Relation`.
   - *Problematic Definition:* `Realized entity` is defined as "an entity that takes no arguments and has spatiotemporal embodiment"; `Abstract entity` is defined as "an entity that takes no arguments and lacks spatiotemporal embodiment"; `Property` is "an entity that takes one argument"; `Relation` is "an entity that takes more than one argument".
   - *Defect:* This partitions L1 by cross-cutting two completely unrelated axes: **metaphysical embodiment** (embodied vs. unembodied) and **predicate arity** ($0$ vs. $1$ vs. $>1$). This is a textbook category mistake. Under this definition, if a property lacks spatiotemporal embodiment, does it belong in `Abstract entity` or `Property`? If an embodied physical object takes zero arguments, it fits `Realized entity`. But what about a physical quality trope (e.g., the specific mass of an electron)? It has spatiotemporal embodiment yet characterizes a bearer (takes 1 argument). The incumbent model forces a choice between two incompatible classification axes at the very root of the tree.
   - *Remedy:* Segregate predicables/predicates from particulars, or eliminate arity as a top-level taxonomic edge.

2. **The "Abstract Person" Blunder (Severe Ontological Fracture):**
   - *Node/Edge:* `Abstract entity` $\rightarrow$ `Social entity` $\rightarrow$ `Person` ("An individual human being considered as a social participant").
   - *Problematic Claim:* `Person` is placed under `Abstract entity` alongside `Number`, `Proposition`, and `Notation`.
   - *Concrete Counterexample:* Socrates is a biological primate, a material body of 70 kg, and an intentional agent walking through Athens. If `Abstract entity` "lacks spatiotemporal embodiment," then classifying Socrates under `Abstract entity` asserts that Socrates has no physical body. Conversely, if Socrates is placed under `Realized entity` $\rightarrow$ `Object` $\rightarrow$ `Item` $\rightarrow$ `Biological object` $\rightarrow$ `Homo sapiens`, the ontology splits the human being into two unconnected entities: an abstract social "Person" and a physical "Organism."
   - *Remedy:* Classify `Person` as a complex continuant/agent under `Object`, with biological ancestry unified with psychological agency, and treat "social participant" as a role or facet.

3. **Institutional and Social Entities as Disembodied Abstractions:**
   - *Node/Edge:* `Abstract entity` $\rightarrow$ `Institutional entity` $\rightarrow$ `Organization`, `Government`, `Corporation`, `Court`.
   - *Defect:* A government levies taxes, deploys police forces, and occupies land; a corporation owns real estate and enters binding contracts. Classifying institutions as `Abstract entity` conflates the **abstract legal framework** (the charter, laws, or text) with the **socially constituted continuant** that possesses causal and legal efficacy in the physical world.
   - *Remedy:* Reclassify institutions as `Social object` / `Socially constituted entity` under continuants/objects, while assigning their rules and charters to `Directive specification` / `Normative content`.

4. **Category Errors in the `Property` Subtree:**
   - *Node/Edge:* `Property` $\rightarrow$ `Quality value` ("A value that specifies a quality on a scale or comparison").
   - *Defect:* `Property` is defined as "an entity that takes one argument." A `Quality value` (such as `5.2 meters`, `#FF0000`, or `severe`) is an argument, a point in a quality space, or an evaluation token. A value takes *zero* arguments. Placing `Quality value` as a subclass of `Property` violates the parent's definition.
   - *Remedy:* Relocate values to `Formal entity` / `Value` or `Abstract entity` / `Scale position`.

5. **Conflation of Normative Content, States, and Unary Predicates:**
   - *Node/Edge:* `Property` $\rightarrow$ `Norm`, `Obligation`, `Goal`, `Purpose`.
   - *Defect:* A `Norm` ("Thou shall not steal") is a directive proposition/specification. An `Obligation` is a normative relational position binding an agent to a beneficiary or community. A `Goal` is a desired state of affairs (a proposition). None of these are unary predicates of the form $P(x)$ in the sense that "Redness" or "Spherical" are.

6. **The `Relation` Branch Lacks Signatures and Conflates Meta-Relations:**
   - *Node/Edge:* `Relation` $\rightarrow$ `Classification relation` ("A relation that assigns an entity to a kind or category").
   - *Defect:* `Classification relation` is `instance-of` or `subclass-of`—the very structural relation constructing the ontology itself. Placing meta-modelling relations alongside domain relations (`Spatial relation`, `Causal relation`) confuses the object-language and metalanguage levels. Furthermore, relations are enumerated as an unconstrained taxonomy without specifying argument roles, domains, or ranges.

---

### 2.2 Initial Gemini Proposal (`UpperOntologyGemini.md`)
The initial Gemini proposal attempted to address the incumbent's errors using a three-world metaphysical architecture (`ConcreteEntity`, `AbstractEntity`, `IntentionalEntity`). While philosophically defensive in an isolated essay, repository inspection reveals distinct structural flaws:

1. **The Platonist Universal / Concrete Trope Fracture:**
   - *Node/Edge:* `AbstractEntity/Predicate/Property` vs. `ConcreteEntity/Continuant/DependentContinuant`.
   - *Defect:* Forcing all properties into `AbstractEntity` (as Platonic universals) while placing bearer-specific features into `DependentContinuant` forces every basic concept (e.g., "Mass", "Temperature", "Color") to exist in two disconnected branches. A user navigating a 20-Questions or browsable hierarchy cannot find a single coherent node for physical properties.
2. **Intentional Overreach (Lumping Fiction with Institutions):**
   - *Node/Edge:* `IntentionalEntity` $\rightarrow$ `SocialInstitutionalEntity` & `FictionalOrImpossibleEntity`.
   - *Defect:* Conflating a bank (`SocialInstitutionalEntity`) with Sherlock Holmes (`FictionalReferent`) under "Intentional" obscures the massive causal asymmetry between social realities that command real physical resources and pure narrative fictions.
3. **Absence of OntoClean Rigor (Kind vs. Role Conflation):**
   - *Defect:* The proposal lacked formal mechanisms to separate rigid categories (which an entity cannot cease to be without ceasing to exist, such as `Organism`) from non-rigid, anti-rigid roles (such as `Student`, `Employee`, `Food`).
4. **Reduction of Properties and Relations to Mathematical Predicates:**
   - *Defect:* Treating all properties as logical `Predicates` misses their empirical role as physical qualities, dispositions, and capacities.

---

### 2.3 The GPT / Sol Proposal (`GPT/` Package)
The GPT/Sol proposal represents an impressive engineering effort: 555 classes, fully mapped from the 439 incumbent nodes, supported by executable Python tests and clean documentation. However, it contains several critical structural compromises:

1. **Preservation of the Problematic `RealizedEntity` vs. `AbstractEntity` Dichotomy:**
   - *Node/Edge:* `Entity` $\rightarrow$ `Realized entity` | `Abstract entity`.
   - *Defect:* GPT retains the incumbent's L1 binary cut, defining `Realized entity` by "concrete occurrence, embodiment, or situated realization" and `Abstract entity` by "individuated without reference to a particular concrete realization." This retains a fundamental border friction:
     - Where does an institutional charter or legal code live? It is an abstract normative structure (`Abstract entity`), but its legal force exists only within a situated, concrete historical jurisdiction (`Realized entity`).
     - Where does a computer program live? As an algorithm it is abstract; as an installed software artifact executing on silicon it is concrete.
2. **`Purpose instance` as a `Dependent feature` (Ontological Incoherence):**
   - *Node/Edge:* `Realized entity` $\rightarrow$ `Dependent feature` $\rightarrow$ `Purpose instance` ("A dependent feature constituted by an intended outcome assigned to a bearer").
   - *Defect:* GPT puts `Purpose instance` alongside `Quality instance` (e.g., mass, shape) and `Disposition instance` (e.g., fragility, solubility). But a purpose does not inhere in an object's physical substrate. If a human assigns a rock the purpose of being a doorstop, the rock's physical constitution undergoes zero change. Purpose is an **extrinsic, intentional assignment** (a teleological role), not an inherent physical trope.
3. **`Entity kind specification` Subordinated to `Predicate specification`:**
   - *Node/Edge:* `Abstract entity` $\rightarrow$ `Predicate specification` $\rightarrow$ `Entity kind specification`.
   - *Defect:* A kind specification (e.g., `Human`, `Electron`, `OakTree`) is not merely a unary predicate $P(x)$. It supplies **identity, persistence, and individuation conditions** over time (a sortal). Treating kinds as mere predicate specifications alongside accidental properties (like "Red" or "Hot") collapses the crucial philosophical distinction between what an entity *is* and what an entity *has*.
4. **Coverage Mapping Overreach (Label Accounting vs. Meaning Preservation):**
   - *Finding in `GPT/coverage-map.md`:*
     - The incumbent node `Agent` ("an entity capable of intentional action") was mapped to a faceted class expression `QualifiedObject` with `AgencySpecification`, removing `Agent` from the canonical tree. But in ordinary language and knowledge representation, an `Agent` is a primary organizing category, not an awkward class expression.
     - Biological ranks were arbitrarily collapsed to guarantee a maximum tree depth of 14 (e.g., jumping `Great ape` to place `Human` directly under `Ape`), sacrificing cladistic fidelity for a presentation depth heuristic.

---

### 2.4 The Astra Proposal (`UpperOntologyAstra.md`)
Astra provides deep philosophical clarity, particularly in dissecting the anatomy of predication and the nature of regions.

1. **Achievements:**
   - Rejects the forced binary Abstract/Concrete divide, replacing it with six open categories: `Object`, `Occurrence`, `Particular feature`, `Region`, `Content`, `Formal entity`.
   - Outstanding property analysis: Cleanly isolates the **Quality Trope** (`FQ`), the **Unary Predicate** (`CPP`), the **Quality Space Region** (`RQ`), the **Quantity Value** (`MVQ`), and the **Directive Specification** (`CD`).
   - Treats `Region` (`R`) with mathematical seriousness, separating spatial, temporal, spatiotemporal, and quality-space dimensions.
2. **Defects & Vulnerabilities:**
   - *Abandonment of Tree Disjointness:* Astra declares its six categories to be an "open collection of partly overlapping categories." While metaphysically honest, permitting fundamental categories to overlap at Level 1 degrades automated reasoning, query routing, and taxonomic navigability.
   - *`Subject` (`OU`) as a Sibling of `Physical object` and `Social object`:* Placing `Subject` ("an object admitted as a center of experience or intentional agency") under `Object` creates a direct identity crisis: a human being is simultaneously a `Physical object` (`OPB Material body`) and an `Experiencing subject` (`OUE`). If these overlap, the tree ceases to provide a canonical primary home.
   - *Over-elevation of `Region`:* Promoting `Region` to Level 1 makes spatial and temporal extents peers of concrete material bodies and processes. In physics, space and time are either relational properties of physical fields or abstract mathematical manifolds. Making `Region` a top-level peer reintroduces substantivalism as a rigid upper-ontology commitment.

---

### 2.5 The Claude Fable Proposal (`UpperOntologyClaudeFable.md`)
Claude Fable offers the most formally disciplined proposal in the repository, anchoring its design in OntoClean, UFO, and philosophical logic.

1. **Achievements:**
   - Rigorous first cut: `Particular` vs. `Predicable`. This immediately eliminates the confused arity/embodiment hybrid of the incumbent.
   - Incorporates OntoClean metaproperties directly into the Property tree: `Kind` (+Rigid, +Identity), `Phase` (-Rigid, intrinsic), `Role` (-Rigid, relational), and `Attribute` (value-mapping).
   - Introduces UFO `Relator` under `Feature` as the truthmaker for external relations (e.g., a marriage, a contractual bond, an employment treaty).
   - Resolves the Meinongian puzzle via `Characterized Object` with dual predication (internal characterization vs. external ontological status).
2. **Defects & Vulnerabilities:**
   - *The `Particular` vs. `Predicable` First Cut is Hostile to Browsing:* While logically pristine, forcing a human user or searcher to choose between "Particular" and "Predicable" at Level 1 fails the *traversal intelligibility* mandate of `OntologyDesignMemoranda.md`. In an encyclopedic knowledge base, users do not navigate to "Dog" by first thinking "I want an individual particular rather than a universal predicable."
   - *`Formal Object` Classified Under `Particular`:* Placing `Number`, `Set`, `Function`, and `Proposition` under `Particular` (relying on the technical logic sense that the number $7$ is an individual rather than a predicate) causes immediate cognitive dissonance. In standard taxonomy, mathematical structures are categorized as abstract universals or formal systems, not "particulars."
   - *Relator Overhead:* Forcing every social and relational fact into a UFO `Relator` introduces excessive metaphysical machinery that complicates intermediate domain modeling.

---

## 3. Dedicated Property and Relation Reconciliation

The central task of this Phase 2 evaluation is resolving the conceptual confusion surrounding `Property` and `Relation`. Across the five proposals, terms like "Quality", "Property", "Attribute", "Feature", "Value", and "Relation" are used with conflicting semantics.

### 3.1 The Fundamental Category Errors in Predication
A rigorous ontology must distinguish between five completely different ontological tiers:
1. **The Inherent Feature (Trope / Particular Quality):** The particular, non-shareable redness, mass, or electrical charge inhering in a specific physical bearer at a specific time. If the bearer is destroyed, the trope ceases to exist.
2. **The Universally Applicable Condition (Predicate / Property):** The repeatable, sharable condition or rule (e.g., $\text{Red}(x)$, $\text{Mass}(x)$) that can be predicated of multiple bearers.
3. **The Dimension / Quality Space:** The structured coordinate space or continuum (e.g., the visible color spectrum, the continuum of real numbers representing mass in kilograms).
4. **The Evaluation Value / Datum:** The point, vector, or nominal symbol representing a location on a scale (e.g., `#FF0000`, `70.4 kg`, `true`).
5. **The Social / Contextual Assignment:** The normative or functional role attributed to an entity by an external agent (e.g., being a "Doorstop", being a "President", being "Money").

The incumbent ontology conflates tiers 1, 2, 4, and 5 under `Property (takes one argument)`. GPT/Sol corrects tier 4 (values) and tier 1 (tropes), but leaves tier 5 confused. Astra and Claude provide the tools to systematically separate all five.

### 3.2 The Fourfold Quality Distinction
To reconcile Property across all proposals, we establish the following explicit architecture:

$$\begin{array}{rcccl}
\text{Bearer-bound Trope} & \longrightarrow & \textbf{Particular Feature} & (\text{e.g., Socrates' wisdom, this apple's red}) \\
\text{Repeatable Condition} & \longrightarrow & \textbf{Property (Unary Predicate)} & (\text{e.g., is-wise, is-red}) \\
\text{Continuous Dimension} & \longrightarrow & \textbf{Quality Space (Region)} & (\text{e.g., CIELAB color space, mass scale}) \\
\text{Scale Point / Token} & \longrightarrow & \textbf{Quality / Quantity Value} & (\text{e.g., } 70\text{ kg}, \text{"Scarlet"})
\end{array}$$

- **Quality Value is NOT a Property:** A quality value has arity 0. It is a formal evaluation token. It must be moved entirely out of `Property` and placed under `Formal entity` / `Value`.
- **Bearer-specific Qualities are NOT Abstract Properties:** A bearer's mass or fragility is a concrete, dependent feature of the bearer. It belongs under `Particular feature` / `Dependent feature`.
- **Property is Strictly an Applicable Unary Condition:** `Property` must denote the repeatable predicate specification capable of being asserted of an argument.

### 3.3 Dispositions, Capacities, and Functions
- **Disposition:** An intrinsic, structurally grounded tendency of an entity to manifest a specific process under specific triggering conditions (e.g., fragility $\rightarrow$ shattering on impact; solubility $\rightarrow$ dissolving in water). Dispositions are *realized* through physical structure, regardless of whether they ever manifest.
- **Capability:** A disposition assessed against a normative performance standard under intentional agency (e.g., a human's capability to read English; an aircraft's capability to reach Mach 2).
- **Function:** A disposition that has been selected (biologically via evolution, or artifactually via intentional design) to achieve an outcome (e.g., the heart's function to pump blood; the clock's function to keep time).
*Reconciliation:* `Disposition` is the ontological base (under `Particular feature`). `Capability` is an agency-linked subtype. `Function` links a disposition to a purpose or design framework.

### 3.4 Norms, Obligations, Roles, and Relators
- **Norm:** An informational directive (under `Content` $\rightarrow$ `Directive specification`) prescribing, permitting, or prohibiting actions.
- **Obligation / Entitlement:** The normative status or position borne by a specific agent under a norm. It is not an abstract property, but an extrinsic `Relational feature` of the agent.
- **Role:** An anti-rigid, non-essential status assumed by an entity in a relational context (e.g., `Patient`, `Teacher`, `Substrate`). Following OntoClean, roles must *never* be made superclasses of rigid kinds. A `Person` is not a subclass of `Teacher`; rather, a `Person` *plays the role of* `Teacher`.
- **Relator:** The social or physical bond that grounds an external relation (e.g., an employment contract, a treaty, a marriage certificate).

### 3.5 Purposes, Goals, and Preference Orderings
- **Goal / Purpose:** A teleological specification of a target state of affairs. Ontologically, a goal is a proposition or state description treated as a target by an agent. It is neither a physical trope nor an intrinsic property.
- **Preference:** An intentional ordering relation over alternative states or outcomes.

### 3.6 Relations: Arity, Internal vs. External, and Meta-Relations
- **Arity is Purely Syntactic, Not Metaphysical:** Fixing an argument in an $n$-ary relation yields an $(n-1)$-ary relation (e.g., $\text{CapitalOf}(x, y)$ with $y = \text{France}$ yields the unary property $\text{CapitalOfFrance}(x)$). Arity is a feature of predicate specifications, not of the entities in the world.
- **Internal vs. External Relations:**
  - *Internal Relation:* A relation that supervenes entirely on the intrinsic features of its relata (e.g., $\text{TallerThan}(A, B)$ holds strictly because $\text{Height}(A) > \text{Height}(B)$). No additional entity in the world is needed to connect them.
  - *External Relation:* A relation that requires an external tie, event, or relator (e.g., $\text{Employs}(\text{Acme}, \text{John})$; $\text{MarriedTo}(A, B)$).
- **Isolation of Meta-Relations:** `Classification relation` (`instance-of`, `subclass-of`) and `Part-whole relation` (`mereological inclusion`) must not be mixed into an arbitrary flat list with causal and social relations. Meta-relations generate the knowledge graph structure itself; domain relations describe connections between entities within the domain.

---

### 3.7 Comprehensive Comparative Reconciliation Matrix

| Concept | Incumbent (`Ontology.md`) | GPT / Sol (`GPT/`) | Astra (`UpperOntologyAstra.md`) | Claude Fable (`UpperOntologyClaudeFable.md`) | Reconciled Resolution (Gemini Final) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Root Definition** | "That which can be referred to, even if nonexistent" | "That which can be referred to, even if nonexistent" | Individuated subject admitted to discourse | Subject of predication/quantification | **"A distinguishable subject of predication or discourse"** (distinguishes reference from existence) |
| **Top-Level Cut** | Realized / Abstract / Property / Relation (4-way arity/embodiment hybrid) | Realized entity / Abstract entity (2-way binary) | Object / Occurrence / Particular feature / Region / Content / Formal entity (6-way open) | Particular / Predicable (2-way instantiability) | **Object / Occurrence / Dependent Feature / Region / Informational Content / Formal Structure** (6-way disjoint, browsing-intelligible) |
| **Quality Trope** | Merged under `Property/Quality` | `Realized entity / Dependent feature / Quality instance` | `Particular feature / Quality (FQ)` | `Particular / Feature / Quality` | **`Dependent Feature` $\rightarrow$ `Intrinsic Quality`** (bearer-dependent concrete trope) |
| **Repeatable Property** | `Property` (L1, arity 1) | `Abstract entity / Predicate specification / Property` | `Content / Predicate / Property (CPP)` | `Predicable / Property` (subdivided into Kind/Role/etc.) | **`Informational Content` $\rightarrow$ `Predicate Specification` $\rightarrow$ `Unary Property`** |
| **Quality / Quantity Value** | `Property / Quality value` (Defective arity) | `Abstract entity / Quantity value`, `Quality value` | `Formal entity / Value (MVQ, MVC)` | `Particular / Formal Object / Magnitude` | **`Formal Structure` $\rightarrow$ `Evaluation Value` $\rightarrow$ `Magnitude Value` / `Category Value`** |
| **Disposition / Capability** | `Property / Disposition`, `Capability` | `Dependent feature / Disposition instance` | `Particular feature / Disposition (FD)`, `Capability (FDC)` | `Particular / Feature / Disposition` | **`Dependent Feature` $\rightarrow$ `Disposition` $\rightarrow$ `Physical Disposition` / `Agentic Capability`** |
| **Norm / Obligation** | `Property / Norm`, `Obligation` | `Information content / Normative content` | `Content / Directive (CDN)` vs. `Feature / Normative position (FRN)` | `Construct / Content / Norm` vs. `Feature / Relator / Obligation` | **Split:** Norm = `Directive Specification`; Obligation = `Relational Feature` (Normative Status of bearer) |
| **Purpose / Goal** | `Property / Purpose`, `Goal` | `Dependent feature / Purpose instance` (Defective) | `Content / Directive / Goal specification (CDG)` | `Construct / Content / Specification` | **`Informational Content` $\rightarrow$ `Directive Specification` $\rightarrow$ `Goal Specification`** |
| **Relations ($n \ge 2$)** | `Relation` (L1, 19 flat children) | `Abstract entity / Predicate specification / Relation` | `Content / Predicate / Relation (CPR)` | `Predicable / Relation` (Internal vs External) | **`Informational Content` $\rightarrow$ `Predicate Specification` $\rightarrow$ `Relation Specification`** |
| **Relational Truthmaker** | Not recognized | `Realized entity / State instance / Relational state` | `Particular feature / Relational feature (FRR, FRN)` | `Particular / Feature / Relator` | **`Dependent Feature` $\rightarrow$ `Relational State / Relator`** |
| **Human / Person** | `Abstract entity / Social entity / Person` (Defective) | `Realized entity / Object / Biotic / Organism / Human` | `Object / Physical / Material body` + `Object / Subject` | `Object / Physical Object / Organism` (Person as Agent) | **`Object` $\rightarrow$ `Organism` $\rightarrow$ `Human Organism`** (Personhood = Agentic capacity/role) |
| **Corporation / Institution** | `Abstract entity / Institutional entity` | `Realized entity / Object / Social object / Organization` | `Object / Social object / Institutional continuant (OSI)` | `Particular / Object / Social Object` | **`Object` $\rightarrow$ `Social Continuant` $\rightarrow$ `Institution / Organization`** |
| **Fictional Characters** | Not handled cleanly | Open ambiguity | `Content / Narrative content` | `Construct / Characterized Object` | **`Informational Content` $\rightarrow$ `Representational Content` $\rightarrow$ `Fictional / Stipulated Entity`** |

---

## 4. Assessment of Existing Mappings, Crosswalks, and Coverage

### 4.1 Audit of the GPT Coverage Map (439 Records)
`GPT/coverage-map.md` maps every single one of the 439 nodes in `ontology.json`. A line-by-line audit reveals that while the mapping is exhaustive in accounting for strings, it exhibits four distinct structural patterns:

1. **Genuinely Corrected Category Errors (340 records):**
   - Correctly rescuing `Organization`, `Corporation`, and `Government` from `Abstract entity` into `Social object`.
   - Correctly moving `Quality value` from `Property` to `Abstract entity / Quality value`.
   - Correctly nesting organisms into monophyletic clades (e.g., `Bird` under `Theropod`, `Mammal` under `Synapsid`).
2. **Evasive Class Expressions (Faceted Evasions) (23 records):**
   - Nodes like `Agent`, `Food`, `Weapon`, `Location`, and `Product` were deleted as primary classes and converted into complex expressions: e.g., `QualifiedObject with FoodSpecification`.
   - *Critique:* While technically pure from an OntoClean standpoint (since "food" is a functional role played by biological or chemical portions, not a rigid kind), in a general-purpose knowledge tree, forcing users through class expressions destroys browsing usability. An ontology designed for human exploration must retain canonical role projections while noting their non-rigid status in metadata.
3. **Lossy Mergers and Semantic Drift (4 records):**
   - Merging `PhysicalSystemModel` and `MathematicalModel` into a single class under `InformationContent`. This obscures the distinction between a mathematical formal structure (e.g., an equation) and its empirical application to a target physical system.
4. **Depth-Truncation Artifacts:**
   - Truncating NCBI taxonomic clades to satisfy an arbitrary maximum depth of 14 (jumping `Hominidae` and `Hominoidea` so `Human` attaches directly to `Ape`). This sacrifices scientific provenance for visual layout.

### 4.2 Policy for Reconciling Disagreements and Preserving Meaning
When reconciling conflicting models across the repository, the following policies must govern:
1. **Never Create a Mere Label Union:** Do not combine competing trees by merging synonym labels into single bloated nodes that conceal contradictory definitions.
2. **Kind over Role for Canonical Hierarchy:** Use rigid kind identity for the single primary parent. Roles, contexts, and uses are captured via secondary classification facets.
3. **Carrier vs. Content Separation:** Any representational entity must be cleanly bifurcated:
   - The *Carrier* (the physical book, silicon chip, sound wave) $\rightarrow$ `Object` / `Process`.
   - The *Content* (the novel, text, algorithm, symphonic score) $\rightarrow$ `Informational Content`.
4. **Stable Identifiers and Deprecation Policy:**
   - Preserve existing IDs from `ontology.json` wherever semantic meaning is preserved.
   - Where a node must be split (e.g., `Property` into `IntrinsicQuality` and `PropertySpecification`), assign explicit, versioned URIs (e.g., `urn:onto:prop:spec:v2` vs. `urn:onto:feature:quality:v2`).
   - Retain deprecated nodes as aliases with formal `owl:deprecated true` and explicit migration pointers (`replacedBy`).

---

## 5. Recommended Reconciled Upper Tree

The recommended upper tree synthesizes the structural rigor of Claude Fable and Astra with the practical coverage and testability of GPT/Sol, while adhering strictly to the display boundary of **at most three subclass edges below `Entity`** (Root $\rightarrow$ L1 $\rightarrow$ L2 $\rightarrow$ L3).

### 5.1 Architecture and Root Definition

- **Root Node:** `Entity`
- **Definition:** *A distinguishable subject of predication or discourse, possessing identity criteria under an interpretation, regardless of actual spatiotemporal existence.*
- **Design Stance:**
  - Replaces "that which can be referred to, even if nonexistent" to eliminate linguistic reference dependence and Meinongian paradoxes.
  - Distinguishes **Particulars** (bearers, occurrences, tropes, regions) from **Abstract Structures** (formal systems, values) and **Informational Contents** (specifications, propositions, fictions).
  - Establishes **six mutually disjoint Level 1 categories** optimized for cognitive intelligibility, avoiding both the Platonist Abstract/Concrete bottleneck and the abstruse Particular/Predicable split.

---

### 5.2 Complete Upper Tree (Root through Great-Grandchildren)

```text
Entity
├── Object
│   ├── Physical Body
│   │   ├── Inanimate Body
│   │   ├── Organism
│   │   └── Physical Aggregate
│   ├── Social Continuant
│   │   ├── Institution
│   │   ├── Social Group
│   │   └── Conventional Artifact
│   └── Agentic System
│       ├── Individual Agent
│       ├── Collective Agent
│       └── Artificial Agent
├── Occurrence
│   ├── Process
│   │   ├── Physical Process
│   │   ├── Biological Process
│   │   └── Cognitive Process
│   ├── Event
│   │   ├── Natural Event
│   │   ├── Action
│   │   └── Social Event
│   └── State Instance
│       ├── Physical State
│       ├── Mental State
│       └── Relational State
├── Dependent Feature
│   ├── Intrinsic Quality
│   │   ├── Physical Quality
│   │   ├── Structural Morphology
│   │   └── Phenomenal Quality
│   ├── Disposition
│   │   ├── Physical Liability
│   │   ├── Functional Capacity
│   │   └── Agency Capability
│   └── Relational Feature
│       ├── Social Role Occupancy
│       ├── Normative Status
│       └── Grounded Relator
├── Region
│   ├── Spatial Region
│   │   ├── Spatial Point
│   │   └── Spatial Extent
│   ├── Temporal Region
│   │   ├── Temporal Instant
│   │   └── Temporal Interval
│   └── Spatiotemporal Region
│       ├── Spatiotemporal Path
│       └── Spatiotemporal Volume
├── Informational Content
│   ├── Predicate Specification
│   │   ├── Kind Specification
│   │   ├── Unary Property
│   │   └── Relation Specification
│   ├── Directive Specification
│   │   ├── Norm Specification
│   │   ├── Goal Specification
│   │   └── Plan Specification
│   └── Representational Content
│       ├── Descriptive Proposition
│       ├── Narrative Work
│       └── Fictional Entity Specification
└── Formal Structure
    ├── Mathematical Entity
    │   ├── Number
    │   ├── Mathematical Collection
    │   └── Mathematical System
    ├── Symbolic System
    │   ├── Formal Language
    │   ├── Notation Syntax
    │   └── Computational Model
    └── Evaluation Value
        ├── Magnitude Value
        ├── Category Value
        └── Truth Value
```

---

### 5.3 Discriminating Definitions

#### Level 1 Categories (Children of `Entity`)
1. **`Object`**: An entity tracked as a unified continuant possessing identity across time, not individuated as an occurrence, dependent feature, region, content, or formal rule.
2. **`Occurrence`**: An entity that unfolds, occurs, or obtains through time, possessing temporal extent or temporal boundaries.
3. **`Dependent Feature`**: A concrete particular that inherently depends upon and inheres in one or more specific bearer objects or systems.
4. **`Region`**: A continuous or discrete extent, locus, or coordinate manifold within space, time, or spacetime, distinguished from any physical occupant.
5. **`Informational Content`**: Repeatable semantic meaning, condition, prescription, or representation, abstracted away from any physical carrier or token inscription.
6. **`Formal Structure`**: An objective, axiomatic, or rule-governed entity individuated by mathematical, logical, symbolic, or evaluative definitions.

#### Subtrees through Level 3 (Great-Grandchildren)

##### 1. Subtree `Object`
- **`Physical Body`**: An object individuated by mass-energy constitution and spatial unity.
  - **`Inanimate Body`**: A physical body whose identity and composition do not derive from biological life (e.g., rock, mineral crystal, star).
  - **`Organism`**: A physical body constituted as a self-maintaining, living cellular biological system (e.g., bacterium, oak tree, human primate).
  - **`Physical Aggregate`**: An object individuated as a loose collective or mass of physical bodies without organismal or anatomical unity (e.g., sand dune, asteroid belt).
- **`Social Continuant`**: An object whose persistence depends on collective intentionality, recognition, or social practices.
  - **`Institution`**: A durable, rule-governed social structure with recognized authority or functions (e.g., legal system, university, central bank).
  - **`Social Group`**: A collection of intentional agents bound by shared identity, affiliation, or organized interaction (e.g., family, club, union).
  - **`Conventional Artifact`**: An object whose social identity and functions are defined by conventional status functions rather than physical shape alone (e.g., physical currency token, boundary marker, passport).
- **`Agentic System`**: An object possessing goal-directed autonomy, perception, and intentional action.
  - **`Individual Agent`**: A singular biological or personal center of intentional action (e.g., person, autonomous animal).
  - **`Collective Agent`**: An organized group structured by decision-making procedures that acts as a single intentional agent (e.g., corporation, state government).
  - **`Artificial Agent`**: A synthetic or computational system exhibiting autonomous, goal-directed behavior (e.g., autonomous software agent, robotic system).

##### 2. Subtree `Occurrence`
- **`Process`**: An occurrence characterized by ongoing temporal unfolding, change, or activity.
  - **`Physical Process`**: A process governed by physical, chemical, or thermodynamic laws (e.g., combustion, radioactive decay).
  - **`Biological Process`**: A process constituted by living metabolic, developmental, or evolutionary activity (e.g., photosynthesis, cellular mitosis).
  - **`Cognitive Process`**: A process constituted by mental, perceptual, or computational reasoning activity (e.g., sensory perception, problem solving).
- **`Event`**: An occurrence individuated as a bounded transition, achievement, or historical happening.
  - **`Natural Event`**: A bounded occurrence occurring without intentional agency (e.g., volcanic eruption, lightning strike).
  - **`Action`**: A bounded occurrence intentionally initiated by an agent (e.g., signing a contract, kicking a ball).
  - **`Social Event`**: A multi-agent coordinated historical or institutional happening (e.g., election, treaty signing, trial).
- **`State Instance`**: An occurrence consisting of the stable obtaining of a condition over a temporal interval.
  - **`Physical State`**: The configuration or thermodynamic condition of a physical system over time (e.g., thermal equilibrium, state of matter).
  - **`Mental State`**: The holding of an attitude, mood, or conscious state by a subject over an interval (e.g., believing $P$, experiencing pain).
  - **`Relational State`**: The ongoing obtaining of an external relationship or legal bond between participants (e.g., being married, state of war).

##### 3. Subtree `Dependent Feature`
- **`Intrinsic Quality`**: A dependent feature characterizing a bearer's internal constitution or morphology without reference to other entities.
  - **`Physical Quality`**: A quality directly measuring physical properties of a bearer (e.g., mass, charge, rest energy).
  - **`Structural Morphology`**: A quality concerning geometric shape, surface texture, or internal topological boundaries (e.g., spherical shape, porousness).
  - **`Phenomenal Quality`**: A quality characterizing subjective qualia or appearance to an observer (e.g., perceived redness, bitterness).
- **`Disposition`**: A dependent feature grounding a tendency, capacity, or liability to manifest a process under triggering conditions.
  - **`Physical Liability`**: An unguided physical susceptibility to undergo change (e.g., fragility, flammability, solubility).
  - **`Functional Capacity`**: An operative capability selected or engineered to perform a task (e.g., conductivity of a wire, catalytic power of an enzyme).
  - **`Agency Capability`**: An acquired or innate ability of an agent to execute an action (e.g., fluency in a language, ability to run).
- **`Relational Feature`**: A dependent feature whose individuation requires an external contextual framework or other entities.
  - **`Social Role Occupancy`**: The particular holding of an extrinsic role by an entity in a context (e.g., John's tenure as president).
  - **`Normative Status`**: An agent's standing as bound by an obligation, right, or legal liability (e.g., citizen's duty, debtor's liability).
  - **`Grounded Relator`**: A particular concrete entity that binds multiple relata into an external relationship (e.g., a specific employment bond).

##### 4. Subtree `Region`
- **`Spatial Region`**: A continuous or discrete locus in a spatial coordinate frame.
  - **`Spatial Point`**: A zero-dimensional spatial position.
  - **`Spatial Extent`**: A multi-dimensional spatial volume, area, or bounding manifold.
- **`Temporal Region`**: A locus or duration within a temporal dimension.
  - **`Temporal Instant`**: A zero-duration boundary point in time.
  - **`Temporal Interval`**: An extended duration or period of time.
- **`Spatiotemporal Region`**: A locus jointly individuated by spatial and temporal coordinates.
  - **`Spatiotemporal Path`**: A trajectory or world-line through spacetime.
  - **`Spatiotemporal Volume`**: An extended four-dimensional region in spacetime.

##### 5. Subtree `Informational Content`
- **`Predicate Specification`**: A reified condition or rule applicable to arguments to evaluate truth or classification.
  - **`Kind Specification`**: A sortal predicate supplying identity, persistence, and individuation conditions for a class (e.g., the concept `Canis familiaris`).
  - **`Unary Property`**: An applicable condition characterizing a single argument (e.g., `is-red`, `is-prime`).
  - **`Relation Specification`**: A multi-argument condition ($n \ge 2$) structuring ordered tuples (e.g., `is-parent-of`, `is-between`).
- **`Directive Specification`**: Content setting a standard, rule, outcome, or plan to guide or evaluate conduct.
  - **`Norm Specification`**: A rule prescribing, permitting, or prohibiting actions within a normative framework (e.g., legal statute, moral rule).
  - **`Goal Specification`**: A description of a desired or intended outcome (e.g., mission objective, target temperature).
  - **`Plan Specification`**: An organized procedure or algorithm of actions directed toward an outcome (e.g., flight plan, recipe).
- **`Representational Content`**: Content structured to depict, narrate, or model reality or fiction.
  - **`Descriptive Proposition`**: A truth-evaluable assertion about actual or hypothetical states of affairs (e.g., "Water boils at 100°C").
  - **`Narrative Work`**: An extended, coherent representational composition (e.g., historical biography, novel, documentary text).
  - **`Fictional Entity Specification`**: A stipulated concept or character description lacking actual physical reference (e.g., `Sherlock Holmes`, `Pegasus`).

##### 6. Subtree `Formal Structure`
- **`Mathematical Entity`**: A formal entity defined axiomatically within a mathematical framework.
  - **`Number`**: An entity specifying numerical count, magnitude, or ordinal position (e.g., integer, real number, complex number).
  - **`Mathematical Collection`**: An entity defined extensionally by membership or ordering axioms (e.g., set, class, sequence).
  - **`Mathematical System`**: A domain equipped with defined operations, relations, or topologies (e.g., algebraic group, metric space, graph).
- **`Symbolic System`**: A repeatable pattern of tokens and syntactic formation rules.
  - **`Formal Language`**: A set of well-formed expressions generated by a formal grammar (e.g., propositional calculus, Python syntax).
  - **`Notation Syntax`**: A conventional system of symbols and typographical conventions (e.g., musical notation, chemical notation).
  - **`Computational Model`**: A formalized state-transition specification (e.g., Turing machine, finite state automaton).
- **`Evaluation Value`**: A determinate position or token within an evaluation space or scale.
  - **`Magnitude Value`**: A quantitative scalar combining a number and a unit (e.g., $9.8\text{ m/s}^2$, $100\text{ K}$).
  - **`Category Value`**: A qualitative rating or categorical label within a nominal scale (e.g., "high", "Class A", "severe").
  - **`Truth Value`**: A formal semantic truth assignment (e.g., `True`, `False`, `Indeterminate`).

---

### 5.4 Explicit Split Policies and Boundary Analysis

1. **Split S1: `Entity` $\rightarrow$ `Object` | `Occurrence` | `Dependent Feature` | `Region` | `Informational Content` | `Formal Structure`**
   - *Organizing Axis:* Mode of individuation and ontological dependence.
   - *Status:* **Jointly Exhaustive and Mutually Disjoint.**
   - *Justification:* Every entity in discourse is either an independent continuant (`Object`), an unfolding temporal happening (`Occurrence`), a bearer-bound trope (`Dependent Feature`), an empty spatial/temporal coordinate locus (`Region`), a semantic/prescriptive meaning (`Informational Content`), or an axiomatic mathematical/evaluative rule (`Formal Structure`).
   - *Boundary Case:* **A Printed Book.** The physical ink and bound paper is an `Object` $\rightarrow$ `Physical Body`. The literary novel is an `Informational Content` $\rightarrow$ `Representational Content` $\rightarrow$ `Narrative Work`. The printing process is an `Occurrence` $\rightarrow$ `Process`. This prevents conflating the physical carrier with the intellectual content.
2. **Split S2: `Object` $\rightarrow$ `Physical Body` | `Social Continuant` | `Agentic System`**
   - *Organizing Axis:* Substrate of identity and agency.
   - *Status:* **Exhaustive.** (Where an entity is both a physical body and an agent, such as a human, the primary navigation parent is `Organism` under `Physical Body`, with `Agentic System` linked as a semantic superclass).
   - *Boundary Case:* **Corporation.** Primarily a `Social Continuant` $\rightarrow$ `Institution`, with secondary inheritance from `Agentic System` $\rightarrow$ `Collective Agent`.
3. **Split S3: `Dependent Feature` $\rightarrow$ `Intrinsic Quality` | `Disposition` | `Relational Feature`**
   - *Organizing Axis:* Autonomy of inherence (Internal constitution vs. Potential behavior vs. Relational/Contextual dependence).
   - *Status:* **Mutually Disjoint.**
   - *Boundary Case:* **Mass vs. Weight.** Mass is an `Intrinsic Quality` $\rightarrow$ `Physical Quality` (invariable across environments). Weight is a `Relational Feature` (depends upon the gravitational field of a second body).
4. **Split S4: `Informational Content` $\rightarrow$ `Predicate Specification` | `Directive Specification` | `Representational Content`**
   - *Organizing Axis:* Communicative and cognitive function (Condition specification vs. Normative prescription vs. Descriptive/Narrative representation).
   - *Status:* **Mutually Disjoint.**
   - *Boundary Case:* **A Traffic Law.** The law as an enacted statute is a `Directive Specification` $\rightarrow$ `Norm Specification`. The condition of exceeding 65 mph is a `Predicate Specification` $\rightarrow$ `Unary Property`.

---

### 5.5 Material Departures from the Independent Proposal
1. **Abolition of the Tripartite `Concrete` / `Abstract` / `Intentional` L1:**
   - *Reason:* Replaced with six clear, browsing-friendly categories. The previous L1 forced physical qualities and their concepts into separate universes and grouped physical banks with non-actual fictions under `Intentional`.
2. **Elevation of `Dependent Feature` as an L1 Peer:**
   - *Reason:* Tropes (bearer-specific qualities and dispositions) are central to scientific and everyday description. Subordinating them inside continuants made qualities inaccessible in knowledge navigation.
3. **Segregation of `Evaluation Value` from `Predicate Specification`:**
   - *Reason:* Rectifies the critical defect identified in `Ontology.md` where `Quality value` was classified under `Property` (arity 1). Values have arity 0 and live in `Formal Structure`.
4. **Integration of OntoClean Rigor:**
   - *Reason:* Explicitly prevents roles (`Food`, `Weapon`, `Student`) from polluting the primary `is-a` backbone above rigid natural kinds.

---

### 5.6 Unresolved Architectural Decisions
1. **The Substantivalism vs. Relationalism Decision for `Region`:**
   - *Dilemma:* Does empty space exist as an entity (`Region`), or is space merely a system of relations between physical bodies?
   - *Discrimination Test:* If the repository adopts general relativity and field theory as primary physical foundations, spatial regions should be modeled as features of gravitational and quantum fields. If it prioritizes intuitive GIS mapping and geometry, `Region` earns its place as an L1 peer. The current proposal retains `Region` at L1 for browsing clarity, pending a formal physics module audit.
2. **Agenthood: Primary Kind vs. Cross-Cutting Facet:**
   - *Dilemma:* Is `Person` primarily an `Organism` that possesses agency, or is `Agent` a fundamental ontological kind peer to `Physical Body`?
   - *Discrimination Test:* If AI systems and corporations achieve legal and cognitive peer status with human agents, `Agentic System` will need promotion to a primary root branch independent of physical substrate.

---

## 6. Actionable Repository Audit Sequence and Bounded Migration Plan

To implement this reconciliation without destabilizing existing tools or rendering scripts, the project should execute the following five-stage bounded audit sequence:

### Phase 2.1: The Emergency Category-Error Repair (Sanitizing `Abstract entity`)
- **Action:** Surgically relocate `Person`, `Group`, `Community`, `Organization`, `Government`, and `Corporation` out of `Abstract entity`.
- **Target Location:** Move them into `Object` $\rightarrow$ `Social Continuant` and `Object` $\rightarrow$ `Organism`.
- **Impact:** Eliminates the catastrophic claim in `ontology.json` that human persons and governments lack spatiotemporal embodiment.

### Phase 2.2: The Property/Value/Predicate Tripartition
- **Action:** Disassemble the incumbent `Property` (arity 1) branch.
- **Relocations:**
  - Move `Quality value` to `Formal Structure` $\rightarrow$ `Evaluation Value`.
  - Move `Norm`, `Obligation`, `Goal`, and `Purpose` to `Informational Content` $\rightarrow$ `Directive Specification`.
  - Retain `Unary Property` and `Relation Specification` under `Informational Content` $\rightarrow$ `Predicate Specification`.
  - Migrate concrete physical qualities (mass, shape, color trope) into `Dependent Feature` $\rightarrow$ `Intrinsic Quality`.

### Phase 2.3: OntoClean Rigidity and Role Cleansing
- **Action:** Audit all nodes in `ontology.json` where roles currently masquerade as kinds.
- **Rules:**
  - Convert `Weapon`, `Food`, `Pet`, `Vehicle`, `Instrument` into secondary role facets or defined class expressions (`Physical Object playing Role X`).
  - Preserve `Organism`, `Mineral`, `Chemical Compound`, and `Artifact Kind` as rigid backbone anchors.

### Phase 2.4: Carrier vs. Content Disentanglement
- **Action:** Audit all informational and representational classes (`Document`, `Book`, `Software`, `Image`, `Audio`).
- **Rule:** Explicitly separate the physical token / storage media (`Physical Body`) from the informational work / algorithm (`Informational Content`).

### Phase 2.5: Relation Normalization and Meta-Relation Isolation
- **Action:** Remove `Classification relation` and `Part-whole relation` from the domain `Relation` list.
- **Rule:** Re-establish `is-a` and `part-of` as typed structural edges in the graph schema. Require all remaining domain relations to declare explicit argument types (Domain and Range constraints).
