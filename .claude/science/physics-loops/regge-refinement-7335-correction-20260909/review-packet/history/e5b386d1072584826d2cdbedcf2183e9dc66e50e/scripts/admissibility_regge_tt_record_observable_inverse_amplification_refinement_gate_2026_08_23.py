#!/usr/bin/env python3
"""Block 180: test whether the gravity observable/refinement gate is selected.

The finite Schur-complement calculation is retained, but it is not promoted to
a physical covariance or a gravity verdict.  The runner instead checks two
pieces of data needed before that interpretation is well posed: an edge-space
representative of a metric observable and a physical norm/refinement map.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
import os
from pathlib import Path
import sys
import time

import numpy as np
from scipy.linalg import eigvalsh, null_space


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import admissibility_nonuniform_conserved_source_regge_increasing_period_pseudoconstraint_scaling_2026_08_12 as block59  # noqa: E402
import admissibility_regge_full_conserved_source_multimode_metric_completion_ward_boundary_2026_08_12 as block62  # noqa: E402


regge = block59.regge
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REGGE_TT_RECORD_OBSERVABLE_INVERSE_AMPLIFICATION_"
    "REFINEMENT_GATE_BOUNDED_THEOREM_NOTE_2026-08-23.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PLAN_PATH = ROOT / ".claude" / "science" / "physics-loops" / (
    "toe-axiom-closure-20260809"
) / "ARTIFACT_PLAN.md"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_REGGE_TT_RECORD_OBSERVABLE_INVERSE_AMPLIFICATION_REFINEMENT_GATE_BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "docs/ADMISSIBILITY_NONUNIFORM_CONSERVED_SOURCE_REGGE_INCREASING_PERIOD_PSEUDOCONSTRAINT_SCALING_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/ADMISSIBILITY_REGGE_FULL_CONSERVED_SOURCE_MULTIMODE_METRIC_COMPLETION_WARD_REFINEMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/ADMISSIBILITY_REFLECTED_CURVATURE_ACTION_RECORD_SOURCE_TWO_STEP_TRANSFER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    ".claude/science/physics-loops/toe-axiom-closure-20260809/ARTIFACT_PLAN.md",
    "scripts/admissibility_nonuniform_conserved_source_regge_increasing_period_pseudoconstraint_scaling_2026_08_12.py",
    "scripts/admissibility_regge_full_conserved_source_multimode_metric_completion_ward_boundary_2026_08_12.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
    "scripts/admissibility_regge_tt_record_observable_inverse_amplification_refinement_gate_2026_08_23.py",
)
AUDIT_TIMEOUT_SEC = 120

PERIOD = 5
REFINEMENT_PERIODS = (5, 7, 9, 11)
HARMONICS = (1, 2)
SOURCE_KINDS = ("static", "null")
SHIFT_COEFFICIENTS = (0.0, 1.0, 10.0)
AMPLITUDE = float(os.environ.get("TOE_METRIC_AMPLITUDE", "1e-4"))
COMPLEX_STEP = float(os.environ.get("TOE_HESSIAN_COMPLEX_STEP", "1e-20"))


@dataclass(frozen=True)
class Response:
    ratio: float
    generalized_min: float
    generalized_max: float
    fixed_gap: float
    dressed_norm: float
    identity_error: float
    solve_residual: float


@dataclass(frozen=True)
class LiftProbe:
    source: str
    harmonic: int
    observable: str
    kernel_dimension: int
    shift_edge_index: int
    shift_projection_norm: float
    metric_error: float
    gauge_error: float
    ratios: tuple[float, ...]
    spread: float
    cancellation_ratio: float
    cancellation_fraction: float
    cancellation_coefficient_norm: float
    responses: tuple[Response, ...]


def source_target(source: str) -> np.ndarray:
    target = np.zeros(10, dtype=complex)
    if source == "static":
        target[regge.HCOMPS.index((3, 3))] = 1.0
    elif source == "null":
        target[regge.HCOMPS.index((0, 0))] = 1.0
        target[regge.HCOMPS.index((3, 3))] = 1.0
        target[regge.HCOMPS.index((0, 3))] = 2.0
    else:
        raise ValueError(source)
    return target


def tt_targets(axis: int) -> dict[str, np.ndarray]:
    left, right = [value for value in range(3) if value != axis]
    plus = np.zeros(10, dtype=complex)
    plus[regge.HCOMPS.index((left, left))] = 1.0 / np.sqrt(2.0)
    plus[regge.HCOMPS.index((right, right))] = -1.0 / np.sqrt(2.0)
    cross = np.zeros(10, dtype=complex)
    cross[regge.HCOMPS.index(tuple(sorted((left, right))))] = np.sqrt(2.0)
    return {"tt_plus": plus, "tt_cross": cross}


def observable_targets(model: block59.SliceModel) -> dict[str, np.ndarray]:
    return {
        **tt_targets(model.axis),
        (
            "record_tensor_candidate"
            if model.source_kind == "null"
            else "density_tensor_candidate"
        ): source_target(model.source_kind),
    }


def momentum(model: block59.SliceModel, harmonic: int) -> np.ndarray:
    value = np.zeros(4)
    value[model.axis] = harmonic * model.k0
    return value


def edge_dual(momentum_value: np.ndarray, target: np.ndarray) -> np.ndarray:
    metric = regge.metric_map(momentum_value)
    return metric @ np.linalg.solve(metric.conj().T @ metric, target)


def kernel_basis(momentum_value: np.ndarray) -> np.ndarray:
    metric = regge.metric_map(momentum_value)
    return null_space(metric.conj().T, rcond=1.0e-12)


def named_kernel_direction(metric: np.ndarray) -> tuple[np.ndarray, int, float]:
    """Project the fixed edge order into the kernel without choosing its basis."""
    projector = np.eye(15) - metric @ np.linalg.solve(
        metric.conj().T @ metric, metric.conj().T
    )
    for edge_index in range(15):
        projected = projector[:, edge_index]
        norm = float(np.linalg.norm(projected))
        if norm > 1.0e-10:
            return projected / norm, edge_index, norm
    raise ValueError("metric lift has no nonmetric edge direction")


def real_harmonic_pair(
    model: block59.SliceModel, harmonic: int, edge_vector: np.ndarray
) -> np.ndarray:
    phase = np.exp(1j * harmonic * model.k0 * np.arange(model.period))
    first = np.asarray(
        [2.0 * np.real(value * edge_vector) for value in phase]
    ).reshape(-1)
    second = np.asarray(
        [-2.0 * np.imag(value * edge_vector) for value in phase]
    ).reshape(-1)
    return np.column_stack((first, second))


def solved_branch(
    period: int, source: str
) -> tuple[block59.SliceModel, np.ndarray, float, float]:
    model = block59.SliceModel(period, source)
    coupling = AMPLITUDE / model.metric_response_per_coupling
    coordinates = model.solve(coupling)
    lengths = model.lengths_from_coordinates(coordinates)
    residual = model.equations(coordinates, coupling)
    metric_response = 0.0
    response = lengths - model.flat_lengths[None, :]
    for mode, _momentum, metric, _gauge, _nongauge in model.mode_data:
        response_k = model.fourier(response, mode)
        fitted = metric @ np.linalg.lstsq(metric, response_k, rcond=None)[0]
        metric_response += float(np.linalg.norm(fitted) ** 2)
    return model, lengths, float(np.linalg.norm(residual)), metric_response**0.5


def batched_hessian(
    model: block59.SliceModel, lengths: np.ndarray
) -> tuple[np.ndarray, float]:
    flattened = np.asarray(lengths, dtype=float).reshape(-1)
    dimension = len(flattened)
    shifted = np.broadcast_to(flattened, (dimension, dimension)).astype(complex).copy()
    shifted[np.arange(dimension), np.arange(dimension)] += 1j * COMPLEX_STEP
    gradients = block62.batched_action_gradient(
        model, shifted.reshape(dimension, model.period, 15)
    ).reshape(dimension, dimension)
    raw = np.imag(gradients).T / COMPLEX_STEP
    raw_asymmetry = float(
        np.linalg.norm(raw - raw.T) / max(np.linalg.norm(raw), 1.0e-30)
    )
    return 0.5 * (raw + raw.T), raw_asymmetry


def projected_blocks(model: block59.SliceModel, hessian: np.ndarray) -> dict:
    nongauge = np.linalg.qr(model.B, mode="reduced")[0]
    displacement = np.linalg.qr(model.BG, mode="reduced")[0]
    hnn = nongauge.T @ hessian @ nongauge
    hnd = nongauge.T @ hessian @ displacement
    hdd = displacement.T @ hessian @ displacement
    schur = hdd - hnd.T @ np.linalg.solve(hnn, hnd)
    schur = 0.5 * (schur + schur.T)
    spectrum = np.linalg.eigvalsh(schur)
    threshold = max(1.0e-12, 1.0e-8 * float(np.max(np.abs(spectrum))))
    return {
        "nongauge": nongauge,
        "displacement": displacement,
        "hnn": hnn,
        "hnd": hnd,
        "hdd": hdd,
        "schur": schur,
        "negative": int(np.sum(spectrum < -threshold)),
        "positive": int(np.sum(spectrum > threshold)),
        "zero": int(np.sum(np.abs(spectrum) <= threshold)),
        "minimum_absolute": float(np.min(np.abs(spectrum))),
        "condition": float(np.linalg.cond(schur)),
        "basis_overlap": float(np.linalg.norm(nongauge.T @ displacement)),
    }


def generalized_phase_spectrum(
    fixed: np.ndarray, correction: np.ndarray
) -> tuple[float, float, float]:
    fixed = 0.5 * (fixed + fixed.T)
    correction = 0.5 * (correction + correction.T)
    fixed_spectrum = np.linalg.eigvalsh(fixed)
    gap = float(np.min(np.abs(fixed_spectrum)))
    threshold = max(1.0e-12, 1.0e-10 * float(np.max(np.abs(fixed_spectrum))))
    if np.all(fixed_spectrum > threshold):
        values = eigvalsh(correction, fixed)
    elif np.all(fixed_spectrum < -threshold):
        values = eigvalsh(-correction, -fixed)
    else:
        return float("-inf"), float("inf"), gap
    return float(np.min(values)), float(np.max(values)), gap


def response(
    model: block59.SliceModel, blocks: dict, harmonic: int, edge_vector: np.ndarray
) -> tuple[Response, np.ndarray]:
    pair = real_harmonic_pair(model, harmonic, edge_vector)
    nongauge = blocks["nongauge"]
    displacement = blocks["displacement"]
    op = nongauge.T @ pair
    og = displacement.T @ pair
    hnn_inverse_op = np.linalg.solve(blocks["hnn"], op)
    fixed = op.T @ hnn_inverse_op
    dressed = og - blocks["hnd"].T @ hnn_inverse_op
    correction = dressed.T @ np.linalg.solve(blocks["schur"], dressed)
    reduced = np.block(
        [[blocks["hnn"], blocks["hnd"]], [blocks["hnd"].T, blocks["hdd"]]]
    )
    reduced_observable = np.vstack((op, og))
    relaxed_solution = np.linalg.solve(reduced, reduced_observable)
    relaxed = reduced_observable.T @ relaxed_solution
    identity_scale = max(
        float(np.linalg.norm(relaxed, ord=2)),
        float(np.linalg.norm(fixed, ord=2) + np.linalg.norm(correction, ord=2)),
        1.0e-30,
    )
    identity_error = float(
        np.linalg.norm(relaxed - fixed - correction, ord=2) / identity_scale
    )
    solve_residual = float(
        np.linalg.norm(reduced @ relaxed_solution - reduced_observable)
        / max(np.linalg.norm(reduced_observable), 1.0e-30)
    )
    lower, upper, fixed_gap = generalized_phase_spectrum(fixed, correction)
    phase_ratio = max(abs(lower), abs(upper))
    return (
        Response(
            ratio=phase_ratio,
            generalized_min=lower,
            generalized_max=upper,
            fixed_gap=fixed_gap,
            dressed_norm=float(np.linalg.norm(dressed)),
            identity_error=identity_error,
            solve_residual=solve_residual,
        ),
        dressed,
    )


def cancellation_edge(
    model: block59.SliceModel,
    blocks: dict,
    harmonic: int,
    base: np.ndarray,
    kernel: np.ndarray,
) -> tuple[np.ndarray, float, float]:
    _base_response, base_dressed = response(model, blocks, harmonic, base)
    directions = []
    columns = []
    for column in range(kernel.shape[1]):
        for direction in (kernel[:, column], 1j * kernel[:, column]):
            directions.append(direction)
            _probe_response, probe_dressed = response(
                model, blocks, harmonic, direction
            )
            columns.append(probe_dressed.reshape(-1))
    design = np.column_stack(columns)
    coefficients = np.linalg.lstsq(
        design, -base_dressed.reshape(-1), rcond=None
    )[0]
    selected = base + sum(
        coefficient * direction
        for coefficient, direction in zip(coefficients, directions)
    )
    _selected_response, selected_dressed = response(
        model, blocks, harmonic, selected
    )
    fraction = float(
        np.linalg.norm(selected_dressed) / max(np.linalg.norm(base_dressed), 1.0e-30)
    )
    return selected, fraction, float(np.linalg.norm(coefficients))


def lift_probes(model: block59.SliceModel, blocks: dict) -> list[LiftProbe]:
    output = []
    for harmonic in HARMONICS:
        momentum_value = momentum(model, harmonic)
        metric = regge.metric_map(momentum_value)
        gauge = regge.gauge_map(momentum_value)
        kernel = kernel_basis(momentum_value)
        shift_direction, shift_edge_index, shift_projection_norm = (
            named_kernel_direction(metric)
        )
        for name, target in observable_targets(model).items():
            base = edge_dual(momentum_value, target)
            representatives = [
                base + coefficient * shift_direction
                for coefficient in SHIFT_COEFFICIENTS
            ]
            responses = tuple(
                response(model, blocks, harmonic, representative)[0]
                for representative in representatives
            )
            selected, cancellation_fraction, coefficient_norm = cancellation_edge(
                model, blocks, harmonic, base, kernel
            )
            cancellation_response = response(model, blocks, harmonic, selected)[0]
            all_representatives = representatives + [selected]
            metric_error = max(
                float(
                    np.linalg.norm(metric.conj().T @ representative - target)
                    / max(np.linalg.norm(target), 1.0e-30)
                )
                for representative in all_representatives
            )
            gauge_error = max(
                float(
                    np.linalg.norm(gauge.conj().T @ representative)
                    / max(np.linalg.norm(representative), 1.0e-30)
                )
                for representative in all_representatives
            )
            ratios = tuple(item.ratio for item in responses)
            spread = max(ratios) / max(min(ratios), 1.0e-30)
            output.append(
                LiftProbe(
                    source=model.source_kind,
                    harmonic=harmonic,
                    observable=name,
                    kernel_dimension=kernel.shape[1],
                    shift_edge_index=shift_edge_index,
                    shift_projection_norm=shift_projection_norm,
                    metric_error=metric_error,
                    gauge_error=gauge_error,
                    ratios=ratios,
                    spread=spread,
                    cancellation_ratio=cancellation_response.ratio,
                    cancellation_fraction=cancellation_fraction,
                    cancellation_coefficient_norm=coefficient_norm,
                    responses=responses + (cancellation_response,),
                )
            )
    return output


def raw_fourier_encoder(period: int, harmonic: int) -> np.ndarray:
    phase = np.exp(2j * np.pi * harmonic * np.arange(period) / period)
    scale = np.sqrt(2.0 / period)
    encoder = np.zeros((15 * period, 30))
    for edge in range(15):
        encoder[edge::15, edge] = scale * np.real(phase)
        encoder[edge::15, 15 + edge] = -scale * np.imag(phase)
    return encoder


def metric_realification(period: int, harmonic: int, axis: int) -> np.ndarray:
    momentum_value = np.zeros(4)
    momentum_value[axis] = 2.0 * np.pi * harmonic / period
    metric = regge.metric_map(momentum_value)
    return np.block(
        [[metric.real, -metric.imag], [metric.imag, metric.real]]
    )


def refinement_probes() -> list[dict]:
    output = []
    for source in SOURCE_KINDS:
        axis = 0 if source == "static" else 1
        for harmonic in HARMONICS:
            for coarse, fine in zip(REFINEMENT_PERIODS, REFINEMENT_PERIODS[1:]):
                coarse_fourier = raw_fourier_encoder(coarse, harmonic)
                fine_fourier = raw_fourier_encoder(fine, harmonic)
                coarse_metric = metric_realification(coarse, harmonic, axis)
                fine_metric = metric_realification(fine, harmonic, axis)
                raw_injection = fine_fourier @ coarse_fourier.T
                transported_band = raw_injection @ coarse_fourier
                raw_isometry = float(
                    np.linalg.norm(
                        transported_band.T @ transported_band - np.eye(30)
                    )
                )
                coarse_gram = coarse_metric.T @ coarse_metric
                fine_gram = fine_metric.T @ fine_metric
                gram_spectrum = eigvalsh(fine_gram, coarse_gram)
                coarse_encoder = coarse_fourier @ coarse_metric
                fine_encoder = fine_fourier @ fine_metric
                intertwining_defect = float(
                    np.linalg.norm(raw_injection @ coarse_encoder - fine_encoder)
                    / np.linalg.norm(fine_encoder)
                )
                output.append(
                    {
                        "source": source,
                        "harmonic": harmonic,
                        "coarse": coarse,
                        "fine": fine,
                        "raw_isometry": raw_isometry,
                        "gram_min": float(np.min(gram_spectrum)),
                        "gram_max": float(np.max(gram_spectrum)),
                        "gram_deviation": float(np.max(np.abs(gram_spectrum - 1.0))),
                        "intertwining_defect": intertwining_defect,
                    }
                )
    return output


def apply_mutation(
    mutation: str,
    branches: list[dict],
    probes: list[LiftProbe],
    refinements: list[dict],
    note: str,
) -> str:
    """Perturb one evidence field so each adversarial run exercises one gate."""
    if mutation == "raw_hessian":
        branches[0]["raw_asymmetry"] = 1.0e-4
    elif mutation == "lift_kernel":
        probes[0] = replace(probes[0], kernel_dimension=4)
    elif mutation == "lift_dependence":
        probes[0] = replace(probes[0], ratios=(1.0, 1.0, 1.0), spread=1.0)
    elif mutation == "cancellation_lift":
        probes[0] = replace(
            probes[0], cancellation_ratio=2.0, cancellation_fraction=1.0
        )
    elif mutation == "refinement_gram":
        refinements[0] = {**refinements[0], "raw_isometry": 1.0e-3}
    elif mutation == "schur_identity":
        first = probes[0]
        altered = replace(first.responses[0], identity_error=1.0e-3)
        probes[0] = replace(first, responses=(altered,) + first.responses[1:])
    elif mutation == "note_boundary":
        note = note.replace(
            "terminal observable verdict: blocked by unselected physical quotient/refinement data",
            "terminal observable verdict: removed",
        )
    elif mutation:
        raise ValueError(f"unknown TOE_MUTATION={mutation}")
    return note


def main() -> int:
    started = time.perf_counter()
    mutation = os.environ.get("TOE_MUTATION", "")
    checks = block59.Checks()
    note = " ".join(NOTE_PATH.read_text(encoding="utf-8").lower().split())
    plan = " ".join(PLAN_PATH.read_text(encoding="utf-8").lower().split())
    axiom = " ".join(AXIOM_PATH.read_text(encoding="utf-8").lower().split())

    branches = []
    probes = []
    for source in SOURCE_KINDS:
        model, lengths, branch_residual, metric_response = solved_branch(
            PERIOD, source
        )
        hessian, raw_asymmetry = batched_hessian(model, lengths)
        blocks = projected_blocks(model, hessian)
        branch_probes = lift_probes(model, blocks)
        probes.extend(branch_probes)
        branches.append(
            {
                "source": source,
                "model": model,
                "branch_residual": branch_residual,
                "metric_response": metric_response,
                "raw_asymmetry": raw_asymmetry,
                "blocks": blocks,
            }
        )
    refinements = refinement_probes()
    note = apply_mutation(mutation, branches, probes, refinements, note)

    print(
        "RESULT: the fixed-average finite Schur identity is valid, but current physical premises justify neither a TT/Record readout representative nor a physical refinement norm"
    )
    print(
        "INTERPRETATION: the Moore-Penrose susceptibility is a convention-scoped diagnostic, not a physical covariance and not a gravity verdict"
    )
    for branch in branches:
        model = branch["model"]
        blocks = branch["blocks"]
        print(
            f"branch: source={branch['source']} L={PERIOD} "
            f"residual={branch['branch_residual']:.2e} metric={branch['metric_response']:.3e} "
            f"ranks={np.linalg.matrix_rank(model.B)}+{np.linalg.matrix_rank(model.BG)}+10={model.complete_rank} "
            f"raw_asym={branch['raw_asymmetry']:.2e} "
            f"Schur={blocks['negative']}-/{blocks['positive']}+/{blocks['zero']}zero "
            f"gap={blocks['minimum_absolute']:.2e} cond={blocks['condition']:.2e}"
        )
    for probe in probes:
        ratios = ",".join(f"{value:.3e}" for value in probe.ratios)
        print(
            f"lift_fiber: source={probe.source} m={probe.harmonic} name={probe.observable} "
            f"ker={probe.kernel_dimension} projected_edge={probe.shift_edge_index} "
            f"projection_norm={probe.shift_projection_norm:.3e} "
            f"ratios[0,1,10]={ratios} spread={probe.spread:.2e} "
            f"least_squares={probe.cancellation_ratio:.3e} "
            f"dress_fraction={probe.cancellation_fraction:.2e}"
        )
    for row in refinements:
        if row["source"] != "static":
            continue
        print(
            f"refinement: sources=static,null m={row['harmonic']} "
            f"L={row['coarse']}->{row['fine']} raw_iso={row['raw_isometry']:.1e} "
            f"Gram=[{row['gram_min']:.6f},{row['gram_max']:.6f}] "
            f"metric_defect={row['intertwining_defect']:.3e}"
        )

    structural = all(
        branch["branch_residual"] < 2.0e-11
        and abs(branch["metric_response"] - AMPLITUDE) < 2.0e-7
        and branch["raw_asymmetry"] < 2.0e-12
        and np.linalg.matrix_rank(branch["model"].B)
        + np.linalg.matrix_rank(branch["model"].BG)
        + 10
        == branch["model"].complete_rank
        == 15 * PERIOD
        and branch["blocks"]["zero"] == 0
        and branch["blocks"]["basis_overlap"] < 2.0e-12
        for branch in branches
    )
    checks.check(
        "fixed-average-raw-Hessian-and-Schur",
        "both sourced L=5 branches have unsymmetrized-Hessian and resolved fixed-average Schur guards",
        structural,
        f"max raw asymmetry={max(row['raw_asymmetry'] for row in branches):.3e}",
    )

    lift_kernel = all(
        probe.kernel_dimension == 5
        and probe.shift_edge_index == 0
        and probe.shift_projection_norm > 1.0e-10
        and probe.metric_error < 2.0e-12
        and probe.gauge_error < 2.0e-12
        for probe in probes
    )
    checks.check(
        "unselected-five-dimensional-edge-lift-fiber",
        "every named conserved tensor target has a five-dimensional edge-lift fiber preserving target and flat gauge identities",
        lift_kernel,
        f"max metric={max(row.metric_error for row in probes):.3e}; max gauge={max(row.gauge_error for row in probes):.3e}",
    )

    tt_probes = [probe for probe in probes if probe.observable.startswith("tt_")]
    opposite_readings = sum(
        min(probe.ratios) < 1.0 < max(probe.ratios) for probe in tt_probes
    )
    lift_dependence = min(probe.spread for probe in tt_probes) > 2.0
    lift_dependence &= opposite_readings == len(tt_probes)
    checks.check(
        "inverse-response-depends-on-unselected-lift",
        "deterministic representatives of the same metric covector give materially inequivalent inverse-response readings",
        lift_dependence,
        f"TT minimum spread={min(row.spread for row in tt_probes):.3f}; sub/dominant flips={opposite_readings}/{len(tt_probes)}",
    )

    strong_cancellations = sum(
        probe.cancellation_fraction < 2.0e-2 for probe in probes
    )
    cancellation = all(
        probe.cancellation_fraction < 0.75
        and probe.cancellation_ratio < probe.ratios[0]
        for probe in probes
    )
    cancellation &= strong_cancellations >= 9
    checks.check(
        "least-squares-lift-nonselection-witness",
        "a target-preserving kernel solve reduces the dressed overlap without being promoted to a physical repair",
        cancellation,
        f"strong reductions={strong_cancellations}/{len(probes)}; max fraction={max(row.cancellation_fraction for row in probes):.3f}",
    )

    paired_refinements = zip(refinements[:6], refinements[6:])
    axis_difference = max(
        abs(left[key] - right[key])
        for left, right in paired_refinements
        for key in (
            "raw_isometry",
            "gram_min",
            "gram_max",
            "intertwining_defect",
        )
    )
    refinement = max(row["raw_isometry"] for row in refinements) < 5.0e-12
    refinement &= min(row["gram_deviation"] for row in refinements) > 1.0e-2
    refinement &= min(row["intertwining_defect"] for row in refinements) > 5.0e-2
    refinement &= axis_difference < 2.0e-12
    checks.check(
        "raw-Parseval-versus-metric-refinement-mismatch",
        "raw Fourier injection is isometric but does not preserve the momentum-dependent metric encoder or its Euclidean Gram form",
        refinement,
        f"Gram deviation=[{min(row['gram_deviation'] for row in refinements):.3e},{max(row['gram_deviation'] for row in refinements):.3e}]; axis diff={axis_difference:.1e}",
    )

    every_response = [item for probe in probes for item in probe.responses]
    schur_identity = all(
        np.isfinite(item.ratio)
        and item.fixed_gap > 1.0e-8
        and item.identity_error < 2.0e-7
        and item.solve_residual < 2.0e-9
        for item in every_response
    )
    checks.check(
        "phasewise-generalized-Schur-identity",
        "phasewise generalized responses obey the exact finite block-inverse identity on every tested representative",
        schur_identity,
        f"max identity={max(row.identity_error for row in every_response):.3e}; max solve={max(row.solve_residual for row in every_response):.3e}",
    )

    note_boundary = (
        "terminal observable verdict: blocked by unselected physical quotient/refinement data"
        in note
        and all(f"### n{index}" in note for index in range(1, 9))
        and "n1--n8 status: `pass`" in note
        and "not gravity failure" in note
        and "zero toe percentage movement" in note
        and "no axiom is amended" in note
        and "fixed-average" in note
        and "independent-audit correction and selector boundary addendum" in plan
        and "source/action and physical-observable identification" in axiom
        and "a choice not fixed by the supplied structure" in axiom
    )
    checks.check(
        "scope-no-go-discipline-and-axiom-boundary",
        "the theorem note keeps the blocker narrow, preserves live routes, and makes no gravity or axiom overclaim",
        note_boundary,
    )

    print(
        "N5_CERTIFICATE: 2 sourced fixed-average Hessians; 8 TT and 4 source-tensor-candidate lift fibers; 48 shifted/cancelled phase-paired responses; 12 directed refinement comparisons"
    )
    print(
        "BOUNDARY: no branch-dependent gauge generator, relational nonlinear observable, matter/source Hessian, Lorentzian covariance, physical quotient norm, or state/update refinement law is supplied"
    )
    print(
        "SELECTOR_VERDICT: BLOCKED_BY_UNSELECTED_PHYSICAL_QUOTIENT_REFINEMENT_DATA"
    )
    print("ROUTE_VERDICT: INCONCLUSIVE")
    print("TOE_MOVEMENT: obligations=0 percentages=0 axioms_amended=0")
    print(f"elapsed_sec={time.perf_counter() - started:.2f}")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
