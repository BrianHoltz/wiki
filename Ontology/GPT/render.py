#!/usr/bin/env python3
"""Render authoritative JSON to readable Markdown. Standard library only."""
import collections,json,pathlib,sys
root=pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else pathlib.Path(__file__).resolve().parent
p=json.loads((root/'ontology-proposal.json').read_text()); by={n['id']:n for n in p['nodes']}
fby={n['id']:n for n in p['class_expressions']}; children=collections.defaultdict(list)
for n in p['nodes']:
    if n['primary_parent']:children[n['primary_parent']].append(n['id'])
lines=['# Proposed ontology — complete canonical tree','',f"{len(by)} defined classes. Every indented edge means **is a subclass of**. One primary parent per nonroot; additional superclass edges and role-qualified expressions appear below. JSON is authoritative.",'','Sibling lists are **selective**, not declarations of exhaustiveness or disjointness. A specification and the entity satisfying it are distinct: “Food specification” classifies unary specifications; actual food portions use a qualified bearer expression.','', '## Canonical tree','']
def walk(i,d):
    n=by[i];lines.append('    '*d+f'- <a id="{i}"></a>**{n["label"]}** — {n["definition"]} `{i}`')
    for c in children[i]:walk(c,d+1)
walk(p['root'],0)
lines+=['','## Additional valid superclass edges','','These are semantic subclass links, not use, location, part-whole, or provenance relations.','', '| Class | Additional superclass |','|---|---|']
for n in p['nodes']:
    for a in n['alternate_parents']:lines.append(f'| [{n["label"]}](#{n["id"]}) | [{by[a]["label"]}](#{a}) |')
lines+=['','## Cross-cutting class expressions','','These remain defined and searchable without dictating the primary kind hierarchy. `satisfies_specification` means the bearer satisfies some instance of the named specification class in the relevant context; the bearer is not itself a specification. Operational facets need the stated domain criterion.','', '| ID and label | Definition | Expression | Canonical entry |','|---|---|---|---|']
for f in p['class_expressions']:
    expression=json.dumps(f['expression'],ensure_ascii=False,separators=(',',':')).replace('|','&#124;')
    lines.append(f'| `{f["id"]}` **{f["label"]}** | {f["definition"]} | `{expression}` | [{by[f["canonical_entry"]]["label"]}](#{f["canonical_entry"]}) |')
lines+=['','## Typed predicate examples','','These are predicate instances classified by the specification classes above. They are not extra class-tree nodes. Context arguments count toward arity.','', '| Predicate | Typed arguments | Meaning |','|---|---|---|']
for r in p['predicate_instances']:
    args=', '.join(a['name']+': '+a['range'] for a in r['arguments'])
    lines.append(f'| `{r["id"]}` | {args} | {r["definition"]} |')
lines+=['','## Split policies','','All child groups are selective. The following notes expose the axis and any expected overlap.','', '| Parent | Axis | Disjointness | Note |','|---|---|---|---|']
for n in p['nodes']:
    if 'child_policy' in n:
        s=n['child_policy'];lines.append(f'| [{n["label"]}](#{n["id"]}) | {s["axis"]} | {s["disjointness"]} | {s["note"]} |')
lines+=['','## Editorial and ambiguity notes','']
for n in p['nodes']:
    if n.get('notes'):lines.append(f'- **[{n["label"]}](#{n["id"]})**: '+ ' '.join(n['notes']))
lines+=['','Full source identifiers, retrieved biological lineages, aliases, formalization constraints, and coverage scope are retained in [ontology-proposal.json](ontology-proposal.json).','']
(root/'ontology-tree.md').write_text('\n'.join(lines))
c=json.loads((root/'coverage-map.json').read_text())
lines=['# Complete original-to-proposal coverage map','',f"All {len(c['mappings'])} original records are accounted for. This measures explicit **concept accounting**, not 439 exact synonym matches. Definitions and questionable source placements are intentionally revised.",'', '**Revised** retains the intended core kind with reviewed wording and placement. **Disambiguated** separates conflated senses or identity criteria; some target classes are broader routes requiring a contextual facet. **Faceted** preserves a cross-cutting class expression outside the canonical hierarchy. **Merged alias** repairs duplicate spellings or typography.','', 'Targets named as specifications classify predicates, not their ordinary bearers. `facet:` targets preserve bearer classifications. Broad destinations such as Process or Region do not claim extensional equivalence.','', '| Original ID / label | Treatment | Proposed replacements | Reason |','|---|---|---|---|']
for m in c['mappings']:
    refs=[]
    for t in m['targets']:
        if t in by:refs.append(f'[{by[t]["label"]}](ontology-tree.md#{t}) (`{t}`)')
        else:refs.append(f'{fby[t]["label"]} (`{t}`)')
    lines.append(f'| `{m["original_id"]}` — {m["original_label"]} | {m["mapping_kind"]} | '+ '; '.join(refs)+' | '+m['note'].replace('|','&#124;')+' |')
lines+=['','Original definitions and all child edges are preserved in [coverage-map.json](coverage-map.json) and the unmodified-data [original-snapshot.json](original-snapshot.json).','']
(root/'coverage-map.md').write_text('\n'.join(lines))
print('Rendered complete tree and all original-node mappings.')
