#!/usr/bin/env python3
# Final path: scripts/admissibility_dirac_kahler_residue_transversality_gate_2026_08_20.py
"""Block 156: THE RESIDUE, THE TRANSVERSALITY, AND THE GATE.

Block 155 closed the registered completion program on Branch II and handed
forward one first item: "the theta-prime live-seam residue and the
transversality certificate, banked together with the Krein-gate result, as
Block 156".  This runner is that block.  Three certificate groups, one block,
every numeral RECOMPUTED from the committed constructors reached through the
Block 155 runner and its Block 154/153/148/147/145/144 chain.

  GROUP 1  THE THETA-PRIME LIVE-SEAM RESIDUE, settled IN TWO TIERS.
  GROUP 2  THE TRANSVERSALITY CERTIFICATE, three loci pairwise.
  GROUP 3  THE KREIN GATE, banked at BARE scope, three channels 16/16 each.

GROUP 1, the headline.  The 14 live carrier classes split exactly 7 / 7.  TYPE A
(6 singletons plus the maximal pair ((2,0),(2,1))): the surviving odd-moment
space V is exactly {b_11 = b_13 = b_31 = b_33 = 0}, DIMENSION 4, and the seam
residue Gram G' is a pure LIVE diagonal there.  TYPE B (6 singletons plus
((3,0),(3,1))): V is exactly {b_10 = b_12 = b_30 = b_32 = 0, b_11 = b_13,
b_31 = b_33}, DIMENSION 2, and G' is purely the two hyperbolic DEAD 2x2 blocks;
the per-edge system on a TYPE B class locks FOUR moments, b_11, b_13, b_31 and
b_33, one per lock row, which collapse to two independent statements only
because V already forces b_11 = b_13 and b_31 = b_33.

  TIER 1, the LINEAR 64-modulus relaxation of the carrier family: LIVE.  7 of
  the 14 classes carry a NONZERO POSITIVE SEMIDEFINITE G', with an explicit
  exact-rational witness on the single healed edge (0,2) at inertia (4,4,0).
  THIS IS A STATEMENT ABOUT A LINEAR FAMILY AND IS NOT ACHIEVED PHYSICAL
  POSITIVITY: the witness is not cone-admissible and cannot be, since its n/a/m
  moduli are not all positive.  REFINEMENT R1, from the disjoint checker and
  MANDATORY here: the witness's stronger property -- that the FULL bare pairing
  is positive semidefinite there too, because Herm([theta' K]_++) vanishes at
  that carrier -- is CARRIER-SPECIAL, not class-general.  The escape locus has
  DIMENSION 44 inside the 48-dimensional class kernel, CODIMENSION 4, and this
  runner exhibits an ALTERNATE carrier in the SAME class, with the SAME odd
  moments and the SAME shear ratio, whose full bare pairing sits at (4,0,4).
  The mechanism is exact: on that class the full pairing is [[0, B], [B^T, D]]
  with D = 1/4 the identity, so its inertia is (4, 4 - rank B, rank B), and the
  escape is exactly rank B = 0.

  TIER 2, the COMMITTED ADMISSIBLE CONE, under the HYPOTHESIS (s_x, s_t) is not
  (0, 0) -- REFINEMENT R2, carried in every statement of the result: DEAD, by a
  CONE SIGN LOCK.  Every one of the 14 classes carries four lock rows per edge
  (EIGHT for the two pair classes) of the shape P + c (s_x/s_t) b_k = 0, where P
  is a sum of EIGHT DISTINCT n/a/m moduli with one shared coefficient -- verified
  SHEAR-FREE -- and c is one nonzero rational shared by all four rows.  The
  coefficients are +1 only POST-NORMALIZATION by that shared factor, which this
  runner measures to be NEGATIVE on 6 of the 12 live singleton classes (7 of 14
  counting the two maximal pairs).  On the cone every n, a and m modulus is
  strictly positive, so each locked moment is strictly nonzero and they all
  carry ONE COMMON SIGN, where positive semidefiniteness needs two of each.
  Inertia is forced to (2,4,2) on all 14 classes; an explicit admissible witness
  at s_x/s_t = 118/9 is exhibited.

  THE R2 COUNTERPOINT, the block's SECOND THEOREM and not a footnote: at ZERO
  connection, s_x = s_t = 0, the residue K vanishes identically on all 16 edges,
  the Hermiticity cut disappears, and an ADMISSIBLE cone field is Hermitian on
  16 of 16 edges with G' nonzero at inertia (4,4,0) -- positive semidefinite.
  So on the committed cone THE RESIDUE POSITIVITY EXISTS EXACTLY WHERE THE
  CONNECTION DIES.  That is the lane's central pattern -- Block 155's banked
  no-go, and the Krein gate of Group 3 below -- at a third structural level.
  The other two corners are degenerate in different ways and both are measured:
  at s_x = 0 the classes are CONE-EMPTY, at s_t = 0 they carry only the zero
  Gram.

  VERDICT.  Block 145's never-positive-semidefinite verdict SURVIVES for theta'
  on the cone with a live connection, but its MECHANISM does not transfer.
  Theta's obstruction was structural -- a traceless Gram with an identically
  zero diagonal, so every off-diagonal 2x2 principal minor is a negative square.
  Theta-prime has four live diagonal slots and a live trace; its obstruction is
  the cone sign lock.  And Block 153's recorded "dimension 2 against dimension
  4" comparison of the mass-block Hermiticity loci is CORRECTED here: those are
  RANKS (2 against 4); as DIMENSIONS the loci are 6 (theta') against 4 (theta),
  so the comparison INVERTS.  Landed notes are never edited; this is a
  correction-in-successor, which is the lane's standard.

GROUP 2, the transversality certificate.  L145 = ker(R - 1) and L147 =
ker(R + 1) for the single involution R: b_{t,x} -> b_{t,3-x}: two eigenspaces of
ONE involution, dimensions 4 and 4, complementary (intersection 0, sum the full
8-space).  L154 has dimension 6 and is NOT an eigenspace of S: x -> x + 2; it
strictly contains ker(S+1).  Both stacked CONSTRAINT ranks are 6, so both
intersections have dimension 2 and both subspace SUMS have dimension 8 -- the
"6" is a constraint rank, not a subspace dimension, and both readings are
printed so the numeral cannot be misread.  On both intersections the live
diagonal is m/4 (q, -q, -p, p) and its sign-flipped variant: two entries of each
sign, forced.  THREE INDEPENDENT ROUTES agree that positivity kills them --
exhaustive extreme-ray enumeration, real-domain QUANTIFIER ELIMINATION (the
checker's replacement for the extreme-ray step), and a finite exact sign sweep
-- each returning p = q = 0, hence all eight odd moments zero and m G' the zero
matrix.  The three loci pairwise meet ONLY at the dead carrier, so the Block 145
live-seam locus and the Block 147 annealed locus are RETIRED as search spaces
for Block 154 style positivity.

GROUP 3, the Krein gate, banked at BARE scope.  PROVENANCE: the completeness
sweep opened the indefinite-metric route -- no positivity axiom, the
constraint-sector shape, ingredients already in Blocks 143/145/148 -- and its
PRE-COMMITTED gate was connection visibility on the live sector.  MEASURED:
(a) anti([theta' K]_++)[LIVE,LIVE] = 0 on 16/16 edges; (b) Herm([X_0 K]_++)
[LIVE,LIVE] = 0 on 16/16, with controls that the object is itself nonzero and
shear-carrying on 16/16 and that its DEAD-LIVE block is live on ALL 16 edges, at
10 slots on the two self-edges (2,2) and (3,3) and 12 on the other 14 -- the
checker's exact pin, and a CORRECTION to the expected 16/16 control, which is
theta-prime-specific; (c) with Block 154's Hermitian channel, THREE CHANNELS,
16/16 EACH: the bare connection has NO live-sector witness anywhere.  Stronger
than the parts: the RAW block [theta' K]_++[LIVE,LIVE] has 0 nonzero slots of 16
on every edge.  TWO BONUSES: anti([theta' K]_++)[DEAD,DEAD] = 0 on 16/16, so
Block 154's DEAD x DEAD anti-Hermitian residue is a MASS-block phenomenon that
does not recur for K; and anti([X_0 K]_++) = 0 in ALL FOUR blocks, so
[X_0 K]_++ is HERMITIAN OUTRIGHT on this carrier family.  The route closes at
its own gate and the lane's central negative is strengthened to the bare level.
K is real and antisymmetric, measured here, so there is no i-convention
ambiguity in any of these Hermitian / anti-Hermitian splits.

DISCLOSURES CARRIED IN THE GATES, not in an appendix.  Neither tier is evaluated
at the committed atlas shears (s_x, s_t) = (3/5, 4/5), i.e. tau = 3/4: the tier
results are CONE-WIDE statements in the ratio tau, each admissible carrier
picking its own tau from its own Hermiticity rows, and the specific atlas point
is untested where relevant -- a genuine widening of the working scope past Block
153's atlas.  s_x and s_t carry NO normalization anywhere in the chain.  The
cone search this runner performs is an EXACT-RATIONAL STRUCTURED SAMPLE and is
corroboration for the symbolic lock argument, never itself the proof; the
disjoint checker ran a larger independent sample of its own, which is recorded
in the note as the checker's and not as this runner's measurement.  The
certificate plumbing -- blob pins, mutation gates, axiom-registry ties -- was
outside the checker's bounded read scope, so it checked physics and not
plumbing.

NO HARDCODED CERTIFICATE ANYWHERE: every printed numeral is recomputed in the
measurement pass, and no check is registered as a literal True.  Every
comparison is exact SymPy arithmetic; no floats anywhere; the integer monotonic
clock is used only for the runtime gate.

TOOLING DISCLOSURE: every inertia is computed by SYMMETRIC CONGRUENCE, delegated
to the committed Block 144 helper through the Block 155/154/153/148/147/145
import chain, so the tool this block reasons with is exactly the blob gate A
pins; the Block 142/143 root-counting helper is unsound on these degenerate
spectra and is deliberately not used; the calibration and the (n_+, n_0, n_-)
ORDER of the returned triple are asserted in gate B before any inertia is read.

PROVENANCE DISCLOSURE: the 64-modulus carrier model, the cover Hodge, the
antiperiodic quotient, the action law, the half pairing, the connection data,
the healing weights, the odd-centred theta', the staggered parity X_0, the
four-chart atlas, the admissible cone and the symmetric-congruence inertia
helper are ALL COMMITTED objects, imported through the Block 155 runner and
never re-derived.  The external literature on Krein-space reconstruction, on
indefinite-metric quantization and on lattice Dirac-Kahler positivity is
REFERENCED nowhere and BORROWED nowhere; every statement is re-proved
in-framework.

HYPOTHESES, named and not imported.  (H1) the pairing convention is [X Q]_{++}
on the half carrier {p = 0, 1}.  (H3) "positive" is a statement about the
Hermitian part.  (H4) the physical cone is nu > 0, |sigma| < 1 per cell.
(H9-156) a LIVE CARRIER CLASS is the locus cut by the per-edge Hermiticity
conditions of a subset of healed edges together with the mass rows, and it is
LIVE when its odd-moment image is nonzero; because adding edges only adds
constraints, the existence question is decided by the singletons and the pair
classes add nothing.  (H10-156) TIER 2's never-positive statement carries the
hypothesis (s_x, s_t) != (0, 0), which is exactly the hypothesis the sign lock
consumes.

NON-CLAIMS, stated once and enforced by gate H: this block claims no priority of
any kind about curved positivity at any scope, it is NOT an OS no-go, it is NOT
a curved OS no-go, it is NOT a Records result and NOT a gravity result, it
justifies NO axiom amendment, it adopts theta' nowhere, it registers NOTHING and
it retires NOTHING.  Block 154's flat-limit calibration gap is NOT touched by
this block and carries forward as an OPEN DEFECT.
"""

from __future__ import annotations

import argparse
import itertools
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

import admissibility_dirac_kahler_discriminator_verdict_2026_08_20 as b155

b154 = b155.b154
b153 = b154.b153
b148 = b153.b148
b147 = b153.b147
b145 = b153.b145
b144 = b153.b144
b142 = b153.b142

MASS = b153.MASS


NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_RESIDUE_TRANSVERSALITY_GATE_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
BLOCK155_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DISCRIMINATOR_VERDICT_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
BLOCK155_RUNNER = (
    "scripts/admissibility_dirac_kahler_discriminator_verdict_2026_08_20.py"
)

# The two artifacts whose blobs are pinned at the parent commit.  Both are IN
# THIS WORKTREE, so plain worktree/commit blob pins suffice.  Blocks 154, 153,
# 148, 147, 145 and 144 are reached THROUGH the Block 155 runner's own import
# chain and are pinned by ITS gate A, which this block does not duplicate.
PARENT_ARTIFACTS = (
    BLOCK155_NOTE,
    BLOCK155_RUNNER,
)
# PLACEHOLDER BLOBS.  The landing supervisor refreshes these two lines by
# anchored sed against the Block 155 branch tip.  Until then gate A FAILS, which
# is the intended state of an unlanded draft.
PARENT_ARTIFACT_BLOBS = (
    "a08d13dd1e2f287e60a0d4f4ef92251a9e231f25",   # Block 155 note
    "d7e55992593bc846ba9e128854028a835c3c0cc1",   # Block 155 runner
)

# Deliberately literal: this is the complete audit read surface.  Every entry is
# a WORKTREE-READABLE path; the cache envelope stats these, so an
# origin/main-only path here would break the audit (the Block 130 lesson,
# re-learned at the Block 150 landing and inherited through Blocks 151-155).
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_RESIDUE_TRANSVERSALITY_GATE_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DISCRIMINATOR_VERDICT_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/admissibility_dirac_kahler_discriminator_verdict_2026_08_20.py",
)

AUDIT_TIMEOUT_SEC = 600
# PLACEHOLDER AUTHORITY PINS, single-line hex literals refreshed by anchored sed
# at landing.  A draft must not carry a passing authority gate.
CURRENT_MAIN = "005f047923055e6ecd5dc8bce1ffd71765c2ffd8"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
# This block stacks on Block 155, so the parent branch is Block 155's.
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block155-discriminator-verdict-20260820"
)
# PLACEHOLDER: the landing supervisor replaces this with the Block 155 branch
# tip.  Until it is the real 40-hex commit the ancestry test fails and gate A
# stays red.
PARENT_COMMIT = "fc1505b16cb7bdc07c40e12ed203ade8004680e9"
# Block 152's tip: a real ancestor of HEAD that PREDATES BOTH Block 155
# artifacts.  VERIFIED before pinning with `git show <commit>:<path>`, which
# fails for the Block 155 note AND for the Block 155 runner at this commit while
# both are present at HEAD, so resolving the parent pin here leaves both pinned
# blobs ABSENT.  This pin is read ONLY under the stale mutation; the baseline
# gate never requires the stale blobs to match.
STALE_PARENT_COMMIT = "26fad1c0b18073dc1121be27adcc531c5ea0651a"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "break_massblock_dimension",
    "break_class_split",
    "break_witness_inertia",
    "claim_full_pairing_class_general",
    "claim_tier2_psd_exists",
    "claim_lock_two_moments_typeB",
    "claim_mechanism_transfers",
    "claim_loci_nested",
    "break_intersection_dim",
    "claim_gate_witness_exists",
    "break_hermitian_outright",
    "drop_zero_connection_counterpoint",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "break_massblock_dimension": "B",
    "break_class_split": "B",
    "break_witness_inertia": "C",
    "claim_full_pairing_class_general": "C",
    "claim_tier2_psd_exists": "D",
    "claim_lock_two_moments_typeB": "D",
    "claim_mechanism_transfers": "E",
    "claim_loci_nested": "F",
    "break_intersection_dim": "F",
    "claim_gate_witness_exists": "G",
    "break_hermitian_outright": "G",
    "drop_zero_connection_counterpoint": "H",
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
    return git_output("hash-object", path)


def commit_blob(commit: str, path: str) -> str:
    """The blob at a path in a commit, or "" when the path is absent there.

    Absence is a real answer here: the stale-pin control deliberately probes a
    commit that predates both pinned artifacts.
    """
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
    return b153.no_float(value)


def congruence_inertia(matrix: sp.MatrixBase) -> tuple[int, int, int]:
    """Exact (n_positive, n_zero, n_negative) WITH multiplicity, by congruence.

    Delegated to the COMMITTED Block 144 helper through the Block
    155/154/153/148/147/145 import chain, so the tool this block reasons with is
    exactly the blob gate A pins.  b142.inertia counts DISTINCT real roots and
    is unsound on these degenerate spectra; the calibration AND the order of the
    returned triple are asserted in gate B.
    """
    return b144.congruence_inertia(matrix)


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
            len(committed_blobs) == len(PARENT_ARTIFACTS)
            and all(is_hash(value) for value in committed_blobs)
            and committed_blobs == worktree_blobs
            and committed_blobs == PARENT_ARTIFACT_BLOBS
        ),
        bool(
            len(stale_blobs) == len(PARENT_ARTIFACTS)
            and all(is_hash(value) for value in stale_blobs)
            and stale_blobs == worktree_blobs
        ),
    )


# ---------------------------------------------------------------------------
# the committed model, imported wholesale through Block 155
# ---------------------------------------------------------------------------
HALF = b153.HALF                          # 8 sites in the positive-time half
PHYS = b153.PHYS                          # 16 quotient sites
PLUS = b153.PLUS
X0 = b153.X0
THETA = b153.THETA
THETA_PRIME_OP = b153.THETA_PRIME_OP
HQ_FREE = b153.HQ_FREE                    # 16x16, 64 moduli
COVER_FREE = b153.COVER_FREE              # 32x32, 64 moduli
COORDS = b153.COORDS                      # the 64 carrier moduli
NCOORD = len(COORDS)                      # 64
EDGE_KEYS = tuple(sorted(b153.EDGE_KEYS))  # the 16 healed edges
HEALING_WEIGHTS = b153.HEALING_WEIGHTS
SHEAR_X, SHEAR_T = b153.SHEAR_X, b153.SHEAR_T
ODD = b153.ODD_SHEAR_COORDS               # b_10 b_11 b_12 b_13 b_30 ... b_33
SHEAR_COORDS = b153.SHEAR_COORDS          # all 16 shear moments
CELLS = b153.CELLS

# the DEAD/LIVE split of the half carrier is READ OFF the committed X_0, never
# hard-coded; gate B pins it against the committed Block 154 tuples.
DEAD = tuple(k for k in range(HALF) if X0[k, k] == -1)
LIVE = tuple(k for k in range(HALF) if X0[k, k] == 1)

ODD_INDEX = tuple(COORDS.index(v) for v in ODD)
SHEAR_INDEX = tuple(COORDS.index(v) for v in SHEAR_COORDS)
NON_SHEAR_INDEX = tuple(
    i for i in range(NCOORD) if not str(COORDS[i]).startswith("b_")
)
ODD_SELECTOR = sp.Matrix(
    [[1 if COORDS[c] == v else 0 for c in range(NCOORD)] for v in ODD]
)
NAMES = tuple(str(v) for v in ODD)
TAU = SHEAR_X / SHEAR_T


def half(op: sp.MatrixBase, matrix: sp.MatrixBase) -> sp.Matrix:
    """[op . M]_{++} on the half carrier {p = 0, 1} (H1)."""
    return sp.expand(PLUS.T * op * matrix * PLUS)


def herm(matrix: sp.MatrixBase) -> sp.Matrix:
    matrix = sp.Matrix(matrix)
    return sp.expand((matrix + matrix.H) / 2)


def anti(matrix: sp.MatrixBase) -> sp.Matrix:
    matrix = sp.Matrix(matrix)
    return sp.expand((matrix - matrix.H) / 2)


def zero(matrix: sp.MatrixBase) -> bool:
    return all(sp.expand(entry) == 0 for entry in sp.Matrix(matrix))


def sub_block(matrix, rows, cols) -> sp.Matrix:
    return sp.Matrix(
        len(rows), len(cols), lambda i, j: sp.expand(matrix[rows[i], cols[j]])
    )


def live_count(matrix) -> int:
    return sum(1 for entry in sp.Matrix(matrix) if sp.expand(entry) != 0)


def span_matrix(vectors, size) -> sp.Matrix:
    if not vectors:
        return sp.zeros(size, 0)
    return sp.Matrix.hstack(*vectors)


def same_space(left: sp.Matrix, right: sp.Matrix) -> bool:
    if left.cols == 0 and right.cols == 0:
        return True
    if left.cols == 0 or right.cols == 0:
        return False
    return (
        left.rank() == right.rank() == sp.Matrix.hstack(left, right).rank()
    )


def nonneg(entry) -> bool:
    return sp.sympify(entry).is_nonnegative is True


def orthant_ray(basis):
    """A nonzero componentwise-NONNEGATIVE vector in span(basis), or None.

    COMPLETE, not a search: U cap R^n_{>=0} is a POINTED cone, so it is
    nontrivial iff it has an extreme ray r; for such an r the slice of U cut by
    the coordinate hyperplanes r vanishes on is exactly 1-dimensional (any extra
    direction y would put both r + eps y and r - eps y in the cone).  All 2^n
    coordinate subsets are enumerated, so a None return is a PROOF of emptiness.
    """
    if not basis:
        return None
    span = span_matrix(basis, basis[0].rows)
    size = span.rows
    for count in range(0, size + 1):
        for active in itertools.combinations(range(size), count):
            if active:
                constraint = sp.Matrix(
                    [[span[i, k] for k in range(span.cols)] for i in active]
                )
                coefficients = constraint.nullspace()
            else:
                coefficients = [
                    sp.Matrix([1 if k == j else 0 for k in range(span.cols)])
                    for j in range(span.cols)
                ]
            if not coefficients:
                continue
            candidate = span_matrix(
                [sp.expand(span * c) for c in coefficients], size
            )
            if candidate.rank() != 1:
                continue
            for column in range(candidate.cols):
                vector = sp.Matrix(
                    [candidate[i, column] for i in range(size)]
                )
                if zero(vector):
                    continue
                for sign in (1, -1):
                    trial = sp.expand(sign * vector)
                    if all(nonneg(entry) for entry in trial):
                        return trial
    return None


def hermiticity_rows(block: sp.Matrix) -> list:
    """Rows of "block is Hermitian identically in the mass", in the 64 moduli."""
    rows = []
    for i in range(block.rows):
        for j in range(i + 1, block.cols):
            defect = sp.expand(block[i, j] - block[j, i])
            if defect == 0:
                continue
            for coefficient in sp.Poly(defect, MASS).all_coeffs():
                coefficient = sp.expand(coefficient)
                if coefficient != 0:
                    rows.append([coefficient.coeff(v, 1) for v in COORDS])
    return rows


def rowspace(rows) -> sp.Matrix:
    if not rows:
        return sp.zeros(0, NCOORD)
    reduced, pivots = sp.Matrix(rows).rref()
    if not pivots:
        return sp.zeros(0, NCOORD)
    return sp.Matrix([list(reduced[k, :]) for k in range(len(pivots))])


# ---------------------------------------------------------------------------
# the certificate constants this runner is claiming
# ---------------------------------------------------------------------------
K_EDGE_COUNT = 16                         # the sixteen healed edges
DEAD_SLOTS = (1, 3, 4, 6)
LIVE_SLOTS = (0, 2, 5, 7)

# GROUP 1, the seam object and the Block 153 numerals
SEAM_ENTRIES = 8
THETA_DIAG_LIVE = 0
PRIME_DIAG_LIVE = 4
THETA_MOMENT_RANK = 4
PRIME_MOMENT_RANK = 6
THETA_MASS_RANK = 4
PRIME_MASS_RANK = 2
THETA_MASS_DIM = 4
PRIME_MASS_DIM = 6
ATLAS_THETA = (18, 46)
ATLAS_PRIME = (20, 44)
LIVE_SINGLETONS = 12
PRIME_PAIRS = 2
THETA_PAIRS = 4
LIVE_TRIPLES = 0
CLASS_COUNT = 14
TYPE_A_COUNT = 7
TYPE_B_COUNT = 7
TYPE_A_DIM = 4
TYPE_B_DIM = 2
CLASS_INERTIAS = ((0, 7, 1), (1, 6, 1), (1, 7, 0))
DEAD_SINGLETONS = ((0, 0), (0, 1), (1, 0), (1, 1))

# TIER 1
TIER1_PSD_CLASSES = 7
WITNESS_EDGE = (0, 2)
WITNESS_SUPPORT = 12
WITNESS_MOMENTS = (-1, 0, -1, 0, 1, 0, 1, 0)
WITNESS_INERTIA = (4, 4, 0)
CLASS_RANK = 16
CLASS_KERNEL = 48
ESCAPE_RANK = 20
ESCAPE_DIM = 44
ESCAPE_CODIM = 4
ALT_SUPPORT = 16
ALT_COUPLING_RANK = 4
ALT_INERTIA = (4, 0, 4)
B148_HERMITIAN_EDGES = 0

# TIER 2
LOCK_ROWS_PER_EDGE = 4
LOCK_ROWS_PAIR_CLASS = 8
LOCK_POSITIVE_TERMS = 8
NEGATIVE_NORMALIZER_SINGLETONS = 6
NEGATIVE_NORMALIZER_CLASSES = 7
TYPE_A_MOMENTS = ("b_10", "b_12", "b_30", "b_32")
TYPE_B_MOMENTS = ("b_11", "b_13", "b_31", "b_33")
LOCK_TABLE = (
    (((0, 2),), R(-2)),
    (((0, 3),), R(3)),
    (((1, 2),), R(-2)),
    (((1, 3),), R(3)),
    (((2, 0),), R(2, 3)),
    (((2, 1),), R(2, 3)),
    (((2, 2),), R(1)),
    (((2, 3),), R(6, 11)),
    (((3, 0),), R(-3, 4)),
    (((3, 1),), R(-3, 4)),
    (((3, 2),), R(-6, 11)),
    (((3, 3),), R(-1)),
    (((2, 0), (2, 1)), R(2, 3)),
    (((3, 0), (3, 1)), R(-3, 4)),
)
FORCED_INERTIA = (2, 4, 2)
CONE_TAU = R(118, 9)
CONE_MOMENT = R(3, 8)
CONE_GRAM_DIAG = (
    R(3, 32), 0, R(3, 32), 0, 0, -R(3, 32), 0, -R(3, 32),
)
SWEEP_STRIDE = 5
SWEEP_FIELDS = 270
DEEP_SWEEP_FIELDS = 1350
SWEEP_INERTIA = (2, 4, 2)
SWEEP_PSD = 0

# the R2 counterpoint and the boundary corners
ZERO_CONNECTION_EDGES = 16
COUNTERPOINT_INERTIA = (4, 4, 0)
COUNTERPOINT_DIAG = (
    R(3, 32), 0, R(3, 32), 0, 0, R(3, 32), 0, R(3, 32),
)
SX_ZERO_HERMITIAN_EDGES = 0
ATLAS_TAU = R(3, 4)

# GROUP 2
INVOLUTION_PAIRS_R = ((0, 3), (1, 2), (4, 7), (5, 6))
INVOLUTION_PAIRS_S = ((0, 2), (1, 3), (4, 6), (5, 7))
L145_DIM = 4
L147_DIM = 4
L154_DIM = 6
KER_S_MINUS_DIM = 4
MEET_DIM = 2
CONSTRAINT_RANK = 6
SUBSPACE_SUM = 8
SIGN_SWEEP_SOLUTIONS = ((0, 0),)

# GROUP 3
CHANNEL_COUNT = 3
RAW_LIVE_SLOTS = 0
X0_TEN_SLOT_EDGES = ((2, 2), (3, 3))
X0_TWELVE_SLOT_EDGES = 14
X0_DEADLIVE_SLOTS = (10, 12)
PRIME_DEADLIVE_SLOTS = (16,)
RAW_PRIME_DEADLIVE = (8, 10)
ANTI_X0_ZERO_BLOCKS = 4
PRIME_SUPPORTS = (16, 20)
PRIME_PART_SUPPORTS = (32,)
X0_SUPPORTS = (20, 24)

RUNTIME_BUDGET_SEC = 150


# ---------------------------------------------------------------------------
# measured facts (computed once, before any mutation flag is consulted)
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Facts:
    main_head: str
    authority: AuthorityCertificate
    # calibration and provenance
    inertia_calibration: bool
    inertia_order_pinned: bool
    inertia_routes_agree: bool
    residue_routes_agree: bool
    half_block_convention: bool
    dead_live_partition: tuple
    k_real_antisymmetric: tuple
    # B: the seam residue object, the loci and the classes
    seam_numerals: tuple
    gram_structure: tuple
    psd_criterion: tuple
    mass_loci: tuple
    atlas_systems: tuple
    live_census: tuple
    class_split: tuple
    class_inertias: tuple
    # C: TIER 1
    tier1_classes: tuple
    tier1_witness: tuple
    tier1_full_pairing: tuple
    tier1_refinement: tuple
    tier1_cone_control: tuple
    # D: TIER 2
    cone_lemma: tuple
    lock_rows: tuple
    lock_table: tuple
    forced_inertia: tuple
    cone_witness: tuple
    cone_sweep: tuple
    deep_sweep: object
    boundary_corners: tuple
    # E: the counterpoint and the verdict
    zero_connection: tuple
    mechanism: tuple
    contrast: tuple
    comparison_correction: tuple
    # F: the transversality certificate
    involutions: tuple
    eigenspaces: tuple
    l154_structure: tuple
    meets: tuple
    meet_diagonals: tuple
    psd_kills_meets: tuple
    nesting: tuple
    # G: the Krein gate
    channels: tuple
    channel_controls: tuple
    block_census: tuple
    x0_deadlive_pin: tuple
    dead_dead: tuple
    anti_x0: tuple
    supports: tuple
    # global
    exact_no_float: bool
    scope: dict


def measure(deep: bool) -> Facts:
    main_head = git_output("rev-parse", "origin/main")
    authority = authority_certificate(main_head)

    # -----------------------------------------------------------------------
    # calibration, in the measurement pass, on matrices whose inertia is known
    # by inspection and on which the root-counting helper is provably wrong
    # -----------------------------------------------------------------------
    inertia_calibration = bool(
        congruence_inertia(sp.diag(1, 2, -3, R(5, 7))) == (3, 0, 1)
        and congruence_inertia(sp.diag(1, 1, -2, -2, 0)) == (2, 1, 2)
        and b142.inertia(sp.diag(1, 1, -2, -2, 0)) != (2, 1, 2)
    )
    inertia_order_pinned = bool(
        congruence_inertia(sp.diag(1, 1, 0, -1)) == (2, 1, 1)
        and congruence_inertia(sp.diag(1, 1, 1, 1, 0, 0, 0, 0)) == (4, 4, 0)
        and congruence_inertia(sp.diag(-1, -1, -1, -1, 0, 0, 0, 0)) == (0, 4, 4)
        and congruence_inertia(sp.zeros(8, 8)) == (0, 8, 0)
    )
    inertia_routes_agree = all(
        b144.congruence_inertia(probe) == b154.congruence_inertia(probe)
        for probe in (
            sp.diag(1, 1, 0, -1),
            sp.diag(R(3, 32), 0, R(3, 32), 0, 0, -R(3, 32), 0, -R(3, 32)),
        )
    )

    # -----------------------------------------------------------------------
    # the committed construction: the 16 healed edge actions and their residues
    # -----------------------------------------------------------------------
    differentials, star_form = b145.connection(SHEAR_X, SHEAR_T)
    edge = b145.edge_differentials(differentials, star_form, HEALING_WEIGHTS)
    action = {
        key: b145.quotient_action(edge[key], COVER_FREE, MASS)
        for key in EDGE_KEYS
    }
    residue = {
        key: sp.expand(action[key] - MASS * HQ_FREE) for key in EDGE_KEYS
    }

    residue_routes_agree = all(
        zero(sp.expand(residue[key] - b154.residue(edge[key])))
        for key in EDGE_KEYS
    )
    half_block_convention = zero(
        sp.expand(b154.half_block(HQ_FREE) - half(THETA_PRIME_OP, HQ_FREE))
    )
    dead_live_partition = (DEAD, LIVE, b154.DEAD, b154.LIVE)
    # K is REAL and ANTISYMMETRIC, so herm/anti (defined with the conjugate
    # transpose) coincide with the symmetric/antisymmetric parts and no
    # i-convention ambiguity enters Group 3 or the seam Gram.  Measured, because
    # the whole census below would silently swap channels if it were false.
    k_real_antisymmetric = (
        sum(
            1
            for key in EDGE_KEYS
            if all(sp.expand(sp.im(entry)) == 0 for entry in residue[key])
        ),
        sum(
            1
            for key in EDGE_KEYS
            if zero(sp.expand(residue[key] + residue[key].T))
        ),
        sum(
            1
            for key in EDGE_KEYS
            if MASS not in sp.expand(residue[key]).free_symbols
        ),
        sum(
            1
            for key in EDGE_KEYS
            if residue[key].shape == (PHYS, PHYS)
        ),
        tuple(sorted(NAMES)) == tuple(sorted(TYPE_A_MOMENTS + TYPE_B_MOMENTS)),
    )

    # -----------------------------------------------------------------------
    # B: the seam residue object, the mass-block loci, the classes
    # -----------------------------------------------------------------------
    raw_pairing = {
        "theta": half(THETA, HQ_FREE),
        "theta'": half(THETA_PRIME_OP, HQ_FREE),
    }
    gram = {name: herm(raw_pairing[name]) for name in raw_pairing}
    prime = gram["theta'"]

    def coefficient_rank(matrix, variables) -> int:
        rows = []
        for i in range(matrix.rows):
            for j in range(matrix.cols):
                entry = sp.expand(matrix[i, j])
                if entry != 0:
                    rows.append([entry.coeff(v, 1) for v in variables])
        return sp.Matrix(rows).rank() if rows else 0

    def diag_live(matrix) -> int:
        return sum(1 for k in range(HALF) if sp.expand(matrix[k, k]) != 0)

    seam_numerals = (
        (
            live_count(gram["theta"]),
            diag_live(gram["theta"]),
            gram["theta"].rank(),
            coefficient_rank(gram["theta"], ODD),
            sp.expand(sp.trace(gram["theta"])) == 0,
        ),
        (
            live_count(prime),
            diag_live(prime),
            prime.rank(),
            coefficient_rank(prime, ODD),
            sp.expand(sp.trace(prime)) == 0,
        ),
    )

    hyperbolic_u = sp.expand(prime[1, 3])
    hyperbolic_v = sp.expand(prime[4, 6])
    live_diagonal = tuple(sp.expand(prime[k, k]) for k in LIVE)
    gram_structure = (
        zero(sub_block(prime, DEAD, LIVE)),
        zero(sp.Matrix(4, 4, lambda i, j: sub_block(prime, LIVE, LIVE)[i, j]
                       if i != j else 0)),
        sp.expand(hyperbolic_u - (ODD[5] + ODD[7]) / 8) == 0,
        sp.expand(hyperbolic_v + (ODD[1] + ODD[3]) / 8) == 0,
        all(
            sp.expand(a - b) == 0
            for a, b in zip(
                live_diagonal,
                (ODD[4] / 4, ODD[6] / 4, -ODD[0] / 4, -ODD[2] / 4),
            )
        ),
        tuple(
            sp.expand(prime[k, k]) == 0 for k in DEAD
        ) == (True, True, True, True),
    )

    # THE EXACT PSD CRITERION, verified rather than asserted: the criterion says
    # PSD <=> both hyperbolic entries vanish and the live diagonal is
    # nonnegative.  Each clause is exercised on a probe carrier and read through
    # the committed inertia helper.
    def gram_at(values: dict) -> sp.Matrix:
        return sp.expand(prime.xreplace({v: values.get(str(v), 0) for v in ODD}))

    psd_criterion = (
        congruence_inertia(
            gram_at({"b_10": -1, "b_12": -1, "b_30": 1, "b_32": 1})
        ),
        congruence_inertia(gram_at({"b_31": 1, "b_33": 1})),
        congruence_inertia(gram_at({"b_11": 1, "b_13": 1})),
        congruence_inertia(
            gram_at({"b_10": 1, "b_12": 1, "b_30": 1, "b_32": 1})
        ),
        congruence_inertia(gram_at({})),
    )

    mass_locus = {}
    for name in ("theta", "theta'"):
        pairing = raw_pairing[name]
        conditions = [
            sp.expand(pairing[i, j] - pairing[j, i])
            for i in range(HALF)
            for j in range(i + 1, HALF)
        ]
        conditions = [c for c in conditions if c != 0]
        extra: set = set()
        for condition in conditions:
            extra |= condition.free_symbols - set(ODD)
        mass_locus[name] = (
            sp.Matrix([[c.coeff(v, 1) for v in ODD] for c in conditions])
            if conditions
            else sp.zeros(0, 8),
            len(conditions),
            not extra,
        )
    landed_locus = sp.Matrix(
        [
            [sp.expand(left - right).coeff(v, 1) for v in ODD]
            for left, right in b145.MASS_GRAM_LOCUS
        ]
    )
    prime_rowspace = sp.Matrix(
        [[0, 1, 0, -1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, -1]]
    )
    mass_loci = (
        (
            mass_locus["theta'"][1],
            mass_locus["theta'"][0].rank(),
            8 - mass_locus["theta'"][0].rank(),
            sp.Matrix.vstack(mass_locus["theta'"][0], prime_rowspace).rank()
            == 2,
            mass_locus["theta'"][2],
        ),
        (
            mass_locus["theta"][1],
            mass_locus["theta"][0].rank(),
            8 - mass_locus["theta"][0].rank(),
            sp.Matrix.vstack(mass_locus["theta"][0], landed_locus).rank()
            == landed_locus.rank() == 4,
            mass_locus["theta"][2],
        ),
    )

    per_edge: dict = {}
    raw_edge_rows: dict = {}
    system: dict = {}
    for name, operator in (("theta", THETA), ("theta'", THETA_PRIME_OP)):
        rows: list = []
        per_edge[name] = {}
        raw_edge_rows[name] = {}
        for key in EDGE_KEYS:
            edge_rows = hermiticity_rows(half(operator, action[key]))
            raw_edge_rows[name][key] = edge_rows
            per_edge[name][key] = rowspace(edge_rows)
            rows.extend(edge_rows)
        system[name] = sp.Matrix(rows)

    atlas_systems = []
    for name in ("theta", "theta'"):
        rank = system[name].rank()
        kernel = system[name].nullspace()
        atlas_systems.append(
            (
                rank,
                NCOORD - rank,
                len(kernel) == NCOORD - rank,
                all(v[i] == 0 for v in kernel for i in SHEAR_INDEX),
            )
        )
    atlas_systems = tuple(atlas_systems)

    stack_cache: dict = {}

    def stacked_rows(name, subset) -> sp.Matrix:
        key = (name, subset)
        if key not in stack_cache:
            blocks = [
                per_edge[name][k] for k in subset if per_edge[name][k].rows
            ]
            stack_cache[key] = (
                sp.Matrix.vstack(*blocks) if blocks else sp.zeros(0, NCOORD)
            )
        return stack_cache[key]

    def live_dim(name, subset) -> int:
        stack = stacked_rows(name, subset)
        if not stack.rows:
            return len(ODD)
        return sp.Matrix.vstack(stack, ODD_SELECTOR).rank() - stack.rank()

    def census(name):
        singles = tuple(k for k in EDGE_KEYS if live_dim(name, (k,)) > 0)
        pairs = tuple(
            s
            for s in itertools.combinations(singles, 2)
            if live_dim(name, s) > 0
        )
        # MONOTONICITY: adding edges only ADDS constraints, so a live subset has
        # only live subsets; a live triple therefore needs all three of its
        # pairs live, which is what bounds the search (H9-156).
        candidates = tuple(
            s
            for s in itertools.combinations(singles, 3)
            if all(p in pairs for p in itertools.combinations(s, 2))
        )
        triples = tuple(s for s in candidates if live_dim(name, s) > 0)
        return singles, pairs, triples, len(candidates)

    prime_singles, prime_pairs, prime_triples, prime_candidates = census(
        "theta'"
    )
    theta_singles, theta_pairs, theta_triples, theta_candidates = census(
        "theta"
    )
    dead_singletons = tuple(k for k in EDGE_KEYS if k not in prime_singles)
    live_census = (
        (len(prime_singles), len(prime_pairs), len(prime_triples)),
        (len(theta_singles), len(theta_pairs), len(theta_triples)),
        prime_pairs,
        dead_singletons,
        dead_singletons == tuple(k for k in EDGE_KEYS if k not in theta_singles),
        all(
            all(live_dim("theta'", (k,)) > 0 for k in pair)
            for pair in prime_pairs
        ),
        (prime_candidates, theta_candidates),
        (
            len(prime_pairs)
            + len([k for k in prime_singles
                   if not any(k in p for p in prime_pairs)]),
            len(theta_pairs)
            + len([k for k in theta_singles
                   if not any(k in p for p in theta_pairs)]),
            b145.MAXIMAL_LIVE_COUNT,
        ),
    )

    classes = tuple((k,) for k in prime_singles) + prime_pairs
    image_cache: dict = {}

    def odd_image(name, subset):
        key = (name, subset)
        if key in image_cache:
            return image_cache[key]
        stack = stacked_rows(name, subset)
        if stack.rows:
            kernel = stack.nullspace()
        else:
            kernel = [
                sp.Matrix([1 if i == j else 0 for i in range(NCOORD)])
                for j in range(NCOORD)
            ]
        projected = [sp.Matrix([v[i] for i in ODD_INDEX]) for v in kernel]
        span = span_matrix(projected, len(ODD))
        basis: list = []
        if span.cols:
            reduced, pivots = span.T.rref()
            basis = [sp.Matrix(list(reduced[k, :])) for k in range(len(pivots))]
        image_cache[key] = basis
        return basis

    even_x_space = span_matrix([sp.eye(8)[:, j] for j in (0, 2, 4, 6)], 8)
    odd_x_space = span_matrix(
        [
            sp.Matrix([0, 1, 0, 1, 0, 0, 0, 0]),
            sp.Matrix([0, 0, 0, 0, 0, 1, 0, 1]),
        ],
        8,
    )

    type_a: list = []
    type_b: list = []
    class_inertia: set = set()
    class_psd: dict = {}
    for subset in classes:
        basis = odd_image("theta'", subset)
        space = span_matrix(basis, 8)
        if same_space(space, even_x_space):
            type_a.append(subset)
        elif same_space(space, odd_x_space):
            type_b.append(subset)
        for column in range(space.cols):
            for sign in (1, -1):
                probe = {
                    ODD[i]: sp.expand(sign * space[i, column]) for i in range(8)
                }
                class_inertia.add(
                    congruence_inertia(sp.expand(prime.xreplace(probe)))
                )
        # the exhaustive PSD decision on this class: intersect V with the two
        # PSD equalities, then enumerate the extreme rays of the live diagonal
        equalities = sp.Matrix(
            [[0, 1, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1]]
        )
        coefficients = (
            sp.expand(equalities * space).nullspace() if space.cols else []
        )
        cut = (
            span_matrix([sp.expand(space * c) for c in coefficients], 8)
            if coefficients
            else sp.zeros(8, 0)
        )
        live_basis = []
        if cut.cols:
            live_map = sp.Matrix(
                [
                    [cut[4, c] for c in range(cut.cols)],
                    [cut[6, c] for c in range(cut.cols)],
                    [-cut[0, c] for c in range(cut.cols)],
                    [-cut[2, c] for c in range(cut.cols)],
                ]
            )
            live_basis = [live_map[:, c] for c in range(live_map.cols)]
        ray = orthant_ray(live_basis) if live_basis else None
        class_psd[subset] = ray is not None

    type_a = tuple(type_a)
    type_b = tuple(type_b)
    class_split = (
        len(classes),
        len(type_a),
        len(type_b),
        len(type_a) + len(type_b) == len(classes),
        span_matrix(odd_image("theta'", type_a[0]), 8).rank() if type_a else 0,
        span_matrix(odd_image("theta'", type_b[0]), 8).rank() if type_b else 0,
        all(
            same_space(span_matrix(odd_image("theta'", s), 8), even_x_space)
            for s in type_a
        ),
        all(
            same_space(span_matrix(odd_image("theta'", s), 8), odd_x_space)
            for s in type_b
        ),
        all(
            zero(sp.expand(mass_locus["theta'"][0]
                           * span_matrix(odd_image("theta'", s), 8)))
            for s in classes
        ),
    )
    class_inertias = tuple(sorted(class_inertia))

    # -----------------------------------------------------------------------
    # C: TIER 1, the LINEAR 64-modulus relaxation
    # -----------------------------------------------------------------------
    tier1_classes = (
        sum(1 for s in classes if class_psd[s]),
        len(classes),
        tuple(sorted(s for s in classes if class_psd[s])) == tuple(sorted(type_a)),
        sum(1 for s in type_b if class_psd[s]),
    )

    target = sp.Matrix(list(WITNESS_MOMENTS))
    witness_rows = stacked_rows("theta'", (WITNESS_EDGE,))
    witness_system = sp.Matrix.vstack(witness_rows, ODD_SELECTOR)
    solution, parameters = witness_system.gauss_jordan_solve(
        sp.Matrix.vstack(sp.zeros(witness_rows.rows, 1), target)
    )
    witness_vector = sp.expand(
        solution.xreplace({p: 0 for p in parameters})
    )
    witness = {COORDS[i]: sp.expand(witness_vector[i]) for i in range(NCOORD)}
    witness_block = sp.expand(
        half(THETA_PRIME_OP, action[WITNESS_EDGE]).xreplace(witness)
    )
    witness_gram = sp.expand(prime.xreplace(witness))
    tier1_witness = (
        sum(1 for value in witness.values() if value != 0),
        tuple(sp.expand(witness[v]) for v in ODD),
        zero(sp.expand(witness_block - witness_block.T)),
        tuple(sp.expand(witness_gram[k, k]) for k in range(HALF)),
        congruence_inertia(witness_gram),
        live_count(witness_gram) > 0,
    )

    prime_residue_half = {
        key: half(THETA_PRIME_OP, residue[key]) for key in EDGE_KEYS
    }
    witness_connection = sp.expand(
        herm(prime_residue_half[WITNESS_EDGE]).xreplace(witness)
    )
    witness_full = sp.expand(witness_gram + witness_connection)
    tier1_full_pairing = (
        live_count(witness_connection),
        congruence_inertia(witness_full),
        sub_block(witness_connection, DEAD, LIVE).rank(),
    )

    # REFINEMENT R1: the escape is CARRIER-SPECIAL.  Quantified by the codimension
    # of the escape locus inside the class kernel, and exhibited by an ALTERNATE
    # carrier on the SAME class with the SAME odd moments at the SAME shear
    # ratio, reached by walking the odd-moment-preserving kernel until the
    # DEAD-LIVE coupling block has full rank.
    unit_tau = {SHEAR_X: sp.Integer(1), SHEAR_T: sp.Integer(1)}
    class_rows = sp.expand(sp.Matrix(raw_edge_rows["theta'"][WITNESS_EDGE]))
    class_rows_unit = sp.expand(class_rows.xreplace(unit_tau))
    connection_rows = []
    connection_block = herm(prime_residue_half[WITNESS_EDGE])
    for i in range(HALF):
        for j in range(HALF):
            entry = sp.expand(connection_block[i, j])
            if entry != 0:
                connection_rows.append([entry.coeff(v, 1) for v in COORDS])
    escape_system = sp.Matrix.vstack(class_rows, sp.Matrix(connection_rows))
    preserving = sp.Matrix.vstack(class_rows_unit, ODD_SELECTOR)
    unit_solution, unit_parameters = preserving.gauss_jordan_solve(
        sp.Matrix.vstack(sp.zeros(class_rows_unit.rows, 1), target)
    )
    base = sp.expand(unit_solution.xreplace({p: 0 for p in unit_parameters}))
    connection_unit = sp.expand(
        herm(prime_residue_half[WITNESS_EDGE]).xreplace(unit_tau)
    )

    def coupling_rank(vector) -> int:
        point = {COORDS[i]: sp.expand(vector[i]) for i in range(NCOORD)}
        return sub_block(
            sp.expand(connection_unit.xreplace(point)), DEAD, LIVE
        ).rank()

    accumulated = sp.zeros(NCOORD, 1)
    current = coupling_rank(sp.expand(base))
    for direction in preserving.nullspace():
        trial = sp.expand(accumulated + direction)
        rank = coupling_rank(sp.expand(base + trial))
        if rank > current:
            accumulated, current = trial, rank
        if current == ALT_COUPLING_RANK:
            break
    alternate_vector = sp.expand(base + accumulated)
    alternate = {
        COORDS[i]: sp.expand(alternate_vector[i]) for i in range(NCOORD)
    }
    alternate_connection = sp.expand(connection_unit.xreplace(alternate))
    alternate_gram = sp.expand(prime.xreplace(alternate))
    tier1_refinement = (
        class_rows.rank(),
        NCOORD - class_rows.rank(),
        escape_system.rank(),
        NCOORD - escape_system.rank(),
        escape_system.rank() - class_rows.rank(),
        sum(1 for value in alternate.values() if value != 0),
        zero(sp.expand(class_rows_unit * alternate_vector)),
        zero(sp.expand(alternate_gram - witness_gram)),
        sub_block(alternate_connection, DEAD, LIVE).rank(),
        congruence_inertia(sp.expand(alternate_gram + alternate_connection)),
        # the inertia LAW behind both readings: [[0, B], [B^T, D]] with D
        # positive definite has inertia (4, 4 - rank B, rank B)
        congruence_inertia(sp.expand(alternate_gram + alternate_connection))
        == (4, 4 - sub_block(alternate_connection, DEAD, LIVE).rank(),
            sub_block(alternate_connection, DEAD, LIVE).rank()),
    )

    escape_point = b147.modulus_point(b148.escape_witness_field())
    escape_vector = sp.Matrix(
        [sp.expand(escape_point[v]) for v in COORDS]
    )
    escape_gram = sp.expand(prime.xreplace(escape_point))
    tier1_cone_control = (
        sum(
            1
            for key in EDGE_KEYS
            if zero(sp.expand(stacked_rows("theta'", (key,)) * escape_vector))
        ),
        b145.in_admissible_cone(b148.escape_witness_field()),
        congruence_inertia(escape_gram),
        live_count(escape_gram) > 0,
    )

    # -----------------------------------------------------------------------
    # D: TIER 2, the committed admissible cone
    # -----------------------------------------------------------------------
    sigma, volume = sp.symbols("sigma nu", real=True)
    cell = b145.moduli_from_field({(0, 0): (sigma, volume)})
    cone_lemma = (
        sp.simplify(cell[0][(0, 0)] - volume) == 0,
        sp.simplify(cell[1][(0, 0)] - volume / (1 - sigma ** 2)) == 0,
        sp.simplify(cell[2][(0, 0)] + volume * sigma / (1 - sigma ** 2)) == 0,
        sp.simplify(cell[3][(0, 0)] - 1 / volume) == 0,
        b145.in_admissible_cone({c: (R(1, 3), sp.Integer(3)) for c in CELLS}),
        not b145.in_admissible_cone({c: (R(1, 3), sp.Integer(-1)) for c in CELLS}),
    )

    def lock_rows_of(key):
        """The lock rows of one healed edge, read from the RAW per-edge rows.

        A lock row couples a strictly positive cone sum to ONE odd moment:
        every non-shear coefficient equal to a single shared multiple of s_t,
        and exactly one shear coefficient, a multiple of s_x.  Nothing is
        assumed about which rows those are -- the shape is measured.
        """
        found = []
        for row in raw_edge_rows["theta'"][key]:
            positive = [i for i in NON_SHEAR_INDEX if sp.expand(row[i]) != 0]
            shears = [
                i
                for i in range(NCOORD)
                if str(COORDS[i]).startswith("b_") and sp.expand(row[i]) != 0
            ]
            if not positive or len(shears) != 1:
                continue
            normalizers = {
                sp.simplify(sp.expand(row[i]) / SHEAR_T) for i in positive
            }
            if len(normalizers) != 1:
                continue
            normalizer = normalizers.pop()
            if normalizer == 0 or normalizer.free_symbols:
                continue
            coefficient = sp.nsimplify(
                sp.simplify(sp.expand(row[shears[0]]) / (normalizer * SHEAR_T * TAU))
            )
            found.append(
                (
                    len(positive),
                    normalizer,
                    coefficient,
                    str(COORDS[shears[0]]),
                    all(
                        not str(COORDS[i]).startswith("b_") for i in positive
                    ),
                    len(set(positive)) == len(positive),
                )
            )
        return found

    edge_locks = {key: lock_rows_of(key) for key in prime_singles}
    lock_report = []
    negative_singletons = 0
    negative_classes = 0
    for subset in classes:
        rows = [row for key in subset for row in edge_locks[key]]
        coefficients = {row[2] for row in rows}
        normalizers = {row[1] for row in rows}
        moments = tuple(sorted({row[3] for row in rows}))
        if any(value < 0 for value in normalizers):
            negative_classes += 1
            if len(subset) == 1:
                negative_singletons += 1
        lock_report.append(
            (
                subset,
                len(rows),
                len(rows) == LOCK_ROWS_PER_EDGE * len(subset),
                tuple(sorted(coefficients, key=str)),
                moments,
                all(row[0] == LOCK_POSITIVE_TERMS for row in rows),
                all(row[4] and row[5] for row in rows),
            )
        )
    lock_rows = (
        tuple(len(edge_locks[key]) for key in prime_singles)
        == tuple([LOCK_ROWS_PER_EDGE] * len(prime_singles)),
        all(entry[2] for entry in lock_report),
        all(entry[5] for entry in lock_report),
        all(entry[6] for entry in lock_report),
        tuple(
            entry[1] for entry in lock_report if len(entry[0]) == 2
        ) == (LOCK_ROWS_PAIR_CLASS, LOCK_ROWS_PAIR_CLASS),
        negative_singletons,
        negative_classes,
    )
    lock_table = tuple(
        (entry[0], entry[3][0] if len(entry[3]) == 1 else entry[3], entry[4])
        for entry in lock_report
    )

    # THE SIGN LOCK's consequence, computed on the forced shape rather than
    # argued: with every locked moment sharing one sign, TYPE A's live diagonal
    # carries two entries of each sign and TYPE B's two hyperbolic entries are
    # both live.  Both signs are exercised.
    def forced_gram(kind: str, sign: int) -> sp.Matrix:
        value = sp.Integer(sign)
        if kind == "A":
            values = {"b_10": value, "b_12": value,
                      "b_30": value, "b_32": value}
        else:
            values = {"b_11": value, "b_13": value,
                      "b_31": value, "b_33": value}
        return sp.expand(
            prime.xreplace({v: values.get(str(v), 0) for v in ODD})
        )

    forced_inertia = (
        congruence_inertia(forced_gram("A", 1)),
        congruence_inertia(forced_gram("A", -1)),
        congruence_inertia(forced_gram("B", 1)),
        congruence_inertia(forced_gram("B", -1)),
        live_count(forced_gram("A", 1)) > 0,
        live_count(forced_gram("B", 1)) > 0,
    )

    cone_field = {}
    for time_index in range(4):
        for space_index in range(4):
            if space_index % 2 == 1:
                cone_field[(time_index, space_index)] = (
                    sp.Integer(0), sp.Integer(1)
                )
            elif time_index % 2 == 0:
                cone_field[(time_index, space_index)] = (
                    R(1, 3), sp.Integer(3)
                )
            else:
                cone_field[(time_index, space_index)] = (
                    R(-1, 3), sp.Integer(1)
                )
    cone_substitution = {
        SHEAR_X: sp.numer(CONE_TAU), SHEAR_T: sp.denom(CONE_TAU)
    }
    cone_hodge = b145.cover_hodge_from_field(cone_field)
    cone_point = b147.modulus_point(cone_field)
    cone_block = half(
        THETA_PRIME_OP,
        b145.quotient_action(
            sp.expand(edge[WITNESS_EDGE].xreplace(cone_substitution)),
            cone_hodge,
            MASS,
        ),
    )
    cone_gram = sp.expand(prime.xreplace(cone_point))
    cone_witness = (
        b145.in_admissible_cone(cone_field),
        zero(sp.expand(cone_block - cone_block.T)),
        tuple(sp.expand(cone_point[v]) for v in ODD),
        tuple(sp.expand(cone_gram[k, k]) for k in range(HALF)),
        congruence_inertia(cone_gram),
        cone_gram.rank(),
        sp.nsimplify(CONE_TAU),
    )

    # the EXACT-RATIONAL structured cone sample.  Corroboration for the symbolic
    # lock, never itself the proof.  Feasibility asks for ONE consistent
    # tau = s_x / s_t across every connection row of an edge, after the
    # connection-free mass rows are satisfied at the carrier.
    constant_part: dict = {}
    time_part: dict = {}
    space_part: dict = {}
    for key in EDGE_KEYS:
        matrix = sp.Matrix(raw_edge_rows["theta'"][key])
        constant_part[key] = sp.Matrix(
            matrix.rows,
            NCOORD,
            lambda i, j: sp.expand(matrix[i, j]).subs(
                {SHEAR_X: 0, SHEAR_T: 0}
            ),
        )
        time_part[key] = sp.Matrix(
            matrix.rows,
            NCOORD,
            lambda i, j: sp.expand(matrix[i, j]).coeff(SHEAR_T, 1),
        )
        space_part[key] = sp.Matrix(
            matrix.rows,
            NCOORD,
            lambda i, j: sp.expand(matrix[i, j]).coeff(SHEAR_X, 1),
        )

    def sweep_field(parameters) -> dict:
        """The x-parity structured cone family.

        At ODD x the cell data is one common (sigma, nu), which puts the field
        on the mass-block locus b_{t,1} = b_{t,3} and b_{t,3} = b_{t,1} by
        construction -- the connection-free rows of every per-edge system, so
        without it no edge is feasible at all.  At EVEN x the data depends on
        the time parity only.  The committed cone witness of Tier 2 is a member
        of this family, which is why the family is the one sampled.
        """
        odd_shear, odd_volume, even_a, volume_a, even_b, volume_b = parameters
        field = {}
        for time_index in range(4):
            for space_index in range(4):
                if space_index % 2 == 1:
                    field[(time_index, space_index)] = (odd_shear, odd_volume)
                elif time_index % 2 == 0:
                    field[(time_index, space_index)] = (even_a, volume_a)
                else:
                    field[(time_index, space_index)] = (even_b, volume_b)
        return field

    def grid(shears_odd, volumes_odd, shears_even, volumes_even) -> tuple:
        return tuple(
            itertools.product(
                shears_odd, volumes_odd,
                shears_even, volumes_even,
                shears_even, volumes_even,
            )
        )

    FAMILY_ONE = grid(
        (sp.Integer(0), R(1, 3), R(-1, 2)),
        (sp.Integer(1), sp.Integer(3)),
        (sp.Integer(0), R(1, 3), R(-1, 3), R(1, 2), R(-1, 2)),
        (sp.Integer(1), sp.Integer(3), R(1, 3)),
    )
    # the second grid, for the twice-verified --deep corroboration: no NONZERO
    # shear value and no volume value is shared with FAMILY_ONE
    FAMILY_TWO = grid(
        (sp.Integer(0), R(2, 5), R(-3, 4)),
        (sp.Integer(2), R(1, 5)),
        (sp.Integer(0), R(2, 5), R(-2, 5), R(3, 4), R(-3, 4)),
        (sp.Integer(2), sp.Integer(5), R(1, 5)),
    )

    def cone_sample(family, stride: int) -> tuple:
        feasible = nonzero = psd = 0
        seen: dict = {}
        edges_hit: set = set()
        ratios: set = set()
        sampled = family[::stride]
        count = len(sampled)
        for parameters in sampled:
            field = sweep_field(parameters)
            if not b145.in_admissible_cone(field):
                continue
            point = b147.modulus_point(field)
            vector = sp.Matrix([sp.expand(point[c]) for c in COORDS])
            sample_gram = sp.expand(prime.xreplace(point))
            gram_zero = zero(sample_gram)
            inertia = congruence_inertia(sample_gram)
            for key in EDGE_KEYS:
                if not zero(sp.expand(constant_part[key] * vector)):
                    continue
                time_values = sp.expand(time_part[key] * vector)
                space_values = sp.expand(space_part[key] * vector)
                ratio = None
                consistent = True
                for row in range(time_values.rows):
                    a, b = time_values[row], space_values[row]
                    if b == 0:
                        if a != 0:
                            consistent = False
                            break
                        continue
                    value = sp.nsimplify(-a / b)
                    if ratio is None:
                        ratio = value
                    elif ratio != value:
                        consistent = False
                        break
                if not consistent or ratio is None or ratio == 0:
                    continue
                feasible += 1
                edges_hit.add(key)
                ratios.add(ratio)
                if not gram_zero:
                    nonzero += 1
                    seen[inertia] = seen.get(inertia, 0) + 1
                    if inertia[2] == 0:
                        psd += 1
        return (
            count,
            feasible,
            nonzero,
            psd,
            tuple(sorted(seen.items(), key=str)),
            len(edges_hit),
            len(ratios),
        )

    cone_sweep = cone_sample(FAMILY_ONE, SWEEP_STRIDE)
    deep_sweep = None
    if deep:
        deep_sweep = (
            cone_sample(FAMILY_ONE, 1),
            cone_sample(FAMILY_TWO, 1),
        )

    # the two DEGENERATE corners the lock does not cover
    space_only = {SHEAR_T: sp.Integer(0)}
    time_only = {SHEAR_X: sp.Integer(0)}
    st_rows = sp.expand(
        sp.Matrix(raw_edge_rows["theta'"][WITNESS_EDGE]).xreplace(space_only)
    )
    st_kernel = st_rows.nullspace()
    st_free = sp.symbols("z0:%d" % len(st_kernel))
    st_point = sp.expand(
        sum(
            (f * v for f, v in zip(st_free, st_kernel)), sp.zeros(NCOORD, 1)
        )
    )
    st_gram = sp.expand(
        prime.xreplace({COORDS[i]: st_point[i] for i in range(NCOORD)})
    )
    sx_hermitian = 0
    for key in EDGE_KEYS:
        block = sp.expand(
            half(THETA_PRIME_OP, action[key]).xreplace(time_only).xreplace(
                cone_point
            )
        )
        if zero(sp.expand(block - block.T)):
            sx_hermitian += 1
    # the committed atlas point tau = 3/4 is NOT where either tier is evaluated:
    # the tier results are statements in the RATIO, and each admissible carrier
    # picks its own ratio from its own Hermiticity rows.  Both halves of that
    # disclosure are measured -- that the cone witness's ratio is not 3/4, and
    # that no normalization on (s_x, s_t) is imposed anywhere in the chain, the
    # two symbols entering the system as free symbols.
    boundary_corners = (
        zero(st_gram),
        span_matrix(
            [sp.Matrix([v[i] for i in ODD_INDEX]) for v in st_kernel], 8
        ).rank(),
        sx_hermitian,
        sp.nsimplify(ATLAS_TAU) != CONE_TAU,
        {SHEAR_X, SHEAR_T} <= system["theta'"].free_symbols,
        sp.simplify(
            (SHEAR_X ** 2 + SHEAR_T ** 2 - 1).xreplace(
                {SHEAR_X: sp.numer(CONE_TAU), SHEAR_T: sp.denom(CONE_TAU)}
            )
        ) != 0,
    )

    # -----------------------------------------------------------------------
    # E: the R2 COUNTERPOINT and the VERDICT
    # -----------------------------------------------------------------------
    flat = {SHEAR_X: sp.Integer(0), SHEAR_T: sp.Integer(0)}
    counterpoint_field = {}
    for time_index in range(4):
        for space_index in range(4):
            if space_index % 2 == 1:
                shear = sp.Integer(0)
            elif time_index == 1:
                shear = R(1, 3)
            elif time_index == 3:
                shear = R(-1, 3)
            else:
                shear = sp.Integer(0)
            counterpoint_field[(time_index, space_index)] = (
                shear, sp.Integer(1)
            )
    counterpoint_point = b147.modulus_point(counterpoint_field)
    counterpoint_gram = sp.expand(prime.xreplace(counterpoint_point))
    flat_hermitian = 0
    for key in EDGE_KEYS:
        block = sp.expand(
            half(THETA_PRIME_OP, action[key]).xreplace(flat).xreplace(
                counterpoint_point
            )
        )
        if zero(sp.expand(block - block.T)):
            flat_hermitian += 1
    zero_connection = (
        sum(
            1
            for key in EDGE_KEYS
            if zero(sp.expand(residue[key].xreplace(flat)))
        ),
        b145.in_admissible_cone(counterpoint_field),
        flat_hermitian,
        tuple(sp.expand(counterpoint_gram[k, k]) for k in range(HALF)),
        congruence_inertia(counterpoint_gram),
        live_count(counterpoint_gram) > 0,
    )

    theta_gram = gram["theta"]
    theta_classes = tuple((k,) for k in theta_singles) + theta_pairs
    theta_psd = 0
    for subset in theta_classes:
        basis = odd_image("theta", subset)
        space = span_matrix(basis, 8)
        if space.cols == 0:
            continue
        parameters_theta = sp.symbols("c0:%d" % space.cols, real=True)
        point = sp.expand(space * sp.Matrix(parameters_theta))
        restricted = sp.expand(
            theta_gram.xreplace({ODD[i]: sp.expand(point[i]) for i in range(8)})
        )
        # a PSD matrix whose whole diagonal vanishes IS zero, since each 2x2
        # principal minor becomes a negative square; both premises are measured
        # here class by class rather than assumed
        diagonal_dead = all(
            sp.expand(restricted[i, i]) == 0 for i in range(HALF)
        )
        if diagonal_dead and not zero(restricted):
            continue
        theta_psd += 1
    mechanism = (
        all(sp.expand(theta_gram[k, k]) == 0 for k in range(HALF)),
        sum(1 for k in range(HALF) if sp.expand(prime[k, k]) != 0),
        sp.expand(sp.trace(theta_gram)) == 0,
        sp.expand(sp.trace(prime)) != 0,
        theta_psd,
        len(theta_classes),
        # "theta's mechanism kills theta' too" -- MEASURED, and false
        all(sp.expand(prime[k, k]) == 0 for k in range(HALF)),
    )

    contrast = (
        orthant_ray([sp.eye(4)[:, j] for j in range(4)]) is not None,
        4,
        congruence_inertia(
            gram_at({"b_10": -1, "b_12": -1, "b_30": 1, "b_32": 1})
        ),
    )
    comparison_correction = (
        mass_loci[0][1],
        mass_loci[1][1],
        mass_loci[0][2],
        mass_loci[1][2],
        mass_loci[0][1] < mass_loci[1][1],
        mass_loci[0][2] > mass_loci[1][2],
    )

    # -----------------------------------------------------------------------
    # F: the TRANSVERSALITY CERTIFICATE
    # -----------------------------------------------------------------------
    def eq_rows(pairs, sign) -> sp.Matrix:
        return sp.Matrix(
            [
                [
                    (1 if k == i else 0) + sign * (1 if k == j else 0)
                    for k in range(8)
                ]
                for i, j in pairs
            ]
        )

    l145 = eq_rows(INVOLUTION_PAIRS_R, -1)
    l147 = eq_rows(INVOLUTION_PAIRS_R, +1)
    l154 = sp.Matrix(
        [[0, 1, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1]]
    )
    r_matrix = sp.zeros(8, 8)
    for i, j in INVOLUTION_PAIRS_R:
        r_matrix[i, j] = r_matrix[j, i] = 1
    s_matrix = sp.zeros(8, 8)
    for i, j in INVOLUTION_PAIRS_S:
        s_matrix[i, j] = s_matrix[j, i] = 1

    involutions = (
        zero(sp.expand(r_matrix * r_matrix - sp.eye(8))),
        zero(sp.expand(s_matrix * s_matrix - sp.eye(8))),
        zero(sp.expand(r_matrix * s_matrix - s_matrix * r_matrix)),
        zero(sp.expand(l154 * span_matrix(
            (s_matrix + sp.eye(8)).nullspace(), 8))),
    )

    plus_r = (r_matrix - sp.eye(8)).nullspace()
    minus_r = (r_matrix + sp.eye(8)).nullspace()
    eigenspaces = (
        span_matrix(plus_r, 8).rank(),
        span_matrix(minus_r, 8).rank(),
        zero(sp.expand(l145 * span_matrix(plus_r, 8))),
        zero(sp.expand(l147 * span_matrix(minus_r, 8))),
        8 - sp.Matrix.vstack(l145, l147).rank(),
        span_matrix(plus_r + minus_r, 8).rank(),
    )

    minus_s = (s_matrix + sp.eye(8)).nullspace()
    kill_odd_x = sp.Matrix(
        [[1 if k == j else 0 for k in range(8)] for j in (1, 3, 5, 7)]
    )
    even_x = kill_odd_x.nullspace()
    meet_of = sp.Matrix.vstack(
        sp.Matrix(
            [[s_matrix[i, k] + sp.eye(8)[i, k] for k in range(8)]
             for i in range(8)]
        ),
        kill_odd_x,
    ).nullspace()
    l154_structure = (
        8 - l154.rank(),
        span_matrix(minus_s, 8).rank(),
        span_matrix(even_x, 8).rank(),
        span_matrix(minus_s + even_x, 8).rank(),
        span_matrix(meet_of, 8).rank(),
        sp.Matrix.vstack(l154, s_matrix - sp.eye(8)).rank() > l154.rank(),
        zero(sp.expand(l154 * span_matrix(minus_s, 8))),
        zero(sp.expand(l154 * span_matrix(even_x, 8))),
    )

    meets = []
    meet_diagonals = []
    psd_kills = []
    p_symbol, q_symbol = sp.symbols("p q", real=True)
    for label, locus in (("L145", l145), ("L147", l147)):
        stacked = sp.Matrix.vstack(locus, l154)
        basis = stacked.nullspace()
        general = sp.expand(
            p_symbol * basis[0] + q_symbol * basis[1]
        )
        diagonal = (
            sp.expand(general[4]),
            sp.expand(general[6]),
            sp.expand(-general[0]),
            sp.expand(-general[2]),
        )
        meets.append(
            (
                label,
                stacked.rank(),
                8 - stacked.rank(),
                (8 - locus.rank()) + (8 - l154.rank()) - (8 - stacked.rank()),
            )
        )
        meet_diagonals.append(
            (
                label,
                tuple(str(entry) for entry in diagonal),
                sp.expand(diagonal[0] + diagonal[1]) == 0,
                sp.expand(diagonal[2] + diagonal[3]) == 0,
            )
        )
        # THREE INDEPENDENT ROUTES to "positivity kills this meet"
        ray = orthant_ray(
            [
                sp.Matrix([sp.expand(d).coeff(p_symbol, 1) for d in diagonal]),
                sp.Matrix([sp.expand(d).coeff(q_symbol, 1) for d in diagonal]),
            ]
        )
        elimination = sp.simplify(
            sp.And(*[sp.Ge(entry, 0) for entry in diagonal])
        )
        sweep_solutions = tuple(
            sorted(
                (a, b)
                for a in (-1, 0, 1)
                for b in (-1, 0, 1)
                if all(
                    sp.expand(entry.xreplace({p_symbol: a, q_symbol: b})) >= 0
                    for entry in diagonal
                )
            )
        )
        dead_at_origin = all(
            sp.expand(general[i].xreplace({p_symbol: 0, q_symbol: 0})) == 0
            for i in range(8)
        )
        psd_kills.append(
            (
                label,
                ray is None,
                elimination == sp.And(
                    sp.Eq(p_symbol, 0), sp.Eq(q_symbol, 0)
                ),
                sweep_solutions == SIGN_SWEEP_SOLUTIONS,
                dead_at_origin,
                zero(
                    sp.expand(
                        prime.xreplace(
                            {
                                ODD[i]: sp.expand(
                                    general[i].xreplace(
                                        {p_symbol: 0, q_symbol: 0}
                                    )
                                )
                                for i in range(8)
                            }
                        )
                    )
                ),
            )
        )
    meets = tuple(meets)
    meet_diagonals = tuple(meet_diagonals)
    psd_kills_meets = tuple(psd_kills)

    # TRANSVERSE, NEVER NESTED: measured pairwise, in both directions, for all
    # three loci.  Containment is decided by rank, U <= V iff stacking V's rows
    # on U's basis kills them.
    def contains(outer: sp.Matrix, inner: sp.Matrix) -> bool:
        basis = span_matrix(inner.nullspace(), 8)
        return basis.cols > 0 and zero(sp.expand(outer * basis))

    nesting = (
        any(
            contains(a, b)
            for a, b in itertools.permutations((l145, l147, l154), 2)
        ),
        contains(l147, l145),
        contains(l145, l147),
        contains(l154, l145),
        contains(l154, l147),
        contains(l145, l154),
    )

    # -----------------------------------------------------------------------
    # G: THE KREIN GATE, at BARE scope
    # -----------------------------------------------------------------------
    x0_residue_half = {key: half(X0, residue[key]) for key in EDGE_KEYS}
    anti_prime = {key: anti(prime_residue_half[key]) for key in EDGE_KEYS}
    herm_prime = {key: herm(prime_residue_half[key]) for key in EDGE_KEYS}
    herm_x0 = {key: herm(x0_residue_half[key]) for key in EDGE_KEYS}
    anti_x0_table = {key: anti(x0_residue_half[key]) for key in EDGE_KEYS}

    def edge_count(predicate) -> int:
        return sum(1 for key in EDGE_KEYS if predicate(key))

    channels = (
        edge_count(lambda k: zero(sub_block(herm_prime[k], LIVE, LIVE))),
        edge_count(lambda k: zero(sub_block(anti_prime[k], LIVE, LIVE))),
        edge_count(lambda k: zero(sub_block(herm_x0[k], LIVE, LIVE))),
        edge_count(lambda k: live_count(sub_block(
            prime_residue_half[k], LIVE, LIVE)) == 0),
    )
    channel_controls = (
        edge_count(lambda k: not zero(herm_x0[k])),
        edge_count(
            lambda k: bool(
                set().union(
                    *[sp.expand(e).free_symbols for e in herm_x0[k]]
                )
                & {SHEAR_X, SHEAR_T}
            )
        ),
        edge_count(lambda k: not zero(prime_residue_half[k])),
        edge_count(lambda k: live_count(sub_block(
            herm_prime[k], DEAD, LIVE)) == 16),
        edge_count(lambda k: live_count(sub_block(
            anti_prime[k], DEAD, LIVE)) == 16),
    )

    def census_of(table) -> tuple:
        return tuple(
            tuple(
                sorted(
                    {
                        live_count(sub_block(table[k], rows, cols))
                        for k in EDGE_KEYS
                    }
                )
            )
            for rows, cols in (
                (DEAD, DEAD), (DEAD, LIVE), (LIVE, DEAD), (LIVE, LIVE)
            )
        )

    block_census = (
        census_of(herm_prime),
        census_of(anti_prime),
        census_of(herm_x0),
        census_of(anti_x0_table),
        census_of(prime_residue_half),
    )
    x0_deadlive_pin = (
        tuple(
            sorted(
                key
                for key in EDGE_KEYS
                if live_count(sub_block(herm_x0[key], DEAD, LIVE)) == 10
            )
        ),
        edge_count(
            lambda k: live_count(sub_block(herm_x0[k], DEAD, LIVE)) == 12
        ),
        edge_count(
            lambda k: live_count(sub_block(herm_x0[k], DEAD, LIVE)) > 0
        ),
    )
    dead_dead = (
        edge_count(lambda k: zero(sub_block(anti_prime[k], DEAD, DEAD))),
        edge_count(lambda k: zero(sub_block(herm_prime[k], DEAD, DEAD))),
        # the Block 154 MASS residue really does live at DEAD x DEAD, so the
        # bonus is a contrast and not a restatement
        sp.expand(anti(half(THETA_PRIME_OP, HQ_FREE))[1, 3]) != 0,
        sp.expand(anti(half(THETA_PRIME_OP, HQ_FREE))[4, 6]) != 0,
    )
    anti_x0 = (
        sum(
            1
            for pair in ((DEAD, DEAD), (DEAD, LIVE), (LIVE, DEAD), (LIVE, LIVE))
            if all(
                zero(sub_block(anti_x0_table[k], pair[0], pair[1]))
                for k in EDGE_KEYS
            )
        ),
        edge_count(lambda k: zero(anti_x0_table[k])),
        edge_count(lambda k: not zero(x0_residue_half[k])),
    )
    supports = (
        tuple(sorted({live_count(prime_residue_half[k]) for k in EDGE_KEYS})),
        tuple(sorted({live_count(herm_prime[k]) for k in EDGE_KEYS})),
        tuple(sorted({live_count(anti_prime[k]) for k in EDGE_KEYS})),
        tuple(sorted({live_count(x0_residue_half[k]) for k in EDGE_KEYS})),
    )

    exact_no_float = no_float(
        (
            prime,
            witness_gram,
            witness_full,
            alternate_gram,
            alternate_connection,
            cone_gram,
            counterpoint_gram,
            escape_gram,
            sp.Matrix(list(CONE_GRAM_DIAG)),
            sp.Matrix(list(COUNTERPOINT_DIAG)),
        )
    )

    return Facts(
        main_head=main_head,
        authority=authority,
        inertia_calibration=inertia_calibration,
        inertia_order_pinned=inertia_order_pinned,
        inertia_routes_agree=inertia_routes_agree,
        residue_routes_agree=residue_routes_agree,
        half_block_convention=half_block_convention,
        dead_live_partition=dead_live_partition,
        k_real_antisymmetric=k_real_antisymmetric,
        seam_numerals=seam_numerals,
        gram_structure=gram_structure,
        psd_criterion=psd_criterion,
        mass_loci=mass_loci,
        atlas_systems=atlas_systems,
        live_census=live_census,
        class_split=class_split,
        class_inertias=class_inertias,
        tier1_classes=tier1_classes,
        tier1_witness=tier1_witness,
        tier1_full_pairing=tier1_full_pairing,
        tier1_refinement=tier1_refinement,
        tier1_cone_control=tier1_cone_control,
        cone_lemma=cone_lemma,
        lock_rows=lock_rows,
        lock_table=lock_table,
        forced_inertia=forced_inertia,
        cone_witness=cone_witness,
        cone_sweep=cone_sweep,
        deep_sweep=deep_sweep,
        boundary_corners=boundary_corners,
        zero_connection=zero_connection,
        mechanism=mechanism,
        contrast=contrast,
        comparison_correction=comparison_correction,
        involutions=involutions,
        eigenspaces=eigenspaces,
        l154_structure=l154_structure,
        meets=meets,
        meet_diagonals=meet_diagonals,
        psd_kills_meets=psd_kills_meets,
        nesting=nesting,
        channels=channels,
        channel_controls=channel_controls,
        block_census=block_census,
        x0_deadlive_pin=x0_deadlive_pin,
        dead_dead=dead_dead,
        anti_x0=anti_x0,
        supports=supports,
        exact_no_float=exact_no_float,
        scope=scope_certificate(raw_note()),
    )


# ---------------------------------------------------------------------------
# H. note scope
# ---------------------------------------------------------------------------
# PLACEHOLDER FENCE, a PLAIN SINGLE-LINE LITERAL.  The landing supervisor
# replaces this one line with the note's own N5 fence, byte for byte, by line
# replacement -- never by a join form.  Until then H-note-scope is a failing
# gate and the runner exits 1.
N5_FENCE = 'N5: per_element: THE THETA-PRIME SEAM RESIDUE SPLITS IN TWO TIERS. The 14 live carrier classes divide exactly 7 / 7 into TYPE A (surviving odd-moment space {b_11 = b_13 = b_31 = b_33 = 0}, DIMENSION 4, G\' a pure live diagonal) and TYPE B (DIMENSION 2, G\' purely the two hyperbolic DEAD blocks, and its per-edge system locks FOUR moments b_11, b_13, b_31, b_33, one per lock row, collapsing to two independent statements only because the class already forces b_11 = b_13 and b_31 = b_33).\nper_site: TIER 1, THE LINEAR 64-MODULUS RELAXATION: LIVE, AND IT IS A LINEAR-FAMILY STATEMENT AND NOT ACHIEVED PHYSICAL POSITIVITY -- 7 of the 14 classes carry a NONZERO POSITIVE SEMIDEFINITE seam Gram, with an exact-rational witness on the single healed edge (0,2) at inertia (4,4,0), 12 of 64 moduli nonzero, which is NOT cone-admissible and cannot be; REFINEMENT R1, DISPLAYED: the witness\'s stronger property, that the FULL bare pairing is positive semidefinite there because Herm([theta\' K]_++) vanishes at that carrier, is CARRIER-SPECIAL and not class-general -- the escape locus has DIMENSION 44 in the 48-dimensional class kernel, CODIMENSION 4, and an ALTERNATE carrier in the SAME class with the SAME odd moments and the SAME shear ratio puts the full bare pairing at (4,0,4), the inertia being (4, 4 - rank B, rank B) in the DEAD-LIVE coupling block B.\nper_mode: TIER 2, THE COMMITTED ADMISSIBLE CONE, UNDER THE HYPOTHESIS (s_x, s_t) != (0, 0): DEAD, BY A CONE SIGN LOCK -- four lock rows per edge, EIGHT for each of the two pair classes, of the shape P + c (s_x/s_t) b_k = 0 with P a sum of EIGHT DISTINCT n/a/m moduli, verified SHEAR-FREE, and c one nonzero rational shared by the four rows; the +1 coefficients hold only POST-NORMALIZATION by a shared factor measured NEGATIVE on 6 of the 12 live singleton classes (7 of 14 counting the pairs); on the cone every n, a and m modulus is strictly positive, so every locked moment is strictly nonzero with ONE COMMON SIGN where positivity needs two of each, inertia is FORCED to (2,4,2) on all 14 classes, and an admissible witness at s_x/s_t = 118/9 is exhibited with b_10 = b_12 = b_30 = b_32 = 3/8.\nper_block: THE COUNTERPOINT, THE BLOCK\'S SECOND THEOREM: at ZERO CONNECTION, s_x = s_t = 0, the residue K vanishes identically on 16 of 16 edges, the Hermiticity cut disappears, and an ADMISSIBLE cone field is Hermitian on 16 of 16 with G\' nonzero at inertia (4,4,0) -- POSITIVE SEMIDEFINITE. So on the committed cone THE RESIDUE POSITIVITY EXISTS EXACTLY WHERE THE CONNECTION DIES, which is the lane\'s central pattern at a third structural level; the other two corners degenerate differently and both are measured, s_x = 0 leaving the classes CONE-EMPTY and s_t = 0 leaving only the zero Gram.\nlattice_wide: THE TRANSVERSALITY CERTIFICATE AND THE KREIN GATE. L145 = ker(R-1) and L147 = ker(R+1) are the two eigenspaces of ONE involution at dimensions 4 and 4, complementary; L154 has dimension 6 and is NOT an S-eigenspace; both stacked CONSTRAINT ranks are 6, so both intersections are dimension 2 while both subspace SUMS are dimension 8; on both intersections the live diagonal is m/4 (q, -q, -p, p) up to sign, two entries of each sign, and THREE INDEPENDENT ROUTES -- extreme-ray enumeration, real QUANTIFIER ELIMINATION and a finite exact sign sweep -- all force p = q = 0, all eight odd moments zero and m G\' identically zero, so the three loci pairwise meet ONLY at the dead carrier and two search spaces are RETIRED. THE KREIN GATE, at BARE scope: anti([theta\' K]_++)[LIVE,LIVE] = 0 on 16/16 and Herm([X_0 K]_++)[LIVE,LIVE] = 0 on 16/16 with the object nonzero and shear-carrying on 16/16, joining Block 154\'s Hermitian channel at THREE CHANNELS, 16/16 EACH; the RAW [theta\' K]_++[LIVE,LIVE] carries 0 of 16 slots, stronger than the parts; BONUSES: anti([theta\' K]_++)[DEAD,DEAD] = 0 on 16/16, so Block 154\'s DEAD x DEAD anti-Hermitian residue is a MASS-block phenomenon that does not recur for K, and anti([X_0 K]_++) = 0 in all four blocks, so [X_0 K]_++ is HERMITIAN OUTRIGHT.\nRESULT: executing Block 155\'s next_trace_action, on the committed fixture and with every numeral RECOMPUTED: BLOCK 145\'S NEVER-POSITIVE-SEMIDEFINITE VERDICT SURVIVES for theta\' on the admissible cone with a live connection, but ITS MECHANISM DOES NOT TRANSFER -- theta\'s obstruction was structural, a traceless Gram with identically zero diagonal, while theta-prime has four live diagonal slots and a live trace and its obstruction is the CONE SIGN LOCK; the indefinite-metric route CLOSES AT ITS OWN PRE-COMMITTED GATE and the lane\'s central negative is STRENGTHENED to the BARE level, the connection being confined to the DEAD-LIVE sector coupling with no completion involved; and Block 153\'s recorded "dimension 2 against dimension 4" is CORRECTED -- those are RANKS, and as DIMENSIONS the mass-block Hermiticity loci are 6 (theta\') against 4 (theta), so the comparison INVERTS, recorded as a correction-in-successor because landed notes are never edited.\nDECISION_CUT: BANK ALL THREE GROUPS AND CONTINUE THE PIVOT. Neither tier is evaluated at the committed atlas shears tau = 3/4, the tier results being CONE-WIDE statements in the ratio with each admissible carrier picking its own tau, and s_x, s_t carry NO normalization; the runner\'s cone search is an exact-rational structured SAMPLE corroborating the symbolic lock and never the proof, and the disjoint checker\'s larger independent search is recorded as the CHECKER\'S sample; theta-prime IS NOT ADOPTED, Block 145\'s verdict is NOT retired, NOTHING is registered, and Block 154\'s FLAT-LIMIT CALIBRATION GAP IS UNTOUCHED BY THIS BLOCK AND CARRIES FORWARD AS AN OPEN DEFECT. NEXT: campaign contract D, the cutting-lane completions at strata 147+; then contract C, the frame-to-momentum map, whose incidence operator is a Gauss-law subsidiary condition.\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero.'

SCOPE_KEYS = (
    "two_tiers",
    "type_split",
    "type_b_four_moments",
    "tier_one_linear_family",
    "tier_one_not_physical_positivity",
    "witness_inertia",
    "carrier_special",
    "escape_codimension",
    "alternate_carrier_inertia",
    "cone_sign_lock",
    "eight_positive_moduli",
    "eight_lock_rows",
    "post_normalization",
    "r2_hypothesis",
    "forced_inertia",
    "admissible_witness",
    "zero_connection_counterpoint",
    "positivity_where_connection_dies",
    "cone_empty_corner",
    "verdict_survives",
    "mechanism_does_not_transfer",
    "rank_not_dimension",
    "correction_in_successor",
    "transversality",
    "one_involution",
    "constraint_rank_six",
    "quantifier_elimination",
    "retired_search_spaces",
    "krein_gate",
    "three_channels",
    "raw_live_block",
    "mass_block_phenomenon",
    "hermitian_outright",
    "x0_control_pin",
    "sample_not_proof",
    "atlas_shears_untested",
    "no_normalization",
    "checker_disclosures",
    "pivot",
    "calibration_gap",
    "independence_disclosure",
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
        "two_tiers": "two tiers" in note,
        "type_split": "type a" in note and "type b" in note,
        "type_b_four_moments": "four moments" in note,
        "tier_one_linear_family": "linear 64-modulus" in note,
        "tier_one_not_physical_positivity": (
            "not achieved physical positivity" in note
        ),
        "witness_inertia": "(4,4,0)" in compact,
        "carrier_special": "carrier-special" in note,
        "escape_codimension": "codimension 4" in note,
        "alternate_carrier_inertia": "(4,0,4)" in compact,
        "cone_sign_lock": "cone sign lock" in note,
        "eight_positive_moduli": "eight distinct" in note,
        "eight_lock_rows": "eight lock rows" in note or "eight for" in note,
        "post_normalization": "post-normalization" in note,
        # the hypothesis Tier 2 consumes, in every statement of the result
        "r2_hypothesis": "(s_x,s_t)!=(0,0)" in compact,
        "forced_inertia": "(2,4,2)" in compact,
        "admissible_witness": "118/9" in compact,
        "zero_connection_counterpoint": "zero connection" in note,
        "positivity_where_connection_dies": (
            "exactly where the connection dies" in note
        ),
        "cone_empty_corner": "cone-empty" in note,
        "verdict_survives": "verdict survives" in note,
        "mechanism_does_not_transfer": "mechanism does not transfer" in note,
        "rank_not_dimension": "rank comparison" in note,
        "correction_in_successor": "correction-in-successor" in note,
        "transversality": "transversality" in note,
        "one_involution": "one involution" in note,
        "constraint_rank_six": "constraint rank" in note,
        "quantifier_elimination": "quantifier elimination" in note,
        "retired_search_spaces": "retired" in note,
        "krein_gate": "krein" in note,
        "three_channels": "three channels" in note,
        "raw_live_block": "0 of 16 slots" in note,
        "mass_block_phenomenon": "mass-block phenomenon" in note,
        "hermitian_outright": "hermitian outright" in note,
        "x0_control_pin": "10 slots" in note,
        "sample_not_proof": "never the proof" in note,
        "atlas_shears_untested": "tau=3/4" in compact,
        "no_normalization": "no normalization" in note,
        "checker_disclosures": "checker" in note,
        "pivot": "pivot" in note,
        "calibration_gap": "calibration gap" in note,
        "independence_disclosure": "cross-context" in note,
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
        # NEGATIVE keys.  The note must NOT be written up as any kind of
        # priority claim about curved positivity; the gate greps the NORMALIZED
        # note, so the banned wording may not appear in the note even inside a
        # prohibition list, and the note describes it instead of spelling it.
        "no_priority_claim": (
            "first curved" not in note
            and "novel" not in note
            and "unprecedented" not in note
        ),
        # The LaTeX rho guard: a line-wrapped \rho leaves a stray "ho_" at the
        # start of a line and silently mangles a modulus name.
        "rho_guard": "\nho_" not in note_text,
    }


# ---------------------------------------------------------------------------
# claims: the only thing a mutation is allowed to touch
# ---------------------------------------------------------------------------
def build_claims(mutation: str) -> dict:
    claims: dict = {
        "main_head": CURRENT_MAIN,
        "parent_pin": "resolved",
        "prime_mass_dim": PRIME_MASS_DIM,
        "type_b_dim": TYPE_B_DIM,
        "witness_inertia": WITNESS_INERTIA,
        "escape_codim": ESCAPE_CODIM,
        "cone_psd_hits": SWEEP_PSD,
        "type_b_moments": TYPE_B_MOMENTS,
        "mechanism_transfers": False,
        "loci_nested": False,
        "intersection_dim": MEET_DIM,
        "gate_channels": (K_EDGE_COUNT, K_EDGE_COUNT, K_EDGE_COUNT),
        "anti_x0_zero_blocks": ANTI_X0_ZERO_BLOCKS,
        "required_scope_keys": SCOPE_KEYS,
    }
    if mutation == "stale_main_authority":
        claims["main_head"] = STALE_MAIN
    elif mutation == "stale_parent_authority":
        claims["parent_pin"] = "stale"
    elif mutation == "break_massblock_dimension":
        # the uncorrected reading of Block 153's comparison: rank read as a
        # dimension, which INVERTS the comparison
        claims["prime_mass_dim"] = THETA_MASS_DIM
    elif mutation == "break_class_split":
        claims["type_b_dim"] = TYPE_A_DIM
    elif mutation == "break_witness_inertia":
        claims["witness_inertia"] = FORCED_INERTIA
    elif mutation == "claim_full_pairing_class_general":
        # R1 denied: the Tier-1 escape asserted to be class-general
        claims["escape_codim"] = 0
    elif mutation == "claim_tier2_psd_exists":
        # a positive semidefinite cone hit asserted WITH a live connection
        claims["cone_psd_hits"] = 1
    elif mutation == "claim_lock_two_moments_typeB":
        claims["type_b_moments"] = ("b_13", "b_33")
    elif mutation == "claim_mechanism_transfers":
        claims["mechanism_transfers"] = True
    elif mutation == "claim_loci_nested":
        claims["loci_nested"] = True
    elif mutation == "break_intersection_dim":
        claims["intersection_dim"] = TYPE_A_DIM
    elif mutation == "claim_gate_witness_exists":
        claims["gate_channels"] = (
            K_EDGE_COUNT, K_EDGE_COUNT, K_EDGE_COUNT - 1
        )
    elif mutation == "break_hermitian_outright":
        claims["anti_x0_zero_blocks"] = 2
    elif mutation == "drop_zero_connection_counterpoint":
        # the R2 hypothesis and its counterpoint dropped from the note's
        # required scope; gate H catches the missing key
        claims["required_scope_keys"] = tuple(
            key
            for key in SCOPE_KEYS
            if key not in ("zero_connection_counterpoint", "r2_hypothesis")
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
            "docs/ADMISSIBILITY_DIRAC_KAHLER_RESIDUE_TRANSVERSALITY_GATE_BOUNDED_THEOREM_NOTE_2026-08-20.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_DISCRIMINATOR_VERDICT_BOUNDED_THEOREM_NOTE_2026-08-20.md",
            "scripts/admissibility_dirac_kahler_discriminator_verdict_2026_08_20.py",
        )
        and PARENT_ARTIFACTS == (BLOCK155_NOTE, BLOCK155_RUNNER)
        and len(PARENT_ARTIFACT_BLOBS) == len(PARENT_ARTIFACTS)
        and facts.main_head == claims["main_head"]
        and authority.fixed_authority
        and authority.parent_ref_and_ancestry
        and parent_blobs_ok
    )

    gate_b = bool(
        facts.inertia_calibration
        and facts.inertia_order_pinned
        and facts.inertia_routes_agree
        and facts.residue_routes_agree
        and facts.half_block_convention
        and facts.dead_live_partition
        == (DEAD_SLOTS, LIVE_SLOTS, DEAD_SLOTS, LIVE_SLOTS)
        and facts.k_real_antisymmetric
        == (
            K_EDGE_COUNT, K_EDGE_COUNT, K_EDGE_COUNT, K_EDGE_COUNT, True,
        )
        and facts.seam_numerals
        == (
            (SEAM_ENTRIES, THETA_DIAG_LIVE, HALF, THETA_MOMENT_RANK, True),
            (SEAM_ENTRIES, PRIME_DIAG_LIVE, HALF, PRIME_MOMENT_RANK, False),
        )
        and facts.gram_structure == (True,) * 6
        # the EXACT PSD criterion, exercised clause by clause through the
        # committed inertia helper rather than asserted
        and facts.psd_criterion
        == (
            WITNESS_INERTIA,
            (1, 6, 1),
            (1, 6, 1),
            FORCED_INERTIA,
            (0, HALF, 0),
        )
        and facts.mass_loci
        == (
            (2, PRIME_MASS_RANK, claims["prime_mass_dim"], True, True),
            (4, THETA_MASS_RANK, THETA_MASS_DIM, True, True),
        )
        and facts.atlas_systems
        == (
            (ATLAS_THETA[0], ATLAS_THETA[1], True, True),
            (ATLAS_PRIME[0], ATLAS_PRIME[1], True, True),
        )
        and facts.live_census
        == (
            (LIVE_SINGLETONS, PRIME_PAIRS, LIVE_TRIPLES),
            (LIVE_SINGLETONS, THETA_PAIRS, LIVE_TRIPLES),
            (((2, 0), (2, 1)), ((3, 0), (3, 1))),
            DEAD_SINGLETONS,
            True,
            True,
            (0, 0),
            (10, 8, b145.MAXIMAL_LIVE_COUNT),
        )
        and facts.class_split
        == (
            CLASS_COUNT,
            TYPE_A_COUNT,
            TYPE_B_COUNT,
            True,
            TYPE_A_DIM,
            claims["type_b_dim"],
            True,
            True,
            True,
        )
        and facts.class_inertias == CLASS_INERTIAS
        and facts.exact_no_float
    )

    gate_c = bool(
        facts.tier1_classes == (TIER1_PSD_CLASSES, CLASS_COUNT, True, 0)
        and facts.tier1_witness
        == (
            WITNESS_SUPPORT,
            WITNESS_MOMENTS,
            True,
            (R(1, 4), 0, R(1, 4), 0, 0, R(1, 4), 0, R(1, 4)),
            claims["witness_inertia"],
            True,
        )
        and facts.tier1_full_pairing == (0, WITNESS_INERTIA, 0)
        # REFINEMENT R1, gated: the escape is a CODIMENSION-4 sub-family of the
        # class, exhibited against an alternate carrier at (4,0,4)
        and facts.tier1_refinement
        == (
            CLASS_RANK,
            CLASS_KERNEL,
            ESCAPE_RANK,
            ESCAPE_DIM,
            claims["escape_codim"],
            ALT_SUPPORT,
            True,
            True,
            ALT_COUPLING_RANK,
            ALT_INERTIA,
            True,
        )
        # the Tier-1 / Tier-2 gap, controlled: the committed admissible-cone
        # escape witness satisfies the bare per-edge system NOWHERE
        and facts.tier1_cone_control
        == (B148_HERMITIAN_EDGES, True, WITNESS_INERTIA, True)
        and facts.exact_no_float
    )

    sweep_ok = (
        facts.cone_sweep[0] == SWEEP_FIELDS
        and facts.cone_sweep[1] > 0
        and facts.cone_sweep[2] > 0
        and facts.cone_sweep[3] == claims["cone_psd_hits"]
        and tuple(entry[0] for entry in facts.cone_sweep[4]) == (SWEEP_INERTIA,)
    )
    deep_ok = facts.deep_sweep is None or (
        len(facts.deep_sweep) == 2
        and all(
            sample[0] == DEEP_SWEEP_FIELDS
            and sample[1] > 0
            and sample[2] > 0
            and sample[3] == claims["cone_psd_hits"]
            and tuple(entry[0] for entry in sample[4]) == (SWEEP_INERTIA,)
            for sample in facts.deep_sweep
        )
    )
    gate_d = bool(
        facts.cone_lemma == (True,) * 6
        and facts.lock_rows
        == (
            True,
            True,
            True,
            True,
            True,
            NEGATIVE_NORMALIZER_SINGLETONS,
            NEGATIVE_NORMALIZER_CLASSES,
        )
        and facts.lock_table
        == tuple(
            (
                subset,
                coefficient,
                TYPE_A_MOMENTS
                if subset[0][0] % 2 == 0
                else claims["type_b_moments"],
            )
            for subset, coefficient in LOCK_TABLE
        )
        and facts.forced_inertia
        == (
            FORCED_INERTIA, FORCED_INERTIA, FORCED_INERTIA, FORCED_INERTIA,
            True, True,
        )
        and facts.cone_witness
        == (
            True,
            True,
            (CONE_MOMENT, 0, CONE_MOMENT, 0, CONE_MOMENT, 0, CONE_MOMENT, 0),
            CONE_GRAM_DIAG,
            FORCED_INERTIA,
            4,
            CONE_TAU,
        )
        and sweep_ok
        and deep_ok
        # the two degenerate corners, measured: s_t = 0 leaves only the zero
        # Gram, s_x = 0 leaves the classes cone-empty
        and facts.boundary_corners
        == (True, 0, SX_ZERO_HERMITIAN_EDGES, True, True, True)
        and facts.exact_no_float
    )

    gate_e = bool(
        facts.zero_connection
        == (
            ZERO_CONNECTION_EDGES,
            True,
            K_EDGE_COUNT,
            COUNTERPOINT_DIAG,
            COUNTERPOINT_INERTIA,
            True,
        )
        and facts.mechanism
        == (
            True,
            PRIME_DIAG_LIVE,
            True,
            True,
            0,
            K_EDGE_COUNT,
            claims["mechanism_transfers"],
        )
        and facts.contrast == (True, 4, WITNESS_INERTIA)
        # the Block 153 comparison correction: RANKS 2 against 4, DIMENSIONS 6
        # against 4, so the comparison inverts
        and facts.comparison_correction
        == (
            PRIME_MASS_RANK,
            THETA_MASS_RANK,
            PRIME_MASS_DIM,
            THETA_MASS_DIM,
            True,
            True,
        )
        and facts.exact_no_float
    )

    gate_f = bool(
        facts.involutions == (True, True, True, True)
        and facts.eigenspaces
        == (L145_DIM, L147_DIM, True, True, 0, SUBSPACE_SUM)
        and facts.l154_structure
        == (
            L154_DIM,
            KER_S_MINUS_DIM,
            4,
            L154_DIM,
            MEET_DIM,
            True,
            True,
            True,
        )
        and facts.meets
        == (
            ("L145", CONSTRAINT_RANK, claims["intersection_dim"], SUBSPACE_SUM),
            ("L147", CONSTRAINT_RANK, claims["intersection_dim"], SUBSPACE_SUM),
        )
        and facts.meet_diagonals
        == (
            ("L145", ("q", "-q", "-p", "p"), True, True),
            ("L147", ("-q", "q", "p", "-p"), True, True),
        )
        # THREE independent routes to the same kill, all gated
        and facts.psd_kills_meets
        == (
            ("L145", True, True, True, True, True),
            ("L147", True, True, True, True, True),
        )
        # the three loci are TRANSVERSE, never nested, measured pairwise in
        # both directions
        and facts.nesting
        == (claims["loci_nested"], False, False, False, False, False)
        and facts.exact_no_float
    )

    gate_g = bool(
        len(claims["gate_channels"]) == CHANNEL_COUNT
        and facts.channels[:CHANNEL_COUNT] == claims["gate_channels"]
        and facts.channels[3] == K_EDGE_COUNT
        and facts.channel_controls
        == (
            K_EDGE_COUNT, K_EDGE_COUNT, K_EDGE_COUNT,
            K_EDGE_COUNT, K_EDGE_COUNT,
        )
        and facts.block_census
        == (
            ((0,), PRIME_DEADLIVE_SLOTS, PRIME_DEADLIVE_SLOTS, (0,)),
            ((0,), PRIME_DEADLIVE_SLOTS, PRIME_DEADLIVE_SLOTS, (0,)),
            ((0,), X0_DEADLIVE_SLOTS, X0_DEADLIVE_SLOTS, (0,)),
            ((0,), (0,), (0,), (0,)),
            ((0,), RAW_PRIME_DEADLIVE, RAW_PRIME_DEADLIVE, (RAW_LIVE_SLOTS,)),
        )
        # the checker's exact pin, and a CORRECTION to the expected 16/16
        and facts.x0_deadlive_pin
        == (X0_TEN_SLOT_EDGES, X0_TWELVE_SLOT_EDGES, K_EDGE_COUNT)
        and facts.dead_dead == (K_EDGE_COUNT, K_EDGE_COUNT, True, True)
        and facts.anti_x0
        == (claims["anti_x0_zero_blocks"], K_EDGE_COUNT, K_EDGE_COUNT)
        and facts.supports
        == (
            PRIME_SUPPORTS,
            PRIME_PART_SUPPORTS,
            PRIME_PART_SUPPORTS,
            X0_SUPPORTS,
        )
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
            "widen the exact-rational structured cone sample to 1350 fields "
            "over all sixteen healed edges and repeat it on a second, disjoint "
            "block of the grid, so the corroboration of the sign lock is twice "
            "verified"
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
    print(f"  class split: {facts.class_split[0]} live classes, "
          f"{facts.class_split[1]} TYPE A at dim {facts.class_split[4]}, "
          f"{facts.class_split[2]} TYPE B at dim {facts.class_split[5]}; "
          f"inertia census {facts.class_inertias}")
    print(f"  TIER 1: {facts.tier1_classes[0]} of {facts.tier1_classes[1]} "
          f"classes nonzero PSD in the linear family; witness on edge "
          f"{WITNESS_EDGE} at {facts.tier1_witness[4]} with "
          f"{facts.tier1_witness[0]} of 64 moduli; full bare pairing "
          f"{facts.tier1_full_pairing[1]}")
    print(f"  R1: class rank {facts.tier1_refinement[0]}, kernel "
          f"{facts.tier1_refinement[1]}, escape dim "
          f"{facts.tier1_refinement[3]} at codimension "
          f"{facts.tier1_refinement[4]}; the alternate carrier "
          f"({facts.tier1_refinement[5]} moduli) has coupling rank "
          f"{facts.tier1_refinement[8]} and full pairing "
          f"{facts.tier1_refinement[9]}")
    print(f"  TIER 2: lock table {facts.lock_table}")
    print(f"  TIER 2: forced inertia {facts.forced_inertia[:4]}; cone witness "
          f"tau = {facts.cone_witness[6]} at {facts.cone_witness[4]}; "
          f"structured cone sample {facts.cone_sweep}")
    print(f"  R2 corners: zero connection {facts.zero_connection[:3]} at "
          f"{facts.zero_connection[4]}; s_x = 0 Hermitian on "
          f"{facts.boundary_corners[2]}/16; s_t = 0 Gram identically zero: "
          f"{facts.boundary_corners[0]}")
    print(f"  GROUP 2: meets {facts.meets}; diagonals {facts.meet_diagonals}; "
          f"three routes {facts.psd_kills_meets}")
    print(f"  GROUP 3: channels {facts.channels}; X_0 DEAD-LIVE pin "
          f"{facts.x0_deadlive_pin}; anti([X_0 K]_++) zero in "
          f"{facts.anti_x0[0]} of 4 blocks; supports {facts.supports}")
    if facts.deep_sweep is not None:
        print(f"  --deep cone samples: {facts.deep_sweep}")
    print()

    checks = Checks()
    checks.check(
        "A-authority",
        "main plus the committed Block 155 note and runner are content-bound, and Blocks 154/153/148/147/145/144 are reached through the Block 155 chain that its own gate A pins",
        gate_values["A"],
    )
    checks.check(
        "B-the-seam-residue-object-and-the-classes",
        "the theta-prime seam residue Gram G' = Herm([theta' H_q]_++) is BLOCK DIAGONAL -- DEAD-LIVE identically zero, LIVE-LIVE diagonal -- so its inertia is exactly the sum of two uncoupled hyperbolic 2x2 DEAD blocks, (b_31+b_33)/8 and -(b_11+b_13)/8, and the LIVE diagonal (b_30, b_32, -b_10, -b_12)/4, and the EXACT PSD criterion is exercised clause by clause through the committed Block 144 congruence helper rather than asserted; Block 153's numerals are RECOMPUTED, theta at coefficient rank 4 traceless with a dead diagonal against theta-prime at rank 6 with four live diagonal slots and a live trace, atlas-global Hermiticity at rank 18 kernel 46 against rank 20 kernel 44 with both kernels inside {b = 0}; the live census reproduces 12 singletons / 2 pairs / 0 triples for theta-prime and 12 / 4 / 0 for theta with the SAME four seam-killing single edges; and the 14 live carrier classes SPLIT EXACTLY 7 / 7, TYPE A at surviving dimension 4 with both hyperbolic blocks dead and TYPE B at surviving dimension 2 with the live diagonal dead, every class lying inside the theta-prime mass-block locus automatically",
        gate_values["B"],
    )
    checks.check(
        "C-tier-one-the-linear-relaxation",
        "IN THE LINEAR 64-MODULUS RELAXATION OF THE CARRIER FAMILY -- A LINEAR-FAMILY STATEMENT, NEVER ACHIEVED PHYSICAL POSITIVITY -- 7 of the 14 live classes carry a NONZERO POSITIVE SEMIDEFINITE seam Gram, decided by exhaustive extreme-ray enumeration whose empty return is a proof of emptiness, and exactly the 7 TYPE A classes do; an explicit exact-rational 64-modulus witness on the single healed edge (0,2), 12 moduli nonzero, makes the bare theta-prime half pairing Hermitian identically in the mass with G' = diag(1/4, 0, 1/4, 0, 0, 1/4, 0, 1/4) at inertia (4,4,0); AND REFINEMENT R1 IS GATED RATHER THAN BURIED -- the further property that the FULL bare pairing is positive semidefinite there, because Herm([theta' K]_++) vanishes at that carrier, is CARRIER-SPECIAL and not class-general: the escape locus has dimension 44 inside the 48-dimensional class kernel, CODIMENSION 4, and an ALTERNATE carrier on the SAME class with the SAME odd moments at the SAME shear ratio has DEAD-LIVE coupling rank 4 and full bare pairing at (4,0,4), the inertia obeying (4, 4 - rank B, rank B) exactly; the Tier-1 / Tier-2 gap is controlled by the committed Block 148 admissible-cone escape witness, which is in the cone and positive semidefinite but satisfies the bare per-edge Hermiticity system on 0 of 16 edges",
        gate_values["C"],
    )
    checks.check(
        "D-tier-two-the-cone-sign-lock",
        "ON THE COMMITTED ADMISSIBLE CONE, UNDER THE HYPOTHESIS (s_x, s_t) != (0, 0) WHICH IS EXACTLY WHAT THE LOCK CONSUMES, THERE IS NO POSITIVE SEMIDEFINITE SEAM GRAM: the cone lemma is re-derived from the committed b145.moduli_from_field, n = nu, a = nu/(1-sigma^2), m = 1/nu all STRICTLY POSITIVE and only b changing sign; every one of the 14 classes carries FOUR lock rows per edge -- EIGHT for each of the two pair classes -- of the shape P + c (s_x/s_t) b_k = 0 with P a sum of EIGHT DISTINCT n/a/m moduli, measured SHEAR-FREE, and one shared nonzero rational c per class, the +1 coefficients holding only POST-NORMALIZATION by a shared factor measured NEGATIVE on 6 of the 12 live singleton classes and 7 of the 14 classes; TYPE A locks b_10, b_12, b_30, b_32 and TYPE B locks FOUR moments b_11, b_13, b_31, b_33 one per row, not two; so every locked moment is strictly nonzero with one common sign where positivity needs two of each, and the inertia is FORCED to (2,4,2) at either sign on both types; an explicit ADMISSIBLE witness at s_x/s_t = 118/9 with b_10 = b_12 = b_30 = b_32 = 3/8 is exhibited, Hermitian on healed edge (0,2), nonzero, rank 4 and NOT positive semidefinite; an exact-rational STRUCTURED CONE SAMPLE corroborates the symbolic lock with every nonzero Gram at (2,4,2) and no positive semidefinite hit, and it is a SAMPLE and never the proof; and the two degenerate corners are measured, s_x = 0 leaving the classes CONE-EMPTY and s_t = 0 leaving only the zero Gram",
        gate_values["D"],
    )
    checks.check(
        "E-the-counterpoint-and-the-verdict",
        "AT ZERO CONNECTION THE POSITIVITY COMES BACK: with s_x = s_t = 0 the bare residue K vanishes identically on 16 of 16 healed edges, the Hermiticity cut disappears, and an ADMISSIBLE cone field is Hermitian on 16 of 16 with G' = diag(3/32, 0, 3/32, 0, 0, 3/32, 0, 3/32) NONZERO at inertia (4,4,0) -- POSITIVE SEMIDEFINITE -- so on the committed cone THE RESIDUE POSITIVITY EXISTS EXACTLY WHERE THE CONNECTION DIES, the lane's central pattern at a third structural level; AND THE VERDICT: Block 145's never-positive-semidefinite verdict SURVIVES for theta-prime on the cone with a live connection, but its MECHANISM DOES NOT TRANSFER -- theta's Gram has an identically zero diagonal and zero trace, so every off-diagonal 2x2 principal minor is a negative square and 0 of its 16 live classes can be nonzero and positive semidefinite, while theta-prime has FOUR live diagonal slots and a live trace, and with no sub-atlas Hermiticity cut its own positive semidefinite set is a nonempty 4-dimensional closed cone, so the obstruction comes entirely from the CUT; and Block 153's recorded comparison is CORRECTED, 2 against 4 being RANKS while the DIMENSIONS are 6 (theta-prime) against 4 (theta), which INVERTS the comparison",
        gate_values["E"],
    )
    checks.check(
        "F-the-transversality-certificate",
        "L145 = ker(R - 1) and L147 = ker(R + 1) for the SINGLE involution R: b_{t,x} -> b_{t,3-x}, at dimensions 4 and 4, meeting only at the origin and spanning the full 8-space -- COMPLEMENTARY; L154 has dimension 6, is NOT an eigenspace of S: x -> x+2 since it strictly contains ker(S+1), and decomposes as ker(S+1) + {b_11 = b_13 = b_31 = b_33 = 0} with the two meeting in dimension 2, so 4 + 4 - 2 = 6; both stacked CONSTRAINT ranks are 6, hence both intersections have dimension 2 while both subspace SUMS have dimension 8, and both readings are printed so the numeral cannot be misread; on both intersections the live diagonal is m/4 (q, -q, -p, p) and its sign-flipped variant, TWO ENTRIES OF EACH SIGN forced by construction, and THREE INDEPENDENT ROUTES agree that positivity kills them -- exhaustive extreme-ray enumeration returning nothing, real-domain QUANTIFIER ELIMINATION returning exactly p = 0 and q = 0, and a finite exact sign sweep leaving only the origin -- so all eight odd moments vanish and the completed pairing m G' is IDENTICALLY ZERO there: the three loci pairwise meet ONLY at the dead carrier, and the Block 145 live-seam locus and the Block 147 annealed locus are RETIRED as search spaces for Block 154 style positivity",
        gate_values["F"],
    )
    checks.check(
        "G-the-krein-gate-at-bare-scope",
        "THE INDEFINITE-METRIC ROUTE CLOSES AT ITS OWN PRE-COMMITTED GATE, which was connection visibility on the live sector: on all 16 healed edges, symbolically in the 64 moduli and in (s_x, s_t), anti([theta' K]_++)[LIVE,LIVE] = 0 on 16/16, Herm([X_0 K]_++)[LIVE,LIVE] = 0 on 16/16 and Block 154's Hermitian channel reproduces at 16/16 -- THREE CHANNELS, 16 OF 16 EACH, so the BARE connection has NO live-sector witness anywhere -- and the RAW block [theta' K]_++[LIVE,LIVE] carries 0 nonzero slots of 16 on every edge, which is strictly stronger than the three parts; the vanishing is a property of the LIVE-LIVE block and not of a dead object, with Herm([X_0 K]_++) itself nonzero and shear-carrying on 16/16 and every DEAD-LIVE block live on all 16 edges -- theta-prime at 16 of 16 slots and X_0 at 10 slots on exactly the two self-edges (2,2) and (3,3) and 12 on the other 14, which CORRECTS the expected 16/16 control to a theta-prime-specific figure; TWO BONUSES: anti([theta' K]_++)[DEAD,DEAD] = 0 on 16/16, so Block 154's DEAD x DEAD anti-Hermitian residue is a MASS-block phenomenon that does not recur for the connection residue, and anti([X_0 K]_++) vanishes in ALL FOUR blocks so [X_0 K]_++ is HERMITIAN OUTRIGHT on this carrier family; and K is measured REAL and ANTISYMMETRIC on 16 of 16, so no i-convention ambiguity enters any of these splits",
        gate_values["G"],
    )
    checks.check(
        "H-note-scope",
        "the two tiers with the linear-family caveat, the 7/7 type split with TYPE B's four locked moments, the (4,4,0) witness with its carrier-special codimension-4 refinement and the (4,0,4) alternate carrier, the cone sign lock with its eight distinct moduli and post-normalization caveat, the (s_x, s_t) != (0, 0) hypothesis carried in every statement, the forced (2,4,2), the 118/9 admissible witness, the zero-connection counterpoint and the cone-empty corner, the surviving verdict with the non-transferring mechanism, the rank-versus-dimension correction recorded as a correction-in-successor, the transversality certificate with its one involution and constraint rank and quantifier elimination and retired search spaces, the Krein gate with three channels and the 0-of-16-slots raw block and the mass-block-phenomenon bonus and the Hermitian-outright bonus and the 10-slot pin, the sample-not-proof and atlas-shear and no-normalization disclosures, the checker, the pivot, the calibration gap, the cross-context disclosure and the exact N5 fence are all present; the LaTeX rho guard holds; and no priority wording about curved positivity appears anywhere in the note, not even inside a prohibition list",
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
