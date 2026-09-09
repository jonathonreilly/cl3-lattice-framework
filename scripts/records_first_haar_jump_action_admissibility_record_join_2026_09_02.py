#!/usr/bin/env python3
"""Bounded exact controls for the supplied finite Haar-jump construction.

The continuum proof is in the note. Six axes integrate only degree <= 2
polynomials exactly; no six-atom replacement of the mark law is made.
"""
from __future__ import annotations

import hashlib
import itertools
import math
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = 'docs/RECORDS_FIRST_HAAR_JUMP_ACTION_ADMISSIBILITY_RECORD_JOIN_BOUNDED_THEOREM_NOTE_2026-09-02.md'
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    'docs/RECORDS_FIRST_HAAR_JUMP_ACTION_ADMISSIBILITY_RECORD_JOIN_BOUNDED_THEOREM_NOTE_2026-09-02.md',
    'docs/MINIMAL_AXIOMS_2026-06-29.md',
)
INPUT_SHA256 = {'docs/RECORDS_FIRST_HAAR_JUMP_ACTION_ADMISSIBILITY_RECORD_JOIN_BOUNDED_THEOREM_NOTE_2026-09-02.md': 'a6544293195f661263ccf89d5fa7fd18b0f3d60942a2f52a392d9c23f56d15a9', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753'}
Q = sp.Rational
ZERO = (Q(0), Q(0), Q(0))
EX, EY, EZ = (Q(1), Q(0), Q(0)), (Q(0), Q(1), Q(0)), (Q(0), Q(0), Q(1))
SLOTS = (EX, tuple(-x for x in EX), EY, tuple(-x for x in EY), EZ, tuple(-x for x in EZ))
SIGMA = (sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.diag(1, -1))
ID = sp.eye(2)


class Harness:
    def __init__(self):
        self.passed = self.failed = 0

    def check(self, label, condition, detail):
        if condition:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if condition else 'FAIL'} {label} :: {detail}")


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), Q(0))


def scale(c, v):
    return tuple(c*x for x in v)


def density(v):
    return (ID + sum((v[i]*SIGMA[i] for i in range(3)), sp.zeros(2)))/2


def mean(six):
    if len(six) != 6 or any(len(v) != 3 or dot(v, v) > 1 for v in six):
        raise ValueError('six Bloch density slots required')
    return tuple(sum((v[i] for v in six), Q(0))/6 for i in range(3))


def neighbor_state(vertices, records, x):
    if x not in vertices or x in records:
        raise ValueError('an open site in the finite domain is required')
    if not set(records).issubset(vertices) or any(len(v) != 3 or dot(v, v) != 1 for v in records.values()):
        raise ValueError('Record contents must be unit Bloch vectors at domain sites')
    # Absent boundary and open slots both supply zero Bloch vector (I/2).
    slots = tuple(records.get(tuple(x[i]+int(d[i]) for i in range(3)), ZERO) for d in SLOTS)
    return mean(slots)


def permutation_sign(p):
    return (-1)**sum(p[i] > p[j] for i in range(3) for j in range(i+1, 3))


def cubic_rotations():
    return tuple((p, signs) for p in itertools.permutations(range(3))
                 for signs in itertools.product((-1, 1), repeat=3)
                 if permutation_sign(p)*math.prod(signs) == 1)


def rotate(v, rot):
    p, signs = rot
    return tuple(signs[i]*v[p[i]] for i in range(3))


def hemisphere_probability(s, u):
    if len(s) != 3 or len(u) != 3 or dot(s, s) > 1 or dot(u, u) != 1:
        raise ValueError('density input and unit pre-mark axis required')
    return Q(1, 2) + dot(s, u)/4


def branch_map(rho, n):
    if dot(n, n) != 1:
        raise ValueError('unit mark required')
    p = density(n)
    return (2*p*rho*p).applyfunc(sp.expand)


def quadrature_channel(rho):
    return sum((branch_map(rho, n) for n in SLOTS), sp.zeros(2))/6


def predicted_channel(s):
    return density(scale(Q(1, 3), s))


def source_check(h):
    actual = {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS}
    h.check('current declared source binding', actual == INPUT_SHA256,
            f'note and governing memo={len(actual)}; no historical Git/process input')


def density_checks(h):
    count = 0
    valid = True
    for d in itertools.product(range(-6, 7), repeat=3):
        if sum(map(abs, d)) > 6:
            continue
        vectors = []
        for i, value in enumerate(d):
            vectors.extend([scale(1 if value > 0 else -1, (EX, EY, EZ)[i])]*abs(value))
        vectors.extend([ZERO]*(6-len(vectors)))
        s = mean(tuple(vectors)); rho = density(s)
        valid &= rho.trace() == 1 and rho.det() >= 0
        count += 1
    h.check('six-slot enclosing axial resultants', valid and count == 377, f'{count} actual density matrices')
    x = (0, 0, 0); corner = {x, (1,0,0), (0,1,0), (0,0,1)}
    records = {(1,0,0): EX, (0,1,0): EY, (0,0,1): EZ}
    isolated = density(neighbor_state({x}, {}, x)); rho = density(neighbor_state(corner, records, x))
    broken = sum((density(v) for v in records.values()), sp.zeros(2))/6
    rejects = 0
    for bad in [(), (EX,)*5, (scale(2, EX),)*6]:
        try: mean(bad)
        except ValueError: rejects += 1
    h.check('boundary and domain controls', isolated == ID/2 and rho.trace() == 1 and
            broken.trace() == Q(1,2) and rejects == 3,
            f'isolated={isolated.tolist()}; corner trace={rho.trace()}; omitted-boundary trace={broken.trace()}; rejected={rejects}')
    rotations = cubic_rotations(); contents = (EX, ZERO, EY, ZERO, EZ, ZERO)
    m = mean(contents); valid = True
    for rot in rotations:
        permuted = [None]*6
        for i, d in enumerate(SLOTS): permuted[SLOTS.index(rotate(d, rot))] = contents[i]
        valid &= mean(tuple(permuted)) == m
        valid &= mean(tuple(rotate(v, rot) for v in contents)) == rotate(m, rot)
    witness = mean((EX,)+(ZERO,)*5)
    h.check('cubic and frame fixtures with genuine variation', valid and len(rotations) == 24 and witness == scale(Q(1,6), EX),
            f'rotations={len(rotations)}; one-record mean={witness}; continuous covariance proved in note')


def channel_checks(h):
    first = tuple(sum(n[i] for n in SLOTS)/6 for i in range(3))
    second = sp.Matrix(3,3,lambda i,j: sum(n[i]*n[j] for n in SLOTS)/6)
    complete = sum((2*density(n).H*density(n) for n in SLOTS), sp.zeros(2))/6
    h.check('degree-two Haar quadrature and actual completeness', first == ZERO and second == sp.eye(3)/3 and complete == ID,
            f'first={first}; second={second.tolist()}; integral K*K={complete.tolist()}')
    fixtures = (ZERO, EX, EY, EZ, (Q(3,5),Q(4,5),Q(0)), (Q(-4,5),Q(0),Q(3,5)))
    rank_one = True; averages = True; matches = True
    for s in fixtures:
        rho = density(s)
        for n in SLOTS + ((Q(3,5),Q(0),Q(4,5)),):
            p = density(n); branch = branch_map(rho,n); mass = 1+dot(s,n)
            rank_one &= branch == mass*p
            if mass != 0: matches &= branch/mass == p
        averages &= quadrature_channel(rho) == predicted_channel(s)
    h.check('actual branch map, pure output and averaged shrink', rank_one and matches and averages,
            f'complex fixtures={len(fixtures)}; nonzero branch normalization; averaged rho(s/3)')
    # An entangled 4x4 state, local Kraus map, then an actual partial trace.
    psi = sp.Matrix([1,0,0,1]); bell = psi*psi.H/2
    after = sum((2*sp.kronecker_product(density(n),ID)*bell*
                 sp.kronecker_product(density(n).H,ID) for n in SLOTS),sp.zeros(4))/6
    remote = lambda r: sp.Matrix(2,2,lambda b,c: sum(r[2*a+b,2*a+c] for a in range(2)))
    h.check('computed local channel and remote Bell marginal', after != bell and after.trace() == 1 and remote(after) == remote(bell) == ID/2,
            f'remote={remote(after).tolist()}; global channel theorem follows completeness')
    s = (Q(3,5),Q(0),Q(4,5)); n = EX
    pushed = sum(((1+b*dot(s,a))/2*density(scale(b,a)) for a,b in ((n,1),(scale(-1,n),-1))),sp.zeros(2))
    h.check('signed-axis first-write operation equality', pushed == branch_map(density(s),n),
            f'combined branch mass={pushed.trace()}; expected 8/5 from two preimages')


def history_checks(h):
    # Two far-separated open sites, each surrounded by six permanent Records.
    sites = ((0,0,0),(10,0,0)); vertices = set(sites); records = {}
    for x, v in zip(sites, (EZ, scale(-1,EZ))):
        for d in SLOTS:
            y = tuple(x[i]+int(d[i]) for i in range(3)); vertices.add(y); records[y] = v
    states = tuple(neighbor_state(vertices,records,x) for x in sites)
    pfirst = tuple(hemisphere_probability(s,EZ) for s in states)
    expected_first = (Q(3,4),Q(1,4))  # Integrals of (1 +/- n_z) on n_z>=0.
    weights = []; residual1 = residual2 = cross = Q(0); conditional = True
    second_values = []
    for selected in range(2):
        p1 = pfirst[selected]
        for x1 in (0,1):
            history_mass = Q(1,2)*(p1 if x1 else 1-p1)
            u2 = EZ if x1 else scale(-1,EZ)
            p2 = hemisphere_probability(states[1-selected],u2)
            expected2 = Q(1,2)+Q(1,4)*(1 if 1-selected == 0 else -1)*(1 if x1 else -1)
            second_values.append(p2)
            # The second conditional probabilities are independently integrated values.
            conditional &= p2 == expected2 and expected2*(1-p2)+(1-expected2)*(-p2) == 0
            for x2 in (0,1):
                w = history_mass*(expected2 if x2 else 1-expected2)
                weights.append(w); residual1 += w*(x1-p1); residual2 += w*(x2-p2)
                cross += w*(x1-p1)*(x2-p2)
    h.check('actual two-stage finite adaptive histories', pfirst == expected_first and conditional and len(weights) == 8 and
            sum(weights) == 1 and residual1 == residual2 == cross == 0 and set(second_values) == {Q(1,4),Q(3,4)},
            f'leaves={len(weights)}; mass={sum(weights)}; first={pfirst}; residual means={residual1},{residual2}; cross={cross}')
    past_probability = sum(pfirst)/2
    h.check('selected-site versus past-only probability', past_probability == Q(1,2) and all(p != past_probability for p in pfirst),
            f'past={past_probability}; selected={pfirst}; site not predictable from past')
    coefficients = tuple(Q((-1)**k,math.factorial(k)) for k in range(10))
    rates = tuple(Q(1) for x in vertices if x not in records)
    after_records = dict(records); after_records[sites[0]] = EX
    after_rates = tuple(Q(1) for x in vertices if x not in after_records)
    h.check('finite race and absorbing record rows', sum(rates) == 2 and sum(after_rates) == 1 and
            all((k+1)*coefficients[k+1] == -coefficients[k] for k in range(9)),
            f'open total 2 -> 1; race probability 1/2; exponential coefficients={len(coefficients)}; finite process proof in note')


def response_family_checks(h):
    s = mean((EX,)+(ZERO,)*5)
    probabilities = tuple(Q(1,2)+lam*dot(s,EX)/4 for lam in (Q(0),Q(1,2),Q(1)))
    h.check('typing-only zero and distinct varying nonzero local laws', probabilities == (Q(1,2),Q(25,48),Q(13,24)) and hemisphere_probability(s,EX) == Q(13,24),
            f'hemispheres lambda=0,1/2,1: {probabilities}; no full-axiom countermodel')


def main():
    h = Harness()
    source_check(h)
    density_checks(h)
    channel_checks(h)
    history_checks(h)
    response_family_checks(h)
    print('Scope: supplied six-slot finite process and exact conditional algebra; continuum proofs in note; physical suppliers open.')
    print('Historical 10/0, 34 named mutations and source-unavailable independent 7/7 are not current validation.')
    print(f'TOTAL: PASS={h.passed} FAIL={h.failed}')
    return int(h.failed != 0)


if __name__ == '__main__':
    raise SystemExit(main())
