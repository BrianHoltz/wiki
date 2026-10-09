# Category-mistake and interpretation stress tests

These cases explain how the proposal is intended to be used. They are not claims that its English definitions constitute a complete axiomatization. Counts and executable checks are in `validation-report.json`.

| Case | Canonical classification | Separate specification, facet, or relationship |
|---|---|---|
| A rock | Rock → Geological body → Material body → Item | Naturalness and abiotic origin can be recorded as qualifications. A rock used to hammer satisfies an instrument role; it does not thereby become a designed Tool. |
| A dog | Domestic dog → Canid → Carnivoran → Eutherian mammal | Diet, habitat, and domestic use do not determine ancestry. Carnivoran does not entail dietary carnivore. |
| A human | Human → Ape → Primate → Mammal | Great-ape, eutherian, synapsid, tetrapod, and lobe-finned ancestry remains in alternate edges or full source lineage. Personhood and agency are separate qualifications. |
| A corporation | Corporation → Organization → Social group | Corporate personhood is a legal qualification. Charter content is normative content; a corporate office is a separate social object. |
| A wedding occurrence | Event → Process, with social-interaction classification where justified | Its record, invitation, commitments, and continuing marital relationship are different entities. |
| An apple's ripening | Biological development → Organism-level process | Its duration is represented through temporal relations; the process is not its resulting color quality. |
| A spacetime extent | Spacetime region → Region | Coordinates or mathematical models representing it are abstract. No universal present is required. |
| Redness | Quality property specification → Descriptive property specification | This apple's particular color is a Quality instance. Its color value is a Quality value. `predicate:is_red` is an instance of a unary specification class. |
| Greater-than | Relation specification, specialized mathematically | `predicate:quantity_greater_than` has two values and an explicit compatible-scale context. A relation's arity can itself be described without identifying its specification with an ordinary argument. |
| A number | Number → Mathematical entity | A numeral is representational content or a token. A number of kilograms is a Quantity value, not just the number. |
| A singleton set | Set → Mathematical entity | The member may be a flock. One-member cardinality does not make the flock a single Item. A realized flock is an Organism aggregate. |
| A proposition | Proposition → Information content | A sentence expresses it; a belief state accepts it; a true proposition is Fact under an interpretation. A worldly state is a State instance. |
| A proof | Proof → Representational content | The theorem proved is a proposition. Checking the proof is a process; its mathematical structures are not identical to the proof text. |
| An algorithm | Algorithm → Computational structure | The same algorithm can have different code representations, storage tokens, and execution occurrences. |
| A printed book | Printed book → Manufactured information carrier | The book's content is Book content → Text content; copies can realize the same content. A digital token need not be a manufactured physical carrier. |
| A currency | Currency system → Social object | Its unit is a Measurement unit; a note or digital denomination token is a Monetary token. A particular debt or account requires a separate claim record, not a currency-system instance. |
| A fictional character | Fictional entity description → Description | The actual description and its narrative context have homes. The portrayed human is not asserted to be an actual Human without an explicit world-indexed interpretation. |
| A virus | Virus → Acellular infectious entity → Biotic object | This does not assert cellular organism status or a single clade uniting all viruses. Host, genome, and transmission remain dimensions for refinement. |
| A lake | Water area → Geographic area → Spatial region | The water amount is a material portion; salinity and flow are cross-cutting classifications of the extent or its relevant water. |
| A seed, fruit, and fruit salad | Reproductive body; Botanical fruit; Prepared food portion | Botanical fruit anatomy, fruit food use, and a processed mixture remain distinct. Some fruits are vegetables in a culinary context without changing ancestry. |
| A borrowed hammer | A hammer is a Tool; the lending occurrence is a possession transfer | Borrowing and lending are two participant perspectives on an occurrence. Neither entails ownership transfer. Buying and selling likewise need not be disjoint event types. |
| A peptide hormone or RNA catalyst | Appropriate material portion or molecular body | Hormone and Enzyme specifications classify function in context. Enzyme does not universally imply Protein. |
| A coal sample or saline water | Geological material portion; water-dominated Mixture | The source's broad Mineral and Water senses are explicitly mapped; they are not silently restricted to mineral species or pure H2O. |

## What is mechanically checked

The executable validator checks 439/439 source mappings, all class and expression definitions, unique IDs and labels, one canonical parent per nonroot, Entity reachability, no cycle even after alternate superclasses, expression references, specification/bearer separation in expression typing, predicate arities/ranges, split-policy presence, canonical depth, intended taxon names, and retrieved ancestry links. Named negative assertions catch the former fungus/plant, virus/organism, film/text, language/expression, molecule/material-portion, region/agent, and enzyme/protein category mistakes.

Additional mutation tests deliberately introduce a cycle, missing definition, dangling parent, missing source mapping, wrong predicate arity, and mismatched taxon identity. Each must be rejected. This verifies that the validator can detect defects, not merely accept the delivered file.

## What needs interpretive review

An automated check does not establish that a definition is essential, that two classes are globally disjoint, or that a particular organization, belief, or fictional referent has the best identity criterion. It does not resolve competing phylogenetic authorities, deep microbial topology, or all fossil placements. Operational facets explicitly identify where a scale, recipient, topology, dietary threshold, or social criterion must be supplied. These are open semantic commitments rather than missing tree records.
