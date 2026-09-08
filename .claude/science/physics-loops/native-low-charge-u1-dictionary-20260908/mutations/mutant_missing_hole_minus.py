"""Portable original finite controls, with optimization-safe predicates."""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ('docs/NATIVE_LOW_CHARGE_U1_DICTIONARY_NOTE_2026-09-08.md', 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md', 'docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md', 'docs/THE_FERMIONS_U1_COUPLED_TO_QUANTUM_LINKS_GAUSS_LAW_AS_A_SUPPORT_CONDITION_AMONG_RECORDS_BOUNDED_THEOREM_NOTE_2026-09-03.md', '.claude/science/physics-loops/native-low-charge-u1-dictionary-20260908/inputs/GLOBAL_D4_SEED.json')
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
import time, signal, resource, sys, pathlib, json, itertools, hashlib
start = time.monotonic()
O = pathlib.Path(__file__).parent
vs = list(itertools.product(range(4), repeat=3))
ids = {v: i for i, v in enumerate(vs)}
edges = set()
for v in vs:
    for a in range(3):
        w = list(v)
        w[a] = (w[a] + 1) % 4
        edges.add(tuple(sorted((ids[v], ids[tuple(w)]))))
edges = sorted(edges)
ei = {e: i for i, e in enumerate(edges)}
inc = [[e for e, (u, v) in enumerate(edges) if i in (u, v)] for i in range(64)]
eps = [(-1) ** sum(v) for v in vs]
w = []
M = []
for e, (i, j) in enumerate(edges):
    mask = 0
    for a, b in ((i, j), (j, i)):
        for f in inc[a]:
            nb = edges[f][0] if edges[f][1] == a else edges[f][1]
            if nb < b:
                mask ^= 1 << f
    w.append(mask)
    mm = mask
    for v in range(i, j):
        for f in inc[v]:
            mm ^= 1 << f
    M.append(mm)

def data(z):
    deg = [sum((z >> e & 1 for e in row)) for row in inc]
    q = [eps[i] * (d - 3) for i, d in enumerate(deg)]
    return (deg, q)

def phase(z, q):
    d = (-z.bit_count() + 2 * sum(((z >> e & 1) * ((M[e] & z) >> e + 1).bit_count() for e in range(192)))) % 4
    holes = [i for i, qv in enumerate(q) if qv]
    s = (sum(holes) - len(holes) * (len(holes) - 1) // 2) % 2
    return (d + 2 * s) % 4

def species(q):
    return sum((1 << 2 * i + (qv == -1) for i, qv in enumerate(q) if qv))

def act(b, i, create):
    if bool(b >> i & 1) == create:
        return (None, 0)
    return (b ^ 1 << i, (b & (1 << i) - 1).bit_count() % 2)
seed = 0
for e, (i, j) in enumerate(edges):
    a = next((a for a in range(3) if vs[i][a] != vs[j][a]))
    origin = i if (vs[i][a] + 1) % 4 == vs[j][a] else j
    if vs[origin][a] % 2:
        seed |= 1 << e
cases = {seed}
used = set()
z = seed
for e, (i, j) in enumerate(edges):
    if i not in used and j not in used:
        used |= {i, j}
        z ^= 1 << e
        cases.add(z)
        if len(used) == 16:
            break
for axiscount in (1, 2):
    z = 0
    for e, (i, j) in enumerate(edges):
        a = next((a for a in range(3) if vs[i][a] != vs[j][a]))
        if a < axiscount:
            z |= 1 << e
    cases.add(z)
cases |= {z ^ (1 << 192) - 1 for z in list(cases)}
rawpath = ROOT / '.claude/science/physics-loops/native-low-charge-u1-dictionary-20260908/inputs/GLOBAL_D4_SEED.json'
raw = json.loads(rawpath.read_text())
cases |= {int(r['initial_bits'], 2) for r in raw['witnesses']}
checks = 0
hops = 0
rings = 0
sectors = set()
wrong_sign = 0
faces = []
for v in vs:
    for a, b in itertools.combinations(range(3), 2):
        va = list(v)
        vb = list(v)
        vab = list(v)
        va[a] = (va[a] + 1) % 4
        vb[b] = (vb[b] + 1) % 4
        vab[a] = (vab[a] + 1) % 4
        vab[b] = (vab[b] + 1) % 4
        cycle = [ids[v], ids[tuple(va)], ids[tuple(vab)], ids[tuple(vb)]]
        faces.append(cycle)
for z in cases:
    deg, q = data(z)
    require(not (max(map(abs, q)) > 1 or sum(q) != 0), 'original guard line 55')
    sectors.add(sum((v * v for v in q)))
    f = species(q)
    up = phase(z, q)
    for e, (i, j) in enumerate(edges):
        Bi = (-1) ** deg[i]
        Bj = (-1) ** deg[j]
        if Bi == Bj:
            continue
        zz = z ^ 1 << e
        dg, qq = data(zz)
        if max(map(abs, qq)) > 1:
            continue
        src = i if q[i] else j
        dst = j if src == i else i
        s = q[src]
        black = i if eps[i] == 1 else j
        forward = src == black
        delta = (zz >> e & 1) - (z >> e & 1)
        require(not delta != (-s if forward else s), 'original guard line 65')
        ff, a = act(f, 2 * src + (s == -1), False)
        ff, b = act(ff, 2 * dst + (s == -1), True)
        require(not ff != species(qq), 'original guard line 67')
        native = (1 + 2 * ((w[e] & z).bit_count() % 2) + (2 if Bi - Bj < 0 else 0)) % 4
        candidate = (2 * (a + b)) % 4
        require(not (native + phase(zz, qq) - up) % 4 != candidate, 'original guard line 70')
        if (native + phase(zz, qq) - up) % 4 != 2 * (a + b) % 4:
            wrong_sign += 1
        hops += 1
    for cycle in faces:
        fs = [ei[tuple(sorted((cycle[k], cycle[(k + 1) % 4])))] for k in range(4)]
        bits = [z >> e & 1 for e in fs]
        if any((bits[k] == bits[(k + 1) % 4] for k in range(4))):
            continue
        zz = z
        native = 0
        for k in reversed(range(4)):
            i, j = (cycle[k], cycle[(k + 1) % 4])
            e = fs[k]
            native += 2 * ((w[e] & zz).bit_count() % 2) + 2 * (i > j)
            zz ^= 1 << e
        dg, qq = data(zz)
        require(not (qq != q or (native + phase(zz, qq) - up) % 4 != 0), 'original guard line 81')
        rings += 1
local = 0
for q in itertools.product((0, 1, -1), repeat=6):
    h = sum((1 << i for i, v in enumerate(q) if v))
    f = species(q)
    for i, j in itertools.permutations(range(6), 2):
        if not q[i] or q[j]:
            continue
        hh, a = act(h, i, False)
        hh, b = act(hh, j, True)
        ff, c = act(f, 2 * i + (q[i] == -1), False)
        ff, d = act(ff, 2 * j + (q[i] == -1), True)
        require(not (a + b - c - d) % 2, 'original guard line 90')
        local += 1
require(not (not hops or not rings or wrong_sign != hops), 'original guard line 92')
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1048576 if sys.platform == 'darwin' else 1024)
require(not (rss >= 384 or time.monotonic() - start >= 180), 'original guard line 94')
out = dict(PASS=True, physical_configurations=len(cases), D_sectors=sorted(sectors), native_hop_columns=hops, native_ring_columns=rings, local_species_CAR_columns=local, missing_hole_minus_rejected=wrong_sign, seconds=time.monotonic() - start, rss_MiB=rss, fixture_sha=hashlib.sha256(rawpath.read_bytes()).hexdigest(), scope='All selected native columns, not fullL4 census; site-major CAR all6-site label columns.')

_elapsed=time.monotonic()-_started
_rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
require(_elapsed<180 and 0<_rss<384,'portable resources')
out['executed_predicates']=_predicates
out['portable_seconds']=_elapsed
out['portable_rss_mib']=_rss
print(json.dumps(out,indent=2,allow_nan=False))
