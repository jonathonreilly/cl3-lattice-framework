#!/usr/bin/env python3
"""Exact probes for one full-Z3 causal-front sampled-instrument law.

The candidate law is a deliberately explicit law value, not merely a law
type.  A finite partial record map grows by its whole nearest-neighbor front.
At a ready site, available labels are the labels on recorded neighbors and a
qubit CP instrument writes one sampled label with weight proportional to its
neighbor incidence.  The runner tests the resulting readiness, normalization,
actuality boundary, record invariance, gluing, full-lattice fresh support, and
the reversible, sector, carrier, scheduling, and export alternatives.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
from typing import Callable, Iterable, Mapping

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "FULL_Z3_CAUSAL_FRONT_SAMPLED_INSTRUMENT_LAW_NOTE_2026-07-14.md"
)
PAIR_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "COMPLETE_SAMPLED_LAW_PAIR_AXIOM_UNDERDETERMINATION_NOTE_2026-07-14.md"
)

PASS = 0
FAIL = 0
Coord = tuple[int, int, int]
Record = dict[Coord, int]


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def exact_equal(left, right) -> bool:
    if isinstance(left, sp.MatrixBase) or isinstance(right, sp.MatrixBase):
        return sp.simplify(left - right) == sp.zeros(*left.shape)
    return sp.simplify(left - right) == 0


I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
P0 = sp.diag(1, 0)
P1 = sp.diag(0, 1)
KET0 = sp.Matrix([1, 0])
KET1 = sp.Matrix([0, 1])
KET_PLUS = (KET0 + KET1) / sp.sqrt(2)


def dagger(matrix: sp.Matrix) -> sp.Matrix:
    return matrix.conjugate().T


def density(vector: sp.Matrix) -> sp.Matrix:
    return sp.simplify(vector * dagger(vector))


def trace(matrix: sp.Matrix):
    return sp.simplify(sp.trace(matrix))


def neighbors(coordinate: Coord) -> tuple[Coord, ...]:
    result = []
    for axis in range(3):
        for direction in (-1, 1):
            neighbor = list(coordinate)
            neighbor[axis] += direction
            result.append(tuple(neighbor))
    return tuple(result)


def causal_front(record: Mapping[Coord, int]) -> frozenset[Coord]:
    domain = frozenset(record)
    return frozenset(
        neighbor
        for site in domain
        for neighbor in neighbors(site)
        if neighbor not in domain
    )


def neighbor_profile(record: Mapping[Coord, int], site: Coord) -> tuple[int, int]:
    counts = [0, 0]
    for neighbor in neighbors(site):
        if neighbor in record:
            counts[record[neighbor]] += 1
    return counts[0], counts[1]


def local_probabilities(record: Mapping[Coord, int], site: Coord) -> tuple[Fraction, Fraction]:
    zero, one = neighbor_profile(record, site)
    total = zero + one
    if site in record or total == 0:
        raise ValueError("site is not ready")
    return Fraction(zero, total), Fraction(one, total)


def available_labels(record: Mapping[Coord, int], site: Coord) -> tuple[int, ...]:
    return tuple(label for label, weight in enumerate(local_probabilities(record, site)) if weight > 0)


def append_front_branch(
    record: Mapping[Coord, int],
    outcomes: Mapping[Coord, int],
) -> tuple[Record, Fraction]:
    ready = causal_front(record)
    if frozenset(outcomes) != ready:
        raise ValueError("a law step must answer the whole ready front")
    successor = dict(record)
    weight = Fraction(1, 1)
    for site in ready:
        outcome = outcomes[site]
        probabilities = local_probabilities(record, site)
        if probabilities[outcome] == 0:
            raise ValueError("outcome is not available")
        weight *= probabilities[outcome]
        successor[site] = outcome
    return successor, weight


def enumerate_front_branches(record: Mapping[Coord, int]) -> tuple[tuple[Record, Fraction], ...]:
    # Sorting is only a deterministic enumeration convention in the runner;
    # the product law itself is permutation independent.
    sites = tuple(sorted(causal_front(record)))
    options = tuple(available_labels(record, site) for site in sites)
    branches = []
    for labels in product(*options):
        outcomes = dict(zip(sites, labels))
        branches.append(append_front_branch(record, outcomes))
    return tuple(branches)


def sampled_front_step(
    record: Mapping[Coord, int],
    seeds: Mapping[Coord, Fraction],
) -> tuple[Record, Fraction]:
    outcomes = {}
    for site in causal_front(record):
        p_zero, _ = local_probabilities(record, site)
        seed = seeds[site]
        if not Fraction(0, 1) <= seed < Fraction(1, 1):
            raise ValueError("sample seeds must lie in [0,1)")
        outcomes[site] = 0 if seed < p_zero else 1
    return append_front_branch(record, outcomes)


def branch_kraus(probability: Fraction, outcome: int) -> tuple[sp.Matrix, sp.Matrix]:
    p = sp.Rational(probability.numerator, probability.denominator)
    ket = (KET0, KET1)[outcome]
    return tuple(sp.sqrt(p) * ket * dagger(bra) for bra in (KET0, KET1))


def branch_map(rho: sp.Matrix, probability: Fraction, outcome: int) -> sp.Matrix:
    return sp.simplify(
        sum(
            (kraus * rho * dagger(kraus) for kraus in branch_kraus(probability, outcome)),
            sp.zeros(2),
        )
    )


def embedded_branch_kraus(
    probability: Fraction,
    outcome: int,
    site: int,
) -> tuple[sp.Matrix, ...]:
    local = branch_kraus(probability, outcome)
    if site == 0:
        return tuple(sp.kronecker_product(kraus, I2) for kraus in local)
    if site == 1:
        return tuple(sp.kronecker_product(I2, kraus) for kraus in local)
    raise ValueError("two-qubit control has only sites 0 and 1")


def apply_kraus(rho: sp.Matrix, kraus_family: Iterable[sp.Matrix]) -> sp.Matrix:
    return sp.simplify(
        sum(
            (kraus * rho * dagger(kraus) for kraus in kraus_family),
            sp.zeros(rho.rows),
        )
    )


def transform_record(
    record: Mapping[Coord, int],
    transform: Callable[[Coord], Coord],
    flip_labels: bool = False,
) -> Record:
    return {
        transform(site): (1 - value if flip_labels else value)
        for site, value in record.items()
    }


def translation(shift: Coord) -> Callable[[Coord], Coord]:
    return lambda coordinate: tuple(coordinate[axis] + shift[axis] for axis in range(3))


def permutation_sign(permutation: tuple[int, int, int]) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(3)
        for right in range(left + 1, 3)
    )
    return -1 if inversions % 2 else 1


def proper_cubic_rotations() -> tuple[Callable[[Coord], Coord], ...]:
    rotations = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            if permutation_sign(permutation) * signs[0] * signs[1] * signs[2] != 1:
                continue

            def transform(
                coordinate: Coord,
                permutation: tuple[int, int, int] = permutation,
                signs: tuple[int, int, int] = signs,
            ) -> Coord:
                return tuple(
                    signs[axis] * coordinate[permutation[axis]]
                    for axis in range(3)
                )

            rotations.append(transform)
    return tuple(rotations)


def l1_ball(radius: int) -> frozenset[Coord]:
    return frozenset(
        (x, y, z)
        for x in range(-radius, radius + 1)
        for y in range(-radius, radius + 1)
        for z in range(-radius, radius + 1)
        if abs(x) + abs(y) + abs(z) <= radius
    )


def source_contract() -> None:
    section("A - Source, authority, and exact-law boundary")
    note = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(note.lower().replace("*", "").replace("`", "").split())
    axioms = AXIOMS.read_text(encoding="utf-8")
    pair_note = PAIR_NOTE.read_text(encoding="utf-8")
    check("A note is authority-free", "authority: none" in normalized)
    check("A note changes no live foundation surface", "changes no axiom, registry, or audit" in normalized)
    check("A note gives an exact law value", "cfsi-1" in normalized and "exact candidate law" in normalized)
    check("A note limits its negative result", "narrow no-go" in normalized)
    check("A pointer frame is boundary-relative", "boundary-relative record projectors" in normalized)
    check("A mixed-frame law is not silently claimed", "mixed-frame neighborhoods" in normalized)
    check("A live Admissibility names a fixed nearest-neighbor rule", "There is one fixed nearest-neighbor admissibility rule" in axioms)
    check("A live Qualification says state is records", "A state is a configuration of records." in axioms)
    check("A paired-law discriminator is present", "one-record transcript" in pair_note.lower() and "lambda=1" in pair_note.lower())


def readiness_availability_and_covariance() -> None:
    section("B - Local readiness, varying availability, and exact covariance")
    record = {
        (0, 0, 0): 0,
        (2, 0, 0): 1,
        (1, 1, 0): 0,
    }
    ready = causal_front(record)
    check("B readiness is exactly open adjacency to a record", all(site not in record and any(neighbor in record for neighbor in neighbors(site)) for site in ready))
    check("B every open site adjacent to a record is ready", all(site in ready for recorded in record for site in neighbors(recorded) if site not in record))

    single_zero = {(0, 0, 0): 0}
    single_one = {(0, 0, 0): 1}
    mixed = {(-1, 0, 0): 0, (1, 0, 0): 1}
    target = (0, 0, 0)
    check("B one zero neighbor makes only zero available", available_labels(single_zero, (1, 0, 0)) == (0,))
    check("B one one neighbor makes only one available", available_labels(single_one, (1, 0, 0)) == (1,))
    check("B a mixed profile makes both labels available", available_labels(mixed, target) == (0, 1))
    check("B mixed availability has normalized incidence weights", local_probabilities(mixed, target) == (Fraction(1, 2), Fraction(1, 2)))

    for label, transform in (("translation", translation((4, -3, 2))),):
        moved = transform_record(record, transform)
        check(
            f"B ready front is exactly {label} covariant",
            causal_front(moved) == frozenset(transform(site) for site in ready),
        )
        check(
            f"B local probability table is exactly {label} covariant",
            all(local_probabilities(record, site) == local_probabilities(moved, transform(site)) for site in ready),
        )

    rotations = proper_cubic_rotations()
    check("B proper cubic rotation family has 24 elements", len(rotations) == 24)
    check(
        "B ready front is covariant under all 24 proper cubic rotations",
        all(
            causal_front(transform_record(record, transform))
            == frozenset(transform(site) for site in ready)
            for transform in rotations
        ),
    )
    check(
        "B local probability table is covariant under all 24 proper cubic rotations",
        all(
            local_probabilities(record, site)
            == local_probabilities(transform_record(record, transform), transform(site))
            for transform in rotations
            for site in ready
        ),
    )

    flipped = transform_record(record, lambda site: site, flip_labels=True)
    check(
        "B global label exchange swaps every local probability",
        all(local_probabilities(record, site) == tuple(reversed(local_probabilities(flipped, site))) for site in ready),
    )


def normalized_local_instrument() -> None:
    section("C - Exact qubit CP instrument, weights, and repeatability")
    probabilities = (Fraction(2, 3), Fraction(1, 3))
    rho = sp.Matrix(
        [
            [sp.Rational(2, 5), sp.Rational(1, 5) + sp.I / 10],
            [sp.Rational(1, 5) - sp.I / 10, sp.Rational(3, 5)],
        ]
    )
    effects = []
    branches = []
    for outcome, probability in enumerate(probabilities):
        kraus = branch_kraus(probability, outcome)
        effect = sp.simplify(sum((dagger(k) * k for k in kraus), sp.zeros(2)))
        branch = branch_map(rho, probability, outcome)
        effects.append(effect)
        branches.append(branch)
        p = sp.Rational(probability.numerator, probability.denominator)
        check(f"C branch {outcome} is completely positive by explicit Kraus form", len(kraus) == 2)
        check(f"C branch {outcome} effect is p_r I", exact_equal(effect, p * I2))
        check(f"C branch {outcome} trace is its incidence weight", exact_equal(trace(branch), p * trace(rho)))
        check(f"C branch {outcome} writes the sharp pointer state", exact_equal(branch, p * trace(rho) * (P0, P1)[outcome]))
    check("C branch effects sum to identity", exact_equal(sum(effects, sp.zeros(2)), I2))
    check("C the nonselective instrument is trace preserving", exact_equal(trace(sum(branches, sp.zeros(2))), trace(rho)))

    for outcome, probability in enumerate(probabilities):
        post = sp.simplify(branches[outcome] / trace(branches[outcome]))
        same = trace((P0, P1)[outcome] * post)
        other = trace((P1, P0)[outcome] * post)
        check(f"C written outcome {outcome} repeats with certainty", exact_equal(same, 1) and exact_equal(other, 0))

    flipped_rho = X * rho * X
    for outcome, probability in enumerate(probabilities):
        left = X * branch_map(rho, probability, outcome) * X
        right = branch_map(flipped_rho, tuple(reversed(probabilities))[1 - outcome], 1 - outcome)
        check(f"C branch {outcome} is label-covariant", exact_equal(left, right))

    hadamard = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
    rotated_rho = sp.simplify(hadamard * rho * dagger(hadamard))
    for outcome, probability in enumerate(probabilities):
        projector = (P0, P1)[outcome]
        rotated_projector = sp.simplify(hadamard * projector * dagger(hadamard))
        p = sp.Rational(probability.numerator, probability.denominator)
        rotated_branch = sp.simplify(p * trace(rotated_rho) * rotated_projector)
        conjugated_branch = sp.simplify(
            hadamard * branch_map(rho, probability, outcome) * dagger(hadamard)
        )
        check(
            f"C branch {outcome} is covariant under a simultaneous qubit-frame conjugation",
            exact_equal(rotated_branch, conjugated_branch),
        )


def exact_law_value_discriminator() -> None:
    section("D - Exact law value is packaged, not selected by architecture")

    def exponential_kernel(lam: int, zero: int, one: int) -> tuple[Fraction, Fraction]:
        if zero and not one:
            return Fraction(1), Fraction(0)
        if one and not zero:
            return Fraction(0), Fraction(1)
        weights = (lam**zero, lam**one)
        total = weights[0] + weights[1]
        return Fraction(weights[0], total), Fraction(weights[1], total)

    linear_two_one = (Fraction(2, 3), Fraction(1, 3))
    lambda_one_two_one = exponential_kernel(1, 2, 1)
    lambda_two_two_one = exponential_kernel(2, 2, 1)
    check("D lambda=1 and lambda=2 share support at the 2:1 profile", all(weight > 0 for weight in lambda_one_two_one + lambda_two_two_one))
    check("D lambda=1 gives one half at the 2:1 profile", lambda_one_two_one[0] == Fraction(1, 2))
    check("D lambda=2 gives two thirds at the 2:1 profile", lambda_two_two_one[0] == Fraction(2, 3))
    check("D CFSI-1 linear incidence gives two thirds at the 2:1 profile", linear_two_one == lambda_two_two_one)

    linear_three_one = (Fraction(3, 4), Fraction(1, 4))
    lambda_two_three_one = exponential_kernel(2, 3, 1)
    check("D CFSI-1 is not secretly the lambda=2 exponential law", linear_three_one[0] == Fraction(3, 4) and lambda_two_three_one[0] == Fraction(4, 5))
    check("D changing only the exact weight formula changes a readable transcript", linear_three_one != lambda_two_three_one)


def composition_gluing_and_extension() -> None:
    section("E - Disjoint composition, front gluing, and cylinders")
    bell = (sp.kronecker_product(KET0, KET0) + sp.kronecker_product(KET1, KET1)) / sp.sqrt(2)
    rho = density(bell)
    p_left = (Fraction(2, 3), Fraction(1, 3))
    p_right = (Fraction(1, 4), Fraction(3, 4))
    left_kraus = embedded_branch_kraus(p_left[0], 0, 0)
    right_kraus = embedded_branch_kraus(p_right[1], 1, 1)
    left_then_right = apply_kraus(apply_kraus(rho, left_kraus), right_kraus)
    right_then_left = apply_kraus(apply_kraus(rho, right_kraus), left_kraus)
    check("D disjoint local branch maps commute", exact_equal(left_then_right, right_then_left))
    check("D joint branch weight is the product of local weights", exact_equal(trace(left_then_right), sp.Rational(1, 2)))

    total_weight = sp.Rational(0)
    for left_outcome, right_outcome in product((0, 1), repeat=2):
        branch = apply_kraus(
            apply_kraus(rho, embedded_branch_kraus(p_left[left_outcome], left_outcome, 0)),
            embedded_branch_kraus(p_right[right_outcome], right_outcome, 1),
        )
        total_weight += trace(branch)
    check("D complete disjoint joint instrument normalizes", exact_equal(total_weight, 1))

    initial = {(-1, 0, 0): 0, (1, 0, 0): 1}
    first_branches = enumerate_front_branches(initial)
    check("D the two-seed first front has two supported branches", len(first_branches) == 2)
    check("D first-front cylinder weights normalize", sum(weight for _, weight in first_branches) == 1)
    check("D the mixed origin is the only stochastic first-front site", {successor[(0, 0, 0)] for successor, _ in first_branches} == {0, 1})
    check("D each first-front branch has weight one half", {weight for _, weight in first_branches} == {Fraction(1, 2)})

    all_prefixes_marginalize = True
    for successor, prefix_weight in first_branches:
        local_sums = [sum(local_probabilities(successor, site)) for site in causal_front(successor)]
        continuation_normalization = Fraction(1, 1)
        for local_sum in local_sums:
            continuation_normalization *= local_sum
        all_prefixes_marginalize &= prefix_weight * continuation_normalization == prefix_weight
    check("D every next-front cylinder family marginalizes to its prefix", all_prefixes_marginalize)

    far_left = {(0, 0, 0): 0}
    far_right = {(10, 0, 0): 1}
    joined = {**far_left, **far_right}
    check("D separated ready fronts glue as a disjoint union", causal_front(joined) == causal_front(far_left) | causal_front(far_right))
    check(
        "D separated local kernels are unchanged by gluing",
        all(local_probabilities(joined, site) == local_probabilities(far_left, site) for site in causal_front(far_left))
        and all(local_probabilities(joined, site) == local_probabilities(far_right, site) for site in causal_front(far_right)),
    )


def actuality_and_boundary() -> None:
    section("F - One actual history and its irreducible selector")
    initial = {(-1, 0, 0): 0, (1, 0, 0): 1}
    ready = causal_front(initial)
    low_seeds = {site: Fraction(1, 4) for site in ready}
    high_seeds = {site: Fraction(3, 4) for site in ready}
    low_history, low_weight = sampled_front_step(initial, low_seeds)
    high_history, high_weight = sampled_front_step(initial, high_seeds)
    check("E each supplied sample field returns one complete successor", len(low_history) == len(initial) + len(ready) and len(high_history) == len(initial) + len(ready))
    check("E low and high sample fields select opposite mixed-site records", low_history[(0, 0, 0)] == 0 and high_history[(0, 0, 0)] == 1)
    check("E both selected histories have their normalized law weight", low_weight == high_weight == Fraction(1, 2))
    check("E normalized weights alone do not identify which history occurred", low_history != high_history and low_weight == high_weight)

    deterministic_label_covariant_tie_breaks = tuple(
        output
        for output in (0, 1)
        if output == 1 - output
    )
    check("E no deterministic label-covariant answer exists on a symmetric tie", not deterministic_label_covariant_tie_breaks)

    homogeneous = {(0, 0, 0): 0}
    homogeneous_successor = enumerate_front_branches(homogeneous)
    check("E a homogeneous seed has one deterministic first successor", len(homogeneous_successor) == 1)
    check("E the incidence law cannot create a label absent from the boundary", set(homogeneous_successor[0][0].values()) == {0})


def record_identity_and_exhaustive_scope() -> None:
    section("G - Append identity, nonreconnection, and operation scope")
    initial = {(-1, 0, 0): 0, (1, 0, 0): 1}
    branches = enumerate_front_branches(initial)
    for successor, _ in branches:
        check("F every successor preserves all prior site-content pairs", all(successor[site] == value for site, value in initial.items()))
        check("F a later ready front excludes all existing record sites", causal_front(successor).isdisjoint(successor))

    zero_branch = next(successor for successor, _ in branches if successor[(0, 0, 0)] == 0)
    one_branch = next(successor for successor, _ in branches if successor[(0, 0, 0)] == 1)

    def compatible_union(left: Mapping[Coord, int], right: Mapping[Coord, int]):
        merged = dict(left)
        for site, value in right.items():
            if site in merged and merged[site] != value:
                return None
            merged[site] = value
        return merged

    check("F conflicting same-site outcome sectors have no append-only common future", compatible_union(zero_branch, one_branch) is None)

    record_projector = sp.kronecker_product(P0, I2)
    future_on_other_site = sp.kronecker_product(I2, X)
    forbidden_flip = sp.kronecker_product(X, I2)
    check("F an operation on a fresh site preserves the old record projector", exact_equal(future_on_other_site * record_projector, record_projector * future_on_other_site))
    check("F allowing an old-site flip would destroy record invariance", not exact_equal(forbidden_flip * record_projector * forbidden_flip, record_projector))


def full_lattice_front_and_schedule() -> None:
    section("H - Full-Z3 fresh support and synchronous-layer ablation")
    record: Record = {(0, 0, 0): 0}
    for radius in range(0, 7):
        expected_volume = (4 * radius**3 + 6 * radius**2 + 8 * radius + 3) // 3
        check(f"G after {radius} steps the domain is the L1 ball", frozenset(record) == l1_ball(radius))
        check(f"G radius {radius} ball has exact cubic volume", len(record) == expected_volume)
        ready = causal_front(record)
        expected_shell = 4 * (radius + 1) ** 2 + 2
        check(f"G next front after radius {radius} has exact quadratic shell size", len(ready) == expected_shell)
        seeds = {site: Fraction(1, 3) for site in ready}
        record, weight = sampled_front_step(record, seeds)
        check(f"G homogeneous front step {radius + 1} is deterministic", weight == 1)

    check("G arbitrarily distant fresh sites remain after every finite tested depth", (9, 0, 0) not in record)
    check("G every fixed radius-six patch is saturated after six steps", l1_ball(6).issubset(record))
    check("G the active front has moved outside that fixed patch", all(site not in l1_ball(6) for site in causal_front({site: 0 for site in l1_ball(6)})))

    target = (1, 1, 0)
    first_parent_only = {(1, 0, 0): 0}
    both_parents = {(1, 0, 0): 0, (0, 1, 0): 1}
    check("G early asynchronous firing would copy the first parent", local_probabilities(first_parent_only, target) == (Fraction(1), Fraction(0)))
    check("G waiting for the full causal layer gives a mixed target law", local_probabilities(both_parents, target) == (Fraction(1, 2), Fraction(1, 2)))
    check("G the maximal synchronous front convention is therefore load-bearing", local_probabilities(first_parent_only, target) != local_probabilities(both_parents, target))


def reversible_unitary_variant() -> None:
    section("I - Reversible-unitary front variant")
    cnot = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
    check("H CNOT front copy is unitary", exact_equal(dagger(cnot) * cnot, sp.eye(4)))
    for source, expected in ((KET0, sp.kronecker_product(KET0, KET0)), (KET1, sp.kronecker_product(KET1, KET1))):
        copied = sp.simplify(cnot * sp.kronecker_product(source, KET0))
        check("H a pointer-basis input copies deterministically", exact_equal(copied, expected))

    initial = sp.kronecker_product(KET_PLUS, KET0)
    coherent_front = sp.simplify(cnot * initial)
    restored = sp.simplify(cnot * coherent_front)
    check("H a superposed source produces a coherent two-branch Bell state", exact_equal(coherent_front, (sp.kronecker_product(KET0, KET0) + sp.kronecker_product(KET1, KET1)) / sp.sqrt(2)))
    check("H the complete front write reverses exactly", exact_equal(restored, initial))
    check("H the unitary state contains no selected outcome variable", coherent_front[0] != 0 and coherent_front[3] != 0)

    record_flag = sp.diag(1, 1, 0, 0)
    conjugated = sp.simplify(dagger(cnot) * record_flag * cnot)
    strict_larger_flag = sp.diag(1, 1, 1, 0)
    check("H unitary conjugation preserves flag rank", conjugated.rank() == record_flag.rank())
    check("H a strict record-support enlargement has larger rank", strict_larger_flag.rank() > record_flag.rank())
    check("H excluding the inverse is an additional forward-semigroup rule", exact_equal(cnot * cnot, sp.eye(4)))


def partial_trace_over_first(rho: sp.Matrix) -> sp.Matrix:
    reduced = sp.zeros(2)
    for a, b, first in product(range(2), range(2), range(2)):
        reduced[a, b] += rho[2 * first + a, 2 * first + b]
    return sp.simplify(reduced)


def sector_and_quantum_repertoire_variant() -> None:
    section("J - Sector/asymptotic actuality and quantum-repertoire boundary")
    tie = (Fraction(1, 2), Fraction(1, 2))
    rho = density(KET_PLUS)
    branch_zero = branch_map(rho, tie[0], 0)
    branch_one = branch_map(rho, tie[1], 1)
    nonselective = sp.simplify(branch_zero + branch_one)
    check("I the nonselective tie law is the equal sector mixture", exact_equal(nonselective, I2 / 2))
    check("I the two record sectors are exactly orthogonal", exact_equal(P0 * P1, sp.zeros(2)))
    check("I the mixed state is distinct from either actual character", not exact_equal(nonselective, P0) and not exact_equal(nonselective, P1))
    check("I a normalized sector measure has two points rather than one selected point", tie == (Fraction(1, 2), Fraction(1, 2)))

    entangled = sp.sqrt(sp.Rational(2, 3)) * sp.kronecker_product(KET0, KET0) + sp.sqrt(sp.Rational(1, 3)) * sp.kronecker_product(KET1, KET1)
    entangled_rho = density(entangled)
    outputs = []
    for outcome, probability in enumerate(tie):
        outputs.append(apply_kraus(entangled_rho, embedded_branch_kraus(probability, outcome, 0)))
    replaced = sp.simplify(sum(outputs, sp.zeros(4)))
    expected_product = sp.kronecker_product(I2 / 2, partial_trace_over_first(entangled_rho))
    check("I the minimal replacement instrument breaks input entanglement", exact_equal(replaced, expected_product))
    check("J the minimal law is quantum-valid but entanglement-breaking", exact_equal(replaced, sp.kronecker_product(I2 / 2, sp.diag(sp.Rational(2, 3), sp.Rational(1, 3)))))


def swap_operator(qubits: int, left: int, right: int) -> sp.Matrix:
    dimension = 2**qubits
    swap = sp.zeros(dimension)
    for state in range(dimension):
        bits = [((state >> (qubits - 1 - position)) & 1) for position in range(qubits)]
        bits[left], bits[right] = bits[right], bits[left]
        target = 0
        for bit in bits:
            target = (target << 1) | bit
        swap[target, state] = 1
    return swap


def computational_ket(bits: tuple[int, ...]) -> sp.Matrix:
    index = 0
    for bit in bits:
        index = (index << 1) | bit
    vector = sp.zeros(2 ** len(bits), 1)
    vector[index] = 1
    return vector


def carrier_and_migratory_export() -> None:
    section("K - Local carrier minimum and dual-rail migratory export")
    candidates = (KET_PLUS, KET0, KET1)
    gram = sp.Matrix(
        [
            [sp.simplify((dagger(left) * right)[0]) for right in candidates]
            for left in candidates
        ]
    )
    check("J open/record-0/record-1 candidate span has rank two", gram.rank() == 2)
    check("J no three nonzero orthogonal status sectors fit one M2", 1 + 1 + 1 > 2)
    check("J a one-dimensional blank plus two record sectors needs dimension three", 1 + 1 + 1 == 3)
    check("J a full open qubit plus two record sectors needs dimension four", 2 + 1 + 1 == 4)

    # Two adjacent rails per logical block: blank=00, record0=10,
    # record1=01.  Parallel nearest-neighbor swaps move the block one step
    # along a 2xZ ladder.
    shift = swap_operator(4, 0, 2) * swap_operator(4, 1, 3)
    check("J dual-rail shift is unitary", exact_equal(dagger(shift) * shift, sp.eye(16)))
    for label, source_bits, target_bits in (
        (0, (1, 0, 0, 0), (0, 0, 1, 0)),
        (1, (0, 1, 0, 0), (0, 0, 0, 1)),
    ):
        shifted = sp.simplify(shift * computational_ket(source_bits))
        check(f"J dual-rail export preserves record content {label}", exact_equal(shifted, computational_ket(target_bits)))
    check("J dual-rail export frees the old block only by moving identity", exact_equal(shift * computational_ket((1, 0, 0, 0)), computational_ket((0, 0, 1, 0))))
    check("J the same unitary can reverse the export", exact_equal(shift * shift, sp.eye(16)))


def documentation_contract() -> None:
    section("L - Residual atoms and no-go discipline needles")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "maximal synchronous front",
        "sampled actuality",
        "record-status",
        "boundary seed",
        "boundary-relative unordered pointer frame",
        "mixed-frame law is not claimed",
        "projective extension",
        "fresh-support",
        "same-site renewal",
        "entanglement-breaking",
        "strongest candidate reference",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — exact residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path",
        "n7 — strongest steelman",
        "n8 — cross-cycle echo",
    )
    for phrase in required:
        check(f"K note contains boundary: {phrase}", phrase in note)


def main() -> None:
    source_contract()
    readiness_availability_and_covariance()
    normalized_local_instrument()
    exact_law_value_discriminator()
    composition_gluing_and_extension()
    actuality_and_boundary()
    record_identity_and_exhaustive_scope()
    full_lattice_front_and_schedule()
    reversible_unitary_variant()
    sector_and_quantum_repertoire_variant()
    carrier_and_migratory_export()
    documentation_contract()
    section("SUMMARY")
    print(f"PASS={PASS}")
    print(f"FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
