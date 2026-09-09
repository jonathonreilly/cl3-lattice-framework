#!/usr/bin/env python3
"""Finite supplied-model definitions and historical receipt diagnostics.

Original production recipe and all earlier claims: .claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_quadratic_gauge_kernel_uniqueness_2026_09_04.py.
Current execution is bounded diagnostics only; no production/physical Maxwell
certificate is supplied. Imaginary-time projection is not a Record formation law.
"""

from __future__ import annotations

from pathlib import Path

from spin_half_cubic_ice_historical_receipt_integrity_2026_09_09 import (historical_text, load_receipt, validate_covariance, check_inputs, held_production, historical_target, shared_zero_covariance, gls_mean)

from dataclasses import dataclass
from itertools import permutations, product

import sympy as sp


AUDIT_INPUT_PATHS = (
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/NO_GO_DISCIPLINE_CHECKLIST_SPIN_HALF_INFRARED_FORWARD_REPLAY_2026-09-05.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_CUBIC_GAUGE_QUADRATIC_MAXWELL_KERNEL_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-09-04.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_CHARGE_COULOMB_FLUX_STIFFNESS_JOIN_BOUNDED_THEOREM_NOTE_2026-09-03.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_RELAXED_MAGNETIC_TWIST_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-04.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_TRANSVERSE_LINEAR_SPECTRAL_CROSSOVER_BOUNDED_THEOREM_NOTE_2026-09-03.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FORWARD_LENGTH_CONVERGENCE_BOUNDED_THEOREM_NOTE_2026-09-04.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_INFRARED_FORWARD_REPLAY_RECOVERY_BOUNDARY_NOTE_2026-09-05.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_INFRARED_MAXWELL_JOIN_HEALTH_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-04.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_LATE_TIME_HIGHER_GRADIENT_MAXWELL_JOIN_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-09-04.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_OFF_AXIS_MAXWELL_HIGH_MOMENTUM_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-09-04.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_convergence_join_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_finite_sample_reanalysis_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_high_stat_extension_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_high_stat_join_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_ladder_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_forward_replay_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_forward_replay_join_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_ladder_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_maxwell_failure_localization_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_maxwell_health_reanalysis_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_maxwell_join_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_cubic_orbit_scout_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_high_q_localization_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_maxwell_isotropy_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_maxwell_isotropy_join_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_staggered_orbit_scout_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_transverse_scout_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_quadratic_gauge_kernel_uniqueness_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_convergence_join_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_finite_sample_reanalysis_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_high_stat_extension_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_high_stat_join_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_ladder_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_forward_replay_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_forward_replay_join_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_ladder_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_maxwell_failure_localization_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_maxwell_health_reanalysis_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_maxwell_join_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_cubic_orbit_scout_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_high_q_localization_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_maxwell_isotropy_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_maxwell_isotropy_join_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_staggered_orbit_scout_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_transverse_scout_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_quadratic_gauge_kernel_uniqueness_2026_09_04.py',
    'data/field/spin_half_cubic_ice_successor_historical_receipts_2026_09_09.json',
    'docs/MINIMAL_AXIOMS_2026-06-29.md',
    'docs/SPIN_HALF_CUBIC_ICE_CUBIC_GAUGE_QUADRATIC_MAXWELL_KERNEL_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-09-04.md',
    'scripts/spin_half_cubic_ice_historical_receipt_integrity_2026_09_09.py',
)

AUDIT_TIMEOUT_SEC = 150


@dataclass(frozen=True)
class QuadraticKernelCertificate:
    rotation_count: int
    cubic_only_dimension: int
    transverse_only_dimension: int
    joint_dimension: int
    normalized_kernel: sp.Matrix


def quadratic_kernel_certificate() -> QuadraticKernelCertificate:
    """Solve the cubic-covariant transverse quadratic kernel exactly."""

    momenta = sp.symbols("q0:3")
    monomials = (
        momenta[0] ** 2,
        momenta[1] ** 2,
        momenta[2] ** 2,
        momenta[0] * momenta[1],
        momenta[0] * momenta[2],
        momenta[1] * momenta[2],
    )
    matrix_entries = tuple(
        (row, column)
        for row in range(3)
        for column in range(row, 3)
    )
    coefficients = sp.symbols("a0:36")
    kernel = sp.zeros(3)
    for entry_index, (row, column) in enumerate(matrix_entries):
        polynomial = sum(
            coefficients[6 * entry_index + monomial_index] * monomial
            for monomial_index, monomial in enumerate(monomials)
        )
        kernel[row, column] = polynomial
        kernel[column, row] = polynomial

    rotations = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rotation = sp.zeros(3)
            for row in range(3):
                rotation[row, permutation[row]] = signs[row]
            if rotation.det() == 1:
                rotations.append(rotation)

    cubic_equations = []
    momentum_column = sp.Matrix(momenta)
    for rotation in rotations:
        rotated_momenta = rotation * momentum_column
        transformed_arguments = kernel.xreplace(
            {
                momenta[index]: rotated_momenta[index]
                for index in range(3)
            }
        )
        transformed_indices = rotation * kernel * rotation.T
        for row in range(3):
            for column in range(row, 3):
                cubic_equations.extend(
                    sp.Poly(
                        sp.expand(
                            transformed_arguments[row, column]
                            - transformed_indices[row, column]
                        ),
                        momenta,
                    ).coeffs()
                )
    transverse_equations = []
    for component in kernel * momentum_column:
        transverse_equations.extend(
            sp.Poly(sp.expand(component), momenta).coeffs()
        )

    cubic_matrix, _ = sp.linear_eq_to_matrix(
        cubic_equations, coefficients
    )
    transverse_matrix, _ = sp.linear_eq_to_matrix(
        transverse_equations, coefficients
    )
    joint_matrix = cubic_matrix.col_join(transverse_matrix)
    nullspace = joint_matrix.nullspace()
    if len(nullspace) != 1:
        normalized_kernel = sp.zeros(3)
    else:
        substitutions = dict(zip(coefficients, nullspace[0], strict=True))
        solved_kernel = sp.simplify(kernel.subs(substitutions))
        normalization = sp.Poly(
            solved_kernel[0, 0], momenta
        ).coeff_monomial(momenta[1] ** 2)
        normalized_kernel = sp.simplify(solved_kernel / normalization)
    return QuadraticKernelCertificate(
        rotation_count=len(rotations),
        cubic_only_dimension=len(coefficients) - cubic_matrix.rank(),
        transverse_only_dimension=(
            len(coefficients) - transverse_matrix.rank()
        ),
        joint_dimension=len(coefficients) - joint_matrix.rank(),
        normalized_kernel=normalized_kernel,
    )


def main() -> int:
    check_inputs(Path(__file__).resolve().parent.parent, AUDIT_EXPECTED_SHA256)
    certificate = quadratic_kernel_certificate()
    q0, q1, q2 = sp.symbols("q0:3")
    maxwell = sp.Matrix(
        (
            (q1**2 + q2**2, -q0 * q1, -q0 * q2),
            (-q0 * q1, q0**2 + q2**2, -q1 * q2),
            (-q0 * q2, -q1 * q2, q0**2 + q1**2),
        )
    )
    conditions = (
        certificate.rotation_count == 24,
        certificate.cubic_only_dimension == 3,
        certificate.transverse_only_dimension == 6,
        certificate.joint_dimension == 1,
        certificate.normalized_kernel == maxwell,
    )
    labels = (
        "the proper cubic group contains exactly twenty-four rotations",
        "cubic covariance alone leaves three symmetric quadratic kernels",
        "gauge transversality alone leaves six symmetric quadratic kernels",
        "their exact intersection is one-dimensional",
        "the surviving normalized kernel is q-squared delta minus q-i q-j",
    )
    passed = 0
    failed = 0
    for condition, label in zip(conditions, labels, strict=True):
        if condition:
            passed += 1
            print(f"[PASS] {passed + failed:02d} {label}")
        else:
            failed += 1
            print(f"[FAIL] {passed + failed:02d} {label}")
    print(
        "KERNEL_DIMENSIONS",
        f"cubic_only={certificate.cubic_only_dimension}",
        f"transverse_only={certificate.transverse_only_dimension}",
        f"joint={certificate.joint_dimension}",
    )
    print(
        "CERTIFICATE: polynomial_order=q2 symmetric_kernel=True "
        "proper_cubic_covariance=True gauge_transversality=True "
        "analyticity_assumed=True higher_orders_unconstrained=True"
    )
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1




# Current source/input identity: literal finite closure.
AUDIT_EXPECTED_SHA256 = {
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/NO_GO_DISCIPLINE_CHECKLIST_SPIN_HALF_INFRARED_FORWARD_REPLAY_2026-09-05.md': 'd005e28ff0cba15f5e5b27580055c2ae51958dfeb967c3603df0d01d8bd4526b',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_CUBIC_GAUGE_QUADRATIC_MAXWELL_KERNEL_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-09-04.md': 'd9c836c854ee20dddf399d51d7bab6b13f9164a920a10ed2c0713cd6b4f150e4',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_CHARGE_COULOMB_FLUX_STIFFNESS_JOIN_BOUNDED_THEOREM_NOTE_2026-09-03.md': '1f6811e0f9a872c2a23946dbf313a32c378ca697f658423e0c13dcad708e0ff9',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_RELAXED_MAGNETIC_TWIST_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-04.md': '73d66f716fdfacc5c6d02f902b2021392e5139041b6018985d2886264a5007ed',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_TRANSVERSE_LINEAR_SPECTRAL_CROSSOVER_BOUNDED_THEOREM_NOTE_2026-09-03.md': '862311719f14a9ba1ee6fc660477fd01510631a87db636f9098a626d5291316d',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FORWARD_LENGTH_CONVERGENCE_BOUNDED_THEOREM_NOTE_2026-09-04.md': '9b2aba542ed2f36643ce4b511b1f85db9b96a0a5b3570e5f306e561b6b8b246e',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_INFRARED_FORWARD_REPLAY_RECOVERY_BOUNDARY_NOTE_2026-09-05.md': '1d22ab5c1f16784462b68ddf4021b7e14a110a6ca7be6cff92ffd279f9011715',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_INFRARED_MAXWELL_JOIN_HEALTH_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-04.md': '139bd99c4f1f9c86bf8f222cb6986957d8f24bfca335a5f3c0ea1654a5a4abbd',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_LATE_TIME_HIGHER_GRADIENT_MAXWELL_JOIN_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-09-04.md': '8a3369b50204369ddfd0311704cf71423a91c5c87df51a6e41dae4657b0ab947',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_OFF_AXIS_MAXWELL_HIGH_MOMENTUM_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-09-04.md': 'c47db40a423d54580b0e27ba844e302c0e9d5cb1105705fb1b5392f21ac00e36',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.txt': '992136071fbd1f87efbae5daec0689ce7309913ccc12fd294bdfc39a54ae569f',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.txt': '2e483ff3d5bc34e7fdde41b8ab06790be1ea487a167bb10b33936e35ff22c894',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.txt': '97687c182b2c0a8f095bea6ddc90018e2580163af81757e1bbeaf2650c04fde7',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_convergence_join_2026_09_04.txt': '366e0cfbca4cc582cc28c34c2e822990b5a1216d42513417677e818584cd4fea',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_finite_sample_reanalysis_2026_09_04.txt': 'db3f966552fb31bab95a3d487220dd0622b21b5da127515f197e7e441ad68445',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_high_stat_extension_2026_09_04.txt': '484c30b66ccbe992290da328e785c22f597dfc698173044c4cec178d3fbaf8b6',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_high_stat_join_2026_09_04.txt': '8ec096ed4b50bf92ee7d709470833d9355b8461c9e9c35e5579d1fec4402ed17',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_ladder_2026_09_04.txt': 'd6ffe038be4e0a5dc6824965dbdcc24595aac7ba2241ef0ca059310ffeabd59e',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_forward_replay_2026_09_04.txt': '849646d782df0c360fd1d180b4d966b3499979b43d1c709b11b5c1e43c2a92e0',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_forward_replay_join_2026_09_04.txt': '5131098b985eab3d4991a5c767c1f057ba047ff694b5d074383037a27f65622c',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_ladder_2026_09_04.txt': '09f1e590b9cf2cade315bca1a854156a42faba262d22b55f21167bad7a6b798c',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_maxwell_failure_localization_2026_09_04.txt': '88552107e8ce428aec277c61645322a927b209b3a3936ec4471e3344b4d50a35',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_maxwell_health_reanalysis_2026_09_04.txt': 'e6e00baa0a8bcb38afdd7cf1e46e09e0c8f5b6ba4422bc2fdcb45fac72a6a92c',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_maxwell_join_2026_09_04.txt': '2c2dec102b9758f4249818ed2ce935a0c582a5a3c3fead19d91b12aadb8b51af',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.txt': '17345ac4bd2839c8d0cd315fdc0d5c6126e3b8879f1b3f49bd055c637d0ec481',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_cubic_orbit_scout_2026_09_04.txt': 'acdfb65d3e785f08ba61b6958461db6154fcd2771e1d309834d00ece3ca48992',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_high_q_localization_2026_09_04.txt': '82e2ad2b36cc44b9a367a16554a52dc5a68c94690a571d642f37e9ececcb5216',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_maxwell_isotropy_2026_09_04.txt': '6ec74acaacd3909cd39b0520c0bc93e690ca949c54119a60e84a89d55a7ea1d0',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_maxwell_isotropy_join_2026_09_04.txt': '7d7cfba76fe8a0de63de2ecd2b2a6241d7401e3904258a45969d30ae76b3f728',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_staggered_orbit_scout_2026_09_04.txt': 'c77aab04384741c1bca11852b0554742db0b8c157545bded3c1b09735b3b42dc',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_transverse_scout_2026_09_04.txt': '5eda05ddbf46d54e600839ecd30f552d3362e3704071037e38c0632dc2f86e81',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_quadratic_gauge_kernel_uniqueness_2026_09_04.txt': 'f28a3a727508e6c2df4a4f1e77d0d0bcfdb77a5d41a282f13219d9ef4a4aa202',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.py': '97881c8721ee3177aeaa610a59f139ef44be809b49bc9c6ed9f0490fe6b10418',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.py': 'a61b5ca89ea5b39ac932744b12e3af46167d81fd4ed5eb52acdb08644f74b28b',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.py': '5bb190ef328d095d83eacf927e2c3964499f178e6f41254368047957a893227d',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_convergence_join_2026_09_04.py': 'aaa07511fdd1650fe317bd8fe03e4826beaa7f7cf5659c475b7b53e4a6b30733',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_finite_sample_reanalysis_2026_09_04.py': '421cd0399b35947d90f208ddab78b38b2caf7e7cd5f593613ff53af300aaf434',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_high_stat_extension_2026_09_04.py': '75461521b7bd0d3806e3a0598c4c82603f7127623762990d478784ad2ef542b1',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_high_stat_join_2026_09_04.py': '1aa54dbb1b298ee8064603b89e97470d541900d7affb61bf329f269908a2ceca',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_ladder_2026_09_04.py': '7ac21e04324b48c9215524d1e889693ee329a5fe0e3495d1a8c14832249bd953',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_forward_replay_2026_09_04.py': '8d87b4c4ffc219e7557cf0ad19213842738f8f8a2879493612e3740fd19d26da',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_forward_replay_join_2026_09_04.py': 'b0556cf80af1a4515ca1a134c435dd40c011f0dfb058acd743c2948522e12af8',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_ladder_2026_09_04.py': '80108851a3d3a77e8e2593502abfa17ee72eab7174ad7043f039afe2e5133867',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_maxwell_failure_localization_2026_09_04.py': '756173baab1c9966bf8c2cdd03860f7736710e17edb7b453fe9e69bf2e328dfb',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_maxwell_health_reanalysis_2026_09_04.py': '9b4fbd65bc089f160e90fef8d2e95b3eaaedb276fd582c9b4697ed393abd0eae',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_maxwell_join_2026_09_04.py': 'fdb9e0d0de5d10282c782cd888a9e3823c76a9c2a253887e76ae8a686de8da1f',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.py': '8cea10e54e91b643a39d2a757eb120ee992197defdf45dce4cac98e36d5197cd',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_cubic_orbit_scout_2026_09_04.py': 'e93ddc34b6bdbca4e17a89aa1d1f2ebef140c8717138d9aa429c8911751dc189',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_high_q_localization_2026_09_04.py': '8be752a7b03f7db990958e4813c7e029e85e06736a7cc6644db712452ceddf96',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_maxwell_isotropy_2026_09_04.py': '6057a37e1415b3dce55c85923514ec481f6cb007921d2ed634c8237be18b7655',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_maxwell_isotropy_join_2026_09_04.py': 'fef6248c3b90c88c1038af037cd152b8e3d33577dcc31286328bdffe6cdfa0ec',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_staggered_orbit_scout_2026_09_04.py': 'ae6390773d562d8ffe37bae981cc64246e0cbebb817eff88b6383ca376e7eeac',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_transverse_scout_2026_09_04.py': '477ca4a1af788464bb798ffa0bc5c2f42fd3c3c3591d22fd075b80e24cb82a4e',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_quadratic_gauge_kernel_uniqueness_2026_09_04.py': 'f621e2b2d00bf85525dae4a1a3f103dd156cb9ba837c5f8f4d5199282ae5c2cb',
    'data/field/spin_half_cubic_ice_successor_historical_receipts_2026_09_09.json': 'c1c7a1cdd92236409d829be9a8dad7700b169e6e8bc3f5d94e28fa34c25653a7',
    'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
    'docs/SPIN_HALF_CUBIC_ICE_CUBIC_GAUGE_QUADRATIC_MAXWELL_KERNEL_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-09-04.md': '5fe56a48c6b93e07662b963cef7f0a7773ef53b8f079ece3db9366eaf5e78384',
    'scripts/spin_half_cubic_ice_historical_receipt_integrity_2026_09_09.py': 'a5514a656d9d3b82c0b76c46e5aff2b9e731eb6b634de2bc99b25b9af458f54f',
}

if __name__ == "__main__":
    raise SystemExit(main())
