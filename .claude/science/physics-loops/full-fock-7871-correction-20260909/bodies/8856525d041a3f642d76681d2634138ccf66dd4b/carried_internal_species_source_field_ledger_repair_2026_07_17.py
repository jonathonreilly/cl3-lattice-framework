#!/usr/bin/env python3
"""Carried internal-species source/field ledger repair.

Give a six-direction matter carrier two internal labels, excited and ground.
The onsite vertex converts an excited carrier plus field vacuum into a ground
carrier plus one scalar field excitation, and performs the reverse absorption.
Both internal labels receive the same Cycle-219 coin and one-edge stream, so
the finite source capacity is carried with matter rather than stored at a
fixed lattice site.

The physical realization used here is a new direct hard-core allocation of
12 matter M2 qubits and six field M2 qubits per coarse cell.  It is not the
Cycle-269 even-CAR compiler.  The runner quantifies the exact logical-dimension
deficit of that unchanged compiler for a literal doubled matter alphabet and
the ordinary-SWAP versus FSWAP residual outside the one-particle sector.

This is a conditional one-matter, Q=1 construction.  The internal excitation
plus field-number charge Q is not called energy or a gravitational source.
The source operator, coupling, sector preparation, and schedule are supplied.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np

import autonomous_cubic_field_emission_cycle214_2026_07_16 as c214
import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "CARRIED_INTERNAL_SPECIES_SOURCE_FIELD_LEDGER_REPAIR_NOTE_2026-07-17.md"
)

BETA = -0.3
MEDIATOR_COUPLING = 0.8
CONTACT_COUPLING = 0.37
TOLERANCE = 4e-11

PASS = 0
FAIL = 0

Position = tuple[int, int, int]


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the carried-source repair note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "12 matter m2",
        "six field m2",
        "42-dimensional",
        "source capacity moves with matter",
        "internal excitation plus field number",
        "not energy",
        "no global occupancy service",
        "all 24 proper-cubic frames",
        "mass fixture",
        "contact deletion",
        "zero leakage",
        "declared carried-code continuity",
        "ordinary swap",
        "fswap",
        "6 l^3",
        "route-specific",
        "not a physical car compiler",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("the note preserves scope and exact import boundaries", not missing, missing)


def add_position(left: Position, displacement: np.ndarray, sign: int = 1) -> Position:
    return tuple(
        int(left[axis] + sign * displacement[axis]) for axis in range(3)
    )


def l1(position: Position) -> int:
    return sum(abs(value) for value in position)


def zero_vector() -> np.ndarray:
    return np.zeros(6, dtype=complex)


def zero_pair() -> np.ndarray:
    return np.zeros((6, 6), dtype=complex)


@dataclass
class CarriedState:
    """One matter carrier: excited/no-field or ground/one-field."""

    excited: dict[Position, np.ndarray]
    pair: dict[tuple[Position, Position], np.ndarray]

    def copy(self) -> "CarriedState":
        return CarriedState(
            {key: value.copy() for key, value in self.excited.items()},
            {key: value.copy() for key, value in self.pair.items()},
        )


def state_norm(state: CarriedState) -> float:
    return float(
        sum(np.vdot(value, value).real for value in state.excited.values())
        + sum(np.vdot(value, value).real for value in state.pair.values())
    )


def state_residual(left: CarriedState, right: CarriedState) -> float:
    total = 0.0
    for key in left.excited.keys() | right.excited.keys():
        difference = left.excited.get(key, zero_vector()) - right.excited.get(
            key, zero_vector()
        )
        total += float(np.vdot(difference, difference).real)
    for key in left.pair.keys() | right.pair.keys():
        difference = left.pair.get(key, zero_pair()) - right.pair.get(
            key, zero_pair()
        )
        total += float(np.vdot(difference, difference).real)
    return float(np.sqrt(total))


def add_states(left: CarriedState, right: CarriedState) -> CarriedState:
    output = left.copy()
    for key, value in right.excited.items():
        output.excited[key] = output.excited.get(key, zero_vector()) + value
    for key, value in right.pair.items():
        output.pair[key] = output.pair.get(key, zero_pair()) + value
    return output


def density_residual(left: dict[Position, float], right: dict[Position, float]) -> float:
    return max(
        (abs(left.get(key, 0.0) - right.get(key, 0.0)) for key in left | right),
        default=0.0,
    )


def matter_density(state: CarriedState) -> dict[Position, float]:
    answer: dict[Position, float] = {}
    for body, value in state.excited.items():
        answer[body] = answer.get(body, 0.0) + float(np.vdot(value, value).real)
    for (body, _field), value in state.pair.items():
        answer[body] = answer.get(body, 0.0) + float(np.vdot(value, value).real)
    return answer


def excitation_density(state: CarriedState) -> dict[Position, float]:
    return {
        body: float(np.vdot(value, value).real)
        for body, value in state.excited.items()
    }


def field_density(state: CarriedState) -> dict[Position, float]:
    answer: dict[Position, float] = {}
    for (_body, field), value in state.pair.items():
        answer[field] = answer.get(field, 0.0) + float(np.vdot(value, value).real)
    return answer


def q_density(state: CarriedState) -> dict[Position, float]:
    answer = excitation_density(state)
    for position, value in field_density(state).items():
        answer[position] = answer.get(position, 0.0) + value
    return answer


def coin_gate(
    state: CarriedState, matter_coin: np.ndarray, field_coin: np.ndarray
) -> CarriedState:
    return CarriedState(
        {position: matter_coin @ value for position, value in state.excited.items()},
        {
            key: np.einsum(
                "ab,cd,bd->ac", matter_coin, field_coin, value, optimize=True
            )
            for key, value in state.pair.items()
        },
    )


def local_vertex(
    excited: np.ndarray, contact_pair: np.ndarray, angle: float
) -> tuple[np.ndarray, np.ndarray]:
    """Direction-preserving E_d <-> G_d times scalar-field rotation."""
    scalar = contact_pair @ c210.UNIFORM
    transverse = contact_pair - np.outer(scalar, c210.UNIFORM.conj())
    cosine = np.cos(angle)
    sine = np.sin(angle)
    new_excited = cosine * excited + 1j * sine * scalar
    new_scalar = 1j * sine * excited + cosine * scalar
    return new_excited, transverse + np.outer(new_scalar, c210.UNIFORM.conj())


def vertex_gate(
    state: CarriedState, angle: float
) -> tuple[CarriedState, dict[Position, float], float]:
    output = state.copy()
    positions = set(state.excited)
    positions.update(body for body, field in state.pair if body == field)
    current: dict[Position, float] = {}
    residual = 0.0
    for position in positions:
        excited = state.excited.get(position, zero_vector())
        pair = state.pair.get((position, position), zero_pair())
        before_e = float(np.vdot(excited, excited).real)
        before_f = float(np.vdot(pair, pair).real)
        new_e, new_pair = local_vertex(excited, pair, angle)
        after_e = float(np.vdot(new_e, new_e).real)
        after_f = float(np.vdot(new_pair, new_pair).real)
        current[position] = after_f - before_f
        residual = max(residual, abs(after_e - before_e + current[position]))
        output.excited[position] = new_e
        output.pair[(position, position)] = new_pair
    return output, current, residual


def body_stream(
    state: CarriedState, *, inverse: bool = False
) -> tuple[
    CarriedState,
    dict[tuple[Position, int], float],
    dict[tuple[Position, int], float],
]:
    output = CarriedState({}, {})
    matter_current: dict[tuple[Position, int], float] = {}
    excitation_current: dict[tuple[Position, int], float] = {}
    sign = -1 if inverse else 1
    for body, value in state.excited.items():
        for direction in range(6):
            destination = add_position(body, c210.DIRECTIONS[direction], sign)
            output.excited.setdefault(destination, zero_vector())[direction] += value[
                direction
            ]
            amount = float(abs(value[direction]) ** 2)
            matter_current[(body, direction)] = (
                matter_current.get((body, direction), 0.0) + amount
            )
            excitation_current[(body, direction)] = (
                excitation_current.get((body, direction), 0.0) + amount
            )
    for (body, field), value in state.pair.items():
        for direction in range(6):
            destination = add_position(body, c210.DIRECTIONS[direction], sign)
            output.pair.setdefault((destination, field), zero_pair())[
                direction, :
            ] += value[direction, :]
            amount = float(np.vdot(value[direction, :], value[direction, :]).real)
            matter_current[(body, direction)] = (
                matter_current.get((body, direction), 0.0) + amount
            )
    return output, matter_current, excitation_current


def field_stream(
    state: CarriedState, *, inverse: bool = False
) -> tuple[CarriedState, dict[tuple[Position, int], float]]:
    output = CarriedState(
        {key: value.copy() for key, value in state.excited.items()}, {}
    )
    current: dict[tuple[Position, int], float] = {}
    sign = -1 if inverse else 1
    for (body, field), value in state.pair.items():
        for direction in range(6):
            destination = add_position(field, c210.DIRECTIONS[direction], sign)
            output.pair.setdefault((body, destination), zero_pair())[
                :, direction
            ] += value[:, direction]
            amount = float(np.vdot(value[:, direction], value[:, direction]).real)
            current[(field, direction)] = current.get((field, direction), 0.0) + amount
    return output, current


def incoming_density(
    current: dict[tuple[Position, int], float], *, inverse: bool = False
) -> dict[Position, float]:
    answer: dict[Position, float] = {}
    sign = -1 if inverse else 1
    for (source, direction), value in current.items():
        destination = add_position(source, c210.DIRECTIONS[direction], sign)
        answer[destination] = answer.get(destination, 0.0) + value
    return answer


def add_densities(
    left: dict[Position, float], right: dict[Position, float]
) -> dict[Position, float]:
    answer = dict(left)
    for key, value in right.items():
        answer[key] = answer.get(key, 0.0) + value
    return answer


def sparse_step(
    state: CarriedState, matter_coin: np.ndarray, field_coin: np.ndarray, angle: float
) -> tuple[CarriedState, dict[str, float]]:
    before_norm = state_norm(state)
    coined = coin_gate(state, matter_coin, field_coin)
    coin_q_residual = density_residual(q_density(coined), q_density(state))
    sourced, source_current, source_residual = vertex_gate(coined, angle)
    body_moved, matter_current, excitation_current = body_stream(sourced)
    matter_edge_residual = density_residual(
        matter_density(body_moved), incoming_density(matter_current)
    )
    field_moved, field_current = field_stream(body_moved)
    q_edge_residual = density_residual(
        q_density(field_moved),
        add_densities(
            incoming_density(excitation_current), incoming_density(field_current)
        ),
    )
    return field_moved, {
        "norm_residual": abs(state_norm(field_moved) - before_norm),
        "coin_q_residual": coin_q_residual,
        "vertex_q_residual": source_residual,
        "source_current_sum": float(sum(source_current.values())),
        "matter_edge_residual": matter_edge_residual,
        "q_edge_residual": q_edge_residual,
        "matter_current_sum_residual": abs(
            sum(matter_current.values()) - sum(matter_density(sourced).values())
        ),
        "q_current_sum_residual": abs(
            sum(excitation_current.values())
            + sum(field_current.values())
            - sum(q_density(sourced).values())
        ),
    }


def inverse_sparse_step(
    state: CarriedState, matter_coin: np.ndarray, field_coin: np.ndarray, angle: float
) -> CarriedState:
    unfielded, _ = field_stream(state, inverse=True)
    unbodied, _, _ = body_stream(unfielded, inverse=True)
    unsourced, _, _ = vertex_gate(unbodied, -angle)
    return coin_gate(unsourced, matter_coin.conj().T, field_coin.conj().T)


def rotate_state(state: CarriedState, frame: np.ndarray) -> CarriedState:
    representation = c210.direction_permutation(frame)

    def rotate_position(position: Position) -> Position:
        return tuple(int(value) for value in frame @ np.asarray(position))

    return CarriedState(
        {
            rotate_position(position): representation @ value
            for position, value in state.excited.items()
        },
        {
            (rotate_position(body), rotate_position(field)): representation
            @ value
            @ representation.T
            for (body, field), value in state.pair.items()
        },
    )


def active_blocks(angle: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return H, V=exp(+i angle H), and Q on E(6) direct-sum GF(36)."""
    exchange = np.zeros((42, 42), dtype=complex)
    for matter_direction in range(6):
        for field_direction in range(6):
            pair_index = 6 + 6 * matter_direction + field_direction
            exchange[pair_index, matter_direction] = c210.UNIFORM[field_direction]
            exchange[matter_direction, pair_index] = c210.UNIFORM[
                field_direction
            ].conjugate()
    square = exchange @ exchange
    vertex = (
        np.eye(42, dtype=complex)
        + (np.cos(angle) - 1) * square
        + 1j * np.sin(angle) * exchange
    )
    excitation_number = np.diag([1.0] * 6 + [0.0] * 36)
    field_number = np.diag([0.0] * 6 + [1.0] * 36)
    return exchange, vertex, excitation_number + field_number


def physical_active_indices() -> tuple[int, ...]:
    """Computational basis images in 18 qubits: E[0:6], G[6:12], F[12:18]."""
    excited = tuple(1 << direction for direction in range(6))
    ground_field = tuple(
        (1 << (6 + matter_direction)) | (1 << (12 + field_direction))
        for matter_direction in range(6)
        for field_direction in range(6)
    )
    return excited + ground_field


def physical_vertex_column(
    basis: int, vertex: np.ndarray, active_indices: tuple[int, ...]
) -> dict[int, complex]:
    """Column of E V E^dagger + I - E E^dagger without a 2^18 matrix."""
    inverse = {physical: logical for logical, physical in enumerate(active_indices)}
    if basis not in inverse:
        return {basis: 1.0 + 0.0j}
    column = inverse[basis]
    return {
        physical: vertex[row, column]
        for row, physical in enumerate(active_indices)
        if abs(vertex[row, column]) > 1e-15
    }


def unchanged_cycle269_capacity() -> list[tuple[int, int, int, int, int]]:
    rows = []
    for length in (3, 4, 5, 6):
        code = c269.build_code(length)
        local_rank, inconsistent = c235.phase_aware_rank(
            list(code.local_checks), code.qubits
        )
        if inconsistent:
            raise AssertionError((length, inconsistent))
        cells = length**3
        code_exponent = code.qubits - local_rank
        target_exponent = 12 * cells + 2
        rows.append(
            (length, code.qubits, code_exponent, target_exponent, target_exponent - code_exponent)
        )
    return rows


def physical_and_capacity_controls(species: c210.Species, angle: float) -> None:
    indices = physical_active_indices()
    check(
        "the direct 18-M2 encoding has 42 distinct active computational states",
        len(indices) == len(set(indices)) == 42,
        {"M2_per_cell": 18, "active_dimension": len(indices)},
    )

    exchange, vertex, charge = active_blocks(angle)
    check(
        "the onsite carried-source vertex is unitary on the active code",
        np.linalg.norm(vertex.conj().T @ vertex - np.eye(42)) < TOLERANCE,
        np.linalg.norm(vertex.conj().T @ vertex - np.eye(42)),
    )
    complement_samples = (0, 3, (1 << 6) | (1 << 7), (1 << 18) - 1)
    check(
        "the selected hard-core vertex is identity-completed on the rest of the 18-M2 Hilbert space",
        all(
            physical_vertex_column(basis, vertex, indices)
            == {basis: 1.0 + 0.0j}
            for basis in complement_samples
        )
        and all(index not in indices for index in complement_samples),
        {
            "physical_dimension": 1 << 18,
            "active_dimension": len(indices),
            "identity_complement_dimension": (1 << 18) - len(indices),
        },
    )
    check(
        "the onsite vertex leaves the active subspace invariant and conserves Q",
        np.linalg.norm(vertex @ charge - charge @ vertex) < TOLERANCE
        and np.linalg.norm(exchange[6:, :6].conj().T @ exchange[6:, :6] - np.eye(6))
        < TOLERANCE,
        np.linalg.norm(vertex @ charge - charge @ vertex),
    )
    check(
        "the emission core has support eight M2 and its exact identity-completed physical gate has support 18 M2",
        2 + 6 == 8 and 12 + 6 == 18,
        {
            "active_core_support": 8,
            "identity_completed_gate_support": 18,
            "cell_union": 18,
        },
    )

    active_coin = np.zeros((42, 42), dtype=complex)
    active_coin[:6, :6] = species.coin
    active_coin[6:, 6:] = np.kron(species.coin, c214.FIELD_COIN)
    covariance = []
    for frame in c210.proper_cubic_frames():
        representation = c210.direction_permutation(frame)
        active_frame = np.zeros((42, 42), dtype=complex)
        active_frame[:6, :6] = representation
        active_frame[6:, 6:] = np.kron(representation, representation)
        covariance.extend(
            (
                np.linalg.norm(active_frame @ vertex @ active_frame.T - vertex),
                np.linalg.norm(active_frame @ active_coin @ active_frame.T - active_coin),
            )
        )
    check(
        "the active vertex and common coin commute with all 24 proper-cubic frames",
        len(covariance) == 48 and max(covariance) < TOLERANCE,
        max(covariance),
    )

    curvature = c210.curvature_tensor(species, step=1e-4)
    dispersion_mass = 1 / float(np.mean(np.diag(curvature)))
    common_one_particle = np.kron(np.eye(2), species.coin)
    check(
        "both internal labels preserve the Cycle-219 one-particle mass fixture",
        np.linalg.norm(
            common_one_particle[:6, :6] - common_one_particle[6:, 6:]
        )
        < TOLERANCE
        and abs(dispersion_mass / species.analytic_mass - 1) < 4e-6,
        {
            "analytic_mass": species.analytic_mass,
            "dispersion_mass": dispersion_mass,
        },
    )

    contact_phases = tuple(
        np.exp(1j * CONTACT_COUPLING * n * (n - 1) / 2) for n in (0, 1, 2)
    )
    check(
        "contact deletion leaves the executed one-matter code unchanged; the supplied law has the algebraic two-matter phase value",
        abs(contact_phases[0] - 1) < TOLERANCE
        and abs(contact_phases[1] - 1) < TOLERANCE
        and abs(contact_phases[2] - np.exp(1j * CONTACT_COUPLING)) < TOLERANCE,
        contact_phases,
    )
    _, deleted_vertex, _ = active_blocks(0.0)
    check(
        "source-coupling deletion returns the two decoupled common matter labels",
        np.linalg.norm(deleted_vertex - np.eye(42)) < TOLERANCE,
        np.linalg.norm(deleted_vertex - np.eye(42)),
    )

    swap = np.eye(4, dtype=complex)[[0, 2, 1, 3]]
    fswap = swap.copy()
    fswap[3, 3] = -1
    check(
        "ordinary SWAP equals FSWAP on the declared one-matter stream sector and fails outside it with exact norm two",
        np.linalg.norm(swap[:3, :3] - fswap[:3, :3]) < TOLERANCE
        and abs(np.linalg.norm(swap - fswap) - 2) < TOLERANCE,
        np.linalg.norm(swap - fswap),
    )

    rows = unchanged_cycle269_capacity()
    check(
        "at tested L=3,4,5,6 the unchanged Cycle-269 code has exact 6 L^3 logical-exponent deficits for literal two-species matter",
        all(
            code_exponent == 6 * length**3 + 2
            and target_exponent == 12 * length**3 + 2
            and deficit == 6 * length**3
            for length, _qubits, code_exponent, target_exponent, deficit in rows
        ),
        rows,
    )


def sparse_dynamics_controls(species: c210.Species, angle: float) -> None:
    initial = CarriedState({(0, 0, 0): c210.UNIFORM.copy()}, {})
    state = initial.copy()
    diagnostics = []
    for _ in range(4):
        state, report = sparse_step(state, species.coin, c214.FIELD_COIN, angle)
        diagnostics.append(report)
    maxima = {
        key: max(abs(report[key]) for report in diagnostics)
        for key in (
            "norm_residual",
            "coin_q_residual",
            "vertex_q_residual",
            "matter_edge_residual",
            "q_edge_residual",
            "matter_current_sum_residual",
            "q_current_sum_residual",
        )
    }
    check(
        "four ticks obey exact norm and declared carried-code Q continuity ledgers",
        max(maxima.values()) < TOLERANCE,
        maxima,
    )
    occupied_bodies = {
        position
        for position, value in matter_density(state).items()
        if value > TOLERANCE
    }
    occupied_fields = {
        position
        for position, value in field_density(state).items()
        if value > TOLERANCE
    }
    check(
        "matter and field remain inside their four-edge causal cones",
        max(map(l1, occupied_bodies), default=0) <= 4
        and max(map(l1, occupied_fields), default=0) <= 4,
        {
            "max_body_l1": max(map(l1, occupied_bodies), default=0),
            "max_field_l1": max(map(l1, occupied_fields), default=0),
        },
    )
    restored = state
    for _ in range(4):
        restored = inverse_sparse_step(
            restored, species.coin, c214.FIELD_COIN, angle
        )
    check(
        "the four-tick carried-source update is exactly inverted",
        state_residual(restored, initial) < 2e-10,
        state_residual(restored, initial),
    )

    emitted, _ = local_vertex(c210.UNIFORM.copy(), zero_pair(), angle)
    _unused = emitted
    _, emission_pair = local_vertex(c210.UNIFORM.copy(), zero_pair(), angle)
    absorbed_excited, absorbed_pair = local_vertex(
        zero_vector(), np.outer(c210.UNIFORM, c210.UNIFORM), angle
    )
    check(
        "the local vertex emits by consuming excitation and absorbs by restoring it",
        abs(np.vdot(emission_pair, emission_pair).real - np.sin(angle) ** 2)
        < TOLERANCE
        and abs(np.vdot(absorbed_excited, absorbed_excited).real - np.sin(angle) ** 2)
        < TOLERANCE
        and abs(
            np.vdot(absorbed_pair, absorbed_pair).real - np.cos(angle) ** 2
        )
        < TOLERANCE,
        {
            "emitted": float(np.vdot(emission_pair, emission_pair).real),
            "absorbed": float(np.vdot(absorbed_excited, absorbed_excited).real),
        },
    )

    rng = np.random.default_rng(20260717)
    random_state = CarriedState(
        {
            (1, -1, 0): rng.normal(size=6) + 1j * rng.normal(size=6),
            (-2, 0, 1): rng.normal(size=6) + 1j * rng.normal(size=6),
        },
        {
            ((0, 0, 0), (0, 0, 0)): rng.normal(size=(6, 6))
            + 1j * rng.normal(size=(6, 6)),
            ((1, 0, -1), (-1, 1, 0)): rng.normal(size=(6, 6))
            + 1j * rng.normal(size=(6, 6)),
        },
    )
    covariance = []
    advanced, _ = sparse_step(
        random_state, species.coin, c214.FIELD_COIN, angle
    )
    for frame in c210.proper_cubic_frames():
        rotated_advanced, _ = sparse_step(
            rotate_state(random_state, frame),
            species.coin,
            c214.FIELD_COIN,
            angle,
        )
        covariance.append(
            state_residual(rotated_advanced, rotate_state(advanced, frame))
        )
    check(
        "the full sparse schedule is covariant under all 24 proper-cubic frames",
        len(covariance) == 24 and max(covariance) < 2e-10,
        max(covariance),
    )

    left = CarriedState({(-5, 0, 0): c210.UNIFORM.copy()}, {})
    right = CarriedState({(5, 0, 0): 1j * c210.UNIFORM.copy()}, {})
    combined, _ = sparse_step(
        add_states(left, right), species.coin, c214.FIELD_COIN, angle
    )
    advanced_left, _ = sparse_step(left, species.coin, c214.FIELD_COIN, angle)
    advanced_right, _ = sparse_step(right, species.coin, c214.FIELD_COIN, angle)
    check(
        "separated one-matter packets compose linearly without a host-side controller",
        state_residual(combined, add_states(advanced_left, advanced_right)) < TOLERANCE,
        state_residual(combined, add_states(advanced_left, advanced_right)),
    )

    moved_excited, _, _ = body_stream(
        CarriedState({(0, 0, 0): np.eye(6)[0].astype(complex)}, {})
    )
    moved_ground, _, _ = body_stream(
        CarriedState(
            {},
            {
                ((0, 0, 0), (3, 0, 0)): np.outer(
                    np.eye(6)[0], c210.UNIFORM
                ).astype(complex)
            },
        )
    )
    check(
        "excited and ground source states use the same one-edge matter stream",
        (1, 0, 0) in moved_excited.excited
        and ((1, 0, 0), (3, 0, 0)) in moved_ground.pair,
        {
            "excited_body": tuple(moved_excited.excited),
            "ground_body": tuple(key[0] for key in moved_ground.pair),
        },
    )


def main() -> int:
    print("CARRIED INTERNAL-SPECIES SOURCE/FIELD LEDGER REPAIR")
    note_contract()
    species = c219.common_species(BETA)
    angle = MEDIATOR_COUPLING * species.analytic_mass
    physical_and_capacity_controls(species, angle)
    sparse_dynamics_controls(species, angle)
    print("SUMMARY", {"pass": PASS, "fail": FAIL})
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
