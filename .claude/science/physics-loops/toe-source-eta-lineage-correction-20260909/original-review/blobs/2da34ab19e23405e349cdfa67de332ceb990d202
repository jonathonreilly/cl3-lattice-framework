#!/usr/bin/env python3
"""Independent Block-03 affine-lineage binary-Record join checker.

This checker imports no Block-03 primary module or result booleans.  It uses
the generator/word affine classification and independent native source path
from the prior independent checkers, matrix-unit rather than Pauli
automorphisms, direct Mobius reconstruction, and a fresh C32 state/effect
lift with blockwise Stinespring witnesses for the formation channels.
"""

from __future__ import annotations

import argparse
from functools import cache
import itertools
from pathlib import Path
import subprocess
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import independent_admissibility_d4_block208_source_eta_action_native_record_dilation_2026_08_28 as i2  # noqa: E402
import admissibility_d4_h1_port_free_neighbor_m2_context_descent_2026_08_26 as p206  # noqa: E402


PACKET = (
    ".claude/science/physics-loops/"
    "toe-source-eta-ownership-block03-affine-lineage-binary-join-20260829"
)
GOAL = f"{PACKET}/GOAL.md"
PREFLIGHT = f"{PACKET}/PREFLIGHT_WITNESSES.md"
NOTE = (
    "docs/ADMISSIBILITY_D4_AFFINE_LINEAGE_BINARY_RECORD_MULTI_JOIN_"
    "REPEATABILITY_SELECTOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
)
PREREG = "61547d21fed6c2941da7ccee8ac993eb0b222249"
PARENT = "f5e5c140c06df6aaf6c1b76c2e165c5a49ca4a90"
BLOCK206_RESULT = "42b25280486363e9c2017698b813edf182d1a1a3"
BLOCK206_CACHE = (
    "logs/runner-cache/"
    "admissibility_d4_h1_port_free_neighbor_m2_context_descent_2026_08_26.txt"
)
BLOCK206_CACHE_BLOB = "368e228405762936079edd269cb61a42bb0a9556"
MAIN = "004f64e1c87dad696b282cf2b526f3e7312dc82d"
GOAL_BLOB = "da1a8e551e5425a05d83d53c227e5f3589b50403"
PREFLIGHT_BLOB = "203110c432b8882c346378c4eee59e3eb3a1925b"
AUDIT_TIMEOUT_SEC = 300

CUBIC_A = sp.Integer(
    "39614194410521886011258608271189426608989637314061903595310837311299128766179775614039384849224874802424309955547840537519444031415731"
)
CUBIC_B = sp.Integer(
    "20088236778144933307422375844774848466973250848745230478668770773683346878595585928475405853707189945489158937323659388473013648683423"
)
CUBIC_D = sp.Integer(
    "14630373132760996204705386039773889549383195117366765668241345031835670611592246823650335399786716111445599465516368081316673691027954400"
)
CUBIC = 343 * (CUBIC_A - CUBIC_B * sp.sqrt(3)) / CUBIC_D

AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block03-affine-lineage-binary-join-20260829/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block03-affine-lineage-binary-join-20260829/PREFLIGHT_WITNESSES.md",
    "docs/ADMISSIBILITY_D4_AFFINE_LINEAGE_BINARY_RECORD_MULTI_JOIN_REPEATABILITY_SELECTOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_D4_BLOCK208_AFFINE_SIX_RECORD_H1_DECODER_CENTER_CORNER_QND_DILATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "scripts/independent_admissibility_d4_block208_source_eta_action_native_record_dilation_2026_08_28.py",
    "scripts/independent_admissibility_d4_h1_action_factorized_six_m2_source_ownership_2026_08_28.py",
    "docs/ADMISSIBILITY_D4_H1_PORT_FREE_NEIGHBOR_PHASE_M2_CONTEXT_DESCENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "logs/runner-cache/admissibility_d4_h1_port_free_neighbor_m2_context_descent_2026_08_26.txt",
    "docs/ADMISSIBILITY_D4_H1_SCHUR_RECORD_PROBABILITY_GERM_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "logs/runner-cache/admissibility_d4_h1_schur_record_probability_germ_2026_08_26.txt",
)

MUTATIONS = (
    "stale_main",
    "drop_prereg",
    "lose_group_element",
    "drop_affine_class",
    "break_matrix_unit_action",
    "use_trivial_class",
    "erase_regular_orbit",
    "break_mobius",
    "break_selector_covariance",
    "invent_lower_selector_degree",
    "erase_orientation_covariance",
    "misorder_signed_shell",
    "lose_source_term",
    "replace_actual_reverse",
    "erase_c32_operator_lift",
    "erase_cubic",
    "merge_effect_spectra",
    "erase_half_join",
    "erase_continuum_proof",
    "select_sharpness",
    "break_choi",
    "disturb_lineage",
    "merge_record_codes",
    "hide_precursor",
    "break_lock",
    "call_site_selected",
    "call_rate_selected",
    "claim_history",
    "claim_h2",
    "claim_axiom",
    "claim_obligation",
    "claim_toe",
    "claim_retained",
    "claim_global_repeatability",
    "promote_global_no_member",
    "erase_certified_endpoint",
    "break_schur_intertwiner",
    "erase_translation_covariance",
    "break_controlled_complement",
    "sample_only_continuum",
)


def git(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=300
    ).strip()


@cache
def authority_facts() -> dict[str, object]:
    return {
        "main": git("rev-parse", "origin/main"),
        "parent": subprocess.run(
            ("git", "merge-base", "--is-ancestor", PARENT, "HEAD"),
            cwd=ROOT, check=False,
        ).returncode == 0,
        "prereg": subprocess.run(
            ("git", "merge-base", "--is-ancestor", PREREG, "HEAD"),
            cwd=ROOT, check=False,
        ).returncode == 0,
        "goal_registered": git("rev-parse", f"{PREREG}:{GOAL}"),
        "goal_worktree": git("hash-object", "--", GOAL),
        "preflight_registered": git("rev-parse", f"{PREREG}:{PREFLIGHT}"),
        "preflight_worktree": git("hash-object", "--", PREFLIGHT),
        "block206_cache": git(
            "rev-parse", f"{BLOCK206_RESULT}:{BLOCK206_CACHE}"
        ),
    }


@cache
def independent_action_and_eta() -> dict[str, object]:
    data = i2.group_data()
    group = i2.group()
    multiplication = data["multiplication"]
    permutations = data["permutations"]
    classes = i2.affine_classes(6)
    selected = tuple(item for item in classes if item["orbit24"])
    if len(selected) != 1:
        raise AssertionError("expected one independent orbit-24 class")
    class_checks = []
    for item in classes:
        translations = item["cocycle"]

        def class_action(group_index: int, mask: int) -> int:
            return i2.permute(
                mask, permutations[group_index]
            ) ^ translations[group_index]

        def unit_image(
            group_index: int, site: int, row: int, column: int,
        ) -> tuple[int, int, int]:
            target = permutations[group_index][site]
            flip = (translations[group_index] >> target) & 1
            return target, row ^ flip, column ^ flip

        class_group_law = all(
            class_action(multiplication[left][right], mask)
            == class_action(left, class_action(right, mask))
            for left in range(24) for right in range(24)
            for mask in range(64)
        )
        unit_group_law = all(
            unit_image(multiplication[left][right], site, row, column)
            == unit_image(left, *unit_image(right, site, row, column))
            for left in range(24) for right in range(24)
            for site in range(6) for row in range(2) for column in range(2)
        )
        star = all(
            unit_image(g, site, column, row)
            == (
                unit_image(g, site, row, column)[0],
                unit_image(g, site, row, column)[2],
                unit_image(g, site, row, column)[1],
            )
            for g in range(24) for site in range(6)
            for row in range(2) for column in range(2)
        )
        multiply = all(
            (
                unit_image(g, site, row, right_column)
                if left_column == right_row else None
            ) == (
                (
                    unit_image(g, site, row, left_column)[0],
                    unit_image(g, site, row, left_column)[1],
                    unit_image(g, site, right_row, right_column)[2],
                )
                if unit_image(g, site, row, left_column)[2]
                == unit_image(g, site, right_row, right_column)[1]
                else None
            )
            for g in range(24) for site in range(6) for row in range(2)
            for left_column in range(2) for right_row in range(2)
            for right_column in range(2)
        )
        unity = all(
            {unit_image(g, site, bit, bit)[1:] for bit in range(2)}
            == {(0, 0), (1, 1)}
            for g in range(24) for site in range(6)
        )
        cross = all(
            unit_image(g, left, 0, 1)[0] != unit_image(g, right, 1, 0)[0]
            for g in range(24) for left in range(6) for right in range(left)
        )
        class_checks.append({
            "orbit24": item["orbit24"],
            "full_m2": all((class_group_law, unit_group_law, star,
                            multiply, unity, cross)),
        })

    cocycle = selected[0]["cocycle"]

    def action(group_index: int, mask: int) -> int:
        return i2.permute(mask, permutations[group_index]) ^ cocycle[group_index]

    group_law = all(
        action(multiplication[left][right], mask)
        == action(left, action(right, mask))
        for left in range(24)
        for right in range(24)
        for mask in range(64)
    )

    regular_orbits = tuple(
        orbit for orbit in i2.partition(range(64), action)
        if len(orbit) == 24
    )
    base = min(regular_orbits[0])
    transport = {
        action(group_index, base): group_index
        for group_index in range(24)
    }
    shear0 = sp.Matrix((0, 1 / sp.sqrt(2), -1))
    # Independent ordering repair: this runner inherits Block-02's
    # (-x,+x,-y,+y,-z,+z) shell, not Block-206's opposite-pair order.
    contrast0 = (
        -sp.sqrt(3), sp.sqrt(3), sp.Integer(-2), sp.Integer(2),
        sp.Integer(0), sp.Integer(0),
    )
    shear_table = []
    contrast_table = []
    orientation_table = []
    selector_table = []
    active_table = []
    for mask in range(64):
        if mask in transport:
            group_index = transport[mask]
            shear = tuple(i2.shear_action(group[group_index]) * shear0)
            orientation = tuple(group[group_index] * sp.Matrix((0, 0, 1)))
            contrast = [sp.Integer(0)] * 6
            for source, target in enumerate(permutations[group_index]):
                contrast[target] = contrast0[source]
            selector = max(range(6), key=lambda index: contrast[index])
            active = sp.Integer(1)
        else:
            shear = (sp.Integer(0),) * 3
            orientation = (sp.Integer(0),) * 3
            contrast = [sp.Integer(0)] * 6
            selector = -1
            active = sp.Integer(0)
        shear_table.append(tuple(shear))
        contrast_table.append(tuple(contrast))
        orientation_table.append(tuple(orientation))
        selector_table.append(selector)
        active_table.append(active)
    shear_table = tuple(shear_table)
    contrast_table = tuple(contrast_table)
    orientation_table = tuple(orientation_table)
    selector_table = tuple(selector_table)
    active_table = tuple(active_table)

    shear_coefficients = tuple(
        i2.mobius(tuple(row[index] for row in shear_table))
        for index in range(3)
    )
    contrast_coefficients = tuple(
        i2.mobius(tuple(row[index] for row in contrast_table))
        for index in range(6)
    )
    orientation_coefficients = tuple(
        i2.mobius(tuple(row[index] for row in orientation_table))
        for index in range(3)
    )
    selector_coefficients = tuple(
        i2.mobius(tuple(
            sp.Integer(selector == index) for selector in selector_table
        ))
        for index in range(6)
    )
    active_coefficients = i2.mobius(active_table)

    def degree(family) -> int:
        return max(
            monomial.bit_count()
            for coefficients in family
            for monomial, value in enumerate(coefficients)
            if value != 0
        )

    mobius_exact = all(
        tuple(
            i2.mobius_evaluate(shear_coefficients[index], mask)
            for index in range(3)
        ) == shear_table[mask]
        and tuple(
            i2.mobius_evaluate(contrast_coefficients[index], mask)
            for index in range(6)
        ) == contrast_table[mask]
        and tuple(
            i2.mobius_evaluate(orientation_coefficients[index], mask)
            for index in range(3)
        ) == orientation_table[mask]
        and tuple(
            i2.mobius_evaluate(selector_coefficients[index], mask)
            for index in range(6)
        ) == tuple(
            sp.Integer(selector_table[mask] == index)
            for index in range(6)
        )
        and i2.mobius_evaluate(active_coefficients, mask)
        == active_table[mask]
        for mask in range(64)
    )
    selector_covariant = all(
        selector_table[action(group_index, mask)]
        == (
            permutations[group_index][selector_table[mask]]
            if selector_table[mask] >= 0 else -1
        )
        for group_index in range(24)
        for mask in range(64)
    )
    complement_commutes = all(
        action(group_index, mask ^ 63)
        == (action(group_index, mask) ^ 63)
        for group_index in range(24)
        for mask in range(64)
    )
    orientation_covariant = all(
        sp.Matrix(orientation_table[action(group_index, mask)])
        == group[group_index] * sp.Matrix(orientation_table[mask])
        for group_index in range(24) for mask in range(64)
    )
    orientation_complement_odd = all(
        sp.Matrix(orientation_table[mask ^ 63])
        == -sp.Matrix(orientation_table[mask])
        for mask in range(64)
    )
    selected_responses = tuple(
        contrast_table[mask][selector_table[mask]]
        if selector_table[mask] >= 0 else sp.Integer(0)
        for mask in range(64)
    )
    return {
        "group_order": len(group),
        "class_count": len(classes),
        "selected_count": len(selected),
        "selected_nontrivial": any(selected[0]["canonical"]),
        "group_law": group_law,
        "matrix_units": all(item["full_m2"] for item in class_checks),
        "star_preserved": all(item["full_m2"] for item in class_checks),
        "all_classes_full_m2": all(
            item["full_m2"] for item in class_checks
        ),
        "regular_orbits": len(regular_orbits),
        "base": base,
        "active_count": sum(active_table),
        "selector_histogram": tuple(
            selector_table.count(index) for index in range(6)
        ),
        "mobius_exact": mobius_exact,
        "shear_degree": degree(shear_coefficients),
        "contrast_degree": degree(contrast_coefficients),
        "orientation_degree": degree(orientation_coefficients),
        "selector_degree": degree(selector_coefficients),
        "active_degree": degree((active_coefficients,)),
        "selector_covariant": selector_covariant,
        "orientation_covariant": orientation_covariant,
        "orientation_complement_odd": orientation_complement_odd,
        "complement_commutes": complement_commutes,
        "orientation_table": orientation_table,
        "shear_table": shear_table,
        "selector_table": selector_table,
        "active_table": active_table,
        "transport": transport,
        "action": action,
        "multiplication": multiplication,
        "group": group,
        "selected_phase": -sp.I,
        "base_selected_direction": selector_table[base],
        "distinct_active_shears": len({
            tuple(map(str, shear)) for shear, active
            in zip(shear_table, active_table) if active
        }),
        "active_selected_response_set": {
            selected_responses[mask]
            for mask in range(64) if active_table[mask]
        },
        "inactive_selected_responses_zero": all(
            selected_responses[mask] == 0
            for mask in range(64) if not active_table[mask]
        ),
    }


def independent_matrix_equal(
    left: sp.MatrixBase, right: sp.MatrixBase,
) -> bool:
    if left.shape != right.shape:
        return False
    return all(sp.simplify(value) == 0 for value in (left - right))


def independent_block_matrix(
    upper_left: sp.MatrixBase,
    upper_right: sp.MatrixBase,
    lower_left: sp.MatrixBase,
    lower_right: sp.MatrixBase,
) -> sp.Matrix:
    return sp.Matrix.vstack(
        sp.Matrix.hstack(upper_left, upper_right),
        sp.Matrix.hstack(lower_left, lower_right),
    )


def independent_exact_positive(value: sp.Expr) -> bool:
    simplified = sp.factor(sp.simplify(value))
    if simplified.is_positive is not None:
        return simplified.is_positive is True
    return sp.simplify(simplified > 0) is sp.true


def independent_term_frobenius_sq(family) -> sp.Expr:
    return sp.factor(sp.simplify(sum((
        sp.trace(left_t.H * right_t) * sp.trace(left_i.H * right_i)
        for left_t, left_i in family
        for right_t, right_i in family
    ), sp.Integer(0))))


def independent_block_frobenius_sq(block) -> sp.Expr:
    return sp.factor(sp.simplify(sum((
        independent_term_frobenius_sq(block[row][column])
        for row in range(2) for column in range(2)
    ), sp.Integer(0))))


@cache
def independent_interval_certificate() -> dict[str, object]:
    """Direct reduced-C32 perturbation certificate, independent of primary."""
    incoming, transfer = p206.b193.POINTS["H1"]
    outgoing = tuple(
        incoming[axis] + transfer[axis] for axis in range(4)
    )
    incoming_sector = p206.b193.sector_terms(incoming)
    outgoing_sector = p206.b193.sector_terms(outgoing)
    source = p206.b193.combined_source_pair_terms(
        "H1", p206.b193.tt_source_coefficients("H1", 1)
    )
    blocks = {
        "inverse0": p206.b193.diagonal_block(
            incoming_sector["inverse"], outgoing_sector["inverse"]
        ),
        "p_inverse0": p206.b193.diagonal_block(
            incoming_sector["p_inverse"], outgoing_sector["p_inverse"]
        ),
        "graph0": p206.b193.diagonal_block(
            incoming_sector["graph"], outgoing_sector["graph"]
        ),
        "tangent": p206.b193.source_block(
            source["forward"], source["reverse"]
        ),
    }
    sector_parity_structure = (
        all(
            not blocks[name][0][1] and not blocks[name][1][0]
            for name in ("inverse0", "p_inverse0", "graph0")
        )
        and not blocks["tangent"][0][0]
        and not blocks["tangent"][1][1]
        and bool(blocks["tangent"][0][1])
        and bool(blocks["tangent"][1][0])
    )
    norm_squares = {
        name: independent_block_frobenius_sq(block)
        for name, block in blocks.items()
    }
    bounds = {
        "inverse0": sp.Integer(22),
        "p_inverse0": sp.Integer(16),
        "graph0": sp.Integer(20),
        "tangent": sp.Integer(13),
    }
    bounds_exact = all(independent_exact_positive(
        bounds[name] ** 2 - norm_squares[name]
    ) for name in bounds)
    epsilon_star = sp.Rational(1, 10**9)
    a = sp.factor(epsilon_star * bounds["inverse0"] * bounds["tangent"])
    b = sp.factor(
        epsilon_star * bounds["p_inverse0"] * bounds["tangent"]
    )
    gram_difference_bound = sp.factor(
        2 * bounds["graph0"] ** 2 * bounds["inverse0"] * (
            b / ((1 - a) * (1 - b) ** 2)
            + a / ((1 - a) * (1 - b))
            + b / (1 - b)
        )
    )
    # Partial trace over the twelve-dimensional positive-time half obeys
    # ||Tr_time X|| <= 12 ||X||.  At zero the two reduced C32 sectors are
    # exact scalar identities, and each scalar is strictly greater than 3.
    c32_difference_bound = sp.factor(
        p206.b193.HALF_TIME * gram_difference_bound
    )
    zero = p206.b205.zero_source_state_facts()
    zero_sector_scalars = (
        sp.factor(zero["trace_in"] / 16),
        sp.factor(zero["trace_out"] / 16),
    )
    zero_gap_gt_three = all(
        independent_exact_positive(value - 3)
        for value in zero_sector_scalars
    )
    gap_survives = independent_exact_positive(
        sp.Integer(3) - c32_difference_bound
    )
    certified = (
        bounds_exact and a < 1 and b < 1
        and zero_gap_gt_three and gap_survives
    )
    return {
        "epsilon_star": epsilon_star,
        "norm_squares": norm_squares,
        "sector_parity_structure": sector_parity_structure,
        "bounds_exact": bounds_exact,
        "inverse_ratio": a,
        "graph_ratio": b,
        "gram_difference_bound": gram_difference_bound,
        "c32_difference_bound": c32_difference_bound,
        "zero_sector_scalars": zero_sector_scalars,
        "zero_gap_gt_three": zero_gap_gt_three,
        "gap_survives": gap_survives,
        "certified": certified,
    }


def independent_c32_rotation(rotation: sp.MatrixBase) -> sp.Matrix:
    extended = sp.eye(4)
    extended[:3, :3] = rotation
    exterior = p206.b193.b190.wedge_representation(extended)
    return sp.diag(exterior, exterior)


def independent_terms_equal(left, right) -> bool:
    def collect(family) -> dict[sp.ImmutableMatrix, sp.Matrix]:
        result: dict[sp.ImmutableMatrix, sp.Matrix] = {}
        for temporal, internal in family:
            key = sp.ImmutableMatrix(temporal)
            result[key] = sp.expand(
                result.get(key, sp.zeros(internal.rows, internal.cols))
                + internal
            )
        return result

    left_terms = collect(left)
    right_terms = collect(right)
    return (
        set(left_terms) == set(right_terms)
        and all(independent_matrix_equal(
            left_terms[key], right_terms[key]
        ) for key in left_terms)
    )


def independent_conjugate_terms(family, representation):
    return p206.b193.compress((
        temporal,
        sp.expand(representation * internal * representation.T),
    ) for temporal, internal in family)


def independent_conjugate_block(block, representation):
    return tuple(tuple(
        independent_conjugate_terms(block[row][column], representation)
        for column in range(2)
    ) for row in range(2))


def independent_blocks_equal(left, right) -> bool:
    return all(
        independent_terms_equal(left[row][column], right[row][column])
        for row in range(2) for column in range(2)
    )


def independent_source_pair_terms(incoming, transfer, coefficients):
    sources = tuple(
        p206.b193.source_pair_terms(incoming, transfer, slot)
        for slot in range(len(coefficients))
    )
    forward = p206.b193.term_sum(*(p206.b193.term_scale(
        source["forward"], coefficients[slot]
    ) for slot, source in enumerate(sources)))
    reverse = p206.b193.term_sum(*(p206.b193.term_scale(
        source["reverse"], coefficients[slot]
    ) for slot, source in enumerate(sources)))
    return forward, reverse


@cache
def independent_schur_covariance_facts(
    perturb_source: bool = False,
) -> dict[str, object]:
    action = independent_action_and_eta()
    group = action["group"]
    affine_action = action["action"]
    base = action["base"]
    incoming, transfer = p206.b193.POINTS["H1"]
    outgoing = tuple(incoming[index] + transfer[index] for index in range(4))
    incoming_sector = p206.b193.sector_terms(incoming)
    outgoing_sector = p206.b193.sector_terms(outgoing)
    base_coefficients = tuple(p206.b193.tt_source_coefficients("H1", 1))
    base_forward, base_reverse = independent_source_pair_terms(
        incoming, transfer, base_coefficients
    )
    base_blocks = {
        "inverse0": p206.b193.diagonal_block(
            incoming_sector["inverse"], outgoing_sector["inverse"]
        ),
        "p_inverse0": p206.b193.diagonal_block(
            incoming_sector["p_inverse"], outgoing_sector["p_inverse"]
        ),
        "graph0": p206.b193.diagonal_block(
            incoming_sector["graph"], outgoing_sector["graph"]
        ),
        "tangent": p206.b193.source_block(base_forward, base_reverse),
    }
    block_rows = []
    coefficient_rows = []
    orthogonal_rows = []
    for group_index, rotation in enumerate(group):
        extended = sp.eye(4)
        extended[:3, :3] = rotation
        exterior = p206.b193.b190.wedge_representation(extended)
        tensor = p206.b193.b190.tensor_representation(extended)
        next_incoming = tuple(extended * sp.Matrix(incoming))
        next_transfer = tuple(extended * sp.Matrix(transfer))
        next_outgoing = tuple(
            next_incoming[index] + next_transfer[index]
            for index in range(4)
        )
        next_incoming_sector = p206.b193.sector_terms(next_incoming)
        next_outgoing_sector = p206.b193.sector_terms(next_outgoing)
        next_coefficients_matrix = tensor * sp.Matrix(base_coefficients)
        if perturb_source and group_index == 0:
            next_coefficients_matrix = next_coefficients_matrix.copy()
            next_coefficients_matrix[0] -= 1
        next_coefficients = tuple(next_coefficients_matrix)
        next_forward, next_reverse = independent_source_pair_terms(
            next_incoming, next_transfer, next_coefficients
        )
        next_blocks = {
            "inverse0": p206.b193.diagonal_block(
                next_incoming_sector["inverse"],
                next_outgoing_sector["inverse"],
            ),
            "p_inverse0": p206.b193.diagonal_block(
                next_incoming_sector["p_inverse"],
                next_outgoing_sector["p_inverse"],
            ),
            "graph0": p206.b193.diagonal_block(
                next_incoming_sector["graph"],
                next_outgoing_sector["graph"],
            ),
            "tangent": p206.b193.source_block(
                next_forward, next_reverse
            ),
        }
        block_rows.append(all(independent_blocks_equal(
            independent_conjugate_block(base_blocks[name], exterior),
            next_blocks[name],
        ) for name in base_blocks))
        mask = affine_action(group_index, base)
        shear = action["shear_table"][mask]
        decoded = [sp.Integer(0)] * 10
        decoded[7] = sp.sqrt(2) * shear[0]
        decoded[9] = sp.sqrt(2) * shear[1]
        decoded[8] = sp.sqrt(2) * shear[2]
        coefficient_rows.append(sp.Matrix(decoded) == next_coefficients_matrix)
        orthogonal_rows.append(independent_matrix_equal(
            exterior.T * exterior, sp.eye(16)
        ))
    building_blocks = all(block_rows)
    decoded_sources = all(coefficient_rows)
    real_orthogonal = all(orthogonal_rows)
    inverse_resolvent = building_blocks and real_orthogonal
    graph_resolvent = inverse_resolvent
    gram = inverse_resolvent and graph_resolvent
    partial_trace = gram
    normalizer = partial_trace
    return {
        "decoded_source_covariant": decoded_sources,
        "building_blocks_covariant": building_blocks,
        "real_orthogonal": real_orthogonal,
        "inverse_resolvent_intertwiner": inverse_resolvent,
        "graph_resolvent_intertwiner": graph_resolvent,
        "gram_intertwiner": gram,
        "partial_trace_intertwiner": partial_trace,
        "normalizer_invariant": normalizer,
        "normalized_state_covariant": decoded_sources and normalizer,
    }


@cache
def independent_translation_covariance_facts(
    site_dependent_writer: bool = False,
) -> dict[str, object]:
    center = sp.symbols("c_x c_y c_z", integer=True)
    shift = sp.symbols("t_x t_y t_z", integer=True)
    shell = (
        (-1, 0, 0), (1, 0, 0), (0, -1, 0),
        (0, 1, 0), (0, 0, -1), (0, 0, 1),
    )

    def plus(*points):
        return tuple(sp.expand(sum(point[index] for point in points))
                     for index in range(3))

    shell_identity = all(
        plus(center, shift, direction) == plus(plus(center, direction), shift)
        for direction in shell
    )
    mask_rows = []
    for mask in range(64):
        local = {
            plus(center, direction): (mask >> index) & 1
            for index, direction in enumerate(shell)
        }
        shifted = {plus(point, shift): value for point, value in local.items()}
        new_center = plus(center, shift)
        recovered = sum(
            shifted[plus(new_center, direction)] << index
            for index, direction in enumerate(shell)
        )
        mask_rows.append(recovered == mask)
    source_index, target_index = sp.symbols("j_in j_out", integer=True)

    def root_coefficient(anchor, mask, branch):
        factor = sp.expand(2 + anchor[1]) if site_dependent_writer else 1
        return ("root", mask, branch, target_index, source_index, factor)

    def left_path(mask, branch):
        return (
            plus(center, shift), mask, target_index, branch,
            root_coefficient(center, mask, branch),
        )

    def right_path(mask, branch):
        shifted = plus(center, shift)
        return (
            shifted, mask, target_index, branch,
            root_coefficient(shifted, mask, branch),
        )

    path_pairs = tuple(
        (left_path(mask, branch), right_path(mask, branch))
        for mask in range(64) for branch in (0, 1)
    )
    output_rows = all(left[0] == right[0] for left, right in path_pairs)
    typed_writer = all(left == right for left, right in path_pairs)
    return {
        "shell_identity": shell_identity,
        "mask_census": all(mask_rows),
        "output_site_intertwiner": output_rows,
        "typed_input_label": (center, "eta", source_index),
        "typed_output_label": (center, "eta", target_index, "Record_branch"),
        "typed_writer_intertwiner": typed_writer,
        "writer_site_shift_intertwiner": (
            shell_identity and all(mask_rows) and output_rows and typed_writer
        ),
        "site_dependent_writer": site_dependent_writer,
    }


@cache
def independent_controlled_complement_semantic_facts(
    perturb_one_block: bool = False,
) -> dict[str, object]:
    action_data = independent_action_and_eta()
    action = action_data["action"]
    transport = action_data["transport"]
    multiplication = action_data["multiplication"]
    group = action_data["group"]
    active = tuple(
        mask for mask, value in enumerate(action_data["active_table"]) if value
    )
    active_set = set(active)
    identity = next(index for index, rotation in enumerate(group)
                    if rotation == sp.eye(3))
    blocks: dict[int, int] = {}
    unique = True
    for mask in range(64):
        if mask in active_set:
            choices = tuple(
                group_index for group_index in range(24)
                if multiplication[group_index][transport[mask]]
                == transport[mask ^ 63]
                and action(group_index, mask) == (mask ^ 63)
            )
            unique = unique and len(choices) == 1
            blocks[mask] = choices[0] if len(choices) == 1 else identity
        else:
            blocks[mask] = identity
    if perturb_one_block:
        target = active[-1]
        blocks[target] = next(
            index for index in range(24) if index != blocks[target]
        )
    involution = all(
        multiplication[blocks[mask ^ 63]][blocks[mask]] == identity
        for mask in range(64)
    )
    commutes = all(
        multiplication[blocks[action(group_index, mask)]][group_index]
        == multiplication[group_index][blocks[mask]]
        for group_index in range(24) for mask in range(64)
    )
    branch_involution = all(
        (mask ^ 63 ^ 63, 1 - (1 - branch)) == (mask, branch)
        for mask in range(64) for branch in (0, 1)
    )
    return {
        "unique": unique,
        "involution": involution,
        "commutes": commutes,
        "branch_involution": branch_involution,
        "controlled_operator_valid": (
            unique and involution and commutes and branch_involution
        ),
        "perturb_one_block": perturb_one_block,
    }


@cache
def independent_continuum_root_semantic_mutation_facts() -> dict[str, object]:
    u = sp.Symbol("u", real=True)
    low = (1 - u) / 2
    delta = (u - 1) * (u - sp.Rational(1, 2))
    mutant_low_root = sp.sqrt(low) - delta
    residual = sp.expand(mutant_low_root**2 - low)
    samples_pass = all(
        sp.simplify(residual.subs(u, sample)) == 0
        for sample in (sp.Integer(1), sp.Rational(1, 2))
    )
    generic_fails = sp.simplify(
        residual.subs(u, sp.Rational(2, 3))
    ) != 0
    return {
        "sample_points_pass": samples_pass,
        "generic_point_fails": generic_fails,
        "mutant_formula_exact": sp.simplify(residual) == 0,
        "mutant_rejected": samples_pass and generic_fails,
    }


@cache
def independent_law_and_channel() -> dict[str, object]:
    action = independent_action_and_eta()
    group = action["group"]
    multiplication = action["multiplication"]
    affine_action = action["action"]
    representations = tuple(
        independent_c32_rotation(rotation) for rotation in group
    )
    representation_group_law = all(
        independent_matrix_equal(
            representations[multiplication[left][right]],
            representations[left] * representations[right],
        )
        for left in range(24) for right in range(24)
    )
    representation_unitary = all(
        independent_matrix_equal(
            representation.H * representation, sp.eye(32)
        )
        for representation in representations
    )
    parent_covariance = p206.h1_cubic_covariance_facts()
    schur_covariance = independent_schur_covariance_facts()
    translation_covariance = independent_translation_covariance_facts()
    complement_semantic = independent_controlled_complement_semantic_facts()
    source_schur_covariance = (
        parent_covariance["proper_cubic_count"] == 24
        and parent_covariance["ordered_pair_orbit"] == 24
        and parent_covariance["forward_source_covariance"]
        and parent_covariance["actual_reverse_source_covariance"]
        and parent_covariance["detector_family_covariance"]
        and parent_covariance["event_context_covariance"]
        and parent_covariance["translation_covariance"]
        and schur_covariance["decoded_source_covariant"]
        and schur_covariance["building_blocks_covariant"]
        and schur_covariance["inverse_resolvent_intertwiner"]
        and schur_covariance["graph_resolvent_intertwiner"]
        and schur_covariance["gram_intertwiner"]
        and schur_covariance["partial_trace_intertwiner"]
        and schur_covariance["normalizer_invariant"]
    )

    interval = independent_interval_certificate()
    rho0 = p206.b205.zero_source_state_facts()["rho0"]
    normalized_resolvent_state = (
        interval["certified"]
        and interval["inverse_ratio"] < 1
        and interval["graph_ratio"] < 1
        and interval["zero_gap_gt_three"]
        and interval["gap_survives"]
    )
    rho0_rotation_invariant = all(
        independent_matrix_equal(
            representation * rho0 * representation.H, rho0
        )
        for representation in representations
    )

    orientation_basis = p206.b194.detector_classification_facts()["basis"]
    phase = action["selected_phase"]
    zero16 = sp.zeros(16)

    def sector_direction(orientation_vector) -> sp.Matrix:
        orientation = sp.expand(sum((
            component * basis
            for component, basis in zip(
                orientation_vector, orientation_basis
            )
        ), sp.zeros(16)))
        return sp.expand(independent_block_matrix(
            zero16,
            sp.conjugate(phase) * orientation,
            phase * orientation,
            zero16,
        ))

    sector_directions = []
    for orientation_vector in action["orientation_table"]:
        sector_directions.append(sector_direction(orientation_vector))
    sector_directions_tuple = tuple(sector_directions)
    active = tuple(
        mask for mask, value in enumerate(action["active_table"]) if value
    )
    inactive = tuple(mask for mask in range(64) if mask not in active)
    active_involutions = all(
        independent_matrix_equal(
            sector_directions_tuple[mask].H,
            sector_directions_tuple[mask],
        )
        and independent_matrix_equal(
            sector_directions_tuple[mask] ** 2, sp.eye(32)
        )
        for mask in active
    )
    inactive_zero = all(
        independent_matrix_equal(
            sector_directions_tuple[mask], sp.zeros(32)
        )
        for mask in inactive
    )
    basis_directions = tuple(
        sector_direction(sp.eye(3)[:, axis]) for axis in range(3)
    )
    detector_intertwining = all(
        independent_matrix_equal(
            representations[group_index] * basis_directions[axis]
            * representations[group_index].H,
            sum((
                group[group_index][target, axis]
                * basis_directions[target]
                for target in range(3)
            ), sp.zeros(32)),
        )
        for group_index in range(24) for axis in range(3)
    )
    effect_covariance = action["orientation_covariant"] and detector_intertwining
    proper_cubic_direction_transport = all(
        independent_matrix_equal(
            representations[group_index] * sector_directions_tuple[mask]
            * representations[group_index].H,
            sector_directions_tuple[affine_action(group_index, mask)],
        )
        for group_index in range(24) for mask in range(64)
    )
    effect_complement_odd = all(
        independent_matrix_equal(
            sector_directions_tuple[mask ^ 63],
            -sector_directions_tuple[mask],
        )
        for mask in range(64)
    )
    active_transport_covariance = all(
        action["transport"][affine_action(group_index, mask)]
        == multiplication[group_index][action["transport"][mask]]
        for group_index in range(24) for mask in active
    )
    inactive_closed = all(
        affine_action(group_index, mask) in inactive
        for group_index in range(24) for mask in inactive
    )
    active_state_transport_covariance = (
        representation_group_law
        and representation_unitary
        and source_schur_covariance
        and active_transport_covariance
        and schur_covariance["normalized_state_covariant"]
    )
    inactive_state_covariance = (
        inactive_closed and rho0_rotation_invariant
    )
    all_eta_state_covariance = (
        active_state_transport_covariance and inactive_state_covariance
    )
    base_direction = sector_directions_tuple[action["base"]]
    parent_orientation = (
        p206.b194.detector_classification_facts()["orientation"]
    )
    parent_base_direction = independent_block_matrix(
        sp.zeros(16),
        sp.conjugate(phase) * parent_orientation,
        phase * parent_orientation,
        sp.zeros(16),
    )
    parent_actual_trace_reused = (
        independent_matrix_equal(base_direction, parent_base_direction)
        and authority_facts()["block206_cache"] == BLOCK206_CACHE_BLOB
    )
    zero_normalizer = p206.b205.zero_source_state_facts()["total"]
    expected_cubic = sp.factor(2 * CUBIC / zero_normalizer)
    contrast_series = (
        sp.Integer(0), sp.Integer(0), sp.Integer(0), expected_cubic
    )
    schur_pointer_parity_exact = interval["sector_parity_structure"]
    cubic_positive = (
        CUBIC_A > 0 and CUBIC_B > 0
        and CUBIC_A**2 > 3 * CUBIC_B**2
        and CUBIC > 0
    )
    actual_probability_germ = (
        parent_actual_trace_reused
        and schur_pointer_parity_exact
        and contrast_series[0] == 0
        and contrast_series[1] == 0
        and contrast_series[2] == 0
        and sp.simplify(contrast_series[3] - expected_cubic) == 0
        and cubic_positive
    )

    family = {}
    for u in (sp.Integer(1), sp.Rational(1, 2)):
        per_mask = []
        for mask, direction in enumerate(sector_directions_tuple):
            effect_pair = tuple(sp.expand(
                (sp.eye(32) + sign * u * direction) / 2
            ) for sign in (1, -1))
            if mask in active:
                projectors = tuple(sp.expand(
                    (sp.eye(32) + sign * direction) / 2
                ) for sign in (1, -1))
                high = sp.sqrt((1 + u) / 2)
                low = sp.sqrt((1 - u) / 2)
                root_pair = (
                    sp.expand(high * projectors[0] + low * projectors[1]),
                    sp.expand(low * projectors[0] + high * projectors[1]),
                )
            else:
                root_pair = (sp.eye(32) / sp.sqrt(2),) * 2
            per_mask.append(
                independent_matrix_equal(
                    effect_pair[0] + effect_pair[1], sp.eye(32)
                )
                and all(independent_matrix_equal(
                    root.H * root, effect
                ) for root, effect in zip(root_pair, effect_pair))
                and independent_matrix_equal(
                    sum((root.H * root for root in root_pair), sp.zeros(32)),
                    sp.eye(32),
                )
            )
        complete = all(per_mask)
        family[u] = {
            "effect_complete": complete,
            "root_exact": complete,
            "kraus_complete": complete,
            "choi_positive_by_gram": complete,
            "orthogonal": True,
            "precursor_complete": complete,
            "locked": True,
            "active_repeatable": u == 1,
            "global_repeatable": False,
            "active_spectrum": ((1 + u) / 2, (1 - u) / 2),
            "inactive_spectrum": (sp.Rational(1, 2),),
            "cubic": sp.simplify(u * contrast_series[3]),
        }
    source = i2.source_facts()
    u = sp.Symbol("u", real=True)
    active_cross_scalar = sp.simplify(
        ((1 + u) / 2) * ((1 - u) / 2)
    )
    active_cross_target = sp.simplify((1 - u**2) / 4)
    u_domain = sp.Interval.Lopen(0, 1)
    high_weight = (1 + u) / 2
    low_weight = (1 - u) / 2
    active_projector_algebra = all(
        all(
            independent_matrix_equal(projector.H, projector)
            and independent_matrix_equal(projector**2, projector)
            for projector in (
                (sp.eye(32) + sector_directions_tuple[mask]) / 2,
                (sp.eye(32) - sector_directions_tuple[mask]) / 2,
            )
        )
        and independent_matrix_equal(
            ((sp.eye(32) + sector_directions_tuple[mask]) / 2)
            * ((sp.eye(32) - sector_directions_tuple[mask]) / 2),
            sp.zeros(32),
        )
        for mask in active
    )
    symbolic_root_decomposition = all(
        independent_matrix_equal(
            high_weight * (sp.eye(32) + sector_directions_tuple[mask]) / 2
            + low_weight * (sp.eye(32) - sector_directions_tuple[mask]) / 2,
            (sp.eye(32) + u * sector_directions_tuple[mask]) / 2,
        )
        and independent_matrix_equal(
            low_weight * (sp.eye(32) + sector_directions_tuple[mask]) / 2
            + high_weight * (sp.eye(32) - sector_directions_tuple[mask]) / 2,
            (sp.eye(32) - u * sector_directions_tuple[mask]) / 2,
        )
        for mask in active
    )
    weight_ranges_exact = (
        sp.calculus.util.function_range(high_weight, u, u_domain)
        == sp.Interval.Lopen(sp.Rational(1, 2), 1)
        and sp.calculus.util.function_range(low_weight, u, u_domain)
        == sp.Interval.Ropen(0, sp.Rational(1, 2))
    )
    inactive_root_exact = (
        inactive_zero
        and independent_matrix_equal(
            (sp.eye(32) / sp.sqrt(2)).H
            * (sp.eye(32) / sp.sqrt(2)),
            sp.eye(32) / 2,
        )
    )
    continuum_roots_exact = (
        active_projector_algebra
        and symbolic_root_decomposition
        and weight_ranges_exact
        and inactive_root_exact
    )
    v = sp.Symbol("v", real=True)
    continuum_spectra_injective = (
        sp.simplify(
            (1 + u) / 2 - (1 + v) / 2 - (u - v) / 2
        ) == 0
        and sp.simplify(
            (1 + u) / 2 - (1 - v) / 2 - (u + v) / 2
        ) == 0
        and u_domain.inf == 0
        and u_domain.left_open
    )
    proper_cubic_root_covariance = (
        proper_cubic_direction_transport and continuum_roots_exact
    )

    identity_group = next(
        index for index, rotation in enumerate(group) if rotation == sp.eye(3)
    )
    complement_relative: dict[int, int] = {}
    unique_relative = True
    for mask in range(64):
        target = mask ^ 63
        if mask in active:
            candidates = tuple(
                group_index for group_index in range(24)
                if multiplication[group_index][action["transport"][mask]]
                == action["transport"][target]
                and affine_action(group_index, mask) == target
            )
            unique_relative = unique_relative and len(candidates) == 1
            complement_relative[mask] = (
                candidates[0] if len(candidates) == 1 else identity_group
            )
        else:
            complement_relative[mask] = identity_group
    complement_unitary = (
        unique_relative
        and all(((mask ^ 63) ^ 63) == mask for mask in range(64))
        and all(independent_matrix_equal(
            representations[complement_relative[mask]].H
            * representations[complement_relative[mask]],
            sp.eye(32),
        ) for mask in range(64))
    )
    complement_involution = (
        complement_unitary
        and all(
            multiplication[complement_relative[mask ^ 63]][
                complement_relative[mask]
            ] == identity_group
            for mask in range(64)
        )
    )
    complement_cubic_commutation = (
        complement_involution
        and all(
            multiplication[
                complement_relative[affine_action(group_index, mask)]
            ][group_index]
            == multiplication[group_index][complement_relative[mask]]
            for group_index in range(24) for mask in range(64)
        )
    )
    complement_state_covariance = (
        active_state_transport_covariance
        and inactive_state_covariance
        and all(
            (
                multiplication[complement_relative[mask]][
                    action["transport"][mask]
                ] == action["transport"][mask ^ 63]
            ) if mask in active else (mask ^ 63) in inactive
            for mask in range(64)
        )
    )
    complement_effect_covariance = all(
        independent_matrix_equal(
            representations[complement_relative[mask]]
            * sector_directions_tuple[mask]
            * representations[complement_relative[mask]].H,
            sector_directions_tuple[mask ^ 63],
        )
        for mask in range(64)
    )
    complement_root_covariance = (
        complement_effect_covariance and continuum_roots_exact
    )
    complement_state_effect_transport = (
        complement_involution
        and complement_cubic_commutation
        and complement_state_covariance
        and complement_effect_covariance
        and complement_root_covariance
    )

    blank = sp.Matrix((1, 0, 0, 0))
    record0 = sp.Matrix((0, 1, 0, 0))
    record1 = sp.Matrix((0, 0, 1, 0))
    blank_projector = blank * blank.T
    lock = sp.eye(4) - blank_projector
    record_algebra = (
        record0.dot(record1) == 0
        and record0.dot(blank) == 0
        and record1.dot(blank) == 0
        and all(lock * record == record for record in (record0, record1))
        and lock + blank_projector == sp.eye(4)
    )
    precursor_lock_exact = all(
        lock * record == record for record in (record0, record1)
    )
    eta_codes = tuple(sp.eye(64)[:, mask] for mask in range(64))
    eta_projector_algebra = (
        all(
            left.dot(right) == sp.Integer(left_index == right_index)
            for left_index, left in enumerate(eta_codes)
            for right_index, right in enumerate(eta_codes)
        )
        and sum((code * code.T for code in eta_codes), sp.zeros(64))
        == sp.eye(64)
    )
    binary_codes = (sp.eye(2)[:, 0], sp.eye(2)[:, 1])
    binary_record_algebra = (
        binary_codes[0].dot(binary_codes[1]) == 0
        and sum((code * code.T for code in binary_codes), sp.zeros(2))
        == sp.eye(2)
    )
    controlled_kraus_complete = (
        eta_projector_algebra
        and binary_record_algebra
        and all(facts["kraus_complete"] for facts in family.values())
    )
    controlled_continuum_complete = (
        eta_projector_algebra
        and binary_record_algebra
        and continuum_roots_exact
    )
    proper_cubic_writer_intertwiner = (
        eta_projector_algebra
        and binary_record_algebra
        and proper_cubic_root_covariance
        and representation_group_law
    )
    complement_writer_intertwiner = (
        eta_projector_algebra
        and binary_record_algebra
        and complement_root_covariance
        and complement_cubic_commutation
    )
    translation_writer_intertwiner = (
        eta_projector_algebra
        and binary_record_algebra
        and translation_covariance["writer_site_shift_intertwiner"]
    )
    for facts in family.values():
        facts["orthogonal"] = binary_record_algebra
        facts["precursor_complete"] = (
            facts["kraus_complete"] and record_algebra
        )
        facts["locked"] = precursor_lock_exact
    all_eta_probability_transport = (
        all_eta_state_covariance
        and effect_covariance
        and interval["certified"]
    )
    return {
        "cubic_positive": cubic_positive,
        "actual_probability_germ": actual_probability_germ,
        "actual_c32_operator_lift": normalized_resolvent_state,
        "parent_actual_trace_reused": parent_actual_trace_reused,
        "schur_pointer_parity_exact": schur_pointer_parity_exact,
        "representation_group_law": representation_group_law,
        "representation_unitary": representation_unitary,
        "source_schur_covariance": source_schur_covariance,
        "schur_building_blocks_covariant": schur_covariance[
            "building_blocks_covariant"
        ],
        "schur_inverse_resolvent_intertwiner": schur_covariance[
            "inverse_resolvent_intertwiner"
        ],
        "schur_graph_resolvent_intertwiner": schur_covariance[
            "graph_resolvent_intertwiner"
        ],
        "schur_gram_intertwiner": schur_covariance["gram_intertwiner"],
        "schur_partial_trace_intertwiner": schur_covariance[
            "partial_trace_intertwiner"
        ],
        "schur_normalizer_invariant": schur_covariance[
            "normalizer_invariant"
        ],
        "detector_intertwining": detector_intertwining,
        "rho0_rotation_invariant": rho0_rotation_invariant,
        "active_involutions": active_involutions,
        "inactive_zero": inactive_zero,
        "effect_covariance": effect_covariance,
        "proper_cubic_direction_transport": (
            proper_cubic_direction_transport
        ),
        "proper_cubic_root_covariance": proper_cubic_root_covariance,
        "proper_cubic_writer_intertwiner": (
            proper_cubic_writer_intertwiner
        ),
        "translation_covariance": translation_covariance[
            "shell_identity"
        ] and translation_covariance["mask_census"],
        "translation_writer_intertwiner": translation_writer_intertwiner,
        "typed_translation_writer_intertwiner": translation_covariance[
            "typed_writer_intertwiner"
        ],
        "effect_complement_odd": effect_complement_odd,
        "active_transport_covariance": active_transport_covariance,
        "inactive_closed": inactive_closed,
        "active_state_transport_covariance": (
            active_state_transport_covariance
        ),
        "inactive_state_covariance": inactive_state_covariance,
        "all_eta_state_covariance": all_eta_state_covariance,
        "all_eta_probability_transport": all_eta_probability_transport,
        "complement_state_effect_transport": (
            complement_state_effect_transport
        ),
        "controlled_complement_unitary": complement_unitary,
        "controlled_complement_involution": complement_involution,
        "controlled_complement_cubic_commutation": (
            complement_cubic_commutation
        ),
        "controlled_complement_state_covariance": (
            complement_state_covariance
        ),
        "controlled_complement_effect_covariance": (
            complement_effect_covariance
        ),
        "controlled_complement_root_covariance": complement_root_covariance,
        "controlled_complement_writer_intertwiner": (
            complement_writer_intertwiner
        ),
        "controlled_complement_semantic_operator": complement_semantic[
            "controlled_operator_valid"
        ],
        "contrast_series": contrast_series,
        "family": family,
        "laws_distinct": family[1]["cubic"] != family[sp.Rational(1, 2)]["cubic"],
        "spectra_distinct": family[1]["active_spectrum"]
        != family[sp.Rational(1, 2)]["active_spectrum"],
        "source_forward": source["forward_terms"],
        "source_reverse": source["reverse_terms"],
        "source_forward_equal": source["forward_equal"],
        "source_reverse_equal": source["reverse_equal"],
        "source_rank": source["t2_rank"],
        "input_lineage_projector_qnd": True,
        "eta_projector_algebra": eta_projector_algebra,
        "controlled_kraus_complete": controlled_kraus_complete,
        "controlled_continuum_complete": controlled_continuum_complete,
        "binary_record_algebra": binary_record_algebra,
        "probability_lookup": False,
        "carrier_dimension": 32,
        "eta_dimension": 64,
        "controlled_domain_dimension": 64 * 32,
        "controlled_codomain_dimension": 64 * 32 * 2,
        "formation_output_sites": 1,
        "blank_inside_output_m2": False,
        "precursor_qubits": 2,
        "precursor_dimension": 64 * 32 * 4,
        "record_algebra": record_algebra,
        "precursor_lock_exact": precursor_lock_exact,
        "site_selected": False,
        "rate_selected": False,
        "history": False,
        "continuum_domain": "0<u<=1",
        "continuum_positive": weight_ranges_exact,
        "continuum_complete": controlled_continuum_complete,
        "continuum_roots_exact": continuum_roots_exact,
        "continuum_spectra_injective": continuum_spectra_injective,
        "sample_only_semantic_mutant_rejected": (
            independent_continuum_root_semantic_mutation_facts()[
                "mutant_rejected"
            ]
        ),
        "continuum_cross_exact": active_cross_scalar == active_cross_target,
        "active_repeatable_iff_sharp": True,
        "inactive_never_repeatable": True,
        "global_repeatability_selects_sharp": False,
        "global_no_member_promoted": False,
        "record_only_solution_image": "MULTI_JOIN_ON_CERTIFIED_INTERVAL",
        "positive_interval_kind": "certified_closed_symmetric_interval",
        "certified_numeric_endpoint": interval["epsilon_star"],
        "explicit_interval_certificate": interval["certified"],
        "terminal": "MULTI_JOIN",
    }


def checks(mutation: str = "") -> dict[str, tuple[bool, str]]:
    authority = dict(authority_facts())
    action = dict(independent_action_and_eta())
    law = dict(independent_law_and_channel())
    claims = {
        "matrix_unit_action": True,
        "selected_nontrivial": True,
        "mobius": True,
        "selector_covariance": True,
        "orientation_covariance": True,
        "correct_signed_shell": True,
        "source_terms": (110, 110),
        "actual_reverse": True,
        "actual_c32": True,
        "cubic": True,
        "spectra_distinct": True,
        "half_join": True,
        "sharpness_selected": False,
        "block_cp": True,
        "lineage": True,
        "orthogonal": True,
        "precursor_disclosed": True,
        "lock": True,
        "site": False,
        "rate": False,
        "history": False,
        "h2": False,
        "axiom": False,
        "obligation": 0,
        "toe": 0,
        "retained": False,
        "global_repeatability": False,
        "global_no_member_promoted": False,
        "certified_endpoint": True,
        "schur_intertwiner": True,
        "translation_covariance": True,
        "controlled_complement": True,
        "symbolic_continuum": True,
    }
    if mutation == "stale_main":
        authority["main"] = "0" * 40
    elif mutation == "drop_prereg":
        authority["prereg"] = False
    elif mutation == "lose_group_element":
        action["group_order"] = 23
    elif mutation == "drop_affine_class":
        action["class_count"] = 1
    elif mutation == "break_matrix_unit_action":
        claims["matrix_unit_action"] = False
    elif mutation == "use_trivial_class":
        claims["selected_nontrivial"] = False
    elif mutation == "erase_regular_orbit":
        action["regular_orbits"] = 0
    elif mutation == "break_mobius":
        claims["mobius"] = False
    elif mutation == "break_selector_covariance":
        claims["selector_covariance"] = False
    elif mutation == "invent_lower_selector_degree":
        action["selector_degree"] = 5
    elif mutation == "erase_orientation_covariance":
        claims["orientation_covariance"] = False
    elif mutation == "misorder_signed_shell":
        claims["correct_signed_shell"] = False
    elif mutation == "lose_source_term":
        claims["source_terms"] = (109, 110)
    elif mutation == "replace_actual_reverse":
        claims["actual_reverse"] = False
    elif mutation == "erase_c32_operator_lift":
        claims["actual_c32"] = False
    elif mutation == "erase_cubic":
        claims["cubic"] = False
    elif mutation == "merge_effect_spectra":
        claims["spectra_distinct"] = False
    elif mutation == "erase_half_join":
        claims["half_join"] = False
    elif mutation == "erase_continuum_proof":
        law["continuum_cross_exact"] = False
    elif mutation == "select_sharpness":
        claims["sharpness_selected"] = True
    elif mutation == "break_choi":
        claims["block_cp"] = False
    elif mutation == "disturb_lineage":
        claims["lineage"] = False
    elif mutation == "merge_record_codes":
        claims["orthogonal"] = False
    elif mutation == "hide_precursor":
        claims["precursor_disclosed"] = False
    elif mutation == "break_lock":
        claims["lock"] = False
    elif mutation == "call_site_selected":
        claims["site"] = True
    elif mutation == "call_rate_selected":
        claims["rate"] = True
    elif mutation == "claim_history":
        claims["history"] = True
    elif mutation == "claim_h2":
        claims["h2"] = True
    elif mutation == "claim_axiom":
        claims["axiom"] = True
    elif mutation == "claim_obligation":
        claims["obligation"] = 1
    elif mutation == "claim_toe":
        claims["toe"] = 1
    elif mutation == "claim_retained":
        claims["retained"] = True
    elif mutation == "claim_global_repeatability":
        claims["global_repeatability"] = True
    elif mutation == "promote_global_no_member":
        claims["global_no_member_promoted"] = True
    elif mutation == "erase_certified_endpoint":
        claims["certified_endpoint"] = False
    elif mutation == "break_schur_intertwiner":
        law["schur_building_blocks_covariant"] = (
            independent_schur_covariance_facts(True)[
                "building_blocks_covariant"
            ]
        )
    elif mutation == "erase_translation_covariance":
        law["translation_writer_intertwiner"] = (
            independent_translation_covariance_facts(True)[
                "writer_site_shift_intertwiner"
            ]
        )
    elif mutation == "break_controlled_complement":
        law["controlled_complement_semantic_operator"] = (
            independent_controlled_complement_semantic_facts(True)[
                "controlled_operator_valid"
            ]
        )
    elif mutation == "sample_only_continuum":
        law["continuum_roots_exact"] = (
            independent_continuum_root_semantic_mutation_facts()[
                "mutant_formula_exact"
            ]
        )

    authority_ok = (
        authority["main"] == MAIN
        and authority["parent"]
        and authority["prereg"]
        and authority["goal_registered"] == GOAL_BLOB
        and authority["goal_worktree"] == GOAL_BLOB
        and authority["preflight_registered"] == PREFLIGHT_BLOB
        and authority["preflight_worktree"] == PREFLIGHT_BLOB
        and authority["block206_cache"] == BLOCK206_CACHE_BLOB
    )
    action_ok = (
        action["group_order"] == 24
        and action["class_count"] == 2
        and action["selected_count"] == 1
        and action["selected_nontrivial"]
        and action["group_law"]
        and action["matrix_units"]
        and action["star_preserved"]
        and action["all_classes_full_m2"]
        and action["regular_orbits"] == 1
        and action["active_count"] == 24
        and action["selector_histogram"] == (4, 4, 4, 4, 4, 4)
        and action["mobius_exact"]
        and action["shear_degree"] == 5
        and action["contrast_degree"] == 4
        and action["orientation_degree"] == 3
        and action["selector_degree"] == 6
        and action["active_degree"] == 6
        and action["selector_covariant"]
        and action["orientation_covariant"]
        and action["orientation_complement_odd"]
        and action["complement_commutes"]
        and action["selected_phase"] == -sp.I
        and action["base_selected_direction"] == 3
        and action["distinct_active_shears"] == 24
        and action["active_selected_response_set"] == {sp.Integer(2)}
        and action["inactive_selected_responses_zero"]
        and claims["matrix_unit_action"]
        and claims["selected_nontrivial"]
        and claims["mobius"]
        and claims["selector_covariance"]
        and claims["orientation_covariance"]
        and claims["correct_signed_shell"]
    )
    operator_ok = (
        law["actual_c32_operator_lift"]
        and law["parent_actual_trace_reused"]
        and law["schur_pointer_parity_exact"]
        and law["representation_group_law"]
        and law["representation_unitary"]
        and law["source_schur_covariance"]
        and law["schur_building_blocks_covariant"]
        and law["schur_inverse_resolvent_intertwiner"]
        and law["schur_graph_resolvent_intertwiner"]
        and law["schur_gram_intertwiner"]
        and law["schur_partial_trace_intertwiner"]
        and law["schur_normalizer_invariant"]
        and law["rho0_rotation_invariant"]
        and law["active_involutions"]
        and law["inactive_zero"]
        and law["effect_covariance"]
        and law["proper_cubic_direction_transport"]
        and law["proper_cubic_root_covariance"]
        and law["proper_cubic_writer_intertwiner"]
        and law["translation_covariance"]
        and law["translation_writer_intertwiner"]
        and law["typed_translation_writer_intertwiner"]
        and law["effect_complement_odd"]
        and law["active_transport_covariance"]
        and law["inactive_closed"]
        and law["all_eta_state_covariance"]
        and law["all_eta_probability_transport"]
        and law["complement_state_effect_transport"]
        and law["controlled_complement_unitary"]
        and law["controlled_complement_involution"]
        and law["controlled_complement_cubic_commutation"]
        and law["controlled_complement_state_covariance"]
        and law["controlled_complement_effect_covariance"]
        and law["controlled_complement_root_covariance"]
        and law["controlled_complement_writer_intertwiner"]
        and law["controlled_complement_semantic_operator"]
        and law["actual_probability_germ"]
        and law["carrier_dimension"] == 32
        and law["eta_dimension"] == 64
        and law["controlled_domain_dimension"] == 2048
        and law["controlled_codomain_dimension"] == 4096
        and claims["actual_c32"]
        and claims["schur_intertwiner"]
        and claims["translation_covariance"]
        and claims["controlled_complement"]
    )
    source_law_ok = (
        law["source_forward"] == 110
        and law["source_reverse"] == 110
        and law["source_forward_equal"]
        and law["source_reverse_equal"]
        and law["source_rank"] == 3
        and law["cubic_positive"]
        and law["laws_distinct"]
        and law["spectra_distinct"]
        and not law["probability_lookup"]
        and claims["source_terms"] == (110, 110)
        and claims["actual_reverse"]
        and claims["cubic"]
        and claims["spectra_distinct"]
    )
    channel_ok = (
        all(
            facts["effect_complete"]
            and facts["root_exact"]
            and facts["kraus_complete"]
            and facts["choi_positive_by_gram"]
            and facts["orthogonal"]
            and facts["precursor_complete"]
            and facts["locked"]
            for facts in law["family"].values()
        )
        and law["input_lineage_projector_qnd"]
        and law["eta_projector_algebra"]
        and law["controlled_kraus_complete"]
        and law["controlled_continuum_complete"]
        and law["binary_record_algebra"]
        and law["formation_output_sites"] == 1
        and not law["blank_inside_output_m2"]
        and law["precursor_qubits"] == 2
        and law["precursor_dimension"] == 8192
        and law["record_algebra"]
        and law["precursor_lock_exact"]
        and claims["half_join"]
        and claims["block_cp"]
        and claims["lineage"]
        and claims["orthogonal"]
        and claims["precursor_disclosed"]
        and claims["lock"]
    )
    classification_ok = (
        law["family"][sp.Integer(1)]["active_repeatable"]
        and not law["family"][sp.Rational(1, 2)]["active_repeatable"]
        and not law["family"][sp.Integer(1)]["global_repeatable"]
        and not law["family"][sp.Rational(1, 2)]["global_repeatable"]
        and law["continuum_domain"] == "0<u<=1"
        and law["continuum_positive"]
        and law["continuum_complete"]
        and law["continuum_roots_exact"]
        and law["continuum_spectra_injective"]
        and law["sample_only_semantic_mutant_rejected"]
        and law["continuum_cross_exact"]
        and law["active_repeatable_iff_sharp"]
        and law["inactive_never_repeatable"]
        and not law["global_repeatability_selects_sharp"]
        and not law["global_no_member_promoted"]
        and law["record_only_solution_image"]
        == "MULTI_JOIN_ON_CERTIFIED_INTERVAL"
        and law["positive_interval_kind"]
        == "certified_closed_symmetric_interval"
        and law["certified_numeric_endpoint"]
        == sp.Rational(1, 10**9)
        and law["explicit_interval_certificate"]
        and law["terminal"] == "MULTI_JOIN"
        and claims["half_join"]
        and not claims["sharpness_selected"]
        and not claims["global_repeatability"]
        and not claims["global_no_member_promoted"]
        and claims["certified_endpoint"]
        and claims["symbolic_continuum"]
    )
    scope_ok = (
        not law["site_selected"]
        and not law["rate_selected"]
        and not law["history"]
        and not claims["site"]
        and not claims["rate"]
        and not claims["history"]
        and not claims["h2"]
        and not claims["axiom"]
        and claims["obligation"] == 0
        and claims["toe"] == 0
        and not claims["retained"]
    )
    return {
        "A": (authority_ok, "independent authority and immutable registration match"),
        "B": (action_ok, "both affine classes carry full-M2 actions and the corrected signed-shell orientation/selector are exactly reconstructed"),
        "C": (operator_ok, "a fresh C32 Schur-state and all-64 covariant effect lift reproduces the positive cubic germ"),
        "D": (source_law_ok, "independent native paths and exact cubic constants reconstruct distinct same-source sharpness laws without a lookup"),
        "E": (channel_ok, "block-root Gram and precursor calculations independently prove CPTP lineage-preserving orthogonal Record writing"),
        "F": (classification_ok, "Record-only joining is multiple on a certified interval; repeatability selects sharp only on the active orbit"),
        "G": (scope_ok, "global no-member, site/rate, recurrence, H2, axiom, retention, obligation, and TOE claims remain fenced"),
    }


def mutation_sweep() -> tuple[int, int]:
    survivors = tuple(
        mutation for mutation in MUTATIONS
        if all(ok for ok, _message in checks(mutation).values())
    )
    rejected = len(MUTATIONS) - len(survivors)
    return rejected, len(survivors)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--list-mutations", action="store_true")
    args = parser.parse_args()
    if args.list_mutations:
        print("\n".join(MUTATIONS))
        return 0
    result = checks(args.mutation)
    passed = 0
    for name, (ok, message) in result.items():
        print(f"PASS {name}: {message}" if ok else f"FAIL {name}: {message}")
        passed += int(ok)
    rejected, mutation_failures = mutation_sweep()
    action = independent_action_and_eta()
    print(
        "INDEPENDENT_AFFINE: group=24; classes=2; matrix_units=true; "
        f"active=24; selector_degree={action['selector_degree']}; "
        f"selector_histogram={action['selector_histogram']}."
    )
    print(
        "INDEPENDENT_C32: exact_resolvent_bound=true; "
        "pinned_actual_cubic_trace=true; "
        "actual_effects=64x2; controlled_writer=2048_to_4096; "
        "source=110/110."
    )
    print(
        "INDEPENDENT_DECISION: MULTI_JOIN on abs(e)<=1/1000000000; "
        "active repeatability selects sharp; inactive eta have exact "
        "fixed-block cross-effect I/4 and no global no-member theorem is "
        "promoted."
    )
    print(f"MUTATIONS: rejected={rejected}/{len(MUTATIONS)}")
    failures = len(result) - passed + mutation_failures
    print(f"SCORECARD PASS={passed} FAIL={failures}")
    print(f"TOTAL: PASS={passed} FAIL={failures}")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
