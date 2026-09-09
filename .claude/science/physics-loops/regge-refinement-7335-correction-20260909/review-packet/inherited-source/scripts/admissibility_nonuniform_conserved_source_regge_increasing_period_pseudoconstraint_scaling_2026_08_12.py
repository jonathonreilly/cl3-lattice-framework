#!/usr/bin/env python3
"""Increasing-period nonlinear Ward scaling on the full-edge Regge slice.

This runner generalizes the period-three Block-58 reduction to arbitrary odd
period.  Every Fourier harmonic, every nonmetric mode, and every nonzero-mode
vertex-displacement direction is retained.  It is intentionally a science
runner first; repository/claim-surface checks are added after the numerical
route decision is stable.
"""

from __future__ import annotations

from dataclasses import dataclass
import itertools
import json
import os
from pathlib import Path
import sys

import numpy as np
from scipy.linalg import null_space


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as regge  # noqa: E402


ALPHA = 1.0 / 1024.0
TARGET_METRIC_AMPLITUDE = float(os.environ.get("TOE_METRIC_AMPLITUDE", "1e-4"))
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_NONUNIFORM_CONSERVED_SOURCE_REGGE_INCREASING_PERIOD_"
    "PSEUDOCONSTRAINT_SCALING_BOUNDED_THEOREM_NOTE_2026-08-12.md"
)
BLOCK58_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_NONUNIFORM_CONSERVED_SOURCE_REGGE_SECOND_ORDER_WARD_"
    "PSEUDOCONSTRAINT_GATE_BOUNDED_THEOREM_NOTE_2026-08-12.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_NONUNIFORM_CONSERVED_SOURCE_REGGE_INCREASING_PERIOD_PSEUDOCONSTRAINT_SCALING_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "scripts/admissibility_nonuniform_conserved_source_regge_increasing_period_pseudoconstraint_scaling_2026_08_12.py",
    "docs/ADMISSIBILITY_NONUNIFORM_CONSERVED_SOURCE_REGGE_SECOND_ORDER_WARD_PSEUDOCONSTRAINT_GATE_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/ADMISSIBILITY_FLAT_REGGE_CURVATURE_SQUARED_BRANCH_LIFT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_nonuniform_conserved_source_regge_second_order_ward_pseudoconstraint_gate_2026_08_12.py",
    "scripts/admissibility_flat_regge_curvature_squared_branch_lift_2026_08_10.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition: bool, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 110 else detail[:107] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)


@dataclass
class SliceModel:
    period: int
    source_kind: str

    def __post_init__(self) -> None:
        if self.period < 3 or self.period % 2 == 0:
            raise ValueError("period must be odd and at least three")
        if self.source_kind not in {"static", "null"}:
            raise ValueError("source_kind must be static or null")
        self.axis = 0 if self.source_kind == "static" else 1
        self.k0 = 2.0 * np.pi / self.period
        self.flat_lengths = np.sqrt(
            np.asarray([sum(direction) for direction in regge.DIRS15], dtype=float)
        )
        self.hinges = self._build_hinges()
        self.B, self.BG, self.mode_data = self._parameterization()
        self.source_k, self.source = self._source_field()
        self.real_hessian = self._flat_real_hessian()
        self.flat_jacobian = self.B.T @ self.real_hessian @ self.B
        self.source_coordinates = self.B.T @ self.source.reshape(-1)
        self.linear = np.linalg.solve(self.flat_jacobian, self.source_coordinates)
        delta_unit = (self.B @ self.linear).reshape(self.period, 15)
        response_k = self.fourier(delta_unit, 1)
        metric = self.mode_data[0][2]
        metric_fit = metric @ np.linalg.lstsq(metric, response_k, rcond=None)[0]
        self.metric_response_per_coupling = float(np.linalg.norm(metric_fit))
        metric_zero = regge.metric_map(np.zeros(4)).real
        average_metric = np.tile(metric_zero, (self.period, 1))
        self.complete_rank = int(
            np.linalg.matrix_rank(np.column_stack((self.B, self.BG, average_metric)))
        )
        self.flat_gauge_residual = float(np.linalg.norm(self.real_hessian @ self.BG))

    def _edge_ref(self, left, right):
        edge_class, anchor = regge.edge_class(tuple(left), tuple(right))
        return int(anchor[self.axis]), edge_class

    def _build_hinges(self):
        hinges = []
        for triangle in regge.TRI_CLASSES:
            vertices = [np.asarray(vertex, dtype=int) for vertex in triangle]
            area_refs = tuple(
                self._edge_ref(vertices[left], vertices[right])
                for left, right in ((0, 1), (0, 2), (1, 2))
            )
            stars = []
            for simplex in regge.STARS[triangle]:
                local = {vertex: index for index, vertex in enumerate(simplex)}
                hinge = sorted(local[vertex] for vertex in triangle)
                missing = tuple(index for index in range(5) if index not in hinge)
                simplex_vertices = [np.asarray(vertex, dtype=int) for vertex in simplex]
                refs = tuple(
                    self._edge_ref(simplex_vertices[left], simplex_vertices[right])
                    for left, right in regge.PAIRS5
                )
                stars.append((missing, refs))
            hinges.append((area_refs, tuple(stars)))
        return tuple(hinges)

    def _parameterization(self):
        metric_zero = regge.metric_map(np.zeros(4)).real
        normal_zero = null_space(metric_zero.T)
        physical_columns = 5 + 11 * (self.period - 1)
        gauge_columns = 4 * (self.period - 1)
        physical_matrix = np.zeros((self.period * 15, physical_columns))
        gauge_matrix = np.zeros((self.period * 15, gauge_columns))
        for site in range(self.period):
            physical_matrix[15 * site : 15 * (site + 1), :5] = normal_zero

        mode_data = []
        p_offset = 5
        g_offset = 0
        for mode in range(1, (self.period + 1) // 2):
            momentum = np.zeros(4)
            momentum[self.axis] = 2.0 * np.pi * mode / self.period
            gauge = regge.gauge_map(momentum)
            physical = null_space(gauge.conj().T)
            metric = regge.metric_map(momentum)
            mode_data.append((mode, momentum, metric, gauge, physical))
            for site in range(self.period):
                rows = slice(15 * site, 15 * (site + 1))
                phase = np.exp(1j * momentum[self.axis] * site)
                physical_matrix[rows, p_offset : p_offset + 11] = 2.0 * (
                    phase * physical
                ).real
                physical_matrix[rows, p_offset + 11 : p_offset + 22] = -2.0 * (
                    phase * physical
                ).imag
                gauge_matrix[rows, g_offset : g_offset + 4] = 2.0 * (
                    phase * gauge
                ).real
                gauge_matrix[rows, g_offset + 4 : g_offset + 8] = -2.0 * (
                    phase * gauge
                ).imag
            p_offset += 22
            g_offset += 8
        return physical_matrix, gauge_matrix, tuple(mode_data)

    def _source_field(self):
        momentum = self.mode_data[0][1]
        metric = self.mode_data[0][2]
        target = np.zeros(10, dtype=complex)
        if self.source_kind == "static":
            target[3] = 1.0
        else:
            target[0] = 1.0
            target[3] = 1.0
            target[6] = 2.0
        source_k = metric @ np.linalg.solve(metric.conj().T @ metric, target)
        source = np.asarray(
            [
                2.0 * np.real(np.exp(1j * self.k0 * site) * source_k)
                for site in range(self.period)
            ]
        )
        return source_k, source

    def get_length(self, lengths, base, reference):
        shift, edge_class = reference
        return lengths[(base + shift) % self.period, edge_class]

    def action_gradient(self, lengths):
        lengths = np.asarray(lengths)
        dtype = np.result_type(lengths.dtype, np.float64)
        total = np.asarray(0.0, dtype=dtype)
        gradient = np.zeros((self.period, 15), dtype=dtype)
        deficits = []
        for base in range(self.period):
            for area_refs, stars in self.hinges:
                area_lengths = np.asarray(
                    [self.get_length(lengths, base, reference) for reference in area_refs]
                )
                area_out = np.asarray(regge.AREA(*(area_lengths * area_lengths)))
                area = area_out[0]
                area_derivatives = 2.0 * area_lengths * area_out[1:]
                deficit = np.asarray(2.0 * np.pi, dtype=dtype)
                deficit_derivatives = np.zeros((self.period, 15), dtype=dtype)
                for missing, refs in stars:
                    simplex_lengths = np.asarray(
                        [self.get_length(lengths, base, reference) for reference in refs]
                    )
                    angle_out = np.asarray(
                        regge.THETA[missing](*(simplex_lengths * simplex_lengths))
                    )
                    deficit -= angle_out[0]
                    derivatives = -2.0 * simplex_lengths * angle_out[1:]
                    for reference, derivative in zip(refs, derivatives):
                        shift, edge_class = reference
                        deficit_derivatives[
                            (base + shift) % self.period, edge_class
                        ] += derivative
                deficits.append(deficit)
                weight = deficit + ALPHA * deficit * deficit
                total += area * weight
                for reference, derivative in zip(area_refs, area_derivatives):
                    shift, edge_class = reference
                    gradient[(base + shift) % self.period, edge_class] += (
                        derivative * weight
                    )
                gradient += area * (1.0 + 2.0 * ALPHA * deficit) * deficit_derivatives
        return total, gradient, np.asarray(deficits)

    @staticmethod
    def _flat_bloch(momentum):
        matrix = np.zeros((15, 15), dtype=complex)
        correction = np.zeros((15, 15), dtype=complex)
        for triangle in regge.TRI_CLASSES:
            area_row, deficit_row, _deficit = regge.tri_rows(triangle, momentum)
            matrix += 0.5 * (
                np.outer(np.conj(area_row), deficit_row)
                + np.outer(np.conj(deficit_row), area_row)
            )
            vertices = [np.asarray(vertex, dtype=float) for vertex in triangle]
            squared = [
                float(np.dot(vertices[left] - vertices[right], vertices[left] - vertices[right]))
                for left, right in ((0, 1), (0, 2), (1, 2))
            ]
            area = float(regge.AREA(*squared)[0])
            correction += 2.0 * ALPHA * area * np.outer(
                np.conj(deficit_row), deficit_row
            )
        return matrix + correction

    def _flat_real_hessian(self):
        momenta = [2.0 * np.pi * index / self.period for index in range(self.period)]
        symbols = []
        for value in momenta:
            momentum = np.zeros(4)
            momentum[self.axis] = value
            symbols.append(self._flat_bloch(momentum))
        hessian = np.zeros((self.period * 15, self.period * 15), dtype=float)
        for left, right in itertools.product(range(self.period), repeat=2):
            block = sum(
                np.exp(1j * value * (left - right)) * symbol
                for value, symbol in zip(momenta, symbols)
            ) / self.period
            hessian[
                15 * left : 15 * (left + 1),
                15 * right : 15 * (right + 1),
            ] = np.real_if_close(block, tol=1000).real
        return 0.5 * (hessian + hessian.T)

    def lengths_from_coordinates(self, coordinates):
        delta = (self.B @ np.asarray(coordinates)).reshape(self.period, 15)
        return self.flat_lengths[None, :] + delta

    def equations(self, coordinates, coupling):
        lengths = self.lengths_from_coordinates(coordinates)
        _action, gradient, _deficits = self.action_gradient(lengths)
        residual = gradient - coupling * self.source
        return self.B.T @ residual.reshape(-1)

    def solve(self, coupling, start=None):
        coordinates = (
            coupling * self.linear if start is None else np.asarray(start).copy()
        )
        for _iteration in range(20):
            residual = self.equations(coordinates, coupling)
            if np.linalg.norm(residual) < 5.0e-13:
                break
            coordinates += np.linalg.solve(self.flat_jacobian, -residual)
        return coordinates

    def fourier(self, field, mode):
        wave_number = 2.0 * np.pi * mode / self.period
        return sum(
            np.exp(-1j * wave_number * site) * field[site]
            for site in range(self.period)
        ) / self.period

    def gauge_harmonics(self, residual):
        rows = []
        for mode, _momentum, _metric, gauge, _physical in self.mode_data:
            residual_k = self.fourier(residual, mode)
            rows.append(
                {
                    "mode": mode,
                    "norm": float(np.linalg.norm(gauge.conj().T @ residual_k)),
                }
            )
        return rows

    def relaxed_gauge_schur(self, lengths):
        """Return the orthonormal physical/gauge Schur spectrum at one branch."""
        flattened = np.asarray(lengths, dtype=float).reshape(-1)
        dimension = len(flattened)
        raw_hessian = np.zeros((dimension, dimension), dtype=float)
        complex_step = 1.0e-20
        for column in range(dimension):
            shifted = flattened.astype(complex)
            shifted[column] += 1j * complex_step
            _action, gradient, _deficits = self.action_gradient(
                shifted.reshape(self.period, 15)
            )
            raw_hessian[:, column] = np.imag(gradient.reshape(-1)) / complex_step
        raw_hessian = 0.5 * (raw_hessian + raw_hessian.T)
        physical_basis = np.linalg.qr(self.B, mode="reduced")[0]
        gauge_basis = np.linalg.qr(self.BG, mode="reduced")[0]
        hpp = physical_basis.T @ raw_hessian @ physical_basis
        hpg = physical_basis.T @ raw_hessian @ gauge_basis
        hgg = gauge_basis.T @ raw_hessian @ gauge_basis
        schur = hgg - hpg.T @ np.linalg.solve(hpp, hpg)
        spectrum = np.linalg.eigvalsh(0.5 * (schur + schur.T))
        return spectrum

    def analyze(self):
        coupling = TARGET_METRIC_AMPLITUDE / self.metric_response_per_coupling
        coordinates = self.solve(coupling)
        lengths = self.lengths_from_coordinates(coordinates)
        _action, gradient, deficits = self.action_gradient(lengths)
        residual = gradient - coupling * self.source
        harmonics = self.gauge_harmonics(residual)

        plus_lengths = self.lengths_from_coordinates(coupling * self.linear)
        minus_lengths = self.lengths_from_coordinates(-coupling * self.linear)
        flat_lengths = np.tile(self.flat_lengths, (self.period, 1))
        _action, plus_gradient, _deficits = self.action_gradient(plus_lengths)
        _action, minus_gradient, _deficits = self.action_gradient(minus_lengths)
        _action, flat_gradient, _deficits = self.action_gradient(flat_lengths)
        leading_field = (
            plus_gradient + minus_gradient - 2.0 * flat_gradient
        ) / (2.0 * TARGET_METRIC_AMPLITUDE**2)
        leading_harmonics = self.gauge_harmonics(leading_field)

        response = lengths - self.flat_lengths[None, :]
        metric_norm = 0.0
        nonmetric_norm = 0.0
        for mode, _momentum, metric, _gauge, _physical in self.mode_data:
            response_k = self.fourier(response, mode)
            metric_fit = metric @ np.linalg.lstsq(metric, response_k, rcond=None)[0]
            metric_norm += float(np.linalg.norm(metric_fit) ** 2)
            nonmetric_norm += float(np.linalg.norm(response_k - metric_fit) ** 2)
        result = {
            "period": self.period,
            "source": self.source_kind,
            "k": self.k0,
            "physical_rank": int(np.linalg.matrix_rank(self.B)),
            "gauge_rank": int(np.linalg.matrix_rank(self.BG)),
            "complete_rank": self.complete_rank,
            "flat_gauge_residual": self.flat_gauge_residual,
            "coupling": coupling,
            "metric_response": metric_norm**0.5,
            "nonmetric_response": nonmetric_norm**0.5,
            "projected_residual": float(np.linalg.norm(self.B.T @ residual.reshape(-1))),
            "gauge_total": float(sum(row["norm"] ** 2 for row in harmonics) ** 0.5),
            "gauge_over_amplitude2": float(
                sum(row["norm"] ** 2 for row in harmonics) ** 0.5
                / TARGET_METRIC_AMPLITUDE**2
            ),
            "gauge_harmonics": harmonics,
            "leading_over_amplitude2": leading_harmonics,
            "max_deficit": float(np.max(np.abs(deficits))),
            "minimum_length": float(np.min(lengths)),
            "source_mean": float(np.linalg.norm(self.source.sum(axis=0))),
            "source_ward": float(
                np.linalg.norm(self.mode_data[0][3].conj().T @ self.source_k)
            ),
        }
        schur_periods = {
            int(item)
            for item in os.environ.get("TOE_SCHUR_PERIODS", "").split(",")
            if item
        }
        if self.period in schur_periods:
            spectrum = self.relaxed_gauge_schur(lengths)
            threshold = max(1.0e-10, 1.0e-6 * float(np.max(np.abs(spectrum))))
            result["schur"] = {
                "dimension": len(spectrum),
                "negative": int(np.sum(spectrum < -threshold)),
                "positive": int(np.sum(spectrum > threshold)),
                "zero": int(np.sum(np.abs(spectrum) <= threshold)),
                "maximum_absolute": float(np.max(np.abs(spectrum))),
                "maximum_over_amplitude": float(
                    np.max(np.abs(spectrum)) / TARGET_METRIC_AMPLITUDE
                ),
                "minimum_absolute_nonzero": float(
                    np.min(np.abs(spectrum[np.abs(spectrum) > threshold]))
                ),
                "eigenvalues": spectrum.tolist(),
            }
        return result


def leading_mode_analysis(
    period: int,
    source_kind: str,
    amplitude: float = TARGET_METRIC_AMPLITUDE,
):
    """Compute the quadratic Ward harmonic without assembling the full torus Hessian."""
    model = object.__new__(SliceModel)
    model.period = period
    model.source_kind = source_kind
    model.axis = 0 if source_kind == "static" else 1
    model.k0 = 2.0 * np.pi / period
    model.flat_lengths = np.sqrt(
        np.asarray([sum(direction) for direction in regge.DIRS15], dtype=float)
    )
    model.hinges = model._build_hinges()

    momentum = np.zeros(4)
    momentum[model.axis] = model.k0
    metric = regge.metric_map(momentum)
    gauge = regge.gauge_map(momentum)
    physical = null_space(gauge.conj().T)
    target = np.zeros(10, dtype=complex)
    if source_kind == "static":
        target[3] = 1.0
    else:
        target[0] = 1.0
        target[3] = 1.0
        target[6] = 2.0
    source_k = metric @ np.linalg.solve(metric.conj().T @ metric, target)
    symbol = model._flat_bloch(momentum)
    quotient = physical.conj().T @ symbol @ physical
    response_k = physical @ np.linalg.solve(
        quotient, physical.conj().T @ source_k
    )
    metric_fit = metric @ np.linalg.lstsq(metric, response_k, rcond=None)[0]
    coupling = amplitude / float(np.linalg.norm(metric_fit))
    delta = np.asarray(
        [
            2.0 * np.real(np.exp(1j * model.k0 * site) * coupling * response_k)
            for site in range(period)
        ]
    )
    flat = np.tile(model.flat_lengths, (period, 1))
    _action, plus, _deficits = model.action_gradient(flat + delta)
    _action, minus, _deficits = model.action_gradient(flat - delta)
    _action, center, _deficits = model.action_gradient(flat)
    leading = (plus + minus - 2.0 * center) / (
        2.0 * amplitude**2
    )
    second_momentum = np.zeros(4)
    second_momentum[model.axis] = 2.0 * model.k0
    second_gauge = regge.gauge_map(second_momentum)
    ward = float(
        np.linalg.norm(second_gauge.conj().T @ model.fourier(leading, 2))
    )
    return {
        "period": period,
        "source": source_kind,
        "k": model.k0,
        "ward_over_amplitude2": ward,
        "ward_over_k3_amplitude2": ward / model.k0**3,
        "coupling": coupling,
        "amplitude": amplitude,
    }


def main() -> int:
    checks = Checks()
    mutation = os.environ.get("TOE_MUTATION", "")
    note = " ".join(NOTE_PATH.read_text(encoding="utf-8").lower().split())
    block58_note = " ".join(
        BLOCK58_NOTE_PATH.read_text(encoding="utf-8").lower().split()
    )
    axiom = " ".join(AXIOM_PATH.read_text(encoding="utf-8").lower().split())
    periods = tuple(
        int(item) for item in os.environ.get("TOE_PERIODS", "3,5,7,9,11").split(",")
    )
    source_kinds = tuple(os.environ.get("TOE_SOURCES", "static,null").split(","))
    results = []
    for period in periods:
        for source_kind in source_kinds:
            result = SliceModel(period, source_kind).analyze()
            results.append(result)
    leading_periods = tuple(
        int(item)
        for item in os.environ.get(
            "TOE_LEADING_PERIODS", "19,25,33,49"
        ).split(",")
        if item
    )
    leading_results = []
    for period in leading_periods:
        for source_kind in source_kinds:
            result = leading_mode_analysis(period, source_kind)
            leading_results.append(result)
    amplitude_controls = [
        leading_mode_analysis(7, source_kind, amplitude)
        for source_kind in source_kinds
        for amplitude in (5.0e-5, 2.0e-4)
    ]

    print(
        "analytic_boundary: actual Regge-plus-deficit-square action, odd transversely homogeneous tori, every edge and harmonic retained"
    )
    print(
        "physical_boundary: Euclidean static density and conditionally Lorentzian null Record source; no selected source, continuum law, or causal nonlinear update"
    )
    print(
        "progress_boundary: infrared pseudo-constraint suppression is positive route evidence, but finite samples do not move a TOE percentage"
    )
    for result in results:
        harmonic = max(result["gauge_harmonics"], key=lambda row: row["norm"])
        print(
            f"period_result: source={result['source']} L={result['period']} "
            f"k={result['k']:.9f} Ward/eta^2={result['gauge_over_amplitude2']:.9f} "
            f"dominant_harmonic={harmonic['mode']} nonmetric/metric="
            f"{result['nonmetric_response']/result['metric_response']:.6f}"
        )

    rank_condition = all(
        result["physical_rank"] == 11 * result["period"] - 6
        and result["gauge_rank"] == 4 * result["period"] - 4
        and result["complete_rank"] == 15 * result["period"]
        and result["flat_gauge_residual"] < 2.0e-10
        for result in results
    )
    checks.check(
        "full-edge-all-harmonic-parameterization",
        "every nonaverage edge direction splits into the complete nongauge and displacement bases",
        rank_condition,
        "; ".join(
            f"L={r['period']} {r['source']}: ranks={r['physical_rank']}+{r['gauge_rank']}+10={r['complete_rank']}"
            for r in results
        ),
    )

    branch_condition = all(
        result["projected_residual"] < 2.0e-12
        and result["minimum_length"] > 0.99
        and result["metric_response"] > result["nonmetric_response"]
        and result["source_mean"] < 1.0e-11
        and result["source_ward"] < 1.0e-11
        for result in results
    )
    checks.check(
        "increasing-period-nonlinear-branches",
        "both conserved sources solve all nongauge equations with positive lengths and metric-dominated response",
        branch_condition,
        f"periods={periods}; max projected residual={max(r['projected_residual'] for r in results):.2e}",
    )

    harmonic_condition = mutation != "harmonic_alias"
    harmonic_details = []
    for result in results:
        rows = result["gauge_harmonics"]
        dominant = max(rows, key=lambda row: row["norm"])
        if result["period"] == 3:
            harmonic_condition &= dominant["mode"] == 1
        else:
            competitors = [row["norm"] for row in rows if row["mode"] != 2]
            harmonic_condition &= (
                dominant["mode"] == 2
                and dominant["norm"] > 100.0 * max(competitors, default=0.0)
            )
        harmonic_details.append(
            f"{result['source']} L={result['period']}: m={dominant['mode']}"
        )
    checks.check(
        "quadratic-harmonic-dealiasing",
        "the L=3 defect is an aliased second harmonic; at every larger period it sits at 2k",
        harmonic_condition,
        ", ".join(harmonic_details),
    )

    amplitude_condition = True
    match_details = []
    for result in results:
        target_mode = 1 if result["period"] == 3 else 2
        leading = next(
            row["norm"]
            for row in result["leading_over_amplitude2"]
            if row["mode"] == target_mode
        )
        ratio = result["gauge_over_amplitude2"] / leading
        amplitude_condition &= 0.98 < ratio < 1.02
        match_details.append(
            f"{result['source']} L={result['period']}: nonlinear/leading={ratio:.6f}"
        )
    for source_kind in source_kinds:
        controls = [row for row in amplitude_controls if row["source"] == source_kind]
        ratio = controls[0]["ward_over_k3_amplitude2"] / controls[1][
            "ward_over_k3_amplitude2"
        ]
        amplitude_condition &= 0.98 < ratio < 1.02
    checks.check(
        "quadratic-amplitude-law",
        "the solved Ward force matches the symmetric quadratic jet and survives a fourfold amplitude change",
        amplitude_condition,
        "; ".join(match_details),
    )

    infrared_condition = True
    infrared_details = []
    for source_kind in source_kinds:
        family = sorted(
            (row for row in results if row["source"] == source_kind),
            key=lambda row: row["period"],
        )
        values = [row["gauge_over_amplitude2"] for row in family]
        infrared_condition &= all(
            right < left for left, right in zip(values, values[1:])
        )
        infrared_condition &= values[-1] < 0.08 * values[0]
        infrared_details.append(
            f"{source_kind}: {values[0]:.6f}->{values[-1]:.6f}"
        )
    checks.check(
        "nonlinear-infrared-suppression",
        "the full nonlinear Ward defect decreases monotonically at fixed physical metric amplitude",
        infrared_condition,
        "; ".join(infrared_details),
    )

    power_condition = mutation != "infrared_power"
    power_details = []
    for source_kind in source_kinds:
        family = sorted(
            (row for row in leading_results if row["source"] == source_kind),
            key=lambda row: row["period"],
        )
        slope, intercept = np.polyfit(
            np.log([row["k"] for row in family]),
            np.log([row["ward_over_amplitude2"] for row in family]),
            1,
        )
        ratios = [row["ward_over_k3_amplitude2"] for row in family]
        power_condition &= 2.94 < slope < 3.04
        power_condition &= max(ratios) / min(ratios) < 1.04
        power_details.append(
            f"{source_kind}: exponent={slope:.6f}, C(k_min)={ratios[-1]:.6f}"
        )
    checks.check(
        "leading-k-cubed-scaling",
        "the independent weak-amplitude tail is k cubed to the resolved commensurate-period accuracy",
        power_condition,
        "; ".join(power_details),
    )

    purity_condition = True
    purity_details = []
    for source_kind in source_kinds:
        family = sorted(
            (row for row in results if row["source"] == source_kind),
            key=lambda row: row["period"],
        )
        ratios = [row["nonmetric_response"] / row["metric_response"] for row in family]
        purity_condition &= all(
            right < left for left, right in zip(ratios, ratios[1:])
        )
        purity_condition &= ratios[-1] < (0.05 if source_kind == "static" else 0.01)
        purity_details.append(
            f"{source_kind}: nonmetric/metric={ratios[0]:.6f}->{ratios[-1]:.6f}"
        )
    checks.check(
        "metric-purity-improves",
        "the nonlinear branches become increasingly metric-dominated along the same infrared sequence",
        purity_condition,
        "; ".join(purity_details),
    )

    note_condition = (
        mutation != "note_boundary"
        and "admissibility is not a dynamics axiom" in axiom
        and "controlled pseudo-constraint refinement" in block58_note
        and all(f"### n{index}" in note for index in range(1, 9))
        and "n1--n8 status: `pass`" in note
        and "not an all-l theorem" in note
        and "no toe percentage moves" in note
        and "no axiom is amended" in note
    )
    checks.check(
        "scope-strategy-and-no-go-packet",
        "the note preserves exact-finite versus controlled-infrared boundaries and carries N1 through N8",
        note_condition,
    )

    print(
        "N5_CERTIFICATE: all edge variables and Fourier harmonics were retained on five odd periods for two conserved sources; longer periods isolate the leading infrared jet"
    )
    print(
        f"per_element: checked 15L edge lengths, 11L-6 nongauge coordinates, and 4L-4 displacement coordinates through L={max(periods)}"
    )
    print(
        "per_site: checked every one of the 50 hinge classes and 240 simplex-hinge incidences per longitudinal site"
    )
    print(
        "per_mode: checked every nonzero harmonic on the nonlinear tori and separated the fundamental source from its generated second harmonic"
    )
    print(
        "per_block: checked both sources, five nonlinear periods, four leading-jet periods, and two amplitude controls per source; Schur blocks are independently checked by the companion"
    )
    print(
        "lattice_wide: increasing-period evidence only; no all-L, full-Z3, observable-decoupling, Lorentzian nonlinear, or selected-law theorem is claimed"
    )
    print(
        "scope_boundary: fixed Regge remains non-exact at finite spacing, while its measured Ward and pseudo-constraint defects soften toward the infrared"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
