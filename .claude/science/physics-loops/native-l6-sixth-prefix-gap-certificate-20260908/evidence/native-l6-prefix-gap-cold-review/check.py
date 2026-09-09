from pathlib import Path
from itertools import product, combinations
from fractions import Fraction as F
from math import isqrt
import json, signal, time, hashlib
signal.alarm(180)
start = time.monotonic()
B = Path(__file__).parent
P = B.parent / 'native-l6-prefix-gap-probe'
c = json.loads((P / 'CENSUS.json').read_text())
vs = list(product(range(6), repeat=3))
idx = {v: i for i, v in enumerate(vs)}
edges = []
for v in vs:
    for a in range(3):
        w = list(v)
        w[a] = (w[a] + 1) % 6
        edges.append(tuple(sorted((idx[v], idx[tuple(w)]))))
if not edges == list(map(tuple, c['edges'])):
    raise ValueError('independent predicate line 10')
bd = set(c['boundary'])
allm = set()
keys = 0
for row in c['rows']:
    e = row['bridge']
    terms = [(a, b) for a, b in combinations(sorted(bd | {e}), 2) if set(edges[a]) & set(edges[b])]
    layer = {(0, 0): 1}
    found = set()
    for k in range(1, 7):
        nxt = {}
        for (used, bc), count in layer.items():
            for a, b in terms:
                fresh = [x for x in (a, b) if x != e]
                nb = bc + int(a == e) + int(b == e)
                if nb > 2 or any((used >> x & 1 for x in fresh)):
                    continue
                u = used | sum((1 << x for x in fresh))
                nxt[u, nb] = nxt.get((u, nb), 0) + count
        layer = nxt
        if k < 6:
            for u, bc in layer:
                found.add((k, u, bc, u ^ bc % 2 << e))
    from functools import lru_cache
    @lru_cache(None)
    def completes(used, bc):
        if used == sum(1 << x for x in bd) and bc == 2: return True
        for a,b in terms:
            fresh=[x for x in (a,b) if x!=e]; nb=bc+int(a==e)+int(b==e)
            if nb<=2 and not any(used>>x&1 for x in fresh) and completes(used|sum(1<<x for x in fresh),nb): return True
        return False
    found={x for x in found if completes(x[1],x[2])}
    if not found == {(r['k'], int(r['used']), r['bridge_count'], int(r['mask'])) for r in row['prefixes']}:
        raise ValueError('independent predicate line 24')
    if not layer[sum((1 << x for x in bd)), 2] == row['matchings'] * 720:
        raise ValueError('independent predicate line 25')
    keys += len(found)
    allm.update((x[3] for x in found))
if not (keys == 2038 and len(allm) == 1534):
    raise ValueError('independent predicate line 27')
mask = int(c['rows'][0]['prefixes'][0]['mask'])
black = [i for i, v in enumerate(vs) if sum(v) % 2 == 0]
white = [i for i in range(216) if i not in black]
bi = {v: i for i, v in enumerate(black)}
wi = {v: i for i, v in enumerate(white)}
M = [[0] * 108 for _ in black]
for e, (i, j) in enumerate(edges):
    value = -(-1) ** sum(vs[e // 3][:e % 3])
    a, b = (i, j) if i in bi else (j, i)
    M[bi[a]][wi[b]] = (value if i in bi else -value) * (-1 if mask >> e & 1 else 1)
A = [[F(sum((x * y for x, y in zip(M[i], M[j])))) + F(25, 4) * (i == j) for j in range(108)] for i in range(108)]
L = [[F(int(i == j)) for j in range(108)] for i in range(108)]
D = []
for j in range(108):
    d = A[j][j] - sum((L[j][k] ** 2 * D[k] for k in range(j)))
    if not d > 0:
        raise ValueError('independent predicate line 34')
    D.append(d)
    for i in range(j + 1, 108):
        L[i][j] = (A[i][j] - sum((L[i][k] * L[j][k] * D[k] for k in range(j)))) / d
inv = [[F(int(i == j)) for j in range(108)] for i in range(108)]
for i in range(108):
    for j in range(i):
        inv[i][j] = -sum((L[i][k] * inv[k][j] for k in range(j, i)))
trace = sum((sum((x * x for x in r)) / d for r, d in zip(inv, D)))
lower = lambda n: F(isqrt(n * 10 ** 60), 10 ** 30)
gap = 72 + 40 * lower(3) + 48 * lower(6) - F(1323, 10) - F(5, 2) * (108 - F(25, 4) * trace)
pilot = json.loads((P / 'PILOT_RESULT.json').read_text())
if not gap == F(next((x['gap_lower'] for x in pilot['rows'] if int(x['mask']) == mask))):
    raise ValueError('independent predicate line 40')
(B / 'RESULT.json').write_text(json.dumps(dict(keys=keys, masks=len(allm), pilot_mask=str(mask), gap=str(gap), seconds=time.monotonic() - start, scope='independent census and one fixed full LDL inverse; no all-gap scan'), indent=2) + '\n')
print('PASS', time.monotonic() - start)
