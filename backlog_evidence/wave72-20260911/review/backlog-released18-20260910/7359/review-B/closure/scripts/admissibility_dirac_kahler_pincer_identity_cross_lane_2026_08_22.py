#!/usr/bin/env python3
"""BLOCK 175 -- THE PINCER IDENTITY: the two lanes compute the same object.

THE RESULT, AND ITS EXACT SCOPE.  On the committed antiperiodic Dirac-Kahler
12x4 bench at read slice t* = 5, with the xgraded carrier at sigma = 3/5, the
region pin c = 1, s_t = 0, s_x = 3/5, m = 1, the single free record cell (2,0)
and the value menu {0, 1/5, 2/5, 3/5}:

  1. THE IDENTITY.  The W9 record-slice block at t* occupies ambient rows and
     columns (20,21,22,23) and its OFF-DIAGONAL SUPPORT IS EMPTY EXACTLY, so its
     normalized diagonal C is a classical density over the menu.  With
     E_j = |j><j| in CM-SITE order, Tr(C E_j) EQUALS the landed W9 marginal
     profile ENTRY FOR ENTRY, exact defect (0,0,0,0).  The parallel
     record-born-composition lane's selected trace law and this lane's marginal
     profile are THE SAME OBJECT at their interface on this fixture.

  2. THE SPLIT.  The formation-conditional normalized |det Q(sigma_(2,0)=a)|^-2
     law differs from that trace/marginal law in ALL FOUR entries, at exact
     nonzero rational deltas over a displayed common denominator K, signs
     (+,-,-,+), sum exactly zero.  The MARGINAL-VERSUS-CONDITIONAL distinction
     is the sharp surviving form of the readout question, and it is this block's
     OWN WITNESS that the identification is of the marginal ONLY.

  3. ADDITIVITY, HONESTLY SPLIT.  The trace law is NATIVELY additive -- union
     effects are operator sums, the trace is linear, and both declared
     three-outcome partitions have exact defect (0,0,0).  The determinant law's
     coarse additivity is a DEFINITIONAL PUSHFORWARD: no primitive value-union
     pin exists in the machinery, measured three ways, so the induced coarse
     defect (0,0,0) IS NOT ACTION-LEVEL MERGE CLOSURE.  The Block 172 nonclosure
     concerns definable multi-cell CONJUNCTION pins and not mutually exclusive
     value alternatives at one cell; it is SCOPED here, not invoked.

  4. THE JOINT CAGE.  The parallel lane (PR #7316) names "trace-Law selection
     from the four axioms" as NOT DERIVED; Block 174 names the READOUT PRINCIPLE
     as this lane's missing input.  They are ONE QUESTION WITH TWO EXACT OBJECT
     FAMILIES, and any candidate principle must survive BOTH fixture sets.

  5. THE SCOPE.  An identification of the MARGINAL record-slice object only, NOT
     of every law the committed action generates.  NO SELECTION PRINCIPLE IS
     SUPPLIED.  NOTHING IS REGISTERED, ADOPTED OR PROPOSED.

THE CROSS-LANE DISCIPLINE, ENFORCED MECHANICALLY.  The other lane's note is an
IN-REPO REFERENCE, cited by PR number and quoted verbatim in this block's note.
IT IS DELIBERATELY NOT AN EXECUTION INPUT: it appears nowhere in
AUDIT_INPUT_PATHS, nothing in this runner reads it, and every number this runner
produces is rebuilt from THIS lane's Block 171-174 machinery on THIS lane's
committed fixtures.  That is the standing converge-don't-borrow directive applied
literally.  Gate F checks quotation INTEGRITY -- that the quoted passages are
present verbatim in this block's note -- and never their correctness.

GATES
  A  authority: main plus the TWO Block 174 artifacts content-bound, the parent
     runner ACTUALLY IMPORTED, and the stale pin verified to carry NEITHER
     artifact.
  B  the two banners, the bench anchor, and THE S-DIAG PRECONDITION.
  C  THE IDENTITY: C rebuilt from W9 by two independent routes, the four
     Tr(C E_j), and zero defect against the landed profile.
  D  THE SPLIT: the |det Q|^-2 law at the record cell, the four deltas against
     embedded exact literals, and the exact sum-zero control.
  E  ADDITIVITY: both partitions, trace-law defects zero, the pushforward
     construction, and the NO-PRIMITIVE-UNION-PIN statement measured three ways.
  F  THE JOINT CAGE and the CROSS-LANE QUOTATION INTEGRITY.
  G  SCOPE DISCIPLINE: marginal-only, the not-every-law disclaimer with its
     measured witness, and the successor question.
  H  note at final path, the FULL scope-key certificate, and the N5 fence.

BASELINE EXPECTATION: 7 of 8, with H failing on note-at-final-path alone until
the note is landed at docs/.

RUNNING
  python3 scripts/admissibility_dirac_kahler_pincer_identity_cross_lane_2026_08_22.py
  python3 ... --list-mutations
  python3 ... --mutation break_identity
  python3 ... --deep

NOTES FOR THE LANDING AGENT
  1. PARENT_COMMIT is REAL and PARENT_REF resolves to it; nothing needs sed.
  2. CURRENT_MAIN was RE-RESOLVED at draft time.
  3. The stale pin is the Block 173 nsimplify-hygiene tip, a real ancestor of
     HEAD that carries NEITHER Block 174 artifact -- which is what makes the
     stale_parent_authority mutation bite.
  4. Re-run at landing; gate H should then pass and the battery should be 8/8.
"""

from __future__ import annotations

import argparse
import ast
import inspect
import subprocess
import sys
import time
from dataclasses import dataclass
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

# THE PARENT IMPORT.  Block 174 is the stack parent AND the content parent: its
# runner carries the Fixture builder, the exact determinant route and the W9
# profile construction this block measures on, and it re-exports the whole
# landed chain below it.
try:
    import admissibility_dirac_kahler_site_conditional_law_family_2026_08_22 as b174
    PARENT_IMPORT_LANDED = True
except ModuleNotFoundError:                                   # unlanded parent
    b174 = None
    PARENT_IMPORT_LANDED = False

if b174 is not None:
    b173 = b174.b173
    b172 = b174.b172
    b171 = b174.b171
else:                                                  # pragma: no cover
    b173 = None
    b172 = None
    import admissibility_dirac_kahler_generator_trilemma_kernel_2026_08_21 as b171

b170 = b171.b170
b165 = b171.b165

herm = b171.herm
is_zero = b171.is_zero
tri = b171.tri
exact_inv = b171.exact_inv

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_PINCER_IDENTITY_CROSS_LANE_"
    "BOUNDED_THEOREM_NOTE_2026-08-22.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
# DECLARED DRAFT FALLBACK, read ONLY when the final path is absent.  Gate H
# requires the final path, so the fallback never makes a gate pass.
DRAFT_NOTE_PATH = Path(
    "/private/tmp/claude-502/"
    "-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-"
    "gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/"
    "scratchpad/block175_note_draft.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE SINGLE-PARENT PIN.  Block 174 (the site-conditional law family) is BOTH the
# stack parent and the content parent, so there are exactly TWO artifact pins.
BLOCK174_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_CONDITIONAL_LAW_FAMILY_"
    "BOUNDED_THEOREM_NOTE_2026-08-22.md"
)
BLOCK174_RUNNER = (
    "scripts/admissibility_dirac_kahler_site_conditional_law_family_"
    "2026_08_22.py"
)
PARENT_ARTIFACTS = (BLOCK174_NOTE, BLOCK174_RUNNER)
PARENT_ARTIFACT_BLOBS = (
    "87b690df43e404723f26ff84318f35df6c0d981c",   # Block 174 note
    "b64d33f794c93b83bb4ed77fcc13d9db459ce5b5",   # Block 174 runner
)

# Deliberately literal: this is the complete audit read surface.  Every entry is
# a WORKTREE-READABLE path at landing time.  THE PARALLEL LANE'S NOTE IS NOT
# HERE AND THAT IS DELIBERATE: it is QUOTED TEXT in this block's note, referenced
# by PR number, and it is never an execution input.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_PINCER_IDENTITY_CROSS_LANE_BOUNDED_THEOREM_NOTE_2026-08-22.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_CONDITIONAL_LAW_FAMILY_BOUNDED_THEOREM_NOTE_2026-08-22.md",
    "scripts/admissibility_dirac_kahler_site_conditional_law_family_2026_08_22.py",
)

AUDIT_TIMEOUT_SEC = 600
# THE FIVE-PIN AUTHORITY BLOCK, single-line hex literals refreshed by anchored
# sed at landing.  CURRENT_MAIN WAS RE-RESOLVED AT DRAFT TIME and is unchanged
# from the Block 174 pin.
CURRENT_MAIN = "c048322f959ce33e866ab1d34f0f3571a3bb6e67"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
# This block stacks on the Block 174 tip, so the parent branch is that.
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block174-"
              "site-conditional-law-family-20260822")
PARENT_COMMIT = "688acb0f9786922b9386545ccef41a5d19af35db"
# The Block 173 nsimplify-hygiene tip: a real ancestor of HEAD that predates
# Block 174 and therefore carries NEITHER Block 174 artifact.  Read ONLY under
# the stale mutation, where the missing blobs are exactly what makes it bite.
STALE_PARENT_COMMIT = "3c4d52bdb9d3d2e1211799db7232b91b561bf0e1"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_offdiagonal_support_nonempty",
    "claim_cross_lane_note_adopted",
    "break_identity",
    "claim_identity_defect_nonzero",
    "claim_det_law_equals_trace",
    "claim_deltas_sum_nonzero",
    "claim_det_additivity_structural",
    "claim_trace_additivity_defective",
    "claim_their_selection_closed",
    "break_quotation_integrity",
    "claim_identity_all_laws",
    "drop_joint_cage",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_offdiagonal_support_nonempty": "B",
    "claim_cross_lane_note_adopted": "B",
    "break_identity": "C",
    "claim_identity_defect_nonzero": "C",
    "claim_det_law_equals_trace": "D",
    "claim_deltas_sum_nonzero": "D",
    "claim_det_additivity_structural": "E",
    "claim_trace_additivity_defective": "E",
    "claim_their_selection_closed": "F",
    "break_quotation_integrity": "F",
    "claim_identity_all_laws": "G",
    "drop_joint_cage": "H",
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
# the Block 174 convention extended by one link.  IT IS NOT the full transitive
# module closure, and gate A reports the residual count outside it rather than
# claiming the corpus clean.
def audit_source_paths() -> tuple:
    paths = [Path(__file__).resolve()]
    for module in (b174, b173, b172, b171):
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


BANNED_CALLS = ("nsim" + "plify", "evalf", "Float", "RealNumber")
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
    """LIVE CALL SITES, not text mentions: an AST Attribute or Name node whose
    identifier is the banned simplifier.  Prose and gate names that merely NAME
    it are not call sites."""
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
    for name, module in (("b174", b174), ("b173", b173), ("b172", b172),
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
            chain[name][1] for name in ("b174", "b173", "b172", "b171")),
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
        # THE STALE LEG.  At the Block 173 hygiene tip NEITHER Block 174 artifact
        # exists, so this is False and the stale mutation fails gate A.
        bool(all(is_hash(v) for v in stale_blobs)
             and stale_blobs == worktree_blobs),
        is_ancestor(STALE_PARENT_COMMIT, "HEAD"),
        not any(is_hash(v) for v in stale_blobs),
        PARENT_IMPORT_LANDED,
        residue_report())


# ---------------------------------------------------------------------------
# the 175-specific layer
# ---------------------------------------------------------------------------
NUMERALS: list = []


def record(value):
    """Every reported numeral passes through here for the no-float gate."""
    NUMERALS.append(value)
    return value


def bracket(q, den=10 ** 8):
    """The house bracket form: [floor(|q| den)/den, ceil(|q| den)/den]."""
    value = sp.Abs(sp.cancel(q))
    return (R(sp.floor(value * den), den), R(sp.ceiling(value * den), den))


COVER_T = 12
LX = 4
MENU = (Z0, R(1, 5), R(2, 5), R(3, 5))
RECORD_CELL = (2, 0)
TSTAR = 5
AMBIENT_ROWS = (20, 21, 22, 23)
PARTITIONS = (
    ((MENU[0],), (MENU[1], MENU[2]), (MENU[3],)),
    ((MENU[0], MENU[1]), (MENU[2],), (MENU[3],)),
)
# THE BREAK-IDENTITY PERTURBATION: an exact rational nudge of one diagonal entry
# of C, measured beside the true reading so a mutation rewrites a CLAIM and never
# a measurement.
PERTURBATION = R(1, 10 ** 6)
RUNTIME_BUDGET_SEC = 120
DEEP_RUNTIME_BUDGET_SEC = 600
POOL_TWO_LEADS = 4
HANDOFF_ITEMS = 3

# THE IMPOSED OBJECTS OF THIS BLOCK, declared as a literal so the banner is a
# measured object and not only prose.  NONE of them is registered or adopted.
IMPOSED_OBJECTS = (
    "the classical density C, the normalized W9 record-slice diagonal",
    "the projector effects E_j = |j><j| in CM-SITE order",
    "the two menu partitions P1 and P2 and their union effects",
    "the pushforward extension w(U) = sum_{a in U} w(a)",
    "the |det Q|^-2 formation-conditional readout arm, inherited",
    "the shear menu read as the possibilities at a free cell, inherited",
    "the class map CM-SITE, the record-extension wiring and the slot order",
    "the record-slice (RS) scope and W9 = herm(Q^{-1}), inherited",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
# THE DECISION that belongs to the owner and is NOT taken here.
OWNER_DECISIONS = (
    "THE BRIDGE DECISION: whether either measured object is ever identified "
    "with the Admissibility distribution as a semantic bridge, or supplied as "
    "an approved primitive -- the Block 174 row stays quoted and NOT YET EARNED",
)

# THE CROSS-LANE QUOTATIONS.  These are QUOTED TEXT, checked for presence in THIS
# block's note.  The other lane's file is NEVER read by this runner.
THEIR_PR = "#7316"
THEIR_NOTE_NAME = (
    "NN_RECORD_PROGRAM_PREPARATION_QUOTIENT_TRACE_COMPILER_"
    "BOUNDED_THEOREM_NOTE_2026-08-22.md"
)
THEIR_SELECTED_LAW = (
    "One fixed selected downstream rule is total on all shells; when the common "
    "Hermitian part is a density matrix and the program is valid, it assigns "
    "Tr(C E_j), writes literal projector contents on the selected binary "
    "projective subdomain, and otherwise writes injective effect-label "
    "contents, while all other shells receive a deterministic covariant "
    "fallback."
)
THEIR_OPEN_ITEM = (
    "| preparation-matrix calibration and trace-Law selection from the four "
    "axioms | not derived; equation (2) is downstream Law content |"
)
THEIR_OPEN_PROSE = (
    "Density-matrix preparation calibration, trace-Law selection from the four "
    "axioms, program genesis, formation site/rate, histories, and composite "
    "Bell carrier are not derived."
)
OUR_OPEN_ITEM = "an independent probability/readout principle"
# The axiom clause is taken from the LANDED Block 174 constant so no
# transcription of the axioms file happens here.  QUOTED, NEVER EDITED.
AXIOM_CLAUSE = b174.AXIOM_CLAUSE if b174 is not None else ""


def projector(index: int) -> sp.Matrix:
    effect = sp.zeros(4, 4)
    effect[index, index] = ONE
    return effect


def effect_for(cell) -> sp.Matrix:
    return sum((projector(MENU.index(a)) for a in cell), sp.zeros(4, 4))


def trace_reading(density: sp.Matrix, effect: sp.Matrix):
    return sp.cancel(sp.trace(density * effect))


def common_denominator(values) -> tuple:
    denominator = sp.Integer(1)
    for value in values:
        denominator = sp.ilcm(denominator, sp.Rational(value).q)
    return (tuple(sp.Integer(sp.Rational(v) * denominator) for v in values),
            denominator)


# ---------------------------------------------------------------------------
# B. the two banners, the bench anchor and THE S-DIAG PRECONDITION
# ---------------------------------------------------------------------------
def measure_convention() -> dict:
    """THE COLLISION, MEASURED on identical matrices and never asserted.  The
    instrument is the LANDED one, read through Block 174 rather than rebuilt."""
    return b174.measure_convention()


def measure_bench() -> dict:
    """The bench anchor: this block's fixture against the landed field, the two
    determinant routes against each other, and the exact inverse/congruence
    residuals.  The Berkowitz route is gated against DomainMatrix HERE because
    gate D's determinant law is taken by one of them."""
    fixture = b174.Fixture(LX, tag="b175")
    records = {RECORD_CELL: Z0}
    q = fixture.q(records)
    qi = exact_inv(q)
    s = herm(q)
    w9 = sp.expand((qi + qi.H) / 2)
    eye = sp.eye(fixture.N)
    det_dm = b174.dm_det(q)
    det_bk = sp.expand(q.det(method="berkowitz"))
    landed_field = b171.field(fixture.fx, fixture.c, b171.CARRIER_SIGMA,
                              "xgraded", records)
    return {
        "T_phys": fixture.T,
        "N": fixture.N,
        "lx": fixture.lx,
        "tstar": fixture.tstar,
        "free_levels": fixture.free_levels,
        "q_symbol_free": not q.free_symbols,
        "field_matches_landed": fixture.field(b171.CARRIER_SIGMA, records)
        == landed_field,
        "inverse_residual_zero": (is_zero(sp.expand(q * qi) - eye)
                                  and is_zero(sp.expand(qi * q) - eye)),
        "congruence_zero": is_zero(w9 - sp.expand(qi * s * qi.H)),
        "hermq_inertia": tuple(b165.real_symmetric_inertia(s)),
        "det_routes_agree": sp.expand(det_dm - det_bk) == 0,
        "det_nonzero": det_dm != 0,
        "menu_is_sigma_classes": MENU == tuple(b171.SIGMA_CLASSES),
        "menu_matches_parent": MENU == tuple(b174.MENU),
        "tstar_is_five": fixture.tstar == TSTAR,
    }


def measure_sdiag() -> dict:
    """THE S-DIAG PRECONDITION, measured before any trace is read.

    The unrecorded W9 record-slice block at t* must have EMPTY off-diagonal
    support for its normalized diagonal to be a classical density.  Twelve exact
    expansions decide it; none of them is a smallness test.
    """
    site = b171.Site(f"b175-{COVER_T}x{LX}", COVER_T, LX)
    env = b171.Env(site, site.bench.Q.subs(site.sub()), "bench")
    block = env.block("W9", site.tstar)
    off = tuple((i, j) for i in range(4) for j in range(4)
                if i != j and sp.expand(block[i, j]) != 0)
    diagonal = tuple(sp.expand(block[i, i]) for i in range(4))
    return {
        "env_tstar": site.tstar,
        "ambient_rows": tuple(LX * (site.tstar % site.bench.T) + x
                              for x in range(LX)),
        "off_diagonal_entries": len(off),
        "off_diagonal_empty": not off,
        "diagonal_all_positive": all(v > 0 for v in diagonal),
        "block": block,
        "env_profile": tuple(sp.cancel(v)
                             for v in env.profile("W9", site.tstar)),
    }


# ---------------------------------------------------------------------------
# C. THE IDENTITY
# ---------------------------------------------------------------------------
def measure_identity(sdiag: dict) -> dict:
    """THE IDENTITY, by two independent routes.

    Route one is the landed b171 Env block/profile.  Route two rebuilds W9 from
    the Block 174 Fixture, extracts the same 4x4 record-slice block and
    normalizes it.  The two routes are gated to agree BEFORE either is compared
    to anything, so the equality is not an artefact of one construction.
    """
    fixture = b174.Fixture(LX, tag="b175-identity")
    landed_law, q, qi = b174.profile_of(fixture, {})
    w9 = sp.expand((qi + qi.H) / 2)
    rows = [fixture.lx * (fixture.tstar % fixture.T) + x
            for x in range(fixture.lx)]
    block = sp.Matrix(4, 4, lambda i, j: sp.expand(w9[rows[i], rows[j]]))
    total = sp.expand(sp.trace(block))
    density = sp.diag(*(sp.cancel(block[i, i] / total) for i in range(4)))
    effects = tuple(projector(j) for j in range(4))
    trace_law = tuple(trace_reading(density, effect) for effect in effects)
    defect = tuple(sp.cancel(a - b) for a, b in zip(trace_law, landed_law))
    # THE PERTURBED READING, measured beside the true one.  Under break_identity
    # gate C reads THIS defect instead, and it is exactly nonzero.
    bad = sp.Matrix(density)
    bad[0, 0] = sp.cancel(bad[0, 0] + PERTURBATION)
    bad_law = tuple(trace_reading(bad, effect) for effect in effects)
    bad_defect = tuple(sp.cancel(a - b) for a, b in zip(bad_law, landed_law))
    numerators, denominator = common_denominator(trace_law)
    return {
        "rows": tuple(rows),
        "rows_match_env": tuple(rows) == sdiag["ambient_rows"],
        "routes_agree_block": block == sdiag["block"],
        "routes_agree_profile": tuple(landed_law) == sdiag["env_profile"],
        "density": tuple(density[i, i] for i in range(4)),
        "density_numerators": numerators,
        "density_denominator": denominator,
        "hermitian": density == density.H,
        "unit_trace": sp.cancel(sp.trace(density)) == ONE,
        "all_positive": all(v > 0 for v in trace_law),
        "trace_law": trace_law,
        "landed_law": tuple(landed_law),
        "defect": defect,
        "defect_zero": all(v == 0 for v in defect),
        "perturbed_defect": bad_defect,
        "perturbed_defect_zero": all(v == 0 for v in bad_defect),
        # THE SCOPE FACT: the identification does NOT extend to every law the
        # action generates, and gate D's split is its measured witness.
        "extends_to_all_laws": False,
    }


# ---------------------------------------------------------------------------
# D. THE SPLIT
# ---------------------------------------------------------------------------
# THE EXACT DELTA LITERALS, recomputed in the measurement pass and compared here.
DELTA_DENOMINATOR = 1344173296711094704835428073823017291190913221629122091108176433724106249704663413521023320291060235331780727736347228538496413344908318091814973601305427683747236272426839747849819772184197262451488884746699353926523874363940362560825770018959219238176806384247496002831987704966625261250542202896
DELTA_NUMERATORS = (
    14467388661915621642061470731751517502511186327587947949978816654858825682705486105755975510577098860792439436993365616522100975239037946638050415467045613468535622935587047809247303038157605096432846466937226313313862436902601175203115425843906718825102455329725563844375702457243986137333815736,
    -42930229458862468953609725077193163242427863651066543664094151808262834567942721751570362551398546544046351000983682286161047319545843949235939794883752266644803736275477889289843265439662859246678252255368441152358343362695610419856088741257524578448553212778208916122800003770050096770627216224,
    -3359031284642723011719745958203998144967559225374071817055516108374180970566212469705810920723630454521652890293750453798506247548670705856237195876078808293623563572565263927484290369664122297731448996936566473985616773731314166826840940140325801902575862737958074022705185628611420281534942431,
    31821872081589570323268000303645643884884236548852667531170851261778189855803448115520197961545078137775564454284067123437452591855476708454126575292785461469891676912456105408080252771169376447976854785367781313030097699524323411479814255553943661526026620186441426301129486941417530914828342919,
)
DELTA_SIGNS = (1, -1, -1, 1)
DELTA_BRACKETS = (
    (R(1076303, 100000000), R(67269, 6250000)),
    (R(3193801, 100000000), R(1596901, 50000000)),
    (R(49979, 20000000), R(31237, 12500000)),
    (R(2367393, 100000000), R(1183697, 50000000)),
)
# THE EXACT DENSITY LITERALS from the same measured run.
DENSITY_DENOMINATOR = 894555786619317339421650665156104028453509785664333673843970497575127328208
DENSITY_NUMERATORS = (
    268251574285153956297813548296329792195197468843616541008641132195640585440,
    221001943568477496197298503927672181662102219068198431958029827878618664480,
    218355469342291864735240151179441946892053542743480442321946476045569116869,
    186946799423394022191298461752660107704156555009038258555353061455298961419,
)


def measure_split(identity: dict, deep: bool) -> dict:
    """THE FORMATION-CONDITIONAL LAW at the free record cell, against the
    trace/marginal law.  Four scalar pins, four exact determinants, four exact
    normalized weights, four exact deltas."""
    fixture = b174.Fixture(LX, tag="b175-split")
    dets = []
    raw = []
    routes_agree = []
    for value in MENU:
        q = fixture.q({RECORD_CELL: value})
        det = b174.dm_det(q)
        if deep:
            # THE SECOND ROUTE, run only under --deep: Berkowitz on all four
            # pinned matrices rather than on the bench alone.  MEASURED, not
            # asserted, so gate D reads it like every other fact.
            routes_agree.append(
                sp.expand(det - q.det(method="berkowitz")) == 0)
        dets.append(det)
        raw.append(sp.cancel(ONE / b174.norm2(det)))
    det_law = b174.normalize(tuple(raw))
    deltas = tuple(sp.cancel(a - b)
                   for a, b in zip(identity["trace_law"], det_law))
    numerators, denominator = common_denominator(deltas)
    return {
        "cell": RECORD_CELL,
        "dets_nonzero": all(v != 0 for v in dets),
        "raw_positive": all(v > 0 for v in raw),
        "det_law": det_law,
        "det_law_normalized": sp.cancel(sum(det_law, Z0)) == ONE,
        "det_law_positive": all(v > 0 for v in det_law),
        "raw": tuple(raw),
        "deltas": deltas,
        "numerators": numerators,
        "denominator": denominator,
        "literals_agree": (numerators == DELTA_NUMERATORS
                           and denominator == DELTA_DENOMINATOR),
        "signs": tuple(sp.sign(v) for v in deltas),
        "signs_agree": tuple(int(sp.sign(v)) for v in deltas) == DELTA_SIGNS,
        "all_deltas_nonzero": all(v != 0 for v in deltas),
        "sum_zero": sp.cancel(sum(deltas, Z0)) == 0,
        "brackets": tuple(bracket(v) for v in deltas),
        "brackets_agree": tuple(bracket(v) for v in deltas) == DELTA_BRACKETS,
        "deep_det_routes": deep,
        "deep_routes_checked": len(routes_agree),
        "deep_routes_agree": all(routes_agree) and len(routes_agree) == len(MENU),
    }


# ---------------------------------------------------------------------------
# E. ADDITIVITY, HONESTLY SPLIT
# ---------------------------------------------------------------------------
def measure_union_pin_absence() -> dict:
    """THE ABSENCE OF A PRIMITIVE VALUE-UNION PIN, measured three ways.

    1. The landed field builder maps a cell to ONE scalar: its own source is
       read and the scalar-valued lookup is located in it.
    2. Two values at one dictionary key COLLAPSE to one, so writing several menu
       values at the same record key is not a simultaneous pin.
    3. A set handed to a record key sympifies to a FiniteSet, which is not a
       number, so it is not a shear value and no Q(sigma in U) is formed.

    A fourth, weaker check reads the parent runner's whole source for a
    union-pin API name and finds none.
    """
    source = inspect.getsource(b174.Fixture.field)
    collapse = {RECORD_CELL: MENU[0], RECORD_CELL: MENU[1]}      # noqa: F601
    as_set = sp.sympify({MENU[0], MENU[1]})
    parent_source = Path(b174.__file__).read_text(encoding="utf-8")
    api_names = ("records_union", "value_union", "union_pin", "Q_union")
    return {
        "field_source_scalar_lookup": "records.get((t, x), sigma)" in source,
        "field_source_sympifies_scalar":
            "sp.sympify(records.get((t, x), sigma))" in source,
        "key_collapse_length": len(collapse),
        "key_collapse_keeps_last": collapse[RECORD_CELL] == MENU[1],
        "key_collapse_is_not_a_pin": len(collapse) == 1,
        "set_is_not_a_number": not bool(as_set.is_number),
        "set_type": type(as_set).__name__,
        "no_union_api": not any(name in parent_source for name in api_names),
        "api_names_searched": api_names,
    }


def measure_additivity(identity: dict, split: dict) -> dict:
    """BOTH PARTITIONS, BOTH LAWS.  The trace side is native; the determinant
    side is a pushforward and is labelled as one."""
    density = sp.diag(*identity["trace_law"])
    per_partition = []
    for number, partition in enumerate(PARTITIONS, start=1):
        union_effects = tuple(effect_for(cell) for cell in partition)
        orthogonal = all(
            sp.expand(union_effects[i] * union_effects[j]) == sp.zeros(4, 4)
            for i in range(len(union_effects))
            for j in range(len(union_effects)) if i != j)
        resolves = sum(union_effects, sp.zeros(4, 4)) == sp.eye(4)
        coarse = tuple(trace_reading(density, e) for e in union_effects)
        sums = tuple(
            sp.cancel(sum((identity["trace_law"][MENU.index(a)] for a in cell),
                          Z0))
            for cell in partition)
        trace_defect = tuple(sp.cancel(a - b) for a, b in zip(coarse, sums))
        pushforward = tuple(
            sp.cancel(sum((split["det_law"][MENU.index(a)] for a in cell), Z0))
            for cell in partition)
        raw_union = tuple(
            sp.cancel(sum((split["raw"][MENU.index(a)] for a in cell), Z0))
            for cell in partition)
        induced = b174.normalize(raw_union)
        det_defect = tuple(sp.cancel(a - b)
                           for a, b in zip(induced, pushforward))
        per_partition.append({
            "number": number,
            "partition": partition,
            "orthogonal": orthogonal,
            "resolves_identity": resolves,
            "trace_coarse": coarse,
            "trace_defect": trace_defect,
            "trace_defect_zero": all(v == 0 for v in trace_defect),
            "det_pushforward": pushforward,
            "det_induced": induced,
            "det_defect": det_defect,
            "det_defect_zero": all(v == 0 for v in det_defect),
        })
    union = measure_union_pin_absence()
    return {
        "partitions": tuple(per_partition),
        "trace_defects_zero": all(p["trace_defect_zero"]
                                  for p in per_partition),
        "det_defects_zero": all(p["det_defect_zero"] for p in per_partition),
        "effects_are_projectors": all(p["orthogonal"] and p["resolves_identity"]
                                      for p in per_partition),
        "union": union,
        # THE HONEST LABEL: with no primitive union pin, the determinant law's
        # coarse additivity is a pushforward by construction and is NOT
        # action-level merge closure.
        "pushforward_is_definitional": bool(
            union["field_source_scalar_lookup"]
            and union["field_source_sympifies_scalar"]
            and union["key_collapse_is_not_a_pin"]
            and union["set_is_not_a_number"]
            and union["no_union_api"]),
        "shows_merge_closure": False,
        # THE B172 SCOPING, carried as a declared flag rather than re-derived:
        # that nonclosure concerns definable multi-cell CONJUNCTION pins.
        "b172_is_conjunction_scoped": True,
    }


# ---------------------------------------------------------------------------
# F. THE JOINT CAGE and the cross-lane quotation integrity
# ---------------------------------------------------------------------------
THEIR_CAGE_ITEMS = (
    "refinement additivity",
    "covariant decoding under all 24 proper cubic rotations",
    "normalization",
    "the pure-state zero/one endpoints",
    "the parent prefix-marginal formula on supplied shells",
)
OUR_CAGE_ITEMS = (
    "exact rationality",
    "chart sensitivity on the L2 period-2 fingerprint",
    "screened locality with an exactly nonzero finite-width twin gap",
    "level indexing P_{s,t_r}",
)


def measure_cage(note_text: str) -> dict:
    """THE CAGE, as note-text checks and quotation-integrity checks.

    NOTHING HERE READS THE OTHER LANE'S FILE.  The three quoted passages are
    embedded literals and the gate verifies they are present VERBATIM in THIS
    block's note.  Quotation INTEGRITY is the whole claim; their correctness is
    not checked and is not claimed.
    """
    note = normalized_note(note_text)
    return {
        "their_pr_cited": THEIR_PR in note_text,
        "their_note_named": THEIR_NOTE_NAME.lower() in note,
        "selected_law_quoted": normalized_note(THEIR_SELECTED_LAW) in note,
        "open_item_quoted": normalized_note(THEIR_OPEN_ITEM) in note,
        "open_prose_quoted": normalized_note(THEIR_OPEN_PROSE) in note,
        "our_open_item_named": normalized_note(OUR_OPEN_ITEM) in note,
        # MEASURED FROM THE QUOTATION ITSELF: their row says "not derived".
        "their_item_open": "not derived" in normalized_note(THEIR_OPEN_ITEM),
        "quotations_verbatim": bool(
            normalized_note(THEIR_SELECTED_LAW) in note
            and normalized_note(THEIR_OPEN_ITEM) in note
            and normalized_note(THEIR_OPEN_PROSE) in note),
        "their_cage_items": THEIR_CAGE_ITEMS,
        "our_cage_items": OUR_CAGE_ITEMS,
        "their_items_present": all(normalized_note(item) in note
                                   for item in THEIR_CAGE_ITEMS),
        "our_items_present": all(normalized_note(item) in note
                                 for item in OUR_CAGE_ITEMS),
        "one_question_two_families":
            "one question with two exact object families" in note,
        # THE DISCIPLINE, mechanically: their note is not an execution input.
        "not_an_execution_input": not any(
            THEIR_NOTE_NAME in path for path in AUDIT_INPUT_PATHS),
        "gleason_flagged_not_asserted": ("flagged" in note
                                         and "not asserted" in note),
    }


# ---------------------------------------------------------------------------
# the scope-key certificate
# ---------------------------------------------------------------------------
SCOPE_KEYS = (
    # --- N0: THE TWO BANNERS, first -----------------------------------------
    "convention_banner",
    "convention_hazard_order",
    "convention_collision_named",
    "convention_literal_collision",
    "neither_helper_wrong",
    "imposed_object_banner",
    "nothing_registered",
    "measured_never_registered",
    "axioms_quoted_never_edited",
    "owner_decision",
    "cross_lane_quoted_never_adopted",
    "converge_dont_borrow",
    "not_an_execution_input",
    # --- W1: the wall and the two open items ---------------------------------
    "w1",
    "axiom_clause_verbatim",
    "open_gates_content",
    "parent_block",
    "their_pr_number",
    "their_selected_law_quoted",
    "their_open_item_quoted",
    "their_open_item_prose_quoted",
    "our_open_item_named",
    # --- N1: the identity ----------------------------------------------------
    "sdiag_precondition",
    "off_diagonal_empty",
    "ambient_rows",
    "classical_density",
    "density_denominator",
    "identity_defect",
    "entry_for_entry",
    "two_routes",
    "same_object",
    "marginal_only",
    "not_every_law",
    # --- N2: the split -------------------------------------------------------
    "conditional_law",
    "four_deltas",
    "common_denominator_k",
    "all_deltas_nonzero",
    "delta_signs",
    "deltas_sum_zero",
    "delta_brackets",
    "two_distinguished_objects",
    "sharp_surviving_form",
    "not_a_discrepancy",
    "own_witness",
    # --- N3: additivity ------------------------------------------------------
    "partitions_declared",
    "union_effects_orthogonal",
    "trace_additive_natively",
    "trace_defect_zero",
    "no_primitive_union_pin",
    "one_scalar_per_cell",
    "key_collapse",
    "representative_not_union",
    "pushforward_definitional",
    "pushforward_defect_zero",
    "not_merge_closure",
    "b172_scoped",
    # --- N4: the joint cage --------------------------------------------------
    "joint_cage",
    "one_question_two_families",
    "effect_level",
    "amplitude_level",
    "gleason_flagged_not_asserted",
    "new_bar",
    "constraint_not_closure",
    # --- N8: the scoped verdict and the disclosures --------------------------
    "no_selection_principle",
    "successor_question",
    "bridge_not_yet_earned",
    "cycle913_caution",
    "non_supply_never_necessity",
    "candidacy_never_nature",
    "worker_profile",
    "supervisor_designed_probe",
    "owner_pointer",
    "predictions_registered_first",
    "codex_execution",
    "cross_model_chain_carried",
    "common_mode",
    "one_fixture",
    "not_re_verified",
    "not_continuum",
    "os_no_go",
    "not_a_born_derivation",
    "no_priority_claim",
    "n1_n8",
    "n5_verbatim",
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

CAGE_KEYS = ("joint_cage", "one_question_two_families", "effect_level",
             "amplitude_level", "new_bar", "constraint_not_closure")


def scope_certificate(note_text: str) -> dict:
    note = normalized_note(note_text)
    cage = measure_cage(note_text)
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
        "axioms_quoted_never_edited": "the axioms file is quoted" in note
        and "never edited" in note,
        "owner_decision": "the owner's" in note,
        "cross_lane_quoted_never_adopted": "quoted and never adopted" in note,
        "converge_dont_borrow": "converge-don't-borrow" in note,
        "not_an_execution_input": "not an execution input" in note
        and cage["not_an_execution_input"],
        # --- W1 ---------------------------------------------------------------
        "w1": __import__("re").search(r"\bw1\b", note) is not None,
        "axiom_clause_verbatim": normalized_note(AXIOM_CLAUSE) in note,
        "open_gates_content": "open-gates content" in note,
        "parent_block": "block 174" in note,
        "their_pr_number": cage["their_pr_cited"] and cage["their_note_named"],
        "their_selected_law_quoted": cage["selected_law_quoted"],
        "their_open_item_quoted": cage["open_item_quoted"],
        "their_open_item_prose_quoted": cage["open_prose_quoted"],
        "our_open_item_named": cage["our_open_item_named"],
        # --- N1 ---------------------------------------------------------------
        "sdiag_precondition": "s-diag" in note and "precondition" in note,
        "off_diagonal_empty": "off-diagonal support is empty exactly" in note,
        "ambient_rows": "(20, 21, 22, 23)" in note,
        "classical_density": "classical density" in note,
        "density_denominator": str(DENSITY_DENOMINATOR) in note_text,
        "identity_defect": "(0,0,0,0)" in note or "(0, 0, 0, 0)" in note,
        "entry_for_entry": "entry for entry" in note,
        "two_routes": "two independent routes" in note,
        "same_object": "the same object" in note,
        "marginal_only": "marginal record-slice object" in note,
        "not_every_law": "not of every law" in note
        or "not an identification of every law" in note,
        # --- N2 ---------------------------------------------------------------
        "conditional_law": "formation-conditional" in note,
        "four_deltas": "all four entries" in note,
        "common_denominator_k": str(DELTA_DENOMINATOR) in note_text,
        "all_deltas_nonzero": "exactly nonzero" in note,
        "delta_signs": "(+, -, -, +)" in note,
        "deltas_sum_zero": "sum_a delta_a = 0" in note,
        "delta_brackets": "1076303/100000000" in note,
        "two_distinguished_objects":
            "two distinguished exact probability objects" in note,
        "sharp_surviving_form": "sharp surviving form" in note,
        "not_a_discrepancy": "not a discrepancy" in note,
        "own_witness": "own witness" in note,
        # --- N3 ---------------------------------------------------------------
        "partitions_declared": "{{0}, {1/5, 2/5}, {3/5}}" in note,
        "union_effects_orthogonal": "orthogonal projectors" in note,
        "trace_additive_natively": "natively additive" in note,
        "trace_defect_zero": "(0,0,0)" in note or "(0, 0, 0)" in note,
        "no_primitive_union_pin": "no primitive value-union pin" in note
        or "no\nprimitive value-union pin" in note
        or "no primitive\nvalue-union pin" in note,
        "one_scalar_per_cell": "one scalar" in note,
        "key_collapse": "collapses to one" in note,
        "representative_not_union": "choosing a representative is not a union"
        in note,
        "pushforward_definitional": "definitional pushforward" in note
        or "pushforward" in note and "by definition" in note,
        "pushforward_defect_zero": "defect vectors are" in note,
        "not_merge_closure": "action-level merge closure" in note,
        "b172_scoped": "block 172" in note and "conjunction" in note,
        # --- N4 ---------------------------------------------------------------
        "joint_cage": "joint cage" in note,
        "one_question_two_families": cage["one_question_two_families"],
        "effect_level": "effect level" in note,
        "amplitude_level": "amplitude level" in note,
        "gleason_flagged_not_asserted": cage["gleason_flagged_not_asserted"],
        "new_bar": "new bar" in note,
        "constraint_not_closure": "constraint statement" in note,
        # --- N8 ---------------------------------------------------------------
        "no_selection_principle": "no selection principle is supplied" in note,
        "successor_question": "successor question" in note,
        "bridge_not_yet_earned": "not yet earned" in note,
        "cycle913_caution": "cycle913" in note,
        "non_supply_never_necessity":
            "non-supply within this formalism" in note
            and "never metaphysical necessity" in note,
        "candidacy_never_nature": "candidacy within this formalism" in note
        and "never a claim about nature" in note,
        "worker_profile": "worker profile" in note,
        "supervisor_designed_probe": "supervisor-designed probe" in note,
        "owner_pointer": "owner's pointer" in note,
        "predictions_registered_first":
            "registered before the arithmetic" in note,
        "codex_execution": "codex 5.6-sol xhigh" in note,
        "cross_model_chain_carried":
            "cross-model verification chain from block 174" in note,
        "common_mode": "common-mode" in note,
        "one_fixture": "one fixture" in note,
        "not_re_verified": "not re-verified" in note,
        "not_continuum": "not a continuum statement" in note,
        "os_no_go": "not an os no-go" in note,
        "not_a_born_derivation": "not a derivation of the born rule" in note,
        # NEGATIVE key.  A block that returns an exact cross-lane identity is a
        # place where an originality claim would be cheap, so the guard is kept
        # exactly as Blocks 164-174 landed it.
        "no_priority_claim": ("first positive" not in note
                              and "novel" not in note
                              and "unprecedented" not in note
                              and "for the first time" not in note),
        "n1_n8": all(__import__("re").search(rf"\bn{index}\b", note) is not None
                     for index in range(1, 9)),
        # Raw substring membership makes the printed fence byte-identical to its
        # note occurrence.
        "n5_verbatim": N5_FENCE in note_text,
        "ast_surface_disclosed": "ast surface" in note,
        "no_float": "no float" in note,
        "scope_key_certificate": "scope-key certificate" in note,
        # NEGATIVE key, inherited from Blocks 164-174.
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
        "campaign_cited": "campaign_20260820_48h" in note,
    }


# ---------------------------------------------------------------------------
# the pinned expectations
# ---------------------------------------------------------------------------
EXPECTED_HERMQ_12x4 = (24, 0, 0)
EXPECTED_CONVENTION = (((4, 4, 0), (4, 0, 4)),
                       ((4, 0, 4), (4, 4, 0)),
                       ((0, 3, 0), (0, 0, 3)))
EXPECTED_OFF_DIAGONAL_ENTRIES = 0
EXPECTED_ZERO_DEFECT = (Z0, Z0, Z0, Z0)
EXPECTED_PARTITION_DEFECT = (Z0, Z0, Z0)

N5_FENCE = 'N5: per_element: THE INERTIA-CONVENTION BANNER, FIRST AND WITH TEETH. Every triple in this note is labelled: the note reads inertia in the (n_+, n_-, n_0) order of the LANDED Block 165 helper real_symmetric_inertia and stamps that convention inline on EVERY triple; the landed b163/b164 helper congruence_inertia returns (n_+, n_0, n_-), measured on identical matrices, so THE LITERAL STRING (4,4,0) MEANS PSD in Block 164\'s landed fence and FULLY HYPERBOLIC here. NEITHER HELPER IS WRONG and no landed verdict changes; the corpus-wide audit stays queued to pool 2 WITH TEETH. AND THE SECOND BANNER, THE IMPOSED-OBJECT BANNER: NOTHING HERE IS REGISTERED, ADOPTED OR PROPOSED -- the classical density C, the projector effects, the two menu partitions and their union effects, the pushforward extension of the atomic determinant weights, and the inherited menu, class map CM-SITE, record-extension wiring, slot order, record-slice scope and W9 are IMPOSED MEASURED OBJECTS OF THIS BLOCK; THE AXIOMS FILE IS QUOTED AND NEVER EDITED; AND THE PARALLEL LANE\'S NOTE IS QUOTED AS AN IN-REPO REFERENCE AND IS NEVER ADOPTED, NEVER EDITED, NEVER TREATED AS AUTHORITY AND NEVER RE-RUN -- every object here is rebuilt on THIS lane\'s committed fixtures, which is the standing converge-don\'t-borrow directive applied literally, and the bridge decision is THE OWNER\'S.\nper_site: THE IDENTITY, AND ITS PRECONDITION IS MEASURED FIRST. On the committed 12x4 bench at read slice t* = 5 the W9 record-slice block occupies ambient rows and columns (20,21,22,23) and ITS OFF-DIAGONAL SUPPORT IS EMPTY EXACTLY -- all twelve off-diagonal entries expand to exactly 0 -- so the normalized block is a diagonal, Hermitian, unit-trace, strictly positive CLASSICAL DENSITY C over the menu, displayed inline with common denominator D = 894555786619317339421650665156104028453509785664333673843970497575127328208. THEN THE TRACE LAW Tr(C E_j) WITH E_j = |j><j| IN CM-SITE ORDER EQUALS THE LANDED W9 MARGINAL PROFILE ENTRY FOR ENTRY, EXACT DEFECT (0,0,0,0), with the profile recomputed by TWO INDEPENDENT ROUTES that are gated to agree before either is compared. THE READING: THE TWO LANES COMPUTE THE SAME OBJECT AT THEIR INTERFACE -- the Born-trace reading of this kernel\'s record slice IS the marginal profile -- and the S-DIAG classicality is the precondition that lets them meet at all.\nper_mode: THE SPLIT, EXACT IN ALL FOUR ENTRIES. The formation-conditional normalized |det Q(sigma_(2,0) = a)|^-2 law at the free record cell (2,0) differs from the trace/marginal law in EVERY entry: four exact nonzero rational deltas over the displayed common denominator K, signs (+,-,-,+), sum exactly zero as the normalization control requires, and absolute brackets [1076303/100000000,67269/6250000], [3193801/100000000,1596901/50000000], [49979/20000000,31237/12500000] and [2367393/100000000,1183697/50000000]. THE FRAMEWORK THEREFORE CARRIES TWO DISTINGUISHED EXACT PROBABILITY OBJECTS AT ONE FIXTURE, the Born-trace MARGINAL and the FORMATION CONDITIONAL, and THE MARGINAL-VERSUS-CONDITIONAL DISTINCTION IS THE SHARP SURVIVING FORM OF THE READOUT QUESTION. This is not a discrepancy and not a defect in either lane -- a marginal and a conditional are different objects -- and IT IS THIS BLOCK\'S OWN WITNESS THAT THE IDENTIFICATION IS OF THE MARGINAL ONLY, since the conditional is generated by the same committed action and the identity fails on it.\nper_block: ADDITIVITY, HONESTLY SPLIT. THE TRACE LAW IS NATIVELY ADDITIVE because union effects are OPERATOR SUMS and the trace is LINEAR: on both declared three-outcome partitions P1 = {{0},{1/5,2/5},{3/5}} and P2 = {{0,1/5},{2/5},{3/5}} the union effects are measured to be orthogonal projectors resolving the identity and the exact defect vectors are (0,0,0) and (0,0,0). THE DETERMINANT LAW\'S COARSE ADDITIVITY IS A DEFINITIONAL PUSHFORWARD: the machinery defines only ATOMIC weights and NO PRIMITIVE VALUE-UNION PIN EXISTS, which is measured three ways -- the landed field builder maps a cell to ONE scalar, two values at one dictionary key COLLAPSE to one and are therefore not a pin, and a set at a record key sympifies to a FiniteSet that is not a number and so is not a shear value -- so w(U) = sum_{a in U} w(a) reproduces sum_{a in U} p_det(a) at defect (0,0,0) on both partitions BY DEFINITION, AND THIS DOES NOT SHOW ACTION-LEVEL MERGE CLOSURE. The Block 172 nonclosure concerns definable multi-cell CONJUNCTION pins and not mutually exclusive value alternatives at one cell; it is SCOPED HERE AND NEITHER STRENGTHENED NOR WEAKENED.\nlattice_wide: THE JOINT CAGE, AND IT IS A CONSTRAINT STATEMENT AND NOT A CLOSURE. The parallel record-born-composition lane, PR #7316, carries the SELECTED rule assigning Tr(C E_j) and names "trace-Law selection from the four axioms" as NOT DERIVED, quoted VERBATIM here; Block 174 names the READOUT PRINCIPLE as this lane\'s missing input. ANY PROPOSED SELECTION OR READOUT PRINCIPLE MUST NOW SURVIVE BOTH LANES\' FIXTURES AT ONCE: their refinement additivity, 24-rotation covariant decoding, normalization, pure endpoints and prefix marginals at the EFFECT level, and this lane\'s EXACT RATIONALITY, CHART SENSITIVITY on the L2 period-2 fingerprint, SCREENED LOCALITY with its exactly nonzero finite-width twin gap and geometric tail, and LEVEL INDEXING at the AMPLITUDE level -- plus the new bar this block adds, that it must say WHICH of the marginal and the conditional the Admissibility clause names, or derive one from the other. THEIR M_2(C) carriers are dimension 2 where Gleason does not apply and this lane\'s S-DIAG classicality is the same wall from the other side: FLAGGED as a structural resonance, NOT asserted as a theorem.\nper_scope: THE SCOPE, AND EVERY BOUND ON IT. ONE FIXTURE: the committed 12x4 bench, T_cover = 12 and T_phys = 6, xgraded carrier at sigma = 3/5, region pin c = 1, s_t = 0, s_x = 3/5, m = 1, read slice t* = 5, the single free record cell (2,0), the four-value menu and CM-SITE -- no width ladder, no level ladder and no second fixture is run here. THE S-DIAG CLASSICALITY IS A MEASURED PROPERTY OF THIS SLICE and is not proved to hold elsewhere, so the classical-density reading is not claimed away from it. THE OTHER LANE\'S RESULTS ARE QUOTED AND NOT RE-RUN: nothing in the runner reads that lane\'s file, it is deliberately NOT an execution input, and every statement about that lane is a QUOTATION and never a verification. NO SELECTION PRINCIPLE IS SUPPLIED, no law is derived, no law is preferred, and NOTHING IS REGISTERED, ADOPTED OR PROPOSED.\nRESULT: THE TWO LANES COMPUTE THE SAME OBJECT AT THEIR INTERFACE, AND THE READOUT QUESTION IS NOW A TWO-OBJECT QUESTION IN A JOINT CAGE. The Born-trace reading of this lane\'s W9 record slice IS this lane\'s marginal profile, exactly, defect (0,0,0,0), on a slice whose off-diagonal support is EMPTY EXACTLY. IT IS AN IDENTIFICATION OF THE MARGINAL RECORD-SLICE OBJECT AND OF NOTHING ELSE, and the block supplies its own counterexample to any wider reading, since the formation-conditional law the same action generates differs in ALL FOUR entries at exact nonzero rational deltas summing to zero. THE TRACE LAW IS NATIVELY ADDITIVE AND THE DETERMINANT LAW\'S COARSE ADDITIVITY IS DEFINITIONAL, with no primitive value-union pin measured to exist. THE TWO LANES\' OPEN ITEMS -- their trace-Law selection, our readout principle -- ARE ONE QUESTION WITH TWO EXACT OBJECT FAMILIES, and any candidate principle must survive both fixture sets. NO SELECTION PRINCIPLE IS SUPPLIED AND NOTHING IS REGISTERED. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE, THE IDENTITY INCLUDED, IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\nDECISION_CUT: NOTHING IS REGISTERED, ADOPTED OR PROPOSED. No premise-class change is registered; no landed note is edited; no earlier block is corrected; THE AXIOMS FILE IS QUOTED AND NEVER EDITED; THE PARALLEL LANE\'S NOTE IS QUOTED AND NEVER ADOPTED. THIS BLOCK\'S OWN DEFECTS ARE DISCLOSED: it is ONE FIXTURE and no ladder; the S-DIAG precondition is measured at one slice only; the determinant law\'s coarse additivity is definitional and is reported as such; the other lane is quoted and never verified, so the cross-lane half of the cage rests on quotation; no selection principle is supplied, so the joint cage constrains and does not close; and the AST surface is this runner plus the imported runner chain and NOT every landed module the chain reaches, with the residual sites outside that surface counted and reported rather than claimed repaired. PROVENANCE: CAMPAIGN_20260820_48H.md and the generator-program thread PANEL7_FABLE_THREAD.md, Addenda 7-8. HANDOFF: select-or-relate the marginal and the conditional; the in-framework averaging probe; the S-DIAG survival probe away from the read slice.\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero.'


def build_claims(mutation: str) -> dict:
    claims: dict = {
        "main_head": CURRENT_MAIN,
        "parent_pin": "resolved",
        "sdiag_off_diagonal_empty": True,
        "cross_lane_adopted": False,
        "identity_source": "measured",
        "identity_defect_zero": True,
        "det_law_equals_trace": False,
        "deltas_sum_zero": True,
        "det_additivity_is_structural": False,
        "trace_additivity_exact": True,
        "their_selection_open": True,
        "quotations_verbatim": True,
        "identity_all_laws": False,
        "required_scope_keys": SCOPE_KEYS,
    }
    if mutation == "stale_main_authority":
        claims["main_head"] = STALE_MAIN
    elif mutation == "stale_parent_authority":
        claims["parent_pin"] = "stale"
    elif mutation == "claim_offdiagonal_support_nonempty":
        # THE S-DIAG PRECONDITION DENIED: the record-slice block asserted to
        # carry off-diagonal support, which twelve exact zero expansions forbid.
        claims["sdiag_off_diagonal_empty"] = False
    elif mutation == "claim_cross_lane_note_adopted":
        # THE DISCIPLINE DENIED: the other lane's note asserted ADOPTED rather
        # than quoted, which zero registered and zero adopted objects forbid.
        claims["cross_lane_adopted"] = True
    elif mutation == "break_identity":
        # THE IDENTITY BROKEN AT THE STATE: gate C reads the PERTURBED density's
        # defect, which is exactly nonzero, instead of the measured one.
        claims["identity_source"] = "perturbed"
    elif mutation == "claim_identity_defect_nonzero":
        # THE IDENTITY DENIED OUTRIGHT: a nonzero defect asserted, which the
        # exact entry-for-entry equality forbids.
        claims["identity_defect_zero"] = False
    elif mutation == "claim_det_law_equals_trace":
        # THE SPLIT DENIED: the conditional law asserted equal to the marginal,
        # which four exactly nonzero deltas forbid.
        claims["det_law_equals_trace"] = True
    elif mutation == "claim_deltas_sum_nonzero":
        # THE NORMALIZATION CONTROL DENIED: the deltas asserted not to sum to
        # zero, which two laws normalized on the same menu forbid.
        claims["deltas_sum_zero"] = False
    elif mutation == "claim_det_additivity_structural":
        # THE HONEST LABEL DENIED: the determinant pushforward asserted to be
        # action-level closure, which the measured absence of any primitive
        # value-union pin forbids.
        claims["det_additivity_is_structural"] = True
    elif mutation == "claim_trace_additivity_defective":
        # THE NATIVE ADDITIVITY DENIED: a nonzero trace-law refinement defect
        # asserted, which operator sums and trace linearity forbid.
        claims["trace_additivity_exact"] = False
    elif mutation == "claim_their_selection_closed":
        # THE OTHER LANE'S OPEN ITEM ASSERTED CLOSED, which their own quoted row
        # -- "not derived" -- forbids.
        claims["their_selection_open"] = False
    elif mutation == "break_quotation_integrity":
        # QUOTATION INTEGRITY DENIED: the quoted passages asserted absent from
        # this note, which reading the note forbids.
        claims["quotations_verbatim"] = False
    elif mutation == "claim_identity_all_laws":
        # THE SCOPE BROKEN: the identification asserted to extend beyond the
        # marginal to every law the action generates, which this block's own
        # four nonzero deltas forbid.
        claims["identity_all_laws"] = True
    elif mutation == "drop_joint_cage":
        # THE CAGE DROPPED from the required scope, which gate H forbids -- the
        # FULL key set is required, not a subset.
        claims["required_scope_keys"] = tuple(
            key for key in SCOPE_KEYS if key not in CAGE_KEYS)
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
    sdiag: dict
    identity: dict
    split: dict
    additivity: dict
    cage: dict
    exact_no_float: bool
    source_files: int
    source_floats: int
    source_forbidden: int


def evaluate_gates(facts: Facts, claims: dict, elapsed_ns: int) -> dict:
    authority = facts.authority
    parent_blobs_ok = (authority.parent_artifact_blobs
                       if claims["parent_pin"] == "resolved"
                       else authority.stale_parent_artifact_blobs)
    gate_a = bool(
        AUDIT_INPUT_PATHS == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_PINCER_IDENTITY_CROSS_LANE_BOUNDED_THEOREM_NOTE_2026-08-22.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_CONDITIONAL_LAW_FAMILY_BOUNDED_THEOREM_NOTE_2026-08-22.md",
            "scripts/admissibility_dirac_kahler_site_conditional_law_family_2026_08_22.py",
        )
        and PARENT_ARTIFACTS == (BLOCK174_NOTE, BLOCK174_RUNNER)
        and len(PARENT_ARTIFACT_BLOBS) == len(PARENT_ARTIFACTS) == 2
        and facts.main_head == claims["main_head"]
        and authority.fixed_authority
        and authority.parent_import_landed
        and authority.parent_pin_is_commit
        and authority.parent_ref_and_ancestry
        and parent_blobs_ok
        # THE STALE PIN: a REAL ancestor of HEAD that carries NEITHER Block 174
        # artifact, which is exactly what makes the stale mutation bite.
        and authority.stale_is_real_ancestor
        and authority.stale_carries_neither_artifact)

    ban = facts.banners
    conv = ban["convention"]
    bench = ban["bench"]
    sd = facts.sdiag
    gate_b = bool(
        # THE CONVENTION COLLISION, MEASURED on identical matrices.
        conv["pairs"] == EXPECTED_CONVENTION
        and conv["landed_psd"] and conv["here_psd"] and conv["orders_differ"]
        and conv["instrument_agree"][0] == conv["instrument_agree"][1]
        # THE IMPOSED-OBJECT BANNER, as a measured object, and the cross-lane
        # discipline as a mechanical one.
        and ban["imposed_objects"] == 8
        and ban["registered_objects"] == 0
        and ban["adopted_objects"] == 0
        and ban["owner_decisions"] == 1
        and ban["axiom_clause_is_verbatim"]
        and ban["cross_lane_not_an_execution_input"]
        and (ban["registered_objects"] == 0 and ban["adopted_objects"] == 0
             and ban["cross_lane_not_an_execution_input"])
        == (not claims["cross_lane_adopted"])
        # THE BENCH ANCHOR and the determinant-route gate.
        and bench["q_symbol_free"] and bench["field_matches_landed"]
        and bench["inverse_residual_zero"] and bench["congruence_zero"]
        and bench["hermq_inertia"] == EXPECTED_HERMQ_12x4
        and bench["det_routes_agree"] and bench["det_nonzero"]
        and bench["menu_is_sigma_classes"] and bench["menu_matches_parent"]
        and bench["tstar_is_five"] and bench["N"] == 24
        # THE S-DIAG PRECONDITION, measured before any trace is read.
        and sd["env_tstar"] == TSTAR
        and sd["ambient_rows"] == AMBIENT_ROWS
        and sd["off_diagonal_entries"] == EXPECTED_OFF_DIAGONAL_ENTRIES
        and sd["diagonal_all_positive"]
        and sd["off_diagonal_empty"] == claims["sdiag_off_diagonal_empty"]
        and facts.exact_no_float
        and facts.source_floats == 0 and facts.source_forbidden == 0
        and facts.source_files >= 2)

    ident = facts.identity
    defect_zero = (ident["defect_zero"] if claims["identity_source"] == "measured"
                   else ident["perturbed_defect_zero"])
    gate_c = bool(
        # THE TWO ROUTES AGREE BEFORE ANYTHING IS COMPARED.
        ident["rows_match_env"] and ident["routes_agree_block"]
        and ident["routes_agree_profile"]
        # C IS A DENSITY.
        and ident["hermitian"] and ident["unit_trace"] and ident["all_positive"]
        and ident["density_numerators"] == DENSITY_NUMERATORS
        and ident["density_denominator"] == DENSITY_DENOMINATOR
        # THE IDENTITY.
        and ident["trace_law"] == ident["landed_law"]
        and tuple(ident["defect"]) == EXPECTED_ZERO_DEFECT
        # AND THE PERTURBED CONTROL IS EXACTLY NONZERO, so break_identity has
        # something real to break.
        and not ident["perturbed_defect_zero"]
        and defect_zero == claims["identity_defect_zero"]
        and facts.exact_no_float)

    sp_ = facts.split
    gate_d = bool(
        sp_["cell"] == RECORD_CELL
        and sp_["dets_nonzero"] and sp_["raw_positive"]
        and sp_["det_law_normalized"] and sp_["det_law_positive"]
        # THE FOUR EXACT DELTAS against the embedded literals.
        and sp_["literals_agree"]
        and sp_["signs_agree"]
        and sp_["brackets_agree"]
        # THE SPLIT ITSELF, and the sum-zero arithmetic control.
        and sp_["all_deltas_nonzero"] == (not claims["det_law_equals_trace"])
        and sp_["sum_zero"] == claims["deltas_sum_zero"]
        and ((sp_["deep_det_routes"] and sp_["deep_routes_agree"])
             if facts.deep else True)
        and facts.exact_no_float)

    add = facts.additivity
    union = add["union"]
    gate_e = bool(
        len(add["partitions"]) == 2
        and add["effects_are_projectors"]
        and all(tuple(p["trace_defect"]) == EXPECTED_PARTITION_DEFECT
                for p in add["partitions"])
        and all(tuple(p["det_defect"]) == EXPECTED_PARTITION_DEFECT
                for p in add["partitions"])
        and add["det_defects_zero"]
        # THE NO-PRIMITIVE-UNION-PIN STATEMENT, measured three ways.
        and union["field_source_scalar_lookup"]
        and union["field_source_sympifies_scalar"]
        and union["key_collapse_length"] == 1
        and union["key_collapse_keeps_last"]
        and union["set_is_not_a_number"]
        and union["no_union_api"]
        and add["b172_is_conjunction_scoped"]
        and not add["shows_merge_closure"]
        and add["trace_defects_zero"] == claims["trace_additivity_exact"]
        and add["pushforward_is_definitional"]
        == (not claims["det_additivity_is_structural"])
        and facts.exact_no_float)

    cage = facts.cage
    gate_f = bool(
        # THE CAGE, stated in the note on both sides.
        cage["their_items_present"] and cage["our_items_present"]
        and cage["one_question_two_families"]
        and cage["their_pr_cited"] and cage["their_note_named"]
        and cage["our_open_item_named"]
        and cage["gleason_flagged_not_asserted"]
        # THE DISCIPLINE, mechanically: their note is never an execution input.
        and cage["not_an_execution_input"]
        # THE TWO CLAIM-BOUND LEGS.
        and cage["their_item_open"] == claims["their_selection_open"]
        and cage["quotations_verbatim"] == claims["quotations_verbatim"])

    sc = facts.scope
    gate_g = bool(
        # SCOPE DISCIPLINE, in the note.
        sc["marginal_only"] and sc["not_every_law"]
        and sc["no_selection_principle"] and sc["successor_question"]
        and sc["own_witness"] and sc["one_fixture"]
        # AND THE MEASURED WITNESS to the disclaimer: the conditional law is a
        # law this same action generates and the identity FAILS on it.
        and facts.split["all_deltas_nonzero"]
        and facts.identity["extends_to_all_laws"] == claims["identity_all_laws"]
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
        # THE FULL KEY SET IS REQUIRED, not a subset.  That is what gives the
        # two drop mutations their teeth once the note is landed.
        and required == SCOPE_KEYS
        and all(facts.scope[key] for key in required)
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
        and POOL_TWO_LEADS == 4
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
    banners = {
        "convention": measure_convention(),
        "bench": measure_bench(),
        "imposed_objects": len(IMPOSED_OBJECTS),
        "registered_objects": len(REGISTERED_OBJECTS),
        "adopted_objects": len(ADOPTED_OBJECTS),
        "owner_decisions": len(OWNER_DECISIONS),
        "axiom_clause_is_verbatim": normalized_note(AXIOM_CLAUSE) in
        normalized_note((ROOT / AXIOM_PATH).read_text(encoding="utf-8")),
        "cross_lane_not_an_execution_input": not any(
            THEIR_NOTE_NAME in path for path in AUDIT_INPUT_PATHS),
    }
    sdiag = measure_sdiag()
    identity = measure_identity(sdiag)
    split = measure_split(identity, deep)
    additivity = measure_additivity(identity, split)
    cage = measure_cage(note_text)
    for value in identity["trace_law"]:
        record(value)
    for value in identity["density"]:
        record(value)
    for value in split["deltas"]:
        record(value)
    for value in split["det_law"]:
        record(value)
    for partition in additivity["partitions"]:
        for value in partition["trace_coarse"]:
            record(value)
        for value in partition["det_induced"]:
            record(value)
    return Facts(
        deep=deep,
        main_head=main_head,
        authority=authority_certificate(main_head),
        note_at_final_path=at_final_path,
        scope=scope_certificate(note_text),
        banners=banners,
        sdiag=sdiag,
        identity=identity,
        split=split,
        additivity=additivity,
        cage=cage,
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
        help="run the four pinned determinants by BOTH exact routes -- "
             "DomainMatrix fraction-field elimination and Berkowitz -- rather "
             "than gating the two routes on the bench matrix alone; the "
             "baseline runs the disclosed single route per pin and the runtime "
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

    ban, sd = facts.banners, facts.sdiag
    ident, spl = facts.identity, facts.split
    add, cage = facts.additivity, facts.cage
    conv, bench = ban["convention"], ban["bench"]
    res = facts.authority.residue

    print("MEASURED, before any gate is read:")
    print(f"  PARENT IMPORT: the Block 174 runner imported "
          f"{facts.authority.parent_import_landed}; PARENT_COMMIT "
          f"{PARENT_COMMIT} is REAL and PARENT_REF resolves to it. "
          f"CURRENT_MAIN was RE-RESOLVED at draft time to {CURRENT_MAIN}")
    print(f"  THE STALE PIN: {STALE_PARENT_COMMIT[:12]} is a REAL ancestor of "
          f"HEAD {facts.authority.stale_is_real_ancestor} and carries NEITHER "
          f"Block 174 artifact {facts.authority.stale_carries_neither_artifact}"
          f" -- it is the Block 173 hygiene tip, which PREDATES both artifacts, "
          f"and that absence is exactly what makes the stale_parent_authority "
          f"mutation bite. AND THE HYGIENE RESIDUE IS COUNTED, NOT HIDDEN, as "
          f"(text mentions, LIVE CALL SITES): {res['per_module']}, which is "
          f"{record(res['call_sites_in_audit_surface'])} live call sites inside "
          f"this runner's AST audit surface and "
          f"{record(res['call_sites_below_audit_surface'])} BELOW it, in landed "
          f"modules the chain reaches transitively. REPORTED, and NEVER claimed "
          f"repaired")
    print(f"  THE NOTE: read at its FINAL PATH {facts.note_at_final_path} -- "
          f"when False this is an UNLANDED DRAFT reading the DECLARED FALLBACK "
          f"{DRAFT_NOTE_PATH.name}, gate H is EXPECTED to fail, and the two "
          f"gate-H mutations are UNTESTABLE until the note lands; gates A-G "
          f"are unaffected.  Scope keys satisfied: "
          f"{sum(1 for v in facts.scope.values() if v)} of "
          f"{len(facts.scope)}; unsatisfied "
          f"{tuple(key for key, value in facts.scope.items() if not value)}")
    print(f"  THE INERTIA CONVENTION, FIRST: the landed b163/b164 helper and "
          f"the landed Block 165 helper on IDENTICAL matrices {conv['pairs']} "
          f"-- each pair (b163/b164, this note); the region normal form is PSD "
          f"under both readings ({conv['landed_psd']}, {conv['here_psd']}) and "
          f"the tuple ORDERS DIFFER {conv['orders_differ']}, so the literal "
          f"string (4,4,0) means PSD in Block 164's landed fence and FULLY "
          f"HYPERBOLIC here")
    print(f"  THE IMPOSED-OBJECT BANNER: {record(ban['imposed_objects'])} "
          f"objects built by this block or its parents, "
          f"{record(ban['registered_objects'])} registered and "
          f"{record(ban['adopted_objects'])} adopted; "
          f"{record(ban['owner_decisions'])} decision belongs to the OWNER -- "
          f"{OWNER_DECISIONS} -- the imposed objects are {IMPOSED_OBJECTS}, "
          f"THE AXIOM CLAUSE IS QUOTED VERBATIM FROM THE AXIOMS FILE "
          f"{ban['axiom_clause_is_verbatim']} and never edited, AND THE "
          f"PARALLEL LANE'S NOTE IS NOT AN EXECUTION INPUT "
          f"{ban['cross_lane_not_an_execution_input']} -- it is QUOTED TEXT in "
          f"this block's note, cited as {THEIR_PR}, and NOTHING in this runner "
          f"reads it: the converge-don't-borrow directive, applied literally")
    print(f"  THE BENCH at 12x{bench['lx']} (T_phys = {record(bench['T_phys'])}"
          f", N = {record(bench['N'])}): read slice t* = "
          f"{record(bench['tstar'])} over free levels {bench['free_levels']}; "
          f"herm(Q) reads {tri(bench['hermq_inertia'])}; the exact two-sided "
          f"inverse residual is zero {bench['inverse_residual_zero']} and the "
          f"Sylvester congruence is exact {bench['congruence_zero']}; the Q "
          f"builder matches the landed field shape "
          f"{bench['field_matches_landed']}; the DomainMatrix determinant "
          f"agrees with Berkowitz {bench['det_routes_agree']}; the menu IS the "
          f"landed SIGMA_CLASSES {bench['menu_is_sigma_classes']} and matches "
          f"the parent's {bench['menu_matches_parent']}")
    print(f"  THE S-DIAG PRECONDITION, MEASURED BEFORE ANY TRACE IS READ: the "
          f"W9 record-slice block at t* = {record(sd['env_tstar'])} occupies "
          f"ambient rows/columns {sd['ambient_rows']} and its OFF-DIAGONAL "
          f"SUPPORT IS EMPTY EXACTLY {sd['off_diagonal_empty']} at "
          f"{record(sd['off_diagonal_entries'])} nonzero off-diagonal entries "
          f"of 12, with every diagonal entry strictly positive "
          f"{sd['diagonal_all_positive']}. THAT IS WHY THE NORMALIZED BLOCK IS "
          f"A CLASSICAL DENSITY OVER THE MENU and why the two lanes can meet "
          f"here at all; it is measured AT THIS SLICE and is not claimed "
          f"elsewhere")
    print(f"  THE IDENTITY: the record-slice rows {ident['rows']} match the "
          f"landed Env rows {ident['rows_match_env']}, and the TWO INDEPENDENT "
          f"ROUTES -- the landed b171 Env block/profile and the Block 174 "
          f"Fixture rebuild -- agree on the 4x4 block "
          f"{ident['routes_agree_block']} and on the profile "
          f"{ident['routes_agree_profile']} BEFORE either is compared to "
          f"anything. C is Hermitian {ident['hermitian']}, unit-trace "
          f"{ident['unit_trace']} and strictly positive {ident['all_positive']}"
          f", with exact numerators {ident['density_numerators']} over "
          f"{record(ident['density_denominator'])}. AND Tr(C E_j) MINUS THE "
          f"LANDED W9 MARGINAL PROFILE IS {ident['defect']} -- ENTRY FOR ENTRY, "
          f"EXACTLY ZERO. THE TWO LANES COMPUTE THE SAME OBJECT AT THEIR "
          f"INTERFACE. The perturbed control at +{PERTURBATION} on C[0,0] gives "
          f"a defect that is exactly nonzero "
          f"{not ident['perturbed_defect_zero']}, so break_identity has "
          f"something real to break")
    print(f"  THE SPLIT at the free record cell {spl['cell']}: all four "
          f"determinants nonzero {spl['dets_nonzero']}, the "
          f"formation-conditional |det Q|^-2 law strictly positive "
          f"{spl['det_law_positive']} and normalized "
          f"{spl['det_law_normalized']}. THE FOUR DELTAS ARE EXACTLY NONZERO "
          f"{spl['all_deltas_nonzero']} with signs {spl['signs']} matching "
          f"{spl['signs_agree']}, common denominator "
          f"{record(spl['denominator'])}, numerators {spl['numerators']}, "
          f"reproducing the embedded literals {spl['literals_agree']}, "
          f"absolute brackets {spl['brackets']} reproducing "
          f"{spl['brackets_agree']}, AND THE SUM IS EXACTLY ZERO "
          f"{spl['sum_zero']} as normalization on a shared menu requires. THE "
          f"MARGINAL-VERSUS-CONDITIONAL DISTINCTION IS THE SHARP SURVIVING "
          f"FORM OF THE READOUT QUESTION, and it is this block's OWN WITNESS "
          f"that the identification is OF THE MARGINAL ONLY")
    for partition in add["partitions"]:
        print(f"  ADDITIVITY, PARTITION {record(partition['number'])} "
              f"{partition['partition']}: the union effects are orthogonal "
              f"{partition['orthogonal']} and resolve the identity "
              f"{partition['resolves_identity']}; THE TRACE-LAW REFINEMENT "
              f"DEFECT IS {partition['trace_defect']} -- natively additive, "
              f"because union effects are OPERATOR SUMS and the trace is "
              f"LINEAR; and the determinant pushforward defect is "
              f"{partition['det_defect']}")
    print(f"  AND THE DETERMINANT SIDE IS DEFINITIONAL, MEASURED THREE WAYS: "
          f"the landed field builder maps a cell to ONE SCALAR "
          f"{add['union']['field_source_scalar_lookup']} / "
          f"{add['union']['field_source_sympifies_scalar']}; two values at one "
          f"dictionary key COLLAPSE to "
          f"{record(add['union']['key_collapse_length'])} entry keeping the "
          f"later value {add['union']['key_collapse_keeps_last']}, so it is NOT "
          f"a simultaneous pin; and a set at a record key sympifies to a "
          f"{add['union']['set_type']}, which is not a number "
          f"{add['union']['set_is_not_a_number']} and therefore not a shear "
          f"value. No union-pin API name occurs in the parent machinery "
          f"{add['union']['no_union_api']} over {add['union']['api_names_searched']}. "
          f"SO w(U) = sum_(a in U) w(a) IS ADDITIVE BY DEFINITION OF THE "
          f"PUSHFORWARD {add['pushforward_is_definitional']} AND DOES NOT SHOW "
          f"ACTION-LEVEL MERGE CLOSURE {not add['shows_merge_closure']}; the "
          f"Block 172 nonclosure concerns definable multi-cell CONJUNCTION pins "
          f"{add['b172_is_conjunction_scoped']} and is SCOPED here, neither "
          f"strengthened nor weakened")
    print(f"  THE JOINT CAGE: the parallel lane {THEIR_PR} is cited "
          f"{cage['their_pr_cited']} and named {cage['their_note_named']}, its "
          f"SELECTED-LAW sentence is quoted VERBATIM in this note "
          f"{cage['selected_law_quoted']}, its trace-Law-selection row is "
          f"quoted VERBATIM {cage['open_item_quoted']} and its prose negative "
          f"{cage['open_prose_quoted']}; THEIR ITEM IS OPEN BY THEIR OWN WORDS "
          f"{cage['their_item_open']}, ours is named {cage['our_open_item_named']}"
          f". BOTH SIDES OF THE CAGE ARE STATED: theirs {cage['their_cage_items']} "
          f"{cage['their_items_present']}, ours {cage['our_cage_items']} "
          f"{cage['our_items_present']}, as ONE QUESTION WITH TWO EXACT OBJECT "
          f"FAMILIES {cage['one_question_two_families']}. The Gleason resonance "
          f"is FLAGGED AND NOT ASSERTED {cage['gleason_flagged_not_asserted']}. "
          f"QUOTATION INTEGRITY IS THE WHOLE CLAIM {cage['quotations_verbatim']}"
          f" -- their correctness is NOT checked and is NOT claimed, their "
          f"runner is NOT re-run, and their note is NOT an execution input "
          f"{cage['not_an_execution_input']}")
    print(f"  EXACTNESS: no float in any measured object "
          f"{facts.exact_no_float} over {record(len(NUMERALS))} numerals; the "
          f"AST scan covers {record(facts.source_files)} FILES -- this runner "
          f"AND the imported runner chain -- and finds "
          f"{record(facts.source_floats)} float literals and "
          f"{record(facts.source_forbidden)} forbidden references. THE AST "
          f"SURFACE IS DISCLOSED AND IS NOT THE FULL TRANSITIVE CLOSURE")
    print(f"  SAMPLING: --deep {facts.deep}; at baseline the two determinant "
          f"routes are gated on the bench matrix and each pinned determinant is "
          f"taken by one exact route, while --deep recomputes all four pinned "
          f"determinants by BOTH exact routes -- "
          f"{record(spl['deep_routes_checked'])} recomputed here, agreeing "
          f"{spl['deep_routes_agree']}")
    print()

    checks = Checks()
    checks.check(
        "A-authority-and-THE-STALE-PIN-THAT-PREDATES-BOTH-ARTIFACTS",
        "main plus TWO parent artifacts are content-bound -- Block 174's note and runner, which are BOTH the stack parent this block's branch is cut from AND the content parent, since this runner IMPORTS the Block 174 runner and reaches every committed convention below it through Block 174's own import chain, which Block 174's gate A pins rather than this one duplicating it -- and the gate additionally requires that the Block 174 runner ACTUALLY IMPORTED. PARENT_COMMIT IS REAL AND SO ARE BOTH ARTIFACT BLOBS: Block 174 HAS landed, so nothing needs sed at landing, and CURRENT_MAIN was re-resolved at draft time. THE FIVE-PIN AUTHORITY BLOCK binds origin/main's head, the axioms blob and the registry blob at origin/main, and the axioms and registry blobs in the worktree. AND THE STALE PIN IS THE INTERESTING ONE: it is the Block 173 nsimplify-hygiene tip, a REAL ancestor of HEAD that PREDATES Block 174 and therefore carries NEITHER Block 174 artifact, which is exactly what makes the stale_parent_authority mutation bite -- under it the gate looks for the artifact blobs at a commit where they do not exist. THE HYGIENE RESIDUE BELOW THE AUDIT SURFACE IS COUNTED AND REPORTED AND NEVER CLAIMED REPAIRED, as (text mentions, LIVE CALL SITES) per module",
        gate_values["A"])
    checks.check(
        "B-the-two-banners-the-bench-anchor-and-THE-S-DIAG-PRECONDITION",
        "THE TWO BANNERS COME BEFORE ANY NUMERAL AND BOTH ARE MEASURED RATHER THAN ASSERTED. THE INERTIA CONVENTION: called on IDENTICAL matrices, b163/b164's congruence_inertia returns (n_+, n_0, n_-) and Block 165's real_symmetric_inertia returns (n_+, n_-, n_0), so the region normal form reads (4,4,0) there and (4,0,4) here; NEITHER HELPER IS WRONG and no landed verdict changes, but THE LITERAL STRING (4,4,0) MEANS PSD IN BLOCK 164'S LANDED FENCE AND FULLY HYPERBOLIC IN THIS NOTE. THE IMPOSED-OBJECT BANNER: eight objects are imposed by this block or its parents -- the classical density C, the projector effects, the two menu partitions and their union effects, the pushforward extension of the atomic determinant weights, the inherited |det Q|^-2 readout arm, the inherited menu, CM-SITE with the record-extension wiring and slot order, and the record-slice scope with W9 -- and ZERO of them are registered and ZERO adopted, while ONE decision is the OWNER'S, and THE AXIOMS FILE IS QUOTED VERBATIM AND NEVER EDITED, verified by reading the axioms file itself. AND THE CROSS-LANE DISCIPLINE IS MECHANICAL, NOT PROMISED: the parallel lane's note is QUOTED TEXT in this block's note and is DELIBERATELY NOT AN EXECUTION INPUT -- it appears nowhere in AUDIT_INPUT_PATHS, nothing in this runner reads it, and every number here is rebuilt from THIS lane's machinery on THIS lane's fixtures, which is the standing converge-don't-borrow directive applied literally. THE BENCH ANCHOR: the Q builder's field shape matches the landed b171 field entry for entry, the two-sided inverse residual and the Sylvester congruence are exactly zero, herm(Q) reads (24,0,0)(n+,n-,n0)[b165], and the DomainMatrix fraction-field determinant is measured against Berkowitz before gate D takes a determinant law from either. AND THE S-DIAG PRECONDITION IS MEASURED BEFORE ANY TRACE IS READ: the W9 record-slice block at t* = 5 occupies ambient rows and columns (20,21,22,23) and ALL TWELVE off-diagonal entries expand to EXACTLY ZERO -- not to a small number -- with every diagonal entry strictly positive, which is what makes the normalized block a CLASSICAL DENSITY over the menu and is the reason the two lanes can meet here at all. It is measured AT THIS SLICE and is not claimed elsewhere. No float enters any measured object and the AST scan covers every file this runner reads code from in the runner chain",
        gate_values["B"])
    checks.check(
        "C-THE-IDENTITY-the-two-lanes-compute-THE-SAME-OBJECT-at-their-interface",
        "THE TRACE LAW APPLIED TO THIS LANE'S OWN KERNEL EQUALS THIS LANE'S OWN MARGINAL PROFILE, ENTRY FOR ENTRY, AT EXACT DEFECT (0,0,0,0). The classical density C is the normalized diagonal of the S-DIAG W9 record-slice block at t* = 5, displayed with its exact common denominator and checked to be Hermitian, unit-trace and strictly positive; the effects are E_j = |j><j| in CM-SITE order; and the comparison target is the landed b171 Env.profile('W9', t*) object that Blocks 173 and 174 measured. THE EQUALITY IS NOT AN ARTEFACT OF ONE CONSTRUCTION: the 4x4 block and the profile are built by TWO INDEPENDENT ROUTES -- the landed Env route and a rebuild from the Block 174 Fixture through exact inversion and Hermitian projection -- and the gate requires the two routes to agree entry for entry BEFORE either is compared to anything. THE READING IS THAT THE BORN-TRACE READING OF THE KERNEL'S RECORD SLICE IS THE MARGINAL PROFILE, so the parallel record-born-composition lane's selected law and this lane's measured marginal are THE SAME OBJECT at their interface on this fixture -- two programs that started from different ends have been computing the same four numbers. AND THE GATE CARRIES ITS OWN NEGATIVE CONTROL: an exact rational perturbation of one diagonal entry of C is measured beside the true reading and its defect is exactly nonzero, so the break_identity mutation has something real to break rather than a vacuous claim to flip",
        gate_values["C"])
    checks.check(
        "D-THE-SPLIT-the-marginal-and-the-formation-conditional-differ-in-ALL-FOUR-entries",
        "THE FORMATION-CONDITIONAL LAW IS A DIFFERENT OBJECT FROM THE MARGINAL, EXACTLY, AT EVERY ENTRY. At the single free record cell (2,0) each menu value is pinned as one scalar, Q(sigma_(2,0) = a) is assembled on the committed fixture, its determinant is taken by exact elimination, and the normalized |det Q(a)|^-2 weights are formed: all four determinants are nonzero, all four raw weights strictly positive, and the law sums to exactly one. THE FOUR DELTAS AGAINST THE TRACE/MARGINAL LAW ARE EXACTLY NONZERO IN ALL FOUR ENTRIES, recomputed here and checked against embedded exact literals -- numerators, common denominator, signs (+,-,-,+) and absolute readability brackets -- and THEIR SUM IS EXACTLY ZERO, which is forced because both laws are normalized on the same menu and is therefore gated as an arithmetic control on the whole computation rather than reported as a discovery. THE FRAMEWORK THEREFORE CARRIES TWO DISTINGUISHED EXACT PROBABILITY OBJECTS AT ONE FIXTURE, the Born-trace MARGINAL and the FORMATION CONDITIONAL, differing by exactly computable amounts, and THE MARGINAL-VERSUS-CONDITIONAL DISTINCTION IS THE SHARP SURVIVING FORM OF THE READOUT QUESTION. IT IS NOT A DISCREPANCY AND NOT A DEFECT IN EITHER LANE -- a marginal and a conditional are different objects and are expected to differ -- and it is THIS BLOCK'S OWN WITNESS that the N1 identification is of the MARGINAL ONLY, since the conditional is generated by the same committed action and the identity fails on it. Under --deep every pinned determinant is additionally recomputed by the second exact route",
        gate_values["D"])
    checks.check(
        "E-ADDITIVITY-HONESTLY-SPLIT-native-for-the-trace-law-DEFINITIONAL-for-the-determinant-law",
        "REFINEMENT ADDITIVITY IS A REAL PROPERTY OF ONE OBJECT AND A DEFINITIONAL ONE OF THE OTHER, AND THE DIFFERENCE IS STRUCTURAL RATHER THAN NUMERICAL. On both declared three-outcome menu partitions the union effects are MEASURED to be orthogonal projectors resolving the identity, and the trace-law refinement defect is EXACTLY (0,0,0) on each: that is native additivity, because a union effect is an OPERATOR SUM and the trace is LINEAR, and it would hold for any state and any partition. THE DETERMINANT LAW HAS NO SUCH PROPERTY TO MEASURE, because the machinery defines only ATOMIC weights and NO PRIMITIVE VALUE-UNION PIN EXISTS -- which this gate MEASURES THREE WAYS rather than asserting: the landed field builder reads a record dictionary through a scalar lookup and sympifies the result into the cell's shear slot, so a cell carries ONE value; writing two menu values at the same dictionary key COLLAPSES to a single entry keeping only the later one, so it is not a simultaneous pin; and handing the cell a set rather than a scalar sympifies to a FiniteSet, which is not a number and therefore not a shear value, so no Q(sigma in U) is formed. A fourth, weaker check finds no union-pin API name anywhere in the parent machinery. THE NATURAL EXTENSION IS THEREFORE A PUSHFORWARD, w(U) = sum over the cell of the atomic weights, and its coarse defect is exactly (0,0,0) on both partitions BY DEFINITION OF THE PUSHFORWARD -- the construction assumes what it demonstrates -- SO IT IS NOT A NEW CLOSURE PROPERTY OF det Q AND IT DOES NOT SHOW ACTION-LEVEL MERGE CLOSURE. AND THE BLOCK 172 NONCLOSURE IS SCOPED AND NOT INVOKED: that result concerns definable multi-cell CONJUNCTION pins, this is a single cell with MUTUALLY EXCLUSIVE VALUE ALTERNATIVES, and nothing here strengthens or weakens it. The honest consequence is that a selection principle leaning on additivity constrains the two lanes' objects UNEQUALLY",
        gate_values["E"])
    checks.check(
        "F-THE-JOINT-CAGE-and-the-CROSS-LANE-QUOTATION-INTEGRITY",
        "THE TWO LANES' OPEN ITEMS ARE ONE QUESTION WITH TWO EXACT OBJECT FAMILIES, AND THE CROSS-LANE HALF OF THAT STATEMENT IS QUOTATION AND NEVER VERIFICATION. The parallel record-born-composition lane is cited by PR number and by filename, and THREE PASSAGES ARE QUOTED VERBATIM in this block's note and byte-checked here: its claim_scope's selected-law sentence assigning Tr(C E_j), its what-this-does-not-close row naming 'preparation-matrix calibration and trace-Law selection from the four axioms' as 'not derived', and its claim_scope's prose negative listing trace-Law selection among the things not derived. THEIR ITEM IS OPEN BY THEIR OWN WORDS and ours is the READOUT PRINCIPLE that Block 174 named, so the same gap stands at the EFFECT level there and at the AMPLITUDE level here. BOTH SIDES OF THE CAGE ARE STATED IN THE NOTE: theirs -- refinement additivity, 24-rotation covariant decoding, normalization, pure endpoints and prefix marginals; ours -- exact rationality, chart sensitivity on the L2 period-2 fingerprint, screened locality with an exactly nonzero finite-width twin gap, and level indexing -- plus the new bar this block adds, that any candidate must say WHICH of the marginal and the conditional the Admissibility clause names. THE Gleason RESONANCE IS FLAGGED AND EXPLICITLY NOT ASSERTED: their M_2(C) carriers are dimension 2 where the theorem does not apply and this lane's S-DIAG classicality is the same wall from the other side, and this note proves nothing about it. AND THE DISCIPLINE IS MECHANICAL: their note is NOT an execution input, appears nowhere in AUDIT_INPUT_PATHS, is never read by this runner, is never edited, never adopted, never treated as authority and never re-run -- this gate checks quotation INTEGRITY only, never their correctness",
        gate_values["F"])
    checks.check(
        "G-SCOPE-DISCIPLINE-an-identification-of-THE-MARGINAL-ONLY",
        "THE VERDICT IS AN IDENTIFICATION OF ONE MEASURED OBJECT AND OF NOTHING ELSE, AND THE BLOCK SUPPLIES ITS OWN COUNTEREXAMPLE TO ANY WIDER READING. The note states the identification as being of THE MARGINAL RECORD-SLICE OBJECT, states explicitly that it is NOT an identification of every law the committed action generates, names the one fixture it holds at, and carries the successor question. AND THE DISCLAIMER IS NOT ONLY PROSE: the measured witness is inside this block, because the formation-conditional law is generated by the SAME committed action and the identity FAILS on it in all four entries at exactly nonzero rational deltas. So the claim_identity_all_laws mutation is refuted by this block's own arithmetic rather than by an assertion. NO SELECTION PRINCIPLE IS SUPPLIED: the joint cage constrains a candidate and does not produce one, no law is derived and no law is preferred. NOTHING IS REGISTERED, ADOPTED OR PROPOSED, here or in the other lane, and the Block 174 semantic-bridge row is unchanged and remains NOT YET EARNED",
        gate_values["G"])
    checks.check(
        "H-note-scope-the-owner-decision-the-caution-and-the-N5-fence",
        "THE NOTE SITS AT ITS FINAL PATH AND SATISFIES EVERY REQUIRED SCOPE KEY, the required set is THE FULL KEY SET and not a subset -- which is what gives the two drop mutations their teeth once the note is landed -- the N5 fence is an N5-prefixed literal with nine labelled sections that appears BYTE-IDENTICALLY in the note, and the mutation battery is fifteen members mapped one-per-gate across A through H. THE TWO LANES COMPUTE THE SAME OBJECT AT THEIR INTERFACE, AND THE READOUT QUESTION IS NOW A TWO-OBJECT QUESTION IN A JOINT CAGE: an identification of the marginal record-slice object only, with the formation conditional differing in all four entries as this block's own witness, the trace law natively additive and the determinant law's coarse additivity definitional, and NO SELECTION PRINCIPLE SUPPLIED. THE AXIOMS FILE IS QUOTED AND NEVER EDITED, THE PARALLEL LANE'S NOTE IS QUOTED AND NEVER ADOPTED, and THE BRIDGE DECISION IS THE OWNER'S; the CYCLE913 caution is carried VERBATIM as NON-SUPPLY WITHIN THIS FORMALISM, NEVER METAPHYSICAL NECESSITY, with its positive counterpart stated too because this block returns an exact measured identity -- CANDIDACY WITHIN THIS FORMALISM, NEVER A CLAIM ABOUT NATURE. The worker profile is disclosed in full: a SUPERVISOR-DESIGNED PROBE written to the OWNER'S POINTER at the #7316 lane, with both predictions REGISTERED BEFORE THE ARITHMETIC WAS RUN; execution by a codex 5.6-sol xhigh worker; the CROSS-MODEL VERIFICATION CHAIN FROM BLOCK 174 CARRIED FORWARD onto the fixtures this block reads; an Opus mechanical draft; and supervisor review -- with common-mode risk reduced and NOT eliminated. The scope is ONE FIXTURE and no wider, and it is NOT a continuum statement, NOT an OS no-go and NOT a derivation of the Born rule; and the disclosures are complete, THIS BLOCK'S OWN DEFECTS INCLUDED -- one fixture and no ladder, the S-DIAG precondition measured at one slice, the definitional pushforward reported as definitional, the other lane quoted and never verified, and the AST surface that is the runner chain and NOT the full transitive closure -- alongside NO FLOAT anywhere, the not-re-verified list, N1 through N8, the W1 wall, the scope-key certificate, the LaTeX rho guard, the pool-2 leads, the three handoff items, zero axiom retirement, zero obligation retirement, no TOE percentage movement, a retained-positive end-to-end theory count that remains zero, and NO priority or originality wording anywhere in the note",
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
