#!/usr/bin/env python3

"""Block33: conditional mathematics with a bounded current entrypoint.
Complete historical sources/controllers and results are archived outside note discovery.
Only the named checks below are fresh execution claims.
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

LAMBDA = sp.symbols("lambda", real=True, nonnegative=True)

T = sp.symbols("t", real=True, nonnegative=True)

RHO = sp.symbols("rho", real=True, nonnegative=True)

OUTCOMES = tuple(itertools.product(range(4), repeat=2))

P0 = sp.ones(4) / 4

PPER = sp.eye(4) - P0

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



ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 30
# Literal inputs and hashes are frozen after all source/note edits.
AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_D4_CLASSICAL_SCREENING_CAUSE_PERSISTENCE_RENEWAL_LOCUS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md', 'docs/ADMISSIBILITY_D4_OUTPUT_CONDITIONED_PAIR_SUCCESSOR_COMMON_TWO_USE_CYLINDER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md', 'docs/ADMISSIBILITY_D4_OUTPUT_STATUS_NN_ORDERED_PAIR_TRANSDUCER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md', 'docs/ADMISSIBILITY_D4_RETURNED_TIP_SUPPLIED_Q_CONDITIONAL_PAIR_INSTRUMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-30.md', 'docs/ADMISSIBILITY_D4_SYMBOLIC_LAMBDA_GUARDED_FINITE_SUCCESSOR_TRANSACTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
DIRECT_HASHES = {'docs/ADMISSIBILITY_D4_CLASSICAL_SCREENING_CAUSE_PERSISTENCE_RENEWAL_LOCUS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md': '157ed95dea5226b3b3bfb97cf41e3315a0f26dde3d9ea02b56ee6e5dbb398518', 'docs/ADMISSIBILITY_D4_OUTPUT_CONDITIONED_PAIR_SUCCESSOR_COMMON_TWO_USE_CYLINDER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md': '655f7bc858b859dd84580ed9eb446f74ecfb1cfb87bfd1d9a00cc2339b9c7e6b', 'docs/ADMISSIBILITY_D4_OUTPUT_STATUS_NN_ORDERED_PAIR_TRANSDUCER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md': '1e853ac20bfdd4fc9e13e07304ee5051cbe67eb9389606bbc3a3555a5be96d6a', 'docs/ADMISSIBILITY_D4_RETURNED_TIP_SUPPLIED_Q_CONDITIONAL_PAIR_INSTRUMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-30.md': '86913d27c2f428d8d510ea374541b017ac4daa380574fe3486756374e7112320', 'docs/ADMISSIBILITY_D4_SYMBOLIC_LAMBDA_GUARDED_FINITE_SUCCESSOR_TRANSACTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md': '70514e46d9d3f136f00b83817aafe49ca89d54d4f8bd684094f3a9fdc75cdd8a', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753'}

def current_inputs_ok():
    return all((ROOT/p).is_file() and hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==sha for p,sha in DIRECT_HASHES.items()) and set(DIRECT_HASHES)==set(AUDIT_INPUT_PATHS) and bool(DIRECT_HASHES)


def main():
    if not current_inputs_ok():
        print('FAIL current_source_and_note_inputs')
        print('TERMINAL: INCOMPLETE-NO-SCIENCE-INFERENCE')
        print('TOTAL: PASS=0 FAIL=1')
        return 1
    passed=1
    failed=0
    print('PASS current_source_and_note_inputs')
    ok=bool(q_family_certificate())
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'spectrum_ranks')
    ok=bool(per_law_four_cause_certificate())
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'four_cause_per_law')
    ok=bool(fixed_five_library_certificate())
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'fixed_five_library')
    ok=bool(covariance_identity_certificate() and finite_weighted_sos_equality_schema_certificate() and product_response_rank_schema_certificate())
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'finite_cause_covariance_SOS')
    ok=bool(exact_frozen_locus_certificate())
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'existential_frozen_locus')
    ok=bool(markov_and_stationarity_certificate() and hidden_memory_lumpability_certificate() and use_dependent_fixed_cause_escape_certificate())
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'Markov_and_hidden_memory')
    ok=bool(binary_equality_event_gap_certificate())
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'binary_event_distinction')
    ok=bool(fixed_isometry_certificate() and three_supplied_bank_certificate())
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'fixed_isometry_and_supplied_banks')
    ok=bool(coherent_control_certificate())
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'coherent_control')
    ok=bool(depth_three_counterhistory_certificate() and not depth_three_counterhistory_certificate("epsilon_b2") and not depth_three_counterhistory_certificate("axis_1"))
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'actual4096_three_use_and_changed_epsilon_axis')
    print('TERMINAL: '+('BLOCK33-NAMED-BOUNDED-CHECKS-COMPLETE;CONDITIONAL-PROOFS-PRESERVED' if failed==0 else 'INCOMPLETE-NO-SCIENCE-INFERENCE'))
    print(f'TOTAL: PASS={passed} FAIL={failed}')
    return int(failed!=0)

if __name__=='__main__':
    raise SystemExit(main())
