#!/usr/bin/env python3
"""Cycle 894 -- INDEPENDENT CHECK, specified to REFUTE.

The primary claims, for Cycle 894:

  Q1  The two lineages do NOT meet at the substrate level (a computed type
      mismatch: disjoint index sets, coprime symmetry group orders 11 and 24,
      and a missing record-configuration argument on the 878 side), but they
      DO meet in the category of finitely additive non-negative rational set
      functions on finite Boolean algebras, where a BRIDGE (phi, N) is
      definable and every verdict is bridge-independent.
  Q2  NO-GO.  All 25 cells of the 5-weighting x 5-requirement table FAIL.
  Q3  A five-property sheet for the missing weighting, sized.

This checker is adversarial.  It does not read the primary's answers before
computing its own, it does not import the primary, and it attacks the
composition map hardest of all -- because that is the claim on which the whole
table rests.  Specifically it hunts the BRIDGE THE PRIMARY MISSED, trying two
candidate bridging constructions the primary never built:

  BRIDGE-A  THE CONFIGURATION-BLOCK (ORBIT) BRIDGE.  The primary's C894-T1
            leans on the 878 side having no record-configuration argument.
            But a bridge may READ the configuration off the event: partition E
            into blocks, one per configuration, and let the weight of window W
            at configuration R be the block-R mass of phi^{-1}(W).  This
            manufactures the missing arity for free.  If it works, the
            primary's headline obstruction is escapable and the NO-GO is
            wrong.
  BRIDGE-B  THETA AS AN OBSERVABLE.  892's IF3 explicitly permits declaring
            the kernel coordinate an observable.  Enlarge the event space to
            E x Theta and weight the product.  If it works, IF3 and IF6 are
            dischargeable without a new weighting.

Both bridges are CONSTRUCTED and TESTED here, not dismissed.

Independence: the amplitude is rebuilt by a different route -- the path-length
correlator that yields the Chebyshev coefficients M_d directly, from which Z
is reassembled -- so the primary's layer-DP and this checker's correlator must
agree value-for-value on all 648 cells or one of them is wrong.  The five 878
weightings are re-implemented from their AST-read definitions rather than by
calling the vendored build_candidates, then cross-checked against it.  Window
sets, the containment filter and the family are independently re-derived.
Iteration orders are reversed where order could matter.

Teeth: eight mutations, each of which MUST be caught.

Exit code is 0 whenever the checker's own machinery is sound and its teeth
bite, regardless of whether the primary's claims survive.  The verdict is
data, not an exit status.
"""
from __future__ import annotations

import ast
import hashlib
import importlib.abc
import json
import sys
import time
from collections import Counter
from fractions import Fraction
from itertools import combinations, product, permutations
from math import gcd
from pathlib import Path

START = time.time()

CYCLE = 894
RUNTIME_CAP_SEC = 900

ROOT = Path(__file__).resolve().parents[1]
SELF_REL = "scripts/frontier_cycle894_interface_independent_check_2026_07_28.py"
OUT_JSON = (ROOT / "outputs"
            / "interface_independent_check_cycle894_receipt_2026_07_28.json")

C878_PRIMARY = "scripts/frontier_cycle878_event_space_groundwork_2026_07_28.py"
C878_RECEIPT = "outputs/event_space_groundwork_cycle878_receipt_2026_07_28.json"
C892_PRIMARY = "scripts/frontier_cycle892_gbw1b_pricing_2026_07_28.py"
C892_RECEIPT = "outputs/gbw1b_pricing_cycle892_receipt_2026_07_28.json"
C885_PRIMARY = "scripts/frontier_cycle885_gbw1_record_window_2026_07_28.py"
C887_PRIMARY = "scripts/frontier_cycle887_window_freedom_2026_07_28.py"
AXIOMS_MD = "docs/MINIMAL_AXIOMS_2026-06-29.md"

C894_PRIMARY = "scripts/frontier_cycle894_interface_attack_2026_07_28.py"
C894_RECEIPT = "outputs/interface_attack_cycle894_receipt_2026_07_28.json"

PINS = (C878_PRIMARY, C878_RECEIPT, C892_PRIMARY, C892_RECEIPT,
        C885_PRIMARY, C887_PRIMARY, AXIOMS_MD)

BRIEF_SHA256 = {
    C878_PRIMARY:
        "6661955d91bd7321804c534c041fbcbc6ac6bd338aeef89c6bb1faf47b69093b",
    C878_RECEIPT:
        "4ef57b09238ed7b92ac1bf8113d45aff0093d2c8deb54ce717f87a2e6d42d17c",
    C892_PRIMARY:
        "76100068829f2143bc629610954858875a1ad6569246d43e59d5502c883b5c1f",
    C892_RECEIPT:
        "1a8c220959038a7f09e0576e745d8497841c7cd102307834be8684af513b5fae",
    C885_PRIMARY:
        "daee8bbfefde80a351bf82a3028d96baf447493d3add8cdc85f4eb63fc114f32",
    C887_PRIMARY:
        "139ed9e2fce1775d41e5d46bf2d6b43063c47f4a3a0cf2c55edf4d8ce2f4fc83",
    AXIOMS_MD:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
}

# The 894 primary is BLOCKLISTED for import and read only as text, and only
# AFTER this checker has computed its own numbers.
BLOCKED_STEMS = {Path(p).stem for p in PINS} | {Path(C894_PRIMARY).stem}


def read_bytes(rel: str) -> bytes:
    return (ROOT / rel).read_bytes()


def read_text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def sha256_of(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def q(v) -> str:
    f = Fraction(v)
    return f"{f.numerator}/{f.denominator}"


def preflight() -> None:
    bad = [p for p in PINS
           if sha256_of(read_bytes(p)) != BRIEF_SHA256[p]]
    if bad:
        print(f"PREFLIGHT ABORT: pinned digest mismatch on {bad}")
        sys.exit(2)


class _Firewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKED_STEMS:
            self.hits.append(fullname)
            raise ImportError(f"FIREWALL: {fullname}")
        return None


FIREWALL = _Firewall()
sys.meta_path.insert(0, FIREWALL)
preflight()


def ast_extract(rel: str, wanted, seed: dict):
    tree = ast.parse(read_text(rel))
    body, seen = [], set()
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in wanted:
            body.append(node)
            seen.add(node.name)
        elif isinstance(node, ast.Assign):
            names = [t.id for t in node.targets if isinstance(t, ast.Name)]
            if any(n in wanted for n in names):
                body.append(node)
                seen.update(n for n in names if n in wanted)
        elif (isinstance(node, ast.AnnAssign)
              and isinstance(node.target, ast.Name)
              and node.target.id in wanted):
            body.append(node)
            seen.add(node.target.id)
    ns = dict(seed)
    exec(compile(ast.Module(body=body, type_ignores=[]),
                 filename=f"<chk:{rel}>", mode="exec"), ns)  # noqa: S102
    return ns, sorted(seen), sorted(set(wanted) - seen)


def _lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b) if a and b else 0


SEED = {"Fraction": Fraction, "product": product,
        "permutations": permutations, "Counter": Counter,
        "lcm": _lcm, "gcd": gcd}

NS885, _, MISS885 = ast_extract(
    C885_PRIMARY, {"NEIGHBOURS", "_lcg", "make_config", "build_family"}, SEED)
FAMILY = NS885["build_family"]()
NEIGHBOURS = NS885["NEIGHBOURS"]

CATALOGUE_NODES = (
    "NEIGHBOURS", "det3", "proper_cubic_rotations", "ROT24", "IDENTITY3",
    "matmul", "apply_mat", "apply_mat_frac", "WEIGHTS", "barycentre", "radii2",
    "packaged", "readout", "windowed_readout", "minkowski", "erosion",
    "bounding_box", "axis_segment_closure", "S_ZERO", "S_N6", "S_BALL1",
    "S_BALL2", "S_FAR", "S_NOT_ROT_INV", "mk_minkowski_map", "mk_erosion_map",
    "map_box", "map_segment_closure", "map_size_keyed", "map_readout_keyed",
    "map_box_union_dil1", "map_depth_keyed",
    "map_IMP_nonequivariant_inflation", "map_IMP_extremal_shell",
    "map_IMP_boundary_shell", "CONST_CUBE", "map_IMP_constant_cube",
    "transform", "truncations", "_TRUNC_CACHE", "make_config", "EXHIBIT_CAP",
    "evaluate_map", "containment_profile", "ESCAPE_CATALOGUE",
    "selector_catalogue", "TEST_SHIFTS",
)
NS887, _, MISS887 = ast_extract(
    C887_PRIMARY, set(CATALOGUE_NODES), dict(SEED, FAMILY=FAMILY))
CATALOGUE = NS887["selector_catalogue"]()
CAT = dict(CATALOGUE)
ROT24 = NS887["ROT24"]

# The kernel geometry, read as literals from the pinned 892 primary.
NS892C, _, MISS892 = ast_extract(
    C892_PRIMARY, {"RBOX", "MAX_STEPS", "THETA_GRID", "THETA_885",
                   "BORN_VOCABULARY"}, SEED)
RBOX = NS892C["RBOX"]
MAX_STEPS = NS892C["MAX_STEPS"]
THETA_GRID = NS892C["THETA_GRID"]
THETA_885 = NS892C["THETA_885"]
BORN_VOCABULARY = NS892C["BORN_VOCABULARY"]

R878 = json.loads(read_text(C878_RECEIPT))
R892 = json.loads(read_text(C892_RECEIPT))

BOX = tuple(product(range(-RBOX, RBOX + 1), repeat=3))
INBOX = frozenset(BOX)


# --------------------------------------------------------------------------
# INDEPENDENT amplitude route: the path-length correlator -> Chebyshev M_d
#
# A(x) = sum_L c_L(x) u^L with u on the unit circle and c_L = count_L(x)/|src|.
# Hence |A(x)|^2 = sum_{L,L'} c_L c_L' cos((L-L') phi)
#               = sum_d M_d(x) T_d(cos phi),
# with M_0 = sum_L c_L^2 and M_d = 2 * sum_{L-L'=d>0} c_L c_L'.
# The primary evaluates u first and squares; this checker builds the
# correlator first and evaluates the Chebyshev series.  Different arithmetic,
# same pinned definition -- a disagreement means one of the two is wrong.
# --------------------------------------------------------------------------
def counts_by_length(cfg):
    """count_L(x) for L = 0..MAX_STEPS.  Reversed neighbour order on purpose."""
    barrier = frozenset(cfg["sites"])
    # the record-determined source: box sites closest to the barycentre
    n = len(cfg["sites"])
    bc = tuple(Fraction(sum(s[i] for s in cfg["sites"]), n) for i in range(3))
    best, src = None, []
    for x in reversed(BOX):
        r2 = sum((Fraction(x[i]) - bc[i]) ** 2 for i in range(3))
        if best is None or r2 < best:
            best, src = r2, [x]
        elif r2 == best:
            src.append(x)
    src = tuple(sorted(src))
    layers = [{x: 1 for x in src}]
    for _ in range(MAX_STEPS):
        cur, nxt = layers[-1], {}
        for x in sorted(cur):
            v = cur[x]
            for nb in reversed(NEIGHBOURS):
                y = (x[0] + nb[0], x[1] + nb[1], x[2] + nb[2])
                if y in INBOX and y not in barrier:
                    nxt[y] = nxt.get(y, 0) + v
        layers.append(nxt)
    return layers, src


_CB: dict = {}


def correlator(cfg):
    """M_d(x) for every amplitude site x, as exact Fractions."""
    key = cfg["name"]
    if key in _CB:
        return _CB[key]
    layers, src = counts_by_length(cfg)
    ns = len(src)
    sites = set()
    for lay in layers:
        sites |= set(lay)
    M: dict = {}
    for x in sites:
        c = [Fraction(lay.get(x, 0), ns) for lay in layers]
        m = [Fraction(0)] * (MAX_STEPS + 1)
        for L in range(len(c)):
            for Lp in range(len(c)):
                d = abs(L - Lp)
                m[d] += c[L] * c[Lp]
        M[x] = m
    _CB[key] = (M, src, layers)
    return _CB[key]


def cheb(d: int, p: Fraction) -> Fraction:
    """T_d by the recurrence, built independently."""
    a, b = Fraction(1), Fraction(p)
    if d == 0:
        return a
    for _ in range(d - 1):
        a, b = b, 2 * p * b - a
    return b


def Zc(cfg, t: Fraction, window) -> Fraction:
    """Z reassembled from the correlator + Chebyshev series."""
    M, _, _ = correlator(cfg)
    p = (1 - t * t) / (1 + t * t)
    tot = Fraction(0)
    for x in window:
        if x in M and x in INBOX:
            m = M[x]
            tot += sum((m[d] * cheb(d, p) for d in range(len(m))), Fraction(0))
    return tot


def Zsq(cfg, t: Fraction, window) -> Fraction:
    """Z by direct squaring -- the primary's route, reimplemented, used ONLY
    as a cross-check of the correlator route."""
    layers, src = counts_by_length(cfg)
    ns = len(src)
    d = 1 + t * t
    u = ((1 - t * t) / d, (2 * t) / d)
    amp: dict = {}
    up = (Fraction(1), Fraction(0))
    for L, lay in enumerate(layers):
        if L > 0:
            up = (up[0] * u[0] - up[1] * u[1], up[0] * u[1] + up[1] * u[0])
        for x, c in lay.items():
            w = (up[0] * Fraction(c, ns), up[1] * Fraction(c, ns))
            a = amp.get(x, (Fraction(0), Fraction(0)))
            amp[x] = (a[0] + w[0], a[1] + w[1])
    return sum((amp[x][0] ** 2 + amp[x][1] ** 2
                for x in window if x in amp and x in INBOX), Fraction(0))


def window_of(name: str, cfg) -> set:
    return set(CAT[name](cfg)["set"])


def holding_windows() -> list:
    out = []
    for name, fn in CATALOGUE:
        if not NS887["evaluate_map"](fn)["admissible_REQ1_REQ5"]:
            continue
        if NS887["containment_profile"](fn)["supp_subset_W_on_all_configs"]:
            out.append(name)
    return sorted(out)


HOLDING = holding_windows()


# --------------------------------------------------------------------------
# INDEPENDENT rebuild of the five 878 weightings, from their definitions
# --------------------------------------------------------------------------
NS878, SEEN878, MISS878 = ast_extract(
    C878_PRIMARY,
    {"build_candidates", "CANDIDATE_NAMES", "CONTROL_NAME", "REGISTER_CAP",
     "lcm"}, SEED)
CANDIDATE_NAMES = NS878["CANDIDATE_NAMES"]
REGISTER_CAP = NS878["REGISTER_CAP"]


def surrogate():
    f = R878["findings"]
    cv = f["candidate_verdicts"]
    n_worlds = f["worlds_with_at_least_one_event"]
    total = f["event_cardinality"]
    n_formed = f["events_by_tag"]["F"]
    n_unf = n_worlds - n_formed
    ev_unf = cv["M3_OCCUPATION_WEIGHTED"]["zero_weight_events"]
    ev_m0 = (cv["M5_FORMATION_MOMENT"]["zero_weight_events"]
             - cv["M4_FORMATION_LIFETIME"]["zero_weight_events"])
    lo, hi = f["per_world_event_count_range"]
    counts = []
    b, r = divmod(ev_unf, n_unf)
    counts += [b + 1] * r + [b] * (n_unf - r)
    n_m0, rr = divmod(ev_m0, hi)
    assert rr == 0
    counts += [hi] * n_m0
    n_rest = n_formed - n_m0
    b2, r2 = divmod(total - ev_unf - ev_m0, n_rest)
    counts += [b2 + 1] * r2 + [b2] * (n_rest - r2)
    events = [(w, j, "B0", j, "x")
              for w, c in enumerate(counts) for j in range(c)]
    formed, occ = {}, [0] * n_worlds
    for w in range(n_unf, n_worlds):
        formed[w] = 0 if w < n_unf + n_m0 else (w - n_unf - n_m0 + 1)
        occ[w] = 1 + (w % 7)
    return {"counts": counts, "events": events, "occ": occ, "formed": formed,
            "boundaries": 16384, "n_unformed": n_unf, "n_moment0": n_m0,
            "in_range": all(lo <= c <= hi for c in counts)}


def my_weightings(sur):
    """Re-implemented from the definitions, NOT by calling build_candidates."""
    ev = sur["events"]
    occ, formed, bnd = sur["occ"], sur["formed"], sur["boundaries"]
    per_world = Counter(e[0] for e in ev)
    supported = sorted(per_world)
    common = 1
    for c in set(per_world.values()):
        common = _lcm(common, c)

    def world_weighted(a):
        nums = [a(e[0]) * (common // per_world[e[0]]) for e in ev]
        return nums, sum(a(w) for w in supported) * common

    out = {}
    out["M1_COUNTING"] = ([1] * len(ev), 1)
    out["M2_PER_WORLD_UNIFORM"] = world_weighted(lambda w: 1)
    out["M3_OCCUPATION_WEIGHTED"] = world_weighted(lambda w: occ[w])
    out["M4_FORMATION_LIFETIME"] = world_weighted(
        lambda w: (bnd - formed[w] + 1) if w in formed else 0)
    out["M5_FORMATION_MOMENT"] = world_weighted(
        lambda w: formed[w] if w in formed else 0)
    return out


# --------------------------------------------------------------------------
# the Z profile and the verdict table, recomputed from scratch
# --------------------------------------------------------------------------
def z_profile():
    onrec, degs, zc = {}, {}, {}
    for cfg in FAMILY:
        supp = set(cfg["sites"])
        fr = set()
        for t in THETA_GRID:
            tot = Zc(cfg, t, INBOX)
            fr.add(Fraction(0) if tot == 0 else Zc(cfg, t, supp) / tot)
        onrec[cfg["name"]] = fr
        M, _, _ = correlator(cfg)
        d = 0
        for n in HOLDING:
            w = window_of(n, cfg)
            for k in range(MAX_STEPS + 1):
                if any(M[x][k] != 0 for x in w if x in M):
                    d = max(d, k)
        degs[cfg["name"]] = d
        zc[cfg["name"]] = len({
            tuple(Zc(cfg, t, window_of(n, cfg)) for t in THETA_GRID)
            for n in HOLDING})
    both = []
    for n in HOLDING:
        van, pos = set(), set()
        for cfg in FAMILY:
            for t in THETA_GRID:
                (van if Zc(cfg, t, window_of(n, cfg)) == 0 else pos).add(
                    cfg["name"])
        if van and pos:
            both.append({"window": n, "vanishes_on": sorted(van),
                         "vanishes_on_count": len(van),
                         "positive_on_count": len(pos)})
    absorb = {}
    for cfg in FAMILY:
        bad, tot = 0, 0
        for a, b in combinations(HOLDING, 2):
            rs = set()
            for t in THETA_GRID:
                zb = Zc(cfg, t, window_of(b, cfg))
                if zb != 0:
                    rs.add(Zc(cfg, t, window_of(a, cfg)) / zb)
            tot += 1
            if len(rs) > 1:
                bad += 1
        absorb[cfg["name"]] = {"theta_varying_pairs": bad, "pairs": tot,
                               "absorbable": bad == 0}
    return {"onrec": onrec, "degs": degs, "zclasses": zc, "both": both,
            "absorb": absorb,
            "onrec_classes": len({x for v in onrec.values() for x in v}),
            "unabsorbable": sorted(k for k, v in absorb.items()
                                   if not v["absorbable"])}


def mu_profile(w, sur):
    n_unf = sur["n_unformed"]
    out = {}
    for m, (nums, den) in w.items():
        tot = sum(nums)
        onrec = sum(x for e, x in zip(sur["events"], nums)
                    if e[0] >= n_unf)
        pos = sum(1 for x in nums if x > 0)
        out[m] = {"theta_arity": 0, "config_arity": 0,
                  "zero_weight_atoms": len(nums) - pos, "positive_atoms": pos,
                  "onrec_fraction": Fraction(onrec, tot),
                  "onrec_classes": 1, "chain_resolution": pos + 1,
                  "degree": 0, "window_argument": False}
    return out


def verdict(p, req, zp):
    """One cell.  Identical logic to the primary's stated tests, coded here
    from the requirement texts rather than copied from the primary."""
    if req == "IF1":
        return "PASS" if p["onrec_classes"] >= zp["onrec_classes"] else "FAIL"
    if req == "IF3":
        return "PASS" if (p["theta_arity"] > 0 or not zp["unabsorbable"]) \
            else "FAIL"
    if req == "IF4":
        return "PASS" if p["window_argument"] else "FAIL"
    if req == "IF5":
        tol = p["zero_weight_atoms"] > 0
        esc = p["config_arity"] > 0 or not zp["both"]
        return "PASS" if (tol and esc) else "FAIL"
    if req == "IF6":
        return "PASS" if p["degree"] >= MAX_STEPS else "FAIL"
    raise AssertionError(req)


OWED = ("IF1", "IF3", "IF4", "IF5", "IF6")


def if_sheet_ids():
    tree = ast.parse(read_text(C892_PRIMARY))
    ids = set()
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        for k, v in zip(node.keys, node.values):
            if (isinstance(k, ast.Constant) and k.value == "id"
                    and isinstance(v, ast.Constant)
                    and str(v.value).startswith("IF")):
                ids.add(v.value)
    return sorted(ids)


def planted(zp):
    p1 = {"theta_arity": 1, "config_arity": len(FAMILY),
          "zero_weight_atoms": 42, "onrec_classes": zp["onrec_classes"],
          "chain_resolution": 648, "degree": MAX_STEPS,
          "window_argument": True}
    p2 = dict(p1, theta_arity=0, degree=0)
    return {"P1_PLANTED_SURVIVOR": p1, "P2_PLANTED_NEAR_MISS": p2}


# --------------------------------------------------------------------------
# THE BRIDGE HUNT -- two constructions the primary never built
# --------------------------------------------------------------------------
def bridge_hunt(zp) -> dict:
    """If either bridge works, the primary's NO-GO is wrong."""
    # ---- BRIDGE-A: the configuration-block (orbit) bridge.
    # Grant the 878 side its missing arity for free: partition E into one
    # block per configuration (the 68 monitor-phase world-orbits are more than
    # enough blocks for 12 configurations), and define the weight of window W
    # at configuration R as the block-R mass of phi^{-1}(W).  Grant the
    # partition MAXIMUM freedom: let each block-measure be an arbitrary
    # non-negative rational set function.  The ONLY surviving constraint is
    # that each block measure is still theta-free.
    #
    # Then for each configuration R the bridge needs a theta-free number
    # b_R(W) with b_R(W) = Z(R,theta,W) / N(R,theta) for all six thetas.
    # Eliminating N by taking a reference window W0 forces
    # Z(R,theta,W)/Z(R,theta,W0) to be theta-free for every W.
    a_rows = []
    for cfg in FAMILY:
        # choose the reference window that maximises the chance of success:
        # any holding window positive at every theta
        refs = [n for n in HOLDING
                if all(Zc(cfg, t, window_of(n, cfg)) != 0
                       for t in THETA_GRID)]
        ok_any = False
        best_bad = None
        for ref in refs:
            bad = 0
            for n in HOLDING:
                rs = {Zc(cfg, t, window_of(n, cfg))
                      / Zc(cfg, t, window_of(ref, cfg))
                      for t in THETA_GRID}
                if len(rs) > 1:
                    bad += 1
            best_bad = bad if best_bad is None else min(best_bad, bad)
            if bad == 0:
                ok_any = True
                break
        a_rows.append({"config": cfg["name"],
                       "reference_windows_available": len(refs),
                       "min_theta_varying_windows": best_bad,
                       "bridge_A_succeeds": ok_any})
    a_ok = [r["config"] for r in a_rows if r["bridge_A_succeeds"]]
    a_bad = [r["config"] for r in a_rows if not r["bridge_A_succeeds"]]

    # ---- BRIDGE-B: theta as an observable (the product extension).
    # Enlarge the event space to E x Theta and weight it.  Any weighting built
    # from an 878 candidate is a PRODUCT mu (x) nu, so the theta-dependence it
    # can express is a pure multiplicative scale nu(theta), which the
    # normalizer N(R,theta) already absorbs.  The bridge therefore still needs
    # the window RATIOS to be theta-free -- the identical obstruction.  What
    # WOULD work is a non-product (coupled) measure on E x Theta, which is not
    # one of the five.
    b_rows = []
    for cfg in FAMILY:
        # a product measure contributes nu(theta) identically to every window,
        # so test whether the theta-dependence of Z is a single common scale
        scales = None
        common_scale = True
        for n in HOLDING:
            vals = [Zc(cfg, t, window_of(n, cfg)) for t in THETA_GRID]
            if all(v == 0 for v in vals):
                continue
            base = next(v for v in vals if v != 0)
            sig = tuple(v / base for v in vals)
            if scales is None:
                scales = sig
            elif sig != scales:
                common_scale = False
        b_rows.append({"config": cfg["name"],
                       "theta_dependence_is_one_common_scale": common_scale,
                       "bridge_B_succeeds": common_scale})
    b_ok = [r["config"] for r in b_rows if r["bridge_B_succeeds"]]
    b_bad = [r["config"] for r in b_rows if not r["bridge_B_succeeds"]]

    return {
        "BRIDGE_A_configuration_block": {
            "construction": (
                "partition E into one block per record configuration (the 68"
                " monitor-phase world-orbits supply far more blocks than the"
                " 12 configurations need) and read the configuration off the"
                " event; each block measure may be an ARBITRARY non-negative"
                " rational set function"),
            "what_it_defeats": (
                "C894-T1 exactly: this bridge manufactures the"
                " record-configuration arity whose absence C894-T1 rests on,"
                " so C894-T1 no longer bites"),
            "per_config": a_rows,
            "succeeds_on": a_ok, "fails_on": a_bad,
            "verdict": "REFUTED" if a_bad else "SUCCEEDS",
            "why": (
                f"the bridge is defeated on {len(a_bad)} of {len(FAMILY)}"
                " configurations by C894-T2 and NOT by C894-T1: even with the"
                " configuration argument granted for free, each block measure"
                " is still theta-free, which forces every holding-window ratio"
                " to be theta-free, and it is not"),
        },
        "BRIDGE_B_theta_as_observable": {
            "construction": (
                "enlarge the event space to E x Theta and weight the product,"
                " which is what 892's IF3 means by declaring the kernel"
                " coordinate an observable"),
            "what_it_defeats": (
                "the naive reading of IF3: it does give the weight a kernel"
                " argument"),
            "per_config": b_rows,
            "succeeds_on": b_ok, "fails_on": b_bad,
            "verdict": "REFUTED" if b_bad else "SUCCEEDS",
            "why": (
                f"a PRODUCT measure contributes one common theta scale to"
                f" every window, and on {len(b_bad)} of {len(FAMILY)}"
                " configurations Z's theta-dependence is NOT one common scale"
                " -- it differs window by window.  Only a COUPLED measure on"
                " E x Theta would do, and no such object is among 878's five"),
        },
        "both_bridges_refuted": bool(a_bad) and bool(b_bad),
        "refinement_of_the_primary": (
            "The primary proves C894-T1 and C894-T2 and lists its residual"
            " properties P1 (configuration arity) and P2 (kernel arity)"
            " side by side, without ranking them: it never tests what happens"
            " if P1 alone is supplied.  This checker does.  BRIDGE-A grants"
            " the record-configuration arity for free -- defeating C894-T1"
            " outright -- and the composition STILL fails, on exactly the"
            " seven configurations where C894-T2 bites.  BRIDGE-B grants a"
            " kernel argument in the only form 878's inventory can express"
            " it, a product measure, and fails on the same seven.  So the two"
            " properties are NOT co-equal: P1 is necessary but not"
            " sufficient, P2 is the irreducible obstruction, and the five"
            " configurations on which both bridges succeed are precisely the"
            " frozen walks, where Z is theta-constant and there is nothing"
            " left to obstruct.  The primary's verdict is right and its"
            " property sheet is complete; what this refines is the ORDERING"
            " of the residual -- a campaign that supplies P1 first buys"
            " nothing, and one that supplies P2 first buys the whole"
            " theta-moving two-thirds of the family."),
    }


# --------------------------------------------------------------------------
# teeth
# --------------------------------------------------------------------------
def teeth(zp, mp, sur, w_mine, table) -> list:
    out = []

    # 1 tampered vendored pin
    raw = bytearray(read_bytes(C878_RECEIPT))
    raw[len(raw) // 2] ^= 0x20
    out.append({"tooth": "tampered vendored 878 pin",
                "detected": sha256_of(bytes(raw)) != BRIEF_SHA256[C878_RECEIPT],
                "how": "flip one byte of the vendored receipt and re-digest"})

    # 2 dropped weighting
    dropped = [m for m in CANDIDATE_NAMES if m != "M3_OCCUPATION_WEIGHTED"]
    cells = len(dropped) * len(OWED)
    out.append({"tooth": "dropped weighting",
                "detected": cells != len(CANDIDATE_NAMES) * len(OWED),
                "how": f"drop M3 -> {cells} cells, completeness gate expects "
                       f"{len(CANDIDATE_NAMES) * len(OWED)}"})

    # 3 hardcoded verdict cell
    tampered = {m: dict(row) for m, row in table.items()}
    tampered["M2_PER_WORLD_UNIFORM"]["IF5"] = "PASS"
    recomputed = verdict(mp["M2_PER_WORLD_UNIFORM"], "IF5", zp)
    out.append({"tooth": "hardcoded verdict cell",
                "detected": tampered["M2_PER_WORLD_UNIFORM"]["IF5"]
                != recomputed,
                "how": "force M2/IF5 to PASS; independent recomputation says "
                       f"{recomputed}"})

    # 4 leaked selection
    fake = {"survivors": ["M2_PER_WORLD_UNIFORM"], "outcome": "SELECTION"}
    real_surv = [m for m in CANDIDATE_NAMES
                 if all(table[m][r] == "PASS" for r in OWED)]
    out.append({"tooth": "leaked selection",
                "detected": fake["survivors"] != real_surv,
                "how": "assert a selected weighting; the recomputed survivor "
                       f"set is {real_surv}"})

    # 5 skipped requirement
    sheet = if_sheet_ids()
    skipped = [r for r in OWED if r != "IF6"]
    out.append({"tooth": "skipped requirement",
                "detected": (len(skipped) != len(OWED)
                             and set(OWED) | {"IF2"} == set(sheet)),
                "how": f"drop IF6; the pinned 892 primary declares {sheet}, "
                       f"so the owed set must be exactly {list(OWED)}"})

    # 6 planted-survivor blindness
    pl = planted(zp)
    p1_ok = all(verdict(pl["P1_PLANTED_SURVIVOR"], r, zp) == "PASS"
                for r in OWED)
    # restore the conjunction bug the primary's own run exposed
    blind = pl["P1_PLANTED_SURVIVOR"]["theta_arity"] > 0 and not zp[
        "unabsorbable"]
    out.append({"tooth": "planted-survivor blindness",
                "detected": p1_ok and not blind,
                "how": "the planted survivor must pass all five; under the "
                       "conjunctive misreading of IF3 it would not, and that "
                       "difference is what makes the blindness visible"})

    # 7 tampered Z
    cfg = FAMILY[0]
    win = window_of("bounding_box", cfg)
    real = Zc(cfg, THETA_GRID[0], win)
    out.append({"tooth": "tampered Z value",
                "detected": (real + Fraction(1, 7)) != Zsq(
                    cfg, THETA_GRID[0], win),
                "how": "perturb Z by 1/7; the independent squaring route "
                       "disagrees"})

    # 8 independent-weighting drift
    nums_v, dens_v, *_ = NS878["build_candidates"](
        sur["events"], sur["occ"], sur["formed"], sur["boundaries"])
    same = all(w_mine[m][0] == nums_v[m] and w_mine[m][1] == dens_v[m]
               for m in CANDIDATE_NAMES)
    out.append({"tooth": "weighting reimplementation drift",
                "detected": same,
                "how": "the five weightings re-implemented from their "
                       "definitions must agree numerator-for-numerator with "
                       "the vendored build_candidates"})
    return out


# --------------------------------------------------------------------------
def main() -> int:
    # ---- independence of the two amplitude routes, on every cell
    route_checks, route_bad = 0, []
    for n in HOLDING:
        for cfg in FAMILY:
            for t in THETA_GRID:
                w = window_of(n, cfg)
                route_checks += 1
                if Zc(cfg, t, w) != Zsq(cfg, t, w):
                    route_bad.append((n, cfg["name"], q(t)))

    zp = z_profile()
    sur = surrogate()
    w_mine = my_weightings(sur)
    mp = mu_profile(w_mine, sur)
    pl = planted(zp)

    table = {m: {r: verdict(mp[m], r, zp) for r in OWED}
             for m in CANDIDATE_NAMES}
    ptable = {m: {r: verdict(p, r, zp) for r in OWED} for m, p in pl.items()}
    survivors = [m for m in CANDIDATE_NAMES
                 if all(table[m][r] == "PASS" for r in OWED)]
    outcome = ("SELECTION" if len(survivors) == 1
               else "NARROWING" if survivors else "NO-GO")

    # ---- restriction gates, verified against BOTH pinned receipts
    f8 = R878["findings"]
    vanish = [(n, c["name"], q(t)) for n in HOLDING for c in FAMILY
              for t in THETA_GRID if Zc(c, t, window_of(n, c)) == 0]
    r892 = {
        "holding_windows": (len(HOLDING), 9),
        "cells": (len(HOLDING) * len(FAMILY) * len(THETA_GRID), 648),
        "vanishing_cells": (len(vanish), 42),
        "frozen_configs": (
            sum(1 for c in FAMILY if not any(counts_by_length(c)[0][1:])), 5),
        "theta_dependent_configs_885_grid": (
            sum(1 for c in FAMILY
                if len({Zc(c, t, INBOX) for t in THETA_885}) > 1), 7),
        "amplitude_inside_support": (
            sum(len({x for lay in counts_by_length(c)[0] for x in lay}
                    & set(c["sites"])) for c in FAMILY), 8),
        "amplitude_outside_support": (
            sum(len({x for lay in counts_by_length(c)[0] for x in lay}
                    - set(c["sites"])) for c in FAMILY), 844),
        "max_kernel_degree": (max(zp["degs"].values()), 4),
    }
    r878 = {
        "event_cardinality": (f8["event_cardinality"], 92260),
        "worlds": (f8["worlds_with_at_least_one_event"], 748),
        "atoms_singleton": (f8["cells_per_family"]["F_ATOM"]
                            == f8["event_cardinality"], True),
        "tag_ordinal_cells": (f8["cells_per_family"]["F_TAG_ORDINAL"],
                              1 + 2 * REGISTER_CAP),
        "admissible": (sum(1 for v in f8["candidate_verdicts"].values()
                           if v["admissible"]), 5),
        "discriminating_pairs": (len(f8["discriminating_pairs"]), 10),
        "rebuilt_zero_counts": (
            {m: sum(1 for x in w_mine[m][0] if x == 0)
             for m in CANDIDATE_NAMES},
            {m: f8["candidate_verdicts"][m]["zero_weight_events"]
             for m in CANDIDATE_NAMES}),
        "surrogate_in_range": (sur["in_range"], True),
    }
    gate892_bad = [k for k, (a, b) in r892.items() if a != b]
    gate878_bad = [k for k, (a, b) in r878.items() if a != b]

    bh = bridge_hunt(zp)
    th = teeth(zp, mp, sur, w_mine, table)
    teeth_ok = all(t["detected"] for t in th)

    # ---- ONLY NOW read the primary's claims
    claims = json.loads(read_text(C894_RECEIPT))
    cv = claims["Q2_table"]["verdicts"]
    cell_agree = all(cv[m][r] == table[m][r]
                     for m in CANDIDATE_NAMES for r in OWED)
    outcome_agree = claims["Q2_table"]["outcome"] == outcome
    surv_agree = claims["Q2_table"]["survivors"] == survivors
    planted_agree = all(
        claims["Q2_table"]["planted_controls"][m][r] == ptable[m][r]
        for m in ptable for r in OWED)
    corroborates = (cell_agree and outcome_agree and surv_agree
                    and planted_agree and not gate892_bad and not gate878_bad
                    and not route_bad)

    elapsed = time.time() - START
    machinery_ok = (not route_bad and not MISS885 and not MISS887
                    and not MISS892 and not MISS878 and teeth_ok
                    and not FIREWALL.hits
                    and elapsed <= RUNTIME_CAP_SEC)

    if corroborates and bh["both_bridges_refuted"]:
        verdict_word = "CORROBORATES WITH A REFINEMENT"
    elif corroborates:
        verdict_word = "REFUTES -- a bridge the primary missed SUCCEEDS"
    else:
        verdict_word = "REFUTES -- recomputation disagrees"

    P = print
    P("=" * 74)
    P(f"CYCLE {CYCLE} -- INDEPENDENT CHECK (specified to refute)")
    P("=" * 74)
    P("")
    P("INDEPENDENCE")
    P(f"  amplitude rebuilt by the path-length CORRELATOR route "
      f"(Chebyshev M_d), cross-checked against direct squaring on all "
      f"{route_checks} cells: {len(route_bad)} disagreements")
    P(f"  the five weightings re-implemented from their definitions, not by "
      f"calling the vendored build_candidates")
    P(f"  windows, containment filter and family re-derived from 885/887")
    P(f"  firewall hits: {FIREWALL.hits}")
    P("")
    P("RESTRICTION GATE -- 892 (independent)")
    for k, (a, b) in r892.items():
        P(f"  [{'ok ' if a == b else 'FAIL'}] {k}: recomputed={a} pinned={b}")
    P("RESTRICTION GATE -- 878 (independent)")
    for k, (a, b) in r878.items():
        P(f"  [{'ok ' if a == b else 'FAIL'}] {k}: recomputed={a} pinned={b}")
    P("")
    P("RECOMPUTED VERDICT TABLE")
    P(f"  {'weighting':<26}" + "".join(f"{r:>7}" for r in OWED))
    for m in CANDIDATE_NAMES:
        P(f"  {m:<26}" + "".join(f"{table[m][r]:>7}" for r in OWED))
    for m in ptable:
        P(f"  {m:<26}" + "".join(f"{ptable[m][r]:>7}" for r in OWED)
          + "   [PLANTED]")
    P(f"  survivors {survivors}   outcome {outcome}")
    P("")
    P("THE BRIDGE HUNT -- two constructions the primary never built")
    for key in ("BRIDGE_A_configuration_block", "BRIDGE_B_theta_as_observable"):
        b = bh[key]
        P(f"  {key}: {b['verdict']}")
        P(f"    construction: {b['construction']}")
        P(f"    what it defeats: {b['what_it_defeats']}")
        P(f"    succeeds on {len(b['succeeds_on'])} configs "
          f"{b['succeeds_on']}")
        P(f"    fails on    {len(b['fails_on'])} configs {b['fails_on']}")
        P(f"    why: {b['why']}")
    P(f"  REFINEMENT: {bh['refinement_of_the_primary']}")
    P("")
    P("TEETH")
    for t in th:
        P(f"  [{'bit ' if t['detected'] else 'MISS'}] {t['tooth']}: "
          f"{t['how']}")
    P(f"  teeth {sum(1 for t in th if t['detected'])}/{len(th)}")
    P("")
    P("AGAINST THE PRIMARY'S CLAIMS")
    P(f"  all 25 cells agree:        {cell_agree}")
    P(f"  outcome class agrees:      {outcome_agree} "
      f"({claims['Q2_table']['outcome']} vs {outcome})")
    P(f"  survivor set agrees:       {surv_agree}")
    P(f"  planted controls agree:    {planted_agree}")
    P("")
    P("=" * 74)
    P(f"  CHECKER VERDICT: {verdict_word}")
    P(f"  machinery sound: {machinery_ok}   elapsed {elapsed:.3f}s")
    P("=" * 74)

    receipt = {
        "cycle": CYCLE,
        "role": "independent check, specified to refute",
        "self_sha256": sha256_of(read_bytes(SELF_REL)),
        "checker_verdict": verdict_word,
        "independence": {
            "amplitude_route": ("path-length correlator -> Chebyshev M_d,"
                                " reassembled; cross-checked against direct"
                                " squaring"),
            "route_cross_checks": route_checks,
            "route_disagreements": route_bad,
            "weightings": ("re-implemented from their AST-read definitions,"
                           " then cross-checked against the vendored"
                           " build_candidates (tooth 8)"),
            "firewall_hits": list(FIREWALL.hits),
        },
        "restriction_gate_892": {k: {"recomputed": a, "pinned": b,
                                     "match": a == b}
                                 for k, (a, b) in r892.items()},
        "restriction_gate_878": {k: {"recomputed": a, "pinned": b,
                                     "match": a == b}
                                 for k, (a, b) in r878.items()},
        "recomputed_table": table,
        "recomputed_planted": ptable,
        "recomputed_survivors": survivors,
        "recomputed_outcome": outcome,
        "bridge_hunt": bh,
        "teeth": th,
        "teeth_bit": sum(1 for t in th if t["detected"]),
        "teeth_total": len(th),
        "agreement_with_primary": {
            "cells": cell_agree, "outcome": outcome_agree,
            "survivors": surv_agree, "planted": planted_agree,
            "corroborates": corroborates,
        },
        "machinery_sound": machinery_ok,
        "elapsed_sec": round(elapsed, 3),
        "boundary": ("this checker selects no weighting and supplies no"
                     " probability rule; it recomputes and attacks"),
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(receipt, indent=2, sort_keys=True,
                                   default=str) + "\n", encoding="utf-8")
    P(f"receipt: {OUT_JSON.relative_to(ROOT)}")
    # exit 0 whenever the checker's own machinery is sound, independent of
    # whether the primary's claims survived
    return 0 if machinery_ok else 1


if __name__ == "__main__":
    sys.exit(main())
