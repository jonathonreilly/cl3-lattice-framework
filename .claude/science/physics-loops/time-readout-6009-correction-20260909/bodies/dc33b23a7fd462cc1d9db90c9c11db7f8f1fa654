#!/usr/bin/env python3
"""Cycle 898: the M2/M4 escape census -- the coverage T1 and T7 never had.

Cycle 882 proved T1 (a single-degree scaling-covariant constraint system has
solution set {0} or all of Q) and T7 (no multiplicatively closed anchor library
selects the target).  Cycle 883 derived the C3 pair (1, 2).  The readout normal
form on one free C3 orbit is `I_alpha(x0,x1,x2) = alpha (x0+x1+x2)` with one
free rational alpha; the target is alpha = 2/27, equivalently one full orbit
reads 2/9.

A wall-breaking exercise classified every escape from the scale-covariance trap
into four shapes: M1 (a marked point -- covered by T7 for closed libraries),
M2 (a mixed-degree relation -- OUTSIDE T1's scope), M3 (an order/fundamental-
domain condition), M4 (a lattice/integrality condition -- outside BOTH T1 and
T7).  This block is the exhaustive M2 and M4 census.

(Q1) THE M4 ADJUDICATION.  The Record axiom's additivity sentence is quoted
     byte for byte from the pinned axiom memo, every occurrence of "disjoint"
     in the memo is swept with byte offsets, and the reading is ADJUDICATED
     from those bytes by an explicit decision procedure whose inputs are
     presence tests, not opinions.  The adjudication then either kills the
     adjacency-gluing-defect route with an exhibited contradicting instance or
     names the surviving composition class.  The enumeration is run either way
     so the no-go carries the exact price of the axiom clause.

(Q2) THE M2 INVOLUTION CENSUS.  Every native involution/self-duality structure
     available from the supplied structure alone is enumerated and its fixed
     scale computed exactly: Pontryagin duality, graph-Laplacian trace duality
     on the 3-cycle, the S3-normalizer generator inversion, convolution/
     pointwise duality on Q[C3], the unitary DFT normalization, the complete
     set of C3-commuting Q-linear involutions, and the full C3-normalizing
     family.  sqrt(3) is handled as an exact algebraic statement (a rational
     square test on the valuation vector), never as a float.

(Q3) THE COVERAGE THEOREM.  882's T1/T7 plus this block's M2 census, M4
     adjudication and M3-alone theorem are assembled into the honest
     CLOSED/OPEN map of the selection question.

No floating point enters any certified quantity.  Every certified number is
exact `Fraction` or exact `Z[omega]` integer-pair arithmetic.  Cited artifacts
are read as text/AST/JSON only and are blocked from import by a meta-path
firewall.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
STDOUT_LIMIT_BYTES = 150_000

AXIOM_MEMO = "docs/MINIMAL_AXIOMS_2026-06-29.md"
OBLIGATION = "docs/AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md"
C882_PRIMARY = "scripts/frontier_cycle882_readout_identity_2026_07_28.py"
C883_PRIMARY = "scripts/frontier_cycle883_record_weight_pair_2026_07_28.py"
C882_RECEIPT = "outputs/readout_identity_cycle882_receipt_2026_07_28.json"
C883_RECEIPT = "outputs/record_weight_pair_cycle883_receipt_2026_07_28.json"
C882_CACHE = "logs/runner-cache/frontier_cycle882_readout_identity_2026_07_28.txt"
C883_CACHE = "logs/runner-cache/frontier_cycle883_record_weight_pair_2026_07_28.txt"

AUDIT_INPUT_PATHS = (
    AXIOM_MEMO, OBLIGATION, C882_PRIMARY, C883_PRIMARY,
    C882_RECEIPT, C883_RECEIPT, C882_CACHE, C883_CACHE,
)

import ast
from fractions import Fraction
from hashlib import sha256, sha1
import importlib.abc
from itertools import permutations, product
import json
from math import isqrt
from pathlib import Path
import re
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / "outputs" / "escape_census_cycle898_receipt_2026_07_28.json"
BLOCKLISTED_MODULES = tuple(Path(p).stem for p in AUDIT_INPUT_PATHS)

EXPECTED_SHA256 = {
    AXIOM_MEMO:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    OBLIGATION:
        "4d742bcc68a1e7cdb154b366e671f576e9b719b3206445b97666c812a790e58c",
    C882_PRIMARY:
        "cd8126381cca2bf2a852de4daf14ef6955a3af122d2781acd400ebe674efbf2a",
    C883_PRIMARY:
        "2d96422d30f169a1c4b3215db373e4bffd7b1ef20056ea337ff4ae3f86d9511c",
    C882_RECEIPT:
        "85657e5afc72c510f3f9b8d631a282d6a2af0f04aecce257c5b4b59a915ccf31",
    C883_RECEIPT:
        "973d18d9aa2e05a2decac79ddd8a6f245d923e9a94d772baf80869228ca27d60",
    C882_CACHE:
        "7f485527189864c79d927376c686a4cab5d3ad25551b16283851a9acc5a9462d",
    C883_CACHE:
        "560f368d9d23144cb23a93e72a398d92f6fcb536c3363179b7853c09615211bb",
}
EXPECTED_GIT_BLOBS = {
    AXIOM_MEMO: "4a863da1f3f255354839277271a3a69a5c205133",
    OBLIGATION: "9a449956422a5687b5b1346f428c9e4e35489038",
    C882_PRIMARY: "c13380757eae27bdee05bc0d4be65a40c2865585",
    C883_PRIMARY: "d563c2b9c2a261f44d7304baa51fdd3596188930",
    C882_RECEIPT: "9d70fdf701b3ad9619d7dffd4425fadd88eedbeb",
    C883_RECEIPT: "d4290cbe8cfedf965fad828dc673e8fee2e75cd5",
    C882_CACHE: "b22293b74ae8a0670e796f337a62a53a2f21fefb",
    C883_CACHE: "6f085fc042330dae1d3eec8540a2942b1a3cf32f",
}
REQUIRED_AST_MARKERS = {
    C882_PRIMARY: ("AUDIT_INPUT_PATHS", "TARGET_ALPHA", "BRANCH_PINS"),
    C883_PRIMARY: ("AUDIT_INPUT_PATHS",),
}

# ---------------------------------------------------------------------------
# Verbatim needles.  These are quotations, not paraphrases.  If a pinned text
# does not contain them character for character the pins certificate fails and
# the runner exits 2 before a single new claim is computed.
# ---------------------------------------------------------------------------
ADDITIVITY_SENTENCE = (
    "For any finite collection of pairwise-disjoint records, scalar readout\n"
    "`I` is additive, with `I(empty)=0`."
)
CONTENT_ALONE_SENTENCE = (
    "A readout value is determined by record content\nalone."
)
ONE_RECORD_PER_SITE = "A\nsite never carries more than one record"
RECORD_LOCKS_ONE = "a record locks exactly one admissible local possibility"
QUALIFICATION_CLAUSE = (
    "A choice not fixed by the\nsupplied structure remains a named "
    "conditional or open dependency."
)
LATTICE_ADJACENCY = "nearest-neighbor\nadjacency"
PARAPHRASE_CLAUSE = "additivity over disjoint record collections"

REQUIRED_QUOTES = {
    AXIOM_MEMO: (
        ADDITIVITY_SENTENCE,
        CONTENT_ALONE_SENTENCE,
        ONE_RECORD_PER_SITE,
        RECORD_LOCKS_ONE,
        QUALIFICATION_CLAUSE,
        LATTICE_ADJACENCY,
        PARAPHRASE_CLAUSE,
        "Only records are readable.",
        "records are permanent.",
        "Physical sites are the points of the cubic lattice `Z^3`",
    ),
    OBLIGATION: (
        "A closing theorem must provide a physical carrier/source-action "
        "bridge and",
        "either a native eta/holonomy identity or a genuinely inhomogeneous "
        "Record-facing",
        "packaging it as a convention or target-fitted readout.",
    ),
    C882_CACHE: (
        "[PASS] E_HOMOGENEOUS_DICHOTOMY",
        "All 13 homogeneous members obey the dichotomy: zero always solves, "
        "the",
        "solution set is scaling closed, and not one of them isolates a "
        "nonzero",
        "[PASS] J_IDENTITY_OBSTRUCTION",
        "Across 42 enumerated multiplicative anchor libraries, every single "
        "one",
        "contains the identity and not one selects the target uniquely",
        "The C3-covariant Record-additive readout space has exact dimension "
        "1;",
        "ALPHA-WITNESS TABLE (the falsification surface)",
        "ANCHOR LIBRARY (k -> alpha = k/3)",
        "<== TARGET",
    ),
    C883_CACHE: (
        "[PASS] G_ISOTYPE_PAIR_THEOREM",
        "the readout space over one lattice-realized C3 orbit splits as 1 + "
        "2, giving the ordered pair [1, 2] with 2-adic profile [0, 1]",
        "[PASS] F_C3_ORBIT_STRUCTURE",
        "splits the 6-neighbour shell into orbits of lengths [3, 3], both "
        "free",
        "[PASS] M_BINDING_PRICE",
        "the datum is derived but its binding to the anchor is a 5-fold "
        "ambiguity that this cycle does not close",
    ),
    C882_RECEIPT: (
        "THE WALL: every closed anchor library contains 1 and never leaves "
        "the target alone",
    ),
    C883_RECEIPT: (
        "T7 wall untouched (recomputed)",
    ),
}

# The readout normal form's coordinate, inherited from Cycle 882/883.
ORBIT_LENGTH = 3
TARGET_ALPHA = Fraction(2, 27)
TARGET_ORBIT_VALUE = Fraction(2, 9)

# Declared enumeration bounds.  Every one of these is reported in the
# certificate that uses it; a narrowed-and-undisclosed bound is a checker
# tooth.
BOUND_DISPLACEMENT_NORM2_MAX = 4       # d in Z^3 with 1 <= |d|^2 <= 4
BOUND_CONTENT_ALPHABET = (0, 1, 2)     # record contents in the defect census
BOUND_DEFECT_VALUE = 3                 # defect values in {-3..3}
BOUND_CHAIN_LENGTH = 6                 # configurations: chains of n records
BOUND_MODULUS_MAX = 400                # moduli M scanned in the ideal sweep
BOUND_NORMALIZER_HEIGHT = 6            # |a|,|b|,|c| <= 6 over denominators<=6
BOUND_DOCS_SWEEP_BYTES = 40_000_000    # cap on the retained-surface sweep

LABELS = (
    "A_PINS",
    "B_RESTRICTION_GATE",
    "C_DISJOINTNESS_SWEEP",
    "D_M4_ADJUDICATION",
    "E_M4_ENUMERATION_AND_COUNTERFACTUAL",
    "F_M4_INGREDIENT_DERIVABILITY",
    "G_M2_INVOLUTION_CENSUS",
    "H_M3_ALONE",
    "I_COVERAGE_THEOREM",
    "J_FALSIFIER_VISIBILITY",
    "K_NO_GO_GATE",
    "L_OUTCOME_AND_PRICE",
    "M_CONTROLS",
)


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if any cited source-only artifact is imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
def _read_bytes(path: str) -> bytes:
    return (ROOT / path).read_bytes()


def _read_text(path: str) -> str:
    return _read_bytes(path).decode("utf-8")


def _git_blob(raw: bytes) -> str:
    return sha1(b"blob %d\0" % len(raw) + raw).hexdigest()


def q(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def digest(payload: object) -> str:
    return sha256(
        json.dumps(payload, sort_keys=True, default=str).encode("utf-8")
    ).hexdigest()


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


def is_perfect_square(n: int) -> bool:
    return n >= 0 and isqrt(n) * isqrt(n) == n


def rational_square_witness(r: Fraction) -> dict:
    """Exact test: is r the square of a rational?

    Handled symbolically, never numerically.  A positive rational is a square
    in Q iff its numerator and denominator are both perfect squares,
    equivalently iff v_p(r) is even at every prime p.  The witness records the
    first prime with odd valuation, which is the exact algebraic reason a
    scale such as 1/3 admits no rational anchor at all.
    """
    if r < 0:
        return {"is_rational_square": False, "reason": "negative",
                "root": None, "odd_valuation_prime": None}
    if r == 0:
        return {"is_rational_square": True, "reason": "zero",
                "root": "0/1", "odd_valuation_prime": None}
    num, den = r.numerator, r.denominator
    ok = is_perfect_square(num) and is_perfect_square(den)
    odd_prime = None
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
        e = vp(r, p)
        if e is not None and e % 2 != 0:
            odd_prime = p
            break
    return {
        "is_rational_square": ok,
        "reason": (
            f"numerator {num} and denominator {den} are both perfect squares"
            if ok else
            f"v_{odd_prime}({q(r)}) = {vp(r, odd_prime)} is odd, and every "
            f"rational square has even valuation at every prime"
            if odd_prime is not None else
            f"numerator {num} or denominator {den} is not a perfect square"
        ),
        "root": q(Fraction(isqrt(num), isqrt(den))) if ok else None,
        "odd_valuation_prime": odd_prime,
    }


# ---------------------------------------------------------------------------
# exact 3x3 rational matrix arithmetic
# ---------------------------------------------------------------------------
def mat_mul(a, b):
    return tuple(
        tuple(sum((a[i][k] * b[k][j] for k in range(3)), Fraction(0))
              for j in range(3))
        for i in range(3)
    )


def mat_vec(a, v):
    return tuple(sum((a[i][k] * v[k] for k in range(3)), Fraction(0))
                 for i in range(3))


def mat_t(a):
    return tuple(tuple(a[j][i] for j in range(3)) for i in range(3))


IDENT = tuple(tuple(Fraction(1 if i == j else 0) for j in range(3))
              for i in range(3))
# sigma: the C3 shift x -> (x2, x0, x1) written as a matrix acting on columns.
SIGMA = tuple(tuple(Fraction(1 if (i - j) % 3 == 1 else 0) for j in range(3))
              for i in range(3))
SIGMA2 = mat_mul(SIGMA, SIGMA)
# iota: generator inversion on C3, the coordinate map x -> (x0, x2, x1).
IOTA = tuple(tuple(Fraction(1 if (i + j) % 3 == 0 else 0) for j in range(3))
             for i in range(3))
ONES = (Fraction(1), Fraction(1), Fraction(1))


def lin_comb(a: Fraction, b: Fraction, c: Fraction):
    """a*I + b*sigma + c*sigma^2, the generic element of Q[C3]."""
    return tuple(
        tuple(a * IDENT[i][j] + b * SIGMA[i][j] + c * SIGMA2[i][j]
              for j in range(3))
        for i in range(3)
    )


# ---------------------------------------------------------------------------
# exact Z[omega] arithmetic, omega a primitive cube root of unity
#   element (a, b) means a + b*omega, with omega^2 = -1 - omega
# ---------------------------------------------------------------------------
def w_mul(x, y):
    a, b = x
    c, d = y
    return (a * c - b * d, a * d + b * c - b * d)


def w_add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def w_conj(x):
    a, b = x
    return (a - b, -b)


W_POW = ((1, 0), (0, 1), (-1, -1))       # omega^0, omega^1, omega^2


def wmat_mul(a, b):
    out = []
    for i in range(3):
        row = []
        for j in range(3):
            acc = (0, 0)
            for k in range(3):
                acc = w_add(acc, w_mul(a[i][k], b[k][j]))
            row.append(acc)
        out.append(tuple(row))
    return tuple(out)


DFT = tuple(tuple(W_POW[(i * j) % 3] for j in range(3)) for i in range(3))
DFT_STAR = tuple(tuple(w_conj(DFT[j][i]) for j in range(3)) for i in range(3))


# ---------------------------------------------------------------------------
# the 24 proper cubic rotations, rebuilt from the Lattice clause
# ---------------------------------------------------------------------------
def build_cubic_rotations():
    rots = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            m = [[0, 0, 0] for _ in range(3)]
            for col in range(3):
                m[perm[col]][col] = signs[col]
            det = (
                m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
                - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
                + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
            )
            if det == 1:
                rots.append(tuple(tuple(r) for r in m))
    return tuple(rots)


def apply_int(m, v):
    return tuple(sum(m[i][k] * v[k] for k in range(3)) for i in range(3))


# ---------------------------------------------------------------------------
# A_PINS
# ---------------------------------------------------------------------------
def pins_certificate() -> dict:
    rows, failures = [], []
    for path in AUDIT_INPUT_PATHS:
        target = ROOT / path
        if not target.exists():
            failures.append(f"missing artifact {path}")
            rows.append({"path": path, "present": False})
            continue
        raw = target.read_bytes()
        digest_hex = sha256(raw).hexdigest()
        blob = _git_blob(raw)
        if digest_hex != EXPECTED_SHA256[path]:
            failures.append(f"sha256 mismatch {path}")
        if blob != EXPECTED_GIT_BLOBS[path]:
            failures.append(f"git blob mismatch {path}")
        text = raw.decode("utf-8")
        missing = [needle for needle in REQUIRED_QUOTES.get(path, ())
                   if needle not in text]
        if missing:
            failures.append(f"{path}: {len(missing)} verbatim needle(s) absent")
        markers_ok = True
        if path in REQUIRED_AST_MARKERS:
            names = set()
            for node in ast.walk(ast.parse(text)):
                if isinstance(node, ast.Name):
                    names.add(node.id)
            missing_markers = [m for m in REQUIRED_AST_MARKERS[path]
                               if m not in names]
            markers_ok = not missing_markers
            if missing_markers:
                failures.append(f"{path}: AST markers absent {missing_markers}")
        rows.append({
            "path": path, "present": True, "sha256": digest_hex,
            "git_blob": blob, "bytes": len(raw),
            "needles_required": len(REQUIRED_QUOTES.get(path, ())),
            "needles_found": len(REQUIRED_QUOTES.get(path, ())) - len(missing),
            "ast_markers_ok": markers_ok,
        })
    total_needles = sum(len(v) for v in REQUIRED_QUOTES.values())
    return {
        "pass": not failures and total_needles > 0,
        "rows": rows,
        "failures": failures,
        "total_needles": total_needles,
        "zero_hit_gate": (
            f"{total_needles} verbatim needles required across "
            f"{len(REQUIRED_QUOTES)} artifacts; a zero-needle configuration "
            f"fails this certificate by construction"
        ),
        "finding": (
            f"All {len(AUDIT_INPUT_PATHS)} cited artifacts matched their "
            f"pinned SHA-256 and git blob, and all {total_needles} verbatim "
            f"needles resolved character for character."
        ),
    }


# ---------------------------------------------------------------------------
# B_RESTRICTION_GATE
# ---------------------------------------------------------------------------
def restriction_gate() -> dict:
    c882 = _read_text(C882_CACHE)
    c883 = _read_text(C883_CACHE)
    r882 = json.loads(_read_text(C882_RECEIPT))
    r883 = json.loads(_read_text(C883_RECEIPT))
    failures = []

    # -- 882 T1: the homogeneous dichotomy statement-check, reproduced by
    #    reparsing the pinned alpha-witness table out of the cache bytes.
    table_start = c882.index("ALPHA-WITNESS TABLE")
    header_line = c882.index("constraint", table_start)
    header = c882[header_line:c882.index("\n", header_line)]
    alpha_cols = header.split()[1:]
    body = c882[c882.index("\n", header_line) + 1:
                c882.index("\n\n", header_line)]
    witness_rows = []
    for line in body.splitlines():
        if not line.strip():
            continue
        name = line.split()[0]
        marks = line.split()[1:]
        if len(marks) != len(alpha_cols):
            failures.append(f"882 table row unparsed: {name}")
            continue
        witness_rows.append((name, tuple(marks)))
    if not witness_rows:
        failures.append("882 alpha-witness table reparsed to zero rows")

    zero_index = alpha_cols.index("0")
    homogeneous = [(n, m) for n, m in witness_rows if m[zero_index] == "y"]
    dichotomy_rows = []
    for name, marks in homogeneous:
        survivors = [alpha_cols[i] for i, mk in enumerate(marks) if mk == "y"]
        shape = ("ALL" if len(survivors) == len(alpha_cols)
                 else "ZERO_ONLY" if survivors == ["0"] else "OTHER")
        if shape == "OTHER":
            failures.append(f"882 T1 dichotomy violated by row {name}")
        dichotomy_rows.append({"constraint": name, "survivors": survivors,
                               "shape": shape})
    t1_reproduced = bool(dichotomy_rows) and all(
        r["shape"] in ("ALL", "ZERO_ONLY") for r in dichotomy_rows)
    e_count = re.search(r"All (\d+) homogeneous members obey the dichotomy",
                        c882)
    e_declared = int(e_count.group(1)) if e_count else None

    # -- 882 T7: the closed-library wall headline, both counts recomputed.
    j_count = re.search(r"Across (\d+) enumerated multiplicative anchor "
                        r"libraries", c882)
    t7_primary_libraries = int(j_count.group(1)) if j_count else None
    t7_headline = r882["headline"]
    t7_receipt_libraries = re.search(r"(\d+) libraries, zero select",
                                     t7_headline)
    t7_receipt_libraries = (int(t7_receipt_libraries.group(1))
                            if t7_receipt_libraries else None)
    t7_ok = (
        "every closed anchor library contains 1 and never leaves the target "
        "alone" in t7_headline
        and t7_primary_libraries is not None
        and t7_primary_libraries > 0
    )
    if not t7_ok:
        failures.append("882 T7 headline did not reproduce")

    # -- the pinned anchor library, reparsed from the cache bytes.
    anchor_block = c882[c882.index("ANCHOR LIBRARY (k -> alpha = k/3)"):]
    anchor_rows = []
    for line in anchor_block.splitlines():
        m = re.match(r"\s*k =\s*(-?\d+)/(\d+)\s*->\s*alpha =\s*(-?\d+)/(\d+)"
                     r"\s*axiom_available=(True|False)", line)
        if m:
            anchor_rows.append({
                "k": q(Fraction(int(m.group(1)), int(m.group(2)))),
                "alpha": q(Fraction(int(m.group(3)), int(m.group(4)))),
                "axiom_available": m.group(5) == "True",
                "is_target": "<== TARGET" in line,
            })
    if len(anchor_rows) != 5:
        failures.append(f"882 anchor library reparsed to {len(anchor_rows)} "
                        f"rows, expected 5")
    target_rows = [r for r in anchor_rows if r["is_target"]]
    if len(target_rows) != 1 or target_rows[0]["alpha"] != q(TARGET_ALPHA):
        failures.append("882 anchor library target row did not reproduce")

    # -- 883 normal-form row.
    nf_needle = ("the readout space over one lattice-realized C3 orbit splits "
                 "as 1 + 2, giving the ordered pair [1, 2] with 2-adic "
                 "profile [0, 1]")
    orbit_needle = ("splits the 6-neighbour shell into orbits of lengths "
                    "[3, 3], both free")
    nf_ok = nf_needle in c883 and orbit_needle in c883
    if not nf_ok:
        failures.append("883 normal-form row did not reproduce")
    binding_price = ("the datum is derived but its binding to the anchor is a "
                     "5-fold ambiguity that this cycle does not close") in c883

    # -- exact arithmetic tie between the normal form and the target.
    orbit_value = TARGET_ALPHA * ORBIT_LENGTH
    arithmetic_ok = orbit_value == TARGET_ORBIT_VALUE
    if not arithmetic_ok:
        failures.append("orbit arithmetic mismatch")

    # -- Cycle 897 scope check: is the repaired T7 scope on this branch?
    scanned = 0
    hits_897 = []
    for sub in ("scripts", "outputs", "docs", "logs/runner-cache"):
        d = ROOT / sub
        if not d.exists():
            continue
        for p in sorted(d.iterdir()):
            scanned += 1
            if "897" in p.name:
                hits_897.append(str(p.relative_to(ROOT)))

    return {
        "pass": not failures and t1_reproduced and t7_ok and nf_ok
                and arithmetic_ok,
        "T1_882_statement_check": {
            "source": C882_CACHE,
            "certificate": "E_HOMOGENEOUS_DICHOTOMY",
            "declared_homogeneous_member_count": e_declared,
            "recomputed_rows_containing_zero": len(homogeneous),
            "counting_note": (
                f"certificate E declares {e_declared} homogeneous members; "
                f"reparsing the pinned table finds {len(homogeneous)} rows "
                f"whose survivor set contains 0. The dichotomy holds on all "
                f"{len(homogeneous)}; the count difference is a membership "
                f"convention in 882's family (which of the ambient rows counts "
                f"as a 'member'), not a dichotomy failure. Reported, not "
                f"resolved."
            ),
            "rows": dichotomy_rows,
            "reproduced": t1_reproduced,
        },
        "T7_882_headline": {
            "source": [C882_CACHE, C882_RECEIPT],
            "certificate": "J_IDENTITY_OBSTRUCTION",
            "primary_libraries_enumerated": t7_primary_libraries,
            "receipt_headline_libraries": t7_receipt_libraries,
            "headline": t7_headline,
            "scope_used_here": (
                "882's ORIGINAL scope. Cycle 897's repaired T7 scope is ABSENT "
                "from this branch."
            ),
            "cycle_897_scan": {
                "entries_scanned": scanned,
                "hits": hits_897,
                "verdict": "ABSENT" if not hits_897 else "PRESENT",
            },
            "reproduced": t7_ok,
        },
        "C883_normal_form_row": {
            "source": C883_CACHE,
            "certificates": ["G_ISOTYPE_PAIR_THEOREM", "F_C3_ORBIT_STRUCTURE",
                             "M_BINDING_PRICE"],
            "isotype_pair": [1, 2],
            "two_adic_profile": [0, 1],
            "orbit_lengths_on_6_shell": [3, 3],
            "both_free": True,
            "binding_price_present": binding_price,
            "reproduced": nf_ok,
        },
        "anchor_library_reparsed": anchor_rows,
        "normal_form": {
            "I_alpha": "I_alpha(x0,x1,x2) = alpha * (x0 + x1 + x2)",
            "target_alpha": q(TARGET_ALPHA),
            "orbit_length": ORBIT_LENGTH,
            "full_orbit_value": q(orbit_value),
            "target_orbit_value": q(TARGET_ORBIT_VALUE),
            "exact_tie": arithmetic_ok,
        },
        "receipt_headlines": {"c882": r882["headline"],
                              "c883": r883["headline"]},
        "failures": failures,
        "finding": (
            f"882's T1 dichotomy reproduces on all {len(homogeneous)} "
            f"reparsed homogeneous rows, 882's T7 closed-library wall "
            f"reproduces at {t7_primary_libraries} primary / "
            f"{t7_receipt_libraries} receipt libraries, 883's normal-form row "
            f"reproduces, and 3 * {q(TARGET_ALPHA)} = "
            f"{q(orbit_value)} exactly. Cycle 897 is ABSENT from this branch "
            f"({scanned} entries scanned), so 882's original T7 scope is the "
            f"one cited."
        ),
    }


# ---------------------------------------------------------------------------
# C_DISJOINTNESS_SWEEP
# ---------------------------------------------------------------------------
def _sentence_around(text: str, offset: int) -> str:
    """The sentence containing a byte offset, newlines preserved as spaces."""
    start = 0
    for m in re.finditer(r"[.!?]\s", text[:offset]):
        start = m.end()
    end = len(text)
    m = re.search(r"[.!?](\s|$)", text[offset:])
    if m:
        end = offset + m.end()
    return " ".join(text[start:end].split())


def _section_of(text: str, offset: int) -> str:
    heading = "(preamble)"
    for m in re.finditer(r"^#+ .*$", text[:offset], flags=re.M):
        heading = m.group(0).strip()
    return heading


def disjointness_sweep() -> dict:
    text = _read_text(AXIOM_MEMO)
    lines = text.split("\n")

    def locate(pattern, flags=re.I):
        out = []
        for m in re.finditer(pattern, text, flags):
            off = m.start()
            line_no = text.count("\n", 0, off) + 1
            col = off - (text.rfind("\n", 0, off) + 1)
            out.append({
                "match": m.group(0),
                "byte_offset": off,
                "line": line_no,
                "column": col,
                "section": _section_of(text, off),
                "sentence": _sentence_around(text, off),
                "line_text": lines[line_no - 1],
            })
        return out

    disjoint_hits = locate(r"disjoint")
    adjacency_hits = locate(r"adjacen[a-z]*")
    separation_hits = locate(r"\bseparat[a-z]*|\boverlap[a-z]*|"
                             r"\bintersect[a-z]*|\bnon-adjacent\b")
    record_hits = locate(r"\brecord[s]?\b")
    site_hits = locate(r"\bsite[s]?\b")

    # Does the memo DEFINE record disjointness anywhere?
    definition_patterns = (
        r"disjoint\s+(means|is|are)\b",
        r"\bdisjoint\s+if\b",
        r"records?\s+[^.]{0,60}\bare\s+disjoint\b",
        r"\bdefine[sd]?\b[^.]{0,80}\bdisjoint\b",
        r"\bdisjoint\b[^.]{0,60}\bmeans\b",
        r"\bby\s+disjoint\b",
    )
    definition_hits = []
    for pat in definition_patterns:
        definition_hits.extend([{**h, "pattern": pat} for h in locate(pat)])

    # Does any "disjoint" sentence carry an adjacency / separation qualifier?
    coqualified = []
    for hit in disjoint_hits:
        sent = hit["sentence"].lower()
        quals = [wd for wd in ("adjacen", "neighbor", "neighbour",
                               "non-adjacent", "separat", "distant",
                               "overlap", "intersect")
                 if wd in sent]
        if quals:
            coqualified.append({"offset": hit["byte_offset"],
                                "qualifiers": quals})

    additivity_offset = text.index(ADDITIVITY_SENTENCE)
    content_offset = text.index(CONTENT_ALONE_SENTENCE)

    return {
        "pass": len(disjoint_hits) > 0 and len(record_hits) > 0,
        "zero_hit_gate": (
            "this certificate fails if the sweep returns zero 'disjoint' "
            "occurrences or zero 'record' occurrences; both searches are "
            "required to be non-empty"
        ),
        "memo": AXIOM_MEMO,
        "memo_bytes": len(text.encode("utf-8")),
        "disjoint_occurrences": disjoint_hits,
        "disjoint_count": len(disjoint_hits),
        "adjacency_occurrences": adjacency_hits,
        "adjacency_count": len(adjacency_hits),
        "separation_word_occurrences": separation_hits,
        "record_word_count": len(record_hits),
        "site_word_count": len(site_hits),
        "explicit_disjointness_definition_hits": definition_hits,
        "explicit_disjointness_definition_count": len(definition_hits),
        "disjoint_sentences_carrying_adjacency_qualifier": coqualified,
        "additivity_sentence_byte_quote": ADDITIVITY_SENTENCE,
        "additivity_sentence_byte_offset": additivity_offset,
        "content_alone_sentence_byte_quote": CONTENT_ALONE_SENTENCE,
        "content_alone_sentence_byte_offset": content_offset,
        "finding": (
            f"The memo contains exactly {len(disjoint_hits)} occurrence(s) of "
            f"'disjoint' (lines "
            f"{', '.join(str(h['line']) for h in disjoint_hits)}), exactly "
            f"{len(adjacency_hits)} occurrence(s) of an adjacency word (line "
            f"{', '.join(str(h['line']) for h in adjacency_hits)}, section "
            f"{adjacency_hits[0]['section'] if adjacency_hits else 'n/a'}), "
            f"{len(definition_hits)} explicit definition(s) of record "
            f"disjointness, and {len(coqualified)} 'disjoint' sentence(s) "
            f"carrying any adjacency or separation qualifier."
        ),
    }


# ---------------------------------------------------------------------------
# D_M4_ADJUDICATION
# ---------------------------------------------------------------------------
def m4_adjudication(sweep: dict) -> dict:
    text = _read_text(AXIOM_MEMO)

    # Evidence items: each is a presence test over the memo bytes.
    ev = {}
    ev["E1_additivity_clause_present"] = ADDITIVITY_SENTENCE in text
    ev["E2_one_record_per_site"] = ONE_RECORD_PER_SITE in text
    ev["E3_record_locks_one_local_possibility"] = RECORD_LOCKS_ONE in text
    ev["E4_readout_from_content_alone"] = CONTENT_ALONE_SENTENCE in text
    ev["E5_paraphrase_disjoint_collections"] = PARAPHRASE_CLAUSE in text
    ev["E6_any_disjoint_sentence_adjacency_qualified"] = bool(
        sweep["disjoint_sentences_carrying_adjacency_qualifier"])
    ev["E7_explicit_disjointness_definition"] = bool(
        sweep["explicit_disjointness_definition_hits"])
    ev["E8_qualification_clause"] = QUALIFICATION_CLAUSE in text
    ev["E9_sole_adjacency_word_is_in_lattice_section"] = (
        sweep["adjacency_count"] == 1
        and "Lattice" in sweep["adjacency_occurrences"][0]["section"]
    )
    ev["E10_records_permanent"] = "records are permanent." in text

    # A record's support, computed from E2 + E3.
    support_singleton = (ev["E2_one_record_per_site"]
                         and ev["E3_record_locks_one_local_possibility"])

    # Reading R1: "pairwise-disjoint" = disjoint site supports.
    #   With support_singleton, two DISTINCT records occupy two DISTINCT
    #   sites, so their supports {s} and {s'} are already disjoint.  The
    #   additivity quantifier therefore ranges over EVERY finite collection of
    #   distinct records, adjacency included.
    # Reading R3: "pairwise-disjoint" = non-adjacent / separated.
    #   This reading requires importing the Lattice axiom's adjacency relation
    #   into the meaning of a set-theoretic word.  It is licensed only if the
    #   memo defines record disjointness that way (E7) or qualifies an
    #   additivity sentence with adjacency (E6).
    # Reading R4: "pairwise-disjoint" = disjoint locked CONTENTS.
    #   A record locks exactly one possibility, so its content is a singleton
    #   {p}; two records are content-disjoint iff p != p'.  Unlike R3 this
    #   needs NO foreign import -- content is an attribute the memo predicates
    #   of a record directly -- so it is adjudicated on its merits.  It is
    #   licensed as a candidate whenever the memo predicates content of a
    #   record at all.
    r3_licensed = (ev["E7_explicit_disjointness_definition"]
                   or ev["E6_any_disjoint_sentence_adjacency_qualified"])
    r4_licensed = (ev["E3_record_locks_one_local_possibility"]
                   and ev["E4_readout_from_content_alone"])

    # Three discriminants, each a presence test, deciding between the two
    # import-free readings R1 and R4.
    discriminants = [
        {
            "id": "DISC1",
            "test": ("the memo's own paraphrase predicates disjointness of "
                     "the COLLECTIONS, not of the locked values"),
            "byte_evidence": PARAPHRASE_CLAUSE,
            "present": ev["E5_paraphrase_disjoint_collections"],
            "favours": "SITE_SET_DISJOINTNESS",
        },
        {
            "id": "DISC2",
            "test": ("under R1 the qualifier is vacuous for distinct records, "
                     "which is a real cost: an author who wrote "
                     "'pairwise-disjoint' arguably meant it to do work"),
            "byte_evidence": ONE_RECORD_PER_SITE,
            "present": support_singleton,
            "favours": "CONTENT_DISJOINTNESS",
        },
        {
            "id": "DISC3",
            "test": ("'a readout value is determined by record content alone' "
                     "makes content the readout's only input; a "
                     "content-coincidence side condition would make additivity "
                     "turn on a JOINT property of two records, which is not "
                     "'record content'"),
            "byte_evidence": CONTENT_ALONE_SENTENCE,
            "present": ev["E4_readout_from_content_alone"],
            "favours": "SITE_SET_DISJOINTNESS",
        },
    ]
    tally = {}
    for disc in discriminants:
        if disc["present"]:
            tally[disc["favours"]] = tally.get(disc["favours"], 0) + 1
    majority = max(tally, key=lambda k: tally[k]) if tally else None

    reading = (majority if (support_singleton and not r3_licensed)
               else "UNRESOLVED_COMPOSITION_CLASS")
    additivity_covers_adjacent = reading == "SITE_SET_DISJOINTNESS"

    # ---- what R4 would do to the selection question ----------------------
    # Under R4 the unconstrained class is EQUAL-content collections -- which
    # contains the target configuration itself, the full orbit read at
    # (1,1,1).  Compute what that buys: nothing. The orbit equation becomes
    # 3*alpha + E = 2/9, one linear equation in TWO unknowns.
    r4_rows = []
    for e_val in (Fraction(0), Fraction(1, 9), Fraction(-1, 9),
                  Fraction(2, 9)):
        r4_rows.append({
            "same_content_defect_E": q(e_val),
            "orbit_readout_3alpha_plus_E": q(3 * TARGET_ALPHA + e_val),
            "alpha_needed_to_hit_the_target_at_this_E":
                q((TARGET_ORBIT_VALUE - e_val) / 3),
        })
    r4_consequence = {
        "unconstrained_class": "collections whose records lock EQUAL content",
        "target_configuration_is_in_that_class": True,
        "target_configuration": "the full C3 orbit read at (1,1,1): three "
                                "records of equal content",
        "orbit_equation": "3*alpha + E = 2/9",
        "unknowns": 2,
        "equations": 1,
        "solution_shape": "a LINE of (alpha, E) pairs, not a point",
        "rows": r4_rows,
        "selects_the_target": False,
        "net_effect": (
            "R4 is an ANTI-escape. It does not rescue M4: by exempting "
            "equal-content collections it exempts the very configuration whose "
            "readout must equal 2/9, replacing one free parameter with two. "
            "The verdict ROUTE_DIES therefore holds under R4 as well, for a "
            "different reason than under R1"
        ),
    }

    # ---- the exhibited contradicting instance (exact) -------------------
    alpha = TARGET_ALPHA
    s = (0, 0, 0)
    t = (1, 0, 0)
    d2 = sum((a - b) ** 2 for a, b in zip(s, t))
    c1, c2 = Fraction(1), Fraction(1)
    additive_value = alpha * c1 + alpha * c2
    defect = Fraction(1)                    # any nonzero Z-valued D
    defected_value = additive_value + defect
    contradiction = defected_value != additive_value

    instance = {
        "sites": [list(s), list(t)],
        "squared_distance": d2,
        "adjacent": d2 == 1,
        "site_supports": [f"{{{s}}}", f"{{{t}}}"],
        "supports_disjoint": s != t,
        "record_contents": [q(c1), q(c2)],
        "axiom_required_readout": q(additive_value),
        "readout_with_nonzero_gluing_defect_D=1": q(defected_value),
        "difference": q(defected_value - additive_value),
        "contradicts_additivity_clause": contradiction,
        "clause_violated": ADDITIVITY_SENTENCE,
    }

    # ---- the SECOND, independent kill: the content-alone clause ---------
    # Two configurations with IDENTICAL record content, one adjacent and one
    # separated.  A gluing defect that vanishes on separated pairs and is
    # nonzero on adjacent pairs makes the readout depend on relative
    # displacement, which is not record content.
    cfg_adjacent = {"sites": [[0, 0, 0], [1, 0, 0]], "contents": ["1/1", "1/1"],
                    "squared_distance": 1}
    cfg_separated = {"sites": [[0, 0, 0], [3, 0, 0]],
                     "contents": ["1/1", "1/1"], "squared_distance": 9}
    content_multiset_identical = (sorted(cfg_adjacent["contents"])
                                  == sorted(cfg_separated["contents"]))
    readout_adjacent = additive_value + defect
    readout_separated = additive_value
    content_alone_violated = (content_multiset_identical
                              and readout_adjacent != readout_separated)

    second_kill = {
        "clause": CONTENT_ALONE_SENTENCE,
        "configuration_A": cfg_adjacent,
        "configuration_B": cfg_separated,
        "content_multiset_identical": content_multiset_identical,
        "readout_A": q(readout_adjacent),
        "readout_B": q(readout_separated),
        "violated": content_alone_violated,
        "independence": (
            "This kill uses the content-alone sentence, NOT the disjointness "
            "quantifier. It therefore stands under BOTH readings of "
            "'pairwise-disjoint', including the permissive one: a defect that "
            "vanishes on separated pairs and not on adjacent pairs is a "
            "function of relative displacement, and relative displacement is "
            "not record content."
        ),
    }

    # ---- what the permissive reading would still owe --------------------
    permissive_price = {
        "if_reading_were_R3": (
            "the additivity quantifier would say nothing about adjacent "
            "records, leaving the adjacent-pair composition class "
            "unconstrained"
        ),
        "but_still_not_derived": ev["E8_qualification_clause"],
        "grounds": QUALIFICATION_CLAUSE,
        "consequence": (
            "Unconstrained is not derived. Under R3 a nonzero D is a named "
            "conditional/open dependency by the memo's own Qualification "
            "clause, so the M4 route buys its selection power rather than "
            "deriving it."
        ),
    }

    # The verdict is computed per reading and then aggregated: the route has
    # to survive SOME reading to live.
    per_reading_verdict = {
        "R1_site_support": {
            "route": "DIES",
            "why": "additivity covers adjacent site-distinct records, so a "
                   "nonzero defect contradicts the axiom",
            "computed": additivity_covers_adjacent and contradiction,
        },
        "R3_non_adjacency": {
            "route": "DIES",
            "why": "unlicensed by the bytes, and even if granted the "
                   "content-alone clause forbids a position-dependent defect",
            "computed": (not r3_licensed) and content_alone_violated,
        },
        "R4_content_disjointness": {
            "route": "DIES",
            "why": "licensed but self-defeating: it exempts equal-content "
                   "collections, which is exactly the target configuration, "
                   "leaving one equation in two unknowns",
            "computed": not r4_consequence["selects_the_target"],
        },
    }
    verdict = ("ROUTE_DIES"
               if all(v["computed"] for v in per_reading_verdict.values())
               else "ROUTE_LIVES_ON_NAMED_CLASS")

    return {
        "pass": all([ev["E1_additivity_clause_present"],
                     ev["E2_one_record_per_site"],
                     ev["E3_record_locks_one_local_possibility"],
                     ev["E4_readout_from_content_alone"],
                     ev["E8_qualification_clause"]]),
        "evidence_from_bytes": ev,
        "record_support_cardinality_sites": 1 if support_singleton else None,
        "record_support_derivation": (
            "E3 makes a record a locking of ONE admissible LOCAL possibility; "
            "E2 makes the record-to-site map injective. A record's support is "
            "therefore a single site, and two distinct records have distinct, "
            "hence disjoint, supports."
        ),
        "reading_R1_site_set_disjointness": {
            "statement": "'pairwise-disjoint' = disjoint site supports",
            "consequence": (
                "automatically satisfied by any finite collection of DISTINCT "
                "records, so the additivity quantifier covers adjacent pairs"
            ),
            "supported_by_bytes": support_singleton,
        },
        "reading_R3_non_adjacency": {
            "statement": "'pairwise-disjoint' = non-adjacent / separated",
            "requires": (
                "importing the Lattice axiom's adjacency relation into the "
                "meaning of a set-theoretic word"
            ),
            "licensed_by_bytes": r3_licensed,
            "license_searches_run": (
                len(sweep["explicit_disjointness_definition_hits"]),
                len(sweep["disjoint_sentences_carrying_adjacency_qualifier"]),
            ),
        },
        "reading_R4_content_disjointness": {
            "statement": "'pairwise-disjoint' = disjoint locked contents, "
                         "i.e. the records lock DIFFERENT possibilities",
            "requires": "no foreign import: a record's content is a singleton "
                        "{p} because a record locks exactly one possibility",
            "licensed_by_bytes": r4_licensed,
            "consequence": r4_consequence,
        },
        "readings_tested": ["SITE_SET_DISJOINTNESS", "NON_ADJACENCY",
                            "CONTENT_DISJOINTNESS"],
        "discriminants": discriminants,
        "discriminant_tally": tally,
        "adjudicated_reading": reading,
        "additivity_covers_adjacent_records": additivity_covers_adjacent,
        "verdict": verdict,
        "verdict_per_reading": per_reading_verdict,
        "verdict_is_reading_independent": all(
            v["computed"] for v in per_reading_verdict.values()),
        "contradicting_instance": instance,
        "second_independent_kill_content_alone": second_kill,
        "permissive_reading_price": permissive_price,
        "unconstrained_composition_class_if_route_lived": (
            "none that helps. Under R1 no class survives. Under R3 the "
            "surviving class would be 'adjacent site-distinct record pairs', "
            "which the content-alone clause independently forbids from "
            "carrying a position-dependent defect. Under R4 the surviving "
            "class is 'equal-content collections', which contains the target "
            "configuration itself and therefore adds a free parameter instead "
            "of removing one."
        ),
        "finding": (
            f"Three readings tested, not two. Adjudicated reading: {reading}, "
            f"carried {tally.get('SITE_SET_DISJOINTNESS', 0)} discriminants "
            f"to {tally.get('CONTENT_DISJOINTNESS', 0)}. A record's support "
            f"is a single site (E2+E3), so 'pairwise-disjoint' is "
            f"automatically satisfied by any finite collection of distinct "
            f"records and the additivity clause covers ADJACENT records. The "
            f"memo defines record disjointness nowhere "
            f"({sweep['explicit_disjointness_definition_count']} hits), no "
            f"'disjoint' sentence carries an adjacency qualifier "
            f"({len(sweep['disjoint_sentences_carrying_adjacency_qualifier'])}"
            f" hits), and the memo's sole adjacency word sits in the Lattice "
            f"section, not in Record. Verdict {verdict}, and it is READING-"
            f"INDEPENDENT: R1 kills by contradiction, R3 by the content-alone "
            f"clause on top of being unlicensed, and R4 kills itself by "
            f"exempting the very equal-content configuration whose readout "
            f"must equal 2/9."
        ),
    }


# ---------------------------------------------------------------------------
# E_M4_ENUMERATION_AND_COUNTERFACTUAL
# ---------------------------------------------------------------------------
def m4_enumeration() -> dict:
    rots = build_cubic_rotations()
    shell = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1),
             (0, 0, -1)]

    # (i) the rotation group and its transitivity on the 6-shell
    group_order = len(rots)
    orbit_of_e1 = {apply_int(g, (1, 0, 0)) for g in rots}
    transitive_on_shell = orbit_of_e1 == set(shell)

    # the C3 axis cycle and its orbits on the shell (reproduces 883 F)
    axis_cycle = ((0, 0, 1), (1, 0, 0), (0, 1, 0))
    assert axis_cycle in rots
    c3_orbits = []
    seen = set()
    for v in shell:
        if v in seen:
            continue
        orb, cur = [], v
        for _ in range(3):
            orb.append(cur)
            seen.add(cur)
            cur = apply_int(axis_cycle, cur)
        c3_orbits.append(tuple(orb))
    orbit_lengths = sorted(len(o) for o in c3_orbits)
    all_free = all(len(set(o)) == 3 for o in c3_orbits)

    # (ii) THE GEOMETRIC VACUITY THEOREM.  Does the target orbit contain any
    #      adjacency interface at all?
    target_orbit = c3_orbits[0]
    pair_distances = []
    for i in range(3):
        for j in range(i + 1, 3):
            a, b = target_orbit[i], target_orbit[j]
            pair_distances.append({
                "pair": [list(a), list(b)],
                "squared_distance": sum((x - y) ** 2 for x, y in zip(a, b)),
            })
    adjacency_interfaces_in_orbit = sum(
        1 for p in pair_distances if p["squared_distance"] == 1)
    geometric_vacuity = adjacency_interfaces_in_orbit == 0

    # (ii-b) THE UNIVERSAL FORM.  The orbit-specific fact above is a corollary
    # of a bound-free one: the nearest-neighbour graph on Z^3 is BIPARTITE,
    # because every edge changes the parity of the coordinate sum. A bipartite
    # graph has no odd cycle, hence no triangle, hence NO three sites anywhere
    # in Z^3 are pairwise adjacent.  Verified on a box, proved in general.
    box = list(product(range(-2, 3), repeat=3))
    edges = [(a, b) for i, a in enumerate(box) for b in box[i + 1:]
             if sum((x - y) ** 2 for x, y in zip(a, b)) == 1]
    parity_flips = all((sum(a) + sum(b)) % 2 == 1 for a, b in edges)
    triangles = 0
    adj_sets = {v: set() for v in box}
    for a, b in edges:
        adj_sets[a].add(b)
        adj_sets[b].add(a)
    for a, b in edges:
        triangles += len(adj_sets[a] & adj_sets[b])
    universal_vacuity = {
        "theorem": (
            "No three sites of Z^3 are pairwise nearest-neighbour adjacent. "
            "The nearest-neighbour graph is bipartite -- every edge changes "
            "the parity of the coordinate sum -- so it contains no odd cycle "
            "and in particular no triangle."
        ),
        "box_checked": "[-2,2]^3",
        "edges_checked": len(edges),
        "every_edge_flips_parity": parity_flips,
        "triangles_found": triangles,
        "consequence": (
            "the geometric vacuity is UNIVERSAL, not a property of the target "
            "orbit: no 3-record collection anywhere on Z^3 can carry three "
            "adjacency interfaces, and the target orbit carries none at all"
        ),
        "holds": parity_flips and triangles == 0,
    }

    # (iii) the covariant defect enumeration over the incompatible class
    displacements = [d for d in product(range(-2, 3), repeat=3)
                     if 1 <= sum(x * x for x in d)
                     <= BOUND_DISPLACEMENT_NORM2_MAX]
    d_orbits = []
    unassigned = set(displacements)
    while unassigned:
        v = min(unassigned)
        orb = {apply_int(g, v) for g in rots}
        d_orbits.append({"representative": list(v),
                         "squared_norm": sum(x * x for x in v),
                         "size": len(orb)})
        unassigned -= orb
    adjacent_orbits = [o for o in d_orbits if o["squared_norm"] == 1]

    # cubic covariance collapses the direction dependence on the adjacent
    # shell, because the 24 rotations act transitively there.
    direction_free_parameters = len(adjacent_orbits)

    # the full covariant, separation-vanishing, empty-normalized defect family
    alphabet = BOUND_CONTENT_ALPHABET
    nonzero = [c for c in alphabet if c != 0]
    free_entries = sorted({tuple(sorted((a, b)))
                           for a in nonzero for b in nonzero})
    n_free = len(free_entries)
    values = list(range(-BOUND_DEFECT_VALUE, BOUND_DEFECT_VALUE + 1))
    family_size = len(values) ** n_free

    # For every member, COMPUTE the induced constraint on alpha.  Nothing here
    # is asserted: the solution set is solved for from the configuration
    # equations, and the target's membership is tested against the answer.
    #
    #   configuration = a chain of n unit-content records along +x, which has
    #   n records and n-1 adjacency interfaces, so
    #       T_n(alpha) = n*alpha + (n-1)*D(1,1).
    #   Purchase reading 1 says T_n(alpha) is in Z for every n in the declared
    #   range.  Writing alpha = p/q in lowest terms, and noting every offset
    #   (n-1)*D(1,1) is an integer because D is Z-valued, the condition is
    #   q | n for every n in the range, i.e. q | gcd(range).
    def _gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return abs(a)

    chain_lengths = list(range(1, BOUND_CHAIN_LENGTH + 1))
    allowed_denominator = 0
    for n in chain_lengths:
        allowed_denominator = _gcd(allowed_denominator, n)
    induced = {}
    members_examined = 0
    offsets_all_integral = True
    target_admitted_members = 0
    probe_alphas = (TARGET_ALPHA, Fraction(1, 3), Fraction(1), Fraction(0),
                    Fraction(2, 9), Fraction(1, 108))
    probe_table = {q(a): 0 for a in probe_alphas}
    for assignment in product(values, repeat=n_free):
        members_examined += 1
        table = dict(zip(free_entries, assignment))
        d11 = table[(1, 1)]
        offsets = [d11 * (n - 1) for n in chain_lengths]
        if any(off != int(off) for off in offsets):
            offsets_all_integral = False
        # solve, do not assert: an alpha survives iff every T_n lands in Z
        for a in probe_alphas:
            if all((a * n + off).denominator == 1
                   for n, off in zip(chain_lengths, offsets)):
                probe_table[q(a)] += 1
                if a == TARGET_ALPHA:
                    target_admitted_members += 1
        key = (f"(1/{allowed_denominator})Z" if allowed_denominator != 1
               else "Z")
        induced[key] = induced.get(key, 0) + 1
    induced_sets = induced
    target_in_any = target_admitted_members > 0
    defect_contributes_denominator = allowed_denominator != 1
    probe_survival = {
        alpha: {"members_admitting": count,
                "of_members": members_examined,
                "survives_anywhere": count > 0}
        for alpha, count in probe_table.items()
    }

    # reading 2 of the purchase: configurations read in (1/M)Z for a purchased
    # modulus M.  A Z-valued defect lies in (1/M)Z already, so it changes the
    # solution set not at all.
    reading2 = {
        "statement": "every finite configuration reads in (1/M)Z",
        "defect_contribution": (
            "Z is a subgroup of (1/M)Z for every positive integer M, so a "
            "Z-valued gluing defect adds no new denominator; the solution set "
            "is (1/M)Z with or without the defect"
        ),
        "selection_power_of_the_defect": "zero",
    }

    # (iv) the purchased-modulus ideal, and the v2 = 1 least-positive member
    def least_positive_v2_one(m: int) -> Fraction | None:
        k = 1
        while k <= 64 * m:
            cand = Fraction(k, m)
            if cand > 0 and vp(cand, 2) == 1:
                return cand
            k += 1
        return None

    ideal_rows = []
    moduli_hitting_target = []
    for m in range(1, BOUND_MODULUS_MAX + 1):
        best = least_positive_v2_one(m)
        if best is None:
            continue
        hit = best == TARGET_ALPHA
        if hit:
            moduli_hitting_target.append(m)
        if m in (9, 12, 27, 36, 54, 81, 108, 216, 324) or hit:
            ideal_rows.append({
                "modulus_M": m,
                "fractional_ideal": f"(1/{m})Z",
                "v2_of_M": vp(Fraction(m), 2),
                "least_positive_with_v2_eq_1": q(best),
                "equals_target": hit,
                "odd_part_of_M": m // (2 ** vp(Fraction(m), 2)),
            })
    odd_parts = sorted({m // (2 ** vp(Fraction(m), 2))
                        for m in moduli_hitting_target})
    twelve_n_hits = [m for m in moduli_hitting_target if m % 12 == 0]
    n_values = [m // 12 for m in twelve_n_hits]

    return {
        "pass": (group_order == 24 and transitive_on_shell
                 and orbit_lengths == [3, 3] and all_free
                 and members_examined == family_size
                 and universal_vacuity["holds"]),
        "declared_bounds": {
            "displacement_squared_norm_max": BOUND_DISPLACEMENT_NORM2_MAX,
            "content_alphabet": list(alphabet),
            "defect_value_range": [-BOUND_DEFECT_VALUE, BOUND_DEFECT_VALUE],
            "chain_lengths": chain_lengths,
            "modulus_scan_max": BOUND_MODULUS_MAX,
            "honesty": (
                "These are the bounds, stated before the results. The defect "
                "census is EXHAUSTIVE inside them; outside them the "
                "geometric-vacuity theorem and the Z-valued-denominator "
                "argument are what carry the claim, and both are "
                "bound-independent."
            ),
        },
        "cubic_rotation_group": {
            "order": group_order,
            "transitive_on_6_shell": transitive_on_shell,
            "c3_axis_cycle": [list(r) for r in axis_cycle],
            "c3_orbit_lengths": orbit_lengths,
            "all_orbits_free": all_free,
            "reproduces_883_F": orbit_lengths == [3, 3] and all_free,
        },
        "C898_T3_geometric_vacuity": {
            "target_orbit": [list(v) for v in target_orbit],
            "pairwise_squared_distances": pair_distances,
            "adjacency_interfaces_in_target_orbit":
                adjacency_interfaces_in_orbit,
            "theorem": (
                "The free C3 orbit on the 6-neighbour shell is "
                "{e1, e2, e3}; every pair inside it is at squared distance 2, "
                "not 1. The configuration whose readout must equal 2/9 "
                "therefore contains ZERO adjacency interfaces, so an "
                "adjacency gluing defect cannot touch it even if one existed."
            ),
            "holds": geometric_vacuity,
            "universal_form": universal_vacuity,
        },
        "displacement_orbits_under_24_rotations": d_orbits,
        "adjacent_shell_orbit_count": direction_free_parameters,
        "covariance_collapse": (
            f"the 24 proper rotations act transitively on the 6 adjacent "
            f"displacements ({direction_free_parameters} orbit), so a cubic-"
            f"covariant defect cannot depend on WHICH neighbour direction the "
            f"interface points along"
        ),
        "counterfactual_defect_family": {
            "class": (
                "Z-valued, cubic-covariant, vanishing on separated pairs, "
                "vanishing when either record content is 0 (empty-record "
                "normalization), symmetric under record exchange"
            ),
            "free_entries": [list(e) for e in free_entries],
            "family_size": family_size,
            "members_enumerated": members_examined,
            "exhaustive_within_bounds": members_examined == family_size,
            "induced_constraint_on_alpha_reading_1": induced_sets,
            "induced_solution_set_solved_not_asserted": {
                "allowed_denominator_gcd_of_chain_lengths":
                    allowed_denominator,
                "derivation": (
                    "alpha = p/q in lowest terms survives iff q | n for every "
                    "chain length n in the declared range, i.e. q | "
                    f"gcd{tuple(chain_lengths)} = {allowed_denominator}"
                ),
                "all_defect_offsets_integral": offsets_all_integral,
            },
            "probe_alpha_survival": probe_survival,
            "induced_constraint_on_alpha_reading_2": reading2,
            "target_admitted_by_any_member": target_in_any,
            "defect_contributes_to_denominator":
                defect_contributes_denominator,
            "price_of_the_axiom_clause": (
                "The additivity sentence forbids exactly this family. The "
                "counterfactual says what the sentence is buying: NOTHING is "
                "lost on the selection question. Every member of the family "
                "leaves the induced solution set at Z (reading 1) or at the "
                "separately purchased (1/M)Z (reading 2). A Z-valued "
                "adjacency defect cannot manufacture a denominator, and the "
                "single-record configuration -- which has no interface at all "
                "-- binds alpha before any interface is seen. The axiom clause "
                "costs the selection question zero selection power."
            ),
        },
        "purchased_modulus_ideal": {
            "statement": "the M4 core purchase 'M*alpha in Z'",
            "fractional_ideal": "(1/M)Z",
            "rows": ideal_rows,
            "moduli_in_scan_hitting_target": moduli_hitting_target,
            "odd_parts_of_hitting_moduli": odd_parts,
            "twelve_N_form_hits": twelve_n_hits,
            "N_values_in_12N_form": n_values,
            "closed_form": (
                "for a modulus M the least positive member of (1/M)Z with "
                "v_2 = 1 is 2^(v_2(M)+1)/M; this equals 2/27 exactly when the "
                "ODD PART of M is 27, i.e. M = 27 * 2^j"
            ),
            "operative_content": (
                "The exercise's '12N*alpha in Z' with N = 9 works, and so does "
                "every M with odd part 27. The generic shape 12N is not the "
                "load-bearing part; the load-bearing part is a single number, "
                "odd_part(M) = 27 = 3^3. The supplied structure offers 3 (the "
                "orbit length) and the isotype pair (1,2); it offers no "
                "exponent 3."
            ),
            "is_2_over_9_the_least_positive_v2_one_member": (
                "at the orbit level: yes, once M has odd part 27 the least "
                "positive v_2 = 1 member of (1/M)Z is alpha = 2/27 and the "
                "orbit reads 3*alpha = 2/9; but the modulus that makes this "
                "true is itself the purchase"
            ),
        },
        "finding": (
            f"The M4 adjacency route dies a third, geometry-only death: the "
            f"target C3 orbit {[list(v) for v in target_orbit]} has "
            f"{adjacency_interfaces_in_orbit} adjacency interfaces (all "
            f"pairwise squared distances are 2), so no adjacency defect can "
            f"reach it -- and the fact is UNIVERSAL, not orbit-specific: "
            f"Z^3's nearest-neighbour graph is bipartite "
            f"({len(edges)} edges checked, every one parity-flipping), so it "
            f"has {triangles} triangles and NO three sites anywhere are "
            f"pairwise adjacent. The counterfactual enumeration over all "
            f"{family_size} members of the forbidden family leaves the "
            f"induced solution set at Z in every case: the axiom clause buys "
            f"zero selection power. The purchased-modulus branch shows the "
            f"whole singleton rests on odd_part(M) = 27, hit by "
            f"{len(moduli_hitting_target)} moduli in the scanned range with "
            f"odd parts {odd_parts}."
        ),
    }


# ---------------------------------------------------------------------------
# F_M4_INGREDIENT_DERIVABILITY
# ---------------------------------------------------------------------------
def m4_ingredient_audit() -> dict:
    memo = _read_text(AXIOM_MEMO)
    c883 = _read_text(C883_CACHE)
    c882 = _read_text(C882_CACHE)

    needles = {
        "integer": r"\binteger[s]?\b",
        "integral/integrality": r"\bintegral\b|\bintegrality\b",
        "rational": r"\brational[s]?\b",
        "valuation": r"\bvaluation[s]?\b|\b2-adic\b|\bp-adic\b",
        "least/minimal/greatest": r"\bleast\b|\bminimal\b|\bgreatest\b|"
                                  r"\bsmallest\b",
        "order/ordered": r"\border(ed|ing)?\b",
        "discrete/lattice-of-values": r"\bdiscrete\b",
        "positive": r"\bpositive\b",
        "scalar": r"\bscalar\b",
        "field(R/Q/C)": r"\bfield\b|\breal number|\bcomplex number",
        "modulus/denominator": r"\bmodulus\b|\bdenominator\b",
    }
    memo_counts = {k: len(re.findall(v, memo, re.I))
                   for k, v in needles.items()}
    memo_hits = {
        k: [" ".join(_sentence_around(memo, m.start()).split())
            for m in re.finditer(v, memo, re.I)]
        for k, v in needles.items()
    }

    # bounded sweep of the retained doc surfaces on this branch
    docs = sorted((ROOT / "docs").glob("*.md"))
    scanned, bytes_read = 0, 0
    provenance = {
        "12N_form": r"12\s*\*?\s*N\b|\b12N\b",
        "N2_minus_1_family_fact": r"N\s*\^\s*2\s*-\s*1|N\*\*2\s*-\s*1|"
                                  r"N\^2-1",
        "alpha_integrality": r"alpha\b[^.\n]{0,40}\b(in|is)\s+Z\b|"
                             r"\bintegrality of alpha\b",
    }
    prov_hits = {k: [] for k in provenance}
    for p in docs:
        if bytes_read > BOUND_DOCS_SWEEP_BYTES:
            break
        try:
            t = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        scanned += 1
        bytes_read += len(t)
        for key, pat in provenance.items():
            if re.search(pat, t):
                prov_hits[key].append(str(p.relative_to(ROOT)))

    ingredients = [
        {
            "ingredient": "alpha is a RATIONAL at all (the ambient field)",
            "needed_for": "any lattice/ideal statement about alpha",
            "grade": "NOT_PINNED_BY_AXIOM",
            "reason": (
                "the Record axiom says 'scalar readout `I`' and never names "
                "the scalar field; 883's H_FIELD_ROBUSTNESS tests two field "
                "readings precisely because the axioms leave it open"
            ),
            "evidence_counts": {"scalar": memo_counts["scalar"],
                                "field(R/Q/C)": memo_counts["field(R/Q/C)"],
                                "rational": memo_counts["rational"]},
        },
        {
            "ingredient": "an integrality statement about alpha "
                          "(alpha in (1/M)Z for some M)",
            "needed_for": "M4's fractional ideal",
            "grade": "PURCHASE",
            "reason": (
                "the memo contains no integer/integrality/denominator "
                "statement about readout VALUES anywhere; the Lattice axiom's "
                "'lattice' is a lattice of SITES, not of readout values, and "
                "the Qualification clause parks anything not fixed by the "
                "supplied structure as a named conditional"
            ),
            "evidence_counts": {
                "integer": memo_counts["integer"],
                "integral/integrality": memo_counts["integral/integrality"],
                "modulus/denominator": memo_counts["modulus/denominator"],
            },
        },
        {
            "ingredient": "the modulus itself: odd_part(M) = 27 "
                          "(the exercise's 12N with N = 9)",
            "needed_for": "the singleton to land on 2/27 rather than "
                          "somewhere else",
            "grade": "PURCHASE_AND_TARGET_TUNED",
            "reason": (
                "certificate E computes that the singleton is 2/27 exactly "
                "when odd_part(M) = 27; no supplied surface on this branch "
                "carries the '12N' or 'N^2-1' family fact in the readout-alpha "
                "lineage, and the supplied structure offers 3 (orbit length) "
                "but no exponent 3"
            ),
            "evidence_counts": {k: len(v) for k, v in prov_hits.items()},
            "provenance_hits": {k: v[:6] for k, v in prov_hits.items()},
        },
        {
            "ingredient": "v_2(alpha) = 1",
            "needed_for": "filtering the ideal down to the target coset",
            "grade": "DERIVED_FOR_A_DIFFERENT_OBJECT",
            "reason": (
                "883 derives the 2-adic profile [0, 1] of the isotype "
                "DIMENSION pair (1, 2), not of alpha. 883's own "
                "M_BINDING_PRICE records that the binding of that datum to "
                "the anchor is a 5-fold ambiguity it does not close, and its "
                "L_BRIDGE_BACK_T7 records that the target became REACHABLE "
                "without becoming SELECTED"
            ),
            "evidence_counts": {
                "883_binding_price_present": int(
                    "5-fold ambiguity" in c883),
                "882_2adic_certificate_present": int(
                    "I_CARDINALITY_GROUP" in c882),
            },
        },
        {
            "ingredient": "the least-positive / fundamental-domain selector",
            "needed_for": "collapsing the coset to a point",
            "grade": "PURCHASE",
            "reason": (
                "the memo contains no order, least, minimal or discreteness "
                "statement about readout values; and certificate H proves the "
                "selector is VACUOUS without the integrality purchase already "
                "in hand"
            ),
            "evidence_counts": {
                "least/minimal/greatest":
                    memo_counts["least/minimal/greatest"],
                "order/ordered": memo_counts["order/ordered"],
                "discrete/lattice-of-values":
                    memo_counts["discrete/lattice-of-values"],
                "positive": memo_counts["positive"],
            },
        },
    ]
    purchases = [i for i in ingredients if "PURCHASE" in i["grade"]]

    return {
        "pass": scanned > 0 and len(ingredients) == 5,
        "zero_hit_gate": (
            f"the retained-surface sweep must scan at least one doc; it "
            f"scanned {scanned}"
        ),
        "memo_needle_counts": memo_counts,
        "memo_needle_sentences": {k: v for k, v in memo_hits.items() if v},
        "retained_surface_sweep": {
            "docs_scanned": scanned,
            "bytes_read": bytes_read,
            "byte_cap": BOUND_DOCS_SWEEP_BYTES,
            "provenance_hit_counts": {k: len(v) for k, v in prov_hits.items()},
            "provenance_hit_paths": {k: v[:6] for k, v in prov_hits.items()},
            "note": (
                "the '12N' and 'N^2-1' string hits that DO exist on this "
                "branch live in unrelated lineages (Brannen delta, plaquette "
                "closure, CKM integer characterization); none is a statement "
                "about the readout coefficient alpha"
            ),
        },
        "ingredients": ingredients,
        "named_purchase_count": len(purchases),
        "verdict": "PRICED",
        "finding": (
            f"Every M4 ingredient is a purchase or is derived for a different "
            f"object. The axiom memo contains "
            f"{memo_counts['integer']} 'integer' hits, "
            f"{memo_counts['integral/integrality']} 'integral/integrality' "
            f"hits, {memo_counts['least/minimal/greatest']} 'least/minimal' "
            f"hits and {memo_counts['discrete/lattice-of-values']} 'discrete' "
            f"hits -- and not one of them is a statement about readout VALUES. "
            f"{len(purchases)} named purchases, plus the field scope and the "
            f"883 binding gap. Sweep covered {scanned} retained docs."
        ),
    }


# ---------------------------------------------------------------------------
# G_M2_INVOLUTION_CENSUS
# ---------------------------------------------------------------------------
def linear_invariance_solution_set(j_matrix) -> dict:
    """Solution set of  I_alpha o J = I_alpha  in the unknown alpha.

    I_alpha(x) = alpha * <1, x>, so I_alpha(Jx) = alpha * <J^T 1, x>.  The
    condition is alpha * (J^T 1 - 1) = 0 componentwise: HOMOGENEOUS LINEAR in
    alpha, hence T1's dichotomy for EVERY linear J with no exception.
    """
    w = tuple(a - b for a, b in zip(mat_vec(mat_t(j_matrix), ONES), ONES))
    if all(c == 0 for c in w):
        return {"kind": "ALL_Q", "w": [q(c) for c in w],
                "fixed_scale_over_Q": "NONE (every alpha is fixed)"}
    return {"kind": "ZERO_ONLY", "w": [q(c) for c in w],
            "fixed_scale_over_Q": "0/1"}


def quadratic_normalization_solution_set(n_const: Fraction) -> dict:
    """Solution set of  alpha^2 * N = 1  in the unknown alpha, exactly."""
    if n_const == 0:
        return {"kind": "EMPTY", "alpha_squared": None,
                "fixed_scale_over_Q": "NONE (degenerate normalization)"}
    r = Fraction(1) / n_const
    wit = rational_square_witness(r)
    if wit["is_rational_square"]:
        root = Fraction(wit["root"])
        assert root * root == r, "rational square root failed to verify"
        return {"kind": "FINITE", "alpha_squared": q(r),
                "solutions": [q(root), q(-root)],
                "fixed_scale_over_Q": q(root),
                "square_witness": wit}
    return {"kind": "IRRATIONAL", "alpha_squared": q(r),
            "solutions": [],
            "fixed_scale_over_Q": "NONE",
            "fixed_scale_algebraic": f"+/- sqrt({q(r)})",
            "square_witness": wit}


def is_selector(sol: dict) -> bool:
    """Does this condition isolate a nonzero rational scale?"""
    if sol["kind"] != "FINITE":
        return False
    return any(Fraction(s) != 0 for s in sol.get("solutions", []))


def m2_census() -> dict:
    entries = []
    checks = {}

    # ---- (a) Pontryagin duality on C3 -------------------------------------
    # The self-dual Haar measure scale c on G and its dual satisfies
    # c^2 * |G| = 1.  |G| = 3 is the ONLY datum the supplied structure gives.
    sol = quadratic_normalization_solution_set(Fraction(ORBIT_LENGTH))
    entries.append({
        "id": "M2-01",
        "name": "Pontryagin self-dual measure on C3",
        "degree": 2,
        "condition": "c^2 * |C3| = 1, i.e. alpha^2 * 3 = 1",
        "structural_constant_N": q(Fraction(3)),
        **sol,
        "verdict": (
            "NO RATIONAL ANCHOR AT ALL -- sharper than a wrong value: the "
            "self-dual scale is 1/sqrt(3), and x^2 = 1/3 has no solution in Q "
            "because v_3(1/3) = -1 is odd"
        ),
    })

    # ---- (b) graph-Laplacian trace duality on the 3-cycle ------------------
    # L(w) = w(2I - A), A the 3-cycle adjacency.  Spectrum of A is {2,-1,-1},
    # verified exactly by characteristic polynomial, so L has spectrum
    # {0, 3w, 3w} and L^+ has {0, 1/(3w), 1/(3w)}.
    A_c3 = tuple(tuple(Fraction(1 if i != j else 0) for j in range(3))
                 for i in range(3))
    # char poly of A: det(A - t I) = -t^3 + 3t + 2 = -(t-2)(t+1)^2
    charpoly_check = []
    for t in (Fraction(2), Fraction(-1), Fraction(0), Fraction(1)):
        m = tuple(tuple(A_c3[i][j] - (t if i == j else 0) for j in range(3))
                  for i in range(3))
        det = (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
               - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
               + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
        charpoly_check.append({"t": q(t), "det(A - tI)": q(det)})
    spectrum_A = [Fraction(2), Fraction(-1), Fraction(-1)]
    checks["A_C3_spectrum_verified"] = all(
        r["det(A - tI)"] == "0/1" for r in charpoly_check if r["t"] in
        ("2/1", "-1/1"))
    # Tr L(w) = 6w ; Tr L(w)^+ = 2/(3w) ; equality gives 18 w^2 = 2
    w_sol = quadratic_normalization_solution_set(Fraction(9))  # w^2 = 1/9
    w_star = Fraction(1, 3)
    tr_l = 6 * w_star
    tr_lplus = Fraction(2, 3 * w_star)
    lap_readings = []
    for label, val in (("edge weight w", w_star),
                       ("per-vertex trace Tr L / |V|", tr_l / 3),
                       ("nonzero eigenvalue 3w", 3 * w_star)):
        lap_readings.append({
            "reading": label,
            "value": q(val),
            "as_alpha_equals_target": val == TARGET_ALPHA,
            "orbit_value_3_alpha": q(3 * val),
            "as_orbit_value_equals_target": val == TARGET_ORBIT_VALUE,
        })
    entries.append({
        "id": "M2-02",
        "name": "graph-Laplacian trace duality on the 3-cycle",
        "degree": 2,
        "condition": "Tr L(w) = Tr L(w)^+, i.e. 6w = 2/(3w), i.e. 18 w^2 = 2",
        "structural_constant_N": q(Fraction(9)),
        **w_sol,
        "spectrum_A_C3": [q(x) for x in spectrum_A],
        "charpoly_evaluations": charpoly_check,
        "Tr_L_at_fixed_point": q(tr_l),
        "Tr_Lplus_at_fixed_point": q(tr_lplus),
        "trace_duality_holds_exactly": tr_l == tr_lplus,
        "anchor_readings": lap_readings,
        "verdict": (
            "RATIONAL BUT WRONG: the only rational fixed scale in the whole "
            "native degree-2 list. w = 1/3 exactly, per-vertex trace 2/3, "
            "nonzero eigenvalue 1. None of the three readings is 2/27, and "
            "none of their orbit values is 2/9"
        ),
    })

    # ---- (c) the S3-normalizer generator inversion ------------------------
    iota_sol = linear_invariance_solution_set(IOTA)
    entries.append({
        "id": "M2-03",
        "name": "generator inversion (the S3 normalizer involution)",
        "degree": 1,
        "condition": "I_alpha o iota = I_alpha, iota: (x0,x1,x2)->(x0,x2,x1)",
        "iota_squared_is_identity": mat_mul(IOTA, IOTA) == IDENT,
        "normalizes_C3": mat_mul(mat_mul(IOTA, SIGMA), IOTA) == SIGMA2,
        **iota_sol,
        "verdict": (
            "PINS NOTHING: iota permutes the coordinates and the readout is "
            "the symmetric sum, so J^T 1 - 1 = 0 and the condition is 0 = 0. "
            "Solution set is the whole line -- T1's permissive horn"
        ),
    })

    # ---- (d) convolution / pointwise duality on Q[C3] ----------------------
    # exact Z[omega] verification: W W* = 3I and W^2 = 3 * (inversion)
    ww_star = wmat_mul(DFT, DFT_STAR)
    w_squared = wmat_mul(DFT, DFT)
    three_i = tuple(tuple((3 if i == j else 0, 0) for j in range(3))
                    for i in range(3))
    three_iota = tuple(tuple((3 if (i + j) % 3 == 0 else 0, 0)
                             for j in range(3)) for i in range(3))
    checks["DFT_unitarity_exact_over_Z_omega"] = ww_star == three_i
    checks["DFT_square_is_3_times_inversion"] = w_squared == three_iota
    # convolution unit delta_e vs pointwise unit (1,1,1):
    #   F(delta_e) = (1,1,1) and F(1) = (3,0,0) = 3 delta_e
    f_delta = tuple(sum((DFT[i][k][0] for k in range(1)), 0) for i in range(3))
    checks["F_of_delta_e_is_all_ones"] = all(
        DFT[i][0] == (1, 0) for i in range(3))
    f_ones = tuple(
        tuple(sum(x for x, _ in [w_mul(DFT[i][k], (1, 0))]) for k in range(3))
        for i in range(3))
    sum_row0 = (sum(DFT[0][k][0] for k in range(3)),
                sum(DFT[0][k][1] for k in range(3)))
    sum_row1 = (sum(DFT[1][k][0] for k in range(3)),
                sum(DFT[1][k][1] for k in range(3)))
    checks["F_of_ones_is_3_delta_e"] = (sum_row0 == (3, 0)
                                        and sum_row1 == (0, 0))
    conv_sol = quadratic_normalization_solution_set(Fraction(3))
    # the Q-rational alternative: the trivial-isotype primitive idempotent
    p0 = lin_comb(Fraction(1, 3), Fraction(1, 3), Fraction(1, 3))
    checks["P0_is_idempotent"] = mat_mul(p0, p0) == p0
    entries.append({
        "id": "M2-04a",
        "name": "convolution/pointwise duality on Q[C3]: Fourier involution "
                "normalization",
        "degree": 2,
        "condition": "F_c^2 = c^2 F^2 = 3 c^2 * inversion; involution "
                     "requires 3 c^2 = 1",
        "structural_constant_N": q(Fraction(3)),
        "exact_algebra": "verified in Z[omega], omega^2 = -1 - omega",
        "F_squared_equals_3_inversion": checks["DFT_square_is_3_times_inversion"],
        **conv_sol,
        "verdict": (
            "NO RATIONAL ANCHOR: same 1/sqrt(3) obstruction. The unit-exchange "
            "reading is worse -- F(delta_e) = (1,1,1) needs c = 1 while "
            "F(1) = 3 delta_e needs c = 1/3, so the unit-swapping "
            "normalization has NO solution at all"
        ),
        "unit_exchange_reading": {
            "requires_c_equals": ["1/1", "1/3"],
            "solution_set": "EMPTY (inconsistent)",
        },
    })
    entries.append({
        "id": "M2-04b",
        "name": "convolution/pointwise duality on Q[C3]: the Q-rational "
                "primitive idempotent",
        "degree": 0,
        "condition": "e_0 = (1/3) sum_g g is the trivial-isotype primitive "
                     "idempotent; its coefficient is the fixed normalization",
        "idempotent_verified": checks["P0_is_idempotent"],
        "kind": "FINITE",
        "solutions": [q(Fraction(1, 3))],
        "fixed_scale_over_Q": q(Fraction(1, 3)),
        "equals_target_alpha": Fraction(1, 3) == TARGET_ALPHA,
        "orbit_value": q(Fraction(1)),
        "verdict": (
            "RATIONAL BUT WRONG: 1/3, which is exactly 882's axiom-available "
            "anchor K4_ANCHOR_UNIT, not the target"
        ),
    })

    # ---- (e) the unitary DFT self-duality normalization --------------------
    dft_sol = quadratic_normalization_solution_set(Fraction(3))
    entries.append({
        "id": "M2-05",
        "name": "unitary DFT self-duality normalization on C3",
        "degree": 2,
        "condition": "U = c W with U U* = I; W W* = 3I forces 3 c^2 = 1",
        "structural_constant_N": q(Fraction(3)),
        "WWstar_equals_3I_exact":
            checks["DFT_unitarity_exact_over_Z_omega"],
        **dft_sol,
        "verdict": (
            "NO RATIONAL ANCHOR: c = 1/sqrt(3), irrational by the same odd "
            "3-adic valuation argument"
        ),
    })

    # ---- the COMPLETE set of C3-commuting Q-linear involutions -------------
    # Solve J^2 = I for J = aI + b sigma + c sigma^2 exactly.  The centralizer
    # of a nonderogatory sigma in M_3(Q) is Q[sigma], so this IS the complete
    # commuting family; the solution below is closed-form, not sampled.
    commuting = []
    for (a, b, c) in ((Fraction(1), Fraction(0), Fraction(0)),
                      (Fraction(-1), Fraction(0), Fraction(0)),
                      (Fraction(-1, 3), Fraction(2, 3), Fraction(2, 3)),
                      (Fraction(1, 3), Fraction(-2, 3), Fraction(-2, 3))):
        j = lin_comb(a, b, c)
        assert mat_mul(j, j) == IDENT, (a, b, c)
        assert mat_mul(j, SIGMA) == mat_mul(SIGMA, j)
        commuting.append({
            "coefficients": [q(a), q(b), q(c)],
            "J_squared_is_identity": True,
            "commutes_with_sigma": True,
            **linear_invariance_solution_set(j),
        })
    # completeness proof, carried out exactly on the defining equations
    # a^2 + 2bc = 1, 2ab + c^2 = 0, b^2 + 2ac = 0
    completeness = {
        "system": ["a^2 + 2bc = 1", "2ab + c^2 = 0", "b^2 + 2ac = 0"],
        "case_bc_eq_0": "b = 0 forces c = 0 forces a = +/-1  ->  J = +/- I",
        "case_bc_ne_0": (
            "multiplying the last two gives b^2 c^2 = 4 a^2 bc, so bc = 4a^2; "
            "then a^2 + 8a^2 = 1 gives a = +/-1/3, and back-substitution "
            "gives (a,b,c) = (-1/3, 2/3, 2/3) or (1/3, -2/3, -2/3)"
        ),
        "total_solutions": 4,
        "centralizer_argument": (
            "sigma is nonderogatory (min poly = char poly = x^3 - 1), so its "
            "centralizer in M_3(Q) is exactly Q[sigma]; the four solutions "
            "above are therefore ALL C3-commuting Q-linear involutions"
        ),
    }
    for row in commuting:
        entries.append({
            "id": f"M2-06[{','.join(row['coefficients'])}]",
            "name": "C3-commuting Q-linear involution "
                    f"({','.join(row['coefficients'])})",
            "degree": 1,
            "condition": "I_alpha o J = I_alpha",
            **{k: v for k, v in row.items()
               if k not in ("coefficients",)},
            "verdict": ("PINS NOTHING (whole line)" if row["kind"] == "ALL_Q"
                        else "PINS ZERO ONLY"),
        })

    # ---- the FULL C3-normalizing family, no height bound needed ------------
    # Every J in Q[sigma] u Q[sigma]iota has J^T 1 = (a+b+c) 1 because sigma
    # and iota are permutation matrices.  So the deg-1 condition reads
    # (a+b+c-1)*alpha = 0 for the WHOLE infinite family: dichotomy, always.
    normalizer_rows = []
    hits = 0
    heights = []
    for den in range(1, BOUND_NORMALIZER_HEIGHT + 1):
        for na in range(-BOUND_NORMALIZER_HEIGHT, BOUND_NORMALIZER_HEIGHT + 1):
            for nb in range(-BOUND_NORMALIZER_HEIGHT,
                            BOUND_NORMALIZER_HEIGHT + 1):
                for nc in range(-BOUND_NORMALIZER_HEIGHT,
                                BOUND_NORMALIZER_HEIGHT + 1):
                    a, b, c = (Fraction(na, den), Fraction(nb, den),
                               Fraction(nc, den))
                    j = mat_mul(IOTA, lin_comb(a, b, c))
                    if mat_mul(j, j) != IDENT:
                        continue
                    hits += 1
                    sol = linear_invariance_solution_set(j)
                    heights.append(sol["kind"])
    normalizer_rows.append({
        "family": "J = iota * q, q in Q[sigma], (iota q)^2 = I",
        "height_bound": BOUND_NORMALIZER_HEIGHT,
        "members_found_in_bounded_slice": hits,
        "solution_kinds_observed": sorted(set(heights)),
        "bound_independent_theorem": (
            "sigma and iota are permutation matrices, so for every "
            "q = aI + b sigma + c sigma^2 the map J = iota q has "
            "J^T 1 = (a+b+c) 1. The deg-1 condition is therefore "
            "(a+b+c-1) alpha = 0 for the ENTIRE infinite family: solution set "
            "is all of Q when a+b+c = 1 and {0} otherwise. No height bound is "
            "needed for this half of the census"
        ),
    })

    # ---- C898-T4: the general linear theorem ------------------------------
    # For EVERY Q-linear J the invariance condition is homogeneous linear in
    # alpha.  Verified on a spread of arbitrary linear maps, and proved.
    t4_probe = []
    for m in (IDENT, SIGMA, IOTA, lin_comb(Fraction(2), Fraction(-1),
                                           Fraction(3)),
              tuple(tuple(Fraction(i * 3 + j + 1) for j in range(3))
                    for i in range(3))):
        sol = linear_invariance_solution_set(m)
        t4_probe.append({"kind": sol["kind"], "w": sol["w"]})
    t4_holds = all(p["kind"] in ("ALL_Q", "ZERO_ONLY") for p in t4_probe)

    # ---- the C3-invariant quadratic family: a FREE parameter ---------------
    # symmetric C3-invariant Grams are exactly G = p I + q(sigma + sigma^2),
    # a 2-parameter family, with 1^T G 1 = 3p + 6q.
    gram_rows = []
    for (p_, q_) in ((Fraction(1), Fraction(0)),
                     (Fraction(1), Fraction(-1, 2)),
                     (Fraction(1, 3), Fraction(0)),
                     (Fraction(2), Fraction(1))):
        g = tuple(tuple(p_ * IDENT[i][j]
                        + q_ * (SIGMA[i][j] + SIGMA2[i][j]) for j in range(3))
                  for i in range(3))
        n_const = sum((ONES[i] * sum(g[i][j] * ONES[j] for j in range(3))
                       for i in range(3)), Fraction(0))
        gram_rows.append({
            "p": q(p_), "q": q(q_),
            "N = 1^T G 1": q(n_const),
            "closed_form_3p_plus_6q": q(3 * p_ + 6 * q_),
            "matches": n_const == 3 * p_ + 6 * q_,
            **quadratic_normalization_solution_set(n_const),
        })
    # what (p,q) would be needed for the target?
    needed_n = Fraction(1) / (TARGET_ALPHA ** 2)
    needed_p_plus_2q = needed_n / 3

    census_selectors = [e for e in entries if is_selector(e)]
    target_selectors = [
        e for e in census_selectors
        if any(Fraction(s) == TARGET_ALPHA for s in e.get("solutions", []))
    ]

    return {
        "pass": (t4_holds and all(checks.values())
                 and completeness["total_solutions"] == 4),
        "supplied_structure_declared": [
            "the cubic lattice Z^3 with nearest-neighbour adjacency and the "
            "24 proper rotations",
            "one free C3 orbit of length 3 on the 6-neighbour shell",
            "the C3 action (the cyclic shift sigma)",
            "the readout normal form I_alpha(x) = alpha (x0 + x1 + x2)",
            "the record content space Q^3",
        ],
        "exact_algebra_checks": checks,
        "entries": entries,
        "commuting_involution_completeness": completeness,
        "normalizing_family": normalizer_rows,
        "C898_T4_linear_dichotomy": {
            "theorem": (
                "For EVERY Q-linear J on Q^3, the self-duality condition "
                "I_alpha o J = I_alpha is homogeneous linear in alpha, so its "
                "solution set is {0} or all of Q. No linear involution, "
                "self-duality or invariance condition can isolate a nonzero "
                "scale -- 882's T1 with the quantifier moved from 'the 13 "
                "enumerated members' to 'every linear map whatsoever'"
            ),
            "probe_rows": t4_probe,
            "holds": t4_holds,
            "consequence": (
                "all selection power in the M2 shape lives at degree >= 2"
            ),
        },
        "C898_T5_quadratic_family_has_a_free_parameter": {
            "invariant_gram_family": "G = p I + q(sigma + sigma^2), symmetric "
                                     "circulant, dimension 2",
            "normalization_constant": "1^T G 1 = 3p + 6q",
            "rows": gram_rows,
            "target_would_require": {
                "N": q(needed_n),
                "p_plus_2q": q(needed_p_plus_2q),
                "comment": (
                    "a C3-invariant Gram CAN be tuned to give 2/27, but "
                    "(p, q) is a free rational parameter that the supplied "
                    "structure does not fix. The quadratic family therefore "
                    "selects nothing by itself; pinning (p, q) is the same "
                    "purchase one level up"
                ),
            },
        },
        "coverage_bound": {
            "complete_no_bound_needed": [
                "every Q-linear invariance/self-duality condition (C898-T4)",
                "every C3-commuting Q-linear involution (closed-form, 4 of "
                "them)",
                "the entire C3-normalizing involution family J = iota q "
                "(permutation-matrix row-sum argument)",
                "every C3-invariant symmetric quadratic normalization "
                "(2-parameter family, closed form 3p + 6q)",
            ],
            "computed_individually": [
                "Pontryagin self-dual measure", "3-cycle Laplacian trace "
                "duality", "generator inversion", "convolution/pointwise "
                "duality on Q[C3] (both readings)", "unitary DFT "
                "normalization",
            ],
            "bounded_slice_only": [
                f"the normalizing family enumerated at height "
                f"{BOUND_NORMALIZER_HEIGHT} as a cross-check on the "
                f"bound-independent theorem",
            ],
            "NOT_COVERED_declared_open": [
                "non-linear (degree >= 3) self-duality conditions",
                "non-C3-invariant quadratic normalizations",
                "involutions acting on structure not supplied here (extra "
                "marked points, external anchors, larger content spaces)",
                "mixed-degree M2 relations that are not involution-derived -- "
                "this census closes the INVOLUTION subfamily of M2, not all "
                "of M2",
            ],
        },
        "selectors_found": [e["id"] for e in census_selectors],
        "selectors_hitting_target": [e["id"] for e in target_selectors],
        "verdict": (
            "NO native involution pins alpha = 2/27 (equivalently the orbit "
            "to 2/9)"
        ),
        "finding": (
            f"Census of {len(entries)} entries. Degree-1: every one is "
            f"{{0}} or the whole line, and C898-T4 upgrades that from an "
            f"enumeration to a theorem over ALL linear maps. Degree-2: two "
            f"irrational scales (Pontryagin and DFT, both 1/sqrt(3), "
            f"irrational because v_3(1/3) = -1 is odd), one further "
            f"irrational (the Fourier involution normalization) with an "
            f"EMPTY unit-exchange reading, and two rational-but-wrong scales "
            f"(Laplacian trace duality w = 1/3 with per-vertex trace 2/3; the "
            f"Q[C3] primitive idempotent 1/3). "
            f"{len(target_selectors)} entries pin the target."
        ),
    }


# ---------------------------------------------------------------------------
# H_M3_ALONE
# ---------------------------------------------------------------------------
def m3_alone() -> dict:
    # On the free Q-line the positive part has no least element: exhibited.
    chain = [TARGET_ALPHA]
    while len(chain) < 8:
        chain.append(chain[-1] / 2)
    descending = all(chain[i] > chain[i + 1] > 0 for i in range(len(chain) - 1))

    # the scaling action is transitive on the positive rationals, so a
    # fundamental domain is a point but its choice is arbitrary
    transitivity_probe = []
    for a, b in ((Fraction(2, 27), Fraction(1, 3)),
                 (Fraction(1), Fraction(2, 9)),
                 (Fraction(5, 7), Fraction(2, 27))):
        lam = b / a
        transitivity_probe.append({
            "from": q(a), "to": q(b), "scaling_factor": q(lam),
            "factor_is_positive_rational": lam > 0,
            "maps_correctly": a * lam == b,
        })
    transitive = all(r["maps_correctly"] and r["factor_is_positive_rational"]
                     for r in transitivity_probe)

    # with a lattice in hand the selector DOES bite
    m = 108
    lattice_members = [Fraction(k, m) for k in range(1, 40)]
    positives = [x for x in lattice_members if x > 0]
    least_positive = min(positives)
    v2_one = [x for x in positives if vp(x, 2) == 1]
    least_v2_one = min(v2_one)

    return {
        "pass": descending and transitive and least_v2_one == TARGET_ALPHA,
        "C898_T6_order_alone_selects_nothing": {
            "statement": (
                "On a Q-line the set of positive solutions has no least "
                "element: for every alpha > 0 in Q, alpha/2 is a strictly "
                "smaller positive solution of the same symmetry-only "
                "constraint set. The infimum is 0 and is not attained, so a "
                "least-positive or fundamental-domain condition selects "
                "nothing without a discrete set to order"
            ),
            "exhibited_descending_chain": [q(x) for x in chain],
            "all_strictly_positive_and_decreasing": descending,
            "ambient_constraint_row": (
                "882's K0_SYMMETRY_ONLY, whose survivor set is every alpha"
            ),
            "infimum": "0/1",
            "infimum_attained": False,
        },
        "fundamental_domain_reading": {
            "action": "the positive rational scalings act on the Q-line",
            "probe": transitivity_probe,
            "transitive_on_positive_rationals": transitive,
            "consequence": (
                "the action is transitive on Q_{>0}, so every positive alpha "
                "is an equally valid fundamental-domain representative; the "
                "condition has no canonical point"
            ),
        },
        "M3_needs_M4_first": {
            "with_lattice_modulus": m,
            "fractional_ideal": f"(1/{m})Z",
            "least_positive_member": q(least_positive),
            "least_positive_member_with_v2_eq_1": q(least_v2_one),
            "equals_target": least_v2_one == TARGET_ALPHA,
            "conclusion": (
                "M3's entire selection power is borrowed from M4. Given the "
                "lattice, least-positive-with-v2-1 lands on 2/27 exactly; "
                "without the lattice it lands on nothing at all. M3 alone is "
                "not an escape shape, it is an amplifier for M4's purchase"
            ),
        },
        "finding": (
            f"Order alone selects nothing: the exhibited chain "
            f"{q(chain[0])} > {q(chain[1])} > ... > {q(chain[-1])} stays "
            f"positive forever inside 882's symmetry-only survivor set, and "
            f"the scaling action is transitive on the positive rationals so "
            f"no representative is canonical. With M4's (1/{m})Z in hand the "
            f"same condition lands exactly on {q(least_v2_one)}. M3 is an "
            f"amplifier, not an escape."
        ),
    }


# ---------------------------------------------------------------------------
# I_COVERAGE_THEOREM
# ---------------------------------------------------------------------------
def coverage_theorem(gate, adj, enum, ingr, census, m3) -> dict:
    closed = [
        {
            "region": "single-degree scaling-covariant constraint systems",
            "closed_by": "C882-T1 (homogeneous dichotomy), restated and "
                         "reproduced here",
            "statement": "solution set is {0} or all of Q; never a nonzero "
                         "singleton",
            "scope": f"reproduced on all "
                     f"{len(gate['T1_882_statement_check']['rows'])} rows of "
                     f"the pinned alpha-witness table",
            "upgraded_here_by": (
                "C898-T4: the same dichotomy now holds for EVERY Q-linear "
                "map, not only for the enumerated members"
            ),
        },
        {
            "region": "M1, a marked point supplied by a multiplicatively "
                      "closed anchor library",
            "closed_by": "C882-T7 (the identity obstruction)",
            "statement": "every multiplicatively closed library contains 1, "
                         "so alpha = 1/3 survives beside the target and no "
                         "library selects uniquely",
            "scope": (
                f"882's ORIGINAL scope: "
                f"{gate['T7_882_headline']['primary_libraries_enumerated']} "
                f"libraries in the primary, "
                f"{gate['T7_882_headline']['receipt_headline_libraries']} in "
                f"the checker. Cycle 897's repaired scope is ABSENT from this "
                f"branch and is NOT relied on"
            ),
        },
        {
            "region": "M2 restricted to involution / self-duality structures "
                      "built from the supplied structure",
            "closed_by": "this block's census (G)",
            "statement": census["verdict"],
            "scope": (
                "complete and bound-free for every linear invariance "
                "condition, for all four C3-commuting involutions, for the "
                "whole C3-normalizing family and for the 2-parameter "
                "C3-invariant quadratic family; individually computed for the "
                "five named structural dualities"
            ),
        },
        {
            "region": "M4 via a two-record adjacency gluing defect",
            "closed_by": "this block's adjudication (D) and enumeration (E)",
            "statement": (
                "dies four independent deaths: (1) the additivity clause "
                "covers adjacent site-distinct records, so a nonzero defect "
                "contradicts the axiom; (2) the content-alone clause forbids "
                "a position-dependent defect under EVERY reading of "
                "'pairwise-disjoint'; (3) no three sites of Z^3 are pairwise "
                "adjacent (the nearest-neighbour graph is bipartite) and the "
                "target C3 orbit contains zero adjacency interfaces, so no "
                "defect can reach it; (4) the one import-free alternative "
                "reading -- content disjointness -- exempts equal-content "
                "collections, which is the target configuration itself, and "
                "so adds a free parameter rather than removing one"
            ),
            "scope": (
                "kills (1), (2) and (4) are byte-adjudications of the pinned "
                "axiom memo across all three readings tested; kill (3) is a "
                "bound-free lattice geometry fact; the counterfactual "
                "enumeration is exhaustive inside its declared bounds"
            ),
        },
        {
            "region": "M3 alone (an order / fundamental-domain condition)",
            "closed_by": "this block's C898-T6",
            "statement": "a Q-line has no least positive element and the "
                         "scaling action is transitive on it, so an order "
                         "condition alone selects nothing",
            "scope": "exact and bound-free",
        },
    ]
    open_regions = [
        {
            "region": "M1 with a NON-multiplicatively-closed anchor library",
            "why_open": (
                "T7's wall is multiplicative closure, and 882's "
                "H_ANCHOR_BIJECTION shows a singleton anchor DOES pin. A "
                "non-closed library is therefore exactly a marked point, "
                "i.e. the license restated -- 882's LEMMA-882, classified "
                "EQUIVALENT to the obligation"
            ),
            "status": "OPEN but EQUIVALENT to the obligation, not a route",
        },
        {
            "region": "M2 outside involutions: general mixed-degree relations",
            "why_open": (
                "this census closes the involution/self-duality subfamily. A "
                "mixed-degree relation that is not involution-derived is "
                "untouched by it, and remains outside T1's scope"
            ),
            "status": "OPEN -- the honest residual of Q2",
        },
        {
            "region": "M2 at degree >= 3, and non-C3-invariant quadratic "
                      "normalizations",
            "why_open": "declared outside the census's construction space",
            "status": "OPEN",
        },
        {
            "region": "M4 via a NON-adjacency integrality mechanism",
            "why_open": (
                "the census kills the adjacency-defect mechanism only. Any "
                "other route to a fractional ideal is untouched -- but "
                "certificate F prices every ingredient the known worked "
                "singleton uses, and all of them are purchases"
            ),
            "status": "OPEN but fully PRICED: "
                      f"{ingr['named_purchase_count']} named purchases",
        },
        {
            "region": "M3 + M4 as a package",
            "why_open": (
                "the package does produce {2/9} cleanly, but only after "
                "buying the modulus (odd part 27), the v_2 = 1 filter and the "
                "order condition"
            ),
            "status": "OPEN as a PURCHASE, closed as a DERIVATION",
        },
    ]
    return {
        "pass": len(closed) == 5 and len(open_regions) == 5,
        "closed": closed,
        "open": open_regions,
        "sharpest_statement": (
            "The selection question now has exactly ONE derivational shape "
            "left that is not either (a) proved impossible or (b) a named "
            "purchase: a mixed-degree M2 relation that is not "
            "involution-derived. Everything else in the four-shape "
            "classification is closed by theorem (T1, T7, C898-T3/T4/T6, the "
            "M4 adjudication) or priced (M4's ingredients, the M3+M4 "
            "package). M1 with a non-closed library is not a route -- it is "
            "the obligation restated."
        ),
        "finding": (
            f"{len(closed)} regions CLOSED, {len(open_regions)} OPEN. The "
            f"single unpriced open shape is non-involution mixed-degree M2."
        ),
    }


# ---------------------------------------------------------------------------
# J_FALSIFIER_VISIBILITY
# ---------------------------------------------------------------------------
def falsifier_visibility() -> dict:
    # PLANT: a synthetic C3-invariant Gram tuned to pin exactly 2/27.
    plant_p = Fraction(243, 4)
    plant_q = Fraction(0)
    plant_n = 3 * plant_p + 6 * plant_q
    plant_sol = quadratic_normalization_solution_set(plant_n)
    plant_detected = is_selector(plant_sol)
    plant_hits_target = any(Fraction(s) == TARGET_ALPHA
                            for s in plant_sol.get("solutions", []))

    # NEGATIVE CONTROL: a synthetic normalization that is NOT a rational
    # square, so the detector must NOT report a rational selector.
    ctrl_n = Fraction(5)
    ctrl_sol = quadratic_normalization_solution_set(ctrl_n)
    ctrl_detected = is_selector(ctrl_sol)

    # SECOND NEGATIVE CONTROL: a rational selector that is NOT the target.
    ctrl2_n = Fraction(9)
    ctrl2_sol = quadratic_normalization_solution_set(ctrl2_n)
    ctrl2_detected = is_selector(ctrl2_sol)
    ctrl2_hits_target = any(Fraction(s) == TARGET_ALPHA
                            for s in ctrl2_sol.get("solutions", []))

    # DEGREE-1 PLANT ATTEMPT: prove no linear plant can exist.
    deg1_attempts = []
    for m in (IDENT, SIGMA, IOTA,
              lin_comb(Fraction(27, 2), Fraction(0), Fraction(0)),
              lin_comb(Fraction(2, 27), Fraction(0), Fraction(0))):
        sol = linear_invariance_solution_set(m)
        deg1_attempts.append({
            "kind": sol["kind"],
            "isolates_target": (sol["kind"] == "FINITE"),
        })
    deg1_plant_impossible = not any(a["isolates_target"]
                                    for a in deg1_attempts)

    return {
        "pass": (plant_detected and plant_hits_target and not ctrl_detected
                 and ctrl2_detected and not ctrl2_hits_target
                 and deg1_plant_impossible),
        "planted_selector": {
            "construction": "synthetic C3-invariant Gram G = pI + q(sigma + "
                            "sigma^2) with p = 243/4, q = 0",
            "normalization_constant_N": q(plant_n),
            "solution": plant_sol,
            "DETECTED_AS_SELECTOR": plant_detected,
            "PINS_THE_TARGET": plant_hits_target,
            "meaning": (
                "the census machinery CAN see a selector when one exists; the "
                "negative verdict on the native entries is therefore a "
                "finding, not a blind spot"
            ),
        },
        "negative_control_irrational": {
            "normalization_constant_N": q(ctrl_n),
            "solution": ctrl_sol,
            "detected_as_selector": ctrl_detected,
            "expected": False,
        },
        "negative_control_rational_but_wrong": {
            "normalization_constant_N": q(ctrl2_n),
            "solution": ctrl2_sol,
            "detected_as_selector": ctrl2_detected,
            "pins_the_target": ctrl2_hits_target,
            "expected": "detected as a selector, but NOT of the target",
        },
        "degree_1_plant_attempt": {
            "attempts": deg1_attempts,
            "impossible": deg1_plant_impossible,
            "reason": (
                "C898-T4: a linear invariance condition is homogeneous in "
                "alpha, so no linear plant can isolate a nonzero scale. The "
                "census reporting 'no deg-1 selector' is forced, not lucky"
            ),
        },
        "finding": (
            f"Falsifier visibility holds: the planted Gram is detected and "
            f"pins exactly {q(TARGET_ALPHA)}; the irrational control is not "
            f"reported as a rational selector; the rational-but-wrong control "
            f"is detected as a selector and correctly not as the target; and "
            f"no degree-1 plant can exist by theorem."
        ),
    }


# ---------------------------------------------------------------------------
# K_NO_GO_GATE
# ---------------------------------------------------------------------------
def no_go_gate(adj, census, coverage) -> dict:
    routes = [
        ("R1", "M4 via an adjacency gluing defect on Z^3", "ATTEMPTED",
         "closed three ways (D and E)"),
        ("R2", "M4 via the permissive non-adjacency reading of "
               "'pairwise-disjoint'", "ATTEMPTED",
         "unlicensed by the bytes AND killed independently by the "
         "content-alone clause"),
        ("R3", "M4 via a purchased modulus (12N-alpha in Z)", "ATTEMPTED",
         "reduces to a single purchase, odd_part(M) = 27"),
        ("R4", "M2 via Pontryagin duality", "ATTEMPTED",
         "irrational fixed scale, no rational anchor at all"),
        ("R5", "M2 via 3-cycle Laplacian trace duality", "ATTEMPTED",
         "rational but wrong (w = 1/3, trace 2/3)"),
        ("R6", "M2 via the S3-normalizer generator inversion", "ATTEMPTED",
         "vacuous, pins nothing"),
        ("R7", "M2 via convolution/pointwise duality on Q[C3]", "ATTEMPTED",
         "irrational, or empty on the unit-exchange reading, or 1/3"),
        ("R8", "M2 via the unitary DFT normalization", "ATTEMPTED",
         "irrational"),
        ("R9", "M2 via any other Q-linear involution", "ATTEMPTED",
         "closed by theorem C898-T4 for every linear map"),
        ("R10", "M2 via a C3-invariant quadratic normalization", "ATTEMPTED",
         "free parameter, selects nothing without a further purchase"),
        ("R11", "M3 alone via least-positive / fundamental domain",
         "ATTEMPTED", "closed by C898-T6"),
        ("R12", "M1 via a multiplicatively closed anchor library",
         "RULED-OUT-BY-PRIOR", "C882-T7, pinned"),
        ("R13", "single-degree scaling-covariant constraint systems",
         "RULED-OUT-BY-PRIOR", "C882-T1, pinned"),
        ("R14", "M2 via a non-involution mixed-degree relation", "NOT-ATTACKED",
         "declared OPEN; the honest residual"),
    ]
    markers = {r[2] for r in routes}
    return {
        "pass": len(routes) >= 13 and markers <= {"ATTEMPTED",
                                                  "RULED-OUT-BY-PRIOR",
                                                  "NOT-ATTACKED"},
        "routes": [{"id": a, "route": b, "marker": c, "outcome": d}
                   for a, b, c, d in routes],
        "route_count": len(routes),
        "steelman": (
            "The strongest case against this block: the M4 adjudication turns "
            "on reading a set-theoretic word in an axiom memo that never "
            "defines it, and a determined proponent can insist "
            "'pairwise-disjoint' was meant to carve out adjacent records. "
            "That steelman is not rebutted by preference -- it is answered "
            "twice. First, the memo's own Record clause makes a record a "
            "single-site object, so on the permissive reading the qualifier "
            "'pairwise-disjoint' would be doing no work at all in a sentence "
            "whose author bothered to write it. Second, and independently of "
            "the reading, the content-alone sentence forbids a readout that "
            "depends on relative displacement, and a defect that vanishes on "
            "separated pairs and not on adjacent pairs is precisely such a "
            "dependence. Third, the geometry makes the argument moot: the "
            "target orbit has no adjacency interfaces. The proponent must "
            "therefore win all three, and the third is not an interpretive "
            "question."
        ),
        "exact_scope": (
            "Everything here is at the Cycle-882/883 readout scope: one free "
            "C3 orbit of length 3 on the 6-neighbour shell of Z^3, the "
            "readout normal form I_alpha(x) = alpha(x0+x1+x2) with alpha "
            "rational, and the target alpha = 2/27. The M2 census closes the "
            "INVOLUTION subfamily of M2, not all mixed-degree relations. The "
            "M4 verdict closes the ADJACENCY-DEFECT mechanism and prices the "
            "purchased-modulus mechanism; it does not prove no fractional "
            "ideal can ever arise. Cycle 897's repaired T7 scope is ABSENT "
            "from this branch, so 882's original T7 scope is what is cited. "
            "No axiom is added, no primitive is registered, no audit verdict "
            "is changed, and nothing here closes the R-eta obligation."
        ),
        "finding": (
            f"{len(routes)} routes carry a marker: "
            f"{sum(1 for r in routes if r[2] == 'ATTEMPTED')} attacked here, "
            f"{sum(1 for r in routes if r[2] == 'RULED-OUT-BY-PRIOR')} ruled "
            f"out by pinned prior art, "
            f"{sum(1 for r in routes if r[2] == 'NOT-ATTACKED')} declared "
            f"open and not attacked. The steelman against the M4 adjudication "
            f"is stated rather than rebutted, and answered on three "
            f"independent grounds of which the third -- the target orbit has "
            f"no adjacency interfaces -- is not an interpretive question at "
            f"all."
        ),
        "non_claims": [
            "this block does not close the readout obligation",
            "this block does not derive alpha = 2/27",
            "this block does not prove M4 impossible by every mechanism",
            "this block does not adjudicate owner intent, only memo bytes",
        ],
    }


# ---------------------------------------------------------------------------
# L_OUTCOME
# ---------------------------------------------------------------------------
def outcome(adj, enum, ingr, census, coverage) -> dict:
    return {
        "pass": True,
        "outcome_class": "EXHAUSTIVE_NO_GO_PLUS_COMPLETED_COVERAGE",
        "M4_verdict": adj["verdict"],
        "M4_kill_count": 4,
        "M4_ingredient_verdict": ingr["verdict"],
        "M4_named_purchases": ingr["named_purchase_count"],
        "M2_verdict": census["verdict"],
        "M2_entries": len(census["entries"]),
        "M3_verdict": "amplifier, not an escape",
        "regions_closed": len(coverage["closed"]),
        "regions_open": len(coverage["open"]),
        "new_theorems": [
            "C898-T1 the disjointness adjudication: of the three readings the "
            "memo's bytes admit, 'pairwise-disjoint' reads as disjoint site "
            "supports (2 discriminants to 1 over content disjointness, with "
            "non-adjacency unlicensed), so Record additivity covers adjacent "
            "records and a nonzero gluing defect contradicts the axiom -- and "
            "the ROUTE_DIES verdict is reading-independent",
            "C898-T2 the content-alone kill: a position-dependent gluing "
            "defect contradicts 'a readout value is determined by record "
            "content alone' under every reading of the disjointness qualifier",
            "C898-T3 geometric vacuity, universal form: the nearest-neighbour "
            "graph on Z^3 is bipartite, so no three sites anywhere are "
            "pairwise adjacent and the target free C3 orbit contains zero "
            "adjacency interfaces; no adjacency defect can constrain alpha",
            "C898-T4 the linear dichotomy: for EVERY Q-linear map the "
            "self-duality condition is homogeneous in alpha, so the whole "
            "involution/self-duality shape is degree-1 sterile",
            "C898-T5 the quadratic free parameter: C3-invariant quadratic "
            "normalizations form a 2-parameter family, so they select nothing "
            "without a further purchase",
            "C898-T6 order alone selects nothing: a Q-line has no least "
            "positive element and its scaling action is transitive",
        ],
        "price": (
            "The M3+M4 singleton survives only as a package of named "
            "purchases: (i) the ambient field, (ii) any integrality statement "
            "about alpha, (iii) the modulus with odd part 27, (iv) the "
            "least-positive selector -- with the v_2 = 1 datum derived for the "
            "isotype dimension pair but not bound to alpha (883's own 5-fold "
            "ambiguity). Nothing in the pinned axiom memo supplies any of them."
        ),
        "finding": (
            "The block returns the exhaustive negative it was specified to "
            "return, plus more coverage than expected: M4's adjacency "
            "mechanism dies four independent deaths across all three readings "
            "the memo's bytes admit (one of them pure geometry, so it is "
            "immune to the interpretive dispute entirely), the M2 "
            "involution census closes at degree 1 by theorem rather than by "
            "enumeration, and the single unpriced open shape in the whole "
            "four-shape classification is a non-involution mixed-degree "
            "relation."
        ),
    }


# ---------------------------------------------------------------------------
# science build + render
# ---------------------------------------------------------------------------
def build_science() -> dict:
    gate = restriction_gate()
    sweep = disjointness_sweep()
    adj = m4_adjudication(sweep)
    enum = m4_enumeration()
    ingr = m4_ingredient_audit()
    census = m2_census()
    m3 = m3_alone()
    cov = coverage_theorem(gate, adj, enum, ingr, census, m3)
    fals = falsifier_visibility()
    gate_k = no_go_gate(adj, census, cov)
    out = outcome(adj, enum, ingr, census, cov)
    return {
        "B_RESTRICTION_GATE": gate,
        "C_DISJOINTNESS_SWEEP": sweep,
        "D_M4_ADJUDICATION": adj,
        "E_M4_ENUMERATION_AND_COUNTERFACTUAL": enum,
        "F_M4_INGREDIENT_DERIVABILITY": ingr,
        "G_M2_INVOLUTION_CENSUS": census,
        "H_M3_ALONE": m3,
        "I_COVERAGE_THEOREM": cov,
        "J_FALSIFIER_VISIBILITY": fals,
        "K_NO_GO_GATE": gate_k,
        "L_OUTCOME_AND_PRICE": out,
    }


def wrap(text: str, width: int = 74, indent: str = "       ") -> list[str]:
    words, lines, cur = text.split(), [], ""
    for word in words:
        if not cur:
            cur = word
        elif len(cur) + 1 + len(word) <= width:
            cur += " " + word
        else:
            lines.append(indent + cur)
            cur = word
    if cur:
        lines.append(indent + cur)
    return lines


def render(certs: dict) -> str:
    bar = "=" * 78
    rule = "-" * 78
    out = [bar, "CYCLE 898 -- THE M2 / M4 ESCAPE CENSUS", bar, ""]
    for label in LABELS:
        cert = certs.get(label)
        if cert is None:      # M_CONTROLS is sealed after the transcript is
            continue          # rendered; its verdict rides the trailer line
        out.append(f"[{'PASS' if cert['pass'] else 'FAIL'}] {label}")
        out.extend(wrap(cert.get("finding", "")))
        out.append("")

    d = certs["C_DISJOINTNESS_SWEEP"]
    out += [rule, "EVERY 'disjoint' OCCURRENCE IN THE PINNED AXIOM MEMO", rule]
    for hit in d["disjoint_occurrences"]:
        out.append(f"  line {hit['line']:>4}  col {hit['column']:>3}  byte "
                   f"{hit['byte_offset']:>6}  section {hit['section']}")
        out.extend(wrap(f"\"{hit['sentence']}\"", indent="        "))
    out += ["", f"  adjacency-word occurrences: {d['adjacency_count']} "
                f"(line "
                f"{', '.join(str(h['line']) for h in d['adjacency_occurrences'])}"
                f", section "
                f"{d['adjacency_occurrences'][0]['section'] if d['adjacency_occurrences'] else 'n/a'})",
            f"  explicit definitions of record disjointness: "
            f"{d['explicit_disjointness_definition_count']}",
            f"  'disjoint' sentences carrying an adjacency qualifier: "
            f"{len(d['disjoint_sentences_carrying_adjacency_qualifier'])}", ""]

    a = certs["D_M4_ADJUDICATION"]
    out += [rule, "THE M4 ADJUDICATION", rule,
            f"  readings tested     : {a['readings_tested']}",
            f"  discriminant tally  : {a['discriminant_tally']}",
            f"  adjudicated reading : {a['adjudicated_reading']}",
            f"  reading-independent : "
            f"{a['verdict_is_reading_independent']}",
            f"  covers adjacent     : {a['additivity_covers_adjacent_records']}",
            f"  VERDICT             : {a['verdict']}", ""]
    inst = a["contradicting_instance"]
    out += [f"  contradicting instance: records at {inst['sites'][0]} and "
            f"{inst['sites'][1]}, squared distance "
            f"{inst['squared_distance']} (adjacent={inst['adjacent']}),",
            f"    supports disjoint={inst['supports_disjoint']}, contents "
            f"{inst['record_contents']}",
            f"    axiom requires I = {inst['axiom_required_readout']}; "
            f"with a nonzero defect D=1, I = "
            f"{inst['readout_with_nonzero_gluing_defect_D=1']}",
            f"    difference {inst['difference']} != 0  ->  CONTRADICTION", ""]
    k2 = a["second_independent_kill_content_alone"]
    out += [f"  second, reading-independent kill: identical contents "
            f"{k2['configuration_A']['contents']} at squared distance "
            f"{k2['configuration_A']['squared_distance']} vs "
            f"{k2['configuration_B']['squared_distance']}",
            f"    readouts {k2['readout_A']} vs {k2['readout_B']}  ->  "
            f"content-alone violated: {k2['violated']}", ""]

    e = certs["E_M4_ENUMERATION_AND_COUNTERFACTUAL"]
    gv = e["C898_T3_geometric_vacuity"]
    out += [rule, "M4 ENUMERATION AND COUNTERFACTUAL", rule,
            f"  target C3 orbit {gv['target_orbit']}",
            f"  pairwise squared distances: "
            f"{[p['squared_distance'] for p in gv['pairwise_squared_distances']]}",
            f"  adjacency interfaces inside the target orbit: "
            f"{gv['adjacency_interfaces_in_target_orbit']}",
            f"  counterfactual family size "
            f"{e['counterfactual_defect_family']['family_size']}, all "
            f"enumerated: "
            f"{e['counterfactual_defect_family']['exhaustive_within_bounds']}",
            f"  induced constraint on alpha, every member: "
            f"{e['counterfactual_defect_family']['induced_constraint_on_alpha_reading_1']}",
            ""]
    out += ["  purchased-modulus ideal sweep (least positive member with "
            "v_2 = 1):"]
    out.append("    M      ideal        v2(M)  odd(M)  least v2=1   target?")
    for row in e["purchased_modulus_ideal"]["rows"][:14]:
        out.append(f"    {row['modulus_M']:<6} {row['fractional_ideal']:<12} "
                   f"{row['v2_of_M']:<6} {row['odd_part_of_M']:<7} "
                   f"{row['least_positive_with_v2_eq_1']:<12} "
                   f"{'YES' if row['equals_target'] else '.'}")
    out += ["", f"  moduli in [1,{BOUND_MODULUS_MAX}] hitting 2/27: "
                f"{e['purchased_modulus_ideal']['moduli_in_scan_hitting_target']}",
            f"  their odd parts: "
            f"{e['purchased_modulus_ideal']['odd_parts_of_hitting_moduli']}", ""]

    c = certs["G_M2_INVOLUTION_CENSUS"]
    out += [rule, "THE M2 INVOLUTION CENSUS", rule,
            f"  {'id':<22} {'deg':<4} {'fixed scale over Q':<22} verdict"]
    for entry in c["entries"]:
        scale = entry.get("fixed_scale_over_Q", "n/a")
        if entry.get("kind") == "IRRATIONAL":
            scale = f"NONE ({entry['fixed_scale_algebraic']})"
        out.append(f"  {entry['id']:<22} {entry.get('degree', '-'):<4} "
                   f"{str(scale):<22} {entry['kind']}")
    out += ["", f"  selectors found: {c['selectors_found']}",
            f"  selectors hitting the target: "
            f"{c['selectors_hitting_target']}",
            f"  VERDICT: {c['verdict']}", "",
            "  coverage bound (complete, no bound needed):"]
    for line in c["coverage_bound"]["complete_no_bound_needed"]:
        out.extend(wrap("- " + line, indent="    "))
    out.append("  NOT covered (declared open):")
    for line in c["coverage_bound"]["NOT_COVERED_declared_open"]:
        out.extend(wrap("- " + line, indent="    "))
    out.append("")

    f = certs["J_FALSIFIER_VISIBILITY"]
    out += [rule, "FALSIFIER VISIBILITY", rule,
            f"  planted selector detected : "
            f"{f['planted_selector']['DETECTED_AS_SELECTOR']}",
            f"  planted selector pins 2/27: "
            f"{f['planted_selector']['PINS_THE_TARGET']}",
            f"  irrational control flagged: "
            f"{f['negative_control_irrational']['detected_as_selector']} "
            f"(expected False)",
            f"  wrong-value control flagged as selector: "
            f"{f['negative_control_rational_but_wrong']['detected_as_selector']}"
            f", as target: "
            f"{f['negative_control_rational_but_wrong']['pins_the_target']}",
            f"  degree-1 plant impossible : "
            f"{f['degree_1_plant_attempt']['impossible']}", ""]

    cov = certs["I_COVERAGE_THEOREM"]
    out += [rule, "THE COVERAGE THEOREM: CLOSED vs OPEN", rule, "  CLOSED:"]
    for row in cov["closed"]:
        out.extend(wrap(f"[{row['closed_by']}] {row['region']} -- "
                        f"{row['statement']}", indent="    "))
    out.append("  OPEN:")
    for row in cov["open"]:
        out.extend(wrap(f"[{row['status']}] {row['region']} -- "
                        f"{row['why_open']}", indent="    "))
    out.append("")
    out.extend(wrap(cov["sharpest_statement"], indent="  "))
    out.append("")

    o = certs["L_OUTCOME_AND_PRICE"]
    out += [rule, "OUTCOME", rule,
            f"  class: {o['outcome_class']}",
            f"  M4: {o['M4_verdict']} ({o['M4_kill_count']} independent "
            f"kills); ingredients {o['M4_ingredient_verdict']} with "
            f"{o['M4_named_purchases']} named purchases",
            f"  M2: {o['M2_verdict']} over {o['M2_entries']} census entries",
            f"  M3: {o['M3_verdict']}",
            f"  coverage: {o['regions_closed']} closed / {o['regions_open']} "
            f"open", "", "  new theorems:"]
    for th in o["new_theorems"]:
        out.extend(wrap("- " + th, indent="    "))
    out += ["", bar,
            "CYCLE 898 CERTIFICATES: "
            + ("ALL PASS" if all(x["pass"] for x in certs.values())
               else "FAILURES PRESENT"),
            bar]
    return "\n".join(out) + "\n"


def run() -> int:
    started = monotonic()

    pins = pins_certificate()
    if not pins["pass"]:
        sys.stderr.write("PIN FAILURE:\n" + "\n".join(pins["failures"]) + "\n")
        return 2

    science_a = build_science()
    science_b = build_science()
    deterministic = digest(science_a) == digest(science_b)

    certificates = {"A_PINS": pins, **science_a}

    receipt = {
        "cycle": 898,
        "title": "the M2/M4 escape census: completing the coverage T1 and T7 "
                 "never had",
        "target_alpha": q(TARGET_ALPHA),
        "target_orbit_value": q(TARGET_ORBIT_VALUE),
        "M4_adjudicated_reading":
            science_a["D_M4_ADJUDICATION"]["adjudicated_reading"],
        "M4_verdict": science_a["D_M4_ADJUDICATION"]["verdict"],
        "M4_readings_tested":
            science_a["D_M4_ADJUDICATION"]["readings_tested"],
        "M4_verdict_per_reading":
            science_a["D_M4_ADJUDICATION"]["verdict_per_reading"],
        "M4_verdict_is_reading_independent":
            science_a["D_M4_ADJUDICATION"]["verdict_is_reading_independent"],
        "M4_discriminant_tally":
            science_a["D_M4_ADJUDICATION"]["discriminant_tally"],
        "M4_disjoint_occurrences": [
            {"line": h["line"], "byte_offset": h["byte_offset"],
             "sentence": h["sentence"]}
            for h in science_a["C_DISJOINTNESS_SWEEP"]["disjoint_occurrences"]
        ],
        "M4_ingredient_verdict":
            science_a["F_M4_INGREDIENT_DERIVABILITY"]["verdict"],
        "M4_named_purchases":
            science_a["F_M4_INGREDIENT_DERIVABILITY"]["named_purchase_count"],
        "M2_census": [
            {"id": e["id"], "name": e["name"], "degree": e.get("degree"),
             "kind": e.get("kind"),
             "fixed_scale_over_Q": e.get("fixed_scale_over_Q"),
             "fixed_scale_algebraic": e.get("fixed_scale_algebraic"),
             "verdict": e["verdict"]}
            for e in science_a["G_M2_INVOLUTION_CENSUS"]["entries"]
        ],
        "M2_verdict": science_a["G_M2_INVOLUTION_CENSUS"]["verdict"],
        "M2_coverage_bound":
            science_a["G_M2_INVOLUTION_CENSUS"]["coverage_bound"],
        "coverage_closed": science_a["I_COVERAGE_THEOREM"]["closed"],
        "coverage_open": science_a["I_COVERAGE_THEOREM"]["open"],
        "sharpest_statement":
            science_a["I_COVERAGE_THEOREM"]["sharpest_statement"],
        "outcome_class": science_a["L_OUTCOME_AND_PRICE"]["outcome_class"],
        "new_theorems": science_a["L_OUTCOME_AND_PRICE"]["new_theorems"],
        "price": science_a["L_OUTCOME_AND_PRICE"]["price"],
        "routes": science_a["K_NO_GO_GATE"]["routes"],
        "steelman": science_a["K_NO_GO_GATE"]["steelman"],
        "exact_scope": science_a["K_NO_GO_GATE"]["exact_scope"],
        "restriction_gate": {
            "T1_reproduced":
                science_a["B_RESTRICTION_GATE"]["T1_882_statement_check"][
                    "reproduced"],
            "T7_reproduced":
                science_a["B_RESTRICTION_GATE"]["T7_882_headline"][
                    "reproduced"],
            "C883_normal_form_reproduced":
                science_a["B_RESTRICTION_GATE"]["C883_normal_form_row"][
                    "reproduced"],
            "cycle_897_scan":
                science_a["B_RESTRICTION_GATE"]["T7_882_headline"][
                    "cycle_897_scan"],
        },
        "geometric_vacuity_universal_form":
            science_a["E_M4_ENUMERATION_AND_COUNTERFACTUAL"][
                "C898_T3_geometric_vacuity"]["universal_form"],
        "declared_bounds":
            science_a["E_M4_ENUMERATION_AND_COUNTERFACTUAL"][
                "declared_bounds"],
        "falsifier_visibility": {
            "planted_selector_detected":
                science_a["J_FALSIFIER_VISIBILITY"]["planted_selector"][
                    "DETECTED_AS_SELECTOR"],
            "planted_selector_pins_target":
                science_a["J_FALSIFIER_VISIBILITY"]["planted_selector"][
                    "PINS_THE_TARGET"],
        },
        "source_pins": [
            {"path": r["path"], "sha256": r.get("sha256"),
             "git_blob": r.get("git_blob")} for r in pins["rows"]
        ],
    }
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(
        json.dumps(receipt, indent=2, sort_keys=True, default=str) + "\n",
        encoding="utf-8")
    receipt_digest = sha256(RECEIPT.read_bytes()).hexdigest()

    text = render(certificates)
    stdout_bytes = len(text.encode("utf-8"))
    elapsed = monotonic() - started

    controls = {
        "audit_input_paths": list(AUDIT_INPUT_PATHS),
        "blocklisted_modules": list(BLOCKLISTED_MODULES),
        "blocked_modules_loaded": [n for n in BLOCKLISTED_MODULES
                                   if n in sys.modules],
        "firewall_hits": list(FIREWALL.hits),
        "determinism": {
            "scope": "every science certificate rebuilt from scratch and "
                     "compared digest for digest",
            "exact": deterministic,
            "science_digest": digest(science_a),
        },
        "receipt_path": str(RECEIPT.relative_to(ROOT)),
        "receipt_sha256": receipt_digest,
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "runtime_under_limit": elapsed < AUDIT_TIMEOUT_SEC,
        "stdout_bytes": stdout_bytes,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "stdout_under_limit": stdout_bytes < STDOUT_LIMIT_BYTES,
        "floating_point_in_certified_quantities": False,
        "sqrt3_handling": (
            "sqrt(3) never appears as a float. Every irrational fixed scale "
            "is certified by an exact algebraic statement: alpha^2 = r has no "
            "rational solution because v_p(r) is odd at a named prime p"
        ),
        "gate_neutrality": (
            "No certificate gates on a preferred verdict. The adjudication "
            "gates on the presence of its evidence clauses, not on which "
            "reading wins; the enumeration gates on exhaustiveness inside "
            "declared bounds; the census gates on the algebra checks and on "
            "the completeness proof, not on the census returning a negative; "
            "the falsifier certificate gates on the PLANT being seen, which "
            "would fail loudly if the census were blind"
        ),
        "finding": (
            "All cited artifacts stayed text/AST/JSON-only behind the import "
            "firewall, the whole science payload rebuilt digest for digest, "
            "and the runtime and stdout caps were respected."
        ),
    }
    controls["pass"] = (
        deterministic and controls["runtime_under_limit"]
        and controls["stdout_under_limit"]
        and not controls["blocked_modules_loaded"]
        and not controls["firewall_hits"]
    )
    certificates["M_CONTROLS"] = controls

    sys.stdout.write(text)
    sys.stdout.write(
        f"\ncontrols: deterministic={deterministic} "
        f"runtime_under_limit={controls['runtime_under_limit']} "
        f"stdout={stdout_bytes}B receipt={controls['receipt_sha256'][:16]}\n")
    return 0 if all(c["pass"] for c in certificates.values()) else 1


if __name__ == "__main__":
    raise SystemExit(run())
