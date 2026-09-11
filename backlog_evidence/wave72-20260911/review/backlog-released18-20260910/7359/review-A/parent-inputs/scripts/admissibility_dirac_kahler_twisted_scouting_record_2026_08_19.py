#!/usr/bin/env python3
"""Block 137: exact twisted-scouting-record certificate.

The runner rebuilds the committed Block 105 four-chart atlas, distinguishes
telescopic connection bookkeeping from independent content, reinterprets the
Block 134 selector residual as an edge correction, and records precisely where
that correction heals or fails to heal the displayed construction.  All
scientific arithmetic is exact SymPy arithmetic; the integer monotonic clock
is used only for the runtime gate.
"""

from __future__ import annotations

import argparse
from itertools import combinations
from pathlib import Path
import re
import subprocess
import time

import sympy as sp

import admissibility_dirac_kahler_connection_residual_theorem_2026_08_17 as b134
import admissibility_dirac_kahler_observable_scaling_law_2026_08_18 as block136
import admissibility_dirac_kahler_residual_invariance_theorem_2026_08_17 as b135


b105 = b134.block105
I = sp.I
R = sp.Rational
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_TWISTED_SCOUTING_RECORD_"
    "BOUNDED_THEOREM_NOTE_2026-08-19.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_OBSERVABLE_SCALING_LAW_"
    "BOUNDED_THEOREM_NOTE_2026-08-18.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_observable_scaling_law_2026_08_18.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_observable_scaling_law_"
    "2026_08_18.txt"
)
B105_RUNNER = (
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_"
    "nonuniform_hodge_overlap_2026_08_14.py"
)
B134_RUNNER = (
    "scripts/admissibility_dirac_kahler_connection_residual_theorem_"
    "2026_08_17.py"
)
B135_RUNNER = (
    "scripts/admissibility_dirac_kahler_residual_invariance_theorem_"
    "2026_08_17.py"
)

# Deliberately literal: this is the complete audit read surface.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TWISTED_SCOUTING_RECORD_BOUNDED_THEOREM_NOTE_2026-08-19.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_OBSERVABLE_SCALING_LAW_BOUNDED_THEOREM_NOTE_2026-08-18.md",
    "scripts/admissibility_dirac_kahler_observable_scaling_law_2026_08_18.py",
    "logs/runner-cache/admissibility_dirac_kahler_observable_scaling_law_2026_08_18.txt",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "scripts/admissibility_dirac_kahler_connection_residual_theorem_2026_08_17.py",
    "scripts/admissibility_dirac_kahler_residual_invariance_theorem_2026_08_17.py",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block136-observable-scaling-law-20260818"
)
PARENT_COMMIT = "a9e0725db114298d9885e86b34d3c99bfe051444"
PARENT_NOTE_BLOB = "5c7e8b724e90320f3ceea332cc3abd4ce5128723"
PARENT_RUNNER_BLOB = "f86976787595c0f183ca8ce15456c8f857c2b6a6"
PARENT_CACHE_BLOB = "34f29c9a23d97732e864cfc85ba51304d298f8bc"
B105_COMMIT = "d06066c2b908aaca0779625d831dfb10620cf34d"
B105_RUNNER_BLOB = "4870f31b5880028ad4f1f3095aad4d0820e4668f"
B134_COMMIT = "acb7d8109bf751c909364aec92c4d833492cfa6c"
B134_RUNNER_BLOB = "f092e5560590d6a4e485a57721878caaa874b4dd"
B135_COMMIT = "dac48758c9967761b1b4419b5870357ca8da7cfa"
B135_RUNNER_BLOB = "a54b45f961583792d01081c1f2aab17c35a0f239"

ANCESTOR_COMMITS = (
    (135, B135_COMMIT),
    (134, B134_COMMIT),
    (133, "80d208f0c12e21fd985d01e5f807a9d34c00ef11"),
    (132, "0236823bed5b648ad8357e5d1b79bdfe1be36c39"),
    (131, "d3a666f62c87b3b8178289024087090c91ced327"),
    (130, "db394d1536a8243c2b01b3e45413813e45f8abdd"),
    (129, "30fd2722a10a02f87c235e2ee592d140f8bb7df5"),
    (128, "f6b0cf59e2cc588ebd3e34b96e730574cb485db2"),
    (127, "ca6792464f60598013a3700f99c02a467af64b7a"),
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
    (105, B105_COMMIT),
    (104, "7fe07db6c03fad1191893c942f708c5cb9a54c43"),
    (103, "99cee0a6c962b382a3ca1a8497d589ffa280dfe8"),
)

MUTATIONS = (
    "stale_upstream_authority",
    "break_atlas_dressing",
    "break_theta_bookkeeping",
    "break_theta_bianchi",
    "break_selector_projection",
    "break_edge_healing",
    "break_edge_acyclicity",
    "break_curvature_profile",
    "conflate_curvature_correction",
    "break_action_identity",
    "erase_action_tail",
    "break_companion_kernel",
    "claim_companion_correction",
    "break_parity_certificate",
    "weaken_note_scope",
)

# The partition is itself the isolation contract: every mutation belongs to
# exactly one gate and is applied only after that gate's raw values exist.
GATE_MUTATIONS = {
    "A": ("stale_upstream_authority", "break_atlas_dressing"),
    "B": ("break_theta_bookkeeping", "break_theta_bianchi"),
    "C": ("break_selector_projection",),
    "D": ("break_edge_healing", "break_edge_acyclicity"),
    "E": ("break_curvature_profile", "conflate_curvature_correction"),
    "F": ("break_action_identity", "erase_action_tail"),
    "G": (
        "break_companion_kernel",
        "claim_companion_correction",
        "break_parity_certificate",
    ),
    "H": ("weaken_note_scope",),
}
MUTATION_PARTITION_EXACT = (
    tuple(
        item
        for gate in ("A", "B", "C", "D", "E", "F", "G", "H")
        for item in GATE_MUTATIONS[gate]
    )
    == MUTATIONS
    and len(set(MUTATIONS)) == 15
)


def mutation_allows(gate: str, mutation: str) -> bool:
    return MUTATION_PARTITION_EXACT and mutation not in GATE_MUTATIONS[gate]


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


def authority_certificate() -> dict[str, object]:
    return {
        "main": git_output("rev-parse", "origin/main"),
        "axiom": commit_blob("origin/main", AXIOM_PATH),
        "worktree_axiom": worktree_blob(AXIOM_PATH),
        "registry": commit_blob("origin/main", REGISTRY_PATH),
        "worktree_registry": worktree_blob(REGISTRY_PATH),
        "parent": git_output("rev-parse", PARENT_REF),
        "parent_ancestor": is_ancestor(PARENT_COMMIT, "HEAD"),
        **{
            f"ancestor_{number}": is_ancestor(commit, "HEAD")
            for number, commit in ANCESTOR_COMMITS
        },
        "parent_note": commit_blob(PARENT_COMMIT, PARENT_NOTE),
        "parent_runner": commit_blob(PARENT_COMMIT, PARENT_RUNNER),
        "parent_cache": commit_blob(PARENT_COMMIT, PARENT_CACHE),
        "worktree_parent_note": worktree_blob(PARENT_NOTE),
        "worktree_parent_runner": worktree_blob(PARENT_RUNNER),
        "worktree_parent_cache": worktree_blob(PARENT_CACHE),
        "b105_runner": commit_blob(B105_COMMIT, B105_RUNNER),
        "worktree_b105_runner": worktree_blob(B105_RUNNER),
        "b134_runner": commit_blob(B134_COMMIT, B134_RUNNER),
        "worktree_b134_runner": worktree_blob(B134_RUNNER),
        "b135_runner": commit_blob(B135_COMMIT, B135_RUNNER),
        "worktree_b135_runner": worktree_blob(B135_RUNNER),
    }


def raw_note() -> bytes:
    try:
        return NOTE_PATH.read_bytes()
    except OSError:
        return b""


def normalized_note(note: bytes) -> str:
    try:
        decoded = note.decode("utf-8")
    except UnicodeError:
        return ""
    return " ".join(decoded.lower().split())


def zero(matrix: sp.MatrixBase) -> bool:
    return b134.matrix_zero(matrix)


def no_float(value: object) -> bool:
    if isinstance(value, sp.MatrixBase):
        return not value.has(sp.Float)
    return not sp.sympify(value).has(sp.Float)


def connection_data(sx: sp.Expr, st: sp.Expr) -> dict[str, object]:
    """Return the exact chart, frame, transition, and differential data."""
    local = b134.local_differential(sx, st)
    phase = b134.lifted(b105.phase_unitary().H)
    charts = {origin: b134.cover_chart_matrix(origin) for origin in b134.ORIGINS}
    frames = {origin: phase * charts[origin] for origin in b134.ORIGINS}
    gauges = {origin: b134.chart_gauge(origin) for origin in b134.ORIGINS}
    local_charts = {
        origin: b134.lifted(sp.simplify(gauges[origin].H * local * gauges[origin]))
        for origin in b134.ORIGINS
    }
    # d_i is in the common physical cover frame; dhat_i is in chart frame i.
    differentials = {
        origin: sp.simplify(charts[origin].H * local_charts[origin] * charts[origin])
        for origin in b134.ORIGINS
    }
    frame_differentials = {
        origin: sp.simplify(frames[origin] * differentials[origin] * frames[origin].H)
        for origin in b134.ORIGINS
    }
    transitions = {
        (first, second): sp.simplify(frames[second] * frames[first].H)
        for first in b134.ORIGINS
        for second in b134.ORIGINS
    }
    defects = {
        (first, second): sp.simplify(
            frame_differentials[second] * transitions[(first, second)]
            - transitions[(first, second)] * frame_differentials[first]
        )
        for first in b134.ORIGINS
        for second in b134.ORIGINS
    }
    return {
        "local": local,
        "phase": phase,
        "charts": charts,
        "frames": frames,
        "gauges": gauges,
        "local_charts": local_charts,
        "d": differentials,
        "dhat": frame_differentials,
        "g": transitions,
        "theta": defects,
    }


def selector_mask(
    first: tuple[int, int], second: tuple[int, int]
) -> tuple[tuple[int, int], ...]:
    """The parameter-independent scalar selectors shared by two charts."""
    factorization = b135.selector_factorization((first, second))
    rows_per_chart = b134.NCELLS * 16
    return tuple(
        key
        for key, indices in factorization.groups
        if any(index < rows_per_chart for index in indices)
        and any(index >= rows_per_chart for index in indices)
    )


def project(
    matrix: sp.MatrixBase, mask: tuple[tuple[int, int], ...]
) -> sp.Matrix:
    result = sp.zeros(matrix.rows, matrix.cols)
    for row, column in mask:
        result[row, column] = matrix[row, column]
    return result


def pair_data(
    data: dict[str, object],
    first: tuple[int, int],
    second: tuple[int, int],
) -> tuple[b134.SelectorSystem, sp.Matrix, sp.Matrix, tuple[tuple[int, int], ...]]:
    system = b135.factorized_selector_system(
        (
            (first, b134.chart_gauge(first)),
            (second, b134.chart_gauge(second)),
        ),
        data["local"],
    )
    omega = b134.conflict_operator(system)
    full_difference = sp.simplify(data["d"][second] - data["d"][first])
    return system, omega, full_difference, selector_mask(first, second)


def quotient_action(
    differential: sp.Matrix, hodge: sp.Matrix, mass: sp.Expr
) -> sp.Matrix:
    cover = sp.simplify(
        mass * hodge + I * (hodge * differential + differential.H * hodge)
    )
    return b134.antiperiodic_quotient(cover)


def quotient_correction(operator: sp.Matrix, hodge: sp.Matrix) -> sp.Matrix:
    cover = sp.simplify(I * (hodge * operator + operator.H * hodge))
    return b134.antiperiodic_quotient(cover)


N5_LINES = (
    'N5: per_element: exact 32x32 transition, selector-projection, edge-anticommutator, triple-curvature, action-tail, and companion-minor certificates are checked',
    'per_site: the displayed Lx=4, Tphysical=4, Tcover=8 carrier has four Z2^2 chart origins and uses the inherited antiperiodic quotient and nonuniform Hodge',
    'per_mode: W*Omega*W^dag=2*i*s_t*T_t^-1*P_even*P_x has even parity and its forward companion correction misses the odd kernel direction identically',
    'per_block: every dressed edge has square zero and the displayed edge has rank 16 and cohomology dimension zero, while the atlas has 24/64 nonzero rank-16 curvatures, the action leaves a rank-8 tail, and the companion stays rank 3',
    'lattice_wide: checked and not executed — parity-mixing and other dressing classes, the general-Z_N charge-kinematic theorem, the joint-lane program, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient beyond the displayed carriers, Records, audit retention, and TOE closure remain open',
)

RESULT_LINE = (
    'RESULT: within the displayed transition-dressing class the twisted formulation does not open the curved OS pipeline'
)
DECISION_LINE = (
    'DECISION_CUT: W1 is not an OS no-go, not a curved OS no-go, and not a no-go for parity-mixing or other dressing classes'
)
TOE_LINE = (
    'TOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero'
)

SCOPE_KEYS = (
    "twisted_record",
    "telescopic_bookkeeping",
    "dressing_class_boundary",
    "os_boundary",
    "st_only_rider",
    "edge_healing",
    "curvature_profile",
    "curvature_disambiguation",
    "action_tail",
    "companion_non_healing",
    "parity",
    "axiom",
    "zero_retirement",
    "zero_score",
    "zero_e2e",
    "gravity_quotient",
    "adm",
    "records_audit",
    "n1_n8",
    "w1",
    "n5_resolution",
    "n5_verbatim",
)


def scope_certificate(note: str) -> dict[str, bool]:
    result = {
        "twisted_record": (
            "twisted scouting record" in note
            or "twisted-formulation scouting record" in note
            or "bounded scouting record" in note
        ),
        "telescopic_bookkeeping": (
            (
                "telescopic bookkeeping" in note
                or "telescopic-bookkeeping" in note
                or "telescopic identity" in note
            )
            and (
                "no independent load" in note
                or "carries no independent" in note
                or "independent evidentiary load" in note
            )
        ),
        "dressing_class_boundary": (
            (
                "displayed dressing class" in note
                or "fixed dressing class" in note
                or "block 105 dressing class" in note
                or "dressing-class boundary" in note
            )
            and (
                "other dressing classes" in note
                or "not a general dressing" in note
                or "dressing theorem remains" in note
            )
        ),
        "os_boundary": (
            "not an os no-go" in note
            or "not a curved os no-go" in note
        ),
        "st_only_rider": (
            "s_t-only" in note
            or "s_t only" in note
            or "s_t$-only" in note
            or ("s_t=0" in note and "only" in note)
        ),
        "edge_healing": (
            "acyclic edge" in note
            or "edge complex" in note
            or "edge healing" in note
        ),
        "curvature_profile": (
            ("24/64" in note or "24 of 64" in note)
            and ("rank 16" in note or "rank-16" in note)
        ),
        "curvature_disambiguation": (
            "not delta_omega" in note
            or "distinct from delta_omega" in note
            or "c_ijk != delta_omega" in note
            or "c_ijk is not delta_omega" in note
        ),
        "action_tail": (
            (
                "rank-8 tail" in note
                or "rank 8 tail" in note
                or "rank-8 action tail" in note
            )
            and ("omega-only" in note or "global quadratic form" in note)
        ),
        "companion_non_healing": (
            ("rank 3" in note or "rank=3" in note)
            and "span(0,1,0,0)" in note
            and ("non-healing" in note or "correction" in note)
        ),
        "parity": (
            "even-parity" in note
            and ("odd companion" in note or "kernel direction" in note)
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
        "records_audit": "records" in note and "audit retention" in note,
        "n1_n8": all(
            re.search(rf"\bn{index}\b", note) is not None
            for index in range(1, 9)
        ),
        "w1": re.search(r"\bw1\b", note) is not None,
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
        "n5_verbatim": all(
            " ".join(line.lower().split()) in note for line in N5_LINES
        )
        and " ".join(RESULT_LINE.lower().split()) in note
        and " ".join(DECISION_LINE.lower().split()) in note
        and " ".join(TOE_LINE.lower().split()) in note,
    }
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    mutation = parser.parse_args().mutation
    started_ns = time.monotonic_ns()
    checks = Checks()

    note = normalized_note(raw_note())
    authority = authority_certificate()
    authority_raw = (
        AUDIT_TIMEOUT_SEC == 600
        and AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_TWISTED_SCOUTING_RECORD_BOUNDED_THEOREM_NOTE_2026-08-19.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_OBSERVABLE_SCALING_LAW_BOUNDED_THEOREM_NOTE_2026-08-18.md",
            "scripts/admissibility_dirac_kahler_observable_scaling_law_2026_08_18.py",
            "logs/runner-cache/admissibility_dirac_kahler_observable_scaling_law_2026_08_18.txt",
            "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
            "scripts/admissibility_dirac_kahler_connection_residual_theorem_2026_08_17.py",
            "scripts/admissibility_dirac_kahler_residual_invariance_theorem_2026_08_17.py",
        )
        and authority["main"] == CURRENT_MAIN
        and authority["axiom"] == CURRENT_AXIOM_BLOB
        and authority["worktree_axiom"] == WORKTREE_AXIOM_BLOB
        and authority["registry"] == CURRENT_REGISTRY_BLOB
        and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
        and authority["parent"] == PARENT_COMMIT
        and authority["parent_ancestor"]
        and all(
            authority[f"ancestor_{number}"] for number in range(103, 136)
        )
        and authority["parent_note"] == PARENT_NOTE_BLOB
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB
        and authority["worktree_parent_note"] == PARENT_NOTE_BLOB
        and authority["worktree_parent_runner"] == PARENT_RUNNER_BLOB
        and authority["worktree_parent_cache"] == PARENT_CACHE_BLOB
        and authority["b105_runner"] == B105_RUNNER_BLOB
        and authority["worktree_b105_runner"] == B105_RUNNER_BLOB
        and authority["b134_runner"] == B134_RUNNER_BLOB
        and authority["worktree_b134_runner"] == B134_RUNNER_BLOB
        and authority["b135_runner"] == B135_RUNNER_BLOB
        and authority["worktree_b135_runner"] == B135_RUNNER_BLOB
        and block136.AUDIT_TIMEOUT_SEC == AUDIT_TIMEOUT_SEC
        and block136.block135 is b135
    )

    origins = b134.ORIGINS
    displayed = b134.DISPLAYED
    first, second = displayed
    sx, st = sp.symbols("s_x s_t", real=True)
    symbolic = connection_data(sx, st)
    fixture = connection_data(b134.S_X, b134.S_T)

    import_exact = (
        Path(b105.__file__).name
        == "admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py"
        and Path(b134.__file__).name
        == "admissibility_dirac_kahler_connection_residual_theorem_2026_08_17.py"
        and Path(b135.__file__).name
        == "admissibility_dirac_kahler_residual_invariance_theorem_2026_08_17.py"
        and Path(block136.__file__).name
        == "admissibility_dirac_kahler_observable_scaling_law_2026_08_18.py"
        and (b134.S_X, b134.S_T, b134.MASS) == (R(3, 5), R(4, 5), R(2, 7))
        and b134.SIZE == 32
        and origins == ((0, 0), (0, 1), (1, 0), (1, 1))
        and len(displayed) == 2
    )
    atlas_exact = (
        set(fixture["charts"])
        == set(fixture["frames"])
        == set(fixture["gauges"])
        == set(fixture["local_charts"])
        == set(fixture["d"])
        == set(fixture["dhat"])
        == set(origins)
        and fixture["local"].shape == (4, 4)
        and fixture["phase"].shape == (32, 32)
        and zero(fixture["phase"].H * fixture["phase"] - sp.eye(32))
        and all(
            fixture["charts"][origin].shape == (32, 32)
            and fixture["frames"][origin].shape == (32, 32)
            and zero(
                fixture["charts"][origin].H
                * fixture["charts"][origin]
                - sp.eye(32)
            )
            and zero(
                fixture["frames"][origin].H
                * fixture["frames"][origin]
                - sp.eye(32)
            )
            and fixture["d"][origin].shape == (32, 32)
            and fixture["d"][origin].rank() == 16
            and zero(fixture["d"][origin] ** 2)
            and fixture["dhat"][origin].rank() == 16
            and zero(fixture["dhat"][origin] ** 2)
            and all(
                no_float(matrix)
                for matrix in (
                    fixture["charts"][origin],
                    fixture["frames"][origin],
                    fixture["gauges"][origin],
                    fixture["local_charts"][origin],
                    fixture["d"][origin],
                    fixture["dhat"][origin],
                )
            )
            for origin in origins
        )
        and no_float(fixture["local"])
        and no_float(fixture["phase"])
    )
    dressing_exact = all(
        fixture["g"][(left, right)].shape == (32, 32)
        and zero(
            fixture["g"][(left, right)]
            - fixture["frames"][right] * fixture["frames"][left].H
        )
        and zero(
            fixture["g"][(left, right)].H
            * fixture["g"][(left, right)]
            - sp.eye(32)
        )
        and zero(
            fixture["g"][(right, left)]
            - fixture["g"][(left, right)].H
        )
        and no_float(fixture["g"][(left, right)])
        for left in origins
        for right in origins
    ) and all(
        zero(
            fixture["g"][(middle, right)]
            * fixture["g"][(left, middle)]
            - fixture["g"][(left, right)]
        )
        for left in origins
        for middle in origins
        for right in origins
    )
    atlas_dressing_raw = import_exact and atlas_exact and dressing_exact
    checks.check(
        "A-fixture-atlas-integrity",
        "Block 136 plus Blocks 105/134/135 are blob-bound; the exact four-chart atlas and every unitary dressing g_ij are rebuilt",
        authority_raw
        and atlas_dressing_raw
        and mutation_allows("A", mutation),
    )

    theta_formula_raw = all(
        zero(
            fixture["theta"][(left, right)]
            - fixture["dhat"][right] * fixture["g"][(left, right)]
            + fixture["g"][(left, right)] * fixture["dhat"][left]
        )
        and zero(
            fixture["theta"][(left, right)]
            - fixture["frames"][right]
            * (fixture["d"][right] - fixture["d"][left])
            * fixture["frames"][left].H
        )
        for left in origins
        for right in origins
    )
    theta_composition_raw = all(
        zero(
            fixture["theta"][(middle, right)]
            * fixture["g"][(left, middle)]
            + fixture["g"][(middle, right)]
            * fixture["theta"][(left, middle)]
            - fixture["theta"][(left, right)]
        )
        for left in origins
        for middle in origins
        for right in origins
    )
    theta_bianchi_raw = all(
        zero(
            fixture["dhat"][right] * fixture["theta"][(left, right)]
            + fixture["theta"][(left, right)] * fixture["dhat"][left]
        )
        for left in origins
        for right in origins
    )
    theta_bookkeeping_raw = theta_formula_raw and theta_composition_raw
    checks.check(
        "B-cocycle-bookkeeping",
        "Theta_ij=dhat_j*g_ij-g_ij*dhat_i obeys composition and Bianchi; FLAG: composition is telescopic bookkeeping (the vacuity catch) and carries no independent load",
        theta_bookkeeping_raw
        and theta_bianchi_raw
        and mutation_allows("B", mutation),
    )

    omega_fixture: dict[
        tuple[tuple[int, int], tuple[int, int]], sp.Matrix
    ] = {}
    omega_symbolic: dict[
        tuple[tuple[int, int], tuple[int, int]], sp.Matrix
    ] = {}
    full_fixture: dict[
        tuple[tuple[int, int], tuple[int, int]], sp.Matrix
    ] = {}
    masks: dict[
        tuple[tuple[int, int], tuple[int, int]], tuple[tuple[int, int], ...]
    ] = {}
    projection_raw = True
    omega_nilpotent_raw = True
    edge_square_raw = True
    edge_anticommutator_raw = True
    edge_acyclicity_raw = True
    for left in origins:
        for right in origins:
            _system, omega, full, mask = pair_data(fixture, left, right)
            (
                _symbolic_system,
                symbolic_omega,
                symbolic_full,
                symbolic_mask,
            ) = pair_data(symbolic, left, right)
            omega_fixture[(left, right)] = omega
            omega_symbolic[(left, right)] = symbolic_omega
            full_fixture[(left, right)] = full
            masks[(left, right)] = mask
            projection_raw &= (
                mask == symbolic_mask
                and zero(omega - project(full, mask))
                and zero(symbolic_omega - project(symbolic_full, symbolic_mask))
            )
            omega_nilpotent_raw &= zero(omega**2) and zero(symbolic_omega**2)
            edge_anticommutator_raw &= zero(
                symbolic["d"][left] * symbolic_omega
                + symbolic_omega * symbolic["d"][left]
            )
            edge_square_raw &= zero(
                (symbolic["d"][left] + symbolic_omega) ** 2
            )
            fixture_edge = sp.simplify(fixture["d"][left] + omega)
            edge_acyclicity_raw &= (
                zero(fixture_edge**2)
                and fixture_edge.rank() == 16
                and b134.SIZE - 2 * fixture_edge.rank() == 0
            )

    displayed_system, omega, full_difference, displayed_mask = pair_data(
        symbolic, first, second
    )
    normal = b134.residual_operator_certificate(displayed_system, st)
    residual_symbols = set().union(
        *(
            entry.free_symbols
            for item in omega_symbolic.values()
            for entry in item
        )
    )
    normal_raw = (
        displayed_system.rank == 192
        and displayed_system.augmented_rank == 193
        and displayed_mask == masks[displayed]
        and normal.signed_frame_exact
        and normal.grading_mechanism_exact
        and zero(normal.residual_frame * omega * normal.residual_frame.H - normal.formula)
        and zero(
            normal.formula
            - 2
            * I
            * st
            * normal.time_shift_inverse
            * normal.even_projector
            * normal.spatial_shift
        )
        and residual_symbols == {st}
        and all(
            zero(item.subs(st, 0)) for item in omega_symbolic.values()
        )
    )
    fixture_omega = omega_fixture[displayed]
    fixture_full = full_fixture[displayed]
    projection_tail = sp.simplify(fixture_full - fixture_omega)
    projection_profile = (
        fixture_omega.rank(),
        len(b134.support(fixture_omega)),
        len(b134.support(fixture_full)),
        len(b134.support(projection_tail)),
    )
    selector_projection_raw = (
        projection_raw
        and normal_raw
        and projection_profile == (16, 16, 48, 32)
        and zero(omega - project(full_difference, displayed_mask))
    )
    checks.check(
        "C-selector-projection",
        "Block 134 Omega_ij is exactly reinterpreted as Pi_ij(d_j-d_i) on the displayed atlas, with s_t-only residual support",
        selector_projection_raw and mutation_allows("C", mutation),
    )

    edge_healing_raw = (
        omega_nilpotent_raw
        and edge_anticommutator_raw
        and edge_square_raw
    )
    checks.check(
        "D-edge-healing",
        "for every displayed ordered edge, Omega^2=0, {d_i,Omega_ij}=0, (d_i+Omega_ij)^2=0, and the edge complex is acyclic",
        edge_healing_raw
        and edge_acyclicity_raw
        and mutation_allows("D", mutation),
    )

    curvature_fixture: dict[
        tuple[tuple[int, int], tuple[int, int], tuple[int, int]], sp.Matrix
    ] = {}
    curvature_symbolic: dict[
        tuple[tuple[int, int], tuple[int, int], tuple[int, int]], sp.Matrix
    ] = {}
    atlas_square_raw = True
    projected_cocycle_raw = True
    transported_curvature_raw = True
    for left in origins:
        for middle in origins:
            for right in origins:
                key = (left, middle, right)
                curvature_fixture[key] = sp.simplify(
                    omega_fixture[(left, right)]
                    - omega_fixture[(middle, right)]
                    - omega_fixture[(left, middle)]
                )
                curvature_symbolic[key] = sp.simplify(
                    omega_symbolic[(left, right)]
                    - omega_symbolic[(middle, right)]
                    - omega_symbolic[(left, middle)]
                )
                # This is the atlas/nerve square of the corrected edge data:
                # the unprojected d terms cancel before the Omega residual.
                atlas_square = sp.simplify(
                    (fixture["d"][left] + omega_fixture[(left, right)])
                    - (fixture["d"][middle] + omega_fixture[(middle, right)])
                    - (fixture["d"][left] + omega_fixture[(left, middle)])
                    + fixture["d"][middle]
                )
                atlas_square_raw &= zero(
                    atlas_square - curvature_fixture[key]
                )
                projected_cocycle_raw &= zero(
                    omega_fixture[(left, right)]
                    - project(
                        full_fixture[(middle, right)]
                        + full_fixture[(left, middle)],
                        masks[(left, right)],
                    )
                )
                omega_hat_lr = (
                    fixture["frames"][right]
                    * omega_fixture[(left, right)]
                    * fixture["frames"][left].H
                )
                omega_hat_mr = (
                    fixture["frames"][right]
                    * omega_fixture[(middle, right)]
                    * fixture["frames"][middle].H
                )
                omega_hat_lm = (
                    fixture["frames"][middle]
                    * omega_fixture[(left, middle)]
                    * fixture["frames"][left].H
                )
                transported_curvature_raw &= zero(
                    omega_hat_lr
                    - omega_hat_mr * fixture["g"][(left, middle)]
                    - fixture["g"][(middle, right)] * omega_hat_lm
                    - fixture["frames"][right]
                    * curvature_fixture[key]
                    * fixture["frames"][left].H
                )

    nonzero_curvatures = {
        key: value
        for key, value in curvature_fixture.items()
        if not zero(value)
    }
    curvature_profiles = {
        (value.rank(), len(b134.support(value)))
        for value in nonzero_curvatures.values()
    }
    representative = ((0, 0), (0, 1), (1, 0))
    representative_values = {
        sp.factor(value)
        for _, _, value in b134.support(curvature_symbolic[representative])
    }
    curvature_profile_raw = (
        atlas_square_raw
        and projected_cocycle_raw
        and transported_curvature_raw
        and len(nonzero_curvatures) == 24
        and curvature_profiles == {(16, 16)}
        and representative_values == {-2 * I * st, 2 * I * st}
        and zero(curvature_symbolic[representative].subs(st, 0))
    )

    hodge = b134.curved_hodge_cover()
    hodge_quotient = b134.antiperiodic_quotient(hodge)
    delta_omega = quotient_correction(fixture_omega, hodge)
    quotient_curvature = b134.antiperiodic_quotient(
        curvature_fixture[representative]
    )
    curvature_disambiguation_raw = (
        curvature_fixture[representative].rank() == 16
        and quotient_curvature.rank() == 8
        and delta_omega.rank() == 16
        and not zero(quotient_curvature - delta_omega)
        and (quotient_curvature - delta_omega).rank() == 16
    )
    checks.check(
        "E-atlas-curvature",
        "the atlas square D^2=C_ijk has exactly 24/64 nonzero rank-16 triples; C_ijk is distinct from the action correction Delta_Omega",
        curvature_profile_raw
        and curvature_disambiguation_raw
        and mutation_allows("E", mutation),
    )

    actions = {
        origin: quotient_action(fixture["d"][origin], hodge, b134.MASS)
        for origin in displayed
    }
    full_action_defect = sp.simplify(actions[second] - actions[first])
    full_action_correction = quotient_correction(fixture_full, hodge)
    omega_action_correction = delta_omega
    action_tail = sp.simplify(
        full_action_defect - omega_action_correction
    )
    action_identity_raw = all(
        zero(
            actions[origin]
            + actions[origin].H
            - 2 * b134.MASS * hodge_quotient
        )
        and (actions[origin] - actions[origin].H).rank() == 16
        for origin in displayed
    )
    action_tail_raw = (
        zero(full_action_defect - full_action_correction)
        and zero(omega_action_correction + omega_action_correction.H)
        and zero(action_tail + action_tail.H)
        and omega_action_correction.rank() == 16
        and action_tail.rank() == 8
        and not zero(action_tail)
        and not zero(full_action_defect - omega_action_correction)
    )
    checks.check(
        "F-action-tail",
        "Q_i+Q_i^dag=2*m*H_q, but the skew Omega correction leaves a nonzero rank-8 tail, excluding an Omega-only atlas-global quadratic form",
        action_identity_raw
        and action_tail_raw
        and mutation_allows("F", mutation),
    )

    mass = sp.symbols("m", real=True, nonzero=True)
    symbolic_action = quotient_action(symbolic["d"][first], hodge, mass)
    symbolic_action_correction = quotient_correction(
        omega_symbolic[displayed], hodge
    )
    coefficient = symbolic_action[4:8, 0:4]
    coefficient_correction = symbolic_action_correction[4:8, 0:4]
    kernel_vector = sp.Matrix((0, 1, 0, 0))
    minors = tuple(
        sp.factor(coefficient.extract(rows, columns).det())
        for rows in combinations(range(4), 3)
        for columns in combinations(range(4), 3)
    )
    fixture_coefficient = actions[first][4:8, 0:4]
    fixture_correction = omega_action_correction[4:8, 0:4]
    companion_kernel_raw = (
        mass.is_real is True
        and mass.is_nonzero is True
        and zero(coefficient * kernel_vector)
        and sp.factor(coefficient.det()) == 0
        and -mass**3 / 384 in minors
        and fixture_coefficient.rank() == 3
        and fixture_coefficient.nullspace() == [kernel_vector]
        and no_float(coefficient)
    )
    companion_correction_raw = (
        zero(coefficient_correction)
        and zero(fixture_correction)
        and (fixture_coefficient + fixture_correction).rank() == 3
        and (fixture_coefficient + fixture_correction).nullspace()
        == [kernel_vector]
    )
    even_projector = normal.even_projector
    odd_projector = sp.eye(b134.SIZE) - even_projector
    residual_omega = sp.simplify(
        normal.residual_frame * omega * normal.residual_frame.H
    )
    parity_core = sp.simplify(
        normal.time_shift_inverse.H
        * residual_omega
        * normal.spatial_shift.H
    )
    local_even = even_projector[:4, :4]
    local_odd = odd_projector[:4, :4]
    parity_raw = (
        even_projector == sp.diag(*((1, 0) * 16))
        and zero(even_projector * odd_projector)
        and zero(parity_core - 2 * I * st * even_projector)
        and zero(odd_projector * parity_core)
        and zero(parity_core * odd_projector)
        and not zero(parity_core)
        and zero(local_even * kernel_vector)
        and local_odd * kernel_vector == kernel_vector
    )
    checks.check(
        "G-companion-non-healing",
        "for symbolic m!=0 the forward coefficient has rank 3 and ker=span(0,1,0,0), Delta_Omega B=0 identically, and even-parity Omega misses the odd kernel direction",
        companion_kernel_raw
        and companion_correction_raw
        and parity_raw
        and mutation_allows("G", mutation),
    )

    scope = scope_certificate(note)
    elapsed_ns = time.monotonic_ns() - started_ns
    checks.check(
        "H-scope",
        "the telescopic and dressing-class flags, OS boundary, s_t-only rider, N1--N8/W1/N5 fence, and TOE firewalls are present",
        set(scope) == set(SCOPE_KEYS)
        and all(scope.values())
        and elapsed_ns <= 500 * 1_000_000_000
        and mutation_allows("H", mutation),
    )

    for line in N5_LINES:
        print(line)
    if checks.failed == 0:
        print(RESULT_LINE)
        print(DECISION_LINE)
    else:
        print(
            "RESULT: BLOCKED — at least one exact authority, atlas, "
            "bookkeeping, projection, edge, curvature, action, companion, "
            "scope, mutation, or runtime certificate failed"
        )
        print(
            "DECISION_CUT: repair the failed certificate without promoting "
            "telescopic bookkeeping or the fixed dressing to a curved OS no-go"
        )
    print(TOE_LINE)
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
