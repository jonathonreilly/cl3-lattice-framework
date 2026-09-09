#!/usr/bin/env python3
"""Exact finite-law objects for the Cycle-656 two-rail compiler.

This module turns the Cycle-655 3,907-factor bounded intertwiner into explicit
finite blueprints.  ``Q`` is the stationwise ROM-selector layer, ``R`` is the
two-SWAP-layer packet shift, and ``A_AUTO = R Q`` means that Q executes first
and R executes second on every application.  ``E_COMBINED`` fixes the single
live token at station zero, every B packet to vacuum, and every selector flag,
scratch and bypass work factor to zero.

The enormous Hilbert-space matrix is deliberately not formed.  The exported
trace law is an exact compositional semantics for the explicit circuit
blueprints: ROM selection records the selected Cycle-655 factor, while R is
executed as its two literal swap layers.  The companion certificate exhausts
the 3,908-step lawful orbit and separately verifies the local matrix gadgets.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from hashlib import sha256
import math
from typing import Iterable, Iterator, Mapping

import numpy as np

import frontier_full128_cycle_cocycle_intertwiner_2026_07_24 as I


S = I.S
TOL = 4.0e-10
EXPECTED_CYCLE655_WORD_SHA256 = (
    "a2e461d4984e4901fa0e8902c289ed2543da7545370891b96f2b50c6ba7f0fbf"
)


@dataclass(frozen=True)
class Instruction:
    kind: str
    lanes: tuple[int, ...]
    matrix: np.ndarray


@dataclass(frozen=True)
class Primitive:
    kind: str
    sites: tuple[int, ...]
    matrix: np.ndarray


TOUCHED_COORDS = tuple(sorted(I.USED_SUPPORT))
LANE_OF = {coord: lane for lane, coord in enumerate(TOUCHED_COORDS)}
LANES = len(TOUCHED_COORDS)
LIVE_TOKEN = LANES
PACKET_LANES = LANES + 1
ORIGINAL_WORD = tuple(
    Instruction(gate.kind, tuple(LANE_OF[site] for site in gate.sites), gate.matrix)
    for gate in I.COMBINED_WORD
)
PADDING = Instruction("inert_padding_identity", (0,), S.I2)
WORD = ORIGINAL_WORD + (PADDING,)
T = len(WORD)

if I.word_digest(I.COMBINED_WORD) != EXPECTED_CYCLE655_WORD_SHA256:
    raise RuntimeError("Cycle-655 combined-word digest changed")
if len(ORIGINAL_WORD) != 3907 or T != 3908 or LANES != 115:
    raise RuntimeError("Cycle-655 word/support cardinality changed")


def square_track(side: int) -> tuple[tuple[int, int], ...]:
    rows = [(x, 0) for x in range(side)]
    rows += [(side - 1, z) for z in range(1, side)]
    rows += [(x, side - 1) for x in reversed(range(side - 1))]
    rows += [(0, z) for z in reversed(range(1, side - 1))]
    return tuple(rows)


RAIL_SIDE = (2 * T + 4) // 4
RAIL_TRACK = square_track(RAIL_SIDE)
if len(RAIL_TRACK) != 2 * T:
    raise RuntimeError("two-rail perimeter mismatch")


def l1(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def a_base(station: int) -> tuple[int, int]:
    return RAIL_TRACK[2 * station]


def b_base(station: int) -> tuple[int, int]:
    return RAIL_TRACK[2 * station + 1]


def a_coord(station: int, site: int) -> tuple[int, int, int]:
    x, z = a_base(station)
    return (x, site, z)


def b_coord(station: int, lane: int) -> tuple[int, int, int]:
    x, z = b_base(station)
    return (x, lane, z)


MATRIX_KEYS = tuple(sorted({
    (len(gate.lanes), S.matrix_digest(gate.matrix)) for gate in WORD
}))
OPCODE = {key: index for index, key in enumerate(MATRIX_KEYS)}
ADDRESS_BITS = math.ceil(math.log2(T))
OPCODE_BITS = math.ceil(math.log2(len(MATRIX_KEYS)))
LANE_BITS = math.ceil(math.log2(LANES))
PROGRAM_BITS = 1 + ADDRESS_BITS + OPCODE_BITS + 1 + 2 * LANE_BITS


def record(station: int) -> tuple[int, int, int, int, int, int]:
    gate = WORD[station]
    second = gate.lanes[1] if len(gate.lanes) == 2 else gate.lanes[0]
    return (
        1,
        station,
        OPCODE[(len(gate.lanes), S.matrix_digest(gate.matrix))],
        len(gate.lanes) - 1,
        gate.lanes[0],
        second,
    )


PROGRAM = tuple(record(station) for station in range(T))


def record_bits(row: tuple[int, ...]) -> tuple[int, ...]:
    valid, address, opcode, arity, first, second = row
    fields = (
        (valid, 1),
        (address, ADDRESS_BITS),
        (opcode, OPCODE_BITS),
        (arity, 1),
        (first, LANE_BITS),
        (second, LANE_BITS),
    )
    bits = tuple(
        (value >> bit) & 1
        for value, width in fields
        for bit in range(width)
    )
    if len(bits) != PROGRAM_BITS:
        raise RuntimeError("program width mismatch")
    return bits


PROGRAM_WORDS = tuple(record_bits(row) for row in PROGRAM)
PROGRAM_SITES = tuple(range(PACKET_LANES, PACKET_LANES + PROGRAM_BITS))
FLAG = PROGRAM_SITES[-1] + 1
MATCH_CONTROLS = (LIVE_TOKEN,) + PROGRAM_SITES
SCRATCH = tuple(range(FLAG + 1, FLAG + len(MATCH_CONTROLS) - 1))
WORK0 = SCRATCH[-1] + 1
WORK1 = WORK0 + 1
STATION_COLUMN_M2 = WORK1 + 1


def toffoli_word(c1: int, c2: int, target: int) -> tuple[Primitive, ...]:
    return (
        Primitive("H", (target,), S.H),
        Primitive("CNOT", (c2, target), S.CNOT),
        Primitive("Tdg", (target,), S.TDG),
        Primitive("CNOT", (c1, target), S.CNOT),
        Primitive("T", (target,), S.T),
        Primitive("CNOT", (c2, target), S.CNOT),
        Primitive("Tdg", (target,), S.TDG),
        Primitive("CNOT", (c1, target), S.CNOT),
        Primitive("T", (c2,), S.T),
        Primitive("T", (target,), S.T),
        Primitive("H", (target,), S.H),
        Primitive("CNOT", (c1, c2), S.CNOT),
        Primitive("T", (c1,), S.T),
        Primitive("Tdg", (c2,), S.TDG),
        Primitive("CNOT", (c1, c2), S.CNOT),
    )


def fredkin_word(control: int, left: int, right: int) -> tuple[Primitive, ...]:
    return (
        Primitive("CNOT", (right, left), S.CNOT),
        *toffoli_word(control, left, right),
        Primitive("CNOT", (right, left), S.CNOT),
    )


def controlled_one(matrix: np.ndarray) -> np.ndarray:
    result = np.zeros((4, 4), dtype=complex)
    for data in range(2):
        result[2 * data, 2 * data] = 1.0
        for target in range(2):
            result[1 + 2 * target, 1 + 2 * data] = matrix[target, data]
    return result


def match_logical_word() -> tuple[tuple[int, int, int], ...]:
    controls = MATCH_CONTROLS
    rows = [(controls[0], controls[1], SCRATCH[0])]
    previous = SCRATCH[0]
    for control, target in zip(controls[2:-1], SCRATCH[1:]):
        rows.append((previous, control, target))
        previous = target
    rows.append((previous, controls[-1], FLAG))
    if len(rows) != len(MATCH_CONTROLS) - 1:
        raise RuntimeError("match-chain length mismatch")
    return tuple(rows)


MATCH_LOGICAL = match_logical_word()
MATCH_EXPANDED = tuple(
    primitive
    for sites in MATCH_LOGICAL
    for primitive in toffoli_word(*sites)
)


@dataclass(frozen=True)
class MatchResult:
    fired: int
    scratch_after: tuple[int, ...]
    flag_after: int


def execute_match(
    pattern: tuple[int, ...],
    supplied: tuple[int, ...],
    token: int,
    scratch: tuple[int, ...] | None = None,
    flag: int = 0,
) -> MatchResult:
    """Execute the exact logical Toffoli chain, including its inverse."""
    if len(pattern) != PROGRAM_BITS or len(supplied) != PROGRAM_BITS:
        raise ValueError("program width mismatch")
    scratch_initial = (0,) * len(SCRATCH) if scratch is None else scratch
    if len(scratch_initial) != len(SCRATCH):
        raise ValueError("scratch width mismatch")
    values = {LIVE_TOKEN: int(token), FLAG: int(flag)}
    values.update(zip(PROGRAM_SITES, supplied))
    values.update(zip(SCRATCH, scratch_initial))
    negative = tuple(
        PROGRAM_SITES[index]
        for index, bit in enumerate(pattern)
        if bit == 0
    )
    for site in negative:
        values[site] ^= 1
    for c1, c2, target in MATCH_LOGICAL:
        values[target] ^= values[c1] & values[c2]
    fired = values[FLAG]
    for c1, c2, target in reversed(MATCH_LOGICAL):
        values[target] ^= values[c1] & values[c2]
    for site in reversed(negative):
        values[site] ^= 1
    if tuple(values[site] for site in PROGRAM_SITES) != supplied:
        raise RuntimeError("match network changed program memory")
    return MatchResult(
        fired=fired,
        scratch_after=tuple(values[site] for site in SCRATCH),
        flag_after=values[FLAG],
    )


@dataclass(frozen=True)
class RomBlock:
    factor_index: int
    pattern: tuple[int, ...]
    action: Instruction


@dataclass(frozen=True)
class SelectorLaw:
    """Lazy but exact blueprint for Q, the replicated ROM-selector circuit."""

    blocks: tuple[RomBlock, ...]
    lookup: dict[tuple[int, ...], RomBlock] = field(init=False, repr=False)

    def __post_init__(self) -> None:
        table = {block.pattern: block for block in self.blocks}
        if len(table) != len(self.blocks):
            raise ValueError("ROM contains aliased record words")
        object.__setattr__(self, "lookup", table)

    def selected_block(
        self, program: tuple[int, ...], token: int
    ) -> RomBlock | None:
        return self.lookup.get(program) if token == 1 else None

    def without_block(self, factor_index: int) -> "SelectorLaw":
        return SelectorLaw(tuple(
            block for block in self.blocks if block.factor_index != factor_index
        ))

    def iter_block_primitives(self, block: RomBlock) -> Iterator[Primitive]:
        negative = tuple(
            PROGRAM_SITES[index]
            for index, bit in enumerate(block.pattern)
            if bit == 0
        )
        for site in negative:
            yield Primitive("negative_X", (site,), S.X)
        yield from MATCH_EXPANDED
        gate = block.action
        if len(gate.lanes) == 1:
            yield Primitive(
                "controlled_one_M2_opcode",
                (FLAG, gate.lanes[0]),
                controlled_one(gate.matrix),
            )
        else:
            works = (WORK0, WORK1)
            for target, work in zip(gate.lanes, works):
                yield from fredkin_word(FLAG, target, work)
            yield Primitive("vacuum_fixed_two_M2_opcode", works, gate.matrix)
            for target, work in reversed(tuple(zip(gate.lanes, works))):
                yield from fredkin_word(FLAG, target, work)
        for primitive in reversed(MATCH_EXPANDED):
            yield Primitive(
                f"uncompute_{primitive.kind}",
                primitive.sites,
                primitive.matrix.conj().T,
            )
        for site in reversed(negative):
            yield Primitive("negative_X", (site,), S.X)

    def iter_q_primitives(self) -> Iterator[Primitive]:
        for block in self.blocks:
            yield from self.iter_block_primitives(block)


Q = SelectorLaw(tuple(
    RomBlock(index, PROGRAM_WORDS[index], WORD[index])
    for index in range(T)
))


@dataclass(frozen=True)
class StationAncilla:
    scratch: tuple[int, ...] = (0,) * len(SCRATCH)
    flag: int = 0
    bypass: tuple[int, int] = (0, 0)


CLEAN_ANCILLA = StationAncilla()


@dataclass(frozen=True)
class PacketTrace:
    token: int
    payload: str
    origin: int | None
    factors: tuple[int, ...] = ()

    @property
    def is_vacuum(self) -> bool:
        return self.token == 0 and self.payload == "vacuum" and not self.factors

    def apply_factor(self, factor_index: int) -> "PacketTrace":
        return PacketTrace(
            token=self.token,
            payload=self.payload,
            origin=self.origin,
            factors=self.factors + (factor_index,),
        )


VACUUM_PACKET = PacketTrace(0, "vacuum", None)


@dataclass(frozen=True)
class LawState:
    a_packets: tuple[PacketTrace, ...]
    b_packets: tuple[PacketTrace, ...]
    programs: tuple[tuple[int, ...], ...]
    ancillas: tuple[StationAncilla, ...]


@dataclass(frozen=True)
class QReport:
    selected: tuple[tuple[int, int, int | None], ...]
    token_zero_stations: int


def q_apply(selector: SelectorLaw, state: LawState) -> tuple[LawState, QReport]:
    if any(ancilla != CLEAN_ANCILLA for ancilla in state.ancillas):
        raise ValueError("Q lawful semantics requires clean flag/scratch/bypass")
    packets = []
    selected = []
    token_zero = 0
    for station, (packet, program) in enumerate(zip(state.a_packets, state.programs)):
        block = selector.selected_block(program, packet.token)
        if packet.token == 0:
            token_zero += 1
        elif packet.token != 1:
            raise ValueError("token must be a computational-basis bit")
        if block is None:
            packets.append(packet)
            continue
        packets.append(packet.apply_factor(block.factor_index))
        selected.append((station, block.factor_index, packet.origin))
    return (
        LawState(tuple(packets), state.b_packets, state.programs, state.ancillas),
        QReport(tuple(selected), token_zero),
    )


@dataclass(frozen=True)
class RailShiftLaw:
    """R as two explicit packet-lane SWAP layers on the alternating rail."""

    stations: int
    packet_lanes: int
    track: tuple[tuple[int, int], ...]

    def layer1_edges(self) -> Iterator[tuple[tuple[int, int, int], ...]]:
        for station in range(self.stations):
            for lane in range(self.packet_lanes):
                yield (a_coord(station, lane), b_coord(station, lane))

    def layer2_edges(self) -> Iterator[tuple[tuple[int, int, int], ...]]:
        for station in range(self.stations):
            for lane in range(self.packet_lanes):
                yield (
                    b_coord(station, lane),
                    a_coord((station + 1) % self.stations, lane),
                )

    def apply(self, state: LawState) -> LawState:
        a_packets = list(state.a_packets)
        b_packets = list(state.b_packets)
        for station in range(self.stations):
            a_packets[station], b_packets[station] = (
                b_packets[station],
                a_packets[station],
            )
        for station in range(self.stations):
            target = (station + 1) % self.stations
            b_packets[station], a_packets[target] = (
                a_packets[target],
                b_packets[station],
            )
        return LawState(
            tuple(a_packets), tuple(b_packets), state.programs, state.ancillas
        )


R = RailShiftLaw(T, PACKET_LANES, RAIL_TRACK)


@dataclass(frozen=True)
class AutoStepReport:
    live_before: tuple[int, ...]
    live_after: tuple[int, ...]
    selected: tuple[tuple[int, int, int | None], ...]
    token_zero_stations: int
    b_nonvacuum_after: int


@dataclass(frozen=True)
class AutoLaw:
    selector: SelectorLaw
    shift: RailShiftLaw
    chronological_layers: tuple[str, str]

    @property
    def operator_product(self) -> str:
        return "A_auto = R Q" if self.chronological_layers == ("Q", "R") else "A_hostile = Q R"

    def apply(self, state: LawState) -> tuple[LawState, AutoStepReport]:
        live_before = tuple(
            station for station, packet in enumerate(state.a_packets) if packet.token
        )
        if self.chronological_layers == ("Q", "R"):
            selected_state, q_report = q_apply(self.selector, state)
            result = self.shift.apply(selected_state)
        elif self.chronological_layers == ("R", "Q"):
            shifted = self.shift.apply(state)
            result, q_report = q_apply(self.selector, shifted)
        else:
            raise ValueError("unsupported layer order")
        live_after = tuple(
            station for station, packet in enumerate(result.a_packets) if packet.token
        )
        return result, AutoStepReport(
            live_before=live_before,
            live_after=live_after,
            selected=q_report.selected,
            token_zero_stations=q_report.token_zero_stations,
            b_nonvacuum_after=sum(not packet.is_vacuum for packet in result.b_packets),
        )


A_AUTO = AutoLaw(Q, R, ("Q", "R"))
HOSTILE_R_THEN_Q = AutoLaw(Q, R, ("R", "Q"))


@dataclass(frozen=True)
class CombinedEmbedding:
    """E_combined genesis appended to the Cycle-655 E_full payload."""

    token_station: int
    program_words: tuple[tuple[int, ...], ...]
    clean_ancilla: StationAncilla

    def encode(self, payload: str = "E_full|psi>") -> LawState:
        a_packets = [VACUUM_PACKET for _ in range(T)]
        a_packets[self.token_station] = PacketTrace(
            1, payload, self.token_station
        )
        return LawState(
            tuple(a_packets),
            tuple(VACUUM_PACKET for _ in range(T)),
            self.program_words,
            tuple(self.clean_ancilla for _ in range(T)),
        )

    def hostile_state(
        self,
        token_positions: Iterable[int],
        payload_positions: Iterable[int] = (),
        program_overrides: Mapping[int, tuple[int, ...]] | None = None,
        ancilla_overrides: Mapping[int, StationAncilla] | None = None,
    ) -> LawState:
        token_set = set(token_positions)
        payload_set = set(payload_positions) | token_set
        a_packets = []
        for station in range(T):
            token = int(station in token_set)
            payload = f"payload@{station}" if station in payload_set else "vacuum"
            origin = station if station in payload_set else None
            a_packets.append(PacketTrace(token, payload, origin))
        programs = list(self.program_words)
        for station, word in (program_overrides or {}).items():
            programs[station] = word
        ancillas = [self.clean_ancilla for _ in range(T)]
        for station, ancilla in (ancilla_overrides or {}).items():
            ancillas[station] = ancilla
        return LawState(
            tuple(a_packets),
            tuple(VACUUM_PACKET for _ in range(T)),
            tuple(programs),
            tuple(ancillas),
        )

    def exact_genesis_failures(self, state: LawState) -> dict[str, int]:
        return {
            "token_count": abs(sum(packet.token for packet in state.a_packets) - 1),
            "token_station": int(not state.a_packets[self.token_station].token),
            "nonvacuum_b": sum(not packet.is_vacuum for packet in state.b_packets),
            "program": sum(left != right for left, right in zip(state.programs, self.program_words)),
            "ancilla": sum(ancilla != self.clean_ancilla for ancilla in state.ancillas),
            "extra_a_payload": sum(
                packet.payload != "vacuum"
                for station, packet in enumerate(state.a_packets)
                if station != self.token_station
            ),
        }


E_COMBINED = CombinedEmbedding(0, PROGRAM_WORDS, CLEAN_ANCILLA)


@dataclass(frozen=True)
class OrbitCertificate:
    steps: int
    trace_sha256: str
    live_count_failures: int
    b_vacuum_failures: int
    program_change_failures: int
    ancilla_change_failures: int
    selected_events: int
    token_zero_station_visits: int
    first_events: tuple[tuple[int, int, int | None], ...]
    last_events: tuple[tuple[int, int, int | None], ...]


def run_orbit(
    law: AutoLaw,
    initial: LawState,
    steps: int = T,
) -> tuple[LawState, OrbitCertificate]:
    state = initial
    initial_programs = initial.programs
    initial_ancillas = initial.ancillas
    initial_live_count = sum(packet.token for packet in initial.a_packets)
    hasher = sha256()
    live_failures = b_failures = program_failures = ancilla_failures = 0
    selected_events = token_zero_visits = 0
    first_events: tuple[tuple[int, int, int | None], ...] = ()
    last_events: tuple[tuple[int, int, int | None], ...] = ()
    for step in range(steps):
        state, report = law.apply(state)
        if step == 0:
            first_events = report.selected
        last_events = report.selected
        live_failures += len(report.live_after) != initial_live_count
        b_failures += report.b_nonvacuum_after != 0
        program_failures += state.programs != initial_programs
        ancilla_failures += state.ancillas != initial_ancillas
        selected_events += len(report.selected)
        token_zero_visits += report.token_zero_stations
        hasher.update(repr((
            step,
            report.live_before,
            report.selected,
            report.live_after,
            report.b_nonvacuum_after,
        )).encode())
    return state, OrbitCertificate(
        steps=steps,
        trace_sha256=hasher.hexdigest(),
        live_count_failures=live_failures,
        b_vacuum_failures=b_failures,
        program_change_failures=program_failures,
        ancilla_change_failures=ancilla_failures,
        selected_events=selected_events,
        token_zero_station_visits=token_zero_visits,
        first_events=first_events,
        last_events=last_events,
    )


def sequence_digest(indices: Iterable[int]) -> str:
    hasher = sha256()
    for index in indices:
        gate = WORD[index]
        hasher.update(str(index).encode())
        hasher.update(gate.kind.encode())
        hasher.update(repr(gate.lanes).encode())
        hasher.update(S.matrix_digest(gate.matrix).encode())
    return hasher.hexdigest()


PADDED_SEQUENCE_SHA256 = sequence_digest(range(T))


def routed_primitive(primitive: Primitive) -> tuple[Primitive, ...]:
    """Expand one ordered logical primitive into an explicit NN subword.

    For a two-site primitive, the first listed operand is transported along
    the station column until it is adjacent to the second listed operand.  The
    original ordered matrix is then applied on that ordered adjacent pair and
    the transport SWAPs are undone in exact reverse order.  This definition
    handles ascending and descending columns without changing operand order.
    """
    if len(primitive.sites) == 1:
        return (primitive,)
    if len(primitive.sites) != 2:
        raise ValueError("primitive arity must be one or two")
    first, second = primitive.sites
    if first == second:
        raise ValueError("colliding two-M2 primitive")
    step = 1 if second > first else -1
    path = tuple(range(first, second + step, step))
    swaps = tuple(
        Primitive("route_swap", (path[index], path[index + 1]), S.SWAP)
        for index in range(len(path) - 2)
    )
    central = Primitive(
        primitive.kind,
        (path[-2], path[-1]),
        primitive.matrix,
    )
    return swaps + (central,) + tuple(reversed(swaps))


def routed_primitive_certificate(primitive: Primitive) -> dict[str, int | str]:
    """Audit an explicit routed subword, including ordered wire semantics."""
    word = routed_primitive(primitive)
    hasher = sha256()
    non_nn = outside = route_kind_failures = 0
    for gate in word:
        hasher.update(gate.kind.encode())
        hasher.update(repr(gate.sites).encode())
        hasher.update(S.matrix_digest(gate.matrix).encode())
        outside += any(site < 0 or site >= STATION_COLUMN_M2 for site in gate.sites)
        non_nn += len(gate.sites) == 2 and abs(gate.sites[0] - gate.sites[1]) != 1

    expected_length = 1 if len(primitive.sites) == 1 else 2 * abs(
        primitive.sites[0] - primitive.sites[1]
    ) - 1
    length_failures = int(len(word) != expected_length)
    central_kind_failures = central_matrix_failures = 0
    operand_order_failures = return_failures = 0

    if len(primitive.sites) == 1:
        central = word[0]
        central_kind_failures += central.kind != primitive.kind
        central_matrix_failures += (
            S.matrix_digest(central.matrix) != S.matrix_digest(primitive.matrix)
        )
        operand_order_failures += central.sites != primitive.sites
    else:
        labels = list(range(STATION_COLUMN_M2))
        center = len(word) // 2
        for gate in word[:center]:
            route_kind_failures += gate.kind != "route_swap"
            left, right = gate.sites
            labels[left], labels[right] = labels[right], labels[left]
        central = word[center]
        central_kind_failures += central.kind != primitive.kind
        central_matrix_failures += (
            S.matrix_digest(central.matrix) != S.matrix_digest(primitive.matrix)
        )
        operand_order_failures += (
            tuple(labels[site] for site in central.sites) != primitive.sites
        )
        for gate in word[center + 1:]:
            route_kind_failures += gate.kind != "route_swap"
            left, right = gate.sites
            labels[left], labels[right] = labels[right], labels[left]
        return_failures += labels != list(range(STATION_COLUMN_M2))

    return {
        "routed_factors": len(word),
        "length_failures": length_failures,
        "non_NN_factors": non_nn,
        "outside_station_factors": outside,
        "route_kind_failures": route_kind_failures,
        "central_kind_failures": central_kind_failures,
        "central_matrix_failures": central_matrix_failures,
        "operand_order_failures": operand_order_failures,
        "wire_return_failures": return_failures,
        "routed_subword_sha256": hasher.hexdigest(),
    }


def routed_count(gate: Primitive) -> int:
    if len(gate.sites) == 1:
        return 1
    distance = abs(gate.sites[0] - gate.sites[1])
    if distance == 0:
        raise ValueError("colliding two-M2 primitive")
    return 2 * distance - 1


def selector_resources() -> dict[str, int | str]:
    logical = one = two = routed = maximum_distance = 0
    ascending = descending = adjacent = 0
    signature_certificates: dict[tuple[str, tuple[int, ...], str], dict] = {}
    failure_fields = (
        "length_failures",
        "non_NN_factors",
        "outside_station_factors",
        "route_kind_failures",
        "central_kind_failures",
        "central_matrix_failures",
        "operand_order_failures",
        "wire_return_failures",
    )
    weighted_failures = {field: 0 for field in failure_fields}
    hasher = sha256()
    for primitive in Q.iter_q_primitives():
        logical += 1
        one += len(primitive.sites) == 1
        two += len(primitive.sites) == 2
        matrix_digest = S.matrix_digest(primitive.matrix)
        signature = (primitive.kind, primitive.sites, matrix_digest)
        certificate = signature_certificates.get(signature)
        if certificate is None:
            certificate = routed_primitive_certificate(primitive)
            signature_certificates[signature] = certificate
        routed += int(certificate["routed_factors"])
        hasher.update(bytes.fromhex(str(certificate["routed_subword_sha256"])))
        for field in failure_fields:
            weighted_failures[field] += int(certificate[field])
        if len(primitive.sites) == 2:
            first, second = primitive.sites
            ascending += first < second
            descending += first > second
            adjacent += abs(first - second) == 1
            maximum_distance = max(
                maximum_distance, abs(first - second)
            )
    per_auto = routed * T + 2 * T * PACKET_LANES
    result: dict[str, int | str] = {
        "ROM_blocks_per_station": len(Q.blocks),
        "logical_Q_factors_per_station": logical,
        "logical_one_M2_factors_per_station": one,
        "logical_two_M2_factors_per_station": two,
        "ascending_two_M2_factors_per_station": ascending,
        "descending_two_M2_factors_per_station": descending,
        "adjacent_two_M2_factors_per_station": adjacent,
        "unique_Q_primitive_signatures": len(signature_certificates),
        "routed_Q_factor_occurrences_checked": logical,
        "routed_Q_NN_factors_per_station": routed,
        "Q_NN_instances_all_stations": routed * T,
        "R_NN_instances_per_A_auto": 2 * T * PACKET_LANES,
        "A_auto_NN_instances": per_auto,
        "A_auto_power_3908_executed_NN_instances": per_auto * T,
        "maximum_route_distance": maximum_distance,
        "Q_schedule_sha256": hasher.hexdigest(),
        "Q_schedule_digest_definition": (
            "sha256 of the ordered sequence of exact routed-subword sha256 bytes"
        ),
    }
    result.update({f"routed_{field}": value for field, value in weighted_failures.items()})
    return result


def rail_geometry_certificate() -> dict[str, int]:
    def inspect(edges: Iterable[tuple[tuple[int, int, int], ...]]) -> dict[str, int]:
        observed_edges = set()
        vertices = set()
        repeats = collisions = non_nn = count = 0
        for edge in edges:
            count += 1
            ordered = tuple(sorted(edge))
            repeats += ordered in observed_edges
            observed_edges.add(ordered)
            collisions += sum(site in vertices for site in edge)
            vertices.update(edge)
            non_nn += l1(*edge) != 1
        return {
            "edges": count,
            "repeats": repeats,
            "vertex_collisions": collisions,
            "non_NN": non_nn,
            "vertices": len(vertices),
        }

    layer1 = inspect(R.layer1_edges())
    layer2 = inspect(R.layer2_edges())
    return {
        "layer1_edges": layer1["edges"],
        "layer2_edges": layer2["edges"],
        "layer1_repeats": layer1["repeats"],
        "layer2_repeats": layer2["repeats"],
        "layer1_vertex_collisions": layer1["vertex_collisions"],
        "layer2_vertex_collisions": layer2["vertex_collisions"],
        "layer1_non_NN": layer1["non_NN"],
        "layer2_non_NN": layer2["non_NN"],
        "layer1_vertices": layer1["vertices"],
        "layer2_vertices": layer2["vertices"],
    }


def route_geometry_certificate() -> dict[str, int]:
    failures = non_nn = outside = edges_checked = 0
    orientation_cases = 0
    for distance in range(1, STATION_COLUMN_M2):
        for sites in ((0, distance), (distance, 0)):
            orientation_cases += 1
            certificate = routed_primitive_certificate(
                Primitive("orientation_probe", sites, S.CNOT)
            )
            edges_checked += int(certificate["routed_factors"])
            non_nn += int(certificate["non_NN_factors"])
            outside += int(certificate["outside_station_factors"])
            failures += sum(int(certificate[field]) for field in (
                "length_failures",
                "route_kind_failures",
                "central_kind_failures",
                "central_matrix_failures",
                "operand_order_failures",
                "wire_return_failures",
            ))
    return {
        "distances_checked": STATION_COLUMN_M2 - 1,
        "ordered_orientation_cases": orientation_cases,
        "endpoint_or_return_failures": failures,
        "NN_edges_checked": edges_checked,
        "non_NN_edges": non_nn,
        "outside_station_edges": outside,
    }


def flipped_program_word(station: int) -> tuple[int, ...]:
    row = list(PROGRAM[station])
    row[2] = (row[2] + 1) % len(MATRIX_KEYS)
    return record_bits(tuple(row))
