#!/usr/bin/env python3
"""Block 67: signed Cycle-713 source through Records into a causal TT response.

This runner sharpens the conditional Blocks 52--66 vertical interfaces.  It
proves that an explicit immediate-registration contract selects hazard one and
that a sharp endpoint-current refinement exists for menu zero but not menu
one.  The selected signed event pair is written with the existing Block-64
carrier grammar.  A content-only root decoder keeps selecting that pair inside
continued history, while a radius-one head-child relation gives a conserved,
signed, arbitrary-horizon single-front source candidate.  Its spatial tensor
supplies a conditional nonzero Block-53 TT response.

The result is a bounded candidate theorem, not a retained law or TOE closure.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from pathlib import Path

import numpy as np
from scipy.linalg import null_space

import admissibility_cycle713_endpoint_record_attachment_intertwiner_boundary_2026_08_12 as b66
import admissibility_canonical_two_tt_positive_transfer_record_source_continuity_lstar_boundary_2026_08_11 as b52
import admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_2026_08_11 as b53


c713 = b66.c713
b65 = b66.b65
b64 = b65.b64
b63 = b65.b63
CNOT = c713.CNOT

ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 180
NOTE_PATH = ROOT / "docs" / "ADMISSIBILITY_CYCLE713_SIGNED_RECORD_SOURCE_CAUSAL_TT_VERTICAL_SLICE_BOUNDED_THEOREM_NOTE_2026-08-13.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
BLOCK66_NOTE = ROOT / "docs" / "ADMISSIBILITY_CYCLE713_ENDPOINT_RECORD_ATTACHMENT_INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-12.md"
BLOCK65_NOTE = ROOT / "docs" / "ADMISSIBILITY_PHYSICAL_STATE_TO_RECORD_ATTACHMENT_SELECTION_CUT_BOUNDED_THEOREM_NOTE_2026-08-12.md"
BLOCK64_NOTE = ROOT / "docs" / "ADMISSIBILITY_STRICT_NEAREST_NEIGHBOR_STATE_DEPENDENT_RECORD_BORN_HISTORY_SINGLE_FRONT_POSITIVE_THEOREM_NOTE_2026-08-12.md"
BLOCK52_NOTE = ROOT / "docs" / "ADMISSIBILITY_CANONICAL_TWO_TT_POSITIVE_TRANSFER_RECORD_SOURCE_CONTINUITY_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
BLOCK53_NOTE = ROOT / "docs" / "ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
BLOCK44_NOTE = ROOT / "docs" / "ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_CYCLE713_SIGNED_RECORD_SOURCE_CAUSAL_TT_VERTICAL_SLICE_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_CYCLE713_ENDPOINT_RECORD_ATTACHMENT_INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/ADMISSIBILITY_PHYSICAL_STATE_TO_RECORD_ATTACHMENT_SELECTION_CUT_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/ADMISSIBILITY_STRICT_NEAREST_NEIGHBOR_STATE_DEPENDENT_RECORD_BORN_HISTORY_SINGLE_FRONT_POSITIVE_THEOREM_NOTE_2026-08-12.md",
    "docs/ADMISSIBILITY_CANONICAL_TWO_TT_POSITIVE_TRANSFER_RECORD_SOURCE_CONTINUITY_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
)

TOL = 4.0e-11
FLIP_FORWARD = ((-1, 0, 0), (0, 1, 0), (0, 0, -1))
SOURCE_TORUS_SIZE = 5
SOURCE_INCIDENCE, SOURCE_EDGE_LOOKUP = b52.periodic_incidence(SOURCE_TORUS_SIZE)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str) -> None:
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        print(f"{'PASS' if result else 'FAIL'} {label}: {detail}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def bit(state: int, wire: int) -> int:
    return (state >> wire) & 1


def rotation_product(left: b64.Rotation, right: b64.Rotation) -> b64.Rotation:
    return tuple(
        tuple(sum(left[row][inner] * right[inner][column] for inner in range(3)) for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def signed_rotation(rotation: b64.Rotation, sign: int) -> b64.Rotation:
    if sign not in (-1, 1):
        raise ValueError(sign)
    return rotation if sign == 1 else rotation_product(rotation, FLIP_FORWARD)


def manhattan(left: b64.Coord, right: b64.Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def matrix_commutator(left: b63.Matrix, right: b63.Matrix) -> b63.Matrix:
    return b63.matrix_add(
        b63.matrix_multiply(left, right),
        b63.matrix_scale(Fraction(-1), b63.matrix_multiply(right, left)),
    )


def matrix_is_zero(value: b63.Matrix) -> bool:
    return value == b63.ZERO_MATRIX


def literal_signed_transfer() -> dict[str, object]:
    """Resolve the literal seam's before/after endpoint direction on all rows."""
    maps, structure = c713.literal_segment_maps(2)
    pointer = structure["new_auxiliary_wires"][2]
    transitions: dict[tuple[tuple[int, int], tuple[int, int], int], int] = {}
    failures = 0
    p1_rows = 0
    sign_failures = 0
    for source, row in enumerate(maps):
        failures += len(row) != 1
        if len(row) != 1:
            continue
        target = next(iter(row))
        pre = (bit(source, 1), bit(source, 6))
        post = (bit(target, 1), bit(target, 6))
        p = bit(target, pointer)
        transitions[(pre, post, p)] = transitions.get((pre, post, p), 0) + 1
        if p == 1:
            p1_rows += 1
            matter = post[1]
            sign = 2 * matter - 1
            expected = 1 if pre == (1, 0) and post == (0, 1) else -1
            sign_failures += pre not in ((1, 0), (0, 1)) or sign != expected
    expected = {
        (((0, 0), (0, 0), 0)): 1024,
        (((1, 0), (0, 1), 1)): 1024,
        (((0, 1), (1, 0), 1)): 1024,
        (((1, 1), (1, 1), 0)): 1024,
    }
    return {
        "rows": len(maps),
        "support_failures": failures,
        "transitions": transitions,
        "expected": expected,
        "p1_rows": p1_rows,
        "sign_failures": sign_failures,
    }


def closest_pointer_sites(
    choice: str,
    wire_sites: tuple[b64.Coord, ...],
    occupied: tuple[b64.Coord, ...] | list[b64.Coord],
) -> tuple[b64.Coord, b64.Coord, b64.Coord]:
    """Place the retained pointer next to the retained endpoint matter wire."""
    occupied_set = set(occupied)
    matter_wire = 6 if choice == "right" else 1
    matter_site = wire_sites[matter_wire]
    directions = ((-1, 0, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1), (0, 1, 0), (1, 0, 0))
    p_candidates = tuple(
        b64.add(matter_site, direction)
        for direction in directions
        if b64.add(matter_site, direction) not in occupied_set
    )
    if not p_candidates:
        raise RuntimeError("no blank nearest neighbour for retained pointer")
    pointer = sorted(p_candidates)[0]

    left_site, right_site = wire_sites[1], wire_sites[6]
    scratch_candidates = []
    for x in range(min(left_site[0], right_site[0]) - 2, max(left_site[0], right_site[0]) + 3):
        for y in range(min(left_site[1], right_site[1]) - 2, max(left_site[1], right_site[1]) + 3):
            for z in range(min(left_site[2], right_site[2]) - 2, max(left_site[2], right_site[2]) + 3):
                site = (x, y, z)
                if site in occupied_set or site == pointer:
                    continue
                dl, dr = manhattan(site, left_site), manhattan(site, right_site)
                scratch_candidates.append((max(dl, dr), dl + dr, site))
    scratch = tuple(row[2] for row in sorted(scratch_candidates)[:2])
    return scratch[0], scratch[1], pointer


def neighboring_physical_certificate(choice: str) -> dict[str, object]:
    cells = ((0, 0, 0), (1, 0, 0))
    C = c713.C712
    eq = C.C709.G.build_equivalence(cells).equivalence
    _eq2, graph, site_map, gauges, occupied, collisions = C.P709.placement_bundle(cells)
    carriers = C.carriers_for(eq, graph, site_map, gauges)
    wire_sites = tuple(carrier[0] for carrier in carriers)
    repeated = tuple(index for index, carrier in enumerate(carriers) if len(carrier) == 2)
    pointer_sites = closest_pointer_sites(choice, wire_sites, occupied)
    extended_sites = wire_sites + pointer_sites
    target_decode = C.synthesize_decode(eq.target_w, eq.target_v)
    target_encode = C.inverse_word(target_decode)
    decoded, qr_residual = c713.instrumented_decoded_word(2)
    decoded += b66.bridge_word(choice, 1, 6, eq.qubits + 2)
    repetition_decode = tuple(
        C.c707.Instruction("signed_record_repetition_decode_CNOT", carriers[index], CNOT)
        for index in repeated
    )
    repetition_encode = tuple(
        C.c707.Instruction("signed_record_repetition_encode_CNOT", carriers[index], CNOT)
        for index in reversed(repeated)
    )
    word = (
        repetition_decode
        + C.abstract_to_physical(target_decode, extended_sites, "signed_record_target_decode_")
        + C.abstract_to_physical(decoded, extended_sites, "signed_record_decoded_")
        + C.abstract_to_physical(target_encode, extended_sites, "signed_record_target_encode_")
        + repetition_encode
    )
    routed, route = C.c707.route_word(word)
    matter_site = wire_sites[6 if choice == "right" else 1]
    return {
        "choice": choice,
        "matter_pointer_distance": manhattan(matter_site, pointer_sites[2]),
        "assigned": len(occupied) + len(pointer_sites),
        "placement_collisions": collisions + len(pointer_sites) - len(set(pointer_sites)),
        "primitive_gates": len(word),
        "routed_gates": len(routed),
        "maximum_route_distance": route["maximum_route_distance"],
        "non_NN_failures": route["non_NN_failures"],
        "operand_order_failures": route["operand_order_failures"],
        "route_return_failures": route["route_return_failures"],
        "blank_route_work": len(set(route["touched_coordinates"]) - set(occupied) - set(pointer_sites)),
        "qr_residual": qr_residual,
    }


def joint_refinement_certificate() -> dict[str, object]:
    commutation_failures = marginal_failures = positivity_failures = 0
    menu1_noncommuting = 0
    nonzero_pairs = 0
    choi_minimum = np.inf
    rotations = b64.ROTATIONS
    for rotation in rotations:
        projectors = tuple(
            b63.rotate_hermitian(rotation, projector) for projector in (b65.P0, b65.P1)
        )
        for menu_index in (0, 1):
            effects = b65.rotated_effects(rotation, menu_index)
            commutators = tuple(
                matrix_commutator(projector, effect)
                for projector in projectors
                for effect in effects
            )
            if menu_index == 0:
                commutation_failures += sum(not matrix_is_zero(value) for value in commutators)
                joints = tuple(
                    tuple(b63.matrix_multiply(projector, effect) for projector in projectors)
                    for effect in effects
                )
                for outcome, row in enumerate(joints):
                    marginal_failures += b63.matrix_sum(row) != effects[outcome]
                    for sign_index, joint in enumerate(row):
                        positivity_failures += not b63.psd(joint)
                        if joint != b63.ZERO_MATRIX:
                            nonzero_pairs += 1
                            effect4 = b65.qkron(b65.P1, joint)
                            tau = b63.normalized_effect_state(effects[outcome])
                            choi = np.kron(b65.qnumpy(effect4).T, b63.to_numpy(tau))
                            choi_minimum = min(choi_minimum, float(np.linalg.eigvalsh(choi).min()))
                for sign_index, projector in enumerate(projectors):
                    marginal_failures += b63.matrix_sum(
                        tuple(joints[outcome][sign_index] for outcome in range(3))
                    ) != projector
            else:
                menu1_noncommuting += sum(not matrix_is_zero(value) for value in commutators)

    # Tomographically complete code-space and external-reference test.
    right_decoder = c713.word_matrix(b66.bridge_word("right", 0, 1, 2), 3)
    code_intertwiner = b66.extraction("right") @ right_decoder @ b66.encoding("right")
    effects = b65.rotated_effects(b64.IDENTITY_ROTATION, 0)
    projectors = (b65.P0, b65.P1)
    branches = tuple(
        (outcome, sign_index, b65.qkron(b65.P1, b63.matrix_multiply(projector, effects[outcome])))
        for outcome in range(3)
        for sign_index, projector in enumerate(projectors)
        if b63.matrix_multiply(projector, effects[outcome]) != b63.ZERO_MATRIX
    )
    reference_cases = 0
    reference_residual = 0.0
    for ref_row, ref_column, row, column in product(range(2), range(2), range(4), range(4)):
        ref_unit = np.zeros((2, 2), dtype=complex)
        ref_unit[ref_row, ref_column] = 1.0
        logical_unit = np.zeros((4, 4), dtype=complex)
        logical_unit[row, column] = 1.0
        recovered = code_intertwiner @ logical_unit @ code_intertwiner.conj().T
        for outcome, _sign_index, effect4 in branches:
            tau = b63.to_numpy(b63.normalized_effect_state(effects[outcome]))
            expected = np.trace(logical_unit @ b65.qnumpy(effect4)) * np.kron(ref_unit, tau)
            observed = np.trace(recovered @ b65.qnumpy(effect4)) * np.kron(ref_unit, tau)
            reference_residual = max(reference_residual, float(np.linalg.norm(observed - expected)))
            reference_cases += 1
    return {
        "rotations": len(rotations),
        "commutation_failures": commutation_failures,
        "marginal_failures": marginal_failures,
        "positivity_failures": positivity_failures,
        "menu1_noncommuting": menu1_noncommuting,
        "nonzero_pairs": nonzero_pairs,
        "choi_minimum": choi_minimum,
        "reference_cases": reference_cases,
        "reference_residual": reference_residual,
    }


def immediate_registration_certificate() -> dict[str, object]:
    """Separate conservation from the stronger no-live-branch contract.

    Block 65's no-Record Kraus branch retains the live P=1 matter state.  The
    immediate-registration contract is therefore an additional conditional
    rule, not a consequence of conservation.  It requires that branch's
    weight to vanish on every P=1 input on this attempt.
    """
    hazards = tuple(
        sorted(
            {
                Fraction(numerator, denominator)
                for denominator in range(1, 17)
                for numerator in range(denominator + 1)
            }
        )
    )
    matter_states = (
        b65.P0,
        b65.P1,
        b65.PPLUS,
        b63.matrix_scale(Fraction(1, 2), b63.IDENTITY),
        b63.pure_real(Fraction(3, 5), Fraction(4, 5)),
    )
    weight_failures = 0
    unique = []
    cases = 0
    for hazard in hazards:
        no_record, formation = b65.instrument_effects(
            b64.IDENTITY_ROTATION, 0, hazard
        )
        weights = []
        for matter in matter_states:
            omega = b65.product_state(b65.P1, matter)
            no_weight = b65.qtrace_product(omega, no_record)
            formation_weight = sum(
                (b65.qtrace_product(omega, effect) for effect in formation),
                Fraction(0),
            )
            weight_failures += no_weight != 1 - hazard
            weight_failures += formation_weight != hazard
            weights.append(no_weight)
            cases += 1
        if all(weight == 0 for weight in weights):
            unique.append(hazard)

    # At f=3/4 the no-Record Kraus action is exactly rho -> rho/4 on P=1,
    # so its normalized output is the same live matter state, not erasure.
    live_residual = 0.0
    for matter in matter_states:
        rho = b63.to_numpy(matter)
        output = 0.25 * rho
        live_residual = max(live_residual, float(np.linalg.norm(output / np.trace(output) - rho)))
    return {
        "hazards": len(hazards),
        "cases": cases,
        "weight_failures": weight_failures,
        "immediate_registration_solutions": tuple(unique),
        "three_quarter_live_residual": live_residual,
    }


@dataclass(frozen=True)
class SignedBranch:
    outcome: int
    sign: int
    direction: b64.Coord
    old_source: b64.Coord
    new_source: b64.Coord
    head_site: b64.Coord
    records: b64.Records


@dataclass(frozen=True)
class DecodedSource:
    direction: b64.Coord
    old_source: b64.Coord
    new_source: b64.Coord
    head_site: b64.Coord
    outcome: int


@dataclass(frozen=True)
class AppendEdge:
    old_source: b64.Coord
    new_source: b64.Coord
    direction: b64.Coord
    kind: str


def signed_branch(
    rotation: b64.Rotation,
    outcome: int,
    sign: int,
    origin: b64.Coord = b64.ORIGIN,
) -> SignedBranch:
    effects = b65.rotated_effects(rotation, 0)
    successor_rotation = signed_rotation(rotation, sign)
    direction = b64.rotate_coord(successor_rotation, b64.BASE_FORWARD)
    side = b64.rotate_coord(rotation, b64.BASE_TRANSVERSE)
    old_source = b64.add(origin, side)
    new_source = b64.add(old_source, direction)
    head_site = b64.add(origin, direction)
    outcome_record = b63.outcome_carrier(effects[outcome], outcome + 1)
    head_record = b64.context_carrier(
        "head",
        b63.normalized_effect_state(effects[outcome]),
        successor_rotation,
        1,
        1,
    )
    return SignedBranch(
        outcome,
        sign,
        direction,
        old_source,
        new_source,
        head_site,
        {new_source: outcome_record, head_site: head_record},
    )


def decode_signed_source(records: b64.Records) -> DecodedSource | None:
    """Decode the unique root event packet from an arbitrary continued front.

    Every ordinary Block-64 outcome has a compatible relay predecessor one
    forward edge behind it.  The supplied bootstrap outcome is the unique
    exception.  Its adjacent bootstrap head is then selected by the head's
    transverse geometry, without using a branch label or insertion history.
    """

    root_outcomes: list[tuple[b64.Coord, tuple[b64.Carrier, int]]] = []
    for outcome_site, carrier in records.items():
        decoded = b64.outcome_decode(carrier)
        if decoded is None:
            continue
        effect, outcome = decoded
        compatible_relays = tuple(
            relay_site
            for direction in b64.DIRECTIONS
            if (relay_site := b64.add(outcome_site, direction)) in records
            and (context := b64.decode_context(records[relay_site])) is not None
            and context.role == "relay"
            and b64.add(relay_site, context.forward) == outcome_site
            and b64.rotated_menus(context.rotation)[context.menu][outcome] == effect
        )
        if not compatible_relays:
            root_outcomes.append((outcome_site, decoded))

    if len(root_outcomes) != 1:
        return None
    new_source, (_effect, outcome) = root_outcomes[0]
    heads = tuple(
        (site, context)
        for direction in b64.DIRECTIONS
        if (site := b64.add(new_source, direction)) in records
        and (context := b64.decode_context(records[site])) is not None
        and context.role == "head"
        and b64.add(new_source, context.transverse) == site
    )
    if len(heads) != 1:
        return None
    head_site, context = heads[0]
    direction = context.forward
    old_source = b64.add(new_source, b64.neg(direction))
    if manhattan(old_source, new_source) != 1 or manhattan(head_site, new_source) != 1:
        return None
    return DecodedSource(direction, old_source, new_source, head_site, outcome)


def decode_active_append_edge(
    records: b64.Records,
    finalize_from_head: bool = False,
) -> AppendEdge | None:
    """Decode the unique next source hop from the current Record configuration."""
    active = b64.active_sites(records)
    if len(active) != 1:
        return None
    target, distribution = next(iter(active.items()))
    signature = b64.local_signature(records, target)
    contexts = tuple(
        (offset, context)
        for offset, carrier in signature.items()
        if (context := b64.decode_context(carrier)) is not None
    )
    if len(contexts) != 1:
        return None
    context_offset, context = contexts[0]
    if distribution.kind == "relay" and context.role == "head":
        source = b64.add(target, context_offset)
    elif distribution.kind == "outcome" and context.role == "relay":
        source = b64.add(target, context_offset)
    elif distribution.kind == "finalize" and context.role == "head":
        source = b64.add(
            target,
            context_offset if finalize_from_head else context.transverse,
        )
        carrier = records.get(source)
        if carrier is None or b64.outcome_decode(carrier) is None:
            return None
    else:
        return None
    direction = tuple(new - old for old, new in zip(source, target))
    if direction not in b64.DIRECTIONS:
        return None
    return AppendEdge(source, target, direction, distribution.kind)  # type: ignore[arg-type]


def edge_continuity_residual(edge: AppendEdge) -> float:
    size = SOURCE_TORUS_SIZE
    old_index = torus_index(edge.old_source, size)
    new_index = torus_index(edge.new_source, size)
    direction = np.asarray(edge.direction, dtype=float)
    axis = int(np.flatnonzero(np.abs(direction) > 0.5)[0])
    flux = np.zeros(3 * size**3)
    if int(direction[axis]) == 1:
        flux[SOURCE_EDGE_LOOKUP[(old_index, axis)]] = 1.0
    else:
        flux[SOURCE_EDGE_LOOKUP[(new_index, axis)]] = -1.0
    increment = np.zeros(size**3)
    increment[old_index] = -1.0
    increment[new_index] = 1.0
    return float(np.linalg.norm(increment + SOURCE_INCIDENCE @ flux))


@dataclass(frozen=True)
class HeadProfile:
    frontiers: tuple[b64.Coord, ...]
    heads: int
    children: int
    invalid_children: int


def decoded_head_child(
    records: b64.Records,
    site: b64.Coord,
    context: b64.Context,
    reverse_child: bool = False,
) -> tuple[b64.Coord | None, bool]:
    """Return a locally certified next head and an invalid-occupancy flag."""
    direction = b64.neg(context.forward) if reverse_child else context.forward
    target = b64.add(site, direction)
    carrier = records.get(target)
    if carrier is None:
        return None, False
    child = b64.decode_context(carrier)
    if child is None or child.role != "head":
        return None, True
    valid = (
        child.rotation == context.rotation
        and child.menu == 1 - context.menu
        and child.phase == 1 - context.phase
    )
    return (target, False) if valid else (None, True)


def decoded_head_profile(
    records: b64.Records,
    reverse_child: bool = False,
) -> HeadProfile:
    """Evaluate the radius-one head-child charge on a whole configuration."""
    frontiers: list[b64.Coord] = []
    heads = children = invalid_children = 0
    for site, carrier in records.items():
        context = b64.decode_context(carrier)
        if context is None or context.role != "head":
            continue
        heads += 1
        child, invalid = decoded_head_child(records, site, context, reverse_child)
        invalid_children += int(invalid)
        if child is None:
            frontiers.append(site)
        else:
            children += 1
    return HeadProfile(tuple(sorted(frontiers)), heads, children, invalid_children)


def head_source_worldline_certificate(
    reverse_child: bool = False,
) -> dict[str, object]:
    """Check the conditional head-source current at every Block-64 stage.

    The charge J_H is one on a head with no compatible head child and zero on
    a head that has one.  Relay and outcome writes leave J_H fixed; finalize
    moves it one forward edge.  Block64's symbolic support/active-site lemmas
    lift the executed finite checks to arbitrary single-front horizon.
    """
    innovations = tuple(
        Fraction(value, 31)
        for value in (1, 5, 9, 13, 17, 21, 25, 29, 3, 7, 11, 15, 19, 23, 27)
    )
    configurations = finalizations = zero_stages = 0
    profile_failures = root_failures = stage_failures = 0
    direction_failures = charge_failures = 0
    continuity_error = stress_error = 0.0
    direction_set: set[b64.Coord] = set()

    for rotation in b64.ROTATIONS:
        for outcome, sign in nonzero_menu0_pairs(rotation):
            branch = signed_branch(rotation, outcome, sign)
            records = dict(branch.records)
            root = decode_signed_source(records)
            root_failures += root is None or not (
                root.old_source == branch.old_source
                and root.new_source == branch.new_source
                and root.head_site == branch.head_site
                and root.direction == branch.direction
                and root.outcome == branch.outcome
            )
            profile = decoded_head_profile(records, reverse_child)
            profile_failures += not (
                profile.frontiers == (branch.head_site,)
                and profile.heads == 1
                and profile.children == 0
                and profile.invalid_children == 0
            )

            for step in range(18):
                expected_kind = ("relay", "outcome", "finalize")[step % 3]
                before = decoded_head_profile(records, reverse_child)
                profile_failures += not (
                    len(before.frontiers) == 1
                    and before.invalid_children == 0
                    and before.children == before.heads - 1
                )
                if len(before.frontiers) != 1:
                    stage_failures += 1
                    break
                old_frontier = before.frontiers[0]
                old_context = b64.decode_context(records[old_frontier])
                direction_failures += (
                    old_context is None
                    or old_context.role != "head"
                    or old_context.forward != branch.direction
                )

                active = b64.active_sites(records)
                if len(active) != 1:
                    stage_failures += 1
                    break
                target, distribution = next(iter(active.items()))
                stage_failures += (
                    distribution.kind != expected_kind
                    or not distribution.normalized
                )
                if expected_kind == "outcome":
                    _choice, carrier = b64.choose(
                        distribution, innovations[(step // 3) % len(innovations)]
                    )
                else:
                    _choice, carrier = b64.choose(distribution, Fraction(0))
                records = b64.append_one(records, target, carrier)

                after = decoded_head_profile(records, reverse_child)
                profile_failures += not (
                    len(after.frontiers) == 1
                    and after.invalid_children == 0
                    and after.children == after.heads - 1
                )
                if len(after.frontiers) != 1:
                    stage_failures += 1
                    break
                new_frontier = after.frontiers[0]
                if expected_kind == "finalize":
                    edge = AppendEdge(
                        old_frontier,
                        new_frontier,
                        tuple(
                            new - old
                            for old, new in zip(old_frontier, new_frontier)
                        ),
                        "head_finalize",
                    )
                    valid_edge = (
                        new_frontier == target
                        and edge.direction == branch.direction
                        and edge.direction in b64.DIRECTIONS
                    )
                    direction_failures += not valid_edge
                    if valid_edge:
                        residual = edge_continuity_residual(edge)
                        continuity_error = max(continuity_error, residual)
                        k = (1,) + edge.direction
                        stress_error = max(
                            stress_error,
                            *(abs(component) * residual for component in k),
                        )
                        direction_set.add(edge.direction)
                    else:
                        continuity_error = float("inf")
                        stress_error = float("inf")
                    charge_failures += before.heads + 1 != after.heads
                    finalizations += 1
                else:
                    charge_failures += (
                        new_frontier != old_frontier
                        or before.heads != after.heads
                    )
                    zero_stages += 1

                root = decode_signed_source(records)
                root_failures += root is None or not (
                    root.old_source == branch.old_source
                    and root.new_source == branch.new_source
                    and root.head_site == branch.head_site
                    and root.direction == branch.direction
                    and root.outcome == branch.outcome
                )
                configurations += 1

    symbolic_parent, symbolic_parent_checks = b64.symbolic_unique_active_induction()
    symbolic_support = b64.arbitrary_support_lemma()
    symbolic_stages = (
        ("relay", 0),
        ("outcome", 0),
        ("finalize", 1),
    )
    symbolic_ok = (
        symbolic_parent
        and symbolic_parent_checks == 5
        and symbolic_support
        and tuple(delta for _kind, delta in symbolic_stages) == (0, 0, 1)
    )
    return {
        "configurations": configurations,
        "finalizations": finalizations,
        "zero_stages": zero_stages,
        "profile_failures": profile_failures,
        "root_failures": root_failures,
        "stage_failures": stage_failures,
        "direction_failures": direction_failures,
        "charge_failures": charge_failures,
        "continuity_error": continuity_error,
        "stress_error": stress_error,
        "directions": tuple(sorted(direction_set)),
        "symbolic_ok": symbolic_ok,
        "symbolic_checks": symbolic_parent_checks + 2,
    }


def append_source_walk_certificate(
    finalize_from_head: bool = False,
) -> dict[str, object]:
    innovations = tuple(
        Fraction(value, 29)
        for value in (1, 5, 9, 13, 17, 21, 25, 3, 7, 11, 15, 19, 23, 27)
    )
    decode_failures = chain_failures = kind_failures = 0
    continuity_error = 0.0
    initial_edges = append_edges = 0
    direction_set: set[b64.Coord] = set()

    def run_steps(
        branch: SignedBranch,
        events: int,
    ) -> None:
        nonlocal decode_failures, chain_failures, kind_failures
        nonlocal continuity_error, initial_edges, append_edges
        records = dict(branch.records)
        decoded = decode_signed_source(records)
        decode_failures += decoded is None
        if decoded is None:
            return
        initial = (
            AppendEdge(
                decoded.old_source,
                decoded.new_source,
                decoded.direction,
                "bootstrap_outcome",
            ),
            AppendEdge(
                decoded.new_source,
                decoded.head_site,
                tuple(
                    head - outcome
                    for outcome, head in zip(decoded.new_source, decoded.head_site)
                ),
                "bootstrap_head",
            ),
        )
        current = branch.old_source
        for edge in initial:
            chain_failures += edge.old_source != current
            chain_failures += edge.direction not in b64.DIRECTIONS
            continuity_error = max(continuity_error, edge_continuity_residual(edge))
            direction_set.add(edge.direction)
            current = edge.new_source
            initial_edges += 1

        chain_failures += current != branch.head_site
        for event in range(events):
            for expected_kind in ("relay", "outcome", "finalize"):
                edge = decode_active_append_edge(records, finalize_from_head)
                decode_failures += edge is None
                if edge is None:
                    return
                chain_failures += edge.old_source != current
                kind_failures += edge.kind != expected_kind
                active = b64.active_sites(records)
                target, distribution = next(iter(active.items()))
                if expected_kind == "outcome":
                    _choice, carrier = b64.choose(
                        distribution, innovations[event % len(innovations)]
                    )
                else:
                    _choice, carrier = b64.choose(distribution, Fraction(0))
                records = b64.append_one(records, target, carrier)
                continuity_error = max(
                    continuity_error, edge_continuity_residual(edge)
                )
                direction_set.add(edge.direction)
                current = edge.new_source
                append_edges += 1

    for rotation in b64.ROTATIONS:
        for outcome, sign in nonzero_menu0_pairs(rotation):
            run_steps(signed_branch(rotation, outcome, sign), 1)
    for outcome, sign in nonzero_menu0_pairs(b64.IDENTITY_ROTATION):
        run_steps(signed_branch(b64.IDENTITY_ROTATION, outcome, sign), 32)

    symbolic_parent, symbolic_parent_checks = b64.symbolic_unique_active_induction()
    symbolic_source_roles = (
        ("head", "relay", "relay"),
        ("relay", "outcome", "outcome"),
        ("outcome", "head", "finalize"),
    )
    symbolic_ok = (
        symbolic_parent
        and symbolic_parent_checks == 5
        and len(symbolic_source_roles) == 3
        and tuple(item[2] for item in symbolic_source_roles)
        == ("relay", "outcome", "finalize")
    )
    return {
        "initial_edges": initial_edges,
        "append_edges": append_edges,
        "decode_failures": decode_failures,
        "chain_failures": chain_failures,
        "kind_failures": kind_failures,
        "continuity_error": continuity_error,
        "directions": tuple(sorted(direction_set)),
        "symbolic_ok": symbolic_ok,
        "symbolic_checks": symbolic_parent_checks + len(symbolic_source_roles),
    }


def nonzero_menu0_pairs(rotation: b64.Rotation) -> tuple[tuple[int, int], ...]:
    effects = b65.rotated_effects(rotation, 0)
    projectors = tuple(
        b63.rotate_hermitian(rotation, projector) for projector in (b65.P0, b65.P1)
    )
    return tuple(
        (outcome, 2 * sign_index - 1)
        for outcome in range(3)
        for sign_index, projector in enumerate(projectors)
        if b63.matrix_multiply(projector, effects[outcome]) != b63.ZERO_MATRIX
    )


def signed_record_certificate(forget_sign: bool = False) -> dict[str, object]:
    continuation_failures = geometry_failures = decode_failures = 0
    covariance_failures = chart_failures = 0
    continuations = long_continuations = active_checks = records_N33 = 0
    permanence_failures = whole_history_decoder_failures = 0
    whole_history_decoder_checks = 0
    innovations = tuple(Fraction(value, 23) for value in (1, 5, 9, 13, 17, 21, 3, 7, 11, 15, 19))
    for rotation in b64.ROTATIONS:
        pairs = nonzero_menu0_pairs(rotation)
        for outcome, physical_sign in pairs:
            sign = 1 if forget_sign else physical_sign
            branch = signed_branch(rotation, outcome, sign)
            context = b64.decode_context(branch.records[branch.head_site])
            geometry_failures += not (
                manhattan(branch.old_source, branch.new_source) == 1
                and manhattan(branch.head_site, branch.new_source) == 1
                and manhattan(b64.ORIGIN, branch.head_site) == 1
            )
            decode_failures += context is None or context.forward != branch.direction
            # Exhaust every branch through one complete relay/outcome/finalize
            # cycle.  Long history is then checked on the four base-orbit
            # representatives; the exact 24x24 test below transports it.
            run = b65.continue_block64(branch.records, 1, innovations)
            continuation_failures += not (
                run.ok and len(run.history) == 1 and len(run.records) == 5
            )
            permanence_failures += any(
                run.records.get(site) != carrier
                for site, carrier in branch.records.items()
            )
            whole = decode_signed_source(run.records)
            whole_history_decoder_failures += whole is None or not (
                whole.old_source == branch.old_source
                and whole.new_source == branch.new_source
                and whole.head_site == branch.head_site
                and whole.direction == branch.direction
                and whole.outcome == branch.outcome
            )
            whole_history_decoder_checks += 1
            continuations += 1
            active_checks += run.active_checks

    for outcome, sign in nonzero_menu0_pairs(b64.IDENTITY_ROTATION):
        branch = signed_branch(b64.IDENTITY_ROTATION, outcome, sign)
        run = b65.continue_block64(branch.records, 32, innovations)
        continuation_failures += not (
            run.ok and len(run.history) == 32 and len(run.records) == 98
        )
        permanence_failures += any(
            run.records.get(site) != carrier
            for site, carrier in branch.records.items()
        )
        whole = decode_signed_source(run.records)
        whole_history_decoder_failures += whole is None or not (
            whole.old_source == branch.old_source
            and whole.new_source == branch.new_source
            and whole.head_site == branch.head_site
            and whole.direction == branch.direction
            and whole.outcome == branch.outcome
        )
        whole_history_decoder_checks += 1
        long_continuations += 1
        active_checks += run.active_checks
        records_N33 = len(run.records)

    # Exact right/left internal-chart equivalence for the same physical signs.
    cx = b66.controlled_x()
    x = b63.to_numpy(b63.PAULI_X)
    effects = b65.rotated_effects(b64.IDENTITY_ROTATION, 0)
    for outcome, sign in nonzero_menu0_pairs(b64.IDENTITY_ROTATION):
        projector = b65.P1 if sign == 1 else b65.P0
        right_effect = b65.qnumpy(b65.qkron(b65.P1, b63.matrix_multiply(projector, effects[outcome])))
        left_projector = b66.x_conjugate(projector)
        left_effect2 = b63.matrix_multiply(left_projector, b66.x_conjugate(effects[outcome]))
        left_effect = b65.qnumpy(b65.qkron(b65.P1, left_effect2))
        chart_failures += np.linalg.norm(left_effect - cx @ right_effect @ cx.conj().T) >= TOL
        right_tau = b63.to_numpy(b63.normalized_effect_state(effects[outcome]))
        left_tau = b63.to_numpy(b63.normalized_effect_state(b66.x_conjugate(effects[outcome])))
        chart_failures += np.linalg.norm(left_tau - x @ right_tau @ x.conj().T) >= TOL

    # Full 24x24 co-transport of the signed frames, directions, and carriers.
    base_pairs = nonzero_menu0_pairs(b64.IDENTITY_ROTATION)
    for left in b64.ROTATIONS:
        for right in b64.ROTATIONS:
            composed = rotation_product(left, right)
            for outcome, sign in base_pairs:
                direct = signed_branch(composed, outcome, sign)
                prior = signed_branch(right, outcome, sign)
                expected_direction = b64.rotate_coord(left, prior.direction)
                expected_records = b65.transformed_records(prior.records, left, b64.ORIGIN)
                covariance_failures += direct.direction != expected_direction
                covariance_failures += direct.records != expected_records
    return {
        "continuations": continuations,
        "long_continuations": long_continuations,
        "continuation_failures": continuation_failures,
        "geometry_failures": geometry_failures,
        "decode_failures": decode_failures,
        "active_checks": active_checks,
        "records_N33": records_N33,
        "permanence_failures": permanence_failures,
        "whole_history_decoder_checks": whole_history_decoder_checks,
        "whole_history_decoder_failures": whole_history_decoder_failures,
        "chart_failures": chart_failures,
        "covariance_cases": 24 * 24 * len(base_pairs),
        "covariance_failures": covariance_failures,
    }


def torus_index(site: b64.Coord, size: int) -> int:
    wrapped = tuple((coordinate + size // 2) % size for coordinate in site)
    return (wrapped[0] * size + wrapped[1]) * size + wrapped[2]


def source_transition_certificate(reverse_incidence: bool = False) -> dict[str, object]:
    size = 5
    incidence, lookup = b52.periodic_incidence(size)
    continuity_error = stress_error = 0.0
    decoder_failures = 0
    symmetry_failures = null_trace_failures = sign_pair_failures = 0
    transitions = 0
    tensors: dict[tuple[b64.Coord, int], np.ndarray] = {}
    for rotation in b64.ROTATIONS:
        for sign in (-1, 1):
            branch = signed_branch(rotation, 1, sign)
            decoded = decode_signed_source(branch.records)
            decoder_failures += decoded is None
            if decoded is None:
                continue
            decoder_failures += not (
                decoded.old_source == branch.old_source
                and decoded.new_source == branch.new_source
                and decoded.direction == branch.direction
                and decoded.outcome == branch.outcome
            )
            old_index = torus_index(decoded.old_source, size)
            new_index = torus_index(decoded.new_source, size)
            direction = np.asarray(decoded.direction, dtype=float)
            axis = int(np.flatnonzero(np.abs(direction) > 0.5)[0])
            flux = np.zeros(3 * size**3)
            if int(direction[axis]) == 1:
                edge = lookup[(old_index, axis)]
                flux[edge] = 1.0
            else:
                edge = lookup[(new_index, axis)]
                flux[edge] = -1.0
            if reverse_incidence:
                flux *= -1.0
            increment = np.zeros(size**3)
            increment[old_index] = -1.0
            increment[new_index] = 1.0
            continuity_error = max(continuity_error, float(np.linalg.norm(increment + incidence @ flux)))

            k = np.concatenate(([1.0], direction))
            tensor = np.outer(k, k)
            tensors[(b64.rotate_coord(rotation, b64.BASE_FORWARD), sign)] = tensor
            symmetry_failures += not np.array_equal(tensor, tensor.T)
            null_trace_failures += abs(-tensor[0, 0] + np.trace(tensor[1:, 1:])) > TOL
            for column in range(4):
                stress_error = max(
                    stress_error,
                    float(np.linalg.norm(k[column] * increment + incidence @ (k[column] * flux))),
                )
            transitions += 1

    for axis in b64.DIRECTIONS[::2]:
        # Locate both signs on a frame whose unsigned forward is this positive axis.
        plus = tensors[(axis, 1)]
        minus = tensors[(axis, -1)]
        sign_pair_failures += not (
            plus[0, 0] == minus[0, 0]
            and np.array_equal(plus[1:, 1:], minus[1:, 1:])
            and np.array_equal(plus[0, 1:], -minus[0, 1:])
        )
    return {
        "transitions": transitions,
        "decoder_failures": decoder_failures,
        "continuity_error": continuity_error,
        "stress_error": stress_error,
        "symmetry_failures": symmetry_failures,
        "null_trace_failures": null_trace_failures,
        "sign_pair_failures": sign_pair_failures,
    }


def conditional_tt_projection_certificate(
    separate_source: bool = False,
    per_branch_coupling: bool = False,
) -> dict[str, object]:
    momentum = np.asarray((0.55, 0.83, -0.37))
    kappa_squared = b53.spatial_symbol(momentum)
    constraint = b53.tt_constraint(momentum)
    quotient = null_space(constraint, rcond=1.0e-11)
    delta = 0.5
    constraint_error = scale_error = 0.0
    minimum_tt_response = np.inf
    naive_row_mismatch = np.inf
    orientation_even_response_error = 0.0
    responses: dict[tuple[b64.Coord, int], dict[Fraction, np.ndarray]] = {}
    directions = b64.DIRECTIONS
    decoder_failures = 0
    for direction_tuple in directions:
        branch = next(
            signed_branch(rotation, 1, sign)
            for rotation in b64.ROTATIONS
            for sign in (-1, 1)
            if signed_branch(rotation, 1, sign).direction == direction_tuple
        )
        decoded = decode_signed_source(branch.records)
        decoder_failures += decoded is None or decoded.direction != direction_tuple
        if decoded is None:
            continue
        direction = np.asarray(decoded.direction, dtype=float)
        stress = np.outer(direction, direction)
        force_direction = np.roll(direction, 1) if separate_source else direction
        force_stress = np.outer(force_direction, force_direction)
        force = np.asarray([np.sum(basis * force_stress) for basis in b53.SYMMETRIC_BASIS])
        responses[(direction_tuple, 1)] = {}
        for coupling in (Fraction(1, 2), Fraction(1), Fraction(2)):
            branch_coupling = float(coupling)
            if per_branch_coupling and direction_tuple[0] < 0:
                branch_coupling *= 1.25
            h = np.zeros(6)
            p = np.zeros(6)
            source_h = np.zeros(4)
            source_p = np.zeros(4)
            for _ in range(2):
                p = p - delta * kappa_squared * h + delta * branch_coupling * force
                source_p = source_p - delta * kappa_squared * source_h + delta * branch_coupling * constraint @ force
                h = h + delta * p
                source_h = source_h + delta * source_p
                constraint_error = max(
                    constraint_error,
                    float(np.linalg.norm(constraint @ h - source_h)),
                    float(np.linalg.norm(constraint @ p - source_p)),
                )
            response = np.concatenate((quotient.T @ h, quotient.T @ p))
            responses[(direction_tuple, 1)][coupling] = response
            minimum_tt_response = min(minimum_tt_response, float(np.linalg.norm(response)))
        reference = responses[(direction_tuple, 1)][Fraction(1)]
        scale_error = max(
            scale_error,
            float(np.linalg.norm(responses[(direction_tuple, 1)][Fraction(1, 2)] - 0.5 * reference)),
            float(np.linalg.norm(responses[(direction_tuple, 1)][Fraction(2)] - 2.0 * reference)),
        )
        t0nu = np.concatenate(([1.0], direction))
        naive_row_mismatch = min(naive_row_mismatch, float(np.linalg.norm(t0nu - constraint @ force)))

    for positive in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
        negative = tuple(-value for value in positive)
        for coupling in (Fraction(1, 2), Fraction(1), Fraction(2)):
            orientation_even_response_error = max(
                orientation_even_response_error,
                float(
                    np.linalg.norm(
                        responses[(positive, 1)][coupling]
                        - responses[(negative, 1)][coupling]
                    )
                ),
            )

    # Check the inherited depth-two law across the full Brillouin-zone sample.
    grid = np.linspace(-np.pi, np.pi, 17)
    symplectic_form = np.asarray(((0.0, 1.0), (-1.0, 0.0)))
    symplectic_error = shadow_error = modulus_error = 0.0
    minimum_shadow = np.inf
    max_group_speed = 0.0
    for values in product(grid, repeat=3):
        sample = np.asarray(values)
        k2 = b53.spatial_symbol(sample)
        if k2 < 1.0e-13:
            continue
        _d, substep, shadow, macro, _frequency = b53.split_substep(k2, 2)
        symplectic_error = max(
            symplectic_error,
            float(np.linalg.norm(substep.T @ symplectic_form @ substep - symplectic_form)),
            float(np.linalg.norm(macro.T @ symplectic_form @ macro - symplectic_form)),
        )
        shadow_error = max(shadow_error, float(np.linalg.norm(macro.T @ shadow @ macro - shadow)))
        minimum_shadow = min(minimum_shadow, float(np.linalg.eigvalsh(shadow)[0]))
        modulus_error = max(modulus_error, float(np.max(np.abs(np.abs(np.linalg.eigvals(macro)) - 1.0))))
        sine_theta_sq = k2 / 4.0 * (1.0 - k2 / 16.0)
        velocity = np.sin(sample) / (2.0 * np.sqrt(sine_theta_sq))
        max_group_speed = max(max_group_speed, float(np.linalg.norm(velocity)))
    return {
        "directions": len(directions),
        "decoder_failures": decoder_failures,
        "constraint_error": constraint_error,
        "scale_error": scale_error,
        "minimum_tt_response": minimum_tt_response,
        "naive_row_mismatch": naive_row_mismatch,
        "orientation_even_response_error": orientation_even_response_error,
        "symplectic_error": symplectic_error,
        "shadow_error": shadow_error,
        "minimum_shadow": minimum_shadow,
        "modulus_error": modulus_error,
        "max_group_speed": max_group_speed,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutation",
        choices=(
            "forget_sign",
            "use_menu1",
            "hazard_three_quarters",
            "hide_physical_distance",
            "reverse_incidence",
            "reverse_head_child",
            "finalize_from_head",
            "separate_source",
            "per_branch_coupling",
            "broaden_boundary",
        ),
    )
    mutation = parser.parse_args().mutation
    checks = Checks()

    notes = tuple(flat(path) for path in (NOTE_PATH, AXIOM_PATH, BLOCK66_NOTE, BLOCK65_NOTE, BLOCK64_NOTE, BLOCK52_NOTE, BLOCK53_NOTE, BLOCK44_NOTE))
    source = " ".join(notes)
    checks.check(
        "A-source-stack-and-scope-binding",
        all((ROOT / path).exists() for path in AUDIT_INPUT_PATHS)
        and "does not choose a hamiltonian or transfer operator" in notes[1]
        and "the linear bianchi identity" in notes[7]
        and "zero toe percentage movement" in notes[0]
        and "conditional vertical interface" in notes[0],
        "Blocks 44 and 52--66 plus the current local axiom snapshot are bound as conditional inputs; no parent is promoted to retained law",
    )

    literal = literal_signed_transfer()
    coherent = b66.coherent_code_intertwiner()
    literal_ok = (
        literal["rows"] == 4096
        and literal["support_failures"] == 0
        and literal["transitions"] == literal["expected"]
        and literal["p1_rows"] == 2048
        and literal["sign_failures"] == 0
        and coherent["matrix_units"] == 16
        and coherent["matrix_unit_residual"] < TOL
    )
    checks.check(
        "B-literal-Cycle713-signed-single-particle-transfer",
        literal_ok,
        f"all {literal['rows']} rows resolve; the {literal['p1_rows']} P=1 rows are exact left/right transfers and 16/16 coherent matrix units survive",
    )

    physical = tuple(neighboring_physical_certificate(choice) for choice in ("right", "left"))
    route_failures = sum(
        int(item[key])
        for item in physical
        for key in ("placement_collisions", "non_NN_failures", "operand_order_failures", "route_return_failures")
    )
    physical_ok = (
        mutation != "hide_physical_distance"
        and route_failures == 0
        and all(item["matter_pointer_distance"] == 1 for item in physical)
        and all(item["assigned"] == 42 for item in physical)
        and all(item["qr_residual"] < TOL for item in physical)
    )
    checks.check(
        "C-neighboring-physical-P-tensor-M-boundary",
        physical_ok,
        f"right/left retained P--M distance=1/1 with routed gates={physical[0]['routed_gates']}/{physical[1]['routed_gates']}, max route={physical[0]['maximum_route_distance']}/{physical[1]['maximum_route_distance']}, failures={route_failures}",
    )

    joint = joint_refinement_certificate()
    registration = immediate_registration_certificate()
    hazard = Fraction(3, 4) if mutation == "hazard_three_quarters" else Fraction(1)
    joint_ok = (
        mutation != "use_menu1"
        and joint["rotations"] == 24
        and joint["commutation_failures"] == 0
        and joint["marginal_failures"] == 0
        and joint["positivity_failures"] == 0
        and joint["menu1_noncommuting"] == 96
        and joint["nonzero_pairs"] == 96
        and joint["choi_minimum"] > -TOL
        and joint["reference_cases"] == 256
        and joint["reference_residual"] < TOL
        and registration["weight_failures"] == 0
        and registration["immediate_registration_solutions"] == (Fraction(1),)
        and registration["three_quarter_live_residual"] < TOL
        and hazard in registration["immediate_registration_solutions"]
    )
    checks.check(
        "D-sharp-current-menu-and-immediate-registration-selector",
        joint_ok,
        f"menu0 has 4 nonzero joint branches/frame; menu1 has {joint['menu1_noncommuting']} noncommuting pairs; the additional no-live-branch-on-this-attempt contract uniquely gives f={registration['immediate_registration_solutions']}; f=3/4 instead retains the normalized live state",
    )

    signed = signed_record_certificate(mutation == "forget_sign")
    signed_ok = (
        signed["continuations"] == 96
        and signed["long_continuations"] == 4
        and signed["continuation_failures"] == 0
        and signed["geometry_failures"] == 0
        and signed["decode_failures"] == 0
        and signed["chart_failures"] == 0
        and signed["covariance_cases"] == 2304
        and signed["covariance_failures"] == 0
        and signed["records_N33"] == 98
        and signed["permanence_failures"] == 0
        and signed["whole_history_decoder_checks"] == 100
        and signed["whole_history_decoder_failures"] == 0
        and mutation != "forget_sign"
    )
    checks.check(
        "E-existing-carrier-signed-event-pair-and-Block64-seeding",
        signed_ok,
        f"all {signed['continuations']} signed event pairs seed one attachment cycle and remain unchanged; {signed['long_continuations']} orbit representatives continue 32 events, with {signed['whole_history_decoder_checks']} exact content-only root-pair selections and zero failures",
    )

    source_certificate = source_transition_certificate(mutation == "reverse_incidence")
    head_source = head_source_worldline_certificate(mutation == "reverse_head_child")
    append_walk = append_source_walk_certificate(mutation == "finalize_from_head")
    source_ok = (
        source_certificate["transitions"] == 48
        and source_certificate["decoder_failures"] == 0
        and source_certificate["continuity_error"] < TOL
        and source_certificate["stress_error"] < TOL
        and source_certificate["symmetry_failures"] == 0
        and source_certificate["null_trace_failures"] == 0
        and source_certificate["sign_pair_failures"] == 0
        and head_source["configurations"] == 1728
        and head_source["finalizations"] == 576
        and head_source["zero_stages"] == 1152
        and head_source["profile_failures"] == 0
        and head_source["root_failures"] == 0
        and head_source["stage_failures"] == 0
        and head_source["direction_failures"] == 0
        and head_source["charge_failures"] == 0
        and head_source["continuity_error"] < TOL
        and head_source["stress_error"] < TOL
        and set(head_source["directions"]) == set(b64.DIRECTIONS)
        and head_source["symbolic_ok"]
        and append_walk["decode_failures"] == 0
        and append_walk["chain_failures"] == 0
        and append_walk["kind_failures"] == 0
        and append_walk["continuity_error"] < TOL
        and set(append_walk["directions"]) == set(b64.DIRECTIONS)
        and append_walk["symbolic_ok"]
    )
    checks.check(
        "F-content-decoded-arbitrary-head-source-worldline",
        source_ok,
        f"{head_source['configurations']} whole-history stages resolve one head charge: {head_source['zero_stages']} zero-source relay/outcome writes and {head_source['finalizations']} signed NN moves cover six directions with exact four-column incidence; Block64 supplies the {head_source['symbolic_checks']}-check arbitrary-horizon lift (alternate microstep-ledger hops={append_walk['initial_edges'] + append_walk['append_edges']})",
    )

    causal = conditional_tt_projection_certificate(
        mutation == "separate_source",
        mutation == "per_branch_coupling",
    )
    causal_ok = (
        mutation not in ("separate_source", "per_branch_coupling")
        and causal["directions"] == 6
        and causal["decoder_failures"] == 0
        and causal["constraint_error"] < 3.0e-14
        and causal["scale_error"] < 3.0e-14
        and causal["minimum_tt_response"] > 0.04
        and causal["naive_row_mismatch"] > 0.1
        and causal["orientation_even_response_error"] < TOL
    )
    checks.check(
        "G-decoded-event-tensor-conditional-TT-response",
        causal_ok,
        f"the decoded event d-tensor has conditional nonzero TT response={causal['minimum_tt_response']:.6f}, and +/- responses correctly coincide to {causal['orientation_even_response_error']:.1e}; T00/T0i still require the open Block44 lapse/shift-source reconstruction (naive Block53-row mismatch={causal['naive_row_mismatch']:.3f})",
    )

    dynamics_ok = (
        causal["symplectic_error"] < 3.0e-14
        and causal["shadow_error"] < 4.0e-14
        and causal["minimum_shadow"] > 1.0e-4
        and causal["modulus_error"] < 4.0e-14
        and causal["max_group_speed"] <= 1.0 + 3.0e-14
    )
    checks.check(
        "H-depth-two-full-zone-positive-causal-control",
        dynamics_ok,
        f"shadow min={causal['minimum_shadow']:.6f}, symplectic={causal['symplectic_error']:.1e}, unit-circle={causal['modulus_error']:.1e}, max |vg|={causal['max_group_speed']:.12f}",
    )

    boundary_phrases = (
        "claim_type: bounded_theorem",
        "zero toe percentage movement",
        "pre-instrument preparation",
        "not one macro tick",
        "four current columns are not the four tt constraint rows",
        "global coupling remains supplied",
        "joint-instrument embedding",
        "immediate-registration contract is additional and unadopted",
        "no canonical axiom is edited",
    )
    boundary_ok = mutation != "broaden_boundary" and all(phrase in notes[0] for phrase in boundary_phrases)
    checks.check(
        "I-interface-cadence-normalization-and-retention-boundary",
        boundary_ok,
        "the prepared decoder, uncompiled joint instrument, conditional head-source identification, incidence ledger, and TT projection are typed separately; physical embedding and Block44 lapse/shift-source/Bianchi reconstruction remain open with cadence, coupling, adoption, and retention",
    )

    no_go_phrases = tuple(f"n{index} —" for index in range(1, 9)) + (
        "no-go discipline gate status: fail",
        "partial-narrowing",
        "unretained authority",
        "sharp-pvm commutant criterion",
        "pairwise directional wall table",
        "per-hit hidden-wall table",
        "per-citation residual table",
    )
    no_go_ok = all(phrase in notes[0] for phrase in no_go_phrases)
    checks.check(
        "J-no-go-discipline-honest-partial-narrowing",
        no_go_ok,
        "N1--N8 are landed; absent retained route authority makes the gate FAIL, so the fixed-menu commutator result ships only as partial-narrowing with live unsharp/replacement routes",
    )

    print(
        "METRICS "
        f"cycle713_rows={literal['rows']} p1_transfers={literal['p1_rows']} "
        f"joint_reference_cases={joint['reference_cases']} immediate_registration_cases={registration['cases']} signed_event_pairs={signed['continuations']} "
        f"head_source_moves={head_source['finalizations']} append_ledger_hops={append_walk['initial_edges'] + append_walk['append_edges']} routed_right_left={physical[0]['routed_gates']}/{physical[1]['routed_gates']}"
    )
    print(
        "N5_CERTIFICATE: every one of 4096 literal Cycle-713 rows, all 16 logical matrix units with a two-dimensional external reference, the exact hazard grid and live-branch controls, 24 proper frames and all 576 frame compositions, every nonzero menu-zero branch, all content-decoded head stages and six directions, four source-stress columns, three coupling controls, and the full 17-cubed momentum sample are resolved"
    )
    print(
        "per_element: each P-tensor-M matrix unit, joint branch effect, successor carrier field, source-current component, symmetric-tensor coordinate, and TT quotient coordinate is checked explicitly"
    )
    print(
        "per_site: the bootstrap root pair and head frontier are decoded from each whole configuration; all 576 finalize moves and the alternate append ledger are checked on the L=5 incidence carrier"
    )
    print(
        "per_mode: every point of the declared 17-by-17-by-17 Brillouin-zone sample is checked for depth-two symplecticity, positive shadow energy, unit-circle stability, and the unit group cone"
    )
    print(
        "per_block: Cycle713 decoding, physical P--M placement, sharp instrument refinement, signed event-pair attachment, arbitrary-horizon head-source induction, and conditional TT projection are checked at typed boundaries"
    )
    print(
        "lattice_wide: the declared single-front head-source current is translation/frame covariant for arbitrary finite horizon, but its physical source identity is conditional and no multi-front law, edge-stress Fourier map, selected cadence, metrology, nonlinear law, or retained theorem is inferred"
    )
    print(
        "scope_boundary: conditional signed event-pair interface, conserved arbitrary-length single-front head-source worldline candidate, sharp-menu discriminator, and immediate-registration contract test; not a compiled physical matter identity, Block52-to-Block44 source/Bianchi intertwiner, axiom update, retained theory, or TOE closure"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
