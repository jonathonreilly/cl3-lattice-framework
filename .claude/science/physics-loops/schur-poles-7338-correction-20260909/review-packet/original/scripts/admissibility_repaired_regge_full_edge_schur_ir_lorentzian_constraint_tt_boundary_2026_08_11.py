#!/usr/bin/env python3
"""Check the full-edge infrared Schur and conditional Lorentzian Regge sector.

The supplied action is the repaired flat Kuhn/Coxeter Regge edge action

    S_alpha = sum_h A_h (epsilon_h + alpha epsilon_h**2),
    alpha = 1/1024.

At zero momentum this runner keeps the complete fifteen-edge Hessian, fixes an
orthonormal five-dimensional complement to the ten constant-metric tangents,
and eliminates that complement by its nonsingular stationary Schur equation.
It computes the complete quadratic momentum coefficient analytically from the
real-space kernel.  It then checks a conditional standard Lorentzian
continuation of that coefficient.  The latter is a candidate infrared law,
not a derivation of a causal Record update from the current axioms.
"""

from __future__ import annotations

from pathlib import Path
import sys

import numpy as np


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_"
    "CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGGE_NOTE_PATH = ROOT / "docs" / (
    "CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_"
    "NARROW_THEOREM_NOTE_2026-06-09.md"
)
REPAIR_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_FLAT_REGGE_CURVATURE_SQUARED_BRANCH_LIFT_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
GREEN_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REGGE_FIXED_AVERAGE_TICK_SOURCE_INCREASING_TORUS_"
    "WARD_GREEN_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
PREMISE_REGISTRY_PATH = (
    ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md",
    "docs/ADMISSIBILITY_FLAT_REGGE_CURVATURE_SQUARED_BRANCH_LIFT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_REGGE_FIXED_AVERAGE_TICK_SOURCE_INCREASING_TORUS_WARD_GREEN_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_regge_fixed_average_tick_source_increasing_torus_ward_green_boundary_2026_08_11.py",
    "scripts/admissibility_flat_regge_curvature_squared_branch_lift_2026_08_10.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)

sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_regge_fixed_average_tick_source_increasing_torus_ward_green_boundary_2026_08_11 as block43  # noqa: E402


HCOMPS = tuple(block43.regge.HCOMPS)
EUCLIDEAN_METRIC = np.eye(4)
LORENTZIAN_METRIC = np.diag((1.0, 1.0, 1.0, -1.0))
TIME_COMPONENTS = tuple(
    index for index, (left, right) in enumerate(HCOMPS) if 3 in (left, right)
)
STATIC_SOURCE_INDEX = HCOMPS.index((3, 3))
TOLERANCE = 1.0e-10


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


def symmetric_basis(index: int) -> np.ndarray:
    left, right = HCOMPS[index]
    matrix = np.zeros((4, 4), dtype=float)
    matrix[left, right] += 1.0
    if left != right:
        matrix[right, left] += 1.0
    return matrix


def einstein_tensors(momentum_lower: np.ndarray, metric: np.ndarray) -> tuple[np.ndarray, ...]:
    """Linearized Einstein tensors for the ten covariant metric-coordinate bases."""
    momentum_lower = np.asarray(momentum_lower, dtype=float)
    momentum_upper = metric @ momentum_lower
    momentum_squared = float(momentum_lower @ momentum_upper)
    tensors = []
    for index in range(len(HCOMPS)):
        perturbation = symmetric_basis(index)
        trace = float(np.trace(metric @ perturbation))
        contracted = momentum_upper @ perturbation
        double_contracted = float(momentum_upper @ perturbation @ momentum_upper)
        tensor = 0.5 * (
            momentum_squared * perturbation
            + np.outer(momentum_lower, momentum_lower) * trace
            - np.outer(momentum_lower, contracted)
            - np.outer(contracted, momentum_lower)
            - metric
            * (momentum_squared * trace - double_contracted)
        )
        tensors.append(tensor)
    return tuple(tensors)


def einstein_action_pairing(momentum_lower: np.ndarray, metric: np.ndarray) -> np.ndarray:
    """Coordinate matrix for h^{mu nu} G_{mu nu} in the HCOMPS convention."""
    tensors = einstein_tensors(momentum_lower, metric)
    pairing = np.zeros((len(HCOMPS), len(HCOMPS)), dtype=float)
    for row, (left, right) in enumerate(HCOMPS):
        multiplicity = 2.0 if left != right else 1.0
        raising_sign = metric[left, left] * metric[right, right]
        for column, tensor in enumerate(tensors):
            pairing[row, column] = (
                multiplicity * raising_sign * tensor[left, right]
            )
    return 0.5 * (pairing + pairing.T)


def continuum_gauge_map(momentum_lower: np.ndarray) -> np.ndarray:
    momentum_lower = np.asarray(momentum_lower, dtype=float)
    columns = np.zeros((len(HCOMPS), 4), dtype=float)
    for direction in range(4):
        covector = np.zeros(4, dtype=float)
        covector[direction] = 1.0
        perturbation = np.outer(momentum_lower, covector) + np.outer(
            covector, momentum_lower
        )
        columns[:, direction] = np.asarray(
            [perturbation[left, right] for left, right in HCOMPS]
        )
    return columns


def constant_split() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    metric_map = block43.METRIC_COEFFICIENTS.astype(complex)
    zero_symbol = np.sum(block43.MATRICES, axis=0).astype(complex)
    left_vectors, singular_values, _ = np.linalg.svd(
        metric_map, full_matrices=True
    )
    nonmetric = left_vectors[:, len(HCOMPS) :]
    nonmetric_block = nonmetric.conj().T @ zero_symbol @ nonmetric
    return metric_map, zero_symbol, nonmetric, nonmetric_block


def leading_schur(
    direction: np.ndarray,
    metric_map: np.ndarray,
    zero_symbol: np.ndarray,
    nonmetric: np.ndarray,
    nonmetric_block: np.ndarray,
) -> np.ndarray:
    """Coefficient of q^2 after stationary elimination of the full complement."""
    direction = np.asarray(direction, dtype=float)
    shift_dot = block43.SHIFTS @ direction
    edge_dot = block43.DIRECTIONS @ direction
    first_symbol = np.einsum(
        "s,sij->ij", 1j * shift_dot, block43.MATRICES, optimize=True
    )
    second_symbol = np.einsum(
        "s,sij->ij", -0.5 * shift_dot**2, block43.MATRICES, optimize=True
    )
    first_metric = 0.5j * edge_dot[:, None] * metric_map

    direct = (
        metric_map.conj().T @ second_symbol @ metric_map
        + first_metric.conj().T @ first_symbol @ metric_map
        + metric_map.conj().T @ first_symbol @ first_metric
        + first_metric.conj().T @ zero_symbol @ first_metric
    )
    mixing = (
        metric_map.conj().T @ first_symbol @ nonmetric
        + first_metric.conj().T @ zero_symbol @ nonmetric
    )
    return direct - mixing @ np.linalg.solve(nonmetric_block, mixing.conj().T)


def full_schur(momentum: np.ndarray, nonmetric: np.ndarray) -> np.ndarray:
    momentum = np.asarray(momentum, dtype=float)
    phases = np.exp(1j * (block43.SHIFTS @ momentum))
    symbol = np.einsum("s,sij->ij", phases, block43.MATRICES, optimize=True)
    metric_map = block43.batch_metric_map(momentum[None, :])[0]
    metric_block = metric_map.conj().T @ symbol @ metric_map
    mixing = metric_map.conj().T @ symbol @ nonmetric
    complement_block = nonmetric.conj().T @ symbol @ nonmetric
    return metric_block - mixing @ np.linalg.solve(
        complement_block, mixing.conj().T
    )


def inertia(matrix: np.ndarray, tolerance: float = TOLERANCE) -> tuple[int, int, int]:
    eigenvalues = np.linalg.eigvalsh(0.5 * (matrix + matrix.conj().T))
    return (
        int(np.sum(eigenvalues < -tolerance)),
        int(np.sum(eigenvalues > tolerance)),
        int(np.sum(np.abs(eigenvalues) <= tolerance)),
    )


def lorentzian_operator(spatial_momentum: np.ndarray, frequency: float) -> np.ndarray:
    spatial_momentum = np.asarray(spatial_momentum, dtype=float)
    momentum_lower = np.concatenate((spatial_momentum, (-float(frequency),)))
    return -0.5 * einstein_action_pairing(momentum_lower, LORENTZIAN_METRIC)


def transverse_traceless_vectors() -> tuple[np.ndarray, np.ndarray]:
    plus = np.zeros(len(HCOMPS), dtype=float)
    plus[HCOMPS.index((1, 1))] = 1.0 / np.sqrt(2.0)
    plus[HCOMPS.index((2, 2))] = -1.0 / np.sqrt(2.0)
    cross = np.zeros(len(HCOMPS), dtype=float)
    cross[HCOMPS.index((1, 2))] = 1.0 / np.sqrt(2.0)
    return plus, cross


def main() -> int:
    checks = Checks()
    note = flat(NOTE_PATH)
    axiom = flat(AXIOM_PATH)
    regge_note = flat(REGGE_NOTE_PATH)
    repair_note = flat(REPAIR_NOTE_PATH)
    green_note = flat(GREEN_NOTE_PATH)

    checks.check(
        "source-and-scope-bindings",
        "the current axioms and three supplied Regge parents are read without promoting the candidate continuation",
        all(
            path.exists()
            for path in (
                NOTE_PATH,
                AXIOM_PATH,
                REGGE_NOTE_PATH,
                REPAIR_NOTE_PATH,
                GREEN_NOTE_PATH,
                PREMISE_REGISTRY_PATH,
            )
        )
        and "admissibility is not a dynamics axiom" in axiom
        and "vertex displacements" in regge_note
        and "0 < alpha <= 1/128" in repair_note
        and "lim_(q->0) q^2 h_tt" in green_note,
    )

    metric_map, zero_symbol, nonmetric, nonmetric_block = constant_split()
    metric_singular = np.linalg.svd(metric_map, compute_uv=False)
    constant_metric_residual = float(np.max(np.abs(zero_symbol @ metric_map)))
    complement_orthogonality = float(
        np.max(np.abs(metric_map.conj().T @ nonmetric))
    )
    checks.check(
        "complete-constant-edge-split",
        "the ten constant-metric tangents and their five-dimensional orthogonal complement exhaust all fifteen edges",
        np.linalg.matrix_rank(metric_map, tol=1.0e-12) == 10
        and nonmetric.shape == (15, 5)
        and metric_singular[-1] > 0.46
        and constant_metric_residual < 1.5e-13
        and complement_orthogonality < 1.0e-14,
        f"min sigma(M0)={metric_singular[-1]:.6f}; |Q0M0|={constant_metric_residual:.3e}",
    )

    complement_eigenvalues = np.linalg.eigvalsh(nonmetric_block)
    complement_gap = float(np.min(np.abs(complement_eigenvalues)))
    checks.check(
        "repaired-nonmetric-block-invertible",
        "the repaired five-direction nonmetric block is nonsingular, so no fifth flat branch is silently discarded",
        inertia(nonmetric_block) == (4, 1, 0) and complement_gap > 1.28,
        "eigenvalues=" + ",".join(f"{value:.6f}" for value in complement_eigenvalues),
    )

    basis_directions = tuple(np.eye(4)[index] for index in range(4))
    directions = list(basis_directions)
    directions.extend(
        basis_directions[left] + basis_directions[right]
        for left in range(4)
        for right in range(left + 1, 4)
    )
    schur_values = [
        leading_schur(
            direction, metric_map, zero_symbol, nonmetric, nonmetric_block
        )
        for direction in directions
    ]
    comparator_values = [
        -0.5 * einstein_action_pairing(direction, EUCLIDEAN_METRIC)
        for direction in directions
    ]
    tensor_error = max(
        float(np.max(np.abs(schur - comparator)))
        for schur, comparator in zip(schur_values, comparator_values)
    )
    imaginary_error = max(
        float(np.max(np.abs(schur.imag))) for schur in schur_values
    )
    checks.check(
        "all-momentum-monomial-einstein-identity",
        "the full-edge Schur coefficient equals minus one-half the Euclidean linearized Einstein pairing for all ten momentum monomials",
        tensor_error < 3.0e-13 and imaginary_error < 1.0e-13,
        f"max coefficient error={tensor_error:.3e}; max imaginary={imaginary_error:.3e}",
    )

    euclidean_ward = 0.0
    euclidean_ranks = set()
    for direction, schur in zip(directions, schur_values):
        gauge = continuum_gauge_map(direction)
        euclidean_ward = max(
            euclidean_ward, float(np.max(np.abs(schur @ gauge)))
        )
        euclidean_ranks.add(np.linalg.matrix_rank(schur, tol=1.0e-10))
    checks.check(
        "leading-displacement-ward-quotient",
        "the derived coefficient has exactly four continuum displacement nulls and rank six at every monomial probe direction",
        euclidean_ward < 8.0e-14 and euclidean_ranks == {6},
        f"max Ward residual={euclidean_ward:.3e}; ranks={sorted(euclidean_ranks)}",
    )

    generic_direction = np.asarray((1.0, 0.3, -0.2, 0.4), dtype=float)
    generic_direction /= np.linalg.norm(generic_direction)
    generic_leading = leading_schur(
        generic_direction, metric_map, zero_symbol, nonmetric, nonmetric_block
    )
    scales = (0.05, 0.025, 0.0125, 0.00625)
    convergence_errors = np.asarray(
        [
            np.max(
                np.abs(
                    full_schur(scale * generic_direction, nonmetric) / scale**2
                    - generic_leading
                )
            )
            for scale in scales
        ]
    )
    checks.check(
        "finite-momentum-schur-convergence",
        "direct complete-edge stationary elimination converges quadratically to the analytic infrared coefficient",
        np.all(convergence_errors[1:] < 0.27 * convergence_errors[:-1])
        and convergence_errors[-1] < 2.1e-6,
        "errors=" + ",".join(f"{value:.3e}" for value in convergence_errors),
    )

    static_operator = schur_values[0]
    static_source = np.zeros(len(HCOMPS), dtype=float)
    static_source[STATIC_SOURCE_INDEX] = 1.0
    static_response = -np.linalg.pinv(static_operator, rcond=1.0e-12) @ static_source
    static_residual = float(
        np.linalg.norm(static_operator @ static_response + static_source)
    )
    static_ward_source = float(
        np.max(np.abs(static_source @ continuum_gauge_map(basis_directions[0])))
    )
    checks.check(
        "static-source-residue-match",
        "the derived infrared operator gives h_tt equals two for the same unit static source orientation as the increasing-torus result",
        abs(static_response[STATIC_SOURCE_INDEX] - 2.0) < 1.0e-12
        and static_residual < 1.0e-12
        and static_ward_source < 1.0e-15,
        f"h_tt={static_response[STATIC_SOURCE_INDEX]:.12f}; residual={static_residual:.3e}",
    )

    kinetic = lorentzian_operator(np.zeros(3), 1.0)
    multiplier_residual = float(
        np.max(np.abs(kinetic[np.asarray(TIME_COMPONENTS), :]))
    )
    checks.check(
        "conditional-lapse-shift-multipliers",
        "in the standard Lorentzian continuation the lapse and three shifts carry no frequency-squared kinetic rows",
        TIME_COMPONENTS == (3, 6, 8, 9)
        and multiplier_residual < 1.0e-15
        and np.linalg.matrix_rank(kinetic, tol=1.0e-12) == 6,
        f"time-coordinate rows={TIME_COMPONENTS}; max kinetic row={multiplier_residual:.3e}",
    )
    checks.check(
        "conditional-dewitt-kinetic-inertia",
        "the six-dimensional spatial kinetic block has five positive shear directions and one negative conformal direction",
        inertia(kinetic) == (1, 5, 4),
        "eigenvalues=" + ",".join(f"{value:.3f}" for value in np.linalg.eigvalsh(kinetic)),
    )

    shell_momentum = np.asarray((1.0, 0.0, 0.0, -1.0))
    shell_operator = lorentzian_operator(shell_momentum[:3], 1.0)
    shell_gauge = continuum_gauge_map(shell_momentum)
    plus, cross = transverse_traceless_vectors()
    shell_spanning = np.column_stack((shell_gauge, plus, cross))
    shell_null_residual = float(
        np.max(np.abs(shell_operator @ shell_spanning))
    )
    checks.check(
        "conditional-null-shell-two-tt-quotient",
        "on the light cone the kernel is exactly four gauge directions plus two independent transverse-traceless polarizations",
        np.linalg.matrix_rank(shell_operator, tol=1.0e-12) == 4
        and np.linalg.matrix_rank(shell_gauge, tol=1.0e-12) == 4
        and np.linalg.matrix_rank(shell_spanning, tol=1.0e-12) == 6
        and shell_null_residual < 1.0e-14,
        f"rank(Q)={np.linalg.matrix_rank(shell_operator, tol=1e-12)}; null residual={shell_null_residual:.3e}",
    )

    dispersion_samples = ((1.3, 0.7), (0.4, 1.7), (1.0, 1.0))
    dispersion_error = 0.0
    mixing_error = 0.0
    for wave_number, frequency in dispersion_samples:
        operator = lorentzian_operator((wave_number, 0.0, 0.0), frequency)
        target = (frequency**2 - wave_number**2) / 4.0
        dispersion_error = max(
            dispersion_error,
            abs(float(plus @ operator @ plus) - target),
            abs(float(cross @ operator @ cross) - target),
        )
        mixing_error = max(mixing_error, abs(float(plus @ operator @ cross)))
    checks.check(
        "conditional-two-tt-light-cone-dispersion",
        "both physical tensor polarizations have the same positive frequency-squared coefficient and no mixing",
        dispersion_error < 5.0e-15
        and mixing_error < 5.0e-15
        and abs(float(plus @ kinetic @ plus) - 0.25) < 1.0e-15
        and abs(float(cross @ kinetic @ cross) - 0.25) < 1.0e-15,
        f"max dispersion error={dispersion_error:.3e}; max TT mixing={mixing_error:.3e}",
    )

    bianchi_momenta = (
        np.asarray((0.7, -0.2, 0.4, -1.1)),
        np.asarray((1.0, 0.0, 0.0, -1.0)),
        np.asarray((0.3, 0.5, -0.8, -0.4)),
    )
    bianchi_error = 0.0
    for momentum_lower in bianchi_momenta:
        momentum_upper = LORENTZIAN_METRIC @ momentum_lower
        for tensor in einstein_tensors(momentum_lower, LORENTZIAN_METRIC):
            bianchi_error = max(
                bianchi_error, float(np.max(np.abs(momentum_upper @ tensor)))
            )
    checks.check(
        "conditional-linear-bianchi-identity",
        "the candidate Lorentzian operator obeys the four linear Bianchi identities needed for constraint consistency",
        bianchi_error < 5.0e-16,
        f"max p^mu G_mu_nu={bianchi_error:.3e}",
    )

    lorentzian_static = lorentzian_operator((1.0, 0.0, 0.0), 0.0)
    lorentzian_response = -np.linalg.pinv(
        lorentzian_static, rcond=1.0e-12
    ) @ static_source
    lorentzian_residual = float(
        np.linalg.norm(lorentzian_static @ lorentzian_response + static_source)
    )
    checks.check(
        "conditional-lorentzian-static-continuity",
        "the candidate Lorentzian constraint solve preserves the positive-source h_tt residue inherited from the complete edge sector",
        abs(lorentzian_response[STATIC_SOURCE_INDEX] - 2.0) < 1.0e-12
        and lorentzian_residual < 1.0e-12,
        f"h_tt={lorentzian_response[STATIC_SOURCE_INDEX]:.12f}; residual={lorentzian_residual:.3e}",
    )

    checks.check(
        "axiom-dynamics-selection-boundary",
        "the source note keeps the Lorentzian continuation conditional because the axioms supply neither its selection nor a Record update",
        all(
            phrase in axiom
            for phrase in (
                "does not choose a hamiltonian or transfer operator",
                "update laws",
                "time metric",
                "source/action",
            )
        )
        and all(
            phrase in note
            for phrase in (
                "lorentzian continuation",
                "not a record-native causal update",
                "no canonical axiom is edited",
                "candidate axiom issue",
            )
        ),
    )

    checks.check(
        "fresh-no-go-discipline-packet",
        "the narrow current-axiom boundary passes N1 through N8 while preserving constructive dynamics and nonflat routes",
        all(f"### n{index}" in note for index in range(1, 9))
        and "status: pass" in note
        and all(
            phrase in note
            for phrase in (
                "not a gravity no-go",
                "stable nonflat",
                "reflection-positive",
                "downstream bridge",
                "not proved necessary",
            )
        ),
    )

    print(
        "N5_CERTIFICATE: fifteen edge coordinates, ten metric coordinates, five nonmetric directions, ten momentum monomials, and the full candidate constraint block are resolved"
    )
    print(
        "per_element: checked all fifteen edge classes, all ten metric components, and every entry of each quadratic-momentum coefficient"
    )
    print(
        "per_site: checked the flat unit-cell tangent split and one Ward-compatible unit static tick source"
    )
    print(
        "per_mode: checked all ten quadratic momentum monomials, one generic finite-momentum sequence, and shell/off-shell TT samples"
    )
    print(
        "per_block: checked the complete 15=(10+5) stationary Schur block, Lorentzian multiplier block, null shell, and Bianchi identity"
    )
    print(
        "lattice_wide: the translation-invariant real-space kernel fixes the infrared coefficient only; no full-zone, full-Z3 phase, or causal update theorem is claimed"
    )
    print(
        "scope_boundary: supplied repaired flat action and conditional standard Lorentzian continuation; action selection, Record update, physical inner product, nonlinear constraints, and stable nonflat phase remain open"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
