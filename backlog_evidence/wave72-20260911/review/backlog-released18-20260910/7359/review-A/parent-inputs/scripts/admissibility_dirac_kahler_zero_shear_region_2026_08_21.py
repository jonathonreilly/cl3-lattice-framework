#!/usr/bin/env python3
# Final path: scripts/admissibility_dirac_kahler_zero_shear_region_2026_08_21.py
"""Block 164: THE ZERO-SHEAR REGION.

SCOUT DISCIPLINE, AND IT IS A HARD BOUNDARY.  Every reflection outside the
committed four, every support outside the committed half, and every carrier
outside the committed family exercised here is a REGISTERED-PREMISE-CLASS CHANGE
to the committed framework.  Each one is MEASURED and NONE of them is
registered, adopted, proposed or claimed.  Nothing in this runner edits, retires
or amends any committed note, axiom, premise or convention.

THE CRITERION, IN CLOSED FORM, PROVED ON THE FULL 64-MODULUS CARRIER FAMILY,
ALL 24 INVOLUTIVE SITE REFLECTIONS, ALL 16 HEALED EDGES, SYMBOLIC MASS AND
SYMBOLIC s_x.  At s_t = 0 the half-support site pairing is EXACTLY

    [r Q]_{S,S} = [[ B , C ] , [ C^T , 0 ]] ,      S = {c, c+1}

with the (c+1,c+1) block IDENTICALLY zero, B carrying NO shear modulus, and C a
HOMOGENEOUS LINEAR form in exactly the EIGHT LOCAL shears {b_{c-1,x}, b_{c,x}}.
A hollow corner forces PSD <=> C = 0 and B >= 0; the traceless 2-cycle minors
force pi = id whenever m != 0; hence

    PSD AND MASS-CARRYING  <=>  X-TRIVIAL (e_x, p_x) = (+1, 0)
                            AND m > 0
                            AND sigma = 0 on the TWO TIME LINKS INCIDENT TO
                                the fixed slice c (cells (c-1,x) and (c,x)),

and there [r Q]_{S,S} = m diag(D(c,.)) (+) 0_4 with

    D(t,x) = ( nu_{t,x} + a_{t-1,x} + a_{t,x-1} + mu_{t-1,x-1} ) / 4 .

D IS A LATTICE-HODGE TRACE -- THREE VOLUME MODULI AND ONE INVERSE VOLUME
MODULUS, the inverse sitting on the past-diagonal corner -- and it is
HOMOGENEOUS OF NO DEGREE under nu -> lambda nu.  It is NEVER "a volume average";
that wording is struck on the independent checker's objection and the gate for
this block greps the lattice-Hodge-trace phrasing instead.

THE CONNECTION THEOREM IS THE INDEPENDENT CHECKER'S RESULT AND IT IS CREDITED AS
SUCH; it is RE-VERIFIED here rather than quoted.  P is EXACTLY AFFINE-LINEAR in
s_t (every healed differential entry is a s_t + b s_x, so P is degree <= 1 in
s_t in 384 of 384 cells) -- so the question Block 163 handed forward as
"perturbative" has an EXACT answer at all magnitudes and both signs: on the
region dB/ds_t = 0, the corner is exactly s_t E with E TRACELESS and a pure form
in the FREE shears, and the off-diagonal block is exactly s_t C1 with C1 never
zero.  NOTHING SURVIVES SWITCHING s_t ON.

THREE DEFECTS OF THIS BLOCK'S OWN SOLVE TRANSCRIPT ARE FOLDED, EACH QUOTED THEN
CORRECTED.  (S1) "the healing weights enter only through s_t, so at s_t = 0 they
drop out entirely" is FALSE and is STRUCK: at s_t = 0 the edge is live in 24 of
24 labels and, after the local shears are pinned, still live in 16 of 24; the
true mechanism is that the edge dependence carries ZERO MASS in 360 of 360
comparisons and therefore enters only through s_x, which on the x-trivial class
lives entirely in C -- so EDGE-BLINDNESS FOLLOWS FROM C = 0.  (S2) the failure
counts of the two earlier characterizations are attached to the WRONG BENCH: 64
+ 64 and 96 are the m = 1 sub-bench (2688 cells); on the three-mass 8064-cell
bench the same guesses cost 128 + 128 and 320.  Both figures are displayed and
correctly attributed.  (S3) "stabilizer of order 8" is a CATEGORY ERROR and is
STRUCK: {0,3} x Z_4 is not closed under addition, so it is a DWELL SET and not a
subgroup; the general-element region-preserving translation group has order 4.

ONE REFINEMENT THIS RUNNER ADDS TO THE CHECKER'S OWN STATEMENT, disclosed rather
than smoothed: the checker's "on a carrier with any free shear, E != 0" holds on
the ODD fixed slices only.  E is nonzero in exactly 32 of the 64 region cells --
c in {1,3}, matching the checker's own 192-of-384 corner measurement -- and is
identically zero at c in {0,2}, where the hollow-corner lemma applies at EVERY
s_t and the C = s_t C1 branch closes the theorem by itself.  The theorem is
unchanged; its proof has two branches and both are exhibited.

NO HARDCODED CERTIFICATE ANYWHERE: every printed numeral is recomputed in the
measurement pass from the committed constructors reached through the LANDED
Block 163 runner, and no check is registered as a literal True.  Exact SymPy
throughout; no float enters any measured object, which is itself gated.  The
integer monotonic clock is used only for the runtime gate.

PROVENANCE DISCLOSURE: the four-chart shear atlas, the local differential, the
64-modulus carrier model and its admissible cone, the cover Hodge, the
antiperiodic quotient and its lift, the sixteen healed edge differentials and
their healing weights, the reflection move machinery and its covariance
condition, the staggered grading X_0, the quotient action, the Block 144
symmetric-congruence inertia helper, and Block 163's descent, involution
enumeration, half support, selector and pairing functor are ALL COMMITTED
objects, imported through the Block 163 runner (b163 -> b162 -> b161 -> b160 ->
b159 -> b156 -> b153 -> b148 -> b147 -> b145 -> b142) and never re-derived.
External lattice-gauge, staggered-fermion and Osterwalder-Schrader literature is
REFERENCED nowhere and BORROWED nowhere; every statement is re-proved
in-framework.

HYPOTHESES, named and not imported.  (H1) the pairing convention is
[r Q]_{S,S} = herm(Sel_S^T r Q Sel_S) on the half support S = {c, c+1}.
(H3) "positive" is a statement about the Hermitian part.  (H4) the physical cone
is nu > 0, |sigma| < 1 per cell.  (H1-163) a PSD verdict here is a statement
about THIS pairing functor on THESE supports over THESE carriers and about no
wider class of objects; "PSD" means no negative direction AND a nonzero positive
count, so the zero form is never counted as a positive.  (H1-164) the region is
read in the 32 real carrier coordinates (16 volumes, 16 shears) and the
64-modulus family is its free relaxation, in which nu, a, b and mu are
independent symbols; a statement proved on the free family holds on the cone.
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

import admissibility_dirac_kahler_site_reflection_channel_2026_08_21 as b163

b162 = b163.b162
b161 = b163.b161
b159 = b163.b159
b156 = b163.b156
b148 = b163.b148
b145 = b163.b145


NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_ZERO_SHEAR_REGION_"
    "BOUNDED_THEOREM_NOTE_2026-08-21.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE SINGLE-PARENT PIN.  Block 163 (the site-reflection channel) is BOTH the
# stack parent -- this block's branch is cut from it -- AND the content parent:
# every committed constructor used here is reached through the Block 163
# runner's own import chain (b162 -> b161 -> b160 -> b159 -> b156 -> b153 ->
# b148 -> b147 -> b145 -> b142), which Block 163's own gate A pins and this
# block does not duplicate.  So there are exactly TWO artifact pins here.
BLOCK163_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_REFLECTION_CHANNEL_"
    "BOUNDED_THEOREM_NOTE_2026-08-21.md"
)
BLOCK163_RUNNER = (
    "scripts/admissibility_dirac_kahler_site_reflection_channel_2026_08_21.py"
)

PARENT_ARTIFACTS = (BLOCK163_NOTE, BLOCK163_RUNNER)
# PLACEHOLDER BLOBS for the Block 163 pair, single-line hex literals; the
# landing supervisor refreshes exactly these two lines by anchored sed against
# the Block 163 branch tip.  Until they are refreshed gate A FAILS, which is the
# intended state of an unlanded draft.
PARENT_ARTIFACT_BLOBS = (
    "9c63f7934900c375dfed5efa2447d8bdcd1eaa76",   # Block 163 note
    "ea907cd3379df7bf51d8081fbefb8027fd197ccc",   # Block 163 runner
)

# Deliberately literal: this is the complete audit read surface.  Every entry is
# a WORKTREE-READABLE path at landing time; the cache envelope stats these, so an
# origin/main-only path here would break the audit (the Block 130 lesson,
# re-learned at every landing since).
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_ZERO_SHEAR_REGION_BOUNDED_THEOREM_NOTE_2026-08-21.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_REFLECTION_CHANNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md",
    "scripts/admissibility_dirac_kahler_site_reflection_channel_2026_08_21.py",
)

AUDIT_TIMEOUT_SEC = 600
# Authority pins, single-line hex literals refreshed by anchored sed at landing.
CURRENT_MAIN = "38109c451a2ba1affde68aeaf58e6507187ff7af"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
# This block stacks on Block 163, so the parent branch is Block 163's.
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block163-site-reflection-channel-20260821"
)
# The Block 163 branch tip, VERIFIED to be an ancestor of HEAD and to carry both
# pinned artifact paths.  The two BLOB lines above are the placeholders.
PARENT_COMMIT = "67036479b317c597372fdfed610630159f97d5f7"
# Block 162's tip: a real ancestor of HEAD that PREDATES BOTH pinned parent
# artifacts.  VERIFIED before pinning with `git rev-parse`, which finds NEITHER
# the Block 163 note NOR the Block 163 runner at this commit, so resolving the
# parent pin here leaves BOTH pinned blobs ABSENT.  This pin is read ONLY under
# the stale mutation; the baseline gate never requires it.
STALE_PARENT_COMMIT = "b9ef6b24579964787ebb54bfbe8f7f406aa648d8"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "break_hollow_corner",
    "break_criterion",
    "claim_single_slice_forced",
    "break_bench_attribution",
    "claim_sigma_in_spectrum",
    "claim_volume_average",
    "break_affine_linearity",
    "break_connection_theorem",
    "claim_edge_blind_via_st",
    "claim_stabilizer_eight",
    "drop_conjunction_split",
    "drop_checker_credit",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "break_hollow_corner": "B",
    "break_criterion": "C",
    "claim_single_slice_forced": "D",
    "break_bench_attribution": "D",
    "claim_sigma_in_spectrum": "E",
    "claim_volume_average": "E",
    "break_affine_linearity": "F",
    "break_connection_theorem": "F",
    "claim_edge_blind_via_st": "G",
    "claim_stabilizer_eight": "G",
    "drop_conjunction_split": "H",
    "drop_checker_credit": "H",
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
    return b163.no_float(value)


def guarded_inertia(matrix: sp.MatrixBase):
    """The committed Block 144 congruence inertia, with its failure DISCLOSED.

    Reached through the landed Block 163 runner, so the tool this block reasons
    with is exactly the blob Block 163's gate A pins.  A cell the landed helper
    cannot resolve is returned as None, counted and reported -- never counted as
    a positive and never counted against one.
    """
    return b163.guarded_inertia(matrix)


def is_psd(inertia) -> bool:
    """H1-163: no negative direction AND a nonzero positive count."""
    return b163.is_psd(inertia)


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
# the committed model, imported wholesale through Block 163
# ---------------------------------------------------------------------------
PHYS_T, LX, PHYS = b163.PHYS_T, b163.LX, b163.PHYS
HALF = b163.HALF
MASS = b163.MASS
SHEAR_X, SHEAR_T = b163.SHEAR_X, b163.SHEAR_T
EDGE_KEYS = b163.EDGE_KEYS
EDGE_DIFF = b163.EDGE_DIFF
COVER_FREE = b163.COVER_FREE
DESCENT = b163.DESCENT
INVOL = b163.INVOLUTIVE_SITE
X_TRIVIAL = b163.X_TRIVIAL

CELLS = tuple((t, x) for t in range(PHYS_T) for x in range(LX))
NUMOD, AMOD, BMOD, IMOD = (
    b145.NU_MODULUS, b145.A_MODULUS, b145.B_MODULUS, b145.INV_MODULUS
)
SHEAR_SET = frozenset(BMOD.values())
NON_SHEAR_SET = (
    frozenset(NUMOD.values()) | frozenset(AMOD.values())
    | frozenset(IMOD.values())
)
ATLAS_SX = R(3, 5)
PROBE_ST = R(4, 5)


# ---------------------------------------------------------------------------
# the certificate constants this runner is claiming
# ---------------------------------------------------------------------------
EDGE_COUNT = 16
INVOLUTIVE_COUNT = 24
X_TRIVIAL_COUNT = 4
COVARIANT_COUNT = 16
CELL_COUNT = 384                    # 24 involutions x 16 healed edges
REGION_CELLS = 64                   # 4 x-trivial reflections x 16 healed edges
NON_XTRIVIAL_CELLS = 320
HQ_DISPLACEMENTS = (0, 1, 3)
RANK_EIGHT_CELLS = 256
RANK_SEVEN_CELLS = 128
RANK_SEVEN_CLASSES = ((-1, 0), (-1, 2))
ODD_SHEAR_KERNEL = (1, 1, 1, 1, -1, -1, -1, -1)
TWO_CYCLE_SLOTS = 1024
BENCH_CARRIERS = 7
BENCH_MASSES = 3
BENCH_CELLS = 8064
BENCH_PSD = 448
BENCH_PSD_INERTIA = (4, 4, 0)
SUB_BENCH_CELLS = 2688
B163_ST0_PSD = 64
REGION_CODIM = 8
REGION_DIM = 24
CONE_COORDS = 32
ATLAS_DIMS = {
    "cap L145": 22, "cap L147": 22, "cap L154": 23,
    "cap b161 survival set": 20, "cap b162 stratum": 19,
}
GENERIC_MEET_DIM = 14
B162_STRATUM_DIM = 22
B161_SURVIVAL_DIM = 24
CHECKER_GUESS_FULL = (128, 128)
CHECKER_GUESS_SUB = (64, 64)
SCOUT_GUESS_FULL = (128, 192)
SCOUT_GUESS_SUB = (0, 96)
REGION_EIGENVALUES = (R(79, 112), R(15, 16), R(49, 48), R(6, 5))
D_STENCIL_MODULI = 8
MAX_ST_DEGREE = 1
CORNER_FILLED_CELLS = 192
E_NONZERO_CELLS = 32
E_ODD_SLICES = (1, 3)
EDGE_COMPARISONS = 360
EDGE_B_CHANGES = 128
EDGE_C_CHANGES = 192
EDGE_LIVE_LABELS = 24
EDGE_LIVE_AFTER_PINNING = 16
EDGE_BLIND_CLASSES = ((-1, 2), (1, 0))
GENERAL_DWELL = 4
WITNESS_DWELL = 8
POOL_TWO_LEADS = 3

RUNTIME_BUDGET_SEC = 150


# ---------------------------------------------------------------------------
# constructions.  Everything below is built from the committed primitives.
# ---------------------------------------------------------------------------
def local_shears(c: int) -> tuple:
    """The eight shear moduli of the two time links INCIDENT to slice c."""
    return tuple(BMOD[((c - 1) % PHYS_T, x)] for x in range(LX)) + \
        tuple(BMOD[(c, x)] for x in range(LX))


def free_shears(c: int) -> tuple:
    """The eight shear moduli of the two links the region leaves FREE."""
    return tuple(BMOD[((c + 1) % PHYS_T, x)] for x in range(LX)) + \
        tuple(BMOD[((c + 2) % PHYS_T, x)] for x in range(LX))


def x_map(label: tuple):
    """The spatial involution pi(x) = e_x (x - p_x) on the fixed slice."""
    _et, _pt, ex, px = label
    return lambda x: (ex * (x - px)) % LX


def d_entry(t: int, x: int):
    """D(t,x): the LATTICE-HODGE TRACE at a quotient site.

    THREE direct volume moduli and ONE INVERSE volume modulus, the inverse on
    the past-diagonal corner (t-1, x-1).  This is NOT a volume average and is
    homogeneous of NO degree under nu -> lambda nu; gate E measures exactly
    that, on the independent checker's objection to the looser wording.
    """
    return (
        NUMOD[(t % PHYS_T, x % LX)]
        + AMOD[((t - 1) % PHYS_T, x % LX)]
        + AMOD[(t % PHYS_T, (x - 1) % LX)]
        + IMOD[((t - 1) % PHYS_T, (x - 1) % LX)]
    ) / 4


def field_of(shear_of, volume_of) -> dict:
    """A carrier field built STRICTLY from sympy exacts (b163's gated form)."""
    return {
        (t, x): (sp.sympify(shear_of(t, x)), sp.sympify(volume_of(t, x)))
        for t in range(PHYS_T)
        for x in range(LX)
    }


def criterion(field: dict, label: tuple, mass) -> bool:
    """THE BLOCK 164 CRITERION at s_t = 0, on the admissible cone.

    PSD-and-mass-carrying  <=>  (e_x, p_x) = (+1, 0)  and  m > 0  and
    sigma = 0 on the two time links INCIDENT to the fixed slice c.
    Edge-free and s_x-free by construction: neither appears here.
    """
    if (label[2], label[3]) != (1, 0):
        return False
    if not mass > 0:
        return False
    c = b163.fixed_slice(label)
    return all(
        field[((c + dt) % PHYS_T, x)][0] == 0
        for dt in (-1, 0) for x in range(LX)
    )


def scout_guess(field: dict, label: tuple, mass) -> bool:
    """Block 163's SOLVE guess: {H_q diagonal} x {x-trivial}.  No mass sign."""
    hq = b145.quotient(b145.cover_hodge_from_field(field))
    return hq.is_diagonal() and (label[2], label[3]) == (1, 0)


def checker_guess(field: dict, label: tuple, mass) -> bool:
    """Block 163's CHECKER guess: shear-free on the SUPPORT slices {c, c+1}.

    Compared LIKE FOR LIKE with the criterion: the mass-orientation clause is
    kept, because the checker's repair differed from the truth in the SLICE PAIR
    alone.  The scout guess below keeps no mass clause, because omitting m > 0
    is one of the two things wrong with it.
    """
    if (label[2], label[3]) != (1, 0):
        return False
    if not mass > 0:
        return False
    c = b163.fixed_slice(label)
    return all(
        field[((c + dt) % PHYS_T, x)][0] == 0
        for dt in (0, 1) for x in range(LX)
    )


def translate(field: dict, dt: int, dx: int) -> dict:
    return {
        (t, x): field[((t - dt) % PHYS_T, (x - dx) % LX)]
        for t in range(PHYS_T) for x in range(LX)
    }


def affine_in(expression, symbol) -> bool:
    """expression has degree <= 1 in symbol, by exact differentiation."""
    return sp.expand(sp.diff(sp.expand(expression), symbol, 2)) == 0


# the carrier bench: 7 cone-admissible carriers, every field exact
BENCH = (
    ("flat", b159.flat_field()),
    ("slice-3 shear (b163 witness)", b163.WITNESS_FIELD),
    ("single-cell shear (3,0)", b163.ST0_BENCH[1][1]),
    ("uniform shear 3/7", b163.ST0_BENCH[2][1]),
    ("graded nu, shear-free",
     field_of(lambda t, x: 0, lambda t, x: R(1 + t + x, 2))),
    ("two-slice shear t in {2,3}",
     field_of(lambda t, x: R(1, 3) if t == 2 else (R(-2, 5) if t == 3 else 0),
              lambda t, x: R(1 + (3 * t + 5 * x) % 5, 3))),
    ("far-shear + aperiodic nu, c=1 legal",
     field_of(lambda t, x: {2: R(1, 2), 3: R(-1, 4)}.get(t, 0),
              lambda t, x: {0: (R(2, 4), R(3, 4), R(5, 4), R(7, 4)),
                            1: (R(3, 8), R(5, 8), R(7, 8), R(11, 8)),
                            2: (R(1), R(1), R(1), R(1)),
                            3: (R(3, 2), R(3, 2), R(3, 2), R(3, 2))}[t][x])),
)
MASS_GRID = (R(1, 10), sp.Integer(1), sp.Integer(-1))
CURVED_ELEMENT = "far-shear + aperiodic nu, c=1 legal"
MULTI_SLICE_ELEMENT = "two-slice shear t in {2,3}"
FLAT_REGION_ELEMENT = "graded nu, shear-free"


# ---------------------------------------------------------------------------
# measured facts (computed once, before any mutation flag is consulted)
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Facts:
    main_head: str
    authority: AuthorityCertificate
    block: tuple            # B: the block theorem at s_t = 0
    criterion: tuple        # C: the criterion and the 8064-cell verification
    shape: tuple            # D: the region's shape, the two failed guesses
    conjunction: tuple      # E: the split, and the lattice-Hodge trace
    connection: tuple       # F: the checker's connection theorem, re-verified
    riders: tuple           # G: the riders at their corrected scope
    exact_no_float: bool
    scope: dict


def measure() -> Facts:
    main_head = git_output("rev-parse", "origin/main")
    authority = authority_certificate(main_head)
    exact: list = []

    hq = sp.expand(b145.quotient(COVER_FREE))
    q_full = {}
    k_zero = {}
    for key in EDGE_KEYS:
        differential = EDGE_DIFF[key]
        residue = sp.expand(b145.quotient(sp.expand(
            sp.I * (COVER_FREE * differential
                    + differential.H * COVER_FREE)
        )))
        q_full[key] = sp.expand(MASS * hq + residue)
        k_zero[key] = sp.expand(residue.subs({SHEAR_T: 0}))

    pairing_full = {}
    for label in INVOL:
        selector = b163.selector(b163.half_support(label))
        descent = DESCENT[label]
        for key in EDGE_KEYS:
            pairing_full[(label, key)] = b163.herm(
                sp.expand(selector.T * descent * q_full[key] * selector)
            )
    pairing_zero = {
        cell: sp.expand(form.subs({SHEAR_T: 0}))
        for cell, form in pairing_full.items()
    }
    zero4 = sp.zeros(LX, LX)

    # ---------------------------------------------------------------- B ----
    sx_homogeneous = sum(
        1 for key in EDGE_KEYS
        if sp.expand(k_zero[key].subs({SHEAR_X: 0})) == sp.zeros(PHYS, PHYS)
        and sp.expand(
            k_zero[key] - SHEAR_X * sp.expand(k_zero[key].diff(SHEAR_X))
        ) == sp.zeros(PHYS, PHYS)
    )
    k_displacements = set()
    for key in EDGE_KEYS:
        for i in range(PHYS):
            for j in range(PHYS):
                if k_zero[key][i, j] != 0:
                    k_displacements.add((i // LX - j // LX) % PHYS_T)
    hq_displacements = {
        (i // LX - j // LX) % PHYS_T
        for i in range(PHYS) for j in range(PHYS) if hq[i, j] != 0
    }
    antisymmetric_slices = 0
    for key in EDGE_KEYS:
        residue = sp.expand(k_zero[key].diff(SHEAR_X))
        for slice_index in range(PHYS_T):
            block = residue[LX * slice_index:LX * slice_index + LX,
                            LX * slice_index:LX * slice_index + LX]
            if sp.expand(block + block.T) == zero4:
                antisymmetric_slices += 1

    hollow = sum(1 for form in pairing_zero.values()
                 if form[LX:HALF, LX:HALF] == zero4)
    b_shear_free = sum(
        1 for form in pairing_zero.values()
        if not (form[:LX, :LX].free_symbols & SHEAR_SET)
    )
    c_supported = 0
    c_homogeneous = 0
    sx_free_in_b = collections.Counter()
    sx_in_c = 0
    for (label, key), form in pairing_zero.items():
        c = b163.fixed_slice(label)
        local = local_shears(c)
        block_c = form[:LX, LX:HALF]
        if block_c.free_symbols & SHEAR_SET <= set(local):
            c_supported += 1
        if sp.expand(block_c.subs({s: 0 for s in local})) == zero4:
            c_homogeneous += 1
        x_trivial = (label[2], label[3]) == (1, 0)
        if SHEAR_X not in form[:LX, :LX].free_symbols:
            sx_free_in_b[x_trivial] += 1
        if SHEAR_X in block_c.free_symbols:
            sx_in_c += 1
    joint_homogeneity = 0
    lam = sp.Symbol("lam", positive=True)
    for (label, key), form in pairing_zero.items():
        if key != EDGE_KEYS[0]:
            continue
        scaled = sp.expand(form.subs(
            {MASS: lam * MASS, SHEAR_X: lam * SHEAR_X}, simultaneous=True
        ))
        if sp.expand(scaled - lam * form) == sp.zeros(HALF, HALF):
            joint_homogeneity += 1
    block = (
        sx_homogeneous,
        tuple(sorted(k_displacements)),
        tuple(sorted(hq_displacements)),
        antisymmetric_slices,
        hollow,
        b_shear_free,
        c_supported,
        c_homogeneous,
        (sx_free_in_b[True], sx_free_in_b[False]),
        sx_in_c,
        joint_homogeneity,
    )
    exact.append(sum(pairing_zero[(INVOL[0], EDGE_KEYS[0])]))

    # ---------------------------------------------------------------- C ----
    d_identity = sum(
        1 for t in range(PHYS_T) for x in range(LX)
        if sp.expand(hq[LX * t + x, LX * t + x] - d_entry(t, x)) == 0
    )
    mass_identity = 0
    for (label, key), form in pairing_zero.items():
        c = b163.fixed_slice(label)
        pi = x_map(label)
        predicted = sp.zeros(LX, LX)
        for x in range(LX):
            predicted[x, pi(x)] = (d_entry(c, x) + d_entry(c, pi(x))) / 2
        if sp.expand(form[:LX, :LX].diff(MASS) - predicted) == zero4:
            mass_identity += 1

    rank_census = collections.Counter()
    rank_seven_classes = set()
    kernels = set()
    x_trivial_permutation = 0
    for (label, key), form in pairing_zero.items():
        c = b163.fixed_slice(label)
        local = local_shears(c)
        block_c = form[:LX, LX:HALF]
        rows = sp.Matrix([
            [sp.expand(sp.expand(block_c[i, j]).coeff(s, 1)) for s in local]
            for i in range(LX) for j in range(LX)
        ])
        rank = rows.rank()
        rank_census[rank] += 1
        if rank == 7:
            rank_seven_classes.add((label[2], label[3]))
            vector = rows.nullspace()[0]
            pivot = next(entry for entry in vector if entry != 0)
            kernels.add(tuple(sp.Rational(entry / pivot) for entry in vector))
        if (label[2], label[3]) == (1, 0):
            hits = [sp.expand(block_c[i, j]) for i in range(LX)
                    for j in range(LX)
                    if sp.expand(block_c[i, j]).coeff(MASS, 1) != 0]
            seen = set()
            good = len(hits) == 2 * LX
            for entry in hits:
                terms = [s for s in local if sp.expand(entry).coeff(s, 1) != 0]
                if len(terms) != 1 or sp.expand(entry) not in (
                    MASS * terms[0] / 8, -MASS * terms[0] / 8
                ):
                    good = False
                else:
                    seen.add(terms[0])
            if good and seen == set(local):
                x_trivial_permutation += 1

    two_cycle_traceless = 0
    two_cycle_massive = 0
    two_cycle_slots = 0
    for (label, key), form in pairing_zero.items():
        c = b163.fixed_slice(label)
        pi = x_map(label)
        block_b = form[:LX, :LX]
        for x in range(LX):
            y = pi(x)
            if y == x:
                continue
            two_cycle_slots += 1
            if sp.expand(block_b[x, x] + block_b[y, y]) == 0:
                two_cycle_traceless += 1
            if sp.expand(block_b[x, y]
                         - MASS * (d_entry(c, x) + d_entry(c, y)) / 2) == 0:
                two_cycle_massive += 1
    normal_form = 0
    for label in X_TRIVIAL:
        c = b163.fixed_slice(label)
        target = sp.diag(*(
            [MASS * d_entry(c, x) for x in range(LX)] + [0] * LX
        ))
        pin = {s: 0 for s in local_shears(c)}
        for key in EDGE_KEYS:
            if sp.expand(pairing_zero[(label, key)].subs(pin)
                         - target) == sp.zeros(HALF, HALF):
                normal_form += 1

    bench_cells = 0
    bench_agree = 0
    bench_disagree = []
    bench_psd = 0
    bench_unresolved = 0
    bench_census = collections.Counter()
    psd_inertias = collections.Counter()
    covariant_psd = 0
    guess_counts = collections.Counter()
    sub_bench_cells = 0
    for name, field in BENCH:
        hodge = b145.cover_hodge_from_field(field)
        for key in EDGE_KEYS:
            differential = sp.expand(EDGE_DIFF[key].subs(
                {SHEAR_T: 0, SHEAR_X: ATLAS_SX}
            ))
            action = b145.quotient_action(differential, hodge, MASS)
            for label in INVOL:
                selector = b163.selector(b163.half_support(label))
                base = b163.herm(sp.expand(
                    selector.T * DESCENT[label] * action * selector
                ))
                for mass in MASS_GRID:
                    form = sp.expand(base.subs({MASS: mass}))
                    inertia = guarded_inertia(form)
                    bench_cells += 1
                    if inertia is None:
                        bench_unresolved += 1
                        continue
                    bench_census[inertia] += 1
                    direct = is_psd(inertia)
                    if direct:
                        bench_psd += 1
                        psd_inertias[inertia] += 1
                        if label in b148.COVARIANT_MOVES:
                            covariant_psd += 1
                    if direct == criterion(field, label, mass):
                        bench_agree += 1
                    else:
                        bench_disagree.append((name, label, key, mass, inertia))
                    for tag, guess in (("checker", checker_guess),
                                       ("scout", scout_guess)):
                        predicted = guess(field, label, mass)
                        if predicted and not direct:
                            guess_counts[(tag, "full", "fp")] += 1
                        elif direct and not predicted:
                            guess_counts[(tag, "full", "fn")] += 1
                        if mass == 1:
                            if predicted and not direct:
                                guess_counts[(tag, "sub", "fp")] += 1
                            elif direct and not predicted:
                                guess_counts[(tag, "sub", "fn")] += 1
                    if mass == 1:
                        sub_bench_cells += 1

    b163_reproduction = sum(
        1 for _name, field in b163.ST0_BENCH for label in INVOL
        for _key in EDGE_KEYS
        if criterion(field, label, sp.Integer(1))
    )
    witness_hodge = b145.cover_hodge_from_field(b163.WITNESS_FIELD)
    witness_differential = sp.expand(EDGE_DIFF[b163.WITNESS_EDGE].subs(
        {SHEAR_T: 0, SHEAR_X: ATLAS_SX}
    ))
    witness_selector = b163.selector(b163.half_support(b163.WITNESS_LABEL))
    witness_form = sp.expand(b163.herm(sp.expand(
        witness_selector.T * DESCENT[b163.WITNESS_LABEL]
        * b145.quotient_action(witness_differential, witness_hodge, MASS)
        * witness_selector
    )))
    criterion_facts = (
        d_identity,
        mass_identity,
        (rank_census[8], rank_census[7]),
        tuple(sorted(rank_seven_classes)),
        tuple(sorted(kernels)),
        x_trivial_permutation,
        (two_cycle_traceless, two_cycle_massive, two_cycle_slots),
        normal_form,
        (bench_cells, bench_agree, len(bench_disagree), bench_unresolved),
        bench_psd,
        dict(psd_inertias),
        dict(bench_census),
        covariant_psd,
        b163_reproduction,
        sp.expand(witness_form.subs({MASS: 1})) == sp.diag(
            1, 1, 1, 1, 0, 0, 0, 0
        ),
        guarded_inertia(sp.expand(witness_form.subs({MASS: 1}))),
        criterion(b163.WITNESS_FIELD, b163.WITNESS_LABEL, sp.Integer(1)),
        sub_bench_cells,
    )
    exact.append(sum(witness_form))

    # ---------------------------------------------------------------- D ----
    region_rows = {}
    atlas = {}
    balance = b162.BALANCE_ROWS
    l147 = b162.L147_ROWS
    l154 = b162.L154_ROWS
    l145 = sp.Matrix([
        [sp.Integer(1) if i == CELLS.index((t, x))
         else (sp.Integer(-1) if i == CELLS.index((t, (3 - x) % LX))
               else sp.Integer(0))
         for i in range(len(CELLS))]
        for t in (1, 3) for x in range(LX)
    ])
    survival = sp.Matrix.vstack(balance, l147)
    stratum = sp.Matrix.vstack(balance, l147, l154)
    for c in range(PHYS_T):
        rows = []
        for cell in ([((c - 1) % PHYS_T, x) for x in range(LX)]
                     + [(c, x) for x in range(LX)]):
            row = [sp.Integer(0)] * len(CELLS)
            row[CELLS.index(cell)] = sp.Integer(1)
            rows.append(row)
        region_rows[c] = sp.Matrix(rows)
        atlas[c] = {
            "region rank": region_rows[c].rank(),
            "cap L145": CONE_COORDS - sp.Matrix.vstack(
                region_rows[c], l145).rank(),
            "cap L147": CONE_COORDS - sp.Matrix.vstack(
                region_rows[c], l147).rank(),
            "cap L154": CONE_COORDS - sp.Matrix.vstack(
                region_rows[c], l154).rank(),
            "cap b161 survival set": CONE_COORDS - sp.Matrix.vstack(
                region_rows[c], survival).rank(),
            "cap b162 stratum": CONE_COORDS - sp.Matrix.vstack(
                region_rows[c], stratum).rank(),
        }
    shared_shear_columns = len({
        j for j in range(len(CELLS))
        if any(region_rows[0][i, j] != 0 for i in range(region_rows[0].rows))
        and any(stratum[i, j] != 0 for i in range(stratum.rows))
    })

    covariant_x_trivial = sum(1 for label in X_TRIVIAL
                              if label in b148.COVARIANT_MOVES)
    two_cycle_classes = {}
    for label in INVOL:
        pi = x_map(label)
        two_cycle_classes[(label[2], label[3])] = sum(
            1 for x in range(LX) if pi(x) != x
        )
    multi_field = dict(BENCH)[MULTI_SLICE_ELEMENT]
    label_c1 = next(label for label in X_TRIVIAL
                    if b163.fixed_slice(label) == 1)
    multi_hodge = b145.cover_hodge_from_field(multi_field)
    multi_form = sp.expand(b163.herm(sp.expand(
        b163.selector(b163.half_support(label_c1)).T * DESCENT[label_c1]
        * b145.quotient_action(
            sp.expand(EDGE_DIFF[(1, 2)].subs({SHEAR_T: 0, SHEAR_X: ATLAS_SX})),
            multi_hodge, MASS
        ) * b163.selector(b163.half_support(label_c1))
    )).subs({MASS: 1}))
    multi_quotient = sp.expand(b145.quotient(multi_hodge))
    sheared_free_links = tuple(sorted({
        t for t in range(PHYS_T) for x in range(LX)
        if multi_field[(t, x)][0] != 0
    }))
    shape = (
        atlas,
        {c: atlas[c]["region rank"] for c in atlas},
        covariant_x_trivial,
        sum(1 for label in INVOL
            if label in b148.COVARIANT_MOVES),
        two_cycle_classes,
        guarded_inertia(multi_form),
        multi_quotient.is_diagonal(),
        sheared_free_links,
        (guess_counts[("checker", "full", "fp")],
         guess_counts[("checker", "full", "fn")]),
        (guess_counts[("checker", "sub", "fp")],
         guess_counts[("checker", "sub", "fn")]),
        (guess_counts[("scout", "full", "fp")],
         guess_counts[("scout", "full", "fn")]),
        (guess_counts[("scout", "sub", "fp")],
         guess_counts[("scout", "sub", "fn")]),
        shared_shear_columns,
        CONE_COORDS - stratum.rank(),
        CONE_COORDS - survival.rank(),
    )

    # ---------------------------------------------------------------- E ----
    volumes = {cell: sp.Symbol(f"v_{cell[0]}{cell[1]}", positive=True)
               for cell in CELLS}
    shears = {cell: sp.Symbol(f"g_{cell[0]}{cell[1]}", real=True)
              for cell in CELLS}
    spectrum_sigma_free = 0
    stencil_cells = {}
    for c in range(PHYS_T):
        substitution = {}
        for cell in CELLS:
            substitution[NUMOD[cell]] = volumes[cell]
            substitution[IMOD[cell]] = 1 / volumes[cell]
            pinned = cell[0] in ((c - 1) % PHYS_T, c)
            substitution[AMOD[cell]] = (
                volumes[cell] if pinned
                else volumes[cell] / (1 - shears[cell] ** 2)
            )
            substitution[BMOD[cell]] = (
                sp.Integer(0) if pinned
                else -volumes[cell] * shears[cell] / (1 - shears[cell] ** 2)
            )
        values = [sp.simplify(sp.expand(d_entry(c, x).subs(substitution)))
                  for x in range(LX)]
        if not any(value.free_symbols & (set(shears.values()) | {SHEAR_X})
                   for value in values):
            spectrum_sigma_free += 1
        if c == 1:
            stencil_cells["distinct volumes"] = len(
                {symbol for value in values for symbol in value.free_symbols}
            )
    forced_cells = tuple(sorted({
        (offset % PHYS_T) for offset in (0, -1, 0, -1)
    }))
    d_cell_slices = {
        "nu": 0, "a (past link)": -1, "a (spatial neighbour)": 0,
        "mu (past diagonal)": -1,
    }
    lam = sp.Symbol("lam", positive=True)
    scale = {}
    for cell in CELLS:
        scale[NUMOD[cell]] = lam * volumes[cell]
        scale[AMOD[cell]] = lam * volumes[cell]
        scale[IMOD[cell]] = 1 / (lam * volumes[cell])
    base_d = d_entry(1, 0).subs({
        **{NUMOD[cell]: volumes[cell] for cell in CELLS},
        **{AMOD[cell]: volumes[cell] for cell in CELLS},
        **{IMOD[cell]: 1 / volumes[cell] for cell in CELLS},
    })
    scaled_d = sp.simplify(d_entry(1, 0).subs(scale))
    homogeneous_degrees = tuple(
        degree for degree in range(-3, 4)
        if sp.simplify(scaled_d - lam ** degree * base_d) == 0
    )
    curved_field = dict(BENCH)[CURVED_ELEMENT]
    curved_hodge = b145.cover_hodge_from_field(curved_field)
    curved_form = sp.expand(b163.herm(sp.expand(
        b163.selector(b163.half_support(label_c1)).T * DESCENT[label_c1]
        * b145.quotient_action(
            sp.expand(EDGE_DIFF[(2, 3)].subs({SHEAR_T: 0, SHEAR_X: ATLAS_SX})),
            curved_hodge, MASS
        ) * b163.selector(b163.half_support(label_c1))
    )).subs({MASS: 1}))
    curved_values = tuple(sorted(sp.Rational(curved_form[i, i])
                                 for i in range(LX)))
    conjunction = (
        spectrum_sigma_free,
        d_cell_slices,
        forced_cells,
        stencil_cells.get("distinct volumes", 0),
        homogeneous_degrees,
        sp.simplify(scaled_d),
        curved_values,
        len(set(curved_values)),
        guarded_inertia(curved_form),
        sp.Matrix(curved_form).rank(),
        sp.expand(b145.quotient(curved_hodge)).is_diagonal(),
    )
    exact.append(sum(curved_values))

    # ---------------------------------------------------------------- F ----
    differential_shapes = set()
    for key in EDGE_KEYS:
        for entry in EDGE_DIFF[key]:
            entry = sp.expand(entry)
            if entry == 0:
                continue
            differential_shapes.add((
                affine_in(entry, SHEAR_T),
                affine_in(entry, SHEAR_X),
                sp.expand(entry.subs({SHEAR_T: 0, SHEAR_X: 0})) == 0,
                sp.expand(sp.diff(entry, SHEAR_T, SHEAR_X)) == 0,
            ))
    affine_cells = sum(
        1 for form in pairing_full.values()
        if all(affine_in(entry, SHEAR_T) for entry in form)
    )
    corner_filled = sum(
        1 for form in pairing_full.values()
        if sp.expand(form[LX:HALF, LX:HALF].diff(SHEAR_T)) != zero4
    )
    mass_blind = 0
    corner_exact = 0
    corner_traceless = 0
    corner_pure_shear = 0
    corner_nonzero = 0
    corner_nonzero_slices = collections.Counter()
    corner_free_link = 0
    flat_corner_zero = 0
    flat_c_linear = 0
    region_c_linear = 0
    for label in X_TRIVIAL:
        c = b163.fixed_slice(label)
        pin = {s: 0 for s in local_shears(c)}
        pin_all = {s: 0 for s in SHEAR_SET}
        free = set(free_shears(c))
        for key in EDGE_KEYS:
            region = sp.expand(pairing_full[(label, key)].subs(pin))
            if sp.expand(region[:LX, :LX].diff(SHEAR_T)) == zero4:
                mass_blind += 1
            corner = region[LX:HALF, LX:HALF]
            e_form = sp.expand(corner.diff(SHEAR_T))
            if sp.expand(corner - SHEAR_T * e_form) == zero4 \
                    and SHEAR_T not in e_form.free_symbols:
                corner_exact += 1
            if all(sp.expand(e_form[i, i]) == 0 for i in range(LX)):
                corner_traceless += 1
            if e_form.free_symbols <= SHEAR_SET:
                corner_pure_shear += 1
            if e_form != zero4:
                corner_nonzero += 1
                corner_nonzero_slices[c] += 1
                if e_form.free_symbols <= free:
                    corner_free_link += 1
            block_c = region[:LX, LX:HALF]
            if sp.expand(block_c.subs({SHEAR_T: 0})) == zero4 \
                    and sp.expand(block_c.diff(SHEAR_T)) != zero4:
                region_c_linear += 1
            flat = sp.expand(pairing_full[(label, key)].subs(pin_all))
            if flat[LX:HALF, LX:HALF] == zero4:
                flat_corner_zero += 1
            if sp.expand(flat[:LX, LX:HALF].diff(SHEAR_T)) != zero4:
                flat_c_linear += 1

    # THE TWO BRANCHES, EXHIBITED ON EXPLICIT CONE-ADMISSIBLE CARRIERS.
    curved_probe = {}
    for sign in (1, -1):
        differential = sp.expand(EDGE_DIFF[(2, 3)].subs(
            {SHEAR_T: sign * PROBE_ST, SHEAR_X: ATLAS_SX}
        ))
        form = sp.expand(b163.herm(sp.expand(
            b163.selector(b163.half_support(label_c1)).T * DESCENT[label_c1]
            * b145.quotient_action(differential, curved_hodge, MASS)
            * b163.selector(b163.half_support(label_c1))
        )).subs({MASS: 1}))
        curved_probe[sign] = (
            guarded_inertia(sp.expand(form[LX:HALF, LX:HALF])),
            guarded_inertia(form),
        )
    flat_field = dict(BENCH)[FLAT_REGION_ELEMENT]
    flat_hodge = b145.cover_hodge_from_field(flat_field)
    label_c0 = next(label for label in X_TRIVIAL
                    if b163.fixed_slice(label) == 0)
    flat_probe = {}
    for sign in (1, -1):
        differential = sp.expand(EDGE_DIFF[(2, 3)].subs(
            {SHEAR_T: sign * PROBE_ST, SHEAR_X: ATLAS_SX}
        ))
        form = sp.expand(b163.herm(sp.expand(
            b163.selector(b163.half_support(label_c0)).T * DESCENT[label_c0]
            * b145.quotient_action(differential, flat_hodge, MASS)
            * b163.selector(b163.half_support(label_c0))
        )).subs({MASS: 1}))
        flat_probe[sign] = (
            form[LX:HALF, LX:HALF] == zero4,
            sp.expand(form[:LX, LX:HALF]) != zero4,
            guarded_inertia(form),
        )
    connection = (
        tuple(sorted(differential_shapes)),
        affine_cells,
        corner_filled,
        mass_blind,
        corner_exact,
        corner_traceless,
        corner_pure_shear,
        corner_nonzero,
        tuple(sorted(corner_nonzero_slices)),
        corner_free_link,
        region_c_linear,
        flat_corner_zero,
        flat_c_linear,
        {sign: curved_probe[sign] for sign in curved_probe},
        {sign: flat_probe[sign] for sign in flat_probe},
    )

    # ---------------------------------------------------------------- G ----
    grade = sp.diag(*([1] * LX + [-1] * LX))
    flip_cells = 0
    for form in pairing_zero.values():
        flipped = sp.expand(form.subs(
            {BMOD[cell]: -BMOD[cell] for cell in CELLS}, simultaneous=True
        ))
        if sp.expand(flipped - grade * form * grade) == sp.zeros(HALF, HALF):
            flip_cells += 1
    orientation_cells = sum(
        1 for form in pairing_zero.values()
        if sp.expand(form.subs({MASS: -MASS, SHEAR_X: -SHEAR_X},
                               simultaneous=True) + form)
        == sp.zeros(HALF, HALF)
    )
    orientation_region = 0
    sx_free_region = 0
    edge_blind_region = 0
    for label in X_TRIVIAL:
        c = b163.fixed_slice(label)
        pin = {s: 0 for s in local_shears(c)}
        reference = sp.expand(pairing_zero[(label, EDGE_KEYS[0])].subs(pin))
        for key in EDGE_KEYS:
            region = sp.expand(pairing_zero[(label, key)].subs(pin))
            if sp.expand(region.subs({MASS: -MASS}) + region) == sp.zeros(
                HALF, HALF
            ):
                orientation_region += 1
            if sp.expand(region.diff(SHEAR_X)) == sp.zeros(HALF, HALF):
                sx_free_region += 1
            if sp.expand(region - reference) == sp.zeros(HALF, HALF):
                edge_blind_region += 1
    sx_live_cells = sum(
        1 for form in pairing_zero.values()
        if sp.expand(form.diff(SHEAR_X)) != sp.zeros(HALF, HALF)
    )

    edge_comparisons = 0
    edge_mass_free = 0
    edge_b_changes = 0
    edge_c_changes = 0
    edge_live_labels = 0
    edge_live_pinned = 0
    edge_blind_classes = set()
    for label in INVOL:
        c = b163.fixed_slice(label)
        pin = {s: 0 for s in local_shears(c)}
        reference = pairing_zero[(label, EDGE_KEYS[0])]
        pinned_reference = sp.expand(reference.subs(pin))
        live = False
        live_pinned = False
        for key in EDGE_KEYS[1:]:
            form = pairing_zero[(label, key)]
            difference = sp.expand(form - reference)
            edge_comparisons += 1
            if sp.expand(difference.diff(MASS)) == sp.zeros(HALF, HALF):
                edge_mass_free += 1
            if sp.expand(difference[:LX, :LX]) != zero4:
                edge_b_changes += 1
            if sp.expand(difference[:LX, LX:HALF]) != zero4:
                edge_c_changes += 1
            if difference != sp.zeros(HALF, HALF):
                live = True
            if sp.expand(form.subs(pin) - pinned_reference) != sp.zeros(
                HALF, HALF
            ):
                live_pinned = True
        edge_live_labels += int(live)
        edge_live_pinned += int(live_pinned)
        if not live_pinned:
            edge_blind_classes.add((label[2], label[3]))

    general_field = dict(BENCH)[CURVED_ELEMENT]
    general_dwell = tuple(sorted(
        (dt, dx) for dt in range(PHYS_T) for dx in range(LX)
        if criterion(translate(general_field, dt, dx), label_c1,
                     sp.Integer(1))
    ))
    witness_dwell = tuple(sorted(
        (dt, dx) for dt in range(PHYS_T) for dx in range(LX)
        if criterion(translate(b163.WITNESS_FIELD, dt, dx),
                     b163.WITNESS_LABEL, sp.Integer(1))
    ))
    dwell_closed = all(
        ((a[0] + b[0]) % PHYS_T, (a[1] + b[1]) % LX) in set(witness_dwell)
        for a in witness_dwell for b in witness_dwell
    )
    equivariant = sum(
        1 for dt in range(PHYS_T)
        if criterion(
            translate(general_field, dt, 0),
            next(label for label in X_TRIVIAL
                 if b163.fixed_slice(label) == (1 + dt) % PHYS_T),
            sp.Integer(1),
        )
    )
    riders = (
        flip_cells,
        orientation_cells,
        orientation_region,
        equivariant,
        (len(general_dwell), tuple(sorted({dt for dt, _ in general_dwell}))),
        len(witness_dwell),
        dwell_closed,
        tuple(sorted({dt for dt, _ in witness_dwell})),
        edge_live_labels,
        edge_live_pinned,
        tuple(sorted(edge_blind_classes)),
        (edge_mass_free, edge_comparisons),
        (edge_b_changes, edge_c_changes),
        edge_blind_region,
        sx_free_region,
        sx_live_cells,
    )

    pool = [hq, pairing_zero[(INVOL[0], EDGE_KEYS[0])], witness_form,
            curved_form, multi_form]
    exact_no_float = bool(
        all(no_float(entry) for matrix in pool for entry in matrix)
        and all(no_float(value) for _name, field in BENCH
                for cell in field for value in field[cell])
        and all(no_float(value) for value in exact)
        and all(no_float(value) for value in MASS_GRID)
    )

    return Facts(
        main_head=main_head,
        authority=authority,
        block=block,
        criterion=criterion_facts,
        shape=shape,
        conjunction=conjunction,
        connection=connection,
        riders=riders,
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
    # --- the criterion ------------------------------------------------------
    "hollow_corner",
    "shear_only_in_c",
    "two_cycle_theorem",
    "criterion_stated",
    "incident_links",
    "mass_sign",
    "x_trivial",
    "bench_agreement",
    "b163_reproduced",
    # --- the shape ----------------------------------------------------------
    "open_region",
    "codimension_eight",
    "covariant_empty",
    "multi_slice",
    "prior_guesses",
    "bench_attribution",
    "stratum_meet",
    "non_transverse",
    "atlas_unverified",
    # --- the conjunction, split ---------------------------------------------
    "conjunction_stated",
    "conjunction_split",
    "sigma_locus_only",
    "sigma_forced",
    "hodge_trace",
    "no_volume_average",
    "four_eigenvalues",
    "non_covariant_class",
    "zero_temporal_connection",
    # --- the connection theorem ---------------------------------------------
    "affine_linear",
    "not_perturbative",
    "traceless_corner",
    "pure_shear_corner",
    "nothing_survives",
    "both_signs",
    "connection_credit",
    "checker_measured",
    "two_branches",
    # --- the corrected mechanism and the riders ------------------------------
    "mechanism_quoted",
    "mechanism_struck",
    "edge_zero_mass",
    "edge_blind_from_c",
    "dwell_set",
    "not_a_subgroup",
    "flip_congruence",
    "m_orientation",
    "translation_equivariance",
    "sx_derivative",
    # --- discipline and disclosures -----------------------------------------
    "checker_credit",
    "quoted_then_corrected",
    "nsimplify_flag",
    "repo_flag",
    "inherited_flags",
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
        # --- the criterion --------------------------------------------------
        "hollow_corner": "hollow corner" in note,
        "shear_only_in_c": "shear lives only in `c`" in note
        or "shear lives only in c" in note,
        "two_cycle_theorem": "2-cycle" in note and "traceless" in note,
        "criterion_stated": "the criterion" in note,
        "incident_links": "incident to the fixed slice" in note,
        "mass_sign": "m > 0" in note,
        "x_trivial": "x-trivial" in note,
        "bench_agreement": "8064" in note,
        "b163_reproduced": "64 cells" in note or "64 psd" in note,
        # --- the shape ------------------------------------------------------
        "open_region": "open 24-dimensional" in note,
        "codimension_eight": "codimension 8" in note or "codim 8" in note,
        "covariant_empty": "every covariant reflection" in note
        and "empty" in note,
        "multi_slice": "multi-slice" in note,
        "prior_guesses": "both earlier characterizations" in note
        or "both prior characterizations" in note,
        "bench_attribution": "128 + 128" in note or "128 false-positive" in note,
        "stratum_meet": "dimension 19" in note or "19-dimensional" in note,
        "non_transverse": "non-transverse" in note,
        "atlas_unverified": "not verified by the checker" in note
        or "the checker did not verify" in note,
        # --- the conjunction, split -----------------------------------------
        "conjunction_stated": "the conjunction" in note,
        "conjunction_split": "it splits" in note or "the split" in note,
        "sigma_locus_only": "locus selection" in note
        or "selects the locus" in note,
        "sigma_forced": "forced" in note,
        "hodge_trace": "lattice-hodge trace" in note,
        "four_eigenvalues": "four distinct" in note,
        "non_covariant_class": "not in b148.covariant_moves" in note
        or "is not covariant" in note,
        "zero_temporal_connection": "zero temporal connection" in note,
        # --- the connection theorem ------------------------------------------
        "affine_linear": "affine-linear" in note,
        "not_perturbative": "not a perturbative question" in note,
        "traceless_corner": "traceless" in note,
        "pure_shear_corner": "pure form in the free shears" in note,
        "nothing_survives": "nothing survives switching" in note,
        "both_signs": "both signs" in note,
        "connection_credit": "the connection theorem" in note,
        "checker_measured": "checker-measured" in note,
        "two_branches": "two branches" in note,
        # --- the corrected mechanism and the riders --------------------------
        "mechanism_quoted": "enter only through `s_t`" in note
        or "enter only through s_t" in note,
        "mechanism_struck": "is struck" in note,
        "edge_zero_mass": "carries zero mass" in note,
        "edge_blind_from_c": "follows from `c` = 0" in note
        or "follows from c = 0" in note,
        "dwell_set": "dwell set" in note,
        "not_a_subgroup": "not a subgroup" in note,
        "flip_congruence": "congruence" in note,
        "m_orientation": "p(-m, -s_x) = -p(m, s_x)" in note,
        "translation_equivariance": "equivariant" in note,
        "sx_derivative": "dp/ds_x = 0" in note,
        # --- discipline and disclosures --------------------------------------
        "checker_credit": "checker" in note,
        "quoted_then_corrected": "quoted then corrected" in note,
        "nsimplify_flag": "nsimplify" in note,
        "repo_flag": "flagged for the repo" in note,
        "inherited_flags": "moduli_from_field" in note,
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
        # NEGATIVE key.  The struck wording may not appear anywhere in the note,
        # not even inside a prohibition list, because the gate greps the
        # NORMALIZED note rather than a sentence.
        "no_volume_average": "volume average" not in note,
        # NEGATIVE key.  A block that repairs its parent's open question must
        # not be written up as a priority or originality claim.
        "no_priority_claim": (
            "first positive" not in note
            and "novel" not in note
            and "unprecedented" not in note
        ),
        # The LaTeX rho guard: a line-wrapped \rho leaves a stray "ho_" at the
        # start of a line and silently mangles a modulus name.
        "rho_guard": "\nho_" not in note_text,
    }


N5_FENCE = 'N5: per_element: THE BLOCK THEOREM AT s_t = 0, ON THE FULL 64-MODULUS FAMILY. For every one of the 24 involutive site reflections, every one of the 16 healed edges, symbolic m and symbolic s_x, the half-support site pairing on S = {c, c+1} is EXACTLY [[B, C],[C^T, 0]]: the (c+1,c+1) block is IDENTICALLY ZERO in 384 of 384 cells -- Block 163 had this only on FLAT carriers -- B carries NO shear modulus at all in 384 of 384, and C is a HOMOGENEOUS LINEAR FORM in exactly the EIGHT LOCAL shears {b_{c-1,x}, b_{c,x}} in 384 of 384. The variables separate: SHEAR LIVES ONLY IN C, mass and volume only in B. At s_t = 0 the residue is exactly s_x Ktilde, homogeneous of degree 1 on all 16 edges, whose slice-diagonal blocks are REAL ANTISYMMETRIC -- which is why s_x cancels from B for the x-trivial class (64 of 64) and for no other (320 of 320 s_x-live), while it is live in C in all 384.\nper_site: THE CRITERION, IN CLOSED FORM. A hollow corner forces PSD <=> C = 0 and B >= 0. On every 2-cycle of pi(x) = e_x(x - p_x) the principal 2x2 minor of B is TRACELESS in 1024 of 1024 slots with off-diagonal m(D_x + D_y)/2, and a traceless symmetric 2x2 is PSD only if zero, so m != 0 forces pi = id. Hence PSD AND MASS-CARRYING <=> X-TRIVIAL (e_x, p_x) = (+1,0) AND m > 0 AND sigma = 0 on the TWO TIME LINKS INCIDENT TO THE FIXED SLICE c, cells (c-1,x) and (c,x) -- the other two links FREE. On the region [r Q]_{S,S} = m diag(D(c,.)) (+) 0_4 at inertia (4,4,0), edge-free and s_x-free, with D(t,x) = (nu_{t,x} + a_{t-1,x} + a_{t,x-1} + mu_{t-1,x-1})/4. Verified against direct inertia on 8064 of 8064 cells, 0 disagreements, 448 PSD all at (4,4,0); Block 163\'s 64 cells and its exact witness diag(1,1,1,1,0,0,0,0) reproduced from the criterion with no computation.\nper_mode: THE SHAPE. One OPEN 24-dimensional region of codimension 8 per fixed slice c inside the 32-coordinate cone: 8 shear coordinates pinned to zero, the other 8 free in (-1,1), all 16 volumes free and positive. EVERY COVARIANT REFLECTION HAS AN EMPTY REGION -- none of the 16 covariant involutions is x-trivial, and (+1,2) is fixed-point-free -- so the positive object lives on the NON-COVARIANT class. Multi-slice shear stays PSD: single-slice support is NOT forced. Both earlier characterizations fail in BOTH directions, and their counts are stated at their true bench: Block 163\'s checker guess {c, c+1} costs 128 + 128 cells on the 8064-cell three-mass bench and 64 + 64 on the 2688-cell m = 1 sub-bench; Block 163\'s scout guess {H_q diagonal} x {x-trivial} costs 320 and 96 respectively.\nper_block: THE CONJUNCTION, AND IT SPLITS. On the region spec([r Q]_{S,S}) = {m D(c,x)} U {0,0,0,0}: POSITIVE, MASS-CARRYING at rank 4, and HODGE-TRACE-SENSITIVE -- four distinct positive eigenvalues (79/112, 15/16, 49/48, 6/5) on a cone-admissible genuinely curved element with non-diagonal H_q. That conjunction had not occurred in the lane before. BUT sigma NEVER enters a positive eigenvalue, and that is FORCED rather than observed: the two a-cells and the mu-cell of D(c,x) all sit INSIDE the two pinned link slices, so D is literally sigma-free there. The shear sector is LOCUS SELECTION ONLY -- the recording-rule pattern\'s second appearance -- and D itself is a LATTICE-HODGE TRACE, three volume moduli plus one INVERSE volume modulus on the past-diagonal corner, homogeneous of NO degree under nu -> lambda nu. And the whole object sits at s_t = 0, ZERO TEMPORAL CONNECTION, on a class that is not in b148.COVARIANT_MOVES.\nlattice_wide: THE CONNECTION THEOREM (the independent checker\'s result, checker-measured and RE-VERIFIED here). Every healed differential entry is a s_t + b s_x, so P is EXACTLY AFFINE-LINEAR in s_t in 384 of 384 cells: the question is NOT A PERTURBATIVE QUESTION. On the region dB/ds_t = 0 in 64 of 64 -- the mass block is s_t-blind -- the corner is exactly s_t E with E TRACELESS in 64 of 64 and a PURE FORM IN THE FREE SHEARS in 64 of 64 (no nu, no a, no mu, no m, no s_x), and C is exactly s_t C1 with C1 nonzero in 64 of 64. TWO BRANCHES, both exhibited: where E is nonzero -- exactly the odd fixed slices, 32 of 64 region cells, matching the checker\'s own 192 of 384 corner count -- a nonzero traceless symmetric block is indefinite, so P fails PSD for EITHER SIGN of s_t; where E vanishes the hollow-corner lemma applies at every s_t and C = s_t C1 forces s_t = 0. NOTHING SURVIVES SWITCHING s_t ON, exactly, at every magnitude and both signs.\nRESULT: THE POSITIVE REGION OF THE SITE CLASS EXISTS EXACTLY AT ZERO TEMPORAL CONNECTION, WITH NECESSITY AND SUFFICIENCY IN CLOSED FORM ON BOTH SIDES. Three defects of this block\'s own solve transcript are quoted then corrected: the edge-blindness mechanism is STRUCK -- at s_t = 0 the healing weights are live in 24 of 24 labels and in 16 of 24 even after pinning, the edge dependence carries ZERO MASS in 360 of 360 comparisons and enters only through s_x, so edge-blindness FOLLOWS FROM C = 0 and x-triviality; the two failure counts are re-attached to their true benches; and "stabilizer of order 8" is a category error, {0,3} x Z_4 not being closed under addition -- it is a DWELL SET, and the general element\'s region-preserving translations have order 4.\nDECISION_CUT: THE ARC IS COMPLETE AT THIS FIXTURE AND NOTHING IS REGISTERED, ADOPTED OR PROPOSED. No site reflection is adopted; no premise-class change is registered; no landed note is edited; Block 160 is NOT corrected, Block 162 is NOT corrected and Block 163 is NOT corrected. The riders stand at corrected scope: FLIP is a congruence on the WHOLE s_t = 0 slice (384 of 384), P(-m, -s_x) = -P(m, s_x) identically, the region is translation-EQUIVARIANT with R_c -> R_{c+dt}, and dP/ds_x = 0 on the region to all orders. REMAINING OPEN: the pool-2 handoff items (contract E; the cutting residuals; the signed-flux census); the loci-atlas verification, which the checker did not verify; and any owner-directed continuation. TOOLING: sympy.nsimplify can return an irrational radical form for an exact Rational and silently corrupt exact arithmetic -- flagged for the repo, with the landed chain to be grepped in pool 2; the inherited b145.moduli_from_field float leak and the landed inertia helper\'s singular-input sentinel are carried.\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero.'


# ---------------------------------------------------------------------------
# claims: the only thing a mutation is allowed to touch
# ---------------------------------------------------------------------------
def build_claims(mutation: str) -> dict:
    claims: dict = {
        "main_head": CURRENT_MAIN,
        "parent_pin": "resolved",
        "hollow_corner_cells": CELL_COUNT,
        "covariant_psd_cells": 0,
        "multi_slice_psd": True,
        "checker_guess_full": CHECKER_GUESS_FULL,
        "sigma_in_positive_spectrum": False,
        "d_is_homogeneous": False,
        "max_st_degree": MAX_ST_DEGREE,
        "survives_nonzero_st": False,
        "edge_blind_via_st": False,
        "witness_dwell_is_group": False,
        "required_scope_keys": SCOPE_KEYS,
    }
    if mutation == "stale_main_authority":
        claims["main_head"] = STALE_MAIN
    elif mutation == "stale_parent_authority":
        claims["parent_pin"] = "stale"
    elif mutation == "break_hollow_corner":
        # THE LOAD-BEARING THEOREM DENIED at its true scope: the corner asserted
        # to be zero only on flat carriers, i.e. Block 163's weaker statement,
        # which would dissolve the hollow-corner lemma and the whole criterion
        claims["hollow_corner_cells"] = 0
    elif mutation == "break_criterion":
        # THE CRITERION DENIED: a COVARIANT reflection asserted to own a PSD
        # mass-carrying cell, which the traceless 2-cycle theorem forbids
        # identically in m, s_x, edge and moduli
        claims["covariant_psd_cells"] = 1
    elif mutation == "claim_single_slice_forced":
        # the region asserted to force single-slice shear support, which the
        # explicit two-free-link PSD element denies
        claims["multi_slice_psd"] = False
    elif mutation == "break_bench_attribution":
        # DEFECT 2 RE-INTRODUCED: the m = 1 sub-bench counts asserted of the
        # three-mass 8064-cell bench
        claims["checker_guess_full"] = CHECKER_GUESS_SUB
    elif mutation == "claim_sigma_in_spectrum":
        # THE SPLIT DENIED: shear asserted to enter a positive eigenvalue, which
        # the cell-incidence identity forbids
        claims["sigma_in_positive_spectrum"] = True
    elif mutation == "claim_volume_average":
        # THE STRUCK WORDING ASSERTED: D asserted to be a homogeneous volume
        # functional -- "a volume average" -- which its scaling behaviour denies
        claims["d_is_homogeneous"] = True
    elif mutation == "break_affine_linearity":
        # the exactness result denied: P asserted to carry s_t^2 content, which
        # would put block 165 back into a perturbative census
        claims["max_st_degree"] = 2
    elif mutation == "break_connection_theorem":
        # THE CHECKER'S THEOREM DENIED: something asserted to survive at s_t != 0
        # on the region, against the traceless-E identity and the C = s_t C1
        # branch
        claims["survives_nonzero_st"] = True
    elif mutation == "claim_edge_blind_via_st":
        # DEFECT 1 RE-INTRODUCED: the STRUCK mechanism asserted -- the healing
        # weights asserted to drop out at s_t = 0
        claims["edge_blind_via_st"] = True
    elif mutation == "claim_stabilizer_eight":
        # DEFECT 3 RE-INTRODUCED: the order-8 dwell set asserted to be a group
        claims["witness_dwell_is_group"] = True
    elif mutation == "drop_conjunction_split":
        # the Q3 SPLIT dropped from the note's scope: without these keys the
        # note may read as though shear entered the positive form
        claims["required_scope_keys"] = tuple(
            key for key in SCOPE_KEYS
            if key not in ("conjunction_split", "sigma_locus_only",
                           "sigma_forced", "hodge_trace", "no_volume_average")
        )
    elif mutation == "drop_checker_credit":
        # the connection theorem stripped of its checker attribution
        claims["required_scope_keys"] = tuple(
            key for key in SCOPE_KEYS
            if key not in ("connection_credit", "checker_measured",
                           "checker_credit", "quoted_then_corrected")
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
            "docs/ADMISSIBILITY_DIRAC_KAHLER_ZERO_SHEAR_REGION_BOUNDED_THEOREM_NOTE_2026-08-21.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_REFLECTION_CHANNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md",
            "scripts/admissibility_dirac_kahler_site_reflection_channel_2026_08_21.py",
        )
        and PARENT_ARTIFACTS == (BLOCK163_NOTE, BLOCK163_RUNNER)
        and len(PARENT_ARTIFACT_BLOBS) == len(PARENT_ARTIFACTS) == 2
        and facts.main_head == claims["main_head"]
        and authority.fixed_authority
        and authority.parent_pin_is_commit
        and authority.parent_ref_and_ancestry
        and parent_blobs_ok
    )

    gate_b = bool(
        facts.block[0] == EDGE_COUNT
        and facts.block[1] == HQ_DISPLACEMENTS
        and facts.block[2] == HQ_DISPLACEMENTS
        and facts.block[3] == EDGE_COUNT * PHYS_T
        and facts.block[4] == claims["hollow_corner_cells"]
        and facts.block[5] == CELL_COUNT
        and facts.block[6] == CELL_COUNT
        and facts.block[7] == CELL_COUNT
        and facts.block[8] == (REGION_CELLS, 0)
        and facts.block[9] == CELL_COUNT
        and facts.block[10] == INVOLUTIVE_COUNT
        and facts.exact_no_float
    )

    gate_c = bool(
        facts.criterion[0] == PHYS
        and facts.criterion[1] == CELL_COUNT
        and facts.criterion[2] == (RANK_EIGHT_CELLS, RANK_SEVEN_CELLS)
        and facts.criterion[3] == RANK_SEVEN_CLASSES
        and facts.criterion[4] == (ODD_SHEAR_KERNEL,)
        and facts.criterion[5] == REGION_CELLS
        and facts.criterion[6] == (TWO_CYCLE_SLOTS, TWO_CYCLE_SLOTS,
                                   TWO_CYCLE_SLOTS)
        and facts.criterion[7] == REGION_CELLS
        and facts.criterion[8] == (BENCH_CELLS, BENCH_CELLS, 0, 0)
        and facts.criterion[9] == BENCH_PSD
        and facts.criterion[10] == {BENCH_PSD_INERTIA: BENCH_PSD}
        and sum(facts.criterion[11].values()) == BENCH_CELLS
        and facts.criterion[12] == claims["covariant_psd_cells"]
        and facts.criterion[13] == B163_ST0_PSD == b163.ST0_PSD_CELLS
        and facts.criterion[14] is True
        and facts.criterion[15] == b163.WITNESS_INERTIA
        and facts.criterion[16] is True
        and facts.criterion[17] == SUB_BENCH_CELLS
        and BENCH_CELLS == BENCH_CARRIERS * EDGE_COUNT * INVOLUTIVE_COUNT
        * BENCH_MASSES
        and facts.exact_no_float
    )

    multi_slice_psd = is_psd(facts.shape[5]) and len(facts.shape[7]) > 1
    gate_d = bool(
        all(value["region rank"] == REGION_CODIM
            for value in facts.shape[0].values())
        and all(
            {key: value[key] for key in ATLAS_DIMS} == ATLAS_DIMS
            for value in facts.shape[0].values()
        )
        and CONE_COORDS - REGION_CODIM == REGION_DIM
        # the transversal yardstick, computed rather than quoted -- and then
        # NOT read as significant, because the two loci share shear coordinates
        and facts.shape[13] == B162_STRATUM_DIM
        and facts.shape[14] == B161_SURVIVAL_DIM
        and REGION_DIM + facts.shape[13] - CONE_COORDS == GENERIC_MEET_DIM
        and ATLAS_DIMS["cap b162 stratum"] > GENERIC_MEET_DIM
        and facts.shape[2] == 0
        and facts.shape[3] == COVARIANT_COUNT
        and facts.shape[4][(1, 0)] == 0
        and facts.shape[4][(1, 2)] == LX
        and min(count for key, count in facts.shape[4].items()
                if key != (1, 0)) > 0
        and multi_slice_psd == claims["multi_slice_psd"]
        and facts.shape[5] == BENCH_PSD_INERTIA
        and facts.shape[6] is False
        and facts.shape[8] == claims["checker_guess_full"]
        and facts.shape[9] == CHECKER_GUESS_SUB
        and facts.shape[10] == SCOUT_GUESS_FULL
        and facts.shape[11] == SCOUT_GUESS_SUB
        and facts.shape[12] > 0
    )

    sigma_in_spectrum = facts.conjunction[0] != PHYS_T
    gate_e = bool(
        facts.conjunction[0] == PHYS_T
        and sigma_in_spectrum == claims["sigma_in_positive_spectrum"]
        and set(facts.conjunction[1].values()) == {0, -1}
        and facts.conjunction[2] == (0, 3)
        and facts.conjunction[3] == D_STENCIL_MODULI
        and (len(facts.conjunction[4]) > 0) == claims["d_is_homogeneous"]
        and sp.Symbol("lam", positive=True) in facts.conjunction[5].free_symbols
        and facts.conjunction[6] == REGION_EIGENVALUES
        and facts.conjunction[7] == LX
        and facts.conjunction[8] == BENCH_PSD_INERTIA
        and facts.conjunction[9] == LX
        and facts.conjunction[10] is False
        and facts.exact_no_float
    )

    max_st_degree = 1 if facts.connection[1] == CELL_COUNT else 2
    # THE CONNECTION THEOREM, read as a disjunction of the two exhibited
    # branches: either the corner is a NONZERO traceless block (indefinite for
    # both signs) or it vanishes and C = s_t C1 with C1 nonzero forces s_t = 0.
    survives_nonzero_st = not (
        facts.connection[5] == REGION_CELLS
        and facts.connection[10] == REGION_CELLS
        and all(probe[0][2] > 0 for probe in facts.connection[13].values())
        and all(probe[0] and probe[1] and not is_psd(probe[2])
                for probe in facts.connection[14].values())
    )
    gate_f = bool(
        facts.connection[0] == ((True, True, True, True),)
        and facts.connection[1] == CELL_COUNT
        and max_st_degree == claims["max_st_degree"]
        and facts.connection[2] == CORNER_FILLED_CELLS
        and facts.connection[3] == REGION_CELLS
        and facts.connection[4] == REGION_CELLS
        and facts.connection[5] == REGION_CELLS
        and facts.connection[6] == REGION_CELLS
        and facts.connection[7] == E_NONZERO_CELLS
        and facts.connection[8] == E_ODD_SLICES
        and facts.connection[9] == E_NONZERO_CELLS
        and facts.connection[10] == REGION_CELLS
        and facts.connection[11] == REGION_CELLS
        and facts.connection[12] == REGION_CELLS
        and all(probe[0][2] > 0 and not is_psd(probe[1])
                for probe in facts.connection[13].values())
        and all(probe[0] and probe[1] and not is_psd(probe[2])
                for probe in facts.connection[14].values())
        and survives_nonzero_st == claims["survives_nonzero_st"]
        and facts.exact_no_float
    )

    edge_blind_via_st = facts.riders[8] == 0
    witness_dwell_is_group = facts.riders[6]
    gate_g = bool(
        facts.riders[0] == CELL_COUNT
        and facts.riders[1] == CELL_COUNT
        and facts.riders[2] == REGION_CELLS
        and facts.riders[3] == PHYS_T
        and facts.riders[4] == (GENERAL_DWELL, (0,))
        and facts.riders[5] == WITNESS_DWELL
        and witness_dwell_is_group == claims["witness_dwell_is_group"]
        and facts.riders[7] == (0, 3)
        and facts.riders[8] == EDGE_LIVE_LABELS
        and edge_blind_via_st == claims["edge_blind_via_st"]
        and facts.riders[9] == EDGE_LIVE_AFTER_PINNING
        and facts.riders[10] == EDGE_BLIND_CLASSES
        and facts.riders[11] == (EDGE_COMPARISONS, EDGE_COMPARISONS)
        and facts.riders[12] == (EDGE_B_CHANGES, EDGE_C_CHANGES)
        and facts.riders[13] == REGION_CELLS
        and facts.riders[14] == REGION_CELLS
        and facts.riders[15] == CELL_COUNT
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
    arguments = parser.parse_args()
    mutation = arguments.mutation
    started_ns = time.monotonic_ns()

    # Every measurement happens once, before any mutation flag is consulted, so
    # a mutation can only rewrite a CLAIM.  No gate can cascade into another
    # because no gate feeds a measurement.
    facts = measure()
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
        f"  THE BLOCK THEOREM AT s_t = 0: the residue is exactly s_x Ktilde on "
        f"{facts.block[0]} of {EDGE_COUNT} edges at time displacements "
        f"{facts.block[1]} (H_q likewise {facts.block[2]}), its slice-diagonal "
        f"blocks REAL ANTISYMMETRIC in {facts.block[3]} of "
        f"{EDGE_COUNT * PHYS_T}; the (c+1,c+1) corner is IDENTICALLY ZERO in "
        f"{facts.block[4]} of {CELL_COUNT} cells, B carries no shear in "
        f"{facts.block[5]}, C is a homogeneous linear form in the 8 LOCAL "
        f"shears in {facts.block[7]} with support {facts.block[6]}; s_x is "
        f"absent from B for {facts.block[8]} (x-trivial, other) and live in C "
        f"in {facts.block[9]}; joint (m, s_x) degree-1 homogeneity "
        f"{facts.block[10]} of {INVOLUTIVE_COUNT}"
    )
    print(
        f"  THE CRITERION: D closed form on {facts.criterion[0]} of {PHYS} "
        f"sites; B's mass part = m(D_x + D_pi(x))/2 in {facts.criterion[1]} of "
        f"{CELL_COUNT}; the C-form has ranks {facts.criterion[2]} (rank-7 "
        f"classes {facts.criterion[3]}, kernel {facts.criterion[4]}); the "
        f"x-trivial pure-m entries are the 8 local shears one by one in "
        f"{facts.criterion[5]} of {REGION_CELLS}; 2-cycle minors "
        f"(traceless, massive, slots) {facts.criterion[6]}; the region normal "
        f"form m diag(D_c) (+) 0_4 in {facts.criterion[7]} of {REGION_CELLS}; "
        f"bench (cells, agree, disagree, unresolved) {facts.criterion[8]} with "
        f"{facts.criterion[9]} PSD at inertias {facts.criterion[10]} and "
        f"{facts.criterion[12]} of them covariant; the m = 1 sub-bench is "
        f"{facts.criterion[17]} cells; Block 163's own s_t = 0 bench "
        f"reproduced at {facts.criterion[13]} PSD with the exact witness "
        f"{facts.criterion[14]} at inertia {facts.criterion[15]}, predicted by "
        f"the criterion {facts.criterion[16]}"
    )
    print(f"  bench inertia census: {facts.criterion[11]}")
    print(
        f"  THE SHAPE: the region's pinning rows have rank "
        f"{facts.shape[1]} per fixed slice, so codimension {REGION_CODIM} and "
        f"dimension {REGION_DIM} in the {CONE_COORDS}-coordinate cone; "
        f"{facts.shape[2]} of the {X_TRIVIAL_COUNT} x-trivial labels are in "
        f"b148.COVARIANT_MOVES (which has {facts.shape[3]}), and the 2-cycle "
        f"counts by class are {facts.shape[4]}, so every covariant class and "
        f"(+1,2) die identically; a MULTI-SLICE region element with shear on "
        f"free links {facts.shape[7]} and NON-diagonal H_q ({facts.shape[6]}) "
        f"is PSD at inertia {facts.shape[5]}; the checker guess {{c, c+1}} "
        f"costs (FP, FN) = {facts.shape[8]} on the {BENCH_CELLS}-cell bench "
        f"and {facts.shape[9]} on the {SUB_BENCH_CELLS}-cell m = 1 sub-bench, "
        f"the scout guess {facts.shape[10]} and {facts.shape[11]}"
    )
    for c in sorted(facts.shape[0]):
        print(f"    loci atlas, c = {c}: " + ", ".join(
            f"{key} = {value}" for key, value in facts.shape[0][c].items()
        ))
    print(
        f"    (the b162 stratum has dimension {facts.shape[13]} and the b161 "
        f"survival set {facts.shape[14]}, so the transversal yardstick for the "
        f"stratum meet is {REGION_DIM} + {facts.shape[13]} - {CONE_COORDS} = "
        f"{GENERIC_MEET_DIM}; the region and the stratum share "
        f"{facts.shape[12]} shear coordinates, so the meet is NON-TRANSVERSE by "
        f"construction and the excess is NOT read as significant -- the "
        f"checker's objection, folded; the checker did NOT verify this atlas)"
    )
    print(
        f"  THE CONJUNCTION, SPLIT: D is sigma-free on the region for "
        f"{facts.conjunction[0]} of {PHYS_T} fixed slices -- FORCED, since D's "
        f"four cells sit at time offsets {facts.conjunction[1]} and therefore "
        f"at slices {facts.conjunction[2]} relative to c, all INSIDE the two "
        f"pinned links; {facts.conjunction[3]} distinct volume moduli enter the "
        f"four eigenvalues; D is homogeneous of degrees {facts.conjunction[4]} "
        f"under nu -> lam nu (empty: a LATTICE-HODGE TRACE, not a volume "
        f"average), scaling to {facts.conjunction[5]}; the displayed curved "
        f"element gives {facts.conjunction[7]} distinct eigenvalues "
        f"{facts.conjunction[6]} at rank {facts.conjunction[9]}, inertia "
        f"{facts.conjunction[8]}, H_q diagonal {facts.conjunction[10]}"
    )
    print(
        f"  THE CONNECTION THEOREM (the checker's, re-verified): every healed "
        f"differential entry is a s_t + b s_x {facts.connection[0]}, so P is "
        f"AFFINE-LINEAR in s_t in {facts.connection[1]} of {CELL_COUNT} cells "
        f"and s_t fills the corner in {facts.connection[2]}; on the region "
        f"dB/ds_t = 0 in {facts.connection[3]} of {REGION_CELLS}, the corner is "
        f"exactly s_t E in {facts.connection[4]}, E is TRACELESS in "
        f"{facts.connection[5]} and a PURE SHEAR FORM in {facts.connection[6]}, "
        f"nonzero in {facts.connection[7]} at fixed slices "
        f"{facts.connection[8]} and supported on the FREE links in "
        f"{facts.connection[9]}; C = s_t C1 with C1 nonzero in "
        f"{facts.connection[10]}; on a fully shear-free carrier the corner "
        f"vanishes in {facts.connection[11]} while dC/ds_t is nonzero in "
        f"{facts.connection[12]}"
    )
    print(
        f"    branch 1 (E nonzero), corner inertia and full inertia by sign of "
        f"s_t: {facts.connection[13]}"
    )
    print(
        f"    branch 2 (E zero), (corner vanishes, C nonzero, full inertia) by "
        f"sign of s_t: {facts.connection[14]}"
    )
    print(
        f"  THE RIDERS AT CORRECTED SCOPE: FLIP acts by the congruence "
        f"diag(I_4, -I_4) in {facts.riders[0]} of {CELL_COUNT}; "
        f"P(-m, -s_x) = -P(m, s_x) in {facts.riders[1]}, and on the region "
        f"P(-m) = -P(m) in {facts.riders[2]} of {REGION_CELLS}; the region is "
        f"translation-EQUIVARIANT on {facts.riders[3]} of {PHYS_T} time shifts; "
        f"the general element's DWELL SET is {facts.riders[4]} and Block 163's "
        f"witness's is {facts.riders[5]} at time shifts {facts.riders[7]}, "
        f"which is closed under addition {facts.riders[6]} -- so the order-8 "
        f"object is NOT a subgroup and 'stabilizer' is STRUCK; THE STRUCK "
        f"MECHANISM: at s_t = 0 the edge is live in {facts.riders[8]} of "
        f"{INVOLUTIVE_COUNT} labels and in {facts.riders[9]} even after "
        f"pinning, the edge-blind classes being {facts.riders[10]}, while the "
        f"edge difference carries ZERO MASS in {facts.riders[11]} comparisons "
        f"and changes (B, C) in {facts.riders[12]} of them -- so edge-blindness "
        f"on the region ({facts.riders[13]} of {REGION_CELLS}) follows from "
        f"C = 0, NOT from s_t = 0; dP/ds_x = 0 on the region in "
        f"{facts.riders[14]} of {REGION_CELLS} while s_x is live off it in "
        f"{facts.riders[15]} of {CELL_COUNT}"
    )
    print()

    checks = Checks()
    checks.check(
        "A-authority",
        "main plus TWO parent artifacts are content-bound: Block 163's note and runner, which are BOTH the stack parent this block's branch is cut from AND the content parent whose import chain (b162 -> b161 -> b160 -> b159 -> b156 -> b153 -> b148 -> b147 -> b145 -> b142) carries every committed constructor used here and is pinned by Block 163's own gate A rather than duplicated in this one",
        gate_values["A"],
    )
    checks.check(
        "B-the-block-theorem-at-zero-temporal-connection",
        "AT s_t = 0 THE SITE PAIRING HAS A HOLLOW CORNER ON THE FULL 64-MODULUS FAMILY, AND THE VARIABLES SEPARATE COMPLETELY: for all 24 involutive site reflections, all 16 healed edges, symbolic mass and symbolic s_x, [r Q]_{S,S} on the half support S = {c, c+1} is exactly [[B, C],[C^T, 0]] with the (c+1,c+1) block IDENTICALLY ZERO in 384 of 384 cells -- Block 163 established this only on FLAT carriers and it is a theorem on EVERY carrier here, because at s_t = 0 nothing reaches time distance 2 -- with B carrying NO shear modulus whatsoever in 384 of 384 and C a HOMOGENEOUS LINEAR FORM in exactly the EIGHT LOCAL shear moduli {b_{c-1,x}, b_{c,x}} in 384 of 384, so SHEAR LIVES ONLY IN C while mass and volume live only in B; and the s_x structure that makes this work is measured rather than assumed -- the s_t = 0 residue is EXACTLY s_x times a matrix homogeneous of degree 1 on all 16 edges, with time displacements {0, +-1} matching H_q's, whose SLICE-DIAGONAL blocks are REAL ANTISYMMETRIC on all 16 edges times 4 slices, which is precisely why herm() kills s_x in the mass block for the x-trivial class (64 of 64) and for no other class (320 of 320 s_x-live) while s_x remains live in C in all 384 cells, so Block 163's 's_x drops out identically' is correct only at its own x-trivial scope",
        gate_values["B"],
    )
    checks.check(
        "C-the-criterion-in-closed-form-and-its-8064-cell-verification",
        "THE EXACT CHARACTERIZATION BLOCK 163 LEFT OPEN, IN CLOSED FORM AND WITHOUT A CENSUS: the hollow corner forces PSD <=> C = 0 and B >= 0, since for a symmetric PSD matrix a zero diagonal entry annihilates its whole row; the C = 0 half is solved by the rank of C as a form in the eight local shears -- rank 8 on 256 cells and rank 7 on exactly the 128 cells of the classes (-1,0) and (-1,2), whose kernel is the single reflection-ODD uniform shear profile (1,1,1,1,-1,-1,-1,-1) -- and on the x-trivial class the pure-mass entries of C are the eight local shears ONE BY ONE at +-m/8 in 64 of 64 cells, so there C = 0 <=> all eight local shears vanish for EVERY m != 0 and EVERY s_x with no genericity assumption; the B >= 0 half is solved by the 2-CYCLE THEOREM -- on every 2-cycle of pi(x) = e_x(x - p_x) the principal 2x2 minor of B is TRACELESS in 1024 of 1024 slots with off-diagonal exactly m(D_x + D_y)/2, and a traceless symmetric 2x2 is PSD only if it is zero, which forces m = 0 on the cone -- so B >= 0 with m != 0 <=> pi = id <=> (e_x, p_x) = (+1,0), and there B = m diag(D(c,.)) exactly with D(t,x) = (nu_{t,x} + a_{t-1,x} + a_{t,x-1} + mu_{t-1,x-1})/4 an identity on all 16 quotient sites; HENCE THE CRITERION -- PSD AND MASS-CARRYING <=> X-TRIVIAL AND m > 0 AND sigma = 0 ON THE TWO TIME LINKS INCIDENT TO THE FIXED SLICE, cells (c-1,x) and (c,x) rather than the two SUPPORT slices -- verified against direct congruence inertia on 8064 of 8064 cells (7 cone-admissible carriers x 16 edges x 24 reflections x 3 masses) with ZERO disagreements, ZERO unresolved cells, 448 PSD every one of them at inertia (4,4,0), and ZERO of them at a covariant reflection; and it reproduces Block 163's own 64-cell s_t = 0 count and its exact witness diag(1,1,1,1,0,0,0,0) with NO computation at all",
        gate_values["C"],
    )
    checks.check(
        "D-the-shape-of-the-region-and-both-refuted-guesses-at-their-true-bench",
        "THE REGION IS ONE OPEN 24-DIMENSIONAL SET PER FIXED SLICE AND EVERY COVARIANT REFLECTION'S REGION IS EMPTY: the eight pinning equations sigma_{c-1,x} = sigma_{c,x} = 0 are independent for every c, so the region has codimension 8 and dimension 24 inside the 32-coordinate cone with the other 8 shears free in (-1,1) and all 16 volumes free and positive; NONE of the four x-trivial labels lies in b148.COVARIANT_MOVES, which contains 16 of the 24 involutions, and every non-x-trivial class has at least one 2-cycle -- including (+1,2), which is fixed-point-free -- so the 2-cycle theorem empties all of them and the lane's positive object sits on the NON-COVARIANT class; SINGLE-SLICE SUPPORT IS NOT FORCED, an explicit cone-admissible element with shear on BOTH free links and a NON-diagonal H_q being PSD at inertia (4,4,0); AND BOTH EARLIER CHARACTERIZATIONS ARE REFUTED IN BOTH DIRECTIONS WITH THEIR COUNTS ATTACHED TO THE BENCH THEY WERE MEASURED ON -- Block 163's checker guess {shear-free on c, c+1} costs 128 false-positive and 128 false-negative cells on the three-mass 8064-cell bench and 64 + 64 on the 2688-cell m = 1 sub-bench, and Block 163's scout guess {H_q diagonal} x {x-trivial} costs 320 and 96 respectively, the solve transcript's own figures having been the sub-bench ones throughout; the loci atlas is measured here at dimensions 22, 22, 23, 20 and 19 for every fixed slice, and the excess over the generic transversal value is NOT read as significant, because the region and the Block 162 stratum are cut by OVERLAPPING shear coordinates so non-transversality is the null hypothesis rather than a discovery",
        gate_values["D"],
    )
    checks.check(
        "E-the-conjunction-and-the-split-with-D-named-a-lattice-Hodge-trace",
        "THE FIRST SIMULTANEOUS CONJUNCTION IN THE LANE, AND IT SPLITS THE GEOMETRY IN A WAY THAT MUST BE STATED PLAINLY: on the region the spectrum is exactly {m D(c,x)} u {0,0,0,0}, so the form is POSITIVE, MASS-CARRYING at rank 4, and genuinely sensitive to the recorded geometry -- an explicit cone-admissible, genuinely curved element with NON-diagonal H_q gives FOUR DISTINCT positive eigenvalues (79/112, 15/16, 49/48, 6/5) with 8 distinct volume moduli entering; BUT THE SHEAR SECTOR NEVER ENTERS A POSITIVE EIGENVALUE AND THAT IS FORCED RATHER THAN OBSERVED -- the two a-cells and the mu-cell of D(c,x) sit at time offsets -1 and 0, i.e. INSIDE the two pinned link slices, so a = nu there and mu = 1/nu never carried a shear, and D restricted to the region is literally shear-free for all four fixed slices -- which makes sigma a PURE SELECTION RULE deciding only WHERE positivity holds, the recording-rule pattern's second appearance; AND THE WORDING IS CORRECTED ON THE INDEPENDENT CHECKER'S OBJECTION: D is NOT a volume average, it is a LATTICE-HODGE TRACE of three direct volume moduli plus ONE INVERSE volume modulus on the past-diagonal corner, and under nu -> lam nu it is homogeneous of NO degree at all, which is measured here by exhibiting the scaled form and finding no exponent in [-3, 3] that reproduces it; and the whole object sits at s_t = 0, ZERO TEMPORAL CONNECTION, on a reflection class that is not covariant",
        gate_values["E"],
    )
    checks.check(
        "F-the-connection-theorem-the-checker-measured-and-this-runner-re-verified",
        "THE QUESTION BLOCK 163 HANDED FORWARD AS PERTURBATIVE HAS AN EXACT ANSWER AT EVERY MAGNITUDE AND BOTH SIGNS, AND THE RESULT IS THE INDEPENDENT CHECKER'S: every entry of every healed differential is exactly a s_t + b s_x -- affine in each connection symbol, with no constant term and no cross term -- so the quotient action is degree <= 1 in s_t and the pairing, being linear in it, is EXACTLY AFFINE-LINEAR in s_t in 384 of 384 cells, with s_t genuinely filling the corner in 192 of them; there is no O(s_t^2) and therefore no perturbative census to run; ON THE REGION the mass block is completely s_t-blind (dB/ds_t = 0 in 64 of 64), the corner is EXACTLY s_t E with E TRACELESS in 64 of 64 and a PURE FORM IN THE FREE SHEAR MODULI in 64 of 64 -- no nu, no a, no mu, no mass and no s_x anywhere in it -- and the off-diagonal block is exactly s_t C1 with C1 NONZERO in 64 of 64; THE THEOREM CLOSES IN TWO BRANCHES AND BOTH ARE EXHIBITED ON EXPLICIT CONE-ADMISSIBLE CARRIERS, which REFINES the checker's own statement rather than repeating it: E is nonzero in exactly 32 of the 64 region cells, precisely the ODD fixed slices, which matches the checker's own 192-of-384 corner measurement, and there a nonzero traceless symmetric block has a strictly negative eigenvalue and is a PRINCIPAL SUBMATRIX, so PSD fails for BOTH SIGNS of s_t; while at the even fixed slices E vanishes identically, the hollow-corner lemma applies at EVERY s_t, and C = s_t C1 with C1 nonzero forces s_t = 0 by itself -- so NOTHING IN THE ZERO-SHEAR REGION SURVIVES SWITCHING s_t ON, exactly, and the lane's central pattern now has closed-form necessity AND sufficiency on both sides",
        gate_values["F"],
    )
    checks.check(
        "G-the-corrected-mechanism-the-dwell-set-and-the-riders",
        "THE SOLVE TRANSCRIPT'S EDGE-BLINDNESS MECHANISM IS FALSE AND IS STRUCK, AND THE REPLACEMENT IS MEASURED: the claim that the healing weights enter only through s_t and therefore drop out at s_t = 0 fails outright, since at s_t = 0 the healed edge changes the pairing in 24 of 24 labels and, even after the eight local shears are pinned, in 16 of 24 -- only the classes (+1,0) and (-1,2) go edge-blind -- while the edge dependence carries ZERO MASS in 360 of 360 label-edge comparisons and changes the mass block in 128 of them and the off-diagonal block in 192; so the edge enters ONLY through s_x, which on the x-trivial class lives entirely in C by the closed form B = m diag(D_c), and EDGE-BLINDNESS ON THE REGION (64 of 64) FOLLOWS FROM C = 0 TOGETHER WITH X-TRIVIALITY rather than from s_t = 0; SECOND, 'stabilizer of order 8' is a category error and is STRUCK -- the size-8 set {0,3} x Z_4 of Block 163's witness is measured NOT to be closed under addition and is therefore not a subgroup at all but a DWELL SET, the set of translations that keep a carrier inside the region, and the general element's dwell set has order 4 at time shift 0 only; THIRD, the surviving riders are re-measured at their corrected scope -- FLIP acts on the WHOLE s_t = 0 slice by the congruence diag(I_4, -I_4) in 384 of 384 cells so inertia is FLIP-invariant everywhere and not merely on the region, P(-m, -s_x) = -P(m, s_x) identically in 384 of 384 with P(-m) = -P(m) on the region in 64 of 64 so Block 163's witness flip is a theorem rather than an accident, the region is translation-EQUIVARIANT carrying R_c to R_{c+dt} on all four time shifts, and dP/ds_x = 0 on the region to all orders in 64 of 64 while s_x is live off the region in 384 of 384",
        gate_values["G"],
    )
    checks.check(
        "H-note-scope",
        "the scout discipline stated as a discipline -- every reflection, support and carrier outside the committed four is a registered-premise-class change that is MEASURED and never registered, adopted or proposed -- THE CRITERION stated in closed form with the hollow corner, the shear-only-in-C separation, the traceless 2-cycle theorem, the x-trivial and m > 0 conditions, the two links INCIDENT to the fixed slice, the 8064-cell agreement and Block 163's 64 cells reproduced; THE SHAPE with the open 24-dimensional codimension-8 region, every covariant reflection's region empty, multi-slice shear allowed, both prior guesses' counts at their TRUE bench, the dimension-19 stratum meet stated as NON-TRANSVERSE from shared shear coordinates and the loci atlas disclosed as not verified by the checker; THE CONJUNCTION stated AND SPLIT, with sigma as locus selection only, the split FORCED by cell incidence, D named a LATTICE-HODGE TRACE and the words 'volume average' absent from the note entirely, four distinct eigenvalues displayed, the class named non-covariant and the connection named zero; THE CONNECTION THEOREM carried as a co-equal section with its CHECKER-MEASURED attribution, exact affine-linearity, the statement that this is not a perturbative question, the traceless corner as a pure form in the free shears, both signs, both branches, and 'nothing survives switching s_t on'; THE THREE DEFECTS quoted then corrected -- the struck s_t mechanism replaced by edge dependence carrying zero mass and edge-blindness following from C = 0, the bench re-attribution, and the dwell set that is not a subgroup -- together with the riders at corrected scope, checker credit, the sympy.nsimplify corruption flagged for the repo, the inherited b145.moduli_from_field and inertia-sentinel flags, common-mode and cross-context disclosure, the not-re-verified list, sample scope, the pool-2 items, N1 through N8, the W1 wall, the exact N5 fence, the worker profile, the LaTeX rho guard, and NO priority or originality wording anywhere in the note, not even inside a prohibition list",
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
