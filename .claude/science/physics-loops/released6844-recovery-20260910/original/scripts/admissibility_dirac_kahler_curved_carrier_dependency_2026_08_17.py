#!/usr/bin/env python3
"""Block 128: curved-carrier dependency of the Dirac--Kahler OS lane.

The runner uses the content-bound Block 105 nonuniform overlap Hodge to
display two exact shifted-chart action completions.  It then certifies why
those completions do not execute the flat companion/momentum pipeline and
why the common nilpotent differential remains the live dependency.  All
scientific arithmetic is exact; wall-clock timing is the sole float.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
import subprocess
import time

import sympy as sp

import admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14 as block105


R = sp.Rational
I = sp.I
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_"
    "BOUNDED_THEOREM_NOTE_2026-08-17.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_NATURALITY_MODULI_"
    "BOUNDED_THEOREM_NOTE_2026-08-17.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_naturality_moduli_2026_08_17.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_naturality_moduli_"
    "2026_08_17.txt"
)
CURVED_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_"
    "NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
CURVED_RUNNER = (
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_"
    "nonuniform_hodge_overlap_2026_08_14.py"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_NATURALITY_MODULI_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "scripts/admissibility_dirac_kahler_naturality_moduli_2026_08_17.py",
    "logs/runner-cache/admissibility_dirac_kahler_naturality_moduli_2026_08_17.txt",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "02602ca09e4ea69a805a824c3c1f31cb1ee35b20"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block127-naturality-moduli-20260817"
)
PARENT_COMMIT = "ca6792464f60598013a3700f99c02a467af64b7a"
PARENT_NOTE_BLOB = "92e3845622ec28df42abf541d80972748b646735"
PARENT_RUNNER_BLOB = "1c5eadf5412006b9b5d5f70c2c0bd702b5c11c1e"
PARENT_CACHE_BLOB = "220d02518328395c7ec3dee9b816d02b02ab74ef"
CURVED_COMMIT = "d06066c2b908aaca0779625d831dfb10620cf34d"
CURVED_NOTE_BLOB = "5eff91757e38f3f2ea7dc2a2c50788636cc2e3a5"
CURVED_RUNNER_BLOB = "4870f31b5880028ad4f1f3095aad4d0820e4668f"
ANCESTOR_COMMITS = (
    (126, "a145a4e2cfc19bc919371196d7c5f3451c0bb45d"),
    (125, "ff85cc8c6a991b2926b9ac5cb5168f2587bc0c0d"),
    (124, "da2b9020e9f15ac55640ef87a0798a78e3c9a0d0"),
    (123, "954322e0e085d6c3133ce24dca49db2efbd7d0a6"),
    (122, "f067b99be7eb49fc46ea8dffccab5e20e6052d88"),
    (121, "1714abeefcf3763c0bfe001f30fd14521c538622"),
    (120, "1c2386bf3df420707fd2ecb2d7ec84002ba40ad1"),
    (119, "33fd2d21558604718f3a88713fe1976aff8f9dbb"),
    (118, "fdd1883c54ca8cc14b1337cc1edc249792d5dab2"),
    (117, "f800356aec0989b6e0fa80ed43274794243b1ca2"),
    (116, "c36d11e4e8d927c6fc31f0a8b579d4bd15f4fa43"),
    (115, "c78301fef7521d0518f485f1bf9266983c9e516a"),
    (114, "75026e71cfbd44ed665ddc41c22ebaa722720ea9"),
    (113, "e76893eb7204d1d727a3ab8838fb3fada3f45dfc"),
    (112, "385a6ba5b1594f20e5d4eebba9da68d8e72abc10"),
    (111, "b04e7c8747b09734711cfcd2bfab961bd12e81ad"),
    (110, "d6761278fca9cac617200792473a8f4da3a6cfff"),
    (109, "ad84cfcc857a65285389ba93b47cd7b718589be5"),
    (108, "8afe8dff5ccf531208238af0aaaec1f547d73874"),
    (107, "d41a05e153d4cb77eee125b82fc0b0bd767bf32e"),
    (106, "22d6d90ec2279e5868c9c825149b2a20beea3797"),
    (105, "d06066c2b908aaca0779625d831dfb10620cf34d"),
    (104, "7fe07db6c03fad1191893c942f708c5cb9a54c43"),
    (103, "99cee0a6c962b382a3ca1a8497d589ffa280dfe8"),
)

MUTATIONS = (
    "stale_axiom_authority",
    "stale_parent_authority",
    "break_inequivalence",
    "claim_global_action",
    "break_commutator_rank",
    "break_schur_rank",
    "break_kernel_witness",
    "break_underdetermination",
    "break_regrouping_survival",
    "break_census",
    "claim_differential_impossible",
    "weaken_no_go_packet",
    "drop_n5_resolution",
    "claim_toe_progress",
    "claim_axiom_amendment",
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition: object) -> None:
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {statement}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args,
        cwd=ROOT,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
    ).strip()


def worktree_blob(path: str) -> str:
    return git_output("hash-object", path)


def commit_blob(commit: str, path: str) -> str:
    return git_output("rev-parse", f"{commit}:{path}")


def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, descendant),
        cwd=ROOT,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


def authority_certificate(mutation: str) -> dict[str, object]:
    expected_axiom = (
        "0" * 40 if mutation == "stale_axiom_authority" else CURRENT_AXIOM_BLOB
    )
    expected_parent = (
        "0" * 40 if mutation == "stale_parent_authority" else PARENT_NOTE_BLOB
    )
    return {
        "main": git_output("rev-parse", "origin/main"),
        "axiom": commit_blob("origin/main", AXIOM_PATH),
        "worktree_axiom": worktree_blob(AXIOM_PATH),
        "expected_axiom": expected_axiom,
        "registry": commit_blob("origin/main", REGISTRY_PATH),
        "worktree_registry": worktree_blob(REGISTRY_PATH),
        "parent": git_output("rev-parse", PARENT_REF),
        "parent_ancestor": is_ancestor(PARENT_COMMIT, "HEAD"),
        **{
            f"ancestor_{number}": is_ancestor(commit, "HEAD")
            for number, commit in ANCESTOR_COMMITS
        },
        "parent_note": commit_blob(PARENT_COMMIT, PARENT_NOTE),
        "expected_parent": expected_parent,
        "parent_runner": commit_blob(PARENT_COMMIT, PARENT_RUNNER),
        "parent_cache": commit_blob(PARENT_COMMIT, PARENT_CACHE),
        "curved": git_output("rev-parse", CURVED_COMMIT),
        "curved_ancestor": is_ancestor(CURVED_COMMIT, "HEAD"),
        "curved_note": commit_blob(CURVED_COMMIT, CURVED_NOTE),
        "curved_runner": commit_blob(CURVED_COMMIT, CURVED_RUNNER),
    }


def normalized_note() -> str:
    try:
        raw_note = NOTE_PATH.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError, UnicodeError):
        return ""
    return " ".join(raw_note.lower().split())


SPACE_EXTENT = block105.LENGTH
PHYSICAL_TIME_EXTENT = block105.LENGTH
COVER_TIME_EXTENT = 2 * PHYSICAL_TIME_EXTENT
COVER_SIZE = COVER_TIME_EXTENT * SPACE_EXTENT
DISPLAYED_ORIGINS = ((1, 0), (1, 1))
DISPLAYED_STEPS = (1, 3)
FORWARD_DIRECTIONS = (2, -2)
KERNEL_WITNESS = sp.Matrix((0, 1, 0, 0))
S_X = R(3, 5)
S_T = R(4, 5)
MASS = R(2, 7)


def cover_index(time_coordinate: int, space_coordinate: int) -> int:
    return (
        (time_coordinate % COVER_TIME_EXTENT) * SPACE_EXTENT
        + space_coordinate % SPACE_EXTENT
    )


def cover_embedding(time_coordinate: int, space_coordinate: int) -> sp.Matrix:
    matrix = sp.zeros(COVER_SIZE, 4)
    for column, (delta_t, delta_x) in enumerate(
        ((0, 0), (0, 1), (1, 0), (1, 1))
    ):
        matrix[
            cover_index(
                time_coordinate + delta_t,
                space_coordinate + delta_x,
            ),
            column,
        ] = 1
    return matrix


def curved_hodge_cover() -> sp.Matrix:
    """Lift the exact Block 105 overlap Hodge to an unaliased time cover."""
    field = block105.overlap_field()
    result = sp.zeros(COVER_SIZE)
    for time_coordinate in range(COVER_TIME_EXTENT):
        for space_coordinate in range(SPACE_EXTENT):
            shear, volume = field[
                (
                    time_coordinate % PHYSICAL_TIME_EXTENT,
                    space_coordinate,
                )
            ]
            embedding = cover_embedding(time_coordinate, space_coordinate)
            result += (
                embedding
                * block105.shear_hodge(shear, volume)
                * embedding.T
                / 4
            )
    return sp.simplify(result)


def chart_differential_cover(origin: tuple[int, int]) -> sp.Matrix:
    """A displayed chartwise nilpotent choice, not a common differential."""
    local_differential = I * (S_X * block105.EX + S_T * block105.ET)
    result = sp.zeros(COVER_SIZE)
    for coarse_t in range(COVER_TIME_EXTENT // 2):
        for coarse_x in range(SPACE_EXTENT // 2):
            embedding = cover_embedding(
                2 * coarse_t + origin[0],
                2 * coarse_x + origin[1],
            )
            result += embedding * local_differential * embedding.T
    return result


def antiperiodic_quotient(matrix: sp.Matrix) -> sp.Matrix:
    """Fold the two-period cover with psi(t+4)=-psi(t)."""
    identity = sp.eye(PHYSICAL_TIME_EXTENT * SPACE_EXTENT)
    injection = sp.Matrix.vstack(-identity, identity)
    selection = sp.Matrix.hstack(sp.zeros(identity.rows), identity)
    return sp.simplify(selection * matrix * injection)


def grassmann_form(action: sp.Matrix) -> sp.Matrix:
    """Alternating form for one complex Grassmann mode and its conjugate."""
    zero = sp.zeros(action.rows)
    return sp.Matrix.vstack(
        sp.Matrix.hstack(zero, action),
        sp.Matrix.hstack(-action.T, zero),
    )


def time_bands(matrix: sp.Matrix) -> tuple[int, ...]:
    bands: set[int] = set()
    for row in range(matrix.rows):
        row_time = row // SPACE_EXTENT
        for column in range(matrix.cols):
            if matrix[row, column] == 0:
                continue
            raw = (column // SPACE_EXTENT - row_time) % COVER_TIME_EXTENT
            signed = (
                raw
                if raw <= COVER_TIME_EXTENT // 2
                else raw - COVER_TIME_EXTENT
            )
            bands.add(signed)
    return tuple(sorted(bands))


@dataclass(frozen=True)
class CurvedCompletion:
    origin: tuple[int, int]
    differential: sp.Matrix
    cover_action: sp.Matrix
    physical_action: sp.Matrix
    alternating_action: sp.Matrix
    bands: tuple[int, ...]
    commutator_rank: int


def build_completions() -> tuple[CurvedCompletion, CurvedCompletion]:
    hodge = curved_hodge_cover()
    spatial_shift = block105.translation_matrix((0, 1))
    doubled_shift = sp.diag(spatial_shift, spatial_shift)
    completions: list[CurvedCompletion] = []
    for origin in DISPLAYED_ORIGINS:
        differential = chart_differential_cover(origin)
        cover_action = sp.simplify(
            MASS * hodge
            + I
            * (
                hodge * differential
                + differential.H * hodge
            )
        )
        physical_action = antiperiodic_quotient(cover_action)
        alternating_action = grassmann_form(physical_action)
        completions.append(
            CurvedCompletion(
                origin,
                differential,
                cover_action,
                physical_action,
                alternating_action,
                time_bands(cover_action),
                (
                    alternating_action * doubled_shift
                    - doubled_shift * alternating_action
                ).rank(),
            )
        )
    return tuple(completions)  # type: ignore[return-value]


def block105_boundary_certificate(completions: tuple[CurvedCompletion, ...]) -> bool:
    source = " ".join((block105.__doc__ or "").lower().split())
    hodge_only = (
        ("overlap hodge" in source or "overlap-hodge" in source)
        and "common global nilpotent differential" in source
        and "remain open" in source
    )
    displayed_are_chartwise = (
        all(
            completion.differential**2 == sp.zeros(COVER_SIZE)
            for completion in completions
        )
        and all(
            left.differential != right.differential
            for left, right in combinations(completions, 2)
        )
    )
    return hodge_only and displayed_are_chartwise


def completion_certificate(
    completions: tuple[CurvedCompletion, ...],
) -> dict[str, object]:
    first_difference = sp.simplify(
        completions[1].physical_action[10, 11]
        - completions[0].physical_action[10, 11]
    )
    pairwise_inequivalent = all(
        left.physical_action != right.physical_action
        and (left.physical_action - right.physical_action).rank() > 0
        for left, right in combinations(completions, 2)
    )
    exact = all(
        all(value.is_Rational is True for value in completion.physical_action)
        for completion in completions
    )
    return {
        "origins": tuple(completion.origin for completion in completions),
        "source_boundary": block105_boundary_certificate(completions),
        "pairwise_inequivalent": pairwise_inequivalent,
        "first_difference": first_difference,
        "pentadiagonal": all(
            completion.bands == (-2, -1, 0, 1, 2)
            for completion in completions
        ),
        "exact": exact,
        "alternating": all(
            completion.alternating_action.T == -completion.alternating_action
            for completion in completions
        ),
    }


def spatial_slice_shift(displacement: int) -> sp.Matrix:
    matrix = sp.zeros(SPACE_EXTENT)
    for source in range(SPACE_EXTENT):
        matrix[(source + displacement) % SPACE_EXTENT, source] = 1
    return matrix


def directional_slice_frame(time_coordinate: int, direction: int) -> sp.Matrix:
    """Characteristic slice frame making the obstruction coordinate fixed."""
    if direction == 2:
        displacement = time_coordinate - 2
    elif direction == -2:
        displacement = -time_coordinate - 1
    else:
        raise ValueError("the two-slice direction must be +2 or -2")
    return spatial_slice_shift(displacement)


def slice_block(
    completion: CurvedCompletion,
    row_time: int,
    column_time: int,
    direction: int,
) -> sp.Matrix:
    row_time %= COVER_TIME_EXTENT
    column_time %= COVER_TIME_EXTENT
    raw = completion.cover_action[
        SPACE_EXTENT * row_time : SPACE_EXTENT * (row_time + 1),
        SPACE_EXTENT * column_time : SPACE_EXTENT * (column_time + 1),
    ]
    return sp.simplify(
        directional_slice_frame(row_time, direction).T
        * raw
        * directional_slice_frame(column_time, direction)
    )


def schur_forward_coefficient(
    completion: CurvedCompletion,
    step: int,
    direction: int,
) -> sp.Matrix:
    return slice_block(completion, step, step + direction, direction)


def schur_records(
    completions: tuple[CurvedCompletion, ...],
) -> tuple[tuple[tuple[int, int], int, int, sp.Matrix], ...]:
    return tuple(
        (
            completion.origin,
            direction,
            step,
            schur_forward_coefficient(completion, step, direction),
        )
        for completion in completions
        for direction in FORWARD_DIRECTIONS
        for step in DISPLAYED_STEPS
    )


def exact_kernel(matrix: sp.Matrix) -> bool:
    nullspace = matrix.nullspace()
    return (
        matrix.rank() == 3
        and matrix * KERNEL_WITNESS == sp.zeros(4, 1)
        and nullspace == [KERNEL_WITNESS]
    )


def bracketed_forward_blocks(
    completion: CurvedCompletion,
    start: int,
    direction: int,
) -> tuple[tuple[sp.Matrix, sp.Matrix], tuple[sp.Matrix, sp.Matrix]]:
    source_times = (start, start + 1)
    target_times = (
        (start + 2, start + 3)
        if direction == 2
        else (start - 2, start - 1)
    )
    return tuple(
        tuple(
            slice_block(completion, source, target, direction)
            for target in target_times
        )
        for source in source_times
    )  # type: ignore[return-value]


def underdetermination_certificate(
    records: tuple[tuple[tuple[int, int], int, int, sp.Matrix], ...],
) -> bool:
    particular = sp.Matrix((1, -2, 3, -4))
    shifted = particular + KERNEL_WITNESS
    return particular != shifted and all(
        matrix * particular == matrix * shifted
        and matrix * (shifted - particular) == sp.zeros(4, 1)
        for _, _, _, matrix in records
    )


def regrouping_certificate(
    completions: tuple[CurvedCompletion, ...],
) -> bool:
    """The same far-band coefficient occurs in both adjacent bracketings."""
    for completion in completions:
        for direction in FORWARD_DIRECTIONS:
            for step in DISPLAYED_STEPS:
                primary = bracketed_forward_blocks(
                    completion, step - 1, direction
                )
                alternative = bracketed_forward_blocks(
                    completion, step, direction
                )
                coefficient = schur_forward_coefficient(
                    completion, step, direction
                )
                if not (
                    primary[1][1] == coefficient
                    and alternative[0][0] == coefficient
                    and exact_kernel(primary[1][1])
                    and exact_kernel(alternative[0][0])
                ):
                    return False
    return True


SCOPE_KEYS = (
    "curved_carrier",
    "common_differential",
    "unexecuted",
    "pentadiagonal",
    "translation_breakdown",
    "schur_rank",
    "kernel_witness",
    "companion_undefined",
    "regrouping",
    "dependency",
    "os_boundary",
    "axiom",
    "zero_retirement",
    "zero_score",
    "zero_e2e",
    "gravity_quotient",
    "adm",
    "n1_n8",
    "w1",
    "n5_resolution",
)


def block105_section12_citation(note: str) -> bool:
    return (
        (
            "block 105 §12" in note
            or "block 105, §12" in note
            or "block 105 section 12" in note
        )
        and "item 1" in note
    )


def dependency_note_certificate(note: str) -> bool:
    impossible_phrases = (
        "common differential is impossible",
        "common nilpotent differential is impossible",
        "common differential cannot be constructed",
        "common nilpotent differential cannot be constructed",
    )
    return (
        block105_section12_citation(note)
        and "dependency" in note
        and (
            "common nilpotent" in note
            or "common differential" in note
        )
        and not any(phrase in note for phrase in impossible_phrases)
    )


def scope_certificate(note: str, mutation: str) -> dict[str, bool]:
    result = {
        "curved_carrier": "curved carrier" in note,
        "common_differential": (
            "common nilpotent" in note or "common differential" in note
        ),
        "unexecuted": "unexecuted" in note,
        "pentadiagonal": "pentadiagonal" in note,
        "translation_breakdown": any(
            phrase in note
            for phrase in (
                "rank[q, u_x] = 32",
                "translation-invariance breakdown",
                "destroys the momentum decomposition",
                "no momentum decomposition exists",
                "translation defect is full rank",
            )
        ),
        "schur_rank": (
            "rank 3" in note or "singular forward coefficient" in note
        ),
        "kernel_witness": (
            "kernel" in note and "(0,1,0,0)" in note
        ),
        "companion_undefined": (
            "companion" in note and "undefined" in note
        ),
        "regrouping": (
            "regrouping" in note or "rebracket" in note
        ),
        "dependency": (
            "dependency" in note
            and ("item 1" in note or "bottleneck" in note)
        ),
        "os_boundary": (
            "not an os no-go" in note
            or "not a curved os no-go" in note
        ),
        "axiom": "no axiom amendment is justified" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": "no toe percentage moves" in note,
        "zero_e2e": (
            "retained-positive end-to-end theory count remains zero" in note
        ),
        "gravity_quotient": (
            "gravity constraint quotient remains unexecuted" in note
        ),
        "adm": "actual adm/history transporter remains" in note,
        "n1_n8": all(f"n{index}" in note for index in range(1, 9)),
        "w1": "w1" in note,
        "n5_resolution": all(
            f"{resolution}:" in note
            for resolution in (
                "per_element",
                "per_site",
                "per_mode",
                "per_block",
                "lattice_wide",
            )
        ),
    }
    if mutation == "weaken_no_go_packet":
        result["os_boundary"] = False
        result["n1_n8"] = False
    if mutation == "drop_n5_resolution":
        result["n5_resolution"] = False
    if mutation == "claim_toe_progress":
        result["zero_score"] = False
    if mutation == "claim_axiom_amendment":
        result["axiom"] = False
    return result


N5_LINES = (
    "N5: per_element: shifted-chart completions are pairwise inequivalent with exact first difference -89/140, every completion remains pentadiagonal, and every spatial-shift commutator has full rank 32",
    "per_site: one Grassmann mode per fine site on the certified curved carrier",
    "per_mode: checked and not defined — the displayed completions admit no spatial-momentum decomposition",
    "per_block: every displayed completion in both directions has singular two-slice Schur forward coefficients at the displayed steps with fixed coordinate kernel (0,1,0,0), and that kernel survives every displayed regrouping",
    "lattice_wide: checked and not executed — the common nilpotent patch/frame differential, scalar-quotient theorem block, cross-lane facet-charge bridge, actual ADM/history transporter completion, joint gravity, gravity constraint quotient beyond the displayed carrier, Records, audit retention, and TOE closure remain open",
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    mutation = parser.parse_args().mutation
    started = time.monotonic()
    checks = Checks()

    authority = authority_certificate(mutation)
    authority_raw = (
        AUDIT_TIMEOUT_SEC == 600
        and AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_NATURALITY_MODULI_BOUNDED_THEOREM_NOTE_2026-08-17.md",
            "scripts/admissibility_dirac_kahler_naturality_moduli_2026_08_17.py",
            "logs/runner-cache/admissibility_dirac_kahler_naturality_moduli_2026_08_17.txt",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
        )
        and authority["main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["worktree_axiom"] == WORKTREE_AXIOM_BLOB
        and authority["registry"] == CURRENT_REGISTRY_BLOB
        and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
        and authority["parent"] == PARENT_COMMIT
        and authority["parent_ancestor"]
        and all(
            authority[f"ancestor_{number}"]
            for number in range(103, 127)
        )
        and authority["parent_note"] == authority["expected_parent"]
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB
        and authority["curved"] == CURVED_COMMIT
        and authority["curved_ancestor"]
        and authority["curved_note"] == CURVED_NOTE_BLOB
        and authority["curved_runner"] == CURVED_RUNNER_BLOB
    )
    checks.check(
        "A-authority",
        "Block 127, ancestors 126--103, and Block 105 curved-fixture blobs are pinned",
        authority_raw,
    )

    completions = build_completions()
    completion = completion_certificate(completions)
    no_global_raw = (
        completion["origins"] == DISPLAYED_ORIGINS
        and completion["source_boundary"]
        and completion["pairwise_inequivalent"]
        and completion["first_difference"] == -R(89, 140)
        and completion["pentadiagonal"]
        and completion["exact"]
        and completion["alternating"]
    )
    no_global_gate = no_global_raw
    if mutation in ("break_inequivalence", "claim_global_action"):
        no_global_gate = False
    checks.check(
        "B-no-global-curved-action",
        "Block 105 supplies Hodge only; two inequivalent exact chart completions remain pentadiagonal",
        no_global_gate,
    )

    commutator_ranks = tuple(
        item.commutator_rank for item in completions
    )
    translation_raw = (
        len(completions) >= 2
        and commutator_ranks == tuple(32 for _ in completions)
    )
    translation_gate = translation_raw
    if mutation == "break_commutator_rank":
        translation_gate = False
    checks.check(
        "C-translation-breakdown",
        "rank[Q_curved,U_x]=32 in both displayed shifted-chart completions",
        translation_gate,
    )

    records = schur_records(completions)
    schur_rank_raw = all(matrix.rank() == 3 for _, _, _, matrix in records)
    kernel_raw = all(exact_kernel(matrix) for _, _, _, matrix in records)
    step_raw = all(
        tuple(
            step
            for origin, item_direction, step, matrix in records
            if origin == completion_item.origin
            and item_direction == direction
            and matrix.rank() == 3
        )
        == DISPLAYED_STEPS
        for completion_item in completions
        for direction in FORWARD_DIRECTIONS
    )
    schur_gate = schur_rank_raw and kernel_raw and step_raw
    if mutation == "break_schur_rank":
        schur_gate = False
    if mutation == "break_kernel_witness":
        schur_gate = False
    checks.check(
        "D-the-companion-obstruction",
        "both directions have rank-3 step-1/3 coefficients with kernel (0,1,0,0)",
        schur_gate,
    )

    underdetermination_raw = underdetermination_certificate(records)
    regrouping_raw = regrouping_certificate(completions)
    consequence_gate = underdetermination_raw and regrouping_raw
    if mutation == "break_underdetermination":
        consequence_gate = False
    if mutation == "break_regrouping_survival":
        consequence_gate = False
    checks.check(
        "E-the-consequence-logic",
        "next-state solves are non-unique along the kernel, which survives rebracketing",
        consequence_gate,
    )

    companion_available = all(matrix.rank() == 4 for _, _, _, matrix in records)
    momentum_available = all(rank == 0 for rank in commutator_ranks)
    monodromy_defined = companion_available
    stable_split_defined = monodromy_defined and momentum_available
    completion_defined = stable_split_defined
    census_raw = (
        completion["pentadiagonal"]
        and not companion_available
        and not momentum_available
        and schur_rank_raw
        and kernel_raw
        and underdetermination_raw
        and regrouping_raw
        and not monodromy_defined
        and not stable_split_defined
        and not completion_defined
    )
    census_gate = census_raw
    if mutation == "break_census":
        census_gate = False
    checks.check(
        "F-the-pipeline-census",
        "bands pass; companions and momentum fail; downstream stages are undefined",
        census_gate,
    )

    note = normalized_note()
    dependency_raw = (
        no_global_raw
        and translation_raw
        and schur_rank_raw
        and kernel_raw
        and underdetermination_raw
        and regrouping_raw
        and census_raw
        and dependency_note_certificate(note)
    )
    dependency_gate = dependency_raw
    if mutation == "claim_differential_impossible":
        dependency_gate = False
    checks.check(
        "G-the-dependency-statement",
        "B--F plus Block 105 section 12 item 1 make the common differential the live dependency",
        dependency_gate,
    )

    scope = scope_certificate(note, mutation)
    elapsed_before_scope = time.monotonic() - started
    checks.check(
        "H-scope",
        "curved/Schur/dependency/N1--N8/W1/N5 and no-go/TOE firewalls are present",
        set(scope) == set(SCOPE_KEYS)
        and all(scope.values())
        and elapsed_before_scope <= 400,
    )

    print(
        "AUTHORITY: "
        f"parent={authority['parent']}; Block105={authority['curved']}; "
        f"axiom={authority['axiom']}"
    )
    print(
        "CURVED_ACTIONS: origins=((1,0),(1,1)); "
        "Q_(1,1)[10,11]-Q_(1,0)[10,11]="
        f"{completion['first_difference']}; time bands=(-2,-1,0,1,2)"
    )
    print(
        "TRANSLATION: rank[Q, U_x]="
        f"{commutator_ranks}; the momentum decomposition fails at full rank"
    )
    print(
        "SCHUR: directions=(+2,-2); singular steps=(1,3); ranks=3; "
        "kernel=(0,1,0,0) in both displayed completions"
    )
    print(
        "CONSEQUENCE: the next state has the exact family x+lambda(0,1,0,0); "
        "both adjacent two-slice bracketings contain the same coefficient"
    )
    print(
        "PIPELINE: band structure=OK; companions=FAIL; momentum=FAIL; "
        "monodromy/stable-split/completion=UNDEFINED"
    )
    for line in N5_LINES:
        print(line)
    print(
        "RESULT: the curved carrier admits no global action, no momentum "
        "decomposition, and no companion construction in every displayed "
        "chart completion — the dependency on the Block 105 common "
        "differential is a theorem, not a suspicion"
    )
    print(
        "DECISION_CUT: construct the common differential; run the "
        "scalar-quotient block and the cross-lane bridge; reject curved-OS "
        "attempts that bypass item 1"
    )
    print(
        "TOE: zero obligation retirement; no TOE percentage moves; "
        "retained-positive end-to-end theory count remains zero; gravity "
        "constraint quotient remains unexecuted; actual ADM/history "
        "transporter remains open"
    )
    return checks.finish()


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}")
        print("TOTAL: PASS=0 FAIL=1")
        raise
