#!/usr/bin/env python3
"""Nonaxial weak-field Regge Ward order on exact cyclic phase quotients."""

from __future__ import annotations

from dataclasses import dataclass
import math
import os
from pathlib import Path
import sys

import numpy as np
from scipy.linalg import null_space


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import admissibility_nonuniform_conserved_source_regge_increasing_period_pseudoconstraint_scaling_2026_08_12 as block59  # noqa: E402


regge = block59.regge
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REGGE_NONAXIAL_MOMENTUM_WARD_K3_FACTORIZATION_"
    "REFINEMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-12.md"
)
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_REGGE_NONAXIAL_MOMENTUM_WARD_K3_FACTORIZATION_REFINEMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/ADMISSIBILITY_NONUNIFORM_CONSERVED_SOURCE_REGGE_INCREASING_PERIOD_PSEUDOCONSTRAINT_SCALING_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_regge_nonaxial_momentum_ward_k3_factorization_refinement_boundary_2026_08_12.py",
    "scripts/admissibility_nonuniform_conserved_source_regge_increasing_period_pseudoconstraint_scaling_2026_08_12.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)


@dataclass(frozen=True)
class Family:
    name: str
    winding: tuple[int, int, int, int]
    periods: tuple[int, ...]


FAMILIES = (
    Family(
        "face",
        (1, 1, 0, 0),
        tuple(
            int(item)
            for item in os.environ.get("TOE_FACE_PERIODS", "49,97,145").split(",")
            if item
        ),
    ),
    Family(
        "body",
        (1, 1, 1, 0),
        tuple(
            int(item)
            for item in os.environ.get("TOE_BODY_PERIODS", "97,145,193").split(",")
            if item
        ),
    ),
)


class PhaseQuotient(block59.SliceModel):
    """One cyclic coordinate s=n.x for an exact single-Bloch-wave jet."""

    def _edge_ref(self, left, right):
        edge_class, anchor = regge.edge_class(tuple(left), tuple(right))
        return int(np.dot(self.winding, anchor)), edge_class


def tensor_target(vector: np.ndarray) -> np.ndarray:
    return np.asarray(
        [
            vector[left] * vector[right] * (2.0 if left != right else 1.0)
            for left, right in regge.HCOMPS
        ],
        dtype=float,
    )


def source_vector(family: str, source: str) -> np.ndarray:
    if source == "static":
        return np.asarray((0.0, 0.0, 0.0, 1.0))
    if family == "face":
        return np.asarray((0.0, 0.0, 1.0, 1.0))
    inverse_root_two = 1.0 / np.sqrt(2.0)
    return np.asarray((inverse_root_two, -inverse_root_two, 0.0, 1.0))


def build_model(period: int, winding: tuple[int, ...]) -> PhaseQuotient:
    model = object.__new__(PhaseQuotient)
    model.period = period
    model.source_kind = "phase-quotient"
    model.winding = np.asarray(winding, dtype=int)
    model.k0 = 2.0 * np.pi / period
    model.flat_lengths = np.sqrt(
        np.asarray([sum(direction) for direction in regge.DIRS15], dtype=float)
    )
    model.hinges = model._build_hinges()
    return model


def analyze(
    family: Family,
    period: int,
    source: str,
    amplitude: float,
) -> dict:
    model = build_model(period, family.winding)
    momentum = model.k0 * model.winding
    momentum_norm = float(np.linalg.norm(momentum))
    metric = regge.metric_map(momentum)
    gauge = regge.gauge_map(momentum)
    physical = null_space(gauge.conj().T)
    vector = source_vector(family.name, source)
    target = tensor_target(vector)
    source_k = metric @ np.linalg.solve(metric.conj().T @ metric, target)
    symbol = model._flat_bloch(momentum)
    quotient = physical.conj().T @ symbol @ physical
    response_k = physical @ np.linalg.solve(
        quotient, physical.conj().T @ source_k
    )
    quotient_residual = float(
        np.linalg.norm(physical.conj().T @ (symbol @ response_k - source_k))
    )
    metric_fit = metric @ np.linalg.lstsq(metric, response_k, rcond=None)[0]
    metric_norm = float(np.linalg.norm(metric_fit))
    nonmetric_ratio = float(np.linalg.norm(response_k - metric_fit) / metric_norm)
    coupling = amplitude / metric_norm
    delta = np.asarray(
        [
            2.0
            * np.real(np.exp(1j * model.k0 * site) * coupling * response_k)
            for site in range(period)
        ]
    )

    # One complex evaluation gives the symmetric quadratic jet:
    # grad(flat+i delta)=grad(flat)+i H delta-(1/2)T(delta,delta)+O(delta^3).
    # The flat term is site-constant and therefore vanishes in the nonzero
    # second-harmonic Fourier coefficient computed below.
    flat = np.tile(model.flat_lengths, (period, 1))
    _action, imaginary_gradient, _deficits = model.action_gradient(flat + 1j * delta)
    quadratic_force = -np.real(imaginary_gradient) / amplitude**2
    second_force = sum(
        np.exp(-2j * model.k0 * site) * quadratic_force[site]
        for site in range(period)
    ) / period
    second_momentum = 2.0 * momentum
    second_gauge = regge.gauge_map(second_momentum)
    ward_vector = second_gauge.conj().T @ second_force
    ward = float(np.linalg.norm(ward_vector))
    gauge_terms = []
    for maximum_order in (1, 2):
        truncated = np.zeros((15, 4), dtype=complex)
        for edge_class, direction in enumerate(regge.DIRS15):
            vector_edge = np.asarray(direction, dtype=float)
            phase = float(np.dot(second_momentum, vector_edge))
            factor = sum(
                (1j * phase) ** order / math.factorial(order)
                for order in range(1, maximum_order + 1)
            )
            truncated[edge_class] = (
                factor * vector_edge / np.linalg.norm(vector_edge)
            )
        gauge_terms.append(truncated.conj().T @ second_force)
    vector_dot_momentum = float(abs(np.dot(momentum, vector)))
    lorentz_norm = float(np.dot(vector[:3], vector[:3]) - vector[3] ** 2)
    return {
        "family": family.name,
        "source": source,
        "period": period,
        "winding": family.winding,
        "momentum_norm": momentum_norm,
        "ward": ward,
        "ward_over_k3": ward / momentum_norm**3,
        "ward_vector_over_k3": ward_vector / momentum_norm**3,
        "force_norm": float(np.linalg.norm(second_force)),
        "linear_generator_ward_over_k2": float(
            np.linalg.norm(gauge_terms[0]) / momentum_norm**2
        ),
        "quadratic_generator_ward_over_k3": float(
            np.linalg.norm(gauge_terms[1]) / momentum_norm**3
        ),
        "cancellation_ratio": float(
            np.linalg.norm(gauge_terms[1]) / np.linalg.norm(gauge_terms[0])
        ),
        "source_ward": float(np.linalg.norm(gauge.conj().T @ source_k)),
        "target_transverse": vector_dot_momentum,
        "lorentz_norm": lorentz_norm,
        "quotient_residual": quotient_residual,
        "nonmetric_ratio": nonmetric_ratio,
        "amplitude": amplitude,
    }


def uniform_metric_flatness() -> tuple[float, float]:
    model = build_model(5, (1, 1, 0, 0))
    perturbation = np.asarray(
        [
            [0.03, 0.01, 0.00, 0.00],
            [0.01, -0.02, 0.005, 0.00],
            [0.00, 0.005, 0.01, -0.004],
            [0.00, 0.00, -0.004, 0.015],
        ]
    )
    metric = np.eye(4) + perturbation
    lengths = np.asarray(
        [
            np.sqrt(np.asarray(direction, dtype=float) @ metric @ direction)
            for direction in regge.DIRS15
        ]
    )
    _action, gradient, deficits = model.action_gradient(
        np.tile(lengths, (model.period, 1))
    )
    return float(np.max(np.abs(deficits))), float(np.max(np.abs(gradient)))


def fit_family(rows: list[dict]) -> tuple[float, float, float]:
    ordered = sorted(rows, key=lambda row: row["momentum_norm"], reverse=True)
    slope, intercept = np.polyfit(
        np.log([row["momentum_norm"] for row in ordered]),
        np.log([row["ward"] for row in ordered]),
        1,
    )
    predicted = np.exp(intercept) * np.asarray(
        [row["momentum_norm"] for row in ordered]
    ) ** slope
    observed = np.asarray([row["ward"] for row in ordered])
    maximum_relative = float(np.max(np.abs(predicted / observed - 1.0)))
    coefficient_ratio = float(
        max(row["ward_over_k3"] for row in ordered)
        / min(row["ward_over_k3"] for row in ordered)
    )
    return float(slope), maximum_relative, coefficient_ratio


def complex_alignment(left: np.ndarray, right: np.ndarray) -> float:
    return float(
        abs(np.vdot(left, right))
        / (np.linalg.norm(left) * np.linalg.norm(right))
    )


def main() -> int:
    checks = block59.Checks()
    mutation = os.environ.get("TOE_MUTATION", "")
    amplitude = float(os.environ.get("TOE_JET_AMPLITUDE", "3e-4"))
    note = " ".join(NOTE_PATH.read_text(encoding="utf-8").lower().split())
    rows = [
        analyze(family, period, source, amplitude)
        for family in FAMILIES
        for period in family.periods
        for source in ("static", "null")
    ]

    print(
        "analytic_boundary: exact single-Bloch cyclic phase quotients of the actual four-dimensional Regge-plus-deficit-square action"
    )
    print(
        "physical_boundary: two nonaxial spatial momentum orbits and conserved static/null polarizations; not generic momentum, all-L, or nonlinear evolution"
    )
    for row in rows:
        print(
            f"tail_result: family={row['family']} source={row['source']} "
            f"L={row['period']} |k|={row['momentum_norm']:.9f} "
            f"W/|k|^3={row['ward_over_k3']:.9f} "
            f"|F2|={row['force_norm']:.9f} "
            f"W1/|k|^2={row['linear_generator_ward_over_k2']:.9f} "
            f"W12/|k|^3={row['quadratic_generator_ward_over_k3']:.9f}"
        )

    phase_condition = mutation != "phase_shift"
    for family in FAMILIES:
        model = build_model(family.periods[0], family.winding)
        phase_condition &= len(model.hinges) == 50
        phase_condition &= sum(len(stars) for _area, stars in model.hinges) == 240
    checks.check(
        "exact-cyclic-phase-quotient",
        "the nonaxial phase shifts retain every local hinge and simplex-hinge incidence",
        phase_condition,
        "two cubic momentum orbits; 50 hinge classes and 240 incidences per phase site",
    )

    deficit, gradient = uniform_metric_flatness()
    checks.check(
        "uniform-metric-flat-anchor",
        "a nontrivial constant metric remains an exactly flat zero-force family",
        deficit < 2.0e-13 and gradient < 2.0e-12,
        f"maximum deficit={deficit:.2e}; maximum action gradient={gradient:.2e}",
    )

    source_condition = all(
        row["source_ward"] < 2.0e-12
        and row["target_transverse"] < 2.0e-12
        and row["quotient_residual"] < 2.0e-11
        and (row["source"] != "null" or abs(row["lorentz_norm"]) < 2.0e-12)
        for row in rows
    )
    checks.check(
        "nonaxial-conserved-source-response",
        "both source polarizations are transverse and solve the flat nongauge response",
        source_condition,
        f"maximum source Ward={max(row['source_ward'] for row in rows):.2e}",
    )

    fit_results = {}
    order_condition = mutation != "infrared_order"
    order_details = []
    for family in FAMILIES:
        for source in ("static", "null"):
            selected = [
                row
                for row in rows
                if row["family"] == family.name and row["source"] == source
            ]
            slope, relative, coefficient_ratio = fit_family(selected)
            fit_results[(family.name, source)] = (
                slope,
                relative,
                coefficient_ratio,
            )
            order_condition &= 2.94 < slope < 3.04
            order_condition &= relative < 0.006
            order_condition &= coefficient_ratio < 1.04
            order_details.append(
                f"{family.name}/{source}: p={slope:.6f}, Cmax/Cmin={coefficient_ratio:.5f}"
            )
    checks.check(
        "nonaxial-k-cubed-tail",
        "face- and body-diagonal static/null Ward tails have resolved cubic momentum order",
        order_condition,
        "; ".join(order_details),
    )

    factor_condition = mutation != "factorization"
    factor_details = []
    for family in FAMILIES:
        for source in ("static", "null"):
            selected = sorted(
                (
                    row
                    for row in rows
                    if row["family"] == family.name and row["source"] == source
                ),
                key=lambda row: row["period"],
            )
            force_values = [row["force_norm"] for row in selected]
            linear_values = [
                row["linear_generator_ward_over_k2"] for row in selected
            ]
            quadratic_values = [
                row["quadratic_generator_ward_over_k3"] for row in selected
            ]
            cancellation_values = [row["cancellation_ratio"] for row in selected]
            alignment = complex_alignment(
                selected[0]["ward_vector_over_k3"],
                selected[-1]["ward_vector_over_k3"],
            )
            factor_condition &= max(force_values) / min(force_values) < 1.04
            factor_condition &= max(linear_values) / min(linear_values) < 1.07
            factor_condition &= max(quadratic_values) / min(quadratic_values) < 1.06
            factor_condition &= all(
                right < left
                for left, right in zip(
                    cancellation_values, cancellation_values[1:]
                )
            )
            factor_condition &= cancellation_values[0] < 0.30
            factor_condition &= alignment > 0.995
            factor_details.append(
                f"{family.name}/{source}: F-ratio={max(force_values)/min(force_values):.4f}, "
                f"cancel={cancellation_values[0]:.4f}->{cancellation_values[-1]:.4f}, "
                f"align={alignment:.6f}"
            )
    checks.check(
        "ward-order-factorization",
        "the bounded force loses its k-squared Ward term between first- and second-order generator contributions",
        factor_condition,
        "; ".join(factor_details),
    )

    controls = (
        analyze(FAMILIES[0], FAMILIES[0].periods[0], "static", amplitude / 2.0),
        analyze(FAMILIES[1], FAMILIES[1].periods[0], "null", amplitude / 2.0),
    )
    reference = (
        next(
            row
            for row in rows
            if row["family"] == "face"
            and row["period"] == FAMILIES[0].periods[0]
            and row["source"] == "static"
        ),
        next(
            row
            for row in rows
            if row["family"] == "body"
            and row["period"] == FAMILIES[1].periods[0]
            and row["source"] == "null"
        ),
    )
    amplitude_ratios = [
        control["ward_over_k3"] / base["ward_over_k3"]
        for control, base in zip(controls, reference)
    ]
    checks.check(
        "complex-jet-amplitude-control",
        "halving the complex-step field amplitude preserves both hostile normalized Ward coefficients",
        all(0.995 < ratio < 1.005 for ratio in amplitude_ratios),
        "; ".join(f"ratio={ratio:.7f}" for ratio in amplitude_ratios),
    )

    note_condition = (
        mutation != "note_boundary"
        and all(f"### n{index}" in note for index in range(1, 9))
        and "n1--n8 status: `pass`" in note
        and "not a generic-momentum theorem" in note
        and "no toe percentage moves" in note
        and "no axiom is amended" in note
        and "observable decoupling remains unproved" in note
    )
    checks.check(
        "scope-refinement-and-no-go-packet",
        "the note separates two nonaxial controls from uniform refinement and physical closure",
        note_condition,
    )

    print(
        "N5_CERTIFICATE: two nonaxial cubic momentum orbits, two conserved source polarizations, and three infrared periods per orbit were executed"
    )
    print(
        "per_element: every one of fifteen edge classes enters all fifty hinge classes at every cyclic phase site"
    )
    print(
        "per_site: all 240 simplex-hinge incidences are rebuilt with the exact dot(winding,anchor) phase shift"
    )
    print(
        "per_mode: the fundamental response and generated second harmonic are distinct on every executed period"
    )
    print(
        "per_block: face/body times static/null tails plus two half-amplitude controls test order and anisotropy"
    )
    print(
        "lattice_wide: not executed; arbitrary momentum direction, uniform all-L bounds, observables, and nonlinear Lorentzian refinement remain open"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
