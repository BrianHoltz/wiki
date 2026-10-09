#!/usr/bin/env python3
"""Validate the proposal, full coverage, graph, formal levels, and biological ancestry.
Standard library only. Run: python3 validate.py [directory]
This checks explicit data invariants, not the truth or uniqueness of an ontology.
"""
import collections, hashlib, json, pathlib, sys
root=pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else pathlib.Path(__file__).resolve().parent
p=json.loads((root/'ontology-proposal.json').read_text())
c=json.loads((root/'coverage-map.json').read_text())
o=json.loads((root/'original-snapshot.json').read_text())
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append({'name':name,'status':'passed'})
check('Supported schema version',p['schema_version']=='1.0' and c['schema_version']=='1.0')
check('Every node is a class specification',all(n['node_kind']=='class' for n in p['nodes']))
nodes={n['id']:n for n in p['nodes']};expressions={e['id']:e for e in p['class_expressions']}
check('Unique class and expression IDs',len(nodes)==len(p['nodes']) and len(expressions)==len(p['class_expressions']) and not nodes.keys()&expressions.keys())
check('Unique canonical labels',len(set(n['label'] for n in nodes.values()))==len(nodes))
check('Complete nonempty definitions',all(isinstance(n['definition'],str) and n['definition'].strip() for n in list(nodes.values())+list(expressions.values())+p['predicate_instances']))
check('Stable class identifiers',all(n['id'] and n['id'].isascii() and n['id'].replace('_','').isalnum() for n in nodes.values()))
check('Exactly one Entity root',[n['id'] for n in nodes.values() if n['primary_parent'] is None]==['Entity'])
check('Every nonroot has one valid primary parent',all(n['primary_parent'] in nodes and n['primary_parent']!=n['id'] for n in nodes.values() if n['id']!='Entity'))
check('Every alternate superclass exists',all(a in nodes and a!=n['id'] and a!=n['primary_parent'] for n in nodes.values() for a in n['alternate_parents']))
check('No repeated alternate parents',all(len(n['alternate_parents'])==len(set(n['alternate_parents'])) for n in nodes.values()))
parents={i:([n['primary_parent']] if n['primary_parent'] else [])+n['alternate_parents'] for i,n in nodes.items()}
visited=set();stack=set()
def visit(i):
    if i in stack: raise AssertionError('Subclass cycle at '+i)
    if i in visited:return
    stack.add(i)
    for a in parents[i]:visit(a)
    stack.remove(i);visited.add(i)
for i in nodes:visit(i)
check('Combined canonical and alternate graph is acyclic',len(visited)==len(nodes))
def ancestors(i,all_edges=True):
    result=set();work=list(parents[i] if all_edges else ([nodes[i]['primary_parent']] if nodes[i]['primary_parent'] else []))
    while work:
        a=work.pop()
        if a in result:continue
        result.add(a);work.extend(parents[a] if all_edges else ([nodes[a]['primary_parent']] if nodes[a]['primary_parent'] else []))
    return result
check('Every class reaches Entity',all(i=='Entity' or 'Entity' in ancestors(i,False) for i in nodes))
def depth(i):return 0 if nodes[i]['primary_parent'] is None else 1+depth(nodes[i]['primary_parent'])
depths={i:depth(i) for i in nodes}
check('Canonical traversal stays at or below 13 edges',max(depths.values())<=13)
children=collections.defaultdict(list)
for i,n in nodes.items():
    if n['primary_parent']:children[n['primary_parent']].append(i)
check('Every sibling group has an explicit split policy',all('child_policy' in nodes[i] for i in children))
check('No unearned exhaustive or global disjoint partition axioms',all(n.get('child_policy',{}).get('coverage','selective')=='selective' for n in nodes.values()))
allowed_ops={'satisfies_specification','not_instance_of','instance_of','all_members_satisfy_specification','contextual_facet'}
for e in expressions.values():
    x=e['expression'];check('Expression entry exists: '+e['id'],e['canonical_entry'] in nodes)
    if x['op']=='class_reference':check('Expression class reference exists: '+e['id'],x['class'] in nodes);continue
    check('Expression base exists: '+e['id'],x['op']=='intersection' and x['base_class'] in nodes)
    for r in x['restrictions']:
        check('Supported expression operation: '+e['id'],r['op'] in allowed_ops)
        if 'class' in r:check('Restriction class exists: '+e['id'],r['class'] in nodes)
        if 'specification_class' in r:
            t=r['specification_class'];check('Restriction uses a unary specification class: '+e['id'],t in nodes and ('Property' in ancestors(t) or t=='Property'))
        if r['op']=='not_instance_of':check('Complement is relative to a superclass: '+e['id'],x['base_class'] in ancestors(r['class']))
original_ids={n['id'] for n in o['nodes']};mappings={m['original_id']:m for m in c['mappings']}
check('Exactly one mapping for every original record',len(mappings)==len(c['mappings']) and mappings.keys()==original_ids)
check('All mappings have explicit existing targets',all(m['targets'] and all(t in nodes or t in expressions for t in m['targets']) for m in mappings.values()))
check('Original labels and definitions retained',all(mappings[n['id']]['original_label']==n['label'] and mappings[n['id']]['legacy_definition']==n['definition'] for n in o['nodes']))
check('All original child edges retained for audit',all(mappings[n['id']]['source_children']==n['children'] for n in o['nodes']))
check('Coverage baseline is all 439 source records',len(original_ids)==439 and p['coverage_scope']['original_record_count']==439)
prids=[r['id'] for r in p['predicate_instances']]
check('Predicate instances use a separate unique namespace',len(prids)==len(set(prids)) and all(i.startswith('predicate:') for i in prids))
for r in p['predicate_instances']:
    a=ancestors(r['type_id']);is_relation='Relation' in a or r['type_id']=='Relation'
    check('Predicate type exists and has proper arity: '+r['id'],r['type_id'] in nodes and r['arity']==len(r['arguments']) and (r['arity']>=2 if is_relation else r['arity']==1))
    check('Predicate ranges are defined classes: '+r['id'],all(a['range'] in nodes for a in r['arguments']))
    check('Predicate formal level is explicit: '+r['id'],r['formal_level']=='predicate_instance')
biological_edges=[];bio_exceptions=[]
for i,n in nodes.items():
    b=n.get('biology',{})
    if b and not b.get('source_id'):bio_exceptions.append({'class':i,'reason':b['validation_scope']})
    if not b.get('source_id'):continue
    check('Retrieved taxon identity matches intended taxon: '+i,b['scientific_name']==b['expected_scientific_name'])
    lineage={a['id'] for a in b['source_lineage']}
    for a in parents[i]:
        ab=nodes[a].get('biology',{})
        if ab.get('source_id'):
            check('Retrieved taxonomic ancestry: '+i+' -> '+a,ab['source_id'] in lineage)
            biological_edges.append([i,a])
# Counterexample checks target actual known category mistakes rather than mere file consistency.
for name,condition in [
 ('Birds retain Dinosaur ancestry','Dinosaur' in ancestors('Bird')),
 ('Humans retain ape, tetrapod, and lobe-finned ancestry',{'Ape','Hominid','Tetrapod','LobeFinnedVertebrate','Mammal','Synapsid'}.issubset(ancestors('Human'))),
 ('Fungi do not inherit Land plant','Plant' not in ancestors('Fungus')),
 ('Viruses are not cellular organisms','Organism' not in ancestors('Virus')),
 ('Celestial bodies are not regions','Region' not in ancestors('AstronomicalBody')),
 ('Jurisdictional areas are not agents','AgentRole' not in ancestors('GeopoliticalArea') and 'Region' in ancestors('GeopoliticalArea')),
 ('Room and hole denote spaces',all('Region' in ancestors(i) and 'Artifact' not in ancestors(i) for i in ['Room','Hole'])),
 ('Language systems are not expressions','LinguisticExpression' not in ancestors('Language')),
 ('Film content is not Text','Text' not in ancestors('MotionPicture')),
 ('Molecules are not amounts of compound substance','CompoundSubstance' not in ancestors('Molecule')),
 ('Atoms are not elemental material portions','ElementalSubstance' not in ancestors('Atom')),
 ('Enzymatic classification does not force every enzyme to be protein','Protein' not in ancestors('Enzyme')),
 ('Personhood specifications do not become humans','Human' not in ancestors('Person')),
 ('Property and Relation are specification kinds',all('AbstractEntity' in ancestors(i) for i in ['Property','Relation'])),
 ('Actual qualities and relational states remain realized',all('RealizedEntity' in ancestors(i) for i in ['Quality','Relationship','ObligationInstance'])),
 ('Game rules and playing are separated','AbstractEntity' in ancestors('Game') and 'Process' in ancestors('Gaming')),
 ('Buying and selling are not forced disjoint',nodes['FinancialTransaction']['child_policy']['disjointness']=='overlapping'),
 ('Combustion is not forced to be decomposition','ChemicalDecomposition' not in ancestors('combust')),
 ('Birth does not imply creation of a previously nonexistent organism','Creation' not in ancestors('Birth')),
]:check(name,condition)
source_parents=collections.defaultdict(list)
for n in o['nodes']:
    for a in n['children']:source_parents[a].append(n['id'])
report={'status':'passed','scope':'Structural, coverage, formal-level, ancestry-data, and selected semantic-counterexample checks; not a proof of philosophical completeness, definition correctness, or logical consistency of all possible formalizations.','checks_passed':len(checks),'canonical_class_count':len(nodes),'canonical_edge_count':len(nodes)-1,'alternate_superclass_edge_count':sum(len(n['alternate_parents']) for n in nodes.values()),'defined_class_expression_count':len(expressions),'predicate_instance_count':len(prids),'original_record_count':len(original_ids),'mapped_original_record_count':len(mappings),'unmapped_original_records':[],'mapping_counts':dict(collections.Counter(m['mapping_kind'] for m in mappings.values())),'maximum_canonical_depth':max(depths.values()),'example_depths':{i:depths[i] for i in ['Organism','Human','Dog','Bird','Book','Corporation','Region','Circle']},'taxonomy_source_id_count':sum(bool(n.get('biology',{}).get('source_id')) for n in nodes.values()),'taxonomy_edges_checked':len(biological_edges),'taxonomy_editorial_exceptions':bio_exceptions,'source_actual_edge_count':sum(len(n['children']) for n in o['nodes']),'source_actual_multiple_parent_records':{i:a for i,a in source_parents.items() if len(a)>1},'checks':checks}
(root/'validation-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ['checks','source_actual_multiple_parent_records']},indent=2))
