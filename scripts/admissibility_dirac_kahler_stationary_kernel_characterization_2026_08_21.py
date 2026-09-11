#!/usr/bin/env python3
"""Corrected Block 173 certificate for normalized finite extension systems."""

from __future__ import annotations

import sys

import sympy as sp

import admissibility_dirac_kahler_released7315_d_fixture_helpers_2026_09_11 as h


AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_STATIONARY_KERNEL_CHARACTERIZATION_BOUNDED_THEOREM_NOTE_2026-08-21.md",
    ".claude/science/physics-loops/toe-axiom-closure-block173-stationary-kernel-characterization-20260821/NO_GO_LEDGER.md",
    "scripts/admissibility_dirac_kahler_released7315_d_fixture_helpers_2026_09_11.py",
    "scripts/admissibility_dirac_kahler_refinement_census_stationary_kernel_2026_08_21.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_REFINEMENT_CENSUS_STATIONARY_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md",
    "scripts/admissibility_dirac_kahler_generator_trilemma_kernel_2026_08_21.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_GENERATOR_TRILEMMA_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md",
    "scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)

INPUT_SHA256 = {'docs/ADMISSIBILITY_DIRAC_KAHLER_STATIONARY_KERNEL_CHARACTERIZATION_BOUNDED_THEOREM_NOTE_2026-08-21.md': 'bd8bb7692a6233355bbd09985022c612ba52db6a555c1b1cc53e4c6bb4395495',
 '.claude/science/physics-loops/toe-axiom-closure-block173-stationary-kernel-characterization-20260821/NO_GO_LEDGER.md': '3a9838fa11560473cf9052f3499fcadde8723b605563575f8919140fc7f76196',
 'scripts/admissibility_dirac_kahler_released7315_d_fixture_helpers_2026_09_11.py': '04ef3fdfe36d7328b827fe448a19ca432f4a8ecefd8b833b0905a9e38c52bbbf',
 'scripts/admissibility_dirac_kahler_refinement_census_stationary_kernel_2026_08_21.py': '3d17c5f9adf1f1808774ee38b254f71511fdbbabca9d782ed1ef4b8114552a7e',
 'docs/ADMISSIBILITY_DIRAC_KAHLER_REFINEMENT_CENSUS_STATIONARY_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md': '97f1e0ddc7df9af5ab0f315e1da69a88292f7d710ca91dc860aff71b6e7196e5',
 'scripts/admissibility_dirac_kahler_generator_trilemma_kernel_2026_08_21.py': '0d9cf17034fe5aa1229ea3c707b2e67534cb860ba5591160ad34e17bee15f09a',
 'docs/ADMISSIBILITY_DIRAC_KAHLER_GENERATOR_TRILEMMA_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md': '6ef3dbeea1b42d03992409377000aa9ef80e4c8653351f258177603b54c42e14',
 'scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py': '0974a71bab3c753e66692740e303ea8062bfa7b6bd88fdc4a2c665d61ac95f87',
 'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py': '5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445',
 'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md': '9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33',
 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
 'docs/audit/data/axiom_premise_nodes.json': '615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37'}

REQUIRED_CLAIM_KEYS = (
    "input_closure",
    "normalized_kernel_criterion",
    "supplied_rank_three_systems",
    "singular_feasible_control",
    "zero_shear_nonuniqueness",
    "finite_sign_endpoints",
    "five_finite_iterates",
    "defect_vector_identity",
    "exact_finite_scope",
)


def build_claims(mutation: str = "") -> dict[str, bool]:
    claims = {key: True for key in REQUIRED_CLAIM_KEYS}
    if mutation == "drop_key":
        claims.pop(REQUIRED_CLAIM_KEYS[-1])
    return claims


def matrix_vector(values) -> sp.Matrix:
    return sp.Matrix(tuple(values))


def supplied_system(tag: str, cover_t: int, lx: int, **parameters) -> dict:
    fixture = h.RecordProfileFixture(tag, cover_t, lx)
    slot = fixture.slots[0]
    p0, extensions, transition, influence = fixture.system(
        {}, slot, **parameters
    )
    result = h.normalizable_kernel(influence)
    representative = (
        None if result.representative is None else matrix_vector(result.representative)
    )
    p0_vector = matrix_vector(p0)
    column_sums = tuple(
        sp.expand(sum(transition[:, column])) for column in range(transition.cols)
    )
    return {
        "fixture": fixture,
        "slot": slot,
        "p0": p0_vector,
        "extensions": extensions,
        "transition": transition,
        "influence": influence,
        "kernel": result,
        "representative": representative,
        "column_sums": column_sums,
        "equation": bool(
            representative is not None
            and h.zero(sp.expand(transition * representative - p0_vector))
            and sp.expand(sum(representative) - 1) == 0
            and h.zero(sp.expand(influence * representative))
        ),
        "exact": h.no_float(
            (p0_vector, extensions, transition, influence, representative)
        ),
    }


def affine_hull_controls() -> dict:
    p0 = matrix_vector((h.R(1, 4),) * 4)
    feasible_transition = p0 * sp.ones(1, 4)
    feasible_influence = feasible_transition - p0 * sp.ones(1, 4)
    feasible = h.normalizable_kernel(feasible_influence)

    other = matrix_vector((h.R(1, 2), h.R(1, 4), h.R(1, 8), h.R(1, 8)))
    infeasible_transition = other * sp.ones(1, 4)
    infeasible_influence = infeasible_transition - p0 * sp.ones(1, 4)
    infeasible = h.normalizable_kernel(infeasible_influence)
    return {
        "feasible_rank": feasible_transition.rank(),
        "feasible_E_rank": feasible_influence.rank(),
        "feasible": feasible,
        "all_probability_vectors_solve": all(
            feasible_transition * sp.eye(4)[:, column] == p0
            for column in range(4)
        ),
        "infeasible_column_sums": tuple(
            sp.expand(sum(infeasible_transition[:, column]))
            for column in range(4)
        ),
        "infeasible": infeasible,
        "infeasible_rank": infeasible_influence.rank(),
        "exact": h.no_float(
            (p0, feasible_transition, infeasible_transition, infeasible_influence)
        ),
    }


def weight_vector_and_iteration(system: dict) -> dict:
    fixture = system["fixture"]
    slot = system["slot"]
    transition = system["transition"]
    p0 = system["p0"]
    representative = system["representative"]
    weights = tuple(
        fixture.weight({(slot, letter): sp.Integer(0)})
        for letter in range(fixture.lx)
    )
    total = sp.expand(sum(weights))
    initial = matrix_vector(sp.cancel(weight / total) for weight in weights)
    current = initial
    iterates = []
    for _ in range(5):
        current = sp.expand(transition * current)
        iterates.append(current)
    influence = system["influence"]
    defect = sp.expand(transition * initial - p0)
    factored = sp.expand(influence * (initial - representative))
    return {
        "initial": initial,
        "iterates": tuple(iterates),
        "all_normalized": all(
            sp.expand(sum(vector) - 1) == 0 for vector in iterates
        ),
        "all_positive": all(
            all(value.is_positive for value in vector) for vector in iterates
        ),
        "solution_maps_to_p0": transition * representative == p0,
        "solution_not_fixed": transition * representative != representative,
        "defect_identity": h.zero(sp.expand(defect - factored)),
        "exact": h.no_float((weights, initial, iterates, defect, factored)),
    }


def main() -> int:
    checks = h.Checks()
    identity_ok, actual = h.verify_input_hashes(INPUT_SHA256)
    claims = build_claims()
    dropped = build_claims("drop_key")
    key_gate = (
        tuple(claims) == REQUIRED_CLAIM_KEYS
        and all(claims.values())
        and tuple(dropped) != REQUIRED_CLAIM_KEYS
    )
    checks.add(
        "A-source-input-and-key-closure",
        identity_ok and tuple(INPUT_SHA256) == AUDIT_INPUT_PATHS and key_gate,
        f"{len(INPUT_SHA256)} literal inputs; exact required-key set; actual={actual}",
    )

    supplied = tuple(
        supplied_system(f"b173_{tag}", cover_t, lx)
        for tag, cover_t, lx in h.PRIMARY
    )
    checks.add(
        "B-supplied-normalized-solutions",
        all(
            result["column_sums"] == (1, 1, 1, 1)
            and result["kernel"].exists
            and result["kernel"].unique
            and result["kernel"].rank == 3
            and result["kernel"].nullity == 1
            and result["equation"]
            and all(value.is_positive for value in result["representative"])
            for result in supplied
        ),
        f"two supplied matrices: {[(r['kernel'].rank, r['kernel'].nullity, tuple(r['representative'])) for r in supplied]}",
    )

    controls = affine_hull_controls()
    checks.add(
        "C-affine-solvability-controls",
        controls["feasible_rank"] == 1
        and controls["feasible_E_rank"] == 0
        and controls["feasible"].exists
        and not controls["feasible"].unique
        and controls["all_probability_vectors_solve"]
        and controls["infeasible_column_sums"] == (1, 1, 1, 1)
        and not controls["infeasible"].exists
        and controls["infeasible_rank"] == 1,
        "a singular rank-one M=P0 1^T is feasible and nonunique; four equal probability columns outside P0's affine point have no normalized solution",
    )

    zero_shear = supplied_system("b173_sigma0", 12, 4, sigma=sp.Integer(0))
    checks.add(
        "D-zero-shear-feasible-nonunique",
        zero_shear["kernel"].exists
        and not zero_shear["kernel"].unique
        and zero_shear["kernel"].rank == 0
        and zero_shear["kernel"].nullity == 4
        and h.zero(zero_shear["influence"])
        and all(
            matrix_vector(extension) == zero_shear["p0"]
            for extension in zero_shear["extensions"]
        ),
        "at sigma=0 every extension profile equals P0, so E=0 and every probability vector solves",
    )

    baseline = supplied[0]
    temporal = supplied_system("b173_st_quarter", 12, 4, st=h.R(1, 4))
    low_mass = supplied_system("b173_mass_third", 12, 4, mass=h.R(1, 3))
    checks.add(
        "E-exact-opposite-sign-endpoints",
        all(value.is_positive for value in baseline["representative"])
        and temporal["kernel"].exists
        and temporal["kernel"].unique
        and any(value.is_negative for value in temporal["representative"])
        and low_mass["kernel"].exists
        and low_mass["kernel"].unique
        and any(value.is_negative for value in low_mass["representative"]),
        "12x4: s_t=0 is positive while s_t=1/4 has a negative entry; m=1 is positive while m=1/3 has a negative entry",
    )

    iteration = weight_vector_and_iteration(baseline)
    checks.add(
        "F-five-finite-pushforwards",
        len(iteration["iterates"]) == 5
        and iteration["all_normalized"]
        and iteration["all_positive"],
        f"five exact normalized positive vectors={tuple(tuple(v) for v in iteration['iterates'])}",
    )
    checks.add(
        "G-solution-is-not-fixed-point",
        iteration["solution_maps_to_p0"]
        and iteration["solution_not_fixed"]
        and baseline["p0"] != baseline["representative"],
        "the normalized solution obeys M mu*=P0 != mu* at the supplied 12x4 matrix",
    )
    checks.add(
        "H-vector-defect-identity",
        iteration["defect_identity"],
        "M mu-P0 = E(mu-mu*) exactly for the displayed normalized one-record weight vector",
    )
    checks.add(
        "I-exact-bounded-scope",
        all(result["exact"] for result in supplied)
        and zero_shear["exact"]
        and temporal["exact"]
        and low_mass["exact"]
        and controls["exact"]
        and iteration["exact"],
        "two supplied systems, two sign-changing endpoint pairs, one zero-shear control, and five iterates only; no nearest-zero, topology, convergence, or universal law",
    )
    return checks.emit()


if __name__ == "__main__":
    sys.exit(main())
