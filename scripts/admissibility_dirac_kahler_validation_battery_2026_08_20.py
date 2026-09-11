#!/usr/bin/env python3
"""Corrected Block 161 finite quotient and carrier certificate."""

from __future__ import annotations

import sys

import sympy as sp

import admissibility_dirac_kahler_released7315_b_fixture_helpers_2026_09_10 as b


AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_VALIDATION_BATTERY_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    ".claude/science/physics-loops/toe-axiom-closure-block161-validation-battery-20260820/NO_GO_LEDGER.md",
    "scripts/admissibility_dirac_kahler_released7315_b_fixture_helpers_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_exchange_condition_contract_2026_08_20.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_EXCHANGE_CONDITION_CONTRACT_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/admissibility_dirac_kahler_link_curvature_scout_2026_08_20.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_LINK_CURVATURE_SCOUT_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)

INPUT_SHA256 = {
    'docs/ADMISSIBILITY_DIRAC_KAHLER_VALIDATION_BATTERY_BOUNDED_THEOREM_NOTE_2026-08-20.md': 'd3efa6d5231babb9b3da9146285a6563004865775e71ae9a20a79c3d0167262a',
    '.claude/science/physics-loops/toe-axiom-closure-block161-validation-battery-20260820/NO_GO_LEDGER.md': 'a4a3166e77c883118f933afc0f14e3ba29643c3bdee5081796dc499bf87cf2fb',
    'scripts/admissibility_dirac_kahler_released7315_b_fixture_helpers_2026_09_10.py': '97846307bffff108c98466329c65a051e8d896ccb9231fd23d9e0ddec962c2c9',
    'scripts/admissibility_dirac_kahler_exchange_condition_contract_2026_08_20.py': 'e7d44e365f271ce84fb9615a9d0814d9667bb6648ad1fc084533cb46184e4387',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_EXCHANGE_CONDITION_CONTRACT_BOUNDED_THEOREM_NOTE_2026-08-20.md': '8cdd86b415f985904f66a1f561a94a41fd0a2babd02c4300724793ff3823e2fa',
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

    edges_symbolic = b.dense_edges()
    edges = {key: sp.expand(value.xreplace(b.ATLAS)) for key, value in edges_symbolic.items()}
    flat = b.h.flat_field()
    even = b.restrict_dense(edges[(2, 2)], b.EVEN_SUPPORT)
    odd = b.restrict_dense(edges[(2, 2)], b.ODD_SUPPORT)
    pairing = b.dense_action_pairing(even, flat, 0)
    target = sp.diag(b.R(4, 5), 0, b.R(4, 5), 0, b.R(4, 5), 0, b.R(4, 5), 0)
    projection = sp.zeros(4, b.HALF)
    for row, slot in enumerate(b.EVEN_SLOTS):
        projection[row, slot] = 1
    checks.add(
        "B-specified-quotient-pullback",
        pairing == target
        and pairing == projection.T * (b.R(4, 5) * sp.eye(4)) * projection
        and pairing.nullspace() == [sp.eye(b.HALF).col(slot) for slot in b.ODD_SLOTS],
        "rank-four pullback; its kernel is exactly the four specified odd-column directions",
    )

    balanced = b.balanced_field()
    balanced_hodge = b.h.cover_hodge_from_field(balanced)
    balanced_forms = tuple(
        b.dense_action_pairing(even, balanced, mass)
        for mass in (0, b.R(1, 10), 1, 5)
    )
    balanced_target = sp.diag(b.R(33, 40), 0, b.R(33, 40), 0,
                              b.R(33, 40), 0, b.R(33, 40), 0)
    checks.add(
        "C-curved-mass-survival-carrier",
        b.h.in_admissible_cone(balanced)
        and not balanced_hodge.is_diagonal()
        and all(form == balanced_target for form in balanced_forms),
        "the balanced curved carrier gives the same rank-four PSD form at four displayed masses",
    )

    sigma, nu = sp.symbols("sigma nu", real=True, nonzero=True)
    a = sp.cancel(nu / (1 - sigma ** 2))
    shear_moment = sp.cancel(-nu * sigma / (1 - sigma ** 2))
    symbolic_action = b.h.quotient_action(even, b.h.COVER_FREE, b.MASS)
    action_symbols = b.free_symbols_of(symbolic_action)
    checks.add(
        "D-shear-magnitude-remains-in-carrier-action",
        sp.diff(a, sigma) != 0
        and sp.simplify(a * (1 - sigma ** 2) - nu) == 0
        and sp.simplify(shear_moment * (1 - sigma ** 2) + nu * sigma) == 0
        and bool(action_symbols & (set(b.h.A_MODULUS.values()) | set(b.h.B_MODULUS.values()))),
        "formal compression removes named directions but the carrier/action retains a and b shear dependence",
    )

    real_weights = sp.symbols("lambda0:4", real=True)
    real_edges = b.dense_edges(weights=real_weights)
    real_prime_zero = tuple(
        b.zero(b.dense_action_pairing(edge, flat, 0, b.THETA_PRIME))
        for edge in real_edges.values()
    )
    complex_edges = b.dense_edges(weights=(sp.I, 0, b.R(1, 2), b.R(-1, 3)))
    complex_prime_live = sum(
        not b.zero(b.dense_action_pairing(edge, flat, 0, b.THETA_PRIME))
        for edge in complex_edges.values()
    )
    checks.add(
        "E-sufficient-annihilation-scope",
        all(real_prime_zero) and complex_prime_live > 0,
        "identity Hodge plus real weights is sufficient; complex controls prevent a global iff claim",
    )

    lam = sp.Symbol("lambda", real=True)
    interpolated = sp.zeros(b.SIZE)
    for x in range(b.LX):
        for row, column in b.crossing_support((x,)):
            interpolated[row, column] = sp.expand(
                (1 + lam * (-1) ** x) * edges[(2, 2)][row, column]
            )
    grid = tuple(b.R(k, 20) for k in range(-20, 21))
    grid_psd = []
    for mass in (0, 1):
        raw = b.dense_action_pairing(interpolated, flat, mass)
        grid_psd.append(tuple(
            value for value in grid
            if (lambda inertia: inertia[2] == 0 and inertia[0] > 0)(
                b.inertia_pzn(raw.xreplace({lam: value}))
            )
        ))
    checks.add(
        "F-rational-lambda-grid",
        tuple(grid_psd) == ((sp.Integer(1),), (sp.Integer(1),)),
        "on the 41-point rational grid, only lambda=1 is PSD at masses zero and one",
    )

    odd_pairing = b.dense_action_pairing(odd, flat, 0)
    checks.add(
        "G-nonunitary-equivalence-by-inertia",
        b.inertia_pzn(pairing) == (4, 4, 0)
        and b.inertia_pzn(odd_pairing) == (2, 4, 2),
        "different inertia proves the two displayed forms are not unitarily congruent",
    )

    checks.add(
        "H-exact-operational-scope",
        b.no_float((pairing, balanced_forms, symbolic_action, odd_pairing, grid_psd)),
        "specified matrix directions and a finite lambda grid only; no absence-of-physics claim",
    )
    return checks.emit()


if __name__ == "__main__":
    sys.exit(main())
