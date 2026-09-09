#!/usr/bin/env python3

"""Block30: conditional mathematics with a bounded current entrypoint.
Complete historical sources/controllers and results are archived outside note discovery.
Only the named checks below are fresh execution claims.
"""

from __future__ import annotations

import hashlib

import itertools

import sys

from dataclasses import dataclass, replace

from functools import lru_cache

from pathlib import Path

import sympy as sp

import admissibility_d4_prior_record_live_preparation_two_event_prefix_2026_08_30 as block23  # noqa: E402

import admissibility_d4_self_delimiting_forward_record_append_history_2026_08_30 as block24  # noqa: E402

import admissibility_d4_returned_tip_strict_support_analytic_coupling_gate_2026_08_30 as block28  # noqa: E402

ZERO = (0, 0, 0)

E1 = (1, 0, 0)

E2 = (0, 1, 0)

DIRECTIONS = block23.DIRECTIONS

OUTCOMES = block23.OUTCOMES

ROTATIONS = block23.ROTATIONS

LAMBDAS = (sp.S.Zero, sp.Rational(1, 2))

def add(left, right):
    return block23.add(left, right)

def negate(vector):
    return block23.negate(vector)

def scale(number, vector):
    return block23.scale(number, vector)

def dot(left, right):
    return block23.dot(left, right)

def cross(left, right):
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )

def translate(vector, shift):
    return add(vector, shift)

def orbit_kind(g, h):
    if g == h:
        return "equal"
    if h == negate(g):
        return "opposite"
    if dot(g, h) == 0:
        return "orthogonal"
    raise ValueError("lateral exits do not belong to a pair orbit")

def route_words(f, g, h, chirality=1, mutation=None):
    """Derive route words from the three invariant pair relations."""
    if chirality not in (-1, 1):
        raise ValueError("chirality must be one fixed sign")
    kind = orbit_kind(g, h)
    effective_sign = chirality
    if mutation == "coordinate_mark" and kind == "opposite" and g == E2:
        effective_sign = -effective_sign
    if mutation == "legacy_four_step":
        if kind == "equal":
            return (negate(f), g, g, f), (f, h, h, negate(f)), kind
        if kind == "orthogonal":
            return (f, f, h, negate(f)), (negate(f), negate(f), g, f), kind
        k = scale(effective_sign, cross(f, g))
        return (negate(f), k, h, f), (f, k, g, negate(f)), kind
    if kind == "equal":
        left = (negate(f), g, g, g, f)
        right = (f, h, h, h, negate(f))
    elif kind == "orthogonal":
        left = (negate(f), g, h, h, f)
        right = (f, h, g, g, negate(f))
    else:
        k = scale(effective_sign, cross(f, g))
        left = (negate(f), k, h, k, f)
        right = (f, k, g, k, negate(f))

    if mutation == "immediate_reverse":
        left = (negate(g),) + left[1:]
    elif mutation == "delete_step":
        left = left[:-1]
    elif mutation == "bad_facing":
        left = left[:-1] + (g,)
    elif mutation == "revisit_center":
        left = (negate(f), f) + left[2:]
    elif mutation == "old_target":
        left = (negate(g),) + left[1:]
    return left, right, kind

@dataclass(frozen=True)
class Walk:
    start: tuple
    initial_front: tuple
    steps: tuple
    targets: tuple
    final_front: tuple
    legal: bool

def walk(start, initial_front, steps):
    current = start
    front = initial_front
    targets = []
    legal = True
    for direction in steps:
        legal &= direction in DIRECTIONS and (
            direction == front or dot(direction, front) == 0
        )
        current = block24.forward_center(current, direction)
        targets.append(current)
        front = direction
    return Walk(start, initial_front, tuple(steps), tuple(targets), front, legal)

@dataclass(frozen=True)
class RoutePlan:
    left_anchor: tuple
    front: tuple
    g: tuple
    h: tuple
    chirality: int
    kind: str
    old_centers: tuple
    left: Walk
    right: Walk

def route_plan(left_anchor, f, g, h, chirality=1, mutation=None):
    if f not in DIRECTIONS or g not in DIRECTIONS or h not in DIRECTIONS:
        raise ValueError("fronts must be cubic unit directions")
    if dot(f, g) != 0 or dot(f, h) != 0:
        raise ValueError("outputs must be lateral to the pair front")
    old_right = block24.forward_center(left_anchor, f)
    left_start = block24.forward_center(left_anchor, g)
    right_start = block24.forward_center(old_right, h)
    if mutation == "shared_start":
        right_start = left_start
    left_words, right_words, kind = route_words(
        f, g, h, chirality, mutation=mutation
    )
    old_centers = (
        block24.forward_center(left_anchor, negate(f)),
        left_anchor,
        old_right,
        block24.forward_center(old_right, f),
        left_start,
        right_start,
    )
    return RoutePlan(
        left_anchor,
        f,
        g,
        h,
        chirality,
        kind,
        old_centers,
        walk(left_start, g, left_words),
        walk(right_start, h, right_words),
    )

def block_sites(center):
    return frozenset(block23.translate(block23.SUPPORT, center))

def returned_facing(left: Walk, right: Walk) -> bool:
    if not left.targets or not right.targets:
        return False
    left_end = left.targets[-1]
    right_end = right.targets[-1]
    return (
        block24.forward_center(left_end, left.final_front) == right_end
        and right.final_front == negate(left.final_front)
    ) or (
        block24.forward_center(right_end, right.final_front) == left_end
        and left.final_front == negate(right.final_front)
    )

def successor_frame(plan: RoutePlan):
    if not plan.left.targets or not plan.right.targets:
        return None
    left_end = plan.left.targets[-1]
    right_end = plan.right.targets[-1]
    if (
        block24.forward_center(left_end, plan.left.final_front) == right_end
        and plan.right.final_front == negate(plan.left.final_front)
    ):
        return block28.PairFrame(left_end, plan.left.final_front)
    if (
        block24.forward_center(right_end, plan.right.final_front) == left_end
        and plan.left.final_front == negate(plan.right.final_front)
    ):
        return block28.PairFrame(right_end, plan.right.final_front)
    return None

def successor_blank_centers(plan: RoutePlan):
    frame = successor_frame(plan)
    if frame is None:
        return ()
    return frame.left_targets + frame.right_targets

def route_plan_certificate(plan: RoutePlan) -> bool:
    left_targets = plan.left.targets
    right_targets = plan.right.targets
    all_targets = left_targets + right_targets
    target_blocks = tuple(block_sites(center) for center in all_targets)
    old_blocks = tuple(block_sites(center) for center in plan.old_centers)
    future_centers = successor_blank_centers(plan)
    future_blocks = tuple(block_sites(center) for center in future_centers)
    occupied_blocks = old_blocks + target_blocks
    return (
        len(plan.left.steps) == len(plan.right.steps) == 5
        and plan.left.legal
        and plan.right.legal
        and len(all_targets) == len(set(all_targets)) == 10
        and all(
            left.isdisjoint(right)
            for left, right in itertools.combinations(target_blocks, 2)
        )
        and all(
            target.isdisjoint(old)
            for target in target_blocks
            for old in old_blocks
        )
        and returned_facing(plan.left, plan.right)
        and len(future_centers) == len(set(future_centers)) == 8
        and all(
            left.isdisjoint(right)
            for left, right in itertools.combinations(future_blocks, 2)
        )
        and all(
            future.isdisjoint(occupied)
            for future in future_blocks
            for occupied in occupied_blocks
        )
    )

def all_plans(mutation=None):
    plans = []
    for f in DIRECTIONS:
        lateral = tuple(direction for direction in DIRECTIONS if dot(f, direction) == 0)
        for g, h in itertools.product(lateral, repeat=2):
            for chirality in (-1, 1):
                plans.append(route_plan(ZERO, f, g, h, chirality, mutation))
    return tuple(plans)

def geometry_certificate(mutation=None) -> bool:
    plans = all_plans(mutation)
    return len(plans) == 192 and all(route_plan_certificate(plan) for plan in plans)

def successor_clearance_only(plan: RoutePlan) -> bool:
    future_centers = successor_blank_centers(plan)
    future_blocks = tuple(block_sites(center) for center in future_centers)
    occupied_blocks = tuple(
        block_sites(center)
        for center in plan.old_centers + plan.left.targets + plan.right.targets
    )
    return (
        returned_facing(plan.left, plan.right)
        and len(future_centers) == len(set(future_centers)) == 8
        and all(
            left.isdisjoint(right)
            for left, right in itertools.combinations(future_blocks, 2)
        )
        and all(
            future.isdisjoint(occupied)
            for future in future_blocks
            for occupied in occupied_blocks
        )
    )

def legacy_four_step_clearance_profile():
    profile = {}
    for chirality in (-1, 1):
        counts = {"equal": 0, "opposite": 0, "orthogonal": 0}
        for f in DIRECTIONS:
            lateral = tuple(
                direction for direction in DIRECTIONS if dot(f, direction) == 0
            )
            for g, h in itertools.product(lateral, repeat=2):
                plan = route_plan(
                    ZERO, f, g, h, chirality, "legacy_four_step"
                )
                if successor_clearance_only(plan):
                    counts[plan.kind] += 1
        profile[chirality] = counts
    return profile

def rotate_walk(walk_data: Walk, rotation):
    return Walk(
        block23.mat_vec(rotation, walk_data.start),
        block23.mat_vec(rotation, walk_data.initial_front),
        tuple(block23.mat_vec(rotation, step) for step in walk_data.steps),
        tuple(block23.mat_vec(rotation, target) for target in walk_data.targets),
        block23.mat_vec(rotation, walk_data.final_front),
        walk_data.legal,
    )

def covariance_certificate(mutation=None) -> bool:
    translation = (5, -7, 11)
    for f in DIRECTIONS:
        lateral = tuple(direction for direction in DIRECTIONS if dot(f, direction) == 0)
        for g, h in itertools.product(lateral, repeat=2):
            for chirality in (-1, 1):
                plan = route_plan(ZERO, f, g, h, chirality, mutation)
                moved = route_plan(translation, f, g, h, chirality, mutation)
                if (
                    moved.left.steps != plan.left.steps
                    or moved.right.steps != plan.right.steps
                    or moved.left.targets
                    != tuple(translate(center, translation) for center in plan.left.targets)
                    or moved.right.targets
                    != tuple(translate(center, translation) for center in plan.right.targets)
                ):
                    return False
                swapped = route_plan(
                    block24.forward_center(ZERO, f),
                    negate(f),
                    h,
                    g,
                    chirality,
                    mutation,
                )
                if (
                    swapped.left.steps != plan.right.steps
                    or swapped.right.steps != plan.left.steps
                    or swapped.left.targets != plan.right.targets
                    or swapped.right.targets != plan.left.targets
                ):
                    return False
                for rotation in ROTATIONS:
                    rotated = route_plan(
                        ZERO,
                        block23.mat_vec(rotation, f),
                        block23.mat_vec(rotation, g),
                        block23.mat_vec(rotation, h),
                        chirality,
                        mutation,
                    )
                    if (
                        rotated.left != rotate_walk(plan.left, rotation)
                        or rotated.right != rotate_walk(plan.right, rotation)
                    ):
                        return False
    return True

def displayed_multiplicity_certificate(mutation=None) -> bool:
    f = E1
    lateral = tuple(direction for direction in DIRECTIONS if dot(f, direction) == 0)
    counts = {"equal": 0, "opposite": 0, "orthogonal": 0}
    distinct_opposite = 0
    coincident_other = 0
    for g, h in itertools.product(lateral, repeat=2):
        kind = orbit_kind(g, h)
        counts[kind] += 1
        plus = route_plan(ZERO, f, g, h, 1)
        minus = route_plan(ZERO, f, g, h, -1)
        if mutation == "collapse_chirality" and kind == "opposite":
            minus = plus
        signatures_equal = (
            plus.left.steps,
            plus.right.steps,
            plus.left.targets,
            plus.right.targets,
        ) == (
            minus.left.steps,
            minus.right.steps,
            minus.left.targets,
            minus.right.targets,
        )
        if kind == "opposite" and not signatures_equal:
            distinct_opposite += 1
        if kind != "opposite" and signatures_equal:
            coincident_other += 1
    return (
        counts == {"equal": 4, "opposite": 4, "orthogonal": 8}
        and distinct_opposite == 4
        and coincident_other == 12
    )

def candidate_carrier_centers(left_anchor, f, chirality):
    lateral = tuple(direction for direction in DIRECTIONS if dot(f, direction) == 0)
    centers = set()
    for g, h in itertools.product(lateral, repeat=2):
        plan = route_plan(left_anchor, f, g, h, chirality)
        centers.update((plan.left.start, plan.right.start))
        centers.update(plan.left.targets)
        centers.update(plan.right.targets)
        centers.update(successor_blank_centers(plan))
    return frozenset(centers)

def common_carrier_certificate(mutation=None) -> bool:
    translation = (5, -7, 11)
    for f in DIRECTIONS:
        minus = candidate_carrier_centers(ZERO, f, -1)
        plus = candidate_carrier_centers(ZERO, f, 1)
        if mutation == "selected_only_carrier":
            sample = route_plan(
                ZERO,
                f,
                tuple(direction for direction in DIRECTIONS if dot(f, direction) == 0)[0],
                tuple(direction for direction in DIRECTIONS if dot(f, direction) == 0)[0],
                1,
            )
            plus = frozenset(
                (sample.left.start, sample.right.start)
                + sample.left.targets
                + sample.right.targets
                + successor_blank_centers(sample)
            )
        if len(minus) != len(plus) or minus != plus or len(plus) != 160:
            return False
        blocks = tuple(block_sites(center) for center in plus)
        if not all(
            left.isdisjoint(right)
            for left, right in itertools.combinations(blocks, 2)
        ):
            return False
        old_centers = (
            block24.forward_center(ZERO, negate(f)),
            ZERO,
            block24.forward_center(ZERO, f),
            block24.forward_center(block24.forward_center(ZERO, f), f),
        )
        if any(
            block_sites(center).intersection(block_sites(old))
            for center in plus
            for old in old_centers
        ):
            return False
        moved = candidate_carrier_centers(translation, f, 1)
        if moved != frozenset(translate(center, translation) for center in plus):
            return False
        for rotation in ROTATIONS:
            rotated = candidate_carrier_centers(
                ZERO, block23.mat_vec(rotation, f), 1
            )
            if rotated != frozenset(
                block23.mat_vec(rotation, center) for center in plus
            ):
                return False
        lateral = tuple(direction for direction in DIRECTIONS if dot(f, direction) == 0)
        for chirality in (-1, 1):
            carrier = candidate_carrier_centers(ZERO, f, chirality)
            for g, h in itertools.product(lateral, repeat=2):
                plan = route_plan(ZERO, f, g, h, chirality)
                locked = {plan.left.start, plan.right.start}
                initial_blank = carrier - locked
                written = set(plan.left.targets + plan.right.targets)
                remaining_blank = initial_blank - written
                if not (
                    route_plan_certificate(plan)
                    and len(locked) == 2
                    and len(initial_blank) == 158
                    and len(written) == 10
                    and written.issubset(initial_blank)
                    and len(remaining_blank) == 148
                    and set(successor_blank_centers(plan)).issubset(
                        remaining_blank
                    )
                ):
                    return False
    return True

@dataclass(frozen=True)
class HandoffControl:
    chirality: int
    left_source: tuple
    right_source: tuple
    pointer_configuration: tuple
    carrier_centers: tuple
    blank_centers: tuple
    plan: RoutePlan

@lru_cache(maxsize=2)
def handoff_controls(chirality):
    carrier = candidate_carrier_centers(block28.Y_LEFT, E1, chirality)
    controls = []
    for outcome in block28.pair_record_outcomes():
        decoded = block28.decode_pair_record_outcome(outcome)
        if decoded is None:
            raise ValueError("Block28 output Record failed to decode")
        g, h, left_source, right_source = decoded
        plan = route_plan(block28.Y_LEFT, E1, g, h, chirality)
        locked = {plan.left.start, plan.right.start}
        controls.append(
            HandoffControl(
                chirality,
                left_source,
                right_source,
                outcome.pointer_configuration,
                tuple(sorted(carrier)),
                tuple(sorted(carrier - locked)),
                plan,
            )
        )
    return tuple(controls)

def local_pointer_code_certificate() -> bool:
    words = (block23.BLANK_POINTER,) + tuple(
        block23.locked_word(front, outcome)
        for front in DIRECTIONS
        for outcome in OUTCOMES
    )
    one_site_binary_orthogonality = all(
        block23.pure_overlap(
            block23.radial_bloch(site, left_bit),
            block23.radial_bloch(site, right_bit),
        )
        == int(left_bit == right_bit)
        for site in block23.POINTER_ORDER
        for left_bit, right_bit in itertools.product((0, 1), repeat=2)
    )
    return len(words) == len(set(words)) == 85 and one_site_binary_orthogonality

def handoff_control_is_physical(control: HandoffControl) -> bool:
    configuration = dict(control.pointer_configuration)
    locked = tuple(
        (center, block23.decode_locked_word(word))
        for center, word in control.pointer_configuration
        if block23.decode_locked_word(word) is not None
    )
    expected_locked = {
        (control.plan.left.start, (control.plan.g, control.left_source)),
        (control.plan.right.start, (control.plan.h, control.right_source)),
    }
    carrier = set(control.carrier_centers)
    blank = set(control.blank_centers)
    written = set(control.plan.left.targets + control.plan.right.targets)
    remaining = blank - written
    return (
        len(configuration) == 8
        and set(configuration).issubset(carrier)
        and set(locked) == expected_locked
        and all(
            word == block23.BLANK_POINTER
            for center, word in control.pointer_configuration
            if center not in {control.plan.left.start, control.plan.right.start}
        )
        and blank
        == carrier - {control.plan.left.start, control.plan.right.start}
        and len(blank) == 158
        and written.issubset(blank)
        and len(remaining) == 148
        and set(successor_blank_centers(control.plan)).issubset(remaining)
    )

def handoff_control_channel_certificate(stop_present=True, mutation=None) -> bool:
    if not local_pointer_code_certificate():
        return False
    plus = handoff_controls(1)
    minus = handoff_controls(-1)
    if mutation == "alias_control":
        plus = plus[:-1] + (replace(plus[-1], pointer_configuration=plus[0].pointer_configuration),)
    configurations = tuple(control.pointer_configuration for control in plus)
    carrier_signatures = {control.carrier_centers for control in plus + minus}
    unique_plans = {control.plan for control in plus + minus}
    common_carrier = set(next(iter(carrier_signatures)))
    complete = (
        len(plus) == len(minus) == 3136
        and len(configurations) == len(set(configurations))
        and tuple(control.pointer_configuration for control in plus)
        == tuple(control.pointer_configuration for control in minus)
        and len(carrier_signatures) == 1
        and all(handoff_control_is_physical(control) for control in plus + minus)
        and len(unique_plans) == 32
        and all(route_plan_certificate(plan) for plan in unique_plans)
        and all(
            set(plan.left.targets + plan.right.targets).issubset(
                common_carrier - {plan.left.start, plan.right.start}
            )
            for plan in unique_plans
        )
    )
    row_sums = tuple(
        sp.simplify(sum(block23.transition(source, target) for target in OUTCOMES))
        for source in OUTCOMES
    )
    ten_step_gram = sp.prod(row_sums[0] for _step in range(10))
    p_active = sp.symbols("p_active", commutative=True)
    stop_gram = (
        block23.projector_reduce((1 - p_active) ** 2, p_active)
        if stop_present
        else sp.S.Zero
    )
    full_gram = block23.projector_reduce(p_active + stop_gram, p_active)
    return (
        complete
        and all(value == 1 for value in row_sums)
        and ten_step_gram == 1
        and stop_gram == 1 - p_active
        and full_gram == 1
    )

def branch_is_physical(anchor, incoming, direction, source, target) -> bool:
    try:
        if direction == incoming:
            branch = block24.append_branch(
                anchor, block23.locked_word(incoming, source), target
            )
            return (
                block24.append_factorization_is_physical(branch)
                and block24.branch_effect_is_recontracted(branch)
                and branch.forward_center
                == block24.forward_center(anchor, direction)
                and sp.simplify(
                    branch.effect.scalar - block23.transition(source, target)
                )
                == 0
            )
        if dot(incoming, direction) == 0:
            branch = block28.turn_branch(
                anchor, incoming, source, direction, target
            )
            return (
                block28.turn_branch_is_physical(branch)
                and branch.effect.target_center
                == block24.forward_center(anchor, direction)
                and sp.simplify(
                    branch.effect.scalar - block23.transition(source, target)
                )
                == 0
            )
    except (KeyError, ValueError):
        return False
    return False

def local_factor_module_certificate() -> bool:
    rows = {
        source: sp.simplify(
            sum(block23.transition(source, target) for target in OUTCOMES)
        )
        for source in OUTCOMES
    }
    if not all(value == 1 for value in rows.values()):
        return False
    if not all(
        block23.transition(source, target).is_positive is True
        for source in OUTCOMES
        for target in OUTCOMES
    ):
        return False
    for incoming in DIRECTIONS:
        exits = (incoming,) + tuple(
            direction for direction in DIRECTIONS if dot(incoming, direction) == 0
        )
        for direction in exits:
            for source, target in itertools.product(OUTCOMES, repeat=2):
                if not branch_is_physical(ZERO, incoming, direction, source, target):
                    return False
    return True

def routed_factor_composition_certificate() -> bool:
    count = 0
    for plan in all_plans():
        if not route_plan_certificate(plan):
            return False
        for arm in (plan.left, plan.right):
            source = OUTCOMES[0]
            target = OUTCOMES[-1]
            anchor = arm.start
            incoming = arm.initial_front
            for direction in arm.steps:
                if not branch_is_physical(anchor, incoming, direction, source, target):
                    return False
                anchor = block24.forward_center(anchor, direction)
                incoming = direction
                source, target = target, source
                count += 1
    return count == 192 * 10

def literal_second_use_certificate(mutation=None) -> bool:
    source_left = OUTCOMES[0]
    source_right = OUTCOMES[-1]
    target_left = OUTCOMES[1]
    target_right = OUTCOMES[-2]
    plans = all_plans("legacy_four_step" if mutation == "legacy_four_step" else None)
    for plan in plans:
        if not route_plan_certificate(plan):
            return False
        frame = successor_frame(plan)
        blank_centers = set(successor_blank_centers(plan))
        history_centers = set(plan.old_centers)
        history_centers.update(plan.left.targets[:-1])
        history_centers.update(plan.right.targets[:-1])
        history_blocks = tuple(block_sites(center) for center in history_centers)
        for lam in LAMBDAS:
            coefficient_sum = sp.S.Zero
            for left_exit, right_exit in itertools.product(
                frame.left_exits, frame.right_exits
            ):
                try:
                    descriptor = block28.pair_kraus_descriptor_for(
                        frame,
                        lam,
                        source_left,
                        source_right,
                        left_exit,
                        right_exit,
                        target_left,
                        target_right,
                    )
                    gram = block28.contract_pair_kraus_descriptor(descriptor)
                except (KeyError, ValueError):
                    return False
                expected = sp.simplify(
                    block28.q_weight(lam, left_exit, right_exit)
                    * block23.transition(source_left, target_left)
                    * block23.transition(source_right, target_right)
                )
                output_centers = {
                    descriptor.left.effect.target_center,
                    descriptor.right.effect.target_center,
                }
                nonidentity = block28.branch_nonidentity_sites(
                    descriptor.left
                ) | block28.branch_nonidentity_sites(descriptor.right)
                if not (
                    gram.coefficient == expected
                    and output_centers.issubset(blank_centers)
                    and all(
                        old.isdisjoint(nonidentity) for old in history_blocks
                    )
                ):
                    return False
                coefficient_sum += block28.q_weight(
                    lam, left_exit, right_exit
                )
            if sp.simplify(coefficient_sum) != 1:
                return False
    return True

def second_use_completion_certificate(stop_present=True) -> bool:
    q_rows = tuple(
        sp.simplify(
            sum(
                block28.q_weight(lam, left_exit, right_exit)
                for left_exit, right_exit in itertools.product(
                    block28.LEFT_EXITS, block28.RIGHT_EXITS
                )
            )
        )
        for lam in LAMBDAS
    )
    transition_rows = tuple(
        sp.simplify(sum(block23.transition(source, target) for target in OUTCOMES))
        for source in OUTCOMES
    )
    p_second = sp.symbols("p_second", commutative=True)
    stop_gram = (
        block23.projector_reduce((1 - p_second) ** 2, p_second)
        if stop_present
        else sp.S.Zero
    )
    full_gram = block23.projector_reduce(p_second + stop_gram, p_second)
    return (
        q_rows == (1, 1)
        and all(value == 1 for value in transition_rows)
        and stop_gram == 1 - p_second
        and full_gram == 1
    )

def two_use_prefix_certificate(include_second_marginal=True) -> bool:
    if not include_second_marginal:
        return False
    for lam in LAMBDAS:
        q_sum = sp.simplify(
            sum(
                block28.q_weight(lam, left_exit, right_exit)
                for left_exit, right_exit in itertools.product(
                    block28.LEFT_EXITS, block28.RIGHT_EXITS
                )
            )
        )
        transition_sum = sp.simplify(
            sum(block23.transition(OUTCOMES[0], target) for target in OUTCOMES)
        )
        second_marginal = sp.simplify(q_sum * transition_sum**2)
        first_equality = sp.simplify(
            sum(
                block28.q_weight(lam, left_exit, right_exit)
                for left_exit, right_exit in itertools.product(
                    block28.LEFT_EXITS, block28.RIGHT_EXITS
                )
                if left_exit == right_exit
            )
        )
        joint_two_equal = sp.simplify(first_equality**2)
        if not (
            second_marginal == 1
            and first_equality == (1 + 3 * lam) / 4
            and joint_two_equal == ((1 + 3 * lam) / 4) ** 2
        ):
            return False
    return True

def output_control_certificate(stop_present=True, mutation=None) -> bool:
    return handoff_control_channel_certificate(
        stop_present=stop_present, mutation=mutation
    )

def handoff_signature(lam, chirality, mutation=None):
    route_sign = chirality
    if mutation == "lambda_dependent_route" and lam == sp.Rational(1, 2):
        route_sign = -route_sign
    f = E1
    lateral = tuple(direction for direction in DIRECTIONS if dot(f, direction) == 0)
    return tuple(
        (
            g,
            h,
            route_plan(ZERO, f, g, h, route_sign).left.steps,
            route_plan(ZERO, f, g, h, route_sign).right.steps,
        )
        for g, h in itertools.product(lateral, repeat=2)
    )

def common_law_pushforward_certificate(mutation=None) -> bool:
    f = E1
    lateral = tuple(direction for direction in DIRECTIONS if dot(f, direction) == 0)
    for chirality in (-1, 1):
        signatures = tuple(
            handoff_signature(lam, chirality, mutation) for lam in LAMBDAS
        )
        if signatures[0] != signatures[1]:
            return False
        for lam in LAMBDAS:
            weights = {
                (g, h): block28.q_weight(lam, g, h)
                for g, h in itertools.product(lateral, repeat=2)
            }
            equality_probability = sp.simplify(
                sum(value for (g, h), value in weights.items() if g == h)
            )
            if (
                sp.simplify(sum(weights.values())) != 1
                or not all(value > 0 for value in weights.values())
                or equality_probability != (1 + 3 * lam) / 4
                or not all(
                    route_plan_certificate(route_plan(ZERO, f, g, h, chirality))
                    for g, h in weights
                )
            ):
                return False
    return True

def bounded_routes():
    plans = all_plans()
    if len(plans) != 192 or not all(route_plan_certificate(p) for p in plans):
        return False
    for front in DIRECTIONS:
        carriers=[]
        for chirality in (-1,1):
            selected=[p for p in plans if p.front == front and p.chirality == chirality]
            # Field name checked against the actual RoutePlan definition below.
            carrier=set()
            for p in selected:
                carrier.update((p.left.start,p.right.start))
                carrier.update(p.left.targets+p.right.targets+successor_blank_centers(p))
            if len(carrier) != 160:
                return False
            for p in selected:
                initial=carrier-{p.left.start,p.right.start}
                written=set(p.left.targets+p.right.targets)
                if len(initial)!=158 or len(written)!=10 or not written <= initial or not set(successor_blank_centers(p)) <= initial-written:
                    return False
            carriers.append(carrier)
        if carriers[0] != carriers[1]:
            return False
    return legacy_four_step_clearance_profile() == {-1:{'equal':24,'opposite':0,'orthogonal':0},1:{'equal':24,'opposite':0,'orthogonal':0}}


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 30
# Literal inputs and hashes are frozen after all source/note edits.
AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_D4_OUTPUT_CONDITIONED_PAIR_SUCCESSOR_COMMON_TWO_USE_CYLINDER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md', 'docs/ADMISSIBILITY_D4_RETURNED_TIP_SUPPLIED_Q_CONDITIONAL_PAIR_INSTRUMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-30.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'scripts/admissibility_d4_prior_record_live_preparation_two_event_prefix_2026_08_30.py', 'scripts/admissibility_d4_returned_tip_strict_support_analytic_coupling_gate_2026_08_30.py', 'scripts/admissibility_d4_self_delimiting_forward_record_append_history_2026_08_30.py')
DIRECT_HASHES = {'docs/ADMISSIBILITY_D4_OUTPUT_CONDITIONED_PAIR_SUCCESSOR_COMMON_TWO_USE_CYLINDER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md': '655f7bc858b859dd84580ed9eb446f74ecfb1cfb87bfd1d9a00cc2339b9c7e6b', 'docs/ADMISSIBILITY_D4_RETURNED_TIP_SUPPLIED_Q_CONDITIONAL_PAIR_INSTRUMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-30.md': '86913d27c2f428d8d510ea374541b017ac4daa380574fe3486756374e7112320', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'scripts/admissibility_d4_prior_record_live_preparation_two_event_prefix_2026_08_30.py': 'a454b4ce47af92bbf55550ebae068ff4a419b141d916b0c4fcdc1678bf283a7e', 'scripts/admissibility_d4_returned_tip_strict_support_analytic_coupling_gate_2026_08_30.py': '54b5d7faac7d6bc3484619d09e30b4b8f27efc84677142a48a5fe24f995d105d', 'scripts/admissibility_d4_self_delimiting_forward_record_append_history_2026_08_30.py': '5eb733c3a50da1f7c1bb8a46b547b1b91fd85c27856e425d8040305b3d009d6c'}

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
    ok=bool(bounded_routes())
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'192_routes_common160_carrier_and_failed_four_step')
    ok=bool(displayed_multiplicity_certificate())
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'two_route_chiralities')
    print('TERMINAL: '+('BLOCK30-NAMED-BOUNDED-CHECKS-COMPLETE;CONDITIONAL-PROOFS-PRESERVED' if failed==0 else 'INCOMPLETE-NO-SCIENCE-INFERENCE'))
    print(f'TOTAL: PASS={passed} FAIL={failed}')
    return int(failed!=0)

if __name__=='__main__':
    raise SystemExit(main())
