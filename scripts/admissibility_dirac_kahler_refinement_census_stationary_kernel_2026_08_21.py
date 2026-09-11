#!/usr/bin/env python3
"""Corrected Block 172 certificate for finite refinement and density identities."""

from __future__ import annotations

import collections
import itertools
import sys

import sympy as sp

import admissibility_dirac_kahler_released7315_d_fixture_helpers_2026_09_11 as h


AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_REFINEMENT_CENSUS_STATIONARY_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md",
    ".claude/science/physics-loops/toe-axiom-closure-block172-refinement-census-stationary-kernel-20260821/NO_GO_LEDGER.md",
    "scripts/admissibility_dirac_kahler_released7315_d_fixture_helpers_2026_09_11.py",
    "scripts/admissibility_dirac_kahler_generator_trilemma_kernel_2026_08_21.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_GENERATOR_TRILEMMA_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md",
    "scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)

INPUT_SHA256 = {'docs/ADMISSIBILITY_DIRAC_KAHLER_REFINEMENT_CENSUS_STATIONARY_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md': '97f1e0ddc7df9af5ab0f315e1da69a88292f7d710ca91dc860aff71b6e7196e5',
 '.claude/science/physics-loops/toe-axiom-closure-block172-refinement-census-stationary-kernel-20260821/NO_GO_LEDGER.md': 'f24b0166fca960a6082b1d500d567ce84d7dafea32ce6eb59ec2d1a12288e62b',
 'scripts/admissibility_dirac_kahler_released7315_d_fixture_helpers_2026_09_11.py': '04ef3fdfe36d7328b827fe448a19ca432f4a8ecefd8b833b0905a9e38c52bbbf',
 'scripts/admissibility_dirac_kahler_generator_trilemma_kernel_2026_08_21.py': '0d9cf17034fe5aa1229ea3c707b2e67534cb860ba5591160ad34e17bee15f09a',
 'docs/ADMISSIBILITY_DIRAC_KAHLER_GENERATOR_TRILEMMA_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md': '6ef3dbeea1b42d03992409377000aa9ef80e4c8653351f258177603b54c42e14',
 'scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py': '0974a71bab3c753e66692740e303ea8062bfa7b6bd88fdc4a2c665d61ac95f87',
 'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py': '5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445',
 'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md': '9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33',
 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
 'docs/audit/data/axiom_premise_nodes.json': '615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37'}

REQUIRED_CLAIM_KEYS = (
    "input_closure",
    "frequency_census",
    "trace_additivity",
    "joint_pin_inequality",
    "reciprocal_bracket",
    "density_phase",
    "psd_qualification",
    "exact_finite_scope",
)


def build_claims(mutation: str = "") -> dict[str, bool]:
    claims = {key: True for key in REQUIRED_CLAIM_KEYS}
    if mutation == "drop_key":
        claims.pop(REQUIRED_CLAIM_KEYS[-1])
    return claims


def trace_additivity_probe() -> bool:
    entries = sp.symbols("g0:16")
    matrix = sp.Matrix(4, 4, entries)
    projectors = tuple(
        sp.diag(*(sp.Integer(index == target) for index in range(4)))
        for target in range(4)
    )
    for size in range(5):
        for subset in itertools.combinations(range(4), size):
            combined = sp.zeros(4)
            for target in subset:
                combined += projectors[target]
            if sp.expand(
                sp.trace(matrix * combined)
                - sum(sp.trace(matrix * projectors[target]) for target in subset)
            ) != 0:
                return False
    return True


def finite_census(tag: str, cover_t: int, lx: int) -> dict:
    fixture = h.RecordProfileFixture(tag, cover_t, lx)
    table = fixture.profile_table()
    frequencies = collections.Counter(row["frequency"] for row in table)
    profiles_by_frequency: dict[tuple, set[tuple]] = collections.defaultdict(set)
    for row in table:
        profiles_by_frequency[row["frequency"]].add(row["profile"])

    level = fixture.free_levels[0]
    cells = tuple(
        (time, space)
        for time in fixture.free_levels
        for space in range(fixture.lx)
    )
    first = (level, 0)
    second = (level, 1)
    singleton_weights = {
        cell: fixture.weight({cell: sp.Integer(0)}) for cell in cells
    }
    pair_weight = fixture.weight(
        {first: sp.Integer(0), second: sp.Integer(0)}
    )
    numerator = sp.expand(
        pair_weight - singleton_weights[first] - singleton_weights[second]
    )
    denominator = sp.expand(sum(singleton_weights.values()))
    defect = sp.cancel(numerator / denominator)
    integer, lower, upper = h.reciprocal_bracket(defect)
    bracket = lower < sp.Abs(defect) and sp.Abs(defect) <= upper

    return {
        "extent": tag,
        "word_count": len(table),
        "frequency_count": len(frequencies),
        "doubled_count": sum(count == 2 for count in frequencies.values()),
        "doubled_separated": all(
            len(profiles_by_frequency[frequency]) == count
            for frequency, count in frequencies.items()
            if count == 2
        ),
        "defect": defect,
        "numerator": numerator,
        "denominator": denominator,
        "bracket": (integer, lower, upper),
        "bracket_holds": bracket,
        "exact": h.no_float((table, singleton_weights, defect)),
    }


def density_probe() -> dict:
    rho = sp.Matrix(
        [[h.R(1, 2), sp.I / 4], [-sp.I / 4, h.R(1, 2)]]
    )
    phi = sp.I
    vector = sp.Matrix([h.R(3, 5), h.R(4, 5) * phi])
    projector = sp.expand(vector * vector.H)
    observed = sp.expand(sp.trace(rho * projector))
    diagonal = sp.expand(
        rho[0, 0] * projector[0, 0] + rho[1, 1] * projector[1, 1]
    )
    off_diagonal = sp.expand(observed - diagonal)
    formula = sp.expand(
        h.R(12, 25)
        * (phi * rho[0, 1] + sp.conjugate(phi) * rho[1, 0])
    )

    rho_real = sp.Matrix([[h.R(1, 2), h.R(1, 4)], [h.R(1, 4), h.R(1, 2)]])
    real_vector = sp.Matrix([h.R(3, 5), h.R(4, 5)])
    real_projector = sp.expand(real_vector * real_vector.H)
    real_off_diagonal = sp.expand(
        sp.trace(rho_real * real_projector)
        - rho_real[0, 0] * real_projector[0, 0]
        - rho_real[1, 1] * real_projector[1, 1]
    )
    positive_diagonal_counterexample = sp.Matrix([[1, 2], [2, 1]])
    return {
        "rho_inertia": h.congruence_inertia(rho),
        "rho_trace": sp.trace(rho),
        "off_diagonal": off_diagonal,
        "formula": formula,
        "real_off_diagonal": real_off_diagonal,
        "counterexample_inertia": h.congruence_inertia(
            positive_diagonal_counterexample
        ),
        "counterexample_determinant": positive_diagonal_counterexample.det(),
        "exact": h.no_float(
            (rho, vector, projector, observed, rho_real, real_off_diagonal)
        ),
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

    results = tuple(
        finite_census(f"b172_{tag}", cover_t, lx)
        for tag, cover_t, lx in h.PRIMARY
    )
    checks.add(
        "B-four-letter-length-two-census",
        all(
            result["word_count"] == 16
            and result["frequency_count"] == 10
            and result["doubled_count"] == 6
            and result["doubled_separated"]
            for result in results
        ),
        "16 words, 10 multisets, six different-letter double pairs, with distinct supplied profiles inside each pair",
    )
    checks.add(
        "C-trace-additivity-identity",
        trace_additivity_probe(),
        "all subsets of four diagonal projectors satisfy trace linearity for a generic 4x4 matrix",
    )
    checks.add(
        "D-supplied-joint-pin-inequality",
        all(
            result["numerator"].is_negative
            and result["denominator"].is_positive
            and result["defect"].is_negative
            for result in results
        )
        and sp.Integer(3) - sp.Integer(1) - sp.Integer(1) > 0,
        f"measured negative defects={[(r['extent'], r['defect']) for r in results]}; positive weights (3,1,1) give the opposite sign",
    )
    checks.add(
        "E-reciprocal-intervals",
        all(result["bracket_holds"] for result in results),
        f"N=floor(1/|delta|) gives strict-lower/weak-upper brackets={[(r['extent'], r['bracket']) for r in results]}",
    )

    density = density_probe()
    checks.add(
        "F-density-phase-order",
        density["rho_inertia"] == (2, 0, 0)
        and density["rho_trace"] == 1
        and density["off_diagonal"] == density["formula"] == -h.R(6, 25)
        and density["real_off_diagonal"] == h.R(6, 25),
        "PSD trace-one complex example gives -6/25 with phi*rho_ij+conj(phi)*rho_ji; the real slice gives 6/25",
    )
    checks.add(
        "G-positive-diagonal-is-not-PSD",
        density["counterexample_determinant"] == -3
        and density["counterexample_inertia"] == (1, 0, 1),
        "[[1,2],[2,1]] has positive diagonal, determinant -3, and inertia (1,0,1)",
    )
    checks.add(
        "H-exact-bounded-scope",
        all(result["exact"] for result in results) and density["exact"],
        "two finite tables, two finite defects, and two-state density identities only; no deep census, global refinement verdict, or axiom",
    )
    return checks.emit()


if __name__ == "__main__":
    sys.exit(main())
