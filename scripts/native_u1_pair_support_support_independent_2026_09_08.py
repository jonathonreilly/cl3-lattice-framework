import resource,sys,json,time,signal
executed_predicates=0
def _require(condition,label):
 global executed_predicates
 executed_predicates+=1
 if not condition:raise RuntimeError(label)
import itertools, json, pathlib, time, signal
if __name__ == '__main__':
    signal.alarm(180)
start = time.monotonic()
p = pathlib.Path(__file__).parent
edges = [(i, 6 + j) for i in range(6) for j in range(6)]
ind = {e: k for k, e in enumerate(edges)}
inc = [[k for k, e in enumerate(edges) if v in e] for v in range(12)]

def q(x):
    return [(1 if v < 6 else -1) * (sum((x >> e & 1 for e in inc[v])) - 3) for v in range(12)]

def arcs(x):
    return [(u, v, k) if x >> k & 1 else (v, u, k) for k, (u, v) in enumerate(edges)]

def move(x, k):
    y = x ^ 1 << k
    _require(not max(map(abs, q(y))) > 1, 'illegal intermediate')
    return y
ice = sum((1 << ind[i, 6 + j] for i in range(6) for j in range(6) if (j - i) % 6 < 3))

def reduce(x):
    tape = []
    while any(q(x)):
        Q = q(x)
        source = Q.index(1)
        front = [source]
        paths = {source: []}
        target = None
        while front:
            u = front.pop()
            if Q[u] == -1:
                target = u
                break
            for a, b, k in arcs(x):
                if a == u and b not in paths:
                    paths[b] = paths[u] + [(a, b, k)]
                    front.append(b)
        _require(not target is None, 'sink counterexample')
        path = paths[target]
        last = max((i for i, (a, b, k) in enumerate(path) if Q[a] == 1))
        path = path[last:]
        _require(not any((Q[a] != 0 for a, b, k in path[1:])), 'interior')
        old = sum((t * t for t in Q))
        for a, b, k in path:
            x = move(x, k)
            tape.append(k)
        _require(not sum((t * t for t in q(x))) != old - 2, 'D drop')
    return (x, tape)

def join(x, y):
    tape = []
    while x != y:
        changed = x ^ y
        ar = [(a, b, k) for a, b, k in arcs(x) if changed >> k & 1]
        v = ar[0][0]
        seen = {}
        walk = []
        while v not in seen:
            seen[v] = len(walk)
            edge = next((t for t in ar if t[0] == v))
            walk.append(edge)
            v = edge[1]
        cycle = walk[seen[v]:]
        for a, b, k in cycle:
            x = move(x, k)
            tape.append(k)
        _require(not any(q(x)), 'ice cycle endpoint')
    _require(not len(tape) > 36, 'join bound')
    return tape
fixtures = [ice, sum((1 << ind[i, 6 + j] for i in range(6) for j in range(6) if (j - i) % 6 < 2))]
fixtures.append(fixtures[1] ^ (1 << 36) - 1)
x = ice
for t in range(512):
    k = (t * t + 17 * t + 7) % 36
    y = x ^ 1 << k
    if max(map(abs, q(y))) <= 1:
        x = y
    if t in [7, 15, 31, 63, 127, 255, 511]:
        fixtures.append(x)
reductions = [reduce(x) for x in fixtures]
pairs = []
for i, j in itertools.product(range(len(fixtures)), repeat=2):
    a, ta = reductions[i]
    b, tb = reductions[j]
    mid = join(a, b)
    tape = ta + mid + list(reversed(tb))
    x = fixtures[i]
    for k in tape:
        x = move(x, k)
    bound = (sum((t * t for t in q(fixtures[i]))) + sum((t * t for t in q(fixtures[j])))) * 11 // 2 + 36
    _require(not (x != fixtures[j] or len(tape) > bound), 'full pair route')
    pairs.append(dict(i=i, j=j, tape=tape, bound=bound))

def amp(x, k):
    i, j = edges[k]
    before = [f for v, w in [(i, j), (j, i)] for f in inc[v] if (edges[f][1] if edges[f][0] == v else edges[f][0]) < w]
    return (-1) ** sum((x >> f & 1 for f in before))
a, b, c = (ind[0, 6], ind[0, 9], ind[0, 7])
word = [a, b, c, a, b, c]
x = ice
phase = 1
states = [x]
for k in word:
    phase *= amp(x, k)
    x = move(x, k)
    states.append(x)
_require(not (x != ice or phase != -1), 'closed A phase')
out = dict(graph='K6,6', fixture_bits=fixtures, D=[sum((t * t for t in q(x))) for x in fixtures], all_ordered_pair_routes=pairs, phase_word=word, phase_states=states, phase=phase, seconds=time.monotonic() - start, scope='different graph exact constructive controls,not exhaustive orientations')
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
_require(0<rss<384 and time.monotonic()-start<180,'resource cap')
out['executed_predicates']=executed_predicates
print(json.dumps(out,indent=2,allow_nan=False))
