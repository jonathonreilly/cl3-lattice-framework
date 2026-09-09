#!/usr/bin/env python3
"""Full transverse-source and unequal-harmonic Regge Ward tensors."""

from __future__ import annotations

import os
from pathlib import Path
import sys
import time

import numpy as np
from scipy.linalg import null_space


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import admissibility_regge_nonlinear_metric_completion_skew_momentum_ward_refinement_boundary_2026_08_12 as block61  # noqa: E402


block60 = block61.block60
regge = block61.regge
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REGGE_FULL_CONSERVED_SOURCE_MULTIMODE_METRIC_COMPLETION_"
    "WARD_REFINEMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-12.md"
)
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_REGGE_FULL_CONSERVED_SOURCE_MULTIMODE_METRIC_COMPLETION_WARD_REFINEMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/ADMISSIBILITY_REGGE_NONLINEAR_METRIC_COMPLETION_SKEW_MOMENTUM_WARD_REFINEMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/ADMISSIBILITY_REGGE_NONAXIAL_MOMENTUM_WARD_K3_FACTORIZATION_REFINEMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_regge_full_conserved_source_multimode_metric_completion_ward_boundary_2026_08_12.py",
    "scripts/admissibility_regge_nonlinear_metric_completion_skew_momentum_ward_refinement_boundary_2026_08_12.py",
    "scripts/admissibility_regge_nonaxial_momentum_ward_k3_factorization_refinement_boundary_2026_08_12.py",
    "scripts/admissibility_nonuniform_conserved_source_regge_increasing_period_pseudoconstraint_scaling_2026_08_12.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)
AUDIT_TIMEOUT_SEC = 480
WINDING = np.asarray((1, 2, 3, 0), dtype=int)
AMPLITUDE = float(os.environ.get("TOE_JET_AMPLITUDE", "3e-4"))
PERIODS = tuple(
    int(item)
    for item in os.environ.get("TOE_FULL_SOURCE_PERIODS", "145,193,257").split(",")
    if item
)


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
            weight = deficit + block61.block59.ALPHA * deficit * deficit
            for reference, derivative in zip(area_refs, area_derivatives.T):
                shift, edge_class = reference
                gradient[:, (base + shift) % period, edge_class] += (
                    derivative * weight
                )
            multiplier = area * (
                1.0 + 2.0 * block61.block59.ALPHA * deficit
            )
            for (shift, edge_class), derivative in derivative_terms:
                gradient[:, (base + shift) % period, edge_class] += (
                    multiplier * derivative
                )
    return gradient


def transverse_tensor_basis(momentum: np.ndarray) -> np.ndarray:
    """Six Frobenius-orthonormal symmetric tensors transverse to momentum."""

    transverse = null_space(momentum.reshape(1, 4))
    columns = []
    for left in range(3):
        for right in range(left, 3):
            tensor = np.outer(transverse[:, left], transverse[:, right])
            if left != right:
                tensor = (tensor + tensor.T) / np.sqrt(2.0)
            target = np.asarray(
                [
                    tensor[a, b] * (2.0 if a != b else 1.0)
                    for a, b in regge.HCOMPS
                ]
            )
            columns.append(target)
    return np.stack(columns, axis=1)


def response_basis(model, harmonic: int) -> dict:
    momentum = harmonic * model.k0 * WINDING
    metric = regge.metric_map(momentum)
    gauge = regge.gauge_map(momentum)
    physical = null_space(gauge.conj().T)
    target_basis = transverse_tensor_basis(momentum)
    source_edges = metric @ np.linalg.solve(
        metric.conj().T @ metric, target_basis
    )
    symbol = model._flat_bloch(momentum)
    responses = physical @ np.linalg.solve(
        physical.conj().T @ symbol @ physical,
        physical.conj().T @ source_edges,
    )
    metric_fits = metric @ np.linalg.lstsq(metric, responses, rcond=None)[0]
    orthonormal_metric, transform = np.linalg.qr(metric_fits, mode="reduced")
    inverse_transform = np.linalg.inv(transform)
    responses = responses @ inverse_transform
    source_edges = source_edges @ inverse_transform
    transformed_targets = target_basis @ inverse_transform
    target_singular_values = np.linalg.svd(
        transformed_targets, compute_uv=False
    )
    return {
        "momentum": momentum,
        "metric": metric,
        "gauge": gauge,
        "symbol": symbol,
        "responses": responses,
        "metric_fits": orthonormal_metric,
        "source_edges": source_edges,
        "source_ward": float(np.linalg.norm(gauge.conj().T @ source_edges)),
        "orthonormal_error": float(
            np.linalg.norm(orthonormal_metric.conj().T @ orthonormal_metric - np.eye(6))
        ),
        "response_residual": float(
            np.linalg.norm(
                physical.conj().T @ (symbol @ responses - source_edges)
            )
        ),
        "target_rank": int(np.linalg.matrix_rank(target_basis, tol=1.0e-12)),
        "response_rank": int(np.linalg.matrix_rank(responses, tol=1.0e-10)),
        "source_basis_condition": float(
            target_singular_values[0] / target_singular_values[-1]
        ),
        "source_basis_minimum": float(target_singular_values[-1]),
        "source_basis_maximum": float(target_singular_values[0]),
        "source_basis_scaled_minimum": float(
            target_singular_values[-1] / np.linalg.norm(momentum) ** 2
        ),
        "source_basis_scaled_maximum": float(
            target_singular_values[0] / np.linalg.norm(momentum) ** 2
        ),
    }


def real_fields(model, modes: np.ndarray, harmonic: int) -> np.ndarray:
    phases = np.exp(
        1j * harmonic * model.k0 * np.arange(model.period)
    )
    return 2.0 * np.real(
        phases[None, :, None] * modes.T[:, None, :]
    )


def fourier(model, fields: np.ndarray, harmonic: int) -> np.ndarray:
    phases = np.exp(-1j * harmonic * model.k0 * np.arange(model.period))
    return np.einsum("s,bse->be", phases, fields) / model.period


def quadratic_samples(model, fields: np.ndarray) -> np.ndarray:
    flat = np.tile(model.flat_lengths, (model.period, 1))
    flat_batch = np.broadcast_to(flat, fields.shape)
    gradients = batched_action_gradient(
        model, flat_batch + 1j * AMPLITUDE * fields
    )
    _action, flat_gradient, _deficits = model.action_gradient(flat)
    return (
        flat_gradient[None, :, :] - np.real(gradients)
    ) / AMPLITUDE**2


def symmetric_source_fields(model, basis: dict) -> tuple[np.ndarray, list[tuple[int, int]]]:
    unit_fields = real_fields(model, basis["responses"], 1)
    sample_fields = []
    labels = []
    for left in range(6):
        for right in range(left, 6):
            labels.append((left, right))
            if left == right:
                sample_fields.append(unit_fields[left])
            else:
                sample_fields.append(unit_fields[left] + unit_fields[right])
    return np.asarray(sample_fields), labels


def symmetric_source_tensor(model, basis: dict, forces: np.ndarray, labels) -> dict:
    raw = np.zeros((15, 6, 6), dtype=complex)
    sampled = dict(zip(labels, forces))
    diagonal = {index: sampled[(index, index)] for index in range(6)}
    for (left, right), force in zip(labels, forces):
        if left == right:
            raw[:, left, right] = force
        else:
            value = 0.5 * (force - diagonal[left] - diagonal[right])
            raw[:, left, right] = value
            raw[:, right, left] = value
    metric_modes = basis["metric_fits"]
    completion = np.zeros_like(raw)
    for left in range(6):
        for right in range(6):
            completion[:, left, right] = -(
                metric_modes[:, left] * metric_modes[:, right]
            ) / (2.0 * model.flat_lengths)
    output_momentum = 2.0 * basis["momentum"]
    symbol = model._flat_bloch(output_momentum)
    reaction = np.einsum("ef,fij->eij", symbol, completion)
    completed = raw + reaction
    gauge = regge.gauge_map(output_momentum)
    ward = np.einsum("ae,aij->eij", gauge.conj(), completed)
    reaction_ward = np.einsum("ae,aij->eij", gauge.conj(), reaction)
    return {
        "pair_count": 21,
        "raw": float(np.linalg.norm(raw)),
        "completed": float(np.linalg.norm(completed)),
        "ward": float(np.linalg.norm(ward)),
        "reaction_ward": float(np.linalg.norm(reaction_ward)),
        "completed_fraction": float(np.linalg.norm(completed) / np.linalg.norm(raw)),
    }


def unequal_harmonic_fields(model, first: dict, second: dict) -> np.ndarray:
    first_fields = real_fields(model, first["responses"], 1)
    second_fields = real_fields(model, second["responses"], 2)
    return np.asarray(
        [
            first_fields[left] + second_fields[right]
            for left in range(6)
            for right in range(6)
        ]
    )


def unequal_harmonic_tensor(
    model, first: dict, second: dict, raw_samples: np.ndarray
) -> dict:
    raw = 0.5 * raw_samples.reshape(6, 6, 15).transpose(2, 0, 1)
    completion = np.zeros_like(raw)
    for left in range(6):
        for right in range(6):
            completion[:, left, right] = -(
                first["metric_fits"][:, left]
                * second["metric_fits"][:, right]
            ) / (2.0 * model.flat_lengths)
    output_momentum = first["momentum"] + second["momentum"]
    symbol = model._flat_bloch(output_momentum)
    reaction = np.einsum("ef,fij->eij", symbol, completion)
    completed = raw + reaction
    gauge = regge.gauge_map(output_momentum)
    ward = np.einsum("ae,aij->eij", gauge.conj(), completed)
    reaction_ward = np.einsum("ae,aij->eij", gauge.conj(), reaction)
    return {
        "pair_count": 36,
        "raw": float(np.linalg.norm(raw)),
        "completed": float(np.linalg.norm(completed)),
        "ward": float(np.linalg.norm(ward)),
        "reaction_ward": float(np.linalg.norm(reaction_ward)),
        "completed_fraction": float(np.linalg.norm(completed) / np.linalg.norm(raw)),
    }


def analyze(period: int) -> dict:
    started = time.perf_counter()
    model = block60.build_model(period, tuple(WINDING))
    first = response_basis(model, 1)
    second = response_basis(model, 2)
    equal_fields, equal_labels = symmetric_source_fields(model, first)
    unequal_fields = unequal_harmonic_fields(model, first, second)
    samples = quadratic_samples(
        model, np.concatenate((equal_fields, unequal_fields), axis=0)
    )
    equal_count = len(equal_fields)
    equal = symmetric_source_tensor(
        model,
        first,
        fourier(model, samples[:equal_count], 2),
        equal_labels,
    )
    unequal = unequal_harmonic_tensor(
        model,
        first,
        second,
        fourier(model, samples[equal_count:], 3),
    )
    k_norm = float(np.linalg.norm(first["momentum"]))
    return {
        "period": period,
        "k": k_norm,
        "source_ward": max(first["source_ward"], second["source_ward"]),
        "orthonormal_error": max(
            first["orthonormal_error"], second["orthonormal_error"]
        ),
        "response_residual": max(
            first["response_residual"], second["response_residual"]
        ),
        "target_rank": min(first["target_rank"], second["target_rank"]),
        "response_rank": min(first["response_rank"], second["response_rank"]),
        "source_basis_condition": max(
            first["source_basis_condition"], second["source_basis_condition"]
        ),
        "source_basis_minimum": min(
            first["source_basis_minimum"], second["source_basis_minimum"]
        ),
        "source_basis_maximum": max(
            first["source_basis_maximum"], second["source_basis_maximum"]
        ),
        "source_basis_scaled_minimum": min(
            first["source_basis_scaled_minimum"],
            second["source_basis_scaled_minimum"],
        ),
        "source_basis_scaled_maximum": max(
            first["source_basis_scaled_maximum"],
            second["source_basis_scaled_maximum"],
        ),
        "equal": equal,
        "unequal": unequal,
        "seconds": time.perf_counter() - started,
    }


def fit_power(rows: list[dict], family: str, key: str, normalized_power: int) -> dict:
    momentum = np.asarray([row["k"] for row in rows])
    observed = np.asarray([row[family][key] for row in rows])
    slope, intercept = np.polyfit(np.log(momentum), np.log(observed), 1)
    predicted = np.exp(intercept) * momentum**slope
    coefficients = observed / momentum**normalized_power
    return {
        "slope": float(slope),
        "maximum_relative": float(np.max(np.abs(predicted / observed - 1.0))),
        "coefficient_spread": float(np.max(coefficients) / np.min(coefficients)),
    }


def gradient_batch_equivalence() -> tuple[float, float]:
    model = block60.build_model(5, tuple(WINDING))
    flat = np.tile(model.flat_lengths, (model.period, 1))
    direction = np.asarray(
        [
            np.cos(model.k0 * site)
            * np.linspace(-0.7, 0.8, 15)
            for site in range(model.period)
        ]
    )
    lengths = flat + 1j * 1.0e-4 * direction
    _action, scalar_gradient, _deficits = model.action_gradient(lengths)
    batch_gradient = batched_action_gradient(model, lengths[None, :, :])[0]
    difference = scalar_gradient - batch_gradient
    return (
        float(np.max(np.abs(difference))),
        float(np.linalg.norm(difference) / np.linalg.norm(scalar_gradient)),
    )


def amplitude_control() -> tuple[float, float]:
    model = block60.build_model(49, tuple(WINDING))
    first = response_basis(model, 1)
    second = response_basis(model, 2)
    first_field = real_fields(model, first["responses"][:, :1], 1)[0]
    second_field = real_fields(model, second["responses"][:, :1], 2)[0]
    fields = np.asarray(
        [
            first_field,
            first_field + second_field,
            0.5 * first_field,
            0.5 * (first_field + second_field),
        ]
    )
    samples = quadratic_samples(model, fields)
    equal_full = fourier(model, samples[0:1], 2)[0]
    equal_half = 4.0 * fourier(model, samples[2:3], 2)[0]
    cross_full = fourier(model, samples[1:2], 3)[0]
    cross_half = 4.0 * fourier(model, samples[3:4], 3)[0]
    return (
        float(np.linalg.norm(equal_half - equal_full) / np.linalg.norm(equal_full)),
        float(np.linalg.norm(cross_half - cross_full) / np.linalg.norm(cross_full)),
    )


def main() -> int:
    checks = block61.block59.Checks()
    mutation = os.environ.get("TOE_MUTATION", "")
    note = " ".join(NOTE_PATH.read_text(encoding="utf-8").lower().split())
    batch_absolute, batch_relative = gradient_batch_equivalence()
    rows = [analyze(period) for period in PERIODS]
    equal_force = fit_power(rows, "equal", "completed", 2)
    equal_ward = fit_power(rows, "equal", "ward", 3)
    unequal_force = fit_power(rows, "unequal", "completed", 2)
    unequal_ward = fit_power(rows, "unequal", "ward", 3)
    amplitude_equal, amplitude_cross = amplitude_control()

    print(
        "analytic_boundary: complete six-dimensional transverse source bases at k and 2k, response-normalized with an explicit invertible physical-source Gram map, plus all 21 equal-mode and 36 k-plus-2k bilinear pairs"
    )
    print(
        "physical_boundary: one skew collinear momentum ray and its first two harmonics; not a uniform angular, noncollinear-mode, observable, or nonlinear evolution theorem"
    )
    print(
        f"batch_equivalence: absolute={batch_absolute:.3e} relative={batch_relative:.3e}"
    )
    for row in rows:
        print(
            f"tensor_result: L={row['period']} k={row['k']:.9f} "
            f"sourceWard={row['source_ward']:.2e} "
            f"orth={row['orthonormal_error']:.2e} residual={row['response_residual']:.2e} "
            f"sourceCond={row['source_basis_condition']:.6f} "
            f"sourceScaled=[{row['source_basis_scaled_minimum']:.6f},{row['source_basis_scaled_maximum']:.6f}] "
            f"equal F/k2={row['equal']['completed']/row['k']**2:.9f} "
            f"W/k3={row['equal']['ward']/row['k']**3:.9f} "
            f"frac={row['equal']['completed_fraction']:.6f} "
            f"cross F/k2={row['unequal']['completed']/row['k']**2:.9f} "
            f"W/k3={row['unequal']['ward']/row['k']**3:.9f} "
            f"frac={row['unequal']['completed_fraction']:.6f} "
            f"reactionWard={max(row['equal']['reaction_ward'], row['unequal']['reaction_ward']):.2e} "
            f"seconds={row['seconds']:.1f}"
        )
    print(
        f"tensor_fits: equal force={equal_force['slope']:.9f} Ward={equal_ward['slope']:.9f}; "
        f"unequal force={unequal_force['slope']:.9f} Ward={unequal_ward['slope']:.9f}"
    )
    print(
        f"amplitude_control: equal_relative={amplitude_equal:.3e} cross_relative={amplitude_cross:.3e}"
    )

    batch_condition = mutation != "batch_gradient"
    batch_condition &= batch_absolute < 5.0e-13
    batch_condition &= batch_relative < 5.0e-9
    checks.check(
        "vectorized-action-gradient-equivalence",
        "the batched full-tensor evaluator reproduces the retained scalar local-action gradient",
        batch_condition,
        f"absolute={batch_absolute:.3e}; relative={batch_relative:.3e}",
    )

    source_condition = mutation != "source_basis"
    source_condition &= all(
        row["target_rank"] == 6
        and row["response_rank"] == 6
        and row["source_ward"] < 2.0e-12
        and row["orthonormal_error"] < 2.0e-12
        and row["response_residual"] < 2.0e-11
        and row["source_basis_condition"] < 2.0
        and row["source_basis_scaled_minimum"] > 0.45
        and row["source_basis_scaled_maximum"] < 1.05
        for row in rows
    )
    checks.check(
        "complete-transverse-source-bases",
        "both unequal input harmonics carry complete six-dimensional conserved source and response bases",
        source_condition,
        f"ranks=6/6; max Ward={max(row['source_ward'] for row in rows):.2e}; "
        f"max condition={max(row['source_basis_condition'] for row in rows):.6f}",
    )

    equal_condition = mutation != "equal_tensor"
    equal_fractions = [row["equal"]["completed_fraction"] for row in rows]
    equal_condition &= all(row["equal"]["pair_count"] == 21 for row in rows)
    equal_condition &= all(
        right < left for left, right in zip(equal_fractions, equal_fractions[1:])
    )
    equal_condition &= equal_fractions[-1] < 0.025
    equal_condition &= 1.96 < equal_force["slope"] < 2.03
    equal_condition &= 2.98 < equal_ward["slope"] < 3.05
    equal_condition &= equal_force["maximum_relative"] < 0.003
    equal_condition &= equal_ward["maximum_relative"] < 0.003
    equal_condition &= equal_force["coefficient_spread"] < 1.02
    equal_condition &= equal_ward["coefficient_spread"] < 1.02
    checks.check(
        "all-source-equal-mode-completed-Ward-order",
        "the complete 21-component symmetric source tensor has quadratic completed force and cubic Ward order",
        equal_condition,
        f"force p={equal_force['slope']:.6f}; Ward p={equal_ward['slope']:.6f}; "
        f"fraction={equal_fractions[0]:.5f}->{equal_fractions[-1]:.5f}",
    )

    unequal_condition = mutation != "multimode_tensor"
    unequal_fractions = [row["unequal"]["completed_fraction"] for row in rows]
    unequal_condition &= all(row["unequal"]["pair_count"] == 36 for row in rows)
    unequal_condition &= all(
        right < left
        for left, right in zip(unequal_fractions, unequal_fractions[1:])
    )
    unequal_condition &= unequal_fractions[-1] < 0.06
    unequal_condition &= 1.92 < unequal_force["slope"] < 2.03
    unequal_condition &= 2.98 < unequal_ward["slope"] < 3.06
    unequal_condition &= unequal_force["maximum_relative"] < 0.004
    unequal_condition &= unequal_ward["maximum_relative"] < 0.003
    unequal_condition &= unequal_force["coefficient_spread"] < 1.03
    unequal_condition &= unequal_ward["coefficient_spread"] < 1.02
    checks.check(
        "all-pair-unequal-harmonic-completed-Ward-order",
        "all 36 k-plus-2k bilinear source pairs have quadratic completed force and cubic Ward order",
        unequal_condition,
        f"force p={unequal_force['slope']:.6f}; Ward p={unequal_ward['slope']:.6f}; "
        f"fraction={unequal_fractions[0]:.5f}->{unequal_fractions[-1]:.5f}",
    )

    reaction_condition = all(
        max(row["equal"]["reaction_ward"], row["unequal"]["reaction_ward"])
        < 2.0e-12
        for row in rows
    )
    checks.check(
        "metric-completion-reaction-is-Ward-null",
        "the fixed square-root completion changes no displacement Ward component in either full tensor",
        reaction_condition,
        f"maximum={max(max(row['equal']['reaction_ward'], row['unequal']['reaction_ward']) for row in rows):.2e}",
    )

    amplitude_condition = mutation != "amplitude_control"
    amplitude_condition &= amplitude_equal < 2.0e-5
    amplitude_condition &= amplitude_cross < 2.0e-5
    checks.check(
        "weak-jet-amplitude-control",
        "halving the field amplitude preserves representative equal- and unequal-harmonic quadratic forces",
        amplitude_condition,
        f"equal={amplitude_equal:.3e}; unequal={amplitude_cross:.3e}",
    )

    note_condition = (
        mutation != "note_boundary"
        and all(f"### n{index}" in note for index in range(1, 9))
        and "n1--n8 status: `pass`" in note
        and "full six-dimensional transverse source class" in note
        and "all 36 unequal-harmonic" in note
        and "not a uniform angular theorem" in note
        and "observable decoupling remains unproved" in note
        and "no toe percentage moves" in note
        and "no axiom is amended" in note
    )
    checks.check(
        "scope-refinement-and-no-go-packet",
        "the note separates the full one-ray tensor result from angular, observable, and physical closure",
        note_condition,
    )

    print(
        "N5_CERTIFICATE: two complete six-dimensional input bases, 21 equal-mode pairs, 36 unequal-harmonic pairs, and three infrared periods were executed"
    )
    print(
        "per_element: all fifteen edge classes enter every raw force, square-root completion, and Hessian reaction"
    )
    print(
        "per_site: all fifty hinges and 240 simplex-hinge incidences enter every cyclic phase site"
    )
    print(
        "per_mode: k, 2k, equal-output 2k, and cross-output 3k sectors are separately retained"
    )
    print(
        "per_block: full source bases, all 21 symmetric pairs, all 36 cross pairs, amplitude control, and Ward-null reactions are checked"
    )
    print(
        "lattice_wide: not executed; angular uniformity, noncollinear mode pairs, observables, refinement, and nonlinear Lorentzian closure remain open"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
