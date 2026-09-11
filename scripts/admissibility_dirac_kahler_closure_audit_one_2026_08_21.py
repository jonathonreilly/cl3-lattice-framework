#!/usr/bin/env python3
"""Corrected Block 169 finite link, imposed-d2, and support certificate.

Despite the historical filename, this is not an exhaustive audit.  It checks
two finite primary fixtures, a five-row index census, time-slice-dependent
couplings, and seven named point samples per primary fixture.
"""

from __future__ import annotations

import sys

import sympy as sp

import admissibility_dirac_kahler_released7315_c_fixture_helpers_2026_09_10 as h


R = sp.Rational
I = sp.I
G2 = sp.Symbol("g_2", real=True)
SLICE_C = 1

AUDIT_INPUT_PATHS = ('scripts/admissibility_dirac_kahler_released7315_c_fixture_helpers_2026_09_10.py',
 'scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py',
 'docs/ADMISSIBILITY_DIRAC_KAHLER_CLOSURE_AUDIT_ONE_BOUNDED_THEOREM_NOTE_2026-08-21.md',
 '.claude/science/physics-loops/toe-axiom-closure-block169-closure-audit-one-20260821/NO_GO_LEDGER.md',
 'docs/MINIMAL_AXIOMS_2026-06-29.md',
 'docs/audit/data/axiom_premise_nodes.json',
 'scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py',
 'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py',
 'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md')

INPUT_SHA256 = {'scripts/admissibility_dirac_kahler_released7315_c_fixture_helpers_2026_09_10.py': '90d9e48440a8a74eabd73553ab61322cf0b75a11de9be1cd65eaee6b5bc6c0db',
 'scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py': '37e2520596484df264bc169a6c7ced21575c2e7784bc78d668338ec30dcc4383',
 'docs/ADMISSIBILITY_DIRAC_KAHLER_CLOSURE_AUDIT_ONE_BOUNDED_THEOREM_NOTE_2026-08-21.md': '297a3b3d5c685a25f4ab86d666667b945faa798fbe429bd21c627f7328b9e0b7',
 '.claude/science/physics-loops/toe-axiom-closure-block169-closure-audit-one-20260821/NO_GO_LEDGER.md': 'cdf7a0bde78118daaa0a16e3508b5a6acaf2cba6d4dd9ac796f31deb915cfba2',
 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
 'docs/audit/data/axiom_premise_nodes.json': '615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37',
 'scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py': '0974a71bab3c753e66692740e303ea8062bfa7b6bd88fdc4a2c665d61ac95f87',
 'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py': '5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445',
 'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md': '9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33'}

SOURCE_AST_MAP = {
    "original_block169": {
        "path": "scripts/admissibility_dirac_kahler_closure_audit_one_2026_08_21.py",
        "source_sha256": "4a878575ea79ba08cdbc092808f24709f29ef0ed2fe96bc70d068f53fa84becb",
        "nodes": {
            "generic_slice_blocks": [657, 668],
            "two_slice_local": [671, 690],
            "inhomogeneous_connection": [693, 723],
            "link_probe": [833, 989],
            "inhomogeneous_probe": [995, 1038],
            "disposal_probe": [1044, 1239],
            "injectivity_probe": [1245, 1316],
        },
    }
}

POINT_SAMPLES = {
    "8x4": (
        (R(1, 3), R(1, 2), 10, False),
        (10, R(1, 2), 10, True),
        (R(1, 3), R(1, 2), R(1, 10), False),
        (10, R(1, 2), R(1, 10), True),
        (1, R(1, 2), R(1, 10), False),
        (1, R(1, 4), R(1, 10), True),
        (1, R(1, 2), 100, False),
    ),
    "12x4": (
        (R(1, 3), R(1, 2), 100, False),
        (3, R(1, 2), 100, True),
        (R(1, 3), R(1, 2), R(1, 10), False),
        (3, R(1, 2), R(1, 10), True),
        (1, R(1, 2), R(1, 50), False),
        (1, R(1, 4), R(1, 50), True),
        (1, R(1, 2), 100, False),
    ),
}


def generic_slice_blocks(fixture: h.Fixture) -> dict:
    out: dict = {}
    for target_t in range(fixture.PHYS_T):
        for source_t in range(fixture.PHYS_T):
            for target_x in range(fixture.LX):
                for source_x in range(fixture.LX):
                    out[(fixture.LX * target_t + target_x,
                         fixture.LX * source_t + source_x)] = (
                        sp.Symbol(f"q{target_t}_{source_t}_{target_x}{source_x}r", real=True)
                        + I * sp.Symbol(f"q{target_t}_{source_t}_{target_x}{source_x}i", real=True)
                    )
    return h.sclean(out)


def two_slice_local(fixture: h.Fixture) -> dict:
    blocks: dict[tuple[int, int], sp.Matrix] = {}
    for time in range(fixture.PHYS_T):
        diagonal = sp.Matrix(fixture.LX, fixture.LX, lambda row, column: (
            sp.Symbol(f"e{time}_{row}{column}r", real=True)
            + I * sp.Symbol(f"e{time}_{row}{column}i", real=True)
        ))
        blocks[(time, time)] = h.herm(diagonal)
        hop = sp.Matrix(fixture.LX, fixture.LX, lambda row, column: (
            sp.Symbol(f"f{time}_{row}{column}r", real=True)
            + I * sp.Symbol(f"f{time}_{row}{column}i", real=True)
        ))
        target = (time + 1) % fixture.PHYS_T
        blocks[(target, time)] = hop
        blocks[(time, target)] = hop.H
    return h.block_operator(fixture, blocks)


def inhomogeneous_connection(
    fixture: h.Fixture,
    temporal: dict[int, sp.Symbol],
    spatial: dict[int, sp.Symbol] | None = None,
) -> dict:
    """One coupling per cover-time slice, spatially constant on that slice."""
    chart_d: dict = {}
    for origin in h.ORIGINS:
        gauge = (h.SHIFT_T ** origin[0]) * (h.SHIFT_X ** origin[1])
        out: dict = {}
        for anchor in fixture.chart_cells(origin):
            time = anchor[0] % fixture.COVER_T
            sx = h.SX if spatial is None else spatial[time]
            local = I * (sx * h.EX + temporal[time] * h.ET)
            block = sp.expand(gauge.H * local * gauge)
            sites = fixture.cell_sites(*anchor)
            for row in range(4):
                for column in range(4):
                    if block[row, column] != 0:
                        key = (sites[row], sites[column])
                        out[key] = out.get(key, 0) + block[row, column]
        chart_d[origin] = h.sclean(out)
    star = h.sadd(chart_d[(0, 0)], h.sscale(chart_d[(1, 0)], -1))
    return {
        (h.CHART_INDEX[left], h.CHART_INDEX[right]): h.sadd(
            chart_d[left],
            h.sscale(
                star,
                h.HEALING_WEIGHTS[h.CHART_INDEX[right]]
                - h.HEALING_WEIGHTS[h.CHART_INDEX[left]],
            ),
        )
        for left in h.ORIGINS
        for right in h.ORIGINS
    }


def reflected_corner(fixture: h.Fixture, action: dict, c: int) -> sp.Matrix:
    matrix = h.dense(action, fixture.PHYS, fixture.PHYS)
    block = matrix[fixture.slice_rows(c - 1), fixture.slice_rows(c + 1)]
    return h.herm(block)


def link_liveness_census() -> tuple[bool, tuple]:
    rows = []
    all_ok = True
    for physical_t in (4, 5, 6, 7, 8):
        fixture = h.Fixture(2 * physical_t, 2, f"T{physical_t}")
        local = two_slice_local(fixture)
        use_rows = fixture.slice_rows(SLICE_C, SLICE_C + 1)
        measured, predicted = [], []
        for label in h.link_labels_x_trivial(fixture):
            delta = (label[1] - 2 * SLICE_C - 1) % physical_t
            form = fixture.pairing(fixture.descent(label), local, use_rows)
            measured.append(not h.zero(form[2:, 2:]))
            predicted.append(((delta - 1) % physical_t) in (0, 1, physical_t - 1))
        all_ok &= measured == predicted
        rows.append((physical_t, sum(measured), len(measured)))
    return all_ok, tuple(rows)


def link_dictionary(fixture: h.Fixture) -> bool:
    action = generic_slice_blocks(fixture)
    dense_action = h.dense(action, fixture.PHYS, fixture.PHYS)
    c, lx, period = SLICE_C, fixture.LX, fixture.PHYS_T
    rows = fixture.slice_rows(c, c + 1)
    for label in h.link_labels_x_trivial(fixture):
        reflection = fixture.descent(label)
        signs = {
            time: next(int(value) for (row, _), value in reflection.items()
                       if row // lx == time)
            for time in range(period)
        }
        image = {time: (label[1] - time) % period for time in range(period)}
        form = fixture.pairing(reflection, action, rows)

        def block(target: int, source: int) -> sp.Matrix:
            return sp.expand(dense_action[
                fixture.slice_rows(target), fixture.slice_rows(source)
            ])

        wanted_b = h.herm(signs[c] * block(image[c], c))
        wanted_d = h.herm(signs[c + 1] * block(image[c + 1], c + 1))
        wanted_c = sp.expand((
            signs[c] * block(image[c], c + 1)
            + signs[c + 1] * block(image[c + 1], c).H
        ) / 2)
        if not (
            h.zero(form[:lx, :lx] - wanted_b)
            and h.zero(form[:lx, lx:] - wanted_c)
            and h.zero(form[lx:, lx:] - wanted_d)
        ):
            return False
    return True


def inhomogeneous_table(fixture: h.Fixture, bench: h.Bench) -> dict:
    temporal = {
        time: sp.Symbol(f"g_{fixture.tag}_{time}", real=True)
        for time in range(fixture.COVER_T)
    }
    spatial = {
        time: sp.Symbol(f"k_{fixture.tag}_{time}", real=True)
        for time in range(fixture.COVER_T)
    }
    dg = inhomogeneous_connection(fixture, temporal)
    dgk = inhomogeneous_connection(fixture, temporal, spatial)
    pin_g = {symbol: h.ST for symbol in temporal.values()}
    pin_gk = dict(pin_g)
    pin_gk.update({symbol: h.SX for symbol in spatial.values()})
    pins = (
        all(h.ssubs(dg[key], pin_g) == fixture.edge_d[key] for key in fixture.EDGE_KEYS),
        all(h.ssubs(dgk[key], pin_gk) == fixture.edge_d[key] for key in fixture.EDGE_KEYS),
    )
    cells = []
    for region, hodge in (("region", bench.hodge), ("offregion", fixture.H_free)):
        for name, builder in (
            ("action", lambda differential, hh=hodge: fixture.quotient_action(differential, hh, h.MASS)),
            ("first_order", lambda differential, hh=hodge: h.first_order(fixture, hh, differential)),
            ("second_order", lambda differential, hh=hodge: h.second_order(fixture, hh, differential, differential)),
        ):
            for coupling, differential in (("g[t]", dg[(0, 0)]), ("g[t],k[t]", dgk[(0, 0)])):
                corner = reflected_corner(fixture, builder(differential), SLICE_C)
                symbols = h.free_symbols_of(corner)
                cells.append((
                    region,
                    name,
                    coupling,
                    all(sp.expand(corner[index, index]) == 0 for index in range(fixture.LX)),
                    not h.zero(corner),
                    bool(symbols & (set(temporal.values()) | set(spatial.values()))),
                ))
    return {"pins": pins, "cells": tuple(cells)}


def imposed_d2_table(fixture: h.Fixture, bench: h.Bench) -> dict:
    d2 = h.displacement_two_shift(fixture, I * G2)
    square = h.smul(d2, d2)
    rows = {row: 0 for row in range(fixture.SIZE)}
    columns = {column: 0 for column in range(fixture.SIZE)}
    for row, column in d2:
        rows[row] += 1
        columns[column] += 1
    addition = h.first_order(fixture, bench.hodge, d2)
    form = bench.pair_action(h.sadd(bench.action, addition))
    samples = []
    for mass, st, coupling, expected_psd in POINT_SAMPLES[fixture.tag]:
        env = bench.carrier(mass=mass, st=st)
        evaluated = sp.expand(form.subs(env).subs({G2: coupling}))
        samples.append((mass, st, coupling, h.inertia_pzn(evaluated), expected_psd))
    return {
        "square_nonzero": bool(square),
        "one_per_row_column": set(rows.values()) == {1} and set(columns.values()) == {1},
        "rank_when_g2_one": h.dense(d2, fixture.SIZE, fixture.SIZE).subs({G2: 1}).rank(),
        "samples": tuple(samples),
    }


def metric_support_and_injectivity(fixture: h.Fixture, bench: h.Bench) -> dict:
    metric = h.dense(fixture.quotient(fixture.H_free), fixture.PHYS, fixture.PHYS)
    support = {
        (row, column)
        for row in range(fixture.PHYS)
        for column in range(fixture.PHYS)
        if sp.expand(metric[row, column]) != 0
    }
    classes = {"x_trivial": [], "x_reflecting": []}
    for label in fixture.involutive:
        if fixture.fixed_slice(label) != SLICE_C:
            continue
        reflection = h.dense(fixture.descent(label), fixture.PHYS, fixture.PHYS)
        transformed = sp.expand(reflection * metric * reflection)
        forbidden = sum(
            (row, column) not in support and sp.expand(transformed[row, column]) != 0
            for row in range(fixture.PHYS)
            for column in range(fixture.PHYS)
        )
        key = "x_trivial" if label[2] == 1 else "x_reflecting"
        classes[key].append((label, forbidden))

    shears = tuple(fixture.B.values())
    maps = {}
    for name, hodge in (("offregion", fixture.H_free), ("region", bench.hodge)):
        action = fixture.quotient_action(fixture.edge_d[(0, 0)], hodge, h.MASS)
        form = bench.pair_action(action)
        cross = sp.expand(form[:fixture.LX, fixture.LX:].subs({h.ST: 0, h.SX: 0, h.MASS: 1}))
        maps[name] = (h.coefficient_rank(cross, shears), h.zero(cross))
    return {"support": classes, "maps": maps}


def main() -> int:
    checks = h.Checks()
    identity_ok, actual = h.verify_input_hashes(INPUT_SHA256)
    checks.add("A-input-identity", identity_ok, f"nine exact inputs; actual={actual}")

    liveness_ok, liveness_rows = link_liveness_census()
    checks.add(
        "B-link-index-census",
        liveness_ok and liveness_rows == ((4, 4, 4), (5, 3, 5), (6, 4, 6), (7, 3, 7), (8, 4, 8)),
        f"five finite T rows at Lx=2; rows={liveness_rows}",
    )

    dictionaries, inhomogeneous, d2_tables, metric_tables = {}, {}, {}, {}
    for tag, cover_t, lx in (("8x4", 8, 4), ("12x4", 12, 4)):
        fixture = h.Fixture(cover_t, lx, tag)
        bench = h.Bench(fixture, SLICE_C)
        dictionaries[tag] = link_dictionary(fixture)
        inhomogeneous[tag] = inhomogeneous_table(fixture, bench)
        d2_tables[tag] = imposed_d2_table(fixture, bench)
        metric_tables[tag] = metric_support_and_injectivity(fixture, bench)

    checks.add(
        "C-link-dictionary",
        all(dictionaries.values()),
        f"fully non-Hermitian block dictionary at the two named fixtures only; {dictionaries}",
    )
    checks.add(
        "D-time-slice-couplings",
        all(row["pins"] == (True, True) and len(row["cells"]) == 12
            and all(cell[3] for cell in row["cells"])
            for row in inhomogeneous.values()),
        "g[t] and k[t] are spatially constant on each cover-time slice; 24 selected zero-diagonal cells, including disclosed vacuous cells",
    )
    checks.add(
        "E-imposed-d2-is-not-a-complex",
        all(row["square_nonzero"] and row["one_per_row_column"]
            and row["rank_when_g2_one"] in (32, 48)
            for row in d2_tables.values()),
        f"d2 is invertible for g2!=0 but d2^2!=0, so no chain complex or cohomology is defined; {d2_tables}",
    )
    checks.add(
        "F-seven-point-rows",
        all(len(row["samples"]) == 7
            and all((here[2] == 0) == wanted
                    for *_, here, wanted in row["samples"])
            for row in d2_tables.values()),
        "the fourteen cells are pointwise PSD/non-PSD tests only; they do not establish endpoint laws or monotonicity",
    )
    checks.add(
        "G-metric-support-and-selected-map",
        all(
            any(count > 0 for _, count in row["support"]["x_trivial"])
            and all(count == 0 for _, count in row["support"]["x_reflecting"])
            and row["maps"]["offregion"] == (8, False)
            and row["maps"]["region"] == (0, True)
            for row in metric_tables.values()
        ),
        f"x-reflecting rows show zero-forbidden-entry support compatibility only; selected shear-map rows={metric_tables}",
    )
    checks.add(
        "H-exact-bounded-scope",
        h.no_float((liveness_rows, dictionaries, inhomogeneous, d2_tables, metric_tables))
        and len(SOURCE_AST_MAP) == 1,
        "finite named classes only; no endpoint theorem, cone preservation, wall independence, or physical closure",
    )
    return checks.emit()


if __name__ == "__main__":
    sys.exit(main())
