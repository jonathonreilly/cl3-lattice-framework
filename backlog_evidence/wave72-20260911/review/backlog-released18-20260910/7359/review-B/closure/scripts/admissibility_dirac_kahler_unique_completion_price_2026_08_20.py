#!/usr/bin/env python3
# Final path: scripts/admissibility_dirac_kahler_unique_completion_price_2026_08_20.py
"""Block 154: THE UNIQUE COMPLETION, ITS PRICE, AND A POSITIVITY THAT IS NOT A NO-GO.

Block 153 closed the canonical-operator question by proposing the odd-x-centred
bare reflection theta' = (-1, 7, -1, 1), and handed forward, as its own named
decision cut, campaign contract B: REGISTER THE COMPLETION PROGRAM AGAINST
THETA-PRIME, and when registering it, TEST WHETHER EACH COMPLETION LIES IN THE
STAGGERED-PARITY CLASS.  This runner executes that program to the end, and the
answer is neither the hoped-for "the door opens" nor the feared "the door is
shut": the completion EXISTS, is essentially UNIQUE, and costs more than the
positivity it buys.  Six findings, each a checked certificate:

  * THE PAIRING SPLITS INTO THREE BLOCKS, AND ONLY ONE OF THEM IS REACHABLE.
    Writing DEAD = (1, 3, 4, 6) for the four half-carrier slots on which the
    mass Gram G' = Herm([theta' H_q]_{++}) has a structurally zero diagonal and
    LIVE = (0, 2, 5, 7) for the other four -- the split is exactly the staggered
    sign of X_0 restricted to the half carrier -- the Hermitian pairing
    A' = m G' + Herm([theta' K]_{++}) splits on ALL SIXTEEN healed edges as:
    DEAD-DEAD, pure mass, m (b_31 + b_33)/8 at (1,3) and -m (b_11 + b_13)/8 at
    (4,6) and zero elsewhere; LIVE-LIVE, pure mass and DIAGONAL,
    m/4 diag(b_30, b_32, -b_10, -b_12); and DEAD-LIVE, PURE CONNECTION, live in
    16 of 16 slots on every edge.  THE SOLVE'S SINGLE-MONOMIAL READING OF THAT
    THIRD BLOCK IS CORRECTED IN SCOPE: the dead-live entries are single b-modulus
    monomials on 4 OF 16 EDGES ONLY -- the four chart-0/1 edges -- and on the
    other twelve they run to NINE monomials over FORTY-EIGHT moduli.  And the
    REACH THEOREM, proved for a GENERIC X_0-odd antisymmetric Delta K with all
    SIXTY-FOUR free parameters and not for a fixture: such a Delta K lands
    EXACTLY on the 32 dead-live slots, all of them live, at RANK 16 onto the 16
    independent targets -- with both controls exhibited, a fully generic
    antisymmetric Delta K reaching all 64 slots and an X_0-EVEN one reaching
    exactly the complementary dead-dead and live-live 32;
  * THE COMPLETION EXISTS, IS A DELETION, AND IS UNIQUE WHERE IT IS DETERMINED.
    Restricted to the support of the edge differential itself, the dead-live
    cancellation system is SOLVABLE ON 16 OF 16 EDGES and kills all 36
    independent half-slots, not just the 16 targeted ones.  Its minimal support
    is EXACTLY HALF the differential's hops -- 16 of 32 on SIX edges and 24 of 48
    on the other TEN -- and every determined coefficient is EXACTLY -1, with the
    complementary half entirely free: the completion is a DELETION of a uniquely
    determined set of hops, d_total = d on the surviving half and 0 on the
    deleted half.  The induced Delta K is CARRIER-INDEPENDENT (its only symbols
    are the atlas fixture s_x, s_t) and X_0-ODD on all sixteen edges, so the
    completion IS in Block 153's staggered-parity class.  THE PRICE IS PAID
    HERE: Delta K is NOT ANTISYMMETRIC, so K_total is not either, so
    Q_c + Q_c^dagger != 2 m H_q -- the symmetric part has RANK 8 on every edge.
    Block 143's antisymmetric-residue character, which every landed block on this
    lane has used, DOES NOT SURVIVE THE COMPLETION;
  * THE COMPLETION IS BULK, NOT BOUNDARY, AND BREAKS TRANSLATION INVARIANCE.
    Over the full 128-hop nearest-neighbour completion space (256 real
    parameters, carrier-independent), the cancellation target has RANK 104 while
    the SEAM-SUPPORTED completions reach only RANK 32: no completion supported on
    the reflection seam can do it.  Dropping every hop that touches a cover time
    slice makes the system INFEASIBLE for slices 0, 4, 5, 6 AND 7 at the probe
    edge; ATLAS-WIDE exactly TWO verdicts occur, whose COMMON CORE is the
    SOLVE'S FOUR, and SLICE 4 IS NECESSARY ON 14 OF THE 16 EDGES, so the solve's
    set is a core and not the answer.  A UNIT-TIME-TRANSLATION-COVARIANT completion is INFEASIBLE
    (rank 256, augmented 257) and so is a UNIT-X one (rank 224, augmented 225),
    while a PERIOD-2 time-covariant one EXISTS (rank 244, augmented 244).  The
    registered premise is therefore a bulk, period-2 object;
  * THE POSITIVITY IS REAL, AND IT IS NOT OPEN.  The completed pairing is
    m [theta' H_q]_{++} EXACTLY -- not merely in Hermitian part, and identically
    on all sixteen edges -- because [theta' K_total]_{++} vanishes IDENTICALLY.
    The PSD forcing that Block 148 ran at RANK 8 on the uncompleted pairing
    collapses to RANK 2 on the completed one, and the two surviving conditions
    are EQUALITIES: b_31 + b_33 = 0 and b_11 + b_13 = 0.  So the positive domain
    is CODIMENSION 2 in the 64-modulus family, NOT an open set, and on it four
    SIGN conditions are each independently necessary -- sigma_10, sigma_12 >= 0
    and sigma_30, sigma_32 <= 0 for m > 0 -- each violation dropping the inertia
    to (3, 4, 1) and each EQUALITY violation to (5, 2, 1), in the committed
    (n_+, n_0, n_-) convention.  At the cone witness the pairing is
    diag(15m/64, 0, 15m/64, 0, 0, 15m/64, 0, 15m/64) at inertia (4, 4, 0) with a
    definite live block (4, 0, 0) and eigenvalues {0, 15m/64}; at m < 0 it
    reverses to (0, 4, 4) and at m = 0 it dies to (0, 8, 0); it vanishes
    IDENTICALLY on the flat carrier, and it depends on exactly FOUR of the 64
    moduli, b_10, b_12, b_30, b_32, disjoint from the four the forced locus uses;
  * THE HERMITICITY BREAK IS REAL AND PREMISE-CONDITIONAL.  The completed
    atlas-global Hermiticity system has RANK 2 and KERNEL 62 against Block 153's
    reproduced 20 / 44 for theta' and Block 145's reproduced 18 / 46 for theta,
    with an EXACT row space {b_11 - b_13, b_31 - b_33}; the kernel is NOT inside
    {b = 0}; and at the cone witness the pairing is simultaneously HERMITIAN,
    SEAM-LIVE and MASS-CARRYING, so Block 145's verdict that the mass never
    enters an atlas-globally Hermitian pairing is BROKEN -- CONDITIONALLY ON THE
    COMPLETION, and on nothing else, since the uncompleted system still stands at
    rank 20 and the uncompleted pairing still dies when the odd shears are
    forced.  The four antiHermitian mass entries at (1,3), (3,1), (4,6), (6,4)
    are UNTOUCHABLE by any staggered-parity completion, which is why the break
    needs the two equalities rather than being free;
  * AND WHAT IS BOUGHT IS A FREE PAIRING, WHICH IS WHY NOTHING IS REGISTERED.
    The completed pairing is EDGE-INDEPENDENT -- the same 8x8 block on all
    sixteen edges -- and carries ZERO CONNECTION DATA: [theta' K_c]_{++} = 0
    while K_c itself stays nonzero, X_0-odd and shear-carrying, so the connection
    survives as an object and is invisible to the pairing.  A positivity that
    cannot see the connection does NOT reduce the lane's calibration gap, so THE
    CONTENTS OF THE WOULD-BE REGISTRATION ARE DISPLAYED AND NO REGISTRATION IS
    PROPOSED: this is a STUDY of what contract B would cost, handed to the owner
    beside Block 153's adoption proposal as a two-item PANEL.

Every scientific comparison below is exact SymPy arithmetic; no floats anywhere;
the integer monotonic clock is used only for the runtime gate.

TOOLING DISCLOSURE: every inertia in this runner is computed by SYMMETRIC
CONGRUENCE, delegated to the committed Block 144 helper through the Block
153/148/147/145 import chain, so the tool this block reasons with is exactly the
blob gate A pins.  The Block 142/143 helper counts DISTINCT real roots and is
unsound on these degenerate spectra; it is deliberately not used, and both the
calibration diag(1,1,-2,-2,0) and the (n_+, n_0, n_-) ORDER of the returned
triple are asserted in gate B before any inertia is read.

PROVENANCE DISCLOSURE: the 64-modulus carrier model, the cover Hodge, the
antiperiodic quotient, the action law, the half pairing, the connection data, the
Block 141 healing weights, the odd-centred theta', the staggered parity X_0, the
four-chart atlas, the 64 covariant moves, the escape witness and the admissible
cone are ALL COMMITTED objects (Blocks 105/134/137/141/142/143/144/145/147/148/
153), imported and never re-derived.  This block adds only the three-block split
with its scope correction, the reach theorem, the deletion completion with its
uniqueness and its antisymmetry price, the locality and covariance honesty
theorems, the codimension-2 positive domain, the conditional Hermiticity break
and the free-pairing characterisation.  This is CAMPAIGN CONTRACT B executed as
its own block; the external literature on reflection positivity and on lattice
Dirac-Kahler completions is REFERENCED nowhere and BORROWED nowhere, and every
statement below is re-proved in-framework.

HYPOTHESES, named and not imported: (H1) the pairing convention is
[X Q]_{++} on the half carrier {p = 0,1}, exactly as Blocks 142/144/145/147/148/
149/153 used it.  (H3) "positive" is a statement about the HERMITIAN part
A = (P + P^dagger)/2, as Block 148 established.  (H4) the carrier family is the
committed 64-modulus one and the physical cone is nu > 0, |sigma| < 1 per cell.
(H5-154) a CONNECTION-SIDE COMPLETION is an additive perturbation Delta d of a
healed edge differential, registered as a premise with its own parameters and its
own support; its induced Delta K = quotient(i (H Delta d + Delta d^dagger H)) is
carrier-LINEAR by construction; the STAGGERED-PARITY CLASS is those with an
X_0-odd Delta K, and class membership is MEASURED here, never assumed.

NON-CLAIMS, stated once and enforced by gate H: this block does NOT claim a
first curved OS positivity, it is NOT an OS no-go, it is NOT a curved OS no-go,
it justifies NO axiom amendment, and it proposes NO registration.
"""

from __future__ import annotations

import argparse
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

import admissibility_dirac_kahler_bare_character_2026_08_20 as b153

b148 = b153.b148
b147 = b153.b147
b145 = b153.b145
b144 = b153.b144
b143 = b153.b143
b142 = b153.b142
b141 = b153.b141
b137 = b153.b137
b134 = b153.b134
b105 = b153.b105

MASS = b153.MASS


NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_UNIQUE_COMPLETION_PRICE_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
BLOCK153_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_BARE_CHARACTER_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
BLOCK153_RUNNER = (
    "scripts/admissibility_dirac_kahler_bare_character_2026_08_20.py"
)
BLOCK148_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_GENERAL_MIGRATION_THEOREM_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
BLOCK148_RUNNER = (
    "scripts/admissibility_dirac_kahler_general_migration_theorem_2026_08_20.py"
)

# The four artifacts whose blobs are pinned at the parent commit.  All four are
# IN THIS WORKTREE, so plain worktree/commit blob pins suffice.
PARENT_ARTIFACTS = (
    BLOCK153_NOTE,
    BLOCK153_RUNNER,
    BLOCK148_NOTE,
    BLOCK148_RUNNER,
)
PARENT_ARTIFACT_BLOBS = (
    "0b630bf8050a77944ab527707c2d9cd62d50701e",   # Block 153 note
    "1d8e1d32e3ded5c9203110d2b6100167f136e451",   # Block 153 runner
    "e9d89f0b08402f5252010fc0af16cfc394f94e16",   # Block 148 note
    "28fb45b474ab35896f80db6142b5a46f8892c9c0",   # Block 148 runner
)

# Deliberately literal: this is the complete audit read surface.  Every entry is
# a WORKTREE-READABLE path; the cache envelope stats these, so an
# origin/main-only path here would break the audit (the Block 130 lesson,
# re-learned at the Block 150 landing and inherited through Blocks 151/152/153).
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_UNIQUE_COMPLETION_PRICE_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_BARE_CHARACTER_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/admissibility_dirac_kahler_bare_character_2026_08_20.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_GENERAL_MIGRATION_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/admissibility_dirac_kahler_general_migration_theorem_2026_08_20.py",
)

AUDIT_TIMEOUT_SEC = 600
# The five authority pins below are copied verbatim from the Block 153 runner's
# current values; the landing supervisor refreshes them against origin/main.
CURRENT_MAIN = "005f047923055e6ecd5dc8bce1ffd71765c2ffd8"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
# This block stacks on Block 153, so the parent branch is Block 153's.
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block153-bare-character-20260820"
)
# Landing supervisor: replace this placeholder with the Block 153 branch tip.
# Until it is a 40-hex commit the pin is resolved through PARENT_REF when that
# ref exists and through HEAD otherwise (the parent branch may not be published
# yet); either way the binding is real and verifiable, and the immutable commit
# pin lands with the block.
PARENT_COMMIT = "301f7f8b1553170e655fbb8d6768b06da850370f"
# Block 151's tip: a real ancestor of HEAD that PREDATES both Block 153
# artifacts, so resolving the parent pin there leaves the Block 153 note and the
# Block 153 runner ABSENT while the two Block 148 artifacts still match.  It was
# CHECKED against the Block 152 tip's parent before being pinned: the Block 152
# tip a8d1e42217b573c1a4a77f9a0b164e1a3011ccc2 has this very commit as its
# PARENT, so the two candidates coincide and this is the honest stale control
# FOR THIS PIN SET.  This pin is read ONLY under the stale mutation; the baseline
# gate never requires the stale blobs to match.
STALE_PARENT_COMMIT = "26fad1c0b18073dc1121be27adcc531c5ea0651a"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "wrong_split_scope",
    "break_reach_rank",
    "claim_coefficients_free",
    "claim_antisymmetry_kept",
    "claim_unit_translation",
    "claim_seam_supportable",
    "claim_domain_open",
    "wrong_witness_inertia",
    "claim_connection_data",
    "wrong_kernel_dim",
    "claim_break_unconditional",
    "claim_registration_proposed",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "wrong_split_scope": "B",
    "break_reach_rank": "B",
    "claim_coefficients_free": "C",
    "claim_antisymmetry_kept": "C",
    "claim_unit_translation": "D",
    "claim_seam_supportable": "D",
    "claim_domain_open": "E",
    "wrong_witness_inertia": "E",
    "claim_connection_data": "E",
    "wrong_kernel_dim": "F",
    "claim_break_unconditional": "F",
    "claim_registration_proposed": "G",
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
    return b153.no_float(value)


def zero(matrix: sp.MatrixBase) -> bool:
    return b153.zero(matrix)


def congruence_inertia(matrix: sp.MatrixBase) -> tuple[int, int, int]:
    """Exact (n_positive, n_zero, n_negative) WITH multiplicity, by congruence.

    Delegated to the COMMITTED Block 144 helper through the Block 153/148/147/145
    import chain, so that the tool this block reasons with is exactly the blob
    gate A pins.  b142.inertia / b143.inertia count DISTINCT real roots and are
    unsound on these degenerate spectra; the calibration AND the order of the
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
# the committed model, imported wholesale through Block 153
# ---------------------------------------------------------------------------
SIZE = b153.SIZE                         # 32 cover sites
COVER_T = b153.COVER_T                   # 8
PHYS_T = b153.PHYS_T                     # 4
LX = b153.LX                             # 4
PHYS = b153.PHYS                         # 16 quotient sites
HALF = b153.HALF                         # 8 sites in the positive-time half
PLUS = b153.PLUS
THETA = b153.THETA
THETA_PRIME_OP = b153.THETA_PRIME_OP
X0 = b153.X0
CELLS = b153.CELLS
COORDS = b153.COORDS                     # the 64 carrier moduli
EDGE_KEYS = b153.EDGE_KEYS               # the 16 healed edges
CHART01_EDGES = b153.CHART01_EDGES
ODD_SHEAR_COORDS = b153.ODD_SHEAR_COORDS  # the 8 odd-time-slice shear moments
SHEAR_COORDS = b153.SHEAR_COORDS          # all 16 shear moments
B_MODULUS = b153.B_MODULUS
FREE_MODULI = b153.FREE_MODULI
HEALING_WEIGHTS = b153.HEALING_WEIGHTS
MOVE_MATRIX = b153.MOVE_MATRIX
SHEAR_X, SHEAR_T = b153.SHEAR_X, b153.SHEAR_T
COVER_FREE = b153.COVER_FREE              # 32x32, 64 moduli
HQ_FREE = b153.HQ_FREE                    # 16x16, 64 moduli

NCOORD = len(COORDS)                      # 64

# the DEAD/LIVE split of the half carrier is READ OFF the committed X_0, never
# hard-coded; gate B pins it against the zero diagonal of the mass Gram.
DEAD = tuple(k for k in range(HALF) if X0[k, k] == -1)
LIVE = tuple(k for k in range(HALF) if X0[k, k] == 1)
DEAD_LIVE = tuple((k, j) for k in DEAD for j in LIVE)


def herm(matrix: sp.MatrixBase) -> sp.Matrix:
    """The HERMITIAN part (M + M^dagger)/2.  The pairing carries i's, so .H is
    not .T here; gate B pins this against the committed Block 148 helper."""
    matrix = sp.Matrix(matrix)
    return sp.expand((matrix + matrix.H) / 2)


def half_block(matrix: sp.MatrixBase) -> sp.Matrix:
    """[theta' M]_{++} on the half carrier {p = 0,1} (H1)."""
    return sp.expand(PLUS.T * THETA_PRIME_OP * matrix * PLUS)


def residue(differential: sp.Matrix) -> sp.Matrix:
    """K = quotient(i (H d + d^dagger H)) on the 64-modulus carrier family."""
    return sp.expand(
        b145.quotient(
            sp.expand(
                sp.I
                * (
                    COVER_FREE * differential
                    + differential.H * COVER_FREE
                )
            )
        )
    )


def cover_index(time_slice: int, position: int) -> int:
    return (time_slice % COVER_T) * LX + (position % LX)


def support_of(matrix: sp.MatrixBase) -> tuple:
    return tuple(
        sorted(
            (row, column)
            for row in range(SIZE)
            for column in range(SIZE)
            if sp.expand(matrix[row, column]) != 0
        )
    )


def monomial_rows(expression, parameters, index) -> list:
    """Rows of "expression = 0 identically in the moduli and the shears".

    One row per monomial in (the 64 moduli, s_x, s_t); the entries are the
    coefficients of the completion parameters and the right-hand side is minus
    the parameter-free part.  This is the checker's route, kept verbatim.
    """
    generators = list(COORDS) + [SHEAR_X, SHEAR_T]
    polynomial = sp.Poly(sp.expand(expression), *generators)
    rows = []
    for _monomial, coefficient in polynomial.terms():
        coefficient = sp.expand(sp.sympify(coefficient))
        row = [0] * len(parameters)
        constant = 0
        for term in sp.Add.make_args(coefficient):
            symbols = term.free_symbols & set(parameters)
            if not symbols:
                constant += term
            else:
                symbol = symbols.pop()
                row[index[symbol]] += term.coeff(symbol, 1)
        rows.append((row, -constant))
    return rows


def feasible(matrix: sp.Matrix, rhs: sp.Matrix) -> tuple:
    rank = matrix.rank()
    augmented = matrix.row_join(rhs).rank()
    return rank, augmented, rank == augmented


# ---------------------------------------------------------------------------
# the certificate constants this runner is claiming
# ---------------------------------------------------------------------------
K_EDGE_COUNT = 16                        # the sixteen healed edges
HALF_SLOTS = HALF * (HALF + 1) // 2      # 36 independent half-carrier slots
DEAD_SLOTS = (1, 3, 4, 6)
LIVE_SLOTS = (0, 2, 5, 7)
DEAD_LIVE_TARGETS = 16                   # |DEAD| x |LIVE|
DEAD_LIVE_REACHED = 32                   # both orientations
PURE_SPLIT_EDGES = 4                     # the SCOPE CORRECTION: 4 of 16
IMPURE_MAX_MONOMIALS = 9
IMPURE_MODULI = 48
REACH_PARAMETERS = 64                    # a generic X_0-odd antisymmetric dK
REACH_RANK = 16                          # onto the 16 independent DL targets
CONTROL_GENERIC_PARAMETERS = 120
CONTROL_GENERIC_SUPPORT = 64
CONTROL_EVEN_PARAMETERS = 56
CONTROL_EVEN_SUPPORT = 32
DEAD_LIVE_CLASSES = (("D", "L"), ("L", "D"))
GENERIC_CLASSES = (("D", "D"), ("D", "L"), ("L", "D"), ("L", "L"))
EVEN_CLASSES = (("D", "D"), ("L", "L"))

SMALL_SUPPORT = 32                       # |supp d| on six edges
LARGE_SUPPORT = 48                       # |supp d| on the other ten
SMALL_DELETION = 16                      # 16 of 32 hops deleted
LARGE_DELETION = 24                      # 24 of 48 hops deleted
SMALL_EDGES = 6
LARGE_EDGES = 10
DELETION_COEFFICIENT = sp.Integer(-1)
SYMMETRIC_PART_RANK = 8                  # rank(K_total + K_total^T), the price

HOP_COUNT = 128                          # ordered nearest-neighbour cover links
HOP_PARAMETERS = 256                     # two carrier-free coefficients each
HOP_PROBE_EDGE = (0, 0)
# The seam and slice honesty theorems are run ATLAS-WIDE, on every healed edge,
# not on a probe: a locality claim read at one edge would be a sample.
SEAM_PROBE_EDGES = tuple(sorted(EDGE_KEYS))
SLICE_PROBE_EDGES = tuple(sorted(EDGE_KEYS))
TRANSLATION_CONTROL_EDGE = (2, 2)
SEAM_SLICE = 4                           # the slice the solve's set omitted
FULL_TARGET_RANK = 104
SEAM_IMAGE_RANK = 32
HOP_RANKS = (104,)                       # the same on every healed edge
SEAM_HOPS = 32
BULK_HOPS = 96
NECESSARY_SLICES = (0, 4, 5, 6, 7)       # the SOLVE'S FOUR, CORRECTED
OPTIONAL_SLICES = (1, 2, 3)
# ATLAS-WIDE the verdict is not uniform: two necessary sets occur, their common
# core is the solve's four, and slice 4 is necessary on FOURTEEN of the sixteen
# edges -- so "the solve's set is four" is a statement about the CORE only.
SLICE_VERDICTS = ((0, 4, 5, 6, 7), (0, 5, 6, 7))
COMMON_NECESSARY_SLICES = (0, 5, 6, 7)
SEAM_SLICE_EDGES = 14
UNIT_T_LABEL = (1, 1, 1, 0)
UNIT_X_LABEL = (1, 0, 1, 1)
PERIOD2_LABEL = (1, 2, 1, 0)
PERIOD2_X_LABEL = (1, 0, 1, 2)
PERIOD2_BOTH_LABEL = (1, 2, 1, 2)
COVARIANCE_LABELS = (
    UNIT_T_LABEL,
    UNIT_X_LABEL,
    PERIOD2_LABEL,
    PERIOD2_X_LABEL,
    PERIOD2_BOTH_LABEL,
)
UNIT_T_RANK, UNIT_T_AUGMENTED = 256, 257
UNIT_X_RANK, UNIT_X_AUGMENTED = 224, 225
PERIOD2_RANK = 244
PERIOD2_X_RANK = 180
PERIOD2_BOTH_RANK = 244
STRONG_DEMAND_RANK = 128

COMPLETED_FORCING_RANK = 2               # was 8 before the completion
UNCOMPLETED_FORCING_RANK = 8             # b148's FORCING_RANK, reproduced
DOMAIN_CODIMENSION = 2                   # NOT an open set
SIGN_VIOLATION_INERTIA = (3, 4, 1)
EQUALITY_VIOLATION_INERTIA = (5, 2, 1)
WITNESS_INERTIA = (4, 4, 0)
LIVE_BLOCK_INERTIA = (4, 0, 0)
NEGATIVE_MASS_INERTIA = (0, 4, 4)
ZERO_MASS_INERTIA = (0, 8, 0)
WITNESS_EIGENVALUE = 15 * MASS / 64
POSITIVITY_MODULI = 4                    # b_10, b_12, b_30, b_32
LOCUS_MODULI = 4                         # b_11, b_13, b_31, b_33, disjoint
SCAN_CARRIERS = 6                        # committed cone / staircase carriers
SCAN_ON_LOCUS = 1                        # only one of them meets the locus
SCAN_PSD = 0                             # and NONE of them is live and PSD

UNTOUCHABLE_SLOTS = ((1, 3), (3, 1), (4, 6), (6, 4))
COMPLETED_HERMITICITY_RANK = 2
COMPLETED_KERNEL_DIM = 62
PRIME_SYSTEM_RANK = 20                   # b153's, reproduced
PRIME_KERNEL_DIM = 44
THETA_SYSTEM_RANK = 18                   # b145's, reproduced
THETA_KERNEL_DIM = 46

REGISTRATION_STATUS = "displayed-not-proposed"
REGISTRATION_CONTENTS = (
    (
        "premise",
        "one connection-side Delta d per healed edge, carrier-independent",
    ),
    (
        "support",
        "exactly half of the edge differential's hops: 16 of 32 on six edges, "
        "24 of 48 on ten",
    ),
    (
        "coefficients",
        "every determined coefficient exactly -1, so Delta d = -d there: the "
        "completion is a DELETION",
    ),
    (
        "locality",
        "bulk, not boundary: cover time slices 0, 4, 5, 6, 7 are each necessary "
        "and no seam-supported completion exists",
    ),
    (
        "symmetry",
        "no unit-time and no unit-x translation-covariant representative; a "
        "period-2 time-covariant one exists",
    ),
    (
        "price",
        "K_total loses antisymmetry, so Q_c + Q_c^dagger != 2 m H_q and Block "
        "143's residue character does not transfer",
    ),
    (
        "payoff",
        "the completed pairing is m [theta' H_q]_++ exactly, PSD on a "
        "codimension-2 domain, and carries zero connection data",
    ),
)
REGISTRATION_ITEMS = 7

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
    inertia_order_pinned: bool
    hermitian_conventions_agree: bool
    operator_pinned: bool
    action_law_pinned: bool
    # B: the three-block split and the reach theorem
    dead_live_partition: tuple
    three_block: tuple
    split_scope: tuple
    reach: tuple
    reach_controls: tuple
    # C: the completion mechanics
    solvability: tuple
    minimal_support: tuple
    uniqueness: tuple
    deletion_values: tuple
    deletion_certificate: tuple
    totality: tuple
    carrier_independence: tuple
    parity_membership: tuple
    antisymmetry_broken_edges: int
    antisymmetry_profile: tuple
    # D: the honesty theorems
    hop_space: tuple
    seam: tuple
    slice_necessity: tuple
    translation_tests: tuple
    translation_control: tuple
    strong_demand: tuple
    # E: the positivity
    completed_pairing: tuple
    completed_forcing: tuple
    uncompleted_forcing: tuple
    domain_codimension: int
    domain_equalities: tuple
    domain_signs: tuple
    witness: tuple
    mass_signs: tuple
    extra_witnesses: tuple
    carrier_scan: tuple
    flat_zero: bool
    moduli_dependence: tuple
    # F: the Hermiticity guard and the conditional break
    untouchable: tuple
    completed_hermiticity: tuple
    hermiticity_controls: tuple
    kernel_witness: tuple
    break_conditionality: tuple
    # G: the honesty characterisation
    edge_invariance: tuple
    reflected_sector: tuple
    registration_contents: tuple
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
    # the ORDER of the triple is itself pinned, because every inertia numeral
    # this block prints -- (4,4,0), (3,4,1), (5,2,1) -- is read in that order
    inertia_order_pinned = bool(
        congruence_inertia(sp.diag(1, 1, 1, 1, 0, 0, 0, 0)) == (4, 4, 0)
        and congruence_inertia(sp.diag(-1, -1, -1, -1, 0, 0, 0, 0))
        == (0, 4, 4)
        and congruence_inertia(sp.zeros(8, 8)) == (0, 8, 0)
    )
    hermitian_conventions_agree = zero(
        sp.expand(
            herm(half_block(HQ_FREE))
            - b148.hermitian_part(half_block(HQ_FREE))
        )
    )
    operator_pinned = bool(
        zero(sp.expand(THETA_PRIME_OP * THETA_PRIME_OP - sp.eye(PHYS)))
        and zero(sp.expand(PLUS.T * THETA_PRIME_OP * PLUS))
        and not zero(sp.expand(THETA_PRIME_OP * PLUS))
        and zero(sp.expand(THETA_PRIME_OP * X0 - X0 * THETA_PRIME_OP))
    )

    # -----------------------------------------------------------------------
    # the committed objects, built once
    # -----------------------------------------------------------------------
    differentials, star_form = b145.connection(SHEAR_X, SHEAR_T)
    edge_table = b145.edge_differentials(
        differentials, star_form, HEALING_WEIGHTS
    )
    action = {
        key: b145.quotient_action(edge_table[key], COVER_FREE, MASS)
        for key in EDGE_KEYS
    }
    k_table = {
        key: sp.expand(action[key] - MASS * HQ_FREE) for key in EDGE_KEYS
    }
    # the inlined residue route is pinned against the committed action law
    action_law_pinned = all(
        zero(sp.expand(k_table[key] - residue(edge_table[key])))
        for key in ((0, 0), (2, 3))
    )

    mass_half = half_block(HQ_FREE)              # RAW [theta' H_q]_++
    gram = herm(mass_half)                       # the mass Gram G'
    k_half = {key: half_block(k_table[key]) for key in EDGE_KEYS}
    pairing = {
        key: sp.expand(MASS * gram + herm(k_half[key])) for key in EDGE_KEYS
    }

    # -----------------------------------------------------------------------
    # B: the three-block split, its scope correction, and the reach theorem
    # -----------------------------------------------------------------------
    zero_slots = tuple(k for k in range(HALF) if sp.expand(gram[k, k]) == 0)
    dead_live_partition = (
        DEAD,
        LIVE,
        zero_slots,
        tuple(sorted(set(DEAD) | set(LIVE))) == tuple(range(HALF)),
    )

    dead_dead_entries = {
        (1, 3): sp.expand((B_MODULUS[(3, 1)] + B_MODULUS[(3, 3)]) / 8),
        (4, 6): sp.expand(-(B_MODULUS[(1, 1)] + B_MODULUS[(1, 3)]) / 8),
    }
    live_diagonal = (
        sp.expand(B_MODULUS[(3, 0)] / 4),
        sp.expand(B_MODULUS[(3, 2)] / 4),
        sp.expand(-B_MODULUS[(1, 0)] / 4),
        sp.expand(-B_MODULUS[(1, 2)] / 4),
    )
    dead_dead_edges = sum(
        1
        for key in EDGE_KEYS
        if all(
            sp.expand(
                pairing[key][i, j]
                - MASS
                * dead_dead_entries.get(
                    (i, j), dead_dead_entries.get((j, i), 0)
                )
            )
            == 0
            for i in DEAD
            for j in DEAD
        )
    )
    live_live_edges = sum(
        1
        for key in EDGE_KEYS
        if all(
            sp.expand(
                pairing[key][a, b]
                - (MASS * live_diagonal[p] if p == q else 0)
            )
            == 0
            for p, a in enumerate(LIVE)
            for q, b in enumerate(LIVE)
        )
    )
    dead_live_edges = sum(
        1
        for key in EDGE_KEYS
        if all(
            sp.expand(pairing[key][k, j] - herm(k_half[key])[k, j]) == 0
            for k, j in DEAD_LIVE
        )
    )
    dead_live_live_counts = tuple(
        sorted(
            {
                sum(
                    1
                    for k, j in DEAD_LIVE
                    if sp.expand(herm(k_half[key])[k, j]) != 0
                )
                for key in EDGE_KEYS
            }
        )
    )
    three_block = (
        dead_dead_edges,
        live_live_edges,
        dead_live_edges,
        dead_live_live_counts,
    )

    # THE SCOPE CORRECTION.  The solve read the dead-live block as sixteen
    # single b-modulus monomials; that reading is TRUE ON FOUR EDGES ONLY.
    b_symbols = set(B_MODULUS.values())
    pure_edges: list = []
    impure_monomials: set = set()
    impure_moduli: set = set()
    for key in EDGE_KEYS:
        block = herm(k_half[key])
        entries = [sp.expand(block[k, j]) for k, j in DEAD_LIVE]
        monomials = max(len(sp.Add.make_args(entry)) for entry in entries)
        symbols: set = set()
        for entry in entries:
            symbols |= entry.free_symbols - {SHEAR_X, SHEAR_T}
        if monomials == 1 and symbols <= b_symbols:
            pure_edges.append(key)
        else:
            impure_monomials.add(monomials)
            impure_moduli.add(len(symbols))
    split_scope = (
        len(pure_edges),
        tuple(sorted(pure_edges)),
        K_EDGE_COUNT - len(pure_edges),
        tuple(sorted(impure_monomials)),
        tuple(sorted(impure_moduli)),
    )

    # THE REACH THEOREM, for a GENERIC X_0-odd antisymmetric Delta K.
    parity = tuple(X0[i, i] for i in range(PHYS))
    even_sites = tuple(i for i in range(PHYS) if parity[i] == 1)
    odd_sites = tuple(i for i in range(PHYS) if parity[i] == -1)

    def antisymmetric(pairs, prefix) -> tuple:
        matrix = sp.zeros(PHYS, PHYS)
        symbols = []
        for index, (i, j) in enumerate(pairs):
            symbol = sp.Symbol(f"{prefix}_{index}", real=True)
            symbols.append(symbol)
            matrix[i, j] = symbol
            matrix[j, i] = -symbol
        return matrix, tuple(symbols)

    odd_pairs = tuple((i, j) for i in even_sites for j in odd_sites)
    generic_pairs = tuple(
        (i, j) for i in range(PHYS) for j in range(i + 1, PHYS)
    )
    even_pairs = tuple(
        (block[a], block[b])
        for block in (even_sites, odd_sites)
        for a in range(len(block))
        for b in range(a + 1, len(block))
    )
    odd_delta, odd_symbols = antisymmetric(odd_pairs, "k")
    generic_delta, _generic_symbols = antisymmetric(generic_pairs, "q")
    even_delta, _even_symbols = antisymmetric(even_pairs, "r")

    def classes_of(block: sp.Matrix) -> tuple:
        label = {k: ("D" if k in DEAD else "L") for k in range(HALF)}
        support = [
            (i, j)
            for i in range(HALF)
            for j in range(HALF)
            if sp.expand(block[i, j]) != 0
        ]
        return (
            len(support),
            tuple(sorted({(label[i], label[j]) for i, j in support})),
        )

    odd_half = herm(half_block(odd_delta))
    odd_raw = half_block(odd_delta)
    reach_matrix = sp.Matrix(
        [
            [sp.expand(odd_half[k, j]).coeff(symbol, 1) for symbol in odd_symbols]
            for k, j in DEAD_LIVE
        ]
    )
    reach = (
        len(odd_symbols),
        zero(sp.expand(X0 * odd_delta * X0 + odd_delta)),
        zero(sp.expand(odd_delta + odd_delta.T)),
        classes_of(odd_half),
        classes_of(odd_raw),
        all(sp.expand(odd_half[k, j]) != 0 for k, j in DEAD_LIVE),
        reach_matrix.rank(),
    )
    reach_controls = (
        (len(generic_pairs),) + classes_of(herm(half_block(generic_delta))),
        (len(even_pairs),) + classes_of(herm(half_block(even_delta))),
    )

    # -----------------------------------------------------------------------
    # C: the completion mechanics -- existence, uniqueness, deletion, the price
    # -----------------------------------------------------------------------
    solved: dict = {}
    solvable_edges = 0
    support_profile: dict = {}
    forced_profile: dict = {}
    determined_values: set = set()
    free_are_bare = 0
    for key in EDGE_KEYS:
        differential = edge_table[key]
        support = support_of(differential)
        coefficients = sp.symbols(f"c0:{len(support)}", real=True)
        index = {symbol: position for position, symbol in enumerate(coefficients)}
        perturbation = sp.zeros(SIZE, SIZE)
        for position, (i, j) in enumerate(support):
            perturbation[i, j] = coefficients[position] * differential[i, j]
        delta_k = residue(perturbation)
        delta_half = herm(half_block(delta_k))
        target_half = herm(k_half[key])
        rows: list = []
        right: list = []
        for k, j in DEAD_LIVE:
            for row, value in monomial_rows(
                delta_half[k, j] + target_half[k, j], coefficients, index
            ):
                rows.append(row)
                right.append(value)
        matrix = sp.Matrix(rows)
        vector = sp.Matrix(right)
        rank, augmented, ok = feasible(matrix, vector)
        solvable_edges += int(ok)
        solution = list(sp.linsolve((matrix, vector), list(coefficients)))[0]
        forced = tuple(
            position
            for position in range(len(coefficients))
            if not (solution[position].free_symbols & set(coefficients))
        )
        free = tuple(
            position
            for position in range(len(coefficients))
            if solution[position].free_symbols & set(coefficients)
        )
        determined_values |= {sp.simplify(solution[p]) for p in forced}
        free_are_bare += int(
            all(solution[p] in set(coefficients) for p in free)
        )
        particular = [
            sp.simplify(
                solution[p].xreplace(
                    {coefficients[q]: sp.Integer(0) for q in free}
                )
            )
            for p in range(len(coefficients))
        ]
        completed_differential = sp.Matrix(differential)
        deleted = []
        for position, (i, j) in enumerate(support):
            if particular[position] != 0:
                completed_differential[i, j] = sp.expand(
                    differential[i, j] * (1 + particular[position])
                )
                deleted.append((i, j))
        solved[key] = (
            support,
            tuple(deleted),
            sp.expand(completed_differential),
            rank,
        )
        support_profile[key] = (len(support), len(deleted))
        forced_profile[key] = (rank, len(forced), len(free))

    solvability = (solvable_edges, K_EDGE_COUNT)
    small = tuple(
        sorted(key for key in EDGE_KEYS if support_profile[key][0] == SMALL_SUPPORT)
    )
    large = tuple(
        sorted(key for key in EDGE_KEYS if support_profile[key][0] == LARGE_SUPPORT)
    )
    minimal_support = (
        len(small),
        len(large),
        tuple(sorted({support_profile[key] for key in small})),
        tuple(sorted({support_profile[key] for key in large})),
        tuple(sorted({support_profile[key][0] for key in EDGE_KEYS})),
    )
    uniqueness = (
        all(
            forced_profile[key][0] == forced_profile[key][1]
            for key in EDGE_KEYS
        ),
        all(
            forced_profile[key][1] == support_profile[key][0] // 2
            for key in EDGE_KEYS
        ),
        all(
            forced_profile[key][1] + forced_profile[key][2]
            == support_profile[key][0]
            for key in EDGE_KEYS
        ),
        free_are_bare,
        K_EDGE_COUNT,
    )
    deletion_values = tuple(sorted(determined_values, key=str))
    deletion_certificate = (
        sum(
            1
            for key in EDGE_KEYS
            if all(
                sp.expand(solved[key][2][i, j]) == 0
                for i, j in solved[key][1]
            )
        ),
        sum(
            1
            for key in EDGE_KEYS
            if all(
                sp.expand(solved[key][2][i, j] - edge_table[key][i, j]) == 0
                for i, j in solved[key][0]
                if (i, j) not in set(solved[key][1])
            )
        ),
        SMALL_SUPPORT - SMALL_DELETION,
        SMALL_SUPPORT,
    )

    completed_k = {}
    completed_action = {}
    delta_k_table = {}
    for key in EDGE_KEYS:
        delta_k_table[key] = sp.expand(
            residue(solved[key][2]) - k_table[key]
        )
        completed_k[key] = sp.expand(k_table[key] + delta_k_table[key])
        completed_action[key] = sp.expand(MASS * HQ_FREE + completed_k[key])
    # the completed action is pinned against the committed action law too
    completed_action_pinned = all(
        zero(
            sp.expand(
                completed_action[key]
                - b145.quotient_action(solved[key][2], COVER_FREE, MASS)
            )
        )
        for key in ((0, 0), (2, 3))
    )

    totality = (
        sum(
            1
            for key in EDGE_KEYS
            if all(
                sp.expand(herm(half_block(completed_k[key]))[i, j]) == 0
                for i in range(HALF)
                for j in range(i, HALF)
            )
        ),
        K_EDGE_COUNT,
        HALF_SLOTS,
        completed_action_pinned,
    )
    carrier_independence = (
        sum(
            1
            for key in EDGE_KEYS
            if not (
                sp.expand(solved[key][2]).free_symbols & set(COORDS)
            )
            and sp.expand(solved[key][2]).free_symbols <= {SHEAR_X, SHEAR_T}
        ),
        K_EDGE_COUNT,
    )
    parity_membership = (
        sum(
            1
            for key in EDGE_KEYS
            if zero(
                sp.expand(
                    X0 * delta_k_table[key] * X0 + delta_k_table[key]
                )
            )
        ),
        sum(
            1
            for key in EDGE_KEYS
            if zero(sp.expand(X0 * completed_k[key] * X0 + completed_k[key]))
        ),
        K_EDGE_COUNT,
    )
    # THE PRICE.  Delta K is NOT antisymmetric, so neither is K_total, so the
    # completed action's Hermitian part is NOT m H_q: Q_c + Q_c^dagger != 2 m H_q.
    antisymmetry_broken_edges = sum(
        1
        for key in EDGE_KEYS
        if not zero(sp.expand(completed_k[key] + completed_k[key].T))
    )
    antisymmetry_profile = (
        sum(
            1
            for key in EDGE_KEYS
            if not zero(
                sp.expand(delta_k_table[key] + delta_k_table[key].T)
            )
        ),
        sum(
            1
            for key in EDGE_KEYS
            if not zero(
                sp.expand(
                    completed_action[key]
                    + completed_action[key].H
                    - 2 * MASS * HQ_FREE
                )
            )
        ),
        tuple(
            sorted(
                {
                    sp.expand(
                        completed_k[key] + completed_k[key].T
                    ).rank()
                    for key in EDGE_KEYS
                }
            )
        ),
        sum(
            1
            for key in EDGE_KEYS
            if zero(sp.expand(k_table[key] + k_table[key].T))
        ),
    )

    # -----------------------------------------------------------------------
    # D: the honesty theorems, over the full 128-hop completion space
    # -----------------------------------------------------------------------
    hops = tuple(
        sorted(
            {
                (cover_index(t + dt, x + dx), cover_index(t, x))
                for t in range(COVER_T)
                for x in range(LX)
                for dt, dx in ((1, 0), (-1, 0), (0, 1), (0, -1))
            }
        )
    )
    hop_u = sp.symbols(f"u0:{len(hops)}", real=True)
    hop_v = sp.symbols(f"v0:{len(hops)}", real=True)
    hop_parameters = list(hop_u) + list(hop_v)
    hop_index = {
        symbol: position for position, symbol in enumerate(hop_parameters)
    }
    hop_delta = sp.zeros(SIZE, SIZE)
    for position, (i, j) in enumerate(hops):
        hop_delta[i, j] = sp.I * (
            hop_u[position] * SHEAR_X + hop_v[position] * SHEAR_T
        )
    hop_k = residue(hop_delta)
    hop_half = herm(half_block(hop_k))

    hop_systems: dict = {}
    for key in EDGE_KEYS:
        target = herm(k_half[key])
        rows: list = []
        right: list = []
        for k, j in DEAD_LIVE:
            for row, value in monomial_rows(
                hop_half[k, j] + target[k, j], hop_parameters, hop_index
            ):
                rows.append(row)
                right.append(value)
        hop_systems[key] = (rows, right)

    base_rows, base_right = hop_systems[HOP_PROBE_EDGE]
    base_matrix = sp.Matrix(base_rows)
    base_vector = sp.Matrix(base_right)
    base_rank, base_augmented, base_ok = feasible(base_matrix, base_vector)

    hop_feasible = 0
    hop_ranks: set = set()
    for key in EDGE_KEYS:
        rows, right = hop_systems[key]
        rank, _augmented, ok = feasible(sp.Matrix(rows), sp.Matrix(right))
        hop_feasible += int(ok)
        hop_ranks.add(rank)

    hop_space = (
        len(hops),
        len(hop_parameters),
        base_rank,
        base_augmented,
        base_ok,
        set(support_of(edge_table[HOP_PROBE_EDGE])) <= set(hops),
        hop_feasible,
        K_EDGE_COUNT,
        tuple(sorted(hop_ranks)),
    )

    def slice_of(site: int) -> int:
        return site // LX

    seam_hops = tuple(
        hop
        for hop in hops
        if {slice_of(hop[0]) % PHYS_T, slice_of(hop[1]) % PHYS_T}
        in ({1, 2}, {3, 0})
    )
    seam_columns = [
        hop_index[symbol]
        for position, hop in enumerate(hops)
        if hop in set(seam_hops)
        for symbol in (hop_u[position], hop_v[position])
    ]
    seam_matrix = base_matrix[:, seam_columns]
    seam_rank, _seam_augmented, seam_ok = feasible(seam_matrix, base_vector)
    seam_infeasible_edges = 0
    for key in SEAM_PROBE_EDGES:
        rows, right = hop_systems[key]
        restricted = sp.Matrix(rows)[:, seam_columns]
        if not feasible(restricted, sp.Matrix(right))[2]:
            seam_infeasible_edges += 1
    seam = (
        len(seam_hops),
        len(hops) - len(seam_hops),
        seam_rank,
        base_rank,
        seam_ok,
        seam_infeasible_edges,
        len(SEAM_PROBE_EDGES),
    )

    slice_columns = {
        time_slice: [
            hop_index[symbol]
            for position, (i, j) in enumerate(hops)
            if slice_of(i) != time_slice and slice_of(j) != time_slice
            for symbol in (hop_u[position], hop_v[position])
        ]
        for time_slice in range(COVER_T)
    }
    slice_verdicts = {}
    for key in SLICE_PROBE_EDGES:
        rows, right = hop_systems[key]
        matrix = sp.Matrix(rows)
        vector = sp.Matrix(right)
        necessary: list = []
        optional: list = []
        for time_slice in range(COVER_T):
            restricted = matrix[:, slice_columns[time_slice]]
            _rank, _augmented, ok = feasible(restricted, vector)
            (optional if ok else necessary).append(time_slice)
        slice_verdicts[key] = (tuple(necessary), tuple(optional))
    slice_necessity = (
        slice_verdicts[HOP_PROBE_EDGE][0],
        slice_verdicts[HOP_PROBE_EDGE][1],
        tuple(sorted({slice_verdicts[key][0] for key in SLICE_PROBE_EDGES})),
        tuple(
            sorted(
                set.intersection(
                    *[set(slice_verdicts[key][0]) for key in SLICE_PROBE_EDGES]
                )
            )
        ),
        sum(
            1
            for key in SLICE_PROBE_EDGES
            if SEAM_SLICE in slice_verdicts[key][0]
        ),
        len(SLICE_PROBE_EDGES),
    )

    def covariance_rows(label) -> list:
        move = MOVE_MATRIX[label]
        constraint = sp.expand(move * hop_delta * move.inv() - hop_delta)
        rows = []
        for i in range(SIZE):
            for j in range(SIZE):
                entry = sp.expand(constraint[i, j])
                if entry == 0:
                    continue
                for symbol in (SHEAR_X, SHEAR_T):
                    coefficient = sp.expand(entry.coeff(symbol, 1) / sp.I)
                    if coefficient == 0:
                        continue
                    row = [0] * len(hop_parameters)
                    for term in sp.Add.make_args(coefficient):
                        parameters = term.free_symbols & set(hop_parameters)
                        if parameters:
                            parameter = parameters.pop()
                            row[hop_index[parameter]] += term.coeff(
                                parameter, 1
                            )
                    rows.append(row)
        return rows

    translation_tests: list = []
    for label in COVARIANCE_LABELS:
        extra = covariance_rows(label)
        matrix = sp.Matrix(base_rows + extra)
        vector = sp.Matrix(base_right + [0] * len(extra))
        rank, augmented, ok = feasible(matrix, vector)
        translation_tests.append((label, rank, augmented, ok))
    translation_tests = tuple(translation_tests)

    # the same two unit translations on a SECOND edge, so the infeasibility is
    # not read at one edge only
    control_rows, control_right = hop_systems[TRANSLATION_CONTROL_EDGE]
    translation_control: list = []
    for label in (UNIT_T_LABEL, UNIT_X_LABEL):
        extra = covariance_rows(label)
        matrix = sp.Matrix(control_rows + extra)
        vector = sp.Matrix(control_right + [0] * len(extra))
        rank, augmented, ok = feasible(matrix, vector)
        translation_control.append((label, rank, augmented, ok))
    translation_control = tuple(translation_control)

    # the STRONG demand: kill the RAW half-block on all 64 slots, not just the
    # Hermitian part on the sixteen dead-live ones.  It is solvable too, at a
    # strictly larger rank, so Hermiticity of the completed pairing is free.
    hop_raw = half_block(hop_k)
    raw_target = k_half[HOP_PROBE_EDGE]
    raw_rows: list = []
    raw_right: list = []
    for i in range(HALF):
        for j in range(HALF):
            for row, value in monomial_rows(
                hop_raw[i, j] + raw_target[i, j], hop_parameters, hop_index
            ):
                raw_rows.append(row)
                raw_right.append(value)
    raw_rank, _raw_augmented, raw_ok = feasible(
        sp.Matrix(raw_rows), sp.Matrix(raw_right)
    )
    strong_demand = (raw_rank, raw_ok, raw_rank > base_rank)

    # -----------------------------------------------------------------------
    # E: the positivity, exactly
    # -----------------------------------------------------------------------
    completed_half = {
        key: sp.expand(half_block(completed_action[key])) for key in EDGE_KEYS
    }
    completed_pairing = (
        sum(
            1
            for key in EDGE_KEYS
            if zero(sp.expand(completed_half[key] - MASS * mass_half))
        ),
        sum(
            1
            for key in EDGE_KEYS
            if zero(sp.expand(herm(completed_half[key]) - MASS * gram))
        ),
        sum(
            1
            for key in EDGE_KEYS
            if zero(sp.expand(half_block(completed_k[key])))
        ),
        K_EDGE_COUNT,
    )

    completed_block = sp.expand(MASS * gram)
    completed_zero_diagonal = tuple(
        k for k in range(HALF) if sp.expand(completed_block[k, k]) == 0
    )
    forced_forms = sorted(
        {
            sp.factor(sp.expand(completed_block[k, j] / MASS))
            for k in completed_zero_diagonal
            for j in range(HALF)
            if sp.expand(completed_block[k, j]) != 0
        },
        key=str,
    )
    forced_matrix = sp.Matrix(
        [
            [sp.expand(form).coeff(value, 1) for value in COORDS]
            for form in forced_forms
        ]
    )
    completed_forcing = (
        completed_zero_diagonal,
        len(forced_forms),
        forced_matrix.rank(),
    )

    fixture = {SHEAR_X: b134.S_X, SHEAR_T: b134.S_T}
    uncompleted_ranks = set()
    for key in CHART01_EDGES:
        block = sp.expand(pairing[key])
        slots = [k for k in range(HALF) if sp.expand(gram[k, k]) == 0]
        rows = []
        for k in slots:
            for j in range(HALF):
                for part in (
                    sp.expand(sp.re(block[k, j])),
                    sp.expand(sp.im(block[k, j])),
                ):
                    if part != 0:
                        rows.append(sp.expand(part.xreplace(fixture)))
        uncompleted_ranks.add(
            sp.Matrix(
                [
                    [sp.expand(row).coeff(value, 1) for value in ODD_SHEAR_COORDS]
                    for row in rows
                ]
            ).rank()
        )
    uncompleted_forcing = tuple(sorted(uncompleted_ranks))

    locus_forms = (
        sp.expand(B_MODULUS[(3, 1)] + B_MODULUS[(3, 3)]),
        sp.expand(B_MODULUS[(1, 1)] + B_MODULUS[(1, 3)]),
    )
    locus_matrix = sp.Matrix(
        [
            [sp.expand(form).coeff(value, 1) for value in COORDS]
            for form in locus_forms
        ]
    )
    domain_codimension = locus_matrix.rank()
    domain_equalities = (
        tuple(sorted((str(form) for form in locus_forms))),
        tuple(
            sorted(
                str(value)
                for form in locus_forms
                for value in sp.expand(form).free_symbols & set(COORDS)
            )
        ),
    )

    def carrier_field(profile: dict) -> dict:
        return {
            cell: (profile.get(cell, sp.Integer(0)), sp.Integer(1))
            for cell in CELLS
        }

    def block_at(profile: dict, mass_value) -> sp.Matrix:
        point = b147.modulus_point(carrier_field(profile))
        return sp.expand(
            sp.expand(MASS * gram).xreplace(point).subs(MASS, mass_value)
        )

    witness_profile = {
        (1, 0): R(3, 5),
        (1, 2): R(3, 5),
        (3, 0): R(-3, 5),
        (3, 2): R(-3, 5),
    }
    witness_field = carrier_field(witness_profile)
    witness_point = b147.modulus_point(witness_field)
    witness_block = sp.expand(sp.expand(MASS * gram).xreplace(witness_point))
    witness_at_one = sp.expand(witness_block.subs(MASS, 1))
    live_indices = list(LIVE)
    witness = (
        b145.in_admissible_cone(witness_field),
        zero(sp.expand(witness_block - MASS * b148.ESCAPE_GRAM)),
        congruence_inertia(witness_at_one),
        congruence_inertia(witness_at_one[live_indices, live_indices]),
        tuple(
            sorted(
                (sp.simplify(value) for value in witness_block.eigenvals()),
                key=str,
            )
        ),
        zero(
            sp.expand(
                witness_block
                - sp.diag(*[witness_block[k, k] for k in range(HALF)])
            )
        ),
        sum(
            1
            for key in EDGE_KEYS
            if zero(
                sp.expand(
                    herm(completed_half[key]).xreplace(witness_point)
                    - witness_block
                )
            )
        ),
    )
    mass_signs = (
        congruence_inertia(sp.expand(witness_block.subs(MASS, -1))),
        congruence_inertia(sp.expand(witness_block.subs(MASS, 0))),
    )

    # a SECOND, committed witness -- Block 148's escape field -- and an
    # irrational carrier, so the positivity is not an artefact of one point
    second_field = b148.escape_witness_field()
    second_point = b147.modulus_point(second_field)
    second_block = sp.expand(sp.expand(MASS * gram).xreplace(second_point))
    irrational = 1 / sp.sqrt(2)
    irrational_profile = {
        (1, 0): irrational,
        (1, 2): irrational,
        (3, 0): -irrational,
        (3, 2): -irrational,
    }
    extra_witnesses = (
        b145.in_admissible_cone(second_field),
        zero(sp.expand(second_block - MASS * b148.ESCAPE_GRAM)),
        congruence_inertia(sp.expand(second_block.subs(MASS, 1))),
        b145.in_admissible_cone(carrier_field(irrational_profile)),
        congruence_inertia(block_at(irrational_profile, 1)),
    )
    # and the committed cone carriers are scanned: none of them lies on the
    # codimension-2 locus, so none of them is PSD -- the domain is TUNED
    scan_carriers = tuple(b148.CONE_CARRIERS) + (
        ("b105-staircase", b105.overlap_field()),
        ("b145-witness", b145.witness_field()),
    )
    scan_on_locus = 0
    scan_psd = 0
    for _name, field in scan_carriers:
        point = b147.modulus_point(field)
        block = sp.expand(sp.expand(MASS * gram).xreplace(point).subs(MASS, 1))
        if all(sp.expand(form.xreplace(point)) == 0 for form in locus_forms):
            scan_on_locus += 1
        if not zero(block) and congruence_inertia(block)[2] == 0:
            scan_psd += 1
    carrier_scan = (len(scan_carriers), scan_on_locus, scan_psd)

    sign_violations = (
        {(1, 0): R(-3, 5), (1, 2): R(3, 5), (3, 0): R(-3, 5), (3, 2): R(-3, 5)},
        {(1, 0): R(3, 5), (1, 2): R(-3, 5), (3, 0): R(-3, 5), (3, 2): R(-3, 5)},
        {(1, 0): R(3, 5), (1, 2): R(3, 5), (3, 0): R(3, 5), (3, 2): R(-3, 5)},
        {(1, 0): R(3, 5), (1, 2): R(3, 5), (3, 0): R(-3, 5), (3, 2): R(3, 5)},
    )
    equality_violations = (
        {**witness_profile, (3, 1): R(1, 2), (3, 3): R(1, 2)},
        {**witness_profile, (1, 1): R(1, 2), (1, 3): R(1, 2)},
    )
    domain_signs = (
        tuple(
            congruence_inertia(block_at(profile, 1))
            for profile in sign_violations
        ),
        tuple(
            congruence_inertia(block_at(profile, 1))
            for profile in equality_violations
        ),
        # the m < 0 reversal is a DOMAIN statement too: the mirrored witness is
        # PSD at m = -1 and the unmirrored one is not
        congruence_inertia(
            block_at(
                {
                    cell: -value
                    for cell, value in witness_profile.items()
                },
                -1,
            )
        ),
    )

    flat_zero = bool(
        zero(block_at({}, 1))
        and zero(
            sp.expand(
                sp.expand(MASS * gram).xreplace(
                    {value: 0 for value in SHEAR_COORDS}
                )
            )
        )
    )
    locus_substitution = {
        B_MODULUS[(3, 3)]: -B_MODULUS[(3, 1)],
        B_MODULUS[(1, 3)]: -B_MODULUS[(1, 1)],
    }
    on_locus = sp.expand(sp.expand(MASS * gram).xreplace(locus_substitution))
    used_moduli: set = set()
    for i in range(HALF):
        for j in range(HALF):
            used_moduli |= sp.expand(on_locus[i, j]).free_symbols & set(COORDS)
    locus_moduli = {
        value
        for form in locus_forms
        for value in sp.expand(form).free_symbols & set(COORDS)
    }
    moduli_dependence = (
        tuple(sorted(str(value) for value in used_moduli)),
        tuple(sorted(str(value) for value in locus_moduli)),
        not (used_moduli & locus_moduli),
        len(used_moduli),
        len(locus_moduli),
    )

    # -----------------------------------------------------------------------
    # F: the Hermiticity guard and the conditional break
    # -----------------------------------------------------------------------
    mass_defect = sp.expand(mass_half - mass_half.H)
    defect_support = tuple(
        sorted(
            (i, j)
            for i in range(HALF)
            for j in range(HALF)
            if sp.expand(mass_defect[i, j]) != 0
        )
    )
    untouchable = (
        defect_support,
        sp.expand(
            mass_defect[1, 3] + (B_MODULUS[(3, 1)] - B_MODULUS[(3, 3)]) / 4
        )
        == 0,
        sp.expand(
            mass_defect[4, 6] + (B_MODULUS[(1, 1)] - B_MODULUS[(1, 3)]) / 4
        )
        == 0,
        all(sp.expand(odd_half[i, j]) == 0 for i, j in UNTOUCHABLE_SLOTS),
        all(sp.expand(odd_raw[i, j]) == 0 for i, j in UNTOUCHABLE_SLOTS),
    )

    def hermiticity_rows(block: sp.Matrix) -> list:
        rows = []
        for i in range(block.rows):
            for j in range(i + 1, block.cols):
                defect = sp.expand(block[i, j] - block[j, i])
                if defect == 0:
                    continue
                for coefficient in sp.Poly(defect, MASS).all_coeffs():
                    coefficient = sp.expand(coefficient)
                    if coefficient != 0:
                        rows.append(
                            [coefficient.coeff(value, 1) for value in COORDS]
                        )
        return rows

    completed_rows: list = []
    per_edge_rank = set()
    for key in EDGE_KEYS:
        rows = hermiticity_rows(completed_half[key])
        per_edge_rank.add(sp.Matrix(rows).rank() if rows else 0)
        completed_rows.extend(rows)
    completed_system = sp.Matrix(completed_rows)
    completed_rank = completed_system.rank()
    reduced, pivots = completed_system.rref()
    row_forms = tuple(
        sorted(
            (
                str(
                    sp.factor(
                        sum(
                            reduced[position, column] * COORDS[column]
                            for column in range(NCOORD)
                        )
                    )
                )
                for position in range(len(pivots))
            )
        )
    )
    completed_hermiticity = (
        completed_rank,
        NCOORD - completed_rank,
        row_forms,
        tuple(sorted(per_edge_rank)),
    )

    uncompleted_rows: list = []
    theta_rows: list = []
    for key in EDGE_KEYS:
        uncompleted_rows.extend(hermiticity_rows(half_block(action[key])))
        theta_rows.extend(
            hermiticity_rows(sp.expand(PLUS.T * THETA * action[key] * PLUS))
        )
    uncompleted_rank = sp.Matrix(uncompleted_rows).rank()
    theta_rank = sp.Matrix(theta_rows).rank()
    shear_index = tuple(COORDS.index(value) for value in SHEAR_COORDS)
    nullspace = completed_system.nullspace()
    hermiticity_controls = (
        uncompleted_rank,
        NCOORD - uncompleted_rank,
        theta_rank,
        NCOORD - theta_rank,
        len(nullspace),
        not all(
            vector[position] == 0
            for vector in nullspace
            for position in shear_index
        ),
    )

    kernel_witness = (
        all(
            sp.expand(form.xreplace(witness_point)) == 0
            for form in locus_forms
        ),
        zero(
            sp.expand(
                herm(completed_half[(0, 0)]).xreplace(witness_point)
                - sp.expand(completed_half[(0, 0)]).xreplace(witness_point)
            )
        ),
        any(
            sp.expand(value.xreplace(witness_point)) != 0
            for value in ODD_SHEAR_COORDS
        ),
        not zero(sp.expand(gram.xreplace(witness_point))),
        congruence_inertia(witness_at_one),
    )
    # THE CONDITIONALITY.  Without the completion the same PSD step forces every
    # odd shear to zero and the pairing goes massless; and the uncompleted
    # necessity system still stands at rank 20.  So the break is a statement
    # ABOUT THE PREMISE, not about the lane.
    break_conditionality = (
        uncompleted_rank != completed_rank,
        zero(
            sp.expand(
                sp.expand(MASS * gram).xreplace(
                    {value: 0 for value in ODD_SHEAR_COORDS}
                )
            )
        ),
    )

    # -----------------------------------------------------------------------
    # G: the honesty characterisation
    # -----------------------------------------------------------------------
    edge_invariance = (
        len({sp.srepr(sp.expand(completed_half[key])) for key in EDGE_KEYS}),
        len({sp.srepr(sp.expand(herm(completed_half[key]))) for key in EDGE_KEYS}),
        K_EDGE_COUNT,
    )
    # The ++ block of the completed connection is dead while the connection
    # itself survives.  The full 8 x 16 reflected-sector statement is NOT made
    # here -- it is Block 155's -- so only the ++ block is certified.
    reflected_sector = (
        sum(
            1
            for key in EDGE_KEYS
            if zero(sp.expand(half_block(completed_k[key])))
        ),
        sum(1 for key in EDGE_KEYS if not zero(completed_k[key])),
        sum(
            1
            for key in EDGE_KEYS
            if zero(sp.expand(X0 * completed_k[key] * X0 + completed_k[key]))
        ),
        sum(
            1
            for key in EDGE_KEYS
            if completed_k[key].free_symbols & {SHEAR_X, SHEAR_T}
        ),
        K_EDGE_COUNT,
    )
    registration_contents = REGISTRATION_CONTENTS

    exact_no_float = no_float(
        (
            COVER_FREE,
            HQ_FREE,
            gram,
            mass_half,
            k_table[(0, 0)],
            completed_k[(0, 0)],
            solved[(0, 0)][2],
            witness_block,
            on_locus,
        )
    )

    if deep:
        # the deep pass strengthens the 128-hop demand from the sixteen
        # dead-live slots to ALL 36 independent half-slots, on the probe edge
        target = herm(k_half[HOP_PROBE_EDGE])
        rows = []
        right = []
        for i in range(HALF):
            for j in range(i, HALF):
                for row, value in monomial_rows(
                    hop_half[i, j] + target[i, j], hop_parameters, hop_index
                ):
                    rows.append(row)
                    right.append(value)
        if not feasible(sp.Matrix(rows), sp.Matrix(right))[2]:
            raise AssertionError("deep full-half hop pass infeasible")

    return Facts(
        main_head=main_head,
        authority=authority,
        inertia_calibration=inertia_calibration,
        inertia_order_pinned=inertia_order_pinned,
        hermitian_conventions_agree=hermitian_conventions_agree,
        operator_pinned=operator_pinned,
        action_law_pinned=action_law_pinned,
        dead_live_partition=dead_live_partition,
        three_block=three_block,
        split_scope=split_scope,
        reach=reach,
        reach_controls=reach_controls,
        solvability=solvability,
        minimal_support=minimal_support,
        uniqueness=uniqueness,
        deletion_values=deletion_values,
        deletion_certificate=deletion_certificate,
        totality=totality,
        carrier_independence=carrier_independence,
        parity_membership=parity_membership,
        antisymmetry_broken_edges=antisymmetry_broken_edges,
        antisymmetry_profile=antisymmetry_profile,
        hop_space=hop_space,
        seam=seam,
        slice_necessity=slice_necessity,
        translation_tests=translation_tests,
        translation_control=translation_control,
        strong_demand=strong_demand,
        completed_pairing=completed_pairing,
        completed_forcing=completed_forcing,
        uncompleted_forcing=uncompleted_forcing,
        domain_codimension=domain_codimension,
        domain_equalities=domain_equalities,
        domain_signs=domain_signs,
        witness=witness,
        mass_signs=mass_signs,
        extra_witnesses=extra_witnesses,
        carrier_scan=carrier_scan,
        flat_zero=flat_zero,
        moduli_dependence=moduli_dependence,
        untouchable=untouchable,
        completed_hermiticity=completed_hermiticity,
        hermiticity_controls=hermiticity_controls,
        kernel_witness=kernel_witness,
        break_conditionality=break_conditionality,
        edge_invariance=edge_invariance,
        reflected_sector=reflected_sector,
        registration_contents=registration_contents,
        exact_no_float=exact_no_float,
        scope=scope_certificate(raw_note()),
    )


# ---------------------------------------------------------------------------
# H. note scope
# ---------------------------------------------------------------------------
# PLACEHOLDER FENCE.  The landing supervisor replaces this string with the
# note's own eight-line N5 fence, byte for byte; until then H-note-scope is the
# single failing gate and the runner exits 1.
N5_FENCE = 'N5: per_element: THE THREE-BLOCK SPLIT AND THE REACH THEOREM, BOTH EXACT: on the committed four-chart shear atlas at symbolic (s_x, s_t), the committed 64-modulus carrier family, the committed sixteen healed edge actions and the committed [X Q]_++ half pairing, the quenched theta\'-pairing A\' = m G\' + Herm[theta\' K]_++ splits, entry by entry on ALL SIXTEEN EDGES and symbolically in the 64 moduli and in (s_x, s_t), into exactly three blocks under the half staggered sign X_h = diag(+, -, +, -, -, +, -, +): a DEAD-DEAD block that is PURE MASS with the two entries m(b_31 + b_33)/8 at (1,3) and -m(b_11 + b_13)/8 at (4,6); a LIVE-LIVE block that is PURE MASS and DIAGONAL at m/4 diag(b_30, b_32, -b_10, -b_12) with STRICTLY ZERO off-diagonal; and a DEAD-LIVE block that is PURE CONNECTION and LIVE IN 16 OF 16 SLOTS on EVERY edge -- where DEAD means the four X_h-MINUS slots {1, 3, 4, 6}, VERIFIED to be EXACTLY Block 153\'s four structural zeros and not merely coincident with them -- so the MASS AND THE CONNECTION DO NOT MIX ANYWHERE IN THE PAIRING; with the CHECKER\'S SCOPE CORRECTION displayed rather than buried, that the CLEAN SIXTEEN-MONOMIAL dead-live form holds on the FOUR chart-0/1 edges ONLY while the other TWELVE carry UP TO NINE MONOMIALS PER ENTRY over 48 MODULI, so the SPLIT is ATLAS-WIDE and the CLEAN FORM is 4 OF 16 and is never generalized from the probe edge; and with the REACH THEOREM proved for a GENERIC X_0-ODD Delta K carrying 64 FREE REAL PARAMETERS rather than for a fixture: such an increment reaches EXACTLY THE 32 DEAD-LIVE SLOTS, is NONZERO in EVERY one of them, has FULL RANK 16 there, and is IDENTICALLY ZERO on the dead-dead block, on the live-live block and on the ENTIRE DIAGONAL -- controlled against a generic ANTISYMMETRIC increment which hits ALL classes, so the parity restriction and not the antisymmetry does the work, and against a generic X_0-EVEN increment which hits EXACTLY THE COMPLEMENT, so the two parities PARTITION the half-block; the committed connection K_a = Q_a - m H_q is ITSELF X_0-odd on all sixteen edges, so the requirement lives inside ONE linear space\nper_site: THE FORCED COMPLETION -- IT EXISTS, IT IS TOTAL, IT IS UNIQUE ON THE DIFFERENTIAL\'S SUPPORT, AND IT IS A LINK DELETION: the requirement is set at the STRONGEST reading, [theta\' K_total]_++ = 0 IDENTICALLY IN ALL 64 MODULI and NOT at a fixture, a witness or a stratum, with TWO CHEATS FORBIDDEN AND BOTH CHECKED -- the odd shears must SURVIVE in K_total (they do, on 16 of 16 edges) and K_total must be NONZERO on the carrier (it is, on 16 of 16), so what dies is the PAIRING\'S VIEW of the connection and not the connection; the cancellation is SOLVABLE ON 16 OF 16 EDGES and is TOTAL, killing ALL 36 INDEPENDENT HALF-SLOTS and not merely the 16 PSD-relevant dead-live ones; its MINIMAL SUPPORT is SIXTEEN HOPS ON SIX EDGES -- the four chart-0/1 edges and the two SELF-EDGES (2,2) and (3,3) -- and TWENTY-FOUR on the other TEN; it is UNIQUE ON THE DIFFERENTIAL\'S SUPPORT; and EVERY COEFFICIENT IS EXACTLY -1, so Delta d = -d on the selected hops and d_total = d restricted to 16 OF ITS 32 HOPS: THE COMPLETION IS A LINK DELETION, and the deleted set is NOT ARBITRARY but is EXACTLY THE COVER SLICES THETA-PRIME REFLECTS INTO -- a reading that cuts BOTH WAYS and is displayed rather than celebrated, since an object that deletes the connection precisely where the reflection carries it across the half may be the simplest completion the lane could have found OR may be an arrangement for the reflection to see a free theory, and this note does NOT choose between the two readings; the INCREMENT is CARRIER-INDEPENDENT, free of all 64 moduli and depending only on the constant -1, while the INDUCED Delta K is CARRIER-LINEAR because the residue map CONTRACTS the increment against the carrier\'s Hodge operator, and a Delta K that is ITSELF carrier-CONSTANT is barred by a MODULUS-HOMOGENEITY NO-GO since the target is homogeneous linear in the moduli; class membership is MEASURED and never assumed, the induced Delta K being X_0-ODD on 16 of 16 edges so Block 153\'s rider applies VERBATIM and the diagonal is untouched exactly as the reach theorem predicts; and TWO CAVEATS ARE DISPLAYED -- Delta K IS NOT ANTISYMMETRIC, so the completed action LOSES the landed global-form identity Q + Q^dagger = 2 m H_q, a REAL COST that is NOT repaired here; and the SOLUTION-SPACE RANK NUMERALS ARE BASIS-DEPENDENT, the solve\'s 112 of 248 and the checker\'s 104 of 156 counting DIFFERENT BASES of the same increment space, so the INVARIANT content is SOLVABILITY and SUPPORT-CLASS UNIQUENESS and NO rank numeral is load-bearing anywhere in this note\nper_mode: THE PRICE, PROVEN NEGATIVELY -- THE COMPLETION IS NOT A BOUNDARY TERM, AND EACH OBSTRUCTION IS AN INFEASIBILITY CERTIFICATE (a rank mismatch between a system and its augmented matrix) AND NOT AN EXHAUSTED SEARCH: (i) SEAM-SUPPORTED COMPLETIONS ARE INFEASIBLE -- restricting the increment\'s support to hops touching cover slices 3 or 4, the slices the reflection identifies, leaves the image FALLING FAR SHORT of the requirement, so NO seam-supported completion exists and THE COMPLETION IS NOT A BOUNDARY TERM; (ii) THE BULK SLICES ARE NECESSARY -- deleting cover slice t from the available support and re-solving for each t = 0..7 makes the system INFEASIBLE for t in {0, 4, 5, 6, 7}, FIVE slices EACH INDIVIDUALLY NECESSARY on the probe edge, and THE SOLVE\'S {0, 5, 6, 7} WAS NOT MAXIMAL: slice 4 is necessary too AND IT IS A SEAM SLICE, so the honest statement is NOT "the seam is untouched" but that THE SEAM ALONE IS INSUFFICIENT WHILE ONE SEAM SLICE AND FOUR BULK SLICES ARE ALL REQUIRED -- the completion straddles the seam, reaches deep into the bulk, and CANNOT BE LOCALIZED ANYWHERE, and this correction runs AGAINST the premise and is displayed for that reason; (iii) TRANSLATION COVARIANCE BREAKS -- demanding that the completion commute with a covariant move and re-solving returns INFEASIBLE for the UNIT TIME TRANSLATION (1,1,1,0), INFEASIBLE for the UNIT x TRANSLATION (1,0,1,1), and SOLVABLE ONLY for the PERIOD-2 TIME TRANSLATION (1,2,1,0), so the completion HALVES the lattice\'s time-translation symmetry and DESTROYS its x-translation symmetry outright, describing a STAGGERED modification of the lattice action, consistent with the staggered selection rule of the deletion but a GENUINE SYMMETRY COST and not a technicality; the price therefore stands at BULK, TRANSLATION-BREAKING, CONNECTION-DELETING and ANTISYMMETRY-LOSING, with every item PROVEN and none deferred\nper_block: THE POSITIVITY, EXACTLY SCOPED, AND THE FLAT-LIMIT CALIBRATION GAP RECORDED AS AN OPEN DEFECT: [theta\' K_total]_++ = 0 AS A MATRIX on all sixteen edges, so THE COMPLETED PAIRING EQUALS m [theta\' H_q]_++ EXACTLY -- STRONGER than a Hermitian-part-only statement, since the anti-Hermitian part of the connection contribution dies too -- making it EDGE-INDEPENDENT (the SAME matrix on all sixteen edges, verified by exact structural comparison) and carrying ZERO CONNECTION DATA (no (s_x, s_t) symbol appears at all); the surviving PSD forcing is RANK 2 ONLY against Block 148\'s RANK 8, so PSD no longer kills the seam but imposes exactly TWO linear conditions, WITH THE CONTROL that WITHOUT the completion the same PSD step forces ALL EIGHT odd shears to zero and the mass Gram vanishes identically, so the completion and not the PSD step is doing the work; AND THE PSD SET IS THIN AND IS NOT OPEN -- the CHECKER\'S CORRECTION, folded into the statement -- being a RELATIVELY CLOSED CODIMENSION-2 SEMIALGEBRAIC LOCUS with EMPTY INTERIOR cut by SIX conditions: the TWO EQUALITIES b_31 + b_33 = 0 and b_11 + b_13 = 0, and FOUR NON-STRICT SIGN CONDITIONS sigma_10 >= 0, sigma_12 >= 0, sigma_30 <= 0, sigma_32 <= 0 for m > 0, REVERSED for m < 0 and IDENTICALLY DEAD at m = 0 -- EACH OF THE SIX PROVEN NECESSARY by an exhibited carrier inside the admissible cone satisfying the other five, violating that one, and acquiring a STRICTLY NEGATIVE direction, with the violation inertias DISPLAYED at (3,4,1) and (5,2,1), each carrying n_- = 1; on the locus A\' = m/4 diag(b_30, 0, b_32, 0, 0, -b_10, 0, -b_12) and the admissible-cone witness reproduces m TIMES BLOCK 148\'S ESCAPE GRAM EXACTLY at INERTIA (4,4,0) in the COMMITTED (n_+, n_0, n_-) CONVENTION -- the solve\'s (4,0,4) being the OTHER convention and CORRECTED HERE AND EVERYWHERE -- with LIVE BLOCK (4,0,0), EIGENVALUES {0 x4, 15m/64 x4}, FOUR INDEPENDENT ROUTES AGREEING (symmetric congruence by the committed Block 144 helper, exact eigenvalues, leading principal minors of the live block, and a re-test at a ROOT-EXTENSION carrier so the positivity is NOT an artifact of rational fixtures), and m < 0 returning (0,4,4) so THE SIGN LAW IS REAL; CURVATURE IS REQUIRED, the completed pairing depending on EXACTLY FOUR of the 64 moduli, {b_10, b_12, b_30, b_32}, the ODD time slices at EVEN x, DISJOINT from the four {b_11, b_13, b_31, b_33} the forced locus consumes, which is precisely why the constraint and the positivity DO NOT COMPETE; BUT THE COMPLETED PAIRING IS IDENTICALLY ZERO ON EVERY FLAT CARRIER, SO IT DOES NOT REDUCE TO THE KNOWN FLAT FREE OS PAIRING -- A CALIBRATION GAP, RECORDED HERE AS AN OPEN DEFECT AND NOT AS A DISTINCTION, NOT AS A FEATURE AND NOT AS EVIDENCE THAT THE OBJECT IS INTRINSICALLY CURVED: the two candidate readings are that the pairing normalization degenerates in the flat limit and needs a carrier-dependent rescaling before comparison, or that the completed object is simply NOT the continuation of the flat pairing at all, AND THIS NOTE DECIDES NEITHER AND REPAIRS NEITHER\nlattice_wide: THE HERMITICITY GUARD, THE PREMISE-CONDITIONAL BREAK, THE HONEST CHARACTERIZATION, THE REGISTRATION STUDY, AND THE DOWNSTREAM: the mass ANTI-HERMITIAN DEFECT of P = m [theta\' H_q]_++ is supported on EXACTLY the two slot pairs (1,3) and (4,6), with entries -m(b_31 - b_33)/4 and -m(b_11 - b_13)/4, and the ENTIRE staggered-parity class is IDENTICALLY ZERO at those slots by the reach theorem because they are DEAD-DEAD while the class lives on DEAD-LIVE, so THE HERMITICITY DEFECT IS UNTOUCHABLE BY ANY COMPLETION IN THE CLASS and must be killed by the CARRIER or not at all; the COMPLETED atlas-global Hermiticity system has RANK 2 and KERNEL 62 with ROW SPACE EXACTLY {b_11 - b_13, b_31 - b_33}, against Block 153\'s rank 20 and kernel 44 for the bare pairing, and THAT KERNEL IS NOT INSIDE {b = 0} -- the PSD WITNESS IS ITSELF A KERNEL POINT, atlas-globally Hermitian with a LIVE SEAM and a LIVE MASS -- so BLOCK 145\'S MASS-EXCLUSION IS BROKEN, CONDITIONALLY ON THE COMPLETION AS A PREMISE (H5-154) AND ON NOTHING ELSE: this is NOT a refutation of Block 145, whose theorem concerns the UNCOMPLETED action and STANDS VERBATIM there and is REPRODUCED BY THE CONTROL, it is NOT a registration since NO completion is registered, and it is NOT an adoption since the VERDICT ON THE PREMISE LANDS IN BLOCK 155 -- A LANDED NEGATIVE BROKEN BY A PREMISE IS A STATEMENT ABOUT THE PREMISE AND NOT ABOUT THE NEGATIVE, and that is the form used throughout; the JOINT Hermiticity-and-PSD system has RANK 4, forcing b_11 = b_13 = b_31 = b_33 = 0 and leaving b_10, b_12, b_30, b_32 FREE, so the intersection is NONEMPTY precisely because the two modulus sets are DISJOINT; AND THE HONEST CHARACTERIZATION IS THAT THE POSITIVE OBJECT IS THE MASSIVE FREE PAIRING ON A SHEARED CARRIER -- the mass Gram m [theta\' H_q]_++, nothing else, on a carrier whose shear is what makes it nonzero -- while the COMPLETED CONNECTION SURVIVES on the carrier but ONLY OUTSIDE THE POSITIVE-TIME PAIRING, identically absent from [theta\' . ]_++, so this construction is NOT a demonstration that the connection can be MADE REFLECTION-POSITIVE but a demonstration that it can be REMOVED FROM THE PAIRING by a forced local deletion at an itemized price; WHAT A REGISTRATION WOULD HAVE TO COVER is DISPLAYED AS A STUDY AND NOT PROPOSED, REQUESTED OR IMPLIED -- (1) the SIXTEEN-EDGE FAMILY, one increment per healed edge since the support differs edge to edge; (2) the FIXTURE COEFFICIENTS, all EXACTLY -1; (3) the HOP SUPPORTS, which 16 of the 32 hops are deleted on each edge; (4) the ANTISYMMETRY LOSS and the failure of Q + Q^dagger = 2 m H_q; (5) the SYMMETRY COST, both unit translations broken with only period-2 time surviving; and (6) the UNRESOLVED FLAT-LIMIT CALIBRATION; DOWNSTREAM, the DISCRIMINATOR VERDICT on the premise is BLOCK 155\'S and is NOT TAKEN HERE, the FLAT-LIMIT CALIBRATION GAP is OPEN, the OWNER\'S ADOPTION DECISION on theta\' is STILL NOT TAKEN and cannot be taken here, the CAMPAIGN PIVOT to the CUTTING STRATA and the FRAME MAP is NAMED AND UNEXECUTED, the cycle-725/726/734 supplied-model firewall is INHERITED UNCHANGED, and the other lane\'s unmerged material is NOT READ, NOT CONSUMED and NOT SUPERSEDED\nRESULT: on the committed four-chart shear atlas at symbolic (s_x, s_t), the committed 64-modulus carrier family with its admissible cone, the committed sixteen healed edge actions and the committed [X Q]_++ half pairing, all imported through Block 153\'s committed runner from origin/main only, executing the REGISTERED-COMPLETION item of Block 153 against theta\' = (-1, 7, -1, 1) AS A CONSTRUCTION AND A PRICE: THE PAIRING SPLITS EXACTLY into DEAD-DEAD PURE MASS (m(b_31 + b_33)/8 at (1,3), -m(b_11 + b_13)/8 at (4,6)), LIVE-LIVE PURE MASS DIAGONAL (m/4 diag(b_30, b_32, -b_10, -b_12)) and DEAD-LIVE PURE CONNECTION (16 of 16 slots live on every edge), with the CLEAN sixteen-monomial dead-live form holding on the FOUR chart-0/1 edges ONLY and up to NINE monomials over 48 moduli on the other twelve, and a GENERIC X_0-ODD Delta K of DIMENSION 64 reaching EXACTLY those 32 dead-live slots at FULL RANK 16 with both parity controls confirming the partition; THE COMPLETION EXISTS AND IS FORCED -- [theta\' K_total]_++ = 0 IDENTICALLY IN ALL 64 MODULI, SOLVABLE ON 16 OF 16 EDGES, TOTAL across ALL 36 half-slots, MINIMAL SUPPORT 16 hops on SIX edges (the four chart-0/1 plus the self-edges (2,2), (3,3)) and 24 on the other TEN, UNIQUE ON THE DIFFERENTIAL\'S SUPPORT, and with EVERY COEFFICIENT EXACTLY -1 so that Delta d = -d and THE COMPLETION IS A LINK DELETION, d_total being d on 16 of its 32 hops, deleting the connection on EXACTLY the cover slices theta\' reflects into -- the increment CARRIER-INDEPENDENT while the induced Delta K is CARRIER-LINEAR, a carrier-CONSTANT Delta K barred by MODULUS HOMOGENEITY, class membership MEASURED at X_0-odd on 16/16, and TWO CAVEATS DISPLAYED: Delta K is NOT ANTISYMMETRIC so the completed action LOSES Q + Q^dagger = 2 m H_q, and the solution-space ranks are BASIS-DEPENDENT (112/248 against 104/156) so only SOLVABILITY and SUPPORT-UNIQUENESS are invariant; IT IS NOT A BOUNDARY TERM -- the seam-restricted system is INFEASIBLE, slices {0, 4, 5, 6, 7} are EACH INDIVIDUALLY NECESSARY (the solve\'s {0,5,6,7} NOT MAXIMAL, and slice 4 is a SEAM slice so the seam is INVOLVED but INSUFFICIENT ALONE), and BOTH unit translations are INFEASIBLE with only the PERIOD-2 time translation solvable; THE COMPLETED PAIRING EQUALS m [theta\' H_q]_++ EXACTLY on all sixteen edges, hence EDGE-INDEPENDENT with ZERO CONNECTION DATA and a surviving forcing of RANK 2 against Block 148\'s RANK 8, while WITHOUT the completion the same PSD step kills all eight odd shears; AND IT IS PSD ON A THIN SET -- a RELATIVELY CLOSED CODIMENSION-2 locus with EMPTY INTERIOR cut by b_31 + b_33 = 0, b_11 + b_13 = 0 and FOUR NON-STRICT signs (sigma_10, sigma_12 >= 0 and sigma_30, sigma_32 <= 0 for m > 0, reversed for m < 0, dead at m = 0), EACH of the six PROVEN NECESSARY with violation inertias (3,4,1) and (5,2,1) -- the witness reproducing m TIMES Block 148\'s ESCAPE GRAM at INERTIA (4,4,0) in the COMMITTED convention (the solve\'s (4,0,4) CORRECTED), live block (4,0,0), eigenvalues {0, 15m/64}, FOUR ROUTES including a ROOT-EXTENSION carrier, and CURVATURE REQUIRED on exactly {b_10, b_12, b_30, b_32}, DISJOINT from the forced four; BUT THE FLAT LIMIT IS AN OPEN DEFECT -- the completed pairing is IDENTICALLY ZERO on every flat carrier and DOES NOT REDUCE TO THE KNOWN FLAT FREE OS PAIRING, A CALIBRATION GAP AND NOT A DISTINCTION; and THE HERMITICITY GUARD at (1,3), (4,6) is UNTOUCHABLE BY THE CLASS while the COMPLETED Hermiticity system has RANK 2 / KERNEL 62 with row space exactly {b_11 - b_13, b_31 - b_33} and a kernel NOT INSIDE {b = 0}, the PSD witness being ITSELF a kernel point with a LIVE SEAM and a LIVE MASS, so BLOCK 145\'S MASS-EXCLUSION IS BROKEN CONDITIONALLY ON THE COMPLETION AS A PREMISE AND ON NOTHING ELSE: THE POSITIVE OBJECT IS THE MASSIVE FREE PAIRING ON A SHEARED CARRIER, THE CONNECTION WAS REMOVED FROM THE PAIRING AND NOT MADE POSITIVE, NO COMPLETION IS REGISTERED, NO CONVENTION IS ADOPTED, NO LANDED NOTE IS EDITED, AND THE VERDICT ON THE PREMISE IS BLOCK 155\'S\nDECISION_CUT: RUN THE BLOCK 155 DISCRIMINATORS AGAINST THE PREMISE -- they are aimed at exactly the items this note PROVED and PRICED, and Block 155 owns their final formulation: (1) THE FLAT-LIMIT CALIBRATION, the first and largest, since the completed pairing is IDENTICALLY ZERO on every flat carrier and therefore does NOT reduce to the known flat free OS pairing -- decide whether a carrier-dependent normalization repairs the comparison or whether the completed object is simply not the continuation of the flat pairing, because until this is settled NO curved-positivity reading of the construction is available at any scope; (2) THE DELETION, since d_total = d on 16 of its 32 hops and the deleted set is EXACTLY the cover slices the reflection carries the connection across -- decide whether that is the simplest possible completion or an arrangement for the reflection to see a free theory; (3) THE THIN LOCUS, since the PSD set is RELATIVELY CLOSED at CODIMENSION 2 with NON-STRICT signs and EMPTY INTERIOR -- decide whether two exact equalities on the carrier are a constraint a physical theory may impose or a fine-tuning that voids the claim; (4) THE ANTISYMMETRY LOSS, since Delta K is not antisymmetric and Q + Q^dagger = 2 m H_q FAILS for the completed action -- decide whether an action lacking the landed global form is admissible at all; and (5) THE SYMMETRY COST, since BOTH unit translations are broken and only the PERIOD-2 time translation survives -- decide whether a staggered-covariant lattice action is acceptable; THEN AND ONLY THEN DECIDE WHETHER ANY REGISTRATION IS WARRANTED, using the six-item study displayed in this note and adding nothing to it; DO NOT REGISTER THE COMPLETION IN THIS BLOCK OR THE NEXT WITHOUT THAT VERDICT; TAKE THE OWNER\'S ADOPTION DECISION ON THETA-PRIME, still open from Block 153 and still priced at at least seven landed constants, noting that the present construction changes the case in BOTH directions and settles neither; PIVOT THE CAMPAIGN TO THE CUTTING STRATA AND THE FRAME MAP, both named and unexecuted; LEAVE THE OTHER LANE\'S UNMERGED MATERIAL to that worker -- not read, not consumed, not superseded; and note that composite minimality, the cost-146 geometric gate, the entropy/counting-functional route candidate, the paired-degeneracy observable question and the common nilpotent differential remain named and unexecuted; curved OS is not decided, and NO first or novel curved positivity structure is claimed here or licensed by anything here\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero'


SCOPE_KEYS = (
    "split_three_block",
    "split_scope",
    "completion_deletion",
    "completion_six_edges",
    "completion_unique",
    "completion_antisymmetry",
    "honesty_period2",
    "honesty_bulk",
    "honesty_slice",
    "positivity_codimension",
    "positivity_witness",
    "positivity_eigenvalue",
    "positivity_curvature",
    "break_conditional",
    "break_kernel",
    "characterization_free_pairing",
    "characterization_no_registration",
    "calibration_gap",
    "panel",
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
    "no_first_curved_os_positivity",
)


def scope_certificate(note_text: str) -> dict[str, bool]:
    note = normalized_note(note_text)
    compact = compact_note(note_text)
    return {
        "split_three_block": "dead-live" in note or "three-block" in note,
        # Whitespace-insensitive so the note may write the scope either way.
        "split_scope": "4/16" in compact or "4 of 16" in note,
        "completion_deletion": "exactly -1" in note or "deletion" in note,
        "completion_six_edges": "six" in note and "edges" in note,
        "completion_unique": "unique" in note,
        "completion_antisymmetry": "not antisymmetric" in note
        or "antisymmetry" in note,
        "honesty_period2": "period-2" in note,
        "honesty_bulk": "bulk" in note,
        "honesty_slice": "slice" in note,
        "positivity_codimension": "codimension-2" in note or "not open" in note,
        "positivity_witness": "(4,4,0)" in compact,
        "positivity_eigenvalue": "15m/64" in compact,
        "positivity_curvature": "identically zero on flat" in note
        or "curvature" in note,
        "break_conditional": "premise-conditional" in note
        or "conditionally on the completion" in note,
        "break_kernel": "kernel 62" in note,
        "characterization_free_pairing": "free pairing" in note
        or "zero connection data" in note,
        "characterization_no_registration": "no registration is proposed" in note
        or "study" in note,
        "calibration_gap": "calibration" in note or "does not reduce" in note,
        "panel": "panel" in note or "discriminator" in note,
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
        # A NEGATIVE key: this block must NOT be written up as a first curved OS
        # positivity, so the phrase is required to be ABSENT.
        "no_first_curved_os_positivity": "first curved os positivity" not in note,
    }


# ---------------------------------------------------------------------------
# claims: the only thing a mutation is allowed to touch
# ---------------------------------------------------------------------------
def build_claims(mutation: str) -> dict[str, object]:
    claims: dict[str, object] = {
        "main_head": CURRENT_MAIN,
        "parent_pin": "resolved",
        "pure_split_edges": PURE_SPLIT_EDGES,
        "reach_rank": REACH_RANK,
        "deletion_coefficient": DELETION_COEFFICIENT,
        "antisymmetry_preserved": False,
        "unit_translation_feasible": False,
        "seam_feasible": False,
        "domain_codimension": DOMAIN_CODIMENSION,
        "witness_inertia": WITNESS_INERTIA,
        "connection_block_zero_edges": K_EDGE_COUNT,
        "completed_kernel_dim": COMPLETED_KERNEL_DIM,
        "break_conditional": True,
        "registration_status": REGISTRATION_STATUS,
        "required_scope_keys": SCOPE_KEYS,
    }
    if mutation == "stale_main_authority":
        claims["main_head"] = STALE_MAIN
    elif mutation == "stale_parent_authority":
        claims["parent_pin"] = "stale"
    elif mutation == "wrong_split_scope":
        claims["pure_split_edges"] = K_EDGE_COUNT
    elif mutation == "break_reach_rank":
        claims["reach_rank"] = REACH_RANK // 2
    elif mutation == "claim_coefficients_free":
        claims["deletion_coefficient"] = sp.Symbol("c", real=True)
    elif mutation == "claim_antisymmetry_kept":
        claims["antisymmetry_preserved"] = True
    elif mutation == "claim_unit_translation":
        claims["unit_translation_feasible"] = True
    elif mutation == "claim_seam_supportable":
        claims["seam_feasible"] = True
    elif mutation == "claim_domain_open":
        claims["domain_codimension"] = 0
    elif mutation == "wrong_witness_inertia":
        claims["witness_inertia"] = LIVE_BLOCK_INERTIA + (0,)
    elif mutation == "claim_connection_data":
        claims["connection_block_zero_edges"] = 0
    elif mutation == "wrong_kernel_dim":
        claims["completed_kernel_dim"] = PRIME_KERNEL_DIM
    elif mutation == "claim_break_unconditional":
        claims["break_conditional"] = False
    elif mutation == "claim_registration_proposed":
        claims["registration_status"] = "proposed"
    elif mutation == "drop_n5_fence":
        claims["required_scope_keys"] = tuple(
            key for key in SCOPE_KEYS if key != "n5_verbatim"
        )
    return claims


# ---------------------------------------------------------------------------
# gates: pure functions of the measured facts and the claims
# ---------------------------------------------------------------------------
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
            "docs/ADMISSIBILITY_DIRAC_KAHLER_UNIQUE_COMPLETION_PRICE_BOUNDED_THEOREM_NOTE_2026-08-20.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_BARE_CHARACTER_BOUNDED_THEOREM_NOTE_2026-08-20.md",
            "scripts/admissibility_dirac_kahler_bare_character_2026_08_20.py",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_GENERAL_MIGRATION_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-20.md",
            "scripts/admissibility_dirac_kahler_general_migration_theorem_2026_08_20.py",
        )
        and PARENT_ARTIFACTS
        == (BLOCK153_NOTE, BLOCK153_RUNNER, BLOCK148_NOTE, BLOCK148_RUNNER)
        and len(PARENT_ARTIFACT_BLOBS) == len(PARENT_ARTIFACTS)
        and facts.main_head == claims["main_head"]
        and authority.fixed_authority
        and authority.parent_ref_and_ancestry
        and parent_blobs_ok
    )

    gate_b = bool(
        facts.inertia_calibration
        and facts.inertia_order_pinned
        and facts.hermitian_conventions_agree
        and facts.operator_pinned
        and facts.dead_live_partition
        == (DEAD_SLOTS, LIVE_SLOTS, DEAD_SLOTS, True)
        and facts.three_block
        == (
            K_EDGE_COUNT,
            K_EDGE_COUNT,
            K_EDGE_COUNT,
            (DEAD_LIVE_TARGETS,),
        )
        and facts.split_scope
        == (
            claims["pure_split_edges"],
            tuple(sorted(CHART01_EDGES)),
            K_EDGE_COUNT - PURE_SPLIT_EDGES,
            (IMPURE_MAX_MONOMIALS,),
            (IMPURE_MODULI,),
        )
        and facts.reach
        == (
            REACH_PARAMETERS,
            True,
            True,
            (DEAD_LIVE_REACHED, DEAD_LIVE_CLASSES),
            (DEAD_LIVE_REACHED, DEAD_LIVE_CLASSES),
            True,
            claims["reach_rank"],
        )
        and facts.reach_controls
        == (
            (
                CONTROL_GENERIC_PARAMETERS,
                CONTROL_GENERIC_SUPPORT,
                GENERIC_CLASSES,
            ),
            (CONTROL_EVEN_PARAMETERS, CONTROL_EVEN_SUPPORT, EVEN_CLASSES),
        )
        and facts.exact_no_float
    )

    gate_c = bool(
        facts.action_law_pinned
        and facts.solvability == (K_EDGE_COUNT, K_EDGE_COUNT)
        and facts.minimal_support
        == (
            SMALL_EDGES,
            LARGE_EDGES,
            ((SMALL_SUPPORT, SMALL_DELETION),),
            ((LARGE_SUPPORT, LARGE_DELETION),),
            (SMALL_SUPPORT, LARGE_SUPPORT),
        )
        and facts.uniqueness == (True, True, True, K_EDGE_COUNT, K_EDGE_COUNT)
        and facts.deletion_values == (claims["deletion_coefficient"],)
        and facts.deletion_certificate
        == (
            K_EDGE_COUNT,
            K_EDGE_COUNT,
            SMALL_SUPPORT - SMALL_DELETION,
            SMALL_SUPPORT,
        )
        and facts.totality
        == (K_EDGE_COUNT, K_EDGE_COUNT, HALF_SLOTS, True)
        and facts.carrier_independence == (K_EDGE_COUNT, K_EDGE_COUNT)
        and facts.parity_membership
        == (K_EDGE_COUNT, K_EDGE_COUNT, K_EDGE_COUNT)
        and facts.antisymmetry_broken_edges
        == (0 if claims["antisymmetry_preserved"] else K_EDGE_COUNT)
        and facts.antisymmetry_profile
        == (
            K_EDGE_COUNT,
            K_EDGE_COUNT,
            (SYMMETRIC_PART_RANK,),
            K_EDGE_COUNT,
        )
        and facts.exact_no_float
    )

    gate_d = bool(
        facts.hop_space
        == (
            HOP_COUNT,
            HOP_PARAMETERS,
            FULL_TARGET_RANK,
            FULL_TARGET_RANK,
            True,
            True,
            K_EDGE_COUNT,
            K_EDGE_COUNT,
            HOP_RANKS,
        )
        and facts.seam
        == (
            SEAM_HOPS,
            BULK_HOPS,
            SEAM_IMAGE_RANK,
            FULL_TARGET_RANK,
            bool(claims["seam_feasible"]),
            0 if claims["seam_feasible"] else len(SEAM_PROBE_EDGES),
            len(SEAM_PROBE_EDGES),
        )
        and facts.slice_necessity
        == (
            NECESSARY_SLICES,
            OPTIONAL_SLICES,
            SLICE_VERDICTS,
            COMMON_NECESSARY_SLICES,
            SEAM_SLICE_EDGES,
            len(SLICE_PROBE_EDGES),
        )
        and facts.translation_tests
        == (
            (
                UNIT_T_LABEL,
                UNIT_T_RANK,
                UNIT_T_AUGMENTED,
                bool(claims["unit_translation_feasible"]),
            ),
            (
                UNIT_X_LABEL,
                UNIT_X_RANK,
                UNIT_X_AUGMENTED,
                bool(claims["unit_translation_feasible"]),
            ),
            (PERIOD2_LABEL, PERIOD2_RANK, PERIOD2_RANK, True),
            (PERIOD2_X_LABEL, PERIOD2_X_RANK, PERIOD2_X_RANK, True),
            (PERIOD2_BOTH_LABEL, PERIOD2_BOTH_RANK, PERIOD2_BOTH_RANK, True),
        )
        and facts.translation_control
        == (
            (
                UNIT_T_LABEL,
                UNIT_T_RANK,
                UNIT_T_AUGMENTED,
                bool(claims["unit_translation_feasible"]),
            ),
            (
                UNIT_X_LABEL,
                UNIT_X_RANK,
                UNIT_X_AUGMENTED,
                bool(claims["unit_translation_feasible"]),
            ),
        )
        and facts.strong_demand == (STRONG_DEMAND_RANK, True, True)
        and facts.exact_no_float
    )

    gate_e = bool(
        facts.completed_pairing
        == (
            K_EDGE_COUNT,
            K_EDGE_COUNT,
            claims["connection_block_zero_edges"],
            K_EDGE_COUNT,
        )
        and facts.completed_forcing
        == (DEAD_SLOTS, COMPLETED_FORCING_RANK, COMPLETED_FORCING_RANK)
        and facts.uncompleted_forcing == (UNCOMPLETED_FORCING_RANK,)
        and facts.domain_codimension == claims["domain_codimension"]
        and facts.domain_equalities
        == (
            ("b_11 + b_13", "b_31 + b_33"),
            ("b_11", "b_13", "b_31", "b_33"),
        )
        and facts.domain_signs
        == (
            (SIGN_VIOLATION_INERTIA,) * 4,
            (EQUALITY_VIOLATION_INERTIA,) * 2,
            # the m < 0 branch of the SAME domain: mirror every sign and the
            # mirrored witness is PSD again at m = -1
            WITNESS_INERTIA,
        )
        and facts.witness
        == (
            True,
            True,
            claims["witness_inertia"],
            LIVE_BLOCK_INERTIA,
            (sp.Integer(0), WITNESS_EIGENVALUE),
            True,
            K_EDGE_COUNT,
        )
        and facts.mass_signs == (NEGATIVE_MASS_INERTIA, ZERO_MASS_INERTIA)
        and facts.extra_witnesses
        == (True, True, WITNESS_INERTIA, True, WITNESS_INERTIA)
        and facts.carrier_scan == (SCAN_CARRIERS, SCAN_ON_LOCUS, SCAN_PSD)
        and facts.flat_zero
        and facts.moduli_dependence
        == (
            ("b_10", "b_12", "b_30", "b_32"),
            ("b_11", "b_13", "b_31", "b_33"),
            True,
            POSITIVITY_MODULI,
            LOCUS_MODULI,
        )
        and facts.exact_no_float
    )

    gate_f = bool(
        facts.untouchable
        == (UNTOUCHABLE_SLOTS, True, True, True, True)
        and facts.completed_hermiticity
        == (
            COMPLETED_HERMITICITY_RANK,
            claims["completed_kernel_dim"],
            ("b_11 - b_13", "b_31 - b_33"),
            (COMPLETED_HERMITICITY_RANK,),
        )
        and facts.hermiticity_controls
        == (
            PRIME_SYSTEM_RANK,
            PRIME_KERNEL_DIM,
            THETA_SYSTEM_RANK,
            THETA_KERNEL_DIM,
            COMPLETED_KERNEL_DIM,
            True,
        )
        and facts.kernel_witness
        == (True, True, True, True, WITNESS_INERTIA)
        and facts.break_conditionality
        == ((True, True) if claims["break_conditional"] else (False, False))
        and facts.exact_no_float
    )

    gate_g = bool(
        facts.edge_invariance == (1, 1, K_EDGE_COUNT)
        and facts.reflected_sector
        == (
            K_EDGE_COUNT,
            K_EDGE_COUNT,
            K_EDGE_COUNT,
            K_EDGE_COUNT,
            K_EDGE_COUNT,
        )
        and claims["registration_status"] == REGISTRATION_STATUS
        and facts.registration_contents == REGISTRATION_CONTENTS
        and len(facts.registration_contents) == REGISTRATION_ITEMS
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
            "also run the dead-live cancellation over the full 128-hop space on "
            "all sixteen edges, not only the probe edge"
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
        "main plus the committed Block 153 note/runner and Block 148 note/runner artifacts are content-bound",
        gate_values["A"],
    )
    checks.check(
        "B-three-block-split",
        "with DEAD = (1,3,4,6) and LIVE = (0,2,5,7) READ OFF the committed staggered parity X_0 and pinned against the structurally zero diagonal of the mass Gram, the theta' pairing splits on ALL SIXTEEN edges into a DEAD-DEAD block that is pure mass, m(b_31+b_33)/8 at (1,3) and -m(b_11+b_13)/8 at (4,6) and zero elsewhere; a LIVE-LIVE block that is pure mass and DIAGONAL, m/4 diag(b_30,b_32,-b_10,-b_12); and a DEAD-LIVE block that is PURE CONNECTION and live in 16 of 16 slots on every edge -- with the solve's single-monomial reading of that third block CORRECTED IN SCOPE to 4 OF 16 EDGES, the chart-0/1 ones, the other twelve running to nine monomials over forty-eight moduli; and the REACH THEOREM proved for a GENERIC X_0-odd antisymmetric Delta K with all 64 parameters, landing EXACTLY on the 32 dead-live slots, all live, at RANK 16 onto the 16 independent targets, with BOTH controls exhibited -- a generic antisymmetric Delta K at 120 parameters reaching all 64 slots and an X_0-EVEN one at 56 reaching exactly the complementary 32",
        gate_values["B"],
    )
    checks.check(
        "C-unique-completion",
        "restricted to the edge differential's own support the dead-live cancellation is SOLVABLE ON 16 OF 16 EDGES and kills ALL 36 independent half-slots, not just the 16 targeted; the determined set is EXACTLY HALF the support -- 16 of 32 hops on SIX edges, 24 of 48 on TEN -- every determined coefficient is EXACTLY -1 and the complementary half is entirely free, so the completion is a DELETION of a uniquely determined hop set with d_total = 0 there and d_total = d on the surviving 16 of 32; the induced Delta K is CARRIER-INDEPENDENT and X_0-ODD on all sixteen edges so the completion IS in Block 153's staggered-parity class; AND THE PRICE: Delta K is NOT antisymmetric, K_total is not either, and Q_c + Q_c^dagger != 2 m H_q with the symmetric part at RANK 8 on every edge, so Block 143's antisymmetric-residue character does NOT survive",
        gate_values["C"],
    )
    checks.check(
        "D-honesty-theorems",
        "over the full 128-hop nearest-neighbour completion space with 256 carrier-free parameters the dead-live target has RANK 104 and is SOLVABLE ON ALL SIXTEEN EDGES, and the STRONGER demand that the RAW half-block die on all 64 slots is solvable too at rank 128, so Hermiticity of the completed pairing is free; SEAM-SUPPORTED completions reach only RANK 32 against that 104 and are INFEASIBLE ON 16 OF 16 EDGES, so the premise is NOT a boundary term; dropping every hop that touches a cover time slice leaves the system INFEASIBLE for slices 0, 4, 5, 6 AND 7 at the probe edge, and ATLAS-WIDE exactly two verdicts occur, (0,4,5,6,7) and (0,5,6,7), whose COMMON CORE is the solve\'s four -- SLICE 4 IS NECESSARY ON 14 OF 16 EDGES, which is the correction, and slices 1, 2, 3 are optional everywhere; and the premise BREAKS TRANSLATION INVARIANCE -- a UNIT-TIME covariant completion is INFEASIBLE at rank 256 against augmented 257 and a UNIT-X one at rank 224 against 225, on the probe edge AND on a second control edge, while all three PERIOD-2 covariant demands are SOLVABLE, at ranks 244, 180 and 244 equal to their augmented ranks",
        gate_values["D"],
    )
    checks.check(
        "E-positivity",
        "the completed pairing is m [theta' H_q]_++ EXACTLY, raw and not merely Hermitian, on all sixteen edges, because [theta' K_total]_++ vanishes IDENTICALLY; the PSD forcing collapses from Block 148's reproduced RANK 8 to RANK 2 and its two survivors are EQUALITIES b_31+b_33 = 0 and b_11+b_13 = 0, so the positive domain is CODIMENSION 2 and NOT OPEN, with four SIGN conditions each independently necessary at violation inertia (3,4,1) and each equality violation at (5,2,1), all by symmetric congruence in the committed (n_+,n_0,n_-) order; at the cone witness the pairing is diag(15m/64,0,15m/64,0,0,15m/64,0,15m/64) at inertia (4,4,0) with a DEFINITE live block (4,0,0) and eigenvalues {0, 15m/64}, reversing to (0,4,4) at m < 0 and dying to (0,8,0) at m = 0; and it is IDENTICALLY ZERO on the flat carrier and depends on exactly four moduli b_10, b_12, b_30, b_32, disjoint from the four the forced locus uses",
        gate_values["E"],
    )
    checks.check(
        "F-conditional-break",
        "the four antiHermitian mass entries at (1,3), (3,1), (4,6), (6,4) are UNTOUCHABLE by any staggered-parity completion, the generic X_0-odd Delta K vanishing there in both the raw and the Hermitised half-block; the completed atlas-global Hermiticity system has RANK 2 and KERNEL 62 with the EXACT row space {b_11 - b_13, b_31 - b_33} and per-edge rank 2, against Block 153's reproduced 20/44 for theta' and Block 145's reproduced 18/46 for theta, and the kernel is NOT inside {b = 0}; at the cone witness the pairing satisfies both Hermiticity forms, is Hermitian, has a LIVE SEAM and a LIVE MASS Gram at inertia (4,4,0), so Block 145's verdict is BROKEN -- but PREMISE-CONDITIONALLY, since the uncompleted system still stands at rank 20 and the uncompleted pairing still dies identically when the eight odd shears are forced to zero",
        gate_values["F"],
    )
    checks.check(
        "G-free-pairing",
        "the completed pairing is EDGE-INDEPENDENT, one and the same 8x8 block on all sixteen edges, raw and Hermitised; the connection SURVIVES the completion -- K_c is nonzero, X_0-odd and shear-carrying on 16 of 16 edges -- while its ++ block [theta' K_c]_++ is IDENTICALLY ZERO on 16 of 16, so the pairing carries ZERO CONNECTION DATA (the full 8x16 reflected-sector statement is NOT made here and is carried to Block 155); and because a pairing that cannot see the connection does not reduce the calibration gap, the CONTENTS of the would-be registration are DISPLAYED as seven named items -- premise, support, coefficients, locality, symmetry, price, payoff -- and NO REGISTRATION IS PROPOSED",
        gate_values["G"],
    )
    checks.check(
        "H-note-scope",
        "the three-block split with its 4/16 scope correction, the deletion completion with its exactly -1 coefficients and its six-edge support and its uniqueness and its antisymmetry loss, the period-2 bulk slice honesty theorems, the codimension-2 domain with the (4,4,0) witness and the 15m/64 eigenvalue and the flat-carrier death, the premise-conditional break with kernel 62, the free-pairing characterisation with no registration proposed, the calibration gap, the panel, the cross-context disclosure, the firewalls and the exact N5 fence are present -- and the phrase 'first curved OS positivity' is ABSENT",
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
