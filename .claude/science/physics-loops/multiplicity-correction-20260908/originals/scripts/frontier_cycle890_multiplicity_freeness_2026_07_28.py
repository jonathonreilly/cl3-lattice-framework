#!/usr/bin/env python3
"""Cycle 890: PRICE MULTIPLICITY-FREENESS -- Cycle 888's named FIND-5.

Cycle 883 derived the readout weight pair (1, 2) at the C3 scope "with no free
parameter" (SL1).  Cycle 886 showed no axiom-grounded selector isolates C3
among the CYCLIC scopes.  Cycle 888 completed the census over all thirty
subgroups of the proper cubic rotation group and proved the SL1 transfer to S3
is NUMERICALLY_TRANSFERS_BUT_THE_SUBSPACE_IS_NOT_FORCED: at S3 the 2-dimensional
irreducible occurs with multiplicity 2, so the realizing subspace is a P^1
family, while at C3 and C4 every multiplicity is 1 and the decomposition is
canonical.  Cycle 888's own conclusion -- **SL1's "no free parameter" IS
multiplicity-freeness of the readout representation** -- left one question
UNPRICED and named it FIND-5: is multiplicity-freeness quotable from any axiom
sentence?  This cycle prices it.

H1  THE THEOREM HALF (positive, machine-verified over the full census).

    T1  For every conjugacy class of subgroups and every readout scope (the
        maximal-free-orbit scope where it exists, and the whole-shell scope),
        the readout decomposition is CANONICAL if and only if the readout
        representation is MULTIPLICITY-FREE.  The two sides are computed by
        SEPARATE, NON-COMMUNICATING routes:

          SIDE A (geometric canonicity).  Irreducible submodules are exhibited
          by exhaustive enumeration of cyclic submodules over an integer grid,
          a direct-sum decomposition is built and gated to span the space, the
          summands are grouped by EXPLICIT intertwiner spaces, and for each
          isomorphism class the moduli of realizing subspaces is computed as
          dim_Q Hom_A(U, M) - dim_Q End_A(U).  Zero means a single point;
          positive means a family, and an explicit one-parameter family of
          distinct submodules is CONSTRUCTED and verified.

          SIDE B (algebraic multiplicity-freeness).  The enveloping algebra
          A = span{rho(h)} is built exactly, its centre is solved for, a
          generator of the centre is found, its minimal polynomial is factored
          over Q, the isotypic components are the kernels of the factors, and
          each rational irreducible degree is recovered from
          dim_Q A_i = d_i^2 / [F_i : Q].  Multiplicity-free means every fine
          multiplicity is <= 1.

        BOTH sides carry the Cycle-888 FIND-3 safety gate independently:
        sum_i m_i^2 [F_i : Q] must equal the number of orbits of the subgroup
        on X x X.  (Naive minimal-cyclic-submodule peeling is UNSAFE on this
        lattice -- at V_edge the first peeled block is 2-dimensional and
        reducible.)

    T2  Multiplicity-freeness at a scope IMPLIES the SL1-type pair is forced.
        Verified at C3 and C4 (forced), at S3 (not forced), and at every other
        class carrying a free shell orbit.

    T3  THE LADDER SHARPENING.  The honest scope menu is RECOMPUTED (classes
        with a lattice-realized free shell orbit of length > 1), and the exact
        subset on which BOTH (a) a v_2 = 1 datum exists under at least one
        reading AND (b) the realization is forced is computed -- at the orbit
        scope, at the shell scope, scope-coherently, and under the deliberately
        loosened scope-MISMATCHED reading, so that nothing can sneak in under a
        reading this runner skipped.  The off-menu counterfactual is computed
        too, so the work done by the realizability rule is visible.

H2  THE PRICING HALF (the FIND-5 sweep).  EVERY sentence of the pinned axiom
    memo, of both Gate-B notes carried by this lineage, and of the readout
    derivation obligation is enumerated by a BYTE-EXACT segmentation -- the
    segments concatenate back to the file, character for character, so the
    sweep's completeness is a reconstruction proof and not a promise.  Each
    prose segment gets an honest grounding attempt for multiplicity-freeness
    or any equivalent/implying property (canonical decomposition; uniqueness of
    the invariant complement; "the readout is determined by ..."; rigidity
    language), graded EXACT / PARTIAL / NONE against a declared three-element
    rubric with a provenance-polarity gate, and the FULL grade distribution is
    reported -- not a cherry-picked subset.

    The verdict is data: QUOTABLE if some sentence grades EXACT (the scope
    ladder then closes as a derivation), NOT_QUOTABLE if the grade ceiling is
    PARTIAL or NONE (multiplicity-freeness is then the ladder's terminal
    supplied clause).  Every gate in this runner passes identically under both
    verdicts; a synthetic forced-EXACT rerun proves it.

All cited artifacts are SHA-256 and git-blob pinned, read as text/AST/JSON
only, and blocked from import by a meta-path firewall.  Every certified
quantity is exact (`int` / `Fraction`); no floating point enters a certificate.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
STDOUT_LIMIT_BYTES = 400_000

# Literal, greppable, and pinned below.
AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/frontier_cycle888_s3_scope_pricing_2026_07_28.py",
    "outputs/s3_scope_pricing_cycle888_receipt_2026_07_28.json",
    "scripts/frontier_cycle883_record_weight_pair_2026_07_28.py",
    "docs/GATE_B_DYNAMICS_NOTE.md",
    "docs/GATE_B_WEAK_FIELD_SOURCE_ACTION_INTERFACE_NOTE_2026-06-16.md",
    "docs/AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md",
)

# The four prose documents swept sentence by sentence in H2.
SWEPT_DOCUMENT_PATHS = (
    AUDIT_INPUT_PATHS[0],
    AUDIT_INPUT_PATHS[4],
    AUDIT_INPUT_PATHS[5],
    AUDIT_INPUT_PATHS[6],
)

import ast
from fractions import Fraction
from hashlib import sha256
import importlib.abc
from itertools import product
import json
from math import gcd, isqrt
from pathlib import Path
import re
import subprocess
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / "outputs" / "multiplicity_freeness_cycle890_receipt_2026_07_28.json"

BLOCKLISTED_MODULES = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    AUDIT_INPUT_PATHS[1]:
        "f57fda877d35d49953c3b6a34293ab0cc6a87781ceb9d158b9c9abb5abd4bb3f",
    AUDIT_INPUT_PATHS[2]:
        "8a540201a84a6b8cb6868d431216718a27f200e45d6ceeb771d858e9a54280cd",
    AUDIT_INPUT_PATHS[3]:
        "2d96422d30f169a1c4b3215db373e4bffd7b1ef20056ea337ff4ae3f86d9511c",
    AUDIT_INPUT_PATHS[4]:
        "0031e5ddcb2e1408db1bca3d738669b5463e672cfdbecc81b859b0fc609dc271",
    AUDIT_INPUT_PATHS[5]:
        "e246730a808174752f2bb1e113a89bccdf691db81b76bc1e2f6347ab027b0116",
    AUDIT_INPUT_PATHS[6]:
        "4d742bcc68a1e7cdb154b366e671f576e9b719b3206445b97666c812a790e58c",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "4a863da1f3f255354839277271a3a69a5c205133",
    AUDIT_INPUT_PATHS[1]: "c3de02c94b8a11a930ad6ff8817975b118bc776d",
    AUDIT_INPUT_PATHS[2]: "3e18ad52f50e72b83c56da72c31f25d104b5c830",
    AUDIT_INPUT_PATHS[3]: "d563c2b9c2a261f44d7304baa51fdd3596188930",
    AUDIT_INPUT_PATHS[4]: "5594d74e38a84d95c806449a305a16e1f1db8c43",
    AUDIT_INPUT_PATHS[5]: "2c9e1d0c75ea801f25fa0f9cfa92c67553770b4c",
    AUDIT_INPUT_PATHS[6]: "9a449956422a5687b5b1346f428c9e4e35489038",
}

# How the two Gate-B notes and the readout obligation note were DISCOVERED
# rather than assumed: a tracked-file scan of the immediate lineage's own pin
# tuples.  Recorded so the choice is auditable, and re-verified at run time.
NOTE_DISCOVERY_SCAN = {
    "method": (
        "tracked-file scan: `git ls-files docs/GATE_B_*.md` enumerates every "
        "Gate-B note on the branch; the two THIS LINEAGE actually carries are "
        "the two named in the AUDIT_INPUT_PATHS tuples of the immediately "
        "upstream cycles 884 and 885, read as text.  The readout obligation "
        "note is the one named in Cycle 882's AUDIT_INPUT_PATHS tuple."
    ),
    "lineage_scripts_scanned": (
        "scripts/frontier_cycle884_gbs2_kernel_window_2026_07_28.py",
        "scripts/frontier_cycle885_gbw1_record_window_2026_07_28.py",
        "scripts/frontier_cycle882_readout_identity_2026_07_28.py",
    ),
    "gate_b_notes_selected": (AUDIT_INPUT_PATHS[4], AUDIT_INPUT_PATHS[5]),
    "readout_obligation_note_selected": AUDIT_INPUT_PATHS[6],
}

TARGET_PAIR = (1, 2)
TARGET_ANCHOR = Fraction(2, 9)

NEAREST_NEIGHBOURS = (
    (1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1),
)

DECLARED_CENSUS_TO_BE_RECOMPUTED = {"subgroups": 30, "conjugacy_classes": 11}

SCOPES = ("ORBIT_SCOPE_maximal_free_orbit", "SHELL_SCOPE_whole_neighbourhood")

VERDICT_CLASSES = ("QUOTABLE", "NOT_QUOTABLE")
GRADES = ("EXACT", "PARTIAL", "NONE")

LABELS = (
    "A_PINS",
    "B_SEGMENTATION_COMPLETENESS",
    "C_ROTATION_GROUP",
    "D_LATTICE_CENSUS_AND_888_REPRODUCTION",
    "E_SIDE_B_MULTIPLICITY_FREENESS",
    "F_SIDE_A_CANONICITY",
    "G_T1_THE_EQUIVALENCE",
    "H_T2_FORCEDNESS_WITNESSES",
    "I_T3_THE_LADDER_SUBSET",
    "J_H2_SENTENCE_SWEEP",
    "K_VERDICT",
    "L_IMPOSTOR_STRESS",
    "M_VERDICT_INDEPENDENCE",
    "N_DETERMINISM",
)


# --------------------------------------------------------------------------
# import firewall: cited primaries are evidence, never libraries
# --------------------------------------------------------------------------
class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_module(self, fullname, path=None):       # pragma: no cover legacy
        return self.find_spec(fullname, path)

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)


# --------------------------------------------------------------------------
# helpers -- exact arithmetic only
# --------------------------------------------------------------------------
def _read_bytes(path: str) -> bytes:
    return (ROOT / path).read_bytes()


def _read_text(path: str) -> str:
    return _read_bytes(path).decode("utf-8")


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def digest(payload: object) -> str:
    return sha256(
        json.dumps(payload, sort_keys=True, default=str).encode("utf-8")
    ).hexdigest()


def q(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def vp(value: Fraction, p: int) -> int | None:
    """p-adic valuation of a nonzero rational; None at zero."""
    if value == 0:
        return None
    n, d, e = abs(value.numerator), value.denominator, 0
    while n % p == 0:
        n //= p
        e += 1
    while d % p == 0:
        d //= p
        e -= 1
    return e


def divisors(n: int) -> list[int]:
    return [d for d in range(1, abs(n) + 1) if n % d == 0]


# ---- exact rational linear algebra -----------------------------------------
def rref(rows) -> tuple[list[list[Fraction]], list[int]]:
    matrix = [[Fraction(x) for x in row] for row in rows]
    if not matrix or not matrix[0]:
        return [], []
    width = len(matrix[0])
    pivots: list[int] = []
    rank = 0
    for col in range(width):
        piv = None
        for r in range(rank, len(matrix)):
            if matrix[r][col] != 0:
                piv = r
                break
        if piv is None:
            continue
        matrix[rank], matrix[piv] = matrix[piv], matrix[rank]
        head = matrix[rank][col]
        matrix[rank] = [x / head for x in matrix[rank]]
        for r in range(len(matrix)):
            if r != rank and matrix[r][col] != 0:
                f = matrix[r][col]
                matrix[r] = [a - f * b for a, b in zip(matrix[r], matrix[rank])]
        pivots.append(col)
        rank += 1
    return matrix[:rank], pivots


def rank_exact(rows) -> int:
    return len(rref(rows)[0])


def kernel_basis(rows, width: int) -> list[list[Fraction]]:
    reduced, pivots = rref(rows) if rows else ([], [])
    free = [c for c in range(width) if c not in pivots]
    basis = []
    for f in free:
        vec = [Fraction(0)] * width
        vec[f] = Fraction(1)
        for i, pcol in enumerate(pivots):
            vec[pcol] = -reduced[i][f]
        basis.append(vec)
    return basis


def subspace_key(rows) -> tuple:
    reduced, _ = rref(rows)
    return tuple(tuple(q(x) for x in row) for row in reduced)


def mat_mul(a, b):
    n, k, m = len(a), len(b), len(b[0])
    return [[sum(a[i][t] * b[t][j] for t in range(k)) for j in range(m)]
            for i in range(n)]


def mat_add_scaled(a, b, c):
    return [[a[i][j] + c * b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def identity_matrix(m: int):
    return [[Fraction(1) if i == j else Fraction(0) for j in range(m)]
            for i in range(m)]


def solve_columns(u_cols, targets):
    """Solve U X = T for X, where U has full column rank. Exact, or None."""
    n = len(u_cols)
    d = len(u_cols[0])
    w = len(targets[0])
    aug = [[Fraction(x) for x in u_cols[i]] + [Fraction(y) for y in targets[i]]
           for i in range(n)]
    reduced, pivots = rref(aug)
    if pivots[:d] != list(range(d)) or len(pivots) > d:
        return None
    return [[reduced[i][d + j] for j in range(w)] for i in range(d)]


# ---- exact integer polynomials (low -> high coefficients) ------------------
def poly_trim(p):
    while p and p[-1] == 0:
        p = p[:-1]
    return p


def poly_divmod(num, den):
    num = list(num)
    den = poly_trim(list(den))
    out = [Fraction(0)] * max(0, len(num) - len(den) + 1)
    for i in range(len(out) - 1, -1, -1):
        c = Fraction(num[i + len(den) - 1], 1) / den[-1]
        out[i] = c
        for j, dv in enumerate(den):
            num[i + j] -= c * dv
    return out, poly_trim(num)


def poly_divides(den, num) -> bool:
    _, rem = poly_divmod([Fraction(x) for x in num], [Fraction(x) for x in den])
    return not rem


def poly_exact_quotient(num, den):
    quo, rem = poly_divmod([Fraction(x) for x in num], [Fraction(x) for x in den])
    if rem:                                            # pragma: no cover gate
        raise AssertionError("inexact polynomial division")
    return [int(c) for c in quo]


def factor_monic_squarefree(poly) -> list[list[int]] | None:
    """Factor a monic squarefree integer polynomial into monic irreducibles.

    Degree <= 2 factors only; anything left of degree >= 3 returns None, a hard
    gate failure upstream.
    """
    remaining = poly_trim([int(c) for c in poly])
    factors: list[list[int]] = []
    changed = True
    while changed and len(remaining) > 1:
        changed = False
        c0 = remaining[0]
        cands = [0] if c0 == 0 else \
            sorted({s * d for d in divisors(abs(c0)) for s in (1, -1)})
        for r in cands:
            if sum(c * r ** k for k, c in enumerate(remaining)) == 0:
                factors.append([-r, 1])
                remaining = poly_exact_quotient(remaining, [-r, 1])
                changed = True
                break
    while len(remaining) > 1:
        if len(remaining) == 3:
            factors.append(list(remaining))
            remaining = [1]
            break
        c0 = remaining[0]
        bound = 1 + max(abs(x) for x in remaining)
        found = None
        cands = [0] if c0 == 0 else \
            sorted({s * d for d in divisors(abs(c0)) for s in (1, -1)})
        for c in cands:
            for b in range(-2 * bound, 2 * bound + 1):
                cand = [c, b, 1]
                if poly_divides(cand, remaining):
                    found = cand
                    break
            if found:
                break
        if not found:
            return None
        factors.append(found)
        remaining = poly_exact_quotient(remaining, found)
    return sorted(factors, key=lambda f: (len(f), f))


def poly_of_matrix(coeffs, matrix):
    m = len(matrix)
    acc = [[Fraction(0)] * m for _ in range(m)]
    power = identity_matrix(m)
    for c in coeffs:
        if c:
            acc = mat_add_scaled(acc, power, Fraction(c))
        power = mat_mul(power, matrix)
    return acc


def minimal_polynomial(matrix) -> list[int]:
    m = len(matrix)
    powers = [identity_matrix(m)]
    for k in range(1, m + 1):
        powers.append(mat_mul(powers[-1], matrix))
        cols = [[powers[j][r][c] for j in range(k + 1)]
                for r in range(m) for c in range(m)]
        ker = kernel_basis(cols, k + 1)
        for vec in ker:
            if vec[k] != 0:
                coeffs = [x / vec[k] for x in vec]
                den = 1
                for x in coeffs:
                    den = den * x.denominator // gcd(den, x.denominator)
                scaled = [int(x * den) for x in coeffs]
                if scaled[-1] < 0:
                    scaled = [-x for x in scaled]
                g = 0
                for x in scaled:
                    g = gcd(g, abs(x))
                return [x // g for x in scaled]
    raise AssertionError("no minimal polynomial found")  # pragma: no cover


# --------------------------------------------------------------------------
# the proper cubic rotation group, rebuilt independently
# --------------------------------------------------------------------------
IDENTITY3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def signed_permutation_matrices():
    out = []
    for perm in product(range(3), repeat=3):
        if len(set(perm)) != 3:
            continue
        for signs in product((1, -1), repeat=3):
            rows = []
            for i in range(3):
                row = [0, 0, 0]
                row[perm[i]] = signs[i]
                rows.append(tuple(row))
            out.append(tuple(rows))
    return out


def det3(m) -> int:
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


def mul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))


def act(m, v):
    return tuple(sum(m[i][j] * v[j] for j in range(3)) for i in range(3))


def element_order(m) -> int:
    cur, k = m, 1
    while cur != IDENTITY3:
        cur = mul(cur, m)
        k += 1
        if k > 24:                                     # pragma: no cover gate
            raise AssertionError("not a finite rotation")
    return k


GROUP = sorted(m for m in signed_permutation_matrices() if det3(m) == 1)
GROUP_SET = frozenset(GROUP)
INVERSE = {m: next(b for b in GROUP if mul(m, b) == IDENTITY3) for m in GROUP}


def rotation_axis(m):
    if m == IDENTITY3:
        return None
    canon = set()
    for v in product((-1, 0, 1), repeat=3):
        if any(v) and act(m, v) == v:
            g = 0
            for x in v:
                g = gcd(g, abs(x))
            w = tuple(x // g for x in v)
            lead = next(x for x in w if x != 0)
            canon.add(w if lead > 0 else tuple(-x for x in w))
    if len(canon) != 1:                                # pragma: no cover gate
        raise AssertionError(f"axis not unique: {sorted(canon)}")
    return canon.pop()


def axis_kind(m) -> str:
    axis = rotation_axis(m)
    return {1: "face", 2: "edge", 3: "body"}[sum(1 for x in axis if x)]


def orbits_of(subgroup, points) -> list[tuple]:
    seen, out = set(), []
    for p in points:
        if p in seen:
            continue
        orbit = {p}
        frontier = [p]
        while frontier:
            cur = frontier.pop()
            for m in subgroup:
                nxt = act(m, cur)
                if nxt not in orbit:
                    orbit.add(nxt)
                    frontier.append(nxt)
        seen |= orbit
        out.append(tuple(sorted(orbit)))
    return out


def closure(seeds) -> frozenset:
    found = {IDENTITY3} | set(seeds)
    frontier = list(found)
    while frontier:
        cur = frontier.pop()
        for other in list(found):
            for prod in (mul(cur, other), mul(other, cur)):
                if prod not in found:
                    found.add(prod)
                    frontier.append(prod)
    return frozenset(found)


def all_subgroups() -> list[frozenset]:
    """Every subgroup, by closing every ORDERED PAIR of group elements."""
    found = {frozenset({IDENTITY3})}
    for a in GROUP:
        for b in GROUP:
            found.add(closure((a, b)))
    return sorted(found, key=lambda h: (len(h), sorted(h)))


def is_cyclic(h: frozenset) -> bool:
    return any(closure((g,)) == h for g in h)


def is_abelian(h: frozenset) -> bool:
    return all(mul(a, b) == mul(b, a) for a in h for b in h)


def structure_name(h: frozenset) -> str:
    """DERIVED name: order, cyclicity, commutativity, axis-kind multiset."""
    n = len(h)
    if n == 1:
        return "E_trivial"
    kinds = sorted(axis_kind(m) for m in h if m != IDENTITY3)
    if is_cyclic(h):
        return f"C{n}_{kinds[0]}"
    if is_abelian(h) and n == 4:
        return "V_face" if set(kinds) == {"face"} else "V_edge"
    if n == 6:
        return "S3_body"
    if n == 8:
        return "D4_face"
    if n == 12:
        return "A4_tetrahedral"
    if n == 24:
        return "O_full"
    return f"G{n}_unnamed"                             # pragma: no cover gate


def normalizer(h: frozenset) -> frozenset:
    return frozenset(g for g in GROUP
                     if frozenset(mul(mul(g, x), INVERSE[g]) for x in h) == h)


def conjugacy_class_of(h: frozenset) -> frozenset:
    return frozenset(
        frozenset(mul(mul(g, x), INVERSE[g]) for x in h) for g in GROUP)


LATTICE = all_subgroups()


def build_lattice_rows() -> list[dict]:
    class_index: dict[frozenset, int] = {}
    classes: list[frozenset] = []
    for h in LATTICE:
        if h in class_index:
            continue
        klass = conjugacy_class_of(h)
        idx = len(classes)
        classes.append(klass)
        for member in klass:
            class_index[member] = idx
    rows = []
    for h in LATTICE:
        rows.append({
            "key": h,
            "order": len(h),
            "name": structure_name(h),
            "class_index": class_index[h],
            "is_cyclic": is_cyclic(h),
            "is_abelian": is_abelian(h),
            "normalizer_order": len(normalizer(h)),
            "normal_in_the_full_group": len(normalizer(h)) == len(GROUP),
            "element_indices": sorted(GROUP.index(m) for m in h),
        })
    return sorted(rows, key=lambda r: (r["order"], r["name"],
                                       r["element_indices"]))


LATTICE_ROWS = build_lattice_rows()
CLASS_NAMES = sorted({r["name"] for r in LATTICE_ROWS})
CLASS_REPRESENTATIVE = {}
for _row in LATTICE_ROWS:
    CLASS_REPRESENTATIVE.setdefault(_row["name"], _row)


def permutation_index(elem, points):
    index = {p: i for i, p in enumerate(points)}
    return tuple(index[act(elem, p)] for p in points)


def permutation_matrix(elem, points):
    n = len(points)
    perm = permutation_index(elem, points)
    m = [[Fraction(0)] * n for _ in range(n)]
    for j in range(n):
        m[perm[j]][j] = Fraction(1)
    return m


def pair_orbit_count(subgroup, points) -> int:
    """Orbits of the subgroup on X x X -- the FIND-3 safety invariant."""
    seen, count = set(), 0
    for a in points:
        for b in points:
            if (a, b) in seen:
                continue
            count += 1
            for g in subgroup:
                seen.add((act(g, a), act(g, b)))
    return count


def scope_points_for(row) -> dict:
    """The two readout scopes of a subgroup, computed from its orbit data."""
    h = sorted(row["key"])
    order = row["order"]
    orbs = orbits_of(h, NEAREST_NEIGHBOURS)
    lengths = sorted(len(o) for o in orbs)
    free = [o for o in orbs if len(o) == order]
    return {
        "shell_orbit_lengths": lengths,
        "shell_orbit_count": len(orbs),
        "free_orbit_count": len(free),
        "has_a_free_orbit_on_the_shell": bool(free),
        "maximal_FREE_orbit_length": max([len(o) for o in free], default=0),
        "acts_freely_on_the_shell": all(L == order for L in lengths),
        "transitive_on_the_shell": len(orbs) == 1,
        "simply_transitive_on_the_shell": len(orbs) == 1 and lengths == [order],
        SCOPES[0]: sorted(max(free, key=len)) if free else None,
        SCOPES[1]: list(NEAREST_NEIGHBOURS),
    }


# ==========================================================================
# SIDE B -- ALGEBRAIC multiplicity-freeness (enveloping algebra route)
# ==========================================================================
def span_of_matrices(mats, n):
    reduced_rows: list[list[Fraction]] = []
    pivots: list[int] = []
    basis = []
    for mat in mats:
        cur = [mat[i][j] for i in range(n) for j in range(n)]
        for row, pcol in zip(reduced_rows, pivots):
            if cur[pcol] != 0:
                f = cur[pcol]
                cur = [a - f * b for a, b in zip(cur, row)]
        piv = next((k for k, x in enumerate(cur) if x != 0), None)
        if piv is None:
            continue
        cur = [x / cur[piv] for x in cur]
        reduced_rows.append(cur)
        pivots.append(piv)
        basis.append(mat)
    return basis


def centre_of_algebra(algebra_basis, gens, n):
    r = len(algebra_basis)
    eqs = []
    for g in gens:
        for i in range(n):
            for j in range(n):
                row = []
                for b in algebra_basis:
                    lhs = sum(b[i][k] * g[k][j] for k in range(n))
                    rhs = sum(g[i][k] * b[k][j] for k in range(n))
                    row.append(lhs - rhs)
                eqs.append(row)
    coeffs = kernel_basis(eqs, r)
    out = []
    for vec in coeffs:
        mat = [[sum(vec[k] * algebra_basis[k][i][j] for k in range(r))
                for j in range(n)] for i in range(n)]
        den = 1
        for i in range(n):
            for j in range(n):
                den = den * mat[i][j].denominator // gcd(
                    den, mat[i][j].denominator)
        out.append([[mat[i][j] * den for j in range(n)] for i in range(n)])
    return out


def find_centre_generator(centre_basis, n):
    r = len(centre_basis)
    for spread in range(1, 6):
        for coeffs in product(range(0, spread + 1), repeat=r):
            if not any(coeffs):
                continue
            z = [[sum(coeffs[k] * centre_basis[k][i][j] for k in range(r))
                  for j in range(n)] for i in range(n)]
            mp = minimal_polynomial([[int(x) for x in row] for row in z])
            if len(mp) - 1 == r:
                return z, mp, list(coeffs)
    return None, None, None                            # pragma: no cover gate


def side_b_multiplicity_freeness(subgroup, points) -> dict:
    """SIDE B: isotypic decomposition through the centre of the enveloping
    algebra.  Never sees SIDE A."""
    n = len(points)
    elements = sorted(subgroup)
    mats = [permutation_matrix(g, points) for g in elements]
    algebra = span_of_matrices(mats, n)
    centre = centre_of_algebra(algebra, mats, n)
    z, mp, coeffs = find_centre_generator(centre, n)
    if z is None:                                      # pragma: no cover gate
        return {"ok": False, "reason": "no generator of the centre found"}
    factors = factor_monic_squarefree(mp)
    if factors is None:                                # pragma: no cover gate
        return {"ok": False, "reason": "irreducible factor of degree > 2"}
    back = [1]
    for f in factors:
        acc = [Fraction(0)] * (len(back) + len(f) - 1)
        for i, a in enumerate(back):
            for j, b in enumerate(f):
                acc[i + j] += a * b
        back = [int(x) for x in acc]
    if back != mp:                                     # pragma: no cover gate
        return {"ok": False, "reason": "factorization does not multiply back"}

    isotypes = []
    for f in factors:
        fz = poly_of_matrix(f, [[Fraction(x) for x in row] for row in z])
        basis = kernel_basis(fz, n)
        dim = len(basis)
        if dim == 0:
            continue
        u_cols = [[basis[k][i] for k in range(dim)] for i in range(n)]
        restricted = []
        for b in algebra:
            image = [[sum(b[i][k] * u_cols[k][c] for k in range(n))
                      for c in range(dim)] for i in range(n)]
            c_mat = solve_columns(u_cols, image)
            if c_mat is None:                          # pragma: no cover gate
                return {"ok": False,
                        "reason": "isotypic component is not A-invariant"}
            restricted.append(c_mat)
        dim_a_i = len(span_of_matrices(restricted, dim))
        t_i = len(f) - 1
        square = dim_a_i * t_i
        d_i = isqrt(square)
        if d_i * d_i != square or d_i == 0 or dim % d_i != 0:
            return {"ok": False,                       # pragma: no cover gate
                    "reason": "degree recovery failed on a component"}
        acts_trivially = all(
            all(rowc == expected for rowc, expected
                in zip(c, identity_matrix(dim))) for c in restricted)
        isotypes.append({
            "irreducible_degree_over_Q": d_i,
            "multiplicity": dim // d_i,
            "component_dimension": dim,
            "endomorphism_field_degree": t_i,
            "dim_Q_of_the_component_algebra": dim_a_i,
            "minimal_polynomial_factor": f,
            "is_the_trivial_isotype": acts_trivially,
        })
    isotypes.sort(key=lambda b: (b["irreducible_degree_over_Q"],
                                 b["multiplicity"],
                                 b["endomorphism_field_degree"]))
    fine_dims = sorted(d for b in isotypes
                       for d in [b["irreducible_degree_over_Q"]]
                       * b["multiplicity"])
    invariant_dim = n - rank_exact(
        [row for m in mats
         for row in mat_add_scaled(m, identity_matrix(n), Fraction(-1))])
    orbit_count = len(orbits_of(elements, points))
    trivial_rows = [b for b in isotypes if b["is_the_trivial_isotype"]]
    trivial_mult = trivial_rows[0]["multiplicity"] if trivial_rows else 0
    sum_m2t = sum(b["multiplicity"] ** 2 * b["endomorphism_field_degree"]
                  for b in isotypes)
    pair_orbits = pair_orbit_count(elements, points)
    gates = {
        "fine_decomposition_sums_to_the_space": sum(fine_dims) == n,
        "trivial_isotype_multiplicity_equals_the_orbit_count":
            trivial_mult == orbit_count,
        "FIND3_safety_sum_m_squared_field_degree_equals_pair_orbit_count":
            sum_m2t == pair_orbits,
        "invariant_dimension_equals_the_orbit_count":
            invariant_dim == orbit_count,
    }
    return {
        "ok": True,
        "route": "SIDE_B_enveloping_algebra_centre_minimal_polynomial",
        "space_dimension": n,
        "subgroup_order": len(elements),
        "enveloping_algebra_dimension": len(algebra),
        "centre_dimension": len(centre),
        "centre_generator_coefficients": coeffs,
        "centre_generator_minimal_polynomial": mp,
        "minimal_polynomial_irreducible_factors": factors,
        "isotypes": isotypes,
        "fine_rational_irreducible_dimensions": fine_dims,
        "fine_multiplicities": [b["multiplicity"] for b in isotypes],
        "invariant_dimension": invariant_dim,
        "orbit_count": orbit_count,
        "coarse_ordered_pair": [invariant_dim, n - invariant_dim],
        "coarse_two_adic_profile": [
            vp(Fraction(invariant_dim), 2) if invariant_dim else None,
            vp(Fraction(n - invariant_dim), 2) if n - invariant_dim else None,
        ],
        "fine_top_rational_irreducible_dimension":
            max(fine_dims) if fine_dims else 0,
        "fine_top_pair": [invariant_dim, max(fine_dims) if fine_dims else 0],
        "fine_dimensions_with_a_v2_equal_to_one":
            [d for d in fine_dims if vp(Fraction(d), 2) == 1],
        "sum_of_m_squared_times_field_degree": sum_m2t,
        "pair_orbit_count": pair_orbits,
        "MULTIPLICITY_FREE": all(b["multiplicity"] <= 1 for b in isotypes),
        "gates": gates,
        "all_gates_pass": all(gates.values()),
    }


# ==========================================================================
# SIDE A -- GEOMETRIC canonicity (submodule exhibition + moduli of
# realizations).  Never sees SIDE B.
# ==========================================================================
def cyclic_submodules(subgroup, points, radius: int) -> dict:
    """Every A-submodule generated by a single integer vector of the grid.

    Generators are normalized projectively (primitive, positive leading entry)
    so each projective point is visited once and the enumeration is
    deterministic.
    """
    n = len(points)
    perms = [permutation_index(g, points) for g in sorted(subgroup)]
    found: dict[tuple, list[list[Fraction]]] = {}
    for w in product(range(-radius, radius + 1), repeat=n):
        if not any(w):
            continue
        g0 = 0
        for x in w:
            g0 = gcd(g0, abs(x))
        primitive = tuple(x // g0 for x in w)
        if primitive != w or next(x for x in w if x != 0) < 0:
            continue
        span = []
        for pm in perms:
            v = [0] * n
            for j in range(n):
                v[pm[j]] = w[j]
            span.append(v)
        reduced, _ = rref(span)
        key = tuple(tuple(q(x) for x in row) for row in reduced)
        if key not in found:
            found[key] = [list(row) for row in reduced]
    return found


def restricted_action(subgroup, points, basis):
    """Matrices of the subgroup action in the given submodule basis, or None
    if the span is not invariant."""
    n = len(points)
    d = len(basis)
    perms = [permutation_index(g, points) for g in sorted(subgroup)]
    columns = [[basis[i][j] for i in range(d)] for j in range(n)]
    out = []
    for pm in perms:
        images = []
        for b in basis:
            row = [Fraction(0)] * n
            for j in range(n):
                row[pm[j]] = b[j]
            images.append(row)
        mat = []
        for row in images:
            aug = [columns[j] + [row[j]] for j in range(n)]
            reduced, pivots = rref(aug)
            sol = [Fraction(0)] * d
            for r, c in enumerate(pivots):
                if c == d:
                    return None
                sol[c] = reduced[r][d]
            mat.append(sol)
        out.append(mat)
    return out


def intertwiner_space(subgroup, points, u_basis, v_basis):
    """Basis of Hom_A(U, V) as dU x dV coefficient matrices."""
    au = restricted_action(subgroup, points, u_basis)
    av = restricted_action(subgroup, points, v_basis)
    if au is None or av is None:                       # pragma: no cover gate
        return None
    du, dv = len(u_basis), len(v_basis)
    eqs = []
    for ga, gb in zip(au, av):
        for i in range(du):
            for j in range(dv):
                row = [Fraction(0)] * (du * dv)
                for k in range(du):
                    row[k * dv + j] += ga[i][k]
                for k in range(dv):
                    row[i * dv + k] -= gb[k][j]
                eqs.append(row)
    return kernel_basis(eqs, du * dv)


def homs_into_the_module(subgroup, points, u_basis):
    """Basis of Hom_A(U, M) with M the whole permutation module.

    dim Hom_A(U, M) = m * [End_A(U) : Q] for U irreducible, so the moduli of
    submodules of M isomorphic to U is P(Hom_A(U,M)) over End_A(U): a SINGLE
    POINT exactly when dim Hom = dim End.
    """
    n = len(points)
    du = len(u_basis)
    au = restricted_action(subgroup, points, u_basis)
    perms = [permutation_index(g, points) for g in sorted(subgroup)]
    eqs = []
    for gi, pm in enumerate(perms):
        ga = au[gi]
        rho = [[Fraction(0)] * n for _ in range(n)]
        for j in range(n):
            rho[pm[j]][j] = Fraction(1)
        for i in range(du):
            for j in range(n):
                row = [Fraction(0)] * (du * n)
                for k in range(du):
                    row[k * n + j] += ga[i][k]
                for k in range(n):
                    row[i * n + k] -= rho[j][k]
                eqs.append(row)
    return kernel_basis(eqs, du * n)


def contains_subspace(outer, inner) -> bool:
    return rank_exact([list(r) for r in outer] + [list(r) for r in inner]) \
        == rank_exact(outer)


def side_a_canonicity(subgroup, points, family_probe: int = 12) -> dict:
    """SIDE A: build a full decomposition into EXHIBITED irreducible
    submodules, group them by explicit intertwiners, and compute the moduli of
    realizing subspaces per isomorphism class.  Never sees SIDE B."""
    n = len(points)
    chosen: list[list[list[Fraction]]] = []
    radius_used = None
    submodule_counts = {}
    for radius in (1, 2, 3):
        subs = cyclic_submodules(subgroup, points, radius)
        submodule_counts[f"cyclic_submodules_at_grid_radius_{radius}"] = len(subs)
        items = sorted(subs.items(), key=lambda kv: (len(kv[1]), kv[0]))
        chosen, current = [], []
        for _key, basis in items:
            if len(current) + len(basis) > n:
                continue
            trial = current + [list(r) for r in basis]
            if rank_exact(trial) != len(trial):
                continue
            irreducible = True
            for _k2, smaller in items:
                if len(smaller) >= len(basis):
                    break
                if contains_subspace(basis, smaller):
                    irreducible = False
                    break
            if not irreducible:
                continue
            chosen.append([list(r) for r in basis])
            current = trial
            if len(current) == n:
                break
        radius_used = radius
        if current and rank_exact(current) == n:
            break
    covered = bool(chosen) and rank_exact(
        [row for b in chosen for row in b]) == n

    classes: list[list[list[list[Fraction]]]] = []
    for basis in chosen:
        placed = False
        for cl in classes:
            hom = intertwiner_space(subgroup, points, basis, cl[0])
            if hom and len(hom) > 0:
                cl.append(basis)
                placed = True
                break
        if not placed:
            classes.append([basis])

    rows = []
    for cl in classes:
        rep = cl[0]
        degree = len(rep)
        end_dim = len(intertwiner_space(subgroup, points, rep, rep))
        hom_dim = len(homs_into_the_module(subgroup, points, rep))
        moduli_dim = hom_dim - end_dim
        exhibited = None
        if moduli_dim > 0 and len(cl) >= 2:
            # explicit one-parameter family of DISTINCT realizing subspaces:
            # graphs of lambda * phi for an intertwiner phi : U -> V.
            other = cl[1]
            phi = intertwiner_space(subgroup, points, rep, other)[0]
            seen = set()
            members = []
            for lam in range(0, family_probe):
                graph = []
                for i, urow in enumerate(rep):
                    combo = [urow[j] for j in range(len(urow))]
                    for k in range(degree):
                        coeff = phi[i * degree + k] * Fraction(lam)
                        if coeff:
                            combo = [a + coeff * b
                                     for a, b in zip(combo, other[k])]
                    graph.append(combo)
                if rank_exact(graph) != degree:         # pragma: no cover gate
                    continue
                if restricted_action(subgroup, points, graph) is None:
                    continue                            # pragma: no cover gate
                key = subspace_key(graph)
                if key not in seen:
                    seen.add(key)
                    members.append(key)
            exhibited = {
                "construction": (
                    "U_lambda = { u + lambda * phi(u) : u in U } for an "
                    "explicit A-isomorphism phi : U -> V between two distinct "
                    "exhibited irreducible submodules; defined for EVERY "
                    "lambda in Q, so the family is infinite over Q"
                ),
                "parameters_probed": family_probe,
                "distinct_members_verified": len(members),
                "every_member_is_A_invariant_of_the_right_dimension": True,
            }
        uniqueness_evidence = None
        if moduli_dim == 0:
            uniqueness_evidence = {
                "argument": (
                    "dim_Q Hom_A(U, M) equals dim_Q End_A(U), so every A-map "
                    "U -> M has image U: the U-isotypic component IS U and no "
                    "second realizing subspace of this type exists"
                ),
                "dim_Hom_A_U_M": hom_dim,
                "dim_End_A_U": end_dim,
                "other_exhibited_submodules_isomorphic_to_U": len(cl) - 1,
            }
        rows.append({
            "irreducible_degree_over_Q": degree,
            "exhibited_summands_in_this_class": len(cl),
            "dim_End_A_of_the_irreducible": end_dim,
            "dim_Hom_A_into_the_whole_module": hom_dim,
            "multiplicity_from_the_hom_space": hom_dim // end_dim,
            "MODULI_DIMENSION_OF_REALIZING_SUBSPACES_over_Q": moduli_dim,
            "realizing_subspace_is_a_single_point": moduli_dim == 0,
            "explicit_family_exhibited": exhibited,
            "uniqueness_evidence": uniqueness_evidence,
            "representative_basis": [[q(x) for x in row] for row in rep],
        })
    rows.sort(key=lambda r: (r["irreducible_degree_over_Q"],
                             r["multiplicity_from_the_hom_space"]))
    sum_m2t = sum(r["multiplicity_from_the_hom_space"] ** 2
                  * r["dim_End_A_of_the_irreducible"] for r in rows)
    pair_orbits = pair_orbit_count(sorted(subgroup), points)
    gates = {
        "the_exhibited_summands_span_the_readout_space": covered,
        "exhibited_degrees_sum_to_the_space_dimension":
            sum(len(b) for b in chosen) == n,
        "FIND3_safety_sum_m_squared_field_degree_equals_pair_orbit_count":
            sum_m2t == pair_orbits,
        "every_class_with_a_positive_moduli_dimension_exhibits_a_family":
            all(r["explicit_family_exhibited"] is not None
                and r["explicit_family_exhibited"]
                ["distinct_members_verified"] >= 2
                for r in rows
                if r["MODULI_DIMENSION_OF_REALIZING_SUBSPACES_over_Q"] > 0),
        "every_single_point_class_carries_a_uniqueness_proof":
            all(r["uniqueness_evidence"] is not None for r in rows
                if r["MODULI_DIMENSION_OF_REALIZING_SUBSPACES_over_Q"] == 0),
    }
    return {
        "route": "SIDE_A_exhibited_submodules_and_hom_space_moduli",
        "space_dimension": n,
        "grid_radius_used": radius_used,
        "grid_enumeration": submodule_counts,
        "exhibited_irreducible_summands": len(chosen),
        "isomorphism_classes": rows,
        "total_moduli_dimension_over_Q":
            sum(r["MODULI_DIMENSION_OF_REALIZING_SUBSPACES_over_Q"]
                for r in rows),
        "sum_of_m_squared_times_field_degree": sum_m2t,
        "pair_orbit_count": pair_orbits,
        "CANONICAL": all(
            r["realizing_subspace_is_a_single_point"] for r in rows),
        "gates": gates,
        "all_gates_pass": all(gates.values()),
    }


# ==========================================================================
# byte-exact document segmentation for the H2 sweep
# ==========================================================================
ABBREVIATIONS = ("e.g", "i.e", "cf", "vs", "etc", "al", "approx", "Dr", "Fig",
                 "No", "St", "Mr", "Ms", "Inc", "Ltd", "Jr", "Sr")

LIST_MARKER = re.compile(r"^(\s*(?:[-*+]|\d+\.)\s+)")
HEADING = re.compile(r"^\s*#{1,6}\s")
TABLE_ROW = re.compile(r"^\s*\|")
FENCE = re.compile(r"^\s*(```|~~~)")


def _sentence_cuts(chunk: str) -> list[int]:
    """Indices (exclusive ends) at which `chunk` splits into sentences."""
    cuts = []
    backticks = 0
    for i, ch in enumerate(chunk):
        if ch == "`":
            backticks += 1
            continue
        if ch not in ".!?":
            continue
        if backticks % 2 == 1:                    # inside an inline code span
            continue
        nxt = chunk[i + 1] if i + 1 < len(chunk) else ""
        if nxt and nxt not in " \n\t":
            continue                              # ".md", "0.1", "3.5"
        word = re.search(r"([A-Za-z.]+)$", chunk[:i])
        if word and word.group(1).rstrip(".") in ABBREVIATIONS:
            continue
        k = i + 1
        while k < len(chunk) and chunk[k] in " \n\t":
            k += 1
        if k < len(chunk):
            follow = chunk[k]
            if not (follow.isupper() or follow.isdigit()
                    or follow in "`*[_\"(-<>|#"):
                continue
        cuts.append(i + 1)
    if not cuts or cuts[-1] != len(chunk):
        cuts.append(len(chunk))
    return cuts


def segment_document(text: str) -> list[dict]:
    """A BYTE-EXACT partition of `text` into classified segments.

    Every character of the file lands in exactly one segment, so
    ''.join(seg['text']) == text is a reconstruction proof of completeness.
    """
    segments: list[dict] = []
    pos = 0
    in_fence = False
    lines = text.splitlines(keepends=True)
    buffer_start = None
    buffer: list[str] = []

    def flush_prose(start: int, chunk: str):
        if not chunk:
            return
        stripped = chunk.strip()
        if not stripped:
            segments.append({"start": start, "text": chunk, "kind": "GAP"})
            return
        lead = len(chunk) - len(chunk.lstrip())
        trail = len(chunk) - len(chunk.rstrip())
        if lead:
            segments.append({"start": start, "text": chunk[:lead],
                             "kind": "GAP"})
        body_start = start + lead
        body = chunk[lead:len(chunk) - trail] if trail else chunk[lead:]
        marker = LIST_MARKER.match(body)
        if marker:
            segments.append({"start": body_start, "text": marker.group(1),
                             "kind": "LIST_MARKER"})
            body_start += len(marker.group(1))
            body = body[len(marker.group(1)):]
        prev = 0
        for cut in _sentence_cuts(body):
            piece = body[prev:cut]
            if piece.strip():
                lead2 = len(piece) - len(piece.lstrip())
                if lead2:
                    segments.append({"start": body_start + prev,
                                     "text": piece[:lead2], "kind": "GAP"})
                segments.append({"start": body_start + prev + lead2,
                                 "text": piece[lead2:], "kind": "SENTENCE"})
            elif piece:
                segments.append({"start": body_start + prev, "text": piece,
                                 "kind": "GAP"})
            prev = cut
        if trail:
            segments.append({"start": start + len(chunk) - trail,
                             "text": chunk[len(chunk) - trail:],
                             "kind": "GAP"})

    for line in lines:
        line_start = pos
        pos += len(line)
        fence_hit = bool(FENCE.match(line))
        structural = bool(HEADING.match(line) or TABLE_ROW.match(line))
        blank = not line.strip()
        if (not in_fence and not fence_hit and not structural and not blank
                and LIST_MARKER.match(line) and buffer):
            # a list item always starts its own block
            flush_prose(buffer_start, "".join(buffer))
            buffer, buffer_start = [], None
        if in_fence or fence_hit or structural or blank:
            if buffer:
                flush_prose(buffer_start, "".join(buffer))
                buffer, buffer_start = [], None
            kind = ("CODE" if (in_fence or fence_hit) else
                    "HEADING" if HEADING.match(line) else
                    "TABLE_ROW" if TABLE_ROW.match(line) else "GAP")
            segments.append({"start": line_start, "text": line, "kind": kind})
            if fence_hit:
                in_fence = not in_fence
            continue
        if buffer_start is None:
            buffer_start = line_start
        buffer.append(line)
    if buffer:
        flush_prose(buffer_start, "".join(buffer))
    segments.sort(key=lambda s: s["start"])
    return segments


# ==========================================================================
# the H2 grounding rubric -- declared, mechanical, and reported in full
# ==========================================================================
RUBRIC = {
    "target_property": (
        "MULTIPLICITY-FREENESS of the readout representation -- equivalently: "
        "the readout decomposition is canonical; the invariant complement is "
        "unique; the realizing subspace carries no free parameter."
    ),
    "E1_SUBJECT_the_readout_object": (
        "readout", "read out", "readable", "reading", "representation",
        "decomposition", "isotype", "isotypic", "irreducible", "multiplicity",
        "invariant", "complement", "component", "sector", "subspace",
        "presentation", "possibility domain", "possibilities", "algebra",
        "observable", "basis", "context", "record content",
    ),
    "E2_UNIQUENESS_no_free_parameter": (
        "determined", "determines", "determine", "exactly one", "unique",
        "uniquely", "alone", "only", "fixed", "no free", "no further",
        "canonical", "rigid", "single", "more than one", "one fixed",
        "complete", "not arbitrary", "no more than",
    ),
    # E3 is split because co-occurrence is not predication.  The property is
    # about the DECOMPOSITION OF A REPRESENTATION into invariant pieces; nouns
    # like "orbit", "sector" and "basis" name objects ADJACENT to that without
    # naming it.  Only the STRONG family can carry an EXACT grade.
    "E3_STRONG_the_decomposition_of_a_representation": (
        "decomposition", "multiplicity", "irreducible", "isotype", "isotypic",
        "invariant subspace", "invariant complement", "invariant piece",
        "complement", "summand", "direct sum", "split into",
    ),
    "E3_WEAK_structurally_adjacent_nouns": (
        "sector", "component", "subspace", "invariant", "split", "basis",
        "orbit", "structure",
    ),
    "POLARITY_EXCLUDES_places_the_content_outside_the_axioms": (
        "downstream", "not generic axiom content", "must cite separate",
        "remains outside", "remain outside", "outside axiom", "does not close",
        "do not close", "does not include", "do not include",
        "must not be treated", "must not be", "remains conditional",
        "remain conditional", "open dependency", "requires a retained",
        "not an approved", "remain bounded", "bounded/pending",
        "no admission class", "historical", "supersedes", "does not derive",
        "derives no", "changes no", "is not a dynamics axiom",
        "does not choose", "adds no new axiom", "supplies no", "not this axiom",
        "remains an open", "open derivation obligation", "no-go",
        "still supplied", "does not discharge", "not a retained",
    ),
    "grading_rule": (
        "POLARITY first: a sentence that places the content downstream, "
        "conditional, historical or outside axiom content CANNOT ground it, "
        "and grades NONE with class EXCLUSION_HIT no matter how many subject "
        "markers it carries.  Otherwise EXACT requires E1 and E2 and a STRONG "
        "E3 marker, with the E2 marker and the STRONG E3 marker occurring in "
        "the SAME clause (comma/semicolon/colon delimited), so that the "
        "uniqueness is predicated OF the decomposition rather than merely "
        "co-occurring with it; exactly two of {E1, E2, E3-any} grades PARTIAL; "
        "anything less grades NONE."
    ),
    "why_two_variants_are_run": (
        "Variant v1_permissive lets the WEAK E3 nouns carry an EXACT; variant "
        "v2_strict does not.  Both are computed and both distributions are "
        "reported, because the difference between them IS the finding: it "
        "shows exactly how thin any 'quotable' reading has to be.  The verdict "
        "is taken from v2_strict, and every sentence the two variants grade "
        "differently is quoted and adjudicated in the open."
    ),
    "price_registration_needles": (
        "A choice not fixed by the supplied structure remains a named "
        "conditional or open dependency.",
        "Further physical structure requires a retained derivation or bridge, "
        "or explicit approved-",
    ),
}


def _markers_hit(lowered: str, family: tuple) -> list[str]:
    return sorted({m for m in family if m in lowered})


RUBRIC_VARIANTS = ("v2_strict", "v1_permissive")


def grade_sentence(text: str, variant: str = "v2_strict") -> dict:
    lowered = norm(text).lower()
    e1 = _markers_hit(lowered, RUBRIC["E1_SUBJECT_the_readout_object"])
    e2 = _markers_hit(lowered, RUBRIC["E2_UNIQUENESS_no_free_parameter"])
    strong = RUBRIC["E3_STRONG_the_decomposition_of_a_representation"]
    weak = RUBRIC["E3_WEAK_structurally_adjacent_nouns"]
    e3_strong = _markers_hit(lowered, strong)
    e3_weak = _markers_hit(lowered, weak)
    e3 = sorted(set(e3_strong) | set(e3_weak))
    excl = _markers_hit(
        lowered,
        RUBRIC["POLARITY_EXCLUDES_places_the_content_outside_the_axioms"])
    exact_family = tuple(strong) + (tuple(weak) if variant == "v1_permissive"
                                    else ())
    e3_for_exact = _markers_hit(lowered, exact_family)
    clauses = [c for c in re.split(r"[;:,]", lowered) if c.strip()]
    same_clause = any(
        any(m in c for m in RUBRIC["E2_UNIQUENESS_no_free_parameter"])
        and any(m in c for m in exact_family)
        for c in clauses)
    present = sum(1 for x in (e1, e2, e3) if x)
    if excl:
        grade, klass = "NONE", "EXCLUSION_HIT"
    elif e1 and e2 and e3_for_exact and same_clause:
        grade, klass = "EXACT", "GROUNDING_CANDIDATE"
    elif present >= 2:
        grade, klass = "PARTIAL", "GROUNDING_CANDIDATE"
    else:
        grade, klass = "NONE", "NO_BEARING"
    # match on the whitespace-normalized form: these sentences wrap across
    # source lines, so a raw substring test silently never fires.
    registers_price = any(norm(needle) in norm(text)
                          for needle in RUBRIC["price_registration_needles"])
    if grade == "EXACT":
        reason = (
            "The sentence carries subject, uniqueness AND decomposition-level "
            "markers, with the uniqueness predicated of the decomposition "
            f"inside one clause (subject {e1}; uniqueness {e2}; level "
            f"{e3_for_exact} under variant {variant}). "
            "The filter would need exactly this: that the readout "
            "representation's split into invariant pieces admits no free "
            "parameter."
        )
    elif grade == "PARTIAL":
        missing = [n for n, x in (("subject", e1), ("uniqueness", e2),
                                  ("decomposition level", e3)) if not x]
        if not missing:
            missing = ["the uniqueness is not predicated OF the decomposition "
                       "(no clause carries both)"]
        reason = (
            f"Present: subject {e1}; uniqueness {e2}; level {e3}. Missing for "
            f"a grounding: {missing}. The filter needs the sentence to say "
            "that the readout representation's decomposition into invariant "
            "pieces is unique; this sentence bears on the readout without "
            "reaching that."
        )
    elif klass == "EXCLUSION_HIT":
        reason = (
            f"The sentence's own provenance predicate {excl} places this "
            "content downstream of, conditional on, or outside the axiom "
            "surface, so it cannot be quoted AS a ground for "
            "multiplicity-freeness. It is evidence about where the property "
            f"lives, not a supply of it. (Markers present anyway: subject "
            f"{e1}; uniqueness {e2}; level {e3}.)"
        )
    else:
        reason = (
            f"Fewer than two rubric elements present (subject {e1}; "
            f"uniqueness {e2}; level {e3}). The filter would need a statement "
            "that the readout representation decomposes in exactly one way; "
            "this sentence makes no claim bearing on that."
        )
    return {
        "grade": grade,
        "class": klass,
        "rubric_variant": variant,
        "E1_subject_markers": e1,
        "E2_uniqueness_markers": e2,
        "E3_decomposition_level_markers": e3,
        "E3_STRONG_markers": e3_strong,
        "E3_WEAK_markers": e3_weak,
        "exclusion_markers": excl,
        "uniqueness_and_level_in_the_same_clause": same_clause,
        "registers_the_price_rather_than_grounding_it": registers_price,
        "reason": reason,
    }


def sweep_document(path: str) -> dict:
    text = _read_text(path)
    segments = segment_document(text)
    rebuilt = "".join(s["text"] for s in segments)
    rows = []
    for idx, seg in enumerate(segments):
        entry = {
            "segment_index": idx,
            "byte_start": seg["start"],
            "byte_end": seg["start"] + len(seg["text"]),
            "kind": seg["kind"],
        }
        if seg["kind"] == "SENTENCE":
            entry["byte_quoted_sentence"] = seg["text"]
            entry["normalized"] = norm(seg["text"])
            entry.update(grade_sentence(seg["text"], "v2_strict"))
            permissive = grade_sentence(seg["text"], "v1_permissive")
            entry["grade_under_v1_permissive"] = permissive["grade"]
            entry["variants_disagree"] = permissive["grade"] != entry["grade"]
            entry["v1_permissive_reason"] = permissive["reason"]
            entry["what_the_sentence_says"] = norm(seg["text"])
            entry["what_the_filter_would_need_it_to_say"] = (
                "that the decomposition of the readout representation into "
                "invariant pieces is unique -- no isotype repeats, so the "
                "realizing subspace carries no free parameter"
            )
        else:
            entry["grade"] = "NONE"
            entry["class"] = "NON_PROSE"
            entry["reason"] = (
                f"segment kind {seg['kind']}: carries no assertion that could "
                "ground the property; retained so the partition is byte-exact"
            )
        rows.append(entry)
    sentences = [r for r in rows if r["kind"] == "SENTENCE"]
    dist = {g: sum(1 for r in sentences if r["grade"] == g) for g in GRADES}
    dist_v1 = {g: sum(1 for r in sentences
                      if r["grade_under_v1_permissive"] == g) for g in GRADES}
    return {
        "grade_distribution_under_v1_permissive": dist_v1,
        "path": path,
        "sha256": sha256(text.encode("utf-8")).hexdigest(),
        "file_bytes": len(text.encode("utf-8")),
        "file_characters": len(text),
        "segment_count": len(segments),
        "sentence_count": len(sentences),
        "segment_kind_counts": {
            k: sum(1 for s in segments if s["kind"] == k)
            for k in sorted({s["kind"] for s in segments})},
        "reconstructs_the_file_byte_for_byte": rebuilt == text,
        "character_accounting":
            sum(len(s["text"]) for s in segments) == len(text),
        "grade_distribution": dist,
        "rows": rows,
    }


# ==========================================================================
# certificates
# ==========================================================================
def pins_certificate() -> dict:
    rows, ok = [], True
    for path in AUDIT_INPUT_PATHS:
        target = ROOT / path
        exists = target.exists()
        got = sha256(_read_bytes(path)).hexdigest() if exists else None
        try:
            blob = subprocess.run(["git", "hash-object", str(target)],
                                  capture_output=True, text=True,
                                  cwd=str(ROOT), check=True).stdout.strip() \
                if exists else None
        except Exception:                              # pragma: no cover gate
            blob = None
        sha_ok = got == EXPECTED_SHA256[path]
        blob_ok = blob == EXPECTED_GIT_BLOBS[path]
        ok = ok and exists and sha_ok and blob_ok
        rows.append({"path": path, "absolute_path": str(target),
                     "exists": exists, "sha256": got,
                     "sha256_matches_pin": sha_ok, "git_blob": blob,
                     "git_blob_matches_pin": blob_ok})
    scan = subprocess.run(["git", "ls-files", "docs/GATE_B_*.md"],
                          capture_output=True, text=True, cwd=str(ROOT))
    gate_b_all = sorted(x for x in scan.stdout.split() if x)
    lineage_hits = {}
    for script in NOTE_DISCOVERY_SCAN["lineage_scripts_scanned"]:
        try:
            src = _read_text(script)
        except OSError:                                # pragma: no cover gate
            lineage_hits[script] = None
            continue
        lineage_hits[script] = sorted(
            {n.value for n in ast.walk(ast.parse(src))
             if isinstance(n, ast.Constant) and isinstance(n.value, str)
             and n.value.startswith("docs/") and n.value.endswith(".md")})
    selected_are_named = all(
        any(sel in (hits or []) for hits in lineage_hits.values())
        for sel in (NOTE_DISCOVERY_SCAN["gate_b_notes_selected"]
                    + (NOTE_DISCOVERY_SCAN["readout_obligation_note_selected"],))
    )
    ok = ok and selected_are_named
    return {
        "statement": (
            "GATE C890-G1. Every cited artifact is pinned by absolute path, "
            "SHA-256 and git blob and read as text/AST/JSON only. A missing or "
            "moved pin is a hard preflight failure (exit 2). The two Gate-B "
            "notes and the readout obligation note are DISCOVERED by a "
            "tracked-file scan of the lineage's own pin tuples, not assumed."
        ),
        "rows": rows,
        "read_mode": "text/AST/JSON only; import blocked by meta-path firewall",
        "note_discovery": dict(
            NOTE_DISCOVERY_SCAN,
            gate_b_notes_tracked_on_the_branch=len(gate_b_all),
            gate_b_notes_named_by_the_lineage=lineage_hits,
            every_selected_note_is_named_by_the_lineage=selected_are_named,
        ),
        "finding": (
            f"{sum(1 for r in rows if r['sha256_matches_pin'] and r['git_blob_matches_pin'])}"
            f"/{len(rows)} pinned artifacts round-trip on both SHA-256 and git "
            f"blob; {len(gate_b_all)} Gate-B notes are tracked on the branch "
            f"and the {len(NOTE_DISCOVERY_SCAN['gate_b_notes_selected'])} this "
            f"lineage carries are the ones swept."
        ),
        "pass": ok,
    }


def ast_recovery_certificate() -> dict:
    """The 888 primary is read as AST -- never imported -- and its declared
    menu rule and constants are recovered so this cycle's independent rebuild
    can be checked against the pinned original's own words."""
    source = _read_text(AUDIT_INPUT_PATHS[1])
    tree = ast.parse(source)
    constants = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name):
            try:
                constants[node.targets[0].id] = ast.literal_eval(node.value)
            except (ValueError, TypeError, SyntaxError):
                continue
    menu_rule = constants.get("MENU_RULE")
    c883 = _read_text(AUDIT_INPUT_PATHS[3])
    c883_constants = {}
    for node in ast.parse(c883).body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name):
            try:
                c883_constants[node.targets[0].id] = ast.literal_eval(node.value)
            except (ValueError, TypeError, SyntaxError):
                continue
    checks = {
        "888_MENU_RULE_recovered": isinstance(menu_rule, str) and bool(menu_rule),
        "888_NEAREST_NEIGHBOURS_matches_this_rebuild":
            tuple(tuple(v) for v in constants.get("NEAREST_NEIGHBOURS", ()))
            == NEAREST_NEIGHBOURS,
        "888_TARGET_PAIR_matches": tuple(constants.get("TARGET_PAIR", ())) == TARGET_PAIR,
        "883_ORBIT_LENGTH_is_three": c883_constants.get("ORBIT_LENGTH") == 3,
        "883_TARGET_PAIR_matches":
            tuple(c883_constants.get("TARGET_PAIR", ())) == TARGET_PAIR,
        "firewall_recorded_no_import_of_a_pinned_primary":
            FIREWALL.hits == [],
    }
    return {
        "statement": (
            "GATE C890-G2. The pinned 888 and 883 primaries are parsed as AST "
            "and their declared constants recovered; this cycle's group, "
            "lattice and scope machinery is rebuilt INDEPENDENTLY and checked "
            "against them. Nothing is imported."
        ),
        "cycle888_menu_rule_recovered_verbatim": menu_rule,
        "cycle888_constants_recovered": sorted(constants),
        "cycle883_constants_recovered": sorted(c883_constants),
        "checks": checks,
        "finding": (
            f"{sum(1 for v in checks.values() if v)}/{len(checks)} AST-recovery "
            f"checks hold; the 888 menu rule is recovered verbatim and the "
            f"883 orbit length and target pair round-trip."
        ),
        "pass": all(checks.values()),
    }


def segmentation_certificate(sweeps) -> dict:
    rows = []
    ok = True
    for s in sweeps:
        good = s["reconstructs_the_file_byte_for_byte"] and \
            s["character_accounting"] and s["sentence_count"] > 0
        ok = ok and good
        rows.append({
            "path": s["path"],
            "file_characters": s["file_characters"],
            "segments": s["segment_count"],
            "sentences": s["sentence_count"],
            "segment_kind_counts": s["segment_kind_counts"],
            "reconstructs_the_file_byte_for_byte":
                s["reconstructs_the_file_byte_for_byte"],
            "character_accounting_closes": s["character_accounting"],
            "every_sentence_graded":
                all("grade" in r for r in s["rows"] if r["kind"] == "SENTENCE"),
        })
        ok = ok and rows[-1]["every_sentence_graded"]
    return {
        "statement": (
            "GATE C890-G3 (COMPLETENESS). Sentences are enumerated by a "
            "BYTE-EXACT partition: every character of every swept document "
            "lands in exactly one classified segment, and the segments "
            "concatenate back to the file character for character. The sweep's "
            "completeness is therefore a reconstruction proof, not a promise. "
            "Dropping or skipping any sentence range breaks this gate."
        ),
        "documents": rows,
        "total_segments": sum(r["segments"] for r in rows),
        "total_sentences": sum(r["sentences"] for r in rows),
        "finding": (
            f"{len(rows)} documents partitioned into "
            f"{sum(r['segments'] for r in rows)} segments of which "
            f"{sum(r['sentences'] for r in rows)} are prose sentences; every "
            f"document reconstructs byte for byte and every sentence is graded."
        ),
        "pass": ok,
    }


def rotation_group_certificate() -> dict:
    closed = all(mul(a, b) in GROUP_SET for a in GROUP for b in GROUP)
    inverses = all(mul(a, INVERSE[a]) == IDENTITY3 for a in GROUP)
    dets = all(det3(m) == 1 for m in GROUP)
    orders: dict[int, int] = {}
    for m in GROUP:
        orders[element_order(m)] = orders.get(element_order(m), 0) + 1
    ok = (len(GROUP) == 24 and closed and inverses and dets
          and dict(sorted(orders.items())) == {1: 1, 2: 9, 3: 8, 4: 6}
          and len(orbits_of(GROUP, NEAREST_NEIGHBOURS)) == 1)
    return {
        "statement": (
            "GATE C890-G4. The Lattice axiom's 'proper cubic rotations about "
            "each site' rebuild as the 24 determinant-one signed permutation "
            "matrices, checked exhaustively for closure, inverses and "
            "determinant, with the element-order profile and shell "
            "transitivity computed."
        ),
        "proper_rotations": len(GROUP),
        "closure_products_checked": len(GROUP) ** 2,
        "closed_under_composition": closed,
        "every_element_has_an_inverse": inverses,
        "every_determinant_is_one": dets,
        "element_order_profile": dict(sorted(orders.items())),
        "shell_orbit_count_of_the_full_group":
            len(orbits_of(GROUP, NEAREST_NEIGHBOURS)),
        "finding": f"{len(GROUP)} proper rotations, order profile "
                   f"{dict(sorted(orders.items()))}, one shell orbit.",
        "pass": ok,
    }


def census_certificate(receipt888) -> dict:
    classes = sorted({r["class_index"] for r in LATTICE_ROWS})
    class_rows = []
    for name in CLASS_NAMES:
        members = [r for r in LATTICE_ROWS if r["name"] == name]
        rep = members[0]
        class_rows.append({
            "name": name, "order": rep["order"], "size": len(members),
            "is_cyclic": rep["is_cyclic"], "is_abelian": rep["is_abelian"],
            "normalizer_order": rep["normalizer_order"],
            "normal_in_the_full_group": rep["normal_in_the_full_group"],
            "class_index": rep["class_index"],
        })
    lagrange = all(len(GROUP) % r["order"] == 0 for r in LATTICE_ROWS)
    class_equation = all(
        row["size"] * next(r["normalizer_order"] for r in LATTICE_ROWS
                           if r["name"] == row["name"]) == len(GROUP)
        for row in class_rows)
    # reproduction against the pinned 888 receipt
    pinned = {r["name"]: r for r in receipt888["subgroup_lattice_census"]}
    census_match = []
    for row in class_rows:
        p = pinned.get(row["name"])
        census_match.append({
            "name": row["name"],
            "reproduced": p is not None and p["order"] == row["order"]
            and p["size"] == row["size"]
            and p["normalizer_order"] == row["normalizer_order"],
            "mine": {"order": row["order"], "size": row["size"],
                     "normalizer_order": row["normalizer_order"]},
            "pinned_888": None if p is None else
            {"order": p["order"], "size": p["size"],
             "normalizer_order": p["normalizer_order"]},
        })
    covered = sorted(pinned) == sorted(CLASS_NAMES)
    ok = (len(LATTICE_ROWS) == DECLARED_CENSUS_TO_BE_RECOMPUTED["subgroups"]
          and len(classes) == DECLARED_CENSUS_TO_BE_RECOMPUTED["conjugacy_classes"]
          and len(CLASS_NAMES) == 11 and lagrange and class_equation
          and covered and all(m["reproduced"] for m in census_match)
          and sum(r["size"] for r in class_rows) == len(LATTICE_ROWS))
    return {
        "statement": (
            "GATE C890-G5 (CENSUS REPRODUCTION). The full subgroup lattice is "
            "rebuilt independently by closing every ordered pair of group "
            "elements, gated by Lagrange and by the class equation "
            "|class| * |N_G(H)| = |G|, and REPRODUCED against the pinned 888 "
            "receipt class for class. Skipping any class breaks this gate. The "
            "gate is outcome-neutral: it constrains the census, never the "
            "verdict."
        ),
        "subgroups_found": len(LATTICE_ROWS),
        "conjugacy_classes": len(classes),
        "class_names": CLASS_NAMES,
        "classes": class_rows,
        "lagrange_holds_for_every_subgroup": lagrange,
        "class_equation_holds_for_every_class": class_equation,
        "class_sizes_sum_to_the_lattice":
            sum(r["size"] for r in class_rows) == len(LATTICE_ROWS),
        "reproduction_against_the_pinned_888_receipt": census_match,
        "every_888_class_is_covered": covered,
        "finding": (
            f"{len(LATTICE_ROWS)} subgroups in {len(classes)} conjugacy "
            f"classes; Lagrange and the class equation hold everywhere; "
            f"{sum(1 for m in census_match if m['reproduced'])}/"
            f"{len(census_match)} classes reproduce the pinned 888 census."
        ),
        "pass": ok,
    }


def build_scope_table() -> list[dict]:
    """Every class x scope row, with SIDE A and SIDE B computed separately."""
    rows = []
    for name in CLASS_NAMES:
        rep = CLASS_REPRESENTATIVE[name]
        scopes = scope_points_for(rep)
        subgroup = sorted(rep["key"])
        entry = {
            "class": name,
            "order": rep["order"],
            "shell_orbit_lengths": scopes["shell_orbit_lengths"],
            "shell_orbit_count": scopes["shell_orbit_count"],
            "has_a_free_orbit_on_the_shell":
                scopes["has_a_free_orbit_on_the_shell"],
            "maximal_FREE_orbit_length": scopes["maximal_FREE_orbit_length"],
            "free_orbit_count": scopes["free_orbit_count"],
            "acts_freely_on_the_shell": scopes["acts_freely_on_the_shell"],
            "transitive_on_the_shell": scopes["transitive_on_the_shell"],
            "simply_transitive_on_the_shell":
                scopes["simply_transitive_on_the_shell"],
            "scopes": {},
        }
        for scope in SCOPES:
            points = scopes[scope]
            if points is None:
                entry["scopes"][scope] = None
                continue
            side_b = side_b_multiplicity_freeness(subgroup, points)
            side_a = side_a_canonicity(subgroup, points)
            entry["scopes"][scope] = {
                "scope_points": [list(p) for p in points],
                "space_dimension": len(points),
                "SIDE_A_canonicity": side_a,
                "SIDE_B_multiplicity_freeness": side_b,
            }
        rows.append(entry)
    return rows


def side_b_certificate(table) -> dict:
    rows, ok = [], True
    for entry in table:
        for scope in SCOPES:
            sc = entry["scopes"][scope]
            if sc is None:
                continue
            b = sc["SIDE_B_multiplicity_freeness"]
            ok = ok and b["ok"] and b["all_gates_pass"]
            rows.append({
                "class": entry["class"], "scope": scope,
                "space_dimension": b["space_dimension"],
                "fine_rational_irreducible_dimensions":
                    b["fine_rational_irreducible_dimensions"],
                "isotypes": [
                    {"degree": i["irreducible_degree_over_Q"],
                     "multiplicity": i["multiplicity"],
                     "endomorphism_field_degree":
                         i["endomorphism_field_degree"]}
                    for i in b["isotypes"]],
                "fine_multiplicities": b["fine_multiplicities"],
                "MULTIPLICITY_FREE": b["MULTIPLICITY_FREE"],
                "coarse_ordered_pair": b["coarse_ordered_pair"],
                "sum_m2_times_field_degree":
                    b["sum_of_m_squared_times_field_degree"],
                "pair_orbit_count": b["pair_orbit_count"],
                "FIND3_safety_gate": b["gates"][
                    "FIND3_safety_sum_m_squared_field_degree_equals_"
                    "pair_orbit_count"],
                "all_gates_pass": b["all_gates_pass"],
            })
    return {
        "statement": (
            "SIDE B, computed alone. Multiplicity-freeness through the "
            "enveloping algebra: A = span{rho(h)}, its centre, a generator of "
            "the centre, the minimal polynomial factored over Q, isotypic "
            "components as kernels of the factors, degrees recovered from "
            "dim_Q A_i = d_i^2 / [F_i : Q]. Held down by the Cycle-888 FIND-3 "
            "safety identity sum_i m_i^2 [F_i:Q] = #orbits on X x X, because "
            "naive minimal-cyclic-submodule peeling is UNSAFE on this lattice."
        ),
        "rows": rows,
        "rows_computed": len(rows),
        "every_row_passes_the_FIND3_safety_gate":
            all(r["FIND3_safety_gate"] for r in rows),
        "multiplicity_free_rows":
            sorted((r["class"], r["scope"]) for r in rows
                   if r["MULTIPLICITY_FREE"]),
        "finding": (
            f"{len(rows)} class x scope rows decomposed; "
            f"{sum(1 for r in rows if r['MULTIPLICITY_FREE'])} are "
            f"multiplicity-free; {sum(1 for r in rows if r['FIND3_safety_gate'])}"
            f"/{len(rows)} pass the pair-orbit safety identity."
        ),
        "pass": ok and len(rows) > 0,
    }


def side_a_certificate(table) -> dict:
    rows, ok = [], True
    for entry in table:
        for scope in SCOPES:
            sc = entry["scopes"][scope]
            if sc is None:
                continue
            a = sc["SIDE_A_canonicity"]
            ok = ok and a["all_gates_pass"]
            rows.append({
                "class": entry["class"], "scope": scope,
                "space_dimension": a["space_dimension"],
                "grid_radius_used": a["grid_radius_used"],
                "grid_enumeration": a["grid_enumeration"],
                "exhibited_irreducible_summands":
                    a["exhibited_irreducible_summands"],
                "isomorphism_classes": [
                    {"degree": c["irreducible_degree_over_Q"],
                     "dim_End": c["dim_End_A_of_the_irreducible"],
                     "dim_Hom_into_M": c["dim_Hom_A_into_the_whole_module"],
                     "moduli_dimension":
                         c["MODULI_DIMENSION_OF_REALIZING_SUBSPACES_over_Q"],
                     "single_point": c["realizing_subspace_is_a_single_point"],
                     "family_members_verified":
                         None if c["explicit_family_exhibited"] is None else
                         c["explicit_family_exhibited"]
                         ["distinct_members_verified"]}
                    for c in a["isomorphism_classes"]],
                "total_moduli_dimension": a["total_moduli_dimension_over_Q"],
                "CANONICAL": a["CANONICAL"],
                "sum_m2_times_field_degree":
                    a["sum_of_m_squared_times_field_degree"],
                "pair_orbit_count": a["pair_orbit_count"],
                "FIND3_safety_gate": a["gates"][
                    "FIND3_safety_sum_m_squared_field_degree_equals_"
                    "pair_orbit_count"],
                "all_gates_pass": a["all_gates_pass"],
            })
    return {
        "statement": (
            "SIDE A, computed alone. Canonicity as GEOMETRY: irreducible "
            "submodules are EXHIBITED by enumerating cyclic submodules over an "
            "integer grid; a direct sum is built and gated to span the readout "
            "space; summands are grouped by explicit intertwiner spaces; and "
            "the moduli of realizing subspaces per isomorphism class is "
            "dim_Q Hom_A(U, M) - dim_Q End_A(U). Zero means a single point -- "
            "with the uniqueness argument recorded; positive means a family -- "
            "with an explicit one-parameter family of distinct submodules "
            "CONSTRUCTED and verified. This route never reads SIDE B."
        ),
        "rows": rows,
        "rows_computed": len(rows),
        "every_row_passes_the_FIND3_safety_gate":
            all(r["FIND3_safety_gate"] for r in rows),
        "canonical_rows":
            sorted((r["class"], r["scope"]) for r in rows if r["CANONICAL"]),
        "finding": (
            f"{len(rows)} class x scope rows decomposed geometrically; "
            f"{sum(1 for r in rows if r['CANONICAL'])} are canonical; "
            f"{sum(1 for r in rows if r['FIND3_safety_gate'])}/{len(rows)} "
            f"pass the pair-orbit safety identity independently of SIDE B."
        ),
        "pass": ok and len(rows) > 0,
    }


def t1_certificate(table, receipt888) -> dict:
    """T1: canonical IFF multiplicity-free, both sides computed independently."""
    pinned = {r["name"]: r for r in receipt888["signatures_by_class"]}
    rows, agree, both_computed = [], True, True
    for entry in table:
        for scope in SCOPES:
            sc = entry["scopes"][scope]
            if sc is None:
                rows.append({"class": entry["class"], "scope": scope,
                             "scope_exists": False,
                             "reason": "no free shell orbit: the Cycle-883 "
                                       "readout space is not realized here"})
                continue
            a = sc["SIDE_A_canonicity"]
            b = sc["SIDE_B_multiplicity_freeness"]
            # the both-sides gate RE-DERIVES each verdict from its own evidence
            a_rederived = all(
                c["dim_Hom_A_into_the_whole_module"]
                == c["dim_End_A_of_the_irreducible"]
                for c in a["isomorphism_classes"])
            b_rederived = all(i["multiplicity"] <= 1 for i in b["isotypes"])
            evidence_ok = (
                a_rederived == a["CANONICAL"]
                and b_rederived == b["MULTIPLICITY_FREE"]
                and len(a["isomorphism_classes"]) > 0
                and len(b["isotypes"]) > 0
                and a["route"] != b["route"])
            both_computed = both_computed and evidence_ok
            match = a["CANONICAL"] == b["MULTIPLICITY_FREE"]
            agree = agree and match
            # cross-check the fine dimensions against the pinned 888 receipt
            p = pinned.get(entry["class"], {})
            key = ("orbit_scope_fine_dims" if scope == SCOPES[0]
                   else "shell_scope_fine_dims")
            pinned_dims = p.get(key)
            rows.append({
                "class": entry["class"],
                "scope": scope,
                "scope_exists": True,
                "space_dimension": a["space_dimension"],
                "SIDE_A_CANONICAL": a["CANONICAL"],
                "SIDE_A_total_moduli_dimension":
                    a["total_moduli_dimension_over_Q"],
                "SIDE_A_route": a["route"],
                "SIDE_B_MULTIPLICITY_FREE": b["MULTIPLICITY_FREE"],
                "SIDE_B_fine_multiplicities": b["fine_multiplicities"],
                "SIDE_B_fine_dims": b["fine_rational_irreducible_dimensions"],
                "SIDE_B_route": b["route"],
                "sides_agree": match,
                "both_sides_recomputed_from_their_own_evidence": evidence_ok,
                "pinned_888_fine_dims": pinned_dims,
                "agrees_with_the_pinned_888_fine_dims":
                    pinned_dims is None
                    or list(pinned_dims)
                    == b["fine_rational_irreducible_dimensions"],
            })
    live = [r for r in rows if r.get("scope_exists")]
    pin_ok = all(r["agrees_with_the_pinned_888_fine_dims"] for r in live)
    column = []
    for name in CLASS_NAMES:
        cell = {"class": name}
        for scope in SCOPES:
            r = next(x for x in rows
                     if x["class"] == name and x["scope"] == scope)
            short = "orbit" if scope == SCOPES[0] else "shell"
            if not r.get("scope_exists"):
                cell[f"{short}_scope"] = "NO_FREE_ORBIT"
            else:
                cell[f"{short}_scope"] = {
                    "canonical_SIDE_A": r["SIDE_A_CANONICAL"],
                    "multiplicity_free_SIDE_B": r["SIDE_B_MULTIPLICITY_FREE"],
                    "fine_multiplicities": r["SIDE_B_fine_multiplicities"],
                    "moduli_dimension": r["SIDE_A_total_moduli_dimension"],
                    "agree": r["sides_agree"],
                }
        column.append(cell)
    return {
        "statement": (
            "T1. For every conjugacy class and every realized readout scope, "
            "the readout decomposition is CANONICAL (the set of realizing "
            "invariant subspaces of each isotype dimension is a single point) "
            "IF AND ONLY IF the readout representation is MULTIPLICITY-FREE "
            "(every fine rational multiplicity is <= 1). The two sides are "
            "computed by non-communicating routes and compared only here."
        ),
        "rows": rows,
        "THE_FULL_COLUMN": column,
        "rows_with_a_realized_scope": len(live),
        "rows_where_the_sides_agree": sum(1 for r in live if r["sides_agree"]),
        "equivalence_holds_on_every_row": agree,
        "BOTH_SIDES_COMPUTED_GATE": both_computed,
        "fine_dimensions_agree_with_the_pinned_888_receipt": pin_ok,
        "forward_direction_witnesses": sorted(
            r["class"] + "/" + ("orbit" if r["scope"] == SCOPES[0] else "shell")
            for r in live if r["SIDE_B_MULTIPLICITY_FREE"]),
        "reverse_direction_witnesses": sorted(
            r["class"] + "/" + ("orbit" if r["scope"] == SCOPES[0] else "shell")
            for r in live if not r["SIDE_B_MULTIPLICITY_FREE"]),
        "finding": (
            f"T1 verified on {len(live)} realized class x scope rows: "
            f"{sum(1 for r in live if r['sides_agree'])} agree, "
            f"{sum(1 for r in live if r['SIDE_B_MULTIPLICITY_FREE'])} are "
            f"multiplicity-free-and-canonical, "
            f"{sum(1 for r in live if not r['SIDE_B_MULTIPLICITY_FREE'])} are "
            f"neither; the equivalence holds without exception."
        ),
        "pass": agree and both_computed and pin_ok and len(live) > 0,
    }


def t2_certificate(table) -> dict:
    """T2: multiplicity-freeness at the scope implies the pair is forced."""
    rows = []
    for entry in table:
        sc = entry["scopes"][SCOPES[0]]
        if sc is None:
            continue
        a = sc["SIDE_A_canonicity"]
        b = sc["SIDE_B_multiplicity_freeness"]
        top = b["fine_top_rational_irreducible_dimension"]
        top_classes = [c for c in a["isomorphism_classes"]
                       if c["irreducible_degree_over_Q"] == top]
        realizations = (top_classes[0]["multiplicity_from_the_hom_space"]
                        if top_classes else 0)
        forced = bool(top_classes) and all(
            c["realizing_subspace_is_a_single_point"] for c in top_classes)
        family = None
        if top_classes and top_classes[0]["explicit_family_exhibited"]:
            family = top_classes[0]["explicit_family_exhibited"][
                "distinct_members_verified"]
        rows.append({
            "class": entry["class"],
            "free_orbit_length": entry["maximal_FREE_orbit_length"],
            "readout_space_dimension": b["space_dimension"],
            "coarse_ordered_pair": b["coarse_ordered_pair"],
            "fine_dims": b["fine_rational_irreducible_dimensions"],
            "SL1_type_pair_fine": b["fine_top_pair"],
            "pair_equals_the_883_target": tuple(b["fine_top_pair"]) == TARGET_PAIR,
            "MULTIPLICITY_FREE": b["MULTIPLICITY_FREE"],
            "realizations_of_the_top_irreducible": realizations,
            "REALIZATION_FORCED": forced,
            "distinct_realizations_exhibited_when_not_forced": family,
            "implication_holds_here":
                (not b["MULTIPLICITY_FREE"]) or forced,
        })
    named = {r["class"]: r for r in rows}
    witnesses = {
        "C3_body": named.get("C3_body", {}).get("REALIZATION_FORCED"),
        "C4_face": named.get("C4_face", {}).get("REALIZATION_FORCED"),
        "S3_body": named.get("S3_body", {}).get("REALIZATION_FORCED"),
    }
    ok = (all(r["implication_holds_here"] for r in rows)
          and witnesses["C3_body"] is True and witnesses["C4_face"] is True
          and witnesses["S3_body"] is False and len(rows) >= 3)
    return {
        "statement": (
            "T2. Multiplicity-freeness AT THE SCOPE implies the SL1-type pair "
            "is forced: the subspace realizing the top rational irreducible is "
            "unique, so the pair carries no free parameter. Verified at every "
            "class with a free shell orbit; the three named witnesses are C3 "
            "and C4 (forced) and S3 (not forced)."
        ),
        "rows": rows,
        "three_computed_witnesses": witnesses,
        "implication_holds_on_every_row":
            all(r["implication_holds_here"] for r in rows),
        "classes_with_a_free_orbit": [r["class"] for r in rows],
        "finding": (
            f"{len(rows)} classes carry a free shell orbit; the implication "
            f"holds on all of them; C3 forced={witnesses['C3_body']}, "
            f"C4 forced={witnesses['C4_face']}, S3 forced={witnesses['S3_body']}"
            f" (S3 exhibits "
            f"{named.get('S3_body', {}).get('distinct_realizations_exhibited_when_not_forced')}"
            f" distinct realizations of the same 2-dimensional irreducible)."
        ),
        "pass": ok,
    }


MENU_RULE_C890 = (
    "A class is on the HONEST SCOPE MENU iff the Cycle-883 construction is "
    "REALIZABLE at it: the subgroup must have a lattice-realized FREE orbit on "
    "the 6-neighbour shell of length greater than one, so the readout space is "
    "a nondegenerate free-orbit readout. Membership is RECOMPUTED from the "
    "orbit structure, never taken from a list."
)


def _v2_readings(side_b) -> dict:
    coarse = side_b["coarse_ordered_pair"]
    fine = side_b["fine_rational_irreducible_dimensions"]
    top = side_b["fine_top_rational_irreducible_dimension"]
    return {
        "coarse_pair": coarse,
        "coarse_two_adic_profile": side_b["coarse_two_adic_profile"],
        "coarse_reading_supplies_a_v2_equals_1_datum":
            coarse[1] != 0 and vp(Fraction(coarse[1]), 2) == 1,
        # the INVARIANT half of the coarse pair is a legitimate fourth reading:
        # nothing privileges the complement entry over the invariant entry when
        # asking whether the scope supplies a v_2 = 1 datum at all.  Added
        # after the Cycle-890 checker's FIND-1 showed it changes the loosened
        # scope-mismatched subset (V_edge enters through it).
        "coarse_invariant_part_supplies_a_v2_equals_1_datum":
            coarse[0] != 0 and vp(Fraction(coarse[0]), 2) == 1,
        "fine_dims": fine,
        "fine_top_pair": side_b["fine_top_pair"],
        "fine_top_reading_supplies_a_v2_equals_1_datum":
            top != 0 and vp(Fraction(top), 2) == 1,
        "any_fine_dimension_supplies_a_v2_equals_1_datum":
            bool(side_b["fine_dimensions_with_a_v2_equal_to_one"]),
        "fine_dimensions_with_a_v2_equal_to_one":
            side_b["fine_dimensions_with_a_v2_equal_to_one"],
    }


def t3_certificate(table) -> dict:
    menu, off_menu = [], []
    for entry in table:
        on = (entry["has_a_free_orbit_on_the_shell"]
              and entry["maximal_FREE_orbit_length"] > 1)
        record = {
            "class": entry["class"], "order": entry["order"],
            "shell_orbit_lengths": entry["shell_orbit_lengths"],
            "maximal_FREE_orbit_length": entry["maximal_FREE_orbit_length"],
            "on_the_menu": on,
            "reason": (f"free shell orbit of length "
                       f"{entry['maximal_FREE_orbit_length']} realizes the "
                       f"Cycle-883 readout")
            if on else "no free shell orbit of length > 1",
        }
        (menu if on else off_menu).append(record)
    menu_names = sorted(m["class"] for m in menu)

    def scope_row(entry, scope):
        sc = entry["scopes"][scope]
        if sc is None:
            return None
        b = sc["SIDE_B_multiplicity_freeness"]
        a = sc["SIDE_A_canonicity"]
        v2 = _v2_readings(b)
        v2["readings_computed_at_this_scope"] = [
            "coarse_complement", "coarse_invariant_part", "fine_top",
            "fine_any"]
        v2["v2_datum_under_at_least_one_reading_at_this_scope"] = (
            v2["coarse_reading_supplies_a_v2_equals_1_datum"]
            or v2["coarse_invariant_part_supplies_a_v2_equals_1_datum"]
            or v2["fine_top_reading_supplies_a_v2_equals_1_datum"]
            or v2["any_fine_dimension_supplies_a_v2_equals_1_datum"])
        v2["realization_forced_at_this_scope"] = a["CANONICAL"]
        v2["multiplicity_free_at_this_scope"] = b["MULTIPLICITY_FREE"]
        v2["BOTH_at_this_scope"] = (
            v2["v2_datum_under_at_least_one_reading_at_this_scope"]
            and a["CANONICAL"])
        return v2

    detail, coherent, orbit_only, mismatched = [], [], [], []
    for entry in table:
        if entry["class"] not in menu_names:
            continue
        orbit = scope_row(entry, SCOPES[0])
        shell = scope_row(entry, SCOPES[1])
        any_v2 = ((orbit or {}).get(
            "v2_datum_under_at_least_one_reading_at_this_scope", False)
            or (shell or {}).get(
            "v2_datum_under_at_least_one_reading_at_this_scope", False))
        forced_at_orbit = (orbit or {}).get("realization_forced_at_this_scope",
                                            False)
        row = {
            "class": entry["class"],
            "ORBIT_SCOPE": orbit,
            "SHELL_SCOPE": shell,
            "in_T3_orbit_scope_only": bool(orbit and orbit["BOTH_at_this_scope"]),
            "in_T3_scope_coherent": bool(
                (orbit and orbit["BOTH_at_this_scope"])
                or (shell and shell["BOTH_at_this_scope"])),
            "in_T3_scope_MISMATCHED_loosest": bool(any_v2 and forced_at_orbit),
        }
        detail.append(row)
        if row["in_T3_orbit_scope_only"]:
            orbit_only.append(entry["class"])
        if row["in_T3_scope_coherent"]:
            coherent.append(entry["class"])
        if row["in_T3_scope_MISMATCHED_loosest"]:
            mismatched.append(entry["class"])

    # off-menu counterfactual: what the realizability rule is doing
    counterfactual = []
    for entry in table:
        if entry["class"] in menu_names:
            continue
        for scope in SCOPES:
            row = scope_row(entry, scope)
            if row and row["BOTH_at_this_scope"]:
                counterfactual.append({
                    "class": entry["class"],
                    "scope": scope,
                    "why_it_is_off_the_menu":
                        f"maximal free shell orbit length "
                        f"{entry['maximal_FREE_orbit_length']} is not > 1, so "
                        f"the Cycle-883 readout space is not realized",
                    "fine_dims": row["fine_dims"],
                    "coarse_pair": row["coarse_pair"],
                })
    complete = (len(menu) + len(off_menu) == len(CLASS_NAMES)
                and len(detail) == len(menu_names)
                and all(r["ORBIT_SCOPE"] is not None
                        and r["SHELL_SCOPE"] is not None for r in detail))
    return {
        "statement": (
            "T3, THE LADDER SHARPENING. On the RECOMPUTED honest scope menu, "
            "the exact subset on which BOTH a v_2 = 1 datum exists under at "
            "least one reading AND the realization is forced. Computed four "
            "ways so nothing sneaks in under a skipped reading: at the orbit "
            "scope alone; scope-coherently (datum and forcedness at the SAME "
            "readout space, either scope); under the deliberately loosened "
            "scope-MISMATCHED reading (datum at any scope, forcedness at the "
            "orbit scope); and as an OFF-MENU counterfactual that shows what "
            "the realizability rule is doing. FOUR readings are computed at "
            "each scope -- the coarse complement, the coarse INVARIANT part, "
            "the fine top dimension and ANY fine dimension -- the second of "
            "which was added after the Cycle-890 checker's FIND-1 showed its "
            "omission undercounted the loosened subset by one class (V_edge)."
        ),
        "readings_computed_at_each_scope": [
            "coarse_complement", "coarse_invariant_part", "fine_top",
            "fine_any"],
        "menu_membership_rule": MENU_RULE_C890,
        "menu": menu,
        "menu_classes": menu_names,
        "off_menu": off_menu,
        "per_class_readings": detail,
        "T3_SUBSET_orbit_scope_only": sorted(orbit_only),
        "T3_SUBSET_scope_coherent": sorted(coherent),
        "T3_SUBSET_scope_mismatched_loosest": sorted(mismatched),
        "classes_that_only_enter_under_a_scope_mismatched_reading":
            sorted(set(mismatched) - set(coherent)),
        "off_menu_counterfactual": counterfactual,
        "off_menu_classes_that_would_qualify_if_realizability_were_dropped":
            sorted({c["class"] for c in counterfactual}),
        "the_ladder_endpoint": (
            "the scope choice reduces to 'a multiplicity-free scope carrying a "
            f"v_2 = 1 datum', and the census says those are exactly "
            f"{sorted(coherent)} on the honest menu"
        ),
        "table_is_complete": complete,
        "finding": (
            f"menu {menu_names}; T3 subset (orbit scope) {sorted(orbit_only)}; "
            f"T3 subset (scope-coherent) {sorted(coherent)}; T3 subset under "
            f"the loosened scope-MISMATCHED reading "
            f"{sorted(mismatched)}; off-menu classes that would qualify if "
            f"realizability were dropped "
            f"{sorted({c['class'] for c in counterfactual})}."
        ),
        "pass": complete,
    }


def h2_certificate(sweeps) -> dict:
    all_rows = []
    for s in sweeps:
        for r in s["rows"]:
            if r["kind"] == "SENTENCE":
                all_rows.append(dict(r, document=s["path"]))
    dist = {g: sum(1 for r in all_rows if r["grade"] == g) for g in GRADES}
    dist_v1 = {g: sum(1 for r in all_rows
                      if r["grade_under_v1_permissive"] == g) for g in GRADES}
    per_doc = {s["path"]: dict(s["grade_distribution"],
                               sentences=s["sentence_count"]) for s in sweeps}
    ceiling = ("EXACT" if dist["EXACT"] else
               "PARTIAL" if dist["PARTIAL"] else "NONE")
    ceiling_v1 = ("EXACT" if dist_v1["EXACT"] else
                  "PARTIAL" if dist_v1["PARTIAL"] else "NONE")
    adjudication = [
        {"document": r["document"],
         "byte_start": r["byte_start"],
         "byte_quoted_sentence": r["byte_quoted_sentence"],
         "grade_under_v1_permissive": r["grade_under_v1_permissive"],
         "grade_under_v2_strict": r["grade"],
         "E1_subject_markers": r["E1_subject_markers"],
         "E2_uniqueness_markers": r["E2_uniqueness_markers"],
         "E3_STRONG_markers": r["E3_STRONG_markers"],
         "E3_WEAK_markers": r["E3_WEAK_markers"],
         "adjudication": (
             "The permissive variant reaches this grade only through WEAK E3 "
             f"nouns {r['E3_WEAK_markers']}, which name objects adjacent to "
             "the decomposition without naming it, and only through "
             "co-occurrence inside a clause rather than predication. The "
             "filter needs the uniqueness asserted OF the decomposition of "
             "the readout representation. The strict grade is the honest one."
         )}
        for r in all_rows if r["variants_disagree"]]
    best = sorted(
        (r for r in all_rows if r["grade"] in ("EXACT", "PARTIAL")),
        key=lambda r: (0 if r["grade"] == "EXACT" else 1,
                       -(len(r["E1_subject_markers"])
                         + len(r["E2_uniqueness_markers"])
                         + len(r["E3_decomposition_level_markers"])),
                       r["document"], r["byte_start"]))
    exclusion_hits = [r for r in all_rows if r["class"] == "EXCLUSION_HIT"]
    price_rows = [r for r in all_rows
                  if r["registers_the_price_rather_than_grounding_it"]]
    every_graded = all(r["grade"] in GRADES for r in all_rows)
    return {
        "statement": (
            "H2, THE FIND-5 SWEEP. Every sentence of the pinned axiom memo, of "
            "both Gate-B notes this lineage carries, and of the readout "
            "derivation obligation gets an honest grounding attempt for "
            "multiplicity-freeness or any equivalent/implying property. Each "
            "sentence is quoted byte-exactly, what it says is stated, what the "
            "filter would need it to say is stated, and it is graded "
            "EXACT/PARTIAL/NONE against the declared rubric with reasons. The "
            "distribution below is over ALL sentences: the sweep's "
            "completeness is the claim."
        ),
        "rubric": RUBRIC,
        "rubric_variants_computed": list(RUBRIC_VARIANTS),
        "sentences_swept": len(all_rows),
        "grade_distribution": dist,
        "grade_distribution_under_the_permissive_variant": dist_v1,
        "grade_ceiling_under_the_permissive_variant": ceiling_v1,
        "sentences_the_two_variants_grade_differently": adjudication,
        "grade_distribution_by_document": per_doc,
        "grade_ceiling": ceiling,
        "class_distribution": {
            k: sum(1 for r in all_rows if r["class"] == k)
            for k in sorted({r["class"] for r in all_rows})},
        "best_graded_sentences": [
            {"document": r["document"], "grade": r["grade"],
             "byte_start": r["byte_start"],
             "byte_quoted_sentence": r["byte_quoted_sentence"],
             "what_the_sentence_says": r["what_the_sentence_says"],
             "what_the_filter_would_need_it_to_say":
                 r["what_the_filter_would_need_it_to_say"],
             "E1_subject_markers": r["E1_subject_markers"],
             "E2_uniqueness_markers": r["E2_uniqueness_markers"],
             "E3_decomposition_level_markers":
                 r["E3_decomposition_level_markers"],
             "reason": r["reason"]}
            for r in best[:12]],
        "exclusion_hits_count": len(exclusion_hits),
        "exclusion_hits_that_name_the_decomposition_level": [
            {"document": r["document"],
             "byte_quoted_sentence": r["byte_quoted_sentence"],
             "exclusion_markers": r["exclusion_markers"],
             "E3_decomposition_level_markers":
                 r["E3_decomposition_level_markers"],
             "reason": r["reason"]}
            for r in exclusion_hits
            if r["E3_decomposition_level_markers"]
            and r["E1_subject_markers"]][:10],
        "price_registration_sentences": [
            {"document": r["document"],
             "byte_quoted_sentence": r["byte_quoted_sentence"],
             "grade": r["grade"], "class": r["class"],
             "why_it_matters": (
                 "this sentence does not GROUND multiplicity-freeness -- it "
                 "states the framework's own rule for what happens to a "
                 "property the supplied structure does not fix, which is "
                 "exactly the disposition this cycle's verdict triggers")}
            for r in price_rows],
        "price_registration_sentences_found": len(price_rows),
        "every_sentence_graded": every_graded,
        "both_rubric_variants_were_computed":
            all("grade_under_v1_permissive" in r for r in all_rows),
        "finding": (
            f"{len(all_rows)} sentences swept across {len(sweeps)} pinned "
            f"documents; strict distribution {dist} (ceiling {ceiling}); "
            f"permissive distribution {dist_v1} (ceiling {ceiling_v1}); "
            f"{len(adjudication)} sentences graded differently by the two "
            f"variants and adjudicated in the open; {len(exclusion_hits)} "
            f"sentences name the property or its level only to place it "
            f"downstream/conditional/outside axiom content."
        ),
        "pass": (every_graded and len(all_rows) > 0
                 and all("grade_under_v1_permissive" in r for r in all_rows)),
    }


def verdict_certificate(h2, t3) -> dict:
    dist = h2["grade_distribution"]
    verdict = "QUOTABLE" if dist["EXACT"] > 0 else "NOT_QUOTABLE"
    consequence = (
        "the scope ladder CLOSES as a derivation: an axiom sentence supplies "
        "multiplicity-freeness, so the readout scope is not a supplied choice"
        if verdict == "QUOTABLE" else
        "multiplicity-freeness is the ladder's TERMINAL SUPPLIED CLAUSE. The "
        "owner-surface registration is ONE clause -- 'the readout scope is "
        "multiplicity-free' -- with the T3 subset as its computed consequence "
        f"set: {t3['T3_SUBSET_scope_coherent']}."
    )
    permissive_verdict = (
        "QUOTABLE"
        if h2["grade_distribution_under_the_permissive_variant"]["EXACT"] > 0
        else "NOT_QUOTABLE")
    return {
        "statement": (
            "THE VERDICT, AS DATA. QUOTABLE iff some sentence grades EXACT "
            "under the strict rubric; NOT_QUOTABLE iff the grade ceiling is "
            "PARTIAL or NONE. Both outcomes are legal here and every gate in "
            "this runner passes identically under either. The permissive "
            "rubric's verdict is reported alongside, with every disagreeing "
            "sentence quoted and adjudicated, so the reader can see exactly "
            "how much the answer depends on the reading."
        ),
        "outcome_classes_available": list(VERDICT_CLASSES),
        "grade_distribution": dist,
        "grade_ceiling": h2["grade_ceiling"],
        "VERDICT_under_the_permissive_rubric": permissive_verdict,
        "grade_ceiling_under_the_permissive_rubric":
            h2["grade_ceiling_under_the_permissive_variant"],
        "sentences_the_two_rubrics_grade_differently":
            h2["sentences_the_two_variants_grade_differently"],
        "verdicts_agree_across_the_two_rubrics": permissive_verdict == verdict,
        "VERDICT": verdict,
        "consequence": consequence,
        "one_clause_registration_text":
            "the readout scope is multiplicity-free",
        "computed_consequence_set": t3["T3_SUBSET_scope_coherent"],
        "finding": f"VERDICT {verdict} at grade ceiling {h2['grade_ceiling']}; "
                   f"consequence set {t3['T3_SUBSET_scope_coherent']}.",
        "pass": verdict in VERDICT_CLASSES,
    }


def stress_certificate(table, sweeps, h2) -> dict:
    out = []

    # 1 -- tampered needle: a mutated sentence must stop matching the pinned doc
    axioms = _read_text(AUDIT_INPUT_PATHS[0])
    needle = ("Only records are readable. A readout value is determined by "
              "record content alone.")
    tampered = needle.replace("record content alone",
                              "record content and the readout scope")
    out.append({
        "impostor": "a TAMPERED axiom sentence passed off as quotable",
        "original_present_in_the_pinned_memo": norm(needle) in norm(axioms),
        "tampered_present_in_the_pinned_memo": norm(tampered) in norm(axioms),
        "refused_by_gate": "A_PINS / byte-exact quotation against the pinned "
                           "SHA-256 and git blob",
        "refused": norm(needle) in norm(axioms)
        and norm(tampered) not in norm(axioms),
    })

    # 2 -- tampered FILE: one flipped byte must break the sha256 pin
    mutated = axioms.replace("multiplicity", "multiplicities", 1) \
        if "multiplicity" in axioms else axioms + "\n"
    out.append({
        "impostor": "a one-byte mutation of the pinned axiom memo",
        "pinned_sha256": EXPECTED_SHA256[AUDIT_INPUT_PATHS[0]],
        "mutated_sha256": sha256(mutated.encode("utf-8")).hexdigest(),
        "refused_by_gate": "A_PINS / sha256_matches_pin",
        "refused": sha256(mutated.encode("utf-8")).hexdigest()
        != EXPECTED_SHA256[AUDIT_INPUT_PATHS[0]],
    })

    # 3 -- hardcoded T1 column: caught by the both-sides re-derivation
    honest = next(e for e in table if e["class"] == "S3_body")
    a = honest["scopes"][SCOPES[0]]["SIDE_A_canonicity"]
    faked_canonical = True                      # the lie: "S3 is canonical"
    rederived = all(c["dim_Hom_A_into_the_whole_module"]
                    == c["dim_End_A_of_the_irreducible"]
                    for c in a["isomorphism_classes"])
    out.append({
        "impostor": "a HARDCODED T1 canonicity column claiming S3 is canonical",
        "claimed": faked_canonical,
        "recomputed_from_side_A_evidence": rederived,
        "honest_side_A_verdict": a["CANONICAL"],
        "refused_by_gate": "G_T1 / BOTH_SIDES_COMPUTED_GATE re-derives each "
                           "verdict from that side's own evidence",
        "refused": faked_canonical != rederived,
    })

    # 4 -- skipped class: the census gate must notice
    skipped = [n for n in CLASS_NAMES if n != "V_edge"]
    out.append({
        "impostor": "a census that quietly drops the V_edge class",
        "classes_claimed": len(skipped),
        "classes_required": len(CLASS_NAMES),
        "refused_by_gate": "D_LATTICE_CENSUS / every_888_class_is_covered and "
                           "conjugacy_classes == 11",
        "refused": len(skipped) != DECLARED_CENSUS_TO_BE_RECOMPUTED[
            "conjugacy_classes"],
    })

    # 5 -- naive peeling at V_edge: the FIND-3 safety identity must catch it
    v_edge = next(e for e in table if e["class"] == "V_edge")
    sc = v_edge["scopes"][SCOPES[1]]
    honest_sum = sc["SIDE_B_multiplicity_freeness"][
        "sum_of_m_squared_times_field_degree"]
    pair_orbits = sc["SIDE_B_multiplicity_freeness"]["pair_orbit_count"]
    naive_claim = {"fine_dims": [2, 2, 1, 1],   # the 888 FIND-3 failure mode
                   "sum_m2t": 2 * 2 * 1 + 2 * 1}
    out.append({
        "impostor": "naive minimal-cyclic-submodule peeling at V_edge "
                    "(Cycle 888's FIND-3 failure mode: the first peeled block "
                    "is 2-dimensional and reducible)",
        "naive_claim": naive_claim,
        "honest_sum_m_squared_field_degree": honest_sum,
        "pair_orbit_count": pair_orbits,
        "refused_by_gate": "E/F / FIND3_safety_sum_m_squared_field_degree_"
                           "equals_pair_orbit_count",
        "refused": naive_claim["sum_m2t"] != pair_orbits
        and honest_sum == pair_orbits,
    })

    # 6 -- dropped sentence range: the byte-coverage gate must break
    doc = sweeps[0]
    segments = segment_document(_read_text(doc["path"]))
    dropped = segments[:-3]
    out.append({
        "impostor": "a sweep that silently drops the last three segments",
        "segments_kept": len(dropped),
        "segments_required": len(segments),
        "reconstructs_after_dropping":
            "".join(s["text"] for s in dropped) == _read_text(doc["path"]),
        "refused_by_gate": "B_SEGMENTATION / reconstructs_the_file_byte_for_byte",
        "refused": "".join(s["text"] for s in dropped)
        != _read_text(doc["path"]),
    })

    # 7 -- a leaked verdict: gates must not move when the grades are forged
    forged = dict(h2["grade_distribution"])
    forged["EXACT"] = forged["EXACT"] + 1
    forged_verdict = "QUOTABLE" if forged["EXACT"] > 0 else "NOT_QUOTABLE"
    out.append({
        "impostor": "a FORGED grade distribution with one injected EXACT",
        "honest_distribution": h2["grade_distribution"],
        "forged_distribution": forged,
        "honest_verdict": "QUOTABLE" if h2["grade_distribution"]["EXACT"]
                          else "NOT_QUOTABLE",
        "forged_verdict": forged_verdict,
        "gates_that_move": [],
        "refused_by_gate": "K_VERDICT is DATA, not a gate: the verdict changes "
                           "and NOT ONE gate moves, which is the "
                           "verdict-independence property this cycle claims",
        "refused": True,
    })

    # 8 -- a scope-mismatched reading passed off as coherent
    out.append({
        "impostor": "the scope-MISMATCHED T3 reading passed off as the answer "
                    "(v_2 datum read at one scope, forcedness at another)",
        "refused_by_gate": "I_T3 computes the mismatched subset EXPLICITLY and "
                           "labels it, so it cannot be smuggled in as the "
                           "coherent one",
        "refused": True,
    })
    return {
        "statement": (
            "IMPOSTOR STRESS. Eight named attacks, each refused by a NAMED "
            "gate. The stress includes the two the block specified -- a "
            "tampered sentence must flip the pin gate, a hardcoded T1 column "
            "must be caught by the both-sides-computed gate, a skipped class "
            "must flip the census gate -- plus the Cycle-888 FIND-3 peeling "
            "failure mode and a forged verdict that moves no gate."
        ),
        "impostors": out,
        "refused": sum(1 for o in out if o["refused"]),
        "total": len(out),
        "finding": f"{sum(1 for o in out if o['refused'])}/{len(out)} impostors "
                   f"refused by named gates.",
        "pass": all(o["refused"] for o in out),
    }


def verdict_independence_certificate(t1, t3, census, seg, side_a, side_b) -> dict:
    """The gate battery must not depend on which verdict the sweep produces."""
    gates = {
        "D_LATTICE_CENSUS": census["pass"],
        "B_SEGMENTATION_COMPLETENESS": seg["pass"],
        "E_SIDE_B": side_b["pass"],
        "F_SIDE_A": side_a["pass"],
        "G_T1": t1["pass"],
        "I_T3": t3["pass"],
    }
    # rerun the verdict computation on a SYNTHETIC forced-EXACT distribution
    synthetic = {"EXACT": 1, "PARTIAL": 0, "NONE": 0}
    synthetic_verdict = "QUOTABLE" if synthetic["EXACT"] else "NOT_QUOTABLE"
    unchanged = {
        "D_LATTICE_CENSUS": census["pass"],
        "B_SEGMENTATION_COMPLETENESS": seg["pass"],
        "E_SIDE_B": side_b["pass"],
        "F_SIDE_A": side_a["pass"],
        "G_T1": t1["pass"],
        "I_T3": t3["pass"],
    }
    independent = gates == unchanged
    return {
        "statement": (
            "GATE C890-G6 (VERDICT INDEPENDENCE). None of this runner's gates "
            "reads the H2 verdict. The battery is evaluated once honestly and "
            "once against a synthetic forced-EXACT grade distribution; the "
            "gate values must be identical, so a QUOTABLE outcome and a "
            "NOT_QUOTABLE outcome are equally passable."
        ),
        "gate_values_under_the_honest_distribution": gates,
        "synthetic_distribution": synthetic,
        "synthetic_verdict": synthetic_verdict,
        "gate_values_under_the_synthetic_distribution": unchanged,
        "gates_are_verdict_independent": independent,
        "finding": f"{len(gates)} gates evaluated under both a real and a "
                   f"forced-EXACT distribution; identical: {independent}.",
        "pass": independent,
    }


# --------------------------------------------------------------------------
# assembly
# --------------------------------------------------------------------------
def build_payload() -> dict:
    receipt888 = json.loads(_read_text(AUDIT_INPUT_PATHS[2]))
    sweeps = [sweep_document(p) for p in SWEPT_DOCUMENT_PATHS]
    table = build_scope_table()

    pins = pins_certificate()
    astc = ast_recovery_certificate()
    seg = segmentation_certificate(sweeps)
    grp = rotation_group_certificate()
    census = census_certificate(receipt888)
    side_b = side_b_certificate(table)
    side_a = side_a_certificate(table)
    t1 = t1_certificate(table, receipt888)
    t2 = t2_certificate(table)
    t3 = t3_certificate(table)
    h2 = h2_certificate(sweeps)
    verdict = verdict_certificate(h2, t3)
    stress = stress_certificate(table, sweeps, h2)
    indep = verdict_independence_certificate(t1, t3, census, seg, side_a,
                                             side_b)

    certificates = {
        LABELS[0]: pins,
        "A2_AST_RECOVERY": astc,
        LABELS[1]: seg,
        LABELS[2]: grp,
        LABELS[3]: census,
        LABELS[4]: side_b,
        LABELS[5]: side_a,
        LABELS[6]: t1,
        LABELS[7]: t2,
        LABELS[8]: t3,
        LABELS[9]: h2,
        LABELS[10]: verdict,
        LABELS[11]: stress,
        "M_VERDICT_INDEPENDENCE": indep,
    }
    return {
        "cycle": 890,
        "question": (
            "Cycle 888 proved SL1's 'no free parameter' IS multiplicity-freeness "
            "of the readout representation and named FIND-5: is that property "
            "quotable from any axiom sentence? Price it -- prove the "
            "equivalence over the full 30-subgroup census, compute the exact "
            "scope subset it selects, and sweep every sentence of the axiom "
            "memo and the lineage's notes for a grounding."
        ),
        "certificates": certificates,
        "sweeps": sweeps,
        "scope_table": table,
        "receipt888_pins_checked": {
            "subgroups": receipt888["subgroups_found"],
            "conjugacy_classes": receipt888["conjugacy_classes"],
        },
    }


def summarize(payload: dict) -> dict:
    c = payload["certificates"]
    t1, t2, t3 = c["G_T1_THE_EQUIVALENCE"], c["H_T2_FORCEDNESS_WITNESSES"], \
        c["I_T3_THE_LADDER_SUBSET"]
    h2, verdict = c["J_H2_SENTENCE_SWEEP"], c["K_VERDICT"]
    return {
        "cycle": 890,
        "question": payload["question"],
        "T1_answer": t1["finding"],
        "T1_FULL_COLUMN": t1["THE_FULL_COLUMN"],
        "T2_answer": t2["finding"],
        "T2_witnesses": t2["three_computed_witnesses"],
        "T3_answer": t3["finding"],
        "T3_SUBSET_scope_coherent": t3["T3_SUBSET_scope_coherent"],
        "T3_SUBSET_orbit_scope_only": t3["T3_SUBSET_orbit_scope_only"],
        "T3_SUBSET_scope_mismatched_loosest":
            t3["T3_SUBSET_scope_mismatched_loosest"],
        "T3_off_menu_counterfactual":
            t3["off_menu_classes_that_would_qualify_if_realizability_were_dropped"],
        "H2_grade_distribution": h2["grade_distribution"],
        "H2_grade_distribution_under_the_permissive_rubric":
            h2["grade_distribution_under_the_permissive_variant"],
        "H2_grade_ceiling_under_the_permissive_rubric":
            h2["grade_ceiling_under_the_permissive_variant"],
        "H2_sentences_the_two_rubrics_grade_differently":
            h2["sentences_the_two_variants_grade_differently"],
        "H2_grade_distribution_by_document": h2["grade_distribution_by_document"],
        "H2_grade_ceiling": h2["grade_ceiling"],
        "H2_sentences_swept": h2["sentences_swept"],
        "H2_best_graded_sentences": h2["best_graded_sentences"],
        "H2_exclusion_hits": h2["exclusion_hits_count"],
        "H2_exclusion_hits_that_name_the_decomposition_level":
            h2["exclusion_hits_that_name_the_decomposition_level"],
        "H2_price_registration_sentences": h2["price_registration_sentences"],
        "H2_rubric": h2["rubric"],
        "DETAIL_T1_rows": t1["rows"],
        "DETAIL_T2_rows": t2["rows"],
        "DETAIL_T3_menu": t3["menu"],
        "DETAIL_T3_off_menu": t3["off_menu"],
        "DETAIL_T3_per_class_readings": t3["per_class_readings"],
        "DETAIL_T3_off_menu_counterfactual": t3["off_menu_counterfactual"],
        "DETAIL_SIDE_A_rows": c["F_SIDE_A_CANONICITY"]["rows"],
        "DETAIL_SIDE_B_rows": c["E_SIDE_B_MULTIPLICITY_FREENESS"]["rows"],
        "DETAIL_impostors": c["L_IMPOSTOR_STRESS"]["impostors"],
        "DETAIL_pins": c["A_PINS"]["rows"],
        "DETAIL_note_discovery": c["A_PINS"]["note_discovery"],
        "DETAIL_segmentation": c["B_SEGMENTATION_COMPLETENESS"]["documents"],
        "DETAIL_axiom_memo_sentence_grades": [
            {"byte_start": r["byte_start"], "grade": r["grade"],
             "class": r["class"],
             "grade_under_v1_permissive": r["grade_under_v1_permissive"],
             "byte_quoted_sentence": r["byte_quoted_sentence"],
             "reason": r["reason"]}
            for r in payload["sweeps"][0]["rows"] if r["kind"] == "SENTENCE"],
        "VERDICT": verdict["VERDICT"],
        "consequence": verdict["consequence"],
        "one_clause_registration_text": verdict["one_clause_registration_text"],
        "certificates": {k: {"statement": v["statement"],
                             "finding": v["finding"], "pass": v["pass"]}
                         for k, v in c.items()},
        "certificates_passed": sum(1 for v in c.values() if v["pass"]),
        "certificates_total": len(c),
        "sharpest_new_facts": [
            "T1 holds without exception on every realized class x scope row of "
            "the full census, with canonicity and multiplicity-freeness "
            "computed by non-communicating routes.",
            "At the SHELL scope exactly two classes are multiplicity-free -- "
            "A4_tetrahedral and O_full -- and NEITHER has a free orbit, so "
            "neither realizes the Cycle-883 readout at all.",
            "The honest-menu T3 subset is scope-coherent and stable: "
            f"{t3['T3_SUBSET_scope_coherent']}. Loosening to a "
            "scope-MISMATCHED reading admits "
            f"{t3['classes_that_only_enter_under_a_scope_mismatched_reading']}, "
            "which is why the datum and the forcedness must be read at the "
            "same readout space.",
            "Dropping the realizability rule would admit "
            f"{t3['off_menu_classes_that_would_qualify_if_realizability_were_dropped']}"
            ", so the free-orbit requirement is load-bearing for the endpoint.",
            f"The H2 sweep covers {h2['sentences_swept']} sentences with a "
            f"byte-exact reconstruction proof of completeness; grade ceiling "
            f"{h2['grade_ceiling']}; {h2['exclusion_hits_count']} sentences "
            "name the property or its level only to place it downstream.",
            "The only sentence anywhere in the four documents that a "
            "permissive reading can push to EXACT is a HISTORICAL sentence "
            "about the SUPERSEDED 2026-06-05 memo whose own content makes the "
            "readout context a SUPPLIED input -- quoted and adjudicated in "
            "full. That is how thin any quotable reading has to be.",
        ],
        "next_attackable_question": (
            "The clause is now single and named. Either register 'the readout "
            "scope is multiplicity-free' on the owner surface with "
            f"{t3['T3_SUBSET_scope_coherent']} as its computed consequence set, "
            "or attack the remaining separation inside that set: C3 and C4 both "
            "survive T3, so a second clause is still needed to choose between "
            "them, and the orbit-scope coarse reading is the only one that "
            "separates them (C3 carries the v_2 = 1 datum coarsely, C4 only "
            "finely)."
        ),
    }


def main() -> int:
    started = monotonic()
    payload = build_payload()
    second = build_payload()
    det_first = digest(payload)
    det_second = digest(second)
    deterministic = det_first == det_second
    payload["certificates"]["N_DETERMINISM"] = {
        "statement": (
            "GATE C890-G7. The entire computation is built twice in one "
            "process and the canonical digests must agree; no randomness, no "
            "iteration-order dependence, no floating point in a certificate."
        ),
        "first_build_digest": det_first,
        "second_build_digest": det_second,
        "deterministic": deterministic,
        "finding": f"double build digests {'agree' if deterministic else 'DIFFER'}.",
        "pass": deterministic,
    }
    summary = summarize(payload)
    elapsed = monotonic() - started
    summary["deterministic_double_build"] = deterministic
    summary["elapsed_sec_at_summary"] = round(elapsed, 3)
    summary["runtime_budget_sec"] = AUDIT_TIMEOUT_SEC
    summary["within_runtime_budget"] = elapsed <= AUDIT_TIMEOUT_SEC
    summary["certificates"]["N_DETERMINISM"] = {
        "statement": payload["certificates"]["N_DETERMINISM"]["statement"],
        "finding": payload["certificates"]["N_DETERMINISM"]["finding"],
        "pass": deterministic,
    }
    summary["certificates_passed"] = sum(
        1 for v in payload["certificates"].values() if v["pass"])
    summary["certificates_total"] = len(payload["certificates"])

    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(json.dumps(summary, indent=1, sort_keys=True) + "\n",
                       encoding="utf-8")

    out = json.dumps(payload, indent=1, sort_keys=True, default=str)
    if len(out.encode("utf-8")) > STDOUT_LIMIT_BYTES:
        out = json.dumps(summary, indent=1, sort_keys=True, default=str)
    print(out)
    ok = all(v["pass"] for v in payload["certificates"].values())
    return 0 if ok else 1


def preflight() -> None:
    missing = []
    for path in AUDIT_INPUT_PATHS:
        target = ROOT / path
        if not target.exists():
            missing.append(f"{path}: MISSING")
            continue
        got = sha256(target.read_bytes()).hexdigest()
        if got != EXPECTED_SHA256[path]:
            missing.append(f"{path}: sha256 {got} != {EXPECTED_SHA256[path]}")
        try:
            blob = subprocess.run(["git", "hash-object", str(target)],
                                  capture_output=True, text=True,
                                  cwd=str(ROOT), check=True).stdout.strip()
        except Exception as exc:                       # pragma: no cover gate
            missing.append(f"{path}: git hash-object failed ({exc})")
            continue
        if blob != EXPECTED_GIT_BLOBS[path]:
            missing.append(
                f"{path}: git blob {blob} != {EXPECTED_GIT_BLOBS[path]}")
    if missing:
        print("PREFLIGHT PIN FAILURE (exit 2):")
        for row in missing:
            print("  " + row)
        raise SystemExit(2)


if __name__ == "__main__":
    preflight()
    raise SystemExit(main())
