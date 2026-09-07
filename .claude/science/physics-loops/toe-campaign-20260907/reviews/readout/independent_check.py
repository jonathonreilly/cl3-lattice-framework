#!/usr/bin/env python3
"""Independent controls; standard library, no author/repository imports.

Bellman optimization ranges over every nonanticipating fresh-draw scheduler
for a fixed terminal event. It does not reuse the author's order-mixture or
forward-flow implementation. Potts controls use a new six-site ladder and
noninteger coupling, with every partially exposed bond condition checked.
"""

from fractions import Fraction as Q
from functools import lru_cache
from itertools import product, permutations
from math import factorial
from decimal import Decimal, localcontext
import json


def neighbors(n, edges):
    return tuple(tuple(j if i == x else i for i, j in edges if i == x or j == x)
                 for x in range(n))


def spin_bond_ladder():
    n = 6
    edges = ((0, 1), (1, 2), (3, 4), (4, 5), (0, 3), (1, 4), (2, 5))
    t = Q(3, 2)
    v = t - 1
    alpha = v / (3 + v)
    pair = (0, 5)
    spins = [(c, t ** sum(c[i] == c[j] for i, j in edges))
             for c in product(range(3), repeat=n)]
    z_spin = sum(w for _, w in spins)
    ex = sum(w for c, w in spins if c[pair[0]] == 0) / z_spin
    ey = sum(w for c, w in spins if c[pair[1]] == 0) / z_spin
    cov = sum(w for c, w in spins if c[pair[0]] == c[pair[1]] == 0) / z_spin - ex * ey
    bonds = {}
    connected_mass = Q(0)
    for bits in product((0, 1), repeat=len(edges)):
        adj = [set() for _ in range(n)]
        for (i, j), present in zip(edges, bits):
            if present:
                adj[i].add(j)
                adj[j].add(i)
        unseen = set(range(n))
        components = []
        while unseen:
            component = {min(unseen)}
            while True:
                expanded = component | set().union(*(adj[i] for i in component))
                if expanded == component:
                    break
                component = expanded
            components.append(component)
            unseen -= component
        w = v ** sum(bits) * 3 ** len(components)
        bonds[bits] = w
        if any(set(pair) <= c for c in components):
            connected_mass += w
    z_bond = sum(bonds.values())
    assert z_spin == z_bond
    assert ex == ey == Q(1, 3)
    assert cov == Q(2, 9) * connected_mass / z_bond
    assert cov >= Q(2, 9) * alpha ** 3
    minimum = Q(1)
    checks = 0
    for target in range(len(edges)):
        other = [i for i in range(len(edges)) if i != target]
        for conditions in product((-1, 0, 1), repeat=len(other)):
            compatible = [(bits, w) for bits, w in bonds.items()
                          if all(c == -1 or bits[i] == c for i, c in zip(other, conditions))]
            conditional = sum(w for bits, w in compatible if bits[target]) / sum(w for _, w in compatible)
            assert conditional >= alpha
            minimum = min(minimum, conditional)
            checks += 1
    assert minimum == alpha
    return dict(partition=str(z_spin), covariance=str(cov), alpha=str(alpha),
                lower_bound=str(Q(2, 9) * alpha ** 3), partial_condition_checks=checks)


def appendix_bellman(weights):
    n = 4
    edges = ((0, 1), (1, 2), (2, 3), (3, 0))
    adj = neighbors(n, edges)
    p, q, r = map(Q, weights)

    def factor(a, b):
        return p if a == b else q if a // 2 == b // 2 else r

    def distribution(state, x):
        raw = []
        for s in range(6):
            weight = Q(1)
            for y in adj[x]:
                if state[y] != -1:
                    weight *= factor(s, state[y])
            raw.append(weight)
        z = sum(raw)
        return tuple(w / z for w in raw)

    @lru_cache(None)
    def optimal_equal_event(state):
        occupied = {s for s in state if s != -1}
        if len(occupied) > 1:
            return Q(0)
        if -1 not in state:
            return Q(1)
        candidates = []
        for x, s in enumerate(state):
            if s == -1:
                candidates.append(sum(prob * optimal_equal_event(state[:x] + (a,) + state[x+1:])
                                      for a, prob in enumerate(distribution(state, x))))
        return max(candidates)

    optimal = optimal_equal_event((-1,) * n)
    z_static = Q(0)
    numerator = Q(0)
    for state in product(range(6), repeat=n):
        w = Q(1)
        for i, j in edges:
            w *= factor(state[i], state[j])
        z_static += w
        if len(set(state)) == 1:
            numerator += w
    static = numerator / z_static
    # Direct normalizer derivation for a tree-growing order: after its arbitrary
    # first label, the three matching probabilities are p/z, p/z, p^2/S.
    z = p + q + 4 * r
    same_pair_sum = p*p + q*q + 4*r*r
    derived = p**4 / (z*z*same_pair_sum)
    assert optimal == derived
    assert static > optimal if len(set(weights)) > 1 else static == optimal
    return dict(weights=[str(x) for x in weights], exact_optimum=str(optimal),
                static_event=str(static), gap=str(static-optimal),
                bellman_states=optimal_equal_event.cache_info().currsize)


def ancestry_on_path():
    # Independent combinatorial witness: all 120 priority orders on P5.
    adj = neighbors(5, ((0, 1), (1, 2), (2, 3), (3, 4)))
    escape = 0
    certificate_extra_shell = False
    for order in permutations(range(5)):
        ranks = {x: order.index(x) for x in range(5)}
        @lru_cache(None)
        def descend(x):
            return frozenset({x}).union(*(descend(y) for y in adj[x] if ranks[y] < ranks[x]))
        ancestry = descend(0)
        escape += any(x >= 3 for x in ancestry)
        certificate = set(ancestry).union(*(set(adj[x]) for x in ancestry))
        assert len(certificate) <= 3 * len(ancestry)
        if ancestry == frozenset({0}):
            assert certificate == {0, 1}
            certificate_extra_shell = True
    assert Q(escape, factorial(5)) == Q(1, factorial(4))
    assert certificate_extra_shell
    return dict(priority_orders=factorial(5), root_escape_distance_3=str(Q(escape, factorial(5))),
                one_neighbor_certificate_needed=certificate_extra_shell)


def exact_distance():
    # Recurrence avoids factorial(257) as the calculation route; the separate
    # integer cross-check is then performed only as an independent identity.
    ratio = Q(108) * 16 / 2
    for m in range(1, 256):
        ratio *= Q(80, m + 2)
    assert ratio == Q(108 * 5**255 * 4**512, factorial(257))
    assert Q(1, 10**21) < ratio < Q(1, 10**20)
    assert factorial(257) > 108 * 5**255 * 4**512
    with localcontext() as ctx:
        ctx.prec = 35
        text_ratio = str(Decimal(ratio.numerator) / Decimal(ratio.denominator))
    return dict(D=512, truncation_radius=255, ratio_decimal=text_ratio,
                comparison='257! > 108 * 5^255 * 4^512', exact_margin_verified=True)


if __name__ == '__main__':
    result = dict(
        ancestry=ancestry_on_path(),
        potts_ladder=spin_bond_ladder(),
        adaptive_bellman=[appendix_bellman(w) for w in
                         ((3,1,2), (Q(5,2),Q(1,3),Q(7,4)), (1,5,2), (2,2,1), (2,2,2))],
        distance=exact_distance(),
    )
    print(json.dumps(result, indent=2))
    print('INDEPENDENT CHECKS: PASS')
