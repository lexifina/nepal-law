"""Independent check of a corpus.d part against its PDF: every character of the act's text layer (from the preamble
to the end, less page furniture, chapter headings and bare section numbers) must equal the units' text in order,
ignoring whitespace and colons. Usage: python -X utf8 verify_en_act.py <part.json> <pdf>"""
import json, re, sys
import fitz

part = json.load(open(sys.argv[1], encoding='utf-8'))
src = '\n'.join(p.get_text() for p in fitz.open(sys.argv[2]))
src = (src.replace('\xa0', ' ').replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
       .replace('–', '-').replace('—', '-').replace('', '').replace('​', ''))
L = [l.strip() for l in src.split('\n')]
L = [l for l in L if l and l != 'www.lawcommission.gov.np' and not re.fullmatch(r'\d{1,3}', l)]
i0 = next(i for i, l in enumerate(L) if l.startswith('Preamble'))
out, skip, nxt = [], 0, 1
for l in L[i0:]:
    if re.fullmatch(r'Chapter- ?\d+', l):
        skip = True
        continue
    if skip and l != f'{nxt}.':
        continue
    skip = False
    if l == f'{nxt}.':
        nxt += 1
        continue
    out.append(l)
S = re.sub(r'[\s:]', '', ''.join(out))[len('Preamble'):]
units = part['acts'][0]['versions'][0]['units']
U = ''
for k, u in units.items():
    t = re.sub(r'^# (Preamble|Sec\. \d+\.)', '', u['text'])
    U += re.sub(r'[\s:]', '', t)
if S == U:
    print('OK', len(units), 'units,', len(S), 'characters identical')
    sys.exit(0)
n = next((i for i in range(min(len(S), len(U))) if S[i] != U[i]), min(len(S), len(U)))
print('MISMATCH at', n, 'of', len(S), len(U))
print('src :', S[max(0, n - 80):n + 80])
print('unit:', U[max(0, n - 80):n + 80])
sys.exit(1)
