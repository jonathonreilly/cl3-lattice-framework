"""Explicit finite label-space model extracted from Cycle320/322 for #7871.

This module runs no historical controller and imports no physical compiler.
RECOVERY.json binds complete original functions/data. Namespace substitutions
below remove the unused parent tower; the finite definitions are unchanged.
The supplied angle has historical parameter origin 0.8 * 3*tan(-(-0.3)/2).
It is not selected by framework axioms. No separate transported F/A factor is
introduced: their equal diagonals are labels on the same seven-state factor.
"""
from __future__ import annotations
from dataclasses import dataclass
from functools import lru_cache
from itertools import combinations
import numpy as np
from scipy.linalg import expm

DIRECTIONS = np.asarray(((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)), dtype=int)
REVERSE = (1,0,3,2,5,4)
ANGLE = 0.8 * float(3 * np.tan(0.15))
Position = tuple[int,int,int]
QKey = tuple
LogicalState = dict
ENDPOINTS = ((0,0,0),(1,0,0))
LOCAL_LABELS = tuple((n, c) for n in range(7) for c in combinations(range(6), n))
LOCAL_MASKS = tuple(sum(1 << d for d in c) for n,c in LOCAL_LABELS)
LOCAL_INDEX = {mask:i for i,mask in enumerate(LOCAL_MASKS)}
LABELS = tuple((ln,ll,rn,rl) for ln,ll in LOCAL_LABELS for rn,rl in LOCAL_LABELS)
JOINT_INDEX = {(LOCAL_INDEX[sum(1 << d for d in ll)],LOCAL_INDEX[sum(1 << d for d in rl)]):i for i,(ln,ll,rn,rl) in enumerate(LABELS)}


def zero_tensor() -> np.ndarray:
    return np.zeros((6, 6, 6), dtype=complex)


@dataclass
class LinkState:
    """One matter carrier: excited/no field/aux or ground/field/carried aux."""

    excited: dict[Position, np.ndarray]
    pair: dict[tuple[Position, Position], np.ndarray]

    def copy(self) -> "LinkState":
        return LinkState(
            {key: value.copy() for key, value in self.excited.items()},
            {key: value.copy() for key, value in self.pair.items()},
        )


def link_recoil_vertex(
    angle: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, tuple[np.ndarray, ...]]:
    dimension = 6 + 6**3
    exchange = np.zeros((dimension, dimension), dtype=complex)
    for direction in range(6):
        pair_index = 6 + 36 * REVERSE[direction] + 6 * direction + direction
        exchange[pair_index, direction] = 1.0
        exchange[direction, pair_index] = 1.0
    square = exchange @ exchange
    vertex = (
        np.eye(dimension, dtype=complex)
        + (np.cos(angle) - 1) * square
        + 1j * np.sin(angle) * exchange
    )
    charge = np.eye(dimension, dtype=complex)
    momenta = []
    for axis in range(3):
        values = [float(DIRECTIONS[d, axis]) for d in range(6)]
        values.extend(
            float(
                DIRECTIONS[matter, axis]
                + DIRECTIONS[field, axis]
                + DIRECTIONS[auxiliary, axis]
            )
            for matter in range(6)
            for field in range(6)
            for auxiliary in range(6)
        )
        momenta.append(np.diag(values))
    return exchange, vertex, charge, tuple(momenta)


def vector_expectation(excited: np.ndarray, pair: np.ndarray) -> np.ndarray:
    probabilities = abs(pair) ** 2
    matter_weights = abs(excited) ** 2 + np.sum(probabilities, axis=(1, 2))
    field_weights = np.sum(probabilities, axis=(0, 2))
    auxiliary_weights = np.sum(probabilities, axis=(0, 1))
    return (
        matter_weights @ DIRECTIONS
        + field_weights @ DIRECTIONS
        + auxiliary_weights @ DIRECTIONS
    )


def local_vertex(
    excited: np.ndarray, contact_pair: np.ndarray, angle: float
) -> tuple[np.ndarray, np.ndarray]:
    _exchange, vertex, _charge, _momenta = link_recoil_vertex(angle)
    vector = np.concatenate((excited, contact_pair.reshape(-1)))
    output = vertex @ vector
    return output[:6], output[6:].reshape(6, 6, 6)


def vertex_gate(state: LinkState, angle: float) -> tuple[LinkState, dict[str, object]]:
    output = state.copy()
    positions = set(state.excited)
    positions.update(body for body, field in state.pair if body == field)
    q_residual = 0.0
    p_residual = 0.0
    source_current: dict[Position, float] = {}
    for position in positions:
        excited = state.excited.get(position, np.zeros(6, dtype=complex))
        pair = state.pair.get((position, position), zero_tensor())
        before_q = float(np.vdot(excited, excited).real + np.vdot(pair, pair).real)
        before_p = vector_expectation(excited, pair)
        new_excited, new_pair = local_vertex(excited, pair, angle)
        after_q = float(
            np.vdot(new_excited, new_excited).real + np.vdot(new_pair, new_pair).real
        )
        after_p = vector_expectation(new_excited, new_pair)
        q_residual = max(q_residual, abs(after_q - before_q))
        p_residual = max(p_residual, float(np.linalg.norm(after_p - before_p)))
        source_current[position] = float(
            np.vdot(new_pair, new_pair).real - np.vdot(pair, pair).real
        )
        output.excited[position] = new_excited
        output.pair[(position, position)] = new_pair
    return output, {
        "local_Q_residual": q_residual,
        "local_P_residual": p_residual,
        "source_current": source_current,
    }

def fermion_hop(mask: int, source: int, target: int) -> tuple[int, int] | None:
    if not ((mask >> source) & 1) or ((mask >> target) & 1):
        return None
    sign = (-1) ** ((mask & ((1 << source) - 1)).bit_count())
    reduced = mask ^ (1 << source)
    sign *= (-1) ** ((reduced & ((1 << target) - 1)).bit_count())
    return reduced | (1 << target), sign


@lru_cache(maxsize=None)
def local_source_blocks(angle: float):
    exchange = np.zeros((448, 448), dtype=complex)
    for source_index, mask in enumerate(LOCAL_MASKS):
        for direction in range(6):
            hopped = fermion_hop(mask, direction, REVERSE[direction])
            if hopped is None:
                continue
            target_mask, sign = hopped
            target_index = LOCAL_INDEX[target_mask]
            reservoir_index = 7 * source_index
            field_index = 7 * target_index + 1 + direction
            exchange[field_index, reservoir_index] += sign
            exchange[reservoir_index, field_index] += sign
    vertex = expm(1j * angle * exchange)
    charge = np.eye(448, dtype=complex)
    number_values = np.repeat(
        [mask.bit_count() for mask in LOCAL_MASKS], 7
    )
    number = np.diag(number_values)
    momenta = []
    for axis in range(3):
        values = []
        for mask in LOCAL_MASKS:
            matter_vector = sum(
                (
                    DIRECTIONS[d]
                    for d in range(6)
                    if (mask >> d) & 1
                ),
                start=np.zeros(3, dtype=int),
            )
            values.append(float(matter_vector[axis]))
            values.extend(
                float(matter_vector[axis] + 2 * DIRECTIONS[d, axis])
                for d in range(6)
            )
        momenta.append(np.diag(values))
    return exchange, vertex, charge, number, tuple(momenta)


def q_reservoir(endpoint: int) -> QKey:
    return ("R", endpoint)


def q_field(cell: tuple[int, int, int], direction: int) -> QKey:
    return ("F", cell, direction)


def prune(state: dict, threshold: float = 2e-13) -> dict:
    return {key: value for key, value in state.items() if np.linalg.norm(value) > threshold}


def state_norm(state: dict) -> float:
    return float(sum(np.vdot(value, value).real for value in state.values()))


def state_residual(left: dict, right: dict) -> float:
    if not left and not right:
        return 0.0
    sample = next(iter(left.values()), next(iter(right.values())))
    zero = np.zeros_like(sample)
    return float(
        np.sqrt(
            sum(
                np.vdot(left.get(key, zero) - right.get(key, zero), left.get(key, zero) - right.get(key, zero)).real
                for key in left.keys() | right.keys()
            )
        )
    )


def apply_source(
    state: LogicalState,
    endpoint: int,
    endpoint_cells=ENDPOINTS,
    *,
    angle: float = ANGLE,
    inverse: bool = False,
) -> LogicalState:
    _exchange, vertex, _charge, _number, _momenta = local_source_blocks(angle)
    if inverse:
        vertex = vertex.conj().T
    cell = endpoint_cells[endpoint]
    active_keys = (q_reservoir(endpoint),) + tuple(
        q_field(cell, direction) for direction in range(6)
    )
    output = {key: value.copy() for key, value in state.items() if key not in active_keys}
    for key in active_keys:
        output[key] = np.zeros(4096, dtype=complex)
    zero = np.zeros(4096, dtype=complex)
    inputs = {key: state.get(key, zero) for key in active_keys}
    for other_index in range(64):
        local_vector = np.zeros(448, dtype=complex)
        for local_index in range(64):
            joint_index = (
                JOINT_INDEX[(local_index, other_index)]
                if endpoint == 0
                else JOINT_INDEX[(other_index, local_index)]
            )
            for q_index, key in enumerate(active_keys):
                local_vector[7 * local_index + q_index] = inputs[key][joint_index]
        local_output = vertex @ local_vector
        for local_index in range(64):
            joint_index = (
                JOINT_INDEX[(local_index, other_index)]
                if endpoint == 0
                else JOINT_INDEX[(other_index, local_index)]
            )
            for q_index, key in enumerate(active_keys):
                output[key][joint_index] = local_output[7 * local_index + q_index]
    return prune(output)
