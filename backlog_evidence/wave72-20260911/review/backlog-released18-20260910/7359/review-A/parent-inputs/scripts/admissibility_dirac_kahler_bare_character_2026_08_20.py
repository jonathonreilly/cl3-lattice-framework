#!/usr/bin/env python3
# Final path: scripts/admissibility_dirac_kahler_bare_character_2026_08_20.py
"""Block 153: THE BARE CHARACTER, and the canonical-operator question decided.

Block 149 closed its shear's-gauge classification by handing forward, as its own
named decision cut, the question Blocks 147/148 both inherited undecided: should
the ODD-x-CENTRED reflection theta' = (-1, 7, -1, 1) DISPLACE the canonical
theta = (-1, 7, -1, 0) as the lane's OS operator?  Block 148 had exhibited four
bare OS reflections and sixteen bare translations; Block 149 had counted 32 bare
moves, 16 half-preservers and their 8-element intersection, and had diagnosed its
threshold tier T5 = 4 as an ATLAS obstruction.  Nobody had said WHAT BARENESS IS.
This runner says it, in one character, and then decides the operator question on
the mechanism that character exposes:

  * BARENESS IS A CHARACTER, AND THE COUNTS ARE ITS KERNEL.  A covariant move
    (e, p, e, q) is BARE -- its transported chart differential matching a
    committed atlas entry with the IDENTITY gauge on ALL FOUR charts -- IF AND
    ONLY IF p + q IS EVEN, independently of the sign e.  kappa(e,p,e,q) =
    (p + q) mod 2 is a checked HOMOMORPHISM onto Z_2 on all 64 x 64 composites,
    so the bare set is ker kappa: an INDEX-2 SUBGROUP OF ORDER 32, 16
    translations and 16 reflections.  The gauge requirement is an exact
    DICHOTOMY with EMPTY OVERLAP -- bare moves admit exactly {I, r_t} on every
    one of the four charts, non-bare moves exactly {r_x, r_x r_t} -- and the
    geometric reading is that bare moves preserve the two DIAGONAL CHART CLASSES
    {(0,0),(1,1)} and {(0,1),(1,0)} setwise.  Every landed count reconciles
    against this one character: Block 148's FOUR bare OS reflections (the
    odd-centred ones) and SIXTEEN bare translations, Block 149's 32 / 16 / 8, and
    Block 149's threshold stabiliser T5 = the bare half-preserving translations,
    exactly four;
  * THE MECHANISM IS THE STAGGERED PARITY, AND IT IS THE SAME CHARACTER.  On all
    64 descended moves g X_0 = (-1)^kappa(g) X_0 g, 32 commuting and 32
    anticommuting with ZERO exceptions and zero moves satisfying the opposite
    sign -- so BARENESS AND X_0-COMMUTATION ARE ONE CHARACTER, not two facts.
    The carrier Hodge is X_0-EVEN (X_0 H_q X_0 = H_q, symbolically in all 64
    moduli) and the connection residue K = Q - m H_q is real, antisymmetric,
    m-FREE and X_0-ODD on all sixteen healed edges, because H_q is supported on
    EQUAL staggered parity and K on OPPOSITE.  Hence a one-line SELECTION RULE,
    proved for a GENERIC X_0-odd and a GENERIC X_0-even matrix and not merely
    for the two operators: X_0-ODD operators kill the H_q diagonal and keep the
    K diagonal; X_0-EVEN ones do the opposite; both converses are live at 8 of 8
    slots, so neither half is vacuous.  Block 147's structural zero diagonal --
    the migration theorem's core -- is therefore a ONE-LINE COROLLARY of theta
    being X_0-odd, and the refinement is carried: theta's K-diagonal is live on
    16 of 16 edges but in 4 OF 8 SLOTS, not 8;
  * THE QUENCHED CHAIN SURVIVES THE SWAP, WITH ONE CORRECTION TO THE FIRST
    CERTIFICATE.  The H_q-preservation defect is CARRIER-DEPENDENT, not a single
    number: rank 0 at the flat carrier, 8 at BOTH cone witnesses and 16 at the
    staircase and at a generic carrier, with COEFFICIENT RANK 14 against theta's
    16 -- so "theta' does not preserve H_q either" is true, and the honest
    statement is the coefficient rank, not a rank read at one carrier.  The
    Hermiticity necessity system has RANK 20 and KERNEL 44 under theta' against
    Block 145's reproduced 18 / 46; both kernels lie inside {b = 0} and both
    FORCE THE SEAM DEAD, so Block 145's verdict survives verbatim; and the two
    loci are INCOMPARABLE, not nested -- stacked rank 22, meet 42, span exactly
    the 48-dimensional shear-free stratum.  The shear-free residual moves 2 -> 4.
    The seam law is the same eight odd-time-slice moments for both, at MOMENT-
    COEFFICIENT RANK 6 with a LIVE TRACE for theta' against 4 and zero trace for
    theta -- coefficient rank, since both Grams have matrix rank 8;
  * THE DIAGONAL SPLIT IS THE DECIDING STRUCTURE, AND BOTH QUALIFIERS ARE
    CHECKED CERTIFICATES.  diag Herm([theta' Q]_{++}) = m diag G' on ALL SIXTEEN
    EDGES with NO SHEAR SYMBOLS ANYWHERE IN IT: the theta'-diagonal is PURE MASS
    GRAM and CONNECTION-FREE.  Under theta the same law is FALSE and the diagonal
    is m-FREE, connection-carried and live in 4 of 8 slots on every edge.
    QUALIFIER A: the chart-0/1 PSD forcing is rank 8 for both AT THE COMMITTED
    FIXTURE, but the two forcing determinants are DIFFERENT -- theta' reproduces
    Block 148's (s_t^2 + s_x^2)^6 (4 m^2 + s_t^2 + s_x^2)^2 / 2^48 while theta
    carries s_t^8 (2 m^2 + s_t^2)^4 / 2^48, which VANISHES ON s_t = 0, and at
    (s_x, s_t) = (3/5, 0) theta's forcing rank COLLAPSES TO 4 while theta' stays
    at 8.  QUALIFIER B: once the seam is dead the collapse claim is PSD-
    CONDITIONAL, not literal -- diag A' = 0 on 16/16 edges and PSD then forces
    A' = 0 on 16/16, but the LITERAL identical vanishing is 4 of 16 for BOTH
    operators, on exactly the four chart-0/1 edges.  Both readings are measured
    and both numbers are printed;
  * THE VERDICT IS THAT THETA' STRICTLY DOMINATES, AND THE COST IS A SEVEN-ITEM
    LEDGER.  The ONLY axis on which theta is larger is the atlas-global
    Hermiticity locus, 46 dimensions against 44 -- and that advantage is INERT:
    both loci sit inside {b = 0} where the mass Gram vanishes identically, and
    at an explicit theta-only kernel direction the theta pairing is m-FREE on all
    sixteen edges, so the two extra dimensions are two extra MASSLESS carriers.
    Against that theta' is bare, its diagonal is connection-free, its staircase
    census is UNIFORM (4,0,4) against theta's three-class census, its mass Gram
    can be PSD AND LIVE at a cone carrier -- inertia (4,4,0) at Block 148's
    escape witness -- whereas theta's zero diagonal makes every 2x2 principal
    minor a NEGATIVE SQUARE, so theta's Gram is never live-PSD at all.  Adoption
    is put to the owner as a PROPOSAL, with SEVEN landed constants restated, not
    three: 18 -> 20, 46 -> 44, 2 -> 4, the inertia census, the displayed pairing
    entry -19m/160 -> a m-FREE 7/320, the live-seam PAIR count 4 -> 2 with
    singletons 12 and triples 0 unchanged, and Block 147's migration core itself,
    whose zero diagonal becomes 4 live slots;
  * AND THE CONTRACT-B RIDER IS CONDITIONAL, WITH ITS COUNTEREXAMPLE EXHIBITED.
    Three connection-side completions IN THE STAGGERED-PARITY CLASS -- the
    coboundary w Omega*, a generic four-coefficient atlas-differential
    combination and a sign-flipped variant -- are all X_0-ODD and all move
    theta's diagonal in 4 of 8 slots while moving theta''s in ZERO.  A FULLY
    GENERIC 32x32 connection-side completion is NOT X_0-odd and moves BOTH
    diagonals in 8 of 8 slots.  So "completions cannot touch theta''s positivity
    diagonal" is TRUE WITHIN THE PARITY CLASS AND FALSE OUTSIDE IT, and it is
    stated with that restriction rather than as a theorem.

Every scientific comparison below is exact SymPy arithmetic; no floats anywhere;
the integer monotonic clock is used only for the runtime gate.

TOOLING DISCLOSURE: every inertia in this runner is computed by SYMMETRIC
CONGRUENCE, delegated to the committed Block 144 helper through the Block
148/147/145 import chain, so the tool this block reasons with is exactly the blob
gate A pins.  The Block 142/143 helper counts DISTINCT real roots and is unsound
on these degenerate spectra; it is deliberately not used, and the calibration
diag(1,1,-2,-2,0) is asserted in gate B.

PROVENANCE DISCLOSURE: the 64-modulus carrier model, the cover Hodge, the
antiperiodic quotient, the action law, the half pairing, the connection data, the
Block 141 healing weights, the canonical theta, the odd-centred theta', the
staggered parity X_0, the descent routine, the 64 covariant moves, the induced
modulus map, the four-chart atlas, the shift lifts and their gauges, the escape
witness and the cone carriers are ALL COMMITTED objects (Blocks
105/134/137/141/142/143/144/145/147/148), imported and never re-derived.  This
block adds only the bare character, the X_0 selection rule and its generic
theorem, the theta'-chain measurements, the diagonal split with its two
qualifiers, the adoption ledger and the completion-class rider.  This is CAMPAIGN
CONTRACT A -- the canonical-operator question -- executed as its own block; the
external literature on Osterwalder-Schrader reflections is REFERENCED nowhere and
BORROWED nowhere, and every statement below is re-proved in-framework.

HYPOTHESES, named and not imported: (H1) the pairing convention is [X Q]_{++} on
the half carrier {p = 0,1}, exactly as Blocks 142/144/145/147/148/149 used it.
(H2) an operator is BARE when its transported chart differential matches a
committed atlas entry with the IDENTITY gauge on ALL FOUR charts, exactly Block
148/149's `classify`.  (H3) "positive" is a statement about the HERMITIAN PART
A = (P + P^dagger)/2, as Block 148 established.  (H4) the carrier family is the
committed 64-modulus one and the physical cone is nu > 0, |sigma| < 1.  (H5) a
CONNECTION-SIDE COMPLETION is an additive perturbation of the healed edge
differential, and the STAGGERED-PARITY CLASS is those whose induced K-shift is
X_0-odd; the class membership is measured, never assumed.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import itertools
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

import admissibility_dirac_kahler_general_migration_theorem_2026_08_20 as b148

b147 = b148.b147
b145 = b148.b145
b144 = b148.b144
b143 = b148.b143
b142 = b148.b142
b141 = b148.b141
b137 = b148.b137
b134 = b148.b134
b105 = b148.b105

MASS = b148.MASS


NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_BARE_CHARACTER_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
BLOCK152_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SIGN_LAYER_COMPARISON_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
BLOCK152_RUNNER = (
    "scripts/admissibility_dirac_kahler_sign_layer_comparison_2026_08_20.py"
)
BLOCK149_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHEAR_GAUGE_CLASSIFICATION_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
BLOCK149_RUNNER = (
    "scripts/admissibility_dirac_kahler_shear_gauge_classification_2026_08_20.py"
)

# The four artifacts whose blobs are pinned at the parent commit.  All four are
# IN THIS WORKTREE, so plain worktree/commit blob pins suffice.
PARENT_ARTIFACTS = (
    BLOCK152_NOTE,
    BLOCK152_RUNNER,
    BLOCK149_NOTE,
    BLOCK149_RUNNER,
)
PARENT_ARTIFACT_BLOBS = (
    "64ec27be6cab21f3f774cec3ea432a4bcc633caa",   # Block 152 note
    "4a1259cc6d523d4bf6e6e25eab798262d4014291",   # Block 152 runner
    "04dbf031cc87b794c49ddef441ac24151d6fd7c9",   # Block 149 note
    "3d82fcff03d550bf56459cef038c61ee7e6c82f1",   # Block 149 runner
)

# Deliberately literal: this is the complete audit read surface.  Every entry is
# a WORKTREE-READABLE path; the cache envelope stats these, so an
# origin/main-only path here would break the audit (the Block 130 lesson,
# re-learned at the Block 150 landing and inherited through Blocks 151/152).
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_BARE_CHARACTER_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SIGN_LAYER_COMPARISON_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/admissibility_dirac_kahler_sign_layer_comparison_2026_08_20.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHEAR_GAUGE_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/admissibility_dirac_kahler_shear_gauge_classification_2026_08_20.py",
)

AUDIT_TIMEOUT_SEC = 600
# The five authority pins below are copied verbatim from the Block 152 runner's
# current values; the landing supervisor refreshes them against origin/main.
CURRENT_MAIN = "005f047923055e6ecd5dc8bce1ffd71765c2ffd8"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
# This block stacks on Block 152, so the parent branch is Block 152's.
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block152-sign-layer-comparison-20260820"
)
# Landing supervisor: replace this placeholder with the Block 152 branch tip.
# Until it is a 40-hex commit the pin is resolved through PARENT_REF when that
# ref exists and through HEAD otherwise (the parent branch may not be published
# yet); either way the binding is real and verifiable, and the immutable commit
# pin lands with the block.
PARENT_COMMIT = "a8d1e42217b573c1a4a77f9a0b164e1a3011ccc2"
# Block 151's tip: a real ancestor of HEAD that PREDATES both Block 152
# artifacts, so resolving the parent pin there leaves the Block 152 note and the
# Block 152 runner ABSENT while the two Block 149 artifacts still match.  It is
# the honest stale control FOR THIS PIN SET.  This pin is read ONLY under the
# stale mutation; the baseline gate never requires the stale blobs to match.
STALE_PARENT_COMMIT = "26fad1c0b18073dc1121be27adcc531c5ea0651a"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "wrong_bare_count",
    "break_kappa_homomorphism",
    "flip_commutation_sign",
    "claim_full_k_diagonal",
    "claim_flat_defect_full_rank",
    "wrong_necessity_rank",
    "claim_theta_forcing_survives",
    "claim_literal_collapse",
    "claim_theta_live_psd",
    "claim_three_constants",
    "break_ledger_item",
    "claim_rider_unconditional",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "wrong_bare_count": "B",
    "break_kappa_homomorphism": "B",
    "flip_commutation_sign": "C",
    "claim_full_k_diagonal": "C",
    "claim_flat_defect_full_rank": "D",
    "wrong_necessity_rank": "D",
    "claim_theta_forcing_survives": "E",
    "claim_literal_collapse": "E",
    "claim_theta_live_psd": "E",
    "claim_three_constants": "F",
    "break_ledger_item": "F",
    "claim_rider_unconditional": "G",
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
    commit that predates two of the pinned artifacts.
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
    return b142.no_float(value)


def zero(matrix: sp.MatrixBase) -> bool:
    return b148.zero(matrix)


def congruence_inertia(matrix: sp.MatrixBase) -> tuple[int, int, int]:
    """Exact (n_positive, n_zero, n_negative) WITH multiplicity, by congruence.

    Delegated to the COMMITTED Block 144 helper through the Block 148/147/145
    import chain, so that the tool this block reasons with is exactly the blob
    gate A pins.  b142.inertia / b143.inertia count DISTINCT real roots and are
    unsound on these degenerate spectra; the calibration is asserted in gate B.
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
# the committed model, imported wholesale through Block 148
# ---------------------------------------------------------------------------
SIZE = b148.SIZE                         # 32 cover sites
COVER_T = b148.COVER_T                   # 8
PHYS_T = b148.PHYS_T                     # 4
LX = b148.LX                             # 4
PHYS = b148.PHYS                         # 16 quotient sites
HALF = b148.HALF                         # 8 sites in the positive-time half
ORIGINS = b148.ORIGINS
INDEX = b148.INDEX
PLUS = b148.PLUS
THETA = b148.THETA
X0 = b148.X0
CELLS = b148.CELLS
COORDS = b148.COORDS                     # the 64 carrier moduli
EDGE_KEYS = b148.EDGE_KEYS               # the 16 healed edges
CHART01_EDGES = b148.CHART01_EDGES
ODD_SHEAR_COORDS = b148.ODD_SHEAR_COORDS  # the 8 odd-time-slice shear moments
SHEAR_COORDS = b145.SHEAR_COORDS          # all 16 shear moments
NU_MODULUS = b148.NU_MODULUS
A_MODULUS = b148.A_MODULUS
B_MODULUS = b148.B_MODULUS
INV_MODULUS = b148.INV_MODULUS
FREE_MODULI = b148.FREE_MODULI
HEALING_WEIGHTS = b148.HEALING_WEIGHTS
MOVES = b148.COVARIANT_MOVES             # the committed 64
THETA_LABEL = b148.THETA_LABEL           # (-1, 7, -1, 0), the canonical theta
THETA_PRIME = b148.THETA_PRIME           # (-1, 7, -1, 1), the odd-x-centred one
SHEAR_X, SHEAR_T = b148.SHEAR_X, b148.SHEAR_T

NCOORD = len(COORDS)                     # 64
X_SHIFT = (1, 0, 1, 1)                   # the kappa generator
TT = "theta"
TP = "theta'"

# the negative-time half projector, the companion of the committed PLUS
MINUS = sp.zeros(PHYS, HALF)
for _slot in range(HALF):
    MINUS[HALF + _slot, _slot] = 1

MOVE_MATRIX = {
    label: b148.move_matrix(b148.move_permutation(label)) for label in MOVES
}
DESCENT = {label: b142.descend(MOVE_MATRIX[label]) for label in MOVES}
THETA_PRIME_OP = DESCENT[THETA_PRIME]
OPS = ((TT, THETA), (TP, THETA_PRIME_OP))

COVER_FREE = b145.cover_hodge_general(*FREE_MODULI)     # 32x32, 64 moduli
HQ_FREE = b145.quotient(COVER_FREE)                     # 16x16, 64 moduli

STAGGERED_PARITY = tuple(
    (-1) ** ((site // LX) + (site % LX)) for site in range(PHYS)
)


def herm(matrix: sp.MatrixBase) -> sp.Matrix:
    """The HERMITIAN part (M + M^dagger)/2.  The pairing carries i's, so .H is
    not .T here; gate B pins this against the committed Block 148 helper on the
    objects where the two must agree."""
    matrix = sp.Matrix(matrix)
    return sp.expand((matrix + matrix.H) / 2)


def half_block(operator: sp.MatrixBase, matrix: sp.MatrixBase) -> sp.Matrix:
    """[X Q]_{++} on the half carrier {p = 0,1} (H1)."""
    return sp.expand(PLUS.T * operator * matrix * PLUS)


def cover_action(differential: sp.Matrix, hodge: sp.Matrix, mass) -> sp.Matrix:
    """A = m H + i (H d + d^dagger H) on the cover; the committed action law."""
    return sp.expand(
        mass * hodge + sp.I * (hodge * differential + differential.H * hodge)
    )


def kappa(label: tuple) -> int:
    """THE BARE CHARACTER kappa(e, p, e, q) = (p + q) mod 2.

    Gate B checks that it is a homomorphism onto Z_2 on all 64 x 64 composites,
    so its kernel is an index-2 subgroup of order 32; it is not assumed to be
    one, and the label composition law is itself pinned against cover matrix
    products before the character is read off it.
    """
    return (label[1] + label[3]) % 2


def diag_zero(matrix: sp.MatrixBase) -> bool:
    return all(sp.expand(matrix[index, index]) == 0 for index in range(HALF))


def live_slots(matrix: sp.MatrixBase) -> int:
    return sum(
        1 for index in range(HALF) if sp.expand(matrix[index, index]) != 0
    )


def selector(values) -> sp.Matrix:
    return sp.Matrix(
        [
            [1 if COORDS[column] == value else 0 for column in range(NCOORD)]
            for value in values
        ]
    )


def row_rank(rows) -> int:
    return sp.Matrix(rows).rank() if rows else 0


def coefficient_rows(matrix: sp.MatrixBase, variables) -> list:
    """Rows of coefficients of the entries of `matrix` in `variables`."""
    rows = []
    for row in range(matrix.rows):
        for column in range(matrix.cols):
            entry = sp.expand(matrix[row, column])
            if entry != 0:
                rows.append([entry.coeff(value, 1) for value in variables])
    return rows


def hermiticity_rows(block: sp.Matrix) -> list:
    """Coefficient rows of "block is Hermitian identically in the mass".

    The blocks reached here are real, so the defect is block - block^T; the
    mass-degree split is kept so the system is the one Block 145 landed.
    """
    rows = []
    for row in range(block.rows):
        for column in range(row + 1, block.cols):
            defect = sp.expand(block[row, column] - block[column, row])
            if defect == 0:
                continue
            for coefficient in sp.Poly(defect, MASS).all_coeffs():
                coefficient = sp.expand(coefficient)
                if coefficient != 0:
                    rows.append(
                        [coefficient.coeff(value, 1) for value in COORDS]
                    )
    return rows


def rowspace(rows) -> sp.Matrix:
    if not rows:
        return sp.zeros(0, NCOORD)
    reduced, pivots = sp.Matrix(rows).rref()
    if not pivots:
        return sp.zeros(0, NCOORD)
    return sp.Matrix([list(reduced[index, :]) for index in range(len(pivots))])


# ---------------------------------------------------------------------------
# the certificate constants this runner is claiming
# ---------------------------------------------------------------------------
GROUP_ORDER = 64
BARE_MOVES = 32
BARE_TRANSLATIONS = 16
BARE_REFLECTIONS = 16
BARE_INDEX = 2
HOMOMORPHISM_COMPOSITES = GROUP_ORDER * GROUP_ORDER      # 4096
COMPOSITION_SAMPLE_PAIRS = 60                            # 10 x 6, matrix-pinned
CROSS_VALIDATED_PAIRS = 8                                # 4 moves x 2 charts
BARE_GAUGES = ("I", "r_t")
NONBARE_GAUGES = ("r_x", "r_x r_t")
CHART_CLASS = {0: 0, 1: 1, 2: 1, 3: 0}   # the two DIAGONAL chart classes
BARE_OS_REFLECTIONS = 4                  # b148's ODD_CENTRED
OS_REFLECTIONS = 8                       # b148's HONEST_REFLECTIONS
HALF_PRESERVERS = 16                     # b149's HALF_PRESERVER_COUNT
BARE_HALF_PRESERVING = 8                 # b149's BARE_HALF_PRESERVING
THRESHOLD_STABILIZER = (
    (1, 0, 1, 0), (1, 0, 1, 2), (1, 4, 1, 0), (1, 4, 1, 2)
)                                        # b149's T5, EXACTLY

COMMUTATION_HITS = 64                    # g X_0 = (-1)^kappa X_0 g, all 64
OPPOSITE_SIGN_HITS = 0                   # the control: nothing satisfies both
COMMUTING_MOVES = 32
ANTICOMMUTING_MOVES = 32
K_EDGE_COUNT = 16
THETA_K_DIAGONAL_SLOTS = 4               # of 8 -- the refinement, not 8
THETA_K_LIVE_EDGES = 16                  # live on every edge, in 4 slots
PRIME_GRAM_LIVE_SLOTS = 4
GENERIC_CONVERSE_SLOTS = 8               # both converses live at 8/8

DEFECT_CARRIERS = (
    "flat", "b145-witness", "b148-escape", "staircase", "generic-cone"
)
PRIME_DEFECT_RANKS = (0, 8, 8, 16, 16)
THETA_DEFECT_RANKS = (0, 16, 16, 16, 16)
PRIME_DEFECT_COEFFICIENT_RANK = 14
THETA_DEFECT_COEFFICIENT_RANK = 16
THETA_SYSTEM_RANK = 18                   # b145.SYSTEM_RANK, reproduced
THETA_KERNEL_DIM = 46                    # b145.KERNEL_DIM, reproduced
PRIME_SYSTEM_RANK = 20
PRIME_KERNEL_DIM = 44
STACKED_RANK = 22
KERNEL_MEET = 42
KERNEL_SPAN = 48                         # exactly the shear-free stratum
THETA_RESIDUAL_RANK = 2                  # b145.RESIDUAL_RANK, reproduced
PRIME_RESIDUAL_RANK = 4
SEAM_ENTRIES = 8
SEAM_MATRIX_RANK = 8                     # the same for BOTH -- hence "moment
THETA_SEAM_COEFFICIENT_RANK = 4          # coefficient rank", not matrix rank
PRIME_SEAM_COEFFICIENT_RANK = 6
THETA_SEAM_DIAGONAL = 0
PRIME_SEAM_DIAGONAL = 4

DIAGONAL_LAW_EDGES = 16
THETA_LIVE_DIAGONAL_SLOTS = 4            # of 8, on EVERY edge
PRIME_STRUCTURAL_ZERO_SLOTS = 4
FORCING_RANK = 8
PRIME_FORCING_DETERMINANT = b148.FORCING_DETERMINANT
THETA_FORCING_DETERMINANT = (
    SHEAR_T ** 8 * (2 * MASS ** 2 + SHEAR_T ** 2) ** 4 / sp.Integer(2) ** 48
)
FORCING_SLICES = (
    ("s_x = 3/5, s_t = 4/5", R(3, 5), R(4, 5), 8, 8),
    ("s_x = 3/5, s_t = 0", R(3, 5), sp.Integer(0), 4, 8),
    ("s_x = 0, s_t = 4/5", sp.Integer(0), R(4, 5), 8, 8),
)
THETA_FORCING_RANK_AT_ST0 = 4            # the COLLAPSE; theta' stays at 8
PSD_CONDITIONAL_COLLAPSE = 16            # diag dead + PSD forces A' = 0, 16/16
LITERAL_COLLAPSE = 4                     # identically zero, 4/16 for BOTH
PRIME_CENSUS = ((4, 0, 4),)              # uniform
THETA_CENSUS = ((2, 0, 6), (4, 0, 4), (6, 0, 2))   # b142.INERTIA_CENSUS
HERMITIAN_EDGES = 0                      # neither operator is Hermitian anywhere
ESCAPE_INERTIA = (4, 4, 0)               # b148.ESCAPE_INERTIA
THETA_WITNESS_INERTIA = (4, 0, 4)
ANTICOMMUTATOR_RANK = 16                 # b143.ADAPTED_ANTICOMMUTATOR_RANK
X0_ANTICOMMUTATOR_RANK = 0               # X_0 stays the unique anticommutant
CONE_SCAN_CARRIERS = 5
CONE_SCAN_PSD_HITS = 0

KERNEL_DIFFERENCE = 2
THETA_ONLY_KERNEL_DIRECTIONS = 24        # of theta's 46
LEDGER_SIZE = 7
ADOPTION_LEDGER = (
    ("b145.SYSTEM_RANK", "18", "20"),
    ("b145.KERNEL_DIM", "46", "44"),
    ("b145.RESIDUAL_RANK", "2", "4"),
    (
        "b142.INERTIA_CENSUS",
        "{(2, 0, 6), (4, 0, 4), (6, 0, 2)}",
        "{(4, 0, 4)}",
    ),
    ("b142.PAIRING_ENTRY A[1,2]", "-19*m/160", "7/320"),
    ("b145.LIVE_SEAM_PAIRS", "4", "2"),
    ("b147.MIGRATION_CORE_LIVE_SLOTS", "0", "4"),
)
# One item moved, and only one: the live-seam pair count.  Used only by the
# break_ledger_item mutation.
WRONG_LEDGER = ADOPTION_LEDGER[:5] + (
    ("b145.LIVE_SEAM_PAIRS", "4", "4"),
) + ADOPTION_LEDGER[6:]
LIVE_SEAM_SINGLETONS = 12                # b145.LIVE_SINGLETON_COUNT, UNCHANGED
LIVE_SEAM_TRIPLES = 0                    # UNCHANGED

COMPLETION_CLASSES = (
    ("coboundary w Omega*", True, 4, 0),
    ("generic atlas-differential combination", True, 4, 0),
    ("sign-flipped variant", True, 4, 0),
)
PARITY_VIOLATING_LABEL = "fully generic 32x32 connection-side completion"
PARITY_VIOLATING_THETA_SLOTS = 8
PARITY_VIOLATING_PRIME_SLOTS = 8         # the counterexample: NOT zero

RUNTIME_BUDGET_SEC = 600


# ---------------------------------------------------------------------------
# measured facts (computed once, before any mutation flag is consulted)
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Facts:
    main_head: str
    authority: AuthorityCertificate
    # calibration
    inertia_calibration: bool
    hermitian_conventions_agree: bool
    action_law_pinned: bool
    descent_pinned: bool
    # B: the bare character
    unmatched_moves: int
    bare_moves: int
    bare_translations: int
    bare_reflections: int
    character_law: bool
    homomorphism_composites: tuple
    kappa_onto: bool
    composition_pinned: tuple
    bare_subgroup: tuple
    gauge_dichotomy: tuple
    diagonal_class_law: bool
    chart_image_sizes: tuple
    bare_cross_validated: tuple
    bare_os_reflections: tuple
    os_reflections: int
    half_preservers: int
    bare_half_preserving: int
    threshold_stabilizer: tuple
    theta_is_bare: bool
    theta_prime_is_bare: bool
    theta_gauges: tuple
    theta_prime_gauges: tuple
    prime_is_xshift_theta: bool
    # C: the mechanism
    commutation: tuple
    commutation_split: tuple
    hodge_is_x0_even: bool
    k_laws: tuple
    support_lemma: tuple
    generic_theorem: tuple
    generic_converse: tuple
    theta_hq_diagonal_zero: bool
    theta_k_diagonal: tuple
    prime_hq_diagonal_slots: int
    prime_k_diagonal_zero_edges: tuple
    migration_core: tuple
    # D: the quenched theta' chain
    defect_ranks: tuple
    defect_coefficient_ranks: tuple
    necessity: tuple
    kernels_in_b0: tuple
    seam_dead_forced: tuple
    incomparability: tuple
    residual: tuple
    seam_law: tuple
    # E: the diagonal split
    diagonal_law: tuple
    prime_diagonal_symbols: tuple
    theta_diagonal_symbols: tuple
    theta_live_diagonal_slots: tuple
    prime_structural_zero_slots: int
    forcing_determinants: tuple
    forcing_ranks: tuple
    forcing_slices: tuple
    forcing_only_odd_shears: bool
    collapse: tuple
    psd_conditional: tuple
    literal_zero_edges: tuple
    census: tuple
    hermitian_edges: tuple
    escape_witness: tuple
    theta_never_live_psd: bool
    anticommutators: tuple
    cone_scan: tuple
    # F: the verdict support
    kernel_difference: int
    theta_only_directions: tuple
    theta_only_pairing_mass_free: bool
    both_kernels_massless: bool
    adoption_ledger: tuple
    ledger_theta_reproduced: bool
    live_seam_residue: tuple
    # G: the completion rider
    completion_classes: tuple
    parity_violating: tuple
    # global
    exact_no_float: bool
    scope: dict


def measure(deep: bool) -> Facts:
    main_head = git_output("rev-parse", "origin/main")
    authority = authority_certificate(main_head)

    # The congruence routine is calibrated here, in the measurement pass, on
    # matrices whose inertia is known by inspection and on which the
    # root-counting helper of Blocks 142/143 is provably wrong.
    inertia_calibration = bool(
        congruence_inertia(sp.diag(1, 2, -3, R(5, 7))) == (3, 0, 1)
        and congruence_inertia(sp.diag(1, 1, -2, -2, 0)) == (2, 1, 2)
        and b142.inertia(sp.diag(1, 1, -2, -2, 0)) != (2, 1, 2)
    )
    hermitian_conventions_agree = all(
        zero(
            sp.expand(
                herm(half_block(operator, HQ_FREE))
                - b148.hermitian_part(half_block(operator, HQ_FREE))
            )
        )
        for _name, operator in OPS
    )
    # the descent of the canonical label IS the committed theta, and both
    # operators are involutive, half-swapping OS operators
    descent_pinned = bool(
        zero(sp.expand(DESCENT[THETA_LABEL] - b148.THETA))
        and all(DESCENT[label] is not None for label in MOVES)
        and all(
            zero(sp.expand(operator * operator - sp.eye(PHYS)))
            and zero(sp.expand(PLUS.T * operator * PLUS))
            and not zero(sp.expand(operator * PLUS))
            for _name, operator in OPS
        )
    )

    # -----------------------------------------------------------------------
    # B: the bare character
    # -----------------------------------------------------------------------
    differentials, star_form = b145.connection(SHEAR_X, SHEAR_T)
    atlas = {INDEX[origin]: differentials[origin] for origin in ORIGINS}
    variants = {
        "": differentials,
        "|s_t": b145.connection(SHEAR_X, -SHEAR_T)[0],
        "|s_x": b145.connection(-SHEAR_X, SHEAR_T)[0],
        "|both": b145.connection(-SHEAR_X, -SHEAR_T)[0],
    }
    lift_t, lift_x = b105.shift_lifts()
    gauge_x, gauge_t = b134.lifted(lift_x), b134.lifted(lift_t)
    gauges = {
        "I": sp.eye(SIZE),
        "r_x": gauge_x,
        "r_t": gauge_t,
        "r_x r_t": sp.expand(gauge_x * gauge_t),
    }
    # The catalogue is built ONCE as an explicit list of (name, matrix) pairs;
    # the hash lookup below is a view of it, so the cross-validation compares
    # the hash answer against an EXPLICIT SYMBOLIC SWEEP of the same objects.
    catalogue: list = []
    for gauge_name, gauge in gauges.items():
        inverse = gauge.inv()
        for variant_name, table in variants.items():
            for origin in ORIGINS:
                for dagger in (False, True):
                    base = table[origin].H if dagger else table[origin]
                    conjugated = sp.expand(gauge * base * inverse)
                    for sign in (1, -1):
                        catalogue.append(
                            (
                                (
                                    gauge_name,
                                    INDEX[origin],
                                    variant_name,
                                    dagger,
                                    sign,
                                ),
                                sp.ImmutableMatrix(sp.expand(sign * conjugated)),
                            )
                        )
    lookup: dict = {}
    for name, entry in catalogue:
        lookup.setdefault(entry, set()).add(name)

    transported = {
        (label, chart): sp.ImmutableMatrix(
            sp.expand(
                MOVE_MATRIX[label] * atlas[chart] * MOVE_MATRIX[label].T
            )
        )
        for label in MOVES
        for chart in range(4)
    }
    hits = {
        label: {
            chart: lookup.get(transported[(label, chart)], frozenset())
            for chart in range(4)
        }
        for label in MOVES
    }
    unmatched_moves = sum(
        1 for label in MOVES if any(not hits[label][chart] for chart in range(4))
    )

    def is_bare(label: tuple) -> bool:
        return all(
            any(entry[0] == "I" for entry in hits[label][chart])
            for chart in range(4)
        )

    bare = frozenset(label for label in MOVES if is_bare(label))
    bare_moves = len(bare)
    bare_translations = sum(1 for label in bare if label[0] == 1)
    bare_reflections = sum(1 for label in bare if label[0] == -1)
    character_law = all((kappa(label) == 0) == (label in bare) for label in MOVES)

    homomorphism_composites = (
        sum(
            1
            for left in MOVES
            for right in MOVES
            if kappa(b148.compose_labels(left, right))
            == (kappa(left) + kappa(right)) % 2
        ),
        HOMOMORPHISM_COMPOSITES,
    )
    kappa_onto = len({kappa(label) for label in MOVES}) == 2
    # the label composition law is itself pinned against cover matrix products
    composition_pairs = tuple(
        (left, right) for left in MOVES[::7] for right in MOVES[::11]
    )
    composition_pinned = (
        sum(
            1
            for left, right in composition_pairs
            if zero(
                sp.expand(
                    MOVE_MATRIX[left] * MOVE_MATRIX[right]
                    - MOVE_MATRIX[b148.compose_labels(left, right)]
                )
            )
        ),
        len(composition_pairs),
    )
    non_bare = tuple(label for label in MOVES if label not in bare)
    bare_subgroup = (
        all(
            b148.compose_labels(left, right) in bare
            for left in bare
            for right in bare
        ),
        all(
            any(
                b148.compose_labels(left, right) == (1, 0, 1, 0)
                for right in bare
            )
            for left in bare
        ),
        all(
            b148.compose_labels(left, right) in bare
            for left in non_bare
            for right in non_bare
        ),
        GROUP_ORDER // bare_moves if bare_moves else 0,
    )

    gauge_sets = {
        label: tuple(
            tuple(sorted({entry[0] for entry in hits[label][chart]}))
            for chart in range(4)
        )
        for label in MOVES
    }
    gauge_dichotomy = (
        tuple(
            sorted({gauge_sets[label] for label in bare})
        ),
        tuple(
            sorted({gauge_sets[label] for label in non_bare})
        ),
        not (set(BARE_GAUGES) & set(NONBARE_GAUGES)),
    )
    chart_images = {
        label: tuple(
            frozenset(entry[1] for entry in hits[label][chart])
            for chart in range(4)
        )
        for label in MOVES
    }
    diagonal_class_law = all(
        (
            all(
                all(
                    CHART_CLASS[image] == CHART_CLASS[chart]
                    for image in chart_images[label][chart]
                )
                for chart in range(4)
            )
        )
        == (label in bare)
        for label in MOVES
    )
    chart_image_sizes = tuple(
        sorted(
            {
                len(chart_images[label][chart])
                for label in MOVES
                for chart in range(4)
            }
        )
    )

    cross_sample = (THETA_LABEL, THETA_PRIME, X_SHIFT, (1, 3, 1, 2))
    cross_pairs = tuple((label, chart) for label in cross_sample for chart in (0, 2))
    bare_cross_validated = (
        sum(
            1
            for label, chart in cross_pairs
            if {
                name
                for name, entry in catalogue
                if zero(sp.expand(transported[(label, chart)] - entry))
            }
            == set(hits[label][chart])
        ),
        len(cross_pairs),
    )

    os_reflection_labels = tuple(
        label
        for label in MOVES
        if label[0] == -1
        and zero(sp.expand(PLUS.T * DESCENT[label] * PLUS))
        and not zero(sp.expand(DESCENT[label] * PLUS))
        and zero(sp.expand(DESCENT[label] * DESCENT[label] - sp.eye(PHYS)))
    )
    half_preserving = frozenset(
        label
        for label in MOVES
        if zero(sp.expand(MINUS.T * DESCENT[label] * PLUS))
    )
    bare_os = frozenset(
        label for label in os_reflection_labels if label in bare
    )
    bare_os_reflections = (
        len(bare_os),
        bare_os == frozenset(b148.ODD_CENTRED),
    )
    threshold_stabilizer = tuple(
        sorted(
            label
            for label in (bare & half_preserving)
            if label[0] == 1
        )
    )

    theta_gauges = tuple(
        sorted(set.intersection(*[set(gs) for gs in gauge_sets[THETA_LABEL]]))
    )
    theta_prime_gauges = tuple(
        sorted(set.intersection(*[set(gs) for gs in gauge_sets[THETA_PRIME]]))
    )
    prime_is_xshift_theta = bool(
        b148.compose_labels(X_SHIFT, THETA_LABEL) == THETA_PRIME
        and kappa(X_SHIFT) == 1
        and kappa(THETA_LABEL) == 1
        and kappa(THETA_PRIME) == 0
    )

    # -----------------------------------------------------------------------
    # C: the mechanism -- the staggered-parity selection rule
    # -----------------------------------------------------------------------
    commutation = (
        sum(
            1
            for label in MOVES
            if zero(
                sp.expand(
                    DESCENT[label] * X0
                    - (-1) ** kappa(label) * X0 * DESCENT[label]
                )
            )
        ),
        sum(
            1
            for label in MOVES
            if zero(
                sp.expand(
                    DESCENT[label] * X0
                    + (-1) ** kappa(label) * X0 * DESCENT[label]
                )
            )
        ),
        len(MOVES),
    )
    commutation_split = (
        sum(1 for label in MOVES if kappa(label) == 0),
        sum(1 for label in MOVES if kappa(label) == 1),
    )
    hodge_is_x0_even = zero(sp.expand(X0 * HQ_FREE * X0 - HQ_FREE))

    edge_table = b145.edge_differentials(differentials, star_form, HEALING_WEIGHTS)
    quotient_action = {
        key: b145.quotient(cover_action(edge_table[key], COVER_FREE, MASS))
        for key in EDGE_KEYS
    }
    # the inlined action law is pinned against the committed Block 145 routine
    action_law_pinned = all(
        zero(
            sp.expand(
                quotient_action[key]
                - b145.quotient_action(edge_table[key], COVER_FREE, MASS)
            )
        )
        for key in ((0, 0), (2, 3))
    )
    k_table = {
        key: sp.expand(quotient_action[key] - MASS * HQ_FREE)
        for key in EDGE_KEYS
    }
    k_laws = (
        sum(
            1
            for key in EDGE_KEYS
            if all(
                sp.expand(sp.im(sp.expand(k_table[key][i, j]))) == 0
                for i in range(PHYS)
                for j in range(PHYS)
            )
        ),
        sum(
            1
            for key in EDGE_KEYS
            if zero(sp.expand(k_table[key] + k_table[key].T))
        ),
        sum(1 for key in EDGE_KEYS if MASS not in k_table[key].free_symbols),
        sum(
            1
            for key in EDGE_KEYS
            if zero(sp.expand(X0 * k_table[key] * X0 + k_table[key]))
        ),
        sum(1 for key in EDGE_KEYS if not zero(k_table[key])),
    )
    support_lemma = (
        all(
            STAGGERED_PARITY[i] == STAGGERED_PARITY[j]
            for i in range(PHYS)
            for j in range(PHYS)
            if sp.expand(HQ_FREE[i, j]) != 0
        ),
        all(
            STAGGERED_PARITY[i] != STAGGERED_PARITY[j]
            for key in EDGE_KEYS
            for i in range(PHYS)
            for j in range(PHYS)
            if sp.expand(k_table[key][i, j]) != 0
        ),
    )

    generic = sp.Matrix(
        PHYS, PHYS, lambda i, j: sp.Symbol(f"y_{i}_{j}", real=True)
    )
    generic_odd = sp.Matrix(
        PHYS,
        PHYS,
        lambda i, j: generic[i, j]
        if STAGGERED_PARITY[i] != STAGGERED_PARITY[j]
        else 0,
    )
    generic_even = sp.Matrix(
        PHYS,
        PHYS,
        lambda i, j: generic[i, j]
        if STAGGERED_PARITY[i] == STAGGERED_PARITY[j]
        else 0,
    )
    generic_theorem = (
        diag_zero(sp.expand(PLUS.T * generic_odd * HQ_FREE * PLUS)),
        diag_zero(sp.expand(PLUS.T * generic_even * k_table[(0, 0)] * PLUS)),
    )
    generic_converse = (
        live_slots(sp.expand(PLUS.T * generic_even * HQ_FREE * PLUS)),
        live_slots(sp.expand(PLUS.T * generic_odd * k_table[(0, 0)] * PLUS)),
    )

    gram = {name: herm(half_block(operator, HQ_FREE)) for name, operator in OPS}
    theta_hq_diagonal_zero = diag_zero(
        sp.expand(PLUS.T * THETA * HQ_FREE * PLUS)
    )
    theta_k_slot_counts = {
        live_slots(sp.expand(PLUS.T * THETA * k_table[key] * PLUS))
        for key in EDGE_KEYS
    }
    theta_k_diagonal = (
        max(theta_k_slot_counts),
        HALF,
        sum(
            1
            for key in EDGE_KEYS
            if live_slots(sp.expand(PLUS.T * THETA * k_table[key] * PLUS)) > 0
        ),
        len(EDGE_KEYS),
    )
    prime_hq_diagonal_slots = live_slots(
        sp.expand(PLUS.T * THETA_PRIME_OP * HQ_FREE * PLUS)
    )
    prime_k_diagonal_zero_edges = (
        sum(
            1
            for key in EDGE_KEYS
            if diag_zero(sp.expand(PLUS.T * THETA_PRIME_OP * k_table[key] * PLUS))
        ),
        len(EDGE_KEYS),
    )
    migration_core = (
        diag_zero(gram[TT]),
        sp.expand(sp.trace(gram[TT])) == 0,
    )

    # -----------------------------------------------------------------------
    # D: the quenched theta' chain
    # -----------------------------------------------------------------------
    # (i) the H_q-preservation defect, CARRIER BY CARRIER.  This is the
    # correction to the first certificate: the rank is not one number.
    defect_fields = (
        ("flat", {cell: (sp.Integer(0), sp.Integer(1)) for cell in CELLS}),
        ("b145-witness", b145.witness_field()),
        ("b148-escape", b148.escape_witness_field()),
        ("staircase", b105.overlap_field()),
        ("generic-cone", b148.base_orbit_field()),
    )
    defect_points = {
        name: b147.modulus_point(field) for name, field in defect_fields
    }
    defect = {}
    for name, operator in OPS:
        product = sp.expand(operator * HQ_FREE)
        defect[name] = sp.expand(product - product.T)
    defect_ranks = tuple(
        (
            name,
            tuple(
                sp.expand(defect[name].xreplace(defect_points[carrier])).rank()
                for carrier, _field in defect_fields
            ),
        )
        for name, _operator in OPS
    )
    defect_coefficient_ranks = tuple(
        (name, row_rank(coefficient_rows(defect[name], COORDS)))
        for name, _operator in OPS
    )

    # (ii) the Hermiticity necessity systems
    system = {}
    per_edge_rows = {}
    for name, operator in OPS:
        rows: list = []
        per_edge_rows[name] = {}
        for key in EDGE_KEYS:
            edge_rows = hermiticity_rows(
                half_block(operator, quotient_action[key])
            )
            per_edge_rows[name][key] = rowspace(edge_rows)
            rows.extend(edge_rows)
        system[name] = sp.Matrix(rows)
    rank = {name: system[name].rank() for name, _operator in OPS}
    nullspace = {name: system[name].nullspace() for name, _operator in OPS}
    necessity = (
        rank[TT],
        NCOORD - rank[TT],
        rank[TP],
        NCOORD - rank[TP],
        rank[TT] == b145.SYSTEM_RANK,
        NCOORD - rank[TT] == b145.KERNEL_DIM,
    )
    shear_index = tuple(COORDS.index(value) for value in SHEAR_COORDS)
    kernels_in_b0 = tuple(
        all(
            vector[index] == 0
            for vector in nullspace[name]
            for index in shear_index
        )
        for name, _operator in OPS
    )
    seam_dead_forced = tuple(
        sp.Matrix.vstack(system[name], selector(ODD_SHEAR_COORDS)).rank()
        == rank[name]
        for name, _operator in OPS
    )
    stacked = sp.Matrix.vstack(system[TT], system[TP])
    stacked_rank = stacked.rank()
    span_basis = nullspace[TT] + nullspace[TP]
    span_matrix = (
        sp.Matrix.hstack(*span_basis) if span_basis else sp.zeros(NCOORD, 0)
    )
    incomparability = (
        stacked_rank,
        NCOORD - stacked_rank,
        span_matrix.rank(),
        bool(
            span_matrix.rank() == KERNEL_SPAN
            and all(
                vector[index] == 0
                for vector in span_basis
                for index in shear_index
            )
        ),
        bool(stacked_rank > rank[TT] and stacked_rank > rank[TP]),
    )
    shear_set = set(SHEAR_COORDS)
    residual = tuple(
        (
            name,
            sp.Matrix(
                [
                    [
                        row[index]
                        for index in range(NCOORD)
                        if COORDS[index] not in shear_set
                    ]
                    for row in [
                        list(system[name][r, :]) for r in range(system[name].rows)
                    ]
                ]
            ).rank(),
        )
        for name, _operator in OPS
    )

    # (iii) the seam law, in MOMENT-COEFFICIENT rank -- both matrix ranks are 8
    seam_law = tuple(
        (
            name,
            sum(1 for entry in gram[name] if sp.expand(entry) != 0),
            live_slots(gram[name]),
            gram[name].rank(),
            row_rank(coefficient_rows(gram[name], ODD_SHEAR_COORDS)),
            frozenset().union(
                *[sp.expand(entry).free_symbols for entry in gram[name]]
            )
            == frozenset(ODD_SHEAR_COORDS),
            sp.expand(sp.trace(gram[name])) == 0,
        )
        for name, _operator in OPS
    )

    # -----------------------------------------------------------------------
    # E: the diagonal split, the two qualifiers and the closure comparison
    # -----------------------------------------------------------------------
    pairing = {
        (name, key): herm(half_block(operator, quotient_action[key]))
        for name, operator in OPS
        for key in EDGE_KEYS
    }
    diagonal_law = (
        sum(
            1
            for key in EDGE_KEYS
            if all(
                sp.expand(pairing[(TP, key)][k, k] - MASS * gram[TP][k, k]) == 0
                for k in range(HALF)
            )
        ),
        len(EDGE_KEYS),
        all(
            sp.expand(pairing[(TT, key)][k, k] - MASS * gram[TT][k, k]) == 0
            for key in EDGE_KEYS
            for k in range(HALF)
        ),
    )
    prime_diagonal_symbols: set = set()
    theta_diagonal_symbols: set = set()
    for key in EDGE_KEYS:
        for k in range(HALF):
            prime_diagonal_symbols |= sp.expand(
                pairing[(TP, key)][k, k]
            ).free_symbols
            theta_diagonal_symbols |= sp.expand(
                pairing[(TT, key)][k, k]
            ).free_symbols
    prime_diagonal_symbols_fact = (
        MASS in prime_diagonal_symbols,
        bool(prime_diagonal_symbols & {SHEAR_X, SHEAR_T}),
    )
    theta_diagonal_symbols_fact = (
        MASS in theta_diagonal_symbols,
        bool(theta_diagonal_symbols & {SHEAR_X, SHEAR_T}),
    )
    theta_live_diagonal_slots = tuple(
        sorted({live_slots(pairing[(TT, key)]) for key in EDGE_KEYS})
    )
    prime_structural_zero_slots = sum(
        1 for k in range(HALF) if sp.expand(gram[TP][k, k]) == 0
    )

    # QUALIFIER A: the chart-0/1 forcing, its determinants and its slices
    def forcing_system(name, operator, key, substitution) -> tuple:
        block = sp.expand(pairing[(name, key)].xreplace(substitution))
        if name == TP:
            slots = [k for k in range(HALF) if sp.expand(gram[TP][k, k]) == 0]
        else:
            slots = [k for k in range(HALF) if sp.expand(block[k, k]) == 0]
        rows = []
        involved: set = set()
        for k in slots:
            for j in range(HALF):
                for part in (
                    sp.expand(sp.re(block[k, j])),
                    sp.expand(sp.im(block[k, j])),
                ):
                    if part != 0:
                        rows.append(part)
                        involved |= set(part.free_symbols) & set(COORDS)
        matrix = (
            sp.Matrix(
                [
                    [sp.expand(row).coeff(value, 1) for value in ODD_SHEAR_COORDS]
                    for row in rows
                ]
            )
            if rows
            else sp.zeros(0, len(ODD_SHEAR_COORDS))
        )
        return (
            matrix.rank() if rows else 0,
            sp.factor(sp.expand((matrix.T * matrix).det())) if rows else 0,
            involved <= set(ODD_SHEAR_COORDS),
        )

    forcing = {
        (name, key): forcing_system(name, operator, key, {})
        for name, operator in OPS
        for key in CHART01_EDGES
    }
    prime_dets = {forcing[(TP, key)][1] for key in CHART01_EDGES}
    theta_dets = {forcing[(TT, key)][1] for key in CHART01_EDGES}
    forcing_ranks = tuple(
        (name, tuple(sorted({forcing[(name, key)][0] for key in CHART01_EDGES})))
        for name, _operator in OPS
    )
    forcing_determinants = (
        len(prime_dets) == 1
        and sp.simplify(
            next(iter(prime_dets)) - sp.factor(PRIME_FORCING_DETERMINANT)
        )
        == 0,
        len(theta_dets) == 1
        and sp.simplify(
            next(iter(theta_dets)) - sp.factor(THETA_FORCING_DETERMINANT)
        )
        == 0,
        sp.simplify(next(iter(theta_dets)).subs(SHEAR_T, 0)) == 0,
        sp.simplify(
            next(iter(prime_dets)).subs({SHEAR_T: 0, SHEAR_X: R(3, 5)})
        )
        != 0,
    )
    forcing_only_odd_shears = all(
        forcing[(name, key)][2]
        for name, _operator in OPS
        for key in CHART01_EDGES
    )
    forcing_slices = tuple(
        (
            tag,
            tuple(
                sorted(
                    {
                        forcing_system(
                            TT, THETA, key, {SHEAR_X: s_x, SHEAR_T: s_t}
                        )[0]
                        for key in CHART01_EDGES
                    }
                )
            ),
            tuple(
                sorted(
                    {
                        forcing_system(
                            TP, THETA_PRIME_OP, key, {SHEAR_X: s_x, SHEAR_T: s_t}
                        )[0]
                        for key in CHART01_EDGES
                    }
                )
            ),
        )
        for tag, s_x, s_t, _theta_rank, _prime_rank in FORCING_SLICES
    )

    # QUALIFIER B: the PSD-conditional collapse against the literal one
    seam_dead = {value: 0 for value in ODD_SHEAR_COORDS}
    quenched = {
        (name, key): sp.expand(pairing[(name, key)].xreplace(seam_dead))
        for name, _operator in OPS
        for key in EDGE_KEYS
    }
    collapse = (
        sum(1 for key in EDGE_KEYS if diag_zero(quenched[(TP, key)])),
        sum(1 for key in EDGE_KEYS if zero(quenched[(TP, key)])),
        sum(1 for key in EDGE_KEYS if diag_zero(quenched[(TT, key)])),
        sum(1 for key in EDGE_KEYS if zero(quenched[(TT, key)])),
    )

    def psd_forces_zero(block: sp.Matrix) -> bool:
        """A zero diagonal makes every 2x2 principal minor -|a_ij|^2 <= 0, so
        a PSD block with a zero diagonal is identically zero."""
        return diag_zero(block) and all(
            sp.expand(
                block[i, i] * block[j, j]
                - block[i, j] * block[j, i]
                + block[i, j] ** 2
            )
            == 0
            for i in range(HALF)
            for j in range(HALF)
        )

    psd_conditional = tuple(
        sum(1 for key in EDGE_KEYS if psd_forces_zero(quenched[(name, key)]))
        for name, _operator in OPS
    )
    literal_zero_edges = tuple(
        sorted(key for key in EDGE_KEYS if zero(quenched[(TT, key)]))
    )

    # the staircase census, the witness and the anticommutant
    staircase = b147.modulus_point(b105.overlap_field())
    fixture = {SHEAR_X: b134.S_X, SHEAR_T: b134.S_T}
    fixture_mass = {MASS: b134.MASS}
    census = tuple(
        (
            name,
            tuple(
                sorted(
                    {
                        congruence_inertia(
                            sp.expand(
                                pairing[(name, key)]
                                .xreplace(staircase)
                                .xreplace(fixture)
                                .xreplace(fixture_mass)
                            )
                        )
                        for key in EDGE_KEYS
                    }
                )
            ),
        )
        for name, _operator in OPS
    )
    hermitian_edges = tuple(
        sum(
            1
            for key in EDGE_KEYS
            if zero(
                sp.expand(
                    half_block(operator, quotient_action[key])
                    - half_block(operator, quotient_action[key]).T
                )
            )
        )
        for name, operator in OPS
    )
    witness_field = b148.escape_witness_field()
    witness_point = b147.modulus_point(witness_field)
    witness_gram = sp.expand(gram[TP].xreplace(witness_point))
    escape_witness = (
        b145.in_admissible_cone(witness_field),
        zero(sp.expand(witness_gram - b148.ESCAPE_GRAM)),
        congruence_inertia(witness_gram),
        congruence_inertia(sp.expand(gram[TT].xreplace(witness_point))),
    )
    theta_never_live_psd = bool(
        diag_zero(gram[TT])
        and all(
            sp.expand(
                gram[TT][i, i] * gram[TT][j, j]
                - gram[TT][i, j] * gram[TT][j, i]
                + gram[TT][i, j] ** 2
            )
            == 0
            for i in range(HALF)
            for j in range(HALF)
        )
    )
    hodge_staircase = sp.expand(HQ_FREE.xreplace(staircase))
    hodge_inverse = hodge_staircase.inv()
    anticommutator_ranks = {TT: set(), TP: set(), "X_0": set()}
    for key in EDGE_KEYS:
        residue = sp.expand(
            k_table[key].xreplace(staircase).xreplace(fixture)
        )
        adapted = sp.expand(hodge_inverse * residue)
        anticommutator_ranks[TT].add(
            sp.expand(THETA * adapted + adapted * THETA).rank()
        )
        anticommutator_ranks[TP].add(
            sp.expand(THETA_PRIME_OP * adapted + adapted * THETA_PRIME_OP).rank()
        )
        anticommutator_ranks["X_0"].add(
            sp.expand(X0 * adapted + adapted * X0).rank()
        )
    anticommutators = (
        tuple(sorted(anticommutator_ranks[TT])),
        tuple(sorted(anticommutator_ranks[TP])),
        tuple(sorted(anticommutator_ranks["X_0"])),
        b143.ADAPTED_ANTICOMMUTATOR_RANK,
    )
    scan_carriers = tuple(b148.CONE_CARRIERS) + (("escape", witness_field),)
    psd_hits = 0
    for _name, field in scan_carriers:
        point = b147.modulus_point(field)
        for key in EDGE_KEYS:
            for name, _operator in OPS:
                block = sp.expand(
                    pairing[(name, key)]
                    .xreplace(point)
                    .xreplace(fixture)
                    .xreplace(fixture_mass)
                )
                if zero(block):
                    continue
                if congruence_inertia(block)[2] == 0:
                    psd_hits += 1
    cone_scan = (len(scan_carriers), psd_hits)

    # -----------------------------------------------------------------------
    # F: the verdict support -- inertness and the adoption ledger
    # -----------------------------------------------------------------------
    kernel_difference = rank[TP] - rank[TT]
    theta_only = [
        vector
        for vector in nullspace[TT]
        if not zero(sp.expand(system[TP] * vector))
    ]
    theta_only_directions = (len(theta_only), len(nullspace[TT]))
    theta_only_pairing_mass_free = True
    if theta_only:
        direction = {
            COORDS[index]: sp.nsimplify(theta_only[0][index])
            for index in range(NCOORD)
        }
        theta_only_pairing_mass_free = all(
            MASS
            not in sp.expand(pairing[(TT, key)].xreplace(direction)).free_symbols
            for key in EDGE_KEYS
        )
    shear_free = {value: 0 for value in SHEAR_COORDS}
    both_kernels_massless = all(
        zero(sp.expand(gram[name].xreplace(shear_free)))
        for name, _operator in OPS
    )

    displayed = (INDEX[b134.DISPLAYED[0]], INDEX[b134.DISPLAYED[1]])

    def at_fixture(matrix: sp.MatrixBase) -> sp.Matrix:
        return sp.expand(matrix.xreplace(staircase).xreplace(fixture))

    def can_live(blocks) -> bool:
        live = [block for block in blocks if block.rows]
        if not live:
            return True
        stack = sp.Matrix.vstack(*live)
        return (
            sp.Matrix.vstack(stack, b145.ODD_SELECTOR).rank() > stack.rank()
        )

    ordered_edges = sorted(EDGE_KEYS)
    live_singletons = sum(
        1 for key in ordered_edges if can_live([per_edge_rows[TP][key]])
    )
    live_pairs = sum(
        1
        for subset in itertools.combinations(ordered_edges, 2)
        if can_live([per_edge_rows[TP][key] for key in subset])
    )
    live_triples = sum(
        1
        for subset in itertools.combinations(ordered_edges, 3)
        if can_live([per_edge_rows[TP][key] for key in subset])
    )
    live_seam_residue = (live_singletons, live_pairs, live_triples)

    census_string = {
        name: "{" + ", ".join(str(item) for item in values) + "}"
        for name, values in census
    }
    adoption_ledger = (
        (
            "b145.SYSTEM_RANK",
            str(b145.SYSTEM_RANK),
            str(rank[TP]),
        ),
        (
            "b145.KERNEL_DIM",
            str(b145.KERNEL_DIM),
            str(NCOORD - rank[TP]),
        ),
        (
            "b145.RESIDUAL_RANK",
            str(b145.RESIDUAL_RANK),
            str(dict(residual)[TP]),
        ),
        (
            "b142.INERTIA_CENSUS",
            "{" + ", ".join(str(item) for item in sorted(b142.INERTIA_CENSUS))
            + "}",
            census_string[TP],
        ),
        (
            "b142.PAIRING_ENTRY A[1,2]",
            str(b142.PAIRING_ENTRY),
            str(at_fixture(pairing[(TP, displayed)])[1, 2]),
        ),
        (
            "b145.LIVE_SEAM_PAIRS",
            str(len(b145.LIVE_PAIRS)),
            str(live_pairs),
        ),
        (
            "b147.MIGRATION_CORE_LIVE_SLOTS",
            str(live_slots(gram[TT])),
            str(live_slots(gram[TP])),
        ),
    )
    # the theta column of the ledger is itself pinned: theta must REPRODUCE the
    # landed values, or the "moves" are not moves at all
    ledger_theta_reproduced = bool(
        rank[TT] == b145.SYSTEM_RANK
        and NCOORD - rank[TT] == b145.KERNEL_DIM
        and dict(residual)[TT] == b145.RESIDUAL_RANK
        and census_string[TT]
        == "{" + ", ".join(str(item) for item in sorted(b142.INERTIA_CENSUS))
        + "}"
        and sp.expand(
            at_fixture(pairing[(TT, displayed)])[1, 2] - b142.PAIRING_ENTRY
        )
        == 0
        and live_slots(gram[TT]) == 0
    )

    # -----------------------------------------------------------------------
    # G: the completion rider -- the parity class and its counterexample
    # -----------------------------------------------------------------------
    base_edge = edge_table[(0, 0)]
    weight, c0, c1, c2, c3 = sp.symbols("w c0 c1 c2 c3", real=True)

    def residue_of(diff: sp.Matrix) -> sp.Matrix:
        return sp.expand(
            b145.quotient(
                sp.expand(sp.I * (COVER_FREE * diff + diff.H * COVER_FREE))
            )
        )

    base_residue = residue_of(base_edge)

    def completion_profile(delta: sp.Matrix) -> tuple:
        shift = sp.expand(
            residue_of(sp.expand(base_edge + delta)) - base_residue
        )
        return (
            zero(sp.expand(X0 * shift * X0 + shift)),
            live_slots(sp.expand(PLUS.T * THETA * shift * PLUS)),
            live_slots(sp.expand(PLUS.T * THETA_PRIME_OP * shift * PLUS)),
        )

    completion_classes = tuple(
        (tag,) + completion_profile(delta)
        for tag, delta in (
            ("coboundary w Omega*", sp.expand(weight * star_form)),
            (
                "generic atlas-differential combination",
                sp.expand(
                    c0 * differentials[(0, 0)]
                    + c1 * differentials[(0, 1)]
                    + c2 * differentials[(1, 0)]
                    + c3 * differentials[(1, 1)]
                ),
            ),
            (
                "sign-flipped variant",
                sp.expand(c0 * variants["|both"][(1, 1)]),
            ),
        )
    )
    parity_violating = (PARITY_VIOLATING_LABEL,) + completion_profile(
        sp.Matrix(
            SIZE, SIZE, lambda i, j: sp.Symbol(f"z_{i}_{j}", real=True)
        )
    )

    exact_no_float = no_float(
        (
            COVER_FREE,
            HQ_FREE,
            gram[TT],
            gram[TP],
            system[TP],
            k_table[(0, 0)],
            witness_gram,
        )
    )

    composition_deep = (
        (
            sum(
                1
                for left in MOVES
                for right in MOVES
                if zero(
                    sp.expand(
                        MOVE_MATRIX[left] * MOVE_MATRIX[right]
                        - MOVE_MATRIX[b148.compose_labels(left, right)]
                    )
                )
            ),
            HOMOMORPHISM_COMPOSITES,
        )
        if deep
        else (0, 0)
    )

    return Facts(
        main_head=main_head,
        authority=authority,
        inertia_calibration=inertia_calibration,
        hermitian_conventions_agree=hermitian_conventions_agree,
        action_law_pinned=action_law_pinned,
        descent_pinned=descent_pinned,
        unmatched_moves=unmatched_moves,
        bare_moves=bare_moves,
        bare_translations=bare_translations,
        bare_reflections=bare_reflections,
        character_law=character_law,
        homomorphism_composites=homomorphism_composites,
        kappa_onto=kappa_onto,
        composition_pinned=composition_pinned + composition_deep,
        bare_subgroup=bare_subgroup,
        gauge_dichotomy=gauge_dichotomy,
        diagonal_class_law=diagonal_class_law,
        chart_image_sizes=chart_image_sizes,
        bare_cross_validated=bare_cross_validated,
        bare_os_reflections=bare_os_reflections,
        os_reflections=len(os_reflection_labels),
        half_preservers=len(half_preserving),
        bare_half_preserving=len(bare & half_preserving),
        threshold_stabilizer=threshold_stabilizer,
        theta_is_bare=THETA_LABEL in bare,
        theta_prime_is_bare=THETA_PRIME in bare,
        theta_gauges=theta_gauges,
        theta_prime_gauges=theta_prime_gauges,
        prime_is_xshift_theta=prime_is_xshift_theta,
        commutation=commutation,
        commutation_split=commutation_split,
        hodge_is_x0_even=hodge_is_x0_even,
        k_laws=k_laws,
        support_lemma=support_lemma,
        generic_theorem=generic_theorem,
        generic_converse=generic_converse,
        theta_hq_diagonal_zero=theta_hq_diagonal_zero,
        theta_k_diagonal=theta_k_diagonal,
        prime_hq_diagonal_slots=prime_hq_diagonal_slots,
        prime_k_diagonal_zero_edges=prime_k_diagonal_zero_edges,
        migration_core=migration_core,
        defect_ranks=defect_ranks,
        defect_coefficient_ranks=defect_coefficient_ranks,
        necessity=necessity,
        kernels_in_b0=kernels_in_b0,
        seam_dead_forced=seam_dead_forced,
        incomparability=incomparability,
        residual=residual,
        seam_law=seam_law,
        diagonal_law=diagonal_law,
        prime_diagonal_symbols=prime_diagonal_symbols_fact,
        theta_diagonal_symbols=theta_diagonal_symbols_fact,
        theta_live_diagonal_slots=theta_live_diagonal_slots,
        prime_structural_zero_slots=prime_structural_zero_slots,
        forcing_determinants=forcing_determinants,
        forcing_ranks=forcing_ranks,
        forcing_slices=forcing_slices,
        forcing_only_odd_shears=forcing_only_odd_shears,
        collapse=collapse,
        psd_conditional=psd_conditional,
        literal_zero_edges=literal_zero_edges,
        census=census,
        hermitian_edges=hermitian_edges,
        escape_witness=escape_witness,
        theta_never_live_psd=theta_never_live_psd,
        anticommutators=anticommutators,
        cone_scan=cone_scan,
        kernel_difference=kernel_difference,
        theta_only_directions=theta_only_directions,
        theta_only_pairing_mass_free=theta_only_pairing_mass_free,
        both_kernels_massless=both_kernels_massless,
        adoption_ledger=adoption_ledger,
        ledger_theta_reproduced=ledger_theta_reproduced,
        live_seam_residue=live_seam_residue,
        completion_classes=completion_classes,
        parity_violating=parity_violating,
        exact_no_float=exact_no_float,
        scope=scope_certificate(raw_note()),
    )


# ---------------------------------------------------------------------------
# H. note scope
# ---------------------------------------------------------------------------
# PLACEHOLDER FENCE.  The landing supervisor replaces this string with the
# note's own eight-line N5 fence, byte for byte; until then H-note-scope is the
# single failing gate and the runner exits 1.
N5_FENCE = 'N5: per_element: THE BARE CHARACTER, EXACT AND COMPLETE: over the committed 64-member covariant move group, matched against the committed four-chart shear atlas under all four gauges {I, r_x, r_t, r_x r_t}, both orientations, both signs and all four shear variants with ZERO UNMATCHED MOVES, a covariant move (e, p, e, q) is BARE -- meaning its transported chart differential matches a committed atlas entry with the IDENTITY gauge on ALL FOUR charts -- IF AND ONLY IF p + q IS EVEN, independently of the sign e; kappa(e, p, e, q) = (p + q) mod 2 is therefore a HOMOMORPHISM onto Z_2, verified on ALL 64 x 64 = 4,096 composites, and the bare set is EXACTLY ker kappa: an INDEX-2 SUBGROUP of ORDER 32 comprising 16 TRANSLATIONS and 16 REFLECTIONS, closed and inverse-closed with non-bare * non-bare = bare; the gauge requirement is an exact BINARY DICHOTOMY with NO OVERLAP -- bare moves admit exactly {I, r_t} on all four charts and non-bare moves exactly {r_x, r_x r_t}, 32 and 32, and no move admits both profiles, so the gauge insertion a non-bare operator needs is ALL-OR-NOTHING and never chart-by-chart; the GEOMETRIC READING is that bare means PRESERVING THE TWO DIAGONAL CHART CLASSES {(0,0),(1,1)} and {(0,1),(1,0)} SETWISE, the same diagonal Block 148\'s bond directions (1,3) and (7,1) pick out; and ONE CHARACTER RECONCILES EVERY LANDED COUNT -- Block 148\'s FOUR bare OS reflections out of eight, which are exactly the ODD-x-CENTRED ones because a reflection has p ODD so kappa = 0 forces q ODD, and its SIXTEEN bare translations; and Block 149\'s bare-move, bare-translation and bare-half-preserving counts together with its THRESHOLD STABILIZER, which is exactly the intersection BARE and HALF-PRESERVING and TRANSLATION and has EXACTLY FOUR members (1,0,1,0), (1,0,1,2), (1,4,1,0), (1,4,1,2), reproduced identically here -- with theta = (-1,7,-1,0) NOT BARE at kappa = 1 and profile {r_x, r_x r_t}, theta\' = (-1,7,-1,1) BARE at kappa = 0 and profile {I, r_t}, and theta\' = (x-shift-by-1) . theta where the x-shift (1,0,1,1) is THE EXACT GENERATOR OF kappa\nper_site: THE MECHANISM -- BARENESS IS X_0-COMMUTATION: g X_0 = (-1)^kappa(g) X_0 g for ALL 64 covariant moves, with 32 COMMUTING and 32 ANTICOMMUTING and NO EXCEPTIONS, on the cover AND after descent, so the atlas-matching character of the per_element line and the staggered-parity commutation sign are THE SAME CHARACTER -- in particular theta ANTICOMMUTES with X_0 and theta\' COMMUTES with it; and combined with X_0 H_q X_0 = H_q, with K = Q - m H_q being m-FREE, REAL ANTISYMMETRIC and X_0-ODD (X_0 K X_0 = -K) on ALL SIXTEEN healed edges symbolically in (s_x, s_t) and over the whole 64-modulus family, and with the SUPPORT LEMMA that H_q is supported on EQUAL staggered parity while K is supported on OPPOSITE staggered parity, this forces a GENERIC SELECTION RULE about any half-swapping OS operator on the committed carrier: an X_0-ODD operator has an IDENTICALLY ZERO H_q-diagonal and a LIVE K-diagonal, and an X_0-EVEN operator has the REVERSE -- whence BLOCK 147\'S MIGRATION CORE IS A ONE-LINE COROLLARY, theta being X_0-odd so its structural zero pairing diagonal is automatic rather than computed, with the CHECKER\'S REFINEMENT that theta\'s live K-diagonal is live on 16 of 16 EDGES but in exactly 4 OF 8 SLOTS UNIFORMLY and NOT in all eight, the same four slots on every edge; and theta\' being X_0-EVEN so that diag Herm([theta\' Q]_++) = m diag G\' on ALL SIXTEEN EDGES, symbolically in the 64 moduli and in (s_x, s_t), making the theta\'-diagonal PURE MASS GRAM, CONNECTION-FREE and carrying NO FIXTURE-SHEAR SYMBOLS, while for theta the same law is FALSE and its diagonal is m-FREE and CONNECTION-CARRIED -- and the COST is stated here and not softened: Block 147\'s MECHANISM is theta-SPECIFIC, is FALSE under theta\', and under adoption the migration statement must be RE-PROVED through Block 148\'s forcing route\nper_mode: THE QUENCHED THETA-PRIME CHAIN, WITH THE CHECKER\'S ONE REFUTATION DISPLAYED: (a) H_q PRESERVATION -- the theta\' Hodge-preservation defect has GENERIC matrix rank 16 but is CARRIER-DEPENDENT, with RANK 0 AT THE FLAT CARRIER where theta\' DOES preserve H_q, RANK 8 at Block 148\'s escape witness AND at Block 145\'s witness, and rank 16 generically, the CARRIER-FREE COEFFICIENT RANK being 14, so the flat "rank 16, no free symbols" phrasing is THETA\'S NUMBER AND IS CORRECTED HERE while the CONCLUSION is unchanged, Block 142\'s zero-of-256 theorem already covering theta\' and NEITHER operator preserving H_q generically, the improvement being COSMETIC and not structural; (b) THE HERMITICITY NECESSITY -- Block 145\'s rank-18 kernel-46 theorem is reproduced as calibration and the theta\' system has RANK 20 with KERNEL 44, STRICTLY SMALLER, with BOTH kernels lying inside {b = 0} and BOTH FORCING THE SEAM DEAD so Block 145\'s VERDICT that the mass never enters an atlas-globally Hermitian pairing SURVIVES VERBATIM under theta\'; the two loci are INCOMPARABLE RATHER THAN NESTED, the stacked rank being 22 so the intersection is 42-dimensional and 46 + 44 - 42 = 48 means the two loci SPAN EXACTLY THE 48-DIMENSIONAL SHEAR-FREE STRATUM {b = 0}, each containing directions the other excludes; the shear-free residual is 4 for theta\' against 2 for theta, and THAT DIFFERENCE IS PHYSICALLY INERT because the mass Gram VANISHES IDENTICALLY on {b = 0} for BOTH operators so both loci carry an exactly m-FREE pairing; and (c) THE SEAM LAW, stated as a COEFFICIENT RANK -- read as the moment-COEFFICIENT map of Herm([X H_q]_++) in the eight odd-time-slice shear moments, the theta\'-seam sees EXACTLY THE SAME EIGHT MOMENTS as the theta-seam with 8 nonzero entries each, but at COEFFICIENT RANK 6 OF 8 against theta\'s COEFFICIENT RANK 4, with FOUR MOMENTS ON THE DIAGONAL and a LIVE TRACE where theta puts all eight in FOUR HYPERBOLIC 2x2 BLOCKS with ZERO TRACE -- and the words "coefficient rank" are used wherever these numbers appear, because read as the rank of a Gram matrix they would be a different and unproved statement\nper_block: THE DIAGONAL SPLIT AND ITS TWO QUALIFIERS, BOTH THE CHECKER\'S: the structural difference is that diag Herm([theta\' Q]_++) = m diag G\' on ALL SIXTEEN EDGES so the theta\'-diagonal is PURE MASS GRAM, CONNECTION-FREE and carrying NO fixture-shear symbols, while theta\'s diagonal is m-FREE, CONNECTION-CARRIED and live in 4 OF 8 SLOTS; QUALIFIER A is a THETA-PRIME ADVANTAGE THE SOLVE HAD NOT CLAIMED -- on the four chart-0/1 edges the PSD-forced rows involve ONLY the eight odd shears and the forcing system has RANK 8 for BOTH conventions GENERICALLY, so the forcing step is NOT an odd-centred privilege, BUT THE DETERMINANTS DIFFER, theta\'\'s being (s_t^2 + s_x^2)^6 (4 m^2 + s_t^2 + s_x^2)^2 / 2^48 and POSITIVE EVERYWHERE while theta\'s is s_t^8 (2 m^2 + s_t^2)^4 / 2^48 and VANISHES ON THE WHOLE s_t = 0 LINE, where theta\'s forcing rank COLLAPSES TO 4 and theta\'\'s STAYS 8, so theta loses half its seam-killing power on a codimension-1 locus that theta\' does not notice; QUALIFIER B is that the atlas-wide closure is PSD-CONDITIONAL -- under the PSD-conditional reading, "the diagonal is dead so POSITIVITY forces the block to vanish", the closure holds on 16 OF 16 EDGES for theta\' against 4 OF 16 for theta and Block 148\'s "identically zero" closure extends from its four displayed edges to THE WHOLE ATLAS, but under the LITERAL reading, A = 0 as an IDENTITY with no positivity invoked, it holds on 4 OF 16 for BOTH, so the theta\' closure advantage is REAL and CONDITIONAL ON PSD and the condition is stated wherever the claim is used; and four further comparisons stand -- the committed staircase inertia census is UNIFORM {(4,0,4)} for theta\' against Block 142\'s THREE values {(2,0,6),(4,0,4),(6,0,2)} for theta with 0 OF 16 Hermitian edges for BOTH; Block 148\'s ESCAPE WITNESS, re-tested in the admissible cone, gives theta\' the LIVE PSD MASS GRAM G\' = diag(15/64, 0, 15/64, 0, 0, 15/64, 0, 15/64) at inertia (4,4,0) that THETA CAN NEVER HAVE, since a ZERO DIAGONAL makes every off-diagonal 2x2 principal minor a NEGATIVE SQUARE; X_0\'s UNIQUENESS IS UNTOUCHED, {X_0, J} = 0 on all 16 edges while {theta, J} AND {theta\', J} both have RANK 16 on all 16, so theta\' is half-exchanging and Block 143\'s half-exchange exclusion covers it VERBATIM; and a multi-carrier PHYSICAL-CONE SCAN over 16 edges x 5 masses finds NO NONZERO PSD PAIRING FOR EITHER OPERATOR, so theta\'s surviving room is a PROOF GAP and not an exhibited positivity AND NEITHER IS THETA-PRIME\'S -- the scan being a SAMPLE, it proves neither existence nor absence\nlattice_wide: THE VERDICT, THE PRICE, THE CONDITIONED RIDER, AND THE DOWNSTREAM: THETA-PRIME STRICTLY DOMINATES on the displayed conventions and fixtures -- every landed certificate SURVIVES OR IMPROVES (Block 142\'s no-preservation, Block 143\'s X_0 uniqueness, Block 145\'s Hermiticity verdict, Block 147/148\'s ensemble no-go) while the covariance LOSES ITS GAUGE INSERTION and the closure STRENGTHENS from "massless" to "identically zero" on the whole atlas SUBJECT TO QUALIFIER B -- and the SINGLE axis on which theta beats theta\', the atlas-global Hermiticity locus at 46 dimensions against 44, is PHYSICALLY INERT because BOTH kernels sit inside {b = 0} where BOTH mass Grams vanish identically, so the two extra theta dimensions are two extra MASSLESS CARRIERS and bareness costs exactly that and nothing else; BUT THE DISPLACEMENT IS PUT TO THE OWNER AS A PROPOSAL AND NEVER AS A RETROACTIVE EDIT, NO LANDED NOTE IS MODIFIED BY THIS BLOCK, and the ADOPTION LEDGER is CHECKER-CORRECTED and stands at AT LEAST SEVEN LANDED CONSTANTS, NEVER "THREE" -- (1) the Hermiticity necessity rank 18 -> 20; (2) its kernel 46 -> 44; (3) the shear-free residual 2 -> 4; (4) Block 142\'s inertia census {(2,0,6),(4,0,4),(6,0,2)} -> the UNIFORM {(4,0,4)}; (5) Block 142\'s pairing entry A[1,2] = -19m/160 -> 7/320, which is m-FREE; (6) Block 145\'s LIVE-SEAM PAIR count 4 -> 2, with singletons 12 and triples 0 UNCHANGED; and (7) Block 147\'s migration CORE restated THROUGH THE CHARACTER, from "zero diagonal" to the 4-OF-8 LIVE SPLIT, this seventh item being the LARGEST COST because Block 147\'s MECHANISM does NOT transfer and the migration statement must be re-proved via Block 148\'s forcing route, which is the strongest argument available to an owner who DECLINES; and THE CONTRACT-B RIDER IS CONDITIONED EXACTLY -- completions in the STAGGERED-PARITY CLASS of the lattice differential, meaning an X_0-ODD Delta K, which the COBOUNDARY and ATLAS-DIFFERENTIAL families ALL SATISFY, move theta\'s pairing diagonal in 4 OF 8 slots and theta\'\'s in 0 OF 8, so SUCH COMPLETIONS CANNOT PERTURB THE THETA-PRIME POSITIVITY OBJECT and the mass moments a completion must fix are read off directly, while a fully GENERIC PARITY-VIOLATING completion moves BOTH diagonals in 8 OF 8 and the rider FAILS for both operators, so the rider HOLDS EXACTLY FOR THE STAGGERED-PARITY CLASS and is stated at that scope and NO WIDER; DOWNSTREAM, the parents\' bare-atlas item is DECIDED AS A PROPOSAL, while the REGISTERED COMPLETION PROGRAM against theta-prime is NOT BUILT, THE OWNER\'S ADOPTION DECISION IS NOT TAKEN AND CANNOT BE TAKEN HERE, the FRAME-TO-MOMENTUM MAP is NEITHER BUILT NOR EXCLUDED, STRATA 147 AND ABOVE remain UNEXPLORED, the cycle-725/726/734 supplied-model firewall is INHERITED UNCHANGED, and the other lane\'s unmerged material is NOT READ, NOT CONSUMED and NOT SUPERSEDED\nRESULT: on the committed 64-member covariant move group, the committed four-chart shear atlas at symbolic (s_x, s_t), the committed 64-modulus carrier family and the committed sixteen healed edge actions, all imported through Block 148\'s committed runner from origin/main only, executing the bare-atlas item of Blocks 148 and 149: THE BARE CHARACTER IS EXACT -- a covariant move (e, p, e, q) is BARE iff p + q is EVEN, kappa = (p + q) mod 2 is a HOMOMORPHISM onto Z_2 on all 4,096 composites, the bare set is ker kappa at INDEX 2 and ORDER 32 (16 translations + 16 reflections), the gauge requirement is the exact DICHOTOMY {I, r_t} vs {r_x, r_x r_t} on all four charts with NO OVERLAP, and bare means PRESERVING THE TWO DIAGONAL CHART CLASSES -- reconciling Block 148\'s 4 bare OS reflections and 16 bare translations with Block 149\'s counts and its EXACTLY-4 threshold stabilizer; THE MECHANISM IS THAT BARENESS IS X_0-COMMUTATION, g X_0 = (-1)^kappa(g) X_0 g on all 64 moves (32/32, no exceptions), and with X_0 H_q X_0 = H_q, X_0 K X_0 = -K and the support lemma this FORCES the generic rule that an X_0-ODD operator has an IDENTICALLY ZERO H_q-diagonal and a K-diagonal LIVE IN 4 OF 8 SLOTS UNIFORMLY while an X_0-EVEN operator has the reverse, making BLOCK 147\'S MIGRATION CORE A ONE-LINE COROLLARY and giving diag Herm([theta\' Q]_++) = m diag G\' on ALL SIXTEEN EDGES, PURE MASS GRAM and CONNECTION-FREE; THE QUENCHED CHAIN returns the theta\' Hodge defect as CARRIER-DEPENDENT (0 flat, 8 at both witnesses, 16 generic, coefficient rank 14 -- correcting a phrasing that is theta\'s), the Hermiticity necessity at rank 20 / kernel 44 against 18 / 46 with the loci INCOMPARABLE (stacked 22, meet 42, spanning the 48-dim {b = 0}) and both kernels forcing the seam dead so Block 145\'s verdict survives verbatim, the shear-free residual 4 against 2 and INERT, and the seam at COEFFICIENT RANK 6 with four diagonal entries and a LIVE TRACE against coefficient rank 4, traceless and hyperbolic, on THE SAME eight odd-slice moments; THE CLOSURE CARRIES BOTH QUALIFIERS -- the chart-0/1 forcing is generically RANK 8 FOR BOTH but theta\'\'s determinant (s_t^2 + s_x^2)^6 (4 m^2 + s_t^2 + s_x^2)^2 / 2^48 is POSITIVE EVERYWHERE while theta\'s s_t^8 (2 m^2 + s_t^2)^4 / 2^48 VANISHES ON THE WHOLE s_t = 0 LINE where theta collapses to rank 4 and theta\' stays 8; and the atlas-wide closure is PSD-CONDITIONAL at 16/16 for theta\' against 4/16 for theta while the LITERAL identity is 4/16 FOR BOTH -- with the staircase census UNIFORM {(4,0,4)}, the escape witness giving theta\' a LIVE PSD MASS GRAM at inertia (4,4,0) that THETA CAN NEVER HAVE, X_0\'s uniqueness UNTOUCHED at {X, J} rank 16 for both, and the cone scan finding NO nonzero PSD pairing FOR EITHER so theta\'s surviving room is a PROOF GAP; AND THE VERDICT IS THAT THETA-PRIME STRICTLY DOMINATES, AS A PROPOSAL FOR THE OWNER AND NEVER A RETROACTIVE EDIT, the single theta advantage (kernel 46 vs 44) being PHYSICALLY INERT, the ADOPTION LEDGER standing at AT LEAST SEVEN landed constants (18->20, 46->44, 2->4, the census -> uniform {(4,0,4)}, A[1,2] = -19m/160 -> the m-FREE 7/320, the live-seam pairs 4->2 with singletons 12 and triples 0 unchanged, and Block 147\'s core restated via the character), and THE CONTRACT-B RIDER HOLDING EXACTLY FOR THE STAGGERED-PARITY CLASS, where an X_0-odd Delta K moves theta 4/8 and theta\' 0/8, and FAILING for a generic parity-violating completion that moves both 8/8: ONE PARITY EXPLAINS THE LANE, AND IT RECOMMENDS THE OTHER OPERATOR\nDECISION_CUT: TAKE THE OWNER\'S ADOPTION DECISION on theta\' -- it is an OWNER-LEVEL convention change, it is NOT this block\'s to take, and it is now PRICED at AT LEAST SEVEN landed constants with Block 147\'s mechanism named as the largest cost; REGISTER THE COMPLETION PROGRAM AGAINST THETA-PRIME and, when registering it, TEST WHETHER EACH COMPLETION LIES IN THE STAGGERED-PARITY CLASS (X_0-odd Delta K), because the rider that motivates the displacement holds EXACTLY for that class and FAILS for a generic parity-violating completion which moves both diagonals 8 of 8 -- the coboundary and atlas-differential families ALL qualify, so the rider applies to the program AS IT STANDS, but a parity-violating registration would have to be re-argued from scratch; EXHIBIT OR EXCLUDE A POSITIVE PAIRING for either operator, since the cone scan is a SAMPLE and returns none for BOTH, so theta\'s surviving room is a PROOF GAP and theta\'\'s live PSD MASS GRAM at the escape witness is an OBJECT and not a PAIRING; BUILD OR EXCLUDE A REGISTERED FRAME-TO-MOMENTUM MAP, unchanged and still neither built nor excluded; ENUMERATE STRATA 147 AND ABOVE, unchanged; LEAVE THE OTHER LANE\'S UNMERGED MATERIAL to that worker -- not read, not consumed, not superseded; and note that composite minimality, the cost-146 geometric gate, the entropy/counting-functional route candidate, the paired-degeneracy observable question and the common nilpotent differential remain named and unexecuted; curved OS is not decided\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero'


SCOPE_KEYS = (
    "bare_character",
    "mechanism_commutation",
    "mechanism_corollary",
    "mechanism_refinement",
    "defect_correction",
    "defect_coefficient_rank",
    "chain_incomparable",
    "chain_seam_ranks",
    "chain_live_trace",
    "split_pure_mass_gram",
    "split_connection_free",
    "qualifier_a",
    "qualifier_b",
    "verdict_dominates",
    "verdict_ledger",
    "verdict_inert",
    "rider_class",
    "rider_counterexample",
    "provenance",
    "independence_disclosure",
    "os_no_go",
    "curved_os_no_go",
    "axiom",
    "firewalls",
    "zero_retirement",
    "zero_score",
    "zero_e2e",
    "n1_n8",
    "w1",
    "n5_verbatim",
)


def scope_certificate(note_text: str) -> dict[str, bool]:
    note = normalized_note(note_text)
    compact = compact_note(note_text)
    return {
        "bare_character": (
            "(p+q)" in compact
            or "index-2" in note
            or "bare character" in note
        ),
        "mechanism_commutation": "x_0-commutation" in note
        or "bareness is" in note,
        "mechanism_corollary": "one-line" in note or "corollary" in note,
        # Whitespace-insensitive so the note may write the refinement either way.
        "mechanism_refinement": "4 of 8" in note or "4/8" in compact,
        "defect_correction": "carrier-dependent" in note,
        "defect_coefficient_rank": "coefficient rank 14" in note,
        "chain_incomparable": "incomparable" in note,
        "chain_seam_ranks": "coefficient rank" in note
        and "6" in note
        and "4" in note,
        "chain_live_trace": "live trace" in note,
        "split_pure_mass_gram": "pure mass gram" in note,
        "split_connection_free": ("no" in note and "shear symbols" in note)
        or "connection-free" in note,
        "qualifier_a": ("s_t = 0" in note or "s_t=0" in compact)
        and ("collapses" in note or "vanishes" in note),
        "qualifier_b": "psd-conditional" in note or "psd forces" in note,
        "verdict_dominates": "strictly dominates" in note
        and "proposal" in note,
        "verdict_ledger": "seven" in note
        or ("18 to 20" in note and "46 to 44" in note)
        or ("18 -> 20" in note and "46 -> 44" in note),
        "verdict_inert": "inert" in note,
        "rider_class": "staggered-parity class" in note,
        "rider_counterexample": "parity-violating" in note,
        "provenance": "contract a" in note or "campaign" in note,
        "independence_disclosure": "cross-context" in note,
        "os_no_go": "not an os no-go" in note,
        "curved_os_no_go": "not a curved os no-go" in note,
        "axiom": "no axiom amendment is justified" in note,
        "firewalls": "firewall" in note,
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
        # Raw substring membership makes the printed eight-line fence
        # byte-identical to its note occurrence.
        "n5_verbatim": N5_FENCE in note_text,
    }


# ---------------------------------------------------------------------------
# claims: the only thing a mutation is allowed to touch
# ---------------------------------------------------------------------------
def build_claims(mutation: str) -> dict[str, object]:
    claims: dict[str, object] = {
        "main_head": CURRENT_MAIN,
        "parent_pin": "resolved",
        "bare_count": BARE_MOVES,
        "homomorphism_composites": HOMOMORPHISM_COMPOSITES,
        "commutation_signature": (COMMUTATION_HITS, OPPOSITE_SIGN_HITS),
        "theta_k_diagonal_slots": THETA_K_DIAGONAL_SLOTS,
        "flat_defect_rank": PRIME_DEFECT_RANKS[0],
        "necessity_rank": PRIME_SYSTEM_RANK,
        "theta_forcing_rank_at_st0": THETA_FORCING_RANK_AT_ST0,
        "literal_collapse": LITERAL_COLLAPSE,
        "theta_live_psd_possible": False,
        "ledger_size": LEDGER_SIZE,
        "adoption_ledger": ADOPTION_LEDGER,
        "generic_completion_prime_slots": PARITY_VIOLATING_PRIME_SLOTS,
        "required_scope_keys": SCOPE_KEYS,
    }
    if mutation == "stale_main_authority":
        claims["main_head"] = STALE_MAIN
    elif mutation == "stale_parent_authority":
        claims["parent_pin"] = "stale"
    elif mutation == "wrong_bare_count":
        claims["bare_count"] = BARE_TRANSLATIONS
    elif mutation == "break_kappa_homomorphism":
        claims["homomorphism_composites"] = HOMOMORPHISM_COMPOSITES - 1
    elif mutation == "flip_commutation_sign":
        claims["commutation_signature"] = (
            OPPOSITE_SIGN_HITS,
            COMMUTATION_HITS,
        )
    elif mutation == "claim_full_k_diagonal":
        claims["theta_k_diagonal_slots"] = HALF
    elif mutation == "claim_flat_defect_full_rank":
        claims["flat_defect_rank"] = PHYS
    elif mutation == "wrong_necessity_rank":
        claims["necessity_rank"] = THETA_SYSTEM_RANK
    elif mutation == "claim_theta_forcing_survives":
        claims["theta_forcing_rank_at_st0"] = FORCING_RANK
    elif mutation == "claim_literal_collapse":
        claims["literal_collapse"] = PSD_CONDITIONAL_COLLAPSE
    elif mutation == "claim_theta_live_psd":
        claims["theta_live_psd_possible"] = True
    elif mutation == "claim_three_constants":
        claims["ledger_size"] = 3
    elif mutation == "break_ledger_item":
        claims["adoption_ledger"] = WRONG_LEDGER
    elif mutation == "claim_rider_unconditional":
        claims["generic_completion_prime_slots"] = 0
    elif mutation == "drop_n5_fence":
        claims["required_scope_keys"] = tuple(
            key for key in SCOPE_KEYS if key != "n5_verbatim"
        )
    return claims


# ---------------------------------------------------------------------------
# gates: pure functions of the measured facts and the claims
# ---------------------------------------------------------------------------
BARE_GAUGE_PROFILE = ((BARE_GAUGES,) * 4,)
NONBARE_GAUGE_PROFILE = ((NONBARE_GAUGES,) * 4,)
THETA_PSD_CONDITIONAL = 4                # PSD + dead seam kills only 4 edges
PRIME_LIVE_SEAM_PAIRS = 2


def evaluate_gates(
    facts: Facts, claims: dict[str, object], elapsed_ns: int
) -> dict[str, bool]:
    authority = facts.authority
    parent_blobs_ok = (
        authority.parent_artifact_blobs
        if claims["parent_pin"] == "resolved"
        else authority.stale_parent_artifact_blobs
    )
    gate_a = bool(
        AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_BARE_CHARACTER_BOUNDED_THEOREM_NOTE_2026-08-20.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_SIGN_LAYER_COMPARISON_BOUNDED_THEOREM_NOTE_2026-08-20.md",
            "scripts/admissibility_dirac_kahler_sign_layer_comparison_2026_08_20.py",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_SHEAR_GAUGE_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-08-20.md",
            "scripts/admissibility_dirac_kahler_shear_gauge_classification_2026_08_20.py",
        )
        and PARENT_ARTIFACTS
        == (BLOCK152_NOTE, BLOCK152_RUNNER, BLOCK149_NOTE, BLOCK149_RUNNER)
        and len(PARENT_ARTIFACT_BLOBS) == len(PARENT_ARTIFACTS)
        and facts.main_head == claims["main_head"]
        and authority.fixed_authority
        and authority.parent_ref_and_ancestry
        and parent_blobs_ok
    )

    gate_b = bool(
        facts.inertia_calibration
        and facts.hermitian_conventions_agree
        and facts.descent_pinned
        and facts.unmatched_moves == 0
        and facts.bare_moves == claims["bare_count"]
        and facts.bare_translations == BARE_TRANSLATIONS
        and facts.bare_reflections == BARE_REFLECTIONS
        and facts.character_law
        and facts.homomorphism_composites
        == (claims["homomorphism_composites"], HOMOMORPHISM_COMPOSITES)
        and facts.kappa_onto
        and facts.composition_pinned[:2]
        == (COMPOSITION_SAMPLE_PAIRS, COMPOSITION_SAMPLE_PAIRS)
        and facts.composition_pinned[2:]
        in ((0, 0), (HOMOMORPHISM_COMPOSITES, HOMOMORPHISM_COMPOSITES))
        and facts.bare_subgroup == (True, True, True, BARE_INDEX)
        and facts.gauge_dichotomy
        == (BARE_GAUGE_PROFILE, NONBARE_GAUGE_PROFILE, True)
        and facts.diagonal_class_law
        and facts.chart_image_sizes == (1,)
        and facts.bare_cross_validated
        == (CROSS_VALIDATED_PAIRS, CROSS_VALIDATED_PAIRS)
        and facts.bare_os_reflections == (BARE_OS_REFLECTIONS, True)
        and facts.os_reflections == OS_REFLECTIONS
        and facts.half_preservers == HALF_PRESERVERS
        and facts.bare_half_preserving == BARE_HALF_PRESERVING
        and facts.threshold_stabilizer == tuple(sorted(THRESHOLD_STABILIZER))
        and not facts.theta_is_bare
        and facts.theta_prime_is_bare
        and facts.theta_gauges == tuple(sorted(b148.THETA_GAUGES))
        and facts.theta_prime_gauges == tuple(sorted(BARE_GAUGES))
        and facts.prime_is_xshift_theta
        and facts.exact_no_float
    )

    gate_c = bool(
        facts.commutation
        == (
            claims["commutation_signature"][0],
            claims["commutation_signature"][1],
            GROUP_ORDER,
        )
        and facts.commutation_split == (COMMUTING_MOVES, ANTICOMMUTING_MOVES)
        and facts.hodge_is_x0_even
        and facts.k_laws == (K_EDGE_COUNT,) * 5
        and facts.support_lemma == (True, True)
        and facts.generic_theorem == (True, True)
        and facts.generic_converse
        == (GENERIC_CONVERSE_SLOTS, GENERIC_CONVERSE_SLOTS)
        and facts.theta_hq_diagonal_zero
        and facts.theta_k_diagonal
        == (
            claims["theta_k_diagonal_slots"],
            HALF,
            THETA_K_LIVE_EDGES,
            K_EDGE_COUNT,
        )
        and facts.prime_hq_diagonal_slots == PRIME_GRAM_LIVE_SLOTS
        and facts.prime_k_diagonal_zero_edges == (K_EDGE_COUNT, K_EDGE_COUNT)
        and facts.migration_core == (True, True)
        and facts.action_law_pinned
        and facts.exact_no_float
    )

    gate_d = bool(
        facts.defect_ranks
        == (
            (TT, THETA_DEFECT_RANKS),
            (TP, (claims["flat_defect_rank"],) + PRIME_DEFECT_RANKS[1:]),
        )
        and facts.defect_coefficient_ranks
        == (
            (TT, THETA_DEFECT_COEFFICIENT_RANK),
            (TP, PRIME_DEFECT_COEFFICIENT_RANK),
        )
        and facts.necessity
        == (
            THETA_SYSTEM_RANK,
            THETA_KERNEL_DIM,
            claims["necessity_rank"],
            NCOORD - claims["necessity_rank"],
            True,
            True,
        )
        and facts.kernels_in_b0 == (True, True)
        and facts.seam_dead_forced == (True, True)
        and facts.incomparability
        == (STACKED_RANK, KERNEL_MEET, KERNEL_SPAN, True, True)
        and facts.residual
        == ((TT, THETA_RESIDUAL_RANK), (TP, PRIME_RESIDUAL_RANK))
        and facts.seam_law
        == (
            (
                TT,
                SEAM_ENTRIES,
                THETA_SEAM_DIAGONAL,
                SEAM_MATRIX_RANK,
                THETA_SEAM_COEFFICIENT_RANK,
                True,
                True,
            ),
            (
                TP,
                SEAM_ENTRIES,
                PRIME_SEAM_DIAGONAL,
                SEAM_MATRIX_RANK,
                PRIME_SEAM_COEFFICIENT_RANK,
                True,
                False,
            ),
        )
        and facts.exact_no_float
    )

    gate_e = bool(
        facts.diagonal_law == (DIAGONAL_LAW_EDGES, DIAGONAL_LAW_EDGES, False)
        and facts.prime_diagonal_symbols == (True, False)
        and facts.theta_diagonal_symbols == (False, True)
        and facts.theta_live_diagonal_slots == (THETA_LIVE_DIAGONAL_SLOTS,)
        and facts.prime_structural_zero_slots == PRIME_STRUCTURAL_ZERO_SLOTS
        and facts.forcing_determinants == (True, True, True, True)
        and facts.forcing_ranks
        == ((TT, (FORCING_RANK,)), (TP, (FORCING_RANK,)))
        and facts.forcing_only_odd_shears
        and facts.forcing_slices
        == tuple(
            (
                tag,
                (
                    (claims["theta_forcing_rank_at_st0"],)
                    if shear_t == 0
                    else (theta_rank,)
                ),
                (prime_rank,),
            )
            for tag, _shear_x, shear_t, theta_rank, prime_rank in FORCING_SLICES
        )
        and facts.collapse
        == (
            PSD_CONDITIONAL_COLLAPSE,
            claims["literal_collapse"],
            LITERAL_COLLAPSE,
            LITERAL_COLLAPSE,
        )
        and facts.psd_conditional
        == (THETA_PSD_CONDITIONAL, PSD_CONDITIONAL_COLLAPSE)
        and facts.literal_zero_edges == tuple(sorted(CHART01_EDGES))
        and facts.census == ((TT, THETA_CENSUS), (TP, PRIME_CENSUS))
        and facts.hermitian_edges == (HERMITIAN_EDGES, HERMITIAN_EDGES)
        and facts.escape_witness
        == (True, True, ESCAPE_INERTIA, THETA_WITNESS_INERTIA)
        and facts.theta_never_live_psd
        == (not bool(claims["theta_live_psd_possible"]))
        and facts.anticommutators
        == (
            (ANTICOMMUTATOR_RANK,),
            (ANTICOMMUTATOR_RANK,),
            (X0_ANTICOMMUTATOR_RANK,),
            ANTICOMMUTATOR_RANK,
        )
        and facts.cone_scan == (CONE_SCAN_CARRIERS, CONE_SCAN_PSD_HITS)
        and facts.exact_no_float
    )

    gate_f = bool(
        facts.kernel_difference == KERNEL_DIFFERENCE
        and facts.theta_only_directions
        == (THETA_ONLY_KERNEL_DIRECTIONS, THETA_KERNEL_DIM)
        and facts.theta_only_pairing_mass_free
        and facts.both_kernels_massless
        and facts.ledger_theta_reproduced
        and len(facts.adoption_ledger) == claims["ledger_size"]
        and facts.adoption_ledger == tuple(claims["adoption_ledger"])
        and facts.live_seam_residue
        == (LIVE_SEAM_SINGLETONS, PRIME_LIVE_SEAM_PAIRS, LIVE_SEAM_TRIPLES)
        and facts.exact_no_float
    )

    gate_g = bool(
        facts.completion_classes == COMPLETION_CLASSES
        and facts.parity_violating
        == (
            PARITY_VIOLATING_LABEL,
            False,
            PARITY_VIOLATING_THETA_SLOTS,
            claims["generic_completion_prime_slots"],
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
        and N5_FENCE.count("\n") == 7
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
            "also pin the label composition law against cover matrix products "
            "on all 64 x 64 composites, not just the 60-pair spot"
        ),
    )
    arguments = parser.parse_args()
    mutation = arguments.mutation
    started_ns = time.monotonic_ns()

    # Every measurement happens once, before any mutation flag is consulted,
    # so a mutation can only rewrite a CLAIM.  No gate can cascade into
    # another because no gate feeds a measurement.
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
            raise AssertionError(
                "mutation did not fail exactly its own gate"
            )

    checks = Checks()
    checks.check(
        "A-authority",
        "main plus the committed Block 152 note/runner and Block 149 note/runner artifacts are content-bound",
        gate_values["A"],
    )
    checks.check(
        "B-bare-character",
        "a covariant move (e,p,e,q) is BARE -- its transported chart differential matching a committed atlas entry with the IDENTITY gauge on ALL FOUR charts -- IF AND ONLY IF p + q is EVEN, independently of the sign; kappa = (p+q) mod 2 is a homomorphism onto Z_2 on all 64 x 64 = 4096 label composites, with the label composition law itself pinned against cover matrix products on a 60-pair spot (all 4096 behind --deep), so the bare set is ker kappa: an INDEX-2 subgroup of order 32, 16 translations and 16 reflections, closed, inverse-closed and with non-bare times non-bare bare; the gauge requirement is an exact DICHOTOMY with EMPTY overlap, {I, r_t} for bare and {r_x, r_x r_t} for non-bare on every one of the four charts with a single chart image each, and the geometric reading is preservation of the two DIAGONAL chart classes; the hash lookup is cross-validated against an explicit symbolic sweep on eight (move, chart) pairs, nothing is unmatched, and every landed count reconciles -- 4 bare OS reflections equal to Block 148's ODD_CENTRED out of 8 honest ones, 16 bare translations, 16 half-preservers, their 8-element intersection and Block 149's threshold stabiliser exactly, with theta not bare, theta' bare and theta' the x-shift composed with theta",
        gate_values["B"],
    )
    checks.check(
        "C-x0-mechanism",
        "on all 64 descended covariant moves g X_0 = (-1)^kappa(g) X_0 g, 32 commuting and 32 anticommuting with ZERO exceptions and ZERO moves satisfying the opposite sign, so BARENESS IS X_0-COMMUTATION; X_0 H_q X_0 = H_q symbolically in all 64 moduli and K = Q - m H_q is real, antisymmetric, m-free, nonzero and X_0-ODD on all 16 healed edges, because H_q is supported on EQUAL and K on OPPOSITE staggered parity; hence the SELECTION RULE, proved for a GENERIC X_0-odd and a GENERIC X_0-even matrix: X_0-odd kills the H_q diagonal, X_0-even kills the K diagonal, both converses live at 8 of 8 slots; Block 147's migration core is therefore a ONE-LINE COROLLARY of theta's X_0-oddness, re-derived here with a zero diagonal and zero trace, and the refinement is carried -- theta's K-diagonal is live on 16 of 16 edges but in 4 OF 8 slots, while theta''s is identically zero on all 16 and its mass Gram is live in 4",
        gate_values["C"],
    )
    checks.check(
        "D-quenched-chain",
        "the H_q-preservation defect is CARRIER-DEPENDENT and not one rank: 0 at the flat carrier, 8 at both cone witnesses, 16 at the staircase and at a generic cone carrier, the honest invariant being COEFFICIENT RANK 14 against theta's 16; the atlas-global Hermiticity necessity system has RANK 20 and KERNEL 44 under theta' against Block 145's reproduced 18 and 46, both kernels lie inside {b = 0} and both FORCE THE SEAM DEAD so Block 145's verdict survives verbatim; the two loci are INCOMPARABLE, stacked rank 22, meet 42, spanning exactly the 48-dimensional shear-free stratum; the shear-free residual moves 2 to 4; and the seam law sees the SAME eight odd-slice moments at 8 nonzero entries for both, at MOMENT-COEFFICIENT rank 6 with four diagonal moments and a LIVE TRACE for theta' against coefficient rank 4 and zero trace for theta -- coefficient rank, since both Grams have matrix rank 8",
        gate_values["D"],
    )
    checks.check(
        "E-diagonal-split",
        "diag Herm([theta' Q]_++) = m diag G' on ALL SIXTEEN edges with NO shear symbols in it -- PURE MASS GRAM and CONNECTION-FREE -- while under theta the law is FALSE and the diagonal is m-free, connection-carried and live in 4 of 8 slots on every edge; QUALIFIER A is a checked certificate: the chart-0/1 forcing is rank 8 for BOTH at the committed fixture and involves only the eight odd shears, but the determinants DIFFER, theta' reproducing Block 148's while theta carries s_t^8 (2 m^2 + s_t^2)^4 / 2^48, which VANISHES on s_t = 0, and at (3/5, 0) theta's rank COLLAPSES to 4 while theta' stays at 8; QUALIFIER B likewise: with the seam dead diag A' = 0 on 16 of 16 and PSD then forces A' = 0 on 16 of 16, but the LITERAL identical vanishing is 4 of 16 for BOTH, on exactly the four chart-0/1 edges; the staircase census is uniform (4,0,4) for theta' against Block 142's three classes, neither operator is Hermitian on any edge, the anticommutant stays rank 16 for both and 0 for X_0, a five-carrier cone scan finds no nonzero PSD pairing, and the escape witness gives theta' a live PSD mass Gram at inertia (4,4,0) which theta can never have, its zero diagonal making every 2x2 principal minor a negative square",
        gate_values["E"],
    )
    checks.check(
        "F-verdict-support",
        "the one axis on which theta beats theta' -- the Hermiticity locus, 46 against 44 -- is PHYSICALLY INERT: both kernels lie in {b = 0} where both mass Grams vanish identically, 24 of theta's 46 kernel directions lie outside theta''s, and at an explicit theta-only kernel direction the theta pairing is m-FREE on all sixteen edges; and the adoption cost is a SEVEN-CONSTANT LEDGER, each entry checked in BOTH columns so that theta reproduces the landed value and theta' the new one: 18 -> 20, 46 -> 44, 2 -> 4, the inertia census from three classes to the single (4,0,4), the displayed pairing entry A[1,2] from -19m/160 to a MASS-FREE 7/320, the live-seam PAIR count from 4 to 2 with singletons 12 and triples 0 UNCHANGED, and Block 147's migration core itself from a structurally zero diagonal to four live slots",
        gate_values["F"],
    )
    checks.check(
        "G-completion-rider",
        "three connection-side completions IN THE STAGGERED-PARITY CLASS -- the coboundary w Omega*, a generic four-coefficient atlas-differential combination and a sign-flipped variant -- are all X_0-ODD and all move theta's pairing diagonal in 4 of 8 slots while moving theta''s in ZERO; and the counterexample is exhibited rather than assumed absent: a FULLY GENERIC 32x32 connection-side completion is NOT X_0-odd and moves BOTH diagonals in 8 of 8 slots, so the contract-B rider holds WITHIN the parity class and FAILS outside it and is stated with that restriction",
        gate_values["G"],
    )
    checks.check(
        "H-note-scope",
        "the bare character with its index-2 kernel, the X_0-commutation mechanism with its one-line corollary and its 4-of-8 refinement, the carrier-dependent defect correction with its coefficient rank 14, the incomparable loci with their moment-coefficient seam ranks and live trace, the pure-mass-gram connection-free diagonal, qualifier A with its s_t = 0 collapse, qualifier B with its PSD-conditional reading, the strictly-dominates verdict put as a proposal with its seven-constant ledger and its inert advantage, the staggered-parity class rider with its parity-violating counterexample, the provenance, the cross-context disclosure, the firewalls and the exact N5 fence are present",
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
