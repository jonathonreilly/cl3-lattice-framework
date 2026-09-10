#!/usr/bin/env python3
"""Block 189: stage-exchange, positive dressing, and source-port boundary.

Work on the exact doubled antiperiodic action of Block 188.  Prove the
grading obstruction for every stage-exchanging dressing on the declared
history support, construct an exact positive dressing that escapes by changing
the stage character, construct a second exact positive dressing with genuinely
mixed stage character, and classify scalar versus matrix graph-port escapes.
This is a bounded finite-carrier theorem, not a physical source, gravity,
Record, OS-reconstruction, axiom, or TOE result.
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

import admissibility_dirac_kahler_dual_frame_temporal_link_stage_intertwiner_boundary_2026_08_24 as b188


NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_STAGE_EXCHANGE_POSITIVE_DRESSING_SOURCE_"
    "PORT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DUAL_FRAME_TEMPORAL_LINK_STAGE_"
    "INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_dual_frame_temporal_link_stage_"
    "intertwiner_boundary_2026_08_24.py"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_STAGE_EXCHANGE_POSITIVE_DRESSING_SOURCE_PORT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DUAL_FRAME_TEMPORAL_LINK_STAGE_INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_dirac_kahler_dual_frame_temporal_link_stage_intertwiner_boundary_2026_08_24.py",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "c79384cb8ffa27fcb53cb89c53a84a708442eaad"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/toe-axiom-closure-block188-dual-frame-temporal-"
    "link-20260824"
)
PARENT_COMMIT = "a4c36311dc393e17649cec581cd609650d5ab27e"
PARENT_BLOBS = (
    "e7127115762e59df75e776d855563ed4b99ff4e3",
    "bd93f1e886ff85339ead3148b1ca213958e16743",
)

MUTATIONS = (
    "stale_main_authority",
    "break_stage_grading",
    "claim_positive_stage_exchange",
    "break_positive_dressing",
    "claim_positive_dressing_exchanges_stage",
    "break_mixed_positive_dressing",
    "claim_mixed_pure_stage",
    "claim_scalar_port_positive",
    "claim_graph_port_covariant",
    "claim_toe_progress",
    "claim_physical_source_rank",
)
MUTATION_GATE = {
    "stale_main_authority": "A",
    "break_stage_grading": "B",
    "claim_positive_stage_exchange": "C",
    "break_positive_dressing": "D",
    "claim_positive_dressing_exchanges_stage": "D",
    "break_mixed_positive_dressing": "D",
    "claim_mixed_pure_stage": "D",
    "claim_scalar_port_positive": "E",
    "claim_graph_port_covariant": "F",
    "claim_toe_progress": "G",
    "claim_physical_source_rank": "G",
}

I = sp.I
AP_DIMENSION = b188.b128.PHYSICAL_TIME_EXTENT * b188.X
FRAME_DIMENSION = 2 * AP_DIMENSION
NEGATIVE_AP_INDICES = b188.NEGATIVE_AP_INDICES
DOUBLED_NEGATIVE_INDICES = NEGATIVE_AP_INDICES + tuple(
    AP_DIMENSION + index for index in NEGATIVE_AP_INDICES
)


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


def authority_ok() -> bool:
    parent_paths = (PARENT_NOTE, PARENT_RUNNER)
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
    )


@dataclass(frozen=True)
class Fixture:
    injection: sp.Matrix
    selection: sp.Matrix
    reflection_ap: sp.Matrix
    action_ap: sp.Matrix
    doubled_reflection: sp.Matrix
    doubled_action: sp.Matrix
    frame_grading: sp.Matrix
    reflected_kernel: sp.Matrix
    history_embedding: sp.Matrix
    history_grading: sp.Matrix
    raw_history_gram: sp.Matrix


def doubled_fixture() -> Fixture:
    identity_ap = sp.eye(AP_DIMENSION)
    injection = sp.Matrix.vstack(-identity_ap, identity_ap)
    selection = sp.Matrix.hstack(sp.zeros(AP_DIMENSION), identity_ap)

    reflection = sp.expand(b188.edge_reflection() * b188.time_parity())
    reflection_ap = sp.expand(selection * reflection * injection)

    field = b188.b128.block105.overlap_field()
    hodge = b188.orbit_average(b188.hodge_cover(field))
    differential = b188.b128.chart_differential_cover(
        b188.DIFFERENTIAL_ORIGIN
    )
    action = b188.completion(hodge, differential)
    action_ap = sp.expand(selection * action * injection)
    dual_action_ap = sp.expand(
        reflection_ap * action_ap * reflection_ap.T
    )

    zero_ap = sp.zeros(AP_DIMENSION)
    doubled_reflection = sp.Matrix.vstack(
        sp.Matrix.hstack(zero_ap, reflection_ap.T),
        sp.Matrix.hstack(reflection_ap, zero_ap),
    )
    doubled_action = sp.diag(action_ap, dual_action_ap.T)
    frame_grading = sp.diag(sp.eye(AP_DIMENSION), -sp.eye(AP_DIMENSION))
    reflected_kernel = sp.expand(doubled_reflection * doubled_action.inv())

    history_embedding = sp.eye(FRAME_DIMENSION)[
        :, list(DOUBLED_NEGATIVE_INDICES)
    ]
    history_grading = sp.expand(
        history_embedding.T * frame_grading * history_embedding
    )
    raw_history_gram = sp.expand(
        history_embedding.T * reflected_kernel * history_embedding
    )
    return Fixture(
        injection=injection,
        selection=selection,
        reflection_ap=reflection_ap,
        action_ap=action_ap,
        doubled_reflection=doubled_reflection,
        doubled_action=doubled_action,
        frame_grading=frame_grading,
        reflected_kernel=reflected_kernel,
        history_embedding=history_embedding,
        history_grading=history_grading,
        raw_history_gram=raw_history_gram,
    )


@dataclass(frozen=True)
class Facts:
    authority: bool
    inputs_readable: bool
    stage_structure: tuple[bool, bool, bool, bool]
    raw_structure: tuple[bool, int, bool, int, int, int, int]
    changed_frame_control: tuple[int, int, int, int, bool, bool, int, int]
    positive_dressing: tuple[bool, bool, bool, bool, bool, bool, bool, int]
    mixed_positive_dressing: tuple[
        bool, bool, bool, bool, bool, bool, int, int, int, int
    ]
    tested_shift_context: tuple[int, int, int, int]
    dressing_shift_defects: tuple[int, int, int, int]
    scalar_ports: tuple[object, object, int, int, int]
    matrix_ports: tuple[bool, bool, int, int, int, int, int, int]
    note_ready: bool
    n5_ready: bool
    fixture_ready: bool
    scope_ready: bool


N5_LINES = (
    "per_element: checked the exact doubled reflection, action, grading, dressings, and Gram entries.",
    "per_site: checked the declared two-slice AP history support in both frames and both graph ports.",
    "per_mode: checked the full stage-grading pair and the eight-dimensional graph-port fibers exactly.",
    "per_block: checked the raw off-diagonal block, the positive factorization, and both shift commutators exactly.",
    "lattice_wide: checked and not executed — no width ladder, long-history OS reconstruction, gravity quotient, or Record write is claimed.",
)

FIXTURE_TOKENS = (
    "K=S Qcal^-1",
    "Gamma=diag(I_16,-I_16)",
    "E_N selects {0,...,7} in each frame",
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
    fixture = doubled_fixture()
    identity_frame = sp.eye(FRAME_DIMENSION)
    identity_history_half = sp.eye(len(NEGATIVE_AP_INDICES))
    zero_history_half = sp.zeros(len(NEGATIVE_AP_INDICES))

    S = fixture.doubled_reflection
    Qcal = fixture.doubled_action
    Gamma = fixture.frame_grading
    K = fixture.reflected_kernel
    EN = fixture.history_embedding
    E = fixture.history_grading
    C = fixture.raw_history_gram

    half = len(NEGATIVE_AP_INDICES)
    Z = C[:half, half:]
    canonical_c = sp.Matrix.vstack(
        sp.Matrix.hstack(zero_history_half, Z),
        sp.Matrix.hstack(Z.H, zero_history_half),
    )

    # Independently reconstruct PR #7350's named minimal reflection-closed
    # frame without importing that parallel branch.  This is a changed-frame
    # control only: Block 189's load-bearing action remains the full orbit.
    field = b188.b128.block105.overlap_field()
    landed_hodge = b188.hodge_cover(field)
    full_hodge = b188.orbit_average(landed_hodge)
    cover_space_shift = b188.cover_shift(0, 1)
    minimal_hodge = sp.expand(
        (landed_hodge + cover_space_shift.T * landed_hodge * cover_space_shift)
        / 2
    )
    differential = b188.b128.chart_differential_cover(
        b188.DIFFERENTIAL_ORIGIN
    )
    full_action = b188.completion(full_hodge, differential)
    minimal_action = b188.completion(minimal_hodge, differential)
    minimal_action_ap = sp.expand(
        fixture.selection * minimal_action * fixture.injection
    )
    minimal_dual_action_ap = sp.expand(
        fixture.reflection_ap * minimal_action_ap * fixture.reflection_ap.T
    )
    minimal_doubled_action = sp.diag(
        minimal_action_ap, minimal_dual_action_ap.T
    )
    minimal_kernel = sp.expand(S * minimal_doubled_action.inv())
    minimal_history_gram = sp.expand(EN.T * minimal_kernel * EN)
    minimal_z = minimal_history_gram[:half, half:]

    W = EN.row_join(S * EN)
    exchange_history = sp.Matrix.vstack(
        sp.Matrix.hstack(sp.zeros(2 * half), sp.eye(2 * half)),
        sp.Matrix.hstack(sp.eye(2 * half), sp.zeros(2 * half)),
    )
    XZ = sp.Matrix.vstack(
        sp.Matrix.hstack(zero_history_half, Z.H.inv()),
        sp.Matrix.hstack(Z.H, zero_history_half),
    )
    AZ = sp.expand(W * sp.diag(XZ, XZ.conjugate()) * W.T)
    theta_z = sp.expand(AZ * S)
    dressed_gram = sp.expand(EN.T * AZ * K * EN)
    positive_target = sp.diag(identity_history_half, Z.H * Z)

    # A same-carrier mixed-stage counterroute to any pure-character dichotomy.
    # The rational hyperbolic pair obeys a^2-b^2=1 and a>|b|, so the
    # central Hermitian factor below has eigenvalues a+-b > 0.
    mixed_a = sp.Rational(5, 3)
    mixed_b = sp.Rational(4, 3)
    mixed_y = sp.Matrix.vstack(
        sp.Matrix.hstack(
            -I * mixed_b * identity_history_half,
            mixed_a * Z.H.inv(),
        ),
        sp.Matrix.hstack(
            mixed_a * Z.H,
            I * mixed_b * identity_history_half,
        ),
    )
    mixed_A = sp.expand(
        W * sp.diag(mixed_y, mixed_y.conjugate()) * W.T
    )
    mixed_theta = sp.expand(mixed_A * S)
    mixed_gram = sp.expand(EN.T * mixed_A * K * EN)
    mixed_target = sp.Matrix.vstack(
        sp.Matrix.hstack(
            mixed_a * identity_history_half,
            -I * mixed_b * Z,
        ),
        sp.Matrix.hstack(
            I * mixed_b * Z.H,
            mixed_a * Z.H * Z,
        ),
    )

    space_shift_ap = sp.expand(
        fixture.selection * b188.cover_shift(0, 1) * fixture.injection
    )
    time_shift_ap = sp.expand(
        fixture.selection * b188.cover_shift(1, 0) * fixture.injection
    )
    doubled_space_shift = sp.diag(space_shift_ap, space_shift_ap)
    doubled_time_shift = sp.diag(time_shift_ap, time_shift_ap)
    action_space_defect = sp.expand(
        fixture.action_ap * space_shift_ap
        - space_shift_ap * fixture.action_ap
    )
    action_time_defect = sp.expand(
        fixture.action_ap * time_shift_ap
        - time_shift_ap * fixture.action_ap
    )
    az_space_defect = sp.expand(
        AZ * doubled_space_shift - doubled_space_shift * AZ
    )
    az_time_defect = sp.expand(
        AZ * doubled_time_shift - doubled_time_shift * AZ
    )
    mixed_basis_grading = sp.diag(E, -E)
    mixed_y_commutator = sp.expand(
        mixed_y * E - E * mixed_y
    )
    mixed_y_anticommutator = sp.expand(
        mixed_y * E + E * mixed_y
    )

    hermitian_scalar_real = sp.expand(Z + Z.H)
    hermitian_scalar_imag = sp.expand(I * (Z - Z.H))
    scalar_span = sp.Matrix.hstack(
        hermitian_scalar_real.reshape(half * half, 1),
        hermitian_scalar_imag.reshape(half * half, 1),
    )

    inverse_graph = sp.Matrix.vstack(Z.H.inv(), identity_history_half)
    direct_graph = sp.Matrix.vstack(Z, identity_history_half)
    support_space_shift = space_shift_ap.extract(
        NEGATIVE_AP_INDICES, NEGATIVE_AP_INDICES
    )
    doubled_support_shift = sp.diag(
        support_space_shift, support_space_shift
    )
    inverse_space_defect = sp.expand(
        doubled_support_shift * inverse_graph
        - inverse_graph * support_space_shift
    )
    direct_space_defect = sp.expand(
        doubled_support_shift * direct_graph
        - direct_graph * support_space_shift
    )

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
        stage_structure=(
            matrix_equal(S * S, identity_frame),
            matrix_equal(S * Gamma * S, -Gamma),
            matrix_equal(Gamma * Qcal - Qcal * Gamma, sp.zeros(FRAME_DIMENSION)),
            matrix_equal(Gamma * EN, EN * E),
        ),
        raw_structure=(
            matrix_equal(K, K.H),
            K.rank(),
            matrix_equal(Gamma * K * Gamma, -K),
            C.rank(),
            Z.rank(),
            nonzero_entries(C - canonical_c),
            nonzero_entries(E * C * E + C),
        ),
        changed_frame_control=(
            nonzero_entries(full_hodge - minimal_hodge),
            (full_hodge - minimal_hodge).rank(),
            nonzero_entries(full_action - minimal_action),
            nonzero_entries(fixture.action_ap - minimal_action_ap),
            matrix_equal(minimal_kernel, minimal_kernel.H),
            matrix_equal(Gamma * minimal_kernel * Gamma, -minimal_kernel),
            minimal_history_gram.rank(),
            minimal_z.rank(),
        ),
        positive_dressing=(
            matrix_equal(W.T * W, identity_frame),
            matrix_equal(W.T * S * W, exchange_history),
            matrix_equal(AZ * AZ, identity_frame),
            matrix_equal(S * AZ.conjugate() * S, AZ),
            matrix_equal(AZ * Gamma, -Gamma * AZ),
            matrix_equal(theta_z * theta_z.conjugate(), identity_frame),
            matrix_equal(theta_z * Gamma, Gamma * theta_z),
            nonzero_entries(dressed_gram - positive_target),
        ),
        mixed_positive_dressing=(
            matrix_equal(mixed_y * mixed_y, sp.eye(2 * half)),
            matrix_equal(S * mixed_A.conjugate() * S, mixed_A),
            matrix_equal(
                mixed_theta * mixed_theta.conjugate(), identity_frame
            ),
            matrix_equal(mixed_gram, mixed_target),
            bool(
                mixed_a**2 - mixed_b**2 == 1
                and mixed_a - mixed_b > 0
                and mixed_a + mixed_b > 0
            ),
            matrix_equal(W.T * Gamma * W, mixed_basis_grading),
            2 * mixed_y_commutator.rank(),
            2 * mixed_y_anticommutator.rank(),
            2 * mixed_y_anticommutator.rank(),
            2 * mixed_y_commutator.rank(),
        ),
        tested_shift_context=(
            action_space_defect.rank(),
            nonzero_entries(action_space_defect),
            action_time_defect.rank(),
            nonzero_entries(action_time_defect),
        ),
        dressing_shift_defects=(
            az_space_defect.rank(),
            nonzero_entries(az_space_defect),
            az_time_defect.rank(),
            nonzero_entries(az_time_defect),
        ),
        scalar_ports=(
            sp.trace(hermitian_scalar_real),
            sp.trace(hermitian_scalar_imag),
            scalar_span.rank(),
            hermitian_scalar_real.rank(),
            hermitian_scalar_imag.rank(),
        ),
        matrix_ports=(
            matrix_equal(inverse_graph.H * C * inverse_graph, 2 * identity_history_half),
            matrix_equal(direct_graph.H * C * direct_graph, 2 * Z.H * Z),
            sp.Matrix.hstack(inverse_graph, E * inverse_graph).rank(),
            sp.Matrix.hstack(direct_graph, E * direct_graph).rank(),
            inverse_space_defect.rank(),
            nonzero_entries(inverse_space_defect),
            direct_space_defect.rank(),
            nonzero_entries(direct_space_defect),
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
    expected_stage_structure = mutation != "break_stage_grading"
    expected_raw_antichiral = mutation != "claim_positive_stage_exchange"
    expected_positive_dressing = mutation != "break_positive_dressing"
    expected_stage_preserving = (
        mutation != "claim_positive_dressing_exchanges_stage"
    )
    expected_mixed_positive = mutation != "break_mixed_positive_dressing"
    expected_mixed_stage_ranks = (
        (32, 32, 0, 32)
        if mutation == "claim_mixed_pure_stage"
        else (32, 32, 32, 32)
    )
    expected_scalar_exclusion = mutation != "claim_scalar_port_positive"
    expected_port_defect = mutation != "claim_graph_port_covariant"

    checks.check(
        "A",
        "fresh authority, exact repaired-parent pins, and all declared inputs",
        facts.authority == expected_authority and facts.inputs_readable,
    )
    checks.check(
        "B",
        "the doubled action has an honest stage-exchanging reflection and invariant history support",
        all(facts.stage_structure) == expected_stage_structure,
    )
    checks.check(
        "C",
        "two distinct closed frames have nonzero Hermitian grading-odd history kernels",
        facts.raw_structure
        == (True, 32, expected_raw_antichiral, 16, 8, 0, 0)
        and facts.changed_frame_control
        == (96, 32, 256, 128, True, True, 16, 8),
    )
    checks.check(
        "D",
        "exact positive pure-preserving and mixed-stage involutions exist, with the pure witness failing tested doubled-shift commutators",
        all(facts.positive_dressing[:6])
        and facts.positive_dressing[6] == expected_stage_preserving
        and facts.positive_dressing[7] == 0
        and facts.dressing_shift_defects
        == ((32, 192, 32, 272) if expected_positive_dressing else (0, 192, 32, 272))
        and all(facts.mixed_positive_dressing[:6]) == expected_mixed_positive
        and facts.mixed_positive_dressing[6:] == expected_mixed_stage_ranks
        and facts.tested_shift_context == (16, 160, 16, 96),
    )
    checks.check(
        "E",
        "every scalar graph with z nonzero has a nonzero traceless form, so none is positive semidefinite",
        facts.scalar_ports
        == ((0, 0, 2, 8, 8) if expected_scalar_exclusion else (0, 0, 1, 8, 8)),
    )
    checks.check(
        "F",
        "two matrix graph ports are exactly positive but grading-mixing and fail inherited diagonal spatial equivariance",
        facts.matrix_ports
        == (
            (True, True, 16, 16, 8, 48, 8, 48)
            if expected_port_defect
            else (True, True, 16, 16, 0, 48, 8, 48)
        ),
    )
    checks.check(
        "G",
        "the note carries N1-N8, N5, named fixtures, and falsifiable TOE scope",
        facts.note_ready and facts.n5_ready and facts.fixture_ready and facts.scope_ready,
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
    return build_checks(measure(args.mutation), args.mutation).report()


if __name__ == "__main__":
    raise SystemExit(main())
