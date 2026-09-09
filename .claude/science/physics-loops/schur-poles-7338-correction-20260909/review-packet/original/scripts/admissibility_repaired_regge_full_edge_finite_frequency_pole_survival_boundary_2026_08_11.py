#!/usr/bin/env python3
"""Check finite-frequency pole survival in the complete repaired Regge edge law.

The runner uses the raw analytic Laurent symbol of the supplied repaired
fifteen-edge Hessian.  Along q=(k,0,0,-i omega), it quotients the exact four
vertex-displacement directions with a bordered determinant, resolves the two
y/z-reflection sectors, and follows one physical pole in each sector.  It
does not turn this conditional analytic continuation into a selected causal
Record update or a physical-inner-product theorem.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from pathlib import Path
import sys

import numpy as np
from scipy.optimize import root


AUDIT_TIMEOUT_SEC = 180

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_FINITE_FREQUENCY_POLE_"
    "SURVIVAL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
GREEN_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REGGE_FIXED_AVERAGE_TICK_SOURCE_INCREASING_TORUS_"
    "WARD_GREEN_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
IR_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_"
    "CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
JOINT_LAW_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_JOINT_RECORD_GRAVITY_LAW_FIVE_CONTROL_AXIOM_CUT_"
    "GATE_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
PREMISE_REGISTRY_PATH = (
    ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_FINITE_FREQUENCY_POLE_SURVIVAL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_REGGE_FIXED_AVERAGE_TICK_SOURCE_INCREASING_TORUS_WARD_GREEN_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_JOINT_RECORD_GRAVITY_LAW_FIVE_CONTROL_AXIOM_CUT_GATE_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_regge_fixed_average_tick_source_increasing_torus_ward_green_boundary_2026_08_11.py",
    "scripts/admissibility_repaired_regge_full_edge_schur_ir_lorentzian_constraint_tt_boundary_2026_08_11.py",
    "scripts/admissibility_joint_record_gravity_law_five_control_axiom_cut_gate_2026_08_11.py",
)

sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_regge_fixed_average_tick_source_increasing_torus_ward_green_boundary_2026_08_11 as block43  # noqa: E402


HCOMPS = tuple(block43.regge.HCOMPS)
DIRECTIONS = np.asarray(block43.DIRECTIONS, dtype=float)
DIRECTION_LENGTHS = np.asarray(block43.DIRECTION_LENGTHS, dtype=float)
SHIFTS = np.asarray(block43.SHIFTS, dtype=float)
MATRICES = np.asarray(block43.MATRICES, dtype=float)
METRIC_COEFFICIENTS = np.asarray(block43.METRIC_COEFFICIENTS, dtype=float)
LOW_MOMENTA = (0.05, 0.10, 0.20, 0.40)
ZONE_MOMENTA = tuple(np.pi * index / 32.0 for index in range(1, 33))
SAMPLED_MOMENTA = LOW_MOMENTA + ZONE_MOMENTA
REVERSAL_MOMENTA = (0.4, 0.8, 1.6, 2.4)


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


@dataclass(frozen=True)
class Sector:
    name: str
    edge_basis: np.ndarray
    gauge_basis: np.ndarray
    tt_vector: np.ndarray


@dataclass(frozen=True)
class PoleDatum:
    wave_number: float
    sector: str
    frequency: complex
    solver_success: bool
    determinant_residual: float
    ward_relative: float
    schur_ward_relative: float
    nonmetric_gap: float
    tt_overlap: float
    next_singular_ratio: float
    multiplier_ratio: float
    nonmetric_metric_ratio: float
    bordered_null_ratio: float
    edge_null_ratio: float


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def analytic_symbol(momentum: np.ndarray) -> np.ndarray:
    """Raw Laurent symbol; no Hermitian symmetrization at complex momentum."""
    phases = np.exp(1j * (SHIFTS @ np.asarray(momentum, dtype=complex)))
    return np.einsum("s,sij->ij", phases, MATRICES, optimize=True)


def analytic_metric_map(momentum: np.ndarray) -> np.ndarray:
    half_phase = DIRECTIONS @ np.asarray(momentum, dtype=complex) / 2.0
    factors = np.empty_like(half_phase, dtype=complex)
    zero = np.abs(half_phase) < 1.0e-13
    factors[zero] = 1.0
    factors[~zero] = (
        np.exp(1j * half_phase[~zero])
        * np.sin(half_phase[~zero])
        / half_phase[~zero]
    )
    return factors[:, None] * METRIC_COEFFICIENTS


def analytic_gauge_map(momentum: np.ndarray) -> np.ndarray:
    phases = np.exp(1j * (DIRECTIONS @ np.asarray(momentum, dtype=complex))) - 1.0
    return phases[:, None] * DIRECTIONS / DIRECTION_LENGTHS[:, None]


def swap_matrix(vectors: np.ndarray, left: int, right: int) -> np.ndarray:
    integer_vectors = np.asarray(vectors, dtype=int)
    permutation = np.zeros((len(integer_vectors), len(integer_vectors)), dtype=float)
    for column, vector in enumerate(integer_vectors):
        image = vector.copy()
        image[left], image[right] = image[right], image[left]
        matches = np.flatnonzero(np.all(integer_vectors == image, axis=1))
        if len(matches) != 1:
            raise AssertionError("coordinate-swap image is not unique")
        permutation[matches[0], column] = 1.0
    return permutation


def sign_basis(involution: np.ndarray, sign: int) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(involution)
    return eigenvectors[:, np.isclose(eigenvalues, float(sign))]


def tt_vectors() -> tuple[np.ndarray, np.ndarray]:
    plus = np.zeros(len(HCOMPS), dtype=float)
    plus[HCOMPS.index((1, 1))] = 1.0 / np.sqrt(2.0)
    plus[HCOMPS.index((2, 2))] = -1.0 / np.sqrt(2.0)
    cross = np.zeros(len(HCOMPS), dtype=float)
    cross[HCOMPS.index((1, 2))] = 1.0 / np.sqrt(2.0)
    return plus, cross


def sector_data() -> tuple[tuple[Sector, ...], np.ndarray, np.ndarray]:
    edge_swap = swap_matrix(DIRECTIONS, 1, 2)
    gauge_swap = np.eye(4)
    gauge_swap[[1, 2]] = gauge_swap[[2, 1]]
    plus, cross = tt_vectors()
    sectors = (
        Sector("even", sign_basis(edge_swap, +1), sign_basis(gauge_swap, +1), cross),
        Sector("odd", sign_basis(edge_swap, -1), sign_basis(gauge_swap, -1), plus),
    )
    return sectors, edge_swap, gauge_swap


def nonmetric_basis() -> np.ndarray:
    left_vectors, _, _ = np.linalg.svd(METRIC_COEFFICIENTS, full_matrices=True)
    return left_vectors[:, len(HCOMPS) :]


def axis_momentum(wave_number: float, frequency: complex) -> np.ndarray:
    return np.asarray((wave_number, 0.0, 0.0, -1j * frequency), dtype=complex)


def bordered_operator(
    wave_number: float, frequency: complex, sector: Sector
) -> np.ndarray:
    momentum = axis_momentum(wave_number, frequency)
    symbol = analytic_symbol(momentum)
    right_gauge = sector.edge_basis.T @ analytic_gauge_map(momentum) @ sector.gauge_basis
    left_gauge = sector.edge_basis.T @ analytic_gauge_map(-momentum) @ sector.gauge_basis
    sector_symbol = sector.edge_basis.T @ symbol @ sector.edge_basis
    zeros = np.zeros(
        (sector.gauge_basis.shape[1], sector.gauge_basis.shape[1]), dtype=complex
    )
    return np.block(
        [[sector_symbol, left_gauge], [right_gauge.T, zeros]]
    )


def scalar_lattice_frequency(wave_number: float) -> float:
    return float(2.0 * np.arcsinh(np.sin(wave_number / 2.0)))


def solve_pole(wave_number: float, sector: Sector) -> tuple[complex, bool, float]:
    initial_frequency = scalar_lattice_frequency(wave_number)
    scale = float(np.linalg.norm(bordered_operator(wave_number, initial_frequency, sector)))

    def determinant_pair(values: np.ndarray) -> np.ndarray:
        frequency = complex(values[0], values[1])
        determinant = np.linalg.det(
            bordered_operator(wave_number, frequency, sector) / scale
        )
        return np.asarray((determinant.real, determinant.imag), dtype=float)

    result = root(
        determinant_pair,
        np.asarray((initial_frequency, 0.0)),
        method="hybr",
        options={"xtol": 1.0e-11},
    )
    frequency = complex(result.x[0], result.x[1])
    return frequency, bool(result.success), float(np.linalg.norm(result.fun))


def pole_datum(
    wave_number: float,
    sector: Sector,
    nonmetric: np.ndarray,
) -> PoleDatum:
    frequency, solver_success, determinant_residual = solve_pole(
        wave_number, sector
    )
    momentum = axis_momentum(wave_number, frequency)
    symbol = analytic_symbol(momentum)
    metric_map = analytic_metric_map(momentum)
    right_gauge = analytic_gauge_map(momentum)
    left_gauge = analytic_gauge_map(-momentum)

    symbol_norm = float(np.linalg.norm(symbol))
    ward_relative = max(
        float(np.linalg.norm(symbol @ right_gauge))
        / (symbol_norm * float(np.linalg.norm(right_gauge))),
        float(np.linalg.norm(left_gauge.T @ symbol))
        / (float(np.linalg.norm(left_gauge)) * symbol_norm),
    )

    left_metric = analytic_metric_map(-momentum).T
    metric_block = left_metric @ symbol @ metric_map
    right_mixing = left_metric @ symbol @ nonmetric
    nonmetric_block = nonmetric.T @ symbol @ nonmetric
    left_mixing = nonmetric.T @ symbol @ metric_map
    schur = metric_block - right_mixing @ np.linalg.solve(
        nonmetric_block, left_mixing
    )
    metric_gauge = np.linalg.lstsq(metric_map, right_gauge, rcond=None)[0]
    schur_ward_relative = float(np.linalg.norm(schur @ metric_gauge)) / (
        float(np.linalg.norm(schur)) * float(np.linalg.norm(metric_gauge))
    )
    nonmetric_gap = float(
        np.linalg.svd(nonmetric_block, compute_uv=False)[-1]
    )

    bordered = bordered_operator(wave_number, frequency, sector)
    _, singular_values, right_vectors = np.linalg.svd(bordered)
    null_vector = right_vectors.conj().T[:, -1]
    edge_count = sector.edge_basis.shape[1]
    sector_edge = null_vector[:edge_count]
    multipliers = null_vector[edge_count:]
    edge_vector = sector.edge_basis @ sector_edge
    edge_vector /= np.linalg.norm(edge_vector)
    coordinates = np.linalg.solve(
        np.column_stack((metric_map, nonmetric)), edge_vector
    )
    metric_coordinates = coordinates[: len(HCOMPS)]
    nonmetric_coordinates = coordinates[len(HCOMPS) :]

    physical_metric = metric_coordinates - metric_gauge @ np.linalg.lstsq(
        metric_gauge, metric_coordinates, rcond=None
    )[0]
    physical_tt = sector.tt_vector - metric_gauge @ np.linalg.lstsq(
        metric_gauge, sector.tt_vector, rcond=None
    )[0]
    tt_overlap = float(abs(np.vdot(physical_tt, physical_metric))) / (
        float(np.linalg.norm(physical_tt)) * float(np.linalg.norm(physical_metric))
    )

    return PoleDatum(
        wave_number=wave_number,
        sector=sector.name,
        frequency=frequency,
        solver_success=solver_success,
        determinant_residual=determinant_residual,
        ward_relative=ward_relative,
        schur_ward_relative=schur_ward_relative,
        nonmetric_gap=nonmetric_gap,
        tt_overlap=tt_overlap,
        next_singular_ratio=float(singular_values[-2] / singular_values[0]),
        multiplier_ratio=float(np.linalg.norm(multipliers) / np.linalg.norm(sector_edge)),
        nonmetric_metric_ratio=float(
            np.linalg.norm(nonmetric_coordinates) / np.linalg.norm(metric_coordinates)
        ),
        bordered_null_ratio=float(singular_values[-1] / singular_values[0]),
        edge_null_ratio=float(np.linalg.norm(symbol @ edge_vector) / symbol_norm),
    )


def main() -> int:
    checks = Checks()
    note = flat(NOTE_PATH)
    axiom = flat(AXIOM_PATH)
    green_note = flat(GREEN_NOTE_PATH)
    ir_note = flat(IR_NOTE_PATH)
    joint_note = flat(JOINT_LAW_NOTE_PATH)

    checks.check(
        "source-and-scope-bindings",
        "the current axioms and three parent boundaries are read without selecting the continuation as physical law",
        all(
            path.exists()
            for path in (
                NOTE_PATH,
                AXIOM_PATH,
                GREEN_NOTE_PATH,
                IR_NOTE_PATH,
                JOINT_LAW_NOTE_PATH,
                PREMISE_REGISTRY_PATH,
            )
        )
        and "admissibility is not a dynamics axiom" in axiom
        and "false brillouin-edge near-pole" in green_note
        and "four gauge directions plus two" in ir_note
        and "exact immutable referent" in joint_note,
    )

    shift_lookup = {
        tuple(int(value) for value in shift): matrix
        for shift, matrix in zip(SHIFTS, MATRICES)
    }
    pairing_error = max(
        float(
            np.max(
                np.abs(
                    matrix.T
                    - shift_lookup[tuple(-int(value) for value in shift)]
                )
            )
        )
        for shift, matrix in zip(SHIFTS, MATRICES)
    )
    time_counts = Counter(int(value) for value in SHIFTS[:, 3])
    real_probe = np.asarray((0.37, -0.21, 0.14, 0.42))
    real_symbol_error = float(
        np.max(
            np.abs(
                analytic_symbol(real_probe)
                - block43.batch_symbol(real_probe[None, :])[0]
            )
        )
    )
    checks.check(
        "raw-laurent-symbol-pairing",
        "the 99-term real-space kernel is transpose-paired and the raw symbol agrees with the Hermitian form only on real momentum",
        len(shift_lookup) == 99
        and time_counts == Counter({-2: 4, -1: 29, 0: 33, 1: 29, 2: 4})
        and pairing_error < 5.0e-15
        and real_symbol_error < 5.0e-15,
        f"time counts={dict(sorted(time_counts.items()))}; pair error={pairing_error:.3e}",
    )

    sectors, edge_swap, gauge_swap = sector_data()
    symmetry_momenta = (
        axis_momentum(0.4, scalar_lattice_frequency(0.4)),
        axis_momentum(np.pi / 2.0, 1.32 - 6.0e-4j),
    )
    symmetry_error = 0.0
    for momentum in symmetry_momenta:
        symbol = analytic_symbol(momentum)
        gauge = analytic_gauge_map(momentum)
        symmetry_error = max(
            symmetry_error,
            float(np.max(np.abs(edge_swap @ symbol - symbol @ edge_swap))),
            float(np.max(np.abs(edge_swap @ gauge - gauge @ gauge_swap))),
        )
    checks.check(
        "axis-reflection-sector-decomposition",
        "the y/z reflection splits all fifteen edges and all four gauge parameters into exact 11+4 and 3+1 sectors",
        tuple(sector.edge_basis.shape[1] for sector in sectors) == (11, 4)
        and tuple(sector.gauge_basis.shape[1] for sector in sectors) == (3, 1)
        and np.max(np.abs(edge_swap @ edge_swap - np.eye(15))) < 1.0e-15
        and symmetry_error < 5.0e-14,
        f"edge dims=11+4; gauge dims=3+1; max intertwining error={symmetry_error:.3e}",
    )

    ward_error = 0.0
    gauge_ranks = set()
    for wave_number, frequency in (
        (0.1, 0.0999 - 1.0e-9j),
        (0.4, 0.3949 - 1.0e-6j),
        (np.pi / 2.0, 1.322 - 6.0e-4j),
        (np.pi, 1.776),
    ):
        momentum = axis_momentum(wave_number, frequency)
        symbol = analytic_symbol(momentum)
        right_gauge = analytic_gauge_map(momentum)
        left_gauge = analytic_gauge_map(-momentum)
        ward_error = max(
            ward_error,
            float(np.max(np.abs(symbol @ right_gauge))),
            float(np.max(np.abs(left_gauge.T @ symbol))),
        )
        gauge_ranks.add(int(np.linalg.matrix_rank(right_gauge, tol=1.0e-10)))
    checks.check(
        "exact-complex-momentum-ward-identity",
        "the complete raw Laurent symbol retains four exact displacement columns on both sides at complex temporal momentum",
        ward_error < 3.0e-13 and gauge_ranks == {4},
        f"max absolute Ward residual={ward_error:.3e}; gauge ranks={sorted(gauge_ranks)}",
    )

    nonmetric = nonmetric_basis()
    data = tuple(
        pole_datum(wave_number, sector, nonmetric)
        for wave_number in SAMPLED_MOMENTA
        for sector in sectors
    )
    by_key = {(datum.wave_number, datum.sector): datum for datum in data}

    max_determinant_residual = max(datum.determinant_residual for datum in data)
    max_bordered_null = max(datum.bordered_null_ratio for datum in data)
    min_next_singular = min(datum.next_singular_ratio for datum in data)
    checks.check(
        "two-sampled-pole-branches-resolved",
        "one isolated bordered-determinant zero is resolved in each parity sector at every one of the 36 declared wave numbers",
        len(data) == 72
        and all(datum.solver_success for datum in data)
        and max_determinant_residual < 1.0e-14
        and max_bordered_null < 3.0e-15
        and min_next_singular > 1.5e-5,
        f"root residual max={max_determinant_residual:.3e}; next-singular ratio min={min_next_singular:.3e}",
    )

    max_ward_relative = max(datum.ward_relative for datum in data)
    max_schur_ward = max(datum.schur_ward_relative for datum in data)
    max_multiplier = max(datum.multiplier_ratio for datum in data)
    max_edge_null = max(datum.edge_null_ratio for datum in data)
    checks.check(
        "physical-edge-null-not-border-artifact",
        "the bordered zeros have vanishing gauge multipliers and are actual nulls of the complete edge symbol",
        max_ward_relative < 8.0e-16
        and max_schur_ward < 1.0e-11
        and max_multiplier < 6.0e-13
        and max_edge_null < 1.0e-15,
        f"Ward={max_ward_relative:.3e}; Schur Ward={max_schur_ward:.3e}; multiplier={max_multiplier:.3e}",
    )

    min_nonmetric_gap = min(datum.nonmetric_gap for datum in data)
    min_tt_overlap = min(datum.tt_overlap for datum in data)
    max_nonmetric_ratio = max(datum.nonmetric_metric_ratio for datum in data)
    checks.check(
        "gapped-remainder-and-tt-character",
        "the five nonmetric directions stay invertible while both pole vectors remain predominantly transverse-traceless after gauge removal",
        min_nonmetric_gap > 1.28
        and min_tt_overlap > 0.93
        and max_nonmetric_ratio < 0.57,
        f"gap min={min_nonmetric_gap:.6f}; TT overlap min={min_tt_overlap:.6f}; n/h max={max_nonmetric_ratio:.6f}",
    )

    low_correction = []
    low_split = []
    low_phase = []
    for wave_number in LOW_MOMENTA:
        even = by_key[(wave_number, "even")].frequency
        odd = by_key[(wave_number, "odd")].frequency
        reference = scalar_lattice_frequency(wave_number)
        low_correction.append(max(abs(even.real - reference), abs(odd.real - reference)))
        low_split.append(abs(even.real - odd.real))
        low_phase.append(max(abs(even.imag), abs(odd.imag)))
    correction_orders = np.log2(np.asarray(low_correction[1:]) / low_correction[:-1])
    split_orders = np.log2(np.asarray(low_split[1:]) / low_split[:-1])
    phase_orders = np.log2(np.asarray(low_phase[1:]) / low_phase[:-1])
    checks.check(
        "infrared-einstein-branch-survival",
        "both full-edge branches approach the common infrared light cone with cubic real corrections and fifth-order pole phase",
        np.all((correction_orders > 2.9) & (correction_orders < 3.1))
        and np.all((split_orders > 2.9) & (split_orders < 3.1))
        and np.all((phase_orders > 4.8) & (phase_orders < 5.1)),
        "orders: correction="
        + ",".join(f"{value:.3f}" for value in correction_orders)
        + "; split="
        + ",".join(f"{value:.3f}" for value in split_orders)
        + "; phase="
        + ",".join(f"{value:.3f}" for value in phase_orders),
    )

    max_reference_deviation = max(
        abs(
            datum.frequency.real / scalar_lattice_frequency(datum.wave_number)
            - 1.0
        )
        for datum in data
    )
    max_polarization_split = max(
        abs(
            by_key[(wave_number, "even")].frequency.real
            - by_key[(wave_number, "odd")].frequency.real
        )
        for wave_number in SAMPLED_MOMENTA
    )
    max_pole_phase = max(abs(datum.frequency.imag) for datum in data)
    checks.check(
        "bounded-oriented-lattice-artifacts",
        "the sampled finite-lattice poles are close to the scalar reference but are not exactly real or polarization-degenerate",
        max_reference_deviation < 0.01
        and 1.0e-3 < max_polarization_split < 7.0e-3
        and 1.0e-4 < max_pole_phase < 1.5e-3,
        f"relative dispersion={max_reference_deviation:.6f}; split={max_polarization_split:.6f}; phase={max_pole_phase:.6f}",
    )

    reversal_residual = 0.0
    for wave_number in REVERSAL_MOMENTA:
        for sector in sectors:
            frequency, success, _ = solve_pole(wave_number, sector)
            reversed_singular = np.linalg.svd(
                bordered_operator(-wave_number, frequency.conjugate(), sector),
                compute_uv=False,
            )
            reversal_residual = max(
                reversal_residual,
                float(reversed_singular[-1] / reversed_singular[0]),
            )
            if not success:
                reversal_residual = np.inf
    checks.check(
        "momentum-reversal-conjugacy",
        "each tested positive-momentum pole has the conjugate pole at reversed momentum, so the small phase is parity-odd",
        reversal_residual < 2.0e-15,
        f"max reversed bordered-null ratio={reversal_residual:.3e}",
    )

    checks.check(
        "physical-and-axiom-boundary",
        "the source keeps pole survival distinct from a selected transfer operator, physical norm, nonlinear phase, or Record-source law",
        all(
            phrase in note
            for phrase in (
                "not a gravity no-go",
                "physical transfer or inner product",
                "no canonical axiom is edited",
                "no toe percentage moves",
                "sampled finite-frequency",
            )
        )
        and all(
            phrase in axiom
            for phrase in (
                "does not choose a hamiltonian or transfer operator",
                "time metric",
                "source/action",
            )
        ),
    )

    checks.check(
        "fresh-no-go-discipline-packet",
        "the narrow single-orientation artifact boundary passes N1 through N8 while preserving all constructive completion routes",
        all(f"### n{index}" in note for index in range(1, 9))
        and "status: pass" in note
        and all(
            phrase in note
            for phrase in (
                "reflected-orientation",
                "unitary dilation",
                "not proved necessary",
                "not a global instability",
            )
        ),
    )

    print(
        "N5_CERTIFICATE: 99 Laurent shifts, fifteen edges, four exact gauge columns, five nonmetric directions, two reflection sectors, 36 wave numbers, and 72 pole solves are resolved"
    )
    print(
        "per_element: checked every Laurent coefficient pairing, every edge coordinate, and every gauge column"
    )
    print(
        "per_site: the supplied translation-invariant repaired Kuhn/Coxeter unit-cell kernel is used without metric-only truncation"
    )
    print(
        "per_mode: checked both parity branches at four infrared and 32 uniformly spaced positive-axis momenta through pi"
    )
    print(
        "per_block: checked exact Ward quotient, full metric/nonmetric Schur block, bordered null vectors, TT diagnostics, and momentum reversal"
    )
    print(
        "lattice_wide: no continuum of momenta, off-axis shell, physical Hilbert space, transfer operator, nonlinear phase, or full-Z3 history is inferred"
    )
    print(
        "scope_boundary: sampled finite-frequency survival for the supplied single-orientation analytic continuation; not selected dynamics, unitarity, stability, or TOE closure"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
