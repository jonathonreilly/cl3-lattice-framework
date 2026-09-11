#!/usr/bin/env python3
# Final path: scripts/admissibility_dirac_kahler_annealed_pairing_migration_2026_08_19.py
"""Block 147: the reflection-covariant (annealed) pairing, and where the
Block 145 dichotomy goes when the reflection is allowed to move the background.

Block 145 proved, on the free per-cell carrier family (sigma(t,x), nu(t,x)),
that a LIVE reflection seam and an ATLAS-GLOBALLY HERMITIAN lattice-theta
pairing are mutually exclusive.  Every statement there is QUENCHED: theta is
tested against ONE FIXED carrier, so the Hermiticity defect is a condition ON
THE CARRIER.  This block builds the COVARIANT object instead -- theta transports
the whole background, and the pairing compares the carrier world with the
theta-transported world -- and asks whether the dichotomy survives.  It does,
but it MIGRATES: Hermiticity becomes free and POSITIVITY inherits the wall.

  * THE INDUCED MAP IS FORCED, NOT CHOSEN.  Exactly ONE of the eight signed
    cover lifts of (t,x) -> (7-t,-x) descends to the canonical quotient theta.
    A reflection reverses each 2x2 cell, so it acts on cell corners by the
    ANTIPODAL permutation (0,0) <-> (1,1), (0,1) <-> (1,0) -- uniformly across
    all 32 cover cells -- which forces the cell map R(t,x) = ((2-t) mod 4,
    (3-x) mod 4) and the modulus map theta*: (nu, a, b, 1/nu)(c) ->
    (1/nu, a, b, nu)(Rc).  THE SHEAR MOMENT b DOES NOT FLIP SIGN, the VOLUME
    INVERTS, a is fixed, theta* is an involution, R preserves cell time parity
    (1 -> 1, 3 -> 3, 0 <-> 2) so the seam-visible ODD sector is preserved, and
    P H P^T = H(theta* moduli) holds EXACTLY on all 64 moduli at both the cover
    and the quotient level.  Three perturbations of the map -- b sign-flipped,
    nu not inverted, R replaced by t -> 3-t -- all FAIL the same identity;
  * COVARIANCE SPLITS INTO A FALSE HALF AND A TRUE HALF.  The naive identity
    theta Q[d; c] theta^-1 = +- Q[d; theta*c]^(dagger) matches 0 of 192
    combinations (3 dressings x 16 edges x sign x adjointness).  The HONEST
    identity
        theta Q[d; c] theta^-1 = Q[-theta d theta^-1; theta* c]^dagger
    holds 48/48 EXACTLY, symbolically in the connection fixture (s_x, s_t) and
    on the free 64-modulus family.  The transformed connection is identified in
    closed form: -theta d_i theta^-1 = (r_x r_t) d_{rho(i)}^dagger (r_x r_t)^-1
    for ALL FOUR charts, with rho the chart x-parity swap; the frequently quoted
    "the reflection flips s_t" presentation is GAUGE-DEPENDENT -- in the r_x
    gauge alone charts 0 and 2 need the s_t flip and an overall minus while
    charts 1 and 3 need neither -- so covariance TRANSPORTS THE CONNECTION AND
    THE ATLAS, never the carrier alone;
  * ENSEMBLE HERMITICITY IS FREE.  With d' = -theta d theta^-1 the cross
    relation [theta Q[d'; theta*c]]_{++} = ([theta Q[d; c]]_{++})^dagger holds
    48/48 IDENTICALLY IN THE MODULI, so the annealed pairing
    P_ann = Herm([theta Q]_{++}) is Hermitian with NO condition on the shear.
    The caveat is carried as a CHECKED certificate, not as prose: with the SAME
    d the cross relation fails 48/48, and the quenched pairing itself is
    Hermitian on 0/48 edges on this family (Block 145's reading, reproduced);
  * THE MASS IS LIVE AT CODIMENSION 4.  The ensemble mass Gram
    G = Herm([theta H_q]_{++}) has ZERO DIAGONAL and exactly four off-diagonal
    slots with generators (b30 + b33)/8, (b31 + b32)/8, -(b10 + b13)/8,
    -(b11 + b12)/8.  The modulus -> Gram map has rank 4 (the Gram MATRIX has
    rank 8 generically, a different number that is recorded so the two are never
    confused), against Block 145's rank-8 quenched seam: the mass survives on a
    CODIMENSION-4 locus instead of dying on a codimension-8 one;
  * THE DICHOTOMY MIGRATES TO POSITIVITY.  tr G = 0 identically and G's diagonal
    vanishes identically, so a PSD G is forced to be ZERO (each 2x2 principal
    minor has determinant -g^2), and P_ann is EXACTLY AFFINE in m with
    coefficient G.  Hence P_ann >= 0 at arbitrarily large mass forces G = 0 and
    then the mass drops out of the pairing entirely: A POSITIVE
    REFLECTION-COVARIANT LATTICE-THETA PAIRING IS MASSLESS TOO.  The migration
    locus is the FOUR sums vanishing, NOT all eight odd shears -- witnessed by a
    carrier with G identically zero and a rank-8 QUENCHED seam, on which P_ann
    is m-independent on all sixteen healed edges -- and the no-PSD census finds
    ZERO PSD blocks over 4 carriers x 16 edges x 4 masses; and
  * P_ann IS A THIRD CONVENTION THAT EXTENDS THE SECOND.  It is not the quenched
    theta pairing (not Hermitian on the staircase) and not the X_0 pairing
    (Hermitian but different), yet it COINCIDES with the quenched pairing 48/48
    on Block 145's restoration carrier, where that one is Hermitian.  The
    reflected carrier re-enters the DISPLAYED (sigma, nu) cone only on nu = 1:
    the exact residual is (1 - nu^2)/(nu (sigma^2 - 1)), and (nu, sigma) =
    (2, 1/3) has the non-physical image (1/2, 9/4, -3/4, 2).  Restricted to
    nu = 1, where both ensemble members are physical, the mass Gram, the trace
    identity and the 48/48 ensemble Hermiticity all survive unchanged.

Every scientific comparison below is exact SymPy arithmetic; no floats anywhere;
the integer monotonic clock is used only for the runtime gate.

TOOLING DISCLOSURE: every inertia in this runner is computed by SYMMETRIC
CONGRUENCE, delegated to the committed Block 144 helper (Sylvester's law with
the 2x2 hyperbolic pivot for a zero diagonal), which gate A pins by blob through
the Block 145 import chain.  The Block 142/143 helper counts DISTINCT real roots
and is unsound on these degenerate spectra; it is deliberately not used, and the
calibration diag(1,1,-2,-2,0) is asserted in gate B.

PROVENANCE DISCLOSURE: the 64-modulus linear model, the carrier builders, the
quotient, the action and the half pairing are the COMMITTED Block 145 objects,
imported and not re-derived; this block adds only the reflection theta*, the
transported connection and the annealed convention.

HYPOTHESES, named and not imported: (H1) the OS pairing convention is
[X Q]_{++} on the half carrier {p = 0,1}, exactly as Blocks 142/144/145 used it.
(H2) the ensemble is the two-member reflection orbit {background,
theta* background}, and the ANNEALED form averages the OS form over that orbit
on a single copy of the field space.  (H3) the atlas, the connection fixture and
the Block 141 healing weights are the committed ones; ONLY the carrier and the
reflection move.  (H4) the displayed carrier family is the committed cone
nu > 0, |sigma| < 1, together with its Block 145 linear envelope.
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
EPS = sp.Symbol("epsilon", real=True)

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

import admissibility_dirac_kahler_seam_dichotomy_2026_08_19 as b145

b144 = b145.b144
b143 = b145.b143
b142 = b145.b142
b141 = b145.b141
b137 = b145.b137
b134 = b145.b134
b105 = b145.b105

MASS = b145.MASS


NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_ANNEALED_PAIRING_MIGRATION_"
    "BOUNDED_THEOREM_NOTE_2026-08-19.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
BLOCK145_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SEAM_DICHOTOMY_"
    "BOUNDED_THEOREM_NOTE_2026-08-19.md"
)
BLOCK145_RUNNER = (
    "scripts/admissibility_dirac_kahler_seam_dichotomy_2026_08_19.py"
)
BLOCK141_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_COBOUNDARY_HEALING_FAMILY_"
    "BOUNDED_THEOREM_NOTE_2026-08-19.md"
)
BLOCK141_RUNNER = (
    "scripts/admissibility_dirac_kahler_coboundary_healing_family_2026_08_19.py"
)
PARENT_ARTIFACTS = (
    BLOCK145_NOTE,
    BLOCK145_RUNNER,
    BLOCK141_NOTE,
    BLOCK141_RUNNER,
)

# Deliberately literal: this is the complete audit read surface.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_ANNEALED_PAIRING_MIGRATION_BOUNDED_THEOREM_NOTE_2026-08-19.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SEAM_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-08-19.md",
    "scripts/admissibility_dirac_kahler_seam_dichotomy_2026_08_19.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_COBOUNDARY_HEALING_FAMILY_BOUNDED_THEOREM_NOTE_2026-08-19.md",
    "scripts/admissibility_dirac_kahler_coboundary_healing_family_2026_08_19.py",
)

AUDIT_TIMEOUT_SEC = 600
# The five authority pins below are copied verbatim from the Block 145 runner's
# current values; the landing supervisor refreshes them against origin/main.
CURRENT_MAIN = "29d17653c9c043a74041f070e311f03fce114c0a"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
# This block stacks on Block 146, so the parent branch is Block 146's.
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block146-m-block-measurement-theory-20260819"
)
# Landing supervisor: replace this placeholder with the Block 146 branch tip.
# Until it is a 40-hex commit the pin is resolved through PARENT_REF when that
# ref exists and through HEAD otherwise (the parent branch is not published
# yet); either way the binding is real and verifiable, and the immutable commit
# pin lands with the block.
PARENT_COMMIT = "980029156b2234a708bad85616fe90ade0ed32c8"
# Block 144's tip: a real ancestor that PREDATES the pinned Block 145 note and
# runner, so resolving the parent pin there leaves two of the four artifacts
# absent.  It is the honest stale control FOR THIS PIN SET.  The Block 145 tip
# 1b3e0d9c73a9dde0f123ae705097b809a2c19ed3 -- the parent of Block 146 -- is NOT
# usable as the stale control here: all four pinned artifacts already exist
# there with exactly the worktree blobs, so a pin resolved at it would still
# certify, and the control would be vacuous.  This pin is read ONLY under the
# stale mutation; the baseline gate never requires the stale blobs to match.
STALE_PARENT_COMMIT = "6195b68e4f10ffb41c59d65b7cb90cd1d0791323"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_shear_sign_flip",
    "break_involutivity",
    "break_falsification_control",
    "claim_naive_covariance",
    "break_honest_identity",
    "claim_same_d_hermiticity",
    "break_quenched_control",
    "wrong_mass_generator",
    "wrong_modulus_rank",
    "break_trace_identity",
    "claim_psd_hit",
    "break_third_convention_coincidence",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_shear_sign_flip": "B",
    "break_involutivity": "B",
    "break_falsification_control": "B",
    "claim_naive_covariance": "C",
    "break_honest_identity": "C",
    "claim_same_d_hermiticity": "D",
    "break_quenched_control": "D",
    "wrong_mass_generator": "E",
    "wrong_modulus_rank": "E",
    "break_trace_identity": "F",
    "claim_psd_hit": "F",
    "break_third_convention_coincidence": "G",
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
    commit that predates some of the pinned artifacts.
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
    return b145.zero(matrix)


def zero_simplified(matrix: sp.MatrixBase) -> bool:
    return b145.zero_simplified(matrix)


def congruence_inertia(matrix: sp.MatrixBase) -> tuple[int, int, int]:
    """Exact (n_positive, n_zero, n_negative) WITH multiplicity, by congruence.

    Delegated to the COMMITTED Block 144 helper through the Block 145 import
    chain, so that the tool this block reasons with is exactly the blob gate A
    pins.  b142.inertia / b143.inertia count DISTINCT real roots and are unsound
    on these degenerate spectra; the calibration is asserted in gate B.
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
            len(committed_blobs) == 4
            and all(is_hash(value) for value in committed_blobs)
            and committed_blobs == worktree_blobs
        ),
        bool(
            len(stale_blobs) == 4
            and all(is_hash(value) for value in stale_blobs)
            and stale_blobs == worktree_blobs
        ),
    )


# ---------------------------------------------------------------------------
# the committed model, imported wholesale from Block 145
# ---------------------------------------------------------------------------
SIZE = b145.SIZE                         # 32 cover sites
COVER_T = b145.COVER_T                   # 8
PHYS_T = b145.PHYS_T                     # 4
LX = b145.LX                             # 4
PHYS = b145.PHYS                         # 16 quotient sites
HALF = b145.HALF                         # 8 sites in the positive-time half
ORIGINS = b145.ORIGINS                   # ((0,0),(0,1),(1,0),(1,1))
INDEX = b145.INDEX
PLUS = b145.PLUS
THETA = b145.THETA
X0 = b145.X0
CELLS = b145.CELLS
COORDS = b145.COORDS
EDGE_KEYS = b145.EDGE_KEYS
ODD_SHEAR_COORDS = b145.ODD_SHEAR_COORDS
NU_MODULUS = b145.NU_MODULUS
A_MODULUS = b145.A_MODULUS
B_MODULUS = b145.B_MODULUS
INV_MODULUS = b145.INV_MODULUS
FREE_MODULI = (NU_MODULUS, A_MODULUS, B_MODULUS, INV_MODULUS)
HEALING_WEIGHTS = b145.HEALING_WEIGHTS
ALT_WEIGHTS = b145.ALT_WEIGHTS
UNDRESSED_WEIGHTS = b145.UNDRESSED_WEIGHTS
MINUS_SITES = b145.MINUS_SITES
PLUS_SITES = b145.PLUS_SITES
WEIGHT_SCHEMES = (
    ("healed", HEALING_WEIGHTS),
    ("alt", ALT_WEIGHTS),
    ("undressed", UNDRESSED_WEIGHTS),
)
INVERSE_INDEX = {value: key for key, value in INDEX.items()}


def herm(matrix: sp.MatrixBase) -> sp.Matrix:
    """The Hermitian part.  Everything here is real, so .H is .T."""
    return sp.expand((matrix + matrix.T) / 2)


def half_pair(action: sp.MatrixBase, operator: sp.MatrixBase = None) -> sp.Matrix:
    """[X Q]_{++} on the half carrier {p = 0,1} (H1)."""
    return sp.expand(
        PLUS.T * (THETA if operator is None else operator) * action * PLUS
    )


# ---------------------------------------------------------------------------
# the reflection: derived from the committed geometry, not assumed
# ---------------------------------------------------------------------------
ANTIPODAL_CORNERS = (
    ((0, 0), (1, 1)),
    ((0, 1), (1, 0)),
    ((1, 0), (0, 1)),
    ((1, 1), (0, 0)),
)
SIGNED_LIFT = (7, 0, 1, 0, 0)            # (shift_t, shift_x, overall, a, b)
RHO = {0: 1, 1: 0, 2: 3, 3: 2}           # the chart x-parity swap


def cell_reflect(cell: tuple[int, int]) -> tuple[int, int]:
    """R(t,x) = ((2-t) mod 4, (3-x) mod 4), derived in gate B."""
    return ((2 - cell[0]) % PHYS_T, (3 - cell[1]) % LX)


def derived_cell_data() -> tuple[dict, set]:
    """The cell map and corner permutations forced by (t,x) -> (7-t, -x).

    A reflection reverses each 2x2 cell, so the image of the cell with origin
    (t,x) is the cell with origin (6-t, -1-x) and the four corners are permuted
    among themselves.  Both are read off here rather than assumed.
    """
    cells: dict[tuple[int, int], tuple[int, int]] = {}
    permutations: set = set()
    for time_index in range(COVER_T):
        for space_index in range(LX):
            origin = ((6 - time_index) % COVER_T, (-1 - space_index) % LX)
            corner_map = {}
            for delta_t in (0, 1):
                for delta_x in (0, 1):
                    image_t = (7 - (time_index + delta_t)) % COVER_T
                    image_x = (-(space_index + delta_x)) % LX
                    corner_map[(delta_t, delta_x)] = (
                        (image_t - origin[0]) % COVER_T,
                        (image_x - origin[1]) % LX,
                    )
            cells[(time_index, space_index)] = origin
            permutations.add(tuple(sorted(corner_map.items())))
    return cells, permutations


def theta_star(nu_value, a_value, b_value, inverse_value) -> tuple:
    """theta* on the per-cell moduli: (nu, a, b, 1/nu)(c) -> (1/nu, a, b, nu)(Rc)."""
    out_nu, out_a, out_b, out_inverse = {}, {}, {}, {}
    for cell in CELLS:
        image = cell_reflect(cell)
        out_nu[image] = inverse_value[cell]
        out_a[image] = a_value[cell]
        out_b[image] = b_value[cell]
        out_inverse[image] = nu_value[cell]
    return out_nu, out_a, out_b, out_inverse


def theta_star_variant(
    nu_value, a_value, b_value, inverse_value, flip_b=False, no_inverse=False,
    reflect=None,
) -> tuple:
    """The three falsification controls of gate B, in one place."""
    reflect = reflect or cell_reflect
    out_nu, out_a, out_b, out_inverse = {}, {}, {}, {}
    for cell in CELLS:
        image = reflect(cell)
        out_nu[image] = nu_value[cell] if no_inverse else inverse_value[cell]
        out_a[image] = a_value[cell]
        out_b[image] = -b_value[cell] if flip_b else b_value[cell]
        out_inverse[image] = (
            inverse_value[cell] if no_inverse else nu_value[cell]
        )
    return out_nu, out_a, out_b, out_inverse


def parity_flipped_reflect(cell: tuple[int, int]) -> tuple[int, int]:
    """The control map t -> 3-t: it does NOT preserve cell time parity."""
    return ((3 - cell[0]) % PHYS_T, (3 - cell[1]) % LX)


def modulus_point(field: dict) -> dict:
    """A carrier field as a substitution on the 64 free moduli."""
    nu_value, a_value, b_value, inverse_value = b145.moduli_from_field(field)
    point = {}
    for cell in CELLS:
        point[NU_MODULUS[cell]] = nu_value[cell]
        point[A_MODULUS[cell]] = a_value[cell]
        point[B_MODULUS[cell]] = b_value[cell]
        point[INV_MODULUS[cell]] = inverse_value[cell]
    return point


def reflected_modulus_point(field: dict) -> dict:
    """theta* of a carrier field, as a substitution on the 64 free moduli."""
    nu_value, a_value, b_value, inverse_value = theta_star(
        *b145.moduli_from_field(field)
    )
    point = {}
    for cell in CELLS:
        point[NU_MODULUS[cell]] = nu_value[cell]
        point[A_MODULUS[cell]] = a_value[cell]
        point[B_MODULUS[cell]] = b_value[cell]
        point[INV_MODULUS[cell]] = inverse_value[cell]
    return point


# nu = 1 is exactly where both ensemble members are physical (gate G).
UNIT_VOLUME = {}
for _cell in CELLS:
    UNIT_VOLUME[NU_MODULUS[_cell]] = sp.Integer(1)
    UNIT_VOLUME[INV_MODULUS[_cell]] = sp.Integer(1)


# ---------------------------------------------------------------------------
# the certificate constants this runner is claiming
# ---------------------------------------------------------------------------
SHEAR_SIGN = 1                           # theta* does NOT flip the shear moment
NAIVE_COMBINATIONS = 192                 # 3 dressings x 16 edges x sign x dagger
NAIVE_HITS = 0
COVARIANT_EDGES = 48
CROSS_HERMITIAN_EDGES = 48
SAME_D_FAILURES = 48
QUENCHED_HERMITIAN_EDGES = 0
ANNEALED_EQUALS_HERM_EDGES = 48
NU1_ENSEMBLE_EDGES = 48
RESTORATION_COINCIDENCE = 48
MASS_GRAM_BLOCKS = ((0, 3), (1, 2), (4, 5), (6, 7))
MASS_GRAM_GENERATORS = {
    (0, 3): (B_MODULUS[(3, 0)] + B_MODULUS[(3, 3)]) / 8,
    (1, 2): (B_MODULUS[(3, 1)] + B_MODULUS[(3, 2)]) / 8,
    (4, 5): -(B_MODULUS[(1, 0)] + B_MODULUS[(1, 3)]) / 8,
    (6, 7): -(B_MODULUS[(1, 1)] + B_MODULUS[(1, 2)]) / 8,
}
GRAM_SLOTS = tuple(
    (i, j, MASS_GRAM_GENERATORS[(i, j)]) for (i, j) in MASS_GRAM_BLOCKS
)
MODULUS_MAP_RANK = 4                     # the codimension of the live-mass locus
GRAM_MATRIX_RANK = 8                     # a DIFFERENT number, recorded so the
                                         # two are never confused
GRAM_INERTIA = (4, 0, 4)
QUENCHED_SEAM_RANK = b145.SEAM_INJECTIVE_RANK        # 8, Block 145's codimension
CENSUS_MASSES = (sp.Integer(0), sp.Integer(1), sp.Integer(10), sp.Integer(1000))
CENSUS_PSD_HITS = 0
CENSUS_PROBES = 4 * 16 * 4
SMALL_SHEAR_PROBE = R(1, 7)
NON_PHYSICAL_PROBE = (sp.Integer(2), R(1, 3))        # (nu, sigma)
NON_PHYSICAL_IMAGE = (R(1, 2), R(9, 4), R(-3, 4), sp.Integer(2))
PHYSICAL_VOLUMES = {-1, 1}

# the migration witness: G vanishes identically while the QUENCHED seam is full
# rank, so the migration locus is codimension 4 and is NOT "all odd shears off"
MIGRATION_WITNESS_SHEARS = {0: R(3, 5), 3: R(-3, 5), 1: R(5, 13), 2: R(-5, 13)}
MIGRATION_WITNESS_SEAM_RANK = 8

# the gauge-dependent presentation of the same transport law: in the r_x gauge
# alone, charts 0 and 2 need (overall sign -1, s_t flipped) while charts 1 and 3
# need (+1, unflipped).  The (r_x r_t) gauge needs neither, on all four charts.
RX_GAUGE_PRESENTATION = ((-1, True), (1, False), (-1, True), (1, False))


# ---------------------------------------------------------------------------
# measured facts (computed once, before any mutation flag is consulted)
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Facts:
    main_head: str
    authority: AuthorityCertificate
    # B: the induced map
    inertia_calibration: bool
    corner_permutation_count: int
    corner_permutation_is_antipodal: bool
    derived_cell_map_matches: bool
    lifts_to_theta: tuple
    lift_is_involution: bool
    theta_is_involution: bool
    shear_sign: int
    volume_inverts: bool
    shear_slot_fixed: bool
    theta_star_involutive: bool
    cell_map_involutive: bool
    parity_preserved: bool
    odd_slices_fixed: bool
    even_slices_swapped: bool
    odd_shear_permutation: bool
    cover_covariance: bool
    quotient_covariance: bool
    control_identities: tuple
    # C: the covariance split
    naive_hits: int
    naive_tested: int
    covariant_edges: int
    covariant_tested: int
    clean_transport: bool
    transport_needs_gauge: bool
    rx_gauge_presentation: tuple
    mirror_in_atlas: int
    # D: the ensemble Hermiticity
    cross_hermitian_edges: int
    same_d_failures: int
    quenched_hermitian_edges: int
    annealed_equals_herm_edges: int
    # E: the live mass Gram
    gram_zero_diagonal: bool
    gram_support: tuple
    gram_slots: tuple
    modulus_map_rank: int
    gram_matrix_rank: int
    gram_inertia: tuple
    quenched_seam_rank: int
    # F: the migration theorem
    gram_traceless: bool
    pann_affine_in_mass: bool
    pann_mass_coefficient_is_gram: bool
    psd_forces_zero: bool
    migration_locus_rank: int
    migration_locus_is_not_all_shears: bool
    witness_gram_zero: bool
    witness_seam_rank: int
    witness_mass_free: bool
    census: tuple
    census_psd_hits: int
    census_probes: int
    # G: the third convention and physicality
    restoration_coincidence: int
    restoration_quenched_hermitian: int
    third_convention_distinct: bool
    physicality_residual: sp.Expr
    physicality_roots: frozenset
    non_physical_image: tuple
    non_physical_image_fails: bool
    nu1_gram_unchanged: bool
    nu1_traceless: bool
    nu1_ensemble_edges: int
    # global
    exact_no_float: bool
    scope: dict


def measure() -> Facts:
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

    # --- B: the induced map, derived from the cover geometry ---------------
    derived_cells, corner_permutations = derived_cell_data()
    corner_permutation_is_antipodal = (
        corner_permutations == {tuple(sorted(dict(ANTIPODAL_CORNERS).items()))}
    )
    derived_cell_map_matches = all(
        (
            derived_cells[(time_index, space_index)][0] % PHYS_T,
            derived_cells[(time_index, space_index)][1],
        )
        == cell_reflect((time_index % PHYS_T, space_index))
        for time_index in range(COVER_T)
        for space_index in range(LX)
    )

    lifts_to_theta = tuple(
        (overall, alpha, beta)
        for overall in (1, -1)
        for alpha in (0, 1)
        for beta in (0, 1)
        if (
            lambda descended: descended is not None
            and zero(descended - THETA)
        )(b142.descend(b142.signed_cover_reflection(7, 0, overall, alpha, beta)))
    )
    reflect = b142.signed_cover_reflection(*SIGNED_LIFT)
    lift_is_involution = zero(sp.expand(reflect * reflect - sp.eye(SIZE)))
    theta_is_involution = zero(sp.expand(THETA * THETA - sp.eye(PHYS)))

    starred = theta_star(*FREE_MODULI)
    twice = theta_star(*starred)
    shear_sign = (
        1
        if all(starred[2][cell_reflect(c)] == B_MODULUS[c] for c in CELLS)
        else (
            -1
            if all(starred[2][cell_reflect(c)] == -B_MODULUS[c] for c in CELLS)
            else 0
        )
    )
    volume_inverts = all(
        starred[0][cell_reflect(c)] == INV_MODULUS[c]
        and starred[3][cell_reflect(c)] == NU_MODULUS[c]
        for c in CELLS
    )
    shear_slot_fixed = all(
        starred[1][cell_reflect(c)] == A_MODULUS[c] for c in CELLS
    )
    theta_star_involutive = all(
        twice[slot][c] == FREE_MODULI[slot][c]
        for slot in range(4)
        for c in CELLS
    )
    cell_map_involutive = all(cell_reflect(cell_reflect(c)) == c for c in CELLS)
    parity_preserved = all(
        cell_reflect(c)[0] % 2 == c[0] % 2 for c in CELLS
    )
    odd_slices_fixed = all(
        cell_reflect((t, x))[0] == t for t in (1, 3) for x in range(LX)
    )
    even_slices_swapped = all(
        cell_reflect((t, x))[0] == (2 - t) % PHYS_T
        for t in (0, 2)
        for x in range(LX)
    )
    # on the ODD (seam-visible) slices the shear is permuted by x -> 3-x; the
    # even slices are exchanged 0 <-> 2, so this is NOT an all-cells statement
    odd_shear_permutation = all(
        starred[2][(t, x)] == B_MODULUS[(t, (3 - x) % LX)]
        for t in (1, 3)
        for x in range(LX)
    )

    cover_free = b145.cover_hodge_general(*FREE_MODULI)
    cover_star = b145.cover_hodge_general(*starred)
    hodge_quotient = b145.quotient(cover_free)
    hodge_quotient_star = b145.quotient(cover_star)
    cover_covariance = zero(
        sp.expand(reflect * cover_free * reflect.T) - cover_star
    )
    quotient_covariance = zero(
        sp.expand(THETA * hodge_quotient * THETA.T) - hodge_quotient_star
    )
    control_identities = tuple(
        zero(
            sp.expand(THETA * hodge_quotient * THETA.T)
            - b145.quotient(
                b145.cover_hodge_general(
                    *theta_star_variant(*FREE_MODULI, **keywords)
                )
            )
        )
        for keywords in (
            {"flip_b": True},
            {"no_inverse": True},
            {"reflect": parity_flipped_reflect},
        )
    )

    # --- C: the transported connection, in closed form ---------------------
    shear_x, shear_t = sp.symbols("s_x s_t", real=True, nonzero=True)
    differentials, star_form = b145.connection(shear_x, shear_t)
    flipped_differentials, _ = b145.connection(shear_x, -shear_t)
    lift_t, lift_x = b105.shift_lifts()
    gauge_x = b134.lifted(lift_x)
    gauge = sp.expand(gauge_x * b134.lifted(lift_t))
    gauge_inverse = gauge.inv()
    gauge_x_inverse = gauge_x.inv()

    transported = {
        index: sp.expand(
            -reflect * differentials[INVERSE_INDEX[index]] * reflect
        )
        for index in range(4)
    }
    clean_transport = all(
        zero(
            transported[index]
            - sp.expand(
                gauge * differentials[INVERSE_INDEX[RHO[index]]].H * gauge_inverse
            )
        )
        for index in range(4)
    )
    transport_needs_gauge = all(
        not zero(
            transported[index] - differentials[INVERSE_INDEX[RHO[index]]].H
        )
        for index in range(4)
    )
    rx_gauge_presentation = tuple(
        tuple(
            (sign, flipped)
            for sign in (1, -1)
            for flipped in (False, True)
            if zero(
                transported[index]
                - sign
                * sp.expand(
                    gauge_x
                    * (
                        flipped_differentials if flipped else differentials
                    )[INVERSE_INDEX[RHO[index]]].H
                    * gauge_x_inverse
                )
            )
        )
        for index in range(4)
    )

    # --- the ONE expensive symbolic pass -----------------------------------
    # Everything in gates C, D and G below is read off this pass; nothing is
    # recomputed, and the concrete carriers enter only by substitution.
    restoration_point = modulus_point(
        b145.flat_field(nu01=sp.Integer(2), nu03=sp.Integer(2))
    )
    naive_hits = naive_tested = 0
    covariant_edges = covariant_tested = 0
    cross_hermitian_edges = same_d_failures = 0
    quenched_hermitian_edges = annealed_equals_herm_edges = 0
    restoration_coincidence = restoration_quenched_hermitian = 0
    nu1_ensemble_edges = 0
    healed_blocks: dict = {}
    for name, weights in WEIGHT_SCHEMES:
        table = b145.edge_differentials(differentials, star_form, weights)
        for key in EDGE_KEYS:
            differential = table[key]
            mirror = sp.expand(-reflect * differential * reflect)
            action = b145.quotient_action(differential, cover_free, MASS)
            same_action = b145.quotient_action(differential, cover_star, MASS)
            mirror_action = b145.quotient_action(mirror, cover_star, MASS)
            conjugated = sp.expand(THETA * action * THETA)

            for candidate in (same_action, same_action.H):
                for sign in (1, -1):
                    naive_tested += 1
                    if zero(conjugated - sign * candidate):
                        naive_hits += 1
            covariant_tested += 1
            if zero(conjugated - mirror_action.H):
                covariant_edges += 1

            block = half_pair(action)
            same_block = half_pair(same_action)
            mirror_block = half_pair(mirror_action)
            if zero(mirror_block - block.H):
                cross_hermitian_edges += 1
            if not zero(same_block - block.H):
                same_d_failures += 1
            if zero(block - block.H):
                quenched_hermitian_edges += 1
            annealed = sp.expand((block + mirror_block) / 2)
            if zero(annealed - annealed.H) and zero(annealed - herm(block)):
                annealed_equals_herm_edges += 1

            unit_block = sp.expand(block.xreplace(UNIT_VOLUME))
            unit_mirror = sp.expand(mirror_block.xreplace(UNIT_VOLUME))
            unit_annealed = sp.expand((unit_block + unit_mirror) / 2)
            if (
                zero(unit_mirror - unit_block.H)
                and zero(unit_annealed - unit_annealed.H)
                and zero(unit_annealed - herm(unit_block))
            ):
                nu1_ensemble_edges += 1

            restored = sp.expand(block.xreplace(restoration_point))
            if zero(restored - restored.H):
                restoration_quenched_hermitian += 1
                if zero(herm(restored) - restored):
                    restoration_coincidence += 1

            if name == "healed":
                healed_blocks[key] = block

    mirror_in_atlas = sum(
        1
        for origin in ORIGINS
        if any(
            zero(sp.expand(-reflect * differentials[origin] * reflect) - sign * candidate)
            or zero(
                sp.expand(-reflect * differentials[origin] * reflect)
                - sign * candidate.H
            )
            for sign in (1, -1)
            for candidate in list(differentials.values())
            + list(flipped_differentials.values())
        )
    )

    # --- E: the live mass Gram ---------------------------------------------
    quenched_gram = half_pair(hodge_quotient)
    gram = herm(quenched_gram)
    gram_zero_diagonal = all(
        sp.expand(gram[k, k]) == 0 for k in range(HALF)
    )
    gram_support = tuple(
        sorted(
            {
                (min(i, j), max(i, j))
                for i in range(HALF)
                for j in range(HALF)
                if sp.expand(gram[i, j]) != 0
            }
        )
    )
    # the four pair slots, read off the Gram rather than asserted: the claim is
    # this table, so a wrong generator is a mutation and not a comment
    gram_slots = tuple(
        (i, j, sp.expand(gram[i, j]))
        for (i, j) in gram_support
        if sp.expand(gram[i, j] - gram[j, i]) == 0
    )
    modulus_map_rank = sp.Matrix(
        [
            [sp.expand(gram[i, j]).coeff(value, 1) for value in COORDS]
            for i in range(HALF)
            for j in range(HALF)
        ]
    ).rank()
    gram_matrix_rank = gram.rank()
    gram_inertia = congruence_inertia(
        gram.xreplace({moment: sp.Integer(1) for moment in ODD_SHEAR_COORDS})
    )
    quenched_seam_rank = sp.Matrix(
        [
            [
                sp.expand(hodge_quotient[MINUS_SITES, PLUS_SITES][i, j]).coeff(
                    moment, 1
                )
                for moment in ODD_SHEAR_COORDS
            ]
            for i in range(HALF)
            for j in range(HALF)
        ]
    ).rank()

    # --- F: the migration theorem ------------------------------------------
    gram_traceless = sp.expand(sp.trace(gram)) == 0
    pann_affine_in_mass = True
    pann_mass_coefficient_is_gram = True
    for key in EDGE_KEYS:
        annealed = herm(healed_blocks[key])
        for i in range(HALF):
            for j in range(HALF):
                entry = sp.expand(annealed[i, j])
                if sp.Poly(entry, MASS).degree() > 1:
                    pann_affine_in_mass = False
                if sp.expand(entry.coeff(MASS, 1) - gram[i, j]) != 0:
                    pann_mass_coefficient_is_gram = False
    # a symmetric matrix with a zero diagonal is PSD only if it vanishes: every
    # 2x2 principal minor has determinant -g^2 <= 0, strictly negative unless
    # the generator is zero.  That is the whole "PSD => G = 0" step.
    psd_forces_zero = all(
        sp.expand(
            (gram[i, j] * gram[j, i] - gram[i, i] * gram[j, j])
            - MASS_GRAM_GENERATORS[(i, j)] ** 2
        )
        == 0
        for (i, j) in MASS_GRAM_BLOCKS
    )
    migration_rows = sp.Matrix(
        [
            [sp.expand(value).coeff(moment, 1) for moment in ODD_SHEAR_COORDS]
            for value in MASS_GRAM_GENERATORS.values()
        ]
    )
    migration_locus_rank = migration_rows.rank()
    migration_locus_is_not_all_shears = migration_locus_rank < len(
        ODD_SHEAR_COORDS
    )

    witness_field = {
        cell: (
            MIGRATION_WITNESS_SHEARS[cell[1]] if cell[0] % 2 else sp.Integer(0),
            sp.Integer(1),
        )
        for cell in CELLS
    }
    witness_point = modulus_point(witness_field)
    witness_gram_zero = zero(sp.expand(gram.xreplace(witness_point)))
    witness_quotient = b145.quotient(b145.cover_hodge_from_field(witness_field))
    witness_seam_rank = witness_quotient[MINUS_SITES, PLUS_SITES].rank()
    witness_mass_free = all(
        zero(
            sp.expand(
                herm(sp.expand(healed_blocks[key].xreplace(witness_point))).diff(
                    MASS
                )
            )
        )
        for key in EDGE_KEYS
    )

    # --- F: the no-PSD census on concrete carriers -------------------------
    fixture_differentials, fixture_star = b145.connection(b134.S_X, b134.S_T)
    fixture_edges = b145.edge_differentials(
        fixture_differentials, fixture_star, HEALING_WEIGHTS
    )
    staircase_field = b105.overlap_field()
    staircase_moduli = b145.moduli_from_field(staircase_field)
    small_shear_field = {
        cell: ((EPS if cell[0] % 2 else sp.Integer(0)), sp.Integer(1))
        for cell in CELLS
    }
    census_carriers = (
        ("staircase", b145.cover_hodge_general(*staircase_moduli)),
        (
            "staircase-reflected",
            b145.cover_hodge_general(*theta_star(*staircase_moduli)),
        ),
        ("b145-witness", b145.cover_hodge_from_field(b145.witness_field())),
        ("small-shear", b145.cover_hodge_from_field(small_shear_field)),
    )
    census = []
    census_psd_hits = 0
    census_probes = 0
    for label, carrier in census_carriers:
        carrier_quotient = b145.quotient(carrier)
        carrier_gram = herm(half_pair(carrier_quotient))
        probe = {EPS: SMALL_SHEAR_PROBE} if carrier_gram.has(EPS) else {}
        inertias = set()
        for key in EDGE_KEYS:
            annealed = herm(
                half_pair(
                    b145.quotient_action(fixture_edges[key], carrier, MASS)
                )
            )
            for mass in CENSUS_MASSES:
                census_probes += 1
                block = sp.expand(annealed.subs(MASS, mass)).xreplace(probe)
                inertia = congruence_inertia(block)
                inertias.add(inertia)
                if inertia[2] == 0 and inertia[0] > 0:
                    census_psd_hits += 1
        census.append(
            (
                label,
                sp.expand(sp.trace(carrier_gram)) == 0,
                not zero_simplified(carrier_gram),
                congruence_inertia(carrier_gram.xreplace(probe)),
                tuple(sorted(inertias)),
            )
        )
    census = tuple(census)

    # --- G: the third convention and physicality ---------------------------
    staircase_action = b145.quotient_action(
        fixture_edges[(2, 3)],
        b145.cover_hodge_general(*staircase_moduli),
        MASS,
    )
    staircase_block = half_pair(staircase_action)
    staggered_block = half_pair(staircase_action, X0)
    third_convention_distinct = bool(
        not zero(staircase_block - staircase_block.H)
        and not zero(herm(staircase_block) - staircase_block)
        and not zero(herm(staircase_block) - staggered_block)
        and zero(staggered_block - staggered_block.H)
    )

    volume_symbol, shear_symbol = sp.symbols("nu sigma", real=True)
    local_a = volume_symbol / (1 - shear_symbol ** 2)
    local_b = -volume_symbol * shear_symbol / (1 - shear_symbol ** 2)
    image = (1 / volume_symbol, local_a, local_b, volume_symbol)
    forced_volume = image[0]
    forced_shear = sp.simplify(-image[2] / image[1])
    physicality_residual = sp.simplify(
        sp.together(image[1] - forced_volume / (1 - forced_shear ** 2))
    )
    physicality_roots = frozenset(
        sp.solve(sp.Eq(sp.numer(sp.together(physicality_residual)), 0),
                 volume_symbol)
    )
    non_physical_image = tuple(
        sp.simplify(
            slot.subs(
                {
                    volume_symbol: NON_PHYSICAL_PROBE[0],
                    shear_symbol: NON_PHYSICAL_PROBE[1],
                }
            )
        )
        for slot in image
    )
    non_physical_image_fails = (
        sp.simplify(
            non_physical_image[1]
            - non_physical_image[0]
            / (1 - (-non_physical_image[2] / non_physical_image[1]) ** 2)
        )
        != 0
    )
    unit_gram = sp.expand(gram.xreplace(UNIT_VOLUME))
    nu1_gram_unchanged = zero(unit_gram - gram)
    nu1_traceless = sp.expand(sp.trace(unit_gram)) == 0

    exact_no_float = no_float(
        (
            hodge_quotient,
            hodge_quotient_star,
            gram,
            quenched_gram,
            tuple(healed_blocks.values()),
            witness_quotient,
            physicality_residual,
            tuple(non_physical_image),
            tuple(transported.values()),
            gauge,
        )
    )

    return Facts(
        main_head=main_head,
        authority=authority,
        inertia_calibration=inertia_calibration,
        corner_permutation_count=len(corner_permutations),
        corner_permutation_is_antipodal=corner_permutation_is_antipodal,
        derived_cell_map_matches=derived_cell_map_matches,
        lifts_to_theta=lifts_to_theta,
        lift_is_involution=lift_is_involution,
        theta_is_involution=theta_is_involution,
        shear_sign=shear_sign,
        volume_inverts=volume_inverts,
        shear_slot_fixed=shear_slot_fixed,
        theta_star_involutive=theta_star_involutive,
        cell_map_involutive=cell_map_involutive,
        parity_preserved=parity_preserved,
        odd_slices_fixed=odd_slices_fixed,
        even_slices_swapped=even_slices_swapped,
        odd_shear_permutation=odd_shear_permutation,
        cover_covariance=cover_covariance,
        quotient_covariance=quotient_covariance,
        control_identities=control_identities,
        naive_hits=naive_hits,
        naive_tested=naive_tested,
        covariant_edges=covariant_edges,
        covariant_tested=covariant_tested,
        clean_transport=clean_transport,
        transport_needs_gauge=transport_needs_gauge,
        rx_gauge_presentation=rx_gauge_presentation,
        mirror_in_atlas=mirror_in_atlas,
        cross_hermitian_edges=cross_hermitian_edges,
        same_d_failures=same_d_failures,
        quenched_hermitian_edges=quenched_hermitian_edges,
        annealed_equals_herm_edges=annealed_equals_herm_edges,
        gram_zero_diagonal=gram_zero_diagonal,
        gram_support=gram_support,
        gram_slots=gram_slots,
        modulus_map_rank=modulus_map_rank,
        gram_matrix_rank=gram_matrix_rank,
        gram_inertia=gram_inertia,
        quenched_seam_rank=quenched_seam_rank,
        gram_traceless=gram_traceless,
        pann_affine_in_mass=pann_affine_in_mass,
        pann_mass_coefficient_is_gram=pann_mass_coefficient_is_gram,
        psd_forces_zero=psd_forces_zero,
        migration_locus_rank=migration_locus_rank,
        migration_locus_is_not_all_shears=migration_locus_is_not_all_shears,
        witness_gram_zero=witness_gram_zero,
        witness_seam_rank=witness_seam_rank,
        witness_mass_free=witness_mass_free,
        census=census,
        census_psd_hits=census_psd_hits,
        census_probes=census_probes,
        restoration_coincidence=restoration_coincidence,
        restoration_quenched_hermitian=restoration_quenched_hermitian,
        third_convention_distinct=third_convention_distinct,
        physicality_residual=physicality_residual,
        physicality_roots=physicality_roots,
        non_physical_image=non_physical_image,
        non_physical_image_fails=non_physical_image_fails,
        nu1_gram_unchanged=nu1_gram_unchanged,
        nu1_traceless=nu1_traceless,
        nu1_ensemble_edges=nu1_ensemble_edges,
        exact_no_float=exact_no_float,
        scope=scope_certificate(raw_note()),
    )


# ---------------------------------------------------------------------------
# H. note scope
# ---------------------------------------------------------------------------
# PLACEHOLDER FENCE.  The landing supervisor replaces this string with the
# note's own eight-line N5 fence, byte for byte; until then H-note-scope is the
# single failing gate and the runner exits 1.
N5_FENCE = 'N5: per_element: THE INDUCED MAP, forced rather than chosen: the cover lift t -> 7-t, x -> -x is the UNIQUE signed lift descending to the canonical theta, the overall minus arising from the ANTIPERIODIC WRAP, and it reverses every 2x2 cell, carrying the cell-origin 0-form corner onto the far 2-form corner -- the ANTIPODAL corner permutation -- so on cells it is R(t,x) = ((2-t) mod 4, (3-x) mod 4) and on the per-cell moduli it is the exact involution theta*: (nu, a, b, 1/nu)(c) -> (1/nu, a, b, nu)(Rc), in which THE SHEAR MOMENT DOES NOT FLIP SIGN and THE VOLUME INVERTS; R PRESERVES cell time parity (1 -> 1, 3 -> 3, 0 <-> 2), so the seam-visible ODD-slice shear maps to odd-slice shear by b_{t,x} -> b_{t,3-x} and is PERMUTED, NOT MIXED with the invisible even sector; theta* is involutive with eight free 2-orbits, and the Hodge transforms COVARIANTLY under it on ALL 64 MODULI, at cover and at quotient level alike\nper_site: THE COVARIANCE SPLIT: the naive same-atlas identity theta Q_c theta^{-1} = +-Q_{theta*c}^{(dagger)} FAILS 0/192 across both x-centrings, both connection signs, both adjointness options, both overall signs and all sixteen edges, while the HONEST covariance theta Q[d; c] theta^{-1} = Q[-theta d theta^{-1}; theta*c]^dagger is EXACT 48/48 on the free 64-modulus family at the healed weights, at the control weights and for the UNDRESSED atlas, so the reflection transports the CARRIER, THE CONNECTION AND THE ATLAS TOGETHER and NEVER THE CARRIER ALONE; the connection transport reads in clean form -theta d_i theta^{-1} = (r_x r_t) d_{rho(i)}(s_x, s_t)^dagger (r_x r_t)^{-1} for all four charts under the chart involution rho = {0: 1, 1: 0, 2: 3, 3: 2}, with NO s_t FLIP and NO SIGN in that gauge -- the "s_t flips" reading is PRESENTATION-DEPENDENT and both presentations are displayed -- and the mirror connection lies OUTSIDE the committed four-chart table, 0/4, so the mirror atlas is not the atlas\nper_mode: THE ENSEMBLE HERMITICITY, with the quenched exclusion BROKEN: with the reflected ensemble member carrying the TRANSFORMED connection d\' = -theta d theta^{-1}, cross-Hermiticity [theta Q_2]_++ = ([theta Q_1]_++)^dagger holds 48/48 IDENTICALLY IN THE MODULI, so the annealed pairing P_ann = Herm([theta Q]_++) is HERMITIAN WITH NO SHEAR CONDITION WHATSOEVER -- against a QUENCHED CONTROL of 0/48 for the Block 145 pairing on the same free family, and against FALSE 48/48 if the reflected member is given the SAME connection d instead of d\', so the full background transport is LOAD-BEARING and a weaker ensemble does not inherit the result; the DOUBLED swap-theta form [[0,A],[B,0]] is also Hermitian but HYPERBOLIC BY CONSTRUCTION, inertia (r, 2(8-r), r) with r = rank B, so the ANNEALED average on one copy is the live convention\nper_block: THE LIVE MASS: the ensemble mass Gram G = Herm([theta H_q]_++) has ZERO DIAGONAL STRUCTURALLY and support exactly the four pair slots (0,3), (1,2), (4,5), (6,7) with generators (b30+b33)/8, (b31+b32)/8, -(b10+b13)/8, -(b11+b12)/8; the MODULUS-TO-GRAM MAP has RANK 4 over the eight odd moments while the GRAM MATRIX itself has RANK 8 at a generic carrier -- two DISTINCT quantities, kept apart -- so the ensemble mass VANISHES only on the CODIMENSION-4 locus b30+b33 = b31+b32 = b10+b13 = b11+b12 = 0, against the quenched theorem\'s CODIMENSION-8 locus where all eight odd moments vanish; the quenched dead-seam stratum is STRICTLY CONTAINED in it, so every carrier Block 145 called massless is massless here too and a four-parameter family the parent could not use is now mass-carrying AND Hermitian\nlattice_wide: THE MIGRATION THEOREM: tr Herm([theta H_q]_++) = 0 IDENTICALLY on the free family and P_ann = m G + P_ann(0) is EXACTLY AFFINE in m, so positive semidefiniteness at arbitrarily large m forces G >= 0, the structural zero diagonal and the vanishing trace then force G = 0, and there P_ann is m-INDEPENDENT: A POSITIVE ANNEALED LATTICE-THETA PAIRING IS MASSLESS TOO, so the Block 145 dichotomy MIGRATES from Hermiticity to positivity -- the covariant escape genuinely breaks the Hermiticity/mass exclusion and THE WALL REAPPEARS ONE LEVEL UP; the no-PSD census records ZERO positive-semidefinite occurrences on the staircase, its theta* reflection, the Block 145 witness and a small-shear symbolic carrier at masses 0, 1, 10 and 1000, each carrying a NONZERO TRACELESS G of inertia (4,0,4); P_ann is a THIRD convention that coincides with the quenched theta pairing EXACTLY on Block 145\'s Hermiticity locus, verified on that block\'s restoration carrier, so it EXTENDS Block 145 and NEVER CONTRADICTS it, while theta*(carrier) is a physical (sigma, nu) member IFF nu = 1 -- the exact residual condition, with an explicit non-physical image displayed -- elsewhere lying inside the Block 145 LINEAR ENVELOPE where all that block\'s theorems live, and restricted to nu = 1, where BOTH members are physical, the mass Gram, the trace identity and the ensemble Hermiticity are UNCHANGED\nRESULT: on the displayed Block 105 atlas at s_x = 3/5, s_t = 4/5 with symbolic m, executing the owner\'s 2026-08-19 suggestion that the shear be treated as a VARIABLE rather than a fixed setting -- reflected or averaged rather than frozen, the quenched-versus-annealed distinction -- the two-member reflection ensemble built from the UNIQUE signed lift makes the ANNEALED lattice-theta pairing HERMITIAN IDENTICALLY IN THE MODULI with NO shear condition, against 0/48 for the quenched convention on the same family, and keeps the MASS LIVE off a CODIMENSION-4 locus against the quenched CODIMENSION-8, so BLOCK 145\'S HERMITICITY/MASS EXCLUSION IS GENUINELY BROKEN and the parent\'s third-convention item is discharged in the affirmative at the level of Hermiticity; but tr Herm([theta H_q]_++) = 0 IDENTICALLY and P_ann is exactly AFFINE in m, so POSITIVITY AT ARBITRARILY LARGE m FORCES THE ENSEMBLE MASS GRAM TO VANISH AND THE MASS THEN DROPS OUT EXACTLY -- A POSITIVE ANNEALED LATTICE-THETA PAIRING IS MASSLESS TOO -- and the census finds ZERO PSD occurrences on four carriers at four masses with inertia (4,0,4) throughout, so THE DICHOTOMY MIGRATES FROM HERMITICITY TO POSITIVITY and the wall reappears one level up; the new convention EXTENDS Block 145 rather than contradicting it, agreeing with the quenched pairing exactly on that block\'s Hermiticity locus, and the reflected member is a physical (sigma, nu) carrier iff nu = 1 while always lying inside the Block 145 linear envelope, the nu = 1 restriction leaving every certificate unchanged; all inertias are computed by EXACT SYMMETRIC CONGRUENCE and the distinct-real-root helper is never called\nDECISION_CUT: build DYNAMICAL-SHEAR ENSEMBLES BEYOND TWO MEMBERS, since the migration is proved for the two-member reflection orbit with a frozen ensemble law and a larger or dynamical ensemble is the only place left where the annealed mass could survive positivity; DECIDE THE SHEAR\'S GAUGE CLASSIFICATION -- physics or bookkeeping -- since the s_t-flip presentation is gauge-dependent and the answer changes what the ensemble average means; register BOUNDARY AND DEFECT COMPLETIONS as premises and execute them rather than importing them; execute the JOINT-LANE PROGRAM; curved OS is not decided\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero'


SCOPE_KEYS = (
    "induced_map_sign",
    "induced_map_volume",
    "induced_map_parity",
    "honest_covariance",
    "transformed_connection_caveat",
    "ensemble_hermiticity",
    "live_mass_codimension",
    "migration",
    "traceless",
    "census_no_psd",
    "third_convention",
    "physicality",
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
        "induced_map_sign": "does not flip" in note or "no sign flip" in note,
        "induced_map_volume": "volume inverts" in note,
        "induced_map_parity": "antipodal" in note or "parity" in note,
        "honest_covariance": "transports" in note
        and ("connection" in note or "never the carrier alone" in note),
        "transformed_connection_caveat": "d' =" in note
        or "transformed connection" in note,
        "ensemble_hermiticity": "no shear condition" in note
        or "identically in the moduli" in note,
        # Whitespace-insensitive so the note may hyphenate either way.
        "live_mass_codimension": "codimension-4" in compact
        or "codim-4" in compact,
        "migration": "migrates" in note and "positivity" in note,
        "traceless": "traceless" in note,
        "census_no_psd": "zero psd" in note or "no psd" in note,
        "third_convention": "extends" in note and "coincides" in note,
        "physicality": "nu = 1" in note,
        "provenance": (
            "owner's" in note
            or "quenched-vs-annealed" in note
            or "annealed" in note
        ),
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
        "shear_sign": SHEAR_SIGN,
        "theta_star_involutive": True,
        "control_identities": (False, False, False),
        "naive_hits": NAIVE_HITS,
        "covariant_edges": COVARIANT_EDGES,
        "same_d_failures": SAME_D_FAILURES,
        "quenched_hermitian_edges": QUENCHED_HERMITIAN_EDGES,
        "gram_slots": GRAM_SLOTS,
        "modulus_map_rank": MODULUS_MAP_RANK,
        "gram_traceless": True,
        "census_psd_hits": CENSUS_PSD_HITS,
        "restoration_coincidence": RESTORATION_COINCIDENCE,
        "required_scope_keys": SCOPE_KEYS,
    }
    if mutation == "stale_main_authority":
        claims["main_head"] = STALE_MAIN
    elif mutation == "stale_parent_authority":
        claims["parent_pin"] = "stale"
    elif mutation == "claim_shear_sign_flip":
        claims["shear_sign"] = -SHEAR_SIGN
    elif mutation == "break_involutivity":
        claims["theta_star_involutive"] = False
    elif mutation == "break_falsification_control":
        claims["control_identities"] = (True, False, False)
    elif mutation == "claim_naive_covariance":
        claims["naive_hits"] = NAIVE_COMBINATIONS
    elif mutation == "break_honest_identity":
        claims["covariant_edges"] = COVARIANT_EDGES - 1
    elif mutation == "claim_same_d_hermiticity":
        claims["same_d_failures"] = 0
    elif mutation == "break_quenched_control":
        claims["quenched_hermitian_edges"] = 48
    elif mutation == "wrong_mass_generator":
        claims["gram_slots"] = tuple(
            (i, j, -value if (i, j) == (4, 5) else value)
            for i, j, value in GRAM_SLOTS
        )
    elif mutation == "wrong_modulus_rank":
        claims["modulus_map_rank"] = MODULUS_MAP_RANK + 1
    elif mutation == "break_trace_identity":
        claims["gram_traceless"] = False
    elif mutation == "claim_psd_hit":
        claims["census_psd_hits"] = CENSUS_PSD_HITS + 1
    elif mutation == "break_third_convention_coincidence":
        claims["restoration_coincidence"] = RESTORATION_COINCIDENCE - 1
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
            "docs/ADMISSIBILITY_DIRAC_KAHLER_ANNEALED_PAIRING_MIGRATION_BOUNDED_THEOREM_NOTE_2026-08-19.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_SEAM_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-08-19.md",
            "scripts/admissibility_dirac_kahler_seam_dichotomy_2026_08_19.py",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_COBOUNDARY_HEALING_FAMILY_BOUNDED_THEOREM_NOTE_2026-08-19.md",
            "scripts/admissibility_dirac_kahler_coboundary_healing_family_2026_08_19.py",
        )
        and PARENT_ARTIFACTS
        == (BLOCK145_NOTE, BLOCK145_RUNNER, BLOCK141_NOTE, BLOCK141_RUNNER)
        and facts.main_head == claims["main_head"]
        and authority.fixed_authority
        and authority.parent_ref_and_ancestry
        and parent_blobs_ok
    )

    gate_b = bool(
        facts.inertia_calibration
        and facts.corner_permutation_count == 1
        and facts.corner_permutation_is_antipodal
        and facts.derived_cell_map_matches
        and facts.lifts_to_theta == ((1, 0, 0),)
        and facts.lift_is_involution
        and facts.theta_is_involution
        and facts.shear_sign == claims["shear_sign"]
        and facts.volume_inverts
        and facts.shear_slot_fixed
        and facts.theta_star_involutive == bool(claims["theta_star_involutive"])
        and facts.cell_map_involutive
        and facts.parity_preserved
        and facts.odd_slices_fixed
        and facts.even_slices_swapped
        and facts.odd_shear_permutation
        and facts.cover_covariance
        and facts.quotient_covariance
        and facts.control_identities == tuple(claims["control_identities"])
        and facts.exact_no_float
    )

    gate_c = bool(
        facts.naive_hits == claims["naive_hits"]
        and facts.naive_tested == NAIVE_COMBINATIONS
        and facts.covariant_edges == claims["covariant_edges"]
        and facts.covariant_tested == COVARIANT_EDGES
        and facts.clean_transport
        and facts.transport_needs_gauge
        and facts.rx_gauge_presentation
        == tuple((entry,) for entry in RX_GAUGE_PRESENTATION)
        and facts.mirror_in_atlas == 0
        and facts.exact_no_float
    )

    gate_d = bool(
        facts.cross_hermitian_edges == CROSS_HERMITIAN_EDGES
        and facts.annealed_equals_herm_edges == ANNEALED_EQUALS_HERM_EDGES
        and facts.same_d_failures == claims["same_d_failures"]
        and facts.quenched_hermitian_edges == claims["quenched_hermitian_edges"]
        and facts.exact_no_float
    )

    claimed_slots = tuple(claims["gram_slots"])
    slots_agree = bool(
        len(facts.gram_slots) == len(claimed_slots)
        and all(
            measured[:2] == claimed[:2]
            and sp.expand(measured[2] - claimed[2]) == 0
            for measured, claimed in zip(facts.gram_slots, claimed_slots)
        )
    )
    gate_e = bool(
        facts.gram_zero_diagonal
        and facts.gram_support == MASS_GRAM_BLOCKS
        and slots_agree
        and facts.modulus_map_rank == claims["modulus_map_rank"]
        and facts.gram_matrix_rank == GRAM_MATRIX_RANK
        and facts.gram_inertia == GRAM_INERTIA
        and facts.quenched_seam_rank == QUENCHED_SEAM_RANK
        and facts.modulus_map_rank < facts.quenched_seam_rank
        and facts.exact_no_float
    )

    gate_f = bool(
        facts.gram_traceless == bool(claims["gram_traceless"])
        and facts.pann_affine_in_mass
        and facts.pann_mass_coefficient_is_gram
        and facts.psd_forces_zero
        and facts.migration_locus_rank == MODULUS_MAP_RANK
        and facts.migration_locus_is_not_all_shears
        and facts.witness_gram_zero
        and facts.witness_seam_rank == MIGRATION_WITNESS_SEAM_RANK
        and facts.witness_mass_free
        and facts.census_probes == CENSUS_PROBES
        and facts.census_psd_hits == claims["census_psd_hits"]
        and len(facts.census) == 4
        and all(
            traceless and nonzero and inertia == GRAM_INERTIA
            for _, traceless, nonzero, inertia, _ in facts.census
        )
        and facts.exact_no_float
    )

    gate_g = bool(
        facts.restoration_coincidence == claims["restoration_coincidence"]
        and facts.restoration_quenched_hermitian == RESTORATION_COINCIDENCE
        and facts.third_convention_distinct
        and facts.physicality_roots == PHYSICAL_VOLUMES
        and sp.simplify(
            facts.physicality_residual
            * (
                sp.Symbol("nu", real=True)
                * (sp.Symbol("sigma", real=True) ** 2 - 1)
            )
            - (1 - sp.Symbol("nu", real=True) ** 2)
        )
        == 0
        and facts.non_physical_image == NON_PHYSICAL_IMAGE
        and facts.non_physical_image_fails
        and facts.nu1_gram_unchanged
        and facts.nu1_traceless
        and facts.nu1_ensemble_edges == NU1_ENSEMBLE_EDGES
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
        and elapsed_ns <= 900 * 1_000_000_000
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
    mutation = parser.parse_args().mutation
    started_ns = time.monotonic_ns()

    # Every measurement happens once, before any mutation flag is consulted,
    # so a mutation can only rewrite a CLAIM.  No gate can cascade into
    # another because no gate feeds a measurement.
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
            raise AssertionError(
                "mutation did not fail exactly its own gate"
            )

    checks = Checks()
    checks.check(
        "A-authority",
        "main plus the committed Block 145 note/runner and Block 141 note/runner artifacts are content-bound",
        gate_values["A"],
    )
    checks.check(
        "B-induced-map",
        "exactly one signed cover lift of (t,x)->(7-t,-x) descends to the canonical theta and is an involution; a reflection permutes cell corners ANTIPODALLY ((0,0)<->(1,1), (0,1)<->(1,0)) uniformly on all 32 cover cells, forcing R(t,x)=((2-t)%4,(3-x)%4) and theta*: (nu,a,b,1/nu)(c)->(1/nu,a,b,nu)(Rc) with the shear b UNCHANGED IN SIGN, the volume INVERTED and a fixed; R and theta* are involutions, cell time parity is preserved (1->1, 3->3, 0<->2) so the odd seam sector is permuted by x->3-x; P H P^T = H(theta* moduli) is exact on all 64 moduli at the cover and the quotient level; and the three perturbed maps (b sign-flipped, nu not inverted, t->3-t) all FAIL that identity",
        gate_values["B"],
    )
    checks.check(
        "C-covariance-split",
        "the naive same-atlas identity theta Q[d;c] theta^-1 = +-Q[d;theta*c]^(dagger) matches 0/192 combinations, while the honest identity theta Q[d;c] theta^-1 = Q[-theta d theta^-1; theta*c]^dagger holds 48/48 exactly, symbolically in (s_x,s_t) and on the free 64-modulus family; the transported connection is (r_x r_t) d_{rho(i)}^dagger (r_x r_t)^-1 on all four charts, the gauge is not removable, the s_t-flip presentation is gauge-dependent ((-1,flip),(+1,none),(-1,flip),(+1,none) in the r_x gauge), and the mirror atlas is in the atlas for 0/4 charts",
        gate_values["C"],
    )
    checks.check(
        "D-ensemble-hermiticity",
        "with d' = -theta d theta^-1 the cross relation [theta Q[d';theta*c]]_{++} = ([theta Q[d;c]]_{++})^dagger holds 48/48 IDENTICALLY IN THE MODULI and the annealed average equals Herm([theta Q]_{++}) on all 48, so P_ann is Hermitian with no shear condition; the caveat is a checked certificate, not prose -- with the SAME d the cross relation fails 48/48 and the quenched theta pairing is Hermitian on 0/48 edges of this family",
        gate_values["D"],
    )
    checks.check(
        "E-live-mass-gram",
        "the ensemble mass Gram Herm([theta H_q]_{++}) has structurally zero diagonal and exactly four pair slots (0,3),(1,2),(4,5),(6,7) with generators (b_30+b_33)/8, (b_31+b_32)/8, -(b_10+b_13)/8, -(b_11+b_12)/8; the modulus->Gram map has rank 4 -- the codimension of the live-mass locus -- against Block 145's rank-8 quenched seam, while the Gram MATRIX has rank 8 generically (a different number, recorded so the two are never confused) and its generic inertia is (4,0,4)",
        gate_values["E"],
    )
    checks.check(
        "F-migration-theorem",
        "tr Herm([theta H_q]_{++}) = 0 identically and P_ann is exactly affine in m with coefficient G, while every 2x2 principal minor of G has determinant -g^2, so PSD forces G=0 and the mass then drops out: a positive reflection-covariant lattice-theta pairing is massless too; the migration locus has rank 4 and is NOT 'all eight odd shears off', witnessed by an exact carrier with G identically zero, quenched seam rank 8 and m-independent P_ann on all 16 healed edges; and the census finds 0 PSD blocks over 256 probes (staircase, its reflection, the Block 145 witness and the small-shear carrier, 16 edges, masses 0,1,10,1000), every carrier Gram being nonzero, traceless and of inertia (4,0,4)",
        gate_values["F"],
    )
    checks.check(
        "G-third-convention",
        "P_ann coincides with the quenched theta pairing 48/48 on Block 145's restoration carrier, where that one is Hermitian 48/48, yet it is a genuinely THIRD convention -- on the staircase the quenched pairing is not Hermitian, P_ann differs from it and from the (Hermitian) X_0 pairing; the reflected carrier is a physical (sigma,nu) member exactly when nu^2=1, the exact residual being (1-nu^2)/(nu(sigma^2-1)) with the displayed non-physical image (1/2,9/4,-3/4,2) at (nu,sigma)=(2,1/3); and restricting to nu=1 leaves the mass Gram, the trace identity and the 48/48 ensemble Hermiticity unchanged",
        gate_values["G"],
    )
    checks.check(
        "H-note-scope",
        "the forced induced map with its unflipped shear, inverted volume and antipodal/parity reading, the honest covariance that transports the connection, the transformed-connection caveat, the unconditional ensemble Hermiticity, the codimension-4 live mass, the migration to positivity with its traceless step, the no-PSD census, the third convention that extends and coincides, the nu=1 physicality, the quenched-vs-annealed provenance, the cross-context disclosure, the firewalls and the exact N5 fence are present",
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
