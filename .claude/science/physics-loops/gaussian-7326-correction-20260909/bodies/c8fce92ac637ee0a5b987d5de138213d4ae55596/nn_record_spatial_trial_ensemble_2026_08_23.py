#!/usr/bin/env python3
"""Exact finite checks for the spatial Record trial-ensemble theorem."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from sympy import I, Matrix, Rational as Q, exp, limit, oo, simplify, sqrt, symbols

from nn_record_homogeneous_payload_self_hosting_writer_2026_08_22 import (
    APPEND_ORDER,
    DIRECTIONS,
    I2,
    SX,
    SZ,
    add,
    content_mass,
    decode_payload,
    local_law,
    matrix_equal,
    recorded_neighbor_contents,
    trace_weight,
)
from nn_record_isolated_shape_compiler_2026_08_22 import (
    BALL_OFFSETS,
    ROOT_EXCLUSION_RADIUS,
    ROTATIONS,
    ROTATED_STAGES,
    TARGET,
    actual_growth_frontier,
    all_stage_states,
    congruent_to_full_block,
    formation_rate,
    geometric_frontier,
    halo,
    l1_distance,
    prefix_embeddings,
    root_eligible,
    rotate_site,
    subtract,
    transform,
    translated_records,
)


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/NN_RECORD_SPATIAL_TRIAL_ENSEMBLE_BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "docs/NN_RECORD_ISOLATED_SHAPE_COMPILER_BOUNDED_THEOREM_NOTE_2026-08-22.md",
    "scripts/nn_record_isolated_shape_compiler_2026_08_22.py",
    "docs/NN_RECORD_HOMOGENEOUS_PAYLOAD_SELF_HOSTING_WRITER_"
    "BOUNDED_THEOREM_NOTE_2026-08-22.md",
    "scripts/nn_record_homogeneous_payload_self_hosting_writer_2026_08_22.py",
)

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "NN_RECORD_SPATIAL_TRIAL_ENSEMBLE_BOUNDED_THEOREM_NOTE_2026-08-23.md"
)

H_STAR = Matrix([[1, 1], [1, 2]])
A_STAR = simplify(H_STAR + I * SX)
B_STAR = simplify(I2 + I * SX)
STAR_DATA = decode_payload(A_STAR)
P_STAR = (
    trace_weight(STAR_DATA.preparation, STAR_DATA.projector)
    if STAR_DATA is not None
    else None
)


@dataclass(frozen=True)
class HaarOrbitLaw:
    """The pushforward of normalized Haar measure by U -> U A_* U^dagger."""

    representative: Matrix


@dataclass(frozen=True)
class TrialCertificate:
    anchor: tuple[int, int, int]
    target: tuple[int, int, int]
    rotation_index: int
    displacement: tuple[int, int, int]
    outcome: str
    payload: Matrix


def trial_content_law(neighbors):
    """Block 33's kernel with its empty branch replaced by one Haar orbit."""
    if not neighbors:
        return HaarOrbitLaw(A_STAR)
    return local_law(neighbors)


def conjugate(value: Matrix, unitary: Matrix) -> Matrix:
    return simplify(unitary * value * unitary.conjugate().T)


def connected_components(records):
    unseen = set(records)
    components = []
    while unseen:
        start = unseen.pop()
        component = {start}
        frontier = [start]
        while frontier:
            site = frontier.pop()
            for direction in DIRECTIONS:
                neighbor = add(site, direction)
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    component.add(neighbor)
                    frontier.append(neighbor)
        components.append(frozenset(component))
    return tuple(components)


def occupied_degree(site, occupied) -> int:
    return sum(add(site, direction) in occupied for direction in DIRECTIONS)


def parse_trial_component(records, component):
    """Decode one guarded immutable component using Records only."""
    component = frozenset(component)
    if len(component) != 12 or not congruent_to_full_block(component):
        return None
    if len(connected_components({site: records[site] for site in component})) != 1:
        return None
    if (halo(component) & frozenset(records)) != component:
        return None
    degree_six = tuple(
        site for site in component if occupied_degree(site, component) == 6
    )
    if len(degree_six) != 1:
        return None
    target = degree_six[0]
    carriers = component - {target}
    payload = records[next(iter(carriers))]
    if decode_payload(payload) is None or not all(
        matrix_equal(records[site], payload) for site in carriers
    ):
        return None
    embeddings = prefix_embeddings(carriers, 11)
    if len(embeddings) != 1:
        return None
    rotation_index, displacement = embeddings[0]
    predicted_target = add(
        displacement, ROTATED_STAGES[11][rotation_index][4]
    )
    if target != predicted_target:
        return None
    decoded = decode_payload(payload)
    if matrix_equal(records[target], decoded.projector):
        outcome = "+"
    elif matrix_equal(records[target], decoded.complement):
        outcome = "-"
    else:
        return None
    anchor = transform(ROTATIONS[rotation_index], displacement, APPEND_ORDER[0])
    return TrialCertificate(
        anchor=anchor,
        target=target,
        rotation_index=rotation_index,
        displacement=displacement,
        outcome=outcome,
        payload=payload,
    )


def rotated_records(records, rotation):
    return {rotate_site(rotation, site): content for site, content in records.items()}


def conjugated_records(records, unitary):
    return {site: conjugate(content, unitary) for site, content in records.items()}


CANONICAL_CARRIER_PATH = (
    (0, 0, 0),
    (1, 0, 0),
    (0, 1, 0),
    (2, 0, 0),
    (2, 1, 0),
    (2, 1, -1),
    (1, 1, -1),
    (2, 1, 1),
    (1, 1, 1),
    (2, 2, 0),
    (1, 2, 0),
)


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

    decoded_star = decode_payload(A_STAR)
    decoded_control = decode_payload(B_STAR)
    check(
        "selected-orbit-fixture",
        isinstance(trial_content_law(tuple()), HaarOrbitLaw)
        and decoded_star is not None
        and decoded_control is not None
        and P_STAR == Q(13, 14)
        and trace_weight(decoded_star.preparation, decoded_star.complement) == Q(1, 14)
        and trace_weight(decoded_control.preparation, decoded_control.projector) == Q(1, 2),
        "the selected conjugacy orbit has invariant 13/14 and 1/14 weights; a typed control orbit has 1/2",
    )

    exact_unitaries = (
        I2,
        SX,
        simplify((SX + SZ) / sqrt(2)),
        Matrix([[1, 0], [0, I]]),
        simplify((I2 + I * SX) / sqrt(2)),
    )
    orbit_covariant = True
    for unitary in exact_unitaries:
        transformed = conjugate(A_STAR, unitary)
        decoded = decode_payload(transformed)
        orbit_covariant = orbit_covariant and (
            matrix_equal(simplify(unitary * unitary.conjugate().T), I2)
            and decoded is not None
            and matrix_equal(
                decoded.preparation, conjugate(decoded_star.preparation, unitary)
            )
            and matrix_equal(
                decoded.projector, conjugate(decoded_star.projector, unitary)
            )
            and trace_weight(decoded.preparation, decoded.projector) == P_STAR
        )
    check(
        "internal-orbit-covariance",
        orbit_covariant,
        "five exact basis changes conjugate both decoded event factors and leave the orbit weight at 13/14",
    )

    stages, exact_partition, completed_quiet, unfinished_count = all_stage_states(
        A_STAR
    )
    terminal_pairs = tuple(
        (carriers, next(iter(geometric_frontier(carriers, 11))))
        for carriers in stages[-2]
    )
    unfinished_delimiters = sum(
        sum(occupied_degree(site, state) == 6 for site in state)
        for level in stages[:-1]
        for state in level
    )
    terminal_delimiters = tuple(
        sum(
            occupied_degree(site, set(carriers) | {target}) == 6
            for site in set(carriers) | {target}
        )
        for carriers, target in terminal_pairs
    )
    check(
        "record-only-terminal-delimiter",
        exact_partition
        and completed_quiet
        and unfinished_count == 895
        and unfinished_delimiters == 0
        and len(terminal_pairs) == 120
        and set(terminal_delimiters) == {1},
        "zero of 895 unfinished shapes and exactly one site in each of 120 terminals has six occupied neighbors",
    )

    parsed = []
    terminal_records = []
    for carriers, target in terminal_pairs:
        for outcome, endpoint in (
            ("+", decoded_star.projector),
            ("-", decoded_star.complement),
        ):
            records = {site: A_STAR for site in carriers}
            records[target] = endpoint
            certificate = parse_trial_component(records, frozenset(records))
            parsed.append(
                certificate is not None
                and certificate.anchor in carriers
                and certificate.target == target
                and certificate.outcome == outcome
            )
            terminal_records.append(records)
    check(
        "exhaustive-record-only-parser",
        len(parsed) == 240 and all(parsed),
        "all 120 placements times both outcomes yield one geometric anchor, frame, target, payload, and branch certificate",
    )

    translation_classes = {}
    for completed in stages[-1]:
        minimum = min(completed)
        normalized = frozenset(subtract(site, minimum) for site in completed)
        actual_root_offset = subtract(TARGET, minimum)
        translation_classes.setdefault(normalized, set()).add(actual_root_offset)
    check(
        "causal-root-erasure-control",
        len(translation_classes) == 24
        and {len(offsets) for offsets in translation_classes.values()} == {5},
        "each of 24 static frame classes is compatible with five translated causal-root histories, so the parser does not invent a seed label",
    )

    sample = terminal_records[0]
    sample_component = frozenset(sample)
    hostile_site = min(halo(sample_component) - sample_component)
    hostile = dict(sample)
    hostile[hostile_site] = B_STAR
    hostile_component = next(
        component
        for component in connected_components(hostile)
        if sample_component & component
    )
    unfinished_parser_rejects = all(
        parse_trial_component(
            {site: A_STAR for site in state}, state
        ) is None
        for level in stages[:-1]
        for state in level
    )
    check(
        "delimiter-false-positive-controls",
        unfinished_parser_rejects
        and parse_trial_component(hostile, hostile_component) is None,
        "the decoder rejects every unfinished history and a completed-looking block with an occupied nearest-neighbor guard",
    )

    displacement = (7, -4, 3)
    translated = translated_records(sample, displacement)
    translated_certificate = parse_trial_component(translated, frozenset(translated))
    spatial_covariant = translated_certificate is not None and (
        translated_certificate.anchor
        == add(parse_trial_component(sample, sample_component).anchor, displacement)
        and translated_certificate.target
        == add(parse_trial_component(sample, sample_component).target, displacement)
    )
    for rotation in ROTATIONS:
        rotated = rotated_records(sample, rotation)
        certificate = parse_trial_component(rotated, frozenset(rotated))
        spatial_covariant = spatial_covariant and (
            certificate is not None
            and certificate.anchor
            == rotate_site(
                rotation, parse_trial_component(sample, sample_component).anchor
            )
            and certificate.outcome == "+"
        )
    basis_covariant = True
    for unitary in exact_unitaries:
        transformed = conjugated_records(sample, unitary)
        certificate = parse_trial_component(transformed, frozenset(transformed))
        basis_covariant = basis_covariant and (
            certificate is not None
            and certificate.anchor
            == parse_trial_component(sample, sample_component).anchor
            and certificate.outcome == "+"
        )
    check(
        "certificate-covariance",
        spatial_covariant and basis_covariant,
        "translation, all 24 proper rotations, and five internal basis changes commute with Record parsing",
    )

    second_displacement = (10, 0, 0)
    pair = dict(sample)
    pair.update(translated_records(sample, second_displacement))
    pair_components = connected_components(pair)
    pair_certificates = tuple(
        parse_trial_component(pair, component) for component in pair_components
    )
    check(
        "unique-two-trial-ownership",
        len(pair_components) == 2
        and all(certificate is not None for certificate in pair_certificates)
        and {certificate.target for certificate in pair_certificates}
        == {
            parse_trial_component(sample, sample_component).target,
            add(
                parse_trial_component(sample, sample_component).target,
                second_displacement,
            ),
        },
        "two distance-ten formation roots leave two nonadjacent components and exactly one terminal-indexed certificate per component",
    )

    canonical_target = next(
        iter(geometric_frontier(frozenset(CANONICAL_CARRIER_PATH), 11))
    )
    canonical_sequence = CANONICAL_CARRIER_PATH + (canonical_target,)
    sequence_legal = root_eligible({}, canonical_sequence[0])
    sequence_records = {}
    for index, site in enumerate(canonical_sequence):
        if index == 0:
            sequence_legal = sequence_legal and isinstance(
                trial_content_law(recorded_neighbor_contents(sequence_records, site)),
                HaarOrbitLaw,
            )
            sequence_records[site] = A_STAR
        elif index < 11:
            sequence_legal = sequence_legal and (
                formation_rate(sequence_records, site) == 1
                and content_mass(
                    trial_content_law(
                        recorded_neighbor_contents(sequence_records, site)
                    ),
                    A_STAR,
                )
                == 1
            )
            sequence_records[site] = A_STAR
        else:
            read = trial_content_law(
                recorded_neighbor_contents(sequence_records, site)
            )
            sequence_legal = sequence_legal and (
                formation_rate(sequence_records, site) == 1
                and content_mass(read, decoded_star.projector) == P_STAR
                and content_mass(read, decoded_star.complement) == Q(1, 14)
            )
            sequence_records[site] = decoded_star.projector
    event_count = len(canonical_sequence)
    tau = symbols("tau", positive=True)
    delta = tau / event_count
    ball_size = len(BALL_OFFSETS[ROOT_EXCLUSION_RADIUS])
    designated_slots = (exp(-delta) * delta) ** event_count
    quiet_remainder = exp(-(ball_size * tau - event_count * delta))
    cylinder_probability = simplify(designated_slots * quiet_remainder)
    check(
        "positive-fixed-time-completion-cylinder",
        sequence_legal
        and event_count == len(set(canonical_sequence)) == 12
        and max(l1_distance(site) for site in canonical_sequence) <= 4
        and ball_size == 1159
        and cylinder_probability
        == exp(-1159 * tau) * (tau / 12) ** 12
        and bool(cylinder_probability.subs(tau, Q(12, 1159)).is_positive),
        "twelve ordered slots inside B9 give the exact positive witness exp(-1159*tau)(tau/12)^12",
    )

    ball_nine = set(BALL_OFFSETS[ROOT_EXCLUSION_RADIUS])
    shifted_ball = {add(site, (19, 0, 0)) for site in ball_nine}
    check(
        "disjoint-iid-cylinder-control",
        not (ball_nine & shifted_ball)
        and 2 * ROOT_EXCLUSION_RADIUS < 19,
        "B9 fields centered on 19 Z^3 are disjoint raw-clock controls; the disclosed sparse grid is not the headline corpus",
    )

    rho = symbols("rho", positive=True)
    n = symbols("n", integer=True, positive=True)
    cube_volume = (2 * n + 1) ** 3
    cube_boundary = simplify(cube_volume - (2 * n - 1) ** 3)
    check(
        "stationary-factor-frequency-algebra",
        simplify((rho * P_STAR) / rho) == P_STAR
        and simplify((rho * (1 - P_STAR)) / rho) == Q(1, 14)
        and limit(cube_boundary / cube_volume, n, oo) == 0,
        "positive trial intensity cancels in the marked/unmarked ratio and cubic boundary-to-volume tends to zero",
    )

    purity_star = simplify((decoded_star.preparation**2).trace())
    purity_control = simplify((decoded_control.preparation**2).trace())
    aggregate = simplify((P_STAR + Q(1, 2)) / 2)
    check(
        "mixed-preparation-typing-mutation",
        purity_star == Q(47, 49)
        and purity_control == Q(1, 2)
        and aggregate == Q(5, 7)
        and aggregate not in (P_STAR, Q(1, 2)),
        "mixing two Record-visible orbit types yields 5/7, so untyped aggregation is neither component probability",
    )

    biased_selection = simplify(P_STAR / (P_STAR + (1 - P_STAR) / 2))
    check(
        "outcome-dependent-thinning-mutation",
        biased_selection == Q(26, 27) and biased_selection != P_STAR,
        "retaining minus outcomes at half the plus rate moves 13/14 to 26/27, exposing the pre-outcome-selection gate",
    )

    x_path = CANONICAL_CARRIER_PATH
    y_path = (
        (5, 4, 0),
        (4, 4, 0),
        (5, 3, 0),
        (3, 4, 0),
        (3, 3, 0),
        (3, 3, -1),
        (4, 3, -1),
        (3, 3, 1),
        (4, 3, 1),
        (3, 2, 0),
        (4, 2, 0),
    )
    payload_b = simplify(2 * A_STAR)
    collision_records = {x_path[0]: A_STAR, y_path[0]: payload_b}
    joint_reachable = True
    for stage, candidate in enumerate(x_path[1:9], start=1):
        current = actual_growth_frontier(collision_records)
        joint_reachable = joint_reachable and any(
            match[0] == stage and matrix_equal(match[3], A_STAR)
            for match in current.get(candidate, ())
        )
        collision_records[candidate] = A_STAR
    for stage, candidate in enumerate(y_path[1:9], start=1):
        current = actual_growth_frontier(collision_records)
        joint_reachable = joint_reachable and any(
            match[0] == stage and matrix_equal(match[3], payload_b)
            for match in current.get(candidate, ())
        )
        collision_records[candidate] = payload_b
    collision_frontier = actual_growth_frontier(collision_records)

    def labeled_sites(frontier, payload):
        return {
            site
            for site, matches in frontier.items()
            if any(matrix_equal(match[3], payload) for match in matches)
        }

    x_ten, y_ten = x_path[9], y_path[9]
    after_x = dict(collision_records)
    after_x[x_ten] = A_STAR
    check(
        "radius-eight-collision-mutation",
        l1_distance(x_path[0], y_path[0]) == 9
        and root_eligible({x_path[0]: A_STAR}, y_path[0], radius=8)
        and joint_reachable
        and labeled_sites(collision_frontier, A_STAR) == {x_ten}
        and labeled_sites(collision_frontier, payload_b) == {y_ten}
        and l1_distance(x_ten, y_ten) == 1
        and not labeled_sites(actual_growth_frontier(after_x), payload_b),
        "deleting one exclusion layer restores the exact P9/P9 fork where one writer jams the other",
    )

    note_text = NOTE.read_text(encoding="utf-8")
    required_fragments = (
        "fixed abstract time",
        "Record-only",
        "Haar-conjugacy orbit",
        "13/14",
        "exp(-1159 tau)(tau/12)^12",
        "spatially stationary and ergodic",
        "not temporal recurrence",
        "PR #7318",
        "TOE percentages remain unchanged",
        "No Minimal Axioms edit",
        "N1 — Alternative Route Enumeration",
        "N8 — Cross-Cycle Echo",
    )
    check(
        "source-contract",
        all(fragment in note_text for fragment in required_fragments),
        "the note binds fixed-time scope, Record parsing, orbit selection, ergodicity, pincer, axiom, score, and N1-N8 boundaries",
    )

    print("per_element: two orbit representatives, five basis changes, and both binary endpoints are checked")
    print("per_site: every terminal delimiter, geometric anchor, guard, and collision frontier is checked")
    print("per_mode: fixed abstract time and spatial Følner averaging are checked; temporal recurrence is excluded")
    print("per_block: all 895 unfinished and 240 completed outcome components are checked")
    print("lattice_wide: stationarity/ergodicity is an analytic factor theorem; finite runners test its local hypotheses and falsifiers")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return int(failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
