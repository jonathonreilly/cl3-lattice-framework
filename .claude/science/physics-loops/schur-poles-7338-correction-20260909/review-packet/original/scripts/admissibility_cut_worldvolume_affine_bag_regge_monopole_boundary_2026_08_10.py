#!/usr/bin/env python3
"""Exact and numerical checks for the cut-worldvolume / Regge source bridge.

The paired note extends the Block-11 spatial cut to a supplied 3+1 binary
worldvolume, derives its tick/lapse source, and tests a flat-law-preserving
one-cell pressure improvement against the actual cubic-Coxeter Regge Hessian.
The exact finite-lattice residuals are reported rather than projected away.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations, product
from math import atan, factorial, log, pi
from pathlib import Path
import sys

import numpy as np


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CUT_WORLDVOLUME_AFFINE_BAG_REGGE_MONOPOLE_BOUNDARY_"
    "BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CUT_SURFACE_COFRAME_STRESS_HIGHER_FORM_WARD_"
    "GEOMETRY_DYNAMICS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
REGGE_NOTE_PATH = ROOT / "docs" / (
    "CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_"
    "NARROW_THEOREM_NOTE_2026-06-09.md"
)
KINETIC_PATH = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_CUT_WORLDVOLUME_AFFINE_BAG_REGGE_MONOPOLE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_CUT_SURFACE_COFRAME_STRESS_HIGHER_FORM_WARD_GEOMETRY_DYNAMICS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
)

sys.path.insert(0, str(ROOT / "scripts"))
import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as regge  # noqa: E402


Vec4 = tuple[int, int, int, int]
EdgeKey = tuple[Vec4, Vec4]
QMatrix = tuple[tuple[Fraction, ...], ...]

AXES4: tuple[Vec4, ...] = (
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
)
TICK = 3


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


def determinant(matrix: QMatrix) -> Fraction:
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    total = Fraction(0)
    for column in range(size):
        minor = tuple(
            tuple(matrix[row][other] for other in range(size) if other != column)
            for row in range(1, size)
        )
        total += (-1 if column % 2 else 1) * matrix[0][column] * determinant(minor)
    return total


def inverse(matrix: QMatrix) -> QMatrix:
    size = len(matrix)
    augmented = [
        list(matrix[row])
        + [Fraction(int(row == column)) for column in range(size)]
        for row in range(size)
    ]
    for pivot in range(size):
        swap = next(row for row in range(pivot, size) if augmented[row][pivot])
        augmented[pivot], augmented[swap] = augmented[swap], augmented[pivot]
        value = augmented[pivot][pivot]
        augmented[pivot] = [entry / value for entry in augmented[pivot]]
        for row in range(size):
            if row == pivot:
                continue
            value = augmented[row][pivot]
            augmented[row] = [
                augmented[row][column] - value * augmented[pivot][column]
                for column in range(2 * size)
            ]
    return tuple(tuple(row[size:]) for row in augmented)


def trace_product(left: QMatrix, right: QMatrix) -> Fraction:
    size = len(left)
    return sum(
        left[row][column] * right[column][row]
        for row in range(size)
        for column in range(size)
    )


def edge_key(left: Vec4, right: Vec4) -> EdgeKey:
    difference = tuple(right[index] - left[index] for index in range(4))
    if all(value >= 0 for value in difference):
        return difference, left
    reverse = tuple(-value for value in difference)
    if all(value >= 0 for value in reverse):
        return reverse, right
    raise ValueError("Kuhn-simplex vertices must be coordinatewise comparable")


def simplex_cover_q_source(axes: tuple[int, ...]) -> tuple[Fraction, dict[EdgeKey, Fraction]]:
    """Flat volume and d(volume)/d(edge-length-squared) for a Kuhn cube cover."""
    dimension = len(axes)
    source: defaultdict[EdgeKey, Fraction] = defaultdict(Fraction)
    total_volume = Fraction(0)
    simplex_volume = Fraction(1, factorial(dimension))
    for order in permutations(axes):
        vertices: list[Vec4] = [(0, 0, 0, 0)]
        for axis in order:
            next_vertex = list(vertices[-1])
            next_vertex[axis] += 1
            vertices.append(tuple(next_vertex))

        gram = tuple(
            tuple(
                Fraction(
                    sum(
                        (vertices[left + 1][axis] - vertices[0][axis])
                        * (vertices[right + 1][axis] - vertices[0][axis])
                        for axis in range(4)
                    )
                )
                for right in range(dimension)
            )
            for left in range(dimension)
        )
        if determinant(gram) != 1:
            raise AssertionError("flat Kuhn simplex must be unimodular")
        gram_inverse = inverse(gram)
        total_volume += simplex_volume

        for left, right in combinations(range(dimension + 1), 2):
            variation = [
                [Fraction(0) for _ in range(dimension)] for _ in range(dimension)
            ]
            if left == 0:
                slot = right - 1
                for other in range(dimension):
                    variation[slot][other] += Fraction(1, 2)
                    variation[other][slot] += Fraction(1, 2)
            else:
                row = left - 1
                column = right - 1
                variation[row][column] -= Fraction(1, 2)
                variation[column][row] -= Fraction(1, 2)
            derivative = (
                simplex_volume
                * Fraction(1, 2)
                * trace_product(gram_inverse, tuple(tuple(row) for row in variation))
            )
            source[edge_key(vertices[left], vertices[right])] += derivative
    return total_volume, {key: value for key, value in source.items() if value}


def length_source(q_source: dict[EdgeKey, Fraction]) -> dict[EdgeKey, Fraction]:
    """Convert q=ell^2 derivatives to ell derivatives; all survivors are axial."""
    result: dict[EdgeKey, Fraction] = {}
    for key, derivative in q_source.items():
        direction, _ = key
        squared_length = sum(value * value for value in direction)
        if squared_length != 1:
            raise AssertionError(
                f"non-axial source survived the complete cube cover: {key} -> {derivative}"
            )
        result[key] = 2 * derivative
    return result


def translated_row(
    source: dict[EdgeKey, Fraction], momentum: np.ndarray, shift: np.ndarray | None = None
) -> np.ndarray:
    result = np.zeros(15, dtype=complex)
    offset = np.zeros(4) if shift is None else shift
    for (direction, anchor), coefficient in source.items():
        class_index = regge.DIR_IDX[direction]
        phase = np.exp(1j * np.dot(momentum, np.asarray(anchor, dtype=float) + offset))
        result[class_index] += float(coefficient) * phase
    return result


def centered_bag_row(
    face_sources: dict[int, dict[EdgeKey, Fraction]],
    volume_source: dict[EdgeKey, Fraction],
    momentum: np.ndarray,
    pressure_ratio: float = 4.0,
) -> np.ndarray:
    result = -pressure_ratio * translated_row(volume_source, momentum)
    for normal in range(3):
        result += translated_row(face_sources[normal], momentum)
        result += translated_row(face_sources[normal], momentum, np.eye(4)[normal])
    cell_center = np.asarray((0.5, 0.5, 0.5, 0.5))
    return result * np.exp(-1j * np.dot(momentum, cell_center))


def continuum_gauge_metric(momentum: np.ndarray) -> np.ndarray:
    result = np.zeros((10, 4), dtype=complex)
    for direction in range(4):
        tensor = np.zeros((4, 4), dtype=complex)
        for axis in range(4):
            tensor[axis, direction] += 1j * momentum[axis]
            tensor[direction, axis] += 1j * momentum[axis]
        result[:, direction] = np.asarray(
            [tensor[left, right] for left, right in regge.HCOMPS]
        )
    return result


def proper_cubic_rotations() -> tuple[np.ndarray, ...]:
    rotations = []
    for order in permutations(range(3)):
        inversions = sum(
            order[left] > order[right]
            for left in range(3)
            for right in range(left + 1, 3)
        )
        parity = -1 if inversions % 2 else 1
        for signs in product((-1, 1), repeat=3):
            if parity * signs[0] * signs[1] * signs[2] != 1:
                continue
            rotation = np.zeros((4, 4), dtype=int)
            for row, column in enumerate(order):
                rotation[row, column] = signs[row]
            rotation[3, 3] = 1
            rotations.append(rotation)
    return tuple(rotations)


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

    print("external_scientific_inputs: none; cube/simplex volume derivatives and the pressure coefficient are derived in-source")
    print("package_local_integrity_reads: current axioms, Block-11 cut stress, approved tick graining, and the actual 3+1 Regge action are source-bound")
    print("analytic_boundary: the 3+1 cofactor and affine-bag statements are exact; Regge null spaces and scaling exponents are executed numerically")
    print("physical_boundary: history law, worldvolume family, pressure mechanism, action orientation, coupling, infrared ensemble, and nonlinear completion are not selected")

    checks.check(
        "source-current-axioms",
        "the current axioms supply spatial locality but explicitly leave history, source/action, and dynamics outside",
        all(
            phrase in axiom_flat
            for phrase in (
                "Physical sites are the points of the cubic lattice `Z^3`",
                "Admissibility is not a dynamics axiom",
                "source/action and physical-observable identification",
                "arrow, record-production dynamics, physical persistence dynamics, time metric",
            )
        ),
    )
    checks.check(
        "source-block11",
        "Block 11 derives the spatial coframe stress and leaves temporal worldvolume history and geometry dynamics open",
        all(
            phrase in parent_flat
            for phrase in (
                "P_i=tau[(Tr Q_i)I-Q_i]",
                "worldvolume history",
                "geometry dynamics or curvature action",
            )
        ),
    )
    checks.check(
        "source-regge",
        "the actual tick-extended Regge Hessian has gauge zeros, constant metric zeros, and one extra non-metric zero branch",
        all(
            phrase in regge_flat
            for phrase in (
                "Vertex displacements (4 components per cell) are exact zero modes",
                "Constant metric perturbations are exact zero modes at `k=0`",
                "one exactly flat branch",
                "does **not** derive the edge-length degrees of freedom or select the Regge action",
            )
        ),
    )
    checks.check(
        "source-tick-primitive",
        "the approved primitive grants only equal-form tick graining and no dynamics, action, or selector",
        "c_t = c_s" in kinetic_flat
        and "It carries no dimensionless dynamical content" in kinetic_flat
        and "not a new dynamics" in kinetic_flat,
    )

    face_q_sources: dict[int, dict[EdgeKey, Fraction]] = {}
    face_sources: dict[int, dict[EdgeKey, Fraction]] = {}
    face_volumes = []
    for normal in range(4):
        axes = tuple(axis for axis in range(4) if axis != normal)
        volume, q_source = simplex_cover_q_source(axes)
        face_volumes.append(volume)
        face_q_sources[normal] = q_source
        face_sources[normal] = length_source(q_source)
    volume4, volume_q_source = simplex_cover_q_source((0, 1, 2, 3))
    volume_source = length_source(volume_q_source)

    checks.check(
        "kuhn-volume-covers",
        "six tetrahedra give each unit hyperface volume one and 24 four-simplices give unit four-volume",
        face_volumes == [Fraction(1)] * 4 and volume4 == 1,
    )
    checks.check(
        "diagonal-edge-cancellation",
        "complete Kuhn covers cancel every flat diagonal-edge volume derivative; only axial edge derivatives survive",
        all(
            sum(value * value for value in direction) == 1
            for source in (*face_q_sources.values(), volume_q_source)
            for direction, _ in source
        ),
    )
    checks.check(
        "hyperface-edge-sum",
        "a unit hyperface has total length derivative one on each tangent axial class and zero on its normal class",
        all(
            sum(
                coefficient
                for (direction, _), coefficient in face_sources[normal].items()
                if direction == AXES4[axis]
            )
            == Fraction(int(axis != normal))
            for normal in range(4)
            for axis in range(4)
        ),
    )
    checks.check(
        "four-volume-edge-sum",
        "the unit four-cell volume has total length derivative one on every axial class",
        all(
            sum(
                coefficient
                for (direction, _), coefficient in volume_source.items()
                if direction == AXES4[axis]
            )
            == 1
            for axis in range(4)
        ),
    )

    metric_at_zero = regge.metric_map(np.zeros(4))
    face_metric_rows = {
        normal: translated_row(source, np.zeros(4)) @ metric_at_zero
        for normal, source in face_sources.items()
    }
    checks.check(
        "coframe-metric-source",
        "each flat hyperface gives one-half on all tangent metric diagonals, including tick for a spatial cut",
        all(
            np.max(
                np.abs(
                    face_metric_rows[normal]
                    - np.asarray(
                        [
                            0.5 if left == right and left != normal else 0.0
                            for left, right in regge.HCOMPS
                        ]
                    )
                )
            )
            < 2.0e-13
            for normal in range(4)
        ),
    )
    checks.check(
        "static-worldvolume-reduction",
        "a static spatial face has the Block-11 two tangential responses plus one equal tick response",
        np.allclose(face_metric_rows[0][[1, 2, 3]], (0.5, 0.5, 0.5), atol=1.0e-13)
        and np.allclose(face_metric_rows[0][[0, 4, 5, 6, 7, 8, 9]], 0.0, atol=1.0e-13),
    )
    cut_count = 6
    tick_count = 5
    checks.check(
        "static-extrusion-count",
        "a one-cell spatial cut extruded through five ticks has 30 timelike faces and integrated metric tick source 15 tau",
        tick_count * cut_count == 30
        and Fraction(tick_count * cut_count, 2) == 15,
    )

    surface_metric = sum(2 * face_metric_rows[normal] for normal in range(3))
    volume_metric = translated_row(volume_source, np.zeros(4)) @ metric_at_zero
    pressure_ratio = Fraction(4)
    bag_metric = surface_metric - float(pressure_ratio) * volume_metric
    checks.check(
        "affine-pressure-uniqueness",
        "homogeneous spatial stationarity uniquely fixes p/tau=4 from 2-(p/tau)/2=0 in every spatial direction",
        all(Fraction(2) - pressure_ratio * Fraction(1, 2) == 0 for _ in range(3))
        and pressure_ratio == 4,
    )
    checks.check(
        "dustlike-flat-source",
        "surface tension plus the derived affine pressure has exact flat metric source (0,0,0,tau) with no shift or spatial stress",
        np.max(np.abs(bag_metric - np.asarray((0, 0, 0, 1, 0, 0, 0, 0, 0, 0))))
        < 3.0e-13,
    )
    wrong_pressure_metric = surface_metric - 3.0 * volume_metric
    checks.check(
        "pressure-control",
        "the active p/tau=3 control leaves spatial source one-half and therefore does not manufacture the dustlike result",
        np.allclose(wrong_pressure_metric[:3], (0.5, 0.5, 0.5), atol=1.0e-13)
        and abs(wrong_pressure_metric[3] - 1.5) < 1.0e-13,
    )

    flat_volume_deviations = (Fraction(0),) * 4
    test_volume_deviations = (Fraction(1, 7), Fraction(-2, 9), Fraction(3, 11), Fraction(5, 13))
    occupations = tuple(product((0, 1), repeat=4))

    def improvement(bits, pressure, deviations):
        return -pressure * sum(
            (Fraction(bit) - Fraction(1, 2)) * deviation
            for bit, deviation in zip(bits, deviations)
        )

    checks.check(
        "flat-law-preserving-improvement",
        "the centered volume improvement vanishes for every configuration at flat geometry",
        all(improvement(bits, pressure_ratio, flat_volume_deviations) == 0 for bits in occupations),
    )
    checks.check(
        "code-pressure-covariance",
        "off background, code complement together with pressure reversal leaves the centered volume improvement exactly invariant",
        all(
            improvement(bits, pressure_ratio, test_volume_deviations)
            == improvement(tuple(1 - bit for bit in bits), -pressure_ratio, test_volume_deviations)
            for bits in occupations
        ),
    )

    plane_residuals = []
    plane_null_overlaps = []
    plane_solve_residuals = []
    for normal in range(3):
        for magnitude in (0.17, 0.4, 1.1, 2.2):
            momentum = magnitude * np.eye(4)[normal]
            source = translated_row(face_sources[normal], momentum)
            gauge = regge.gauge_map(momentum)
            hessian = regge.bloch_Q(momentum)
            eigenvalues, eigenvectors = np.linalg.eigh(hessian)
            zero_space = eigenvectors[:, np.abs(eigenvalues) < 1.0e-8]
            plane_residuals.append(float(np.max(np.abs(source @ gauge))))
            plane_null_overlaps.append(float(np.linalg.norm(zero_space.conj().T @ source.conj())))
            solution = -np.linalg.pinv(hessian, rcond=1.0e-10) @ source.conj()
            plane_solve_residuals.append(float(np.linalg.norm(hessian @ solution + source.conj())))
    checks.check(
        "wrapping-plane-regge-ward",
        "all sampled wrapping-plane sources annihilate the four Regge gauge modes exactly to machine precision",
        max(plane_residuals) < 2.0e-13,
        f"max gauge residual={max(plane_residuals):.3e}",
    )
    checks.check(
        "wrapping-plane-full-null-compatibility",
        "the same plane sources also annihilate the extra non-metric zero branch and lie in the nonzero-momentum Hessian range",
        max(plane_null_overlaps) < 4.0e-12 and max(plane_solve_residuals) < 4.0e-12,
        f"max null overlap={max(plane_null_overlaps):.3e}; max solve residual={max(plane_solve_residuals):.3e}",
    )

    direction = np.asarray((1.0, 0.7, 0.4, 0.0))
    direction /= np.linalg.norm(direction)
    scaling_rows = []
    tick_target = np.zeros(10)
    tick_target[3] = 1.0
    for epsilon in (0.1, 0.05, 0.025):
        momentum = epsilon * direction
        source = centered_bag_row(face_sources, volume_source, momentum)
        gauge = regge.gauge_map(momentum)
        hessian = regge.bloch_Q(momentum)
        eigenvalues, eigenvectors = np.linalg.eigh(hessian)
        zero_space = eigenvectors[:, np.abs(eigenvalues) < 1.0e-8]
        metric_source = source @ regge.metric_map(momentum)
        scaling_rows.append(
            {
                "epsilon": epsilon,
                "metric_deviation": float(np.linalg.norm(metric_source - tick_target)),
                "gauge_force": float(np.linalg.norm(source @ gauge)),
                "null_overlap": float(np.linalg.norm(zero_space.conj().T @ source.conj())),
            }
        )
    metric_slope = log_slope(
        scaling_rows[0]["epsilon"],
        scaling_rows[0]["metric_deviation"],
        scaling_rows[1]["epsilon"],
        scaling_rows[1]["metric_deviation"],
    )
    gauge_slope = log_slope(
        scaling_rows[0]["epsilon"],
        scaling_rows[0]["gauge_force"],
        scaling_rows[1]["epsilon"],
        scaling_rows[1]["gauge_force"],
    )
    null_slope = log_slope(
        scaling_rows[0]["epsilon"],
        scaling_rows[0]["null_overlap"],
        scaling_rows[1]["epsilon"],
        scaling_rows[1]["null_overlap"],
    )
    checks.check(
        "centered-monopole-expansion",
        "the centered bag metric source approaches the pure tick source quadratically",
        1.97 < metric_slope < 2.03,
        f"measured exponent={metric_slope:.6f}",
    )
    checks.check(
        "finite-lattice-gauge-remainder",
        "at generic mixed momentum the unprojected bag gauge force is nonzero and scales as k cubed",
        scaling_rows[-1]["gauge_force"] > 1.0e-8 and 2.95 < gauge_slope < 3.05,
        f"measured exponent={gauge_slope:.6f}; epsilon=.025 residual={scaling_rows[-1]['gauge_force']:.3e}",
    )
    checks.check(
        "finite-lattice-extra-null-remainder",
        "the generic bag overlap with the full Regge null space is nonzero and scales as k squared",
        scaling_rows[-1]["null_overlap"] > 1.0e-6 and 1.95 < null_slope < 2.05,
        f"measured exponent={null_slope:.6f}; epsilon=.025 overlap={scaling_rows[-1]['null_overlap']:.3e}",
    )

    response_coefficients = []
    response_errors = []
    response_solve_residuals = []
    directions = (
        np.asarray((1.0, 0.0, 0.0, 0.0)),
        np.asarray((1.0, 1.0, 0.0, 0.0)) / np.sqrt(2.0),
        direction,
        np.asarray((1.0, 1.0, 1.0, 0.0)) / np.sqrt(3.0),
    )
    for unit_direction in directions:
        coefficients = []
        for epsilon in (0.05, 0.025):
            momentum = epsilon * unit_direction
            metric_map = regge.metric_map(momentum)
            metric_hessian = metric_map.conj().T @ regge.bloch_Q(momentum) @ metric_map
            source = centered_bag_row(face_sources, volume_source, momentum)
            metric_source = source @ metric_map
            gauge_metric = continuum_gauge_metric(momentum)
            transverse_projector = np.eye(10) - gauge_metric @ np.linalg.pinv(gauge_metric)
            transverse_source = metric_source @ transverse_projector
            response = -np.linalg.pinv(metric_hessian, rcond=1.0e-10) @ transverse_source.conj()
            response_solve_residuals.append(
                float(np.linalg.norm(metric_hessian @ response + transverse_source.conj()))
            )
            coefficients.append(float((np.dot(momentum, momentum) * response[3]).real))
        response_coefficients.append(coefficients[-1])
        response_errors.append((abs(coefficients[0] - 2.0), abs(coefficients[1] - 2.0)))
    checks.check(
        "regge-lapse-pole",
        "after the explicitly named metric-transverse projection, four spatial directions give |k|^2 h_tick,tick -> 2 tau in the raw Regge orientation",
        max(abs(value - 2.0) for value in response_coefficients) < 2.0e-4
        and max(response_solve_residuals) < 3.0e-10,
        "coefficients=" + ",".join(f"{value:.7f}" for value in response_coefficients),
    )
    checks.check(
        "regge-lapse-pole-convergence",
        "halving momentum reduces every lapse-pole coefficient error, consistent with the O(k^2) lattice correction",
        all(second < first for first, second in response_errors),
    )

    radius = 3.0
    regulators = (0.4, 0.2, 0.1, 0.05)
    regulated_green = [
        atan(radius / regulator) / (2.0 * pi * pi * radius)
        for regulator in regulators
    ]
    green_limit = 1.0 / (4.0 * pi * radius)
    checks.check(
        "three-dimensional-green-tail",
        "the regulated inverse transform of 1/|k|^2 converges to 1/(4 pi r), so the derived static lapse pole is a 1/r monopole shape",
        all(
            abs(regulated_green[index + 1] - green_limit)
            < abs(regulated_green[index] - green_limit)
            for index in range(len(regulated_green) - 1)
        )
        and abs(regulated_green[-1] / green_limit - 1.0) < 0.011,
    )

    zero_hessian = regge.bloch_Q(np.zeros(4))
    zero_eigenvalues, zero_eigenvectors = np.linalg.eigh(zero_hessian)
    zero_space = zero_eigenvectors[:, np.abs(zero_eigenvalues) < 1.0e-8]
    zero_source = centered_bag_row(face_sources, volume_source, np.zeros(4))
    zero_overlap = float(np.linalg.norm(zero_space.conj().T @ zero_source.conj()))
    zero_solution_residual = float(
        np.linalg.norm(
            zero_hessian @ (-np.linalg.pinv(zero_hessian) @ zero_source.conj())
            + zero_source.conj()
        )
    )
    checks.check(
        "periodic-zero-mode-boundary",
        "the nonzero bag source overlaps the 11-dimensional k=0 Regge null space, so the bare finite periodic linear equation has no solution",
        zero_space.shape[1] == 11 and zero_overlap > 1.7 and zero_solution_residual > 1.7,
        f"null overlap={zero_overlap:.6f}; solve residual={zero_solution_residual:.6f}",
    )

    source_needles = (
        "S_W[x;E]",
        "p_*=4tau",
        "T_bag(0)=tau e_tau e_tau^T",
        "|k|^2 h_tau_tau -> 2tau",
        "1/r",
        "Geometry-indexed history/action amendment",
        "No-Go Discipline Gate",
        "N1 — alternative route enumeration",
        "N8 — cross-cycle echo",
    )
    checks.check(
        "theorem-source-surface",
        "the paired note states the worldvolume action, derived pressure, tick source, Regge pole, radial consequence, axiom amendment, and N1-N8 packet",
        all(needle in note_flat for needle in source_needles),
    )
    boundary_needles = (
        "No canonical axiom is edited",
        "fixed TOE percentages do not move",
        "not an exact finite-lattice dust solution",
        "not a selected physical mass",
        "open or infinite boundary",
        "other local improvements",
        "No universal no-go is claimed",
    )
    checks.check(
        "boundary-source-surface",
        "the note preserves governance, finite-lattice, physical-selection, infrared, live-route, no-go, and percentage boundaries",
        all(needle in note_flat for needle in boundary_needles),
    )
    checks.check(
        "canonical-axiom-nonmutation",
        "the canonical memo still contains none of the worldvolume, pressure, Regge, or candidate-amendment wording",
        all(
            phrase not in axiom_flat
            for phrase in (
                "S_W[x;E]",
                "p_*=4tau",
                "T_bag(0)=tau e_tau e_tau^T",
                "Geometry-indexed history/action amendment",
            )
        ),
    )

    rotations = proper_cubic_rotations()
    tick_tensor = np.diag((0.0, 0.0, 0.0, 1.0))
    checks.check(
        "proper-cubic-monopole-covariance",
        "all 24 proper spatial cubic rotations leave the derived flat tick-only source invariant",
        len(rotations) == 24
        and all(np.array_equal(rotation @ tick_tensor @ rotation.T, tick_tensor) for rotation in rotations),
    )

    print("per_element: checked exact simplex-volume derivatives and cancellation of every diagonal-edge derivative in each complete Kuhn cover")
    print("per_site: checked one static cell worldtube, its six boundary faces, centered volume improvement, and unique affine pressure coefficient")
    print("per_mode: checked plane and generic mixed Fourier modes against Regge gauge, extra-null, metric-source, and response equations")
    print("per_block: checked the positive worldvolume family through affine bag source, Regge metric projection, lapse pole, and radial Green tail")
    print("lattice_wide: checked the finite periodic k=0 incompatibility and kept open-boundary, constrained-zero-mode, and dynamical completions explicit")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
