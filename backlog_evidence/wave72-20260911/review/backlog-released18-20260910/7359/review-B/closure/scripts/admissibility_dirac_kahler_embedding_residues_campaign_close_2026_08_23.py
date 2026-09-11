#!/usr/bin/env python3
"""BLOCK 179 -- THE EMBEDDING RESIDUES AND THE CAMPAIGN CLOSE.

THE RESULT, AND ITS EXACT SCOPE.  On the committed 12x6 CONSTANT-CARRIER
Dirac-Kahler fixture -- cover extent T_cover = 12 at T_phys = 6 and L_x = 6,
region pin c = 1, shear zero on the pinned time levels {0,1} and the committed
CARRIER_SIGMA = 3/5 elsewhere, constant volume 7/5, s_x = 3/5, s_t = 0 and mass
1, so that Q is symbol-free -- with the chart translation U|t,x> = |t, x+2 mod 6>
and the DISCLOSED cyclotomic field Q(sqrt(-3)):

  1. RESIDUE 4, THE ORIENTATION SELECTOR -- DISSOLVED TRIVIALLY.  The two
     chart-momentum characters at (t,p) = (0,0) satisfy f_2 = conj(f_1) exactly
     and give the IDENTICAL restriction f_1^dag Q f_1 = f_2^dag Q f_2 =
     3193/2240, with antilinear residuals f^T Q f = 0 EXACTLY in both, so each
     orientation restricts to (3193/2240)|z|^2 with no z^2 term.  NO SELECTOR IS
     NEEDED.  BUT THE CROSS-MODEL CHECK ADJUDICATED THAT EQUALITY FORCED AND NOT
     CONTENTFUL -- the measured orbit block is a real SCALAR, so the equality is
     an algebraic tautology after the real-symmetric restriction -- and this
     block carries the adjudication rather than the stronger wording.

  2. RESIDUE 3, THE MULTIPLICITY SELECTOR -- NARROWED AND NOT DISSOLVED.  ALL
     TWELVE copies of the k = 1 character restrict to beta|z|^2 with zero
     antilinear residual, so every copy is one complex slot in the SAME fork
     cell; the coefficient is LEVEL-INDEXED and parity-independent with EXACTLY
     THREE values, 3193/2240 at t = 0 and 2, 43/35 at t = 1 and 1817/1120 at
     t = 3, 4, 5, over level classes {0,2}, {1} and {3,4,5} which DO NOT
     coincide with the pinned/free split.  THE SOLVE'S DISSOLUTION CLAIM IS
     QUOTED AND REFUTED: the rank-12 isotype Gram is NOT diagonal (36 nonzero
     off-diagonal entries; the (3,0) copy couples to exactly five others), and
     the flavor lane's own slot counter is ADDITIVE, so retaining all twelve
     holomorphic copies gives r = 6 and Q = 13/3 and NOT r = 1/2, Q = 2/3.
     Q = 2/3 FIRES FOR THE EXPLICIT ONE-COPY EMBEDDING and a multiplicity
     selector, quotient or fiber theorem is A NAMED OPEN REQUIREMENT.

  3. THE CARRIER MAP -- EXHIBITED AT REPRESENTATION/METRIC-INSTANCE LEVEL.
     U_orb = P_3 EXACTLY on the natural orbit basis with U E = E P_3, the same
     3-cycle as the flavor lane's C_3 on the hw = 1 translation characters.  The
     orbit restriction is R = (3193/2240) I_3: circulant, J-COMPONENT EXACTLY
     ZERO, an instance of M(alpha, beta) = alpha P_s + beta P_d at the
     DEGENERATE point alpha = beta = 3193/2240, det_R = alpha beta^2 =
     32553430057/11239424000 EXACTLY.  BUT R IS A SCALAR, so its
     METRIC-PRESERVATION LEG IS BASIS-VACUOUS -- exhibited against a
     non-circulant witness that commutes with R while a nondegenerate family
     member does not -- and what is exhibited is AN EQUIVARIANT ONE-ORBIT MODULE
     MAP AND NOT A PHYSICAL OBSERVABLE-PRESERVING CARRIER MAP.

  4. THE REMAINDER IS SIX NAMED ITEMS, three restored or supplied by the check
     and three from the solve: the multiplicity selector or fiber theorem; the
     M_2(C) carrier-algebra embedding; non-vacuous physical observable
     preservation; the record-write identification; the ambient hw >= 2
     mismatch; and the metric-ratio degeneracy, at which THEIR r-SELECTION WALL
     IS NOT REACHED.

  5. THE CAMPAIGN CLOSE is carried as a STRUCTURAL VERDICT with no measurement
     of its own, over SEVEN BLOCKS of the landed chain, with the campaign's
     corrections ledger in three groups and the owner's-bar items listed.

GATES
  A  authority: main plus the TWO Block 178 artifacts content-bound, the parent
     runner ACTUALLY IMPORTED, and the stale pin verified to carry NEITHER.
  B  the two banners -- the inertia convention and the imposed-object banner
     with the counting-bit PROPOSAL restated -- and the 12x6 fixture rebuilt
     from LANDED modules with the (3193/2240)|z|^2 restriction gated.
  C  RESIDUE 4: both orientations exactly equal, both antilinear residuals zero,
     and the forced-not-contentful adjudication carried as note text.
  D  RESIDUE 3: the twelve-copy ledger with 1817/1120 and 43/35, the level
     classes, the t = 3 slot typing, AND THE REFUTATION -- the non-diagonal
     rank-12 Gram and the raw-count r = 6 / Q = 13/3 counter-exhibit computed by
     the flavor lane's OWN arbiter -- with the one-copy scoping gated.
  E  THE CARRIER MAP: U_orb == P_3, the circulant/isotype decomposition with all
     eigenvalues equal, det_R = 32553430057/11239424000, the M(alpha, beta)
     instance identity, and the basis-vacuity witness.
  F  THE REMAINDER LEDGER: SIX items present verbatim-keyed in the note, with
     the degeneracy statement and the unreached ratio wall gated.
  G  THE CAMPAIGN CLOSE: the landed-block citations, the corrections ledger in
     three groups, the owner's-bar list, and the counting-bit-proposal
     restatement.
  H  note at final path, the FULL scope-key certificate, and the N5 fence.

BASELINE EXPECTATION: 7 of 8, with H failing on note-at-final-path alone until
the note is landed at docs/.

RUNNING
  python3 scripts/admissibility_dirac_kahler_embedding_residues_campaign_close_2026_08_23.py
  python3 ... --list-mutations
  python3 ... --mutation claim_multiplicity_dissolved
  python3 ... --deep

NOTES FOR THE LANDING AGENT
  1. PARENT_COMMIT is REAL and PARENT_REF resolves to it; nothing needs sed.
  2. CURRENT_MAIN was RE-RESOLVED at draft time.
  3. The stale pin is the Block 177 tip, a real ancestor of HEAD that carries
     NEITHER Block 178 artifact -- which is what makes the
     stale_parent_authority mutation bite.
  4. Re-run at landing; gate H should then pass and the battery should be 8/8.
"""

from __future__ import annotations

import argparse
import ast
import subprocess
import sys
import time
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

import sympy as sp

R = sp.Rational
Z0 = sp.Integer(0)
ONE = sp.Integer(1)

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

# THE PARENT IMPORT.  Block 178 is the stack parent AND the content parent: it
# re-exports the whole landed chain, and its campaign is the one this block
# closes.  NOTHING from the scratchpad is imported anywhere in this runner; the
# 12x6 fixture below is rebuilt from LANDED modules reached through this import.
try:
    import admissibility_dirac_kahler_shear_mirror_interference_2026_08_23 as b178
    PARENT_IMPORT_LANDED = True
except ModuleNotFoundError:                                   # unlanded parent
    b178 = None
    PARENT_IMPORT_LANDED = False

if b178 is not None:
    b177 = b178.b177
    b176 = b178.b176
    b175 = b178.b175
    b174 = b178.b174
    b171 = b178.b171
    b170 = b178.b170
    b166 = b178.b166
    b165 = b178.b165
else:                                                  # pragma: no cover
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
    "ADMISSIBILITY_DIRAC_KAHLER_EMBEDDING_RESIDUES_CAMPAIGN_CLOSE_BOUNDED_"
    "THEOREM_NOTE_2026-08-23.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
# DECLARED DRAFT FALLBACK, read ONLY when the final path is absent.  Gate H
# requires the final path, so the fallback never makes a gate pass.
DRAFT_NOTE_PATH = Path(
    "/private/tmp/claude-502/"
    "-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-"
    "gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/"
    "scratchpad/block179_note_draft.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE SINGLE-PARENT PIN.  Block 178 is BOTH the stack parent and the content
# parent, so there are exactly TWO artifact pins.
BLOCK178_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHEAR_MIRROR_INTERFERENCE_BOUNDED_THEOREM_"
    "NOTE_2026-08-23.md"
)
BLOCK178_RUNNER = (
    "scripts/admissibility_dirac_kahler_shear_mirror_interference_"
    "2026_08_23.py"
)
PARENT_ARTIFACTS = (BLOCK178_NOTE, BLOCK178_RUNNER)
PARENT_ARTIFACT_BLOBS = (
    "ecbbd297e81477b5a61d9b29bdc57bf12a954e78",   # Block 178 note
    "4de322fe54a5059378fe74ed1d3e3320ae04b221",   # Block 178 runner
)

# THE FLAVOR LANE'S FORK ARBITER, reached through the LANDED Block 176 loader.
# It is read from origin/main at Block 176's PINNED BLOB, it is NOT a worktree
# read, and it is NOT in AUDIT_INPUT_PATHS -- the same discipline Block 176
# landed.  Its own correctness is not checked here and its source sits OUTSIDE
# this runner's AST exactness surface, which is disclosed and not hidden.
FLAVOR_RUNNER = "scripts/berezin_detc_detr_fork_2026_06_04.py"
FLAVOR_FORK_NOTE = "docs/KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md"
FLAVOR_COUNTING_FUNCTIONS = ("r_from_slot_count", "q_from_r")

# Deliberately literal: this is the complete audit read surface.  Every entry is
# a WORKTREE-READABLE LANDED path at landing time.  The flavor RUNNER is
# deliberately absent, because it is read from origin/main and never from the
# worktree.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_EMBEDDING_RESIDUES_CAMPAIGN_CLOSE_BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHEAR_MIRROR_INTERFERENCE_BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "docs/KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md",
    "scripts/admissibility_dirac_kahler_shear_mirror_interference_2026_08_23.py",
    "scripts/admissibility_dirac_kahler_complex_structure_synthesis_2026_08_23.py",
    "scripts/admissibility_dirac_kahler_generator_trilemma_kernel_2026_08_21.py",
    "scripts/admissibility_dirac_kahler_closure_audit_two_2026_08_21.py",
)

AUDIT_TIMEOUT_SEC = 600
# THE FIVE-PIN AUTHORITY BLOCK, single-line hex literals refreshed by anchored
# sed at landing.  CURRENT_MAIN WAS RE-RESOLVED AT DRAFT TIME.
CURRENT_MAIN = "0e212ee4c66019a9dc8dae204680d7c45a0ae8ab"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
# This block stacks on the Block 178 tip, so the parent branch is that.
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block178-"
              "shear-mirror-interference-20260823")
PARENT_COMMIT = "5d8bc1e92be934cf3f90368f6cd0a68bb224d9fa"
# The Block 177 tip: a real ancestor of HEAD that predates Block 178 and
# therefore carries NEITHER Block 178 artifact.  Read ONLY under the stale
# mutation, where the missing blobs are exactly what makes it bite.
STALE_PARENT_COMMIT = "1db319647c14f447cfbcd90bc2da99a2205102e4"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "break_beta_restriction",
    "claim_orientation_selector_needed",
    "claim_multiplicity_dissolved",
    "claim_q_two_thirds_unconditional",
    "claim_carrier_map_physical",
    "break_det_r",
    "claim_full_flavor_bridge",
    "claim_ratio_wall_reached",
    "claim_readout_derived",
    "drop_owner_bar_list",
    "drop_corrections_ledger",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_objects_registered": "B",
    "break_beta_restriction": "B",
    "claim_orientation_selector_needed": "C",
    "claim_multiplicity_dissolved": "D",
    "claim_q_two_thirds_unconditional": "D",
    "claim_carrier_map_physical": "E",
    "break_det_r": "E",
    "claim_full_flavor_bridge": "F",
    "claim_ratio_wall_reached": "F",
    "claim_readout_derived": "G",
    "drop_owner_bar_list": "G",
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
# the Block 176/177/178 convention.  IT IS NOT the full transitive module
# closure, AND IT DOES NOT COVER THE FLAVOR ARBITER, which is read from
# origin/main through the landed Block 176 loader; gate A reports the residual
# count outside the surface rather than claiming the corpus clean.
def audit_source_paths() -> tuple:
    paths = [Path(__file__).resolve()]
    for module in (b178, b177, b176, b175, b174, b171):
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
    for name, module in (("b178", b178), ("b177", b177), ("b176", b176),
                         ("b175", b175), ("b174", b174), ("b171", b171),
                         ("b170", b170), ("b165", b165)):
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
            for name in ("b178", "b177", "b176", "b175", "b174", "b171")),
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
        # THE STALE LEG.  At the Block 177 tip NEITHER Block 178 artifact
        # exists, so this is False and the stale mutation fails gate A.
        bool(all(is_hash(v) for v in stale_blobs)
             and stale_blobs == worktree_blobs),
        is_ancestor(STALE_PARENT_COMMIT, "HEAD"),
        not any(is_hash(v) for v in stale_blobs),
        PARENT_IMPORT_LANDED,
        residue_report())


# ---------------------------------------------------------------------------
# the 179-specific layer
# ---------------------------------------------------------------------------
NUMERALS: list = []


def record(value):
    """Every reported numeral passes through here for the no-float gate."""
    NUMERALS.append(value)
    return value


# THE COMMITTED FIXTURE, declared as literals so every constant is auditable.
COVER_T = 12
LX = 6
PHYS_T = 6
FIXTURE_N = 36
CONST_VOLUME = R(7, 5)
REGION_PIN = 1
PINNED_LEVELS = (0, 1)
FREE_LEVELS = (2, 3, 4, 5)
SHIFT = 2
# THE DISCLOSED CYCLOTOMIC FIELD.  omega is an exact primitive cube root of
# unity and every non-rational entry below lies in Q(omega) = Q(sqrt(-3)).
OMEGA = (-ONE + sp.sqrt(3) * sp.I) / 2
P3 = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
BETA = R(3193, 2240)
LEVEL_LEDGER = {0: R(3193, 2240), 1: R(43, 35), 2: R(3193, 2240),
                3: R(1817, 1120), 4: R(1817, 1120), 5: R(1817, 1120)}
LEVEL_CLASSES = ((0, 2), (1,), (3, 4, 5))
DISTINCT_LEVEL_VALUES = 3
PARITIES = (0, 1)
COPY_COUNT = 12
GRAM_OFFDIAGONAL_NONZEROS = 36
COUPLED_COPY = (3, 0)
COUPLED_PARTNERS = ((2, 0), (2, 1), (3, 1), (4, 0), (4, 1))
TYPED_COPY = (3, 0)
TYPED_COPY_BETA = R(1817, 1120)
DET_R = R(32553430057, 11239424000)
ONE_COPY_SLOTS = 1
ALL_COPY_SLOTS = 12
ONE_COPY_R = R(1, 2)
ONE_COPY_Q = R(2, 3)
ALL_COPY_R = sp.Integer(6)
ALL_COPY_Q = R(13, 3)
NONDEGENERATE_ALPHA = ONE
NONDEGENERATE_BETA = sp.Integer(2)
RUNTIME_BUDGET_SEC = 120
DEEP_RUNTIME_BUDGET_SEC = 600
POOL_TWO_LEADS = 3
HANDOFF_ITEMS = 3
LANDED_BLOCK_CITATIONS = (171, 174, 175, 176, 177, 178, 179)
CAMPAIGN_PRS = ("#7318", "#7325", "#7330", "#7331", "#7336")

# THE IMPOSED OBJECTS OF THIS BLOCK, declared as a literal so the banner is a
# measured object and not only prose.  NONE of them is registered or adopted.
IMPOSED_OBJECTS = (
    "the committed 12x6 CONSTANT-CARRIER fixture: T_cover = 12 at T_phys = 6 and L_x = 6, region pin c = 1, shear zero on the pinned levels {0,1} and CARRIER_SIGMA = 3/5 elsewhere, constant volume 7/5, s_x = 3/5, s_t = 0 and mass 1",
    "the chart translation U|t,x> = |t, x+2 mod 6>, its cyclotomic projectors P_k = (I + omega^(-k) U + omega^(-2k) U^2)/3, and the DISCLOSED field Q(omega) = Q(sqrt(-3))",
    "the chart-momentum characters f_k(t,p) = 3^(-1/2) sum_j omega^(-kj)|t, p+2j> at every time level and parity class, and the conjugate pair f_2 = conj(f_1)",
    "the 3-element chart ORBIT {(0,0),(0,2),(0,4)}, its embedding E and the orbit restriction R = E^T Q E",
    "the flavor lane's fork-input family M(alpha, beta) = alpha P_s + beta P_d on the regular R[Z_3] module, with det_R M = alpha beta^2, READ from landed authority and never re-derived here",
    "the non-circulant basis-vacuity witness X = e_0 e_1^T and the nondegenerate control member M(1,2)",
    "the committed reflection, region pin, slice index set, class map CM-SITE, slot order and record-slice scope, inherited",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
# THE PROPOSALS AT THE OWNER'S BAR, declared as counted literals.  NONE is
# adopted and NONE is registered.
OWNER_BAR_ITEMS = (
    "THE COUNTING-BIT SUPPLY: POLARIZATION-SELECT supplied at action/type level "
    "for the explicit ONE-COPY embedding, Q = 2/3 exactly, scoped by this "
    "block's refutation of the multiplicity dissolution -- A PROPOSAL",
    "THE REFLECTION-PAIRING READOUT PRINCIPLE: the reading of |det Q|^-2 as Z "
    "paired with its own reflection -- A PROPOSAL, narrowed by Blocks 177 and "
    "178 since positivity and sensitivity supply no selection",
    "THE DRAWER ITEMS FROM THE PRIOR CAMPAIGN, still standing and unadopted: "
    "the bridge axiom in the drawer; the design fork; the b141/b142 items; and "
    "e_x = -1",
)
# THE DECISION that belongs to the owner and is NOT taken here.
OWNER_DECISIONS = (
    "THE READOUT AXIOM: whether any composition/Born/readout axiom is ever "
    "supplied that would select one member of the fork-independent family -- it "
    "is ABSENT here, it is NEVER PROPOSED here, and it stays the owner's",
)
# THE SIX REMAINDER ITEMS.  Three were restored or supplied by the cross-model
# check and three come from the solve; all six are OPEN.
REMAINDER_ITEMS = (
    "THE MULTIPLICITY SELECTOR OR FIBER THEOREM: a selector, a quotient, or a "
    "theorem that the rank-12 chart multiplicity is external base-space "
    "degeneracy.  Copywise identical type does NOT reduce the total slot count "
    "to one.  RESTORED BY THE CHECK AND LOAD-BEARING.  STATUS: ADDRESSED BY THE "
    "FIBER-THEOREM SOLVE, CHECK PENDING -- NOT RESOLVED, and it stays an OPEN "
    "item in this ledger until the cross-model check on that solve lands",
    "THE M_2(C) CARRIER-ALGEBRA EMBEDDING: an injective unital *-map preserving "
    "products and adjoints, which identifying content-writes with shear pins "
    "does NOT supply.  RESTORED BY THE CHECK",
    "NON-VACUOUS PHYSICAL OBSERVABLE PRESERVATION: equality of two "
    "regular-representation 3-cycles plus preservation of a scalar metric "
    "proves MODULE EQUIVALENCE and not that the physical generators and "
    "observables coincide.  SUPPLIED BY THE CHECK",
    "THE RECORD-WRITE IDENTIFICATION: their M_2(C) content-writes against our "
    "shear pins -- untouched",
    "THE AMBIENT MISMATCH: their hw >= 2 shell sectors have no chart-line "
    "counterpart at this fixture -- untouched",
    "THE METRIC-RATIO DEGENERACY: our realization sits at the symmetric point "
    "alpha = beta of their family, so THEIR r-SELECTION WALL IS NOT REACHED by "
    "this instance and only the polarization/counting bit transfers",
)
# THE FIVE SUPERVISOR CORRECTIONS OF THE CAMPAIGN, carried verbatim-keyed.
SUPERVISOR_CORRECTIONS = (
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
    "COUNTING-BIT SCOPE because every copy fires the holomorphic cell and the "
    "fork needs only the slot count.  REFUTED THIS ROUND: the slot counter is "
    "ADDITIVE, so the full rank-12 eigenspace gives r = 6 and Q = 13/3",
)
# THE CHECKERS' DISCOVERIES ACROSS THE CAMPAIGN, in three groups.
CHECKER_DISCOVERIES = (
    "ON THE SCALAR-SECTOR SOLVE (Block 177): the OBJECT MISMATCH with exact "
    "witness -35233/38760 making the theorem CONDITIONAL; the complex-scope "
    "correction r^2 -> |r|^2; the clean witness v = e_0 - 5 e_4 with "
    "v^dag G v = -57/160; and sector-uniqueness, NOT readout-uniqueness",
    "ON THE MIRROR SOLVE (Block 178): the antiunitary convention r Q r = Q^T; "
    "the volume counterexample (1,2,3,4)_x; the full hop censuses and the "
    "refuted extent-scaling story; the 24-entry single-level accounting; and "
    "the rational-continuity proof superseding the sample-based limit claim",
    "ON THIS BLOCK'S RESIDUE SOLVE: the orientation equality adjudicated FORCED "
    "and not new selector content; the multiplicity dissolution REFUTED with "
    "the non-diagonal rank-12 Gram and the r = 6, Q = 13/3 counter-exhibit; the "
    "carrier map weakened to representation/metric-instance level with the "
    "basis-vacuity of the scalar metric leg named; and the remainder list "
    "expanded from three items to six",
)
# THE DRAFT WORKERS' CATCHES, disclosed rather than absorbed.
DRAFT_WORKER_CATCHES = (
    "BLOCK 178's DRAFT -- THE HERM-DET BLINDNESS CATCH: 1/det(herm Q) is "
    "positive and fork-independent but DIAL-BLIND, because herm(Q) is itself "
    "s_t-free; disclosed rather than dropped and excluded from the sensitive "
    "sub-family",
    "THIS BLOCK'S DRAFT -- THE LEVEL LEDGER IS THREE-VALUED: the campaign "
    "record's two-value phrasing omits 43/35 at t = 1 and the return of "
    "3193/2240 at t = 2, and the coefficient classes {0,2}, {1} and {3,4,5} do "
    "NOT coincide with the pinned/free split {0,1} and {2,3,4,5}",
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


def build_fixture():
    """THE 12x6 CONSTANT CARRIER, rebuilt from LANDED modules only.

    This is the Block 174 Width(6, 'const') construction reproduced from its
    landed ingredients -- b170.Bench, b166.carrier_substitution and the landed
    b171 dial constants -- and NOT imported from any scratchpad module.
    """
    bench = Bench(f"{COVER_T}x{LX}", COVER_T, LX)
    fx = bench.fx
    pinned = {(bench.c - 1) % fx.PHYS_T, bench.c % fx.PHYS_T}
    field = {(t, x): (Z0 if t in pinned else b171.CARRIER_SIGMA, CONST_VOLUME)
             for (t, x) in fx.CELLS}
    sub = b166.carrier_substitution(fx, field)
    sub[SX] = b171.BENCH_SX
    sub[ST] = Z0
    sub[MASS] = b171.BENCH_MASS
    action = sp.expand(bench.Q.subs(sub))
    return bench, tuple(sorted(pinned)), action


def chart_translation(bench) -> sp.Matrix:
    """U|t,x> = |t, x+2 mod L_x>, one block per physical time level."""
    translation = sp.zeros(bench.N)
    for t in range(bench.T):
        for x in range(bench.lx):
            translation[bench.lx * t + (x + SHIFT) % bench.lx,
                        bench.lx * t + x] = 1
    return translation


def chart_character(bench, t: int, parity: int, k: int) -> sp.Matrix:
    vector = sp.zeros(bench.N, 1)
    for index in range(3):
        vector[bench.lx * t + parity + SHIFT * index] = (
            OMEGA ** (-k * index) / sp.sqrt(3))
    return vector


def orbit_embedding(bench, t: int, parity: int) -> sp.Matrix:
    embedding = sp.zeros(bench.N, 3)
    for index in range(3):
        embedding[bench.lx * t + parity + SHIFT * index, index] = 1
    return embedding


# ---------------------------------------------------------------------------
# B. the fixture and the banners
# ---------------------------------------------------------------------------
def measure_fixture() -> dict:
    """THE COMMITTED FIXTURE AND ITS CHART STRUCTURE, exactly."""
    out: dict = {}
    bench, pinned, action = build_fixture()
    out["bench"] = bench
    out["Q"] = action
    out["N"] = bench.N
    out["T_phys"] = bench.T
    out["lx"] = bench.lx
    out["c"] = bench.c
    out["pinned"] = pinned
    out["free"] = tuple(t for t in range(bench.T) if t not in pinned)
    out["symbol_free"] = not action.free_symbols
    out["inertia"] = tuple(b165.real_symmetric_inertia(herm(action)))
    out["carrier_sigma"] = b171.CARRIER_SIGMA
    out["volume"] = CONST_VOLUME

    translation = chart_translation(bench)
    out["U"] = translation
    identity = sp.eye(bench.N)
    out["U_order_three"] = translation ** 3 == identity
    out["U_unitary"] = sp.expand(translation.H * translation) == identity
    out["U_commutes"] = is_zero(sp.expand(action * translation
                                          - translation * action))
    out["omega_primitive"] = sp.expand(OMEGA ** 2 + OMEGA + 1) == 0
    projectors = tuple(
        sp.expand(sum((OMEGA ** (-k * power) * translation ** power
                       for power in range(3)),
                      sp.zeros(bench.N))) / 3
        for k in range(3))
    out["projector_traces"] = tuple(
        exact_scalar(sp.trace(projector)) for projector in projectors)
    out["projectors_resolve"] = matrix_zero(
        sum(projectors, sp.zeros(bench.N)) - identity)
    return out


# ---------------------------------------------------------------------------
# C. RESIDUE 4 -- the orientation selector
# ---------------------------------------------------------------------------
def measure_orientation(fixture: dict) -> dict:
    """BOTH ORIENTATIONS, restricted exactly, with their antilinear residuals."""
    out: dict = {}
    bench, action, translation = fixture["bench"], fixture["Q"], fixture["U"]
    f_one = chart_character(bench, 0, 0, 1)
    f_two = chart_character(bench, 0, 0, 2)
    out["conjugate_pair"] = matrix_zero(f_two - f_one.conjugate())
    out["f_one_eigen"] = matrix_zero(translation * f_one - OMEGA * f_one)
    out["f_two_eigen"] = matrix_zero(translation * f_two - OMEGA ** 2 * f_two)
    out["f_one_unit"] = exact_scalar((f_one.H * f_one)[0]) == 1
    out["f_two_unit"] = exact_scalar((f_two.H * f_two)[0]) == 1
    out["beta_one"] = exact_scalar((f_one.H * action * f_one)[0])
    out["beta_two"] = exact_scalar((f_two.H * action * f_two)[0])
    out["antilinear_one"] = exact_scalar((f_one.T * action * f_one)[0])
    out["antilinear_two"] = exact_scalar((f_two.T * action * f_two)[0])
    # THE SYMBOLIC TYPING: phi = (x + iy) f gives beta(x^2 + y^2) and nothing
    # else -- one complex slot, no z^2 and no conj(z)^2 term.
    x_symbol, y_symbol = sp.symbols("x y", real=True)
    for label, vector, beta in (("one", f_one, out["beta_one"]),
                                ("two", f_two, out["beta_two"])):
        phi = (x_symbol + sp.I * y_symbol) * vector
        form = exact_scalar((phi.H * action * phi)[0])
        out[f"typing_{label}"] = sp.expand(
            form - beta * (x_symbol ** 2 + y_symbol ** 2)) == 0
    out["induced_metric_one"] = (
        sp.diag(out["beta_one"], out["beta_one"])
        == sp.Matrix([[BETA, Z0], [Z0, BETA]]))
    # THE MEASURED FLAG the orientation mutation bites on.  It is FALSE and that
    # is the point: the two orientations do NOT differ, so nothing selects.
    out["orientations_differ"] = out["beta_one"] != out["beta_two"]
    return out


# ---------------------------------------------------------------------------
# D. RESIDUE 3 -- the multiplicity selector, and the REFUTATION
# ---------------------------------------------------------------------------
def load_counting_arbiter() -> tuple:
    """The flavor lane's OWN slot counter, through the LANDED Block 176 loader.

    The counter is THEIRS: r_from_slot_count and q_from_r are called, and the
    additive counter-exhibit below is therefore computed by the machinery whose
    lane the question belongs to and not by a re-implementation here.
    """
    if b176 is None:                                       # pragma: no cover
        return {}, ""
    arbiter, seen = b176.load_fork_arbiter()
    return arbiter, seen


def measure_multiplicity(fixture: dict, deep: bool) -> dict:
    """THE TWELVE-COPY LEDGER, THE TYPING, AND THE ADDITIVE COUNTER-EXHIBIT."""
    out: dict = {}
    bench, action = fixture["bench"], fixture["Q"]
    copies = tuple((t, p) for t in range(bench.T) for p in PARITIES)
    out["copies"] = copies
    out["copy_count"] = len(copies)

    vectors = {copy: chart_character(bench, copy[0], copy[1], 1)
               for copy in copies}
    ledger = {}
    antilinear = {}
    typing = {}
    x_symbol, y_symbol = sp.symbols("x y", real=True)
    for copy, vector in vectors.items():
        beta = exact_scalar((vector.H * action * vector)[0])
        ledger[copy] = beta
        antilinear[copy] = exact_scalar((vector.T * action * vector)[0])
        phi = (x_symbol + sp.I * y_symbol) * vector
        form = exact_scalar((phi.H * action * phi)[0])
        typing[copy] = sp.expand(
            form - beta * (x_symbol ** 2 + y_symbol ** 2)) == 0
    out["ledger"] = ledger
    out["antilinear_all_zero"] = all(value == 0 for value in antilinear.values())
    out["typing_all_hold"] = all(typing.values())
    out["parity_independent"] = all(
        ledger[(t, 0)] == ledger[(t, 1)] for t in range(bench.T))
    out["level_values"] = {t: ledger[(t, 0)] for t in range(bench.T)}
    out["distinct_values"] = len({sp.srepr(v) for v in ledger.values()})
    classes: dict = {}
    for t in range(bench.T):
        classes.setdefault(sp.srepr(ledger[(t, 0)]), []).append(t)
    out["level_classes"] = tuple(sorted(
        tuple(levels) for levels in classes.values()))
    out["classes_match_pin_split"] = (
        set(out["level_classes"]) == {tuple(fixture["pinned"]),
                                      tuple(fixture["free"])})
    # THE TYPED COPY, spelled out because its coefficient differs from the one
    # the landed embedding used.
    out["typed_copy_beta"] = ledger[TYPED_COPY]
    out["typed_copy_antilinear"] = antilinear[TYPED_COPY]
    out["typed_copy_typing"] = typing[TYPED_COPY]

    # THE FIRST REFUTATION LEG: the rank-12 isotype Gram is NOT diagonal.
    basis = sp.Matrix.hstack(*[vectors[copy] for copy in copies])
    out["copies_orthonormal"] = matrix_zero(
        sp.expand(basis.H * basis) - sp.eye(len(copies)))
    gram = sp.Matrix(len(copies), len(copies), lambda i, j: exact_scalar(
        (vectors[copies[i]].H * action * vectors[copies[j]])[0]))
    offdiagonal = [(i, j) for i in range(len(copies))
                   for j in range(len(copies))
                   if i != j and gram[i, j] != 0]
    out["gram_offdiagonal_nonzeros"] = len(offdiagonal)
    out["gram_is_diagonal"] = len(offdiagonal) == 0
    index = copies.index(COUPLED_COPY)
    out["coupled_partners"] = tuple(
        copies[j] for j in range(len(copies))
        if j != index and gram[index, j] != 0)

    # THE SECOND AND DECISIVE REFUTATION LEG: the flavor lane's OWN slot
    # counter is ADDITIVE, so the full eigenspace does NOT give Q = 2/3.
    arbiter, flavor_seen = load_counting_arbiter()
    out["arbiter_blob"] = flavor_seen
    out["arbiter_loaded"] = bool(arbiter) and all(
        name in arbiter for name in FLAVOR_COUNTING_FUNCTIONS)
    if out["arbiter_loaded"]:
        one_r = arbiter["r_from_slot_count"](ONE_COPY_SLOTS)
        all_r = arbiter["r_from_slot_count"](ALL_COPY_SLOTS)
        out["one_copy_r"] = R(Fraction(one_r).numerator,
                              Fraction(one_r).denominator)
        out["all_copy_r"] = R(Fraction(all_r).numerator,
                              Fraction(all_r).denominator)
        one_q = arbiter["q_from_r"](one_r)
        all_q = arbiter["q_from_r"](all_r)
        out["one_copy_q"] = R(Fraction(one_q).numerator,
                              Fraction(one_q).denominator)
        out["all_copy_q"] = R(Fraction(all_q).numerator,
                              Fraction(all_q).denominator)
    else:                                                  # pragma: no cover
        out["one_copy_r"] = out["all_copy_r"] = None
        out["one_copy_q"] = out["all_copy_q"] = None
    # THE TWO MEASURED FLAGS the two D mutations bite on.  BOTH ARE FALSE.
    out["multiplicity_is_dissolved"] = (
        out["arbiter_loaded"] and out["all_copy_q"] == out["one_copy_q"])
    out["q_is_unconditional"] = (
        out["arbiter_loaded"] and out["all_copy_q"] == ONE_COPY_Q)
    # THE DEEP LEG, DECLARED: re-derive the whole ledger from the CONJUGATE
    # k = 2 orientation.  It is NOT RUN at baseline, and None means NOT RUN
    # rather than agreement.
    if deep:
        conjugate = {}
        for copy in copies:
            vector = chart_character(bench, copy[0], copy[1], 2)
            conjugate[copy] = exact_scalar((vector.H * action * vector)[0])
        out["deep_ledger"] = {t: conjugate[(t, 0)] for t in range(bench.T)}
        out["deep_ledger_agrees"] = conjugate == ledger
    else:
        out["deep_ledger"] = {}
        out["deep_ledger_agrees"] = None
    return out


# ---------------------------------------------------------------------------
# E. the carrier map
# ---------------------------------------------------------------------------
def measure_carrier(fixture: dict) -> dict:
    """THE ORBIT: equivariance exact, metric an instance, metric leg vacuous."""
    out: dict = {}
    bench, action, translation = fixture["bench"], fixture["Q"], fixture["U"]
    embedding = orbit_embedding(bench, 0, 0)
    out["U_orbit"] = sp.expand(embedding.T * translation * embedding)
    out["U_orb_is_three_cycle"] = out["U_orbit"] == P3
    out["orbit_preserved"] = is_zero(
        sp.expand(translation * embedding - embedding * P3))
    out["U_orb_order_three"] = out["U_orbit"] ** 3 == sp.eye(3)

    restriction = sp.Matrix(3, 3, lambda i, j: exact_scalar(
        (embedding.T * action * embedding)[i, j]))
    out["restriction"] = restriction
    out["is_symmetric"] = restriction == restriction.T
    circulant = (restriction[0, 0], restriction[1, 0], restriction[2, 0])
    out["circulant_coefficients"] = circulant
    out["is_circulant"] = is_zero(sp.expand(
        restriction - (circulant[0] * sp.eye(3) + circulant[1] * P3
                       + circulant[2] * P3 ** 2)))
    out["distance_two_couplings_vanish"] = (circulant[1] == 0
                                            and circulant[2] == 0)
    singleton = (sp.eye(3) + P3 + P3 ** 2) / 3
    doublet = sp.eye(3) - singleton
    out["alpha"] = sp.expand((singleton * restriction).trace())
    out["beta"] = sp.cancel(sp.expand((doublet * restriction).trace()) / 2)
    out["is_family_instance"] = is_zero(sp.expand(
        restriction - out["alpha"] * singleton - out["beta"] * doublet))
    out["is_degenerate"] = out["alpha"] == out["beta"]
    # THE J-COMPONENT of the circulant, which is what a nonzero doublet
    # antisymmetric part would carry.  It is EXACTLY ZERO here.
    out["j_component"] = sp.cancel(circulant[1] - circulant[2])
    eigenvalues = restriction.eigenvals()
    out["eigenvalues"] = tuple(sorted(
        (sp.srepr(value), multiplicity)
        for value, multiplicity in eigenvalues.items()))
    out["all_eigenvalues_equal"] = len(eigenvalues) == 1
    out["det_r"] = sp.expand(restriction.det())
    out["det_matches_family_law"] = (
        out["det_r"] == sp.expand(out["alpha"] * out["beta"] ** 2))

    # THE BASIS-VACUITY WITNESS.  Because the restriction is a SCALAR, it
    # commutes with a NON-circulant matrix -- indeed with the whole algebra --
    # while a NONDEGENERATE member of the same family does not.  So the
    # metric-preservation leg constrains nothing and only U_orb carries content.
    witness = sp.zeros(3)
    witness[0, 1] = 1
    out["restriction_is_scalar"] = restriction == restriction[0, 0] * sp.eye(3)
    out["scalar_commutes_with_witness"] = is_zero(
        sp.expand(restriction * witness - witness * restriction))
    nondegenerate = sp.expand(NONDEGENERATE_ALPHA * singleton
                              + NONDEGENERATE_BETA * doublet)
    out["nondegenerate_fails_witness"] = not is_zero(
        sp.expand(nondegenerate * witness - witness * nondegenerate))
    out["centralizer_is_everything"] = all(
        is_zero(sp.expand(restriction * unit - unit * restriction))
        for unit in (sp.Matrix(3, 3, lambda a, b: 1 if (a, b) == (i, j) else 0)
                     for i in range(3) for j in range(3)))
    # THE TWO MEASURED FLAGS the E and F mutations bite on.  BOTH ARE FALSE.
    out["metric_leg_has_content"] = not out["restriction_is_scalar"]
    out["ratio_wall_reached"] = out["alpha"] != out["beta"]
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
    "imposed_object_banner",
    "nothing_registered",
    "measured_never_registered",
    "nothing_adopted",
    "owner_bar",
    "proposals_stay_proposals",
    "counting_bit_remains_proposal",
    "imported_authority",
    # --- W1 ---------------------------------------------------------------
    "w1",
    "campaign_thesis",
    "parent_block",
    "parent_pr",
    "grandparent_pr",
    "synthesis_pr",
    "residue_ledger_closed",
    "open_gates_content",
    # --- N1 ---------------------------------------------------------------
    "residue_four",
    "orientation_residue_quoted",
    "both_orientations_equal",
    "beta_literal",
    "conjugate_pair",
    "no_selector_needed",
    "orientation_forced_not_contentful",
    "algebraic_tautology",
    "antilinear_residual_zero",
    # --- N2 ---------------------------------------------------------------
    "residue_three",
    "multiplicity_residue_quoted",
    "twelve_copies",
    "level_indexed",
    "third_level_value",
    "bulk_level_value",
    "level_classes",
    "classes_not_pin_split",
    "dissolution_refuted",
    "gram_not_diagonal",
    "additive_slot_counter",
    "raw_count_thirteen_thirds",
    "one_copy_load_bearing",
    "one_copy_scoping",
    "named_open_requirement",
    "typed_copy",
    "block174_cited",
    # --- N3 ---------------------------------------------------------------
    "carrier_map",
    "carrier_residue_quoted",
    "equivariance_exact",
    "basis_to_basis",
    "circulant_j_zero",
    "degenerate_point",
    "fork_family_instance",
    "det_r_literal",
    "metric_leg_basis_vacuous",
    "one_orbit_module_map",
    "counting_bit_transfers_one_copy",
    "what_does_not_transfer",
    # --- N4 ---------------------------------------------------------------
    "remainder_ledger",
    "remainder_multiplicity_theorem",
    "remainder_algebra_embedding",
    "remainder_observable_preservation",
    "remainder_record_writes",
    "remainder_ambient",
    "remainder_ratio_degeneracy",
    "ratio_wall_not_reached",
    "only_polarization_transfers",
    # --- N5 ---------------------------------------------------------------
    "n5_verbatim",
    # --- N6 ---------------------------------------------------------------
    "campaign_close",
    "one_committed_structure",
    "complex_unit",
    "sesquilinear_grammar",
    "antiunitary_reflection",
    "seven_blocks",
    "born_candidate_in_family",
    "symmetric_power_theorem",
    "shear_mirror_theorem",
    "transport_response",
    "counting_bit_supplied",
    "cross_lane_pincer",
    "pincer_pr",
    "sister_lane_cited",
    "axioms_only_route_closed",
    "no_unique_readout",
    "readout_axiom_never_proposed",
    "sector_identification_fork",
    "full_bridge_needs_remainder",
    "owner_bar_list",
    "drawer_items",
    # --- N7 ---------------------------------------------------------------
    "corrections_ledger",
    "five_cut_hypotheses",
    "checker_discoveries",
    "draft_worker_catches",
    "checker_overrides",
    "codex_refute_check",
    "checker_credited",
    "level_ledger_catch",
    "herm_det_catch",
    "process_working",
    # --- N8 ---------------------------------------------------------------
    "verdict",
    "successor_question",
    "cycle913_caution",
    "non_supply_never_necessity",
    "candidacy_never_nature",
    "worker_profile",
    "supervisor_inline_science",
    "opus_mechanical_only",
    "common_mode",
    "one_fixture",
    "not_re_verified",
    "not_continuum",
    "not_a_flavor_bridge",
    "not_a_koide_derivation",
    "not_a_born_derivation",
    "no_priority_claim",
    "n1_n8",
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
)

# THE CAMPAIGN-CLOSE SECTION's own required subset, which is what gate G reads
# and what the two drop mutations remove a member of.
CLOSE_KEYS = (
    "campaign_close",
    "one_committed_structure",
    "seven_blocks",
    "born_candidate_in_family",
    "symmetric_power_theorem",
    "shear_mirror_theorem",
    "transport_response",
    "counting_bit_supplied",
    "one_copy_scoping",
    "cross_lane_pincer",
    "pincer_pr",
    "sister_lane_cited",
    "no_unique_readout",
    "readout_axiom_never_proposed",
    "sector_identification_fork",
    "full_bridge_needs_remainder",
    "owner_bar_list",
    "drawer_items",
    "counting_bit_remains_proposal",
    "corrections_ledger",
    "five_cut_hypotheses",
    "checker_discoveries",
    "draft_worker_catches",
)


def scope_certificate(note_text: str) -> dict:
    note = normalized_note(note_text)
    return {
        # --- N0 ---------------------------------------------------------------
        "convention_banner": "(n_+, n_-, n_0)" in note,
        "convention_hazard_order": "(n_+, n_0, n_-)" in note,
        "convention_collision_named": "congruence_inertia" in note
        and "real_symmetric_inertia" in note,
        "convention_literal_collision": "(4,4,0)" in note,
        "neither_helper_wrong": "neither helper is wrong" in note,
        "imposed_object_banner": "imposed measured object" in note,
        "nothing_registered": "nothing here is registered" in note,
        "measured_never_registered": "measured" in note
        and "never registered" in note,
        "nothing_adopted": "nothing is adopted" in note,
        "owner_bar": "the owner's bar" in note,
        "proposals_stay_proposals": "proposals stay proposals" in note,
        "counting_bit_remains_proposal":
            "the counting-bit supply remains a proposal" in note,
        "imported_authority": "imported authority" in note,
        # --- W1 ---------------------------------------------------------------
        "w1": __import__("re").search(r"\bw1\b", note) is not None,
        "campaign_thesis": "the campaign thesis" in note,
        "parent_block": "block 178" in note,
        "parent_pr": "#7336" in note,
        "grandparent_pr": "#7331" in note,
        "synthesis_pr": "#7330" in note,
        "residue_ledger_closed":
            "closes the embedding-residue ledger" in note,
        "open_gates_content": "open-gates content" in note,
        # --- N1 ---------------------------------------------------------------
        "residue_four": "residue 4" in note,
        "orientation_residue_quoted":
            "the k = 1 / k = 2 orientation has no selector" in note,
        "both_orientations_equal":
            "both orientations give the identical restriction coefficient"
            in note,
        "beta_literal": "3193/2240" in note,
        "conjugate_pair": "f_2 = conj(f_1)" in note,
        "no_selector_needed": "no selector is needed" in note,
        "orientation_forced_not_contentful": "forced and not contentful" in note,
        "algebraic_tautology": "an algebraic tautology after the "
        "real-symmetric restriction" in note,
        "antilinear_residual_zero": "the antilinear residuals are exactly zero"
        in note or "with zero antilinear residual" in note,
        # --- N2 ---------------------------------------------------------------
        "residue_three": "residue 3" in note,
        "multiplicity_residue_quoted":
            "the rank-12 chart multiplicity has no selector" in note,
        "twelve_copies": "all twelve copies" in note,
        "level_indexed": "the coefficient is level-indexed" in note,
        "third_level_value": "43/35" in note,
        "bulk_level_value": "1817/1120" in note,
        "level_classes": "{0,2}" in note and "{3,4,5}" in note,
        "classes_not_pin_split":
            "do not coincide with the pinned/free split" in note,
        "dissolution_refuted": "that inference is refuted" in note,
        "gram_not_diagonal": "the rank-12 isotype block is not diagonal" in note,
        "additive_slot_counter": "r_from_slot_count(n) = n/2" in note,
        "raw_count_thirteen_thirds": "q = (1 + 2r)/3 = 13/3" in note,
        "one_copy_load_bearing":
            "the one-copy choice in the original embedding was load-bearing"
            in note,
        "one_copy_scoping":
            "fires for the explicit one-copy embedding" in note,
        "named_open_requirement": "a named open requirement" in note,
        "typed_copy": "the `t = 3` copies" in note or "the t = 3 copies" in note,
        "block174_cited": "block 174" in note,
        # --- N3 ---------------------------------------------------------------
        "carrier_map": "the carrier map" in note,
        "carrier_residue_quoted":
            "observable-preserving equivariant carrier map" in note,
        "equivariance_exact": "u_orb = [[0,0,1],[1,0,0],[0,1,0]] = p_3" in note,
        "basis_to_basis": "basis-to-basis" in note,
        "circulant_j_zero": "j-component is exactly zero" in note,
        "degenerate_point": "alpha = beta = 3193/2240" in note,
        "fork_family_instance":
            "m(alpha, beta) = alpha p_s + beta p_d" in note,
        "det_r_literal": "32553430057/11239424000" in note,
        "metric_leg_basis_vacuous": "basis-vacuous" in note,
        "one_orbit_module_map": "equivariant one-orbit module map" in note,
        "counting_bit_transfers_one_copy":
            "the counting bit transfers through the exhibited map for one "
            "chosen copy" in note,
        "what_does_not_transfer": "what does not transfer" in note,
        # --- N4 ---------------------------------------------------------------
        "remainder_ledger": "the remainder, six named items" in note,
        "remainder_multiplicity_theorem":
            "the multiplicity selector or fiber theorem" in note,
        "remainder_algebra_embedding":
            "the `m_2(c)` carrier-algebra embedding" in note,
        "remainder_observable_preservation":
            "non-vacuous physical observable preservation" in note,
        "remainder_record_writes": "the record-write identification" in note,
        "remainder_ambient": "the ambient mismatch" in note
        and "hw >= 2" in note,
        "remainder_ratio_degeneracy": "the metric-ratio degeneracy" in note,
        "ratio_wall_not_reached":
            "their r-selection wall is not reached by this instance" in note,
        "only_polarization_transfers":
            "only the polarization/counting bit transfers" in note,
        # --- N5 ---------------------------------------------------------------
        # Raw substring membership makes the printed fence byte-identical to its
        # note occurrence.
        "n5_verbatim": N5_FENCE in note_text,
        # --- N6 ---------------------------------------------------------------
        "campaign_close": "the campaign close" in note,
        "one_committed_structure": "one committed structure" in note,
        "complex_unit": "the action's complex unit" in note,
        "sesquilinear_grammar": "sesquilinear-only grammar" in note,
        "antiunitary_reflection": "antiunitary reflection" in note,
        "seven_blocks": "seven blocks of the landed chain" in note,
        "born_candidate_in_family":
            "the born-shaped readout candidate" in note,
        "symmetric_power_theorem":
            "the conditional symmetric-power theorem" in note,
        "shear_mirror_theorem": "the shear-mirror theorem" in note,
        "transport_response": "record-consistency response" in note,
        "counting_bit_supplied": "q = 2/3" in note,
        "cross_lane_pincer": "the cross-lane pincer" in note,
        "pincer_pr": "#7318" in note,
        "sister_lane_cited": "#7325" in note,
        "axioms_only_route_closed":
            "closes the axioms-only selection route" in note,
        "no_unique_readout": "there is no unique readout derivation" in note,
        "readout_axiom_never_proposed": "none is proposed here" in note,
        "sector_identification_fork":
            "the sector identification is a genuine fork" in note,
        "full_bridge_needs_remainder":
            "the full flavor bridge needs the six-item remainder" in note,
        "owner_bar_list": "the items at the owner's bar" in note,
        "drawer_items": "the drawer items from the prior campaign" in note,
        # --- N7 ---------------------------------------------------------------
        "corrections_ledger": "the corrections ledger" in note,
        "five_cut_hypotheses": "the supervisor's five cut hypotheses" in note,
        "checker_discoveries": "the checkers' discoveries" in note,
        "draft_worker_catches": "the draft workers' catches" in note,
        "checker_overrides":
            "override the solve everywhere they collide" in note,
        "codex_refute_check": "codex 5.6-sol xhigh" in note,
        "checker_credited": "the checker is credited" in note,
        "level_ledger_catch": "the level ledger is three-valued" in note,
        "herm_det_catch": "the herm-det blindness catch" in note,
        "process_working": "the process working" in note,
        # --- N8 ---------------------------------------------------------------
        "verdict":
            "the embedding-residue ledger is resolved into one trivial "
            "dissolution, one narrowing, one representation-level exhibit and "
            "six named remainder items" in note,
        "successor_question": "the successor question" in note,
        "cycle913_caution": "cycle913" in note,
        "non_supply_never_necessity":
            "non-supply within this formalism" in note
            and "never metaphysical necessity" in note,
        "candidacy_never_nature": "candidacy within this formalism" in note
        and "never a claim about nature" in note,
        "worker_profile": "worker profile" in note,
        "supervisor_inline_science": "all solve-side science" in note,
        "opus_mechanical_only": "mechanical drafting only" in note,
        "common_mode": "common-mode" in note,
        "one_fixture": "one fixture" in note,
        "not_re_verified": "not re-verified" in note,
        "not_continuum": "not a continuum statement" in note,
        "not_a_flavor_bridge": "not a flavor bridge" in note,
        "not_a_koide_derivation":
            "not a derivation of the koide relation" in note,
        "not_a_born_derivation": "not a derivation of the born rule" in note,
        # NEGATIVE key, inherited from Blocks 164-178.
        "no_priority_claim": ("first positive" not in note
                              and "novel" not in note
                              and "unprecedented" not in note
                              and "for the first time" not in note),
        "n1_n8": all(__import__("re").search(rf"\bn{index}\b", note) is not None
                     for index in range(1, 9)),
        "ast_surface_disclosed": "ast surface" in note,
        "no_float": "no float" in note,
        "scope_key_certificate": "scope-key certificate" in note,
        # NEGATIVE key, inherited from Blocks 164-178.
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
    }


N5_FENCE = "N5: per_element: THE TWO BANNERS, FIRST AND WITH TEETH. THE INERTIA CONVENTION: every triple in this note is labelled and read in the (n_+, n_-, n_0) order of the LANDED Block 165 helper real_symmetric_inertia, while the landed b163/b164 helper congruence_inertia returns (n_+, n_0, n_-), measured on identical matrices, so THE LITERAL STRING (4,4,0) MEANS PSD in Block 164's landed fence and FULLY HYPERBOLIC here; NEITHER HELPER IS WRONG and no landed verdict changes, and this block's own triple inertia(herm Q) = (36,0,0)(n+,n-,n0)[b165] is positive definite under either reading. AND THE IMPOSED-OBJECT BANNER: NOTHING HERE IS REGISTERED OR ADOPTED -- the committed 12x6 constant-carrier fixture, the chart translation U with its cyclotomic projectors over the disclosed field Q(sqrt(-3)), the chart-momentum characters at every time level and parity class, the 3-element chart orbit with its embedding and restriction, the flavor lane's fork-input family M(alpha, beta) = alpha P_s + beta P_d read from landed authority and never re-derived here, and the inherited reflection, region pin, slice index set, class map CM-SITE, slot order and record-slice scope are IMPOSED MEASURED OBJECTS OF THIS BLOCK; AND THE COUNTING-BIT SUPPLY REMAINS A PROPOSAL AT THE OWNER'S BAR; NOTHING IS REGISTERED AND NOTHING IS ADOPTED.\nper_site: RESIDUE 4, THE ORIENTATION SELECTOR, DISSOLVED TRIVIALLY. At the committed 12x6 constant carrier the two chart-momentum characters at (t,p) = (0,0) are exact unit-norm eigenvectors of U at omega and omega^2 with f_2 = conj(f_1) EXACTLY, and their committed restrictions are IDENTICAL: f_1^dag Q f_1 = f_2^dag Q f_2 = 3193/2240, with the antilinear residuals f_1^T Q f_1 = f_2^T Q f_2 = 0 EXACTLY, so each orientation restricts to (3193/2240)|z|^2 with no z^2 term and induces the same real metric diag(3193/2240, 3193/2240). NO SELECTOR IS NEEDED. BUT THE CROSS-MODEL CHECK ADJUDICATED THAT EQUALITY FORCED AND NOT CONTENTFUL and this note carries the adjudication: because f_2 = conj(f_1), any real-symmetric orbit block gives the conjugate pair equal real Rayleigh quotients, and the measured orbit block is stronger still, a real SCALAR -- so the equality is an ALGEBRAIC TAUTOLOGY AFTER THE REAL-SYMMETRIC RESTRICTION and NOT NEW SELECTOR CONTENT. The residue is dissolved because it was mis-posed, and this note claims that and not more.\nper_mode: RESIDUE 3, THE MULTIPLICITY SELECTOR, NARROWED AND NOT DISSOLVED. ALL TWELVE COPIES were restricted, not one: at every time level t = 0..5 and both parity classes the k = 1 character restricts to beta|z|^2 with the antilinear residual EXACTLY ZERO in all twelve, so every copy is one complex slot in the SAME fork cell. THE COEFFICIENT IS LEVEL-INDEXED AND PARITY-INDEPENDENT WITH EXACTLY THREE VALUES -- 3193/2240 at t = 0 and 2, 43/35 at t = 1, and 1817/1120 at t = 3, 4 and 5 -- over level classes {0,2}, {1} and {3,4,5} which DO NOT COINCIDE with the pinned/free split {0,1} and {2,3,4,5}; the class structure is MEASURED and is NOT derived here. THE SOLVE'S DISSOLUTION CLAIM IS QUOTED AND REFUTED, CREDITED TO THE CROSS-MODEL CHECK: the rank-12 isotype Gram is NOT diagonal, with 36 nonzero off-diagonal entries and the (3,0) copy coupling to exactly five others, so these are not twelve factorized scalar cells; and DECISIVELY the flavor lane's own slot counter is ADDITIVE, r_from_slot_count(n) = n/2, so retaining all twelve holomorphic copies gives r = 6 and Q = (1+2r)/3 = 13/3 and NOT r = 1/2, Q = 2/3. THE ONE-COPY CHOICE IN THE LANDED EMBEDDING WAS LOAD-BEARING; Q = 2/3 FIRES FOR THE EXPLICIT ONE-COPY EMBEDDING; and A MULTIPLICITY SELECTOR, QUOTIENT OR FIBER THEOREM IS A NAMED OPEN REQUIREMENT.\nper_block: THE CARRIER MAP, EXHIBITED AT REPRESENTATION/METRIC-INSTANCE LEVEL AND NOT AT PHYSICAL SCOPE. On the natural orbit basis of the 3-element chart orbit {(0,0),(0,2),(0,4)} the committed U restricts to U_orb = [[0,0,1],[1,0,0],[0,1,0]] = P_3 EXACTLY with U_orb^3 = I and U E = E P_3, so U on the chart orbit IS the same 3-cycle permutation as the flavor lane's C_3 on the hw = 1 translation characters, basis-to-basis. The committed orbit restriction is R = E^T Q E = (3193/2240) I_3: circulant with coefficients (3193/2240, 0, 0), the same-level distance-2 couplings VANISHING on this carrier, J-COMPONENT EXACTLY ZERO, all three character eigenvalues equal, and EXACTLY an instance of M(alpha, beta) at the DEGENERATE point alpha = beta = 3193/2240 with det_R = alpha beta^2 = 32553430057/11239424000 EXACTLY. BUT BECAUSE R IS A SCALAR ITS METRIC-PRESERVATION LEG IS BASIS-VACUOUS, exhibited against the non-circulant witness X = e_0 e_1^T which commutes with R while the nondegenerate family member M(1,2) does not, so ONLY U_orb = P_3 CARRIES CONTENT. WHAT TRANSFERS, FOR ONE CHOSEN ORBIT COPY: the C_3 module, its R (+) C representation typing, and after choosing J the algebraic 2 real slots <-> 1 complex slot comparison -- THE COUNTING BIT TRANSFERS FOR ONE CHOSEN COPY. WHAT DOES NOT: any nontrivial alpha/beta metric ratio, hierarchy, a metric-selected J or orientation, uniqueness of the carrier, the full rank-12 count, record-write observables, or the hw >= 2 ambient sectors. IT IS AN EQUIVARIANT ONE-ORBIT MODULE MAP AND NOT A PHYSICAL OBSERVABLE-PRESERVING CARRIER MAP.\nlattice_wide: THE REMAINDER, SIX NAMED ITEMS. The solve itemized three; THE CROSS-MODEL CHECK FOUND THE LIST INCOMPLETE AND ADDED THREE MORE, AND ITS FINDING OVERRIDES THE SOLVE. (1) THE MULTIPLICITY SELECTOR OR FIBER THEOREM -- a selector, a quotient, or a theorem that the rank-12 chart multiplicity is external base-space degeneracy; copywise identical type does NOT reduce the total slot count to one; RESTORED AND LOAD-BEARING. (2) THE M_2(C) CARRIER-ALGEBRA EMBEDDING -- an injective unital *-map preserving products and adjoints, which identifying content-writes with shear pins does NOT supply; RESTORED. (3) NON-VACUOUS PHYSICAL OBSERVABLE PRESERVATION -- equality of two regular-representation 3-cycles plus preservation of a scalar metric proves MODULE EQUIVALENCE and not that the physical generators and observables coincide; the unclosed physical content of the advertised map. (4) THE RECORD-WRITE IDENTIFICATION -- their M_2(C) content-writes against our shear pins, untouched. (5) THE AMBIENT MISMATCH -- their hw >= 2 shell sectors have no chart-line counterpart, untouched. (6) THE METRIC-RATIO DEGENERACY -- our realization sits at the symmetric point alpha = beta, so THEIR r-SELECTION WALL IS NOT REACHED BY THIS INSTANCE and ONLY THE POLARIZATION/COUNTING BIT TRANSFERS. AND ONE STANDING DISCLOSURE OUTSIDE THE LEDGER: Q = (1+2r)/3 REMAINS THEIR IMPORTED AUTHORITY.\nper_scope: THE CAMPAIGN CLOSE, AS A STRUCTURAL VERDICT WITH NO MEASUREMENT OF ITS OWN. ONE COMMITTED STRUCTURE -- the action's complex unit i, its SESQUILINEAR-ONLY GRAMMAR with every field occurrence carrying one conjugated and one unconjugated leg, and the ANTIUNITARY REFLECTION Theta phi = r conj(phi) -- was measured across SEVEN BLOCKS OF THE LANDED CHAIN, 171, 174, 175, 176, 177, 178 and this one, and it supplied: THE BORN-SHAPED READOUT CANDIDATE within a FORK-INDEPENDENT FAMILY (176, 177, 178); THE CONDITIONAL SYMMETRIC-POWER THEOREM (177, #7331 -- every n >= 1 particle sector indefinite on EITHER kernel candidate, the vacuum window unique IN-FAMILY, the grading fork GENUINE); THE SHEAR-MIRROR THEOREM (178, #7336 -- shears break the mirror, volumes do not, the canonical reconstruction blocked at SHEAR SCOPE); TRANSPORT MEASURED AS A RECORD-CONSISTENCY RESPONSE (178, INTERPRETATION SCOPE); THE KOIDE COUNTING BIT SUPPLIED FOR THE EXPLICIT ONE-COPY EMBEDDING WITH Q = 2/3 EXACT (176, #7330, and this block's residue ledger, with the one-copy scoping part of the supply); and THE CROSS-LANE PINCER (the pincer identity #7318; the sister lane's #7325 countermodel CLOSING THE AXIOMS-ONLY SELECTION ROUTE and leaving the action-native supply route live). THE HONEST LIMITS: THERE IS NO UNIQUE READOUT DERIVATION and a READOUT AXIOM WOULD BE NEEDED, NEVER PROPOSED HERE; the sector identification is A GENUINE FORK; THE FULL FLAVOR BRIDGE NEEDS THE SIX-ITEM REMAINDER; and NOTHING IS REGISTERED OR ADOPTED. THE ITEMS AT THE OWNER'S BAR ARE LISTED: the counting-bit supply; the reflection-pairing readout principle; and the drawer items from the prior campaign -- the bridge axiom in the drawer, the design fork, the b141/b142 items and e_x = -1.\nRESULT: THE EMBEDDING RESIDUES AND THE CAMPAIGN CLOSE. RESIDUE 4 IS DISSOLVED TRIVIALLY, the orientation equality FORCED and not new selector content. RESIDUE 3 IS NARROWED AND NOT DISSOLVED: every copy is one complex slot in the same cell, the coefficient is level-indexed over three exact values, but raw fork counting over the rank-12 eigenspace gives r = 6 and Q = 13/3, so Q = 2/3 FIRES FOR THE EXPLICIT ONE-COPY EMBEDDING and a SELECTOR OR FIBER THEOREM IS A NAMED OPEN REQUIREMENT. THE CARRIER MAP IS EXHIBITED AT REPRESENTATION/METRIC-INSTANCE LEVEL, the metric leg BASIS-VACUOUS at the degenerate point, an EQUIVARIANT ONE-ORBIT MODULE MAP and NOT a physical observable-preserving carrier map. THE REMAINDER IS SIX NAMED ITEMS and the campaign closes with all six open. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\nDECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is edited; no earlier block is corrected; the bar items stay PROPOSALS, and PROPOSALS STAY PROPOSALS. THE CORRECTIONS LEDGER FOR THE WHOLE CAMPAIGN IS CARRIED IN THREE GROUPS AS THE VERIFICATION STRUCTURE'S PRODUCT: FIVE SUPERVISOR CUT HYPOTHESES -- the wrap hypothesis, the pin hypothesis, the geometry-free slogan, the forced-fork/uniqueness claim and, THIS ROUND, THE MULTIPLICITY-DISSOLUTION CLAIM; THE CHECKERS' DISCOVERIES -- the object mismatch with witness -35233/38760 making the symmetric-power theorem CONDITIONAL, r^2 -> |r|^2, the witness v = e_0 - 5 e_4 with v^dag G v = -57/160, sector-uniqueness not readout-uniqueness, the convention r Q r = Q^T, the volume counterexample (1,2,3,4)_x, the full hop censuses, the 24-entry accounting, the rational-continuity proof, and THIS ROUND the forced-orientation adjudication, the multiplicity refutation and the six-item remainder; and THE DRAFT WORKERS' CATCHES -- the herm-det dial-blindness catch of Block 178 and, THIS ROUND, THE THREE-VALUED LEVEL LEDGER with 43/35 at t = 1 that the campaign record's two-value phrasing omitted. THE CHECKER IS CREDITED and ITS FINDINGS OVERRIDE THE SOLVE EVERYWHERE THEY COLLIDE. THIS BLOCK'S OWN DEFECTS ARE DISCLOSED: it is ONE FIXTURE with no ladder; only one residue is dissolved and it is dissolved trivially; the multiplicity dissolution is WITHDRAWN; the carrier map is representation-level; Q = (1+2r)/3 remains IMPORTED AUTHORITY; the campaign-close section introduces no measurement of its own; and the AST surface is this runner plus the imported runner chain and NOT every landed module the chain reaches, with residual sites counted rather than claimed repaired. PROVENANCE: CAMPAIGN_20260823_COMPLEX_STRUCTURE.md sections B4 PARTIAL and B4 CARRIER-MAP RESIDUE, with b179_embed_findings.md, b179_embed_probe.py and b179res_check_findings.md preserved in generator-program-20260821/. HANDOFF: supply the multiplicity selector or fiber theorem; supply the M_2(C) algebra embedding; supply a non-vacuous observable-preservation bridge.\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero."


def build_claims(mutation: str) -> dict:
    claims: dict = {
        "main_head": CURRENT_MAIN,
        "parent_pin": "resolved",
        "objects_registered": False,
        "beta_restriction": BETA,
        "orientation_selector_needed": False,
        "multiplicity_dissolved": False,
        "q_two_thirds_unconditional": False,
        "carrier_map_physical": False,
        "det_r": DET_R,
        "full_flavor_bridge": False,
        "ratio_wall_reached": False,
        "readout_derived": False,
        "required_close_keys": CLOSE_KEYS,
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
    elif mutation == "break_beta_restriction":
        # THE RESTRICTION BROKEN: a wrong coefficient asserted, which the exact
        # (3193/2240)|z|^2 restriction forbids.
        claims["beta_restriction"] = sp.cancel(BETA + R(1, 10 ** 6))
    elif mutation == "claim_orientation_selector_needed":
        # RESIDUE 4 REASSERTED: an orientation selector asserted NEEDED, which
        # the two exactly equal restrictions forbid.
        claims["orientation_selector_needed"] = True
    elif mutation == "claim_multiplicity_dissolved":
        # THE REFUTED CLAIM REASSERTED: residue 3 asserted DISSOLVED, which the
        # additive slot counter's r = 6, Q = 13/3 counter-exhibit forbids.
        claims["multiplicity_dissolved"] = True
    elif mutation == "claim_q_two_thirds_unconditional":
        # THE SCOPING DROPPED: Q = 2/3 asserted to hold over the FULL rank-12
        # eigenspace, which the arbiter's own additive count forbids.
        claims["q_two_thirds_unconditional"] = True
    elif mutation == "claim_carrier_map_physical":
        # THE WEAKENED CLAIM RE-STRENGTHENED: the metric leg asserted to carry
        # content, which the measured SCALAR orbit block forbids.
        claims["carrier_map_physical"] = True
    elif mutation == "break_det_r":
        # THE FAMILY DETERMINANT BROKEN: a wrong exact rational asserted, which
        # the recomputed orbit restriction forbids.
        claims["det_r"] = sp.cancel(DET_R + R(1, 10 ** 6))
    elif mutation == "claim_full_flavor_bridge":
        # THE BRIDGE ASSERTED COMPLETE, which six open remainder items forbid.
        claims["full_flavor_bridge"] = True
    elif mutation == "claim_ratio_wall_reached":
        # THE RATIO WALL ASSERTED REACHED, which alpha = beta forbids.
        claims["ratio_wall_reached"] = True
    elif mutation == "claim_readout_derived":
        # THE READOUT ASSERTED DERIVED, which the campaign's own withdrawal and
        # this block's declared status flag forbid.
        claims["readout_derived"] = True
    elif mutation == "drop_owner_bar_list":
        claims["required_close_keys"] = tuple(
            key for key in CLOSE_KEYS if key != "owner_bar_list")
    elif mutation == "drop_corrections_ledger":
        claims["required_close_keys"] = tuple(
            key for key in CLOSE_KEYS if key != "corrections_ledger")
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
    fixture: dict
    orientation: dict
    multiplicity: dict
    carrier: dict
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
        AUDIT_INPUT_PATHS == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_EMBEDDING_RESIDUES_CAMPAIGN_CLOSE_BOUNDED_THEOREM_NOTE_2026-08-23.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_SHEAR_MIRROR_INTERFERENCE_BOUNDED_THEOREM_NOTE_2026-08-23.md",
            "docs/KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md",
            "scripts/admissibility_dirac_kahler_shear_mirror_interference_2026_08_23.py",
            "scripts/admissibility_dirac_kahler_complex_structure_synthesis_2026_08_23.py",
            "scripts/admissibility_dirac_kahler_generator_trilemma_kernel_2026_08_21.py",
            "scripts/admissibility_dirac_kahler_closure_audit_two_2026_08_21.py",
        )
        # THE FLAVOR RUNNER IS DELIBERATELY ABSENT: it is read from origin/main
        # through the landed Block 176 loader and never from the worktree.
        and FLAVOR_RUNNER not in AUDIT_INPUT_PATHS
        and PARENT_ARTIFACTS == (BLOCK178_NOTE, BLOCK178_RUNNER)
        and len(PARENT_ARTIFACT_BLOBS) == len(PARENT_ARTIFACTS) == 2
        and facts.main_head == claims["main_head"]
        and authority.fixed_authority
        and authority.parent_import_landed
        and authority.parent_pin_is_commit
        and authority.parent_ref_and_ancestry
        and parent_blobs_ok
        # THE STALE PIN: a REAL ancestor of HEAD that carries NEITHER Block 178
        # artifact, which is exactly what makes the stale mutation bite.
        and authority.stale_is_real_ancestor
        and authority.stale_carries_neither_artifact)

    ban = facts.banners
    fix = facts.fixture
    ori = facts.orientation
    gate_b = bool(
        # THE CONVENTION COLLISION, MEASURED on identical matrices.
        ban["convention"]["pairs"] == EXPECTED_CONVENTION
        and ban["convention"]["landed_psd"] and ban["convention"]["here_psd"]
        and ban["convention"]["orders_differ"]
        # THE IMPOSED-OBJECT BANNER and THE PROPOSALS, as measured objects.
        and ban["imposed_objects"] == 7
        and ban["registered_objects"] == 0
        and ban["adopted_objects"] == 0
        and ban["owner_bar_items"] == 3
        and ban["owner_decisions"] == 1
        and ban["supervisor_corrections"] == 5
        and ban["checker_discoveries"] == 3
        and ban["draft_worker_catches"] == 2
        and ban["remainder_items"] == 6
        and (ban["registered_objects"] == 0 and ban["adopted_objects"] == 0)
        == (not claims["objects_registered"])
        # THE 12x6 FIXTURE, rebuilt through the LANDED chain and never imported
        # from any scratchpad module.
        and fix["N"] == FIXTURE_N and fix["T_phys"] == PHYS_T
        and fix["lx"] == LX and fix["c"] == REGION_PIN
        and fix["pinned"] == PINNED_LEVELS and fix["free"] == FREE_LEVELS
        and fix["symbol_free"]
        and fix["inertia"] == (FIXTURE_N, 0, 0)
        and fix["carrier_sigma"] == R(3, 5) and fix["volume"] == CONST_VOLUME
        and fix["omega_primitive"]
        and fix["U_order_three"] and fix["U_unitary"] and fix["U_commutes"]
        and fix["projector_traces"] == (sp.Integer(12),) * 3
        and fix["projectors_resolve"]
        # THE RESTRICTION ITSELF, which is what the beta mutation bites on.
        and ori["beta_one"] == claims["beta_restriction"]
        and ori["typing_one"]
        and ori["induced_metric_one"]
        and facts.exact_no_float
        and facts.source_floats == 0 and facts.source_forbidden == 0
        and facts.source_files >= 2)

    gate_c = bool(
        # THE CONJUGATE PAIR AND ITS TWO EIGENVALUE IDENTITIES.
        ori["conjugate_pair"] and ori["f_one_eigen"] and ori["f_two_eigen"]
        and ori["f_one_unit"] and ori["f_two_unit"]
        # BOTH ORIENTATIONS, EXACTLY EQUAL, AT THE LITERAL VALUE.
        and ori["beta_one"] == BETA and ori["beta_two"] == BETA
        and ori["beta_one"] == ori["beta_two"]
        # BOTH ANTILINEAR RESIDUALS EXACTLY ZERO -- one complex slot each.
        and ori["antilinear_one"] == 0 and ori["antilinear_two"] == 0
        and ori["typing_one"] and ori["typing_two"]
        # THE ADJUDICATION, CARRIED AS NOTE TEXT: forced, not contentful.
        and facts.scope["orientation_forced_not_contentful"]
        and facts.scope["algebraic_tautology"]
        and facts.scope["no_selector_needed"]
        and facts.scope["orientation_residue_quoted"]
        # THE CLAIM-BOUND LEG: the two orientations do NOT differ.
        and ori["orientations_differ"] == claims["orientation_selector_needed"]
        and facts.exact_no_float)

    mul = facts.multiplicity
    car = facts.carrier
    gate_d = bool(
        # THE TWELVE-COPY LEDGER, EXACT AND COMPLETE.
        mul["copy_count"] == COPY_COUNT
        and mul["level_values"] == LEVEL_LEDGER
        and mul["distinct_values"] == DISTINCT_LEVEL_VALUES
        and mul["level_classes"] == LEVEL_CLASSES
        and not mul["classes_match_pin_split"]
        and mul["parity_independent"]
        and mul["antilinear_all_zero"]
        and mul["typing_all_hold"]
        and mul["copies_orthonormal"]
        # THE TYPED COPY at t = 3, spelled out rather than inferred.
        and mul["typed_copy_beta"] == TYPED_COPY_BETA
        and mul["typed_copy_antilinear"] == 0
        and mul["typed_copy_typing"]
        # THE FIRST REFUTATION LEG: the rank-12 Gram is NOT diagonal.
        and not mul["gram_is_diagonal"]
        and mul["gram_offdiagonal_nonzeros"] == GRAM_OFFDIAGONAL_NONZEROS
        and mul["coupled_partners"] == COUPLED_PARTNERS
        # THE DECISIVE LEG: the flavor lane's OWN additive counter.
        and mul["arbiter_loaded"]
        and mul["one_copy_r"] == ONE_COPY_R and mul["one_copy_q"] == ONE_COPY_Q
        and mul["all_copy_r"] == ALL_COPY_R and mul["all_copy_q"] == ALL_COPY_Q
        and mul["all_copy_q"] != mul["one_copy_q"]
        # THE SCOPING, GATED AS NOTE TEXT.
        and facts.scope["multiplicity_residue_quoted"]
        and facts.scope["dissolution_refuted"]
        and facts.scope["gram_not_diagonal"]
        and facts.scope["additive_slot_counter"]
        and facts.scope["raw_count_thirteen_thirds"]
        and facts.scope["one_copy_load_bearing"]
        and facts.scope["one_copy_scoping"]
        and facts.scope["named_open_requirement"]
        and facts.scope["level_indexed"]
        and facts.scope["classes_not_pin_split"]
        # THE TWO CLAIM-BOUND LEGS.  Both measured flags are FALSE.
        and mul["multiplicity_is_dissolved"] == claims["multiplicity_dissolved"]
        and mul["q_is_unconditional"] == claims["q_two_thirds_unconditional"]
        and (mul["deep_ledger_agrees"] is True if facts.deep else True)
        and facts.exact_no_float)

    gate_e = bool(
        # THE EQUIVARIANCE, EXACT AND BASIS-TO-BASIS.
        car["U_orb_is_three_cycle"] and car["orbit_preserved"]
        and car["U_orb_order_three"]
        # THE CIRCULANT / ISOTYPE DECOMPOSITION, with the J-component ZERO and
        # ALL THREE EIGENVALUES EQUAL.
        and car["is_symmetric"] and car["is_circulant"]
        and car["distance_two_couplings_vanish"]
        and car["j_component"] == 0
        and car["all_eigenvalues_equal"]
        and car["alpha"] == BETA and car["beta"] == BETA
        and car["is_degenerate"]
        # THE M(alpha, beta) INSTANCE IDENTITY AND ITS DETERMINANT LAW.
        and car["is_family_instance"]
        and car["det_matches_family_law"]
        and car["det_r"] == claims["det_r"]
        # THE BASIS-VACUITY WITNESS: the scalar commutes with a NON-circulant
        # matrix while a NONDEGENERATE family member does not.
        and car["restriction_is_scalar"]
        and car["scalar_commutes_with_witness"]
        and car["nondegenerate_fails_witness"]
        and car["centralizer_is_everything"]
        # THE SCOPED STATEMENTS, gated as note text.
        and facts.scope["carrier_residue_quoted"]
        and facts.scope["equivariance_exact"]
        and facts.scope["basis_to_basis"]
        and facts.scope["circulant_j_zero"]
        and facts.scope["degenerate_point"]
        and facts.scope["fork_family_instance"]
        and facts.scope["det_r_literal"]
        and facts.scope["metric_leg_basis_vacuous"]
        and facts.scope["one_orbit_module_map"]
        and facts.scope["counting_bit_transfers_one_copy"]
        and facts.scope["what_does_not_transfer"]
        # THE CLAIM-BOUND LEG: the metric leg carries NO content.
        and car["metric_leg_has_content"] == claims["carrier_map_physical"]
        and facts.exact_no_float)

    gate_f = bool(
        # SIX ITEMS, DECLARED AND KEYED.
        ban["remainder_items"] == 6
        and len(REMAINDER_ITEMS) == 6
        and facts.scope["remainder_ledger"]
        and facts.scope["remainder_multiplicity_theorem"]
        and facts.scope["remainder_algebra_embedding"]
        and facts.scope["remainder_observable_preservation"]
        and facts.scope["remainder_record_writes"]
        and facts.scope["remainder_ambient"]
        and facts.scope["remainder_ratio_degeneracy"]
        # THE DEGENERACY STATEMENT AND THE UNREACHED WALL.
        and facts.scope["ratio_wall_not_reached"]
        and facts.scope["only_polarization_transfers"]
        and facts.scope["imported_authority"]
        and car["is_degenerate"]
        # THE TWO CLAIM-BOUND LEGS.  Both measured flags are FALSE.
        and ban["bridge_is_complete"] == claims["full_flavor_bridge"]
        and car["ratio_wall_reached"] == claims["ratio_wall_reached"]
        and facts.exact_no_float)

    close_keys = tuple(claims["required_close_keys"])
    gate_g = bool(
        # THE CAMPAIGN-CLOSE SECTION, as declared literals rather than prose.
        ban["landed_block_citations"] == len(LANDED_BLOCK_CITATIONS) == 7
        and ban["supervisor_corrections"] == 5
        and ban["checker_discoveries"] == 3
        and ban["draft_worker_catches"] == 2
        and ban["owner_bar_items"] == 3
        # EVERY CITED BLOCK AND PR PRESENT IN THE NOTE.
        and all(facts.scope[key] for key in
                ("parent_block", "parent_pr", "grandparent_pr", "synthesis_pr",
                 "pincer_pr", "sister_lane_cited", "block174_cited"))
        # THE REQUIRED CLOSE KEYS ARE THE FULL SET, which is what gives the two
        # drop mutations their teeth.
        and close_keys == CLOSE_KEYS
        and all(facts.scope[key] for key in close_keys)
        and set(CLOSE_KEYS) <= set(SCOPE_KEYS)
        and facts.scope["checker_overrides"]
        and facts.scope["codex_refute_check"]
        and facts.scope["checker_credited"]
        and facts.scope["process_working"]
        and facts.scope["level_ledger_catch"]
        and facts.scope["herm_det_catch"]
        # THE CLAIM-BOUND LEG: the readout is NOT derived anywhere.
        and ban["readout_is_derived"] == claims["readout_derived"]
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
def measure(deep: bool) -> Facts:
    note_text, at_final_path = raw_note()
    main_head = resolve_ref("origin/main")
    scope = scope_certificate(note_text)
    fixture = measure_fixture()
    orientation = measure_orientation(fixture)
    multiplicity = measure_multiplicity(fixture, deep)
    carrier = measure_carrier(fixture)
    banners = {
        "convention": b176.measure_convention() if b176 is not None else {},
        "imposed_objects": len(IMPOSED_OBJECTS),
        "registered_objects": len(REGISTERED_OBJECTS),
        "adopted_objects": len(ADOPTED_OBJECTS),
        "owner_bar_items": len(OWNER_BAR_ITEMS),
        "owner_decisions": len(OWNER_DECISIONS),
        "remainder_items": len(REMAINDER_ITEMS),
        "supervisor_corrections": len(SUPERVISOR_CORRECTIONS),
        "checker_discoveries": len(CHECKER_DISCOVERIES),
        "draft_worker_catches": len(DRAFT_WORKER_CATCHES),
        "landed_block_citations": len(LANDED_BLOCK_CITATIONS),
        # THE TWO DECLARED STATUS FLAGS, so the mutations bite on a declared
        # object and not on prose.  Both are FALSE and both are the point.
        "readout_is_derived": False,
        "bridge_is_complete": False,
    }
    record(fixture["N"])
    record(fixture["T_phys"])
    for value in fixture["inertia"]:
        record(value)
    for value in fixture["projector_traces"]:
        record(value)
    record(orientation["beta_one"])
    record(orientation["beta_two"])
    record(orientation["antilinear_one"])
    record(orientation["antilinear_two"])
    for value in multiplicity["level_values"].values():
        record(value)
    record(multiplicity["gram_offdiagonal_nonzeros"])
    record(multiplicity["typed_copy_beta"])
    for key in ("one_copy_r", "one_copy_q", "all_copy_r", "all_copy_q"):
        if multiplicity[key] is not None:
            record(multiplicity[key])
    record(carrier["alpha"])
    record(carrier["beta"])
    record(carrier["j_component"])
    record(carrier["det_r"])
    for value in carrier["circulant_coefficients"]:
        record(value)
    return Facts(
        deep=deep,
        main_head=main_head,
        authority=authority_certificate(main_head),
        note_at_final_path=at_final_path,
        scope=scope,
        banners=banners,
        fixture=fixture,
        orientation=orientation,
        multiplicity=multiplicity,
        carrier=carrier,
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
        help="also restrict the k = 2 character at EVERY copy and re-derive "
             "the level ledger from the conjugate orientation; the runtime "
             "budget is lengthened")
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
    fix, ori = facts.fixture, facts.orientation
    mul, car = facts.multiplicity, facts.carrier
    res = facts.authority.residue

    print("MEASURED, before any gate is read:")
    print(f"  PARENT IMPORT: the Block 178 runner imported "
          f"{facts.authority.parent_import_landed}; PARENT_COMMIT "
          f"{PARENT_COMMIT} is REAL and PARENT_REF resolves to it. "
          f"CURRENT_MAIN was RE-RESOLVED at draft time to {CURRENT_MAIN}. "
          f"NOTHING from the scratchpad is imported: the 12x6 fixture below is "
          f"the Block 174 Width(6,'const') construction REBUILT from its LANDED "
          f"ingredients")
    print(f"  THE STALE PIN: {STALE_PARENT_COMMIT[:12]} is a REAL ancestor of "
          f"HEAD {facts.authority.stale_is_real_ancestor} and carries NEITHER "
          f"Block 178 artifact {facts.authority.stale_carries_neither_artifact}"
          f" -- it is the Block 177 tip, which PREDATES both artifacts, and "
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
          f"and FULLY HYPERBOLIC here")
    print(f"  THE IMPOSED-OBJECT BANNER AND THE PROPOSALS: "
          f"{record(ban['imposed_objects'])} objects built by this block or its "
          f"parents, {record(ban['registered_objects'])} registered and "
          f"{record(ban['adopted_objects'])} adopted; "
          f"{record(ban['owner_bar_items'])} items sit at THE OWNER'S BAR AS "
          f"PROPOSALS -- {OWNER_BAR_ITEMS} -- and "
          f"{record(ban['owner_decisions'])} decision belongs to the OWNER: "
          f"{OWNER_DECISIONS}. The imposed objects are {IMPOSED_OBJECTS}")
    print(f"  THE FIXTURE, rebuilt from LANDED modules: 12x6 constant carrier, "
          f"N = {record(fix['N'])}, T_phys = {record(fix['T_phys'])}, L_x = "
          f"{fix['lx']}, region pin c = {fix['c']}, pinned levels "
          f"{fix['pinned']} at zero shear and free levels {fix['free']} at "
          f"CARRIER_SIGMA = {fix['carrier_sigma']}, constant volume "
          f"{fix['volume']}; Q is SYMBOL-FREE {fix['symbol_free']} with "
          f"inertia(herm Q) = {fix['inertia']}(n+,n-,n0)[b165]. THE CHART "
          f"STRUCTURE: omega is an exact primitive cube root "
          f"{fix['omega_primitive']} over the DISCLOSED field Q(sqrt(-3)), U is "
          f"unitary {fix['U_unitary']} of exact order three "
          f"{fix['U_order_three']}, [Q,U] = 0 EXACTLY {fix['U_commutes']}, and "
          f"the three cyclotomic projectors have exact traces "
          f"{fix['projector_traces']} and resolve the identity "
          f"{fix['projectors_resolve']}")
    print(f"  RESIDUE 4, THE ORIENTATION: f_2 = conj(f_1) EXACTLY "
          f"{ori['conjugate_pair']}, both unit-norm eigenvectors of U at omega "
          f"and omega^2 {(ori['f_one_eigen'], ori['f_two_eigen'])}, and the two "
          f"restrictions are IDENTICAL: f_1^dag Q f_1 = "
          f"{record(ori['beta_one'])} and f_2^dag Q f_2 = "
          f"{record(ori['beta_two'])}, with antilinear residuals "
          f"{record(ori['antilinear_one'])} and "
          f"{record(ori['antilinear_two'])} -- so each orientation is "
          f"beta|z|^2 with NO z^2 term {(ori['typing_one'], ori['typing_two'])} "
          f"and the induced real metric is diag(beta, beta) "
          f"{ori['induced_metric_one']}. THE ORIENTATIONS DO NOT DIFFER "
          f"{ori['orientations_differ']}, so NO SELECTOR IS NEEDED -- AND THE "
          f"CHECK ADJUDICATED THAT EQUALITY FORCED, an algebraic tautology "
          f"after the real-symmetric restriction, NOT new selector content")
    print(f"  RESIDUE 3, THE LEDGER: all {record(mul['copy_count'])} copies "
          f"restricted, not one. The level values are {mul['level_values']} -- "
          f"{record(mul['distinct_values'])} DISTINCT VALUES over the level "
          f"classes {mul['level_classes']}, PARITY-INDEPENDENT "
          f"{mul['parity_independent']}, and those classes DO NOT coincide with "
          f"the pinned/free split {mul['classes_match_pin_split']}. Every "
          f"antilinear residual is exactly zero {mul['antilinear_all_zero']} "
          f"and every copy types as beta|z|^2 {mul['typing_all_hold']}; the "
          f"t = 3 copy is spelled out at beta = {record(mul['typed_copy_beta'])}"
          f" with residual {mul['typed_copy_antilinear']}")
    print(f"  AND THE DISSOLUTION CLAIM IS REFUTED, ON TWO MEASURED LEGS. "
          f"FIRST, the rank-12 isotype Gram is NOT diagonal "
          f"{not mul['gram_is_diagonal']}: it has "
          f"{record(mul['gram_offdiagonal_nonzeros'])} nonzero off-diagonal "
          f"entries and the {COUPLED_COPY} copy couples to exactly "
          f"{len(mul['coupled_partners'])} others, {mul['coupled_partners']} -- "
          f"so these are NOT twelve factorized scalar cells. SECOND AND "
          f"DECISIVELY, the flavor lane's OWN counter is ADDITIVE: at its "
          f"pinned blob {mul['arbiter_blob'][:12]} loaded through the landed "
          f"Block 176 loader {mul['arbiter_loaded']}, ONE copy gives r = "
          f"{record(mul['one_copy_r'])} and Q = {record(mul['one_copy_q'])} "
          f"while ALL TWELVE give r = {record(mul['all_copy_r'])} and Q = "
          f"{record(mul['all_copy_q'])}. MEASURED dissolved = "
          f"{mul['multiplicity_is_dissolved']} and MEASURED unconditional = "
          f"{mul['q_is_unconditional']}: Q = 2/3 FIRES FOR THE EXPLICIT "
          f"ONE-COPY EMBEDDING and a SELECTOR OR FIBER THEOREM IS A NAMED OPEN "
          f"REQUIREMENT")
    print(f"  THE CARRIER MAP: on the natural orbit basis U restricts to "
          f"{car['U_orbit'].tolist()} == P_3 {car['U_orb_is_three_cycle']}, of "
          f"exact order three {car['U_orb_order_three']}, and the orbit is "
          f"preserved {car['orbit_preserved']} -- the SAME 3-cycle as their "
          f"C_3, BASIS-TO-BASIS. The orbit restriction is "
          f"{car['restriction'].tolist()}: circulant {car['is_circulant']} with "
          f"coefficients {car['circulant_coefficients']}, the same-level "
          f"distance-2 couplings VANISHING "
          f"{car['distance_two_couplings_vanish']}, J-COMPONENT "
          f"{record(car['j_component'])}, all three eigenvalues equal "
          f"{car['all_eigenvalues_equal']} at {car['eigenvalues']}, an EXACT "
          f"instance of M(alpha, beta) {car['is_family_instance']} at the "
          f"DEGENERATE point alpha = {record(car['alpha'])} = beta = "
          f"{record(car['beta'])} {car['is_degenerate']}, with det_R = "
          f"{record(car['det_r'])} matching alpha beta^2 "
          f"{car['det_matches_family_law']}")
    print(f"  AND THE METRIC LEG IS BASIS-VACUOUS, EXHIBITED: the restriction "
          f"is a SCALAR {car['restriction_is_scalar']}, so it commutes with the "
          f"NON-circulant witness e_0 e_1^T "
          f"{car['scalar_commutes_with_witness']} and indeed with the WHOLE "
          f"3x3 algebra {car['centralizer_is_everything']}, while the "
          f"NONDEGENERATE family member M(1,2) does NOT "
          f"{car['nondegenerate_fails_witness']}. So the metric-preservation "
          f"leg carries NO content {car['metric_leg_has_content']}, only "
          f"U_orb = P_3 does, and THEIR r-SELECTION WALL IS NOT REACHED "
          f"{car['ratio_wall_reached']} -- what is exhibited is AN EQUIVARIANT "
          f"ONE-ORBIT MODULE MAP AND NOT A PHYSICAL OBSERVABLE-PRESERVING "
          f"CARRIER MAP")
    print(f"  THE REMAINDER: {record(ban['remainder_items'])} NAMED ITEMS, "
          f"three restored or supplied by the check and three from the solve, "
          f"ALL OPEN -- {REMAINDER_ITEMS}. Declared bridge complete = "
          f"{ban['bridge_is_complete']}")
    print(f"  THE CAMPAIGN CLOSE: ONE COMMITTED STRUCTURE measured across "
          f"{record(ban['landed_block_citations'])} BLOCKS OF THE LANDED CHAIN "
          f"{LANDED_BLOCK_CITATIONS}, with the campaign PRs {CAMPAIGN_PRS}. "
          f"Declared readout derived = {ban['readout_is_derived']}")
    print(f"  THE CORRECTIONS LEDGER: {record(ban['supervisor_corrections'])} "
          f"SUPERVISOR CUT HYPOTHESES -- {SUPERVISOR_CORRECTIONS} -- "
          f"{record(ban['checker_discoveries'])} GROUPS OF CHECKER DISCOVERIES "
          f"-- {CHECKER_DISCOVERIES} -- and "
          f"{record(ban['draft_worker_catches'])} DRAFT-WORKER CATCHES -- "
          f"{DRAFT_WORKER_CATCHES}. ALL OF THEM ARE DISCLOSED AS THE PROCESS "
          f"WORKING")
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
    print(f"  SAMPLING: --deep {facts.deep}; at baseline every one of the "
          f"twelve k = 1 copies is restricted and typed exactly and the whole "
          f"rank-12 Gram is built, so there is no sampling in the ledger; "
          f"--deep additionally re-derives the ledger from the CONJUGATE k = 2 "
          f"orientation. DEEP LEDGER {mul['deep_ledger']}; agreement "
          f"{mul['deep_ledger_agrees']} -- None and {{}} mean the leg was NOT "
          f"RUN at this invocation, which is DISCLOSED rather than reported as "
          f"agreement")
    print()

    checks = Checks()
    checks.check(
        "A-authority-and-THE-STALE-PIN-THAT-PREDATES-BOTH-ARTIFACTS",
        "main plus the TWO Block 178 artifacts content-bound -- its note and its runner, which are BOTH the stack parent this block's branch is cut from AND the content parent, since this runner IMPORTS the Block 178 runner and reaches the whole committed chain through Block 178's own import chain, which Block 178's gate A pins rather than this one duplicating it -- and the gate additionally requires that the Block 178 runner ACTUALLY IMPORTED, because the 12x6 fixture below is built by the LANDED Block 170 Bench and the LANDED Block 166 carrier substitution reached through it and by NOTHING from any scratchpad module. PARENT_COMMIT IS REAL AND SO ARE BOTH ARTIFACT BLOBS: Block 178 HAS landed, so nothing needs sed at landing, and CURRENT_MAIN was re-resolved at draft time. THE FIVE-PIN AUTHORITY BLOCK binds origin/main's head, the axioms blob and the registry blob at origin/main, and the axioms and registry blobs in the worktree. THE STALE PIN IS THE BLOCK 177 TIP, a REAL ancestor of HEAD that PREDATES Block 178 and therefore carries NEITHER Block 178 artifact, which is exactly what makes the stale_parent_authority mutation bite -- under it the gate looks for the artifact blobs at a commit where they do not exist. THE FLAVOR RUNNER IS DELIBERATELY ABSENT FROM AUDIT_INPUT_PATHS, because it is read from origin/main through the landed Block 176 loader and never from the worktree, and THE HYGIENE RESIDUE BELOW THE AUDIT SURFACE IS COUNTED AND REPORTED AND NEVER CLAIMED REPAIRED, as (text mentions, LIVE CALL SITES) per module",
        gate_values["A"])
    checks.check(
        "B-the-two-banners-THE-PROPOSAL-RESTATED-and-the-12x6-fixture-rebuilt-from-LANDED-modules",
        "THE TWO BANNERS COME BEFORE ANY NUMERAL AND BOTH ARE MEASURED RATHER THAN ASSERTED. THE INERTIA CONVENTION: called on IDENTICAL matrices, b163/b164's congruence_inertia returns (n_+, n_0, n_-) and Block 165's real_symmetric_inertia returns (n_+, n_-, n_0), so the region normal form reads (4,4,0) there and (4,0,4) here; NEITHER HELPER IS WRONG and no landed verdict changes, but THE LITERAL STRING (4,4,0) MEANS PSD IN BLOCK 164'S LANDED FENCE AND FULLY HYPERBOLIC IN THIS NOTE -- and this block's own triple, inertia(herm Q) = (36,0,0), is positive definite under either reading and is stated anyway. THE IMPOSED-OBJECT BANNER: seven objects are imposed by this block or its parents -- the 12x6 constant-carrier fixture, the chart translation with its cyclotomic projectors over the disclosed field, the chart-momentum characters at every level and parity, the 3-element orbit with its embedding and restriction, the flavor lane's fork-input family read from landed authority, the basis-vacuity witness and its nondegenerate control, and the inherited reflection, region pin, slice index set, class map, slot order and record-slice scope -- and ZERO of them are registered and ZERO adopted, while THREE ITEMS SIT AT THE OWNER'S BAR AS PROPOSALS, the counting-bit supply first among them. AND THE FIXTURE IS REBUILT FROM LANDED MODULES AND MEASURED: the quotient action is 36x36 at T_phys = 6 and L_x = 6 with region pin c = 1, pinned levels (0,1) at zero shear and free levels (2,3,4,5) at CARRIER_SIGMA = 3/5, constant volume 7/5, Q symbol-free, inertia (36,0,0), omega an exact primitive cube root over the DISCLOSED field Q(sqrt(-3)), U unitary of exact order three commuting with Q entry for entry, and three cyclotomic projectors of exact trace 12 resolving the identity. THE RESTRICTION ITSELF IS GATED HERE: phi^dag Q phi = (3193/2240)|z|^2 exactly, with the induced real metric diag(3193/2240, 3193/2240), and asserting a different coefficient fails this gate. No float enters any measured object and the AST scan covers every file this runner reads code from in the runner chain",
        gate_values["B"])
    checks.check(
        "C-RESIDUE-4-DISSOLVED-TRIVIALLY-with-THE-FORCED-NOT-CONTENTFUL-ADJUDICATION-CARRIED",
        "THE TWO ORIENTATIONS ARE MEASURED SIDE BY SIDE AND THEY ARE IDENTICAL. At the committed fixture the chart-momentum characters at (t,p) = (0,0) are exact unit-norm eigenvectors of U at omega and omega^2 with f_2 = conj(f_1) EXACTLY, and their committed restrictions are f_1^dag Q f_1 = f_2^dag Q f_2 = 3193/2240 -- the same exact rational, not two rationals that happen to agree to some precision, since no precision is involved anywhere. BOTH ANTILINEAR RESIDUALS ARE EXACTLY ZERO, f_1^T Q f_1 = f_2^T Q f_2 = 0, so each orientation restricts to (3193/2240)|z|^2 with NO z^2 and NO conj(z)^2 term, and the symbolic typing phi = (x + iy) f returns beta(x^2 + y^2) exactly in both. THE FORK'S INPUT IS LITERALLY THE SAME OBJECT EITHER WAY and NO SELECTOR IS NEEDED, so residue 4 is dissolved. AND THE GATE REQUIRES THE NOTE TO SAY WHAT KIND OF DISSOLUTION THAT IS, because the cross-model check adjudicated it: since f_2 = conj(f_1), any real-symmetric orbit block gives the conjugate pair equal real Rayleigh quotients, and the measured orbit block is stronger still -- a real SCALAR -- so the equality is AN ALGEBRAIC TAUTOLOGY AFTER THE REAL-SYMMETRIC RESTRICTION and NOT NEW SELECTOR CONTENT. The residue is dissolved because it was mis-posed, the note is required to carry that adjudication verbatim-keyed, and asserting that a selector is needed fails this gate against two exactly equal measured rationals",
        gate_values["C"])
    checks.check(
        "D-RESIDUE-3-NARROWED-NOT-DISSOLVED-the-THREE-VALUED-LEDGER-and-THE-ADDITIVE-COUNTER-EXHIBIT",
        "ALL TWELVE COPIES WERE RESTRICTED, NOT ONE, AND THE LEDGER IS GATED IN FULL. At every time level and both parity classes the k = 1 character restricts to beta|z|^2 with the antilinear residual EXACTLY ZERO in all twelve and the symbolic typing holding in all twelve, so every copy is ONE COMPLEX SLOT in the SAME fork cell. THE COEFFICIENT IS LEVEL-INDEXED AND PARITY-INDEPENDENT WITH EXACTLY THREE DISTINCT VALUES -- 3193/2240 at t = 0 and 2, 43/35 at t = 1, and 1817/1120 at t = 3, 4 and 5 -- over level classes {0,2}, {1} and {3,4,5} which the gate MEASURES do NOT coincide with the pinned/free split {0,1} and {2,3,4,5}; the campaign record's two-value phrasing is corrected here and the correction is carried in the ledger of N7. The t = 3 copy is spelled out at 1817/1120 rather than inferred, because its coefficient differs from the one the landed embedding used. AND THE DISSOLUTION CLAIM IS REFUTED ON TWO MEASURED LEGS, WHICH IS THE SPINE OF THIS GATE. FIRST: the twelve copies are orthonormal but the rank-12 isotype Gram is NOT diagonal -- 36 nonzero off-diagonal entries, with the (3,0) copy coupling to exactly five others, (2,0), (2,1), (3,1), (4,0) and (4,1) -- so these are not twelve factorized scalar Gaussian cells. SECOND AND DECISIVELY: the flavor lane's OWN slot counter is ADDITIVE, r_from_slot_count(n) = n/2, and the gate calls THEIR function at Block 176's pinned blob rather than re-implementing it, obtaining r = 1/2 and Q = 2/3 for ONE copy but r = 6 and Q = 13/3 for all twelve. COPYWISE TYPE-INDEPENDENCE THEREFORE CANNOT SELECT OR COUNT ONE COPY: the one-copy choice in the landed embedding was LOAD-BEARING, Q = 2/3 FIRES FOR THE EXPLICIT ONE-COPY EMBEDDING, a multiplicity selector, quotient or fiber theorem is A NAMED OPEN REQUIREMENT, and asserting either that residue 3 is dissolved or that Q = 2/3 is unconditional fails this gate",
        gate_values["D"])
    checks.check(
        "E-THE-CARRIER-MAP-at-REPRESENTATION-METRIC-INSTANCE-LEVEL-with-THE-BASIS-VACUITY-WITNESS",
        "THE EQUIVARIANCE LEG IS EXACT AND IT IS THE ONLY LEG THAT CARRIES CONTENT. On the natural orbit basis of the 3-element chart orbit the committed U restricts to U_orb = [[0,0,1],[1,0,0],[0,1,0]] = P_3 EXACTLY, of exact order three, with the orbit preserved as U E = E P_3 -- the SAME 3-cycle permutation as the flavor lane's C_3 on the hw = 1 translation characters, BASIS-TO-BASIS. THE METRIC LEG IS AN EXACT INSTANCE OF THEIR OWN FAMILY: the orbit restriction is symmetric and circulant with coefficients (3193/2240, 0, 0), so the same-level distance-2 couplings VANISH on this carrier and the J-COMPONENT IS EXACTLY ZERO; decomposed on the isotypes it is alpha P_s + beta P_d at alpha = beta = 3193/2240, ALL THREE CHARACTER EIGENVALUES EQUAL, which is the DEGENERATE point of M(alpha, beta) and not a nondegenerate singlet/doublet split; and their own determinant law gives det_R = alpha beta^2 = 32553430057/11239424000 exactly, which the gate checks against the recomputed determinant so that eigenvalue degeneracy is visibly NOT determinant singularity. AND THE GATE EXHIBITS THE VACUITY RATHER THAN ASSERTING IT: because the restriction is a SCALAR it commutes with the NON-circulant witness e_0 e_1^T, and with the whole 3x3 matrix algebra, while the NONDEGENERATE family member M(1,2) does NOT commute with that witness. So at alpha = beta the set of basis changes preserving the metric is everything, THE METRIC-PRESERVATION LEG CONSTRAINS NOTHING, only U_orb = P_3 carries representation content, and WHAT IS EXHIBITED IS AN EQUIVARIANT ONE-ORBIT MODULE MAP AND NOT A PHYSICAL OBSERVABLE-PRESERVING CARRIER MAP. Asserting that the metric leg carries content, or a wrong family determinant, fails this gate",
        gate_values["E"])
    checks.check(
        "F-THE-REMAINDER-SIX-NAMED-ITEMS-with-THE-UNREACHED-RATIO-WALL",
        "THE REMAINDER LEDGER IS SIX ITEMS AND THIS GATE REQUIRES ALL SIX PRESENT, VERBATIM-KEYED, NOT SUMMARISED. THREE WERE RESTORED OR SUPPLIED BY THE CROSS-MODEL CHECK AND THEY COME FIRST BECAUSE THE FIRST OF THEM IS LOAD-BEARING: the MULTIPLICITY SELECTOR OR FIBER THEOREM, since copywise identical type does not reduce the total slot count to one; the M_2(C) CARRIER-ALGEBRA EMBEDDING as an injective unital *-map preserving products and adjoints, which identifying content-writes with shear pins does not supply; and NON-VACUOUS PHYSICAL OBSERVABLE PRESERVATION, since equality of two regular-representation 3-cycles plus preservation of a scalar metric proves module equivalence and not that the physical generators and observables coincide. THREE COME FROM THE SOLVE AND ARE CARRIED AT THEIR STATED STRENGTH: the RECORD-WRITE IDENTIFICATION, untouched; the AMBIENT MISMATCH at hw >= 2, untouched; and THE METRIC-RATIO DEGENERACY, which this gate binds to a measured fact -- alpha = beta at this realization, so THEIR r-SELECTION WALL, a statement about the metric RATIO, IS NOT REACHED BY THIS INSTANCE and ONLY THE POLARIZATION/COUNTING BIT TRANSFERS. THE STANDING DISCLOSURE OUTSIDE THE LEDGER IS ALSO REQUIRED: Q = (1+2r)/3 REMAINS THEIR IMPORTED AUTHORITY and is derived nowhere in this lane. Asserting that the flavor bridge is complete, or that the ratio wall is reached, fails HERE and nowhere else",
        gate_values["F"])
    checks.check(
        "G-THE-CAMPAIGN-CLOSE-the-CORRECTIONS-LEDGER-and-THE-OWNER-S-BAR-LIST",
        "THE CLOSE IS A STRUCTURAL VERDICT WITH NO MEASUREMENT OF ITS OWN, AND THIS GATE BINDS ITS PARTS AS DECLARED LITERALS. ONE COMMITTED STRUCTURE -- the action's complex unit, its sesquilinear-only grammar and the antiunitary reflection -- measured across SEVEN BLOCKS OF THE LANDED CHAIN, 171, 174, 175, 176, 177, 178 and this one, each cited in the note, to supply: the BORN-SHAPED READOUT CANDIDATE within a fork-independent FAMILY; the CONDITIONAL SYMMETRIC-POWER THEOREM with every n >= 1 sector indefinite on either kernel, the vacuum window unique IN-FAMILY and the grading fork GENUINE; the SHEAR-MIRROR THEOREM with the canonical reconstruction blocked at shear scope; TRANSPORT MEASURED AS A RECORD-CONSISTENCY RESPONSE at interpretation scope; the KOIDE COUNTING BIT supplied for the EXPLICIT ONE-COPY EMBEDDING with Q = 2/3 exact, the one-copy scoping being part of the supply and not a footnote; and the CROSS-LANE PINCER, the pincer identity #7318 with the sister lane's #7325 countermodel CLOSING THE AXIOMS-ONLY SELECTION ROUTE. THE HONEST LIMITS ARE REQUIRED PRESENT: no unique readout derivation and a readout axiom that would be needed and is NEVER PROPOSED HERE; the sector identification a GENUINE FORK; the full flavor bridge needing the six-item remainder; and nothing registered or adopted. THE ITEMS AT THE OWNER'S BAR ARE LISTED -- the counting-bit supply, the reflection-pairing readout principle, and the drawer items from the prior campaign -- and REMOVING THAT LIST FAILS HERE. AND THE CORRECTIONS LEDGER FOR THE WHOLE CAMPAIGN IS THE VERIFICATION STRUCTURE'S PRODUCT, in three groups: FIVE SUPERVISOR CUT HYPOTHESES including this round's multiplicity-dissolution claim, THREE GROUPS OF CHECKER DISCOVERIES, and TWO DRAFT-WORKER CATCHES including this block's three-valued level ledger. THE CHECKER IS CREDITED and the note states that ITS FINDINGS OVERRIDE THE SOLVE EVERYWHERE THEY COLLIDE. Removing the corrections ledger or the owner's-bar list, or asserting the readout derived, fails HERE and nowhere else",
        gate_values["G"])
    checks.check(
        "H-note-scope-the-caution-and-the-N5-fence",
        "THE NOTE SITS AT ITS FINAL PATH AND SATISFIES EVERY REQUIRED SCOPE KEY, the required set is THE FULL KEY SET and not a subset, the N5 fence is an N5-prefixed literal with nine labelled sections that appears BYTE-IDENTICALLY in the note, and the mutation battery is fifteen members mapped one-per-gate across A through H. THE VERDICT THIS GATE CERTIFIES IS FOUR SCOPED STATEMENTS AND NOTHING WIDER: RESIDUE 4 IS DISSOLVED TRIVIALLY, the orientation equality FORCED and not new selector content; RESIDUE 3 IS NARROWED AND NOT DISSOLVED, with Q = 2/3 firing for the explicit ONE-COPY embedding and a selector or fiber theorem a NAMED OPEN REQUIREMENT; THE CARRIER MAP IS EXHIBITED AT REPRESENTATION/METRIC-INSTANCE LEVEL, its metric leg basis-vacuous, an equivariant one-orbit module map and NOT a physical observable-preserving carrier map; and THE REMAINDER IS SIX NAMED ITEMS, all open. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 caution, carried verbatim -- and every positive here is CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE. The worker profile is disclosed in full: ALL SOLVE-SIDE SCIENCE by the supervising frontier model INLINE, per the owner's standing directive; the REFUTE-SPEC'D adversarial check by a codex 5.6-sol xhigh worker, cross-model, whose findings OVERRIDE the solve everywhere they collide; OPUS MECHANICAL DRAFTING ONLY; and supervisor review and landing -- with common-mode risk reduced and NOT eliminated. The scope is ONE FIXTURE and no wider; it is NOT a continuum statement, NOT A FLAVOR BRIDGE, NOT a derivation of the Koide relation and NOT a derivation of the Born rule; and the disclosures are complete, THIS BLOCK'S OWN DEFECTS INCLUDED -- one fixture with no ladder, one residue dissolved and dissolved trivially, the multiplicity dissolution withdrawn, the carrier map representation-level, Q = (1+2r)/3 still imported authority, and the campaign-close section carrying no measurement of its own -- alongside NO FLOAT anywhere, the not-re-verified list, N1 through N8, the W1 wall, the scope-key certificate, the LaTeX rho guard, the pool-2 leads, the three handoff items, zero axiom retirement, zero obligation retirement, no TOE percentage movement, a retained-positive end-to-end theory count that remains zero, and NO priority or originality wording anywhere in the note",
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
