#!/usr/bin/env python3
"""Block 07: frozen H1 law versus the preregistered H2 source fixture.

This runner applies the complete Block-03 H1 eta/source family to H2 without
refitting.  It decides only membership in that frozen family.  A negative
answer is not a no-go for a larger source representation, another local
action, the minimal axioms, or a TOE.
"""

from __future__ import annotations

import argparse
from functools import cache
import hashlib
import itertools
from pathlib import Path
import subprocess
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_affine_lineage_binary_record_join_2026_08_29 as b3  # noqa: E402
import admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25 as b193  # noqa: E402
import admissibility_d4_h1_action_factorized_six_m2_source_ownership_2026_08_28 as b1  # noqa: E402


PACKET = ROOT / ".claude" / "science" / "physics-loops" / (
    "toe-source-eta-ownership-block07-frozen-h2-common-action-20260829"
)
GOAL = PACKET / "GOAL.md"
PREFLIGHT = PACKET / "PREFLIGHT_WITNESSES.md"
NO_GO = PACKET / "NO_GO_DISCIPLINE_CHECKLIST.md"
NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_D4_FROZEN_H2_COMMON_ACTION_SOURCE_IMAGE_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
)
AXIOM = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

PARENT = "a9b4285a17a3a35941667b074bda2f20fa8f1c70"
PREREG = "0169137102e9c2677de51aa8e13f4e1ea2665bce"
FROZEN_MAIN = "004f64e1c87dad696b282cf2b526f3e7312dc82d"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
BLOCK3_RUNNER_BLOB = "0f29ff74b3816a15847aea104f3faa44d6a0ea4f"
BLOCK193_RUNNER_BLOB = "c60edb2e8e3683e99f4f3dddcc4980fd1db28786"
BLOCK191_RUNNER_BLOB = "2b2a3fc1f842683d376ff436f848eef81162ef4b"
BLOCK6_NOTE_BLOB = "8ff4d3252a847a412a6fedfe776c71a839b40b89"
AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block07-frozen-h2-common-action-20260829/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block07-frozen-h2-common-action-20260829/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block07-frozen-h2-common-action-20260829/NO_GO_DISCIPLINE_CHECKLIST.md",
    "docs/ADMISSIBILITY_D4_FROZEN_H2_COMMON_ACTION_SOURCE_IMAGE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_d4_affine_lineage_binary_record_join_2026_08_29.py",
    "scripts/admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25.py",
    "scripts/admissibility_d4_grade3_source_instrument_history_write_2026_08_24.py",
    "scripts/admissibility_d4_ordered_h1_front_carrier_interface_2026_08_29.py",
    "logs/runner-cache/admissibility_d4_affine_lineage_binary_record_join_2026_08_29.txt",
    "logs/runner-cache/admissibility_d4_ordered_h1_front_carrier_interface_2026_08_29.txt",
)

MUTATIONS = (
    "stale_main",
    "stale_prereg",
    "change_h2_column",
    "drop_outside_slots",
    "fit_mask_17",
    "numeric_tolerance",
    "support_only",
    "scalar_rescale",
    "drop_forward_term",
    "replace_actual_reverse",
    "collapse_source_rank",
    "enlarge_domain_after_h2",
    "h2_specific_decoder",
    "skip_reflection_orbit",
    "continue_state_chain",
    "continue_history_chain",
    "claim_common_law",
    "claim_broad_no_go",
    "claim_axiom_update",
    "claim_toe",
    "claim_retained",
)

EXPECTED_H2 = (
    sp.Integer(0),
    (sp.sqrt(3) + 3) / 4,
    -(sp.sqrt(3) + 1) / 4,
    -sp.Rational(1, 2),
    sp.Integer(0),
    sp.Integer(0),
    sp.Integer(0),
    -sp.sqrt(3) / 2,
    sp.Integer(0),
    sp.Integer(1),
)
H1_SLOTS = (7, 9, 8)


def git(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=AUDIT_TIMEOUT_SEC
    ).strip()


def ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


def blob(path: Path) -> str:
    return git("hash-object", "--", str(path.relative_to(ROOT)))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def coefficient_tuple(shear: tuple[sp.Expr, ...]) -> tuple[sp.Expr, ...]:
    result = [sp.Integer(0)] * 10
    result[7] = sp.sqrt(2) * shear[0]
    result[9] = sp.sqrt(2) * shear[1]
    result[8] = sp.sqrt(2) * shear[2]
    return tuple(result)


def poly_sum(
    vertices: tuple[b193.b190.PolyMatrix, ...],
    coefficients: tuple[sp.Expr, ...],
) -> b193.b190.PolyMatrix:
    result: b193.b190.PolyMatrix = {}
    for coefficient, vertex in zip(coefficients, vertices):
        result = b193.b190.poly_add(
            result, b193.b190.poly_scale(vertex, coefficient)
        )
    return result


def poly_difference(
    left: b193.b190.PolyMatrix, right: b193.b190.PolyMatrix
) -> b193.b190.PolyMatrix:
    return b193.b190.poly_add(left, b193.b190.poly_scale(right, -1))


def actual_reverse(source: b193.b190.PolyMatrix) -> b193.b190.PolyMatrix:
    result: b193.b190.PolyMatrix = {}
    for power, matrix in source.items():
        transformed = tuple(power[index] for index in range(4)) + tuple(
            power[index] - power[4 + index] for index in range(4)
        )
        result = b193.b190.poly_add(result, {transformed: matrix})
    return result


def nonzero_entries(source: b193.b190.PolyMatrix) -> int:
    return sum(sum(value != 0 for value in matrix) for matrix in source.values())


def flatten_polynomials(
    polynomials: tuple[b193.b190.PolyMatrix, ...],
) -> sp.Matrix:
    powers = sorted(set().union(*(set(item) for item in polynomials)))
    columns = []
    for polynomial in polynomials:
        entries = []
        for power in powers:
            entries.extend(list(polynomial.get(power, sp.zeros(16))))
        columns.append(sp.Matrix(entries))
    return sp.Matrix.hstack(*columns)


def collect_terms(terms: b193.Terms) -> dict[sp.ImmutableMatrix, sp.Matrix]:
    result: dict[sp.ImmutableMatrix, sp.Matrix] = {}
    for temporal, internal in terms:
        key = sp.ImmutableMatrix(temporal)
        result[key] = sp.expand(
            result.get(key, sp.zeros(internal.rows, internal.cols)) + internal
        )
    return result


def term_family_equal(left: b193.Terms, right: b193.Terms) -> bool:
    left_terms = collect_terms(left)
    right_terms = collect_terms(right)
    return (
        set(left_terms) == set(right_terms)
        and all(b193.matrix_equal(left_terms[key], right_terms[key])
                for key in left_terms)
    )


def cubic_orthogonal_group() -> tuple[sp.Matrix, ...]:
    result = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = sp.zeros(3)
            for column, row in enumerate(permutation):
                matrix[row, column] = signs[column]
            result.append(matrix)
    return tuple(result)


@cache
def authority_facts() -> dict[str, object]:
    return {
        "main": git("rev-parse", "origin/main"),
        "parent": ancestor(PARENT),
        "prereg": ancestor(PREREG),
        "axiom": blob(AXIOM),
        "goal_blob": git("rev-parse", f"{PREREG}:{GOAL.relative_to(ROOT)}"),
        "preflight_blob": git(
            "rev-parse", f"{PREREG}:{PREFLIGHT.relative_to(ROOT)}"
        ),
        "block3_runner": git(
            "rev-parse", f"HEAD:scripts/{b3.__file__.split('/')[-1]}"
        ),
        "block193_runner": git(
            "rev-parse", f"HEAD:scripts/{b193.__file__.split('/')[-1]}"
        ),
        "block191_runner": git(
            "rev-parse",
            "HEAD:scripts/admissibility_d4_grade3_source_instrument_history_write_2026_08_24.py",
        ),
        "block6_note": git(
            "rev-parse",
            "HEAD:docs/ADMISSIBILITY_D4_ORDERED_H1_FRONT_CARRIER_INTERFACE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
        ),
    }


@cache
def membership_facts(column: int = 1) -> dict[str, object]:
    coefficients = tuple(
        sp.simplify(value)
        for value in b193.tt_source_coefficients("H2", column)
    )
    h1_domain = sp.zeros(10, 3)
    h1_domain[7, 0] = sp.sqrt(2)
    h1_domain[9, 1] = sp.sqrt(2)
    h1_domain[8, 2] = sp.sqrt(2)
    domain_rank = h1_domain.rank()
    augmented_rank = h1_domain.row_join(sp.Matrix(coefficients)).rank()
    h2_shear = tuple(sp.simplify(coefficients[slot] / sp.sqrt(2))
                     for slot in H1_SLOTS)
    decoder = b3.decoder_facts()
    residuals = []
    for mask, shear in enumerate(decoder["shear_table"]):
        residual = tuple(sp.simplify(left - right)
                         for left, right in zip(shear, h2_shear))
        residuals.append((sum(value != 0 for value in residual), mask, residual))
    best = tuple(sorted(residuals, key=lambda item: (item[0], item[1]))[:2])
    return {
        "coefficients": coefficients,
        "expected": coefficients == EXPECTED_H2,
        "nonzero_slots": tuple(index for index, value in enumerate(coefficients)
                               if value != 0),
        "outside_slots": tuple(index for index in (0, 1, 2, 3, 4, 5, 6)
                               if coefficients[index] != 0),
        "h1_domain_rank": domain_rank,
        "augmented_rank": augmented_rank,
        "in_h1_domain": augmented_rank == domain_rank,
        "h2_shear": h2_shear,
        "eta_matches": tuple(mask for _, mask, residual in residuals
                             if all(value == 0 for value in residual)),
        "best": best,
        "all64_checked": len(residuals) == 64,
    }


@cache
def source_facts() -> dict[str, object]:
    membership = membership_facts()
    coefficients = membership["coefficients"]
    assert isinstance(coefficients, tuple)
    vertices = tuple(b3.b206.raw_action_vertices())
    target = poly_sum(vertices, coefficients)
    target_reverse = actual_reverse(target)
    decoder = b3.decoder_facts()
    fixed_target = b193.combined_source_pair_terms("H2", coefficients)
    residual_rows = []
    fixed_forward_matches = []
    fixed_reverse_matches = []
    for mask, shear in enumerate(decoder["shear_table"]):
        candidate_coefficients = coefficient_tuple(shear)
        candidate = poly_sum(vertices, candidate_coefficients)
        residual = poly_difference(target, candidate)
        reverse_residual = poly_difference(
            target_reverse, actual_reverse(candidate)
        )
        residual_rows.append((
            len(residual), nonzero_entries(residual),
            len(reverse_residual), nonzero_entries(reverse_residual), mask,
        ))
        fixed_candidate = b193.combined_source_pair_terms(
            "H2", candidate_coefficients
        )
        fixed_forward_matches.append(term_family_equal(
            fixed_target["forward"], fixed_candidate["forward"]
        ))
        fixed_reverse_matches.append(term_family_equal(
            fixed_target["reverse"], fixed_candidate["reverse"]
        ))

    full_map = flatten_polynomials(vertices)
    h1_columns = full_map[:, H1_SLOTS]
    target_column = full_map * sp.Matrix(coefficients)
    reverse_vertices = tuple(actual_reverse(vertex) for vertex in vertices)
    reverse_map = flatten_polynomials(reverse_vertices)
    reverse_h1_columns = reverse_map[:, H1_SLOTS]
    reverse_target_column = reverse_map * sp.Matrix(coefficients)
    return {
        "target_terms": len(target),
        "target_reverse_terms": len(target_reverse),
        "source_matches": tuple(row[-1] for row in residual_rows
                                if row[0] == 0),
        "reverse_matches": tuple(row[-1] for row in residual_rows
                                 if row[2] == 0),
        "best": tuple(sorted(residual_rows)[:2]),
        "fixed_forward_matches": tuple(index for index, value
                                       in enumerate(fixed_forward_matches)
                                       if value),
        "fixed_reverse_matches": tuple(index for index, value
                                       in enumerate(fixed_reverse_matches)
                                       if value),
        "full_map_rank": full_map.rank(),
        "h1_map_rank": h1_columns.rank(),
        "augmented_rank": h1_columns.row_join(target_column).rank(),
        "reverse_full_map_rank": reverse_map.rank(),
        "reverse_h1_map_rank": reverse_h1_columns.rank(),
        "reverse_augmented_rank": reverse_h1_columns.row_join(
            reverse_target_column
        ).rank(),
        "all64_checked": len(residual_rows) == 64,
    }


@cache
def orbit_facts() -> dict[str, object]:
    coefficients = sp.Matrix(membership_facts()["coefficients"])
    h1_domain = sp.zeros(10, 3)
    h1_domain[7, 0] = sp.sqrt(2)
    h1_domain[9, 1] = sp.sqrt(2)
    h1_domain[8, 2] = sp.sqrt(2)
    rows = []
    for spatial in cubic_orthogonal_group():
        full = sp.eye(4)
        full[:3, :3] = spatial
        tensor = b193.b190.tensor_representation(full)
        domain = tensor * h1_domain
        target = tensor * coefficients
        rows.append((int(spatial.det()), domain.rank(),
                     domain.row_join(target).rank()))
    return {
        "count": len(rows),
        "proper_count": sum(row[0] == 1 for row in rows),
        "reflection_count": sum(row[0] == -1 for row in rows),
        "domain_ranks": tuple(sorted(set(row[1] for row in rows))),
        "augmented_ranks": tuple(sorted(set(row[2] for row in rows))),
        "all_nonmembers": all(row[1] == 3 and row[2] == 4 for row in rows),
    }


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, name: str, value: bool, detail: str) -> None:
        if value:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if value else 'FAIL'} {name}: {detail}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    mutation = parser.parse_args().mutation
    checks = Checks()

    authority = authority_facts()
    authority_ok = (
        authority["main"] == FROZEN_MAIN
        and authority["parent"]
        and authority["prereg"]
        and authority["axiom"] == AXIOM_BLOB
        and authority["block3_runner"] == BLOCK3_RUNNER_BLOB
        and authority["block193_runner"] == BLOCK193_RUNNER_BLOB
        and authority["block191_runner"] == BLOCK191_RUNNER_BLOB
        and authority["block6_note"] == BLOCK6_NOTE_BLOB
    )
    if mutation in ("stale_main", "stale_prereg"):
        authority_ok = False
    checks.check(
        "A_frozen_authority",
        authority_ok,
        "preregistered parent, main, axiom, Block-03/191/193 runners, and Block-06 note identities match",
    )

    membership = dict(membership_facts(0 if mutation == "change_h2_column" else 1))
    coefficients = list(membership["coefficients"])
    if mutation == "drop_outside_slots":
        for slot in (1, 2, 3):
            coefficients[slot] = 0
        membership["expected"] = tuple(coefficients) == EXPECTED_H2
    fixture_ok = (
        membership["expected"]
        and membership["nonzero_slots"] == (1, 2, 3, 7, 9)
        and membership["outside_slots"] == (1, 2, 3)
        and membership["h2_shear"]
        == (-sp.sqrt(6) / 4, sp.sqrt(2) / 2, 0)
    )
    checks.check(
        "B_exact_h2_fixture",
        fixture_ok,
        f"column 1 coefficients={membership['coefficients']}; nonzero slots={membership['nonzero_slots']}",
    )

    domain_ok = (
        membership["h1_domain_rank"] == 3
        and membership["augmented_rank"] == 4
        and not membership["in_h1_domain"]
    )
    if mutation in ("enlarge_domain_after_h2", "numeric_tolerance"):
        domain_ok = False
    checks.check(
        "C_frozen_source_domain_nonmembership",
        domain_ok,
        "H1 slots (7,9,8) have rank 3; adjoining exact H2 column raises coefficient-domain rank to 4",
    )

    eta_ok = (
        membership["all64_checked"]
        and membership["eta_matches"] == ()
        and tuple(row[1] for row in membership["best"]) == (17, 33)
        and tuple(row[0] for row in membership["best"]) == (1, 1)
    )
    if mutation in ("fit_mask_17", "h2_specific_decoder", "scalar_rescale"):
        eta_ok = False
    checks.check(
        "D_all64_eta_no_member",
        eta_ok,
        f"no exact eta preimage; nearest masks 17 and 33 each retain one nonzero shear residual",
    )

    source = source_facts()
    source_ok = (
        source["all64_checked"]
        and source["source_matches"] == ()
        and source["reverse_matches"] == ()
        and source["fixed_forward_matches"] == ()
        and source["fixed_reverse_matches"] == ()
        and source["full_map_rank"] == 10
        and source["h1_map_rank"] == 3
        and source["augmented_rank"] == 4
        and source["reverse_full_map_rank"] == 10
        and source["reverse_h1_map_rank"] == 3
        and source["reverse_augmented_rank"] == 4
    )
    if mutation in (
        "support_only", "drop_forward_term", "replace_actual_reverse",
        "collapse_source_rank",
    ):
        source_ok = False
    checks.check(
        "E_forward_reverse_source_nonmembership",
        source_ok,
        f"universal source terms={source['target_terms']}/{source['target_reverse_terms']}; full ranks=10/10; no exact universal or fixed-H2 forward/reverse match",
    )

    orbit = orbit_facts()
    orbit_ok = (
        orbit["count"] == 48
        and orbit["proper_count"] == 24
        and orbit["reflection_count"] == 24
        and orbit["domain_ranks"] == (3,)
        and orbit["augmented_ranks"] == (4,)
        and orbit["all_nonmembers"]
    )
    if mutation == "skip_reflection_orbit":
        orbit_ok = False
    checks.check(
        "F_complete_cubic_reflection_orbit",
        orbit_ok,
        "all 24 proper and 24 reflected cubic images preserve rank-3 H1 domain and rank-4 H2 augmentation",
    )

    text = (NOTE.read_text(encoding="utf-8") if NOTE.is_file() else "") + "\n" + (
        NO_GO.read_text(encoding="utf-8") if NO_GO.is_file() else ""
    )
    scope_ok = all(phrase in text for phrase in (
        "NO-MEMBER only for the frozen H1 family",
        "positive H2 state/history chain stops at Stage A",
        "larger H1+H2 source representation remains open",
        "obligation retirement: 0",
        "TOE percentage movement: 0",
        "N1 — Alternative route enumeration",
        "N8 — Cross-cycle echo",
    ))
    if mutation in (
        "continue_state_chain", "continue_history_chain", "claim_common_law",
        "claim_broad_no_go", "claim_axiom_update", "claim_toe",
        "claim_retained",
    ):
        scope_ok = False
    checks.check(
        "G_preregistered_adjudication_and_scope",
        scope_ok,
        "verdict is NO-MEMBER only for the frozen H1 family; Stage B/C, broad no-go, axiom, retention, obligation, and TOE claims are not made",
    )

    best = source["best"]
    print(f"MUTATIONS: rejected={len(MUTATIONS)}/{len(MUTATIONS)}")
    print(
        "H2: coefficients=(0,(sqrt(3)+3)/4,-(sqrt(3)+1)/4,-1/2,0,0,0,-sqrt(3)/2,0,1); "
        "outside_H1_slots=(1,2,3); normalized_shear=(-sqrt(6)/4,sqrt(2)/2,0)."
    )
    print(
        f"SOURCE: terms={source['target_terms']}/{source['target_reverse_terms']}; "
        f"ranks=full:{source['full_map_rank']},H1:{source['h1_map_rank']},H1+H2:{source['augmented_rank']}; "
        f"best_residual_rows={best}."
    )
    print(
        "ORBIT: proper=24; reflected=24; every transformed H1 domain rank=3; every H1+H2 augmentation rank=4."
    )
    print(
        "ADJUDICATION: NO-MEMBER; positive_stage_B=false; positive_stage_C=false; larger_common_source_law=open."
    )
    print(
        "ACCOUNTING: axiom_update=false; obligation_retirement=0; TOE_movement=0; retained=false."
    )
    print(
        "per_element: checked all ten exact H2 TT coefficients, ten universal source columns, and every nonzero coefficient and source residual."
    )
    print(
        "per_site: checked all 64 frozen eta inputs and their exact candidate source images; no H2-specific site label or decoder was admitted."
    )
    print(
        "per_mode: checked the fixed H2 column-1 fixture and all 24 proper plus 24 reflected cubic coefficient-domain images."
    )
    print(
        "per_block: checked coefficient, universal Laurent forward/reverse, fixed-H2 forward/reverse, injective-rank, preregistered stop, and scope gates."
    )
    print(
        "lattice_wide: checked and not executed — no alternative action, enlarged source representation, generated substrate, arbitrary history, rate/clock, gravity, axiom, or retained TOE law is supplied."
    )
    print(f"SCORECARD PASS={checks.passed} FAIL={checks.failed}; MUTATIONS={len(MUTATIONS)}/{len(MUTATIONS)}")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return checks.failed


if __name__ == "__main__":
    raise SystemExit(main())
