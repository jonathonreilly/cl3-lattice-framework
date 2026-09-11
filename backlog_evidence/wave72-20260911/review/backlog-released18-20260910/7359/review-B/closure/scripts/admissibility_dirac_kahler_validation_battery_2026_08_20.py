#!/usr/bin/env python3
# Final path: scripts/admissibility_dirac_kahler_validation_battery_2026_08_20.py
"""Block 161: THE VALIDATION BATTERY.

SCOUT DISCIPLINE, AND IT IS A HARD BOUNDARY.  Every support restriction, every
reweighting, every reflection outside the committed four and every half carrier
outside the committed four exercised here is a REGISTERED-PREMISE-CLASS CHANGE
to the committed framework.  Each one is MEASURED and NONE of them is
registered, adopted, proposed or claimed.  Nothing in this runner edits, retires
or amends any committed note, axiom, premise or convention.  The owner adopts
nothing except axiom changes, and this block asks for no adoption.

THE VERDICT AGAINST THE PRE-REGISTERED BRANCHES (panel 3's kill-test battery,
whose seven tests and branch semantics were fixed BEFORE any measurement):

  THE DOOR READING IS DEAD.  T1 killed it, exactly as three of the five lenses
  predicted, and the mechanism is POSITIVITY BY DECOUPLING: on all six
  positive-semidefinite edges ker F(0) is four-dimensional and all 24 null
  vectors are EXACTLY odd-x; the odd-x rows of the 8x16 block [theta K]_++
  vanish identically; the residue K touches no odd-x row or column of the whole
  16x16; and on the cone the codimension-4 PSD locus IS the parity-decoupling
  locus.  The sharpest phrasing is LITERALLY true and it is the independent
  checker's verification: P = A-transpose A with A = sqrt(4/5) P_even, so the
  form is the PULLBACK of a positive definite form on the even-x quotient.

  T2 SPLITS: the form carries s_t LINEARLY -- it is NOT the fully
  connection-blind Block 154 class -- but it is completely s_x-BLIND, its
  first-order holonomy response is zero, a spatial dressing changes nothing at
  any order, and only 4 of the 8 supported cover hops feed the pairing at all.

  T4 REFUTES the Adams-style flavored-coefficient reading: over the 41-point
  lambda grid the only PSD-and-live point is lambda = 1 exactly, with the three
  pre-registered anchors reproduced.

  T6 AT ITS CORRECTED SCOPE.  The 6-of-12 signature reversals are measured and
  stand; the primary's "chart dependence" reading is DOWNGRADED by the checker,
  because the split obeys exactly value(i,j) = base(i) - s_t (lambda_j -
  lambda_i) -- the sign of a healing-weight-dependent scalar multiplying a fixed
  rank-4 pullback.  THE KILL RESTS ON T1 AND NEVER ON T6.

THE THETA-PRIME BLINDNESS THEOREM IS REFUTED AS STATED AND RE-SCOPED.  The
primary claimed an identically zero exchange pairing on all sixteen edges for
"ANY shears and ANY healing weights".  The exact annihilation condition is
Im(lambda_j - lambda_i) = 0 -- the REALITY of the healing-weight differences --
TOGETHER WITH a cover Hodge proportional to the identity.  The honest statement
is that the COMMITTED configuration sits inside theta-prime's annihilation set;
Block 160's codimension-8-of-48 framing was EXACT at its own quantifier scope
and the word "understates" is STRUCK.

THE MASS-SURVIVAL SUB-LOCUS STANDS AND IS SHARPENED.  The carrier-side balance
IS Block 147's annealed locus L147 = ker(R+1) verbatim; the witness sits in the
dimension-2 intersection L147 cap L154 and is not the dead carrier; there is NO
contradiction with Block 156, whose kill is theta-prime-scoped; and the all-mass
positivity is proved SYMBOLICALLY (dF/dm = 0 identically).  This note carries
the BLOCK 156 NARROWING: "The three loci pairwise meet only at the dead carrier"
is false as a bare subspace statement and true only with its own positivity
qualifier attached.

NO HARDCODED CERTIFICATE ANYWHERE: every printed numeral is recomputed in the
measurement pass from the committed constructors reached through the Block 160
runner, and no check is registered as a literal True.  Exact SymPy throughout;
no float enters any measured object, which is itself gated; the integer
monotonic clock is used only for the runtime gate.

PROVENANCE DISCLOSURE: the four-chart shear atlas, the local differential and
its EX/ET structure, the 64-modulus carrier model and its admissible cone, the
cover Hodge, the antiperiodic quotient, the sixteen healed edge differentials
and their healing weights, the half pairing, the committed theta and
theta-prime, the reflection move machinery, the Block 156 involution pairs and
locus dimensions, and the Block 144 symmetric-congruence inertia helper are ALL
COMMITTED objects, imported through the Block 160 runner (b160 -> b159 -> b158
-> b156 -> b155/b154/b153/b148/b147/b145/b144/b142/b137/b134/b105) and never
re-derived.  External lattice-gauge, staggered-fermion and Osterwalder-Schrader
literature is REFERENCED nowhere and BORROWED nowhere; every statement is
re-proved in-framework.

HYPOTHESES, named and not imported.  (H1) the pairing convention is [X Q]_{++}
on a half carrier of the cover.  (H3) "positive" is a statement about the
Hermitian part.  (H4) the physical cone is nu > 0, |sigma| < 1 per cell.
(H1-160) a pairing is exchange-compatible when the reflection carries the half
onto its complement.  (H1-161) a "validation battery" verdict is a statement
about THIS object -- the pure link deletion of a committed healed edge to the
eight even-x temporal crossing hops -- and about no wider class of objects.
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

import admissibility_dirac_kahler_exchange_condition_contract_2026_08_20 as b160

b159 = b160.b159
b158 = b159.b158
b156 = b159.b156
b148 = b159.b148
b147 = b159.b147
b145 = b159.b145
b144 = b159.b144
b142 = b159.b142

MASS = b159.MASS


NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_VALIDATION_BATTERY_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE SINGLE-PARENT PIN.  Block 160 (the exchange-condition contract) is BOTH
# the stack parent -- this block's branch is cut from it -- AND the content
# parent: every committed constructor used here is reached through the Block 160
# runner's own import chain (b159 -> b158 -> b156 -> b155/b154/b153/b148/b147/
# b145/b144/b142/b137/b134/b105), which Block 160's own gate A pins and this
# block does not duplicate.  So there are exactly TWO artifact pins here.
BLOCK160_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_EXCHANGE_CONDITION_CONTRACT_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
BLOCK160_RUNNER = (
    "scripts/admissibility_dirac_kahler_exchange_condition_contract_"
    "2026_08_20.py"
)

PARENT_ARTIFACTS = (BLOCK160_NOTE, BLOCK160_RUNNER)
# PLACEHOLDER BLOBS for the Block 160 pair, single-line hex literals; the
# landing supervisor refreshes exactly these two lines by anchored sed against
# the Block 160 branch tip.  Until they are refreshed gate A FAILS, which is the
# intended state of an unlanded draft.
PARENT_ARTIFACT_BLOBS = (
    "f3f96e3c5447e364e2dde0bc6e49a2da39adef66",   # Block 160 note
    "0dfe6128470ae16599f504abd6826d0928a8f76c",   # Block 160 runner
)

# Deliberately literal: this is the complete audit read surface.  Every entry is
# a WORKTREE-READABLE path at landing time; the cache envelope stats these, so an
# origin/main-only path here would break the audit (the Block 130 lesson,
# re-learned at the Block 150 landing and inherited through Blocks 151-160).
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_VALIDATION_BATTERY_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_EXCHANGE_CONDITION_CONTRACT_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/admissibility_dirac_kahler_exchange_condition_contract_2026_08_20.py",
)

AUDIT_TIMEOUT_SEC = 600
# Authority pins, single-line hex literals refreshed by anchored sed at landing.
CURRENT_MAIN = "005f047923055e6ecd5dc8bce1ffd71765c2ffd8"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
# This block stacks on Block 160, so the parent branch is Block 160's.
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block160-exchange-condition-contract-20260820"
)
# The Block 160 branch tip, VERIFIED to be an ancestor of HEAD and to carry both
# pinned artifact paths.  The two BLOB lines above are the placeholders.
PARENT_COMMIT = "91cad4272b0727d1af828069a89d8ca7a79cd9c9"
# Block 154's tip: a real ancestor of HEAD that PREDATES BOTH pinned parent
# artifacts.  VERIFIED before pinning with `git rev-parse <commit>:<path>`,
# which FAILS for the Block 160 note AND the Block 160 runner at this commit, so
# resolving the parent pin here leaves BOTH pinned blobs ABSENT.  This pin is
# read ONLY under the stale mutation; the baseline gate never requires it.
STALE_PARENT_COMMIT = "301f7f8b1553170e655fbb8d6768b06da850370f"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_nulls_balanced",
    "break_factorization",
    "claim_sx_dependence",
    "break_stabilizer",
    "claim_adams_onset",
    "claim_chart_dependence",
    "break_counterterm_reach",
    "claim_theta_prime_universal",
    "claim_locus_contradicts_b156",
    "break_mass_independence",
    "drop_b156_narrowing",
    "drop_survivors",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_nulls_balanced": "B",
    "break_factorization": "B",
    "claim_sx_dependence": "C",
    "break_stabilizer": "D",
    "claim_adams_onset": "E",
    "claim_chart_dependence": "E",
    "break_counterterm_reach": "F",
    "claim_theta_prime_universal": "G",
    "claim_locus_contradicts_b156": "G",
    "break_mass_independence": "G",
    "drop_b156_narrowing": "H",
    "drop_survivors": "H",
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
    return b159.no_float(value)


def congruence_inertia(matrix: sp.MatrixBase) -> tuple[int, int, int]:
    """Exact (n_positive, n_zero, n_negative) WITH multiplicity, by congruence.

    Delegated to the COMMITTED Block 144 helper through the Block 160/159/158/
    156 import chain, so the tool this block reasons with is exactly the blob
    Block 160's gate A pins.  Called on EXACT algebraic matrices only.
    """
    return b159.inertia(matrix)


def sturm_inertia(matrix: sp.MatrixBase) -> tuple[int, int, int]:
    """The SECOND, INDEPENDENT inertia route, used only under --deep.

    Exact real-root counting on the characteristic polynomial of a Hermitian
    matrix with rational entries.  Legitimate because a Hermitian spectrum is
    real; it shares no code path with the committed congruence helper, so an
    agreement between the two is a genuine cross-check rather than a repeat.
    """
    variable = sp.Symbol("_sturm_x")
    size = matrix.rows
    poly = sp.Poly(matrix.charpoly(variable).as_expr(), variable)
    roots = poly.real_roots()          # WITH multiplicity, exact algebraics
    if len(roots) != size:
        # a non-real spectrum would land here and be reported as a mismatch
        # rather than silently agreeing with the congruence route
        return (-1, -1, -1)
    positive = sum(1 for r in roots if r > 0)
    negative = sum(1 for r in roots if r < 0)
    return (positive, size - positive - negative, negative)


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
# the committed model, imported wholesale through Block 160
# ---------------------------------------------------------------------------
SHEAR_X, SHEAR_T = b159.SHEAR_X, b159.SHEAR_T
THETA, THETA_PRIME_OP = b159.THETA, b159.THETA_PRIME_OP
HEALING_WEIGHTS = b159.HEALING_WEIGHTS
EDGE_KEYS = b159.EDGE_KEYS
LIVE, DEAD = b159.LIVE, b159.DEAD
HALF = b159.HALF_DIM                      # 8
PHYS = b159.PHYS                          # 16
SIZE = b159.SIZE                          # 32
COVER_T, LX = b159.COVER_T, b159.LX
ATLAS = b159.ATLAS
PROBE_EDGE = b159.PROBE_EDGE

zero, herm, sub_block, live_count = (
    b159.zero, b159.herm, b159.sub_block, b159.live_count
)
clean = b159.clean
cover_index, cover_site = b159.cover_index, b159.cover_site
half_selector, half_pairing, exchange_tag = (
    b159.half_selector, b159.half_pairing, b159.exchange_tag
)
COMMITTED_ROWS = b159.HALVES[0][1]        # the committed half {p = 0, 1}
PRESERVING_ROWS = b159.HALVES[1][1]

# the half-slot <-> site dictionary: half slot j <-> PHYS row j <-> cover site
# (j // 4, j % 4), so the spatial column of slot j is j % 4.
EVEN_SLOTS = tuple(j for j in range(HALF) if j % LX % 2 == 0)     # (0,2,4,6)
ODD_SLOTS = tuple(j for j in range(HALF) if j % LX % 2 == 1)      # (1,3,5,7)
P_EVEN = sp.diag(*[1 if j in EVEN_SLOTS else 0 for j in range(HALF)])
P_ODD = sp.eye(HALF) - P_EVEN
QUOTIENT_PROJECTION = sp.Matrix(
    len(EVEN_SLOTS), HALF,
    lambda r, c: 1 if c == EVEN_SLOTS[r] else 0,
)

EVEN_CELLS = ((0, 0), (0, 2), (2, 0), (2, 2))
B_EVEN = tuple(b145.B_MODULUS[cell] for cell in EVEN_CELLS)


# ---------------------------------------------------------------------------
# the certificate constants this runner is claiming
# ---------------------------------------------------------------------------
EDGE_COUNT = 16
LIVE_EDGES = 12
PSD_EDGES = ((0, 3), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3))
PSD_EDGE_COUNT = 6
NSD_EDGE_COUNT = 6
EMPTY_EDGE_COUNT = 4
PRIMARY_EDGE = (2, 2)
PSD_INERTIA = (4, 4, 0)
NSD_INERTIA = (0, 4, 4)
DEAD_INERTIA = (0, 8, 0)
ODD_X_INERTIA = (2, 4, 2)
FULL_CROSSING_INERTIA = (6, 0, 2)
MASSIVE_CURVED_INERTIA = (4, 0, 4)
PRIMARY_DIAGONAL = R(4, 5)
NULL_DIMENSION = 4
NULL_VECTORS = 24
ROW_OCCUPANCY = (1, 0, 1, 0, 1, 0, 1, 0)
CONE_OFF_DIAGONAL = ((0, 7), (1, 4), (2, 5), (3, 6))
CONE_COORDINATES = 32
CSTAR_CORE = (R(257, 240), R(229, 210), R(31, 30), R(79, 75))
FEEDING_HOPS = 4
DIPOLE_PLAQUETTES = 2
GAUGE_PLAQUETTES = 0
STABILIZER_ORDER = 8
STABILIZER_SHIFTS = tuple(
    sorted((pt, px) for pt in (0, 2, 4, 6) for px in (0, 2))
)
TRANSLATION_GROUP = 32
ORBIT_CENSUS = {(4, 4, 0): 8, (2, 4, 2): 8, (0, 8, 0): 16}
EVEN_X_SPECTRUM = {R(4, 5): 4, sp.Integer(0): 4}
ODD_X_SPECTRUM = {R(4, 5): 2, sp.Integer(0): 4, R(-4, 5): 2}
ODD_X_OFF_DIAGONAL = ((1, 3), (5, 7))
GRID_POINTS = 41
ANCHOR_INERTIA = {
    R(1): PSD_INERTIA, R(-1): ODD_X_INERTIA, R(0): FULL_CROSSING_INERTIA,
}
DEEP_CONFIGURATIONS = 10
CHART_SCALE = R(257, 192)
CHART_POSITIVE = 6
CHART_NEGATIVE = 6
MASS_SLOTS = ((0, 3), (1, 2), (4, 5), (6, 7))
COUNTERTERM_ODD_ODD = ((1, 3), (5, 7))
COUNTERTERM_EVEN_ODD = (
    (0, 5), (0, 7), (2, 5), (2, 7), (4, 1), (4, 3), (6, 1), (6, 3)
)
SECOND_ORDER_INERTIA = (0, 4, 4)
SECOND_ORDER_EIGENVALUES = (
    R(-375, 51296), R(-1215, 263168), R(-1215, 253952), R(-507, 1294336),
)
SCALING_AMPLITUDES = (R(1), R(1, 2), R(1, 4))
SCALING_ENCLOSURES = (
    (R(-27372166, 10 ** 10), R(-27372165, 10 ** 10)),
    (R(-573568366, 10 ** 12), R(-573568365, 10 ** 12)),
    (R(-137513651, 10 ** 12), R(-137513650, 10 ** 12)),
)
SCALING_RATIO_WINDOWS = (
    (R(477225, 100000), R(477226, 100000)),
    (R(417099, 100000), R(417100, 100000)),
)
WITNESS_DIAGONAL = R(33, 40)
WITNESS_MOMENT = R(3, 8)
ODD_MOMENTS = 8
BALANCE_EQUATIONS = 4
PSD_EQUATIONS = 4
SURVIVAL_CODIMENSION = 8
TIED_WEIGHTS = 24
TIED_PARAMETERS = 48
VANISHING_CODIMENSION = 8
COMMITTED_IMAGE_RANK = 3
COMMITTED_FAMILY_PARAMETERS = 6
THETA_PRIME_REAL_ZERO = 16
THETA_REAL_ZERO = 2
THETA_PRIME_COMPLEX_ZERO = 4
THETA_PRIME_CURVED_ZERO = 0
THETA_PRIME_CURVED_LIVE_ZERO = 16
FREE_VOLUME_ZERO_EDGES = ((0, 0), (1, 1))
UNIFORM_VOLUMES = (sp.Integer(2), R(1, 2))
SINGLE_CELL_REVIVALS = 16
TIED_GENERATOR_CLASSES = 512
TIED_REAL_GENERATORS = 1024
MASS_REACHING_GENERATORS = 64
MASS_REACHING_CLASSES = 32
MASS_REACHING_HOPS = 64
MASS_REACHING_DISPLACEMENTS = ((1, 3), (3, 1), (5, 3), (7, 1))
CURVED_EXTRA_DISPLACEMENTS = ((0, 0), (2, 2), (4, 0), (6, 2))
CURVED_EXTRA_HOPS = 128
COMMITTED_DISPLACEMENTS = ((1, 0), (7, 0), (0, 1), (0, 3))
PROBE_SUPPORT = 48
POOL_TWO_LEADS = 3

RUNTIME_BUDGET_SEC = 150


# ---------------------------------------------------------------------------
# constructions.  Everything below is built from the committed primitives.
# ---------------------------------------------------------------------------
def crossing_hops(columns) -> tuple:
    """The temporal half-boundary-crossing cover hops on the given columns.

    Cover hops (1,x) <- (2,x) and (3,x) <- (4,x), antiperiodically imaged.
    Every one lies in the committed displacement class (-1,0) and inside the
    committed probe edge's own 48-hop support, so restricting to them is a LINK
    DELETION and never a support widening.
    """
    out = []
    for x in columns:
        for target_t, source_t in ((1, 2), (3, 4)):
            p, q = cover_index(target_t, x), cover_index(source_t, x)
            out.append((p, q))
            out.append(((p + PHYS) % SIZE, (q + PHYS) % SIZE))
    return tuple(out)


EVEN_SUPPORT = crossing_hops((0, 2))
ODD_SUPPORT = crossing_hops((1, 3))


def restrict(matrix: sp.Matrix, support) -> sp.Matrix:
    out = sp.zeros(SIZE, SIZE)
    for p, q in support:
        out[p, q] = matrix[p, q]
    return out


def field_of(sigma: dict, volume=None) -> dict:
    volume = volume or {}
    return {
        (t, x): (
            sigma.get((t, x), sp.Integer(0)),
            volume.get((t, x), sp.Integer(1)),
        )
        for t in range(4)
        for x in range(LX)
    }


def pairing_of(differential, hodge, mass=sp.Integer(0), operator=None):
    operator = THETA if operator is None else operator
    return clean(
        half_pairing(
            operator, b145.quotient_action(differential, hodge, mass),
            COMMITTED_ROWS,
        )
    )


def symbolic_pairing(differential, hodge, mass=sp.Integer(0), operator=None):
    operator = THETA if operator is None else operator
    raw = half_pairing(
        operator, b145.quotient_action(differential, hodge, mass),
        COMMITTED_ROWS,
    )
    return sp.Matrix(HALF, HALF, lambda i, j: sp.expand(raw[i, j]))


def parity_fraction(vector: sp.Matrix) -> tuple:
    """(||P_even v||^2, ||P_odd v||^2) normalised, EXACT rationals."""
    norm = sp.expand(sum(sp.Abs(vector[i]) ** 2 for i in range(HALF)))
    even = sp.expand(sum(sp.Abs(vector[i]) ** 2 for i in EVEN_SLOTS))
    return (sp.simplify(even / norm), sp.simplify(1 - even / norm))


def null_projector(matrix: sp.Matrix) -> tuple:
    basis = sp.GramSchmidt([sp.Matrix(v) for v in matrix.nullspace()], True)
    projector = sp.zeros(HALF, HALF)
    for vector in basis:
        projector += vector * vector.H
    return basis, projector


def even_content_of_nullspace(matrix: sp.Matrix):
    """trace(Pi P_even)/dim on the null space -- basis-free and EXACT."""
    vectors = matrix.nullspace()
    if not vectors:
        return (0, None)
    stack = sp.Matrix.hstack(*vectors)
    gram = sp.simplify(stack.H * stack)
    value = sp.simplify(
        sp.trace(gram.inv() * (stack.H * P_EVEN * stack)) / len(vectors)
    )
    return (len(vectors), sp.nsimplify(value))


def most_negative_enclosure(matrix: sp.Matrix, window) -> bool:
    """Certify low < r < high for the most negative eigenvalue, EXACTLY.

    Exact real-root counting on the characteristic polynomial: no root at all
    below `low`, and exactly one inside the window.  No float is created.
    """
    low, high = window
    variable = sp.Symbol("_enclosure_x")
    poly = sp.Poly(matrix.charpoly(variable).as_expr(), variable)
    bound = 1 + sum(abs(c) for c in poly.all_coeffs())
    return bool(
        poly.count_roots(-bound, low) == 0 and poly.count_roots(low, high) == 1
    )


def ratio_window(upper, lower) -> tuple:
    """|upper| / |lower| as a rational interval, both enclosures negative."""
    return (abs(upper[1]) / abs(lower[0]), abs(upper[0]) / abs(lower[1]))


def locus_rows(pairs) -> sp.Matrix:
    """The rows v[i] + v[j] = 0 on the committed ordered odd-moment basis."""
    rows = []
    for i, j in pairs:
        row = [sp.Integer(0)] * len(b156.ODD)
        row[i] = sp.Integer(1)
        row[j] = sp.Integer(1)
        rows.append(row)
    return sp.Matrix(rows)


def kernel_dimension(matrix: sp.Matrix) -> int:
    return len(b156.ODD) - matrix.rank()


def odd_moment_vector(field: dict) -> tuple:
    _nu, _a, moduli, _inv = b145.moduli_from_field(field)
    return tuple(
        sp.nsimplify(moduli[(int(str(s)[2]), int(str(s)[3]))])
        for s in b145.ODD_SHEAR_COORDS
    )


def transport_field(field: dict, label: tuple) -> dict:
    _et, pt, _ex, px = label
    return {
        ((t + pt) % 4, (x + px) % LX): field[(t, x)]
        for t in range(4)
        for x in range(LX)
    }


CSTAR = field_of(
    {
        (1, 0): R(1, 3), (1, 2): R(-1, 3), (3, 1): R(2, 5), (1, 1): R(1, 4),
        (0, 1): R(1, 5), (2, 3): R(-1, 5), (3, 3): R(1, 3),
    },
    {(t, x): (R(3, 2) if t % 2 else R(2, 3)) for t in range(4) for x in range(LX)},
)
BALANCED = field_of({
    (1, 0): R(1, 3), (1, 3): R(-1, 3), (1, 1): R(1, 3), (1, 2): R(-1, 3),
    (3, 0): R(1, 3), (3, 3): R(-1, 3), (3, 1): R(1, 3), (3, 2): R(-1, 3),
})
ON_LOCUS_A = field_of(
    {(1, 0): R(1, 3), (1, 2): R(-1, 3), (3, 0): R(1, 3), (3, 2): R(-1, 3)}
)
OFF_LOCUS_A = field_of({cell: R(1, 5) for cell in EVEN_CELLS})
OFF_LOCUS_B = field_of(
    {(0, 0): R(1, 3), (1, 1): R(1, 4)},
    {(t, x): (sp.Integer(2) if x % 2 else sp.Integer(1))
     for t in range(4) for x in range(LX)},
)
LAMBDA = sp.Symbol("lam")
ALPHA = sp.Symbol("alpha", real=True)


# ---------------------------------------------------------------------------
# measured facts (computed once, before any mutation flag is consulted)
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Facts:
    main_head: str
    authority: AuthorityCertificate
    # B: the object, and T1's decoupling kill
    calibration: tuple
    decoupling: tuple
    factorization: tuple
    # C: T2's content and holonomy derivative
    content: tuple
    holonomy: tuple
    # D: T3's stabilizer and T7's riders
    orbit: tuple
    riders: tuple
    # E: T4's lambda family and T6 at its corrected scope
    family: tuple
    chart_law: tuple
    # F: T5's mass-lift order
    mass_order: tuple
    counterterm: tuple
    scaling: tuple
    # G: the theta-prime scope and the mass-survival stratum
    blindness: tuple
    stratum: tuple
    # deep sweeps
    deep_family: object
    deep_generators: object
    # H / global
    exact_no_float: bool
    scope: dict


def measure(deep: bool) -> Facts:
    main_head = git_output("rev-parse", "origin/main")
    authority = authority_certificate(main_head)
    exact: list = []

    # -----------------------------------------------------------------------
    # the committed constructions, imported and never re-derived
    # -----------------------------------------------------------------------
    differentials, star = b145.connection(SHEAR_X, SHEAR_T)
    edges_symbolic = b145.edge_differentials(
        differentials, star, HEALING_WEIGHTS
    )
    edge = {
        key: sp.expand(edges_symbolic[key].xreplace(ATLAS))
        for key in EDGE_KEYS
    }
    flat_cover = b145.cover_hodge_from_field(b159.flat_field())
    free_cover = b145.cover_hodge_general(
        b145.NU_MODULUS, b145.A_MODULUS, b145.B_MODULUS, b145.INV_MODULUS
    )
    cstar_cover = b145.cover_hodge_from_field(CSTAR)
    obj = restrict(edge[PRIMARY_EDGE], EVEN_SUPPORT)
    shear_t_value = ATLAS[SHEAR_T]

    # ---------------------------------------------------------------- B ----
    deletion = []
    for key in EDGE_KEYS:
        pairing = pairing_of(restrict(edge[key], EVEN_SUPPORT), flat_cover)
        deletion.append((key, congruence_inertia(pairing)))
    psd_edges = tuple(sorted(k for k, s in deletion if s == PSD_INERTIA))
    primary = pairing_of(obj, flat_cover)
    calibration = (
        b145.in_admissible_cone(b159.flat_field()),
        flat_cover == sp.eye(SIZE),
        b145.quotient(flat_cover) == sp.eye(PHYS),
        exchange_tag(THETA, COMMITTED_ROWS),
        psd_edges,
        sum(1 for _k, s in deletion if s == NSD_INERTIA),
        sum(1 for _k, s in deletion if s == DEAD_INERTIA),
        primary == sp.diag(
            *[PRIMARY_DIAGONAL if j in EVEN_SLOTS else 0 for j in range(HALF)]
        ),
        primary.rank(),
        congruence_inertia(primary),
        all(
            zero(sp.expand(pairing_of(obj, flat_cover, m) - primary))
            for m in (R(1, 10), sp.Integer(1), sp.Integer(5))
        ),
        sum(1 for entry in edge[PROBE_EDGE] if entry != 0),
    )
    exact.append(sum(primary))

    null_rows = []
    for key in psd_edges:
        pairing = pairing_of(restrict(edge[key], EVEN_SUPPORT), flat_cover)
        basis, _projector = null_projector(pairing)
        null_rows.append(
            (key, len(basis), tuple(parity_fraction(v) for v in basis))
        )
    block_8x16 = sp.expand(
        half_selector(COMMITTED_ROWS).T
        * THETA
        * b145.quotient_action(obj, flat_cover, sp.Integer(0))
    )
    occupancy = tuple(
        sum(1 for j in range(PHYS) if sp.expand(block_8x16[i, j]) != 0)
        for i in range(HALF)
    )
    residue = b145.quotient_action(obj, flat_cover, sp.Integer(0))
    odd_physical = tuple(r for r in range(PHYS) if r % LX in (1, 3))
    mass_raw = sp.expand(
        half_selector(COMMITTED_ROWS).T * THETA * b145.quotient(flat_cover)
    )
    cone = symbolic_pairing(obj, free_cover)
    cone_off = tuple(
        (i, j)
        for i in range(HALF) for j in range(HALF)
        if i < j and sp.simplify(cone[i, j]) != 0
    )
    cone_shears = set()
    for entry in cone:
        cone_shears |= set(sp.expand(entry).free_symbols) & set(
            b145.SHEAR_COORDS
        )
    decoupling = (
        tuple(row[1] for row in null_rows),
        sum(len(row[2]) for row in null_rows),
        all(f == (0, 1) for row in null_rows for f in row[2]),
        occupancy,
        all(
            sp.expand(residue[i, j]) == 0
            for i in range(PHYS) for j in range(PHYS)
            if (i in odd_physical) or (j in odd_physical)
        ),
        not zero(mass_raw)
        and zero(sp.expand(herm(mass_raw * half_selector(COMMITTED_ROWS)))),
        cone_off,
        all((i in EVEN_SLOTS) != (j in EVEN_SLOTS) for i, j in cone_off),
        tuple(sorted(str(s) for s in cone_shears)),
        tuple(
            sp.simplify(cone[i, j] * 10) for i, j in cone_off
        ),
    )
    exact.append(sum(cone[i, j] for i, j in cone_off))

    quotient_core = sp.Matrix(
        len(EVEN_SLOTS), len(EVEN_SLOTS),
        lambda r, c: primary[EVEN_SLOTS[r], EVEN_SLOTS[c]],
    )
    root = sp.sqrt(PRIMARY_DIAGONAL)
    factor = root * QUOTIENT_PROJECTION
    cstar_pairing = pairing_of(obj, cstar_cover)
    cstar_core = sp.Matrix(
        len(EVEN_SLOTS), len(EVEN_SLOTS),
        lambda r, c: cstar_pairing[EVEN_SLOTS[r], EVEN_SLOTS[c]],
    )
    factorization = (
        quotient_core == PRIMARY_DIAGONAL * sp.eye(len(EVEN_SLOTS)),
        zero(sp.expand(primary - factor.T * factor)),
        zero(sp.expand(primary - P_EVEN.T * primary * P_EVEN)),
        no_float(sum(factor)),
        tuple(cstar_core[k, k] for k in range(len(EVEN_SLOTS))),
        cstar_core.is_diagonal(),
        zero(
            sp.expand(
                cstar_pairing
                - QUOTIENT_PROJECTION.T * cstar_core * QUOTIENT_PROJECTION
            )
        ),
    )
    exact.append(sum(factor))

    # ---------------------------------------------------------------- C ----
    symbolic_object = restrict(
        sp.expand(edges_symbolic[PRIMARY_EDGE]), EVEN_SUPPORT
    )
    symbolic_form = symbolic_pairing(symbolic_object, flat_cover)
    content = (
        tuple(sorted(str(s) for s in symbolic_form.free_symbols)),
        symbolic_form == sp.diag(
            *[SHEAR_T if j in EVEN_SLOTS else 0 for j in range(HALF)]
        ),
        zero(sp.expand(symbolic_form.xreplace({SHEAR_T: 0}))),
        SHEAR_X in symbolic_form.free_symbols,
    )
    exact.append(sum(symbolic_form))

    phase = sp.exp(sp.I * ALPHA)
    dressing = {}
    for x in (0, 2):
        dressing[((2, x), (1, x))] = phase
        dressing[((6, x), (5, x))] = phase
        dressing[((4, x), (3, x))] = phase
        dressing[((0, x), (7, x))] = phase
    dressed_field = b159.link_field(dressing)
    dressed = sp.Matrix(
        HALF, HALF,
        lambda i, j: sp.simplify(
            half_pairing(
                THETA,
                b145.quotient_action(
                    b159.dress(obj, dressed_field), flat_cover, sp.Integer(0)
                ),
                COMMITTED_ROWS,
            )[i, j]
        ),
    )
    spectrum = {sp.simplify(v): m for v, m in dressed.eigenvals().items()}
    derivatives = {
        sp.simplify(sp.diff(v, ALPHA).subs(ALPHA, 0)) for v in spectrum
    }
    marker = sp.Symbol("_feed_z")
    feeding = []
    for p, q in EVEN_SUPPORT:
        probe = sp.Matrix(obj)
        probe[p, q] = marker
        names = set()
        for entry in half_pairing(
            THETA, b145.quotient_action(probe, flat_cover, sp.Integer(0)),
            COMMITTED_ROWS,
        ):
            names |= sp.expand(entry).free_symbols
        if marker in names:
            feeding.append((cover_site(p), cover_site(q)))
    spatial_field = b159.link_field({((0, 0), (0, 1)): phase})
    _values, nontrivial = b159.census(spatial_field)
    unit = R(3, 5) + sp.I * R(4, 5)
    gauge = []
    for exponent in (lambda t, x: t, lambda t, x: t + x):
        phases = {
            (t, x): sp.expand(unit ** exponent(t, x))
            for t in range(COVER_T) for x in range(LX)
        }
        gauge_field = b159.pure_gauge_field(phases)
        _v, gauge_nontrivial = b159.census(gauge_field)
        gauge_pairing = pairing_of(
            b159.dress(obj, gauge_field), flat_cover
        )
        gauge.append(
            (
                len(gauge_nontrivial),
                congruence_inertia(gauge_pairing),
                zero(sp.expand(gauge_pairing - primary)),
            )
        )
    holonomy = (
        spectrum == {PRIMARY_DIAGONAL * sp.cos(ALPHA): 4, sp.Integer(0): 4},
        derivatives == {sp.Integer(0)},
        congruence_inertia(clean(dressed.xreplace({ALPHA: sp.pi / 3}))),
        congruence_inertia(clean(dressed.xreplace({ALPHA: sp.pi / 2}))),
        congruence_inertia(clean(dressed.xreplace({ALPHA: 2 * sp.pi / 3}))),
        len(feeding),
        tuple(sorted({hop[0][0] for hop in feeding})),
        len(nontrivial),
        zero(sp.expand(b159.dress(obj, spatial_field) - obj)),
        tuple(gauge),
    )

    # ---------------------------------------------------------------- D ----
    orbit_rows = {}
    for name, field in (("flat", b159.flat_field()), ("c*", CSTAR)):
        cover = b145.cover_hodge_from_field(field)
        census = collections.Counter()
        rows = []
        for pt in range(COVER_T):
            for px in range(LX):
                move = b148.move_matrix(b148.move_permutation((1, pt, 1, px)))
                moved = pairing_of(
                    sp.expand(move * obj * move.T),
                    sp.expand(move * cover * move.T),
                )
                signature = congruence_inertia(moved)
                census[signature] += 1
                rows.append(((pt, px), signature, zero(moved)))
        orbit_rows[name] = (dict(census), rows)
    flat_census, flat_rows = orbit_rows["flat"]
    star_census, star_rows = orbit_rows["c*"]
    stabilizer = tuple(
        sorted(s for s, sig, dead in flat_rows if sig == PSD_INERTIA and not dead)
    )
    stabilizer_set = set(stabilizer)
    closed = all(
        ((a[0] + b[0]) % COVER_T, (a[1] + b[1]) % LX) in stabilizer_set
        for a in stabilizer for b in stabilizer
    )
    inverses = all(
        ((-a[0]) % COVER_T, (-a[1]) % LX) in stabilizer_set for a in stabilizer
    )
    dead_shifts = tuple(s for s, sig, _d in flat_rows if sig == DEAD_INERTIA)
    orbit = (
        len(flat_rows),
        flat_census,
        star_census,
        stabilizer,
        len(stabilizer),
        closed,
        inverses,
        (0, 0) in stabilizer_set,
        tuple(sorted({s[0] % 2 for s in dead_shifts})),
        len(dead_shifts),
        all(
            sig == ODD_X_INERTIA
            for s, sig, _d in flat_rows
            if s[0] % 2 == 0 and s[1] % 2 == 1
        ),
        tuple(
            sorted(s for s, sig, dead in star_rows
                   if sig == PSD_INERTIA and not dead)
        ),
    )

    odd_object = pairing_of(restrict(edge[PRIMARY_EDGE], ODD_SUPPORT), flat_cover)
    flipped = {s: -s for s in b145.SHEAR_COORDS}
    weight = sp.Symbol("w", real=True, positive=True)
    swap = []
    for shape in (
        lambda x: weight,
        lambda x: weight * (-1) ** x,
        lambda x: sp.I * weight,
        lambda x: sp.I * weight * (-1) ** x,
    ):
        differential = sp.zeros(SIZE, SIZE)
        for x in range(LX):
            for p, q in crossing_hops((x,)):
                differential[p, q] = shape(x)
        a = pairing_of(differential, flat_cover, operator=THETA)
        b = pairing_of(differential, flat_cover, operator=THETA_PRIME_OP)
        swap.append(
            (
                zero(a),
                zero(b),
                None if zero(a) else congruence_inertia(
                    clean(a.xreplace({weight: 1}))
                ),
                None if zero(b) else congruence_inertia(
                    clean(b.xreplace({weight: 1}))
                ),
            )
        )
    riders = (
        all(
            sp.expand(
                cone[i, j].xreplace(flipped) + cone[i, j]
            ) == 0
            for i, j in cone_off
        ),
        all(
            sp.expand(cone[j, j].xreplace(flipped) - cone[j, j]) == 0
            for j in range(HALF)
        ),
        congruence_inertia(odd_object),
        all(odd_object[j, j] == 0 for j in range(HALF)),
        tuple(
            (i, j) for i in range(HALF) for j in range(HALF)
            if i < j and odd_object[i, j] != 0
        ),
        {sp.nsimplify(v): m for v, m in primary.eigenvals().items()},
        {sp.nsimplify(v): m for v, m in odd_object.eigenvals().items()},
        (primary.rank(), odd_object.rank()),
        tuple(swap),
    )
    exact.append(sum(odd_object))

    # ---------------------------------------------------------------- E ----
    lambda_differential = sp.zeros(SIZE, SIZE)
    for x in range(LX):
        coefficient = 1 + LAMBDA * (-1) ** x
        for p, q in crossing_hops((x,)):
            lambda_differential[p, q] = sp.expand(
                coefficient * edge[PRIMARY_EDGE][p, q]
            )
    grid = tuple(R(k, 20) for k in range(-20, 21))
    configurations = [
        ("flat", flat_cover, sp.Integer(0)),
        ("flat", flat_cover, sp.Integer(1)),
    ]
    for name, field in (
        ("ON-locus A", ON_LOCUS_A), ("ON-locus B (c*)", CSTAR),
        ("OFF-locus A", OFF_LOCUS_A), ("OFF-locus B", OFF_LOCUS_B),
    ):
        cover = b145.cover_hodge_from_field(field)
        configurations.append((name, cover, sp.Integer(0)))
        configurations.append((name, cover, sp.Integer(1)))
    family_rows = []
    for name, cover, mass in configurations[:2]:
        raw = symbolic_pairing(lambda_differential, cover, mass)
        sweep = {
            value: congruence_inertia(clean(raw.xreplace({LAMBDA: value})))
            for value in grid
        }
        psd = tuple(v for v in grid if sweep[v][2] == 0 and sweep[v][0] > 0)
        family_rows.append((name, mass, sweep, psd))
    anchor_rows = []
    for name, cover, mass in configurations:
        raw = symbolic_pairing(lambda_differential, cover, mass)
        anchors = {
            value: congruence_inertia(clean(raw.xreplace({LAMBDA: value})))
            for value in (R(-1), R(0), R(1))
        }
        anchor_rows.append(
            (
                name,
                str(mass),
                tuple(sorted(anchors.items(), key=str)),
                even_content_of_nullspace(clean(raw.xreplace({LAMBDA: 1}))),
            )
        )
    off_even = {
        "OFF-locus A": sum(
            1 for cell in EVEN_CELLS if OFF_LOCUS_A[cell][0] != 0
        ),
        "OFF-locus B": sum(
            1 for cell in EVEN_CELLS if OFF_LOCUS_B[cell][0] != 0
        ),
    }
    family = (
        zero(sp.expand(lambda_differential.xreplace({LAMBDA: 1}) - 2 * obj)),
        zero(
            sp.expand(
                lambda_differential.xreplace({LAMBDA: -1})
                - 2 * restrict(edge[PRIMARY_EDGE], ODD_SUPPORT)
            )
        ),
        zero(
            sp.expand(
                pairing_of(lambda_differential.xreplace({LAMBDA: 0}), flat_cover)
                - pairing_of(edge[PRIMARY_EDGE], flat_cover)
            )
        ),
        len(grid),
        tuple(row[3] for row in family_rows),
        all(
            row[2][value][2] > 0
            for row in family_rows for value in grid if -1 < value < 1
        ),
        all(
            dict(row[2]) == ANCHOR_INERTIA
            for row in anchor_rows if row[0] == "flat"
        ),
        all(
            dict(row[2])[R(1)]
            == (PSD_INERTIA if row[1] == "0" else MASSIVE_CURVED_INERTIA)
            for row in anchor_rows if row[0].startswith("ON-locus")
        ),
        all(
            dict(row[2])[R(1)][2] == off_even[row[0]]
            for row in anchor_rows
            if row[0].startswith("OFF-locus") and row[1] == "0"
        )
        and all(
            dict(row[2])[R(1)][2] > 0
            for row in anchor_rows if row[0].startswith("OFF-locus")
        ),
        tuple(
            row[3] for row in anchor_rows
            if row[0] in ("flat", "ON-locus A", "ON-locus B (c*)")
            and row[1] == "0"
        ),
        len(configurations),
        tuple(anchor_rows),
    )

    base = (sp.Integer(0), sp.Integer(0), shear_t_value, -shear_t_value)
    chart_rows = []
    for key in EDGE_KEYS:
        differential = restrict(edge[key], EVEN_SUPPORT)
        if zero(differential):
            continue
        flat_pairing = pairing_of(differential, flat_cover)
        curved = pairing_of(differential, cstar_cover)
        predicted = base[key[0]] - shear_t_value * (
            HEALING_WEIGHTS[key[1]] - HEALING_WEIGHTS[key[0]]
        )
        chart_rows.append(
            (
                key,
                flat_pairing[0, 0],
                predicted,
                sp.simplify(curved[0, 0] / flat_pairing[0, 0]),
                congruence_inertia(flat_pairing),
                congruence_inertia(curved),
            )
        )
    chart_law = (
        len(chart_rows),
        all(row[1] == row[2] for row in chart_rows),
        base,
        tuple(sorted({str(row[3]) for row in chart_rows})),
        sum(1 for row in chart_rows if row[5] == PSD_INERTIA),
        sum(1 for row in chart_rows if row[5] == NSD_INERTIA),
        tuple(sorted({row[4] == row[5] for row in chart_rows})),
        tuple(sorted(str(row[1]) for row in chart_rows)),
    )
    exact.append(sum(row[1] for row in chart_rows))

    # ---------------------------------------------------------------- F ----
    free_hq = b145.quotient(free_cover)
    seam = sp.Matrix(
        HALF, HALF,
        lambda i, j: sp.simplify(
            half_pairing(THETA, free_hq, COMMITTED_ROWS)[i, j]
        ),
    )
    seam_slots = tuple(
        (i, j) for i in range(HALF) for j in range(HALF)
        if i < j and seam[i, j] != 0
    )
    seam_shears = set()
    for entry in seam:
        seam_shears |= set(sp.expand(entry).free_symbols) & set(
            b145.SHEAR_COORDS
        )
    precheck = []
    for name, field in (
        ("flat", b159.flat_field()),
        ("uniform odd-t", field_of({(t, x): R(1, 3)
                                    for t in (1, 3) for x in range(LX)})),
        ("ON-locus A", ON_LOCUS_A),
        ("c*", CSTAR),
    ):
        hq = b145.quotient(b145.cover_hodge_from_field(field))
        precheck.append(
            (
                name,
                zero(sp.expand(THETA * hq * THETA - hq.H)),
                zero(sp.expand(THETA * hq * THETA + hq.H)),
            )
        )
    full = symbolic_pairing(obj, cstar_cover, MASS)
    f_zero = clean(full.xreplace({MASS: 0}))
    f_prime = clean(
        sp.Matrix(HALF, HALF, lambda i, j: sp.diff(full[i, j], MASS))
    )
    _basis, projector = null_projector(f_zero)
    pseudo = sp.diag(*[
        sp.Integer(0) if f_zero[j, j] == 0 else 1 / f_zero[j, j]
        for j in range(HALF)
    ])
    second = clean(sp.expand(-projector * f_prime * pseudo * f_prime * projector))
    mass_order = (
        seam_slots,
        tuple(sp.simplify(seam[i, j] * 8) for i, j in seam_slots),
        all((i in EVEN_SLOTS) != (j in EVEN_SLOTS) for i, j in seam_slots),
        tuple(sorted(str(s) for s in seam_shears)),
        all(seam[i, j] == 0 for i in EVEN_SLOTS for j in EVEN_SLOTS),
        all(seam[i, j] == 0 for i in ODD_SLOTS for j in ODD_SLOTS),
        tuple(precheck),
        zero(sp.expand(full - (f_zero + MASS * f_prime))),
        congruence_inertia(f_zero),
        tuple(f_zero[j, j] for j in EVEN_SLOTS),
        zero(sp.expand(projector - P_ODD)),
        zero(clean(sp.expand(projector * f_prime * projector))),
        (
            zero(sp.expand(f_zero * pseudo * f_zero - f_zero))
            and zero(sp.expand(pseudo * f_zero * pseudo - pseudo))
            and zero(sp.expand((f_zero * pseudo).H - f_zero * pseudo))
            and zero(sp.expand((pseudo * f_zero).H - pseudo * f_zero))
        ),
        congruence_inertia(second),
        tuple(sorted(
            [
                (sp.nsimplify(sp.simplify(v)), m)
                for v, m in second.eigenvals().items()
            ],
            key=str,
        )),
    )
    exact.append(sum(f_zero) + sum(f_prime))

    counterterm_operator = sp.zeros(SIZE, SIZE)
    for x in range(LX):
        for k, (target_t, source_t) in enumerate(((1, 2), (3, 4))):
            value = (
                sp.Symbol(f"ctr{x}{k}", real=True)
                + sp.I * sp.Symbol(f"cti{x}{k}", real=True)
            )
            p, q = cover_index(target_t, x), cover_index(source_t, x)
            counterterm_operator[p, q] = value
            counterterm_operator[(p + PHYS) % SIZE, (q + PHYS) % SIZE] = value
    counterterm_gram = sp.Matrix(
        HALF, HALF,
        lambda i, j: sp.simplify(
            half_pairing(
                THETA,
                b145.quotient_action(
                    counterterm_operator, free_cover, sp.Integer(0)
                ),
                COMMITTED_ROWS,
            )[i, j]
        ),
    )
    odd_odd = tuple(
        (i, j) for i in ODD_SLOTS for j in ODD_SLOTS
        if i < j and counterterm_gram[i, j] != 0
    )
    even_odd = tuple(
        (i, j) for i in EVEN_SLOTS for j in ODD_SLOTS
        if counterterm_gram[i, j] != 0
    )
    counterterm = (
        len(counterterm_operator.free_symbols),
        odd_odd,
        all(counterterm_gram[i, i] == 0 for i in ODD_SLOTS),
        tuple(sorted(even_odd)),
        set(even_odd).isdisjoint(set(seam_slots)),
        # the checker's SOUND route, replacing the primary's zero-row shortcut:
        # F' itself has no odd-odd entry anywhere, so P_0 (F' + G) P_0 = 0 is
        # exactly the vanishing of G's own hollow odd-odd block, and then PSD at
        # second order forces C = 0 and with it the even-odd block.
        all(f_prime[i, j] == 0 for i in ODD_SLOTS for j in ODD_SLOTS),
    )

    scaling_rows = []
    for amplitude in SCALING_AMPLITUDES:
        field = field_of({
            (1, 0): amplitude * R(1, 3), (1, 2): -amplitude * R(1, 3),
            (3, 0): amplitude * R(1, 3), (3, 2): -amplitude * R(1, 3),
        })
        pairing = pairing_of(
            obj, b145.cover_hodge_from_field(field), sp.Integer(1)
        )
        scaling_rows.append((amplitude, congruence_inertia(pairing), pairing))
    enclosures = tuple(
        most_negative_enclosure(row[2], window)
        for row, window in zip(scaling_rows, SCALING_ENCLOSURES)
    )
    windows = (
        ratio_window(SCALING_ENCLOSURES[0], SCALING_ENCLOSURES[1]),
        ratio_window(SCALING_ENCLOSURES[1], SCALING_ENCLOSURES[2]),
    )
    scaling = (
        tuple(str(row[0]) for row in scaling_rows),
        tuple(row[1] for row in scaling_rows),
        enclosures,
        windows,
        tuple(
            lo <= windows[k][0] and windows[k][1] <= hi
            for k, (lo, hi) in enumerate(SCALING_RATIO_WINDOWS)
        ),
    )

    # ---------------------------------------------------------------- G ----
    real_weights = sp.symbols("Lw0:4", real=True)
    real_edges = b145.edge_differentials(differentials, star, real_weights)
    prime_real_zero = sum(
        1 for key in EDGE_KEYS
        if zero(pairing_of(
            sp.expand(real_edges[key]), flat_cover, operator=THETA_PRIME_OP
        ))
    )
    theta_real_zero = sum(
        1 for key in EDGE_KEYS
        if zero(pairing_of(sp.expand(real_edges[key]), flat_cover))
    )
    reference = sp.expand(real_edges[PROBE_EDGE])
    crossing_weight = tuple(
        sp.simplify(reference[cover_index(1, x), cover_index(2, x)])
        for x in range(LX)
    )
    complex_weights = tuple(
        sp.Symbol(f"Uw{k}", real=True) + sp.I * sp.Symbol(f"Vw{k}", real=True)
        for k in range(4)
    )
    complex_edges = b145.edge_differentials(
        differentials, star, complex_weights
    )
    prime_complex_zero = tuple(
        sorted(
            key for key in EDGE_KEYS
            if zero(pairing_of(
                sp.expand(complex_edges[key]), flat_cover,
                operator=THETA_PRIME_OP,
            ))
        )
    )
    curved_zero, curved_live_zero = 0, 0
    for key in EDGE_KEYS:
        pairing = pairing_of(
            sp.expand(real_edges[key]), free_cover, operator=THETA_PRIME_OP
        )
        curved_zero += 1 if zero(pairing) else 0
        curved_live_zero += 1 if zero(sub_block(pairing, LIVE, LIVE)) else 0
    volume = {
        (t, x): sp.Symbol(f"nu_{t}{x}", positive=True)
        for t in range(4) for x in range(LX)
    }
    free_volume_cover = b145.cover_hodge_from_field(
        {cell: (sp.Integer(0), volume[cell]) for cell in volume}
    )
    free_volume_zero = tuple(
        sorted(
            key for key in EDGE_KEYS
            if zero(pairing_of(
                sp.expand(real_edges[key]), free_volume_cover,
                operator=THETA_PRIME_OP,
            ))
        )
    )
    uniform = tuple(
        sum(
            1 for key in EDGE_KEYS
            if zero(pairing_of(
                sp.expand(real_edges[key]),
                b145.cover_hodge_from_field(
                    {cell: (sp.Integer(0), value) for cell in volume}
                ),
                operator=THETA_PRIME_OP,
            ))
        )
        for value in UNIFORM_VOLUMES
    )
    revivals = sum(
        1 for cell in volume
        if not zero(pairing_of(
            sp.expand(real_edges[PROBE_EDGE]),
            b145.cover_hodge_from_field({
                other: (R(1, 3) if other == cell else sp.Integer(0),
                        sp.Integer(1))
                for other in volume
            }),
            operator=THETA_PRIME_OP,
        ))
    )
    tied, tied_symbols, representative = b160.tied_family(
        edge[PROBE_EDGE], "w"
    )
    tied_parameters = sorted(tied.free_symbols, key=str)
    locus_ranks = []
    for operator in (THETA_PRIME_OP, THETA):
        pairing = half_pairing(
            operator,
            b145.quotient_action(tied, flat_cover, sp.Integer(0)),
            COMMITTED_ROWS,
        )
        equations = []
        for i in range(HALF):
            for j in range(HALF):
                entry = sp.expand(pairing[i, j])
                if entry != 0:
                    equations.extend([sp.re(entry), sp.im(entry)])
        system, _rhs = sp.linear_eq_to_matrix(
            [sp.expand(e) for e in equations if sp.expand(e) != 0],
            tied_parameters,
        )
        locus_ranks.append(system.rank())
    image_coordinates = []
    symbolic_probe = sp.expand(real_edges[PROBE_EDGE])
    for _key, (_index, (p, q)) in sorted(
        representative.items(), key=lambda kv: kv[1][0]
    ):
        value = sp.expand(symbolic_probe[p, q])
        image_coordinates.extend([sp.re(value), sp.im(value)])
    family_parameters = [SHEAR_X, SHEAR_T] + list(real_weights)
    jacobian = sp.Matrix(
        [[sp.diff(c, p) for p in family_parameters] for c in image_coordinates]
    )
    blindness = (
        prime_real_zero,
        theta_real_zero,
        crossing_weight,
        all(
            sp.simplify(crossing_weight[x] + crossing_weight[(x + 1) % LX]) == 0
            for x in range(LX)
        ),
        prime_complex_zero,
        len(prime_complex_zero),
        curved_zero,
        curved_live_zero,
        free_volume_zero,
        uniform,
        revivals,
        len(tied_symbols),
        len(tied_parameters),
        tuple(locus_ranks),
        jacobian.rank(),
        len(family_parameters),
        len(image_coordinates),
    )
    exact.append(sum(crossing_weight))

    l147 = locus_rows(b156.INVOLUTION_PAIRS_R)
    odd_x_pairs = tuple(
        pair for pair in b156.INVOLUTION_PAIRS_S
        if all(str(b156.ODD[k])[3] in "13" for k in pair)
    )
    l154 = locus_rows(odd_x_pairs)
    meet = sp.Matrix.vstack(l147, l154)
    witness_moments = odd_moment_vector(BALANCED)
    balanced_cover = b145.cover_hodge_from_field(BALANCED)
    witness_full = symbolic_pairing(obj, balanced_cover, MASS)
    theta_mass = clean(
        half_pairing(THETA, b145.quotient(balanced_cover), COMMITTED_ROWS)
    )
    prime_mass = clean(
        half_pairing(
            THETA_PRIME_OP, b145.quotient(balanced_cover), COMMITTED_ROWS
        )
    )
    stratum = (
        kernel_dimension(l147),
        b156.L147_DIM,
        kernel_dimension(l154),
        b156.L154_DIM,
        kernel_dimension(meet),
        b156.MEET_DIM,
        witness_moments,
        zero(l147 * sp.Matrix(witness_moments)),
        zero(l154 * sp.Matrix(witness_moments)),
        all(v != 0 for v in witness_moments),
        tuple(sorted({abs(v) for v in witness_moments})),
        zero(theta_mass),
        congruence_inertia(prime_mass),
        congruence_inertia(sub_block(prime_mass, LIVE, LIVE)),
        zero(sp.diff(witness_full, MASS)),
        witness_full.xreplace({MASS: 0}) == sp.diag(
            *[WITNESS_DIAGONAL if j in EVEN_SLOTS else 0 for j in range(HALF)]
        ),
        congruence_inertia(clean(witness_full.xreplace({MASS: 0}))),
        tuple(
            congruence_inertia(pairing_of(obj, balanced_cover, m))
            for m in (sp.Integer(0), R(1, 10), sp.Integer(1), sp.Integer(5))
        ),
        b145.in_admissible_cone(BALANCED),
        sum(1 for cell in BALANCED if BALANCED[cell][0] != 0),
        all(BALANCED[cell][0] == 0 for cell in EVEN_CELLS),
        not balanced_cover.is_diagonal(),
        b145.quotient(balanced_cover) != sp.eye(PHYS),
        not zero(
            half_pairing(
                THETA, b145.quotient(balanced_cover), PRESERVING_ROWS
            )
        ),
        BALANCE_EQUATIONS + PSD_EQUATIONS,
        set(str(s) for s in b145.ODD_SHEAR_COORDS).isdisjoint(
            set(str(s) for s in B_EVEN)
        ),
        CONE_COORDINATES,
    )
    exact.append(sum(witness_moments) + sum(witness_full.xreplace({MASS: 0})))

    # -------------------------------------------------------------- deep ---
    deep_family = None
    deep_generators = None
    if deep:
        rows = []
        for name, cover, mass in configurations:
            raw = symbolic_pairing(lambda_differential, cover, mass)
            sweep = {}
            agree = True
            for value in grid:
                point = clean(raw.xreplace({LAMBDA: value}))
                first = congruence_inertia(point)
                second_route = sturm_inertia(point)
                agree = agree and first == second_route
                sweep[value] = first
            psd = tuple(v for v in grid if sweep[v][2] == 0 and sweep[v][0] > 0)
            rows.append((name, str(mass), psd, agree))
        deep_family = (
            len(rows),
            len(grid),
            tuple(row[2] for row in rows),
            all(row[3] for row in rows),
            all(
                set(row[2]) <= {R(1)} for row in rows
            ),
        )

        classes = {}
        for p in range(SIZE):
            for q in range(SIZE):
                classes.setdefault(b160.antiperiodic_key(p, q), []).append(
                    (p, q)
                )

        order = sorted(classes)
        generic = sp.zeros(SIZE, SIZE)
        symbols = {}
        for index, key in enumerate(order):
            value = (
                sp.Symbol(f"gu{index}", real=True)
                + sp.I * sp.Symbol(f"gv{index}", real=True)
            )
            symbols[key] = value
            for p, q in classes[key]:
                generic[p, q] = value
        pairing = half_pairing(
            THETA,
            b145.quotient_action(generic, flat_cover, sp.Integer(0)),
            COMMITTED_ROWS,
        )
        names = set()
        for i, j in MASS_SLOTS:
            names |= sp.expand(pairing[i, j]).free_symbols
        reaching = {s for s in names if str(s)[:2] in ("gu", "gv")}
        reaching_indices = {int(str(s)[2:]) for s in reaching}
        explicit = set()
        for index in sorted(reaching_indices):
            single = sp.zeros(SIZE, SIZE)
            for p, q in classes[order[index]]:
                single[p, q] = sp.Integer(1)
            planted = half_pairing(
                THETA,
                b145.quotient_action(single, flat_cover, sp.Integer(0)),
                COMMITTED_ROWS,
            )
            if any(sp.expand(planted[i, j]) != 0 for i, j in MASS_SLOTS):
                explicit.add(index)
        displacement_census = collections.Counter()
        hops = []
        for index in reaching_indices:
            for p, q in classes[order[index]]:
                displacement_census[b160.displacement(SIZE * p + q)] += 1
                hops.append(SIZE * p + q)
        probe_support = {
            SIZE * p + q
            for p in range(SIZE) for q in range(SIZE)
            if edge[PROBE_EDGE][p, q] != 0
        }
        # the same reading on the GENERAL 64-modulus carrier, where a further
        # dt-EVEN family reaches: still uncommitted, still off the probe support
        curved_pairing = half_pairing(
            THETA,
            b145.quotient_action(generic, free_cover, sp.Integer(0)),
            COMMITTED_ROWS,
        )
        curved_names = set()
        for i, j in MASS_SLOTS:
            curved_names |= sp.expand(curved_pairing[i, j]).free_symbols
        curved_indices = {
            int(str(s)[2:]) for s in curved_names if str(s)[:2] in ("gu", "gv")
        }
        curved_census = collections.Counter()
        curved_hops = []
        for index in curved_indices - reaching_indices:
            for p, q in classes[order[index]]:
                curved_census[b160.displacement(SIZE * p + q)] += 1
                curved_hops.append(SIZE * p + q)
        deep_generators = (
            len(order),
            2 * len(order),
            len(reaching),
            len(reaching_indices),
            len(hops),
            tuple(sorted(displacement_census)),
            explicit == reaching_indices,
            len(probe_support),
            len(probe_support & set(hops)),
            tuple(sorted(
                set(displacement_census) & set(COMMITTED_DISPLACEMENTS)
            )),
            tuple(sorted(curved_census)),
            len(curved_hops),
            len(probe_support & set(curved_hops)),
            tuple(sorted(
                set(curved_census) & set(COMMITTED_DISPLACEMENTS)
            )),
        )

    exact_no_float = all(no_float(value) for value in exact)

    return Facts(
        main_head=main_head,
        authority=authority,
        calibration=calibration,
        decoupling=decoupling,
        factorization=factorization,
        content=content,
        holonomy=holonomy,
        orbit=orbit,
        riders=riders,
        family=family,
        chart_law=chart_law,
        mass_order=mass_order,
        counterterm=counterterm,
        scaling=scaling,
        blindness=blindness,
        stratum=stratum,
        deep_family=deep_family,
        deep_generators=deep_generators,
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
    "pre_registered_branches",
    "panel_provenance",
    "door_reading_dead",
    "positivity_by_decoupling",
    "nulls_odd_x",
    "odd_x_rows_zero",
    "decoupling_locus",
    "pullback_factorization",
    "s_t_linear",
    "s_x_blind",
    "zero_holonomy_derivative",
    "four_of_eight_hops",
    "adams_refuted",
    "lambda_one_only",
    "t6_downgraded",
    "scalar_law",
    "kill_rests_on_t1",
    "theta_prime_refuted_as_stated",
    "any_weights_quoted",
    "reality_condition",
    "hodge_proportional_identity",
    "complex_counterexample",
    "committed_scope_honest",
    "codim_eight_exact",
    "understates_struck",
    "image_rank_three",
    "corpus_scopes_stand",
    "l147_verbatim",
    "dim_two_intersection",
    "not_dead_carrier",
    "no_b156_contradiction",
    "theta_prime_scoped_kill",
    "b156_narrowing",
    "dead_carrier_quote",
    "positivity_qualifier",
    "mass_independent",
    "dfdm_zero",
    "codim_eight_arithmetic",
    "counterterm_empty",
    "counterterm_strengthened",
    "uncommitted_classes",
    "b_zero_structural",
    "second_order_negative",
    "curvature_squared",
    "inside_kernel",
    "precheck_neither",
    "carrier_side_open",
    "stabilizer_order_eight",
    "census_identical",
    "flip_invariant",
    "odd_x_conjugate",
    "spectra_argument",
    "role_swap",
    "taste_structure",
    "survivors",
    "killed",
    "block_162",
    "site_reflection_lead",
    "pool_two",
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
        "pre_registered_branches": "pre-registered" in note,
        "panel_provenance": "panel" in note,
        # --- the verdict against the pre-registered branches ------------------
        "door_reading_dead": "the door reading is dead" in note,
        "positivity_by_decoupling": "positivity by decoupling" in note,
        "nulls_odd_x": "24" in note and "odd-x" in note,
        "odd_x_rows_zero": "row occupancy" in note,
        "decoupling_locus": "parity-decoupling locus" in note,
        "pullback_factorization": "a^t a" in note and "pullback" in note,
        "s_t_linear": "linearly" in note or "linear in" in note,
        "s_x_blind": "s_x-blind" in note,
        "zero_holonomy_derivative": "holonomy" in note
        and "o(alpha^2)" in compact,
        "four_of_eight_hops": "4 of the 8" in note,
        "adams_refuted": "adams" in note and "refuted" in note,
        "lambda_one_only": "lambda = 1" in note,
        "t6_downgraded": "downgraded" in note,
        "scalar_law": "base(i) - s_t" in note,
        "kill_rests_on_t1": "rests on t1" in note,
        # --- the theta-prime blindness theorem at its true scope --------------
        "theta_prime_refuted_as_stated": "refuted as stated" in note,
        "any_weights_quoted": "any shears and any healing weights" in note,
        "reality_condition": "im(lambda_j - lambda_i) = 0" in note,
        "hodge_proportional_identity": "proportional to the identity" in note,
        "complex_counterexample": "12 of 16" in note or "12/16" in note,
        "committed_scope_honest": "committed configuration" in note,
        "codim_eight_exact": "codimension 8" in note,
        "understates_struck": "understates" in note and "struck" in note,
        "image_rank_three": "rank 3" in note,
        "corpus_scopes_stand": "own carrier scopes" in note,
        # --- the mass-survival stratum and the Block 156 narrowing ------------
        "l147_verbatim": "l147" in note and "verbatim" in note,
        "dim_two_intersection": "dimension 2" in note,
        "not_dead_carrier": "not the dead carrier" in note,
        "no_b156_contradiction": "no contradiction" in note,
        "theta_prime_scoped_kill": "theta-prime-scoped" in note,
        "b156_narrowing": "narrowing" in note,
        "dead_carrier_quote": (
            "the three loci pairwise meet only at the dead carrier" in note
        ),
        "positivity_qualifier": "positivity qualifier" in note,
        "mass_independent": "mass-independent" in note,
        "dfdm_zero": "df/dm = 0" in note,
        "codim_eight_arithmetic": "codimension 8" in note
        and "32-coordinate" in note,
        "counterterm_empty": "counterterm" in note and "empty" in note,
        "counterterm_strengthened": "strengthened" in note,
        "uncommitted_classes": "(1,3)" in compact and "(5,3)" in compact,
        "b_zero_structural": "structurally" in note,
        "second_order_negative": "second order" in note,
        "curvature_squared": "quadratic" in note,
        "inside_kernel": "ker f(0)" in note,
        "precheck_neither": "neither even nor odd" in note,
        "carrier_side_open": "carrier-side open" in note,
        # --- what survives ----------------------------------------------------
        "stabilizer_order_eight": "order-8" in note,
        "census_identical": "(4,4,0): 8" in compact
        or "(4,4,0):8" in compact,
        "flip_invariant": "flip" in note,
        "odd_x_conjugate": "hollow" in note,
        "spectra_argument": "spectra" in note or "spectrum" in note,
        "role_swap": "swap" in note,
        "taste_structure": "taste" in note,
        "survivors": "what survives" in note,
        "killed": "killed" in note,
        "block_162": "block 162" in note,
        "site_reflection_lead": "site-reflection" in note,
        "pool_two": "pool 2" in note,
        # --- discipline and disclosures --------------------------------------
        "checker_credit": "checker" in note,
        "quoted_then_corrected": "quoted" in note,
        "common_mode": "common-mode" in note,
        "cross_context": "cross-context" in note,
        "not_re_verified": "not re-verified" in note,
        "sample_not_cone_wide": "not a cone-wide" in note or "sample" in note,
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
        # NEGATIVE key.  A block whose headline is a KILL must not be written up
        # as any kind of priority or originality claim; the gate greps the
        # NORMALIZED note, so the banned wording may not appear anywhere, not
        # even inside a prohibition list, and the note describes it instead of
        # spelling it.
        "no_priority_claim": (
            "first positive" not in note
            and "novel" not in note
            and "unprecedented" not in note
        ),
        # The LaTeX rho guard: a line-wrapped \rho leaves a stray "ho_" at the
        # start of a line and silently mangles a modulus name.
        "rho_guard": "\nho_" not in note_text,
    }


N5_FENCE = 'N5: per_element: THE DOOR READING IS DEAD, AND T1 KILLED IT EXACTLY AS THREE OF THE FIVE LENSES PREDICTED: POSITIVITY BY DECOUPLING. On all six PSD edges ker F(0) is 4-dimensional and all 24 null vectors are EXACTLY odd-x -- ||P_odd v||^2 = 1 and ||P_even v||^2 = 0 as exact rationals, not sampled; the odd-x rows of the 8x16 block [theta K]_++ vanish identically at row occupancy (1,0,1,0,1,0,1,0); the residue K has no nonzero entry in any odd-x row or column of the whole 16x16; and on the cone every off-diagonal -- (0,7) = b_20/10, (1,4) = b_00/10, (2,5) = b_22/10, (3,6) = b_02/10 -- joins an even-x slot to an odd-x slot against a ZERO diagonal, so THE CODIMENSION-4 PSD LOCUS IS THE PARITY-DECOUPLING LOCUS. THE SHARPEST PHRASING IS LITERALLY TRUE, AND IT IS THE CHECKER\'S VERIFICATION: P = A^T A with A = sqrt(4/5) P_even, an exact matrix identity, so the form is the PULLBACK of a positive definite form on the even-x quotient; on the curved carrier c* it is still Pe^T diag(257/240, 229/210, 31/30, 79/75) Pe.\nper_site: T2 SPLITS AND T4 REFUTES. T2: with both shears symbolic the flat pairing is diag(s_t, 0, s_t, 0, s_t, 0, s_t, 0) -- carrying s_t LINEARLY and vanishing iff s_t = 0, so NOT the fully connection-blind Block 154 class -- but it is completely s_x-BLIND, its first-order holonomy response is ZERO (dressed spectrum {(4/5)cos(alpha) x4, 0 x4}, every eigenvalue derivative 0 at alpha = 0, motion O(alpha^2)), a spatial dressing that makes two plaquettes nontrivial leaves differential, residue and pairing COMPLETELY UNCHANGED at every order, and only 4 of the 8 supported cover hops feed the {p=0,1} pairing at all. T4: over the 41-point lambda grid the ONLY PSD-and-live point is lambda = 1 exactly, the three pre-registered anchors reproduce ((4,4,0) at lambda = 1, (2,4,2) at -1, (6,0,2) at 0), and the nulls at lambda = 1 have even-x content EXACTLY 0 -- THE ADAMS-STYLE FLAVORED-COEFFICIENT READING IS REFUTED.\nper_mode: T6 AT ITS CORRECTED SCOPE, AND THE CORRECTION IS THE CHECKER\'S DOWNGRADE. The measurement stands: on the same carrier c*, with the carrier and all four locus coordinates untouched (b_even map = I), 6 of the 12 live committed edges give (4,4,0) and 6 give (0,4,4). The primary read this as CHART DEPENDENCE in the Block 154 sense and that reading is DOWNGRADED, because the split obeys EXACTLY value(i,j) = base(i) - s_t (lambda_j - lambda_i) with base = (0, 0, +s_t, -s_t) and s_t = 4/5, verified on all twelve live edges, and at c* every one of the twelve scalars is the flat value times ONE common positive constant 257/192. What reverses is the sign of a HEALING-WEIGHT-DEPENDENT SCALAR multiplying a fixed rank-4 pullback, not a chart-dependent signature. THE KILL RESTS ON T1 AND NEVER ON T6.\nper_block: THE THETA-PRIME BLINDNESS THEOREM AT ITS TRUE SCOPE, AND THE HEADLINE IS REFUTED AS STATED. The primary claimed an "identically zero exchange pairing on all 16 edges for ANY shears and ANY healing weights"; the checker refuted it, and the exact annihilation condition is Im(lambda_j - lambda_i) = 0 -- the REALITY of the healing-weight differences -- TOGETHER WITH a cover Hodge proportional to the identity. With complex weights theta-prime is NONZERO on 12 of 16 edges; on the general 64-modulus carrier NONZERO on 16 of 16, though its live-live block is still zero on 16 of 16 so Block 159\'s W1 core is intact; at zero shear with 16 free per-cell volumes it is zero on only 2 of 16, and every one of the 16 single-cell shear perturbations revives it. THE HONEST STATEMENT: the COMMITTED configuration -- real weight-differences on identity-Hodge flat carriers -- sits INSIDE theta-prime\'s annihilation set, so the committed family was theta-prime-blind in the CONNECTION channel at exactly that scope. Block 160\'s codimension-8-of-48 framing was EXACT at its own quantifier scope (both loci rank 8 of 48; the committed family\'s image there is a rank 3 variety, not a 6-parameter one), the word "understates" is STRUCK, and the landed corpus statements stand at their own carrier scopes.\nlattice_wide: THE MASS-SURVIVAL SUB-LOCUS STANDS, SHARPENED, AND IT IS BLOCK 147\'S ANNEALED LOCUS. The carrier-side balance b_10+b_13 = b_11+b_12 = b_30+b_33 = b_31+b_32 = 0 IS L147 = ker(R+1) VERBATIM; the witness carrier sits in the DIMENSION-2 intersection L147 cap L154 and is NOT the dead carrier, all eight odd moments being +-3/8. NO CONTRADICTION WITH BLOCK 156: its transversality kill is THETA-PRIME-SCOPED, and at this very carrier theta\'s mass Gram is identically ZERO while theta-prime\'s is (2,4,2) with live-live (2,0,2), so Block 156\'s kill fires untouched. THE BLOCK 156 NARROWING, WHICH THIS NOTE CARRIES: the landed sentence "The three loci pairwise meet only at the dead carrier" is FALSE as a bare subspace statement, since L147 cap L154 has dimension 2, and TRUE only with its own positivity qualifier attached; it is narrowed accordingly and the landed note is not edited. The all-mass positivity is proved SYMBOLICALLY: dF/dm = 0 IDENTICALLY, the pairing is diag(33/40, 0, 33/40, 0, 33/40, 0, 33/40, 0), MASS-INDEPENDENT, inertia (4,4,0) at every m; and the codimension-8 arithmetic is exact -- 4 balance equations on the odd-time shears plus 4 PSD equations on the even-time even-x cells, on DISJOINT coordinates of the 32-coordinate cone.\nRESULT: THE MASS NO-GO\'S FINAL SHAPE IS BETWEEN THE TWO PRE-REGISTERED EXTREMES, AT FULL PRECISION. B = P_0 F\'(0) P_0 = 0 STRUCTURALLY: the seam insertion herm([theta H_q]_++) is purely even-x-to-odd-x at the four slots (0,3) = (b_30+b_33)/8, (1,2) = (b_31+b_32)/8, (4,5) = -(b_10+b_13)/8, (6,7) = -(b_11+b_12)/8, fed exclusively by the eight odd-TIME shears with EMPTY even-even and odd-odd blocks, and ker F(0) is exactly the odd-x span -- so the FIRST-ORDER reflection-odd no-go DOES NOT FIRE. Second order: C = -P_0 F\' F(0)^+ F\' P_0 at inertia (0,4,4) with exact eigenvalues {-375/51296, -1215/263168, -1215/253952, -507/1294336}, the negative directions lying 99.9%+ inside ker F(0), and the negatives scaling QUADRATICALLY with the curvature -- three shear amplitudes give most-negative eigenvalues in successive ratios 4.77225... and 4.17099..., converging to 4. The pre-check theta H_q theta against H_q-dagger is NEITHER EVEN NOR ODD on a generic admissible carrier, so it does not decide the order by itself. THE OPERATOR-SIDE EMPTINESS STANDS AND IS STRENGTHENED BY THE CHECKER\'S SWEEP: the mass-channel slots are reachable only from displacement classes {(1,3), (3,1), (5,3), (7,1)}, none of them a committed class and none inside the probe edge\'s own 48-hop support. No first-order fire, second-order negative, OPERATOR-SIDE EMPTY, CARRIER-SIDE OPEN.\nDECISION_CUT: BANK THE KILL MECHANISM AND THE MASS-SURVIVAL STRATUM; THE DOOR IS CLOSED. KILLED: the door reading (positivity by decoupling), the Adams-style flavored-coefficient derivation, and the covariant/ADM constraint reading. SURVIVING: the staggered/taste structure -- an honest order-8 stabilizer (even-t x even-x), census {(4,4,0): 8, (2,4,2): 8, (0,8,0): 16} identical on the flat carrier and at c*, closure verified, the locus exactly FLIP-invariant, the odd-x conjugate HOLLOW at (2,4,2) and NOT unitarily related to the even-x form (spectra {4/5 x4, 0 x4} against {4/5 x2, 0 x4, -4/5 x2} at equal rank 4 -- the primary\'s inertia-only argument is REPLACED, while Sylvester still gives non-congruence), and the real/imaginary staggering swapping theta and theta-prime EXACTLY; the theta-prime blindness at COMMITTED scope; and the MASS-INDEPENDENT PSD carrier on L147 cap L154, which resurrects the annealed locus as the mass-survival stratum. NOTHING is registered, adopted or proposed; theta is NOT re-adopted; theta-prime is NOT adopted; Block 145\'s verdict is NOT retired; no landed note is edited. NEXT: the mass-survival stratum characterization (Block 162, scout discipline); the site-reflection mass-channel scout; the pool-2 handoff items.\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero.'


# ---------------------------------------------------------------------------
# claims: the only thing a mutation is allowed to touch
# ---------------------------------------------------------------------------
def build_claims(mutation: str) -> dict:
    claims: dict = {
        "main_head": CURRENT_MAIN,
        "parent_pin": "resolved",
        "nulls_are_odd_x": True,
        "pullback_identity": True,
        "shear_content": ("s_t",),
        "stabilizer_order": STABILIZER_ORDER,
        "psd_lambda_sets": ((R(1),), (R(1),)),
        "chart_law_holds": True,
        "counterterm_disjoint": True,
        "theta_prime_complex_zero": THETA_PRIME_COMPLEX_ZERO,
        "theta_mass_gram_dead": True,
        "mass_derivative_zero": True,
        "required_scope_keys": SCOPE_KEYS,
    }
    if mutation == "stale_main_authority":
        claims["main_head"] = STALE_MAIN
    elif mutation == "stale_parent_authority":
        claims["parent_pin"] = "stale"
    elif mutation == "claim_nulls_balanced":
        # T1's kill denied at its sharpest clause: the nulls asserted to carry
        # even-x content, which is the SURVIVES branch of the pre-registered
        # projection test
        claims["nulls_are_odd_x"] = False
    elif mutation == "break_factorization":
        # the checker's literal verification denied: P asserted NOT to be A^T A
        claims["pullback_identity"] = False
    elif mutation == "claim_sx_dependence":
        # T2's blindness denied: the spatial shear asserted to appear in the
        # form, which would make the object connection-carrying in both
        # directions rather than s_t-only
        claims["shear_content"] = ("s_t", "s_x")
    elif mutation == "break_stabilizer":
        # the taste reading's load-bearing number: the stabilizer asserted to be
        # the full translation group, which would make the object fully
        # invariant rather than a coset structure
        claims["stabilizer_order"] = TRANSLATION_GROUP
    elif mutation == "claim_adams_onset":
        # the REFUTED Adams reading asserted: a PSD onset strictly below
        # lambda = 1, which is exactly the branch the 41-point grid closed
        claims["psd_lambda_sets"] = ((R(1, 2), R(1)), (R(1, 2), R(1)))
    elif mutation == "claim_chart_dependence":
        # the DOWNGRADED reading asserted: the 6/12 split held NOT to follow the
        # healing-weight scalar law, i.e. left as chart dependence
        claims["chart_law_holds"] = False
    elif mutation == "break_counterterm_reach":
        # the operator-side emptiness denied: the crossing-block counterterm's
        # even-odd support asserted to meet the mass channel's
        claims["counterterm_disjoint"] = False
    elif mutation == "claim_theta_prime_universal":
        # THE REFUTED HEADLINE, asserted: theta-prime annihilating on all 16
        # edges for ANY healing weights, which the complex-weight counterexample
        # kills
        claims["theta_prime_complex_zero"] = EDGE_COUNT
    elif mutation == "claim_locus_contradicts_b156":
        # the Block 156 resolution denied: theta's mass Gram at the witness
        # asserted NONZERO, which is what a genuine contradiction with Block
        # 156's transversality kill would require
        claims["theta_mass_gram_dead"] = False
    elif mutation == "break_mass_independence":
        # the symbolic all-mass result denied: dF/dm asserted nonzero, which
        # would reduce the stratum to a four-point sample
        claims["mass_derivative_zero"] = False
    elif mutation == "drop_b156_narrowing":
        # the correction-in-successor duty dropped from the note's scope
        claims["required_scope_keys"] = tuple(
            key
            for key in SCOPE_KEYS
            if key
            not in (
                "b156_narrowing",
                "dead_carrier_quote",
                "positivity_qualifier",
                "no_b156_contradiction",
                "theta_prime_scoped_kill",
            )
        )
    elif mutation == "drop_survivors":
        # the survivor/killed ledger dropped from the note's scope
        claims["required_scope_keys"] = tuple(
            key
            for key in SCOPE_KEYS
            if key
            not in ("survivors", "killed", "taste_structure", "block_162")
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
            "docs/ADMISSIBILITY_DIRAC_KAHLER_VALIDATION_BATTERY_BOUNDED_THEOREM_NOTE_2026-08-20.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_EXCHANGE_CONDITION_CONTRACT_BOUNDED_THEOREM_NOTE_2026-08-20.md",
            "scripts/admissibility_dirac_kahler_exchange_condition_contract_2026_08_20.py",
        )
        and PARENT_ARTIFACTS == (BLOCK160_NOTE, BLOCK160_RUNNER)
        and len(PARENT_ARTIFACT_BLOBS) == len(PARENT_ARTIFACTS) == 2
        and facts.main_head == claims["main_head"]
        and authority.fixed_authority
        and authority.parent_pin_is_commit
        and authority.parent_ref_and_ancestry
        and parent_blobs_ok
    )

    gate_b = bool(
        facts.calibration
        == (
            True,
            True,
            True,
            "EXCH",
            PSD_EDGES,
            NSD_EDGE_COUNT,
            EMPTY_EDGE_COUNT,
            True,
            NULL_DIMENSION,
            PSD_INERTIA,
            True,
            PROBE_SUPPORT,
        )
        and facts.decoupling
        == (
            (NULL_DIMENSION,) * PSD_EDGE_COUNT,
            NULL_VECTORS,
            claims["nulls_are_odd_x"],
            ROW_OCCUPANCY,
            True,
            True,
            CONE_OFF_DIAGONAL,
            True,
            tuple(sorted(str(s) for s in B_EVEN)),
            (
                b145.B_MODULUS[(2, 0)], b145.B_MODULUS[(0, 0)],
                b145.B_MODULUS[(2, 2)], b145.B_MODULUS[(0, 2)],
            ),
        )
        and facts.factorization
        == (
            True,
            claims["pullback_identity"],
            True,
            True,
            CSTAR_CORE,
            True,
            True,
        )
        and facts.exact_no_float
    )

    gate_c = bool(
        facts.content
        == (
            claims["shear_content"],
            True,
            True,
            False,
        )
        and facts.holonomy
        == (
            True,
            True,
            PSD_INERTIA,
            DEAD_INERTIA,
            NSD_INERTIA,
            FEEDING_HOPS,
            (5, 7),
            DIPOLE_PLAQUETTES,
            True,
            (
                (GAUGE_PLAQUETTES, PSD_INERTIA, False),
                (GAUGE_PLAQUETTES, PSD_INERTIA, False),
            ),
        )
        and facts.exact_no_float
    )

    gate_d = bool(
        facts.orbit
        == (
            TRANSLATION_GROUP,
            ORBIT_CENSUS,
            ORBIT_CENSUS,
            STABILIZER_SHIFTS,
            claims["stabilizer_order"],
            True,
            True,
            True,
            (1,),
            ORBIT_CENSUS[DEAD_INERTIA],
            True,
            STABILIZER_SHIFTS,
        )
        and facts.riders
        == (
            True,
            True,
            ODD_X_INERTIA,
            True,
            ODD_X_OFF_DIAGONAL,
            EVEN_X_SPECTRUM,
            ODD_X_SPECTRUM,
            (NULL_DIMENSION, NULL_DIMENSION),
            (
                (True, True, None, None),
                (True, False, None, MASSIVE_CURVED_INERTIA),
                (False, False, (2, 0, 6), MASSIVE_CURVED_INERTIA),
                (False, True, (2, 0, 6), None),
            ),
        )
        and facts.riders[5] != facts.riders[6]
        and facts.exact_no_float
    )

    gate_e = bool(
        facts.family
        == (
            True,
            True,
            True,
            GRID_POINTS,
            claims["psd_lambda_sets"],
            True,
            True,
            True,
            True,
            ((NULL_DIMENSION, sp.Integer(0)),) * 3,
            DEEP_CONFIGURATIONS,
            facts.family[11],
        )
        and facts.chart_law
        == (
            LIVE_EDGES,
            claims["chart_law_holds"],
            (
                sp.Integer(0), sp.Integer(0),
                ATLAS[SHEAR_T], -ATLAS[SHEAR_T],
            ),
            (str(CHART_SCALE),),
            CHART_POSITIVE,
            CHART_NEGATIVE,
            (True,),
            facts.chart_law[7],
        )
        and facts.exact_no_float
    )

    deep_family_ok = facts.deep_family is None or (
        facts.deep_family
        == (
            DEEP_CONFIGURATIONS,
            GRID_POINTS,
            facts.deep_family[2],
            True,
            True,
        )
    )
    deep_generators_ok = facts.deep_generators is None or (
        facts.deep_generators
        == (
            TIED_GENERATOR_CLASSES,
            TIED_REAL_GENERATORS,
            MASS_REACHING_GENERATORS,
            MASS_REACHING_CLASSES,
            MASS_REACHING_HOPS,
            MASS_REACHING_DISPLACEMENTS,
            True,
            PROBE_SUPPORT,
            0,
            (),
            CURVED_EXTRA_DISPLACEMENTS,
            CURVED_EXTRA_HOPS,
            0,
            (),
        )
    )
    gate_f = bool(
        facts.mass_order
        == (
            MASS_SLOTS,
            (
                b145.B_MODULUS[(3, 0)] + b145.B_MODULUS[(3, 3)],
                b145.B_MODULUS[(3, 1)] + b145.B_MODULUS[(3, 2)],
                -b145.B_MODULUS[(1, 0)] - b145.B_MODULUS[(1, 3)],
                -b145.B_MODULUS[(1, 1)] - b145.B_MODULUS[(1, 2)],
            ),
            True,
            tuple(sorted(str(s) for s in b145.ODD_SHEAR_COORDS)),
            True,
            True,
            (
                ("flat", True, False),
                ("uniform odd-t", True, False),
                ("ON-locus A", False, False),
                ("c*", False, False),
            ),
            True,
            PSD_INERTIA,
            CSTAR_CORE,
            True,
            True,
            True,
            SECOND_ORDER_INERTIA,
            tuple(sorted(
                [(value, 1) for value in SECOND_ORDER_EIGENVALUES]
                + [(sp.Integer(0), NULL_DIMENSION)],
                key=str,
            )),
        )
        and facts.counterterm
        == (
            2 * 2 * LX,
            COUNTERTERM_ODD_ODD,
            True,
            tuple(sorted(COUNTERTERM_EVEN_ODD)),
            claims["counterterm_disjoint"],
            True,
        )
        and facts.scaling
        == (
            tuple(str(a) for a in SCALING_AMPLITUDES),
            (MASSIVE_CURVED_INERTIA,) * len(SCALING_AMPLITUDES),
            (True,) * len(SCALING_AMPLITUDES),
            facts.scaling[3],
            (True, True),
        )
        and deep_family_ok
        and deep_generators_ok
        and facts.exact_no_float
    )

    gate_g = bool(
        facts.blindness
        == (
            THETA_PRIME_REAL_ZERO,
            THETA_REAL_ZERO,
            facts.blindness[2],
            True,
            ((0, 0), (1, 1), (2, 2), (3, 3)),
            claims["theta_prime_complex_zero"],
            THETA_PRIME_CURVED_ZERO,
            THETA_PRIME_CURVED_LIVE_ZERO,
            FREE_VOLUME_ZERO_EDGES,
            (EDGE_COUNT, EDGE_COUNT),
            SINGLE_CELL_REVIVALS,
            TIED_WEIGHTS,
            TIED_PARAMETERS,
            (VANISHING_CODIMENSION, VANISHING_CODIMENSION),
            COMMITTED_IMAGE_RANK,
            COMMITTED_FAMILY_PARAMETERS,
            TIED_PARAMETERS,
        )
        and claims["theta_prime_complex_zero"] < EDGE_COUNT
        and facts.stratum
        == (
            b156.L147_DIM,
            b156.L147_DIM,
            b156.L154_DIM,
            b156.L154_DIM,
            b156.MEET_DIM,
            b156.MEET_DIM,
            (-WITNESS_MOMENT, -WITNESS_MOMENT, WITNESS_MOMENT,
             WITNESS_MOMENT, -WITNESS_MOMENT, -WITNESS_MOMENT,
             WITNESS_MOMENT, WITNESS_MOMENT),
            True,
            True,
            True,
            (WITNESS_MOMENT,),
            claims["theta_mass_gram_dead"],
            ODD_X_INERTIA,
            (2, 0, 2),
            claims["mass_derivative_zero"],
            True,
            PSD_INERTIA,
            (PSD_INERTIA,) * 4,
            True,
            ODD_MOMENTS,
            True,
            True,
            True,
            True,
            SURVIVAL_CODIMENSION,
            True,
            CONE_COORDINATES,
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
            "run the two TWICE-VERIFIED sweeps: the full 41-point lambda grid "
            "over all ten configurations, with every inertia read twice, once "
            "by the committed Block 144 congruence helper and once by exact "
            "real-root counting on the characteristic polynomial; and the "
            "explicit antiperiodically-tied single-hop generator sweep against "
            "the four mass-channel slots, planted generator by generator and "
            "checked against the free-symbol reading"
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
        f"  THE OBJECT: flat cover Hodge is I_32 {facts.calibration[1]} and "
        f"H_q is I_16 {facts.calibration[2]}; theta is {facts.calibration[3]} "
        f"on the committed half; the pure link deletion is (4,4,0) on "
        f"{facts.calibration[4]}, (0,4,4) on {facts.calibration[5]} more and "
        f"empty on {facts.calibration[6]}; the primary pairing is "
        f"diag(4/5,0,...) {facts.calibration[7]} at rank {facts.calibration[8]}"
        f" inertia {facts.calibration[9]}, mass-independent on flat "
        f"{facts.calibration[10]}; probe support {facts.calibration[11]}"
    )
    print(
        f"  T1 DECOUPLING KILL: null dimensions {facts.decoupling[0]}, "
        f"{facts.decoupling[1]} null vectors all exactly odd-x "
        f"{facts.decoupling[2]}; 8x16 row occupancy {facts.decoupling[3]}; K "
        f"touches no odd-x row or column {facts.decoupling[4]}; the flat mass "
        f"block is raw-nonzero with a vanishing Hermitian part "
        f"{facts.decoupling[5]}; cone off-diagonals {facts.decoupling[6]} all "
        f"cross-parity {facts.decoupling[7]} carrying only "
        f"{facts.decoupling[8]} at ten times {facts.decoupling[9]}"
    )
    print(
        f"  THE PULLBACK, LITERALLY: the even-x core is (4/5) I_4 "
        f"{facts.factorization[0]}; P = A^T A with A = sqrt(4/5) P_even "
        f"{facts.factorization[1]}; P = P_even^T P P_even "
        f"{facts.factorization[2]}; no float in the factor "
        f"{facts.factorization[3]}; on c* the core is diagonal "
        f"{facts.factorization[5]} at {facts.factorization[4]} and the "
        f"pullback identity still holds {facts.factorization[6]}"
    )
    print(
        f"  T2 CONTENT: the symbolic form carries {facts.content[0]} and is "
        f"diag(s_t,0,...) {facts.content[1]}, vanishing iff s_t = 0 "
        f"{facts.content[2]}; s_x present {facts.content[3]}"
    )
    print(
        f"  T2 HOLONOMY: dressed spectrum is {{(4/5)cos a x4, 0 x4}} "
        f"{facts.holonomy[0]} with every first derivative zero "
        f"{facts.holonomy[1]}; inertia at pi/3 {facts.holonomy[2]}, pi/2 "
        f"{facts.holonomy[3]}, 2pi/3 {facts.holonomy[4]}; only "
        f"{facts.holonomy[5]} of 8 hops feed, at cover times "
        f"{facts.holonomy[6]}; a spatial dressing makes {facts.holonomy[7]} "
        f"plaquettes nontrivial and changes nothing {facts.holonomy[8]}; "
        f"pure gauge {facts.holonomy[9]}"
    )
    print(
        f"  T3 ORBIT: {facts.orbit[0]} translations, census flat "
        f"{facts.orbit[1]} and c* {facts.orbit[2]}; stabilizer "
        f"{facts.orbit[3]} of order {facts.orbit[4]}, closed "
        f"{facts.orbit[5]}, inverses {facts.orbit[6]}, identity "
        f"{facts.orbit[7]}; the {facts.orbit[9]} dead elements have time "
        f"parities {facts.orbit[8]}; even-t odd-x all (2,4,2) "
        f"{facts.orbit[10]}"
    )
    print(
        f"  T7 RIDERS: FLIP negates the off-diagonals {facts.riders[0]} and "
        f"fixes the diagonals {facts.riders[1]}; the odd-x conjugate is "
        f"{facts.riders[2]}, hollow {facts.riders[3]}, supported at "
        f"{facts.riders[4]}; SPECTRA even-x {facts.riders[5]} against odd-x "
        f"{facts.riders[6]} at equal ranks {facts.riders[7]}; the weight table "
        f"is {facts.riders[8]}"
    )
    print(
        f"  T4 LAMBDA FAMILY: {facts.family[3]}-point grid; PSD sets on the "
        f"flat carrier {facts.family[4]}; every interior lambda indefinite "
        f"{facts.family[5]}; flat anchors reproduce {facts.family[6]}; "
        f"ON-locus lambda = 1 splits by mass {facts.family[7]}; OFF-locus "
        f"negatives count the violated locus equations {facts.family[8]}; "
        f"nulls at lambda = 1 {facts.family[9]}; {facts.family[10]} "
        f"configurations available under --deep"
    )
    for row in facts.family[11]:
        print(f"    anchors {row[0]:16s} m = {row[1]}: {dict(row[2])}")
    print(
        f"  T6 AT ITS CORRECTED SCOPE: {facts.chart_law[0]} live edges; the "
        f"scalar law value(i,j) = base(i) - s_t (lambda_j - lambda_i) holds "
        f"{facts.chart_law[1]} with base {facts.chart_law[2]}; at c* every "
        f"scalar is the flat one times {facts.chart_law[3]}; "
        f"{facts.chart_law[4]} give (4,4,0) and {facts.chart_law[5]} give "
        f"(0,4,4), the flat and curved signatures agreeing {facts.chart_law[6]}"
    )
    print(
        f"  T5 MASS ORDER: seam slots {facts.mass_order[0]} at eight times "
        f"{facts.mass_order[1]}, all cross-parity {facts.mass_order[2]}, "
        f"carrying {facts.mass_order[3]}, even-even empty "
        f"{facts.mass_order[4]}, odd-odd empty {facts.mass_order[5]}; "
        f"pre-check {facts.mass_order[6]}; F affine {facts.mass_order[7]}; "
        f"F(0) inertia {facts.mass_order[8]} at even-x diagonals "
        f"{facts.mass_order[9]}; P_0 = P_odd {facts.mass_order[10]}; B = 0 "
        f"{facts.mass_order[11]}; Penrose {facts.mass_order[12]}; C inertia "
        f"{facts.mass_order[13]} at {facts.mass_order[14]}"
    )
    print(
        f"  T5 COUNTERTERM: {facts.counterterm[0]} free real parameters; "
        f"odd-odd support {facts.counterterm[1]} with zero diagonal "
        f"{facts.counterterm[2]}; even-odd support {facts.counterterm[3]}, "
        f"disjoint from the mass channel {facts.counterterm[4]}; F' itself "
        f"has no odd-odd entry {facts.counterterm[5]}"
    )
    print(
        f"  T5 CURVATURE SCALING: amplitudes {facts.scaling[0]} at inertia "
        f"{facts.scaling[1]}, each most-negative eigenvalue exactly enclosed "
        f"{facts.scaling[2]}; ratio windows "
        f"{tuple((str(sp.N(w[0], 9)), str(sp.N(w[1], 9))) for w in facts.scaling[3])}"
        f" inside the claimed windows {facts.scaling[4]}"
    )
    print(
        f"  THETA-PRIME SCOPE: real symbolic weights on the flat carrier give "
        f"theta-prime zero on {facts.blindness[0]} of 16 and theta zero on "
        f"{facts.blindness[1]}; crossing weights {facts.blindness[2]} are "
        f"x-staggered {facts.blindness[3]}; COMPLEX weights leave theta-prime "
        f"zero on only {facts.blindness[5]} edges {facts.blindness[4]}; on the "
        f"general 64-modulus carrier zero on {facts.blindness[6]} with the "
        f"live-live block still zero on {facts.blindness[7]}; free per-cell "
        f"volumes leave it zero on {facts.blindness[8]} while uniform volumes "
        f"restore {facts.blindness[9]}; single-cell shears revive "
        f"{facts.blindness[10]} of 16"
    )
    print(
        f"  THE LOCI: {facts.blindness[11]} tied weights over "
        f"{facts.blindness[12]} real parameters, vanishing ranks (theta-prime, "
        f"theta) = {facts.blindness[13]}; the committed family's image has "
        f"Jacobian rank {facts.blindness[14]} from "
        f"{facts.blindness[15]} parameters into {facts.blindness[16]} "
        f"coordinates"
    )
    print(
        f"  THE STRATUM: dim L147 {facts.stratum[0]} against Block 156's "
        f"{facts.stratum[1]}; dim L154 {facts.stratum[2]} against "
        f"{facts.stratum[3]}; dim of the meet {facts.stratum[4]} against "
        f"{facts.stratum[5]}; witness odd moments {facts.stratum[6]}, in L147 "
        f"{facts.stratum[7]} and in L154 {facts.stratum[8]}, all nonzero "
        f"{facts.stratum[9]} at magnitude {facts.stratum[10]}; theta's mass "
        f"Gram dead {facts.stratum[11]}; theta-prime's is {facts.stratum[12]} "
        f"with live-live {facts.stratum[13]}; dF/dm = 0 {facts.stratum[14]}; "
        f"the pairing is diag(33/40,0,...) {facts.stratum[15]} at "
        f"{facts.stratum[16]}, inertia at four masses {facts.stratum[17]}; "
        f"cone-admissible {facts.stratum[18]} with {facts.stratum[19]} nonzero "
        f"odd-time shears; codimension {facts.stratum[24]} on disjoint "
        f"coordinates {facts.stratum[25]}"
    )
    if facts.deep_family is not None:
        print(f"  --deep lambda grid, twice verified: {facts.deep_family}")
    if facts.deep_generators is not None:
        print(f"  --deep generator sweep, twice verified: "
              f"{facts.deep_generators}")
    print()

    checks = Checks()
    checks.check(
        "A-authority",
        "main plus TWO parent artifacts are content-bound: Block 160's note and runner, which are BOTH the stack parent this block's branch is cut from AND the content parent whose import chain (b159 -> b158 -> b156 -> b155/b154/b153/b148/b147/b145/b144/b142/b137/b134/b105) carries every committed constructor used here and is pinned by Block 160's own gate A rather than duplicated in this one",
        gate_values["A"],
    )
    checks.check(
        "B-the-object-and-the-decoupling-kill",
        "THE OBJECT IS REBUILT BEFORE ANYTHING IS MEASURED AGAINST IT, AND THEN THE PRE-REGISTERED PROJECTION TEST FIRES ITS KILL BRANCH: the committed flat carrier is cone-admissible with cover Hodge I_32 and mass Gram I_16, theta is half-EXCHANGING on {p = 0, 1}, and the pure link deletion of a committed healed edge to the eight even-x temporal crossing hops WITH THEIR OWN COMMITTED WEIGHTS is positive semidefinite at (4,4,0) on exactly the six edges (0,3), (1,3), (2,0), (2,1), (2,2), (2,3), negative semidefinite on six more and empty on four, with the primary object's pairing exactly diag(4/5, 0, 4/5, 0, 4/5, 0, 4/5, 0) at rank 4 and mass-independent on the flat carrier; AND THEN T1 KILLS THE DOOR READING BY DECOUPLING -- ker F(0) is four-dimensional on all six PSD edges and all 24 null vectors are EXACTLY odd-x as exact rationals, the odd-x rows of the 8x16 block [theta K]_++ vanish identically at occupancy (1,0,1,0,1,0,1,0) so the odd-x sector is ANNIHILATED rather than merely degenerate, the residue K has no nonzero entry in any odd-x row or column of the whole 16x16, and on the committed 64-modulus cone every off-diagonal (0,7) = b_20/10, (1,4) = b_00/10, (2,5) = b_22/10, (3,6) = b_02/10 joins an even-x slot to an odd-x slot against a zero diagonal, so the codimension-4 PSD locus IS the parity-decoupling locus; and the sharpest phrasing is LITERALLY TRUE, verified as an exact matrix identity rather than asserted -- P = A-transpose A with A = sqrt(4/5) P_even, a PULLBACK of a positive definite form on the even-x quotient, and on the curved carrier c* the same pullback shape with core diag(257/240, 229/210, 31/30, 79/75)",
        gate_values["B"],
    )
    checks.check(
        "C-content-and-the-holonomy-derivative",
        "T2 SPLITS, AND BOTH HALVES ARE MEASURED RATHER THAN ASSERTED: with BOTH shears symbolic the object's flat pairing is exactly diag(s_t, 0, s_t, 0, s_t, 0, s_t, 0), so it carries the temporal shear LINEARLY and vanishes identically iff s_t = 0 and is therefore NOT in Block 154's fully connection-blind artifact class -- but the spatial shear s_x does not appear in any entry, so the form is completely s_x-BLIND; the first-order holonomy response is ZERO, since dressing all eight supported hops by e^{i alpha} gives the spectrum {(4/5)cos(alpha) x4, 0 x4} whose every eigenvalue derivative vanishes at alpha = 0, motion being O(alpha^2), with the signature (4,4,0) on the open interval |alpha| < pi/2, degenerate (0,8,0) at pi/2 and reversed (0,4,4) beyond; a single SPATIAL link dressing makes two plaquettes nontrivial -- the committed minimal dipole -- and leaves differential, residue and pairing COMPLETELY UNCHANGED, so curvature living off the eight hops is invisible at every order and not merely to first order; two rational-unimodular PURE GAUGES with zero nontrivial plaquettes change the four nonzero eigenvalues while preserving the inertia, so the dressing acts by congruence and only the signature is invariant; AND THE THINNESS IS DISCLOSED -- of the object's eight cover hops only FOUR feed the {p = 0, 1} pairing at all, namely the antiperiodic image copies at cover times 5 and 7, so the certificate rests on four cover hops, half of an already-deleted support",
        gate_values["C"],
    )
    checks.check(
        "D-the-taste-structure-and-the-riders",
        "THE ONE STRUCTURAL RESULT THAT SURVIVES IS MEASURED AT FULL EXPLICITNESS, AND THE RIDER ARGUMENT IS THE CHECKER'S REPAIRED ONE: over the full 32-element translation group, with the WHOLE configuration transported (differential and carrier) and theta and the half held fixed, the census is {(4,4,0): 8, (2,4,2): 8, (0,8,0): 16} IDENTICALLY on the flat carrier and on the curved interior carrier c*, and the stabilizer is measured -- not assumed -- to be exactly the even-time, even-x translations, an honest order-8 index-4 subgroup verified CLOSED under all 64 compositions, closed under inverses and containing the identity, which is NOT Block 155's ragged shape; the 16 dead elements are exactly the odd-TIME translations, because an odd time shift carries the hops off the half boundary, while even-time odd-x shifts all give (2,4,2), so time parity decides live-versus-dead and x parity decides PSD-versus-indefinite; AND THE RIDERS: the codimension-4 locus is exactly FLIP-invariant since FLIP negates precisely the four off-diagonal entries and fixes all four diagonals, the odd-x conjugate deletion is HOLLOW with zero diagonal and support only at (1,3) and (5,7) at inertia (2,4,2), and the non-relation is proved BY SPECTRA rather than by inertia -- {4/5 x4, 0 x4} against {4/5 x2, 0 x4, -4/5 x2} at equal rank 4, so no unitary relates them, the primary's inertia-only argument being replaced while Sylvester's law still gives non-congruence -- and the real/imaginary staggering swaps theta and theta-prime exactly, uniform real weights annihilating both, staggered real weights annihilating theta alone and staggered imaginary weights annihilating theta-prime alone",
        gate_values["D"],
    )
    checks.check(
        "E-the-lambda-family-and-T6-at-its-corrected-scope",
        "TWO PRE-REGISTERED READINGS FALL HERE, AND THE SECOND FALLS ONLY AS FAR AS THE CHECKER'S DOWNGRADE ALLOWS: the lambda family C(lambda) = (1 + lambda (-1)^x) C_committed is built correctly -- lambda = 1 is twice the validated object, lambda = -1 is twice its odd-x conjugate, lambda = 0 reproduces the full committed edge's own pairing -- and over the 41-point grid on the flat carrier at both masses the ONLY positive-semidefinite-and-live point is lambda = 1 exactly, every strictly interior lambda being indefinite, with the three pre-registered anchors reproduced exactly ((4,4,0), (2,4,2), (6,0,2) at lambda = 1, -1, 0) on the flat carrier and on both ON-locus curvature carriers, and with the null space at lambda = 1 four-dimensional at even-x content EXACTLY zero, so the Adams-style DERIVABLE FLAVORED COEFFICIENT reading is REFUTED and the decoupling branch fires again in agreement with T1; AND T6's MEASUREMENT STANDS WHILE ITS INTERPRETATION DOES NOT -- on the same carrier c*, with the carrier and all four locus coordinates untouched, 6 of the 12 live committed edges give (4,4,0) and 6 give (0,4,4), but the split obeys EXACTLY value(i,j) = base(i) - s_t (lambda_j - lambda_i) with base = (0, 0, +s_t, -s_t) verified on all twelve live edges, and at c* every one of the twelve scalars is the flat value times ONE common positive constant 257/192, so what reverses is the sign of a healing-weight-dependent SCALAR multiplying a fixed rank-4 pullback and not a chart-dependent signature: the kill rests on T1 and never on T6",
        gate_values["E"],
    )
    checks.check(
        "F-the-mass-lift-order-and-the-counterterm-theorem",
        "THE MASS NO-GO'S FINAL SHAPE IS BETWEEN THE TWO PRE-REGISTERED EXTREMES AND EVERY STEP IS EXACT: on the committed 64-modulus family the seam insertion herm([theta H_q]_++) has exactly four nonzero slots (0,3) = (b_30+b_33)/8, (1,2) = (b_31+b_32)/8, (4,5) = -(b_10+b_13)/8, (6,7) = -(b_11+b_12)/8, every one of them even-x-to-odd-x, fed exclusively by the eight odd-TIME shears with an empty even-even block and an empty odd-odd block; the pre-check theta H_q theta against H_q-dagger is reflection-EVEN on the flat and on the theta-symmetric uniform odd-time carrier and NEITHER even NOR odd on a generic admissible carrier, so it does not decide the order by itself; F(m) is exactly affine in the mass with F'' = 0, the kernel projector P_0 equals P_odd as a matrix identity, and B = P_0 F'(0) P_0 = 0 STRUCTURALLY rather than numerically, so the FIRST-ORDER reflection-odd no-go does NOT fire; the four Penrose identities are verified and the second-order coefficient C = -P_0 F' F(0)^+ F' P_0 is minus a Gram matrix at inertia (0,4,4) with exact eigenvalues {-375/51296, -1215/263168, -1215/253952, -507/1294336}; the crossing-block counterterm, run with 16 free real parameters over all four columns and both time classes, has a HOLLOW odd-odd block and an even-odd support disjoint from the mass channel's, so no O(m) crossing-block counterterm exists -- and the derivation used here is the checker's sound route, that P_0 (F' + G) P_0 = 0 forces the second-order coefficient to vanish and hence the even-odd block with it, not the primary's loose zero-row shortcut; AND THE NEGATIVES ARE SOFT -- three shear amplitudes give most-negative eigenvalues certified by EXACT real-root enclosures, in successive ratios inside the windows claimed, quadratic in the shear and converging to 4, so the drift is O(curvature^2 m^2) and not O(1)",
        gate_values["F"],
    )
    checks.check(
        "G-the-theta-prime-scope-and-the-mass-survival-stratum",
        "THE BLOCK'S TWO HEADLINE CORRECTIONS ARE MEASURED IN FULL, AND THE FIRST OF THEM REFUTES THE PRIMARY'S OWN HEADLINE: with real symbolic healing weights on the committed flat carrier theta-prime's exchange pairing is identically zero on all 16 healed edges while theta's is nonzero on 14, and the crossing weights are i s_t (lambda_j - lambda_i)(-1)^x, x-staggered for any shears and any weights -- BUT STAGGERING IS NOT WHAT ANNIHILATES: with COMPLEX healing weights theta-prime is zero on only 4 of the 16 edges, on the general 64-modulus carrier it is nonzero on all 16 (its live-live block still zero on all 16, so Block 159's W1 core is intact), at zero shear with 16 free per-cell volumes it is zero on only 2, uniform volumes restore all 16 because they make the cover Hodge a multiple of the identity, and every one of the 16 single-cell shear perturbations revives it, so the exact condition is Im(lambda_j - lambda_i) = 0 TOGETHER WITH a cover Hodge proportional to the identity and the honest statement is that the COMMITTED configuration sits inside the annihilation set; Block 160's codimension count is EXACT at its own scope, both vanishing loci having rank 8 in the 48-real-parameter tied weight space with the committed family's image a rank-3 variety inside it, so the word understates is struck; AND THE MASS-SURVIVAL STRATUM STANDS AND IS SHARPENED -- the carrier-side balance is Block 147's annealed locus L147 = ker(R+1) VERBATIM at Block 156's own dimension, L154 and the dimension-2 intersection reproduce Block 156's own constants, the witness sits in that intersection with all eight odd moments at +-3/8 and is NOT the dead carrier, there is NO contradiction with Block 156 because its kill is theta-prime-scoped (at this very carrier theta's mass Gram is identically zero while theta-prime's is (2,4,2) with live-live (2,0,2), so that kill fires untouched), the all-mass positivity is proved SYMBOLICALLY with dF/dm = 0 identically and the pairing exactly diag(33/40, 0, 33/40, 0, 33/40, 0, 33/40, 0) at (4,4,0) for every mass, the carrier is cone-admissible with eight nonzero odd-time shears and a non-diagonal cover Hodge, and the codimension-8 arithmetic is exact on disjoint coordinate sets of the 32-coordinate cone",
        gate_values["G"],
    )
    checks.check(
        "H-note-scope",
        "the scout discipline stated as a discipline -- every support restriction, reweighting, reflection and half carrier here is a registered-premise-class change that is MEASURED and never registered, adopted or proposed -- the pre-registered branch semantics quoted with their panel provenance, THE DOOR READING DECLARED DEAD with positivity-by-decoupling as the mechanism and the 24 odd-x nulls, the zero odd-x row occupancy, the parity-decoupling locus and the A-transpose-A pullback factorization displayed, T2's s_t-linearity against its s_x-blindness and its O(alpha^2) holonomy motion and its four-of-eight feeding hops, the Adams reading refuted at lambda = 1 only, T6 DOWNGRADED with the scalar law base(i) - s_t (lambda_j - lambda_i) in place of chart dependence and the kill recorded as resting on T1, THE THETA-PRIME HEADLINE QUOTED AND THEN CORRECTED with its ANY-shears-and-ANY-healing-weights wording reproduced, the reality condition Im(lambda_j - lambda_i) = 0, the Hodge-proportional-to-the-identity condition, the complex-weight counterexample, the committed-configuration scope, Block 160's codimension 8 recorded as exact with understates struck and the rank-3 image named, and the landed corpus statements left standing at their own carrier scopes, THE MASS-SURVIVAL STRATUM with L147 identified verbatim, the dimension-2 intersection, the live witness, the absence of contradiction with Block 156 and its theta-prime-scoped kill, THE BLOCK 156 NARROWING carrying the landed sentence verbatim with its positivity qualifier, the mass-independence and dF/dm = 0 and the codimension-8 arithmetic on the 32-coordinate cone, the counterterm emptiness and its strengthening to the uncommitted displacement classes, B = 0 structurally, the second-order negative coefficient inside ker F(0), the quadratic curvature scaling, the neither-even-nor-odd pre-check and the carrier-side-open verdict, THE SURVIVORS AND THE KILLED as an explicit ledger with the order-8 stabilizer, the identical census, FLIP-invariance, the hollow odd-x conjugate and its spectra argument, the role swap and the taste structure, Block 162, the site-reflection lead and the pool-2 items, together with checker credit, quoted-then-corrected readings, common-mode and cross-context disclosure, the not-re-verified list, sample scope, N1 through N8, the W1 wall, the exact N5 fence, the LaTeX rho guard, and NO priority or originality wording anywhere in the note, not even inside a prohibition list",
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
