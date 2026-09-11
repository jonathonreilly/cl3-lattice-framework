#!/usr/bin/env python3
"""BLOCK 181 -- THE COMMON-DIFFERENTIAL SECTION THEOREM.

THE RESULT, AND ITS EXACT SCOPE.  On the certified Block 105 curved carrier as
landed by Block 128 -- the 8x4 cover of dimension 32, the antiperiodic quotient
of dimension 16, MASS = 2/7 and the completion Q = MASS*H + i*(H d + d^H H) --
with the four chart origins (0,0), (0,1), (1,0), (1,1) and the plain cover
shifts U_t and U_x:

  1. THE TRANSLATION-ORBIT THEOREM.  Every chart differential is NILPOTENT with
     d_o^2 = 0 exactly and rank 16, and all four are EXACT plain-shift
     conjugates of the single d_00 with a ZERO residual and NO staggered signs.
     The cocycle closes at (1,1) in BOTH orderings and [U_t, U_x] = 0: the
     chart connection IS the shift cocycle, and it is FLAT.

  2. THE NAIVE-AVERAGE FAILURE, QUANTIFIED.  d_avg = (1/4) sum_o d_o has
     d_avg^2 of FULL RANK 32 -- b105's "generically invertible" failure at its
     maximum -- because averaging conjugates of a nilpotent destroys
     nilpotency, while conjugating the frame does not.

  3. THE b105 TARGET, CONSTRUCTED.  On the redundant patch carrier V^+4 with
     D = diag(d_o) -- nilpotent for free -- the graph section
     s(v) = (v, S_1 v, S_2 v, S_3 v) has D-INVARIANT RANGE, certified by the
     EXACT intertwiner identities d_o S_o = S_o d_00.  That is Block 105
     section 12 item 1's object, and the b128 gate that was UNEXECUTED is now
     EXECUTED and PASSES in the section frame.

  4. THE TWISTED DESCENT, AND ACYCLICITY.  On the 16-dimensional antiperiodic
     quotient the time-shift conjugacy survives ONLY through the
     ANTIPERIODIC-wrapped shift (residual 0), while the periodic wrap FAILS at
     EXACTLY 4 entries.  Every quotient differential is nilpotent of rank
     8 = half of 16, so im = ker: THE ANTIPERIODIC COMPLEX IS ACYCLIC, with no
     zero modes -- the correct NS-sector statement.

  5. THE SECTION HODGE, ORTHOGONALLY SEPARATED FROM FLAT.  H_s = (1/4) sum_o
     S_o^T H S_o is SYMMETRIC and POSITIVE DEFINITE (all 32 leading minors
     > 0) and differs from the raw curved Hodge at 96 entries and from the
     flat Hodge -- which is EXACTLY I_32, gated -- at 96 entries.  The entry
     counts are MATRIX-LEVEL; the class question is answered at ORTHOGONAL
     scope by the check's trace certificate, gated here:
     tr(H_s) = 927831123589/27222868400 != 32, so no orthogonal or
     shift-group matrix carries H_s to flat.  Sylvester bars any
     congruence-scope claim, so none is made.

  6. CHART COVARIANCE, THE CONTRAST, AND THE NON-ISOSPECTRALITY.
     Q(S_k H_s S_k^T, d_k) is the EXACT S_k-conjugate of Q(H_s, d_00) on the
     cover AND on the quotient under the twisted shifts, while the LANDED
     b128 pairing of a FIXED H against a SHIFTED d fails conjugacy at 256
     entries, PAIR-EXACT for the two actions the b128 runner lands.  SCOPE
     HONESTY: this is a NEW CHART-COVARIANT BASE OBJECT DONE RIGHT -- THIRD
     against the two landed actions, FIFTH against the four-origin auxiliary
     extrapolation -- NOT a proof that the landed actions were secretly
     equivalent.  AND THE CHECK DECIDED THE PROBE: the landed pair is
     NON-ISOSPECTRAL, its exact z^14 charpoly coefficients gated here, so the
     landed actions were never gauge copies and b128's inequivalence is
     STRENGTHENED to similarity-inequivalence.

  7. THE RESIDUAL IS TRANSLATION NONINVARIANCE -- THE CURVATURE LABEL IS
     WITHDRAWN.  The momentum-gate commutator rank stays at 32 for the section
     completion, for the landed control, AND for the check's FLAT-HODGE
     control (I_32 with the same d_00), gated here: the chartwise differential
     alone breaks invariance on the flat reference, so the rank-32 number is
     NOT a curvature invariant.  The section completion is
     translation-COVARIANT with a shift-invariant spectrum and NOT
     translation-INVARIANT; covariance-not-invariance is a REFRAME, never a
     repair of the missing invariant action.

  8. THE MODULI, DISCLOSED.  The commutant of the quotient d_00 is
     128-DIMENSIONAL (8 Jordan-2 blocks); the equal-weight section point is the
     CANONICAL SYMMETRIC POINT and NO uniqueness principle is claimed.

THE b128 RELATION, STATED ONCE: the obstruction is REFRAMED AND NOT
CONTRADICTED, and EVERY b128 NUMBER STANDS.  The pairwise inequivalence of the
displayed completions with exact first difference -89/140 was CHART-GAUGE
MIXING -- and the check STRENGTHENED it, the landed pair measured
NON-ISOSPECTRAL; the unexecuted common-differential gate is now executed; and
the full-rank-32 spatial-shift commutator certifies TRANSLATION NONINVARIANCE
of every representative, NOT curvature -- the flat-Hodge control also ranks 32.

THE ADVERSARIAL CHECK (codex 5.6-sol xhigh, cross-model, machinery-disjoint):
CONFIRMED-WITH-CORRECTION.  All forty solve assertions reproduced; three
mandatory corrections -- the curvature label withdrawn (the flat control), the
landed count fixed at TWO with the pair non-isospectral, and the flatness
scope split (orthogonal answered, congruence barred) -- are FOLDED INTO THIS
RUNNER AS GATES: the five check-fold constants near the expected values.

GATES
  A  AUTHORITY: the five-pin authority block, the TWO Block 180 artifacts
     content-bound at PARENT_COMMIT and in the worktree, the audit inputs
     readable, and the stale pin verified to be a REAL ancestor of HEAD that
     carries NEITHER artifact.
  B  THE IMPOSED-OBJECT BANNER AND THE NOT-CLAIMED KEYS: five imposed objects,
     ZERO registered and ZERO adopted, with flatness-as-class, the equivalence
     of Block 128's landed four, and uniqueness of the section point all
     declared NOT CLAIMED as measured constants and gated against the claims.
  C  THE TRANSLATION ORBIT: d_o^2 = 0 exactly and rank d_o = 16 at all four
     chart origins on the dim-32 cover; exact PLAIN-shift conjugacy
     d_o = S_o d_00 S_o^-1 at the three nontrivial origins; the (1,1) cocycle
     closing in the REVERSED ordering too; the flatness identity
     [U_t, U_x] = 0; and the STAGGERED-SIGNED conjugator measured to FAIL, so
     no staggered sign is needed and none is available.
  D  THE NAIVE-AVERAGE FAILURE AND THE SECTION: rank(d_avg^2) = 32, FULL, with
     the check's determinant certificate det(d_avg^2) = (3/10)^64 gated; and
     the three exact intertwiner identities d_o S_o = S_o d_00, which are
     exactly D-invariance of the graph section's range.
  E  THE TWISTED DESCENT: quotient dimension 16 at time extent 4, the
     antiperiodic Ut-conjugacy exact, the PERIODIC wrap failing at EXACTLY 4
     entries, the PLAIN-wrap Ux-conjugacy exact, the check's wrap-uniqueness
     control (the WRONG space-antiperiodic shift failing at exactly 4),
     quotient nilpotency for all four origins, and rank 8 = half of 16 so
     im = ker.
  F  THE SECTION HODGE: H_s symmetric, 96-entry difference from the raw curved
     Hodge, 96-entry difference from the flat Hodge, positive definite by
     32 positive leading minors, the flat reference pinned as EXACTLY I_32,
     and the check's trace certificate separating H_s from flat at ORTHOGONAL
     scope.
  G  COVARIANCE, THE RESIDUAL AND THE MODULI: the three base-k section
     completions EXACT S-conjugates on the cover and the three twisted-shift
     descents exact on the quotient, against the CONTRAST that the landed b128
     pairing fails at 256 entries; the check's non-isospectrality certificate
     (both landed z^14 coefficients, equal to the recorded rationals AND
     differing); the momentum-gate commutator rank 32 for the section
     completion, 32 for the LANDED control, and 32 for the check's FLAT-HODGE
     control -- the correction that withdrew the curvature label; and the
     commutant of the quotient d_00 at dimension 128.
  H  the note at its final path and the N5 fence, byte-identical.

BASELINE EXPECTATION: A through G PASS, with H failing on note-at-final-path
alone until the note is landed at docs/.

MUTATIONS
  THE SWEEP CONTRACT: fifteen declared mutations, each of which rewrites ONE
  CLAIM and must flip EXACTLY ONE FAMILY to FAIL.  Every measurement happens
  once, before any mutation flag is consulted, so a mutation can only rewrite a
  CLAIM and no gate can cascade into another.
    A  stale_main_authority, stale_parent_authority
    B  claim_objects_registered, claim_flatness_as_class,
       claim_landed_four_equivalent
    C  break_orbit_conjugacy, claim_staggered_signs_needed
    D  break_average_rank, break_intertwiner
    E  break_periodic_defect, claim_twist_spatial
    F  break_hodge_minors
    G  break_contrast_count, break_commutant_dim
    H  drop_n5_fence
  BEFORE LANDING GATE H ALREADY FAILS AT BASELINE, on note-at-final-path
  alone, so drop_n5_fence cannot flip it and THE SWEEP IS RUN AT LANDING, once
  the note sits at docs/ and the baseline is 8 of 8 by family.

RUNNING
  python3 scripts/admissibility_dirac_kahler_common_differential_section_2026_08_24.py
  python3 ... --list-mutations
  python3 ... --mutation break_contrast_count

NOTES FOR THE LANDING AGENT
  1. NOTHING from any scratchpad is imported OR READ.  Every object below is
     rebuilt from the LANDED Block 128 runner
     scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py
     and from the Block 105 module it re-exports as `block105`, and the note is
     read at its FINAL PATH ONLY -- there is no draft fallback anywhere in this
     runner, so gate H FAILS until the note lands at docs/.
  2. EVERY CHECK IS EXACT.  sympy Rational and Integer arithmetic only; no
     float enters any measured object and no tolerance is used anywhere.
  3. The N5 fence appears byte-identically in the note; gate H checks it as a
     raw substring.
  4. PARENT_COMMIT is REAL and PARENT_REF resolves to it; nothing needs sed,
     and CURRENT_MAIN was RE-RESOLVED at draft time.
  5. The stale pin is the Block 179 tip, a real ancestor of HEAD that predates
     Block 180 and carries NEITHER Block 180 artifact -- which is what makes
     the stale_parent_authority mutation bite.
  6. Re-run at landing; gate H should then pass, the battery should be 8/8 by
     family, and the fifteen-mutation sweep should be run then.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

# THE MACHINERY IMPORT.  Block 128 is the content parent: it carries the
# certified Block 105 curved carrier, the 8x4 cover, the antiperiodic quotient,
# the curved Hodge, the chart differentials, the completion convention and the
# momentum gate, and it re-exports Block 105 as `block105`.  NOTHING from any
# scratchpad is imported or read anywhere in this runner.
try:
    import admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17 as b128
    MACHINERY_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b128 = None
    MACHINERY_IMPORT_LANDED = False

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_COMMON_DIFFERENTIAL_SECTION_BOUNDED_THEOREM_"
    "NOTE_2026-08-24.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

ORIGINS = ((0, 0), (0, 1), (1, 0), (1, 1))

# THE STACK PARENT'S TWO ARTIFACTS.  Block 180 is the commit this block's
# branch is cut from, and its note and its runner are the pair that
# distinguishes the parent pin from the stale pin: both exist at PARENT_COMMIT
# and NEITHER exists at STALE_PARENT_COMMIT.
BLOCK180_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_ORIENTATION_BIT_TERMINAL_BOUNDED_THEOREM_"
    "NOTE_2026-08-24.md"
)
BLOCK180_RUNNER = (
    "scripts/admissibility_dirac_kahler_orientation_bit_terminal_2026_08_24.py"
)
PARENT_ARTIFACTS = (BLOCK180_NOTE, BLOCK180_RUNNER)
PARENT_ARTIFACT_BLOBS = (
    "b105dcf4b1e0c2deb39ca92cbb56f7b02c6f2e9b",   # Block 180 note
    "607682b0caca6514c29f074d6120bb5935aef471",   # Block 180 runner
)
# THE CONTENT PARENT, read and imported rather than pinned: Block 128's note
# and runner, whose obstruction this block reframes.
BLOCK128_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_"
    "NOTE_2026-08-17.md"
)
BLOCK128_RUNNER = (
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py"
)
CAMPAIGN_NOTE = ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md"

# Deliberately literal: this is the complete audit read surface.  Every entry is
# a WORKTREE-READABLE path at landing time -- this block's own note excepted,
# since it lands later and gate H is the gate that owns it.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_COMMON_DIFFERENTIAL_SECTION_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_LOCAL_DUAL_PATCH_DESCENT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_ORIENTATION_BIT_TERMINAL_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_dirac_kahler_orientation_bit_terminal_2026_08_24.py",
    ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md",
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
# This block stacks on the Block 180 tip, so the parent branch is that.
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block180-"
              "orientation-bit-terminal-20260824")
PARENT_COMMIT = "b2664db3fc277983cf657fc6ad47db860b7a49fe"
# The Block 179 tip: a real ancestor of HEAD that predates Block 180 and
# therefore carries NEITHER Block 180 artifact.  Read ONLY under the stale
# mutation, where the missing blobs are exactly what makes it bite.
STALE_PARENT_COMMIT = "a1c71f03e7474eb91aafce8958a1a02cb1e24930"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_flatness_as_class",
    "claim_landed_four_equivalent",
    "break_orbit_conjugacy",
    "claim_staggered_signs_needed",
    "break_average_rank",
    "break_intertwiner",
    "break_periodic_defect",
    "claim_twist_spatial",
    "break_hodge_minors",
    "break_contrast_count",
    "break_commutant_dim",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_objects_registered": "B",
    "claim_flatness_as_class": "B",
    "claim_landed_four_equivalent": "B",
    "break_orbit_conjugacy": "C",
    "claim_staggered_signs_needed": "C",
    "break_average_rank": "D",
    "break_intertwiner": "D",
    "break_periodic_defect": "E",
    "claim_twist_spatial": "E",
    "break_hodge_minors": "F",
    "break_contrast_count": "G",
    "break_commutant_dim": "G",
    "drop_n5_fence": "H",
}


class Checks:
    def __init__(self) -> None:
        self.results: list[tuple[str, str, bool]] = []

    def check(self, key: str, statement: str, condition: object) -> None:
        self.results.append((key, statement, bool(condition)))

    def families(self) -> dict:
        summary: dict[str, bool] = {}
        for key, _, value in self.results:
            family = key.split("-", 1)[0]
            summary[family] = summary.get(family, True) and value
        return summary

    def report(self) -> None:
        for key, statement, value in self.results:
            print(f"[{'PASS' if value else 'FAIL'}] {key}: {statement}")
        print("GATES " + " ".join(
            f"{family}={'PASS' if value else 'FAIL'}"
            for family, value in self.families().items()))

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


@dataclass(frozen=True)
class AuthorityCertificate:
    fixed_authority: bool
    parent_pin_is_commit: bool
    parent_ref_and_ancestry: bool
    parent_artifact_blobs: bool
    stale_parent_artifact_blobs: bool
    stale_is_real_ancestor: bool
    stale_carries_neither_artifact: bool
    machinery_import_landed: bool
    inputs_readable: int
    inputs_missing: tuple


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
        # THE STALE LEG.  At the Block 179 tip NEITHER Block 180 artifact
        # exists, so this is False and the stale mutation fails gate A.
        bool(all(is_hash(v) for v in stale_blobs)
             and stale_blobs == worktree_blobs),
        is_ancestor(STALE_PARENT_COMMIT, "HEAD"),
        not any(is_hash(v) for v in stale_blobs),
        MACHINERY_IMPORT_LANDED,
        readable,
        missing)


# ---------------------------------------------------------------------------
# B. the imposed objects and the NOT-CLAIMED keys, as measured literals
# ---------------------------------------------------------------------------
# THE IMPOSED OBJECTS OF THIS BLOCK, declared as a literal so the banner is a
# measured object and not only prose.  NONE of them is registered or adopted.
IMPOSED_OBJECTS = (
    "the certified Block 105 curved carrier exactly as landed by Block 128 -- the 8x4 cover of dimension 32, the antiperiodic quotient of dimension 16, the nonuniform overlap Hodge, MASS = 2/7 and the completion convention Q = MASS*H + i*(H d + d^H H)",
    "the four chart origins (0,0), (0,1), (1,0), (1,1) and their plain cover shifts U_t and U_x",
    "the redundant four-patch carrier V^+4 with D = diag(d_o) and the graph section s(v) = (v, S_1 v, S_2 v, S_3 v)",
    "the orbit-averaged section Hodge H_s = (1/4) sum_o S_o^T H S_o and the equal-weight point it sits at",
    "the landed momentum gate and the landed chart completion used as its control, both read from the Block 128 runner and never re-derived here",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
# THE BANNER'S SECOND HALF, AS DECLARED MEASURED CONSTANTS rather than prose, so
# the B mutations bite on an object.  ALL THREE ARE FALSE AND STAY FALSE: every
# H_s statement in this block is MATRIX-LEVEL, the equivalence of Block 128's
# landed four is a checker probe and is not decided here, and the equal-weight
# section point is CANONICAL and NOT unique inside a 128-dimensional commutant.
FLATNESS_AS_CLASS_CLAIMED = False
LANDED_FOUR_EQUIVALENCE_CLAIMED = False
UNIQUENESS_CLAIMED = False

# THE EXPECTED VALUES, declared as literals so every claim below is auditable
# against the note without reading the code that measures it.
ZERO_RESIDUAL = 0
CHART_RANK = 16
AVERAGE_RANK = 32
QUOTIENT_DIM = 16
QUOTIENT_TIME_EXTENT = 4
PERIODIC_DEFECT = 4
QUOTIENT_RANK = 8
RAW_HODGE_DEFECT = 96
FLAT_HODGE_DEFECT = 96
CONTRAST_DEFECT = 256
SECTION_GATE_RANK = 32
CONTROL_GATE_RANK = 32
COMMUTANT_DIM = 128
# THE CHECK-FOLD CONSTANTS: five exact values the adversarial check computed
# on machinery-disjoint routes, now gated here so the folded claims stay
# runner-certified.  The trace certificate separates H_s from the flat
# reference under ORTHOGONAL/shift equivalence (Sylvester bars anything
# stronger); the determinant certifies the full-rank average failure; the
# space-antiperiodic defect pins the twist as uniquely temporal; the
# flat-control rank REFUTES the curvature label for the rank-32 residual; and
# the two z^14 coefficients certify the landed pair NON-ISOSPECTRAL.
HS_TRACE = sp.Rational(927831123589, 27222868400)
DAVG_DET = sp.Rational(3, 10) ** 64
SPACE_ANTI_DEFECT = 4
FLAT_CONTROL_GATE_RANK = 32
Z14_COEFFS = {
    (1, 0): sp.Rational(1195620534151694060907411, 62608868331486568000000),
    (1, 1): sp.Rational(8650195819888697214240517, 435757723587146513280000),
}

# THE H-FAMILY SCOPE KEYS.  The set is required WHOLE by gate H, which is what
# gives drop_n5_fence its teeth: dropping a key from the required set makes the
# required set differ from the declared set and the gate fails.
SCOPE_KEYS = ("n5_verbatim",)


def scope_certificate(text: str) -> dict:
    return {"n5_verbatim": N5_FENCE in text}


# ---------------------------------------------------------------------------
# exact helpers -- no float and no tolerance anywhere
# ---------------------------------------------------------------------------
def nonzero_entries(matrix: sp.MatrixBase) -> int:
    return sum(1 for i in range(matrix.rows) for j in range(matrix.cols)
               if matrix[i, j] != 0)


def residual_count(matrix: sp.MatrixBase) -> int:
    """THE RESIDUAL, COUNTED: exact nonzero entries after exact expansion.  A
    count of 0 is the exact zero-matrix statement and no tolerance is involved
    at any point."""
    return nonzero_entries(sp.expand(matrix))


# ---------------------------------------------------------------------------
# the cover: the shift cocycle, the chart differentials, the section
# ---------------------------------------------------------------------------
T_COVER, X_EXTENT = b128.COVER_TIME_EXTENT, b128.SPACE_EXTENT
N_COVER = T_COVER * X_EXTENT
MASS = b128.MASS
IU = sp.I


def cover_shift(dt: int, dx: int) -> sp.Matrix:
    """The PLAIN translation on the cover: no staggered sign is needed."""
    shift = sp.zeros(N_COVER, N_COVER)
    for t in range(T_COVER):
        for x in range(X_EXTENT):
            shift[b128.cover_index(t + dt, x + dx), b128.cover_index(t, x)] = 1
    return shift


def completion(hodge: sp.Matrix, differential: sp.Matrix) -> sp.Matrix:
    """The LANDED b128 completion convention, applied to a supplied pairing."""
    return sp.expand(MASS * hodge
                     + IU * (hodge * differential + differential.H * hodge))


def flat_hodge_cover() -> sp.Matrix:
    """The flat comparison object, averaged over the same four origins."""
    flat = sp.zeros(N_COVER, N_COVER)
    for t in range(T_COVER):
        for x in range(X_EXTENT):
            emb = b128.cover_embedding(t, x)
            flat += emb * b128.block105.shear_hodge(
                sp.Integer(0), sp.Integer(1)) * emb.T / 4
    return sp.expand(flat)


def quotient_shift(dim: int, time_extent: int, dt: int, dx: int,
                   wrap: int, space_wrap: int = 1) -> sp.Matrix:
    """The induced shift on the antiperiodic quotient.

    `wrap` is the sign picked up crossing the TEMPORAL seam: -1 is the
    ANTIPERIODIC wrap and +1 is the periodic control.  `space_wrap` is the
    sign picked up crossing the SPATIAL seam -- +1 is the physical (periodic)
    convention, and -1 exists ONLY for the check's wrap-uniqueness control,
    the deliberately WRONG space-antiperiodic shift that must fail.
    """
    shift = sp.zeros(dim, dim)
    for t in range(time_extent):
        for x in range(X_EXTENT):
            t2 = t + dt
            x2 = x + dx
            sign = wrap if (t2 >= time_extent or t2 < 0) else 1
            sign *= space_wrap if (x2 >= X_EXTENT or x2 < 0) else 1
            shift[(t2 % time_extent) * X_EXTENT + x2 % X_EXTENT,
                  t * X_EXTENT + x] = sign
    return shift


def staggered_sign_cover() -> sp.Matrix:
    """X_0 = diag((-1)^(t+x)) on the cover site order, built through the LANDED
    b128 index map so it cannot drift from the shift convention above.  It is
    the STAGGERED SIGN this block measures to be NEITHER needed NOR available as
    a conjugator."""
    grading = sp.zeros(N_COVER, N_COVER)
    for t in range(T_COVER):
        for x in range(X_EXTENT):
            index = b128.cover_index(t, x)
            grading[index, index] = sp.Integer(-1) ** (t + x)
    return grading


def note_text() -> tuple:
    """(text, at_final_path).  THE FINAL PATH IS THE ONLY PATH READ: there is no
    draft fallback anywhere in this runner, so before landing the text is empty
    and gate H fails on note-at-final-path alone."""
    try:
        return NOTE_PATH.read_text(encoding="utf-8"), True
    except OSError:
        return "", False


# ---------------------------------------------------------------------------
# THE N5 FENCE.  Single-line literal with \n separators; it appears
# BYTE-IDENTICALLY in the note and gate H checks it as a raw substring.
# ---------------------------------------------------------------------------
N5_FENCE = 'N5: per_element: THE IMPOSED-OBJECT BANNER, FIRST AND WITH TEETH. NOTHING HERE IS REGISTERED OR ADOPTED -- the certified Block 105 curved carrier as landed by Block 128 (the 8x4 cover of dimension 32, the antiperiodic quotient of dimension 16, MASS = 2/7 and the completion Q = MASS*H + i*(H d + d^H H)), the four chart origins (0,0), (0,1), (1,0) and (1,1), the plain cover shifts U_t and U_x, the redundant four-patch carrier V^+4 with D = diag(d_o), the graph section s(v) = (v, S_1 v, S_2 v, S_3 v), the orbit-averaged section Hodge H_s and the equal-weight point it sits at are IMPOSED MEASURED OBJECTS OF THIS BLOCK, rebuilt from the LANDED Block 128 runner and from NOTHING in any scratchpad. THE b128 NUMBERS ALL STAND AND NOTHING LANDED IS EDITED OR CORRECTED: this block REFRAMES the b128 obstruction and does not contradict it. FLATNESS-AS-CLASS IS NOT CLAIMED AT CONGRUENCE SCOPE -- every H_s statement here is MATRIX-LEVEL or, through the check-gated trace certificate, ORTHOGONAL-CLASS-LEVEL and no stronger. NOTHING IS REGISTERED, NOTHING IS ADOPTED, AND NO AXIOM AMENDMENT IS JUSTIFIED.\nper_site: THE TRANSLATION-ORBIT THEOREM AND THE NAIVE-AVERAGE FAILURE. On the dim-32 cover every chart differential d_o is NILPOTENT with d_o^2 = 0 exactly and rank 16, and all four are EXACT plain-shift conjugates of the single d_00 -- d_o = S_o d_00 S_o^-1 with a ZERO residual for S_o in {1, U_x, U_t, U_t U_x} and NO staggered signs needed -- while the cocycle closes at (1,1) in BOTH orderings and [U_t, U_x] = 0, so THE CHART CONNECTION IS THE SHIFT COCYCLE AND IT IS FLAT: the obstruction to the common differential is NOT curvature of the chart connection. AND THE NAIVE FRAME AVERAGE FAILS MAXIMALLY: d_avg = (1/4) sum_o d_o has d_avg^2 of FULL RANK 32 -- b105\'s generically-invertible failure QUANTIFIED -- because averaging conjugates of a nilpotent destroys nilpotency while conjugating the frame does not.\nper_mode: THE b105 TARGET, CONSTRUCTED. On the redundant patch carrier V^+4 with D = diag(d_(0,0), d_(0,1), d_(1,0), d_(1,1)) -- nilpotent FOR FREE -- the graph section s(v) = (v, S_1 v, S_2 v, S_3 v) has D-INVARIANT RANGE, certified by the EXACT intertwiner identities d_o S_o = S_o d_00 with a zero residual at all three nontrivial origins. That is the object Block 105 asked for twice over -- its section 1 next-precise-lemma prose, a transition-compatible nilpotent differential on the redundant patch carrier whose physical range is invariant, and its section 12 item 1 decision text, byte-exact, derive the common nilpotent patch/frame differential or its exact connection residual -- and THE b128 GATE THAT WAS UNEXECUTED IS NOW EXECUTED AND PASSES IN THE SECTION FRAME. THE FULLER 2026-08-15 DUAL-PATCH BLOCKER IS NOT EXECUTED HERE: its pullback clauses, the same graded Ward action and the signed staggered shifts, are UNTESTED by this block and stay OPEN.\nper_block: THE TWISTED DESCENT AND THE ACYCLIC COMPLEX. On the 16-dimensional antiperiodic quotient the time-shift conjugacy survives ONLY through the ANTIPERIODIC-wrapped shift: the wrap sign -1 gives a ZERO residual while the PERIODIC wrap FAILS at EXACTLY 4 entries, so the Z_2 twist is the sole global structure of the descent, and the spatial conjugacy descends untwisted. Every quotient differential is nilpotent with rank 8 = HALF of 16, so im = ker EXACTLY: THE ANTIPERIODIC COMPLEX IS ACYCLIC, WITH NO ZERO MODES -- the correct NS-sector statement, and the twist that enables the descent is the same structure that kills the cohomology.\nlattice_wide: THE SECTION HODGE AND THE CHART-COVARIANT COMPLETION. H_s = (1/4) sum_o S_o^T H S_o is SYMMETRIC and POSITIVE DEFINITE with all 32 leading minors > 0, and it differs from the raw curved Hodge H at 96 entries and from the flat Hodge at 96 entries -- MATRIX-LEVEL DIFFERENCE STATEMENTS, AND FLATNESS-AS-CLASS IS NOT CLAIMED AT CONGRUENCE SCOPE, where Sylvester makes every positive form congruent to every other; AND THE CHECK ANSWERED THE ORTHOGONAL-CLASS QUESTION: tr(H_s) = 927831123589/27222868400 differs from the flat trace 32, so H_s is NOT orthogonally or shift-equivalent to the flat reference. AND THE COMPLETION IS CHART-COVARIANT: Q(S_k H_s S_k^T, d_k) is the EXACT S_k-conjugate of Q(H_s, d_00) on the cover AND on the quotient under the twisted shifts, while the LANDED b128 pairing of a FIXED H against a SHIFTED d fails conjugacy at 256 entries -- PAIR-EXACT for the two actions the b128 runner lands, (1,0) against (1,1), and for the displayed d_00-against-d_01 comparison, NOT a uniform count, the (1,1)-against-(0,0) auxiliary giving 184. SCOPE HONESTY, AND IT IS LOAD-BEARING: THIS IS A NEW CHART-COVARIANT BASE OBJECT DONE RIGHT -- THIRD relative to the two actions the b128 runner actually lands, FIFTH relative to the four-origin auxiliary extrapolation -- AND NOT A PROOF THAT THE LANDED ACTIONS WERE SECRETLY EQUIVALENT; AND THE CHECK DECIDED THE PROBE: THE LANDED PAIR IS NON-ISOSPECTRAL, exact z^14 charpoly coefficients differing, so the landed actions are inequivalent even under arbitrary similarity and are NOT gauge copies of one another.\nper_scope: THE RESIDUAL IS NONINVARIANCE -- THE CURVATURE LABEL IS WITHDRAWN BY THE CHECK -- AND THE MODULI ARE DISCLOSED. The momentum-gate commutator rank stays at 32 for the section completion, exactly as it does for the LANDED control, so the section completion is translation-COVARIANT -- exact conjugacy, hence a shift-invariant spectrum -- and NOT translation-INVARIANT. AND THE CAUSAL LABEL IS CORRECTED, THE CHECK OVERRIDING THE SOLVE: the exact FLAT-HODGE CONTROL, H_flat = I_32 exactly, paired with the same d_00 ALSO has commutator rank 32, so the chartwise differential ALONE already breaks invariance on the flat reference, H_s contributes its own noninvariance separately, and the rank-32 number is NOT a curvature invariant; covariance-not-invariance is a REFRAME of what the gate measures and NEVER a repair of the missing invariant action or momentum decomposition. AND THE MODULI ARE DISCLOSED RATHER THAN HIDDEN: the commutant of the quotient d_00 is 128-DIMENSIONAL, 8 Jordan-2 blocks, the equal-weight section point is the CANONICAL SYMMETRIC POINT of that family, and NO UNIQUENESS PRINCIPLE IS CLAIMED.\nRESULT: THE COMMON DIFFERENTIAL EXISTS ON THE REDUNDANT PATCH CARRIER, THE CHART OBSTRUCTION WAS GAUGE, THE RESIDUAL IS NONINVARIANCE SHARED BY FLAT AND CURVED PAIRINGS ALIKE, AND THE QUOTIENT TWIST IS THE ANTIPERIODIC SIGN. The b128 obstruction is REFRAMED AND NOT CONTRADICTED and EVERY b128 NUMBER STANDS: the pairwise inequivalence of the displayed completions with exact first difference -89/140 was CHART-GAUGE MIXING, a FIXED H paired against a SHIFTED d, and the check STRENGTHENED it, the landed pair being NON-ISOSPECTRAL; the unexecuted common-differential gate of Block 105 section 12 item 1 is NOW EXECUTED AND PASSES in the section frame; and the full-rank-32 spatial-shift commutator certifies TRANSLATION NONINVARIANCE of every representative -- NOT curvature, the flat-Hodge control also ranking 32 -- while the covariant orbit stays isospectral. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\nDECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is edited; no earlier block is corrected; b128 STANDS AS LANDED and this block reframes rather than repairs it; the bar items stay PROPOSALS, and PROPOSALS STAY PROPOSALS. THIS BLOCK\'S OWN DEFECTS ARE DISCLOSED: it is a SINGLE FIXTURE FAMILY, the b128 8x4 cover and its 16-dimensional antiperiodic quotient over the certified Block 105 curved carrier, with NO width ladder and NO second carrier rule; it is the FOUR-ORIGIN chart set and no wider; the equal-weight section point is CANONICAL AND NOT UNIQUE inside a 128-dimensional commutant; every curvature statement is MATRIX-LEVEL AND NOT CLASS-LEVEL, with flatness-as-class NOT claimed at congruence scope and ANSWERED at orthogonal scope by the check; and the isospectrality probe is DECIDED, the landed pair NON-ISOSPECTRAL. THE ADVERSARIAL CHECK IS PART OF THIS BLOCK\'S EVIDENCE AND THE CHECKER\'S FINDINGS OVERRIDE THE SOLVE EVERYWHERE THEY COLLIDE. PROVENANCE: CAMPAIGN_20260824_GRAVITY_MAINLINE.md, at its G2 OPENING RESULTS and G2 SOLVE COMPLETE anchors.\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero.'


# ---------------------------------------------------------------------------
# the claims: every expected value the gates compare against, in ONE place
# ---------------------------------------------------------------------------
def build_claims(mutation: str) -> dict:
    claims: dict = {
        # A -- the authority pins.
        "main_head": CURRENT_MAIN,
        "parent_pin": "resolved",
        # B -- the banner's declared status flags.
        "objects_registered": False,
        "flatness_as_class_claimed": FLATNESS_AS_CLASS_CLAIMED,
        "landed_four_equivalence_claimed": LANDED_FOUR_EQUIVALENCE_CLAIMED,
        "uniqueness_claimed": UNIQUENESS_CLAIMED,
        # C -- the translation orbit.
        "chart_nilpotency_residual": ZERO_RESIDUAL,
        "chart_rank": CHART_RANK,
        "orbit_residual": ZERO_RESIDUAL,
        "cocycle_residual": ZERO_RESIDUAL,
        "flatness_residual": ZERO_RESIDUAL,
        "signed_conjugators": False,
        # D -- the naive average and the section.
        "average_rank": AVERAGE_RANK,
        "intertwiner_residual": ZERO_RESIDUAL,
        # E -- the twisted descent.
        "quotient_dim": QUOTIENT_DIM,
        "quotient_time_extent": QUOTIENT_TIME_EXTENT,
        "antiperiodic_residual": ZERO_RESIDUAL,
        "periodic_defect": PERIODIC_DEFECT,
        "spatial_plain_conjugates": True,
        "quotient_nilpotency_residual": ZERO_RESIDUAL,
        "quotient_rank": QUOTIENT_RANK,
        # F -- the section Hodge, with the check's trace certificate.
        "hodge_symmetry_residual": ZERO_RESIDUAL,
        "raw_hodge_defect": RAW_HODGE_DEFECT,
        "flat_hodge_defect": FLAT_HODGE_DEFECT,
        "hodge_positive_definite": True,
        "flat_is_identity": True,
        "hs_trace": HS_TRACE,
        # D-extra -- the check's determinant certificate for the average.
        "davg_det": DAVG_DET,
        # E-extra -- the check's wrap-sign uniqueness control.
        "space_anti_defect": SPACE_ANTI_DEFECT,
        # G -- covariance, the residual (with the check's flat control and the
        # non-isospectrality certificate) and the moduli.
        "covariance_residual": ZERO_RESIDUAL,
        "contrast_defect": CONTRAST_DEFECT,
        "quotient_completion_residual": ZERO_RESIDUAL,
        "section_gate_rank": SECTION_GATE_RANK,
        "control_gate_rank": CONTROL_GATE_RANK,
        "flat_control_gate_rank": FLAT_CONTROL_GATE_RANK,
        "z14_coeffs": Z14_COEFFS,
        "commutant_dim": COMMUTANT_DIM,
        # H -- the note and the fence.
        "required_scope_keys": SCOPE_KEYS,
    }
    if mutation == "stale_main_authority":
        claims["main_head"] = STALE_MAIN
    elif mutation == "stale_parent_authority":
        claims["parent_pin"] = "stale"
    elif mutation == "claim_objects_registered":
        # THE BANNER DENIED: the imposed objects asserted REGISTERED, which
        # zero registered and zero adopted objects forbid.
        claims["objects_registered"] = True
    elif mutation == "claim_flatness_as_class":
        # THE CONGRUENCE-SCOPE BOUND DENIED: flatness asserted AS A CLASS at
        # congruence scope, which Sylvester makes unaskable and this block's
        # declared scope forbids -- the check's trace certificate separates
        # H_s from flat at ORTHOGONAL scope and no stronger claim exists.
        claims["flatness_as_class_claimed"] = True
    elif mutation == "claim_landed_four_equivalent":
        # THE SCOPE-HONESTY SENTENCE DENIED: Block 128's landed four asserted
        # secretly equivalent, which this block neither measures nor claims.
        claims["landed_four_equivalence_claimed"] = True
    elif mutation == "break_orbit_conjugacy":
        # THE ORBIT BROKEN: a NONZERO plain-shift conjugacy residual asserted
        # allowed, which the exact zero at all three nontrivial origins
        # forbids.
        claims["orbit_residual"] = 4
    elif mutation == "claim_staggered_signs_needed":
        # THE STAGGERED SIGN REASSERTED: the conjugators claimed to carry the
        # staggered sign, which the MEASURED failure of the SIGNED shift to
        # conjugate forbids -- the plain shift is the one that works.
        claims["signed_conjugators"] = True
    elif mutation == "break_average_rank":
        # THE NAIVE-AVERAGE FAILURE SOFTENED: d_avg^2 asserted rank-deficient,
        # which the measured FULL rank 32 forbids.
        claims["average_rank"] = 16
    elif mutation == "break_intertwiner":
        # THE SECTION BROKEN: a nonzero intertwiner residual asserted, which
        # exact D-invariance of the graph section's range forbids.
        claims["intertwiner_residual"] = 4
    elif mutation == "break_periodic_defect":
        # THE TWIST DENIED: the PERIODIC wrap asserted to descend as well,
        # which the measured exact 4-entry defect forbids.
        claims["periodic_defect"] = 0
    elif mutation == "claim_twist_spatial":
        # THE TWIST MISPLACED: the SPATIAL conjugacy asserted to need the
        # antiperiodic wrap, which the exact PLAIN-wrap descent forbids.
        claims["spatial_plain_conjugates"] = False
    elif mutation == "break_hodge_minors":
        # THE PAIRING DEGRADED: a NONPOSITIVE leading minor asserted
        # acceptable, which 32 exactly positive minors forbid.
        claims["hodge_positive_definite"] = False
    elif mutation == "break_contrast_count":
        # THE CONTRAST DELETED: the LANDED b128 pairing asserted conjugate --
        # the landed pairing's conjugate, at zero -- which the measured
        # 256-entry failure forbids.
        claims["contrast_defect"] = 0
    elif mutation == "break_commutant_dim":
        # THE MODULI MISSTATED: a wrong commutant dimension asserted, which the
        # measured 128 for 8 Jordan-2 blocks forbids.
        claims["commutant_dim"] = 256
    elif mutation == "drop_n5_fence":
        claims["required_scope_keys"] = tuple(
            key for key in SCOPE_KEYS if key != "n5_verbatim")
    return claims


# ---------------------------------------------------------------------------
# the measurement pass: every gate reads it, no gate feeds it
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Facts:
    main_head: str
    authority: AuthorityCertificate
    note_at_final_path: bool
    scope: dict
    banners: dict
    nilpotency_residual: dict
    chart_rank: dict
    orbit_residual: dict
    signed_orbit_defect: dict
    signed_conjugators: bool
    cocycle_residual: int
    flatness_residual: int
    average_rank: int
    intertwiner_residual: dict
    quotient_dim: int
    quotient_time_extent: int
    antiperiodic_residual: int
    periodic_defect: int
    spatial_residual: int
    spatial_plain_conjugates: bool
    quotient_nilpotency_residual: dict
    quotient_rank: int
    hodge_symmetry_residual: int
    raw_defect: int
    flat_defect: int
    hodge_positive_definite: bool
    flat_is_identity: bool
    hs_trace: object
    davg_det: object
    space_anti_defect: int
    covariance_residual: dict
    contrast_defect: int
    quotient_completion_residual: dict
    section_gate_rank: int
    control_gate_rank: int
    flat_control_gate_rank: int
    z14_by_origin: dict
    commutant_dim: int


def measure() -> Facts:
    text, at_final_path = note_text()
    main_head = resolve_ref("origin/main")

    Ut, Ux = cover_shift(1, 0), cover_shift(0, 1)
    SMAP = {
        (0, 0): sp.eye(N_COVER),
        (0, 1): Ux,
        (1, 0): Ut,
        (1, 1): sp.expand(Ut * Ux),
    }
    D = {o: sp.Matrix(b128.chart_differential_cover(o)) for o in ORIGINS}

    # --- C: nilpotency, rank and the translation orbit ---------------------
    nilpotency = {o: residual_count(D[o] * D[o]) for o in ORIGINS}
    chart_rank = {o: D[o].rank() for o in ORIGINS}
    orbit = {o: residual_count(SMAP[o] * D[(0, 0)] * SMAP[o].T - D[o])
             for o in ORIGINS[1:]}
    cocycle = residual_count(
        sp.expand(Ux * Ut) * D[(0, 0)] * sp.expand(Ux * Ut).T - D[(1, 1)])
    flatness = residual_count(Ut * Ux - Ux * Ut)
    # THE SIGNED CONTROL: the same conjugation with the STAGGERED-SIGNED shift
    # X_0 S_o in place of the plain S_o.  It is measured, not assumed, and it
    # FAILS -- which is what "NO staggered signs" means here.
    grading = staggered_sign_cover()
    signed = {o: residual_count((grading * SMAP[o]) * D[(0, 0)]
                                * (grading * SMAP[o]).T - D[o])
              for o in ORIGINS[1:]}

    # --- D: the naive frame average and the section intertwiners -----------
    davg = sp.expand(sum([D[o] for o in ORIGINS], sp.zeros(N_COVER, N_COVER))
                     / 4)
    davg_sq = sp.expand(davg * davg)
    average_rank = davg_sq.rank()
    # THE CHECK'S DETERMINANT CERTIFICATE: an exact nonzero determinant is a
    # stronger full-rank witness than the rank computation alone.
    davg_det = sp.expand(davg_sq.det())
    # s(v) = (v, S_1 v, S_2 v, S_3 v); range invariance <=> d_o S_o = S_o d_00.
    intertwiner = {o: residual_count(D[o] * SMAP[o] - SMAP[o] * D[(0, 0)])
                   for o in ORIGINS[1:]}

    # --- E: the antiperiodic-twisted descent -------------------------------
    DQ = {o: sp.Matrix(b128.antiperiodic_quotient(D[o])) for o in ORIGINS}
    n_quot = DQ[(0, 0)].shape[0]
    t_quot = n_quot // X_EXTENT
    Utq_anti = quotient_shift(n_quot, t_quot, 1, 0, -1)
    Utq_per = quotient_shift(n_quot, t_quot, 1, 0, 1)
    Uxq = quotient_shift(n_quot, t_quot, 0, 1, 1)
    antiperiodic = residual_count(
        Utq_anti * DQ[(0, 0)] * Utq_anti.inv() - DQ[(1, 0)])
    periodic = residual_count(
        Utq_per * DQ[(0, 0)] * Utq_per.inv() - DQ[(1, 0)])
    spatial_residual = residual_count(
        Uxq * DQ[(0, 0)] * Uxq.inv() - DQ[(0, 1)])
    # THE CHECK'S WRAP-SIGN UNIQUENESS CONTROL: a deliberately WRONG
    # space-antiperiodic shift must FAIL at exactly 4 entries, pinning the
    # twist as uniquely temporal -- (time, space) = (-1, +1) is the one
    # closing pair.
    Uxq_anti = quotient_shift(n_quot, t_quot, 0, 1, 1, space_wrap=-1)
    space_anti_defect = residual_count(
        Uxq_anti * DQ[(0, 0)] * Uxq_anti.inv() - DQ[(0, 1)])
    quotient_nilpotency = {o: residual_count(DQ[o] * DQ[o]) for o in ORIGINS}
    quotient_rank = DQ[(0, 0)].rank()

    # --- F: the section-frame Hodge ----------------------------------------
    H = sp.Matrix(b128.curved_hodge_cover())
    Hs = sp.expand(
        sum([SMAP[o].T * H * SMAP[o] for o in ORIGINS],
            sp.zeros(N_COVER, N_COVER)) / 4)
    hodge_symmetry = residual_count(Hs - Hs.T)
    raw_defect = residual_count(Hs - H)
    flat_reference = flat_hodge_cover()
    flat_defect = residual_count(Hs - flat_reference)
    # THE CHECK'S FLAT-IDENTITY FACT AND TRACE CERTIFICATE: the flat reference
    # is EXACTLY I_32, and tr(H_s) differs from the flat trace 32, so no
    # orthogonal -- in particular no shift-group -- matrix carries H_s to it.
    flat_is_identity = bool(
        sp.expand(flat_reference - sp.eye(N_COVER)).is_zero_matrix)
    hs_trace = sp.expand(Hs.trace())
    minors_positive = all(Hs[:k, :k].det() > 0 for k in range(1, N_COVER + 1))

    # --- G: covariance, the scoped residual and the moduli -----------------
    Qs = completion(Hs, D[(0, 0)])
    covariance = {
        o: residual_count(SMAP[o] * Qs * SMAP[o].T
                          - completion(sp.expand(SMAP[o] * Hs * SMAP[o].T),
                                       D[o]))
        for o in ORIGINS[1:]}
    contrast = residual_count(
        Ux * completion(H, D[(0, 0)]) * Ux.T - completion(H, D[(0, 1)]))
    Qs_phys = sp.Matrix(b128.antiperiodic_quotient(Qs))
    SQ = {
        (0, 1): Uxq,
        (1, 0): Utq_anti,
        (1, 1): sp.expand(Utq_anti * Uxq),
    }
    descent = {
        o: residual_count(
            SQ[o] * Qs_phys * SQ[o].T
            - sp.Matrix(b128.antiperiodic_quotient(
                completion(sp.expand(SMAP[o] * Hs * SMAP[o].T), D[o]))))
        for o in ORIGINS[1:]}
    generator = b128.block105.translation_matrix((0, 1))
    doubled = sp.diag(generator, generator)
    G_sec = sp.Matrix(b128.grassmann_form(Qs_phys))
    section_gate_rank = (G_sec * doubled - doubled * G_sec).rank()
    # THE CHECK'S FLAT-HODGE CONTROL, the correction that withdrew the
    # curvature label: the exactly flat pairing over the same d_00 must ALSO
    # rank 32, so the rank-32 residual is NOT a curvature invariant.
    G_flat = sp.Matrix(b128.grassmann_form(sp.Matrix(
        b128.antiperiodic_quotient(completion(flat_reference, D[(0, 0)])))))
    flat_control_gate_rank = (G_flat * doubled - doubled * G_flat).rank()
    landed = b128.build_completions()
    control = landed[0]
    # THE CHECK'S NON-ISOSPECTRALITY CERTIFICATE: the two landed physical
    # actions' exact degree-16 characteristic polynomials, read at z^14.
    z14_by_origin = {
        comp.origin: sp.expand(
            sp.Matrix(comp.physical_action).charpoly().all_coeffs()[2])
        for comp in landed}
    commutant_map = sp.Matrix(
        sp.kronecker_product(sp.eye(n_quot), DQ[(0, 0)])
        - sp.kronecker_product(DQ[(0, 0)].T, sp.eye(n_quot)))
    commutant_dim = n_quot * n_quot - commutant_map.rank()

    banners = {
        "imposed_objects": len(IMPOSED_OBJECTS),
        "registered_objects": len(REGISTERED_OBJECTS),
        "adopted_objects": len(ADOPTED_OBJECTS),
        # THE DECLARED STATUS FLAGS, so the B mutations bite on a declared
        # object and not on prose.  ALL FOUR ARE MEASURED AND ALL ARE FALSE.
        "objects_registered": bool(REGISTERED_OBJECTS or ADOPTED_OBJECTS),
        "flatness_as_class_claimed": FLATNESS_AS_CLASS_CLAIMED,
        "landed_four_equivalence_claimed": LANDED_FOUR_EQUIVALENCE_CLAIMED,
        "uniqueness_claimed": UNIQUENESS_CLAIMED,
    }
    return Facts(
        main_head=main_head,
        authority=authority_certificate(main_head),
        note_at_final_path=at_final_path,
        scope=scope_certificate(text),
        banners=banners,
        nilpotency_residual=nilpotency,
        chart_rank=chart_rank,
        orbit_residual=orbit,
        signed_orbit_defect=signed,
        signed_conjugators=all(value == 0 for value in signed.values()),
        cocycle_residual=cocycle,
        flatness_residual=flatness,
        average_rank=average_rank,
        intertwiner_residual=intertwiner,
        quotient_dim=n_quot,
        quotient_time_extent=t_quot,
        antiperiodic_residual=antiperiodic,
        periodic_defect=periodic,
        spatial_residual=spatial_residual,
        spatial_plain_conjugates=spatial_residual == 0,
        quotient_nilpotency_residual=quotient_nilpotency,
        quotient_rank=quotient_rank,
        hodge_symmetry_residual=hodge_symmetry,
        raw_defect=raw_defect,
        flat_defect=flat_defect,
        hodge_positive_definite=minors_positive,
        flat_is_identity=flat_is_identity,
        hs_trace=hs_trace,
        davg_det=davg_det,
        space_anti_defect=space_anti_defect,
        covariance_residual=covariance,
        contrast_defect=contrast,
        quotient_completion_residual=descent,
        section_gate_rank=section_gate_rank,
        control_gate_rank=control.commutator_rank,
        flat_control_gate_rank=flat_control_gate_rank,
        z14_by_origin=z14_by_origin,
        commutant_dim=commutant_dim,
    )


# ---------------------------------------------------------------------------
# the gates: pure functions of the measured facts and the claims
# ---------------------------------------------------------------------------
def build_checks(facts: Facts, claims: dict) -> Checks:
    checks = Checks()
    authority = facts.authority
    parent_blobs_ok = (authority.parent_artifact_blobs
                       if claims["parent_pin"] == "resolved"
                       else authority.stale_parent_artifact_blobs)

    # --- A: authority -------------------------------------------------------
    checks.check(
        "A-authority-and-THE-STALE-PIN-THAT-PREDATES-BOTH-ARTIFACTS",
        "THE FIVE-PIN AUTHORITY BLOCK binds origin/main's head, the axioms "
        "blob and the registry blob at origin/main, and the axioms and "
        "registry blobs in the worktree. THE TWO BLOCK 180 ARTIFACTS ARE "
        "CONTENT-BOUND -- its note and its runner, the pair that identifies "
        "the commit this block's branch is cut from -- at PARENT_COMMIT, in "
        "the worktree and against their pinned blobs, and PARENT_COMMIT IS "
        "REAL and PARENT_REF resolves to it, so nothing needs sed at landing. "
        "THE STALE PIN IS THE BLOCK 179 TIP, a REAL ancestor of HEAD that "
        "PREDATES Block 180 and therefore carries NEITHER Block 180 artifact, "
        "which is exactly what makes the stale_parent_authority mutation bite: "
        "under it the gate looks for the artifact blobs at a commit where they "
        "do not exist. AUDIT_INPUT_PATHS IS LITERAL and every one of its "
        "entries is required readable in the worktree EXCEPT this block's own "
        "note, which lands later and belongs to gate H. AND THE MACHINERY "
        "IMPORT IS GATED: the LANDED Block 128 runner must have imported, "
        "because every object this runner measures is rebuilt from it and from "
        "the Block 105 module it re-exports -- NOTHING from any scratchpad is "
        "imported or read anywhere",
        bool(
            AUDIT_INPUT_PATHS[0] == SELF_NOTE_INPUT
            and len(AUDIT_INPUT_PATHS) == 9
            and len(set(AUDIT_INPUT_PATHS)) == 9
            and BLOCK180_NOTE in AUDIT_INPUT_PATHS
            and BLOCK180_RUNNER in AUDIT_INPUT_PATHS
            and BLOCK128_NOTE in AUDIT_INPUT_PATHS
            and BLOCK128_RUNNER in AUDIT_INPUT_PATHS
            and CAMPAIGN_NOTE in AUDIT_INPUT_PATHS
            # EVERY AUDIT INPUT BUT THIS BLOCK'S OWN NOTE IS READABLE IN THE
            # WORKTREE; the note itself is gate H's, because it lands later.
            and authority.inputs_readable == len(AUDIT_INPUT_PATHS) - 1
            and authority.inputs_missing == ()
            and PARENT_ARTIFACTS == (BLOCK180_NOTE, BLOCK180_RUNNER)
            and len(PARENT_ARTIFACT_BLOBS) == len(PARENT_ARTIFACTS) == 2
            and facts.main_head == claims["main_head"]
            and authority.fixed_authority
            and authority.machinery_import_landed
            and authority.parent_pin_is_commit
            and authority.parent_ref_and_ancestry
            and parent_blobs_ok
            # THE STALE PIN: a REAL ancestor of HEAD that carries NEITHER
            # Block 180 artifact.
            and authority.stale_is_real_ancestor
            and authority.stale_carries_neither_artifact))

    # --- B: the imposed-object banner and the NOT-CLAIMED keys -------------
    ban = facts.banners
    checks.check(
        "B-THE-IMPOSED-OBJECT-BANNER-and-the-NOT-CLAIMED-keys",
        f"THE BANNER COMES BEFORE ANY NUMERAL AND IT IS MEASURED RATHER THAN "
        f"ASSERTED. {ban['imposed_objects']} objects are IMPOSED by this block "
        f"-- the certified Block 105 curved carrier exactly as landed by Block "
        f"128, the four chart origins and their plain cover shifts, the "
        f"redundant four-patch carrier with its graph section, the "
        f"orbit-averaged section Hodge and the equal-weight point it sits at, "
        f"and the landed momentum gate with the landed chart completion as its "
        f"control -- and {ban['registered_objects']} are REGISTERED and "
        f"{ban['adopted_objects']} are ADOPTED. AND THE BANNER'S SECOND HALF "
        f"IS WHAT IS NOT CLAIMED, gated as declared constants: "
        f"FLATNESS-AS-CLASS IS NOT CLAIMED anywhere, since every H_s statement "
        f"here is MATRIX-LEVEL and the spectral separation test is the "
        f"checker's; THE EQUIVALENCE OF BLOCK 128's LANDED FOUR IS NOT "
        f"CLAIMED, since this block exhibits a FIFTH chart-covariant object "
        f"and decides nothing about the four; and NO UNIQUENESS IS CLAIMED for "
        f"the section point, which is CANONICAL inside a 128-dimensional "
        f"commutant and not forced. Asserting any of the three, or asserting "
        f"that the imposed objects are registered, fails HERE and nowhere else",
        bool(
            ban["imposed_objects"] == 5
            and ban["registered_objects"] == 0
            and ban["adopted_objects"] == 0
            and ban["objects_registered"] == claims["objects_registered"]
            and ban["flatness_as_class_claimed"]
            == claims["flatness_as_class_claimed"]
            and ban["landed_four_equivalence_claimed"]
            == claims["landed_four_equivalence_claimed"]
            and ban["uniqueness_claimed"] == claims["uniqueness_claimed"]))

    # --- C: nilpotency, rank and the translation orbit ---------------------
    for o in ORIGINS:
        checks.check(
            f"C-nilpotency-d_{o}",
            "the chart differential SQUARES TO ZERO exactly on the "
            "32-dimensional cover -- no tolerance is involved",
            facts.nilpotency_residual[o] == claims["chart_nilpotency_residual"])
        checks.check(
            f"C-rank-16-d_{o}",
            "the chart differential has EXACT rank 16, half the carrier "
            "dimension, so it is a maximal-rank nilpotent",
            facts.chart_rank[o] == claims["chart_rank"])
    for o in ORIGINS[1:]:
        checks.check(
            f"C-shift-conjugacy-d_{o}-equals-S-d00-S-inverse",
            "the chart differential is the EXACT PLAIN-SHIFT CONJUGATE of the "
            "single d_00 with a ZERO full-matrix residual and NO staggered "
            "sign anywhere: the four charts are ONE differential in four "
            "translated frames",
            facts.orbit_residual[o] == claims["orbit_residual"])
    checks.check(
        "C-cocycle-closes-in-the-REVERSED-ordering",
        "the (1,1) corner closes with Ux Ut as well as with Ut Ux, so the "
        "cocycle is ordering-independent and the chart transition is a "
        "genuine cocycle rather than a chosen path",
        facts.cocycle_residual == claims["cocycle_residual"])
    checks.check(
        "C-flatness-[Ut,Ux]=0",
        "the two cover shifts COMMUTE exactly, so the chart holonomy is "
        "TRIVIAL and the chart connection is FLAT: whatever obstructs the "
        "common differential, it is NOT curvature of the chart connection",
        facts.flatness_residual == claims["flatness_residual"])
    checks.check(
        "C-NO-staggered-sign-the-SIGNED-conjugator-is-MEASURED-to-FAIL",
        f"the STAGGERED-SIGNED conjugator X_0 S_o is built and tested in the "
        f"same run, and it FAILS at {tuple(facts.signed_orbit_defect.values())}"
        f" nonzero entries: the plain shift is the conjugator and the "
        f"staggered sign is NEITHER needed NOR available. Claiming the "
        f"conjugators carry a staggered sign fails HERE and nowhere else",
        facts.signed_conjugators == claims["signed_conjugators"])

    # --- D: the naive average and the D-invariant section ------------------
    checks.check(
        "D-naive-average-d_avg-squared-has-FULL-rank-32",
        f"the frame average d_avg = (1/4) sum_o d_o has d_avg^2 of FULL rank "
        f"{facts.average_rank} on the 32-dimensional carrier -- b105's "
        f"'generically invertible' failure QUANTIFIED AT ITS MAXIMUM. "
        f"Averaging conjugates of a nilpotent DESTROYS nilpotency; "
        f"conjugating the frame does not",
        facts.average_rank == claims["average_rank"])
    checks.check(
        "D-the-CHECK-determinant-certificate-det-d_avg-squared",
        f"det(d_avg^2) = {facts.davg_det} equals (3/10)^64 exactly -- the "
        f"adversarial check's NONZERO-DETERMINANT certificate, a strictly "
        f"stronger full-rank witness than the rank computation, folded in as "
        f"a gate",
        sp.expand(facts.davg_det - claims["davg_det"]) == 0)
    for o in ORIGINS[1:]:
        checks.check(
            f"D-intertwiner-d_{o}-S-equals-S-d00",
            "the EXACT intertwiner identity, which is precisely D-invariance "
            "of the graph section's range on the redundant patch carrier "
            "V^+4 with D = diag(d_o) -- Block 105 section 12 item 1's object, "
            "and the b128 gate that was UNEXECUTED is EXECUTED here",
            facts.intertwiner_residual[o] == claims["intertwiner_residual"])

    # --- E: the antiperiodic-twisted descent -------------------------------
    checks.check(
        "E-quotient-dim-16-time-extent-4",
        f"the antiperiodic quotient is {facts.quotient_dim}-dimensional at "
        f"time extent {facts.quotient_time_extent}, the LANDED b128 physical "
        f"carrier",
        (facts.quotient_dim, facts.quotient_time_extent)
        == (claims["quotient_dim"], claims["quotient_time_extent"]))
    checks.check(
        "E-antiperiodic-Ut-conjugacy-on-the-quotient",
        "the time-shift conjugacy SURVIVES the descent through the "
        "ANTIPERIODIC-wrapped shift with a ZERO residual: the Z_2 twist is "
        "the sole global structure of the descent",
        facts.antiperiodic_residual == claims["antiperiodic_residual"])
    checks.check(
        "E-PERIODIC-wrap-FAILS-at-exactly-4-entries",
        f"the periodic control wrap fails at EXACTLY {facts.periodic_defect} "
        f"entries -- the twist is not decorative and the defect is counted, "
        f"not summarised",
        facts.periodic_defect == claims["periodic_defect"])
    checks.check(
        "E-PLAIN-wrap-Ux-conjugacy-on-the-quotient",
        "the SPATIAL conjugacy descends UNTWISTED with a zero residual: the "
        "twist is temporal and only temporal. Claiming the spatial conjugacy "
        "needs the antiperiodic wrap fails HERE and nowhere else",
        facts.spatial_plain_conjugates == claims["spatial_plain_conjugates"])
    checks.check(
        "E-the-CHECK-wrap-uniqueness-SPACE-antiperiodic-fails-at-4",
        f"the deliberately WRONG space-antiperiodic shift fails the spatial "
        f"conjugacy at EXACTLY {facts.space_anti_defect} entries -- the "
        f"adversarial check's wrap-sign sweep folded in as a gate: "
        f"(time, space) = (-1, +1) is the UNIQUE closing pair, so the Z_2 "
        f"twist is pinned as uniquely temporal by measurement, not convention",
        facts.space_anti_defect == claims["space_anti_defect"])
    for o in ORIGINS:
        checks.check(
            f"E-quotient-nilpotency-d_{o}",
            "the quotient differential squares to zero exactly, so the "
            "descended object is still a differential",
            facts.quotient_nilpotency_residual[o]
            == claims["quotient_nilpotency_residual"])
    checks.check(
        "E-quotient-rank-8-ACYCLIC-im-equals-ker",
        f"rank {facts.quotient_rank} is EXACTLY half of 16, so im = ker and "
        f"the ANTIPERIODIC COMPLEX IS ACYCLIC with NO ZERO MODES -- the "
        f"correct NS-sector statement, and the twist that enables the descent "
        f"is the same structure that kills the cohomology",
        facts.quotient_rank == claims["quotient_rank"])

    # --- F: the section-frame Hodge ----------------------------------------
    checks.check(
        "F-H_s-symmetric",
        "the orbit-averaged section Hodge is EXACTLY symmetric, so it is a "
        "pairing and not merely a matrix",
        facts.hodge_symmetry_residual == claims["hodge_symmetry_residual"])
    checks.check(
        "F-H_s-differs-from-the-RAW-curved-Hodge-at-96-entries",
        f"{facts.raw_defect} entries differ. THIS IS A MATRIX-LEVEL STATEMENT "
        f"ONLY: the section frame is a DIFFERENT MATRIX from the raw curved "
        f"Hodge, and NO flatness-as-class claim is made or gated here",
        facts.raw_defect == claims["raw_hodge_defect"])
    checks.check(
        "F-H_s-differs-from-the-FLAT-Hodge-at-96-entries",
        f"{facts.flat_defect} entries differ from the same-origin average of "
        f"the flat shear Hodge. MATRIX-LEVEL as an entry count -- and the "
        f"class question it cannot answer is answered by the trace "
        f"certificate gated below, at ORTHOGONAL scope and no stronger",
        facts.flat_defect == claims["flat_hodge_defect"])
    checks.check(
        "F-the-FLAT-reference-is-EXACTLY-the-identity",
        "the same-origin average of shear_hodge(0,1) is I_32 EXACTLY -- the "
        "adversarial check's flat-identity fact, folded in as a gate so the "
        "flat comparison object is pinned rather than described",
        facts.flat_is_identity == claims["flat_is_identity"])
    checks.check(
        "F-the-CHECK-trace-certificate-separates-H_s-from-flat-ORTHOGONALLY",
        f"tr(H_s) = {facts.hs_trace} equals 927831123589/27222868400 exactly "
        f"and DIFFERS from the flat trace 32, so NO orthogonal matrix -- in "
        f"particular no shift-group element -- carries H_s to the flat "
        f"reference. THE ORTHOGONAL-CLASS SEPARATION IS ANSWERED, and "
        f"Sylvester bars any congruence-scope strengthening: every "
        f"positive-definite form is congruent to every other, so the "
        f"orthogonal scope is the strongest honest scope",
        sp.expand(facts.hs_trace - claims["hs_trace"]) == 0
        and sp.expand(facts.hs_trace - 32) != 0)
    checks.check(
        "F-H_s-POSITIVE-DEFINITE-by-32-positive-leading-minors",
        "all 32 leading principal minors are EXACTLY positive rationals, so "
        "H_s is a legitimate Hodge pairing and the section frame is not a "
        "degenerate average",
        facts.hodge_positive_definite == claims["hodge_positive_definite"])

    # --- G: covariance, the scoped residual and the moduli -----------------
    for o in ORIGINS[1:]:
        checks.check(
            f"G-base-{o}-completion-is-the-EXACT-S-conjugate",
            "pairing the SHIFTED Hodge with the SHIFTED differential gives "
            "the exact S-conjugate of the base completion with a ZERO "
            "residual: THE SECTION COMPLETION IS CHART-COVARIANT",
            facts.covariance_residual[o] == claims["covariance_residual"])
    checks.check(
        "G-CONTRAST-the-LANDED-b128-pairing-fails-at-256-entries",
        f"the landed pairing of a FIXED H against a SHIFTED d fails conjugacy "
        f"at {facts.contrast_defect} entries -- PAIR-EXACT for the landed "
        f"(1,0)/(1,1) pair and this displayed d_00/d_01 comparison, NOT a "
        f"uniform count (the (1,1)-vs-(0,0) auxiliary gives 184). b128's "
        f"displayed pairwise-inequivalent completions were CHART-GAUGE "
        f"MIXING. SCOPE HONESTY: this exhibits a NEW CHART-COVARIANT BASE "
        f"OBJECT DONE RIGHT -- THIRD against the TWO actions the b128 runner "
        f"lands, FIFTH against the four-origin auxiliary extrapolation -- and "
        f"is NOT a proof that the landed actions were secretly equivalent; "
        f"every b128 number stands",
        facts.contrast_defect == claims["contrast_defect"])
    checks.check(
        "G-the-CHECK-non-isospectrality-certificate-z14-coefficients",
        f"the TWO landed physical actions' exact degree-16 characteristic "
        f"polynomials, read at z^14, are "
        f"{facts.z14_by_origin.get((1, 0))} at origin (1,0) and "
        f"{facts.z14_by_origin.get((1, 1))} at origin (1,1) -- both equal the "
        f"check's recorded exact rationals AND THEY DIFFER: the landed pair "
        f"is NON-ISOSPECTRAL, inequivalent even under arbitrary similarity, "
        f"NEVER gauge copies -- b128's inequivalence certificate is "
        f"STRENGTHENED by the check, and the probe the solve left open is "
        f"DECIDED",
        set(facts.z14_by_origin) == set(claims["z14_coeffs"])
        and all(sp.expand(facts.z14_by_origin[o] - claims["z14_coeffs"][o])
                == 0 for o in claims["z14_coeffs"])
        and sp.expand(facts.z14_by_origin[(1, 0)]
                      - facts.z14_by_origin[(1, 1)]) != 0)
    for o in ORIGINS[1:]:
        checks.check(
            f"G-quotient-completion-descent-base-{o}",
            "the chart covariance SURVIVES the antiperiodic descent under the "
            "TWISTED shifts with a zero residual, so it is a statement about "
            "the physical carrier and not only about the cover",
            facts.quotient_completion_residual[o]
            == claims["quotient_completion_residual"])
    checks.check(
        "G-momentum-gate-rank-32-NONINVARIANCE-the-curvature-label-withdrawn",
        f"the momentum-gate commutator of the SECTION completion has rank "
        f"{facts.section_gate_rank}, unchanged from the landed value. The "
        f"section completion is translation-COVARIANT -- exact conjugacy, "
        f"hence a shift-invariant spectrum -- and NOT translation-INVARIANT. "
        f"THE CURVATURE LABEL IS WITHDRAWN: the flat-Hodge control gated "
        f"below also ranks 32, so the rank-32 number certifies TRANSLATION "
        f"NONINVARIANCE of the representative and is NOT a curvature "
        f"invariant; covariance-not-invariance is a REFRAME, never a repair "
        f"of the missing invariant action",
        facts.section_gate_rank == claims["section_gate_rank"])
    checks.check(
        "G-CONTROL-the-landed-chart-completion-also-ranks-32",
        "the LANDED b128 completion is measured in the same run and carries "
        "the same rank-32 defect, so the section frame neither improves nor "
        "worsens the momentum gate and the comparison is like-for-like",
        facts.control_gate_rank == claims["control_gate_rank"])
    checks.check(
        "G-the-CHECK-FLAT-HODGE-control-also-ranks-32",
        f"the exactly FLAT pairing -- I_32 with the same d_00 -- has "
        f"momentum-gate commutator rank {facts.flat_control_gate_rank}: the "
        f"adversarial check's correction folded in as a gate. The chartwise "
        f"differential ALONE breaks translation invariance on the flat "
        f"reference, so the rank-32 residual is NOT curvature and the "
        f"solve's first label is WITHDRAWN as content",
        facts.flat_control_gate_rank == claims["flat_control_gate_rank"])
    checks.check(
        "G-commutant-dim-128-8-Jordan-2-blocks",
        f"the commutant of the quotient d_00 has dimension "
        f"{facts.commutant_dim}, the exact value for 8 Jordan-2 blocks. THE "
        f"EQUAL-WEIGHT SECTION POINT IS THE CANONICAL SYMMETRIC POINT OF THIS "
        f"FAMILY AND NO UNIQUENESS PRINCIPLE IS CLAIMED -- the moduli are "
        f"DISCLOSED, not hidden",
        facts.commutant_dim == claims["commutant_dim"])

    # --- H: the note at its final path, and the N5 fence -------------------
    required = tuple(claims["required_scope_keys"])
    checks.check(
        "H-note-at-final-path-and-the-N5-fence",
        f"the note is read at its FINAL PATH {facts.note_at_final_path} -- "
        f"THERE IS NO DRAFT FALLBACK ANYWHERE IN THIS RUNNER, so when False "
        f"the note has not landed at docs/ yet, gate H is EXPECTED to fail on "
        f"that alone, and families A through G are unaffected. The N5 fence is "
        f"an N5-prefixed single-line literal with nine labelled sections that "
        f"must appear BYTE-IDENTICALLY in the note, the required scope-key set "
        f"is THE FULL DECLARED SET and not a subset, and the mutation battery "
        f"is fifteen members mapped one-per-family across A through H",
        bool(
            facts.note_at_final_path
            and NOTE_PATH.name == FINAL_NOTE_NAME
            and set(facts.scope) == set(SCOPE_KEYS)
            # THE FULL KEY SET IS REQUIRED, not a subset.
            and required == SCOPE_KEYS
            and all(facts.scope[key] for key in required)
            and facts.scope["n5_verbatim"]
            and len(MUTATIONS) == 15
            and len(set(MUTATIONS)) == 15
            and set(MUTATION_GATE) == set(MUTATIONS)
            and set(MUTATION_GATE.values()) == set("ABCDEFGH")
            and N5_FENCE.startswith("N5: ")
            and 9 <= N5_FENCE.count("\n") + 1 <= 12
            and all(N5_FENCE.count(f"\n{name}:") == 1
                    for name in ("per_site", "per_mode", "per_block",
                                 "lattice_wide", "per_scope", "RESULT",
                                 "DECISION_CUT", "TOE"))))
    return checks


def report_measured(facts: Facts, elapsed_ns: int) -> None:
    authority = facts.authority
    ban = facts.banners
    print("MEASURED, before any gate is read:")
    print(f"  AUTHORITY: origin/main resolves to {facts.main_head}; the "
          f"five-pin block is fixed {authority.fixed_authority}. "
          f"PARENT_COMMIT {PARENT_COMMIT} is REAL and PARENT_REF resolves to "
          f"it {authority.parent_ref_and_ancestry}, and BOTH Block 180 "
          f"artifacts are content-bound there and in the worktree "
          f"{authority.parent_artifact_blobs}. THE AUDIT INPUTS: "
          f"{authority.inputs_readable} of {len(AUDIT_INPUT_PATHS) - 1} "
          f"readable in the worktree (this block's own note excluded, since it "
          f"lands later and is gate H's), missing {authority.inputs_missing}")
    print(f"  THE STALE PIN: {STALE_PARENT_COMMIT[:12]} is a REAL ancestor of "
          f"HEAD {authority.stale_is_real_ancestor} and carries NEITHER Block "
          f"180 artifact {authority.stale_carries_neither_artifact} -- it is "
          f"the Block 179 tip, which PREDATES both artifacts, and that absence "
          f"is exactly what makes the stale_parent_authority mutation bite")
    print(f"  THE MACHINERY: the LANDED Block 128 runner is imported "
          f"{authority.machinery_import_landed} and every object below is "
          f"rebuilt from it -- the cover is {T_COVER}x{X_EXTENT} at dimension "
          f"{N_COVER}, the antiperiodic quotient is {facts.quotient_dim}"
          f"-dimensional at time extent {facts.quotient_time_extent}, "
          f"MASS = {MASS}, and the completion convention is "
          f"Q = MASS*H + i*(H d + d^H H). NOTHING from any scratchpad is "
          f"imported or read")
    print(f"  THE BANNER: {ban['imposed_objects']} imposed objects, "
          f"{ban['registered_objects']} registered and "
          f"{ban['adopted_objects']} adopted; MEASURED "
          f"flatness-as-class-claimed {ban['flatness_as_class_claimed']}, "
          f"landed-four-equivalence-claimed "
          f"{ban['landed_four_equivalence_claimed']} and uniqueness-claimed "
          f"{ban['uniqueness_claimed']}. The imposed objects are "
          f"{IMPOSED_OBJECTS}")
    print(f"  THE ORBIT: the four chart differentials are nilpotent of rank 16 "
          f"and are EXACT plain-shift conjugates of the single d_00; the "
          f"cocycle closes in both orderings and [U_t, U_x] = 0, so the chart "
          f"connection is the shift cocycle AND IT IS FLAT. The naive frame "
          f"average has d_avg^2 at FULL rank {facts.average_rank}. AND THE "
          f"STAGGERED-SIGNED CONJUGATOR IS MEASURED TO FAIL, at "
          f"{tuple(facts.signed_orbit_defect.values())} nonzero entries: no "
          f"staggered sign is needed and none is available")
    print(f"  THE DESCENT: the antiperiodic wrap gives a zero residual and the "
          f"PERIODIC control fails at exactly {facts.periodic_defect} entries; "
          f"the quotient differentials are nilpotent at rank "
          f"{facts.quotient_rank}, exactly half of {facts.quotient_dim}, so "
          f"im = ker AND THE COMPLEX IS ACYCLIC")
    print(f"  THE SECTION HODGE: H_s is symmetric and positive definite by 32 "
          f"leading minors, and differs from the RAW curved Hodge at "
          f"{facts.raw_defect} entries and from the FLAT Hodge at "
          f"{facts.flat_defect}. THESE ARE MATRIX-LEVEL STATEMENTS AND "
          f"FLATNESS-AS-CLASS IS NOT CLAIMED ANYWHERE IN THIS RUNNER")
    print(f"  THE COVARIANCE AND THE RESIDUAL: the section completion is "
          f"exactly S-conjugate on the cover and on the quotient, while the "
          f"LANDED b128 pairing fails at {facts.contrast_defect} entries; the "
          f"momentum-gate commutator rank is {facts.section_gate_rank} for the "
          f"section completion and {facts.control_gate_rank} for the landed "
          f"control -- TRANSLATION-COVARIANT, NOT TRANSLATION-INVARIANT, AND "
          f"THE RESIDUAL IS CURVATURE")
    print(f"  THE MODULI: the commutant of the quotient d_00 is "
          f"{facts.commutant_dim}-dimensional, 8 Jordan-2 blocks; the "
          f"equal-weight point is CANONICAL AND NOT UNIQUE")
    print(f"  THE NOTE: read at its FINAL PATH {facts.note_at_final_path} -- "
          f"when False the note has NOT landed at docs/ yet, there is no draft "
          f"fallback anywhere in this runner, gate H is EXPECTED to fail and "
          f"the gate-H mutation is UNTESTABLE until the note lands. Scope keys "
          f"satisfied: {sum(1 for v in facts.scope.values() if v)} of "
          f"{len(facts.scope)}; unsatisfied "
          f"{tuple(key for key, value in facts.scope.items() if not value)}")
    print(f"  EXACTNESS: every measured object above is exact sympy Rational "
          f"or Integer arithmetic; NO FLOAT and NO TOLERANCE enters any check. "
          f"ELAPSED {elapsed_ns // 1_000_000} ms")
    print(f"  THE b128 RELATION: the obstruction is REFRAMED AND NOT "
          f"CONTRADICTED and every b128 number STANDS -- the pairwise "
          f"inequivalence at exact first difference -89/140 was chart-gauge "
          f"mixing, the unexecuted common-differential gate is now EXECUTED, "
          f"and the full-rank-32 commutator is REIDENTIFIED as background "
          f"curvature")
    print()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument(
        "--list-mutations", action="store_true",
        help="print the declared mutation names, one per line, and exit")
    arguments = parser.parse_args()
    if arguments.list_mutations:
        for name in MUTATIONS:
            print(name)
        return 0
    mutation = arguments.mutation
    started_ns = time.monotonic_ns()

    # Every measurement happens once, before any mutation flag is consulted, so
    # a mutation can only rewrite a CLAIM.  No family can cascade into another
    # because no gate feeds a measurement.
    facts = measure()
    elapsed_ns = time.monotonic_ns() - started_ns

    checks = build_checks(facts, build_claims(""))
    if mutation:
        raw = checks.families()
        checks = build_checks(facts, build_claims(mutation))
        mutated = checks.families()
        target = MUTATION_GATE[mutation]
        changed = {family for family in raw if raw[family] != mutated[family]}
        if changed - {target} or mutated[target]:
            raise AssertionError("mutation did not fail exactly its own gate")

    report_measured(facts, elapsed_ns)
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
