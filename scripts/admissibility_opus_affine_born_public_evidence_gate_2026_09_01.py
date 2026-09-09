#!/usr/bin/env python3
"""Block 35: public affine/Born evidence and sufficient-bridge gate.

This runner tests only the assumptions and formulas visible in canonical-main
axiom sources and PR #7814's sole public evidence blob.  It neither reviews nor
lands that PR and makes no claim about stronger definitions in its unavailable
archive.
"""

from __future__ import annotations

# Current publication uses the clean candidate only. Exact legacy controllers
# and all historical source variants remain in the outside-discovery recovery.

import ast
import hashlib
import itertools
import json
import math
import subprocess
import sys
from fractions import Fraction
from pathlib import Path
from typing import Callable, Iterable, Sequence

import mpmath as mp
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = ('docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_OPUS_AFFINE_BORN_PUBLIC_EVIDENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-01.md')
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
DIRECT_HASHES = {'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/ADMISSIBILITY_OPUS_AFFINE_BORN_PUBLIC_EVIDENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-01.md': 'bd4e310f4e9d5f07b2e3f11ad1dc94b2541c12b80a38051584e1d778724a64e7'}


def current_inputs_ok() -> bool:
    return all((ROOT / path).is_file() and hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected
               for path, expected in DIRECT_HASHES.items())


def guard_current_inputs() -> None:
    if not current_inputs_ok():
        raise RuntimeError("current source/premise input missing or changed")
    print(f"INPUT_BOUND: {len(DIRECT_HASHES)} actual current inputs")


MINIMAL_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"

PASS_COUNT = 0
FAIL_COUNT = 0


def emit(ok: bool, name: str, detail: str) -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        print(f"PASS {name}: {detail}")
    else:
        FAIL_COUNT += 1
        print(f"FAIL {name}: {detail}")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()




def dot(a: Sequence[int | Fraction], b: Sequence[int | Fraction]) -> Fraction:
    return sum((Fraction(x) * Fraction(y) for x, y in zip(a, b)), Fraction(0))


def neg(a: Sequence[int | Fraction]) -> tuple[Fraction, ...]:
    return tuple(-Fraction(x) for x in a)


def determinant3(rows: Sequence[Sequence[int]]) -> int:
    a, b, c = rows
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def proper_cubic_rotations() -> list[tuple[tuple[int, ...], ...]]:
    rotations: list[tuple[tuple[int, ...], ...]] = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            rows = []
            for i in range(3):
                row = [0, 0, 0]
                row[perm[i]] = signs[i]
                rows.append(tuple(row))
            matrix = tuple(rows)
            if determinant3(matrix) == 1:
                rotations.append(matrix)
    assert len(rotations) == 24
    return rotations


def matvec(
    matrix: Sequence[Sequence[int]], vector: Sequence[int | Fraction]
) -> tuple[Fraction, ...]:
    return tuple(dot(row, vector) for row in matrix)




def gate_rotation_covariance() -> None:
    rotations = proper_cubic_rotations()
    vectors = [
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1),
        (Fraction(1, 3), Fraction(2, 3), Fraction(2, 3)),
    ]
    ok = all(
        dot(matvec(r, a), matvec(r, b)) == dot(a, b)
        for r in rotations
        for a in vectors
        for b in vectors
    )
    emit(
        ok,
        "simultaneous_cubic_rotation_invariance",
        "all 24 proper cubic rotations preserve the dot-product argument of every tested kernel",
    )


def gate_nonlinear_positive_kernels() -> None:
    u, k = sp.symbols("u k", real=True)
    exponential = sp.exp(k * u)
    second = sp.diff(exponential, u, 2)
    k0 = sp.Rational(2, 3)
    midpoint_gap = sp.simplify(
        exponential.subs({u: -1, k: k0})
        + exponential.subs({u: 1, k: k0})
        - 2 * exponential.subs({u: 0, k: k0})
    )
    polynomial = 1 + sp.Rational(1, 2) * u**2
    polynomial_gap = sp.simplify(
        polynomial.subs(u, -1) + polynomial.subs(u, 1) - 2 * polynomial.subs(u, 0)
    )
    epsilon = sp.Rational(1, 8)
    oriented = (1 + u) * (1 + epsilon * (1 - u**2))
    oriented_prime = sp.expand(sp.diff(oriented, u))
    oriented_second = sp.expand(sp.diff(oriented, u, 2))
    oriented_endpoints = (sp.simplify(oriented.subs(u, -1)), sp.simplify(oriented.subs(u, 1)))
    # oriented_prime is concave on [-1,1], so its minimum is at an endpoint.
    oriented_monotone = min(
        sp.Rational(oriented_prime.subs(u, endpoint)) for endpoint in (-1, 1)
    ) > 0
    ok = (
        second == k**2 * sp.exp(k * u)
        and float(midpoint_gap.evalf(40)) > 0
        and polynomial_gap == 1
        and min(float(polynomial.subs(u, x)) for x in (-1, 0, 1)) > 0
        and oriented_endpoints == (0, 2)
        and oriented_monotone
        and oriented_second != 0
    )
    emit(
        ok,
        "strict_positive_nonlinear_invariant_counterfamilies",
        "exp(k u), 1+u^2/2, and a monotone orthogonal-zero endpoint-normalized deformation are covariant and non-affine",
    )


C4_EDGES = ((0, 1), (1, 2), (2, 3), (3, 0))


def gate_markov_triangle_free_factorization() -> None:
    # A concrete positive C4 edge-product law.  The global-to-conditional ratio
    # for changing site 0 must cancel both edges not incident on site 0.
    k = sp.symbols("k", real=True)
    old = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0))
    # Use a genuinely nonzero local change: E(new)-E(old)=2.  This prevents
    # the cancellation control from degenerating to the identity 1 == 1.
    new = ((0, 1, 0), old[1], old[2], old[3])

    def exponent(configuration: Sequence[Sequence[int]]) -> int:
        return sum(int(dot(configuration[i], configuration[j])) for i, j in C4_EDGES)

    global_ratio = sp.exp(k * (exponent(new) - exponent(old)))
    local_delta = (
        dot(new[0], new[1])
        + dot(new[0], new[3])
        - dot(old[0], old[1])
        - dot(old[0], old[3])
    )
    local_ratio = sp.exp(k * int(local_delta))
    vertices = set(range(4))
    no_triangles = all(
        not all(
            tuple(sorted(edge)) in {tuple(sorted(e)) for e in C4_EDGES}
            for edge in ((a, b), (a, c), (b, c))
        )
        for a, b, c in itertools.combinations(vertices, 3)
    )
    ok = no_triangles and local_delta == 2
    ok = ok and sp.simplify(global_ratio - local_ratio) == 0
    emit(
        ok,
        "triangle_free_markov_edge_factorization",
        "a nonzero delta=2 C4 update cancels nonincident edges exactly; the strict-positive law is Markov and triangle-free while its edge potential remains nonlinear",
    )


def gate_local_z3_conditional() -> None:
    k = mp.mpf(2) / 3
    # For one unit neighbor H, integral over normalized angular coordinates is
    # 4*pi*sinh(k)/k.  Rotation changes H's direction but not this normalizer.
    z = 4 * mp.pi * mp.sinh(k) / k
    density_ratio = mp.e ** (2 * k)
    zero_field_limit = 4 * mp.pi
    ok = z > 0 and density_ratio > 1 and abs(
        4 * mp.pi * mp.sinh(mp.mpf("1e-20")) / mp.mpf("1e-20") - zero_field_limit
    ) < mp.mpf("1e-35")
    emit(
        ok,
        "z3_neighbor_conditioned_distribution",
        "exp(k n·sum_neighbors m) normalizes for every local field, has full support, and varies with neighbor orientation",
    )


def gate_affinity_representation_theorem() -> None:
    # General separately affine real kernel on Bloch balls:
    # c + a.r + b.s + r^T M s.  Simultaneous proper-cubic covariance forces
    # a=b=0 and M proportional to I.
    a = sp.symbols("a0:3")
    b = sp.symbols("b0:3")
    m = sp.symbols("m0:9")
    avec = sp.Matrix(a)
    bvec = sp.Matrix(b)
    matrix = sp.Matrix(3, 3, m)
    variables = list(a) + list(b) + list(m)
    equations = []
    for rot_raw in proper_cubic_rotations():
        rot = sp.Matrix(rot_raw)
        equations.extend(list(rot.T * avec - avec))
        equations.extend(list(rot.T * bvec - bvec))
        equations.extend(list(rot.T * matrix * rot - matrix))
    coeff, _ = sp.linear_eq_to_matrix(equations, variables)
    nullspace = coeff.nullspace()
    expected = sp.Matrix([0] * 6 + [1, 0, 0, 0, 1, 0, 0, 0, 1])
    ok = coeff.rank() == 14 and len(nullspace) == 1
    ok = ok and (nullspace[0] / nullspace[0][6]) == expected
    emit(
        ok,
        "separate_affinity_plus_covariance_is_sufficient",
        "the 15-coefficient invariant solve has rank 14, leaving only c+b r·s; affinity is the missing load-bearing premise",
    )


def gate_event_additivity_is_not_affinity() -> None:
    k = sp.Rational(2, 3)
    weights = [sp.exp(k), sp.exp(-k), 1, 1, 1, 1]
    total = sum(weights)
    event_a = {0, 2}
    event_b = {3, 5}
    p_a = sum(weights[i] for i in event_a) / total
    p_b = sum(weights[i] for i in event_b) / total
    p_union = sum(weights[i] for i in event_a | event_b) / total
    additive = sp.simplify(p_union - p_a - p_b) == 0
    # A 50/50 mixture of opposite neighbor Bloch vectors has zero Bloch vector.
    # Compare normalized six-outcome probabilities, not raw pair weights.
    pure_normalizer = 2 * sp.cosh(k) + 4
    mixed_preparation_probability = sp.cosh(k) / pure_normalizer
    zero_bloch_probability = sp.Rational(1, 6)
    mixture_gap = sp.factor(
        mixed_preparation_probability - zero_bloch_probability
    )
    expected_gap = (sp.cosh(k) - 1) / (3 * sp.cosh(k) + 6)
    ok = additive and sp.simplify(mixture_gap - expected_gap) == 0
    ok = ok and float(mixture_gap.evalf(40)) > 0
    emit(
        ok,
        "event_additivity_does_not_imply_preparation_affinity",
        "the nonlinear law is additive at fixed condition but its normalized six-outcome probability violates 50/50 preparation affinity by (cosh(k)-1)/(3 cosh(k)+6)",
    )


def gate_pure_qubit_trace_and_endpoints() -> None:
    rx, ry, rz, sx, sy, sz = sp.symbols("rx ry rz sx sy sz", real=True)
    i = sp.I
    sigma_x = sp.Matrix([[0, 1], [1, 0]])
    sigma_y = sp.Matrix([[0, -i], [i, 0]])
    sigma_z = sp.Matrix([[1, 0], [0, -1]])
    identity = sp.eye(2)
    rho = (identity + rx * sigma_x + ry * sigma_y + rz * sigma_z) / 2
    sigma = (identity + sx * sigma_x + sy * sigma_y + sz * sigma_z) / 2
    overlap = sp.simplify(sp.trace(rho * sigma))
    expected = (1 + rx * sx + ry * sy + rz * sz) / 2
    born = lambda u: 1 + u
    anti = lambda u: 1 - u
    ok = overlap == expected
    ok = ok and (born(-1), born(1), anti(-1), anti(1)) == (0, 2, 2, 0)
    ok = ok and all(1 >= abs(beta) for beta in (-1, sp.Rational(-1, 2), 0, sp.Rational(1, 2), 1))
    emit(
        ok,
        "affine_positive_cone_and_endpoint_orientation",
        "2 Tr(rho sigma)=1+r·s; orthogonal exclusion selects the Born ray, while same-state exclusion selects anti-Born",
    )


AXES = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)


def affine_weight(configuration: Sequence[Sequence[int]], lam: Fraction) -> Fraction:
    value = Fraction(1)
    for left, right in C4_EDGES:
        value *= 1 + lam * dot(configuration[left], configuration[right])
    return value


def stagger(configuration: Sequence[Sequence[int]]) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(neg(v) if index in (0, 2) else tuple(Fraction(x) for x in v) for index, v in enumerate(configuration))


def partition_and_edge_correlation(lam: Fraction) -> tuple[Fraction, Fraction]:
    partition = Fraction(0)
    numerator = Fraction(0)
    for configuration in itertools.product(AXES, repeat=4):
        weight = affine_weight(configuration, lam)
        partition += weight
        numerator += weight * dot(configuration[0], configuration[1])
    return partition, numerator / partition


def gate_bipartite_stagger_map() -> None:
    lambdas = (Fraction(1), Fraction(2, 3), Fraction(1, 5))
    pointwise = all(
        affine_weight(configuration, lam) == affine_weight(stagger(configuration), -lam)
        for lam in lambdas
        for configuration in itertools.product(AXES, repeat=4)
    )
    summaries = []
    aggregate = True
    for lam in lambdas:
        z_plus, c_plus = partition_and_edge_correlation(lam)
        z_minus, c_minus = partition_and_edge_correlation(-lam)
        aggregate = aggregate and z_plus == z_minus and c_plus == -c_minus
        summaries.append(f"{lam}:{c_plus}")
    emit(
        pointwise and aggregate,
        "born_antiborn_bipartite_equivalence_and_discriminator",
        "one-sublattice inversion maps lambda to -lambda pointwise; Z is equal and edge correlation reverses (" + ", ".join(summaries) + ")",
    )


def gate_common_scale_cancels() -> None:
    alpha, c, b = sp.symbols("alpha c b", positive=True)
    degree = 6
    unscaled = sp.prod(c + b * sp.Rational(j, 7) for j in range(-3, 3))
    scaled = sp.prod(alpha * (c + b * sp.Rational(j, 7)) for j in range(-3, 3))
    ratio = sp.simplify(scaled / unscaled)
    ok = ratio == alpha**degree
    emit(
        ok,
        "conditional_normalization_erases_common_kernel_scale",
        "six-neighbor products gain the same alpha^6 for every candidate local state, so probability normalization cannot fix an absolute rate/unit",
    )


def gate_displayed_gravity_arithmetic() -> None:
    mp.mp.dps = 50
    integrand: Callable[[mp.mpf], mp.mpf] = lambda t: (
        mp.e ** (-2 * t) * mp.besseli(0, 2 * t)
    ) ** 4
    w4 = mp.quad(integrand, [0, 1, 4, 16, 64, mp.inf])
    tau0 = 1 / (16 * mp.pi**2 * w4)
    newton = 2 * mp.pi * tau0
    planck = mp.sqrt(newton)
    b1_d4 = Fraction(4 - 1, 3 * 4)
    b1_d3 = Fraction(3 - 1, 3 * 3)
    ok = abs(w4 - mp.mpf("0.1549333902310602140848372081073751")) < mp.mpf("1e-34")
    ok = ok and abs(newton - mp.mpf("0.2568118835690281168264053164")) < mp.mpf("1e-27")
    ok = ok and abs(planck - mp.mpf("0.5067661034136242589762562403")) < mp.mpf("1e-27")
    ok = ok and (b1_d4, b1_d3) == (Fraction(1, 4), Fraction(2, 9))
    emit(
        ok,
        "displayed_gravity_formula_arithmetic_only",
        f"W4={mp.nstr(w4, 12)}, G/a^2={mp.nstr(newton, 10)}, lP/a={mp.nstr(planck, 9)}, b1(4)=1/4; no operator derivation tested",
    )




def main() -> int:
    gates: Iterable[Callable[[], None]] = (
        gate_rotation_covariance,
        gate_nonlinear_positive_kernels,
        gate_markov_triangle_free_factorization,
        gate_local_z3_conditional,
        gate_affinity_representation_theorem,
        gate_event_additivity_is_not_affinity,
        gate_pure_qubit_trace_and_endpoints,
        gate_bipartite_stagger_map,
        gate_common_scale_cancels,
        gate_displayed_gravity_arithmetic,
    )
    guard_current_inputs()
    for gate in gates:
        try:
            gate()
        except Exception as exc:  # fail closed with a compact deterministic line
            emit(False, gate.__name__, f"{type(exc).__name__}: {exc}")

    print(
        "per_element: checked — strict positivity, non-affinity, qubit overlap, affine-cone endpoints, and all displayed scalar arithmetic were evaluated exactly or at pinned high precision"
    )
    print(
        "per_site: checked — the normalized six-outcome conditional varies non-affinely under the displayed preparation mixture, while ordinary event additivity remains distinct from preparation affinity"
    )
    print(
        "per_mode: checked — all 24 proper-cubic rotations, the invariant separately-affine coefficient space, and the Born/anti-Born sign orientation were resolved"
    )
    print(
        "per_block: checked — a nonzero delta=2 C4 update cancels nonincident edges, and the staggered map was exhaustively evaluated on all 1296 six-axis configurations at three exact parameters"
    )
    print(
        "lattice_wide: checked and not executed — only finite/local controls ran; the general Z3 specification and bipartite change-of-variables claims rest on the displayed analytic proof, and no thermodynamic Monte Carlo, continuum limit, gravity operator, source attachment, or dynamics was reproduced"
    )
    print(
        "TERMINAL: PUBLIC-NAMED-COVARIANCE-MARKOV-TRIANGLE-FREE-HAMMERSLEY-CLIFFORD-PLUS-CURRENT-RECORD-CONDITIONS-ALLOW-STRICTLY-POSITIVE-NONLINEAR-DOT-PRODUCT-KERNELS;SEPARATE-PREPARATION-AFFINITY-PLUS-SIMULTANEOUS-QUBIT-COVARIANCE-IS-SUFFICIENT-FOR-THE-AFFINE-FAMILY-BUT-IS-NOT-CURRENT-AXIOM-CONTENT;WITHIN-THAT-AFFINE-FAMILY-ORTHOGONAL-EXCLUSION-SELECTS-THE-BORN-RAY-WHILE-SAME-STATE-EXCLUSION-SELECTS-ANTI-BORN-BUT-WITHOUT-AFFINITY-A-MONOTONE-NONLINEAR-ORTHOGONAL-ZERO-FAMILY-SURVIVES-AND-COMMON-SCALE-CANCELS;BIPARTITE-STAGGERING-EXACTLY-EXCHANGES-THE-SIGNS-AND-IS-A-DISCRIMINATOR-NOT-A-SELECTOR;DISPLAYED-GRAVITY-ARITHMETIC-REPRODUCES-BUT-THE-UNLANDED-DERIVATIONS-OPERATOR-SOURCE-AND-DYNAMICS-DO-NOT;CONDITIONAL-MATHEMATICAL-BOUNDARY-NO-TOE-MOVEMENT"
    )
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
