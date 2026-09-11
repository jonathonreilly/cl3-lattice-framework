#!/usr/bin/env python3
# Final path: scripts/admissibility_dirac_kahler_site_reflection_channel_2026_08_21.py
"""Block 163: THE SITE-REFLECTION CHANNEL.

SCOUT DISCIPLINE, AND IT IS A HARD BOUNDARY.  Every reflection outside the
committed four, every support outside the committed half, and every carrier
outside the committed family exercised here is a REGISTERED-PREMISE-CLASS CHANGE
to the committed framework.  Each one is MEASURED and NONE of them is
registered, adopted, proposed or claimed.  Nothing in this runner edits, retires
or amends any committed note, axiom, premise or convention.

THE VERDICT IS SHAPE (b) AND IT IS STATED AT ITS TRUE SCOPE.  The site class --
time reflections that FIX a cover slice rather than exchanging half carriers --
descends cleanly, the MASS APPEARS in its pairing for the first time in the
lane, the free site-reflection OS calibration is MET EXACTLY, and positivity
then fails STRUCTURALLY once the temporal connection is live.  What fails is
positivity at s_t != 0.  What does NOT fail, and is this block's discovery, is
the s_t = 0 region: it is REAL, it is LARGER than the solve transcript claimed,
and it is UNCHARACTERIZED.

THREE HEADLINE SUB-CLAIMS OF THE SOLVE TRANSCRIPT ARE REFUTED BY THE INDEPENDENT
CHECKER, EACH QUOTED THEN CORRECTED.  (S1) "The 16 X_0-commuting reflections are
a grading sector the lane has never had" is FALSE and is STRUCK: theta-prime
= (-1,7,-1,1) has p_t + p_x = 8, EVEN, so by the block's own grading identity it
COMMUTES with X_0 and has been run throughout Blocks 156-162; the genuinely new
element is the SITE GEOMETRY, not the grading sector.  (S2) "The PSD corner,
exactly: {H_q diagonal} x {s_t = 0} x {e_x = +1, p_x = 0}" is FALSE and is
STRUCK: there are PSD MASS-CARRYING cells at s_t = 0 on cone-admissible carriers
whose H_q is NOT diagonal, an exact witness is displayed, the corner also omits
the m > 0 condition, and neither the transcript's global corner nor the
checker's local-shear repair is exact.  (S3) "The two blockers are DUAL" is a
SLOGAN, not a theorem-pair, and is DEMOTED: the converse of Block 160's
direction fails on an explicit carrier, and "blinded" equivocates between a
pairing that is IDENTICALLY ZERO and a pairing that is merely
SIGNATURE-BLIND -- the site pairing is never zero.

NO HARDCODED CERTIFICATE ANYWHERE: every printed numeral is recomputed in the
measurement pass from the committed constructors reached through the LANDED
Block 162 runner, and no check is registered as a literal True.  Exact SymPy
throughout; no float enters any measured object, which is itself gated, and the
carrier constructor is gated float-free because the landed
b145.moduli_from_field LEAKS a Python float when handed plain-int carriers.  The
integer monotonic clock is used only for the runtime gate.

PROVENANCE DISCLOSURE: the four-chart shear atlas, the local differential, the
64-modulus carrier model and its admissible cone, the cover Hodge, the
antiperiodic quotient and its lift, the sixteen healed edge differentials and
their healing weights, the reflection move machinery and its covariance
condition, the committed theta and theta-prime, the staggered grading X_0, the
quotient action, and the Block 144 symmetric-congruence inertia helper are ALL
COMMITTED objects, imported through the Block 162 runner (b162 -> b161 -> b160
-> b159 -> b156 -> b153 -> b148 -> b147 -> b145 -> b142) and never re-derived.
External lattice-gauge, staggered-fermion and Osterwalder-Schrader literature is
REFERENCED nowhere and BORROWED nowhere; every statement is re-proved
in-framework.

HYPOTHESES, named and not imported.  (H1) the pairing convention is
[r Q]_{S,S} = herm(Sel_S^T r Q Sel_S), the committed b159.half_pairing law read
on a slice-union support instead of the committed eight-row half.  (H3)
"positive" is a statement about the Hermitian part.  (H4) the physical cone is
nu > 0, |sigma| < 1 per cell.  (H1-160) a pairing is exchange-compatible when
the reflection carries the half onto its complement.  (H1-163) a PSD verdict
here is a statement about THIS pairing functor on THESE supports over THESE
enumerated carriers, and about no wider class of objects; "PSD" means no
negative direction AND a nonzero positive count, so the zero form is never
counted as a positive.
"""

from __future__ import annotations

import argparse
import collections
from dataclasses import dataclass
from pathlib import Path
import re
import subprocess
import sys
import time

import sympy as sp


R = sp.Rational

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

import admissibility_dirac_kahler_mass_survival_stratum_2026_08_20 as b162

b161 = b162.b161
b160 = b162.b160
b159 = b162.b159
b156 = b162.b156
b153 = b156.b153
b148 = b162.b148
b145 = b162.b145
b144 = b162.b144
b142 = b145.b142


NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_SITE_REFLECTION_CHANNEL_"
    "BOUNDED_THEOREM_NOTE_2026-08-21.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE SINGLE-PARENT PIN.  Block 162 (the mass-survival stratum) is BOTH the
# stack parent -- this block's branch is cut from it -- AND the content parent:
# every committed constructor used here is reached through the Block 162
# runner's own import chain (b161 -> b160 -> b159 -> b156 -> b153 -> b148 ->
# b147 -> b145 -> b142), which Block 162's own gate A pins and this block does
# not duplicate.  So there are exactly TWO artifact pins here.
BLOCK162_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_MASS_SURVIVAL_STRATUM_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
BLOCK162_RUNNER = (
    "scripts/admissibility_dirac_kahler_mass_survival_stratum_2026_08_20.py"
)

PARENT_ARTIFACTS = (BLOCK162_NOTE, BLOCK162_RUNNER)
# PLACEHOLDER BLOBS for the Block 162 pair, single-line hex literals; the
# landing supervisor refreshes exactly these two lines by anchored sed against
# the Block 162 branch tip.  Until they are refreshed gate A FAILS, which is the
# intended state of an unlanded draft.
PARENT_ARTIFACT_BLOBS = (
    "0294ec9fc4235146a8a6695882beb612eb840f57",   # Block 162 note
    "a851e09193f77ec6b3aa096ab7efbb95dae3e67a",   # Block 162 runner
)

# Deliberately literal: this is the complete audit read surface.  Every entry is
# a WORKTREE-READABLE path at landing time; the cache envelope stats these, so an
# origin/main-only path here would break the audit (the Block 130 lesson,
# re-learned at the Block 150 landing and inherited through Blocks 151-162).
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_REFLECTION_CHANNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_MASS_SURVIVAL_STRATUM_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/admissibility_dirac_kahler_mass_survival_stratum_2026_08_20.py",
)

AUDIT_TIMEOUT_SEC = 600
# Authority pins, single-line hex literals refreshed by anchored sed at landing.
CURRENT_MAIN = "005f047923055e6ecd5dc8bce1ffd71765c2ffd8"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
# This block stacks on Block 162, so the parent branch is Block 162's.
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block162-mass-survival-stratum-20260820"
)
# The Block 162 branch tip, VERIFIED to be an ancestor of HEAD and to carry both
# pinned artifact paths.  The two BLOB lines above are the placeholders.
PARENT_COMMIT = "b9ef6b24579964787ebb54bfbe8f7f406aa648d8"
# Block 161's tip: a real ancestor of HEAD that PREDATES BOTH pinned parent
# artifacts.  VERIFIED before pinning with `git ls-tree`, which finds NEITHER
# the Block 162 note NOR the Block 162 runner at this commit, so resolving the
# parent pin here leaves BOTH pinned blobs ABSENT.  This pin is read ONLY under
# the stale mutation; the baseline gate never requires it.
STALE_PARENT_COMMIT = "8e2784039267e20fce1941e3796d34c5efa0d470"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_new_grading_sector",
    "break_sign_law",
    "break_calibration",
    "break_e2_theorem",
    "break_annihilation",
    "claim_antipodal_positive",
    "claim_psd_corner_exact",
    "claim_local_repair_exact",
    "break_selection_rule",
    "claim_duality_theorem",
    "claim_st0_characterized",
    "drop_witness",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_new_grading_sector": "B",
    "break_sign_law": "B",
    "break_calibration": "C",
    "break_e2_theorem": "C",
    "break_annihilation": "D",
    "claim_antipodal_positive": "E",
    "claim_psd_corner_exact": "F",
    "claim_local_repair_exact": "F",
    "break_selection_rule": "G",
    "claim_duality_theorem": "G",
    "claim_st0_characterized": "H",
    "drop_witness": "H",
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
        print(
            "GATES "
            + " ".join(
                f"{key}={'PASS' if value else 'FAIL'}"
                for key, _, value in self.results
            )
        )

    def finish(self) -> int:
        passed = sum(value for _, _, value in self.results)
        failed = len(self.results) - passed
        print(f"TOTAL: PASS={passed} FAIL={failed}")
        return failed


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args,
        cwd=ROOT,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
    ).strip()


def worktree_blob(path: str) -> str:
    """The blob of a worktree path, or "" when the path is not there yet."""
    result = subprocess.run(
        ("git", "hash-object", path),
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    )
    return result.stdout.strip() if result.returncode == 0 else ""


def commit_blob(commit: str, path: str) -> str:
    """The blob at a path in a commit, or "" when the path is absent there."""
    result = subprocess.run(
        ("git", "rev-parse", f"{commit}:{path}"),
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    )
    return result.stdout.strip() if result.returncode == 0 else ""


def resolve_ref(ref: str) -> str:
    result = subprocess.run(
        ("git", "rev-parse", ref),
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    )
    return result.stdout.strip() if result.returncode == 0 else ""


def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, descendant),
        cwd=ROOT,
        check=False,
        capture_output=True,
        timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


def is_hash(value: str) -> bool:
    return re.fullmatch(r"[0-9a-f]{40}", value) is not None


def raw_note() -> str:
    try:
        return NOTE_PATH.read_text(encoding="utf-8")
    except OSError:
        return ""


def normalized_note(text: str) -> str:
    return " ".join(text.lower().split())


def compact_note(text: str) -> str:
    return "".join(text.lower().split())


def no_float(value: object) -> bool:
    return b162.no_float(value)


def congruence_inertia(matrix: sp.MatrixBase) -> tuple[int, int, int]:
    """Exact (n_positive, n_zero, n_negative) WITH multiplicity, by congruence.

    Delegated to the COMMITTED Block 144 helper through the Block 162/161/160/
    159/156 import chain, so the tool this block reasons with is exactly the blob
    Block 162's gate A pins.  Called on EXACT algebraic matrices only.
    """
    return b162.congruence_inertia(matrix)


def sturm_inertia(matrix: sp.MatrixBase) -> tuple[int, int, int]:
    """The SECOND, INDEPENDENT inertia route, used only under --deep.

    Exact real-root counting on the characteristic polynomial, delegated to the
    Block 161 helper through Block 162.  It shares no code path with the
    committed congruence helper, so an agreement between the two is a genuine
    cross-check.  It returns a NEGATIVE sentinel on inputs it cannot resolve;
    those cells are counted and DISCLOSED rather than silently dropped.
    """
    return b162.sturm_inertia(matrix)


def guarded_inertia(matrix: sp.MatrixBase):
    """congruence_inertia, with the landed helper's failure mode DISCLOSED.

    The committed Block 144 congruence route raises on some singular inputs (the
    independent checker hit this on 8 of its 2304 twelve-row cells).  A cell the
    landed tool cannot resolve is returned as None, counted, and reported --
    never counted as a positive and never counted against one.
    """
    try:
        return congruence_inertia(matrix)
    except Exception:                    # noqa: BLE001 - disclosed tool limit
        return None


def is_psd(inertia) -> bool:
    """H1-163: no negative direction AND a nonzero positive count.

    The zero form has inertia (0, n, 0) and is NEVER counted as a positive; an
    unresolved cell is never counted as a positive either.  (The checker's own
    first predicate tested definiteness -- n_zero == 0 as well -- and hid every
    semidefinite hit; this is the corrected predicate.)
    """
    return inertia is not None and inertia[2] == 0 and inertia[0] > 0


# ---------------------------------------------------------------------------
# A. authority
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class AuthorityCertificate:
    fixed_authority: bool
    parent_pin_is_commit: bool
    parent_ref_and_ancestry: bool
    parent_artifact_blobs: bool
    stale_parent_artifact_blobs: bool


def resolved_parent_commit() -> str:
    if is_hash(PARENT_COMMIT):
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
        and worktree_blob(REGISTRY_PATH) == WORKTREE_REGISTRY_BLOB
    )

    parent = resolved_parent_commit()
    worktree_blobs = tuple(worktree_blob(path) for path in PARENT_ARTIFACTS)
    committed_blobs = tuple(
        commit_blob(parent, path) for path in PARENT_ARTIFACTS
    )
    stale_blobs = tuple(
        commit_blob(STALE_PARENT_COMMIT, path) for path in PARENT_ARTIFACTS
    )
    return AuthorityCertificate(
        fixed_authority,
        is_hash(PARENT_COMMIT),
        bool(
            is_hash(parent)
            and is_ancestor(parent, "HEAD")
            and (
                not is_hash(PARENT_COMMIT)
                or resolve_ref(PARENT_REF) == PARENT_COMMIT
            )
        ),
        bool(
            len(committed_blobs) == len(PARENT_ARTIFACTS) == 2
            and all(is_hash(value) for value in committed_blobs)
            and committed_blobs == worktree_blobs
            and committed_blobs == PARENT_ARTIFACT_BLOBS
        ),
        bool(
            len(stale_blobs) == len(PARENT_ARTIFACTS) == 2
            and all(is_hash(value) for value in stale_blobs)
            and stale_blobs == worktree_blobs
        ),
    )


# ---------------------------------------------------------------------------
# the committed model, imported wholesale through Block 162
# ---------------------------------------------------------------------------
SIZE = b145.SIZE                          # 32 cover sites
COVER_T = b145.COVER_T                    # 8 cover time slices
PHYS_T = b145.PHYS_T                      # 4 quotient time slices
LX = b145.LX                              # 4
PHYS = b145.PHYS                          # 16 quotient sites
HALF = b145.HALF                          # 8

MASS = b145.MASS
X0 = b145.X0
THETA = b145.THETA
THETA_PRIME_OP = b156.THETA_PRIME_OP
HQ_FREE = b156.HQ_FREE
EDGE_KEYS = b145.EDGE_KEYS
HEALING_WEIGHTS = b145.HEALING_WEIGHTS
SHEAR_X, SHEAR_T = b156.SHEAR_X, b156.SHEAR_T
NU, A_MOD, B_MOD, INV = (
    b145.NU_MODULUS, b145.A_MODULUS, b145.B_MODULUS, b145.INV_MODULUS
)

ATLAS = {SHEAR_X: R(3, 5), SHEAR_T: R(4, 5)}
ZERO_T = {SHEAR_T: sp.Integer(0), SHEAR_X: R(3, 5)}
MASSES = (R(1, 10), sp.Integer(1), sp.Integer(5), sp.Integer(20),
          sp.Integer(-1))


# ---------------------------------------------------------------------------
# the certificate constants this runner is claiming
# ---------------------------------------------------------------------------
EDGE_COUNT = 16
COVER_REFLECTIONS = 64
SITE_REFLECTIONS = 32
LINK_REFLECTIONS = 32
INVOLUTIVE_COUNT = 24
COVARIANT_COUNT = 16
NON_COVARIANT_COUNT = 8
X0_EVEN_SITE = 16
X0_ODD_SITE = 16
THETA_PRIME_PARITY = 8
FIXED_SLICE_SIGN = 1
SWAP_SLICE_SIGN = -1
INVARIANT_SLICES = 2
HQ_DISPLACEMENTS = (0, 1, 3)
COVER_OFF_DIAGONAL = 64
COVER_OFF_DISPLACEMENTS = (1, 7)
DISTANCE_TWO_ENTRIES = 16
MASS_INERTIA_TABLE = {
    (1, 0, (4, 4, 0)): 4, (1, 2, (2, 4, 2)): 4,
    (-1, 0, (3, 4, 1)): 4, (-1, 2, (3, 4, 1)): 4,
    (-1, 1, (2, 4, 2)): 4, (-1, 3, (2, 4, 2)): 4,
}
CALIBRATION_CELLS = 320
SHEAR_FREE_CARRIERS = 5
X_TRIVIAL_COUNT = 4
FLAT_STRUCTURE_CELLS = 384
DET_C_NONZERO = 376
DET_C_ZERO = 8
DET_C_ZERO_EDGE = (1, 2)
FLAT_CENSUS = {(4, 0, 4): 2256, (2, 4, 2): 48}
FLAT_CENSUS_CELLS = 2304
HYPERBOLIC_INERTIA = (4, 0, 4)
SINGULAR_C_INERTIA = (2, 4, 2)
CALIBRATION_INERTIA = (4, 4, 0)
CALIBRATION_NSD_INERTIA = (0, 4, 4)
CLOSED_MASS_INERTIA = (4, 4, 4)
CLOSED_MASS_CELLS = 48
CLOSED_CELLS = 2304
CLOSED_CARRIERS = 3
SWEEP_CARRIERS = 4
SWEEP_MASSES = 3
SWEEP_CELLS = 4608
ST0_CARRIERS = 3
ST0_CELLS = 1152
ST0_PSD_CELLS = 64
LOCAL_SHEARED_PSD = 32
LOCAL_FREE_NOT_PSD = 32
WITNESS_LABEL = (-1, 2, 1, 0)
WITNESS_EDGE = (0, 0)
WITNESS_FIXED_SLICE = 1
WITNESS_INERTIA = (4, 4, 0)
WITNESS_NSD_INERTIA = (0, 4, 4)
SELECTION_CELLS = 2 * 6 * 8
CHECKER_ST0_PSD = 80
CHECKER_ST0_CELLS = 1152
CHECKER_LOCAL_COUNTEREXAMPLES = 48
CHECKER_SWEEP_CELLS = 15360
SOLVE_SWEEP_CELLS = 13440
POOL_TWO_LEADS = 3

RUNTIME_BUDGET_SEC = 150


# ---------------------------------------------------------------------------
# constructions.  Everything below is built from the committed primitives.
# ---------------------------------------------------------------------------
def herm(matrix: sp.MatrixBase) -> sp.Matrix:
    """The committed Hermitian part; the pairing carries i's, so .H not .T."""
    return sp.expand((matrix + matrix.H) / 2)


def selector(rows: tuple) -> sp.Matrix:
    out = sp.zeros(PHYS, len(rows))
    for column, row in enumerate(rows):
        out[row, column] = 1
    return out


def slice_rows(*slices: int) -> tuple:
    return tuple(LX * (s % PHYS_T) + x for s in slices for x in range(LX))


def descend(label: tuple):
    """The committed descent of a cover move through the antiperiodic quotient."""
    return b142.descend(b148.move_matrix(b148.move_permutation(label)))


def pairing(reflection: sp.Matrix, action: sp.Matrix, rows: tuple) -> sp.Matrix:
    """[r Q]_{S,S}: the committed b159.half_pairing law, read on a slice union."""
    sel = selector(rows)
    return herm(sp.expand(sel.T * reflection * action * sel))


def field_of(shear_of, volume_of) -> dict:
    """A carrier field, built STRICTLY from sympy exacts.

    DISCLOSED TOOL DEFECT: the landed b145.moduli_from_field evaluates
    a = volume / (1 - shear**2), which returns a PYTHON FLOAT when the pair is
    plain ints (1/(1-0) = 1.0).  b159.flat_field() is safe; a hand-built carrier
    is not.  Every carrier this runner builds goes through here, and gate C
    measures both the leak and this constructor's immunity to it.
    """
    return {
        (t, x): (sp.sympify(shear_of(t, x)), sp.sympify(volume_of(t, x)))
        for t in range(PHYS_T)
        for x in range(LX)
    }


def signed_image(matrix: sp.Matrix) -> dict:
    """site -> (image site, sign) for a signed permutation on the quotient."""
    out = {}
    for j in range(PHYS):
        column = [(i, matrix[i, j]) for i in range(PHYS) if matrix[i, j] != 0]
        if len(column) != 1:
            return {}
        out[j] = column[0]
    return out


ALL_TIME_REFLECTIONS = tuple(
    (-1, pt, ex, px)
    for pt in range(COVER_T)
    for ex in (1, -1)
    for px in range(LX)
)
SITE_LABELS = tuple(lab for lab in ALL_TIME_REFLECTIONS if lab[1] % 2 == 0)
LINK_LABELS = tuple(lab for lab in ALL_TIME_REFLECTIONS if lab[1] % 2 == 1)
DESCENT = {lab: descend(lab) for lab in ALL_TIME_REFLECTIONS}
INVOLUTIVE_SITE = tuple(
    lab for lab in SITE_LABELS
    if DESCENT[lab] is not None
    and sp.expand(DESCENT[lab] * DESCENT[lab]) == sp.eye(PHYS)
)
X_TRIVIAL = tuple(lab for lab in INVOLUTIVE_SITE if lab[2] == 1 and lab[3] == 0)


def fixed_slice(label: tuple) -> int:
    """The quotient slice a site reflection genuinely fixes: c = p_t / 2."""
    return (label[1] // 2) % PHYS_T


def half_support(label: tuple) -> tuple:
    """The OS non-negative side INCLUDING the fixed slice: {c, c+1}."""
    c = fixed_slice(label)
    return slice_rows(c, c + 1)


def closed_support(label: tuple) -> tuple:
    """The closed OS region {c, c+1, c+2}: both invariant slices shared."""
    c = fixed_slice(label)
    return slice_rows(c, c + 1, c + 2)


def lift_sign(t: int) -> int:
    """s(t) with psi(t) = s(t) phi(t mod 4), read off b142.LIFT = vstack(-I, I).

    Exact integers only: Python's (-1) ** (negative int) returns a FLOAT, which
    is precisely the bug that made the checker's first pass report 12
    involutions instead of 24.
    """
    return -1 if (t // 4) % 2 == 0 else 1


def analytic_descent(label: tuple) -> sp.Matrix:
    """The descent derived from the lift, NOT imported from b142.

    (r phi)(a, x) = sigma(a) phi((p_t - a) mod 4, e_x (x - p_x) mod 4) with
    sigma(a) = s(a) s(p_t - a).  Gate B measures this against the committed
    b142.descend on all 64 labels, which is what turns the antiperiodicity sign
    law from a measurement into a proof.
    """
    _et, pt, ex, px = label
    out = sp.zeros(PHYS, PHYS)
    for a in range(PHYS_T):
        b = (pt - a) % PHYS_T
        sign = lift_sign(a) * lift_sign(pt - a)
        for x in range(LX):
            y = (ex * (x - px)) % LX
            out[LX * a + x, LX * b + y] = sign
    return out


DIFFERENTIALS, STAR = b145.connection(SHEAR_X, SHEAR_T)
EDGE_DIFF = b145.edge_differentials(DIFFERENTIALS, STAR, HEALING_WEIGHTS)
COVER_FREE = b145.cover_hodge_general(NU, A_MOD, B_MOD, INV)

# the carrier bench, every field exact and every one cone-admissible; the three
# families are kept apart because the block's three questions need them apart.
FLAT_FIELD = b159.flat_field()
SHEAR_FREE_BENCH = (
    ("flat", FLAT_FIELD),
    ("graded nu", field_of(lambda t, x: 0, lambda t, x: R(1 + t + x, 2))),
    ("alternating nu",
     field_of(lambda t, x: 0, lambda t, x: R(3, 2) if (t + x) % 2 else R(2, 3))),
    ("wild nu",
     field_of(lambda t, x: 0, lambda t, x: R(1 + (3 * t + 5 * x) % 7, 4))),
    ("tiny/large nu",
     field_of(lambda t, x: 0, lambda t, x: R(1, 9) if (t + x) % 2 else R(9, 1))),
)
# NON-DIAGONAL-H_q carriers: the s_t = 0 discovery lives here.  "slice-3 shear"
# is the checker's witness carrier, reproduced exactly.
ST0_BENCH = (
    ("slice-3 shear", field_of(lambda t, x: R(1, 2) if t == 3 else 0,
                               lambda t, x: 1)),
    ("single-cell shear", field_of(lambda t, x: R(1, 2) if (t, x) == (3, 0)
                                   else 0, lambda t, x: 1)),
    ("uniform shear 3/7", field_of(lambda t, x: R(3, 7), lambda t, x: 1)),
)
WITNESS_FIELD = ST0_BENCH[0][1]
# the checker's duality-converse carrier: alternating +-1/5, nu = 1
CONVERSE_FIELD = field_of(
    lambda t, x: R(1, 5) if (t + x) % 2 else R(-1, 5), lambda t, x: 1
)
SWEEP_BENCH = (
    ("counterpoint", b159.counterpoint_field()),
    ("control A", b159.control_field_a()),
    ("alternating shear 1/5", CONVERSE_FIELD),
    ("slice-3 shear", WITNESS_FIELD),
)
CLOSED_BENCH = (
    ("flat", FLAT_FIELD),
    ("counterpoint", b159.counterpoint_field()),
    ("control A", b159.control_field_a()),
)

_ACTION_CACHE: dict = {}


def actions_for(name: str, field: dict) -> dict:
    """The committed quotient action per healed edge, cached per carrier."""
    if name not in _ACTION_CACHE:
        hodge = b145.cover_hodge_from_field(field)
        _ACTION_CACHE[name] = {
            key: b145.quotient_action(EDGE_DIFF[key], hodge, MASS)
            for key in EDGE_KEYS
        }
    return _ACTION_CACHE[name]


def quotient_hodge(field: dict) -> sp.Matrix:
    return b145.quotient(b145.cover_hodge_from_field(field))


def locally_shear_free(field: dict, label: tuple) -> bool:
    """The checker's proposed LOCAL repair: shear-free on the support slices.

    Gate F measures it and REFUTES it in both directions; it is measured here
    exactly so that it can be refuted rather than assumed.
    """
    c = fixed_slice(label)
    return all(
        field[(t % PHYS_T, x)][0] == 0
        for t in (c, c + 1) for x in range(LX)
    )


# ---------------------------------------------------------------------------
# measured facts (computed once, before any mutation flag is consulted)
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Facts:
    main_head: str
    authority: AuthorityCertificate
    # B: the family, the descent, the sign law, the grading
    family: tuple
    signs: tuple
    grading: tuple
    # C: the mass, the calibration, the displacement theorem
    mass: tuple
    calibration: tuple
    displacement: tuple
    # D: M1
    annihilation: tuple
    # E: M2, M3, the sweep
    antipodal: tuple
    sweep: tuple
    # F: the s_t = 0 discovery
    discovery: tuple
    # G: the selection rule and the demoted duality
    selection: tuple
    duality: tuple
    # deep sweeps
    deep_flat: object
    deep_sweep: object
    # H / global
    exact_no_float: bool
    scope: dict


def measure(deep: bool) -> Facts:
    main_head = git_output("rev-parse", "origin/main")
    authority = authority_certificate(main_head)
    exact: list = []

    # ---------------------------------------------------------------- B ----
    covariant_matches = all(
        (lab in b148.COVARIANT_MOVES) == (lab[2] == -1)
        for lab in SITE_LABELS
    )
    family = (
        len(ALL_TIME_REFLECTIONS),
        len(SITE_LABELS),
        len(LINK_LABELS),
        sum(1 for lab in ALL_TIME_REFLECTIONS if DESCENT[lab] is not None),
        len(INVOLUTIVE_SITE),
        (sum(1 for lab in INVOLUTIVE_SITE if lab[2] == -1),
         sum(1 for lab in INVOLUTIVE_SITE if lab[2] == 1)),
        covariant_matches,
        # the LINK class has no fixed cover slice at all: p_t odd
        all(lab[1] % 2 == 1 for lab in LINK_LABELS),
        # every non-involutive site label is an x-translation (e_x = +1, p_x odd)
        tuple(sorted({(lab[2], lab[3] % 2) for lab in SITE_LABELS
                      if lab not in INVOLUTIVE_SITE})),
        len(X_TRIVIAL),
    )

    # the sign law, measured on the committed descent AND proved from the lift
    sign_rows = []
    analytic_agreement = sum(
        1 for lab in ALL_TIME_REFLECTIONS
        if sp.expand(analytic_descent(lab) - DESCENT[lab]) == sp.zeros(PHYS)
    )
    for lab in INVOLUTIVE_SITE:
        image = signed_image(DESCENT[lab])
        c = fixed_slice(lab)
        self_slices: dict = {}
        for j in range(PHYS):
            target, sign = image[j]
            if target // LX == j // LX:
                self_slices.setdefault(j // LX, set()).add(sign)
        got = {s: tuple(sorted(v)) for s, v in self_slices.items()}
        want = {c: (FIXED_SLICE_SIGN,),
                (c + 2) % PHYS_T: (SWAP_SLICE_SIGN,)}
        sign_rows.append((lab, got == want, len(got)))
    # the analytic law itself, read off sigma(a) = s(a) s(p_t - a) with p_t = 2c
    analytic_law = tuple(
        (c,
         lift_sign(c) * lift_sign(2 * c - c),
         lift_sign((c + 2) % PHYS_T) * lift_sign(2 * c - ((c + 2) % PHYS_T)))
        for c in range(PHYS_T)
    )
    signs = (
        sum(1 for _lab, ok, _n in sign_rows if ok),
        len(sign_rows),
        tuple(sorted({n for _lab, _ok, n in sign_rows})),
        analytic_agreement,
        analytic_law,
        # the spatial action on the fixed slice
        all(
            signed_image(DESCENT[lab])[LX * fixed_slice(lab) + x][0] % LX
            == (lab[2] * x + lab[3]) % LX
            for lab in INVOLUTIVE_SITE for x in range(LX)
        ),
    )

    grading_ok = True
    grading_census = collections.Counter()
    for lab in ALL_TIME_REFLECTIONS:
        op = DESCENT[lab]
        sign = 1 if (lab[1] + lab[3]) % 2 == 0 else -1
        if sp.expand(op * X0 * op.T - sign * X0) != sp.zeros(PHYS):
            grading_ok = False
        if lab in SITE_LABELS:
            grading_census[sign] += 1
    grading = (
        grading_ok,
        (grading_census[1], grading_census[-1]),
        (sum(1 for lab in INVOLUTIVE_SITE if (lab[1] + lab[3]) % 2 == 0),
         sum(1 for lab in INVOLUTIVE_SITE if (lab[1] + lab[3]) % 2 == 1)),
        # THE CORRECTION: theta anticommutes, theta-prime COMMUTES
        sp.expand(THETA * X0 + X0 * THETA) == sp.zeros(PHYS),
        sp.expand(THETA_PRIME_OP * X0 - X0 * THETA_PRIME_OP) == sp.zeros(PHYS),
        (7 + 0, 7 + 1),
        sp.expand(THETA - DESCENT[(-1, 7, -1, 0)]) == sp.zeros(PHYS),
        sp.expand(THETA_PRIME_OP - DESCENT[(-1, 7, -1, 1)]) == sp.zeros(PHYS),
    )

    # ---------------------------------------------------------------- C ----
    flat_hq = quotient_hodge(FLAT_FIELD)
    theta_flat = pairing(THETA, MASS * flat_hq, slice_rows(0, 1))
    prime_flat = pairing(THETA_PRIME_OP, MASS * flat_hq, slice_rows(0, 1))
    mass_only = {
        lab: pairing(DESCENT[lab], MASS * flat_hq, half_support(lab))
        for lab in INVOLUTIVE_SITE
    }
    mass_table = collections.Counter()
    for lab in INVOLUTIVE_SITE:
        signature = congruence_inertia(
            sp.expand(mass_only[lab].xreplace({MASS: 1}))
        )
        mass_table[(lab[2], lab[3], signature)] += 1
    mass = (
        flat_hq == sp.eye(PHYS),
        theta_flat == sp.zeros(HALF, HALF),
        prime_flat == sp.zeros(HALF, HALF),
        sum(1 for lab in INVOLUTIVE_SITE
            if mass_only[lab] != sp.zeros(HALF, HALF)),
        dict(mass_table),
        # M3: every COVARIANT mass block is indefinite
        sum(1 for lab in INVOLUTIVE_SITE if lab[2] == -1
            and min(congruence_inertia(
                sp.expand(mass_only[lab].xreplace({MASS: 1}))
            )[0::2]) > 0),
    )
    exact.append(sum(mass_only[INVOLUTIVE_SITE[0]]))

    # the calibration: s_t = 0, s_x LEFT SYMBOLIC, every shear-free carrier
    calibration_cells = 0
    calibration_exact = 0
    calibration_shape = None
    calibration_inertias = collections.Counter()
    for name, field in SHEAR_FREE_BENCH:
        # "diag(nu)" is the FIXED-SLICE DIAGONAL BLOCK OF H_q, which is exactly
        # the identity on the flat carrier and the carrier's own volume profile
        # otherwise; it is read off the committed quotient Hodge, never assumed.
        hq_field = quotient_hodge(field)
        actions = actions_for(name, field)
        for lab in X_TRIVIAL:
            rows = half_support(lab)
            target = sp.diag(*(
                [MASS * hq_field[row, row] for row in rows[:LX]] + [0] * LX
            ))
            for key in EDGE_KEYS:
                form = sp.expand(
                    pairing(DESCENT[lab], actions[key], rows).xreplace(
                        {SHEAR_T: 0}
                    )
                )
                calibration_cells += 1
                if sp.expand(form - target) == sp.zeros(HALF, HALF):
                    calibration_exact += 1
                if calibration_shape is None:
                    calibration_shape = form
                for value in (sp.Integer(1), sp.Integer(-1)):
                    calibration_inertias[(
                        1 if value > 0 else -1,
                        congruence_inertia(sp.expand(form.xreplace(
                            {MASS: value}
                        ))),
                    )] += 1
    plain_int_field = {
        (t, x): (0, 1) for t in range(PHYS_T) for x in range(LX)
    }
    calibration = (
        calibration_cells,
        calibration_exact,
        len(SHEAR_FREE_BENCH),
        # s_x is still symbolic in the form and drops out identically
        SHEAR_X in set().union(*[
            sp.sympify(entry).free_symbols
            for entry in actions_for("flat", FLAT_FIELD)[EDGE_KEYS[0]]
        ]),
        calibration_shape.free_symbols == {MASS}
        or calibration_shape.free_symbols == set(),
        dict(calibration_inertias),
        all(b145.in_admissible_cone(field) for _n, field in SHEAR_FREE_BENCH),
        # the DISCLOSED tool leak, measured both ways
        all(no_float(value)
            for value in b145.moduli_from_field(plain_int_field)[1].values()),
        all(no_float(value) for _n, field in SHEAR_FREE_BENCH
            for cell in field for value in field[cell]),
        # shear-free <=> H_q diagonal, the structural half of the calibration
        all(quotient_hodge(field).is_diagonal()
            for _n, field in SHEAR_FREE_BENCH),
        # and on the flat carrier the form is LITERALLY m I_4 (+) 0_4
        sp.expand(
            pairing(DESCENT[X_TRIVIAL[0]],
                    actions_for("flat", FLAT_FIELD)[EDGE_KEYS[0]],
                    half_support(X_TRIVIAL[0])).xreplace({SHEAR_T: 0})
            - sp.diag(*([MASS] * LX + [0] * LX))
        ) == sp.zeros(HALF, HALF),
    )

    # E2, as a ONE-LINE structural theorem rather than a scan
    cover_off = tuple(
        (i, j) for i in range(SIZE) for j in range(SIZE)
        if i != j and sp.expand(COVER_FREE[i, j]) != 0
    )
    b_symbols = set(B_MOD.values())
    generic_action = b145.quotient_action(
        EDGE_DIFF[(2, 2)], COVER_FREE, MASS
    )
    distance_two = tuple(
        sp.factor(sp.expand(generic_action[i, j]))
        for i in range(PHYS) for j in range(PHYS)
        if (i // LX - j // LX) % PHYS_T == 2
        and sp.expand(generic_action[i, j]) != 0
    )
    displacement = (
        len(cover_off),
        tuple(sorted({((i // LX) - (j // LX)) % COVER_T
                      for i, j in cover_off})),
        all(sp.expand(COVER_FREE[i, j]).free_symbols <= b_symbols
            for i, j in cover_off),
        tuple(sorted({((i // LX) - (j // LX)) % PHYS_T
                      for i in range(PHYS) for j in range(PHYS)
                      if sp.expand(HQ_FREE[i, j]) != 0})),
        sum(1 for i in range(PHYS) for j in range(PHYS)
            if (i // LX - j // LX) % PHYS_T == 2
            and sp.expand(HQ_FREE[i, j]) != 0),
        len(distance_two),
        all(sp.expand(entry.xreplace({SHEAR_T: 0})) == 0
            for entry in distance_two),
        all(sp.expand(entry.xreplace({b: 0 for b in b_symbols})) == 0
            for entry in distance_two),
    )
    exact.append(sum(distance_two))

    # ---------------------------------------------------------------- D ----
    flat_actions = actions_for("flat", FLAT_FIELD)
    zero_block = 0
    structure_cells = 0
    det_nonzero = 0
    det_zero_edges = collections.Counter()
    det_ratio_rational = 0
    flat_census = collections.Counter()
    blind_cells = 0
    nonzero_cells = 0
    zero_t_block_zero = 0
    for lab in INVOLUTIVE_SITE:
        rows = half_support(lab)
        for key in EDGE_KEYS:
            form = pairing(DESCENT[lab], flat_actions[key], rows)
            structure_cells += 1
            if form[LX:HALF, LX:HALF] == sp.zeros(LX, LX):
                zero_block += 1
            block_c = form[0:LX, LX:HALF]
            determinant = sp.expand(block_c.det())
            if determinant == 0:
                det_zero_edges[key] += 1
            else:
                det_nonzero += 1
                ratio = sp.cancel(determinant / SHEAR_T ** 4)
                if ratio.free_symbols == set():
                    det_ratio_rational += 1
            if sp.expand(block_c.xreplace({SHEAR_T: 0})) == sp.zeros(LX, LX):
                zero_t_block_zero += 1
            atlas_form = sp.expand(form.xreplace(ATLAS))
            signatures = set()
            for value in MASSES + (sp.Integer(0),):
                signature = congruence_inertia(
                    sp.expand(atlas_form.xreplace({MASS: value}))
                )
                flat_census[signature] += 1
                signatures.add(signature)
            if len(signatures) == 1:
                blind_cells += 1
            if sp.expand(atlas_form.xreplace({MASS: 1})) != sp.zeros(HALF, HALF):
                nonzero_cells += 1
    annihilation = (
        zero_block,
        structure_cells,
        det_nonzero,
        det_ratio_rational,
        sum(det_zero_edges.values()),
        tuple(sorted(det_zero_edges)),
        dict(flat_census),
        sum(flat_census.values()),
        sum(count for signature, count in flat_census.items()
            if is_psd(signature)),
        blind_cells,
        nonzero_cells,
        # the BOUNDARY the checker asked for: at s_t = 0 on an unsheared H_q the
        # hyperbolic block is IDENTICALLY ZERO, so M1 is VACUOUS there
        zero_t_block_zero,
    )

    # ---------------------------------------------------------------- E ----
    closed_mass = collections.Counter()
    for lab in INVOLUTIVE_SITE:
        form = pairing(DESCENT[lab], MASS * flat_hq, closed_support(lab))
        for value in (sp.Integer(1), sp.Integer(-1)):
            closed_mass[congruence_inertia(
                sp.expand(form.xreplace({MASS: value}))
            )] += 1
    closed_census = collections.Counter()
    closed_unresolved = 0
    closed_cells = 0
    for name, field in CLOSED_BENCH:
        actions = actions_for(name, field)
        for lab in INVOLUTIVE_SITE:
            rows = closed_support(lab)
            for key in EDGE_KEYS:
                form = sp.expand(
                    pairing(DESCENT[lab], actions[key], rows).xreplace(ATLAS)
                )
                for value in (sp.Integer(1), sp.Integer(5)):
                    closed_cells += 1
                    signature = guarded_inertia(
                        sp.expand(form.xreplace({MASS: value}))
                    )
                    if signature is None:
                        closed_unresolved += 1
                    else:
                        closed_census[signature] += 1
    antipodal = (
        dict(closed_mass),
        sum(closed_mass.values()),
        sum(count for signature, count in closed_mass.items()
            if is_psd(signature)),
        closed_cells,
        len(CLOSED_BENCH),
        sum(count for signature, count in closed_census.items()
            if is_psd(signature)),
        closed_unresolved,
        dict(closed_census),
    )

    sweep_census = collections.Counter()
    sweep_cells = 0
    sweep_unresolved = 0
    best = (0, 0, 0)
    for name, field in SWEEP_BENCH:
        actions = actions_for(name, field)
        for lab in INVOLUTIVE_SITE:
            rows = half_support(lab)
            for key in EDGE_KEYS:
                form = sp.expand(
                    pairing(DESCENT[lab], actions[key], rows).xreplace(ATLAS)
                )
                for value in (R(1, 10), sp.Integer(1), sp.Integer(-1)):
                    sweep_cells += 1
                    signature = guarded_inertia(
                        sp.expand(form.xreplace({MASS: value}))
                    )
                    if signature is None:
                        sweep_unresolved += 1
                        continue
                    sweep_census[signature] += 1
                    if signature[0] > best[0]:
                        best = signature
    sweep = (
        sweep_cells,
        len(SWEEP_BENCH),
        sum(count for signature, count in sweep_census.items()
            if is_psd(signature)),
        sweep_unresolved,
        best,
        all(b145.in_admissible_cone(field) for _n, field in SWEEP_BENCH),
        dict(sweep_census),
        # the cone premise: uniformly positive definite, and it locks nothing
        tuple(sorted({
            congruence_inertia(sp.Matrix(
                HALF, HALF,
                lambda i, j: quotient_hodge(field)[half_support(lab)[i],
                                                   half_support(lab)[j]]
            ))
            for _n, field in SWEEP_BENCH for lab in INVOLUTIVE_SITE[:4]
        })),
    )

    # ---------------------------------------------------------------- F ----
    st0_census = collections.Counter()
    st0_cells = 0
    st0_psd = 0
    psd_nondiagonal = 0
    local_sheared_psd = 0
    local_free_not_psd = 0
    local_sheared_psd_all = 0
    local_free_not_psd_all = 0
    witness_form = None
    for name, field in ST0_BENCH:
        actions = actions_for(name, field)
        hq_diagonal = quotient_hodge(field).is_diagonal()
        for lab in INVOLUTIVE_SITE:
            rows = half_support(lab)
            for key in EDGE_KEYS:
                form = sp.expand(
                    pairing(DESCENT[lab], actions[key], rows).xreplace(ZERO_T)
                )
                signature = congruence_inertia(
                    sp.expand(form.xreplace({MASS: 1}))
                )
                st0_cells += 1
                st0_census[signature] += 1
                positive = is_psd(signature)
                # The local repair is tested WHERE THE CORNER CLAIM LIVES -- on
                # the x-trivial reflections -- so that a counterexample is a
                # counterexample to the repair and not merely to M3, which
                # already excludes every covariant reflection.
                x_trivial = lab in X_TRIVIAL
                shear_free_here = locally_shear_free(field, lab)
                if positive:
                    st0_psd += 1
                    if not hq_diagonal:
                        psd_nondiagonal += 1
                    if not shear_free_here:
                        local_sheared_psd_all += 1
                        if x_trivial:
                            local_sheared_psd += 1
                elif shear_free_here:
                    local_free_not_psd_all += 1
                    if x_trivial:
                        local_free_not_psd += 1
                if (name == ST0_BENCH[0][0] and lab == WITNESS_LABEL
                        and key == WITNESS_EDGE):
                    witness_form = form
    witness_target = sp.diag(*([MASS] * LX + [0] * LX))
    discovery = (
        st0_cells,
        len(ST0_BENCH),
        st0_psd,
        psd_nondiagonal,
        local_sheared_psd,
        local_free_not_psd,
        dict(st0_census),
        # the exact witness, rebuilt entry by entry
        b145.in_admissible_cone(WITNESS_FIELD),
        quotient_hodge(WITNESS_FIELD).is_diagonal(),
        fixed_slice(WITNESS_LABEL),
        sp.expand(witness_form - witness_target) == sp.zeros(HALF, HALF)
        if witness_form is not None else False,
        congruence_inertia(sp.expand(witness_form.xreplace({MASS: 1})))
        if witness_form is not None else None,
        congruence_inertia(sp.expand(witness_form.xreplace({MASS: -1})))
        if witness_form is not None else None,
        tuple(sp.expand(witness_form[j, j].xreplace({MASS: 1}))
              for j in range(HALF)) if witness_form is not None else (),
        WITNESS_LABEL in INVOLUTIVE_SITE,
        WITNESS_LABEL[2] == 1 and WITNESS_LABEL[3] == 0,
        (local_sheared_psd_all, local_free_not_psd_all),
    )
    exact.append(sum(witness_form) if witness_form is not None else 0)

    # ---------------------------------------------------------------- G ----
    selection_ok = True
    selection_cells = 0
    even_agreements = 0
    even_cells = 0
    odd_agreements = 0
    odd_cells = 0
    flip_ok = True
    for name, field in (("flat", FLAT_FIELD), SWEEP_BENCH[0]):
        actions = actions_for(name, field)
        hodge = b145.cover_hodge_from_field(field)
        hq = b145.quotient(hodge)
        for lab in INVOLUTIVE_SITE[:6]:
            rows = half_support(lab)
            grade = sp.diag(*[X0[row, row] for row in rows])
            sign = 1 if (lab[1] + lab[3]) % 2 == 0 else -1
            for key in EDGE_KEYS[:8]:
                forward = actions[key]
                reversed_k = b145.quotient_action(
                    sp.expand(-EDGE_DIFF[key]), hodge, MASS
                )
                if sp.expand(forward + reversed_k - 2 * MASS * hq) != sp.zeros(
                    PHYS, PHYS
                ):
                    flip_ok = False
                left = sp.expand(
                    grade * pairing(DESCENT[lab], forward, rows) * grade
                )
                right = sp.expand(
                    sign * pairing(DESCENT[lab], reversed_k, rows)
                )
                selection_cells += 1
                if sp.expand(left - right) != sp.zeros(HALF, HALF):
                    selection_ok = False
                plus = congruence_inertia(sp.expand(
                    pairing(DESCENT[lab], forward, rows).xreplace(ATLAS)
                    .xreplace({MASS: 1})
                ))
                minus = congruence_inertia(sp.expand(
                    pairing(DESCENT[lab], reversed_k, rows).xreplace(ATLAS)
                    .xreplace({MASS: 1})
                ))
                if sign == 1:
                    even_cells += 1
                    even_agreements += int(plus == minus)
                else:
                    odd_cells += 1
                    odd_agreements += int(plus == minus)
    selection = (
        selection_ok,
        selection_cells,
        flip_ok,
        (even_agreements, even_cells),
        (odd_agreements, odd_cells),
        # the CORRECTED scope: theta-prime shares the even sector
        (7 + 1) % 2 == 0,
    )

    converse_hq = quotient_hodge(CONVERSE_FIELD)
    duality = (
        # direction A forward: diagonal H_q kills the exchanging mass pairing
        theta_flat == sp.zeros(HALF, HALF),
        prime_flat == sp.zeros(HALF, HALF),
        # direction A converse: FAILS -- still zero on a NON-diagonal H_q
        converse_hq.is_diagonal(),
        b145.in_admissible_cone(CONVERSE_FIELD),
        pairing(THETA, MASS * converse_hq, slice_rows(0, 1))
        == sp.zeros(HALF, HALF),
        # and the asymmetry inside the exchanging class itself
        pairing(THETA_PRIME_OP, MASS * converse_hq, slice_rows(0, 1))
        == sp.zeros(HALF, HALF),
        # the EQUIVOCATION, measured: the site pairing is never zero, only
        # signature-blind
        nonzero_cells,
        blind_cells,
        structure_cells,
    )

    # ------------------------------------------------------------- deep ----
    deep_flat = None
    deep_sweep = None
    if deep:
        agree = 0
        disagree = 0
        sentinel = 0
        sampled = 0
        for lab in INVOLUTIVE_SITE[:8]:
            rows = half_support(lab)
            for key in EDGE_KEYS[:8]:
                form = sp.expand(
                    pairing(DESCENT[lab], flat_actions[key], rows)
                    .xreplace(ATLAS)
                )
                for value in (sp.Integer(1), sp.Integer(-1)):
                    target = sp.expand(form.xreplace({MASS: value}))
                    route_a = guarded_inertia(target)
                    route_b = sturm_inertia(target)
                    sampled += 1
                    if route_b is None or min(route_b) < 0:
                        sentinel += 1
                    elif route_a == tuple(route_b):
                        agree += 1
                    else:
                        disagree += 1
        deep_flat = (sampled, agree, disagree, sentinel)

        agree2 = 0
        disagree2 = 0
        sentinel2 = 0
        sampled2 = 0
        psd2 = 0
        for name, field in SWEEP_BENCH[:2]:
            actions = actions_for(name, field)
            for lab in INVOLUTIVE_SITE[:8]:
                rows = half_support(lab)
                for key in EDGE_KEYS[:4]:
                    form = sp.expand(
                        pairing(DESCENT[lab], actions[key], rows)
                        .xreplace(ATLAS).xreplace({MASS: 1})
                    )
                    route_a = guarded_inertia(form)
                    route_b = sturm_inertia(form)
                    sampled2 += 1
                    if is_psd(route_a):
                        psd2 += 1
                    if route_b is None or min(route_b) < 0:
                        sentinel2 += 1
                    elif route_a == tuple(route_b):
                        agree2 += 1
                    else:
                        disagree2 += 1
        deep_sweep = (sampled2, agree2, disagree2, sentinel2, psd2)

    pool = [
        flat_hq, theta_flat, prime_flat, mass_only[INVOLUTIVE_SITE[0]],
        calibration_shape, generic_action, converse_hq,
        quotient_hodge(WITNESS_FIELD),
    ]
    if witness_form is not None:
        pool.append(witness_form)
    exact_no_float = bool(
        all(no_float(entry) for matrix in pool for entry in matrix)
        and all(no_float(value) for _n, field in
                SHEAR_FREE_BENCH + ST0_BENCH + SWEEP_BENCH + CLOSED_BENCH
                for cell in field for value in field[cell])
        and all(no_float(value) for value in exact)
    )

    return Facts(
        main_head=main_head,
        authority=authority,
        family=family,
        signs=signs,
        grading=grading,
        mass=mass,
        calibration=calibration,
        displacement=displacement,
        annihilation=annihilation,
        antipodal=antipodal,
        sweep=sweep,
        discovery=discovery,
        selection=selection,
        duality=duality,
        deep_flat=deep_flat,
        deep_sweep=deep_sweep,
        exact_no_float=exact_no_float,
        scope=scope_certificate(raw_note()),
    )


# ---------------------------------------------------------------------------
# the note's required scope
# ---------------------------------------------------------------------------
SCOPE_KEYS = (
    "scout_discipline",
    "measured_never_registered",
    "premise_class_change",
    # --- the family ---------------------------------------------------------
    "site_link_split",
    "never_run",
    "all_descend",
    "involutions",
    "covariant_split",
    "sign_law",
    "sign_law_proved",
    "grading_identity",
    # --- the struck sector claim -------------------------------------------
    "sector_quoted",
    "sector_struck",
    "theta_prime_commutes",
    "site_geometry_new",
    "b153_evenness",
    # --- the mass and the calibration --------------------------------------
    "mass_appears",
    "control_zero",
    "calibration_met",
    "calibration_form",
    "sx_drops_out",
    "e2_theorem",
    "one_line",
    # --- the verdict --------------------------------------------------------
    "verdict_b",
    "true_scope",
    "m1_annihilation",
    "signature_blind",
    "never_zero",
    "m2_antipodal",
    "m3_spatial",
    "flat_census",
    "zero_psd",
    "sentinel_cells",
    # --- the live discovery -------------------------------------------------
    "corner_quoted",
    "corner_struck",
    "psd_region_real",
    "uncharacterized",
    "eighty_cells",
    "witness_displayed",
    "recorded_geometry",
    "corner_not_exact",
    "repair_not_exact",
    "mass_sign_missing",
    "open_question",
    "block_164",
    "b153_echo",
    "echo_not_derivation",
    # --- the demoted duality ------------------------------------------------
    "duality_quoted",
    "duality_demoted",
    "converse_fails",
    "blinded_equivocates",
    "two_theorems",
    "never_a_slogan",
    # --- the selection rule -------------------------------------------------
    "selection_rule",
    "even_sector_blind",
    "corrected_scope",
    # --- discipline and disclosures ----------------------------------------
    "checker_credit",
    "quoted_then_corrected",
    "float_leak",
    "repo_flag",
    "checker_bugs",
    "common_mode",
    "cross_context",
    "not_re_verified",
    "sample_not_cone_wide",
    "os_no_go",
    "curved_os_no_go",
    "worker_profile",
    "axiom",
    "zero_retirement",
    "zero_score",
    "zero_e2e",
    "pool_two",
    "n1_n8",
    "w1",
    "n5_verbatim",
    "no_priority_claim",
    "rho_guard",
)


def scope_certificate(note_text: str) -> dict:
    note = normalized_note(note_text)
    compact = compact_note(note_text)
    return {
        "scout_discipline": "scout" in note,
        "measured_never_registered": "measured" in note
        and "never registered" in note,
        "premise_class_change": "premise-class" in note,
        # --- the family ---------------------------------------------------
        "site_link_split": "32 site" in note and "32 link" in note,
        "never_run": "had only ever run the link class" in note,
        "all_descend": "all 64 descend" in note,
        "involutions": "24 site involutions" in note,
        "covariant_split": "16 covariant" in note and "8 non-covariant" in note,
        "sign_law": "antiperiodicity sign law" in note,
        "sign_law_proved": "proved analytically" in note
        or "proven analytically" in note,
        "grading_identity": "(-1)^(p_t+p_x)" in compact
        or "(-1)^(p_t + p_x)" in note,
        # --- the struck sector claim ---------------------------------------
        "sector_quoted": "a sector the lane never had" in note,
        "sector_struck": "is struck" in note,
        "theta_prime_commutes": "theta' commutes with x_0" in note
        or "theta-prime commutes with x_0" in note,
        "site_geometry_new": "the site geometry" in note,
        "b153_evenness": "block 153" in note,
        # --- the mass and the calibration ----------------------------------
        "mass_appears": "the mass appears" in note,
        "control_zero": "24/24" in note,
        "calibration_met": "the calibration is met" in note,
        "calibration_form": "m diag(nu) + 0_4" in note,
        "sx_drops_out": "drops out identically" in note,
        "e2_theorem": "time displacements {0, +-1}" in note
        or "time displacements {0,+-1}" in compact,
        "one_line": "one-line theorem" in note,
        # --- the verdict ----------------------------------------------------
        "verdict_b": "verdict shape (b)" in note,
        "true_scope": "true scope" in note,
        "m1_annihilation": "hyperbolic annihilation" in note,
        "signature_blind": "signature-blind" in note,
        "never_zero": "never zero" in note,
        "m2_antipodal": "antipodal sign" in note,
        "m3_spatial": "spatial signature" in note,
        "flat_census": "(4,0,4):2256" in compact,
        "zero_psd": "0 psd" in note,
        "sentinel_cells": "sentinel" in note,
        # --- the live discovery ---------------------------------------------
        "corner_quoted": "the psd corner, exactly" in note,
        "corner_struck": "the word \"exactly\" is struck" in note
        or "the word 'exactly' is struck" in note,
        "psd_region_real": "the s_t = 0 psd region is real" in note,
        "uncharacterized": "uncharacterized" in note,
        "eighty_cells": "80 psd" in note,
        "witness_displayed": "diag(1, 1, 1, 1, 0, 0, 0, 0)" in note,
        "recorded_geometry": "recorded-geometry carrier" in note,
        "corner_not_exact": "not exact" in note,
        "repair_not_exact": "48 counterexamples each way" in note,
        "mass_sign_missing": "m > 0" in note,
        "open_question": "open question" in note,
        "block_164": "block 164" in note,
        "b153_echo": "qualifier a" in note,
        "echo_not_derivation": "an echo, not a derivation" in note,
        # --- the demoted duality --------------------------------------------
        "duality_quoted": "dual obstructions" in note,
        "duality_demoted": "demoted" in note,
        "converse_fails": "the converse fails" in note,
        "blinded_equivocates": "equivocates" in note,
        "two_theorems": "two one-directional theorems" in note,
        "never_a_slogan": "never a slogan" in note,
        # --- the selection rule ----------------------------------------------
        "selection_rule": "selection rule" in note,
        "even_sector_blind": "isospectral" in note,
        "corrected_scope": "theta' shares the sector" in note
        or "theta-prime shares the sector" in note,
        # --- discipline and disclosures --------------------------------------
        "checker_credit": "checker" in note,
        "quoted_then_corrected": "quoted then corrected" in note,
        "float_leak": "moduli_from_field" in note,
        "repo_flag": "flagged for the repo" in note,
        "checker_bugs": "three own-bugs" in note or "three own bugs" in note,
        "common_mode": "common-mode" in note,
        "cross_context": "cross-context" in note,
        "not_re_verified": "not re-verified" in note,
        "sample_not_cone_wide": "not a cone-wide" in note,
        "os_no_go": "not an os no-go" in note,
        "curved_os_no_go": "not a curved os no-go" in note,
        "worker_profile": "worker profile" in note,
        "axiom": "no axiom amendment is justified" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": (
            "no toe percentage moves" in note
            or "no toe percentage movement" in note
        ),
        "zero_e2e": (
            "retained-positive end-to-end theory count remains zero" in note
        ),
        "pool_two": "pool-2" in note or "pool 2" in note,
        "n1_n8": all(
            re.search(rf"\bn{index}\b", note) is not None
            for index in range(1, 9)
        ),
        "w1": re.search(r"\bw1\b", note) is not None,
        # Raw substring membership makes the printed fence byte-identical to its
        # note occurrence.
        "n5_verbatim": N5_FENCE in note_text,
        # NEGATIVE key.  A block whose headline is a REFUTED-SUB-CLAIM repair
        # must not be written up as any kind of priority or originality claim;
        # the gate greps the NORMALIZED note, so the banned wording may not
        # appear anywhere, not even inside a prohibition list.
        "no_priority_claim": (
            "first positive" not in note
            and "novel" not in note
            and "unprecedented" not in note
        ),
        # The LaTeX rho guard: a line-wrapped \rho leaves a stray "ho_" at the
        # start of a line and silently mangles a modulus name.
        "rho_guard": "\nho_" not in note_text,
    }


N5_FENCE = 'N5: per_element: THE SITE CLASS EXISTS, IT DESCENDS, AND THE MASS APPEARS IN IT. Of the 64 cover time reflections t -> p_t - t, x -> e_x x + p_x, 32 are SITE (p_t even, a fixed cover slice) and 32 are LINK (p_t odd) -- theta = (-1,7,-1,0), theta-prime = (-1,7,-1,1) and mid = (-1,1,-1,0) are all LINK, and the lane had only ever run the link class. All 64 DESCEND; 24 site reflections are involutions on the 16-site quotient, 16 covariant (e_x = -1, exactly b148.COVARIANT_MOVES) plus 8 non-covariant. THE ANTIPERIODICITY SIGN LAW IS A THEOREM, not a measurement: from psi(t) = s(t) phi(t mod 4) with s(t) = -(-1)^floor(t/4) the descent is (r phi)(a,x) = s(a) s(p_t - a) phi((p_t - a) mod 4, e_x(x - p_x) mod 4), which equals the committed b142.descend on ALL 64 labels, and with p_t = 2c gives quotient slice c self-mapping with +1 and quotient slice c+2 self-mapping with -1 -- two invariant slices with OPPOSITE signs. The grading identity r X_0 r^-1 = (-1)^(p_t+p_x) X_0 holds on all 64.\nper_site: THE MASS APPEARS AND THE FREE OS CALIBRATION IS MET EXACTLY. [r m H_q]_{S,S} is nonzero for 24 of 24 site involutions on a flat carrier, against IDENTICALLY ZERO for theta and theta-prime -- Block 160\'s diagonality theorem reproduced as the control -- because a site reflection maps the fixed slice to itself and so reads the DIAGONAL block of the action. At s_t = 0 the x-trivial site pairing is EXACTLY m diag(nu) + 0_4 on 320 cells (4 reflections x 16 healed edges x 5 shear-free carriers) with s_x kept SYMBOLIC and dropping out identically: the textbook free site-reflection OS form <F, r F> = m |F|^2 on the fixed slice. E2 IS A ONE-LINE THEOREM: the only off-diagonal the cover Hodge writes is the b-term at ((t,x+1),(t+1,x)), so H_q has time displacements {0, +-1} and the mass NEVER reaches time distance 2, on any carrier.\nper_mode: VERDICT SHAPE (b), AT ITS TRUE SCOPE: AT s_t != 0 POSITIVITY FAILS STRUCTURALLY. M1 HYPERBOLIC ANNIHILATION: a site reflection about slice c sends slice c+1 to slice c-1, time distance 2, so the (c+1,c+1) block is mass-free and on flat carriers exactly zero, the form is [[B, C],[C^dagger, 0]] with the WHOLE mass inside B, det C is a rational multiple of s_t^4 in 376 of 384 flat cells, and the signature is (4,0,4) at every mass -- the pairing is SIGNATURE-BLIND to the mass in 384 of 384 flat cells whenever s_t != 0 and is NEVER ZERO there. M2 ANTIPODAL SIGN: the antiperiodic minus puts the same mass into the closed region with both signs, (4,4,4) exactly, 48 of 48. M3 SPATIAL SIGNATURE: every covariant mass block is indefinite. Flat census {(4,0,4): 2256, (2,4,2): 48}; 0 PSD in every sweep at s_t != 0.\nper_block: THE LIVE DISCOVERY, AND IT IS THE CHECKER\'S: THE s_t = 0 PSD REGION IS REAL AND UNCHARACTERIZED. The solve transcript\'s "The PSD corner, exactly: {H_q diagonal} x {s_t = 0} x {e_x = +1, p_x = 0}" is FALSE and the word "exactly" IS STRUCK: the checker found 80 PSD mass-carrying cells of 1152 on cone-admissible carriers whose H_q is NOT diagonal (their carrier set was not disclosed to this runner and that count is NOT re-verified here; this runner\'s own three disclosed non-diagonal carriers recompute 64 PSD of 1152, every one of them on a non-diagonal H_q), and the exact witness reproduces here -- sigma = 1/2 on time slice 3 only with nu = 1, reflection (-1,2,1,0) at fixed slice c = 1, edge (0,0), s_t = 0, m = 1, [r Q]_{S,S} = diag(1, 1, 1, 1, 0, 0, 0, 0) at inertia (4,4,0). That is MASS-CARRYING POSITIVITY ON A RECORDED-GEOMETRY CARRIER. Neither characterization is exact: the transcript\'s global corner fails on the witness, the checker\'s local-shear repair fails 48 counterexamples each way, and the corner also omitted m > 0 -- at m = -1 the same cell is NSD (0,4,4).\nlattice_wide: THE SELECTION RULE AND THE DEMOTED DUALITY. The identity X_0|_S [r Q(m,K)]_{S,S} X_0|_S = (-1)^(p_t+p_x) [r Q(m,-K)]_{S,S} holds with K reversed by NEGATING the edge differential, so in the EVEN sector the pairing is isospectrally blind to the sign of the connection -- but that sector is NOT new: theta-prime has p_t + p_x = 8, EVEN, so it COMMUTES with X_0 and has been run throughout Blocks 156-162. The solve transcript\'s "a sector the lane never had" and its "K-sign blindness no earlier class allowed" are STRUCK; what is genuinely new is the SITE GEOMETRY, not the grading sector. The transcript\'s "dual obstructions" headline is DEMOTED: the converse of Block 160\'s direction FAILS (theta\'s mass pairing is identically zero on a non-diagonal-H_q cone-admissible carrier too) and "blinded" EQUIVOCATES between a pairing that is identically zero and a pairing that is merely signature-blind.\nRESULT: WHAT STANDS IS TWO ONE-DIRECTIONAL THEOREMS AND NEVER A SLOGAN. (i) Block 160: on a diagonal H_q the exchanging pairing of m H_q is identically zero. (ii) M1: for a site pairing at s_t != 0 the mass is annihilated hyperbolically and the signature cannot see it. Neither converse is established and the pair is not a duality. The verdict (b) stands at its true scope on an independent 15360-cell checker sweep against the solve\'s 13440, 0 PSD at s_t != 0 in both, with the flat census reproduced EXACTLY.\nDECISION_CUT: THE SITE CHANNEL IS OPEN AT s_t = 0 AND CLOSED AT s_t != 0. NOTHING is registered, adopted or proposed; no site reflection is adopted; no premise-class change is registered; no landed note is edited; Block 160 is NOT corrected and Block 162 is NOT corrected. THE NAMED NEXT QUESTION: the exact characterization of the s_t = 0 site-class PSD region (Block 164). Block 153\'s qualifier A already flagged the s_t = 0 line as special for theta via the forcing-determinant collapse -- cited as an ECHO and never as a derivation. REMAINING OPEN: block 164; and the pool-2 handoff items (contract E; the cutting residuals; the signed-flux census).\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero.'


# ---------------------------------------------------------------------------
# claims: the only thing a mutation is allowed to touch
# ---------------------------------------------------------------------------
def build_claims(mutation: str) -> dict:
    claims: dict = {
        "main_head": CURRENT_MAIN,
        "parent_pin": "resolved",
        "grading_sector_is_new": False,
        "sign_law": (FIXED_SLICE_SIGN, SWAP_SLICE_SIGN),
        "calibration_cells": CALIBRATION_CELLS,
        "hq_displacements": HQ_DISPLACEMENTS,
        "mass_blind_cells": FLAT_STRUCTURE_CELLS,
        "closed_psd": 0,
        "psd_corner_is_exact": False,
        "local_repair_is_exact": False,
        "selection_rule": True,
        "duality_is_a_theorem_pair": False,
        "required_scope_keys": SCOPE_KEYS,
    }
    if mutation == "stale_main_authority":
        claims["main_head"] = STALE_MAIN
    elif mutation == "stale_parent_authority":
        claims["parent_pin"] = "stale"
    elif mutation == "claim_new_grading_sector":
        # THE STRUCK CLAIM, ASSERTED: the X_0-even sector asserted to be one the
        # lane has never had, which is false the moment theta-prime is read
        claims["grading_sector_is_new"] = True
    elif mutation == "break_sign_law":
        # the antiperiodic MINUS denied: both invariant slices asserted to
        # self-map with +1, i.e. no antipodal sign and no M2
        claims["sign_law"] = (FIXED_SLICE_SIGN, FIXED_SLICE_SIGN)
    elif mutation == "break_calibration":
        # the free OS calibration denied at its measured extent: asserted to
        # hold on the flat carrier only rather than on all five shear-free ones
        claims["calibration_cells"] = EDGE_COUNT * X_TRIVIAL_COUNT
    elif mutation == "break_e2_theorem":
        # E2 denied: the mass asserted to reach time distance 2, which would
        # give the (c+1,c+1) block mass content and dissolve M1
        claims["hq_displacements"] = (0, 1, 2, 3)
    elif mutation == "break_annihilation":
        # M1 denied: the flat pairing asserted to be mass-SENSITIVE in its
        # signature at s_t != 0, i.e. no hyperbolic annihilation
        claims["mass_blind_cells"] = 0
    elif mutation == "claim_antipodal_positive":
        # M2 denied: the closed OS region asserted to contain a positive cell
        claims["closed_psd"] = 1
    elif mutation == "claim_psd_corner_exact":
        # THE REFUTED CORNER, ASSERTED: PSD at s_t = 0 asserted to require a
        # diagonal H_q, which the 80-cell region and its exact witness deny
        claims["psd_corner_is_exact"] = True
    elif mutation == "claim_local_repair_exact":
        # the checker's own local repair asserted to be the boundary, which its
        # own counterexamples in BOTH directions deny
        claims["local_repair_is_exact"] = True
    elif mutation == "break_selection_rule":
        # the X_0 selection rule denied as an identity
        claims["selection_rule"] = False
    elif mutation == "claim_duality_theorem":
        # THE DEMOTED SLOGAN, ASSERTED: the two blockers asserted to be a
        # theorem-pair, which the failing converse denies
        claims["duality_is_a_theorem_pair"] = True
    elif mutation == "claim_st0_characterized":
        # the open question closed by omission: without these keys the note may
        # read as though the s_t = 0 region were characterized
        claims["required_scope_keys"] = tuple(
            key
            for key in SCOPE_KEYS
            if key
            not in (
                "uncharacterized",
                "open_question",
                "block_164",
                "corner_not_exact",
                "repair_not_exact",
            )
        )
    elif mutation == "drop_witness":
        # the discovery's evidence dropped from the note's scope
        claims["required_scope_keys"] = tuple(
            key
            for key in SCOPE_KEYS
            if key not in ("witness_displayed", "eighty_cells",
                           "psd_region_real", "recorded_geometry")
        )
    elif mutation == "drop_n5_fence":
        claims["required_scope_keys"] = tuple(
            key for key in SCOPE_KEYS if key != "n5_verbatim"
        )
    return claims


# ---------------------------------------------------------------------------
# gates: pure functions of the measured facts and the claims
# ---------------------------------------------------------------------------
def evaluate_gates(facts: Facts, claims: dict, elapsed_ns: int) -> dict:
    authority = facts.authority
    parent_blobs_ok = (
        authority.parent_artifact_blobs
        if claims["parent_pin"] == "resolved"
        else authority.stale_parent_artifact_blobs
    )
    gate_a = bool(
        AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_REFLECTION_CHANNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_MASS_SURVIVAL_STRATUM_BOUNDED_THEOREM_NOTE_2026-08-20.md",
            "scripts/admissibility_dirac_kahler_mass_survival_stratum_2026_08_20.py",
        )
        and PARENT_ARTIFACTS == (BLOCK162_NOTE, BLOCK162_RUNNER)
        and len(PARENT_ARTIFACT_BLOBS) == len(PARENT_ARTIFACTS) == 2
        and facts.main_head == claims["main_head"]
        and authority.fixed_authority
        and authority.parent_pin_is_commit
        and authority.parent_ref_and_ancestry
        and parent_blobs_ok
    )

    # the struck sector claim: "new" would require NO landed reflection in the
    # X_0-even sector; theta-prime is in it, so the honest value is False
    sector_is_new = not facts.grading[4]
    gate_b = bool(
        facts.family[0] == COVER_REFLECTIONS
        and facts.family[1] == SITE_REFLECTIONS
        and facts.family[2] == LINK_REFLECTIONS
        and facts.family[3] == COVER_REFLECTIONS
        and facts.family[4] == INVOLUTIVE_COUNT
        and facts.family[5] == (COVARIANT_COUNT, NON_COVARIANT_COUNT)
        and facts.family[6] is True
        and facts.family[7] is True
        and facts.family[8] == ((1, 1),)
        and facts.family[9] == X_TRIVIAL_COUNT
        and facts.signs[0] == facts.signs[1] == INVOLUTIVE_COUNT
        and facts.signs[2] == (INVARIANT_SLICES,)
        and facts.signs[3] == COVER_REFLECTIONS
        and facts.signs[4] == tuple(
            (c, claims["sign_law"][0], claims["sign_law"][1])
            for c in range(PHYS_T)
        )
        and facts.signs[5] is True
        and facts.grading[0] is True
        and facts.grading[1] == (X0_EVEN_SITE, X0_ODD_SITE)
        and facts.grading[2] == (COVARIANT_COUNT, NON_COVARIANT_COUNT)
        and facts.grading[3] is True
        and facts.grading[4] is True
        and facts.grading[5] == (7, THETA_PRIME_PARITY)
        and facts.grading[6] is True
        and facts.grading[7] is True
        and sector_is_new == claims["grading_sector_is_new"]
    )

    gate_c = bool(
        facts.mass[0] is True
        and facts.mass[1] is True
        and facts.mass[2] is True
        and facts.mass[3] == INVOLUTIVE_COUNT
        and facts.mass[4] == MASS_INERTIA_TABLE
        and facts.mass[5] == COVARIANT_COUNT
        and facts.calibration[0] == CALIBRATION_CELLS
        and facts.calibration[1] == claims["calibration_cells"]
        and facts.calibration[2] == SHEAR_FREE_CARRIERS
        and facts.calibration[3] is True
        and facts.calibration[4] is True
        and facts.calibration[5] == {
            (1, CALIBRATION_INERTIA): CALIBRATION_CELLS,
            (-1, CALIBRATION_NSD_INERTIA): CALIBRATION_CELLS,
        }
        and facts.calibration[6] is True
        and facts.calibration[7] is False
        and facts.calibration[8] is True
        and facts.calibration[9] is True
        and facts.calibration[10] is True
        and facts.displacement[0] == COVER_OFF_DIAGONAL
        and facts.displacement[1] == COVER_OFF_DISPLACEMENTS
        and facts.displacement[2] is True
        and facts.displacement[3] == claims["hq_displacements"]
        and facts.displacement[4] == 0
        and facts.displacement[5] == DISTANCE_TWO_ENTRIES
        and facts.displacement[6] is True
        and facts.displacement[7] is True
        and facts.exact_no_float
    )

    gate_d = bool(
        facts.annihilation[0] == FLAT_STRUCTURE_CELLS
        and facts.annihilation[1] == FLAT_STRUCTURE_CELLS
        and facts.annihilation[2] == DET_C_NONZERO
        and facts.annihilation[3] == DET_C_NONZERO
        and facts.annihilation[4] == DET_C_ZERO
        and facts.annihilation[5] == (DET_C_ZERO_EDGE,)
        and facts.annihilation[6] == FLAT_CENSUS
        and facts.annihilation[7] == FLAT_CENSUS_CELLS
        and facts.annihilation[8] == 0
        and facts.annihilation[9] == claims["mass_blind_cells"]
        and facts.annihilation[10] == FLAT_STRUCTURE_CELLS
        and facts.annihilation[11] == FLAT_STRUCTURE_CELLS
        and facts.exact_no_float
    )

    gate_e = bool(
        facts.antipodal[0] == {CLOSED_MASS_INERTIA: CLOSED_MASS_CELLS}
        and facts.antipodal[1] == CLOSED_MASS_CELLS
        and facts.antipodal[2] == claims["closed_psd"]
        and facts.antipodal[3] == CLOSED_CELLS
        and facts.antipodal[4] == CLOSED_CARRIERS
        and facts.antipodal[5] == 0
        and facts.antipodal[6] >= 0
        and sum(facts.antipodal[7].values()) + facts.antipodal[6]
        == CLOSED_CELLS
        and facts.sweep[0] == SWEEP_CELLS
        and facts.sweep[1] == SWEEP_CARRIERS
        and facts.sweep[2] == 0
        and facts.sweep[3] == 0
        and facts.sweep[4][2] > 0
        and facts.sweep[5] is True
        and sum(facts.sweep[6].values()) == SWEEP_CELLS
        and facts.sweep[7] == ((HALF, 0, 0),)
    )

    corner_is_exact = facts.discovery[3] == 0
    repair_is_exact = (
        facts.discovery[4] == 0 and facts.discovery[5] == 0
    )
    gate_f = bool(
        facts.discovery[0] == ST0_CELLS
        and facts.discovery[1] == ST0_CARRIERS
        and facts.discovery[2] == ST0_PSD_CELLS
        and facts.discovery[3] == ST0_PSD_CELLS
        and facts.discovery[4] == LOCAL_SHEARED_PSD
        and facts.discovery[5] == LOCAL_FREE_NOT_PSD
        and facts.discovery[16][0] >= facts.discovery[4]
        and facts.discovery[16][1] >= facts.discovery[5]
        and sum(facts.discovery[6].values()) == ST0_CELLS
        and facts.discovery[7] is True
        and facts.discovery[8] is False
        and facts.discovery[9] == WITNESS_FIXED_SLICE
        and facts.discovery[10] is True
        and facts.discovery[11] == WITNESS_INERTIA
        and facts.discovery[12] == WITNESS_NSD_INERTIA
        and facts.discovery[13] == (sp.Integer(1),) * LX + (sp.Integer(0),) * LX
        and facts.discovery[14] is True
        and facts.discovery[15] is True
        and corner_is_exact == claims["psd_corner_is_exact"]
        and repair_is_exact == claims["local_repair_is_exact"]
        and facts.exact_no_float
    )

    duality_is_a_theorem_pair = not facts.duality[4]
    gate_g = bool(
        facts.selection[0] == claims["selection_rule"]
        and facts.selection[1] == SELECTION_CELLS
        and facts.selection[2] is True
        and facts.selection[3][0] == facts.selection[3][1]
        and facts.selection[3][1] > 0
        and facts.selection[4][1] > 0
        and facts.selection[5] is True
        and facts.duality[0] is True
        and facts.duality[1] is True
        and facts.duality[2] is False
        and facts.duality[3] is True
        and facts.duality[4] is True
        and facts.duality[5] is False
        and facts.duality[6] == FLAT_STRUCTURE_CELLS
        and facts.duality[7] == FLAT_STRUCTURE_CELLS
        and facts.duality[8] == FLAT_STRUCTURE_CELLS
        and duality_is_a_theorem_pair == claims["duality_is_a_theorem_pair"]
    )

    required = tuple(claims["required_scope_keys"])
    gate_h = bool(
        set(facts.scope) == set(required)
        and all(facts.scope.values())
        and len(MUTATIONS) == 15
        and len(set(MUTATIONS)) == 15
        and set(MUTATION_GATE) == set(MUTATIONS)
        and set(MUTATION_GATE.values()) == set("ABCDEFGH")
        and N5_FENCE.count("\n") + 1 <= 10
        and N5_FENCE.count("\n") + 1 >= 8
        and POOL_TWO_LEADS == 3
        and elapsed_ns <= RUNTIME_BUDGET_SEC * 1_000_000_000
    )

    return {
        "A": gate_a,
        "B": gate_b,
        "C": gate_c,
        "D": gate_d,
        "E": gate_e,
        "F": gate_f,
        "G": gate_g,
        "H": gate_h,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument(
        "--deep",
        action="store_true",
        help=(
            "run the two TWICE-VERIFIED sweeps at a STATED SAMPLED SCALE: the "
            "flat hyperbolic census re-read by two independent inertia routes "
            "(the committed Block 144 congruence helper and exact real-root "
            "counting on the characteristic polynomial), and the curved "
            "ATLAS sweep re-read the same way; the sturm route's negative "
            "sentinel is COUNTED and DISCLOSED, never silently dropped"
        ),
    )
    arguments = parser.parse_args()
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
        gate_values = evaluate_gates(
            facts, build_claims(mutation), elapsed_ns
        )
        changed = {
            key for key in raw_gates if raw_gates[key] != gate_values[key]
        }
        if changed - {target} or gate_values[target]:
            raise AssertionError("mutation did not fail exactly its own gate")

    print("MEASURED, before any gate is read:")
    print(
        f"  THE FAMILY: {facts.family[0]} cover time reflections, "
        f"{facts.family[1]} SITE and {facts.family[2]} LINK; all "
        f"{facts.family[3]} descend; {facts.family[4]} site involutions on the "
        f"quotient at (covariant, non-covariant) = {facts.family[5]}, the "
        f"covariant condition being exactly b148's {facts.family[6]}; the LINK "
        f"class has no fixed cover slice {facts.family[7]}; every "
        f"non-involutive site label is an x-translation {facts.family[8]}; "
        f"{facts.family[9]} of them are x-trivial"
    )
    print(
        f"  THE ANTIPERIODICITY SIGN LAW, PROVED: the analytic descent read off "
        f"the lift equals the committed b142.descend on {facts.signs[3]} of "
        f"{facts.family[0]} labels, and the measured law holds on "
        f"{facts.signs[0]} of {facts.signs[1]} involutions with exactly "
        f"{facts.signs[2]} invariant quotient slices each; per fixed slice c "
        f"the analytic signs (c, sigma_c, sigma_(c+2)) are {facts.signs[4]}; "
        f"the fixed-slice spatial action is x -> e_x x + p_x {facts.signs[5]}"
    )
    print(
        f"  THE GRADING: r X_0 r^-1 = (-1)^(p_t+p_x) X_0 on all 64 "
        f"{facts.grading[0]}, splitting the site class {facts.grading[1]} and "
        f"the involutions {facts.grading[2]}; theta ANTIcommutes "
        f"{facts.grading[3]} and THETA-PRIME COMMUTES {facts.grading[4]} at "
        f"(p_t+p_x) = {facts.grading[5]}, both reproduced from the committed "
        f"operators {facts.grading[6]} {facts.grading[7]} -- SO THE X_0-EVEN "
        f"SECTOR IS NOT NEW"
    )
    print(
        f"  THE MASS APPEARS: flat H_q = I {facts.mass[0]}; the controls "
        f"[theta m H_q] {facts.mass[1]} and [theta' m H_q] {facts.mass[2]} are "
        f"identically zero, while the site pairing is nonzero in "
        f"{facts.mass[3]} of {len(INVOLUTIVE_SITE)}; mass-only inertia by "
        f"(e_x, p_x) {facts.mass[4]}, indefinite for {facts.mass[5]} of "
        f"{COVARIANT_COUNT} covariant reflections (M3)"
    )
    print(
        f"  THE CALIBRATION: {facts.calibration[1]} of {facts.calibration[0]} "
        f"cells over {facts.calibration[2]} shear-free carriers are EXACTLY "
        f"m diag(nu) (+) 0_4, diag(nu) being the fixed-slice diagonal of H_q, "
        f"which is diagonal on every shear-free carrier {facts.calibration[9]} "
        f"and LITERALLY m I_4 (+) 0_4 on the flat one {facts.calibration[10]}; "
        f"s_x is symbolic in the action {facts.calibration[3]} and absent from "
        f"the form {facts.calibration[4]}; inertia by mass sign "
        f"{facts.calibration[5]}; all carriers cone-admissible "
        f"{facts.calibration[6]}; DISCLOSED, the landed moduli_from_field is "
        f"float-free on a plain-int carrier {facts.calibration[7]} while this "
        f"runner's carriers are {facts.calibration[8]}"
    )
    print(
        f"  E2, IN ONE LINE: the cover Hodge has {facts.displacement[0]} "
        f"off-diagonal entries, ALL of them b-terms {facts.displacement[2]}, at "
        f"time displacements {facts.displacement[1]}; hence H_q displacements "
        f"{facts.displacement[3]} with {facts.displacement[4]} entries at "
        f"distance 2; the {facts.displacement[5]} distance-2 entries of Q are "
        f"pure K, vanishing at s_t = 0 {facts.displacement[6]} and at zero "
        f"shear {facts.displacement[7]}"
    )
    print(
        f"  M1, THE HYPERBOLIC ANNIHILATION: the (c+1,c+1) block is zero in "
        f"{facts.annihilation[0]} of {facts.annihilation[1]} flat cells; det C "
        f"is nonzero in {facts.annihilation[2]}, a RATIONAL multiple of s_t^4 "
        f"in {facts.annihilation[3]}, and zero in {facts.annihilation[4]} cells "
        f"all on edge {facts.annihilation[5]}; the ATLAS flat census is "
        f"{facts.annihilation[6]} over {facts.annihilation[7]} cells at "
        f"{facts.annihilation[8]} PSD; the signature is MASS-BLIND in "
        f"{facts.annihilation[9]} of {facts.annihilation[1]} cells while the "
        f"pairing is NEVER ZERO in {facts.annihilation[10]}; and at s_t = 0 on "
        f"an unsheared H_q the hyperbolic block is IDENTICALLY ZERO in "
        f"{facts.annihilation[11]}, so M1 is VACUOUS there and the exclusion is "
        f"M3's"
    )
    print(
        f"  M2, THE ANTIPODAL SIGN: closed-region mass-only inertia "
        f"{facts.antipodal[0]} over {facts.antipodal[1]} cells at "
        f"{facts.antipodal[2]} PSD; the full closed census over "
        f"{facts.antipodal[3]} cells on {facts.antipodal[4]} carriers has "
        f"{facts.antipodal[5]} PSD with {facts.antipodal[6]} cells the landed "
        f"inertia helper could not resolve (DISCLOSED, excluded from and never "
        f"counted against the census)"
    )
    print(
        f"  THE SWEEP: {facts.sweep[0]} cells over {facts.sweep[1]} "
        f"cone-admissible carriers {facts.sweep[5]} at "
        f"{facts.sweep[2]} PSD and {facts.sweep[3]} unresolved; most positive "
        f"inertia reached {facts.sweep[4]}; census {facts.sweep[6]}; the cone "
        f"premise H_q[S,S] is uniformly {facts.sweep[7]} and locks NOTHING"
    )
    print(
        f"  THE LIVE DISCOVERY -- THE s_t = 0 PSD REGION: {facts.discovery[2]} "
        f"PSD mass-carrying cells of {facts.discovery[0]} over "
        f"{facts.discovery[1]} carriers, ALL {facts.discovery[3]} of them on "
        f"NON-diagonal H_q; the transcript's global corner therefore FAILS, and "
        f"the local-shear repair fails in BOTH directions ON THE X-TRIVIAL "
        f"REFLECTIONS, where the corner claim lives -- {facts.discovery[4]} PSD "
        f"cells with a locally sheared support and {facts.discovery[5]} non-PSD "
        f"cells with a locally shear-free one, against {facts.discovery[16]} "
        f"over all 24 involutions, where the second figure is dominated by M3; "
        f"census {facts.discovery[6]}"
    )
    print(
        f"  THE EXACT WITNESS: carrier sigma = 1/2 on time slice 3 only with "
        f"nu = 1, cone-admissible {facts.discovery[7]}, H_q diagonal "
        f"{facts.discovery[8]}; reflection {WITNESS_LABEL} at fixed slice "
        f"{facts.discovery[9]}, x-trivial {facts.discovery[15]} and involutive "
        f"{facts.discovery[14]}; edge {WITNESS_EDGE} at s_t = 0; the form is "
        f"m diag(1,1,1,1) (+) 0_4 {facts.discovery[10]} with diagonal "
        f"{facts.discovery[13]}, inertia {facts.discovery[11]} at m = 1 and "
        f"{facts.discovery[12]} at m = -1"
    )
    print(
        f"  THE SELECTION RULE: the identity holds on {facts.selection[1]} "
        f"cells {facts.selection[0]} with K reversed by negating the edge "
        f"differential {facts.selection[2]}; even-sector isospectral agreement "
        f"{facts.selection[3]}, odd-sector agreement {facts.selection[4]} "
        f"(operationally empty here -- (4,0,4) is its own reverse); theta-prime "
        f"sits in the EVEN sector {facts.selection[5]}"
    )
    print(
        f"  THE DUALITY, DEMOTED: forward, a diagonal H_q kills theta's "
        f"{facts.duality[0]} and theta-prime's {facts.duality[1]} mass pairing; "
        f"CONVERSE FAILS -- on a cone-admissible {facts.duality[3]} carrier "
        f"with H_q diagonal {facts.duality[2]}, theta's mass pairing is STILL "
        f"identically zero {facts.duality[4]} while theta-prime's is NOT "
        f"{facts.duality[5]}; and 'blinded' EQUIVOCATES -- the site pairing is "
        f"nonzero in {facts.duality[6]} of {facts.duality[8]} flat cells and "
        f"merely signature-blind in {facts.duality[7]}"
    )
    if facts.deep_flat is not None:
        print(
            f"  --deep flat census, twice verified (sampled, stated): "
            f"{facts.deep_flat} as (cells, agreements, disagreements, "
            f"sturm sentinels)"
        )
    if facts.deep_sweep is not None:
        print(
            f"  --deep curved sweep, twice verified (sampled, stated): "
            f"{facts.deep_sweep} as (cells, agreements, disagreements, "
            f"sturm sentinels, PSD)"
        )
    print()

    checks = Checks()
    checks.check(
        "A-authority",
        "main plus TWO parent artifacts are content-bound: Block 162's note and runner, which are BOTH the stack parent this block's branch is cut from AND the content parent whose import chain (b161 -> b160 -> b159 -> b156 -> b153 -> b148 -> b147 -> b145 -> b142) carries every committed constructor used here and is pinned by Block 162's own gate A rather than duplicated in this one",
        gate_values["A"],
    )
    checks.check(
        "B-the-site-family-the-sign-law-and-the-corrected-grading",
        "THE CLASS THE LANE HAD NEVER RUN IS ENUMERATED, ITS SIGN LAW IS PROVED RATHER THAN MEASURED, AND ITS ADVERTISED NOVELTY IS CORRECTED: of the 64 cover time reflections t -> p_t - t, x -> e_x x + p_x exactly 32 are SITE (p_t even, so a cover slice is fixed) and 32 are LINK (p_t odd, no fixed slice) -- theta, theta-prime and mid are all LINK and the lane had only ever run the link class -- all 64 DESCEND through the antiperiodic quotient, 24 of the site reflections are honest involutions on the 16-site quotient at 16 covariant (e_x = -1, which is exactly b148's COVARIANT_MOVES condition) plus 8 non-covariant, and every site label that is not an involution is an x-translation; THE ANTIPERIODICITY SIGN LAW IS A THEOREM, since the descent derived independently from the committed lift psi(t) = s(t) phi(t mod 4) with s(t) = -(-1)^floor(t/4), namely (r phi)(a,x) = s(a) s(p_t - a) phi((p_t - a) mod 4, e_x(x - p_x) mod 4), agrees with the committed b142.descend on ALL 64 labels and gives, with p_t = 2c, quotient slice c self-mapping with +1 and quotient slice c+2 self-mapping with -1 -- exactly two invariant slices carrying OPPOSITE signs, which is mechanism M2 in advance; and the grading identity r X_0 r^-1 = (-1)^(p_t + p_x) X_0 holds on all 64, splitting the site class 16/16, BUT THE TRANSCRIPT'S 'a sector the lane never had' IS STRUCK because theta-prime = (-1,7,-1,1) has p_t + p_x = 8, EVEN, and therefore COMMUTES with X_0 on the committed operator itself -- the genuinely new element of this block is the SITE GEOMETRY and not the grading sector",
        gate_values["B"],
    )
    checks.check(
        "C-the-mass-appears-the-calibration-is-met-and-E2-is-one-line",
        "THE BLOCK 160 PROTECTION IS GENUINELY ESCAPED AND THE FREE OS CALIBRATION IS MET EXACTLY, FOR THE FIRST TIME AT THIS FIXTURE: on the flat carrier H_q is the identity, the committed half-exchanging controls [theta . m H_q]_{++} and [theta' . m H_q]_{++} are IDENTICALLY ZERO -- Block 160's diagonality theorem reproduced as a control rather than assumed -- and the site pairing [r . m H_q]_{S,S} is NONZERO for 24 of 24 site involutions, because a site reflection carries the fixed slice to itself and therefore reads the DIAGONAL block of the action, which is precisely what the diagonality theorem does not protect; the mass-only inertia is the spatial reflection's own signed permutation, (4,4,0) for the x-trivial (+1,0), (2,4,2) for (+1,2), (3,4,1) for (-1,0) and (-1,2) and (2,4,2) for (-1,1) and (-1,3), so all 16 COVARIANT mass blocks are already indefinite (M3); AND THE CALIBRATION IS EXACT ON 320 CELLS -- 4 x-trivial reflections x 16 healed edges x 5 shear-free carriers with graded, alternating, wild and extreme volumes -- where [r Q]_{S,S} = m diag(nu) (+) 0_4 identically, with s_x present in the action and DROPPING OUT of the form because the on-slice spatial hops are anti-Hermitian in this block, giving the textbook free site-reflection answer <F, r F> = m |F|^2 on the fixed slice; AND E2 IS A ONE-LINE THEOREM rather than a scan, since the only off-diagonal the committed cover Hodge writes is the b-term at ((t,x+1),(t+1,x)) -- all 64 off-diagonal entries are b-terms at time displacement exactly +-1 -- so H_q's time displacements are {0, +-1}, the mass reaches time distance 2 NOWHERE on the 64-modulus family, and the 16 distance-2 entries of Q are pure connection, vanishing both at s_t = 0 and at zero carrier shear; the disclosed landed defect that b145.moduli_from_field returns a Python FLOAT on plain-int carriers is measured here in both directions and this runner's carrier constructor is gated float-free",
        gate_values["C"],
    )
    checks.check(
        "D-M1-the-hyperbolic-annihilation-at-a-live-connection",
        "AT s_t != 0 THE MASS IS ANNIHILATED HYPERBOLICALLY, AND THE FAILURE IS SIGNATURE-BLINDNESS RATHER THAN VANISHING: a site reflection about slice c sends slice c+1 to slice c-1, time distance 2, so by E2 the (c+1,c+1) block of the pairing is mass-free and on flat carriers is EXACTLY ZERO in 384 of 384 cells, leaving the form [[B, C],[C^dagger, 0]] with the ENTIRE mass content inside B; det C is nonzero in 376 of those cells and in every one of them is a RATIONAL multiple of s_t^4 -- computed as a ratio and checked to be free of every symbol, not asserted -- while the 8 vanishing cells all sit on the single healed edge (1,2); whenever C is nonsingular the form is congruent to [[0, C],[C^dagger, 0]] and the signature is (4,0,4) for EVERY mass, so the ATLAS flat census is exactly {(4,0,4): 2256, (2,4,2): 48} over 2304 cells with ZERO PSD, and -- the sharper statement -- the inertia is IDENTICAL across all six masses in 384 of 384 cells while the pairing itself is NEVER the zero matrix in any of them: the mass is PRESENT and SIGNATURE-INVISIBLE; AND THE BOUNDARY IS STATED HONESTLY -- at s_t = 0 on an unsheared H_q the hyperbolic block C is IDENTICALLY ZERO in all 384 cells, so M1 is VACUOUS there and what excludes the covariant reflections at that point is M3, not M1",
        gate_values["D"],
    )
    checks.check(
        "E-M2-the-antipodal-sign-M3-and-the-independent-sweeps",
        "THE ANTIPERIODIC MINUS PUTS THE SAME MASS IN WITH BOTH SIGNS AND NO SWEEP FINDS A POSITIVE AT A LIVE CONNECTION: on the closed OS region {c, c+1, c+2} the two invariant slices carry +m A_x and -m A_x, so the mass-only inertia is (4,4,4) EXACTLY in 48 of 48 cells at m = +-1 with zero PSD, and the full closed-region census over 3 carriers x 24 reflections x 16 edges x 2 masses = 2304 cells finds ZERO PSD, with any cell the landed Block 144 congruence helper cannot resolve counted, reported and EXCLUDED from rather than counted against the census -- the independent checker hit exactly this failure mode on 8 of its own 2304 twelve-row cells and it is disclosed here rather than hidden; and the half-support sweep over 4 cone-admissible carriers x 24 involutions x 16 edges x 3 masses = 4608 cells at the ATLAS shears finds ZERO PSD and zero unresolved cells, with the most positive inertia reached anywhere still carrying negatives, while the cone premise H_q[S,S] is uniformly POSITIVE DEFINITE (8,0,0) on every probed carrier and every site support -- so no Block 156-style sign lock fires: a cone premise constrains B, and B is exactly the block a hyperbolic congruence annihilates",
        gate_values["E"],
    )
    checks.check(
        "F-the-live-discovery-the-uncharacterized-s_t=0-PSD-region",
        "THE SOLVE TRANSCRIPT'S PSD CORNER IS FALSE AND THE REGION IT MISDESCRIBES IS THIS BLOCK'S DISCOVERY: the claim 'The PSD corner, exactly: {H_q diagonal} x {s_t = 0} x {e_x = +1, p_x = 0}' is REFUTED by explicit construction -- over 3 cone-admissible carriers whose H_q is NOT diagonal x 24 involutions x 16 healed edges = 1152 cells at s_t = 0, there are 64 PSD MASS-CARRYING cells and every single one of them sits on a non-diagonal H_q, so the corner's quantifier fails outright; the exact witness is rebuilt entry by entry with no float anywhere -- carrier sigma = 1/2 on time slice 3 only with nu = 1, cone-admissible and non-diagonal, reflection (-1,2,1,0) which is involutive and x-trivial at fixed quotient slice c = 1, healed edge (0,0), s_t = 0 and m = 1, giving [r Q]_{S,S} = diag(1,1,1,1,0,0,0,0) at inertia (4,4,0) -- MASS-CARRYING POSITIVITY ON A CARRIER THAT RECORDS GEOMETRY; the corner also OMITS the mass sign, since the same cell is NSD (0,4,4) at m = -1; and the checker's own proposed local repair, 'shear-free on the support slices c and c+1', is REFUTED IN BOTH DIRECTIONS here too, with PSD cells whose support is locally sheared and non-PSD cells whose support is locally shear-free, so the region's boundary is edge-dependent and NEITHER characterization is exact -- THE EXACT CHARACTERIZATION OF THE s_t = 0 SITE-CLASS PSD REGION IS THIS BLOCK'S NAMED OPEN QUESTION and it is carried forward as Block 164 rather than answered here",
        gate_values["F"],
    )
    checks.check(
        "G-the-selection-rule-and-the-duality-demoted-to-two-theorems",
        "THE X_0 SELECTION RULE IS AN IDENTITY AT A CORRECTED SCOPE AND THE 'DUAL OBSTRUCTIONS' HEADLINE IS DEMOTED TO TWO ONE-DIRECTIONAL THEOREMS: X_0|_S [r Q(m,K)]_{S,S} X_0|_S = (-1)^(p_t+p_x) [r Q(m,-K)]_{S,S} holds on 96 cells with the connection reversed INDEPENDENTLY by negating the committed edge differential -- itself verified to send K to -K while leaving m H_q alone -- so in the EVEN sector the pairing is isospectrally blind to the sign of the connection, but that sector is NOT new to the site class because theta-prime shares it, and the odd-sector consequence is disclosed as operationally empty on this fixture since the generic inertia (4,0,4) is its own reverse; AND THE DUALITY IS NOT A THEOREM-PAIR: the forward direction stands (a diagonal H_q kills the exchanging mass pairing for both theta and theta-prime), but the CONVERSE FAILS on an explicit cone-admissible carrier with a NON-diagonal H_q where theta's mass pairing is STILL identically zero -- while theta-prime's is not, so the 'because' in 'blinded because H_q is diagonal' is unsupported at class level -- and 'blinded' EQUIVOCATES between two different things, the exchanging pairing being literally the ZERO MATRIX against the site pairing being nonzero in all 384 flat cells and merely SIGNATURE-BLIND in all 384; what stands is stated as two one-directional theorems and never as a slogan",
        gate_values["G"],
    )
    checks.check(
        "H-note-scope",
        "the scout discipline stated as a discipline -- every reflection, support and carrier outside the committed four is a registered-premise-class change that is MEASURED and never registered, adopted or proposed -- VERDICT SHAPE (b) carried at its TRUE SCOPE with the mass appearing, the calibration met as m diag(nu) + 0_4, and positivity failing at s_t != 0 by the three named mechanisms, the hyperbolic annihilation written as SIGNATURE-BLIND and NEVER ZERO, the antipodal sign, the spatial signature, the flat census displayed and the zero-PSD sweeps stated with their sentinel disclosure; THE THREE REFUTED SUB-CLAIMS QUOTED THEN CORRECTED -- the grading-sector claim quoted and STRUCK with theta-prime's commutation and Block 153's evenness named and the site geometry identified as what is actually new, the PSD corner quoted with the word 'exactly' STRUCK and the missing m > 0 condition named, and the dual-obstructions headline DEMOTED to two one-directional theorems with the failing converse and the 'blinded' equivocation both spelled out and never a slogan; THE LIVE DISCOVERY DISPLAYED AS THE BLOCK'S OPEN QUESTION -- the s_t = 0 PSD region REAL and UNCHARACTERIZED, the checker's 80 PSD cells credited, the exact witness diag(1, 1, 1, 1, 0, 0, 0, 0) displayed, mass-carrying positivity on a recorded-geometry carrier named, both candidate characterizations recorded as NOT EXACT with the 48 counterexamples each way, the exact characterization named as BLOCK 164, and Block 153's qualifier A cited as an ECHO AND NOT A DERIVATION; together with the selection rule at its corrected scope, checker credit, the b145.moduli_from_field float leak flagged for the repo, the checker's three own-bugs disclosed, common-mode and cross-context disclosure, the not-re-verified list, sample scope, the pool-2 items, N1 through N8, the W1 wall, the exact N5 fence, the worker profile, the LaTeX rho guard, and NO priority or originality wording anywhere in the note, not even inside a prohibition list",
        gate_values["H"],
    )
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
