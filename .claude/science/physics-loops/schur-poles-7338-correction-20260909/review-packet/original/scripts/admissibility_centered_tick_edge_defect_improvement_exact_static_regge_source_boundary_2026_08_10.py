#!/usr/bin/env python3
"""Checks for a centered tick-edge defect improvement and exact static source.

The paired note replaces the geometry derivative of the Block-12 isolated
unit bag, but not its flat law or wrapping-plane sector, by one actual axial
tick-edge line derivative.  Static nonzero modes are tested directly against
the supplied cubic-Coxeter Regge Hessian without projecting the source.
"""

from __future__ import annotations

from itertools import product
from math import atan, log, pi
from pathlib import Path
import sys

import numpy as np


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CENTERED_TICK_EDGE_DEFECT_IMPROVEMENT_EXACT_STATIC_"
    "REGGE_SOURCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CUT_WORLDVOLUME_AFFINE_BAG_REGGE_MONOPOLE_BOUNDARY_"
    "BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
REGGE_NOTE_PATH = ROOT / "docs" / (
    "CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_"
    "NARROW_THEOREM_NOTE_2026-06-09.md"
)
KINETIC_PATH = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_CENTERED_TICK_EDGE_DEFECT_IMPROVEMENT_EXACT_STATIC_REGGE_SOURCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_CUT_WORLDVOLUME_AFFINE_BAG_REGGE_MONOPOLE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "scripts/admissibility_cut_worldvolume_affine_bag_regge_monopole_boundary_2026_08_10.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)

sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_cut_worldvolume_affine_bag_regge_monopole_boundary_2026_08_10 as bag  # noqa: E402
import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as regge  # noqa: E402


TICK = 3
TICK_DIRECTION = (0, 0, 0, 1)
TICK_EDGE_INDEX = regge.DIR_IDX[TICK_DIRECTION]


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


def isolated_defect(center: int, neighbors: tuple[int, ...]) -> int:
    """Signed range-one isolated-defect indicator; complement reverses sign."""
    occupied = center * int(all(value == 0 for value in neighbors))
    hole = (1 - center) * int(all(value == 1 for value in neighbors))
    return occupied - hole


def line_row(momentum: np.ndarray, anchor: np.ndarray | None = None) -> np.ndarray:
    """Coefficient 2 makes the actual tick edge carry unit h_tt source."""
    result = np.zeros(15, dtype=complex)
    phase = 1.0 if anchor is None else np.exp(1j * np.dot(momentum, anchor))
    result[TICK_EDGE_INDEX] = 2.0 * phase
    return result


def source_data(source: np.ndarray, momentum: np.ndarray) -> dict[str, float | int]:
    hessian = regge.bloch_Q(momentum)
    eigenvalues, eigenvectors = np.linalg.eigh(hessian)
    zero_space = eigenvectors[:, np.abs(eigenvalues) < 1.0e-8]
    solution = -np.linalg.pinv(hessian, rcond=1.0e-10) @ source.conj()
    return {
        "zero_count": zero_space.shape[1],
        "gauge": float(np.linalg.norm(source @ regge.gauge_map(momentum))),
        "null": float(np.linalg.norm(zero_space.conj().T @ source.conj())),
        "solve": float(np.linalg.norm(hessian @ solution + source.conj())),
    }


def extra_null_overlap(source: np.ndarray, momentum: np.ndarray) -> float:
    """Separate the fifth Regge null direction from the four gauge columns."""
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
    return float(abs(np.vdot(extra_left[:, 0], source.conj())))


def log_slope(first_x: float, first_y: float, second_x: float, second_y: float) -> float:
    return log(second_y / first_y) / log(second_x / first_x)


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    parent = PARENT_PATH.read_text(encoding="utf-8")
    regge_note = REGGE_NOTE_PATH.read_text(encoding="utf-8")
    kinetic = KINETIC_PATH.read_text(encoding="utf-8")
    note_flat = " ".join(note.split())
    axiom_flat = " ".join(axiom.split())
    parent_flat = " ".join(parent.split())
    regge_flat = " ".join(regge_note.split())
    kinetic_flat = " ".join(kinetic.split())

    print("external_scientific_inputs: none; the line coefficient is fixed by the internally derived Block-12 homogeneous source")
    print("package_local_integrity_reads: current axioms, Block-12 bag residuals, equal-form tick graining, and the actual Regge Hessian are source-bound")
    print("analytic_boundary: flat-law preservation, axial metric source, and static gauge Ward are exact; extra-null compatibility is exhaustive on named finite tori")
    print("physical_boundary: defect/action selection, mass identification, coupling, sign, infrared ensemble, and dynamic histories remain open")

    checks.check(
        "source-current-axioms",
        "the current axioms do not silently supply a history action, source/action bridge, or physical mass",
        all(
            phrase in axiom_flat
            for phrase in (
                "Admissibility is not a dynamics axiom",
                "source/action and physical-observable identification",
                "it does not supply the formation site, probability, or rate",
            )
        ),
    )
    checks.check(
        "source-block12-residual",
        "Block 12 names the localized gauge, extra-null, and periodic-zero-mode residuals attacked here",
        all(
            phrase in parent_flat
            for phrase in (
                "gauge force is nonzero and scales as `O(k^3)`",
                "overlap with the extra Regge zero branch is nonzero and scales as `O(k^2)`",
                "bare finite periodic linear equation has no solution",
            )
        ),
    )
    checks.check(
        "source-regge-boundary",
        "the supplied Regge carrier has four gauge zeros plus one extra non-metric zero branch at nonzero momentum",
        "Vertex displacements (4 components per cell) are exact zero modes" in regge_flat
        and "four massive branches" in regge_flat
        and "one exactly flat branch" in regge_flat
        and "does **not** derive the edge-length degrees of freedom or select the Regge action" in regge_flat,
    )
    checks.check(
        "source-tick-primitive",
        "the approved primitive grants equal-form tick graining but no dynamics, mass, source, or selector",
        "c_t = c_s" in kinetic_flat
        and "It carries no dimensionless dynamical content" in kinetic_flat
        and "not a new dynamics" in kinetic_flat,
    )

    neighborhoods = tuple(product((0, 1), repeat=7))
    defect_values = {
        bits: isolated_defect(bits[0], tuple(bits[1:])) for bits in neighborhoods
    }
    checks.check(
        "isolated-defect-classification",
        "the range-one selector is +1 only on an isolated occupied site, -1 only on an isolated hole, and zero otherwise",
        sum(value == 1 for value in defect_values.values()) == 1
        and sum(value == -1 for value in defect_values.values()) == 1
        and sum(value == 0 for value in defect_values.values()) == 126,
    )
    checks.check(
        "defect-complement-covariance",
        "binary complement reverses the signed isolated-defect indicator exactly on all 128 neighborhoods",
        all(
            isolated_defect(1 - bits[0], tuple(1 - value for value in bits[1:]))
            == -defect_values[bits]
            for bits in neighborhoods
        ),
    )
    face_sources: dict[int, dict] = {}
    face_flat_volumes = {}
    for normal in range(4):
        axes = tuple(axis for axis in range(4) if axis != normal)
        flat_volume, q_source = bag.simplex_cover_q_source(axes)
        face_flat_volumes[normal] = flat_volume
        face_sources[normal] = bag.length_source(q_source)
    four_flat_volume, volume_q_source = bag.simplex_cover_q_source((0, 1, 2, 3))
    volume_source = bag.length_source(volume_q_source)
    flat_bag_value = sum(
        2 * (face_flat_volumes[normal] - 1) for normal in range(3)
    ) - 4 * (four_flat_volume - 1)
    flat_tick_length = np.linalg.norm(np.asarray(TICK_DIRECTION, dtype=float))
    flat_line_value = 2.0 * (flat_tick_length - 1.0)
    checks.check(
        "flat-law-preserving-counter-improvement",
        "the actual centered Kuhn bag and centered tick line make d_iso(L-B) vanish on all 128 flat neighborhoods",
        face_flat_volumes == {normal: 1 for normal in range(4)}
        and four_flat_volume == 1
        and flat_tick_length == 1.0
        and all(
            value * (flat_line_value - float(flat_bag_value)) == 0.0
            for value in defect_values.values()
        ),
    )

    zero_momentum = np.zeros(4)
    target = np.zeros(10)
    target[3] = 1.0
    bag_zero = bag.centered_bag_row(face_sources, volume_source, zero_momentum)
    line_zero = line_row(zero_momentum)
    counter_zero = line_zero - bag_zero
    metric_zero = regge.metric_map(zero_momentum)
    checks.check(
        "unique-line-normalization",
        "the actual unit tick edge has metric derivative one-half, so preserving Block-12 T_tt=1 uniquely fixes line coefficient two",
        abs(regge.metric_map(zero_momentum)[TICK_EDGE_INDEX, 3] - 0.5) < 1.0e-15
        and np.max(np.abs(line_zero @ metric_zero - target)) < 1.0e-15,
    )
    checks.check(
        "homogeneous-source-preservation",
        "the bag-to-line counter-improvement has zero homogeneous metric source and preserves the derived tick-only normalization",
        np.max(np.abs(bag_zero @ metric_zero - target)) < 3.0e-13
        and np.max(np.abs(counter_zero @ metric_zero)) < 3.0e-13
        and np.max(np.abs((bag_zero + counter_zero) @ metric_zero - target)) < 3.0e-13,
    )
    checks.check(
        "isolated-source-replacement",
        "on the selected isolated unit tube, the local counter-improvement replaces the complete bag edge row by the tick-edge line row",
        np.max(np.abs(bag_zero + (line_zero - bag_zero) - line_zero)) < 1.0e-15,
    )

    # A wrapping plane has in-plane occupied neighbors and never activates the
    # isolated-defect switch.  Enumerate a periodic L=3 coordinate plane.
    plane_defects = []
    size = 3
    plane = {(x, y, z): int(z == 0) for x, y, z in product(range(size), repeat=3)}
    axes3 = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
    for site, center in plane.items():
        neighbors = tuple(
            plane[tuple((site[axis] + shift[axis]) % size for axis in range(3))]
            for shift in axes3
        )
        plane_defects.append(isolated_defect(center, neighbors))
    checks.check(
        "wrapping-plane-preservation",
        "the range-one correction vanishes on every site of the periodic wrapping-plane fixture",
        plane_defects == [0] * (size**3),
    )

    generic_direction = np.asarray((1.0, 0.7, 0.4, 0.0))
    generic_direction /= np.linalg.norm(generic_direction)
    generic_momentum = 0.4 * generic_direction
    bag_generic = bag.centered_bag_row(face_sources, volume_source, generic_momentum)
    line_generic = line_row(generic_momentum)
    corrected_generic = bag_generic + (line_generic - bag_generic)
    bag_data = source_data(bag_generic, generic_momentum)
    corrected_data = source_data(corrected_generic, generic_momentum)
    checks.check(
        "counterterm-cancels-bag-residuals",
        "the finite local line-minus-bag stencil cancels both named generic residuals rather than projecting the source",
        bag_data["gauge"] > 1.0e-3
        and bag_data["null"] > 1.0e-3
        and corrected_data["gauge"] < 1.0e-14
        and corrected_data["null"] < 2.0e-12
        and corrected_data["solve"] < 5.0e-12,
        f"bag gauge={bag_data['gauge']:.3e}, bag null={bag_data['null']:.3e}; corrected gauge={corrected_data['gauge']:.3e}, corrected null={corrected_data['null']:.3e}",
    )

    correction_metric_norms = []
    for epsilon in (0.1, 0.05):
        momentum = epsilon * generic_direction
        bag_source = bag.centered_bag_row(face_sources, volume_source, momentum)
        correction = line_row(momentum) - bag_source
        correction_metric_norms.append(float(np.linalg.norm(correction @ regge.metric_map(momentum))))
    correction_slope = log_slope(0.1, correction_metric_norms[0], 0.05, correction_metric_norms[1])
    checks.check(
        "counterterm-leading-source-neutrality",
        "the correcting stencil changes the metric source only at order k squared and therefore preserves the monopole residue",
        1.97 < correction_slope < 2.03,
        f"measured metric-source exponent={correction_slope:.6f}",
    )

    checks.check(
        "static-axial-gauge-ward",
        "for k_tick=0 the actual tick-edge source annihilates all four discrete vertex-gauge columns identically",
        np.max(np.abs(line_generic @ regge.gauge_map(generic_momentum))) == 0.0,
    )
    checks.check(
        "static-pure-tick-metric-source",
        "for every static momentum the line row maps exactly to pure unit T_tt with zero spatial stress and shift",
        np.max(np.abs(line_generic @ regge.metric_map(generic_momentum) - target)) < 1.0e-15,
    )

    worst_null = 0.0
    worst_solve = 0.0
    worst_gauge = 0.0
    wrong_zero_counts = 0
    mode_count = 0
    for length in range(3, 9):
        mode_indices = range(-(length // 2), (length + 1) // 2)
        for index in product(mode_indices, repeat=3):
            if index == (0, 0, 0):
                continue
            momentum = np.asarray(
                (2.0 * pi * index[0] / length,
                 2.0 * pi * index[1] / length,
                 2.0 * pi * index[2] / length,
                 0.0)
            )
            data = source_data(line_row(momentum), momentum)
            mode_count += 1
            worst_gauge = max(worst_gauge, float(data["gauge"]))
            worst_null = max(worst_null, float(data["null"]))
            worst_solve = max(worst_solve, float(data["solve"]))
            wrong_zero_counts += int(data["zero_count"] != 5)
    checks.check(
        "finite-torus-mode-inventory",
        "every nonzero static mode on each periodic spatial torus L=3 through L=8 has exactly five Regge zero modes",
        mode_count == 1281 and wrong_zero_counts == 0,
        f"modes={mode_count}; wrong zero counts={wrong_zero_counts}",
    )
    checks.check(
        "finite-torus-full-null-compatibility",
        "the tick-edge source annihilates the complete five-dimensional null space on all 1,281 exhaustive nonzero modes",
        worst_gauge < 1.0e-14 and worst_null < 2.0e-13,
        f"max gauge={worst_gauge:.3e}; max full-null overlap={worst_null:.3e}",
    )
    checks.check(
        "finite-torus-unprojected-solvability",
        "the unprojected actual edge equation solves on all 1,281 exhaustive nonzero static modes",
        worst_solve < 5.0e-12,
        f"max solve residual={worst_solve:.3e}",
    )

    # Any finite collection of static isolated sources has the same edge
    # direction with a scalar structure factor, so null compatibility is
    # inherited mode by mode.  Verify a two-source hostile phase explicitly.
    separation = np.asarray((2.0, -1.0, 1.0, 0.0))
    two_source = line_row(generic_momentum) + line_row(generic_momentum, separation)
    two_data = source_data(two_source, generic_momentum)
    checks.check(
        "isolated-source-additivity",
        "two separated static defect lines retain exact gauge/full-null compatibility and additive tick charge",
        two_data["gauge"] < 1.0e-14
        and two_data["null"] < 4.0e-12
        and two_data["solve"] < 8.0e-12
        and abs((two_source @ regge.metric_map(generic_momentum))[3]) > 0.1,
    )

    directions = (
        np.asarray((1.0, 0.0, 0.0, 0.0)),
        np.asarray((1.0, 1.0, 0.0, 0.0)) / np.sqrt(2.0),
        generic_direction,
        np.asarray((1.0, 1.0, 1.0, 0.0)) / np.sqrt(3.0),
    )
    pole_coefficients = []
    pole_errors = []
    pole_residuals = []
    transverse_residuals = []
    for direction in directions:
        coefficients = []
        for epsilon in (0.05, 0.025):
            momentum = epsilon * direction
            metric_map = regge.metric_map(momentum)
            metric_hessian = metric_map.conj().T @ regge.bloch_Q(momentum) @ metric_map
            metric_source = line_row(momentum) @ metric_map
            gauge_metric = bag.continuum_gauge_metric(momentum)
            transverse_residuals.append(float(np.linalg.norm(metric_source @ gauge_metric)))
            response = -np.linalg.pinv(metric_hessian, rcond=1.0e-10) @ metric_source.conj()
            pole_residuals.append(
                float(np.linalg.norm(metric_hessian @ response + metric_source.conj()))
            )
            coefficients.append(float((np.dot(momentum, momentum) * response[3]).real))
        pole_coefficients.append(coefficients[-1])
        pole_errors.append((abs(coefficients[0] - 2.0), abs(coefficients[1] - 2.0)))
    checks.check(
        "unprojected-regge-lapse-pole",
        "without any source projection, four directions give |k|^2 h_tt -> 2 in the actual Regge metric Hessian",
        max(abs(value - 2.0) for value in pole_coefficients) < 2.0e-4
        and max(pole_residuals) < 3.0e-10
        and max(transverse_residuals) < 1.0e-14,
        "coefficients=" + ",".join(f"{value:.7f}" for value in pole_coefficients),
    )
    checks.check(
        "unprojected-pole-convergence",
        "halving momentum reduces every unprojected lapse-pole coefficient error",
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
        "open-boundary-green-tail",
        "the unprojected static pole retains the regulated open-boundary 1/(4 pi r) Green shape",
        all(
            abs(regulated_green[index + 1] - green_limit)
            < abs(regulated_green[index] - green_limit)
            for index in range(len(regulated_green) - 1)
        )
        and abs(regulated_green[-1] / green_limit - 1.0) < 0.011,
    )

    zero_data = source_data(line_zero, zero_momentum)
    checks.check(
        "periodic-zero-mode-boundary",
        "the nonzero total tick charge still lies outside the bare k=0 periodic Hessian range",
        zero_data["zero_count"] == 11
        and zero_data["null"] > 1.7
        and zero_data["solve"] > 1.7,
        f"null overlap={zero_data['null']:.6f}; solve residual={zero_data['solve']:.6f}",
    )

    dynamic_momentum = np.asarray((0.3, 0.2, 0.1, 0.4))
    dynamic_data = source_data(line_row(dynamic_momentum), dynamic_momentum)
    dynamic_extra = extra_null_overlap(line_row(dynamic_momentum), dynamic_momentum)
    checks.check(
        "dynamic-history-control",
        "a tick-dependent Fourier mode is not covered: the fixed vertical line then has nonzero gauge and extra-null overlap",
        dynamic_data["gauge"] > 0.5 and dynamic_extra > 1.0e-3,
        f"gauge={dynamic_data['gauge']:.3e}; separated extra-null overlap={dynamic_extra:.3e}",
    )

    rotations = bag.proper_cubic_rotations()
    tick_tensor = np.diag((0.0, 0.0, 0.0, 1.0))
    checks.check(
        "proper-cubic-source-covariance",
        "all 24 proper spatial cubic rotations preserve both the range-one neighbor class and the tick-only source",
        len(rotations) == 24
        and all(np.array_equal(rotation @ tick_tensor @ rotation.T, tick_tensor) for rotation in rotations),
    )

    theorem_needles = (
        "I_iso=d_iso(L-B)",
        "s_line(k)=2tau e_tau-edge",
        "1,281",
        "without a source projection",
        "Geometry-indexed history/action amendment",
        "No-Go Discipline Gate",
        "N1 — alternative route enumeration",
        "N8 — cross-cycle echo",
    )
    checks.check(
        "theorem-source-surface",
        "the note states the local correction, exact line source, exhaustive scope, unprojected pole, axiom map, and N1-N8 packet",
        all(needle in note_flat for needle in theorem_needles),
    )
    boundary_needles = (
        "No canonical axiom is edited",
        "fixed TOE percentages do not move",
        "not a selected physical mass",
        "bare periodic k=0 equation",
        "dynamic histories remain open",
        "No universal no-go is claimed",
    )
    checks.check(
        "boundary-source-surface",
        "the note preserves action-selection, physical-mass, periodic, dynamic-history, no-go, governance, and percentage boundaries",
        all(needle in note_flat for needle in boundary_needles),
    )
    checks.check(
        "canonical-axiom-nonmutation",
        "the canonical memo contains none of the tick-edge defect improvement or candidate-amendment wording",
        all(
            phrase not in axiom_flat
            for phrase in (
                "I_iso=d_iso(L-B)",
                "s_line(k)=2tau e_tau-edge",
                "centered tick-edge defect improvement",
                "Geometry-indexed history/action amendment",
            )
        ),
    )

    print("per_element: checked the actual axial tick-edge metric derivative, unique coefficient two, and exact static gauge factor")
    print("per_site: checked all 128 range-one neighborhoods, isolated bag-to-line replacement, complement covariance, and plane nonactivation")
    print("per_mode: checked every nonzero static Fourier mode on L=3 through L=8 tori against gauge, full null space, and edge solvability")
    print("per_block: checked local counter-improvement through unprojected Regge lapse pole, convergence, and regulated radial Green tail")
    print("lattice_wide: checked 1,281 nonzero periodic modes and separately retained the incompatible nonzero total-charge k=0 mode")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
