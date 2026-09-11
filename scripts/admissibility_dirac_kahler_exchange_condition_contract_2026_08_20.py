#!/usr/bin/env python3
"""Corrected Block 160 finite exchange-pairing certificate."""

from __future__ import annotations

import sys

import sympy as sp

import admissibility_dirac_kahler_released7315_b_fixture_helpers_2026_09_10 as b


AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_EXCHANGE_CONDITION_CONTRACT_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    ".claude/science/physics-loops/toe-axiom-closure-block160-exchange-condition-contract-20260820/NO_GO_LEDGER.md",
    "scripts/admissibility_dirac_kahler_released7315_b_fixture_helpers_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_link_curvature_scout_2026_08_20.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_LINK_CURVATURE_SCOUT_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)

# Generated from final bytes at source freeze; kept literal for runner-cache.
INPUT_SHA256 = {
    'docs/ADMISSIBILITY_DIRAC_KAHLER_EXCHANGE_CONDITION_CONTRACT_BOUNDED_THEOREM_NOTE_2026-08-20.md': '8cdd86b415f985904f66a1f561a94a41fd0a2babd02c4300724793ff3823e2fa',
    '.claude/science/physics-loops/toe-axiom-closure-block160-exchange-condition-contract-20260820/NO_GO_LEDGER.md': '359bbbf264f02e8132121329c98efd88b88cc4b4e0239c30741d9ee11e45ee91',
    'scripts/admissibility_dirac_kahler_released7315_b_fixture_helpers_2026_09_10.py': '97846307bffff108c98466329c65a051e8d896ccb9231fd23d9e0ddec962c2c9',
    'scripts/admissibility_dirac_kahler_link_curvature_scout_2026_08_20.py': '2ea65a2613d2822427bfb2a0e3ac4f4ea57a18c732c27f7312bbca585f61776f',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_LINK_CURVATURE_SCOUT_BOUNDED_THEOREM_NOTE_2026-08-20.md': '2601b9fc27fc78df48d22ade9104251fd1da85f174f6c7126cad9e6319ff8068',
    'scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py': '37e2520596484df264bc169a6c7ced21575c2e7784bc78d668338ec30dcc4383',
    'scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py': '0974a71bab3c753e66692740e303ea8062bfa7b6bd88fdc4a2c665d61ac95f87',
    'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py': '5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md': '9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33',
    'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
    'docs/audit/data/axiom_premise_nodes.json': '615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37',
}


def main() -> int:
    checks = b.Checks()
    identity_ok, actual = b.verify_input_hashes(INPUT_SHA256)
    identity_ok = identity_ok and tuple(INPUT_SHA256) == AUDIT_INPUT_PATHS
    checks.add("A-source-input-closure", identity_ok, f"{len(INPUT_SHA256)} literal inputs; actual={actual}")

    symbolic_edges = b.dense_edges()
    edges = {key: sp.expand(value.xreplace(b.ATLAS)) for key, value in symbolic_edges.items()}
    flat = b.h.flat_field()
    primary = b.restrict_dense(edges[(2, 2)], b.EVEN_SUPPORT)

    deletion = {
        key: b.inertia_pzn(b.dense_action_pairing(
            b.restrict_dense(edge, b.EVEN_SUPPORT), flat, sp.Integer(0)
        ))
        for key, edge in edges.items()
    }
    checks.add(
        "B-committed-link-deletion-census",
        sum(value == (4, 4, 0) for value in deletion.values()) == 6
        and sum(value == (0, 4, 4) for value in deletion.values()) == 6
        and sum(value == (0, 8, 0) for value in deletion.values()) == 4,
        "on the displayed half and flat carrier: six PSD, six NSD, four zero (p,z,n order)",
    )

    volumes = {cell: sp.Symbol(f"nu_{cell[0]}{cell[1]}", positive=True) for cell in b.CELLS}
    generic_flat = b.field_of(volumes=volumes)
    flat_hq = b.h.quotient(b.h.cover_hodge_from_field(generic_flat))
    flat_mass = b.dense_pairing(b.THETA, b.MASS * flat_hq)
    checks.add(
        "C-flat-mass-diagonality",
        flat_hq.is_diagonal() and b.zero(flat_mass),
        "the exchanging half pairing of the mass Gram vanishes on the free-volume flat family",
    )

    flat_forms = tuple(
        b.dense_action_pairing(primary, flat, mass)
        for mass in (sp.Integer(0), b.R(1, 10), sp.Integer(1), sp.Integer(5))
    )
    target_flat = sp.diag(b.R(4, 5), 0, b.R(4, 5), 0, b.R(4, 5), 0, b.R(4, 5), 0)
    selected_curved = (
        b.odd_time_field(b.R(1, 3), sp.Integer(1)),
        b.odd_time_field(b.R(3, 4), sp.Integer(3)),
    )
    selected_massive = tuple(
        b.inertia_pzn(b.dense_action_pairing(primary, field, mass))
        for field in selected_curved
        for mass in (b.R(1, 10), sp.Integer(1), sp.Integer(5))
    )
    checks.add(
        "D-displayed-flat-and-curved-samples",
        all(form == target_flat for form in flat_forms)
        and set(selected_massive) == {(4, 0, 4)},
        "flat witness is PSD at four masses; two named curved families are indefinite at three nonzero masses",
    )

    balanced = b.balanced_field()
    balanced_forms = tuple(
        b.dense_action_pairing(primary, balanced, mass)
        for mass in (sp.Integer(0), b.R(1, 10), sp.Integer(1), sp.Integer(5))
    )
    target_balanced = sp.diag(b.R(33, 40), 0, b.R(33, 40), 0,
                              b.R(33, 40), 0, b.R(33, 40), 0)
    checks.add(
        "E-curved-mass-survival-counterexample",
        b.h.in_admissible_cone(balanced)
        and not b.h.cover_hodge_from_field(balanced).is_diagonal()
        and all(form == target_balanced for form in balanced_forms),
        "the Block-161 balanced curved carrier is PSD and unchanged at the four displayed masses",
    )

    real_weights = sp.symbols("lambda0:4", real=True)
    real_edges = b.dense_edges(weights=real_weights)
    prime_zero = sum(
        b.zero(b.dense_action_pairing(edge, flat, 0, b.THETA_PRIME))
        for edge in real_edges.values()
    )
    theta_zero = sum(
        b.zero(b.dense_action_pairing(edge, flat, 0, b.THETA))
        for edge in real_edges.values()
    )
    checks.add(
        "F-real-weight-sufficient-scope",
        (prime_zero, theta_zero) == (16, 2),
        "identity Hodge plus real healing weights annihilates all 16 theta-prime forms; no necessity claim",
    )

    checks.add(
        "G-exact-bounded-scope",
        b.no_float((tuple(edges.values()), flat_forms, selected_massive, balanced_forms))
        and b.h.in_admissible_cone(flat)
        and all(b.h.in_admissible_cone(field) for field in selected_curved),
        "exact finite supplied matrices only; no all-carrier or physical-action classification",
    )
    return checks.emit()


if __name__ == "__main__":
    sys.exit(main())
