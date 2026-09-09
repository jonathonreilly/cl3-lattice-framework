#!/usr/bin/env python3
"""Conditional local-Gauss endpoint bridge into the landed Cycle-612 code.

This runner does not call an update ordinal, packet count, rotor value, or
schedule position time.  It computes a coherent candidate endpoint predicate
from changes of local matter occupation/B eigenvalues across the exact
Cycle-703 dressed FSWAP.  Supplied occurrence/admission/domain values gate a
finite reversible software predecessor/interval model.  Projection of that
model intertwines the unchanged Cycle-610 EventChain, and its identities feed
the unchanged Cycle-612 JointOrder harness.

The predicate is an opportunity, not occurrence.  The software packet model
is not a physical-M2 bank and is not a permanent Record.  Its integer interval
has no empirical unit.  The local-Gauss operators are BKSF graph-edge qubits;
their Cycle-232 Z3 physical-site placement/repetition lift is not composed in
this runner.  BKSF state preparation/common E remains open here.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from hashlib import sha256
from itertools import product
import importlib.util
import json
import math
from pathlib import Path
import resource
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle703_local_gauss_reference_adversary_2026_07_25 as GAUSS


START = time.perf_counter()
PASS = 0
FAIL = 0

C610_SHA256 = "36fcb1655bbdcd758b69ea1e273821e5c820f738eb63199570c8f36c7e294bac"
C612_SHA256 = "6365d5aed1e70fb9b427ee6fb987879027cc30c818856a992b3fbf9d057e0c1b"
GAUSS_SHA256 = "781823cf744be93de73f5e86e4e4cc988e0e7fe19c9c88a264b6f58169c07b0e"
BKSF_STATE_PREPARATION_EXECUTED = False


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label} :: {detail}")


def load_landed(name: str):
    path = ROOT / "scripts" / f"{name}.py"
    digest = sha256(path.read_bytes()).hexdigest()
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module, digest


C612, C612_SHA = load_landed(
    "physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22"
)
C610 = C612.C610
C610_SHA = sha256(Path(C610.__file__).read_bytes()).hexdigest()
GAUSS_SHA = sha256(Path(GAUSS.__file__).read_bytes()).hexdigest()


# ---------------------------------------------------------------------------
# Local BKSF edge-qubit endpoint predicate.
# ---------------------------------------------------------------------------

def b_eigenvalue(occupation: int) -> int:
    """B=(-1)^n on an occupation eigenstate."""

    return 1 - 2 * occupation


def matter_delta_mask(before: tuple[int, ...], after: tuple[int, ...]) -> int:
    return sum((left ^ right) << index for index, (left, right) in enumerate(
        zip(before, after)
    ))


def endpoint_from_b_change(
    before: tuple[int, ...], after: tuple[int, ...]
) -> int:
    return int(any(
        b_eigenvalue(left) != b_eigenvalue(right)
        for left, right in zip(before, after)
    ))


def endpoint_pointer_gate(
    state: tuple[int, int, int, int, int, int, int], inverse: bool = False
) -> tuple[int, int, int, int, int, int, int]:
    """Seven-M2 reversible comparator permutation.

    Registers are (n_u^-, n_v^-, n_u^+, n_v^+, d_u, d_v, p).  On the blank
    pointer domain d_u=d_v=p=0 it leaves the four occupations unchanged and
    writes both B/occupation deltas and their OR.  The inverse applies the
    same XOR/Toffoli grammar in reverse.  On superpositions this is a coherent
    entangling opportunity pointer, not an occurrence selector.
    """

    nu0, nv0, nu1, nv1, du, dv, pointer = state
    if inverse:
        pointer ^= du | dv
        dv ^= nv0 ^ nv1
        du ^= nu0 ^ nu1
    else:
        du ^= nu0 ^ nu1
        dv ^= nv0 ^ nv1
        pointer ^= du | dv
    return nu0, nv0, nu1, nv1, du, dv, pointer


def endpoint_controls() -> dict[str, object]:
    inverse_failures = 0
    for raw in range(1 << 7):
        state = tuple((raw >> index) & 1 for index in range(7))
        inverse_failures += endpoint_pointer_gate(
            endpoint_pointer_gate(state), inverse=True
        ) != state

    predicate_failures = b_failures = delta_count_failures = 0
    reference_failures = contact_false_positives = 0
    endpoint_true = endpoint_false = 0
    logical_rows = tuple(product((0, 1), repeat=12))
    for left_mode in range(6):
        for right_mode in range(6):
            right = 6 + right_mode
            for logical in logical_rows:
                extended = GAUSS.extended_codeword(logical)
                target, _target_phase = GAUSS.target_fswap_action(
                    logical, left_mode, right
                )
                observed, _observed_phase = GAUSS.corrected_fswap_action(
                    extended, left_mode, right_mode
                )
                target_extended = GAUSS.extended_codeword(target)
                expected = logical[left_mode] ^ logical[right]
                predicate = endpoint_from_b_change(logical, target)
                pointer_state = endpoint_pointer_gate((
                    logical[left_mode], logical[right],
                    target[left_mode], target[right], 0, 0, 0,
                ))
                predicate_failures += predicate != expected
                b_failures += pointer_state[-1] != predicate
                delta_count_failures += (
                    matter_delta_mask(logical, target).bit_count()
                    != 2 * expected
                )
                reference_failures += (
                    observed != target_extended
                    or GAUSS.d_bits(observed) != (0, 0)
                    or sum(
                        extended[index] != observed[index] for index in (6, 13)
                    ) != 2 * expected
                )
                endpoint_true += predicate
                endpoint_false += 1 - predicate

            # Diagonal contact changes phase only, never local occupation/B.
            for logical in logical_rows:
                contact_false_positives += endpoint_from_b_change(
                    logical, logical
                )

    # Physical B words are products of incident edge-M2 Zs.  Extract the
    # maximum bounded support on every open-L2 spatial matter bond.
    graph = GAUSS.base.ReferenceGraph(2, False)
    b_weights = []
    b_union_weights = []
    b_owner_cells = []
    for (cell, axis, operand), _edge in graph.cross_edge.items():
        if operand != 0:
            continue
        target = list(cell)
        target[axis] += 1
        target = tuple(target)
        u = graph.vertex_index[(cell, 2 * axis + 1)]
        v = graph.vertex_index[(target, 2 * axis)]
        bu = graph.B(u)
        bv = graph.B(v)
        b_weights.extend(((bu.x | bu.z).bit_count(), (bv.x | bv.z).bit_count()))
        union = (bu.x | bu.z | bv.x | bv.z)
        b_union_weights.append(union.bit_count())
        owners = {
            graph.edges[index][3]
            for index in range(len(graph.edges)) if (union >> index) & 1
        }
        b_owner_cells.append(len(owners))

    # Proper-cubic frames only permute the six local ports.  The predicate
    # truth table is independent of the chosen port pair, so transport closes
    # without an exterior ordering table.
    frames = GAUSS.base.c210.proper_cubic_frames()
    frame_port_failures = 0
    for frame in frames:
        permutation = GAUSS.base.c210.direction_permutation(frame)
        frame_port_failures += (
            any(
                sum(abs(complex(permutation[target, source])) > 0.5
                    for target in range(6)) != 1
                for source in range(6)
            )
            or any(
                sum(abs(complex(permutation[target, source])) > 0.5
                    for source in range(6)) != 1
                for target in range(6)
            )
        )

    return {
        "pointer_truth_table_rows": 1 << 7,
        "pointer_inverse_failures": inverse_failures,
        "common_E_columns": 1 << 12,
        "directed_port_pairs": 36,
        "seam_predicate_failures": predicate_failures,
        "B_pointer_failures": b_failures,
        "matter_delta_count_failures": delta_count_failures,
        "local_D_or_reference_failures": reference_failures,
        "contact_false_positives": contact_false_positives,
        "endpoint_true_cases": endpoint_true,
        "endpoint_false_cases": endpoint_false,
        "edge_qubit_B_words": len(b_weights),
        "maximum_single_B_edge_qubit_weight": max(b_weights),
        "maximum_two_endpoint_B_edge_qubit_union": max(b_union_weights),
        "maximum_B_support_owner_cells": max(b_owner_cells),
        "proper_cubic_frames": len(frames),
        "frame_port_failures": frame_port_failures,
        "runtime_exterior_order_table_used": False,
        "schedule_ordinal_read": False,
    }


# ---------------------------------------------------------------------------
# Finite reversible predecessor/interval software model.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class IntervalPacket:
    identity: int
    predecessor: int | None
    rotor_before: int
    rotor: int
    carry: int
    delta_mask: int
    endpoint: int
    binder: int
    valid: int
    orientation: int
    actuality: int
    admissibility: int
    law_domain: int


@dataclass
class ReversiblePacketBank:
    bank: int
    head: int | None = None
    rotor: int = 14
    cells: dict[int, IntervalPacket] = field(default_factory=dict)
    exhausted: bool = False

    def append(
        self,
        address: int,
        delta_mask: int,
        endpoint: int,
        orientation: int,
        binder: int,
        actuality: int,
        admissibility: int,
        law_domain: int,
    ) -> str:
        opportunity = endpoint & binder
        if not opportunity:
            return "no_opportunity"
        if address in self.cells:
            return "refused_fresh"
        if not (actuality & admissibility & law_domain):
            return "refused_supplied"
        if len(self.cells) >= self.bank or not (0 <= address < self.bank):
            self.exhausted = True
            return "exhausted"
        rotor_before = self.rotor
        rotor = (rotor_before + 1) % 16
        packet = IntervalPacket(
            identity=address,
            predecessor=self.head,
            rotor_before=rotor_before,
            rotor=rotor,
            carry=int(rotor == 0),
            delta_mask=delta_mask,
            endpoint=endpoint,
            binder=binder,
            valid=1,
            orientation=orientation,
            actuality=actuality,
            admissibility=admissibility,
            law_domain=law_domain,
        )
        self.cells[address] = packet
        self.head = address
        self.rotor = rotor
        return "admitted"

    def unappend(self, address: int) -> str:
        """Exact inverse on the declared last-packet domain."""

        if address != self.head or address not in self.cells:
            return "refused_not_head"
        packet = self.cells.pop(address)
        self.head = packet.predecessor
        self.rotor = packet.rotor_before
        self.exhausted = False
        return "unappended"

    def refill(self, extra: int) -> None:
        self.bank += extra
        self.exhausted = False

    def ordered(self) -> list[IntervalPacket] | None:
        if self.head is None:
            return []
        reverse = []
        seen = set()
        cursor = self.head
        while cursor is not None:
            if cursor in seen or cursor not in self.cells:
                return None
            seen.add(cursor)
            packet = self.cells[cursor]
            reverse.append(packet)
            cursor = packet.predecessor
        if len(seen) != len(self.cells):
            return None
        return list(reversed(reverse))

    def interval(self, start_identity: int, end_identity: int) -> int | None:
        cells = self.ordered()
        if cells is None:
            return None
        identities = [cell.identity for cell in cells]
        if start_identity not in identities or end_identity not in identities:
            return None
        start = identities.index(start_identity)
        end = identities.index(end_identity)
        if start > end:
            reverse = self.interval(end_identity, start_identity)
            return None if reverse is None else -reverse
        span = cells[start + 1:end + 1]
        expected = cells[start].identity
        for cell in span:
            if cell.predecessor != expected or not cell.valid or not cell.binder:
                return None
            expected = cell.identity
        carries = sum(cell.carry for cell in span)
        rotor_delta = cells[end].rotor - cells[start].rotor
        return 16 * carries + rotor_delta

    def project_cycle610(self):
        chain = C610.EventChain(bank=self.bank)
        ordered = self.ordered()
        if ordered is None:
            return None
        chain.cells = [
            C610.EventCell(
                identity=cell.identity,
                rotor=cell.rotor,
                carry=cell.carry,
                predecessor=cell.predecessor,
                binder=cell.binder,
                valid=cell.valid,
                orientation=cell.orientation,
            )
            for cell in ordered
        ]
        chain.admitted_ticks = {cell.identity for cell in ordered}
        chain.exhausted = self.exhausted
        return chain


def bank_state(bank: ReversiblePacketBank) -> str:
    payload = {
        "bank": bank.bank,
        "head": bank.head,
        "rotor": bank.rotor,
        "exhausted": bank.exhausted,
        "cells": {key: asdict(value) for key, value in sorted(bank.cells.items())},
    }
    return sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()


def edge_qubit_endpoint_case(changed: bool = True):
    logical = [0] * 12
    if changed:
        logical[0] = 1
    else:
        logical[0] = logical[6] = 1
    logical = tuple(logical)
    target, _phase = GAUSS.target_fswap_action(logical, 0, 6)
    return {
        "before": logical,
        "after": target,
        "delta_mask": matter_delta_mask(logical, target),
        "endpoint": endpoint_from_b_change(logical, target),
    }


def packet_interface_controls() -> dict[str, object]:
    changed = edge_qubit_endpoint_case(True)
    unchanged = edge_qubit_endpoint_case(False)
    packet = ReversiblePacketBank(bank=C610.BANK_SIZE)
    chain = C610.EventChain(bank=C610.BANK_SIZE)
    statuses_match = 0
    projection_failures = interval_failures = 0
    statuses = []
    for address in range(C610.BANK_SIZE + 1):
        orientation = 1  # supplied local directed-port orientation
        left = packet.append(
            address, changed["delta_mask"], changed["endpoint"], orientation,
            binder=1, actuality=1, admissibility=1, law_domain=1,
        )
        right = chain.admit(
            tick_id=address, orientation=orientation,
            certificate=changed["endpoint"], binder=1,
            actuality=1, admissibility=1, law_domain=1,
        )
        statuses.append(left)
        statuses_match += left == right
        projected = packet.project_cycle610()
        if projected is None:
            projection_failures += 1
        else:
            projection_failures += [asdict(row) for row in projected.cells] != [
                asdict(row) for row in chain.cells
            ]

    packet.refill(C610.BANK_REFILL)
    chain.refill(C610.BANK_REFILL)
    refill_left = packet.append(
        C610.BANK_SIZE, changed["delta_mask"], changed["endpoint"], -1,
        binder=1, actuality=1, admissibility=1, law_domain=1,
    )
    refill_right = chain.admit(
        tick_id=C610.BANK_SIZE, orientation=-1,
        certificate=changed["endpoint"], binder=1,
        actuality=1, admissibility=1, law_domain=1,
    )
    no_endpoint_left = packet.append(
        C610.BANK_SIZE + 1, unchanged["delta_mask"], unchanged["endpoint"], 1,
        binder=1, actuality=1, admissibility=1, law_domain=1,
    )
    no_endpoint_right = chain.admit(
        tick_id=C610.BANK_SIZE + 1, orientation=1,
        certificate=unchanged["endpoint"], binder=1,
        actuality=1, admissibility=1, law_domain=1,
    )
    duplicate_left = packet.append(
        2, changed["delta_mask"], changed["endpoint"], 1,
        binder=1, actuality=1, admissibility=1, law_domain=1,
    )
    duplicate_right = chain.admit(
        tick_id=2, orientation=1, certificate=changed["endpoint"], binder=1,
        actuality=1, admissibility=1, law_domain=1,
    )
    no_actuality_left = packet.append(
        C610.BANK_SIZE + 1, changed["delta_mask"], changed["endpoint"], 1,
        binder=1, actuality=0, admissibility=1, law_domain=1,
    )
    no_actuality_right = chain.admit(
        tick_id=C610.BANK_SIZE + 1, orientation=1,
        certificate=changed["endpoint"], binder=1,
        actuality=0, admissibility=1, law_domain=1,
    )

    projected = packet.project_cycle610()
    projection_failures += projected is None
    if projected is not None:
        projection_failures += [asdict(row) for row in projected.cells] != [
            asdict(row) for row in chain.cells
        ]
        a_id, b_id, c_id = 2, 11, 23
        for start, end in (
            (a_id, b_id), (b_id, c_id), (a_id, c_id), (b_id, a_id)
        ):
            interval_failures += packet.interval(start, end) != chain.interval(
                start, end
            )
        d_ab = packet.interval(a_id, b_id)
        d_bc = packet.interval(b_id, c_id)
        d_ac = packet.interval(a_id, c_id)
    else:
        d_ab = d_bc = d_ac = None

    # Exact append/unappend replay on a separate declared bank.
    reversible = ReversiblePacketBank(bank=8)
    initial = bank_state(reversible)
    for address in range(6):
        reversible.append(
            address, changed["delta_mask"], changed["endpoint"],
            1,
            binder=1, actuality=1, admissibility=1, law_domain=1,
        )
    forward = bank_state(reversible)
    inverse_statuses = [reversible.unappend(address) for address in reversed(range(6))]
    returned = bank_state(reversible)
    for address in range(6):
        reversible.append(
            address, changed["delta_mask"], changed["endpoint"],
            1,
            binder=1, actuality=1, admissibility=1, law_domain=1,
        )
    replay = bank_state(reversible)

    register_inverse_cases = register_inverse_failures = carry_failures = 0
    for rotor_before in range(16):
        for orientation in (-1, 1):
            for delta_mask in (1, 3, (1 << 12) - 1):
                probe = ReversiblePacketBank(bank=1, rotor=rotor_before)
                before = bank_state(probe)
                status = probe.append(
                    0, delta_mask, 1, orientation,
                    binder=1, actuality=1, admissibility=1, law_domain=1,
                )
                register_inverse_cases += 1
                carry_failures += (
                    status != "admitted"
                    or probe.cells[0].carry != int(rotor_before == 15)
                )
                inverse = probe.unappend(0)
                register_inverse_failures += (
                    inverse != "unappended" or bank_state(probe) != before
                )

    address_bits = math.ceil(math.log2(C610.BANK_SIZE + C610.BANK_REFILL + 1))
    # predecessor, rotor-before, rotor-after, carry, 12-bit matter delta,
    # endpoint, binder, valid, orientation, and three supplied admission bits.
    packet_payload_bits = (
        address_bits + 4 + 4 + 1 + 12 + 1 + 1 + 1 + 1 + 3
    )
    return {
        "Cycle610_append_attempts_compared": C610.BANK_SIZE + 1,
        "matching_statuses": statuses_match,
        "bank_admitted": statuses.count("admitted"),
        "bank_exhausted_seen": "exhausted" in statuses,
        "refill_statuses": (refill_left, refill_right),
        "no_endpoint_statuses": (no_endpoint_left, no_endpoint_right),
        "duplicate_statuses": (duplicate_left, duplicate_right),
        "no_actuality_statuses": (no_actuality_left, no_actuality_right),
        "projection_failures": projection_failures,
        "interval_failures": interval_failures,
        "d_ab": d_ab,
        "d_bc": d_bc,
        "d_ac": d_ac,
        "additivity_closed": d_ab is not None and d_bc is not None
            and d_ac == d_ab + d_bc,
        "reversal_closed": d_ab is not None
            and packet.interval(11, 2) == -d_ab,
        "inverse_statuses": tuple(inverse_statuses),
        "inverse_returned_initial_state": returned == initial,
        "forward_replay_exact": replay == forward,
        "register_inverse_cases": register_inverse_cases,
        "register_inverse_failures": register_inverse_failures,
        "carry_truth_failures": carry_failures,
        "candidate_packet_payload_bits_per_bank_cell": packet_payload_bits,
        "candidate_head_bits": address_bits,
        "bank_cells": C610.BANK_SIZE,
        "software_blank_address_selector_supplied": True,
        "actuality_admissibility_domain_supplied": True,
        "empirical_unit_supplied": False,
        "schedule_ordinal_stored": False,
        "software_packet_inverse_accessible": True,
    }


# ---------------------------------------------------------------------------
# Unchanged Cycle-612 JointOrder harness, gated by physical opportunities.
# ---------------------------------------------------------------------------

def joint_order_controls() -> dict[str, object]:
    changed = edge_qubit_endpoint_case(True)
    opportunity_a = changed["endpoint"]
    opportunity_b = changed["endpoint"]

    joint = C612.JointOrder()
    for i in range(3):
        if opportunity_a:
            joint.admit_local("A", 100 + i)
    for i in range(2):
        if opportunity_b:
            joint.admit_local("B", 200 + i)
    s1 = joint.admit_shared(900) if opportunity_a & opportunity_b else "no_opportunity"
    if opportunity_a:
        joint.admit_local("A", 103)
    if opportunity_b:
        joint.admit_local("B", 202)
    s2 = joint.admit_shared(901) if opportunity_a & opportunity_b else "no_opportunity"
    consistent_acyclic = joint.acyclic()

    adversary = C612.JointOrder()
    for i in range(4):
        adversary.admit_local("A", 300 + i)
    for i in range(4):
        adversary.admit_local("B", 400 + i)
    first = adversary.admit_shared(910)
    adversary.force_shared(911, 1, 6)
    refusal = adversary.admit_shared(912)

    forced = C612.JointOrder()
    for i in range(3):
        forced.admit_local("A", 500 + i)
        forced.admit_local("B", 600 + i)
    forced.force_shared(920, 0, 2)
    forced.force_shared(921, 2, 0)

    unchanged = edge_qubit_endpoint_case(False)
    gated = C612.JointOrder()
    no_endpoint_status = (
        gated.admit_shared(930) if unchanged["endpoint"] else "no_opportunity"
    )
    return {
        "edge_qubit_opportunities": (opportunity_a, opportunity_b),
        "consistent_statuses": (s1, s2),
        "consistent_acyclic": consistent_acyclic,
        "inverted_first": first,
        "inverted_refusal": refusal,
        "forced_cycle_detected": not forced.acyclic(),
        "no_endpoint_status": no_endpoint_status,
        "JointOrder_class_module": C612.JointOrder.__module__,
    }


def main() -> None:
    check(
        "the landed Cycle610, Cycle612, and Cycle703 local-Gauss runners are byte-pinned",
        C610_SHA == C610_SHA256
        and C612_SHA == C612_SHA256
        and GAUSS_SHA == GAUSS_SHA256,
        {
            "Cycle610": C610_SHA[:16],
            "Cycle612": C612_SHA[:16],
            "Cycle703_Gauss": GAUSS_SHA[:16],
        },
    )

    endpoint = endpoint_controls()
    check(
        "local matter B changes give a bounded reversible endpoint opportunity on every exact two-cell seam column",
        endpoint["pointer_inverse_failures"] == 0
        and endpoint["seam_predicate_failures"] == 0
        and endpoint["B_pointer_failures"] == 0
        and endpoint["matter_delta_count_failures"] == 0
        and endpoint["local_D_or_reference_failures"] == 0
        and endpoint["contact_false_positives"] == 0
        and endpoint["endpoint_true_cases"] > 0
        and endpoint["endpoint_false_cases"] > 0
        and endpoint["maximum_B_support_owner_cells"] <= 2
        and endpoint["proper_cubic_frames"] == 24
        and endpoint["frame_port_failures"] == 0
        and not endpoint["runtime_exterior_order_table_used"]
        and not endpoint["schedule_ordinal_read"],
        endpoint,
    )

    packet = packet_interface_controls()
    check(
        "the reversible software packet model projects exactly to unchanged Cycle610 admission and interval semantics",
        packet["matching_statuses"] == packet["Cycle610_append_attempts_compared"]
        and packet["bank_admitted"] == C610.BANK_SIZE
        and packet["bank_exhausted_seen"]
        and packet["refill_statuses"] == ("admitted", "admitted")
        and packet["no_endpoint_statuses"] == ("no_opportunity", "no_opportunity")
        and packet["duplicate_statuses"] == ("refused_fresh", "refused_fresh")
        and packet["no_actuality_statuses"] == ("refused_supplied", "refused_supplied")
        and packet["projection_failures"] == 0
        and packet["interval_failures"] == 0
        and packet["additivity_closed"]
        and packet["reversal_closed"],
        packet,
    )

    check(
        "the finite predecessor/interval software model has an exact inverse and replay",
        set(packet["inverse_statuses"]) == {"unappended"}
        and packet["inverse_returned_initial_state"]
        and packet["forward_replay_exact"]
        and packet["register_inverse_cases"] == 96
        and packet["register_inverse_failures"] == 0
        and packet["carry_truth_failures"] == 0
        and packet["software_packet_inverse_accessible"]
        and not packet["schedule_ordinal_stored"],
        {
            "inverse_statuses": packet["inverse_statuses"],
            "returned_initial": packet["inverse_returned_initial_state"],
            "replay": packet["forward_replay_exact"],
        },
    )

    joint = joint_order_controls()
    check(
        "the edge-qubit endpoint adapter preserves the unchanged Cycle612 acyclicity/refusal harness",
        joint["edge_qubit_opportunities"] == (1, 1)
        and joint["consistent_statuses"] == ("admitted", "admitted")
        and joint["consistent_acyclic"]
        and joint["inverted_first"] == "admitted"
        and joint["inverted_refusal"] == "refused_inverted"
        and joint["forced_cycle_detected"]
        and joint["no_endpoint_status"] == "no_opportunity",
        joint,
    )

    check(
        "physical-site placement, occurrence, admission, permanence, empirical unit, and state preparation remain explicit",
        packet["software_blank_address_selector_supplied"]
        and packet["actuality_admissibility_domain_supplied"]
        and not packet["empirical_unit_supplied"]
        and packet["software_packet_inverse_accessible"]
        and not BKSF_STATE_PREPARATION_EXECUTED,
        {
            "endpoint_type": "coherent candidate opportunity",
            "occurrence_and_admission": "supplied ports",
            "packet_type": "finite reversible software adapter; physical M2 bank unconstructed",
            "Record_permanence": False,
            "empirical_unit": None,
            "BKSF_state_preparation": False,
        },
    )

    certificate = {
        "endpoint": endpoint,
        "packet_interface": packet,
        "Cycle612_joint_order": joint,
    }
    digest = sha256(json.dumps(certificate, sort_keys=True, default=str,
        separators=(",", ":")).encode()).hexdigest()
    result = {
        "authority": "none",
        "audit": "unset",
        "cycle": 704,
        "status": "conditional-local-Gauss-Cycle612-endpoint-bridge",
        "terminal": "LOCAL_GAUSS_ENDPOINT_SOFTWARE_PACKET_INTERFACE_CLOSED_PHYSICAL_BANK_OPEN",
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "interface_equations": (
            "Pi_610 A_packet(P_B, supplied_tokens) = A_610 Pi_610",
            "D_packet = D_610 Pi_610 on the lawful predecessor domain",
            "J_612 Pi_610(packet identities) preserves JointOrder admission/refusal",
        ),
        "certificate": certificate,
        "supplied": (
            "local-D BKSF code and exact dressed FSWAP",
            "blank endpoint/payload values and address selection in the software model",
            "actuality, admissibility, law-domain, and co-registration ports",
            "Cycle610 K16 packet convention and Cycle612 cross-order rule",
        ),
        "derived": (
            "bounded coherent endpoint opportunity from local-Gauss edge-qubit B changes",
            "exact finite reversible predecessor/interval software adapter",
            "Cycle610 projection/intertwiner and unchanged Cycle612 order harness",
        ),
        "open": (
            "objective occurrence and an autonomous admission law",
            "Record permanence (the packet inverse remains accessible)",
            "empirical interval unit or identification with duration",
            "composition with the BKSF edge-qubit common E/preparation and a Z3 physical-site placement",
            "endpoints for diagonal-phase-only or general superposed coin dynamics",
            "a bit-level reversible M2 address, freshness, append/unappend, and bank-selection circuit",
        ),
        "claim_ceiling": (
            "A conditional finite interface theorem: on occupation-basis local-D edge-qubit seam transitions, "
            "a bounded matter-caused B-change opportunity feeds a finite reversible software adapter "
            "that projects exactly to the landed predecessor/interval and finite causal-order code. "
            "The BKSF graph has not been lifted into a physical-site placement and the packet bank "
            "has not been compiled to physical M2. This is not an occurrence law, "
            "Record, clock, empirical duration, or state-preparation result."
        ),
        "resources": {
            "elapsed_seconds": time.perf_counter() - START,
            "peak_rss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024 * 1024),
            "certificate_sha256": digest,
        },
    }
    print("SUMMARY_JSON", json.dumps(result, sort_keys=True, default=str))
    print("RESULT", result["terminal"] if result["pass"] else "UNFINISHED_IMPLEMENTATION")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
