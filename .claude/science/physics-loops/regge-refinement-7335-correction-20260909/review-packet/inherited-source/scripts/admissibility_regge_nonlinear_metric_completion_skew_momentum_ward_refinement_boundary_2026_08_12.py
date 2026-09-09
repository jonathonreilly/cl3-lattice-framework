#!/usr/bin/env python3
"""Nonlinear metric-length completion of the Regge quadratic Ward force."""

from __future__ import annotations

import os
from pathlib import Path
import sys

import numpy as np
from scipy.linalg import null_space


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import admissibility_nonuniform_conserved_source_regge_increasing_period_pseudoconstraint_scaling_2026_08_12 as block59  # noqa: E402
import admissibility_regge_nonaxial_momentum_ward_k3_factorization_refinement_boundary_2026_08_12 as block60  # noqa: E402


regge = block60.regge
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REGGE_NONLINEAR_METRIC_COMPLETION_SKEW_MOMENTUM_WARD_"
    "REFINEMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-12.md"
)
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_REGGE_NONLINEAR_METRIC_COMPLETION_SKEW_MOMENTUM_WARD_REFINEMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/ADMISSIBILITY_REGGE_NONAXIAL_MOMENTUM_WARD_K3_FACTORIZATION_REFINEMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/ADMISSIBILITY_NONUNIFORM_CONSERVED_SOURCE_REGGE_INCREASING_PERIOD_PSEUDOCONSTRAINT_SCALING_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_regge_nonlinear_metric_completion_skew_momentum_ward_refinement_boundary_2026_08_12.py",
    "scripts/admissibility_regge_nonaxial_momentum_ward_k3_factorization_refinement_boundary_2026_08_12.py",
    "scripts/admissibility_nonuniform_conserved_source_regge_increasing_period_pseudoconstraint_scaling_2026_08_12.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)


WINDING = (1, 2, 3, 0)
PERIODS = tuple(
    int(item)
    for item in os.environ.get("TOE_SKEW_PERIODS", "145,193,257").split(",")
    if item
)
AMPLITUDE = float(os.environ.get("TOE_JET_AMPLITUDE", "3e-4"))


def skew_source_vector(source: str) -> np.ndarray:
    if source == "static":
        return np.asarray((0.0, 0.0, 0.0, 1.0))
    inverse_root_five = 1.0 / np.sqrt(5.0)
    return np.asarray((2.0 * inverse_root_five, -inverse_root_five, 0.0, 1.0))


def prepare_period(period: int) -> dict:
    model = block60.build_model(period, WINDING)
    momentum = model.k0 * model.winding
    flat = np.tile(model.flat_lengths, (period, 1))
    _action, flat_gradient, _deficits = model.action_gradient(flat)
    return {
        "model": model,
        "momentum": momentum,
        "momentum_norm": float(np.linalg.norm(momentum)),
        "metric": regge.metric_map(momentum),
        "gauge": regge.gauge_map(momentum),
        "physical": null_space(regge.gauge_map(momentum).conj().T),
        "symbol": model._flat_bloch(momentum),
        "flat": flat,
        "flat_gradient": flat_gradient,
    }


def analyze_source(prepared: dict, source: str) -> dict:
    model = prepared["model"]
    momentum = prepared["momentum"]
    momentum_norm = prepared["momentum_norm"]
    metric = prepared["metric"]
    gauge = prepared["gauge"]
    physical = prepared["physical"]
    symbol = prepared["symbol"]
    target_vector = skew_source_vector(source)
    target = block60.tensor_target(target_vector)
    source_k = metric @ np.linalg.solve(metric.conj().T @ metric, target)
    response_k = physical @ np.linalg.solve(
        physical.conj().T @ symbol @ physical,
        physical.conj().T @ source_k,
    )
    metric_fit = metric @ np.linalg.lstsq(metric, response_k, rcond=None)[0]
    metric_norm = float(np.linalg.norm(metric_fit))
    coupling = AMPLITUDE / metric_norm
    response_mode = coupling * response_k
    metric_mode = coupling * metric_fit
    delta = np.asarray(
        [
            2.0 * np.real(np.exp(1j * model.k0 * site) * response_mode)
            for site in range(model.period)
        ]
    )
    _action, complex_gradient, _deficits = model.action_gradient(
        prepared["flat"] + 1j * delta
    )
    quadratic_force = (
        prepared["flat_gradient"] - np.real(complex_gradient)
    ) / AMPLITUDE**2
    raw_force = sum(
        np.exp(-2j * model.k0 * site) * quadratic_force[site]
        for site in range(model.period)
    ) / model.period

    # If q_e=ell_e^2 is linear in the line-averaged metric, then
    # sqrt(ell_e^2+dq_e)=ell_e+dq_e/(2ell_e)-dq_e^2/(8ell_e^3)+...
    # With first length coefficient d_e=dq_e/(2ell_e), the positive-2k
    # second-order coefficient is exactly -d_e^2/(2ell_e).
    metric_completion = -(
        metric_mode * metric_mode
    ) / (2.0 * model.flat_lengths * AMPLITUDE**2)
    second_momentum = 2.0 * momentum
    second_symbol = model._flat_bloch(second_momentum)
    reaction = second_symbol @ metric_completion
    completed_force = raw_force + reaction
    second_gauge = regge.gauge_map(second_momentum)
    raw_ward = second_gauge.conj().T @ raw_force
    completed_ward = second_gauge.conj().T @ completed_force
    reaction_ward = second_gauge.conj().T @ reaction
    return {
        "period": model.period,
        "source": source,
        "momentum_norm": momentum_norm,
        "raw_force": float(np.linalg.norm(raw_force)),
        "completed_force": float(np.linalg.norm(completed_force)),
        "completed_force_over_k2": float(
            np.linalg.norm(completed_force) / momentum_norm**2
        ),
        "completion_fraction": float(
            np.linalg.norm(completed_force) / np.linalg.norm(raw_force)
        ),
        "raw_ward": float(np.linalg.norm(raw_ward)),
        "completed_ward": float(np.linalg.norm(completed_ward)),
        "completed_ward_over_k3": float(
            np.linalg.norm(completed_ward) / momentum_norm**3
        ),
        "reaction_ward": float(np.linalg.norm(reaction_ward)),
        "ward_relative_change": float(
            np.linalg.norm(completed_ward - raw_ward)
            / np.linalg.norm(raw_ward)
        ),
        "source_ward": float(np.linalg.norm(gauge.conj().T @ source_k)),
        "target_transverse": float(abs(np.dot(momentum, target_vector))),
        "lorentz_norm": float(
            np.dot(target_vector[:3], target_vector[:3]) - target_vector[3] ** 2
        ),
        "quotient_residual": float(
            np.linalg.norm(
                physical.conj().T @ (symbol @ response_k - source_k)
            )
        ),
        "nonmetric_ratio": float(
            np.linalg.norm(response_k - metric_fit) / metric_norm
        ),
    }


def richardson_uniform_force(model, flat, flat_gradient, direction) -> np.ndarray:
    epsilon = 1.0e-3

    def raw(step: float) -> np.ndarray:
        field = np.tile(direction, (model.period, 1))
        _action, gradient, _deficits = model.action_gradient(flat + 1j * step * field)
        return np.mean(
            (flat_gradient - np.real(gradient)) / step**2,
            axis=0,
        )

    return (9.0 * raw(epsilon) - raw(3.0 * epsilon)) / 8.0


def uniform_metric_identity() -> dict:
    model = block60.build_model(3, (1, 1, 0, 0))
    flat = np.tile(model.flat_lengths, (model.period, 1))
    _action, flat_gradient, _deficits = model.action_gradient(flat)
    metric = regge.metric_map(np.zeros(4)).real
    symbol = model._flat_bloch(np.zeros(4)).real
    diagonal_forces = [
        richardson_uniform_force(model, flat, flat_gradient, metric[:, index])
        for index in range(10)
    ]
    forces = []
    reactions = []
    relative_residuals = []
    absolute_residuals = []
    for left in range(10):
        for right in range(left, 10):
            if left == right:
                force = diagonal_forces[left]
                completion = -metric[:, left] ** 2 / (2.0 * model.flat_lengths)
            else:
                force = (
                    richardson_uniform_force(
                        model,
                        flat,
                        flat_gradient,
                        metric[:, left] + metric[:, right],
                    )
                    - diagonal_forces[left]
                    - diagonal_forces[right]
                )
                completion = -(
                    metric[:, left] * metric[:, right]
                ) / model.flat_lengths
            reaction = symbol @ completion
            residual = force + reaction
            forces.append(force)
            reactions.append(reaction)
            absolute_residuals.append(float(np.linalg.norm(residual)))
            relative_residuals.append(
                float(np.linalg.norm(residual) / np.linalg.norm(force))
            )
    force_matrix = np.asarray(forces).T
    reaction_matrix = np.asarray(reactions).T
    return {
        "pairs": len(forces),
        "symbol_rank": int(np.linalg.matrix_rank(symbol, tol=1.0e-8)),
        "force_rank": int(np.linalg.matrix_rank(force_matrix, tol=1.0e-5)),
        "reaction_rank": int(
            np.linalg.matrix_rank(reaction_matrix, tol=1.0e-8)
        ),
        "maximum_relative_residual": max(relative_residuals),
        "maximum_absolute_residual": max(absolute_residuals),
    }


def fit_power(rows: list[dict], key: str) -> tuple[float, float, float]:
    ordered = sorted(rows, key=lambda row: row["momentum_norm"], reverse=True)
    momentum = np.asarray([row["momentum_norm"] for row in ordered])
    observed = np.asarray([row[key] for row in ordered])
    slope, intercept = np.polyfit(np.log(momentum), np.log(observed), 1)
    predicted = np.exp(intercept) * momentum**slope
    maximum_relative = float(np.max(np.abs(predicted / observed - 1.0)))
    normalized_power = 2 if key == "completed_force" else 3
    coefficients = observed / momentum**normalized_power
    return (
        float(slope),
        maximum_relative,
        float(np.max(coefficients) / np.min(coefficients)),
    )


def main() -> int:
    checks = block59.Checks()
    mutation = os.environ.get("TOE_MUTATION", "")
    note = " ".join(NOTE_PATH.read_text(encoding="utf-8").lower().split())
    uniform = uniform_metric_identity()
    rows = []
    for period in PERIODS:
        prepared = prepare_period(period)
        for source in ("static", "null"):
            rows.append(analyze_source(prepared, source))

    print(
        "analytic_boundary: exact second-order square-root metric embedding and one skew single-Bloch phase quotient of the actual Regge-plus-deficit-square action"
    )
    print(
        "physical_boundary: constant-metric ten-tangent identity plus winding (1,2,3,0) static/null controls; not a uniform angular, all-source, or nonlinear evolution theorem"
    )
    print(
        f"uniform_identity: pairs={uniform['pairs']} force/reaction/symbol ranks="
        f"{uniform['force_rank']}/{uniform['reaction_rank']}/{uniform['symbol_rank']} "
        f"max_relative={uniform['maximum_relative_residual']:.3e}"
    )
    for row in rows:
        print(
            f"completion_result: source={row['source']} L={row['period']} "
            f"|k|={row['momentum_norm']:.9f} "
            f"Fcompleted/|k|^2={row['completed_force_over_k2']:.9f} "
            f"W/|k|^3={row['completed_ward_over_k3']:.9f} "
            f"completed/raw={row['completion_fraction']:.6f}"
        )

    uniform_condition = mutation != "uniform_identity"
    uniform_condition &= uniform["pairs"] == 55
    uniform_condition &= uniform["symbol_rank"] == 5
    uniform_condition &= uniform["force_rank"] == 5
    uniform_condition &= uniform["reaction_rank"] == 5
    uniform_condition &= uniform["maximum_relative_residual"] < 2.0e-6
    checks.check(
        "complete-uniform-metric-second-jet",
        "all 55 symmetric metric-tangent pairs cancel against the square-root completion reaction",
        uniform_condition,
        f"ranks={uniform['force_rank']}/{uniform['reaction_rank']}/{uniform['symbol_rank']}; "
        f"max relative={uniform['maximum_relative_residual']:.3e}",
    )

    source_condition = all(
        row["source_ward"] < 2.0e-12
        and row["target_transverse"] < 2.0e-12
        and row["quotient_residual"] < 2.0e-11
        and (row["source"] != "null" or abs(row["lorentz_norm"]) < 2.0e-12)
        for row in rows
    )
    checks.check(
        "skew-conserved-source-response",
        "the less-symmetric static and Lorentz-null sources are transverse and solve the full nongauge quotient",
        source_condition,
        f"maximum source Ward={max(row['source_ward'] for row in rows):.2e}",
    )

    completion_condition = mutation != "metric_completion"
    for source in ("static", "null"):
        selected = sorted(
            (row for row in rows if row["source"] == source),
            key=lambda row: row["period"],
        )
        fractions = [row["completion_fraction"] for row in selected]
        completion_condition &= all(
            right < left for left, right in zip(fractions, fractions[1:])
        )
        completion_condition &= fractions[0] < 0.05
        completion_condition &= fractions[-1] < 0.02
    checks.check(
        "nonlinear-metric-completion-removes-reaction",
        "the square-root completion removes the bounded reaction and leaves a vanishing skew force fraction",
        completion_condition,
        "; ".join(
            f"{source}: {next(row for row in rows if row['source']==source and row['period']==PERIODS[0])['completion_fraction']:.5f}"
            f"->{next(row for row in rows if row['source']==source and row['period']==PERIODS[-1])['completion_fraction']:.5f}"
            for source in ("static", "null")
        ),
    )

    force_condition = mutation != "force_order"
    force_details = []
    for source in ("static", "null"):
        selected = [row for row in rows if row["source"] == source]
        slope, relative, spread = fit_power(selected, "completed_force")
        force_condition &= 1.94 < slope < 2.04
        force_condition &= relative < 0.003
        force_condition &= spread < 1.03
        force_details.append(
            f"{source}: p={slope:.6f}, Cmax/Cmin={spread:.5f}"
        )
    checks.check(
        "completed-force-k-squared-tail",
        "the reaction-subtracted force has resolved quadratic order on the skew family",
        force_condition,
        "; ".join(force_details),
    )

    ward_invariance = all(
        row["reaction_ward"] < 2.0e-12
        and row["ward_relative_change"] < 2.0e-10
        for row in rows
    )
    checks.check(
        "completion-is-Ward-null",
        "the flat-Hessian completion reaction changes no displacement Ward component",
        ward_invariance,
        f"maximum reaction Ward={max(row['reaction_ward'] for row in rows):.2e}",
    )

    ward_condition = mutation != "ward_order"
    ward_details = []
    for source in ("static", "null"):
        selected = [row for row in rows if row["source"] == source]
        slope, relative, spread = fit_power(selected, "completed_ward")
        ward_condition &= 2.94 < slope < 3.04
        ward_condition &= relative < 0.003
        ward_condition &= spread < 1.03
        ward_details.append(
            f"{source}: p={slope:.6f}, Cmax/Cmin={spread:.5f}"
        )
    checks.check(
        "skew-Ward-k-cubed-tail",
        "the unchanged skew Ward vector has resolved cubic order after nonlinear metric completion",
        ward_condition,
        "; ".join(ward_details),
    )

    purity_condition = True
    for source in ("static", "null"):
        selected = sorted(
            (row for row in rows if row["source"] == source),
            key=lambda row: row["period"],
        )
        values = [row["nonmetric_ratio"] for row in selected]
        purity_condition &= all(
            right < left for left, right in zip(values, values[1:])
        )
        purity_condition &= values[-1] < 0.002
    checks.check(
        "skew-response-metric-purity",
        "the same less-symmetric response approaches the nonlinear metric carrier",
        purity_condition,
        "; ".join(
            f"{source}: {next(row for row in rows if row['source']==source and row['period']==PERIODS[-1])['nonmetric_ratio']:.6f}"
            for source in ("static", "null")
        ),
    )

    note_condition = (
        mutation != "note_boundary"
        and all(f"### n{index}" in note for index in range(1, 9))
        and "n1--n8 status: `pass`" in note
        and "not a uniform angular theorem" in note
        and "observable decoupling remains unproved" in note
        and "no toe percentage moves" in note
        and "no axiom is amended" in note
    )
    checks.check(
        "scope-refinement-and-no-go-packet",
        "the note keeps the exact metric identity separate from uniform refinement and physical closure",
        note_condition,
    )

    print(
        "N5_CERTIFICATE: all 55 constant-metric tangent pairs and a three-period skew winding with two conserved sources were executed"
    )
    print(
        "per_element: all fifteen edge classes enter the square-root completion and every local action gradient"
    )
    print(
        "per_site: all fifty hinges and 240 simplex-hinge incidences enter every skew phase site"
    )
    print(
        "per_mode: fundamental response, generated second harmonic, Hessian reaction, and Ward projection are separately retained"
    )
    print(
        "per_block: ten metric tangents, 55 symmetric pairs, skew static/null tails, and reaction-null controls are checked"
    )
    print(
        "lattice_wide: not executed; a uniform angular/source theorem, multimode fields, observables, and nonlinear Lorentzian refinement remain open"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
