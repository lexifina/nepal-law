"""The Law Commission English act PDFs (old /en/ site, Internet Archive) whose act is in the Commission's current
alphabetical index of acts in force (lawcommission.gov.np/pages/alphabetical-index-of-acts/, Nepali), matched by hand
by name and Bikram Sambat year. Writes .work/selected.json: [{key, file, url, ts}]. Reads only .work/en_pdfs.json."""
import json, re
from pathlib import Path
H = Path(__file__).parent
# English file stem | matched entry of the current Nepali index (kept for the record)
IN_FORCE = (H / 'in_force.txt').read_text('utf-8')


def rows():
    for ln in IN_FORCE.strip().splitlines():
        en, _, np = ln.partition(' | ')
        yield en.strip(), np.strip()


def main():
    d = json.loads((H / '.work' / 'en_pdfs.json').read_text())
    out, miss, seen = [], [], set()
    for en, np in rows():
        caps = [(k, r) for k, v in d.items() if k.split('/')[-1][:-4] == en for r in v]
        if not caps:
            miss.append(en)
            continue
        caps.sort(key=lambda kr: kr[1]['timestamp'])
        k, r = caps[-1]   # the latest capture of the file
        key = re.sub(r'^the-', '', re.sub(r'-final-eng-version.*$', '', en)).strip('-')
        key = re.sub(r'-(\d{4})-?(\d{4})$', r'-\1-\2', key)
        assert key not in seen, key
        seen.add(key)
        out.append({'key': key, 'file': en, 'np_index': np, 'url': r['original'], 'ts': r['timestamp'],
                    'digest': r['digest']})
    (H / '.work' / 'selected.json').write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')
    print(len(out), 'selected; missing', miss)


if __name__ == '__main__':
    main()
