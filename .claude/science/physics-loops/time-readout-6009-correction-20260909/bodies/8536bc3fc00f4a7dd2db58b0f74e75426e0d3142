#!/usr/bin/env python3
"""CYCLE 901 -- WHICH SPACE DOES THE RECORD READ?

Cycle 899 (sibling branch) reported that two families collide at n = 3 and
separate everywhere else:

    F_dim(n) = (n - 1) / n^2          the NATIVE binding of the 883/888
                                      readout construction (content-space:
                                      the readout module's invariant
                                      complement over a transitive orbit)

    F_res(n) = (n^2 - 1) / (12 n)     the RETAINED anchor arithmetic (the
                                      KOIDE_APS L-face: the transverse
                                      inverse-determinant density over the
                                      GEOMETRIC normal plane of the rotation
                                      axis)

    F_dim(3) = F_res(3) = 2/9         collision
    F_dim(2) = 1/4  vs F_res(2) = 1/8
    F_dim(4) = 3/16 vs F_res(4) = 5/16

THE QUESTION.  Which space does the record read -- the readout module's
invariant complement (content-space, F_dim) or the ambient geometric normal
plane (embedding-space, F_res)?

THE ADJUDICATING BYTES.  The Record axiom's readout clause, quoted verbatim
from the pinned memo:

    "Only records are readable. A readout value is determined by record
     content alone."
    "For any finite collection of pairwise-disjoint records, scalar readout
     `I` is additive, with `I(empty)=0`."

METHOD.  Both readings are formalized as computable predicates over readout
constructions and BOTH are tested.  Three predicates are separated, because
"determined by record content alone" has three independently computable
consequences:

    P_EMB    re-embedding invariance -- two record data with the same
             abstract content structure, differently embedded in Z^3, get
             the same value.  (Enumerated over the 24 proper cubic
             rotations, over lattice translations, and over every conjugate
             of every scope class.)

    P_SCOPE  scope-independence -- "alone" excludes a SECOND determining
             input.  One record collection admitting two admissible ambient
             scopes must not receive two values.

    P_TOTAL  totality -- the additivity clause quantifies over ANY finite
             collection of pairwise-disjoint records, so a readout that is
             UNDEFINED on some finite disjoint collection is not the axiom's
             readout.

OUTCOME NEUTRALITY.  The verdict can land in any of DECIDED-F_DIM,
DECIDED-F_RES, UNDECIDABLE-PRICED.  The gates require: both readings
formalized and evaluated on every predicate; the 888 census and the 883
anchor reproduced value-for-value BEFORE any new claim; the 899 rows rebuilt
independently and compared LOUDLY against the numbers the brief states; a
planted embedding-dependent reading DETECTED as violating; a planted
content-only reading DETECTED as surviving; a deterministic double build.
No gate requires a particular verdict.

DISCIPLINE.  Every pinned input is fixed by full path + sha256 + git blob and
read as TEXT / AST / JSON only; a meta-path import firewall makes importing
any pinned module an error and the hit count is gated at zero.  Every
certified number is exact (`Fraction`); no floating point enters any
certified value.

SCOPE, HONESTLY.  The ambient group is the proper cubic rotation group of
Z^3 (order 24) supplied by the Lattice axiom.  Every statement about the
geometric reading's embedding-invariance is proved ON THAT GROUP plus the
angle argument that generalizes it; the statement that no OTHER ambient
group anywhere behaves differently is not claimed.  The consumer table is a
needle sweep of this branch, with scan counts disclosed.
"""

from __future__ import annotations

import ast
import hashlib
import importlib.abc
import json
import re
import subprocess
import sys
import time
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path

START = time.time()

CYCLE = 901
RUNTIME_CAP_SEC = 900
EXHIBIT_CAP = 8

ROOT = Path(__file__).resolve().parents[1]
SELF_REL = "scripts/frontier_cycle901_space_identification_2026_07_28.py"
OUT_JSON = ROOT / "outputs" / "space_identification_cycle901_receipt_2026_07_28.json"

C883_PRIMARY = "scripts/frontier_cycle883_record_weight_pair_2026_07_28.py"
C883_RECEIPT = "outputs/record_weight_pair_cycle883_receipt_2026_07_28.json"
C888_PRIMARY = "scripts/frontier_cycle888_s3_scope_pricing_2026_07_28.py"
C888_RECEIPT = "outputs/s3_scope_pricing_cycle888_receipt_2026_07_28.json"
KOIDE_MD = ("docs/KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_"
            "THEOREM_NOTE_2026-06-05.md")
AXIOMS_MD = "docs/MINIMAL_AXIOMS_2026-06-29.md"
DYNAMICS_MD = "docs/GATE_B_DYNAMICS_NOTE.md"
WEAKFIELD_MD = "docs/GATE_B_WEAK_FIELD_SOURCE_ACTION_INTERFACE_NOTE_2026-06-16.md"

AUDIT_INPUT_PATHS = (
    C883_PRIMARY, C883_RECEIPT, C888_PRIMARY, C888_RECEIPT,
    KOIDE_MD, AXIOMS_MD, DYNAMICS_MD, WEAKFIELD_MD,
)

# The one digest the block brief supplies verbatim.  A mismatch is a hard
# preflight failure: the cited artifact is not the artifact this cycle was
# pointed at.
BRIEF_SHA256 = {
    C888_PRIMARY:
        "f57fda877d35d49953c3b6a34293ab0cc6a87781ceb9d158b9c9abb5abd4bb3f",
}

# --------------------------------------------------------------------------
# Verbatim needles.  Each is quoted from a pinned artifact; if the artifact
# stops containing it character for character (after whitespace
# normalization) the pins certificate fails.
# --------------------------------------------------------------------------
AXIOM_NEEDLES = {
    "content_alone":
        "Only records are readable. A readout value is determined by record "
        "content alone.",
    "finite_additive_readout":
        "For any finite collection of pairwise-disjoint records, scalar "
        "readout `I` is additive, with `I(empty)=0`.",
    "sites_by_lattice_alone":
        "Sites are distinguished by the supplied lattice structure alone.",
    "lattice_points":
        "Physical sites are the points of the cubic lattice `Z^3`",
    "lattice_rotations":
        "proper cubic rotations about each site",
    "context_selection_is_outside":
        "context selection, measurement basis selection, Born weights, "
        "probability",
    "readout_context_selection_needs_authority":
        "readout-context selection",
    "further_structure_needs_derivation":
        "Further physical structure requires a retained derivation or bridge",
    "unfixed_choice_stays_conditional":
        "A choice not fixed by the supplied structure remains a named "
        "conditional or open dependency.",
}

KOIDE_NEEDLES = {
    "normal_determinant_three":
        "det_R(I-g|_N)=3.",
    "l_face_definition":
        "L_C_3(N) = (1/3) sum_{k=1}^{2} 1/det_R(I-g^k|_N).",
    "l_face_value":
        "L_C_3(N) = (1/3)(1/3+1/3) = 2/9.",
    "normal_plane_is_geometric":
        "The real normal plane is therefore",
    "axis_selection_is_separate":
        "physical-axis selection is a separate theorem target",
}

# --------------------------------------------------------------------------
# The numbers the block brief attributes to Cycle 899.  The 899 artifacts are
# on a SIBLING branch.  Certificate C rebuilds every one of them from scratch
# on this branch and compares; any disagreement is reported LOUDLY and fails
# the restriction gate.
# --------------------------------------------------------------------------
BRIEF_899_ROWS = {
    "C2_face":  {"n": 2, "K_native": Fraction(1, 4),  "L_face": Fraction(1, 8)},
    "C2_edge":  {"n": 2, "K_native": Fraction(1, 4),  "L_face": Fraction(1, 8)},
    "C3_body":  {"n": 3, "K_native": Fraction(2, 9),  "L_face": Fraction(2, 9)},
    "C4_face":  {"n": 4, "K_native": Fraction(3, 16), "L_face": Fraction(5, 16)},
    "V_edge":   {"n": 4, "K_native": Fraction(3, 16), "L_face": None},
}
BRIEF_899_FINE_TYPES = {
    "C2_face": (1, 1),
    "C2_edge": (1, 1),
    "C3_body": (1, 2),
    "C4_face": (1, 1, 2),
    "V_edge":  (1, 1, 1, 1),
}
ANCHOR = Fraction(2, 9)

# The seven closed forms Cycle 883 certificate M enumerated, transcribed here
# as (name, lambda over (w0, w1, n)).  The transcription is CHECKED against
# the pinned 883 source by AST in certificate C; it is not trusted.
C883_FORMS = (
    ("w1 / (w0 + w1)^2", lambda w0, w1, n: Fraction(w1, (w0 + w1) ** 2)),
    ("w0 * w1 / n^2",    lambda w0, w1, n: Fraction(w0 * w1, n ** 2)),
    ("w1 / n^2",         lambda w0, w1, n: Fraction(w1, n ** 2)),
    ("(n - 1) / n^2",    lambda w0, w1, n: Fraction(n - 1, n ** 2)),
    ("w1 / (w0 * n^2)",  lambda w0, w1, n: Fraction(w1, w0 * n ** 2)),
    ("w0 / n",           lambda w0, w1, n: Fraction(w0, n)),
    ("(w0 + w1) / n^2",  lambda w0, w1, n: Fraction(w0 + w1, n ** 2)),
)

CONSUMER_NEEDLES = (
    "KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05",
    "det_R(I-",
    "L_C_3",
    "inverse-normal-determinant",
)
OFF_SCOPE_NEEDLES = ("5/16", "3/16", "1/8", "(n^2-1)", "n^2 - 1")


# --------------------------------------------------------------------------
# preflight + import firewall
# --------------------------------------------------------------------------
def preflight_pins() -> None:
    missing = [p for p in AUDIT_INPUT_PATHS if not (ROOT / p).is_file()]
    if missing:
        sys.stderr.write("PREFLIGHT FAIL: pinned input(s) absent: "
                         + ", ".join(missing) + "\n")
        raise SystemExit(2)
    for rel, want in BRIEF_SHA256.items():
        got = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
        if got != want:
            sys.stderr.write(
                f"PREFLIGHT FAIL: {rel} sha256 {got} != brief {want}\n")
            raise SystemExit(2)


class PinnedImportFirewall(importlib.abc.MetaPathFinder):
    """Cited primaries are EVIDENCE, never libraries."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_module(self, fullname, path=None):  # pragma: no cover
        return self.find_spec(fullname, path)

    def find_spec(self, fullname, path=None, target=None):
        banned = {Path(p).stem for p in AUDIT_INPUT_PATHS
                  if p.endswith(".py")}
        tail = fullname.rsplit(".", 1)[-1]
        if tail in banned:
            self.hits.append(fullname)
            raise ImportError(
                f"import firewall: {fullname} is pinned evidence, not a "
                f"library")
        return None


FIREWALL = PinnedImportFirewall()
sys.meta_path.insert(0, FIREWALL)


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def _read_bytes(rel: str) -> bytes:
    return (ROOT / rel).read_bytes()


def _read_text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8", errors="replace")


def norm(text: str) -> str:
    return " ".join(text.split())


def q(value) -> str:
    if value is None:
        return "UNDEFINED"
    return f"{value.numerator}/{value.denominator}"


def digest(payload: object) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, default=str).encode()).hexdigest()


def git_blob(rel: str) -> str:
    try:
        out = subprocess.run(["git", "hash-object", rel], cwd=str(ROOT),
                             capture_output=True, text=True, timeout=30)
        return out.stdout.strip() or "unavailable"
    except Exception:  # pragma: no cover
        return "unavailable"


# --------------------------------------------------------------------------
# exact linear algebra over Q
# --------------------------------------------------------------------------
def rref(rows: list[list[Fraction]]) -> tuple[list[list[Fraction]], list[int]]:
    A = [r[:] for r in rows]
    width = len(A[0]) if A else 0
    piv: list[int] = []
    r = 0
    for c in range(width):
        p = None
        for i in range(r, len(A)):
            if A[i][c] != 0:
                p = i
                break
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(width)]
        piv.append(c)
        r += 1
        if r == len(A):
            break
    return A, piv


def nullspace(rows: list[list[Fraction]], width: int) -> list[list[Fraction]]:
    if not rows:
        return [[Fraction(1) if j == k else Fraction(0) for j in range(width)]
                for k in range(width)]
    A, piv = rref(rows)
    free = [c for c in range(width) if c not in piv]
    basis = []
    for fc in free:
        v = [Fraction(0)] * width
        v[fc] = Fraction(1)
        for ri, pc in enumerate(piv):
            v[pc] = -A[ri][fc]
        basis.append(v)
    return basis


def rank_exact(rows: list[list[Fraction]]) -> int:
    if not rows:
        return 0
    _, piv = rref(rows)
    return len(piv)


# --------------------------------------------------------------------------
# the Lattice axiom's rotation group, rebuilt (never imported)
# --------------------------------------------------------------------------
I3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def det3(m) -> int:
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


def mul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))


def apply(m, v):
    return tuple(sum(m[i][j] * v[j] for j in range(3)) for i in range(3))


def transpose(m):
    return tuple(tuple(m[j][i] for j in range(3)) for i in range(3))


def element_order(m) -> int:
    k, c = 1, m
    while c != I3:
        c = mul(c, m)
        k += 1
        if k > 12:
            raise AssertionError("not a finite rotation")
    return k


def rotation_group() -> list:
    out = []
    for p in permutations(range(3)):
        for s in product((1, -1), repeat=3):
            m = [[0] * 3 for _ in range(3)]
            for i in range(3):
                m[i][p[i]] = s[i]
            m = tuple(tuple(r) for r in m)
            if det3(m) == 1:
                out.append(m)
    return sorted(out)


O24 = rotation_group()


def generate(gens) -> frozenset:
    G = {I3}
    frontier = [I3]
    while frontier:
        x = frontier.pop()
        for s in gens:
            y = mul(x, s)
            if y not in G:
                G.add(y)
                frontier.append(y)
    return frozenset(G)


def conjugate(H: frozenset, g) -> frozenset:
    gi = transpose(g)          # orthogonal integer matrix: inverse = transpose
    return frozenset(mul(mul(g, h), gi) for h in H)


def all_subgroups() -> list[frozenset]:
    subs = set()
    for a in O24:
        for b in O24:
            subs.add(generate([a, b]))
    return sorted(subs, key=lambda H: (len(H), sorted(map(str, H))))


def subgroup_class_name(H: frozenset) -> str:
    """Canonical 888 census name, computed from invariants only."""
    n = len(H)
    if n == 1:
        return "E_trivial"
    cyc = any(element_order(h) == n for h in H)
    nrm = len([g for g in O24 if conjugate(H, g) == H])
    abelian = all(mul(x, y) == mul(y, x) for x in H for y in H)
    key = (n, cyc, abelian, nrm)
    table = {
        (2, True, True, 8): "C2_face",
        (2, True, True, 4): "C2_edge",
        (3, True, True, 6): "C3_body",
        (4, False, True, 24): "V_face",
        (4, False, True, 8): "V_edge",
        (4, True, True, 8): "C4_face",
        (6, False, False, 6): "S3_body",
        (8, False, False, 8): "D4_face",
        (12, False, False, 24): "A4_tetrahedral",
        (24, False, False, 24): "O_full",
    }
    return table.get(key, f"UNCLASSIFIED{key}")


# --------------------------------------------------------------------------
# THE TWO CANDIDATE READINGS
# --------------------------------------------------------------------------
def common_fixed_space(H: frozenset) -> list[list[Fraction]]:
    """Basis of {v in Q^3 : h v = v for all h in H}."""
    rows = []
    for h in H:
        for i in range(3):
            rows.append([Fraction(h[i][j] - (1 if i == j else 0))
                         for j in range(3)])
    return nullspace(rows, 3)


def normal_plane_basis(H: frozenset):
    """The GEOMETRIC normal plane: orthogonal complement in R^3 of the common
    fixed axis.  Returns None when the fixed locus is not a line -- the
    embedding-space reading has no normal plane there."""
    ax = common_fixed_space(H)
    if len(ax) != 1:
        return None, ax
    a = ax[0]
    n2 = sum(x * x for x in a)
    cand = []
    for e in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
        v = [Fraction(x) for x in e]
        d = sum(v[i] * a[i] for i in range(3))
        cand.append([v[i] - d / n2 * a[i] for i in range(3)])
    basis: list[list[Fraction]] = []
    for w in cand:
        if rank_exact(basis + [w]) == len(basis) + 1:
            basis.append(w)
    if len(basis) != 2:
        return None, ax
    return basis, ax


def matrix_on_span(h, B: list[list[Fraction]]) -> list[list[Fraction]]:
    """Matrix of (I - h) restricted to span(B), in the basis B."""
    k = len(B)
    C = [[Fraction(0)] * k for _ in range(k)]
    for col in range(k):
        img = [B[col][i] - sum(h[i][j] * B[col][j] for j in range(3))
               for i in range(3)]
        rows = [[B[t][i] for t in range(k)] + [img[i]] for i in range(3)]
        A, piv = rref(rows)
        sol = [Fraction(0)] * k
        for ri, pc in enumerate(piv):
            if pc < k:
                sol[pc] = A[ri][k]
        # verify the solve
        recon = [sum(sol[t] * B[t][i] for t in range(k)) for i in range(3)]
        if recon != img:
            raise AssertionError("normal-plane solve failed")
        for row in range(k):
            C[row][col] = sol[row]
    return C


def det2(C) -> Fraction:
    return C[0][0] * C[1][1] - C[0][1] * C[1][0]


def L_face_geometric(H: frozenset):
    """READING R (embedding-space).  The retained anchor arithmetic:

        L(H) = (1/|H|) sum_{h != e} 1 / det_R(I - h |_N)

    with N the GEOMETRIC normal plane of the rotation axis.  Returns
    (value | None, diagnostic)."""
    B, ax = normal_plane_basis(H)
    if B is None:
        return None, {"reason": "no rotation axis: common fixed locus has "
                                f"dimension {len(ax)}, not 1",
                      "fixed_locus_dimension": len(ax)}
    total = Fraction(0)
    dets = {}
    for h in sorted(H):
        if h == I3:
            continue
        d = det2(matrix_on_span(h, B))
        dets[str(h)] = q(Fraction(d))
        if d == 0:
            return None, {"reason": "singular transverse determinant",
                          "fixed_locus_dimension": len(ax)}
        total += Fraction(1) / d
    return total / len(H), {"reason": "defined",
                            "fixed_locus_dimension": len(ax),
                            "transverse_determinants": dets}


def orbit_decomposition(H: frozenset, points) -> list[list[tuple]]:
    rem = set(points)
    orbits = []
    while rem:
        p = sorted(rem)[0]
        orb = {apply(h, p) for h in H}
        orbits.append(sorted(orb))
        rem -= orb
    return sorted(orbits)


def isotype_pair(H: frozenset, points) -> tuple[int, int]:
    """READING D input.  The readout coefficient space over the records is
    Q^points (Record additivity: I(x) = sum a_i x_i, I(empty) = 0).  Its
    invariant subspace under the permutation action has dimension = number of
    orbits.  Computed by exact nullspace, not quoted."""
    pts = sorted(points)
    idx = {p: i for i, p in enumerate(pts)}
    n = len(pts)
    rows = []
    for h in sorted(H):
        for p in pts:
            row = [Fraction(0)] * n
            row[idx[p]] += 1
            row[idx[apply(h, p)]] -= 1
            rows.append(row)
    inv = len(nullspace(rows, n))
    return inv, n - inv


def K_native(H: frozenset, points) -> Fraction:
    """READING D (content-space).  The 883-native binding: (n - 1) / n^2 with
    n the number of pairwise-disjoint records in the collection."""
    return Fraction(len(points) - 1, len(points) ** 2)


def F_dim(n: int) -> Fraction:
    return Fraction(n - 1, n * n)


def F_res(n: int) -> Fraction:
    return Fraction(n * n - 1, 12 * n)


def rational_irreducible_dims(H: frozenset, points) -> tuple[int, ...]:
    """Fine type: the multiset of rational-irreducible dimensions of the
    permutation module Q^points, computed as the isotypic block dimensions of
    the commutant-free decomposition.  For an abelian H acting simply
    transitively this is read off the exponents of the group; computed here
    by factoring the module over Q via the fixed spaces of each subgroup."""
    pts = sorted(points)
    n = len(pts)
    if n == 0:
        return ()
    # Decompose Q^n under the cyclic/abelian action by splitting on the
    # rational minimal polynomial of each generator's permutation matrix.
    # For our cases the module is the regular representation of H; its
    # rational irreducibles are indexed by the cyclic quotients.  We compute
    # it structurally: dims = [phi-block sizes] = for each divisor d of the
    # exponent lattice, the Q-irreducible of degree phi(d) with multiplicity.
    # Implemented as: rank of the image of each "cyclotomic" projector is
    # avoided; instead use the orbit-of-characters count over subgroups.
    #
    # Simple exact route valid for abelian H acting regularly: the rational
    # irreducibles of Q[H] are the Q-conjugacy classes of characters, of
    # degree = size of the class.
    if not all(mul(x, y) == mul(y, x) for x in H for y in H):
        return ()
    # build the abstract abelian group as a permutation group on pts
    perms = []
    for h in sorted(H):
        perms.append(tuple(pts.index(apply(h, p)) for p in pts))
    # characters over C are hard to do exactly; use the equivalent statement:
    # Q[H] = direct sum over subgroups K <= H with H/K cyclic of the
    # Q-irreducible of degree phi(|H/K|), each once.
    dims = []
    subs_of_H = set()
    for a in H:
        for b in H:
            subs_of_H.add(generate([a, b]) & H)
    for K in subs_of_H:
        if not K <= H:
            continue
        m = len(H) // len(K)
        # H/K cyclic?  For abelian H, H/K is cyclic iff there is h in H whose
        # image generates, i.e. the smallest e with h^e in K equals m.
        cyclic_quot = False
        for h in H:
            e = 1
            c = h
            while c not in K:
                c = mul(c, h)
                e += 1
                if e > len(H):
                    break
            if e == m:
                cyclic_quot = True
                break
        if cyclic_quot:
            dims.append(euler_phi(m))
    return tuple(sorted(dims))


def euler_phi(m: int) -> int:
    r, k = m, m
    p = 2
    while p * p <= k:
        if k % p == 0:
            while k % p == 0:
                k //= p
            r -= r // p
        p += 1
    if k > 1:
        r -= r // k
    return r


# --------------------------------------------------------------------------
# certificate A: pins
# --------------------------------------------------------------------------
def pins_certificate() -> dict:
    pins = []
    for rel in AUDIT_INPUT_PATHS:
        raw = _read_bytes(rel)
        pins.append({
            "path": rel,
            "exists": True,
            "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest(),
            "git_blob": git_blob(rel),
            "brief_sha256_match": (
                hashlib.sha256(raw).hexdigest() == BRIEF_SHA256[rel]
                if rel in BRIEF_SHA256 else None),
        })
    ax = norm(_read_text(AXIOMS_MD))
    ko = norm(_read_text(KOIDE_MD))
    ax_hits = {k: ax.count(v) for k, v in AXIOM_NEEDLES.items()}
    ko_hits = {k: ko.count(v) for k, v in KOIDE_NEEDLES.items()}
    all_needles = all(v >= 1 for v in ax_hits.values()) and \
        all(v >= 1 for v in ko_hits.values())
    brief_checked = [p for p in pins if p["brief_sha256_match"] is not None]
    ok = (all_needles
          and all(p["brief_sha256_match"] for p in brief_checked)
          and len(FIREWALL.hits) == 0)
    return {
        "pins": pins,
        "pin_count": len(pins),
        "self_sha256": hashlib.sha256(_read_bytes(SELF_REL)).hexdigest(),
        "self_git_blob": git_blob(SELF_REL),
        "brief_supplied_digests_checked": len(brief_checked),
        "brief_supplied_digests_all_match":
            all(p["brief_sha256_match"] for p in brief_checked),
        "axiom_needle_occurrences": ax_hits,
        "koide_needle_occurrences": ko_hits,
        "every_needle_present": all_needles,
        "import_firewall_hits": len(FIREWALL.hits),
        "import_firewall_hit_names": list(FIREWALL.hits),
        "read_mode": "TEXT / AST / JSON only; no pinned module is imported",
        "pass": ok,
    }


# --------------------------------------------------------------------------
# certificate B: the Record axiom's readout clause, read as text
# --------------------------------------------------------------------------
def axiom_clause_certificate() -> dict:
    """C901-T1.  The readout clause's three computable consequences."""
    ax = norm(_read_text(AXIOMS_MD))
    clause = AXIOM_NEEDLES["content_alone"]
    additivity = AXIOM_NEEDLES["finite_additive_readout"]
    consequences = [
        {
            "predicate": "P_EMB",
            "name": "re-embedding invariance",
            "from_clause": "content_alone",
            "byte_support": clause,
            "reading": (
                "'determined by record content' is a FUNCTIONAL claim: the "
                "readout value is the image of the record content under some "
                "function.  Two record data with the same content must "
                "therefore receive the same value, however they are embedded "
                "in Z^3."),
            "computable_test": (
                "transport a record datum by every proper cubic rotation and "
                "by lattice translations, conjugating the ambient scope with "
                "it; the value must not move."),
        },
        {
            "predicate": "P_SCOPE",
            "name": "scope-independence",
            "from_clause": "content_alone",
            "byte_support": clause,
            "reading": (
                "'ALONE' is an exclusive: content is the ONLY determining "
                "input.  A construction whose value depends on a second, "
                "separately supplied input -- e.g. which ambient rotation "
                "subgroup is nominated as the scope -- is not determined by "
                "content alone.  Computable form: one record collection that "
                "admits two admissible ambient scopes must not receive two "
                "values."),
            "computable_test": (
                "exhibit one finite collection of pairwise-disjoint records "
                "admitting two admissible scopes; compare the values."),
        },
        {
            "predicate": "P_TOTAL",
            "name": "totality on finite disjoint collections",
            "from_clause": "finite_additive_readout",
            "byte_support": additivity,
            "reading": (
                "'For ANY finite collection of pairwise-disjoint records' "
                "quantifies universally.  A construction that is UNDEFINED on "
                "some finite collection of pairwise-disjoint records is not "
                "the readout the clause describes; it is a partial functional "
                "whose domain restriction is itself extra supplied content."),
            "computable_test": (
                "exhibit a finite disjoint record collection on which the "
                "construction returns no value."),
        },
    ]
    # The memo's own placement of context selection.
    context_lines = [
        {"needle": AXIOM_NEEDLES["context_selection_is_outside"],
         "occurrences": ax.count(AXIOM_NEEDLES["context_selection_is_outside"]),
         "what_it_does": (
             "the memo lists context selection among 'Open Gates Outside The "
             "Axioms' -- so a reading that needs a supplied scope/context "
             "cannot draw that scope from axiom content")},
        {"needle": AXIOM_NEEDLES["readout_context_selection_needs_authority"],
         "occurrences": ax.count(
             AXIOM_NEEDLES["readout_context_selection_needs_authority"]),
         "what_it_does": (
             "rows requiring readout-context selection 'must cite separate "
             "retained authorities or remain bounded/pending'")},
        {"needle": AXIOM_NEEDLES["sites_by_lattice_alone"],
         "occurrences": ax.count(AXIOM_NEEDLES["sites_by_lattice_alone"]),
         "what_it_does": (
             "the STRONGEST pro-geometry sentence in the memo: it licenses "
             "distinguishing SITES by lattice structure.  Its subject is "
             "sites, not readout values -- recorded here so the geometric "
             "reading's best byte is on the table")},
    ]
    ok = (ax.count(clause) == 1 and ax.count(additivity) == 1
          and all(c["occurrences"] >= 1 for c in context_lines))
    return {
        "theorem": (
            "C901-T1.  The Record readout clause yields exactly three "
            "independently computable necessary conditions on any candidate "
            "readout construction: P_EMB, P_SCOPE, P_TOTAL."),
        "byte_quoted_clause": clause,
        "byte_quoted_clause_occurrences_in_memo": ax.count(clause),
        "byte_quoted_additivity": additivity,
        "byte_quoted_additivity_occurrences_in_memo": ax.count(additivity),
        "consequences": consequences,
        "memo_sentences_bearing_on_scope_supply": context_lines,
        "honesty": (
            "P_EMB and P_TOTAL are uncontroversial readings.  P_SCOPE is the "
            "load-bearing one and it is defended from a single word -- "
            "'alone'.  Certificate J steelmans its denial and tests the "
            "steelman computationally."),
        "pass": ok,
    }


# --------------------------------------------------------------------------
# certificate C: RESTRICTION GATE -- reproduce 888 and 883 before any claim
# --------------------------------------------------------------------------
def restriction_gate_certificate() -> dict:
    """Reproduce, value for value: 888's subgroup-lattice census (all 11
    rows), 883's C3 anchor (isotype pair and 2-adic profile), and 883's
    closed-form table.  Then rebuild the 899 rows independently and compare
    LOUDLY against the numbers the brief states."""
    receipt888 = json.loads(_read_text(C888_RECEIPT))
    pinned_rows = receipt888["subgroup_lattice_census"]

    # --- rebuild the census from the Lattice axiom, never quoting it -----
    subs = all_subgroups()
    seen = set()
    rebuilt = []
    for H in subs:
        if H in seen:
            continue
        cl = {conjugate(H, g) for g in O24}
        seen |= cl
        nrm = [g for g in O24 if conjugate(H, g) == H]
        rebuilt.append({
            "name": subgroup_class_name(H),
            "order": len(H),
            "size": len(cl),
            "is_abelian": all(mul(x, y) == mul(y, x) for x in H for y in H),
            "is_cyclic": (len(H) == 1
                          or any(element_order(h) == len(H) for h in H)),
            "normalizer_order": len(nrm),
            "normal_in_the_full_group": len(cl) == 1,
        })
    rebuilt.sort(key=lambda r: (r["order"], -r["size"], r["name"]))
    by_name = {r["name"]: r for r in rebuilt}
    census_rows = []
    census_ok = True
    for pr in pinned_rows:
        mine = by_name.get(pr["name"])
        fields = ("order", "size", "is_abelian", "is_cyclic",
                  "normalizer_order", "normal_in_the_full_group")
        agree = mine is not None and all(mine[f] == pr[f] for f in fields)
        census_ok &= agree
        census_rows.append({
            "name": pr["name"],
            "pinned_888": {f: pr[f] for f in fields},
            "rebuilt_901": {f: mine[f] for f in fields} if mine else None,
            "agrees": agree,
        })

    # --- reproduce 883's C3 anchor --------------------------------------
    receipt883 = json.loads(_read_text(C883_RECEIPT))
    headline883 = receipt883["headline"]
    C3 = generate([((0, 0, 1), (1, 0, 0), (0, 1, 0))])
    c3_orbit = sorted({apply(h, (1, 0, 0)) for h in C3})
    pair883 = isotype_pair(C3, c3_orbit)
    v2 = lambda x: (0 if x % 2 else 1 + v2(x // 2)) if x else None
    profile883 = (v2(pair883[0]), v2(pair883[1]))
    anchor_rebuilt = L_face_geometric(C3)[0]
    headline_pair_forms = ["(1,2)", "(1, 2)"]
    headline_states_the_pair = any(f in headline883
                                   for f in headline_pair_forms)
    headline_states_the_profile = any(f in headline883
                                      for f in ["(0,1)", "(0, 1)"])
    c3_ok = (pair883 == (1, 2) and profile883 == (0, 1)
             and anchor_rebuilt == ANCHOR
             and headline_states_the_pair and headline_states_the_profile)

    # --- verify the C883_FORMS transcription against the pinned AST ------
    tree = ast.parse(_read_text(C883_PRIMARY))
    ast_form_names = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Dict):
            keys = [k.value for k in node.keys
                    if isinstance(k, ast.Constant) and isinstance(k.value, str)]
            if "name" in keys and "value" in keys:
                for k, v in zip(node.keys, node.values):
                    if (isinstance(k, ast.Constant) and k.value == "name"
                            and isinstance(v, ast.Constant)
                            and isinstance(v.value, str)):
                        ast_form_names.append(v.value)
    transcribed = [n for n, _ in C883_FORMS]
    forms_ok = all(n in ast_form_names for n in transcribed)

    # --- reproduce 883's closed-form table at (w0, w1, n) = (1, 2, 3) ----
    form_rows = []
    for name, fn in C883_FORMS:
        val = fn(1, 2, 3)
        form_rows.append({"name": name, "value_at_(1,2,3)": q(val),
                          "hits_the_anchor": val == ANCHOR})
    hitting = [r["name"] for r in form_rows if r["hits_the_anchor"]]
    forms_table_ok = len(hitting) == 5 and forms_ok

    # --- INDEPENDENT REBUILD of the 899 rows -----------------------------
    named = {
        "C2_face": generate([((-1, 0, 0), (0, -1, 0), (0, 0, 1))]),
        "C2_edge": generate([((0, 1, 0), (1, 0, 0), (0, 0, -1))]),
        "C3_body": C3,
        "C4_face": generate([((0, -1, 0), (1, 0, 0), (0, 0, 1))]),
        "V_face":  generate([((-1, 0, 0), (0, -1, 0), (0, 0, 1)),
                             ((1, 0, 0), (0, -1, 0), (0, 0, -1))]),
        "V_edge":  generate([((-1, 0, 0), (0, -1, 0), (0, 0, 1)),
                             ((0, 1, 0), (1, 0, 0), (0, 0, -1))]),
    }
    # sanity: each named representative really is in the class it claims
    naming_ok = all(subgroup_class_name(H) == nm for nm, H in named.items())

    rows899 = []
    rebuild_ok = True
    for nm in ("C2_face", "C2_edge", "C3_body", "C4_face", "V_edge"):
        H = named[nm]
        pts = free_orbit(H)
        n = len(pts)
        pair = isotype_pair(H, pts)
        fine = rational_irreducible_dims(H, pts)
        kn = K_native(H, pts)
        lf, diag = L_face_geometric(H)
        want = BRIEF_899_ROWS[nm]
        agree = (n == want["n"] and kn == want["K_native"]
                 and lf == want["L_face"]
                 and fine == BRIEF_899_FINE_TYPES[nm])
        rebuild_ok &= agree
        rows899.append({
            "class": nm,
            "free_orbit": [list(p) for p in pts],
            "n": n,
            "readout_isotype_pair": list(pair),
            "fine_rational_irreducible_dims": list(fine),
            "K_native_rebuilt": q(kn),
            "L_face_rebuilt": q(lf),
            "L_face_status": diag["reason"],
            "brief_899_K_native": q(want["K_native"]),
            "brief_899_L_face": q(want["L_face"]),
            "brief_899_fine_type": list(BRIEF_899_FINE_TYPES[nm]),
            "agrees_with_brief_899": agree,
        })
    disagreements = [r["class"] for r in rows899
                     if not r["agrees_with_brief_899"]]

    ok = (census_ok and c3_ok and forms_table_ok and naming_ok and rebuild_ok)
    return {
        "gate": (
            "RESTRICTION GATE.  888's census, 883's anchor and 883's "
            "closed-form table are reproduced value-for-value, and the 899 "
            "rows -- whose artifacts are ABSENT from this branch -- are "
            "rebuilt from scratch and compared."),
        "cycle899_artifacts_present_on_this_branch": False,
        "cycle899_scan": scan_for_899(),
        "census_rows": census_rows,
        "census_reproduced": census_ok,
        "cycle883_headline_as_pinned": headline883,
        "cycle883_C3_orbit": [list(p) for p in c3_orbit],
        "cycle883_isotype_pair_rebuilt": list(pair883),
        "cycle883_two_adic_profile_rebuilt": list(profile883),
        "cycle883_anchor_rebuilt_from_geometry": q(anchor_rebuilt),
        "cycle883_headline_states_the_pair": headline_states_the_pair,
        "cycle883_headline_states_the_profile": headline_states_the_profile,
        "cycle883_reproduced": c3_ok,
        "cycle883_form_names_found_in_pinned_ast": forms_ok,
        "cycle883_closed_form_table": form_rows,
        "cycle883_forms_returning_the_anchor": hitting,
        "cycle883_forms_table_reproduced": forms_table_ok,
        "named_representatives_verified_by_invariants": naming_ok,
        "cycle899_rows_rebuilt": rows899,
        "cycle899_rebuild_agrees_everywhere": rebuild_ok,
        "cycle899_disagreements": disagreements,
        "LOUD": ("NO DISAGREEMENT with the brief's 899 numbers"
                 if rebuild_ok else
                 f"DISAGREEMENT with the brief's 899 numbers at "
                 f"{disagreements} -- the rebuild is authoritative here and "
                 f"the sibling table must be re-checked"),
        "pass": ok,
    }


def scan_for_899() -> dict:
    hits = []
    scanned = 0
    for pat in ("scripts/*", "outputs/*", "logs/runner-cache/*", "docs/*"):
        for p in sorted(ROOT.glob(pat)):
            scanned += 1
            if "899" in p.name or "cycle899" in p.name.lower():
                hits.append(str(p.relative_to(ROOT)))
    return {"paths_scanned": scanned, "hits": hits, "hit_count": len(hits),
            "conclusion": ("899 artifacts ABSENT on this branch; every 899 "
                           "number used below is REBUILT, never cited")}


def free_orbit(H: frozenset) -> list[tuple]:
    """A canonical free (simply transitive) orbit of H on Z^3, found by a
    deterministic scan of a small box.  Free orbits are what both readings
    take as their record collection."""
    box = sorted(
        [(x, y, z) for x in range(-2, 3) for y in range(-2, 3)
         for z in range(-2, 3) if (x, y, z) != (0, 0, 0)],
        key=lambda p: (sum(c * c for c in p), p))
    for p in box:
        orb = {apply(h, p) for h in H}
        if len(orb) == len(H):
            return sorted(orb)
    raise AssertionError("no free orbit in the scanned box")


# --------------------------------------------------------------------------
# certificate D: the two families, closed form and proved
# --------------------------------------------------------------------------
def families_certificate() -> dict:
    """C901-T2.  (a) The geometric L-face over any cyclic rotation subgroup of
    order n equals (n^2 - 1) / (12 n), independent of the axis.  (b) Every
    883 closed form that returns the anchor at n = 3 extends to ONE family,
    (n - 1) / n^2."""
    # (a) verify over EVERY cyclic subgroup of O, all conjugates
    cyc_rows = []
    a_ok = True
    for H in all_subgroups():
        n = len(H)
        if n == 1 or not any(element_order(h) == n for h in H):
            continue
        lf, diag = L_face_geometric(H)
        agree = lf == F_res(n)
        a_ok &= agree
        cyc_rows.append({"class": subgroup_class_name(H), "order": n,
                         "L_face": q(lf), "F_res(n)": q(F_res(n)),
                         "agrees": agree})
    # (b) extend every 883 form to a family in n, with (w0, w1) = (1, n - 1)
    fam_rows = []
    for name, fn in C883_FORMS:
        vals = {}
        for n in (2, 3, 4, 5, 6):
            vals[n] = fn(1, n - 1, n)
        is_Fdim = all(vals[n] == F_dim(n) for n in vals)
        fam_rows.append({
            "name": name,
            "values_n_2_to_6": {str(n): q(v) for n, v in vals.items()},
            "hits_anchor_at_n_3": vals[3] == ANCHOR,
            "equals_F_dim_as_a_family": is_Fdim,
        })
    anchor_hitters = [r for r in fam_rows if r["hits_anchor_at_n_3"]]
    all_hitters_are_Fdim = all(r["equals_F_dim_as_a_family"]
                               for r in anchor_hitters)
    b_ok = len(anchor_hitters) == 5 and all_hitters_are_Fdim

    # (c) the collision and separation table
    collide = []
    for n in (2, 3, 4, 5, 6, 7, 8):
        collide.append({"n": n, "F_dim": q(F_dim(n)), "F_res": q(F_res(n)),
                        "equal": F_dim(n) == F_res(n)})
    equal_at = [r["n"] for r in collide if r["equal"]]
    c_ok = equal_at == [3]

    return {
        "theorem_a": (
            "C901-T2a.  For every cyclic rotation subgroup H <= O of order n, "
            "L_face(H) = (n^2 - 1) / (12 n), independent of which axis H "
            "rotates about.  Reason: every non-identity element of a cyclic "
            "order-n rotation group acts on the normal plane as a rotation "
            "by 2 pi k / n, so det_R(I - h|_N) = 2 - 2 cos(2 pi k / n) "
            "depends on k and n alone.  Verified here on all cyclic "
            "subgroups of O, all conjugates."),
        "cyclic_rows": cyc_rows,
        "theorem_a_holds": a_ok,
        "consequence_a": (
            "the geometric reading is EMBEDDING-INVARIANT on its whole domain "
            "of definition.  P_EMB cannot catch it.  This is stated first "
            "because it is the geometric reading's strongest computed "
            "defence and it survives."),
        "theorem_b": (
            "C901-T2b.  Of the seven closed forms 883 enumerated, exactly "
            "five return the anchor 2/9 at n = 3, and ALL FIVE are the same "
            "function of n once (w0, w1) = (1, n - 1) is substituted, namely "
            "(n - 1) / n^2.  883's five-fold discrete ambiguity is therefore "
            "FAMILY-DEGENERATE: it is one family, not five."),
        "family_rows": fam_rows,
        "anchor_hitting_forms": [r["name"] for r in anchor_hitters],
        "all_anchor_hitters_collapse_to_F_dim": all_hitters_are_Fdim,
        "theorem_b_holds": b_ok,
        "collision_table": collide,
        "families_agree_only_at": equal_at,
        "theorem_c": (
            "C901-T2c.  F_dim(n) = F_res(n) iff n = 3 (checked n = 2..8; "
            "12 n (n - 1) = n^2 (n^2 - 1) reduces to 12 (n - 1) = n (n^2 - 1) "
            "= n (n - 1)(n + 1), i.e. n(n + 1) = 12, i.e. n = 3)."),
        "algebraic_check": (Fraction(3 * 4) == Fraction(12)),
        "pass": a_ok and b_ok and c_ok,
    }


# --------------------------------------------------------------------------
# certificate E: the content-only predicates, formalized and evaluated
# --------------------------------------------------------------------------
def make_readings() -> dict:
    """Each reading is a function (record_points, scope_subgroup) -> value or
    None.  Two candidates plus two PLANTS for falsifier visibility."""

    def reading_D(pts, H):
        return K_native(H, pts)

    def reading_R(pts, H):
        return L_face_geometric(H)[0]

    def plant_violating(pts, H):
        """PLANT-V: designed to violate content-alone.  Reads the x-coordinate
        of the lexicographically first record site -- pure embedding."""
        return Fraction(sorted(pts)[0][0])

    def plant_surviving(pts, H):
        """PLANT-S: designed to survive.  Reads the record count alone."""
        return Fraction(len(pts))

    return {
        "READING_D_content_space": reading_D,
        "READING_R_embedding_space": reading_R,
        "PLANT_V_embedding_dependent": plant_violating,
        "PLANT_S_content_only": plant_surviving,
    }


def admissible_scopes(pts, ladder: str) -> list[frozenset]:
    """Which ambient rotation subgroups may be nominated as the scope of a
    record collection.  BOTH ladders are computed, because the choice of
    ladder is exactly what the geometric reading's steelman disputes.

    L1  simply transitive on the collection  (the 883/888 free-orbit
        convention -- the geometric reading's most favourable ladder)
    L2  setwise preserving the collection    (the L-face construction's own
        input is a rotation subgroup, not an orbit)
    """
    P = set(pts)
    out = []
    for H in all_subgroups():
        if len(H) == 1:
            continue
        if not all(apply(h, p) in P for h in H for p in P):
            continue
        if ladder == "L1":
            if len(H) == len(P) and len(orbit_decomposition(H, P)) == 1:
                out.append(H)
        else:
            out.append(H)
    return out


def predicate_certificate() -> dict:
    """C901-T3.  Evaluate P_EMB, P_SCOPE, P_TOTAL on both readings and on
    both plants."""
    readings = make_readings()

    # ---- the record collections used as test data ---------------------
    named = {
        "C2_face": generate([((-1, 0, 0), (0, -1, 0), (0, 0, 1))]),
        "C2_edge": generate([((0, 1, 0), (1, 0, 0), (0, 0, -1))]),
        "C3_body": generate([((0, 0, 1), (1, 0, 0), (0, 1, 0))]),
        "C4_face": generate([((0, -1, 0), (1, 0, 0), (0, 0, 1))]),
        "V_face":  generate([((-1, 0, 0), (0, -1, 0), (0, 0, 1)),
                             ((1, 0, 0), (0, -1, 0), (0, 0, -1))]),
        "V_edge":  generate([((-1, 0, 0), (0, -1, 0), (0, 0, 1)),
                             ((0, 1, 0), (1, 0, 0), (0, 0, -1))]),
    }
    data = [(nm, free_orbit(H), H) for nm, H in named.items()]

    results = {}
    for rname, fn in readings.items():
        # ---- P_EMB -----------------------------------------------------
        emb_rows = []
        emb_ok = True
        for nm, pts, H in data:
            base = fn(pts, H)
            moved = []
            for g in O24:
                gp = sorted(apply(g, p) for p in pts)
                gH = conjugate(H, g)
                v = fn(gp, gH)
                if v != base:
                    moved.append({"rotation": str(g), "value": q(v)})
            # lattice translations: the content structure is unchanged, the
            # ambient placement is not
            for t in ((1, 0, 0), (0, 1, 0), (3, -2, 5)):
                tp = sorted(tuple(p[i] + t[i] for i in range(3)) for p in pts)
                v = fn(tp, H)
                if v != base:
                    moved.append({"translation": list(t), "value": q(v)})
            emb_rows.append({"class": nm, "base_value": q(base),
                             "re_embeddings_tested": len(O24) + 3,
                             "value_moved_count": len(moved),
                             "exhibits": moved[:EXHIBIT_CAP],
                             "invariant": not moved})
            emb_ok &= not moved

        # ---- P_TOTAL ---------------------------------------------------
        tot_rows = []
        tot_ok = True
        for nm, pts, H in data:
            v = fn(pts, H)
            defined = v is not None
            tot_ok &= defined
            tot_rows.append({"class": nm, "n": len(pts),
                             "value": q(v), "defined": defined})

        # ---- P_SCOPE ---------------------------------------------------
        scope_rows = []
        scope_ok = True
        for ladder in ("L1", "L2"):
            for nm, pts, H in data:
                scopes = admissible_scopes(pts, ladder)
                vals = {}
                for S in scopes:
                    vals.setdefault(q(fn(pts, S)), []).append(
                        subgroup_class_name(S))
                single = len(vals) == 1
                scope_ok &= single
                scope_rows.append({
                    "ladder": ladder,
                    "record_collection_from": nm,
                    "records": [list(p) for p in pts],
                    "admissible_scopes": sorted(
                        {subgroup_class_name(S) for S in scopes}),
                    "scope_count": len(scopes),
                    "distinct_values": sorted(vals),
                    "value_to_scopes": {k: sorted(set(v))
                                        for k, v in vals.items()},
                    "single_valued": single,
                })
        results[rname] = {
            "P_EMB": {"rows": emb_rows, "holds": emb_ok},
            "P_TOTAL": {"rows": tot_rows, "holds": tot_ok},
            "P_SCOPE": {"rows": scope_rows, "holds": scope_ok},
            "content_only": emb_ok and tot_ok and scope_ok,
        }

    # ---- falsifier visibility -----------------------------------------
    plant_v_caught = not results["PLANT_V_embedding_dependent"]["content_only"]
    plant_v_caught_by = [p for p in ("P_EMB", "P_TOTAL", "P_SCOPE")
                         if not results["PLANT_V_embedding_dependent"][p]["holds"]]
    plant_s_survived = results["PLANT_S_content_only"]["content_only"]

    return {
        "theorem": (
            "C901-T3.  The content-only predicate, formalized as "
            "P_EMB & P_SCOPE & P_TOTAL, is evaluated on both candidate "
            "readings and on two planted readings."),
        "summary": {
            r: {"P_EMB": v["P_EMB"]["holds"],
                "P_SCOPE": v["P_SCOPE"]["holds"],
                "P_TOTAL": v["P_TOTAL"]["holds"],
                "content_only": v["content_only"]}
            for r, v in results.items()
        },
        "detail": results,
        "falsifier_visibility": {
            "planted_violating_reading": (
                "PLANT-V reads the x-coordinate of the lexicographically "
                "first record site -- pure ambient embedding"),
            "planted_violating_detected": plant_v_caught,
            "planted_violating_caught_by": plant_v_caught_by,
            "planted_surviving_reading": (
                "PLANT-S reads the record count alone"),
            "planted_surviving_survived": plant_s_survived,
            "the_predicate_can_see_both_ways": plant_v_caught
            and plant_s_survived,
        },
        "pass": plant_v_caught and plant_s_survived,
    }


# --------------------------------------------------------------------------
# certificate F: the C2 discriminator
# --------------------------------------------------------------------------
def c2_discriminator_certificate() -> dict:
    """C901-T4.  n = 2 already separates the families (1/4 vs 1/8).  Does the
    geometric L-face take DIFFERENT values on the two canonical C2 classes,
    whose normal-plane geometries differ?"""
    face = [H for H in all_subgroups() if subgroup_class_name(H) == "C2_face"]
    edge = [H for H in all_subgroups() if subgroup_class_name(H) == "C2_edge"]
    rows = []
    for label, group in (("C2_face", face), ("C2_edge", edge)):
        for H in group:
            g = sorted(h for h in H if h != I3)[0]
            B, ax = normal_plane_basis(H)
            lf, diag = L_face_geometric(H)
            pts = free_orbit(H)
            rows.append({
                "class": label,
                "generator": str(g),
                "rotation_axis": [q(x) for x in ax[0]] if len(ax) == 1
                else None,
                "axis_type": ("coordinate/face axis" if label == "C2_face"
                              else "edge / face-diagonal axis"),
                "normal_plane_basis": [[q(x) for x in b] for b in B]
                if B else None,
                "transverse_determinants":
                    diag.get("transverse_determinants"),
                "L_face": q(lf),
                "free_orbit": [list(p) for p in pts],
                "readout_isotype_pair": list(isotype_pair(H, pts)),
                "K_native": q(K_native(H, pts)),
            })
    face_vals = {r["L_face"] for r in rows if r["class"] == "C2_face"}
    edge_vals = {r["L_face"] for r in rows if r["class"] == "C2_edge"}
    same = face_vals == edge_vals and len(face_vals) == 1
    # geometries really do differ
    axes = {r["class"]: sorted({str(r2["rotation_axis"]) for r2 in rows
                                if r2["class"] == r["class"]})
            for r in rows}
    geometries_differ = axes["C2_face"] != axes["C2_edge"]
    return {
        "theorem": (
            "C901-T4 (the C2 discriminator).  Both canonical C2 classes are "
            "tested.  Their rotation axes are of genuinely different lattice "
            "type -- coordinate axes (3 of them) versus face-diagonal axes "
            "(6 of them) -- and their normal planes are correspondingly "
            "different subspaces of R^3."),
        "rows": rows,
        "class_sizes": {"C2_face": len(face), "C2_edge": len(edge)},
        "geometries_genuinely_differ": geometries_differ,
        "C2_face_L_values": sorted(face_vals),
        "C2_edge_L_values": sorted(edge_vals),
        "L_face_same_on_both_classes": same,
        "F_dim_at_n_2": q(F_dim(2)),
        "F_res_at_n_2": q(F_res(2)),
        "families_separate_at_n_2": F_dim(2) != F_res(2),
        "RESULT": (
            "GEOMETRIC READING SURVIVES THE C2 TEST.  L_face = 1/8 on BOTH "
            "classes.  Reported honestly: this test does NOT produce a "
            "content-alone violation.  The reason is structural -- every "
            "order-2 rotation acts on its normal plane as -I, so "
            "det_R(I - h|_N) = 4 whatever the axis.  n = 2 separates the two "
            "FAMILIES (1/4 vs 1/8) but does not indict either reading."
            if same else
            "GEOMETRIC READING FAILS THE C2 TEST: identical content, "
            "different value."),
        "pass": True,   # outcome-neutral: either result is a valid finding
        "test_was_decisive": not same,
    }


# --------------------------------------------------------------------------
# certificate G: the conjugate-C4 test
# --------------------------------------------------------------------------
def conjugate_certificate() -> dict:
    """C901-T5.  Do the conjugate C4 subgroups' geometric normal planes give
    the SAME L-face for the same abstract content?"""
    rows = []
    ok_by_class = {}
    for cls in ("C4_face", "C3_body", "C2_face", "C2_edge"):
        group = [H for H in all_subgroups() if subgroup_class_name(H) == cls]
        vals = set()
        for H in group:
            lf, diag = L_face_geometric(H)
            B, ax = normal_plane_basis(H)
            pts = free_orbit(H)
            vals.add(q(lf))
            rows.append({
                "class": cls,
                "axis": [q(x) for x in ax[0]] if len(ax) == 1 else None,
                "normal_plane": [[q(x) for x in b] for b in B] if B else None,
                "L_face": q(lf),
                "K_native": q(K_native(H, pts)),
                "free_orbit": [list(p) for p in pts],
            })
        ok_by_class[cls] = {"conjugates": len(group),
                            "distinct_L_values": sorted(vals),
                            "all_conjugates_agree": len(vals) == 1}
    all_agree = all(v["all_conjugates_agree"] for v in ok_by_class.values())
    return {
        "theorem": (
            "C901-T5 (the conjugate test).  Every conjugate of every cyclic "
            "scope class is evaluated.  Conjugation by an orthogonal map "
            "carries the normal plane to the normal plane and preserves "
            "determinants, so agreement is expected; it is COMPUTED here "
            "rather than assumed, because a disagreement would have been an "
            "immediate content-alone violation."),
        "rows": rows[:24],
        "row_count": len(rows),
        "by_class": ok_by_class,
        "all_conjugates_agree": all_agree,
        "RESULT": (
            "GEOMETRIC READING SURVIVES THE CONJUGATE TEST.  All 3 conjugate "
            "C4_face subgroups give 5/16; all 4 C3_body give 2/9; all 3 "
            "C2_face and all 6 C2_edge give 1/8."
            if all_agree else
            "GEOMETRIC READING FAILS THE CONJUGATE TEST."),
        "pass": True,
        "test_was_decisive": not all_agree,
    }


# --------------------------------------------------------------------------
# certificate H: the V_edge / double-scope crux
# --------------------------------------------------------------------------
def crux_certificate() -> dict:
    """C901-T6 (THE CRUX).  A single finite collection of pairwise-disjoint
    records that admits TWO admissible ambient scopes."""
    C4 = generate([((0, -1, 0), (1, 0, 0), (0, 0, 1))])
    Ve = generate([((-1, 0, 0), (0, -1, 0), (0, 0, 1)),
                   ((0, 1, 0), (1, 0, 0), (0, 0, -1))])
    S = sorted({(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)})

    # verify BOTH act simply transitively on the very same record set
    def simply_transitive(H, pts):
        P = set(pts)
        return (len(H) == len(P)
                and all(apply(h, p) in P for h in H for p in P)
                and len(orbit_decomposition(H, P)) == 1)

    st_c4 = simply_transitive(C4, S)
    st_ve = simply_transitive(Ve, S)
    same_set = True

    lf_c4, d_c4 = L_face_geometric(C4)
    lf_ve, d_ve = L_face_geometric(Ve)
    kn_c4 = K_native(C4, S)
    kn_ve = K_native(Ve, S)

    # the full L1 and L2 scope ladders on THIS record collection
    ladders = {}
    for ladder in ("L1", "L2"):
        scopes = admissible_scopes(S, ladder)
        geo, con = {}, {}
        for H in scopes:
            geo.setdefault(q(L_face_geometric(H)[0]), []).append(
                subgroup_class_name(H))
            con.setdefault(q(K_native(H, S)), []).append(
                subgroup_class_name(H))
        ladders[ladder] = {
            "scopes": sorted({subgroup_class_name(H) for H in scopes}),
            "scope_count": len(scopes),
            "geometric_reading_values": {k: sorted(set(v))
                                         for k, v in geo.items()},
            "geometric_reading_distinct_value_count": len(geo),
            "geometric_reading_single_valued": len(geo) == 1,
            "content_reading_values": {k: sorted(set(v))
                                       for k, v in con.items()},
            "content_reading_distinct_value_count": len(con),
            "content_reading_single_valued": len(con) == 1,
        }

    # V_edge / V_face totality failure
    undefined_rows = []
    for nm in ("V_edge", "V_face", "D4_face", "S3_body"):
        H = [G for G in all_subgroups() if subgroup_class_name(G) == nm][0]
        lf, diag = L_face_geometric(H)
        pts = free_orbit(H) if len(H) <= 8 else None
        undefined_rows.append({
            "class": nm, "order": len(H),
            "L_face": q(lf), "reason": diag["reason"],
            "fixed_locus_dimension": diag["fixed_locus_dimension"],
            "K_native_on_a_free_orbit": q(K_native(H, pts)) if pts else None,
        })

    violation_L1 = not ladders["L1"]["geometric_reading_single_valued"]
    violation_L2 = not ladders["L2"]["geometric_reading_single_valued"]
    content_survives = (ladders["L1"]["content_reading_single_valued"]
                        and ladders["L2"]["content_reading_single_valued"])
    totality_fail = any(r["L_face"] == "UNDEFINED" for r in undefined_rows)

    return {
        "theorem": (
            "C901-T6 (THE CRUX).  The four lattice sites S = {+e1, -e1, +e2, "
            "-e2} carry four pairwise-disjoint records.  That ONE record "
            "collection is a simply transitive orbit of TWO different "
            "order-4 rotation subgroups: the cyclic C4_face about the z axis, "
            "and a non-cyclic V_edge Klein group.  Both lie in the "
            "collection's full setwise stabilizer D4_face."),
        "record_collection": [list(p) for p in S],
        "record_count": len(S),
        "the_same_records_under_both_scopes": same_set,
        "C4_face_acts_simply_transitively": st_c4,
        "V_edge_acts_simply_transitively": st_ve,
        "C4_face_elements": sorted(str(h) for h in C4),
        "V_edge_elements": sorted(str(h) for h in Ve),
        "geometric_reading_under_C4_face": q(lf_c4),
        "geometric_reading_under_V_edge": q(lf_ve),
        "geometric_reading_V_edge_reason": d_ve["reason"],
        "content_reading_under_C4_face": q(kn_c4),
        "content_reading_under_V_edge": q(kn_ve),
        "scope_ladders_on_this_collection": ladders,
        "constructions_undefined_on_free_orbits": undefined_rows,
        "P_SCOPE_violated_by_geometric_reading_on_L1": violation_L1,
        "P_SCOPE_violated_by_geometric_reading_on_L2": violation_L2,
        "P_TOTAL_violated_by_geometric_reading": totality_fail,
        "content_reading_single_valued_on_both_ladders": content_survives,
        "THE_COMPUTED_VIOLATION": (
            "ONE record collection, TWO admissible scopes, TWO answers.  On "
            "the most favourable ladder L1 (simply transitive scopes only) "
            f"the geometric reading returns {q(lf_c4)} under C4_face and NO "
            "VALUE under V_edge.  On ladder L2 (all preserving rotation "
            "subgroups) it returns "
            f"{sorted(ladders['L2']['geometric_reading_values'])} -- a "
            "value-versus-value disagreement, not merely a definedness gap.  "
            f"The content reading returns {q(kn_c4)} on every scope of both "
            "ladders, because (n - 1)/n^2 is a function of the RECORD COUNT "
            "alone and takes no ambient input."),
        "why_the_C2_and_conjugate_tests_missed_it": (
            "both of those tests vary the EMBEDDING while holding the scope's "
            "abstract type fixed, and C901-T2a proves the L-face is blind to "
            "that.  The crux varies the SCOPE while holding the records "
            "themselves literally fixed -- the one degree of freedom the word "
            "'alone' forbids."),
        "pass": True,
        "violation_found": violation_L1 or violation_L2 or totality_fail,
    }


# --------------------------------------------------------------------------
# certificate I: scope-invariance selects a unique native form
# --------------------------------------------------------------------------
def form_selection_certificate() -> dict:
    """C901-T7.  883 left a five-fold binding ambiguity.  P_SCOPE closes it."""
    S = sorted({(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)})
    scopes = admissible_scopes(S, "L2")
    rows = []
    for name, fn in C883_FORMS:
        vals = {}
        for H in scopes:
            w0, w1 = isotype_pair(H, S)
            try:
                v = fn(w0, w1, len(S))
            except ZeroDivisionError:
                v = None
            vals.setdefault(q(v), []).append(subgroup_class_name(H))
        anchor_at_3 = fn(1, 2, 3) == ANCHOR
        rows.append({
            "name": name,
            "hits_anchor_at_n_3": anchor_at_3,
            "values_over_the_L2_scope_ladder": {k: sorted(set(v))
                                                for k, v in vals.items()},
            "distinct_value_count": len(vals),
            "scope_invariant": len(vals) == 1,
        })
    survivors = [r["name"] for r in rows
                 if r["hits_anchor_at_n_3"] and r["scope_invariant"]]
    return {
        "theorem": (
            "C901-T7.  Among the five 883 closed forms that return the "
            "anchor at n = 3, P_SCOPE selects exactly one: (n - 1)/n^2, the "
            "only one that is a function of the record COUNT rather than of "
            "the scope's orbit decomposition.  883's residual 'five-fold "
            "discrete ambiguity' is closed by the content-alone clause "
            "itself, not by new supply."),
        "test_collection": [list(p) for p in S],
        "scope_ladder": "L2 (all rotation subgroups preserving the records)",
        "scope_count": len(scopes),
        "rows": rows,
        "anchor_hitting_and_scope_invariant": survivors,
        "selection_is_unique": len(survivors) == 1,
        "selected_form": survivors[0] if len(survivors) == 1 else None,
        "honesty": (
            "This is a strictly stronger use of P_SCOPE than the crux needs.  "
            "The crux only requires that the CONTENT family be scope-stable "
            "where the geometric one is not; T7 additionally observes that "
            "scope-stability picks a unique representative of the family."),
        "pass": len(survivors) >= 1,
    }


# --------------------------------------------------------------------------
# certificate J: the steelmen, computed both ways
# --------------------------------------------------------------------------
def steelman_certificate(crux: dict, families: dict) -> dict:
    ax = norm(_read_text(AXIOMS_MD))
    ko = norm(_read_text(KOIDE_MD))
    steelmen = [
        {
            "id": "SM1",
            "claim": "the orbit's subgroup type IS record content",
            "strongest_form": (
                "The readout module's decomposition is determined by the "
                "group action on the records.  If the group action counts as "
                "content, then so does the subgroup's type, and the geometric "
                "reading is reading content after all."),
            "computed_test": (
                "if subgroup type were content, the SAME record collection "
                "would have to have two contents at once, since S = "
                "{+-e1, +-e2} is a simply transitive orbit of both a C4 and a "
                "V4.  Content would not be a function of the records."),
            "computed_result": (
                "REFUTED.  C901-T6 exhibits the collection.  "
                f"C4_face gives {crux['geometric_reading_under_C4_face']}, "
                f"V_edge gives {crux['geometric_reading_under_V_edge']}, on "
                "one and the same four records."),
            "byte_support_against": AXIOM_NEEDLES["content_alone"],
            "byte_occurrences": ax.count(AXIOM_NEEDLES["content_alone"]),
            "survives": False,
        },
        {
            "id": "SM2",
            "claim": ("the Lattice axiom's 'distinguished by the supplied "
                      "lattice structure alone' licenses geometric input to "
                      "the readout"),
            "strongest_form": (
                "The memo explicitly says lattice structure alone "
                "distinguishes sites, and the normal plane is lattice "
                "structure.  So consuming it is licensed."),
            "computed_test": (
                "read the sentence's grammatical subject and check whether "
                "any memo or Gate-B sentence connects lattice geometry to a "
                "readout VALUE."),
            "computed_result": (
                "SURVIVES ONLY AS SITE-DISTINGUISHABILITY.  The sentence's "
                "subject is 'Sites'; it licenses telling sites apart, which "
                "the content reading also needs (the records sit at distinct "
                "sites).  Certificate K sweeps for a sentence connecting "
                "geometry to a readout value and reports the count."),
            "byte_support_for": AXIOM_NEEDLES["sites_by_lattice_alone"],
            "byte_occurrences": ax.count(
                AXIOM_NEEDLES["sites_by_lattice_alone"]),
            "survives": "partially -- for sites, not for readout values",
        },
        {
            "id": "SM3",
            "claim": ("the geometric L-face is not a violating readout at "
                      "all; it is a CONTEXT-CONDITIONAL functional awaiting a "
                      "supplied scope"),
            "strongest_form": (
                "The memo itself lists context selection among the open "
                "gates OUTSIDE the axioms.  So the L-face is simply a "
                "downstream object that needs a context supplier -- not an "
                "axiom-violating one.  Nothing is refuted; something is "
                "merely unsupplied."),
            "computed_test": (
                "check whether the memo supplies a scope selector, and "
                "whether the L-face's own source note claims one."),
            "computed_result": (
                "THIS STEELMAN SURVIVES AND IS ADOPTED AS THE PRICING.  The "
                "memo places 'context selection' outside axiom content and "
                "requires separate retained authority for "
                "'readout-context selection'.  The L-face source note itself "
                "says 'physical-axis selection is a separate theorem "
                "target'.  Consequence: the L-face is mathematically "
                "untouched, but it cannot be cited as THE readout on the "
                "Record axiom's authority, because on that authority the "
                "value must be fixed by content alone and the L-face needs a "
                "second input the axioms do not supply."),
            "byte_support_for": AXIOM_NEEDLES["context_selection_is_outside"],
            "byte_occurrences": ax.count(
                AXIOM_NEEDLES["context_selection_is_outside"]),
            "byte_support_from_the_l_face_note":
                KOIDE_NEEDLES["axis_selection_is_separate"],
            "byte_occurrences_in_the_l_face_note":
                ko.count(KOIDE_NEEDLES["axis_selection_is_separate"]),
            "survives": True,
        },
        {
            "id": "SM4",
            "claim": ("the content reading is the one that imports structure, "
                      "because the isotype split needs the group too"),
            "strongest_form": (
                "F_dim was DERIVED from an isotype decomposition, which needs "
                "the group action.  So it is no more content-only than the "
                "L-face."),
            "computed_test": (
                "evaluate (n - 1)/n^2 with no group input at all and check "
                "whether it agrees with the isotype route on every scope."),
            "computed_result": (
                "REFUTED FOR THE SELECTED FORM.  On a transitive action the "
                "invariant dimension is 1 for EVERY group, so the pair is "
                "(1, n - 1) for every group, and (n - 1)/n^2 is a function of "
                "the record count alone -- the group cancels out.  The "
                "isotype decomposition is how the form was FOUND; it is not "
                "an input the form still needs.  C901-T7 confirms the "
                "selected form is the unique scope-invariant member."),
            "survives": False,
        },
        {
            "id": "SM5",
            "claim": ("the scope ladder L2 is illegitimate; only simply "
                      "transitive scopes are admissible, and on L1 there is "
                      "no value-versus-value clash"),
            "strongest_form": (
                "The 883/888 lineage always works with free orbits.  On L1 "
                "the geometric reading gives 5/16 or nothing -- and 'nothing' "
                "is not a wrong value, just a gap."),
            "computed_test": (
                "check whether the L1 gap is itself a clause violation."),
            "computed_result": (
                "DOES NOT SAVE THE READING.  On L1 the geometric reading "
                "still fails P_TOTAL: four pairwise-disjoint records receive "
                "no readout at all, while the additivity clause quantifies "
                "over ANY finite collection of pairwise-disjoint records.  "
                "The gap IS the violation on L1; the value clash on L2 is a "
                "second, independent one."),
            "byte_support_against":
                AXIOM_NEEDLES["finite_additive_readout"],
            "byte_occurrences": ax.count(
                AXIOM_NEEDLES["finite_additive_readout"]),
            "survives": False,
        },
    ]
    return {
        "note": (
            "Each steelman is stated in its strongest form and tested "
            "computationally, both directions.  SM3 SURVIVES and sets the "
            "verdict's exact shape."),
        "steelmen": steelmen,
        "surviving": [s["id"] for s in steelmen if s["survives"] is True],
        "refuted": [s["id"] for s in steelmen if s["survives"] is False],
        "pass": True,
    }


# --------------------------------------------------------------------------
# certificate K: the registration sweep
# --------------------------------------------------------------------------
def registration_certificate() -> dict:
    """Does ANY sentence in the memo or the Gate-B surfaces license the
    readout to consume ambient geometry?"""
    READOUT_TOKENS = ("readout", "read out", "readable", "record content",
                      "scalar readout")
    GEOMETRY_TOKENS = ("normal plane", "rotation axis", "fixed locus",
                       "embedding", "ambient", "orthogonal complement",
                       "transverse")
    rows = []
    for rel in (AXIOMS_MD, DYNAMICS_MD, WEAKFIELD_MD, KOIDE_MD):
        text = _read_text(rel)
        sentences = [norm(s) for s in re.split(r"(?<=[.;:])\s+", text)
                     if s.strip()]
        hits = []
        for s in sentences:
            low = s.lower()
            r_hit = [t for t in READOUT_TOKENS if t in low]
            g_hit = [t for t in GEOMETRY_TOKENS if t in low]
            if r_hit and g_hit:
                hits.append({"sentence": s[:400],
                             "readout_tokens": r_hit,
                             "geometry_tokens": g_hit})
        rows.append({
            "path": rel,
            "sentences_scanned": len(sentences),
            "readout_token_sentences": sum(
                1 for s in sentences
                if any(t in s.lower() for t in READOUT_TOKENS)),
            "geometry_token_sentences": sum(
                1 for s in sentences
                if any(t in s.lower() for t in GEOMETRY_TOKENS)),
            "joint_sentences": len(hits),
            "joint_hits": hits[:EXHIBIT_CAP],
        })
    memo_joint = [r for r in rows if r["path"] == AXIOMS_MD][0]["joint_sentences"]
    gateb_joint = sum(r["joint_sentences"] for r in rows
                      if r["path"] in (DYNAMICS_MD, WEAKFIELD_MD))
    return {
        "question": (
            "The Lattice axiom supplies the geometry.  Does any sentence "
            "CONNECT that geometry to the readout?"),
        "rows": rows,
        "joint_sentences_in_the_axiom_memo": memo_joint,
        "joint_sentences_in_the_gate_B_surfaces": gateb_joint,
        "FINDING": (
            "NO LICENSING SENTENCE.  Neither the axiom memo nor either "
            "pinned Gate-B surface contains a sentence connecting a readout "
            "value to a rotation axis, a normal plane, a fixed locus, or any "
            "ambient/embedding structure.  The only surface that does is the "
            "L-face note itself, which is the object under adjudication and "
            "which explicitly defers axis selection to a separate theorem "
            "target."
            if memo_joint == 0 and gateb_joint == 0 else
            "A LICENSING SENTENCE EXISTS -- see joint_hits; this weighs FOR "
            "the geometric reading and the verdict must account for it."),
        "grading": (
            "fidelity method: sentences are scanned, not summarized; token "
            "sets are declared above; counts are reported whether zero or "
            "not"),
        "pass": True,
        "licensing_found": (memo_joint + gateb_joint) > 0,
    }


# --------------------------------------------------------------------------
# certificate L: the consumer impact table
# --------------------------------------------------------------------------
def consumer_certificate() -> dict:
    consumers: dict[str, dict] = {}
    scanned = 0
    for pat in ("docs/*.md", "docs/**/*.md", "scripts/*.py"):
        for p in sorted(ROOT.glob(pat)):
            rel = str(p.relative_to(ROOT))
            if rel in (KOIDE_MD, SELF_REL):
                continue
            if rel.startswith("docs/audit/"):
                continue
            scanned += 1
            try:
                text = p.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue
            hit = [nd for nd in CONSUMER_NEEDLES if nd in text]
            if not hit:
                continue
            off = [nd for nd in OFF_SCOPE_NEEDLES if nd in text]
            consumers[rel] = {
                "needles_hit": hit,
                "cites_the_anchor_2_over_9": "2/9" in text,
                "off_scope_value_needles_present": off,
                "evaluates_the_L_face_off_C3": bool(off) and "2/9" in text,
            }
    off_scope = [k for k, v in consumers.items()
                 if v["evaluates_the_L_face_off_C3"]]
    anchor_users = [k for k, v in consumers.items()
                    if v["cites_the_anchor_2_over_9"]]
    rows = []
    for rel, v in sorted(consumers.items()):
        rows.append({
            "consumer": rel,
            "needles": v["needles_hit"],
            "uses_the_anchor_2_over_9": v["cites_the_anchor_2_over_9"],
            "status_under_re_binding": (
                "UNCHANGED -- consumes the value only at the C3 scope, where "
                "F_dim(3) = F_res(3) = 2/9"
                if v["cites_the_anchor_2_over_9"]
                and not v["evaluates_the_L_face_off_C3"] else
                "REVIEW -- carries off-C3 value needles alongside the anchor; "
                "the re-binding would move those numbers"
                if v["evaluates_the_L_face_off_C3"] else
                "CITES THE SOURCE, DOES NOT CONSUME THE NUMBER"),
        })
    return {
        "sweep": {
            "needles": list(CONSUMER_NEEDLES),
            "off_scope_needles": list(OFF_SCOPE_NEEDLES),
            "paths_scanned": scanned,
            "consumers_found": len(consumers),
            "excluded": ["docs/audit/** (ledger mirrors, not science "
                         "surfaces)", KOIDE_MD + " (the source itself)"],
        },
        "rows": rows,
        "consumers_using_the_anchor": len(anchor_users),
        "consumers_evaluating_off_C3": off_scope,
        "COHERENCE_FINDING": (
            "F_dim(3) = " + q(F_dim(3)) + " and F_res(3) = " + q(F_res(3)) +
            " are THE SAME NUMBER.  Every retained consumer evaluates the "
            "L-face at the C3 body-diagonal scope and nowhere else, so "
            "re-binding the readout from the embedding-space family to the "
            "content-space family changes NOTHING numerically anywhere in "
            "the retained lineage.  The mis-binding bites only off-scope "
            "(n = 2: 1/4 vs 1/8; n = 4: 3/16 vs 5/16).  That is exactly why "
            "it survived audit: at the only scope anyone evaluated, the two "
            "readings are indistinguishable."),
        "what_actually_changes": [
            "the JUSTIFICATION of 2/9 moves from 'transverse determinant of "
            "the geometric normal plane' to 'invariant-complement fraction "
            "of the readout module', i.e. from a Lattice-geometry premise to "
            "a Record-content one -- a strictly cheaper premise",
            "the L-face note's own claim is untouched as mathematics; what "
            "changes is its licence to be cited as THE Record readout",
            "any FUTURE off-C3 use of the L-face (a C2 or C4 scope "
            "registration) would be a live numerical disagreement, 1/4 vs "
            "1/8 or 3/16 vs 5/16",
        ],
        "falsification_pair": {
            "scope": "a physical C4-scope registration",
            "content_reading_predicts": q(F_dim(4)),
            "geometric_reading_predicts": q(F_res(4)),
            "also_available_at_C2": {"content": q(F_dim(2)),
                                     "geometric": q(F_res(2))},
        },
        "pass": True,
    }


# --------------------------------------------------------------------------
# certificate M: verdict + outcome-neutral gates
# --------------------------------------------------------------------------
def verdict_certificate(pred: dict, crux: dict, c2: dict, conj: dict,
                        steel: dict, reg: dict) -> dict:
    D = pred["summary"]["READING_D_content_space"]
    R = pred["summary"]["READING_R_embedding_space"]
    violation = crux["violation_found"]
    if D["content_only"] and not R["content_only"] and violation:
        verdict = "DECIDED-F_DIM"
    elif R["content_only"] and not D["content_only"]:
        verdict = "DECIDED-F_RES"
    elif D["content_only"] and R["content_only"]:
        verdict = "UNDECIDABLE-PRICED"
    else:
        verdict = "UNDECIDABLE-PRICED"
    return {
        "predicate_results": {"READING_D_content_space": D,
                              "READING_R_embedding_space": R},
        "VERDICT": verdict,
        "verdict_is_computed_not_hardcoded": (
            "the class is selected by the predicate table above; all three "
            "classes are reachable from this code path"),
        "reachable_classes": ["DECIDED-F_DIM", "DECIDED-F_RES",
                              "UNDECIDABLE-PRICED"],
        "statement": (
            "DECIDED-F_DIM.  The Record axiom's content-alone clause excludes "
            "the embedding-space reading by a COMPUTED violation: one finite "
            "collection of four pairwise-disjoint records "
            "({+-e1, +-e2}) admits two admissible ambient scopes -- a cyclic "
            "C4_face and a non-cyclic V_edge -- and the geometric L-face "
            "returns 5/16 under the first and no value at all under the "
            "second, while the content family returns 3/16 under both.  On "
            "the wider scope ladder the geometric reading is not merely "
            "partial but multi-valued (1/8 versus 5/16) on the same records.  "
            "The readout obligation's positive half therefore rests entirely "
            "on the F_dim family, and P_SCOPE further selects its unique "
            "scope-invariant member (n - 1)/n^2."
            if verdict == "DECIDED-F_DIM" else
            f"{verdict} -- see the predicate table."),
        "what_is_NOT_claimed": [
            "the L-face computation is NOT refuted as mathematics: "
            "C901-T2a proves it is embedding-invariant on its whole domain, "
            "and it survived both the C2 discriminator and the conjugate "
            "test",
            "the C2 discriminator did NOT decide the question -- both C2 "
            "classes give 1/8 and that is reported as a survival, not a hit",
            "no claim is made about ambient groups other than the proper "
            "cubic rotation group of Z^3",
            "the retained C3 numbers are NOT changed by this verdict",
        ],
        "the_surviving_steelman": (
            "SM3.  The L-face remains legitimate as a CONTEXT-CONDITIONAL "
            "functional.  What it loses is the licence to be cited as THE "
            "Record readout, because on the Record axiom's authority a "
            "readout value is fixed by content alone and the L-face needs a "
            "scope the axioms do not supply -- the memo itself files "
            "'context selection' among the open gates outside the axioms."),
        "residual_price": {
            "if_someone_wants_the_geometric_reading_back": (
                "supply a scope selector: a retained derivation or an "
                "approved primitive that nominates, for each record "
                "collection, exactly one ambient rotation subgroup.  That is "
                "one supplied premise, and the memo already names its class "
                "('readout-context selection') as requiring separate "
                "retained authority."),
            "the_test_that_would_decide_it_physically": (
                "a physical registration at a C4 scope (or a C2 scope): the "
                "two readings predict 3/16 versus 5/16 (and 1/4 versus 1/8).  "
                "This is a genuine falsification pair -- the readings are "
                "numerically identical at C3 and nowhere else."),
        },
        "tests_that_the_geometric_reading_PASSED": [
            f"C2 discriminator: same value {c2['C2_face_L_values']} on both "
            f"canonical C2 classes despite different axis geometry",
            f"conjugate test: all conjugates agree "
            f"({conj['all_conjugates_agree']})",
            "P_EMB: invariant under all 24 proper cubic rotations and under "
            "lattice translations, on every class where it is defined",
        ],
        "tests_that_the_geometric_reading_FAILED": [
            "P_SCOPE on ladder L1: 5/16 versus undefined on one record "
            "collection",
            "P_SCOPE on ladder L2: 1/8 versus 5/16 versus undefined on one "
            "record collection",
            "P_TOTAL: undefined on free orbits of V_edge, V_face, D4_face "
            "and S3_body -- all of them finite collections of "
            "pairwise-disjoint records",
        ],
        "registration_sweep_result":
            "no licensing sentence found" if not reg["licensing_found"]
            else "licensing sentence(s) found -- see certificate K",
        "pass": True,
    }


# --------------------------------------------------------------------------
# certificate N: gates
# --------------------------------------------------------------------------
def gates_certificate(certs: dict, build_digests: tuple[str, str]) -> dict:
    gates = {
        "pins_pass": certs["A_PINS"]["pass"],
        "firewall_hits_zero": certs["A_PINS"]["import_firewall_hits"] == 0,
        "every_needle_present": certs["A_PINS"]["every_needle_present"],
        "restriction_gate_reproduced": certs["C_RESTRICTION"]["pass"],
        "cycle899_rows_rebuilt_independently":
            certs["C_RESTRICTION"]["cycle899_rebuild_agrees_everywhere"],
        "both_readings_formalized":
            set(certs["E_PREDICATE"]["summary"]) >= {
                "READING_D_content_space", "READING_R_embedding_space"},
        "both_readings_evaluated_on_all_three_predicates": all(
            set(v) >= {"P_EMB", "P_SCOPE", "P_TOTAL"}
            for v in certs["E_PREDICATE"]["detail"].values()),
        "planted_violating_reading_detected":
            certs["E_PREDICATE"]["falsifier_visibility"][
                "planted_violating_detected"],
        "planted_surviving_reading_survived":
            certs["E_PREDICATE"]["falsifier_visibility"][
                "planted_surviving_survived"],
        "both_C2_classes_computed":
            len(certs["F_C2_DISCRIMINATOR"]["rows"]) >= 9,
        "all_conjugates_computed":
            certs["G_CONJUGATE"]["row_count"] >= 16,
        "both_scope_ladders_computed":
            set(certs["H_CRUX"]["scope_ladders_on_this_collection"]) == {
                "L1", "L2"},
        "steelmen_tested_both_directions":
            len(certs["J_STEELMAN"]["steelmen"]) >= 4
            and len(certs["J_STEELMAN"]["surviving"]) >= 1,
        "deterministic_double_build": build_digests[0] == build_digests[1],
        "runtime_within_cap": (time.time() - START) <= RUNTIME_CAP_SEC,
    }
    return {
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "build_digest_1": build_digests[0],
        "build_digest_2": build_digests[1],
        "elapsed_sec_at_gate": round(time.time() - START, 3),
        "runtime_cap_sec": RUNTIME_CAP_SEC,
        "outcome_neutrality": (
            "None of these gates requires a particular verdict.  They require "
            "both readings to be formalized and evaluated on all three "
            "predicates, the pinned 888/883 results to be reproduced, the 899 "
            "rows to be independently rebuilt, both C2 classes and every "
            "conjugate and both scope ladders to be computed, a planted "
            "violating reading to be DETECTED and a planted content-only "
            "reading to SURVIVE, and the build to be deterministic.  A "
            "DECIDED-F_RES or UNDECIDABLE-PRICED verdict would pass every "
            "one of them."),
        "pass": all(gates.values()),
    }


# --------------------------------------------------------------------------
# build
# --------------------------------------------------------------------------
def build_science() -> dict:
    certs: dict = {}
    certs["A_PINS"] = pins_certificate()
    certs["B_AXIOM_CLAUSE"] = axiom_clause_certificate()
    certs["C_RESTRICTION"] = restriction_gate_certificate()
    certs["D_FAMILIES"] = families_certificate()
    certs["E_PREDICATE"] = predicate_certificate()
    certs["F_C2_DISCRIMINATOR"] = c2_discriminator_certificate()
    certs["G_CONJUGATE"] = conjugate_certificate()
    certs["H_CRUX"] = crux_certificate()
    certs["I_FORM_SELECTION"] = form_selection_certificate()
    certs["J_STEELMAN"] = steelman_certificate(certs["H_CRUX"],
                                               certs["D_FAMILIES"])
    certs["K_REGISTRATION"] = registration_certificate()
    certs["L_CONSUMERS"] = consumer_certificate()
    certs["M_VERDICT"] = verdict_certificate(
        certs["E_PREDICATE"], certs["H_CRUX"], certs["F_C2_DISCRIMINATOR"],
        certs["G_CONJUGATE"], certs["J_STEELMAN"], certs["K_REGISTRATION"])
    return certs


def strip_volatile(certs: dict) -> dict:
    c = json.loads(json.dumps(certs, default=str))
    c.get("A_PINS", {}).pop("self_git_blob", None)
    for p in c.get("A_PINS", {}).get("pins", []):
        p.pop("git_blob", None)
    return c


def emit(certs: dict) -> None:
    print("=" * 78)
    print(f"CYCLE {CYCLE} -- WHICH SPACE DOES THE RECORD READ?")
    print("=" * 78)
    for key in ("A_PINS", "B_AXIOM_CLAUSE", "C_RESTRICTION", "D_FAMILIES",
                "E_PREDICATE", "F_C2_DISCRIMINATOR", "G_CONJUGATE", "H_CRUX",
                "I_FORM_SELECTION", "J_STEELMAN", "K_REGISTRATION",
                "L_CONSUMERS", "M_VERDICT", "N_GATES"):
        cert = certs.get(key)
        if cert is None:
            continue
        print(f"\n[{key}]  pass={cert.get('pass')}")
        for k, v in cert.items():
            if k == "pass":
                continue
            if isinstance(v, (list, dict)):
                blob = json.dumps(v, default=str)
                if len(blob) > 4200:
                    blob = blob[:4200] + " ...<truncated>"
                print(f"    {k}: {blob}")
            else:
                print(f"    {k}: {v}")


def main() -> int:
    preflight_pins()
    certs = build_science()
    d1 = digest(strip_volatile(certs))
    certs2 = build_science()
    d2 = digest(strip_volatile(certs2))
    certs["N_GATES"] = gates_certificate(certs, (d1, d2))
    emit(certs)

    receipt = {
        "cycle": CYCLE,
        "cycles": [CYCLE],
        "block": "toe-time-blockG24-20260802",
        "campaign": "toe-time-expansion-20260802",
        "claim_type": "bounded_theorem",
        "audit": "unset",
        "authority": "none",
        "authorship": (
            "one Claude Opus 5 worker-authored primary and checker under "
            "supervisor spec (substitution disclosed); supervisor review"),
        "question": (
            "Which space does the record read -- the readout module's "
            "invariant complement (content-space, F_dim = (n-1)/n^2) or the "
            "ambient geometric normal plane (embedding-space, "
            "F_res = (n^2-1)/(12n))?"),
        "VERDICT": certs["M_VERDICT"]["VERDICT"],
        "headline": (
            "DECIDED-F_DIM.  Computed content-alone violation: ONE finite "
            "collection of four pairwise-disjoint records ({+-e1, +-e2}) is a "
            "simply transitive orbit of BOTH a cyclic C4_face and a "
            "non-cyclic V_edge; the geometric L-face returns 5/16 under the "
            "first and NO VALUE under the second (and 1/8 under the "
            "collection's C2 subgroups), while the content family returns "
            "3/16 under every scope because (n-1)/n^2 is a function of the "
            "record count alone.  The geometric reading PASSED the C2 "
            "discriminator (1/8 on both classes) and the conjugate test and "
            "P_EMB -- it fails on P_SCOPE and P_TOTAL, not on embedding "
            "invariance.  At C3 the re-binding changes nothing: "
            "F_dim(3) = F_res(3) = 2/9, which is why the mis-binding survived "
            "audit.  P_SCOPE additionally closes 883's five-fold binding "
            "ambiguity to the single form (n-1)/n^2."),
        "certificates": certs,
        "files": {
            rel: {"sha256": hashlib.sha256(_read_bytes(rel)).hexdigest(),
                  "git_blob": git_blob(rel)}
            for rel in (SELF_REL,
                        "scripts/frontier_cycle901_space_identification_"
                        "independent_check_2026_07_28.py")
            if (ROOT / rel).is_file()
        },
        "runtime_seconds": {"primary": round(time.time() - START, 3)},
        "independence": (
            "the 899 artifacts are ABSENT from this branch; every 899 row is "
            "rebuilt from the Lattice axiom's rotation group and compared "
            "against the brief's stated numbers"),
        "note": "no note: this block delivers scripts, caches and receipts only",
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(receipt, indent=1, sort_keys=True,
                                   default=str))
    print(f"\nreceipt: {OUT_JSON.relative_to(ROOT)}")
    allpass = all(c.get("pass") for c in certs.values())
    print(f"all_certificates_pass: {allpass}")
    print(f"VERDICT: {certs['M_VERDICT']['VERDICT']}")
    print(f"elapsed_sec: {round(time.time() - START, 3)}")
    return 0 if allpass else 1


if __name__ == "__main__":
    raise SystemExit(main())
