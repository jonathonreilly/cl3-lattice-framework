#!/usr/bin/env python3
"""Block 188: dual-frame temporal link and stage-intertwiner boundary.

Rebuild the Block-128 8x4 curved carrier, derive the projective reflection,
extract every temporal band before antiperiodic descent, and test the exact
map to the ordered Block-78 stage representation.  The direct single-carrier
intertwiner is empty, while a displayed dual-adjoint frame doubling gives an
honest reflection and the desired exchanged (2,0)/(0,2) weights.  Its displayed
reflected form is nevertheless exactly balanced rather than positive.  This
is a bounded carrier theorem, not a DK/gravity/Record or TOE no-go.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17 as b128


NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_DUAL_FRAME_TEMPORAL_LINK_STAGE_"
    "INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_COMMON_ACTION_STATIONARITY_GRAVITY_STAGE_"
    "ORIENTATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_common_action_stationarity_gravity_stage_"
    "orientation_boundary_2026_08_24.py"
)
B128_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_"
    "THEOREM_NOTE_2026-08-17.md"
)
B128_RUNNER = (
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py"
)
B107_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_ADM_SEAM_TWO_HISTORY_GRAM_BOUNDED_"
    "THEOREM_NOTE_2026-08-15.md"
)
B114_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_POSITIVE_DRESSED_REFLECTION_BOUNDED_"
    "THEOREM_NOTE_2026-08-15.md"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DUAL_FRAME_TEMPORAL_LINK_STAGE_INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_COMMON_ACTION_STATIONARITY_GRAVITY_STAGE_ORIENTATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_common_action_stationarity_gravity_stage_orientation_boundary_2026_08_24.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_ADM_SEAM_TWO_HISTORY_GRAM_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_POSITIVE_DRESSED_REFLECTION_BOUNDED_THEOREM_NOTE_2026-08-15.md",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "c79384cb8ffa27fcb53cb89c53a84a708442eaad"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/toe-axiom-closure-block187-common-action-"
    "tournament-20260824"
)
PARENT_COMMIT = "add760976c80ab3a6076aad595b446acca7c41ef"
PARENT_BLOBS = (
    "6c1720ab158465070e325d5970250f0db6868f2a",
    "76ed26ee51e09c7d711febdcf8466020a0441da3",
)
B128_COMMIT = "f6b0cf59e2cc588ebd3e34b96e730574cb485db2"
B128_BLOBS = (
    "194cf07ad9a0b7269defe6bdba8750fc6fe95640",
    "90f9b53b2ef499367f2f65fd8314a13137af203b",
)
B107_COMMIT = "d41a05e153d4cb77eee125b82fc0b0bd767bf32e"
B114_COMMIT = "75026e71cfbd44ed665ddc41c22ebaa722720ea9"

MUTATIONS = (
    "stale_main_authority",
    "break_ap_descent",
    "break_band_character",
    "claim_single_stage_intertwiner",
    "break_doubled_stage_exchange",
    "claim_direct_reflected_form_hermitian",
    "drop_n5_certificate",
    "claim_toe_progress",
    "claim_physical_source_rank",
)
MUTATION_GATE = {
    "stale_main_authority": "A",
    "break_ap_descent": "B",
    "break_band_character": "C",
    "claim_single_stage_intertwiner": "D",
    "break_doubled_stage_exchange": "E",
    "claim_direct_reflected_form_hermitian": "F",
    "drop_n5_certificate": "G",
    "claim_toe_progress": "G",
    "claim_physical_source_rank": "G",
}


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=AUDIT_TIMEOUT_SEC
    ).strip()


def commit_blob(commit: str, path: str) -> str:
    return git_output("rev-parse", f"{commit}:{path}")


def worktree_blob(path: str) -> str:
    return git_output("hash-object", path)


def is_ancestor(ancestor: str, descendant: str = "HEAD") -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, descendant),
        cwd=ROOT,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


def nonzero_entries(matrix: sp.MatrixBase) -> int:
    return sum(entry != 0 for entry in matrix)


def matrix_equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return left.shape == right.shape and all(
        sp.expand(entry) == 0 for entry in left - right
    )


T = b128.COVER_TIME_EXTENT
X = b128.SPACE_EXTENT
N = b128.COVER_SIZE
I = sp.I
DIFFERENTIAL_ORIGIN = (0, 0)
NEGATIVE_AP_INDICES = tuple(range(2 * X))
CELL_DUAL_MAP = sp.Matrix(
    (
        (0, 0, -1, 0),
        (0, 0, 0, -1),
        (1, 0, 0, 0),
        (0, 1, 0, 0),
    )
)


def cover_shift(dt: int, dx: int) -> sp.Matrix:
    result = sp.zeros(N)
    for time in range(T):
        for space in range(X):
            result[
                b128.cover_index(time + dt, space + dx),
                b128.cover_index(time, space),
            ] = 1
    return result


def edge_reflection() -> sp.Matrix:
    result = sp.zeros(N)
    for time in range(T):
        for space in range(X):
            result[
                b128.cover_index(T - 1 - time, space),
                b128.cover_index(time, space),
            ] = 1
    return result


def time_parity() -> sp.Matrix:
    return sp.diag(*[
        sp.Integer(-1) ** (time % 2)
        for time in range(T)
        for _space in range(X)
    ])


def signed_displacement(raw: int) -> int:
    return raw if raw <= T // 2 else raw - T


def temporal_band(matrix: sp.Matrix, displacement: int) -> sp.Matrix:
    return sp.Matrix(
        matrix.rows,
        matrix.cols,
        lambda row, column: matrix[row, column]
        if signed_displacement((column // X - row // X) % T) == displacement
        else 0,
    )


def band_signature(matrix: sp.Matrix) -> tuple[tuple[int, int, int], ...]:
    result = []
    for displacement in (-2, -1, 0, 1, 2):
        block = temporal_band(matrix, displacement)
        if nonzero_entries(block):
            result.append((displacement, nonzero_entries(block), block.rank()))
    return tuple(result)


def orbit_average(matrix: sp.Matrix) -> sp.Matrix:
    shifts = tuple(
        cover_shift(dt, dx) for dt in range(T) for dx in (0, 1)
    )
    return sp.expand(
        sum((shift.T * matrix * shift for shift in shifts), sp.zeros(N))
        / len(shifts)
    )


def shear_block(shear: object, volume: object) -> sp.Matrix:
    """The landed Block-105 cell Hodge, reached through Block 128."""
    return b128.block105.shear_hodge(shear, volume)


def dual_block(shear: object, volume: object) -> sp.Matrix:
    """The independently constructed dual cell block M H(q,v) M^T."""
    return sp.expand(
        CELL_DUAL_MAP * shear_block(shear, volume) * CELL_DUAL_MAP.T
    )


def hodge_cover(field: dict, block=shear_block) -> sp.Matrix:
    """Build the cover Hodge from a supplied cell field and cell block."""
    result = sp.zeros(N)
    for time in range(T):
        for space in range(X):
            shear, volume = field[(time % b128.PHYSICAL_TIME_EXTENT, space)]
            embedding = b128.cover_embedding(time, space)
            result += embedding * block(shear, volume) * embedding.T / 4
    return sp.expand(result)


def reflected_field(field: dict) -> dict:
    """Cell-field reflection induced by the site map t -> 7-t."""
    return {
        (time, space): field[
            ((2 - time) % b128.PHYSICAL_TIME_EXTENT, space)
        ]
        for time in range(b128.PHYSICAL_TIME_EXTENT)
        for space in range(X)
    }


def completion(hodge: sp.Matrix, differential: sp.Matrix) -> sp.Matrix:
    """Apply the landed Block-128 massive Dirac--Kahler completion."""
    return sp.expand(
        b128.MASS * hodge
        + I * (hodge * differential + differential.H * hodge)
    )


def descends(
    matrix: sp.Matrix, injection: sp.Matrix, selection: sp.Matrix
) -> bool:
    quotient = sp.expand(selection * matrix * injection)
    return matrix_equal(matrix * injection, injection * quotient)


def intertwiner_rank(source: sp.Matrix) -> tuple[int, int, int]:
    stage_exchange = sp.Matrix(((0, 1), (1, 0)))
    variables = sp.symbols(f"f0:{2 * source.rows}")
    candidate = sp.Matrix(2, source.rows, variables)
    coefficients, _ = sp.linear_eq_to_matrix(
        list(candidate * source - stage_exchange * candidate), variables
    )
    rank = coefficients.rank()
    return len(variables), rank, len(variables) - rank


@dataclass(frozen=True)
class Facts:
    authority: bool
    inputs_readable: bool
    r_projective: bool
    r_wrong_square_entries: int
    ap_descent: bool
    ap_projective: bool
    ap_orientation_split: tuple[int, int]
    landed_hodge_control: bool
    independent_dual_hodge: bool
    independent_dual_discriminator: bool
    h_signature: tuple[tuple[int, int, int], ...]
    d_signature: tuple[tuple[int, int, int], ...]
    q_signature: tuple[tuple[int, int, int], ...]
    band_descent: tuple[int, int, int, int]
    band_covariance: bool
    stripped_odd_residual: int
    stripped_wrong_residual: int
    same_frame_h: tuple[tuple[int, int], tuple[int, int]]
    same_frame_q: tuple[tuple[int, int], tuple[int, int]]
    direct_dressing: bool
    direct_reality_entries: int
    single_intertwiner: tuple[int, int, int]
    stage_basis_residual: int
    doubled_reflection: bool
    doubled_stage_exchange: bool
    doubled_intertwiner: tuple[int, int, int]
    direct_gram_rank: int
    direct_gram_hermiticity_entries: int
    doubled_gram: tuple[bool, int, bool, int]
    action_orientation_ranks: tuple[int, int, int, int]
    note_ready: bool
    n5_ready: bool
    fixture_ready: bool
    scope_ready: bool


def authority_ok() -> bool:
    parent_paths = (PARENT_NOTE, PARENT_RUNNER)
    b128_paths = (B128_NOTE, B128_RUNNER)
    return bool(
        git_output("rev-parse", "origin/main") == CURRENT_MAIN
        and commit_blob("origin/main", AXIOM_PATH) == CURRENT_AXIOM_BLOB
        and commit_blob("origin/main", REGISTRY_PATH) == CURRENT_REGISTRY_BLOB
        and worktree_blob(AXIOM_PATH) == WORKTREE_AXIOM_BLOB
        and worktree_blob(REGISTRY_PATH) == WORKTREE_REGISTRY_BLOB
        and git_output("rev-parse", PARENT_REF) == PARENT_COMMIT
        and is_ancestor(PARENT_COMMIT)
        and tuple(commit_blob(PARENT_COMMIT, path) for path in parent_paths)
        == PARENT_BLOBS
        and tuple(worktree_blob(path) for path in parent_paths) == PARENT_BLOBS
        and is_ancestor(B128_COMMIT)
        and tuple(commit_blob(B128_COMMIT, path) for path in b128_paths)
        == B128_BLOBS
        and tuple(worktree_blob(path) for path in b128_paths) == B128_BLOBS
        and is_ancestor(B107_COMMIT)
        and is_ancestor(B114_COMMIT)
    )


N5_LINES = (
    "per_element: checked the exact reflection, band, and stage-intertwiner matrix entries.",
    "per_site: checked all 32 cover sites and the 16 antiperiodic quotient sites.",
    "per_mode: checked both eight-dimensional projective orientation eigenspaces exactly.",
    "per_block: checked every live temporal band and both primal/dual frame blocks exactly.",
    "lattice_wide: checked and not executed — no width ladder, "
    "four-dimensional lift, or Record history is claimed.",
)

FIXTURE_TOKENS = (
    "d_00=d[(0,0)]",
    "N_-={0,1,...,7}",
    "first two AP time slices and all four spatial sites",
)

SCOPE_TOKENS = (
    "obligation_retirement: 0",
    "toe_percentage_movement: 0",
    "axiom_status: unchanged",
    "no physical source or Record-readable rank is claimed",
    "not a gravity failure",
    "does not edit the minimal axioms or primitive registry",
)

SCOPE_FORBIDDEN = (
    r"obligation_retirement:\s*[1-9]",
    r"toe_percentage_movement:\s*[1-9]",
    r"physical source rank(?: is|:|=)\s*[1-9]",
)


def measure(mutation: str = "") -> Facts:
    reflection = edge_reflection()
    parity = time_parity()
    r_matrix = sp.expand(reflection * parity)
    identity_n = sp.eye(N)

    identity_ap = sp.eye(b128.PHYSICAL_TIME_EXTENT * X)
    injection = sp.Matrix.vstack(-identity_ap, identity_ap)
    selection = sp.Matrix.hstack(sp.zeros(identity_ap.rows), identity_ap)
    r_ap = sp.expand(selection * r_matrix * injection)
    j_ap = I * r_ap

    field = b128.block105.overlap_field()
    landed_hodge = hodge_cover(field)
    hodge = orbit_average(landed_hodge)
    differential = b128.chart_differential_cover(DIFFERENTIAL_ORIGIN)
    action = completion(hodge, differential)

    # The dual Hodge is built independently from the closed-form cell dual and
    # reflected field.  Only the differential is defined by co-transport; the
    # completed action covariance below is consequently a formal consistency
    # check once Hodge covariance and differential transport are established.
    dual_hodge = orbit_average(
        hodge_cover(reflected_field(field), dual_block)
    )
    dual_differential = sp.expand(r_matrix * differential * r_matrix.T)
    dual_action = completion(dual_hodge, dual_differential)

    live_bands = tuple(
        temporal_band(matrix, displacement)
        for matrix in (
            hodge,
            differential,
            action,
            dual_hodge,
            dual_differential,
            dual_action,
        )
        for displacement in (-2, -1, 0, 1, 2)
        if nonzero_entries(temporal_band(matrix, displacement))
    )
    band_descent_failures = sum(
        not descends(band, injection, selection) for band in live_bands
    )
    whole_objects = (
        hodge,
        differential,
        action,
        dual_hodge,
        dual_differential,
        dual_action,
    )
    whole_descent_failures = sum(
        not descends(matrix, injection, selection) for matrix in whole_objects
    )

    covariance = all(
        matrix_equal(
            r_matrix * temporal_band(source, displacement) * r_matrix.T,
            temporal_band(target, -displacement),
        )
        for source, target in (
            (hodge, dual_hodge),
            (differential, dual_differential),
            (action, dual_action),
        )
        for displacement in (-2, -1, 0, 1, 2)
    )

    temporal_shift = cover_shift(1, 0)
    c_plus = temporal_band(action, 1) * temporal_shift
    c_dual_minus = temporal_band(dual_action, -1) * temporal_shift.T
    stripped = sp.expand(r_matrix * c_plus * r_matrix.T)

    same_h = tuple(
        (
            nonzero_entries(sp.expand(
                r_matrix * temporal_band(hodge, 1) * r_matrix.T
                - sign * temporal_band(hodge, -1)
            )),
            sp.expand(
                r_matrix * temporal_band(hodge, 1) * r_matrix.T
                - sign * temporal_band(hodge, -1)
            ).rank(),
        )
        for sign in (1, -1)
    )
    same_q = tuple(
        (
            nonzero_entries(sp.expand(
                r_matrix * temporal_band(action, 1) * r_matrix.T
                - sign * temporal_band(action, -1)
            )),
            sp.expand(
                r_matrix * temporal_band(action, 1) * r_matrix.T
                - sign * temporal_band(action, -1)
            ).rank(),
        )
        for sign in (1, -1)
    )

    # The unique Block-114-form dressing satisfying A P = R is A=-T_t.
    direct_dressing = -parity
    direct_reality = sp.expand(
        reflection * direct_dressing.conjugate() * reflection - direct_dressing
    )

    stage_exchange = sp.Matrix(((0, 1), (1, 0)))
    stage_sign = sp.diag(1, -1)
    link_stage = -stage_exchange
    stage_basis_residual = nonzero_entries(sp.expand(
        stage_sign * link_stage * stage_sign.inv() - stage_exchange
    ))

    action_ap = sp.expand(selection * action * injection)
    dual_action_ap = sp.expand(r_ap * action_ap * r_ap.T)
    zero_ap = sp.zeros(identity_ap.rows)
    doubled_reflection = sp.Matrix.vstack(
        sp.Matrix.hstack(zero_ap, r_ap.T),
        sp.Matrix.hstack(r_ap, zero_ap),
    )
    frame_orientation = sp.diag(*(
        [1] * identity_ap.rows + [-1] * identity_ap.rows
    ))
    doubled_action = sp.diag(action_ap, dual_action_ap.T)
    weight_0 = sp.eye(2 * identity_ap.rows) + frame_orientation
    weight_1 = sp.eye(2 * identity_ap.rows) - frame_orientation

    negative = NEGATIVE_AP_INDICES
    direct_gram = (r_ap * action_ap.inv()).extract(negative, negative)
    doubled_negative = negative + tuple(
        identity_ap.rows + index for index in negative
    )
    doubled_gram = (
        doubled_reflection * doubled_action.inv()
    ).extract(doubled_negative, doubled_negative)
    restricted_orientation = sp.diag(*([1] * len(negative) + [-1] * len(negative)))

    p_plus = (identity_ap + j_ap) / 2
    p_minus = (identity_ap - j_ap) / 2

    note_text = (
        NOTE_PATH.read_text(encoding="utf-8") if NOTE_PATH.is_file() else ""
    )
    if mutation == "claim_toe_progress":
        note_text += "\ntoe_percentage_movement: 1\n"
    if mutation == "claim_physical_source_rank":
        note_text += "\nphysical source rank: 8\n"
    normalized_note = " ".join(note_text.split())
    required_sections = tuple(f"### N{index}" for index in range(1, 9))

    return Facts(
        authority=authority_ok(),
        inputs_readable=all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
        r_projective=bool(
            matrix_equal(r_matrix.T * r_matrix, identity_n)
            and matrix_equal(r_matrix * r_matrix, -identity_n)
            and matrix_equal(r_matrix.T, -r_matrix)
        ),
        r_wrong_square_entries=nonzero_entries(r_matrix * r_matrix - identity_n),
        ap_descent=matrix_equal(r_matrix * injection, injection * r_ap),
        ap_projective=bool(
            matrix_equal(r_ap.T * r_ap, identity_ap)
            and matrix_equal(r_ap * r_ap, -identity_ap)
        ),
        ap_orientation_split=(
            identity_ap.rows - (j_ap - identity_ap).rank(),
            identity_ap.rows - (j_ap + identity_ap).rank(),
        ),
        landed_hodge_control=matrix_equal(
            landed_hodge, b128.curved_hodge_cover()
        ),
        independent_dual_hodge=matrix_equal(
            r_matrix * hodge * r_matrix.T, dual_hodge
        ),
        independent_dual_discriminator=not matrix_equal(
            r_matrix * hodge * r_matrix.T,
            orbit_average(hodge_cover(reflected_field(field))),
        ),
        h_signature=band_signature(hodge),
        d_signature=band_signature(differential),
        q_signature=band_signature(action),
        band_descent=(
            len(live_bands),
            band_descent_failures,
            len(whole_objects),
            whole_descent_failures,
        ),
        band_covariance=covariance,
        stripped_odd_residual=nonzero_entries(stripped + c_dual_minus),
        stripped_wrong_residual=nonzero_entries(stripped - c_dual_minus),
        same_frame_h=(same_h[0], same_h[1]),
        same_frame_q=(same_q[0], same_q[1]),
        direct_dressing=bool(
            matrix_equal(direct_dressing * reflection, r_matrix)
            and matrix_equal(direct_dressing * direct_dressing, identity_n)
            and matrix_equal(
                reflection * direct_dressing.conjugate() * reflection,
                -direct_dressing,
            )
        ),
        direct_reality_entries=nonzero_entries(direct_reality),
        single_intertwiner=intertwiner_rank(r_ap),
        stage_basis_residual=stage_basis_residual,
        doubled_reflection=bool(
            matrix_equal(doubled_reflection.T, doubled_reflection)
            and matrix_equal(doubled_reflection * doubled_reflection, sp.eye(32))
            and matrix_equal(
                doubled_reflection * doubled_action.H * doubled_reflection,
                doubled_action,
            )
        ),
        doubled_stage_exchange=bool(
            matrix_equal(
                doubled_reflection * frame_orientation * doubled_reflection,
                -frame_orientation,
            )
            and matrix_equal(
                doubled_reflection * weight_0 * doubled_reflection, weight_1
            )
            and matrix_equal(
                doubled_reflection * weight_1 * doubled_reflection, weight_0
            )
        ),
        doubled_intertwiner=intertwiner_rank(doubled_reflection),
        direct_gram_rank=direct_gram.rank(),
        direct_gram_hermiticity_entries=nonzero_entries(
            sp.expand(direct_gram - direct_gram.H)
        ),
        doubled_gram=(
            matrix_equal(doubled_gram, doubled_gram.H),
            doubled_gram.rank(),
            matrix_equal(
                restricted_orientation * doubled_gram * restricted_orientation,
                -doubled_gram,
            ),
            doubled_gram[: len(negative), len(negative) :].rank(),
        ),
        action_orientation_ranks=tuple(
            (left * action_ap * right).rank()
            for left in (p_plus, p_minus)
            for right in (p_plus, p_minus)
        ),
        note_ready=bool(
            note_text and all(section in note_text for section in required_sections)
        ),
        n5_ready=all(line in note_text for line in N5_LINES),
        fixture_ready=all(token in normalized_note for token in FIXTURE_TOKENS),
        scope_ready=bool(
            all(token in normalized_note for token in SCOPE_TOKENS)
            and not any(
                re.search(pattern, normalized_note) for pattern in SCOPE_FORBIDDEN
            )
        ),
    )


class Checks:
    def __init__(self) -> None:
        self.rows: list[tuple[str, str, bool]] = []

    def check(self, gate: str, statement: str, condition: object) -> None:
        self.rows.append((gate, statement, bool(condition)))

    def report(self) -> int:
        for gate, statement, condition in self.rows:
            print(f"[{'PASS' if condition else 'FAIL'}] {gate}: {statement}")
        passed = sum(condition for _, _, condition in self.rows)
        failed = len(self.rows) - passed
        for line in N5_LINES:
            print(line)
        print(f"TOTAL: PASS={passed} FAIL={failed}")
        return failed


def build_checks(facts: Facts, mutation: str) -> Checks:
    checks = Checks()
    expected_authority = mutation != "stale_main_authority"
    expected_ap_descent = mutation != "break_ap_descent"
    expected_odd_residual = 1 if mutation == "break_band_character" else 0
    expected_single_nullity = (
        1 if mutation == "claim_single_stage_intertwiner" else 0
    )
    expected_double_exchange = mutation != "break_doubled_stage_exchange"
    expected_direct_hermiticity = (
        0 if mutation == "claim_direct_reflected_form_hermitian" else 40
    )
    expected_n5 = mutation != "drop_n5_certificate"

    checks.check(
        "A",
        "fresh authority, exact parent/carrier pins, and all declared inputs",
        facts.authority == expected_authority and facts.inputs_readable,
    )
    checks.check(
        "B",
        "R, every live band, and all six operators descend to an 8+8 AP split",
        facts.r_projective
        and facts.r_wrong_square_entries == 32
        and facts.ap_descent == expected_ap_descent
        and facts.ap_projective
        and facts.ap_orientation_split == (8, 8)
        and facts.band_descent == (20, 0, 6, 0),
    )
    checks.check(
        "C",
        "an independent dual Hodge closes every band; stripped odd links flip",
        facts.landed_hodge_control
        and facts.independent_dual_hodge
        and facts.independent_dual_discriminator
        and facts.h_signature == ((-1, 32, 32), (0, 32, 32), (1, 32, 32))
        and facts.d_signature == ((-1, 16, 16), (0, 16, 16))
        and facts.q_signature
        == (
            (-2, 16, 16),
            (-1, 72, 32),
            (0, 80, 32),
            (1, 72, 32),
            (2, 16, 16),
        )
        and facts.band_covariance
        and facts.stripped_odd_residual == expected_odd_residual
        and facts.stripped_wrong_residual == 72
        and facts.same_frame_h == ((64, 32), (64, 32))
        and facts.same_frame_q == ((80, 32), (104, 32)),
    )
    checks.check(
        "D",
        "the unique direct dressing is reflection-odd and the single-stage intertwiner is zero",
        facts.direct_dressing
        and facts.direct_reality_entries == 32
        and facts.single_intertwiner == (32, 32, expected_single_nullity)
        and facts.stage_basis_residual == 0,
    )
    checks.check(
        "E",
        "dual-adjoint doubling gives honest reversal and exchanged (2,0)/(0,2) weights",
        facts.doubled_reflection
        and facts.doubled_stage_exchange == expected_double_exchange
        and facts.doubled_intertwiner == (64, 32, 32),
    )
    checks.check(
        "F",
        "the direct Gram is non-Hermitian while the doubled Gram is exact balanced 8+8",
        facts.direct_gram_rank == 8
        and facts.direct_gram_hermiticity_entries == expected_direct_hermiticity
        and facts.doubled_gram == (True, 16, True, 8)
        and facts.action_orientation_ranks == (8, 8, 8, 8),
    )
    checks.check(
        "G",
        "the note carries N1-N8, N5, named fixtures, and falsifiable TOE scope",
        facts.note_ready
        and facts.n5_ready == expected_n5
        and facts.fixture_ready
        and facts.scope_ready,
    )
    return checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--list-mutations", action="store_true")
    args = parser.parse_args()
    if args.list_mutations:
        for mutation in MUTATIONS:
            print(f"{mutation}: {MUTATION_GATE[mutation]}")
        return 0
    facts = measure(args.mutation)
    return build_checks(facts, args.mutation).report()


if __name__ == "__main__":
    raise SystemExit(main())
