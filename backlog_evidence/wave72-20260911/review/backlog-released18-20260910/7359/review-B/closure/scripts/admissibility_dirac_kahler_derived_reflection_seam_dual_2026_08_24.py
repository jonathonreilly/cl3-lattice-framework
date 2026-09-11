#!/usr/bin/env python3
"""BLOCK 183 -- THE DERIVED REFLECTION AND THE SEAM-DUAL FRAME.

THE RESULT, AND ITS EXACT SCOPE.  On the certified Block 105 curved carrier as
landed by Block 128 and re-used by Blocks 181 and 182 -- the 8x4 cover of
dimension 32, the parameterized cover Hodge H[g] over the LANDED Block 105
overlap field, the chart differential d_00 and the completion convention
Q(H,d) = m*H + i*(H d + d^H H) at SYMBOLIC POSITIVE MASS -- THE TIME REFLECTION
IS DERIVED FROM THE CARRIER'S OWN EMBEDDING CORRESPONDENCE, IT SQUARES TO MINUS
ONE, AND THE SEAM IS SHOWN TO PAIR THE FRAME WITH A DUAL FRAME:

  0. THE NEGATIVE GRIDS ARE THE DERIVATION PATH, AND THEY ARE RECORDED FIRST.
     The reflection was NOT guessed into place.  Three guess programs failed
     first and the campaign records all three: an EIGHT-CELL naive sweep (two
     site reflections x flipped/unflipped field x dagger/plain target, every
     residual in the band 352-368), a TWENTY-CANDIDATE dressed grid that mapped
     d_00 onto NONE of {+-d_00, +-d_00^H, +-d_10, +-d_10^H}, and a SIXTEEN-
     TARGET diagonal-intertwiner solve.  Two of the three are re-measured HERE
     as pinned certificates: the naive band endpoints 352 and 368, and the
     eight explicit non-identities that put the derived conjugate outside the
     guessed family.  THE FAILURES FORCED THE DERIVATION; they are not an
     apology for it.

  1. THE DERIVED REFLECTION, WHICH SQUARES TO MINUS ONE (C).  cover_embedding's
     corner order (00, 01, 10, 11) IS the form basis (1, dx, dt, dx^dt).  Block
     104's own bond convention theta(t) = -1-t -- read from its primary body --
     acts on cells [t, t+1] -> [-2-t, -1-t]; the staggered one-component-per-
     site identification makes the site map t -> 7-t single-valued; and the form
     parity that goes with it is Block 105's own P_t = diag(1,1,-1,-1) pullback,
     which on this carrier is tpar = diag((-1)^(t%2)).  SO R = P_edge * tpar,
     AND NOTHING ABOUT IT IS A CHOICE.  Measured: R is REAL ORTHOGONAL
     (R R^T = I, so R^-1 = R^T = -R) and R^2 = -I EXACTLY, against a 32-entry
     residual for +I -- a PROJECTIVE involution with R^4 = I whose conjugation
     action on operators is nonetheless an exact involution.  d_ref =
     R d_00 R^-1 is NILPOTENT of rank 16, and THE FLAT CONTROL IS EXACT:
     R Q(I, d_00) R^-1 = Q(I, d_00), residual ZERO.  The x-parity variant
     P_edge * diag((-1)^x) is an HONEST involution (square +I) and sends the
     flat completion to its ADJOINT, R_x Q R_x^-1 = Q^H = Q^T exactly.  AND THE
     GRADE CO-TRANSPORTS, for the THIRD time in this lane: d_00 has all 32 of
     its nonzero entries at grade jump +1, while d_ref splits EXACTLY 16 / 16
     between jumps -1 and +1, so against the FIXED census N = diag(t%2 + x%2)
     the commutator defect is EXACTLY 16 ENTRIES -- while against the
     CO-TRANSPORTED census R N R^-1 it is grade-raising at ZERO residual.

  2. THE CELL FACTORIZATION (D).  For EVERY ONE of the 32 cells,
     R emb(t,x) = emb((6-t)%8, x) * (s * M) with s = (-1)^t and with ONE 4x4 M
     for every cell -- and M^2 = -I EXACTLY.  M IS A COMPLEX STRUCTURE ON THE
     CELL.  The sign is forced (a single M at every cell requires the dressing
     to alternate), and with it R^2 = -I is forced too: theta(t) = 6-t
     preserves t-parity, so the two cell signs multiply to +1 and
     R^2 emb(c) = emb(c) M^2 = -emb(c).

  3. THE DUAL BLOCK, IN CLOSED FORM (E).  At SYMBOLIC (q, v),
     M H(q,v) M^T = [[-v/(q^2-1), 0, 0, -q*v/(q^2-1)], [0, 1/v, 0, 0],
     [0, 0, v, 0], [-q*v/(q^2-1), 0, 0, -v/(q^2-1)]] EXACTLY -- the STAR-DUAL
     family.  It is NOT H(q,v), NOT H(-q,v), NOT either inverse, NOT H(q,1/v)
     and NOT H(-q,1/v): six explicit non-identities, all measured.

  4. THE HODGE-LEVEL THEOREM (F).  R H[g] R^-1 = H_dual[theta g] EXACTLY at the
     LANDED field, with theta the cell field reflection (t,x) -> ((2-t)%4, x)
     and H_dual built from the dual block.  The control comes first: H[landed
     field] IS the LANDED curved_hodge_cover() at zero residual.  And two
     discriminating controls are measured in the same run: the UNDRESSED site
     reflection does NOT satisfy it, and the reflection against the UNDUALIZED
     target does not either.

  5. THE SECTION POINTS, AND WHAT CLOSURE DOES AND DOES NOT SELECT (G).  THE
     MECHANISM IS EXHIBITED AS A CONJUGATION TABLE: R U_t R^-1 = -U_t^-1
     EXACTLY (against a 32-entry residual for +U_t^-1) and R U_x R^-1 = U_x
     EXACTLY.  So closure of an orbit-averaged section point needs only that
     the TEMPORAL WEIGHTS be reflection-symmetric, w_k = w_{-k}.  THE BLOCK 181
     EQUAL-WEIGHT POINT IS NOT REFLECTION-CLOSED -- its {0,1}^2 origin set maps
     to {0,-1}x{0,1}, so against the SAME origin set the Hodge-level residual is
     EXACTLY 96 and the action-level residual is EXACTLY 256, while against the
     REFLECTED origin set the Hodge-level residual is EXACTLY ZERO.  BUT
     CLOSURE DOES NOT SELECT A POINT.  The reflection orbits of the temporal
     exponents are {0}, {4}, {1,7}, {2,6}, {3,5}, and EVERY equal-weight union
     of them containing 0, crossed with {I, U_x}, closes EXACTLY and is
     POSITIVE DEFINITE: SIXTEEN such sets, FIFTEEN of them PROPER subsets of
     the full orbit, with {I, U_x} the MINIMAL member -- which closes exactly,
     is PD by 32 exact leading minors, carries the two-step covariance, and
     differs from the full-orbit point at 96 entries.  CLOSURE CONSTRAINS THE
     BLOCK 181 MODULI AND NEVER PINS THEM.  At the full-orbit point H_sym the
     same package holds and the action-level identity R Q(H_sym[g], d_00) R^-1
     = m H_sym_dual + i(H_sym_dual d_ref + d_ref^H H_sym_dual) is EXACT --
     A FORMAL COROLLARY of the Hodge-level closure plus orthogonality and the
     distribution of conjugation, ADDING NO INDEPENDENT CONSTRAINT, and gated
     as a consistency certificate.

WHAT IS NOT CLAIMED, STATED ONCE: NO OS OR REFLECTION-POSITIVITY THEOREM -- the
reflection is constructed and its covariance measured, and no positivity of any
pairing is asserted; NO TEMPORAL-LINK EXTRACTION -- the dt=+-1 band is NOT
extracted here; NO TWO-HISTORY GRAM; NO GRAVITY RESULT; and NO UNIQUE SELECTION
OF A SECTION POINT -- reflection closure RULES OUT the equal-weight point and
ADMITS a whole orbit-constant-weight family, uniqueness is REFUTED rather than
merely unclaimed, and the banner key is gated as a declared constant.

GATES
  A  AUTHORITY: the five-pin authority block, the TWO Block 182 artifacts
     content-bound at PARENT_COMMIT and in the worktree, the nine audit inputs
     readable, and the stale pin verified to be a REAL ancestor of HEAD that
     carries NEITHER artifact.
  B  THE IMPOSED-OBJECT BANNER AND THE NOT-CLAIMED KEYS: six imposed objects,
     ZERO registered and ZERO adopted, with the OS/reflection-positivity
     theorem, the temporal-link extraction, the two-history Gram, any gravity
     result and any UNIQUE SELECTION of a section point all declared NOT
     CLAIMED as measured constants.
  C  THE DERIVED REFLECTION: the two primary-body citation pins, orthogonality,
     R^2 = -I against the 32-entry +I residual, the involutive conjugation
     action, nilpotency and rank of d_ref, the eight non-identities that put it
     outside the guessed family, the 16/16 jump census against d_00's 32/0 with
     the fixed-census defect at EXACTLY 16 and the co-transported census at
     ZERO, THE FLAT CONTROL at ZERO, the x-parity variant's honest involution
     and adjoint image, and the recorded naive-sweep band endpoints 352 / 368.
  D  THE CELL FACTORIZATION: all 32 cells exact with ONE M and the forced sign
     s = (-1)^t, M orthogonal, and M^2 = -I.
  E  THE DUAL BLOCK: the closed form exact at symbolic (q,v) and the six
     non-identities.
  F  THE HODGE-LEVEL THEOREM: the landed-field control, the exact theorem, and
     the two discriminating controls.
  G  THE SECTION POINTS: the conjugation table, the equal-weight 96 / 256
     failures with the reflected origin set at EXACTLY ZERO, the SIXTEEN closed
     sets with FIFTEEN proper and all PD, the minimal member {I, U_x}, the
     full-orbit point's closure / 32 positive minors / two-step covariance
     against the one-step control, and the action-level corollary.
  H  the note at its final path and the N5 fence, byte-identical.

BASELINE EXPECTATION: A through G PASS, with H failing on note-at-final-path
alone until the note is landed at docs/.

MUTATIONS
  THE SWEEP CONTRACT: fifteen declared mutations, each of which rewrites ONE
  CLAIM and must flip EXACTLY ONE FAMILY to FAIL.  Every measurement happens
  once, before any mutation flag is consulted, so a mutation can only rewrite a
  CLAIM and no gate can cascade into another.
    A  stale_main_authority, stale_parent_authority
    B  claim_objects_registered, claim_os_positivity, claim_selection_unique
    C  break_r_square, break_flat_control
    D  break_cell_factorization
    E  break_dual_block
    F  break_hodge_theorem
    G  break_conjugation_table, break_256, break_sym_closure, break_sym_pd
    H  drop_n5_fence
  BEFORE LANDING GATE H ALREADY FAILS AT BASELINE, on note-at-final-path alone,
  so drop_n5_fence cannot flip it and THE SWEEP IS RUN AT LANDING, once the note
  sits at docs/ and the baseline is 8 of 8 by family.

RUNNING
  python3 scripts/admissibility_dirac_kahler_derived_reflection_seam_dual_2026_08_24.py
  python3 ... --list-mutations
  python3 ... --mutation break_sym_closure

NOTES FOR THE LANDING AGENT
  1. NOTHING from any scratchpad is imported OR READ.  Every object below is
     rebuilt from the LANDED Block 128 runner
     scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py
     and from the Block 105 module it re-exports as `block105`, and the note is
     read at its FINAL PATH ONLY -- there is no draft fallback anywhere in this
     runner, so gate H FAILS until the note lands at docs/.
  2. EVERY CHECK IS EXACT.  sympy Rational, Integer and Symbol arithmetic only;
     no float enters any measured object and no tolerance is used anywhere.
  3. The N5 fence appears byte-identically in the note; gate H checks it as a
     raw substring.
  4. PARENT_COMMIT is REAL and PARENT_REF resolves to it; nothing needs sed, and
     CURRENT_MAIN was carried forward from the Block 182 runner and re-resolved
     at draft time.
  5. The stale pin is the Block 181 tip, a real ancestor of HEAD that predates
     Block 182 and carries NEITHER Block 182 artifact -- which is what makes the
     stale_parent_authority mutation bite.
  6. TWO SOLVE-SIDE CLAIMS WERE REFUTED BY THE ADVERSARIAL CHECK BEFORE LANDING
     AND THE CHECKER'S VERSION IS WHAT THIS RUNNER GATES.  (i) The solve
     recorded the derived reflection as "an involution (R^2 = I),
     grade-preserving"; BOTH HALVES ARE WRONG and the derivation itself is what
     forbids them -- R^2 = -I exactly, and the exterior census CO-TRANSPORTS
     with a 16-entry fixed-census defect.  (ii) The solve read
     reflection-closure as a SELECTION PRINCIPLE that might pin the Block 181
     section point; the checker exhibited SMALLER closed sets and the reading is
     REFUTED -- closure CONSTRAINS the moduli and never pins them.  Nothing else
     moves: every other statement in this block is a CONJUGATION, and a central
     sign and a co-transported grade change none of them.
  7. Re-run at landing; gate H should then pass, the battery should be 8/8 by
     family, and the fifteen-mutation sweep should be run then.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

# THE MACHINERY IMPORT, LANDED.  Block 128 is the CARRIER parent: it carries the
# certified Block 105 curved carrier, the 8x4 cover, the cover embedding whose
# corner order IS the form basis, the chart differentials and the completion
# convention, and it re-exports Block 105 as `block105`, from which the shear
# Hodge block and the overlap field are read.  NOTHING from any scratchpad is
# imported or read anywhere in this runner.
try:
    import admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17 as b128
    MACHINERY_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b128 = None
    MACHINERY_IMPORT_LANDED = False

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_DERIVED_REFLECTION_SEAM_DUAL_BOUNDED_"
    "THEOREM_NOTE_2026-08-24.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

ORIGINS = ((0, 0), (0, 1), (1, 0), (1, 1))

# THE STACK PARENT'S TWO ARTIFACTS.  Block 182 is the commit this block's branch
# is cut from, and its note and its runner are the pair that distinguishes the
# parent pin from the stale pin: both exist at PARENT_COMMIT and NEITHER exists
# at STALE_PARENT_COMMIT.
BLOCK182_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DUAL_PATCH_PULLBACK_SECTION_FRAME_BOUNDED_"
    "THEOREM_NOTE_2026-08-24.md"
)
BLOCK182_RUNNER = (
    "scripts/admissibility_dirac_kahler_dual_patch_pullback_section_frame_2026_08_24.py"
)
PARENT_ARTIFACTS = (BLOCK182_NOTE, BLOCK182_RUNNER)
PARENT_ARTIFACT_BLOBS = (
    "dc95799fa18e21e5a5d125001e20f481e2b32433",   # Block 182 note
    "3f9da0683ce6f9ad6137042726a282fb355df5c9",   # Block 182 runner
)
# THE SECTION-POINT PARENT, whose equal-weight point this block tests and whose
# 128-dimensional moduli this block constrains without pinning.
BLOCK181_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_COMMON_DIFFERENTIAL_SECTION_BOUNDED_"
    "THEOREM_NOTE_2026-08-24.md"
)
# THE CARRIER PARENT, read and imported rather than pinned.
BLOCK128_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_"
    "NOTE_2026-08-17.md"
)
BLOCK128_RUNNER = (
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py"
)
# THE TWO PRIMARY BODIES THE DERIVATION IS READ FROM.  Block 105 supplies the
# time-reflection pullback P_t = diag(1,1,-1,-1) (its equation 32) and the
# seam-frame-overlap next gate; Block 104 supplies the bond reflection
# theta(t) = -1-t (its equations 36 and 38) and the antilinearity language.
BLOCK105_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_"
    "HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
BLOCK104_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WICK_PHASE_FINE_SITE_STAGGERED_OS_LORENTZ_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
CAMPAIGN_NOTE = ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md"

# Deliberately literal: this is the complete audit read surface.  Every entry is
# a WORKTREE-READABLE path at landing time -- this block's own note excepted,
# since it lands later and gate H is the gate that owns it.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DERIVED_REFLECTION_SEAM_DUAL_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DUAL_PATCH_PULLBACK_SECTION_FRAME_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_dirac_kahler_dual_patch_pullback_section_frame_2026_08_24.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_COMMON_DIFFERENTIAL_SECTION_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WICK_PHASE_FINE_SITE_STAGGERED_OS_LORENTZ_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md",
)
# THE BLOCK'S OWN NOTE is the one audit input gate A does NOT require readable,
# because it does not exist until landing and gate H is the gate that owns it.
SELF_NOTE_INPUT = AUDIT_INPUT_PATHS[0]

AUDIT_TIMEOUT_SEC = 600
# THE FIVE-PIN AUTHORITY BLOCK, single-line hex literals refreshed by anchored
# sed at landing.  CARRIED FORWARD FROM THE BLOCK 182 RUNNER AND RE-RESOLVED AT
# DRAFT TIME.
CURRENT_MAIN = "c79384cb8ffa27fcb53cb89c53a84a708442eaad"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
# This block stacks on the Block 182 tip, so the parent branch is that.
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block182-"
              "dual-patch-pullback-section-frame-20260824")
PARENT_COMMIT = "9900b2f21e57a732637c8af7ab03667f919e956d"
# The Block 181 tip: a real ancestor of HEAD that predates Block 182 and
# therefore carries NEITHER Block 182 artifact.  Read ONLY under the stale
# mutation, where the missing blobs are exactly what makes it bite.
STALE_PARENT_COMMIT = "40f2e979bb64d264af679141f40aff1646e95029"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_os_positivity",
    "claim_selection_unique",
    "break_r_square",
    "break_flat_control",
    "break_cell_factorization",
    "break_dual_block",
    "break_hodge_theorem",
    "break_conjugation_table",
    "break_256",
    "break_sym_closure",
    "break_sym_pd",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_objects_registered": "B",
    "claim_os_positivity": "B",
    "claim_selection_unique": "B",
    "break_r_square": "C",
    "break_flat_control": "C",
    "break_cell_factorization": "D",
    "break_dual_block": "E",
    "break_hodge_theorem": "F",
    "break_conjugation_table": "G",
    "break_256": "G",
    "break_sym_closure": "G",
    "break_sym_pd": "G",
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
        # THE STALE LEG.  At the Block 181 tip NEITHER Block 182 artifact
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
    "the certified Block 105 curved carrier exactly as landed by Block 128 and re-used by Blocks 181 and 182 -- the 8x4 cover of dimension 32, the parameterized cover Hodge over the LANDED Block 105 overlap field, the chart differential d_00 and the completion convention Q(H,d) = m*H + i*(H d + d^H H) at SYMBOLIC POSITIVE MASS",
    "the DERIVED bond reflection R = P_edge * tpar, with P_edge the site permutation t -> 7-t read off Block 104's theta(t) = -1-t and tpar = diag((-1)^(t%2)) read off Block 105's P_t = diag(1,1,-1,-1), together with its x-parity control variant P_edge * diag((-1)^x)",
    "the cell map M = [[0,0,-1,0],[0,0,0,-1],[1,0,0,0],[0,1,0,0]] and the dual block M H(q,v) M^T built from Block 105's shear Hodge at symbolic (q,v)",
    "the cell field reflection theta(t,x) = ((2-t)%4, x) with the parameterized cover Hodge H[g] and its dual H_dual[g]",
    "the section-point family: the Block 181 equal-weight four-origin average H_s, the reflection-closed sixteen-shift full-orbit average H_sym, and every equal-weight orbit-constant set between them, all crossed with the x-offsets {I, U_x}",
    "the exterior grade N = diag(t%2 + x%2) taken from Block 106 through Block 182, together with its co-transport R N R^-1",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
# THE BANNER'S SECOND HALF, AS DECLARED MEASURED CONSTANTS rather than prose, so
# the B mutations bite on an object.  ALL FIVE ARE FALSE AND STAY FALSE.  The
# reflection is CONSTRUCTED and its covariance MEASURED; no positivity of any
# pairing is asserted, the dt=+-1 temporal-link band is NOT extracted, no
# two-history Gram is built, no gravity result exists here, and NO UNIQUE
# SELECTION of a section point exists -- gate G exhibits fifteen smaller closed
# sets, so uniqueness is REFUTED and not merely unclaimed.
OS_POSITIVITY_CLAIMED = False
TEMPORAL_LINK_CLAIMED = False
TWO_HISTORY_GRAM_CLAIMED = False
GRAVITY_CLAIMED = False
SELECTION_UNIQUENESS_CLAIMED = False

# THE EXPECTED VALUES, declared as literals so every claim below is auditable
# against the note without reading the code that measures it.
ZERO_RESIDUAL = 0
COVER_DIM = 32
CELL_COUNT = 32
DIFFERENTIAL_RANK = 16
DIFFERENTIAL_ENTRIES = 32
FIXED_CENSUS_DEFECT = 16
JUMP_DOWN_COUNT = 16
JUMP_UP_COUNT = 16
NAIVE_LOW_RESIDUAL = 352
NAIVE_HIGH_RESIDUAL = 368
EQUAL_WEIGHT_HODGE_RESIDUAL = 96
EQUAL_WEIGHT_ACTION_RESIDUAL = 256
ONE_STEP_CONTROL_RESIDUAL = 192
MINIMAL_VERSUS_FULL_ENTRIES = 96
SYM_SHIFT_COUNT = 16
MINIMAL_SHIFT_COUNT = 2
REFLECTION_ORBIT_COUNT = 5
CLOSED_SET_COUNT = 16
PROPER_CLOSED_SET_COUNT = 15
LEADING_MINOR_COUNT = 32

# THE DERIVATION'S CITATION PINS, read from the two PRIMARY BODIES so the
# derivation has a measured referent and is never a recollection.
B105_REFLECTION_PIN = "P_t=diag(1,1,-1,-1)"
B105_SEAM_PIN = "seam-frame overlap"
B104_BOND_PIN = "theta(t)=-1-t"
B104_ANTILINEAR_PIN = "reflection is anti-linear"

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


def positive_definite(matrix: sp.Matrix) -> bool:
    """SYMMETRY PLUS 32 EXACTLY POSITIVE LEADING PRINCIPAL MINORS.  Exact
    rational determinants by the Berkowitz algorithm: no eigenvalue estimate,
    no numerical factorization and no tolerance enters the decision."""
    if residual_count(matrix - matrix.T) != 0:
        return False
    return all(matrix[:size, :size].det(method="berkowitz") > 0
               for size in range(1, matrix.rows + 1))


# ---------------------------------------------------------------------------
# the cover: the shift cocycle, the chart differentials, the reflection
# ---------------------------------------------------------------------------
T_COVER, X_EXTENT = b128.COVER_TIME_EXTENT, b128.SPACE_EXTENT
PHYSICAL_T = b128.PHYSICAL_TIME_EXTENT
N_COVER = T_COVER * X_EXTENT
MASS = b128.MASS
IU = sp.I
SYMBOLIC_MASS = sp.Symbol("m", positive=True)
SHEAR_SYMBOL, VOLUME_SYMBOL = sp.symbols("q v")

# THE CELL MAP.  A signed corner swap: it exchanges the scalar slot with the dt
# slot and the dx slot with the dx^dt slot, with the sign that makes M^2 = -I.
CELL_MAP = sp.Matrix([[0, 0, -1, 0],
                      [0, 0, 0, -1],
                      [1, 0, 0, 0],
                      [0, 1, 0, 0]])


def cover_shift(dt: int, dx: int) -> sp.Matrix:
    """The PLAIN translation on the cover: no staggered sign is needed."""
    shift = sp.zeros(N_COVER, N_COVER)
    for t in range(T_COVER):
        for x in range(X_EXTENT):
            shift[b128.cover_index(t + dt, x + dx), b128.cover_index(t, x)] = 1
    return shift


def edge_reflection() -> sp.Matrix:
    """P_edge: the SITE permutation t -> 7-t on the 8x4 cover.  This is Block
    104's bond convention theta(t) = -1-t made single-valued by the staggered
    one-component-per-site identification: the bond map [t,t+1] -> [-2-t,-1-t]
    is a site map because each site carries exactly one component."""
    matrix = sp.zeros(N_COVER, N_COVER)
    for t in range(T_COVER):
        for x in range(X_EXTENT):
            matrix[b128.cover_index(T_COVER - 1 - t, x),
                   b128.cover_index(t, x)] = 1
    return matrix


def time_parity() -> sp.Matrix:
    """tpar = diag((-1)^(t%2)): Block 105's P_t = diag(1,1,-1,-1) pullback
    written on this carrier.  The corner order (00,01,10,11) IS the form basis
    (1, dx, dt, dx^dt), so the dt-carrying corners are exactly the odd-t sites
    and the form parity is the t-parity."""
    return sp.diag(*[sp.Integer(-1) ** (t % 2)
                     for t in range(T_COVER) for _ in range(X_EXTENT)])


def space_parity() -> sp.Matrix:
    """diag((-1)^x): the x-parity dressing, kept as the CONTROL variant."""
    return sp.diag(*[sp.Integer(-1) ** x
                     for _ in range(T_COVER) for x in range(X_EXTENT)])


def exterior_grade() -> sp.Matrix:
    """deg = t%2 + x%2 on the cover, Block 106's census as Block 182 carried
    it forward -- not a degree invented here."""
    return sp.diag(*[sp.Integer((t % 2) + (x % 2))
                     for t in range(T_COVER) for x in range(X_EXTENT)])


def grade_jump_census(operator: sp.Matrix, grade: sp.Matrix) -> dict:
    """THE JUMP CENSUS: for every nonzero entry of `operator`, the exact grade
    difference it carries.  A pure grade-raising operator has every entry at
    +1; anything else is exhibited here rather than described."""
    operator = sp.expand(operator)
    census: dict = {}
    for row in range(operator.rows):
        for column in range(operator.cols):
            if operator[row, column] == 0:
                continue
            jump = int(grade[row, row] - grade[column, column])
            census[jump] = census.get(jump, 0) + 1
    return census


def completion(hodge: sp.Matrix, differential: sp.Matrix,
               mass: object = SYMBOLIC_MASS) -> sp.Matrix:
    """The LANDED b128 completion convention, applied to a supplied pairing, at
    SYMBOLIC POSITIVE MASS by default so every identity below is an operator
    identity in m and not a coincidence at MASS = 2/7."""
    return sp.expand(mass * hodge
                     + IU * (hodge * differential + differential.H * hodge))


def dual_completion(hodge: sp.Matrix, differential: sp.Matrix) -> sp.Matrix:
    """The SAME convention written in the dual frame, for the action-level
    consistency certificate."""
    return completion(hodge, differential)


def shear_block(shear: object, volume: object) -> sp.Matrix:
    """The LANDED Block 105 shear Hodge, read through Block 128."""
    return b128.block105.shear_hodge(shear, volume)


def dual_block(shear: object, volume: object) -> sp.Matrix:
    """THE DUAL BLOCK, M H(q,v) M^T.  Gate E exhibits its closed form."""
    return sp.expand(CELL_MAP * shear_block(shear, volume) * CELL_MAP.T)


DUAL_BLOCK_CLOSED_FORM = sp.Matrix([
    [-VOLUME_SYMBOL / (SHEAR_SYMBOL ** 2 - 1), 0, 0,
     -SHEAR_SYMBOL * VOLUME_SYMBOL / (SHEAR_SYMBOL ** 2 - 1)],
    [0, 1 / VOLUME_SYMBOL, 0, 0],
    [0, 0, VOLUME_SYMBOL, 0],
    [-SHEAR_SYMBOL * VOLUME_SYMBOL / (SHEAR_SYMBOL ** 2 - 1), 0, 0,
     -VOLUME_SYMBOL / (SHEAR_SYMBOL ** 2 - 1)]])


def hodge_cover(field: dict, block=shear_block) -> sp.Matrix:
    """THE PARAMETERIZED COVER HODGE H[g], with the CELL BLOCK left free.  With
    `block = shear_block` this is the LANDED b128 curved_hodge_cover
    construction with the field free -- gate F controls it against the landed
    object -- and with `block = dual_block` it is the DUAL-FRAME Hodge."""
    result = sp.zeros(N_COVER, N_COVER)
    for t in range(T_COVER):
        for x in range(X_EXTENT):
            shear, volume = field[(t % PHYSICAL_T, x)]
            embedding = b128.cover_embedding(t, x)
            result += embedding * block(shear, volume) * embedding.T / 4
    return sp.expand(result)


def reflected_field(field: dict) -> dict:
    """theta on the CELL field: (t,x) -> ((2-t)%4, x).  This is the field-side
    shadow of the site map t -> 7-t: a cell at t maps to the cell at 6-t, and
    the field has period 4 in t, so 6-t reduces to (2-t)%4."""
    return {(t, x): field[((2 - t) % PHYSICAL_T, x)]
            for t in range(PHYSICAL_T) for x in range(X_EXTENT)}


def shifted_field(field: dict, dt: int, dx: int) -> dict:
    """Block 106's ACTIVE field translation convention (T_a g)_(n+a) = g_n, as
    Block 182 carried it forward."""
    return {(t, x): field[((t - dt) % PHYSICAL_T, (x - dx) % X_EXTENT)]
            for t in range(PHYSICAL_T) for x in range(X_EXTENT)}


def orbit_average(matrix: sp.Matrix, shifts: tuple) -> sp.Matrix:
    """(1/|S|) sum_{S} S^T A S -- the section-point construction, with the shift
    set supplied so every point in the family is built by the SAME code and the
    points differ ONLY in their shift set."""
    return sp.expand(
        sum([shift.T * matrix * shift for shift in shifts],
            sp.zeros(N_COVER, N_COVER)) / len(shifts))


def reflection_orbits() -> tuple:
    """THE REFLECTION ORBITS OF THE TEMPORAL EXPONENTS, k ~ -k mod 8.  Gate G
    uses them because the conjugation table says closure needs nothing more
    than reflection-symmetric temporal weights."""
    orbits = []
    seen: set = set()
    for step in range(T_COVER):
        if step in seen:
            continue
        orbit = tuple(sorted({step, (-step) % T_COVER}))
        orbits.append(orbit)
        seen |= set(orbit)
    return tuple(orbits)


def equal_weight_closed_sets() -> tuple:
    """EVERY equal-weight union of reflection orbits that contains exponent 0:
    the complete family of equal-weight reflection-closed temporal exponent
    sets, enumerated rather than sampled."""
    orbits = reflection_orbits()
    others = tuple(orbit for orbit in orbits if 0 not in orbit)
    sets = []
    for size in range(len(others) + 1):
        for choice in combinations(others, size):
            sets.append(tuple(sorted(
                {0} | {step for orbit in choice for step in orbit})))
    return tuple(sets)


def note_text() -> tuple:
    """(text, at_final_path).  THE FINAL PATH IS THE ONLY PATH READ: there is no
    draft fallback anywhere in this runner, so before landing the text is empty
    and gate H fails on note-at-final-path alone."""
    try:
        return NOTE_PATH.read_text(encoding="utf-8"), True
    except OSError:
        return "", False


def landed_text(path: str) -> str:
    """A LANDED PRIMARY BODY, read at its own path in the worktree.  Gate C
    reads the Block 104 and Block 105 notes through this and through nothing
    else -- the Block 182 process rule, that every citation is checked against
    the primary body and never against a summary, applied to the two notes this
    block's derivation is built out of."""
    try:
        return (ROOT / path).read_text(encoding="utf-8")
    except OSError:
        return ""


# ---------------------------------------------------------------------------
# THE N5 FENCE.  Single-line literal with \n separators; it appears
# BYTE-IDENTICALLY in the note and gate H checks it as a raw substring.
# ---------------------------------------------------------------------------
N5_FENCE = "N5: per_element: THE IMPOSED-OBJECT BANNER, FIRST AND WITH TEETH. NOTHING HERE IS REGISTERED OR ADOPTED -- the certified Block 105 curved carrier as landed by Block 128 and re-used by Blocks 181 and 182 (the 8x4 cover of dimension 32, the parameterized cover Hodge over the LANDED Block 105 overlap field, the chart differential d_00, and the completion Q(H,d) = m*H + i*(H d + d^H H) at SYMBOLIC POSITIVE MASS), the DERIVED bond reflection R = P_edge * tpar with P_edge the site permutation t -> 7-t and tpar = diag((-1)^(t%2)) together with its x-parity control variant, the cell map M = [[0,0,-1,0],[0,0,0,-1],[1,0,0,0],[0,1,0,0]] and the dual block M H(q,v) M^T, the cell field reflection theta(t,x) = ((2-t)%4, x) with the parameterized Hodge H[g] and its dual H_dual[g], the section-point family from the Block 181 equal-weight four-origin average through every equal-weight orbit-constant set to the sixteen-shift full-orbit average, and the exterior grade N = diag(t%2 + x%2) with its co-transport R N R^-1 are IMPOSED MEASURED OBJECTS OF THIS BLOCK, rebuilt from the LANDED Block 128 runner and the Block 105 module it re-exports and from NOTHING in any scratchpad. NO OS OR REFLECTION-POSITIVITY THEOREM IS CLAIMED; NO TEMPORAL-LINK EXTRACTION IS PERFORMED, the dt=+-1 band being left to the successor; NO TWO-HISTORY GRAM IS BUILT; NO GRAVITY RESULT IS CLAIMED; AND NO UNIQUE SELECTION OF A SECTION POINT EXISTS OR IS CLAIMED -- uniqueness is REFUTED by fifteen exhibited smaller closed sets, not merely left unclaimed, and the banner key is gated as a declared constant. NOTHING IS REGISTERED, NOTHING IS ADOPTED, AND NO AXIOM AMENDMENT IS JUSTIFIED.\nper_site: THE NEGATIVE GRIDS ARE THE DERIVATION PATH, AND THEY COME BEFORE THE POSITIVE RESULT. The reflection was not guessed into place: an EIGHT-CELL naive sweep (two site reflections x flipped/unflipped field x dagger/plain target) failed with every residual in the band 352-368, a TWENTY-CANDIDATE dressed grid mapped d_00 onto NONE of the guessed family, and a SIXTEEN-TARGET diagonal-intertwiner solve failed too. TWO OF THE THREE ARE RE-MEASURED HERE AS PINNED CERTIFICATES: the undressed edge reflection of the Block 181 equal-weight curved action against the plain unflipped target at the theta-reflected field has residual EXACTLY 352 with the edge-transported differential and EXACTLY 368 with the differential held fixed -- the recorded band's two endpoints -- and the DERIVED conjugate d_ref = R d_00 R^-1 sits outside the guessed family at all EIGHT non-identities against {+-d_00, +-d_00^H, +-d_10, +-d_10^H}. THE FAILURES FORCED THE DERIVATION AND ARE RECORDED AS THE PATH, NOT AS CORRECTIONS.\nper_mode: THE REFLECTION IS DERIVED FROM THE CARRIER AND IT SQUARES TO MINUS ONE. cover_embedding's corner order (00,01,10,11) IS the form basis (1,dx,dt,dx^dt); Block 104's bond convention theta(t) = -1-t, read from its primary body, acts on cells [t,t+1] -> [-2-t,-1-t]; the staggered one-component-per-site identification makes the site map t -> 7-t single-valued; and the form parity that goes with it is Block 105's own P_t = diag(1,1,-1,-1) pullback, which on this carrier is tpar = diag((-1)^(t%2)). SO R = P_edge * tpar AND NOTHING ABOUT IT IS A CHOICE. MEASURED: R is REAL ORTHOGONAL with R R^T = I so R^-1 = R^T = -R; R^2 = -I EXACTLY against a 32-entry residual for +I, a PROJECTIVE involution with R^4 = I whose conjugation action on operators is nonetheless an exact involution; d_ref = R d_00 R^-1 is NILPOTENT of rank 16; and THE FLAT CONTROL IS EXACT, R Q(I,d_00) R^-1 = Q(I,d_00) at ZERO residual, with the x-parity variant an HONEST involution sending the flat completion to its adjoint, R_x Q R_x^-1 = Q^H = Q^T exactly. AND THE GRADE CO-TRANSPORTS FOR THE THIRD TIME IN THIS LANE: d_00 carries all 32 of its nonzero entries at grade jump +1 while d_ref splits EXACTLY 16 down and 16 up, so the FIXED census N = diag(t%2 + x%2) has a commutator defect of EXACTLY 16 ENTRIES while the CO-TRANSPORTED census R N R^-1 closes it at ZERO. THE KRAMERS READING of R^2 = -I -- a T^2 = -1 signature on a fermionic carrier -- IS A READING ONLY, untested here, and NOTHING is claimed from it.\nper_block: THE CELL FACTORIZATION, AND THE COMPLEX STRUCTURE ON THE CELL. For EVERY ONE of the 32 cells, R emb(t,x) = emb((6-t)%8, x) * (s*M) with s = (-1)^t and with ONE 4x4 M for every cell, at zero residual; M is orthogonal and M^2 = -I EXACTLY. THE SIGN IS FORCED, because a single M at every cell requires the dressing to alternate, and with it R^2 = -I is forced too: theta(t) = 6-t preserves t-parity, so the two cell signs multiply to +1 and R^2 emb(c) = emb(c) M^2 = -emb(c). M IS A COMPLEX STRUCTURE ON THE CELL AND THAT IS A MEASURED FACT ABOUT THE CARRIER, NOT AN INTERPRETATION.\nlattice_wide: THE DUAL BLOCK IN CLOSED FORM AND THE HODGE-LEVEL THEOREM. At SYMBOLIC (q,v), M H(q,v) M^T = [[-v/(q^2-1), 0, 0, -q*v/(q^2-1)], [0, 1/v, 0, 0], [0, 0, v, 0], [-q*v/(q^2-1), 0, 0, -v/(q^2-1)]] EXACTLY, and it is NOT H(q,v), NOT H(-q,v), NOT either inverse, NOT H(q,1/v) and NOT H(-q,1/v) -- six explicit non-identities. AND THE THEOREM: R H[g] R^-1 = H_dual[theta g] EXACTLY at the LANDED field, with the LANDED-FIELD CONTROL FIRST -- H[landed field] IS the LANDED curved_hodge_cover() at zero residual -- and with two discriminating controls measured in the same run: the UNDRESSED site reflection does NOT satisfy it, and the dressed reflection against the UNDUALIZED target does not either. THE READING THAT THE SHEAR MIGRATES from the (dx,dt) coupling to the (scalar,dx^dt) coupling with the 1/(1-q^2) factor -- the ADM data in the dual frame -- IS A READING AND IS MARKED AS ONE.\nper_scope: WHAT REFLECTION CLOSURE RULES OUT, WHAT IT ADMITS, AND WHAT IT NEVER PINS. THE MECHANISM IS A CONJUGATION TABLE: R U_t R^-1 = -U_t^-1 EXACTLY against a 32-entry residual for +U_t^-1, and R U_x R^-1 = U_x EXACTLY, so congruence-level closure of an orbit-averaged point needs only reflection-symmetric temporal weights w_k = w_{-k}. IT RULES OUT THE BLOCK 181 EQUAL-WEIGHT POINT: its {0,1}^2 origin set maps to {0,-1}x{0,1}, so against the SAME origin set the Hodge-level residual is EXACTLY 96 entries and the action-level residual is EXACTLY 256, while against the REFLECTED origin set the Hodge-level residual is EXACTLY ZERO -- the mechanism exhibited and not described. AND IT ADMITS A WHOLE FAMILY RATHER THAN A POINT: the reflection orbits of the temporal exponents are {0}, {4}, {1,7}, {2,6}, {3,5}, and ALL SIXTEEN equal-weight unions containing 0, crossed with {I, U_x}, close EXACTLY and are POSITIVE DEFINITE by 32 exact leading minors -- FIFTEEN of them PROPER subsets of the full orbit, with {I, U_x} the MINIMAL member, which also carries the two-step covariance and differs from the full-orbit point at 96 entries. REFLECTION CLOSURE CONSTRAINS THE BLOCK 181 MODULI AND NEVER PINS THEM; NO UNIQUE SELECTOR EXISTS AND NONE IS CLAIMED. At the full-orbit point the same package holds and the action-level identity R Q(H_sym[g], d_00) R^-1 = m H_sym_dual + i(H_sym_dual d_ref + d_ref^H H_sym_dual) is EXACT -- A FORMAL COROLLARY of the Hodge-level closure plus orthogonality and the distribution of conjugation, ADDING NO INDEPENDENT CONSTRAINT ONCE THE CLOSURE AND THE DEFINITIONS ARE ESTABLISHED, and gated as a consistency certificate.\nRESULT: THE TIME REFLECTION IS DERIVED FROM THE CARRIER, IT SQUARES TO MINUS ONE, THE SEAM PAIRS THE FRAME WITH A DUAL FRAME, AND REFLECTION CLOSURE CONSTRAINS THE SECTION MODULI WITHOUT PINNING THEM. R = P_edge * tpar is constructed from the embedding correspondence after three guess programs failed; the cell factorization carries ONE M with M^2 = -I; the dual block is exhibited in closed form and separated from six neighbours; R H[g] R^-1 = H_dual[theta g] is EXACT; the Block 181 equal-weight point fails closure at 96 and 256 while its reflected origin set is EXACT; and sixteen orbit-constant points close exactly and are positive definite, fifteen of them smaller than the full orbit. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\nDECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is EDITED; no landed number is touched; Blocks 104, 105, 128, 181 and 182 STAND EXACTLY AS LANDED; the bar items stay PROPOSALS, and PROPOSALS STAY PROPOSALS. THIS BLOCK'S OWN DEFECTS ARE DISCLOSED: it is a SINGLE FIXTURE FAMILY, the b128 8x4 cover over the certified Block 105 curved carrier at ONE field, with NO width ladder, NO second carrier rule and NO quotient statement; THE FRAME-PAIRS-WITH-DUAL-FRAME READING IS A READING and not a theorem, as is the ADM migration reading and the Kramers reading of R^2 = -I; THE ACTION-LEVEL IDENTITY IS A FORMAL COROLLARY that adds no independent constraint; NO OS OR REFLECTION-POSITIVITY THEOREM IS CLAIMED and no pairing is shown positive; the temporal-link band is NOT extracted and no two-history Gram is built; and the whole block is KINEMATIC FRAME DATA. AND TWO SOLVE-SIDE CLAIMS WERE REFUTED BY THE ADVERSARIAL CHECK BEFORE LANDING AND THE CHECKER'S VERSION IS WHAT SHIPS: R^2 = -I with a CO-TRANSPORTING census, against the solve's involution-and-grade-preserving sentence; and reflection closure as a CONSTRAINT rather than a SELECTOR, against the solve's uniqueness reading, which fifteen exhibited smaller closed sets refute. PROVENANCE: CAMPAIGN_20260824_GRAVITY_MAINLINE.md, at its G4 OPENED, G4 DERIVED-REFLECTION SOLVE and G4 CORE THEOREM PROVEN anchors, as corrected by the b183 adversarial check.\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero."


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
        "os_positivity_claimed": OS_POSITIVITY_CLAIMED,
        "temporal_link_claimed": TEMPORAL_LINK_CLAIMED,
        "two_history_gram_claimed": TWO_HISTORY_GRAM_CLAIMED,
        "gravity_claimed": GRAVITY_CLAIMED,
        "selection_uniqueness_claimed": SELECTION_UNIQUENESS_CLAIMED,
        # C -- the derived reflection.
        "citation_pins": True,
        "reflection_is_orthogonal_residual": ZERO_RESIDUAL,
        "r_square_residual": ZERO_RESIDUAL,
        "r_square_against_identity": COVER_DIM,
        "adjoint_involution_residual": ZERO_RESIDUAL,
        "d_ref_nilpotency_residual": ZERO_RESIDUAL,
        "d_ref_rank": DIFFERENTIAL_RANK,
        "d_ref_outside_family": True,
        "d_ref_jump_census": {-1: JUMP_DOWN_COUNT, 1: JUMP_UP_COUNT},
        "base_jump_census": {1: DIFFERENTIAL_ENTRIES},
        "fixed_census_defect": FIXED_CENSUS_DEFECT,
        "transported_census_residual": ZERO_RESIDUAL,
        "flat_control_residual": ZERO_RESIDUAL,
        "xpar_square_residual": ZERO_RESIDUAL,
        "xpar_adjoint_residual": ZERO_RESIDUAL,
        "naive_low_residual": NAIVE_LOW_RESIDUAL,
        "naive_high_residual": NAIVE_HIGH_RESIDUAL,
        # D -- the cell factorization.
        "cell_factorization_failures": 0,
        "cells_checked": CELL_COUNT,
        "cell_map_square_residual": ZERO_RESIDUAL,
        "cell_map_orthogonal_residual": ZERO_RESIDUAL,
        # E -- the dual block.
        "dual_block_residual": ZERO_RESIDUAL,
        "dual_block_separations": 6,
        # F -- the Hodge-level theorem.
        "hodge_control_residual": ZERO_RESIDUAL,
        "hodge_theorem_residual": ZERO_RESIDUAL,
        "undressed_hodge_control": True,
        "undualized_hodge_control": True,
        # G -- the section points.
        "temporal_conjugation_residual": ZERO_RESIDUAL,
        "temporal_conjugation_against_plus": COVER_DIM,
        "spatial_conjugation_residual": ZERO_RESIDUAL,
        "equal_weight_hodge_residual": EQUAL_WEIGHT_HODGE_RESIDUAL,
        "reflected_origin_set_residual": ZERO_RESIDUAL,
        "equal_weight_action_residual": EQUAL_WEIGHT_ACTION_RESIDUAL,
        "reflection_orbit_count": REFLECTION_ORBIT_COUNT,
        "closed_set_count": CLOSED_SET_COUNT,
        "proper_closed_set_count": PROPER_CLOSED_SET_COUNT,
        "closed_sets_all_closed": True,
        "closed_sets_all_positive_definite": True,
        "minimal_shift_count": MINIMAL_SHIFT_COUNT,
        "minimal_closure_residual": ZERO_RESIDUAL,
        "minimal_positive_definite": True,
        "minimal_two_step_residual": ZERO_RESIDUAL,
        "minimal_versus_full_entries": MINIMAL_VERSUS_FULL_ENTRIES,
        "sym_closure_residual": ZERO_RESIDUAL,
        "sym_shift_count": SYM_SHIFT_COUNT,
        "sym_positive_definite": True,
        "sym_leading_minors": LEADING_MINOR_COUNT,
        "two_step_residual": ZERO_RESIDUAL,
        "one_step_control_residual": ONE_STEP_CONTROL_RESIDUAL,
        "sym_action_residual": ZERO_RESIDUAL,
        "mass_is_symbolic": True,
        # H -- the note and the fence.
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
    elif mutation == "claim_os_positivity":
        # THE SCOPE OVERSOLD: the derived reflection asserted to supply an OS or
        # reflection-positivity theorem, which a covariance identity alone never
        # supplies -- no pairing is shown positive anywhere in this block.
        claims["os_positivity_claimed"] = True
    elif mutation == "claim_selection_unique":
        # THE REFUTED READING RE-ASSERTED: reflection-closure asserted to pin the
        # section point UNIQUELY, which the FIFTEEN smaller closed sets gate G
        # exhibits forbid outright.  This is the mutation that guards the
        # correction the adversarial check forced.
        claims["selection_uniqueness_claimed"] = True
    elif mutation == "break_r_square":
        # THE SQUARE RE-ASSERTED AS +I: the solve's original sentence, restored,
        # which the exact R^2 = -I forbids -- and which gate D's M^2 = -I with
        # the parity-even cell sign forbids structurally as well.
        claims["r_square_residual"] = COVER_DIM
        claims["r_square_against_identity"] = ZERO_RESIDUAL
    elif mutation == "break_flat_control":
        # THE CONTROL DELETED: a nonzero flat-completion residual asserted
        # allowed, which the exact flat control forbids -- and the flat control
        # is what stops the reflection being a curved-only artifact.
        claims["flat_control_residual"] = 4
    elif mutation == "break_cell_factorization":
        # THE ONE-M FACTORIZATION DENIED: a failing cell asserted allowed, which
        # the exact 32-cell factorization with a single M forbids.
        claims["cell_factorization_failures"] = 1
    elif mutation == "break_dual_block":
        # THE CLOSED FORM BROKEN: a nonzero residual against the exhibited dual
        # block asserted allowed at symbolic (q,v), which the exact closed form
        # forbids.
        claims["dual_block_residual"] = 4
    elif mutation == "break_hodge_theorem":
        # THE THEOREM DELETED: a nonzero R H[g] R^-1 - H_dual[theta g] residual
        # asserted allowed, which the exact Hodge-level closure forbids.
        claims["hodge_theorem_residual"] = 4
    elif mutation == "break_conjugation_table":
        # THE MECHANISM INVERTED: R U_t R^-1 asserted to be +U_t^-1, which the
        # measured 32-entry residual against +U_t^-1 forbids.  The sign is what
        # makes the shift set close, so denying it denies the whole selection
        # analysis.
        claims["temporal_conjugation_residual"] = COVER_DIM
        claims["temporal_conjugation_against_plus"] = ZERO_RESIDUAL
    elif mutation == "break_256":
        # THE EQUAL-WEIGHT FAILURE ERASED: the Block 181 point asserted
        # reflection-closed at the action level, which the measured 256-entry
        # residual forbids -- and erasing it would erase the reason a different
        # point was needed at all.
        claims["equal_weight_action_residual"] = 0
    elif mutation == "break_sym_closure":
        # THE CLOSURE DELETED: a nonzero sixteen-shift closure residual asserted
        # allowed, which the exact closure forbids.
        claims["sym_closure_residual"] = 4
    elif mutation == "break_sym_pd":
        # THE SECTION POINT DEGRADED: H_sym asserted not positive definite,
        # which the 32 exactly positive leading minors forbid -- a Hodge that is
        # not PD is not a section point at all.
        claims["sym_positive_definite"] = False
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
    citation_pins: dict
    reflection_is_orthogonal_residual: int
    r_square_residual: int
    r_square_against_identity: int
    adjoint_involution_residual: dict
    d_ref_nilpotency_residual: int
    d_ref_rank: int
    d_ref_family: dict
    d_ref_jump_census: dict
    base_jump_census: dict
    fixed_census_defect: int
    transported_census_residual: int
    flat_control_residual: int
    xpar_square_residual: int
    xpar_adjoint_residual: int
    xpar_is_not_flat_fixing: int
    naive_low_residual: int
    naive_high_residual: int
    cell_factorization_failures: int
    cells_checked: int
    cell_map_square_residual: int
    cell_map_orthogonal_residual: int
    dual_block_residual: int
    dual_block_separations: dict
    hodge_control_residual: int
    hodge_theorem_residual: int
    undressed_hodge_residual: int
    undualized_hodge_residual: int
    temporal_conjugation_residual: int
    temporal_conjugation_against_plus: int
    spatial_conjugation_residual: int
    equal_weight_hodge_residual: int
    reflected_origin_set_residual: int
    equal_weight_action_residual: int
    reflection_orbits: tuple
    closed_set_count: int
    proper_closed_set_count: int
    closed_sets_all_closed: bool
    closed_sets_all_positive_definite: bool
    minimal_shift_count: int
    minimal_closure_residual: int
    minimal_positive_definite: bool
    minimal_two_step_residual: dict
    minimal_versus_full_entries: int
    sym_closure_residual: int
    sym_shift_count: int
    sym_positive_definite: bool
    sym_leading_minors: int
    two_step_residual: dict
    one_step_control_residual: int
    sym_action_residual: int
    mass_is_symbolic: bool


def measure() -> Facts:
    text, at_final_path = note_text()
    main_head = resolve_ref("origin/main")

    # --- the carrier, rebuilt from the LANDED Block 128 runner --------------
    Ut, Ux = cover_shift(1, 0), cover_shift(0, 1)
    d00 = sp.Matrix(b128.chart_differential_cover((0, 0)))
    d10 = sp.Matrix(b128.chart_differential_cover((1, 0)))
    grade = exterior_grade()
    field = b128.block105.overlap_field()
    theta_g = reflected_field(field)

    # --- C: the derived reflection -----------------------------------------
    P_edge = edge_reflection()
    R = sp.expand(P_edge * time_parity())
    # R IS REAL ORTHOGONAL, so its inverse is its transpose and conjugation by
    # it commutes with the adjoint.  No operator inverse is ever formed.
    R_inv = R.T
    reflection_is_orthogonal_residual = residual_count(R * R.T - sp.eye(N_COVER))
    r_square_residual = residual_count(R * R + sp.eye(N_COVER))
    r_square_against_identity = residual_count(R * R - sp.eye(N_COVER))
    d_ref = sp.expand(R * d00 * R_inv)
    H_field = hodge_cover(field)
    adjoint_involution_residual = {
        "d_00": residual_count(R * d_ref * R_inv - d00),
        "H": residual_count(R * (R * H_field * R_inv) * R_inv - H_field),
    }
    d_ref_nilpotency_residual = residual_count(d_ref * d_ref)
    d_ref_rank = d_ref.rank()
    d_ref_family = {
        "+d_00": residual_count(d_ref - d00),
        "-d_00": residual_count(d_ref + d00),
        "+d_00^H": residual_count(d_ref - d00.H),
        "-d_00^H": residual_count(d_ref + d00.H),
        "+d_10": residual_count(d_ref - d10),
        "-d_10": residual_count(d_ref + d10),
        "+d_10^H": residual_count(d_ref - d10.H),
        "-d_10^H": residual_count(d_ref + d10.H),
    }
    d_ref_jump_census = grade_jump_census(d_ref, grade)
    base_jump_census = grade_jump_census(d00, grade)
    fixed_census_defect = residual_count(
        grade * d_ref - d_ref * grade - d_ref)
    transported_grade = sp.expand(R * grade * R_inv)
    transported_census_residual = residual_count(
        transported_grade * d_ref - d_ref * transported_grade - d_ref)
    Q_flat = completion(sp.eye(N_COVER), d00)
    flat_control_residual = residual_count(R * Q_flat * R_inv - Q_flat)
    R_x = sp.expand(P_edge * space_parity())
    xpar_square_residual = residual_count(R_x * R_x - sp.eye(N_COVER))
    xpar_image = sp.expand(R_x * Q_flat * R_x.T)
    xpar_adjoint_residual = residual_count(xpar_image - Q_flat.H)
    xpar_is_not_flat_fixing = residual_count(xpar_image - Q_flat)

    # --- the recorded naive negatives, re-measured as pinned certificates ---
    four_shifts = tuple(
        sp.expand(Ut ** origin[0] * Ux ** origin[1]) for origin in ORIGINS)
    H_s = orbit_average(H_field, four_shifts)
    Q_s = completion(H_s, d00)
    H_s_theta = orbit_average(hodge_cover(theta_g), four_shifts)
    undressed_image = sp.expand(P_edge * Q_s * P_edge.T)
    d_edge = sp.expand(P_edge * d00 * P_edge.T)
    naive_low_residual = residual_count(
        undressed_image - completion(H_s_theta, d_edge))
    naive_high_residual = residual_count(
        undressed_image - completion(H_s_theta, d00))

    # --- D: the cell factorization -----------------------------------------
    cells_checked = 0
    cell_factorization_failures = 0
    for t in range(T_COVER):
        for x in range(X_EXTENT):
            cells_checked += 1
            sign = sp.Integer(-1) ** t
            image = sp.expand(R * sp.Matrix(b128.cover_embedding(t, x)))
            target = sp.expand(
                sp.Matrix(b128.cover_embedding((6 - t) % T_COVER, x))
                * (sign * CELL_MAP))
            if residual_count(image - target) != 0:
                cell_factorization_failures += 1
    cell_map_square_residual = residual_count(CELL_MAP * CELL_MAP + sp.eye(4))
    cell_map_orthogonal_residual = residual_count(
        CELL_MAP * CELL_MAP.T - sp.eye(4))

    # --- E: the dual block, at SYMBOLIC (q, v) ------------------------------
    reference = dual_block(SHEAR_SYMBOL, VOLUME_SYMBOL)
    dual_block_residual = nonzero_entries(
        sp.simplify(reference - DUAL_BLOCK_CLOSED_FORM))
    neighbours = {
        "H(q,v)": shear_block(SHEAR_SYMBOL, VOLUME_SYMBOL),
        "H(-q,v)": shear_block(-SHEAR_SYMBOL, VOLUME_SYMBOL),
        "H(q,v)^-1": shear_block(SHEAR_SYMBOL, VOLUME_SYMBOL).inv(),
        "H(-q,v)^-1": shear_block(-SHEAR_SYMBOL, VOLUME_SYMBOL).inv(),
        "H(q,1/v)": shear_block(SHEAR_SYMBOL, 1 / VOLUME_SYMBOL),
        "H(-q,1/v)": shear_block(-SHEAR_SYMBOL, 1 / VOLUME_SYMBOL),
    }
    dual_block_separations = {
        name: nonzero_entries(sp.simplify(reference - other))
        for name, other in neighbours.items()
    }

    # --- F: the Hodge-level theorem ----------------------------------------
    hodge_control_residual = residual_count(
        H_field - sp.Matrix(b128.curved_hodge_cover()))
    H_dual_theta = hodge_cover(theta_g, dual_block)
    hodge_theorem_residual = residual_count(R * H_field * R_inv - H_dual_theta)
    # THE TWO DISCRIMINATING CONTROLS, measured in the same run: drop the sign
    # dressing, or drop the dual block, and the identity dies.
    undressed_hodge_residual = residual_count(
        P_edge * H_field * P_edge.T - H_dual_theta)
    undualized_hodge_residual = residual_count(
        R * H_field * R_inv - hodge_cover(theta_g))

    # --- G: the mechanism, then the whole admitted family -------------------
    # THE CONJUGATION TABLE.  It is the mechanism behind every closure statement
    # below, and it is measured rather than argued.
    temporal_conjugation_residual = residual_count(R * Ut * R_inv + Ut.T)
    temporal_conjugation_against_plus = residual_count(R * Ut * R_inv - Ut.T)
    spatial_conjugation_residual = residual_count(R * Ux * R_inv - Ux)

    H_s_dual_theta = orbit_average(H_dual_theta, four_shifts)
    equal_weight_hodge_residual = residual_count(
        R * H_s * R_inv - H_s_dual_theta)
    # THE MECHANISM, EXHIBITED: the {0,1}^2 origin set maps to {0,-1}x{0,1} --
    # and against THAT set the Hodge-level residual is exactly zero.
    reflected_shifts = tuple(
        sp.expand(Ut.T ** origin[0] * Ux ** origin[1]) for origin in ORIGINS)
    reflected_origin_set_residual = residual_count(
        R * H_s * R_inv - orbit_average(H_dual_theta, reflected_shifts))
    equal_weight_action_residual = residual_count(
        R * Q_s * R_inv
        - dual_completion(H_s_dual_theta, d_ref))

    def shift_set(exponents: tuple) -> tuple:
        return tuple(sp.expand(Ut ** step * Ux ** offset)
                     for step in exponents for offset in range(2))

    orbits = reflection_orbits()
    closed_sets = equal_weight_closed_sets()
    closed_sets_all_closed = True
    closed_sets_all_positive_definite = True
    for exponents in closed_sets:
        shifts = shift_set(exponents)
        averaged = orbit_average(H_field, shifts)
        if residual_count(
                R * averaged * R_inv
                - orbit_average(H_dual_theta, shifts)) != 0:
            closed_sets_all_closed = False
        if not positive_definite(averaged):
            closed_sets_all_positive_definite = False

    minimal_shifts = shift_set((0,))
    H_min = orbit_average(H_field, minimal_shifts)
    minimal_closure_residual = residual_count(
        R * H_min * R_inv - orbit_average(H_dual_theta, minimal_shifts))
    minimal_positive_definite = positive_definite(H_min)

    sym_shifts = shift_set(tuple(range(T_COVER)))
    H_sym = orbit_average(H_field, sym_shifts)
    H_sym_dual_theta = orbit_average(H_dual_theta, sym_shifts)
    sym_closure_residual = residual_count(
        R * H_sym * R_inv - H_sym_dual_theta)
    sym_positive_definite = positive_definite(H_sym)
    minimal_versus_full_entries = residual_count(H_min - H_sym)

    def point_completion(source: dict, shifts: tuple) -> sp.Matrix:
        return completion(orbit_average(hodge_cover(source), shifts), d00)

    Ut2, Ux2 = sp.expand(Ut * Ut), sp.expand(Ux * Ux)

    def two_step_table(shifts: tuple) -> dict:
        base = point_completion(field, shifts)
        return {
            "t+": residual_count(
                Ut2 * base * Ut2.T
                - point_completion(shifted_field(field, 2, 0), shifts)),
            "t-": residual_count(
                Ut2.T * base * Ut2
                - point_completion(shifted_field(field, -2, 0), shifts)),
            "x+": residual_count(
                Ux2 * base * Ux2.T
                - point_completion(shifted_field(field, 0, 2), shifts)),
            "x-": residual_count(
                Ux2.T * base * Ux2
                - point_completion(shifted_field(field, 0, -2), shifts)),
        }

    minimal_two_step_residual = two_step_table(minimal_shifts)
    two_step_residual = two_step_table(sym_shifts)
    Q_sym = completion(H_sym, d00)
    one_step_control_residual = residual_count(
        Ut * Q_sym * Ut.T
        - point_completion(shifted_field(field, 1, 0), sym_shifts))
    sym_action_residual = residual_count(
        R * Q_sym * R_inv - dual_completion(H_sym_dual_theta, d_ref))

    citation_pins = {
        "b105_reflection": B105_REFLECTION_PIN in landed_text(BLOCK105_NOTE),
        "b105_seam": B105_SEAM_PIN in landed_text(BLOCK105_NOTE),
        "b104_bond": B104_BOND_PIN in landed_text(BLOCK104_NOTE),
        "b104_antilinear": B104_ANTILINEAR_PIN in landed_text(BLOCK104_NOTE),
    }
    banners = {
        "imposed_objects": len(IMPOSED_OBJECTS),
        "registered_objects": len(REGISTERED_OBJECTS),
        "adopted_objects": len(ADOPTED_OBJECTS),
        # THE DECLARED STATUS FLAGS, so the B mutations bite on a declared
        # object and not on prose.  ALL FIVE ARE MEASURED AND ALL ARE FALSE.
        "objects_registered": bool(REGISTERED_OBJECTS or ADOPTED_OBJECTS),
        "os_positivity_claimed": OS_POSITIVITY_CLAIMED,
        "temporal_link_claimed": TEMPORAL_LINK_CLAIMED,
        "two_history_gram_claimed": TWO_HISTORY_GRAM_CLAIMED,
        "gravity_claimed": GRAVITY_CLAIMED,
        "selection_uniqueness_claimed": SELECTION_UNIQUENESS_CLAIMED,
    }
    return Facts(
        main_head=main_head,
        authority=authority_certificate(main_head),
        note_at_final_path=at_final_path,
        scope=scope_certificate(text),
        banners=banners,
        citation_pins=citation_pins,
        reflection_is_orthogonal_residual=reflection_is_orthogonal_residual,
        r_square_residual=r_square_residual,
        r_square_against_identity=r_square_against_identity,
        adjoint_involution_residual=adjoint_involution_residual,
        d_ref_nilpotency_residual=d_ref_nilpotency_residual,
        d_ref_rank=d_ref_rank,
        d_ref_family=d_ref_family,
        d_ref_jump_census=d_ref_jump_census,
        base_jump_census=base_jump_census,
        fixed_census_defect=fixed_census_defect,
        transported_census_residual=transported_census_residual,
        flat_control_residual=flat_control_residual,
        xpar_square_residual=xpar_square_residual,
        xpar_adjoint_residual=xpar_adjoint_residual,
        xpar_is_not_flat_fixing=xpar_is_not_flat_fixing,
        naive_low_residual=naive_low_residual,
        naive_high_residual=naive_high_residual,
        cell_factorization_failures=cell_factorization_failures,
        cells_checked=cells_checked,
        cell_map_square_residual=cell_map_square_residual,
        cell_map_orthogonal_residual=cell_map_orthogonal_residual,
        dual_block_residual=dual_block_residual,
        dual_block_separations=dual_block_separations,
        hodge_control_residual=hodge_control_residual,
        hodge_theorem_residual=hodge_theorem_residual,
        undressed_hodge_residual=undressed_hodge_residual,
        undualized_hodge_residual=undualized_hodge_residual,
        temporal_conjugation_residual=temporal_conjugation_residual,
        temporal_conjugation_against_plus=temporal_conjugation_against_plus,
        spatial_conjugation_residual=spatial_conjugation_residual,
        equal_weight_hodge_residual=equal_weight_hodge_residual,
        reflected_origin_set_residual=reflected_origin_set_residual,
        equal_weight_action_residual=equal_weight_action_residual,
        reflection_orbits=orbits,
        closed_set_count=len(closed_sets),
        proper_closed_set_count=sum(
            1 for exponents in closed_sets if len(exponents) < T_COVER),
        closed_sets_all_closed=closed_sets_all_closed,
        closed_sets_all_positive_definite=closed_sets_all_positive_definite,
        minimal_shift_count=len(minimal_shifts),
        minimal_closure_residual=minimal_closure_residual,
        minimal_positive_definite=minimal_positive_definite,
        minimal_two_step_residual=minimal_two_step_residual,
        minimal_versus_full_entries=minimal_versus_full_entries,
        sym_closure_residual=sym_closure_residual,
        sym_shift_count=len(sym_shifts),
        sym_positive_definite=sym_positive_definite,
        sym_leading_minors=N_COVER,
        two_step_residual=two_step_residual,
        one_step_control_residual=one_step_control_residual,
        sym_action_residual=sym_action_residual,
        mass_is_symbolic=bool(SYMBOLIC_MASS.is_Symbol
                              and SYMBOLIC_MASS.is_positive
                              and SYMBOLIC_MASS in Q_sym.free_symbols
                              and SYMBOLIC_MASS in Q_flat.free_symbols),
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
        "registry blobs in the worktree. THE TWO BLOCK 182 ARTIFACTS ARE "
        "CONTENT-BOUND -- its note and its runner, the pair that identifies "
        "the commit this block's branch is cut from -- at PARENT_COMMIT, in "
        "the worktree and against their pinned blobs, and PARENT_COMMIT IS "
        "REAL and PARENT_REF resolves to it, so nothing needs sed at landing. "
        "THE STALE PIN IS THE BLOCK 181 TIP, a REAL ancestor of HEAD that "
        "PREDATES Block 182 and therefore carries NEITHER Block 182 artifact, "
        "which is exactly what makes the stale_parent_authority mutation bite: "
        "under it the gate looks for the artifact blobs at a commit where they "
        "do not exist. AUDIT_INPUT_PATHS IS LITERAL and every one of its NINE "
        "entries is required readable in the worktree EXCEPT this block's own "
        "note, which lands later and belongs to gate H -- and the nine include "
        "the TWO PRIMARY BODIES this block's derivation is read from, the "
        "Block 105 and Block 104 notes. AND THE MACHINERY IMPORT IS GATED: the "
        "LANDED Block 128 runner must have imported, because every object this "
        "runner measures is rebuilt from it and from the Block 105 module it "
        "re-exports -- NOTHING from any scratchpad is imported or read anywhere",
        bool(
            AUDIT_INPUT_PATHS[0] == SELF_NOTE_INPUT
            and len(AUDIT_INPUT_PATHS) == 9
            and len(set(AUDIT_INPUT_PATHS)) == 9
            and BLOCK182_NOTE in AUDIT_INPUT_PATHS
            and BLOCK182_RUNNER in AUDIT_INPUT_PATHS
            and BLOCK181_NOTE in AUDIT_INPUT_PATHS
            and BLOCK128_NOTE in AUDIT_INPUT_PATHS
            and BLOCK128_RUNNER in AUDIT_INPUT_PATHS
            and BLOCK105_NOTE in AUDIT_INPUT_PATHS
            and BLOCK104_NOTE in AUDIT_INPUT_PATHS
            and CAMPAIGN_NOTE in AUDIT_INPUT_PATHS
            # EVERY AUDIT INPUT BUT THIS BLOCK'S OWN NOTE IS READABLE IN THE
            # WORKTREE; the note itself is gate H's, because it lands later.
            and authority.inputs_readable == len(AUDIT_INPUT_PATHS) - 1
            and authority.inputs_missing == ()
            and PARENT_ARTIFACTS == (BLOCK182_NOTE, BLOCK182_RUNNER)
            and len(PARENT_ARTIFACT_BLOBS) == len(PARENT_ARTIFACTS) == 2
            and facts.main_head == claims["main_head"]
            and authority.fixed_authority
            and authority.machinery_import_landed
            and authority.parent_pin_is_commit
            and authority.parent_ref_and_ancestry
            and parent_blobs_ok
            # THE STALE PIN: a REAL ancestor of HEAD that carries NEITHER
            # Block 182 artifact.
            and authority.stale_is_real_ancestor
            and authority.stale_carries_neither_artifact))

    # --- B: the imposed-object banner and the NOT-CLAIMED keys -------------
    ban = facts.banners
    checks.check(
        "B-THE-IMPOSED-OBJECT-BANNER-and-the-NOT-CLAIMED-keys",
        f"THE BANNER COMES BEFORE ANY NUMERAL AND IT IS MEASURED RATHER THAN "
        f"ASSERTED. {ban['imposed_objects']} objects are IMPOSED by this block "
        f"-- the certified Block 105 curved carrier as landed by Block 128 and "
        f"re-used by Blocks 181 and 182, the DERIVED bond reflection R = "
        f"P_edge * tpar with its x-parity control variant, the cell map M with "
        f"the dual block M H(q,v) M^T, the cell field reflection theta with the "
        f"parameterized Hodge and its dual, the whole section-point family, and "
        f"the exterior census with its co-transport -- and "
        f"{ban['registered_objects']} are REGISTERED and "
        f"{ban['adopted_objects']} are ADOPTED. AND THE BANNER'S SECOND HALF IS "
        f"WHAT IS NOT CLAIMED, gated as declared constants: NO OS OR "
        f"REFLECTION-POSITIVITY THEOREM IS CLAIMED, because a covariance "
        f"identity is not a positivity statement and no pairing is shown "
        f"positive here; NO TEMPORAL-LINK EXTRACTION IS PERFORMED, the dt=+-1 "
        f"band being left to the successor; NO TWO-HISTORY GRAM IS BUILT; NO "
        f"GRAVITY RESULT IS CLAIMED; and NO UNIQUE SELECTION OF A SECTION POINT "
        f"IS CLAIMED -- and that last key is not a hedge but a REFUTATION, "
        f"since gate G exhibits FIFTEEN closed sets smaller than the full "
        f"orbit. Asserting any of the five, or asserting that the imposed "
        f"objects are registered, fails HERE and nowhere else",
        bool(
            ban["imposed_objects"] == 6
            and ban["registered_objects"] == 0
            and ban["adopted_objects"] == 0
            and ban["objects_registered"] == claims["objects_registered"]
            and ban["os_positivity_claimed"] == claims["os_positivity_claimed"]
            and ban["temporal_link_claimed"] == claims["temporal_link_claimed"]
            and ban["two_history_gram_claimed"]
            == claims["two_history_gram_claimed"]
            and ban["gravity_claimed"] == claims["gravity_claimed"]
            and ban["selection_uniqueness_claimed"]
            == claims["selection_uniqueness_claimed"]))

    # --- C: the derived reflection -----------------------------------------
    pins = facts.citation_pins
    checks.check(
        "C-THE-DERIVATION-IS-READ-FROM-THE-PRIMARY-BODIES",
        f"THE TWO INGREDIENTS OF THE DERIVATION ARE PINNED IN THE NOTES THEY "
        f"COME FROM, not in a recollection of them. Block 104's bond convention "
        f"'{B104_BOND_PIN}' is present in its primary body "
        f"({pins['b104_bond']}) together with its antilinearity sentence, "
        f"'{B104_ANTILINEAR_PIN}' ({pins['b104_antilinear']}); Block 105's "
        f"time-reflection pullback '{B105_REFLECTION_PIN}' is present in its "
        f"primary body ({pins['b105_reflection']}) together with the "
        f"'{B105_SEAM_PIN}' phrase this block's first reading answers "
        f"({pins['b105_seam']}). THE REFLECTION IS ASSEMBLED FROM TWO LANDED "
        f"CONVENTIONS AND A CORNER CORRESPONDENCE, AND NONE OF THE THREE IS "
        f"INVENTED HERE -- which is what makes it DERIVED rather than chosen",
        bool(all(pins.values()) == claims["citation_pins"]))
    checks.check(
        "C-R-is-REAL-ORTHOGONAL-and-SQUARES-TO-MINUS-ONE",
        f"R = P_edge * tpar is REAL ORTHOGONAL -- R R^T - I has "
        f"{facts.reflection_is_orthogonal_residual} nonzero entries, so "
        f"R^-1 = R^T and NO OPERATOR INVERSE IS EVER FORMED and conjugation by "
        f"R commutes with the adjoint. AND THE SQUARE IS MEASURED, NOT ASSUMED: "
        f"R^2 + I has {facts.r_square_residual} nonzero entries while R^2 - I "
        f"has {facts.r_square_against_identity}. R^2 = -I EXACTLY, so R^-1 is "
        f"also -R. THE SOLVE'S 'an involution (R^2 = I)' IS REFUTED AND THE "
        f"REFUTATION IS FORCED BY THE DERIVATION ITSELF: gate D's single cell "
        f"map has M^2 = -I and the cell sign is parity-even under theta, so the "
        f"square CANNOT be +I. R IS A PROJECTIVE INVOLUTION WITH R^4 = I, and "
        f"its conjugation action on operators IS an exact involution -- "
        f"measured directly at {tuple(facts.adjoint_involution_residual.values())}"
        f" -- so every downstream statement, all of which are conjugations, is "
        f"untouched by the central sign. Asserting R^2 = +I fails HERE and "
        f"nowhere else",
        bool(
            facts.reflection_is_orthogonal_residual
            == claims["reflection_is_orthogonal_residual"]
            and facts.r_square_residual == claims["r_square_residual"]
            and facts.r_square_against_identity
            == claims["r_square_against_identity"]
            and all(value == claims["adjoint_involution_residual"]
                    for value in facts.adjoint_involution_residual.values())))
    checks.check(
        "C-the-REFLECTED-DIFFERENTIAL-classified-and-OUTSIDE-the-guessed-family",
        f"d_ref = R d_00 R^-1 is NILPOTENT with a zero square "
        f"({facts.d_ref_nilpotency_residual}) and rank {facts.d_ref_rank}, the "
        f"same rank as d_00. AND IT IS OUTSIDE THE FAMILY THE GUESS GRID SWEPT: "
        f"all EIGHT residuals against {tuple(facts.d_ref_family)} are nonzero, "
        f"{tuple(facts.d_ref_family.values())}. THIS IS THE RECORDED "
        f"TWENTY-CANDIDATE NEGATIVE RE-MEASURED AT ITS CONCLUSION: the "
        f"reflection image was never going to be found by sweeping the chart "
        f"and sign-dressed families, which is why it had to be DERIVED",
        bool(
            facts.d_ref_nilpotency_residual
            == claims["d_ref_nilpotency_residual"]
            and facts.d_ref_rank == claims["d_ref_rank"]
            and (all(value != 0 for value in facts.d_ref_family.values())
                 == claims["d_ref_outside_family"])
            and len(facts.d_ref_family) == 8))
    checks.check(
        "C-THE-CENSUS-CO-TRANSPORTS-16-16-jumps-fixed-defect-16-transported-ZERO",
        f"THE GRADING CLAIM IS CORRECTED BY AN EXACT CENSUS. d_00 carries all "
        f"{sum(facts.base_jump_census.values())} of its nonzero entries at "
        f"grade jump +1 ({facts.base_jump_census}) -- it is purely "
        f"grade-raising -- while d_ref splits {facts.d_ref_jump_census}: "
        f"EXACTLY 16 entries DOWN and EXACTLY 16 UP. So the FIXED census "
        f"N = diag(t%2 + x%2) is NOT a grade operator for it and "
        f"[N, d_ref] - d_ref has EXACTLY {facts.fixed_census_defect} nonzero "
        f"entries, while the CO-TRANSPORTED census R N R^-1 closes it to "
        f"{facts.transported_census_residual} -- EXACTLY ZERO. THE SOLVE'S "
        f"'grade-preserving' IS REFUTED: the reflection does not fix the "
        f"census, it TRANSPORTS it, which is Block 106's lesson through Block "
        f"182 recurring a THIRD time on a new object. ALL THREE NUMBERS ARE "
        f"MEASURED IN THE SAME RUN so the statement is a contrast and not an "
        f"assertion",
        bool(facts.d_ref_jump_census == claims["d_ref_jump_census"]
             and facts.base_jump_census == claims["base_jump_census"]
             and facts.fixed_census_defect == claims["fixed_census_defect"]
             and facts.transported_census_residual
             == claims["transported_census_residual"]))
    checks.check(
        "C-THE-FLAT-CONTROL-IS-EXACT-and-the-XPAR-VARIANT-gives-the-ADJOINT",
        f"THE CONTROL COMES FIRST. R Q(I, d_00) R^-1 = Q(I, d_00) with a "
        f"{facts.flat_control_residual}-entry residual -- EXACT -- so the "
        f"derived reflection is a symmetry of the FLAT completion and the "
        f"curved statements below are not bought by a reflection tuned to the "
        f"curved object. AND THE X-PARITY VARIANT IS KEPT AS THE DISCRIMINATING "
        f"CONTROL: R_x = P_edge * diag((-1)^x) is an HONEST involution "
        f"(R_x^2 - I has {facts.xpar_square_residual} entries, so its square is "
        f"+I and not -I) and it sends the flat completion to its ADJOINT, "
        f"R_x Q R_x^-1 - Q^H having {facts.xpar_adjoint_residual} entries while "
        f"R_x Q R_x^-1 - Q has {facts.xpar_is_not_flat_fixing}. TWO DRESSINGS, "
        f"TWO DIFFERENT ANSWERS, MEASURED SIDE BY SIDE: the t-parity dressing "
        f"FIXES the flat completion and the x-parity dressing ADJOINTS it -- "
        f"and only one of the two squares to minus one. Asserting a nonzero "
        f"flat-control residual fails HERE and nowhere else",
        bool(facts.flat_control_residual == claims["flat_control_residual"]
             and facts.xpar_square_residual == claims["xpar_square_residual"]
             and facts.xpar_adjoint_residual == claims["xpar_adjoint_residual"]
             and facts.xpar_is_not_flat_fixing != 0))
    checks.check(
        "C-THE-RECORDED-NAIVE-NEGATIVES-re-measured-at-352-and-368",
        f"THE UNDRESSED REFLECTION FAILS, AND THE FAILURE IS PINNED AT BOTH "
        f"ENDS OF THE RECORDED BAND. The undressed edge reflection P_edge "
        f"conjugating the Block 181 equal-weight curved action, against the "
        f"PLAIN (non-adjoint) UNFLIPPED target at the theta-reflected field, "
        f"has residual EXACTLY {facts.naive_low_residual} with the "
        f"edge-transported differential and EXACTLY {facts.naive_high_residual} "
        f"with the differential held fixed at d_00 -- the two endpoints of the "
        f"352-368 band the campaign recorded for its eight-cell naive sweep. "
        f"THE SIGN DRESSING IS LOAD-BEARING AND THE NUMBER SAYS SO",
        bool(facts.naive_low_residual == claims["naive_low_residual"]
             and facts.naive_high_residual == claims["naive_high_residual"]))

    # --- D: the cell factorization ------------------------------------------
    checks.check(
        "D-THE-CELL-FACTORIZATION-one-M-every-cell-and-M-squared-is-MINUS-I",
        f"for EVERY ONE of the {facts.cells_checked} cells of the 8x4 cover, "
        f"R emb(t,x) = emb((6-t)%8, x) * (s*M) at ZERO residual with "
        f"s = (-1)^t and with the SAME 4x4 M at every cell "
        f"({facts.cell_factorization_failures} failures). M is ORTHOGONAL "
        f"({facts.cell_map_orthogonal_residual}) and M^2 = -I EXACTLY "
        f"({facts.cell_map_square_residual}): THE CELL CARRIES A COMPLEX "
        f"STRUCTURE, and it is a measured fact about the carrier rather than a "
        f"reading imposed on it. THE ALTERNATING SIGN IS FORCED -- one M at "
        f"every cell requires the dressing to alternate -- and it is what makes "
        f"gate C's R^2 = -I a theorem rather than an accident: theta preserves "
        f"t-parity, so the two cell signs multiply to +1 and the square is M^2. "
        f"Asserting a single failing cell fails HERE and nowhere else",
        bool(
            facts.cell_factorization_failures
            == claims["cell_factorization_failures"]
            and facts.cells_checked == claims["cells_checked"]
            and facts.cell_map_square_residual
            == claims["cell_map_square_residual"]
            and facts.cell_map_orthogonal_residual
            == claims["cell_map_orthogonal_residual"]))

    # --- E: the dual block ---------------------------------------------------
    checks.check(
        "E-THE-DUAL-BLOCK-IN-CLOSED-FORM-at-SYMBOLIC-q-and-v",
        f"M H(q,v) M^T equals [[-v/(q^2-1), 0, 0, -q*v/(q^2-1)], [0, 1/v, 0, "
        f"0], [0, 0, v, 0], [-q*v/(q^2-1), 0, 0, -v/(q^2-1)]] EXACTLY at "
        f"SYMBOLIC (q,v) -- residual {facts.dual_block_residual} -- so this is "
        f"an identity in the metric parameters and not a coincidence at the "
        f"landed field. AND IT IS A GENUINELY NEW BLOCK, SEPARATED FROM SIX "
        f"NEIGHBOURS: it is not H(q,v), not H(-q,v), not either inverse, not "
        f"H(q,1/v) and not H(-q,1/v), at "
        f"{tuple(facts.dual_block_separations.values())} nonzero entries "
        f"respectively. Asserting a nonzero closed-form residual fails HERE and "
        f"nowhere else",
        bool(
            facts.dual_block_residual == claims["dual_block_residual"]
            and len(facts.dual_block_separations)
            == claims["dual_block_separations"]
            and all(value != 0
                    for value in facts.dual_block_separations.values())))

    # --- F: the Hodge-level theorem -----------------------------------------
    checks.check(
        "F-CONTROL-the-parameterized-Hodge-reproduces-the-LANDED-one",
        f"H[landed field] equals the LANDED b128 curved_hodge_cover() EXACTLY, "
        f"at {facts.hodge_control_residual} nonzero entries. THE CONTROL COMES "
        f"FIRST: the theorem below is about a family whose base point is the "
        f"landed object itself, so no covariance is bought by redefining the "
        f"Hodge",
        facts.hodge_control_residual == claims["hodge_control_residual"])
    checks.check(
        "F-THE-HODGE-LEVEL-THEOREM-R-H-Rinv-equals-H_dual-at-theta-g",
        f"R H[g] R^-1 = H_dual[theta g] EXACTLY -- residual "
        f"{facts.hodge_theorem_residual} -- with theta the cell field "
        f"reflection (t,x) -> ((2-t)%4, x) and H_dual built from the dual "
        f"block. THE REFLECTION DOES NOT PRESERVE THE FRAME; IT PAIRS THE FRAME "
        f"WITH THE DUAL FRAME. AND BOTH DISCRIMINATING CONTROLS ARE MEASURED IN "
        f"THE SAME RUN: drop the sign dressing and the identity dies "
        f"({facts.undressed_hodge_residual} entries), drop the dual block and "
        f"it dies too ({facts.undualized_hodge_residual} entries). Asserting a "
        f"nonzero theorem residual fails HERE and nowhere else",
        bool(
            facts.hodge_theorem_residual == claims["hodge_theorem_residual"]
            and (facts.undressed_hodge_residual != 0)
            == claims["undressed_hodge_control"]
            and (facts.undualized_hodge_residual != 0)
            == claims["undualized_hodge_control"]))

    # --- G: the section points ----------------------------------------------
    checks.check(
        "G-THE-CONJUGATION-TABLE-is-the-mechanism-and-it-is-MEASURED",
        f"R U_t R^-1 = -U_t^-1 EXACTLY -- the residual against -U_t^-1 is "
        f"{facts.temporal_conjugation_residual} while the residual against "
        f"+U_t^-1 is {facts.temporal_conjugation_against_plus} -- and "
        f"R U_x R^-1 = U_x EXACTLY "
        f"({facts.spatial_conjugation_residual}). THIS TABLE IS THE WHOLE "
        f"MECHANISM: the reflection inverts the temporal shift and fixes the "
        f"spatial one, the sign cancels in any conjugation S^T A S, and "
        f"therefore closure of an orbit-averaged section point needs NOTHING "
        f"MORE than reflection-symmetric temporal weights w_k = w_{{-k}}. "
        f"Everything else in this family is a consequence of these three "
        f"numbers. Asserting R U_t R^-1 = +U_t^-1 fails HERE and nowhere else",
        bool(
            facts.temporal_conjugation_residual
            == claims["temporal_conjugation_residual"]
            and facts.temporal_conjugation_against_plus
            == claims["temporal_conjugation_against_plus"]
            and facts.spatial_conjugation_residual
            == claims["spatial_conjugation_residual"]))
    checks.check(
        "G-CLOSURE-RULES-OUT-THE-EQUAL-WEIGHT-POINT-at-96-and-256",
        f"the Block 181 equal-weight four-origin point FAILS reflection "
        f"closure, and the MECHANISM is exhibited rather than described. "
        f"Against the SAME origin set the Hodge-level residual is EXACTLY "
        f"{facts.equal_weight_hodge_residual} entries and the action-level "
        f"residual is EXACTLY {facts.equal_weight_action_residual}; against the "
        f"REFLECTED origin set {{0,-1}}x{{0,1}} -- which is exactly where the "
        f"conjugation table sends {{0,1}}^2 -- the Hodge-level residual is "
        f"{facts.reflected_origin_set_residual}, EXACTLY ZERO. THE ZERO AT THE "
        f"REFLECTED SET IS THE PROOF OF THE MECHANISM. Asserting the "
        f"equal-weight point reflection-closed at the action level fails HERE "
        f"and nowhere else",
        bool(
            facts.equal_weight_hodge_residual
            == claims["equal_weight_hodge_residual"]
            and facts.equal_weight_action_residual
            == claims["equal_weight_action_residual"]
            and facts.reflected_origin_set_residual
            == claims["reflected_origin_set_residual"]))
    checks.check(
        "G-CLOSURE-ADMITS-A-FAMILY-AND-NEVER-PINS-A-POINT-15-smaller-sets",
        f"AND CLOSURE IS NOT A SELECTOR. The reflection orbits of the temporal "
        f"exponents are {facts.reflection_orbits} -- "
        f"{len(facts.reflection_orbits)} of them -- and EVERY equal-weight "
        f"union of them containing 0, crossed with {{I, U_x}}, is "
        f"reflection-closed: {facts.closed_set_count} such sets, ALL of them "
        f"closing EXACTLY ({facts.closed_sets_all_closed}) and ALL of them "
        f"POSITIVE DEFINITE by 32 exact leading minors "
        f"({facts.closed_sets_all_positive_definite}), of which "
        f"{facts.proper_closed_set_count} are PROPER subsets of the full "
        f"orbit. THE MINIMAL MEMBER IS {{I, U_x}}, "
        f"{facts.minimal_shift_count} shifts: it closes at "
        f"{facts.minimal_closure_residual}, is positive definite "
        f"({facts.minimal_positive_definite}), carries the two-step covariance "
        f"at {tuple(facts.minimal_two_step_residual.values())}, and DIFFERS "
        f"from the full-orbit point at {facts.minimal_versus_full_entries} "
        f"entries -- so the two are genuinely different section points and not "
        f"the same object twice. REFLECTION CLOSURE CONSTRAINS THE BLOCK 181 "
        f"MODULI AND NEVER PINS THEM: it RULES OUT the equal-weight point and "
        f"ADMITS an orbit-constant-weight family, and NO UNIQUE SELECTOR "
        f"EXISTS. This check is the adversarial refutation of the solve's "
        f"selection reading, carried as content",
        bool(
            len(facts.reflection_orbits) == claims["reflection_orbit_count"]
            and facts.closed_set_count == claims["closed_set_count"]
            and facts.proper_closed_set_count
            == claims["proper_closed_set_count"]
            and facts.closed_sets_all_closed == claims["closed_sets_all_closed"]
            and facts.closed_sets_all_positive_definite
            == claims["closed_sets_all_positive_definite"]
            and facts.minimal_shift_count == claims["minimal_shift_count"]
            and facts.minimal_closure_residual
            == claims["minimal_closure_residual"]
            and facts.minimal_positive_definite
            == claims["minimal_positive_definite"]
            and all(value == claims["minimal_two_step_residual"]
                    for value in facts.minimal_two_step_residual.values())
            and facts.minimal_versus_full_entries
            == claims["minimal_versus_full_entries"]))
    checks.check(
        "G-THE-FULL-ORBIT-POINT-closes-exactly-is-PD-and-stays-two-step-covariant",
        f"with H_sym the {facts.sym_shift_count}-shift full-orbit average "
        f"(1/16) sum over k in 0..7 and xo in {{0,1}} of "
        f"(U_t^k U_x^xo)^T H[g] (U_t^k U_x^xo), R H_sym[g] R^-1 = "
        f"H_sym_dual[theta g] EXACTLY -- residual "
        f"{facts.sym_closure_residual} -- WITH THE SAME SHIFT SET on both "
        f"sides. H_sym is symmetric and POSITIVE DEFINITE by "
        f"{facts.sym_leading_minors} exactly positive leading principal minors "
        f"({facts.sym_positive_definite}), exact rational determinants with no "
        f"eigenvalue estimate and no tolerance anywhere. AND THE SECTION-FRAME "
        f"STRUCTURE SURVIVES: U^2 Q(H_sym[g], d_00) U^2T = Q(H_sym[T^2 g], "
        f"d_00) at {tuple(facts.two_step_residual.values())} on both axes in "
        f"both directions, against a ONE-STEP control that fails at "
        f"{facts.one_step_control_residual} entries in the same run. IT IS ONE "
        f"MEMBER OF THE ADMITTED FAMILY AND NOT A SELECTED POINT. Asserting a "
        f"nonzero closure residual, or asserting H_sym not positive definite, "
        f"fails HERE and nowhere else",
        bool(
            facts.sym_closure_residual == claims["sym_closure_residual"]
            and facts.sym_shift_count == claims["sym_shift_count"]
            and facts.sym_positive_definite == claims["sym_positive_definite"]
            and facts.sym_leading_minors == claims["sym_leading_minors"]
            and all(value == claims["two_step_residual"]
                    for value in facts.two_step_residual.values())
            and facts.one_step_control_residual
            == claims["one_step_control_residual"]))
    checks.check(
        "G-THE-ACTION-LEVEL-IDENTITY-a-FORMAL-COROLLARY-not-a-new-fact",
        f"R Q(H_sym[g], d_00) R^-1 = m H_sym_dual[theta g] + i(H_sym_dual "
        f"d_ref + d_ref^H H_sym_dual) EXACTLY, at {facts.sym_action_residual} "
        f"nonzero entries and at SYMBOLIC POSITIVE MASS "
        f"({facts.mass_is_symbolic}). AND THE GATE SAYS WHAT THE IDENTITY IS: "
        f"IT IS A FORMAL COROLLARY of the Hodge-level closure of the previous "
        f"check, together with R's orthogonality (so conjugation commutes with "
        f"the adjoint) and the distribution of conjugation over m*H + i(H d + "
        f"d^H H) with d_ref DEFINED as R d_00 R^-1. IT ADDS NO INDEPENDENT "
        f"CONSTRAINT once the closure and the definitions are established, it "
        f"is GATED AS A CONSISTENCY CERTIFICATE, and a reader who counts it as "
        f"a second theorem is double-counting one theorem -- a sentence that is "
        f"in the note as well as here",
        bool(facts.sym_action_residual == claims["sym_action_residual"]
             and facts.mass_is_symbolic == claims["mass_is_symbolic"]))

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
          f"it {authority.parent_ref_and_ancestry}, and BOTH Block 182 "
          f"artifacts are content-bound there and in the worktree "
          f"{authority.parent_artifact_blobs}. THE AUDIT INPUTS: "
          f"{authority.inputs_readable} of {len(AUDIT_INPUT_PATHS) - 1} "
          f"readable in the worktree (this block's own note excluded, since it "
          f"lands later and is gate H's), missing {authority.inputs_missing}")
    print(f"  THE STALE PIN: {STALE_PARENT_COMMIT[:12]} is a REAL ancestor of "
          f"HEAD {authority.stale_is_real_ancestor} and carries NEITHER Block "
          f"182 artifact {authority.stale_carries_neither_artifact} -- it is "
          f"the Block 181 tip, which PREDATES both artifacts, and that absence "
          f"is exactly what makes the stale_parent_authority mutation bite")
    print(f"  THE MACHINERY: the LANDED Block 128 runner is imported "
          f"{authority.machinery_import_landed} and every object below is "
          f"rebuilt from it and from the Block 105 module it re-exports -- the "
          f"cover is {T_COVER}x{X_EXTENT} at dimension {N_COVER}, the field has "
          f"period {PHYSICAL_T} in t, the landed MASS is {MASS} and every "
          f"completion here is run at SYMBOLIC POSITIVE MASS instead. NOTHING "
          f"from any scratchpad is imported or read")
    print(f"  THE BANNER: {ban['imposed_objects']} imposed objects, "
          f"{ban['registered_objects']} registered and "
          f"{ban['adopted_objects']} adopted; MEASURED os-positivity-claimed "
          f"{ban['os_positivity_claimed']}, temporal-link-claimed "
          f"{ban['temporal_link_claimed']}, two-history-Gram-claimed "
          f"{ban['two_history_gram_claimed']}, gravity-claimed "
          f"{ban['gravity_claimed']} and selection-uniqueness-claimed "
          f"{ban['selection_uniqueness_claimed']}. The imposed objects are "
          f"{IMPOSED_OBJECTS}")
    print(f"  THE CITATION PINS: {facts.citation_pins} -- the derivation's two "
          f"ingredients read from the Block 104 and Block 105 PRIMARY BODIES")
    print(f"  THE DERIVED REFLECTION: R R^T - I has "
          f"{facts.reflection_is_orthogonal_residual} nonzero entries; R^2 + I "
          f"has {facts.r_square_residual} and R^2 - I has "
          f"{facts.r_square_against_identity}, SO R^2 = -I EXACTLY and R is a "
          f"PROJECTIVE involution whose conjugation action is an exact "
          f"involution {tuple(facts.adjoint_involution_residual.values())}. "
          f"d_ref is nilpotent ({facts.d_ref_nilpotency_residual}) of rank "
          f"{facts.d_ref_rank} and sits outside the guessed family at "
          f"{facts.d_ref_family}")
    print(f"  THE CENSUS: d_00's jump census is {facts.base_jump_census} and "
          f"d_ref's is {facts.d_ref_jump_census}; the FIXED census defect is "
          f"{facts.fixed_census_defect} and the CO-TRANSPORTED census closes it "
          f"at {facts.transported_census_residual}. THE GRADE CO-TRANSFORMS "
          f"WITH THE FRAME, for the third time in this lane")
    print(f"  THE CONTROLS: the FLAT control residual is "
          f"{facts.flat_control_residual}; the x-parity variant squares to +I "
          f"({facts.xpar_square_residual}) and sends the flat completion to its "
          f"ADJOINT ({facts.xpar_adjoint_residual}) rather than to itself "
          f"({facts.xpar_is_not_flat_fixing}). THE RECORDED NAIVE NEGATIVES: "
          f"{facts.naive_low_residual} and {facts.naive_high_residual}, the two "
          f"endpoints of the campaign's recorded 352-368 band")
    print(f"  THE CELL FACTORIZATION: {facts.cells_checked} cells checked with "
          f"{facts.cell_factorization_failures} failures; M M^T - I has "
          f"{facts.cell_map_orthogonal_residual} entries and M^2 + I has "
          f"{facts.cell_map_square_residual} -- M IS A COMPLEX STRUCTURE ON THE "
          f"CELL, and it is what forces R^2 = -I")
    print(f"  THE DUAL BLOCK: the closed-form residual at symbolic (q,v) is "
          f"{facts.dual_block_residual}, and the six separations are "
          f"{facts.dual_block_separations}")
    print(f"  THE HODGE-LEVEL THEOREM: the landed-field control residual is "
          f"{facts.hodge_control_residual} and the theorem residual is "
          f"{facts.hodge_theorem_residual}; the UNDRESSED control fails at "
          f"{facts.undressed_hodge_residual} and the UNDUALIZED control at "
          f"{facts.undualized_hodge_residual}")
    print(f"  THE CONJUGATION TABLE: R U_t R^-1 + U_t^-1 has "
          f"{facts.temporal_conjugation_residual} entries against "
          f"{facts.temporal_conjugation_against_plus} for the plus sign, and "
          f"R U_x R^-1 - U_x has {facts.spatial_conjugation_residual}. THE "
          f"REFLECTION INVERTS THE TEMPORAL SHIFT AND FIXES THE SPATIAL ONE")
    print(f"  THE SECTION POINTS: the equal-weight point fails at "
          f"{facts.equal_weight_hodge_residual} (Hodge) and "
          f"{facts.equal_weight_action_residual} (action) against the SAME "
          f"origin set, and at {facts.reflected_origin_set_residual} against "
          f"the REFLECTED origin set. The reflection orbits are "
          f"{facts.reflection_orbits}, giving {facts.closed_set_count} "
          f"equal-weight closed sets of which {facts.proper_closed_set_count} "
          f"are PROPER; all close exactly {facts.closed_sets_all_closed} and "
          f"all are positive definite "
          f"{facts.closed_sets_all_positive_definite}. THE MINIMAL MEMBER "
          f"{{I, U_x}} closes at {facts.minimal_closure_residual}, is PD "
          f"{facts.minimal_positive_definite}, is two-step covariant at "
          f"{tuple(facts.minimal_two_step_residual.values())} and differs from "
          f"the full-orbit point at {facts.minimal_versus_full_entries} "
          f"entries. NO UNIQUE SELECTOR EXISTS")
    print(f"  THE FULL-ORBIT POINT: closure {facts.sym_closure_residual}, "
          f"positive definite {facts.sym_positive_definite} by "
          f"{facts.sym_leading_minors} exact leading minors, two-step "
          f"covariance {tuple(facts.two_step_residual.values())} against a "
          f"one-step control at {facts.one_step_control_residual}, and the "
          f"action-level identity at {facts.sym_action_residual} -- WHICH IS A "
          f"FORMAL COROLLARY of the Hodge-level closure and adds no independent "
          f"constraint")
    print(f"  THE NOTE: read at its FINAL PATH {facts.note_at_final_path} -- "
          f"when False the note has NOT landed at docs/ yet, there is no draft "
          f"fallback anywhere in this runner, gate H is EXPECTED to fail and "
          f"the gate-H mutation is UNTESTABLE until the note lands. Scope keys "
          f"satisfied: {sum(1 for v in facts.scope.values() if v)} of "
          f"{len(facts.scope)}; unsatisfied "
          f"{tuple(key for key, value in facts.scope.items() if not value)}")
    print(f"  EXACTNESS: every measured object above is exact sympy Rational, "
          f"Integer or Symbol arithmetic; NO FLOAT and NO TOLERANCE enters any "
          f"check. ELAPSED {elapsed_ns // 1_000_000} ms")
    print(f"  THE CORPUS RELATION: Blocks 104, 105, 128, 181 and 182 STAND "
          f"EXACTLY AS LANDED and no landed note is edited. What this block "
          f"corrects is TWO OF ITS OWN SOLVE-SIDE CLAIMS, both refuted by the "
          f"adversarial check before landing: R^2 = -I with a CO-TRANSPORTING "
          f"census rather than an involution with a preserved grade, and "
          f"reflection closure as a CONSTRAINT on the Block 181 moduli rather "
          f"than a SELECTOR of a point")
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
