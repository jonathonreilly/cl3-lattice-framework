#!/usr/bin/env python3
"""Checks for a closed helical defect history and neutral Regge source pair.

The paired note turns the Block-13 tick-edge line into a two-member edge
family: the static tick line and one moving tick-space face-diagonal line.  A
closed line has an exact telescoping vertex-gauge Ward identity.  A signed
pair of parallel closed lines cancels the compact zero mode and is tested
directly against the actual Regge edge Hessian without source projection.
"""

from __future__ import annotations

from itertools import product
from math import atan, pi
from pathlib import Path
import sys

import numpy as np


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_"
    "REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
STATIC_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CENTERED_TICK_EDGE_DEFECT_IMPROVEMENT_EXACT_STATIC_"
    "REGGE_SOURCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
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

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_CENTERED_TICK_EDGE_DEFECT_IMPROVEMENT_EXACT_STATIC_REGGE_SOURCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_CUT_WORLDVOLUME_AFFINE_BAG_REGGE_MONOPOLE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "scripts/admissibility_centered_tick_edge_defect_improvement_exact_static_regge_source_boundary_2026_08_10.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)

sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_centered_tick_edge_defect_improvement_exact_static_regge_source_boundary_2026_08_10 as static  # noqa: E402
import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as regge  # noqa: E402


TICK = np.asarray((0, 0, 0, 1), dtype=int)
HELIX = np.asarray((1, 0, 0, 1), dtype=int)
TRANSVERSE = np.asarray((0, 1, 0, 0), dtype=int)
BODY = np.asarray((1, 1, 1, 1), dtype=int)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition: bool, detail: str = "") -> None:
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {statement}")
        if detail:
            print(f"       {detail}")
        self.passed += int(ok)
        self.failed += int(not ok)


def centered_indices(length: int) -> range:
    return range(-(length // 2), (length + 1) // 2)


def edge_row(direction: np.ndarray, momentum: np.ndarray | None = None) -> np.ndarray:
    """Derivative of 2(ell_v-|v|) with respect to actual edge lengths."""
    del momentum  # the single anchored edge has no additional phase
    row = np.zeros(15, dtype=complex)
    row[regge.DIR_IDX[tuple(int(value) for value in direction)]] = 2.0
    return row


def structure_factor(length: int, momentum: np.ndarray, direction: np.ndarray) -> complex:
    theta = float(np.dot(momentum, direction))
    return sum(np.exp(1j * step * theta) for step in range(length))


def closed_line_row(
    length: int,
    momentum: np.ndarray,
    direction: np.ndarray,
    anchor: np.ndarray | None = None,
) -> np.ndarray:
    origin = np.zeros(4, dtype=float) if anchor is None else np.asarray(anchor, dtype=float)
    phase = np.exp(1j * np.dot(momentum, origin))
    return phase * structure_factor(length, momentum, direction) * edge_row(direction)


def neutral_pair_row(length: int, momentum: np.ndarray) -> np.ndarray:
    return (
        closed_line_row(length, momentum, HELIX)
        - closed_line_row(length, momentum, HELIX, TRANSVERSE)
    )


def source_data(source: np.ndarray, momentum: np.ndarray) -> dict[str, float | int]:
    return static.source_data(source, momentum)


def extra_null_vector(momentum: np.ndarray) -> np.ndarray:
    """Return the fifth Regge zero direction after removing the four gauges."""
    hessian = regge.bloch_Q(momentum)
    eigenvalues, eigenvectors = np.linalg.eigh(hessian)
    zero_space = eigenvectors[:, np.abs(eigenvalues) < 1.0e-8]
    gauge_left, gauge_singular, _ = np.linalg.svd(
        regge.gauge_map(momentum), full_matrices=False
    )
    gauge_basis = gauge_left[:, gauge_singular > 1.0e-10]
    projected = (
        np.eye(hessian.shape[0], dtype=complex)
        - gauge_basis @ gauge_basis.conj().T
    ) @ zero_space
    extra_left, extra_singular, _ = np.linalg.svd(projected, full_matrices=False)
    if gauge_basis.shape[1] != 4 or zero_space.shape[1] != 5 or extra_singular[0] < 0.9:
        raise AssertionError("expected four gauge directions plus one independent zero branch")
    return extra_left[:, 0]


def metric_tensor(components: np.ndarray) -> np.ndarray:
    result = np.zeros((4, 4), dtype=complex)
    for value, (left, right) in zip(components, regge.HCOMPS):
        result[left, right] = value
        result[right, left] = value
    return result


def metric_covector(direction: np.ndarray) -> np.ndarray:
    vector = np.asarray(direction, dtype=float)
    length = np.linalg.norm(vector)
    values = []
    for left, right in regge.HCOMPS:
        basis = np.zeros((4, 4), dtype=float)
        basis[left, right] += 1.0
        if left != right:
            basis[right, left] += 1.0
        values.append(float(vector @ basis @ vector) / length)
    return np.asarray(values)


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    static_note = STATIC_NOTE_PATH.read_text(encoding="utf-8")
    history_note = HISTORY_NOTE_PATH.read_text(encoding="utf-8")
    regge_note = REGGE_NOTE_PATH.read_text(encoding="utf-8")
    kinetic = KINETIC_PATH.read_text(encoding="utf-8")
    note_flat = " ".join(note.split())
    axiom_flat = " ".join(axiom.split())
    static_flat = " ".join(static_note.split())
    history_flat = " ".join(history_note.split())
    regge_flat = " ".join(regge_note.split())
    kinetic_flat = " ".join(kinetic.split())

    print("external_scientific_inputs: none; the closed-line Ward identity is a finite geometric sum on the supplied edge carrier")
    print("package_local_integrity_reads: current axioms, Block-13 static source, the existing history/action candidate, and the actual Regge Hessian are source-bound")
    print("analytic_boundary: loop closure and the four vertex-gauge Ward directions are exact on every declared torus mode")
    print("physical_boundary: the moving line is prescribed Euclidean history data; positive mass, causal selection, Lorentzian dynamics, coupling, and realization remain open")

    checks.check(
        "source-current-axioms",
        "the current axioms do not silently select a moving history, source action, infrared ensemble, or geometry dynamics",
        "Admissibility is not a dynamics axiom" in axiom_flat
        and "update laws" in axiom_flat
        and "source/action and physical-observable identification" in axiom_flat,
    )
    checks.check(
        "source-block13-boundary",
        "Block 13 supplies the exact static tick edge while leaving a conserved dynamic history and compact zero mode open",
        "fixed vertical edge is not a conserved dynamic worldline" in static_flat
        and "compact nonzero-charge zero mode" in static_flat
        and "actual axial tick-edge source" in static_flat,
    )
    checks.check(
        "source-existing-history-amendment",
        "the existing candidate already permits a fixed history action and a background-subtracted zero-mode ensemble",
        "fixed unnormalized local" in history_flat
        and "action representative" in history_flat
        and "background-subtracted" in history_flat
        and "This is sufficient wording, not adopted wording" in history_flat,
    )
    checks.check(
        "source-regge-boundary",
        "the supplied carrier has fifteen edge classes, four gauge directions, and one extra decoupled branch",
        "**15** edge classes" in regge_flat
        and "four massive branches" in regge_flat
        and "one exactly flat branch" in regge_flat,
    )
    checks.check(
        "source-tick-primitive",
        "equal-form tick graining supplies no history choice, source sign, or dynamics",
        "It carries no dimensionless dynamical content" in kinetic_flat
        and "not a new dynamics" in kinetic_flat,
    )

    closure_ok = True
    disjoint_ok = True
    flat_action_ok = True
    for length in range(3, 9):
        for direction in (TICK, HELIX):
            vertices = {
                tuple((step * direction) % length)
                for step in range(length)
            }
            closure_ok &= len(vertices) == length
            closure_ok &= np.array_equal((length * direction) % length, np.zeros(4, dtype=int))
            flat_length = float(np.linalg.norm(direction))
            flat_action_ok &= 2.0 * sum(flat_length - flat_length for _ in range(length)) == 0.0
        first = {tuple((step * HELIX) % length) for step in range(length)}
        second = {tuple((TRANSVERSE + step * HELIX) % length) for step in range(length)}
        disjoint_ok &= first.isdisjoint(second)
    checks.check(
        "closed-edge-history",
        "the static and face-diagonal histories are closed L-edge cycles for every L=3 through L=8",
        closure_ok and flat_action_ok,
    )
    checks.check(
        "transverse-pair-disjointness",
        "translation by one y edge produces a distinct parallel closed helix on every declared torus",
        disjoint_ok,
    )

    static_momentum = np.asarray((0.31, -0.22, 0.17, 0.0))
    static_source = edge_row(TICK)
    static_target = np.zeros(10)
    static_target[3] = 1.0
    checks.check(
        "static-member-block13",
        "the v=t member is exactly the Block-13 coefficient-two tick-edge source and pure T_tt row",
        np.array_equal(static_source, static.line_row(static_momentum))
        and np.max(np.abs(static_source @ regge.metric_map(static_momentum) - static_target)) < 1.0e-15,
    )

    hostile_length = 7
    hostile_index = np.asarray((2, 1, -3, -2), dtype=float)
    hostile_momentum = 2.0 * pi * hostile_index / hostile_length
    hostile_anchor = np.asarray((0, 1, 1, 0), dtype=float)
    direct_sum = sum(
        np.exp(1j * np.dot(hostile_momentum, hostile_anchor + step * HELIX))
        for step in range(hostile_length)
    )
    formula_sum = (
        np.exp(1j * np.dot(hostile_momentum, hostile_anchor))
        * structure_factor(hostile_length, hostile_momentum, HELIX)
    )
    checks.check(
        "closed-line-fourier-transform",
        "the analytic structure factor equals the direct transform of all seven actual helix edges",
        abs(direct_sum - formula_sum) < 1.0e-13
        and abs(abs(formula_sum) - hostile_length) < 1.0e-13,
    )

    helix_length = float(np.linalg.norm(HELIX))
    principal_momentum = np.asarray((0.37, 0.22, -0.19, -0.37))
    principal_metric_source = edge_row(HELIX) @ regge.metric_map(principal_momentum)
    expected_metric_source = metric_covector(HELIX)
    checks.check(
        "dynamic-rank-one-metric-source",
        "on principal support k dot v=0 the moving actual edge maps exactly to v tensor v divided by |v|",
        abs(np.dot(principal_momentum, HELIX)) < 1.0e-15
        and np.max(np.abs(principal_metric_source - expected_metric_source)) < 2.0e-15
        and abs(principal_metric_source[6]) > 1.0,
    )
    checks.check(
        "dynamic-metric-ward",
        "the principal moving metric source annihilates all four continuum gauge columns",
        np.linalg.norm(
            principal_metric_source @ static.bag.continuum_gauge_metric(principal_momentum)
        ) < 2.0e-15,
    )

    total_modes = 0
    sourced_modes = 0
    dynamic_modes = 0
    principal_modes = 0
    principal_dynamic_modes = 0
    umklapp_modes = 0
    wrong_zero_counts = 0
    worst_ward = 0.0
    worst_null = 0.0
    worst_solve = 0.0
    worst_unsourced = 0.0
    worst_umklapp_metric = 0.0
    single_nonzero_modes = 0
    single_wrong_zero_counts = 0
    single_worst_ward = 0.0
    single_worst_null = 0.0
    single_worst_solve = 0.0
    per_length: list[tuple[int, int, int]] = []
    for length in range(3, 9):
        local_sourced = 0
        local_dynamic = 0
        indices = centered_indices(length)
        for index in product(indices, repeat=4):
            total_modes += 1
            momentum = 2.0 * pi * np.asarray(index, dtype=float) / length
            single_source = closed_line_row(length, momentum, HELIX)
            if any(value != 0 for value in index) and np.linalg.norm(single_source) > 2.0e-12:
                single_nonzero_modes += 1
                single_data = source_data(single_source, momentum)
                single_wrong_zero_counts += int(single_data["zero_count"] != 5)
                single_worst_ward = max(single_worst_ward, float(single_data["gauge"]))
                single_worst_null = max(single_worst_null, float(single_data["null"]))
                single_worst_solve = max(single_worst_solve, float(single_data["solve"]))
            source = neutral_pair_row(length, momentum)
            ward = source @ regge.gauge_map(momentum)
            worst_ward = max(worst_ward, float(np.linalg.norm(ward)))
            expected_sourced = ((index[0] + index[3]) % length == 0) and (index[1] % length != 0)
            if not expected_sourced:
                worst_unsourced = max(worst_unsourced, float(np.linalg.norm(source)))
                continue
            sourced_modes += 1
            local_sourced += 1
            is_dynamic = index[3] != 0
            dynamic_modes += int(is_dynamic)
            local_dynamic += int(is_dynamic)
            index_sum = index[0] + index[3]
            if index_sum == 0:
                principal_modes += 1
                principal_dynamic_modes += int(is_dynamic)
            else:
                umklapp_modes += 1
                worst_umklapp_metric = max(
                    worst_umklapp_metric,
                    float(np.linalg.norm(source @ regge.metric_map(momentum))),
                )
            data = source_data(source, momentum)
            wrong_zero_counts += int(data["zero_count"] != 5)
            worst_null = max(worst_null, float(data["null"]))
            worst_solve = max(worst_solve, float(data["solve"]))
        per_length.append((length, local_sourced, local_dynamic))

    checks.check(
        "finite-torus-support-inventory",
        "the neutral pair has 1,088 nonzero Fourier sources among all 8,755 modes on L=3 through L=8",
        total_modes == 8755
        and sourced_modes == 1088
        and per_length == [(3, 18, 12), (4, 48, 36), (5, 100, 80), (6, 180, 150), (7, 294, 252), (8, 448, 392)]
        and worst_unsourced < 2.0e-12,
        f"total={total_modes}; sourced={sourced_modes}; per-L={per_length}",
    )
    checks.check(
        "dynamic-mode-inventory",
        "922 sourced modes have nonzero tick frequency; 824 are principal metric-support modes and 98 are disclosed Umklapp modes",
        dynamic_modes == 922
        and principal_modes == 990
        and principal_dynamic_modes == 824
        and umklapp_modes == 98
        and worst_umklapp_metric < 2.0e-12,
        f"dynamic={dynamic_modes}; principal={principal_modes}; principal-dynamic={principal_dynamic_modes}; Umklapp={umklapp_modes}",
    )
    checks.check(
        "closed-line-exact-gauge-ward",
        "the telescoping closed-line identity annihilates all four vertex-gauge directions on every declared torus mode",
        worst_ward < 2.0e-13,
        f"max gauge residual={worst_ward:.3e}",
    )
    checks.check(
        "finite-torus-zero-inventory",
        "every one of the 1,088 nonzero pair sources meets a five-dimensional Regge zero space",
        wrong_zero_counts == 0,
        f"wrong zero counts={wrong_zero_counts}",
    )
    checks.check(
        "finite-torus-full-null-compatibility",
        "the neutral moving pair annihilates the complete Regge null space on all 1,088 sourced modes",
        worst_null < 3.0e-13,
        f"max full-null overlap={worst_null:.3e}",
    )
    checks.check(
        "finite-torus-unprojected-solvability",
        "the actual unprojected edge equation solves on all 1,088 sourced modes",
        worst_solve < 5.0e-12,
        f"max direct solve residual={worst_solve:.3e}",
    )
    checks.check(
        "single-line-fixed-global-mode-route",
        "after removing only k=0, one positive helix is Ward/full-null compatible and directly solvable on all 1,281 supported nonzero modes",
        single_nonzero_modes == 1281
        and single_wrong_zero_counts == 0
        and single_worst_ward < 2.0e-13
        and single_worst_null < 3.0e-13
        and single_worst_solve < 5.0e-12,
        (
            f"supported={single_nonzero_modes}; gauge={single_worst_ward:.3e}; "
            f"full-null={single_worst_null:.3e}; solve={single_worst_solve:.3e}"
        ),
    )

    zero_momentum = np.zeros(4)
    single_zero = closed_line_row(5, zero_momentum, HELIX)
    pair_zero = neutral_pair_row(5, zero_momentum)
    single_zero_data = source_data(single_zero, zero_momentum)
    pair_zero_data = source_data(pair_zero, zero_momentum)
    checks.check(
        "single-line-zero-mode-control",
        "one positive closed helix retains a nonzero compact k=0 incompatibility",
        np.linalg.norm(single_zero) == 10.0
        and single_zero_data["zero_count"] == 11
        and single_zero_data["null"] > 8.0
        and single_zero_data["solve"] > 8.0,
        f"null overlap={single_zero_data['null']:.6f}; solve residual={single_zero_data['solve']:.6f}",
    )
    checks.check(
        "neutral-pair-zero-mode-cancellation",
        "the signed transverse pair cancels k=0 exactly rather than projecting the source",
        np.array_equal(pair_zero, np.zeros(15, dtype=complex))
        and pair_zero_data["null"] == 0.0
        and pair_zero_data["solve"] == 0.0,
    )

    body_momentum = np.asarray((0.3, 0.2, -0.1, -0.4))
    body_source = edge_row(BODY)
    body_data = source_data(body_source, body_momentum)
    body_extra = static.extra_null_overlap(body_source, body_momentum)
    checks.check(
        "body-diagonal-extra-branch-control",
        "closed-line gauge conservation alone is insufficient: the full body-diagonal edge lies in the fifth null branch on this carrier",
        body_data["gauge"] < 1.0e-14
        and body_extra > 1.9
        and body_data["solve"] > 1.9,
        f"gauge={body_data['gauge']:.3e}; extra-null={body_extra:.6f}; solve={body_data['solve']:.6f}",
    )
    body_extra_vector = extra_null_vector(body_momentum)
    body_hessian = regge.bloch_Q(body_momentum)
    lifted_body_hessian = body_hessian + np.outer(
        body_extra_vector, body_extra_vector.conj()
    )
    lifted_body_solution = -np.linalg.pinv(
        lifted_body_hessian, rcond=1.0e-10
    ) @ body_source.conj()
    lifted_body_residual = float(
        np.linalg.norm(lifted_body_hessian @ lifted_body_solution + body_source.conj())
    )
    lifted_body_gauge = float(
        np.linalg.norm(lifted_body_hessian @ regge.gauge_map(body_momentum))
    )
    lifted_body_zero_count = int(
        np.count_nonzero(np.abs(np.linalg.eigvalsh(lifted_body_hessian)) < 1.0e-8)
    )
    checks.check(
        "body-diagonal-lifted-branch-route",
        "an explicit rank-one lift of only the fifth branch preserves four gauge zeros and makes the body source solvable",
        lifted_body_zero_count == 4
        and lifted_body_gauge < 2.0e-13
        and lifted_body_residual < 1.0e-12,
        (
            f"zero-count={lifted_body_zero_count}; gauge={lifted_body_gauge:.3e}; "
            f"solve={lifted_body_residual:.3e}"
        ),
    )

    perpendicular_directions = (
        np.asarray((1.0, 0.0, 0.0, -1.0)) / np.sqrt(2.0),
        np.asarray((0.0, 1.0, 0.0, 0.0)),
        np.asarray((0.0, 0.0, 1.0, 0.0)),
        np.asarray((1.0, 1.0, 1.0, -1.0)) / 2.0,
    )
    pole_coefficients = []
    pole_errors = []
    pole_residuals = []
    pole_wards = []
    pole_target = 2.0 * helix_length
    for direction in perpendicular_directions:
        coefficients = []
        for epsilon in (0.05, 0.025):
            momentum = epsilon * direction
            metric_map = regge.metric_map(momentum)
            metric_hessian = metric_map.conj().T @ regge.bloch_Q(momentum) @ metric_map
            metric_source = edge_row(HELIX) @ metric_map
            pole_wards.append(
                float(np.linalg.norm(metric_source @ static.bag.continuum_gauge_metric(momentum)))
            )
            response = -np.linalg.pinv(metric_hessian, rcond=1.0e-10) @ metric_source.conj()
            pole_residuals.append(
                float(np.linalg.norm(metric_hessian @ response + metric_source.conj()))
            )
            response_tensor = metric_tensor(response)
            unit_tangent = HELIX.astype(float) / helix_length
            coefficients.append(
                float((np.dot(momentum, momentum) * (unit_tangent @ response_tensor @ unit_tangent)).real)
            )
        pole_coefficients.append(coefficients[-1])
        pole_errors.append((abs(coefficients[0] - pole_target), abs(coefficients[1] - pole_target)))
    checks.check(
        "unprojected-moving-line-pole",
        "four transverse directions give |k|^2 h_vv -> 2 sqrt(2) without source projection",
        max(abs(value - pole_target) for value in pole_coefficients) < 2.0e-4
        and max(pole_residuals) < 3.0e-10
        and max(pole_wards) < 2.0e-14,
        "coefficients=" + ",".join(f"{value:.7f}" for value in pole_coefficients),
    )
    checks.check(
        "moving-line-pole-convergence",
        "halving transverse momentum reduces every moving-line pole-coefficient error",
        all(second < first for first, second in pole_errors),
    )

    radius = 3.0
    regulators = (0.4, 0.2, 0.1, 0.05)
    regulated_green = [
        atan(radius / regulator) / (2.0 * pi * pi * radius)
        for regulator in regulators
    ]
    green_limit = 1.0 / (4.0 * pi * radius)
    checks.check(
        "open-transverse-green-tail",
        "the moving line pole has the regulated three-transverse-dimensional 1/(4 pi r_perp) Green shape",
        all(
            abs(regulated_green[index + 1] - green_limit)
            < abs(regulated_green[index] - green_limit)
            for index in range(len(regulated_green) - 1)
        )
        and abs(regulated_green[-1] / green_limit - 1.0) < 0.011,
    )

    checks.check(
        "theorem-source-surface",
        "the note states the closed action, telescoping Ward identity, neutral pair, inventories, pole, Umklapp boundary, and axiom map",
        all(
            phrase in note_flat
            for phrase in (
                "A_v,a[g]=2 sum",
                "F_L(theta)(exp(i theta)-1)=exp(i L theta)-1=0",
                "1,088",
                "922",
                "824",
                "98",
                "2 sqrt(2)",
                "per-lattice-step",
                "No physical line-density convention is selected",
                "background-subtracted",
                "existing candidate",
            )
        ),
    )
    checks.check(
        "no-go-discipline-source-surface",
        "the note carries N1 through N8 and rejects a universal body-diagonal, dynamics, mass, or new-axiom reading",
        all(f"N{index}" in note for index in range(1, 9))
        and "No universal no-go" in note_flat
        and "not a dynamics law" in note_flat
        and "not a positive-mass ensemble" in note_flat
        and "no new axiom is required" in note_flat,
    )
    checks.check(
        "boundary-source-surface",
        "the note preserves Euclidean/Lorentzian, selection, positivity, coupling, nonlinear, Born, and realized-history boundaries",
        all(
            phrase in note_flat
            for phrase in (
                "Euclidean face diagonal",
                "naive Lorentzian continuation",
                "physical action representative",
                "coupling sign",
                "nonlinear completion",
                "Born functional",
                "realized history",
                "fixed TOE percentages remain unchanged",
            )
        ),
    )
    checks.check(
        "canonical-axiom-nonmutation",
        "the canonical memo contains none of the helical-history or neutral-pair amendment wording",
        all(
            phrase not in axiom_flat
            for phrase in (
                "closed helical defect history",
                "neutral Regge source pair",
                "tick-space face-diagonal line",
            )
        ),
    )

    print("per_element: checked the actual tick and tick-space face-diagonal line derivatives, rank-one metric map, and body-diagonal rejector")
    print("per_site: checked closed L-edge helices and one disjoint transverse signed pair for every L=3 through L=8")
    print("per_mode: checked 1,281 fixed-global-mode positive-line sources and all 1,088 neutral-pair sources against the complete Regge null space")
    print("per_block: checked static-member inheritance through exact moving Ward identity, neutral infrared cancellation, unprojected pole, and open transverse Green tail")
    print("lattice_wide: checked all 8,755 Fourier modes on six four-tori and solved every sourced edge equation without projection")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
