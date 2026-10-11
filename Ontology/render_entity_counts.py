#!/usr/bin/env python3
"""Publish sourced entity-count sidecars and evidence into all shared tree browsers.

Graphs stay authoritative and unchanged. Existing files are rewritten in place.
"""
import html
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATASETS = ['.', 'GPT', 'SUMO', 'HumanKnowledge', 'Propaedia', 'Rogets', 'Wikipedia']

# Keep this addition in the shared browser and its generated projections.
UI = r'''// Entity counts: scoped populations, catalogue totals and cardinalities.
function formatEntityCount(s){
const parts=[];
if(s.extinctDisplay)parts.push(`${s.extinctDisplay}☠︎`);
if(s.extantDisplay)parts.push(`${s.extantDisplay}♥︎`);
return parts.length?parts.join('+')+(s.countLabel?` ${s.countLabel}`:''):s.display;
}
function entityStats(n){return (n.entityCounts||[]).map(s=>{
const title=[s.scope,s.interpretation,s.retrieved?`Sources checked ${s.retrieved}`:''].filter(Boolean).join(' ');
return `<a class="entity-count" href="${esc(s.url)}" title="${esc(title)}" aria-label="${esc(`${n.label}: ${formatEntityCount(s)}. ${title}`)}" target="_blank" rel="noopener">${esc(formatEntityCount(s))}</a>`;
}).join(' · ')}
// End entity counts.
'''


def write(path, text):
    before = path.read_text() if path.exists() else None
    if before != text:
        with path.open('w') as stream:
            stream.write(text)


def plain(markdown):
    return re.sub(r'\[([^]]+)\]\((?:https?://[^\s]+|[^()\s]+)\)', r'\1', markdown).replace('**', '')


def update_browser(path):
    source = path.read_text()
    if '// Entity counts: ' in source:
        source = re.sub(r'// Entity counts: [\s\S]*?// End entity counts\.\n', lambda _: UI, source, count=1)
    else:
        assert source.count('function renderNode(') == 1, path
        source = source.replace('function renderNode(', UI + 'function renderNode(', 1)
        old = "const species=speciesStats(n);const childrenStats="
        assert old in source, path
        source = source.replace(old, "const species=[speciesStats(n),entityStats(n)].filter(Boolean).join(' · ');const childrenStats=", 1)
        old = "['ontology.json','species-counts.json']"
        assert old in source, path
        source = source.replace(old, "['ontology.json','species-counts.json','entity-counts.json']", 1)
        source = source.replace('then(([x,counts])=>', 'then(([x,counts,entities])=>', 1)
        source = source.replace('n.speciesCount=counts[n.id]||null', 'n.speciesCount=counts[n.id]||null;n.entityCounts=entities[n.id]||[]', 1)
        source = source.replace('Could not load ontology or species counts:', 'Could not load ontology or reference counts:', 1)
        source = source.replace('.species-count{', '.entity-count,.species-count{', 1)
        source = source.replace('.species-count:hover{', '.entity-count:hover,.species-count:hover{', 1)
    write(path, source)


def main():
    evidence = json.loads((ROOT / 'entity-count-references.json').read_text())
    records = evidence['records']
    all_mappings = []
    for dataset in DATASETS:
        nodes = json.loads((ROOT / dataset / 'ontology.json').read_text())['nodes']
        by_id = {n['id']: n for n in nodes}
        counts = {}
        prefix = '' if dataset == '.' else '../'
        for key, record in records.items():
            assert record['sources'], key
            for mapping in record['mappings'].get(dataset, []):
                node = mapping['id']
                assert node in by_id, (dataset, node)
                item = dict(record=key, display=mapping.get('display', record['display']),
                            scope=plain(record['claim']), interpretation=mapping.get('interpretation', ''),
                            url=f'{prefix}entity-counts.html#{key}', retrieved=evidence['retrieved'])
                for name in ['extinctDisplay', 'extantDisplay', 'countLabel']:
                    if name in record:
                        item[name] = record[name]
                assert not any(v['record'] == key for v in counts.get(node, [])), (dataset, node, key)
                counts.setdefault(node, []).append(item)
                all_mappings.append((dataset, node, key))
        write(ROOT / dataset / 'entity-counts.json', json.dumps(counts, ensure_ascii=False, indent=2) + '\n')
        update_browser(ROOT / dataset / 'index.html')
        print(f'{dataset}: {len(counts)} nodes, {sum(map(len, counts.values()))} entity-count annotations')
    e = html.escape
    parts = ['<!doctype html><html lang="en"><meta charset="utf-8">',
             '<meta name="viewport" content="width=device-width,initial-scale=1">',
             '<title>Entity counts — sources and scope</title>',
             '<style>body{font:16px/1.5 system-ui;max-width:65em;margin:2em auto;padding:0 1em}'
             'article{border-top:1px solid #ccc;padding:1em 0;scroll-margin-top:1em}'
             'a{overflow-wrap:anywhere}h2{margin:.3em 0}</style>',
             '<h1>Entity counts</h1>', f'<p>{e(evidence["policy"])}</p>',
             '<p>ℵ₀: countably infinite. 𝔠 = 2<sup>ℵ₀</sup>: uncountably infinite, the cardinality of the continuum; '
             '𝔠 is not assumed to equal ℵ₁. ☠︎ follows supported extinct counts and ♥︎ follows extant counts, '
             'with extant last. Missing splits are omitted, never treated as zero.</p>',
             f'<p>Sources checked {e(evidence["retrieved"])}. '
             '<a href="Ontology.md#entity-counts">Project reference</a> · '
             '<a href="entity-count-references.json">Counts and reviewed mappings</a> · '
             '<a href="taxon-species-counts.html">Biological species counts</a></p>']
    for key, record in records.items():
        parts += [f'<article id="{e(key)}"><h2>{e(key.replace("-", " ").capitalize())}</h2>',
                  f'<p>{e(plain(record["claim"]))}</p>',
                  '<p>Sources: ' + ' · '.join(f'<a href="{e(url)}">{e(url.split("/")[2])}</a>' for url in record['sources']) + '.</p>']
        for dataset, mappings in record['mappings'].items():
            href = 'index.html' if dataset == '.' else f'{dataset}/index.html'
            links = ' · '.join(f'<a href="{e(href)}#{e(m["id"])}">{e(m["id"])}</a>' for m in mappings)
            parts.append(f'<p>{e(dataset)}: {links}</p>')
            for mapping in mappings:
                if mapping.get('interpretation'):
                    parts.append(f'<p>{e(mapping["id"])}: {e(mapping["interpretation"])}</p>')
        if not record['mappings']:
            parts.append('<p>No matching entry exists in the published trees; the count remains available here.</p>')
        if record.get('unmapped_detail'):
            parts.append(f'<p>{e(record["unmapped_detail"])}</p>')
        parts.append('</article>')
    parts.append('</html>\n')
    write(ROOT / 'entity-counts.html', '\n'.join(parts))
    assert all_mappings


if __name__ == '__main__':
    main()
    subprocess.run(['node', str(ROOT / 'test_browser.js')], check=True)
