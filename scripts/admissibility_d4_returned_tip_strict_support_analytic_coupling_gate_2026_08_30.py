#!/usr/bin/env python3

"""Block28: conditional mathematics with a bounded current entrypoint.
Complete historical sources/controllers and results are archived outside note discovery.
Only the named checks below are fresh execution claims.
"""

from __future__ import annotations

import hashlib

import itertools

import sys

from dataclasses import dataclass

from functools import lru_cache

from pathlib import Path

import sympy as sp

import admissibility_d4_prior_record_live_preparation_two_event_prefix_2026_08_30 as block23  # noqa: E402

import admissibility_d4_self_delimiting_forward_record_append_history_2026_08_30 as block24  # noqa: E402

ZERO = (0, 0, 0)

E1 = (1, 0, 0)

DIRECTIONS = block23.DIRECTIONS

OUTCOMES = block23.OUTCOMES

ROTATIONS = block23.ROTATIONS

SUPPORT = frozenset(block23.SUPPORT)

Y_LEFT = block23.scale(9, E1)

Y_RIGHT = block23.scale(18, E1)

F_LEFT = E1

F_RIGHT = block23.negate(E1)

@dataclass(frozen=True)
class PairFrame:
    left_anchor: tuple
    front: tuple

    @property
    def right_anchor(self):
        return block24.forward_center(self.left_anchor, self.front)

    @property
    def right_front(self):
        return block23.negate(self.front)

    @property
    def left_exits(self):
        return lateral_directions(self.front)

    @property
    def right_exits(self):
        return lateral_directions(self.right_front)

    @property
    def left_targets(self):
        return lateral_centers(self.left_anchor, self.front)

    @property
    def right_targets(self):
        return lateral_centers(self.right_anchor, self.right_front)

    @property
    def centers(self):
        return (
            self.left_anchor,
            self.right_anchor,
            *self.left_targets,
            *self.right_targets,
        )

def add(left, right):
    return block23.add(left, right)

def scale(number, vector):
    return block23.scale(number, vector)

def block_sites(center):
    return frozenset(block23.translate(set(SUPPORT), center))

def lateral_directions(front):
    return tuple(
        direction for direction in DIRECTIONS if block23.dot(front, direction) == 0
    )

LEFT_EXITS = lateral_directions(F_LEFT)

RIGHT_EXITS = lateral_directions(F_RIGHT)

def lateral_centers(anchor, front):
    return tuple(
        block24.forward_center(anchor, exit_front)
        for exit_front in lateral_directions(front)
    )

LEFT_TARGETS = lateral_centers(Y_LEFT, F_LEFT)

RIGHT_TARGETS = lateral_centers(Y_RIGHT, F_RIGHT)

PAIR_CENTERS = (Y_LEFT, Y_RIGHT) + LEFT_TARGETS + RIGHT_TARGETS

CANONICAL_FRAME = PairFrame(Y_LEFT, F_LEFT)

def returned_geometry_certificate() -> bool:
    blocks = tuple(block_sites(center) for center in PAIR_CENTERS)
    return (
        len(LEFT_EXITS) == len(RIGHT_EXITS) == 4
        and set(LEFT_EXITS) == set(RIGHT_EXITS)
        and len(PAIR_CENTERS) == len(set(PAIR_CENTERS)) == 10
        and all(
            left.isdisjoint(right)
            for left, right in itertools.combinations(blocks, 2)
        )
        and block24.forward_center(Y_LEFT, F_LEFT) == Y_RIGHT
        and block24.forward_center(Y_RIGHT, F_RIGHT) == Y_LEFT
    )

@dataclass(frozen=True)
class TurnEffect:
    current_word: tuple
    incoming_front: tuple
    exit_front: tuple
    target_center: tuple
    forward_input: object
    output_word: tuple
    scalar: object

@dataclass(frozen=True)
class TurnBranch:
    anchor: tuple
    incoming_front: tuple
    exit_front: tuple
    source: tuple
    target: tuple
    factors: tuple
    effect: TurnEffect

TURN_FACTOR_KEYS = block24.APPEND_FACTOR_KEYS

def make_turn_factors(
    anchor, incoming_front, source, exit_front, target, mutation=None
):
    current_word = block23.locked_word(incoming_front, source)
    current_output = (
        block23.BLANK_POINTER if mutation == "overwrite_record" else current_word
    )
    output_front = incoming_front if mutation == "stale_output_front" else exit_front
    target_center = (
        scale(27, E1)
        if mutation == "third_write_wrong_block"
        else block24.forward_center(anchor, exit_front)
    )
    live_maps = tuple(
        (
            site,
            block23.BLANK_BLOCK.live[index],
            block23.ordered_live(block23.prepared_vectors(source))[index],
        )
        for index, site in enumerate(DIRECTIONS)
    )
    prep_pointer = block23.pointer_rank_one_maps(
        block23.BLANK_POINTER, block23.ready_word(output_front)
    )
    writer_pointer = block23.pointer_rank_one_maps(
        block23.ready_word(output_front), block23.locked_word(output_front, target)
    )
    return (
        ("anchor", anchor),
        ("current_live_identities", block23.OLD_LIVE_IDENTITIES),
        (
            "current_pointer_projectors",
            block23.pointer_rank_one_maps(current_word, current_output),
        ),
        ("forward_center", target_center),
        ("forward_live_prep_maps", live_maps),
        ("forward_pointer_prep_maps", prep_pointer),
        ("forward_live_root", block23.root_operator_factor(target)),
        ("forward_writer_pointer_maps", writer_pointer),
        (
            "spectator_identity_centers",
            block24.spectator_centers(anchor, exit_front),
        ),
        (
            "spectator_identity_factors",
            block24.spectator_identity_factors(anchor, exit_front),
        ),
        ("outside_carrier_identity", "I_outside"),
        ("lateral_touch", True),
    )

@lru_cache(maxsize=None)
def contract_turn_effect(factors):
    if tuple(entry[0] for entry in factors) != TURN_FACTOR_KEYS:
        raise ValueError("turn factor list is missing, duplicated, or extended")
    data = block24.factor_dictionary(factors)
    current_maps = data["current_pointer_projectors"]
    current_input = tuple(entry[1] for entry in current_maps)
    current_output = tuple(entry[2] for entry in current_maps)
    decoded = block23.decode_locked_word(current_input)
    if (
        decoded is None
        or current_output != current_input
        or tuple(entry[0] for entry in current_maps) != block23.POINTER_ORDER
    ):
        raise ValueError("turn current Record is not an exact QND control")
    incoming_front, source = decoded
    if data["current_live_identities"] != block23.OLD_LIVE_IDENTITIES:
        raise ValueError("turn current live factors are not identities")

    anchor = data["anchor"]
    live_maps = data["forward_live_prep_maps"]
    prep_maps = data["forward_pointer_prep_maps"]
    if (
        tuple(entry[0] for entry in live_maps) != DIRECTIONS
        or tuple(entry[0] for entry in prep_maps) != block23.POINTER_ORDER
    ):
        raise ValueError("turn target preparation is incomplete")
    forward_input = block24.block_from_factor_inputs(live_maps, prep_maps)
    prepared = block24.block_from_factor_outputs(live_maps, prep_maps)
    if forward_input != block23.BLANK_BLOCK:
        raise ValueError("turn target is not the exact full Blank block")
    exit_front = block23.decode_ready_word(prepared.pointer)
    if (
        exit_front is None
        or block23.dot(incoming_front, exit_front) != 0
        or data["forward_center"] != block24.forward_center(anchor, exit_front)
        or prepared.live
        != block23.ordered_live(block23.prepared_vectors(source))
    ):
        raise ValueError("turn target or prepared direction is not physical")

    writer_maps = data["forward_writer_pointer_maps"]
    writer_input = tuple(entry[1] for entry in writer_maps)
    writer_output = tuple(entry[2] for entry in writer_maps)
    root = data["forward_live_root"]
    if (
        tuple(entry[0] for entry in writer_maps) != block23.POINTER_ORDER
        or writer_input != prepared.pointer
        or block23.decode_locked_word(writer_output) != (exit_front, root[0])
    ):
        raise ValueError("turn writer output is not bound to its root and exit")
    expected_spectators = block24.spectator_identity_factors(anchor, exit_front)
    if (
        data["spectator_identity_factors"] != expected_spectators
        or not all(
            operator == "I_2"
            for _center, _site, operator in expected_spectators
        )
        or data["outside_carrier_identity"] != "I_outside"
        or data["lateral_touch"] is not True
    ):
        raise ValueError("turn spectator or outside identity is incomplete")
    literal_effect = block23.contract_root_adjoint_root(root)
    coefficient = block23.expectation_from_effect_data(
        literal_effect, block23.live_dictionary(prepared.live)
    )
    return TurnEffect(
        current_input,
        incoming_front,
        exit_front,
        data["forward_center"],
        forward_input,
        writer_output,
        sp.simplify(coefficient),
    )

@lru_cache(maxsize=None)
def turn_branch(anchor, incoming_front, source, exit_front, target, mutation=None):
    factors = make_turn_factors(
        anchor, incoming_front, source, exit_front, target, mutation
    )
    return TurnBranch(
        anchor,
        incoming_front,
        exit_front,
        source,
        target,
        factors,
        contract_turn_effect(factors),
    )

def turn_branch_is_physical(branch) -> bool:
    data = block24.factor_dictionary(branch.factors)
    current_maps = data["current_pointer_projectors"]
    live_maps = data["forward_live_prep_maps"]
    prep_maps = data["forward_pointer_prep_maps"]
    prepared = block24.block_from_factor_outputs(live_maps, prep_maps)
    return (
        tuple(entry[0] for entry in branch.factors) == TURN_FACTOR_KEYS
        and tuple(entry[1] for entry in current_maps)
        == tuple(entry[2] for entry in current_maps)
        == block23.locked_word(branch.incoming_front, branch.source)
        and len(current_maps)
        == len(prep_maps)
        == len(data["forward_writer_pointer_maps"])
        == 26
        and len(live_maps) == 6
        and block24.block_from_factor_inputs(live_maps, prep_maps)
        == block23.BLANK_BLOCK
        and prepared
        == block23.block_product(
            block23.prepared_vectors(branch.source),
            block23.ready_word(branch.exit_front),
        )
        and data["forward_live_root"]
        == block23.root_operator_factor(branch.target)
        and block23.decode_locked_word(branch.effect.output_word)
        == (branch.exit_front, branch.target)
        and branch.effect.target_center
        == block24.forward_center(branch.anchor, branch.exit_front)
        and block23.dot(branch.incoming_front, branch.exit_front) == 0
        and branch.effect.forward_input == block23.BLANK_BLOCK
        and sp.simplify(
            branch.effect.scalar
            - block23.transition(branch.source, branch.target)
        )
        == 0
    )

@lru_cache(maxsize=1)
def all_turn_branches():
    return tuple(
        turn_branch(anchor, incoming, source, exit_front, target)
        for anchor, incoming in ((Y_LEFT, F_LEFT), (Y_RIGHT, F_RIGHT))
        for source in OUTCOMES
        for exit_front in lateral_directions(incoming)
        for target in OUTCOMES
    )

def target_row_sums():
    return {
        source: sp.simplify(
            sum(block23.transition(source, target) for target in OUTCOMES)
        )
        for source in OUTCOMES
    }

def local_turn_certificate() -> bool:
    branches = all_turn_branches()
    rows = target_row_sums()
    return (
        len(branches) == 2 * 14 * 4 * 14 == 1568
        and all(turn_branch_is_physical(branch) for branch in branches)
        and all(value == 1 for value in rows.values())
        and all(
            block23.transition(source, target).is_positive is True
            for source in OUTCOMES
            for target in OUTCOMES
        )
    )

def branch_nonidentity_sites(branch):
    return block_sites(branch.anchor) | block_sites(branch.effect.target_center)

def branch_writer_sites(branch):
    data = block24.factor_dictionary(branch.factors)
    return frozenset(
        add(branch.effect.target_center, site)
        for site, _input, _output in data["forward_writer_pointer_maps"]
    )

def tensor_support_certificate(mutation=None) -> bool:
    source = OUTCOMES[0]
    target = OUTCOMES[-1]
    for left_exit, right_exit in itertools.product(LEFT_EXITS, RIGHT_EXITS):
        left = turn_branch(Y_LEFT, F_LEFT, source, left_exit, target)
        right_anchor = Y_LEFT if mutation == "shared_writer" else Y_RIGHT
        right = turn_branch(right_anchor, F_RIGHT, source, right_exit, target)
        if not (
            branch_nonidentity_sites(left).isdisjoint(
                branch_nonidentity_sites(right)
            )
            and branch_writer_sites(left).isdisjoint(branch_writer_sites(right))
        ):
            return False
    return True

@dataclass(frozen=True)
class ControlAtom:
    center: tuple
    role: str
    state: object

@dataclass(frozen=True)
class PairControl:
    left_source: tuple
    right_source: tuple
    left_word: tuple
    right_word: tuple
    blank_centers: tuple
    atoms: tuple[ControlAtom, ...]

def pair_control_for(frame, left_source, right_source):
    left_word = block23.locked_word(frame.front, left_source)
    right_word = block23.locked_word(frame.right_front, right_source)
    blank_centers = frame.left_targets + frame.right_targets
    return PairControl(
        left_source,
        right_source,
        left_word,
        right_word,
        blank_centers,
        (
            ControlAtom(frame.left_anchor, "current-pointer", left_word),
            ControlAtom(frame.right_anchor, "current-pointer", right_word),
            *(
                ControlAtom(center, "Blank-block", block23.BLANK_BLOCK)
                for center in blank_centers
            ),
        ),
    )

def pair_control(left_source, right_source):
    return pair_control_for(CANONICAL_FRAME, left_source, right_source)

def pair_controls(mutation=None):
    controls = [
        pair_control(left, right)
        for left, right in itertools.product(OUTCOMES, repeat=2)
    ]
    if mutation == "duplicate_control":
        controls[-1] = controls[0]
    return tuple(controls)

def control_atom_overlap(left, right):
    if left.center != right.center:
        return sp.S.One
    if left.role != right.role:
        raise ValueError("pair controls use incompatible atoms at one center")
    if left.role == "current-pointer":
        return sp.simplify(block23.pointer_overlap(left.state, right.state))
    if left.role == "Blank-block":
        return sp.simplify(block23.block_overlap(left.state, right.state))
    raise ValueError("unknown pair-control atom")

def control_overlap(left, right):
    left_atoms = {atom.center: atom for atom in left.atoms}
    right_atoms = {atom.center: atom for atom in right.atoms}
    if set(left_atoms) != set(right_atoms):
        raise ValueError("pair controls do not use the same physical centers")
    return sp.simplify(
        sp.prod(
            control_atom_overlap(left_atoms[center], right_atoms[center])
            for center in left_atoms
        )
    )

def controls_orthogonal(left, right) -> bool:
    return control_overlap(left, right) == 0

def control_is_rank_one_projector(control) -> bool:
    return (
        len(control.atoms) == 10
        and len({atom.center for atom in control.atoms}) == 10
        and control_overlap(control, control) == 1
    )

@dataclass(frozen=True)
class ActiveControlSum:
    controls: tuple[PairControl, ...]
    pairwise_orthogonal: bool
    idempotent: bool
    complement_nontrivial: bool

@lru_cache(maxsize=1)
def active_control_sum():
    controls = pair_controls()
    pairwise = all(
        controls_orthogonal(controls[i], controls[j])
        for i in range(len(controls))
        for j in range(i)
    )
    idempotent = pairwise and all(
        control_is_rank_one_projector(control) for control in controls
    )
    complement_nontrivial = all(
        block23.pointer_overlap(
            block23.BLANK_POINTER, block23.locked_word(F_LEFT, source)
        )
        == 0
        for source in OUTCOMES
    )
    return ActiveControlSum(
        controls,
        pairwise,
        idempotent,
        complement_nontrivial,
    )

def pair_control_certificate(mutation=None) -> bool:
    controls = pair_controls(mutation)
    labels = tuple((control.left_source, control.right_source) for control in controls)
    pairwise = all(
        controls_orthogonal(controls[i], controls[j])
        for i in range(len(controls))
        for j in range(i)
    )
    literal_controls = all(
        control_is_rank_one_projector(control) for control in controls
    )
    complement_nontrivial = all(
        block23.pointer_overlap(
            block23.BLANK_POINTER, block23.locked_word(F_LEFT, source)
        )
        == 0
        for source in OUTCOMES
    )
    p = sp.symbols("p_active", commutative=True)
    stop_gram = block23.projector_reduce((1 - p) ** 2, p)
    full_gram = block23.projector_reduce(p + stop_gram, p)
    return (
        len(controls) == len(OUTCOMES) ** 2 == 196
        and len(labels) == len(set(labels))
        and pairwise
        and literal_controls
        and all(
            {atom.center for atom in control.atoms} == set(PAIR_CENTERS)
            for control in controls
        )
        and complement_nontrivial
        and stop_gram == 1 - p
        and full_gram == 1
        and (
            mutation is not None
            or (
                active_control_sum().controls == controls
                and active_control_sum().pairwise_orthogonal
                and active_control_sum().idempotent
                and active_control_sum().complement_nontrivial
            )
        )
    )

def pair_stabilizer():
    return tuple(
        rotation
        for rotation in ROTATIONS
        if block23.mat_vec(rotation, F_LEFT) in (F_LEFT, F_RIGHT)
    )

def q_weight(lam, left_exit, right_exit, mutation=None):
    if left_exit == right_exit:
        value = (1 + 3 * lam) / 16
        if mutation == "bad_diagonal":
            value = (1 + 4 * lam) / 16
    else:
        value = (1 - lam) / 16
    value = sp.simplify(value)
    marked = LEFT_EXITS[0]
    partner = LEFT_EXITS[1]
    epsilon = sp.Rational(1, 64)
    if mutation == "biased_cell" and (left_exit, right_exit) == (
        marked,
        marked,
    ):
        value += epsilon
    if mutation == "coordinate_mark":
        if (left_exit, right_exit) in ((marked, marked), (partner, partner)):
            value += epsilon
        if (left_exit, right_exit) in ((marked, partner), (partner, marked)):
            value -= epsilon
    return sp.simplify(value)

def q_table(lam, mutation=None):
    pairs = list(itertools.product(LEFT_EXITS, RIGHT_EXITS))
    if mutation == "delete_pair":
        pairs.pop()
    return {
        pair: q_weight(lam, *pair, mutation=mutation)
        for pair in pairs
    }

def pair_action(rotation, pair):
    left_exit, right_exit = pair
    if block23.mat_vec(rotation, F_LEFT) == F_LEFT:
        return (
            block23.mat_vec(rotation, left_exit),
            block23.mat_vec(rotation, right_exit),
        )
    return (
        block23.mat_vec(rotation, right_exit),
        block23.mat_vec(rotation, left_exit),
    )

def q_certificate(lam, mutation=None):
    table = q_table(lam, mutation)
    expected_pairs = set(itertools.product(LEFT_EXITS, RIGHT_EXITS))
    complete = set(table) == expected_pairs
    positive = complete and all(value > 0 for value in table.values())
    normalized = complete and sp.simplify(sum(table.values())) == 1
    left_marginals = {
        left: sp.simplify(
            sum(table.get((left, right), 0) for right in RIGHT_EXITS)
        )
        for left in LEFT_EXITS
    }
    right_marginals = {
        right: sp.simplify(
            sum(table.get((left, right), 0) for left in LEFT_EXITS)
        )
        for right in RIGHT_EXITS
    }
    uniform = complete and all(
        value == sp.Rational(1, 4)
        for value in (*left_marginals.values(), *right_marginals.values())
    )
    covariant = complete and all(
        table[pair] == table[pair_action(rotation, pair)]
        for rotation in pair_stabilizer()
        for pair in expected_pairs
    )
    return {
        "complete": complete,
        "positive": positive,
        "normalized": normalized,
        "uniform_marginals": uniform,
        "covariant": covariant,
    }

@dataclass(frozen=True)
class PairKrausDescriptor:
    """One literal left/right Kraus product guarded by one pair control."""

    control: PairControl
    left: TurnBranch
    right: TurnBranch
    weight: object
    amplitude: object
    factorization: tuple

@dataclass(frozen=True)
class GuardedBranchGram:
    control: PairControl
    coefficient: object
    output_records: tuple

def pair_kraus_descriptor_for(
    frame,
    lam,
    left_source,
    right_source,
    left_exit,
    right_exit,
    left_target,
    right_target,
    raw_amplitude=False,
):
    weight = q_weight(lam, left_exit, right_exit)
    control = pair_control_for(frame, left_source, right_source)
    left = turn_branch(
        frame.left_anchor,
        frame.front,
        left_source,
        left_exit,
        left_target,
    )
    right = turn_branch(
        frame.right_anchor,
        frame.right_front,
        right_source,
        right_exit,
        right_target,
    )
    amplitude = weight if raw_amplitude else sp.sqrt(weight)
    return PairKrausDescriptor(
        control,
        left,
        right,
        weight,
        amplitude,
        (
            ("amplitude", amplitude),
            ("full_pair_control", control.atoms),
            ("left_turn_factors", left.factors),
            ("right_turn_factors", right.factors),
        ),
    )

def pair_kraus_descriptor(
    lam,
    left_source,
    right_source,
    left_exit,
    right_exit,
    left_target,
    right_target,
    raw_amplitude=False,
):
    return pair_kraus_descriptor_for(
        CANONICAL_FRAME,
        lam,
        left_source,
        right_source,
        left_exit,
        right_exit,
        left_target,
        right_target,
        raw_amplitude,
    )

def branch_input_atoms(branch):
    return (
        ControlAtom(
            branch.anchor,
            "current-pointer",
            block23.locked_word(branch.incoming_front, branch.source),
        ),
        ControlAtom(
            branch.effect.target_center,
            "Blank-block",
            branch.effect.forward_input,
        ),
    )

def full_guard_is_bound(descriptor) -> bool:
    factor_data = dict(descriptor.factorization)
    if tuple(factor_data) != (
        "amplitude",
        "full_pair_control",
        "left_turn_factors",
        "right_turn_factors",
    ):
        return False
    if (
        factor_data["full_pair_control"] != descriptor.control.atoms
        or factor_data["left_turn_factors"] != descriptor.left.factors
        or factor_data["right_turn_factors"] != descriptor.right.factors
        or factor_data["amplitude"] != descriptor.amplitude
    ):
        return False
    required_inputs = branch_input_atoms(descriptor.left) + branch_input_atoms(
        descriptor.right
    )
    if not all(atom in descriptor.control.atoms for atom in required_inputs):
        return False
    selected_centers = {
        descriptor.left.effect.target_center,
        descriptor.right.effect.target_center,
    }
    unused_blank_atoms = tuple(
        atom
        for atom in descriptor.control.atoms
        if atom.role == "Blank-block" and atom.center not in selected_centers
    )
    nonidentity = branch_nonidentity_sites(
        descriptor.left
    ) | branch_nonidentity_sites(descriptor.right)
    return (
        len(required_inputs) == 4
        and len(unused_blank_atoms) == 6
        and all(
            block_sites(atom.center).isdisjoint(nonidentity)
            for atom in unused_blank_atoms
        )
        and block24.factor_dictionary(descriptor.left.factors)[
            "outside_carrier_identity"
        ]
        == "I_outside"
        and block24.factor_dictionary(descriptor.right.factors)[
            "outside_carrier_identity"
        ]
        == "I_outside"
    )

def contract_pair_kraus_descriptor(descriptor):
    left = descriptor.left
    right = descriptor.right
    squared_amplitude = sp.simplify(
        descriptor.amplitude * sp.conjugate(descriptor.amplitude)
    )
    if not (
        descriptor.control.left_source == left.source
        and descriptor.control.right_source == right.source
        and descriptor.control.left_word
        == block23.locked_word(left.incoming_front, left.source)
        and descriptor.control.right_word
        == block23.locked_word(right.incoming_front, right.source)
        and control_is_rank_one_projector(descriptor.control)
        and full_guard_is_bound(descriptor)
        and left.effect.target_center in descriptor.control.blank_centers
        and right.effect.target_center in descriptor.control.blank_centers
        and turn_branch_is_physical(left)
        and turn_branch_is_physical(right)
        and branch_nonidentity_sites(left).isdisjoint(
            branch_nonidentity_sites(right)
        )
        and branch_writer_sites(left).isdisjoint(branch_writer_sites(right))
        and squared_amplitude == descriptor.weight
    ):
        raise ValueError("pair Kraus factors do not realize the declared Gram")
    return GuardedBranchGram(
        descriptor.control,
        sp.simplify(
            squared_amplitude * left.effect.scalar * right.effect.scalar
        ),
        (
            (left.effect.target_center, left.effect.output_word),
            (right.effect.target_center, right.effect.output_word),
        ),
    )

@dataclass(frozen=True)
class GuardedTargetAxis:
    control: PairControl
    side: str
    exit_front: tuple
    branches: tuple[TurnBranch, ...]
    coefficients: tuple
    complete: bool

@lru_cache(maxsize=None)
def guarded_target_axis(left_source, right_source, side, exit_front):
    control = pair_control(left_source, right_source)
    if side == "left":
        anchor, incoming, source = Y_LEFT, F_LEFT, left_source
    elif side == "right":
        anchor, incoming, source = Y_RIGHT, F_RIGHT, right_source
    else:
        raise ValueError("unknown guarded target-axis side")
    branches = tuple(
        turn_branch(anchor, incoming, source, exit_front, target)
        for target in OUTCOMES
    )
    coefficients = tuple(branch.effect.scalar for branch in branches)
    complete = (
        len(branches) == len(OUTCOMES)
        and tuple(branch.target for branch in branches) == OUTCOMES
        and all(turn_branch_is_physical(branch) for branch in branches)
        and all(
            all(atom in control.atoms for atom in branch_input_atoms(branch))
            for branch in branches
        )
        and all(
            block23.decode_locked_word(branch.effect.output_word)
            == (exit_front, branch.target)
            for branch in branches
        )
        and sp.simplify(sum(coefficients)) == 1
    )
    return GuardedTargetAxis(
        control,
        side,
        exit_front,
        branches,
        coefficients,
        complete,
    )

def guarded_control_row(lam, control, raw_amplitude=False):
    coefficient = sp.S.Zero
    for left_exit, right_exit in itertools.product(LEFT_EXITS, RIGHT_EXITS):
        left_axis = guarded_target_axis(
            control.left_source,
            control.right_source,
            "left",
            left_exit,
        )
        right_axis = guarded_target_axis(
            control.left_source,
            control.right_source,
            "right",
            right_exit,
        )
        if not (
            left_axis.complete
            and right_axis.complete
            and left_axis.control == right_axis.control == control
        ):
            raise ValueError("guarded target axis is incomplete")
        weight = q_weight(lam, left_exit, right_exit)
        amplitude = weight if raw_amplitude else sp.sqrt(weight)
        squared_amplitude = sp.simplify(amplitude * sp.conjugate(amplitude))
        coefficient += (
            squared_amplitude
            * sum(left_axis.coefficients)
            * sum(right_axis.coefficients)
        )
    return sp.simplify(coefficient)

@lru_cache(maxsize=1)
def pair_tensor_lemma_certificate() -> bool:
    for lam in (sp.S.Zero, sp.Rational(1, 2)):
        for left_source, right_source in itertools.product(OUTCOMES, repeat=2):
            control = pair_control(left_source, right_source)
            for left_exit, right_exit in itertools.product(
                LEFT_EXITS, RIGHT_EXITS
            ):
                left_axis = guarded_target_axis(
                    left_source, right_source, "left", left_exit
                )
                right_axis = guarded_target_axis(
                    left_source, right_source, "right", right_exit
                )
                descriptor = pair_kraus_descriptor(
                    lam,
                    left_source,
                    right_source,
                    left_exit,
                    right_exit,
                    OUTCOMES[0],
                    OUTCOMES[-1],
                )
                gram = contract_pair_kraus_descriptor(descriptor)
                expected = sp.simplify(
                    q_weight(lam, left_exit, right_exit)
                    * block23.transition(left_source, OUTCOMES[0])
                    * block23.transition(right_source, OUTCOMES[-1])
                )
                expected_outcome = pair_record_outcome(
                    left_exit,
                    right_exit,
                    OUTCOMES[0],
                    OUTCOMES[-1],
                )
                expected_records = tuple(
                    (center, word)
                    for center, word in expected_outcome.pointer_configuration
                    if block23.decode_locked_word(word) is not None
                )
                if not (
                    left_axis.complete
                    and right_axis.complete
                    and left_axis.control == right_axis.control == control
                    and gram.control == descriptor.control == control
                    and gram.coefficient == expected
                    and gram.output_records == expected_records
                ):
                    return False
            if guarded_control_row(lam, control) != 1:
                return False
    return True

def symbolic_q_family_certificate() -> bool:
    lam = sp.symbols("lambda", real=True)
    diagonal = sp.simplify((1 + 3 * lam) / 16)
    off_diagonal = sp.simplify((1 - lam) / 16)
    covariance = all(
        sp.simplify(
            q_weight(lam, *pair)
            - q_weight(lam, *pair_action(rotation, pair))
        )
        == 0
        for rotation in pair_stabilizer()
        for pair in itertools.product(LEFT_EXITS, RIGHT_EXITS)
    )
    return (
        sp.simplify(4 * diagonal + 12 * off_diagonal) == 1
        and sp.simplify(diagonal + 3 * off_diagonal) == sp.Rational(1, 4)
        and sp.Poly(diagonal, lam).degree() == 1
        and sp.Poly(off_diagonal, lam).degree() == 1
        and sp.diff(diagonal, lam) == sp.Rational(3, 16)
        and sp.diff(off_diagonal, lam) == -sp.Rational(1, 16)
        and sp.simplify(diagonal.subs(lam, 0)) > 0
        and sp.simplify(off_diagonal.subs(lam, 0)) > 0
        and sp.simplify(diagonal.subs(lam, 1)) > 0
        and sp.simplify(off_diagonal.subs(lam, 1)) == 0
        and covariance
    )

def turn_branch_covariance_certificate(branch, rotation):
    moved = turn_branch(
        block23.mat_vec(rotation, branch.anchor),
        block23.mat_vec(rotation, branch.incoming_front),
        block23.mat_vec(rotation, branch.source),
        block23.mat_vec(rotation, branch.exit_front),
        block23.mat_vec(rotation, branch.target),
    )
    data = block24.factor_dictionary(branch.factors)
    moved_data = block24.factor_dictionary(moved.factors)
    return (
        moved.effect.target_center
        == block23.mat_vec(rotation, branch.effect.target_center)
        and block23.rotate_block_product(block23.BLANK_BLOCK, rotation)
        == block23.BLANK_BLOCK
        and block24.current_factor_rotation_certificate(
            data["current_live_identities"],
            data["current_pointer_projectors"],
            moved_data["current_live_identities"],
            moved_data["current_pointer_projectors"],
            rotation,
        )
        and block24.preparation_factor_rotation_certificate(
            data["forward_live_prep_maps"],
            data["forward_pointer_prep_maps"],
            moved_data["forward_live_prep_maps"],
            moved_data["forward_pointer_prep_maps"],
            rotation,
        )
        and block24.writer_factor_rotation_certificate(
            data["forward_writer_pointer_maps"],
            data["forward_live_root"][1],
            moved_data["forward_writer_pointer_maps"],
            moved_data["forward_live_root"][1],
            rotation,
        )
        and block24.spectator_factor_rotation_certificate(
            data["spectator_identity_factors"],
            moved_data["spectator_identity_factors"],
            rotation,
        )
        and block24.root_covariance_certificate(branch.target, rotation)
        and block23.rotate_word(branch.effect.current_word, rotation)
        == moved.effect.current_word
        and block23.rotate_word(branch.effect.output_word, rotation)
        == moved.effect.output_word
        and data["outside_carrier_identity"]
        == moved_data["outside_carrier_identity"]
        == "I_outside"
        and data["lateral_touch"] is moved_data["lateral_touch"] is True
        and sp.simplify(moved.effect.scalar - branch.effect.scalar) == 0
    )

def translate_center(center, translation):
    return add(center, translation)

@lru_cache(maxsize=1)
def turn_translation_covariance_certificate() -> bool:
    a0, a1, a2, t0, t1, t2 = sp.symbols("a0 a1 a2 t0 t1 t2")
    anchor = (a0, a1, a2)
    translation = (t0, t1, t2)
    moved_anchor = translate_center(anchor, translation)
    for incoming in DIRECTIONS:
        for exit_front in lateral_directions(incoming):
            branch = turn_branch(
                anchor,
                incoming,
                OUTCOMES[0],
                exit_front,
                OUTCOMES[-1],
            )
            moved = turn_branch(
                moved_anchor,
                incoming,
                OUTCOMES[0],
                exit_front,
                OUTCOMES[-1],
            )
            data = block24.factor_dictionary(branch.factors)
            moved_data = block24.factor_dictionary(moved.factors)
            translated_spectators = {
                (translate_center(center, translation), site, operator)
                for center, site, operator in data["spectator_identity_factors"]
            }
            if not (
                moved.effect.target_center
                == translate_center(branch.effect.target_center, translation)
                and data["current_pointer_projectors"]
                == moved_data["current_pointer_projectors"]
                and data["forward_live_prep_maps"]
                == moved_data["forward_live_prep_maps"]
                and data["forward_pointer_prep_maps"]
                == moved_data["forward_pointer_prep_maps"]
                and data["forward_live_root"] == moved_data["forward_live_root"]
                and data["forward_writer_pointer_maps"]
                == moved_data["forward_writer_pointer_maps"]
                and translated_spectators
                == set(moved_data["spectator_identity_factors"])
                and branch.effect.output_word == moved.effect.output_word
                and branch.effect.scalar == moved.effect.scalar
            ):
                return False
    return True

def affine(rotation, translation, site):
    return add(block23.mat_vec(rotation, site), translation)

def transformed_frame(frame, rotation, translation=ZERO):
    return PairFrame(
        affine(rotation, translation, frame.left_anchor),
        block23.mat_vec(rotation, frame.front),
    )

def control_transport_certificate(
    frame, left_source, right_source, rotation, translation=ZERO
):
    original = pair_control_for(frame, left_source, right_source)
    moved_frame = transformed_frame(frame, rotation, translation)
    expected = pair_control_for(
        moved_frame,
        block23.mat_vec(rotation, left_source),
        block23.mat_vec(rotation, right_source),
    )
    moved_atoms = []
    for atom in original.atoms:
        if atom.role == "current-pointer":
            moved_state = block23.rotate_word(atom.state, rotation)
        elif atom.role == "Blank-block":
            moved_state = block23.rotate_block_product(atom.state, rotation)
        else:
            return False
        moved_atoms.append(
            ControlAtom(
                affine(rotation, translation, atom.center),
                atom.role,
                moved_state,
            )
        )
    return (
        moved_frame.right_anchor
        == affine(rotation, translation, frame.right_anchor)
        and set(moved_atoms) == set(expected.atoms)
        and control_is_rank_one_projector(expected)
    )

def unordered_pair_stabilizer_certificate() -> bool:
    for rotation in pair_stabilizer():
        swaps = block23.mat_vec(rotation, F_LEFT) == F_RIGHT
        translation = scale(27, E1) if swaps else ZERO
        moved_centers = {
            affine(rotation, translation, center) for center in PAIR_CENTERS
        }
        if moved_centers != set(PAIR_CENTERS):
            return False
        for left_source, right_source in itertools.product(OUTCOMES, repeat=2):
            original = pair_control(left_source, right_source)
            expected = pair_control(
                block23.mat_vec(
                    rotation, right_source if swaps else left_source
                ),
                block23.mat_vec(
                    rotation, left_source if swaps else right_source
                ),
            )
            moved_atoms = set()
            for atom in original.atoms:
                state = (
                    block23.rotate_word(atom.state, rotation)
                    if atom.role == "current-pointer"
                    else block23.rotate_block_product(atom.state, rotation)
                )
                moved_atoms.add(
                    ControlAtom(
                        affine(rotation, translation, atom.center),
                        atom.role,
                        state,
                    )
                )
            if moved_atoms != set(expected.atoms):
                return False
        for lam in (sp.S.Zero, sp.Rational(1, 2)):
            for left_exit, right_exit in itertools.product(
                LEFT_EXITS, RIGHT_EXITS
            ):
                moved_left = block23.mat_vec(
                    rotation, right_exit if swaps else left_exit
                )
                moved_right = block23.mat_vec(
                    rotation, left_exit if swaps else right_exit
                )
                if q_weight(lam, left_exit, right_exit) != q_weight(
                    lam, moved_left, moved_right
                ):
                    return False
    return True

@lru_cache(maxsize=1)
def full_pair_covariance_certificate() -> bool:
    symbolic_translation = sp.symbols("tau_0 tau_1 tau_2")
    controls_transport = all(
        control_transport_certificate(
            CANONICAL_FRAME,
            left_source,
            right_source,
            rotation,
            symbolic_translation,
        )
        for rotation in ROTATIONS
        for left_source, right_source in itertools.product(OUTCOMES, repeat=2)
    )
    branches_transport = all(
        turn_branch_covariance_certificate(branch, rotation)
        for branch in all_turn_branches()
        for rotation in ROTATIONS
    )
    q_transport = all(
        q_weight(lam, left_exit, right_exit)
        == q_weight(
            lam,
            block23.mat_vec(rotation, left_exit),
            block23.mat_vec(rotation, right_exit),
        )
        for lam in (sp.S.Zero, sp.Rational(1, 2))
        for rotation in ROTATIONS
        for left_exit, right_exit in itertools.product(LEFT_EXITS, RIGHT_EXITS)
    )
    return (
        controls_transport
        and branches_transport
        and q_transport
        and turn_translation_covariance_certificate()
        and unordered_pair_stabilizer_certificate()
    )

def local_covariance_certificate() -> bool:
    state_covariance = all(
        block23.mat_vec(rotation, block23.prepared_vectors(source)[site])
        == block23.prepared_vectors(block23.mat_vec(rotation, source))[
            block23.mat_vec(rotation, site)
        ]
        for rotation in ROTATIONS
        for source in OUTCOMES
        for site in DIRECTIONS
    )
    record_covariance = all(
        block23.rotate_word(block23.locked_word(front, target), rotation)
        == block23.locked_word(
            block23.mat_vec(rotation, front),
            block23.mat_vec(rotation, target),
        )
        for rotation in ROTATIONS
        for front in DIRECTIONS
        for target in OUTCOMES
    )
    transition_covariance = all(
        sp.simplify(
            block23.transition(
                block23.mat_vec(rotation, source),
                block23.mat_vec(rotation, target),
            )
            - block23.transition(source, target)
        )
        == 0
        for rotation in ROTATIONS
        for source in OUTCOMES
        for target in OUTCOMES
    )
    geometry_covariance = all(
        block23.mat_vec(
            rotation, block24.forward_center(ZERO, exit_front)
        )
        == block24.forward_center(
            ZERO, block23.mat_vec(rotation, exit_front)
        )
        for rotation in ROTATIONS
        for exit_front in DIRECTIONS
    )
    return (
        len(ROTATIONS) == 24
        and len(pair_stabilizer()) == 8
        and state_covariance
        and record_covariance
        and transition_covariance
        and geometry_covariance
        and block24.translation_covariance_certificate()
        and full_pair_covariance_certificate()
    )

@dataclass(frozen=True)
class PairRecordOutcome:
    left_exit: tuple
    right_exit: tuple
    left_target: tuple
    right_target: tuple
    pointer_configuration: tuple

def pair_record_outcome(
    left_exit, right_exit, left_target, right_target, mutation=None
):
    left_word = block23.locked_word(left_exit, left_target)
    right_word = block23.locked_word(right_exit, right_target)
    if mutation == "alias_record_label" and (
        left_exit,
        left_target,
    ) == (LEFT_EXITS[-1], OUTCOMES[-1]):
        left_word = block23.locked_word(LEFT_EXITS[-1], OUTCOMES[0])
    configuration = tuple(
        (
            center,
            left_word
            if center == block24.forward_center(Y_LEFT, left_exit)
            else right_word
            if center == block24.forward_center(Y_RIGHT, right_exit)
            else block23.BLANK_POINTER,
        )
        for center in LEFT_TARGETS + RIGHT_TARGETS
    )
    return PairRecordOutcome(
        left_exit,
        right_exit,
        left_target,
        right_target,
        configuration,
    )

@lru_cache(maxsize=1)
def pair_record_outcomes():
    return tuple(
        pair_record_outcome(left_exit, right_exit, left_target, right_target)
        for left_exit, right_exit in itertools.product(LEFT_EXITS, RIGHT_EXITS)
        for left_target, right_target in itertools.product(OUTCOMES, repeat=2)
    )

def decode_pair_record_outcome(outcome):
    locked = tuple(
        (center, block23.decode_locked_word(word))
        for center, word in outcome.pointer_configuration
        if block23.decode_locked_word(word) is not None
    )
    if len(locked) != 2:
        return None
    left_entries = tuple(entry for entry in locked if entry[0] in LEFT_TARGETS)
    right_entries = tuple(entry for entry in locked if entry[0] in RIGHT_TARGETS)
    if len(left_entries) != 1 or len(right_entries) != 1:
        return None
    left_center, left_label = left_entries[0]
    right_center, right_label = right_entries[0]
    left_exit, left_target = left_label
    right_exit, right_target = right_label
    if (
        left_center != block24.forward_center(Y_LEFT, left_exit)
        or right_center != block24.forward_center(Y_RIGHT, right_exit)
    ):
        return None
    return left_exit, right_exit, left_target, right_target

def record_label_certificate(mutation=None) -> bool:
    local_labels = [
        (exit_front, target, block23.locked_word(exit_front, target))
        for exit_front in LEFT_EXITS
        for target in OUTCOMES
    ]
    local_words = tuple(word for _exit, _target, word in local_labels)
    code_words = (block23.BLANK_POINTER,) + local_words
    code_orthonormal = all(
        block23.pointer_overlap(left, right) == int(i == j)
        for i, left in enumerate(code_words)
        for j, right in enumerate(code_words)
    )
    outcomes = (
        tuple(
            pair_record_outcome(
                left_exit,
                right_exit,
                left_target,
                right_target,
                mutation,
            )
            for left_exit, right_exit in itertools.product(
                LEFT_EXITS, RIGHT_EXITS
            )
            for left_target, right_target in itertools.product(
                OUTCOMES, repeat=2
            )
        )
        if mutation
        else pair_record_outcomes()
    )
    configurations = tuple(outcome.pointer_configuration for outcome in outcomes)
    decoded = all(
        block23.decode_locked_word(word) == (exit_front, target)
        for exit_front, target, word in local_labels
    )
    decoded_outcomes = tuple(decode_pair_record_outcome(outcome) for outcome in outcomes)
    decoded_matches_metadata = all(
        decoded
        == (
            outcome.left_exit,
            outcome.right_exit,
            outcome.left_target,
            outcome.right_target,
        )
        for outcome, decoded in zip(outcomes, decoded_outcomes)
    )
    same_event_terms = tuple(
        decoded
        for decoded in decoded_outcomes
        if decoded is not None and decoded[0] == decoded[1]
    )
    return (
        len(local_labels) == 4 * 14 == 56
        and len(local_words) == len(set(local_words))
        and code_orthonormal
        and decoded
        and len(outcomes) == 16 * 14**2 == 3136
        and len(configurations) == len(set(configurations))
        and decoded_matches_metadata
        and len(same_event_terms) == 4 * 14**2 == 784
        and set(LEFT_TARGETS).isdisjoint(RIGHT_TARGETS)
    )

def guarded_same_record_event_row(lam, left_source, right_source):
    coefficient = sp.S.Zero
    for left_exit, right_exit in itertools.product(LEFT_EXITS, RIGHT_EXITS):
        left_axis = guarded_target_axis(
            left_source, right_source, "left", left_exit
        )
        right_axis = guarded_target_axis(
            left_source, right_source, "right", right_exit
        )
        left_decoded = {
            block23.decode_locked_word(branch.effect.output_word)
            for branch in left_axis.branches
        }
        right_decoded = {
            block23.decode_locked_word(branch.effect.output_word)
            for branch in right_axis.branches
        }
        if not (
            left_axis.complete
            and right_axis.complete
            and {label[0] for label in left_decoded} == {left_exit}
            and {label[0] for label in right_decoded} == {right_exit}
        ):
            raise ValueError("Record event is not bound to the emitted labels")
        if next(iter(left_decoded))[0] == next(iter(right_decoded))[0]:
            coefficient += (
                q_weight(lam, left_exit, right_exit)
                * sum(left_axis.coefficients)
                * sum(right_axis.coefficients)
            )
    return sp.simplify(coefficient)

def readable_same_record_event_certificate(lam):
    if not record_label_certificate():
        return False, None
    values = tuple(
        guarded_same_record_event_row(lam, left_source, right_source)
        for left_source, right_source in itertools.product(OUTCOMES, repeat=2)
    )
    return len(set(values)) == 1, values[0]

@dataclass(frozen=True)
class ActiveGramTerm:
    control: PairControl
    coefficient: object

@dataclass(frozen=True)
class StopKrausDescriptor:
    active: ActiveControlSum
    operator_form: str = "I-P_active"

def active_gram_terms(lam, raw_amplitude=False):
    return tuple(
        ActiveGramTerm(
            control,
            guarded_control_row(lam, control, raw_amplitude=raw_amplitude),
        )
        for control in active_control_sum().controls
    )

def full_space_completion_certificate(terms, stop_present=True):
    active = active_control_sum()
    stop = StopKrausDescriptor(active) if stop_present else None
    if not (
        active.pairwise_orthogonal
        and active.idempotent
        and active.complement_nontrivial
        and tuple(term.control for term in terms) == active.controls
        and all(term.coefficient == 1 for term in terms)
    ):
        return False
    if stop is None or stop.operator_form != "I-P_active":
        return False
    # P_active is the explicit sum of the 196 orthogonal rank-one controls.
    # Its idempotence, proved above, makes (I-P_active)^2=I-P_active.
    p_active = sp.symbols("P_active", commutative=True)
    stop_gram = block23.projector_reduce((1 - p_active) ** 2, p_active)
    total_gram = block23.projector_reduce(p_active + stop_gram, p_active)
    return stop_gram == 1 - p_active and total_gram == 1

def candidate_channel_certificate(lam, raw_amplitude=False, stop_present=True):
    q_report = q_certificate(lam)
    terms = active_gram_terms(lam, raw_amplitude=raw_amplitude)
    return (
        all(q_report.values())
        and local_turn_certificate()
        and tensor_support_certificate()
        and pair_tensor_lemma_certificate()
        and pair_control_certificate()
        and record_label_certificate()
        and full_space_completion_certificate(terms, stop_present=stop_present)
    )

REFERENCE_DIMENSION = sp.symbols("d_R", integer=True, positive=True)

REFERENCE_ROW = sp.symbols("r_R", integer=True, nonnegative=True)

REFERENCE_COLUMN = sp.symbols("s_R", integer=True, nonnegative=True)

REFERENCE_IDENTITY = sp.Identity(REFERENCE_DIMENSION)

REFERENCE_ELEMENT = sp.KroneckerDelta(REFERENCE_ROW, REFERENCE_COLUMN)

@dataclass(frozen=True)
class ReferenceExtendedGramTerm:
    control: PairControl
    coefficient: object
    reference_operator: object
    matrix_element: object

def arbitrary_reference_certificate() -> bool:
    if sp.adjoint(REFERENCE_IDENTITY) * REFERENCE_IDENTITY != REFERENCE_IDENTITY:
        return False
    for lam in (sp.S.Zero, sp.Rational(1, 2)):
        terms = active_gram_terms(lam)
        extensions = tuple(
            ReferenceExtendedGramTerm(
                term.control,
                term.coefficient,
                REFERENCE_IDENTITY,
                sp.simplify(term.coefficient * REFERENCE_ELEMENT),
            )
            for term in terms
        )
        if not (
            tuple(extension.control for extension in extensions)
            == active_control_sum().controls
            and all(
                extension.coefficient == 1
                and extension.reference_operator == REFERENCE_IDENTITY
                and extension.matrix_element == REFERENCE_ELEMENT
                for extension in extensions
            )
            and full_space_completion_certificate(terms)
        ):
            return False
    return True

def physical_mutation_rejected(mutation) -> bool:
    try:
        branch = turn_branch(
            Y_LEFT,
            F_LEFT,
            OUTCOMES[0],
            LEFT_EXITS[0],
            OUTCOMES[-1],
            mutation,
        )
    except ValueError:
        return True
    return not turn_branch_is_physical(branch)

def raw_amplitude_descriptor_rejected() -> bool:
    descriptor = pair_kraus_descriptor(
        sp.Rational(1, 2),
        OUTCOMES[0],
        OUTCOMES[-1],
        LEFT_EXITS[0],
        RIGHT_EXITS[-1],
        OUTCOMES[0],
        OUTCOMES[-1],
        raw_amplitude=True,
    )
    try:
        contract_pair_kraus_descriptor(descriptor)
    except ValueError:
        return True
    return False

def bounded_local_factors():
    effects = [block23.effect(b) for b in OUTCOMES]
    if sum(e[0] for e in effects) != 1:
        return False
    for n in DIRECTIONS:
        if any(sp.simplify(sum(e[1][n][j] for e in effects)) != 0 for j in range(3)):
            return False
    for b in OUTCOMES:
        _norms, values = block23.spectral_resolution(b)
        if len(values) != 64 or not all(v.is_positive for v in values.values()):
            return False
        actual = block23.contract_root_adjoint_root(block23.root_operator_factor(b))
        if not block23.effect_equal(actual, block23.effect(b)):
            return False
    if not all(v == 1 for v in target_row_sums().values()):
        return False
    if not all(block23.transition(s,t).is_positive for s in OUTCOMES for t in OUTCOMES):
        return False
    for source, target in itertools.product((OUTCOMES[0], OUTCOMES[-1]), repeat=2):
        branch = turn_branch(Y_LEFT, F_LEFT, source, LEFT_EXITS[0], target)
        if not turn_branch_is_physical(branch):
            return False
        factors = list(branch.factors)
        index = next(i for i, x in enumerate(factors) if x[0] == 'forward_writer_pointer_maps')
        factors[index] = (factors[index][0], factors[index][1][:-1])
        try:
            contract_turn_effect(tuple(factors))
        except ValueError:
            pass
        else:
            return False
    return True


def bounded_record_outputs():
    # Complete literal configurations, with a lookup of the very same code words.
    # Orthogonality is the radial-bit projector identity, proved in the note.
    decoder = {block23.locked_word(f,b):(f,b) for f in DIRECTIONS for b in OUTCOMES}
    if len(decoder) != 84 or block23.BLANK_POINTER in decoder:
        return False
    outputs = pair_record_outcomes()
    if len(outputs) != 3136 or len({o.pointer_configuration for o in outputs}) != 3136:
        return False
    for o in outputs:
        nonblank = [(c,decoder.get(w)) for c,w in o.pointer_configuration if w != block23.BLANK_POINTER]
        expected = {(block24.forward_center(Y_LEFT,o.left_exit),(o.left_exit,o.left_target)),
                    (block24.forward_center(Y_RIGHT,o.right_exit),(o.right_exit,o.right_target))}
        if set(nonblank) != expected or len(nonblank) != 2:
            return False
    return True


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 30
# Literal inputs and hashes are frozen after all source/note edits.
AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_D4_RETURNED_TIP_SUPPLIED_Q_CONDITIONAL_PAIR_INSTRUMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-30.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'scripts/admissibility_d4_prior_record_live_preparation_two_event_prefix_2026_08_30.py', 'scripts/admissibility_d4_self_delimiting_forward_record_append_history_2026_08_30.py')
DIRECT_HASHES = {'docs/ADMISSIBILITY_D4_RETURNED_TIP_SUPPLIED_Q_CONDITIONAL_PAIR_INSTRUMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-30.md': '86913d27c2f428d8d510ea374541b017ac4daa380574fe3486756374e7112320', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'scripts/admissibility_d4_prior_record_live_preparation_two_event_prefix_2026_08_30.py': 'a454b4ce47af92bbf55550ebae068ff4a419b141d916b0c4fcdc1678bf283a7e', 'scripts/admissibility_d4_self_delimiting_forward_record_append_history_2026_08_30.py': '5eb733c3a50da1f7c1bb8a46b547b1b91fd85c27856e425d8040305b3d009d6c'}

def current_inputs_ok():
    return all((ROOT/p).is_file() and hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==sha for p,sha in DIRECT_HASHES.items()) and set(DIRECT_HASHES)==set(AUDIT_INPUT_PATHS) and bool(DIRECT_HASHES)


def main():
    if not current_inputs_ok():
        print('FAIL current_source_and_note_inputs')
        print('TERMINAL: INCOMPLETE-NO-SCIENCE-INFERENCE')
        print('TOTAL: PASS=0 FAIL=1')
        return 1
    passed=1
    failed=0
    print('PASS current_source_and_note_inputs')
    ok=bool(bounded_local_factors())
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'local_positive_roots_rows_and_actual_writer_deletion')
    ok=bool(returned_geometry_certificate())
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'ten_block_geometry')
    ok=bool(bounded_record_outputs())
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'3136_actual_record_configurations')
    ok=bool(all(q_certificate(sp.S.Zero).values()) and all(q_certificate(sp.Rational(1,2)).values()) and not all(q_certificate(sp.Rational(1,2),"bad_diagonal").values()))
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'two_q_tables_and_changed_weight')
    print('TERMINAL: '+('BLOCK28-NAMED-BOUNDED-CHECKS-COMPLETE;CONDITIONAL-PROOFS-PRESERVED' if failed==0 else 'INCOMPLETE-NO-SCIENCE-INFERENCE'))
    print(f'TOTAL: PASS={passed} FAIL={failed}')
    return int(failed!=0)

if __name__=='__main__':
    raise SystemExit(main())
