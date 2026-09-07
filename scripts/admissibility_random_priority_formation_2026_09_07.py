#!/usr/bin/env python3
"""Exact controls for the conditional random-priority formation construction.

Standard library only. No Monte Carlo, random seeds, repository imports, network,
or output-file writes. Finite certificates test the formulas and implementations;
the infinite-lattice arguments are in the paired source note.
"""

from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations_with_replacement, permutations, product
from math import factorial, prod


PASS = 0


def check(name, condition, detail=""):
    global PASS
    if not condition:
        print(f"FAIL {name}: {detail}")
        raise AssertionError(name)
    PASS += 1
    print(f"PASS {name}" + (f": {detail}" if detail else ""))


def phi(s, t, weights):
    p, q, r = weights
    return p if s == t else q if s // 2 == t // 2 else r


def odds(values, weights):
    raw = [prod(phi(s, t, weights) for t in values) for s in range(6)]
    return tuple(F(w, sum(raw)) for w in raw)


def graph(vertices, edges):
    neighbors = {x: set() for x in vertices}
    for x, y in edges:
        neighbors[x].add(y)
        neighbors[y].add(x)
    return neighbors


def ancestors(root, neighbors, priority):
    found = {root}
    pending = [root]
    while pending:
        x = pending.pop()
        for y in neighbors[x]:
            if priority[y] < priority[x] and y not in found:
                found.add(y)
                pending.append(y)
    return found


def race(probabilities, marks):
    """Exact deterministic exponential-race map at declared rational marks.

    The marks in finite map tests are fixtures, not samples of exponentials.
    In the theorem independent Exp(1) marks give exactly the supplied odds.
    """
    scores = tuple(marks[s] / probabilities[s] for s in range(6))
    winner = min(range(6), key=lambda s: scores[s])
    if scores.count(scores[winner]) != 1:
        raise ValueError("fixture has an exponential-race tie")
    return winner


def solve_sorted(neighbors, priority, marks, weights):
    out = {}
    for x in sorted(neighbors, key=priority.__getitem__):
        out[x] = race(odds([out[y] for y in neighbors[x] if y in out], weights), marks[x])
    return out


def solve_ancestor(root, neighbors, priority, marks, weights):
    subset = ancestors(root, neighbors, priority)
    induced = {x: neighbors[x] & subset for x in subset}
    return solve_sorted(induced, priority, marks, weights)[root]


def neighbors_z3(x):
    for axis in range(3):
        for step in (-1, 1):
            y = list(x)
            y[axis] += step
            yield tuple(y)


def solve_local_z3(roots, mark_source, weights):
    """On-demand infinite-lattice construction for a supplied consistent mark source.

    mark_source(x) returns (priority, six positive race marks). With true iid
    continuous priorities and independent iid Exp(1) race marks this terminates
    almost surely and samples the theorem's finite marginal exactly. This file
    supplies no pseudo-random surrogate for that infinite probability space.
    A deterministic mark source can have infinite descending paths; no claim of
    termination is made on such input. The one-neighbor certificate shell is
    included in queried, even when its sites are not ancestors.
    """
    if not weights or any(w <= 0 for w in weights):
        raise ValueError("strictly positive orbit weights are required")
    roots = tuple(roots)
    cache = {}
    def get(x):
        if x not in cache:
            cache[x] = mark_source(x)
        return cache[x]
    found = set(roots)
    pending = list(roots)
    while pending:
        x = pending.pop()
        tx, _ = get(x)
        for y in neighbors_z3(x):
            ty, _ = get(y)
            if ty < tx and y not in found:
                found.add(y)
                pending.append(y)
    induced = {x: set(neighbors_z3(x)) & found for x in found}
    priority = {x: get(x)[0] for x in found}
    marks = {x: get(x)[1] for x in found}
    values = solve_sorted(induced, priority, marks, weights)
    return {x: values[x] for x in roots}, frozenset(found), frozenset(cache)


def formation_mass(values, order, neighbors, weights):
    out = F(1)
    past = set()
    for x in order:
        out *= odds([values[y] for y in neighbors[x] & past], weights)[values[x]]
        past.add(x)
    return out


def order_law(neighbors, weights):
    """Complete order/configuration summation; independent of state-flow code."""
    vertices = tuple(neighbors)
    orders = tuple(permutations(vertices))
    law = {}
    for values in product(range(6), repeat=len(vertices)):
        law[values] = sum((formation_mass(values, order, neighbors, weights)
                           for order in orders), F(0)) / len(orders)
    return law


def flow_law(neighbors, weights, adaptive=False):
    """Forward probability flow through all partial record configurations."""
    n = len(neighbors)
    current = {(-1,) * n: F(1)}
    for _ in range(n):
        nxt = defaultdict(F)
        for state, mass in current.items():
            blank = [x for x in range(n) if state[x] == -1]
            # Optional scheduler sees values of formed neighbors, never a pending draw.
            scores = {x: 1 + (sum(state[y] == 0 for y in neighbors[x]) if adaptive else 0)
                      for x in blank}
            for x in blank:
                qx = F(scores[x], sum(scores.values()))
                conditional = odds([state[y] for y in neighbors[x] if state[y] != -1], weights)
                for s in range(6):
                    new = state[:x] + (s,) + state[x + 1:]
                    nxt[new] += mass * qx * conditional[s]
        current = nxt
    return dict(current)


def static_law(neighbors, weights):
    edges = [(x, y) for x in neighbors for y in neighbors[x] if x < y]
    raw = {v: prod(phi(v[x], v[y], weights) for x, y in edges)
           for v in product(range(6), repeat=len(neighbors))}
    partition = sum(raw.values())
    return {v: F(w, partition) for v, w in raw.items()}, partition


def marginal(law, sites):
    out = defaultdict(F)
    for v, mass in law.items():
        out[tuple(v[x] for x in sites)] += mass
    return dict(out)


def tv(left, right):
    return sum((abs(left.get(v, F(0)) - right.get(v, F(0)))
                for v in left.keys() | right.keys()), F(0)) / 2


def cubic_rotations():
    for perm in permutations(range(3)):
        parity = (-1) ** sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3))
        for signs in product((-1, 1), repeat=3):
            if parity * prod(signs) == 1:
                def coordinate(x, perm=perm, signs=signs):
                    return tuple(x[perm[i]] if signs[i] == 1 else 1 - x[perm[i]] for i in range(3))
                mapping = []
                for label in range(6):
                    axis, sign = label // 2, 1 if label % 2 == 0 else -1
                    new_axis = perm.index(axis)
                    new_sign = signs[new_axis] * sign
                    mapping.append(2 * new_axis + (new_sign == -1))
                yield coordinate, tuple(mapping)


def tail(m):
    if m < 1:
        return F(1)
    return min(F(1), F(6 * 5 ** (m - 1), factorial(m + 1)))


def components(n, edges):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for x, y in edges:
        parent[find(x)] = find(y)
    return tuple(find(x) for x in range(n))


def potts_bond_control(neighbors, pair):
    """Independent spin and bond sums for p=q=2,r=1, hence q_colors=3,v=1."""
    n = len(neighbors)
    edges = [(x, y) for x in neighbors for y in neighbors[x] if x < y]
    z_spin = pair_spin = 0
    for colors in product(range(3), repeat=n):
        weight = 2 ** sum(colors[x] == colors[y] for x, y in edges)
        z_spin += weight
        if colors[pair[0]] == colors[pair[1]] == 0:
            pair_spin += weight
    z_bond = conn_bond = 0
    states = {}
    for mask in range(1 << len(edges)):
        roots = components(n, [edge for j, edge in enumerate(edges) if mask & (1 << j)])
        weight = 3 ** len(set(roots))
        states[mask] = weight
        z_bond += weight
        if roots[pair[0]] == roots[pair[1]]:
            conn_bond += weight
    cov = F(pair_spin, z_spin) - F(1, 9)
    check(f"spin_bond_partition_{n}", z_spin == z_bond, f"Z={z_spin}")
    check(f"spin_bond_covariance_{n}", cov == F(2 * conn_bond, 9 * z_bond), f"cov={cov}")
    minimum = F(1)
    for mask, absent_weight in states.items():
        for j in range(len(edges)):
            if not mask & (1 << j):
                present_weight = states[mask | (1 << j)]
                minimum = min(minimum, F(present_weight, absent_weight + present_weight))
    check(f"bond_insertion_floor_{n}", minimum == F(1, 4), f"minimum={minimum}")
    return cov


def main():
    rotations = tuple(cubic_rotations())
    check("proper_cubic_group_size", len({mapping for _, mapping in rotations}) == 24)
    conditions = tuple(values for k in range(7)
                       for values in combinations_with_replacement(range(6), k))
    normalized = covariant = True
    for values in conditions:
        law = odds(values, (3, 1, 2))
        normalized &= all(v > 0 for v in law) and sum(law) == 1
        for _, mapping in rotations:
            changed = odds([mapping[v] for v in values], (3, 1, 2))
            covariant &= all(changed[mapping[s]] == law[s] for s in range(6))
    check("all_partial_multiset_odds", normalized, f"conditions={len(conditions)}")
    check("all_partial_multiset_covariance", covariant, f"comparisons={len(conditions)*24*6}")

    vertices = tuple(product((0, 1), repeat=3))
    edges = [(x, y) for x in vertices for y in vertices if x < y and sum(a != b for a, b in zip(x, y)) == 1]
    cube_coords = graph(vertices, edges)
    priority = {x: F((5 * i) % 8 + 1, 10) for i, x in enumerate(vertices)}
    primes = (101, 103, 107, 109, 113, 127)
    marks = {x: tuple(F(primes[(s + i) % 6], 17 + i) for s in range(6))
             for i, x in enumerate(vertices)}
    whole = solve_sorted(cube_coords, priority, marks, (3, 1, 2))
    check("ancestor_equals_sorted_cube", all(solve_ancestor(x, cube_coords, priority, marks, (3, 1, 2)) == whole[x] for x in vertices))
    ok = True
    for rotate, mapping in rotations:
        transformed_marks = {}
        for x in vertices:
            row = [None] * 6
            for s in range(6):
                row[mapping[s]] = marks[x][s]
            transformed_marks[rotate(x)] = tuple(row)
        result = solve_sorted(cube_coords, {rotate(x): priority[x] for x in vertices}, transformed_marks, (3, 1, 2))
        ok &= all(result[rotate(x)] == mapping[whole[x]] for x in vertices)
    check("pathwise_race_covariance", ok, "24 rotations; marks relabeled with effects")
    shift = lambda x: (x[0] + 7, x[1] - 4, x[2] + 3)
    translated = {shift(x): {shift(y) for y in ys} for x, ys in cube_coords.items()}
    result = solve_sorted(translated, {shift(x): v for x, v in priority.items()}, {shift(x): v for x, v in marks.items()}, (3, 1, 2))
    check("pathwise_translation", all(result[shift(x)] == whole[x] for x in vertices))

    origin = (0, 0, 0)
    ball2 = {x for x in product(range(-2, 3), repeat=3) if sum(map(abs, x)) <= 2}
    shell1 = tuple(neighbors_z3(origin))
    def local_fixture(x):
        if x not in ball2:
            raise AssertionError("ancestor solver read beyond its certificate shell")
        index = sorted(ball2).index(x)
        priority = F(9, 10) if x == origin else F(shell1.index(x) + 1, 10) if x in shell1 else F(950 + index, 1000)
        return priority, tuple(F(primes[(s + index) % 6], 31) for s in range(6))
    result, found, queried = solve_local_z3((origin,), local_fixture, (3, 1, 2))
    ball_graph = {x: set(neighbors_z3(x)) & ball2 for x in ball2}
    result_full = solve_sorted(ball_graph, {x: local_fixture(x)[0] for x in ball2}, {x: local_fixture(x)[1] for x in ball2}, (3, 1, 2))
    check("on_demand_z3_certificate", found == {origin, *shell1} and queried == ball2 and result[origin] == result_full[origin],
          f"ancestors={len(found)}; queried={len(queried)}; root_label={result[origin]}")

    path3 = graph(range(3), ((0, 1), (1, 2)))
    path4 = graph(range(4), ((0, 1), (1, 2), (2, 3)))
    cycle4 = graph(range(4), ((0, 1), (1, 2), (2, 3), (3, 0)))
    for label, neighbors in (("path3", path3), ("cycle4", cycle4)):
        exact = order_law(neighbors, (3, 1, 2))
        flows = flow_law(neighbors, (3, 1, 2))
        check(f"priority_order_vs_flow_{label}", exact == flows and sum(exact.values()) == 1, f"configurations={len(exact)}")
    law4 = flow_law(path4, (3, 1, 2))
    law3 = flow_law(path3, (3, 1, 2))
    error = tv(marginal(law4, (0, 1)), marginal(law3, (0, 1)))
    escaped = 0
    for order in permutations(range(4)):
        pr = {x: order.index(x) for x in range(4)}
        escaped += bool((ancestors(0, path4, pr) | ancestors(1, path4, pr)) - {0, 1, 2})
    check("exact_boundary_escape", F(escaped, 24) == F(1, 6), f"escape={escaped}/24")
    check("exact_boundary_cancellation", error == 0, "sites 0,1: pair_TV=0 despite escape=1/6")
    boundary_error = tv(marginal(law4, (0, 2)), marginal(law3, (0, 2)))
    check("exact_boundary_nonzero_tv", 0 < boundary_error <= F(1, 2),
          f"sites 0,2: pair_TV={boundary_error}; escape=T_2>T_3 has probability 1/2")

    for weights in ((3, 1, 2), (5, 2, 4), (2, 1, 2), (2, 2, 1), (2, 2, 2)):
        p, q, r = weights
        z, a, b = p + q + 4*r, p + q - 2*r, p - q
        static, partition = static_law(cycle4, weights)
        den1 = z*z * (z*z + 2*a*a + 3*b*b)
        den2 = (z*z + 2*a*a + 3*b*b)**2
        masses = [formation_mass((0, 0, 0, 0), o, cycle4, weights) for o in permutations(range(4))]
        check(f"plaquette_spectral_control_{weights}", partition == z**4 + 2*a**4 + 3*b**4 and
              sorted(masses) == sorted([F(p**4, den1)]*16 + [F(p**4, den2)]*8))
        static_event = sum((v for k, v in static.items() if len(set(k)) == 1), F(0))
        envelope = 6 * max(masses)
        gap = static_event - envelope
        check(f"plaquette_envelope_{weights}", gap > 0 if len(set(weights)) > 1 else gap == 0,
              f"static={static_event}; envelope={envelope}; gap={gap}")
    adaptive = flow_law(cycle4, (3, 1, 2), adaptive=True)
    for values, mass in adaptive.items():
        check_envelope = mass <= max(formation_mass(values, o, cycle4, (3, 1, 2)) for o in permutations(range(4)))
        if not check_envelope:
            raise AssertionError(f"adaptive envelope failure at {values}")
    check("adaptive_history_dependent_control", sum(adaptive.values()) == 1, "1296 pointwise envelopes; scheduler sees formed values")

    for m in range(1, 7):
        # A fixed simple path has exactly one decreasing relative order.
        orders = tuple(permutations(range(m + 1)))
        decreasing = sum(all(v[j] > v[j + 1] for j in range(m)) for v in orders)
        check(f"path_order_factorial_{m}", decreasing == 1 and len(orders) == factorial(m + 1))
    for m in (10, 20, 40):
        check(f"tail_ratio_{m}", F(6*5**m, factorial(m+2)) / F(6*5**(m-1), factorial(m+1)) == F(5, m+2), f"b_{m}={tail(m)}")

    potts_bond_control(cycle4, (0, 2))
    cube_index = {x: i for i, x in enumerate(vertices)}
    cube = graph(range(8), [(cube_index[x], cube_index[y]) for x, y in edges])
    cube_cov = potts_bond_control(cube, (0, 7))
    check("static_path_lower_bound_cube", cube_cov >= F(2, 9*4**3), f"cov={cube_cov}; lower=1/288")
    upper = 4 * tail(256)
    lower = F(2, 9 * 4**512)
    ratio = upper / lower
    # Independently compare the unreduced integers rather than just the Fraction ratio.
    check("infinite_discriminator_integer", factorial(257) > 108 * 5**255 * 4**512,
          "distance=512; radius=255; p=q=2,r=1")
    check("infinite_discriminator_margin", F(1, 10**21) < ratio < F(1, 10**20),
          "10^-21 < formation_bound/static_lower < 10^-20")
    print(f"TOTAL: PASS={PASS} FAIL=0")


if __name__ == "__main__":
    main()
