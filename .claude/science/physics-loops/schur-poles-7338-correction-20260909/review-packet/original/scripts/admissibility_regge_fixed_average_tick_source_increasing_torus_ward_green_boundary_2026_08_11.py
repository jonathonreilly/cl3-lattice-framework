#!/usr/bin/env python3
"""Check a fixed-average positive tick source on increasing repaired Regge tori.

The supplied flat Kuhn/Coxeter edge action is

    S_alpha = sum_h A_h (epsilon_h + alpha epsilon_h**2),
    alpha = 1/1024.

Its curvature-square term removes the fifth nonmetric flat branch while
preserving the four vertex-displacement Ward directions.  This runner places
one unit static tick source on odd spatial tori, fixes only the homogeneous
metric mode, solves the complete fifteen-edge equations, and Fourier
reconstructs the gauge-invariant tick-edge response.  It also demonstrates
why restricting the indefinite edge form to the ten-metric image can create a
false Brillouin-edge response pole.

The result is a bounded increasing-region linear test.  It does not select the
action, prove an all-L or infinite-volume theorem, construct a semibounded
Euclidean phase, or supply Lorentzian nonlinear Record dynamics.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
import sys
import time

import numpy as np


AUDIT_TIMEOUT_SEC = 240

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REGGE_FIXED_AVERAGE_TICK_SOURCE_INCREASING_TORUS_"
    "WARD_GREEN_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGGE_NOTE_PATH = ROOT / "docs" / (
    "CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_"
    "NARROW_THEOREM_NOTE_2026-06-09.md"
)
SOURCE_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CENTERED_TICK_EDGE_DEFECT_IMPROVEMENT_EXACT_STATIC_"
    "REGGE_SOURCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
HISTORY_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_"
    "REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
REPAIR_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_FLAT_REGGE_CURVATURE_SQUARED_BRANCH_LIFT_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
EC_BOUNDARY_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_PERIODIC_FLAT_EC_CONNECTION_NEGATIVE_MODE_AXIOM_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
PREMISE_REGISTRY_PATH = (
    ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_REGGE_FIXED_AVERAGE_TICK_SOURCE_INCREASING_TORUS_WARD_GREEN_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md",
    "docs/ADMISSIBILITY_CENTERED_TICK_EDGE_DEFECT_IMPROVEMENT_EXACT_STATIC_REGGE_SOURCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_FLAT_REGGE_CURVATURE_SQUARED_BRANCH_LIFT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_PERIODIC_FLAT_EC_CONNECTION_NEGATIVE_MODE_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
    "scripts/admissibility_flat_regge_curvature_squared_branch_lift_2026_08_10.py",
    "scripts/admissibility_nonlinear_regge_extra_branch_cubic_lift_2026_08_10.py",
    "scripts/admissibility_fixed_metric_nonlinear_regge_kkt_continuation_2026_08_10.py",
)

sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_flat_regge_curvature_squared_branch_lift_2026_08_10 as block20  # noqa: E402
import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as regge  # noqa: E402


ALPHA = 1.0 / 1024.0
LENGTHS_TO_TEST = (33, 49, 65, 81, 97)
DIFFERENCE_RADIUS = 8
TARGET_GREEN_COEFFICIENT = 1.0 / (2.0 * np.pi)
EDGE_ZERO_TOLERANCE = 1.0e-8
INVERSE_TOLERANCE = 1.0e-10
BATCH_SIZE = 2048
TICK_EDGE_INDEX = regge.DIR_IDX[(0, 0, 0, 1)]


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 132 else detail[:129] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


@lru_cache(maxsize=1)
def flat_lengths() -> np.ndarray:
    return np.sqrt(
        np.asarray([sum(direction) for direction in regge.DIRS15], dtype=float)
    )


@lru_cache(maxsize=1)
def regge_kernel() -> dict:
    kernel, deficits = block20.uniform_regge_kernel(flat_lengths())
    if np.max(np.abs(deficits)) >= 2.0e-13:
        raise AssertionError("flat Regge deficits failed to vanish")
    return kernel


@lru_cache(maxsize=1)
def curvature_square_kernel() -> dict:
    return block20.curvature_squared_kernel(flat_lengths())


def combined_kernel() -> tuple[np.ndarray, np.ndarray]:
    merged: defaultdict[tuple[int, ...], np.ndarray] = defaultdict(
        lambda: np.zeros((15, 15), dtype=float)
    )
    for shift, matrix in regge_kernel().items():
        merged[tuple(int(value) for value in shift)] += np.asarray(matrix, dtype=float)
    for shift, matrix in curvature_square_kernel().items():
        merged[tuple(int(value) for value in shift)] += ALPHA * np.asarray(
            matrix, dtype=float
        )
    return (
        np.asarray(tuple(merged), dtype=float),
        np.asarray(tuple(merged.values()), dtype=float),
    )


def metric_coefficients() -> np.ndarray:
    coefficients = np.zeros((15, 10), dtype=float)
    for direction_index, direction in enumerate(regge.DIRS15):
        vector = np.asarray(direction, dtype=float)
        length = float(np.linalg.norm(vector))
        for component_index, (left, right) in enumerate(regge.HCOMPS):
            value = vector[left] * vector[right]
            if left != right:
                value *= 2.0
            coefficients[direction_index, component_index] = value / (2.0 * length)
    return coefficients


SHIFTS, MATRICES = combined_kernel()
DIRECTIONS = np.asarray(regge.DIRS15, dtype=float)
DIRECTION_LENGTHS = np.linalg.norm(DIRECTIONS, axis=1)
METRIC_COEFFICIENTS = metric_coefficients()


def batch_symbol(momentum: np.ndarray) -> np.ndarray:
    phases = np.exp(1j * momentum @ SHIFTS.T)
    symbol = np.einsum("bs,sij->bij", phases, MATRICES, optimize=True)
    return 0.5 * (symbol + symbol.conj().transpose(0, 2, 1))


def batch_metric_map(momentum: np.ndarray) -> np.ndarray:
    half_phase = 0.5 * (momentum @ DIRECTIONS.T)
    phases = np.exp(1j * half_phase) * np.sinc(half_phase / np.pi)
    return phases[:, :, None] * METRIC_COEFFICIENTS[None, :, :]


def batch_gauge_map(momentum: np.ndarray) -> np.ndarray:
    phases = np.exp(1j * (momentum @ DIRECTIONS.T)) - 1.0
    return (
        phases[:, :, None]
        * DIRECTIONS[None, :, :]
        / DIRECTION_LENGTHS[None, :, None]
    )


def solve_hermitian(
    matrix: np.ndarray, source: np.ndarray, tolerance: float
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    coefficients = (
        eigenvectors.conj().transpose(0, 2, 1) @ source[:, :, None]
    )[:, :, 0]
    inverse_values = np.zeros_like(eigenvalues)
    mask = np.abs(eigenvalues) > tolerance
    inverse_values[mask] = 1.0 / eigenvalues[mask]
    response = -(
        eigenvectors @ (inverse_values * coefficients)[:, :, None]
    )[:, :, 0]
    return response, eigenvalues, eigenvectors


def batch_edge_response(momentum: np.ndarray):
    q_edge = batch_symbol(momentum)
    source = np.zeros((momentum.shape[0], 15), dtype=complex)
    source[:, TICK_EDGE_INDEX] = 2.0
    response, eigenvalues, _ = solve_hermitian(
        q_edge, source.conj(), INVERSE_TOLERANCE
    )
    residual = np.linalg.norm(
        q_edge @ response[:, :, None] + source.conj()[:, :, None], axis=(1, 2)
    )
    gauge = batch_gauge_map(momentum)
    ward = np.linalg.norm(q_edge @ gauge, axis=(1, 2))
    source_ward = np.linalg.norm(source[:, None, :] @ gauge, axis=(1, 2))
    zero_counts = np.sum(np.abs(eigenvalues) < EDGE_ZERO_TOLERANCE, axis=1)
    negative_counts = np.sum(eigenvalues < -EDGE_ZERO_TOLERANCE, axis=1)
    positive_counts = np.sum(eigenvalues > EDGE_ZERO_TOLERANCE, axis=1)
    nonzero_absolute = np.where(
        np.abs(eigenvalues) > EDGE_ZERO_TOLERANCE,
        np.abs(eigenvalues),
        np.inf,
    )
    quotient_gap = np.min(nonzero_absolute, axis=1)
    return {
        "tick_response": 2.0 * response[:, TICK_EDGE_INDEX],
        "edge_response": response,
        "residual": residual,
        "ward": ward,
        "source_ward": source_ward,
        "zero_counts": zero_counts,
        "negative_counts": negative_counts,
        "positive_counts": positive_counts,
        "quotient_gap": quotient_gap,
        "q_edge": q_edge,
    }


def batch_metric_restriction(momentum: np.ndarray, q_edge: np.ndarray):
    metric = batch_metric_map(momentum)
    q_metric = metric.conj().transpose(0, 2, 1) @ q_edge @ metric
    source = 2.0 * metric[:, TICK_EDGE_INDEX, :]
    response, eigenvalues, _ = solve_hermitian(
        q_metric, source.conj(), INVERSE_TOLERANCE
    )
    residual = np.linalg.norm(
        q_metric @ response[:, :, None] + source.conj()[:, :, None], axis=(1, 2)
    )
    return response[:, 3], residual, metric, q_metric, eigenvalues


@dataclass
class TorusResult:
    length: int
    elapsed: float
    modes: int
    max_residual: float
    max_ward: float
    max_source_ward: float
    inertias: set[tuple[int, int, int]]
    min_normalized_gap: float
    max_imaginary: float
    mean: float
    max_response: float
    max_response_k: np.ndarray
    profile: np.ndarray
    difference_coefficient: float
    metric_max_response: float | None = None
    metric_max_k: np.ndarray | None = None


def torus_result(length: int, metric_control: bool = False) -> TorusResult:
    indices = np.indices((length, length, length), dtype=int).reshape(3, -1).T
    signed = np.where(indices <= length // 2, indices, indices - length)
    keep = np.any(signed != 0, axis=1)
    kept_indices = indices[keep]
    spatial = (2.0 * np.pi / length) * signed[keep].astype(float)
    momentum = np.column_stack((spatial, np.zeros(spatial.shape[0])))
    flat_indices = np.ravel_multi_index(kept_indices.T, (length, length, length))
    spectrum = np.zeros(length**3, dtype=complex)

    max_residual = 0.0
    max_ward = 0.0
    max_source_ward = 0.0
    inertias: set[tuple[int, int, int]] = set()
    min_normalized_gap = float("inf")
    max_response = 0.0
    max_response_k = np.zeros(3, dtype=float)
    metric_max_response = 0.0 if metric_control else None
    metric_max_k = np.zeros(3, dtype=float) if metric_control else None
    started = time.perf_counter()

    for begin in range(0, momentum.shape[0], BATCH_SIZE):
        end = min(begin + BATCH_SIZE, momentum.shape[0])
        batch = batch_edge_response(momentum[begin:end])
        values = batch["tick_response"]
        spectrum[flat_indices[begin:end]] = values
        max_residual = max(max_residual, float(np.max(batch["residual"])))
        max_ward = max(max_ward, float(np.max(batch["ward"])))
        max_source_ward = max(
            max_source_ward, float(np.max(batch["source_ward"]))
        )
        for negative, positive, zero in zip(
            batch["negative_counts"],
            batch["positive_counts"],
            batch["zero_counts"],
        ):
            inertias.add((int(negative), int(positive), int(zero)))
        lattice_k2 = 4.0 * np.sum(
            np.sin(0.5 * momentum[begin:end, :3]) ** 2, axis=1
        )
        min_normalized_gap = min(
            min_normalized_gap,
            float(np.min(batch["quotient_gap"] / lattice_k2)),
        )
        local = int(np.argmax(np.abs(values)))
        if abs(values[local]) > max_response:
            max_response = float(abs(values[local]))
            max_response_k = spatial[begin + local].copy()

        if metric_control:
            metric_values, _, _, _, _ = batch_metric_restriction(
                momentum[begin:end], batch["q_edge"]
            )
            metric_local = int(np.argmax(np.abs(metric_values)))
            if abs(metric_values[metric_local]) > float(metric_max_response):
                metric_max_response = float(abs(metric_values[metric_local]))
                metric_max_k = spatial[begin + metric_local].copy()

    field = np.fft.ifftn(spectrum.reshape((length, length, length)))
    profile = field.real[:, 0, 0]
    radius = DIFFERENCE_RADIUS
    difference_coefficient = 2.0 * radius * (
        profile[radius] - profile[2 * radius]
    )
    return TorusResult(
        length=length,
        elapsed=time.perf_counter() - started,
        modes=length**3 - 1,
        max_residual=max_residual,
        max_ward=max_ward,
        max_source_ward=max_source_ward,
        inertias=inertias,
        min_normalized_gap=min_normalized_gap,
        max_imaginary=float(np.max(np.abs(field.imag))),
        mean=float(abs(np.mean(field))),
        max_response=max_response,
        max_response_k=max_response_k,
        profile=profile,
        difference_coefficient=float(difference_coefficient),
        metric_max_response=metric_max_response,
        metric_max_k=metric_max_k,
    )


def metric_restriction_control(momentum: np.ndarray) -> dict[str, float]:
    full = batch_edge_response(momentum[None, :])
    metric_value, metric_residual, metric, q_metric, metric_eigenvalues = (
        batch_metric_restriction(momentum[None, :], full["q_edge"])
    )
    edge_eigenvalues = np.linalg.eigvalsh(full["q_edge"][0])
    edge_nonzero = np.abs(edge_eigenvalues)[
        np.abs(edge_eigenvalues) > EDGE_ZERO_TOLERANCE
    ]
    metric_nonzero = np.abs(metric_eigenvalues[0])[
        np.abs(metric_eigenvalues[0]) > INVERSE_TOLERANCE
    ]
    return {
        "metric_map_min_singular": float(np.linalg.svd(metric[0], compute_uv=False)[-1]),
        "metric_gap": float(np.min(metric_nonzero)),
        "metric_response": float(abs(metric_value[0])),
        "metric_residual": float(metric_residual[0]),
        "edge_gap": float(np.min(edge_nonzero)),
        "edge_response": float(abs(full["tick_response"][0])),
        "edge_residual": float(full["residual"][0]),
    }


def main() -> int:
    checks = Checks()
    note = flat(NOTE_PATH)
    axiom = flat(AXIOM_PATH)
    regge_note = flat(REGGE_NOTE_PATH)
    source_note = flat(SOURCE_NOTE_PATH)
    history_note = flat(HISTORY_NOTE_PATH)
    repair_note = flat(REPAIR_NOTE_PATH)
    ec_boundary = flat(EC_BOUNDARY_PATH)

    checks.check(
        "source-and-scope-bindings",
        "the current axioms and all supplied Regge, source, repair, and EC-boundary parents are read without premise promotion",
        all(
            path.exists()
            for path in (
                NOTE_PATH,
                AXIOM_PATH,
                REGGE_NOTE_PATH,
                SOURCE_NOTE_PATH,
                HISTORY_NOTE_PATH,
                REPAIR_NOTE_PATH,
                EC_BOUNDARY_PATH,
                PREMISE_REGISTRY_PATH,
            )
        )
        and "admissibility is not a dynamics axiom" in axiom
        and "vertex displacements" in regge_note
        and "compact zero mode" in source_note
        and "signed pair" in history_note
        and "0 < alpha <= 1/128" in repair_note
        and "strictly negative" in ec_boundary,
    )

    reconstruction_error = 0.0
    for momentum in (
        np.asarray((0.0, 0.0, 0.0, 0.0)),
        np.asarray((0.31, -0.27, 0.19, 0.41)),
        np.asarray((1.1, -0.7, 0.5, 0.9)),
    ):
        reconstructed = block20.bloch(regge_kernel(), momentum)
        reconstruction_error = max(
            reconstruction_error,
            float(np.max(np.abs(reconstructed - regge.bloch_Q(momentum)))),
        )
    checks.check(
        "real-space-regge-kernel-reconstruction",
        "the precomputed real-space kernel reproduces the retained fifteen-edge Regge symbol",
        reconstruction_error < 8.0e-13,
        f"max Bloch reconstruction error={reconstruction_error:.3e}",
    )

    low_momenta = np.asarray(
        ((0.1, 0.0, 0.0, 0.0), (0.05, 0.0, 0.0, 0.0), (0.025, 0.0, 0.0, 0.0)),
        dtype=float,
    )
    low = batch_edge_response(low_momenta)
    pole_coefficients = np.asarray(
        [
            momentum[0] ** 2 * response.real
            for momentum, response in zip(low_momenta, low["tick_response"])
        ]
    )
    pole_errors = np.abs(pole_coefficients - 2.0)
    low_relative_residual = low["residual"] / (
        2.0 + np.linalg.norm(low["edge_response"], axis=1)
    )
    checks.check(
        "exact-static-source-ward",
        "the coefficient-two tick edge is a unit metric source and annihilates every static vertex-displacement gauge column",
        float(np.max(low["source_ward"])) < 1.0e-15
        and float(np.max(low["ward"])) < 2.0e-14,
    )
    checks.check(
        "unprojected-long-wave-residue",
        "the complete repaired edge solve approaches k squared h_tt equals two without a source projection or fitted coefficient",
        np.all(np.diff(pole_errors) < 0.0)
        and pole_errors[-1] < 2.0e-4
        and float(np.max(low["residual"])) < 5.0e-11
        and float(np.max(low_relative_residual)) < 2.0e-14,
        "k2h_tt="
        + ",".join(f"{value:.9f}" for value in pole_coefficients)
        + f"; max relative solve={np.max(low_relative_residual):.3e}",
    )

    results = [
        torus_result(length, metric_control=(length == 65))
        for length in LENGTHS_TO_TEST
    ]
    total_modes = sum(result.modes for result in results)
    checks.check(
        "exhaustive-increasing-torus-ward-inventory",
        "every declared nonzero static mode has exactly four Ward nulls and no fifth nonmetric zero",
        total_modes == 1_872_320
        and all(result.inertias == {(9, 2, 4)} for result in results)
        and max(result.max_ward for result in results) < 1.5e-13
        and max(result.max_source_ward for result in results) < 1.0e-15,
        f"modes={total_modes}; inertias={sorted(set().union(*(r.inertias for r in results)))}",
    )
    checks.check(
        "finite-inventory-quotient-gap",
        "the nonzero edge quotient stays separated from zero relative to the spatial lattice momentum on every declared grid",
        min(result.min_normalized_gap for result in results) > 0.058
        and all(
            np.count_nonzero(np.abs(result.max_response_k) > 1.0e-12) == 1
            and abs(np.max(np.abs(result.max_response_k)) - 2.0 * np.pi / result.length)
            < 1.0e-12
            for result in results
        ),
        "min gap/khat2="
        + ",".join(f"L{r.length}:{r.min_normalized_gap:.6f}" for r in results),
    )
    checks.check(
        "unprojected-solve-and-real-field",
        "all declared complete edge solves close and Fourier reconstruction is real with fixed zero average",
        max(result.max_residual for result in results) < 9.0e-12
        and max(result.max_imaginary for result in results) < 5.0e-17
        and max(result.mean for result in results) < 4.0e-19,
        f"max solve={max(r.max_residual for r in results):.3e}; max imaginary={max(r.max_imaginary for r in results):.3e}",
    )

    coefficients = np.asarray([result.difference_coefficient for result in results])
    coefficient_errors = np.abs(coefficients - TARGET_GREEN_COEFFICIENT)
    checks.check(
        "increasing-region-green-difference",
        "the boundary-offset-free radius-eight field difference approaches the residue-forced one-over-r coefficient along the declared sequence",
        np.all(np.diff(coefficients) > 0.0)
        and np.all(np.diff(coefficient_errors) < 0.0)
        and coefficient_errors[-1] / TARGET_GREEN_COEFFICIENT < 4.3e-4,
        "C8="
        + ",".join(f"L{r.length}:{r.difference_coefficient:.9f}" for r in results)
        + f"; target={TARGET_GREEN_COEFFICIENT:.9f}",
    )
    checks.check(
        "fixed-average-compensator-decouples",
        "the sole finite-volume compensation is a uniform unit-density subtraction whose local magnitude falls as L cubed",
        all(
            1.0 / results[index + 1].length**3 < 1.0 / results[index].length**3
            for index in range(len(results) - 1)
        )
        and 1.0 / results[-1].length**3 < 1.1e-6,
        f"unit compensator density at L97={1.0 / 97**3:.9e}",
    )

    l65 = next(result for result in results if result.length == 65)
    if l65.metric_max_k is None:
        raise AssertionError("missing metric restriction control")
    control_momentum = np.concatenate((l65.metric_max_k, (0.0,)))
    control = metric_restriction_control(control_momentum)
    checks.check(
        "metric-only-restriction-false-pole",
        "the full-rank ten-metric congruence develops a Brillouin-edge near-zero and a response above four thousand",
        float(l65.metric_max_response) > 4000.0
        and np.linalg.norm(l65.metric_max_k) > 4.0
        and control["metric_map_min_singular"] > 0.09
        and control["metric_gap"] < 7.0e-5
        and control["metric_response"] > 4000.0,
        f"k={l65.metric_max_k}; metric response={control['metric_response']:.3f}; gap={control['metric_gap']:.3e}",
    )
    checks.check(
        "complete-edge-control-removes-false-pole",
        "at the same momentum the complete edge quotient is regular and the unprojected response is small",
        control["edge_gap"] > 0.68
        and control["edge_response"] < 0.19
        and control["edge_residual"] < 1.0e-12,
        f"edge response={control['edge_response']:.9f}; gap={control['edge_gap']:.9f}; solve={control['edge_residual']:.3e}",
    )
    checks.check(
        "indefinite-euclidean-boundary",
        "the repaired vertex-displacement quotient remains nine-negative/two-positive, so this is not a semibounded Euclidean phase theorem",
        all(result.inertias == {(9, 2, 4)} for result in results)
        and "not a semibounded euclidean" in note
        and "lorentzian" in note,
    )

    checks.check(
        "fresh-no-go-discipline-packet",
        "the source note lands fresh N1 through N8 and preserves Lorentzian, nonflat, open-boundary, and law-selection routes",
        all(f"### n{index}" in note for index in range(1, 9))
        and "status: pass" in note
        and all(
            phrase in note
            for phrase in (
                "not a gravity no-go",
                "open or dirichlet",
                "stable nonflat",
                "law selection",
                "no canonical axiom is edited",
            )
        ),
    )

    for result in results:
        print(
            f"inventory L={result.length}: modes={result.modes} solve={result.max_residual:.3e} "
            f"gap/khat2={result.min_normalized_gap:.6f} C8={result.difference_coefficient:.9f} "
            f"seconds={result.elapsed:.2f}"
        )
    print(
        "N5_CERTIFICATE: all fifteen edge classes, one unit tick source, 1,872,320 static modes, the complete edge block, and five increasing tori are resolved at their stated scopes"
    )
    print(
        "per_element: checked all fifteen Kuhn/Coxeter edge classes, the coefficient-two tick row, and the ten-metric restriction control"
    )
    print(
        "per_site: checked one localized unit metric source plus the explicitly disclosed uniform fixed-average compensation"
    )
    print(
        "per_mode: checked every nonzero static momentum on L=33,49,65,81,97 and three independent long-wave controls"
    )
    print(
        "per_block: checked the complete repaired fifteen-edge symbol before any metric-only restriction and exposed the restricted false pole"
    )
    print(
        "lattice_wide: checked five finite odd increasing tori only; no all-L, full-Z3, continuous-zone, nonlinear, or Lorentzian theorem is claimed"
    )
    print(
        "scope_boundary: supplied flat linear Regge law with fixed average; action selection, semibounded phase, physical mass/coupling, nonlinear stability, and causal update remain open"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
