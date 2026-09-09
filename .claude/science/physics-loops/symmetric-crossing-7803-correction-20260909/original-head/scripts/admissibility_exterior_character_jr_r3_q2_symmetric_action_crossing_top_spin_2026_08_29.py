#!/usr/bin/env python3
"""Exact certificate for the two-order local action/crossing top branch.

The parent finite-step response is proportional to B C_c + C B.  On the
fine residual packet this becomes A C + C A with A=(I-Q)M_V.  This runner
checks the complete two-order coefficient on all three admissible plaquette
placements, including the coupled shared-rung original-link census.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path

import admissibility_exterior_character_jr_r3_q2_symmetric_action_crossing_top_spin_independent_2026_08_29 as independent


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 30
MAX_LAYER = 8
AUDIT_INPUT_PATHS = (
    "scripts/admissibility_exterior_character_jr_r3_q2_symmetric_action_crossing_top_spin_independent_2026_08_29.py",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R3_Q2_SYMMETRIC_ACTION_CROSSING_TOP_SPIN_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R3_Q2_PHYSICAL_Q_ACTION_CROSSING_TOWER_NO_GO_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R3_Q2_ADJACENT_PRODUCT_CUBIC_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_TEMPORAL_SPATIAL_SEMIGROUP_DEFECT_GENERATED_INTERACTION_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_TIME_REFINEMENT_SEMIGROUP_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE = ROOT / AUDIT_INPUT_PATHS[1]
TRIVIAL = (0, 1)
VECTOR = (1, -1)
PLACEMENTS = ("p0_disjoint", "p1_disjoint", "p2_shared_h3")
MUTATIONS = (
    "drop_pre_crossing_order",
    "subtract_operator_orders",
    "p_edge_power_4_to_3",
    "spectator_power_8_to_7",
    "shared_as_disjoint",
    "shared_rung_double_count",
    "shared_top_fusion_not_unit",
    "replace_physical_q_with_static_cup",
    "claim_mixed_placement_completion",
    "claim_full_exponential_completion",
    "claim_invariant_closure",
    "claim_global_memory",
    "claim_signed_control_is_physical",
    "axiom_edit",
)
SCOPE_MUTATIONS = {
    "replace_physical_q_with_static_cup": (
        "Physical `Q` here is conditional Haar and is not a static cup projector.",
        "Physical `Q` here is a static cup projector.",
    ),
    "claim_mixed_placement_completion": (
        "Mixed-placement histories are not evaluated by this coefficient theorem.",
        "Mixed-placement histories are completely classified.",
    ),
    "claim_full_exponential_completion": (
        "The full action exponential is not evaluated by this coefficient theorem.",
        "The full action exponential is included in this result.",
    ),
    "claim_invariant_closure": (
        "No invariant-closure statement is proposed.",
        "Invariant closure of the physical response is proved.",
    ),
    "claim_global_memory": (
        "No global minimal-memory statement is proposed.",
        "Global minimal memory is determined.",
    ),
    "claim_signed_control_is_physical": (
        "The signed cancellation control lies outside the supplied positive multiplier domain.",
        "The signed cancellation control lies inside the supplied positive multiplier domain.",
    ),
    "axiom_edit": (
        "No axiom or approved primitive is edited.",
        "An axiom or approved primitive is edited.",
    ),
}


@dataclass(frozen=True)
class Sample:
    name: str
    determinant: F
    spins: tuple[F, ...]


def make_samples() -> tuple[Sample, ...]:
    positive_a = Sample(
        "positive_a",
        F(1, 5),
        (F(1),) + tuple(F(spin + 2, 2 * spin + 5) for spin in range(1, MAX_LAYER + 2)),
    )
    positive_b = Sample(
        "positive_b",
        F(2, 7),
        (F(1),) + tuple(F(2 * spin + 1, 3 * spin + 4) for spin in range(1, MAX_LAYER + 2)),
    )
    signed = Sample(
        "signed",
        F(-2, 7),
        (F(1),) + tuple(
            F((-1) ** spin * (spin + 1), 4 * spin + 5)
            for spin in range(1, MAX_LAYER + 2)
        ),
    )
    identity = Sample("identity", F(1), (F(1),) * (MAX_LAYER + 2))
    haar = Sample("Haar", F(0), (F(1),) + (F(0),) * (MAX_LAYER + 1))
    spectator_zero_spins = list(positive_a.spins)
    spectator_zero_spins[1] = F(0)
    spectator_zero = Sample("spectator_zero", positive_a.determinant, tuple(spectator_zero_spins))
    return positive_a, positive_b, signed, identity, haar, spectator_zero


POSITIVE_A, POSITIVE_B, SIGNED, IDENTITY, HAAR, SPECTATOR_ZERO = make_samples()


def add_term(table: dict[tuple[int, int], F], irrep: tuple[int, int], value: F) -> None:
    table[irrep] = table.get(irrep, F(0)) + value
    if not table[irrep]:
        table.pop(irrep)


def add_tables(*tables: dict[tuple[int, int], F]) -> dict[tuple[int, int], F]:
    result: dict[tuple[int, int], F] = {}
    for table in tables:
        for irrep, value in table.items():
            add_term(result, irrep, value)
    return result


def defining_vector_multiply(table: dict[tuple[int, int], F]) -> dict[tuple[int, int], F]:
    result: dict[tuple[int, int], F] = {}
    for (spin, parity), coefficient in table.items():
        outputs = (1,) if spin == 0 else range(spin - 1, spin + 2)
        for output_spin in outputs:
            add_term(result, (output_spin, -parity), coefficient)
    return result


def physical_q_residual(table: dict[tuple[int, int], F]) -> dict[tuple[int, int], F]:
    result = dict(table)
    result.pop(TRIVIAL, None)
    return result


def irrep_multiplier(irrep: tuple[int, int], sample: Sample) -> F:
    spin, parity = irrep
    if irrep == TRIVIAL:
        return F(1)
    if spin == 0:
        if parity != -1:
            raise AssertionError("unexpected spin-zero parity")
        return sample.determinant
    return sample.spins[spin]


def disjoint_crossing_eigenvalue(irrep: tuple[int, int], sample: Sample) -> F:
    return irrep_multiplier(irrep, sample) ** 4 * sample.spins[1] ** 8


def disjoint_crossing(
    table: dict[tuple[int, int], F], sample: Sample
) -> dict[tuple[int, int], F]:
    return {
        irrep: coefficient * disjoint_crossing_eigenvalue(irrep, sample)
        for irrep, coefficient in table.items()
        if coefficient * disjoint_crossing_eigenvalue(irrep, sample)
    }


def symmetric_disjoint_layer(
    table: dict[tuple[int, int], F], sample: Sample
) -> dict[tuple[int, int], F]:
    """A C + C A on a disjoint packet, operators acting right to left."""
    pre_crossed = physical_q_residual(defining_vector_multiply(disjoint_crossing(table, sample)))
    post_crossed = disjoint_crossing(physical_q_residual(defining_vector_multiply(table)), sample)
    return add_tables(pre_crossed, post_crossed)


def symmetric_disjoint_recurrence(
    table: dict[tuple[int, int], F], sample: Sample
) -> dict[tuple[int, int], F]:
    result: dict[tuple[int, int], F] = {}
    for input_irrep, coefficient in table.items():
        spin, parity = input_irrep
        outputs = (1,) if spin == 0 else range(spin - 1, spin + 2)
        for output_spin in outputs:
            output_irrep = (output_spin, -parity)
            if output_irrep == TRIVIAL:
                continue
            factor = (
                disjoint_crossing_eigenvalue(input_irrep, sample)
                + disjoint_crossing_eigenvalue(output_irrep, sample)
            )
            add_term(result, output_irrep, coefficient * factor)
    return result


def crossing_top(placement: int, spin: int, sample: Sample) -> F:
    if placement in (0, 1):
        return sample.spins[spin] ** 4 * sample.spins[1] ** 8
    if placement == 2:
        return sample.spins[spin] ** 3 * sample.spins[1] ** 7 * sample.spins[spin + 1]
    raise ValueError(f"unknown placement {placement}")


def symmetric_top_factor(placement: int, spin: int, sample: Sample) -> F:
    return crossing_top(placement, spin, sample) + crossing_top(placement, spin + 1, sample)


def top_formula(placement: int, layer: int, sample: Sample) -> F:
    result = F(1)
    for spin in range(1, layer):
        result *= symmetric_top_factor(placement, spin, sample)
    return result


def disjoint_tower(sample: Sample, last_layer: int = MAX_LAYER) -> list[dict[tuple[int, int], F]]:
    levels = [{VECTOR: F(1)}]
    while len(levels) < last_layer:
        levels.append(symmetric_disjoint_layer(levels[-1], sample))
    return levels


def independent_sample(sample: Sample) -> dict[int, F]:
    return {spin: sample.spins[spin] for spin in range(1, MAX_LAYER + 2)}


def scope_check(mutation: str | None = None) -> bool:
    text = " ".join(NOTE.read_text(encoding="utf-8").split())
    required = tuple(source for source, _replacement in SCOPE_MUTATIONS.values())
    if mutation in SCOPE_MUTATIONS:
        source, replacement = SCOPE_MUTATIONS[mutation]
        if text.count(source) != 1:
            raise AssertionError(f"scope mutation source count for {mutation}: {text.count(source)}")
        text = text.replace(source, replacement, 1)
    return all(phrase in text for phrase in required)


def mutation_detected(mutation: str) -> bool:
    if mutation == "drop_pre_crossing_order":
        return symmetric_top_factor(0, 3, POSITIVE_A) != crossing_top(0, 4, POSITIVE_A)
    if mutation == "subtract_operator_orders":
        hostile = crossing_top(0, 3, IDENTITY) - crossing_top(0, 4, IDENTITY)
        return hostile == 0 and symmetric_top_factor(0, 3, IDENTITY) == 2
    if mutation in {"p_edge_power_4_to_3", "spectator_power_8_to_7"}:
        p_power = 3 if mutation == "p_edge_power_4_to_3" else 4
        c_power = 7 if mutation == "spectator_power_8_to_7" else 8
        hostile = POSITIVE_A.spins[3] ** p_power * POSITIVE_A.spins[1] ** c_power
        oracle = independent.census_crossing(0, 3, independent_sample(POSITIVE_A))
        return hostile != oracle
    if mutation == "shared_as_disjoint":
        hostile = POSITIVE_A.spins[3] ** 4 * POSITIVE_A.spins[1] ** 8
        oracle = independent.census_crossing(2, 3, independent_sample(POSITIVE_A))
        return hostile != oracle
    if mutation == "shared_rung_double_count":
        hostile = (
            POSITIVE_A.spins[3] ** 4
            * POSITIVE_A.spins[1] ** 8
            * POSITIVE_A.spins[4]
        )
        oracle = independent.census_crossing(2, 3, independent_sample(POSITIVE_A))
        return hostile != oracle
    if mutation == "shared_top_fusion_not_unit":
        hostile = F(4, 7) * symmetric_top_factor(2, 3, POSITIVE_A)
        oracle = independent.symmetric_factor(2, 3, independent_sample(POSITIVE_A))
        return hostile != oracle
    return scope_check() and not scope_check(mutation)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mutation-suite", action="store_true")
    arguments = parser.parse_args()
    if arguments.mutation_suite:
        detected = 0
        for mutation in MUTATIONS:
            caught = mutation_detected(mutation)
            detected += int(caught)
            print(f"[{'PASS' if caught else 'FAIL'}] mutation rejected: {mutation}")
        print(f"TOTAL: PASS={detected} FAIL={len(MUTATIONS) - detected}")
        return int(detected != len(MUTATIONS))
    if arguments.mutation:
        caught = mutation_detected(arguments.mutation)
        print(f"[{'PASS' if caught else 'FAIL'}] mutation rejected: {arguments.mutation}")
        print(f"TOTAL: PASS={int(caught)} FAIL={int(not caught)}")
        return int(not caught)

    checks: list[tuple[str, bool]] = []

    def check(label: str, condition: bool) -> None:
        checks.append((label, bool(condition)))
        print(f"[{'PASS' if condition else 'FAIL'}] {label}")

    for sample in (POSITIVE_A, POSITIVE_B, SIGNED):
        levels = disjoint_tower(sample)
        check(
            f"{sample.name}: direct A C + C A composition equals the independent coefficient recurrence",
            all(
                symmetric_disjoint_layer(levels[index], sample)
                == symmetric_disjoint_recurrence(levels[index], sample)
                for index in range(MAX_LAYER - 1)
            ),
        )
        check(
            f"{sample.name}: both disjoint placements have the exact all-layer top coefficient",
            all(
                levels[layer - 1].get((layer, (-1) ** layer), F(0))
                == top_formula(0, layer, sample)
                == top_formula(1, layer, sample)
                for layer in range(1, MAX_LAYER + 1)
            ),
        )
        check(
            f"{sample.name}: physical conditional-Haar scalar is absent at every disjoint layer",
            all(level.get(TRIVIAL, F(0)) == 0 for level in levels),
        )
        check(
            f"{sample.name}: primary top factors match the independent original-link census on all placements",
            all(
                symmetric_top_factor(placement, spin, sample)
                == independent.symmetric_factor(placement, spin, independent_sample(sample))
                for placement in range(3)
                for spin in range(1, MAX_LAYER)
            ),
        )

    check(
        "supplied-sign controls reinforce on both disjoint placements and the shared-rung placement",
        all(
            symmetric_top_factor(placement, spin, sample) > 0
            for sample in (POSITIVE_A, POSITIVE_B)
            for placement in range(3)
            for spin in range(1, MAX_LAYER)
        ),
    )
    check(
        "identity crossing gives factor two per layer for every placement",
        all(
            symmetric_top_factor(placement, spin, IDENTITY) == 2
            and top_formula(placement, MAX_LAYER, IDENTITY) == 2 ** (MAX_LAYER - 1)
            for placement in range(3)
            for spin in range(1, MAX_LAYER)
        ),
    )
    check(
        "Haar endpoint kills every crossed top factor",
        all(symmetric_top_factor(placement, spin, HAAR) == 0
            for placement in range(3) for spin in range(1, MAX_LAYER)),
    )
    check(
        "zero defining-vector spectator kills every placement even with higher multipliers live",
        all(symmetric_top_factor(placement, spin, SPECTATOR_ZERO) == 0
            for placement in range(3) for spin in range(1, MAX_LAYER)),
    )

    signed_cancel_spins = list(IDENTITY.spins)
    signed_cancel_spins[4] = F(-1)
    signed_cancel = Sample("signed_cancel", F(1), tuple(signed_cancel_spins))
    check(
        "shared placement has an exact signed cancellation locus outside the positive supplied domain",
        symmetric_top_factor(2, 2, signed_cancel) == 0
        and symmetric_top_factor(0, 2, signed_cancel) == 2,
    )
    check(
        "real disjoint order terms cannot cancel unless both fourth-power terms vanish",
        all(
            symmetric_top_factor(0, spin, SIGNED) != 0
            for spin in range(1, MAX_LAYER)
        ),
    )
    response_scalar = -F(3, 10) * F(5, 7) / 2
    independent_pre = response_scalar * independent.census_crossing(
        2, 3, independent_sample(POSITIVE_A)
    )
    independent_post = response_scalar * independent.census_crossing(
        2, 4, independent_sample(POSITIVE_A)
    )
    check(
        "one-step parent scalar preserves the independently reconstructed two-order addition and common sign",
        response_scalar * symmetric_top_factor(2, 3, POSITIVE_A)
        == independent_pre + independent_post
        and independent_pre < 0
        and independent_post < 0,
    )
    check("scope locks preserve all open boundaries", scope_check())
    check("independent maximal-torus and original-link implementation", independent.all_checks_pass())

    print("placement_link_counts", {
        PLACEMENTS[index]: dict(sorted(independent.top_edge_label_counts(index, 4).items()))
        for index in range(3)
    })
    print("positive_layer8_top", {
        PLACEMENTS[index]: str(top_formula(index, MAX_LAYER, POSITIVE_A))
        for index in range(3)
    })
    print("signed_shared_cancellation_spin", 2)
    print("per_element: checked and executed — both operator orders and exact top coefficients were compared term by term")
    print("per_site: checked and not executed — no physical site-evolution or sitewise dynamics statement is made")
    print("per_mode: checked and not executed — no momentum, continuum, or normal-mode construction enters this packet")
    print("per_block: checked and executed — all three fine-plaquette placements in the supplied two-cell local geometry were tested")
    print("lattice_wide: checked and not executed — mixed placements, invariant closure, and global memory are not inferred")
    passed = sum(int(condition) for _label, condition in checks)
    print(f"TOTAL: PASS={passed} FAIL={len(checks) - passed}")
    return int(passed != len(checks))


if __name__ == "__main__":
    raise SystemExit(main())
