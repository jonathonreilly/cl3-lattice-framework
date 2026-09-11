#!/usr/bin/env python3
# Final path: scripts/admissibility_dirac_kahler_mass_survival_stratum_2026_08_20.py
"""Block 162: THE MASS-SURVIVAL STRATUM.

SCOUT DISCIPLINE, AND IT IS A HARD BOUNDARY.  Every support restriction, every
reweighting, every reflection outside the committed four and every half carrier
outside the committed four exercised here is a REGISTERED-PREMISE-CLASS CHANGE
to the committed framework.  Each one is MEASURED and NONE of them is
registered, adopted, proposed or claimed.  Nothing in this runner edits, retires
or amends any committed note, axiom, premise or convention.

THE HEADLINE IS A LAYERED EQUIVALENCE, AND IT CLOSES A CLASS.  On the free
64-modulus family the deletion-restricted theta pairing is diag(G) on the four
even-x slots, with an IDENTICALLY ZERO odd-odd block and NO shear modulus
anywhere in the even-even block; its ENTIRE cross-parity content is eight
entries, four at m^0 and four at m^1; and supp(dF/dm) is EXACTLY those four m^1
entries.  Hence

  F mass-independent          <=>  L147 alone                  (codimension 4)
  F PSD at m = 0              <=>  the even-shear balance alone (codimension 4)
  F PSD at ANY SINGLE m != 0  <=>  both                         (codimension 8)

so THE MASS-SURVIVAL CONDITION IS THE CROSS-PARITY VANISHING CONDITION and the
positivity is QUOTIENT POSITIVITY BY CONSTRUCTION.  Nothing escapes the
decoupling at any scope measured here, and the deletion REMOVES an indefinite
full-rank object rather than exposing a positive one.

THE STRATUM-WIDE PSD THEOREM IS PROVED AND NEVER SAMPLED: every committed edge
is c(i,j) Q^T G Q with ONE shared G whose 5G is a diagonal of four
unit-coefficient sums of strictly positive cone moduli, so the edge census is
6 PSD / 6 NSD / 4 identically zero / ZERO indefinite at every mass and at every
point of the stratum.

THE BLOCK 161 ADJUDICATION.  Block 161's codimension-8 sentence names the
32-coordinate cone (the mass-survival set proper, dimension 24) and its
dimension-2 sentence names the 8-dimensional odd-moment space.  Those are
DIFFERENT AMBIENT SPACES and both statements are correct, so NO
CORRECTION-IN-SUCCESSOR is warranted and none is made.  One Block 161 DISPLAY
SLIP is disclosed: its "4 free odd-shear directions plus all 16 volumes"
enumerated 20 of that locus's 24 free directions.

THREE TRANSCRIPT CORRECTIONS FROM THE INDEPENDENT CHECKER, EACH QUOTED THEN
CORRECTED.  (D1) the carrier-move sweep is 32 profiles over 16 CARRIER
translations x FLIP, and the cover's 32 shifts descend to 16 distinct carrier
profiles.  (D2) theta-prime's DEAD blocks are (1,3) and (4,6); (5,7) is
live-live and identically zero there.  (D3) "no curved stratum point makes it
PSD" is FALSE and is STRUCK, on an explicit cone-admissible curved on-stratum
counterexample; the correct qualifier is FLAT ODD-TIME ROWS, not a flat carrier.
Two vacuous proof routes are replaced: the dimensions are computed BY RANK, and
the FLIP-alone invariance is proved over the whole stratum with the carrier's
shears negated BEFORE the pairing is formed.

NO HARDCODED CERTIFICATE ANYWHERE: every printed numeral is recomputed in the
measurement pass from the committed constructors reached through the LANDED
Block 161 validation battery, and no check is registered as a literal True.
Exact SymPy throughout; no float enters any measured object, which is itself
gated; the integer monotonic clock is used only for the runtime gate.

PROVENANCE DISCLOSURE: the four-chart shear atlas, the local differential, the
64-modulus carrier model and its admissible cone, the cover Hodge, the
antiperiodic quotient, the sixteen healed edge differentials and their healing
weights, the half pairing, the committed theta and theta-prime, the reflection
move machinery, the Block 156 involution pairs and locus dimensions, and the
Block 144 symmetric-congruence inertia helper are ALL COMMITTED objects,
imported through the Block 161 runner (b161 -> b160 -> b159 -> b158 -> b156 ->
b155/b154/b153/b148/b147/b145/b144/b142/b137/b134/b105) and never re-derived.
External lattice-gauge, staggered-fermion and Osterwalder-Schrader literature is
REFERENCED nowhere and BORROWED nowhere; every statement is re-proved
in-framework.

HYPOTHESES, named and not imported.  (H1) the pairing convention is [X Q]_{++}
on a half carrier of the cover.  (H3) "positive" is a statement about the
Hermitian part.  (H4) the physical cone is nu > 0, |sigma| < 1 per cell.
(H1-160) a pairing is exchange-compatible when the reflection carries the half
onto its complement.  (H1-162) a "characterization" verdict is a statement about
THIS object -- the committed link deletion of a committed healed edge to the
eight even-x temporal crossing hops, over the committed sixteen healed edges --
and about no wider class of objects.
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

import admissibility_dirac_kahler_validation_battery_2026_08_20 as b161

b160 = b161.b160
b159 = b161.b159
b156 = b161.b156
b148 = b161.b148
b147 = b161.b147
b145 = b161.b145
b144 = b161.b144

MASS = b161.MASS


NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_MASS_SURVIVAL_STRATUM_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE SINGLE-PARENT PIN.  Block 161 (the validation battery) is BOTH the stack
# parent -- this block's branch is cut from it -- AND the content parent: every
# committed constructor used here is reached through the Block 161 runner's own
# import chain (b160 -> b159 -> b158 -> b156 -> b155/b154/b153/b148/b147/b145/
# b144/b142/b137/b134/b105), which Block 161's own gate A pins and this block
# does not duplicate.  So there are exactly TWO artifact pins here.
BLOCK161_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_VALIDATION_BATTERY_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
BLOCK161_RUNNER = (
    "scripts/admissibility_dirac_kahler_validation_battery_2026_08_20.py"
)

PARENT_ARTIFACTS = (BLOCK161_NOTE, BLOCK161_RUNNER)
# PLACEHOLDER BLOBS for the Block 161 pair, single-line hex literals; the
# landing supervisor refreshes exactly these two lines by anchored sed against
# the Block 161 branch tip.  Until they are refreshed gate A FAILS, which is the
# intended state of an unlanded draft.
PARENT_ARTIFACT_BLOBS = (
    "0038501b74b8da150b82a6f1fc6518805148e49e",   # Block 161 note
    "6e063fd5d331c36e94e6e6f6cdc67931eb16b543",   # Block 161 runner
)

# Deliberately literal: this is the complete audit read surface.  Every entry is
# a WORKTREE-READABLE path at landing time; the cache envelope stats these, so an
# origin/main-only path here would break the audit (the Block 130 lesson,
# re-learned at the Block 150 landing and inherited through Blocks 151-161).
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_MASS_SURVIVAL_STRATUM_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_VALIDATION_BATTERY_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/admissibility_dirac_kahler_validation_battery_2026_08_20.py",
)

AUDIT_TIMEOUT_SEC = 600
# Authority pins, single-line hex literals refreshed by anchored sed at landing.
CURRENT_MAIN = "005f047923055e6ecd5dc8bce1ffd71765c2ffd8"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
# This block stacks on Block 161, so the parent branch is Block 161's.
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block161-validation-battery-20260820"
)
# The Block 161 branch tip, VERIFIED to be an ancestor of HEAD and to carry both
# pinned artifact paths.  The two BLOB lines above are the placeholders.
PARENT_COMMIT = "8e2784039267e20fce1941e3796d34c5efa0d470"
# Block 160's tip: a real ancestor of HEAD that PREDATES BOTH pinned parent
# artifacts.  VERIFIED before pinning with `git rev-parse <commit>:<path>`,
# which FAILS for the Block 161 note AND the Block 161 runner at this commit, so
# resolving the parent pin here leaves BOTH pinned blobs ABSENT.  This pin is
# read ONLY under the stale mutation; the baseline gate never requires it.
STALE_PARENT_COMMIT = "91cad4272b0727d1af828069a89d8ca7a79cd9c9"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_escape_exists",
    "break_layered_iff",
    "break_shared_g",
    "claim_edge_indefinite",
    "claim_l154_active",
    "break_recording_rule",
    "claim_orientation_recorded",
    "claim_flattenable",
    "break_stabilizer",
    "claim_seam_positive",
    "claim_corrects_161",
    "drop_site_reflection_lead",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_escape_exists": "B",
    "break_layered_iff": "B",
    "break_shared_g": "C",
    "claim_edge_indefinite": "C",
    "claim_l154_active": "D",
    "break_recording_rule": "E",
    "claim_orientation_recorded": "E",
    "claim_flattenable": "E",
    "break_stabilizer": "F",
    "claim_seam_positive": "G",
    "claim_corrects_161": "H",
    "drop_site_reflection_lead": "H",
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
    return b161.no_float(value)


def congruence_inertia(matrix: sp.MatrixBase) -> tuple[int, int, int]:
    """Exact (n_positive, n_zero, n_negative) WITH multiplicity, by congruence.

    Delegated to the COMMITTED Block 144 helper through the Block 161/160/159/
    158/156 import chain, so the tool this block reasons with is exactly the blob
    Block 161's gate A pins.  Called on EXACT algebraic matrices only.
    """
    return b161.congruence_inertia(matrix)


def sturm_inertia(matrix: sp.MatrixBase) -> tuple[int, int, int]:
    """The SECOND, INDEPENDENT inertia route, used only under --deep.

    Exact real-root counting on the characteristic polynomial, delegated to the
    Block 161 helper.  It shares no code path with the committed congruence
    helper, so an agreement between the two is a genuine cross-check.
    """
    return b161.sturm_inertia(matrix)


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
# the committed model, imported wholesale through Block 161
# ---------------------------------------------------------------------------
HALF = b161.HALF                          # 8
PHYS = b161.PHYS                          # 16
LX = b161.LX                              # 4
COVER_T = b161.COVER_T                    # 8
EDGE_KEYS = b161.EDGE_KEYS
EVEN_SLOTS = b161.EVEN_SLOTS              # (0, 2, 4, 6)
ODD_SLOTS = b161.ODD_SLOTS                # (1, 3, 5, 7)
LIVE = b161.LIVE                          # (0, 2, 5, 7)
EVEN_CELLS = b161.EVEN_CELLS              # (0,0) (0,2) (2,0) (2,2)
QUOTIENT_PROJECTION = b161.QUOTIENT_PROJECTION

NU, A, B, INV = (
    b145.NU_MODULUS, b145.A_MODULUS, b145.B_MODULUS, b145.INV_MODULUS
)
CELLS = tuple((t, x) for t in range(4) for x in range(LX))
ODD_CELLS = tuple((t, x) for t in (1, 3) for x in range(LX))
EVEN_TIME_ODD_X = ((0, 1), (0, 3), (2, 1), (2, 3))

U, V = sp.symbols("u v", real=True)
P1, Q1, P3, Q3 = sp.symbols("p1 q1 p3 q3", real=True)
SIGMA_S, NU_S = sp.symbols("sigma_chart nu_chart", real=True)


# ---------------------------------------------------------------------------
# the certificate constants this runner is claiming
# ---------------------------------------------------------------------------
EDGE_COUNT = 16
PSD_EDGES = b161.PSD_EDGES
PSD_EDGE_COUNT = 6
NSD_EDGE_COUNT = 6
EMPTY_EDGE_COUNT = 4
INDEFINITE_EDGE_COUNT = 0
PRIMARY_EDGE = (2, 2)
PSD_INERTIA = (4, 4, 0)
NSD_INERTIA = (0, 4, 4)
DEAD_INERTIA = (0, 8, 0)
ODD_X_INERTIA = (2, 4, 2)
FULL_CROSSING_INERTIA = (6, 0, 2)
MASSIVE_CURVED_INERTIA = (4, 0, 4)
FULL_HOP_CENSUS = {(6, 0, 2): 6, (2, 0, 6): 6, (4, 0, 4): 4}
ORBIT_CENSUS = b161.ORBIT_CENSUS
STABILIZER_ORDER = 8
STABILIZER_SHIFTS = b161.STABILIZER_SHIFTS
STRATUM_CARRIER_STABILIZER = ((0, 0), (0, 2), (2, 0), (2, 2))
TRANSLATION_GROUP = 32
CARRIER_TRANSLATIONS = 16
MOVE_PROFILES = 32
COVER_DESCENT = 16
FLATTENING_MOVES = 0
CONE_COORDINATES = 32
CROSS_PARITY_ENTRIES = 8
MASS_CROSS_ENTRIES = 4
M0_CROSS = ((0, 7), (1, 4), (2, 5), (3, 6))
M1_CROSS = ((0, 3), (1, 2), (4, 5), (6, 7))
FULL_HOP_CROSS = ((0, 5), (1, 6), (2, 7), (3, 4))
# the m^0 cross entries ARE the even-shear balance coordinates, in the order the
# support enumeration returns them; the m^1 cross entries ARE L147's equations.
M0_MODULI = (B[(2, 0)], B[(0, 0)], B[(2, 2)], B[(0, 2)])
M1_MODULI = (
    B[(3, 0)] + B[(3, 3)], B[(3, 1)] + B[(3, 2)],
    -B[(1, 0)] - B[(1, 3)], -B[(1, 1)] - B[(1, 2)],
)
# the contrast carriers' measured inertias: the even-shear balance ALONE is PSD
# at m = 0 and loses two directions at m != 0; L147 ALONE (balance violated)
# already fails at m = 0.
BALANCE_ONLY_MASSIVE_INERTIA = (4, 2, 2)
L147_ONLY_MASSLESS_INERTIA = (4, 3, 1)
BALANCE_RANK = 4
L147_RANK = 4
L154_RANK = 2
SURVIVAL_RANK = 8
STRATUM_RANK = 10
SURVIVAL_DIMENSION = 24
STRATUM_DIMENSION = 22
SLICE_CODIMENSION = 2
IFF_CODIMENSIONS = (4, 4, 8)
KLEIN_ORDER = 4
KLEIN_CHARACTER = (1, 1, -1, -1)
JOINT_CHARACTER_DIMENSION = 1
ODD_MOMENTS = 8
GENERIC_MOMENT_U = R(-3, 8)
GENERIC_MOMENT_V = R(-1, 4)
GENERIC_DIAGONALS = (R(1279, 1344), R(299, 288), R(643, 576), R(239, 240))
SEAM_STRATUM_RANK = 0
SEAM_STRATUM_INERTIA = (0, 8, 0)
THETA_PRIME_DEAD_BLOCKS = ((1, 3), (4, 6))
THETA_PRIME_LIVE_LIVE_PAIR = (5, 7)
THETA_PRIME_GENERIC_INERTIA = (2, 4, 2)
THETA_PRIME_LIVE_INERTIA = (2, 0, 2)
THETA_PRIME_HALF_DEAD_INERTIA = (1, 6, 1)
SEAM_COEFFICIENT_RANK = 4
POOL_TWO_LEADS = 3

RUNTIME_BUDGET_SEC = 150


# ---------------------------------------------------------------------------
# constructions.  Everything below is built from the committed primitives.
# ---------------------------------------------------------------------------
def sym(matrix: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix(HALF, HALF, lambda i, j: sp.expand(matrix[i, j]))


def substitute(matrix: sp.MatrixBase, rule: dict) -> sp.Matrix:
    return sp.Matrix(HALF, HALF, lambda i, j: sp.expand(
        sp.sympify(matrix[i, j]).xreplace(rule)
    ))


def upper_support(matrix: sp.MatrixBase) -> tuple:
    return tuple(
        (i, j)
        for i in range(HALF) for j in range(HALF)
        if i < j and sp.expand(matrix[i, j]) != 0
    )


def diagonal_support(matrix: sp.MatrixBase) -> tuple:
    return tuple(j for j in range(HALF) if sp.expand(matrix[j, j]) != 0)


def cross_parity(matrix: sp.MatrixBase) -> tuple:
    """Upper entries joining an even-x slot to an odd-x slot."""
    return tuple(
        (i, j)
        for i, j in upper_support(matrix)
        if (i in EVEN_SLOTS) != (j in EVEN_SLOTS)
    )


def same_parity(matrix: sp.MatrixBase, slots) -> tuple:
    return tuple(
        (i, j)
        for i, j in upper_support(matrix)
        if i in slots and j in slots
    )


def locus_rows_on_cells(cells) -> sp.Matrix:
    """Rows e_cell = 0 on the ordered 16 shear-moment coordinates."""
    rows = []
    for cell in cells:
        row = [sp.Integer(0)] * len(CELLS)
        row[CELLS.index(cell)] = sp.Integer(1)
        rows.append(row)
    return sp.Matrix(rows)


def pair_rows_on_cells(pairs) -> sp.Matrix:
    """Rows b_p + b_q = 0 on the ordered 16 shear-moment coordinates."""
    rows = []
    for left, right in pairs:
        row = [sp.Integer(0)] * len(CELLS)
        row[CELLS.index(left)] += sp.Integer(1)
        row[CELLS.index(right)] += sp.Integer(1)
        rows.append(row)
    return sp.Matrix(rows)


R_PAIRS = tuple(
    ((t, x), (t, (3 - x) % LX)) for t in (1, 3) for x in range(LX)
)
S_ODD_X_PAIRS = tuple(((t, 1), (t, 3)) for t in (1, 3))

BALANCE_ROWS = locus_rows_on_cells(EVEN_CELLS)
L147_ROWS = pair_rows_on_cells(R_PAIRS)
L154_ROWS = pair_rows_on_cells(S_ODD_X_PAIRS)

# the STRATUM substitution: even-shear balance + L147 cap L154 on the odd rows,
# with the four even-time odd-x shears left FREE.
STRATUM_B = {cell: sp.Integer(0) for cell in EVEN_CELLS}
STRATUM_B.update(
    {(1, 0): U, (1, 1): U, (1, 2): -U, (1, 3): -U,
     (3, 0): V, (3, 1): V, (3, 2): -V, (3, 3): -V}
)
STRATUM = {B[cell]: value for cell, value in STRATUM_B.items()}

# L147 + the even-shear balance alone: Block 161's codimension-8 mass-survival
# set, with the four L154-violating odd-moment freedoms p1, q1, p3, q3 explicit.
SURVIVAL_B = {cell: sp.Integer(0) for cell in EVEN_CELLS}
SURVIVAL_B.update(
    {(1, 0): P1, (1, 1): Q1, (1, 2): -Q1, (1, 3): -P1,
     (3, 0): P3, (3, 1): Q3, (3, 2): -Q3, (3, 3): -P3}
)
SURVIVAL = {B[cell]: value for cell, value in SURVIVAL_B.items()}

# the even-shear balance ALONE (L147 free), and L147 ALONE (balance free)
BALANCE_ONLY = {B[cell]: sp.Integer(0) for cell in EVEN_CELLS}
L147_ONLY = {
    B[left]: -B[right] for left, right in (((1, 0), (1, 3)), ((1, 1), (1, 2)),
                                           ((3, 0), (3, 3)), ((3, 1), (3, 2)))
}

A_CHART = NU_S / (1 - SIGMA_S ** 2)
B_CHART = -NU_S * SIGMA_S / (1 - SIGMA_S ** 2)

# the exact-rational generic cone-admissible stratum point
GENERIC_SIGMA = {
    (0, 0): sp.Integer(0), (0, 2): sp.Integer(0),
    (2, 0): sp.Integer(0), (2, 2): sp.Integer(0),
    (0, 1): R(1, 7), (0, 3): R(-2, 7), (2, 1): R(3, 7), (2, 3): R(-1, 6),
    (1, 0): R(1, 3), (1, 1): R(1, 2), (1, 2): R(-1, 5), (1, 3): R(-2, 5),
    (3, 0): R(1, 4), (3, 1): R(1, 2), (3, 2): R(-1, 6), (3, 3): R(-3, 7),
}
GENERIC_NU = {
    (0, 0): R(7, 4), (0, 1): R(5, 3), (0, 2): R(5, 6), (0, 3): R(9, 7),
    (2, 0): R(11, 7), (2, 1): R(4, 3), (2, 2): R(13, 9), (2, 3): R(7, 5),
    (1, 0): sp.Integer(1), (1, 1): R(9, 16), (1, 2): R(9, 5), (1, 3): R(63, 80),
    (3, 0): R(15, 16), (3, 1): R(3, 8), (3, 2): R(35, 24), (3, 3): R(10, 21),
}
GENERIC = {cell: (GENERIC_SIGMA[cell], GENERIC_NU[cell]) for cell in CELLS}

# the checker's CURVED on-stratum counterexample for defect D3: cone-admissible,
# on the stratum with u = v = 0, and genuinely curved.
CURVED_DEAD_ROWS = b161.field_of({(0, 1): R(1, 3), (2, 3): R(-1, 4)},
                                 {(2, 3): R(3, 2)})

# a contrast carrier that keeps the even-shear balance and VIOLATES L147
BALANCE_NOT_L147 = b161.field_of({(1, 0): R(1, 3), (3, 1): R(1, 4)})
# a contrast carrier that satisfies L147 and VIOLATES the even-shear balance
L147_NOT_BALANCE = b161.field_of(
    {(0, 0): R(1, 5), (1, 0): R(1, 3), (1, 3): R(-1, 3)}
)


def deleted(key):
    return b161.restrict(EDGE[key], b161.EVEN_SUPPORT)


def odd_deleted(key):
    return b161.restrict(EDGE[key], b161.ODD_SUPPORT)


DIFFERENTIALS, STAR = b145.connection(b161.SHEAR_X, b161.SHEAR_T)
EDGE_SYMBOLIC = b145.edge_differentials(
    DIFFERENTIALS, STAR, b161.HEALING_WEIGHTS
)
EDGE = {
    key: sp.expand(EDGE_SYMBOLIC[key].xreplace(b161.ATLAS))
    for key in EDGE_KEYS
}
FREE_COVER = b145.cover_hodge_general(NU, A, B, INV)
FLAT_COVER = b145.cover_hodge_from_field(b159.flat_field())


def stratum_cover(sign: int) -> sp.Matrix:
    """The cover Hodge of the GENERAL stratum carrier, shears optionally negated.

    Free positive nu and a, the locked odd rows +-u and +-v, and the four free
    even-time odd-x shears -- the whole stratum, not a point.  `sign = -1`
    negates every shear moment BEFORE the cover Hodge is assembled, so the FLIP
    comparison is between two genuinely different carriers.
    """
    moments = {}
    for cell in CELLS:
        if cell in STRATUM_B:
            moments[cell] = sign * STRATUM_B[cell]
        else:
            moments[cell] = sign * B[cell]
    return b145.cover_hodge_general(NU, A, moments, INV)


# ---------------------------------------------------------------------------
# measured facts (computed once, before any mutation flag is consulted)
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Facts:
    main_head: str
    authority: AuthorityCertificate
    # B: the complete support and the layered equivalence
    calibration: tuple
    support: tuple
    layers: tuple
    # C: the stratum-wide PSD theorem
    factorization: tuple
    census: tuple
    # D: the extent, the chart, the Klein structure, L154's inertness
    extent: tuple
    algebra: tuple
    # E: the recording rule, the curvature, FLIP
    recording: tuple
    curvature: tuple
    flip: tuple
    # F: stability
    stability: tuple
    # G: the seam
    seam: tuple
    # deep sweeps
    deep_full_hop: object
    deep_moves: object
    # H / global
    exact_no_float: bool
    scope: dict


def measure(deep: bool) -> Facts:
    main_head = git_output("rev-parse", "origin/main")
    authority = authority_certificate(main_head)
    exact: list = []

    # ---------------------------------------------------------------- B ----
    witness_cover = b145.cover_hodge_from_field(b161.BALANCED)
    witness = b161.symbolic_pairing(deleted(PRIMARY_EDGE), witness_cover, MASS)
    generic_cover = b145.cover_hodge_from_field(GENERIC)
    calibration = (
        (b156.L147_DIM, b156.L154_DIM, b156.MEET_DIM),
        sp.expand(sp.diff(witness, MASS)) == sp.zeros(HALF, HALF),
        witness.xreplace({MASS: 0}) == sp.diag(
            *[R(33, 40) if j in EVEN_SLOTS else 0 for j in range(HALF)]
        ),
        b145.in_admissible_cone(GENERIC),
        tuple(
            b145.moduli_from_field(GENERIC)[2][cell] for cell in ODD_CELLS
        ),
        tuple(
            sp.Integer(b145.moduli_from_field(GENERIC)[2][cell] == 0)
            for cell in EVEN_CELLS
        ),
        len({b145.moduli_from_field(GENERIC)[1][cell] for cell in CELLS}),
        len({b145.moduli_from_field(GENERIC)[2][cell]
             for cell in EVEN_TIME_ODD_X}),
    )
    exact.append(sum(witness))

    cone_form = b161.symbolic_pairing(deleted(PRIMARY_EDGE), FREE_COVER, MASS)
    cone_form = sym(cone_form)
    mass_derivative = sym(sp.diff(cone_form, MASS))
    cross = cross_parity(cone_form)
    mass_zero = cone_form.xreplace({MASS: 0})
    mass_one = sym(cone_form.xreplace({MASS: 1}))
    even_even = same_parity(cone_form, EVEN_SLOTS)
    odd_odd_entries = tuple(
        (i, j)
        for i in ODD_SLOTS for j in ODD_SLOTS
        if sp.expand(cone_form[i, j]) != 0
    )
    even_even_shears = set()
    for i in EVEN_SLOTS:
        for j in EVEN_SLOTS:
            even_even_shears |= (
                sp.expand(cone_form[i, j]).free_symbols & set(B.values())
            )
    zero_mass_cross = tuple(
        (i, j) for i, j in cross if sp.expand(mass_zero[i, j]) != 0
    )
    mass_cross = tuple(upper_support(mass_derivative))
    support = (
        cross,
        len(cross),
        zero_mass_cross,
        mass_cross,
        len(mass_cross),
        odd_odd_entries,
        even_even,
        tuple(sorted(str(s) for s in even_even_shears)),
        tuple(diagonal_support(cone_form)),
        tuple(sp.expand(cone_form[i, j] * 10) for i, j in zero_mass_cross),
        tuple(
            sp.expand(mass_derivative[i, j] * 8) for i, j in mass_cross
        ),
    )
    exact.append(sum(cone_form[i, j] for i, j in cross))

    # the three layers, each a RANK and not a hand-written list
    balance_rank = BALANCE_ROWS.rank()
    l147_rank = L147_ROWS.rank()
    l154_rank = L154_ROWS.rank()
    survival_rank = sp.Matrix.vstack(BALANCE_ROWS, L147_ROWS).rank()
    stratum_rank = sp.Matrix.vstack(
        BALANCE_ROWS, L147_ROWS, L154_ROWS
    ).rank()
    balance_only_form = substitute(cone_form, BALANCE_ONLY)
    l147_only_form = substitute(cone_form, L147_ONLY)
    balance_cover = b145.cover_hodge_from_field(BALANCE_NOT_L147)
    l147_cover = b145.cover_hodge_from_field(L147_NOT_BALANCE)
    layers = (
        (balance_rank, l147_rank, l154_rank),
        (survival_rank, stratum_rank),
        # mass-independence needs L147 alone
        sym(sp.diff(substitute(cone_form, L147_ONLY), MASS))
        == sp.zeros(HALF, HALF),
        sym(sp.diff(substitute(cone_form, BALANCE_ONLY), MASS))
        != sp.zeros(HALF, HALF),
        # every odd-slot diagonal is identically zero, so ONE surviving cross
        # entry gives a strictly negative 2x2 minor
        tuple(sp.expand(cone_form[j, j]) for j in ODD_SLOTS),
        cross_parity(balance_only_form),
        cross_parity(l147_only_form),
        # measured: balance alone is PSD at m = 0 and INDEFINITE at m = 1
        congruence_inertia(
            b161.pairing_of(deleted(PRIMARY_EDGE), balance_cover, sp.Integer(0))
        ),
        congruence_inertia(
            b161.pairing_of(deleted(PRIMARY_EDGE), balance_cover, sp.Integer(1))
        ),
        # measured: L147 alone (balance violated) is NOT PSD, even at m = 0
        congruence_inertia(
            b161.pairing_of(deleted(PRIMARY_EDGE), l147_cover, sp.Integer(0))
        ),
        b145.in_admissible_cone(BALANCE_NOT_L147),
        b145.in_admissible_cone(L147_NOT_BALANCE),
    )

    # ---------------------------------------------------------------- C ----
    stratum_form = substitute(cone_form, STRATUM)
    shared_g = sp.diag(*[stratum_form[j, j] for j in EVEN_SLOTS])
    pullback = QUOTIENT_PROJECTION.T * shared_g * QUOTIENT_PROJECTION
    scalars = {}
    identity_holds = True
    stratum_forms = {}
    for key in EDGE_KEYS:
        form = substitute(
            sym(b161.symbolic_pairing(deleted(key), FREE_COVER, MASS)), STRATUM
        )
        stratum_forms[key] = form
        if form == sp.zeros(HALF, HALF):
            scalars[key] = sp.Integer(0)
        else:
            scalars[key] = sp.nsimplify(
                sp.cancel(form[0, 0] / stratum_form[0, 0])
            )
        identity_holds = identity_holds and sp.expand(
            form - scalars[key] * pullback
        ) == sp.zeros(HALF, HALF)
    diagonal_shape = []
    for j in EVEN_SLOTS:
        entry = sp.expand(stratum_form[j, j] * 5)
        names = tuple(sorted(str(s) for s in entry.free_symbols))
        unit = all(sp.expand(sp.diff(entry, s)) == 1 for s in entry.free_symbols)
        positive = entry.free_symbols <= (
            set(NU.values()) | set(A.values()) | set(INV.values())
        )
        diagonal_shape.append((names, len(names), unit, positive))
    factorization = (
        identity_holds,
        tuple(sorted(str(s) for s in shared_g.free_symbols)),
        tuple(diagonal_shape),
        sp.expand(stratum_form - pullback) == sp.zeros(HALF, HALF),
        tuple(sp.expand(stratum_form[j, j]) for j in ODD_SLOTS),
        tuple(scalars[key] for key in EDGE_KEYS),
        all(
            sym(sp.diff(stratum_forms[key], MASS)) == sp.zeros(HALF, HALF)
            for key in EDGE_KEYS
        ),
    )
    exact.append(sum(shared_g))

    inertia_rows = []
    for key in EDGE_KEYS:
        row = []
        for mass in (sp.Integer(0), sp.Integer(1)):
            row.append(
                congruence_inertia(
                    b161.pairing_of(deleted(key), generic_cover, mass)
                )
            )
        inertia_rows.append((key, tuple(row)))
    census_counter = collections.Counter(row[1][1] for row in inertia_rows)
    psd_keys = tuple(sorted(k for k, sig in inertia_rows if sig[1] == PSD_INERTIA))
    indefinite = sum(
        1 for _k, sig in inertia_rows if sig[1][0] > 0 and sig[1][2] > 0
    )
    full_hop_counter = collections.Counter(
        congruence_inertia(
            b161.pairing_of(EDGE[key], generic_cover, sp.Integer(1))
        )
        for key in EDGE_KEYS
    )
    full_form = substitute(
        sym(b161.symbolic_pairing(EDGE[PRIMARY_EDGE], FREE_COVER, MASS)),
        STRATUM,
    )
    odd_form = substitute(
        sym(b161.symbolic_pairing(odd_deleted(PRIMARY_EDGE), FREE_COVER, MASS)),
        STRATUM,
    )
    census = (
        tuple(sig for _k, sig in inertia_rows),
        dict(census_counter),
        psd_keys,
        indefinite,
        all(sig[0] == sig[1] for _k, sig in inertia_rows),
        dict(full_hop_counter),
        cross_parity(full_form),
        tuple(sp.expand(full_form[j, j]) for j in ODD_SLOTS),
        tuple(
            sp.expand(-10 * full_form[i, j]).free_symbols
            <= (set(NU.values()) | set(A.values()) | set(INV.values()))
            for i, j in ((1, 3), (5, 7))
        ),
        tuple(
            congruence_inertia(
                b161.pairing_of(EDGE[key], generic_cover, sp.Integer(1))
            )
            for key in EDGE_KEYS if scalars[key] == 0
        ),
        tuple(sp.expand(odd_form[j, j]) for j in range(HALF)),
        congruence_inertia(
            b161.pairing_of(odd_deleted(PRIMARY_EDGE), generic_cover,
                            sp.Integer(0))
        ),
        congruence_inertia(
            b161.pairing_of(odd_deleted(PRIMARY_EDGE), FLAT_COVER,
                            sp.Integer(0))
        ),
    )

    # ---------------------------------------------------------------- D ----
    survival_form = substitute(cone_form, SURVIVAL)
    survival_symbols = set()
    for key in EDGE_KEYS:
        form = substitute(
            sym(b161.symbolic_pairing(deleted(key), FREE_COVER, MASS)), SURVIVAL
        )
        for entry in form:
            survival_symbols |= sp.expand(entry).free_symbols
    extent = (
        (balance_rank, l147_rank, l154_rank, survival_rank, stratum_rank),
        (
            CONE_COORDINATES - survival_rank,
            CONE_COORDINATES - stratum_rank,
            stratum_rank - survival_rank,
        ),
        sp.simplify((A_CHART ** 2 - B_CHART ** 2) / A_CHART - NU_S) == 0,
        sp.simplify(-B_CHART / A_CHART - SIGMA_S) == 0,
        sp.simplify(A_CHART ** 2 - A_CHART * NU_S - B_CHART ** 2) == 0,
        sp.simplify(
            (A_CHART ** 2 - B_CHART ** 2) / A_CHART
            / (1 - (-B_CHART / A_CHART) ** 2)
            - A_CHART
        ) == 0,
        sp.expand(survival_form - pullback) == sp.zeros(HALF, HALF),
        tuple(sorted(str(s) for s in survival_symbols & {P1, Q1, P3, Q3})),
        tuple(sorted(str(s) for s in survival_symbols & set(B.values()))),
    )

    r_perm = sp.Matrix(LX, LX, lambda i, j: 1 if j == (3 - i) % LX else 0)
    s_perm = sp.Matrix(LX, LX, lambda i, j: 1 if j == (i + 2) % LX else 0)
    orbit_of_zero = set()
    for element in (sp.eye(LX), r_perm, s_perm, r_perm * s_perm):
        orbit_of_zero.add(
            tuple(element[0, c] for c in range(LX)).index(1)
        )
    joint = sp.Matrix.vstack(r_perm + sp.eye(LX), s_perm + sp.eye(LX))
    characters = tuple(
        tuple(int(v) for v in vec)
        for vec in (
            sp.Matrix([1, 1, 1, 1]), sp.Matrix([1, -1, 1, -1]),
            sp.Matrix([1, 1, -1, -1]), sp.Matrix([1, -1, -1, 1]),
        )
        if r_perm * vec == -vec and s_perm * vec == -vec
    )
    algebra = (
        r_perm ** 2 == sp.eye(LX) and s_perm ** 2 == sp.eye(LX),
        r_perm * s_perm == s_perm * r_perm,
        all(r_perm[i, i] == 0 and s_perm[i, i] == 0 for i in range(LX)),
        len({
            tuple(element)
            for element in (sp.eye(LX), r_perm, s_perm, r_perm * s_perm)
        }),
        len(orbit_of_zero),
        LX - joint.rank(),
        characters,
    )

    # ---------------------------------------------------------------- E ----
    generic_moments = b145.moduli_from_field(GENERIC)[2]
    recording = (
        tuple(GENERIC_SIGMA[cell] for cell in EVEN_CELLS),
        tuple(generic_moments[cell] for cell in EVEN_CELLS),
        sp.solve(sp.Eq(B_CHART, 0), SIGMA_S),
        tuple(GENERIC_SIGMA[cell] for cell in EVEN_TIME_ODD_X),
        len({generic_moments[cell] for cell in EVEN_TIME_ODD_X}),
        tuple(sum(generic_moments[(t, x)] for x in range(LX)) for t in (1, 3)),
        tuple(len({abs(generic_moments[(t, x)]) for x in range(LX)})
              for t in (1, 3)),
        all(
            generic_moments[(t, x)] + generic_moments[(t, (3 - x) % LX)] == 0
            and generic_moments[(t, x)] + generic_moments[(t, (x + 2) % LX)] == 0
            for t in (1, 3) for x in range(LX)
        ),
        tuple(GENERIC_SIGMA[(1, x)] for x in range(LX)),
        tuple(generic_moments[(1, x)] for x in range(LX)),
        (generic_moments[(1, 0)], generic_moments[(3, 0)]),
        len({abs(GENERIC_SIGMA[(1, x)]) for x in range(LX)}),
    )

    profiles = []
    for pt in range(4):
        for px in range(LX):
            moved = b161.transport_field(GENERIC, (1, pt, 1, px))
            moments = b145.moduli_from_field(moved)[2]
            for sign in (1, -1):
                profiles.append(
                    tuple(sign * moments[cell] for cell in CELLS)
                )
    flat_profiles = sum(
        1 for profile in profiles if all(value == 0 for value in profile)
    )
    constant_rows = sum(
        1
        for profile in profiles
        for t in (1, 3)
        if len({profile[CELLS.index((t, x))] for x in range(LX)}) == 1
    )
    curvature = (
        len(profiles),
        len(set(profiles)),
        flat_profiles,
        constant_rows,
        4 * LX,
        generic_moments[(1, 0)] != generic_moments[(1, 2)],
        not generic_cover.is_diagonal(),
        b145.quotient(generic_cover) != sp.eye(PHYS),
        tuple(sorted(str(s) for s in (
            sp.expand(full_form[0, 0]).free_symbols & {U, V}
        ))),
        tuple(sorted(str(s) for s in (
            sp.expand(full_form[4, 4]).free_symbols & {U, V}
        ))),
        tuple(sorted(str(s) for s in (
            sp.expand(stratum_form[0, 0]).free_symbols & {U, V}
        ))),
        tuple(
            sp.expand(sp.diff(full_form[j, j] * 20, symbol))
            for j, symbol in ((0, V), (2, V), (4, U), (6, U))
        ),
    )

    # the WHOLE-STRATUM FLIP proof: the shears are negated in the CARRIER, so
    # the two cover Hodges genuinely differ, and the pairings are compared with
    # the mass left alone.
    cover_plus = stratum_cover(1)
    cover_minus = stratum_cover(-1)
    form_plus = sym(
        b161.symbolic_pairing(deleted(PRIMARY_EDGE), cover_plus, MASS)
    )
    form_minus = sym(
        b161.symbolic_pairing(deleted(PRIMARY_EDGE), cover_minus, MASS)
    )
    joint_flip = sym(
        substitute(cone_form, {s: -s for s in B.values()}).xreplace(
            {MASS: -MASS}
        )
    )
    joint_difference = upper_support(sym(joint_flip - cone_form))
    flip = (
        cover_plus != cover_minus,
        sp.expand(form_plus - form_minus) == sp.zeros(HALF, HALF),
        sym(sp.diff(form_plus, MASS)) == sp.zeros(HALF, HALF),
        tuple(sorted(str(s) for s in set().union(*[
            sp.expand(entry).free_symbols for entry in form_plus
        ]) & set(B.values()))),
        sp.simplify(A_CHART.xreplace({SIGMA_S: -SIGMA_S}) - A_CHART) == 0,
        sp.simplify(B_CHART.xreplace({SIGMA_S: -SIGMA_S}) + B_CHART) == 0,
        joint_difference,
        tuple(sp.expand((joint_flip - cone_form)[i, j] * 5)
              for i, j in joint_difference),
    )
    exact.append(sum(form_plus))

    # ---------------------------------------------------------------- F ----
    orbit_counter = collections.Counter()
    orbit_rows = []
    for pt in range(COVER_T):
        for px in range(LX):
            move = b148.move_matrix(b148.move_permutation((1, pt, 1, px)))
            moved = b161.pairing_of(
                sp.expand(move * deleted(PRIMARY_EDGE) * move.T),
                sp.expand(move * generic_cover * move.T),
            )
            signature = congruence_inertia(moved)
            orbit_counter[signature] += 1
            orbit_rows.append(((pt, px), signature, b161.zero(moved)))
    stabilizer = tuple(
        sorted(s for s, sig, dead in orbit_rows
               if sig == PSD_INERTIA and not dead)
    )
    stabilizer_set = set(stabilizer)
    carrier_stabilizer = []
    for pt in range(4):
        for px in range(LX):
            moments = b145.moduli_from_field(
                b161.transport_field(GENERIC, (1, pt, 1, px))
            )[2]
            if (
                all(moments[cell] == 0 for cell in EVEN_CELLS)
                and all(
                    moments[(t, x)] + moments[(t, (3 - x) % LX)] == 0
                    and moments[(t, x)] + moments[(t, (x + 2) % LX)] == 0
                    for t in (1, 3) for x in range(LX)
                )
            ):
                carrier_stabilizer.append((pt, px))

    weights = sp.symbols("lam0 lam1 lam2 lam3", real=True)
    symbolic_edges = b145.edge_differentials(DIFFERENTIALS, STAR, weights)
    shear_t = b161.SHEAR_T
    base = (sp.Integer(0), sp.Integer(0), shear_t, -shear_t)
    reference = A[(2, 0)] + A[(3, 3)] + INV[(2, 3)] + NU[(3, 0)]
    law = []
    law_symbols = set()
    for (i, j) in EDGE_KEYS:
        form = substitute(
            sym(
                b161.symbolic_pairing(
                    b161.restrict(
                        sp.expand(symbolic_edges[(i, j)]), b161.EVEN_SUPPORT
                    ),
                    FREE_COVER, MASS,
                )
            ),
            STRATUM,
        )
        for entry in form:
            law_symbols |= sp.expand(entry).free_symbols
        coefficient = sp.cancel(form[0, 0] * 5 / reference)
        predicted = 5 * (base[i] - shear_t * (weights[j] - weights[i])) / 4
        law.append(sp.simplify(coefficient - predicted) == 0)
    committed_scalars = tuple(
        sp.nsimplify(scalars[key] / scalars[PRIMARY_EDGE]) for key in EDGE_KEYS
    )
    generic_diagonals = tuple(
        sp.nsimplify(
            sp.expand(stratum_form[j, j] * 5).xreplace({
                **{A[c]: b145.moduli_from_field(GENERIC)[1][c] for c in CELLS},
                **{NU[c]: b145.moduli_from_field(GENERIC)[0][c] for c in CELLS},
                **{INV[c]: b145.moduli_from_field(GENERIC)[3][c] for c in CELLS},
            }) / 4
        )
        for j in EVEN_SLOTS
    )
    stability = (
        len(orbit_rows),
        dict(orbit_counter),
        stabilizer,
        len(stabilizer),
        all(
            ((a[0] + b[0]) % COVER_T, (a[1] + b[1]) % LX) in stabilizer_set
            for a in stabilizer for b in stabilizer
        ),
        all(((-a[0]) % COVER_T, (-a[1]) % LX) in stabilizer_set
            for a in stabilizer),
        (0, 0) in stabilizer_set,
        tuple(sorted(carrier_stabilizer)),
        all(law),
        len(law),
        b161.SHEAR_X in law_symbols,
        b161.SHEAR_T in law_symbols,
        committed_scalars,
        sum(1 for key in EDGE_KEYS if scalars[key] > 0),
        sum(1 for key in EDGE_KEYS if scalars[key] < 0),
        generic_diagonals,
        len(set(generic_diagonals)),
    )

    # ---------------------------------------------------------------- G ----
    theta_gram = sym(
        b161.clean(
            b161.half_pairing(
                b161.THETA, b145.quotient(FREE_COVER), b161.COMMITTED_ROWS
            )
        )
    )
    prime_gram = sym(
        b161.clean(
            b161.half_pairing(
                b161.THETA_PRIME_OP, b145.quotient(FREE_COVER),
                b161.COMMITTED_ROWS,
            )
        )
    )
    theta_rows = []
    for i, j in upper_support(theta_gram):
        row = [sp.Integer(0)] * len(CELLS)
        entry = sp.expand(theta_gram[i, j] * 8)
        for cell in CELLS:
            row[CELLS.index(cell)] = sp.expand(sp.diff(entry, B[cell]))
        theta_rows.append(row)
    theta_matrix = sp.Matrix(theta_rows)
    theta_stratum = substitute(theta_gram, STRATUM)
    prime_stratum = substitute(prime_gram, STRATUM)
    curved_cover = b145.cover_hodge_from_field(CURVED_DEAD_ROWS)
    curved_moments = b145.moduli_from_field(CURVED_DEAD_ROWS)[2]
    curved_prime = b161.clean(
        b161.half_pairing(
            b161.THETA_PRIME_OP, b145.quotient(curved_cover),
            b161.COMMITTED_ROWS,
        )
    )
    curved_theta = b161.clean(
        b161.half_pairing(
            b161.THETA, b145.quotient(curved_cover), b161.COMMITTED_ROWS
        )
    )
    generic_prime = b161.clean(
        b161.half_pairing(
            b161.THETA_PRIME_OP, b145.quotient(generic_cover),
            b161.COMMITTED_ROWS,
        )
    )
    live_diagonal = tuple(sp.expand(prime_stratum[k, k] * 4) for k in LIVE)
    seam = (
        upper_support(theta_gram),
        theta_matrix.rank(),
        theta_stratum.rank(),
        congruence_inertia(theta_stratum),
        substitute(theta_gram, SURVIVAL) == sp.zeros(HALF, HALF),
        upper_support(prime_gram),
        tuple(
            (i, j) for i, j in upper_support(prime_gram)
            if i not in LIVE and j not in LIVE
        ),
        sp.expand(prime_gram[THETA_PRIME_LIVE_LIVE_PAIR[0],
                              THETA_PRIME_LIVE_LIVE_PAIR[1]]),
        live_diagonal,
        sp.expand(sum(live_diagonal)),
        # the "only" in "PSD only at u = v = 0": the live diagonal is a +- pair
        (live_diagonal[0] + live_diagonal[1],
         live_diagonal[2] + live_diagonal[3]),
        tuple(sp.expand(prime_stratum[j, j]) for j in range(HALF)
              if j not in LIVE),
        congruence_inertia(generic_prime),
        congruence_inertia(b161.sub_block(generic_prime, LIVE, LIVE)),
        b161.zero(
            b161.clean(
                b161.half_pairing(
                    b161.THETA, b145.quotient(generic_cover),
                    b161.COMMITTED_ROWS,
                )
            )
        ),
        congruence_inertia(
            sp.diag(*[
                sp.expand(prime_stratum[j, j].xreplace(
                    {U: R(1, 3), V: sp.Integer(0)}
                ))
                for j in range(HALF)
            ])
        ),
        congruence_inertia(
            sp.diag(*[
                sp.expand(prime_stratum[j, j].xreplace(
                    {U: sp.Integer(0), V: sp.Integer(0)}
                ))
                for j in range(HALF)
            ])
        ),
        # DEFECT D3: a CURVED on-stratum point where theta-prime's seam Gram is
        # identically zero -- vacuously PSD, so "no curved stratum point makes
        # it PSD" is FALSE.
        b145.in_admissible_cone(CURVED_DEAD_ROWS),
        tuple(sp.Integer(curved_moments[cell] == 0) for cell in EVEN_CELLS),
        tuple(sp.expand(curved_moments[cell]) for cell in ODD_CELLS),
        not curved_cover.is_diagonal(),
        b145.quotient(curved_cover) != sp.eye(PHYS),
        b161.zero(curved_prime),
        b161.zero(curved_theta),
        congruence_inertia(
            b161.pairing_of(deleted(PRIMARY_EDGE), curved_cover, sp.Integer(1))
        ),
        sum(1 for cell in CELLS if curved_moments[cell] != 0),
    )
    exact.append(sum(prime_stratum))

    # ------------------------------------------------------------- deep ----
    deep_full_hop = None
    deep_moves = None
    if deep:
        agreements = []
        for key in EDGE_KEYS:
            pairing = b161.pairing_of(
                EDGE[key], generic_cover, sp.Integer(1)
            )
            agreements.append(
                congruence_inertia(pairing) == sturm_inertia(pairing)
            )
        deep_census = collections.Counter(
            sturm_inertia(
                b161.pairing_of(EDGE[key], generic_cover, sp.Integer(1))
            )
            for key in EDGE_KEYS
        )
        deep_full_hop = (
            all(agreements), len(agreements), dict(deep_census)
        )
        cover_profiles = []
        for pt in range(COVER_T):
            for px in range(LX):
                moments = b145.moduli_from_field(
                    b161.transport_field(GENERIC, (1, pt, 1, px))
                )[2]
                cover_profiles.append(tuple(moments[cell] for cell in CELLS))
        carrier_profiles = []
        for pt in range(4):
            for px in range(LX):
                moments = b145.moduli_from_field(
                    b161.transport_field(GENERIC, (1, pt, 1, px))
                )[2]
                carrier_profiles.append(tuple(moments[cell] for cell in CELLS))
        deep_moves = (
            len(cover_profiles),
            len(set(cover_profiles)),
            len(carrier_profiles),
            len(set(carrier_profiles)),
            set(cover_profiles) == set(carrier_profiles),
        )

    pool = [
        cone_form, stratum_form, full_form, odd_form, theta_gram, prime_gram,
        prime_stratum, generic_cover, witness, form_plus, shared_g,
    ]
    exact_no_float = bool(
        all(no_float(entry) for matrix in pool for entry in matrix)
        and all(no_float(value) for cell in CELLS for value in GENERIC[cell])
        and all(no_float(scalars[key]) for key in EDGE_KEYS)
        and all(no_float(value) for value in generic_diagonals)
        and all(no_float(value) for value in exact)
    )

    return Facts(
        main_head=main_head,
        authority=authority,
        calibration=calibration,
        support=support,
        layers=layers,
        factorization=factorization,
        census=census,
        extent=extent,
        algebra=algebra,
        recording=recording,
        curvature=curvature,
        flip=flip,
        stability=stability,
        seam=seam,
        deep_full_hop=deep_full_hop,
        deep_moves=deep_moves,
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
    # --- the layered equivalence ------------------------------------------
    "layered_equivalence",
    "mass_independence_iff",
    "psd_zero_mass_iff",
    "psd_any_mass_iff",
    "codim_four",
    "codim_eight",
    "dfdm_support",
    "odd_odd_zero",
    "even_even_no_shear",
    "cross_parity_condition",
    "quotient_by_construction",
    "nothing_escapes",
    "deletion_removes_indefinite",
    "full_hop_census",
    # --- the stratum-wide PSD theorem --------------------------------------
    "shared_g",
    "unit_coefficient",
    "never_sampled",
    "edge_census",
    "computed_not_asserted",
    "rational_chart",
    "open_extent",
    "dimensions_by_rank",
    # --- the two-object bookkeeping and the 161 adjudication ----------------
    "dim_twenty_four",
    "dim_twenty_two",
    "different_ambient",
    "b161_accurate",
    "no_successor_correction",
    "display_slip",
    "enumerated_twenty",
    "l154_inert",
    # --- the algebra --------------------------------------------------------
    "klein",
    "regular_representation",
    "unique_character",
    "free_involutions",
    # --- the recording rule -------------------------------------------------
    "recording_rule",
    "forced_flat",
    "domain_wall",
    "zero_spatial_mean",
    "genuinely_curved",
    "curvature_deleted",
    "move_sweep_count",
    "cover_descent",
    "flip_alone",
    "sigma_squared",
    "no_orientation",
    "balance_alone",
    # --- stability ----------------------------------------------------------
    "stabilizer_order_eight",
    "stratum_own_stabilizer",
    "t6_law",
    "sx_absent",
    "four_diagonals",
    # --- the seam -----------------------------------------------------------
    "seam_moment_locus",
    "annihilation_not_positivity",
    "lock_fires_untouched",
    "dead_blocks",
    "live_live",
    "curved_counterexample",
    "flat_odd_rows",
    # --- the verdict --------------------------------------------------------
    "class_understood",
    "no_connection_route",
    "site_reflection_lead",
    "pool_two",
    # --- discipline and disclosures ----------------------------------------
    "vacuous_replaced",
    "checker_credit",
    "quoted_then_corrected",
    "common_mode",
    "cross_context",
    "not_re_verified",
    "sample_not_cone_wide",
    "os_no_go",
    "curved_os_no_go",
    "axiom",
    "zero_retirement",
    "zero_score",
    "zero_e2e",
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
        # --- the layered equivalence ------------------------------------------
        "layered_equivalence": "layered equivalence" in note,
        "mass_independence_iff": "mass-independence <=> l147" in note,
        "psd_zero_mass_iff": "psd at m = 0 <=> the even-shear balance" in note,
        "psd_any_mass_iff": "psd at any single m != 0 <=> both" in note,
        "codim_four": "codimension 4" in note,
        "codim_eight": "codimension 8" in note,
        "dfdm_support": "supp(df/dm)" in note,
        "odd_odd_zero": "odd-odd block is identically zero" in note,
        "even_even_no_shear": "no shear modulus" in note,
        "cross_parity_condition": "the cross-parity vanishing condition" in note,
        "quotient_by_construction": "quotient positivity by construction" in note,
        "nothing_escapes": "nothing escapes" in note,
        "deletion_removes_indefinite": "removes an indefinite" in note,
        "full_hop_census": "(6,0,2):6" in compact,
        # --- the stratum-wide PSD theorem --------------------------------------
        "shared_g": "one shared" in note,
        "unit_coefficient": "unit-coefficient" in note
        or "unit coefficients" in note,
        "never_sampled": "never sampled" in note,
        "edge_census": "zero indefinite" in note,
        "computed_not_asserted": "computed rather than asserted" in note,
        "rational_chart": "(a^2-b^2)/a" in note,
        "open_extent": "22-dimensional" in note,
        "dimensions_by_rank": "by rank" in note,
        # --- the two-object bookkeeping and the 161 adjudication ----------------
        "dim_twenty_four": "dimension 24" in note,
        "dim_twenty_two": "dimension 22" in note,
        "different_ambient": "different ambient spaces" in note,
        "b161_accurate": "block 161 was accurate" in note,
        "no_successor_correction": "no correction-in-successor" in note,
        "display_slip": "display slip" in note,
        "enumerated_twenty": "enumerated 20" in note,
        "l154_inert": "completely inert" in note,
        # --- the algebra --------------------------------------------------------
        "klein": "klein" in note,
        "regular_representation": "regular representation" in note
        or "regular z2 x z2 representation" in note,
        "unique_character": "unique joint" in note,
        "free_involutions": "free involutions" in note,
        # --- the recording rule -------------------------------------------------
        "recording_rule": "staggered recording rule" in note,
        "forced_flat": "forced flat" in note,
        "domain_wall": "domain wall" in note,
        "zero_spatial_mean": "zero spatial mean" in note,
        "genuinely_curved": "genuinely curved" in note,
        "curvature_deleted": "deleted, not absent" in note,
        "move_sweep_count": "16 carrier translations" in note,
        "cover_descent": "descend to 16 distinct" in note
        or "descending to 16 distinct" in note,
        "flip_alone": "flip alone" in note,
        "sigma_squared": "sigma^2" in note,
        "no_orientation": "records no orientation" in note,
        "balance_alone": "even-shear balance alone" in note,
        # --- stability ----------------------------------------------------------
        "stabilizer_order_eight": "order-8" in note,
        "stratum_own_stabilizer": (
            "the stratum's own translation stabilizer" in note
        ),
        "t6_law": "base(i) - s_t" in note,
        "sx_absent": "never appears" in note,
        "four_diagonals": "1279/1344" in note,
        # --- the seam -----------------------------------------------------------
        "seam_moment_locus": (
            "moment-locus where theta's seam gram vanishes" in note
        ),
        "annihilation_not_positivity": "annihilation, not by positivity" in note
        or "annihilation, not positivity" in note,
        "lock_fires_untouched": "fires untouched" in note,
        "dead_blocks": "(1,3)and(4,6)" in compact,
        "live_live": "live-live" in note,
        "curved_counterexample": "sigma_(0,1) = 1/3" in note,
        "flat_odd_rows": "flat odd-time rows" in note,
        # --- the verdict --------------------------------------------------------
        "class_understood": "completely understood" in note,
        "no_connection_route": (
            "no route to a connection-carrying positive structure" in note
        ),
        "site_reflection_lead": "site-reflection" in note,
        "pool_two": "pool-2" in note or "pool 2" in note,
        # --- discipline and disclosures ----------------------------------------
        "vacuous_replaced": "vacuous" in note,
        "checker_credit": "checker" in note,
        "quoted_then_corrected": "quoted then corrected" in note,
        "common_mode": "common-mode" in note,
        "cross_context": "cross-context" in note,
        "not_re_verified": "not re-verified" in note,
        "sample_not_cone_wide": "not a cone-wide" in note,
        "os_no_go": "not an os no-go" in note,
        "curved_os_no_go": "not a curved os no-go" in note,
        "axiom": "no axiom amendment is justified" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": (
            "no toe percentage moves" in note
            or "no toe percentage movement" in note
        ),
        "zero_e2e": (
            "retained-positive end-to-end theory count remains zero" in note
        ),
        "n1_n8": all(
            re.search(rf"\bn{index}\b", note) is not None
            for index in range(1, 9)
        ),
        "w1": re.search(r"\bw1\b", note) is not None,
        # Raw substring membership makes the printed fence byte-identical to its
        # note occurrence.
        "n5_verbatim": N5_FENCE in note_text,
        # NEGATIVE key.  A block whose headline closes a class must not be
        # written up as any kind of priority or originality claim; the gate greps
        # the NORMALIZED note, so the banned wording may not appear anywhere, not
        # even inside a prohibition list.
        "no_priority_claim": (
            "first positive" not in note
            and "novel" not in note
            and "unprecedented" not in note
        ),
        # The LaTeX rho guard: a line-wrapped \rho leaves a stray "ho_" at the
        # start of a line and silently mangles a modulus name.
        "rho_guard": "\nho_" not in note_text,
    }


N5_FENCE = 'N5: per_element: THE LAYERED EQUIVALENCE IS THE CHARACTERIZATION. On the free 64-modulus family the deletion-restricted theta pairing is diag(G) on the four even-x slots with an IDENTICALLY ZERO odd-odd block and NO shear modulus anywhere in the even-even block; its ENTIRE cross-parity content is eight entries -- (0,7) = b_20/10, (1,4) = b_00/10, (2,5) = b_22/10, (3,6) = b_02/10 at m^0 and (0,3) = m(b_30+b_33)/8, (1,2) = m(b_31+b_32)/8, (4,5) = -m(b_10+b_13)/8, (6,7) = -m(b_11+b_12)/8 at m^1 -- and supp(dF/dm) is EXACTLY those four m^1 entries. So: F mass-independent <=> L147 alone (codimension 4); F PSD at m = 0 <=> the even-shear balance alone (codimension 4); F PSD at ANY SINGLE m != 0 <=> both (codimension 8), which is also PSD at every m. THE m^1 HALF OF THE CROSS-PARITY BLOCK IS L147, SO THE MASS-SURVIVAL CONDITION IS THE CROSS-PARITY VANISHING CONDITION: positivity there is QUOTIENT POSITIVITY BY CONSTRUCTION, NOTHING ESCAPES the decoupling at any scope measured, and the deletion REMOVES AN INDEFINITE full-rank object -- full-hop census {(6,0,2): 6, (2,0,6): 6, (4,0,4): 4}, not one of the sixteen PSD.\nper_site: THE STRATUM-WIDE PSD THEOREM, PROVED AND NEVER SAMPLED. Every committed edge is c(i,j) Q^T G Q with ONE SHARED G, verified as a full 8x8 identity on 16 of 16 edges, and 5G = diag(a_20+a_33+m_23+n_30, a_22+a_31+m_21+n_32, a_00+a_13+m_03+n_10, a_02+a_11+m_01+n_12) -- four UNIT-COEFFICIENT sums of strictly positive cone moduli -- so the inertia is forced at every stratum point and every mass. Edge census 6 PSD / 6 NSD / 4 identically zero / ZERO indefinite, the six PSD edges Block 161\'s six exactly, the inertias COMPUTED and not asserted. The exact rational chart nu = (a^2-b^2)/a, sigma = -b/a inverts the committed modulus map in both directions and makes the stratum linear: an OPEN subset of a 22-dimensional subspace of the 32-coordinate cone.\nper_mode: THE TWO-OBJECT BOOKKEEPING, AND BLOCK 161 WAS ACCURATE. By rank: the even-shear balance is rank 4, L147 is rank 4, L154\'s odd-x rows are rank 2; the MASS-SURVIVAL SET PROPER is balance + L147 at rank 8, DIMENSION 24 in the 32-coordinate cone, and the L147 cap L154 slice is rank 10, DIMENSION 22 -- a codimension-2 cut of it. Block 156\'s dimension-2 meet is a statement in the 8-DIMENSIONAL ODD-MOMENT SPACE. These are DIFFERENT AMBIENT SPACES and Block 161 stated both correctly, so NO CORRECTION-IN-SUCCESSOR is warranted and none is made; one Block 161 DISPLAY SLIP is disclosed, its "4 free odd-shear directions plus all 16 volumes" having ENUMERATED 20 of the locus\'s 24 directions by omitting the four even-time odd-x shears. L154 is COMPLETELY INERT for the theta pairing: none of the sixteen edge forms sees its violating freedoms.\nper_block: THE ALGEBRA AND THE RECORDING RULE. R : x -> 3-x and S : x -> x+2 are commuting FREE INVOLUTIONS acting simply transitively, so the spatial 4-space IS THE REGULAR Z2 x Z2 REPRESENTATION and (1,1,-1,-1) is the UNIQUE JOINT (-,-) character, by rank. The physics is a STAGGERED RECORDING RULE: even-time slices FORCE the even-x cells FLAT and free the odd-x ones; odd-time slices carry rigid +-u two-cell DOMAIN WALLS of ZERO SPATIAL MEAN, antisymmetric under both R and S, with the constraint on the MOMENTS and not on sigma (generic t = 1: sigma = (1/3, 1/2, -1/5, -2/5) against b = (-3/8, -3/8, 3/8, 3/8)). The carriers are GENUINELY CURVED and no committed move flattens them -- 32 profiles over 16 CARRIER TRANSLATIONS x FLIP, the cover\'s 32 shifts DESCENDING TO 16 DISTINCT profiles (the solve transcript\'s "64 profiles over 32 translations" is CORRECTED).\nlattice_wide: THE CURVATURE IS DELETED, NOT ABSENT, AND THE FORM RECORDS NO ORIENTATION. The full-hop diagonal on the stratum is (4a+4a+4m+4n +- 3v)/20 on the live pair and (... +- 3u)/20 on the dead pair -- the recorded shear LINEARLY -- while the deletion-restricted PSD object is (a+a+m+n)/5 with u and v ABSENT. THE FLIP STRENGTHENING: on the stratum F is invariant under FLIP ALONE, the mass NOT reversed, seeing sigma^2 only, proved symbolically over the WHOLE stratum with the carrier\'s shears negated BEFORE the pairing is formed (the solve\'s symbolic conjunct was VACUOUS and is replaced). Block 161\'s joint identity F(flip(c), -m) = F(c, m) is a consequence of THE EVEN-SHEAR BALANCE ALONE: the difference is nonzero at exactly the four m^0 entries, at -b_20/5, -b_00/5, -b_22/5, -b_02/5. STABILITY: the ORDER-8 stabilizer persists at the general element AND is the stratum\'s own translation stabilizer; the T6 law 4c(i,j) = base(i) - s_t (lambda_j - lambda_i) holds symbolically on all 16 edges; s_x NEVER APPEARS; the four general-point diagonals (1279/1344, 299/288, 643/576, 239/240) are distinct, so c*\'s 257/192 uniformity was special to c*.\nRESULT: THE SEAM, AND THE THREE CORRECTIONS. L147 is EXACTLY the moment-locus where theta\'s seam Gram vanishes, at rank 4, so the seam residue is IDENTICALLY ZERO on the stratum -- rank 0, inertia (0,8,0): the Block 156 cone sign lock is evaded by ANNIHILATION, NOT POSITIVITY, and there is no positive seam content to have. Theta-prime\'s lock FIRES UNTOUCHED: the traceless LIVE diagonal (v, -v, -u, u)/4 on (0,2,5,7), (2,4,2) with live-live (2,0,2) at the generic point, PSD iff u = v = 0 because a traceless diagonal is PSD iff zero. CORRECTIONS, EACH QUOTED THEN CORRECTED: D1 the move-sweep count; D2 theta-prime\'s DEAD blocks are (1,3) and (4,6), NOT (5,7), which is live-live and identically zero there; D3 "no curved stratum point makes it PSD" is FALSE and is STRUCK -- counterexample sigma_(0,1) = 1/3, sigma_(2,3) = -1/4 with nu_(2,3) = 3/2, cone-admissible, on the stratum, genuinely curved, seam Gram identically zero there; the correct qualifier is FLAT ODD-TIME ROWS and not a flat carrier. (2,4,2) is the GENERIC-POINT value: (1,6,1) at u = 0 or v = 0, (0,8,0) at both.\nDECISION_CUT: THE THETA/EVEN-X PAIRING CLASS IS COMPLETELY UNDERSTOOD AND CLOSED. Its positive sector is EXACTLY its quotient sector; it is mass-tolerant EXACTLY on the cross-parity-vanishing locus; it is ORIENTATION-BLIND; it DELETES the curvature the carrier records. THE CLASS OFFERS NO ROUTE to a connection-carrying positive structure, and that is the lane\'s final word on it at this fixture. NOTHING is registered, adopted or proposed; theta is NOT re-adopted; theta-prime is NOT adopted; Block 145\'s verdict is NOT retired; Block 161 is NOT corrected; no landed note is edited. REMAINING OPEN: the SITE-REFLECTION mass channel -- the one pairing class where the mass CAN appear, never tested, the one live lead; and the pool 2 handoff items (contract E; the cutting residuals; the signed-flux census).\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero.'


# ---------------------------------------------------------------------------
# claims: the only thing a mutation is allowed to touch
# ---------------------------------------------------------------------------
def build_claims(mutation: str) -> dict:
    claims: dict = {
        "main_head": CURRENT_MAIN,
        "parent_pin": "resolved",
        "cross_parity_is_the_locus": True,
        "iff_codimensions": IFF_CODIMENSIONS,
        "shared_g_identity": True,
        "indefinite_edges": INDEFINITE_EDGE_COUNT,
        "l154_inert": True,
        "even_x_forced_flat": True,
        "flip_alone_invariant": True,
        "flattening_moves": FLATTENING_MOVES,
        "stabilizer_order": STABILIZER_ORDER,
        "theta_seam_inertia": SEAM_STRATUM_INERTIA,
        "required_scope_keys": SCOPE_KEYS,
    }
    if mutation == "stale_main_authority":
        claims["main_head"] = STALE_MAIN
    elif mutation == "stale_parent_authority":
        claims["parent_pin"] = "stale"
    elif mutation == "claim_escape_exists":
        # THE DECOUPLING IDENTIFICATION DENIED: the mass-survival locus asserted
        # to be something OTHER than the cross-parity vanishing locus, i.e. a
        # channel that stays positive while carrying cross-parity content
        claims["cross_parity_is_the_locus"] = False
    elif mutation == "break_layered_iff":
        # the codimension arithmetic of the layered equivalence denied: PSD at a
        # nonzero mass asserted to cost only 4 rather than 8
        claims["iff_codimensions"] = (4, 4, 4)
    elif mutation == "break_shared_g":
        # the factorization denied: the sixteen edge forms asserted NOT to be a
        # per-edge scalar times ONE shared pullback
        claims["shared_g_identity"] = False
    elif mutation == "claim_edge_indefinite":
        # the 0-indefinite census denied: the four dead edges asserted
        # indefinite ON the stratum, which is their OFF-stratum behaviour
        claims["indefinite_edges"] = EMPTY_EDGE_COUNT
    elif mutation == "claim_l154_active":
        # L154 asserted to do work for the theta pairing, which would make the
        # codimension-8 statements false at their own scope
        claims["l154_inert"] = False
    elif mutation == "break_recording_rule":
        # the staggered recording rule denied at its load-bearing half: the
        # even-time even-x cells asserted NOT to be forced flat
        claims["even_x_forced_flat"] = False
    elif mutation == "claim_orientation_recorded":
        # THE FLIP STRENGTHENING DENIED: the form asserted to record a shear
        # orientation, i.e. NOT invariant under FLIP with the mass left alone
        claims["flip_alone_invariant"] = False
    elif mutation == "claim_flattenable":
        # the move sweep denied: some committed carrier move asserted to flatten
        # the stratum's recorded shear
        claims["flattening_moves"] = 1
    elif mutation == "break_stabilizer":
        # the taste reading's load-bearing number: the stabilizer asserted to be
        # the full translation group
        claims["stabilizer_order"] = TRANSLATION_GROUP
    elif mutation == "claim_seam_positive":
        # ANNIHILATION denied and replaced by POSITIVITY: theta's seam Gram on
        # the stratum asserted to be a nonzero PSD object rather than zero
        claims["theta_seam_inertia"] = (2, 6, 0)
    elif mutation == "claim_corrects_161":
        # the adjudication duty dropped from the note's scope: without these
        # keys the note may read as CORRECTING a predecessor that was accurate
        claims["required_scope_keys"] = tuple(
            key
            for key in SCOPE_KEYS
            if key
            not in (
                "b161_accurate",
                "no_successor_correction",
                "different_ambient",
                "display_slip",
                "enumerated_twenty",
            )
        )
    elif mutation == "drop_site_reflection_lead":
        # the one remaining live lead dropped from the note's scope
        claims["required_scope_keys"] = tuple(
            key
            for key in SCOPE_KEYS
            if key not in ("site_reflection_lead", "pool_two")
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
            "docs/ADMISSIBILITY_DIRAC_KAHLER_MASS_SURVIVAL_STRATUM_BOUNDED_THEOREM_NOTE_2026-08-20.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_VALIDATION_BATTERY_BOUNDED_THEOREM_NOTE_2026-08-20.md",
            "scripts/admissibility_dirac_kahler_validation_battery_2026_08_20.py",
        )
        and PARENT_ARTIFACTS == (BLOCK161_NOTE, BLOCK161_RUNNER)
        and len(PARENT_ARTIFACT_BLOBS) == len(PARENT_ARTIFACTS) == 2
        and facts.main_head == claims["main_head"]
        and authority.fixed_authority
        and authority.parent_pin_is_commit
        and authority.parent_ref_and_ancestry
        and parent_blobs_ok
    )

    cross_is_locus = bool(
        facts.support[2] == M0_CROSS
        and facts.support[3] == M1_CROSS
        and facts.support[9] == M0_MODULI
        and facts.support[10] == M1_MODULI
        and facts.support[5] == ()
        and facts.support[7] == ()
    )
    gate_b = bool(
        facts.calibration
        == (
            (4, 6, 2),
            True,
            True,
            True,
            (GENERIC_MOMENT_U, GENERIC_MOMENT_U, -GENERIC_MOMENT_U,
             -GENERIC_MOMENT_U, GENERIC_MOMENT_V, GENERIC_MOMENT_V,
             -GENERIC_MOMENT_V, -GENERIC_MOMENT_V),
            (sp.Integer(1),) * 4,
            EDGE_COUNT,
            4,
        )
        and len(facts.support[0]) == CROSS_PARITY_ENTRIES
        and facts.support[1] == CROSS_PARITY_ENTRIES
        and facts.support[4] == MASS_CROSS_ENTRIES
        and facts.support[6] == ()
        and facts.support[8] == EVEN_SLOTS
        and cross_is_locus == claims["cross_parity_is_the_locus"]
        and facts.layers[0] == (BALANCE_RANK, L147_RANK, L154_RANK)
        and facts.layers[1] == (SURVIVAL_RANK, STRATUM_RANK)
        and facts.layers[2] is True
        and facts.layers[3] is True
        and facts.layers[4] == (sp.Integer(0),) * 4
        and facts.layers[5] == M1_CROSS
        and facts.layers[6] == M0_CROSS
        and facts.layers[7] == PSD_INERTIA
        and facts.layers[8] == BALANCE_ONLY_MASSIVE_INERTIA
        and facts.layers[9] == L147_ONLY_MASSLESS_INERTIA
        and facts.layers[10] is True
        and facts.layers[11] is True
        and (facts.layers[0][0], facts.layers[0][1], facts.layers[1][0])
        == claims["iff_codimensions"]
        and facts.exact_no_float
    )

    gate_c = bool(
        facts.factorization[0] == claims["shared_g_identity"]
        and len(facts.factorization[1]) == 16
        and all(
            row[1] == 4 and row[2] and row[3]
            for row in facts.factorization[2]
        )
        and facts.factorization[3] is True
        and facts.factorization[4] == (sp.Integer(0),) * 4
        and facts.factorization[6] is True
        and facts.census[1] == {
            PSD_INERTIA: PSD_EDGE_COUNT,
            NSD_INERTIA: NSD_EDGE_COUNT,
            DEAD_INERTIA: EMPTY_EDGE_COUNT,
        }
        and facts.census[2] == PSD_EDGES
        and facts.census[3] == claims["indefinite_edges"]
        and facts.census[4] is True
        and facts.census[5] == FULL_HOP_CENSUS
        and facts.census[6] == FULL_HOP_CROSS
        and facts.census[7] == (sp.Integer(0),) * 4
        and facts.census[8] == (True, True)
        and facts.census[9] == (MASSIVE_CURVED_INERTIA,) * EMPTY_EDGE_COUNT
        and facts.census[10] == (sp.Integer(0),) * HALF
        and facts.census[11] == MASSIVE_CURVED_INERTIA
        and facts.census[12] == ODD_X_INERTIA
        and facts.exact_no_float
    )

    gate_d = bool(
        facts.extent[0]
        == (BALANCE_RANK, L147_RANK, L154_RANK, SURVIVAL_RANK, STRATUM_RANK)
        and facts.extent[1]
        == (SURVIVAL_DIMENSION, STRATUM_DIMENSION, SLICE_CODIMENSION)
        and facts.extent[2] is True
        and facts.extent[3] is True
        and facts.extent[4] is True
        and facts.extent[5] is True
        and (facts.extent[6] and facts.extent[7] == () and facts.extent[8] == ())
        == claims["l154_inert"]
        and facts.algebra[0] is True
        and facts.algebra[1] is True
        and facts.algebra[2] is True
        and facts.algebra[3] == KLEIN_ORDER
        and facts.algebra[4] == LX
        and facts.algebra[5] == JOINT_CHARACTER_DIMENSION
        and facts.algebra[6] == (KLEIN_CHARACTER,)
    )

    gate_e = bool(
        (
            facts.recording[0] == (sp.Integer(0),) * 4
            and facts.recording[1] == (sp.Integer(0),) * 4
            and facts.recording[2] == [0]
        )
        == claims["even_x_forced_flat"]
        and all(value != 0 for value in facts.recording[3])
        and facts.recording[4] == 4
        and facts.recording[5] == (sp.Integer(0), sp.Integer(0))
        and facts.recording[6] == (1, 1)
        and facts.recording[7] is True
        and facts.recording[9] == (
            GENERIC_MOMENT_U, GENERIC_MOMENT_U,
            -GENERIC_MOMENT_U, -GENERIC_MOMENT_U,
        )
        and facts.recording[10] == (GENERIC_MOMENT_U, GENERIC_MOMENT_V)
        and facts.recording[11] == LX
        and facts.curvature[0] == MOVE_PROFILES
        and facts.curvature[1] == MOVE_PROFILES
        and facts.curvature[2] == claims["flattening_moves"]
        and facts.curvature[3] == FLATTENING_MOVES
        and facts.curvature[4] == CARRIER_TRANSLATIONS
        and facts.curvature[5] is True
        and facts.curvature[6] is True
        and facts.curvature[7] is True
        and facts.curvature[8] == ("v",)
        and facts.curvature[9] == ("u",)
        and facts.curvature[10] == ()
        and facts.curvature[11] == (
            sp.Integer(3), sp.Integer(-3), sp.Integer(3), sp.Integer(-3)
        )
        and facts.flip[0] is True
        and (facts.flip[1] and facts.flip[2] and facts.flip[3] == ())
        == claims["flip_alone_invariant"]
        and facts.flip[4] is True
        and facts.flip[5] is True
        and facts.flip[6] == M0_CROSS
        and facts.flip[7] == tuple(-value for value in M0_MODULI)
        and facts.exact_no_float
    )

    gate_f = bool(
        facts.stability[0] == TRANSLATION_GROUP
        and facts.stability[1] == ORBIT_CENSUS
        and facts.stability[2] == STABILIZER_SHIFTS
        and facts.stability[3] == claims["stabilizer_order"]
        and facts.stability[4] is True
        and facts.stability[5] is True
        and facts.stability[6] is True
        and facts.stability[7] == STRATUM_CARRIER_STABILIZER
        and facts.stability[8] is True
        and facts.stability[9] == EDGE_COUNT
        and facts.stability[10] is False
        and facts.stability[11] is True
        and facts.stability[12] == (
            R(0), R(0), R(-1, 2), R(1, 3),
            R(0), R(0), R(-1, 2), R(1, 3),
            R(3, 2), R(3, 2), R(1), R(11, 6),
            R(-4, 3), R(-4, 3), R(-11, 6), R(-1),
        )
        and facts.stability[13] == PSD_EDGE_COUNT
        and facts.stability[14] == NSD_EDGE_COUNT
        and facts.stability[15] == GENERIC_DIAGONALS
        and facts.stability[16] == 4
    )

    gate_g = bool(
        facts.seam[0] == ((0, 3), (1, 2), (4, 5), (6, 7))
        and facts.seam[1] == SEAM_COEFFICIENT_RANK
        and facts.seam[2] == SEAM_STRATUM_RANK
        and facts.seam[3] == claims["theta_seam_inertia"]
        and facts.seam[4] is True
        and facts.seam[6] == THETA_PRIME_DEAD_BLOCKS
        and facts.seam[7] == 0
        and facts.seam[8] == (V, -V, -U, U)
        and facts.seam[9] == 0
        and facts.seam[10] == (sp.Integer(0), sp.Integer(0))
        and facts.seam[11] == (sp.Integer(0),) * 4
        and facts.seam[12] == THETA_PRIME_GENERIC_INERTIA
        and facts.seam[13] == THETA_PRIME_LIVE_INERTIA
        and facts.seam[14] is True
        and facts.seam[15] == THETA_PRIME_HALF_DEAD_INERTIA
        and facts.seam[16] == DEAD_INERTIA
        and facts.seam[17] is True
        and facts.seam[18] == (sp.Integer(1),) * 4
        and facts.seam[19] == (sp.Integer(0),) * ODD_MOMENTS
        and facts.seam[20] is True
        and facts.seam[21] is True
        and facts.seam[22] is True
        and facts.seam[23] is True
        and facts.seam[24] == PSD_INERTIA
        and facts.seam[25] == 2
        and facts.exact_no_float
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
            "run the two TWICE-VERIFIED sweeps: the full-hop inertia census "
            "over all sixteen edges at the generic stratum point, read twice, "
            "once by the committed Block 144 congruence helper and once by "
            "exact real-root counting on the characteristic polynomial; and "
            "the carrier-move sweep recounted at BOTH group levels, showing "
            "that the cover's 32 translations descend to exactly the 16 "
            "distinct carrier profiles the baseline sweep uses"
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
        f"  CALIBRATION: Block 156's locus dimensions {facts.calibration[0]}; "
        f"the Block 161 witness pairing is mass-independent "
        f"{facts.calibration[1]} at diag(33/40, 0, ...) {facts.calibration[2]}; "
        f"the generic stratum point is cone-admissible {facts.calibration[3]} "
        f"with odd moments {facts.calibration[4]}, even-cell moments zero "
        f"{facts.calibration[5]}, {facts.calibration[6]} distinct a-moduli and "
        f"{facts.calibration[7]} distinct even-time odd-x shears"
    )
    print(
        f"  THE COMPLETE SUPPORT: the cross-parity block is {facts.support[1]} "
        f"entries {facts.support[0]}; at m^0 {facts.support[2]} carrying ten "
        f"times {facts.support[9]}; at m^1 {facts.support[3]} carrying eight "
        f"times {facts.support[10]}; supp(dF/dm) is exactly those "
        f"{facts.support[4]}; the odd-odd block is {facts.support[5]} and the "
        f"even-even off-diagonal is {facts.support[6]} with shear content "
        f"{facts.support[7]}; the diagonal support is {facts.support[8]}"
    )
    print(
        f"  THE LAYERED EQUIVALENCE, BY RANK: (balance, L147, L154) ranks "
        f"{facts.layers[0]}, (survival, stratum) ranks {facts.layers[1]}; "
        f"mass-independence on L147 alone {facts.layers[2]} and NOT on the "
        f"balance alone {facts.layers[3]}; every odd-slot diagonal is "
        f"{facts.layers[4]}; the balance alone leaves {facts.layers[5]} and "
        f"L147 alone leaves {facts.layers[6]}; measured, the balance-only "
        f"carrier is {facts.layers[7]} at m = 0 and {facts.layers[8]} at "
        f"m = 1, the L147-only carrier {facts.layers[9]} at m = 0, both "
        f"cone-admissible {facts.layers[10]} {facts.layers[11]}"
    )
    print(
        f"  THE SHARED G: the 16-edge identity F = c(i,j) Q^T G Q holds "
        f"{facts.factorization[0]} with G carrying {len(facts.factorization[1])}"
        f" moduli; each 5G diagonal is a unit-coefficient sum of four strictly "
        f"positive moduli {tuple(row[1:] for row in facts.factorization[2])}; "
        f"the primary IS the pullback {facts.factorization[3]}; odd diagonals "
        f"{facts.factorization[4]}; dF/dm = 0 on all 16 "
        f"{facts.factorization[6]}"
    )
    for slot, row in zip(EVEN_SLOTS, facts.factorization[2]):
        print(f"    5 G[{slot},{slot}] = {' + '.join(row[0])}")
    print(
        f"  THE EDGE CENSUS, COMPUTED: {facts.census[1]} at m = 1, identical "
        f"at m = 0 {facts.census[4]}; PSD edges {facts.census[2]}; indefinite "
        f"edges {facts.census[3]}; the FULL-HOP census {facts.census[5]} with "
        f"cross-parity support {facts.census[6]}, hollow odd diagonals "
        f"{facts.census[7]} against strictly negative couplings "
        f"{facts.census[8]}, and the four deletion-dead edges "
        f"{facts.census[9]} before deletion; the odd-x conjugate is hollow "
        f"{facts.census[10]} at {facts.census[11]} on the stratum against "
        f"{facts.census[12]} at the flat carrier"
    )
    print(
        f"  THE EXTENT: ranks {facts.extent[0]} give (survival, stratum, "
        f"slice) = {facts.extent[1]} in the 32-coordinate cone; the chart "
        f"inverts {facts.extent[2]} {facts.extent[3]} on the conic "
        f"{facts.extent[4]} and round-trips {facts.extent[5]}; the codim-8 "
        f"locus already gives the same pullback {facts.extent[6]} and sees "
        f"neither its L154 freedoms {facts.extent[7]} nor any shear modulus "
        f"{facts.extent[8]}"
    )
    print(
        f"  THE KLEIN STRUCTURE: involutions {facts.algebra[0]}, commuting "
        f"{facts.algebra[1]}, fixed-point-free {facts.algebra[2]}; group order "
        f"{facts.algebra[3]}; the orbit of a cell has size {facts.algebra[4]} "
        f"so the action is simply transitive; the joint (-,-) eigenspace has "
        f"dimension {facts.algebra[5]} spanned by {facts.algebra[6]}"
    )
    print(
        f"  THE RECORDING RULE: even-time even-x sigma {facts.recording[0]} and "
        f"moments {facts.recording[1]}, with b = 0 iff sigma in "
        f"{facts.recording[2]}; even-time odd-x sigma {facts.recording[3]} at "
        f"{facts.recording[4]} distinct moments; odd-row spatial means "
        f"{facts.recording[5]} at {facts.recording[6]} distinct magnitudes, "
        f"R- and S-antisymmetric {facts.recording[7]}; at t = 1 sigma is "
        f"{facts.recording[8]} against moments {facts.recording[9]}, "
        f"{facts.recording[11]} distinct |sigma| against one |b|; "
        f"(u, v) = {facts.recording[10]}"
    )
    print(
        f"  THE MOVE SWEEP, AT ITS CORRECTED SIZE: {facts.curvature[0]} "
        f"profiles over {facts.curvature[4]} carrier translations x FLIP, all "
        f"distinct {facts.curvature[1]}, flat ones {facts.curvature[2]}, "
        f"spatially constant odd rows {facts.curvature[3]}; the carrier is "
        f"curved {facts.curvature[5]} with a non-diagonal cover Hodge "
        f"{facts.curvature[6]} and a non-identity quotient {facts.curvature[7]}"
    )
    print(
        f"  THE CURVATURE IS DELETED: the full-hop diagonal carries "
        f"{facts.curvature[8]} and {facts.curvature[9]} at 20x coefficients "
        f"{facts.curvature[11]}, while the deleted object carries "
        f"{facts.curvature[10]}"
    )
    print(
        f"  FLIP, OVER THE WHOLE STRATUM: the two stratum carriers differ "
        f"{facts.flip[0]} and give the same form {facts.flip[1]}, "
        f"mass-independent {facts.flip[2]}, with shear content "
        f"{facts.flip[3]}; a is even in sigma {facts.flip[4]} and b is odd "
        f"{facts.flip[5]}; Block 161's joint identity fails only at "
        f"{facts.flip[6]} at five times {facts.flip[7]} -- the even-shear "
        f"balance alone"
    )
    print(
        f"  STABILITY: {facts.stability[0]} cover translations, census "
        f"{facts.stability[1]}, stabilizer {facts.stability[2]} of order "
        f"{facts.stability[3]}, closed {facts.stability[4]}, inverses "
        f"{facts.stability[5]}, identity {facts.stability[6]}; the STRATUM's "
        f"own carrier stabilizer is {facts.stability[7]}; the T6 law holds on "
        f"{facts.stability[9]} edges {facts.stability[8]} with s_x present "
        f"{facts.stability[10]} and s_t present {facts.stability[11]}; the "
        f"normalised scalars are {facts.stability[12]} at "
        f"{facts.stability[13]} positive and {facts.stability[14]} negative; "
        f"the four generic diagonals {facts.stability[15]} are "
        f"{facts.stability[16]} distinct"
    )
    print(
        f"  THE SEAM: theta's Gram is supported at {facts.seam[0]} with "
        f"coefficient rank {facts.seam[1]}, and on the stratum has rank "
        f"{facts.seam[2]} at inertia {facts.seam[3]}, already zero on the "
        f"codim-8 locus {facts.seam[4]}; theta-prime's support is "
        f"{facts.seam[5]} with DEAD blocks {facts.seam[6]} and the live-live "
        f"pair (5,7) at {facts.seam[7]}; the live diagonal is 1/4 x "
        f"{facts.seam[8]}, traceless {facts.seam[9]}, in +- pairs "
        f"{facts.seam[10]}, dead slots {facts.seam[11]}; at the generic point "
        f"{facts.seam[12]} with live-live {facts.seam[13]} while theta's is "
        f"zero {facts.seam[14]}; at u != 0 = v it is {facts.seam[15]} and at "
        f"u = v = 0 it is {facts.seam[16]}"
    )
    print(
        f"  DEFECT D3, THE CURVED COUNTEREXAMPLE: cone-admissible "
        f"{facts.seam[17]}, even-cell moments zero {facts.seam[18]}, odd rows "
        f"{facts.seam[19]}, non-diagonal cover Hodge {facts.seam[20]}, "
        f"non-identity quotient {facts.seam[21]}, {facts.seam[25]} nonzero "
        f"shear moments; theta-prime's seam Gram is zero there "
        f"{facts.seam[22]} and theta's is zero {facts.seam[23]}, while the "
        f"deleted pairing is {facts.seam[24]} at m = 1 -- so the point is LIVE "
        f"and CURVED and vacuously PSD"
    )
    if facts.deep_full_hop is not None:
        print(f"  --deep full-hop census, twice verified: {facts.deep_full_hop}")
    if facts.deep_moves is not None:
        print(f"  --deep move sweep, both group levels: {facts.deep_moves}")
    print()

    checks = Checks()
    checks.check(
        "A-authority",
        "main plus TWO parent artifacts are content-bound: Block 161's note and runner, which are BOTH the stack parent this block's branch is cut from AND the content parent whose import chain (b160 -> b159 -> b158 -> b156 -> b155/b154/b153/b148/b147/b145/b144/b142/b137/b134/b105) carries every committed constructor used here and is pinned by Block 161's own gate A rather than duplicated in this one",
        gate_values["A"],
    )
    checks.check(
        "B-the-complete-support-and-the-layered-equivalence",
        "THE BLOCK'S HEADLINE IS AN EQUIVALENCE WITH THREE LAYERS AND IT IS ENUMERATED RATHER THAN OBSERVED: on the FREE 64-modulus family the deletion-restricted theta pairing's ENTIRE support is four even-even diagonals, an IDENTICALLY ZERO odd-odd block, an even-even block with NO shear modulus in it at all, and exactly eight cross-parity entries -- (0,7) = b_20/10, (1,4) = b_00/10, (2,5) = b_22/10, (3,6) = b_02/10 at m^0, which IS the even-shear balance, and (0,3) = m(b_30+b_33)/8, (1,2) = m(b_31+b_32)/8, (4,5) = -m(b_10+b_13)/8, (6,7) = -m(b_11+b_12)/8 at m^1, which IS L147 = ker(R+1) -- with supp(dF/dm) EXACTLY those four m^1 entries and nothing else in the form touching the mass; and because every odd-slot diagonal is identically zero, one surviving cross entry gives a strictly negative 2x2 minor, so by rank 4, rank 4 and rank 8 on the sixteen shear-moment coordinates F is mass-independent IFF L147 (codimension 4), F is PSD at m = 0 IFF the even-shear balance (codimension 4), and F is PSD at ANY SINGLE m != 0 IFF both (codimension 8), which is also PSD at every mass -- verified against exact-rational cone-admissible carriers on each side, the balance-only carrier being (4,4,0) at m = 0 and (4,2,2) at m = 1 and the L147-only carrier already (4,3,1) at m = 0: THE MASS-SURVIVAL CONDITION IS THE CROSS-PARITY VANISHING CONDITION, so the positivity is QUOTIENT POSITIVITY BY CONSTRUCTION and nothing escapes the decoupling",
        gate_values["B"],
    )
    checks.check(
        "C-the-stratum-wide-PSD-theorem-and-the-census",
        "THE POSITIVITY IS PROVED OVER THE WHOLE STRATUM AND NEVER SAMPLED, AND THE DELETION IS WHAT MAKES IT: every one of the sixteen committed edges satisfies the FULL 8x8 identity F_(i,j) = c(i,j) Q^T G Q against ONE shared G built once, with c(i,j) a carrier-independent scalar and 5G = diag(a_20+a_33+m_23+n_30, a_22+a_31+m_21+n_32, a_00+a_13+m_03+n_10, a_02+a_11+m_01+n_12) -- four sums of four DISTINCT moduli with UNIT coefficients, every one of them strictly positive on the cone -- so the inertia is forced at every point of the stratum and dF/dm vanishes on all sixteen edges; the census, with every inertia COMPUTED edge by edge at m = 0 and m = 1 rather than asserted, is 6 PSD (4,4,0) / 6 NSD (0,4,4) / 4 identically zero (0,8,0) and ZERO INDEFINITE, the six PSD edges being Block 161's six exactly; AND THE OTHER CHANNELS COST WHAT THEY CARRY -- the FULL-HOP pairing carries eight cross-parity entries at (0,5), (1,6), (2,7), (3,4) fed by the four even-time odd-x shears, has a HOLLOW odd-slot pair in each block against a coupling that is strictly negative everywhere on the cone, and is measured NONSINGULAR on all sixteen edges at census {(6,0,2): 6, (2,0,6): 6, (4,0,4): 4} with not one PSD, the four deletion-dead edges being FULL-RANK INDEFINITE (4,0,4) before the deletion, and the odd-x conjugate deletion is hollow throughout at (4,0,4) on the stratum against (2,4,2) at the flat carrier",
        gate_values["C"],
    )
    checks.check(
        "D-the-extent-the-chart-the-algebra-and-L154s-inertness",
        "THE EXTENT IS COMPUTED BY RANK AND THE TWO OBJECTS ARE KEPT APART: the even-shear balance has rank 4, L147 has rank 4, L154's odd-x rows have rank 2, balance + L147 has rank 8 and all three together rank 10 on the sixteen shear-moment coordinates, so the MASS-SURVIVAL SET PROPER has DIMENSION 24 in the 32-coordinate cone and the L147 cap L154 slice has DIMENSION 22, a codimension-2 cut of it -- two objects that Block 156's dimension-2 statement, which lives in the 8-DIMENSIONAL ODD-MOMENT SPACE, does not contradict, so Block 161 stated both accurately and NO CORRECTION-IN-SUCCESSOR is warranted; the committed modulus map inverts RATIONALLY as nu = (a^2-b^2)/a and sigma = -b/a on the conic a^2 - a nu - b^2 = 0 with the round trip verified in BOTH directions, so the stratum is linear in the (a, b) chart and is an OPEN subset of a 22-dimensional subspace; L154 IS COMPLETELY INERT for the theta pairing, since on the codimension-8 locus alone the form is already the same pullback and NONE of the sixteen edge forms contains any of the four L154-violating odd-moment freedoms or any shear modulus at all; AND THE ALGEBRA IS THREE LINES -- R : x -> 3-x and S : x -> x+2 are commuting fixed-point-free involutions generating a Klein four-group of order 4 whose orbit of a cell is all four cells, so the action is SIMPLY TRANSITIVE and the spatial 4-space IS the regular representation, and the joint (-1,-1) eigenspace is ONE-dimensional BY RANK, spanned by (1,1,-1,-1)",
        gate_values["D"],
    )
    checks.check(
        "E-the-recording-rule-the-deleted-curvature-and-FLIP",
        "THE PHYSICS IS A STAGGERED RECORDING RULE AND THE CURVATURE IT RECORDS IS DELETED RATHER THAN ABSENT: even-time slices FORCE the two even-x cells flat -- their shears and their moments are zero and b = 0 iff sigma = 0 on the cone -- while their two odd-x cells are FREE and carry four distinct nonzero moments; odd-time slices carry all four cells at ONE locked magnitude with ZERO spatial mean, antisymmetric under BOTH R and S, and the constraint is on the MOMENTS and not on sigma, the generic t = 1 row having four distinct |sigma| against a single |b|; the carriers are GENUINELY CURVED with non-diagonal cover Hodge and non-identity quotient, and NO committed carrier move flattens them -- the sweep is 32 profiles over 16 CARRIER translations x FLIP, all distinct, none flat and none spatially constant on an odd-time row, the count corrected from the solve transcript's '64 profiles over 32 translations'; the FULL-HOP diagonal carries the recorded shear LINEARLY at 20x coefficients (+3, -3) in v and (+3, -3) in u while the deletion-restricted PSD object contains neither, so the link deletion is EXACTLY the step that erases the recorded curvature; AND FLIP IS STRENGTHENED OVER THE WHOLE STRATUM BY THE CHECKER'S ROUTE, not by the solve's vacuous substitution -- the stratum carrier is assembled symbolically with free positive nu and a, locked odd rows and free even-time odd-x shears, the shears are negated BEFORE the cover Hodge is built so the two carriers genuinely differ, and the pairings are IDENTICAL with the mass left alone, the form containing no shear modulus at all and a being even in sigma at fixed nu, so it sees sigma^2 only and records NO orientation; and Block 161's joint identity F(flip(c), -m) = F(c, m) is located exactly, its difference nonzero only at the four m^0 entries at -b_20/5, -b_00/5, -b_22/5, -b_02/5, hence a consequence of THE EVEN-SHEAR BALANCE ALONE",
        gate_values["E"],
    )
    checks.check(
        "F-stability-the-shared-stabilizer-and-the-T6-scalar-law",
        "THE STRUCTURE THAT SURVIVES IS A PROPERTY OF THE STRATUM AND NOT OF A WITNESS: over the full 32-element cover translation group with the WHOLE configuration transported at the GENERAL stratum element, the census is {(4,4,0): 8, (2,4,2): 8, (0,8,0): 16} -- Block 161's exactly -- and the stabilizer is measured to be the even-time even-x translations, an honest order-8 subgroup verified closed under all 64 compositions, closed under inverses and containing the identity; AND THE STRATUM'S OWN CARRIER-TRANSLATION STABILIZER IS THE SAME GROUP, exactly {(0,0), (0,2), (2,0), (2,2)} of the sixteen carrier shifts, lifting to those eight cover shifts, so the carrier locus and the pairing SHARE a stabilizer and the taste structure is carrier-level; the T6 scalar law 4c(i,j) = base(i) - s_t (lambda_j - lambda_i) with base = s_t (0, 0, 1, -1) holds on all sixteen edges with SYMBOLIC healing weights and SYMBOLIC shears over the whole stratum, s_x appears in NO entry of ANY edge while s_t does, and at the committed weights the law reproduces the sixteen measured scalars exactly at 6 positive and 6 negative, so chart transitions move only a scalar sign against a G common to all sixteen edges; AND THE GENERAL ELEMENT IS NOT c* -- its four carrier diagonals (1279/1344, 299/288, 643/576, 239/240) are all DISTINCT, so Block 161's single common constant 257/192 was special to c*",
        gate_values["F"],
    )
    checks.check(
        "G-the-seam-annihilation-and-the-three-corrections",
        "THE SEAM IS EVADED BY ANNIHILATION AND NEVER BY POSITIVITY, AND THE TRANSCRIPT'S TWO SEAM DEFECTS ARE CORRECTED: theta's seam residue Gram on the free family is supported at exactly (0,3), (1,2), (4,5), (6,7) and its coefficient matrix on the sixteen shear moments has RANK 4, so the moment-locus where it vanishes IS L147 -- whence on the stratum it is IDENTICALLY ZERO at rank 0 and inertia (0,8,0), already so on the codimension-8 locus alone, and the Block 156 cone sign lock has nothing to fire on rather than being satisfied; theta-prime's lock fires UNTOUCHED, its DEAD blocks being (1,3) AND (4,6) -- NOT (5,7), which is a LIVE-LIVE pair and is identically zero there, and which is a different committed object -- and what survives being the traceless LIVE diagonal (v, -v, -u, u)/4 on slots (0,2,5,7), measured (2,4,2) with live-live (2,0,2) at the generic point while theta's is zero, (1,6,1) when exactly one of u, v vanishes and (0,8,0) when both do, so PSD holds IFF u = v = 0 because the live diagonal is a pair of +- pairs and a traceless diagonal is PSD iff it is zero; AND THE TRANSCRIPT'S 'no curved stratum point makes it PSD' IS FALSE AND IS STRUCK -- the checker's counterexample sigma_(0,1) = 1/3 and sigma_(2,3) = -1/4 with nu_(2,3) = 3/2 is cone-admissible, sits ON the stratum with dead odd rows, is GENUINELY CURVED with a non-diagonal cover Hodge and a non-identity quotient and two nonzero shear moments, carries an identically zero theta-prime seam Gram and is LIVE at (4,4,0) at m = 1, so the correct qualifier is FLAT ODD-TIME ROWS and not a flat carrier",
        gate_values["G"],
    )
    checks.check(
        "H-note-scope",
        "the scout discipline stated as a discipline -- every support restriction, reweighting, reflection and half carrier here is a registered-premise-class change that is MEASURED and never registered, adopted or proposed -- THE LAYERED EQUIVALENCE carried as the headline with its three layers written out in plain ASCII and their codimensions 4, 4 and 8, the supp(dF/dm) statement, the identically zero odd-odd block and the shear-free even-even block, the cross-parity vanishing condition named as the mass-survival condition, QUOTIENT POSITIVITY BY CONSTRUCTION, the nothing-escapes verdict, the deletion recorded as REMOVING an indefinite object and the full-hop census displayed, THE STRATUM-WIDE PSD THEOREM with its ONE shared G and its unit-coefficient sums and its never-sampled proof status, the zero-indefinite edge census with its inertias computed rather than asserted, the exact rational chart and the open 22-dimensional extent with the dimensions taken BY RANK, THE TWO-OBJECT BOOKKEEPING with dimension 24 against dimension 22 in DIFFERENT AMBIENT SPACES, the adjudication that BLOCK 161 WAS ACCURATE with NO CORRECTION-IN-SUCCESSOR and the Block 161 DISPLAY SLIP disclosed as having ENUMERATED 20 of 24 directions, L154 recorded as COMPLETELY INERT, THE KLEIN STRUCTURE with its free involutions, its regular representation and its unique joint character, THE RECORDING RULE with the forced-flat even-x cells, the zero-spatial-mean domain walls, the genuinely curved carriers, the curvature DELETED AND NOT ABSENT, the move sweep at 16 CARRIER TRANSLATIONS with the cover's shifts DESCENDING TO 16 DISTINCT profiles, FLIP ALONE with sigma^2 and no recorded orientation and the even-shear-balance-alone sharpening, THE STABILITY with the order-8 stabilizer, the stratum's own translation stabilizer, the base(i) - s_t scalar law, s_x never appearing and the four distinct diagonals, THE SEAM with L147 as the moment-locus where theta's Gram vanishes, ANNIHILATION AND NOT POSITIVITY, theta-prime's lock firing untouched, the DEAD blocks (1,3) and (4,6) against the live-live pair, the curved counterexample and the flat-odd-time-rows qualifier, THE VERDICT that the class is COMPLETELY UNDERSTOOD and offers NO ROUTE to a connection-carrying positive structure, the SITE-REFLECTION lead and the POOL-2 items carried forward, together with checker credit, the vacuous routes replaced, quoted-then-corrected readings, common-mode and cross-context disclosure, the not-re-verified list, sample scope, N1 through N8, the W1 wall, the exact N5 fence, the LaTeX rho guard, and NO priority or originality wording anywhere in the note, not even inside a prohibition list",
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
