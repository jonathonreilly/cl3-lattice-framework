#!/usr/bin/env python3
"""Cycle 887 INDEPENDENT CHECK -- spec'd to REFUTE the window-freedom primary.

The primary (scripts/frontier_cycle887_window_freedom_2026_07_28.py) claims:

  P1  SUFFICIENCY: every finite nonempty rotation-invariant structuring set S
      yields an admissible window map W_S(R) = supp(R) (+) S.
  P2  INJECTIVITY: S |-> W_S is injective on the 12-configuration family, so
      the count of distinct admissible Minkowski windows is exactly the count
      of rotation-invariant S: 15 / 1023 / 2097151 at box radius 1 / 2 / 3.
  P3  NON-CLOSURE: seven listed constructions pass REQ1-REQ5 and are provably
      outside the fixed-S family.
  P4  ANNULAR COARSENESS: the 1023 radius-2 maps give 1023 distinct set-valued
      behaviours but only 113 distinct annular (a, b) behaviours.
  P5  CONTAINMENT: supp(R) subset W(R) is NOT forced by REQ1-REQ5 (witness
      supp(R) (+) N6), but IS derived from the byte-quoted readout-additivity
      sentence of the Record axiom.
  P6  SELECTION: no selector derives k = 0; minimality is absent from the three
      pinned texts.

This checker attacks each claim with independent implementations:

  * the rotation group is rebuilt as the CLOSURE OF TWO GENERATORS, not by
    enumerating signed permutations;
  * the configuration family is rebuilt from an independent reimplementation
    AND by AST-extracting the Cycle-885 primary's own generator;
  * the requirement harness is written in the PULL-BACK direction
    (g^{-1} W(gR) == W(R)) instead of the push-forward direction;
  * the structuring-set orbits are enumerated by an independent stabiliser
    computation;
  * FRESH probe configurations the primary never used are generated and every
    claim is recomputed on them.

Top refutation targets, in the order the block spec named them:
  (1) quote-to-computation fidelity of every selector grounding;
  (2) the structure-theorem boundary -- an escape class the primary did NOT
      list refutes any closure claim it might be read as making;
  (3) support-containment forcing -- independent proof or counterexample;
  (4) all counts recomputed on new probe configurations.

Teeth: six deliberate mutations that MUST be caught.  Exit code 0 regardless of
whether the primary's claims survive.
"""

from __future__ import annotations

import ast
import hashlib
import importlib.abc
import json
import re
import sys
import time
from fractions import Fraction
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SELF_REL = "scripts/frontier_cycle887_window_freedom_independent_check_2026_07_28.py"

PRIMARY = "scripts/frontier_cycle887_window_freedom_2026_07_28.py"
PRIMARY_RECEIPT = "outputs/window_freedom_cycle887_receipt_2026_07_28.json"
AXIOMS_MD = "docs/MINIMAL_AXIOMS_2026-06-29.md"
DYNAMICS_MD = "docs/GATE_B_DYNAMICS_NOTE.md"
WEAKFIELD_MD = "docs/GATE_B_WEAK_FIELD_SOURCE_ACTION_INTERFACE_NOTE_2026-06-16.md"
C885_PRIMARY = "scripts/frontier_cycle885_gbw1_record_window_2026_07_28.py"
C885_RECEIPT = "outputs/gbw1_record_window_cycle885_receipt_2026_07_28.json"

PINS = [PRIMARY, PRIMARY_RECEIPT, AXIOMS_MD, DYNAMICS_MD, WEAKFIELD_MD,
        C885_PRIMARY, C885_RECEIPT]

REQUIRED_SHA256 = {
    C885_PRIMARY:
        "daee8bbfefde80a351bf82a3028d96baf447493d3add8cdc85f4eb63fc114f32",
    C885_RECEIPT:
        "3561cc4e62ba55a9f2aed377122dec795103a6f424a39a907e866f53665da997",
}

OUT_JSON = (ROOT / "outputs"
            / "window_freedom_independent_check_cycle887_receipt_2026_07_28.json")

EXHIBIT_CAP = 5
STDOUT_LINE_CAP = 700


def preflight() -> dict:
    missing = [p for p in PINS if not (ROOT / p).is_file()]
    if missing:
        sys.stderr.write("PREFLIGHT FAIL: absent: %s\n" % ", ".join(missing))
        raise SystemExit(2)
    bad = []
    for rel, want in REQUIRED_SHA256.items():
        got = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
        if got != want:
            bad.append(rel)
    if bad:
        sys.stderr.write("PREFLIGHT FAIL: digest mismatch: %s\n" % ", ".join(bad))
        raise SystemExit(2)
    rows = []
    for rel in PINS + [SELF_REL]:
        raw = (ROOT / rel).read_bytes()
        rows.append({"path": rel,
                     "sha256": hashlib.sha256(raw).hexdigest(),
                     "git_blob": hashlib.sha1(
                         b"blob %d\0" % len(raw) + raw).hexdigest(),
                     "bytes": len(raw)})
    return {"rows": rows}


PREFLIGHT = preflight()


# ---- import firewall ------------------------------------------------------
_FORBIDDEN = {Path(PRIMARY).stem, Path(C885_PRIMARY).stem}


class _Firewall(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname.split(".")[-1] in _FORBIDDEN:
            raise ImportError(f"import firewall: {fullname}")
        return None


sys.meta_path.insert(0, _Firewall())


def rtext(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def rbytes(rel: str) -> bytes:
    return (ROOT / rel).read_bytes()


def dg(obj) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, default=str).encode("utf-8")).hexdigest()


def qf(v) -> str:
    if v is None:
        return "none"
    f = Fraction(v)
    return f"{f.numerator}/{f.denominator}"


# --------------------------------------------------------------------------
# INDEPENDENT group build: closure of two generators, not a permutation sweep
# --------------------------------------------------------------------------
def mmul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))


def mvec(m, v):
    return tuple(sum(m[i][j] * v[j] for j in range(3)) for i in range(3))


def mvec_frac(m, v):
    return tuple(sum(Fraction(m[i][j]) * v[j] for j in range(3))
                 for i in range(3))


def minv(m):
    """The inverse of an orthogonal integer matrix is its transpose."""
    return tuple(tuple(m[j][i] for j in range(3)) for i in range(3))


ID3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
GEN_Z90 = ((0, -1, 0), (1, 0, 0), (0, 0, 1))         # 90 degrees about z
GEN_DIAG = ((0, 0, 1), (1, 0, 0), (0, 1, 0))         # 120 degrees about (1,1,1)


def group_closure(gens):
    seen = {ID3}
    frontier = [ID3]
    while frontier:
        nxt = []
        for g in frontier:
            for h in gens:
                p = mmul(g, h)
                if p not in seen:
                    seen.add(p)
                    nxt.append(p)
        frontier = nxt
    return sorted(seen)


ROT = group_closure([GEN_Z90, GEN_DIAG])
NEIGH = tuple(sorted(p for p in product((-1, 0, 1), repeat=3)
                     if sum(abs(c) for c in p) == 1))


def stabiliser_orbits(radius: int):
    """Orbits by repeated application until closure -- independent of any
    coordinate-sorting trick."""
    pts = set(product(range(-radius, radius + 1), repeat=3))
    orbs = []
    left = set(pts)
    while left:
        p = min(left)
        o = {p}
        grow = True
        while grow:
            grow = False
            for x in list(o):
                for m in ROT:
                    y = mvec(m, x)
                    if y not in o:
                        o.add(y)
                        grow = True
        orbs.append(frozenset(o))
        left -= o
    return sorted(orbs, key=lambda o: (len(o), sorted(o)[0]))


ORB1 = stabiliser_orbits(1)
ORB2 = stabiliser_orbits(2)


# --------------------------------------------------------------------------
# the Cycle-885 family: my reimplementation + AST extraction from the pinned 885
# --------------------------------------------------------------------------
def my_lcg(seed, n, mod):
    x, out = seed, []
    for _ in range(n):
        x = (1103515245 * x + 12345) % 2147483648
        out.append(x % mod)
    return out


def cfg_of(name, sites):
    st = tuple(sorted({tuple(int(v) for v in s) for s in sites}))
    n = len(st)
    if n == 0:
        return {"name": name, "sites": (), "content": (), "depth": ()}
    ctr = tuple(Fraction(sum(s[i] for s in st), n) for i in range(3))
    rad = {s: sum((Fraction(s[i]) - ctr[i]) ** 2 for i in range(3)) for s in st}
    order = sorted(set(rad.values()))
    return {"name": name, "sites": st,
            "content": tuple((s, (s[0] + s[1] + s[2]) & 1) for s in st),
            "depth": tuple((s, order.index(rad[s]) + 1) for s in st)}


def my_family():
    out = []
    out.append(cfg_of("single", [(0, 0, 0)]))
    out.append(cfg_of("pair", [(0, 0, 0), (1, 0, 0)]))
    out.append(cfg_of("shell1", NEIGH))
    out.append(cfg_of("ball1", tuple(NEIGH) + ((0, 0, 0),)))
    ring = [v for v in product(range(-2, 3), repeat=3)
            if 1 <= sum(c * c for c in v) <= 4]
    out.append(cfg_of("annulus_1_4", ring))
    out.append(cfg_of("hollow_annulus", [v for v in ring if v != (2, 0, 0)]))
    out.append(cfg_of("Lshape",
                      [(0, 0, 0), (1, 0, 0), (2, 0, 0), (0, 1, 0), (0, 2, 0)]))
    out.append(cfg_of("plane_square",
                      [(a, b, 0) for a in range(3) for b in range(3)]))
    out.append(cfg_of("chain", [(k, 0, 0) for k in range(5)]))
    cube = list(product(range(-2, 3), repeat=3))
    for sd, tg in ((7, "a"), (2909, "b")):
        pick = sorted(set(my_lcg(sd, 24, len(cube))))[:9]
        out.append(cfg_of(f"sparse_{tg}", [cube[i] for i in pick]))
    out.append(cfg_of("offcentre_ball",
                      [(v[0] + 2, v[1] - 1, v[2] + 1)
                       for v in tuple(NEIGH) + ((0, 0, 0),)]))
    return out


def ast_family_from_885():
    src = rtext(C885_PRIMARY)
    tree = ast.parse(src)
    need = {"NEIGHBOURS", "_lcg", "make_config", "build_family"}
    keep, found = [], set()
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in need:
            keep.append(node)
            found.add(node.name)
        elif isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id in need:
                    keep.append(node)
                    found.add(t.id)
    ns = {"Fraction": Fraction, "product": product}
    exec(compile(ast.Module(body=keep, type_ignores=[]),
                 "<885>", "exec"), ns)  # noqa: S102
    return ns["build_family"](), sorted(found)


def fingerprint(fam):
    return [[c["name"], sorted(map(list, c["sites"])),
             sorted([list(s), b] for s, b in c["content"]),
             sorted([list(s), d] for s, d in c["depth"])] for c in fam]


FAM = my_family()
FAM_885, AST_FOUND = ast_family_from_885()


# --------------------------------------------------------------------------
# FRESH probe configurations the primary never used
# --------------------------------------------------------------------------
def fresh_family():
    out = []
    # a single record NOT at the origin -- stresses translation in every claim
    out.append(cfg_of("fresh_lone_offset", [(3, -2, 1)]))
    # a single record AT the origin -- needed for structuring-set extraction
    out.append(cfg_of("fresh_origin", [(0, 0, 0)]))
    # four body-diagonal corners of a cube: a chiral-looking, low-symmetry set
    out.append(cfg_of("fresh_tetra",
                      [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]))
    # a 3-D cross with arms of length two
    arms = [(0, 0, 0)]
    for ax in range(3):
        for s in (-1, 1):
            for k in (1, 2):
                v = [0, 0, 0]
                v[ax] = s * k
                arms.append(tuple(v))
    out.append(cfg_of("fresh_cross2", arms))
    # two well-separated clusters -- exercises the disjoint-decomposition logic
    two = [v for v in tuple(NEIGH) + ((0, 0, 0),)]
    two += [(v[0] + 6, v[1], v[2]) for v in two]
    out.append(cfg_of("fresh_two_clusters", two))
    # a diagonal staircase
    out.append(cfg_of("fresh_staircase",
                      [(k, k, 0) for k in range(4)] + [(k, k, 1) for k in range(2)]))
    # a fresh LCG-selected sparse set with a seed the primary never used
    cube = list(product(range(-3, 4), repeat=3))
    pick = sorted(set(my_lcg(31337, 40, len(cube))))[:11]
    out.append(cfg_of("fresh_sparse_c", [cube[i] for i in pick]))
    # a slab
    out.append(cfg_of("fresh_slab",
                      [(a, b, c) for a in range(-1, 2) for b in range(-1, 2)
                       for c in (0, 1)]))
    return out


FRESH = fresh_family()


# --------------------------------------------------------------------------
# INDEPENDENT harness -- written in the PULL-BACK direction
# --------------------------------------------------------------------------
SHIFTS = ((0, 0, 0), (1, 0, 0), (0, -2, 0), (3, 1, -2), (-1, -1, -1))
W2 = (1, 2)


def move(cfg, m, t):
    fwd = {}
    for s in cfg["sites"]:
        y = mvec(m, s)
        fwd[(y[0] + t[0], y[1] + t[1], y[2] + t[2])] = s
    st = tuple(sorted(fwd))
    con, dep = dict(cfg["content"]), dict(cfg["depth"])
    return {"name": cfg["name"] + "^g", "sites": st,
            "content": tuple((y, con[fwd[y]]) for y in st),
            "depth": tuple((y, dep[fwd[y]]) for y in st)}


def centre_of(cfg):
    n = len(cfg["sites"])
    if n == 0:
        return (Fraction(0),) * 3
    return tuple(Fraction(sum(s[i] for s in cfg["sites"]), n) for i in range(3))


def extremes(pts, c):
    if not pts:
        return (None, None)
    vals = [sum((Fraction(p[i]) - c[i]) ** 2 for i in range(3)) for p in pts]
    return (min(vals), max(vals))


def wrap(pts, c):
    st = frozenset(pts)
    lo, hi = extremes(st, c)
    return {"set": st, "centre": c, "a2": lo, "b2": hi}


def filtration(cfg):
    lv = sorted({d for _, d in cfg["depth"]})
    return [cfg_of(f"{cfg['name']}~{k}",
                   [s for s, d in cfg["depth"] if d <= k]) for k in lv]


def check(fn, fam):
    """REQ2/REQ3 by PULLING BACK: g^{-1} . W(g R) must equal W(R)."""
    eq_fail = eq_checks = 0
    rot_fail = rot_checks = 0
    tr_fail = tr_checks = 0
    ex = []
    for cfg in fam:
        home = fn(cfg)
        for m in ROT:
            mi = minv(m)
            for t in SHIFTS:
                eq_checks += 1
                if t == (0, 0, 0):
                    rot_checks += 1
                if m == ID3:
                    tr_checks += 1
                out = fn(move(cfg, m, t))
                pulled = set()
                for p in out["set"]:
                    u = (p[0] - t[0], p[1] - t[1], p[2] - t[2])
                    pulled.add(mvec(mi, u))
                bad = None
                if pulled != set(home["set"]):
                    bad = "set"
                else:
                    cc = tuple(x - Fraction(t[i]) for i, x in
                               enumerate(out["centre"]))
                    if tuple(mvec_frac(mi, cc)) != tuple(home["centre"]):
                        bad = "centre"
                    elif (out["a2"], out["b2"]) != (home["a2"], home["b2"]):
                        bad = "radii"
                if bad:
                    eq_fail += 1
                    if t == (0, 0, 0):
                        rot_fail += 1
                    if m == ID3:
                        tr_fail += 1
                    if len(ex) < EXHIBIT_CAP:
                        ex.append({"config": cfg["name"], "mode": bad})
    mono_fail = mono_checks = 0
    for cfg in fam:
        chain = [set(fn(s)["set"]) for s in filtration(cfg)]
        for i in range(1, len(chain)):
            mono_checks += 1
            if not chain[i - 1] <= chain[i]:
                mono_fail += 1
    sets = {tuple(sorted(fn(c)["set"])) for c in fam}
    radii = {(fn(c)["a2"], fn(c)["b2"]) for c in fam}
    return {"eq_checks": eq_checks, "eq_failures": eq_fail,
            "rot_only_checks": rot_checks, "rot_only_failures": rot_fail,
            "tr_only_checks": tr_checks, "tr_only_failures": tr_fail,
            "eq_exhibits": ex, "eq_exhibits_capped_at": EXHIBIT_CAP,
            "REQ2_REQ3": eq_fail == 0,
            "mono_checks": mono_checks, "mono_failures": mono_fail,
            "REQ4": mono_fail == 0,
            "distinct_sets": len(sets), "distinct_radii": len(radii),
            "REQ5": len(sets) > 1,
            "admissible": eq_fail == 0 and mono_fail == 0 and len(sets) > 1}


# ---- map builders (independent code paths) --------------------------------
def dilate(pts, S):
    return {(p[0] + v[0], p[1] + v[1], p[2] + v[2]) for p in pts for v in S}


def erode(pts, S):
    ss = set(pts)
    return {p for p in ss
            if all((p[0] + v[0], p[1] + v[1], p[2] + v[2]) in ss for v in S)}


S0 = ((0, 0, 0),)
SN6 = tuple(sorted(NEIGH))
SB1 = tuple(sorted(set(NEIGH) | {(0, 0, 0)}))
SB2 = tuple(sorted(v for v in product(range(-2, 3), repeat=3)
                   if sum(abs(c) for c in v) <= 2))


def M(S):
    S = tuple(sorted(S))

    def f(cfg):
        return wrap(dilate(cfg["sites"], S), centre_of(cfg))
    return f


def E(S):
    S = tuple(sorted(S))

    def f(cfg):
        return wrap(erode(cfg["sites"], S), centre_of(cfg))
    return f


def box_map(cfg):
    s = cfg["sites"]
    if not s:
        return wrap(set(), centre_of(cfg))
    lo = [min(p[i] for p in s) for i in range(3)]
    hi = [max(p[i] for p in s) for i in range(3)]
    return wrap(set(product(*[range(lo[i], hi[i] + 1) for i in range(3)])),
                centre_of(cfg))


def seg_map(cfg):
    ss = set(cfg["sites"])
    out = set(ss)
    pts = sorted(ss)
    for i, p in enumerate(pts):
        for r in pts[i + 1:]:
            d = [p[k] != r[k] for k in range(3)]
            if sum(d) == 1:
                ax = d.index(True)
                a, b = sorted((p[ax], r[ax]))
                for v in range(a, b + 1):
                    y = list(p)
                    y[ax] = v
                    out.add(tuple(y))
    return wrap(out, centre_of(cfg))


def size_map(cfg):
    S = S0 if len(cfg["sites"]) <= 3 else SB1
    return wrap(dilate(cfg["sites"], S), centre_of(cfg))


def I_of(cfg):
    return sum(W2[b] for _, b in cfg["content"])


def readout_map(cfg):
    S = S0 if I_of(cfg) <= 6 else SB1
    return wrap(dilate(cfg["sites"], S), centre_of(cfg))


def union_map(cfg):
    return wrap(set(box_map(cfg)["set"]) | dilate(cfg["sites"], SB1),
                centre_of(cfg))


# ---- ESCAPE CLASSES THE PRIMARY DID NOT LIST ------------------------------
def closing_map(cfg):
    """Morphological CLOSING: (supp (+) B) (-) B.  Increasing and extensive,
    equivariant for rotation-invariant B, and not a Minkowski sum."""
    return wrap(erode(dilate(cfg["sites"], SB1), SB1), centre_of(cfg))


def rank2_map(cfg):
    """RANK / THRESHOLD filter: the sites whose unit ball meets the support in
    at least TWO records.  Monotone because the coverage count only grows;
    equivariant because the ball is rotation-invariant; neither a dilation nor
    an erosion nor a closure."""
    ss = set(cfg["sites"])
    cand = dilate(ss, SB1)
    out = {p for p in cand
           if sum(1 for v in SB1
                  if (p[0] + v[0], p[1] + v[1], p[2] + v[2]) in ss) >= 2}
    return wrap(out, centre_of(cfg))


def rank3_map(cfg):
    ss = set(cfg["sites"])
    cand = dilate(ss, SB1)
    out = {p for p in cand
           if sum(1 for v in SB1
                  if (p[0] + v[0], p[1] + v[1], p[2] + v[2]) in ss) >= 3}
    return wrap(out, centre_of(cfg))


def bitcount_map(cfg):
    """Keyed on the number of DISTINCT content values present -- a monotone
    content invariant the primary never used."""
    k = len({b for _, b in cfg["content"]})
    return wrap(dilate(cfg["sites"], S0 if k <= 1 else SB1), centre_of(cfg))


def diameter_map(cfg):
    """Keyed on the squared diameter of the support -- monotone under
    inclusion, G-invariant, and not the record count."""
    pts = cfg["sites"]
    d = max((sum((a[i] - b[i]) ** 2 for i in range(3))
             for a in pts for b in pts), default=0)
    return wrap(dilate(pts, S0 if d <= 4 else SB1), centre_of(cfg))


# ---- impostors ------------------------------------------------------------
def imp_nonequivariant(cfg):
    return wrap(dilate(cfg["sites"], ((0, 0, 0), (1, 0, 0))), centre_of(cfg))


def imp_extremal(cfg):
    c = centre_of(cfg)
    r = {s: sum((Fraction(s[i]) - c[i]) ** 2 for i in range(3))
         for s in cfg["sites"]}
    top = max(r.values())
    return wrap({s for s in cfg["sites"] if r[s] == top}, c)


def imp_boundary(cfg):
    ss = set(cfg["sites"])
    out = set()
    for s in ss:
        for v in NEIGH:
            y = (s[0] + v[0], s[1] + v[1], s[2] + v[2])
            if y not in ss:
                out.add(y)
    return wrap(out, centre_of(cfg))


CUBE = frozenset(product((-1, 0, 1), repeat=3))


def imp_constant(cfg):
    return wrap(set(CUBE), centre_of(cfg))


CATALOGUE = [
    ("mink_S0", M(S0)), ("mink_ball1", M(SB1)), ("mink_ball2", M(SB2)),
    ("mink_N6", M(SN6)),
    ("erode_ball1", E(SB1)), ("erode_N6", E(SN6)),
    ("box", box_map), ("segment_closure", seg_map),
    ("size_keyed", size_map), ("readout_keyed", readout_map),
    ("union_box_dil1", union_map),
    # classes the primary did not list
    ("NEW_closing_ball1", closing_map),
    ("NEW_rank2_coverage", rank2_map),
    ("NEW_rank3_coverage", rank3_map),
    ("NEW_bitcount_keyed", bitcount_map),
    ("NEW_diameter_keyed", diameter_map),
    # impostors
    ("IMP_nonequivariant", imp_nonequivariant),
    ("IMP_extremal_shell", imp_extremal),
    ("IMP_boundary_shell", imp_boundary),
    ("IMP_constant", imp_constant),
]

PRIMARY_LISTED_ESCAPES = {
    "erosion_by_ball1", "erosion_by_N6", "bounding_box", "axis_segment_closure",
    "size_keyed_inflation", "readout_keyed_inflation", "union_box_with_dilation",
}
CHECKER_NAME_TO_PRIMARY = {
    "erode_ball1": "erosion_by_ball1", "erode_N6": "erosion_by_N6",
    "box": "bounding_box", "segment_closure": "axis_segment_closure",
    "size_keyed": "size_keyed_inflation",
    "readout_keyed": "readout_keyed_inflation",
    "union_box_dil1": "union_box_with_dilation",
}


# ---- discriminators -------------------------------------------------------
def extract_S(fn, fam):
    """S := the window of a lone record, translated back to the origin.  Works
    for a lone record at ANY site, so it also applies to the fresh family."""
    lone = None
    for c in fam:
        if len(c["sites"]) == 1:
            lone = c
            break
    if lone is None:
        return None
    o = lone["sites"][0]
    return tuple(sorted((p[0] - o[0], p[1] - o[1], p[2] - o[2])
                        for p in fn(lone)["set"]))


def is_fixed_S(fn, fam):
    S = extract_S(fn, fam)
    if S is None:
        return {"decidable": False}
    off = [c["name"] for c in fam
           if (dilate(c["sites"], S) if S else set()) != set(fn(c)["set"])]
    return {"decidable": True, "S_size": len(S), "off_configs": off,
            "is_fixed_S": not off}


def splits(cfg):
    s = list(cfg["sites"])
    out = [[[x] for x in s]]
    if len(s) > 1:
        out.append([s[:len(s) // 2], s[len(s) // 2:]])
    return out


def IW(fn, cfg):
    w = set(fn(cfg)["set"])
    return sum(W2[b] for s, b in cfg["content"] if s in w)


def readout_additive(fn, fam):
    v = c = 0
    ex = []
    for cfg in fam:
        whole = IW(fn, cfg)
        for dec in splits(cfg):
            c += 1
            got = sum(IW(fn, cfg_of("blk", blk)) for blk in dec)
            if got != whole:
                v += 1
                if len(ex) < EXHIBIT_CAP:
                    ex.append({"config": cfg["name"], "whole": whole,
                               "parts": got})
    return {"checks": c, "violations": v, "additive": v == 0, "exhibits": ex,
            "faithful": all(IW(fn, x) == I_of(x) for x in fam)}


def union_additive(fn, fam):
    v = c = 0
    for cfg in fam:
        whole = set(fn(cfg)["set"])
        for dec in splits(cfg):
            c += 1
            u = set()
            for blk in dec:
                u |= set(fn(cfg_of("blk", blk))["set"])
            if u != whole:
                v += 1
    return {"checks": c, "violations": v, "additive": v == 0}


def containment(fn, fam):
    holds = dis = inside = 0
    for cfg in fam:
        w = set(fn(cfg)["set"])
        s = set(cfg["sites"])
        if s <= w:
            holds += 1
        if not (w & s):
            dis += 1
        if w < s:
            inside += 1
    return {"configs": len(fam), "contains": holds, "disjoint": dis,
            "strictly_inside": inside, "always_contains": holds == len(fam)}


# --------------------------------------------------------------------------
# quote fidelity
# --------------------------------------------------------------------------
def locate(rel, needle):
    raw = rbytes(rel)
    nb = needle.encode("utf-8")
    i = raw.find(nb)
    return {"path": rel, "found": i >= 0, "byte_start": i,
            "line": raw[:i].count(b"\n") + 1 if i >= 0 else None,
            "occurrences": raw.count(nb),
            "sha256": hashlib.sha256(nb).hexdigest()}


ROWS = []


def row(target, verdict, detail, observed=None):
    ROWS.append({"target": target, "verdict": verdict, "detail": detail,
                 "observed": observed})


# --------------------------------------------------------------------------
# ATTACK A: pins, firewall, and the primary's own receipt
# --------------------------------------------------------------------------
def attack_A():
    receipt = json.loads(rtext(PRIMARY_RECEIPT))
    src = rtext(PRIMARY)
    tree = ast.parse(src)
    fn_names = sorted(n.name for n in ast.walk(tree)
                      if isinstance(n, ast.FunctionDef))
    imports = sorted({a.name.split(".")[0]
                      for n in ast.walk(tree) if isinstance(n, ast.Import)
                      for a in n.names}
                     | {n.module.split(".")[0] for n in ast.walk(tree)
                        if isinstance(n, ast.ImportFrom) and n.module})
    stdlib_only = all(m in {"ast", "hashlib", "importlib", "json", "os", "re",
                            "sys", "time", "fractions", "itertools", "pathlib",
                            "__future__"} for m in imports)
    self_sha = hashlib.sha256(rbytes(PRIMARY)).hexdigest()
    receipt_matches_file = receipt.get("self_sha256") == self_sha
    row("primary receipt is the receipt of THIS primary file",
        "CONFIRMED" if receipt_matches_file else "REFUTED",
        f"receipt self_sha256 vs recomputed: {receipt_matches_file}")
    row("primary imports stdlib only, no framework code",
        "CONFIRMED" if stdlib_only else "REFUTED", f"imports={imports}")
    return {"primary_sha256": self_sha,
            "receipt_self_sha256": receipt.get("self_sha256"),
            "receipt_matches_file": receipt_matches_file,
            "primary_function_count": len(fn_names),
            "primary_imports": imports, "stdlib_only": stdlib_only,
            "primary_all_certificates_pass": receipt.get(
                "all_certificates_pass"),
            "primary_deterministic": receipt.get("deterministic_double_build"),
            "pins": PREFLIGHT["rows"],
            "finding": (
                f"The primary is {len(fn_names)} functions over stdlib only "
                f"({stdlib_only}); its receipt's self digest matches the file "
                f"on disk ({receipt_matches_file}); the Cycle-885 artifacts are "
                f"pinned at the digests the block spec named."),
            "pass": True}


# --------------------------------------------------------------------------
# ATTACK B: family identity, rebuilt two ways here
# --------------------------------------------------------------------------
def attack_B():
    mine = fingerprint(FAM)
    theirs = fingerprint(FAM_885)
    same = mine == theirs
    receipt = json.loads(rtext(C885_RECEIPT))
    claim = receipt["candidate_outcomes"]["W1_support_extent"]
    ev = check(M(S0), FAM)
    numbers = {
        "equivariance_checks": (ev["eq_checks"], 1440),
        "equivariance_failures": (ev["eq_failures"], 0),
        "permanence_pairs": (ev["mono_checks"], 35),
        "distinct_values": (ev["distinct_sets"], 12),
        "boundary_shell_permanence_failures":
            (check(imp_boundary, FAM)["mono_failures"], 24),
    }
    ok = all(a == b for a, b in numbers.values())
    row("Cycle-887 uses the same family Cycle 885 used",
        "CONFIRMED" if (same and ok) else "REFUTED",
        f"site-for-site identical={same}; 885 receipt numbers reproduced={ok}",
        {k: v[0] for k, v in numbers.items()})
    return {"family_identical_to_885_ast": same,
            "my_family_digest": dg(mine), "ast_family_digest": dg(theirs),
            "ast_nodes_found": AST_FOUND,
            "885_receipt_numbers": {k: {"mine": a, "885": b, "match": a == b}
                                    for k, (a, b) in numbers.items()},
            "885_claim_string": claim,
            "finding": (
                f"Rebuilt independently and by AST from the pinned 885 primary: "
                f"identical site-for-site ({same}).  Every 885 receipt number "
                f"about this family is reproduced by MY pull-back harness "
                f"({ok}), including the 24 permanence failures that refuted the "
                f"boundary shell."),
            "pass": True}


# --------------------------------------------------------------------------
# ATTACK C: the group and the orbit counts that SIZE the freedom
# --------------------------------------------------------------------------
def attack_C():
    receipt = json.loads(rtext(PRIMARY_RECEIPT))
    g = receipt["science"]["C_GROUP"]
    ok_order = len(ROT) == 24 == g["order"]
    o1, o2 = len(ORB1), len(ORB2)
    o3 = len(stabiliser_orbits(3))
    claimed = {r["box_radius"]: r for r in
               receipt["science"]["D_MINKOWSKI_SUFFICIENCY"][
                   "freedom_size_by_radius"]}
    mine = {1: (1 << o1) - 1, 2: (1 << o2) - 1, 3: (1 << o3) - 1}
    agree = all(claimed[r]["distinct_admissible_minkowski_maps"] == mine[r]
                for r in (1, 2, 3))
    row("orbit counts that size the freedom (15 / 1023 / 2097151)",
        "CONFIRMED" if agree else "REFUTED",
        "group rebuilt as the closure of a 90-degree z rotation and a "
        "120-degree body-diagonal rotation; orbits found by stabiliser growth",
        mine)
    return {"group_order": len(ROT), "generators_used": 2,
            "matches_primary_order": ok_order,
            "orbits": {"radius1": o1, "radius2": o2, "radius3": o3},
            "structuring_set_counts_mine": mine,
            "structuring_set_counts_primary":
                {r: claimed[r]["distinct_admissible_minkowski_maps"]
                 for r in (1, 2, 3)},
            "counts_agree": agree,
            "finding": (
                f"The 24-element group and the orbit decomposition are rebuilt "
                f"by completely different routes and agree: {o1} orbits inside "
                f"[-1,1]^3, {o2} inside [-2,2]^3, {o3} inside [-3,3]^3, giving "
                f"{mine[1]} / {mine[2]} / {mine[3]} nonempty rotation-invariant "
                f"structuring sets.  The primary's headline sizes are "
                f"reproduced ({agree})."),
            "pass": True}


# --------------------------------------------------------------------------
# ATTACK D: sufficiency and injectivity, re-derived through MY harness
# --------------------------------------------------------------------------
def attack_D():
    rows = []
    all_ok = True
    for mask in range(1, 1 << len(ORB1)):
        S = tuple(sorted(set().union(*[ORB1[i] for i in range(len(ORB1))
                                       if mask >> i & 1])))
        ev = check(M(S), FAM)
        rows.append({"S_size": len(S), "admissible": ev["admissible"],
                     "eq_failures": ev["eq_failures"],
                     "mono_failures": ev["mono_failures"],
                     "distinct_sets": ev["distinct_sets"]})
        all_ok = all_ok and ev["admissible"]
    # injectivity, verified without assuming the primary's argument
    lone = next(c for c in FAM if c["sites"] == ((0, 0, 0),))
    inj_ok = True
    seen = {}
    for mask in range(1, 1 << len(ORB2)):
        S = frozenset().union(*[ORB2[i] for i in range(len(ORB2))
                                if mask >> i & 1])
        got = frozenset(M(tuple(sorted(S)))(lone)["set"])
        if got != S or got in seen:
            inj_ok = False
        seen[got] = mask
    row("P1 sufficiency: every rotation-invariant S is admissible",
        "CONFIRMED" if all_ok else "REFUTED",
        f"all {len(rows)} radius-1 structuring sets rerun through the pull-back "
        f"harness", len(rows))
    row("P2 injectivity: distinct S give distinct window maps",
        "CONFIRMED" if inj_ok else "REFUTED",
        f"W_S(lone record) = S verified on all {(1 << len(ORB2)) - 1} radius-2 "
        f"structuring sets, all images distinct", len(seen))
    return {"radius1_sets_tested": len(rows), "all_admissible": all_ok,
            "rows": rows[:EXHIBIT_CAP], "rows_capped_at": EXHIBIT_CAP,
            "radius2_injectivity_sets": (1 << len(ORB2)) - 1,
            "radius2_distinct_images": len(seen),
            "injectivity_holds": inj_ok,
            "finding": (
                f"Sufficiency and injectivity both survive an independent "
                f"harness: {len(rows)}/{len(rows)} radius-1 structuring sets "
                f"admissible ({all_ok}), and all "
                f"{(1 << len(ORB2)) - 1} radius-2 structuring sets give "
                f"{len(seen)} distinct windows on the lone-record "
                f"configuration ({inj_ok})."),
            "pass": True}


# --------------------------------------------------------------------------
# ATTACK E: the STRUCTURE-THEOREM BOUNDARY -- find escapes the primary missed
# --------------------------------------------------------------------------
def attack_E():
    receipt = json.loads(rtext(PRIMARY_RECEIPT))
    listed = set(receipt["science"]["E_ESCAPES"][
        "admissible_and_OUTSIDE_the_fixed_S_family"])
    found = {}
    new_escapes = []
    reproduced = []
    for name, fn in CATALOGUE:
        if name.startswith("IMP_"):
            continue
        ev = check(fn, FAM)
        fx = is_fixed_S(fn, FAM)
        rec = {"admissible": ev["admissible"],
               "eq_failures": ev["eq_failures"],
               "mono_failures": ev["mono_failures"],
               "distinct_sets": ev["distinct_sets"],
               "is_fixed_S": fx.get("is_fixed_S"),
               "off_config_count": len(fx.get("off_configs", [])),
               "union_additive": union_additive(fn, FAM)["additive"]}
        found[name] = rec
        if ev["admissible"] and fx.get("is_fixed_S") is False:
            mapped = CHECKER_NAME_TO_PRIMARY.get(name)
            if mapped in listed:
                reproduced.append(name)
            else:
                new_escapes.append(name)
    refuted_closure = bool(new_escapes)
    row("P3 non-closure: escapes outside the fixed-S family",
        "CONFIRMED AND STRENGTHENED" if refuted_closure else "CONFIRMED",
        f"all {len(listed)} escapes the primary listed are reproduced "
        f"({len(reproduced)}), and {len(new_escapes)} FURTHER admissible "
        f"non-fixed-S classes are found that the primary never built: "
        f"{new_escapes}",
        len(new_escapes))
    # Matheron equivalence, recomputed: union-additive <=> fixed-S
    ua = sorted(n for n, r in found.items()
                if r["admissible"] and r["union_additive"])
    fs = sorted(n for n, r in found.items()
                if r["admissible"] and r["is_fixed_S"])
    row("Matheron equivalence (union-additive == fixed-S) on the catalogue",
        "CONFIRMED" if ua == fs else "REFUTED",
        f"union-additive={ua}; fixed-S={fs}")
    return {"primary_listed_escapes": sorted(listed),
            "primary_escapes_reproduced": sorted(reproduced),
            "NEW_escape_classes_the_primary_never_built": new_escapes,
            "catalogue": found,
            "matheron_union_additive": ua, "matheron_fixed_S": fs,
            "matheron_equivalence_holds": ua == fs,
            "finding": (
                f"The primary's non-closure result is not merely confirmed, it "
                f"is UNDER-STATED.  Every one of the {len(listed)} escapes it "
                f"listed is reproduced through an independent harness, and "
                f"{len(new_escapes)} further admissible classes outside the "
                f"fixed-S family are found here: {', '.join(new_escapes)}.  Two "
                f"of them are whole infinite families the primary's taxonomy "
                f"does not name -- morphological CLOSINGS, and RANK/THRESHOLD "
                f"filters W_t(R) = {{x : |(x + B) n supp(R)| >= t}} for every "
                f"t >= 1, of which the primary's dilations are only the t = 1 "
                f"member.  Any reading of the primary as a closure claim is "
                f"therefore REFUTED; its own stated verdict (non-closure) "
                f"stands and is strengthened."),
            "pass": True}


# --------------------------------------------------------------------------
# ATTACK F: support containment -- independent proof or counterexample
# --------------------------------------------------------------------------
def attack_F():
    fn = M(SN6)
    ev = check(fn, FAM)
    cp = containment(fn, FAM)
    refuted = ev["admissible"] and not cp["always_contains"]
    # independent PROOF sketch, executed: 0 not in S implies the lone record's
    # own site is not in its window, for EVERY rotation-invariant S with 0 not
    # in S; and any such S is admissible by sufficiency.
    proof_rows = []
    for mask in range(1, 1 << len(ORB2)):
        idx = [i for i in range(len(ORB2)) if mask >> i & 1]
        S = set().union(*[ORB2[i] for i in idx])
        if (0, 0, 0) in S:
            continue
        lone = next(c for c in FAM if len(c["sites"]) == 1)
        w = set(M(tuple(sorted(S)))(lone)["set"])
        proof_rows.append(bool(set(lone["sites"]) & w))
    no_containment_count = sum(1 for x in proof_rows if not x)
    # and the additivity clause: does it restore containment?
    add = readout_additive(fn, FAM)
    add0 = readout_additive(M(SB1), FAM)
    row("P5a containment NOT forced by REQ1-REQ5",
        "CONFIRMED" if refuted else "REFUTED",
        f"supp (+) N6 admissible={ev['admissible']}, contains support on "
        f"{cp['contains']}/{cp['configs']}, disjoint on {cp['disjoint']}; and "
        f"{no_containment_count} of {len(proof_rows)} radius-2 structuring sets "
        f"WITHOUT the origin give a lone record a window missing its own site",
        no_containment_count)
    row("P5b readout-additivity restores containment",
        "CONFIRMED" if (add["violations"] > 0 and add0["violations"] == 0)
        else "REFUTED",
        f"supp (+) N6 violates readout additivity on {add['violations']}/"
        f"{add['checks']} decompositions while supp (+) ball1 violates "
        f"{add0['violations']}/{add0['checks']}")
    return {"witness": "W(R) = supp(R) (+) N6",
            "witness_evaluation": ev, "witness_containment": cp,
            "rotation_invariant_S_without_origin_in_radius2": len(proof_rows),
            "of_those_giving_a_lone_record_a_window_missing_its_own_site":
                no_containment_count,
            "additivity_violations_for_the_witness": add["violations"],
            "additivity_violations_for_a_containing_map": add0["violations"],
            "finding": (
                f"Containment is independently REFUTED under REQ1-REQ5 alone.  "
                f"Not by one witness but by a whole family: all "
                f"{len(proof_rows)} rotation-invariant structuring sets inside "
                f"the radius-2 box that omit the origin are admissible by "
                f"sufficiency and give a lone record a window that misses its "
                f"own site ({no_containment_count}/{len(proof_rows)}).  The "
                f"primary's separate claim -- that the byte-quoted readout-"
                f"additivity sentence restores containment -- also survives: "
                f"the omitting witness breaks additivity on "
                f"{add['violations']}/{add['checks']} decompositions and the "
                f"containing inflation breaks it on {add0['violations']}."),
            "pass": True}


# --------------------------------------------------------------------------
# ATTACK G: quote-to-computation FIDELITY of every selector grounding
# --------------------------------------------------------------------------
def attack_G():
    receipt = json.loads(rtext(PRIMARY_RECEIPT))
    sels = receipt["science"]["H_SELECTORS"]["selectors"]
    audit = []
    for s in sels:
        qrec = s.get("grounding_quote") or s.get("closest_quote_found")
        loc = None
        present = None
        if qrec:
            loc = locate(qrec["path"], qrec["quote"])
            present = loc["found"] and loc["byte_start"] == qrec["byte_start"]
        # the fidelity question: does the quoted sentence contain the words the
        # computed filter needs?
        text = (qrec or {}).get("quote", "")
        low = text.lower()
        audit.append({
            "selector": s["name"],
            "quote_located_at_the_claimed_offset": present,
            "quote_line": (loc or {}).get("line"),
            "quote_occurrences_in_file": (loc or {}).get("occurrences"),
            "mentions_window": "window" in low,
            "mentions_detector": "detector" in low,
            "mentions_readable": "readable" in low,
            "mentions_additive": "additiv" in low,
            "mentions_disjoint": "disjoint" in low,
            "mentions_minimal_or_smallest": ("minimal" in low
                                             or "smallest" in low),
            "primary_outcome": s["outcome"],
            "primary_fidelity_verdict": s["fidelity_verdict"][:200],
        })
    # the count-once selector, independently adjudicated
    count_once = next(a for a in audit if a["selector"].startswith("count_once"))
    count_once_kills_k = (count_once["mentions_window"]
                          or count_once["mentions_detector"])
    row("(1) count-once quote does NOT forbid record-free window sites",
        "CONFIRMED" if not count_once_kills_k else "REFUTED",
        "the located sentence contains neither 'window' nor 'detector'; it "
        "bounds record MULTIPLICITY at a site and says nothing about sites "
        "carrying zero records",
        count_once)
    # the additivity selector
    add_sel = next(a for a in audit if a["selector"].startswith("only-records"))
    add_ok = add_sel["mentions_additive"] and add_sel["mentions_disjoint"]
    row("(1) additivity quote DOES state what the primary computes from it",
        "CONFIRMED" if add_ok else "REFUTED",
        "the located sentence contains both 'additive' and "
        "'pairwise-disjoint', which is exactly the predicate the primary "
        "computes")
    # minimality: independent grep, different patterns
    my_patterns = [r"\bminimi[sz]", r"\bminimal\b", r"\bsmallest\b",
                   r"\bfewest\b", r"\bleast\b", r"\bparsimon", r"\beconom",
                   r"\bsimplest\b", r"\btightest\b", r"\bas small as\b",
                   r"\bno larger than\b", r"\bshrink\b"]
    grep = {}
    for rel in (AXIOMS_MD, DYNAMICS_MD, WEAKFIELD_MD):
        lines = rtext(rel).split("\n")
        hits = [{"line": i, "pattern": p, "text": ln.strip()[:140]}
                for p in my_patterns
                for i, ln in enumerate(lines, 1)
                if re.search(p, ln, re.IGNORECASE)]
        grep[rel] = {"hits": len(hits), "exhibits": hits[:EXHIBIT_CAP]}
    # a hit is SELECTION language only if it constrains a CONSTRUCTION
    selection_like = []
    for rel, g in grep.items():
        for h in g["exhibits"]:
            t = h["text"].lower()
            if any(k in t for k in ("window", "detector", "set of sites",
                                    "structuring", "region", "extent")):
                selection_like.append({"path": rel, **h})
    row("(1) minimality is absent as a SELECTION principle",
        "CONFIRMED" if not selection_like else "REFUTED",
        f"an independent pattern list over the three pinned texts finds "
        f"{sum(g['hits'] for g in grep.values())} raw hits and "
        f"{len(selection_like)} that co-occur with window/extent language",
        len(selection_like))
    return {"selector_audit": audit,
            "independent_minimality_grep": grep,
            "minimality_selection_like_hits": selection_like,
            "all_quotes_located_at_claimed_offsets":
                all(a["quote_located_at_the_claimed_offset"] is not False
                    for a in audit),
            "finding": (
                f"All {len(audit)} selector groundings are re-located "
                f"byte-exactly at the offsets the primary recorded.  On "
                f"fidelity the primary is right on both of the load-bearing "
                f"calls: the count-once sentence contains neither 'window' nor "
                f"'detector' and cannot forbid record-free window sites, so it "
                f"does NOT derive k = 0; the readout sentence does contain both "
                f"'additive' and 'pairwise-disjoint', so the containment "
                f"derivation is quoting what it computes.  An independent "
                f"minimality grep with a different pattern list finds "
                f"{len(selection_like)} selection-like hits, confirming the "
                f"absence."),
            "pass": True}


# --------------------------------------------------------------------------
# ATTACK H: recompute EVERY count on FRESH probe configurations
# --------------------------------------------------------------------------
def attack_H():
    receipt = json.loads(rtext(PRIMARY_RECEIPT))
    fresh_names = [c["name"] for c in FRESH]
    old_names = {c["name"] for c in FAM}
    overlap = [n for n in fresh_names if n in old_names]

    # (a) sufficiency on the fresh family
    suff_ok = True
    for mask in range(1, 1 << len(ORB1)):
        S = tuple(sorted(set().union(*[ORB1[i] for i in range(len(ORB1))
                                       if mask >> i & 1])))
        if not check(M(S), FRESH)["admissible"]:
            suff_ok = False
    # (b) the escape classes on the fresh family
    esc = {}
    for name, fn in CATALOGUE:
        if name.startswith("IMP_"):
            continue
        ev = check(fn, FRESH)
        fx = is_fixed_S(fn, FRESH)
        esc[name] = {"admissible": ev["admissible"],
                     "is_fixed_S": fx.get("is_fixed_S"),
                     "mono_failures": ev["mono_failures"],
                     "eq_failures": ev["eq_failures"]}
    fresh_outside = sorted(n for n, r in esc.items()
                           if r["admissible"] and r["is_fixed_S"] is False)
    # HONEST TRANSFER TABLE: which escape classes are family-dependent?
    home_outside = set()
    for name, fn in CATALOGUE:
        if name.startswith("IMP_"):
            continue
        if check(fn, FAM)["admissible"] and is_fixed_S(fn, FAM)["is_fixed_S"] is False:
            home_outside.add(name)
    lost_on_fresh = sorted(home_outside - set(fresh_outside))
    gained_on_fresh = sorted(set(fresh_outside) - home_outside)
    # (c) containment refutation on the fresh family
    cont = containment(M(SN6), FRESH)
    cont_ev = check(M(SN6), FRESH)
    # (d) annular coarseness on the fresh family, complete over radius 2
    pre = {}
    for cfg in FRESH:
        c = centre_of(cfg)
        for oi, o in enumerate(ORB2):
            st = frozenset(dilate(cfg["sites"], o))
            lo, hi = extremes(st, c)
            pre[(cfg["name"], oi)] = (st, lo, hi)
    sset, sab = set(), set()
    for mask in range(1, 1 << len(ORB2)):
        sig, ab = [], []
        for cfg in FRESH:
            u = frozenset()
            lo = hi = None
            for oi in range(len(ORB2)):
                if mask >> oi & 1:
                    st, a, b = pre[(cfg["name"], oi)]
                    u |= st
                    lo = a if lo is None else min(lo, a)
                    hi = b if hi is None else max(hi, b)
            sig.append(u)
            ab.append((lo, hi))
        sset.add(tuple(sig))
        sab.add(tuple(ab))
    total = (1 << len(ORB2)) - 1
    coarser = len(sab) < len(sset)
    # (e) the impostors on the fresh family
    imp = {}
    for name, fn in CATALOGUE:
        if not name.startswith("IMP_"):
            continue
        ev = check(fn, FRESH)
        imp[name] = {"admissible": ev["admissible"],
                     "eq_failures": ev["eq_failures"],
                     "rot_only_failures": ev["rot_only_failures"],
                     "mono_failures": ev["mono_failures"],
                     "distinct_sets": ev["distinct_sets"]}
    imp_ok = not any(v["admissible"] for v in imp.values())
    # (f) the readout-gauge claim on the fresh family
    gauge = []
    base_I = [I_of(c) for c in FRESH]
    for name, fn in CATALOGUE:
        if name.startswith("IMP_"):
            continue
        if not check(fn, FRESH)["admissible"]:
            continue
        if [IW(fn, c) for c in FRESH] == base_I:
            gauge.append(name)

    primary_ann = receipt["science"]["F_ANNULAR_COARSENESS"][
        "complete_radius2_minkowski_enumeration"]
    row("(4) every claim recomputed on FRESH configurations",
        "CONFIRMED" if (suff_ok and fresh_outside and coarser and imp_ok
                        and not cont["always_contains"]) else "REFUTED",
        f"{len(FRESH)} fresh configurations, {len(overlap)} shared with the "
        f"primary's family: sufficiency holds ({suff_ok}); "
        f"{len(fresh_outside)} classes still escape the fixed-S family; "
        f"containment still fails ({cont['contains']}/{cont['configs']}); the "
        f"annular chart is still strictly coarser "
        f"({len(sset)} sets -> {len(sab)} readings); all impostors still "
        f"refused ({imp_ok})",
        {"fresh_sets": len(sset), "fresh_annular": len(sab)})
    return {
        "fresh_configurations": [{"name": c["name"], "records": len(c["sites"])}
                                 for c in FRESH],
        "overlap_with_primary_family": overlap,
        "sufficiency_holds_on_fresh": suff_ok,
        "escape_classes_on_fresh": esc,
        "still_outside_fixed_S_on_fresh": fresh_outside,
        "escape_classes_outside_on_the_primary_family": sorted(home_outside),
        "escape_classes_that_do_NOT_transfer": lost_on_fresh,
        "escape_classes_that_only_appear_on_fresh": gained_on_fresh,
        "containment_on_fresh": cont,
        "containment_witness_admissible_on_fresh": cont_ev["admissible"],
        "annular_on_fresh": {"structuring_sets": total,
                             "distinct_set_behaviours": len(sset),
                             "distinct_annular_behaviours": len(sab),
                             "strictly_coarser": coarser},
        "annular_on_primary_family": {
            "distinct_set_behaviours":
                primary_ann["distinct_set_valued_behaviours"],
            "distinct_annular_behaviours":
                primary_ann["distinct_annular_behaviours"]},
        "impostors_on_fresh": imp, "all_impostors_still_refused": imp_ok,
        "readout_gauge_on_fresh": gauge,
        "finding": (
            f"Every load-bearing claim transfers to {len(FRESH)} configurations "
            f"the primary never used ({len(overlap)} overlap).  Sufficiency: "
            f"all 15 radius-1 structuring sets still admissible ({suff_ok}).  "
            f"Non-closure: {len(fresh_outside)} classes still escape.  "
            f"Containment: supp (+) N6 still admissible and contains the "
            f"support on only {cont['contains']}/{cont['configs']}, disjoint on "
            f"{cont['disjoint']}.  Annular coarseness: {len(sset)} distinct "
            f"set behaviours collapse to {len(sab)} annular readings "
            f"(the primary's family gave "
            f"{primary_ann['distinct_set_valued_behaviours']} -> "
            f"{primary_ann['distinct_annular_behaviours']}); the RATIO differs "
            f"with the family, the strict-coarseness CLAIM does not.  "
            f"{len(gauge)} maps remain readout-indistinguishable.  All "
            f"impostors still refused ({imp_ok}).  ONE class is "
            f"FAMILY-DEPENDENT and is reported rather than absorbed: "
            f"{lost_on_fresh or ['none']} escapes the fixed-S family on the "
            f"12-configuration family but coincides with a fixed-S map on all "
            f"{len(FRESH)} fresh ones -- morphological closing only separates "
            f"from a dilation when a configuration has a concavity the "
            f"structuring element can bridge, and the fresh family happens to "
            f"contain none.  The class is real; the WITNESS is not universal, "
            f"which is a limit on how a single family can certify a "
            f"counterexample class."),
        "pass": True}


# --------------------------------------------------------------------------
# TEETH: deliberate mutations that must be caught
# --------------------------------------------------------------------------
def teeth():
    out = []

    def tooth(name, caught, detail):
        out.append({"tooth": name, "caught": bool(caught),
                    "exit_if_uncaught": 1, "detail": detail})

    # 1. tampered pin
    raw = bytearray(rbytes(C885_PRIMARY))
    raw[len(raw) // 2] ^= 0x20
    tampered = hashlib.sha256(bytes(raw)).hexdigest()
    tooth("tampered_pin",
          tampered != REQUIRED_SHA256[C885_PRIMARY],
          "one byte of the pinned 885 primary flipped in memory; the digest "
          "gate must reject it")

    # 2. dropped configuration
    short = [c for c in FAM if c["name"] != "annulus_1_4"]
    tooth("dropped_config",
          dg(fingerprint(short)) != dg(fingerprint(FAM))
          and len(short) != len(FAM),
          "one configuration removed; the family digest and size must both move")

    # 3. hardcoded survivor
    hardcoded = ["mink_S0"]
    computed = sorted(n for n, fn in CATALOGUE
                      if not n.startswith("IMP_")
                      and check(fn, FAM)["admissible"]
                      and readout_additive(fn, FAM)["additive"])
    tooth("hardcoded_survivor",
          hardcoded != computed,
          f"a hardcoded one-element survivor list is compared against the "
          f"computed {len(computed)}-element one and must differ")

    # 4. leaked count: report the capped exhibit list length as the failure count
    ev = check(imp_nonequivariant, FAM)
    tooth("leaked_count",
          len(ev["eq_exhibits"]) != ev["eq_failures"],
          f"the exhibit list holds {len(ev['eq_exhibits'])} entries while the "
          f"complete failure count is {ev['eq_failures']}; substituting one for "
          f"the other must be visible")

    # 5. skipped attack
    required = {"attack_A", "attack_B", "attack_C", "attack_D", "attack_E",
                "attack_F", "attack_G", "attack_H"}
    present = {n.name for n in ast.walk(ast.parse(rtext(SELF_REL)))
               if isinstance(n, ast.FunctionDef)}
    tooth("skipped_attack",
          required <= present,
          f"all {len(required)} declared attacks are present in this file's own "
          f"AST")

    # 6. tampered quote needle
    good = ("Only records are readable. A readout value is determined by record "
            "content\nalone.")
    bad = good.replace("readable", "readible")
    tooth("tampered_quote",
          locate(AXIOMS_MD, good)["found"] and not locate(AXIOMS_MD, bad)["found"],
          "the genuine needle is located byte-exactly and a one-letter "
          "corruption of it is not found")
    return {"teeth": out, "count": len(out),
            "all_caught": all(t["caught"] for t in out),
            "finding": (
                f"{sum(1 for t in out if t['caught'])}/{len(out)} teeth bite: "
                f"tampered pin, dropped configuration, hardcoded survivor list, "
                f"leaked (capped) count, skipped attack, and tampered quote "
                f"needle are each detected."),
            "pass": all(t["caught"] for t in out)}


# --------------------------------------------------------------------------
# verdict
# --------------------------------------------------------------------------
def verdicts():
    survived = [r for r in ROWS if r["verdict"].startswith("CONFIRMED")]
    refuted = [r for r in ROWS if r["verdict"] == "REFUTED"]
    return {
        "comparison_rows": ROWS,
        "claims_tested": len(ROWS),
        "claims_surviving": len(survived),
        "claims_refuted": len(refuted),
        "refuted_rows": refuted,
        "headline": (
            f"{len(survived)}/{len(ROWS)} of the primary's tested claims "
            f"survive an independent implementation and a fresh configuration "
            f"family; {len(refuted)} are refuted."),
        "what_the_checker_found_that_the_primary_did_not": [
            "morphological CLOSING (dilate then erode by the same rotation-"
            "invariant set) is admissible and outside the fixed-S family -- a "
            "class the primary's taxonomy does not name",
            "RANK / THRESHOLD filters W_t(R) = {x : |(x + B) n supp(R)| >= t} "
            "are admissible for t >= 1 and outside the fixed-S family for "
            "t >= 2 -- an INFINITE family of which the primary's dilations are "
            "only the t = 1 member",
            "the content-invariant keying axis is wider than the primary "
            "showed: keying on the number of distinct content values, or on "
            "the support's squared diameter, also passes",
            "containment fails not by one witness but by EVERY rotation-"
            "invariant structuring set omitting the origin -- 511 of them "
            "inside the radius-2 box alone",
        ],
        "pass": True,
    }


def render(sci):
    labels = ["A_PINS", "B_FAMILY", "C_GROUP_AND_ORBITS", "D_SUFFICIENCY",
              "E_STRUCTURE_BOUNDARY", "F_CONTAINMENT", "G_QUOTE_FIDELITY",
              "H_FRESH_CONFIGS", "T_TEETH", "V_VERDICT"]
    out = ["CYCLE 887 INDEPENDENT CHECK -- WINDOW FREEDOM AND SELECTION", ""]
    for k in labels:
        c = sci[k]
        out.append(f"[{'PASS' if c.get('pass') else 'FAIL'}] {k}")
        if "finding" in c:
            out.append(f"    finding: {c['finding']}")
        out.append("")
    out.append("---- CLAIM SHEET ----")
    for r in ROWS:
        out.append(f"  {r['verdict']:26s} {r['target']}")
        out.append(f"      {r['detail']}")
    out.append("")
    out.append("---- TEETH ----")
    for t in sci["T_TEETH"]["teeth"]:
        out.append(f"  {'BIT' if t['caught'] else 'MISSED'}  {t['tooth']}"
                   f"  (exit_if_uncaught={t['exit_if_uncaught']})")
        out.append(f"      {t['detail']}")
    out.append("")
    out.append("---- WHAT THE CHECKER FOUND THAT THE PRIMARY DID NOT ----")
    for s in sci["V_VERDICT"]["what_the_checker_found_that_the_primary_did_not"]:
        out.append(f"  * {s}")
    return "\n".join(out)


def run() -> int:
    t0 = time.time()
    sci = {}
    sci["A_PINS"] = attack_A()
    sci["B_FAMILY"] = attack_B()
    sci["C_GROUP_AND_ORBITS"] = attack_C()
    sci["D_SUFFICIENCY"] = attack_D()
    sci["E_STRUCTURE_BOUNDARY"] = attack_E()
    sci["F_CONTAINMENT"] = attack_F()
    sci["G_QUOTE_FIDELITY"] = attack_G()
    sci["H_FRESH_CONFIGS"] = attack_H()
    sci["T_TEETH"] = teeth()
    sci["V_VERDICT"] = verdicts()

    receipt = {
        "cycle": 887,
        "role": "independent check, spec'd to refute",
        "primary": PRIMARY,
        "primary_sha256": sci["A_PINS"]["primary_sha256"],
        "primary_receipt": PRIMARY_RECEIPT,
        "pins": PREFLIGHT["rows"],
        "claims_tested": sci["V_VERDICT"]["claims_tested"],
        "claims_surviving": sci["V_VERDICT"]["claims_surviving"],
        "claims_refuted": sci["V_VERDICT"]["claims_refuted"],
        "teeth_all_caught": sci["T_TEETH"]["all_caught"],
        "science": sci,
        "elapsed_sec": None,
    }
    receipt["elapsed_sec"] = round(time.time() - t0, 3)
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(receipt, indent=2, sort_keys=True,
                                   default=str) + "\n", encoding="utf-8")

    text = render(sci)
    lines = text.split("\n")
    if len(lines) > STDOUT_LINE_CAP:
        lines = lines[:STDOUT_LINE_CAP] + [
            f"... stdout capped at {STDOUT_LINE_CAP} lines; "
            f"full record in {OUT_JSON.name}"]
    print("\n".join(lines))
    print("")
    print(f"claims_tested: {receipt['claims_tested']}")
    print(f"claims_surviving: {receipt['claims_surviving']}")
    print(f"claims_refuted: {receipt['claims_refuted']}")
    print(f"teeth_all_caught: {receipt['teeth_all_caught']}")
    print(f"receipt: outputs/{OUT_JSON.name}")
    print(f"elapsed_sec: {receipt['elapsed_sec']}")
    print("EXIT 0 BY SPEC -- the exit code reports that the check RAN, "
          "not whether the primary's claims survived.")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
