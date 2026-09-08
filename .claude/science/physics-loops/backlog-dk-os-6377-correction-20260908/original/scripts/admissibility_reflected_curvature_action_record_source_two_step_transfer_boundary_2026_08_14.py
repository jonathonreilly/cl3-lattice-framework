#!/usr/bin/env python3
"""Block 74: falsify the shortest reflected-curvature gravity transfer route.

The runner adds the exact Block-49 curvature intertwiner to the Block-48
twenty-two-edge reflected action,

    Q_mu(q) = Q_union(q) + mu D(-q)^T D(q),  mu = 1/1024.

It first tests the constructive target: lift only the three relative h_it
flat modes, retain the common ten-coordinate metric, exact displacement Ward
identities, time reflection, all six Block-68 Record sources, and the static
Newtonian residue.  It then applies a necessary Stieltjes/Hankel positivity
test to two genuinely local, same-time transverse edge observables.  The test
separates the attractive infrared two-slice result from a hostile finite-zone
counterexample.  It is a boundary on this action/cadence pair, not a gravity
no-go.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
import os
from pathlib import Path
import sys

import numpy as np
from scipy.linalg import null_space


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 240
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REFLECTED_CURVATURE_ACTION_RECORD_SOURCE_TWO_STEP_"
    "TRANSFER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
BLOCK48_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REGGE_REFLECTED_ORIENTATION_COMMON_METRIC_TRANSFER_"
    "GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
BLOCK49_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REFLECTED_PLAQUETTE_CURVATURE_RECORD_RICCI_SOURCE_"
    "INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
BLOCK53_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_"
    "UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
BLOCK68_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CYCLE713_RECORD_STRESS_BLOCK44_IR_REFLECTED_CARRIER_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
PREMISE_PATH = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_REFLECTED_CURVATURE_ACTION_RECORD_SOURCE_TWO_STEP_TRANSFER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_REGGE_REFLECTED_ORIENTATION_COMMON_METRIC_TRANSFER_GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_REFLECTED_PLAQUETTE_CURVATURE_RECORD_RICCI_SOURCE_INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_CYCLE713_RECORD_STRESS_BLOCK44_IR_REFLECTED_CARRIER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_regge_reflected_orientation_common_metric_transfer_gate_boundary_2026_08_11.py",
    "scripts/admissibility_reflected_plaquette_curvature_record_ricci_source_intertwiner_boundary_2026_08_11.py",
    "scripts/admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_2026_08_11.py",
    "scripts/admissibility_cycle713_record_stress_block44_ir_reflected_carrier_boundary_2026_08_13.py",
    "scripts/admissibility_reflected_curvature_action_record_source_two_step_transfer_boundary_2026_08_14.py",
)

sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_regge_reflected_orientation_common_metric_transfer_gate_boundary_2026_08_11 as block48  # noqa: E402
import admissibility_reflected_plaquette_curvature_record_ricci_source_intertwiner_boundary_2026_08_11 as block49  # noqa: E402
import admissibility_cycle713_record_stress_block44_ir_reflected_carrier_boundary_2026_08_13 as block68  # noqa: E402


MU = 1.0 / 1024.0
RIVAL_MU = 2.0 / 1024.0
HALF_MU = 1.0 / 2048.0
TIME_SIZES = (256, 512, 1024, 2048)
IR_WAVE_NUMBER = 0.4
HOSTILE_WAVE_NUMBER = np.pi / 2.0
STATIC_WAVE_NUMBERS = (0.0125, 0.025, 0.05, 0.10, 0.20, 0.40)
TORUS_SIZES = tuple(range(3, 9))


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 168 else detail[:165] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


@dataclass(frozen=True)
class SourceCertificate:
    samples: int
    nullities: tuple[int, ...]
    maximum_ward: float
    maximum_relative_residual: tuple[float, ...]
    selection_ratio: float


@dataclass(frozen=True)
class TemporalCarrier:
    size: int
    wave_number: float
    moments: tuple[np.ndarray, np.ndarray]
    quotient_inertias: tuple[tuple[int, int, int], ...]
    maximum_gauge_overlap: float
    maximum_reflection_overlap: float
    maximum_ward: float
    maximum_hermiticity: float
    maximum_bordered_error: float
    minimum_quotient_gap: float


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def inertia(matrix: np.ndarray, tolerance: float = 1.0e-9) -> tuple[int, int, int]:
    hermitian = 0.5 * (matrix + matrix.conj().T)
    eigenvalues = np.linalg.eigvalsh(hermitian)
    return (
        int(np.sum(eigenvalues < -tolerance)),
        int(np.sum(eigenvalues > tolerance)),
        int(np.sum(np.abs(eigenvalues) <= tolerance)),
    )


def cross_action_symbol(
    union: block48.ReflectionUnion,
    momentum: np.ndarray,
    mu: float,
    mutation: str = "",
) -> np.ndarray:
    """Finite-range reflected action with an analytic D(-q)^T D(q) term."""

    q = np.asarray(momentum, dtype=complex)
    right = block49.centered_curvature_intertwiner(union, q)
    if mutation == "wrong_reflection_factor":
        left = right.T
        penalty = left @ right
    else:
        left = block49.centered_curvature_intertwiner(union, -q).T
        penalty = left @ right
    return block48.union_symbol(union, q) + mu * penalty


def relative_shift_modes(
    union: block48.ReflectionUnion,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    (shared_constraint, pair_to_union, _), _ = block48.union_reflection_split(union)
    relative_pairs = np.zeros((20, 3), dtype=float)
    for column, spatial in enumerate(range(3)):
        component = block48.HCOMPS.index((spatial, 3))
        relative_pairs[component, column] = 1.0
        relative_pairs[len(block48.HCOMPS) + component, column] = -1.0
    return shared_constraint, pair_to_union, pair_to_union @ relative_pairs


def structural_certificate(
    union: block48.ReflectionUnion, mu: float, mutation: str
) -> dict[str, object]:
    shared, pair_to_union, relative = relative_shift_modes(union)
    common = block48.metric_coefficients(np.asarray(union.directions))
    zero = np.zeros(4, dtype=complex)
    rows_zero = block49.centered_curvature_intertwiner(union, zero)
    symbol_zero = cross_action_symbol(union, zero, mu, mutation)

    common_residual = float(np.max(np.abs(rows_zero @ common)))
    relative_singular = np.linalg.svd(rows_zero @ relative, compute_uv=False)
    combined_rank = int(
        np.linalg.matrix_rank(
            np.column_stack((common, relative)), tol=1.0e-12
        )
    )

    momenta = (
        np.asarray((0.025, 0.0, 0.0, 0.0)),
        np.asarray((0.40, 0.0, 0.0, 0.0)),
        np.asarray((0.30, 0.20, -0.10, 0.40)),
        np.asarray((1.20, -0.20, 0.40, 0.70)),
    )
    nullities: set[int] = set()
    maximum_ward = 0.0
    maximum_reflection = 0.0
    maximum_hermiticity = 0.0
    for momentum in momenta:
        symbol = cross_action_symbol(union, momentum, mu, mutation)
        right_gauge = block48.union_gauge_map(union, momentum)
        left_gauge = block48.union_gauge_map(union, -momentum)
        nullities.add(22 - int(np.linalg.matrix_rank(symbol, tol=1.0e-9)))
        maximum_ward = max(
            maximum_ward,
            float(np.max(np.abs(symbol @ right_gauge))),
            float(np.max(np.abs(left_gauge.T @ symbol))),
        )
        reflected = block48.TIME_REFLECTION @ momentum
        theta_right = block48.union_time_reflection_matrix(union, momentum)
        theta_left = block48.union_time_reflection_matrix(union, -momentum)
        transformed = (
            theta_left.T
            @ cross_action_symbol(union, reflected, mu, mutation)
            @ theta_right
        )
        maximum_reflection = max(
            maximum_reflection, float(np.max(np.abs(symbol - transformed)))
        )
        maximum_hermiticity = max(
            maximum_hermiticity, float(np.max(np.abs(symbol - symbol.conj().T)))
        )

    return {
        "zero_inertia": inertia(symbol_zero),
        "common_residual": common_residual,
        "relative_singular": relative_singular,
        "combined_rank": combined_rank,
        "shared_rank": int(np.linalg.matrix_rank(shared, tol=1.0e-12)),
        "pair_rank": int(np.linalg.matrix_rank(pair_to_union, tol=1.0e-12)),
        "nullities": tuple(sorted(nullities)),
        "ward": maximum_ward,
        "reflection": maximum_reflection,
        "hermiticity": maximum_hermiticity,
    }


def source_certificate(
    union: block48.ReflectionUnion,
    mus: tuple[float, ...],
    drop_closure_edge: bool,
    mutation: str,
) -> SourceCertificate:
    edge_index = {direction: slot for slot, direction in enumerate(union.directions)}
    maximum_ward = 0.0
    maximum_relative_residual = np.zeros(len(mus), dtype=float)
    nullities: set[int] = set()
    samples = 0
    selection_pair: tuple[np.ndarray, np.ndarray] | None = None

    for size in TORUS_SIZES:
        for direction in block68.DIRECTIONS:
            carrier = block68.canonical_carrier(tuple(union.directions), direction)
            if carrier is None:
                raise AssertionError("reflected union must carry every signed direction")
            edge, base_offset = carrier
            row = edge_index[edge]
            step = np.concatenate((direction, (1,))).astype(int)
            separation = block68.transverse_offset(direction)
            line_length = size - int(drop_closure_edge)
            for mode in product(range(size), repeat=4):
                momentum = 2.0 * np.pi * np.asarray(mode, dtype=float) / size
                line_factor = sum(
                    np.exp(1j * np.dot(momentum, count * step + base_offset))
                    for count in range(line_length)
                )
                neutral_factor = line_factor * (
                    1.0 - np.exp(1j * np.dot(momentum, separation))
                )
                source = np.zeros(len(union.directions), dtype=complex)
                source[row] = 2.0 * neutral_factor
                source_norm = float(np.linalg.norm(source))
                if source_norm < 1.0e-9:
                    continue

                samples += 1
                gauge = block48.union_gauge_map(union, momentum)
                maximum_ward = max(
                    maximum_ward, float(np.linalg.norm(source.conj() @ gauge))
                )
                source_column = source.conj()
                curvature = block49.centered_curvature_intertwiner(union, momentum)
                responses = []
                for slot, mu in enumerate(mus):
                    symbol = cross_action_symbol(union, momentum, mu, mutation)
                    nullities.add(22 - int(np.linalg.matrix_rank(symbol, tol=1.0e-9)))
                    response = -np.linalg.pinv(symbol, rcond=1.0e-9) @ source_column
                    residual = float(np.linalg.norm(symbol @ response + source_column))
                    maximum_relative_residual[slot] = max(
                        maximum_relative_residual[slot], residual / source_norm
                    )
                    responses.append(curvature @ response)

                if (
                    size == 5
                    and tuple(int(item) for item in direction) == (1, 0, 0)
                    and tuple(mode) == (1, 1, 0, 4)
                ):
                    selection_pair = (responses[0], responses[1])

    if selection_pair is None:
        raise AssertionError("declared coefficient-selection witness was not executed")
    selection_ratio = float(
        (np.linalg.norm(selection_pair[0]) - np.linalg.norm(selection_pair[1]))
        / np.linalg.norm(selection_pair[0])
    )
    return SourceCertificate(
        samples=samples,
        nullities=tuple(sorted(nullities)),
        maximum_ward=maximum_ward,
        maximum_relative_residual=tuple(float(item) for item in maximum_relative_residual),
        selection_ratio=selection_ratio,
    )


def static_source_certificate(
    union: block48.ReflectionUnion, mu: float, mutation: str
) -> dict[str, tuple[float, ...]]:
    edge_index = {direction: slot for slot, direction in enumerate(union.directions)}
    source = np.zeros(len(union.directions), dtype=complex)
    source[edge_index[(0, 0, 0, 1)]] = 2.0
    residues = []
    nonmetric_fractions = []
    solve_residuals = []
    for wave_number in STATIC_WAVE_NUMBERS:
        momentum = np.asarray((wave_number, 0.0, 0.0, 0.0), dtype=complex)
        symbol = cross_action_symbol(union, momentum, mu, mutation)
        response = -np.linalg.pinv(symbol, rcond=1.0e-10) @ source
        metric_map = block49.union_line_metric_map(union, momentum)
        metric = np.linalg.lstsq(metric_map, response, rcond=None)[0]
        fitted = metric_map @ metric
        residues.append(
            float(
                (wave_number**2 * metric[block48.HCOMPS.index((3, 3))]).real
            )
        )
        nonmetric_fractions.append(
            float(np.linalg.norm(response - fitted) / np.linalg.norm(response))
        )
        solve_residuals.append(float(np.linalg.norm(symbol @ response + source)))
    return {
        "residues": tuple(residues),
        "nonmetric": tuple(nonmetric_fractions),
        "solve": tuple(solve_residuals),
    }


def local_tt_observables(
    union: block48.ReflectionUnion, mutation: str
) -> tuple[np.ndarray, np.ndarray]:
    index = {direction: slot for slot, direction in enumerate(union.directions)}
    plus = np.zeros(len(union.directions), dtype=complex)
    plus[index[(0, 1, 0, 0)]] = 1.0
    plus[index[(0, 0, 1, 0)]] = -1.0

    cross = np.zeros(len(union.directions), dtype=complex)
    cross[index[(0, 1, 1, 0)]] = np.sqrt(2.0)
    cross[index[(0, 1, 0, 0)]] = -1.0
    cross[index[(0, 0, 1, 0)]] = -1.0
    if mutation == "gauge_observable":
        cross[index[(1, 0, 0, 0)]] += 1.0
    return plus, cross


def temporal_carrier(
    union: block48.ReflectionUnion,
    size: int,
    wave_number: float,
    mu: float,
    mutation: str,
) -> TemporalCarrier:
    frequencies = -np.pi + np.arange(size) * (2.0 * np.pi / size)
    observables = local_tt_observables(union, mutation)
    covariance = tuple(np.empty(size, dtype=complex) for _ in observables)
    quotient_inertias: set[tuple[int, int, int]] = set()
    maximum_gauge_overlap = 0.0
    maximum_reflection_overlap = 0.0
    maximum_ward = 0.0
    maximum_hermiticity = 0.0
    maximum_bordered_error = 0.0
    minimum_quotient_gap = np.inf

    for frequency_index, frequency in enumerate(frequencies):
        momentum = np.asarray((wave_number, 0.0, 0.0, frequency), dtype=complex)
        symbol = cross_action_symbol(union, momentum, mu, mutation)
        gauge = block48.union_gauge_map(union, momentum)
        quotient = null_space(gauge.conj().T, rcond=1.0e-11)
        operator = quotient.conj().T @ (-symbol) @ quotient
        operator = 0.5 * (operator + operator.conj().T)
        quotient_inertias.add(inertia(operator))
        minimum_quotient_gap = min(
            minimum_quotient_gap,
            float(np.min(np.abs(np.linalg.eigvalsh(operator)))),
        )
        maximum_ward = max(maximum_ward, float(np.linalg.norm(symbol @ gauge)))
        maximum_hermiticity = max(
            maximum_hermiticity, float(np.linalg.norm(symbol - symbol.conj().T))
        )
        for slot, observable in enumerate(observables):
            maximum_gauge_overlap = max(
                maximum_gauge_overlap,
                float(np.linalg.norm(gauge.conj().T @ observable)),
            )
            reflection = block48.union_time_reflection_matrix(union, momentum)
            maximum_reflection_overlap = max(
                maximum_reflection_overlap,
                float(np.linalg.norm(reflection @ observable - observable)),
            )
            projected = quotient.conj().T @ observable
            covariance_value = projected.conj() @ np.linalg.solve(operator, projected)
            covariance[slot][frequency_index] = covariance_value
            bordered = np.block(
                [
                    [-symbol, gauge],
                    [gauge.conj().T, np.zeros((4, 4), dtype=complex)],
                ]
            )
            right_hand_side = np.concatenate((observable, np.zeros(4, dtype=complex)))
            bordered_response = np.linalg.solve(bordered, right_hand_side)[:22]
            bordered_value = observable.conj() @ bordered_response
            maximum_bordered_error = max(
                maximum_bordered_error,
                float(abs(covariance_value - bordered_value)),
            )

    moments = tuple(
        np.asarray(
            [
                np.mean(np.exp(1j * frequencies * time) * values).real
                for time in range(13)
            ]
        )
        for values in covariance
    )
    return TemporalCarrier(
        size=size,
        wave_number=wave_number,
        moments=(moments[0], moments[1]),
        quotient_inertias=tuple(sorted(quotient_inertias)),
        maximum_gauge_overlap=maximum_gauge_overlap,
        maximum_reflection_overlap=maximum_reflection_overlap,
        maximum_ward=maximum_ward,
        maximum_hermiticity=maximum_hermiticity,
        maximum_bordered_error=maximum_bordered_error,
        minimum_quotient_gap=minimum_quotient_gap,
    )


def hankel_minimum(
    moments: np.ndarray, step: int, order: int, shift: int
) -> float:
    matrix = np.asarray(
        [
            [moments[step * (left + right + shift)] for right in range(order)]
            for left in range(order)
        ],
        dtype=float,
    )
    return float(np.linalg.eigvalsh(matrix)[0])


def main() -> int:
    checks = Checks()
    mutation = os.environ.get("TOE_MUTATION", "")
    note = flat(NOTE_PATH)
    axioms = flat(AXIOM_PATH)
    block48_note = flat(BLOCK48_PATH)
    block49_note = flat(BLOCK49_PATH)
    block53_note = flat(BLOCK53_PATH)
    block68_note = flat(BLOCK68_PATH)

    checks.check(
        "A-authority-and-scope-bindings",
        "the actual axiom boundary and Blocks 48, 49, 53, and 68 are bound without promotion",
        all((ROOT / path).exists() for path in AUDIT_INPUT_PATHS)
        and "does not choose a hamiltonian or transfer operator" in axioms
        and "thirteen-dimensional constant-metric flat fiber" in block48_note
        and "exact three-component intertwiner exists" in block49_note
        and "stable finite-depth causal two-tt update exists" in block53_note
        and "6,528" in block68_note,
    )

    union = block48.build_reflection_union()
    applied_mu = 0.0 if mutation == "remove_cross_action" else MU
    structural = structural_certificate(union, applied_mu, mutation)
    checks.check(
        "B-exact-flat-fiber-thirteen-to-ten",
        "the local curvature square lifts exactly three relative h_it modes and leaves ten common flat metrics",
        len(union.directions) == 22
        and structural["shared_rank"] == 7
        and structural["pair_rank"] == 17
        and structural["combined_rank"] == 13
        and structural["zero_inertia"] == (7, 5, 10)
        and structural["common_residual"] < 5.0e-15
        and np.max(np.abs(np.asarray(structural["relative_singular"]) - 2.0)) < 5.0e-15,
        "Q0 inertia=" + str(structural["zero_inertia"])
        + f"; D common={structural['common_residual']:.3e}; relative singular="
        + np.array2string(np.asarray(structural["relative_singular"]), precision=9),
    )
    checks.check(
        "C-local-ward-reflection-and-four-null-sector",
        "the cross action is Hermitian, reflection covariant, Ward null, and leaves only four generic gauge nulls",
        structural["nullities"] == (4,)
        and structural["ward"] < 1.0e-12
        and structural["reflection"] < 1.0e-12
        and structural["hermiticity"] < 1.0e-12,
        f"nullities={structural['nullities']}; Ward={structural['ward']:.3e}; reflection={structural['reflection']:.3e}; Hermiticity={structural['hermiticity']:.3e}",
    )

    source = source_certificate(
        union,
        (MU, RIVAL_MU if mutation != "erase_rival" else MU),
        mutation == "drop_closure_edge",
        mutation,
    )
    checks.check(
        "D-all-six-record-sources-survive",
        "all 6,528 supported closed neutral six-direction Record sources solve with exactly four nulls",
        source.samples == 6528
        and source.nullities == (4,)
        and source.maximum_ward < 1.0e-12
        and max(source.maximum_relative_residual) < 1.0e-10,
        f"samples={source.samples}; nullities={source.nullities}; Ward={source.maximum_ward:.3e}; relative solve={source.maximum_relative_residual}",
    )

    static = static_source_certificate(union, MU, mutation)
    checks.check(
        "E-newtonian-residue-and-common-metric-limit",
        "the pure temporal edge source retains k^2 h_tt to two while its nonmetric fraction vanishes",
        abs(static["residues"][0] - 2.0) < 5.0e-5
        and abs(static["residues"][-1] - 2.0) < 0.02
        and static["nonmetric"][0] < 5.0e-6
        and static["nonmetric"][-1] < 5.0e-3
        and max(static["solve"]) < 2.0e-10,
        "k^2h_tt=" + ",".join(f"{item:.9f}" for item in static["residues"])
        + "; nonmetric=" + ",".join(f"{item:.3e}" for item in static["nonmetric"]),
    )

    checks.check(
        "F-coefficient-selection-countermodel",
        "mu and two-mu pass the structural/source gates but differ on one conserved Record-source curvature-response norm",
        0.17 < source.selection_ratio < 0.19
        and mutation != "note_scope",
        f"L=5, d=+x, mode=(1,1,0,4) relative curvature-response norm drop={source.selection_ratio:.9f}",
    )

    ir_data = tuple(
        temporal_carrier(union, size, IR_WAVE_NUMBER, MU, mutation)
        for size in TIME_SIZES
    )
    hostile_wave = IR_WAVE_NUMBER if mutation == "replace_hostile_by_ir" else HOSTILE_WAVE_NUMBER
    hostile_data = tuple(
        temporal_carrier(union, size, hostile_wave, MU, mutation)
        for size in TIME_SIZES
    )
    all_carriers = ir_data + hostile_data
    checks.check(
        "G-local-same-time-tt-observable-interface",
        "the plus and cross edge combinations are exactly gauge invariant and the quotient calculation is stable",
        max(item.maximum_gauge_overlap for item in all_carriers) < 1.0e-13
        and max(item.maximum_reflection_overlap for item in all_carriers) < 1.0e-13
        and max(item.maximum_ward for item in all_carriers) < 2.0e-12
        and max(item.maximum_hermiticity for item in all_carriers) < 2.0e-12
        and max(item.maximum_bordered_error for item in all_carriers) < 2.0e-12
        and min(item.minimum_quotient_gap for item in all_carriers) > 2.0e-3
        and all(item.quotient_inertias == ((4, 14, 0),) for item in all_carriers),
        f"gauge={max(item.maximum_gauge_overlap for item in all_carriers):.3e}; reflection={max(item.maximum_reflection_overlap for item in all_carriers):.3e}; bordered={max(item.maximum_bordered_error for item in all_carriers):.3e}; gap={min(item.minimum_quotient_gap for item in all_carriers):.3e}; inertias={sorted(set(item.quotient_inertias for item in all_carriers))}",
    )

    convergence = max(
        float(np.max(np.abs(data[-1].moments[observable][:9] - data[-2].moments[observable][:9])))
        for data in (ir_data, hostile_data)
        for observable in range(2)
    )
    checks.check(
        "H-temporal-carrier-convergence",
        "the first nine local-observable moments converge across the two finest temporal carriers",
        convergence < 1.0e-9,
        f"maximum N=1024 to N=2048 moment change={convergence:.3e}",
    )

    ir = ir_data[-1]
    one_step_shifted = tuple(
        hankel_minimum(moments, step=1, order=2, shift=1)
        for moments in ir.moments
    )
    checks.check(
        "I-one-step-positive-transfer-killed",
        "the shifted Stieltjes Hankel condition is negative for both local TT observables at k=0.4",
        one_step_shifted[0] < -1.0e-6
        and one_step_shifted[1] < -1.0e-4,
        f"shifted one-step minima plus={one_step_shifted[0]:.9e}, cross={one_step_shifted[1]:.9e}",
    )

    ir_two_step = tuple(
        (
            hankel_minimum(moments, step=2, order=2, shift=0),
            hankel_minimum(moments, step=2, order=2, shift=1),
        )
        for moments in ir.moments
    )
    checks.check(
        "J-infrared-two-step-escape-retained",
        "the first unshifted and shifted two-step tests are positive at k=0.4, so the hostile test is load bearing",
        min(value for pair in ir_two_step for value in pair) > 1.0e-10,
        f"IR two-step minima plus={ir_two_step[0]}, cross={ir_two_step[1]}",
    )

    hostile = hostile_data[-1]
    hostile_two_step = tuple(
        (
            hankel_minimum(moments, step=2, order=3, shift=0),
            hankel_minimum(moments, step=2, order=2, shift=1),
        )
        for moments in hostile.moments
    )
    tuning_rows = []
    for mu in (HALF_MU, MU, RIVAL_MU):
        datum = temporal_carrier(union, TIME_SIZES[-1], hostile_wave, mu, mutation)
        tuning_rows.append(
            tuple(
                hankel_minimum(moments, step=2, order=3, shift=0)
                for moments in datum.moments
            )
        )
    checks.check(
        "K-two-step-full-zone-transfer-killed",
        "the apparent infrared two-step escape has a stable negative half-space Gram at k=pi/2 for both TT observables",
        hostile_two_step[0][0] < -3.0e-7
        and hostile_two_step[1][0] < -5.0e-8
        and hostile_two_step[1][1] < -3.0e-7
        and all(row[0] < -3.0e-7 for row in tuning_rows)
        and all(row[1] < -1.0e-9 for row in tuning_rows),
        f"hostile plus={hostile_two_step[0]}, cross={hostile_two_step[1]}; half/base/double unshifted={tuning_rows}",
    )

    checks.check(
        "L-no-go-discipline-and-axiom-boundary",
        "the narrow one/two-step retirement passes N1-N8 while longer-block, boundary, canonical, and connection routes remain live",
        all(f"n{index} —" in note for index in range(1, 9))
        and all(
            phrase in note
            for phrase in (
                "longer blocking",
                "boundary term",
                "canonical constraint reduction",
                "connection/holonomy",
                "no canonical axiom is edited",
                "zero toe percentage movement",
            )
        )
        and mutation != "note_scope",
    )

    print(
        "N5_CERTIFICATE: 22 reflected edges, 3 local curvature rows, 10 common metric modes, 3 relative shifts, 4 gauge nulls, 6,528 Record-source modes, 6 static residues, 2 local TT observables, 4 temporal carriers, 2 momenta, and 3 mu values are resolved"
    )
    print(
        "per_element: every coefficient of the three reflected curvature rows, both local same-time TT edge observables, and every source/response vector enters the checks"
    )
    print(
        "per_site: the finite-range original-plus-reflected unit-cell action and its transverse same-time y-z edge combinations are executed without a metric-only projection"
    )
    print(
        "per_mode: every supported Block-68 source mode on periodic L=3 through L=8 is solved; temporal moments use k=0.4 and the hostile k=pi/2"
    )
    print(
        "per_block: exact 13-to-10 fiber reduction, Ward/reflection, source range, Newton residue, coefficient rivalry, and one/two-step Stieltjes gates are composed"
    )
    print(
        "lattice_wide: full temporal-frequency circles are integrated on four carrier sizes, but no full-Z3 phase, nonlinear solved branch, longer-block transfer, or selected Record clock is claimed"
    )
    print(
        "scope_boundary: constructive local source/common-metric action plus a narrow one- and two-slice physical-transfer obstruction; not gravity failure, all-cadence failure, axiom adoption, retention, or TOE closure"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
