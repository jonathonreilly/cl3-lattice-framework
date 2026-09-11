#!/usr/bin/env python3
"""Corrected Block 167 finite null-model and hollow-corner certificate.

The QCA is a reference-imposed comparison object.  This producer checks the
counterexample missed by the historical universal claim and records finite
generator/control tables.  It makes no physical or all-carrier conclusion.
"""

from __future__ import annotations

import sys

import sympy as sp

import admissibility_dirac_kahler_released7315_c_fixture_helpers_2026_09_10 as h


R = sp.Rational
I = sp.I
SLICE_C = 1

AUDIT_INPUT_PATHS = ('scripts/admissibility_dirac_kahler_released7315_c_fixture_helpers_2026_09_10.py',
 'scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py',
 'docs/ADMISSIBILITY_DIRAC_KAHLER_NULL_MODEL_CORNER_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-21.md',
 '.claude/science/physics-loops/toe-axiom-closure-block167-null-model-corner-theorem-20260821/NO_GO_LEDGER.md',
 'docs/MINIMAL_AXIOMS_2026-06-29.md',
 'docs/audit/data/axiom_premise_nodes.json',
 'scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py',
 'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py',
 'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md')

INPUT_SHA256 = {'scripts/admissibility_dirac_kahler_released7315_c_fixture_helpers_2026_09_10.py': '90d9e48440a8a74eabd73553ab61322cf0b75a11de9be1cd65eaee6b5bc6c0db',
 'scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py': '37e2520596484df264bc169a6c7ced21575c2e7784bc78d668338ec30dcc4383',
 'docs/ADMISSIBILITY_DIRAC_KAHLER_NULL_MODEL_CORNER_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-21.md': 'b141d283b8304ef696df9816eceb568c78f610a46c1034bfdf7b0492acf15387',
 '.claude/science/physics-loops/toe-axiom-closure-block167-null-model-corner-theorem-20260821/NO_GO_LEDGER.md': 'd3c5de71937203f663ec0c72ecf8cc3a063d9ce9b90022375e27ac84cb8b0e71',
 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
 'docs/audit/data/axiom_premise_nodes.json': '615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37',
 'scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py': '0974a71bab3c753e66692740e303ea8062bfa7b6bd88fdc4a2c665d61ac95f87',
 'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py': '5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445',
 'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md': '9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33'}

SOURCE_AST_MAP = {
    "original_block167": {
        "path": "scripts/admissibility_dirac_kahler_null_model_corner_theorem_2026_08_21.py",
        "source_sha256": "a64bd52c7e9da0a3376c69c4562f944681a540815e6460a552d97fa4a73c269d",
        "nodes": {
            "cayley_cs": [583, 586],
            "cayley_phase": [589, 592],
            "pair_unitary": [595, 602],
            "qca_step": [605, 625],
            "qca_history": [628, 653],
            "refutation_probe": [933, 1019],
            "named_generator_probe": [1271, 1293],
        },
    }
}

NULL_GRID = (
    (sp.Integer(1), sp.Integer(0), sp.Integer(0)),
    (sp.Integer(1), R(1, 2), sp.Integer(0)),
    (sp.Integer(1), sp.Integer(0), R(3, 5)),
    (sp.Integer(1), R(1, 2), R(3, 5)),
    (sp.Integer(1), -R(1, 2), R(3, 5)),
    (R(1, 3), R(1, 4), -R(2, 5)),
    (sp.Integer(3), R(3, 4), R(1, 5)),
    (sp.Integer(0), R(1, 8), R(3, 5)),
)


def cayley_cs(half_tangent):
    value = sp.sympify(half_tangent)
    return (
        sp.cancel((1 - value ** 2) / (1 + value ** 2)),
        sp.cancel(2 * value / (1 + value ** 2)),
    )


def cayley_phase(sigma):
    value = sp.sympify(sigma)
    return sp.cancel((1 + I * value / 2) / (1 - I * value / 2))


def pair_unitary(lx: int, pairs, block: sp.MatrixBase) -> sp.Matrix:
    out = sp.eye(lx)
    for left, right in pairs:
        out[left, left] = block[0, 0]
        out[left, right] = block[0, 1]
        out[right, left] = block[1, 0]
        out[right, right] = block[1, 1]
    return out


def qca_step(lx: int, mass, st, sigma) -> sp.Matrix:
    """Reference-imposed partitioned unitary; not a framework object."""
    cos_t, sin_t = cayley_cs(sp.sympify(st) / 2)
    phase = cayley_phase(sigma)
    transport = sp.Matrix([
        [cos_t, -sp.conjugate(phase) * sin_t],
        [phase * sin_t, cos_t],
    ])
    cos_m, sin_m = cayley_cs(sp.sympify(mass) / 2)
    coin = sp.Matrix([[cos_m, -I * sin_m], [-I * sin_m, cos_m]])
    even = [(index, index + 1) for index in range(0, lx, 2)]
    odd = [(index, (index + 1) % lx) for index in range(1, lx, 2)]
    return sp.expand(
        pair_unitary(lx, even, coin)
        * pair_unitary(lx, odd, transport)
        * pair_unitary(lx, even, transport)
    )


def qca_history(
    fixture: h.Fixture,
    mass,
    st,
    sigma,
    carrier: dict,
    wrap_sign: int = -1,
) -> tuple[dict, sp.Matrix]:
    """The reference-imposed nearest-slice history used in the comparison."""
    step = qca_step(fixture.LX, mass, st, sigma)
    diagonal = h.hodge_trace(fixture)
    out: dict = {}
    for time in range(fixture.PHYS_T):
        for space in range(fixture.LX):
            value = sp.expand(mass * diagonal[(time, space)]).subs(carrier)
            if value != 0:
                index = fixture.LX * time + space
                out[(index, index)] = value
    for time in range(fixture.PHYS_T):
        target = (time + 1) % fixture.PHYS_T
        sign = wrap_sign if target == 0 else 1
        for target_x in range(fixture.LX):
            for source_x in range(fixture.LX):
                value = step[target_x, source_x]
                if value != 0:
                    out[(fixture.LX * target + target_x, fixture.LX * time + source_x)] = sign * value
                reverse = step.H[source_x, target_x]
                if reverse != 0:
                    out[(fixture.LX * time + source_x, fixture.LX * target + target_x)] = sign * reverse
    return h.sclean(out), step


def block_form(diagonal: sp.MatrixBase, cross: sp.MatrixBase) -> sp.Matrix:
    diagonal, cross = sp.Matrix(diagonal), sp.Matrix(cross)
    return sp.Matrix(sp.BlockMatrix([
        [diagonal, cross],
        [cross.H, sp.zeros(cross.cols, cross.cols)],
    ]))


NAMED_GENERATORS = (
    ("E_t", lambda: h.ET),
    ("E_t+E_t^T", lambda: h.ET + h.ET.T),
    ("E_t+2J3", lambda: h.ET + sp.diag(-1, -1, 1, 1)),
    ("E_t+I", lambda: h.ET + sp.eye(4)),
    ("E_tE_t^T+E_t", lambda: h.ET + h.ET * h.ET.T),
    ("i(E_t-E_t^T)", lambda: I * (h.ET - h.ET.T)),
    ("2J3 (hop-free)", lambda: sp.diag(-1, -1, 1, 1)),
)


def named_generator_table(fixture: h.Fixture) -> tuple:
    bench = h.Bench(fixture, SLICE_C)
    out = []
    for name, build in NAMED_GENERATORS:
        generator = sp.Matrix(build())
        edge = fixture.connection_for(I * h.SX, I * h.ST, generator)[(0, 0)]
        action = fixture.quotient_action(edge, bench.hodge, h.MASS)
        form = bench.pair_action(action)
        cross_one = sp.expand(form[:fixture.LX, fixture.LX:].diff(h.ST))
        rank = sp.expand(cross_one.subs(bench.carrier(st=0))).rank()
        evaluated = sp.expand(form.subs(bench.carrier(st=R(1, 2))))
        hop = any(
            generator[row, column] != 0 and (row < 2) != (column < 2)
            for row in range(4)
            for column in range(4)
        )
        out.append((name, hop, rank, h.inertia_pzn(evaluated)))
    return tuple(out)


def recomputed_control_trace(fixture: h.Fixture) -> sp.Expr:
    c = SLICE_C
    field = {cell: (R(3, 5), R(1, 2)) for cell in fixture.CELLS}
    substitution = h.carrier_substitution(fixture, field)
    substitution.update({h.SX: R(3, 5), h.ST: R(1, 2), h.MASS: 1})
    action = h.dense(
        fixture.quotient_action(fixture.edge_d[(0, 0)], fixture.H_free, h.MASS),
        fixture.PHYS,
        fixture.PHYS,
    )
    outgoing = sp.expand(
        action[fixture.slice_rows(c + 1), fixture.slice_rows(c)].subs(substitution)
    )
    diagonal = h.hodge_trace(fixture)
    gram_c = sp.diag(*[
        sp.expand(diagonal[(c, space)]).subs(substitution)
        for space in range(fixture.LX)
    ])
    gram_next = sp.diag(*[
        sp.expand(diagonal[((c + 1) % fixture.PHYS_T, space)]).subs(substitution)
        for space in range(fixture.LX)
    ])
    return sp.cancel(sp.trace(gram_c.inv() * outgoing.H * gram_next * outgoing))


def main() -> int:
    checks = h.Checks()
    identity_ok, actual = h.verify_input_hashes(INPUT_SHA256)
    checks.add("A-input-identity", identity_ok, f"nine exact inputs; actual={actual}")

    positive = sp.diag(3, 5, 7, 11)
    negative = -sp.eye(4)
    zero_cross = sp.zeros(4, 4)
    nonzero_cross = sp.diag(1, 0, 0, 0)
    checks.add(
        "B-hollow-block-hypotheses",
        h.is_psd(block_form(positive, zero_cross))
        and not h.is_psd(block_form(negative, zero_cross))
        and not h.is_psd(block_form(positive, nonzero_cross)),
        "finite controls distinguish C=0 from the additional necessary condition B>=0",
    )

    anti_rows = []
    for value in (I * sp.eye(4), I * sp.diag(1, 2, 3, 5)):
        form = block_form(positive, h.herm(value))
        anti_rows.append((value.rank(), h.zero(h.herm(value)), h.inertia_pzn(form)))
    checks.add(
        "C-invertible-antihermitian-family",
        all(rank == 4 and cross_zero and inertia == (4, 4, 0)
            for rank, cross_zero, inertia in anti_rows),
        f"only the exhibited invertible members carry rank four; rows={anti_rows}",
    )

    counterexamples = {}
    grid_tables = {}
    generator_tables = {}
    controls = {}
    for tag, cover_t, lx in (("8x4", 8, 4), ("12x4", 12, 4)):
        fixture = h.Fixture(cover_t, lx, tag)
        bench = h.Bench(fixture, SLICE_C)
        carrier = bench.carrier(st=0, mass=2)
        history, step = qca_history(fixture, 2, 0, R(3, 5), carrier)
        paired = fixture.pairing(bench.reflection, history, bench.rows)
        counterexamples[tag] = (
            h.zero(step + step.H),
            h.zero(step.H * step - sp.eye(lx)),
            step.rank(),
            h.zero(paired[:lx, lx:]),
            h.zero(paired[lx:, lx:]),
            h.inertia_pzn(paired),
        )
        grid = []
        for mass, st, sigma in NULL_GRID:
            historical, unitary = qca_history(fixture, mass, st, sigma, carrier)
            form = fixture.pairing(bench.reflection, historical, bench.rows)
            grid.append((mass, st, sigma, h.zero(unitary.H * unitary - sp.eye(lx)),
                         unitary.rank(), h.inertia_pzn(form)))
        grid_tables[tag] = tuple(grid)
        generator_tables[tag] = named_generator_table(fixture)
        controls[tag] = recomputed_control_trace(fixture)

    checks.add(
        "D-qca-counterexample",
        all(row == (True, True, 4, True, True, (4, 4, 0))
            for row in counterexamples.values()),
        f"mass=2, st=0 gives anti-Hermitian unitary U, C=herm(U)=0 and PSD; {counterexamples}",
    )
    checks.add(
        "E-eight-reference-samples",
        all(len(rows) == 8 and all(unitary and rank == 4 for _, _, _, unitary, rank, _ in rows)
            for rows in grid_tables.values()),
        f"finite unitary/full-rank table retained without a universal exclusion; {grid_tables}",
    )
    checks.add(
        "F-generator-scope",
        all(
            next(row for row in rows if row[0].startswith("2J3"))[1:] == (False, 0, (4, 4, 0))
            for rows in generator_tables.values()
        ),
        f"hop-free 2J3 has zero C1 rank and remains PSD; hop-carrying rows are only a finite table; {generator_tables}",
    )
    checks.add(
        "G-recomputed-action-control",
        all(value.is_Rational and value > 0 for value in controls.values()),
        f"control trace is recomputed from the outgoing action block; {controls}",
    )
    checks.add(
        "H-exact-bounded-scope",
        h.no_float((counterexamples, grid_tables, generator_tables, controls))
        and len(SOURCE_AST_MAP) == 1,
        "two finite extents; no framework adoption, all-carrier theorem, or physical closure",
    )
    return checks.emit()


if __name__ == "__main__":
    sys.exit(main())
