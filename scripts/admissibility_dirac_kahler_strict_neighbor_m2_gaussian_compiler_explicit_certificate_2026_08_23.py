#!/usr/bin/env python3
"""Explicit finite-fixture certificate for the recovered Gaussian compiler.

This prototype closes the algebraic and finite-routing checks that a lane count
cannot close.  It executes two disclosed mass-one fixtures: the supplied xgraded
background at width four and the constant background at width eight, each at
T_cover=12, for c=1/2 and c=1/3 (the m/2 and m/3 splits at m=1).  It

* separates the three arm-sensitive rows into an arm-blind Gaussian factor and
  an S0/S1/S2 Record-star bridge;
* compiles every arm-blind residual so an original occurrence has at most one
  scalar precision edge;
* assigns every scalar variable an actual Z^3 site and M2(C) payload slot;
* subdivides every non-nearest scalar edge along an explicit nearest-neighbor
  path, with a unit Schur pivot at each inserted route variable; and
* reverses the compiler and Record Schur steps, and certifies recovery along
  every routed path by the generic unit-pivot identity and finite induction,
  back to the exact supplied-fixture precision.

Ordinary carriers reserve the central M2 coefficient for an integer tag and use
at most three Pauli-frame payloads.  S0 is the one declared four-payload
Record neighbor.  Every routed S0 edge has an adjacent terminal carrier, but a
role-to-S0-payload selector is not instantiated.  The Record center reserves
its central coefficient for the arm/frame tag and carries the three bridge
variables in its Pauli slots.

The explicit crossbar uses one z height per routed nonzero cross-site precision
edge.  It is a
finite width-4/8 witness, not a cover-independent fixed-density construction:
height and physical volume grow with the finite compiled graph.  The script
prints that boundary and never reports full W_NN closure.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations_with_replacement, permutations, product
from math import isqrt
from pathlib import Path
from typing import Iterable, Iterator

import sympy as sp

import admissibility_dirac_kahler_strict_neighbor_m2_gaussian_compiler_released7333_fixture_2026_09_10 as b43


b175 = b43.b175
b174 = b43.b174
R = sp.Rational
ZERO = sp.Integer(0)
ONE = sp.Integer(1)
I = sp.I

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_STRICT_NEIGHBOR_M2_GAUSSIAN_COMPILER_"
    "BOUNDED_THEOREM_NOTE_2026-08-23.md"
)
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_STRICT_NEIGHBOR_M2_GAUSSIAN_"
    "COMPILER_BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "scripts/admissibility_dirac_kahler_strict_neighbor_m2_gaussian_"
    "compiler_released7333_fixture_2026_09_10.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_"
    "NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_"
    "nonuniform_hodge_overlap_2026_08_14.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)
INPUT_SHA256 = {
    "docs/ADMISSIBILITY_DIRAC_KAHLER_STRICT_NEIGHBOR_M2_GAUSSIAN_COMPILER_BOUNDED_THEOREM_NOTE_2026-08-23.md": "b77307fd3fcc3a603a34f41841dc707c09d341011ab54dca19b6e45f3541f6c4",
    "scripts/admissibility_dirac_kahler_strict_neighbor_m2_gaussian_compiler_released7333_fixture_2026_09_10.py": "8d2e071da05f0e540c8ec061b5dbea6cb996040a33b90efcd2f6e11b73d52cd2",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md": "9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py": "5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445",
    "docs/MINIMAL_AXIOMS_2026-06-29.md": "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753",
    "docs/audit/data/axiom_premise_nodes.json": "615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37",
}


def input_hashes_match() -> bool:
    return all(
        (ROOT / path).is_file()
        and sha256((ROOT / path).read_bytes()).hexdigest()
        == INPUT_SHA256[path]
        for path in AUDIT_INPUT_PATHS
    )

ALPHA = sp.Integer(3)
BETA = R(3, 2)
C_NORMALIZATION = R(9, 2)
SQRT_ALPHA = sp.sqrt(ALPHA)
SQRT_BETA = sp.sqrt(BETA)

RECORD_SITE = (0, 0, 0)
S0_SITE = (1, 0, 0)
S1_SITE = (0, 1, 0)
S2_SITE = (0, 0, 1)
RECORD_BLANKS = ((-1, 0, 0), (0, -1, 0), (0, 0, -1))
SPECIAL_SITES = {RECORD_SITE, S0_SITE, S1_SITE, S2_SITE, *RECORD_BLANKS}

DIRECTIONS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)

PAULI = (
    sp.Matrix([[ZERO, ONE], [ONE, ZERO]]),
    sp.Matrix([[ZERO, -I], [I, ZERO]]),
    sp.Matrix([[ONE, ZERO], [ZERO, -ONE]]),
)
IDENTITY2 = sp.eye(2)
TAG_BASE = 100

SparsePrecision = dict[tuple[str, str], sp.Expr]
Site = tuple[int, int, int]


@dataclass(frozen=True)
class Term:
    label: str
    coefficient: sp.Expr
    original: bool


@dataclass(frozen=True)
class Route:
    index: int
    left: str
    right: str
    coefficient: sp.Expr
    layer: int
    sites: tuple[Site, ...]


@dataclass
class FixtureCertificate:
    width: int
    split_name: str
    edge_count: int
    compiled_mediators: int
    route_mediators: int
    active_sites: int
    max_height: int
    max_scalar_degree: int
    max_payloads: int
    max_tagged_payloads: int
    s0_bulk_degree: int
    map_digest: str
    compiler_determinant: sp.Expr
    record_determinant: sp.Expr


def add_site(left: Site, right: Site) -> Site:
    return tuple(left[index] + right[index] for index in range(3))


def sub_site(left: Site, right: Site) -> Site:
    return tuple(left[index] - right[index] for index in range(3))


def manhattan(left: Site, right: Site) -> int:
    return sum(abs(left[index] - right[index]) for index in range(3))


def canonical(left: str, right: str) -> tuple[str, str, bool]:
    if left <= right:
        return left, right, False
    return right, left, True


def exact_zero(value: sp.Expr) -> bool:
    expanded = sp.expand(value)
    return expanded == 0 or sp.cancel(expanded) == 0


def add_entry(
    precision: SparsePrecision, left: str, right: str, value: sp.Expr
) -> None:
    first, second, swapped = canonical(left, right)
    contribution = sp.conjugate(value) if swapped else value
    updated = sp.expand(precision.get((first, second), ZERO) + contribution)
    if updated == 0:
        precision.pop((first, second), None)
    else:
        precision[(first, second)] = updated


def get_entry(precision: SparsePrecision, left: str, right: str) -> sp.Expr:
    first, second, swapped = canonical(left, right)
    value = precision.get((first, second), ZERO)
    return sp.conjugate(value) if swapped else value


def add_precision(target: SparsePrecision, source: SparsePrecision) -> None:
    for (left, right), value in source.items():
        add_entry(target, left, right, value)


def rank_one(terms: Iterable[tuple[str, sp.Expr]]) -> SparsePrecision:
    combined: dict[str, sp.Expr] = defaultdict(lambda: ZERO)
    for label, coefficient in terms:
        combined[label] = sp.expand(combined[label] + coefficient)
    labels = sorted(combined)
    output: SparsePrecision = {}
    for left_index, left in enumerate(labels):
        for right in labels[left_index:]:
            value = sp.expand(sp.conjugate(combined[left]) * combined[right])
            add_entry(output, left, right, value)
    return output


def factor_precision(factors: Iterable[Iterable[Term]]) -> SparsePrecision:
    output: SparsePrecision = {}
    for factor in factors:
        add_precision(
            output,
            rank_one((term.label, term.coefficient) for term in factor),
        )
    return output


def sparse_equal(left: SparsePrecision, right: SparsePrecision) -> bool:
    return all(
        exact_zero(left.get(key, ZERO) - right.get(key, ZERO))
        for key in set(left) | set(right)
    )


def eliminate_one(
    precision: SparsePrecision, hidden: str
) -> tuple[SparsePrecision, sp.Expr]:
    pivot = sp.simplify(get_entry(precision, hidden, hidden))
    if pivot == 0:
        raise AssertionError(f"zero Schur pivot for {hidden}")
    neighbors = sorted(
        {
            right if left == hidden else left
            for left, right in precision
            if hidden in (left, right) and left != right
        }
    )
    output = {
        key: value
        for key, value in precision.items()
        if hidden not in key
    }
    for left, right in combinations_with_replacement(neighbors, 2):
        correction = sp.cancel(
            get_entry(precision, left, hidden)
            * get_entry(precision, hidden, right)
            / pivot
        )
        add_entry(output, left, right, -correction)
    return output, pivot


def split_terms(
    terms: list[Term], prefix: str, state: list[int], cut: int
) -> tuple[list[Term], list[Term]]:
    label = f"{prefix}:g{state[0]}"
    state[0] += 1
    left = [
        Term(
            term.label,
            sp.expand(SQRT_ALPHA * term.coefficient),
            term.original,
        )
        for term in terms[:cut]
    ]
    right = [
        Term(
            term.label,
            sp.expand(SQRT_BETA * term.coefficient),
            term.original,
        )
        for term in terms[cut:]
    ]
    left.append(Term(label, -SQRT_ALPHA, False))
    right.append(Term(label, SQRT_BETA, False))
    return left, right


def reduce_arity(
    terms: list[Term], prefix: str, state: list[int]
) -> list[list[Term]]:
    if len(terms) <= 3:
        return [terms]
    left, right = split_terms(terms, prefix, state, len(terms) // 2)
    return reduce_arity(left, prefix, state) + reduce_arity(
        right, prefix, state
    )


def isolate_originals(
    terms: list[Term], prefix: str, state: list[int]
) -> list[list[Term]]:
    """Make every non-unary original occurrence have one scalar edge."""
    output: list[list[Term]] = []
    current = list(terms)
    while sum(term.original for term in current) > 1:
        index = next(
            position for position, term in enumerate(current) if term.original
        )
        ordered = [current[index], *current[:index], *current[index + 1 :]]
        leaf, current = split_terms(ordered, prefix, state, 1)
        output.append(leaf)
    if sum(term.original for term in current) == 1 and len(current) > 2:
        index = next(
            position for position, term in enumerate(current) if term.original
        )
        ordered = [current[index], *current[:index], *current[index + 1 :]]
        leaf, current = split_terms(ordered, prefix, state, 1)
        output.append(leaf)
    output.append(current)
    return output


def compile_named_factor(
    terms: tuple[tuple[str, sp.Expr], ...], prefix: str
) -> tuple[list[list[Term]], tuple[str, ...]]:
    state = [0]
    base = [Term(label, sp.sympify(coefficient), True) for label, coefficient in terms]
    factors: list[list[Term]] = []
    for reduced in reduce_arity(base, prefix, state):
        factors.extend(isolate_originals(reduced, prefix, state))
    mediators = tuple(f"{prefix}:g{index}" for index in range(state[0]))
    return factors, mediators


def compiler_reverse_certificate(
    terms: tuple[tuple[str, sp.Expr], ...],
    factors: list[list[Term]],
    mediators: tuple[str, ...],
) -> tuple[bool, SparsePrecision, sp.Expr]:
    precision = factor_precision(factors)
    for mediator in reversed(mediators):
        precision, pivot = eliminate_one(precision, mediator)
        if not exact_zero(pivot - C_NORMALIZATION):
            return False, precision, ZERO
    target = rank_one(terms)
    return (
        sparse_equal(precision, target),
        precision,
        C_NORMALIZATION ** len(mediators),
    )


def arm_sets(fixture: object) -> tuple[tuple[dict, ...], tuple[dict, ...], tuple]:
    qs = tuple(fixture.q({b175.RECORD_CELL: value}) for value in b175.MENU)
    symmetric = tuple(sp.expand((q + q.H) / 2) for q in qs)
    edges = b43.edge_union(symmetric)
    halves = tuple(
        b43.arm_bundle(fixture, value, edges, fraction=R(1, 2))
        for value in b175.MENU
    )
    thirds = tuple(
        b43.arm_bundle(fixture, value, edges, fraction=R(1, 3))
        for value in b175.MENU
    )
    return halves, thirds, edges


def row_rosters(
    bundles: tuple[tuple[dict, ...], ...]
) -> tuple[tuple[str, ...], ...]:
    size = bundles[0][0]["q"].rows
    bcols = bundles[0][0]["B"].cols
    output = []
    for row in range(size):
        labels = [
            f"p{column}"
            for column in range(size)
            if any(
                arm["q"][row, column] != 0
                for family in bundles
                for arm in family
            )
        ]
        labels.extend(
            f"z{column}"
            for column in range(bcols)
            if any(
                arm["B"][row, column] != 0
                for family in bundles
                for arm in family
            )
        )
        output.append(tuple(labels))
    return tuple(output)


def changed_rows(family: tuple[dict, ...]) -> tuple[int, ...]:
    reference = family[-1]
    return tuple(
        row
        for row in range(reference["q"].rows)
        if any(
            arm["q"].row(row) != reference["q"].row(row)
            or arm["B"].row(row) != reference["B"].row(row)
            for arm in family[:-1]
        )
    )


def row_coefficients(
    arm: dict, row: int, roster: tuple[str, ...]
) -> tuple[sp.Expr, ...]:
    scale = ONE / sp.sqrt(arm["variance"])
    return tuple(
        sp.expand(
            scale
            * (
                arm["q"][row, int(label[1:])]
                if label[0] == "p"
                else -arm["B"][row, int(label[1:])]
            )
        )
        for label in roster
    )


def changing_sets(
    bundles: tuple[tuple[dict, ...], ...],
    rows: tuple[int, ...],
    rosters: tuple[tuple[str, ...], ...],
) -> tuple[frozenset[str], ...]:
    output = []
    for row in rows:
        changing = set()
        for position, label in enumerate(rosters[row]):
            for family in bundles:
                values = tuple(
                    row_coefficients(arm, row, rosters[row])[position]
                    for arm in family
                )
                if any(not exact_zero(value - values[-1]) for value in values[:-1]):
                    changing.add(label)
                    break
        output.append(frozenset(changing))
    return tuple(output)


def record_pack(
    rows: tuple[int, ...], changing: tuple[frozenset[str], ...]
) -> tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...]]:
    core = changing[1] & changing[2]
    side_one = ((changing[0] | changing[1]) - core) | {
        f"y{rows[0]}",
        f"y{rows[1]}",
    }
    side_two = (changing[2] - core) | {f"y{rows[2]}"}
    return tuple(sorted(core)), tuple(sorted(side_one)), tuple(sorted(side_two))


def bridge_precision(
    left: tuple[tuple[str, sp.Expr], ...],
    right: tuple[tuple[str, sp.Expr], ...],
    hidden: str,
) -> SparsePrecision:
    output: SparsePrecision = {}
    add_precision(
        output,
        {
            key: 2 * value
            for key, value in rank_one(left).items()
        },
    )
    add_precision(
        output,
        {
            key: 2 * value
            for key, value in rank_one(right).items()
        },
    )
    add_entry(output, hidden, hidden, ONE)
    for label, coefficient in left:
        add_entry(output, label, hidden, sp.conjugate(coefficient))
    for label, coefficient in right:
        add_entry(output, label, hidden, -sp.conjugate(coefficient))
    return output


def record_reverse_certificate(
    roster: tuple[str, ...],
    coefficients: tuple[sp.Expr, ...],
    changing: frozenset[str],
    core: frozenset[str],
    root: str,
    bridge_hidden: str,
) -> tuple[bool, SparsePrecision, SparsePrecision, tuple[sp.Expr, sp.Expr]]:
    fixed = tuple(
        (label, sp.expand(SQRT_ALPHA * coefficient))
        for label, coefficient in zip(roster, coefficients)
        if label not in changing
    ) + ((root, -SQRT_ALPHA),)
    left = tuple(
        (label, sp.expand(SQRT_BETA * coefficient))
        for label, coefficient in zip(roster, coefficients)
        if label in changing and label in core
    )
    right = tuple(
        (label, sp.expand(SQRT_BETA * coefficient))
        for label, coefficient in zip(roster, coefficients)
        if label in changing and label not in core
    ) + ((root, SQRT_BETA),)

    bridge = bridge_precision(left, right, bridge_hidden)
    precision = rank_one(fixed)
    add_precision(precision, bridge)
    after_h, h_pivot = eliminate_one(precision, bridge_hidden)
    visible, y_pivot = eliminate_one(after_h, root)
    target = rank_one(zip(roster, coefficients))
    exact = (
        exact_zero(h_pivot - ONE)
        and exact_zero(y_pivot - C_NORMALIZATION)
        and sparse_equal(visible, target)
    )
    return exact, visible, bridge, (h_pivot, y_pivot)


def proper_cubic_rotations() -> tuple[tuple[tuple[int, int, int], ...], ...]:
    output = []
    for order in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows = []
            for row in range(3):
                values = [0, 0, 0]
                values[order[row]] = signs[row]
                rows.append(tuple(values))
            rotation = tuple(rows)
            if int(sp.det(sp.Matrix(rotation))) == 1:
                output.append(rotation)
    return tuple(output)


def rotate(rotation, vector: Site) -> Site:
    return tuple(
        sum(rotation[row][column] * vector[column] for column in range(3))
        for row in range(3)
    )


def sigma(vector: Site) -> sp.Matrix:
    return sp.expand(
        sum(
            (vector[index] * PAULI[index] for index in range(3)),
            sp.zeros(2),
        )
    )


def tagged_code(frame_index: int, role: int) -> sp.Integer:
    return sp.Integer(TAG_BASE * (role + 1) + frame_index)


def tagged_encode(
    rotations,
    frame_index: int,
    role: int,
    payloads: tuple[sp.Expr, sp.Expr, sp.Expr],
) -> sp.Matrix:
    frame = rotations[frame_index]
    answer = tagged_code(frame_index, role) * IDENTITY2
    for index, payload in enumerate(payloads):
        basis = rotate(
            frame,
            tuple(1 if axis == index else 0 for axis in range(3)),
        )
        answer += payload * sigma(basis)
    return sp.expand(answer)


def tagged_decode(rotations, carrier: sp.Matrix):
    code = sp.expand(sp.trace(carrier) / 2)
    if not code.is_Integer:
        raise ValueError("central coordinate is not an integer tag code")
    code_int = int(code)
    role_plus_one, frame_index = divmod(code_int, TAG_BASE)
    role = role_plus_one - 1
    if role < 0 or frame_index >= len(rotations):
        raise ValueError("central coordinate is outside tagged support")
    frame = rotations[frame_index]
    traceless = sp.expand(carrier - code * IDENTITY2)
    payloads = []
    for index in range(3):
        basis = rotate(
            frame,
            tuple(1 if axis == index else 0 for axis in range(3)),
        )
        payloads.append(sp.expand(sp.trace(traceless * sigma(basis)) / 2))
    return frame_index, role, tuple(payloads)


def terminal_escape(home: Site, port_index: int) -> tuple[Site, ...]:
    """One of 18 explicit paths from a home to a unique vertical pin."""
    group, slot = divmod(port_index, 3)
    branch = (-1, 0, 1)[slot]
    relative: list[Site]
    if group == 0:  # +x
        relative = [(1, 0, 0), (2, 0, 0), (3, 0, 0)]
        if branch:
            relative.append((3, branch, 0))
        relative.append((3, branch, 1))
    elif group == 1:  # -x
        relative = [(-1, 0, 0), (-2, 0, 0), (-3, 0, 0)]
        if branch:
            relative.append((-3, branch, 0))
        relative.append((-3, branch, 1))
    elif group == 2:  # +y
        relative = [(0, 1, 0), (0, 2, 0), (0, 3, 0)]
        if branch:
            relative.append((branch, 3, 0))
        relative.append((branch, 3, 1))
    elif group == 3:  # -y
        relative = [(0, -1, 0), (0, -2, 0), (0, -3, 0)]
        if branch:
            relative.append((branch, -3, 0))
        relative.append((branch, -3, 1))
    elif group == 4:  # +z
        relative = [(0, 0, 1), (0, 0, 2), (0, 0, 3), (0, -1, 3)]
        if branch:
            relative.append((branch, -1, 3))
    elif group == 5:  # -z, then leave the home projection before rising
        relative = [(0, 0, -1), (0, 1, -1)]
        if branch:
            relative.append((branch, 1, -1))
    else:
        raise AssertionError(f"bad terminal port {port_index}")
    result = tuple(add_site(home, site) for site in relative)
    if manhattan(home, result[0]) != 1 or any(
        manhattan(left, right) != 1 for left, right in zip(result, result[1:])
    ):
        raise AssertionError("terminal escape is not nearest-neighbor")
    return result


def step_axis(start: Site, target: Site, axis: int) -> Iterator[Site]:
    current = list(start)
    delta = target[axis] - current[axis]
    direction = 1 if delta > 0 else -1
    for _ in range(abs(delta)):
        current[axis] += direction
        yield tuple(current)


def route_sites(
    left_home: Site,
    right_home: Site,
    left_escape: tuple[Site, ...],
    right_escape: tuple[Site, ...],
    layer: int,
) -> tuple[Site, ...]:
    sites = [left_home, *left_escape]
    current = sites[-1]
    target_top = (current[0], current[1], layer)
    sites.extend(step_axis(current, target_top, 2))
    current = sites[-1]
    right_pin = right_escape[-1]
    horizontal_x = (right_pin[0], current[1], layer)
    sites.extend(step_axis(current, horizontal_x, 0))
    current = sites[-1]
    horizontal_y = (right_pin[0], right_pin[1], layer)
    sites.extend(step_axis(current, horizontal_y, 1))
    current = sites[-1]
    target_pin = (right_pin[0], right_pin[1], right_pin[2])
    sites.extend(step_axis(current, target_pin, 2))
    sites.extend(reversed(right_escape[:-1]))
    sites.append(right_home)
    if any(manhattan(left, right) != 1 for left, right in zip(sites, sites[1:])):
        raise AssertionError("crossbar route contains a non-nearest step")
    if len(set(sites)) != len(sites):
        raise AssertionError("crossbar route self-intersects")
    return tuple(sites)


def subdivision_identity(coefficient: sp.Expr) -> bool:
    k = sp.sympify(coefficient)
    extended = sp.Matrix(
        [
            [ONE, ZERO, ONE],
            [ZERO, sp.conjugate(k) * k, -sp.conjugate(k)],
            [ONE, -k, ONE],
        ]
    )
    visible = sp.simplify(
        extended[:2, :2]
        - extended[:2, 2:] * extended[2:, :2]
    )
    target = sp.Matrix([[ZERO, k], [sp.conjugate(k), ZERO]])
    return visible == target


def assign_homes(
    labels: Iterable[str],
    pack: tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...]],
) -> tuple[dict[str, Site], dict[str, int]]:
    homes: dict[str, Site] = {}
    slots: dict[str, int] = {}
    for site, group in zip((S0_SITE, S1_SITE, S2_SITE), pack):
        for slot, label in enumerate(group):
            homes[label] = site
            slots[label] = slot
    ordinary = sorted(set(labels) - set(homes))
    columns = max(1, isqrt(len(ordinary)))
    if columns * columns < len(ordinary):
        columns += 1
    for index, label in enumerate(ordinary):
        site = (30 + 10 * (index % columns), 30 + 10 * (index // columns), 0)
        homes[label] = site
        slots[label] = 0
    if len(set(site for label, site in homes.items() if label in ordinary)) != len(ordinary):
        raise AssertionError("ordinary home collision")
    return homes, slots


def allowed_ports(site: Site) -> tuple[int, ...]:
    if site == S0_SITE:
        # -x is the Record-facing edge.
        groups = (0, 2, 3, 4, 5)
    elif site == S1_SITE:
        # -y is the Record-facing edge; leave first through -x.
        groups = (1, 2, 0, 4, 5)
    elif site == S2_SITE:
        # -z is the Record-facing edge; leave first through -x.
        groups = (1, 3, 0, 2, 4)
    else:
        groups = tuple(range(6))
    return tuple(3 * group + slot for group in groups for slot in range(3))


def route_graph(
    precision: SparsePrecision,
    homes: dict[str, Site],
    base_slots: dict[str, int],
    record_h_labels: tuple[str, ...],
) -> tuple[bool, dict]:
    edges = [
        (left, right, value)
        for (left, right), value in sorted(precision.items())
        if left != right and not exact_zero(value) and homes[left] != homes[right]
    ]
    incidents: dict[str, list[int]] = defaultdict(list)
    site_incidents: dict[Site, list[tuple[int, str]]] = defaultdict(list)
    for edge_index, (left, right, _) in enumerate(edges):
        incidents[left].append(edge_index)
        incidents[right].append(edge_index)
        site_incidents[homes[left]].append((edge_index, left))
        site_incidents[homes[right]].append((edge_index, right))
    degree = max((len(values) for values in incidents.values()), default=0)
    site_degree = max((len(values) for values in site_incidents.values()), default=0)
    if any(
        len(values) > len(allowed_ports(site))
        for site, values in site_incidents.items()
    ):
        return False, {
            "reason": "terminal port capacity",
            "degree": degree,
            "site_degree": site_degree,
        }

    port_for: dict[tuple[int, str], int] = {}
    for site, endpoint_incidents in site_incidents.items():
        ports = allowed_ports(site)
        for position, (edge_index, label) in enumerate(sorted(endpoint_incidents)):
            port_for[(edge_index, label)] = ports[position]

    base_payloads: dict[Site, list[str]] = defaultdict(list)
    for label, site in homes.items():
        base_payloads[site].append(label)
    base_payloads[RECORD_SITE].extend(record_h_labels)
    for site in RECORD_BLANKS:
        base_payloads.setdefault(site, [])

    slot_for = dict(base_slots)
    for slot, label in enumerate(record_h_labels):
        slot_for[label] = slot
    if any(
        sorted(slot_for[label] for label in payloads) != list(range(len(payloads)))
        for payloads in base_payloads.values()
    ):
        return False, {"reason": "base payload-slot assignment"}

    # S0 is the sole four-payload untagged carrier; every other active carrier
    # reserves its central coordinate for a tag and has at most three payloads.
    if len(base_payloads[S0_SITE]) != 4:
        return False, {"reason": "S0 is not four payloads"}
    if any(
        len(payloads) > 3
        for site, payloads in base_payloads.items()
        if site != S0_SITE
    ):
        return False, {"reason": "base tagged-carrier capacity"}

    occupancy: Counter[Site] = Counter(
        {site: len(payloads) for site, payloads in base_payloads.items()}
    )
    home_sites = set(base_payloads)
    digest = sha256()
    for site, payloads in sorted(base_payloads.items()):
        for label in sorted(payloads, key=lambda item: slot_for[item]):
            digest.update(
                f"base:{label}:{site}:{slot_for[label]}\n".encode("utf-8")
            )
    routes: list[Route] = []
    route_mediators = 0
    max_load = max(occupancy.values(), default=0)
    active_cross_edges = 0
    s0_adjacent_endpoints = 0

    for edge_index, (left, right, coefficient) in enumerate(edges):
        left_escape = terminal_escape(
            homes[left], port_for[(edge_index, left)]
        )
        right_escape = terminal_escape(
            homes[right], port_for[(edge_index, right)]
        )
        layer = 10 + edge_index
        sites = route_sites(
            homes[left], homes[right], left_escape, right_escape, layer
        )
        if not subdivision_identity(coefficient):
            return False, {"reason": "scalar subdivision identity"}

        internal = sites[1:-1]
        if any(site in home_sites for site in internal):
            return False, {
                "reason": "route crosses a scalar home",
                "edge": edge_index,
            }
        for path_index, site in enumerate(internal):
            slot = occupancy[site]
            if slot >= 3:
                return False, {
                    "reason": "ordinary carrier payload overflow",
                    "edge": edge_index,
                    "site": site,
                    "load_before": slot,
                }
            occupancy[site] += 1
            max_load = max(max_load, occupancy[site])
            digest.update(
                f"{edge_index}:{path_index}:{site}:{slot}\n".encode("utf-8")
            )
        if homes[left] == S0_SITE:
            s0_adjacent_endpoints += 1
            if manhattan(S0_SITE, sites[1]) != 1:
                return False, {"reason": "S0 route terminal is not adjacent"}
        if homes[right] == S0_SITE:
            s0_adjacent_endpoints += 1
            if manhattan(S0_SITE, sites[-2]) != 1:
                return False, {"reason": "S0 route terminal is not adjacent"}

        # Recursive insertion along L edges has L-1 unit pivots.  Its final
        # scalar chain consists only of consecutive physical neighbors.
        active_cross_edges += len(sites) - 1
        route_mediators += len(internal)
        routes.append(
            Route(
                edge_index,
                left,
                right,
                coefficient,
                layer,
                sites,
            )
        )

    onsite_edges = tuple(
        (left, right)
        for (left, right), value in precision.items()
        if left != right and not exact_zero(value) and homes[left] == homes[right]
    )
    all_steps_nn = all(
        all(
            manhattan(left_site, right_site) == 1
            for left_site, right_site in zip(route.sites, route.sites[1:])
        )
        for route in routes
    )
    s0_labels = set(base_payloads[S0_SITE])
    s0_degree = sum(
        1
        for left, right, _ in edges
        if left in s0_labels or right in s0_labels
    )
    max_tagged_load = max(
        (load for site, load in occupancy.items() if site != S0_SITE),
        default=0,
    )
    return True, {
        "routes": routes,
        "edge_count": len(edges),
        "onsite_edges": len(onsite_edges),
        "degree": degree,
        "site_degree": site_degree,
        "route_mediators": route_mediators,
        "active_sites": len(occupancy),
        "max_height": max((route.layer for route in routes), default=0),
        "max_load": max_load,
        "max_tagged_load": max_tagged_load,
        "digest": digest.hexdigest(),
        "all_steps_nn": all_steps_nn,
        "s0_degree": s0_degree,
        "s0_adjacent_endpoints": s0_adjacent_endpoints,
        "active_cross_edges": active_cross_edges,
    }


def build_split_certificate(
    fixture: object,
    width: int,
    split_name: str,
    family: tuple[dict, ...],
    bundles: tuple[tuple[dict, ...], ...],
    rosters: tuple[tuple[str, ...], ...],
    changed: tuple[int, ...],
    changing: tuple[frozenset[str], ...],
    pack: tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...]],
) -> tuple[bool, FixtureCertificate | dict]:
    reference = family[-1]
    changing_by_row = dict(zip(changed, changing))
    changed_position = {row: index for index, row in enumerate(changed)}
    compiled_factors: list[list[Term]] = []
    compiler_mediators: list[str] = []
    recovered: SparsePrecision = {}
    direct: SparsePrecision = {}
    compiler_exact = True

    for row, roster in enumerate(rosters):
        coefficients = row_coefficients(reference, row, roster)
        direct_row = rank_one(zip(roster, coefficients))
        add_precision(direct, direct_row)
        if row in changing_by_row:
            row_changing = changing_by_row[row]
            root = f"y{row}"
            fixed_terms = tuple(
                (label, sp.expand(SQRT_ALPHA * coefficient))
                for label, coefficient in zip(roster, coefficients)
                if label not in row_changing
            ) + ((root, -SQRT_ALPHA),)
            terms = fixed_terms
        else:
            terms = tuple(zip(roster, coefficients))
        prefix = f"w{width}:{split_name}:r{row}"
        factors, mediators = compile_named_factor(terms, prefix)
        exact, visible, _ = compiler_reverse_certificate(
            terms, factors, mediators
        )
        compiler_exact &= exact
        compiled_factors.extend(factors)
        compiler_mediators.extend(mediators)
        if row not in changing_by_row:
            add_precision(recovered, visible)

    # The standard zeta norm is arm independent and already on-site.
    for column in range(reference["B"].cols):
        label = f"z{column}"
        add_entry(direct, label, label, ONE)

    compiled_bulk = factor_precision(compiled_factors)
    for column in range(reference["B"].cols):
        add_entry(compiled_bulk, f"z{column}", f"z{column}", ONE)

    core = frozenset(pack[0])
    record_pivots: list[tuple[sp.Expr, sp.Expr]] = []
    record_local = True
    record_exact = True
    for arm_index, arm in enumerate(family):
        for row in range(fixture.N):
            if row not in changing_by_row:
                continue
            position = changed_position[row]
            coefficients = row_coefficients(arm, row, rosters[row])
            root = f"y{row}"
            hidden = f"h{row}"
            exact, visible, bridge, pivots = record_reverse_certificate(
                rosters[row],
                coefficients,
                changing[position],
                core,
                root,
                hidden,
            )
            record_exact &= exact
            record_pivots.append(pivots)
            if arm_index == len(family) - 1:
                add_precision(recovered, visible)

            side_site = S1_SITE if position < 2 else S2_SITE
            site_of = {
                **{label: S0_SITE for label in pack[0]},
                **{label: S1_SITE for label in pack[1]},
                **{label: S2_SITE for label in pack[2]},
                hidden: RECORD_SITE,
            }
            for (left, right), value in bridge.items():
                if left == right or exact_zero(value):
                    continue
                left_site = site_of[left]
                right_site = site_of[right]
                record_local &= left_site == right_site or (
                    RECORD_SITE in (left_site, right_site)
                    and (
                        S0_SITE in (left_site, right_site)
                        or side_site in (left_site, right_site)
                    )
                    and manhattan(left_site, right_site) == 1
                )
    for column in range(reference["B"].cols):
        add_entry(recovered, f"z{column}", f"z{column}", ONE)
    record_exact &= sparse_equal(recovered, direct)
    record_exact &= all(
        exact_zero(h_pivot - ONE)
        and exact_zero(y_pivot - C_NORMALIZATION)
        for h_pivot, y_pivot in record_pivots
    )
    record_determinant = C_NORMALIZATION ** len(changed)
    compiler_determinant = sp.Pow(
        C_NORMALIZATION, len(compiler_mediators), evaluate=False
    )

    labels = {
        label
        for key in compiled_bulk
        for label in key
    } | set(pack[0]) | set(pack[1]) | set(pack[2])
    homes, slots = assign_homes(labels, pack)
    h_labels = tuple(f"h{row}" for row in changed)
    routed, routing = route_graph(compiled_bulk, homes, slots, h_labels)
    if not routed:
        return False, routing

    max_original_factor_degree = Counter()
    for factor in compiled_factors:
        labels_in_factor = [term.label for term in factor]
        for term in factor:
            if term.original:
                max_original_factor_degree[term.label] += max(0, len(labels_in_factor) - 1)
    original_isolation = max(max_original_factor_degree.values(), default=0) <= 18

    rotations = proper_cubic_rotations()
    sample_payloads = (R(2, 7) + I / 5, -R(3, 11), I * R(5, 13))
    sample_roles = (0, routing["active_sites"], routing["edge_count"] + 17)
    tagged_ok = all(
        tagged_decode(
            rotations,
            tagged_encode(rotations, frame_index, role, sample_payloads),
        )
        == (frame_index, role, sample_payloads)
        for frame_index in range(len(rotations))
        for role in sample_roles
    )
    coefficient_map = sp.Matrix(
        [
            [ONE, ZERO, ZERO, ONE],
            [ZERO, ONE, -I, ZERO],
            [ZERO, ONE, I, ZERO],
            [ONE, ZERO, ZERO, -ONE],
        ]
    )
    full_codec_jacobian_ok = sp.simplify(
        coefficient_map.det() * sp.conjugate(coefficient_map.det())
    ) == 16

    ok = all(
        (
            compiler_exact,
            record_exact,
            record_local,
            routed,
            routing["all_steps_nn"],
            routing["max_load"] <= 4,
            routing["max_tagged_load"] <= 3,
            routing["degree"] <= 18,
            routing["s0_degree"] <= 15,
            routing["s0_adjacent_endpoints"] == routing["s0_degree"],
            original_isolation,
            tagged_ok,
            full_codec_jacobian_ok,
        )
    )
    if not ok:
        return False, {
            "reason": "certificate invariant",
            "compiler_exact": compiler_exact,
            "record_exact": record_exact,
            "record_local": record_local,
            "routing": routing,
            "original_isolation": original_isolation,
            "tagged_ok": tagged_ok,
            "full_codec_jacobian_ok": full_codec_jacobian_ok,
        }

    return True, FixtureCertificate(
        width=width,
        split_name=split_name,
        edge_count=routing["edge_count"],
        compiled_mediators=len(compiler_mediators),
        route_mediators=routing["route_mediators"],
        active_sites=routing["active_sites"],
        max_height=routing["max_height"],
        max_scalar_degree=routing["degree"],
        max_payloads=routing["max_load"],
        max_tagged_payloads=routing["max_tagged_load"],
        s0_bulk_degree=routing["s0_degree"],
        map_digest=routing["digest"],
        compiler_determinant=compiler_determinant,
        record_determinant=record_determinant,
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

    check(
        "source-input-closure",
        input_hashes_match() and b43.supplier_certificate(),
        "the note, extracted finite supplier, current Block 105 note/runner, minimal axioms, and premise registry match their exact declared bytes",
    )

    all_certificates: list[FixtureCertificate] = []
    pack_shapes = []
    for width in (4, 8):
        pattern = None if width == 4 else b174.constant_pattern(width)
        fixture = b174.Fixture(
            width,
            pattern=pattern,
            tag=f"b179-explicit-w{width}",
        )
        halves, thirds, _ = arm_sets(fixture)
        bundles = (halves, thirds)
        rosters = row_rosters(bundles)
        changed_half = changed_rows(halves)
        changed_third = changed_rows(thirds)
        changing = changing_sets(bundles, changed_half, rosters)
        packing = record_pack(changed_half, changing)
        pack_shapes.append(tuple(map(len, packing)))
        check(
            f"width-{width}-record-roster",
            changed_half == changed_third
            and len(changed_half) == 3
            and tuple(map(len, packing)) == (4, 3, 2),
            (
                f"background={'xgraded' if pattern is None else 'constant'}, "
                f"T_cover=12, m=1, changed_rows={changed_half}, "
                f"S0/S1/S2={tuple(map(len, packing))}"
            ),
        )
        for split_name, family in (("m2", halves), ("m3", thirds)):
            exact, result = build_split_certificate(
                fixture,
                width,
                split_name,
                family,
                bundles,
                rosters,
                changed_half,
                changing,
                packing,
            )
            if exact:
                assert isinstance(result, FixtureCertificate)
                all_certificates.append(result)
                check(
                    f"width-{width}-{split_name}-explicit-map",
                    True,
                    (
                        f"routed_cross_edges={result.edge_count}, degree={result.max_scalar_degree}, "
                        f"S0={result.s0_bulk_degree}, route_hidden={result.route_mediators}, "
                        f"sites={result.active_sites}, max_z={result.max_height}, "
                        f"tagged_payload_max={result.max_tagged_payloads}, "
                        f"S0_payloads={result.max_payloads}, digest={result.map_digest[:16]}"
                    ),
                )
            else:
                check(
                    f"width-{width}-{split_name}-explicit-map",
                    False,
                    repr(result),
                )

    check(
        "all-four-finite-certificates",
        len(all_certificates) == 4
        and pack_shapes == [(4, 3, 2), (4, 3, 2)]
        and all(certificate.max_payloads <= 4 for certificate in all_certificates)
        and all(certificate.max_tagged_payloads <= 3 for certificate in all_certificates)
        and all(certificate.max_scalar_degree <= 18 for certificate in all_certificates),
        "the disclosed xgraded-width-4 and constant-width-8 mass-one fixtures have exact compiler/Record reverse-Schur, route-identity, NN, collision, slot-capacity, and tag-codec checks for c=1/2,1/3",
    )

    heights = {(item.width, item.split_name): item.max_height for item in all_certificates}
    sites = {(item.width, item.split_name): item.active_sites for item in all_certificates}
    fixed_density_closed = False
    print(
        "BOUNDARY fixed_density_cover_independent=false: "
        "the explicit crossbar assigns one z layer per routed nonzero cross-site precision edge; "
        f"heights={heights}, active_sites={sites}. A periodic finite-type "
        "bounded-density embedding and its seam/cubic-covariance proof remain open."
    )
    check(
        "scope-boundary-is-machine-visible",
        not fixed_density_closed
        and all(item.max_height == item.edge_count + 9 for item in all_certificates),
        "resource height grows with the routed cross-edge roster, so this runner does not claim full W_NN closure",
    )

    print(
        "per_element: C-pivot compiler, generic unit-pivot route identity, "
        "and the full four-complex-coordinate M2 codec Jacobian are exact; "
        "the fixed-tag support uses a three-complex-payload pushforward"
    )
    print(
        "per_site: every instantiated routed cross-site edge is cubic NN; "
        "ordinary carriers have an integer tag plus <=3 payloads, while S0 uses four and its selector metadata is not executed"
    )
    print(
        "per_mode: at m=1, c=1/2 and c=1/3 reverse exactly through Record/compiler elimination and each finite route is covered by the checked identity plus induction"
    )
    print(
        "per_block: the disclosed xgraded-width-4 and constant-width-8 fixtures recover all four arms of the exact supplied-fixture precision at m=1"
    )
    print(
        "lattice_wide: NOT CLOSED; this finite crossbar is height/volume growing and supplies no periodic cover-independent fixed-density template"
    )
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return failed


if __name__ == "__main__":
    raise SystemExit(main())
