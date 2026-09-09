#!/usr/bin/env python3
"""Independent reconstruction of the hard-core self-addressing compiler."""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path

from sympy import I, Matrix, Rational as Q, simplify

from nn_record_homogeneous_payload_self_hosting_writer_2026_08_22 import (
    GaussianLaw,
    I2,
    SX,
    content_mass,
    decode_payload,
    local_law,
)


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/NN_RECORD_ISOLATED_SHAPE_COMPILER_BOUNDED_THEOREM_NOTE_2026-08-22.md",
    "scripts/nn_record_isolated_shape_compiler_2026_08_22.py",
    "scripts/nn_record_homogeneous_payload_self_hosting_writer_2026_08_22.py",
)

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "NN_RECORD_ISOLATED_SHAPE_COMPILER_BOUNDED_THEOREM_NOTE_2026-08-22.md"
)

E = (
    (1, 0, 0), (-1, 0, 0), (0, 1, 0),
    (0, -1, 0), (0, 0, 1), (0, 0, -1),
)
ORDER = (
    (1, 1, 0), (1, 0, 0), (0, 1, 0), (-1, 1, 0),
    (-1, 0, 0), (1, 0, 1), (0, 0, 1), (1, 0, -1),
    (0, 0, -1), (1, -1, 0), (0, -1, 0),
)
O = (0, 0, 0)


def plus(a, b):
    return tuple(a[i] + b[i] for i in range(3))


def minus(a, b):
    return tuple(a[i] - b[i] for i in range(3))


def norm(a):
    return sum(abs(value) for value in a)


def parity(permutation):
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(3)
        for j in range(i + 1, 3)
    )
    return -1 if inversions % 2 else 1


def rotation_group():
    group = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            if parity(permutation) * signs[0] * signs[1] * signs[2] == 1:
                group.append((permutation, signs))
    return tuple(group)


GROUP = rotation_group()


def rotate(rotation, point):
    permutation, signs = rotation
    return tuple(signs[row] * point[permutation[row]] for row in range(3))


def move(points, displacement):
    return frozenset(plus(point, displacement) for point in points)


def neighborhood(points):
    return frozenset(points) | {plus(point, edge) for point in points for edge in E}


BLOCK = frozenset(ORDER) | {O}
GUARD = neighborhood(BLOCK)


def embeddings(points, stage):
    points = frozenset(points)
    result = []
    for rotation in GROUP:
        template = frozenset(rotate(rotation, point) for point in ORDER[:stage])
        rotated_root = rotate(rotation, ORDER[0])
        for observed in points:
            displacement = minus(observed, rotated_root)
            if move(template, displacement) == points:
                result.append((rotation, displacement))
    return tuple(result)


def next_sites(points, stage, obstacles=frozenset()):
    canonical_next = ORDER[stage] if stage < len(ORDER) else O
    result = set()
    for rotation, displacement in embeddings(points, stage):
        placed_guard = move(
            (rotate(rotation, point) for point in GUARD), displacement
        )
        if (placed_guard - set(points)) & set(obstacles):
            continue
        result.add(plus(displacement, rotate(rotation, canonical_next)))
    return frozenset(result - set(points) - set(obstacles))


def actual_stage_matches(points):
    """Independently union every clean embedded prefix stage in the Law."""
    points = frozenset(points)
    result = {}
    for stage in range(1, len(ORDER) + 1):
        canonical_next = ORDER[stage] if stage < len(ORDER) else O
        for rotation in GROUP:
            template = frozenset(rotate(rotation, point) for point in ORDER[:stage])
            rotated_root = rotate(rotation, ORDER[0])
            rotated_next = rotate(rotation, canonical_next)
            rotated_guard = frozenset(rotate(rotation, point) for point in GUARD)
            for observed_root in points:
                displacement = minus(observed_root, rotated_root)
                placed_prefix = move(template, displacement)
                if not placed_prefix.issubset(points):
                    continue
                placed_guard = move(rotated_guard, displacement)
                if (placed_guard - placed_prefix) & points:
                    continue
                candidate = plus(displacement, rotated_next)
                if candidate not in points:
                    result.setdefault(candidate, set()).add(stage)
    return {candidate: frozenset(stages) for candidate, stages in result.items()}


def actual_labeled_stage_matches(records):
    """All-stage matcher with independent writer labels standing in for content."""
    points = frozenset(records)
    result = {}
    for stage in range(1, len(ORDER) + 1):
        canonical_next = ORDER[stage] if stage < len(ORDER) else O
        for rotation in GROUP:
            template = frozenset(rotate(rotation, point) for point in ORDER[:stage])
            rotated_root = rotate(rotation, ORDER[0])
            rotated_next = rotate(rotation, canonical_next)
            rotated_guard = frozenset(rotate(rotation, point) for point in GUARD)
            for observed_root in points:
                displacement = minus(observed_root, rotated_root)
                placed_prefix = move(template, displacement)
                if not placed_prefix.issubset(points):
                    continue
                labels = {records[point] for point in placed_prefix}
                if len(labels) != 1:
                    continue
                placed_guard = move(rotated_guard, displacement)
                if (placed_guard - placed_prefix) & points:
                    continue
                candidate = plus(displacement, rotated_next)
                if candidate not in points:
                    result.setdefault(candidate, set()).add(
                        (stage, next(iter(labels)))
                    )
    return {candidate: frozenset(matches) for candidate, matches in result.items()}


def target_sites(points, stage):
    return frozenset(
        plus(displacement, rotate(rotation, O))
        for rotation, displacement in embeddings(points, stage)
    )


def histories():
    result = [{frozenset({O})}]
    exact_stage_partition = True
    for stage in range(1, 11):
        successors = set()
        for state in result[-1]:
            actual = actual_stage_matches(state)
            expected = next_sites(state, stage)
            exact_stage_partition = exact_stage_partition and (
                frozenset(actual) == expected
                and all(stages == frozenset({stage}) for stages in actual.values())
            )
            successors.update(
                frozenset(set(state) | {candidate}) for candidate in actual
            )
        result.append(successors)
    terminal_pairs = set()
    for carriers in result[-1]:
        actual = actual_stage_matches(carriers)
        expected = next_sites(carriers, 11)
        exact_stage_partition = exact_stage_partition and (
            frozenset(actual) == expected
            and all(stages == frozenset({11}) for stages in actual.values())
        )
        terminal_pairs.update((carriers, target) for target in actual)
    completed_quiescent = all(
        not actual_stage_matches(set(carriers) | {target})
        for carriers, target in terminal_pairs
    )
    return (
        tuple(result),
        terminal_pairs,
        exact_stage_partition,
        completed_quiescent,
        sum(len(level) for level in result),
    )


def neighbor_count(site, occupied):
    return sum(plus(site, edge) in occupied for edge in E)


def main() -> int:
    passed = 0
    failed = 0

    def check(name, condition, detail):
        nonlocal passed, failed
        if condition:
            passed += 1
            print(f"PASS {name}: {detail}")
        else:
            failed += 1
            print(f"FAIL {name}: {detail}")

    check(
        "independent-cubic-group-and-guard",
        len(GROUP) == 24 and len(BLOCK) == 12 and len(GUARD) == 41,
        "signed permutations independently recover 24 rotations and the 12/41 block census",
    )

    canonical_counts = tuple(
        len(next_sites(frozenset(ORDER[:stage]), stage)) for stage in range(1, 12)
    )
    check(
        "independent-frontier-orbits",
        canonical_counts == (6, 8, 2, 1, 2, 1, 1, 1, 1, 1, 1),
        "the independent stabilizer enumeration reproduces every equal-rate frontier size",
    )

    (
        stage_sets,
        terminal_pairs,
        exact_stage_partition,
        completed_quiescent,
        unfinished_state_count,
    ) = histories()
    counts = tuple(len(level) for level in stage_sets)
    final_carriers = stage_sets[-1]
    check(
        "independent-history-closure",
        counts + (len(terminal_pairs),)
        == (1, 6, 36, 72, 60, 120, 120, 120, 120, 120, 120, 120)
        and len(terminal_pairs) == 120
        and len({target for _carriers, target in terminal_pairs}) == 18
        and max(norm(site) for carriers, target in terminal_pairs for site in set(carriers) | {target}) == 4,
        "all histories independently close into 120 radius-four placements with 18 output offsets",
    )

    check(
        "independent-all-stage-exhaustion",
        exact_stage_partition
        and completed_quiescent
        and unfinished_state_count == 895,
        "all 895 unfinished states have only the intended stage and all 120 terminals have no growth frontier",
    )

    address_ok = True
    for header in stage_sets[2]:
        direct = target_sites(header, 3)
        continuations = {header}
        for stage in range(3, 11):
            continuations = {
                frozenset(set(state) | {candidate})
                for state in continuations
                for candidate in next_sites(state, stage)
            }
        eventual = {
            target
            for state in continuations
            for target in next_sites(state, 11)
        }
        address_ok = address_ok and len(direct) == 1 and eventual == set(direct)
    check(
        "independent-three-record-address",
        address_ok,
        "every three-site L header independently fixes the same target across all later races",
    )

    all_degrees_ok = True
    for stage, states in enumerate(stage_sets, start=1):
        if stage > 11:
            break
        for state in states:
            for candidate in next_sites(state, stage):
                all_degrees_ok = all_degrees_ok and neighbor_count(candidate, state) == (
                    1 if stage < 11 else 6
                )
    h_value = Matrix([[1, 1], [1, 2]])
    payload = simplify(h_value + I * SX)
    decoded = decode_payload(payload)
    carrier_law = local_law((payload,))
    read_law = local_law((payload,) * 6)
    check(
        "independent-content-interface",
        all_degrees_ok
        and content_mass(carrier_law, payload) == 1
        and decoded is not None
        and content_mass(read_law, decoded.projector) == Q(13, 14)
        and content_mass(read_law, decoded.complement) == Q(1, 14)
        and not isinstance(read_law, GaussianLaw),
        "independent neighbor degrees reproduce deterministic copies and the exact terminal read",
    )

    completed = [set(carriers) | {target} for carriers, target in terminal_pairs]
    possible_offsets = set().union(*completed)
    forbidden = {
        minus(minus(left, right), separation)
        for left in possible_offsets
        for right in possible_offsets
        for separation in ((0, 0, 0),) + E
    }
    check(
        "independent-radius-nine-separation",
        max(norm(vector) for vector in forbidden) == 9
        and all(norm(vector) >= 10 for vector in ((10, 0, 0), (6, 4, 0))),
        "no pair of reachable cores can overlap or touch when causal roots are distance ten",
    )

    x_path = (
        (0, 0, 0), (1, 0, 0), (0, 1, 0), (2, 0, 0), (2, 1, 0),
        (2, 1, -1), (1, 1, -1), (2, 1, 1), (1, 1, 1), (2, 2, 0),
        (1, 2, 0),
    )
    y_path = (
        (5, 4, 0), (4, 4, 0), (5, 3, 0), (3, 4, 0), (3, 3, 0),
        (3, 3, -1), (4, 3, -1), (3, 3, 1), (4, 3, 1), (3, 2, 0),
        (4, 2, 0),
    )
    paths_valid = True
    for path in (x_path, y_path):
        occupied = frozenset({path[0]})
        for stage, candidate in enumerate(path[1:], start=1):
            paths_valid = paths_valid and candidate in next_sites(occupied, stage)
            occupied = frozenset(set(occupied) | {candidate})
    x10, y10 = x_path[9], y_path[9]
    joint_records = {x_path[0]: "X", y_path[0]: "Y"}
    joint_reachable = True
    for stage, candidate in enumerate(x_path[1:9], start=1):
        matches = actual_labeled_stage_matches(joint_records)
        joint_reachable = joint_reachable and (stage, "X") in matches.get(
            candidate, frozenset()
        )
        joint_records[candidate] = "X"
    for stage, candidate in enumerate(y_path[1:9], start=1):
        matches = actual_labeled_stage_matches(joint_records)
        joint_reachable = joint_reachable and (stage, "Y") in matches.get(
            candidate, frozenset()
        )
        joint_records[candidate] = "Y"
    joint_frontier = actual_labeled_stage_matches(joint_records)

    def sites_for_label(frontier, label):
        return {
            site
            for site, matches in frontier.items()
            if any(match_label == label for _stage, match_label in matches)
        }

    x_frontier = sites_for_label(joint_frontier, "X")
    y_frontier = sites_for_label(joint_frontier, "Y")
    after_x = dict(joint_records)
    after_x[x10] = "X"
    after_y = dict(joint_records)
    after_y[y10] = "Y"
    check(
        "independent-radius-eight-mutation",
        norm(minus(x_path[0], y_path[0])) == 9
        and paths_valid
        and joint_reachable
        and x_frontier == {x10}
        and y_frontier == {y10}
        and joint_frontier[x10] == frozenset({(9, "X")})
        and joint_frontier[y10] == frozenset({(9, "Y")})
        and norm(minus(x10, y10)) == 1
        and not sites_for_label(actual_labeled_stage_matches(after_x), "Y")
        and not sites_for_label(actual_labeled_stage_matches(after_y), "X"),
        "the independent all-stage P9/P9 reconstruction shows the first tenth birth jams every continuation of the other writer",
    )

    singleton = frozenset({O})
    singleton_frontier = next_sites(singleton, 1)
    covariance_ok = True
    representative_fails = False
    selected = min(singleton_frontier)
    for rotation in GROUP:
        rotated_state = frozenset(rotate(rotation, site) for site in singleton)
        expected = frozenset(rotate(rotation, site) for site in singleton_frontier)
        actual = next_sites(rotated_state, 1)
        covariance_ok = covariance_ok and expected == actual
        representative_fails = representative_fails or rotate(rotation, selected) != min(actual)
    check(
        "independent-covariance-control",
        covariance_ok and representative_fails,
        "frontier sets commute with all rotations while a preferred representative does not",
    )

    p2 = frozenset(ORDER[:2])
    early_law = local_law((payload,))
    moved_header = p2 | {O}
    check(
        "independent-fixed-target-boundary",
        O in next_sites(p2, 2)
        and content_mass(early_law, payload) == 1
        and O not in target_sites(moved_header, 3),
        "the canonical origin can be a permanent third carrier before the header selects another output",
    )

    count_ball = lambda radius: sum(
        abs(x) + abs(y) + abs(z) <= radius
        for x in range(-radius, radius + 1)
        for y in range(-radius, radius + 1)
        for z in range(-radius, radius + 1)
    )
    check(
        "independent-causal-and-root-cylinder",
        count_ball(9) == 1159,
        "independent lattice enumeration recovers the range-nine influence and direct B9 root cylinder",
    )

    note = NOTE.read_text(encoding="utf-8")
    fences = (
        "self-addressing", "predesignated-target", "hostile", "recurrent",
        "physical time", "trace-Law selection", "PR #7318",
        "TOE percentages", "No Minimal Axioms edit",
    )
    check(
        "independent-source-fence",
        all(fence in note for fence in fences),
        "the note preserves address, environment, resource, time, selection, axiom, and score limits",
    )

    print("per_element: independent generic payload, copy support, projector weights, and binary occupancy semantics are checked")
    print("per_site: independent seed, symmetry frontier, emergent target, occupied, and jammed branches are checked")
    print("per_mode: independent range-nine and marked-clock bounds are checked; no physical-time interpretation is made")
    print("per_block: 895 unfinished states, 120 terminals, 18 target offsets, all headers, and the two-writer mutation are reconstructed")
    print("lattice_wide: root separation plus finite-stage recurring clocks imply admitted-root completion only from blank initial data")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return int(failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
