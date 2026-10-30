"""Check whether the Wikipedia pages behind the catalog changed since the last time they were incorporated.

Usage:
  python scripts/check-wikipedia.py            show what changed on each page
  python scripts/check-wikipedia.py --record   store the current revision as incorporated

Run before each new release. Use --record only after the changes have been carried into
wikipedia/ and into the skill catalog.
"""
import json
import pathlib
import sys
import urllib.parse
import urllib.request

STATE = pathlib.Path(__file__).resolve().parent.parent / 'wikipedia/revisions.json'
PAGES = [
    ('en.wikipedia.org', 'Wikipedia:Signs of AI writing', 'en/signs-of-ai-writing.md'),
    ('pt.wikipedia.org', 'Wikipédia:Sinais de texto gerado por inteligência artificial', 'pt-br/sinais-de-texto-gerado-por-ia.md'),
    ('pt.wikipedia.org', 'Wikipédia:Grandes modelos de linguagem', 'pt-br/sinais-de-texto-gerado-por-ia.md'),
]
UA = {'User-Agent': 'humanizer-check-wikipedia/1.0'}


def api(host, **params):
    url = f'https://{host}/w/api.php?' + urllib.parse.urlencode({**params, 'format': 'json', 'formatversion': 2})
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
        return json.load(r)


def current_revision(host, title):
    p = api(host, action='query', prop='revisions', titles=title, rvprop='ids|timestamp')['query']['pages'][0]
    return p['revisions'][0]


def sections(host, revid):
    return [s['line'] for s in api(host, action='parse', oldid=revid, prop='sections')['parse']['sections']]


def main():
    record = '--record' in sys.argv
    state = json.loads(STATE.read_text(encoding='utf-8')) if STATE.exists() else {}
    changed = False
    for host, title, extract in PAGES:
        key = f'{host}/{title}'
        now = current_revision(host, title)
        before = state.get(key)
        if before and before['revid'] == now['revid']:
            print(f'no change    {title} (rev {now["revid"]})')
            continue
        changed = True
        new = sections(host, now['revid'])
        if before:
            print(f'CHANGED      {title}: rev {before["revid"]} ({before["timestamp"]}) -> {now["revid"]} ({now["timestamp"]})')
            print(f'  diff: https://{host}/w/index.php?diff={now["revid"]}&oldid={before["revid"]}')
            for s in new:
                if s not in before['sections']:
                    print(f'  + section: {s}')
            for s in before['sections']:
                if s not in new:
                    print(f'  - section: {s}')
        else:
            print(f'not recorded {title} (rev {now["revid"]})')
        print(f'  extract to update: wikipedia/{extract}')
        if record:
            state[key] = {'revid': now['revid'], 'timestamp': now['timestamp'], 'sections': new}
    if record:
        STATE.write_text(json.dumps(state, ensure_ascii=False, indent=1) + '\n', encoding='utf-8', newline='\n')
        print(f'recorded in {STATE}')
    elif changed:
        print('Carry the changes into the extract and the catalog, then run with --record.')


if __name__ == '__main__':
    main()
