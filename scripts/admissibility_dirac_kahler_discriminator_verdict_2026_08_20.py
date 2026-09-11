#!/usr/bin/env python3
"""Corrected Block 155 finite discriminator certificate."""

from __future__ import annotations

import collections
import sys

import sympy as sp

import admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10 as h


AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DISCRIMINATOR_VERDICT_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    ".claude/science/physics-loops/toe-axiom-closure-block155-discriminator-verdict-20260820/NO_GO_LEDGER.md",
    "scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_unique_completion_price_2026_08_20.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_UNIQUE_COMPLETION_PRICE_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/admissibility_dirac_kahler_bare_character_2026_08_20.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_BARE_CHARACTER_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)

INPUT_SHA256 = {
    'docs/ADMISSIBILITY_DIRAC_KAHLER_DISCRIMINATOR_VERDICT_BOUNDED_THEOREM_NOTE_2026-08-20.md': '227c121b6ba02f5414af664b2d14a6602338694df18f46c38f7bfa012650df3d',
    '.claude/science/physics-loops/toe-axiom-closure-block155-discriminator-verdict-20260820/NO_GO_LEDGER.md': '803a16230229a8bb958635521618e982c395efbf0f7b8d098a2d1e6bfed9a13f',
    'scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py': '37e2520596484df264bc169a6c7ced21575c2e7784bc78d668338ec30dcc4383',
    'scripts/admissibility_dirac_kahler_unique_completion_price_2026_08_20.py': '806e4dc362c468703303f943beb6ccde039c8a6f262c50a80c3153ef828c80ff',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_UNIQUE_COMPLETION_PRICE_BOUNDED_THEOREM_NOTE_2026-08-20.md': 'b2e5d57e255dae4f010988c0dc823607260179006860cc5b45619898535f19d4',
    'scripts/admissibility_dirac_kahler_bare_character_2026_08_20.py': 'af15e1cdd0bded4bfc37edfd49ebbb572b2ced3233e137ddec2532dc0ac32c51',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_BARE_CHARACTER_BOUNDED_THEOREM_NOTE_2026-08-20.md': '830435f2f820728c213a24665958ee82abb1c1622b7b5a56018de10251a55dcd',
    'scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py': '0974a71bab3c753e66692740e303ea8062bfa7b6bd88fdc4a2c665d61ac95f87',
    'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py': '5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md': '9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33',
    'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
    'docs/audit/data/axiom_premise_nodes.json': '615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37',
}


def main() -> int:
    checks = h.Checks()
    identity_ok, actual = h.verify_input_hashes(INPUT_SHA256)
    checks.add("A-source-input-closure", identity_ok, f"12 literal inputs; actual={actual}")

    differentials, star = h.connection()
    edges = h.edge_differentials(differentials, star)
    solved = h.completion_table()
    profiles = collections.Counter(
        (len(data["support"]), len(data["deleted"])) for data in solved.values()
    )
    untouched = {len(data["support"]) - len(data["deleted"]) for data in solved.values()}
    link_kinds = {
        h.link_kind(row, column)
        for data in solved.values() for row, column in data["deleted"]
    }
    checks.add(
        "B-selected-deletion-scope",
        profiles == {(32, 16): 6, (48, 24): 10}
        and untouched == {16, 24}
        and link_kinds == {"T+", "T-", "X+", "X-"},
        "active deletion and untouched support are reported separately",
    )

    ranks_by_edge = {
        key: (sp.Matrix(edges[key]).rank(), sp.Matrix(data["completed"]).rank())
        for key, data in solved.items()
    }
    rank_pair_counts = collections.Counter(ranks_by_edge.values())
    checks.add(
        "C-similarity-invariant-rank-drop",
        rank_pair_counts == {(16, 10): 14, (16, 8): 2}
        and {
            key for key, pair in ranks_by_edge.items() if pair == (16, 8)
        } == {(2, 2), (3, 3)},
        "generic symbolic ranks strictly drop: fourteen 16->10, edges (2,2) and (3,3) 16->8",
    )

    full_rows = {
        key: h.full_plus_row(h.THETA_PRIME, h.residue(data["completed"]))
        for key, data in solved.items()
    }
    bare_mixed = {
        key: sp.expand(h.PLUS.T * h.THETA_PRIME * h.residue(edges[key]) * h.MINUS)
        for key in h.EDGE_KEYS
    }
    checks.add(
        "D-selected-full-row-cancellation",
        all(h.zero(value) for value in full_rows.values())
        and all(not h.zero(value) for value in bare_mixed.values()),
        "completed full 8x16 row zero; bare mixed-half controls nonzero",
    )

    probe = (0, 0)
    completed_residue = h.residue(solved[probe]["completed"])
    action = sp.expand(h.MASS * h.HQ_FREE + completed_residue)
    qt = sp.expand(h.PLUS.T * h.THETA_PRIME)
    tau2 = h.DESCENT[(1, 2, 1, 0)]
    p0 = sp.expand(qt * action * h.PLUS)
    p2 = sp.expand(qt * action * tau2 * h.PLUS)
    point = h.modulus_point(h.transfer_witness_field())
    p0w = sp.expand(p0.xreplace(point).subs(h.MASS, 1))
    p2w = sp.expand(p2.xreplace(point).subs(h.MASS, 1))
    kernel = p0w.nullspace()
    transfer = sp.expand(p0w.pinv() * p2w)
    descends = all(
        h.zero(sp.expand(p0w * transfer * vector)) for vector in kernel
    )
    kills_kernel = all(h.zero(sp.expand(p2w * vector)) for vector in kernel)
    range_residual = sp.expand((sp.eye(h.HALF) - p0w * p0w.pinv()) * p2w)
    checks.add(
        "E-correct-transfer-predicates",
        len(kernel) == 4
        and not kills_kernel
        and descends
        and all(h.zero(sp.expand(transfer * vector)) for vector in kernel)
        and not h.zero(range_residual)
        and sp.expand(p0w * transfer - p2w) == -range_residual,
        "P2 does not kill ker(P0), while T does and descends; the unreduced left-equation range residual is nonzero",
    )

    cover_residue = sp.expand(
        sp.I
        * (
            h.COVER_FREE * solved[probe]["completed"]
            + solved[probe]["completed"].H * h.COVER_FREE
        )
    )
    checks.add(
        "F-compression-is-not-automatic-descent",
        not h.zero(h.descent_residual(cover_residue)),
        "formal SELECT M LIFT fails the separate intertwining test on the probe",
    )

    checks.add(
        "G-system-language",
        h.no_float((ranks_by_edge, rank_pair_counts, p0w, p2w, transfer, range_residual)),
        "matrix ranks are basis-invariant; no branch Boolean or physical quotient is inferred",
    )
    return checks.emit()


if __name__ == "__main__":
    sys.exit(main())
