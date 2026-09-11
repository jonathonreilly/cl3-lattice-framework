#!/usr/bin/env python3
"""BLOCK 180 -- THE ORIENTATION BIT, TERMINATED.

THE RESULT, AND ITS EXACT SCOPE.  On the committed CONSTANT-CARRIER Dirac-Kahler
fixtures -- the 12x6 cover at T_phys = 6 and L_x = 6 and the 8x4 cover at
T_phys = 4 and L_x = 4, region pin c = 1, shear zero on the pinned time levels
{0,1} and the committed CARRIER_SIGMA = 3/5 elsewhere, constant volume 7/5,
mass 1, at the FRAME BENCHMARK (s_x, s_t) = (3/5, 1/4) and at the MEASURE
FIXTURE (s_x, s_t) = (3/5, 0) -- with the landed staggered grading
X_0 = (-1)^(t+x), the chart translation U|t,x> = |t, x+2 mod L_x> and the
DISCLOSED cyclotomic field Q(sqrt(-3)):

  1. THE FRAME THEOREM.  X_0 Q(+s_x,+s_t) X_0 = Q(-s_x,-s_t) EXACTLY at both
     extents with a ZERO residual, while either single flip leaves 84 nonzero
     entries at 12x6 and 32 at 8x4.  X_0 is unitary and involutive, but it is
     NOT a fixed-point symmetry: X_0 Q(+,+) X_0 - Q(+,+) has 144 nonzero entries
     at 12x6 and 56 at 8x4.  The equivalence is HORIZONTAL, between class
     points -- THE CHECKER'S CORRECTION OF THE SUPERVISOR'S FRAME READING,
     carried here rather than the stronger reading -- and the grading descends
     through the antiperiodic quotient iff both PHYSICAL extents are even, which
     6x6 and 4x4 satisfy.

  2. THE NO-REGISTRATION THEOREM.  X_0 commutes with the committed reflection r,
     so the determinant, the spectrum, herm(Q^-1) and the reflected form are all
     conjugate across (+,+) <-> (-,-): NO COMMITTED-CLASS CHANNEL DETECTS THE
     OVERALL ORIENTATION, and the geometries that would register it are exactly
     the ones where the grading fails to descend.  The surviving datum is the
     TRIPLE SIGN sigma s_x s_t, spectrally registered by tr(Q^2) and
     COUNT-NEUTRAL.

  3. THE WITT UNIT THEOREM.  The plain W9 Gram on the four eigenlines is the
     scalar (875/1462) I_4, while the REFLECTED (OS) Gram is EXACTLY
     ANTI-DIAGONAL with (g_+,h_-) = (g_-,h_+) = 875/1462 and every diagonal
     entry zero: every eigenline is ISOTROPIC, each Theta-orbit is one
     HYPERBOLIC CELL, and LINE-COUNTING AT n = 4 IS DEAD BY COMPUTATION.

  4. THE WIGNER SILENCE.  The magnetic Klein group has NO honest corepresentation
     on the class-doubled carrier: the unitary X_0-swap control PASSES exactly,
     and all SIX antiunitary placements FAIL A^T Q_D conj(A) = Q_D^T with exact
     residual counts 360, 336, 336, 336, 360, 360.  The Herring test is
     UNEVALUABLE and is reported SILENT AND NOT FORCED.

  5. THE DET-EXPONENT FACT, THE ARBITER-NATIVE LEG.  The c-sector's factor in the
     landed 12x6 partition function is EXACTLY (62866/30625)^2 =
     3952133956/937890625 -- TWO CELLS -- verified BOTH by the flavor arbiter's
     own det_cpair and by the basis-free ratio det(slice)/det(k=0 fiber), and
     calibrated against the accepted one-slot precedent beta = 3193/2240 and the
     level-4 singleton D4 = (1817/1120)(I + (3/5)J), the b = a s_x law again.
     The landed disconnection makes it a TRUE Z-factor.

  6. THE RESOLUTION.  What the committed structure says PREMISE-FREE is n = 2,
     r = 1, Q = 1.  The additive branch is TRUE of the landed measure and
     quotient counting is FALSE of committed structure; the supervisor's
     Witt-decides-the-count reading is QUOTED AND CORRECTED as the arc's EIGHTH
     supervisor correction.  Q = 2/3 requires exactly ONE new physical input,
     THE SIGMA-REALITY CONDITION -- carrier = Fix(-Theta o X_0), a verified
     antilinear involution with Fix = {z g_+ + zbar h_+} -- a MAJORANA-TYPE
     field-content commitment, A PROPOSAL AT THE OWNER'S BAR AND ADOPTED NOWHERE.

GATES
  A  authority: main plus the TWO Block 179 artifacts content-bound, the parent
     runner ACTUALLY IMPORTED, the audit inputs readable, and the stale pin
     verified to carry NEITHER artifact.
  B  the two banners -- the inertia convention and the imposed-object banner with
     the SIGMA-REALITY PROPOSAL restated -- and BOTH bench fixtures rebuilt from
     LANDED modules with their inertia triples gated.
  C  THE FRAME LEGS: the joint-flip identity at BOTH extents, the single-flip
     defect counts, the self-conjugation counts that refute the fixed-point
     reading, X_0 unitary and involutive, and the NO-REGISTRATION channels.
  D  THE WITT LEG: the anti-diagonal reflected Gram rebuilt exactly at the
     875/1462 pattern, against the plain-Gram scalar contrast.
  E  THE WIGNER LEG: the six placement failures reproduced with the invariance
     condition A^T Q_D conj(A) = Q_D^T tested for all six, and the X_0-swap
     unitary invariance PASSING as the control.
  F  THE DET-EXPONENT LEG: the c-sector factor by BOTH routes, the beta and D4
     calibrations, the disconnection, and the arbiter composition to Q = 1.
  G  THE RESOLUTION AND THE PROPOSAL: the premise-free Q = 1 statement, the
     sigma-reality one-liner verbatim-keyed, the Fix involution verified
     IN-RUNNER, and the corrections ledger and stop/reopen sections present.
  H  note at final path, the FULL scope-key certificate, and the N5 fence.

BASELINE EXPECTATION: 7 of 8, with H failing on note-at-final-path alone until
the note is landed at docs/.

RUNNING
  python3 scripts/admissibility_dirac_kahler_orientation_bit_terminal_2026_08_24.py
  python3 ... --list-mutations
  python3 ... --mutation claim_quotient_true_of_measure
  python3 ... --deep

NOTES FOR THE LANDING AGENT
  1. PARENT_COMMIT is REAL and PARENT_REF resolves to it; nothing needs sed.
  2. CURRENT_MAIN was RE-RESOLVED at draft time.
  3. The stale pin is the Block 178 tip, a real ancestor of HEAD that carries
     NEITHER Block 179 artifact -- which is what makes the
     stale_parent_authority mutation bite.
  4. Re-run at landing; gate H should then pass and the battery should be 8/8.
"""

from __future__ import annotations

import argparse
import ast
import subprocess
import sys
import time
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

import sympy as sp

R = sp.Rational
Z0 = sp.Integer(0)
ONE = sp.Integer(1)
IU = sp.I

_FINAL_LOCATION_ROOT = Path(__file__).resolve().parents[1]
# This fallback keeps the scratchpad draft executable before it is moved to
# scripts/, where the final-location branch is used.
ROOT = (
    _FINAL_LOCATION_ROOT
    if (_FINAL_LOCATION_ROOT / ".git").exists()
    else Path(
        "/Users/jonBridger/Projects/Physics-baremetal-probes/"
        ".claude/worktrees/gravity-toe-lane-work-427b0b"
    )
)
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

# THE PARENT IMPORT.  Block 179 is the stack parent AND the content parent: it
# re-exports the whole landed chain, and its campaign is the one this block's
# arc terminates.  NOTHING from the scratchpad is imported anywhere in this
# runner; both fixtures below are rebuilt from LANDED modules reached through
# this import.
try:
    import admissibility_dirac_kahler_embedding_residues_campaign_close_2026_08_23 as b179
    PARENT_IMPORT_LANDED = True
except ModuleNotFoundError:                                   # unlanded parent
    b179 = None
    PARENT_IMPORT_LANDED = False

if b179 is not None:
    b178 = b179.b178
    b177 = b179.b177
    b176 = b179.b176
    b175 = b179.b175
    b174 = b179.b174
    b171 = b179.b171
    b170 = b179.b170
    b166 = b179.b166
    b165 = b179.b165
else:                                                  # pragma: no cover
    b178 = None
    b177 = None
    b176 = None
    b175 = None
    b174 = None
    import admissibility_dirac_kahler_generator_trilemma_kernel_2026_08_21 as b171
    b170 = b171.b170
    b166 = b170.b166
    b165 = b171.b165

herm = b171.herm
is_zero = b171.is_zero
Bench = b170.Bench
SX = b170.SX
ST = b170.ST
MASS = b170.MASS

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_ORIENTATION_BIT_TERMINAL_BOUNDED_THEOREM_"
    "NOTE_2026-08-24.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
# DECLARED DRAFT FALLBACK, read ONLY when the final path is absent.  Gate H
# requires the final path, so the fallback never makes a gate pass.
DRAFT_NOTE_PATH = Path(
    "/private/tmp/claude-502/"
    "-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-"
    "gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/"
    "scratchpad/block180_note_draft.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE SINGLE-PARENT PIN.  Block 179 is BOTH the stack parent and the content
# parent, so there are exactly TWO artifact pins.
BLOCK179_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_EMBEDDING_RESIDUES_CAMPAIGN_CLOSE_BOUNDED_"
    "THEOREM_NOTE_2026-08-23.md"
)
BLOCK179_RUNNER = (
    "scripts/admissibility_dirac_kahler_embedding_residues_campaign_close_"
    "2026_08_23.py"
)
PARENT_ARTIFACTS = (BLOCK179_NOTE, BLOCK179_RUNNER)
PARENT_ARTIFACT_BLOBS = (
    "9cde263d7a832ebd001b7ee4c0ebe616e73b9482",   # Block 179 note
    "85df3c0696955b2d979e4e1a9e77a31a4a117efc",   # Block 179 runner
)

# THE FLAVOR LANE'S FORK ARBITER, reached through the LANDED Block 176 loader.
# It is read from origin/main at Block 176's PINNED BLOB, it is NOT a worktree
# read, and it is NOT in AUDIT_INPUT_PATHS -- the same discipline Blocks 176-179
# landed.  Its own correctness is not checked here and its source sits OUTSIDE
# this runner's AST exactness surface, which is disclosed and not hidden.
FLAVOR_RUNNER = "scripts/berezin_detc_detr_fork_2026_06_04.py"
FLAVOR_FORK_NOTE = "docs/KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md"
FLAVOR_ARBITER_FUNCTIONS = ("r_from_slot_count", "q_from_r", "det_cpair",
                            "det_fraction", "complex_realification", "CPair", "F")

# Deliberately literal: this is the complete audit read surface.  Every entry is
# a WORKTREE-READABLE path at landing time, and the exercise packet is listed in
# full because its three computed legs are load-bearing here.  The flavor RUNNER
# is deliberately absent, because it is read from origin/main and never from the
# worktree.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_ORIENTATION_BIT_TERMINAL_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_EMBEDDING_RESIDUES_CAMPAIGN_CLOSE_BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "docs/KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md",
    "scripts/admissibility_dirac_kahler_embedding_residues_campaign_close_2026_08_23.py",
    "scripts/admissibility_dirac_kahler_shear_mirror_interference_2026_08_23.py",
    "scripts/admissibility_dirac_kahler_complex_structure_synthesis_2026_08_23.py",
    "scripts/admissibility_dirac_kahler_generator_trilemma_kernel_2026_08_21.py",
    "scripts/admissibility_dirac_kahler_closure_audit_two_2026_08_21.py",
    ".claude/science/physics-loops/generator-program-20260821/b182_frame_check_findings.md",
    ".claude/science/exercises/koide-counting-rule-decision-20260824/SYNTHESIS_FINAL.md",
    ".claude/science/exercises/koide-counting-rule-decision-20260824/SYNTHESIS_WITT_RESULT.md",
    ".claude/science/exercises/koide-counting-rule-decision-20260824/det_exponent_verdict.md",
    ".claude/science/exercises/koide-counting-rule-decision-20260824/det_exponent_probe.py",
    ".claude/science/exercises/koide-counting-rule-decision-20260824/ex1_assumptions_ledger.md",
    ".claude/science/exercises/koide-counting-rule-decision-20260824/ex2_first_principles_reduction.md",
    ".claude/science/exercises/koide-counting-rule-decision-20260824/ex3_literature_templates.md",
    ".claude/science/exercises/koide-counting-rule-decision-20260824/ex4_math_sector_search.md",
)
# THE BLOCK'S OWN NOTE is the one audit input gate A does NOT require readable,
# because it does not exist until landing and gate H is the gate that owns it.
SELF_NOTE_INPUT = AUDIT_INPUT_PATHS[0]

AUDIT_TIMEOUT_SEC = 600
# THE FIVE-PIN AUTHORITY BLOCK, single-line hex literals refreshed by anchored
# sed at landing.  CURRENT_MAIN WAS RE-RESOLVED AT DRAFT TIME.
CURRENT_MAIN = "c79384cb8ffa27fcb53cb89c53a84a708442eaad"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
# This block stacks on the Block 179 tip, so the parent branch is that.
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block179-"
              "embedding-residues-campaign-close-20260823")
PARENT_COMMIT = "a1c71f03e7474eb91aafce8958a1a02cb1e24930"
# The Block 178 tip: a real ancestor of HEAD that predates Block 179 and
# therefore carries NEITHER Block 179 artifact.  Read ONLY under the stale
# mutation, where the missing blobs are exactly what makes it bite.
STALE_PARENT_COMMIT = "5d8bc1e92be934cf3f90368f6cd0a68bb224d9fa"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "break_joint_flip_identity",
    "claim_bit_registrable",
    "break_witt_gram",
    "claim_line_counting_alive",
    "claim_wigner_plus_one",
    "claim_quotient_true_of_measure",
    "break_det_exponent",
    "claim_witt_decides_count",
    "claim_q_two_thirds_premise_free",
    "drop_sigma_reality_proposal",
    "drop_corrections_ledger",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_objects_registered": "B",
    "break_joint_flip_identity": "C",
    "claim_bit_registrable": "C",
    "break_witt_gram": "D",
    "claim_line_counting_alive": "D",
    "claim_wigner_plus_one": "E",
    "claim_quotient_true_of_measure": "F",
    "break_det_exponent": "F",
    "claim_witt_decides_count": "G",
    "claim_q_two_thirds_premise_free": "G",
    "drop_sigma_reality_proposal": "G",
    "drop_corrections_ledger": "G",
    "drop_n5_fence": "H",
}


class Checks:
    def __init__(self) -> None:
        self.results: list[tuple[str, str, bool]] = []

    def check(self, key: str, statement: str, condition: object) -> None:
        self.results.append((key, statement, bool(condition)))

    def report(self) -> None:
        for key, statement, value in self.results:
            print(f"[{'PASS' if value else 'FAIL'}] {key}: {statement}")
        print("GATES " + " ".join(
            f"{key}={'PASS' if value else 'FAIL'}"
            for key, _, value in self.results))

    def finish(self) -> int:
        passed = sum(value for _, _, value in self.results)
        failed = len(self.results) - passed
        print(f"TOTAL: PASS={passed} FAIL={failed}")
        return failed


# ---------------------------------------------------------------------------
# A. authority
# ---------------------------------------------------------------------------
def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=AUDIT_TIMEOUT_SEC).strip()


def worktree_blob(path: str) -> str:
    result = subprocess.run(
        ("git", "hash-object", path), cwd=ROOT, text=True,
        capture_output=True, check=False, timeout=AUDIT_TIMEOUT_SEC)
    return result.stdout.strip() if result.returncode == 0 else ""


def commit_blob(commit: str, path: str) -> str:
    result = subprocess.run(
        ("git", "rev-parse", f"{commit}:{path}"), cwd=ROOT, text=True,
        capture_output=True, check=False, timeout=AUDIT_TIMEOUT_SEC)
    return result.stdout.strip() if result.returncode == 0 else ""


def resolve_ref(ref: str) -> str:
    result = subprocess.run(
        ("git", "rev-parse", ref), cwd=ROOT, text=True,
        capture_output=True, check=False, timeout=AUDIT_TIMEOUT_SEC)
    return result.stdout.strip() if result.returncode == 0 else ""


def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, descendant),
        cwd=ROOT, check=False, capture_output=True,
        timeout=AUDIT_TIMEOUT_SEC).returncode == 0


def is_hash(value: str) -> bool:
    import re as _re
    return _re.fullmatch(r"[0-9a-f]{40}", value) is not None


def is_placeholder(value: str) -> bool:
    """A DECLARED placeholder is 40 hex characters that are all zero but the
    trailing block tag.  It is hash-SHAPED and is never a resolvable commit."""
    return is_hash(value) and value.startswith("0" * 30)


def audit_inputs_readable() -> tuple:
    """(readable count, missing paths).  THE BLOCK'S OWN NOTE IS EXCLUDED, since
    it does not exist until landing and gate H is the gate that owns it."""
    missing = tuple(
        path for path in AUDIT_INPUT_PATHS
        if path != SELF_NOTE_INPUT and not (ROOT / path).is_file())
    return len(AUDIT_INPUT_PATHS) - 1 - len(missing), missing


def raw_note() -> tuple:
    """(text, at_final_path).  The fallback is DECLARED and never hidden."""
    try:
        return NOTE_PATH.read_text(encoding="utf-8"), True
    except OSError:
        pass
    try:
        return DRAFT_NOTE_PATH.read_text(encoding="utf-8"), False
    except OSError:
        return "", False


def normalized_note(text: str) -> str:
    return " ".join(text.lower().split())


def no_float(value: object) -> bool:
    """The committed exactness predicate, reached through the landed chain."""
    return b165.no_float(value)


# THE AST GATE'S READ SURFACE.  It covers EVERY FILE THIS RUNNER READS CODE FROM
# in the runner chain -- this file AND the imported runner modules -- which is
# the Block 176/177/178/179 convention.  IT IS NOT the full transitive module
# closure, AND IT DOES NOT COVER THE FLAVOR ARBITER, which is read from
# origin/main through the landed Block 176 loader; gate A reports the residual
# count outside the surface rather than claiming the corpus clean.
def audit_source_paths() -> tuple:
    paths = [Path(__file__).resolve()]
    for module in (b179, b178, b177, b176, b175, b174, b171):
        if module is None:
            continue
        source = getattr(module, "__file__", None)
        if source:
            resolved = Path(source).resolve()
            if resolved not in paths:
                paths.append(resolved)
    return tuple(paths)


def source_float_literals() -> int:
    """AST self-check: NO float literal in ANY file read for code."""
    total = 0
    for path in audit_source_paths():
        tree = ast.parse(path.read_text(encoding="utf-8"))
        total += sum(1 for node in ast.walk(tree)
                     if isinstance(node, ast.Constant)
                     and isinstance(node.value, float))
    return total


BANNED_CALLS = ("nsim" + "plify", "evalf", "Fl" + "oat", "RealNumber")
_NS = BANNED_CALLS[0]


def source_forbidden_calls() -> int:
    """AST self-check: no nsimplify, no evalf, no Float in ANY such file."""
    banned = set(BANNED_CALLS)
    total = 0
    for path in audit_source_paths():
        tree = ast.parse(path.read_text(encoding="utf-8"))
        total += sum(1 for node in ast.walk(tree)
                     if (isinstance(node, ast.Attribute) and node.attr in banned)
                     or (isinstance(node, ast.Name) and node.id in banned))
    return total


def call_sites(text: str) -> int:
    """LIVE CALL SITES, not text mentions."""
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return -1
    return sum(1 for node in ast.walk(tree)
               if (isinstance(node, ast.Attribute) and node.attr == _NS)
               or (isinstance(node, ast.Name) and node.id == _NS))


def residue_report() -> dict:
    """The hygiene residue below the audit surface, COUNTED and never hidden."""
    chain = {}
    for name, module in (("b179", b179), ("b178", b178), ("b177", b177),
                         ("b176", b176), ("b175", b175), ("b174", b174),
                         ("b171", b171), ("b170", b170), ("b165", b165)):
        source = getattr(module, "__file__", None) if module is not None else None
        if source:
            text = Path(source).read_text(encoding="utf-8")
            chain[name] = (text.count(_NS), call_sites(text))
        else:
            chain[name] = (-1, -1)
    return {
        "per_module": chain,
        "call_sites_in_audit_surface": sum(
            chain[name][1]
            for name in ("b179", "b178", "b177", "b176", "b175", "b174",
                         "b171")),
        "call_sites_below_audit_surface": sum(
            chain[name][1] for name in ("b170", "b165")),
    }


@dataclass(frozen=True)
class AuthorityCertificate:
    fixed_authority: bool
    parent_pin_is_commit: bool
    parent_ref_and_ancestry: bool
    parent_artifact_blobs: bool
    stale_parent_artifact_blobs: bool
    stale_is_real_ancestor: bool
    stale_carries_neither_artifact: bool
    parent_import_landed: bool
    inputs_readable: int
    inputs_missing: tuple
    residue: dict


def resolved_parent_commit() -> str:
    if is_hash(PARENT_COMMIT) and not is_placeholder(PARENT_COMMIT):
        return PARENT_COMMIT
    resolved = resolve_ref(PARENT_REF)
    return resolved if is_hash(resolved) else git_output("rev-parse", "HEAD")


def authority_certificate(main_head: str) -> AuthorityCertificate:
    fixed_authority = bool(
        AUDIT_TIMEOUT_SEC == 600
        and main_head == CURRENT_MAIN
        and commit_blob("origin/main", AXIOM_PATH) == CURRENT_AXIOM_BLOB
        and commit_blob("origin/main", REGISTRY_PATH) == CURRENT_REGISTRY_BLOB
        and worktree_blob(AXIOM_PATH) == WORKTREE_AXIOM_BLOB
        and worktree_blob(REGISTRY_PATH) == WORKTREE_REGISTRY_BLOB)
    parent = resolved_parent_commit()
    worktree_blobs = tuple(worktree_blob(path) for path in PARENT_ARTIFACTS)
    committed_blobs = tuple(commit_blob(parent, p) for p in PARENT_ARTIFACTS)
    stale_blobs = tuple(
        commit_blob(STALE_PARENT_COMMIT, p) for p in PARENT_ARTIFACTS)
    readable, missing = audit_inputs_readable()
    return AuthorityCertificate(
        fixed_authority,
        is_hash(PARENT_COMMIT) and not is_placeholder(PARENT_COMMIT),
        bool(is_hash(parent) and is_ancestor(parent, "HEAD")
             and (is_placeholder(PARENT_COMMIT)
                  or resolve_ref(PARENT_REF) == PARENT_COMMIT)),
        bool(len(committed_blobs) == len(PARENT_ARTIFACTS) == 2
             and all(is_hash(v) for v in committed_blobs)
             and committed_blobs == worktree_blobs
             and committed_blobs == PARENT_ARTIFACT_BLOBS),
        # THE STALE LEG.  At the Block 178 tip NEITHER Block 179 artifact
        # exists, so this is False and the stale mutation fails gate A.
        bool(all(is_hash(v) for v in stale_blobs)
             and stale_blobs == worktree_blobs),
        is_ancestor(STALE_PARENT_COMMIT, "HEAD"),
        not any(is_hash(v) for v in stale_blobs),
        PARENT_IMPORT_LANDED,
        readable,
        missing,
        residue_report())


# ---------------------------------------------------------------------------
# the 180-specific layer
# ---------------------------------------------------------------------------
NUMERALS: list = []


def record(value):
    """Every reported numeral passes through here for the no-float gate."""
    NUMERALS.append(value)
    return value


# THE COMMITTED FIXTURES, declared as literals so every constant is auditable.
BIG_TAG, BIG_COVER, BIG_LX, BIG_PHYS, BIG_N = "12x6", 12, 6, 6, 36
SMALL_TAG, SMALL_COVER, SMALL_LX, SMALL_PHYS, SMALL_N = "8x4", 8, 4, 4, 16
CONST_VOLUME = R(7, 5)
REGION_PIN = 1
PINNED_LEVELS = (0, 1)
SHIFT = 2
# THE TWO DIAL SETTINGS, separated on purpose.
FRAME_SX = R(3, 5)
FRAME_ST = R(1, 4)
MEASURE_SX = R(3, 5)
MEASURE_ST = Z0
# THE DISCLOSED CYCLOTOMIC FIELD.  omega is an exact primitive cube root of
# unity and every non-rational entry below lies in Q(omega) = Q(sqrt(-3)).
OMEGA = (-ONE + sp.sqrt(3) * sp.I) / 2
J2 = sp.Matrix([[0, 1], [-1, 0]])

# THE FRAME LEG's exact literals, from the b182 check and reproduced here.
JOINT_FLIP_RESIDUAL = 0
SINGLE_FLIP_DEFECTS = {BIG_TAG: 84, SMALL_TAG: 32}
SELF_CONJUGATION_DEFECTS = {BIG_TAG: 144, SMALL_TAG: 56}
INERTIA = {BIG_TAG: (BIG_N, 0, 0), SMALL_TAG: (SMALL_N, 0, 0)}
TRACE_SQ_JOINT = {BIG_TAG: R(47794293, 896000),
                  SMALL_TAG: R(378637341, 17920000)}
TRACE_SQ_SPLIT = {BIG_TAG: R(82268811, 1792000),
                  SMALL_TAG: R(335627241, 17920000)}
PHYSICAL_EXTENTS = {BIG_TAG: (BIG_PHYS, BIG_LX), SMALL_TAG: (SMALL_PHYS, SMALL_LX)}

# THE WITT LEG's exact literals.
W1_ENTRY = R(875, 1462)
WITT_ANTIDIAGONAL = ((0, 3), (1, 2), (2, 1), (3, 0))
LINE_COUNT_DEAD = 4
CELL_COUNT = 2

# THE WIGNER LEG's exact literals: six placements, six failures, one control.
WIGNER_PLACEMENTS = ("r_diag", "rX0_diag", "X0r_diag",
                     "r_swap", "rX0_swap", "X0r_swap")
WIGNER_DEFECTS = (360, 336, 336, 336, 360, 360)
WIGNER_FAILURES = 6

# THE MEASURE LEG's exact literals.
SECTOR_A = R(43, 35)
SECTOR_D = R(129, 175)
CELL_UNIT = R(62866, 30625)
C_FACTOR = R(3952133956, 937890625)
DET_EXPONENT = 2
BETA_CALIBRATOR = R(3193, 2240)
D4_CALIBRATOR = R(1817, 1120)
SLICE_LEVEL = 1
K_ZERO = 0
PREMISE_FREE_R = ONE
PREMISE_FREE_Q = ONE
SIGMA_REAL_R = R(1, 2)
SIGMA_REAL_Q = R(2, 3)
SECTOR_REAL_DIMS = 8
FIX_REAL_DIMS = 2

RUNTIME_BUDGET_SEC = 150
DEEP_RUNTIME_BUDGET_SEC = 600
POOL_TWO_LEADS = 3
HANDOFF_ITEMS = 3
ARC_PRS = ("#7330", "#7331", "#7336", "#7337")
SISTER_PRS = ("#7332", "#7334", "#7335", "#7338")

# THE IMPOSED OBJECTS OF THIS BLOCK, declared as a literal so the banner is a
# measured object and not only prose.  NONE of them is registered or adopted.
IMPOSED_OBJECTS = (
    "the committed 12x6 CONSTANT-CARRIER fixture at T_phys = 6 and L_x = 6, and its 8x4 companion at T_phys = 4 and L_x = 4, region pin c = 1, shear zero on the pinned time levels {0,1} and CARRIER_SIGMA = 3/5 elsewhere, constant volume 7/5, mass 1",
    "the two dial settings this block separates: the FRAME BENCHMARK (s_x, s_t) = (3/5, 1/4), at which both couplings are live, and the MEASURE FIXTURE (s_x, s_t) = (3/5, 0), the landed b180/b181 fixture",
    "the LANDED STAGGERED GRADING X_0 = diag((-1)^(t+x)) -- unitary, involutive, real, local -- and the diagonal relabeling group {1, X_0, X_t, X_x} with X_0 = X_t X_x",
    "the chart translation U|t,x> = |t, x+2 mod L_x>, the chart-momentum characters f_k(t,p) = 3^(-1/2) sum_j omega^(-kj)|t, p+2j> and the DISCLOSED field Q(omega) = Q(sqrt(-3))",
    "the four record-slice eigenlines g_+, g_-, h_+, h_- at lam_+- = 43/35 +- (129/175) i, their Theta-orbits O_+ = {g_+, h_-} and O_- = {g_-, h_+}, and the antilinear sigma = -Theta o X_0",
    "the class-doubled carrier Q(+3/5) (+) Q(-3/5) and the six antiunitary placements built from r, r X_0 and X_0 r in diagonal and swap form",
    "the flavor lane's fork arbiter -- det_cpair, det_fraction, complex_realification, r_from_slot_count and q_from_r -- READ from landed authority through the landed Block 176 loader and never re-derived here",
    "the committed reflection, region pin, slice index set, class map CM-SITE, slot order and record-slice scope, inherited",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
# THE PROPOSALS AT THE OWNER'S BAR, declared as counted literals.  NONE is
# adopted and NONE is registered.
OWNER_BAR_ITEMS = (
    "THE SIGMA-REALITY CONDITION, in one line: 'the record-slice generation "
    "carrier is the sigma-real form Fix(-Theta o X_0).'  ADOPT gives Q = 2/3 "
    "with every other link committed and computed; DECLINE leaves Q = 1 as the "
    "committed measure's own value -- A PROPOSAL, replacing every prior form of "
    "the counting proposal on the bar",
    "THE REFLECTION-PAIRING READOUT PRINCIPLE: the reading of |det Q|^-2 as Z "
    "paired with its own reflection -- A PROPOSAL, standing from Blocks 176-178",
    "THE DRAWER ITEMS FROM THE PRIOR CAMPAIGNS, still standing and unadopted: "
    "the bridge axiom in the drawer; the design fork; the b141/b142 items; and "
    "e_x = -1",
)
# THE DECISION that belongs to the owner and is NOT taken here.
OWNER_DECISIONS = (
    "THE SIGMA-REALITY CONDITION ITSELF: whether the record-slice generation "
    "carrier is the sigma-real form.  It is a FIELD-CONTENT COMMITMENT, "
    "physical in kind, UNREGISTRABLE IN-CLASS by this block's own "
    "no-registration theorem, and it is DECIDABLE ONLY BY ADOPTION OR BY FUTURE "
    "PHYSICS.  It is named here and it is NOT decided here",
)
# THE ARC'S EIGHT SUPERVISOR CORRECTIONS, carried verbatim-keyed.
ARC_CORRECTIONS = (
    "THE WRAP HYPOTHESIS: that the reflection breaking was the antiperiodic "
    "wrap.  WRONG AND OWNED: at zero shear the defect is exactly 0 under BOTH "
    "tests at BOTH extents",
    "THE PIN HYPOTHESIS: that the breaking was dial-independent and not "
    "level-local.  WRONG AND OWNED: pinning the two region levels removes "
    "exactly their share, 64 -> 32 and 96 -> 64",
    "THE GEOMETRY-FREE SLOGAN: 'the mirror-symmetric sector is exactly the "
    "geometry-free sector'.  REFUTED by the exact volume counterexample "
    "(1,2,3,4)_x and REPLACED BY: SHEARS BREAK THE MIRROR; VOLUMES DO NOT",
    "THE FORCED-FORK AND UNIQUENESS CLAIM: that non-invariance FORCES herm() "
    "and makes |Z|^2 THE UNIQUE fork-independent positive sensitive window.  "
    "REFUTED: it blocks a CANONICAL reconstruction only, and the readout sits "
    "in a FAMILY",
    "THE MULTIPLICITY-DISSOLUTION CLAIM: that residue 3 was DISSOLVED AT "
    "COUNTING-BIT SCOPE.  REFUTED: the slot counter is ADDITIVE, so the full "
    "rank-12 eigenspace gives r = 6 and Q = 13/3",
    "THE THETA-ANTIPARTICLE READING: that the second orbit was the antiparticle "
    "half of the first.  REFUTED: theta CLOSES WITHIN each orbit, so each orbit "
    "already contains its own conjugate partner and the second orbit is a "
    "GENUINE SECOND DOUBLET CANDIDATE -- two orbits, two slots",
    "THE FRAME-QUOTIENT COUNTING READING: that X_0 makes the orientation pure "
    "frame data and therefore that frame-invariant counting must count the "
    "exchanged pair once.  CORRECTED BY THE b182 CHECK: the equivalence is "
    "HORIZONTAL between class points and NOT a fixed-point symmetry, the "
    "horizontal quotient still has TWO slot-orbits, and the sign-channel "
    "precedent entails invariant REPORTING and not slot-WEIGHTING",
    "THE WITT-DECIDES-THE-COUNT READING: that the physical pairing's Witt "
    "structure fixes r = 1/2.  CORRECTED BY THE DET-EXPONENT PROBE: it fixes "
    "THE UNIT AND NOT THE COUNT, the landed measure carries TWO cells, and "
    "READOUT STRUCTURE CANNOT DELETE INTEGRATION CONTENT",
)
# THE NEUTRAL FOUR-EXERCISE FAN-OUT, each returning NO DECISION ARGUED.
EXERCISE_WORKERS = (
    "ex1, THE ASSUMPTIONS LEDGER: swept the approved foundation and found NO "
    "counting rule, NO slot semantics, NO quotient rule and NO polarization "
    "selector anywhere in it; contributed the A1 presentation-invariance clause "
    "and the evenness-class convention question.  LEDGER VERDICT, NO RESOLUTION "
    "ARGUED",
    "ex2, THE FIRST-PRINCIPLES REDUCTION: found the wall is NOT a counting-rule "
    "question at all -- the count is fixed once record-slice FIELD CONTENT is "
    "stated, and the committed measure already states it; contributed "
    "sigma = -Theta o X_0 and the det-exponent probe direction with its THREE "
    "pre-declared exact outcomes",
    "ex3, THE EXTERNAL-TEMPLATE SURVEY: found NO template decides the bit from "
    "committed structure alone; contributed the Wigner/Herring corepresentation "
    "template with its magnetic group and its class-doubled carrier, FOR "
    "IN-FRAMEWORK RE-PROOF, and imported nothing as authority",
    "ex4, THE MATHEMATICS-SECTOR SEARCH: contributed the A6a object, the 4x4 "
    "Gram whose ZERO PATTERN decides isotropic against anisotropic, which "
    "became the Witt leg.  SEARCH AND REFRAMING ONLY, NO DECISION",
)
# THE THREE COMPUTED LEGS, which are what the fan-out made possible.
COMPUTED_LEGS = (
    "THE WITT UNIT THEOREM (readout): the reflected Gram is EXACTLY "
    "ANTI-DIAGONAL, every eigenline ISOTROPIC, each Theta-orbit ONE HYPERBOLIC "
    "CELL, the minimal readable unit the CELL, and line-counting at n = 4 DEAD "
    "BY COMPUTATION.  It fixes THE UNIT",
    "THE WIGNER SILENCE (symmetry): the magnetic Klein group has NO honest "
    "corepresentation on the class-doubled carrier -- six placements, six exact "
    "invariance failures, one PASSING unitary control -- so the Herring test is "
    "UNEVALUABLE and the leg is reported SILENT AND NOT FORCED",
    "THE DET-EXPONENT FACT (measure, arbiter-native): the c-sector's factor in "
    "the landed 12x6 partition function is EXACTLY (62866/30625)^2, TWO CELLS, "
    "verified two ways and calibrated against the accepted one-slot precedent.  "
    "It fixes THE COUNT, and it was run by a separate worker against a "
    "PRE-DECLARED three-outcome fork",
)
# THE STOP CONDITIONS and THE REOPENERS, declared as counted literals.
STOP_ITEMS = (
    "ALL COUNTING, CONVENTION AND FRAME ROUTES -- COMPUTED CLOSED, with exact "
    "residuals rather than judgement calls",
    "THE WIGNER/SYMMETRY ROUTE -- NO ACTION: the group does not act on the "
    "doubling, so there is nothing to test.  SILENT, NOT NEGATIVE",
    "FURTHER THEOREM ATTEMPTS ON THE SELECTION: three checker rounds plus this "
    "exercise, and the reason is now STRUCTURAL -- the selection is a "
    "field-content commitment and no theorem about readout, frame or symmetry "
    "can supply it",
    "THE KOIDE TAIL, per the owner's direction; the lane repoints to the "
    "gravity mainline",
)
REOPEN_ITEMS = (
    "THE FLAVOR LANE'S WRITER MECHANISM LANDS -- it would fix slot semantics "
    "DYNAMICALLY rather than by convention",
    "ANY LANDED RESULT FIXES SECTOR REALITY CONDITIONS -- precisely the input "
    "the sigma bit names, arriving from elsewhere",
    "AN ODD-EXTENT-COMPATIBLE GRADING VARIANT IS CONSTRUCTED -- it would make "
    "the orientation bit REGISTRABLE and void the no-registration theorem's "
    "scope",
    "THE SISTER LANE'S #7334 GRADING DERIVATION, ON REVIEW, BEARS ON THE "
    "MEASURE CALIBRATION -- the Wick tower separates vacuum 1 / Z_Q / |Z_Q|^2, "
    "and the det-exponent leg rests on which of those the landed Z is.  THAT "
    "REVIEW IS OPEN AND IS NOT PREJUDGED HERE",
)
# THE DRAFT WORKER'S CATCH, disclosed rather than absorbed.
DRAFT_WORKER_CATCHES = (
    "THIS BLOCK'S DRAFT -- THE SIX WIGNER FAILURES ARE NOT UNIFORM: the exercise "
    "packet reported six exact failures without their sizes, and the exact "
    "residual entry counts are 360, 336, 336, 336, 360, 360, which the runner "
    "now gates individually so a future modified doubling cannot be scored "
    "against a summary",
)


# ---------------------------------------------------------------------------
# the shared exact instruments
# ---------------------------------------------------------------------------
def exact_scalar(value):
    """Collapse a Q(sqrt(-3)) expression to its exact rational value.

    No float, no decimal and no banned simplifier is involved: this is sympy's
    exact radical/complex simplification over the DISCLOSED cyclotomic field.
    """
    return sp.cancel(sp.expand(sp.simplify(value)))


def matrix_zero(matrix: sp.MatrixBase) -> bool:
    return all(exact_scalar(entry) == 0 for entry in matrix)


def nonzero_entries(matrix: sp.MatrixBase) -> int:
    """THE DEFECT COUNT: exact nonzero entries after exact expansion."""
    return sum(1 for entry in sp.expand(matrix) if entry != 0)


def build_fixture(tag: str, cover_t: int, lx: int, sx, st):
    """A COMMITTED CONSTANT CARRIER, rebuilt from LANDED modules only.

    This is the Block 174 Width(., 'const') construction reproduced from its
    landed ingredients -- b170.Bench and b166.carrier_substitution -- and NOT
    imported from any scratchpad module.
    """
    bench = Bench(tag, cover_t, lx)
    fx = bench.fx
    pinned = {(bench.c - 1) % fx.PHYS_T, bench.c % fx.PHYS_T}
    field = {(t, x): (Z0 if t in pinned else b171.CARRIER_SIGMA, CONST_VOLUME)
             for (t, x) in fx.CELLS}
    sub = b166.carrier_substitution(fx, field)
    sub[SX] = sx
    sub[ST] = st
    sub[MASS] = b171.BENCH_MASS
    return bench, tuple(sorted(pinned)), sp.expand(bench.Q.subs(sub))


def staggered_grading(phys_t: int, lx: int) -> sp.Matrix:
    """THE LANDED GRADING X_0 = diag((-1)^(t+x)) on the quotient site order."""
    return sp.diag(*[sp.Integer(-1) ** (t + x)
                     for t in range(phys_t) for x in range(lx)])


# ---------------------------------------------------------------------------
# B. the fixtures and the banners
# ---------------------------------------------------------------------------
def measure_fixtures() -> dict:
    """BOTH COMMITTED FIXTURES, at both dial settings, exactly."""
    out: dict = {}
    for tag, cover_t, lx in ((BIG_TAG, BIG_COVER, BIG_LX),
                             (SMALL_TAG, SMALL_COVER, SMALL_LX)):
        bench, pinned, q_pp = build_fixture(tag, cover_t, lx, FRAME_SX, FRAME_ST)
        _, _, q_mm = build_fixture(tag, cover_t, lx, -FRAME_SX, -FRAME_ST)
        _, _, q_mp = build_fixture(tag, cover_t, lx, -FRAME_SX, FRAME_ST)
        _, _, q_pm = build_fixture(tag, cover_t, lx, FRAME_SX, -FRAME_ST)
        out[tag] = {
            "bench": bench, "pinned": pinned, "N": bench.N, "T_phys": bench.T,
            "lx": bench.lx, "c": bench.c,
            "Q_pp": q_pp, "Q_mm": q_mm, "Q_mp": q_mp, "Q_pm": q_pm,
            "symbol_free": not q_pp.free_symbols,
            "inertia": tuple(b165.real_symmetric_inertia(herm(q_pp))),
            "X0": staggered_grading(bench.T, bench.lx),
            "extents_even": bench.T % 2 == 0 and bench.lx % 2 == 0,
        }
    # THE MEASURE FIXTURE, at s_t = 0: the landed b180/b181 fixture on which the
    # Witt, Wigner and det-exponent legs run.
    bench, pinned, q_measure = build_fixture(
        BIG_TAG, BIG_COVER, BIG_LX, MEASURE_SX, MEASURE_ST)
    _, _, q_measure_minus = build_fixture(
        BIG_TAG, BIG_COVER, BIG_LX, -MEASURE_SX, MEASURE_ST)
    out["measure"] = {
        "bench": bench, "pinned": pinned, "N": bench.N, "T_phys": bench.T,
        "lx": bench.lx, "Q": q_measure, "Q_minus": q_measure_minus,
        "symbol_free": not q_measure.free_symbols,
        "X0": staggered_grading(bench.T, bench.lx),
        "carrier_sigma": b171.CARRIER_SIGMA, "volume": CONST_VOLUME,
    }
    return out


# ---------------------------------------------------------------------------
# C. THE FRAME LEGS and THE NO-REGISTRATION THEOREM
# ---------------------------------------------------------------------------
def measure_frame(fixtures: dict) -> dict:
    """THE JOINT FLIP, THE SINGLE FLIPS, THE SELF-CONJUGATION, THE CHANNELS."""
    out: dict = {}
    for tag in (BIG_TAG, SMALL_TAG):
        data = fixtures[tag]
        n, grading = data["N"], data["X0"]
        conjugated = sp.expand(grading * data["Q_pp"] * grading)
        leg = {
            # THE JOINT FLIP, exact at both extents.
            "joint_residual": nonzero_entries(conjugated - data["Q_mm"]),
            # EITHER SINGLE FLIP, and neither is available.
            "single_mp": nonzero_entries(conjugated - data["Q_mp"]),
            "single_pm": nonzero_entries(conjugated - data["Q_pm"]),
            # NOT A FIXED-POINT SYMMETRY, which is the check's correction.
            "self_defect": nonzero_entries(conjugated - data["Q_pp"]),
            "x0_involutive": sp.expand(grading * grading) == sp.eye(n),
            "x0_unitary": sp.expand(grading.H * grading) == sp.eye(n),
            "x0_real": all(entry.is_real for entry in grading),
            "extents_even": data["extents_even"],
            "physical_extents": (data["T_phys"], data["lx"]),
            "inertia": data["inertia"],
        }
        # THE NO-REGISTRATION CHANNELS: every committed-class readout is built
        # from these, and every one of them is conjugate across (+,+) <-> (-,-).
        reflection = data["bench"].r
        leg["commutes_with_reflection"] = is_zero(
            sp.expand(grading * reflection - reflection * grading))
        det_pp = data["Q_pp"].det()
        det_mm = data["Q_mm"].det()
        det_pm = data["Q_pm"].det()
        leg["det_conjugate"] = sp.expand(det_pp - det_mm) == 0
        variable = sp.Symbol("z")
        leg["spectrum_conjugate"] = (
            data["Q_pp"].charpoly(variable).all_coeffs()
            == data["Q_mm"].charpoly(variable).all_coeffs())
        g_pp = data["Q_pp"].inv(method="LU")
        g_mm = data["Q_mm"].inv(method="LU")
        leg["covariance_conjugate"] = is_zero(sp.expand(
            grading * herm(g_pp) * grading - herm(g_mm)))
        # THE INVARIANT THAT IS REGISTERED, and it carries no count.
        leg["trace_sq_pp"] = sp.expand((data["Q_pp"] * data["Q_pp"]).trace())
        leg["trace_sq_mm"] = sp.expand((data["Q_mm"] * data["Q_mm"]).trace())
        leg["trace_sq_pm"] = sp.expand((data["Q_pm"] * data["Q_pm"]).trace())
        leg["joint_class_agrees"] = leg["trace_sq_pp"] == leg["trace_sq_mm"]
        leg["classes_separate"] = leg["trace_sq_pp"] != leg["trace_sq_pm"]
        leg["det_separates_classes"] = sp.expand(det_pp - det_pm) != 0
        # THE TWO MEASURED FLAGS the two C mutations bite on.  BOTH ARE FALSE.
        leg["is_fixed_point_symmetry"] = leg["self_defect"] == 0
        leg["bit_is_registrable"] = not (
            leg["commutes_with_reflection"] and leg["det_conjugate"]
            and leg["spectrum_conjugate"] and leg["covariance_conjugate"]
            and leg["joint_class_agrees"])
        out[tag] = leg
    out["registration_needs_odd_extent"] = not (
        out[BIG_TAG]["extents_even"] and out[SMALL_TAG]["extents_even"]
        and out[BIG_TAG]["joint_residual"] == JOINT_FLIP_RESIDUAL
        and out[SMALL_TAG]["joint_residual"] == JOINT_FLIP_RESIDUAL) is False
    out["bit_is_registrable"] = (out[BIG_TAG]["bit_is_registrable"]
                                 or out[SMALL_TAG]["bit_is_registrable"])
    return out


# ---------------------------------------------------------------------------
# the record-slice sector: the objects the D, E, F and G legs share
# ---------------------------------------------------------------------------
def sector_objects(fixtures: dict) -> dict:
    """THE FOUR EIGENLINES, THEIR ORBITS, AND THE COVARIANCE, exactly."""
    data = fixtures["measure"]
    bench, action, n = data["bench"], data["Q"], data["N"]
    lx = data["lx"]

    def site(t: int, x: int) -> int:
        return lx * (t % data["T_phys"]) + (x % lx)

    def character(k: int, t: int, parity: int) -> sp.Matrix:
        vector = sp.zeros(n, 1)
        for index in range(3):
            vector[site(t, parity + SHIFT * index), 0] = (
                OMEGA ** ((-k * index) % 3) / sp.sqrt(3))
        return vector

    out: dict = {"site": site, "character": character}
    chart_one = character(1, SLICE_LEVEL, 0).row_join(character(1, SLICE_LEVEL, 1))
    chart_two = character(2, SLICE_LEVEL, 0).row_join(character(2, SLICE_LEVEL, 1))
    out["B1"], out["B2"] = chart_one, chart_two
    out["charts_orthonormal"] = (
        matrix_zero(chart_one.H * chart_one - sp.eye(2))
        and matrix_zero(chart_two.H * chart_two - sp.eye(2)))
    out["chart_blocks"] = (
        matrix_zero(sp.expand(chart_one.H * action * chart_one)
                    - (SECTOR_A * sp.eye(2) + SECTOR_D * J2))
        and matrix_zero(sp.expand(chart_two.H * action * chart_two)
                        - (SECTOR_A * sp.eye(2) + SECTOR_D * J2)))
    root_two = sp.sqrt(2)
    up = sp.Matrix([1, IU]) / root_two
    down = sp.Matrix([1, -IU]) / root_two
    g_plus, g_minus = chart_one * up, chart_one * down
    h_plus, h_minus = chart_two * up, chart_two * down
    out["lines"] = {"g+": g_plus, "g-": g_minus, "h+": h_plus, "h-": h_minus}
    out["order"] = ("g+", "g-", "h+", "h-")
    lam_plus = SECTOR_A + SECTOR_D * IU
    lam_minus = SECTOR_A - SECTOR_D * IU
    out["lam"] = (lam_plus, lam_minus)
    out["eigenlines_exact"] = all(matrix_zero(action * vec - lam * vec) for vec, lam
                                  in ((g_plus, lam_plus), (g_minus, lam_minus),
                                      (h_plus, lam_plus), (h_minus, lam_minus)))
    reflection = bench.r
    out["reflection"] = reflection
    out["reflection_acts_as_identity"] = (
        matrix_zero(reflection * chart_one - chart_one)
        and matrix_zero(reflection * chart_two - chart_two))

    def theta(vector: sp.Matrix) -> sp.Matrix:
        return reflection * vector.conjugate()

    out["theta"] = theta
    out["orbits_exact"] = (
        matrix_zero(theta(g_plus) - h_minus)
        and matrix_zero(theta(g_minus) - h_plus)
        and matrix_zero(theta(h_minus) - g_plus)
        and matrix_zero(theta(h_plus) - g_minus))
    out["orbits"] = (("g+", "h-"), ("g-", "h+"))

    # THE COMMITTED COVARIANCE, assembled over the landed disconnection.
    slice_rows = [site(SLICE_LEVEL, x) for x in range(lx)]
    complement = [i for i in range(n) if i not in slice_rows]
    out["slice_rows"], out["complement"] = slice_rows, complement
    out["disconnection"] = all(
        action[i, j] == 0 and action[j, i] == 0
        for i in slice_rows for j in complement)
    slice_block = action[slice_rows, slice_rows]
    rest_block = action[complement, complement]
    out["slice_block"], out["rest_block"] = slice_block, rest_block
    slice_inverse = slice_block.inv(method="LU")
    rest_inverse = rest_block.inv(method="LU")
    covariance = sp.zeros(n, n)
    for a, i in enumerate(slice_rows):
        for b, j in enumerate(slice_rows):
            covariance[i, j] = slice_inverse[a, b]
    for a, i in enumerate(complement):
        for b, j in enumerate(complement):
            covariance[i, j] = rest_inverse[a, b]
    out["G"] = covariance
    out["covariance_exact"] = is_zero(sp.expand(action * covariance - sp.eye(n)))
    out["W9"] = sp.expand((covariance + covariance.T) / 2)
    return out


# ---------------------------------------------------------------------------
# D. THE WITT LEG
# ---------------------------------------------------------------------------
def measure_witt(sector: dict) -> dict:
    """THE PLAIN GRAM, THE REFLECTED GRAM, AND THE ISOTROPY."""
    out: dict = {}
    weight = sector["W9"]
    order = sector["order"]
    lines = [sector["lines"][name] for name in order]
    plain = sp.Matrix(4, 4, lambda i, j: exact_scalar(
        (lines[i].H * weight * lines[j])[0]))
    out["plain"] = plain
    out["plain_is_scalar"] = plain == W1_ENTRY * sp.eye(4)
    out["plain_self_pairings"] = tuple(plain[i, i] for i in range(4))
    reflected = sp.Matrix(4, 4, lambda i, j: exact_scalar(
        (sector["theta"](lines[i]).H * weight * lines[j])[0]))
    out["reflected"] = reflected
    out["diagonal_all_zero"] = all(reflected[i, i] == 0 for i in range(4))
    out["antidiagonal_entries"] = tuple(
        reflected[i, j] for i, j in WITT_ANTIDIAGONAL)
    out["antidiagonal_uniform"] = all(
        reflected[i, j] == W1_ENTRY for i, j in WITT_ANTIDIAGONAL)
    out["off_pattern_zero"] = all(
        reflected[i, j] == 0 for i in range(4) for j in range(4)
        if (i, j) not in WITT_ANTIDIAGONAL)
    out["every_line_isotropic"] = out["diagonal_all_zero"]
    # EACH ORBIT IS ONE HYPERBOLIC CELL: the 2x2 restriction on each orbit is
    # exactly the hyperbolic form, off-diagonal only.
    cells = {}
    for orbit in sector["orbits"]:
        idx = [order.index(name) for name in orbit]
        cell = sp.Matrix(2, 2, lambda i, j: reflected[idx[i], idx[j]])
        cells[orbit] = cell
    out["cells"] = cells
    out["cells_hyperbolic"] = all(
        cell[0, 0] == 0 and cell[1, 1] == 0
        and cell[0, 1] == W1_ENTRY and cell[1, 0] == W1_ENTRY
        for cell in cells.values())
    out["cell_count"] = len(cells)
    out["cell_det_content"] = exact_scalar(SECTOR_A ** 2 + SECTOR_D ** 2)
    # THE MEASURED FLAG the line-counting mutation bites on.  It is FALSE: a
    # lone eigenline cannot be normed, so line counting is not available.
    out["line_counting_alive"] = not out["every_line_isotropic"]
    out["line_count_if_alive"] = LINE_COUNT_DEAD
    return out


# ---------------------------------------------------------------------------
# E. THE WIGNER LEG
# ---------------------------------------------------------------------------
def measure_wigner(fixtures: dict, sector: dict) -> dict:
    """SIX ANTIUNITARY PLACEMENTS, SIX FAILURES, ONE PASSING UNITARY CONTROL."""
    out: dict = {}
    data = fixtures["measure"]
    n = data["N"]
    action, action_minus, grading = data["Q"], data["Q_minus"], data["X0"]
    out["class_doubling_exact"] = is_zero(
        sp.expand(grading * action * grading - action_minus))
    zero_block = sp.zeros(n, n)
    doubled = sp.Matrix(sp.BlockMatrix([[action, zero_block],
                                        [zero_block, action_minus]]))
    out["doubled_dimension"] = doubled.shape[0]
    reflection = sector["reflection"]
    generators = {
        "r": reflection,
        "rX0": sp.expand(reflection * grading),
        "X0r": sp.expand(grading * reflection),
    }
    transposed = doubled.T
    defects = {}
    for form in ("diag", "swap"):
        for name, generator in generators.items():
            placement = (
                sp.Matrix(sp.BlockMatrix([[generator, zero_block],
                                          [zero_block, generator]]))
                if form == "diag" else
                sp.Matrix(sp.BlockMatrix([[zero_block, generator],
                                          [generator, zero_block]])))
            # THE ANTIUNITARY INVARIANCE CONDITION, exactly as the template
            # states it: A^T Q_D conj(A) = Q_D^T.
            residual = sp.expand(
                placement.T * doubled * placement.conjugate() - transposed)
            defects[f"{name}_{form}"] = nonzero_entries(residual)
    out["defects"] = defects
    out["defect_tuple"] = tuple(defects[name] for name in WIGNER_PLACEMENTS)
    out["placements_tested"] = len(defects)
    out["failures"] = sum(1 for value in defects.values() if value != 0)
    # THE CONTROL: the unitary X_0-swap IS an exact symmetry of the doubling,
    # so the halving subgroup does act and the doubling is not vacuous.
    swap = sp.Matrix(sp.BlockMatrix([[zero_block, grading],
                                     [grading, zero_block]]))
    out["control_passes"] = is_zero(sp.expand(swap.H * doubled * swap - doubled))
    out["control_unitary"] = sp.expand(swap.H * swap) == sp.eye(2 * n)
    # THE MEASURED FLAG the wigner mutation bites on.  It is FALSE: with no
    # honest corepresentation the Herring character sum cannot be evaluated.
    out["herring_evaluable"] = out["failures"] < len(defects)
    return out


# ---------------------------------------------------------------------------
# F. THE DET-EXPONENT LEG
# ---------------------------------------------------------------------------
def load_fork_arbiter() -> tuple:
    """The flavor lane's OWN arbiter, through the LANDED Block 176 loader."""
    if b176 is None:                                       # pragma: no cover
        return {}, ""
    arbiter, seen = b176.load_fork_arbiter()
    return arbiter, seen


def measure_exponent(fixtures: dict, sector: dict) -> dict:
    """THE C-SECTOR FACTOR BY BOTH ROUTES, AND ITS TWO CALIBRATORS."""
    out: dict = {}
    data = fixtures["measure"]
    action = data["Q"]
    arbiter, blob = load_fork_arbiter()
    out["arbiter_blob"] = blob
    out["arbiter_loaded"] = bool(arbiter) and all(
        name in arbiter for name in FLAVOR_ARBITER_FUNCTIONS)
    if not out["arbiter_loaded"]:                          # pragma: no cover
        return out
    pair_type, fraction = arbiter["CPair"], arbiter["F"]

    def to_pair(value):
        return pair_type(fraction(sp.re(value)), fraction(sp.im(value)))

    # THE DISCONNECTION makes the restriction a TRUE Z-factor.
    slice_block, rest_block = sector["slice_block"], sector["rest_block"]
    det_full = action.det()
    det_slice = slice_block.det()
    det_rest = rest_block.det()
    out["disconnection"] = sector["disconnection"]
    out["det_factorizes"] = sp.expand(det_full - det_slice * det_rest) == 0

    # ROUTE ONE: the flavor arbiter's OWN det_cpair on the sector block.
    lam_plus, lam_minus = sector["lam"]
    order = sector["order"]
    lines = [sector["lines"][name] for name in order]
    basis = lines[0].row_join(lines[1]).row_join(lines[2]).row_join(lines[3])
    sector_block = sp.expand(basis.H * action * basis)
    out["sector_block_diagonal"] = matrix_zero(
        sector_block - sp.diag(lam_plus, lam_minus, lam_plus, lam_minus))
    arbiter_factor = arbiter["det_cpair"](
        tuple(tuple(to_pair(sector_block[i, j]) for j in range(4))
              for i in range(4)))
    out["arbiter_factor_real"] = arbiter_factor.im == fraction(0)
    out["arbiter_factor_matches"] = (
        arbiter_factor.re == fraction(C_FACTOR.p, C_FACTOR.q))

    # ROUTE TWO: the BASIS-FREE site extraction det(slice)/det(k = 0 fiber).
    character = sector["character"]
    fiber = character(K_ZERO, SLICE_LEVEL, 0).row_join(
        character(K_ZERO, SLICE_LEVEL, 1))
    fiber_block = sp.expand(fiber.H * action * fiber)
    out["basis_free_factor"] = exact_scalar(det_slice / fiber_block.det())
    out["routes_agree"] = out["basis_free_factor"] == C_FACTOR
    out["unit"] = exact_scalar(SECTOR_A ** 2 + SECTOR_D ** 2)
    out["exponent"] = (DET_EXPONENT if out["basis_free_factor"] == CELL_UNIT ** 2
                       else (1 if out["basis_free_factor"] == CELL_UNIT else 0))

    # CALIBRATOR ONE: the accepted one-slot precedent, reproduced.
    beta = exact_scalar((character(1, 0, 0).H * action * character(1, 0, 0))[0])
    out["beta"] = beta
    out["beta_first_power"] = (
        arbiter["det_cpair"](((to_pair(beta),),)).re
        == fraction(BETA_CALIBRATOR.p, BETA_CALIBRATOR.q))
    out["beta_realified_square"] = (
        arbiter["det_fraction"](arbiter["complex_realification"](to_pair(beta)))
        == fraction(BETA_CALIBRATOR.p, BETA_CALIBRATOR.q) ** 2)

    # CALIBRATOR TWO: the level-4 singleton fiber and the b = a s_x law.
    level_four = character(1, 4, 0).row_join(character(1, 4, 1))
    d_four = sp.expand(level_four.H * action * level_four)
    a_four, b_four = exact_scalar(d_four[0, 0]), exact_scalar(d_four[0, 1])
    out["d4_a"], out["d4_b"] = a_four, b_four
    out["d4_law"] = (a_four == D4_CALIBRATOR
                     and b_four == a_four * MEASURE_SX
                     and matrix_zero(d_four - (a_four * sp.eye(2) + b_four * J2)))
    out["d4_det_first_power"] = exact_scalar(
        d_four.det() - (a_four ** 2 + b_four ** 2)) == 0
    site = sector["site"]
    out["d4_chain_coupled"] = any(
        action[site(4, x), site(other, y)] != 0
        for x in range(data["lx"]) for other in (3, 5) for y in range(data["lx"]))

    # THE COVARIANCE PIN: the full unconstrained-Gaussian signature.
    covariance = sector["G"]
    target = (SECTOR_A * sp.eye(2) - SECTOR_D * J2) / out["unit"]
    out["full_covariance"] = (
        matrix_zero(sp.expand(sector["B1"].H * covariance * sector["B1"]) - target)
        and matrix_zero(sp.expand(sector["B2"].H * covariance * sector["B2"])
                        - target))
    out["sector_real_dims"] = SECTOR_REAL_DIMS
    out["w1_cross_check"] = matrix_zero(
        sp.expand(sector["B1"].H * sector["W9"] * sector["B1"])
        - W1_ENTRY * sp.eye(2))

    # THE ARBITER COMPOSITION, in the arbiter's own functions.
    slots = out["exponent"]
    premise_free_r = arbiter["r_from_slot_count"](slots)
    premise_free_q = arbiter["q_from_r"](premise_free_r)
    halved_r = arbiter["r_from_slot_count"](1)
    halved_q = arbiter["q_from_r"](halved_r)
    out["premise_free_r"] = R(Fraction(premise_free_r).numerator,
                              Fraction(premise_free_r).denominator)
    out["premise_free_q"] = R(Fraction(premise_free_q).numerator,
                              Fraction(premise_free_q).denominator)
    out["halved_r"] = R(Fraction(halved_r).numerator,
                        Fraction(halved_r).denominator)
    out["halved_q"] = R(Fraction(halved_q).numerator,
                        Fraction(halved_q).denominator)
    # THE MEASURED FLAG the F mutations bite on.  The exponent is 2.
    out["quotient_true_of_measure"] = out["exponent"] == 1
    return out


# ---------------------------------------------------------------------------
# G. THE RESOLUTION: sigma, its fixed form, and the corrected reading
# ---------------------------------------------------------------------------
def measure_sigma(fixtures: dict, sector: dict) -> dict:
    """sigma = -Theta o X_0 VERIFIED IN-RUNNER: antilinear, involutive, Fix."""
    out: dict = {}
    grading = fixtures["measure"]["X0"]
    reflection = sector["reflection"]
    lines = sector["lines"]
    g_plus, h_plus = lines["g+"], lines["h+"]
    g_minus, h_minus = lines["g-"], lines["h-"]

    def sigma(vector: sp.Matrix) -> sp.Matrix:
        return -reflection * grading * vector.conjugate()

    # THE GRADING'S ACTION ON THE LINES, which is what makes sigma close on E_+.
    out["grading_maps_lines"] = (
        matrix_zero(grading * g_plus + g_minus)
        and matrix_zero(grading * h_minus + h_plus))
    out["sigma_swaps"] = (matrix_zero(sigma(g_plus) - h_plus)
                          and matrix_zero(sigma(h_plus) - g_plus))
    out["sigma_involutive"] = (matrix_zero(sigma(sigma(g_plus)) - g_plus)
                               and matrix_zero(sigma(sigma(h_plus)) - h_plus))
    # ANTILINEARITY, tested on the imaginary unit and on additivity.
    out["sigma_antilinear"] = (
        matrix_zero(sp.expand(sigma(IU * g_plus) + IU * sigma(g_plus)))
        and matrix_zero(sp.expand(sigma(g_plus + h_plus)
                                  - sigma(g_plus) - sigma(h_plus))))
    # FIX(sigma) = {z g_+ + zbar h_+}, real-2-dimensional.
    first = sp.expand(g_plus + h_plus)
    second = sp.expand(IU * (g_plus - h_plus))
    out["fix_basis_fixed"] = (matrix_zero(sp.expand(sigma(first) - first))
                              and matrix_zero(sp.expand(sigma(second) - second)))
    out["fix_real_dims"] = FIX_REAL_DIMS
    out["fix_independent"] = sp.Matrix.hstack(first, second).rank() == 2
    # A GENERAL MEMBER of the stated form is fixed, and a NON-member is not.
    x_sym, y_sym = sp.symbols("x y", real=True)
    z_sym = x_sym + IU * y_sym
    general = sp.expand(z_sym * g_plus + sp.conjugate(z_sym) * h_plus)
    out["fix_form_exact"] = matrix_zero(sp.expand(sigma(general) - general))
    out["non_member_moves"] = not matrix_zero(
        sp.expand(sigma(g_plus) - g_plus))
    out["sigma_uses_landed_objects_only"] = bool(
        out["grading_maps_lines"] and sector["orbits_exact"])
    out["second_orbit_present"] = (
        not matrix_zero(g_minus - g_plus) and not matrix_zero(h_minus - h_plus))
    return out


# ---------------------------------------------------------------------------
# the scope-key certificate
# ---------------------------------------------------------------------------
SCOPE_KEYS = (
    # --- N0 ---------------------------------------------------------------
    "convention_banner",
    "convention_hazard_order",
    "convention_collision_named",
    "convention_literal_collision",
    "neither_helper_wrong",
    "both_inertia_triples",
    "imposed_object_banner",
    "nothing_registered",
    "measured_never_registered",
    "nothing_adopted",
    "owner_bar",
    "proposals_stay_proposals",
    "sigma_proposal_banner",
    "imported_authority",
    # --- W1 ---------------------------------------------------------------
    "w1",
    "campaign_thesis",
    "parent_block",
    "parent_pr",
    "synthesis_pr",
    "symmetric_power_pr",
    "mirror_pr",
    "four_routes",
    "terminates_with_computed_legs",
    "open_gates_content",
    # --- N1 ---------------------------------------------------------------
    "frame_theorem",
    "joint_flip_identity",
    "single_flip_defects",
    "self_conjugation_defects",
    "not_fixed_point_symmetry",
    "checker_correction_disclosed",
    "horizontal_equivalence",
    "two_fiber_slots",
    "reporting_not_weighting",
    "descent_evenness",
    "existence_not_licence",
    "no_registration_theorem",
    "no_channel_detects",
    "registering_geometries",
    "triple_sign_invariant",
    "count_neutral",
    "trace_sq_literals",
    "non_supply_scope",
    # --- N2 ---------------------------------------------------------------
    "three_computed_legs",
    "synthesis_governing",
    "witt_unit_theorem",
    "plain_gram_scalar",
    "reflected_gram_antidiagonal",
    "witt_entry_literal",
    "every_line_isotropic",
    "orbit_one_cell",
    "lone_line_unreadable",
    "minimal_readable_unit",
    "line_counting_dead",
    "wigner_silence",
    "magnetic_klein_group",
    "six_placements",
    "six_failures",
    "wigner_defect_literals",
    "control_passes",
    "herring_unevaluable",
    "silent_not_forced",
    "det_exponent_fact",
    "arbiter_native",
    "c_factor_literal",
    "exponent_two",
    "unit_literal",
    "two_routes",
    "basis_free_route",
    "disconnection_z_factor",
    "beta_calibrator",
    "d4_calibrator",
    "b_equals_a_sx",
    "unconstrained_gaussian",
    # --- N3 ---------------------------------------------------------------
    "resolution_premise_free",
    "two_cells",
    "premise_free_r",
    "premise_free_q",
    "additive_true_of_measure",
    "quotient_false_of_structure",
    "witt_reading_quoted",
    "eighth_correction",
    "unit_not_count",
    "readout_cannot_delete",
    "det_blind_windows",
    "window_invisible",
    # --- N4 ---------------------------------------------------------------
    "one_named_input",
    "sigma_definition",
    "antilinear_involution",
    "sigma_square",
    "fix_form",
    "majorana_type",
    "not_a_counting_convention",
    "physical_in_kind",
    "unregistrable_in_class",
    "adoption_or_future_physics",
    "sigma_reality_proposal",
    "adopt_branch",
    "decline_branch",
    "replaces_prior_forms",
    "phenomenological_note",
    "owner_weighing_not_derivation",
    # --- N5 ---------------------------------------------------------------
    "n5_verbatim",
    # --- N6 ---------------------------------------------------------------
    "stop_reopen",
    "routes_computed_closed",
    "wigner_no_action",
    "koide_stops",
    "reopen_writer_mechanism",
    "reopen_sector_reality",
    "reopen_odd_extent",
    "reopen_sister_lane",
    "review_not_prejudged",
    # --- N7 ---------------------------------------------------------------
    "arc_ledger",
    "corrections_ledger",
    "eight_corrections",
    "correction_wrap",
    "correction_pin",
    "correction_slogan",
    "correction_forced_fork",
    "correction_multiplicity",
    "correction_theta_antiparticle",
    "correction_frame_quotient",
    "correction_witt_count",
    "checker_overrides",
    "neutral_fanout",
    "fanout_decided_nothing",
    "no_rule_in_foundation",
    "pre_declared_fork",
    "verification_structure_working",
    "cycle913_caution",
    "non_supply_never_necessity",
    "candidacy_never_nature",
    "worker_profile",
    "supervisor_inline_science",
    "four_neutral_workers",
    "det_probe_worker",
    "codex_checks",
    "opus_mechanical_only",
    "common_mode",
    # --- N8 ---------------------------------------------------------------
    "verdict",
    "successor_question",
    "two_fixtures",
    "measure_leg_scoped",
    "wigner_silent_not_negative",
    "no_priority_claim",
    "n1_n8",
    "not_re_verified",
    "not_continuum",
    "not_a_flavor_bridge",
    "not_a_koide_derivation",
    "not_a_born_derivation",
    "ast_surface_disclosed",
    "no_float",
    "scope_key_certificate",
    "no_volume_average",
    "rho_guard",
    "zero_retirement",
    "zero_score",
    "zero_e2e",
    "axiom",
    "campaign_cited",
    "gravity_campaign_cited",
    "packet_cited",
    "frame_check_cited",
)

# THE RESOLUTION SECTION's own required subset, which is what gate G reads and
# what the two drop mutations remove a member of.
RESOLUTION_KEYS = (
    "resolution_premise_free",
    "two_cells",
    "premise_free_r",
    "premise_free_q",
    "additive_true_of_measure",
    "quotient_false_of_structure",
    "witt_reading_quoted",
    "eighth_correction",
    "unit_not_count",
    "readout_cannot_delete",
    "one_named_input",
    "sigma_definition",
    "antilinear_involution",
    "sigma_square",
    "fix_form",
    "majorana_type",
    "not_a_counting_convention",
    "physical_in_kind",
    "unregistrable_in_class",
    "adoption_or_future_physics",
    "sigma_reality_proposal",
    "adopt_branch",
    "decline_branch",
    "phenomenological_note",
    "owner_weighing_not_derivation",
    "stop_reopen",
    "routes_computed_closed",
    "reopen_writer_mechanism",
    "reopen_sector_reality",
    "reopen_odd_extent",
    "reopen_sister_lane",
    "corrections_ledger",
    "eight_corrections",
    "correction_theta_antiparticle",
    "correction_frame_quotient",
    "correction_witt_count",
    "checker_overrides",
    "neutral_fanout",
)


def scope_certificate(note_text: str) -> dict:
    note = normalized_note(note_text)
    return {
        # --- N0 -------------------------------------------------------------
        "convention_banner": "(n_+, n_-, n_0)" in note,
        "convention_hazard_order": "(n_+, n_0, n_-)" in note,
        "convention_collision_named": "congruence_inertia" in note
        and "real_symmetric_inertia" in note,
        "convention_literal_collision": "(4,4,0)" in note,
        "neither_helper_wrong": "neither helper is wrong" in note,
        "both_inertia_triples": "(36,0,0)(n+,n-,n0)[b165]" in note
        and "(16,0,0)(n+,n-,n0)[b165]" in note,
        "imposed_object_banner": "imposed measured object" in note,
        "nothing_registered": "nothing here is registered" in note,
        "measured_never_registered": "measured" in note
        and "never registered" in note,
        "nothing_adopted": "nothing is adopted" in note,
        "owner_bar": "the owner's bar" in note,
        "proposals_stay_proposals": "proposals stay proposals" in note,
        "sigma_proposal_banner":
            "the sigma-reality condition remains a proposal at the owner's bar"
            in note,
        "imported_authority": "imported authority" in note,
        # --- W1 -------------------------------------------------------------
        "w1": __import__("re").search(r"\bw1\b", note) is not None,
        "campaign_thesis": "the campaign thesis" in note,
        "parent_block": "block 179" in note,
        "parent_pr": "#7337" in note,
        "synthesis_pr": "#7330" in note,
        "symmetric_power_pr": "#7331" in note,
        "mirror_pr": "#7336" in note,
        "four_routes": "four routes were live at the wall" in note,
        "terminates_with_computed_legs":
            "terminates the orientation-bit and counting question with "
            "computed legs" in note,
        "open_gates_content": "open-gates content" in note,
        # --- N1 -------------------------------------------------------------
        "frame_theorem": "the frame theorem" in note,
        "joint_flip_identity":
            "x_0 q(+s_x, +s_t) x_0 - q(-s_x, -s_t) = 0" in note,
        "single_flip_defects":
            "84 nonzero entries at 12x6 and 32 at 8x4" in note,
        "self_conjugation_defects":
            "144 nonzero entries at 12x6 and 56 at 8x4" in note,
        "not_fixed_point_symmetry":
            "not a symmetry of the supplied-sign benchmark point" in note,
        "checker_correction_disclosed":
            "the adversarial check corrected that reading and this note "
            "carries the correction" in note,
        "horizontal_equivalence":
            "horizontal equivalence between class points" in note,
        "two_fiber_slots": "two fiber slots" in note,
        "reporting_not_weighting":
            "invariant reporting and not orbit slot-weighting" in note,
        "descent_evenness": "iff both physical extents are even" in note,
        "existence_not_licence":
            "existence in-class is not a licence to quotient" in note,
        "no_registration_theorem": "the no-registration theorem" in note,
        "no_channel_detects":
            "no committed-class channel detects the overall orientation" in note,
        "registering_geometries":
            "the geometries that would register it are exactly the ones where "
            "the grading fails to descend" in note,
        "triple_sign_invariant": "sigma s_x s_t" in note,
        "count_neutral": "count-neutral" in note,
        "trace_sq_literals": "47794293/896000" in note
        and "82268811/1792000" in note and "378637341/17920000" in note
        and "335627241/17920000" in note,
        "non_supply_scope":
            "non-supply result at committed-class scope" in note,
        # --- N2 -------------------------------------------------------------
        "three_computed_legs": "the three computed legs" in note,
        "synthesis_governing": "is the governing statement" in note,
        "witt_unit_theorem": "the witt unit theorem" in note,
        "plain_gram_scalar": "the plain w9 gram is the scalar" in note,
        "reflected_gram_antidiagonal": "the reflected (os) gram" in note
        and "is exactly anti-diagonal" in note,
        "witt_entry_literal": "875/1462" in note,
        "every_line_isotropic": "every eigenline is isotropic" in note,
        "orbit_one_cell": "orbit is exactly one hyperbolic cell" in note,
        "lone_line_unreadable": "a lone eigenline is unreadable" in note,
        "minimal_readable_unit":
            "the minimal readable object is the orbit-cell" in note,
        "line_counting_dead": "line-counting" in note
        and "is dead by computation" in note,
        "wigner_silence": "the wigner silence" in note,
        "magnetic_klein_group":
            "the magnetic klein group has no honest corepresentation" in note,
        "six_placements": "six placements" in note,
        "six_failures": "all six fail" in note,
        "wigner_defect_literals": "360, 336, 336, 336, 360, 360" in note,
        "control_passes": "the unitary control passes exactly" in note,
        "herring_unevaluable": "cannot be evaluated" in note,
        "silent_not_forced": "silent, not forced" in note,
        "det_exponent_fact": "the det-exponent fact" in note,
        "arbiter_native": "the arbiter-native leg" in note,
        "c_factor_literal": "3952133956/937890625" in note,
        "exponent_two": "exponent 2, not 1" in note,
        "unit_literal": "62866/30625" in note,
        "two_routes": "measured two independent ways" in note,
        "basis_free_route": "det(slice)/det(k=0 fiber)" in note,
        "disconnection_z_factor": "makes the restriction a true" in note,
        "beta_calibrator": "3193/2240" in note,
        "d4_calibrator": "1817/1120" in note,
        "b_equals_a_sx": "b = a s_x" in note,
        "unconstrained_gaussian": "the unconstrained-gaussian signature" in note,
        # --- N3 -------------------------------------------------------------
        "resolution_premise_free":
            "what the committed structure says, premise-free" in note,
        "two_cells": "n = 2" in note,
        "premise_free_r": "r = 1" in note,
        "premise_free_q": "q = 1" in note,
        "additive_true_of_measure":
            "the additive branch is true of the landed measure" in note,
        "quotient_false_of_structure":
            "quotient counting is false of committed structure" in note,
        "witt_reading_quoted":
            "the count is not a convention: fed the physical pairing, the slot "
            "structure is orbit = one cell = one complex slot -> r = 1/2 -> "
            "q = 2/3." in note,
        "eighth_correction": "the arc's eighth supervisor correction" in note,
        "unit_not_count":
            "the witt result governs the unit, not the count" in note,
        "readout_cannot_delete":
            "readout structure cannot delete integration content" in note,
        "det_blind_windows": "det-blind" in note,
        "window_invisible": "invisible to all landed observables" in note,
        # --- N4 -------------------------------------------------------------
        "one_named_input": "the one named input" in note,
        "sigma_definition": "sigma := -theta o x_0" in note,
        "antilinear_involution": "antilinear involution" in note,
        "sigma_square": "sigma^2 = +1" in note,
        "fix_form": "fix(sigma) = {z g_+ + zbar h_+}" in note,
        "majorana_type": "majorana-type reality condition" in note,
        "not_a_counting_convention": "not a counting convention" in note,
        "physical_in_kind": "physical in kind" in note,
        "unregistrable_in_class": "unregistrable in-class" in note,
        "adoption_or_future_physics":
            "decidable only by adoption or by future physics" in note,
        "sigma_reality_proposal":
            "the record-slice generation carrier is the sigma-real form" in note,
        "adopt_branch":
            "with every other link committed and computed" in note,
        "decline_branch":
            "stands as the committed measure's own value" in note,
        "replaces_prior_forms":
            "replaces every prior form of the counting proposal" in note,
        "phenomenological_note": "the observed koide value is" in note,
        "owner_weighing_not_derivation":
            "that is a weighing for the owner and is not a derivation" in note,
        # --- N5 -------------------------------------------------------------
        # Raw substring membership makes the printed fence byte-identical to its
        # note occurrence.
        "n5_verbatim": N5_FENCE in note_text,
        # --- N6 -------------------------------------------------------------
        "stop_reopen": "stop and reopen" in note,
        "routes_computed_closed": "computed closed" in note,
        "wigner_no_action": "no action" in note,
        "koide_stops": "the koide tail, per the owner's direction" in note,
        "reopen_writer_mechanism":
            "the flavor lane's writer mechanism lands" in note,
        "reopen_sector_reality":
            "any landed result fixes sector reality conditions" in note,
        "reopen_odd_extent":
            "an odd-extent-compatible grading variant is constructed" in note,
        "reopen_sister_lane": "#7334" in note,
        "review_not_prejudged":
            "that review is open and is not prejudged here" in note,
        # --- N7 -------------------------------------------------------------
        "arc_ledger": "the arc ledger" in note,
        "corrections_ledger": "the corrections ledger" in note,
        "eight_corrections": "eight supervisor corrections" in note,
        "correction_wrap": "the wrap hypothesis" in note,
        "correction_pin": "the pin hypothesis" in note,
        "correction_slogan": "the geometry-free slogan" in note,
        "correction_forced_fork":
            "the forced-fork and uniqueness claim" in note,
        "correction_multiplicity": "the multiplicity-dissolution claim" in note,
        "correction_theta_antiparticle": "the theta-antiparticle reading" in note,
        "correction_frame_quotient":
            "the frame-quotient counting reading" in note,
        "correction_witt_count": "the witt-decides-the-count reading" in note,
        "checker_overrides":
            "override the solve everywhere they collide" in note,
        "neutral_fanout": "the neutral four-exercise fan-out" in note,
        "fanout_decided_nothing":
            "the fan-out decided nothing and was not supposed to" in note,
        "no_rule_in_foundation":
            "no counting rule, no slot semantics, no quotient rule and no "
            "polarization selector" in note,
        "pre_declared_fork": "pre-declared three-outcome fork" in note,
        "verification_structure_working":
            "that is the verification structure working" in note,
        "cycle913_caution": "cycle913" in note,
        "non_supply_never_necessity":
            "non-supply within this formalism" in note
            and "never metaphysical necessity" in note,
        "candidacy_never_nature": "candidacy within this formalism" in note
        and "never a claim about nature" in note,
        "worker_profile": "worker profile" in note,
        "supervisor_inline_science":
            "all solve-side science and every synthesis" in note,
        "four_neutral_workers": "four neutral fable exercise workers" in note,
        "det_probe_worker": "a separate fable det-probe worker" in note,
        "codex_checks": "codex 5.6-sol" in note,
        "opus_mechanical_only": "mechanical drafting only" in note,
        "common_mode": "common-mode" in note,
        # --- N8 -------------------------------------------------------------
        "verdict":
            "the orientation bit is terminated with computed legs" in note,
        "successor_question": "the successor question" in note,
        "two_fixtures": "two fixtures" in note,
        "measure_leg_scoped": "12x6 alone" in note,
        "wigner_silent_not_negative": "silent and not negative" in note,
        # NEGATIVE key, inherited from Blocks 164-179.
        "no_priority_claim": ("first positive" not in note
                              and "novel" not in note
                              and "unprecedented" not in note
                              and "for the first time" not in note),
        "n1_n8": all(__import__("re").search(rf"\bn{index}\b", note) is not None
                     for index in range(1, 9)),
        "not_re_verified": "not re-verified" in note,
        "not_continuum": "not a continuum statement" in note,
        "not_a_flavor_bridge": "not a flavor bridge" in note,
        "not_a_koide_derivation":
            "not a derivation of the koide relation" in note,
        "not_a_born_derivation": "not a derivation of the born rule" in note,
        "ast_surface_disclosed": "ast surface" in note,
        "no_float": "no float" in note,
        "scope_key_certificate": "scope-key certificate" in note,
        # NEGATIVE key, inherited from Blocks 164-179.
        "no_volume_average": "volume average" not in note,
        # The LaTeX rho guard: a line-wrapped \rho leaves a stray "ho_" at the
        # start of a line and silently mangles a modulus name.
        "rho_guard": "\nho_" not in note_text,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": ("no toe percentage moves" in note
                       or "no toe percentage movement" in note),
        "zero_e2e": "retained-positive end-to-end theory count remains zero"
        in note,
        "axiom": "no axiom amendment is justified" in note,
        "campaign_cited": "campaign_20260823_complex_structure" in note,
        "gravity_campaign_cited": "campaign_20260824_gravity_mainline" in note,
        "packet_cited": "koide-counting-rule-decision-20260824" in note,
        "frame_check_cited": "b182_frame_check_findings.md" in note,
    }


N5_FENCE = 'N5: per_element: THE TWO BANNERS, FIRST AND WITH TEETH. THE INERTIA CONVENTION: every triple in this note is labelled and read in the (n_+, n_-, n_0) order of the LANDED Block 165 helper real_symmetric_inertia, while the landed b163/b164 helper congruence_inertia returns (n_+, n_0, n_-), measured on identical matrices, so THE LITERAL STRING (4,4,0) MEANS PSD in Block 164\'s landed fence and FULLY HYPERBOLIC here; NEITHER HELPER IS WRONG and no landed verdict changes, and this block\'s own triples inertia(herm Q) = (36,0,0)(n+,n-,n0)[b165] at 12x6 and (16,0,0)(n+,n-,n0)[b165] at 8x4 are positive definite under either reading. AND THE IMPOSED-OBJECT BANNER: NOTHING HERE IS REGISTERED OR ADOPTED -- the committed 12x6 and 8x4 constant-carrier fixtures, the frame benchmark (s_x,s_t) = (3/5,1/4) and the measure fixture (3/5,0), the LANDED STAGGERED GRADING X_0 = (-1)^(t+x) and its diagonal relabeling group, the chart translation and chart-momentum characters over the disclosed field Q(sqrt(-3)), the four record-slice eigenlines with their Theta-orbits and the antilinear sigma = -Theta o X_0, the class-doubled carrier with its six antiunitary placements, the flavor lane\'s fork arbiter read from landed authority and never re-derived here, and the inherited reflection, region pin, slice index set, class map CM-SITE, slot order and record-slice scope are IMPOSED MEASURED OBJECTS OF THIS BLOCK; AND THE SIGMA-REALITY CONDITION REMAINS A PROPOSAL AT THE OWNER\'S BAR; NOTHING IS REGISTERED AND NOTHING IS ADOPTED.\nper_site: THE FRAME THEOREM. At the frame benchmark (s_x,s_t) = (3/5,1/4) with the constant carrier and mass 1, exact full-matrix subtraction gives X_0 Q(+s_x,+s_t) X_0 - Q(-s_x,-s_t) = 0 with ZERO nonzero entries AT BOTH EXTENTS, while either single flip leaves 84 nonzero entries at 12x6 and 32 at 8x4 -- THE JOINT FLIP IS THE ONLY FLIP THE GRADING PERFORMS -- and X_0 is unitary and involutive with X_0^2 = I exactly. BUT IT IS NOT A FIXED-POINT SYMMETRY: X_0 Q(+,+) X_0 - Q(+,+) has 144 nonzero entries at 12x6 and 56 at 8x4, so what X_0 supplies is HORIZONTAL EQUIVALENCE BETWEEN CLASS POINTS and not a vertical symmetry of the fixed (3/5,1/4) fiber. THIS IS THE CHECKER\'S CORRECTION OF THE SUPERVISOR\'S FRAME READING AND THIS NOTE CARRIES THE CORRECTION: the horizontal quotient still has two slot-orbits, (p,O_+) <-> (-p,O_-) and (p,O_-) <-> (-p,O_+), so it leaves TWO fiber slots and does not identify O_+ with O_- at p; and the landed sign-channel precedent entails INVARIANT REPORTING AND NOT ORBIT SLOT-WEIGHTING. THE DESCENT SCOPE: (-1)^(t+x) descends through the antiperiodic quotient iff both PHYSICAL extents are even, which 6x6 and 4x4 satisfy, and EXISTENCE IN-CLASS IS NOT A LICENCE TO QUOTIENT.\nper_mode: THE NO-REGISTRATION THEOREM AND THE COUNT-NEUTRAL INVARIANT. NO COMMITTED-CLASS CHANNEL DETECTS THE OVERALL ORIENTATION: X_0 commutes with the committed reflection r, so Q, herm(Q^-1), the reflected form, the determinant, the spectrum and the zero-set data are all conjugate across (+,+) <-> (-,-), and every landed readout in this lane is built from those objects. AND THE REGISTERING GEOMETRIES ARE EXACTLY THE ONES WHERE THE GRADING FAILS TO DESCEND -- registration would require an odd physical extent, at which (-1)^(t+x) is not a map of the quotient at all -- so the bit is unregistrable precisely where it is defined. THE INVARIANT THAT IS REGISTERED IS THE TRIPLE SIGN sigma s_x s_t and NOT s_x s_t: s_x s_t is invariant only under the fixed-carrier stabilizer {1, X_0}, while X_t and X_x flip it while also flipping the supplied carrier shear orientation, and X_0 = X_t X_x. That class IS spectrally registered -- tr(Q^2) separates it at 47794293/896000 against 82268811/1792000 at 12x6 and 378637341/17920000 against 335627241/17920000 at 8x4 -- BUT IT CHANGES NO VECTOR-SPACE MULTIPLICITY AND IS COUNT-NEUTRAL. This is a NON-SUPPLY result at committed-class scope and not a claim that no wider formalism registers the bit.\nper_block: THE THREE COMPUTED LEGS OF THE DECISION EXERCISE, whose SYNTHESIS_FINAL.md is the GOVERNING STATEMENT. THE WITT UNIT THEOREM: at 12x6, s_t = 0, on the four eigenlines the PLAIN W9 GRAM is the scalar (875/1462) I_4 -- anisotropic, the additive reading\'s home -- while THE REFLECTED (OS) GRAM <Theta u, v> IS EXACTLY ANTI-DIAGONAL with (g_+,h_-) = (g_-,h_+) = 875/1462 and every diagonal entry exactly zero, so EVERY EIGENLINE IS ISOTROPIC and EACH THETA-ORBIT IS EXACTLY ONE HYPERBOLIC CELL; a lone eigenline is UNREADABLE, the minimal readable unit is the ORBIT-CELL whose det content a^2 + d^2 = 62866/30625 is one complex slot\'s, and LINE-COUNTING AT n = 4 IS DEAD BY COMPUTATION. THE WIGNER SILENCE: the magnetic Klein group M = {1, X_0, Theta, Theta X_0} can act honestly only on the class-doubled carrier Q(+3/5) (+) Q(-3/5); the unitary X_0-swap control PASSES exactly, and SIX PLACEMENTS of the antiunitary -- r, r X_0 and X_0 r in diagonal and swap form -- give SIX EXACT FAILURES of A^T Q_D conj(A) = Q_D^T with residual counts 360, 336, 336, 336, 360, 360, so THE HERRING TEST IS UNEVALUABLE and the leg is reported SILENT AND NOT FORCED, with no +1 and no -1 claimed.\nlattice_wide: THE DET-EXPONENT FACT, THE ARBITER-NATIVE LEG. The measure is the landed Z of H1-170b, exp(-phi^dag Q phi) with G = Q^-1 full -- the same declaration the ACCEPTED Block 179 cell consumed. THE LANDED DISCONNECTION MAKES IT A TRUE Z-FACTOR: the full record slice at t = 1 decouples in Q both ways exactly, so det Q = det(slice) x det(rest) exactly. On the four eigenlines the sector block is exactly diag(lam_+, lam_-, lam_+, lam_-) and the c-sector\'s factor is EXACTLY (62866/30625)^2 = 3952133956/937890625 -- EXPONENT 2, NOT 1 -- verified TWO WAYS, by the flavor arbiter\'s OWN det_cpair and by the basis-free site extraction det(slice)/det(k=0 fiber), which agree exactly. CALIBRATED AGAINST ACCEPTED PRECEDENT: the Block 179 accepted cell reproduces at beta = 3193/2240 with det_C[[beta]] = beta and realified det beta^2, ONE complex slot to ONE det factor at the FIRST power; and the level-4 singleton fiber gives D4 = (1817/1120)(I + (3/5)J), THE b = a s_x LAW AGAIN, with det D4 = a4^2 + d4^2 at power 1 and never squared, chain-coupled so a restriction cell and NOT a Z-factor. The committed covariance confirms it: B_k^dag G B_k = (aI - dJ)/(a^2+d^2) on BOTH charts, invertible, no anomalous channel, EIGHT real integration dimensions on the sector and NEVER the two-real-dimensional Fix(sigma) carrier.\nper_scope: THE RESOLUTION, THE EIGHTH CORRECTION, AND THE ONE NAMED INPUT. WHAT THE COMMITTED STRUCTURE SAYS PREMISE-FREE IS n = 2 CELLS, r = 1, Q = 1, composed through the flavor lane\'s own arbiter. THE ADDITIVE BRANCH IS TRUE OF THE LANDED MEASURE AND QUOTIENT COUNTING IS FALSE OF COMMITTED STRUCTURE: the factor is pinned, present and unique in the landed Z, and the pre-declared cancellation outcome does not fire. THE SUPERVISOR\'S WITT-DECIDES-THE-COUNT READING IS QUOTED AND CORRECTED as the arc\'s EIGHTH SUPERVISOR CORRECTION -- the Witt result governs THE UNIT AND NOT THE COUNT, the landed measure contains TWO such cells, the step to r = 1/2 silently selects ONE cell, and READOUT STRUCTURE CANNOT DELETE INTEGRATION CONTENT. AND Q = 2/3 REQUIRES EXACTLY ONE NEW PHYSICAL INPUT, NAMED TO THE BONE: THE SIGMA-REALITY CONDITION -- restrict the record-slice generation carrier to Fix(-Theta o X_0), where sigma = -Theta o X_0 is verified in-runner to be an antilinear involution with sigma^2 = +1, sigma(g_+) = h_+ and Fix(sigma) = {z g_+ + zbar h_+} real-2-dimensional. IT IS A MAJORANA-TYPE REALITY CONDITION ON THE SECTOR\'S FIELD CONTENT: not a counting convention, not frame data, not a gauge choice, PHYSICAL IN KIND, UNREGISTRABLE IN-CLASS by the no-registration theorem, and DECIDABLE ONLY BY ADOPTION OR BY FUTURE PHYSICS. THE PROPOSAL AT THE OWNER\'S BAR, IN ONE LINE: "the record-slice generation carrier is the sigma-real form Fix(-Theta o X_0)." ADOPT gives Q = 2/3 with every other link committed and computed; DECLINE leaves Q = 1 as the committed measure\'s own value. THE PHENOMENOLOGICAL NOTE, FOR THE OWNER\'S WEIGHING AND NEVER A DERIVATION: the observed Koide value is 2/3, and if the observed value is taken as input it SELECTS the reality condition, after which the framework predicts nothing new here but acquires a Majorana-type structural fact about the record slice.\nRESULT: THE ORIENTATION BIT IS TERMINATED WITH COMPUTED LEGS. THE FRAME ROUTE IS CLOSED by the exact joint flip, the horizontal-not-vertical correction and the no-registration theorem, with the surviving triple-sign invariant COUNT-NEUTRAL. THE READOUT ROUTE FIXES THE UNIT: the reflected Gram is anti-diagonal, every eigenline isotropic, each orbit one hyperbolic cell, and line-counting at n = 4 DEAD. THE SYMMETRY ROUTE IS SILENT: no honest corepresentation, six exact placement failures against a passing unitary control, the Herring test unevaluable. THE MEASURE ROUTE DECIDES: the c-sector factor is exactly (62866/30625)^2, two cells, so n = 2, r = 1, Q = 1 PREMISE-FREE. Q = 2/3 IS ONE NAMED MAJORANA-TYPE REALITY CONDITION AWAY, AT THE OWNER\'S BAR. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\nDECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is edited; no earlier block is corrected; the bar items stay PROPOSALS, and PROPOSALS STAY PROPOSALS. THE ARC\'S CORRECTIONS LEDGER IS EIGHT SUPERVISOR CORRECTIONS, ALL SHIPPED, AS THE VERIFICATION STRUCTURE\'S PRODUCT: the wrap hypothesis; the pin hypothesis; the geometry-free slogan; the forced-fork/uniqueness claim; the multiplicity-dissolution claim; the theta-antiparticle reading, refuted when theta was measured to CLOSE WITHIN each orbit so the second orbit is a genuine second doublet candidate; the frame-quotient counting reading, corrected by the b182 check to horizontal equivalence with invariant reporting and not slot-weighting; and THE WITT-DECIDES-THE-COUNT READING, corrected by the det-exponent probe. THE CHECKERS ARE CREDITED AND THEIR FINDINGS OVERRIDE THE SOLVE EVERYWHERE THEY COLLIDE. THIS BLOCK\'S OWN DEFECTS ARE DISCLOSED: it is TWO FIXTURES with no wider ladder and the measure leg runs at 12x6 alone; the no-registration theorem is a NON-SUPPLY result at committed-class scope; the Wigner leg is SILENT AND NOT NEGATIVE; Q = (1+2r)/3 and r_from_slot_count remain IMPORTED AUTHORITY; the measure leg is scoped to the landed H1-170b declaration at constant carrier and s_x != 0 and its exponent is invisible to every landed normalized window; and the AST surface is this runner plus the imported runner chain and NOT every landed module the chain reaches, with residual sites counted rather than claimed repaired. PROVENANCE: CAMPAIGN_20260823_COMPLEX_STRUCTURE.md and CAMPAIGN_20260824_GRAVITY_MAINLINE.md, with b182_frame_check_findings.md preserved in generator-program-20260821/ and the decision packet koide-counting-rule-decision-20260824/ preserved entire. HANDOFF: the owner decides the sigma-reality condition; the lane repoints to the gravity mainline; review the sister lane\'s #7334 grading derivation against the measure calibration.\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero.'

def build_claims(mutation: str) -> dict:
    claims: dict = {
        "main_head": CURRENT_MAIN,
        "parent_pin": "resolved",
        "objects_registered": False,
        "joint_flip_residual": JOINT_FLIP_RESIDUAL,
        "bit_registrable": False,
        "witt_entry": W1_ENTRY,
        "line_counting_alive": False,
        "herring_evaluable": False,
        "det_exponent": DET_EXPONENT,
        "c_factor": C_FACTOR,
        "witt_decides_count": False,
        "premise_free_q": PREMISE_FREE_Q,
        "required_resolution_keys": RESOLUTION_KEYS,
        "required_scope_keys": SCOPE_KEYS,
    }
    if mutation == "stale_main_authority":
        claims["main_head"] = STALE_MAIN
    elif mutation == "stale_parent_authority":
        claims["parent_pin"] = "stale"
    elif mutation == "claim_objects_registered":
        # THE BANNER DENIED: the imposed objects asserted REGISTERED, which zero
        # registered and zero adopted objects forbid.
        claims["objects_registered"] = True
    elif mutation == "break_joint_flip_identity":
        # THE FRAME IDENTITY BROKEN: a nonzero joint-flip residual asserted,
        # which the exact zero at both extents forbids.
        claims["joint_flip_residual"] = 1
    elif mutation == "claim_bit_registrable":
        # THE NO-REGISTRATION THEOREM DENIED: the orientation asserted
        # detectable in-class, which the measured conjugacy of the determinant,
        # the spectrum, the covariance and tr(Q^2) forbids.
        claims["bit_registrable"] = True
    elif mutation == "break_witt_gram":
        # THE REFLECTED GRAM BROKEN: a wrong exact entry asserted, which the
        # rebuilt anti-diagonal 875/1462 pattern forbids.
        claims["witt_entry"] = sp.cancel(W1_ENTRY + R(1, 10 ** 6))
    elif mutation == "claim_line_counting_alive":
        # THE DEAD READING REASSERTED: line-counting at n = 4 asserted
        # available, which four exactly isotropic eigenlines forbid.
        claims["line_counting_alive"] = True
    elif mutation == "claim_wigner_plus_one":
        # THE SILENCE FORCED INTO A VERDICT: the Herring test asserted
        # evaluated, which six exact placement failures forbid.
        claims["herring_evaluable"] = True
    elif mutation == "claim_quotient_true_of_measure":
        # QUOTIENT COUNTING REASSERTED: det exponent 1 asserted, which the
        # measured (62866/30625)^2 forbids.
        claims["det_exponent"] = 1
    elif mutation == "break_det_exponent":
        # THE MEASURED FACTOR BROKEN: a wrong exact rational asserted, which
        # both independent routes forbid.
        claims["c_factor"] = sp.cancel(C_FACTOR + R(1, 10 ** 6))
    elif mutation == "claim_witt_decides_count":
        # THE CORRECTED READING REASSERTED: the Witt structure asserted to fix
        # the COUNT, which the two-cell measure content forbids.
        claims["witt_decides_count"] = True
    elif mutation == "claim_q_two_thirds_premise_free":
        # THE PREMISE DROPPED: Q = 2/3 asserted premise-free, which the
        # arbiter's own composition on the measured slot count forbids.
        claims["premise_free_q"] = SIGMA_REAL_Q
    elif mutation == "drop_sigma_reality_proposal":
        claims["required_resolution_keys"] = tuple(
            key for key in RESOLUTION_KEYS if key != "sigma_reality_proposal")
    elif mutation == "drop_corrections_ledger":
        claims["required_resolution_keys"] = tuple(
            key for key in RESOLUTION_KEYS if key != "corrections_ledger")
    elif mutation == "drop_n5_fence":
        claims["required_scope_keys"] = tuple(
            key for key in SCOPE_KEYS if key != "n5_verbatim")
    return claims


# ---------------------------------------------------------------------------
# gates: pure functions of the measured facts and the claims
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Facts:
    deep: bool
    main_head: str
    authority: AuthorityCertificate
    note_at_final_path: bool
    scope: dict
    banners: dict
    fixtures: dict
    frame: dict
    sector: dict
    witt: dict
    wigner: dict
    exponent: dict
    sigma: dict
    exact_no_float: bool
    source_files: int
    source_floats: int
    source_forbidden: int


EXPECTED_CONVENTION = (((4, 4, 0), (4, 0, 4)),
                       ((4, 0, 4), (4, 4, 0)),
                       ((0, 3, 0), (0, 0, 3)))


def evaluate_gates(facts: Facts, claims: dict, elapsed_ns: int) -> dict:
    authority = facts.authority
    parent_blobs_ok = (authority.parent_artifact_blobs
                       if claims["parent_pin"] == "resolved"
                       else authority.stale_parent_artifact_blobs)
    gate_a = bool(
        AUDIT_INPUT_PATHS[0] == SELF_NOTE_INPUT
        and len(AUDIT_INPUT_PATHS) == 19
        and len(set(AUDIT_INPUT_PATHS)) == 19
        # THE FLAVOR RUNNER IS DELIBERATELY ABSENT: it is read from origin/main
        # through the landed Block 176 loader and never from the worktree.
        and FLAVOR_RUNNER not in AUDIT_INPUT_PATHS
        and FLAVOR_FORK_NOTE in AUDIT_INPUT_PATHS
        and BLOCK179_NOTE in AUDIT_INPUT_PATHS
        and BLOCK179_RUNNER in AUDIT_INPUT_PATHS
        # THE EXERCISE PACKET, listed in full because its three computed legs
        # are load-bearing here.
        and sum(1 for path in AUDIT_INPUT_PATHS
                if "koide-counting-rule-decision-20260824" in path) == 8
        and ".claude/science/physics-loops/generator-program-20260821/"
            "b182_frame_check_findings.md" in AUDIT_INPUT_PATHS
        # EVERY AUDIT INPUT BUT THIS BLOCK'S OWN NOTE IS READABLE IN THE
        # WORKTREE; the note itself is gate H's, because it lands later.
        and authority.inputs_readable == len(AUDIT_INPUT_PATHS) - 1
        and authority.inputs_missing == ()
        and PARENT_ARTIFACTS == (BLOCK179_NOTE, BLOCK179_RUNNER)
        and len(PARENT_ARTIFACT_BLOBS) == len(PARENT_ARTIFACTS) == 2
        and facts.main_head == claims["main_head"]
        and authority.fixed_authority
        and authority.parent_import_landed
        and authority.parent_pin_is_commit
        and authority.parent_ref_and_ancestry
        and parent_blobs_ok
        # THE STALE PIN: a REAL ancestor of HEAD that carries NEITHER Block 179
        # artifact, which is exactly what makes the stale mutation bite.
        and authority.stale_is_real_ancestor
        and authority.stale_carries_neither_artifact)

    ban = facts.banners
    fixtures = facts.fixtures
    gate_b = bool(
        # THE CONVENTION COLLISION, MEASURED on identical matrices.
        ban["convention"]["pairs"] == EXPECTED_CONVENTION
        and ban["convention"]["landed_psd"] and ban["convention"]["here_psd"]
        and ban["convention"]["orders_differ"]
        # THE IMPOSED-OBJECT BANNER and THE PROPOSALS, as measured objects.
        and ban["imposed_objects"] == 8
        and ban["registered_objects"] == 0
        and ban["adopted_objects"] == 0
        and ban["owner_bar_items"] == 3
        and ban["owner_decisions"] == 1
        and ban["arc_corrections"] == 8
        and ban["exercise_workers"] == 4
        and ban["computed_legs"] == 3
        and ban["stop_items"] == 4
        and ban["reopen_items"] == 4
        and ban["draft_worker_catches"] == 1
        and (ban["registered_objects"] == 0 and ban["adopted_objects"] == 0)
        == (not claims["objects_registered"])
        # BOTH FIXTURES, rebuilt through the LANDED chain and never imported
        # from any scratchpad module.
        and fixtures[BIG_TAG]["N"] == BIG_N
        and fixtures[BIG_TAG]["T_phys"] == BIG_PHYS
        and fixtures[BIG_TAG]["lx"] == BIG_LX
        and fixtures[SMALL_TAG]["N"] == SMALL_N
        and fixtures[SMALL_TAG]["T_phys"] == SMALL_PHYS
        and fixtures[SMALL_TAG]["lx"] == SMALL_LX
        and all(fixtures[tag]["c"] == REGION_PIN
                and fixtures[tag]["pinned"] == PINNED_LEVELS
                and fixtures[tag]["symbol_free"]
                and fixtures[tag]["inertia"] == INERTIA[tag]
                for tag in (BIG_TAG, SMALL_TAG))
        and fixtures["measure"]["symbol_free"]
        and fixtures["measure"]["carrier_sigma"] == R(3, 5)
        and fixtures["measure"]["volume"] == CONST_VOLUME
        and facts.exact_no_float
        and facts.source_floats == 0 and facts.source_forbidden == 0
        and facts.source_files >= 2)

    frame = facts.frame
    gate_c = bool(
        # THE JOINT FLIP, EXACT AT BOTH EXTENTS, AND CLAIM-BOUND.
        all(frame[tag]["joint_residual"] == claims["joint_flip_residual"]
            for tag in (BIG_TAG, SMALL_TAG))
        and all(frame[tag]["joint_residual"] == JOINT_FLIP_RESIDUAL
                for tag in (BIG_TAG, SMALL_TAG))
        # EITHER SINGLE FLIP, AND NEITHER IS AVAILABLE.
        and all(frame[tag]["single_mp"] == SINGLE_FLIP_DEFECTS[tag]
                and frame[tag]["single_pm"] == SINGLE_FLIP_DEFECTS[tag]
                for tag in (BIG_TAG, SMALL_TAG))
        # NOT A FIXED-POINT SYMMETRY -- the check's correction, measured.
        and all(frame[tag]["self_defect"] == SELF_CONJUGATION_DEFECTS[tag]
                and not frame[tag]["is_fixed_point_symmetry"]
                for tag in (BIG_TAG, SMALL_TAG))
        # X_0 UNITARY, INVOLUTIVE, REAL, AND DESCENDING IN-CLASS.
        and all(frame[tag]["x0_involutive"] and frame[tag]["x0_unitary"]
                and frame[tag]["x0_real"] and frame[tag]["extents_even"]
                and frame[tag]["physical_extents"] == PHYSICAL_EXTENTS[tag]
                for tag in (BIG_TAG, SMALL_TAG))
        # THE NO-REGISTRATION CHANNELS, ALL CONJUGATE ACROSS (+,+) <-> (-,-).
        and all(frame[tag]["commutes_with_reflection"]
                and frame[tag]["det_conjugate"]
                and frame[tag]["spectrum_conjugate"]
                and frame[tag]["covariance_conjugate"]
                and frame[tag]["joint_class_agrees"]
                for tag in (BIG_TAG, SMALL_TAG))
        # THE INVARIANT THAT IS REGISTERED, AND IT CARRIES NO COUNT.
        and all(frame[tag]["trace_sq_pp"] == TRACE_SQ_JOINT[tag]
                and frame[tag]["trace_sq_pm"] == TRACE_SQ_SPLIT[tag]
                and frame[tag]["classes_separate"]
                and frame[tag]["det_separates_classes"]
                for tag in (BIG_TAG, SMALL_TAG))
        # THE SCOPED STATEMENTS, gated as note text.
        and facts.scope["frame_theorem"]
        and facts.scope["joint_flip_identity"]
        and facts.scope["single_flip_defects"]
        and facts.scope["self_conjugation_defects"]
        and facts.scope["not_fixed_point_symmetry"]
        and facts.scope["checker_correction_disclosed"]
        and facts.scope["horizontal_equivalence"]
        and facts.scope["two_fiber_slots"]
        and facts.scope["reporting_not_weighting"]
        and facts.scope["descent_evenness"]
        and facts.scope["existence_not_licence"]
        and facts.scope["no_registration_theorem"]
        and facts.scope["no_channel_detects"]
        and facts.scope["registering_geometries"]
        and facts.scope["triple_sign_invariant"]
        and facts.scope["count_neutral"]
        and facts.scope["trace_sq_literals"]
        and facts.scope["non_supply_scope"]
        # THE CLAIM-BOUND LEG: no committed-class channel registers the bit.
        and frame["bit_is_registrable"] == claims["bit_registrable"]
        and (frame["deep"]["agrees"] is True if facts.deep else True)
        and facts.exact_no_float)

    sector = facts.sector
    witt = facts.witt
    gate_d = bool(
        # THE SECTOR ITSELF, rebuilt exactly before any Gram is taken.
        sector["charts_orthonormal"] and sector["chart_blocks"]
        and sector["eigenlines_exact"] and sector["orbits_exact"]
        and sector["reflection_acts_as_identity"]
        and sector["covariance_exact"]
        # THE PLAIN GRAM: the anisotropic scalar, the additive reading's home.
        and witt["plain_is_scalar"]
        and all(value == W1_ENTRY for value in witt["plain_self_pairings"])
        # THE REFLECTED GRAM: EXACTLY ANTI-DIAGONAL, and CLAIM-BOUND.
        and witt["diagonal_all_zero"]
        and witt["off_pattern_zero"]
        and witt["antidiagonal_uniform"]
        and all(value == claims["witt_entry"]
                for value in witt["antidiagonal_entries"])
        # EACH ORBIT ONE HYPERBOLIC CELL, at the one-complex-slot det content.
        and witt["cells_hyperbolic"]
        and witt["cell_count"] == CELL_COUNT
        and witt["cell_det_content"] == CELL_UNIT
        and witt["every_line_isotropic"]
        # THE SCOPED STATEMENTS, gated as note text.
        and facts.scope["witt_unit_theorem"]
        and facts.scope["plain_gram_scalar"]
        and facts.scope["reflected_gram_antidiagonal"]
        and facts.scope["witt_entry_literal"]
        and facts.scope["every_line_isotropic"]
        and facts.scope["orbit_one_cell"]
        and facts.scope["lone_line_unreadable"]
        and facts.scope["minimal_readable_unit"]
        and facts.scope["line_counting_dead"]
        and facts.scope["three_computed_legs"]
        and facts.scope["synthesis_governing"]
        # THE CLAIM-BOUND LEG: line-counting at n = 4 is DEAD.
        and witt["line_counting_alive"] == claims["line_counting_alive"]
        and facts.exact_no_float)

    wigner = facts.wigner
    gate_e = bool(
        # THE DOUBLING IS REAL AND ITS UNITARY HALF ACTS.
        wigner["class_doubling_exact"]
        and wigner["doubled_dimension"] == 2 * BIG_N
        and wigner["control_passes"] and wigner["control_unitary"]
        # SIX PLACEMENTS, SIX EXACT FAILURES, AT THEIR MEASURED SIZES.
        and wigner["placements_tested"] == len(WIGNER_PLACEMENTS) == 6
        and wigner["failures"] == WIGNER_FAILURES
        and wigner["defect_tuple"] == WIGNER_DEFECTS
        and all(value != 0 for value in wigner["defects"].values())
        # THE SCOPED STATEMENTS, gated as note text.
        and facts.scope["wigner_silence"]
        and facts.scope["magnetic_klein_group"]
        and facts.scope["six_placements"]
        and facts.scope["six_failures"]
        and facts.scope["wigner_defect_literals"]
        and facts.scope["control_passes"]
        and facts.scope["herring_unevaluable"]
        and facts.scope["silent_not_forced"]
        and facts.scope["wigner_silent_not_negative"]
        # THE CLAIM-BOUND LEG: the Herring test CANNOT be evaluated.
        and wigner["herring_evaluable"] == claims["herring_evaluable"]
        and facts.exact_no_float)

    exponent = facts.exponent
    gate_f = bool(
        exponent["arbiter_loaded"]
        # THE DISCONNECTION MAKES IT A TRUE Z-FACTOR.
        and exponent["disconnection"] and exponent["det_factorizes"]
        and exponent["sector_block_diagonal"]
        # BOTH ROUTES, AND THEY AGREE.
        and exponent["arbiter_factor_real"]
        and exponent["arbiter_factor_matches"]
        and exponent["routes_agree"]
        and exponent["basis_free_factor"] == claims["c_factor"]
        and exponent["unit"] == CELL_UNIT
        and exponent["exponent"] == claims["det_exponent"]
        # THE TWO CALIBRATORS, AT THEIR EXACT VALUES AND POWERS.
        and exponent["beta"] == BETA_CALIBRATOR
        and exponent["beta_first_power"] and exponent["beta_realified_square"]
        and exponent["d4_a"] == D4_CALIBRATOR
        and exponent["d4_law"] and exponent["d4_det_first_power"]
        and exponent["d4_chain_coupled"]
        # THE COVARIANCE PIN: the full unconstrained-Gaussian signature.
        and exponent["full_covariance"] and exponent["w1_cross_check"]
        and exponent["sector_real_dims"] == SECTOR_REAL_DIMS
        # THE ARBITER COMPOSITION, in the arbiter's own functions.
        and exponent["premise_free_r"] == PREMISE_FREE_R
        and exponent["premise_free_q"] == PREMISE_FREE_Q
        and exponent["halved_r"] == SIGMA_REAL_R
        and exponent["halved_q"] == SIGMA_REAL_Q
        # THE SCOPED STATEMENTS, gated as note text.
        and facts.scope["det_exponent_fact"]
        and facts.scope["arbiter_native"]
        and facts.scope["c_factor_literal"]
        and facts.scope["exponent_two"]
        and facts.scope["unit_literal"]
        and facts.scope["two_routes"]
        and facts.scope["basis_free_route"]
        and facts.scope["disconnection_z_factor"]
        and facts.scope["beta_calibrator"]
        and facts.scope["d4_calibrator"]
        and facts.scope["b_equals_a_sx"]
        and facts.scope["unconstrained_gaussian"]
        and facts.scope["additive_true_of_measure"]
        and facts.scope["quotient_false_of_structure"]
        # THE CLAIM-BOUND LEG: quotient counting is FALSE of the measure.
        and exponent["quotient_true_of_measure"] == (claims["det_exponent"] == 1)
        and facts.exact_no_float)

    sigma = facts.sigma
    resolution_keys = tuple(claims["required_resolution_keys"])
    gate_g = bool(
        # sigma VERIFIED IN-RUNNER: antilinear, involutive, and its Fix.
        sigma["grading_maps_lines"] and sigma["sigma_swaps"]
        and sigma["sigma_involutive"] and sigma["sigma_antilinear"]
        and sigma["fix_basis_fixed"] and sigma["fix_form_exact"]
        and sigma["fix_independent"] and sigma["non_member_moves"]
        and sigma["fix_real_dims"] == FIX_REAL_DIMS
        and sigma["sigma_uses_landed_objects_only"]
        and sigma["second_orbit_present"]
        # THE REQUIRED RESOLUTION KEYS ARE THE FULL SET, which is what gives
        # the two drop mutations their teeth.
        and resolution_keys == RESOLUTION_KEYS
        and all(facts.scope[key] for key in resolution_keys)
        and set(RESOLUTION_KEYS) <= set(SCOPE_KEYS)
        # THE STOP/REOPEN SECTION AND THE CORRECTIONS LEDGER, present.
        and facts.scope["koide_stops"]
        and facts.scope["review_not_prejudged"]
        and facts.scope["fanout_decided_nothing"]
        and facts.scope["no_rule_in_foundation"]
        and facts.scope["verification_structure_working"]
        and facts.scope["arc_ledger"]
        and ban["arc_corrections"] == 8
        and ban["stop_items"] == 4 and ban["reopen_items"] == 4
        # THE TWO CLAIM-BOUND LEGS.  The Witt result does NOT decide the count,
        # and the premise-free value is Q = 1.
        and ban["witt_decides_count"] == claims["witt_decides_count"]
        and exponent["premise_free_q"] == claims["premise_free_q"]
        and facts.exact_no_float)

    required = tuple(claims["required_scope_keys"])
    budget = DEEP_RUNTIME_BUDGET_SEC if facts.deep else RUNTIME_BUDGET_SEC
    gate_h = bool(
        # THE NOTE AT ITS FINAL PATH.  An unlanded draft fails HERE and only
        # here; the scope certificate is still computed from the declared draft
        # fallback so the supervisor can see every key before landing.
        facts.note_at_final_path
        and NOTE_PATH.name == FINAL_NOTE_NAME
        and set(facts.scope) == set(SCOPE_KEYS)
        # THE FULL KEY SET IS REQUIRED, not a subset.
        and required == SCOPE_KEYS
        and all(facts.scope[key] for key in required)
        and facts.scope["n5_verbatim"]
        and facts.scope["scope_key_certificate"]
        and facts.scope["no_priority_claim"]
        and len(MUTATIONS) == 15
        and len(set(MUTATIONS)) == 15
        and set(MUTATION_GATE) == set(MUTATIONS)
        and set(MUTATION_GATE.values()) == set("ABCDEFGH")
        # THE N5 FENCE: N5-prefixed, 9 to 12 lines, the standard sections.
        and N5_FENCE.startswith("N5: ")
        and 9 <= N5_FENCE.count("\n") + 1 <= 12
        and all(N5_FENCE.count(f"\n{name}:") == 1
                for name in ("per_site", "per_mode", "per_block",
                             "lattice_wide", "per_scope", "RESULT",
                             "DECISION_CUT", "TOE"))
        and POOL_TWO_LEADS == 3
        and HANDOFF_ITEMS == 3
        and elapsed_ns <= budget * 1_000_000_000)

    return {"A": gate_a, "B": gate_b, "C": gate_c, "D": gate_d,
            "E": gate_e, "F": gate_f, "G": gate_g, "H": gate_h}


# ---------------------------------------------------------------------------
# the measurement pass: every gate reads it, no gate feeds it
# ---------------------------------------------------------------------------
DEEP_SX = R(1, 7)
DEEP_ST = R(1, 2)


def measure_deep(deep: bool) -> dict:
    """THE DEEP LEG, DECLARED: re-derive the joint-flip identity at a SECOND
    dial pair at both extents, so the frame theorem is not read off one
    benchmark.  It is NOT RUN at baseline, and None means NOT RUN rather than
    agreement."""
    if not deep:
        return {"ran": False, "joint_residuals": {}, "single_defects": {},
                "agrees": None}
    joint = {}
    single = {}
    for tag, cover_t, lx, phys in ((BIG_TAG, BIG_COVER, BIG_LX, BIG_PHYS),
                                   (SMALL_TAG, SMALL_COVER, SMALL_LX, SMALL_PHYS)):
        _, _, q_pp = build_fixture(tag, cover_t, lx, DEEP_SX, DEEP_ST)
        _, _, q_mm = build_fixture(tag, cover_t, lx, -DEEP_SX, -DEEP_ST)
        _, _, q_mp = build_fixture(tag, cover_t, lx, -DEEP_SX, DEEP_ST)
        grading = staggered_grading(phys, lx)
        conjugated = sp.expand(grading * q_pp * grading)
        joint[tag] = nonzero_entries(conjugated - q_mm)
        single[tag] = nonzero_entries(conjugated - q_mp)
    return {"ran": True, "joint_residuals": joint, "single_defects": single,
            "agrees": all(value == JOINT_FLIP_RESIDUAL for value in joint.values())
            and all(value != 0 for value in single.values())}


def measure(deep: bool) -> Facts:
    note_text, at_final_path = raw_note()
    main_head = resolve_ref("origin/main")
    scope = scope_certificate(note_text)
    fixtures = measure_fixtures()
    frame = measure_frame(fixtures)
    sector = sector_objects(fixtures)
    witt = measure_witt(sector)
    wigner = measure_wigner(fixtures, sector)
    exponent = measure_exponent(fixtures, sector)
    sigma = measure_sigma(fixtures, sector)
    frame["deep"] = measure_deep(deep)
    banners = {
        "convention": b176.measure_convention() if b176 is not None else {},
        "imposed_objects": len(IMPOSED_OBJECTS),
        "registered_objects": len(REGISTERED_OBJECTS),
        "adopted_objects": len(ADOPTED_OBJECTS),
        "owner_bar_items": len(OWNER_BAR_ITEMS),
        "owner_decisions": len(OWNER_DECISIONS),
        "arc_corrections": len(ARC_CORRECTIONS),
        "exercise_workers": len(EXERCISE_WORKERS),
        "computed_legs": len(COMPUTED_LEGS),
        "stop_items": len(STOP_ITEMS),
        "reopen_items": len(REOPEN_ITEMS),
        "draft_worker_catches": len(DRAFT_WORKER_CATCHES),
        # THE DECLARED STATUS FLAGS, so the mutations bite on a declared object
        # and not on prose.  BOTH ARE MEASURED and BOTH ARE FALSE.
        "witt_decides_count": exponent.get("exponent") == 1,
        "readout_is_derived": False,
    }
    for tag in (BIG_TAG, SMALL_TAG):
        record(fixtures[tag]["N"])
        for value in fixtures[tag]["inertia"]:
            record(value)
        record(frame[tag]["joint_residual"])
        record(frame[tag]["single_mp"])
        record(frame[tag]["single_pm"])
        record(frame[tag]["self_defect"])
        record(frame[tag]["trace_sq_pp"])
        record(frame[tag]["trace_sq_pm"])
    for value in witt["plain_self_pairings"]:
        record(value)
    for value in witt["antidiagonal_entries"]:
        record(value)
    record(witt["cell_det_content"])
    record(witt["cell_count"])
    for value in wigner["defect_tuple"]:
        record(value)
    for key in ("basis_free_factor", "unit", "exponent", "beta", "d4_a", "d4_b",
                "premise_free_r", "premise_free_q", "halved_r", "halved_q"):
        if exponent.get(key) is not None:
            record(exponent[key])
    record(sigma["fix_real_dims"])
    return Facts(
        deep=deep,
        main_head=main_head,
        authority=authority_certificate(main_head),
        note_at_final_path=at_final_path,
        scope=scope,
        banners=banners,
        fixtures=fixtures,
        frame=frame,
        sector=sector,
        witt=witt,
        wigner=wigner,
        exponent=exponent,
        sigma=sigma,
        exact_no_float=all(no_float(v) for v in NUMERALS),
        source_files=len(audit_source_paths()),
        source_floats=source_float_literals(),
        source_forbidden=source_forbidden_calls(),
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument(
        "--list-mutations", action="store_true",
        help="print the declared mutation names, one per line, and exit")
    parser.add_argument(
        "--deep", action="store_true",
        help="also re-derive the joint-flip identity at a SECOND dial pair "
             "(s_x, s_t) = (1/7, 1/2) at both extents, so the frame theorem is "
             "not read off one benchmark; the runtime budget is lengthened")
    arguments = parser.parse_args()
    if arguments.list_mutations:
        for name in MUTATIONS:
            print(name)
        return 0
    mutation = arguments.mutation
    started_ns = time.monotonic_ns()

    # Every measurement happens once, before any mutation flag is consulted, so
    # a mutation can only rewrite a CLAIM.  No gate can cascade into another
    # because no gate feeds a measurement.
    facts = measure(arguments.deep)
    elapsed_ns = time.monotonic_ns() - started_ns

    raw_gates = evaluate_gates(facts, build_claims(""), elapsed_ns)
    gate_values = dict(raw_gates)
    if mutation:
        target = MUTATION_GATE[mutation]
        gate_values = evaluate_gates(facts, build_claims(mutation), elapsed_ns)
        changed = {k for k in raw_gates if raw_gates[k] != gate_values[k]}
        if changed - {target} or gate_values[target]:
            raise AssertionError("mutation did not fail exactly its own gate")

    ban = facts.banners
    frame, witt = facts.frame, facts.witt
    wigner, exponent, sigma = facts.wigner, facts.exponent, facts.sigma
    res = facts.authority.residue

    print("MEASURED, before any gate is read:")
    print(f"  PARENT IMPORT: the Block 179 runner imported "
          f"{facts.authority.parent_import_landed}; PARENT_COMMIT "
          f"{PARENT_COMMIT} is REAL and PARENT_REF resolves to it. "
          f"CURRENT_MAIN was RE-RESOLVED at draft time to {CURRENT_MAIN}. "
          f"NOTHING from the scratchpad is imported: both fixtures below are "
          f"the Block 174 Width(.,'const') construction REBUILT from its LANDED "
          f"ingredients. THE AUDIT INPUTS: "
          f"{record(facts.authority.inputs_readable)} of "
          f"{len(AUDIT_INPUT_PATHS) - 1} readable in the worktree (this block's "
          f"own note excluded, since it lands later and is gate H's), missing "
          f"{facts.authority.inputs_missing}")
    print(f"  THE STALE PIN: {STALE_PARENT_COMMIT[:12]} is a REAL ancestor of "
          f"HEAD {facts.authority.stale_is_real_ancestor} and carries NEITHER "
          f"Block 179 artifact {facts.authority.stale_carries_neither_artifact}"
          f" -- it is the Block 178 tip, which PREDATES both artifacts, and "
          f"that absence is exactly what makes the stale_parent_authority "
          f"mutation bite. AND THE HYGIENE RESIDUE IS COUNTED, NOT HIDDEN, as "
          f"(text mentions, LIVE CALL SITES): {res['per_module']}, which is "
          f"{record(res['call_sites_in_audit_surface'])} live call sites inside "
          f"this runner's AST audit surface and "
          f"{record(res['call_sites_below_audit_surface'])} BELOW it, in landed "
          f"modules the chain reaches transitively. REPORTED, and NEVER claimed "
          f"repaired")
    print(f"  THE NOTE: read at its FINAL PATH {facts.note_at_final_path} -- "
          f"when False this is an UNLANDED DRAFT reading the DECLARED FALLBACK "
          f"{DRAFT_NOTE_PATH.name}, gate H is EXPECTED to fail, and the gate-H "
          f"mutation is UNTESTABLE until the note lands; gates A-G are "
          f"unaffected.  Scope keys satisfied: "
          f"{sum(1 for v in facts.scope.values() if v)} of "
          f"{len(facts.scope)}; unsatisfied "
          f"{tuple(key for key, value in facts.scope.items() if not value)}")
    print(f"  THE INERTIA CONVENTION, FIRST: the landed b163/b164 helper and "
          f"the landed Block 165 helper on IDENTICAL matrices "
          f"{ban['convention'].get('pairs')} -- each pair (b163/b164, this "
          f"note); the region normal form is PSD under both readings and the "
          f"tuple ORDERS DIFFER {ban['convention'].get('orders_differ')}, so "
          f"the literal string (4,4,0) means PSD in Block 164's landed fence "
          f"and FULLY HYPERBOLIC here. THIS BLOCK'S OWN TRIPLES: "
          f"{facts.fixtures[BIG_TAG]['inertia']} at 12x6 and "
          f"{facts.fixtures[SMALL_TAG]['inertia']} at 8x4, both "
          f"(n+,n-,n0)[b165] and both positive definite under either reading")
    print(f"  THE IMPOSED-OBJECT BANNER AND THE PROPOSALS: "
          f"{record(ban['imposed_objects'])} objects built by this block or its "
          f"parents, {record(ban['registered_objects'])} registered and "
          f"{record(ban['adopted_objects'])} adopted; "
          f"{record(ban['owner_bar_items'])} items sit at THE OWNER'S BAR AS "
          f"PROPOSALS -- {OWNER_BAR_ITEMS} -- and "
          f"{record(ban['owner_decisions'])} decision belongs to the OWNER: "
          f"{OWNER_DECISIONS}. The imposed objects are {IMPOSED_OBJECTS}")
    print(f"  THE FIXTURES, rebuilt from LANDED modules: 12x6 at N = "
          f"{record(facts.fixtures[BIG_TAG]['N'])} and 8x4 at N = "
          f"{record(facts.fixtures[SMALL_TAG]['N'])}, region pin "
          f"{facts.fixtures[BIG_TAG]['c']}, pinned levels "
          f"{facts.fixtures[BIG_TAG]['pinned']} at zero shear and "
          f"CARRIER_SIGMA = {facts.fixtures['measure']['carrier_sigma']} "
          f"elsewhere, constant volume "
          f"{facts.fixtures['measure']['volume']}; the FRAME BENCHMARK is "
          f"(s_x,s_t) = ({FRAME_SX}, {FRAME_ST}) and the MEASURE FIXTURE is "
          f"({MEASURE_SX}, {MEASURE_ST}); Q is SYMBOL-FREE at both "
          f"{(facts.fixtures[BIG_TAG]['symbol_free'], facts.fixtures['measure']['symbol_free'])}")
    print(f"  THE FRAME THEOREM: the JOINT FLIP X_0 Q(+,+) X_0 - Q(-,-) has "
          f"{record(frame[BIG_TAG]['joint_residual'])} nonzero entries at 12x6 "
          f"and {record(frame[SMALL_TAG]['joint_residual'])} at 8x4 -- EXACT AT "
          f"BOTH EXTENTS -- while EITHER SINGLE FLIP leaves "
          f"{(frame[BIG_TAG]['single_mp'], frame[BIG_TAG]['single_pm'])} at "
          f"12x6 and {(frame[SMALL_TAG]['single_mp'], frame[SMALL_TAG]['single_pm'])}"
          f" at 8x4. X_0 is involutive {frame[BIG_TAG]['x0_involutive']}, "
          f"unitary {frame[BIG_TAG]['x0_unitary']} and real "
          f"{frame[BIG_TAG]['x0_real']}, and both PHYSICAL extents are even "
          f"{(frame[BIG_TAG]['physical_extents'], frame[SMALL_TAG]['physical_extents'])}"
          f" so the grading descends IN-CLASS")
    print(f"  AND IT IS NOT A FIXED-POINT SYMMETRY, WHICH IS THE CHECK'S "
          f"CORRECTION: X_0 Q(+,+) X_0 - Q(+,+) has "
          f"{record(frame[BIG_TAG]['self_defect'])} nonzero entries at 12x6 and "
          f"{record(frame[SMALL_TAG]['self_defect'])} at 8x4, so what X_0 "
          f"supplies is HORIZONTAL EQUIVALENCE BETWEEN CLASS POINTS and NOT a "
          f"vertical symmetry of the supplied-sign fiber. MEASURED fixed-point "
          f"symmetry = "
          f"{(frame[BIG_TAG]['is_fixed_point_symmetry'], frame[SMALL_TAG]['is_fixed_point_symmetry'])}")
    print(f"  THE NO-REGISTRATION THEOREM, ON MEASURED CHANNELS: X_0 commutes "
          f"with the committed reflection "
          f"{frame[BIG_TAG]['commutes_with_reflection']}, and across "
          f"(+,+) <-> (-,-) the DETERMINANT {frame[BIG_TAG]['det_conjugate']}, "
          f"the SPECTRUM {frame[BIG_TAG]['spectrum_conjugate']}, the COVARIANCE "
          f"herm(Q^-1) {frame[BIG_TAG]['covariance_conjugate']} and tr(Q^2) "
          f"{frame[BIG_TAG]['joint_class_agrees']} all agree -- so MEASURED "
          f"registrable = {frame['bit_is_registrable']}. THE INVARIANT THAT IS "
          f"REGISTERED is the TRIPLE SIGN sigma s_x s_t: tr(Q^2) = "
          f"{record(frame[BIG_TAG]['trace_sq_pp'])} against "
          f"{record(frame[BIG_TAG]['trace_sq_pm'])} at 12x6 and "
          f"{record(frame[SMALL_TAG]['trace_sq_pp'])} against "
          f"{record(frame[SMALL_TAG]['trace_sq_pm'])} at 8x4 -- REGISTERED AND "
          f"COUNT-NEUTRAL")
    print(f"  THE WITT LEG: the PLAIN W9 Gram is the scalar "
          f"{witt['plain_self_pairings'][0]} I_4 {witt['plain_is_scalar']} -- "
          f"anisotropic, the additive reading's home -- while the REFLECTED "
          f"(OS) Gram is {witt['reflected'].tolist()}: EXACTLY ANTI-DIAGONAL "
          f"with every diagonal entry zero {witt['diagonal_all_zero']}, every "
          f"off-pattern entry zero {witt['off_pattern_zero']} and the "
          f"anti-diagonal uniform at {witt['antidiagonal_entries']} "
          f"{witt['antidiagonal_uniform']}. EACH THETA-ORBIT IS ONE HYPERBOLIC "
          f"CELL {witt['cells_hyperbolic']} over {record(witt['cell_count'])} "
          f"cells at det content {record(witt['cell_det_content'])} -- so a "
          f"LONE EIGENLINE IS UNREADABLE and MEASURED line-counting alive = "
          f"{witt['line_counting_alive']}")
    print(f"  THE WIGNER LEG: the class doubling is exact "
          f"{wigner['class_doubling_exact']} at dimension "
          f"{wigner['doubled_dimension']}, and the UNITARY X_0-SWAP CONTROL "
          f"PASSES {wigner['control_passes']} -- so the halving subgroup DOES "
          f"act and the doubling is not vacuous. BUT ALL "
          f"{record(wigner['failures'])} OF THE "
          f"{wigner['placements_tested']} ANTIUNITARY PLACEMENTS FAIL "
          f"A^T Q_D conj(A) = Q_D^T, at exact residual counts "
          f"{wigner['defects']}. THE HERRING TEST IS THEREFORE UNEVALUABLE: "
          f"MEASURED evaluable = {wigner['herring_evaluable']}, and the leg is "
          f"reported SILENT AND NOT FORCED -- no +1 and no -1 is claimed")
    print(f"  THE DET-EXPONENT LEG: the record slice decouples "
          f"{exponent['disconnection']} and det Q = det(slice) det(rest) "
          f"{exponent['det_factorizes']}, so the restriction is a TRUE "
          f"Z-FACTOR. The sector block is exactly diag(lam+, lam-, lam+, lam-) "
          f"{exponent['sector_block_diagonal']} and the c-factor is "
          f"{record(exponent['basis_free_factor'])} = "
          f"({record(exponent['unit'])})^{record(exponent['exponent'])} -- BY "
          f"BOTH ROUTES: the arbiter's OWN det_cpair at its pinned blob "
          f"{exponent['arbiter_blob'][:12]} {exponent['arbiter_factor_matches']}"
          f" and the BASIS-FREE det(slice)/det(k=0 fiber) "
          f"{exponent['routes_agree']}")
    print(f"  AND IT IS CALIBRATED, NOT ASSERTED: the accepted one-slot "
          f"precedent reproduces at beta = {record(exponent['beta'])} with the "
          f"det factor at the FIRST power {exponent['beta_first_power']} and "
          f"the realified square {exponent['beta_realified_square']}; the "
          f"level-4 singleton gives D4 = {record(exponent['d4_a'])}(I + "
          f"{MEASURE_SX} J) with b = a s_x {exponent['d4_law']}, det at power 1 "
          f"{exponent['d4_det_first_power']}, chain-coupled "
          f"{exponent['d4_chain_coupled']} so a restriction cell and NOT a "
          f"Z-factor; and the committed covariance is the FULL "
          f"unconstrained-Gaussian one on ALL FOUR eigenlines "
          f"{exponent['full_covariance']} over "
          f"{exponent['sector_real_dims']} real dimensions. THE ARBITER "
          f"COMPOSITION, in THEIR functions: n = {exponent['exponent']} gives "
          f"r = {record(exponent['premise_free_r'])} and Q = "
          f"{record(exponent['premise_free_q'])}, while the sigma-real halved "
          f"carrier would give r = {record(exponent['halved_r'])} and Q = "
          f"{record(exponent['halved_q'])}. MEASURED quotient-true-of-measure = "
          f"{exponent['quotient_true_of_measure']} and MEASURED "
          f"witt-decides-count = {ban['witt_decides_count']}")
    print(f"  THE ONE NAMED INPUT, VERIFIED IN-RUNNER: sigma = -Theta o X_0 is "
          f"ANTILINEAR {sigma['sigma_antilinear']}, INVOLUTIVE "
          f"{sigma['sigma_involutive']}, swaps g+ and h+ {sigma['sigma_swaps']}"
          f", and its fixed set is EXACTLY {{z g+ + zbar h+}} "
          f"{sigma['fix_form_exact']} -- real-{record(sigma['fix_real_dims'])}"
          f"-dimensional {sigma['fix_independent']}, with a NON-member moved "
          f"{sigma['non_member_moves']} -- built from LANDED objects only "
          f"{sigma['sigma_uses_landed_objects_only']}, and the SECOND ORBIT IS "
          f"PRESENT {sigma['second_orbit_present']}. IMPOSING IT IS THE "
          f"(62866/30625)^1 MEASURE, WHICH THE LANDED Z EXACTLY IS NOT")
    print(f"  THE ARC LEDGER: {record(ban['arc_corrections'])} SUPERVISOR "
          f"CORRECTIONS -- {ARC_CORRECTIONS} -- "
          f"{record(ban['exercise_workers'])} NEUTRAL EXERCISE WORKERS, none of "
          f"which decided anything -- {EXERCISE_WORKERS} -- "
          f"{record(ban['computed_legs'])} COMPUTED LEGS -- {COMPUTED_LEGS} -- "
          f"and {record(ban['draft_worker_catches'])} DRAFT-WORKER CATCH -- "
          f"{DRAFT_WORKER_CATCHES}. STOP: {STOP_ITEMS}. REOPEN: {REOPEN_ITEMS}")
    print(f"  EXACTNESS: no float in any measured object "
          f"{facts.exact_no_float} over {record(len(NUMERALS))} numerals; the "
          f"AST scan covers {record(facts.source_files)} FILES -- this runner "
          f"AND the imported runner chain -- and finds "
          f"{record(facts.source_floats)} float literals and "
          f"{record(facts.source_forbidden)} forbidden references. THE AST "
          f"SURFACE IS DISCLOSED, IS NOT THE FULL TRANSITIVE CLOSURE, AND DOES "
          f"NOT COVER THE FLAVOR ARBITER, which is read from origin/main at "
          f"Block 176's pinned blob and whose own correctness is NOT checked "
          f"here")
    print(f"  SAMPLING: --deep {facts.deep}; at baseline BOTH extents are "
          f"measured in full at the frame benchmark and the whole 4x4 reflected "
          f"Gram, all six antiunitary placements and both det routes are built "
          f"exactly, so there is no sampling anywhere; --deep additionally "
          f"re-derives the joint-flip identity at the SECOND dial pair "
          f"(s_x, s_t) = ({DEEP_SX}, {DEEP_ST}). DEEP {frame['deep']} -- ran "
          f"False and agrees None mean the leg was NOT RUN at this invocation, "
          f"which is DISCLOSED rather than reported as agreement")
    print()
    checks = Checks()
    checks.check(
        "A-authority-and-THE-STALE-PIN-THAT-PREDATES-BOTH-ARTIFACTS",
        "main plus the TWO Block 179 artifacts content-bound -- its note and its runner, which are BOTH the stack parent this block's branch is cut from AND the content parent, since this runner IMPORTS the Block 179 runner and reaches the whole committed chain through Block 179's own import chain, which Block 179's gate A pins rather than this one duplicating it -- and the gate additionally requires that the Block 179 runner ACTUALLY IMPORTED, because both fixtures below are built by the LANDED Block 170 Bench and the LANDED Block 166 carrier substitution reached through it and by NOTHING from any scratchpad module. PARENT_COMMIT IS REAL AND SO ARE BOTH ARTIFACT BLOBS: Block 179 HAS landed, so nothing needs sed at landing, and CURRENT_MAIN was re-resolved at draft time. THE FIVE-PIN AUTHORITY BLOCK binds origin/main's head, the axioms blob and the registry blob at origin/main, and the axioms and registry blobs in the worktree. THE STALE PIN IS THE BLOCK 178 TIP, a REAL ancestor of HEAD that PREDATES Block 179 and therefore carries NEITHER Block 179 artifact, which is exactly what makes the stale_parent_authority mutation bite -- under it the gate looks for the artifact blobs at a commit where they do not exist. AUDIT_INPUT_PATHS IS LITERAL AND IT LISTS THE DECISION PACKET IN FULL -- all eight files of koide-counting-rule-decision-20260824 plus the preserved b182 frame-check findings -- because the three computed legs of this note are read from them, and EVERY ONE OF THEM IS REQUIRED READABLE IN THE WORKTREE except this block's own note, which lands later and belongs to gate H. THE FLAVOR RUNNER IS DELIBERATELY ABSENT FROM AUDIT_INPUT_PATHS, because it is read from origin/main through the landed Block 176 loader and never from the worktree, and THE HYGIENE RESIDUE BELOW THE AUDIT SURFACE IS COUNTED AND REPORTED AND NEVER CLAIMED REPAIRED, as (text mentions, LIVE CALL SITES) per module",
        gate_values["A"])
    checks.check(
        "B-the-two-banners-THE-SIGMA-REALITY-PROPOSAL-RESTATED-and-BOTH-fixtures-rebuilt-from-LANDED-modules",
        "THE TWO BANNERS COME BEFORE ANY NUMERAL AND BOTH ARE MEASURED RATHER THAN ASSERTED. THE INERTIA CONVENTION: called on IDENTICAL matrices, b163/b164's congruence_inertia returns (n_+, n_0, n_-) and Block 165's real_symmetric_inertia returns (n_+, n_-, n_0), so the region normal form reads (4,4,0) there and (4,0,4) here; NEITHER HELPER IS WRONG and no landed verdict changes, but THE LITERAL STRING (4,4,0) MEANS PSD IN BLOCK 164'S LANDED FENCE AND FULLY HYPERBOLIC IN THIS NOTE -- and this block's own triples, inertia(herm Q) = (36,0,0) at 12x6 and (16,0,0) at 8x4, are positive definite under either reading and are stated anyway. THE IMPOSED-OBJECT BANNER: eight objects are imposed by this block or its parents -- both constant-carrier fixtures, the two dial settings this block deliberately separates, the LANDED staggered grading and its diagonal relabeling group, the chart translation and characters over the disclosed field, the four record-slice eigenlines with their Theta-orbits and the antilinear sigma, the class-doubled carrier with its six antiunitary placements, the flavor lane's fork arbiter read from landed authority, and the inherited reflection, region pin, slice index set, class map, slot order and record-slice scope -- and ZERO of them are registered and ZERO adopted, while THREE ITEMS SIT AT THE OWNER'S BAR AS PROPOSALS, THE SIGMA-REALITY CONDITION FIRST AMONG THEM, and ONE DECISION belongs to the owner and is not taken here. AND BOTH FIXTURES ARE REBUILT FROM LANDED MODULES AND MEASURED: the 12x6 quotient action is 36x36 at T_phys = 6 and L_x = 6 and the 8x4 is 16x16 at T_phys = 4 and L_x = 4, both with region pin c = 1, pinned levels (0,1) at zero shear and CARRIER_SIGMA = 3/5 elsewhere, constant volume 7/5, both symbol-free, with the arc's declared counts -- eight corrections, four neutral exercise workers, three computed legs, four stop items and four reopeners -- gated as literals rather than prose. No float enters any measured object and the AST scan covers every file this runner reads code from in the runner chain",
        gate_values["B"])
    checks.check(
        "C-THE-FRAME-THEOREM-AT-BOTH-EXTENTS-and-THE-NO-REGISTRATION-THEOREM",
        "THE JOINT FLIP IS EXACT AND THE SINGLE FLIP IS UNAVAILABLE, AT BOTH EXTENTS. At the frame benchmark (s_x, s_t) = (3/5, 1/4) exact full-matrix subtraction gives X_0 Q(+s_x,+s_t) X_0 - Q(-s_x,-s_t) = 0 with ZERO nonzero entries at 12x6 and ZERO at 8x4, while against EITHER single flip the residual carries 84 nonzero entries at 12x6 and 32 at 8x4 -- not two numbers that agree to some precision, since no precision is involved anywhere. X_0 is involutive, unitary and real, and both PHYSICAL extents are even, 6x6 and 4x4, so the landed descent condition is met and the map exists IN-CLASS at both fixtures. AND THE GATE REQUIRES THE NOTE TO CARRY THE CHECK'S CORRECTION, because the supervisor's frame reading did not survive it: X_0 Q(+,+) X_0 - Q(+,+) has 144 nonzero entries at 12x6 and 56 at 8x4, so X_0 IS NOT A FIXED-POINT SYMMETRY of the supplied-sign benchmark, what it supplies is HORIZONTAL EQUIVALENCE BETWEEN CLASS POINTS, the horizontal quotient still has TWO slot-orbits, and the landed sign-channel precedent entails INVARIANT REPORTING AND NOT ORBIT SLOT-WEIGHTING. THE NO-REGISTRATION THEOREM IS THEN MEASURED ON ITS CHANNELS RATHER THAN ASSERTED: X_0 commutes with the committed reflection, and across (+,+) <-> (-,-) the determinant, the full characteristic polynomial, the committed covariance herm(Q^-1) and tr(Q^2) ALL AGREE at both extents, so no committed-class readout separates the two orientations and the geometries that would register the bit are exactly the odd-extent ones where the grading fails to descend. THE DATUM THAT IS REGISTERED IS THE TRIPLE SIGN: tr(Q^2) separates the classes exactly at 47794293/896000 against 82268811/1792000 at 12x6 and 378637341/17920000 against 335627241/17920000 at 8x4, with the determinants differing too -- REGISTERED AND COUNT-NEUTRAL. Asserting a nonzero joint-flip residual, or that the bit is registrable, fails this gate against exact measured zeros and exact measured agreements",
        gate_values["C"])
    checks.check(
        "D-THE-WITT-UNIT-THEOREM-cells-not-lines-with-THE-ANTI-DIAGONAL-PATTERN-REBUILT",
        "THE SECTOR IS REBUILT EXACTLY BEFORE ANY GRAM IS TAKEN: the two chart bases are orthonormal, each restricts to aI + dJ at a = 43/35 and d = 129/175, the four eigenlines are exact eigenvectors at lam_+- = a +- di, the committed reflection acts as the identity on the sector columns, the Theta-orbits are exactly O_+ = {g_+, h_-} and O_- = {g_-, h_+}, and the covariance is assembled over the landed disconnection with Q G = I exactly. THEN THE TWO GRAMS ARE PUT SIDE BY SIDE. THE PLAIN W9 GRAM IS THE SCALAR (875/1462) I_4 -- every line self-pairs, the form is anisotropic on each line, and that is the additive reading's home. THE REFLECTED (OS) GRAM <Theta u, v> IS EXACTLY ANTI-DIAGONAL: every diagonal entry is exactly zero, every off-pattern entry is exactly zero, and the four anti-diagonal entries are uniformly 875/1462 -- so EVERY EIGENLINE IS ISOTROPIC, pairing exclusively with its own Theta-orbit partner, and EACH ORBIT IS EXACTLY ONE HYPERBOLIC CELL, which the gate checks cell by cell rather than inferring from the pattern. THE ZERO PATTERN IS THE LOAD-BEARING FACT AND THE GATE TREATS IT THAT WAY. THE CONSEQUENCE THE THEOREM LICENSES AND NO MORE: an isotropic line cannot be normed alone, so A LONE EIGENLINE IS UNREADABLE, THE MINIMAL READABLE OBJECT IS THE ORBIT-CELL at det content a^2 + d^2 = 62866/30625 -- exactly one complex slot's -- and LINE-COUNTING AT n = 4 IS DEAD BY COMPUTATION. Asserting a wrong exact Gram entry, or that line-counting is still available, fails HERE and nowhere else",
        gate_values["D"])
    checks.check(
        "E-THE-WIGNER-SILENCE-six-exact-failures-against-a-PASSING-unitary-control",
        "THE DOUBLING IS NOT VACUOUS AND THE GATE PROVES THAT FIRST. The class doubling is exact -- X_0 Q(+3/5) X_0 = Q(-3/5) with a zero residual -- and the unitary X_0-swap on Q(+3/5) (+) Q(-3/5) is an EXACT symmetry of the doubled form, so the unitary halving subgroup H = {1, X_0} genuinely acts and the carrier is the right one to test on. AND THEN NO NATURAL PLACEMENT OF THE ANTIUNITARY ACTS. Six placements are built from the committed r, from r X_0 and from X_0 r, each in diagonal and in swap form, and each is tested against the antiunitary invariance condition exactly as the external template states it, A^T Q_D conj(A) = Q_D^T. ALL SIX FAIL, and the gate binds their exact residual entry counts one by one -- 360, 336, 336, 336, 360, 360 -- rather than a summary, so a future modified doubling cannot be scored against this leg by matching a headline. THE MAGNETIC KLEIN GROUP THEREFORE HAS NO HONEST COREPRESENTATION ON THIS DOUBLING, the Herring/Wigner character sum CANNOT BE EVALUATED, and per the exercise's own honesty discipline the leg is reported SILENT AND NOT FORCED: no +1 and no -1 is claimed, the absence of the action is the finding, and a modified doubling would be a NEW construction, flagged and not run. Asserting that the test was evaluated fails HERE and nowhere else",
        gate_values["E"])
    checks.check(
        "F-THE-DET-EXPONENT-FACT-both-routes-both-calibrators-and-THE-ARBITER-COMPOSITION",
        "THIS IS THE LEG THAT DECIDES, AND IT IS STATED IN THE FORK ARBITER'S OWN CURRENCY. First the gate establishes that the restriction is a TRUE Z-FACTOR rather than a conditional: the full record slice decouples in Q in BOTH directions exactly, so det Q = det(slice) x det(rest) exactly. Then the c-sector factor is measured BY TWO INDEPENDENT ROUTES that involve different machinery: the flavor arbiter's OWN det_cpair, called at Block 176's pinned blob on the sector block, which the gate first checks is exactly diag(lam_+, lam_-, lam_+, lam_-); and the BASIS-FREE site extraction det(slice)/det(k = 0 fiber), which makes no basis choice at all. THEY AGREE EXACTLY at (62866/30625)^2 = 3952133956/937890625 -- EXPONENT 2, NOT 1. AND IT IS CALIBRATED AGAINST ACCEPTED PRECEDENT RATHER THAN ASSERTED. The Block 179 ACCEPTED cell reproduces at beta = 3193/2240, with the arbiter's det_C[[beta]] = beta and the realified determinant beta^2 -- ONE complex slot to ONE det factor at the FIRST power -- which fixes the per-slot currency; and the level-4 singleton fiber gives D4 = (1817/1120)(I + (3/5)J), THE b = a s_x LAW AGAIN, with det D4 = a4^2 + d4^2 at power 1 and never squared, and the gate additionally measures that this fiber is CHAIN-COUPLED, so it is a restriction cell and NOT a Z-factor while the c-fiber alone is both. The committed covariance confirms it from the other side: B_k^dag G B_k = (aI - dJ)/(a^2+d^2) on BOTH charts, the unconstrained-Gaussian signature over eight real integration dimensions, NEVER the two-real-dimensional Fix(sigma) carrier. FINALLY THE COMPOSITION IS DONE IN THEIR FUNCTIONS AND NOT RE-IMPLEMENTED: n = 2 gives r = 1 and Q = 1, while the halved carrier would give r = 1/2 and Q = 2/3. THE ADDITIVE BRANCH IS TRUE OF THE LANDED MEASURE AND QUOTIENT COUNTING IS FALSE OF COMMITTED STRUCTURE. Asserting exponent 1, or a wrong exact factor, fails HERE and nowhere else",
        gate_values["F"])
    checks.check(
        "G-THE-RESOLUTION-THE-EIGHTH-CORRECTION-and-THE-SIGMA-REALITY-PROPOSAL",
        "THE ONE NAMED INPUT IS VERIFIED IN-RUNNER AND NOT ONLY DESCRIBED. sigma = -Theta o X_0 is measured to be ANTILINEAR -- sigma(i v) = -i sigma(v) and additive -- INVOLUTIVE with sigma^2 = +1, to swap g_+ and h_+, and to have fixed set EXACTLY {z g_+ + zbar h_+}, checked on a general symbolic z rather than on two sample vectors, real-2-dimensional and independent, with a NON-member exhibited as moved; and it is built from LANDED objects only, the grading's action on the lines and the Theta-orbits both being measured first. THE SECOND ORBIT IS MEASURED PRESENT, which is what makes the selection a selection. AND THE RESOLUTION IS GATED AS TEXT AT ITS EXACT STRENGTH. What the committed structure says PREMISE-FREE is n = 2, r = 1, Q = 1, and the gate binds the premise-free Q to the arbiter's own composition, so asserting Q = 2/3 premise-free fails here. THE SUPERVISOR'S WITT-DECIDES-THE-COUNT READING IS REQUIRED QUOTED AND THEN CORRECTED -- the note carries the quotation verbatim-keyed and the correction as THE ARC'S EIGHTH SUPERVISOR CORRECTION: the Witt result governs THE UNIT AND NOT THE COUNT, the landed measure contains TWO cells, the step to r = 1/2 silently selects ONE, and READOUT STRUCTURE CANNOT DELETE INTEGRATION CONTENT. THE PROPOSAL IS REQUIRED PRESENT IN ONE LINE -- 'the record-slice generation carrier is the sigma-real form Fix(-Theta o X_0)' -- with its ADOPT and DECLINE branches, its MAJORANA-TYPE characterisation, its not-a-counting-convention/physical-in-kind/unregistrable-in-class status, and the phenomenological note explicitly marked as the owner's weighing and NEVER a derivation. THE CORRECTIONS LEDGER IS EIGHT ITEMS AND THE STOP/REOPEN SECTION IS FOUR AND FOUR, all declared as counted literals. Removing the sigma-reality proposal or the corrections ledger, or asserting that the Witt result decides the count or that Q = 2/3 is premise-free, fails HERE and nowhere else",
        gate_values["G"])
    checks.check(
        "H-note-scope-the-caution-and-the-N5-fence",
        "THE NOTE SITS AT ITS FINAL PATH AND SATISFIES EVERY REQUIRED SCOPE KEY, the required set is THE FULL KEY SET and not a subset, the N5 fence is an N5-prefixed literal with nine labelled sections that appears BYTE-IDENTICALLY in the note, and the mutation battery is fifteen members mapped one-per-gate across A through H. THE VERDICT THIS GATE CERTIFIES IS FIVE SCOPED STATEMENTS AND NOTHING WIDER: THE FRAME ROUTE IS CLOSED, with the joint flip exact at both extents, the equivalence HORIZONTAL, no committed-class registration channel, and the surviving triple-sign invariant COUNT-NEUTRAL; THE READOUT ROUTE FIXES THE UNIT, every eigenline isotropic, each orbit one hyperbolic cell, line-counting at n = 4 DEAD BY COMPUTATION; THE SYMMETRY ROUTE IS SILENT, the Herring test unevaluable and reported SILENT AND NOT FORCED rather than negative; THE MEASURE ROUTE DECIDES, at exponent 2, so n = 2, r = 1, Q = 1 PREMISE-FREE; and Q = 2/3 IS ONE NAMED MAJORANA-TYPE REALITY CONDITION AWAY, AT THE OWNER'S BAR AND ADOPTED NOWHERE. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 caution, carried verbatim -- and every positive here is CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE. The worker profile is disclosed in full: ALL SOLVE-SIDE SCIENCE AND EVERY SYNTHESIS by the supervising frontier model INLINE, per the owner's standing directive; FOUR NEUTRAL Fable EXERCISE WORKERS on the fan-out, none of which decided anything; a SEPARATE Fable DET-PROBE WORKER on the deciding computation, against a PRE-DECLARED three-outcome fork; codex 5.6-sol adversarial checks throughout the arc, cross-model, whose findings OVERRIDE the solve everywhere they collide; OPUS MECHANICAL DRAFTING ONLY; and supervisor review and landing -- with common-mode risk reduced and NOT eliminated. The scope is TWO FIXTURES and no wider, with the measure leg at 12x6 alone; it is NOT a continuum statement, NOT A FLAVOR BRIDGE, NOT a derivation of the Koide relation and NOT a derivation of the Born rule; and the disclosures are complete, THIS BLOCK'S OWN DEFECTS INCLUDED -- two fixtures with no wider ladder, the no-registration theorem a NON-SUPPLY result at committed-class scope, the Wigner leg SILENT AND NOT NEGATIVE, Q = (1+2r)/3 and r_from_slot_count still imported authority, the measure leg scoped to the landed H1-170b declaration with an exponent invisible to every landed normalized window, and the sigma-reality condition NAMED AND NOT DECIDED -- alongside NO FLOAT anywhere, the not-re-verified list, N1 through N8, the W1 wall, the scope-key certificate, the LaTeX rho guard, the pool-2 leads, the three handoff items, zero axiom retirement, zero obligation retirement, no TOE percentage movement, a retained-positive end-to-end theory count that remains zero, and NO priority or originality wording anywhere in the note",
        gate_values["H"])
    checks.report()
    print(N5_FENCE)
    return checks.finish()


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except Exception as error:
        print(f"[FAIL] INTERNAL-EXCEPTION: {type(error).__name__}: {error}")
        print("TOTAL: PASS=0 FAIL=1")
        raise
