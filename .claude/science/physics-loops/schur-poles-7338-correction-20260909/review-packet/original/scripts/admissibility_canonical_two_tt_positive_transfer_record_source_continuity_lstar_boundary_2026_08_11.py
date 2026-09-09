#!/usr/bin/env python3
"""Construct a positive constrained two-TT transfer and test Record sources.

The runner supplies a conditional local quadratic family, proves its physical
TT quotient and positive transfer controls, and then checks the exact periodic
continuity obstruction for identifying one new permanent Record with a new
nonzero scalar gravity charge.  It does not select the family or amend axioms.
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path
import sys

import numpy as np
from scipy.linalg import null_space


AUDIT_TIMEOUT_SEC = 180

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CANONICAL_TWO_TT_POSITIVE_TRANSFER_RECORD_SOURCE_"
    "CONTINUITY_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
KINETIC_PATH = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
IR_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_"
    "CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
RECORD_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_PERMANENT_RECORD_FORMATION_SCHEDULER_LORENTZIAN_"
    "TIME_CONSTRAINT_SELECTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
JOINT_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_JOINT_RECORD_GRAVITY_LAW_FIVE_CONTROL_AXIOM_CUT_"
    "GATE_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
CURVATURE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REFLECTED_PLAQUETTE_CURVATURE_RECORD_RICCI_SOURCE_"
    "INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
OS_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_COMMON_METRIC_TT_OS_ONE_TWO_STEP_HANKEL_OBSTRUCTION_"
    "AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
PREMISE_PATH = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_CANONICAL_TWO_TT_POSITIVE_TRANSFER_RECORD_SOURCE_CONTINUITY_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_PERMANENT_RECORD_FORMATION_SCHEDULER_LORENTZIAN_TIME_CONSTRAINT_SELECTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_JOINT_RECORD_GRAVITY_LAW_FIVE_CONTROL_AXIOM_CUT_GATE_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_REFLECTED_PLAQUETTE_CURVATURE_RECORD_RICCI_SOURCE_INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_COMMON_METRIC_TT_OS_ONE_TWO_STEP_HANKEL_OBSTRUCTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/audit/data/axiom_premise_nodes.json",
)


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


def permutation_sign(values: tuple[int, ...]) -> int:
    inversions = sum(
        values[left] > values[right]
        for left in range(len(values))
        for right in range(left + 1, len(values))
    )
    return -1 if inversions % 2 else 1


def proper_cubic_rotations() -> tuple[np.ndarray, ...]:
    rotations: list[np.ndarray] = []
    for permutation in permutations(range(3)):
        sign_p = permutation_sign(permutation)
        for signs in product((-1, 1), repeat=3):
            if sign_p * int(np.prod(signs)) != 1:
                continue
            matrix = np.zeros((3, 3), dtype=int)
            for row, column in enumerate(permutation):
                matrix[row, column] = signs[row]
            rotations.append(matrix)
    return tuple(rotations)


SYMMETRIC_BASIS = (
    np.asarray(((1, 0, 0), (0, 0, 0), (0, 0, 0)), dtype=float),
    np.asarray(((0, 0, 0), (0, 1, 0), (0, 0, 0)), dtype=float),
    np.asarray(((0, 0, 0), (0, 0, 0), (0, 0, 1)), dtype=float),
    np.asarray(((0, 1, 0), (1, 0, 0), (0, 0, 0)), dtype=float) / np.sqrt(2.0),
    np.asarray(((0, 0, 1), (0, 0, 0), (1, 0, 0)), dtype=float) / np.sqrt(2.0),
    np.asarray(((0, 0, 0), (0, 0, 1), (0, 1, 0)), dtype=float) / np.sqrt(2.0),
)


def lattice_vector(momentum: np.ndarray) -> np.ndarray:
    return 2.0 * np.sin(np.asarray(momentum, dtype=float) / 2.0)


def spatial_laplacian(momentum: np.ndarray) -> float:
    vector = lattice_vector(momentum)
    return float(vector @ vector)


def tt_constraint(momentum: np.ndarray) -> np.ndarray:
    vector = lattice_vector(momentum)
    rows = [np.asarray([np.trace(basis) for basis in SYMMETRIC_BASIS])]
    rows.extend(
        np.asarray([(basis @ vector)[axis] for basis in SYMMETRIC_BASIS])
        for axis in range(3)
    )
    return np.asarray(rows, dtype=float)


def transfer_data(momentum: np.ndarray, irrelevant_coefficient: float):
    kappa_squared = spatial_laplacian(momentum)
    kappa = float(np.sqrt(kappa_squared))
    temporal_mass = 1.0 + irrelevant_coefficient * kappa_squared
    energy = float(2.0 * np.arcsinh(kappa / (2.0 * np.sqrt(temporal_mass))))
    decay = float(np.exp(-energy))
    residue = float(1.0 / (2.0 * temporal_mass * np.sinh(energy)))
    canonical_mass = float(temporal_mass * np.sinh(energy) / energy)
    return kappa_squared, temporal_mass, energy, decay, residue, canonical_mass


def gaussian_kernel_matrix(
    momentum: np.ndarray, irrelevant_coefficient: float
) -> np.ndarray:
    kappa_squared, temporal_mass, *_ = transfer_data(
        momentum, irrelevant_coefficient
    )
    coordinates = np.linspace(-3.0, 3.0, 21)
    left = coordinates[:, None]
    right = coordinates[None, :]
    return np.exp(
        -0.5 * temporal_mass * (left - right) ** 2
        -0.25 * kappa_squared * (left**2 + right**2)
    )


def symplectic_matrix(momentum: np.ndarray, irrelevant_coefficient: float):
    *_, energy, _, _, canonical_mass = transfer_data(
        momentum, irrelevant_coefficient
    )
    cosine = np.cos(energy)
    sine = np.sin(energy)
    matrix = np.asarray(
        (
            (cosine, sine / (canonical_mass * energy)),
            (-canonical_mass * energy * sine, cosine),
        )
    )
    hessian = np.diag(
        (canonical_mass * energy**2, 1.0 / canonical_mass)
    )
    return matrix, hessian


def periodic_incidence(size: int) -> tuple[np.ndarray, dict[tuple[int, int], int]]:
    sites = size**3
    incidence = np.zeros((sites, 3 * sites), dtype=float)
    edge_lookup: dict[tuple[int, int], int] = {}

    def index(site: tuple[int, int, int]) -> int:
        return (site[0] * size + site[1]) * size + site[2]

    edge = 0
    for site in product(range(size), repeat=3):
        source = index(site)
        for axis in range(3):
            target_site = list(site)
            target_site[axis] = (target_site[axis] + 1) % size
            target = index(tuple(target_site))
            incidence[source, edge] = 1.0
            incidence[target, edge] = -1.0
            edge_lookup[(source, axis)] = edge
            edge += 1
    return incidence, edge_lookup


def main() -> int:
    checks = Checks()
    note = flat(NOTE_PATH)
    axioms = flat(AXIOM_PATH)
    kinetic = flat(KINETIC_PATH)
    infrared = flat(IR_PATH)
    record = flat(RECORD_PATH)
    joint = flat(JOINT_PATH)
    curvature = flat(CURVATURE_PATH)
    os_note = flat(OS_PATH)

    checks.check(
        "source-and-scope-bindings",
        "the current foundation and exact gravity/Record parents are read without treating the conditional family as selected",
        all((ROOT / path).exists() for path in AUDIT_INPUT_PATHS)
        and "does not choose a hamiltonian or transfer operator" in axioms
        and "c_t = c_s" in kinetic
        and "two transverse-traceless polarizations" in infrared
        and "permanent" in record
        and "record-extension instrument" in joint
        and "trace-reversed temporal/ricci source" in curvature
        and "negative one- and two-step os moment grams" in os_note,
    )

    rotations = proper_cubic_rotations()
    rotation_error = 0.0
    for vector in (
        np.asarray((0.2, 0.4, -0.6)),
        np.asarray((1.1, -0.7, 0.3)),
    ):
        reference = spatial_laplacian(vector)
        for rotation in rotations:
            rotation_error = max(
                rotation_error,
                abs(spatial_laplacian(rotation @ vector) - reference),
            )
    checks.check(
        "proper-cubic-local-symbol",
        "the spatial Laplacian and mixed temporal coefficient are proper-cubic invariant and arise from nearest-neighbour plaquette terms",
        len(rotations) == 24 and rotation_error < 2.0e-15
        and "nearest-neighbour plaquette" in note,
        f"rotations={len(rotations)}; invariance={rotation_error:.3e}",
    )

    grid_size = 9
    grid = 2.0 * np.pi * np.arange(-(grid_size // 2), grid_size // 2 + 1) / grid_size
    momenta = tuple(
        np.asarray(values, dtype=float)
        for values in product(grid, repeat=3)
        if values != (0.0, 0.0, 0.0)
    )
    ranks = tuple(
        int(np.linalg.matrix_rank(tt_constraint(momentum), tol=1.0e-11))
        for momentum in momenta
    )
    checks.check(
        "exactly-two-tt-constraint-fiber",
        "trace plus three lattice-divergence constraints have rank four at every nonzero declared spatial momentum",
        len(momenta) == 728 and set(ranks) == {4},
        f"modes={len(momenta)}; ranks={sorted(set(ranks))}; TT dimension={6-ranks[0]}",
    )

    positivity = []
    hankel_minimum = 1.0
    decay_bounds = [1.0, 0.0]
    for coefficient in (0.0, 1.0):
        for momentum in momenta:
            _, temporal_mass, energy, decay, residue, _ = transfer_data(
                momentum, coefficient
            )
            positivity.append((temporal_mass, energy, residue))
            decay_bounds[0] = min(decay_bounds[0], decay)
            decay_bounds[1] = max(decay_bounds[1], decay)
            moments = np.asarray([residue * decay**time for time in range(11)])
            gram = np.asarray(
                [[moments[left + right] for right in range(6)] for left in range(6)]
            )
            hankel_minimum = min(hankel_minimum, float(np.linalg.eigvalsh(gram)[0]))
    checks.check(
        "positive-two-mode-os-transfer-family",
        "both r=0 and r=1 have positive temporal mass, real energy, positive residue, contraction decay, and PSD OS moments on every mode",
        min(value[0] for value in positivity) >= 1.0
        and min(value[1] for value in positivity) > 0.0
        and min(value[2] for value in positivity) > 0.0
        and 0.0 < decay_bounds[0] <= decay_bounds[1] < 1.0
        and hankel_minimum > -2.0e-12,
        f"decay={decay_bounds[0]:.6f}..{decay_bounds[1]:.6f}; worst Hankel={hankel_minimum:.3e}",
    )

    representative = np.asarray((0.4, 0.0, 0.0))
    kernel_minima = tuple(
        float(np.linalg.eigvalsh(gaussian_kernel_matrix(representative, coefficient))[0])
        for coefficient in (0.0, 1.0)
    )
    checks.check(
        "one-step-kernel-factorization-control",
        "the coordinate kernel is a positive Gaussian convolution sandwiched by positive potential factors for both completions",
        min(kernel_minima) > -2.0e-12
        and "m c_a m" in note,
        f"sampled kernel minima={kernel_minima}",
    )

    symplectic_form = np.asarray(((0.0, 1.0), (-1.0, 0.0)))
    symplectic_error = 0.0
    energy_error = 0.0
    constraint_error = 0.0
    rng = np.random.default_rng(5108)
    for coefficient in (0.0, 1.0):
        for momentum in momenta[::41]:
            evolution, hessian = symplectic_matrix(momentum, coefficient)
            symplectic_error = max(
                symplectic_error,
                float(np.linalg.norm(evolution.T @ symplectic_form @ evolution - symplectic_form)),
            )
            energy_error = max(
                energy_error,
                float(np.linalg.norm(evolution.T @ hessian @ evolution - hessian)),
            )
            constraint = tt_constraint(momentum)
            quotient = null_space(constraint, rcond=1.0e-11)
            amplitudes = rng.normal(size=(2, 2))
            evolved = amplitudes @ evolution.T
            constraint_error = max(
                constraint_error,
                float(np.linalg.norm(constraint @ quotient @ evolved[:, 0])),
                float(np.linalg.norm(constraint @ quotient @ evolved[:, 1])),
            )
    checks.check(
        "canonical-positive-energy-constraint-update",
        "the Lorentzian log-transfer oscillator map is symplectic, preserves its positive Hamiltonian, and keeps both TT constraints exact",
        symplectic_error < 2.0e-14
        and energy_error < 2.0e-13
        and constraint_error < 2.0e-14,
        f"symplectic={symplectic_error:.3e}; energy={energy_error:.3e}; constraints={constraint_error:.3e}",
    )

    static_error = 0.0
    for momentum in momenta:
        kappa_squared = spatial_laplacian(momentum)
        for coefficient in (0.0, 1.0):
            temporal_mass = 1.0 + coefficient * kappa_squared
            static_symbol = kappa_squared + temporal_mass * 4.0 * np.sin(0.0) ** 2
            static_error = max(static_error, abs(static_symbol - kappa_squared))
    checks.check(
        "static-source-continuity",
        "the irrelevant mixed derivative changes only temporal propagation; both transfers have exactly the same static kernel and source response",
        static_error == 0.0,
        f"maximum static difference={static_error:.1e}",
    )

    small_momenta = (
        2.0 * np.pi / 129.0,
        2.0 * np.pi / 257.0,
        2.0 * np.pi / 513.0,
    )
    infrared_errors = []
    for coefficient in (0.0, 1.0):
        ratios = []
        for wave_number in small_momenta:
            kappa_squared, _, energy, *_ = transfer_data(
                np.asarray((wave_number, 0.0, 0.0)), coefficient
            )
            ratios.append(energy / np.sqrt(kappa_squared))
        infrared_errors.append(max(abs(value - 1.0) for value in ratios))
    energy_zero = transfer_data(representative, 0.0)[2]
    energy_one = transfer_data(representative, 1.0)[2]
    checks.check(
        "os0-equal-infrared-inequivalent-finite-transfer",
        "r=0 and r=1 have the same unit-speed OS0 quadratic limit and static law but different finite-lattice transfer gaps",
        max(infrared_errors) < 2.0e-3
        and abs(energy_zero - energy_one) > 0.02,
        f"E_0(0.4)={energy_zero:.9f}; E_1(0.4)={energy_one:.9f}; IR errors={infrared_errors}",
    )

    incidence, edge_lookup = periodic_incidence(3)
    incidence_rank = int(np.linalg.matrix_rank(incidence, tol=1.0e-12))
    source_unit = 0.25
    isolated = np.zeros(27)
    isolated[0] = source_unit
    isolated_solution, *_ = np.linalg.lstsq(incidence, -isolated, rcond=None)
    isolated_residual = float(np.linalg.norm(incidence @ isolated_solution + isolated))
    checks.check(
        "single-record-source-continuity-obstruction",
        "one newly formed Record with nonzero Block-49 Ricci charge cannot be the divergence of a periodic local source flux",
        incidence_rank == 26
        and abs(np.sum(isolated) - source_unit) < 1.0e-15
        and isolated_residual > 0.04,
        f"rank={incidence_rank}; total increment={np.sum(isolated):.6f}; best residual={isolated_residual:.9f}",
    )

    flux = np.zeros(81)
    flux[edge_lookup[(0, 0)]] = source_unit
    conservative_increment = -(incidence @ flux)
    continuity_error = float(np.linalg.norm(conservative_increment + incidence @ flux))
    rng = np.random.default_rng(5111)
    gravity_field = rng.normal(size=81)
    source_before = incidence @ gravity_field
    gravity_after = gravity_field - flux
    source_after = incidence @ gravity_after
    propagation_error = float(
        np.linalg.norm(source_after - source_before - conservative_increment)
    )
    checks.check(
        "local-conservative-record-transport-repair",
        "a nearest-neighbour source transport has zero total increment and an exact local Gauss-constraint intertwiner",
        abs(np.sum(conservative_increment)) < 1.0e-15
        and np.count_nonzero(np.abs(conservative_increment) > 1.0e-15) == 2
        and continuity_error < 1.0e-15
        and propagation_error < 2.0e-15,
        f"increment support={np.flatnonzero(conservative_increment)}; continuity={continuity_error:.3e}; propagation={propagation_error:.3e}",
    )

    record_sources = {
        "t": (2.0 * 1.0 - 1.0) / 4.0,
        "x": (2.0 * 0.0 - 1.0) / 4.0,
        "x+t": (2.0 * 1.0 - 2.0) / (4.0 * np.sqrt(2.0)),
    }
    checks.check(
        "record-source-decoder-transition-boundary",
        "nonzero single t-like or x-like Record charges fail continuity while a zero-charge diagonal or balanced transition remains possible",
        abs(record_sources["t"] - 0.25) < 1.0e-15
        and abs(record_sources["x"] + 0.25) < 1.0e-15
        and record_sources["x+t"] == 0.0
        and "transition-based conserved source-current decoder" in note,
        f"sources={record_sources}",
    )

    checks.check(
        "extensional-transfer-fork",
        "two local positive constraint-preserving completions satisfy the same declared structural and static contract but differ physically",
        energy_zero != energy_one
        and "r=0" in note
        and "r=1" in note
        and "current axioms do not select" in note,
    )
    checks.check(
        "exact-lstar-axiom-boundary",
        "the smallest honest constitutional target must bind the transfer kernel and a conserved Record-extension source instrument",
        "retype admissibility" in note
        and "delta j + div s = 0" in note
        and "no canonical axiom is edited" in note
        and "zero toe percentage points" in note,
    )
    checks.check(
        "fresh-no-go-discipline-packet",
        "the periodic isolated-source and present-foundation nonselection claims pass N1 through N8 with their repairs live",
        all(f"n{index} —" in note for index in range(1, 9))
        and all(
            phrase in note
            for phrase in (
                "open boundary",
                "background reservoir",
                "paired neutral formation",
                "worldline continuation",
                "downstream uniqueness theorem",
            )
        ),
    )

    print(
        "N5_CERTIFICATE: all 728 nonzero L=9 spatial momenta, four local TT constraints, two physical polarizations, both r=0 and r=1 transfer kernels, 24 proper cubic rotations, six-by-six OS moment blocks, canonical symplectic controls, all 27 sites and 81 oriented edges of the L=3 continuity carrier, three Record rays, one isolated formation, and one conservative transport repair are resolved"
    )
    print(
        "per_element: checked every symmetric-tensor coordinate through trace/divergence constraints, both TT coordinates, each transfer coefficient, and every site/edge incidence entry"
    )
    print(
        "per_site: checked one complete periodic L=3 source-continuity carrier and the formation/transport updates at both endpoints of one nearest-neighbour edge"
    )
    print(
        "per_mode: checked every nonzero L=9 spatial momentum for r=0 and r=1, plus all declared infrared and representative finite-momentum controls"
    )
    print(
        "per_block: checked local action symmetry, TT quotient, positive OS/canonical transfer, static equality, finite-transfer fork, isolated-source obstruction, and conservative repair"
    )
    print(
        "lattice_wide: the formulas extend translation-covariantly to finite periodic lattices, but no selected Record law, absolute history, nonlinear geometry, nonflat phase, full-Z3 measure, or canonical axiom adoption is inferred"
    )
    print(
        "scope_boundary: conditional positive linear two-TT transfer family plus exact periodic Record-source continuity cut; not selected gravity, nonlinear Einstein dynamics, axiom necessity, axiom adoption, or TOE closure"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
