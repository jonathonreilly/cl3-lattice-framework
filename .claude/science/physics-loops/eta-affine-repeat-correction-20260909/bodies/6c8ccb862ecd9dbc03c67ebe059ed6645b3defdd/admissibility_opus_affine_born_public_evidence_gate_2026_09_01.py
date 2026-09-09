#!/usr/bin/env python3
"""Block 35: public affine/Born evidence and sufficient-bridge gate.

This runner tests only the assumptions and formulas visible in canonical-main
axiom sources and PR #7814's sole public evidence blob.  It neither reviews nor
lands that PR and makes no claim about stronger definitions in its unavailable
archive.
"""

from __future__ import annotations

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
CANONICAL_MAIN = "aa7338d1fbc34a4b92205182b26793194e4727b6"
PR_HEAD = "9b5dbb97455a1c26783ad5b4c154d5edea123fdf"
PR_PATH = ".claude/science/opus-direct-20260827/LANDING_CORE.md"
MINIMAL_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PREDECESSOR_NOTE = "docs/work_history/repo/review_feedback/OPERATIONAL_QUOTIENT_BORN_AFFINITY_CYCLE20_NOTE_2026-07-14.md"
PREDECESSOR_RUNNER = "scripts/operational_quotient_born_affinity_cycle20_2026_07_14.py"
PACKET = ".claude/science/physics-loops/toe-source-eta-ownership-block35-opus-affine-born-evidence-gate-20260901"
POSTSTATE_PATH = f"{PACKET}/POSTEXECUTION_STATE.yaml"
TOE_UPDATE_PATH = f"{PACKET}/TOE_LANE_UPDATE.md"
EXPECTED_SHA256 = {
    MINIMAL_PATH: "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753",
    REGISTRY_PATH: "615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37",
    f"{PR_HEAD}:{PR_PATH}": "1c01baa66f3f87df6f4d4dba0ffed378582e37189d0b848a4c8c8b3588a4572e",
    PREDECESSOR_NOTE: "dfb44a519055f5099ff03f571271ba2e416da705976899ac877e7121551047b4",
    PREDECESSOR_RUNNER: "d5cc88a558b769d1291d4c8da629b2038078d41ca9ad0e0c91542e0a34440724",
    POSTSTATE_PATH: "4ddabf05fd542593148de6fd79091af4614e80a1f802f0667a2da763db81f4f9",
    TOE_UPDATE_PATH: "155961ed6d1e9de78c37f30c6cefe6e686994ab93b42bab81b0fca77d94a8c22",
}

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


def git_bytes(spec: str) -> bytes:
    return subprocess.run(
        ["git", "show", spec],
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout


def git_lines(*args: str) -> list[str]:
    out = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout
    return [line for line in out.splitlines() if line]


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


def gate_public_inputs() -> None:
    minimal = git_bytes(f"{CANONICAL_MAIN}:{MINIMAL_PATH}")
    registry = git_bytes(f"{CANONICAL_MAIN}:{REGISTRY_PATH}")
    landing = git_bytes(f"{PR_HEAD}:{PR_PATH}")
    predecessor_note = git_bytes(f"{CANONICAL_MAIN}:{PREDECESSOR_NOTE}")
    predecessor_runner = git_bytes(f"{CANONICAL_MAIN}:{PREDECESSOR_RUNNER}")
    poststate = (ROOT / POSTSTATE_PATH).read_bytes()
    toe_update = (ROOT / TOE_UPDATE_PATH).read_bytes()
    actual = {
        MINIMAL_PATH: sha256(minimal),
        REGISTRY_PATH: sha256(registry),
        f"{PR_HEAD}:{PR_PATH}": sha256(landing),
        PREDECESSOR_NOTE: sha256(predecessor_note),
        PREDECESSOR_RUNNER: sha256(predecessor_runner),
        POSTSTATE_PATH: sha256(poststate),
        TOE_UPDATE_PATH: sha256(toe_update),
    }
    tree = git_lines(
        "ls-tree", "-r", "--name-only", PR_HEAD, ".claude/science/opus-direct-20260827"
    )
    needles = [
        b"covariance + Markov + triangle-freeness",
        b"Hammersley",
        "φ = a +".encode(),
        b"opposite",
        b"0.5545",
        "W₄".encode(),
    ]
    ok = actual == EXPECTED_SHA256 and tree == [PR_PATH] and all(
        needle in landing for needle in needles
    )
    emit(
        ok,
        "public_evidence_identity",
        "seven canonical/public/result-state evidence hashes match; PR tree contains LANDING_CORE only",
    )


def gate_current_axiom_scope() -> None:
    minimal = git_bytes(f"{CANONICAL_MAIN}:{MINIMAL_PATH}").decode()
    minimal_flat = " ".join(minimal.split())
    registry = json.loads(git_bytes(f"{CANONICAL_MAIN}:{REGISTRY_PATH}"))
    required = [
        "the distribution's extensional form and values are not specified by this memo",
        'Finite additivity, a named scalar collection functional `I`, and an assigned',
        "The distribution's form and values, dynamics, readout contexts",
        "A readout value is determined by record content alone",
    ]
    current_path = registry["nodes"]["minimal_axioms"]["current_path"]
    registry_note = registry["nodes"]["minimal_axioms"]["note"]
    registry_current = (
        "specific distribution form or values" in registry_note
        and "a site with no record cannot be read" in registry_note
        and "scalar readout I is additive" not in registry_note
    )
    ok = current_path == MINIMAL_PATH and all(x in minimal_flat for x in required) and registry_current
    emit(
        ok,
        "current_axiom_form_value_and_additivity_boundary",
        "canonical source and registry leave distribution form/values open and exclude removed scalar Record additivity; branch-stale prose is not used",
    )


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


def gate_operational_predecessor_boundary() -> None:
    note = (ROOT / PREDECESSOR_NOTE).read_bytes()
    runner = (ROOT / PREDECESSOR_RUNNER).read_bytes()
    process = subprocess.run(
        [sys.executable, str(ROOT / PREDECESSOR_RUNNER)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    output = process.stdout
    exact_failure = output.count("\nFAIL ") == 1 and "FAIL A live foundation needle: scalar readout i is additive" in output
    positive_core = all(
        needle in output
        for needle in (
            "PASS B randomized preparations pair affinely for every test",
            "PASS D deleting physical mixing permits nonaffinity",
            "PASS F exact conditional reset gives vanishing IID frequency variance",
            "PASS=118 FAIL=1",
        )
    )
    authority_boundary = all(
        needle in note
        for needle in (
            b"Authority:** none",
            b"Physical Randomization Gives Affinity",
            b"trial/reset corpus is separate",
        )
    )
    ok = (
        sha256(note) == EXPECTED_SHA256[PREDECESSOR_NOTE]
        and sha256(runner) == EXPECTED_SHA256[PREDECESSOR_RUNNER]
        and process.returncode == 1
        and exact_failure
        and positive_core
        and authority_boundary
        and not process.stderr
    )
    emit(
        ok,
        "operational_randomizer_predecessor_current_boundary",
        "authority-free predecessor reruns 118/1: affinity/reset controls pass and only the removed scalar-Record-additivity needle fails",
    )


def gate_hostile_mutations() -> None:
    # Each item is a deliberately false promotion or algebraic corruption.  A
    # successful gate rejects every one from recomputed evidence.  No mutation
    # verdict is represented by a literal False constant.
    u = sp.symbols("u", real=True)
    k = sp.Rational(2, 3)
    minimal = git_bytes(f"{CANONICAL_MAIN}:{MINIMAL_PATH}").decode()
    registry = json.loads(git_bytes(f"{CANONICAL_MAIN}:{REGISTRY_PATH}"))
    registry_note = registry["nodes"]["minimal_axioms"]["note"]
    landing = git_bytes(f"{PR_HEAD}:{PR_PATH}")
    landing_lower = landing.lower()
    tree = git_lines(
        "ls-tree", "-r", "--name-only", PR_HEAD, ".claude/science/opus-direct-20260827"
    )
    poststate = (ROOT / POSTSTATE_PATH).read_text()
    toe_update = (ROOT / TOE_UPDATE_PATH).read_text()
    public_executables = [path for path in tree if Path(path).suffix == ".py"]

    summaries = [
        (*partition_and_edge_correlation(lam), *partition_and_edge_correlation(-lam))
        for lam in (Fraction(1), Fraction(2, 3), Fraction(1, 5))
    ]
    normalized_mixture_gap = sp.factor(
        sp.cosh(k) / (2 * sp.cosh(k) + 4) - sp.Rational(1, 6)
    )
    target_correlation = Fraction(1109, 2000)  # quoted decimal 0.5545
    no_triangles = all(
        not all(
            tuple(sorted(edge)) in {tuple(sorted(e)) for e in C4_EDGES}
            for edge in ((a, b), (a, c), (b, c))
        )
        for a, b, c in itertools.combinations(range(4), 3)
    )

    mutations = {
        "exp_is_affine": sp.diff(sp.exp(k * u), u, 2) == 0,
        "quadratic_is_affine": sp.diff(1 + u**2 / 2, u, 2) == 0,
        "orthogonal_zero_endpoint_forces_affine": sp.diff(
            (1 + u) * (1 + sp.Rational(1, 8) * (1 - u**2)), u, 2
        ) == 0,
        "constant_kernel_varies": sp.exp(0 * 1) != sp.exp(0 * -1),
        "mixture_affinity_for_exp": sp.simplify(
            sp.cosh(k) / (2 * sp.cosh(k) + 4) - sp.Rational(1, 6)
        )
        == 0,
        "born_equals_antiborn_at_same": (1 + 1) == (1 - 1),
        "born_equals_antiborn_at_orthogonal": (1 - 1) == (1 + 1),
        "stagger_selects_positive_sign": any(z_plus > z_minus for z_plus, _, z_minus, _ in summaries),
        "partition_equivalence_selects_sign": any(z_plus != z_minus for z_plus, _, z_minus, _ in summaries),
        "public_quoted_05545_reproduced": bool(public_executables)
        and any(abs(c_plus) == target_correlation for _, c_plus, _, _ in summaries),
        "public_gravity_operator_derived": bool(public_executables)
        and b"operator derivation" in landing_lower,
        "public_gravity_source_attached": bool(public_executables)
        and b"source attachment" in landing_lower,
        "public_metric_dynamics_derived": bool(public_executables)
        and b"metric dynamics" in landing_lower,
        "public_archive_present_in_pr_tree": any(
            path.endswith("POSITIVE_PATH.md") or Path(path).suffix == ".py"
            for path in tree
        ),
        "current_record_additivity": "scalar readout I is additive" in minimal
        or "scalar readout I is additive" in registry_note,
        "event_additivity_implies_affinity": normalized_mixture_gap == 0,
        "hammersley_clifford_implies_degree_one": no_triangles
        and sp.diff(sp.exp(k * u), u, 2) == 0,
        "public_block34_lambda_identified": all(
            needle in landing for needle in (b"Block 34", b"C_lambda", b"8ecca1f3")
        ),
        "current_premises_select_born": "Born weight values" in minimal
        and "remain outside axiom content" not in minimal,
        "packet_obligation_retired": "obligation_retirement_claimed: true" in poststate,
        "packet_toe_score_moved": "toe_score_movement_claimed: true" in poststate
        or "No score moves." not in toe_update,
    }
    rejected = sum(not bool(value) for value in mutations.values())
    source_tree = ast.parse(Path(__file__).read_text())
    mutation_dicts = [
        node.value
        for node in ast.walk(source_tree)
        if isinstance(node, ast.Assign)
        and any(isinstance(target, ast.Name) and target.id == "mutations" for target in node.targets)
        and isinstance(node.value, ast.Dict)
    ]
    literal_verdicts = [
        value
        for mapping in mutation_dicts
        for value in mapping.values
        if isinstance(value, ast.Constant) and isinstance(value.value, bool)
    ]
    ok = rejected == len(mutations) and len(mutation_dicts) == 1 and not literal_verdicts
    emit(
        ok,
        "designated_hostile_mutations",
        f"{rejected}/{len(mutations)} algebra, evidence, scope, gravity, and governance promotions rejected from computed predicates; 0 literal Boolean verdicts",
    )


def gate_identity_mutations() -> None:
    actual = [
        sha256(git_bytes(f"{CANONICAL_MAIN}:{MINIMAL_PATH}")),
        sha256(git_bytes(f"{CANONICAL_MAIN}:{REGISTRY_PATH}")),
        sha256(git_bytes(f"{PR_HEAD}:{PR_PATH}")),
        sha256(git_bytes(f"{CANONICAL_MAIN}:{PREDECESSOR_NOTE}")),
        sha256(git_bytes(f"{CANONICAL_MAIN}:{PREDECESSOR_RUNNER}")),
        sha256((ROOT / POSTSTATE_PATH).read_bytes()),
        sha256((ROOT / TOE_UPDATE_PATH).read_bytes()),
    ]
    expected = list(EXPECTED_SHA256.values())
    candidates = []
    for index, digest in enumerate(expected):
        for replacement in ("0", "f"):
            if digest[0] == replacement:
                replacement = "e"
            mutant = expected.copy()
            mutant[index] = replacement + digest[1:]
            candidates.append(mutant)
    rejected = sum(candidate != actual for candidate in candidates)
    ok = actual == expected and rejected == len(candidates)
    emit(
        ok,
        "identity_mutations",
        f"baseline 7/7 content identities match and {rejected}/{len(candidates)} digest corruptions fail closed",
    )


def main() -> int:
    gates: Iterable[Callable[[], None]] = (
        gate_public_inputs,
        gate_current_axiom_scope,
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
        gate_operational_predecessor_boundary,
        gate_hostile_mutations,
        gate_identity_mutations,
    )
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
        "TERMINAL: PUBLIC-NAMED-COVARIANCE-MARKOV-TRIANGLE-FREE-HAMMERSLEY-CLIFFORD-PLUS-CURRENT-RECORD-CONDITIONS-ALLOW-STRICTLY-POSITIVE-NONLINEAR-DOT-PRODUCT-KERNELS;SEPARATE-PREPARATION-AFFINITY-PLUS-SIMULTANEOUS-QUBIT-COVARIANCE-IS-SUFFICIENT-FOR-THE-AFFINE-FAMILY-BUT-IS-NOT-CURRENT-AXIOM-CONTENT;WITHIN-THAT-AFFINE-FAMILY-ORTHOGONAL-EXCLUSION-SELECTS-THE-BORN-RAY-WHILE-SAME-STATE-EXCLUSION-SELECTS-ANTI-BORN-BUT-WITHOUT-AFFINITY-A-MONOTONE-NONLINEAR-ORTHOGONAL-ZERO-FAMILY-SURVIVES-AND-COMMON-SCALE-CANCELS;BIPARTITE-STAGGERING-EXACTLY-EXCHANGES-THE-SIGNS-AND-IS-A-DISCRIMINATOR-NOT-A-SELECTOR;DISPLAYED-GRAVITY-ARITHMETIC-REPRODUCES-BUT-THE-UNLANDED-DERIVATIONS-OPERATOR-SOURCE-AND-DYNAMICS-DO-NOT;PUBLIC-EVIDENCE-BOUNDARY-INCOMPLETE-NO-TOE-MOVEMENT"
    )
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
