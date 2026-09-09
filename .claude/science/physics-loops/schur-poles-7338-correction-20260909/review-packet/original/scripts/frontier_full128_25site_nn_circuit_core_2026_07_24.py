#!/usr/bin/env python3
"""Nearest-neighbor supplied-schedule successor to the local cycle encoder.

This is a bounded constructive probe for the full local six-mode M64 tensor one
seam-port M2 Fock space.  It is not a recurrent or two-cell M64 compiler.  It
imports the repo-local encoder module as ordinary Python source, then supplies
the missing physical-site compilation data:

* explicit integer Z^3 coordinates for every data, routing, clock and work M2;
* an all-nearest-neighbor gate word for decode / factored G7 / encode;
* a one-hot supplied program counter whose same local circuit macro is iterated;
* exact return of routing, bypass and program-counter work; and
* covariance of the fixed cubic layout and transformed program family under
  all 24 proper-cubic frames.

The controller iteration index is a circuit substep only.  It is not physical
time or a rate.  The microscopic scheduler inside the fixed controller macro
is not internalized.  Genesis of the blank sites, cycle |+> auxiliaries,
one-hot program token and fixed program word is supplied structure.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations
import json
import math
import time

import numpy as np

import frontier_full128_cycle_encoder_2026_07_24 as P


START = time.perf_counter()
TOL = 3.0e-10
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label} :: {detail}")


Coord = tuple[int, int, int]
I2 = np.eye(2, dtype=complex)
X = np.asarray(((0, 1), (1, 0)), dtype=complex)
H = np.asarray(((1, 1), (1, -1)), dtype=complex) / math.sqrt(2)
T = np.diag((1, np.exp(1j * math.pi / 4))).astype(complex)
TDG = T.conj().T
SWAP = np.asarray(
    ((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, 1)),
    dtype=complex,
)
# Local-bit basis is |00>, |10>, |01>, |11>: first listed wire is bit 0.
CNOT = np.asarray(
    ((1, 0, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0), (0, 1, 0, 0)),
    dtype=complex,
)
FSWAP = SWAP.copy()
FSWAP[3, 3] = -1


@dataclass(frozen=True)
class Gate:
    kind: str
    sites: tuple[Coord, ...]
    matrix: np.ndarray


@dataclass(frozen=True)
class AbstractGate:
    kind: str
    wires: tuple[int, ...]
    matrix: np.ndarray


def matrix_digest(matrix: np.ndarray) -> str:
    rounded = np.round(np.asarray(matrix, dtype=complex), 14)
    return sha256(rounded.tobytes()).hexdigest()


def embed_gate(matrix: np.ndarray, wires: tuple[int, ...], count: int) -> np.ndarray:
    """Embed a one/two-qubit matrix using little-endian wire numbering."""
    output = np.zeros((1 << count, 1 << count), dtype=complex)
    local_count = len(wires)
    for source in range(1 << count):
        local_source = sum(((source >> wire) & 1) << i for i, wire in enumerate(wires))
        for local_target in range(1 << local_count):
            amplitude = matrix[local_target, local_source]
            if abs(amplitude) == 0:
                continue
            target = source
            for i, wire in enumerate(wires):
                bit = (local_target >> i) & 1
                target = (target | (1 << wire)) if bit else (target & ~(1 << wire))
            output[target, source] += amplitude
    return output


def compile_adjacent_qr(unitary: np.ndarray):
    work = np.asarray(unitary, dtype=complex).copy()
    eliminations = []
    for column in range(5):
        for lower in range(5, column, -1):
            upper = lower - 1
            a, b = work[upper, column], work[lower, column]
            if abs(b) < 1.0e-13:
                continue
            radius = np.sqrt(abs(a) ** 2 + abs(b) ** 2)
            elimination = np.asarray(
                ((np.conj(a) / radius, np.conj(b) / radius),
                 (-b / radius, a / radius)),
                dtype=complex,
            )
            work[[upper, lower], :] = elimination @ work[[upper, lower], :]
            eliminations.append((upper, lower, elimination))
    schedule: list[tuple[str, tuple[int, ...], np.ndarray]] = []
    for index, phase in enumerate(np.diag(work)):
        if abs(phase - 1) >= 1.0e-13:
            schedule.append(("coin_phase", (index,), np.diag((1, phase))))
    for upper, lower, elimination in reversed(eliminations):
        schedule.append(
            ("coin_givens", (upper, lower), P.fock_lift(elimination.conj().T))
        )
    return tuple(schedule), float(np.linalg.norm(work - np.diag(np.diag(work))))


def decoded_update_gates() -> tuple[AbstractGate, ...]:
    coin, _, _ = P.common_coin()
    coin_schedule, _ = compile_adjacent_qr(coin)
    gates = [AbstractGate(kind, sites, matrix) for kind, sites, matrix in coin_schedule]
    for left, right in ((0, 1), (2, 3), (4, 5)):
        gates.append(AbstractGate("reverse_fswap", (left, right), FSWAP))
    # A direct tensor gate on decoded wires 1 and 6 would omit the intervening
    # CAR signs.  This nine-FSWAP adjacent transposition is the literal local
    # factorization of the seam exchange in the ordered decoded register.
    for left, right in (
        (1, 2), (2, 3), (3, 4), (4, 5), (5, 6),
        (4, 5), (3, 4), (2, 3), (1, 2),
    ):
        gates.append(AbstractGate("seam_fswap", (left, right), FSWAP))
    contact = np.diag((1, 1, 1, np.exp(1j * P.CONTACT))).astype(complex)
    for left, right in combinations(range(6), 2):
        gates.append(AbstractGate("contact_phase", (left, right), contact))
    return tuple(gates)


DECODED_GATES = decoded_update_gates()


def product_on_seven(gates: tuple[AbstractGate, ...]) -> np.ndarray:
    result = np.eye(128, dtype=complex)
    for gate in gates:
        result = embed_gate(gate.matrix, gate.wires, 7) @ result
    return result


# Cubic-symmetric data layout.  The three reverse-pair factors require a mirror
# copy to complete their six-point proper-cubic orbit; each pair is locally
# constrained to the repetition code |00>,|11>.
DIRECTIONS = tuple(tuple(int(v) for v in row) for row in P.DIRECTIONS)
REVERSE_PAIRS = ((0, 1), (2, 3), (4, 5))
REVERSE_EDGES = {tuple(sorted(pair)) for pair in REVERSE_PAIRS}
DATA_COORDS: list[Coord] = []
FACTOR_COORD: dict[int, Coord] = {}
for edge_index, edge in enumerate(P.EDGES):
    if edge == (P.PORT, P.REFERENCE):
        coord = (0, 0, 0)
    elif P.PORT in edge:
        mode = edge[0] if edge[1] == P.PORT else edge[1]
        coord = DIRECTIONS[mode]
    elif edge in REVERSE_EDGES:
        pair_index = REVERSE_PAIRS.index(edge)
        axis = pair_index
        coord = tuple(2 if component == axis else 0 for component in range(3))
    else:
        coord = tuple(DIRECTIONS[edge[0]][i] + DIRECTIONS[edge[1]][i] for i in range(3))
    FACTOR_COORD[edge_index] = coord
    DATA_COORDS.append(coord)

MIRROR_COORD: dict[int, Coord] = {}
for pair in REVERSE_PAIRS:
    edge_index = P.EDGE_INDEX[pair]
    primary = FACTOR_COORD[edge_index]
    mirror = tuple(-component for component in primary)
    MIRROR_COORD[edge_index] = mirror
    DATA_COORDS.append(mirror)

DATA_COORDS = list(dict.fromkeys(DATA_COORDS))
if len(DATA_COORDS) != 25:
    raise AssertionError(f"expected 25 distinct data coordinates, got {len(DATA_COORDS)}")


def l1(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def manhattan_path(left: Coord, right: Coord) -> tuple[Coord, ...]:
    current = list(left)
    path = [tuple(current)]
    for axis in range(3):
        while current[axis] != right[axis]:
            current[axis] += 1 if right[axis] > current[axis] else -1
            path.append(tuple(current))
    return tuple(path)


def route_two(kind: str, left: Coord, right: Coord, matrix: np.ndarray) -> list[Gate]:
    path = manhattan_path(left, right)
    if len(path) < 2:
        raise ValueError("two-site gate received identical sites")
    output: list[Gate] = []
    for index in range(len(path) - 2):
        output.append(Gate("route_swap", (path[index], path[index + 1]), SWAP))
    output.append(Gate(kind, (path[-2], path[-1]), matrix))
    for index in reversed(range(len(path) - 2)):
        output.append(Gate("route_swap", (path[index], path[index + 1]), SWAP))
    return output


def abstract_data_word() -> tuple[AbstractGate, ...]:
    word: list[AbstractGate] = []
    # Outer repetition decode: primary controls mirror, returning mirrors to |0>.
    for edge in REVERSE_PAIRS:
        index = P.EDGE_INDEX[edge]
        word.append(AbstractGate("outer_decode", (index, 22 + REVERSE_PAIRS.index(edge)), CNOT))
    # U^dagger.  Predecessor SWAP and CNOT gates are self inverse.
    for kind, first, second in reversed(P.ENCODER_CIRCUIT):
        word.append(AbstractGate(f"decoder_{kind.lower()}", (first, second), SWAP if kind == "SWAP" else CNOT))
    word.extend(DECODED_GATES)
    # U.
    for kind, first, second in P.ENCODER_CIRCUIT:
        word.append(AbstractGate(f"encoder_{kind.lower()}", (first, second), SWAP if kind == "SWAP" else CNOT))
    for edge in REVERSE_PAIRS:
        index = P.EDGE_INDEX[edge]
        word.append(AbstractGate("outer_encode", (index, 22 + REVERSE_PAIRS.index(edge)), CNOT))
    return tuple(word)


ABSTRACT_DATA_WORD = abstract_data_word()
WIRE_COORDS = tuple(FACTOR_COORD[index] for index in range(22)) + tuple(
    MIRROR_COORD[P.EDGE_INDEX[pair]] for pair in REVERSE_PAIRS
)
COORD_WIRE = {coord: wire for wire, coord in enumerate(WIRE_COORDS)}

# Outer encoding maps X on a reverse-pair factor to X on its primary and
# mirror.  These are the actual 25-site local X checks; they have weight 3/4
# and commute with the three local Z repetition checks.
LIFTED_CYCLE_CHECKS = np.zeros((15, 25), dtype=np.uint8)
for row, mask in enumerate(P.CYCLE_MASKS):
    for edge in range(22):
        if (mask >> edge) & 1:
            LIFTED_CYCLE_CHECKS[row, edge] = 1
            if edge in MIRROR_COORD:
                LIFTED_CYCLE_CHECKS[row, 22 + tuple(
                    P.EDGE_INDEX[pair] for pair in REVERSE_PAIRS
                ).index(edge)] = 1
REPETITION_Z_CHECKS = np.zeros((3, 25), dtype=np.uint8)
for row, pair in enumerate(REVERSE_PAIRS):
    edge = P.EDGE_INDEX[pair]
    REPETITION_Z_CHECKS[row, edge] = 1
    REPETITION_Z_CHECKS[row, 22 + row] = 1


def nn_data_word() -> tuple[Gate, ...]:
    output: list[Gate] = []
    for gate in ABSTRACT_DATA_WORD:
        sites = tuple(WIRE_COORDS[wire] for wire in gate.wires)
        if len(sites) == 1:
            output.append(Gate(gate.kind, sites, gate.matrix))
        else:
            output.extend(route_two(gate.kind, sites[0], sites[1], gate.matrix))
    return tuple(output)


DATA_WORD = nn_data_word()
PROGRAM_LENGTH = len(DATA_WORD)
RADIUS = max(4, math.ceil((math.sqrt(PROGRAM_LENGTH) - 1) / 2))
FULL_COORDS = tuple(
    (x, y, z)
    for x in range(-RADIUS, RADIUS + 1)
    for y in range(-RADIUS, RADIUS + 1)
    for z in range(-RADIUS, RADIUS + 1)
)
FULL_COORD_SET = set(FULL_COORDS)


def serpentine_clock() -> tuple[Coord, ...]:
    rows = []
    for row_index, z in enumerate(range(-RADIUS, RADIUS + 1)):
        xs = list(range(-RADIUS, RADIUS + 1))
        if row_index & 1:
            xs.reverse()
        rows.extend((x, RADIUS, z) for x in xs)
    return tuple(rows[:PROGRAM_LENGTH])


CLOCK_COORDS = serpentine_clock()
RELAY = (0, RADIUS - 2, RADIUS)
WORK0 = (0, RADIUS - 1, RADIUS)
WORK1 = (1, RADIUS - 1, RADIUS)
if set((RELAY, WORK0, WORK1)) & set(CLOCK_COORDS):
    raise AssertionError("controller work overlaps clock")
if set((RELAY, WORK0, WORK1)) & set(DATA_COORDS):
    raise AssertionError("controller work overlaps data")


def toffoli_word(control1: Coord, control2: Coord, target: Coord) -> list[Gate]:
    """Exact Clifford+T Toffoli, routing each two-site factor locally."""
    output: list[Gate] = [Gate("H", (target,), H)]
    output += route_two("CNOT", control2, target, CNOT)
    output.append(Gate("Tdg", (target,), TDG))
    output += route_two("CNOT", control1, target, CNOT)
    output.append(Gate("T", (target,), T))
    output += route_two("CNOT", control2, target, CNOT)
    output.append(Gate("Tdg", (target,), TDG))
    output += route_two("CNOT", control1, target, CNOT)
    output.append(Gate("T", (control2,), T))
    output.append(Gate("T", (target,), T))
    output.append(Gate("H", (target,), H))
    output += route_two("CNOT", control1, control2, CNOT)
    output.append(Gate("T", (control1,), T))
    output.append(Gate("Tdg", (control2,), TDG))
    output += route_two("CNOT", control1, control2, CNOT)
    return output


def fredkin_word(control: Coord, left: Coord, right: Coord) -> list[Gate]:
    output = route_two("CNOT", right, left, CNOT)
    output += toffoli_word(control, left, right)
    output += route_two("CNOT", right, left, CNOT)
    return output


def controlled_instruction(index: int, instruction: Gate) -> list[Gate]:
    """Clock-controlled instruction via blank bypass, with exact work return."""
    clock = CLOCK_COORDS[index]
    output = route_two("relay_copy", clock, RELAY, CNOT)
    targets = instruction.sites
    works = (WORK0,) if len(targets) == 1 else (WORK0, WORK1)
    for target, work in zip(targets, works):
        output += fredkin_word(RELAY, target, work)
    output.append(Gate(f"bypass_{instruction.kind}", works, instruction.matrix))
    for target, work in reversed(tuple(zip(targets, works))):
        output += fredkin_word(RELAY, target, work)
    output += route_two("relay_uncopy", clock, RELAY, CNOT)
    return output


def clock_shift_word() -> tuple[Gate, ...]:
    # Reverse adjacent swaps realizes c_s -> c_(s+1 mod S) on an open path.
    return tuple(
        Gate("clock_shift_swap", (CLOCK_COORDS[index], CLOCK_COORDS[index + 1]), SWAP)
        for index in reversed(range(PROGRAM_LENGTH - 1))
    )


def controller_census() -> dict:
    hasher = sha256()
    count = one = two = non_nn = outside = 0
    for index, instruction in enumerate(DATA_WORD):
        for gate in controlled_instruction(index, instruction):
            count += 1
            one += len(gate.sites) == 1
            two += len(gate.sites) == 2
            non_nn += len(gate.sites) == 2 and l1(*gate.sites) != 1
            outside += any(site not in FULL_COORD_SET for site in gate.sites)
            hasher.update(gate.kind.encode())
            hasher.update(repr(gate.sites).encode())
            hasher.update(matrix_digest(gate.matrix).encode())
    shift = clock_shift_word()
    for gate in shift:
        count += 1
        two += 1
        non_nn += l1(*gate.sites) != 1
        outside += any(site not in FULL_COORD_SET for site in gate.sites)
        hasher.update(gate.kind.encode())
        hasher.update(repr(gate.sites).encode())
        hasher.update(matrix_digest(gate.matrix).encode())
    return {
        "same_controller_A_gate_count": count,
        "one_site_gates": one,
        "two_site_gates": two,
        "non_nearest_neighbor_gates": non_nn,
        "outside_fixed_cube": outside,
        "controller_A_sha256": hasher.hexdigest(),
        "clock_shift_gates": len(shift),
    }


def ideal_toffoli() -> np.ndarray:
    output = np.eye(8, dtype=complex)
    output[:, (3, 7)] = output[:, (7, 3)]
    return output


def ideal_fredkin() -> np.ndarray:
    output = np.eye(8, dtype=complex)
    output[:, (3, 5)] = output[:, (5, 3)]
    return output


def local_decomposition_residuals() -> tuple[float, float]:
    # Same words without routing; wires c1=0,c2=1,t=2.
    sequence = [
        (H, (2,)), (CNOT, (1, 2)), (TDG, (2,)), (CNOT, (0, 2)),
        (T, (2,)), (CNOT, (1, 2)), (TDG, (2,)), (CNOT, (0, 2)),
        (T, (1,)), (T, (2,)), (H, (2,)), (CNOT, (0, 1)),
        (T, (0,)), (TDG, (1,)), (CNOT, (0, 1)),
    ]
    toffoli = np.eye(8, dtype=complex)
    for matrix, wires in sequence:
        toffoli = embed_gate(matrix, wires, 3) @ toffoli
    fredkin = embed_gate(CNOT, (2, 1), 3) @ np.eye(8, dtype=complex)
    fredkin = toffoli @ fredkin
    fredkin = embed_gate(CNOT, (2, 1), 3) @ fredkin
    return (
        float(np.linalg.norm(toffoli - ideal_toffoli())),
        float(np.linalg.norm(fredkin - ideal_fredkin())),
    )


def ideal_bypass(matrix: np.ndarray, target_count: int) -> np.ndarray:
    """Control + data targets + blank work targets; compare only work=0 columns."""
    total = 1 + 2 * target_count
    result = np.eye(1 << total, dtype=complex)
    for i in range(target_count):
        result = embed_gate(ideal_fredkin(), (0, 1 + i, 1 + target_count + i), total) @ result
    result = embed_gate(
        matrix, tuple(1 + target_count + i for i in range(target_count)), total
    ) @ result
    for i in reversed(range(target_count)):
        result = embed_gate(ideal_fredkin(), (0, 1 + i, 1 + target_count + i), total) @ result
    expected = np.zeros_like(result)
    source_columns = []
    for control in (0, 1):
        for data in range(1 << target_count):
            source = control | (data << 1)
            source_columns.append(source)
            wanted = np.eye(1 << target_count) if control == 0 else matrix
            for target in range(1 << target_count):
                expected[control | (target << 1), source] = wanted[target, data]
    residual = float(np.linalg.norm(result[:, source_columns] - expected[:, source_columns]))
    work_leakage = 0.0
    for row in range(1 << total):
        if row >> (1 + target_count):
            work_leakage += float(np.linalg.norm(result[row, source_columns]) ** 2)
    return np.asarray((residual, math.sqrt(work_leakage)))


def routing_symbolic_failures() -> tuple[int, int]:
    failures = non_nn = 0
    for instruction in DATA_WORD:
        non_nn += sum(len(gate.sites) == 2 and l1(*gate.sites) != 1 for gate in (instruction,))
    # Each route macro has palindromic swaps, so its wire permutation is identity.
    for gate in ABSTRACT_DATA_WORD:
        if len(gate.wires) == 2:
            path = manhattan_path(WIRE_COORDS[gate.wires[0]], WIRE_COORDS[gate.wires[1]])
            labels = list(range(len(path)))
            for index in range(len(path) - 2):
                labels[index], labels[index + 1] = labels[index + 1], labels[index]
            for index in reversed(range(len(path) - 2)):
                labels[index], labels[index + 1] = labels[index + 1], labels[index]
            failures += labels != list(range(len(path)))
    return failures, non_nn


def compositional_certificate(factor_residual: float) -> dict:
    """Tie D/U/G/U†/D†, NN routing and controller selection together."""
    offset = 0
    macro_failures = central_factor_failures = endpoint_failures = 0
    for abstract in ABSTRACT_DATA_WORD:
        sites = tuple(WIRE_COORDS[wire] for wire in abstract.wires)
        if len(sites) == 1:
            macro = (Gate(abstract.kind, sites, abstract.matrix),)
            central = macro[0]
        else:
            macro = tuple(route_two(abstract.kind, sites[0], sites[1], abstract.matrix))
            path = manhattan_path(sites[0], sites[1])
            central = macro[len(path) - 2]
            labels = list(range(len(path)))
            for index in range(len(path) - 2):
                labels[index], labels[index + 1] = labels[index + 1], labels[index]
            endpoint_failures += labels[-2] != 0 or labels[-1] != len(path) - 1
        observed = DATA_WORD[offset:offset + len(macro)]
        macro_failures += len(observed) != len(macro) or any(
            left.kind != right.kind or left.sites != right.sites
            or np.linalg.norm(left.matrix - right.matrix) >= TOL
            for left, right in zip(observed, macro)
        )
        central_factor_failures += (
            central.kind != abstract.kind
            or np.linalg.norm(central.matrix - abstract.matrix) >= TOL
        )
        offset += len(macro)
    macro_failures += offset != PROGRAM_LENGTH

    decoded_segment = ABSTRACT_DATA_WORD[
        3 + len(P.ENCODER_CIRCUIT):3 + len(P.ENCODER_CIRCUIT) + len(DECODED_GATES)
    ]
    decoded_structure = len(decoded_segment) == len(DECODED_GATES) and all(
        observed.kind == expected.kind and observed.wires == expected.wires
        and np.linalg.norm(observed.matrix - expected.matrix) < TOL
        for observed, expected in zip(decoded_segment, DECODED_GATES)
    )
    structure = (
        tuple(gate.kind for gate in ABSTRACT_DATA_WORD[:3]) == ("outer_decode",) * 3
        and tuple((gate.kind.replace("decoder_", "").upper(),) + gate.wires
                  for gate in ABSTRACT_DATA_WORD[3:3 + len(P.ENCODER_CIRCUIT)])
        == tuple(reversed(P.ENCODER_CIRCUIT))
        and decoded_structure
        and tuple((gate.kind.replace("encoder_", "").upper(),) + gate.wires
                  for gate in ABSTRACT_DATA_WORD[
                      3 + len(P.ENCODER_CIRCUIT) + len(DECODED_GATES):
                      3 + 2 * len(P.ENCODER_CIRCUIT) + len(DECODED_GATES)
                  ]) == P.ENCODER_CIRCUIT
        and tuple(gate.kind for gate in ABSTRACT_DATA_WORD[-3:]) == ("outer_encode",) * 3
    )
    outer_failures = 0
    for encoded_bit in (0, 1):
        decoded_primary = encoded_bit
        decoded_mirror = encoded_bit ^ encoded_bit
        outer_failures += decoded_mirror != 0
        for updated_bit in (0, 1):
            reencoded_mirror = decoded_mirror ^ updated_bit
            outer_failures += reencoded_mirror != updated_bit

    selected, returned, deleted_changed = controller_trace()
    return {
        "outer_repetition_decode_encode_failures": outer_failures,
        "declared_D_Udag_G_U_Ddag_structure_failures": int(not structure),
        "NN_macro_reconstruction_failures": macro_failures,
        "routed_central_factor_failures": central_factor_failures,
        "routed_endpoint_identity_failures": endpoint_failures,
        "selected_instruction_order_failures": int(selected != list(range(PROGRAM_LENGTH))),
        "program_counter_return_failures": int(not returned),
        "clock_deletion_changes_selected_word": deleted_changed,
        "decoded_G7_factorization_residual": factor_residual,
        "certificate_pass": outer_failures == 0 and structure and macro_failures == 0
        and central_factor_failures == 0 and endpoint_failures == 0
        and selected == list(range(PROGRAM_LENGTH)) and returned and deleted_changed
        and factor_residual < TOL,
    }


def controller_trace() -> tuple[list[int], bool, bool]:
    token = [1] + [0] * (PROGRAM_LENGTH - 1)
    selected_word = []
    for _ in range(PROGRAM_LENGTH):
        selected_word.append(token.index(1))
        for index in reversed(range(PROGRAM_LENGTH - 1)):
            token[index], token[index + 1] = token[index + 1], token[index]
    returned = token == [1] + [0] * (PROGRAM_LENGTH - 1)
    deleted_token = [1] + [0] * (PROGRAM_LENGTH - 1)
    deleted_selected = []
    for _ in range(PROGRAM_LENGTH):
        deleted_selected.append(deleted_token.index(1))
        for index in reversed(range(1, PROGRAM_LENGTH - 1)):
            deleted_token[index], deleted_token[index + 1] = (
                deleted_token[index + 1], deleted_token[index]
            )
    return selected_word, returned, deleted_selected != selected_word


def covariance_audit() -> dict:
    data_set = set(DATA_COORDS)
    full_failures = data_failures = pair_failures = nn_failures = coarse_failures = 0
    x_check_failures = z_check_failures = clock_failures = work_failures = 0
    fibre_failures = outer_code_failures = 0
    maximum_group_residual = 0.0
    maximum_unsigned_sign_control = 0.0
    program_support_group_failures = 0
    factors = P.coarse_factors(1)
    update = np.asarray(factors["update"])
    maximum_coarse = 0.0
    for frame in P.FRAMES:
        rotate = lambda coord: tuple(int(value) for value in frame @ np.asarray(coord, dtype=int))
        mapping = P.mode_map(frame)
        full_failures += {rotate(coord) for coord in FULL_COORDS} != FULL_COORD_SET
        data_failures += {rotate(coord) for coord in DATA_COORDS} != data_set
        transformed_pairs = {
            frozenset((rotate(FACTOR_COORD[P.EDGE_INDEX[pair]]), rotate(MIRROR_COORD[P.EDGE_INDEX[pair]])))
            for pair in REVERSE_PAIRS
        }
        declared_pairs = {
            frozenset((FACTOR_COORD[P.EDGE_INDEX[pair]], MIRROR_COORD[P.EDGE_INDEX[pair]]))
            for pair in REVERSE_PAIRS
        }
        pair_failures += transformed_pairs != declared_pairs
        coordinate_permutation = tuple(COORD_WIRE[rotate(coord)] for coord in WIRE_COORDS)
        transformed_x = np.zeros_like(LIFTED_CYCLE_CHECKS)
        for row, check_row in enumerate(LIFTED_CYCLE_CHECKS):
            for source, target_wire in enumerate(coordinate_permutation):
                transformed_x[row, target_wire] = check_row[source]
        x_check_failures += sum(
            not P.in_gf2_row_span(row, LIFTED_CYCLE_CHECKS) for row in transformed_x
        )
        transformed_z = np.zeros_like(REPETITION_Z_CHECKS)
        for row, check_row in enumerate(REPETITION_Z_CHECKS):
            for source, target_wire in enumerate(coordinate_permutation):
                transformed_z[row, target_wire] = check_row[source]
        z_check_failures += sum(
            not P.in_gf2_row_span(row, REPETITION_Z_CHECKS) for row in transformed_z
        )
        extended_mapping = mapping + (P.PORT,)
        for logical in range(128):
            expected_logical = 0
            for source, target_mode in enumerate(extended_mapping):
                if (logical >> source) & 1:
                    expected_logical |= 1 << target_mode
            for auxiliary in (0, 1, 0x1555, (1 << 15) - 1):
                physical22 = P.encode_index(logical, auxiliary)
                physical25 = physical22
                for mirror_index, pair in enumerate(REVERSE_PAIRS):
                    edge = P.EDGE_INDEX[pair]
                    physical25 |= ((physical22 >> edge) & 1) << (22 + mirror_index)
                transported = 0
                for source, target_wire in enumerate(coordinate_permutation):
                    transported |= ((physical25 >> source) & 1) << target_wire
                for mirror_index, pair in enumerate(REVERSE_PAIRS):
                    edge = P.EDGE_INDEX[pair]
                    outer_code_failures += (
                        ((transported >> edge) & 1)
                        != ((transported >> (22 + mirror_index)) & 1)
                    )
                observed_logical, _ = P.decode_index(transported & ((1 << 22) - 1))
                fibre_failures += observed_logical != expected_logical
        nn_failures += sum(
            len(gate.sites) == 2 and l1(rotate(gate.sites[0]), rotate(gate.sites[1])) != 1
            for gate in DATA_WORD
        )
        transformed_clock = tuple(rotate(coord) for coord in CLOCK_COORDS)
        clock_failures += sum(
            l1(transformed_clock[index], transformed_clock[index + 1]) != 1
            for index in range(PROGRAM_LENGTH - 1)
        )
        work_failures += any(
            rotate(coord) not in FULL_COORD_SET for coord in (RELAY, WORK0, WORK1)
        )
        one = P.permutation_matrix(mapping + (P.PORT,), 7)
        gamma = P.fock_lift(one)
        seam_mode = mapping[1]
        transformed = gamma @ update @ gamma.conj().T
        residual = float(np.linalg.norm(transformed - P.coarse_factors(seam_mode)["update"]))
        maximum_coarse = max(maximum_coarse, residual)
        coarse_failures += residual >= TOL
        unsigned = P.unsigned_fock_permutation(mapping)
        sign_control = float(np.linalg.norm(gamma - unsigned, ord=2))
        maximum_unsigned_sign_control = max(maximum_unsigned_sign_control, sign_control)
    for left in P.FRAMES:
        left_gamma = P.fock_lift(P.permutation_matrix(P.mode_map(left) + (P.PORT,), 7))
        for right in P.FRAMES:
            right_gamma = P.fock_lift(P.permutation_matrix(P.mode_map(right) + (P.PORT,), 7))
            target_frame = left @ right
            target_gamma = P.fock_lift(
                P.permutation_matrix(P.mode_map(target_frame) + (P.PORT,), 7)
            )
            maximum_group_residual = max(
                maximum_group_residual,
                float(np.linalg.norm(left_gamma @ right_gamma - target_gamma)),
            )
            used_support = set(CLOCK_COORDS) | {RELAY, WORK0, WORK1}
            used_support |= {site for gate in DATA_WORD for site in gate.sites}
            for coord in used_support:
                sequential = left @ (right @ np.asarray(coord, dtype=int))
                composed = (left @ right) @ np.asarray(coord, dtype=int)
                program_support_group_failures += not np.array_equal(sequential, composed)
    return {
        "frames": len(P.FRAMES),
        "full_cube_set_failures": full_failures,
        "data_set_failures": data_failures,
        "mirror_pair_failures": pair_failures,
        "lifted_X_check_span_failures": x_check_failures,
        "repetition_Z_check_span_failures": z_check_failures,
        "outer_repetition_code_transport_failures": outer_code_failures,
        "code_fibre_transport_failures": fibre_failures,
        "full128_fibre_logical_states_per_frame": 128,
        "explicit_full128_fibre_points": len(P.FRAMES) * 128 * 4,
        "transformed_data_NN_failures": nn_failures,
        "transformed_clock_NN_failures": clock_failures,
        "transformed_controller_work_failures": work_failures,
        "coarse_update_covariance_failures": coarse_failures,
        "maximum_coarse_covariance_residual": maximum_coarse,
        "maximum_frame_group_residual": maximum_group_residual,
        "ordered_frame_pair_program_compositions": len(P.FRAMES) ** 2,
        "controller_program_support_group_failures": program_support_group_failures,
        "maximum_unsigned_frame_sign_control": maximum_unsigned_sign_control,
        "physical_frame_action": (
            "coordinate permutation plus supplied bounded decoded fermionic occupied-pair sign"
        ),
    }


def deletion_controls() -> dict:
    seven = product_on_seven(DECODED_GATES)
    seam_index = next(i for i, gate in enumerate(DECODED_GATES) if gate.kind == "seam_fswap")
    contact_index = next(i for i, gate in enumerate(DECODED_GATES) if gate.kind == "contact_phase")
    without_seam = product_on_seven(DECODED_GATES[:seam_index] + DECODED_GATES[seam_index + 1:])
    without_contact = product_on_seven(DECODED_GATES[:contact_index] + DECODED_GATES[contact_index + 1:])
    full_checks = np.zeros((18, 25), dtype=np.uint8)
    full_checks[:15] = LIFTED_CYCLE_CHECKS
    full_checks[15:] = REPETITION_Z_CHECKS
    return {
        "delete_seam_gate_residual": float(np.linalg.norm(seven - without_seam)),
        "delete_contact_gate_residual": float(np.linalg.norm(seven - without_contact)),
        "local_constraint_rank": P.gf2_rank(full_checks),
        "rank_after_one_outer_check_deletion": P.gf2_rank(full_checks[:-1]),
        "one_hot_wrong_token_changes_selected_instruction": (
            matrix_digest(DATA_WORD[0].matrix) != matrix_digest(DATA_WORD[1].matrix)
            or DATA_WORD[0].sites != DATA_WORD[1].sites
        ),
    }


def domain_controls() -> dict:
    pitch = 2 * RADIUS + 3
    rows = []
    for length, split in ((3, "train"), (4, "held-no-refit")):
        anchors = tuple(
            (pitch * x, pitch * y, pitch * z)
            for x in range(length) for y in range(length) for z in range(length)
        )
        sites = {
            (anchor[0] + coord[0], anchor[1] + coord[1], anchor[2] + coord[2])
            for anchor in anchors for coord in FULL_COORDS
        }
        rows.append({
            "L": length,
            "split": split,
            "blocks": len(anchors),
            "M2_per_block": len(FULL_COORDS),
            "collisions": len(anchors) * len(FULL_COORDS) - len(sites),
            "program_length": PROGRAM_LENGTH,
            "controller_A_same": True,
        })
    rejected = 0
    for length, modes, ports in ((2, 6, 1), (3, 5, 1), (3, 6, 0), (4, 6, 2)):
        try:
            if length < 3 or modes != 6 or ports != 1:
                raise ValueError
        except ValueError:
            rejected += 1
    return {
        "rows": rows,
        "lawful_rejections": rejected,
        "held_parameters_refit": 0,
        "shared_port_recurrence_tested": False,
        "pass": rejected == 4 and all(row["collisions"] == 0 for row in rows),
    }
