#!/usr/bin/env python3

"""Block34: conditional mathematics with a bounded current entrypoint.
Complete historical sources/controllers and results are archived outside note discovery.
Only the named checks below are fresh execution claims.
"""

from __future__ import annotations

import ast

import hashlib

import itertools

import json

import re

import subprocess

from dataclasses import dataclass, fields, replace

from functools import lru_cache

from pathlib import Path

import sympy as sp

R = sp.Rational

LAMBDA = sp.symbols("lambda", real=True)

LAMBDA_0 = sp.symbols("lambda_0", real=True)

FRONT = sp.Matrix((1, 0, 0))

LATERAL = (
    sp.Matrix((0, -1, 0)),
    sp.Matrix((0, 1, 0)),
    sp.Matrix((0, 0, -1)),
    sp.Matrix((0, 0, 1)),
)

P_FRONT = sp.eye(3) - FRONT * FRONT.T

OUTCOME_PAIRS = tuple(itertools.product(range(4), repeat=2))

def q_table(mutation: str | None = None) -> dict[tuple[int, int], sp.Expr]:
    diagonal = (1 + 3 * LAMBDA) / 16
    off_diagonal = (1 - LAMBDA) / 16
    if mutation == "bad_diagonal_weight":
        diagonal = (1 + 2 * LAMBDA) / 16
    if mutation == "bad_off_diagonal_weight":
        off_diagonal = (1 - 2 * LAMBDA) / 16
    table = {
        (g, h): diagonal if g == h else off_diagonal
        for g, h in OUTCOME_PAIRS
    }
    if mutation == "omit_outcome":
        del table[(0, 1)]
    if mutation == "break_marginal":
        table[(0, 0)] += LAMBDA / 32
        table[(1, 1)] -= LAMBDA / 32
    return table

def sum_matrix(terms, rows: int = 3, cols: int = 3) -> sp.Matrix:
    return sum(terms, sp.zeros(rows, cols))

def proper_cubic_rotations() -> tuple[sp.Matrix, ...]:
    rotations = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = sp.zeros(3)
            for row, column in enumerate(permutation):
                matrix[row, column] = signs[row]
            if matrix.det() == 1:
                rotations.append(matrix)
    return tuple(rotations)

def actual_vectors(mutation: str | None = None) -> tuple[sp.Matrix, ...]:
    if mutation != "tetrahedral_surrogate":
        return LATERAL
    root = sp.sqrt(3)
    return tuple(
        sp.Matrix(corner) / root
        for corner in ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))
    )

def geometry_certificate(mutation: str | None = None) -> bool:
    table = q_table(mutation)
    vectors = actual_vectors(mutation)
    if len(table) != 16:
        return False
    total = sp.factor(sum(table.values()))
    left = tuple(sp.factor(sum(table[g, h] for h in range(4))) for g in range(4))
    right = tuple(sp.factor(sum(table[g, h] for g in range(4))) for h in range(4))
    mean_g = sum_matrix(
        (table[g, h] * vectors[g] for g, h in table), 3, 1
    )
    mean_h = sum_matrix(
        (table[g, h] * vectors[h] for g, h in table), 3, 1
    )
    egg = sum_matrix(table[g, h] * vectors[g] * vectors[g].T for g, h in table)
    ehh = sum_matrix(table[g, h] * vectors[h] * vectors[h].T for g, h in table)
    pair = sum_matrix(table[g, h] * vectors[g] * vectors[h].T for g, h in table)
    expected_pair = LAMBDA * P_FRONT / 2
    if mutation == "bad_pair_scale":
        expected_pair = LAMBDA * P_FRONT / 3
    claimed_trace = LAMBDA if mutation != "bad_trace" else 2 * LAMBDA
    k0, k1, k2 = sp.symbols("k0 k1 k2", real=True)
    momentum = sp.Matrix((k0, k1, k2))
    expected_residual = LAMBDA * (
        momentum - (momentum.dot(FRONT)) * FRONT
    ).T / 2
    claimed_residual = momentum.T * pair
    if mutation == "claim_generic_transverse":
        claimed_residual = sp.zeros(1, 3)
    covariance = True
    for rotation in proper_cubic_rotations():
        front = rotation * FRONT
        rotated = tuple(rotation * vector for vector in vectors)
        rotated_pair = sum_matrix(
            table[g, h] * rotated[g] * rotated[h].T for g, h in table
        )
        covariance = covariance and rotated_pair == sp.simplify(
            LAMBDA * (sp.eye(3) - front * front.T) / 2
        )
    return bool(
        total == 1
        and left == (R(1, 4),) * 4
        and right == (R(1, 4),) * 4
        and all(table[g, h] == table[h, g] for g, h in table)
        and mean_g == sp.zeros(3, 1)
        and mean_h == sp.zeros(3, 1)
        and egg == P_FRONT / 2
        and ehh == P_FRONT / 2
        and pair == expected_pair
        and sp.trace(pair) == claimed_trace
        and FRONT.T * pair == sp.zeros(1, 3)
        and sp.simplify(sp.trace(pair.T * pair) - LAMBDA**2 / 2) == 0
        and sp.simplify(claimed_residual - expected_residual) == sp.zeros(1, 3)
        and len(proper_cubic_rotations()) == 24
        and covariance
    )

def homogeneous_ray_certificate(mutation: str | None = None) -> bool:
    shape = P_FRONT / 2
    tensor = LAMBDA * shape
    coefficients = sp.symbols("ell0:9", real=True)
    base_residual = sum(
        coefficients[3 * i + j] * shape[i, j]
        for i in range(3)
        for j in range(3)
    )
    residual = sum(
        coefficients[3 * i + j] * tensor[i, j]
        for i in range(3)
        for j in range(3)
    )
    if mutation == "make_homogeneous_inhomogeneous":
        residual += 1
    trace_roots = set(sp.solve(sp.Eq(sp.trace(tensor), 0), LAMBDA))
    claimed_trace_roots = trace_roots
    if mutation == "claim_positive_homogeneous_selector":
        claimed_trace_roots = {R(2, 3)}
    if mutation == "drop_zero_only_branch":
        claimed_trace_roots = set()
    gamma, amplitude, scale = sp.symbols(
        "gamma amplitude scale", nonzero=True, real=True
    )
    response = gamma * amplitude * shape
    rescaled_response = (gamma / scale) * (amplitude * scale) * shape
    if mutation == "separate_free_coupling":
        rescaled_response += shape
    normalized = sp.simplify(tensor / sp.trace(tensor))
    claimed_normalized = normalized
    if mutation == "claim_trace_normalization_keeps_lambda":
        claimed_normalized = normalized + LAMBDA * shape
    return bool(
        sp.factor(residual - LAMBDA * base_residual) == 0
        and FRONT.T * tensor == sp.zeros(1, 3)
        and claimed_trace_roots == {0}
        and response == rescaled_response
        and claimed_normalized == shape
        and sp.trace(shape) == 1
    )

def debit_recoil_certificate(mutation: str | None = None) -> bool:
    counts = parent_debit_counts(mutation)
    if counts is None:
        return False
    locked_before, blank_before, locked_after, blank_after = counts
    debit_count = blank_before - blank_after
    table = q_table()
    unordered_probability = sp.S.Zero
    unordered_tensor = sp.zeros(3)
    double_counted_tensor = sp.zeros(3)
    declared_opposite_bookkeeping_ok = True
    for g in range(4):
        for h in range(g, 4):
            probability = table[g, h] if g == h else 2 * table[g, h]
            dyad = (
                LATERAL[g] * LATERAL[g].T
                if g == h
                else (
                    LATERAL[g] * LATERAL[h].T
                    + LATERAL[h] * LATERAL[g].T
                ) / 2
            )
            unordered_probability += probability
            unordered_tensor += probability * dyad
            double_counted_tensor += (
                (2 if g != h else 1) * probability * dyad
            )
            declared_opposite_bookkeeping_ok = (
                declared_opposite_bookkeeping_ok
                and dyad + (-dyad) == sp.zeros(3)
            )
    if mutation == "double_count_pair":
        unordered_tensor = double_counted_tensor
    alpha = sp.symbols("alpha", real=True)
    conversion = alpha
    if mutation == "lambda_dependent_debit_conversion":
        conversion = alpha * LAMBDA
    source = conversion * (LAMBDA * P_FRONT / 2)
    declared_opposite = -source
    if mutation == "missing_recoil":
        declared_opposite = sp.zeros(3)
    kappa = sp.symbols("kappa", real=True)
    locus = sp.solve(sp.Eq(LAMBDA, kappa * debit_count), LAMBDA)
    samples = (sp.S.Zero, R(1, 5), R(2, 3), R(9, 10))
    conversions = tuple(sp.simplify(value / debit_count) for value in samples)
    return bool(
        debit_count == locked_after - locked_before
        and debit_count > 0
        and sp.factor(unordered_probability) == 1
        and unordered_tensor == LAMBDA * P_FRONT / 2
        and double_counted_tensor == (5 * LAMBDA - 1) * P_FRONT / 8
        and declared_opposite_bookkeeping_ok
        and sp.simplify(source + declared_opposite) == sp.zeros(3)
        and sp.diff(conversion, LAMBDA) == 0
        and locus == [debit_count * kappa]
        and all(sp.simplify(debit_count * coefficient - value) == 0
                for value, coefficient in zip(samples, conversions))
    )

@dataclass(frozen=True)
class WardCompletionResult:
    contractions_zero: bool
    ray_scaling: bool
    provenance: str
    authority_class: str
    nonzero_frequency_only: bool
    local_lattice_four_stress: bool
    cadence_supplied: bool
    zero_mode_supplied: bool

def ward_completion_result(mutation: str | None = None) -> WardCompletionResult:
    omega = sp.symbols("omega", nonzero=True, real=True)
    p0, p1, p2 = sp.symbols("p0 p1 p2", real=True)
    momentum = sp.Matrix((p0, p1, p2))
    spatial = LAMBDA * P_FRONT / 2
    mixed = spatial * momentum / omega
    temporal = (momentum.T * spatial * momentum)[0] / omega**2
    if mutation == "bad_ward_completion_sign":
        mixed = -mixed
    if mutation == "drop_time_completion":
        temporal = sp.S.Zero
    spatial_ward = sp.simplify(-omega * mixed.T + momentum.T * spatial)
    temporal_ward = sp.simplify(-omega * temporal + (momentum.T * mixed)[0])
    completed_entries = tuple(mixed) + (temporal,)
    ray_scaling = all(
        sp.simplify(entry - LAMBDA * sp.diff(entry, LAMBDA)) == 0
        for entry in completed_entries
    )
    result = WardCompletionResult(
        contractions_zero=bool(
            spatial_ward == sp.zeros(1, 3) and temporal_ward == 0
        ),
        ray_scaling=bool(ray_scaling),
        provenance="self_contained_symmetric_tensor_substitution",
        authority_class="supplied_continuum_algebra",
        nonzero_frequency_only=True,
        local_lattice_four_stress=False,
        cadence_supplied=False,
        zero_mode_supplied=False,
    )
    replacements = {
        "bad_ward_provenance": {"provenance": "landed-authority"},
        "promote_open_pr_authority": {"authority_class": "retained"},
        "promote_omega_zero_completion": {"zero_mode_supplied": True},
        "promote_local_lattice_four_stress": {"local_lattice_four_stress": True},
        "promote_cadence": {"cadence_supplied": True},
    }
    if mutation in replacements:
        result = replace(result, **replacements[mutation])
    return result

def ward_completion_certificate(mutation: str | None = None) -> bool:
    result = ward_completion_result(mutation)
    return bool(
        result.contractions_zero
        and result.ray_scaling
        and result.provenance == "self_contained_symmetric_tensor_substitution"
        and result.authority_class == "supplied_continuum_algebra"
        and result.nonzero_frequency_only
        and not result.local_lattice_four_stress
        and not result.cadence_supplied
        and not result.zero_mode_supplied
    )

def equality_off_contrast_values(
    mutation: str | None = None,
) -> tuple[sp.Expr, sp.Expr]:
    diagonal_symbol, off_symbol = sp.symbols("a b", real=True)
    solutions = sp.solve(
        (
            sp.Eq(diagonal_symbol + 3 * off_symbol, 0),
            sp.Eq(diagonal_symbol**2 + 3 * off_symbol**2, 4),
        ),
        (diagonal_symbol, off_symbol),
        dict=True,
    )
    positive = tuple(
        (solution[diagonal_symbol], solution[off_symbol])
        for solution in solutions
        if solution[diagonal_symbol].is_positive
    )
    if len(positive) != 1:
        raise AssertionError("equality/off q0-unit grammar did not have one positive orientation")
    diagonal, off_diagonal = positive[0]
    if mutation == "bad_contrast_values":
        diagonal = sp.S(2)
    return diagonal, off_diagonal

def physical_orbit(pair: tuple[int, int]) -> str:
    g, h = pair
    if g == h:
        return "same"
    if LATERAL[g].dot(LATERAL[h]) == -1:
        return "opposite"
    return "perpendicular"

def fixed_reference_score_certificate(mutation: str | None = None) -> bool:
    diagonal_count = 4
    off_count = 12
    if mutation == "bad_orbit_counts":
        off_count = 11
    diagonal, off_diagonal = equality_off_contrast_values(mutation)
    uniform_mean = sp.simplify(
        (diagonal_count * diagonal + off_count * off_diagonal) / 16
    )
    uniform_second = sp.simplify(
        (diagonal_count * diagonal**2 + off_count * off_diagonal**2) / 16
    )
    if mutation == "bad_uniform_mean_claim":
        uniform_mean += 1
    if mutation == "bad_uniform_variance_claim":
        uniform_second += 1
    table = q_table()
    values = {
        pair: diagonal if pair[0] == pair[1] else off_diagonal
        for pair in OUTCOME_PAIRS
    }
    mean = sp.factor(sum(table[pair] * values[pair] for pair in OUTCOME_PAIRS))
    second = sp.factor(
        sum(table[pair] * values[pair] ** 2 for pair in OUTCOME_PAIRS)
    )
    variance = sp.factor(second - mean**2)
    expected_mean = sp.sqrt(3) * LAMBDA
    expected_second = 1 + 2 * LAMBDA
    expected_variance = (1 - LAMBDA) * (1 + 3 * LAMBDA)
    if mutation == "bad_contrast_mean":
        expected_mean += LAMBDA
    if mutation == "bad_contrast_second":
        expected_second += LAMBDA
    if mutation == "bad_contrast_variance":
        expected_variance += LAMBDA
    roots = set(sp.solve(sp.Eq(variance, 1), LAMBDA))
    claimed_roots = roots
    if mutation == "drop_recurrence_root":
        claimed_roots = {R(2, 3)}
    nonzero_roots = {root for root in roots if root != 0}
    if mutation == "erase_zero_without_condition":
        nonzero_roots = roots
    reference_factor = sp.factor(
        ((1 - LAMBDA) * (1 + 3 * LAMBDA))
        - ((1 - LAMBDA_0) * (1 + 3 * LAMBDA_0))
    )
    expected_reference = sp.factor(
        (LAMBDA - LAMBDA_0) * (2 - 3 * (LAMBDA + LAMBDA_0))
    )
    if mutation == "hide_reference_root":
        expected_reference = LAMBDA - LAMBDA_0
    score = {
        pair: sp.factor(sp.diff(table[pair], LAMBDA) / table[pair])
        for pair in OUTCOME_PAIRS
    }
    expected_score = {
        pair: sp.factor(
            sp.sqrt(3) * (values[pair] - expected_mean) / expected_variance
        )
        for pair in OUTCOME_PAIRS
    }
    score_formula = all(
        sp.simplify(score[pair] - expected_score[pair]) == 0
        for pair in OUTCOME_PAIRS
    )
    score_at_q0 = all(
        sp.simplify(
            score[pair].subs(LAMBDA, 0) - sp.sqrt(3) * values[pair]
        ) == 0
        for pair in OUTCOME_PAIRS
    )
    fisher_information = sp.factor(
        sum(table[pair] * score[pair] ** 2 for pair in OUTCOME_PAIRS)
    )
    orbit_counts = {
        orbit: sum(physical_orbit(pair) == orbit for pair in OUTCOME_PAIRS)
        for orbit in ("same", "opposite", "perpendicular")
    }
    nuisance = {
        "same": sp.sqrt(2),
        "opposite": -sp.sqrt(2),
        "perpendicular": sp.S.Zero,
    }
    nuisance_mean = sp.simplify(
        sum(orbit_counts[orbit] * nuisance[orbit] for orbit in orbit_counts) / 16
    )
    nuisance_second = sp.simplify(
        sum(
            orbit_counts[orbit] * nuisance[orbit] ** 2
            for orbit in orbit_counts
        )
        / 16
    )
    diagonal_probability = sp.factor(
        sum(table[pair] for pair in OUTCOME_PAIRS if pair[0] == pair[1])
    )
    complement_control = (
        diagonal_probability.subs(LAMBDA, 0) == R(1, 4)
        and diagonal_probability.subs(LAMBDA, R(2, 3)) == R(3, 4)
    )
    fixed_q0_scale = sp.S.One
    if mutation == "lambda_dependent_reference":
        fixed_q0_scale = 1 / sp.sqrt(variance)
    if mutation == "hide_actual_d4_nuisance":
        nuisance_second += 1
    if mutation == "misstate_fisher_information":
        fisher_information += 1
    return bool(
        diagonal_count == 4
        and off_count == 12
        and uniform_mean == 0
        and uniform_second == 1
        and diagonal > 0
        and sp.simplify(diagonal + 3 * off_diagonal) == 0
        and mean == expected_mean
        and second == expected_second
        and sp.simplify(variance - expected_variance) == 0
        and claimed_roots == {0, R(2, 3)}
        and nonzero_roots == {R(2, 3)}
        and reference_factor == expected_reference
        and score_formula
        and score_at_q0
        and sp.simplify(fisher_information - 3 / expected_variance) == 0
        and orbit_counts == {"same": 4, "opposite": 4, "perpendicular": 8}
        and nuisance_mean == 0
        and nuisance_second == 1
        and nuisance["same"] != diagonal
        and complement_control
        and sp.diff(fixed_q0_scale, LAMBDA) == 0
    )

def absolute_normalizer_certificate(mutation: str | None = None) -> bool:
    target = sp.symbols("N", positive=True)
    radius = sp.symbols("R_source", positive=True)
    trace_locus = sp.solve(sp.Eq(LAMBDA, target), LAMBDA)
    norm_locus = sp.solve(sp.Eq(LAMBDA**2 / 2, radius**2), LAMBDA)
    positive_norm_locus = [root for root in norm_locus if root.could_extract_minus_sign() is False]
    trace_free = sp.solve(sp.Eq(LAMBDA, 0), LAMBDA)
    if mutation == "fit_absolute_target":
        target = LAMBDA
    return bool(
        trace_locus == [target]
        and set(norm_locus) == {-sp.sqrt(2) * radius, sp.sqrt(2) * radius}
        and positive_norm_locus == [sp.sqrt(2) * radius]
        and trace_free == [0]
        and sp.diff(target, LAMBDA) == 0
    )

import admissibility_d4_symbolic_lambda_guarded_state_carrier_successor_gate_2026_08_31 as block32

def parent_debit_counts(mutation=None):
    # Apply the actual finite transaction on a route-derived carrier, not prose/status regexes.
    front=block32.CANONICAL_FRONT
    _kind,g,h=block32.block31.token_order(front)[0]
    p=block32.block30.route_plan(block32.ZERO,front,g,h,block32.CHIRALITY)
    carrier=block32.block30.candidate_carrier_centers(block32.ZERO,front,block32.CHIRALITY)
    frame=block32.block30.successor_frame(p)
    locked=frozenset({p.left.start,p.right.start});blank=frozenset(carrier-locked)
    targets=(block32.block24.forward_center(frame.left_anchor,frame.left_exits[0]),block32.block24.forward_center(frame.right_anchor,frame.right_exits[0]))
    consumed=frozenset(p.left.targets+p.right.targets+targets)
    before=block32.FiniteCarrierState(block32.BLANK_SELECTOR,blank,locked)
    after=block32.apply_finite_transaction(before,0,blank,consumed)
    counts=(len(locked),len(blank),len(after.locked_centers),len(after.blank_centers))
    return counts[:-1]+(counts[-1]+1,) if mutation=='parent_debit_count_drift' else counts


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 30
# Literal inputs and hashes are frozen after all source/note edits.
AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_D4_NORMALIZED_RECORD_PAIR_SOURCE_GRAVITY_PINCER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md', 'docs/ADMISSIBILITY_D4_OUTPUT_CONDITIONED_PAIR_SUCCESSOR_COMMON_TWO_USE_CYLINDER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md', 'docs/ADMISSIBILITY_D4_OUTPUT_STATUS_NN_ORDERED_PAIR_TRANSDUCER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md', 'docs/ADMISSIBILITY_D4_RETURNED_TIP_SUPPLIED_Q_CONDITIONAL_PAIR_INSTRUMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-30.md', 'docs/ADMISSIBILITY_D4_SYMBOLIC_LAMBDA_GUARDED_FINITE_SUCCESSOR_TRANSACTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/audit/data/axiom_premise_nodes.json', 'scripts/admissibility_d4_nn_record_relation_transducer_dispatch_gate_2026_08_31.py', 'scripts/admissibility_d4_output_conditioned_pair_successor_handoff_gate_2026_08_31.py', 'scripts/admissibility_d4_prior_record_live_preparation_two_event_prefix_2026_08_30.py', 'scripts/admissibility_d4_returned_tip_strict_support_analytic_coupling_gate_2026_08_30.py', 'scripts/admissibility_d4_self_delimiting_forward_record_append_history_2026_08_30.py', 'scripts/admissibility_d4_symbolic_lambda_guarded_state_carrier_successor_gate_2026_08_31.py')
DIRECT_HASHES = {'docs/ADMISSIBILITY_D4_NORMALIZED_RECORD_PAIR_SOURCE_GRAVITY_PINCER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md': 'd850a387515e06f684191e06ac7750551f69c132c3d1b852fcfbe498042129e0', 'docs/ADMISSIBILITY_D4_OUTPUT_CONDITIONED_PAIR_SUCCESSOR_COMMON_TWO_USE_CYLINDER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md': '655f7bc858b859dd84580ed9eb446f74ecfb1cfb87bfd1d9a00cc2339b9c7e6b', 'docs/ADMISSIBILITY_D4_OUTPUT_STATUS_NN_ORDERED_PAIR_TRANSDUCER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md': '1e853ac20bfdd4fc9e13e07304ee5051cbe67eb9389606bbc3a3555a5be96d6a', 'docs/ADMISSIBILITY_D4_RETURNED_TIP_SUPPLIED_Q_CONDITIONAL_PAIR_INSTRUMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-30.md': '86913d27c2f428d8d510ea374541b017ac4daa380574fe3486756374e7112320', 'docs/ADMISSIBILITY_D4_SYMBOLIC_LAMBDA_GUARDED_FINITE_SUCCESSOR_TRANSACTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md': '70514e46d9d3f136f00b83817aafe49ca89d54d4f8bd684094f3a9fdc75cdd8a', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/audit/data/axiom_premise_nodes.json': '615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37', 'scripts/admissibility_d4_nn_record_relation_transducer_dispatch_gate_2026_08_31.py': '2a0651c82f4d0416bc400c9b444d0ea65e388cfa18c3b02e78d24963f1379c22', 'scripts/admissibility_d4_output_conditioned_pair_successor_handoff_gate_2026_08_31.py': '62721ae1b16c8b5bbbdc7cb5356513367997fbb6a1de1cb771348e172bdd20ba', 'scripts/admissibility_d4_prior_record_live_preparation_two_event_prefix_2026_08_30.py': 'a454b4ce47af92bbf55550ebae068ff4a419b141d916b0c4fcdc1678bf283a7e', 'scripts/admissibility_d4_returned_tip_strict_support_analytic_coupling_gate_2026_08_30.py': '54b5d7faac7d6bc3484619d09e30b4b8f27efc84677142a48a5fe24f995d105d', 'scripts/admissibility_d4_self_delimiting_forward_record_append_history_2026_08_30.py': '5eb733c3a50da1f7c1bb8a46b547b1b91fd85c27856e425d8040305b3d009d6c', 'scripts/admissibility_d4_symbolic_lambda_guarded_state_carrier_successor_gate_2026_08_31.py': '1a35ad599d70e52b8296df13e3c1b18b210d7a35082728fee6e87ee3a9b09987'}

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
    ok=bool(geometry_certificate())
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'actual_lateral_moments')
    ok=bool(homogeneous_ray_certificate())
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'homogeneous_ray')
    ok=bool(debit_recoil_certificate() and not debit_recoil_certificate("double_count_pair"))
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'actual_debit_and_count_once')
    ok=bool(ward_completion_certificate() and not ward_completion_certificate("bad_ward_completion_sign"))
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'nonzero_Ward_and_changed_sign')
    ok=bool(fixed_reference_score_certificate())
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'reference_score_Fisher_orbits')
    ok=bool(absolute_normalizer_certificate())
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'conditional_absolute_target')
    print('TERMINAL: '+('BLOCK34-NAMED-BOUNDED-CHECKS-COMPLETE;CONDITIONAL-PROOFS-PRESERVED' if failed==0 else 'INCOMPLETE-NO-SCIENCE-INFERENCE'))
    print(f'TOTAL: PASS={passed} FAIL={failed}')
    return int(failed!=0)

if __name__=='__main__':
    raise SystemExit(main())
