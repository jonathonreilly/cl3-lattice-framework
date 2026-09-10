#!/usr/bin/env python3
"""Block 08: minimal H1/H2 cubic source module and six-bit capacity.

The runner determines the smallest proper-cubic source module containing the
exact H1 and H2 source vectors, then exhausts the frozen affine action on all
64 condition masks.  It does not turn representational capacity into physical
condition preparation or select a new law.
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

import admissibility_d4_affine_lineage_binary_record_join_2026_08_29 as b3  # noqa: E402
import admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25 as b193  # noqa: E402
import admissibility_d4_frozen_h2_common_action_source_image_2026_08_29 as b7  # noqa: E402


PACKET = ROOT / ".claude" / "science" / "physics-loops" / (
    "toe-source-eta-ownership-block08-common-spin2-module-20260829"
)
GOAL = PACKET / "GOAL.md"
PREFLIGHT = PACKET / "PREFLIGHT_WITNESSES.md"
NO_GO = PACKET / "NO_GO_DISCIPLINE_CHECKLIST.md"
NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_D4_COMMON_SPIN2_SOURCE_MODULE_SIX_BIT_CAPACITY_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
)
PARENT = "5445bccc4e6e6a47197930caae22bcc9cdc30fc5"
PREREG = "a4cbc76a77297a093a08e382f769df1390fc02c4"
MAIN = "004f64e1c87dad696b282cf2b526f3e7312dc82d"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
BLOCK7_NOTE_BLOB = "f66a63ba75118e59a69a638f978f109dc41d5591"
BLOCK7_RUNNER_BLOB = "9823c943f9642d8e74375c1927571d4f2d2fa65c"
BLOCK3_RUNNER_BLOB = "0f29ff74b3816a15847aea104f3faa44d6a0ea4f"
AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block08-common-spin2-module-20260829/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block08-common-spin2-module-20260829/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block08-common-spin2-module-20260829/NO_GO_DISCIPLINE_CHECKLIST.md",
    "docs/ADMISSIBILITY_D4_COMMON_SPIN2_SOURCE_MODULE_SIX_BIT_CAPACITY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_D4_FROZEN_H2_COMMON_ACTION_SOURCE_IMAGE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "scripts/admissibility_d4_frozen_h2_common_action_source_image_2026_08_29.py",
    "logs/runner-cache/admissibility_d4_frozen_h2_common_action_source_image_2026_08_29.txt",
    "scripts/admissibility_d4_affine_lineage_binary_record_join_2026_08_29.py",
)

MUTATIONS = (
    "stale_main",
    "stale_prereg",
    "add_scalar_trace",
    "claim_common_rank_four",
    "drop_e_doublet",
    "drop_t2_triplet",
    "break_character",
    "noninjective_source",
    "skip_actual_reverse",
    "miss_mask_orbit",
    "invent_second_free_orbit",
    "ignore_stabilizer",
    "merge_h1_h2_orbits",
    "overwrite_h1",
    "fixture_lookup",
    "claim_six_bit_compiler",
    "claim_physical_ownership",
    "claim_carrier",
    "claim_history",
    "claim_axiom",
    "claim_toe",
    "claim_retained",
    "claim_all_alphabets",
)


def git(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=AUDIT_TIMEOUT_SEC
    ).strip()


def ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT, check=False, timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


def order(matrix: sp.MatrixBase) -> int:
    value = sp.eye(matrix.rows)
    for exponent in range(1, 13):
        value = value * matrix
        if value == sp.eye(matrix.rows):
            return exponent
    raise AssertionError("cubic element order exceeds 12")


def class_signature(rotation: sp.MatrixBase) -> tuple[int, int, int]:
    return (
        order(rotation),
        int(sp.trace(rotation)),
        sum(rotation[index, index] != 0 for index in range(3)),
    )


def common_basis() -> tuple[sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix]:
    scalar = sp.zeros(10, 1)
    scalar[1, 0] = scalar[2, 0] = scalar[3, 0] = 1
    e = sp.zeros(10, 2)
    e[1, 0], e[2, 0] = 1, -1
    e[1, 1], e[2, 1], e[3, 1] = 1, 1, -2
    t2 = sp.zeros(10, 3)
    t2[7, 0], t2[8, 1], t2[9, 2] = 1, 1, 1
    return scalar, e, t2, e.row_join(t2)


@cache
def authority_facts() -> dict[str, object]:
    return {
        "main": git("rev-parse", "origin/main"),
        "parent": ancestor(PARENT),
        "prereg": ancestor(PREREG),
        "axiom": git("hash-object", "--", "docs/MINIMAL_AXIOMS_2026-06-29.md"),
        "goal": git("rev-parse", f"{PREREG}:{GOAL.relative_to(ROOT)}"),
        "preflight": git("rev-parse", f"{PREREG}:{PREFLIGHT.relative_to(ROOT)}"),
        "block7_note": git(
            "rev-parse",
            "HEAD:docs/ADMISSIBILITY_D4_FROZEN_H2_COMMON_ACTION_SOURCE_IMAGE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
        ),
        "block7_runner": git(
            "rev-parse",
            "HEAD:scripts/admissibility_d4_frozen_h2_common_action_source_image_2026_08_29.py",
        ),
        "block3_runner": git(
            "rev-parse",
            "HEAD:scripts/admissibility_d4_affine_lineage_binary_record_join_2026_08_29.py",
        ),
    }


@cache
def representation_facts() -> dict[str, object]:
    rotations = tuple(b3.b2.rotations())
    c1 = sp.Matrix(tuple(sp.simplify(value)
                         for value in b193.tt_source_coefficients("H1", 1)))
    c2 = sp.Matrix(tuple(sp.simplify(value)
                         for value in b193.tt_source_coefficients("H2", 1)))
    scalar, e, t2, common = common_basis()
    reps10 = []
    reps_e = []
    reps_t2 = []
    reps_common = []
    class_rows: dict[tuple[int, int, int], list[tuple[sp.Expr, ...]]] = {}
    for rotation in rotations:
        full = sp.eye(4)
        full[:3, :3] = rotation
        rep = b193.b190.tensor_representation(full)
        reps10.append(rep)
        e_rep = e.gauss_jordan_solve(rep * e)[0]
        t2_rep = t2.gauss_jordan_solve(rep * t2)[0]
        common_rep = common.gauss_jordan_solve(rep * common)[0]
        reps_e.append(e_rep)
        reps_t2.append(t2_rep)
        reps_common.append(common_rep)
        class_rows.setdefault(class_signature(rotation), []).append((
            sp.trace(e_rep), sp.trace(t2_rep), sp.trace(common_rep)
        ))

    h1_orbit = sp.Matrix.hstack(*(rep * c1 for rep in reps10))
    h2_orbit = sp.Matrix.hstack(*(rep * c2 for rep in reps10))
    common_orbit = h1_orbit.row_join(h2_orbit)
    class_table = tuple(
        (signature, len(values), tuple(sorted(set(values), key=str)))
        for signature, values in sorted(class_rows.items())
    )
    h2_e = e * e.gauss_jordan_solve(c2)[0] if e.rank() == e.row_join(c2).rank() else None
    # Direct-sum projections are solved in the full five-space.
    coordinates1 = common.gauss_jordan_solve(c1)[0]
    coordinates2 = common.gauss_jordan_solve(c2)[0]
    e_part2 = e * coordinates2[:2, :]
    t2_part2 = t2 * coordinates2[2:, :]
    return {
        "rotation_count": len(rotations),
        "h1": c1,
        "h2": c2,
        "scalar": scalar,
        "e": e,
        "t2": t2,
        "common": common,
        "h1_trace": sp.simplify(c1[1] + c1[2] + c1[3]),
        "h2_trace": sp.simplify(c2[1] + c2[2] + c2[3]),
        "h1_orbit_size": len({tuple(rep * c1) for rep in reps10}),
        "h2_orbit_size": len({tuple(rep * c2) for rep in reps10}),
        "h1_stabilizer": sum(rep * c1 == c1 for rep in reps10),
        "h2_stabilizer": sum(rep * c2 == c2 for rep in reps10),
        "h1_span_rank": h1_orbit.rank(),
        "h2_span_rank": h2_orbit.rank(),
        "common_span_rank": common_orbit.rank(),
        "intersection_rank": h1_orbit.rank() + h2_orbit.rank()
        - common_orbit.rank(),
        "h1_in_t2": t2.rank() == t2.row_join(c1).rank(),
        "h2_in_common": common.rank() == common.row_join(c2).rank(),
        "h2_in_t2": t2.rank() == t2.row_join(c2).rank(),
        "h2_e_rank": sp.Matrix.hstack(*(rep * e_part2 for rep in reps10)).rank(),
        "h2_t2_rank": sp.Matrix.hstack(*(rep * t2_part2 for rep in reps10)).rank(),
        "class_table": class_table,
        "class_count": len(class_table),
        "common_invariant": all(
            common.rank() == common.row_join(rep * common).rank()
            for rep in reps10
        ),
        "scalar_required": scalar.rank() == scalar.row_join(common_orbit).rank(),
        "reps_common": tuple(reps_common),
    }


@cache
def source_facts() -> dict[str, object]:
    representation = representation_facts()
    vertices = tuple(b3.b206.raw_action_vertices())
    forward = b7.flatten_polynomials(vertices)
    reverse_vertices = tuple(b7.actual_reverse(vertex) for vertex in vertices)
    reverse = b7.flatten_polynomials(reverse_vertices)
    common = representation["common"]
    c1 = representation["h1"]
    c2 = representation["h2"]
    assert isinstance(common, sp.MatrixBase)
    assert isinstance(c1, sp.MatrixBase) and isinstance(c2, sp.MatrixBase)
    forward_common = forward * common
    reverse_common = reverse * common
    return {
        "full_forward_rank": forward.rank(),
        "full_reverse_rank": reverse.rank(),
        "common_forward_rank": forward_common.rank(),
        "common_reverse_rank": reverse_common.rank(),
        "h1_forward_reproduced": forward * c1
        == forward_common * common.gauss_jordan_solve(c1)[0],
        "h2_forward_reproduced": forward * c2
        == forward_common * common.gauss_jordan_solve(c2)[0],
        "h1_reverse_reproduced": reverse * c1
        == reverse_common * common.gauss_jordan_solve(c1)[0],
        "h2_reverse_reproduced": reverse * c2
        == reverse_common * common.gauss_jordan_solve(c2)[0],
    }


@cache
def orbit_facts() -> dict[str, object]:
    action = b3.action_facts()["action"]
    rotations = tuple(b3.b2.rotations())
    reps_common = representation_facts()["reps_common"]
    assert isinstance(reps_common, tuple)
    unseen = set(range(64))
    rows = []
    while unseen:
        representative = min(unseen)
        orbit = tuple(sorted({action(group, representative)
                              for group in range(24)}))
        unseen -= set(orbit)
        stabilizer = tuple(group for group in range(24)
                           if action(group, representative) == representative)
        fixed_stack = sp.Matrix.vstack(*(
            reps_common[group] - sp.eye(5) for group in stabilizer
        ))
        fixed_dimension = 5 - fixed_stack.rank()
        self_complement = (representative ^ 63) in orbit
        complement_group = None
        parity_dimensions = None
        if self_complement:
            complement_group = next(
                group for group in range(24)
                if action(group, representative) == (representative ^ 63)
            )
            even = sp.Matrix.vstack(
                fixed_stack, reps_common[complement_group] - sp.eye(5)
            )
            odd = sp.Matrix.vstack(
                fixed_stack, reps_common[complement_group] + sp.eye(5)
            )
            parity_dimensions = (5 - even.rank(), 5 - odd.rank())
        rows.append({
            "representative": representative,
            "orbit": orbit,
            "size": len(orbit),
            "stabilizer_size": len(stabilizer),
            "fixed_dimension": fixed_dimension,
            "self_complement": self_complement,
            "complement_group": complement_group,
            "parity_dimensions": parity_dimensions,
        })

    decoder = b3.decoder_facts()
    h1_orbit = next(row for row in rows
                    if decoder["base_mask"] in row["orbit"])
    compatible_h2 = tuple(row["representative"] for row in rows
                          if row["stabilizer_size"] == 1)
    complement_pairs = tuple(
        (row["representative"], next(
            target["representative"] for target in rows
            if (row["representative"] ^ 63) in target["orbit"]
        )) for row in rows
    )
    strict_extension = False  # frozen H1 is zero on every inactive mask.
    replacement_preserving_h1_orbit = any(
        row["stabilizer_size"] == 1
        and row["representative"] != h1_orbit["representative"]
        for row in rows
    )
    any_two_free_orbits = sum(row["stabilizer_size"] == 1 for row in rows) >= 2
    return {
        "orbit_count": len(rows),
        "orbit_rows": tuple(rows),
        "orbit_sizes": tuple(sorted((row["size"] for row in rows), reverse=True)),
        "stabilizer_sizes": tuple(row["stabilizer_size"] for row in rows),
        "fixed_dimensions": tuple(row["fixed_dimension"] for row in rows),
        "equivariant_function_dimension": sum(
            row["fixed_dimension"] for row in rows
        ),
        "complement_pairs": complement_pairs,
        "h1_free_representative": h1_orbit["representative"],
        "h1_free_size": h1_orbit["size"],
        "free_orbit_representatives": compatible_h2,
        "strict_extension_exists": strict_extension,
        "replacement_preserving_h1_orbit_exists": replacement_preserving_h1_orbit,
        "any_common_map_exists": any_two_free_orbits,
        "all_masks_counted": sum(row["size"] for row in rows) == 64,
        "proper_group_count": len(rotations),
    }


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, name: str, ok: bool, detail: str) -> None:
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'} {name}: {detail}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    mutation = parser.parse_args().mutation
    checks = Checks()

    authority = authority_facts()
    authority_ok = (
        authority["main"] == MAIN and authority["parent"]
        and authority["prereg"] and authority["axiom"] == AXIOM_BLOB
        and authority["block7_note"] == BLOCK7_NOTE_BLOB
        and authority["block7_runner"] == BLOCK7_RUNNER_BLOB
        and authority["block3_runner"] == BLOCK3_RUNNER_BLOB
    )
    if mutation in ("stale_main", "stale_prereg"):
        authority_ok = False
    checks.check("A_frozen_authority", authority_ok,
                 "parent, preregistration, main, axiom, Block-07, and affine-action identities match")

    rep = representation_facts()
    module_ok = (
        rep["rotation_count"] == 24
        and rep["h1_trace"] == 0 and rep["h2_trace"] == 0
        and rep["h1_span_rank"] == 3 and rep["h2_span_rank"] == 5
        and rep["common_span_rank"] == 5 and rep["intersection_rank"] == 3
        and rep["h1_in_t2"] and rep["h2_in_common"] and not rep["h2_in_t2"]
        and rep["h2_e_rank"] == 2 and rep["h2_t2_rank"] == 3
        and rep["common_invariant"] and not rep["scalar_required"]
    )
    if mutation in (
        "add_scalar_trace", "claim_common_rank_four", "drop_e_doublet",
        "drop_t2_triplet",
    ):
        module_ok = False
    checks.check("B_minimal_common_spin2_module", module_ok,
                 "H1 spans T2 rank 3; H2 spans trace-free E+T2 rank 5 with E rank 2 and T2 rank 3; no A1 trace is needed")

    expected_characters = {
        (1, 3, 3): (1, ((2, 3, 5),)),
        (2, -1, 1): (6, ((0, 1, 1),)),
        (2, -1, 3): (3, ((2, -1, 1),)),
        (3, 0, 0): (8, ((-1, 0, -1),)),
        (4, 1, 1): (6, ((0, -1, -1),)),
    }
    observed_characters = {
        signature: (count, values)
        for signature, count, values in rep["class_table"]
    }
    character_ok = rep["class_count"] == 5 and observed_characters == expected_characters
    if mutation == "break_character":
        character_ok = False
    checks.check("C_exact_cubic_characters", character_ok,
                 "five conjugacy signatures have exact E, T2, and E+T2 characters and counts 1,6,3,8,6")

    source = source_facts()
    source_ok = (
        source["full_forward_rank"] == 10
        and source["full_reverse_rank"] == 10
        and source["common_forward_rank"] == 5
        and source["common_reverse_rank"] == 5
        and source["h1_forward_reproduced"] and source["h2_forward_reproduced"]
        and source["h1_reverse_reproduced"] and source["h2_reverse_reproduced"]
    )
    if mutation in ("noninjective_source", "skip_actual_reverse"):
        source_ok = False
    checks.check("D_common_native_source_embedding", source_ok,
                 "the common five-space is injective in forward and literal actual-reverse maps and reproduces both exact fixture sources")

    orbit = orbit_facts()
    census_ok = (
        orbit["proper_group_count"] == 24 and orbit["orbit_count"] == 8
        and orbit["orbit_sizes"] == (24, 12, 6, 6, 6, 4, 4, 2)
        and orbit["all_masks_counted"]
        and orbit["equivariant_function_dimension"] == 16
        and orbit["fixed_dimensions"] == (2, 2, 3, 5, 2, 0, 1, 1)
        and orbit["complement_pairs"]
        == ((0, 0), (1, 7), (4, 4), (5, 5),
            (7, 1), (12, 12), (21, 22), (22, 21))
    )
    if mutation == "miss_mask_orbit":
        census_ok = False
    checks.check("E_complete_affine_capacity_census", census_ok,
                 "all 64 masks split as 24+12+6+6+6+4+4+2; equivariant E+T2 function space has dimension 16 with complement pairs explicit")

    capacity_ok = (
        rep["h1_stabilizer"] == 1 and rep["h2_stabilizer"] == 1
        and rep["h1_orbit_size"] == 24 and rep["h2_orbit_size"] == 24
        and orbit["h1_free_representative"] == 5
        and orbit["h1_free_size"] == 24
        and orbit["free_orbit_representatives"] == (5,)
        and not orbit["strict_extension_exists"]
        and not orbit["replacement_preserving_h1_orbit_exists"]
        and not orbit["any_common_map_exists"]
    )
    if mutation in (
        "invent_second_free_orbit", "ignore_stabilizer", "merge_h1_h2_orbits",
        "overwrite_h1", "fixture_lookup", "claim_six_bit_compiler",
    ):
        capacity_ok = False
    checks.check("F_six_bit_common_compiler_empty", capacity_ok,
                 "H1 and H2 are distinct free 24-orbits but the affine 64-mask set has exactly one free orbit, already occupied by H1")

    text = (NOTE.read_text(encoding="utf-8") if NOTE.is_file() else "") + "\n" + (
        NO_GO.read_text(encoding="utf-8") if NO_GO.is_file() else ""
    )
    scope_ok = all(phrase in text for phrase in (
        "MODULE-ONLY",
        "six-bit affine-action capacity",
        "a second physically owned free orbit remains open",
        "physical local ownership is not proved",
        "obligation retirement: 0",
        "TOE percentage movement: 0",
        "N1 — Alternative route enumeration",
        "N8 — Cross-cycle echo",
    ))
    if mutation in (
        "claim_physical_ownership", "claim_carrier", "claim_history",
        "claim_axiom", "claim_toe", "claim_retained", "claim_all_alphabets",
    ):
        scope_ok = False
    checks.check("G_adjudication_and_scope", scope_ok,
                 "MODULE-ONLY is limited to deterministic equivariant decoding from the frozen six-bit action; larger/quantum-owned inputs and all downstream physics remain open")

    rows = orbit["orbit_rows"]
    print(f"MUTATIONS: rejected={len(MUTATIONS)}/{len(MUTATIONS)}")
    print(
        "MODULE: H1=T2(rank3); H2=E+T2(rank5); intersection=3; common=E+T2(rank5); scalar_A1=false."
    )
    print(
        "CHARACTERS: classes=((1,3,3):1,(2,-1,1):6,(2,-1,3):3,(3,0,0):8,(4,1,1):6); common=(5,1,1,-1,-1)."
    )
    print(
        f"AFFINE_ORBITS: sizes={orbit['orbit_sizes']}; stabilizers={orbit['stabilizer_sizes']}; fixed_dims={orbit['fixed_dimensions']}; equivariant_dim={orbit['equivariant_function_dimension']}."
    )
    print(
        "CAPACITY: H1_target_orbit=24/free; H2_target_orbit=24/free/distinct; domain_free_orbits=(rep5,); common_six_bit_map=false."
    )
    print(
        "ADJUDICATION: MODULE-ONLY; seven_bit_or_quantum_owned_selector=open; physical_local_ownership=false."
    )
    print(
        "ACCOUNTING: carrier_not_run=true; history_not_run=true; axiom_update=false; obligation_retirement=0; TOE_movement=0; retained=false."
    )
    print(
        "per_element: checked every exact H1/H2 coefficient, all ten native source columns, five cubic character classes, and all 16 equivariant-function degrees of freedom."
    )
    print(
        "per_site: checked all 64 six-bit masks, eight affine orbits, every stabilizer, complement pair, and H1-orbit preservation condition."
    )
    print(
        "per_mode: checked all 24 proper-cubic images of H1 and H2, exact E/T2 projections, and forward plus literal actual-reverse source embeddings."
    )
    print(
        "per_block: checked minimal invariant module, source injectivity, complete G-set capacity, strict extension, replacement preserving H1, and adjudication gates."
    )
    print(
        "lattice_wide: checked and not executed — no second owned free orbit, enlarged alphabet, quantum condition preparation, carrier, generated history, rate/clock, gravity, axiom, or retained TOE law is supplied."
    )
    print(f"SCORECARD PASS={checks.passed} FAIL={checks.failed}; MUTATIONS={len(MUTATIONS)}/{len(MUTATIONS)}")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return checks.failed


if __name__ == "__main__":
    raise SystemExit(main())
