#!/usr/bin/env python3
"""Checks timelike edge-current networks and the compact homothety boundary.

The paired note constructs two positive future-temporal edge networks on the
supplied four-dimensional Kuhn/Coxeter carrier.  It also gives a separating
null covector at compact zero momentum: the constant-metric homothety has
strictly positive components, so no nonzero componentwise-nonnegative length
source can lie in the image of the unmodified flat Regge Hessian at k=0.
"""

from __future__ import annotations

from itertools import product
from math import pi, sqrt
from pathlib import Path
import sys

import numpy as np
import sympy as sp


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_TIMELIKE_EDGE_CURRENT_NETWORK_COMPACT_HOMOTHETY_"
    "REGGE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
HELIX_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_"
    "REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
TWO_STREAM_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_POSITIVE_TWO_STREAM_TIMELIKE_MEAN_DILATION_ZERO_MODE_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
HISTORY_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CUT_WORLDVOLUME_AFFINE_BAG_REGGE_MONOPOLE_BOUNDARY_"
    "BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
REGGE_NOTE_PATH = ROOT / "docs" / (
    "CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_"
    "NARROW_THEOREM_NOTE_2026-06-09.md"
)
KINETIC_PATH = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED_PATH = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_TIMELIKE_EDGE_CURRENT_NETWORK_COMPACT_HOMOTHETY_REGGE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_POSITIVE_TWO_STREAM_TIMELIKE_MEAN_DILATION_ZERO_MODE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_CUT_WORLDVOLUME_AFFINE_BAG_REGGE_MONOPOLE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "scripts/admissibility_closed_helical_defect_history_ward_neutral_ir_regge_response_boundary_2026_08_10.py",
    "scripts/admissibility_centered_tick_edge_defect_improvement_exact_static_regge_source_boundary_2026_08_10.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)

sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_closed_helical_defect_history_ward_neutral_ir_regge_response_boundary_2026_08_10 as helix  # noqa: E402
import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as regge  # noqa: E402


TICK = np.asarray((0, 0, 0, 1), dtype=int)
FACE = np.asarray((1, 0, 0, 1), dtype=int)
SPACE_X = np.asarray((1, 0, 0, 0), dtype=int)
COARSE = TICK + FACE
TEMPORAL_INDICES = tuple(
    index for index, direction in enumerate(regge.DIRS15) if direction[3] == 1
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition: bool, detail: str = "") -> None:
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}")
        if not ok:
            print(f"       {statement}")
        if detail:
            print(f"       {detail}")
        self.passed += int(ok)
        self.failed += int(not ok)


def centered_indices(length: int) -> range:
    return range(-(length // 2), (length + 1) // 2)


def temporal_bundle_rows() -> tuple[np.ndarray, np.ndarray]:
    """Return two nonnegative spatial-permutation-symmetric weight bundles."""
    bundle_a = np.zeros(15, dtype=float)
    bundle_b = np.zeros(15, dtype=float)
    for index in TEMPORAL_INDICES:
        direction = regge.DIRS15[index]
        spatial_weight = sum(direction[:3])
        if spatial_weight == 1:
            bundle_a[index] = 2.0 * sqrt(2.0)
        elif spatial_weight == 0:
            bundle_b[index] = 3.0
        elif spatial_weight == 2:
            bundle_b[index] = sqrt(3.0)
    return bundle_a, bundle_b


def tangent_current(weights: np.ndarray) -> np.ndarray:
    current = np.zeros(4, dtype=float)
    for index, weight in enumerate(weights):
        if weight == 0.0:
            continue
        direction = np.asarray(regge.DIRS15[index], dtype=float)
        current += weight * direction / np.linalg.norm(direction)
    return current


def equal_weight_relation_matrix() -> sp.Matrix:
    """Expand future-temporal unit tangents over Q-basis 1,sqrt(2),sqrt(3)."""
    matrix = sp.zeros(12, len(TEMPORAL_INDICES))
    for column, index in enumerate(TEMPORAL_INDICES):
        direction = regge.DIRS15[index]
        spatial_weight = sum(direction[:3])
        if spatial_weight == 0:
            basis_index, factor = 0, sp.Integer(1)
        elif spatial_weight == 1:
            basis_index, factor = 1, sp.Rational(1, 2)
        elif spatial_weight == 2:
            basis_index, factor = 2, sp.Rational(1, 3)
        else:
            basis_index, factor = 0, sp.Rational(1, 2)
        for coordinate, component in enumerate(direction):
            if component:
                matrix[3 * coordinate + basis_index, column] = factor
    return matrix


def bouquet_row(length: int, momentum: np.ndarray) -> np.ndarray:
    return helix.closed_line_row(length, momentum, TICK) + helix.closed_line_row(
        length, momentum, FACE
    )


def homothety_vector() -> np.ndarray:
    identity_metric = np.asarray((1, 1, 1, 1, 0, 0, 0, 0, 0, 0), dtype=float)
    return regge.metric_map(np.zeros(4)) @ identity_metric


def response_coefficient(source: np.ndarray, momentum: np.ndarray) -> tuple[float, float]:
    hessian = regge.bloch_Q(momentum)
    solution = -np.linalg.pinv(hessian, rcond=1.0e-10) @ source.conj()
    residual = float(np.linalg.norm(hessian @ solution + source.conj()))
    coefficient = float(
        (np.dot(momentum, momentum) * (source @ solution)).real
    )
    return coefficient, residual


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    helix_note = HELIX_NOTE_PATH.read_text(encoding="utf-8")
    two_stream_note = TWO_STREAM_NOTE_PATH.read_text(encoding="utf-8")
    history_note = HISTORY_NOTE_PATH.read_text(encoding="utf-8")
    regge_note = REGGE_NOTE_PATH.read_text(encoding="utf-8")
    kinetic = KINETIC_PATH.read_text(encoding="utf-8")
    realized = REALIZED_PATH.read_text(encoding="utf-8")
    note_flat = " ".join(note.split())
    axiom_flat = " ".join(axiom.split())
    helix_flat = " ".join(helix_note.split())
    two_stream_flat = " ".join(two_stream_note.split())
    history_flat = " ".join(history_note.split())
    regge_flat = " ".join(regge_note.split())
    kinetic_flat = " ".join(kinetic.split())
    realized_flat = " ".join(realized.split())

    print("external_scientific_inputs: none; all current, bundle, Fourier, and homothety identities are derived on the supplied edge carrier")
    print("package_local_integrity_reads: current axioms, Block-14 closed lines, Block-15 positive two-stream boundary, equal-form tick graining, and the actual Regge Hessian are source-bound")
    print("analytic_boundary: positive balanced currents and the compact homothety separator are exact; full-null inventories are finite and named")
    print("physical_boundary: aggregate current is not a selected rank-one massive trajectory, and the weighted bundle includes spacelike primitive edges")

    checks.check(
        "source-current-axioms",
        "the current axioms do not silently select the network action, history routing, compact ensemble, or geometry dynamics",
        "Admissibility is not a dynamics axiom" in axiom_flat
        and "source/action and physical-observable identification" in axiom_flat
        and "update laws" in axiom_flat,
    )
    checks.check(
        "source-prior-frontier",
        "Blocks 14--15 leave connected routing, balanced bundle histories, physical compact mechanism, and combined geometry live",
        "positive-energy or positive-mass compact ensemble" in helix_flat
        and "subluminal timelike history" in helix_flat
        and "balanced multi-edge junctions" in helix_flat
        and "geometry action selection, orientation, coupling sign, and coupling size" in helix_flat
        and "two lines are disjoint" in two_stream_flat
        and "fixed-global, open, sign-indefinite combined-geometry" in two_stream_flat,
    )
    checks.check(
        "source-existing-history-amendment",
        "the existing candidate types a fixed history action, combined Ward identity, and declared compact ensemble without selecting them",
        "fixed unnormalized local" in history_flat
        and "Conservation is the Ward identity" in history_flat
        and "background-subtracted, or globally constrained zero-mode" in history_flat
        and "This is sufficient wording, not adopted wording" in history_flat,
    )
    checks.check(
        "source-regge-boundary",
        "the supplied carrier has fifteen edge classes, ten constant-metric zero modes, and one extra decoupled branch at k=0",
        "**15** edge classes" in regge_flat
        and "Constant metric perturbations are exact zero modes at `k=0`" in regge_flat
        and "one exactly flat branch" in regge_flat,
    )
    checks.check(
        "source-tick-primitive",
        "equal-form tick graining supplies no causal selector, action weights, source sign, or compact constraint",
        "It carries no dimensionless dynamical content" in kinetic_flat
        and "not a new dynamics" in kinetic_flat,
    )
    checks.check(
        "source-realized-state-boundary",
        "the realized-state primitive supplies pointwise evaluation but no history, state selector, boundary condition, or weighting",
        "pointwise evaluation, not a state-selection rule" in realized_flat
        and "does not supply a state" in realized_flat
        and "boundary condition" in realized_flat,
    )

    temporal_directions = tuple(regge.DIRS15[index] for index in TEMPORAL_INDICES)
    checks.check(
        "future-temporal-edge-inventory",
        "the current carrier has exactly eight future-temporal 0/1 edge classes in four spatial-Hamming classes",
        len(temporal_directions) == 8
        and tuple(sum(direction[:3]) for direction in temporal_directions).count(0) == 1
        and tuple(sum(direction[:3]) for direction in temporal_directions).count(1) == 3
        and tuple(sum(direction[:3]) for direction in temporal_directions).count(2) == 3
        and tuple(sum(direction[:3]) for direction in temporal_directions).count(3) == 1,
    )
    relation_matrix = equal_weight_relation_matrix()
    checks.check(
        "equal-weight-junction-rigidity",
        "the eight normalized temporal directions have no nonzero rational relation, so an equal-coefficient integer junction preserves every edge-class count",
        relation_matrix.rank() == 8 and relation_matrix.nullspace() == [],
        f"number-field coefficient rank={relation_matrix.rank()}",
    )

    bundle_a, bundle_b = temporal_bundle_rows()
    contrast = bundle_a - bundle_b
    current_a = tangent_current(bundle_a)
    current_b = tangent_current(bundle_b)
    target_current = np.asarray((2.0, 2.0, 2.0, 6.0))
    checks.check(
        "positive-permutation-symmetric-bundles",
        "both bundle rows are nonnegative and constant on each spatial-Hamming orbit of the positive-coordinate temporal inventory",
        np.min(bundle_a) >= 0.0
        and np.min(bundle_b) >= 0.0
        and np.count_nonzero(bundle_a) == 3
        and np.count_nonzero(bundle_b) == 4,
    )
    checks.check(
        "exact-bundle-current-identity",
        "the three weighted face diagonals and the tick-plus-three-plane bundle carry the same Euclidean tangent current (2,2,2,6)",
        np.max(np.abs(current_a - target_current)) < 2.0e-15
        and np.max(np.abs(current_b - target_current)) < 2.0e-15,
    )
    current_speed = float(np.linalg.norm(target_current[:3]) / target_current[3])
    current_lorentz_norm = float(
        target_current[3] ** 2 - np.dot(target_current[:3], target_current[:3])
    )
    checks.check(
        "strictly-timelike-aggregate-current",
        "the common bundle current has naive Lorentzian speed 1/sqrt(3) and squared norm 24",
        abs(current_speed - 1.0 / sqrt(3.0)) < 2.0e-15
        and abs(current_lorentz_norm - 24.0) < 2.0e-14,
    )

    max_vertex_force = 0.0
    history_count = 0
    nonconstant_histories = 0
    supported_history_modes = 0
    per_length_history: list[tuple[int, int, int, int]] = []
    worst_history_gauge = 0.0
    worst_history_null = 0.0
    worst_history_solve = 0.0
    wrong_history_zero_counts = 0
    min_k0_solve = float("inf")
    max_k0_solve = 0.0
    worst_k0_scale_error = 0.0
    zero_momentum = np.zeros(4)
    zero_hessian = regge.bloch_Q(zero_momentum)
    zero_pinv = np.linalg.pinv(zero_hessian, rcond=1.0e-10)
    scale_vector = homothety_vector()
    for length in range(3, 9):
        local_supported = 0
        local_nonconstant = 0
        mode_data: dict[int, dict[str, float | int]] = {}
        for mode in range(1, length):
            momentum = np.asarray((0.0, 0.0, 0.0, 2.0 * pi * mode / length))
            mode_data[mode] = helix.source_data(contrast, momentum)
        for bits in product((0, 1), repeat=length):
            history_count += 1
            selected = np.asarray(bits, dtype=float)
            if 0 < sum(bits) < length:
                nonconstant_histories += 1
                local_nonconstant += 1
            for tick in range(length):
                outgoing = current_a if bits[tick] else current_b
                incoming = current_a if bits[(tick - 1) % length] else current_b
                max_vertex_force = max(
                    max_vertex_force, float(np.linalg.norm(outgoing - incoming))
                )
            mean_source = (
                sum(bits) * bundle_a + (length - sum(bits)) * bundle_b
            ) / length
            zero_solution = -zero_pinv @ mean_source
            zero_residual = float(
                np.linalg.norm(zero_hessian @ zero_solution + mean_source)
            )
            min_k0_solve = min(min_k0_solve, zero_residual)
            max_k0_solve = max(max_k0_solve, zero_residual)
            worst_k0_scale_error = max(
                worst_k0_scale_error,
                abs(float(np.vdot(scale_vector, mean_source).real) - 6.0),
            )
            for mode in range(1, length):
                amplitude = sum(
                    selected[tick]
                    * np.exp(2j * pi * mode * tick / length)
                    for tick in range(length)
                )
                if abs(amplitude) < 1.0e-10:
                    continue
                supported_history_modes += 1
                local_supported += 1
                data = mode_data[mode]
                wrong_history_zero_counts += int(data["zero_count"] != 5)
                worst_history_gauge = max(worst_history_gauge, float(data["gauge"]))
                worst_history_null = max(worst_history_null, float(data["null"]))
                worst_history_solve = max(worst_history_solve, float(data["solve"]))
        per_length_history.append(
            (length, 2**length, local_nonconstant, local_supported)
        )
    checks.check(
        "binary-history-local-balance",
        "all 504 binary bundle histories on L=3 through L=8 have exact sitewise incoming-outgoing current balance",
        history_count == 504
        and nonconstant_histories == 492
        and max_vertex_force < 3.0e-15,
    )
    checks.check(
        "binary-history-mode-inventory",
        "the 504 histories have 2,768 supported nonzero history-mode pairs with the declared per-L census",
        supported_history_modes == 2768
        and per_length_history
        == [
            (3, 8, 6, 12),
            (4, 16, 14, 34),
            (5, 32, 30, 120),
            (6, 64, 62, 260),
            (7, 128, 126, 756),
            (8, 256, 254, 1586),
        ],
        f"per-L={per_length_history}",
    )
    checks.check(
        "binary-history-full-null-compatibility",
        "every supported nonzero binary-history mode meets five Regge zeros and annihilates the complete null space",
        wrong_history_zero_counts == 0
        and worst_history_gauge < 2.0e-13
        and worst_history_null < 3.0e-12,
        f"gauge={worst_history_gauge:.3e}; full-null={worst_history_null:.3e}",
    )
    checks.check(
        "binary-history-unprojected-solvability",
        "every supported nonzero binary-history edge equation solves directly without source projection",
        worst_history_solve < 5.0e-10,
        f"max normalized solve residual={worst_history_solve:.3e}",
    )
    checks.check(
        "binary-history-positive-mean-control",
        "every binary history has positive sequence-independent homothety charge six per tick and a nonzero k=0 solve residual",
        worst_k0_scale_error < 3.0e-14
        and min_k0_solve > 3.20
        and max_k0_solve < 3.47,
        f"normalized k0 solve range=[{min_k0_solve:.6f},{max_k0_solve:.6f}]",
    )

    sample_frequency = 0.61
    sample_momentum = np.asarray((0.0, 0.0, 0.0, sample_frequency))
    contrast_metric = contrast @ regge.metric_map(sample_momentum)
    phase_sinc = np.exp(0.5j * sample_frequency) * np.sinc(
        sample_frequency / (2.0 * pi)
    )
    expected_contrast_metric = np.zeros(10, dtype=complex)
    for component in (4, 5, 7):
        expected_contrast_metric[component] = -phase_sinc
    checks.check(
        "binary-contrast-pure-shear-map",
        "the bundle contrast maps exactly to equal xy, xz, and yz spatial shear with no lapse, shift, or diagonal source",
        np.max(np.abs(contrast_metric - expected_contrast_metric)) < 4.0e-15,
    )

    pole_coefficients = []
    pole_errors = []
    pole_residuals = []
    for frequency in (0.2, 0.1, 0.05, 0.025):
        coefficient, residual = response_coefficient(
            contrast, np.asarray((0.0, 0.0, 0.0, frequency))
        )
        pole_coefficients.append(coefficient)
        pole_errors.append(abs(coefficient - 6.0))
        pole_residuals.append(residual)
    checks.check(
        "binary-shear-unprojected-pole",
        "the actual edge response to the bundle contrast has omega-squared source-contracted response tending to six",
        pole_errors[-1] < 4.0e-4 and max(pole_residuals) < 1.0e-9,
        "coefficients=" + ",".join(f"{value:.7f}" for value in pole_coefficients),
    )
    checks.check(
        "binary-shear-pole-convergence",
        "each halving of the pure-tick momentum reduces the tensor-pole coefficient error",
        all(pole_errors[index + 1] < pole_errors[index] for index in range(3)),
    )

    bouquet_total_modes = 0
    bouquet_sourced_modes = 0
    bouquet_dynamic_modes = 0
    bouquet_overlap_modes = 0
    bouquet_wrong_zero_counts = 0
    bouquet_worst_gauge = 0.0
    bouquet_worst_null = 0.0
    bouquet_worst_solve = 0.0
    bouquet_per_length: list[tuple[int, int, int, int]] = []
    bouquet_connected = True
    for length in range(3, 9):
        tick_vertices = {
            tuple((step * TICK) % length) for step in range(length)
        }
        face_vertices = {
            tuple((step * FACE) % length) for step in range(length)
        }
        bouquet_connected &= tick_vertices.intersection(face_vertices) == {(0, 0, 0, 0)}
        local_sourced = 0
        local_dynamic = 0
        local_overlap = 0
        for index in product(centered_indices(length), repeat=4):
            bouquet_total_modes += 1
            if not any(index):
                continue
            momentum = 2.0 * pi * np.asarray(index, dtype=float) / length
            tick_active = abs(helix.structure_factor(length, momentum, TICK)) > 2.0e-12
            face_active = abs(helix.structure_factor(length, momentum, FACE)) > 2.0e-12
            if not (tick_active or face_active):
                continue
            source = bouquet_row(length, momentum)
            bouquet_sourced_modes += 1
            local_sourced += 1
            bouquet_dynamic_modes += int(index[3] != 0)
            local_dynamic += int(index[3] != 0)
            bouquet_overlap_modes += int(tick_active and face_active)
            local_overlap += int(tick_active and face_active)
            data = helix.source_data(source, momentum)
            bouquet_wrong_zero_counts += int(data["zero_count"] != 5)
            bouquet_worst_gauge = max(bouquet_worst_gauge, float(data["gauge"]))
            bouquet_worst_null = max(bouquet_worst_null, float(data["null"]))
            bouquet_worst_solve = max(bouquet_worst_solve, float(data["solve"]))
        bouquet_per_length.append(
            (length, local_sourced, local_dynamic, local_overlap)
        )
    checks.check(
        "positive-bouquet-connected-support",
        "the positive tick and face-diagonal loops share exactly one vertex and form a connected two-loop bouquet on every declared torus",
        bouquet_connected,
    )
    unit_current = TICK.astype(float) + FACE.astype(float) / sqrt(2.0)
    coarse_speed = float(np.linalg.norm(COARSE[:3]) / COARSE[3])
    tension_speed = float(np.linalg.norm(unit_current[:3]) / unit_current[3])
    checks.check(
        "positive-bouquet-timelike-routing",
        "label exchange at the balanced bouquet vertex has coarse speed one-half, while the aggregate unit-tangent current has speed sqrt(2)-one",
        abs(coarse_speed - 0.5) < 1.0e-15
        and abs(tension_speed - (sqrt(2.0) - 1.0)) < 2.0e-15
        and COARSE[3] ** 2 - np.dot(COARSE[:3], COARSE[:3]) == 3,
    )
    checks.check(
        "positive-bouquet-mode-inventory",
        "the bouquet has 2,369 nonzero sources, including 1,088 dynamic and 193 two-line-overlap modes, among all 8,755 modes",
        bouquet_total_modes == 8755
        and bouquet_sourced_modes == 2369
        and bouquet_dynamic_modes == 1088
        and bouquet_overlap_modes == 193
        and bouquet_per_length
        == [
            (3, 44, 18, 8),
            (4, 111, 48, 15),
            (5, 224, 100, 24),
            (6, 395, 180, 35),
            (7, 636, 294, 48),
            (8, 959, 448, 63),
        ],
        f"per-L={bouquet_per_length}",
    )
    checks.check(
        "positive-bouquet-full-null-compatibility",
        "every one of the 2,369 positive-bouquet nonzero sources annihilates all five Regge null directions",
        bouquet_wrong_zero_counts == 0
        and bouquet_worst_gauge < 2.0e-13
        and bouquet_worst_null < 3.0e-13,
        f"gauge={bouquet_worst_gauge:.3e}; full-null={bouquet_worst_null:.3e}",
    )
    checks.check(
        "positive-bouquet-unprojected-solvability",
        "the actual edge equation solves directly for all 2,369 nonzero bouquet sources",
        bouquet_worst_solve < 5.0e-12,
        f"max direct solve residual={bouquet_worst_solve:.3e}",
    )

    bouquet_zero = bouquet_row(5, zero_momentum)
    bouquet_zero_data = helix.source_data(bouquet_zero, zero_momentum)
    checks.check(
        "positive-bouquet-zero-mode-control",
        "the connected positive bouquet retains the compact k=0 incompatibility despite exact nonzero-mode closure",
        abs(float(np.vdot(scale_vector, bouquet_zero).real) - 5.0 * (1.0 + sqrt(2.0))) < 2.0e-14
        and bouquet_zero_data["null"] > 13.5
        and bouquet_zero_data["solve"] > 13.5,
        f"homothety={np.vdot(scale_vector, bouquet_zero).real:.6f}; solve={bouquet_zero_data['solve']:.6f}",
    )

    expected_scale_vector = np.asarray(
        [sqrt(sum(direction)) / 2.0 for direction in regge.DIRS15], dtype=float
    )
    scale_residual = float(np.linalg.norm(zero_hessian @ scale_vector))
    checks.check(
        "compact-homothety-null-vector",
        "the identity-metric homothety is the strictly positive edge vector |d|/2 and is null under Q_R(0)",
        np.max(np.abs(scale_vector.real - expected_scale_vector)) < 2.0e-15
        and np.max(np.abs(scale_vector.imag)) < 2.0e-15
        and np.min(scale_vector.real) == 0.5
        and scale_residual < 2.0e-13,
        f"norm={np.linalg.norm(scale_vector):.7f}; Q0 residual={scale_residual:.3e}",
    )
    extreme_overlaps = [
        float(np.vdot(scale_vector, helix.edge_row(np.asarray(direction))).real)
        for direction in regge.DIRS15
    ]
    checks.check(
        "nonnegative-source-cone-separation",
        "all fifteen nonnegative edge-source extreme rays have strictly positive homothety overlap, separating the entire nonzero cone from image Q_R(0)",
        min(extreme_overlaps) >= 1.0
        and max(extreme_overlaps) <= 2.0 + 2.0e-15,
        f"extreme overlap range=[{min(extreme_overlaps):.6f},{max(extreme_overlaps):.6f}]",
    )

    chord_row = np.zeros(15, dtype=float)
    chord_length = sqrt(5.0)
    chord_row[regge.DIR_IDX[tuple(SPACE_X)]] = -2.0 / chord_length
    chord_row[regge.DIR_IDX[tuple(TICK)]] = 4.0 / chord_length
    chord_row[regge.DIR_IDX[tuple(FACE)]] = 4.0 * sqrt(2.0) / chord_length
    chord_metric = chord_row @ regge.metric_map(zero_momentum)
    chord_target = helix.metric_covector(COARSE)
    chord_zero_data = helix.source_data(chord_row, zero_momentum)
    checks.check(
        "composite-timelike-chord-control",
        "the two-tick chord u=(1,0,0,2) has a rank-one timelike metric source but one negative edge coefficient and positive homothety charge sqrt(5)",
        abs(np.linalg.norm(COARSE) - chord_length) < 1.0e-15
        and np.max(np.abs(chord_metric - chord_target)) < 3.0e-15
        and chord_row[regge.DIR_IDX[tuple(SPACE_X)]] < 0.0
        and abs(float(np.vdot(scale_vector, chord_row).real) - chord_length) < 2.0e-15
        and chord_zero_data["solve"] > 0.1,
    )

    common_transverse = (
        np.asarray((0.0, 1.0, 0.0, 0.0)),
        np.asarray((0.0, 0.0, 1.0, 0.0)),
        np.asarray((0.0, 1.0, 1.0, 0.0)) / sqrt(2.0),
    )
    bouquet_pole_coefficients = []
    bouquet_pole_errors = []
    bouquet_pole_residuals = []
    per_step_bouquet = helix.edge_row(TICK) + helix.edge_row(FACE)
    for direction in common_transverse:
        local_coefficients = []
        for epsilon in (0.05, 0.025, 0.0125):
            coefficient, residual = response_coefficient(
                per_step_bouquet, epsilon * direction
            )
            local_coefficients.append(coefficient)
            bouquet_pole_residuals.append(residual)
        bouquet_pole_coefficients.append(local_coefficients[-1])
        bouquet_pole_errors.append(
            [abs(value - 6.0) for value in local_coefficients]
        )
    checks.check(
        "positive-bouquet-unprojected-pole",
        "three common-transverse directions give a source-contracted one-over-k-squared coefficient tending to six without projection",
        max(abs(value - 6.0) for value in bouquet_pole_coefficients) < 1.0e-4
        and max(bouquet_pole_residuals) < 5.0e-10
        and all(
            all(errors[index + 1] < errors[index] for index in range(2))
            for errors in bouquet_pole_errors
        ),
        "coefficients=" + ",".join(f"{value:.7f}" for value in bouquet_pole_coefficients),
    )

    checks.check(
        "theorem-source-surface",
        "the note states the bundle identity, binary inventory, bouquet census, homothety separator, composite control, poles, and axiom map",
        all(
            phrase in note_flat
            for phrase in (
                "J_A=J_B=(2,2,2,6)",
                "2,768",
                "2,369",
                "|d|/2",
                "sqrt(5)",
                "tending to six",
                "existing candidate",
            )
        ),
    )
    checks.check(
        "no-go-discipline-source-surface",
        "the note lands N1 through N8 and narrows the no-go to nonzero positive length sources at bare compact k=0",
        all(f"N{index}" in note for index in range(1, 9))
        and "No universal gravity no-go" in note_flat
        and "unmodified compact zero-mode equation" in note_flat
        and "not a new axiom requirement" in note_flat,
    )
    checks.check(
        "boundary-source-surface",
        "the note preserves aggregate-versus-rank-one, constituent causality, action selection, global ensemble, coupling, nonlinear, Born, and realization boundaries",
        all(
            phrase in note_flat
            for phrase in (
                "not a rank-one massive-particle stress tensor",
                "spacelike primitive edges",
                "action-weight selection",
                "compact ensemble",
                "coupling",
                "nonlinear",
                "Born",
                "realized history",
                "fixed TOE percentages remain unchanged",
            )
        ),
    )
    checks.check(
        "canonical-axiom-nonmutation",
        "the canonical memo contains none of the timelike-network, bundle-weight, or compact-homothety amendment wording",
        all(
            phrase not in axiom_flat
            for phrase in (
                "timelike edge-current network",
                "proper-cubic bundle weights",
                "compact Regge homothety constraint",
            )
        ),
    )

    print("per_element: checked all fifteen positive edge-source extreme rays, eight temporal unit directions, two bundles, and the composite chord")
    print("per_site: checked exact incoming-outgoing balance for every vertex of all 504 binary bundle histories and the connected bouquet junction")
    print("per_mode: checked all 2,768 supported binary history-mode pairs and every one of 2,369 nonzero bouquet sources against five null directions")
    print("per_block: checked number-field junction rigidity, positive timelike currents, unprojected tensor and transverse poles, and the axiom boundary")
    print("lattice_wide: checked all 8,755 Fourier modes on six four-tori, every binary history of lengths three through eight, and every compact mean")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
