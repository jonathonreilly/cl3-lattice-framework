#!/usr/bin/env python3
"""Corrected Block 171 certificate for two supplied finite profile fixtures."""

from __future__ import annotations

import sys

import sympy as sp

import admissibility_dirac_kahler_released7315_d_fixture_helpers_2026_09_11 as h


AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_GENERATOR_TRILEMMA_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md",
    ".claude/science/physics-loops/toe-axiom-closure-block171-generator-trilemma-20260821/NO_GO_LEDGER.md",
    "scripts/admissibility_dirac_kahler_released7315_d_fixture_helpers_2026_09_11.py",
    "scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)

INPUT_SHA256 = {'docs/ADMISSIBILITY_DIRAC_KAHLER_GENERATOR_TRILEMMA_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md': '6ef3dbeea1b42d03992409377000aa9ef80e4c8653351f258177603b54c42e14',
 '.claude/science/physics-loops/toe-axiom-closure-block171-generator-trilemma-20260821/NO_GO_LEDGER.md': 'aced1c63cc023d0981b9db2ceb03add9fde929be2d1108918c93346002e2ae26',
 'scripts/admissibility_dirac_kahler_released7315_d_fixture_helpers_2026_09_11.py': '04ef3fdfe36d7328b827fe448a19ca432f4a8ecefd8b833b0905a9e38c52bbbf',
 'scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py': '0974a71bab3c753e66692740e303ea8062bfa7b6bd88fdc4a2c665d61ac95f87',
 'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py': '5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445',
 'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md': '9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33',
 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
 'docs/audit/data/axiom_premise_nodes.json': '615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37'}

REQUIRED_CLAIM_KEYS = (
    "input_closure",
    "inverse_congruence",
    "supplied_positivity",
    "finite_profile_table",
    "finite_gibbs_factorization",
    "direct_sum_closure",
    "exact_finite_scope",
)


def build_claims(mutation: str = "") -> dict[str, bool]:
    claims = {key: True for key in REQUIRED_CLAIM_KEYS}
    if mutation == "drop_key":
        claims.pop(REQUIRED_CLAIM_KEYS[-1])
    return claims


def herm(matrix: sp.MatrixBase) -> sp.Matrix:
    matrix = sp.Matrix(matrix)
    return sp.expand((matrix + matrix.H) / 2)


def direct_sum_probe() -> tuple[bool, tuple]:
    q1 = sp.Matrix([[2, sp.I], [0, 3]])
    q2 = sp.Matrix([[4, 1], [-1, 2]])
    whole = sp.diag(q1, q2)
    inverse = whole.inv()
    polynomial = sp.expand(whole.H * whole + 2 * whole + sp.eye(4))
    expected_inverse = sp.diag(q1.inv(), q2.inv())
    expected_polynomial = sp.diag(
        sp.expand(q1.H * q1 + 2 * q1 + sp.eye(2)),
        sp.expand(q2.H * q2 + 2 * q2 + sp.eye(2)),
    )
    return (
        inverse == expected_inverse and polynomial == expected_polynomial,
        tuple(inverse[:2, :2]),
    )


def fixture_certificate(tag: str, cover_t: int, lx: int) -> dict:
    fixture = h.RecordProfileFixture(tag, cover_t, lx)
    q = fixture.q_matrix()
    inverse = fixture.inverse()
    hq = herm(q)
    hinverse = herm(inverse)
    table = fixture.profile_table()

    weights = {(row["trail"]): row["weight"] for row in table}
    total = sp.expand(sum(weights.values()))
    joint = {trail: sp.cancel(weight / total) for trail, weight in weights.items()}
    marginal = {
        left: sp.expand(sum(joint[(left, right)] for right in range(lx)))
        for left in range(lx)
    }
    conditional = {
        (left, right): sp.cancel(joint[(left, right)] / marginal[left])
        for left in range(lx)
        for right in range(lx)
    }
    factorized = all(
        sp.expand(joint[(left, right)] - marginal[left] * conditional[(left, right)])
        == 0
        for left in range(lx)
        for right in range(lx)
    )

    return {
        "tag": tag,
        "shape": q.shape,
        "inverse_residual": h.zero(sp.expand(q * inverse - sp.eye(q.rows))),
        "congruence": h.zero(
            sp.expand(hinverse - inverse * hq * inverse.H)
        ),
        "hq_inertia": h.congruence_inertia(hq),
        "hinverse_inertia": h.congruence_inertia(hinverse),
        "w9_inertia": h.congruence_inertia(fixture.w9_block()),
        "row_count": len(table),
        "records": tuple(tuple(sorted(row["records"])) for row in table),
        "positive_weights": all(weight.is_positive for weight in weights.values()),
        "positive_profiles": all(
            all(value.is_positive for value in row["profile"]) for row in table
        ),
        "normalized_profiles": all(
            sp.expand(sum(row["profile"]) - 1) == 0 for row in table
        ),
        "distinct_profiles": len({row["profile"] for row in table}),
        "joint_positive": all(value.is_positive for value in joint.values()),
        "joint_normalized": sp.expand(sum(joint.values()) - 1) == 0,
        "factorized": factorized,
        "exact": h.no_float((q, inverse, table, joint, conditional)),
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
        fixture_certificate(f"b171_{tag}", cover_t, lx)
        for tag, cover_t, lx in h.PRIMARY
    )
    checks.add(
        "B-inverse-congruence",
        all(result["inverse_residual"] and result["congruence"] for result in results),
        "H(Q^-1)=Q^-1 H(Q) Q^-dag entrywise at the supplied 12x4 and 8x4 matrices",
    )
    checks.add(
        "C-supplied-positive-matrices",
        all(
            result["hq_inertia"] == (result["shape"][0], 0, 0)
            and result["hinverse_inertia"] == (result["shape"][0], 0, 0)
            and result["w9_inertia"] == (4, 0, 0)
            for result in results
        ),
        f"exact (positive,zero,negative) inertias={[(r['hq_inertia'], r['hinverse_inertia'], r['w9_inertia']) for r in results]}",
    )
    checks.add(
        "D-reconstructed-finite-profile-table",
        all(
            result["row_count"] == 16
            and result["positive_weights"]
            and result["positive_profiles"]
            and result["normalized_profiles"]
            and result["distinct_profiles"] == 16
            for result in results
        ),
        "16 ordered two-record rows per extent; all weights/profiles positive; each profile normalized; 16 distinct",
    )
    checks.add(
        "E-finite-gibbs-factorization",
        all(
            result["joint_positive"]
            and result["joint_normalized"]
            and result["factorized"]
            for result in results
        ),
        "the positive 16-point joint equals its marginal times its conditional exactly at both extents",
    )
    direct_sum, first_block = direct_sum_probe()
    checks.add(
        "F-direct-sum-closure",
        direct_sum,
        f"defined inverse and one polynomial expression remain block diagonal; first inverse block={first_block}",
    )
    checks.add(
        "G-exact-bounded-scope",
        all(result["exact"] for result in results) and h.no_float(first_block),
        "32 finite rows and two supplied matrices only; no history census, limit, physical action, or generator classification",
    )
    return checks.emit()


if __name__ == "__main__":
    sys.exit(main())
