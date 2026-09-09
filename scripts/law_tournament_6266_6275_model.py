"""Owned finite bridge for original Blocks 67/71; supplied carrier conventions.

Only current Block 63 matrix/carrier algebra and Block 64 local functions are
used. Their historical main functions and physical compiler imports are unused.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations, permutations
import numpy as np
import admissibility_strict_nearest_neighbor_state_dependent_record_born_history_single_front_2026_08_12 as b64
import admissibility_record_native_state_dependent_born_history_joint_law_candidate_gate_2026_08_12 as b63

Z, ONE = b63.ZERO, b63.ONE
P0, P1 = b63.matrix(1, 0, 0, 0), b63.matrix(0, 0, 0, 1)
PAIRS = ((0, -1), (1, -1), (1, 1), (2, 1))
LAWS = ('output_root', 'adjacent_packet')
R0 = b64.IDENTITY_ROTATION


def exact_matrix(x, n):
    return (isinstance(x, (tuple, list)) and len(x) == n
            and all(isinstance(row, (tuple, list)) and len(row) == n for row in x)
            and all(isinstance(a, b63.ExactComplex)
                    and type(a.real) in (int, F) and type(a.imag) in (int, F)
                    for row in x for a in row))


def determinant(x):
    n = len(x)
    result = Z
    for perm in permutations(range(n)):
        term = ONE
        for i, j in enumerate(perm):
            term = term * x[i][j]
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n))
        result = result + (-term if inversions % 2 else term)
    return result


def density4(x):
    """Exact Gaussian-rational Hermitian, trace-one, all-principal-minor PSD."""
    if not exact_matrix(x, 4):
        return False
    if any(x[i][j] != x[j][i].conjugate() for i in range(4) for j in range(4)):
        return False
    if sum((x[i][i] for i in range(4)), Z) != ONE:
        return False
    for k in range(1, 5):
        for idx in combinations(range(4), k):
            d = determinant(tuple(tuple(x[i][j] for j in idx) for i in idx))
            if d.imag != 0 or d.real < 0:
                return False
    return True


def kron(a, b):
    return tuple(tuple(a[i//2][j//2]*b[i%2][j%2] for j in range(4)) for i in range(4))


def diagonal(values):
    return tuple(tuple(b63.z(values[i]) if i == j else Z for j in range(4)) for i in range(4))


def trace_product(a, b):
    value = sum((a[i][j]*b[j][i] for i in range(4) for j in range(4)), Z)
    if value.imag != 0:
        raise ValueError('nonreal trace product')
    return value.real


def effects(rotation):
    menu = b64.rotated_menus(rotation)[0]
    return (kron(P0, b63.IDENTITY),) + tuple(
        kron(P1, b63.matrix_multiply(b63.rotate_hermitian(rotation, P0 if s == -1 else P1), menu[h]))
        for h, s in PAIRS)


def weights(omega, rotation):
    if not density4(omega) or rotation not in b64.ROTATIONS:
        raise ValueError('outside exact density/frame domain')
    return tuple(trace_product(omega, e) for e in effects(rotation))


def signed_rotation(rotation, sign):
    if sign not in (-1, 1):
        raise ValueError('sign')
    return rotation if sign == 1 else tuple(tuple(rotation[i][j]*(-1 if j in (0, 2) else 1) for j in range(3)) for i in range(3))


def candidate_records(law, rotation, pair):
    """The actual two original carrier dictionaries, with root at the origin."""
    if law not in LAWS or rotation not in b64.ROTATIONS or pair not in PAIRS:
        raise ValueError('candidate arguments')
    h, s = pair
    effect = b64.rotated_menus(rotation)[0][h]
    tau = b63.normalized_effect_state(effect)
    successor = signed_rotation(rotation, s)
    head = b64.context_carrier('head', tau, successor, 1, 1)
    if law == 'output_root':
        root = b63.program_carrier(tau, b64.rotate_coord(rotation, b64.BASE_FRAME), 40+PAIRS.index(pair))
        site = b64.rotate_coord(successor, b64.BASE_FORWARD)
    else:
        root = b63.outcome_carrier(effect, h+1)
        site = b64.neg(b64.rotate_coord(rotation, b64.BASE_TRANSVERSE))
    return {b64.ORIGIN: root, site: head}


@dataclass(frozen=True)
class Outcome:
    key: object
    weight: F
    status: str
    records: tuple
    spent: bool


def distribution(law, omega, rotation=R0, records=None, *, context_valid=True, output_valid=True, spent=False):
    """Total on the explicitly typed patch interface; invalid input refuses.

    Zero-weight branches remain part of a normalized distribution. No clipping
    or normalization repair is performed. Readiness bits are supplied metadata,
    not a proof of a physical preparation or physical output compiler.
    """
    if records is None:
        records = {}
    if not isinstance(records, dict) or any(
            not isinstance(site, tuple) or len(site) != 3 or any(type(a) is not int for a in site)
            or not exact_matrix(carrier, 2) for site, carrier in records.items()):
        raise ValueError('records must be a finite integer-site / exact-carrier dictionary')
    old = tuple(sorted(records.items()))
    refusal = (Outcome('refusal', F(1), 'refusal', old, True),)
    if (law not in LAWS or rotation not in b64.ROTATIONS or not density4(omega)
            or type(context_valid) is not bool or type(output_valid) is not bool or type(spent) is not bool
            or not context_valid or not output_valid or spent):
        return refusal
    assignments = [candidate_records(law, rotation, pair) for pair in PAIRS]
    if any(site in records for packet in assignments for site in packet):
        return refusal
    w = weights(omega, rotation)
    if any(v < 0 for v in w) or sum(w, F(0)) != 1:
        raise ArithmeticError('effect normalization/domain invariant failed')
    result = [Outcome('no_record', w[0], 'no_record', old, True)]
    for pair, value, packet in zip(PAIRS, w[1:], assignments):
        result.append(Outcome(pair, value, 'formed', tuple(sorted({**records, **packet}.items())), True))
    return tuple(result)


def realize(outcomes, key):
    for item in outcomes:
        if item.key == key and item.weight > 0:
            return item
    raise ValueError('unavailable or zero-weight realized branch')


def index(p, m, b, r, a):
    return p | (m << 1) | (b << 2) | (r << 3) | (a << 4)


def dilation(bridge=True):
    """Parent analytic isometry; columns b=P+2M, external columns a=2P+M."""
    v = np.zeros((32, 4), complex)
    for bits, col, square in (
            ((0,0,0,0,0),0,F(1)), ((0,1,0,0,0),2,F(1)),
            ((1,0,0,0,0),1,F(1,2)), ((1,0,1,0,0),1,F(5,14)),
            ((1,0,1,1,1),1,F(1,7)), ((1,1,0,0,0),3,F(1,7)),
            ((1,1,0,1,1),3,F(2,35)), ((1,1,1,1,0),3,F(4,5))):
        v[index(*bits), col] = np.sqrt(float(square))
    s = np.eye(4)[:, [0, 2, 1, 3]]
    return v @ (s if bridge else np.eye(4))


def actual_channels(x, bridge=True):
    y = dilation(bridge) @ x @ dilation(bridge).conj().T
    no_b = np.zeros((4, 4), complex)
    for ml in range(2):
        for mr in range(2):
            no_b[2*ml, 2*mr] = sum(y[index(0,ml,b,r,a), index(0,mr,b,r,a)]
                                   for b in range(2) for r in range(2) for a in range(2))
    s = np.eye(4)[:, [0, 2, 1, 3]]
    fine = []
    for h, sign in PAIRS:
        m = (sign+1)//2; b = h-m
        fine.append(np.array([[sum(y[index(1,m,b,r,a),index(1,m,b,t,a)] for a in range(2))
                              for t in range(2)] for r in range(2)]))
    return (s.T @ no_b @ s, *fine)


def expected_channels(x):
    p = np.diag([1, 1, 0, 0])
    menu = b63.MENUS[0]
    return (p @ x @ p,) + tuple(
        x[2+(s+1)//2, 2+(s+1)//2] * float(menu[h][(s+1)//2][(s+1)//2].real)
        * b63.to_numpy(b63.normalized_effect_state(menu[h])) for h,s in PAIRS)


def channel_residual(bridge=True):
    worst = 0.0
    for i in range(4):
        for j in range(4):
            x = np.zeros((4,4), complex);x[i,j] = 1
            actual, expected = actual_channels(x, bridge), expected_channels(x)
            worst = max(worst, *(float(np.max(np.abs(a-b))) for a,b in zip(actual, expected)))
            for h in range(3):
                a = sum((actual[k+1] for k,pair in enumerate(PAIRS) if pair[0] == h), np.zeros((2,2),complex))
                b = sum((expected[k+1] for k,pair in enumerate(PAIRS) if pair[0] == h), np.zeros((2,2),complex))
                worst = max(worst, float(np.max(np.abs(a-b))))
    return worst


def root_site(law, records):
    if law == 'output_root':
        found = []
        for site, carrier in records.items():
            _rho, frame, code = b63.decode_program(carrier)
            if code.denominator == 1 and 40 <= code <= 43 and tuple(frame) in b64.FRAME_TO_ROTATION:
                found.append(site)
    else:
        found = []
        for site, carrier in records.items():
            dec = b64.outcome_decode(carrier)
            if dec is None:
                continue
            effect, h = dec
            predecessors = [q for d in b64.DIRECTIONS if (q := b64.add(site,d)) in records
                            and (c := b64.decode_context(records[q])) is not None and c.role == 'relay'
                            and b64.add(q,c.forward) == site and b64.rotated_menus(c.rotation)[c.menu][h] == effect]
            if not predecessors:
                found.append(site)
    return found[0] if len(found) == 1 else None


def geometry(law, records):
    root = root_site(law, records)
    if root is None:
        return None
    heads = [(site,c) for site, carrier in records.items()
             if (c := b64.decode_context(carrier)) is not None and c.role == 'head']
    distance = min((sum(abs(a-b) for a,b in zip(site,root)) for site,_ in heads), default=None)
    nearest = [(site,c) for site,c in heads if sum(abs(a-b) for a,b in zip(site,root)) == distance]
    if len(nearest) != 1:
        return None
    site,c = nearest[0];d = tuple(a-b for a,b in zip(site,root))
    return distance, sum(a*b for a,b in zip(d,c.forward)), sum(a*b for a,b in zip(d,c.transverse))


def continue_one(records):
    before = dict(records)
    kinds = []
    for kind in ('relay', 'outcome', 'finalize'):
        active = b64.active_sites(records)
        if len(active) != 1:
            raise ValueError('not an isolated single front')
        target, dist = next(iter(active.items()))
        if dist.kind != kind or not dist.normalized:
            raise ValueError('invalid local stage')
        _, carrier = b64.choose(dist, F(1,3) if kind == 'outcome' else F(0))
        records = b64.append_one(records, target, carrier);kinds.append(kind)
    if any(records.get(site) != carrier for site,carrier in before.items()):
        raise ArithmeticError('overwrite')
    return records, tuple(kinds)
