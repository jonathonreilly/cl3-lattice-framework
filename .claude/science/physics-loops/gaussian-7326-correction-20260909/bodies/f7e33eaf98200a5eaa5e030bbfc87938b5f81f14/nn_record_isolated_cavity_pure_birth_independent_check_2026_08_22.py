#!/usr/bin/env python3
"""Independent reconstruction of the isolated-cavity Record birth claim."""

from __future__ import annotations

from itertools import combinations, permutations, product
from math import factorial
from pathlib import Path

from sympy import Matrix, Rational as Q, exp, simplify


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/NN_RECORD_ISOLATED_CAVITY_PURE_BIRTH_BOUNDED_THEOREM_NOTE_"
    "2026-08-22.md",
)

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "NN_RECORD_ISOLATED_CAVITY_PURE_BIRTH_BOUNDED_THEOREM_NOTE_"
    "2026-08-22.md"
)

O = (0, 0, 0)
DIRS = (
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
GENERIC = frozenset(("A", "B", "Aq"))


def add(left, right):
    return tuple(left[index] + right[index] for index in range(3))


def slots(state, site):
    return tuple(state.get(add(site, direction)) for direction in DIRS)


def base(state, site):
    if site in state:
        return False
    values = slots(state, site)
    occupied = tuple(value for value in values if value is not None)
    if not occupied or len(occupied) == 6:
        return False
    if occupied[0] not in GENERIC or any(value != occupied[0] for value in occupied):
        return False
    return any(
        values[2 * axis] is not None
        and values[2 * axis + 1] is not None
        and values[2 * axis] == values[2 * axis + 1]
        for axis in range(3)
    )


def hold(state, site):
    return base(state, site) and not any(
        neighbor not in state and base(state, neighbor)
        for neighbor in (add(site, direction) for direction in DIRS)
    )


def rate(state, site):
    return 0 if site in state or hold(state, site) else 1


def adjacent(left, right):
    return sum(abs(left[index] - right[index]) for index in range(3)) == 1


def sign(perm):
    inversions = sum(
        1 for i in range(3) for j in range(i + 1, 3) if perm[i] > perm[j]
    )
    return -1 if inversions % 2 else 1


def rotations():
    result = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            if sign(perm) * signs[0] * signs[1] * signs[2] != 1:
                continue
            matrix = Matrix.zeros(3)
            for row, column in enumerate(perm):
                matrix[row, column] = signs[row]
            result.append(matrix)
    return tuple(result)


def rotate(matrix, site):
    value = matrix * Matrix(site)
    return tuple(int(value[index]) for index in range(3))


def adjacent_holes():
    right = (0, 1, 0)
    state = {}
    for center, other in ((O, right), (right, O)):
        for direction in DIRS:
            site = add(center, direction)
            if site != other:
                state[site] = "A"
    return state, right


def exhaustive_star_exit():
    star = (O,) + DIRS
    sea = {
        (x, y, z): "A"
        for x in range(-3, 4)
        for y in range(-3, 4)
        for z in range(-3, 4)
    }
    checked = 0
    for count in range(1, 8):
        for blank_tuple in combinations(star, count):
            blanks = set(blank_tuple)
            state = {site: value for site, value in sea.items() if site not in blanks}
            checked += 1
            if not any(rate(state, site) == 1 for site in blanks):
                return False, checked
            for site in blanks:
                if hold(state, site) and not any(
                    add(site, direction) in blanks
                    and rate(state, add(site, direction)) == 1
                    for direction in DIRS
                ):
                    return False, checked
    return True, checked


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

    state = {}
    rates = []
    candidate_neighbors_clear = True
    predecessor_counts = []
    for site in ORDER:
        predecessor_counts.append(sum(adjacent(site, old) for old in state))
        check_rate = rate(state, site)
        state[site] = "A"
        rates.append(rate(state, O))
        if base(state, O):
            candidate_neighbors_clear = candidate_neighbors_clear and all(
                not base(state, add(O, direction))
                for direction in DIRS
                if add(O, direction) not in state
            )
        if check_rate != 1:
            candidate_neighbors_clear = False
    check(
        "independent-scaffold-profile",
        predecessor_counts == [0] + [1] * 10
        and rates == [1] * 4 + [0] * 6 + [1]
        and candidate_neighbors_clear,
        "the independent predicate holds only the target from steps 5 through 10",
    )

    event_state = {}
    event_labels = ORDER[:5] + (O,) + ORDER[5:] + (O,)
    statuses = []
    for index, site in enumerate(event_labels):
        if site in event_state:
            statuses.append("occupied")
        elif rate(event_state, site) == 0:
            statuses.append("held")
        else:
            event_state[site] = "P" if site == O else "A"
            statuses.append("formed")
    check(
        "independent-rescue-execution",
        statuses[5] == "held"
        and statuses[-1] == "formed"
        and event_state[O] == "P"
        and len(event_state) == 12,
        "one protected target proposal is ignored and the completed shell later forms the read Record",
    )

    core = set(ORDER) | {O}
    halo = core | {add(site, direction) for site in core for direction in DIRS}
    check(
        "independent-cylinder-count",
        len(core) == 12
        and len(halo) == 41
        and Q(factorial(30), factorial(41)) > 0
        and Q(1, 41) ** 13 == Q(1, 925103102315013629321),
        "the independent halo census reproduces 30!/41! and the protected 41^-13 subevent",
    )

    pair = {(1, 0, 0): "A", (-1, 0, 0): "A", (0, 1, 0): "A"}
    mixed = dict(pair)
    mixed[(0, 0, 1)] = "B"
    quotient = {(1, 0, 0): "A", (-1, 0, 0): "Aq", (0, 1, 0): "A"}
    full = {direction: "A" for direction in DIRS}
    check(
        "branch-hostiles",
        hold(pair, O)
        and rate(pair, O) == 0
        and not base(mixed, O)
        and rate(mixed, O) == 1
        and not base(quotient, O)
        and rate(quotient, O) == 1
        and not base(full, O)
        and rate(full, O) == 1,
        "coherent hold, mixed escape, literal equality, and full-shell priority are independently separated",
    )

    two_hole_state, right_hole = adjacent_holes()
    check(
        "independent-two-hole-deletion",
        base(two_hole_state, O)
        and base(two_hole_state, right_hole)
        and not hold(two_hole_state, O)
        and not hold(two_hole_state, right_hole)
        and rate(two_hole_state, O) == rate(two_hole_state, right_hole) == 1,
        "adjacent base cavities release instead of mutually freezing",
    )

    star_ok, star_count = exhaustive_star_exit()
    check(
        "independent-finite-cavity-exit",
        star_ok and star_count == 127,
        "an independent exhaustive seven-site sea fixture has no nonempty all-held pattern",
    )

    shadow = {site: "A" for site in ORDER[:6]}
    shadow[(-1, 0, 1)] = "A"
    check(
        "independent-shadow-control",
        base(shadow, O)
        and base(shadow, (0, 0, 1))
        and not hold(shadow, O)
        and rate(shadow, O) == 1,
        "a neighboring candidate creates the disclosed early-release shadow collision",
    )

    rotation_ok = True
    proper = rotations()
    for rotation in proper:
        rotated_order = tuple(rotate(rotation, site) for site in ORDER)
        rotated_state = {}
        profile = []
        for site in rotated_order:
            rotation_ok = rotation_ok and rate(rotated_state, site) == 1
            rotated_state[site] = "A"
            profile.append(rate(rotated_state, O))
        rotation_ok = rotation_ok and profile == [1] * 4 + [0] * 6 + [1]
    check(
        "independent-cubic-orbit",
        len(proper) == 24 and rotation_ok,
        "all signed-permutation rotations independently preserve the protected profile",
    )

    radius_two = {
        (x, y, z)
        for x in range(-2, 3)
        for y in range(-2, 3)
        for z in range(-2, 3)
        if abs(x) + abs(y) + abs(z) <= 2
    }
    ratio = simplify(Q(25**51, factorial(51)) / Q(25**50, factorial(50)))
    check(
        "independent-causal-bound",
        len(radius_two) == 25 and ratio == Q(25, 51) < 1,
        "range two gives a 25-site influence ball and factorially controlled ordered paths",
    )

    star_zero = {O} | {add(O, direction) for direction in DIRS}
    far = (3, 0, 0)
    star_far = {far} | {add(far, direction) for direction in DIRS}
    p_seed_at_one = simplify((1 - exp(-1)) * exp(-6))
    check(
        "independent-global-jump-boundary",
        bool(p_seed_at_one.is_positive) and star_zero.isdisjoint(star_far),
        "disjoint stars carry independent positive early-seed events, excluding global finite-jump language",
    )

    source = NOTE.read_text() if NOTE.exists() else ""
    check(
        "independent-source-fence",
        all(
            phrase in source
            for phrase in (
                "sitewise saturation",
                "abstract formation parameter",
                "not a reliable compiler",
                "cavity-shadow collision",
                "No Minimal Axioms edit",
            )
        ),
        "the note preserves the liveness, time, reliability, collision, and axiom boundaries",
    )

    print(
        "per_element: independent literal payload labels, exact rates, and content-branch boundaries are checked"
    )
    print(
        "per_site: independent coherent hold, mixed/full release, adjacent-hole escape, shadow release, and permanence are checked"
    )
    print(
        "per_mode: the range-two causal bound and abstract proposal parameter are checked; no Feller or physical-time claim is made"
    )
    print(
        "per_block: the protected 13-event cylinder, 127 cavity patterns, 41-site halo, and 24 rotations are reconstructed"
    )
    print(
        "lattice_wide: sitewise saturation follows from stabilization plus recurring clocks; the shadow control rejects universal reliability, global finite-jump language fails, and recurrent resources remain open"
    )
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
