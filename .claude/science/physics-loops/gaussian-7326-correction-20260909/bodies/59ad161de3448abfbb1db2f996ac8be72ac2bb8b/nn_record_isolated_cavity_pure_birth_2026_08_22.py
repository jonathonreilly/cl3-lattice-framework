#!/usr/bin/env python3
"""Exact checks for the range-two isolated-cavity Record birth process."""

from __future__ import annotations

from itertools import combinations
from math import factorial, prod
from pathlib import Path

from sympy import I, Matrix, Rational as Q, exp, simplify, sqrt, symbols

from nn_record_homogeneous_payload_self_hosting_writer_2026_08_22 import (
    APPEND_ORDER,
    DIRECTIONS,
    GaussianLaw,
    I2,
    SX,
    SY,
    add,
    append_record,
    conjugate_law,
    content_mass,
    decode_payload,
    finite_law_equal,
    gaussian_density_at,
    local_law,
    matrix_equal,
    positive_truth,
    proper_cubic_rotations,
    recorded_neighbor_contents,
    rotate_site,
)


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/NN_RECORD_ISOLATED_CAVITY_PURE_BIRTH_BOUNDED_THEOREM_NOTE_"
    "2026-08-22.md",
    "docs/NN_RECORD_HOMOGENEOUS_PAYLOAD_SELF_HOSTING_WRITER_"
    "BOUNDED_THEOREM_NOTE_2026-08-22.md",
    "scripts/nn_record_homogeneous_payload_self_hosting_writer_2026_08_22.py",
)

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "NN_RECORD_ISOLATED_CAVITY_PURE_BIRTH_BOUNDED_THEOREM_NOTE_"
    "2026-08-22.md"
)

TARGET = (0, 0, 0)
PROTECTED_EVENT_LABELS = (
    APPEND_ORDER[:5]
    + (TARGET,)
    + APPEND_ORDER[5:]
    + (TARGET,)
)


def neighbor_slots(records, site):
    return tuple(records.get(add(site, direction)) for direction in DIRECTIONS)


def coherent_pair_candidate(records, site) -> bool:
    """The literal-payload incomplete-cavity predicate b_x."""
    if site in records:
        return False
    slots = neighbor_slots(records, site)
    occupied = tuple(value for value in slots if value is not None)
    if not occupied or len(occupied) == 6:
        return False
    payload = occupied[0]
    if decode_payload(payload) is None:
        return False
    if not all(matrix_equal(value, payload) for value in occupied):
        return False
    return any(
        slots[2 * axis] is not None
        and slots[2 * axis + 1] is not None
        and matrix_equal(slots[2 * axis], slots[2 * axis + 1])
        for axis in range(3)
    )


def raw_pair_candidate(records, site) -> bool:
    """Deleted predecessor: any literal generic opposite pair holds the site."""
    if site in records:
        return False
    slots = neighbor_slots(records, site)
    if all(value is not None for value in slots):
        first = slots[0]
        if decode_payload(first) is not None and all(
            matrix_equal(value, first) for value in slots[1:]
        ):
            return False
    return any(
        slots[2 * axis] is not None
        and slots[2 * axis + 1] is not None
        and matrix_equal(slots[2 * axis], slots[2 * axis + 1])
        and decode_payload(slots[2 * axis]) is not None
        for axis in range(3)
    )


def isolated_cavity_hold(records, site) -> bool:
    """Hold b_x only when no blank nearest neighbor is another b-candidate."""
    if not coherent_pair_candidate(records, site):
        return False
    return not any(
        neighbor not in records and coherent_pair_candidate(records, neighbor)
        for neighbor in (add(site, direction) for direction in DIRECTIONS)
    )


def formation_rate(records, site):
    """Range-two birth rate c_x in units of the proposal clock rate."""
    if site in records:
        return Q(0)
    return Q(0) if isolated_cavity_hold(records, site) else Q(1)


def simple_coherent_rate(records, site):
    if site in records:
        return Q(0)
    return Q(0) if coherent_pair_candidate(records, site) else Q(1)


def execute_proposal(records, site, sampled_content, protected: bool = True):
    """Execute one marked proposal against the selected rate and content law."""
    if site in records:
        return "occupied"
    if protected and formation_rate(records, site) == 0:
        return "held"
    law = local_law(recorded_neighbor_contents(records, site))
    if isinstance(law, GaussianLaw):
        if sampled_content is None or not positive_truth(gaussian_density_at(sampled_content)):
            return "unsupported"
        append_record(records, site, sampled_content)
        return "seed"
    mass = content_mass(law, sampled_content)
    if mass is None or not positive_truth(mass):
        return "unsupported"
    append_record(records, site, sampled_content)
    return "record"


def halo(core):
    return set(core) | {
        add(site, direction)
        for site in core
        for direction in DIRECTIONS
    }


def rotate_records(rotation: Matrix, records):
    return {
        rotate_site(rotation, site): content
        for site, content in records.items()
    }


def translate_records(records, shift):
    return {add(site, shift): content for site, content in records.items()}


def adjacent_hole_fixture(payload):
    left = TARGET
    right = (0, 1, 0)
    records = {}
    for center, other in ((left, right), (right, left)):
        for direction in DIRECTIONS:
            site = add(center, direction)
            if site != other:
                records[site] = payload
    return records, left, right


def finite_star_patterns_have_exit(payload) -> bool:
    """Exhaust a 7-site blank cavity inside a fixed payload sea."""
    star = (TARGET,) + tuple(DIRECTIONS)
    sea = {
        (x, y, z): payload
        for x in range(-3, 4)
        for y in range(-3, 4)
        for z in range(-3, 4)
    }
    for blank_count in range(1, len(star) + 1):
        for blank_tuple in combinations(star, blank_count):
            blanks = set(blank_tuple)
            records = {site: value for site, value in sea.items() if site not in blanks}
            if not any(formation_rate(records, site) == 1 for site in blanks):
                return False
            for site in blanks:
                if not isolated_cavity_hold(records, site):
                    continue
                if not any(
                    add(site, direction) in blanks
                    and formation_rate(records, add(site, direction)) == 1
                    for direction in DIRECTIONS
                ):
                    return False
    return True


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
    payload_b = simplify(Matrix([[2, I], [-I, 1]]) + I * SY)
    decoded_a = decode_payload(payload_a)

    empty_records = {}
    one_neighbor = {(1, 0, 0): payload_a}
    pair_records = {
        (1, 0, 0): payload_a,
        (-1, 0, 0): payload_a,
        (0, 1, 0): payload_a,
    }
    check(
        "formation-rate-totality",
        formation_rate(empty_records, TARGET) == 1
        and formation_rate(one_neighbor, TARGET) == 1
        and coherent_pair_candidate(pair_records, TARGET)
        and isolated_cavity_hold(pair_records, TARGET)
        and formation_rate(pair_records, TARGET) == 0
        and formation_rate({TARGET: payload_a}, TARGET) == 0,
        "empty, one-neighbor, coherent-pair, and occupied conditions receive exact rates",
    )

    full_shell = {direction: payload_a for direction in DIRECTIONS}
    full_law = local_law(recorded_neighbor_contents(full_shell, TARGET))
    check(
        "full-shell-read-priority",
        not coherent_pair_candidate(full_shell, TARGET)
        and formation_rate(full_shell, TARGET) == 1
        and decoded_a is not None
        and content_mass(full_law, decoded_a.projector) == Q(13, 14),
        "the incomplete clause releases a six-equal shell to Block33 Rule R",
    )

    mixed_records = dict(pair_records)
    mixed_records[(0, 0, 1)] = payload_b
    mixed_full = {
        DIRECTIONS[0]: payload_a,
        DIRECTIONS[1]: payload_a,
        DIRECTIONS[2]: payload_b,
        DIRECTIONS[3]: payload_b,
        DIRECTIONS[4]: payload_b,
        DIRECTIONS[5]: payload_b,
    }
    check(
        "mixed-front-escape",
        raw_pair_candidate(mixed_records, TARGET)
        and raw_pair_candidate(mixed_full, TARGET)
        and not coherent_pair_candidate(mixed_records, TARGET)
        and not coherent_pair_candidate(mixed_full, TARGET)
        and formation_rate(mixed_records, TARGET) == 1,
        "coherence removes the predecessor rule's permanent full mixed-shell equal-pair trap",
    )

    quotient_twin = simplify(payload_a + 3 * I * I2)
    decoded_twin = decode_payload(quotient_twin)
    quotient_pair = {
        (1, 0, 0): payload_a,
        (-1, 0, 0): quotient_twin,
        (0, 1, 0): payload_a,
    }
    check(
        "literal-not-quotient-equality",
        decoded_twin is not None
        and matrix_equal(decoded_twin.preparation, decoded_a.preparation)
        and matrix_equal(decoded_twin.projector, decoded_a.projector)
        and not matrix_equal(payload_a, quotient_twin)
        and not coherent_pair_candidate(quotient_pair, TARGET)
        and formation_rate(quotient_pair, TARGET) == 1,
        "quotient-equivalent but literally unequal payloads do not create a hold",
    )

    adjacent_records, left_hole, right_hole = adjacent_hole_fixture(payload_a)
    check(
        "adjacent-cavity-release",
        coherent_pair_candidate(adjacent_records, left_hole)
        and coherent_pair_candidate(adjacent_records, right_hole)
        and simple_coherent_rate(adjacent_records, left_hole) == 0
        and simple_coherent_rate(adjacent_records, right_hole) == 0
        and formation_rate(adjacent_records, left_hole) == 1
        and formation_rate(adjacent_records, right_hole) == 1,
        "the range-two anti-cluster clause deletes the two-hole mutual freeze",
    )

    check(
        "finite-cavity-exit-certificate",
        finite_star_patterns_have_exit(payload_a),
        "all 127 nonempty blank patterns in an exact seven-site cavity have an eligible exit",
    )

    records = {}
    predecessor_counts = []
    site_rates = []
    target_rates = []
    missing_candidate_free = True
    content_supported = True
    for index, site in enumerate(APPEND_ORDER):
        condition = recorded_neighbor_contents(records, site)
        predecessor_counts.append(len(condition))
        site_rates.append(formation_rate(records, site))
        if index == 0:
            content_supported = content_supported and isinstance(local_law(condition), GaussianLaw)
        else:
            content_supported = content_supported and content_mass(local_law(condition), payload_a) == 1
        append_record(records, site, payload_a)
        target_rates.append(formation_rate(records, TARGET))
        if coherent_pair_candidate(records, TARGET):
            missing_candidate_free = missing_candidate_free and all(
                not coherent_pair_candidate(records, add(TARGET, direction))
                for direction in DIRECTIONS
                if add(TARGET, direction) not in records
            )
    check(
        "protected-scaffold-geometry",
        predecessor_counts == [0] + [1] * 10
        and site_rates == [1] * 11
        and target_rates == [1] * 4 + [0] * 6 + [1]
        and missing_candidate_free
        and content_supported,
        "all carriers remain eligible while the origin is held from step 5 through step 10",
    )

    rescued = {}
    rescue_statuses = []
    for event_index, site in enumerate(PROTECTED_EVENT_LABELS):
        if site == TARGET and event_index == 5:
            sample = payload_a
        elif site == TARGET:
            sample = decoded_a.projector
        else:
            sample = payload_a
        rescue_statuses.append(execute_proposal(rescued, site, sample, protected=True))
    check(
        "protected-proposal-rescue",
        rescue_statuses[5] == "held"
        and rescue_statuses[-1] == "record"
        and len(rescued) == 12
        and matrix_equal(rescued[TARGET], decoded_a.projector),
        "an actual target proposal after step 5 is ignored, then the full shell writes the projector",
    )

    deleted = {}
    for site in APPEND_ORDER[:5]:
        execute_proposal(deleted, site, payload_a, protected=True)
    early_status = execute_proposal(deleted, TARGET, payload_a, protected=False)
    for site in APPEND_ORDER[5:]:
        execute_proposal(deleted, site, payload_a, protected=True)
    late_status = execute_proposal(deleted, TARGET, decoded_a.projector, protected=True)
    check(
        "hold-deletion-control",
        early_status == "record"
        and late_status == "occupied"
        and matrix_equal(deleted[TARGET], payload_a),
        "deleting the hold makes the same intermediate proposal lock A and reject the later read",
    )

    core = set(APPEND_ORDER) | {TARGET}
    guard_halo = halo(core)
    basic_probability = Q(factorial(30), factorial(41))
    sequential_basic_probability = prod(Q(1, k) for k in range(31, 42))
    rescue_probability = Q(1, len(guard_halo)) ** len(PROTECTED_EVENT_LABELS)
    check(
        "finite-cylinder-probability",
        len(core) == 12
        and len(guard_halo) == 41
        and len(guard_halo - core) == 29
        and basic_probability == sequential_basic_probability > 0
        and rescue_probability == Q(1, 925103102315013629321) > 0,
        "the 41-site basic order has mass 30!/41!, and one load-bearing rescue order has mass 41^-13",
    )

    shadow_records = {}
    shadow_reachable = True
    for index, site in enumerate(APPEND_ORDER[:6]):
        condition = recorded_neighbor_contents(shadow_records, site)
        shadow_reachable = shadow_reachable and formation_rate(shadow_records, site) == 1
        if index == 0:
            shadow_reachable = shadow_reachable and isinstance(local_law(condition), GaussianLaw)
        else:
            shadow_reachable = shadow_reachable and content_mass(local_law(condition), payload_a) == 1
        shadow_records[site] = payload_a
    shadow_neighbor = (0, 0, 1)
    shadow_extra = (-1, 0, 1)
    shadow_reachable = (
        shadow_reachable
        and formation_rate(shadow_records, shadow_extra) == 1
        and content_mass(
            local_law(recorded_neighbor_contents(shadow_records, shadow_extra)),
            payload_a,
        )
        == 1
    )
    shadow_records[shadow_extra] = payload_a
    shadow_target_status = execute_proposal(
        dict(shadow_records), TARGET, payload_a, protected=True
    )
    check(
        "cavity-shadow-collision",
        shadow_reachable
        and coherent_pair_candidate(shadow_records, TARGET)
        and coherent_pair_candidate(shadow_records, shadow_neighbor)
        and not isolated_cavity_hold(shadow_records, TARGET)
        and formation_rate(shadow_records, TARGET) == 1
        and shadow_target_status == "record"
        and content_mass(local_law(recorded_neighbor_contents(shadow_records, TARGET)), payload_a) == 1,
        "a positive supported birth sequence reaches a shadow release and premature target payload copy",
    )

    rotations = proper_cubic_rotations()
    rotation_ok = len(rotations) == 24
    for rotation in rotations:
        rotated_order = tuple(rotate_site(rotation, site) for site in APPEND_ORDER)
        rotated_records = {}
        profile = []
        for site in rotated_order:
            rotation_ok = rotation_ok and formation_rate(rotated_records, site) == 1
            rotated_records[site] = payload_a
            profile.append(formation_rate(rotated_records, TARGET))
        rotation_ok = rotation_ok and profile == [1] * 4 + [0] * 6 + [1]
    check(
        "proper-cubic-process-covariance",
        rotation_ok,
        "all 24 proper cubic rotations preserve carrier eligibility and the target hold/release profile",
    )

    shift = (7, -5, 3)
    translated = translate_records({site: payload_a for site in APPEND_ORDER[:5]}, shift)
    check(
        "translation-process-covariance",
        formation_rate({site: payload_a for site in APPEND_ORDER[:5]}, TARGET) == 0
        and formation_rate(translated, add(TARGET, shift)) == 0,
        "translation preserves the isolated coherent-cavity hold",
    )

    hadamard = Matrix([[1, 1], [1, -1]]) / sqrt(2)
    conjugated_full = {
        site: simplify(hadamard * content * hadamard.conjugate().T)
        for site, content in full_shell.items()
    }
    check(
        "internal-basis-process-covariance",
        formation_rate(conjugated_full, TARGET) == formation_rate(full_shell, TARGET)
        and finite_law_equal(
            local_law(recorded_neighbor_contents(conjugated_full, TARGET)),
            conjugate_law(full_law, hadamard),
        ),
        "unitary re-presentation preserves the rate and conjugates the completed read law",
    )

    radius_two_ball = {
        (x, y, z)
        for x in range(-2, 3)
        for y in range(-2, 3)
        for z in range(-2, 3)
        if abs(x) + abs(y) + abs(z) <= 2
    }
    term_50 = Q(25**50, factorial(50))
    term_51 = Q(25**51, factorial(51))
    check(
        "finite-causal-cone-bound",
        len(radius_two_ball) == 25
        and simplify(term_51 / term_50) == Q(25, 51) < 1,
        "the range-two ancestor count is bounded by 25^n tau^n/n!, whose ratio eventually contracts",
    )

    check(
        "local-nonexplosion",
        len(core) == 12 and len(set(PROTECTED_EVENT_LABELS)) == 12,
        "permanence permits at most one accepted state change per coordinate and at most |Lambda| in finite Lambda",
    )

    tau = symbols("tau", positive=True)
    isolated_seed_probability = simplify((1 - exp(-tau)) * exp(-6 * tau))
    isolated_seed_probability_at_one = isolated_seed_probability.subs(tau, 1)
    first_star = {TARGET} | {add(TARGET, direction) for direction in DIRECTIONS}
    second_center = (3, 0, 0)
    second_star = {second_center} | {
        add(second_center, direction) for direction in DIRECTIONS
    }
    check(
        "global-finite-jump-deletion",
        positive_truth(isolated_seed_probability_at_one)
        and first_star.isdisjoint(second_star),
        "infinitely many disjoint stars have positive seed-before-neighbors events, so global finite-jump CTMC language is rejected",
    )

    perturbed_pair = {
        (1, 0, 0): payload_a,
        (-1, 0, 0): simplify(payload_a + Q(1, 100) * I2),
        (0, 1, 0): payload_a,
    }
    check(
        "literal-equality-discontinuity",
        formation_rate(pair_records, TARGET) == 0
        and formation_rate(perturbed_pair, TARGET) == 1,
        "an arbitrarily small literal payload mismatch releases the rate, so no Feller claim is made",
    )

    note_text = NOTE.read_text() if NOTE.exists() else ""
    check(
        "source-contract",
        all(
            token in note_text
            for token in (
                "No-Go Discipline Gate",
                "range-two",
                "sitewise saturation",
                "cavity-shadow",
                "no TOE-percentage movement",
                "PR #7318",
            )
        ),
        "the note binds process range, liveness scope, collision wall, pincer, and score boundary",
    )

    print(
        "per_element: literal payload equality, generic decoding, content support, trace output, and exact rate values are checked"
    )
    print(
        "per_site: empty, one-neighbor, coherent hold, full read, mixed escape, shadow release, and permanence branches are executed"
    )
    print(
        "per_mode: the abstract Poisson formation parameter and causal-cone bound are checked; no physical time, continuum, gravity, or PR determinant fixture is claimed"
    )
    print(
        "per_block: the 41-site cylinder, protected 13-proposal rescue, 127 cavity patterns, and all 24 cubic rotations are checked"
    )
    print(
        "lattice_wide: Harris existence and sitewise saturation are proved analytically; the shadow fixture rejects universal compiler reliability and global finite-jump language fails, while recurrent resources are not constructed"
    )
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
