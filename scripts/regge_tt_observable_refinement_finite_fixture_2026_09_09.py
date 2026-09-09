#!/usr/bin/env python3
"""Finite L=5 Regge fixture extracted from the reviewed Block 59/62 closure.

Only definitions exercised by the TT lift/refinement theorem are retained.
The historical campaign modules remain byte-exact in the adjacent correction
archive and are not imported as current scientific authority.
"""
from __future__ import annotations

from dataclasses import dataclass
import itertools

import numpy as np
from scipy.linalg import null_space

import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as regge

ALPHA = 1.0 / 1024.0
EXTRACTION_PROVENANCE = {
    "slice_model_source": "scripts/admissibility_nonuniform_conserved_source_regge_increasing_period_pseudoconstraint_scaling_2026_08_12.py",
    "slice_model_sha256": "02ce6bdd92087f157a03ca2149ec749499084f47d3bb5a2d0eb8cf1abb2cd5ce",
    "batched_gradient_source": "scripts/admissibility_regge_full_conserved_source_multimode_metric_completion_ward_boundary_2026_08_12.py",
    "batched_gradient_sha256": "ae27903c9bc265aec87d31413583ee0e0d14ebdcc4f07e64e25c4bb138f58597",
    "regge_source": "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
    "regge_sha256": "537371554e1a5244875645ca600f5f01e0ccfae64530572630d934e8ea0a85ce",
}


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


def batched_action_gradient(model, lengths: np.ndarray) -> np.ndarray:
    """Vectorized action gradient for fields shaped (batch, period, 15)."""

    lengths = np.asarray(lengths)
    batch, period, edge_count = lengths.shape
    if period != model.period or edge_count != 15:
        raise ValueError("unexpected batched field shape")
    dtype = np.result_type(lengths.dtype, np.float64)
    gradient = np.zeros((batch, period, 15), dtype=dtype)

    def values(base: int, references) -> np.ndarray:
        return np.stack(
            [
                lengths[:, (base + shift) % period, edge_class]
                for shift, edge_class in references
            ],
            axis=1,
        )

    for base in range(period):
        for area_refs, stars in model.hinges:
            area_lengths = values(base, area_refs)
            area_out = regge.AREA(
                *(area_lengths[:, index] ** 2 for index in range(3))
            )
            area = np.asarray(area_out[0])
            area_derivatives = 2.0 * area_lengths * np.stack(
                [np.asarray(item) for item in area_out[1:]], axis=1
            )
            deficit = np.full(batch, 2.0 * np.pi, dtype=dtype)
            derivative_terms = []
            for missing, refs in stars:
                simplex_lengths = values(base, refs)
                angle_out = regge.THETA[missing](
                    *(simplex_lengths[:, index] ** 2 for index in range(10))
                )
                deficit -= np.asarray(angle_out[0])
                derivatives = -2.0 * simplex_lengths * np.stack(
                    [np.asarray(item) for item in angle_out[1:]], axis=1
                )
                for reference, derivative in zip(refs, derivatives.T):
                    derivative_terms.append((reference, derivative))
            weight = deficit + ALPHA * deficit * deficit
            for reference, derivative in zip(area_refs, area_derivatives.T):
                shift, edge_class = reference
                gradient[:, (base + shift) % period, edge_class] += (
                    derivative * weight
                )
            multiplier = area * (
                1.0 + 2.0 * ALPHA * deficit
            )
            for (shift, edge_class), derivative in derivative_terms:
                gradient[:, (base + shift) % period, edge_class] += (
                    multiplier * derivative
                )
    return gradient
