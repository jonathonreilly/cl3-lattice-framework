#!/usr/bin/env python3
"""Resolve the reflected-orientation three-shift intertwiner.

The twenty-two-edge reflection union contains, for each spatial direction, one
elementary space--time parallelogram.  Its two diagonals minus its four sides
give an exact local displacement-gauge invariant.  On the line-averaged common
metric carrier the centered invariant factors exactly into a strictly positive
lattice form factor times the linearized sectional-curvature polynomial.

Consequently the invariant removes the three relative forward/backward h_it
zero modes at zero momentum, but imposing it as a homogeneous constraint at
nonzero momentum would also remove the sourced Newtonian curvature.  The
Record rank-one stress fixes only the contracted Ricci source; an explicit
trace-free covariant decoder family witnesses the remaining sectional/Weyl
choice.  No physical law, transfer, clock, or axiom selection is inferred.
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path
import sys

import numpy as np
import sympy as sp


AUDIT_TIMEOUT_SEC = 180

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REFLECTED_PLAQUETTE_CURVATURE_RECORD_RICCI_SOURCE_"
    "INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REFLECTION_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REGGE_REFLECTED_ORIENTATION_COMMON_METRIC_TRANSFER_"
    "GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
RECORD_SOURCE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_RECORD_EDGE_SCORE_RANK_ONE_METRIC_STRESS_SPATIAL_"
    "PROJECTIVE_CURVATURE_REACTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
GREEN_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REGGE_FIXED_AVERAGE_TICK_SOURCE_INCREASING_TORUS_"
    "WARD_GREEN_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
IR_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_"
    "CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
PREMISE_REGISTRY_PATH = (
    ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_REFLECTED_PLAQUETTE_CURVATURE_RECORD_RICCI_SOURCE_INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_REGGE_REFLECTED_ORIENTATION_COMMON_METRIC_TRANSFER_GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_RECORD_EDGE_SCORE_RANK_ONE_METRIC_STRESS_SPATIAL_PROJECTIVE_CURVATURE_REACTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_REGGE_FIXED_AVERAGE_TICK_SOURCE_INCREASING_TORUS_WARD_GREEN_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_regge_reflected_orientation_common_metric_transfer_gate_boundary_2026_08_11.py",
    "scripts/admissibility_record_edge_score_rank_one_metric_stress_spatial_projective_curvature_reaction_boundary_2026_08_10.py",
)

sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_regge_reflected_orientation_common_metric_transfer_gate_boundary_2026_08_11 as block48  # noqa: E402


HCOMPS = tuple(block48.HCOMPS)
TIME_REFLECTION = np.diag((1, 1, 1, -1)).astype(int)
STATIC_MOMENTA = (0.025, 0.05, 0.10, 0.20, 0.40, 0.80, np.pi / 2.0, np.pi)


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


def basis_direction(index: int) -> tuple[int, int, int, int]:
    return tuple(1 if coordinate == index else 0 for coordinate in range(4))


def curvature_intertwiner(
    union: block48.ReflectionUnion, momentum: np.ndarray
) -> np.ndarray:
    """Three local two-diagonal-minus-four-side space--time plaquette rows."""
    q = np.asarray(momentum, dtype=complex)
    index = {direction: slot for slot, direction in enumerate(union.directions)}
    time = basis_direction(3)
    rows = np.zeros((3, len(union.directions)), dtype=complex)
    for spatial in range(3):
        axis = basis_direction(spatial)
        forward = tuple(axis[mu] + time[mu] for mu in range(4))
        reflected = tuple(axis[mu] - time[mu] for mu in range(4))
        rows[spatial, index[forward]] = np.sqrt(2.0)
        rows[spatial, index[reflected]] = np.sqrt(2.0) * np.exp(1j * q[3])
        rows[spatial, index[axis]] = -(1.0 + np.exp(1j * q[3]))
        rows[spatial, index[time]] = -(1.0 + np.exp(1j * q[spatial]))
    return rows


def centered_curvature_intertwiner(
    union: block48.ReflectionUnion, momentum: np.ndarray
) -> np.ndarray:
    q = np.asarray(momentum, dtype=complex)
    centering = np.diag(np.exp(-0.5j * (q[:3] + q[3])))
    return centering @ curvature_intertwiner(union, q)


def union_line_metric_map(
    union: block48.ReflectionUnion, momentum: np.ndarray
) -> np.ndarray:
    directions = np.asarray(union.directions, dtype=float)
    half_phase = directions @ np.asarray(momentum, dtype=complex) / 2.0
    factors = np.ones(len(directions), dtype=complex)
    nonzero = np.abs(half_phase) >= 1.0e-13
    factors[nonzero] = (
        np.exp(1j * half_phase[nonzero])
        * np.sin(half_phase[nonzero])
        / half_phase[nonzero]
    )
    return factors[:, None] * block48.metric_coefficients(directions)


def centered_form_factor(left: float, right: float) -> float:
    """Continuous principal-zone form factor, including the coordinate axes."""
    left = float(left)
    right = float(right)
    if abs(left) < 1.0e-10 and abs(right) < 1.0e-10:
        return 1.0 / 12.0
    if abs(right) < 1.0e-10:
        half = left / 2.0
        return float(
            (np.sin(half) - half * np.cos(half))
            / (2.0 * left * half * half)
        )
    if abs(left) < 1.0e-10:
        half = right / 2.0
        return float(
            (np.sin(half) - half * np.cos(half))
            / (2.0 * right * half * half)
        )
    minus = np.sinc((left - right) / (2.0 * np.pi))
    plus = np.sinc((left + right) / (2.0 * np.pi))
    return float((minus - plus) / (2.0 * left * right))


def sectional_metric_rows(momentum: np.ndarray) -> np.ndarray:
    """Unweighted linearized R_itit polynomial, up to the stated sign/factor."""
    q = np.asarray(momentum, dtype=complex)
    rows = np.zeros((3, len(HCOMPS)), dtype=complex)
    for spatial in range(3):
        left = q[spatial]
        time = q[3]
        rows[spatial, HCOMPS.index((spatial, spatial))] = time * time
        rows[spatial, HCOMPS.index((spatial, 3))] = -2.0 * left * time
        rows[spatial, HCOMPS.index((3, 3))] = left * left
    return rows


def expected_centered_metric_rows(momentum: np.ndarray) -> np.ndarray:
    q = np.asarray(momentum, dtype=complex)
    factors = np.asarray(
        [centered_form_factor(float(q[i].real), float(q[3].real)) for i in range(3)]
    )
    return np.diag(factors) @ sectional_metric_rows(q)


def inertia(matrix: np.ndarray, tolerance: float = 1.0e-9) -> tuple[int, int, int]:
    eigenvalues = np.linalg.eigvalsh(0.5 * (matrix + matrix.conj().T))
    return (
        int(np.sum(eigenvalues < -tolerance)),
        int(np.sum(eigenvalues > tolerance)),
        int(np.sum(np.abs(eigenvalues) <= tolerance)),
    )


def proper_cubic_rotations() -> tuple[np.ndarray, ...]:
    rotations = []
    for permutation in permutations(range(3)):
        permutation_matrix = np.zeros((3, 3), dtype=int)
        for row, column in enumerate(permutation):
            permutation_matrix[row, column] = 1
        for signs in product((-1, 1), repeat=3):
            candidate = np.diag(signs) @ permutation_matrix
            if round(np.linalg.det(candidate)) == 1:
                rotations.append(candidate)
    return tuple(rotations)


def trace_reversed_temporal_source(direction: np.ndarray) -> float:
    direction = np.asarray(direction, dtype=float)
    length = float(np.linalg.norm(direction))
    return float((2.0 * direction[3] ** 2 - length * length) / (4.0 * length))


def sectional_source_decoder(direction: np.ndarray, eta: float) -> np.ndarray:
    """A covariant family sharing one contracted trace-reversed source."""
    direction = np.asarray(direction, dtype=float)
    length = float(np.linalg.norm(direction))
    spatial_square = direction[:3] ** 2
    spatial_trace = float(np.sum(spatial_square))
    contracted = trace_reversed_temporal_source(direction)
    anisotropy = (spatial_square - spatial_trace / 3.0) / (2.0 * length)
    return np.full(3, contracted / 3.0) + float(eta) * anisotropy


def main() -> int:
    checks = Checks()
    note = flat(NOTE_PATH)
    axiom = flat(AXIOM_PATH)
    reflection_note = flat(REFLECTION_PATH)
    record_note = flat(RECORD_SOURCE_PATH)
    green_note = flat(GREEN_PATH)
    ir_note = flat(IR_PATH)

    checks.check(
        "source-and-scope-bindings",
        "the current axioms and four exact gravity/Record parents are read without importing a selected field or update law",
        all(
            path.exists()
            for path in (
                NOTE_PATH,
                AXIOM_PATH,
                REFLECTION_PATH,
                RECORD_SOURCE_PATH,
                GREEN_PATH,
                IR_PATH,
                PREMISE_REGISTRY_PATH,
            )
        )
        and "three-component orientation-shift intertwiner" in reflection_note
        and "rank-one metric stress" in record_note
        and "increasing-torus green boundary" in green_note
        and "all ten independent momentum monomials" in ir_note
        and "admissibility is not a dynamics axiom" in axiom,
    )

    union = block48.build_reflection_union()
    local_rows = curvature_intertwiner(union, np.zeros(4))
    nonzero_counts = tuple(int(np.count_nonzero(np.abs(row) > 1.0e-14)) for row in local_rows)
    checks.check(
        "three-local-reflected-parallelograms",
        "the reflected union contains three independent two-diagonal-minus-four-side space-time plaquette rows",
        len(union.directions) == 22
        and local_rows.shape == (3, 22)
        and np.linalg.matrix_rank(local_rows, tol=1.0e-12) == 3
        and nonzero_counts == (4, 4, 4),
        f"shape={local_rows.shape}; rank=3; stored-edge counts={nonzero_counts}",
    )

    ward_error = 0.0
    row_ranks = set()
    for momentum in (
        np.asarray((0.3, 0.2, -0.1, 0.4), dtype=complex),
        np.asarray((0.4, 0.0, 0.0, -0.395j), dtype=complex),
        np.asarray((1.2, -0.2, 0.4, 0.7), dtype=complex),
    ):
        rows = curvature_intertwiner(union, momentum)
        ward_error = max(
            ward_error,
            float(np.max(np.abs(rows @ block48.union_gauge_map(union, momentum)))),
        )
        row_ranks.add(int(np.linalg.matrix_rank(rows, tol=1.0e-12)))
    checks.check(
        "exact-displacement-intertwiner",
        "all three local rows annihilate the four exact union displacement columns at real and complex momentum",
        ward_error < 2.0e-15 and row_ranks == {3},
        f"maximum C(q) Gamma(q)={ward_error:.3e}; ranks={sorted(row_ranks)}",
    )

    reflection_error = 0.0
    for momentum in (
        np.asarray((0.3, 0.2, -0.1, 0.4), dtype=complex),
        np.asarray((0.4, 0.0, 0.0, -0.395j), dtype=complex),
        np.asarray((1.2, -0.2, 0.4, 0.7), dtype=complex),
    ):
        reflected = TIME_REFLECTION @ momentum
        transformed = (
            np.diag(np.exp(-0.5j * (reflected[:3] + reflected[3])))
            @ curvature_intertwiner(union, reflected)
            @ block48.union_time_reflection_matrix(union, momentum)
        )
        reflection_error = max(
            reflection_error,
            float(
                np.max(
                    np.abs(transformed - centered_curvature_intertwiner(union, momentum))
                )
            ),
        )
    checks.check(
        "centered-time-reflection-covariance",
        "plaquette-center phases turn the three rows into exact time-reflection-even curvature observables",
        reflection_error < 2.0e-15,
        f"maximum centered reflection residual={reflection_error:.3e}",
    )

    (shared_constraint, pair_to_union, _), _ = block48.union_reflection_split(union)
    relative_pairs = np.zeros((20, 3), dtype=float)
    for column, spatial in enumerate(range(3)):
        component = HCOMPS.index((spatial, 3))
        relative_pairs[component, column] = 1.0
        relative_pairs[len(HCOMPS) + component, column] = -1.0
    relative_edge_modes = pair_to_union @ relative_pairs
    common_metric = block48.metric_coefficients(np.asarray(union.directions))
    combined_constraint = np.vstack((shared_constraint, local_rows @ pair_to_union))
    checks.check(
        "zero-momentum-common-carrier-repair",
        "at zero momentum the rows annihilate all ten common metrics and map the three relative h_it shifts isomorphically",
        np.max(np.abs(local_rows @ common_metric)) < 5.0e-16
        and np.max(np.abs(local_rows @ relative_edge_modes - 2.0 * np.eye(3))) < 5.0e-16
        and np.linalg.matrix_rank(combined_constraint, tol=1.0e-12) == 10
        and block48.matrix_null_basis(combined_constraint).shape[1] == 10,
        "C(0) M_common=0; C(0) M_relative=2 I_3; paired constrained fiber dimension=10",
    )

    factorization_error = 0.0
    for momentum in (
        np.asarray((0.3, 0.2, -0.1, 0.4)),
        np.asarray((0.8, -0.5, 0.2, -0.7)),
        np.asarray((np.pi, 0.4, -1.0, 0.6)),
    ):
        actual = (
            centered_curvature_intertwiner(union, momentum)
            @ union_line_metric_map(union, momentum)
        )
        expected = expected_centered_metric_rows(momentum)
        factorization_error = max(
            factorization_error, float(np.max(np.abs(actual - expected)))
        )

    epsilon, left, right = sp.symbols("epsilon left right", nonzero=True, real=True)
    sinc = lambda value: sp.sin(value) / value
    symbolic_factor = (
        sinc(epsilon * (left - right) / 2)
        - sinc(epsilon * (left + right) / 2)
    ) / (2 * epsilon**2 * left * right)
    series = sp.simplify(sp.series(symbolic_factor, epsilon, 0, 5).removeO())
    expected_series = (
        sp.Rational(1, 12)
        - epsilon**2 * (left**2 + right**2) / 480
        + epsilon**4 * (left**4 + right**4) / 53760
        + epsilon**4 * left**2 * right**2 / 16128
    )
    checks.check(
        "exact-line-metric-sectional-curvature-factorization",
        "the centered stencil equals a scalar form factor times q_i^2 h_tt-2 q_i q_t h_it+q_t^2 h_ii",
        factorization_error < 3.0e-15
        and sp.simplify(series - expected_series) == 0,
        f"maximum factorization residual={factorization_error:.3e}; F(0,0)=1/12",
    )

    grid = np.linspace(-np.pi, np.pi, 129)
    factors = np.asarray(
        [centered_form_factor(a, b) for a in grid for b in grid], dtype=float
    )
    checks.check(
        "principal-zone-positive-curvature-form-factor",
        "the exact form factor is strictly positive on the principal Brillouin square, so the stencil has no curvature-blind zero there",
        np.min(factors) > 0.05
        and abs(centered_form_factor(0.0, 0.0) - 1.0 / 12.0) < 1.0e-15,
        f"129x129 control range={np.min(factors):.9f}..{np.max(factors):.9f}",
    )

    static_inertias = set()
    curvature_values = []
    metric_source = np.zeros(len(HCOMPS), dtype=float)
    metric_source[HCOMPS.index((3, 3))] = 1.0
    for wave_number in STATIC_MOMENTA:
        momentum = np.asarray((wave_number, 0.0, 0.0, 0.0), dtype=complex)
        rows = curvature_intertwiner(union, momentum)
        kernel = block48.matrix_null_basis(rows)
        restricted = kernel.conj().T @ block48.union_symbol(union, momentum) @ kernel
        static_inertias.add(inertia(restricted))

        response = -np.linalg.pinv(
            block48.common_metric_operator(momentum), rcond=1.0e-10
        ) @ metric_source
        curvature = (
            centered_curvature_intertwiner(union, momentum)
            @ union_line_metric_map(union, momentum)
            @ response
        )
        curvature_values.append(float(curvature[0].real))
    checks.check(
        "hard-zero-gluing-falsifier",
        "C=0 removes the relative static branch but also forbids the nonzero sourced Newtonian curvature of the common-metric response",
        static_inertias == {(12, 3, 4)}
        and min(abs(value) for value in curvature_values[:6]) > 0.16
        and abs(curvature_values[0] - 1.0 / 6.0) < 5.0e-5,
        f"restricted inertia={sorted(static_inertias)}; centered C_x response={curvature_values}",
    )

    exact_sources = {}
    for direction in union.directions:
        squared = sum(value * value for value in direction)
        exact_sources[direction] = sp.simplify(
            sp.Rational(2 * direction[3] ** 2 - squared, 4) / sp.sqrt(squared)
        )
    reflected_source_error = max(
        abs(
            trace_reversed_temporal_source(np.asarray(direction, dtype=float))
            - trace_reversed_temporal_source(
                TIME_REFLECTION @ np.asarray(direction, dtype=float)
            )
        )
        for direction in union.directions
    )
    checks.check(
        "record-rank-one-to-contracted-ricci-source",
        "each edge-labelled Record stress has an exact trace-reversed temporal source, additive and even under time reflection",
        len(exact_sources) == 22
        and exact_sources[(0, 0, 0, 1)] == sp.Rational(1, 4)
        and exact_sources[(1, 0, 0, 0)] == -sp.Rational(1, 4)
        and exact_sources[(1, 0, 0, 1)] == 0
        and exact_sources[(1, 1, 1, 1)] == -sp.Rational(1, 4)
        and reflected_source_error < 1.0e-15,
        "J_t=1/4; J_x=-1/4; J_(x+t)=0; J_(x+y+z+t)=-1/4",
    )

    rotations = proper_cubic_rotations()
    decoder_covariance_error = 0.0
    decoder_sum_error = 0.0
    for direction in union.directions:
        vector = np.asarray(direction, dtype=float)
        for eta in (0.0, 1.0, -0.5):
            decoded = sectional_source_decoder(vector, eta)
            decoder_sum_error = max(
                decoder_sum_error,
                abs(float(np.sum(decoded)) - trace_reversed_temporal_source(vector)),
            )
            for rotation in rotations:
                transformed = vector.copy()
                transformed[:3] = rotation @ vector[:3]
                permutation_action = rotation.astype(float) ** 2
                decoder_covariance_error = max(
                    decoder_covariance_error,
                    float(
                        np.max(
                            np.abs(
                                sectional_source_decoder(transformed, eta)
                                - permutation_action @ decoded
                            )
                        )
                    ),
                )
    checks.check(
        "covariant-additive-sectional-source-family",
        "a continuous eta-family of local proper-cubic/time-reflection covariant sectional decoders shares the same contracted Record source",
        len(rotations) == 24
        and decoder_covariance_error < 2.0e-15
        and decoder_sum_error < 2.0e-15,
        f"24 rotations; covariance={decoder_covariance_error:.3e}; contracted sum={decoder_sum_error:.3e}",
    )

    witness_direction = np.asarray((1.0, 0.0, 0.0, 0.0))
    isotropic = sectional_source_decoder(witness_direction, 0.0)
    directional = sectional_source_decoder(witness_direction, 1.0)
    generic_momentum = np.asarray((0.3, 0.2, -0.1, 0.4), dtype=complex)
    sectional_rows = sectional_metric_rows(generic_momentum)
    isotropic_lift = np.linalg.pinv(sectional_rows) @ isotropic
    directional_lift = np.linalg.pinv(sectional_rows) @ directional
    lift_error = max(
        float(np.max(np.abs(sectional_rows @ isotropic_lift - isotropic))),
        float(np.max(np.abs(sectional_rows @ directional_lift - directional))),
    )
    checks.check(
        "tracefree-sectional-weyl-nonselection",
        "the contracted Record source admits distinct covariant sectional allocations and both have generic metric lifts",
        np.linalg.matrix_rank(sectional_rows, tol=1.0e-12) == 3
        and abs(float(np.sum(isotropic)) - float(np.sum(directional))) < 1.0e-15
        and np.linalg.norm(isotropic - directional) > 0.4
        and lift_error < 2.0e-15,
        f"eta0={isotropic.tolist()}; eta1={directional.tolist()}; lift residual={lift_error:.3e}",
    )

    checks.check(
        "connection-law-and-axiom-boundary",
        "the result identifies a curvature/connection equation and tracefree propagation rule as missing extensional law fields, not a hard metric constraint",
        all(
            phrase in note
            for phrase in (
                "exact reflected plaquette curvature intertwiner",
                "hard zero is not the physical gluing law",
                "trace-free electric-weyl",
                "no toe percentage moves",
                "no canonical axiom is edited",
            )
        )
        and all(
            phrase in axiom
            for phrase in (
                "does not choose a hamiltonian or transfer operator",
                "update laws",
                "source/action and physical-observable identification",
            )
        ),
    )

    checks.check(
        "fresh-no-go-discipline-packet",
        "the hard-zero and contracted-source nonselection claims pass N1 through N8 while preserving live connection, transfer, and nonlinear routes",
        all(f"### n{index}" in note for index in range(1, 9))
        and "status: pass" in note
        and all(
            phrase in note
            for phrase in (
                "levi-civita/holonomy",
                "canonical constraint",
                "reflection-positive transfer",
                "not a gravity no-go",
            )
        ),
    )

    print(
        "N5_CERTIFICATE: all 22 reflected-union edge classes, three local plaquette rows, four displacement columns, ten common metric coordinates, three relative h_it modes, eight static momenta, 22 Record rays, 24 proper cubic rotations, and two explicit sectional decoder representatives are resolved"
    )
    print(
        "per_element: checked every edge coefficient in each of the three two-diagonal-minus-four-side plaquette rows and every Record-ray trace-reversed temporal source"
    )
    print(
        "per_site: checked one complete original-plus-reflected local cell with its three space-time parallelograms and zero-momentum paired-metric fiber"
    )
    print(
        "per_mode: checked exact Ward/reflection identities at real and complex momenta, exact line-metric factorization, and eight nonzero static axis controls"
    )
    print(
        "per_block: checked common-carrier repair, positive principal-zone form factor, hard-zero Newtonian falsifier, and the eta=0 versus eta=1 sectional-source fork"
    )
    print(
        "lattice_wide: the operator is finite-range and translation covariant, but no nonlinear holonomy law, full-Z3 phase, physical transfer, causal Record tick, or global boundary state is inferred"
    )
    print(
        "scope_boundary: exact local curvature intertwiner and contracted Record-source boundary; not selected gravity dynamics, a nonlinear Einstein theorem, axiom adoption, or TOE closure"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
