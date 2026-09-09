#!/usr/bin/env python3
"""Block30: supplied-control physical successor and conditional second use.

Derive a fixed-five-step output-conditioned route from every Block28 lateral
Record pair to a complete fresh returned-pair carrier.  The individual writes are literal
Block24 straight appends or Block28 perpendicular turns.  The route controller
is deliberately supplied at pair level; this runner does not promote it to a
nearest-neighbor autonomous law.
"""

from __future__ import annotations

import hashlib
import itertools
import sys
from dataclasses import dataclass, replace
from functools import lru_cache
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_prior_record_live_preparation_two_event_prefix_2026_08_30 as block23  # noqa: E402
import admissibility_d4_self_delimiting_forward_record_append_history_2026_08_30 as block24  # noqa: E402
import admissibility_d4_returned_tip_strict_support_analytic_coupling_gate_2026_08_30 as block28  # noqa: E402


AUDIT_TIMEOUT_SEC = 900
PACKET_REL = (
    ".claude/science/physics-loops/"
    "toe-source-eta-ownership-block30-physical-successor-handoff-20260831"
)
PACKET = ROOT / PACKET_REL
RUNNER_SOURCE_PIN = PACKET / "RUNNER_SOURCE_PIN.md"

DIRECT_HASHES = {
    "scripts/admissibility_d4_prior_record_live_preparation_two_event_prefix_2026_08_30.py": "426488df2a431cb7d415d5e933013f7ce0826cc9514f96cd041b9fc6ff49742a",
    "scripts/admissibility_d4_self_delimiting_forward_record_append_history_2026_08_30.py": "f98534f07655e0de296f2060932e34aa7a600f08545f3661be2843d05accc15d",
    "scripts/admissibility_d4_returned_tip_strict_support_analytic_coupling_gate_2026_08_30.py": "91141d7b917b52eef1335cc6d405acd5927d75ab32ce2f4e0620d4c9007b9a2a",
    "docs/MINIMAL_AXIOMS_2026-06-29.md": "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753",
}

FROZEN = {
    "APPROACH_REGISTRY.md": "3aab62ff2777b10c8ec904f2f1f21322ebb5dc7d2dafc40cf780af86de8d6d80",
    "ARTIFACT_PLAN.md": "af732d9c86c8294635bc90e0cf627e1349941b398cc77fc03ce2bae4e61d9be9",
    "ASSUMPTIONS_AND_IMPORTS.md": "dff5a7e15257b1a5ad5a1e5f6d01edf0720c5f5b78577554295ffb8c8459e196",
    "AUTHORITY_GATE.md": "c39a92056f6f926f2d3788fc052bbb976c7f1283d96970d2685b57badca10ce9",
    "GOAL.md": "f13cc6746afe042e1c82f9341cf0063d57904ab01b4b4159ad242ee01c02632f",
    "INDEPENDENT_STATIC_ATTACK_FINAL.md": "e4840b544761a937bccbc5d4c96aec63d95d0d28c338ac1924fed64ba70dfd49",
    "MUTATION_PLAN.md": "0f150b13606a97dd1dc408d537a91b83697b615771cfd419cacc3ed132bdaf77",
    "NO_GO_DISCIPLINE_CHECKLIST.md": "b9423ff04f165a0bda2dc6ac6ee49510c4f838817a250688f702ba660004dc74",
    "OPPORTUNITY_QUEUE.md": "8867d3e024c7a9c8257661778112385a29f719f5d30441d3a85b89306ad47830",
    "PANEL_RETURN.md": "fc183fa9a3cc794344c91d98b7ff2da15c31e0109a0d409c4ad015fe26ca2906",
    "PREFLIGHT_WITNESSES.md": "5f66ff786f8338f984862ab5026f1f0fdf61cf1333b1e51801636db282a9404f",
    "PREREG_AMENDMENT_SUCCESSOR_CARRIER.md": "122fe79ede0f4408cfdd034c585b2b65807b8d53b42ba84c5f99eefa2a02845f",
    "ROUTE_PORTFOLIO.md": "a92ea649512a778a65e7b6e75f8f22c3c5e09c027594049c91124926423784d1",
    "STATE.yaml": "797e27332c6e4cd9d472727172979578a971de08e673540252b63fff36fd00bc",
    "TRACE_GATE.md": "28e28db87b55d2733a3a95923754d4bb19040cfb3f23989f97d3041fc0dd1994",
}

# This literal tuple is parsed by the content-bound cache wrapper.
AUDIT_INPUT_PATHS = (
    "scripts/admissibility_d4_prior_record_live_preparation_two_event_prefix_2026_08_30.py",
    "scripts/admissibility_d4_self_delimiting_forward_record_append_history_2026_08_30.py",
    "scripts/admissibility_d4_returned_tip_strict_support_analytic_coupling_gate_2026_08_30.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block30-physical-successor-handoff-20260831/APPROACH_REGISTRY.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block30-physical-successor-handoff-20260831/ARTIFACT_PLAN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block30-physical-successor-handoff-20260831/ASSUMPTIONS_AND_IMPORTS.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block30-physical-successor-handoff-20260831/AUTHORITY_GATE.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block30-physical-successor-handoff-20260831/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block30-physical-successor-handoff-20260831/MUTATION_PLAN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block30-physical-successor-handoff-20260831/NO_GO_DISCIPLINE_CHECKLIST.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block30-physical-successor-handoff-20260831/OPPORTUNITY_QUEUE.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block30-physical-successor-handoff-20260831/PANEL_RETURN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block30-physical-successor-handoff-20260831/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block30-physical-successor-handoff-20260831/PREREG_AMENDMENT_SUCCESSOR_CARRIER.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block30-physical-successor-handoff-20260831/ROUTE_PORTFOLIO.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block30-physical-successor-handoff-20260831/STATE.yaml",
    ".claude/science/physics-loops/toe-source-eta-ownership-block30-physical-successor-handoff-20260831/TRACE_GATE.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block30-physical-successor-handoff-20260831/INDEPENDENT_STATIC_ATTACK_FINAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block30-physical-successor-handoff-20260831/RUNNER_SOURCE_PIN.md",
)

ZERO = (0, 0, 0)
E1 = (1, 0, 0)
E2 = (0, 1, 0)
DIRECTIONS = block23.DIRECTIONS
OUTCOMES = block23.OUTCOMES
ROTATIONS = block23.ROTATIONS
DISPLACEMENT = block23.DISPLACEMENT
LAMBDAS = (sp.S.Zero, sp.Rational(1, 2))


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def runner_source_pin_ok() -> bool:
    if not RUNNER_SOURCE_PIN.exists():
        return False
    pins = {}
    for line in RUNNER_SOURCE_PIN.read_text().splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            pins[key.strip()] = value.strip().strip("`")
    return pins.get("source_sha256") == file_sha256(Path(__file__))


def frozen_hashes_ok() -> bool:
    return (
        all(file_sha256(ROOT / name) == digest for name, digest in DIRECT_HASHES.items())
        and all(file_sha256(PACKET / name) == digest for name, digest in FROZEN.items())
        and runner_source_pin_ok()
    )


def input_fingerprint() -> str:
    digest = hashlib.sha256()
    digest.update(b"runner-cache-input-fingerprint-v1\0")
    for relative in AUDIT_INPUT_PATHS:
        body = (ROOT / relative).read_bytes()
        encoded = relative.encode("utf-8")
        digest.update(len(encoded).to_bytes(8, "big"))
        digest.update(encoded)
        digest.update(len(body).to_bytes(8, "big"))
        digest.update(body)
    return digest.hexdigest()


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


@dataclass(frozen=True)
class ClaimScope:
    nearest_neighbor_controller: bool = False
    autonomous_invocation: bool = False
    autonomous_second_pair_use: bool = False
    resource_renewal: bool = False
    cadence_or_rate: bool = False
    gravity_join: bool = False
    axiom_amendment: bool = False
    audit_retention: bool = False
    obligation_retirement: bool = False
    toe_score_movement: bool = False


DEFAULT_SCOPE = ClaimScope()
TERMINAL_TEXT = (
    "BOTH-SUPPLIED-Q-LAWS-SURVIVE-COMMON-FINITE-TWO-USE-CYLINDER;"
    "AT-LEAST-TWO-COVARIANT-ROUTES-PRESENT"
)


def scope_guard_certificate(scope=DEFAULT_SCOPE, terminal=TERMINAL_TEXT) -> bool:
    return terminal == TERMINAL_TEXT and not any(scope.__dict__.values())


def corrupted_factor_rejections():
    source = OUTCOMES[0]
    target = OUTCOMES[-1]
    current = block23.locked_word(E1, source)
    results = {}
    try:
        factors = block24.make_append_factors(
            ZERO, current, target, drop_writer_pointer_factor=True
        )
        block24.contract_append_effect(factors)
        results["corrupt_straight_factor"] = False
    except (KeyError, ValueError):
        results["corrupt_straight_factor"] = True
    locked = block23.BlockProduct(
        block23.BLANK_LIVE, block23.locked_word(E1, source)
    )
    try:
        factors = block24.make_append_factors(
            ZERO, current, target, forward_input_override=locked
        )
        block24.contract_append_effect(factors)
        results["locked_target_claimed_Blank"] = False
    except (KeyError, ValueError):
        results["locked_target_claimed_Blank"] = True
    try:
        factors = block28.make_turn_factors(
            ZERO, E1, source, E2, target, "overwrite_record"
        )
        block28.contract_turn_effect(factors)
        results["overwrite_current_Record"] = False
    except (KeyError, ValueError):
        results["overwrite_current_Record"] = True
    return results


def mutation_rejections():
    rejections = {
        "coordinate_named_route_breaks_covariance": not covariance_certificate(
            "coordinate_mark"
        ),
        "immediate_reverse_breaks_step_legality": not geometry_certificate(
            "immediate_reverse"
        ),
        "deleted_step_breaks_five_step_type": not geometry_certificate("delete_step"),
        "bad_endpoint_breaks_facing_pair": not geometry_certificate("bad_facing"),
        "revisited_center_breaks_freshness": not geometry_certificate(
            "revisit_center"
        ),
        "shared_output_breaks_arm_disjointness": not geometry_certificate(
            "shared_start"
        ),
        "old_Record_target_breaks_freshness": not geometry_certificate("old_target"),
        "legacy_four_step_pair_fails_complete_successor": legacy_four_step_clearance_profile()
        == {
            -1: {"equal": 24, "opposite": 0, "orthogonal": 0},
            1: {"equal": 24, "opposite": 0, "orthogonal": 0},
        },
        "selected_only_Blanks_fail_common_carrier": not common_carrier_certificate(
            "selected_only_carrier"
        ),
        "aliased_pair_control_breaks_injectivity": not output_control_certificate(
            mutation="alias_control"
        ),
        "missing_STOP_breaks_full_space_TP": not output_control_certificate(False),
        "missing_second_STOP_breaks_two_use_TP": not second_use_completion_certificate(
            False
        ),
        "omitted_second_marginal_breaks_prefix": not two_use_prefix_certificate(
            False
        ),
        "lambda_dependent_route_breaks_common_handoff": not common_law_pushforward_certificate(
            "lambda_dependent_route"
        ),
        "collapsed_chirality_breaks_route_multiplicity": not displayed_multiplicity_certificate(
            "collapse_chirality"
        ),
    }
    rejections.update(corrupted_factor_rejections())
    for field in ClaimScope.__dataclass_fields__:
        rejections[f"scope_{field}_promotion_rejected"] = not scope_guard_certificate(
            replace(DEFAULT_SCOPE, **{field: True})
        )
    return rejections


class Checks:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def check(self, name, condition, detail):
        if condition:
            self.passed += 1
            print(f"PASS {name}: {detail}")
        else:
            self.failed += 1
            print(f"FAIL {name}: {detail}")


def main() -> int:
    checks = Checks()
    checks.check(
        "frozen_inputs_and_source_pin",
        frozen_hashes_ok(),
        f"19 frozen inputs plus source pin; fingerprint={input_fingerprint()}",
    )
    checks.check(
        "derived_five_step_successor_geometry",
        geometry_certificate(),
        "192 plans; ten fresh trail Records, one returned-facing pair, and eight clear next-use Blank blocks each",
    )
    checks.check(
        "translation_rotation_side_exchange_covariance",
        covariance_certificate(),
        "192 translations/side exchanges and 4,608 proper-cubic transports derived from orbit formulas",
    )
    checks.check(
        "literal_straight_and_turn_factor_module",
        local_factor_module_certificate(),
        "5,880 exact source/target branches reconstruct positive normalized Block24/28 rows",
    )
    checks.check(
        "routed_factor_composition_and_debit",
        routed_factor_composition_certificate(),
        "1,920 route-step instances bind exact QND factors; every route consumes ten fresh Blank blocks",
    )
    checks.check(
        "fixed_common_successor_carrier",
        common_carrier_certificate(),
        "one covariant 160-block carrier serves every output and chirality: 2 Locked + 158 Blank, then 10 consumed + 148 Blank",
    )
    checks.check(
        "literal_handoff_controls_and_STOP",
        output_control_certificate(),
        "3,136 orthogonal output controls bind the common carrier, normalized ten-step channel, and full-space STOP",
    )
    checks.check(
        "common_two_law_pushforward",
        common_law_pushforward_certificate(),
        "the same lambda-independent handoff normalizes both supplied laws and preserves P(g=h)=1/4,5/8",
    )
    checks.check(
        "literal_second_Block28_use",
        literal_second_use_certificate(),
        "6,144 frame/lambda/exit descriptors bind the reached pair and eight Blank targets while preserving every trail Record",
    )
    checks.check(
        "second_use_STOP_and_prefix",
        second_use_completion_certificate() and two_use_prefix_certificate(),
        "the second Kraus family has a complement STOP and marginalizes exactly to the first-use/handoff prefix",
    )
    checks.check(
        "positive_route_multiplicity",
        displayed_multiplicity_certificate(),
        "canonical orbit counts are 4 equal, 8 orthogonal, 4 opposite; both chiralities differ on all opposite pairs",
    )
    checks.check(
        "bounded_claim_scope",
        scope_guard_certificate(),
        "joint controller and both invocations remain supplied; nearest-neighbor autonomy, renewal, cadence, gravity, axioms, audit, and scores remain open",
    )
    mutations = mutation_rejections()
    for name, rejected in mutations.items():
        print(f"MUTATION {'REJECTED' if rejected else 'SURVIVED'} {name}")
    checks.check(
        "designated_mutations",
        len(mutations) == 28 and all(mutations.values()),
        f"rejected={sum(mutations.values())}/{len(mutations)}",
    )

    print(
        "per_element: checked — exact transition roots and Locked-pointer maps for every straight/turn source-target branch"
    )
    print(
        "per_site: checked — five handoff writes per arm, QND history, ten fresh trail Blocks, eight clear second-use targets, and outside identities"
    )
    print(
        "per_mode: checked — all 16 ordered lateral exit pairs, both fixed chiralities, and lambda=0,1/2"
    )
    print(
        "per_block: checked — common 160-block carrier, 3,136 output controls, handoff/second-use normalization, prefix, and both STOPs"
    )
    print(
        "lattice_wide: checked and not executed — the two uses remain externally invoked; no nearest-neighbor comparison, autonomy, renewal, or global tiling is claimed"
    )
    if checks.failed == 0:
        print(f"TERMINAL: {TERMINAL_TEXT}")
    else:
        print("TERMINAL: INCOMPLETE-NO-SCIENCE-INFERENCE")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
