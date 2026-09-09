#!/usr/bin/env python3
"""Cycle 882: the readout-identity half of the R-eta closure obligation.

The pinned obligation `AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md`
asks a closing theorem for TWO things: a physical carrier/source-action bridge,
AND "either a native eta/holonomy identity or a genuinely inhomogeneous
Record-facing normalization theorem".  The bridge half was priced on the sibling
lineage (Cycle 871, PR #5926).  THIS cycle attacks the other half.

Prior art is load bearing and is quoted, not paraphrased.  The homogeneous
Record-additive C3-covariant symmetry-only pin is DEAD: the pinned stretch
no-go exhibits a one-parameter family `I_alpha(x0,x1,x2) = alpha (x0+x1+x2)`
with witnesses `alpha in {0, 1/9, 1/3, 1, 2/27}` all satisfying empty-record
normalization, finite additivity and C3 covariance.  That family is this
block's falsification surface: every constraint derived below is evaluated
against every witness and the survivor set is emitted computed.

(A) PRIOR ART AS DATA.  The obligation and the two 2026-07-04 no-go notes are
    SHA-256 and git-blob pinned, read as text only, and their live-route and
    escape-condition sections are extracted verbatim.  The live routes are
    emitted as an enumerated table, not summarised.  The two notes both use the
    letter `alpha` for DIFFERENT objects; the collision is certified apart.

(B) THE ATTACK.  Working from the four axioms + approved primitives only (no
    new axiom, no new primitive, no comparator, no fitted value), the readout
    functional space is rebuilt by exact linear algebra, "genuinely
    inhomogeneous" is given a formal definition with three proved-equivalent
    characterisations, and four route classes are closed by theorem rather than
    prose: homogeneous self-consistency, ratio/comparative observables,
    subdivision intensivity, and multiplicative anchor libraries.

(C) THE OUTCOME.  Negative-shaped and priced: a sharper obstruction plus a
    priced partial.  The five witnesses are shown to be EXACTLY the five
    nameable Record-facing anchors, four of which are axiom-available and none
    of which is the target; the target anchor is excluded from the
    orbit-cardinality group by an exact 2-adic valuation argument; and every
    multiplicative anchor library contains the identity, so no closed algebraic
    anchor rule can ever pin the target uniquely.  The terminal missing lemma
    is classified EQUIVALENT to the obligation at scope, both directions
    computed.

(D) N-GATE.  Eleven routes with ATTEMPTED / RULED-OUT-BY-PRIOR markers and
    pins, the steelman, and the exact scope, all inline.

No floating point enters any certified quantity; every certified number is
exact `Fraction` arithmetic.  Cited artifacts are read as text/AST only and are
blocked from import by a meta-path firewall.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "docs/AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md",
    "docs/ACPHILAMBDA_R_ETA_HCLASS_FIRST_PRINCIPLES_STRETCH_NO_GO_NOTE_2026-07-04.md",
    "docs/ACPHILAMBDA_R_ETA_ANGLE_NATIVE_FRONTIER_NO_GO_NOTE_2026-07-04.md",
    "scripts/frontier_cycle880_visible_point_physics_2026_07_28.py",
)

import ast
from fractions import Fraction
from hashlib import sha256
import importlib.abc
from itertools import combinations, product
import json
from pathlib import Path
import re
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / "outputs" / "readout_identity_cycle882_receipt_2026_07_28.json"
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "4d742bcc68a1e7cdb154b366e671f576e9b719b3206445b97666c812a790e58c",
    AUDIT_INPUT_PATHS[1]:
        "08c15bdc0c2fc2ccd750ca2752260ae02ec2521a70bc0307103c42058a63ed09",
    AUDIT_INPUT_PATHS[2]:
        "83f4ab11435b7f5224c1013768dc56c28dfb56f0ab3fdd5811f9b06251dde665",
    AUDIT_INPUT_PATHS[3]:
        "e9d6f8a1483b87f7b0520ebe04356fcf4910bc5a25d1f7af97555644892d6ee4",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "9a449956422a5687b5b1346f428c9e4e35489038",
    AUDIT_INPUT_PATHS[1]: "e2ca96d22c95e991b76d9ec999f12726398bc3df",
    AUDIT_INPUT_PATHS[2]: "92553eb71833303c5d5f0fa74af6511108a8e54b",
    AUDIT_INPUT_PATHS[3]: "db0472a8fe3e9e93f3f31f8e0b5ac0fd5c6630f8",
}
REQUIRED_AST_MARKERS = {
    AUDIT_INPUT_PATHS[3]: ("BRANCH_PINS", "AUDIT_INPUT_PATHS"),
}

# Verbatim evidence located inside the pinned artifacts by exact substring
# search.  These are quotations, not paraphrases: if a pinned text does not
# contain them character for character the pins certificate fails.
REQUIRED_QUOTES = {
    AUDIT_INPUT_PATHS[0]: (
        "readout is the fixed-locus density class `h`, identity-read in "
        "`h`-units as the",
        "A closing theorem must provide a physical carrier/source-action "
        "bridge and",
        "either a native eta/holonomy identity or a genuinely inhomogeneous "
        "Record-facing",
        "normalization theorem. It must derive the density-to-angle equality "
        "instead of",
        "packaging it as a convention or target-fitted readout.",
    ),
    AUDIT_INPUT_PATHS[1]: (
        "I_alpha(x0, x1, x2) = alpha (x0 + x1 + x2).",
        "I_alpha(1,1,1) = L3(1,2) = 2/9,",
        "alpha = 2/27.",
        "But `alpha = 0`, `alpha = 1/9`, `alpha = 1/3`, `alpha = 1`, and",
        "`alpha = 2/27` all satisfy empty-record normalization, finite "
        "additivity,",
        "and C3 covariance on the same supplied frame.",
        "The C3 covariance constraint forces equality of the three cell "
        "coefficients;",
        "it does not force the coefficient `alpha`.",
        "Fails: covariance leaves the scalar coefficient free.",
        "1. **h-class theorem.** Derive that the physical charged-lepton "
        "scalar readout",
        "5. **Approved-primitive proposal.** Seek approval for a narrow "
        "readout",
    ),
    AUDIT_INPUT_PATHS[2]: (
        "Homogeneous self-consistency/readout maps",
        "are closed under global rescale. A homogeneous fixed-point equation "
        "either",
        "forces the zero/on-locus member or leaves the whole line free. It "
        "never",
        "isolates the nonzero off-locus member `Phi = 2/3`.",
        "2. **Record-facing inhomogeneous readout theorem.** Derive a scalar",
        "   singleton readout clause that pins the fixed-locus density member "
        "rather",
        "   than the count member or the zero member.",
        "the only zero-offset linear map `Phi = alpha S_sum` that hits the "
        "target is",
        "`alpha = 1`, which is exactly the unlicensed fixed-locus-to-angle "
        "bridge.",
        "  fixed-locus sum S_sum = 2/3",
        "A future angle-native theorem is not ruled out. It must supply the",
        "inhomogeneous license rather than merely writing `Phi = S_sum`.",
    ),
}

# Commit pins for artifacts on this branch's history.  Pins, not reads.
BRANCH_PINS = {
    "cycle868_block_commit": "9506d38958",
    "cycle873_block_commit": "d38a5ae809",
    "cycle876_block_commit": "311d83e951",
    "cycle880_runner_commit": "b11ac86dfd",
    "cycle880_checker_commit": "1068ce3303",
    "cycle880_block_commit": "a5d501944f",
    "obligation_commit": "ae9f477368",
    "cycle871_runner_present_in_this_worktree": False,
    "cycle871_receipt_present_in_this_worktree": False,
}

# The letter `alpha` names two DIFFERENT objects in the two pinned no-gos.
# This block works in the STRETCH note's coordinate.  The collision is a real
# integrity hazard and is certified apart rather than silently merged.
ALPHA_COORDINATE = "stretch_note_readout_coefficient"

ORBIT_LENGTH = 3
FULL_ORBIT = (Fraction(1), Fraction(1), Fraction(1))
L3_FIXED_LOCUS_DENSITY = Fraction(2, 9)      # `L3(1,2) = 2/9`, pinned
S_SUM = Fraction(2, 3)                       # `S_sum = 2/3`, pinned
TARGET_ALPHA = Fraction(2, 27)               # `alpha = 2/27`, pinned

# The five pinned witnesses.  Order is the order of the pinned sentence.
PINNED_WITNESSES = (
    Fraction(0),
    Fraction(1, 9),
    Fraction(1, 3),
    Fraction(1),
    Fraction(2, 27),
)

# Extra alphas this runner tests beyond the pinned five.  The independent
# checker tests a disjoint and larger adversarial set.
EXTRA_ALPHAS = (
    Fraction(2, 9), Fraction(2, 3), Fraction(1, 27), Fraction(-2, 27),
    Fraction(1, 2), Fraction(4, 27), Fraction(-1),
)

STRENGTH_CLASSES = ("WEAKER", "EQUIVALENT", "STRONGER", "INCOMPARABLE")
ROUTE_MARKERS = ("ATTEMPTED", "RULED-OUT-BY-PRIOR")

LABELS = (
    "A_PINS",
    "B_PRIOR_ART_AS_DATA",
    "C_READOUT_SPACE",
    "D_GENUINE_INHOMOGENEITY",
    "E_HOMOGENEOUS_DICHOTOMY",
    "F_RATIO_BLINDNESS",
    "G_INTENSIVITY",
    "H_ANCHOR_BIJECTION",
    "I_CARDINALITY_GROUP",
    "J_IDENTITY_OBSTRUCTION",
    "K_ALPHA_WITNESS_TABLE",
    "L_TERMINAL_LEMMA",
    "M_OUTCOME_AND_PRICE",
    "N_NO_GO_GATE",
    "O_CONTROLS",
)


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if any cited source-only primary is imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self, fullname: str, path: object = None, target: object = None
    ) -> None:
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def _read_bytes(path: str) -> bytes:
    return (ROOT / path).read_bytes()


def _read_text(path: str) -> str:
    return _read_bytes(path).decode("utf-8")


def _git_blob(raw: bytes) -> str:
    from hashlib import sha1
    return sha1(b"blob %d\0" % len(raw) + raw).hexdigest()


def q(value: Fraction) -> str:
    """Exact rational rendered as text; no float ever touches a certificate."""
    return f"{value.numerator}/{value.denominator}"


def digest(payload: object) -> str:
    return sha256(
        json.dumps(payload, sort_keys=True, default=str).encode("utf-8")
    ).hexdigest()


def v2(value: Fraction) -> int | None:
    """2-adic valuation of a nonzero rational; None at zero."""
    if value == 0:
        return None
    n, d, e = abs(value.numerator), value.denominator, 0
    while n % 2 == 0:
        n //= 2
        e += 1
    while d % 2 == 0:
        d //= 2
        e -= 1
    return e


def v3(value: Fraction) -> int | None:
    if value == 0:
        return None
    n, d, e = abs(value.numerator), value.denominator, 0
    while n % 3 == 0:
        n //= 3
        e += 1
    while d % 3 == 0:
        d //= 3
        e -= 1
    return e


# --------------------------------------------------------------------------
# exact linear algebra over Q (nullspace of a small rational matrix)
# --------------------------------------------------------------------------
def rref(rows: list[list[Fraction]]) -> tuple[list[list[Fraction]], list[int]]:
    mat = [list(row) for row in rows]
    pivots: list[int] = []
    r = 0
    if not mat:
        return mat, pivots
    ncols = len(mat[0])
    for c in range(ncols):
        piv = None
        for i in range(r, len(mat)):
            if mat[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        mat[r], mat[piv] = mat[piv], mat[r]
        lead = mat[r][c]
        mat[r] = [value / lead for value in mat[r]]
        for i in range(len(mat)):
            if i != r and mat[i][c] != 0:
                factor = mat[i][c]
                mat[i] = [
                    a - factor * b for a, b in zip(mat[i], mat[r])
                ]
        pivots.append(c)
        r += 1
        if r == len(mat):
            break
    return mat, pivots


def nullspace(rows: list[list[Fraction]], ncols: int) -> list[list[Fraction]]:
    mat, pivots = rref(rows)
    free = [c for c in range(ncols) if c not in pivots]
    basis: list[list[Fraction]] = []
    for f in free:
        vec = [Fraction(0)] * ncols
        vec[f] = Fraction(1)
        for i, p in enumerate(pivots):
            vec[p] = -mat[i][f]
        basis.append(vec)
    return basis


# --------------------------------------------------------------------------
# the affine normal form in the single unknown alpha
# --------------------------------------------------------------------------
def solve_affine(rows: tuple[tuple[Fraction, Fraction], ...]) -> tuple[str, object]:
    """rows are (c, k) meaning `c * alpha == k`.  Exact solution set over Q."""
    sol: Fraction | None = None
    for c, k in rows:
        if c == 0:
            if k != 0:
                return ("EMPTY", None)
            continue
        here = k / c
        if sol is None:
            sol = here
        elif sol != here:
            return ("EMPTY", None)
    if sol is None:
        return ("ALL_OF_Q", None)
    return ("SINGLETON", sol)


def is_homogeneous(rows: tuple[tuple[Fraction, Fraction], ...]) -> bool:
    return all(k == 0 for _, k in rows)


def satisfies(rows: tuple[tuple[Fraction, Fraction], ...], alpha: Fraction) -> bool:
    return all(c * alpha == k for c, k in rows)


# --------------------------------------------------------------------------
# the readout model: records, functionals, evaluation
# --------------------------------------------------------------------------
def readout(alpha: Fraction, record: tuple[tuple[Fraction, ...], ...]) -> Fraction:
    """`I_alpha` on a record given as a tuple of disjoint C3-orbit copies."""
    return alpha * sum(sum(orbit) for orbit in record)


TEST_RECORDS: tuple[tuple[str, tuple[tuple[Fraction, ...], ...]], ...] = (
    ("empty", ()),
    ("full_orbit", (FULL_ORBIT,)),
    ("single_cell", ((Fraction(1), Fraction(0), Fraction(0)),)),
    ("two_cells", ((Fraction(1), Fraction(1), Fraction(0)),)),
    ("two_copies", (FULL_ORBIT, FULL_ORBIT)),
    ("three_copies", (FULL_ORBIT, FULL_ORBIT, FULL_ORBIT)),
    ("mixed", ((Fraction(2), Fraction(0), Fraction(1)),
               (Fraction(0), Fraction(3), Fraction(0)))),
)


# --------------------------------------------------------------------------
# certificate A: pins
# --------------------------------------------------------------------------
def pins_certificate() -> dict:
    rows = []
    ok = True
    for path in AUDIT_INPUT_PATHS:
        raw = _read_bytes(path)
        got_sha = sha256(raw).hexdigest()
        got_blob = _git_blob(raw)
        sha_ok = got_sha == EXPECTED_SHA256[path]
        blob_ok = got_blob == EXPECTED_GIT_BLOBS[path]
        text = raw.decode("utf-8")
        missing = [
            quote for quote in REQUIRED_QUOTES.get(path, ())
            if quote not in text
        ]
        markers = REQUIRED_AST_MARKERS.get(path, ())
        marker_missing: list[str] = []
        if markers:
            tree = ast.parse(raw, filename=path)
            names = {
                node.id for node in ast.walk(tree) if isinstance(node, ast.Name)
            }
            marker_missing = [m for m in markers if m not in names]
        row_ok = sha_ok and blob_ok and not missing and not marker_missing
        ok = ok and row_ok
        rows.append({
            "path": path,
            "sha256": got_sha,
            "sha256_matches_pin": sha_ok,
            "git_blob": got_blob,
            "git_blob_matches_pin": blob_ok,
            "quotes_required": len(REQUIRED_QUOTES.get(path, ())),
            "quotes_missing": missing,
            "ast_markers_missing": marker_missing,
            "read_mode": "text/AST only; never imported",
            "pass": row_ok,
        })
    return {
        "rows": rows,
        "branch_pins": dict(BRANCH_PINS),
        "finding": (
            "Every cited artifact matched its pinned SHA-256 and git blob and "
            "contained each required quotation character for character."
            if ok else
            "At least one cited artifact failed its pin or quote check."
        ),
        "pass": ok,
    }


# --------------------------------------------------------------------------
# certificate B: prior art as data
# --------------------------------------------------------------------------
def _extract_section(text: str, header: str) -> str:
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.strip() == header:
            start = i + 1
            break
    if start is None:
        return ""
    out = []
    for line in lines[start:]:
        if line.startswith("## "):
            break
        out.append(line)
    return "\n".join(out).strip()


def _enumerate_routes(section: str) -> list[dict]:
    routes = []
    for match in re.finditer(
        r"^(\d+)\. \*\*(.+?)\*\*(.*?)(?=^\d+\. \*\*|\Z)",
        section + "\n", re.S | re.M,
    ):
        body = " ".join((match.group(3) or "").split())
        routes.append({
            "index": int(match.group(1)),
            "name": match.group(2).strip(),
            "text": body,
        })
    return routes


def prior_art_certificate() -> dict:
    obligation = _read_text(AUDIT_INPUT_PATHS[0])
    stretch = _read_text(AUDIT_INPUT_PATHS[1])
    frontier = _read_text(AUDIT_INPUT_PATHS[2])

    closure = _extract_section(obligation, "## Closure criterion")
    stretch_live = _extract_section(stretch, "## Remaining Live Routes")
    stretch_dead = _extract_section(stretch, "## What Does Not Move")
    frontier_live = _extract_section(frontier, "## Remaining Live Routes")
    frontier_dead = _extract_section(frontier, "## What Does Not Move")

    stretch_routes = _enumerate_routes(stretch_live)
    frontier_routes = _enumerate_routes(frontier_live)

    # The obligation's own two-clause structure, quoted rather than described.
    bridge_clause = "a physical carrier/source-action bridge" in closure
    disjunct_native = "a native eta/holonomy identity" in closure
    disjunct_inhomog = (
        "a genuinely inhomogeneous Record-facing" in closure
        and "normalization theorem" in closure
    )

    # Recover the sibling-lineage Cycle-871 reference from the pinned Cycle-880
    # runner by AST rather than transcribing it.
    tree = ast.parse(_read_bytes(AUDIT_INPUT_PATHS[3]), filename=AUDIT_INPUT_PATHS[3])
    cycle871_reference = ""
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            targets = [t.id for t in node.targets if isinstance(t, ast.Name)]
            if "BRANCH_PINS" in targets and isinstance(node.value, ast.Dict):
                for key, value in zip(node.value.keys, node.value.values):
                    if (isinstance(key, ast.Constant)
                            and key.value == "cycle871_reference"):
                        cycle871_reference = ast.literal_eval(value)
    dim_match = re.search(r"free dimension (\d+)", cycle871_reference)
    pinned_871_dimension = int(dim_match.group(1)) if dim_match else None

    # The alpha name collision, certified apart.
    collision = {
        "stretch_note_alpha": (
            "coefficient of the Record-additive C3-covariant readout: "
            "I_alpha(x0,x1,x2) = alpha (x0+x1+x2); target member alpha = 2/27"
        ),
        "frontier_note_alpha": (
            "coefficient of the zero-offset holonomy map Phi = alpha S_sum; "
            "the only member hitting the target is alpha = 1"
        ),
        "same_letter_different_object": True,
        "this_block_works_in": ALPHA_COORDINATE,
        "stretch_alpha_one_reads": q(readout(Fraction(1), (FULL_ORBIT,))),
        "frontier_alpha_one_reads": q(Fraction(1) * S_SUM),
        "values_differ": readout(Fraction(1), (FULL_ORBIT,)) != Fraction(1) * S_SUM,
    }

    ok = (
        bool(closure) and bridge_clause and disjunct_native and disjunct_inhomog
        and len(stretch_routes) == 5 and len(frontier_routes) == 4
        and bool(stretch_dead) and bool(frontier_dead)
        and bool(cycle871_reference)
        and collision["values_differ"]
    )
    return {
        "obligation_closure_criterion_verbatim": closure,
        "obligation_has_bridge_clause": bridge_clause,
        "obligation_disjunct_1_native_identity": disjunct_native,
        "obligation_disjunct_2_inhomogeneous_normalization": disjunct_inhomog,
        "this_cycle_attacks": "disjunct_2_inhomogeneous_Record_facing_normalization",
        "stretch_note_live_routes": stretch_routes,
        "frontier_note_live_routes": frontier_routes,
        "stretch_note_what_does_not_move_verbatim": stretch_dead,
        "frontier_note_what_does_not_move_verbatim": frontier_dead,
        "cycle871_reference_recovered_from_cycle880_by_ast": cycle871_reference,
        "cycle871_free_dimension_per_on_branch_pin": pinned_871_dimension,
        "cycle871_runner_absent_from_this_worktree": True,
        "cycle871_dimension_discrepancy_note": (
            "The task brief describes 871's priced free dimension as 2; the "
            "only 871 statement PRESENT on this branch is the Cycle-880 "
            "BRANCH_PINS string recovered above, which says free dimension "
            f"{pinned_871_dimension}. The 871 runner itself is not in this "
            "worktree, so its number cannot be recomputed here. Both readings "
            "are emitted as DATA; nothing below depends on which is right."
        ),
        "alpha_name_collision": collision,
        "finding": (
            "The obligation's closure criterion is a conjunction (bridge AND a "
            "disjunction); this block attacks the second disjunct. Nine live "
            "routes are enumerated verbatim across the two pinned no-gos, and "
            "the two notes' clashing uses of the letter alpha are separated."
        ),
        "pass": ok,
    }


# --------------------------------------------------------------------------
# certificate C: the readout space, rebuilt not transcribed
# --------------------------------------------------------------------------
def readout_space_certificate() -> dict:
    """Derive the alpha-family instead of quoting it.

    A Record-additive scalar on a 3-cell orbit is linear: I(x) = a0 x0 + a1 x1
    + a2 x2 with I(0) = 0 (empty-record normalization).  C3 covariance under
    the cyclic shift imposes I(sigma x) = I(x) for all x, i.e. two independent
    linear conditions on (a0, a1, a2).  The nullspace is computed exactly.
    """
    # Covariance rows: coefficients of (a0, a1, a2) in I(sigma x) - I(x) = 0
    # evaluated on the standard basis records e0, e1, e2.
    shift = (1, 2, 0)  # sigma sends cell i to cell shift[i]
    rows: list[list[Fraction]] = []
    for j in range(ORBIT_LENGTH):
        row = [Fraction(0)] * ORBIT_LENGTH
        row[shift[j]] += Fraction(1)
        row[j] -= Fraction(1)
        rows.append(row)
    basis = nullspace(rows, ORBIT_LENGTH)
    dim = len(basis)
    generator = basis[0] if dim == 1 else None
    normalised = None
    if generator is not None and generator[0] != 0:
        normalised = tuple(c / generator[0] for c in generator)

    # The family recovered above is exactly I_alpha(x) = alpha * (x0+x1+x2).
    family_matches = normalised == (Fraction(1), Fraction(1), Fraction(1))

    # Target member, DERIVED from the pinned fixed-locus arithmetic.
    derived_target = L3_FIXED_LOCUS_DENSITY / ORBIT_LENGTH
    target_matches_pin = derived_target == TARGET_ALPHA
    sum_identity = ORBIT_LENGTH * L3_FIXED_LOCUS_DENSITY == S_SUM

    witness_rows = []
    for alpha in PINNED_WITNESSES + EXTRA_ALPHAS:
        additive = all(
            readout(alpha, a + b) == readout(alpha, a) + readout(alpha, b)
            for a in (TEST_RECORDS[1][1], TEST_RECORDS[2][1])
            for b in (TEST_RECORDS[3][1], TEST_RECORDS[6][1])
        )
        covariant = all(
            readout(alpha, (tuple(orb[shift.index(i)] for i in range(3)),))
            == readout(alpha, (orb,))
            for orb in (FULL_ORBIT, (Fraction(2), Fraction(0), Fraction(1)))
        )
        witness_rows.append({
            "alpha": q(alpha),
            "pinned_witness": alpha in PINNED_WITNESSES,
            "empty_record_reads_zero": readout(alpha, ()) == 0,
            "finitely_additive": additive,
            "c3_covariant": covariant,
            "full_orbit_reads": q(readout(alpha, (FULL_ORBIT,))),
        })
    all_survive = all(
        row["empty_record_reads_zero"] and row["finitely_additive"]
        and row["c3_covariant"] for row in witness_rows
    )
    ok = (
        dim == 1 and family_matches and target_matches_pin and sum_identity
        and all_survive
    )
    return {
        "covariance_rows": [[q(c) for c in row] for row in rows],
        "nullspace_dimension": dim,
        "nullspace_generator_normalised": (
            [q(c) for c in normalised] if normalised else None),
        "family_is_alpha_times_orbit_sum": family_matches,
        "free_dimension_from_symmetry_alone": dim,
        "L3_fixed_locus_density": q(L3_FIXED_LOCUS_DENSITY),
        "target_alpha_derived": q(derived_target),
        "target_alpha_matches_pinned_2_over_27": target_matches_pin,
        "three_times_2_over_9_equals_S_sum": sum_identity,
        "witness_rows": witness_rows,
        "every_tested_alpha_satisfies_the_symmetry_only_constraints": all_survive,
        "finding": (
            f"The C3-covariant Record-additive readout space has exact "
            f"dimension {dim}; the symmetry-only constraint set therefore "
            f"leaves a full line of readouts, and all "
            f"{len(witness_rows)} tested members satisfy it. The target member "
            f"alpha = {q(derived_target)} is DERIVED as L3(1,2)/3 rather than "
            f"transcribed. This reproduces the pinned no-go from scratch."
        ),
        "pass": ok,
    }


# --------------------------------------------------------------------------
# certificate D: what "genuinely inhomogeneous" must mean
# --------------------------------------------------------------------------
def constraint_library() -> list[dict]:
    """Every candidate constraint, in affine normal form `c*alpha == k`."""
    lib: list[dict] = []

    def add(cid, name, rows, provenance, kind):
        lib.append({
            "id": cid, "name": name, "rows": rows,
            "provenance": provenance, "kind": kind,
        })

    add("K0_SYMMETRY_ONLY",
        "empty-record normalization + finite additivity + C3 covariance",
        (), "pinned stretch no-go (DEAD route, not re-attempted)", "SYMMETRY")
    add("K1_COUNT_ONCE",
        "Record count-once: re-registering a registered cell adds nothing",
        (), "axiom Record", "SYMMETRY")
    for lam in (Fraction(0), Fraction(1, 3), Fraction(1, 2), Fraction(2, 3),
                Fraction(1), Fraction(2), Fraction(3), Fraction(-1)):
        add(f"K2_HOMOG_FIXPOINT_lam_{q(lam).replace('/', '_')}",
            f"homogeneous self-consistency I = ({q(lam)}) I",
            ((Fraction(1) - lam, Fraction(0)),),
            "frontier no-go bin 2, upgraded from prose to affine normal form",
            "HOMOGENEOUS")
    for n in (2, 3, 5):
        add(f"K3_INTENSIVE_n{n}",
            f"subdivision intensivity: {n} disjoint copies read as one",
            ((Fraction(ORBIT_LENGTH * (n - 1)), Fraction(0)),),
            "the word 'density' in the obligation, read as intensivity",
            "HOMOGENEOUS")
    anchors = anchor_library()
    for a in anchors:
        add(f"K4_ANCHOR_{a['id']}",
            f"Record-facing anchor: one full orbit reads {q(a['k'])}",
            ((Fraction(ORBIT_LENGTH), a["k"]),),
            a["provenance"], "AFFINE")
    return lib


def anchor_library() -> list[dict]:
    """The nameable Record-facing anchor constants on one full C3 orbit."""
    return [
        {"id": "NULL", "k": Fraction(0),
         "name": "the null reading (the zero member)",
         "axiom_available": True,
         "provenance": "Record: the empty reading, extended to the full orbit"},
        {"id": "INVERSE_MULTIPLICITY", "k": Fraction(1, 3),
         "name": "one over the orbit multiplicity, 1/|C3|",
         "axiom_available": True,
         "provenance": "Lattice/Record: the orbit cardinality 3, inverted"},
        {"id": "UNIT", "k": Fraction(1),
         "name": "the unit reading (one orbit reads one)",
         "axiom_available": True,
         "provenance": "Record: normalisation of a single registered orbit"},
        {"id": "COUNT", "k": Fraction(3),
         "name": "the cell count (the count member)",
         "axiom_available": True,
         "provenance": "Lattice/Record: cardinality of the orbit"},
        {"id": "FIXED_LOCUS_DENSITY", "k": L3_FIXED_LOCUS_DENSITY,
         "name": "the fixed-locus density L3(1,2) = 2/9 (THE TARGET)",
         "axiom_available": False,
         "provenance": (
             "retained fixed-locus arithmetic; its BINDING to the readout is "
             "exactly the open R-eta license")},
    ]


def genuine_inhomogeneity_certificate(lib: list[dict]) -> dict:
    """Three characterisations of 'genuinely inhomogeneous', proved equal.

    P1  the affine normal form carries a nonzero constant term (some k != 0);
    P2  the solution set is a nonzero singleton;
    P3  the solution set is NOT closed under alpha -> lambda alpha.
    """
    scale_tests = (Fraction(2), Fraction(1, 2), Fraction(-3), Fraction(5, 7))
    rows = []
    ok = True
    for entry in lib:
        rr = entry["rows"]
        kind, sol = solve_affine(rr)
        p1 = any(k != 0 for _, k in rr)
        p2 = kind == "SINGLETON" and sol != 0
        # P3: exhibit a scaling that leaves the solution set.
        probe = [a for a in PINNED_WITNESSES + EXTRA_ALPHAS if satisfies(rr, a)]
        p3 = any(
            not satisfies(rr, lam * a)
            for a in probe for lam in scale_tests
        )
        agree = (p1 == p2 == p3)
        ok = ok and agree
        rows.append({
            "constraint_id": entry["id"],
            "kind": entry["kind"],
            "solution_kind": kind,
            "solution": q(sol) if isinstance(sol, Fraction) else None,
            "P1_nonzero_constant_term": p1,
            "P2_nonzero_singleton": p2,
            "P3_not_scaling_closed": p3,
            "three_characterisations_agree": agree,
        })
    genuinely = [r["constraint_id"] for r in rows if r["P1_nonzero_constant_term"]]
    return {
        "definition": (
            "A constraint system on the readout line is GENUINELY "
            "INHOMOGENEOUS iff its affine normal form c*alpha = k carries a "
            "nonzero constant term k. Equivalently (proved below over the "
            "whole library) iff its solution set is a nonzero singleton; "
            "equivalently iff its solution set is not closed under global "
            "rescale."
        ),
        "equivalence_rows": rows,
        "all_three_characterisations_agree_everywhere": ok,
        "genuinely_inhomogeneous_members": genuinely,
        "corollary_constant_must_be_readout_independent": (
            "If k is itself computed from readouts, k = f(I) with f homogeneous "
            "of degree 1, then substituting returns a homogeneous system and P1 "
            "fails. Hence the inhomogeneous constant must be supplied by "
            "content that is NOT the readout. That is the formal content of "
            "the obligation's word 'genuinely'."
        ),
        "finding": (
            f"'Genuinely inhomogeneous' is pinned to a single testable "
            f"predicate, and the three candidate readings of it coincide on "
            f"every one of the {len(rows)} library members. Exactly "
            f"{len(genuinely)} members qualify, and all of them are anchor "
            f"constraints."
        ),
        "pass": ok and bool(genuinely),
    }


# --------------------------------------------------------------------------
# certificate E: the homogeneous dichotomy theorem
# --------------------------------------------------------------------------
def homogeneous_dichotomy_certificate(lib: list[dict]) -> dict:
    """THEOREM. A homogeneous constraint set has solution set {0} or all of Q.

    Proof (machine-checked member by member): with every k = 0, alpha = 0
    solves every row, so the set is never empty; and if alpha0 != 0 solves it
    then so does lambda*alpha0 for every lambda in Q, and {lambda*alpha0} = Q.
    Hence the set is {0} or Q and can never be the nonzero singleton the
    obligation needs.
    """
    lam_probe = (Fraction(2), Fraction(1, 2), Fraction(-1), Fraction(7, 5),
                 Fraction(2, 27), Fraction(9, 2))
    rows = []
    ok = True
    for entry in lib:
        if entry["kind"] == "AFFINE":
            continue
        rr = entry["rows"]
        homog = is_homogeneous(rr)
        kind, sol = solve_affine(rr)
        zero_solves = satisfies(rr, Fraction(0))
        closed = all(
            satisfies(rr, lam * a)
            for a in PINNED_WITNESSES + EXTRA_ALPHAS if satisfies(rr, a)
            for lam in lam_probe
        )
        dichotomy = kind in ("ALL_OF_Q",) or (kind == "SINGLETON" and sol == 0)
        row_ok = homog and zero_solves and closed and dichotomy
        ok = ok and row_ok
        rows.append({
            "constraint_id": entry["id"],
            "homogeneous": homog,
            "zero_always_solves": zero_solves,
            "solution_set": (
                "ALL_OF_Q" if kind == "ALL_OF_Q" else f"{{{q(sol)}}}"),
            "scaling_closed": closed,
            "dichotomy_holds": dichotomy,
            "can_be_a_nonzero_singleton": not dichotomy,
            "pass": row_ok,
        })
    return {
        "theorem": (
            "C882-T1. Let S be the solution set in alpha of a constraint "
            "system that is homogeneous OF A SINGLE DEGREE d on the "
            "C3-covariant Record-additive readout line -- equivalently, that "
            "is scaling covariant, F(lambda a) = lambda^d F(a). Then S = {0} "
            "or S = Q. In particular S is never a nonzero singleton, so no "
            "scaling-covariant route can select the target member."
        ),
        "scope_qualification_is_load_bearing": (
            "The single-degree qualification is NOT decoration. Constraints "
            "with merely a zero constant term but MIXED degree escape the "
            "dichotomy: alpha^2 - c alpha = 0 has solution set {0, c}, which "
            "contains a nonzero member. The independent checker exhibits this "
            "counterexample (certificate CE) and the route it opens "
            "(certificate CF); neither closes the obligation, because {0, c} "
            "still retains the zero member and c is still an externally "
            "supplied constant. Every member of this runner's library is "
            "linear, so nothing computed here is affected."
        ),
        "rows": rows,
        "members_checked": len(rows),
        "any_homogeneous_member_pinned_a_nonzero_value": any(
            row["can_be_a_nonzero_singleton"] for row in rows),
        "upgrade_over_prior_art": (
            "The pinned frontier no-go states this as prose ('Homogeneous "
            "self-consistency/readout maps are closed under global rescale'). "
            "Here it is an exact dichotomy with the affine normal form as its "
            "proof, checked on every homogeneous member of the library."
        ),
        "finding": (
            f"All {len(rows)} homogeneous members obey the dichotomy: zero "
            f"always solves, the solution set is scaling closed, and not one of "
            f"them isolates a nonzero member."
        ),
        "pass": ok,
    }


# --------------------------------------------------------------------------
# certificate F: ratio / comparative blindness
# --------------------------------------------------------------------------
def ratio_blindness_certificate() -> dict:
    """THEOREM. Degree-0 rational functionals of readouts are alpha-blind.

    Any observable built as a ratio of readouts (or any degree-0 rational
    combination) is invariant along the whole alpha line off zero.  Hence NO
    comparative Record theorem -- however elaborate -- can pin the member.
    """
    named = [(n, r) for n, r in TEST_RECORDS if r]
    functionals = []
    for (na, ra), (nb, rb) in combinations(named, 2):
        functionals.append((f"I[{na}]/I[{nb}]", ra, rb, 1, 1))
    for (na, ra), (nb, rb) in list(combinations(named, 2))[:6]:
        functionals.append((f"I[{na}]^2/I[{nb}]^2", ra, rb, 2, 2))

    alphas = [a for a in PINNED_WITNESSES + EXTRA_ALPHAS if a != 0]
    rows = []
    ok = True
    for label, ra, rb, pa, pb in functionals:
        values = []
        for alpha in alphas:
            den = readout(alpha, rb)
            if den == 0:
                values = None
                break
            values.append((readout(alpha, ra) ** pa) / (den ** pb))
        if values is None:
            continue
        blind = len(set(values)) == 1
        ok = ok and blind
        rows.append({
            "functional": label,
            "degree": pa - pb,
            "value_common": q(values[0]),
            "alpha_independent": blind,
            "alphas_tested": len(alphas),
        })
    return {
        "theorem": (
            "C882-T2. Every degree-0 rational functional of readouts takes the "
            "same value at every nonzero alpha. Comparative / ratio Record "
            "observables are therefore blind to the member and cannot supply "
            "the inhomogeneous constant."
        ),
        "rows": rows,
        "functionals_checked": len(rows),
        "all_alpha_blind": ok,
        "consequence": (
            "The inhomogeneous constant cannot be manufactured by comparing "
            "readouts to each other. It must be an absolute anchor: an "
            "equation with one side supplied by non-readout content."
        ),
        "finding": (
            f"All {len(rows)} degree-0 functionals returned one common value "
            f"across {len(alphas)} distinct nonzero alphas, so the entire "
            f"comparative sector is certified alpha-blind."
        ),
        "pass": ok and bool(rows),
    }


# --------------------------------------------------------------------------
# certificate G: intensivity kills the whole line
# --------------------------------------------------------------------------
def intensivity_certificate() -> dict:
    """THEOREM. Record-additive AND subdivision-intensive implies alpha = 0.

    The obligation calls the target a DENSITY.  If 'density' is cashed as
    intensivity (n disjoint copies read the same as one), then additivity gives
    n*I = I for n >= 2, hence I = 0.  So the target member is NOT a density in
    the intensive sense; it is an extensive functional whose value on ONE orbit
    coincides with a density.  This closes the 'it is a density, so it is
    normalised' route by theorem.
    """
    rows = []
    ok = True
    for n in (2, 3, 5):
        rr = ((Fraction(ORBIT_LENGTH * (n - 1)), Fraction(0)),)
        kind, sol = solve_affine(rr)
        survivors = [
            q(a) for a in PINNED_WITNESSES if satisfies(rr, a)
        ]
        forced_zero = kind == "SINGLETON" and sol == 0
        ok = ok and forced_zero and survivors == ["0/1"]
        rows.append({
            "copies": n,
            "constraint": f"{ORBIT_LENGTH * n} alpha == {ORBIT_LENGTH} alpha",
            "solution": q(sol) if isinstance(sol, Fraction) else kind,
            "pinned_witnesses_surviving": survivors,
            "target_survives": q(TARGET_ALPHA) in survivors,
        })
    return {
        "theorem": (
            "C882-T3. On the Record-additive readout line, subdivision "
            "intensivity forces alpha = 0. Hence no reading of the word "
            "'density' as intensivity can reach the target member; the target "
            "is extensive and merely agrees with a density on one orbit."
        ),
        "rows": rows,
        "target_survives_intensivity": any(r["target_survives"] for r in rows),
        "consequence": (
            "The obligation's phrase 'fixed-locus density class' cannot be "
            "discharged by a normalisation argument about densities. The "
            "density word is a NAME for the target value, not a constraint "
            "that selects it."
        ),
        "finding": (
            "Intensivity at 2, 3 and 5 copies each collapse the line to the "
            "zero member; the target member survives none of them."
        ),
        "pass": ok,
    }


# --------------------------------------------------------------------------
# certificate H: the witnesses ARE the anchors
# --------------------------------------------------------------------------
def anchor_bijection_certificate() -> dict:
    """THEOREM. alpha = k/3 is a bijection anchors <-> members, and the five
    pinned witnesses are exactly the five nameable Record-facing anchors."""
    anchors = anchor_library()
    rows = []
    for a in anchors:
        alpha = a["k"] / ORBIT_LENGTH
        rr = ((Fraction(ORBIT_LENGTH), a["k"]),)
        kind, sol = solve_affine(rr)
        rows.append({
            "anchor_id": a["id"],
            "anchor_name": a["name"],
            "anchor_constant_k": q(a["k"]),
            "pins_alpha": q(alpha),
            "solution_is_a_singleton": kind == "SINGLETON" and sol == alpha,
            "alpha_is_a_pinned_witness": alpha in PINNED_WITNESSES,
            "axiom_available_without_the_fixed_locus_arithmetic":
                a["axiom_available"],
            "is_the_target": alpha == TARGET_ALPHA,
            "provenance": a["provenance"],
        })
    induced = {a["k"] / ORBIT_LENGTH for a in anchors}
    bijection = induced == set(PINNED_WITNESSES) and len(induced) == len(anchors)
    axiom_alphas = sorted(
        (a["k"] / ORBIT_LENGTH for a in anchors if a["axiom_available"]),
        key=lambda f: (f.numerator, f.denominator),
    )
    target_axiom_available = TARGET_ALPHA in axiom_alphas
    complement = sorted(
        set(PINNED_WITNESSES) - {TARGET_ALPHA},
        key=lambda f: (f.numerator, f.denominator),
    )
    exactly_complement = axiom_alphas == complement
    ok = bijection and all(r["solution_is_a_singleton"] for r in rows)
    return {
        "theorem": (
            "C882-T4. The map k -> k/3 is a bijection from Record-facing "
            "anchor constants to readout members. Under it the five pinned "
            "witnesses {0, 1/9, 1/3, 1, 2/27} are exactly the five nameable "
            "anchors {0, 1/3, 1, 3, 2/9}: null, inverse multiplicity, unit, "
            "count, fixed-locus density. The pinned witness list is therefore "
            "not a list of arbitrary examples -- it IS the anchor library."
        ),
        "rows": rows,
        "anchor_to_member_map_is_a_bijection_onto_the_pinned_witnesses":
            bijection,
        "axiom_available_anchors_pin": [q(a) for a in axiom_alphas],
        "target_alpha": q(TARGET_ALPHA),
        "target_is_axiom_available": target_axiom_available,
        "axiom_available_set_equals_the_complement_of_the_target":
            exactly_complement,
        "corollary": (
            "C882-T5. The anchors available from Lattice + Record cardinality "
            "data alone pin exactly {0, 1/9, 1/3, 1} -- precisely the four "
            "NON-target witnesses. The target member is pinned by the single "
            "anchor k = 2/9, which is the retained fixed-locus arithmetic, and "
            "whose BINDING to the readout is the open license itself."
        ),
        "finding": (
            "Every anchor pins a singleton, the anchor-to-member map is a "
            "bijection onto the five pinned witnesses, and the four "
            "axiom-available anchors pin exactly the four wrong members."
        ),
        "pass": ok,
    }


# --------------------------------------------------------------------------
# certificate I: the orbit-cardinality group misses the target 2-adically
# --------------------------------------------------------------------------
def cardinality_group_certificate() -> dict:
    """THEOREM. No product or quotient of orbit-cardinality data reaches 2/9.

    Anchors built multiplicatively from the single full C3 orbit have only the
    cardinality 3 available.  Every element of <3> has 2-adic valuation 0,
    while v_2(2/9) = 1.  The obstruction is exact and holds at every exponent,
    not just in a scanned window: the '2' in 2/9 comes from the fixed-locus
    weight pair (1,2), not from the C3 orbit.
    """
    window = range(-6, 7)
    elements = [Fraction(3) ** e for e in window]
    valuations = sorted({v2(x) for x in elements})
    target_v2 = v2(L3_FIXED_LOCUS_DENSITY)
    target_v3 = v3(L3_FIXED_LOCUS_DENSITY)
    reachable = L3_FIXED_LOCUS_DENSITY in set(elements)
    ok = valuations == [0] and target_v2 == 1 and not reachable
    return {
        "theorem": (
            "C882-T6. Let G3 = <3> be the multiplicative group generated by "
            "the orbit cardinality. Every g in G3 has v_2(g) = 0, whereas "
            "v_2(2/9) = 1. Hence 2/9 is not in G3 at ANY exponent, and no "
            "anchor assembled multiplicatively from orbit-cardinality data can "
            "be the target anchor."
        ),
        "generator": 3,
        "exponent_window_scanned": [min(window), max(window)],
        "distinct_2_adic_valuations_in_the_group": valuations,
        "target_anchor": q(L3_FIXED_LOCUS_DENSITY),
        "target_2_adic_valuation": target_v2,
        "target_3_adic_valuation": target_v3,
        "target_reachable_in_the_scanned_window": reachable,
        "proof_is_exponent_free": (
            "v_2 is a group homomorphism Q* -> Z and v_2(3) = 0, so v_2 "
            "vanishes on all of <3> regardless of exponent. The window scan is "
            "corroboration, not the proof."
        ),
        "escape_condition_named": (
            "A Record-facing datum with v_2 = 1 must enter. Concretely: derive "
            "that the charged-lepton record carries the fixed-locus weight "
            "pair (1, 2) as Record content. That is a sharper successor target "
            "than 'derive h-class'."
        ),
        "finding": (
            f"The orbit-cardinality group has a single 2-adic valuation "
            f"({valuations}); the target anchor has valuation {target_v2}, so "
            f"the target is arithmetically out of reach of orbit multiplicity "
            f"alone."
        ),
        "pass": ok,
    }


# --------------------------------------------------------------------------
# certificate J: the exact wall -- the identity obstruction
# --------------------------------------------------------------------------
def identity_obstruction_certificate() -> dict:
    """THEOREM (THE EXACT WALL). No multiplicative anchor library selects.

    Widening the anchor library to reach 2/9 is possible -- but any anchor
    library closed under multiplication contains the identity 1, and k = 1 pins
    alpha = 1/3. So the target is never ALONE. Selection therefore cannot come
    from any closed algebraic structure on the anchor constants; it requires a
    genuinely singleton-valued Record predicate. This derives, rather than
    assumes, the pinned frontier note's demand for a 'scalar singleton readout
    clause'.
    """
    primes = (2, 3, 5, 7)
    rows = []
    any_selective = False
    identity_always = True
    for size in (1, 2, 3):
        for gens in combinations(primes, size):
            for w in (1, 2, 3):
                elements = set()
                for exps in product(range(-w, w + 1), repeat=size):
                    value = Fraction(1)
                    for g, e in zip(gens, exps):
                        value *= Fraction(g) ** e
                    elements.add(value)
                contains_identity = Fraction(1) in elements
                identity_always = identity_always and contains_identity
                members = {k / ORBIT_LENGTH for k in elements} | {Fraction(0)}
                survivors = sorted(
                    members & set(PINNED_WITNESSES),
                    key=lambda f: (f.numerator, f.denominator),
                )
                reaches = TARGET_ALPHA in survivors
                selective = reaches and len(survivors) == 1
                any_selective = any_selective or selective
                rows.append({
                    "generators": list(gens),
                    "exponent_window": w,
                    "library_size": len(elements),
                    "contains_the_identity": contains_identity,
                    "reaches_the_target": reaches,
                    "pinned_witnesses_surviving": [q(a) for a in survivors],
                    "uniquely_selects_the_target": selective,
                })
    # Tightness: a NON-multiplicative singleton library does select.
    singleton_members = {L3_FIXED_LOCUS_DENSITY / ORBIT_LENGTH}
    singleton_survivors = sorted(
        singleton_members & set(PINNED_WITNESSES),
        key=lambda f: (f.numerator, f.denominator),
    )
    singleton_selects = singleton_survivors == [TARGET_ALPHA]
    ok = identity_always and singleton_selects
    return {
        "theorem": (
            "C882-T7. Every multiplicatively closed anchor library contains "
            "1, and the anchor k = 1 pins alpha = 1/3. Therefore no "
            "multiplicative anchor rule -- any generating set, any exponent "
            "window -- can pin the target member uniquely. Uniqueness requires "
            "a non-closed, singleton-valued Record predicate."
        ),
        "libraries_enumerated": len(rows),
        "every_library_contains_the_identity": identity_always,
        "any_library_uniquely_selects_the_target": any_selective,
        "rows_reaching_the_target": [
            r for r in rows if r["reaches_the_target"]
        ][:12],
        "tightness_check": {
            "note": (
                "The theorem is not vacuous: a non-multiplicative singleton "
                "library {2/9} DOES select the target. So the wall is exactly "
                "multiplicative closure, not anchors as such."
            ),
            "singleton_library_survivors": [q(a) for a in singleton_survivors],
            "singleton_library_selects_the_target": singleton_selects,
        },
        "the_exact_wall": (
            "The readout half of the obligation reduces to producing ONE "
            "Record-facing predicate that is singleton valued on the anchor "
            "constant and returns 2/9. No symmetry, closure, ratio, "
            "intensivity or multiplicative-invariance argument can produce it, "
            "by C882-T1, T2, T3 and T7. This is why the pinned note asks for a "
            "'singleton readout clause' -- the demand is now derived."
        ),
        "finding": (
            f"Across {len(rows)} enumerated multiplicative anchor libraries, "
            f"every single one contains the identity and not one selects the "
            f"target uniquely; the singleton control confirms the wall is "
            f"multiplicative closure rather than anchoring itself."
        ),
        "pass": ok,
    }


# --------------------------------------------------------------------------
# certificate K: THE FALSIFICATION SURFACE -- the alpha-witness table
# --------------------------------------------------------------------------
def alpha_witness_table_certificate(lib: list[dict]) -> dict:
    """For every derived constraint, which of the five witnesses survives.

    This is the block's falsification surface. The certificate passes on the
    table being COMPLETE and INTERNALLY CONSISTENT -- it does not encode which
    alphas ought to survive.
    """
    all_alphas = PINNED_WITNESSES + EXTRA_ALPHAS
    rows = []
    complete = True
    consistent = True
    for entry in lib:
        rr = entry["rows"]
        kind, sol = solve_affine(rr)
        pinned_surv = [a for a in PINNED_WITNESSES if satisfies(rr, a)]
        extra_surv = [a for a in EXTRA_ALPHAS if satisfies(rr, a)]
        # Internal consistency: membership must agree with the solved set.
        for a in all_alphas:
            expect = (
                kind == "ALL_OF_Q" or (kind == "SINGLETON" and a == sol)
            )
            if satisfies(rr, a) != expect:
                consistent = False
        if len(pinned_surv) + len(extra_surv) == 0 and kind != "EMPTY":
            complete = False
        rows.append({
            "constraint_id": entry["id"],
            "constraint": entry["name"],
            "kind": entry["kind"],
            "genuinely_inhomogeneous": any(k != 0 for _, k in rr),
            "solution_set": (
                "ALL_OF_Q" if kind == "ALL_OF_Q"
                else ("EMPTY" if kind == "EMPTY" else f"{{{q(sol)}}}")),
            "witness_0": satisfies(rr, Fraction(0)),
            "witness_1_9": satisfies(rr, Fraction(1, 9)),
            "witness_1_3": satisfies(rr, Fraction(1, 3)),
            "witness_1": satisfies(rr, Fraction(1)),
            "witness_2_27_TARGET": satisfies(rr, TARGET_ALPHA),
            "pinned_survivors": [q(a) for a in pinned_surv],
            "extra_alphas_surviving": [q(a) for a in extra_surv],
            "kills_all_wrong_alphas_keeping_at_most_the_target": (
                set(pinned_surv) <= {TARGET_ALPHA}),
            "provenance": entry["provenance"],
        })
    discriminating = [
        r["constraint_id"] for r in rows
        if r["kills_all_wrong_alphas_keeping_at_most_the_target"]
        and r["witness_2_27_TARGET"]
    ]
    return {
        "purpose": (
            "The block's falsification surface. Any future candidate theorem "
            "must reproduce a row here that keeps 2/27 and kills 0, 1/9, 1/3 "
            "and 1. Rows are computed; the gate checks completeness and "
            "internal consistency only and encodes no preferred survivor."
        ),
        "alphas_tested": [q(a) for a in all_alphas],
        "rows": rows,
        "constraints_tabulated": len(rows),
        "constraints_that_uniquely_keep_the_target": discriminating,
        "table_complete": complete,
        "table_internally_consistent": consistent,
        "finding": (
            f"{len(rows)} constraints x {len(all_alphas)} alphas tabulated. "
            f"{len(discriminating)} constraint(s) uniquely keep the target, "
            f"and each of them is an anchor constraint whose constant is the "
            f"fixed-locus arithmetic -- i.e. the license restated, not derived."
        ),
        "pass": complete and consistent,
    }


# --------------------------------------------------------------------------
# certificate L: the terminal missing lemma, classified by strength
# --------------------------------------------------------------------------
def terminal_lemma_certificate() -> dict:
    """Classify the terminal missing lemma against the obligation.

    LEMMA-882 (the anchor-binding lemma). The Record-facing readout of one
    registered full C3 orbit equals the fixed-locus density L3(1,2) = 2/9.

    Direction 1 (LEMMA => obligation at scope). LEMMA fixes alpha = 2/9 / 3 =
    2/27, i.e. the readout IS the fixed-locus density class; multiplying by the
    orbit length gives 3 * 2/9 = 2/3 = S_sum, the pinned angle target, with no
    extra clock-rate or normalization factor.

    Direction 2 (obligation => LEMMA). If the readout identity holds, evaluate
    it on the single full orbit: the reading is exactly 2/9.

    Both directions are exact one-liners, so the missing lemma is EQUIVALENT to
    the obligation at this scope -- not weaker. Consequence: the readout half
    cannot be chipped at. It closes whole or not at all.
    """
    alpha_from_lemma = L3_FIXED_LOCUS_DENSITY / ORBIT_LENGTH
    d1 = (
        alpha_from_lemma == TARGET_ALPHA
        and ORBIT_LENGTH * L3_FIXED_LOCUS_DENSITY == S_SUM
    )
    d2 = readout(TARGET_ALPHA, (FULL_ORBIT,)) == L3_FIXED_LOCUS_DENSITY
    strength = "EQUIVALENT" if (d1 and d2) else "INCOMPARABLE"

    subsidiary = [
        {
            "lemma": "SL1 weight-pair supply: the charged-lepton record carries "
                     "the fixed-locus weight pair (1, 2) as Record content",
            "strength_vs_obligation": "WEAKER",
            "why": (
                "It supplies a datum with v_2 = 1, defeating C882-T6, but does "
                "not by itself bind that datum to the readout; the binding "
                "predicate is still needed."
            ),
            "would_close_the_block": False,
        },
        {
            "lemma": "SL2 singleton readout predicate: a Record-facing clause "
                     "that is singleton valued on the anchor constant",
            "strength_vs_obligation": "EQUIVALENT",
            "why": (
                "By C882-T7 this is exactly what selection requires, and by the "
                "two directions above it is inter-derivable with the readout "
                "identity at this scope."
            ),
            "would_close_the_block": True,
        },
        {
            "lemma": "SL3 universal readout-selection principle for all finite "
                     "orbit records at all multiplicities",
            "strength_vs_obligation": "STRONGER",
            "why": (
                "It implies LEMMA-882 by restriction to the C3 orbit and also "
                "settles orbits this block never touches."
            ),
            "would_close_the_block": True,
        },
        {
            "lemma": "SL4 approved narrow readout-selection primitive",
            "strength_vs_obligation": "INCOMPARABLE",
            "why": (
                "Governance, not derivation. It discharges the obligation by "
                "registration rather than proof, and the obligation says so."
            ),
            "would_close_the_block": False,
        },
    ]
    strengths_valid = all(
        row["strength_vs_obligation"] in STRENGTH_CLASSES
        for row in subsidiary
    )
    return {
        "terminal_lemma": (
            "LEMMA-882 (anchor binding). The Record-facing readout of one "
            "registered full C3 orbit equals the fixed-locus density "
            "L3(1,2) = 2/9."
        ),
        "direction_lemma_implies_obligation": d1,
        "direction_obligation_implies_lemma": d2,
        "alpha_forced_by_the_lemma": q(alpha_from_lemma),
        "angle_recovered": q(ORBIT_LENGTH * L3_FIXED_LOCUS_DENSITY),
        "angle_target_S_sum": q(S_SUM),
        "strength_vs_obligation": strength,
        "subsidiary_lemmas": subsidiary,
        "strength_classes_valid": strengths_valid,
        "consequence": (
            "Because the terminal lemma is EQUIVALENT rather than weaker, "
            "incremental chipping at the readout half is dead: any real move "
            "must be SL1 (which defeats one named obstruction but does not "
            "close) or SL2/SL3 (which close), or governance via SL4."
        ),
        "finding": (
            "Both derivation directions verify exactly, so the missing lemma "
            "is classified EQUIVALENT to the obligation at this scope; three "
            "subsidiary lemmas are classified WEAKER, STRONGER and "
            "INCOMPARABLE respectively."
        ),
        "pass": d1 and d2 and strengths_valid,
    }


# --------------------------------------------------------------------------
# certificate M: outcome and price
# --------------------------------------------------------------------------
def outcome_certificate(prior: dict) -> dict:
    residual_continuous_dimension = 1   # the anchor constant k
    residual_discrete_choice = len(anchor_library())
    pinned_871 = prior["cycle871_free_dimension_per_on_branch_pin"]
    return {
        "outcome_class": "SHARPER_OBSTRUCTION_PLUS_PRICED_PARTIAL",
        "route_closed": False,
        "what_was_derived": [
            "C882-T1 homogeneous dichotomy: homogeneous routes give {0} or Q, "
            "never a nonzero singleton (prior art's prose, now a theorem).",
            "C882-T2 ratio blindness: the entire degree-0 comparative sector is "
            "alpha-independent, so no comparative Record theorem can pin.",
            "C882-T3 intensivity collapse: additive + intensive implies zero, "
            "so the word 'density' supplies no selecting constraint.",
            "C882-T4/T5 anchor bijection: the five pinned witnesses ARE the "
            "five nameable anchors, and the four axiom-available anchors pin "
            "exactly the four wrong members.",
            "C882-T6 2-adic obstruction: the orbit-cardinality group has "
            "v_2 = 0 throughout while the target anchor has v_2 = 1, so orbit "
            "multiplicity cannot reach it at any exponent.",
            "C882-T7 identity obstruction (THE EXACT WALL): every "
            "multiplicatively closed anchor library contains 1 and therefore "
            "always admits alpha = 1/3 alongside the target; selection needs a "
            "singleton-valued predicate, which is why the pinned note asks for "
            "one.",
            "A formal definition of 'genuinely inhomogeneous' with three "
            "proved-equivalent characterisations.",
        ],
        "what_remains": (
            "LEMMA-882, the anchor-binding clause. Classified EQUIVALENT to "
            "the obligation at this scope, so nothing short of it closes the "
            "readout half."
        ),
        "residual_free_dimension_readout_half": residual_continuous_dimension,
        "residual_free_dimension_note": (
            "One continuous parameter: the anchor constant k, with alpha = k/3. "
            "The named/discrete residual is the choice among "
            f"{residual_discrete_choice} anchors, of which exactly one is the "
            "target."
        ),
        "dimension_before_this_cycle": 1,
        "dimension_after_this_cycle": residual_continuous_dimension,
        "dimension_honestly_unchanged": True,
        "what_changed_instead": (
            "The dimension count did not fall -- and this block does not "
            "pretend it did. What changed is the CHARACTER of the residual: "
            "from 'a free coefficient on a line' to 'one named anchor among "
            "five, four of which are axiom-available and all four wrong', plus "
            "four route classes closed by theorem and one exact wall with a "
            "named escape condition."
        ),
        "cycle871_bridge_half_free_dimension_per_on_branch_pin": pinned_871,
        "joint_price_if_the_two_halves_are_independent": (
            None if pinned_871 is None
            else pinned_871 + residual_continuous_dimension
        ),
        "joint_price_caveat": (
            "The Cycle-871 runner is absent from this worktree, so its number "
            "is a PIN read out of the Cycle-880 BRANCH_PINS string, not a "
            "recomputation. Independence of the two halves is asserted by "
            "neither this block nor the pin, so the sum is reported as "
            "conditional arithmetic and nothing depends on it."
        ),
        "named_successor_target": (
            "SL1: derive that the charged-lepton record carries the fixed-locus "
            "weight pair (1, 2) as Record content. C882-T6 makes this the "
            "unique arithmetic gap, and it is strictly weaker than the "
            "obligation, so it is attackable."
        ),
        "corrections_forced_by_the_independent_checker": [
            "C882-T1 was restated for single-degree (scaling-covariant) "
            "homogeneity after the checker exhibited mixed-degree "
            "zero-constant-term counterexamples; no computed result moved, "
            "since this runner's whole constraint library is linear.",
            "Route R13 (bilinear Record relations) was added to the route "
            "table after the checker constructed it. It reaches the target "
            "without an explicitly written constant and therefore shows that "
            "C882-T6's restriction to orbit-cardinality data is load bearing; "
            "it selects nothing, so the block's outcome is unchanged.",
            "The checker also MEASURED where C882-T6 dissolves: admitting "
            "record copy multiplicity 2 as a generator reaches the target "
            "immediately. That is the same escape condition SL1 names, "
            "arrived at independently.",
        ],
        "finding": (
            "Negative-shaped and priced. Four route classes closed by theorem, "
            "one exact wall (multiplicative closure always keeps the identity), "
            "the witness list explained as the anchor library, and the terminal "
            "lemma classified EQUIVALENT. The free dimension is unchanged at 1."
        ),
        "pass": True,
    }


# --------------------------------------------------------------------------
# certificate N: the no-go discipline gate
# --------------------------------------------------------------------------
def no_go_gate_certificate() -> dict:
    routes = [
        {"route": "R1 Record additivity + C3 covariance symmetry-only pin",
         "marker": "RULED-OUT-BY-PRIOR",
         "pin": "stretch no-go frame 1 (blob e2ca96d2), reproduced here as "
                "C882 certificate C (nullspace dimension 1)"},
        {"route": "R2 fixed-locus arithmetic as class selector",
         "marker": "RULED-OUT-BY-PRIOR",
         "pin": "stretch no-go frame 2: supplies the value inside the class, "
                "not class membership"},
        {"route": "R3 supplied finite context / W2 as readout license",
         "marker": "RULED-OUT-BY-PRIOR",
         "pin": "stretch no-go frame 3: context algebra, no carrier"},
        {"route": "R4 holonomy normal form Phi = c S_sum",
         "marker": "RULED-OUT-BY-PRIOR",
         "pin": "stretch no-go frame 4 + frontier no-go bin 3 (blob 92553eb7): "
                "relocates the target, restates the license"},
        {"route": "R5 approved-primitive registry search for a hidden h-class",
         "marker": "RULED-OUT-BY-PRIOR",
         "pin": "stretch no-go frame 5: registry contains no h-class, R-eta, "
                "observable bridge, event law or selector"},
        {"route": "R6 periodic/torsion phases and canonical 2*pi packaging",
         "marker": "RULED-OUT-BY-PRIOR",
         "pin": "frontier no-go bin 1 plus the retained radian-bridge no-go"},
        {"route": "R7 homogeneous self-consistency / fixed-point readout maps",
         "marker": "ATTEMPTED",
         "pin": "C882-T1: upgraded from the frontier note's prose to an exact "
                "dichotomy over the whole constraint library"},
        {"route": "R8 ratio / comparative Record observables",
         "marker": "ATTEMPTED",
         "pin": "C882-T2: NEW closure. The degree-0 sector is alpha-blind"},
        {"route": "R9 intensivity / density-normalisation route",
         "marker": "ATTEMPTED",
         "pin": "C882-T3: NEW closure. Additive + intensive forces zero"},
        {"route": "R10 multiplicative anchor libraries from cardinality data",
         "marker": "ATTEMPTED",
         "pin": "C882-T6 and C882-T7: NEW closure and the exact wall"},
        {"route": "R11 Record count-once / registration idempotence",
         "marker": "ATTEMPTED",
         "pin": "constraint K1_COUNT_ONCE: affine normal form is empty, so it "
                "does not discriminate any member"},
        {"route": "R12 Record-facing affine anchor binding (LEMMA-882)",
         "marker": "ATTEMPTED",
         "pin": "the surviving live route; classified EQUIVALENT to the "
                "obligation in certificate L"},
        {"route": "R13 bilinear Record relations I(R1) I(R2) = I(R3), where "
                  "the inhomogeneous constant is carried by record sizes "
                  "rather than written down",
         "marker": "ATTEMPTED",
         "pin": "constructed by the Cycle-882 independent checker, certificate "
                "CF, NOT by this runner. It reaches the target at record sizes "
                "(1, 27, 2) -- so it does evade C882-T6, whose scope is the "
                "orbit cardinality alone -- but its solution set is {0, "
                "s3/(s1 s2)} and every positive rational is attainable, so it "
                "selects nothing and retains the zero member. Recorded here "
                "because the route table must carry it."},
    ]
    markers_valid = all(r["marker"] in ROUTE_MARKERS for r in routes)
    attempted = [r for r in routes if r["marker"] == "ATTEMPTED"]
    ruled = [r for r in routes if r["marker"] == "RULED-OUT-BY-PRIOR"]
    enough = len(routes) >= 5
    return {
        "N1_route_enumeration": routes,
        "routes_named": len(routes),
        "routes_attempted_here": len(attempted),
        "routes_ruled_out_by_prior_art": len(ruled),
        "markers_valid": markers_valid,
        "at_least_five_routes": enough,
        "N2_wall_independence": (
            "No new wall name is introduced. The wall remains the R-eta "
            "density-read-as-angle license. This block sharpens its SHAPE: it "
            "is a singleton-valued anchor-binding predicate, and every closed "
            "algebraic route to it is now shown impossible."
        ),
        "N3_hidden_wall_scan": (
            "No observed lepton mass, comparator, fitted selector, Born or "
            "interface rule, event law, occurrence rate, probability rule, "
            "theta premise, source/action bridge, physical-carrier theorem, "
            "h-unit assumption, new axiom, new primitive or owner decision "
            "enters any proof above. The fixed-locus rational 2/9 and the sum "
            "2/3 are used ONLY as pinned retained arithmetic and never as a "
            "licensed readout."
        ),
        "N4_residual_matching": (
            "The residual matches the zero-weight R-eta open obligation "
            "exactly: the arithmetic 2/9 and 2/3 is retained; the open item is "
            "the identification that binds the fixed-locus rational to the "
            "physical readout."
        ),
        "N5_proven_surface": (
            "Proven here: (i) an exact dichotomy for homogeneous constraints; "
            "(ii) alpha-blindness of the degree-0 comparative sector; (iii) "
            "collapse under intensivity; (iv) the anchor bijection and the "
            "axiom-available anchor set; (v) a 2-adic exclusion of the target "
            "anchor from orbit-cardinality data; (vi) the identity obstruction "
            "for all multiplicatively closed anchor libraries. NOT proven: any "
            "terminal mathematical no-go against future readout-license "
            "theorems. SL2 and SL3 remain open and attackable."
        ),
        "N6_partial_closure": (
            "Four route classes closed by theorem; the live target is narrowed "
            "from 'select a member of a line' to 'produce one singleton-valued "
            "Record predicate returning 2/9', with SL1 named as a strictly "
            "weaker, attackable successor."
        ),
        "N7_steelman": (
            "A reviewer can say: you re-parameterised a free coefficient as a "
            "free constant, so the free dimension is still 1 and nothing was "
            "derived. That is substantially correct and certificate M states "
            "it in those words. The rebuttal is bounded: (a) four route classes "
            "that previously looked open are now closed by exact theorem rather "
            "than by prose, so the campaign cannot spend cycles on them; (b) "
            "the five witnesses are no longer arbitrary examples but the "
            "complete named anchor library, of which the four axiom-available "
            "members are exactly the four wrong ones -- a strictly sharper "
            "statement than 'the coefficient is free'; (c) the terminal lemma "
            "is proved EQUIVALENT, which kills incrementalism as a strategy; "
            "and (d) C882-T6 isolates the gap to a single arithmetic fact "
            "(v_2 = 1), giving the first successor target on this half that is "
            "strictly weaker than the obligation. This is route pruning plus a "
            "sharper wall. It is not a closure and is not sold as one."
        ),
        "N8_exact_scope": (
            "Scope: the finite single full C3 orbit readout family over Q at "
            "the obligation's own scope, with Record additivity, C3 covariance "
            "and empty-record normalization as the only structural inputs, plus "
            "the pinned retained arithmetic L3(1,2) = 2/9 and S_sum = 2/3 used "
            "as numbers only. Out of scope and NOT claimed: other orbits, "
            "non-abelian records, infinite records, the h-unit half, the "
            "carrier/source-action half (Cycle 871), any delta, r, Koide value, "
            "charged-lepton mass or mixing angle, and any statement about all "
            "future mathematical constructions."
        ),
        "finding": (
            f"{len(routes)} routes named ({len(ruled)} ruled out by pinned "
            f"prior art, {len(attempted)} attacked here), with the steelman and "
            f"the exact scope stated inline."
        ),
        "pass": markers_valid and enough,
    }


# --------------------------------------------------------------------------
# assembly
# --------------------------------------------------------------------------
def build_science() -> dict:
    lib = constraint_library()
    prior = prior_art_certificate()
    return {
        "B_PRIOR_ART_AS_DATA": prior,
        "C_READOUT_SPACE": readout_space_certificate(),
        "D_GENUINE_INHOMOGENEITY": genuine_inhomogeneity_certificate(lib),
        "E_HOMOGENEOUS_DICHOTOMY": homogeneous_dichotomy_certificate(lib),
        "F_RATIO_BLINDNESS": ratio_blindness_certificate(),
        "G_INTENSIVITY": intensivity_certificate(),
        "H_ANCHOR_BIJECTION": anchor_bijection_certificate(),
        "I_CARDINALITY_GROUP": cardinality_group_certificate(),
        "J_IDENTITY_OBSTRUCTION": identity_obstruction_certificate(),
        "K_ALPHA_WITNESS_TABLE": alpha_witness_table_certificate(lib),
        "L_TERMINAL_LEMMA": terminal_lemma_certificate(),
        "M_OUTCOME_AND_PRICE": outcome_certificate(prior),
        "N_NO_GO_GATE": no_go_gate_certificate(),
    }


def render(certificates: dict) -> str:
    out = [
        "=" * 78,
        "CYCLE 882 -- THE READOUT-IDENTITY OBLIGATION (R-eta, readout half)",
        "=" * 78,
        "",
    ]
    for label in LABELS:
        if label not in certificates:
            continue
        cert = certificates[label]
        out.append(f"[{ 'PASS' if cert['pass'] else 'FAIL' }] {label}")
        finding = cert.get("finding", "")
        if finding:
            for line in _wrap(finding, 74):
                out.append(f"       {line}")
        out.append("")
    out.append("-" * 78)
    out.append("ALPHA-WITNESS TABLE (the falsification surface)")
    out.append("-" * 78)
    header = f"{'constraint':44s} {'0':>5s} {'1/9':>5s} {'1/3':>5s} {'1':>5s} {'2/27':>6s}"
    out.append(header)
    for row in certificates["K_ALPHA_WITNESS_TABLE"]["rows"]:
        out.append(
            f"{row['constraint_id'][:44]:44s} "
            f"{'y' if row['witness_0'] else '.':>5s} "
            f"{'y' if row['witness_1_9'] else '.':>5s} "
            f"{'y' if row['witness_1_3'] else '.':>5s} "
            f"{'y' if row['witness_1'] else '.':>5s} "
            f"{'y' if row['witness_2_27_TARGET'] else '.':>6s}"
        )
    out.append("")
    out.append("-" * 78)
    out.append("ANCHOR LIBRARY (k -> alpha = k/3)")
    out.append("-" * 78)
    for row in certificates["H_ANCHOR_BIJECTION"]["rows"]:
        out.append(
            f"  k = {row['anchor_constant_k']:>5s}  ->  alpha = "
            f"{row['pins_alpha']:>6s}  axiom_available="
            f"{str(row['axiom_available_without_the_fixed_locus_arithmetic']):5s}"
            f"  {'<== TARGET' if row['is_the_target'] else ''}"
        )
    out.append("")
    out.append("-" * 78)
    out.append("OUTCOME")
    out.append("-" * 78)
    outcome = certificates["M_OUTCOME_AND_PRICE"]
    out.append(f"  class: {outcome['outcome_class']}")
    out.append(f"  residual free dimension (readout half): "
               f"{outcome['residual_free_dimension_readout_half']}")
    for line in _wrap(outcome["what_remains"], 74):
        out.append(f"  remains: {line}" if line == _wrap(
            outcome["what_remains"], 74)[0] else f"           {line}")
    out.append("")
    out.append("=" * 78)
    verdict = all(cert["pass"] for cert in certificates.values())
    out.append(f"CYCLE 882 CERTIFICATES: {'ALL PASS' if verdict else 'FAIL'}")
    out.append("=" * 78)
    return "\n".join(out) + "\n"


def _wrap(text: str, width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    cur = ""
    for word in words:
        if not cur:
            cur = word
        elif len(cur) + 1 + len(word) <= width:
            cur += " " + word
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def run() -> int:
    started = monotonic()

    pins = pins_certificate()
    science_a = build_science()
    science_b = build_science()
    deterministic = digest(science_a) == digest(science_b)

    certificates = {"A_PINS": pins, **science_a}

    receipt = {
        "cycle": 882,
        "title": "the readout-identity obligation: the inhomogeneous half",
        "alpha_coordinate": ALPHA_COORDINATE,
        "pinned_witnesses": [q(a) for a in PINNED_WITNESSES],
        "target_alpha": q(TARGET_ALPHA),
        "outcome_class": science_a["M_OUTCOME_AND_PRICE"]["outcome_class"],
        "residual_free_dimension": science_a["M_OUTCOME_AND_PRICE"][
            "residual_free_dimension_readout_half"],
        "terminal_lemma_strength": science_a["L_TERMINAL_LEMMA"][
            "strength_vs_obligation"],
        "theorems": [
            "C882-T1 homogeneous dichotomy",
            "C882-T2 ratio blindness",
            "C882-T3 intensivity collapse",
            "C882-T4 anchor bijection",
            "C882-T5 axiom-available anchors miss the target",
            "C882-T6 2-adic exclusion",
            "C882-T7 identity obstruction (the exact wall)",
        ],
        "alpha_witness_table": science_a["K_ALPHA_WITNESS_TABLE"]["rows"],
        "anchor_library": science_a["H_ANCHOR_BIJECTION"]["rows"],
        "routes": science_a["N_NO_GO_GATE"]["N1_route_enumeration"],
        "scope": science_a["N_NO_GO_GATE"]["N8_exact_scope"],
        "steelman": science_a["N_NO_GO_GATE"]["N7_steelman"],
        "source_pins": [
            {"path": row["path"], "sha256": row["sha256"],
             "git_blob": row["git_blob"]}
            for row in pins["rows"]
        ],
        "branch_pins": dict(BRANCH_PINS),
    }
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(
        json.dumps(receipt, indent=2, sort_keys=True, default=str) + "\n",
        encoding="utf-8",
    )
    cache_digest = sha256(CACHE.read_bytes()).hexdigest()

    text = render(certificates)
    stdout_bytes = len(text.encode("utf-8"))
    elapsed = monotonic() - started

    controls = {
        "audit_input_paths": list(AUDIT_INPUT_PATHS),
        "blocklisted_modules": list(BLOCKLISTED_MODULES),
        "blocked_modules_loaded": [
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ],
        "firewall_hits": list(FIREWALL.hits),
        "determinism": {
            "scope": "every science certificate rebuilt from scratch and "
                     "compared digest for digest",
            "exact": deterministic,
            "science_digest": digest(science_a),
        },
        "cache_path": str(CACHE.relative_to(ROOT)),
        "cache_sha256": cache_digest,
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "runtime_under_limit": elapsed < AUDIT_TIMEOUT_SEC,
        "stdout_bytes": stdout_bytes,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "stdout_under_limit": stdout_bytes < STDOUT_LIMIT_BYTES,
        "floating_point_in_certified_quantities": False,
        "gate_neutrality": (
            "No certificate gate tests for a preferred alpha, a preferred "
            "survivor set, or a positive outcome. The alpha-witness table "
            "gates on completeness and internal consistency; the theorem "
            "certificates gate on the computed claim matching the computed "
            "solution sets; the outcome certificate is descriptive and gates "
            "on nothing."
        ),
        "finding": (
            "All cited artifacts stayed text/AST-only behind the import "
            "firewall, the whole science payload rebuilt digest for digest, "
            "and the runtime and stdout caps were respected."
        ),
    }
    controls["pass"] = (
        deterministic
        and controls["runtime_under_limit"]
        and controls["stdout_under_limit"]
        and not controls["blocked_modules_loaded"]
        and not controls["firewall_hits"]
    )
    certificates["O_CONTROLS"] = controls

    sys.stdout.write(text)
    # Wall-clock seconds are deliberately NOT printed: the transcript is a
    # committed cache and must be byte stable across cold runs.
    sys.stdout.write(
        f"\ncontrols: deterministic={deterministic} "
        f"runtime_under_limit={controls['runtime_under_limit']} "
        f"stdout={stdout_bytes}B cache={controls['cache_sha256'][:16]}\n"
    )
    return 0 if all(cert["pass"] for cert in certificates.values()) else 1


if __name__ == "__main__":
    raise SystemExit(run())
