import resource,sys,json,time,signal
executed_predicates=0
def _require(condition,label):
 global executed_predicates
 executed_predicates+=1
 if not condition:raise RuntimeError(label)
import time, signal, resource, sys, pathlib, json, itertools, hashlib
start = time.monotonic()
if __name__ == '__main__':
    signal.alarm(180)
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
rawpath = pathlib.Path(__file__).resolve().parents[1] / '.claude/science/physics-loops/native-u1-pair-and-all-sector-support-20260908/inputs/GLOBAL_D4_SEED.json'
raw = json.loads(rawpath.read_text())
cases |= {int(r['initial_bits'], 2) for r in raw['witnesses']}

def candidate(z, e, omit_block_phase=False):
    deg, q = data(z)
    i, j = edges[e]
    b, wv = (i, j) if eps[i] > 0 else (j, i)
    orientation = 1 if b < wv else -1
    bit = z >> e & 1
    if bit == 0:
        terms = [(1, ((b, 1, True), (wv, 1, False))), (1, ((b, -1, False), (wv, -1, True))), (-1, ((b, 1, True), (wv, -1, True))), (-1, ((b, -1, False), (wv, 1, False)))]
    else:
        terms = [(1, ((b, 1, False), (wv, 1, True))), (1, ((b, -1, True), (wv, -1, False))), (-1, ((b, -1, True), (wv, 1, True))), (-1, ((b, 1, False), (wv, -1, False)))]
    out = {}
    f = species(q)
    for coef, ops in terms:
        if omit_block_phase and coef == -1:
            coef = 1
        ff = f
        par = 0
        for v, s, c in reversed(ops):
            ff, sgn = act(ff, 2 * v + (s == -1), c)
            if ff is None:
                break
            par += sgn
        if ff is None or any((ff >> 2 * v & 3 == 3 for v in (b, wv))):
            continue
        zz = z ^ 1 << e
        qq = data(zz)[1]
        _require(not (max(map(abs, qq)) > 1 or ff != species(qq)), 'candidate Gauss/refusal')
        pp = (3 + 2 * (coef < 0) + 2 * (orientation < 0) + 2 * par) % 4
        out[zz] = out.get(zz, 0) + 1j ** pp
    return out
counts = {}
forbidden = 0
wrong = 0
twostep = 0
paths = set()

def checkcolumn(z, e):
    global forbidden, wrong
    q = data(z)[1]
    zz = z ^ 1 << e
    qq = data(zz)[1]
    got = candidate(z, e)
    if max(map(abs, qq)) > 1:
        _require(not got, 'forbidden survived')
        forbidden += 1
        return None
    expected = 1j ** ((2 * ((w[e] & z).bit_count() % 2) + phase(zz, qq) - phase(z, q)) % 4)
    _require(not got != {zz: expected}, ('native A map', e, got, expected))
    D = sum((v * v for v in q))
    DD = sum((v * v for v in qq))
    counts[str((D, DD))] = counts.get(str((D, DD)), 0) + 1
    if candidate(z, e, True) != {zz: expected}:
        wrong += 1
    return (zz, expected)
for z in cases:
    for e in range(192):
        got = checkcolumn(z, e)
        if got is None:
            continue
        zz, p1 = got
        for f in range(0, 192, 31):
            if f == e:
                continue
            q2 = data(zz ^ 1 << f)[1]
            if max(map(abs, q2)) > 1:
                continue
            end, p2 = checkcolumn(zz, f)
            startq = data(z)[1]
            native = 1j ** (2 * ((w[e] & z).bit_count() % 2) + 2 * ((w[f] & zz).bit_count() % 2) + phase(end, q2) - phase(z, startq))
            _require(not abs(p1 * p2 - native) > 1e-14, 'two step')
            twostep += 1
            paths.add((sum((v * v for v in startq)), sum((v * v for v in data(zz)[1])), sum((v * v for v in q2))))
_require(not (not all((str(k) in counts for k in [(0, 2), (2, 0), (2, 4), (4, 2)])) or not wrong or (not {(0, 2, 4), (2, 0, 2)} <= paths)), 'coverage')
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1048576 if sys.platform == 'darwin' else 1024)
_require(not (rss >= 384 or time.monotonic() - start >= 180), 'resources')
out = {'PASS': True, 'initial_configurations': len(cases), 'allowed_column_counts_with_composition_repeats': counts, 'forbidden_columns': forbidden, 'missing_bD_pair_sign_mutant_rejected': wrong, 'nonbacktracking_two_edge_paths': twostep, 'D_path_types': sorted(paths), 'seconds': time.monotonic() - start, 'rss_MiB': rss, 'scope': 'Direct native Pauli phases versus projected two-species CAR; selected full L4 columns, not a census.'}
out = out
out = out
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
_require(0<rss<384 and time.monotonic()-start<180,'resource cap')
out['executed_predicates']=executed_predicates
print(json.dumps(out,indent=2,allow_nan=False))
