#!/usr/bin/env python3
"""Exact C4 Berezin action -> OS Gram/Fock boundary -> Record decision surface.

The runner starts from one rational two-slice Grassmann action.  It extracts
the coherent-boundary coefficient matrix from the action cross factor, rather
than supplying a Fock operator, and joins that matrix to the exact OS
reconstruction.  Exact index raising also checks whether the coefficient
array is Gram data or a translated correlator; here it is the Gram and yields
the identity Riesz operator.  The resulting finite statement remains
conditional on the physical matter-functional identification (I-4), action
selection, temporal extension, physical time, preparation, and Record
formation.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import subprocess
from dataclasses import dataclass
from fractions import Fraction
from functools import reduce
from pathlib import Path

import sympy as sp

import gl_f_identification_bridge_check_2026_06_11 as bridge


ROOT = Path(__file__).resolve().parents[1]
PACKET = (
    ".claude/science/physics-loops/"
    "toe-matter-os-action-record-closure-block45-20260901"
)
BASE_COMMIT = "2cea9a595ee2f0a6c47096de6f821b905182f48c"
PREREG_COMMIT = "cc2ee3f63f"
BLOCK44_COMMIT = "73eccf9394"
MINIMAL_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
MINIMAL_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"

FROZEN_PACKET_BLOBS = {
    f"{PACKET}/GOAL.md": "ea2c918df2dc87bcf7ebd3b90c766b50dfd522f9",
    f"{PACKET}/EXACT_TARGET_CONTRACT.md": "2b311ddf494fd47b166c453a0424cdbed943e780",
    f"{PACKET}/ASSUMPTIONS_AND_IMPORTS.md": "bc9d08bb9d8c1c1aca69850838ec8c3379ca9108",
    f"{PACKET}/ROUTE_PORTFOLIO.md": "6b73f04eff6b57f5f8b0e5361c4f72dde2ad0767",
    f"{PACKET}/MUTATION_PLAN.md": "ccd0745b60c36432cec0b10c4f7a2884b8287eb7",
    f"{PACKET}/OPPORTUNITY_QUEUE.md": "138ca9bcbd6518e1b4b47ad4833a204893f3a032",
    f"{PACKET}/PRIOR_ART_SEARCH.md": "6dceeeb9a88f13cafdf103a59d9537eb1fed1bac",
    f"{PACKET}/TRACE_GATE.md": "7bbdcaf32411c690b9e84e7b16ce6c530b0f70c1",
}

PINNED_MAIN_BLOBS = {
    MINIMAL_PATH: MINIMAL_BLOB,
    "scripts/gl_f_berezin_rp_reconstruction_check_2026_06_10.py":
        "cfa1c5e266341320870984f8eb3f3f3feb5184af",
    "scripts/gl_f_identification_bridge_check_2026_06_11.py":
        "8143748090f96060c89e5bd7e21630575c9903dd",
    "docs/GL_F_FROM_BEREZIN_RP_RECONSTRUCTION_NARROW_THEOREM_NOTE_2026-06-10.md":
        "b05b0b39f9d04d5da90a27221a77e7845d686324",
    "docs/GL_F_IDENTIFICATION_BRIDGE_DECOMPOSITION_NARROW_THEOREM_NOTE_2026-06-11.md":
        "8bc8a4f90efc6494727ae39a377b128b22f01bc2",
    "docs/AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md":
        "115124dc81bac6b890d8a7095346209906a66ce5",
    "docs/FREE_STAGGERED_D_DIMENSIONAL_TWO_STEP_MANY_BODY_TRANSFER_IDENTITY_NOTE_2026-07-20.md":
        "f5b2569c5f69fc1b81a749d6437b3ec9b90d90fe",
    "docs/CORNER_AXIS_FREE_TRANSFER_EXTENSION_PER_CHANNEL_TRACE_CORRESPONDENCE_AND_MODE_SET_FORK_BOUNDED_NOTE_2026-06-12.md":
        "64237e2d511082281643f96ed2baa76169275986",
    "scripts/frontier_transfer_trace_correspondence_fixes_kernel_normalization_2026_06_12.py":
        "ac84cea6d21d0780f40e8b14190da3425dc8ca24",
}

PINNED_BLOCK44_BLOBS = {
    "scripts/admissibility_same_law_plaquette_noether_record_statistics_discriminator_2026_09_01.py":
        "ebe2cc9c21f7cb49d03e839e4127b7034dd96b42",
    f".claude/science/physics-loops/toe-matter-noether-record-vertical-slice-block44-20260901/POSTEXECUTION_NOVELTY_AUDIT.md":
        "92d00fa5fc0d241df4cbb34ce3ed2e68cb529791",
}

# Current mutable inputs; original Git pins below remain historical identities.
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    'docs/MINIMAL_AXIOMS_2026-06-29.md',
    'scripts/gl_f_berezin_rp_reconstruction_check_2026_06_10.py',
    'scripts/gl_f_identification_bridge_check_2026_06_11.py',
    'docs/GL_F_FROM_BEREZIN_RP_RECONSTRUCTION_NARROW_THEOREM_NOTE_2026-06-10.md',
    'docs/GL_F_IDENTIFICATION_BRIDGE_DECOMPOSITION_NARROW_THEOREM_NOTE_2026-06-11.md',
    'docs/AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md',
    'archive/notes/docs/FREE_STAGGERED_D_DIMENSIONAL_TWO_STEP_MANY_BODY_TRANSFER_IDENTITY_NOTE_2026-07-20.md',
    'docs/CORNER_AXIS_FREE_TRANSFER_EXTENSION_PER_CHANNEL_TRACE_CORRESPONDENCE_AND_MODE_SET_FORK_BOUNDED_NOTE_2026-06-12.md',
    'scripts/frontier_transfer_trace_correspondence_fixes_kernel_normalization_2026_06_12.py',
    '.claude/science/physics-loops/toe-matter-os-action-record-closure-block45-20260901/GOAL.md',
    '.claude/science/physics-loops/toe-matter-os-action-record-closure-block45-20260901/EXACT_TARGET_CONTRACT.md',
    '.claude/science/physics-loops/toe-matter-os-action-record-closure-block45-20260901/ASSUMPTIONS_AND_IMPORTS.md',
    '.claude/science/physics-loops/toe-matter-os-action-record-closure-block45-20260901/ROUTE_PORTFOLIO.md',
    '.claude/science/physics-loops/toe-matter-os-action-record-closure-block45-20260901/MUTATION_PLAN.md',
    '.claude/science/physics-loops/toe-matter-os-action-record-closure-block45-20260901/OPPORTUNITY_QUEUE.md',
    '.claude/science/physics-loops/toe-matter-os-action-record-closure-block45-20260901/PRIOR_ART_SEARCH.md',
    '.claude/science/physics-loops/toe-matter-os-action-record-closure-block45-20260901/TRACE_GATE.md',
    'docs/C4_BEREZIN_COEFFICIENT_GRAM_AND_SUPPLIED_RECORD_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-08.md',
)
CURRENT_PATH_ALIASES = {'docs/FREE_STAGGERED_D_DIMENSIONAL_TWO_STEP_MANY_BODY_TRANSFER_IDENTITY_NOTE_2026-07-20.md': 'archive/notes/docs/FREE_STAGGERED_D_DIMENSIONAL_TWO_STEP_MANY_BODY_TRANSFER_IDENTITY_NOTE_2026-07-20.md'}
CURRENT_NOTE_PATH = 'docs/C4_BEREZIN_COEFFICIENT_GRAM_AND_SUPPLIED_RECORD_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-08.md'
CURRENT_NOTE_SHA256 = '5d62c7dd12ffb7dd46a08ccb0356f8ca03cec8b34080e0eec00a49beb15b4c05'

MUTATIONS = (
    "change_kernel_entry",
    "break_positive_square_root",
    "wrong_kernel_generator_polynomial",
    "theta_asymmetric_action",
    "indefinite_action_kernel",
    "commuting_nilpotent_integrand",
    "skip_coherent_coefficient_extraction",
    "rescale_vacuum_coefficient",
    "permanent_instead_of_determinant",
    "break_Gamma_composition",
    "wrong_transfer_generator",
    "insert_JW_without_intertwiner",
    "claim_hard_core_intertwiner",
    "chemical_shift_changes_Q2_dynamics",
    "reverse_current_01",
    "delete_current_01",
    "target_adjacent_occupancy",
    "product_specific_writer",
    "overwrite_pointer",
    "claim_I4_closed",
    "claim_Born_frequencies",
    "conflate_Gram_with_transfer",
)

N = 4
DIM = 2**N
EDGES = ((0, 1), (1, 2), (2, 3), (3, 0))
TWO_PARTICLE_BASIS = (3, 5, 6, 9, 10, 12)


@dataclass
class Harness:
    passed: int = 0
    failed: int = 0

    def check(self, label: str, condition: bool, detail: str) -> None:
        if condition:
            self.passed += 1
            print(f"PASS {label} :: {detail}")
        else:
            self.failed += 1
            print(f"FAIL {label} :: {detail}")


def git_blob(commit: str, path: str) -> str:
    return subprocess.run(
        ["git", "rev-parse", f"{commit}:{path}"],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout.strip()


def worktree_blob(path: str) -> str:
    return subprocess.run(
        ["git", "hash-object", path],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout.strip()


def matrix_zero(matrix: sp.MatrixBase) -> bool:
    return all(sp.simplify(value) == 0 for value in matrix)


def positive_definite_exact(matrix: sp.MatrixBase) -> bool:
    """Sylvester certificate for exact real symmetric matrices."""
    if matrix != matrix.T:
        return False
    return all(
        sp.simplify(matrix[:size, :size].det()) > 0
        for size in range(1, matrix.rows + 1)
    )


def ket(index: int, dimension: int) -> sp.Matrix:
    result = sp.zeros(dimension, 1)
    result[index, 0] = 1
    return result


def to_fraction(value: sp.Expr | int | Fraction) -> Fraction:
    value = sp.Rational(value)
    return Fraction(int(value.p), int(value.q))


def fraction_rows(matrix: sp.MatrixBase) -> list[list[Fraction]]:
    return [[to_fraction(matrix[i, j]) for j in range(matrix.cols)] for i in range(matrix.rows)]


def sympy_matrix(matrix: list[list[Fraction]]) -> sp.Matrix:
    return sp.Matrix(
        [[sp.Rational(value.numerator, value.denominator) for value in row] for row in matrix]
    )


def adjoint(matrix: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix(matrix.conjugate().T)


def source_binding_certificate(harness: Harness, mutation: str | None) -> None:
    prereg_pinned = sum(
        git_blob(PREREG_COMMIT, path) == blob
        for path, blob in FROZEN_PACKET_BLOBS.items()
    )
    prereg_unchanged = sum(
        worktree_blob(path) == blob for path, blob in FROZEN_PACKET_BLOBS.items()
    )
    main_pinned = sum(
        git_blob(BASE_COMMIT, path) == blob
        and worktree_blob(CURRENT_PATH_ALIASES.get(path, path)) == blob
        for path, blob in PINNED_MAIN_BLOBS.items()
    )
    block44_pinned = sum(
        git_blob(BLOCK44_COMMIT, path) == blob
        for path, blob in PINNED_BLOCK44_BLOBS.items()
    )
    target = (ROOT / PACKET / "EXACT_TARGET_CONTRACT.md").read_text()
    harness.check(
        "preregistration, parent science, and Block 44 comparison are source-bound",
        prereg_pinned == len(FROZEN_PACKET_BLOBS)
        and prereg_unchanged == len(FROZEN_PACKET_BLOBS)
        and main_pinned == len(PINNED_MAIN_BLOBS)
        and block44_pinned == len(PINNED_BLOCK44_BLOBS)
        and hashlib.sha256((ROOT / CURRENT_NOTE_PATH).read_bytes()).hexdigest() == CURRENT_NOTE_SHA256
        and "is postulated" in target
        and "physical-functional identification" in target,
        f"prereg={prereg_pinned}/{len(FROZEN_PACKET_BLOBS)} "
        f"unchanged={prereg_unchanged}/{len(FROZEN_PACKET_BLOBS)} "
        f"main={main_pinned}/{len(PINNED_MAIN_BLOBS)} "
        f"block44={block44_pinned}/{len(PINNED_BLOCK44_BLOBS)}",
    )


def base_source_matrices() -> tuple[sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix]:
    adjacency = sp.Matrix(
        [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]
    )
    h = -adjacency
    g = h + 3 * sp.eye(N)
    B = sp.Matrix(
        [[25, 15, 9, 15], [15, 25, 15, 9], [9, 15, 25, 15], [15, 9, 15, 25]]
    ) / 128
    K = sp.Matrix(
        [
            [289, 255, 225, 255],
            [255, 289, 255, 225],
            [225, 255, 289, 255],
            [255, 225, 255, 289],
        ]
    ) / 4096
    return h, g, B, K


def action_matrices(mutation: str | None) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix]:
    h, g, B, K = base_source_matrices()
    B = sp.Matrix(B)
    K = sp.Matrix(K)
    if mutation == "change_kernel_entry":
        K[0, 0] += sp.Rational(1, 4096)
    elif mutation == "theta_asymmetric_action":
        K[0, 1] += sp.Rational(1, 4096)
    elif mutation == "indefinite_action_kernel":
        K[0, 0] -= 1
    if mutation == "break_positive_square_root":
        B[0, 0] += sp.Rational(1, 128)
    return h, g, B, K


def d4_permutations() -> tuple[tuple[int, ...], ...]:
    result = []
    for shift in range(N):
        result.append(tuple((site + shift) % N for site in range(N)))
        result.append(tuple((-site + shift) % N for site in range(N)))
    return tuple(result)


def permutation_matrix(permutation: tuple[int, ...]) -> sp.Matrix:
    result = sp.zeros(N)
    for source, target in enumerate(permutation):
        result[target, source] = 1
    return result


def source_kernel_certificate(
    harness: Harness, mutation: str | None
) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix]:
    h, expected_g, B, K = action_matrices(mutation)
    polynomial_constant = 1312 if mutation == "wrong_kernel_generator_polynomial" else 1311
    recovered_g = (
        131072 * K**2 - 36992 * K + polynomial_constant * sp.eye(N)
    ) / 255
    frames = d4_permutations()
    d4_ok = all(
        matrix_zero(permutation_matrix(frame) * K * permutation_matrix(frame).T - K)
        and matrix_zero(permutation_matrix(frame) * B * permutation_matrix(frame).T - B)
        for frame in frames
    )
    positive_B = positive_definite_exact(B)
    positive_K = positive_definite_exact(K)
    square_ok = matrix_zero(B**2 - K)
    recovery_ok = matrix_zero(recovered_g - expected_g)
    locality_ok = matrix_zero(recovered_g - 3 * sp.eye(N) - h)
    harness.check(
        "one positive D4 action kernel exactly recovers the local C4 generator",
        K == K.T
        and B == B.T
        and positive_B
        and positive_K
        and square_ok
        and recovery_ok
        and locality_ok
        and d4_ok,
        f"B2=K:{square_ok} positive=({positive_B},{positive_K}) "
        f"recover_g={recovery_ok} D4={d4_ok}",
    )
    return h, recovered_g, B, K


def subset_for_index(index: int) -> tuple[int, ...]:
    return tuple(site for site in range(N) if (index >> (N - 1 - site)) & 1)


def permanent(matrix: sp.MatrixBase) -> sp.Expr:
    if matrix.rows == 0:
        return sp.Integer(1)
    return sp.simplify(
        sum(
            sp.prod(matrix[row, permutation[row]] for row in range(matrix.rows))
            for permutation in itertools.permutations(range(matrix.cols))
        )
    )


def cross_exponential(matrix: sp.MatrixBase) -> dict[int, Fraction]:
    """Exterior polynomial exp(sum_ij bar_eta_i M_ij xi_j)."""
    result: dict[int, Fraction] = {0: Fraction(1)}
    for left in range(N):
        for right in range(N):
            coefficient = to_fraction(matrix[left, right])
            if not coefficient:
                continue
            mask, sign = bridge.mul_mono(1 << left, 1 << (N + right), -1)
            factor = {0: Fraction(1), mask: sign * coefficient}
            result = bridge.amul(result, factor, -1)
    return result


def coefficient_gamma(
    matrix: sp.MatrixBase,
    mutation: str | None,
    role: str,
) -> tuple[sp.Matrix, bool, bool]:
    polynomial = cross_exponential(matrix)
    gamma = sp.zeros(DIM)
    determinant_identity = True
    for row in range(DIM):
        target = subset_for_index(row)
        for column in range(DIM):
            source = subset_for_index(column)
            if len(target) != len(source):
                continue
            degree = len(target)
            mask = sum(1 << site for site in target) + sum(
                1 << (N + site) for site in source
            )
            raw = sp.Rational(polynomial.get(mask, Fraction(0)).numerator,
                              polynomial.get(mask, Fraction(0)).denominator)
            phase = -1 if ((degree * (degree - 1) // 2) % 2) else 1
            submatrix = matrix.extract(target, source)
            determinant = sp.det(submatrix) if degree else sp.Integer(1)
            determinant_identity = determinant_identity and sp.simplify(raw - phase * determinant) == 0
            value = sp.simplify(raw / phase)
            if mutation == "permanent_instead_of_determinant":
                value = permanent(submatrix)
            gamma[row, column] = value
    if mutation == "rescale_vacuum_coefficient" and role == "K":
        gamma *= 2
    if mutation == "break_Gamma_composition" and role == "B":
        gamma[1, 1] += 1
    extracted = mutation != "skip_coherent_coefficient_extraction"
    return sp.Matrix(gamma), determinant_identity, extracted


def coherent_kernel_certificate(
    harness: Harness,
    mutation: str | None,
    B: sp.Matrix,
    K: sp.Matrix,
) -> tuple[sp.Matrix, sp.Matrix]:
    gamma_K, determinant_K, extracted = coefficient_gamma(K, mutation, "K")
    gamma_B, determinant_B, _ = coefficient_gamma(B, mutation, "B")
    gamma_I, determinant_I, _ = coefficient_gamma(sp.eye(N), mutation, "I")
    vacuum_ok = gamma_K[0, 0] == 1 and all(
        gamma_K[row, 0] == (1 if row == 0 else 0) for row in range(DIM)
    )
    composition_ok = matrix_zero(gamma_B**2 - gamma_K)
    identity_ok = matrix_zero(gamma_I - sp.eye(DIM))
    trace_ok = sp.simplify(sp.trace(gamma_K) - (sp.eye(N) + K).det()) == 0
    harness.check(
        "the action cross-kernel coefficients derive normalized Gamma(K) and its composition law",
        extracted
        and determinant_K
        and determinant_B
        and determinant_I
        and vacuum_ok
        and identity_ok
        and composition_ok
        and trace_ok,
        f"det_coeff={determinant_K} vacuum={vacuum_ok} GammaI={identity_ok} "
        f"GammaB2={composition_ok} trace={trace_ok}",
    )
    return gamma_K, gamma_B


def reconstruction_certificate(
    harness: Harness, mutation: str | None, K: sp.Matrix
) -> dict:
    eps = 1 if mutation == "commuting_nilpotent_integrand" else -1
    build_error = None
    try:
        reconstruction = bridge.build_reconstruction(N, fraction_rows(K), eps)
    except Exception as error:  # invalid hostile action must fail, not crash the suite
        build_error = type(error).__name__
        _, _, _, base_K = base_source_matrices()
        reconstruction = bridge.build_reconstruction(N, fraction_rows(base_K), -1)
    model = reconstruction["model"]
    gram = reconstruction["G"]
    occupation_gram = reconstruction["Gp"]
    theta_ok = model.theta(model.S) == model.S
    symmetric = all(
        gram[left][right] == gram[right][left]
        for left in range(len(gram))
        for right in range(len(gram))
    )
    psd, rank = bridge.ldl_psd(gram)
    occupation_psd, occupation_rank = bridge.ldl_psd(occupation_gram)
    harness.check(
        "the same action has a Theta-symmetric reflection-positive rank-16 OS reconstruction",
        build_error is None
        and eps == -1
        and theta_ok
        and model.Ztop != 0
        and symmetric
        and psd
        and rank == DIM
        and occupation_psd
        and occupation_rank == DIM,
        f"eps={eps} theta={theta_ok} PSD={psd} rank={rank} "
        f"occupation_rank={occupation_rank} error={build_error}",
    )
    reconstruction["build_error"] = build_error
    reconstruction["eps_used"] = eps
    return reconstruction


def os_index_type_certificate(
    harness: Harness,
    mutation: str | None,
    reconstruction: dict,
    gamma_K: sp.Matrix,
) -> bool:
    """Distinguish a covariant OS bilinear from a mixed-index operator.

    In the helper's occupation-class order, the cross-kernel coefficient
    array is the OS Gram itself.  Raising its first index therefore produces
    the identity endomorphism.  Calling the same covariant array Gamma(K) a
    nontrivial OS time translation would conflate tensor types.
    """
    standard_indices = []
    for mask in reconstruction["occ"]:
        occupied = tuple(
            site
            for site in range(N)
            if mask & (1 << reconstruction["model"].idx(1, site, 1))
        )
        standard_indices.append(sum(1 << (N - 1 - site) for site in occupied))
    coefficient_bilinear = gamma_K.extract(standard_indices, standard_indices)
    metric = sympy_matrix(reconstruction["Gp"])
    same_covariant_array = matrix_zero(metric - coefficient_bilinear)
    raised_endomorphism = sp.simplify(metric.inv() * coefficient_bilinear)
    raised_is_identity = matrix_zero(raised_endomorphism - sp.eye(DIM))
    coefficient_is_nontrivial = not matrix_zero(coefficient_bilinear - sp.eye(DIM))
    honest_boundary = mutation != "conflate_Gram_with_transfer"
    hard_target_closed = not (
        same_covariant_array and raised_is_identity and coefficient_is_nontrivial
    )
    harness.check(
        "the two-slice coefficient array is OS Gram data, not a nontrivial time-translation operator",
        same_covariant_array
        and raised_is_identity
        and coefficient_is_nontrivial
        and honest_boundary
        and not hard_target_closed,
        f"C=G:{same_covariant_array} G^-1C=I:{raised_is_identity} "
        f"C_nontrivial={coefficient_is_nontrivial} target_closed={hard_target_closed}",
    )
    return hard_target_closed


def gp_adjoint(matrix: list[list[Fraction]], reconstruction: dict) -> list[list[Fraction]]:
    return bridge.mat_mul(
        reconstruction["Gp_inv"],
        bridge.mat_mul(bridge.mat_T(matrix), reconstruction["Gp"]),
    )


def field_linear_combination(
    coefficients: list[list[Fraction]],
    fields: list[list[list[Fraction]]],
) -> list[list[list[Fraction]]]:
    result = []
    for row in coefficients:
        value = [[Fraction(0)] * DIM for _ in range(DIM)]
        for coefficient, field in zip(row, fields):
            if coefficient:
                value = bridge.mat_add(
                    value,
                    [[coefficient * entry for entry in field_row] for field_row in field],
                )
        result.append(value)
    return result


def reconstructed_car_certificate(
    harness: Harness,
    mutation: str | None,
    reconstruction: dict,
    B: sp.Matrix,
    K: sp.Matrix,
) -> tuple[list[list[list[Fraction]]], list[list[list[Fraction]]]]:
    psi = reconstruction["psi"]
    psi_dagger = [gp_adjoint(field, reconstruction) for field in psi]
    try:
        covariance = fraction_rows(K.inv())
    except Exception:
        covariance = [[Fraction(0)] * N for _ in range(N)]
    covariance_ok = True
    for left in range(N):
        for right in range(N):
            scalar, value = bridge.is_scalar(
                bridge.anticomm(psi[left], psi_dagger[right])
            )
            covariance_ok = covariance_ok and scalar and value == covariance[left][right]
    fields = field_linear_combination(fraction_rows(B), psi)
    daggers = [gp_adjoint(field, reconstruction) for field in fields]
    car_aa = all(
        bridge.is_zero(bridge.anticomm(fields[left], fields[right]))
        for left in range(N)
        for right in range(N)
    )
    car_ad = True
    for left in range(N):
        for right in range(N):
            scalar, value = bridge.is_scalar(
                bridge.anticomm(fields[left], daggers[right])
            )
            car_ad = car_ad and scalar and value == Fraction(left == right)
    harness.check(
        "the reflected functional fixes K^-1 covariance and B-normalized CAR",
        covariance_ok and car_aa and car_ad and reconstruction["eps_used"] == -1,
        f"covariance={covariance_ok} CAR_aa={car_aa} CAR_ad={car_ad}",
    )
    return fields, daggers


def standard_fields() -> tuple[
    list[list[list[Fraction]]], list[list[list[Fraction]]]
]:
    one = Fraction(1)
    identity = [[one, Fraction(0)], [Fraction(0), one]]
    z = [[one, Fraction(0)], [Fraction(0), -one]]
    lowering = [[Fraction(0), one], [Fraction(0), Fraction(0)]]
    jw = []
    hard_core = []
    for site in range(N):
        jw.append(bridge.kron_list([z] * site + [lowering] + [identity] * (N - site - 1)))
        hard_core.append(
            bridge.kron_list([identity] * site + [lowering] + [identity] * (N - site - 1))
        )
    return jw, hard_core


def dictionary_certificate(
    harness: Harness,
    mutation: str | None,
    reconstruction: dict,
    fields: list[list[list[Fraction]]],
    daggers: list[list[list[Fraction]]],
) -> tuple[sp.Matrix | None, list[list[list[Fraction]]], list[list[list[Fraction]]]]:
    jw, hard_core = standard_fields()
    pairs = []
    for site in range(N):
        pairs.append((fields[site], jw[site]))
        pairs.append((daggers[site], bridge.mat_T(jw[site])))
    jw_kernel = bridge.sylvester_kernel(pairs, DIM)
    S = sp.Matrix(jw_kernel[0]) if jw_kernel else None
    full_rank = S is not None and S.rank() == DIM
    metric_ok = False
    scale = None
    if full_rank:
        st_s = S.T * S
        metric = sympy_matrix(reconstruction["Gp"])
        for row in range(DIM):
            for column in range(DIM):
                if metric[row, column] != 0:
                    scale = sp.simplify(st_s[row, column] / metric[row, column])
                    break
            if scale is not None:
                break
        metric_ok = scale is not None and scale > 0 and matrix_zero(st_s - scale * metric)
    hard_pairs = []
    for site in range(N):
        hard_pairs.append((fields[site], hard_core[site]))
        hard_pairs.append((daggers[site], bridge.mat_T(hard_core[site])))
    hard_kernel = bridge.sylvester_kernel(hard_pairs, DIM)
    claim_ok = mutation not in {
        "insert_JW_without_intertwiner",
        "claim_hard_core_intertwiner",
    }
    harness.check(
        "the reconstructed dictionary is uniquely CAR and excludes the hard-core frame",
        len(jw_kernel) == 1
        and full_rank
        and metric_ok
        and len(hard_kernel) == 0
        and claim_ok,
        f"JW_nullity={len(jw_kernel)} rank={S.rank() if S is not None else 0} "
        f"metric={metric_ok} hard_core_nullity={len(hard_kernel)}",
    )
    return S, jw, hard_core


def bilinear(
    annihilators: list[list[list[Fraction]]],
    creators: list[list[list[Fraction]]],
    one_particle: sp.MatrixBase,
) -> sp.Matrix:
    result = sp.zeros(DIM)
    for left in range(N):
        for right in range(N):
            coefficient = sp.Rational(one_particle[left, right])
            if coefficient:
                result += coefficient * sympy_matrix(
                    bridge.mat_mul(creators[left], annihilators[right])
                )
    return sp.Matrix(result)


def spectral_function(
    matrix: sp.MatrixBase, values: dict[sp.Expr, sp.Expr]
) -> sp.Matrix:
    identity = sp.eye(matrix.rows)
    output = sp.zeros(matrix.rows)
    eigenvalues = tuple(values)
    for eigenvalue in eigenvalues:
        projector = sp.eye(matrix.rows)
        for other in eigenvalues:
            if other != eigenvalue:
                projector = sp.simplify(
                    projector * (matrix - other * identity) / (eigenvalue - other)
                )
        output += values[eigenvalue] * projector
    return sp.Matrix(output.applyfunc(sp.simplify))


def transfer_generator_certificate(
    harness: Harness,
    mutation: str | None,
    reconstruction: dict,
    fields: list[list[list[Fraction]]],
    daggers: list[list[list[Fraction]]],
    S: sp.Matrix | None,
    jw: list[list[list[Fraction]]],
    gamma_K: sp.Matrix,
    K: sp.Matrix,
    recovered_g: sp.Matrix,
) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    g_transfer = sp.Matrix(recovered_g)
    if mutation == "wrong_transfer_generator":
        g_transfer += sp.eye(N)
    jw_daggers = [bridge.mat_T(field) for field in jw]
    standard_generator = bilinear(jw, jw_daggers, g_transfer)
    reconstructed_generator = bilinear(fields, daggers, g_transfer)
    eigenvalues = tuple(sorted(standard_generator.eigenvals(), key=lambda value: int(value)))
    exact_exponential = spectral_function(
        standard_generator, {value: sp.Rational(1, 4) ** value for value in eigenvalues}
    )
    transfer_ok = matrix_zero(gamma_K - exact_exponential)
    intertwining_ok = S is not None and matrix_zero(
        S * reconstructed_generator - standard_generator * S
    )
    creator_covariance = True
    for source in range(N):
        left = gamma_K * sympy_matrix(jw_daggers[source])
        right = sum(
            (
                K[target, source]
                * sympy_matrix(jw_daggers[target])
                * gamma_K
                for target in range(N)
            ),
            sp.zeros(DIM),
        )
        creator_covariance = creator_covariance and matrix_zero(left - right)
    positive = positive_definite_exact(gamma_K)
    harness.check(
        "the flat-boundary coefficient matrix has the exterior-power spectrum tied to the reconstructed bilinear",
        transfer_ok and intertwining_ok and creator_covariance and positive,
        f"Gamma=4^-dGamma(g):{transfer_ok} intertwining={intertwining_ok} "
        f"creator_covariance={creator_covariance} positive={positive}",
    )
    return standard_generator, reconstructed_generator, g_transfer


def fixed_charge_hopping_certificate(
    harness: Harness,
    mutation: str | None,
    fields: list[list[list[Fraction]]],
    daggers: list[list[list[Fraction]]],
    S: sp.Matrix | None,
    jw: list[list[list[Fraction]]],
    standard_generator: sp.Matrix,
    h: sp.Matrix,
) -> tuple[sp.Matrix, sp.Matrix]:
    jw_daggers = [bridge.mat_T(field) for field in jw]
    standard_hopping = bilinear(jw, jw_daggers, h)
    reconstructed_hopping = bilinear(fields, daggers, h)
    q_operator = sum(
        (
            sympy_matrix(bridge.mat_mul(jw_daggers[site], jw[site]))
            for site in range(N)
        ),
        sp.zeros(DIM),
    )
    q2 = sp.Matrix(standard_generator).extract(TWO_PARTICLE_BASIS, TWO_PARTICLE_BASIS)
    h2 = standard_hopping.extract(TWO_PARTICLE_BASIS, TWO_PARTICLE_BASIS)
    shift_ok = matrix_zero(q2 - h2 - 6 * sp.eye(6))
    intertwining_ok = S is not None and matrix_zero(
        S * reconstructed_hopping - standard_hopping * S
    )
    conserved = matrix_zero(standard_hopping * q_operator - q_operator * standard_hopping)
    mutation_ok = mutation != "chemical_shift_changes_Q2_dynamics"
    harness.check(
        "the boundary-coefficient logarithm reduces to the same local hopping law in the fixed Q=2 sector",
        shift_ok and intertwining_ok and conserved and mutation_ok,
        f"g2=h2+6I:{shift_ok} reconstructed={intertwining_ok} U1={conserved}",
    )
    return standard_hopping, reconstructed_hopping


def oriented_current(
    jw: list[list[list[Fraction]]],
    source: int,
    target: int,
    mutation: str | None,
) -> sp.Matrix:
    annihilator_source = sympy_matrix(jw[source])
    annihilator_target = sympy_matrix(jw[target])
    current = sp.I * (
        adjoint(annihilator_target) * annihilator_source
        - adjoint(annihilator_source) * annihilator_target
    )
    if set((source, target)) == {0, 1} and mutation == "reverse_current_01":
        current = -current
    if set((source, target)) == {0, 1} and mutation == "delete_current_01":
        current = sp.zeros(DIM)
    return sp.Matrix(current)


def current_certificate(
    harness: Harness,
    mutation: str | None,
    jw: list[list[list[Fraction]]],
    hopping: sp.Matrix,
) -> None:
    phase = sp.symbols("A", real=True)
    derivative_results = []
    for source, target in EDGES:
        annihilator_source = sympy_matrix(jw[source])
        annihilator_target = sympy_matrix(jw[target])
        phased = -(
            sp.exp(-sp.I * phase) * adjoint(annihilator_target) * annihilator_source
            + sp.exp(sp.I * phase) * adjoint(annihilator_source) * annihilator_target
        )
        derivative = sp.Matrix(phased).diff(phase).subs(phase, 0)
        derivative_results.append(
            matrix_zero(derivative - oriented_current(jw, source, target, mutation))
        )
    numbers = [adjoint(sympy_matrix(field)) * sympy_matrix(field) for field in jw]
    continuity_results = []
    for site in range(N):
        neighbors = tuple(
            right if left == site else left
            for left, right in EDGES
            if left == site or right == site
        )
        divergence = sum(
            (oriented_current(jw, site, neighbor, mutation) for neighbor in neighbors),
            sp.zeros(DIM),
        )
        continuity_results.append(
            matrix_zero(
                sp.I * (hopping * numbers[site] - numbers[site] * hopping)
                + divergence
            )
        )
    harness.check(
        "Peierls differentiation of that generator gives exact four-site continuity",
        all(derivative_results) and all(continuity_results),
        f"link_derivatives={sum(derivative_results)}/4 continuity={sum(continuity_results)}/4",
    )


def transfer_discriminator_certificate(
    harness: Harness,
    mutation: str | None,
    jw: list[list[list[Fraction]]],
    hard_core: list[list[list[Fraction]]],
    h: sp.Matrix,
) -> tuple[sp.Matrix, sp.Matrix, int, int]:
    jw_daggers = [bridge.mat_T(field) for field in jw]
    hard_daggers = [bridge.mat_T(field) for field in hard_core]
    car_two = bilinear(jw, jw_daggers, h).extract(TWO_PARTICLE_BASIS, TWO_PARTICLE_BASIS)
    hard_two = bilinear(hard_core, hard_daggers, h).extract(
        TWO_PARTICLE_BASIS, TWO_PARTICLE_BASIS
    )
    initial_position = TWO_PARTICLE_BASIS.index(10)
    target_index = 6 if mutation == "target_adjacent_occupancy" else 5
    target_position = TWO_PARTICLE_BASIS.index(target_index)
    car_polynomial = matrix_zero(car_two * (car_two**2 - 4 * sp.eye(6)))
    hard_polynomial = matrix_zero(hard_two * (hard_two**2 - 8 * sp.eye(6)))
    all_time_dark = (
        car_two[target_position, initial_position] == 0
        and (car_two**2)[target_position, initial_position] == 0
    )
    z_star = sp.pi / (2 * sp.sqrt(2))
    hard_evolution = (
        sp.eye(6)
        - sp.I * sp.sin(2 * sp.sqrt(2) * z_star) * hard_two / (2 * sp.sqrt(2))
        + (sp.cos(2 * sp.sqrt(2) * z_star) - 1) * hard_two**2 / 8
    )
    hard_amplitude = sp.simplify(hard_evolution[target_position, initial_position])
    deterministic_hard = hard_amplitude == -1
    harness.check(
        "the action-derived CAR law is all-time dark where the same supplied hard-core hopping is deterministic",
        car_polynomial and hard_polynomial and all_time_dark and deterministic_hard,
        f"CAR_dark={all_time_dark} HCB_amplitude={hard_amplitude} "
        f"polynomials=({car_polynomial},{hard_polynomial})",
    )
    return car_two, hard_two, initial_position, target_position


def record_certificate(
    harness: Harness,
    mutation: str | None,
    car_two: sp.Matrix,
    hard_two: sp.Matrix,
    initial_position: int,
    target_position: int,
) -> None:
    z_star = sp.pi / (2 * sp.sqrt(2))
    car_evolution = (
        sp.eye(6)
        - sp.I * sp.sin(2 * z_star) * car_two / 2
        + (sp.cos(2 * z_star) - 1) * car_two**2 / 4
    )
    hard_evolution = (
        sp.eye(6)
        - sp.I * sp.sin(2 * sp.sqrt(2) * z_star) * hard_two / (2 * sp.sqrt(2))
        + (sp.cos(2 * sp.sqrt(2) * z_star) - 1) * hard_two**2 / 8
    )
    initial = ket(initial_position, 6)
    car_state = sp.simplify(car_evolution * initial)
    hard_state = sp.simplify(hard_evolution * initial)
    target_car = ket(target_position, 6) * ket(target_position, 6).T
    target_hard = sp.Matrix(target_car)
    if mutation == "product_specific_writer":
        other_position = (target_position + 1) % 6
        target_hard = ket(other_position, 6) * ket(other_position, 6).T
    complement_car = sp.eye(6) - target_car
    complement_hard = sp.eye(6) - target_hard
    pointer_zero = ket(0, 2)
    pointer_one = ket(1, 2)
    writer_car = sp.kronecker_product(complement_car, pointer_zero) + sp.kronecker_product(
        target_car, pointer_one
    )
    writer_hard = sp.kronecker_product(complement_hard, pointer_zero) + sp.kronecker_product(
        target_hard, pointer_one
    )
    isometry_car = matrix_zero(writer_car.T.conjugate() * writer_car - sp.eye(6))
    isometry_hard = matrix_zero(writer_hard.T.conjugate() * writer_hard - sp.eye(6))
    output_car = sp.simplify(writer_car * car_state)
    output_hard = sp.simplify(writer_hard * hard_state)
    record_zero = sp.kronecker_product(sp.eye(6), pointer_zero * pointer_zero.T)
    record_one = sp.kronecker_product(sp.eye(6), pointer_one * pointer_one.T)
    weights_car = (
        sp.simplify((adjoint(output_car) * record_zero * output_car)[0]),
        sp.simplify((adjoint(output_car) * record_one * output_car)[0]),
    )
    weights_hard = (
        sp.simplify((adjoint(output_hard) * record_zero * output_hard)[0]),
        sp.simplify((adjoint(output_hard) * record_one * output_hard)[0]),
    )
    common = target_car == target_hard and writer_car == writer_hard
    full_target = sp.zeros(DIM)
    full_target[TWO_PARTICLE_BASIS[target_position], TWO_PARTICLE_BASIS[target_position]] = 1
    parity = sp.diag(*[(-1) ** len(subset_for_index(index)) for index in range(DIM)])
    even = matrix_zero(full_target * parity - parity * full_target)
    future_hamiltonian = sp.kronecker_product(car_two, sp.eye(2))
    if mutation == "overwrite_pointer":
        future_hamiltonian += sp.kronecker_product(sp.eye(6), sp.Matrix([[0, 1], [1, 0]]))
    permanence = all(
        matrix_zero(future_hamiltonian * record - record * future_hamiltonian)
        for record in (record_zero, record_one)
    )
    harness.check(
        "one common even CPTP writer turns the exact support difference into fixed pointer Records",
        common
        and isometry_car
        and isometry_hard
        and even
        and weights_car == (1, 0)
        and weights_hard == (0, 1)
        and permanence,
        f"common={common} isometry=({isometry_car},{isometry_hard}) even={even} "
        f"weights=({weights_car},{weights_hard}) permanent={permanence}",
    )


def scope_certificate(harness: Harness, mutation: str | None) -> None:
    assumptions = (ROOT / PACKET / "ASSUMPTIONS_AND_IMPORTS.md").read_text()
    goal = (ROOT / PACKET / "GOAL.md").read_text()
    target = (ROOT / PACKET / "EXACT_TARGET_CONTRACT.md").read_text()
    flat_goal = " ".join(goal.split())
    flat_target = " ".join(target.split())
    boundaries = (
        "I-4" in assumptions
        and "No arbitrary-branch" in assumptions
        and "does not claim" in flat_goal
        and "general staggered" in flat_target
        and "exact owner approval" in flat_target
    )
    claim_ok = mutation not in {"claim_I4_closed", "claim_Born_frequencies"}
    harness.check(
        "claim custody leaves physical-functional selection, time, and Record formation open",
        boundaries and claim_ok,
        f"boundaries={boundaries} I4_overclaim={mutation == 'claim_I4_closed'} "
        f"Born_overclaim={mutation == 'claim_Born_frequencies'}",
    )


def run(mutation: str | None) -> Harness:
    harness = Harness()

    def mutation_killed() -> bool:
        if mutation is None or harness.failed == 0:
            return False
        print(f"TOTAL: PASS={harness.passed} FAIL={harness.failed}")
        return True

    source_binding_certificate(harness, mutation)
    if mutation_killed():
        return harness
    h, recovered_g, B, K = source_kernel_certificate(harness, mutation)
    if mutation_killed():
        return harness
    gamma_K, _ = coherent_kernel_certificate(harness, mutation, B, K)
    if mutation_killed():
        return harness
    reconstruction = reconstruction_certificate(harness, mutation, K)
    if mutation_killed():
        return harness
    os_index_type_certificate(harness, mutation, reconstruction, gamma_K)
    if mutation_killed():
        return harness
    fields, daggers = reconstructed_car_certificate(
        harness, mutation, reconstruction, B, K
    )
    if mutation_killed():
        return harness
    S, jw, hard_core = dictionary_certificate(
        harness, mutation, reconstruction, fields, daggers
    )
    if mutation_killed():
        return harness
    standard_generator, _, _ = transfer_generator_certificate(
        harness,
        mutation,
        reconstruction,
        fields,
        daggers,
        S,
        jw,
        gamma_K,
        K,
        recovered_g,
    )
    if mutation_killed():
        return harness
    hopping, _ = fixed_charge_hopping_certificate(
        harness, mutation, fields, daggers, S, jw, standard_generator, h
    )
    if mutation_killed():
        return harness
    current_certificate(harness, mutation, jw, hopping)
    if mutation_killed():
        return harness
    car_two, hard_two, initial_position, target_position = transfer_discriminator_certificate(
        harness, mutation, jw, hard_core, h
    )
    if mutation_killed():
        return harness
    record_certificate(
        harness,
        mutation,
        car_two,
        hard_two,
        initial_position,
        target_position,
    )
    if mutation_killed():
        return harness
    scope_certificate(harness, mutation)
    print(f"TOTAL: PASS={harness.passed} FAIL={harness.failed}")
    return harness


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    arguments = parser.parse_args()
    result = run(arguments.mutation)
    return 1 if result.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
