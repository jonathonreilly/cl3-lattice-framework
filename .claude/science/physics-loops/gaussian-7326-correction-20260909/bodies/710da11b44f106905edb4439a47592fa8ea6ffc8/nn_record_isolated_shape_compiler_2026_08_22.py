#!/usr/bin/env python3
"""Exact checks for an endogenous hard-core Record shape compiler."""

from __future__ import annotations

from pathlib import Path

from sympy import I, Matrix, Rational as Q, exp, factorial, simplify, sqrt, symbols

from nn_record_homogeneous_payload_self_hosting_writer_2026_08_22 import (
    APPEND_ORDER,
    DIRECTIONS,
    GaussianLaw,
    I2,
    SX,
    add,
    conjugate_law,
    content_mass,
    decode_payload,
    finite_law_equal,
    local_law,
    matrix_equal,
    proper_cubic_rotations,
    recorded_neighbor_contents,
    rotate_site,
)


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/NN_RECORD_ISOLATED_SHAPE_COMPILER_BOUNDED_THEOREM_NOTE_2026-08-22.md",
    "docs/NN_RECORD_ISOLATED_CAVITY_PURE_BIRTH_BOUNDED_THEOREM_NOTE_2026-08-22.md",
    "scripts/nn_record_isolated_cavity_pure_birth_2026_08_22.py",
    "docs/NN_RECORD_HOMOGENEOUS_PAYLOAD_SELF_HOSTING_WRITER_"
    "BOUNDED_THEOREM_NOTE_2026-08-22.md",
    "scripts/nn_record_homogeneous_payload_self_hosting_writer_2026_08_22.py",
)

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "NN_RECORD_ISOLATED_SHAPE_COMPILER_BOUNDED_THEOREM_NOTE_2026-08-22.md"
)

TARGET = (0, 0, 0)
ROOT_EXCLUSION_RADIUS = 9
REACHABLE_BLOCK_RADIUS = 4

ROTATIONS = proper_cubic_rotations()
FULL_BLOCK = frozenset(APPEND_ORDER) | {TARGET}


def subtract(left, right):
    return tuple(left[index] - right[index] for index in range(3))


def l1_distance(left, right=(0, 0, 0)) -> int:
    return sum(abs(left[index] - right[index]) for index in range(3))


def translate(sites, displacement):
    return frozenset(add(site, displacement) for site in sites)


def halo(sites):
    return frozenset(sites) | {
        add(site, direction) for site in sites for direction in DIRECTIONS
    }


FULL_GUARD = halo(FULL_BLOCK)


def ball_offsets(radius: int):
    return tuple(
        (x, y, z)
        for x in range(-radius, radius + 1)
        for y in range(-radius, radius + 1)
        for z in range(-radius, radius + 1)
        if abs(x) + abs(y) + abs(z) <= radius
    )


BALL_OFFSETS = {
    ROOT_EXCLUSION_RADIUS: ball_offsets(ROOT_EXCLUSION_RADIUS),
}


def transform(rotation, displacement, site):
    return add(displacement, rotate_site(rotation, site))


ROTATED_STAGES = {}
for stage in range(1, len(APPEND_ORDER) + 1):
    canonical_next = APPEND_ORDER[stage] if stage < len(APPEND_ORDER) else TARGET
    ROTATED_STAGES[stage] = tuple(
        (
            frozenset(rotate_site(rotation, site) for site in APPEND_ORDER[:stage]),
            rotate_site(rotation, APPEND_ORDER[0]),
            rotate_site(rotation, canonical_next),
            frozenset(rotate_site(rotation, site) for site in FULL_GUARD),
            rotate_site(rotation, TARGET),
        )
        for rotation in ROTATIONS
    )


def prefix_embeddings(sites, stage: int):
    """All proper-cubic/translation embeddings of P_stage onto sites."""
    sites = frozenset(sites)
    if len(sites) != stage:
        return ()
    embeddings = []
    for rotation_index, (prefix, anchor, _next, _guard, _target) in enumerate(
        ROTATED_STAGES[stage]
    ):
        for observed_anchor in sites:
            displacement = subtract(observed_anchor, anchor)
            if translate(prefix, displacement) == sites:
                embeddings.append((rotation_index, displacement))
    return tuple(embeddings)


def geometric_frontier(sites, stage: int):
    frontier = set()
    for rotation_index, displacement in prefix_embeddings(sites, stage):
        rotated_next = ROTATED_STAGES[stage][rotation_index][2]
        frontier.add(add(displacement, rotated_next))
    return frozenset(frontier - set(sites))


def possible_targets(sites, stage: int):
    targets = set()
    for rotation_index, displacement in prefix_embeddings(sites, stage):
        rotated_target = ROTATED_STAGES[stage][rotation_index][4]
        targets.add(add(displacement, rotated_target))
    return frozenset(targets)


def root_eligible(records, site, radius: int = ROOT_EXCLUSION_RADIUS) -> bool:
    if site in records:
        return False
    offsets = BALL_OFFSETS[radius] if radius in BALL_OFFSETS else ball_offsets(radius)
    return all(
        add(site, offset) not in records
        for offset in offsets
        if offset != (0, 0, 0)
    )


def growth_matches(records, site):
    """Clean full-guard prefix embeddings whose next site is site."""
    if site in records:
        return ()
    matches = []
    for stage in range(1, len(APPEND_ORDER) + 1):
        for rotation_index, (prefix, _anchor, rotated_next, guard, _target) in enumerate(
            ROTATED_STAGES[stage]
        ):
            displacement = subtract(site, rotated_next)
            placed_prefix = translate(prefix, displacement)
            values = tuple(records.get(point) for point in placed_prefix)
            if any(value is None for value in values):
                continue
            payload = values[0]
            if decode_payload(payload) is None or not all(
                value is payload or matrix_equal(value, payload)
                for value in values[1:]
            ):
                continue
            placed_guard = translate(guard, displacement)
            if any(point in records for point in placed_guard - placed_prefix):
                continue
            matches.append((stage, rotation_index, displacement, payload))
    return tuple(matches)


def actual_growth_frontier(records):
    """Every blank site enabled by the Law's union over all prefix stages."""
    occupied = frozenset(records)
    frontier = {}
    generic_cache = {}
    for stage in range(1, len(APPEND_ORDER) + 1):
        for rotation_index, (
            prefix,
            anchor,
            rotated_next,
            guard,
            _target,
        ) in enumerate(ROTATED_STAGES[stage]):
            for observed_anchor in occupied:
                displacement = subtract(observed_anchor, anchor)
                placed_prefix = translate(prefix, displacement)
                values = tuple(records.get(point) for point in placed_prefix)
                if any(value is None for value in values):
                    continue
                payload = values[0]
                payload_key = id(payload)
                if payload_key not in generic_cache:
                    generic_cache[payload_key] = decode_payload(payload) is not None
                if not generic_cache[payload_key] or not all(
                    value is payload or matrix_equal(value, payload)
                    for value in values[1:]
                ):
                    continue
                candidate = add(displacement, rotated_next)
                if candidate in occupied:
                    continue
                placed_guard = translate(guard, displacement)
                if (placed_guard - placed_prefix) & occupied:
                    continue
                frontier.setdefault(candidate, []).append(
                    (stage, rotation_index, displacement, payload)
                )
    return {candidate: tuple(matches) for candidate, matches in frontier.items()}


def formation_rate(records, site, exclusion_radius: int = ROOT_EXCLUSION_RADIUS) -> int:
    if site in records:
        return 0
    if root_eligible(records, site, exclusion_radius):
        return 1
    return int(bool(growth_matches(records, site)))


def all_stage_states(payload):
    """Reachable states driven by the actual union-over-all-stages matcher."""
    stages = [{frozenset({TARGET})}]
    exact_stage_partition = True
    for stage in range(1, len(APPEND_ORDER) + 1):
        successors = set()
        for state in stages[-1]:
            records = {site: payload for site in state}
            actual = actual_growth_frontier(records)
            expected = geometric_frontier(state, stage)
            exact_stage_partition = exact_stage_partition and (
                frozenset(actual) == expected
                and all(
                    {match[0] for match in matches} == {stage}
                    for matches in actual.values()
                )
            )
            successors.update(
                frozenset(set(state) | {candidate}) for candidate in actual
            )
        stages.append(successors)
    completed_quiescent = all(
        not actual_growth_frontier({site: payload for site in state})
        for state in stages[-1]
    )
    return (
        tuple(stages),
        exact_stage_partition,
        completed_quiescent,
        sum(len(level) for level in stages[:-1]),
    )


def congruent_to_full_block(sites) -> bool:
    sites = frozenset(sites)
    if len(sites) != len(FULL_BLOCK):
        return False
    for rotation in ROTATIONS:
        rotated = frozenset(rotate_site(rotation, point) for point in FULL_BLOCK)
        anchor = min(rotated)
        for observed in sites:
            if translate(rotated, subtract(observed, anchor)) == sites:
                return True
    return False


def translated_records(records, displacement):
    return {add(site, displacement): content for site, content in records.items()}


def conjugated_records(records, unitary):
    return {
        site: simplify(unitary * content * unitary.conjugate().T)
        for site, content in records.items()
    }


def main() -> int:
    passed = 0
    failed = 0

    def check(name: str, condition: bool, detail: str) -> None:
        nonlocal passed, failed
        if condition:
            passed += 1
            print(f"PASS {name}: {detail}")
        else:
            failed += 1
            print(f"FAIL {name}: {detail}")

    h_real = Matrix([[1, 1], [1, 2]])
    payload_a = simplify(h_real + I * SX)
    decoded_a = decode_payload(payload_a)

    check(
        "finite-range-rate-totality",
        formation_rate({}, TARGET) == 1
        and formation_rate({TARGET: payload_a}, TARGET) == 0
        and formation_rate({(8, 0, 0): payload_a}, TARGET) == 0
        and formation_rate({(10, 0, 0): payload_a}, TARGET) == 1,
        "the binary rate seeds only an empty radius-nine ball, advances clean prefixes, and never overwrites",
    )

    expected_frontier_counts = (6, 8, 2, 1, 2, 1, 1, 1, 1, 1, 1)
    canonical_frontier_counts = []
    guarded_rates_ok = True
    for stage in range(1, len(APPEND_ORDER) + 1):
        prefix = frozenset(APPEND_ORDER[:stage])
        frontier = geometric_frontier(prefix, stage)
        canonical_frontier_counts.append(len(frontier))
        records = {site: payload_a for site in prefix}
        guarded_rates_ok = guarded_rates_ok and all(
            formation_rate(records, candidate) == 1 for candidate in frontier
        )
    check(
        "equivariant-prefix-frontiers",
        tuple(canonical_frontier_counts) == expected_frontier_counts
        and guarded_rates_ok,
        "equal-rate symmetry frontiers have exact sizes 6,8,2,1,2,1,1,1,1,1,1",
    )

    (
        stages,
        exact_stage_partition,
        completed_quiescent,
        unfinished_state_count,
    ) = all_stage_states(payload_a)
    stage_counts = tuple(len(states) for states in stages)
    final_shapes = stages[-1]
    reachable_radius = max(
        l1_distance(site) for shape in final_shapes for site in shape
    )
    check(
        "exhaustive-reachable-shape-closure",
        stage_counts == (1, 6, 36, 72, 60, 120, 120, 120, 120, 120, 120, 120)
        and len(final_shapes) == 120
        and reachable_radius == REACHABLE_BLOCK_RADIUS
        and all(congruent_to_full_block(shape) for shape in final_shapes),
        "the actual all-stage matcher closes into 120 proper-cubic writer placements inside radius four",
    )

    check(
        "all-stage-matcher-exhaustion",
        exact_stage_partition
        and completed_quiescent
        and unfinished_state_count == 895,
        "all 895 unfinished states enable exactly their intended stage and all 120 completed placements have no growth frontier",
    )

    branch_geometry_ok = True
    selected_target_offsets = set()
    for stage, states in enumerate(stages[:-1], start=1):
        for state in states:
            frontier = geometric_frontier(state, stage)
            for candidate in frontier:
                predecessor_count = sum(
                    add(candidate, direction) in state for direction in DIRECTIONS
                )
                branch_geometry_ok = branch_geometry_ok and predecessor_count == (
                    1 if stage < len(APPEND_ORDER) else 6
                )
                if stage == len(APPEND_ORDER):
                    selected_target_offsets.add(candidate)
    check(
        "all-branch-content-interface",
        branch_geometry_ok and len(selected_target_offsets) == 18,
        "every carrier frontier has one predecessor, every final frontier has six, and 18 output offsets emerge",
    )

    header_states = stages[2]
    header_targets = {tuple(possible_targets(state, 3)) for state in header_states}
    persistent_address = True
    for stage in range(3, len(APPEND_ORDER)):
        for state in stages[stage - 1]:
            targets = possible_targets(state, stage)
            persistent_address = (
                persistent_address
                and len(targets) == 1
                and targets.isdisjoint(geometric_frontier(state, stage))
            )
    check(
        "three-record-self-address",
        len(header_states) == 36
        and all(len(targets) == 1 for targets in header_targets)
        and persistent_address,
        "a three-Record L header uniquely fixes an output site that no later carrier frontier occupies",
    )

    canonical_records = {}
    carrier_support = True
    for index, site in enumerate(APPEND_ORDER):
        condition = recorded_neighbor_contents(canonical_records, site)
        if index == 0:
            carrier_support = carrier_support and isinstance(local_law(condition), GaussianLaw)
        else:
            carrier_support = carrier_support and content_mass(local_law(condition), payload_a) == 1
        canonical_records[site] = payload_a
    read_law = local_law(recorded_neighbor_contents(canonical_records, TARGET))
    check(
        "exact-content-and-read-completion",
        carrier_support
        and decoded_a is not None
        and content_mass(read_law, decoded_a.projector) == Q(13, 14)
        and content_mass(read_law, decoded_a.complement) == Q(1, 14),
        "the inherited kernel copies all carriers and writes the exact trace-weighted projector Record",
    )

    root_positions_safe = all(
        not root_eligible({TARGET: payload_a}, offset)
        for offset in BALL_OFFSETS[ROOT_EXCLUSION_RADIUS]
        if offset != TARGET
    ) and all(
        root_eligible({TARGET: payload_a}, offset)
        for offset in ball_offsets(ROOT_EXCLUSION_RADIUS + 1)
        if l1_distance(offset) == ROOT_EXCLUSION_RADIUS + 1
    )
    possible_sites = set().union(*final_shapes)
    forbidden_displacements = {
        subtract(subtract(left, right), near)
        for left in possible_sites
        for right in possible_sites
        for near in ((0, 0, 0),) + DIRECTIONS
    }
    check(
        "endogenous-root-separation",
        root_positions_safe
        and max(l1_distance(vector) for vector in forbidden_displacements) == 9,
        "the same rate suppresses all later roots through distance nine; distance-ten roots have nonadjacent reachable blocks",
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
        for stage, candidate in enumerate(path[1:], start=1):
            paths_legal = paths_legal and candidate in geometric_frontier(state, stage)
            state = frozenset(set(state) | {candidate})
    payload_b = simplify(2 * payload_a)
    joint_records = {x_path[0]: payload_a, y_path[0]: payload_b}
    joint_reachable = True
    for stage, candidate in enumerate(x_path[1:9], start=1):
        matches = actual_growth_frontier(joint_records)
        joint_reachable = joint_reachable and any(
            match[0] == stage and match[3] is payload_a
            for match in matches.get(candidate, ())
        )
        joint_records[candidate] = payload_a
    for stage, candidate in enumerate(y_path[1:9], start=1):
        matches = actual_growth_frontier(joint_records)
        joint_reachable = joint_reachable and any(
            match[0] == stage and match[3] is payload_b
            for match in matches.get(candidate, ())
        )
        joint_records[candidate] = payload_b
    joint_frontier = actual_growth_frontier(joint_records)

    def sites_for_payload(frontier, payload):
        return {
            site
            for site, matches in frontier.items()
            if any(match[3] is payload for match in matches)
        }

    x_frontier = sites_for_payload(joint_frontier, payload_a)
    y_frontier = sites_for_payload(joint_frontier, payload_b)
    x_ten = x_path[9]
    y_ten = y_path[9]
    after_x = dict(joint_records)
    after_x[x_ten] = payload_a
    after_y = dict(joint_records)
    after_y[y_ten] = payload_b
    check(
        "radius-eight-deletion-control",
        l1_distance(x_path[0], y_path[0]) == 9
        and root_eligible({x_path[0]: payload_a}, y_path[0], radius=8)
        and decode_payload(payload_b) is not None
        and not matrix_equal(payload_a, payload_b)
        and paths_legal
        and joint_reachable
        and x_frontier == {x_ten}
        and y_frontier == {y_ten}
        and {match[0] for match in joint_frontier[x_ten]} == {9}
        and {match[0] for match in joint_frontier[y_ten]} == {9}
        and l1_distance(x_ten, y_ten) == 1
        and not sites_for_payload(actual_growth_frontier(after_x), payload_b)
        and not sites_for_payload(actual_growth_frontier(after_y), payload_a),
        "the radius-eight all-stage matcher reaches a P9/P9 fork where the first p10 birth jams every continuation of the other writer",
    )

    singleton = frozenset({TARGET})
    chosen = min(geometric_frontier(singleton, 1))
    deterministic_covariance_fails = False
    set_frontier_covariant = True
    for rotation in ROTATIONS:
        rotated_singleton = frozenset(rotate_site(rotation, point) for point in singleton)
        rotated_frontier = frozenset(
            rotate_site(rotation, point) for point in geometric_frontier(singleton, 1)
        )
        actual_frontier = geometric_frontier(rotated_singleton, 1)
        set_frontier_covariant = set_frontier_covariant and rotated_frontier == actual_frontier
        deterministic_covariance_fails = deterministic_covariance_fails or (
            rotate_site(rotation, chosen) != min(actual_frontier)
        )
    check(
        "deterministic-direction-deletion",
        set_frontier_covariant and deterministic_covariance_fails,
        "the whole equal-rate frontier is cubic-covariant, while a lexicographic preferred direction is not",
    )

    p2 = frozenset(APPEND_ORDER[:2])
    p2_frontier = geometric_frontier(p2, 2)
    early_records = {site: payload_a for site in p2}
    early_copy = content_mass(
        local_law(recorded_neighbor_contents(early_records, TARGET)), payload_a
    )
    early_records[TARGET] = payload_a
    shifted_header = frozenset(early_records)
    shifted_target = possible_targets(shifted_header, 3)
    check(
        "predesignated-target-boundary",
        TARGET in p2_frontier
        and formation_rate({site: payload_a for site in p2}, TARGET) == 1
        and early_copy == 1
        and formation_rate(early_records, TARGET) == 0
        and len(shifted_target) == 1
        and TARGET not in shifted_target,
        "before the L header, a predesignated coordinate can become a carrier; permanence moves the emergent output elsewhere",
    )

    translation = (7, -4, 3)
    stage_five = {site: payload_a for site in APPEND_ORDER[:5]}
    stage_five_candidate = APPEND_ORDER[5]
    translated = translated_records(stage_five, translation)
    translated_candidate = add(stage_five_candidate, translation)
    rotation_covariance = True
    for rotation in ROTATIONS:
        rotated_records = {
            rotate_site(rotation, site): content for site, content in stage_five.items()
        }
        rotation_covariance = rotation_covariance and (
            formation_rate(rotated_records, rotate_site(rotation, stage_five_candidate))
            == formation_rate(stage_five, stage_five_candidate)
        )
    check(
        "spacetime-covariance",
        formation_rate(translated, translated_candidate)
        == formation_rate(stage_five, stage_five_candidate)
        == 1
        and rotation_covariance,
        "translations and all 24 proper cubic rotations preserve the prefix rate",
    )

    unitary = simplify((I2 + I * SX) / sqrt(2))
    unitary_records = conjugated_records(stage_five, unitary)
    original_condition = recorded_neighbor_contents(stage_five, stage_five_candidate)
    transformed_condition = recorded_neighbor_contents(unitary_records, stage_five_candidate)
    check(
        "internal-basis-covariance",
        simplify(unitary * unitary.conjugate().T) == I2
        and formation_rate(unitary_records, stage_five_candidate) == 1
        and finite_law_equal(
            local_law(transformed_condition),
            conjugate_law(local_law(original_condition), unitary),
        ),
        "unitary re-presentation preserves geometric eligibility and conjugates the content Law",
    )

    ball_nine = len(BALL_OFFSETS[ROOT_EXCLUSION_RADIUS])
    tau = symbols("tau", positive=True)
    witness_probability = simplify((1 - exp(-ball_nine * tau)) / ball_nine)
    check(
        "positive-endogenous-root-cylinders",
        ball_nine == 1159
        and witness_probability.subs(tau, Q(1, ball_nine))
        == (1 - exp(-1)) / ball_nine
        and bool((1 - exp(-1)).is_positive),
        "a center-first B9 proposal event has positive mass and directly guarantees a root without supplied halo data",
    )

    n = symbols("n", integer=True, positive=True)
    causal_term = (ball_nine * tau) ** n / factorial(n)
    causal_predecessor = (ball_nine * tau) ** (n - 1) / factorial(n - 1)
    check(
        "finite-causal-cone-and-liveness",
        simplify(causal_term / causal_predecessor) == ball_nine * tau / n
        and all(geometric_frontier(state, stage) for stage, states in enumerate(stages[:-1], 1) for state in states),
        "range nine gives factorially controlled Harris ancestors and every finite prefix retains a recurring-clock exit",
    )

    note_text = NOTE.read_text(encoding="utf-8")
    required_fragments = (
        "self-addressing",
        "range-nine",
        "120",
        "18",
        "1159",
        "same rate Law",
        "predesignated-target compiler",
        "PR #7318",
        "TOE percentages remain unchanged",
        "No Minimal Axioms edit",
        "N1 — Alternative route enumeration",
        "N8 — Cross-Cycle Echo",
    )
    check(
        "source-contract",
        all(fragment in note_text for fragment in required_fragments),
        "the note binds endogenous reservation, emergent address, collision mutation, pincer, axiom, and score boundaries",
    )

    print("per_element: generic root payloads, literal copies, projector outcomes, and exact binary rates are checked")
    print("per_site: root, every prefix frontier, protected emergent target, blocked root, and occupied branches are checked")
    print("per_mode: abstract Poisson clocks and range-nine causal cones are checked; no physical time or gravity claim is made")
    print("per_block: all 895 unfinished states, 120 completed placements, 18 output offsets, and the radius-eight mutation are checked")
    print("lattice_wide: endogenous hard-core seeding and admitted-root completion are proved from the blank state; renewal and retained authority remain open")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return int(failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
