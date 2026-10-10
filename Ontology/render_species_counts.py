#!/usr/bin/env python3
"""Build browser sidecars and linked evidence from taxon-species-counts.json.

Independent of ontology generators: rebuilding a tree preserves researched counts.
Existing files are rewritten in place so editor/file-watcher inodes stay live.
"""
import html
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATASETS = ['.', 'GPT', 'SUMO', 'HumanKnowledge', 'Propaedia', 'Rogets', 'Wikipedia']


def write(path, text):
    with path.open('w') as stream:
        stream.write(text)


def main():
    evidence = json.loads((ROOT / 'taxon-species-counts.json').read_text())
    records = evidence['records']
    for key, record in records.items():
        total = record.get('total')
        extinct, extant = record.get('extinct'), record.get('extant')
        for count in (total, extinct, extant):
            assert count is None or (type(count) is int and count >= 0), key
        assert not record.get('components'), key
        assert set(record.get('references', {})) == {
            kind for kind in ('total', 'extinct', 'extant') if record.get(kind) is not None
        }, key
        for kind, reference in record.get('references', {}).items():
            assert kind in ('total', 'extinct', 'extant'), (key, kind)
            assert record[kind] == reference['count'], (key, kind)
            assert reference['source'] in record['sources'], (key, kind)
        assert all(source in evidence['sources'] for source in record['sources']), key
    for dataset in DATASETS:
        nodes = json.loads((ROOT / dataset / 'ontology.json').read_text())['nodes']
        ids = {node['id'] for node in nodes}
        counts = {}
        prefix = '' if dataset == '.' else '../'
        for key, record in records.items():
            for mapping in record['mappings'].get(dataset, []):
                node = mapping['id']
                assert node in ids, (dataset, node)
                assert node not in counts, (dataset, node)
                total = record.get('total')
                extinct, extant = record.get('extinct'), record.get('extant')
                counts[node] = dict(
                    total=total, extinct=extinct, extant=extant,
                    taxon=record['taxon'], scope=record['scope'],
                    interpretation=mapping.get('interpretation', ''),
                    url=f'{prefix}taxon-species-counts.html#{key}',
                    retrieved=evidence['retrieved'],
                )
        write(ROOT / dataset / 'species-counts.json',
              json.dumps(counts, ensure_ascii=False, indent=2) + '\n')
        print(f'{dataset}: {len(counts)} species-count nodes')
    e = html.escape
    parts = ['<!doctype html><html lang="en"><meta charset="utf-8">',
             '<meta name="viewport" content="width=device-width,initial-scale=1">',
             '<title>Taxon species counts — sources and scope</title>',
             '<style>body{font:16px/1.5 system-ui;max-width:70em;margin:2em auto;padding:0 1em}'
             'article{border-top:1px solid #ccc;padding:1em 0;scroll-margin-top:1em}'
             'h2{margin:.3em 0}a{overflow-wrap:anywhere}dt{font-weight:600}dd{margin-bottom:.7em}</style>',
             '<h1>Taxon species counts</h1>',
             f'<p>Research retrieved {e(evidence["retrieved"])}. {e(evidence["policy"])}</p>',
             '<p>Tree numbers are compact, suggestive counts: a lone number is a total without a split; '
             '☠︎ follows extinct counts and ♥︎ follows extant counts, with extant last. '
             'Unavailable counts are omitted. Living/non-fossil checklist proxies can retain recently extinct species. '
             'Click a tree count for its reference taxon and method. Counts from independent sources '
             'need not agree or add up; source coverage and extinction periods differ.</p>',
             '<p><a href="taxon-species-counts.json">Authoritative research JSON</a></p>',
             '<h2>Sources</h2><dl>']
    for key, source in evidence['sources'].items():
        parts += [f'<dt id="source-{key}"><a href="{e(source["url"])}">{e(source["title"])}</a> — {e(source["date"])}</dt>',
                  f'<dd>{e(source["notes"])}</dd>']
        if source.get('download'):
            parts += [f'<dd><a href="{e(source["download"])}">Source dataset</a> '
                      + (f'— SHA-256 {e(source["sha256"])}' if source.get('sha256') else '') + '</dd>']
    parts += ['</dl><h2>Counts and mappings</h2>']
    for key, record in records.items():
        status = [f'{kind.capitalize()} reference count: {record[kind]:,}'
                  for kind in ('total', 'extinct', 'extant') if record.get(kind) is not None]
        parts += [f'<article id="{key}"><h2>{e(record["taxon"])}</h2>',
                  f'<p>{e("; ".join(status))}.</p><p>{e(record["scope"])}</p>',
                  f'<p>{e(record["method"])}</p>']
        for kind, reference in record.get('references', {}).items():
            parts += [f'<p>{e(kind.capitalize())}: <a href="{e(reference["url"])}">'
                      f'{e(reference["taxon"])}</a> — '
                      f'<a href="#source-{e(reference["source"])}">'
                      f'{e(evidence["sources"][reference["source"]]["title"])}</a>. '
                      f'{e(reference["method"])}</p>']
        parts += ['<p>Sources: ' + ', '.join(f'<a href="#source-{x}">{e(evidence["sources"][x]["title"])}</a>' for x in record['sources']) + '.</p>']
        if record.get('queries'):
            parts += ['<p>API evidence: ' + ', '.join(f'<a href="{e(url)}">{e(label)}</a>' for label, url in record['queries'].items()) + '.</p>']
        for dataset, mappings in record['mappings'].items():
            parts += ['<p>' + e(dataset + ': ' + ', '.join(m['id'] for m in mappings)) + '. '
                      + e(' '.join(m.get('interpretation', '') for m in mappings)) + '</p>']
        parts += ['</article>']
    if evidence['comparisons']:
        parts += ['<h2>Compared sources</h2><ul>']
    for item in evidence['comparisons']:
        parts += [f'<li><a href="{e(item["source"])}">{e(item["taxon"])}</a>: {item["count"]:,}. {e(item["scope"])}</li>']
    if evidence['comparisons']:
        parts += ['</ul>']
    parts += ['<h2>Unnumbered groupings</h2><ul>']
    for item in evidence['exclusions']:
        parts += [f'<li>{e(", ".join(item["datasets"]) + ": " + ", ".join(item["nodes"]))}. {e(item["reason"])}</li>']
    parts += ['</ul></html>\n']
    write(ROOT / 'taxon-species-counts.html', '\n'.join(parts))


if __name__ == '__main__':
    main()
    subprocess.run(['node', str(ROOT / 'test_browser.js')], check=True)
