#!/usr/bin/env python3
"""Independent reconstruction of the spatial Record trial ensemble."""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path

from sympy import I, Matrix, Rational as Q, exp, limit, oo, simplify, sqrt, symbols

from nn_record_homogeneous_payload_self_hosting_writer_2026_08_22 import (
    I2,
    SX,
    SZ,
    content_mass,
    decode_payload,
    local_law,
    matrix_equal,
    trace_weight,
)


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/NN_RECORD_SPATIAL_TRIAL_ENSEMBLE_BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "scripts/nn_record_spatial_trial_ensemble_2026_08_23.py",
    "docs/NN_RECORD_ISOLATED_SHAPE_COMPILER_BOUNDED_THEOREM_NOTE_2026-08-22.md",
    "scripts/nn_record_isolated_shape_compiler_independent_check_2026_08_22.py",
    "scripts/nn_record_homogeneous_payload_self_hosting_writer_2026_08_22.py",
)

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "NN_RECORD_SPATIAL_TRIAL_ENSEMBLE_BOUNDED_THEOREM_NOTE_2026-08-23.md"
)

E = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
ORDER = (
    (1, 1, 0),
    (1, 0, 0),
    (0, 1, 0),
    (-1, 1, 0),
    (-1, 0, 0),
    (1, 0, 1),
    (0, 0, 1),
    (1, 0, -1),
    (0, 0, -1),
    (1, -1, 0),
    (0, -1, 0),
)
O = (0, 0, 0)


def plus(left, right):
    return tuple(left[index] + right[index] for index in range(3))


def minus(left, right):
    return tuple(left[index] - right[index] for index in range(3))


def norm(point):
    return sum(abs(coordinate) for coordinate in point)


def parity(permutation):
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(3)
        for right in range(left + 1, 3)
    )
    return -1 if inversions % 2 else 1


def rotation_group():
    result = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            if parity(permutation) * product_value(signs) == 1:
                result.append((permutation, signs))
    return tuple(result)


def product_value(values):
    result = 1
    for value in values:
        result *= value
    return result


GROUP = rotation_group()


def rotate(rotation, point):
    permutation, signs = rotation
    return tuple(
        signs[row] * point[permutation[row]] for row in range(3)
    )


def move(points, displacement):
    return frozenset(plus(point, displacement) for point in points)


def neighborhood(points):
    points = frozenset(points)
    return points | {plus(point, edge) for point in points for edge in E}


BLOCK = frozenset(ORDER) | {O}
GUARD = neighborhood(BLOCK)


def embeddings(points, stage):
    points = frozenset(points)
    result = []
    for rotation in GROUP:
        template = frozenset(rotate(rotation, point) for point in ORDER[:stage])
        template_anchor = rotate(rotation, ORDER[0])
        for observed in points:
            displacement = minus(observed, template_anchor)
            if move(template, displacement) == points:
                result.append((rotation, displacement))
    return tuple(result)


def next_sites(points, stage, obstacles=frozenset()):
    points = frozenset(points)
    canonical_next = ORDER[stage] if stage < len(ORDER) else O
    result = set()
    for rotation, displacement in embeddings(points, stage):
        placed_guard = move(
            (rotate(rotation, point) for point in GUARD), displacement
        )
        if (placed_guard - points) & set(obstacles):
            continue
        result.add(plus(displacement, rotate(rotation, canonical_next)))
    return frozenset(result - points - set(obstacles))


def actual_stage_matches(points):
    """Union all clean embedded prefixes, independently of expected stage."""
    points = frozenset(points)
    result = {}
    for stage in range(1, len(ORDER) + 1):
        canonical_next = ORDER[stage] if stage < len(ORDER) else O
        for rotation in GROUP:
            template = frozenset(
                rotate(rotation, point) for point in ORDER[:stage]
            )
            template_anchor = rotate(rotation, ORDER[0])
            rotated_guard = frozenset(
                rotate(rotation, point) for point in GUARD
            )
            rotated_next = rotate(rotation, canonical_next)
            for observed in points:
                displacement = minus(observed, template_anchor)
                prefix = move(template, displacement)
                if not prefix.issubset(points):
                    continue
                guard = move(rotated_guard, displacement)
                if (guard - prefix) & points:
                    continue
                candidate = plus(displacement, rotated_next)
                if candidate not in points:
                    result.setdefault(candidate, set()).add(stage)
    return {site: frozenset(stages) for site, stages in result.items()}


def actual_labeled_stage_matches(records):
    points = frozenset(records)
    result = {}
    for stage in range(1, len(ORDER) + 1):
        canonical_next = ORDER[stage] if stage < len(ORDER) else O
        for rotation in GROUP:
            template = frozenset(
                rotate(rotation, point) for point in ORDER[:stage]
            )
            template_anchor = rotate(rotation, ORDER[0])
            rotated_guard = frozenset(
                rotate(rotation, point) for point in GUARD
            )
            rotated_next = rotate(rotation, canonical_next)
            for observed in points:
                displacement = minus(observed, template_anchor)
                prefix = move(template, displacement)
                if not prefix.issubset(points):
                    continue
                labels = {records[site] for site in prefix}
                if len(labels) != 1:
                    continue
                guard = move(rotated_guard, displacement)
                if (guard - prefix) & points:
                    continue
                candidate = plus(displacement, rotated_next)
                if candidate not in points:
                    result.setdefault(candidate, set()).add(
                        (stage, next(iter(labels)))
                    )
    return {site: frozenset(matches) for site, matches in result.items()}


def histories():
    levels = [{frozenset({O})}]
    exact_partition = True
    for stage in range(1, 11):
        successors = set()
        for state in levels[-1]:
            actual = actual_stage_matches(state)
            expected = next_sites(state, stage)
            exact_partition = exact_partition and (
                frozenset(actual) == expected
                and all(found == frozenset({stage}) for found in actual.values())
            )
            successors.update(
                frozenset(set(state) | {candidate}) for candidate in actual
            )
        levels.append(successors)
    terminals = set()
    for carriers in levels[-1]:
        actual = actual_stage_matches(carriers)
        expected = next_sites(carriers, 11)
        exact_partition = exact_partition and (
            frozenset(actual) == expected
            and all(found == frozenset({11}) for found in actual.values())
        )
        terminals.update((carriers, target) for target in actual)
    return tuple(levels), frozenset(terminals), exact_partition


def degree(site, points):
    return sum(plus(site, edge) in points for edge in E)


def connected_components(records):
    unseen = set(records)
    result = []
    while unseen:
        start = unseen.pop()
        component = {start}
        frontier = [start]
        while frontier:
            current = frontier.pop()
            for edge in E:
                candidate = plus(current, edge)
                if candidate in unseen:
                    unseen.remove(candidate)
                    component.add(candidate)
                    frontier.append(candidate)
        result.append(frozenset(component))
    return tuple(result)


def parse(records, component):
    component = frozenset(component)
    if len(component) != 12:
        return None
    if len(connected_components({site: records[site] for site in component})) != 1:
        return None
    if neighborhood(component) & frozenset(records) != component:
        return None
    terminals = tuple(site for site in component if degree(site, component) == 6)
    if len(terminals) != 1:
        return None
    target = terminals[0]
    carriers = component - {target}
    payload = records[next(iter(carriers))]
    decoded = decode_payload(payload)
    if decoded is None or not all(
        matrix_equal(records[site], payload) for site in carriers
    ):
        return None
    frames = embeddings(carriers, 11)
    if len(frames) != 1:
        return None
    rotation, displacement = frames[0]
    if target != plus(displacement, rotate(rotation, O)):
        return None
    if matrix_equal(records[target], decoded.projector):
        outcome = "+"
    elif matrix_equal(records[target], decoded.complement):
        outcome = "-"
    else:
        return None
    anchor = plus(displacement, rotate(rotation, ORDER[0]))
    return anchor, target, rotation, displacement, outcome


def conjugate(value, unitary):
    return simplify(unitary * value * unitary.conjugate().T)


def neighbor_contents(records, site):
    return tuple(
        records[plus(site, edge)]
        for edge in E
        if plus(site, edge) in records
    )


def ball(radius):
    return frozenset(
        (x, y, z)
        for x in range(-radius, radius + 1)
        for y in range(-radius, radius + 1)
        for z in range(-radius, radius + 1)
        if abs(x) + abs(y) + abs(z) <= radius
    )


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

    h_value = Matrix([[1, 1], [1, 2]])
    payload = simplify(h_value + I * SX)
    control = simplify(I2 + I * SX)
    decoded = decode_payload(payload)
    decoded_control = decode_payload(control)
    p_star = trace_weight(decoded.preparation, decoded.projector)
    p_control = trace_weight(
        decoded_control.preparation, decoded_control.projector
    )
    unitaries = (
        I2,
        SX,
        simplify((SX + SZ) / sqrt(2)),
        Matrix([[1, 0], [0, I]]),
        simplify((I2 + I * SX) / sqrt(2)),
    )
    orbit_ok = True
    for unitary in unitaries:
        transformed = decode_payload(conjugate(payload, unitary))
        orbit_ok = orbit_ok and (
            transformed is not None
            and matrix_equal(
                transformed.preparation, conjugate(decoded.preparation, unitary)
            )
            and matrix_equal(
                transformed.projector, conjugate(decoded.projector, unitary)
            )
            and trace_weight(transformed.preparation, transformed.projector)
            == p_star
        )
    check(
        "independent-orbit-weight",
        decoded is not None
        and decoded_control is not None
        and p_star == Q(13, 14)
        and trace_weight(decoded.preparation, decoded.complement) == Q(1, 14)
        and p_control == Q(1, 2)
        and orbit_ok,
        "an independent decoder route reproduces both orbit weights and five exact conjugation checks",
    )

    levels, terminal_pairs, exact_partition = histories()
    level_counts = tuple(len(level) for level in levels)
    unfinished_delimiters = sum(
        sum(degree(site, state) == 6 for site in state)
        for level in levels
        for state in level
    )
    terminal_delimiters = tuple(
        sum(degree(site, set(carriers) | {target}) == 6 for site in set(carriers) | {target})
        for carriers, target in terminal_pairs
    )
    check(
        "independent-terminal-delimiter",
        len(GROUP) == 24
        and level_counts == (1, 6, 36, 72, 60, 120, 120, 120, 120, 120, 120)
        and sum(level_counts) == 895
        and exact_partition
        and len(terminal_pairs) == 120
        and unfinished_delimiters == 0
        and set(terminal_delimiters) == {1},
        "the all-stage reconstruction independently gives 895 unfinished states and one delimiter in all 120 terminals",
    )

    parse_results = []
    plus_records = []
    for carriers, target in terminal_pairs:
        for outcome, endpoint in (
            ("+", decoded.projector),
            ("-", decoded.complement),
        ):
            records = {site: payload for site in carriers}
            records[target] = endpoint
            result = parse(records, frozenset(records))
            parse_results.append(
                result is not None
                and result[0] in carriers
                and result[1] == target
                and result[4] == outcome
            )
            if outcome == "+":
                plus_records.append(records)
    check(
        "independent-exhaustive-parser",
        len(parse_results) == 240 and all(parse_results),
        "an independently written parser accepts every placement and both endpoints without a history label",
    )

    translation_classes = {}
    for carriers, target in terminal_pairs:
        completed = frozenset(set(carriers) | {target})
        minimum = min(completed)
        normalized = frozenset(minus(site, minimum) for site in completed)
        translation_classes.setdefault(normalized, set()).add(minus(O, minimum))
    check(
        "independent-causal-root-ambiguity",
        len(translation_classes) == 24
        and {len(offsets) for offsets in translation_classes.values()} == {5},
        "translation quotient independently leaves five possible historical root offsets in each of 24 static frames",
    )

    sample = plus_records[0]
    component = frozenset(sample)
    sample_result = parse(sample, component)
    shift = (7, -4, 3)
    shifted = {plus(site, shift): value for site, value in sample.items()}
    shifted_result = parse(shifted, frozenset(shifted))
    covariance_ok = (
        sample_result is not None
        and shifted_result is not None
        and shifted_result[0] == plus(sample_result[0], shift)
        and shifted_result[1] == plus(sample_result[1], shift)
    )
    for rotation in GROUP:
        rotated = {rotate(rotation, site): value for site, value in sample.items()}
        result = parse(rotated, frozenset(rotated))
        covariance_ok = covariance_ok and (
            result is not None
            and result[0] == rotate(rotation, sample_result[0])
            and result[1] == rotate(rotation, sample_result[1])
            and result[4] == "+"
        )
    for unitary in unitaries:
        transformed = {
            site: conjugate(value, unitary) for site, value in sample.items()
        }
        result = parse(transformed, frozenset(transformed))
        covariance_ok = covariance_ok and (
            result is not None
            and result[0] == sample_result[0]
            and result[1] == sample_result[1]
            and result[4] == "+"
        )
    check(
        "independent-parser-covariance",
        covariance_ok,
        "translations, all signed-permutation frames, and five basis changes commute with the independent parser",
    )

    hostile_site = min(neighborhood(component) - component)
    hostile = dict(sample)
    hostile[hostile_site] = control
    hostile_component = next(
        found for found in connected_components(hostile) if component & found
    )
    pair_shift = (10, 0, 0)
    pair = dict(sample)
    pair.update({plus(site, pair_shift): value for site, value in sample.items()})
    pair_components = connected_components(pair)
    pair_results = tuple(parse(pair, found) for found in pair_components)
    check(
        "independent-guard-and-ownership",
        parse(hostile, hostile_component) is None
        and len(pair_components) == 2
        and all(result is not None for result in pair_results)
        and {result[1] for result in pair_results}
        == {sample_result[1], plus(sample_result[1], pair_shift)},
        "one adjacent hostile Record is rejected while distance-ten formation roots yield two terminal-owned trials",
    )

    sequence = [O]
    state = frozenset(sequence)
    sequence_legal = True
    for stage in range(1, 11):
        choices = next_sites(state, stage)
        sequence_legal = sequence_legal and bool(choices)
        chosen = min(choices)
        sequence.append(chosen)
        state = frozenset(sequence)
    terminal_choices = next_sites(state, 11)
    sequence_legal = sequence_legal and len(terminal_choices) == 1
    sequence.append(next(iter(terminal_choices)))
    records = {}
    for index, site in enumerate(sequence):
        if index < 11:
            if index:
                sequence_legal = sequence_legal and content_mass(
                    local_law(neighbor_contents(records, site)), payload
                ) == 1
            records[site] = payload
        else:
            read = local_law(neighbor_contents(records, site))
            sequence_legal = sequence_legal and (
                content_mass(read, decoded.projector) == Q(13, 14)
                and content_mass(read, decoded.complement) == Q(1, 14)
            )
            records[site] = decoded.projector
    ball_nine = ball(9)
    ball_size = len(ball_nine)
    event_count = len(sequence)
    tau = symbols("tau", positive=True)
    delta = tau / event_count
    designated_slots = (exp(-delta) * delta) ** event_count
    quiet_remainder = exp(-(ball_size * tau - event_count * delta))
    witness = simplify(designated_slots * quiet_remainder)
    check(
        "independent-positive-cylinder",
        sequence_legal
        and event_count == len(set(sequence)) == 12
        and max(norm(site) for site in sequence) <= 4
        and ball_size == 1159
        and witness == exp(-1159 * tau) * (tau / 12) ** 12
        and bool(witness.subs(tau, Q(12, 1159)).is_positive)
        and not (ball_nine & move(ball_nine, (19, 0, 0))),
        "an independently selected legal order has the same positive twelve-slot witness and disjoint B9 control",
    )

    intensity = symbols("intensity", positive=True)
    n = symbols("n", integer=True, positive=True)
    volume = (2 * n + 1) ** 3
    boundary = simplify(volume - (2 * n - 1) ** 3)
    check(
        "independent-frequency-algebra",
        simplify((intensity * p_star) / intensity) == p_star
        and p_star == Q(13, 14)
        and limit(boundary / volume, n, oo) == 0,
        "the independently expressed marked/unmarked ratio is 13/14 on a cubic Folner sequence",
    )

    purity = simplify((decoded.preparation**2).trace())
    control_purity = simplify((decoded_control.preparation**2).trace())
    aggregate = simplify((p_star + p_control) / 2)
    selected = simplify(p_star / (p_star + (1 - p_star) / 2))
    check(
        "independent-selection-mutations",
        purity == Q(47, 49)
        and control_purity == Q(1, 2)
        and aggregate == Q(5, 7)
        and selected == Q(26, 27),
        "orbit mixing and outcome-dependent thinning independently move the apparent weights to 5/7 and 26/27",
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
    paths_legal = True
    for path in (x_path, y_path):
        state = frozenset({path[0]})
        for stage, candidate in enumerate(path[1:], 1):
            paths_legal = paths_legal and candidate in next_sites(state, stage)
            state = frozenset(set(state) | {candidate})
    collision = {x_path[0]: "A", y_path[0]: "B"}
    joint_reachable = True
    for stage, site in enumerate(x_path[1:9], start=1):
        current = actual_labeled_stage_matches(collision)
        joint_reachable = joint_reachable and (stage, "A") in current.get(
            site, frozenset()
        )
        collision[site] = "A"
    for stage, site in enumerate(y_path[1:9], start=1):
        current = actual_labeled_stage_matches(collision)
        joint_reachable = joint_reachable and (stage, "B") in current.get(
            site, frozenset()
        )
        collision[site] = "B"
    frontier = actual_labeled_stage_matches(collision)

    def sites_for(label, found):
        return {
            site
            for site, matches in found.items()
            if any(match_label == label for _stage, match_label in matches)
        }

    x_ten, y_ten = x_path[9], y_path[9]
    after_x = dict(collision)
    after_x[x_ten] = "A"
    check(
        "independent-radius-eight-mutation",
        norm(minus(x_path[0], y_path[0])) == 9
        and paths_legal
        and joint_reachable
        and sites_for("A", frontier) == {x_ten}
        and sites_for("B", frontier) == {y_ten}
        and norm(minus(x_ten, y_ten)) == 1
        and not sites_for("B", actual_labeled_stage_matches(after_x)),
        "the independent all-prefix matcher reproduces the distance-nine P9/P9 jam",
    )

    note_text = NOTE.read_text(encoding="utf-8")
    source_text = Path(__file__).read_text(encoding="utf-8")
    check(
        "independent-source-contract",
        "24 translation-normalized frames" in note_text
        and "five possible seed offsets" in note_text
        and "spatially stationary and ergodic" in note_text
        and "No Minimal Axioms edit" in note_text
        and "N8 — Cross-Cycle Echo" in note_text
        and ("from nn_record_spatial_trial_" + "ensemble_2026_08_23")
        not in source_text,
        "the independent route binds the corrected history boundary, theorem scope, axiom fence, and N1-N8 packet",
    )

    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return int(failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
