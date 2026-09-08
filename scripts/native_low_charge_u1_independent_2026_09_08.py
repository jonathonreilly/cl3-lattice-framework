"""Portable original finite controls, with optimization-safe predicates."""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ('docs/NATIVE_LOW_CHARGE_U1_DICTIONARY_NOTE_2026-09-08.md', 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md', 'docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md', 'docs/THE_FERMIONS_U1_COUPLED_TO_QUANTUM_LINKS_GAUSS_LAW_AS_A_SUPPORT_CONDITION_AMONG_RECORDS_BOUNDED_THEOREM_NOTE_2026-09-03.md')
import argparse,time,signal,resource,sys,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
_started=time.monotonic()
if __name__ == '__main__':
    signal.alarm(AUDIT_TIMEOUT_SEC)
    _parser=argparse.ArgumentParser();_parser.add_argument('--json',action='store_true');_parser.parse_args()
_predicates=0
def require(value,message):
    global _predicates
    _predicates+=1
    if not value:raise RuntimeError(message)
import itertools, json, pathlib, time, signal, resource, sys
start = time.monotonic()
P = pathlib.Path(__file__).parent
checks = 0
oldfail = 0

def op(z, k, create):
    if bool(z >> k & 1) == create:
        return (None, 0)
    return (z ^ 1 << k, (-1) ** (z & (1 << k) - 1).bit_count())
for m in range(1, 9):
    for mask in range(1 << m):
        I = [i for i in range(m) if mask >> i & 1]
        z = (1 << m) - 1
        s = 1
        for i in reversed(I):
            z, t = op(z, i, False)
            s *= t
        require(z == (1 << m) - 1 ^ mask and s == (-1) ** sum(I), 'original assert line 12')
        oldfail += s != (-1) ** (sum(I) - len(I) * (len(I) - 1) // 2)
        checks += 1
coords = list(itertools.product(range(4), repeat=3))
label = {v: (13 * i + 7) % 64 for i, v in enumerate(coords)}
pos = {label[v]: v for v in coords}
eps = {i: (-1) ** sum(v) for i, v in pos.items()}
edges = set()
for v in coords:
    for a in range(3):
        w = list(v)
        w[a] = (w[a] + 1) % 4
        edges.add(tuple(sorted((label[v], label[tuple(w)]))))
edges = sorted(edges)
ei = {e: k for k, e in enumerate(edges)}
inc = {i: [] for i in range(64)}
for k, (i, j) in enumerate(edges):
    inc[i].append(k)
    inc[j].append(k)
order = {i: sorted(inc[i], key=lambda e: edges[e][0] if edges[e][1] == i else edges[e][1], reverse=bool(i % 2)) for i in inc}
w = []
M = []
for e, (i, j) in enumerate(edges):
    mask = 0
    for v in [i, j]:
        for f in order[v][:order[v].index(e)]:
            mask ^= 1 << f
    interval = 0
    for v in range(i, j):
        for f in inc[v]:
            interval ^= 1 << f
    w.append(mask)
    M.append(mask ^ interval)
for e in range(192):
    require(M[e] >> e & 1, 'original assert line 31')
    for f in range(e):
        require(M[e] >> f & 1 == M[f] >> e & 1, 'original assert line 32')

def charges(z):
    return [eps[v] * (sum((z >> e & 1 for e in inc[v])) - 3) for v in range(64)]

def phi(z, q):
    quad = sum(((z >> e & 1) * (M[e] & z & (1 << e) - 1).bit_count() for e in range(192)))
    I = [i for i, v in enumerate(q) if v]
    D = len(I)
    return (-z.bit_count() + 2 * (quad + sum(I) + D * (D - 1) // 2)) % 4

def fb(q):
    return sum((1 << 2 * i + (s < 0) for i, s in enumerate(q) if s))
seed = 0
for e, (i, j) in enumerate(edges):
    v = pos[i]
    z = pos[j]
    a = next((a for a in range(3) if v[a] != z[a]))
    origin = v if (v[a] + 1) % 4 == z[a] else z
    if origin[a] % 2:
        seed |= 1 << e
cases = {seed}
z = seed
used = set()
for e, (i, j) in enumerate(edges):
    if i not in used and j not in used:
        z ^= 1 << e
        used |= {i, j}
        cases.add(z)
        if len(used) == 16:
            break
for axes in [1, 2]:
    z = sum((1 << e for e, (i, j) in enumerate(edges) if next((a for a in range(3) if pos[i][a] != pos[j][a])) < axes))
    cases.add(z)
cases |= {z ^ (1 << 192) - 1 for z in list(cases)}
hops = rings = wrong = 0
Ds = set()
for z in cases:
    q = charges(z)
    require(max(map(abs, q)) <= 1 and sum(q) == 0, 'original assert line 52')
    Ds.add(sum((v * v for v in q)))
    base = phi(z, q)
    for e, (i, j) in enumerate(edges):
        Bi = (-1) ** sum((z >> f & 1 for f in inc[i]))
        Bj = (-1) ** sum((z >> f & 1 for f in inc[j]))
        if Bi == Bj:
            continue
        zz = z ^ 1 << e
        qq = charges(zz)
        if max(map(abs, qq)) > 1:
            continue
        src = i if q[i] else j
        dst = j if src == i else i
        s = q[src]
        f = fb(q)
        f, a = op(f, 2 * src + (s < 0), False)
        f, b = op(f, 2 * dst + (s < 0), True)
        require(f == fb(qq), 'original assert line 58')
        native = (1 + 2 * ((w[e] & z).bit_count() % 2) + (2 if Bi - Bj < 0 else 0)) % 4
        wanted = 0 if -a * b == 1 else 2
        require((native + phi(zz, qq) - base) % 4 == wanted, 'original assert line 61')
        wrong += (native + phi(zz, qq) - base) % 4 != (0 if a * b == 1 else 2)
        black = i if eps[i] == 1 else j
        require((zz >> e & 1) - (z >> e & 1) == (-s if src == black else s), 'original assert line 63')
        hops += 1
    for v in coords:
        for a, b in itertools.combinations(range(3), 2):
            va = list(v)
            vb = list(v)
            vab = list(v)
            va[a] = (va[a] + 1) % 4
            vb[b] = (vb[b] + 1) % 4
            vab[a] = (vab[a] + 1) % 4
            vab[b] = (vab[b] + 1) % 4
            C = [label[v], label[tuple(va)], label[tuple(vab)], label[tuple(vb)]]
            es = [ei[tuple(sorted((C[k], C[(k + 1) % 4])))] for k in range(4)]
            bits = [z >> e & 1 for e in es]
            if any((bits[k] == bits[(k + 1) % 4] for k in range(4))):
                continue
            zz = z
            phase = 0
            for k in reversed(range(4)):
                e = es[k]
                phase += 2 * ((w[e] & zz).bit_count() % 2) + 2 * (C[k] > C[(k + 1) % 4])
                zz ^= 1 << e
            qq = charges(zz)
            require(qq == q and (phase + phi(zz, qq) - base) % 4 == 0, 'original assert line 72')
            rings += 1
require(hops and rings and (wrong == hops) and oldfail, 'original assert line 73')
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1048576 if sys.platform == 'darwin' else 1024)
require(rss < 384, 'original assert line 75')
out = dict(hole_basis_subsets=checks, old_basis_formula_failures=oldfail, relabeled_native_configurations=len(cases), D_sectors=sorted(Ds), native_hop_columns=hops, ring_columns=rings, missing_minus_failures=wrong, seconds=time.monotonic() - start, rss_mib=rss, scope='finite different-order native controls; no full global census')

_elapsed=time.monotonic()-_started
_rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
require(_elapsed<180 and 0<_rss<384,'portable resources')
out['executed_predicates']=_predicates
out['portable_seconds']=_elapsed
out['portable_rss_mib']=_rss
print(json.dumps(out,indent=2,allow_nan=False))
