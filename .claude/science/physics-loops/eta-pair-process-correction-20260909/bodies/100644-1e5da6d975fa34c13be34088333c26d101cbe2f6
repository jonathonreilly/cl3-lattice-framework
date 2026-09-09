#!/usr/bin/env python3
"""Block33: classical screening cause-persistence and renewal locus gate.

This runner independently recomputes the supplied Block32 q_lambda family.
It proves a narrow finite-classical result: if one unchanged screening cause
is used twice with the same conditional product response and fresh response
noise, equality with the product two-use law is possible for this family only
at lambda=0.  Explicit supplied-iid and coherent controls retain the complete
strict interval, and an exact depth-three counterhistory shows why pair
marginals alone do not establish renewal.

Nothing here derives a physical cause carrier, reset, source normalization,
gravity law, probability selector, or axiom change.
"""

from __future__ import annotations

import ast
import hashlib
import itertools
from dataclasses import dataclass, fields
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 300

PACKET_REL = (
    ".claude/science/physics-loops/"
    "toe-source-eta-ownership-block33-common-dilation-renewal-locus-20260831"
)
PACKET = ROOT / PACKET_REL
RUNNER_SOURCE_PIN = PACKET / "RUNNER_SOURCE_PIN.md"

BLOCK28_RUNNER = (
    "scripts/admissibility_d4_returned_tip_strict_support_analytic_coupling_"
    "gate_2026_08_30.py"
)
BLOCK32_RUNNER = (
    "scripts/admissibility_d4_symbolic_lambda_guarded_state_carrier_"
    "successor_gate_2026_08_31.py"
)
BLOCK28_NOTE = (
    "docs/ADMISSIBILITY_D4_RETURNED_TIP_SUPPLIED_Q_CONDITIONAL_PAIR_"
    "INSTRUMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-30.md"
)
BLOCK32_NOTE = (
    "docs/ADMISSIBILITY_D4_SYMBOLIC_LAMBDA_GUARDED_FINITE_SUCCESSOR_"
    "TRANSACTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md"
)
AXIOM_NOTE = "docs/MINIMAL_AXIOMS_2026-06-29.md"

DIRECT_HASHES = {
    BLOCK28_RUNNER: "91141d7b917b52eef1335cc6d405acd5927d75ab32ce2f4e0620d4c9007b9a2a",
    BLOCK32_RUNNER: "0547f7b51d8e93f08d5dcd5e3493e724319b98c003a1810490a772b684965fb2",
    BLOCK28_NOTE: "9469f0d03cff9779d7686a62e27a9f1c5dd22dfe8c281d70ab57970f2e3bb5e9",
    BLOCK32_NOTE: "5d7da090e39bbdd9120245804e049577bbacbd9acf3d6eaee79eadc68a5adb36",
    AXIOM_NOTE: "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753",
}

FROZEN = {
    "APPROACH_REGISTRY.md": "3998c170d09a36819b8e81c909c3a2837a237f59d4c5cfaa2f34a6d03bccfbc8",
    "ARTIFACT_PLAN.md": "7abaa687424f617ba24a0e6f3374f65d1dac1921c8aca061c13f2009d5c134d9",
    "ASSUMPTIONS_AND_IMPORTS.md": "8509c2ff3e1598b6085a76123703cb6958ce0d45b148ee6d60ad53b414901da7",
    "AUTHORITY_GATE.md": "02673af7daed2622ddb229d502d95d63bde7a1d30ad81769770771ba5678f655",
    "GOAL.md": "9a387faff491abca46a1c0efdf9477b371f530453eaebf99da3707a194e20765",
    "MUTATION_PLAN.md": "de7b5e92f6c10c4a8d02f13d2f35481c34fbc6187d1fa7687df01f7a40c8c8e4",
    "NO_GO_DISCIPLINE_CHECKLIST.md": "0a65cd86d6b65ed676d5569b7565b461ba1216f7ef836af36d6691f6f162793f",
    "OPPORTUNITY_QUEUE.md": "840f59430af2dec58af64b84ccf8459ccd846ad545a4ca4628bbb21075748003",
    "PANEL_RETURN.md": "662ef710532f7bda750c6b6934d6a0ac39e267f49c6f6326f6373543fa800e68",
    "PREFLIGHT_WITNESSES.md": "2294bcb1403e62f7b8952ca6b38bf2d1c52d5dd678e6b8d5c33fc00653c64f66",
    "ROUTE_PORTFOLIO.md": "798c356e38e4d6aba63e412ac1c68cdd2b64ab82dd56f3acfb2b72e22fd636e6",
    "STATE.yaml": "8f1b089d022bd948ebeb8b4880160f6d8c9036b0df630fbeb0be1b33209fa5ed",
    "TRACE_GATE.md": "4d9a4df7565a0ea6f77f6ae5b77b2b16e00b26f73db73e5ba582eb83464d1c61",
    "INDEPENDENT_STATIC_ATTACK_FINAL.md": "d6dd602323cb1a5f11ab51c886ab9649384233f7fcd7dd0778e670f42cdfccff",
}

# Kept literal for the repository's cache and forensic parsers.
AUDIT_INPUT_PATHS = (
    "scripts/admissibility_d4_returned_tip_strict_support_analytic_coupling_gate_2026_08_30.py",
    "scripts/admissibility_d4_symbolic_lambda_guarded_state_carrier_successor_gate_2026_08_31.py",
    "docs/ADMISSIBILITY_D4_RETURNED_TIP_SUPPLIED_Q_CONDITIONAL_PAIR_INSTRUMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-30.md",
    "docs/ADMISSIBILITY_D4_SYMBOLIC_LAMBDA_GUARDED_FINITE_SUCCESSOR_TRANSACTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block33-common-dilation-renewal-locus-20260831/APPROACH_REGISTRY.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block33-common-dilation-renewal-locus-20260831/ARTIFACT_PLAN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block33-common-dilation-renewal-locus-20260831/ASSUMPTIONS_AND_IMPORTS.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block33-common-dilation-renewal-locus-20260831/AUTHORITY_GATE.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block33-common-dilation-renewal-locus-20260831/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block33-common-dilation-renewal-locus-20260831/MUTATION_PLAN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block33-common-dilation-renewal-locus-20260831/NO_GO_DISCIPLINE_CHECKLIST.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block33-common-dilation-renewal-locus-20260831/OPPORTUNITY_QUEUE.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block33-common-dilation-renewal-locus-20260831/PANEL_RETURN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block33-common-dilation-renewal-locus-20260831/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block33-common-dilation-renewal-locus-20260831/ROUTE_PORTFOLIO.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block33-common-dilation-renewal-locus-20260831/STATE.yaml",
    ".claude/science/physics-loops/toe-source-eta-ownership-block33-common-dilation-renewal-locus-20260831/TRACE_GATE.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block33-common-dilation-renewal-locus-20260831/INDEPENDENT_STATIC_ATTACK_FINAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block33-common-dilation-renewal-locus-20260831/RUNNER_SOURCE_PIN.md",
)


LAMBDA = sp.symbols("lambda", real=True, nonnegative=True)
T = sp.symbols("t", real=True, nonnegative=True)
RHO = sp.symbols("rho", real=True, nonnegative=True)
OUTCOMES = tuple(itertools.product(range(4), repeat=2))
P0 = sp.ones(4) / 4
PPER = sp.eye(4) - P0


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def runner_source_pin_ok() -> bool:
    if not RUNNER_SOURCE_PIN.exists():
        return False
    pins = {}
    for line in RUNNER_SOURCE_PIN.read_text(encoding="utf-8").splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            pins[key.strip()] = value.strip().strip("`")
    return pins.get("source_sha256") == file_sha256(Path(__file__))


def frozen_hashes_ok() -> bool:
    expected = tuple(DIRECT_HASHES) + tuple(
        f"{PACKET_REL}/{name}" for name in FROZEN
    ) + (f"{PACKET_REL}/RUNNER_SOURCE_PIN.md",)
    values = set(DIRECT_HASHES.values()) | set(FROZEN.values())
    return (
        "PENDING" not in values
        and AUDIT_INPUT_PATHS == expected
        and all(
            (ROOT / name).is_file()
            and file_sha256(ROOT / name) == digest
            for name, digest in DIRECT_HASHES.items()
        )
        and all(
            (PACKET / name).is_file()
            and file_sha256(PACKET / name) == digest
            for name, digest in FROZEN.items()
        )
        and runner_source_pin_ok()
    )


def input_fingerprint() -> str:
    digest = hashlib.sha256()
    digest.update(b"runner-cache-input-fingerprint-v1\0")
    for relative in AUDIT_INPUT_PATHS:
        path = ROOT / relative
        body = path.read_bytes() if path.exists() else b"MISSING"
        encoded = relative.encode("utf-8")
        digest.update(len(encoded).to_bytes(8, "big"))
        digest.update(encoded)
        digest.update(len(body).to_bytes(8, "big"))
        digest.update(body)
    return digest.hexdigest()


def q_matrix(lam=LAMBDA, mutation: str | None = None) -> sp.Matrix:
    lam = sp.sympify(lam)
    diagonal = (1 + 3 * lam) / 16
    off_diagonal = (1 - lam) / 16
    if mutation == "bad_diagonal":
        diagonal = (1 + 2 * lam) / 16
    if mutation == "bad_off_diagonal":
        off_diagonal = (1 - 2 * lam) / 16
    matrix = sp.Matrix(
        4,
        4,
        lambda g, h: diagonal if g == h else off_diagonal,
    )
    if mutation == "delete_cell":
        matrix[0, 1] = 0
    if mutation == "marked_label":
        matrix[0, 0] += lam / 32
        matrix[1, 1] -= lam / 32
    return matrix


def flatten(matrix: sp.Matrix) -> sp.Matrix:
    return sp.Matrix([matrix[g, h] for g, h in OUTCOMES])


def matrix_zero(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(value) == 0 for value in matrix)


@lru_cache(maxsize=None)
def q_family_certificate(mutation: str | None = None) -> bool:
    q = q_matrix(mutation=mutation)
    expected = (P0 + LAMBDA * PPER) / 4
    eigens = q.eigenvals()
    normalized = sp.simplify(sum(q)) == 1
    marginals = all(
        sp.simplify(sum(q.row(g))) == sp.Rational(1, 4)
        and sp.simplify(sum(q.col(g))) == sp.Rational(1, 4)
        for g in range(4)
    )
    symmetric = q == q.T
    interval_nonnegative = all(
        sp.Poly(value, LAMBDA).degree() <= 1
        and value.subs(LAMBDA, 0) >= 0
        and value.subs(LAMBDA, 1) >= 0
        for value in q
    )
    strict_support_witness = all(
        value.subs(LAMBDA, sp.Rational(999, 1000)) > 0 for value in q
    )
    return (
        matrix_zero(q - expected)
        and normalized
        and marginals
        and symmetric
        and interval_nonnegative
        and strict_support_witness
        and sp.factor(q.det()) == LAMBDA**3 / 256
        and eigens == {sp.Rational(1, 4): 1, LAMBDA / 4: 3}
        and q.subs(LAMBDA, 0).rank() == 1
        and q.subs(LAMBDA, sp.Rational(2, 5)).rank() == 4
    )


@lru_cache(maxsize=None)
def per_law_four_cause_certificate(mutation: str | None = None) -> bool:
    s = P0 + T * PPER
    if mutation == "sqrt_sign":
        s = P0 - T * PPER
    if mutation == "linear_lambda":
        s = P0 + T**2 * PPER
    if mutation == "wrong_weight":
        reconstructed = s * s.T / 5
    else:
        reconstructed = s * s.T / 4
    entry_form = all(
        sp.simplify(s[i, j] - ((1 + 3 * T) / 4 if i == j else (1 - T) / 4))
        == 0
        for i in range(4)
        for j in range(4)
    )
    interval_nonnegative = all(
        sp.Poly(value, T).degree() <= 1
        and value.subs(T, 0) >= 0
        and value.subs(T, 1) >= 0
        for value in s
    )
    return (
        entry_form
        and all(sp.simplify(sum(s.col(j))) == 1 for j in range(4))
        and matrix_zero(reconstructed - q_matrix(T**2))
        and interval_nonnegative
    )


def product_support_on_diagonal(left: frozenset[int], right: frozenset[int]) -> bool:
    return bool(left and right) and all(g == h for g in left for h in right)


@lru_cache(maxsize=None)
def fixed_five_library_certificate(mutation: str | None = None) -> bool:
    uniform = sp.ones(4) / 16
    atoms = []
    for index in range(4):
        atom = sp.zeros(4)
        atom[index, index] = 1
        atoms.append(atom)
    weights = [1 - LAMBDA] + [LAMBDA / 4] * 4
    if mutation == "four_only":
        library = atoms
        reconstruction = sum(
            (LAMBDA / 4 * atom for atom in atoms), sp.zeros(4)
        )
    else:
        library = [uniform] + atoms
        reconstruction = sum(
            (weight * response for weight, response in zip(weights, library)),
            sp.zeros(4),
        )
    subsets = [
        frozenset(i for i in range(4) if mask & (1 << i))
        for mask in range(1, 16)
    ]
    diagonal_products = [
        (left, right)
        for left in subsets
        for right in subsets
        if product_support_on_diagonal(left, right)
    ]
    support_lemma = all(
        len(left) == len(right) == 1 and left == right
        for left, right in diagonal_products
    )
    full_endpoint_needs_four = len(diagonal_products) == 4
    uniform_outside_atom_hull = any(uniform[g, h] > 0 for g in range(4) for h in range(4) if g != h)
    closed_limit_reached = matrix_zero(
        q_matrix(1)
        - sum(
            (response.subs(LAMBDA, 1) * weight.subs(LAMBDA, 1)
             for response, weight in zip([uniform] + atoms, weights)),
            sp.zeros(4),
        )
    )
    return (
        len(library) == 5
        and all(response.rank() == 1 for response in library)
        and all(sp.simplify(sum(response)) == 1 for response in library)
        and sp.simplify(sum(weights)) == 1
        and matrix_zero(reconstruction - q_matrix())
        and support_lemma
        and full_endpoint_needs_four
        and uniform_outside_atom_hull
        and closed_limit_reached
    )


def outer(left: sp.Matrix, right: sp.Matrix) -> sp.Matrix:
    return left * right.T


def response_library(lam) -> tuple[sp.Matrix, ...]:
    t = sp.sqrt(lam)
    s = P0 + t * PPER
    return tuple(
        sp.Matrix([s[g, z] * s[h, z] for g, h in OUTCOMES])
        for z in range(4)
    )


def mixture(weights, responses) -> sp.Matrix:
    return sum(
        (weight * response for weight, response in zip(weights, responses)),
        sp.zeros(len(responses[0]), 1),
    )


def frozen_history(weights, responses) -> sp.Matrix:
    return sum(
        (weight * outer(response, response) for weight, response in zip(weights, responses)),
        sp.zeros(len(responses[0])),
    )


def kernel_history(weights, kernel: sp.Matrix, responses) -> sp.Matrix:
    size = len(responses[0])
    return sum(
        (
            weights[z] * kernel[z, zp] * outer(responses[z], responses[zp])
            for z in range(len(weights))
            for zp in range(len(weights))
        ),
        sp.zeros(size),
    )


@lru_cache(maxsize=1)
def covariance_identity_certificate() -> bool:
    # Generic expansion: normalization is imposed by p2=1-p0-p1.
    p0, p1 = sp.symbols("p0 p1", real=True)
    weights = (p0, p1, 1 - p0 - p1)
    symbols = sp.symbols("r0:9", real=True)
    responses = tuple(sp.Matrix(symbols[3 * z : 3 * z + 3]) for z in range(3))
    q = mixture(weights, responses)
    left = frozen_history(weights, responses) - outer(q, q)
    right = sum(
        (
            weights[z] * outer(responses[z] - q, responses[z] - q)
            for z in range(3)
        ),
        sp.zeros(3),
    )
    if not matrix_zero(sp.simplify(left - right)):
        return False

    lam = sp.Rational(2, 5)
    per_law = response_library(lam)
    pi = [sp.Rational(1, 4)] * 4
    q_lam = mixture(pi, per_law)
    covariance = frozen_history(pi, per_law) - outer(q_lam, q_lam)
    factor = sp.Matrix.hstack(
        *(sp.Rational(1, 2) * (response - q_lam) for response in per_law)
    )
    psd_factorization = matrix_zero(covariance - factor * factor.T)
    trace_gap = sp.simplify(covariance.trace())
    norm_gap = sp.simplify(
        sum(
            pi[z] * ((per_law[z] - q_lam).T * (per_law[z] - q_lam))[0]
            for z in range(4)
        )
    )
    return psd_factorization and trace_gap == norm_gap and trace_gap > 0


@lru_cache(maxsize=1)
def finite_weighted_sos_equality_schema_certificate() -> bool:
    """Encode the cardinality-independent equality step as a positive SOS.

    The proof is structural: for any finite cause count the trace adds one
    positive weight times one Euclidean squared norm.  The symbolic instance
    below checks every monomial/weight pairing for the actual 16-outcome
    response space; ``weighted_sos_zero_iff`` then exhausts active/inactive
    sector logic on an independent exact rational grammar.  Extending the
    outer finite loop adds only another positive block of the same form.
    """

    cause_count = 7
    weights = sp.symbols(f"p0:{cause_count}", positive=True)
    deviations = tuple(
        tuple(
            sp.symbols(f"d{cause}_{outcome}", real=True)
            for outcome in range(16)
        )
        for cause in range(cause_count)
    )
    flat = tuple(value for row in deviations for value in row)
    trace = sp.Add(
        *(
            weights[cause] * deviations[cause][outcome] ** 2
            for cause in range(cause_count)
            for outcome in range(16)
        )
    )
    terms = sp.Poly(trace, *flat).terms()
    structural_sos = (
        len(terms) == cause_count * 16
        and all(
            sum(monomial) == 2
            and monomial.count(2) == 1
            and coefficient in weights
            and coefficient.is_positive is True
            for monomial, coefficient in terms
        )
    )

    def weighted_sos_zero_iff(active_weights, vectors) -> bool:
        value = sum(
            active_weights[cause]
            * sum(component * component for component in vectors[cause])
            for cause in range(len(active_weights))
        )
        active_zero = all(
            weight == 0 or all(component == 0 for component in vector)
            for weight, vector in zip(active_weights, vectors)
        )
        return (value == 0) == active_zero

    exhaustive_active_logic = all(
        weighted_sos_zero_iff(weights_exact, vectors)
        for weights_exact in itertools.product((0, 1, 2), repeat=3)
        if any(weights_exact)
        for components in itertools.product((-1, 0, 1), repeat=6)
        for vectors in ((components[0:2], components[2:4], components[4:6]),)
    )
    return structural_sos and exhaustive_active_logic


@lru_cache(maxsize=1)
def product_response_rank_schema_certificate() -> bool:
    left = sp.symbols("a0:4", real=True)
    right = sp.symbols("b0:4", real=True)
    response = sp.Matrix(left) * sp.Matrix([right])
    all_two_minors_zero = all(
        sp.simplify(
            response.extract((i, j), (k, ell)).det()
        )
        == 0
        for i, j in itertools.combinations(range(4), 2)
        for k, ell in itertools.combinations(range(4), 2)
    )
    nonzero_witness = response.subs(
        {**{left[i]: int(i == 0) for i in range(4)}, **{right[i]: sp.Rational(1, 4) for i in range(4)}}
    )
    return all_two_minors_zero and nonzero_witness.rank() == 1


@lru_cache(maxsize=1)
def universal_frozen_screening_locus_certificate() -> bool:
    # Covariance identity + positive-SOS equality + rank-one screening
    # responses is the finite-factorization proof schema.  The determinant of
    # Q_lambda then excludes every positive lambda; the one-state q0 response
    # is the converse witness.
    return (
        covariance_identity_certificate()
        and finite_weighted_sos_equality_schema_certificate()
        and product_response_rank_schema_certificate()
        and sp.factor(q_matrix().det()) == LAMBDA**3 / 256
        and q_matrix(0).rank() == 1
        and q_matrix(sp.Rational(1, 7)).rank() == 4
        and lambda_zero_factorization_certificate()
    )


@lru_cache(maxsize=1)
def lambda_zero_row_factorization_gap() -> sp.Expr:
    q0 = flatten(q_matrix(0))
    row_responses = []
    for z in range(4):
        row_responses.append(
            sp.Matrix([sp.Rational(1, 4) if g == z else 0 for g, h in OUTCOMES])
        )
    row_weights = [sp.Rational(1, 4)] * 4
    row_q = mixture(row_weights, row_responses)
    row_gap = frozen_history(row_weights, row_responses) - outer(row_q, row_q)
    if row_q != q0:
        return sp.nan
    return sp.simplify(row_gap.trace())


@lru_cache(maxsize=1)
def lambda_zero_factorization_certificate() -> bool:
    q0 = flatten(q_matrix(0))
    # Existence: one active product response equals q0.
    one_state_gap = frozen_history([sp.S.One], [q0]) - outer(q0, q0)
    # Non-universality: a frozen row label still averages to q0 but correlates uses.
    row_gap = lambda_zero_row_factorization_gap()
    # Inactive sectors are unconstrained by the equality condition.
    arbitrary = sp.Matrix([sp.S.One] + [sp.S.Zero] * 15)
    inactive_gap = frozen_history([sp.S.One, sp.S.Zero], [q0, arbitrary]) - outer(q0, q0)
    return (
        matrix_zero(one_state_gap)
        and row_gap == sp.Rational(3, 16)
        and matrix_zero(inactive_gap)
    )


@lru_cache(maxsize=None)
def exact_frozen_locus_certificate(mutation: str | None = None) -> bool:
    rank_zero = q_matrix(0).rank()
    rank_positive = q_matrix(sp.Rational(1, 7)).rank()
    if mutation == "claim_every_zero_factorization":
        return lambda_zero_row_factorization_gap() == 0
    if mutation == "allow_positive":
        rank_positive = 1
    return (
        q_family_certificate()
        and universal_frozen_screening_locus_certificate()
        and lambda_zero_factorization_certificate()
        and rank_zero == 1
        and rank_positive == 4
        and per_law_four_cause_certificate()
    )


def binary_responses() -> tuple[sp.Matrix, sp.Matrix]:
    return flatten(q_matrix(0)), flatten(q_matrix(1))


@lru_cache(maxsize=None)
def markov_and_stationarity_certificate(mutation: str | None = None) -> bool:
    r0, r1 = binary_responses()
    pi = sp.Matrix([[1 - LAMBDA, LAMBDA]])
    projection = sp.Matrix([[1 - LAMBDA, LAMBDA], [1 - LAMBDA, LAMBDA]])
    identity = sp.eye(2)
    kernel = projection + RHO * (identity - projection)
    if mutation == "transpose_kernel":
        kernel = kernel.T
    q = (1 - LAMBDA) * r0 + LAMBDA * r1
    history = kernel_history([1 - LAMBDA, LAMBDA], kernel, [r0, r1])
    delta = r1 - r0
    expected = RHO * LAMBDA * (1 - LAMBDA) * outer(delta, delta)
    base_ok = (
        all(sp.simplify(sum(kernel.row(row))) == 1 for row in range(2))
        and matrix_zero(sp.simplify(pi * kernel - pi))
        and matrix_zero(sp.simplify(history - outer(q, q) - expected))
        and all(
            entry.subs({LAMBDA: lam_endpoint, RHO: rho_endpoint}) >= 0
            for entry in kernel
            for lam_endpoint in (0, 1)
            for rho_endpoint in (0, 1)
        )
    )

    # A nonsymmetric exact oracle fixes row-stochastic orientation.
    pi_ns = sp.Matrix([[sp.Rational(3, 4), sp.Rational(1, 4)]])
    k_ns = sp.Matrix([[sp.Rational(5, 6), sp.Rational(1, 6)], [sp.Rational(1, 2), sp.Rational(1, 2)]])
    h_ns = kernel_history(list(pi_ns), k_ns, [r0, r1])
    q_ns = sp.Rational(3, 4) * r0 + sp.Rational(1, 4) * r1
    residual_ns = h_ns - outer(q_ns, q_ns)
    orientation_ok = (
        pi_ns * k_ns == pi_ns
        and k_ns * pi_ns.T != pi_ns.T
        and sp.simplify(residual_ns.trace()) == sp.Rational(3, 256)
    )

    frozen = kernel_history(
        [1 - LAMBDA, LAMBDA], sp.eye(2), [r0, r1]
    )
    reset = kernel_history(
        [1 - LAMBDA, LAMBDA], projection, [r0, r1]
    )
    endpoints_ok = (
        matrix_zero(reset - outer(q, q))
        and matrix_zero(
            frozen - outer(q, q) - LAMBDA * (1 - LAMBDA) * outer(delta, delta)
        )
        and sp.solve(sp.factor(RHO * LAMBDA * (1 - LAMBDA)), RHO) == [0]
        and sp.solve(sp.factor(RHO * LAMBDA * (1 - LAMBDA)), LAMBDA) == [0, 1]
    )
    return base_ok and orientation_ok and endpoints_ok


@lru_cache(maxsize=1)
def hidden_memory_lumpability_certificate() -> bool:
    r0, r1 = binary_responses()
    responses = [r0, r0, r1, r1]  # states (c,u) in (0,0),(0,1),(1,0),(1,1)
    weights = [sp.Rational(1, 4)] * 4
    kernel = sp.zeros(4)
    states = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for row, (_c, u) in enumerate(states):
        for col, (_cp, up) in enumerate(states):
            if up == u:
                kernel[row, col] = sp.Rational(1, 2)
    q = mixture(weights, responses)
    history = kernel_history(weights, kernel, responses)
    reset_projection = sp.ones(4) / 4
    return (
        all(sum(kernel.row(row)) == 1 for row in range(4))
        and sp.Matrix([weights]) * kernel == sp.Matrix([weights])
        and kernel != reset_projection
        and matrix_zero(history - outer(q, q))
    )


@lru_cache(maxsize=1)
def shared_conditional_noise_escape_certificate() -> bool:
    q0 = flatten(q_matrix(0))
    coupled = sp.zeros(16)
    for outcome in range(16):
        coupled[outcome, outcome] = q0[outcome]
    return (
        all(sum(coupled.row(outcome)) == q0[outcome] for outcome in range(16))
        and all(sum(coupled.col(outcome)) == q0[outcome] for outcome in range(16))
        and not matrix_zero(coupled - outer(q0, q0))
    )


@lru_cache(maxsize=None)
def covariance_mutation_certificate(mutation: str) -> bool:
    lam = sp.Rational(2, 5)
    responses = response_library(lam)
    weights = [sp.Rational(1, 4)] * 4
    q = mixture(weights, responses)
    correct = frozen_history(weights, responses) - outer(q, q)
    dropped_cross_terms = frozen_history(weights, responses)
    reversed_gap = -correct
    if mutation == "drop_cross_terms":
        return not matrix_zero(dropped_cross_terms - correct)
    if mutation == "reverse_sign":
        return correct.trace() > 0 and reversed_gap.trace() < 0
    return False


@lru_cache(maxsize=1)
def use_dependent_fixed_cause_escape_certificate() -> bool:
    lam = sp.Rational(1, 3)
    responses = response_library(lam)
    q = mixture([sp.Rational(1, 4)] * 4, responses)
    history = sp.zeros(16)
    unequal_kernel_seen = False
    for first in range(4):
        for second in range(4):
            history += sp.Rational(1, 16) * outer(responses[first], responses[second])
            unequal_kernel_seen |= first != second and responses[first] != responses[second]
    return unequal_kernel_seen and matrix_zero(history - outer(q, q))


@lru_cache(maxsize=1)
def lambda_dependent_response_not_common_certificate() -> bool:
    responses = response_library(LAMBDA)
    reconstructed = mixture([sp.Rational(1, 4)] * 4, responses)
    response_symbols = set().union(
        *(set(value.free_symbols) for response in responses for value in response)
    )
    return matrix_zero(reconstructed - flatten(q_matrix())) and LAMBDA in response_symbols


@lru_cache(maxsize=1)
def binary_equality_event_gap_certificate() -> bool:
    r0, r1 = binary_responses()
    equality_indices = [index for index, (g, h) in enumerate(OUTCOMES) if g == h]
    p0 = sum(r0[index] for index in equality_indices)
    p1 = sum(r1[index] for index in equality_indices)
    persistent = (1 - LAMBDA) * p0**2 + LAMBDA * p1**2
    renewed = ((1 - LAMBDA) * p0 + LAMBDA * p1) ** 2
    q = (1 - LAMBDA) * r0 + LAMBDA * r1
    complete_pair_repeat_gap = sp.simplify(
        (1 - LAMBDA) * (r0.T * r0)[0]
        + LAMBDA * (r1.T * r1)[0]
        - (q.T * q)[0]
    )
    return (
        p0 == sp.Rational(1, 4)
        and p1 == 1
        and sp.simplify(
            persistent - renewed - 9 * LAMBDA * (1 - LAMBDA) / 16
        )
        == 0
        and sp.simplify(
            complete_pair_repeat_gap - 3 * LAMBDA * (1 - LAMBDA) / 16
        )
        == 0
        and sp.simplify(complete_pair_repeat_gap - (persistent - renewed)) != 0
    )


def isometry_columns(mutation: str | None = None):
    # Codomain labels are (cause sector 0..4, output Blank/pair 0..16,
    # archive Blank/pair 0..16).  Only the five Ready/Blank input columns are used.
    columns: list[dict[tuple[int, int, int], sp.Expr]] = []
    independent = {}
    for pair_index in range(16):
        archive = 1 if mutation == "merge_archive" else pair_index + 1
        independent[(0, pair_index + 1, archive)] = (
            sp.Rational(1, 16)
            if mutation == "bad_amplitude"
            else sp.Rational(1, 4) + LAMBDA / 100
            if mutation == "lambda_response"
            else sp.Rational(1, 4)
        )
    columns.append(independent)
    for i in range(4):
        pair_index = 4 * i + i
        cause = 0 if mutation == "merge_cause" else i + 1
        columns.append({(cause, pair_index + 1, pair_index + 1): sp.S.One})
    if mutation == "duplicate_control":
        columns[2] = dict(columns[1])
    return columns


def sparse_inner(left, right):
    return sp.simplify(
        sum(sp.conjugate(amplitude) * right.get(label, 0) for label, amplitude in left.items())
    )


def reduced_output_density(mutation: str | None = None) -> sp.Matrix:
    columns = isometry_columns(mutation)
    weights = [1 - LAMBDA] + [LAMBDA / 4] * 4
    rho = sp.zeros(17)
    for weight, column in zip(weights, columns):
        for (cause, output, archive), amplitude in column.items():
            for (cause2, output2, archive2), amplitude2 in column.items():
                if cause == cause2 and archive == archive2:
                    rho[output, output2] += weight * amplitude * sp.conjugate(amplitude2)
    return sp.simplify(rho)


@lru_cache(maxsize=None)
def fixed_isometry_certificate(mutation: str | None = None) -> bool:
    columns = isometry_columns(mutation)
    gram = sp.Matrix(
        5, 5, lambda i, j: sparse_inner(columns[i], columns[j])
    )
    rho = reduced_output_density(mutation)
    target = sp.zeros(17)
    q = flatten(q_matrix())
    for index in range(16):
        target[index + 1, index + 1] = q[index]
    free_symbols_v = set().union(
        *(set(amplitude.free_symbols) for column in columns for amplitude in column.values())
    )
    expected_rho_c = sp.diag(
        1 - LAMBDA, LAMBDA / 4, LAMBDA / 4, LAMBDA / 4, LAMBDA / 4
    )
    rho_c = expected_rho_c.copy()
    if mutation == "coherent_cause":
        rho_c[0, 1] = rho_c[1, 0] = LAMBDA / 8
    derivative = sp.diag(-1, sp.Rational(1, 4), sp.Rational(1, 4), sp.Rational(1, 4), sp.Rational(1, 4))
    shape_ok = (
        len(columns[0]) == 16
        and all(value == sp.Rational(1, 4) for value in columns[0].values())
        and all(len(column) == 1 and tuple(column.values()) == (sp.S.One,) for column in columns[1:])
        and {next(iter(columns[i]))[0] for i in range(1, 5)} == {1, 2, 3, 4}
    )
    return (
        gram == sp.eye(5)
        and rho == target
        and rho[0, 0] == 0
        and all(rho[i, j] == 0 for i in range(17) for j in range(17) if i != j)
        and free_symbols_v == set()
        and rho_c == expected_rho_c
        and rho_c.diff(LAMBDA) == derivative
        and sp.simplify(rho_c.trace()) == 1
        and shape_ok
        and 5 * 17 * 17 == 1445
    )


@lru_cache(maxsize=None)
def three_supplied_bank_certificate(mutation: str | None = None) -> bool:
    registers = [f"{kind}{use}" for use in range(1, 4) for kind in ("C", "O", "A")]
    availability_time = {register: 0 for register in registers}
    if mutation == "alias_archive":
        registers[-1] = "A2"
    if mutation == "omit_blank":
        blank_banks = {"O1", "A1", "O2", "A2", "O3"}
    else:
        blank_banks = {f"{kind}{use}" for use in range(1, 4) for kind in ("O", "A")}
    if mutation == "host_insert":
        for register in ("C2", "O2", "A2"):
            availability_time[register] = 1
        for register in ("C3", "O3", "A3"):
            availability_time[register] = 2
    lam = Fraction(2, 5)
    cause_weights = [1 - lam] + [lam / 4] * 4
    response_probabilities = []
    response_probabilities.append([Fraction(1, 16)] * 16)
    for i in range(4):
        response_probabilities.append(
            [Fraction(1) if g == h == i else Fraction(0) for g, h in OUTCOMES]
        )
    q = [
        sum(cause_weights[c] * response_probabilities[c][x] for c in range(5))
        for x in range(16)
    ]
    output = [Fraction(0)] * (16**3)
    cause_triples = 0
    for c1, c2, c3 in itertools.product(range(5), repeat=3):
        cause_triples += 1
        weight = cause_weights[c1] * cause_weights[c2] * cause_weights[c3]
        for x1, x2, x3 in itertools.product(range(16), repeat=3):
            index = (x1 * 16 + x2) * 16 + x3
            output[index] += (
                weight
                * response_probabilities[c1][x1]
                * response_probabilities[c2][x2]
                * response_probabilities[c3][x3]
            )
    target = [
        q[x1] * q[x2] * q[x3]
        for x1, x2, x3 in itertools.product(range(16), repeat=3)
    ]
    symbolic_weights = [1 - LAMBDA] + [LAMBDA / 4] * 4
    symbolic_responses = [
        [sp.Rational(value.numerator, value.denominator) for value in response]
        for response in response_probabilities
    ]
    symbolic_q = [
        sp.simplify(
            sum(symbolic_weights[c] * symbolic_responses[c][x] for c in range(5))
        )
        for x in range(16)
    ]
    return (
        len(registers) == len(set(registers)) == 9
        and blank_banks == {"O1", "A1", "O2", "A2", "O3", "A3"}
        and all(time == 0 for time in availability_time.values())
        and cause_triples == 125
        and output == target
        and sum(output) == 1
        and sp.Matrix(symbolic_q) == flatten(q_matrix())
    )


@lru_cache(maxsize=None)
def coherent_control_certificate(mutation: str | None = None) -> bool:
    lam = sp.Rational(1, 3)
    expected_symbolic_phase = (
        2 * LAMBDA - 1 + 2 * sp.I * sp.sqrt(LAMBDA * (1 - LAMBDA))
    )
    symbolic_phase = expected_symbolic_phase
    if mutation == "fixed_phase":
        symbolic_phase = sp.I
    if mutation == "nonunit_phase":
        symbolic_phase = sp.S(2)
    if mutation == "wrong_angle":
        symbolic_phase = LAMBDA + sp.I * sp.sqrt(1 - LAMBDA**2)
    if mutation == "family_drift":
        symbolic_phase = expected_symbolic_phase + LAMBDA - sp.Rational(1, 3)
    phase = symbolic_phase.subs(LAMBDA, lam)
    unitary = P0 + phase * PPER
    probabilities = sp.Matrix(
        4, 4, lambda g, h: sp.simplify(unitary[g, h] * sp.conjugate(unitary[g, h]))
    )
    permutations_ok = True
    for permutation in itertools.permutations(range(4)):
        p = sp.zeros(4)
        for old, new in enumerate(permutation):
            p[new, old] = 1
        permutations_ok &= matrix_zero(p * unitary - unitary * p)
    expected = 4 * q_matrix(lam)
    phase_formula_ok = sp.simplify(symbolic_phase - expected_symbolic_phase) == 0
    phase_real = 2 * LAMBDA - 1
    phase_imaginary_squared = 4 * LAMBDA * (1 - LAMBDA)
    symbolic_norm = sp.expand(phase_real**2 + phase_imaginary_squared)
    symbolic_diagonal_probability = sp.expand(
        ((1 + 3 * phase_real) ** 2 + 9 * phase_imaginary_squared) / 16
    )
    symbolic_off_probability = sp.expand(
        ((1 - phase_real) ** 2 + phase_imaginary_squared) / 16
    )
    strict_table = 4 * q_matrix(sp.Rational(2, 5))
    dephased_choi = sp.diag(*tuple(strict_table))
    unitary_vector = sp.Matrix(tuple(unitary))
    unitary_choi = unitary_vector * sp.conjugate(unitary_vector.T)
    dephased_choi_rank = dephased_choi.rank()
    unitary_choi_rank = unitary_choi.rank()
    return (
        matrix_zero(unitary * sp.conjugate(unitary.T) - sp.eye(4))
        and matrix_zero(probabilities - expected)
        and phase_formula_ok
        and symbolic_norm == 1
        and sp.simplify(symbolic_diagonal_probability - 4 * q_matrix()[0, 0]) == 0
        and sp.simplify(symbolic_off_probability - 4 * q_matrix()[0, 1]) == 0
        and permutations_ok
        and dephased_choi_rank == 16
        and unitary_choi_rank == 1
        and LAMBDA in symbolic_phase.free_symbols
        and phase != 1
    )


def w_vector(mutation: str | None = None) -> list[int]:
    if mutation == "distinguished_label":
        return [1 if index == 0 else -1 if index == 1 else 0 for index in range(16)]
    if mutation == "nonzero_sum":
        return [4 if g == h else -1 for g, h in OUTCOMES]
    return [3 if g == h else -1 for g, h in OUTCOMES]


@lru_cache(maxsize=None)
def h3_epsilon(lam, mutation: str | None = None):
    b = (1 - lam) / 16
    if mutation == "epsilon_b2":
        return b**2 / 54
    if mutation == "epsilon_large":
        return b**3 / 8
    if mutation == "family_drift":
        return b**3 / 54 + (lam - sp.Rational(2, 5)) * b**2
    return b**3 / 54


@lru_cache(maxsize=None)
def h3_table(lam: Fraction, mutation: str | None = None) -> tuple[Fraction, ...]:
    a = (1 + 3 * lam) / 16
    b = (1 - lam) / 16
    q = [a if g == h else b for g, h in OUTCOMES]
    w_mutation = mutation if mutation in {"distinguished_label", "nonzero_sum"} else None
    w = w_vector(w_mutation)
    epsilon = h3_epsilon(lam, mutation)
    table = []
    for x, y, z in itertools.product(range(16), repeat=3):
        if mutation == "axis_1":
            feature = w[y] * w[z]
        elif mutation == "axis_2":
            feature = w[x] * w[z]
        elif mutation == "axis_3":
            feature = w[x] * w[y]
        else:
            feature = w[x] * w[y] * w[z]
        table.append(q[x] * q[y] * q[z] + epsilon * feature)
    return tuple(table)


def h3_index(x: int, y: int, z: int) -> int:
    return (x * 16 + y) * 16 + z


def h3_marginals_ok(table: tuple[Fraction, ...], lam: Fraction) -> bool:
    a = (1 + 3 * lam) / 16
    b = (1 - lam) / 16
    q = [a if g == h else b for g, h in OUTCOMES]
    if sum(table) != 1:
        return False
    for x in range(16):
        if sum(table[h3_index(x, y, z)] for y in range(16) for z in range(16)) != q[x]:
            return False
    for y in range(16):
        if sum(table[h3_index(x, y, z)] for x in range(16) for z in range(16)) != q[y]:
            return False
    for z in range(16):
        if sum(table[h3_index(x, y, z)] for x in range(16) for y in range(16)) != q[z]:
            return False
    for x, y in itertools.product(range(16), repeat=2):
        if sum(table[h3_index(x, y, z)] for z in range(16)) != q[x] * q[y]:
            return False
        if sum(table[h3_index(x, z, y)] for z in range(16)) != q[x] * q[y]:
            return False
        if sum(table[h3_index(z, x, y)] for z in range(16)) != q[x] * q[y]:
            return False
    return True


def h3_symmetry_certificate(mutation: str | None = None) -> bool:
    # Invariance of q and w makes their tensor products invariant.  Checking
    # all outcomes under S4 is stronger than the displayed proper-cubic subgroup.
    w_mutation = mutation if mutation in {"distinguished_label", "nonzero_sum"} else None
    w = w_vector(w_mutation)
    for permutation in itertools.permutations(range(4)):
        outcome_map = {
            index: OUTCOMES.index((permutation[g], permutation[h]))
            for index, (g, h) in enumerate(OUTCOMES)
        }
        for x in range(16):
            if w[x] != w[outcome_map[x]]:
                return False
    side_map = {index: OUTCOMES.index((h, g)) for index, (g, h) in enumerate(OUTCOMES)}
    return all(w[x] == w[side_map[x]] for x in range(16))


@lru_cache(maxsize=None)
def depth_three_counterhistory_certificate(mutation: str | None = None) -> bool:
    lam = Fraction(2, 5)
    table = h3_table(lam, mutation)
    b = (1 - lam) / 16
    diagonal_cell = h3_index(0, 5, 10)
    q_diag = (1 + 3 * lam) / 16
    residual = table[diagonal_cell] - q_diag**3
    b_symbol, excess = sp.symbols("b excess", positive=True)
    a_symbol = b_symbol + excess
    all_off = sp.expand(b_symbol**3 - b_symbol**3 / 54)
    one_off = sp.expand(b_symbol * a_symbol**2 - b_symbol**3 / 6)
    one_off_remainder = sp.Poly(
        sp.expand(one_off - sp.Rational(5, 6) * b_symbol**3),
        b_symbol,
        excess,
    )
    symbolic_bounds = (
        all_off == sp.Rational(53, 54) * b_symbol**3
        and all(coefficient >= 0 for coefficient in one_off_remainder.coeffs())
        and sp.simplify(27 * b_symbol**3 / 54 - b_symbol**3 / 2) == 0
    )
    symbolic_b = (1 - LAMBDA) / 16
    epsilon_formula_ok = sp.simplify(
        h3_epsilon(LAMBDA, mutation) - symbolic_b**3 / 54
    ) == 0
    predictive_shift = residual / (q_diag**2)
    w_mutation = mutation if mutation in {"distinguished_label", "nonzero_sum"} else None
    return (
        sum(w_vector(w_mutation)) == 0
        and len(table) == 4096
        and min(table) > 0
        and h3_marginals_ok(table, lam)
        and residual == b**3 / 2
        and predictive_shift != 0
        and epsilon_formula_ok
        and symbolic_bounds
        and h3_symmetry_certificate(mutation)
    )


@dataclass(frozen=True)
class Scope:
    physical_cause_carrier: bool = False
    cause_is_Record: bool = False
    nn_stinespring_compiled: bool = False
    third_Block32_transaction: bool = False
    branchwise_reset_derived: bool = False
    physical_reset: bool = False
    physical_renewal: bool = False
    autonomous_invocation: bool = False
    cadence_or_rate: bool = False
    arbitrary_depth: bool = False
    nature_lambda_selected: bool = False
    fixed_common_coherent_unitary: bool = False
    other_architectures_excluded: bool = False
    normalized_conserved_source: bool = False
    gravity_closed: bool = False
    axiom_change: bool = False
    audit_verdict: bool = False
    obligation_retirement: bool = False
    toe_score_movement: bool = False


REQUIRED_SCOPE_FIELDS = {
    "physical_cause_carrier",
    "cause_is_Record",
    "nn_stinespring_compiled",
    "third_Block32_transaction",
    "branchwise_reset_derived",
    "physical_reset",
    "physical_renewal",
    "autonomous_invocation",
    "cadence_or_rate",
    "arbitrary_depth",
    "nature_lambda_selected",
    "fixed_common_coherent_unitary",
    "other_architectures_excluded",
    "normalized_conserved_source",
    "gravity_closed",
    "axiom_change",
    "audit_verdict",
    "obligation_retirement",
    "toe_score_movement",
}

TERMINAL_TEXT = (
    "FINITE-CLASSICAL-SCREENING-FROZEN-SAME-CAUSE-IDENTICAL-PRODUCT-RESPONSE-"
    "CONDITIONALLY-IID-BLOCK32-PRODUCT-HISTORY-EXISTENCE-LOCUS-LAMBDA-ZERO;"
    "SUPPLIED-IID-PREINITIALIZED-DISJOINT-BANKS-FIVE-CAUSE-AND-LAMBDA-"
    "DEPENDENT-COHERENT-CONTROLS-RETAIN-FULL-STRICT-INTERVAL;ALL-PAIR-"
    "MARGINALS-DO-NOT-DETERMINE-DEPTH-THREE;"
    "LAMBDA-REMAINS-IN-ENVIRONMENT-PREPARATION-COUPLING-OR-SUPPLIED-"
    "HISTORY-RESET-LAW"
)

SCOPE_TERMINAL_PROMOTIONS = {
    "physical_cause_carrier": "PHYSICAL-CAUSE-CARRIER-CONSTRUCTED",
    "cause_is_Record": "CAUSE-IS-RECORD",
    "nn_stinespring_compiled": "NN-STINESPRING-COMPILED",
    "third_Block32_transaction": "THIRD-BLOCK32-TRANSACTION-EXECUTED",
    "branchwise_reset_derived": "BRANCHWISE-RESET-DERIVED",
    "physical_reset": "PHYSICAL-RESET-DERIVED",
    "physical_renewal": "PHYSICAL-RENEWAL-DERIVED",
    "autonomous_invocation": "AUTONOMOUS-INVOCATION-DERIVED",
    "cadence_or_rate": "CADENCE-OR-RATE-DERIVED",
    "arbitrary_depth": "ARBITRARY-DEPTH-RENEWAL-PROVED",
    "nature_lambda_selected": "NATURE-LAMBDA-SELECTED",
    "fixed_common_coherent_unitary": "FIXED-COMMON-COHERENT-UNITARY",
    "other_architectures_excluded": "OTHER-ARCHITECTURES-EXCLUDED",
    "normalized_conserved_source": "NORMALIZED-CONSERVED-SOURCE-DERIVED",
    "gravity_closed": "GRAVITY-CLOSED",
    "axiom_change": "AXIOM-AMENDED",
    "audit_verdict": "AUDIT-VERDICT-APPLIED",
    "obligation_retirement": "OBLIGATION-RETIRED",
    "toe_score_movement": "TOE-SCORE-MOVED",
}


def scope_guard(scope: Scope = Scope(), terminal: str = TERMINAL_TEXT) -> bool:
    actual_fields = {field.name for field in fields(scope)}
    forbidden_terminal = tuple(SCOPE_TERMINAL_PROMOTIONS.values()) + (
        "NATURE-SELECTS-ZERO",
        "MICROSCOPIC-ENVIRONMENT-RANK-FROM-MATRIX-RANK",
        "NONNEGATIVE-RANK-SELECTS-LAW",
        "BINARY-MODE-IS-COMPLETE-CAUSE",
        "FIVE-MINIMAL-FOR-ONE-POSITIVE-LAW",
        "PARAMETER-RELOCATION-IS-SELECTION",
        "NO-ENVIRONMENT-USED",
    )
    required_fragments = (
        "FINITE-CLASSICAL-SCREENING",
        "FROZEN-SAME-CAUSE-IDENTICAL-PRODUCT-RESPONSE",
        "CONDITIONALLY-IID",
        "BLOCK32-PRODUCT-HISTORY",
        "LOCUS-LAMBDA-ZERO",
        "SUPPLIED-IID",
        "PREINITIALIZED-DISJOINT-BANKS",
        "LAMBDA-DEPENDENT-COHERENT",
        "FULL-STRICT-INTERVAL",
        "PAIR-MARGINALS-DO-NOT-DETERMINE-DEPTH-THREE",
        "LAMBDA-REMAINS-IN-ENVIRONMENT-PREPARATION-COUPLING-OR-SUPPLIED-HISTORY-RESET-LAW",
    )
    return (
        actual_fields == REQUIRED_SCOPE_FIELDS
        and all(not getattr(scope, name) for name in REQUIRED_SCOPE_FIELDS)
        and terminal == TERMINAL_TEXT
        and all(fragment in terminal for fragment in required_fragments)
        and not any(fragment in terminal for fragment in forbidden_terminal)
    )


def static_source_certificate() -> bool:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    forbidden_calls = {
        "write_text",
        "write_bytes",
        "unlink",
        "remove",
        "rename",
        "rmdir",
        "mkdir",
        "makedirs",
        "system",
        "open",
        "run",
        "Popen",
    }
    calls = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Attribute):
                calls.append(node.func.attr)
            elif isinstance(node.func, ast.Name):
                calls.append(node.func.id)
    declared_literal = ast.literal_eval(
        next(
            node.value
            for node in tree.body
            if isinstance(node, ast.Assign)
            and any(isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS" for target in node.targets)
        )
    )
    forbidden_surfaces = (
        "NO_GO_LEDGER.md",
        "AUDIT_LEDGER.md",
        "REVIEW_QUEUE.json",
        "TOE_PERCENTAGE_UPDATE",
    )
    return (
        tuple(declared_literal) == AUDIT_INPUT_PATHS
        and not (forbidden_calls & set(calls))
        and not any(surface in "\n".join(AUDIT_INPUT_PATHS) for surface in forbidden_surfaces)
    )


FROZEN_MUTATION_NAMES = tuple(f"frozen_{index:02d}" for index in range(1, 41))


def mutation_rejections() -> dict[str, bool]:
    q_half = q_matrix(sp.Rational(1, 2))
    q_half_flat = flatten(q_half)
    r0, r1 = binary_responses()
    half_weights = [sp.Rational(1, 2)] * 2
    half_q = mixture(half_weights, (r0, r1))
    frozen_half = kernel_history(half_weights, sp.eye(2), (r0, r1))
    reset_half = outer(half_q, half_q)
    dephased_rank = sum(
        1 for value in 4 * q_matrix(sp.Rational(2, 5)) if bool(value > 0)
    )
    rho_c = sp.diag(
        1 - LAMBDA, LAMBDA / 4, LAMBDA / 4, LAMBDA / 4, LAMBDA / 4
    )
    frozen = {
        "frozen_01": not q_family_certificate("bad_diagonal")
        and not q_family_certificate("bad_off_diagonal"),
        "frozen_02": any(value == 0 for value in q_matrix(1))
        and not scope_guard(terminal=TERMINAL_TEXT.replace("FULL-STRICT-INTERVAL", "FULL-CLOSED-INTERVAL")),
        "frozen_03": not per_law_four_cause_certificate("linear_lambda"),
        "frozen_04": not exact_frozen_locus_certificate("allow_positive"),
        "frozen_05": dephased_rank == 16
        and not scope_guard(terminal=TERMINAL_TEXT + ";MICROSCOPIC-ENVIRONMENT-RANK-FROM-MATRIX-RANK"),
        "frozen_06": not scope_guard(terminal=TERMINAL_TEXT + ";NONNEGATIVE-RANK-SELECTS-LAW"),
        "frozen_07": shared_conditional_noise_escape_certificate()
        and not scope_guard(terminal=TERMINAL_TEXT.replace("CONDITIONALLY-IID-", "")),
        "frozen_08": markov_and_stationarity_certificate()
        and matrix_zero(reset_half - outer(q_half_flat, q_half_flat))
        and not matrix_zero(frozen_half - reset_half),
        "frozen_09": use_dependent_fixed_cause_escape_certificate(),
        "frozen_10": hidden_memory_lumpability_certificate(),
        "frozen_11": not scope_guard(terminal=TERMINAL_TEXT + ";CAUSE-IS-RECORD"),
        "frozen_12": binary_equality_event_gap_certificate()
        and sp.simplify(
            3 * LAMBDA * (1 - LAMBDA) / 16
            - 9 * LAMBDA * (1 - LAMBDA) / 16
        )
        != 0,
        "frozen_13": covariance_mutation_certificate("drop_cross_terms"),
        "frozen_14": covariance_mutation_certificate("reverse_sign"),
        "frozen_15": not exact_frozen_locus_certificate("claim_every_zero_factorization"),
        "frozen_16": coherent_control_certificate()
        and not scope_guard(terminal=TERMINAL_TEXT.replace("FINITE-CLASSICAL-SCREENING-", "")),
        "frozen_17": q_matrix(1).rank() == 4
        and not scope_guard(terminal=TERMINAL_TEXT + ";BINARY-MODE-IS-COMPLETE-CAUSE"),
        "frozen_18": not fixed_five_library_certificate("four_only"),
        "frozen_19": per_law_four_cause_certificate()
        and not scope_guard(terminal=TERMINAL_TEXT + ";FIVE-MINIMAL-FOR-ONE-POSITIVE-LAW"),
        "frozen_20": LAMBDA in rho_c.free_symbols
        and not scope_guard(terminal=TERMINAL_TEXT + ";PARAMETER-RELOCATION-IS-SELECTION")
        and not scope_guard(
            terminal=TERMINAL_TEXT.replace("-OR-SUPPLIED-HISTORY-RESET-LAW", "")
        ),
        "frozen_21": lambda_dependent_response_not_common_certificate(),
        "frozen_22": not fixed_isometry_certificate("lambda_response"),
        "frozen_23": not three_supplied_bank_certificate("alias_archive")
        and not three_supplied_bank_certificate("omit_blank"),
        "frozen_24": not three_supplied_bank_certificate("host_insert")
        and not scope_guard(terminal=TERMINAL_TEXT.replace("PREINITIALIZED-DISJOINT-BANKS-", "")),
        "frozen_25": not fixed_isometry_certificate("merge_archive")
        and not scope_guard(terminal=TERMINAL_TEXT + ";NO-ENVIRONMENT-USED"),
        "frozen_26": not fixed_isometry_certificate("duplicate_control"),
        "frozen_27": not coherent_control_certificate("nonunit_phase"),
        "frozen_28": not coherent_control_certificate("wrong_angle")
        and not coherent_control_certificate("family_drift"),
        "frozen_29": not coherent_control_certificate("fixed_phase"),
        "frozen_30": dephased_rank == 16 and dephased_rank != 1,
        "frozen_31": min(h3_table(Fraction(15, 16), "epsilon_b2")) < 0
        and min(h3_table(Fraction(0), "epsilon_large")) < 0
        and not depth_three_counterhistory_certificate("family_drift"),
        "frozen_32": not depth_three_counterhistory_certificate("nonzero_sum"),
        "frozen_33": not depth_three_counterhistory_certificate("distinguished_label"),
        "frozen_34": all(
            not depth_three_counterhistory_certificate(mutation)
            for mutation in ("axis_1", "axis_2", "axis_3")
        ),
        "frozen_35": not scope_guard(terminal=TERMINAL_TEXT + ";ARBITRARY-DEPTH-RENEWAL-PROVED"),
        "frozen_36": not matrix_zero(frozen_half - reset_half)
        and not scope_guard(terminal=TERMINAL_TEXT + ";BRANCHWISE-RESET-DERIVED"),
        "frozen_37": not scope_guard(terminal=TERMINAL_TEXT + ";PHYSICAL-RENEWAL-DERIVED"),
        "frozen_38": not scope_guard(terminal=TERMINAL_TEXT + ";NN-STINESPRING-COMPILED")
        and not scope_guard(terminal=TERMINAL_TEXT + ";THIRD-BLOCK32-TRANSACTION-EXECUTED"),
        "frozen_39": not scope_guard(terminal=TERMINAL_TEXT + ";NORMALIZED-CONSERVED-SOURCE-DERIVED")
        and not scope_guard(terminal=TERMINAL_TEXT + ";GRAVITY-CLOSED"),
        "frozen_40": all(
            not scope_guard(terminal=TERMINAL_TEXT + ";" + promotion)
            for promotion in (
                "AXIOM-AMENDED",
                "AUDIT-VERDICT-APPLIED",
                "OBLIGATION-RETIRED",
                "TOE-SCORE-MOVED",
            )
        ),
    }
    scope_model = {
        f"scope_model_{name}": not scope_guard(Scope(**{name: True}))
        for name in sorted(REQUIRED_SCOPE_FIELDS)
    }
    scope_terminal = {
        f"scope_terminal_{name}": not scope_guard(
            terminal=TERMINAL_TEXT + ";" + SCOPE_TERMINAL_PROMOTIONS[name]
        )
        for name in sorted(REQUIRED_SCOPE_FIELDS)
    }
    combined = {**frozen, **scope_model, **scope_terminal}
    return {name: bool(rejected) for name, rejected in combined.items()}


def expected_mutation_names() -> set[str]:
    return (
        set(FROZEN_MUTATION_NAMES)
        | {f"scope_model_{name}" for name in REQUIRED_SCOPE_FIELDS}
        | {f"scope_terminal_{name}" for name in REQUIRED_SCOPE_FIELDS}
    )


class Checks:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def check(self, name: str, condition: bool, detail: str) -> None:
        if condition:
            self.passed += 1
            print(f"PASS {name}: {detail}")
        else:
            self.failed += 1
            print(f"FAIL {name}: {detail}")


def print_resolution_boundaries(executed: bool = True) -> None:
    if not executed:
        print(
            "per_element: checked and not executed — content identity failed before any q_lambda, covariance, or H3 science check"
        )
        print(
            "per_site: checked and not executed — content identity failed; no local M2 cause carrier or site map was constructed"
        )
        print(
            "per_mode: checked and not executed — content identity failed before finite cause or Markov modes were evaluated"
        )
        print(
            "per_block: checked and not executed — content identity failed before frozen two-use or scalar three-use composition"
        )
        print(
            "lattice_wide: checked and not executed — content identity failed; no autonomous process, source, or gravity law was constructed"
        )
        return
    print(
        "per_element: checked — all 16 q_lambda cells, the 16-by-16 covariance, and all 4,096 H3 entries were contracted exactly"
    )
    print(
        "per_site: checked and not executed — no local M2 cause carrier, Ready/Spent site map, or nearest-neighbor gate was constructed"
    )
    print(
        "per_mode: checked — the finite uniform/transverse label modes and declared binary Markov mode were evaluated; no lattice spectral mode is claimed"
    )
    print(
        "per_block: checked — frozen two-use algebra and an abstract scalar three-use counterlaw were composed; no third Block32 transaction was executed"
    )
    print(
        "lattice_wide: checked and not executed — no autonomous invocation, physical reset, cadence, arbitrary-depth process, source, or gravity law was constructed"
    )


def main() -> int:
    checks = Checks()
    identity_ok = frozen_hashes_ok()
    checks.check(
        "frozen_inputs_and_source_pin",
        identity_ok,
        f"20 literal inputs; fingerprint={input_fingerprint()}",
    )
    if not identity_ok:
        print_resolution_boundaries(executed=False)
        print("TERMINAL: INCOMPLETE-NO-SCIENCE-INFERENCE")
        print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
        return 1
    checks.check(
        "q_lambda_spectrum_rank_and_support",
        q_family_certificate(),
        "Q=(P0+lambda Pperp)/4; spectrum 1/4,lambda/4x3; det=lambda^3/256; ranks 1 then 4",
    )
    checks.check(
        "per_law_four_cause_factorization",
        per_law_four_cause_certificate(),
        "S=P0+sqrt(lambda)Pperp is stochastic/nonnegative and Q=SS^T/4",
    )
    checks.check(
        "fixed_five_response_library_minimum",
        fixed_five_library_certificate(),
        "one uniform plus four diagonal product responses realize the family; endpoint support proves five minimal",
    )
    checks.check(
        "general_frozen_covariance_identity",
        covariance_identity_certificate()
        and finite_weighted_sos_equality_schema_certificate()
        and product_response_rank_schema_certificate(),
        "generic covariance expansion plus the finite positive-weight SOS equality schema and product-response rank-one minors",
    )
    checks.check(
        "exact_existential_frozen_locus",
        exact_frozen_locus_certificate(),
        "some compatible frozen factorization exists exactly at lambda=0; inactive sectors ignored; not every lambda=0 factorization works",
    )
    checks.check(
        "markov_orientation_and_reset_locus",
        markov_and_stationarity_certificate(),
        "row-stochastic K=Pi+rho(I-Pi) has residual rho*lambda*(1-lambda) Delta tensor Delta; rho=0 is visible redraw",
    )
    checks.check(
        "live_hidden_and_use_dependent_escapes",
        hidden_memory_lumpability_certificate() and use_dependent_fixed_cause_escape_certificate(),
        "hidden memory can persist under visible redraw, and a fixed composite cause with use-dependent kernels realizes positive lambda product histories",
    )
    checks.check(
        "readable_binary_event_control",
        binary_equality_event_gap_certificate(),
        "persistent-minus-renewed excess for both complete pairs satisfying g=h is 9*lambda*(1-lambda)/16",
    )
    checks.check(
        "fixed_controlled_isometry",
        fixed_isometry_certificate(),
        "explicit 1445-row sparse Ready-subspace map has VdaggerV=I5 and full diagonal reduced output Q_lambda",
    )
    checks.check(
        "three_supplied_disjoint_banks",
        three_supplied_bank_certificate(),
        "symbolic one-use mixture plus nine preinitialized registers; all 125 cause triples and 4096 tensor cells checked exactly at lambda=2/5",
    )
    checks.check(
        "lambda_dependent_coherent_control",
        coherent_control_certificate(),
        "permutation-covariant unitary has |U_gh|^2=4q_gh; same visible table does not identify dephased versus unitary channel rank",
    )
    checks.check(
        "strict_depth_three_counterhistory",
        depth_three_counterhistory_certificate(),
        "all 4096 positive entries, 16 one-use and all three 256 pair marginals; all-diagonal cell residual b^3/2",
    )
    checks.check(
        "static_source_and_scope",
        static_source_certificate() and scope_guard(),
        "literal input manifest, read-only source, required 19-field negative scope, qualified terminal",
    )

    mutations = mutation_rejections()
    for name in FROZEN_MUTATION_NAMES:
        rejected = mutations[name]
        print(f"MUTATION {'REJECTED' if rejected else 'SURVIVED'} {name}")
    model_names = [name for name in mutations if name.startswith("scope_model_")]
    terminal_names = [name for name in mutations if name.startswith("scope_terminal_")]
    print(
        "MUTATION "
        f"{'REJECTED' if all(mutations[name] for name in model_names) else 'SURVIVED'} "
        f"scope_model_promotions_{sum(mutations[name] for name in model_names)}/{len(model_names)}"
    )
    print(
        "MUTATION "
        f"{'REJECTED' if all(mutations[name] for name in terminal_names) else 'SURVIVED'} "
        f"scope_terminal_promotions_{sum(mutations[name] for name in terminal_names)}/{len(terminal_names)}"
    )
    checks.check(
        "designated_hostile_mutations",
        set(mutations) == expected_mutation_names() and all(mutations.values()),
        f"rejected={sum(mutations.values())}/{len(mutations)}",
    )

    print_resolution_boundaries()

    if checks.failed == 0:
        print(f"TERMINAL: {TERMINAL_TEXT}")
    else:
        print("TERMINAL: INCOMPLETE-NO-SCIENCE-INFERENCE")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
