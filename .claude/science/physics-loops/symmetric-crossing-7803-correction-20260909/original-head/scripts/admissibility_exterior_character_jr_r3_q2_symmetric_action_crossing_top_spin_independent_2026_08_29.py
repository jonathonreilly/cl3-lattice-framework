#!/usr/bin/env python3
"""Independent exact link-census check for the symmetric top-spin response.

This module imports no Block248 primary code.  It reconstructs the three fine
plaquettes and the neighboring merged loop from oriented original links,
extracts the unique maximal-torus monomial of the coupled shared-rung network,
and evaluates the two crossing orders by multiplying one central multiplier
per original link representation.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction as F


AUDIT_TIMEOUT_SEC = 30
MAX_SPIN = 9
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R3_Q2_SYMMETRIC_ACTION_CROSSING_TOP_SPIN_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R3_Q2_PHYSICAL_Q_ACTION_CROSSING_TOWER_NO_GO_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R3_Q2_ADJACENT_PRODUCT_CUBIC_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_TEMPORAL_SPATIAL_SEMIGROUP_DEFECT_GENERATED_INTERACTION_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_TIME_REFINEMENT_SEMIGROUP_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


def plaquette(index: int) -> tuple[tuple[str, int], ...]:
    return (
        (f"u{index}", 1),
        (f"h{index + 1}", 1),
        (f"v{index}", -1),
        (f"h{index}", -1),
    )


def merged(start: int, stop: int) -> tuple[tuple[str, int], ...]:
    return (
        *tuple((f"u{index}", 1) for index in range(start, stop + 1)),
        (f"h{stop + 1}", 1),
        *tuple((f"v{index}", -1) for index in range(stop, start - 1, -1)),
        (f"h{start}", -1),
    )


PLAQUETTES = tuple(plaquette(index) for index in range(3))
C0 = merged(0, 2)
C1 = merged(3, 5)
INTERNAL_RUNGS = frozenset({"h1", "h2"})


def link_map(loop: tuple[tuple[str, int], ...]) -> dict[str, int]:
    return dict(loop)


def character(spin: int) -> dict[int, F]:
    """SO(3) maximal-torus character; inversion parity is tracked separately."""
    return {weight: F(1) for weight in range(-spin, spin + 1)}


def multiply(left: dict[int, F], right: dict[int, F]) -> dict[int, F]:
    result: dict[int, F] = {}
    for left_weight, left_value in left.items():
        for right_weight, right_value in right.items():
            weight = left_weight + right_weight
            result[weight] = result.get(weight, F(0)) + left_value * right_value
    return {weight: value for weight, value in result.items() if value}


def decompose(polynomial: dict[int, F]) -> dict[int, F]:
    work = dict(polynomial)
    result: dict[int, F] = {}
    while work:
        top = max(abs(weight) for weight in work)
        coefficient = work.get(top, work.get(-top, F(0)))
        if not coefficient:
            raise AssertionError("not a symmetric SO(3) character polynomial")
        result[top] = result.get(top, F(0)) + coefficient
        for weight in range(-top, top + 1):
            work[weight] = work.get(weight, F(0)) - coefficient
            if not work[weight]:
                work.pop(weight)
    return result


def top_fusion_multiplicity(spin: int) -> F:
    return decompose(multiply(character(spin), character(1))).get(spin + 1, F(0))


def maximal_torus_edge_weights(placement: int, spin: int) -> dict[str, int]:
    """One of the conjugate unique monomials saturating every top edge label."""
    p_map = link_map(PLAQUETTES[placement])
    c_map = link_map(C1)
    shared = set(p_map) & set(c_map)
    spectator_weight = -1 if shared else 1
    result: dict[str, int] = {}
    for link in set(p_map) | set(c_map):
        result[link] = (
            spin * p_map.get(link, 0)
            + spectator_weight * c_map.get(link, 0)
        )
    return result


def top_edge_label_counts(placement: int, spin: int) -> Counter[int]:
    return Counter(abs(weight) for weight in maximal_torus_edge_weights(placement, spin).values())


def census_crossing(placement: int, spin: int, multipliers: dict[int, F]) -> F:
    result = F(1)
    for label, count in top_edge_label_counts(placement, spin).items():
        result *= multipliers[label] ** count
    return result


def symmetric_factor(placement: int, spin: int, multipliers: dict[int, F]) -> F:
    """Top coefficient of A C + C A, with operators acting right to left."""
    return (
        census_crossing(placement, spin, multipliers)
        + census_crossing(placement, spin + 1, multipliers)
    ) * top_fusion_multiplicity(spin)


def tower_coefficient(
    placement: int, layer: int, multipliers: dict[int, F]
) -> F:
    result = F(1)
    for spin in range(1, layer):
        result *= symmetric_factor(placement, spin, multipliers)
    return result


def positive_sample() -> dict[int, F]:
    return {spin: F(spin + 2, 2 * spin + 5) for spin in range(1, MAX_SPIN + 2)}


def run_checks() -> list[tuple[str, bool]]:
    checks: list[tuple[str, bool]] = []
    p_sets = tuple(set(link_map(loop)) for loop in PLAQUETTES)
    c_set = set(link_map(C1))
    checks.append((
        "oriented original-link reconstruction gives three four-link plaquettes and one eight-link merged loop",
        all(len(links) == 4 for links in p_sets) and len(c_set) == 8,
    ))
    checks.append((
        "the first two placements are disjoint and the boundary placement shares only oppositely oriented h3",
        not (p_sets[0] & c_set)
        and not (p_sets[1] & c_set)
        and p_sets[2] & c_set == {"h3"}
        and link_map(PLAQUETTES[2])["h3"] == -link_map(C1)["h3"],
    ))
    checks.append((
        "maximal-torus census gives disjoint multiplicities four and eight",
        all(top_edge_label_counts(index, 4) == Counter({1: 8, 4: 4}) for index in (0, 1)),
    ))
    checks.append((
        "maximal-torus census gives shared multiplicities three, seven, and one coupled top label",
        top_edge_label_counts(2, 4) == Counter({1: 7, 4: 3, 5: 1}),
    ))
    checks.append((
        "O(3) defining-vector fusion has a unique unit-coefficient top summand",
        all(top_fusion_multiplicity(spin) == 1 for spin in range(1, MAX_SPIN)),
    ))

    sample = positive_sample()
    checks.append((
        "disjoint census reproduces r_n^4 r_1^8 at every checked spin",
        all(census_crossing(0, spin, sample) == sample[spin] ** 4 * sample[1] ** 8
            for spin in range(1, MAX_SPIN)),
    ))
    checks.append((
        "shared census reproduces r_n^3 r_1^7 r_(n+1) at every checked spin",
        all(census_crossing(2, spin, sample)
            == sample[spin] ** 3 * sample[1] ** 7 * sample[spin + 1]
            for spin in range(1, MAX_SPIN)),
    ))
    checks.append((
        "both disjoint placements have identical positive symmetric factors",
        all(symmetric_factor(0, spin, sample) == symmetric_factor(1, spin, sample) > 0
            for spin in range(1, MAX_SPIN)),
    ))
    checks.append((
        "the shared placement has positive symmetric factors on the supplied-sign domain",
        all(symmetric_factor(2, spin, sample) > 0 for spin in range(1, MAX_SPIN)),
    ))
    c0_set = set(link_map(C0))
    checks.append((
        "physical-Q top channels carry a nontrivial internal-rung label absent from the coarse merged loop",
        not (c0_set & INTERNAL_RUNGS)
        and all(
            any(
                link in INTERNAL_RUNGS and abs(weight) == spin
                for link, weight in maximal_torus_edge_weights(placement, spin).items()
            )
            for placement in range(3)
            for spin in range(1, MAX_SPIN)
        ),
    ))

    identity = {spin: F(1) for spin in range(1, MAX_SPIN + 2)}
    checks.append((
        "identity crossing makes every two-order factor two and every layer coefficient a power of two",
        all(tower_coefficient(placement, 7, identity) == 2 ** 6 for placement in range(3)),
    ))
    signed_cancel = dict(identity)
    signed_cancel[4] = F(-1)
    checks.append((
        "a nonphysical signed shared-rung sample cancels exactly at spin two while disjoint factors do not",
        symmetric_factor(2, 2, signed_cancel) == 0
        and symmetric_factor(0, 2, signed_cancel) != 0,
    ))
    return checks


def all_checks_pass() -> bool:
    return all(passed for _label, passed in run_checks())


def main() -> int:
    checks = run_checks()
    for label, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
    passed = sum(int(value) for _label, value in checks)
    print(f"TOTAL: PASS={passed} FAIL={len(checks) - passed}")
    return int(passed != len(checks))


if __name__ == "__main__":
    raise SystemExit(main())
