#!/usr/bin/env python3
# Final path: scripts/admissibility_dirac_kahler_general_migration_theorem_2026_08_20.py
"""Block 148: the GENERAL migration theorem, and the one escape it opens.

Block 147 proved, for the TWO-MEMBER reflection ensemble {c, theta* c} carrying
the honestly transported connection, that the annealed lattice-theta pairing is
Hermitian identically in the moduli while its mass Gram
G = Herm([theta H_q]_{++}) has a STRUCTURALLY ZERO DIAGONAL and vanishing trace,
so a POSITIVE annealed pairing is MASSLESS.  Its named next question was whether
a LARGER orbit average escapes that verdict.  It does not -- and the reason is
stronger and more embarrassing for the parent's argument than expected:

  * THE ORBIT IS 64 OF 128, AND THE CHARACTERISATION IS A SUPPORT ARGUMENT.
    All 128 affine cover moves (t,x) -> (e_t t + p, e_x x + q) descend through
    the antiperiodic quotient, but the cover Hodge of the free 64-modulus family
    carries its off-diagonal weight on the DIAGONAL BOND alone -- the bond
    directions are exactly (1,3) and (7,1) -- so a move with e_t != e_x carries
    that bond onto an antidiagonal one and LEAVES THE FAMILY.  Exactly the 64
    moves with e_t = e_x act, they form a group of order 64 acting on carriers
    through order 32 with kernel {id, four-step time shift}, and the induced map
    is a cell relabelling with nu <-> 1/nu on a reflection and NO sign anywhere.
    The ANTIPERIODIC time translation T_AP -- the object the name suggests --
    does NOT descend for any j != 0; it is the PLAIN cover shift that descends,
    and four of its steps descend to -I, which is the antiperiodic wrap.  The
    half-swapping translations are NOT involutions, so they are not OS
    reflections and the pairing convention cannot be built from them;
  * THE MIGRATION CORE IS AN IDENTITY, SO NO ENSEMBLE ESCAPES IT.  diag
    Herm([theta H_q(y)]_{++}) = 0 holds IDENTICALLY IN THE 64 MODULI y, and the
    Gram is LINEAR in y.  A weighted ensemble average is a convex combination of
    substitution instances of one identity, so it inherits the zero diagonal
    whatever the ensemble is -- group orbit or not, symmetric or not, two members
    or sixty-four.  With a zero diagonal every 2x2 principal minor is -g^2, so
    PSD forces the averaged Gram to vanish and the mass drops out: THE BLOCK 147
    VERDICT HOLDS FOR ARBITRARY ENSEMBLES.  Hermiticity itself needs the
    ensemble to be theta-closed AND to carry the transported connection: three
    non-closed controls (partners dropped, weights not theta-symmetric, the SAME
    connection on both members) all fail, as checked certificates;
  * THE ESCAPE IS REAL, AND IT IS THE ODD-CENTRED REFLECTION.  Of the eight
    honest OS reflections in the group -- half-swapping and involutive -- the
    four with an EVEN x-centring (canonical theta among them) have the
    structurally zero diagonal Block 147 used, while the four with an ODD
    x-centring DO NOT: theta' = (-1, 7, -1, 1) has an exact physical-cone
    carrier on which Herm([theta' H_q]_{++}) = diag(15/64, 0, 15/64, 0, 0,
    15/64, 0, 15/64), inertia (4, 4, 0) -- POSITIVE SEMIDEFINITE, NONZERO,
    RANK 4.  BLOCK 147'S MECHANISM GENUINELY FAILS THERE, and this runner says
    so rather than hiding it;
  * AND YET THE ESCAPE CLOSES, BY A STRICTLY STRONGER ROUTE.  On the HERMITIAN
    PART A = (P + P^dagger)/2 -- the only object PSD is a statement about -- the
    diagonal is EXACTLY m diag G, and diag G still has FOUR structural zeros.
    PSD then forces those four ROWS to vanish, an over-determined linear system
    in the eight odd shear moments whose normal determinant is
        det(M^T M) = (s_t^2 + s_x^2)^6 (4 m^2 + s_t^2 + s_x^2)^2 / 2^48
    on every chart-0/1 edge (and the pooled 4-edge system agrees up to 2^-32),
    a STRICTLY POSITIVE quantity for every real m and every nonzero fixture, so
    the system has rank 8 at every mass.  All eight odd shears die, G = 0,
    diag A = 0, and a PSD matrix with zero diagonal is zero: A POSITIVE
    ODD-CENTRED PAIRING IS IDENTICALLY ZERO.  That is stronger than the parent's
    "massless", and it is reached without the parent's step;
  * THE X_0 CONVENTION IS BLOCKED FOR A DIFFERENT, CONE-DEPENDENT REASON.
    [X_0 H_q]_{++} has EIGHT PAIRWISE DISTINCT diagonal entries, each a
    four-term sum of VOLUME moduli, four with a plus and four with a minus, and
    its off-diagonal support is four disjoint 2x2 blocks {0,7}, {2,5} (both
    slots positive) and {1,4}, {3,6} (both negative).  IN THE CONE the blocks
    are DEFINITE and the inertia is (4,0,4) at every carrier, at every orbit
    member and at the uniform ensemble average.  THE CONE PREMISE IS
    LOAD-BEARING and is carried as two checked counterexamples, not as prose:
    a linear-envelope point with the SAME diagonal signs but an oversized shear
    gives (3,0,5), and one with sign-flipped volume moduli gives (8,0,0); and
  * THE ODD-CENTRED REFLECTION IS THE BARE ONE.  Its transported connection
    lands on the committed four-chart table with NO gauge dressing at all, on
    all four charts, while canonical theta needs r_x or r_x r_t and has ZERO
    bare hits.  Bareness alone is not a characterisation -- sixteen pure
    translations are bare too -- so the uniqueness claimed here is uniqueness
    AMONG THE OS REFLECTIONS, and it is stated that way.

Every scientific comparison below is exact SymPy arithmetic; no floats anywhere;
the integer monotonic clock is used only for the runtime gate.

TOOLING DISCLOSURE: every inertia in this runner is computed by SYMMETRIC
CONGRUENCE, delegated to the committed Block 144 helper (Sylvester's law with
the 2x2 hyperbolic pivot for a zero diagonal) through the Block 147/145 import
chain, so the tool this block reasons with is exactly the blob gate A pins.  The
Block 142/143 helper counts DISTINCT real roots and is unsound on these
degenerate spectra; it is deliberately not used, and the calibration
diag(1,1,-2,-2,0) is asserted in gate B.

PROVENANCE DISCLOSURE: the 64-modulus carrier model, the cover Hodge, the
antiperiodic quotient, the action law, the half pairing, the connection data,
the Block 141 healing weights, the canonical theta, the staggered parity X_0,
the descent routine and the reflection theta* are all COMMITTED objects (Blocks
105/134/137/141/142/143/144/145/147), imported and never re-derived.  This block
adds only the affine move family, the general ensemble average, the odd-centred
escape and its closure, and the bare-atlas classification.

HYPOTHESES, named and not imported: (H1) the pairing convention is [X Q]_{++} on
the half carrier {p = 0,1}, exactly as Blocks 142/144/145/147 used it.  (H2) an
ENSEMBLE is a finite family of carriers with nonnegative weights summing to one,
each member carrying its own honestly transported connection; a THETA-CLOSED
ensemble is one whose support and weights are invariant under composing with the
reflection.  (H3) the atlas, the connection fixture and the Block 141 healing
weights are the committed ones; ONLY the carrier and the move vary.  (H4) the
displayed carrier family is the committed cone nu > 0, |sigma| < 1 together with
its Block 145 linear envelope; every sign statement is quantified over the CONE
and gate F carries the envelope counterexamples that show the difference.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import random
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

import admissibility_dirac_kahler_annealed_pairing_migration_2026_08_19 as b147

b145 = b147.b145
b144 = b147.b144
b143 = b147.b143
b142 = b147.b142
b141 = b147.b141
b137 = b147.b137
b134 = b147.b134
b105 = b147.b105

MASS = b147.MASS


NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_GENERAL_MIGRATION_THEOREM_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
BLOCK147_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_ANNEALED_PAIRING_MIGRATION_"
    "BOUNDED_THEOREM_NOTE_2026-08-19.md"
)
BLOCK147_RUNNER = (
    "scripts/admissibility_dirac_kahler_annealed_pairing_migration_2026_08_19.py"
)
BLOCK145_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SEAM_DICHOTOMY_"
    "BOUNDED_THEOREM_NOTE_2026-08-19.md"
)
BLOCK145_RUNNER = (
    "scripts/admissibility_dirac_kahler_seam_dichotomy_2026_08_19.py"
)
PARENT_ARTIFACTS = (
    BLOCK147_NOTE,
    BLOCK147_RUNNER,
    BLOCK145_NOTE,
    BLOCK145_RUNNER,
)

# Deliberately literal: this is the complete audit read surface.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_GENERAL_MIGRATION_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_ANNEALED_PAIRING_MIGRATION_BOUNDED_THEOREM_NOTE_2026-08-19.md",
    "scripts/admissibility_dirac_kahler_annealed_pairing_migration_2026_08_19.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SEAM_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-08-19.md",
    "scripts/admissibility_dirac_kahler_seam_dichotomy_2026_08_19.py",
)

AUDIT_TIMEOUT_SEC = 600
# The five authority pins below are copied verbatim from the Block 147 runner's
# current values; the landing supervisor refreshes them against origin/main.
CURRENT_MAIN = "29d17653c9c043a74041f070e311f03fce114c0a"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
# This block stacks on Block 147, so the parent branch is Block 147's.
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block147-annealed-pairing-migration-20260819"
)
# Landing supervisor: replace this placeholder with the Block 147 branch tip.
# Until it is a 40-hex commit the pin is resolved through PARENT_REF when that
# ref exists and through HEAD otherwise (the parent branch may not be published
# yet); either way the binding is real and verifiable, and the immutable commit
# pin lands with the block.
PARENT_COMMIT = "7cc1175d087f8aca09471c25acab5fab40350994"
# Block 146's tip: a real ancestor that PREDATES the pinned Block 147 note and
# runner, so resolving the parent pin there leaves two of the four artifacts
# ABSENT.  It is the honest stale control FOR THIS PIN SET -- the Block 145 tip
# would NOT be, since two of the four artifacts already carry the worktree blobs
# there and a pin resolved at it would still certify on them.  This pin is read
# ONLY under the stale mutation; the baseline gate never requires the stale
# blobs to match.
STALE_PARENT_COMMIT = "980029156b2234a708bad85616fe90ade0ed32c8"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "wrong_orbit_count",
    "claim_antiperiodic_descends",
    "break_honest_identity",
    "break_diagonal_identity",
    "claim_non_closed_hermitian",
    "claim_even_centring_live",
    "wrong_forcing_determinant",
    "claim_massless_but_nonzero",
    "claim_envelope_validity",
    "wrong_block_signs",
    "claim_theta_is_bare",
    "claim_translations_not_bare",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "wrong_orbit_count": "B",
    "claim_antiperiodic_descends": "B",
    "break_honest_identity": "C",
    "break_diagonal_identity": "D",
    "claim_non_closed_hermitian": "D",
    "claim_even_centring_live": "E",
    "wrong_forcing_determinant": "E",
    "claim_massless_but_nonzero": "E",
    "claim_envelope_validity": "F",
    "wrong_block_signs": "F",
    "claim_theta_is_bare": "G",
    "claim_translations_not_bare": "G",
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
    return b147.zero(matrix)


def zero_simplified(matrix: sp.MatrixBase) -> bool:
    return b147.zero_simplified(matrix)


def congruence_inertia(matrix: sp.MatrixBase) -> tuple[int, int, int]:
    """Exact (n_positive, n_zero, n_negative) WITH multiplicity, by congruence.

    Delegated to the COMMITTED Block 144 helper through the Block 147/145 import
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
# the committed model, imported wholesale through Block 147
# ---------------------------------------------------------------------------
SIZE = b147.SIZE                         # 32 cover sites
COVER_T = b147.COVER_T                   # 8
PHYS_T = b147.PHYS_T                     # 4
LX = b147.LX                             # 4
PHYS = b147.PHYS                         # 16 quotient sites
HALF = b147.HALF                         # 8 sites in the positive-time half
ORIGINS = b147.ORIGINS                   # ((0,0),(0,1),(1,0),(1,1))
INDEX = b147.INDEX
PLUS = b147.PLUS
THETA = b147.THETA
X0 = b147.X0
CELLS = b147.CELLS
COORDS = b147.COORDS
EDGE_KEYS = b147.EDGE_KEYS
ODD_SHEAR_COORDS = b147.ODD_SHEAR_COORDS
NU_MODULUS = b147.NU_MODULUS
A_MODULUS = b147.A_MODULUS
B_MODULUS = b147.B_MODULUS
INV_MODULUS = b147.INV_MODULUS
FREE_MODULI = b147.FREE_MODULI
HEALING_WEIGHTS = b147.HEALING_WEIGHTS
WEIGHT_SCHEMES = b147.WEIGHT_SCHEMES
VOLUME_COORDS = frozenset(
    list(NU_MODULUS.values())
    + list(A_MODULUS.values())
    + list(INV_MODULUS.values())
)
SHEAR_COORDS = frozenset(B_MODULUS.values())

SHEAR_X, SHEAR_T = sp.symbols("s_x s_t", real=True, nonzero=True)


def herm(matrix: sp.MatrixBase) -> sp.Matrix:
    """The Hermitian part; delegated to the committed Block 147 helper."""
    return b147.herm(matrix)


def half_pair(action: sp.MatrixBase, operator: sp.MatrixBase = None) -> sp.Matrix:
    """[X Q]_{++} on the half carrier {p = 0,1} (H1)."""
    return sp.expand(
        PLUS.T * (THETA if operator is None else operator) * action * PLUS
    )


# ---------------------------------------------------------------------------
# the affine lattice moves, built from the committed cover indexing
# ---------------------------------------------------------------------------
ALL_MOVES = tuple(
    (time_sign, time_shift, space_sign, space_shift)
    for time_sign in (1, -1)
    for time_shift in range(COVER_T)
    for space_sign in (1, -1)
    for space_shift in range(LX)
)
COVARIANT_MOVES = tuple(label for label in ALL_MOVES if label[0] == label[2])


def move_permutation(label: tuple) -> dict:
    """(t,x) -> (e_t t + p, e_x x + q) as a site permutation of the cover."""
    time_sign, time_shift, space_sign, space_shift = label
    return {
        b134.cover_index(t, x): b134.cover_index(
            time_sign * t + time_shift, space_sign * x + space_shift
        )
        for t in range(COVER_T)
        for x in range(LX)
    }


def move_matrix(permutation: dict) -> sp.Matrix:
    matrix = sp.zeros(SIZE)
    for source, target in permutation.items():
        matrix[target, source] = 1
    return matrix


def conjugate(matrix: sp.Matrix, permutation: dict) -> sp.Matrix:
    """g M g^T for a permutation g, by index relabelling (no matrix product)."""
    out = sp.zeros(SIZE, SIZE)
    for i in range(SIZE):
        row = permutation[i]
        for j in range(SIZE):
            value = matrix[i, j]
            if value != 0:
                out[row, permutation[j]] = value
    return out


def compose_labels(left: tuple, right: tuple) -> tuple:
    """left after right, in the (e_t, p, e_x, q) coordinates."""
    return (
        left[0] * right[0],
        (left[0] * right[1] + left[1]) % COVER_T,
        left[2] * right[2],
        (left[2] * right[3] + left[3]) % LX,
    )


def theta_compose(label: tuple) -> tuple:
    """theta . g, with theta the canonical (-1, 7, -1, 0)."""
    return compose_labels(THETA_LABEL, label)


def cell_map(label: tuple):
    """The induced 2x2-cell map, read off the cover geometry.

    A translation carries the cell with origin c to the cell with origin
    c + (p, q).  A reflection REVERSES each cell, so the cell-origin 0-form
    corner is carried onto the far 2-form corner and the image cell's origin is
    the image of the (1,1) corner: c -> (p - 1 - t, q - 1 - x).  At
    (e, p, q) = (-1, 7, 0) this reproduces Block 147's committed
    R(t,x) = ((2-t) mod 4, (3-x) mod 4).
    """
    time_sign, time_shift, _, space_shift = label
    if time_sign == 1:
        return lambda c: (
            (c[0] + time_shift) % PHYS_T,
            (c[1] + space_shift) % LX,
        )
    return lambda c: (
        (time_shift - 1 - c[0]) % PHYS_T,
        (space_shift - 1 - c[1]) % LX,
    )


def induced_tables(label: tuple, tables: tuple) -> tuple:
    """g* on the per-cell moduli: a cell relabelling, with nu <-> 1/nu on a
    reflection and NO sign anywhere.  Verified against the cover identity.
    """
    phi = cell_map(label)
    nu_value, a_value, b_value, inverse_value = tables
    out = ({}, {}, {}, {})
    for cell in CELLS:
        image = phi(cell)
        values = (
            (inverse_value[cell], a_value[cell], b_value[cell], nu_value[cell])
            if label[0] == -1
            else (nu_value[cell], a_value[cell], b_value[cell], inverse_value[cell])
        )
        for slot in range(4):
            out[slot][image] = values[slot]
    return out


def induced_substitution(label: tuple) -> dict:
    """g* as an xreplace substitution on the 64 free moduli."""
    tables = induced_tables(label, FREE_MODULI)
    point = {}
    for cell in CELLS:
        point[NU_MODULUS[cell]] = tables[0][cell]
        point[A_MODULUS[cell]] = tables[1][cell]
        point[B_MODULUS[cell]] = tables[2][cell]
        point[INV_MODULUS[cell]] = tables[3][cell]
    return point


def push_point(point: dict, label: tuple) -> dict:
    """g* on a concrete modulus point."""
    phi = cell_map(label)
    out = {}
    for cell in CELLS:
        image = phi(cell)
        swap = label[0] == -1
        out[NU_MODULUS[image]] = point[
            INV_MODULUS[cell] if swap else NU_MODULUS[cell]
        ]
        out[INV_MODULUS[image]] = point[
            NU_MODULUS[cell] if swap else INV_MODULUS[cell]
        ]
        out[A_MODULUS[image]] = point[A_MODULUS[cell]]
        out[B_MODULUS[image]] = point[B_MODULUS[cell]]
    return out


def point_key(point: dict) -> tuple:
    return tuple(sorted((str(key), sp.srepr(value)) for key, value in point.items()))


# ---------------------------------------------------------------------------
# the certificate constants this runner is claiming
# ---------------------------------------------------------------------------
THETA_LABEL = (-1, 7, -1, 0)             # the canonical even-x-centred theta
THETA_PRIME = (-1, 7, -1, 1)             # the odd-x-centred escape reflection
GENERATOR_MOVES = ((1, 0, 1, 1), (1, 1, 1, 0), THETA_LABEL, THETA_PRIME)
SPOT_MOVES = COVARIANT_MOVES[::4]        # 16 moves, evenly spread
SPOT_EDGES = ((0, 0), (1, 2), (2, 3), (3, 1))
CHART01_EDGES = ((0, 0), (0, 1), (1, 0), (1, 1))
ACTING_SAMPLE = ((1, 1, 1, 0), (1, 0, 1, 1), THETA_LABEL, (-1, 3, -1, 3))
NON_ACTING_SAMPLE = ((1, 0, -1, 0), (-1, 7, 1, 0), (1, 3, -1, 2), (-1, 3, 1, 1))

MOVE_COUNT = 128                         # all affine cover moves
ACTING_COUNT = 64                        # exactly those with e_t = e_x
GROUP_ORDER = 64
CARRIER_IMAGE_ORDER = 32
CARRIER_KERNEL = ((1, 0, 1, 0), (1, 4, 1, 0))
BOND_DIRECTIONS = ((1, 3), (7, 1))       # the DIAGONAL bond, both orientations
HALF_SWAP_TRANSLATIONS = 8               # p = 2, 6; none of them involutive
GENERATOR_COVARIANT_HITS = 64            # 4 generators x 16 healed edges
SPOT_COVARIANT_HITS = 64                 # 16 moves x 4 edges
DEEP_COVARIANT_HITS = 1024               # 64 moves x 16 edges, behind --deep
ORBIT_SAMPLE_SIZE = 16
HONEST_REFLECTIONS = 8
EVEN_CENTRED = tuple(
    (-1, p, -1, q) for p in (3, 7) for q in (0, 2)
)
ODD_CENTRED = tuple(
    (-1, p, -1, q) for p in (3, 7) for q in (1, 3)
)
ESCAPE_GRAM = sp.diag(R(15, 64), 0, R(15, 64), 0, 0, R(15, 64), 0, R(15, 64))
ESCAPE_INERTIA = (4, 4, 0)
ESCAPE_STRUCTURAL_ZEROS = 4
FORCING_DETERMINANT = (
    (SHEAR_T ** 2 + SHEAR_X ** 2) ** 6
    * (4 * MASS ** 2 + SHEAR_T ** 2 + SHEAR_X ** 2) ** 2
    / sp.Integer(2) ** 48
)
POOLED_DETERMINANT = (
    (SHEAR_T ** 2 + SHEAR_X ** 2) ** 6
    * (4 * MASS ** 2 + SHEAR_T ** 2 + SHEAR_X ** 2) ** 2
    / sp.Integer(2) ** 32
)
WRONG_DETERMINANT = (
    (SHEAR_T ** 2 + SHEAR_X ** 2) ** 6
    * (2 * MASS ** 2 + SHEAR_T ** 2 + SHEAR_X ** 2) ** 2
    / sp.Integer(2) ** 48
)
FORCING_RANK = 8
FORCING_MASSES = (sp.Integer(0), sp.Integer(1), sp.Integer(-1), R(7, 3))
ENSEMBLE_GRAM_INERTIA = (4, 0, 4)
ODD_CENTRED_LIVE_SLOTS = (4, 4, 4, 4)
RUNTIME_BUDGET_SEC = 600
X0_BLOCKS = ((0, 7), (1, 4), (2, 5), (3, 6))
X0_DIAGONAL_SIGNS = (1, -1, 1, -1, -1, 1, -1, 1)
X0_BLOCK_SIGNS = ((1, 1), (-1, -1), (1, 1), (-1, -1))
X0_DISTINCT_SUMS = 8
X0_CONE_INERTIA = (4, 0, 4)
X0_DEFINITE_BLOCKS = 4
HALF_HODGE_INERTIA = (8, 0, 0)           # the cone premise: H_q[+,+] > 0
ENVELOPE_SIGN_PRESERVING = (3, 0, 5)
ENVELOPE_SIGN_FLIPPING = (8, 0, 0)
ENVELOPE_OVERSIZED_SHEAR = sp.Integer(10)
BARE_TRANSLATIONS = 16
THETA_GAUGES = ("r_x", "r_x r_t")
TRANSLATION_COUNT = 32


# the exact physical-cone carrier realising the odd-centred PSD mass Gram
def escape_witness_field() -> dict:
    """(sigma, nu) per cell: nu = 1 everywhere, shear only on the ODD slices."""
    profile = {
        1: {0: R(3, 5), 1: R(1, 2), 2: R(3, 5), 3: R(-1, 2)},
        3: {0: R(-3, 5), 1: R(1, 2), 2: R(-3, 5), 3: R(-1, 2)},
    }
    return {
        cell: (
            profile[cell[0]][cell[1]] if cell[0] % 2 else sp.Integer(0),
            sp.Integer(1),
        )
        for cell in CELLS
    }


def base_orbit_field() -> dict:
    """A generic cone carrier: 16 distinct shears and 16 distinct volumes."""
    return {
        cell: (R(index - 8, 17), R(index + 3, 7))
        for index, cell in enumerate(CELLS)
    }


CONE_CARRIERS = (
    ("flat", {cell: (sp.Integer(0), sp.Integer(1)) for cell in CELLS}),
    ("staircase", b105.overlap_field()),
    ("b145-witness", b145.witness_field()),
    (
        "mixed",
        {
            cell: (
                R(3, 5) if cell[0] % 2 else R(-1, 3),
                R(7, 4) if cell[1] % 2 else R(2, 5),
            )
            for cell in CELLS
        },
    ),
)


def hermitian_part(matrix: sp.MatrixBase) -> sp.Matrix:
    """(M + M^dagger)/2.  The pairing carries i's, so .H is NOT .T here.

    Block 147's `herm` is the SYMMETRIC part, which coincides with this one on
    the real objects (the Hodge and its Grams) and NOT on the pairing; gate E
    pins the two against each other on the Gram before using either.
    """
    return sp.expand((matrix + matrix.H) / 2)


# ---------------------------------------------------------------------------
# measured facts (computed once, before any mutation flag is consulted)
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Facts:
    main_head: str
    authority: AuthorityCertificate
    # B: the orbit
    inertia_calibration: bool
    descend_count: int
    bond_directions: tuple
    acting_count: int
    acting_is_equal_parity: bool
    acting_sample: tuple
    non_acting_sample: tuple
    group_order: int
    group_closed_on_labels: bool
    group_closed_on_matrices: bool
    carrier_image_order: int
    carrier_kernel: tuple
    antiperiodic_descends: tuple
    plain_shift_descends: bool
    plain_shift_fourth_is_minus_identity: bool
    half_swap_translations: tuple
    # C: covariance
    generator_covariance: tuple
    spot_covariance: tuple
    deep_covariance: tuple
    action_law_pinned: bool
    # D: the migration core
    gram_zero_diagonal: bool
    gram_traceless: bool
    gram_linear_in_moduli: bool
    gram_minor_identity: bool
    gram_hermitian_conventions_agree: bool
    substituted_zero_diagonal: int
    orbit_members: int
    orbit_theta_closed: bool
    cross_hermitian: tuple
    weights_non_uniform: bool
    ensemble_hermitian: bool
    ensemble_gram_zero_diagonal: bool
    ensemble_gram_nonzero: bool
    ensemble_gram_inertia: tuple
    non_closed_controls: tuple
    # E: the escape and its closure
    honest_reflections: tuple
    even_centred_blocked: tuple
    even_centred_minor_identity: tuple
    odd_centred_live: tuple
    escape_gram_matches: bool
    escape_inertia: tuple
    escape_in_cone: bool
    escape_structural_zeros: tuple
    closure_diagonal_law: bool
    closure_only_odd_shears: bool
    closure_determinants: tuple
    closure_ranks: tuple
    closure_mass_ranks: tuple
    pooled_determinants: tuple
    endgame_gram_vanishes: bool
    endgame_diagonal_vanishes: bool
    endgame_minor_identity: bool
    # F: the X_0 complement
    x0_symmetric: bool
    x0_diagonal_shapes: bool
    x0_diagonal_signs: tuple
    x0_distinct_sums: int
    x0_blocks: tuple
    x0_block_signs: tuple
    x0_cone_census: tuple
    x0_orbit_inertias: tuple
    x0_average_inertia: tuple
    half_hodge_inertias: tuple
    envelope_sign_preserving: tuple
    envelope_sign_flipping: tuple
    # G: the bare atlas
    bare_reflections: tuple
    bare_translation_count: int
    theta_bare_hits: int
    theta_gauges: tuple
    unmatched_moves: int
    bare_cross_validated: bool
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

    # --- the move family, and the committed carrier model ------------------
    permutations = {label: move_permutation(label) for label in ALL_MOVES}
    matrices = {label: move_matrix(permutations[label]) for label in ALL_MOVES}
    descended = {label: b142.descend(matrices[label]) for label in ALL_MOVES}
    descend_count = sum(1 for value in descended.values() if value is not None)

    cover_free = b145.cover_hodge_general(*FREE_MODULI)
    hodge_quotient = b145.quotient(cover_free)
    support = frozenset(
        (i, j)
        for i in range(SIZE)
        for j in range(SIZE)
        if cover_free[i, j] != 0
    )
    bond_directions = tuple(
        sorted(
            {
                (((j // LX) - (i // LX)) % COVER_T, ((j % LX) - (i % LX)) % LX)
                for (i, j) in support
                if i != j
            }
        )
    )

    # --- B: which moves act on the 64-modulus family -----------------------
    # The support test is the whole argument: the family's off-diagonal weight
    # sits on the DIAGONAL bond, and a move with e_t != e_x carries it onto an
    # antidiagonal one, which the family cannot represent.
    def keeps_support(label: tuple) -> bool:
        permutation = permutations[label]
        return all(
            (permutation[i], permutation[j]) in support for (i, j) in support
        )

    acting = tuple(label for label in ALL_MOVES if keeps_support(label))
    acting_count = len(acting)
    acting_is_equal_parity = bool(
        all(label[0] == label[2] for label in acting)
        and all(
            label[0] != label[2] for label in ALL_MOVES if label not in set(acting)
        )
    )
    # a four-move sample from each class, carried as EXACT evidence: the acting
    # ones satisfy the full 32x32 cover identity g H g^T = H(g* moduli), the
    # rejected ones are refuted by an explicit support escape
    acting_sample = tuple(
        (
            label,
            descended[label] is not None,
            zero(
                sp.expand(
                    conjugate(cover_free, permutations[label])
                    - b145.cover_hodge_general(
                        *induced_tables(label, FREE_MODULI)
                    )
                )
            ),
        )
        for label in ACTING_SAMPLE
    )
    non_acting_sample = tuple(
        (
            label,
            descended[label] is not None,
            not keeps_support(label),
        )
        for label in NON_ACTING_SAMPLE
    )

    group_closed_on_labels = all(
        compose_labels(left, right) in set(COVARIANT_MOVES)
        for left in COVARIANT_MOVES
        for right in COVARIANT_MOVES
    )
    group_closed_on_matrices = all(
        zero(
            sp.expand(
                matrices[left] * matrices[right]
                - matrices[compose_labels(left, right)]
            )
        )
        for left in GENERATOR_MOVES
        for right in SPOT_MOVES
    )
    induced_keys = {
        label: tuple(
            sorted(
                (str(key), str(value))
                for key, value in induced_substitution(label).items()
            )
        )
        for label in COVARIANT_MOVES
    }
    identity_key = induced_keys[(1, 0, 1, 0)]
    carrier_image_order = len(set(induced_keys.values()))
    carrier_kernel = tuple(
        sorted(
            label
            for label in COVARIANT_MOVES
            if induced_keys[label] == identity_key
        )
    )

    antiperiodic_descends = tuple(
        b142.descend(b134.antiperiodic_time_translation(j)) is not None
        for j in range(COVER_T)
    )
    plain_shift_descends = all(
        descended[(1, j, 1, 0)] is not None for j in range(COVER_T)
    )
    plain_shift_fourth_is_minus_identity = zero(
        sp.expand(descended[(1, 4, 1, 0)] + sp.eye(PHYS))
    )
    half_swap_translations = tuple(
        (
            label,
            zero(
                sp.expand(descended[label] * descended[label] - sp.eye(PHYS))
            ),
        )
        for label in COVARIANT_MOVES
        if label[0] == 1
        and zero(sp.expand(PLUS.T * descended[label] * PLUS))
        and not zero(sp.expand(descended[label] * PLUS))
    )

    # --- the one expensive symbolic pass: the 16 healed edge actions --------
    differentials, star_form = b145.connection(SHEAR_X, SHEAR_T)
    edge_table = b145.edge_differentials(
        differentials, star_form, HEALING_WEIGHTS
    )
    cover_actions = {
        key: sp.expand(
            MASS * cover_free
            + sp.I
            * (
                cover_free * edge_table[key]
                + edge_table[key].H * cover_free
            )
        )
        for key in EDGE_KEYS
    }
    quotient_actions = {
        key: b145.quotient(cover_actions[key]) for key in EDGE_KEYS
    }
    # the inlined action law is pinned against the committed Block 145 routine
    # rather than trusted: it is written out only because the committed one
    # spends its time on generic simplification
    action_law_pinned = all(
        zero(
            sp.expand(
                quotient_actions[key]
                - b145.quotient_action(edge_table[key], cover_free, MASS)
            )
        )
        for key in ((0, 0), (2, 3))
    )
    inverses = {
        label: descended[label].inv()
        for label in set(GENERATOR_MOVES) | set(SPOT_MOVES) | set(COVARIANT_MOVES)
    } if deep else {
        label: descended[label].inv()
        for label in set(GENERATOR_MOVES) | set(SPOT_MOVES)
    }

    def covariant(label: tuple, key: tuple) -> bool:
        """The honest Block 147 covariance, one move and one edge.

            g Q[d; c] g^-1 = Q[d_g; g* c]   (daggered on a reflection)

        with d_g the transported connection; because the move is orthogonal the
        transported action is the RELABELLED cover action, and the orientation
        character of a reflection sends d -> -d, which is exactly A -> A^dagger.
        """
        conjugated = sp.expand(
            descended[label] * quotient_actions[key] * inverses[label]
        )
        source = (
            sp.expand(cover_actions[key].H)
            if label[0] == -1
            else cover_actions[key]
        )
        transported = b145.quotient(conjugate(source, permutations[label]))
        if label[0] == -1:
            transported = transported.H
        return zero(sp.expand(conjugated - transported))

    generator_covariance = (
        sum(
            1
            for label in GENERATOR_MOVES
            for key in EDGE_KEYS
            if covariant(label, key)
        ),
        len(GENERATOR_MOVES) * len(EDGE_KEYS),
    )
    spot_covariance = (
        sum(
            1
            for label in SPOT_MOVES
            for key in SPOT_EDGES
            if covariant(label, key)
        ),
        len(SPOT_MOVES) * len(SPOT_EDGES),
    )
    deep_covariance = (
        (
            sum(
                1
                for label in COVARIANT_MOVES
                for key in EDGE_KEYS
                if covariant(label, key)
            ),
            len(COVARIANT_MOVES) * len(EDGE_KEYS),
        )
        if deep
        else (0, 0)
    )

    # --- D: the migration core ---------------------------------------------
    raw_gram = half_pair(hodge_quotient)
    gram = herm(raw_gram)
    gram_hermitian_conventions_agree = zero(
        sp.expand(gram - hermitian_part(raw_gram))
    )
    gram_zero_diagonal = all(sp.expand(gram[k, k]) == 0 for k in range(HALF))
    gram_traceless = sp.expand(sp.trace(gram)) == 0
    gram_linear_in_moduli = b145.is_linear_in_moduli(gram)
    gram_minor_identity = all(
        sp.expand(
            gram[i, i] * gram[j, j] - gram[i, j] * gram[j, i] + gram[i, j] ** 2
        )
        == 0
        for i in range(HALF)
        for j in range(HALF)
    )
    # the zero diagonal is an IDENTITY in the moduli, so it survives every
    # substitution instance and hence every weighted average
    substituted_zero_diagonal = sum(
        1
        for label in COVARIANT_MOVES
        if all(
            sp.expand(gram.xreplace(induced_substitution(label))[k, k]) == 0
            for k in range(HALF)
        )
    )

    fixture_differentials, fixture_star = b145.connection(b134.S_X, b134.S_T)
    fixture_edges = b145.edge_differentials(
        fixture_differentials, fixture_star, HEALING_WEIGHTS
    )
    reflect = matrices[THETA_LABEL]
    ensemble_edge = fixture_edges[(2, 3)]
    transported_edge = sp.expand(-reflect * ensemble_edge * reflect.T)

    base_point = b147.modulus_point(base_orbit_field())
    sample_labels = [(1, p, 1, q) for p in (0, 2) for q in range(LX)]
    sample_labels += [theta_compose(label) for label in sample_labels]
    orbit: dict = {}
    for label in sample_labels:
        moved = push_point(base_point, label)
        orbit.setdefault(point_key(moved), moved)
    members = list(orbit.values())
    positions = {point_key(point): i for i, point in enumerate(members)}
    partner = {
        i: positions[point_key(push_point(point, THETA_LABEL))]
        for i, point in enumerate(members)
    }
    orbit_theta_closed = bool(
        sorted(partner.values()) == list(range(len(members)))
        and all(partner[partner[i]] == i for i in range(len(members)))
    )

    def member_block(point: dict, differential: sp.Matrix) -> sp.Matrix:
        carrier = b145.cover_hodge_general(
            *[
                {cell: point[table[cell]] for cell in CELLS}
                for table in (NU_MODULUS, A_MODULUS, B_MODULUS, INV_MODULUS)
            ]
        )
        return half_pair(
            b145.quotient_action(differential, carrier, MASS)
        )

    cross_hermitian = (
        sum(
            1
            for i, point in enumerate(members)
            if zero(
                sp.expand(
                    member_block(members[partner[i]], transported_edge)
                    - member_block(point, ensemble_edge).H
                )
            )
        ),
        len(members),
    )
    representatives, seen = [], set()
    for i in range(len(members)):
        if i in seen:
            continue
        representatives.append(i)
        seen |= {i, partner[i]}
    generator = random.Random(3)
    weights = {
        i: R(generator.randint(1, 30), generator.randint(31, 60))
        for i in representatives
    }
    weights_non_uniform = len(set(weights.values())) > 1
    ensemble = sp.zeros(HALF, HALF)
    for i in representatives:
        ensemble += weights[i] * (
            member_block(members[i], ensemble_edge)
            + member_block(members[partner[i]], transported_edge)
        )
    ensemble = sp.expand(ensemble)
    ensemble_hermitian = zero(sp.expand(ensemble - ensemble.H))
    ensemble_gram = herm(
        sp.Matrix(
            HALF,
            HALF,
            lambda i, j: sp.expand(ensemble[i, j]).coeff(MASS, 1),
        )
    )
    ensemble_gram_zero_diagonal = all(
        sp.expand(ensemble_gram[k, k]) == 0 for k in range(HALF)
    )
    ensemble_gram_nonzero = not zero(ensemble_gram)
    ensemble_gram_inertia = congruence_inertia(ensemble_gram)

    # the three non-closed controls, as CHECKED certificates
    dropped = sp.expand(
        sum(
            (
                weights[i] * member_block(members[i], ensemble_edge)
                for i in representatives
            ),
            sp.zeros(HALF, HALF),
        )
    )
    asymmetric = sp.zeros(HALF, HALF)
    for position, i in enumerate(representatives):
        asymmetric += weights[i] * member_block(members[i], ensemble_edge) + (
            weights[i] + (1 if position == 0 else 0)
        ) * member_block(members[partner[i]], transported_edge)
    asymmetric = sp.expand(asymmetric)
    same_connection = sp.expand(
        sum(
            (
                weights[i]
                * (
                    member_block(members[i], ensemble_edge)
                    + member_block(members[partner[i]], ensemble_edge)
                )
                for i in representatives
            ),
            sp.zeros(HALF, HALF),
        )
    )
    non_closed_controls = (
        zero(sp.expand(dropped - dropped.H)),
        zero(sp.expand(asymmetric - asymmetric.H)),
        zero(sp.expand(same_connection - same_connection.H)),
    )

    # --- E: the honest OS reflections, the escape, and its closure ---------
    honest_reflections = tuple(
        label
        for label in COVARIANT_MOVES
        if descended[label] is not None
        and zero(sp.expand(PLUS.T * descended[label] * PLUS))
        and not zero(sp.expand(descended[label] * PLUS))
        and zero(
            sp.expand(descended[label] * descended[label] - sp.eye(PHYS))
        )
    )
    reflection_grams = {
        label: herm(half_pair(hodge_quotient, descended[label]))
        for label in EVEN_CENTRED + ODD_CENTRED
    }
    even_centred_blocked = tuple(
        all(sp.expand(reflection_grams[label][k, k]) == 0 for k in range(HALF))
        for label in EVEN_CENTRED
    )
    even_centred_minor_identity = tuple(
        all(
            sp.expand(
                reflection_grams[label][i, i] * reflection_grams[label][j, j]
                - reflection_grams[label][i, j] * reflection_grams[label][j, i]
                + reflection_grams[label][i, j] ** 2
            )
            == 0
            for i in range(HALF)
            for j in range(HALF)
        )
        for label in EVEN_CENTRED
    )
    odd_centred_live = tuple(
        sum(
            1
            for k in range(HALF)
            if sp.expand(reflection_grams[label][k, k]) != 0
        )
        for label in ODD_CENTRED
    )

    witness_field = escape_witness_field()
    witness_point = b147.modulus_point(witness_field)
    witness_gram = sp.expand(
        reflection_grams[THETA_PRIME].xreplace(witness_point)
    )
    escape_gram_matches = zero(sp.expand(witness_gram - ESCAPE_GRAM))
    escape_inertia = congruence_inertia(witness_gram)
    escape_in_cone = b145.in_admissible_cone(witness_field)

    closure_determinants: set = set()
    pooled_determinants: set = set()
    closure_ranks: set = set()
    closure_mass_ranks: set = set()
    closure_diagonal_law = True
    closure_only_odd_shears = True
    escape_structural_zeros = []
    for label in ODD_CENTRED:
        operator = descended[label]
        reflection_gram = reflection_grams[label]
        zero_slots = [
            k for k in range(HALF) if sp.expand(reflection_gram[k, k]) == 0
        ]
        escape_structural_zeros.append(len(zero_slots))
        pooled_rows: list = []
        for key in CHART01_EDGES:
            # PSD is a statement about the HERMITIAN PART, so that is what the
            # forcing argument is run on -- this is where Block 147's step is
            # replaced rather than repaired.
            pairing = hermitian_part(half_pair(quotient_actions[key], operator))
            if not all(
                sp.expand(pairing[k, k] - MASS * reflection_gram[k, k]) == 0
                for k in range(HALF)
            ):
                closure_diagonal_law = False
            rows = []
            for k in zero_slots:
                for j in range(HALF):
                    for part in (
                        sp.expand(sp.re(pairing[k, j])),
                        sp.expand(sp.im(pairing[k, j])),
                    ):
                        if part != 0:
                            rows.append(part)
            involved: set = set()
            for row in rows:
                involved |= set(row.free_symbols) & set(COORDS)
            if not involved <= set(ODD_SHEAR_COORDS):
                closure_only_odd_shears = False
            system = sp.Matrix(
                [
                    [sp.expand(row).coeff(value, 1) for value in ODD_SHEAR_COORDS]
                    for row in rows
                ]
            )
            closure_determinants.add(
                sp.factor(sp.expand((system.T * system).det()))
            )
            closure_ranks.add(system.rank())
            for mass in FORCING_MASSES:
                closure_mass_ranks.add(
                    sp.Matrix(
                        [
                            [
                                sp.expand(row.subs(MASS, mass)).coeff(value, 1)
                                for value in ODD_SHEAR_COORDS
                            ]
                            for row in rows
                        ]
                    ).rank()
                )
            pooled_rows.extend(rows)
        pooled = sp.Matrix(
            [
                [sp.expand(row).coeff(value, 1) for value in ODD_SHEAR_COORDS]
                for row in pooled_rows
            ]
        )
        pooled_determinants.add(sp.factor(sp.expand((pooled.T * pooled).det())))

    # the endgame: the forced rows kill the eight odd shears, and THERE the
    # Gram and the whole Hermitian part collapse -- a PSD matrix with a zero
    # diagonal is zero, so a positive odd-centred pairing is IDENTICALLY zero
    kill_odd = {value: sp.Integer(0) for value in ODD_SHEAR_COORDS}
    endgame_gram_vanishes = zero(
        sp.expand(reflection_grams[THETA_PRIME].xreplace(kill_odd))
    )
    endgame_pairing = sp.expand(
        hermitian_part(
            half_pair(quotient_actions[(0, 0)], descended[THETA_PRIME])
        ).xreplace(kill_odd)
    )
    endgame_diagonal_vanishes = all(
        sp.expand(endgame_pairing[k, k]) == 0 for k in range(HALF)
    )
    endgame_minor_identity = all(
        sp.expand(
            endgame_pairing[i, j] * endgame_pairing[j, i]
            - (
                sp.expand(sp.re(endgame_pairing[i, j])) ** 2
                + sp.expand(sp.im(endgame_pairing[i, j])) ** 2
            )
        )
        == 0
        for i in range(HALF)
        for j in range(HALF)
    )

    # --- F: the X_0 complement ---------------------------------------------
    x0_block = half_pair(hodge_quotient, X0)
    x0_symmetric = zero(sp.expand(x0_block - x0_block.T))
    x0_diagonal_shapes = True
    x0_diagonal_signs = []
    scaled_entries = []
    for k in range(HALF):
        scaled = sp.expand(4 * x0_block[k, k])
        scaled_entries.append(scaled)
        terms = sp.Add.make_args(scaled)
        coefficients = {term.as_coeff_Mul()[0] for term in terms}
        symbols = {term.as_coeff_Mul()[1] for term in terms}
        if (
            len(terms) == 4
            and symbols <= VOLUME_COORDS
            and coefficients in ({sp.Integer(1)}, {sp.Integer(-1)})
        ):
            x0_diagonal_signs.append(int(next(iter(coefficients))))
        else:
            x0_diagonal_shapes = False
            x0_diagonal_signs.append(0)
    x0_diagonal_signs = tuple(x0_diagonal_signs)
    x0_distinct_sums = len(
        {
            sp.expand(x0_diagonal_signs[k] * scaled_entries[k])
            for k in range(HALF)
        }
    )
    x0_support = {
        (min(i, j), max(i, j))
        for i in range(HALF)
        for j in range(HALF)
        if i != j and sp.expand(x0_block[i, j]) != 0
    }
    x0_blocks = tuple(sorted(x0_support))
    x0_block_signs = tuple(
        (x0_diagonal_signs[i], x0_diagonal_signs[j]) for (i, j) in x0_blocks
    )

    x0_cone_census = []
    half_hodge_inertias = []
    for label, field in CONE_CARRIERS:
        point = b147.modulus_point(field)
        evaluated = sp.expand(x0_block.xreplace(point))
        per_block = [
            congruence_inertia(evaluated[[i, j], [i, j]])
            for (i, j) in x0_blocks
        ]
        x0_cone_census.append(
            (
                label,
                congruence_inertia(evaluated),
                sum(
                    1
                    for inertia in per_block
                    if inertia[2] == 0 or inertia[0] == 0
                ),
            )
        )
        half_hodge_inertias.append(
            congruence_inertia(
                sp.expand(
                    hodge_quotient[
                        list(range(HALF)), list(range(HALF))
                    ].xreplace(point)
                )
            )
        )
    x0_cone_census = tuple(x0_cone_census)
    half_hodge_inertias = tuple(half_hodge_inertias)

    mixed_point = b147.modulus_point(dict(CONE_CARRIERS)["mixed"])
    orbit_average = sp.zeros(HALF, HALF)
    x0_orbit_inertias = set()
    for label in COVARIANT_MOVES:
        moved = sp.expand(x0_block.xreplace(push_point(mixed_point, label)))
        x0_orbit_inertias.add(congruence_inertia(moved))
        orbit_average += moved
    x0_orbit_inertias = tuple(sorted(x0_orbit_inertias))
    x0_average_inertia = congruence_inertia(
        sp.expand(orbit_average / len(COVARIANT_MOVES))
    )

    # THE CONE PREMISE, carried as two counterexamples rather than as prose:
    # inside the Block 145 linear envelope the (4,0,4) split is FALSE, both
    # with the diagonal signs preserved and with them flipped.
    envelope_point = {}
    for cell in CELLS:
        for table in (NU_MODULUS, A_MODULUS, INV_MODULUS):
            envelope_point[table[cell]] = sp.Integer(1)
        envelope_point[B_MODULUS[cell]] = sp.Integer(0)
    preserving_point = dict(envelope_point)
    preserving_point[B_MODULUS[(0, 3)]] = ENVELOPE_OVERSIZED_SHEAR
    preserving = sp.expand(x0_block.xreplace(preserving_point))
    envelope_sign_preserving = (
        tuple(int(sp.sign(preserving[k, k])) for k in range(HALF))
        == x0_diagonal_signs,
        congruence_inertia(preserving),
    )
    flipping_point = dict(envelope_point)
    negative_slots = [k for k in range(HALF) if X0[k, k] == -1]
    for symbol in set().union(
        *[set(sp.expand(hodge_quotient[k, k]).free_symbols) for k in negative_slots]
    ):
        flipping_point[symbol] = sp.Integer(-1)
    flipping = sp.expand(x0_block.xreplace(flipping_point))
    envelope_sign_flipping = (
        tuple(int(sp.sign(flipping[k, k])) for k in range(HALF))
        == x0_diagonal_signs,
        congruence_inertia(flipping),
    )

    # --- G: the bare atlas --------------------------------------------------
    atlas = {INDEX[origin]: differentials[origin] for origin in ORIGINS}
    variants = {
        "": differentials,
        "|s_t": b145.connection(SHEAR_X, -SHEAR_T)[0],
        "|s_x": b145.connection(-SHEAR_X, SHEAR_T)[0],
        "|both": b145.connection(-SHEAR_X, -SHEAR_T)[0],
    }
    lift_t, lift_x = b105.shift_lifts()
    gauge_x = b134.lifted(lift_x)
    gauge_t = b134.lifted(lift_t)
    gauges = {
        "I": sp.eye(SIZE),
        "r_x": gauge_x,
        "r_t": gauge_t,
        "r_x r_t": sp.expand(gauge_x * gauge_t),
    }
    lookup: dict = {}
    for gauge_name, gauge in gauges.items():
        gauge_inverse = gauge.inv()
        for variant_name, table in variants.items():
            for origin in ORIGINS:
                for dagger in (False, True):
                    base = table[origin].H if dagger else table[origin]
                    for sign in (1, -1):
                        key = sp.ImmutableMatrix(
                            sp.expand(sign * gauge * base * gauge_inverse)
                        )
                        lookup.setdefault(key, set()).add(
                            (
                                gauge_name,
                                INDEX[origin],
                                variant_name,
                                dagger,
                                sign,
                            )
                        )

    def classify(label: tuple) -> dict:
        matrix = matrices[label]
        inverse = matrix.T
        return {
            chart: lookup.get(
                sp.ImmutableMatrix(
                    sp.expand(matrix * atlas[chart] * inverse)
                ),
                frozenset(),
            )
            for chart in range(4)
        }

    translations = tuple(
        label for label in COVARIANT_MOVES if label[0] == 1
    )
    bare_reflections, bare_translation_count, unmatched_moves = [], 0, 0
    for label in honest_reflections + translations:
        hits = classify(label)
        if any(not hits[chart] for chart in range(4)):
            unmatched_moves += 1
        elif all(
            any(hit[0] == "I" for hit in hits[chart]) for chart in range(4)
        ):
            if label[0] == -1:
                bare_reflections.append(label)
            else:
                bare_translation_count += 1
    bare_reflections = tuple(sorted(bare_reflections))
    theta_hits = classify(THETA_LABEL)
    theta_bare_hits = sum(
        1
        for chart in range(4)
        for hit in theta_hits[chart]
        if hit[0] == "I"
    )
    theta_gauges = tuple(
        sorted({hit[0] for chart in range(4) for hit in theta_hits[chart]})
    )
    # the hash lookup is a speed device, so it is cross-validated against an
    # explicit symbolic comparison on the escape reflection's first chart
    transported_chart = sp.expand(
        matrices[THETA_PRIME] * atlas[0] * matrices[THETA_PRIME].T
    )
    direct = {
        (gauge_name, INDEX[origin], variant_name, dagger, sign)
        for gauge_name, gauge in gauges.items()
        for variant_name, table in variants.items()
        for origin in ORIGINS
        for dagger in (False, True)
        for sign in (1, -1)
        if zero(
            sp.expand(
                transported_chart
                - sign
                * gauge
                * (table[origin].H if dagger else table[origin])
                * gauge.inv()
            )
        )
    }
    bare_cross_validated = direct == set(classify(THETA_PRIME)[0])

    exact_no_float = no_float(
        (
            cover_free,
            hodge_quotient,
            gram,
            x0_block,
            ensemble,
            witness_gram,
            tuple(quotient_actions.values()),
            tuple(closure_determinants),
            tuple(pooled_determinants),
        )
    )

    return Facts(
        main_head=main_head,
        authority=authority,
        inertia_calibration=inertia_calibration,
        descend_count=descend_count,
        bond_directions=bond_directions,
        acting_count=acting_count,
        acting_is_equal_parity=acting_is_equal_parity,
        acting_sample=acting_sample,
        non_acting_sample=non_acting_sample,
        group_order=len(COVARIANT_MOVES),
        group_closed_on_labels=group_closed_on_labels,
        group_closed_on_matrices=group_closed_on_matrices,
        carrier_image_order=carrier_image_order,
        carrier_kernel=carrier_kernel,
        antiperiodic_descends=antiperiodic_descends,
        plain_shift_descends=plain_shift_descends,
        plain_shift_fourth_is_minus_identity=plain_shift_fourth_is_minus_identity,
        half_swap_translations=half_swap_translations,
        generator_covariance=generator_covariance,
        spot_covariance=spot_covariance,
        deep_covariance=deep_covariance,
        action_law_pinned=action_law_pinned,
        gram_zero_diagonal=gram_zero_diagonal,
        gram_traceless=gram_traceless,
        gram_linear_in_moduli=gram_linear_in_moduli,
        gram_minor_identity=gram_minor_identity,
        gram_hermitian_conventions_agree=gram_hermitian_conventions_agree,
        substituted_zero_diagonal=substituted_zero_diagonal,
        orbit_members=len(members),
        orbit_theta_closed=orbit_theta_closed,
        cross_hermitian=cross_hermitian,
        weights_non_uniform=weights_non_uniform,
        ensemble_hermitian=ensemble_hermitian,
        ensemble_gram_zero_diagonal=ensemble_gram_zero_diagonal,
        ensemble_gram_nonzero=ensemble_gram_nonzero,
        ensemble_gram_inertia=ensemble_gram_inertia,
        non_closed_controls=non_closed_controls,
        honest_reflections=honest_reflections,
        even_centred_blocked=even_centred_blocked,
        even_centred_minor_identity=even_centred_minor_identity,
        odd_centred_live=odd_centred_live,
        escape_gram_matches=escape_gram_matches,
        escape_inertia=escape_inertia,
        escape_in_cone=escape_in_cone,
        escape_structural_zeros=tuple(escape_structural_zeros),
        closure_diagonal_law=closure_diagonal_law,
        closure_only_odd_shears=closure_only_odd_shears,
        closure_determinants=tuple(closure_determinants),
        closure_ranks=tuple(sorted(closure_ranks)),
        closure_mass_ranks=tuple(sorted(closure_mass_ranks)),
        pooled_determinants=tuple(pooled_determinants),
        endgame_gram_vanishes=endgame_gram_vanishes,
        endgame_diagonal_vanishes=endgame_diagonal_vanishes,
        endgame_minor_identity=endgame_minor_identity,
        x0_symmetric=x0_symmetric,
        x0_diagonal_shapes=x0_diagonal_shapes,
        x0_diagonal_signs=x0_diagonal_signs,
        x0_distinct_sums=x0_distinct_sums,
        x0_blocks=x0_blocks,
        x0_block_signs=x0_block_signs,
        x0_cone_census=x0_cone_census,
        x0_orbit_inertias=x0_orbit_inertias,
        x0_average_inertia=x0_average_inertia,
        half_hodge_inertias=half_hodge_inertias,
        envelope_sign_preserving=envelope_sign_preserving,
        envelope_sign_flipping=envelope_sign_flipping,
        bare_reflections=bare_reflections,
        bare_translation_count=bare_translation_count,
        theta_bare_hits=theta_bare_hits,
        theta_gauges=theta_gauges,
        unmatched_moves=unmatched_moves,
        bare_cross_validated=bare_cross_validated,
        exact_no_float=exact_no_float,
        scope=scope_certificate(raw_note()),
    )


# ---------------------------------------------------------------------------
# H. note scope
# ---------------------------------------------------------------------------
# PLACEHOLDER FENCE.  The landing supervisor replaces this string with the
# note's own eight-line N5 fence, byte for byte; until then H-note-scope is the
# single failing gate and the runner exits 1.
N5_FENCE = 'N5: per_element: THE ORBIT, exhausted rather than sampled: all 128 unsigned affine cover moves (t,x) -> (e_t t + p, e_x x + q) DESCEND through the antiperiodic quotient, and EXACTLY 64 act on the 64-modulus carrier family, characterized by e_t = e_x -- the family\'s ONLY BOND DIRECTION IS THE DIAGONAL (1,-1), so a mixed-parity move carries the cover Hodge\'s support off itself and all 64 such moves are REFUTED BY SUPPORT CONTAINMENT rather than merely unverified; the surviving 64 form (Z_8 x Z_4):Z_2 of ORDER 64 and act on CARRIERS through ORDER 32 with kernel {id, t-shift-by-4}, two distinct quantities kept apart; the wrap-signed antiperiodic shift T_AP^j DESCENDS ONLY AT j = 0 while the PLAIN cover shift is the carrier move, descending at EVERY j with shift^4 -> -I (the wrap); and of the half-swapping translations in the carrier group FOUR SQUARE TO -I and the rest to -(x-shift-by-2), so NONE IS INVOLUTIVE -- the load-bearing point that excludes every translation from the OS-reflection census\nper_site: THE COVARIANCE IS GROUP-WIDE: Block 147\'s honest identity is not a property of theta but of the whole carrier group, g Q[d; c] g^{-1} = Q[g d g^{-1}; g*c] holding 1024/1024 over 64 moves x 16 healed edges, SYMBOLIC in the fixture shears (s_x, s_t) and in ALL 64 MODULI, with 192/192 on the generators -- the x-shift, the t-shift, theta and the odd-centred theta\' -- across the healed weights, the control weights and the UNDRESSED atlas; the reflection case carries the adjoint, and the "ORIENTATION CHARACTER" sigma(g) = eps sending d -> -d is recorded as PRESENTATIONAL rather than structural, since A(-d) = A(d)^dagger makes the sign form and the dagger form ALGEBRAIC TWINS of one identity and not two independent facts\nper_mode: THE GENERAL ENSEMBLE PAIRING: per-element cross-Hermiticity [theta g]_++ = ([g]_++)^dagger holds 1024/1024 IDENTICALLY IN THE MODULI, so it is inherited by any weighted sum in which g and theta.g carry equal weight -- hence EVERY THETA-CLOSED ENSEMBLE, ANY SIZE, ANY WEIGHTS, ORBIT OR NOT, has a HERMITIAN pairing, and that pairing is EXACTLY AFFINE in m with the averaged mass Gram as its m-coefficient, entrywise; Block 147\'s two-member ensemble is the SMALLEST INSTANCE of this, not the special one; and the hypothesis is not decorative -- the DROPPED-PARTNER control, the ASYMMETRIC-WEIGHTS control and the UNTRANSFORMED-CONNECTION control ALL FAIL HERMITICITY, so theta-closure with honest transport is exactly the named class and nothing weaker\nper_block: THE GENERAL MIGRATION CORE: diag Herm([theta H_q(y)]_++) = 0 is an IDENTITY IN THE MODULI y -- not an evaluation at a carrier -- so it survives the substitution y -> g*y for each of the 64 covariant moves and therefore survives ARBITRARY WEIGHTED AVERAGING, since an ensemble average is a CONVEX COMBINATION OF SUBSTITUTION INSTANCES; hence diag G_ens = 0 and tr G_ens = 0 for EVERY ensemble, every 2x2 principal minor of G_ens is -g^2 <= 0, positive semidefiniteness forces G_ens = 0, and the pairing is then m-INDEPENDENT: THE BLOCK 147 MIGRATION THEOREM HOLDS FOR EVERY ENSEMBLE WHATSOEVER, so the parent\'s result was never a property of its average and the enlargement it named as the last place an annealed mass could survive positivity is EXHAUSTED\nlattice_wide: THE ESCAPE, ITS STRONGER CLOSURE, AND THE X_0 COMPLEMENT: reading every covariant move as a pairing operator gives 42/64 with a zero diagonal and 22/64 with a live trace, zero diagonal <=> zero trace exactly, but an OS reflection must SWAP THE TIME HALVES and be INVOLUTIVE, which leaves EXACTLY EIGHT (e = -1, p in {3,7}, q in 0..3); the four EVEN-x-centred are BLOCKED since every 2x2 minor is minus a square, while for the four ODD-x-centred BLOCK 147\'S ZERO-DIAGONAL STEP GENUINELY FAILS -- at the physical cone carrier nu = 1 with sigma = -3/5 at (1,0),(1,2) and sigma = +3/5 at (3,0),(3,2), G = diag(15/64, 0, 15/64, 0, 0, 15/64, 0, 15/64) is a POSITIVE SEMIDEFINITE LIVE MASS GRAM of inertia (4,4,0), rank 4, trace 15/16; the closure is STRONGER than migration: diag A = m diag G identically with A THE HERMITIAN PART -- the PSD step must be taken on A, since the RAW pairing\'s row system DEGENERATES AT m = 0 -- diag G has FOUR STRUCTURAL ZEROS, PSD forces the four corresponding ROWS of G to vanish, and on the four chart-0/1 left edges, or on the ATLAS-POOLED system, those rows involve exactly the eight odd shears with det(M^T M) = (s_t^2 + s_x^2)^6 (4 m^2 + s_t^2 + s_x^2)^2 / 2^48 per displayed edge and (65 s_t^2 + 96 s_x^2)^6 (384 m^2 + 65 s_t^2 + 96 s_x^2)^2 / 472769874482845188096 pooled, EVERY EXPANDED MONOMIAL POSITIVE OF EVEN DEGREE, so the rank is 8 AT EVERY REAL m: all eight odd shears vanish, G = 0, diag A = 0, and A POSITIVE ODD-CENTRED PAIRING IS IDENTICALLY ZERO, STRICTLY STRONGER THAN MASSLESS -- with the PER-EDGE HONESTY CAVEAT stated, that generic edges carry non-shear moduli and that edges (2,2) and (3,3) have the s_t-coefficient zero, so the system is displayed on those edges and on the pooled atlas rather than claimed edge-uniformly; and for the X_0 convention, diag [X_0 H_q]_++ consists of EIGHT PAIRWISE DISTINCT four-term VOLUME sums, four positive and four negative, supported on FOUR DISJOINT CARRIER-INDEPENDENT 2x2 BLOCKS pairing SAME-SIGN slots ({0,7}, {2,5} positive; {1,4}, {3,6} negative), so under the LOAD-BEARING CONE PREMISE a > |b| -- equivalently H_q[+,+] POSITIVE DEFINITE, whose necessity is exhibited by linear-envelope points of the SAME sign pattern giving (3,0,5) or (8,0,0), so the cone quantification is REAL AND NOT DECORATIVE -- all four blocks are DEFINITE, two positive-definite and two negative-definite, inertia (4,0,4), and since every covariant move only RELABELS VOLUME SLOTS (nu <-> 1/nu, no signs) no ensemble average changes the split: (4,0,4) ACROSS THE ENTIRE CENSUS, with diag [X_0 Q]_++ = m diag [X_0 H_q]_++ making four slots STRICTLY NEGATIVE for m > 0, so THE X_0 CONVENTION IS BLOCKED AT EVERY ENSEMBLE; finally, among the eight OS reflections the ODD-x-CENTRED ones are the UNIQUE ones whose transported connection stays in the BARE committed atlas, -g d_i g^{-1} = d_i(s_x, -s_t)^dagger with the IDENTITY gauge on all four charts where the canonical theta needs the r_x or r_x r_t gauge -- sixteen pure translations being bare as well, so BARENESS IS UNIQUE AMONG THE OS REFLECTIONS ONLY -- and whether the odd-centred reflection should DISPLACE THETA AS THE CANONICAL OS OPERATOR is NAMED AND NOT DECIDED HERE\nRESULT: on the displayed Block 105 atlas with (s_x, s_t) and m SYMBOLIC and the committed fixtures s_x = 3/5, s_t = 4/5 available but never required, executing Block 147\'s named ensembles-beyond-two-members item and DECIDING IT COMPLETELY, diag Herm([theta H_q(y)]_++) = 0 is an IDENTITY IN THE MODULI, so it survives arbitrary substitution and hence ARBITRARY WEIGHTED AVERAGING, and with per-element cross-Hermiticity 1024/1024 and exact affineness in m EVERY THETA-CLOSED ENSEMBLE OF ANY SIZE AND ANY WEIGHTS has a Hermitian pairing whose positive semidefiniteness FORCES ITS ENSEMBLE MASS GRAM TO ZERO -- THE BLOCK 147 MIGRATION THEOREM HOLDS FOR EVERY ENSEMBLE WHATSOEVER, generalising the parent rather than contradicting it; the carrier group is exhausted (128 moves descend, exactly 64 act, e_t = e_x by the DIAGONAL-BOND SUPPORT ARGUMENT, (Z_8 x Z_4):Z_2 of order 64 acting through order 32) with honest covariance 1024/1024 and 192/192 across all three dressings, no half-swapping translation involutive, and EXACTLY EIGHT honest OS reflections of which four are blocked and four ODD-x-CENTRED GENUINELY ESCAPE with a PSD LIVE mass Gram diag(15/64, 0, 15/64, 0, 0, 15/64, 0, 15/64) of inertia (4,4,0) -- and those four are then closed STRICTLY MORE STRONGLY, since diag A = m diag G on the HERMITIAN PART with four structural zeros forces an eight-variable system of determinant (s_t^2 + s_x^2)^6 (4 m^2 + s_t^2 + s_x^2)^2 / 2^48 per displayed edge and (65 s_t^2 + 96 s_x^2)^6 (384 m^2 + 65 s_t^2 + 96 s_x^2)^2 / 472769874482845188096 pooled, every expanded monomial POSITIVE, hence RANK 8 AT EVERY REAL m and A POSITIVE ODD-CENTRED PAIRING IDENTICALLY ZERO; the X_0 convention is CONE-BLOCKED at (4,0,4) across the entire census under the load-bearing premise a > |b|, whose necessity is exhibited by envelope counterexamples at (3,0,5) and (8,0,0); the VERDICT is the COMPLETE ENSEMBLE NO-GO FOR BOTH DISPLAYED CONVENTIONS -- no reflection-symmetric ensemble of any size carries a positive massive lattice-theta pairing on this atlas, and X_0 is blocked at every ensemble -- with everything symbolic in (s_x, s_t) and in m across all three dressings, so NOTHING IS A FIXTURE ACCIDENT; all inertias are computed by EXACT SYMMETRIC CONGRUENCE and the distinct-real-root helper is never called\nDECISION_CUT: decide THE ODD-CENTRED REFLECTION AS THE CANONICAL OS OPERATOR -- the BARE-ATLAS QUESTION -- since the odd-x-centred reflections are the UNIQUE OS reflections whose transported connection needs no gauge while the canonical theta needs r_x or r_x r_t, and the choice of OS operator is prior to every pairing verdict this arc has stated; DECIDE THE SHEAR\'S GAUGE CLASSIFICATION -- physics or bookkeeping -- inherited undecided from Block 147; register BOUNDARY AND DEFECT COMPLETIONS as premises and execute them rather than importing them; execute the JOINT-LANE PROGRAM; non-lattice pairing conventions remain unbuilt and curved OS is not decided\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero'


SCOPE_KEYS = (
    "orbit_characterisation",
    "half_swap_not_involutive",
    "antiperiodic_shift",
    "migration_identity",
    "every_ensemble",
    "escape_centring",
    "escape_genuine",
    "escape_witness",
    "closure_hermitian_part",
    "closure_identically_zero",
    "closure_rank",
    "per_edge_honesty",
    "x0_pairwise_distinct",
    "x0_definite",
    "cone_premise",
    "bare_atlas",
    "bare_uniqueness",
    "named_next",
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
        "orbit_characterisation": "e_t = e_x" in note
        or "64 of 128" in note
        or "e_t=e_x" in compact,
        "half_swap_not_involutive": "not involutive" in note
        or "not involutions" in note,
        "antiperiodic_shift": "does not descend" in note or "plain" in note,
        "migration_identity": "identity in the moduli" in note,
        "every_ensemble": "every ensemble" in note or "arbitrary" in note,
        # Whitespace-insensitive so the note may hyphenate either way.
        "escape_centring": "odd-x-centred" in compact
        or "odd-centred" in compact,
        "escape_genuine": "genuinely fails" in note,
        "escape_witness": "15/64" in note,
        "closure_hermitian_part": "hermitian part" in note,
        "closure_identically_zero": "identically zero" in note,
        "closure_rank": "rank 8 at every real m" in note or "2^48" in note,
        "per_edge_honesty": "pooled" in note or "chart-0/1" in compact,
        "x0_pairwise_distinct": "pairwise distinct" in note,
        "x0_definite": "definite" in note,
        "cone_premise": "h_q[+,+]" in compact or "cone inequality" in note,
        "bare_atlas": "bare" in note,
        "bare_uniqueness": "unique among the os reflections" in note,
        "named_next": "canonical os operator" in note
        or "displace theta" in note,
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
        "acting_count": ACTING_COUNT,
        "antiperiodic_descends": (True,) + (False,) * (COVER_T - 1),
        "generator_covariance": GENERATOR_COVARIANT_HITS,
        "gram_zero_diagonal": True,
        "non_closed_controls": (False, False, False),
        "even_centred_blocked": (True, True, True, True),
        "closure_determinant": FORCING_DETERMINANT,
        "psd_forces_identically_zero": True,
        "envelope_inertias": (
            ENVELOPE_SIGN_PRESERVING,
            ENVELOPE_SIGN_FLIPPING,
        ),
        "x0_block_signs": X0_BLOCK_SIGNS,
        "theta_bare_hits": 0,
        "bare_translation_count": BARE_TRANSLATIONS,
        "required_scope_keys": SCOPE_KEYS,
    }
    if mutation == "stale_main_authority":
        claims["main_head"] = STALE_MAIN
    elif mutation == "stale_parent_authority":
        claims["parent_pin"] = "stale"
    elif mutation == "wrong_orbit_count":
        claims["acting_count"] = ACTING_COUNT // 2
    elif mutation == "claim_antiperiodic_descends":
        claims["antiperiodic_descends"] = (True,) * COVER_T
    elif mutation == "break_honest_identity":
        claims["generator_covariance"] = GENERATOR_COVARIANT_HITS - 1
    elif mutation == "break_diagonal_identity":
        claims["gram_zero_diagonal"] = False
    elif mutation == "claim_non_closed_hermitian":
        claims["non_closed_controls"] = (True, False, False)
    elif mutation == "claim_even_centring_live":
        claims["even_centred_blocked"] = (False, True, True, True)
    elif mutation == "wrong_forcing_determinant":
        claims["closure_determinant"] = WRONG_DETERMINANT
    elif mutation == "claim_massless_but_nonzero":
        claims["psd_forces_identically_zero"] = False
    elif mutation == "claim_envelope_validity":
        claims["envelope_inertias"] = (X0_CONE_INERTIA, X0_CONE_INERTIA)
    elif mutation == "wrong_block_signs":
        claims["x0_block_signs"] = ((1, -1), (-1, 1), (1, -1), (-1, 1))
    elif mutation == "claim_theta_is_bare":
        claims["theta_bare_hits"] = 1
    elif mutation == "claim_translations_not_bare":
        claims["bare_translation_count"] = 0
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
            "docs/ADMISSIBILITY_DIRAC_KAHLER_GENERAL_MIGRATION_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-20.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_ANNEALED_PAIRING_MIGRATION_BOUNDED_THEOREM_NOTE_2026-08-19.md",
            "scripts/admissibility_dirac_kahler_annealed_pairing_migration_2026_08_19.py",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_SEAM_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-08-19.md",
            "scripts/admissibility_dirac_kahler_seam_dichotomy_2026_08_19.py",
        )
        and PARENT_ARTIFACTS
        == (BLOCK147_NOTE, BLOCK147_RUNNER, BLOCK145_NOTE, BLOCK145_RUNNER)
        and facts.main_head == claims["main_head"]
        and authority.fixed_authority
        and authority.parent_ref_and_ancestry
        and parent_blobs_ok
    )

    gate_b = bool(
        facts.inertia_calibration
        and facts.descend_count == MOVE_COUNT
        and facts.bond_directions == BOND_DIRECTIONS
        and facts.acting_count == claims["acting_count"]
        and facts.acting_is_equal_parity
        and len(facts.acting_sample) == 4
        and all(
            descends and exact for _, descends, exact in facts.acting_sample
        )
        and len(facts.non_acting_sample) == 4
        and all(
            descends and escapes
            for _, descends, escapes in facts.non_acting_sample
        )
        and facts.group_order == GROUP_ORDER
        and facts.group_closed_on_labels
        and facts.group_closed_on_matrices
        and facts.carrier_image_order == CARRIER_IMAGE_ORDER
        and facts.carrier_kernel == CARRIER_KERNEL
        and facts.antiperiodic_descends == tuple(claims["antiperiodic_descends"])
        and facts.plain_shift_descends
        and facts.plain_shift_fourth_is_minus_identity
        and len(facts.half_swap_translations) == HALF_SWAP_TRANSLATIONS
        and not any(
            involutive for _, involutive in facts.half_swap_translations
        )
        and facts.exact_no_float
    )

    gate_c = bool(
        facts.generator_covariance
        == (claims["generator_covariance"], GENERATOR_COVARIANT_HITS)
        and facts.spot_covariance == (SPOT_COVARIANT_HITS, SPOT_COVARIANT_HITS)
        and facts.action_law_pinned
        and facts.deep_covariance
        in ((0, 0), (DEEP_COVARIANT_HITS, DEEP_COVARIANT_HITS))
        and facts.exact_no_float
    )

    gate_d = bool(
        facts.gram_zero_diagonal == bool(claims["gram_zero_diagonal"])
        and facts.gram_traceless
        and facts.gram_linear_in_moduli
        and facts.gram_minor_identity
        and facts.gram_hermitian_conventions_agree
        and facts.substituted_zero_diagonal == GROUP_ORDER
        and facts.orbit_members == ORBIT_SAMPLE_SIZE
        and facts.orbit_theta_closed
        and facts.cross_hermitian == (ORBIT_SAMPLE_SIZE, ORBIT_SAMPLE_SIZE)
        and facts.weights_non_uniform
        and facts.ensemble_hermitian
        and facts.ensemble_gram_zero_diagonal
        and facts.ensemble_gram_nonzero
        and facts.ensemble_gram_inertia == ENSEMBLE_GRAM_INERTIA
        and facts.non_closed_controls == tuple(claims["non_closed_controls"])
        and facts.exact_no_float
    )

    gate_e = bool(
        len(facts.honest_reflections) == HONEST_REFLECTIONS
        and set(facts.honest_reflections) == set(EVEN_CENTRED + ODD_CENTRED)
        and facts.even_centred_blocked == tuple(claims["even_centred_blocked"])
        and all(facts.even_centred_minor_identity)
        and facts.odd_centred_live == ODD_CENTRED_LIVE_SLOTS
        and facts.escape_gram_matches
        and facts.escape_inertia == ESCAPE_INERTIA
        and facts.escape_in_cone
        and facts.escape_structural_zeros
        == (ESCAPE_STRUCTURAL_ZEROS,) * len(ODD_CENTRED)
        and facts.closure_diagonal_law
        and facts.closure_only_odd_shears
        and len(facts.closure_determinants) == 1
        and sp.expand(
            facts.closure_determinants[0] - claims["closure_determinant"]
        )
        == 0
        and len(facts.pooled_determinants) == 1
        and sp.expand(facts.pooled_determinants[0] - POOLED_DETERMINANT) == 0
        and facts.closure_ranks == (FORCING_RANK,)
        and facts.closure_mass_ranks == (FORCING_RANK,)
        and facts.endgame_gram_vanishes
        and (
            facts.endgame_diagonal_vanishes and facts.endgame_minor_identity
        )
        == bool(claims["psd_forces_identically_zero"])
        and facts.exact_no_float
    )

    gate_f = bool(
        facts.x0_symmetric
        and facts.x0_diagonal_shapes
        and facts.x0_diagonal_signs == X0_DIAGONAL_SIGNS
        and facts.x0_distinct_sums == X0_DISTINCT_SUMS
        and facts.x0_blocks == X0_BLOCKS
        and facts.x0_block_signs
        == tuple(tuple(pair) for pair in claims["x0_block_signs"])
        and len(facts.x0_cone_census) == len(CONE_CARRIERS)
        and all(
            inertia == X0_CONE_INERTIA and definite == X0_DEFINITE_BLOCKS
            for _, inertia, definite in facts.x0_cone_census
        )
        and facts.half_hodge_inertias
        == (HALF_HODGE_INERTIA,) * len(CONE_CARRIERS)
        and facts.x0_orbit_inertias == (X0_CONE_INERTIA,)
        and facts.x0_average_inertia == X0_CONE_INERTIA
        and facts.envelope_sign_preserving[0]
        and not facts.envelope_sign_flipping[0]
        and (
            facts.envelope_sign_preserving[1],
            facts.envelope_sign_flipping[1],
        )
        == tuple(tuple(item) for item in claims["envelope_inertias"])
        and facts.exact_no_float
    )

    gate_g = bool(
        facts.bare_reflections == ODD_CENTRED
        and facts.bare_translation_count == claims["bare_translation_count"]
        and facts.theta_bare_hits == claims["theta_bare_hits"]
        and facts.theta_gauges == THETA_GAUGES
        and facts.unmatched_moves == 0
        and facts.bare_cross_validated
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
        help="also run the full 64-move x 16-edge covariance sweep",
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
        "main plus the committed Block 147 note/runner and Block 145 note/runner artifacts are content-bound",
        gate_values["A"],
    )
    checks.check(
        "B-orbit",
        "all 128 affine cover moves descend, but the family's off-diagonal weight sits on the DIAGONAL bond (directions (1,3) and (7,1)), so exactly the 64 with e_t = e_x act on the 64 moduli -- four acting moves verified by the exact 32x32 cover identity and four rejected ones by an explicit support escape; those 64 form a group of order 64 acting on carriers through order 32 with kernel {identity, four-step time shift}; the ANTIPERIODIC time translation does NOT descend for any j != 0 while the plain cover shift does, with shift^4 = -I; and the eight half-swapping translations are NOT involutions",
        gate_values["B"],
    )
    checks.check(
        "C-covariance",
        "the honest identity g Q[d;c] g^-1 = Q[d_g; g*c] (daggered on a reflection) holds 64/64 on the four generators against all sixteen healed edges symbolically in (s_x,s_t) and on the free 64-modulus family, and 64/64 on a sixteen-move by four-edge spot sweep; the inlined action law is pinned against the committed Block 145 routine; the full 64x16 = 1024 sweep is available behind --deep",
        gate_values["C"],
    )
    checks.check(
        "D-migration-core",
        "diag Herm([theta H_q(y)]_{++}) = 0 is an IDENTITY in the moduli (linear entries, zero trace, every 2x2 minor -g^2, and the zero diagonal reproduced at all 64 substitution instances), so EVERY weighted ensemble average inherits it and PSD forces the averaged mass Gram to vanish; per-element cross-Hermiticity holds 16/16 on a theta-closed orbit sample, a non-uniformly weighted theta-closed ensemble is Hermitian with a zero-diagonal nonzero (4,0,4) mass Gram, and the three non-closed controls -- partners dropped, weights not theta-symmetric, the same connection on both members -- all FAIL",
        gate_values["D"],
    )
    checks.check(
        "E-escape-and-closure",
        "of the eight honest OS reflections the four EVEN-x-centred ones are blocked exactly as in Block 147 (zero diagonal, minors -g^2) while the four ODD-x-centred ones are LIVE with four nonzero diagonal entries; theta'=(-1,7,-1,1) has an exact physical-cone carrier with Gram diag(15/64,0,15/64,0,0,15/64,0,15/64) of inertia (4,4,0), so the parent's mechanism genuinely fails; but on the HERMITIAN part diag A = m diag G with four structural zeros, the forced rows give det(M^T M) = (s_t^2+s_x^2)^6 (4m^2+s_t^2+s_x^2)^2/2^48 on every chart-0/1 edge (pooled: the same over 2^32), rank 8 at m = 0, 1, -1, 7/3, so all eight odd shears vanish, G = 0, diag A = 0 and a positive odd-centred pairing is IDENTICALLY ZERO",
        gate_values["E"],
    )
    checks.check(
        "F-x0-complement",
        "[X_0 H_q]_{++} has eight PAIRWISE DISTINCT four-term volume sums on its diagonal, four positive and four negative, and four disjoint SAME-SIGN 2x2 blocks (0,7),(2,5) positive and (1,4),(3,6) negative, which are DEFINITE in the cone -- inertia (4,0,4) at four cone carriers, at all 64 orbit members and at the uniform ensemble average, with H_q[+,+] positive definite there; THE CONE PREMISE IS LOAD-BEARING, carried as two checked linear-envelope counterexamples: an oversized shear with the SAME diagonal signs gives (3,0,5) and sign-flipped volume moduli give (8,0,0)",
        gate_values["F"],
    )
    checks.check(
        "G-bare-atlas",
        "the four ODD-x-centred reflections transport the connection onto the committed four-chart table with NO gauge on all four charts, while canonical theta has ZERO bare hits and needs r_x or r_x r_t; sixteen pure translations are bare too, so the uniqueness is UNIQUENESS AMONG THE OS REFLECTIONS and is stated that way; nothing in the tested set is unmatched, and the hash lookup is cross-validated against an explicit symbolic comparison",
        gate_values["G"],
    )
    checks.check(
        "H-note-scope",
        "the orbit characterisation with its non-involutive half-swaps and the antiperiodic-shift fact, the identity-in-the-moduli migration core over arbitrary ensembles, the odd-centred escape with its 15/64 witness and its genuine failure of the parent's step, the Hermitian-part closure with its determinant and its identically-zero conclusion, the per-edge/pooled honesty, the X_0 rewrite with its pairwise-distinct definite blocks and the load-bearing cone premise, the bare-atlas uniqueness, the named next question, the cross-context disclosure, the firewalls and the exact N5 fence are present",
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
