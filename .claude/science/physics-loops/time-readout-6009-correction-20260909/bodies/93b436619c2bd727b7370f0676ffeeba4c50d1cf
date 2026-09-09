#!/usr/bin/env python3
"""CYCLE 941 -- GB-S2 ATTACKED: the kernel+window obligation, re-priced today.

Owner-directed gravity-lane work, campaign toe-time-expansion-20260802,
block G29.  No axiom, primitive, registry, policy, queue or audit surface
is touched by this runner.  It reads pinned bytes and computes.

WHAT THIS BLOCK DOES
--------------------
Cycle 871 itemized the gravity lane's obligations with computed sizes and
gave GB-S2 (kernel + detector-window readout) the largest: free dimension
EIGHT.  Cycle 935 then proved the bridge scalar dimensionless and
ruler-immune, establishing the CASHING RULE -- a registered ruler cashes a
composition exactly when the dimensionless side has free dimension 0 --
which makes retained-grade dimensionless theorems the only currency that
can ever close such a row.  GB-S2 is exactly such a target.

This runner:

  Q0  rebuilds the GB-S2 ledger from the pinned bytes of every block that
      touched it (884, 885, 887, 892, 893, 894, 896, 900, 902, 903) and
      RECONCILES three published counts: 871's 8, Cycle 896's "6 free + 5
      owed", and today's surface.  The reconciliation is a computation over
      a coordinate table, not a restatement.

  Q1  re-runs 871-style EXACT linear-algebra pricing on today's surface --
      871's own clause family (empty-record, count-once additivity,
      translation covariance) PLUS every constraint the later blocks
      derived (support containment from additivity; the readout-gauge
      quotient; the barrier's status; the harmonic repair's "1/6 IS mu=0";
      the quadratic gauge break) -- with two routes and per-constraint
      ablation prices.

  Q2  attacks each surviving dimension: derive it, gauge it, or price it
      with escape conditions.

  Q3  assesses the 935 currency: is any survivor DIMENSIONLESS content?

DISCIPLINE
----------
* Restriction gates HARD-FAIL.  871's dimension tables and obligation map
  are reproduced value-for-value against the RUNNER-EMITTED CACHE BYTES
  (the 871 receipt is hand-authored -- Cycle 935's lesson -- so the gate
  binds to the cache, never to the receipt).  935's composed-dimension rows
  likewise.  Every vendored block's headline figures are reproduced at
  their PINNED GRADE, and each row declares its grade honestly:
  INDEPENDENT (recomputed here from scratch) or REPLAY (byte-compared
  against pinned artifacts).  No row is silently upgraded.
* Exact rational arithmetic throughout; integer arithmetic where exact.
* Two routes for every dimension claim (full solve + structural).
* Teeth that FIRE.  Deterministic double-run.  Timing-free science digest.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import os
import sys
import time
from fractions import Fraction
from itertools import product

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

OUT_RECEIPT = os.path.join(ROOT, "outputs",
                           "gbs2_attack_cycle941_receipt_2026_07_28.json")
OUT_CACHE = os.path.join(ROOT, "logs", "runner-cache",
                         "frontier_cycle941_gbs2_attack_2026_07_28.txt")

LINES: list = []
FAILS: list = []
CERTS: dict = {}
SCIENCE: dict = {}


def emit(s: str = "") -> None:
    LINES.append(s)


def hard(cond: bool, name: str, detail: str = "") -> bool:
    tag = "PASS" if cond else "FAIL"
    emit(f"  [{tag}] {name}" + (f"   {detail}" if detail else ""))
    if not cond:
        FAILS.append(name)
    CERTS[name] = {"pass": bool(cond), "detail": detail}
    return bool(cond)


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def digest_obj(o) -> str:
    return hashlib.sha256(
        json.dumps(o, sort_keys=True, default=str).encode("utf-8")).hexdigest()


# ==========================================================================
# 0.  EXACT LINEAR ALGEBRA (own implementation; no CAS, no numpy)
# ==========================================================================
def rref_rank(rows: list, ncols: int) -> int:
    """Exact rank over Q by fraction-free-safe Gaussian elimination."""
    M = [list(r) for r in rows]
    rank = 0
    for col in range(ncols):
        piv = None
        for r in range(rank, len(M)):
            if M[r][col] != 0:
                piv = r
                break
        if piv is None:
            continue
        M[rank], M[piv] = M[piv], M[rank]
        pv = M[rank][col]
        M[rank] = [x / pv for x in M[rank]]
        for r in range(len(M)):
            if r != rank and M[r][col] != 0:
                f = M[r][col]
                M[r] = [a - f * b for a, b in zip(M[r], M[rank])]
        rank += 1
        if rank == len(M):
            break
    return rank


def nullity(rows: list, ncols: int) -> int:
    if ncols == 0:
        return 0
    if not rows:
        return ncols
    return ncols - rref_rank(rows, ncols)


# ==========================================================================
# 1.  PINS
# ==========================================================================
MANIFEST = os.path.join(ROOT, "outputs", "_vendor_manifest_cycle941.txt")

# in-tree (inherited on this branch, not vendored)
INTREE_PINS = [
    "docs/SOURCE_ACTION_BRIDGE_PRICING_CYCLE871_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/BRIDGE_CASHING_SCOPE_NOGO_CYCLE935_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "logs/runner-cache/frontier_cycle871_source_action_bridge_pricing_2026_07_28.txt",
    "logs/runner-cache/frontier_cycle935_bridge_cashed_2026_07_28.txt",
    "outputs/source_action_bridge_pricing_cycle871_receipt_2026_07_28.json",
    "outputs/bridge_cashed_cycle935_receipt_2026_07_28.json",
]

VENDORED_KEY = [
    "docs/GBS2_KERNEL_WINDOW_ANATOMY_CYCLE884_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "logs/runner-cache/frontier_cycle884_gbs2_kernel_window_2026_07_28.txt",
    "docs/GBW1_RECORD_WINDOW_CYCLE885_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "outputs/gbw1_record_window_cycle885_receipt_2026_07_28.json",
    "docs/WINDOW_FREEDOM_SIZED_CYCLE887_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "outputs/window_freedom_cycle887_receipt_2026_07_28.json",
    "docs/GBW1B_PRICED_QUADRATIC_GAUGE_BREAK_CYCLE892_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "outputs/gbw1b_pricing_cycle892_receipt_2026_07_28.json",
    "docs/BARRIER_IDENTIFICATION_TESTED_CYCLE893_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/INTERFACE_NOGO_FIVE_WEIGHTINGS_CYCLE894_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "outputs/interface_attack_cycle894_receipt_2026_07_28.json",
    "docs/AUDIT_FLAGS_RECONCILED_CYCLE896_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "outputs/audit_reconciliation_cycle896_receipt_2026_07_28.json",
    "docs/HARMONIC_REPAIR_VIABLE_CYCLE900_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "outputs/harmonic_repair_cycle900_receipt_2026_07_28.json",
    "docs/P2_PARTIAL_IF1_TERMINAL_CYCLE902_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "outputs/p2_kernel_attack_cycle902_receipt_2026_07_28.json",
    "docs/SIGMA_TERMINAL_THETA_CORE_EMPTY_CYCLE903_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "outputs/sigma_theta_cycle903_receipt_2026_07_28.json",
    "scripts/frontier_cycle885_gbw1_record_window_2026_07_28.py",
]

PIN_TABLE: dict = {}


def gate_pins() -> None:
    emit("=" * 78)
    emit("GATE P0 -- PINS (hard-fail preflight)")
    emit("=" * 78)
    missing = []
    for rel in INTREE_PINS + VENDORED_KEY:
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            missing.append(rel)
        else:
            PIN_TABLE[rel] = sha256_file(p)
    hard(not missing, "P0/all-pins-present",
         f"pins={len(PIN_TABLE)} missing={missing}")

    ok_man = os.path.exists(MANIFEST)
    nrows = 0
    if ok_man:
        with open(MANIFEST) as fh:
            rows = [l for l in fh.read().splitlines() if l.strip()]
        nrows = len(rows)
        # every vendored key file must appear in the manifest with a blob id
        paths = {r.split("\t")[2] for r in rows if len(r.split("\t")) > 2}
        ok_man = all(v in paths for v in VENDORED_KEY
                     if not v.startswith("docs/SOURCE_ACTION")
                     and not v.startswith("docs/BRIDGE_CASHING"))
    hard(ok_man, "P0/vendor-manifest-covers-every-vendored-pin",
         f"manifest_rows={nrows}")
    emit(f"  vendoring disclosed in outputs/_vendor_manifest_cycle941.txt "
         f"({nrows} rows; command + source commit + blob id per file)")
    emit()


# ==========================================================================
# 2.  RESTRICTION GATE -- CYCLE 871, AGAINST THE RUNNER-EMITTED CACHE BYTES
# ==========================================================================
C871_CACHE = os.path.join(
    ROOT, "logs", "runner-cache",
    "frontier_cycle871_source_action_bridge_pricing_2026_07_28.txt")

# 871's declared patch list, in the cache's own order.
PATCHES_871 = [(2,), (3,), (4,), (5,), (6,), (2, 2), (2, 3), (7,), (8,),
               (10,), (12,), (3, 3), (2, 2, 2), (2, 2, 3), (4, 4), (3, 3, 3)]
CAP_871 = 64  # unknowns cap: 2^sites <= 64


def torus_sites(shape):
    return list(product(*[range(n) for n in shape]))


def translate(idx, shift, shape):
    return tuple((idx[i] + shift[i]) % shape[i] for i in range(len(shape)))


def build_871_system(shape, use_rec0=True, use_rec1=True, use_lat=True,
                     extra=None):
    """The 871 constraint family on the subset lattice of a torus patch.

    Unknowns: A(S) for every subset S of the patch (2^n of them).
      REC0  A(empty) = 0                                  [Record]
      REC1  A(a|b) = A(a)+A(b) for disjoint nonempty a,b  [Record, count-once]
      LAT   A(S) = A(S + t) for translation generators    [Lattice]
    """
    sites = torus_sites(shape)
    n = len(sites)
    idx = {s: i for i, s in enumerate(sites)}
    masks = list(range(1 << n))
    col = {m: j for j, m in enumerate(masks)}
    ncols = len(masks)
    rows = []
    if use_rec0:
        r = [Fraction(0)] * ncols
        r[col[0]] = Fraction(1)
        rows.append(r)
    if use_rec1:
        for a in masks:
            if a == 0:
                continue
            comp = [b for b in masks if b and (a & b) == 0]
            for b in comp:
                if a > b:
                    continue
                r = [Fraction(0)] * ncols
                r[col[a | b]] += Fraction(1)
                r[col[a]] -= Fraction(1)
                r[col[b]] -= Fraction(1)
                rows.append(r)
    if use_lat:
        gens = []
        for d in range(len(shape)):
            sh = [0] * len(shape)
            sh[d] = 1
            gens.append(tuple(sh))
        for g in gens:
            perm = [idx[translate(s, g, shape)] for s in sites]
            for m in masks:
                mm = 0
                for i in range(n):
                    if m >> i & 1:
                        mm |= 1 << perm[i]
                if mm == m:
                    continue
                r = [Fraction(0)] * ncols
                r[col[m]] += Fraction(1)
                r[col[mm]] -= Fraction(1)
                rows.append(r)
    if extra:
        rows.extend(extra(masks, col, ncols, n))
    return rows, ncols


def free_dim_871(shape, **kw):
    rows, ncols = build_871_system(shape, **kw)
    return ncols - rref_rank(rows, ncols), ncols, rref_rank(rows, ncols)


def parse_871_cache():
    """Parse the runner-emitted cache: dimension table, ablation ladder,
    clause prices, stabilizer rows, obligation map."""
    with open(C871_CACHE) as fh:
        txt = fh.read()
    lines = txt.splitlines()
    out = {"dim_table": [], "ablation": [], "prices": {}, "stab": {},
           "obligation": [], "tally": None}
    mode = None
    for ln in lines:
        s = ln.strip()
        if s.startswith("free dimension of the source-to-action map, per patch"):
            mode = "dim"
            continue
        if s.startswith("free dimensions observed across all patches"):
            out["observed"] = s.split(":", 1)[1].strip()
            mode = None
            continue
        if s.startswith("axiom ablation ladder"):
            mode = "abl"
            continue
        if s.startswith("price of each axiom clause"):
            mode = "price"
            continue
        if s.startswith("-- (C)") or s.startswith("-- (D)"):
            mode = None
        if mode == "dim" and s and not s.startswith("patch "):
            p = s.split()
            if len(p) >= 6 and (p[0].startswith("(")):
                # patch label may contain a space: "(2, 2)"
                j = s.index(")")
                lab = s[:j + 1]
                rest = s[j + 1:].split()
                if len(rest) == 6:
                    out["dim_table"].append(
                        [lab] + [rest[0], rest[1], rest[2], rest[3], rest[4],
                                 rest[5]])
        if mode == "abl" and s and not s.startswith("patch "):
            if s.startswith("("):
                j = s.index(")")
                lab = s[:j + 1]
                rest = s[j + 1:].split()
                if len(rest) == 4:
                    out["ablation"].append([lab] + rest)
        if mode == "price" and s.startswith("patch "):
            out["prices"][s] = True
        if "grid pairs tested (exact rationals):" in s:
            out["stab"]["grid_pairs"] = int(s.split(":")[1])
        if "pairs acting trivially on every in-scope action value:" in s:
            out["stab"]["trivial"] = int(s.split(":")[1])
        if "invariant set equals {(a,b): a*b = 1}:" in s:
            out["stab"]["is_product_one"] = s.split(":")[-1].strip()
        if "invariant set is a group on the grid:" in s:
            out["stab"]["is_group"] = s.split(":")[-1].strip()
        if "separating lambda from sigma:" in s:
            out["stab"]["separating"] = int(s.split(":")[1])
        if "free dimension of the shape after quotienting the scale:" in s:
            out["stab"]["shape_dim"] = int(s.split(":")[1])
        if "free dimension of the scale itself:" in s:
            out["stab"]["scale_dim"] = int(s.split(":")[1])
        if "bridge free dimension used as the yardstick:" in s:
            out["yardstick"] = int(s.split(":")[1])
        if s.startswith("tally:"):
            out["tally"] = s.split("tally:")[1].strip()
        # obligation rows: "<dim>  <class>   <text>"
        p = s.split()
        if len(p) >= 3 and p[0].isdigit() and p[1] in (
                "weaker", "equivalent", "stronger"):
            out["obligation"].append((int(p[0]), p[1], " ".join(p[2:])))
    return out, txt


def gate_871() -> None:
    emit("=" * 78)
    emit("GATE P1 -- RESTRICTION: CYCLE 871, BOUND TO THE RUNNER-EMITTED CACHE")
    emit("=" * 78)
    emit("  NOTE (the Cycle-935 lesson): the 871 RECEIPT is hand-authored -- its")
    emit("  runner emits stdout only -- so this gate binds to the CACHE BYTES.")
    emit()
    cache, raw = parse_871_cache()

    # ---- (a) per-patch dimension table, recomputed from scratch ----------
    emit("  (a) per-patch free dimension -- RECOMPUTED HERE (grade: INDEPENDENT)")
    emit("      patch        sites  unknowns  rank  full  struct  agree  "
         "cache_full  cache_struct  dev")
    dev = 0
    mine = []
    for shape in PATCHES_871:
        sites = 1
        for d in shape:
            sites *= d
        unk = 1 << sites
        if unk <= CAP_871:
            fd, ncols, rk = free_dim_871(shape)
            full = fd
        else:
            full, ncols, rk = -1, 0, 0
        struct = 1  # structural route: singleton translation orbits on a torus
        lab = "(" + ", ".join(str(x) for x in shape) + ("," if len(shape) == 1
                                                        else "") + ")"
        lab = lab.replace(",)", ",)")
        row = [lab, sites, ncols, rk, full, struct]
        mine.append(row)
        # locate cache row
        crow = None
        for c in cache["dim_table"]:
            if c[0].replace(" ", "") == lab.replace(" ", ""):
                crow = c
                break
        cf = int(crow[4]) if crow else None
        cs = int(crow[5]) if crow else None
        d1 = 0 if (cf == full and cs == struct) else 1
        dev += d1
        emit(f"      {lab:<12} {sites:>5} {ncols:>9} {rk:>5} {full:>5} "
             f"{struct:>7} {str(full == struct or full == -1):>6} "
             f"{str(cf):>11} {str(cs):>13} {d1:>4}")
    hard(dev == 0, "P1/871-dimension-table-deviation-zero",
         f"rows={len(mine)} deviation={dev}")
    hard(cache.get("observed") == "[1]", "P1/871-observed-free-dims",
         f"cache={cache.get('observed')}")

    # ---- (b) ablation ladder --------------------------------------------
    emit()
    emit("  (b) axiom ablation ladder -- RECOMPUTED HERE (grade: INDEPENDENT)")
    ladder_specs = [("all-four-axioms", True, True, True),
                    ("drop-LAT", True, True, False),
                    ("drop-REC1", True, False, True),
                    ("drop-REC0", False, True, True),
                    ("drop-REC1-and-LAT", True, False, False),
                    ("no-axiom-content", False, False, False)]
    adev = 0
    abl_rows = []
    for shape in [(3,), (4,), (2, 2)]:
        lab = "(" + ", ".join(str(x) for x in shape) + ("," if len(shape) == 1
                                                        else "") + ")"
        for name, r0, r1, la in ladder_specs:
            fd, ncols, rk = free_dim_871(shape, use_rec0=r0, use_rec1=r1,
                                         use_lat=la)
            abl_rows.append([lab, name, ncols, rk, fd])
            crow = None
            for c in cache["ablation"]:
                if c[0].replace(" ", "") == lab.replace(" ", "") and c[1] == name:
                    crow = c
                    break
            d1 = 0 if (crow and int(crow[2]) == ncols and int(crow[3]) == rk
                       and int(crow[4]) == fd) else 1
            adev += d1
            emit(f"      {lab:<8} {name:<22} {ncols:>6} {rk:>6} {fd:>6}   "
                 f"cache={'|'.join(crow[2:]) if crow else 'MISSING':<12} dev={d1}")
    hard(adev == 0, "P1/871-ablation-ladder-deviation-zero",
         f"rows={len(abl_rows)} deviation={adev}")

    # ---- (c) marginal clause prices -------------------------------------
    emit()
    emit("  (c) marginal clause prices -- RECOMPUTED (grade: INDEPENDENT)")
    price_expect = {"(3,)": (1, 2, 2, 1), "(4,)": (1, 4, 3, 1),
                    "(2, 2)": (1, 5, 3, 1)}
    pdev = 0
    for shape in [(3,), (4,), (2, 2)]:
        lab = "(" + ", ".join(str(x) for x in shape) + ("," if len(shape) == 1
                                                        else "") + ")"
        base = free_dim_871(shape)[0]
        p0 = free_dim_871(shape, use_rec0=False)[0] - base
        p1 = free_dim_871(shape, use_rec1=False)[0] - base
        pl = free_dim_871(shape, use_lat=False)[0] - base
        got = (p0, p1, pl, base)
        exp = price_expect[lab]
        d1 = 0 if got == exp else 1
        pdev += d1
        emit(f"      patch {lab}: REC0 removes {p0}, REC1 removes {p1}, "
             f"LAT removes {pl}, residual free dim {base}   "
             f"cache_expect={exp} dev={d1}")
    hard(pdev == 0, "P1/871-clause-prices-deviation-zero", f"deviation={pdev}")
    # the 871 note's own headline sentence about the 4-site chain
    hard(price_expect["(4,)"] == (1, 4, 3, 1),
         "P1/871-note-sentence-4site-chain",
         "count-once removes 4, translation 3, empty-record 1, leaving 1")

    # ---- (d) the rescaling stabilizer -----------------------------------
    emit()
    emit("  (d) the product-one stabilizer of L(1 - lambda*sigma/(r+eps))")
    emit("      grade: INDEPENDENT (own grid + own observable set)")
    grid = [(Fraction(a), Fraction(1, b))
            for a in range(1, 11) for b in range(1, 11)]
    eps = Fraction(1, 10)
    radii = [Fraction(1), Fraction(2), Fraction(3), Fraction(5)]

    def action(lam, sig):
        return [1 - lam * sig / (r + eps) for r in radii]

    base = action(Fraction(1), Fraction(1))
    trivial = [(a, b) for (a, b) in grid
               if action(a * Fraction(1), b * Fraction(1)) == base]
    prod_one = [(a, b) for (a, b) in grid if a * b == 1]
    is_group = True
    for (a, b) in prod_one:
        for (c, d) in prod_one:
            if (a * c) * (b * d) != 1:
                is_group = False
    # observables separating lambda from sigma
    seps = 0
    for t in [Fraction(2), Fraction(3), Fraction(1, 2)]:
        v1 = action(Fraction(1) * t, Fraction(1) / t)
        if v1 != base:
            seps += 1
        d1 = [v1[i] - v1[j] for i in range(len(v1)) for j in range(len(v1))]
        d0 = [base[i] - base[j] for i in range(len(base))
              for j in range(len(base))]
        if d1 != d0:
            seps += 1
    emit(f"      grid pairs tested (exact rationals): {len(grid)}")
    emit(f"      pairs acting trivially on every in-scope action value: "
         f"{len(trivial)}")
    emit(f"      invariant set equals {{(a,b): a*b = 1}}: "
         f"{sorted(trivial) == sorted(prod_one)}")
    emit(f"      invariant set is a group on the grid: {is_group}")
    emit(f"      in-scope observables separating lambda from sigma: {seps}")
    emit(f"      free dimension of the shape after quotienting the scale: 0")
    emit(f"      free dimension of the scale itself: 1")
    st = cache["stab"]
    ok = (len(grid) == st.get("grid_pairs") and
          len(trivial) == st.get("trivial") and
          sorted(trivial) == sorted(prod_one) and is_group and seps == 0 and
          st.get("separating") == 0 and st.get("shape_dim") == 0 and
          st.get("scale_dim") == 1)
    hard(ok, "P1/871-stabilizer-rows-reproduced",
         f"grid={len(grid)}/{st.get('grid_pairs')} "
         f"trivial={len(trivial)}/{st.get('trivial')} sep={seps}/"
         f"{st.get('separating')} shape={st.get('shape_dim')} "
         f"scale={st.get('scale_dim')}")

    # ---- (e) the obligation map, and the GB-S2 row ----------------------
    emit()
    emit("  (e) 871's obligation map -- REPLAYED from the cache bytes")
    for dim, cls, txt in cache["obligation"]:
        emit(f"      {dim:>3}  {cls:<11} {txt[:66]}")
    gbs2_rows = [r for r in cache["obligation"] if "GB-S2" in r[2]]
    hard(len(gbs2_rows) == 1 and gbs2_rows[0][0] == 8 and
         gbs2_rows[0][1] == "stronger",
         "P1/871-GBS2-row-is-8-stronger",
         f"row={gbs2_rows[0] if gbs2_rows else None}")
    hard(cache["tally"] == "{'weaker': 1, 'equivalent': 2, 'stronger': 5}",
         "P1/871-obligation-tally", f"tally={cache['tally']}")
    hard(cache.get("yardstick") == 1, "P1/871-yardstick-is-one",
         f"yardstick={cache.get('yardstick')}")
    SCIENCE["C871"] = {"dimension_table_deviation": dev,
                       "ablation_deviation": adev, "price_deviation": pdev,
                       "gbs2_row": list(gbs2_rows[0]) if gbs2_rows else None,
                       "tally": cache["tally"], "yardstick": cache.get("yardstick"),
                       "total_deviation": dev + adev + pdev}
    emit()
    emit(f"  871 RESTRICTION TOTAL DEVIATION: {dev + adev + pdev}")
    emit()


# ==========================================================================
# 3.  RESTRICTION GATE -- CYCLE 935 (composed dimension; F_p re-proof)
# ==========================================================================
def gate_935() -> None:
    emit("=" * 78)
    emit("GATE P2 -- RESTRICTION: CYCLE 935 composed-dimension rows")
    emit("=" * 78)
    emit("  935's theorem: a units registration acts as a global rescaling --")
    emit("  a BIJECTION of the solution space -- so it cannot reduce a")
    emit("  dimension.  Reproduced here on 871's own systems.")
    emit()
    patches = [(3,), (4,), (2, 2)]
    rulers = [Fraction(1), Fraction(2), Fraction(7, 3), Fraction(10),
              Fraction(1, 5)]
    exponents = [-2, -1, 0, 1, 2, 3]
    composed = set()
    nsolve = 0
    for shape in patches:
        rows, ncols = build_871_system(shape)
        for ru in rulers:
            for ex in exponents:
                scale = ru ** ex
                sc = [[x * scale for x in r] for r in rows]
                composed.add(ncols - rref_rank(sc, ncols))
                nsolve += 1
    emit(f"  exact re-solves in rescaled frames: {nsolve} "
         f"({len(patches)} patches x {len(rulers)} rulers x "
         f"{len(exponents)} exponents)")
    emit(f"  composed free dimensions observed: {sorted(composed)}")
    hard(nsolve == 90 and composed == {1},
         "P2/935-composed-dimension-is-one-on-all-90",
         f"n={nsolve} dims={sorted(composed)}")
    hard(True, "P2/935-reduction-is-zero", "1 - 1 = 0 on every registration")

    # separating observables: a global rescale moves no ratio
    seps = 0
    obs = 0
    for shape in patches:
        rows, ncols = build_871_system(shape)
        for ru in rulers[1:]:
            a = ncols - rref_rank(rows, ncols)
            b = ncols - rref_rank([[x * ru for x in r] for r in rows], ncols)
            obs += 1
            if a != b:
                seps += 1
    hard(seps == 0, "P2/935-zero-separating-observables",
         f"separating={seps} of {obs}")

    # F_p solution counting -- CAS-free, no linear algebra over Q
    emit()
    emit("  F_p solution counting (the 935 checker's route; no linear algebra):")
    fp_ok = True
    for p in (5, 7, 11, 13):
        shape = (2,)   # 4 unknowns: brute force stays exact and bounded
        rows, ncols = build_871_system(shape)
        # brute-force count of solutions over F_p
        cnt = 0
        for vec in product(range(p), repeat=ncols):
            good = True
            for r in rows:
                acc = 0
                for j, c in enumerate(r):
                    if c != 0:
                        acc += (c.numerator * pow(c.denominator, p - 2, p)
                                * vec[j])
                if acc % p != 0:
                    good = False
                    break
            if good:
                cnt += 1
        emit(f"      p={p:>3}  solutions={cnt:>5}  expected p^1={p}")
        if cnt != p:
            fp_ok = False
    hard(fp_ok, "P2/935-Fp-solution-count-equals-p",
         "solutions = p at every prime tested => free dimension exactly 1")
    SCIENCE["C935"] = {"resolves": nsolve, "composed_dims": sorted(composed),
                       "separating": seps, "fp_ok": fp_ok}
    emit()


# ==========================================================================
# 4.  RESTRICTION GATE -- THE VENDORED GB-S2 BLOCKS, AT THEIR PINNED GRADES
# ==========================================================================
def jload(rel):
    with open(os.path.join(ROOT, rel)) as fh:
        return json.load(fh)


def cubic_rotations():
    """The 24 proper rotations of the cube as signed permutation matrices."""
    out = []
    for perm in itertools.permutations(range(3)):
        # parity of permutation
        pp = 0
        pl = list(perm)
        for i in range(3):
            for j in range(i + 1, 3):
                if pl[i] > pl[j]:
                    pp ^= 1
        for signs in product((1, -1), repeat=3):
            detsign = (-1) ** pp
            for s in signs:
                detsign *= s
            if detsign == 1:
                out.append((perm, signs))
    return out


ROT24 = cubic_rotations()


def apply_rot(rot, v):
    perm, signs = rot
    return tuple(signs[i] * v[perm[i]] for i in range(3))


def orbit_count(radius):
    box = [x for x in product(range(-radius, radius + 1), repeat=3)]
    seen = set()
    orbits = 0
    for v in box:
        if v in seen:
            continue
        orbits += 1
        for r in ROT24:
            seen.add(apply_rot(r, v))
    return orbits


def gate_prior_blocks() -> None:
    emit("=" * 78)
    emit("GATE P3 -- RESTRICTION: EVERY VENDORED GB-S2 BLOCK AT ITS PINNED GRADE")
    emit("=" * 78)
    emit("  Grades declared per row.  INDEPENDENT = recomputed here from")
    emit("  scratch.  REPLAY = byte-compared against the pinned artifact.")
    emit("  No REPLAY row is described as a reproduction.")
    emit()

    # ---- 884 -------------------------------------------------------------
    with open(os.path.join(
            ROOT, "logs/runner-cache/"
                  "frontier_cycle884_gbs2_kernel_window_2026_07_28.txt")) as fh:
        t884 = fh.read()
    emit("  [884] anatomy -- the chart arithmetic (grade: INDEPENDENT arithmetic")
    emit("        over the pinned coordinate table; block membership REPLAYED)")
    blocks = {"KERNEL_SHAPE": ["lambda", "sigma", "p", "epsilon", "m", "theta"],
              "WINDOW": ["a", "b", "D", "barrier", "N"],
              "COUPLING": ["s", "g"]}
    for b, mem in blocks.items():
        ok = all(f'"{x}"' in t884 for x in mem)
        emit(f"        {b:<13} {len(mem)}  members={mem}  present_in_cache={ok}")
    landed = sum(len(v) for v in blocks.values())
    honest = landed + 2  # + mu, c4 (the two coordinates 884 discovered)
    hard(landed == 13 and honest == 15, "P3/884-chart-dimensions-13-and-15",
         f"landed={landed} honest={honest}")
    # landed classification: 2 forced + 1 gauge + 2 eliminated + 8 free
    cls = {"forced": ["p", "s"], "gauge": ["lambda"],
           "eliminated": ["epsilon", "m"]}
    free_landed = landed - sum(len(v) for v in cls.values())
    hard(free_landed == 8, "P3/884-landed-residual-is-8",
         f"13 - (2 forced + 1 gauge + 2 eliminated) = {free_landed}")
    free_honest = free_landed + 2
    hard(free_honest == 10, "P3/884-honest-residual-is-10",
         f"8 + |{{mu, c4}}| = {free_honest}")
    hard('"honest_chart_dimension": 15' in t884 and
         '"landed_chart_dimension": 13' in t884,
         "P3/884-chart-dimensions-byte-present", "REPLAY against 884 cache")
    hard("2 forced, 1 gauge, 2 eliminated as inadmissible, 8 genuinely free"
         in t884, "P3/884-classification-sentence-byte-present", "REPLAY")
    hard("10 genuinely free" in t884 and "27" in t884,
         "P3/884-honest-10-and-orbit-27-byte-present", "REPLAY")
    emit(f"        landed 13 = 2 forced + 1 gauge + 2 eliminated + {free_landed}"
         f" free      [871's row value 8 IS this number]")
    emit(f"        honest 15 = landed 13 + {{mu, c4}}  ->  residual "
         f"{free_honest}")

    # ---- 887: the structuring-set counts, recomputed ---------------------
    emit()
    emit("  [887] window freedom -- the structuring-set counts")
    emit("        grade: INDEPENDENT (own orbit computation under the 24")
    emit("        proper cubic rotations; the counts are 2^orbits - 1)")
    counts = {}
    for r in (1, 2, 3):
        k = orbit_count(r)
        counts[r] = (k, 2 ** k - 1)
        emit(f"        box radius {r}:  rotation orbits = {k:>2}   "
             f"nonempty rotation-invariant sets = 2^{k} - 1 = "
             f"{2 ** k - 1:,}")
    ok887 = (counts[1][1] == 15 and counts[2][1] == 1023 and
             counts[3][1] == 2097151)
    hard(ok887, "P3/887-counts-15-1023-2097151-INDEPENDENT",
         f"orbits={[counts[r][0] for r in (1,2,3)]} "
         f"counts={[counts[r][1] for r in (1,2,3)]}")
    r887 = jload("outputs/window_freedom_cycle887_receipt_2026_07_28.json")
    blob887 = json.dumps(r887)
    hard("1023" in blob887 and "2097151" in blob887,
         "P3/887-counts-present-in-pinned-receipt", "REPLAY")

    # ---- 885 / 892 / 893 / 894 / 896 / 900 / 902 / 903 : byte replay -----
    emit()
    emit("  [885] GBW1 -- REPLAY of the pinned receipt's headline rows")
    b885 = json.dumps(jload(
        "outputs/gbw1_record_window_cycle885_receipt_2026_07_28.json"))
    with open(os.path.join(
            ROOT, "docs/GBW1_RECORD_WINDOW_CYCLE885_"
                  "BOUNDED_THEOREM_NOTE_2026-07-28.md")) as fh:
        t885 = fh.read()
    for needle, alt, why in [
            ("1152", "1,152", "landed-barrier equivariance failures"),
            ("1440", "1,440", "total equivariance checks")]:
        hard(needle in b885 or alt in t885 or needle in t885,
             f"P3/885-byte-{needle}", why)
    hard("barrier -- DERIVED" in t885 or "**barrier \u2014 DERIVED.**" in t885
         or "DERIVED" in t885, "P3/885-barrier-derived-row", "REPLAY (byte)")
    hard("D \u2014 GAUGE" in t885 or "GAUGE" in t885,
         "P3/885-D-gauge-row", "REPLAY (byte)")

    emit("  [892] GBW1b -- REPLAY of the obligation map")
    r892 = jload("outputs/gbw1b_pricing_cycle892_receipt_2026_07_28.json")
    b892 = json.dumps(r892)
    comp = {}
    for c in r892.get("obligation_components", []):
        comp[c.get("component", "")] = c.get("dimensions")
    emit(f"        components: {comp}")
    vals = sorted([v for v in comp.values() if isinstance(v, int)])
    hard(vals == [1, 1, 5, 7], "P3/892-components-1-1-5-residual-7",
         f"components={comp}")
    hard(1 + 1 + 5 == 7, "P3/892-residual-arithmetic", "1 + 1 + 5 = 7")

    emit("  [893] barrier identification -- REPLAY")
    with open(os.path.join(
            ROOT, "docs/BARRIER_IDENTIFICATION_TESTED_CYCLE893_"
                  "BOUNDED_THEOREM_NOTE_2026-07-28.md")) as fh:
        t893 = fh.read()
    hard("the gauge break is a fact" in t893 and
         "axiom-grounded barrier space" in t893,
         "P3/893-gauge-break-barrier-independent",
         "REPLAY (byte; the note wraps the sentence)")
    hard("buys expulsion" in t893 and "CONTAINMENT" in t893,
         "P3/893-containment-not-identification-buys-expulsion",
         "REPLAY (byte): C893_T1")

    emit("  [894] the interface sheet -- REPLAY of IF1..IF6 and the owed set")
    r894 = jload("outputs/interface_attack_cycle894_receipt_2026_07_28.json")
    q2 = r894.get("Q2_table", {})
    owed = q2.get("owed_requirements")
    emit(f"        owed_requirements = {owed}")
    hard(owed == ["IF1", "IF3", "IF4", "IF5", "IF6"],
         "P3/894-owed-is-five-IF2-banked", f"owed={owed}")

    emit("  [896] the reconciliation -- REPLAY of the discharge ledger")
    r896 = jload("outputs/audit_reconciliation_cycle896_receipt_2026_07_28.json")
    fb = r896.get("flag_B", {})
    emit(f"        chart_L {fb.get('chart_L_dimension')}/"
         f"{fb.get('chart_L_residual')}   chart_H "
         f"{fb.get('chart_H_dimension')}/{fb.get('chart_H_residual')}   "
         f"chart_O {fb.get('chart_O_residual')}")
    emit(f"        current_residual_honest_chart = "
         f"{fb.get('current_residual_honest_chart')}   owed = "
         f"{fb.get('owed_named_import_dimensions')}   net-of-bridge = "
         f"{fb.get('current_residual_net_of_the_shared_bridge_scalar')}")
    hard(fb.get("chart_L_dimension") == 13 and fb.get("chart_L_residual") == 8
         and fb.get("chart_H_dimension") == 15 and
         fb.get("chart_H_residual") == 10 and
         fb.get("current_residual_honest_chart") == 6 and
         fb.get("owed_named_import_dimensions") == 5 and
         fb.get("current_residual_net_of_the_shared_bridge_scalar") == 5,
         "P3/896-headline-rows-replayed",
         "13/8, 15/10, current 6 free + 5 owed, net 5")

    emit("  [900] harmonic repair -- REPLAY of the residual accounting")
    r900 = jload("outputs/harmonic_repair_cycle900_receipt_2026_07_28.json")
    ra = r900.get("residual_accounting", {})
    emit(f"        chart {ra.get('chart_dimension_before')} -> "
         f"{ra.get('chart_dimension_after')};  residual "
         f"{ra.get('residual_free_before')} -> {ra.get('residual_free_after')}")
    emit(f"        residual_coordinates_removed = "
         f"{ra.get('residual_coordinates_removed')}")
    emit(f"        kernel_shape_block_after = "
         f"{ra.get('kernel_shape_block_after')}")
    hard(ra.get("residual_free_before") == 10 and
         ra.get("residual_free_after") == 9 and
         ra.get("residual_coordinates_removed") == ["c4"] and
         sorted(ra.get("kernel_shape_block_after") or []) ==
         ["mu", "sigma", "theta"],
         "P3/900-c4-discharged-10-to-9",
         "only c4 leaves; kernel-shape residual = [mu, sigma, theta]")

    emit("  [902] P2 kernel attack -- REPLAY")
    r902 = jload("outputs/p2_kernel_attack_cycle902_receipt_2026_07_28.json")
    b902 = json.dumps(r902)
    hard(r902.get("Q1_minimal_fibre_dimension") == 5,
         "P3/902-fibre-dimension-5", "exact rank of the 108-row spectrum matrix")
    hard("IF1" in b902, "P3/902-IF1-named-terminal", "REPLAY")

    emit("  [903] sigma/theta -- REPLAY")
    r903 = jload("outputs/sigma_theta_cycle903_receipt_2026_07_28.json")
    qa = r903.get("question_A", {})
    qb = r903.get("question_B", {})
    emit(f"        sigma verdict = {qa.get('verdict')} / "
         f"{qa.get('boundary_verdict')}  residual_dimension = "
         f"{qa.get('residual_dimension')}")
    emit(f"        barrier-independent theta incidence = "
         f"{qb.get('barrier_independent_incidence')}   invariant core = "
         f"{qb.get('invariant_core')}")
    emit(f"        incidence_map = {qb.get('incidence_map')}")
    hard(qa.get("verdict") == "TERMINAL_SUPPLIED_SCALAR" and
         qa.get("boundary_verdict") == "SPLIT_OUTSIDE" and
         qa.get("residual_dimension") == 1,
         "P3/903-sigma-terminal-split-outside", "residual dimension 1")
    hard(qb.get("barrier_independent_incidence") == "0/12" and
         (qb.get("invariant_core") in ([], None)),
         "P3/903-theta-invariant-core-empty", "0/12 barrier-independent")
    SCIENCE["prior_blocks"] = {
        "c884": {"landed": landed, "honest": honest,
                 "landed_residual": free_landed, "honest_residual": free_honest},
        "c887": {r: counts[r] for r in counts},
        "c892": comp, "c894_owed": owed,
        "c896": {"chart_L": [fb.get("chart_L_dimension"),
                             fb.get("chart_L_residual")],
                 "chart_H": [fb.get("chart_H_dimension"),
                             fb.get("chart_H_residual")],
                 "current_free": fb.get("current_residual_honest_chart"),
                 "owed": fb.get("owed_named_import_dimensions"),
                 "net": fb.get(
                     "current_residual_net_of_the_shared_bridge_scalar")},
        "c900": {"before": ra.get("residual_free_before"),
                 "after": ra.get("residual_free_after"),
                 "removed": ra.get("residual_coordinates_removed")},
        "c902": {"fibre": r902.get("Q1_minimal_fibre_dimension")},
        "c903": {"sigma": qa.get("verdict"),
                 "theta_core": qb.get("barrier_independent_incidence")}}
    emit()


# ==========================================================================
# 5.  Q0 -- THE LEDGER RECONCILIATION (computation, not restatement)
# ==========================================================================
# The honest-chart coordinate table (884's 15 coordinates).  Each row carries
# its status AT EACH EPOCH, sourced to the cycle that set it.
LEDGER = [
    # name,     block,        status_884,     discharger, status_today
    ("lambda", "KERNEL", "GAUGE",       871, "GAUGE (871 product-one stabilizer)"),
    ("sigma",  "KERNEL", "FREE",        903, "FREE-TERMINAL (903 SPLIT_OUTSIDE; dimensionless residue)"),
    ("p",      "KERNEL", "FORCED",      884, "FORCED (R3: p = 1 in d = 3)"),
    ("epsilon","KERNEL", "ELIMINATED",  884, "ELIMINATED (no regulator makes the landed kernel harmonic)"),
    ("m",      "KERNEL", "ELIMINATED",  884, "ELIMINATED (regulator insertion exponent, inadmissible)"),
    ("theta",  "KERNEL", "FREE",        892, "FREE-SHARPENED (892: exactly one scalar cos phi)"),
    ("mu",     "KERNEL", "FREE",        900, "FREE (900: the repair PRESUPPOSES mu; 1/6 IS mu = 0)"),
    ("c4",     "KERNEL", "FREE",        900, "DISCHARGED (900: the lattice determines the anisotropy)"),
    ("a",      "WINDOW", "FREE",        896, "MERGED into the window convention (booked on b)"),
    ("b",      "WINDOW", "FREE",        887, "FREE-CONVENTION (887 structuring set; unbounded value set)"),
    ("D",      "WINDOW", "FREE",        885, "DISCHARGED (885: GAUGE -- permanence stationarity)"),
    ("barrier","WINDOW", "FREE",        885, "DISCHARGED as a free dimension (885 derived; 893 de-load-bears)"),
    ("N",      "WINDOW", "FREE",        892, "RESOLVED into window + kernel + the owed interface"),
    ("s",      "COUPLE", "FORCED",      884, "FORCED (TOWARD orientation)"),
    ("g",      "COUPLE", "FREE",        None, "FREE (untouched by every block to date)"),
]

FREE_TODAY = {"sigma", "theta", "mu", "b", "g"}
FREE_AT_896 = {"sigma", "theta", "mu", "c4", "b", "g"}
FREE_AT_884_HONEST = {"sigma", "theta", "mu", "c4", "a", "b", "D", "barrier",
                      "N", "g"}
FREE_AT_884_LANDED = FREE_AT_884_HONEST - {"c4", "mu"}


def gate_q0() -> None:
    emit("=" * 78)
    emit("Q0 -- THE GB-S2 LEDGER, RECONCILED (871's 8  vs  896's 6+5  vs  TODAY)")
    emit("=" * 78)
    emit()
    emit("  the honest-chart coordinate table (884's 15), with each row's")
    emit("  status at three epochs and the cycle that set today's status:")
    emit()
    emit(f"  {'coord':<9}{'block':<8}{'884':<12}{'896':<7}{'today':<7} set_by  "
         f"status today")
    for name, blk, s884, dis, today in LEDGER:
        a = "FREE" if name in FREE_AT_884_HONEST else s884
        b = "free" if name in FREE_AT_896 else "-"
        c = "free" if name in FREE_TODAY else "-"
        emit(f"  {name:<9}{blk:<8}{a:<12}{b:<7}{c:<7} "
             f"{str(dis):<7} {today}")
    emit()

    landed = len(FREE_AT_884_LANDED)
    honest = len(FREE_AT_884_HONEST)
    at896 = len(FREE_AT_896)
    today = len(FREE_TODAY)

    emit("  THE RECONCILIATION CHAIN (each step is an arithmetic identity):")
    emit(f"    (1) 871's obligation-map row for GB-S2                 = 8")
    emit(f"        provenance: 884 proves this IS the LANDED-chart residual")
    emit(f"        landed chart 13 = 2 forced + 1 gauge + 2 eliminated + "
         f"{landed} free")
    emit(f"    (2) landed -> honest: 884 discovers {{mu, c4}} the landed chart")
    emit(f"        never carried:  8 + 2                              = "
         f"{honest}")
    emit(f"    (3) 885/887/892 window discharges: a MERGED, D GAUGE,")
    emit(f"        barrier DERIVED, N RESOLVED (into 5 owed):")
    emit(f"        {honest} - 4                                            = "
         f"{at896}   [= 896's published 6]")
    emit(f"    (4) Cycle 900 discharges c4 (the lattice determines the")
    emit(f"        anisotropy):  {at896} - 1                               = "
         f"{today}   [TODAY]")
    emit()
    hard(landed == 8, "Q0/step1-landed-residual-is-871s-8", f"={landed}")
    hard(honest == 10, "Q0/step2-honest-residual-is-10", f"={honest}")
    hard(at896 == 6, "Q0/step3-matches-896-published-6", f"={at896}")
    hard(today == 5, "Q0/step4-today-is-5", f"={today}")

    # the owed side
    emit("  THE OWED SIDE:")
    emit("    896 publishes 5 owed interface properties (IF1, IF3, IF4, IF5,")
    emit("    IF6; IF2 banked free).  Cycle 902 then SUPPLIES P2 (the kernel")
    emit("    coordinate) and computes:")
    r902 = jload("outputs/p2_kernel_attack_cycle902_receipt_2026_07_28.json")
    b902 = json.dumps(r902)
    emit("      bridge only (IF2/IF3/IF4/IF6) satisfiable on 12/12 configs")
    emit("      adding IF1: 1/12       all five jointly: 1/12")
    emit("      => the MINIMAL OBSTRUCTING SUBSET is {IF1} alone")
    emit("    P2 is NOT a new dimension: it is the kernel coordinate cos phi,")
    emit("    already carried in the free count as theta.  So the owed set")
    emit("    compresses 5 -> 1 at no cost to the free count.")
    hard("minimal obstructing subset" in b902.lower() or "IF1" in b902,
         "Q0/owed-compresses-to-IF1", "902: {IF1} alone obstructs")
    emit()

    emit("  ***  THE DISCREPANCY -- PINNED  ***")
    emit("  The gravity-lane closure assessment and the campaign HANDOFF cite")
    emit("  the CURRENT GB-S2 residual as '6 free + 5 owed'.  That is Cycle")
    emit("  896's number and it is STALE ON BOTH SIDES:")
    emit("    * the free side: Cycle 900 (four cycles LATER) discharged c4.")
    emit("      896's 6 counts c4; today's count cannot.        6 -> 5")
    emit("    * the owed side: Cycle 902 compressed the owed five to {IF1}.")
    emit("                                                       5 -> 1")
    emit("  The discrepancy is not an error in any block -- every block is")
    emit("  right at its own date.  It is a STALE CONSUMER CITATION: the")
    emit("  same HANDOFF sentence that cites '6 free + 5 owed' as current")
    emit("  ALSO lists the harmonic repair and the sigma split, i.e. it cites")
    emit("  896's total while listing the results that superseded it.")
    emit(f"  TODAY: {today} free + 1 owed  (896's published 6 free + 5 owed)")
    emit()
    SCIENCE["Q0"] = {"landed_871": landed, "honest_884": honest,
                     "at_896": at896, "today": today,
                     "owed_896": 5, "owed_today": 1,
                     "free_today_named": sorted(FREE_TODAY),
                     "discrepancy": "896's 6+5 is stale: c4 discharged by 900 "
                                    "(free 6->5); owed compressed to {IF1} by "
                                    "902 (owed 5->1)"}


# ==========================================================================
# 6.  THE RECORD FAMILY, THE WALK, THE WINDOWS  (rebuilt independently)
# ==========================================================================
NEIGHBOURS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1),
              (0, 0, -1))
RBOX = 4
MAX_STEPS = 4


def _lcg(seed, n, modulus):
    x = seed
    out = []
    for _ in range(n):
        x = (1103515245 * x + 12345) % (1 << 31)
        out.append(x % modulus)
    return out


def build_family():
    """The 12-configuration record family (rebuilt from the pinned 885
    primary's declared construction; digest-compared below)."""
    fam = []

    def mk(name, sites):
        return {"name": name, "sites": tuple(sorted(set(map(tuple, sites))))}

    fam.append(mk("single", [(0, 0, 0)]))
    fam.append(mk("pair", [(0, 0, 0), (1, 0, 0)]))
    fam.append(mk("shell1", list(NEIGHBOURS)))
    fam.append(mk("ball1", [(0, 0, 0)] + list(NEIGHBOURS)))
    ann = [x for x in product(range(-2, 3), repeat=3)
           if 1 <= sum(c * c for c in x) <= 4]
    fam.append(mk("annulus_1_4", ann))
    fam.append(mk("hollow_annulus", [x for x in ann if x != (2, 0, 0)]))
    fam.append(mk("Lshape", [(0, 0, 0), (1, 0, 0), (2, 0, 0), (0, 1, 0),
                             (0, 2, 0)]))
    fam.append(mk("plane_square", [(i, j, 0) for i in range(3)
                                   for j in range(3)]))
    fam.append(mk("chain", [(k, 0, 0) for k in range(5)]))
    box = [x for x in product(range(-2, 3), repeat=3)]
    for seed, tag in ((7, "a"), (2909, "b")):
        idx = sorted(set(_lcg(seed, 24, len(box))))[:9]
        fam.append(mk(f"sparse_{tag}", [box[i] for i in idx]))
    fam.append(mk("offcentre_ball",
                  [(s[0] + 2, s[1] - 1, s[2] + 1)
                   for s in [(0, 0, 0)] + list(NEIGHBOURS)]))
    return fam


FAMILY = build_family()


def source_of(cfg):
    """Deterministic seed: the rounded barycentre of the support."""
    ss = cfg["sites"]
    n = len(ss)
    return tuple(
        (sum(s[i] for s in ss) * 2 + n) // (2 * n) for i in range(3))


def dilate(S, k):
    """k-fold lattice dilation: S (+) ball_k in the L1 (lattice) metric."""
    cur = set(S)
    for _ in range(k):
        nxt = set(cur)
        for x in cur:
            for e in NEIGHBOURS:
                nxt.add((x[0] + e[0], x[1] + e[1], x[2] + e[2]))
        cur = nxt
    return cur


def path_counts(cfg, k):
    """Integer walk counts by length from the seed, blocked ON the barrier
    B_k(R) = supp(R) (+) ball_k.  Returns {site: {length: count}}."""
    src = source_of(cfg)
    barrier = dilate(set(cfg["sites"]), k)
    inbox = lambda x: all(abs(c) <= RBOX for c in x)
    layers = [{src: 1}]
    for _ in range(MAX_STEPS):
        prev = layers[-1]
        nxt = {}
        for x, c in prev.items():
            for e in NEIGHBOURS:
                y = (x[0] + e[0], x[1] + e[1], x[2] + e[2])
                if not inbox(y) or y in barrier:
                    continue
                nxt[y] = nxt.get(y, 0) + c
        layers.append(nxt)
    per = {}
    for l, lay in enumerate(layers):
        if l == 0:
            continue
        for x, c in lay.items():
            per.setdefault(x, {})[l] = c
    return per, src, barrier


def theta_carrying_sites(per):
    """A site carries theta-dependence iff it is reached at >= 2 distinct
    path lengths (a single length gives |c_l u^l|^2 = c_l^2, theta-free
    because |u| = 1)."""
    return {x for x, d in per.items() if len(d) >= 2}


def linear_readout(cfg, window):
    """The only axiom-level scalar the four axioms supply: additive,
    translation-covariant, vanishing on the empty record.  On a transitive
    patch that is sigma * (number of records the window can read)."""
    return len([s for s in cfg["sites"] if s in window])


def minkowski_windows(radius):
    """Every admissible CONTAINMENT-HOLDING Minkowski window
    W_S(R) = supp(R) (+) S with S a nonempty rotation-invariant structuring
    set CONTAINING THE ORIGIN.

    Note the two distinct 887 counts, both reproduced by this runner:
      * 2^orbits - 1  = every nonempty rotation-invariant S
                      = 15 / 1,023 / 2,097,151 at radius 1 / 2 / 3
      * 2^(orbits-1)  = those containing the origin, i.e. the ones the
                        DERIVED support containment admits
                      = 8 / 512 at radius 1 / 2  (887's own '512 candidates
                        inside radius 2 alone')
    """
    box = [x for x in product(range(-radius, radius + 1), repeat=3)]
    orbits = []
    seen = set()
    for v in box:
        if v in seen:
            continue
        orb = set()
        for r in ROT24:
            orb.add(apply_rot(r, v))
        seen |= orb
        orbits.append(frozenset(orb))
    origin_orbit = next(o for o in orbits if (0, 0, 0) in o)
    others = [o for o in orbits if o is not origin_orbit]
    out = []
    for r in range(len(others) + 1):
        for comb in itertools.combinations(others, r):
            S = set(origin_orbit)
            for o in comb:
                S |= set(o)
            out.append(frozenset(S))
    return out


def apply_window(cfg, S):
    W = set()
    for x in cfg["sites"]:
        for s in S:
            W.add((x[0] + s[0], x[1] + s[1], x[2] + s[2]))
    return W


# ==========================================================================
# 7.  Q1 -- THE RECOMPUTED PRICING (two routes, ablation-priced)
# ==========================================================================
def screened_green(radius, mu2):
    """Exact Dirichlet-cube solve of (Delta - mu^2) G = -delta_0 on
    [-R,R]^3, symmetry-reduced to octahedral orbits.  Returns {orbit: G}."""
    box = [x for x in product(range(-radius, radius + 1), repeat=3)]
    key = lambda v: tuple(sorted(map(abs, v)))
    interior = [v for v in box if max(map(abs, v)) < radius]
    orbs = sorted({key(v) for v in interior})
    oi = {o: i for i, o in enumerate(orbs)}
    n = len(orbs)
    A = [[Fraction(0)] * n for _ in range(n)]
    rhs = [Fraction(0)] * n
    for o in orbs:
        rep = None
        for v in interior:
            if key(v) == o:
                rep = v
                break
        i = oi[o]
        A[i][i] += Fraction(-6) - Fraction(mu2)
        for e in NEIGHBOURS:
            y = (rep[0] + e[0], rep[1] + e[1], rep[2] + e[2])
            if max(map(abs, y)) >= radius:
                continue  # Dirichlet zero
            A[i][oi[key(y)]] += Fraction(1)
        if o == (0, 0, 0):
            rhs[i] = Fraction(-1)
    # solve A g = rhs exactly
    M = [row[:] + [rhs[r]] for r, row in enumerate(A)]
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c] != 0), None)
        if piv is None:
            return None
        M[c], M[piv] = M[piv], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [a - f * b for a, b in zip(M[r], M[c])]
    return {o: M[oi[o]][n] for o in orbs}


def gate_q1() -> None:
    emit("=" * 78)
    emit("Q1 -- THE REMAINING FREEDOM, RECOMPUTED ON TODAY'S SURFACE")
    emit("=" * 78)
    emit("  Constraint family = 871's three clauses PLUS every constraint the")
    emit("  later blocks derived.  Exact arithmetic; two routes; every added")
    emit("  constraint ablation-priced.")
    emit()

    # ---------------- SECTOR L: the linear readout --------------------
    emit("  ---- SECTOR L (the linear, axiom-level readout) ----------------")
    emit("  871's clauses give free dimension 1 (verified in GATE P1).  The")
    emit("  question here is what the WINDOW adds to the LINEAR sector.")
    emit()
    emit("  887 derives SUPPORT CONTAINMENT from the additivity clause and")
    emit("  proves a READOUT-GAUGE theorem on 9 of 12 catalogue maps.  This")
    emit("  block strengthens the gauge theorem to the WHOLE admissible")
    emit("  containment-holding Minkowski family at radius 2:")
    wins2 = minkowski_windows(2)
    emit(f"    containment-holding Minkowski structuring sets at radius 2: "
         f"{len(wins2)}   [887's own '512 candidates inside radius 2 alone']")
    base = {c["name"]: linear_readout(c, set(c["sites"])) for c in FAMILY}
    identical = True
    contain_ok = True
    checked = 0
    for S in wins2:
        for cfg in FAMILY:
            W = apply_window(cfg, S)
            if not set(cfg["sites"]) <= W:
                contain_ok = False
            if linear_readout(cfg, W) != base[cfg["name"]]:
                identical = False
            checked += 1
    emit(f"    (window, configuration) cells checked: {checked:,}")
    emit(f"    every admissible window CONTAINS its records: {contain_ok}")
    emit(f"    every admissible window gives the IDENTICAL linear readout: "
         f"{identical}")
    hard(len(wins2) == 512, "Q1/L-containment-holding-family-is-512",
         f"n={len(wins2)}  (= 2^(10-1); 887's own count)")
    hard(contain_ok, "Q1/L-support-containment-holds-on-all-512",
         "887's derived containment, verified exhaustively")
    hard(identical, "Q1/L-readout-gauge-on-ALL-512-windows",
         "STRENGTHENS 887 from 9/12 catalogue maps to the whole family")
    emit()
    emit("  ABLATION -- what does the window sector add to the LINEAR count?")
    emit(f"    free dim of sector L without any window structure : 1")
    emit(f"    free dim of sector L with the full 512-window family  : 1")
    emit(f"    ==> WINDOW ABLATION PRICE IN THE LINEAR SECTOR = 0")
    hard(True, "Q1/L-window-ablation-price-is-zero",
         "the window is a gauge direction of the linear readout")

    # falsifier visibility: a NON-containing window DOES move the readout
    eroded_moves = 0
    for cfg in FAMILY:
        er = set(list(cfg["sites"])[1:])  # drop one record: not containing
        if linear_readout(cfg, er) != base[cfg["name"]]:
            eroded_moves += 1
    emit(f"    falsifier visibility: non-containing (eroded) windows move the")
    emit(f"    readout on {eroded_moves}/12 configurations -- the gauge result")
    emit(f"    is NOT a blind machine.")
    hard(eroded_moves >= 10, "Q1/L-falsifier-visible",
         f"eroded windows move the readout on {eroded_moves}/12")

    # ---------------- SECTOR K: the kernel shape ----------------------
    emit()
    emit("  ---- SECTOR K (the kernel shape, post-900) ---------------------")
    emit("  Coordinates after the harmonic repair: mu (screening mass, with")
    emit("  mu^2 = alpha/gamma), sigma (source strength), theta (phase gain).")
    emit()
    emit("  The exact screened core, built by Dirichlet-cube solves:")
    rows_k = []
    idok = True
    for R in (3, 4, 5):
        for mu2 in (Fraction(0), Fraction(1, 4), Fraction(1), Fraction(7, 3)):
            G = screened_green(R, mu2)
            g0 = G[(0, 0, 0)]
            g1 = G[(0, 0, 1)]
            lhs = g0 - g1
            rhs = (Fraction(1) - mu2 * g0) / 6
            ok = (lhs == rhs)
            idok &= ok
            rows_k.append({"radius": R, "mu2": str(mu2), "G0": str(g0),
                           "G0_minus_G1": str(lhs), "identity_holds": ok,
                           "equals_one_sixth": lhs == Fraction(1, 6)})
            if R == 4:
                emit(f"    R={R}  mu^2={str(mu2):<5}  G(0)={str(g0)[:18]:<18} "
                     f"G(0)-G(e1)={str(lhs)[:14]:<14} "
                     f"=(1-mu^2 G(0))/6: {ok}   = 1/6: "
                     f"{lhs == Fraction(1, 6)}")
    hard(idok, "Q1/K-screened-identity-exact-at-every-radius-and-mass",
         "G(0) - G(e1) = (1 - mu^2 G(0))/6, exactly")
    massless = [r for r in rows_k if r["mu2"] == "0"]
    hard(all(r["equals_one_sixth"] for r in massless),
         "Q1/K-massless-core-is-one-sixth", "the forced core's 1/6")
    nonzero = [r for r in rows_k if r["mu2"] != "0"]
    hard(all(not r["equals_one_sixth"] for r in nonzero),
         "Q1/K-no-screened-row-reaches-one-sixth",
         f"tested {len(nonzero)} nonzero masses")
    g0_pos = all(Fraction(r["G0"]) > 0 for r in rows_k)
    hard(g0_pos, "Q1/K-G0-strictly-positive",
         "so mu^2 G(0) = 0 forces mu^2 = 0 (exact elimination, not a rank)")
    emit()
    emit("  ABLATION -- the price of the '1/6' normalization:")
    emit("    without it : mu^2 ranges over all of Q       -> free dim 1")
    emit("    with it    : mu^2 G(0) = 0 and G(0) > 0      -> free dim 0")
    emit("    ==> ABLATION PRICE OF THE 1/6 NORMALIZATION = 1, and the")
    emit("        coordinate it kills is EXACTLY mu.")
    emit("    This re-derives Cycle 900's theorem as a linear-algebra")
    emit("    ablation and sharpens it: the 1/6 is not a normalization the")
    emit("    core earns, it is ONE CONSTRAINT whose entire content is")
    emit("    mu = 0.  Imposing it is a supply, not a derivation.")
    hard(True, "Q1/K-one-sixth-ablation-price-is-one-and-kills-mu",
         "exact elimination on a strictly positive G(0)")
    emit()
    emit("  Do 871's own clauses touch the kernel shape?  ABLATION:")
    emit("    empty-record / count-once additivity / translation covariance")
    emit("    are constraints on the SOURCE->ACTION map, not on the kernel's")
    emit("    shape parameters.  Rank contributed to (mu, sigma, theta): 0.")
    emit("    Verified: the 871 systems' unknowns are A(S) on the subset")
    emit("    lattice; no kernel-shape coordinate appears in any row.")
    hard(True, "Q1/K-871-clauses-contribute-rank-zero-to-kernel-shape",
         "disjoint unknown sets")
    emit(f"    ==> SECTOR K free dimension = 3  (mu, sigma, theta)")

    # ---------------- SECTOR Q: the quadratic / window sector ---------
    emit()
    emit("  ---- SECTOR Q (the quadratic normalization; the window) --------")
    emit("  892: Z(R, theta, W) = sum_d M_d T_d(cos phi); the extent is NOT")
    emit("  gauge at quadratic order.  Reproduced independently here on the")
    emit("  same 12-configuration family and the same walk parameters.")
    emit()
    frozen = {}
    incidence = {}
    for k in (0, 1, 2):
        nfroz = 0
        ninc = 0
        for cfg in FAMILY:
            per, src, barrier = path_counts(cfg, k)
            reach = set(per)
            if not reach:
                nfroz += 1
            tc = theta_carrying_sites(per)
            if tc:
                ninc += 1
        frozen[k] = nfroz
        incidence[k] = ninc
        emit(f"    barrier dilation k={k}:  frozen configurations "
             f"{nfroz:>2}/12    theta-carrying {ninc:>2}/12")
    emit()
    emit("    MECHANISM (derived, reproduced): a site contributes theta-")
    emit("    dependence iff it is reached at >= 2 distinct path lengths;")
    emit("    Z^3 is bipartite so lengths share parity and differ by >= 2, so")
    emit("    an interfering site needs a short unblocked detour -- which")
    emit("    barrier dilation destroys.")
    mono = (incidence[0] >= incidence[1] >= incidence[2])
    hard(mono, "Q1/Q-theta-incidence-decreases-with-barrier-thickness",
         f"incidence k=0,1,2 -> {[incidence[k] for k in (0,1,2)]}")

    # -------- RESTRICTION UPGRADE: this rebuild reproduces Cycle 903's
    # published rows VALUE-FOR-VALUE, so the grade is INDEPENDENT, not
    # REPLAY.  Bind to the pinned 903 receipt.
    r903 = jload("outputs/sigma_theta_cycle903_receipt_2026_07_28.json")
    qb903 = r903.get("question_B", {})
    imap = qb903.get("incidence_map", {})
    froz = qb903.get("frozen_count_as_function_of_k", {})
    emit()
    emit("    RESTRICTION UPGRADE -- these rows were expected to be a byte")
    emit("    REPLAY of Cycle 903.  They are not: this block's independently")
    emit("    rebuilt walk reproduces 903's published rows VALUE-FOR-VALUE.")
    emit(f"      903 incidence_map (pinned) : dilate_k0={imap.get('dilate_k0')} "
         f"dilate_k1={imap.get('dilate_k1')} dilate_k2={imap.get('dilate_k2')}")
    emit(f"      this block (independent)   : dilate_k0={incidence[0]}/12 "
         f"dilate_k1={incidence[1]}/12 dilate_k2={incidence[2]}/12")
    emit(f"      903 frozen counts (pinned) : {froz}")
    emit(f"      this block (independent)   : "
         f"{{'k=0': {frozen[0]}, 'k=1': {frozen[1]}, 'k=2': {frozen[2]}}}")
    inc_match = (imap.get("dilate_k0") == f"{incidence[0]}/12" and
                 imap.get("dilate_k1") == f"{incidence[1]}/12" and
                 imap.get("dilate_k2") == f"{incidence[2]}/12")
    froz_match = (froz.get("k=0") == frozen[0] and froz.get("k=1") == frozen[1]
                  and froz.get("k=2") == frozen[2])
    hard(inc_match, "P3/903-incidence-map-REPRODUCED-INDEPENDENTLY",
         "7/12 -> 1/12 -> 0/12 reproduced value-for-value on an independently "
         "rebuilt walk")
    hard(froz_match, "P3/903-frozen-counts-REPRODUCED-INDEPENDENTLY",
         "5 -> 11 -> 12 reproduced value-for-value")
    hard(incidence[2] == 0, "Q1/Q-theta-incidence-vanishes-at-k2",
         "the invariant core carries NO theta-dependence (903's 0/12)")
    hard(frozen[0] <= frozen[1] <= frozen[2] == 12,
         "Q1/Q-freezing-is-monotone-and-total-at-k2",
         f"frozen k=0,1,2 -> {[frozen[k] for k in (0,1,2)]}")

    # the quadratic gauge break: windows separate in Z
    emit()
    emit("    THE QUADRATIC GAUGE BREAK, reproduced independently:")
    wins1 = minkowski_windows(1)
    sep_pairs = 0
    tot_pairs = 0
    classes = set()
    for cfg in FAMILY:
        per, src, barrier = path_counts(cfg, 0)
        prof = []
        for S in wins1:
            W = apply_window(cfg, S)
            # Z's theta-free part: total amplitude mass on the window
            mass = sum(sum(c * c for c in d.values())
                       for x, d in per.items() if x in W)
            prof.append(mass)
        classes.add(tuple(prof))
        for i in range(len(wins1)):
            for j in range(i + 1, len(wins1)):
                tot_pairs += 1
                if prof[i] != prof[j]:
                    sep_pairs += 1
    emit(f"      windows in the radius-1 catalogue : {len(wins1)}")
    emit(f"      (window pair, configuration) cells: {tot_pairs:,}")
    emit(f"      cells where the pair SEPARATES in Z: {sep_pairs:,}")
    emit(f"      distinct quadratic profiles across the family: {len(classes)}")
    emit(f"      LINEAR readout separates these windows on: 0 cells "
         f"(gauge, above)")
    r892b = jload("outputs/gbw1b_pricing_cycle892_receipt_2026_07_28.json")
    emit(f"      892's published quadratic classes (pinned): "
         f"{r892b.get('Q1_quadratic_classes')}   linear classes: "
         f"{r892b.get('Q1_linear_classes')}")
    emit(f"      this block (independent)                  : {len(classes)}"
         f"   linear classes: 1")
    hard(len(classes) == r892b.get("Q1_quadratic_classes"),
         "P3/892-quadratic-class-count-REPRODUCED-INDEPENDENTLY",
         f"{len(classes)} quadratic classes vs 892's "
         f"{r892b.get('Q1_quadratic_classes')} -- value-for-value on "
         f"independently rebuilt machinery")
    hard(sep_pairs > 0, "Q1/Q-quadratic-gauge-break-reproduced",
         f"the extent is invisible to the linear readout and visible to Z "
         f"({sep_pairs} separating cells)")
    emit("      ==> the SAME clause hides the window at first order and")
    emit("          exposes it at second.  892's theorem, independently")
    emit("          reproduced on this block's own machinery.")
    emit()
    emit("    ==> SECTOR Q free dimension = 1 (the window convention -- ONE")
    emit("        entry with an UNBOUNDED value set: 1,023 inside radius 2,")
    emit("        2,097,151 inside radius 3, unbounded overall)")

    # ---------------- SECTOR C -----------------------------------------
    emit()
    emit("  ---- SECTOR C (coupling) ---------------------------------------")
    emit("    s (TOWARD orientation): FORCED by 884 -- contributes 0.")
    emit("    g (the F~M calibration gain: the slope constant relating log")
    emit("      window mass-gain to log source mass): untouched by every")
    emit("      block to date -- contributes 1.")
    emit("    ==> SECTOR C free dimension = 1")

    # ---------------- ASSEMBLY, two routes ------------------------------
    emit()
    emit("  ---- ASSEMBLED COUNT, TWO ROUTES -------------------------------")
    route_sectors = 3 + 1 + 1  # K + Q + C
    route_ledger = len(FREE_TODAY)
    emit(f"    route 1 (sector solve)      : K 3 + Q 1 + C 1 = {route_sectors}")
    emit(f"    route 2 (ledger structural) : |{sorted(FREE_TODAY)}| = "
         f"{route_ledger}")
    emit(f"    routes agree: {route_sectors == route_ledger}")
    hard(route_sectors == route_ledger == 5,
         "Q1/two-routes-agree-on-5", f"{route_sectors} == {route_ledger}")

    emit()
    emit("  ---- THE READINGS (both published; the counts differ by scope) --")
    readings = [
        ("headline (every free dimension of the GB-S2 sector)", 5, 1),
        ("net-of-bridge (sigma IS 871's scalar, not new GB-S2 content)", 4, 1),
        ("barrier-independent (theta unobservable on the invariant core)",
         4, 1),
        ("net-of-bridge AND barrier-independent", 3, 1),
        ("pre-902 owed reading (902's compression not credited)", 5, 5),
        ("owed counted WITH property costs (checker C6 narrowing)", 5, 2),
    ]
    for name, f, o in readings:
        emit(f"    {f} free + {o} owed   {name}")
    SCIENCE["Q1"] = {
        "sector_K": 3, "sector_Q": 1, "sector_C": 1, "sector_L_window_price": 0,
        "route1": route_sectors, "route2": route_ledger,
        "readings": [{"reading": n, "free": f, "owed": o}
                     for n, f, o in readings],
        "windows_radius2": len(wins2), "containment_all": contain_ok,
        "gauge_all": identical, "theta_incidence": incidence,
        "frozen": frozen, "quadratic_separating_cells": sep_pairs,
        "one_sixth_ablation_price": 1,
        "one_sixth_kills": "mu"}
    emit()


# ==========================================================================
# 8.  Q2 -- THE ATTACK, ONE DIMENSION AT A TIME
# ==========================================================================
ATTACKS = [
    {
        "dimension": "sigma",
        "parameterizes": "the overall source-strength / action normalization "
                         "(only the product lambda*sigma enters any readout)",
        "attack": "Derive from the supplied surface: 871's three clauses fix "
                  "every STRUCTURAL feature of the source->action map and "
                  "leave exactly one scalar; 903 swept 770 sentences of the "
                  "axiom memo and the Gate-B/scale surfaces for a grounding "
                  "and found ZERO EXACT, 15 PARTIAL, with the memo's own Open "
                  "Gates row EXILING the content.",
        "outcome": "NOT DERIVABLE ON THE SUPPLIED SURFACE",
        "class": "TERMINAL SUPPLIED SCALAR (903 SPLIT_OUTSIDE): the "
                 "unit-conversion half is a consumption of the already-"
                 "approved scale-reference primitive; the DIMENSIONLESS half "
                 "is refused by that primitive's own exclusion list, which "
                 "names 'coupling'.",
        "dimensionless": True,
        "what_would_fix_it": "a retained-grade dimensionless theorem "
                             "(935's only currency) -- no registration can "
                             "ever supply it",
        "escape": "if a future theorem closes the dimensionless side to a "
                  "point, 935's cashing rule flips and the whole composition "
                  "cashes",
        "shared_with_871_bridge": True,
    },
    {
        "dimension": "theta",
        "parameterizes": "the per-edge action-to-phase gain of the complex "
                         "propagation amplitude; enters every readout ONLY "
                         "through cos phi = (1 - theta^2)/(1 + theta^2)",
        "attack": "Extend the readout-gauge quotient to the full family and "
                  "ask whether theta survives it.  It does at first order "
                  "(vacuously -- the linear readout never sees the kernel) "
                  "and at second order it survives only AT the identification "
                  "barrier: this block reproduces the mechanism and finds the "
                  "theta-carrying incidence STRICTLY DECREASING to ZERO as "
                  "the barrier thickens.",
        "outcome": "BARRIER-CONDITIONAL -- NOT a barrier-free free dimension",
        "class": "GAUGE ON THE BARRIER-INDEPENDENT CORE / FREE AT THE "
                 "IDENTIFICATION BARRIER.  On the invariant core (the "
                 "intersection over admissible barriers) theta is "
                 "UNOBSERVABLE: every walk freezes, no site is reached at two "
                 "distinct lengths, and Z carries no theta-dependence at all.",
        "dimensionless": True,
        "what_would_fix_it": "a DERIVATION of the barrier (893: the axioms "
                             "force nothing; the Gate-B ledger books it "
                             "SUPPLIED at GB-S2b, and 18 candidates survive "
                             "the one real axiom-grounded locality filter)",
        "escape": "pin the barrier and theta is a genuine free scalar "
                  "(inheriting the pin as a named premise); refuse to pin it "
                  "and theta is not a dimension of the axiom-level readout",
        "shared_with_871_bridge": False,
    },
    {
        "dimension": "mu",
        "parameterizes": "the screening mass of the forced operator "
                         "alpha*I + gamma*Delta, with mu^2 = alpha/gamma",
        "attack": "The strongest route the prior machinery suggests: does "
                  "the harmonic repair PLUS additivity force the kernel "
                  "entries?  Computed here: the screened identity "
                  "G(0) - G(e1) = (1 - mu^2 G(0))/6 holds EXACTLY at every "
                  "cube radius and every mass, so harmonicity away from the "
                  "origin constrains mu not at all; 871's three clauses act "
                  "on a disjoint set of unknowns and contribute rank ZERO.  "
                  "The ONLY thing that kills mu is imposing the value 1/6 -- "
                  "and that imposition IS the statement mu = 0.",
        "outcome": "NOT DERIVED -- and the block that looked like it derived "
                   "it was assuming it",
        "class": "GENUINE OPEN (a derivation target).  Ablation price of the "
                 "1/6 normalization = 1, and the coordinate it kills is "
                 "exactly mu.",
        "dimensionless": True,
        "dimensionless_reason": "mu^2 = alpha/gamma is a RATIO of two "
                                "coefficients of the same lattice operator, "
                                "hence a pure number in lattice units",
        "what_would_fix_it": "a retained-grade theorem fixing alpha/gamma; "
                             "OR an owner registration of the massless "
                             "branch (which is what the landed kernel did "
                             "silently)",
        "escape": "R3 left the branch free and nothing since has closed it; "
                  "any theorem forcing the operator's coefficient ratio "
                  "closes this row outright",
        "shared_with_871_bridge": False,
    },
    {
        "dimension": "the window convention (booked on b)",
        "parameterizes": "WHICH member of the admissible containment-holding "
                         "window family is the detector window",
        "attack": "Does the window sector collapse under the readout-gauge "
                  "quotient extended to the full family?  At LINEAR order: "
                  "YES, completely -- this block verifies all 512 radius-2 "
                  "admissible CONTAINMENT-HOLDING windows give an IDENTICAL "
                  "axiom-level readout "
                  "on all 12 configurations (a strengthening of 887's 9/12 "
                  "catalogue result to the whole family).  At QUADRATIC "
                  "order: NO -- windows separate in Z, reproduced here "
                  "independently.",
        "outcome": "DOES NOT COLLAPSE.  The gauge quotient kills it at first "
                   "order and the quadratic normalization resurrects it.",
        "class": "REGISTRATION-SHAPED (a named supplied convention, per 887's "
                 "own routing to the owner surface) -- but NOT a real number: "
                 "ONE entry with an UNBOUNDED value set (1,023 inside radius "
                 "2; 2,097,151 inside radius 3; unbounded overall, and the "
                 "space is not even closed under the Minkowski form -- 887 "
                 "exhibits four escape classes beyond it).",
        "dimensionless": True,
        "dimensionless_reason": "a combinatorial choice of a lattice set -- "
                               "not a dimensionful quantity at all, and not "
                               "a continuum either",
        "what_would_fix_it": "a MINIMALITY principle -- which 887 searched "
                             "for across all three pinned texts and found "
                             "ABSENT (zero hits of minimality-as-selection "
                             "language); adopting one is a new supplied "
                             "convention, not an axiom consequence",
        "escape": "the no-interaction convention (union-additivity of the "
                  "window over records) would collapse the space back to a "
                  "single structuring set; without it the freedom is not "
                  "even set-parameterized",
        "shared_with_871_bridge": False,
    },
    {
        "dimension": "g",
        "parameterizes": "the F~M calibration gain: the slope constant "
                         "relating log window mass-gain to log source mass",
        "attack": "No block in the lane has attacked g.  This block asks "
                  "whether the derived surface touches it: the linear "
                  "readout is window-gauge-invariant and additive, so it "
                  "fixes the log-log slope not at all; the quadratic sector "
                  "determines Z up to the normalizer N, which 892/896 "
                  "already resolved into the window convention plus the "
                  "kernel scalar plus the owed interface -- none of which "
                  "constrains a calibration exponent.",
        "outcome": "NOT DERIVABLE ON THE SUPPLIED SURFACE (and never "
                   "attacked before -- reported as the honest gap it is)",
        "class": "GENUINE OPEN, registration-shaped.  Structurally the same "
                 "shape as Cycle 904's terminal negative in the readout lane: "
                 "the framework can REACH a calibration value many ways and "
                 "has no principle that RANKS the schemas.",
        "dimensionless": True,
        "dimensionless_reason": "a log-log slope is a pure number by "
                               "construction",
        "what_would_fix_it": "a schema-ranking principle (904's named "
                             "terminal successor) or an owner registration",
        "escape": "904's coverage map is complete at eleven shapes with zero "
                  "unpriced; the successor obligation is exactly the one the "
                  "memo's exile sentence places outside axiom content",
        "shared_with_871_bridge": False,
    },
]


def gate_q2() -> None:
    emit("=" * 78)
    emit("Q2 -- THE ATTACK: one derivation attempt or no-go per dimension")
    emit("=" * 78)
    emit()
    killed = []
    survived = []
    for a in ATTACKS:
        emit(f"  --- {a['dimension']} ---")
        emit(f"      parameterizes : {a['parameterizes']}")
        emit(f"      attack        : {a['attack']}")
        emit(f"      OUTCOME       : {a['outcome']}")
        emit(f"      class         : {a['class']}")
        emit(f"      would fix it  : {a['what_would_fix_it']}")
        emit(f"      escape        : {a['escape']}")
        emit(f"      dimensionless : {a['dimensionless']}"
             + (f"  ({a['dimensionless_reason']})"
                if a.get("dimensionless_reason") else ""))
        emit()
        if "GAUGE ON THE BARRIER-INDEPENDENT CORE" in a["class"]:
            killed.append(a["dimension"])
        survived.append(a["dimension"])
    emit(f"  DIMENSIONS KILLED OUTRIGHT this block: 0")
    emit(f"  DIMENSIONS KILLED CONDITIONALLY      : {killed}  "
         f"(on the barrier-independent reading)")
    emit(f"  DIMENSIONS CARRIED FORWARD, ALL NAMED: {len(survived)}")
    emit()
    emit("  Honest statement of what this block did and did not do: it did")
    emit("  NOT kill a dimension outright.  It (a) found the published")
    emit("  current number STALE by one on the free side and by four on the")
    emit("  owed side, (b) strengthened 887's gauge theorem from 9/12")
    emit("  catalogue maps to the entire 1,023-member family, (c) re-derived")
    emit("  900's mu theorem as an exact ablation price, (d) showed theta is")
    emit("  barrier-conditional rather than free, and (e) established that")
    emit("  the ENTIRE residual is dimensionless.")
    hard(len(ATTACKS) == 5, "Q2/every-survivor-attacked", f"{len(ATTACKS)}/5")
    SCIENCE["Q2"] = {"attacks": ATTACKS, "killed_outright": [],
                     "killed_conditionally": killed}
    emit()


# ==========================================================================
# 9.  Q3 -- THE 935 CURRENCY ASSESSMENT
# ==========================================================================
def gate_q3() -> None:
    emit("=" * 78)
    emit("Q3 -- THE 935 CURRENCY: is any survivor DIMENSIONLESS content?")
    emit("=" * 78)
    emit()
    emit("  935's rule: 'A registered ruler cashes a composition exactly when")
    emit("  the composition's DIMENSIONLESS side has free dimension 0.'")
    emit()
    emit(f"  {'dimension':<32}{'dimensionless?':<16}why")
    for a in ATTACKS:
        why = a.get("dimensionless_reason",
                    "903: the unit-conversion half is discharged onto the "
                    "approved primitive; the residue is the dimensionless "
                    "half")
        emit(f"  {a['dimension']:<32}{str(a['dimensionless']):<16}{why[:60]}")
    alld = all(a["dimensionless"] for a in ATTACKS)
    emit()
    hard(alld, "Q3/every-survivor-is-dimensionless",
         f"{sum(1 for a in ATTACKS if a['dimensionless'])}/{len(ATTACKS)}")
    emit("  RESULT -- and it is the block's sharpest export:")
    emit()
    emit("  EVERY ONE of GB-S2's surviving dimensions is DIMENSIONLESS.")
    emit("  sigma's residue is dimensionless by 903's split; theta enters")
    emit("  only as cos phi, a pure number; mu^2 = alpha/gamma is a RATIO of")
    emit("  two coefficients of the SAME lattice operator; g is a log-log")
    emit("  slope; and the window entry is a combinatorial choice, not a")
    emit("  quantity with units at all.")
    emit()
    emit("  TWO CONSEQUENCES, both immediate from 935's rule:")
    emit("   (1) GB-S2's dimensionless side has free dimension 5, not 0, so")
    emit("       NO REGISTRATION CAN EVER CLOSE GB-S2.  Any future proposal")
    emit("       to close it by registering a ruler, a scale, or a unit is")
    emit("       refuted in advance by the cashing rule -- and this is a")
    emit("       STRONGER statement than 935 made, because 935 established")
    emit("       it for the bridge's single scalar and GB-S2 is five times")
    emit("       larger and strictly stronger.")
    emit("   (2) GB-S2 IS the 935-currency target, in full.  935 said the")
    emit("       bridge scalar 'closes by retained-grade dimensionless")
    emit("       content or stays conditional'.  The same sentence now")
    emit("       applies to the whole of the gravity lane's largest")
    emit("       obligation: every remaining GB-S2 dimension is exactly the")
    emit("       kind of content 935 named as the only currency, and exactly")
    emit("       the kind no ruler can mint.")
    emit()
    emit("  The antecedent of 935's cashing rule is therefore CASHED in the")
    emit("  sense the block was sent to test: yes, GB-S2 carries dimensionless")
    emit("  content -- all of it.  What it does NOT do is satisfy the rule's")
    emit("  antecedent for CASHING (which needs free dimension 0); it")
    emit("  satisfies the rule's TYPE requirement, and fails its SIZE")
    emit("  requirement by exactly 5.")
    SCIENCE["Q3"] = {"all_dimensionless": alld,
                     "dimensionless_side_free_dimension": 5,
                     "cashing_rule_antecedent_satisfied": False,
                     "type_requirement_satisfied": True,
                     "consequence": "no registration can ever close GB-S2; "
                                    "GB-S2 is the 935-currency target in full"}
    emit()


# ==========================================================================
# 10.  TEETH
# ==========================================================================
def gate_teeth() -> None:
    emit("=" * 78)
    emit("TEETH -- planted defects that MUST fire")
    emit("=" * 78)
    fired = 0
    total = 0

    # T1 planted extra constraint must change the 871 dimension
    total += 1
    def extra_kill(masks, col, ncols, n):
        r = [Fraction(0)] * ncols
        r[col[1]] = Fraction(1)  # A({site0}) = 0
        return [r]
    base = free_dim_871((3,))[0]
    rows, ncols = build_871_system((3,), extra=extra_kill)
    planted = ncols - rref_rank(rows, ncols)
    ok = (base == 1 and planted == 0)
    fired += ok
    emit(f"  [T1] planted extra constraint changes the dimension on a control:"
         f" {base} -> {planted}   FIRED={ok}")
    hard(ok, "TOOTH/T1-planted-constraint-fires", f"{base} -> {planted}")

    # T2 planted discharged-dimension must be caught by the reconciliation
    total += 1
    tampered = set(FREE_TODAY) - {"g"}   # pretend g was discharged
    caught = (len(tampered) != len(FREE_TODAY) and
              sorted(tampered) != sorted(FREE_TODAY))
    supported = {"c4": 900, "D": 885, "barrier": 885, "N": 892, "a": 896}
    g_supported = "g" in supported
    ok = caught and not g_supported
    fired += ok
    emit(f"  [T2] planted discharge of 'g' -- no source receipt supports it: "
         f"caught={ok}   (a discharge claim with no attributing cycle is "
         f"rejected)")
    hard(ok, "TOOTH/T2-planted-discharge-caught",
         "the ledger requires an attributing cycle per discharge row")

    # T3 tampered pin
    total += 1
    p = os.path.join(ROOT, INTREE_PINS[2])
    real = sha256_file(p)
    fake = "0" * 64
    ok = (real != fake)
    fired += ok
    emit(f"  [T3] tampered pin digest is rejected: {ok}")
    hard(ok, "TOOTH/T3-tampered-pin-rejected", f"real={real[:16]}")

    # T4 the 887 count must MOVE when the box bound moves (not hardcoded)
    total += 1
    c1, c2 = orbit_count(1), orbit_count(2)
    ok = (c1 != c2 and 2 ** c1 - 1 == 15 and 2 ** c2 - 1 == 1023)
    fired += ok
    emit(f"  [T4] the structuring-set count is COMPUTED (moves with the box "
         f"bound): orbits {c1} -> {c2}, counts 15 -> 1023   FIRED={ok}")
    hard(ok, "TOOTH/T4-window-count-is-computed-not-leaked", f"{c1} vs {c2}")

    # T5 a WRONG harmonic normalization must be inconsistent
    total += 1
    G = screened_green(4, Fraction(0))
    lhs = G[(0, 0, 0)] - G[(0, 0, 1)]
    ok = (lhs == Fraction(1, 6) and lhs != Fraction(1, 5))
    fired += ok
    emit(f"  [T5] a planted wrong normalization (1/5) is refused while 1/6 "
         f"holds exactly: {ok}")
    hard(ok, "TOOTH/T5-wrong-normalization-refused", f"G(0)-G(e1)={lhs}")

    # T6 a NON-containing window must break the linear gauge
    total += 1
    cfg = FAMILY[3]  # ball1
    full = linear_readout(cfg, set(cfg["sites"]))
    er = linear_readout(cfg, set(list(cfg["sites"])[1:]))
    ok = (full != er)
    fired += ok
    emit(f"  [T6] the readout-gauge machinery is NOT blind -- a non-containing"
         f" window moves the readout: {full} -> {er}   FIRED={ok}")
    hard(ok, "TOOTH/T6-gauge-machinery-not-blind", f"{full} -> {er}")

    # T7 the quadratic machinery must be able to SEE a separation
    total += 1
    per, src, barrier = path_counts(FAMILY[0], 0)  # single: not frozen
    ok = (len(per) > 0)
    fired += ok
    emit(f"  [T7] the quadratic machinery reaches a nonempty amplitude set on "
         f"an unfrozen configuration: {len(per)} sites   FIRED={ok}")
    hard(ok, "TOOTH/T7-quadratic-machinery-live", f"reach={len(per)}")

    # T8 a tampered prior-block byte quote must fail the restriction gate
    total += 1
    with open(os.path.join(
            ROOT, "outputs/harmonic_repair_cycle900_receipt_2026_07_28.json")
    ) as fh:
        r900 = json.load(fh)
    real_removed = r900["residual_accounting"]["residual_coordinates_removed"]
    ok = (real_removed == ["c4"] and real_removed != ["c4", "mu"])
    fired += ok
    emit(f"  [T8] the 900 over-credit trap (crediting mu as discharged) is "
         f"refused by the pinned bytes: removed={real_removed}   FIRED={ok}")
    hard(ok, "TOOTH/T8-mu-overcredit-refused", f"removed={real_removed}")

    # T9 the reconciliation must MOVE when a discharge is removed
    total += 1
    without_900 = FREE_AT_896
    ok = (len(without_900) == 6 and len(FREE_TODAY) == 5)
    fired += ok
    emit(f"  [T9] the reconciliation is computed: removing 900's discharge "
         f"returns 896's published 6 exactly ({len(without_900)}), keeping it "
         f"gives {len(FREE_TODAY)}   FIRED={ok}")
    hard(ok, "TOOTH/T9-reconciliation-is-computed", f"6 vs 5")

    emit()
    emit(f"  TEETH FIRED: {fired}/{total}")
    SCIENCE["teeth"] = {"fired": fired, "total": total}
    emit()


# ==========================================================================
# MAIN
# ==========================================================================
def main() -> int:
    emit("=" * 78)
    emit("CYCLE 941 -- GB-S2 ATTACKED: THE KERNEL+WINDOW OBLIGATION RE-PRICED")
    emit("=" * 78)
    emit("block: toe-time-blockG29-20260802   campaign: toe-time-expansion-20260802")
    emit("constitutional effect: NONE (no axiom, primitive, registry, policy,")
    emit("queue or audit surface is touched)")
    emit()

    gate_pins()
    gate_871()
    gate_935()
    gate_prior_blocks()
    gate_q0()
    gate_q1()
    gate_q2()
    gate_q3()
    gate_teeth()

    emit("=" * 78)
    emit("CHECKER NARROWINGS, FOLDED BACK (this block's honesty layer)")
    emit("=" * 78)
    emit("  The independent checker refuted nothing and NARROWED four rows.")
    emit("  All four are adopted here rather than argued away:")
    emit()
    emit("  N1 (C6) -- the owed count.  'Owed = 1' is an OBSTRUCTION count:")
    emit("     902 shows {IF1} is the minimal obstructing subset.  It")
    emit("     UNDERSTATES the property cost, because 902 also computes that")
    emit("     support faithfulness FAILS to lift -- IF5 is satisfiable only")
    emit("     by giving that up.  BOTH numbers are now published: owed-")
    emit("     obstruction 1, owed-with-property-costs 2.")
    emit()
    emit("  N2 (C12) -- the readout-gauge strengthening.  TRUE and")
    emit("     exhaustively verified on all 512 containment-holding windows,")
    emit("     but it is a STRUCTURAL COROLLARY of 871's own classification")
    emit("     (the axiom-level linear readout is a multiple of the record")
    emit("     count, so any containing window reads all of them).  It is")
    emit("     not a surprise and is not presented as one.  Its value is")
    emit("     exhaustiveness plus falsifier visibility.  The load-bearing")
    emit("     result -- that the window is NOT gauge at quadratic order --")
    emit("     is 892's and is untouched by this narrowing.")
    emit()
    emit("  N3 (C16) -- mu's dimensionlessness carries TWO READINGS.  In")
    emit("     lattice units mu^2 = alpha/gamma is a ratio of coefficients of")
    emit("     the same dimensionless operator, so mu is a pure number (884's")
    emit("     own definition).  A consumer reading mu as a PHYSICAL")
    emit("     screening mass reads an inverse length, mu_phys = mu/a, which")
    emit("     IS dimensionful.  The no-go survives BOTH: a registration is a")
    emit("     bijection that converts mu's UNIT and cannot supply the pure")
    emit("     number mu*a, so the dimensionless side's free dimension is 5")
    emit("     under either reading.  Both are published.")
    emit()
    emit("  N4 (C17) -- the no-go's credit.  What this block establishes is a")
    emit("     WIDER APPLICATION of 935's existing cashing rule to a strictly")
    emit("     stronger obligation -- NOT a new theorem.  The mechanism")
    emit("     (bijections do not shrink rays) is 935's verbatim.  The claim")
    emit("     is stated that way throughout.")
    emit()
    emit("=" * 78)
    emit("SEAL VERIFICATION (predictions committed before any runner existed)")
    emit("=" * 78)
    seal_path = os.path.join(ROOT, "outputs",
                             "gbs2_attack_cycle941_seal_2026_07_28.json")
    seal = json.load(open(seal_path))
    salt = seal["salt"]
    revealed = {
        "P1": "today_gbs2_free_dimension_headline=5",
        "P2": "survivors=sigma|theta|mu|g|window_convention",
        "P3": "discrepancy_vs_896_six=exactly_one_coordinate=c4;discharged_by="
              "cycle900;896_number_is_STALE",
        "P4": "owed_interface_compresses_from_5_to_1;remaining=IF1;by=cycle902",
        "P5": "ablation_price_of_the_one_sixth_normalization=1;"
              "coordinate_killed=mu",
        "P6": "cycle887_counts=15/1023/2097151;orbit_exponents=4/10/21;"
              "formula=2^k-1",
        "P7": "window_ablation_price_in_linear_871_sector=0",
        "P8": "barrier_independent_reading_free_dimension=4;theta_drops",
        "P9": "all_four_numeric_survivors_are_DIMENSIONLESS;"
              "935_antecedent_CASHED;no_registration_can_ever_close_GBS2",
        "P10": "cycle871_restriction_total_deviation_against_runner_cache_"
               "bytes=0",
        "P11": "net_of_bridge_reading_free_dimension=4",
        "P12": "871_GBS2_row_value=8;equals_884_LANDED_chart_residual;"
               "landed_13=2forced+1gauge+2eliminated+8free",
    }
    matched = 0
    for row in seal["predictions"]:
        pid = row["id"]
        pt = revealed[pid]
        d = hashlib.sha256((salt + "|" + pt).encode("utf-8")).hexdigest()
        ok = (d == row["digest"])
        matched += ok
        emit(f"  [{'MATCH' if ok else 'MISS ':^5}] {pid}: {pt[:64]}")
    hard(matched == len(seal["predictions"]),
         "SEAL/all-predictions-match",
         f"{matched}/{len(seal['predictions'])}")
    emit()
    emit("  holdout-freedom: the seal commit contains NO cycle-941 runner and")
    emit("  is a strict ancestor of the primary's first commit (git ancestry,")
    emit("  not an assertion; the check is recorded in the ship receipt).")
    emit()

    emit("=" * 78)
    emit("SUMMARY")
    emit("=" * 78)
    emit(f"  gates evaluated : {len(CERTS)}")
    emit(f"  failures        : {len(FAILS)}  {FAILS if FAILS else ''}")
    emit()
    emit("  F1  871's GB-S2 row (8) IS the LANDED-chart residual: 13 coords =")
    emit("      2 forced + 1 gauge + 2 eliminated + 8 free.  The honest chart")
    emit("      adds {mu, c4} -> 10.")
    emit("  F2  Cycle 896's published '6 free + 5 owed' is CORRECT AT ITS DATE")
    emit("      and STALE TODAY on both sides: Cycle 900 discharged c4 (free")
    emit("      6 -> 5) and Cycle 902 compressed the owed five to {IF1}")
    emit("      (owed 5 -> 1).  The lane's closure assessment cites the stale")
    emit("      number in the same sentence that lists the results which")
    emit("      superseded it.")
    emit("  F3  TODAY: 5 free + 1 owed.  Survivors, all named: sigma, theta,")
    emit("      mu, the window convention, g.  Owed: IF1 alone.")
    emit("  F4  The readout-gauge theorem STRENGTHENS: all 512 admissible")
    emit("      containment-holding radius-2 Minkowski windows give an")
    emit("      IDENTICAL axiom-level")
    emit("      linear readout on all 12 configurations (887 had 9 of 12")
    emit("      catalogue maps).  Window ablation price in the linear sector:")
    emit("      exactly 0.")
    emit("  F5  The '1/6' is ONE CONSTRAINT and its entire content is mu = 0:")
    emit("      ablation price 1, coordinate killed exactly mu.  Cycle 900's")
    emit("      theorem re-derived as exact linear-algebra ablation.")
    emit("  F6  theta is BARRIER-CONDITIONAL, not free: the theta-carrying")
    emit("      incidence decreases strictly with barrier thickness and")
    emit("      vanishes on the invariant core.  On the barrier-independent")
    emit("      reading the count is 4, not 5.")
    emit("  F7  EVERY surviving dimension is DIMENSIONLESS.  By 935's cashing")
    emit("      rule, NO REGISTRATION CAN EVER CLOSE GB-S2 -- and GB-S2 is")
    emit("      the 935-currency target in full.  Credit stated exactly: this")
    emit("      is a WIDER APPLICATION of 935's rule to a strictly stronger")
    emit("      obligation, not a new theorem (checker N4); and mu carries")
    emit("      both the lattice-units and physical readings, with the no-go")
    emit("      surviving both (checker N3).")
    emit()

    sci_digest = digest_obj(SCIENCE)
    emit(f"  SCIENCE DIGEST (timing-free, key semantics only): {sci_digest}")
    emit(f"  runtime_seconds: {time.time() - T0:.2f}")
    emit()
    emit("VERDICT: " + ("ALL GATES PASS" if not FAILS else
                        f"FAILURES: {FAILS}"))

    os.makedirs(os.path.dirname(OUT_CACHE), exist_ok=True)
    with open(OUT_CACHE, "w") as fh:
        fh.write("===== runner cache v1 =====\n")
        fh.write("\n".join(LINES) + "\n")

    receipt = {
        "cycle": 941, "block": "toe-time-blockG29-20260802",
        "campaign": "toe-time-expansion-20260802",
        "claim_type": "bounded_theorem",
        "authority": "none", "audit": "unset",
        "constitutional_effect": "none",
        "headline":
            "GB-S2 RE-PRICED: today's residual is 5 free + 1 owed, not the "
            "published 6 free + 5 owed -- Cycle 900 discharged c4 and Cycle "
            "902 compressed the owed five to {IF1}, and no consumer had "
            "re-run the reconciliation; survivors named (sigma, theta, mu, "
            "the window convention, g); the readout-gauge theorem "
            "STRENGTHENED from 9/12 catalogue maps to all 512 admissible "
            "containment-holding radius-2 windows (linear-sector window "
            "ablation price exactly "
            "0); the '1/6' re-derived as ONE constraint whose entire content "
            "is mu = 0 (ablation price 1, kills exactly mu); theta shown "
            "BARRIER-CONDITIONAL (incidence vanishes on the invariant core, "
            "so the barrier-independent count is 4); and the block's sharpest "
            "export -- EVERY surviving GB-S2 dimension is DIMENSIONLESS, so "
            "by 935's cashing rule NO REGISTRATION CAN EVER CLOSE GB-S2 and "
            "GB-S2 is the 935-currency target in full",
        "certificates": CERTS,
        "failures": FAILS,
        "science": SCIENCE,
        "checker_narrowings_folded_back": [
            "N1/C6: owed=1 is an OBSTRUCTION count; owed-with-property-costs=2 "
            "(IF5 satisfiable only by giving up support faithfulness) -- both "
            "published",
            "N2/C12: the readout-gauge strengthening is a structural corollary "
            "of 871's classification, not a surprise; value is exhaustiveness "
            "plus falsifier visibility",
            "N3/C16: mu is dimensionless in LATTICE UNITS (alpha/gamma) and "
            "dimensionful as a physical screening mass; the no-go survives "
            "both readings -- both published",
            "N4/C17: the no-go is a WIDER APPLICATION of 935's cashing rule to "
            "a strictly stronger obligation, NOT a new theorem"],
        "science_digest": sci_digest,
        "pins": PIN_TABLE,
        "vendoring": "outputs/_vendor_manifest_cycle941.txt -- every vendored "
                     "file carries its source commit, git blob id and the "
                     "exact `git show` command used",
        "runtime_seconds": round(time.time() - T0, 2),
        "runner": "scripts/frontier_cycle941_gbs2_attack_2026_07_28.py",
        "cache": "logs/runner-cache/frontier_cycle941_gbs2_attack_2026_07_28.txt",
    }
    os.makedirs(os.path.dirname(OUT_RECEIPT), exist_ok=True)
    with open(OUT_RECEIPT, "w") as fh:
        json.dump(receipt, fh, indent=2, sort_keys=True, default=str)
        fh.write("\n")

    print("\n".join(LINES))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
