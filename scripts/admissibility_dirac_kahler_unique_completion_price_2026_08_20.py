#!/usr/bin/env python3
"""Corrected Block 154 certificate on the supplied finite matrices."""

from __future__ import annotations

import collections
import sys

import sympy as sp

import admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10 as h


AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_UNIQUE_COMPLETION_PRICE_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    ".claude/science/physics-loops/toe-axiom-closure-block154-unique-completion-price-20260820/NO_GO_LEDGER.md",
    "scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_bare_character_2026_08_20.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_BARE_CHARACTER_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)

INPUT_SHA256 = {
    'docs/ADMISSIBILITY_DIRAC_KAHLER_UNIQUE_COMPLETION_PRICE_BOUNDED_THEOREM_NOTE_2026-08-20.md': 'b2e5d57e255dae4f010988c0dc823607260179006860cc5b45619898535f19d4',
    '.claude/science/physics-loops/toe-axiom-closure-block154-unique-completion-price-20260820/NO_GO_LEDGER.md': 'bcac8d2c3e0828bcc6ae070e2a8b027208e8ca52305f1d4a55a784d241ec7e12',
    'scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py': '37e2520596484df264bc169a6c7ced21575c2e7784bc78d668338ec30dcc4383',
    'scripts/admissibility_dirac_kahler_bare_character_2026_08_20.py': 'af15e1cdd0bded4bfc37edfd49ebbb572b2ced3233e137ddec2532dc0ac32c51',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_BARE_CHARACTER_BOUNDED_THEOREM_NOTE_2026-08-20.md': '830435f2f820728c213a24665958ee82abb1c1622b7b5a56018de10251a55dcd',
    'scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py': '0974a71bab3c753e66692740e303ea8062bfa7b6bd88fdc4a2c665d61ac95f87',
    'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py': '5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md': '9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33',
    'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
    'docs/audit/data/axiom_premise_nodes.json': '615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37',
}


def reach_certificate() -> tuple:
    even = tuple(k for k in range(h.PHYS) if h.X0[k, k] == 1)
    odd = tuple(k for k in range(h.PHYS) if h.X0[k, k] == -1)
    pairs = tuple((i, j) for i in even for j in odd)
    symbols = sp.symbols(f"r0:{len(pairs)}", real=True)
    delta = sp.zeros(h.PHYS)
    for symbol, (i, j) in zip(symbols, pairs):
        delta[i, j], delta[j, i] = symbol, -symbol
    block = h.herm(h.half_block(h.THETA_PRIME, delta))
    coefficient_map = sp.Matrix(
        [[sp.expand(block[i, j]).coeff(symbol) for symbol in symbols]
         for i in h.DEAD for j in h.LIVE]
    )
    return (
        len(symbols),
        h.zero(h.X0 * delta * h.X0 + delta),
        h.live_count(block),
        coefficient_map.rank(),
    )


def nearest_neighbor_probe(edge) -> tuple:
    hops = tuple(
        sorted(
            {
                (h.fixture.cover_index(t + dt, x + dx), h.fixture.cover_index(t, x))
                for t in range(h.COVER_T)
                for x in range(h.LX)
                for dt, dx in ((1, 0), (-1, 0), (0, 1), (0, -1))
            }
        )
    )
    u = sp.symbols(f"u0:{len(hops)}", real=True)
    v = sp.symbols(f"v0:{len(hops)}", real=True)
    parameters = tuple(u) + tuple(v)
    index = {symbol: position for position, symbol in enumerate(parameters)}
    delta = sp.zeros(h.SIZE)
    for position, (row, column) in enumerate(hops):
        delta[row, column] = sp.I * (
            u[position] * h.SHEAR_X + v[position] * h.SHEAR_T
        )
    image = h.herm(h.half_block(h.THETA_PRIME, h.residue(delta)))
    target = h.herm(h.half_block(h.THETA_PRIME, h.residue(edge)))
    rows, right = [], []
    for row in h.DEAD:
        for column in h.LIVE:
            for coefficients, value in h.monomial_rows(
                image[row, column] + target[row, column], parameters, index
            ):
                rows.append(coefficients)
                right.append(value)
    matrix, vector = sp.Matrix(rows), sp.Matrix(right)
    full = h.feasible(matrix, vector)

    def residue_slice(site: int) -> int:
        return (site // h.LX) % h.PHYS_T

    crossings = tuple(
        hop for hop in hops
        if {residue_slice(hop[0]), residue_slice(hop[1])} in ({1, 2}, {3, 0})
    )
    crossing_columns = [
        index[symbol]
        for position, hop in enumerate(hops)
        if hop in set(crossings)
        for symbol in (u[position], v[position])
    ]
    crossing = h.feasible(matrix[:, crossing_columns], vector)
    necessity = []
    for time_slice in range(h.COVER_T):
        columns = [
            index[symbol]
            for position, (row, column) in enumerate(hops)
            if row // h.LX != time_slice and column // h.LX != time_slice
            for symbol in (u[position], v[position])
        ]
        if not h.feasible(matrix[:, columns], vector)[2]:
            necessity.append(time_slice)
    return len(hops), len(parameters), len(crossings), full, crossing, tuple(necessity)


def main() -> int:
    checks = h.Checks()
    identity_ok, actual = h.verify_input_hashes(INPUT_SHA256)
    checks.add("A-source-input-closure", identity_ok, f"10 literal inputs; actual={actual}")

    checks.add(
        "B-odd-reach-coefficient-map",
        reach_certificate() == (64, True, 32, 16),
        "64 coefficients; all 32 oriented dead-live slots; coefficient-map rank 16",
    )

    differentials, star = h.connection()
    edges = h.edge_differentials(differentials, star)
    solved = h.completion_table()
    profile = collections.Counter(
        (len(data["support"]), len(data["deleted"])) for data in solved.values()
    )
    forced_values = {
        data["solution"][position]
        for data in solved.values()
        for position in data["forced"]
    }
    half_zero = all(
        h.zero(h.half_block(h.THETA_PRIME, h.residue(data["completed"])))
        for data in solved.values()
    )
    checks.add(
        "C-support-restricted-deletion",
        profile == {(32, 16): 6, (48, 24): 10}
        and forced_values == {-1}
        and half_zero,
        "six 32/16 and ten 48/24 support/deletion profiles; selected representative kills the full half block",
    )

    symmetric_ranks = {
        sp.expand(h.residue(data["completed"]) + h.residue(data["completed"]).T).rank()
        for data in solved.values()
    }
    checks.add(
        "D-price",
        symmetric_ranks == {8}
        and all(h.live_count(data["completed"]) > 0 for data in solved.values())
        and all(
            not h.zero(h.residue(data["completed"])) for data in solved.values()
        ),
        "completed residue loses antisymmetry and survives outside the zero half block",
    )

    probe = nearest_neighbor_probe(edges[(0, 0)])
    checks.add(
        "E-crossing-and-slice-probe",
        probe == (128, 256, 32, (104, 104, True), (32, 33, False), (0, 4, 5, 6, 7)),
        "probe only: full rank 104; crossing-hop rank 32/infeasible; five necessary slices",
    )

    gram = h.herm(h.half_block(h.THETA_PRIME, h.HQ_FREE))
    escape = sp.expand(gram.xreplace(h.modulus_point(h.escape_witness_field())))
    flat = sp.expand(gram.xreplace(h.modulus_point(h.flat_field())))
    checks.add(
        "F-finite-mass-gram",
        escape == h.R(15, 64) * sp.diag(1, 0, 1, 0, 0, 1, 0, 1)
        and h.congruence_inertia(escape) == (4, 4, 0)
        and h.zero(flat),
        "escape carrier inertia (4,4,0); flat carrier Gram zero",
    )

    completed = solved[(0, 0)]["completed"]
    cover_residue = sp.expand(
        sp.I * (h.COVER_FREE * completed + completed.H * h.COVER_FREE)
    )
    formal = h.formal_compression(cover_residue)
    checks.add(
        "G-formal-compression-versus-descent",
        formal == h.residue(completed)
        and not h.zero(h.descent_residual(cover_residue)),
        "SELECT M LIFT is computed; the separate intertwining residual is nonzero",
    )

    checks.add(
        "H-exact-finite-scope",
        h.no_float((probe, escape, solved)),
        "supplied finite matrices only; no physical quotient or action identification",
    )
    return checks.emit()


if __name__ == "__main__":
    sys.exit(main())
