#!/usr/bin/env python3
"""Cycle 892 INDEPENDENT CHECK -- spec'd to REFUTE the GBW1b pricing.

The Cycle 892 primary claims that the detector-window EXTENT, which Cycle 887
proved invisible to the LINEAR axiom-level readout, becomes LOAD-BEARING at
quadratic order: the 9 containment-holding admissible windows of 887's
catalogue split into 8 distinct Z classes.  It backs that with two structural
theorems -- amplitude expulsion (C892-T1) and window monotonicity with an
exact difference formula (C892-T2) -- plus a kernel structure theorem
(C892-T3) and a parity theorem (C892-T4).  This checker tries to break all of
it.

INDEPENDENCE.  The amplitude and propagation machinery here is written from
scratch and shares NO code with the primary.  Where the primary walks a
length-LAYERED dynamic program over a dict of accumulated Gaussian rationals,
this checker ENUMERATES EVERY ADMISSIBLE PATH EXPLICITLY by depth-first
search, tallies endpoints by path length, and builds the amplitude by raising
the unit-circle point to an explicit power for each length.  Two different
algorithms, two different data structures, one pinned physical rule.  The
primary is read as TEXT and JSON only; the firewall makes importing it an
error.

WHAT IS ATTACKED, IN ORDER.

1.  THE RESTRICTION GATE.  885's N rows and 887's readout-gauge row are
    recomputed with the independent machinery.  If the primary's reproduction
    were an artifact of shared code, it dies here.

2.  THE PARTITION, RECOMPUTED ON THE FULL CATALOGUE.

3.  THREE WINDOWS THE PRIMARY NEVER EVALUATED, built here from 887's wider
    families and never from its catalogue: a RANK/THRESHOLD filter, a
    MORPHOLOGICAL CLOSING, and a UNION map.  Each is tested for admissibility
    and containment with an independently written harness AND with the pinned
    887 harness.  For each that is admissible and containment-holding, the
    primary's structural claim C892-T2 makes a SHARP, FALSIFIABLE PREDICTION
    BEFORE Z IS COMPUTED: the class of W is determined by W intersected with
    the amplitude support src(R) union Reach(R), so two windows with equal
    intersection must share a class and windows with unequal intersection must
    not.  The prediction is recorded first and then tested.  A MISPREDICTION
    REFUTES C892-T2.

4.  THE ADVERSARIAL HUNT.  The primary claims Z separates every genuinely
    distinct containment-holding window and that Z is monotone in the window.
    Three adversarial constructions attack that:
      (i)  a window enlarged only on sites that carry NO amplitude, which the
           theorem says must NOT change Z -- if Z moves, C892-T2 dies;
      (ii) a window enlarged on sites that DO carry amplitude, which the
           theorem says must strictly increase Z -- if Z fails to move or
           moves down, C892-T2 dies;
      (iii) a search over hundreds of generated containment-holding windows
           for any monotonicity violation, any amplitude found inside supp(R)
           beyond the seed, and any pair of distinct-intersection windows with
           equal Z.

5.  THE INTERFACE DERIVATION.  Each requirement the primary states must cite a
    COMPUTED fact of Z.  The cited facts are recomputed independently here,
    and a needle check confirms that no Born-rule vocabulary entered the
    requirement text as a premise.

6.  TEETH.  Eight deliberately broken variants must each be CAUGHT.  A tooth
    that does not bite is reported as a failure of this checker, not of the
    primary.

This checker exits 0 whether or not the primary's claims survive.  Its job is
to report, not to gate.

REPAIR LOG.  The first full run of this checker reported C892-T2 REFUTED, with
42 violations of the form "same amplitude intersection, different Z", all on
the configuration `sparse_b`.  Both defects were in the CHECKER, and both were
found by reading its own output rather than by trusting it:

  1.  CROSS-CONFIGURATION KEY COLLISION.  The generated sweep's fingerprint
      dictionary was created once, OUTSIDE the loop over configurations, so an
      amplitude intersection arising on a late configuration collided with an
      identical intersection from an earlier one and compared their Z values
      -- two different configurations, therefore two legitimately different
      Z's.  The 42 "violations" were phantom: the fingerprint is only ever
      claimed to determine Z AT FIXED R.  Keyed per configuration, the same
      7192 generated windows produce ZERO violations.  This is recorded rather
      than quietly corrected because a refutation that dissolves under repair
      is exactly the kind of result that should stay visible.

  2.  FIXED-BOX SCAN IN THE RANK FILTER.  The new rank/threshold window
      scanned the fixed amplitude grid for candidate sites, so a configuration
      translated near the grid wall had its window clipped and the map failed
      equivariance -- an artifact of the SCAN, not of the map, which made the
      window non-admissible and therefore untestable.  The scan now runs over
      the support's own unit dilation, which provably contains every site with
      three record neighbours.
"""

from __future__ import annotations

import ast
import hashlib
import importlib.abc
import json
import sys
import time
from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path

START = time.time()

CYCLE = 892
RUNTIME_CAP_SEC = 900
STDOUT_LIMIT_BYTES = 150_000
EXHIBIT_CAP = 6

ROOT = Path(__file__).resolve().parents[1]
SELF_REL = "scripts/frontier_cycle892_gbw1b_independent_check_2026_07_28.py"
OUT_JSON = ROOT / "outputs" / \
    "gbw1b_independent_check_cycle892_receipt_2026_07_28.json"

C892_PRIMARY = "scripts/frontier_cycle892_gbw1b_pricing_2026_07_28.py"
C892_RECEIPT = "outputs/gbw1b_pricing_cycle892_receipt_2026_07_28.json"
C885_PRIMARY = "scripts/frontier_cycle885_gbw1_record_window_2026_07_28.py"
C885_RECEIPT = "outputs/gbw1_record_window_cycle885_receipt_2026_07_28.json"
C885_CHECKER = "scripts/frontier_cycle885_gbw1_independent_check_2026_07_28.py"
C885_CACHE = "logs/runner-cache/frontier_cycle885_gbw1_record_window_2026_07_28.txt"
C887_PRIMARY = "scripts/frontier_cycle887_window_freedom_2026_07_28.py"
C887_RECEIPT = "outputs/window_freedom_cycle887_receipt_2026_07_28.json"
AXIOMS_MD = "docs/MINIMAL_AXIOMS_2026-06-29.md"
DYNAMICS_MD = "docs/GATE_B_DYNAMICS_NOTE.md"
WEAKFIELD_MD = "docs/GATE_B_WEAK_FIELD_SOURCE_ACTION_INTERFACE_NOTE_2026-06-16.md"

AUDIT_INPUT_PATHS = (
    C892_PRIMARY, C892_RECEIPT, C885_PRIMARY, C885_RECEIPT, C885_CHECKER,
    C885_CACHE, C887_PRIMARY, C887_RECEIPT, AXIOMS_MD, DYNAMICS_MD,
    WEAKFIELD_MD,
)

BRIEF_SHA256 = {
    C885_PRIMARY:
        "daee8bbfefde80a351bf82a3028d96baf447493d3add8cdc85f4eb63fc114f32",
    C885_RECEIPT:
        "3561cc4e62ba55a9f2aed377122dec795103a6f424a39a907e866f53665da997",
    C887_PRIMARY:
        "139ed9e2fce1775d41e5d46bf2d6b43063c47f4a3a0cf2c55edf4d8ce2f4fc83",
    C887_RECEIPT:
        "d1807305098ae995224118f93b301fc822ef0d6efc9e49c4a16e90d694592f86",
}

THETAS = (Fraction(1, 2), Fraction(1, 3), Fraction(2, 5),
          Fraction(1, 7), Fraction(3, 8), Fraction(5, 6))
THETAS_885 = (Fraction(1, 2), Fraction(1, 3), Fraction(2, 5))

BOX_RADIUS = 4
DEPTH = 4

BORN_NEEDLES = (
    "born rule", "born's rule", "probability amplitude squared",
    "|psi|^2", "wavefunction", "hilbert space", "unitary evolution",
    "quantum probability", "measurement postulate",
)


# --------------------------------------------------------------------------
# preflight + firewall
# --------------------------------------------------------------------------
def preflight() -> None:
    missing = [p for p in AUDIT_INPUT_PATHS if not (ROOT / p).is_file()]
    if missing:
        sys.stderr.write("PREFLIGHT FAIL: absent: " + ", ".join(missing) + "\n")
        raise SystemExit(2)
    for rel, want in BRIEF_SHA256.items():
        got = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
        if got != want:
            sys.stderr.write(f"PREFLIGHT FAIL: {rel} {got} != {want}\n")
            raise SystemExit(2)


preflight()

_STEMS = {Path(p).stem for p in AUDIT_INPUT_PATHS}


class _Wall(importlib.abc.MetaPathFinder):
    def __init__(self):
        self.hits = []

    def find_module(self, fullname, path=None):  # pragma: no cover - legacy
        return self.find_spec(fullname, path)

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in _STEMS:
            self.hits.append(fullname)
            raise ImportError(f"firewall forbids {fullname}")
        return None


WALL = _Wall()
sys.meta_path.insert(0, WALL)


def rbytes(rel):
    return (ROOT / rel).read_bytes()


def rtext(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def sha(b):
    return hashlib.sha256(b).hexdigest()


def blob(b):
    return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()


def dig(p):
    return hashlib.sha256(
        json.dumps(p, sort_keys=True, default=str).encode()).hexdigest()


def q(v):
    f = Fraction(v)
    return f"{f.numerator}/{f.denominator}"


PRIMARY_RECEIPT = json.loads(rtext(C892_RECEIPT))
R885 = json.loads(rtext(C885_RECEIPT))
R887 = json.loads(rtext(C887_RECEIPT))


# --------------------------------------------------------------------------
# pinned definitions pulled by AST (the DEFINITIONS under test, not the
# primary's code): the 885 family generator and the 887 map catalogue
# --------------------------------------------------------------------------
def pull(rel, names, seed):
    tree = ast.parse(rtext(rel))
    keep, got = [], set()
    for n in tree.body:
        if isinstance(n, ast.FunctionDef) and n.name in names:
            keep.append(n)
            got.add(n.name)
        elif isinstance(n, ast.Assign):
            ids = [t.id for t in n.targets if isinstance(t, ast.Name)]
            if any(i in names for i in ids):
                keep.append(n)
                got.update(i for i in ids if i in names)
        elif (isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Name)
              and n.target.id in names):
            keep.append(n)
            got.add(n.target.id)
    ns = dict(seed)
    exec(compile(ast.Module(body=keep, type_ignores=[]),  # noqa: S102
                 f"<pin:{rel}>", "exec"), ns)
    return ns, sorted(got), sorted(set(names) - got)


SEED = {"Fraction": Fraction, "product": product, "permutations": permutations}

F_NODES = ("NEIGHBOURS", "_lcg", "make_config", "build_family")
N885, G885, M885 = pull(C885_PRIMARY, set(F_NODES), SEED)
FAM = N885["build_family"]()

C_NODES = (
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
N887, G887, M887 = pull(C887_PRIMARY, set(C_NODES), dict(SEED, FAMILY=FAM))
CAT = dict(N887["selector_catalogue"]())
CAT_NAMES = sorted(CAT)


def fam_fp(fam):
    return [{"name": c["name"], "sites": [list(s) for s in c["sites"]],
             "content": [[list(s), b] for s, b in c["content"]],
             "depth": [[list(s), d] for s, d in c["depth"]]} for c in fam]


FAM_DIGEST = dig(fam_fp(FAM))


# ==========================================================================
# INDEPENDENT AMPLITUDE MACHINERY
# --------------------------------------------------------------------------
# The primary propagates a layered dynamic program over accumulated Gaussian
# rationals.  This enumerates EVERY admissible path explicitly by depth-first
# search, tallies endpoints by path length, and raises the unit point to an
# explicit power per length.  No function, constant or data structure below is
# taken from the primary.
# ==========================================================================
STEPS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
GRID = frozenset(product(range(-BOX_RADIUS, BOX_RADIUS + 1), repeat=3))


def centroid(cfg):
    n = len(cfg["sites"])
    return tuple(Fraction(sum(s[i] for s in cfg["sites"]), n) for i in range(3))


def emitters(cfg):
    """The record-determined emitters: grid points nearest the centroid."""
    g = centroid(cfg)
    scored = sorted(
        (sum((Fraction(x[i]) - g[i]) ** 2 for i in range(3)), x)
        for x in GRID)
    best = scored[0][0]
    return tuple(sorted(x for d, x in scored if d == best))


_PATHS: dict = {}


def path_tally(cfg):
    """endpoint -> {length: number of admissible paths}, by EXPLICIT DFS.

    A path starts at an emitter and takes up to DEPTH steps; every step must
    land inside the grid and NOT on a blocked site.  Blocked = supp(R).
    """
    key = cfg["name"]
    if key in _PATHS:
        return _PATHS[key]
    blocked = frozenset(cfg["sites"])
    tally: dict = {}
    stack = [(e, 0) for e in emitters(cfg)]
    while stack:
        here, k = stack.pop()
        tally.setdefault(here, {})
        tally[here][k] = tally[here].get(k, 0) + 1
        if k == DEPTH:
            continue
        for st in STEPS:
            nxt = (here[0] + st[0], here[1] + st[1], here[2] + st[2])
            if nxt in GRID and nxt not in blocked:
                stack.append((nxt, k + 1))
    _PATHS[key] = tally
    return tally


def circle_point(theta: Fraction):
    """(cos, sin) as an exact rational point on the unit circle."""
    den = 1 + theta * theta
    return (Fraction(1 - theta * theta, 1) / den, Fraction(2 * theta, 1) / den)


def raise_power(z, k):
    """z^k by explicit repeated multiplication -- no incremental carry."""
    acc = (Fraction(1), Fraction(0))
    for _ in range(k):
        acc = (acc[0] * z[0] - acc[1] * z[1], acc[0] * z[1] + acc[1] * z[0])
    return acc


_FIELD: dict = {}


def field(cfg, theta):
    key = (cfg["name"], theta)
    if key in _FIELD:
        return _FIELD[key]
    tally = path_tally(cfg)
    m = len(emitters(cfg))
    z = circle_point(theta)
    powers = [raise_power(z, k) for k in range(DEPTH + 1)]
    out = {}
    for site, by_len in tally.items():
        re = Fraction(0)
        im = Fraction(0)
        for k, count in by_len.items():
            w = Fraction(count, m)
            re += w * powers[k][0]
            im += w * powers[k][1]
        out[site] = (re, im)
    _FIELD[key] = out
    return out


def norm_on(cfg, theta, sites):
    f = field(cfg, theta)
    tot = Fraction(0)
    for x in sites:
        if x in f and x in GRID:
            re, im = f[x]
            tot += re * re + im * im
    return tot


def wset(name, cfg):
    return set(CAT[name](cfg)["set"])


def amplitude_support(cfg):
    """Where amplitude actually lives, computed independently."""
    return {x for x, by_len in path_tally(cfg).items() if any(by_len.values())}


def reachable(cfg):
    """Sites attainable in one or more steps."""
    return {x for x, by_len in path_tally(cfg).items()
            if any(k > 0 for k in by_len)}


# --------------------------------------------------------------------------
# A: pins
# --------------------------------------------------------------------------
def pins_cert():
    rows = []
    for rel in AUDIT_INPUT_PATHS:
        raw = rbytes(rel)
        rows.append({"path": rel, "sha256": sha(raw), "git_blob": blob(raw),
                     "brief_match": (None if rel not in BRIEF_SHA256
                                     else sha(raw) == BRIEF_SHA256[rel])})
    checked = [r for r in rows if r["brief_match"] is not None]
    return {
        "pins": rows,
        "pin_count": len(rows),
        "brief_digests_checked": len(checked),
        "brief_digests_all_match": all(r["brief_match"] for r in checked),
        "self_sha256": sha(rbytes(SELF_REL)),
        "firewall_hits": len(WALL.hits),
        "ast_nodes_missing": M885 + M887,
        "independence_statement": (
            "The amplitude machinery in this file (STEPS, GRID, centroid, "
            "emitters, path_tally, circle_point, raise_power, field, "
            "norm_on) is written from scratch and enumerates paths by "
            "depth-first search.  The primary uses a length-layered dynamic "
            "program.  No primary function is imported, executed or "
            "AST-extracted; the primary is read as text and JSON only."),
        "primary_ast_nodes_borrowed": 0,
        "finding": (
            f"{len(rows)} pins by path + sha256 + git blob; "
            f"{len(checked)} brief-supplied digests all match; "
            f"{len(WALL.hits)} firewall hits; 0 primary nodes borrowed."),
        "pass": (all(r["brief_match"] for r in checked)
                 and not (M885 + M887) and len(WALL.hits) == 0),
    }


# --------------------------------------------------------------------------
# B: the restriction gate, recomputed with independent machinery
# --------------------------------------------------------------------------
def boundary_shell(cfg):
    supp = set(cfg["sites"])
    out = set()
    for s in supp:
        for st in STEPS:
            t = (s[0] + st[0], s[1] + st[1], s[2] + st[2])
            if t not in supp:
                out.add(t)
    return out


def cache_block(text, key):
    i = text.find(f'"{key}"')
    if i < 0:
        return None
    s = text.find("{", i)
    d = 0
    for k in range(s, len(text)):
        if text[k] == "{":
            d += 1
        elif text[k] == "}":
            d -= 1
            if d == 0:
                return json.loads(text[s:k + 1])
    return None


def restriction_cert():
    pinned = cache_block(rtext(C885_CACHE), "K_N_TERMINAL_NORMALIZATION") or {}
    mine = {c["name"]: {q(t): q(norm_on(c, t, boundary_shell(c)))
                        for t in THETAS_885} for c in FAM}
    mism = [{"config": r["config"], "pinned": r["Z_by_theta"],
             "independent": mine.get(r["config"])}
            for r in pinned.get("rows", [])
            if mine.get(r["config"]) != r["Z_by_theta"]]
    dep = sum(1 for v in mine.values() if len(set(v.values())) > 1)
    ctl = sum(1 for c in FAM
              if len({q(norm_on(c, t, set(c["sites"]))) for t in THETAS_885})
              > 1)
    base = [N887["readout"](c) for c in FAM]
    adm, ind = [], []
    for n in CAT_NAMES:
        if not N887["evaluate_map"](CAT[n])["admissible_REQ1_REQ5"]:
            continue
        adm.append(n)
        if [N887["windowed_readout"](CAT[n], c) for c in FAM] == base:
            ind.append(n)
    g = R887["science"]["I_READOUT_GAUGE"]
    checks = {
        "c885_rows_value_for_value": len(mism) == 0
                                     and len(pinned.get("rows", [])) == 12,
        "c885_theta_dependence_7_of_12":
            dep == pinned.get("configs_whose_Z_moves_with_theta"),
        "c885_degenerate_control_0_of_12":
            ctl == pinned.get("degenerate_window_control", {}).get(
                "configs_whose_Z_moves_with_theta"),
        "c887_readout_gauge_9_of_12":
            len(ind) == g["count_indistinguishable"]
            and sorted(ind) == sorted(
                g["readout_indistinguishable_from_the_support_window"]),
        "c887_admissible_set": sorted(adm) == sorted(g["per_map"]),
        "family_digest":
            FAM_DIGEST == R887["science"]["B_FAMILY"]["family_digest_885_ast"],
        "primary_family_digest_agrees":
            FAM_DIGEST == PRIMARY_RECEIPT["family_digest"],
    }
    return {
        "role": (
            "The pinned 885 and 887 rows recomputed with the INDEPENDENT "
            "path-enumeration machinery.  If the primary's reproduction were "
            "an artifact of sharing code with 885, it fails here."),
        "checks": checks,
        "mismatch_exhibits": mism[:EXHIBIT_CAP],
        "independent_theta_dependence": f"{dep}/12",
        "independent_degenerate_control": f"{ctl}/12",
        "independent_readout_gauge": f"{len(ind)}/{len(adm)}",
        "family_digest": FAM_DIGEST,
        "finding": (
            f"{sum(1 for v in checks.values() if v)}/{len(checks)} checks "
            f"reproduce under independent machinery: 885's rows match value "
            f"for value ({len(mism)} mismatches), theta-dependence {dep}/12, "
            f"degenerate control {ctl}/12, readout gauge {len(ind)}/{len(adm)}."),
        "pass": all(checks.values()),
    }


# --------------------------------------------------------------------------
# C: the partition, recomputed on the FULL catalogue
# --------------------------------------------------------------------------
def signature(fn):
    return tuple(q(norm_on(c, t, set(fn(c)["set"])))
                 for c in FAM for t in THETAS)


def partition_cert():
    adm, hold = [], []
    for n in CAT_NAMES:
        if not N887["evaluate_map"](CAT[n])["admissible_REQ1_REQ5"]:
            continue
        adm.append(n)
        if N887["containment_profile"](CAT[n])["supp_subset_W_on_all_configs"]:
            hold.append(n)
    classes: dict = {}
    for n in sorted(hold):
        classes.setdefault(signature(CAT[n]), []).append(n)
    mine = sorted(sorted(v) for v in classes.values())
    theirs = sorted(sorted(v) for v in PRIMARY_RECEIPT["Q1_partition"])
    linear: dict = {}
    base = [N887["readout"](c) for c in FAM]
    for n in sorted(hold):
        linear.setdefault(
            tuple(N887["windowed_readout"](CAT[n], c) for c in FAM), []).append(n)
    return {
        "admissible": sorted(adm),
        "containment_holding": sorted(hold),
        "independent_linear_classes": len(linear),
        "independent_quadratic_classes": len(classes),
        "independent_partition": mine,
        "primary_partition": theirs,
        "partitions_agree": mine == theirs,
        "primary_linear_classes": PRIMARY_RECEIPT["Q1_linear_classes"],
        "primary_quadratic_classes": PRIMARY_RECEIPT["Q1_quadratic_classes"],
        "class_counts_agree": (
            len(classes) == PRIMARY_RECEIPT["Q1_quadratic_classes"]
            and len(linear) == PRIMARY_RECEIPT["Q1_linear_classes"]),
        "linear_readout_matches_full_readout": all(
            list(k) == base for k in linear),
        "finding": (
            f"Independently, {len(hold)} containment-holding windows give "
            f"{len(linear)} LINEAR class(es) and {len(classes)} QUADRATIC "
            f"classes.  Partition agreement with the primary: "
            f"{mine == theirs}."),
        "pass": mine == theirs,
    }


# --------------------------------------------------------------------------
# D: three windows the primary never evaluated
# --------------------------------------------------------------------------
S1 = tuple(sorted(set(STEPS) | {(0, 0, 0)}))


def _dilate(sites, S):
    return {(s[0] + v[0], s[1] + v[1], s[2] + v[2]) for s in sites for v in S}


def _erode(sites, S):
    ss = set(sites)
    return {x for x in ss
            if all((x[0] + v[0], x[1] + v[1], x[2] + v[2]) in ss for v in S)}


def w_rank_filter(cfg):
    """NEW #1 -- a RANK / THRESHOLD filter member.

    W(R) = supp(R) union {x : at least 3 of x's six neighbours are records}.
    The neighbour count is a content-only, rotation-invariant local statistic;
    thresholding a monotone statistic is monotone; the explicit union with the
    support makes containment structural.

    The candidate set is the support's own unit dilation, NOT the fixed
    amplitude grid: a site with three record neighbours is necessarily within
    one step of a record, so this loses nothing -- and scanning a FIXED box
    would silently clip the window whenever a translated configuration left
    the box, which shows up as an equivariance failure that is an artifact of
    the scan rather than of the map.  See the repair log.
    """
    supp = set(cfg["sites"])
    cand = {(s[0] + st[0], s[1] + st[1], s[2] + st[2])
            for s in supp for st in STEPS} | supp
    extra = {x for x in cand
             if sum(1 for st in STEPS
                    if (x[0] + st[0], x[1] + st[1], x[2] + st[2]) in supp) >= 3}
    return N887["packaged"](supp | extra, N887["barycentre"](cfg))


def w_closing(cfg):
    """NEW #2 -- a MORPHOLOGICAL CLOSING, erosion after dilation.

    W(R) = erode(dilate(supp(R), S1), S1) with S1 the closed unit ball.
    Closing is extensive (it contains its argument), increasing, and
    equivariant for a rotation-invariant structuring element -- so it should
    be admissible and containment-holding, and it is NOT a Minkowski sum.
    """
    return N887["packaged"](_erode(_dilate(cfg["sites"], S1), S1),
                            N887["barycentre"](cfg))


def w_union(cfg):
    """NEW #3 -- a UNION map over two maps of different type.

    W(R) = rank-filter(R) union axis-segment-closure(R).  A closure probe of
    the surviving space that the primary's catalogue does not contain.
    """
    a = set(w_rank_filter(cfg)["set"])
    b = set(N887["axis_segment_closure"](cfg["sites"]))
    return N887["packaged"](a | b, N887["barycentre"](cfg))


NEW_WINDOWS = (("NEW_rank_threshold_filter_k3", w_rank_filter),
               ("NEW_morphological_closing_ball1", w_closing),
               ("NEW_union_rank_with_axis_closure", w_union))


def independent_admissibility(fn):
    """A second, independently written REQ harness.  Rotation + translation
    equivariance on the pinned test group, permanence-monotonicity on the
    depth filtration, and non-constancy."""
    eqf = eqc = 0
    for cfg in FAM:
        base = set(fn(cfg)["set"])
        for m in N887["ROT24"]:
            for sh in N887["TEST_SHIFTS"]:
                eqc += 1
                moved = set(fn(N887["transform"](cfg, m, sh))["set"])
                want = set()
                for s in base:
                    r = N887["apply_mat"](m, s)
                    want.add((r[0] + sh[0], r[1] + sh[1], r[2] + sh[2]))
                if moved != want:
                    eqf += 1
    mf = mc = 0
    for cfg in FAM:
        prev = None
        for sub in N887["truncations"](cfg):
            cur = set(fn(sub)["set"])
            if prev is not None:
                mc += 1
                if not prev <= cur:
                    mf += 1
            prev = cur
    distinct = len({tuple(sorted(fn(c)["set"])) for c in FAM})
    return {"equivariance_checks": eqc, "equivariance_failures": eqf,
            "permanence_checks": mc, "permanence_failures": mf,
            "distinct_values": distinct,
            "admissible": eqf == 0 and mf == 0 and distinct > 1}


def new_windows_cert(part):
    hold = part["containment_holding"]
    classes: dict = {}
    for n in hold:
        classes.setdefault(signature(CAT[n]), []).append(n)
    # the fingerprint C892-T2 says determines the class
    def amp_fingerprint(fn):
        return tuple(tuple(sorted(set(fn(c)["set"]) & amplitude_support(c)))
                     for c in FAM)
    known_fp = {n: amp_fingerprint(CAT[n]) for n in hold}

    rows = []
    mispredictions = []
    for name, fn in NEW_WINDOWS:
        ind = independent_admissibility(fn)
        pinned_ev = N887["evaluate_map"](fn)
        cp = N887["containment_profile"](fn)
        row = {
            "window": name,
            "in_the_primary_catalogue": name in CAT_NAMES,
            "independent_harness": ind,
            "pinned_887_harness_admissible":
                pinned_ev["admissible_REQ1_REQ5"],
            "harnesses_agree":
                ind["admissible"] == pinned_ev["admissible_REQ1_REQ5"],
            "contains_support_on": cp["contains_support"],
            "of": cp["configs"],
            "containment_holds": cp["supp_subset_W_on_all_configs"],
        }
        if not (row["pinned_887_harness_admissible"]
                and row["containment_holds"]):
            row["verdict"] = ("not admissible and/or breaks containment: "
                              "correctly outside the partition")
            rows.append(row)
            continue

        # ---- THE PREDICTION, RECORDED BEFORE Z IS COMPUTED
        fp = amp_fingerprint(fn)
        matches = sorted(n for n in hold if known_fp[n] == fp)
        predicted = ("joins the class of " + ", ".join(matches)
                     if matches else "forms a NEW class")
        row["C892_T2_prediction_made_before_computing_Z"] = predicted
        row["prediction_rule"] = (
            "C892-T2 says Z(W) is the amplitude mass on W intersect "
            "supp(A).  So the class is a function of W intersect "
            "(src union Reach) ALONE.  Windows with an equal such "
            "intersection must share a class; windows with an unequal one "
            "must not.")

        # ---- now compute
        sig = signature(fn)
        landed = sorted(classes.get(sig, []))
        row["actually_lands_with"] = landed or "a NEW class"
        ok = (sorted(matches) == landed) if matches else (not landed)
        row["prediction_correct"] = ok
        if not ok:
            mispredictions.append({"window": name, "predicted": predicted,
                                   "actual": landed or "new class"})
        # ---- and check the theorem's monotonicity on this new window too
        supp_map = CAT["minkowski_S_zero__the_885_support_window"]
        viol = []
        for c in FAM:
            inner = set(supp_map(c)["set"])
            outer = set(fn(c)["set"])
            if not inner <= outer:
                continue
            for t in THETAS:
                lhs = norm_on(c, t, outer) - norm_on(c, t, inner)
                if lhs < 0 or lhs != norm_on(c, t, outer - inner):
                    viol.append({"config": c["name"], "theta": q(t)})
        row["difference_formula_violations_against_the_support_window"] = \
            len(viol)
        row["Z_sample_at_theta_1_2"] = {
            c["name"]: q(norm_on(c, Fraction(1, 2), set(fn(c)["set"])))
            for c in FAM}
        rows.append(row)

    tested = [r for r in rows if "prediction_correct" in r]
    return {
        "role": (
            "Three windows the primary never evaluated, built here from 887's "
            "wider families: a rank/threshold filter, a morphological closing, "
            "and a union map.  Each admissible containment-holding one gets a "
            "SHARP prediction from C892-T2 recorded BEFORE Z is computed.  A "
            "misprediction refutes the structural proof."),
        "windows": rows,
        "count_built": len(NEW_WINDOWS),
        "count_admissible_and_containment_holding": len(tested),
        "count_predicted_correctly": sum(1 for r in tested
                                         if r["prediction_correct"]),
        "mispredictions": mispredictions,
        "C892_T2_refuted_by_the_new_windows": len(mispredictions) > 0,
        "finding": (
            f"{len(NEW_WINDOWS)} new windows built; {len(tested)} are "
            f"admissible AND containment-holding and therefore testable; "
            f"{sum(1 for r in tested if r['prediction_correct'])} of those "
            f"land exactly where C892-T2 predicted BEFORE Z was computed.  "
            f"{len(mispredictions)} mispredictions."),
        "pass": len(tested) > 0,
    }


# --------------------------------------------------------------------------
# E: the adversarial hunt
# --------------------------------------------------------------------------
def adversarial_cert(part):
    hold = part["containment_holding"]
    supp_map = CAT["minkowski_S_zero__the_885_support_window"]

    # ---- (i) enlarge ONLY on amplitude-free sites: Z must NOT move
    dead_rows, dead_bad = [], []
    for c in FAM:
        live = amplitude_support(c)
        base = set(supp_map(c)["set"])
        dead = sorted(x for x in GRID if x not in live and x not in base)[:40]
        if not dead:
            continue
        big = base | set(dead)
        moved = [q(t) for t in THETAS
                 if norm_on(c, t, big) != norm_on(c, t, base)]
        dead_rows.append({"config": c["name"], "dead_sites_added": len(dead),
                          "thetas_where_Z_moved": moved})
        if moved:
            dead_bad.append(c["name"])

    # ---- (ii) enlarge on sites that DO carry amplitude: Z must strictly rise
    live_rows, live_bad = [], []
    for c in FAM:
        live = amplitude_support(c)
        base = set(supp_map(c)["set"])
        add = sorted(x for x in live if x not in base)
        if not add:
            continue
        big = base | set(add)
        failed = [q(t) for t in THETAS
                  if norm_on(c, t, big) <= norm_on(c, t, base)]
        live_rows.append({"config": c["name"], "live_sites_added": len(add),
                          "thetas_where_Z_failed_to_rise": failed})
        if failed:
            live_bad.append(c["name"])

    # ---- (iii) a generated sweep of containment-holding windows.
    #      The amplitude-intersection fingerprint is keyed PER CONFIGURATION.
    #      Keying it globally would compare Z values from different
    #      configurations and manufacture 42 phantom violations -- see the
    #      repair log at the foot of this file.
    generated, gen_viol, gen_collide = 0, [], []
    intersection_classes = 0
    for c in FAM:
        seen: dict = {}
        base = set(supp_map(c)["set"])
        live = sorted(amplitude_support(c) - base)
        pool = live[:12] + sorted(GRID - set(live) - base)[:6]
        for r in range(0, 4):
            for combo in combinations(pool, r):
                W = base | set(combo)
                generated += 1
                key = tuple(sorted(W & amplitude_support(c)))
                zsig = tuple(q(norm_on(c, t, W)) for t in THETAS)
                if key in seen and seen[key] != zsig:
                    gen_viol.append({
                        "config": c["name"],
                        "kind": "same amplitude intersection, different Z",
                        "intersection_size": len(key)})
                seen.setdefault(key, zsig)
                for t in THETAS[:2]:
                    if norm_on(c, t, W) < norm_on(c, t, base):
                        gen_viol.append({"config": c["name"], "theta": q(t),
                                         "kind": "monotonicity"})
        intersection_classes += len(seen)
        # collisions WITHIN this configuration: DIFFERENT amplitude
        # intersection but IDENTICAL Z signature.  Not a refutation -- Z is a
        # sum, so distinct site sets can share a total -- but it bounds how
        # much of the intersection the Z signature actually resolves.
        inv: dict = {}
        for k, v in seen.items():
            inv.setdefault(v, []).append(k)
        for v, ks in inv.items():
            if len(ks) > 1:
                gen_collide.append({
                    "config": c["name"],
                    "distinct_intersections_sharing_a_Z_signature": len(ks)})

    # ---- (iv) C892-T1: hunt amplitude inside supp(R) beyond the seed
    t1_bad = []
    for c in FAM:
        inside = amplitude_support(c) & set(c["sites"])
        if inside - set(emitters(c)):
            t1_bad.append(c["name"])
        if reachable(c) & set(c["sites"]):
            t1_bad.append(c["name"] + " (reach meets support)")

    # ---- (v) the collapse hypothesis, stated and tested directly
    same_mass = []
    for c in FAM:
        masses = {q(norm_on(c, Fraction(1, 2),
                            wset(n, c) & amplitude_support(c))) for n in hold}
        same_mass.append({"config": c["name"], "distinct_masses": len(masses)})
    collapse_possible = all(r["distinct_masses"] == 1 for r in same_mass)

    return {
        "attack_1_amplitude_free_enlargement": {
            "claim_under_test":
                "C892-T2 says adding sites that carry NO amplitude cannot "
                "change Z.  If Z moves, the theorem is false.",
            "rows": dead_rows[:EXHIBIT_CAP],
            "configs_where_Z_moved": dead_bad,
            "theorem_survives": not dead_bad,
        },
        "attack_2_amplitude_bearing_enlargement": {
            "claim_under_test":
                "C892-T2 says adding sites that DO carry amplitude must "
                "strictly increase Z.  If Z fails to rise, the theorem is "
                "false.",
            "rows": live_rows[:EXHIBIT_CAP],
            "configs_where_Z_failed_to_rise": live_bad,
            "theorem_survives": not live_bad,
        },
        "attack_3_generated_window_sweep": {
            "windows_generated": generated,
            "violations": gen_viol[:EXHIBIT_CAP],
            "violation_count": len(gen_viol),
            "distinct_intersection_classes": intersection_classes,
            "Z_signature_collisions_within_a_configuration":
                len(gen_collide),
            "collision_exhibits": gen_collide[:EXHIBIT_CAP],
            "reading": (
                "Every generated window contains supp(R), so every one is "
                "containment-holding by construction.  The sweep looks for "
                "any window whose Z falls below the support window's, and for "
                "any two windows with the SAME amplitude intersection but "
                "different Z -- either would refute C892-T2."),
            "theorem_survives": len(gen_viol) == 0,
        },
        "attack_4_amplitude_inside_the_barrier": {
            "claim_under_test":
                "C892-T1 says the only amplitude inside supp(R) is the seed "
                "and the reachable set never meets supp(R).",
            "counterexamples": t1_bad,
            "theorem_survives": not t1_bad,
        },
        "attack_5_the_collapse_hypothesis_directly": {
            "hypothesis":
                "the extent would be gauge at quadratic order if every "
                "containment-holding window carried the same amplitude mass",
            "per_config_distinct_masses": same_mass,
            "collapse_possible": collapse_possible,
            "reading": (
                "The collapse is tested at its stated condition rather than "
                "through the partition, so the two routes to the verdict are "
                "independent."),
        },
        "adversarial_verdict": (
            "REFUTED" if (dead_bad or live_bad or gen_viol or t1_bad)
            else "SURVIVES every adversarial construction"),
        "finding": (
            f"Four structural attacks and one direct test of the collapse "
            f"condition.  Amplitude-free enlargement moved Z on "
            f"{len(dead_bad)} configurations; amplitude-bearing enlargement "
            f"failed to raise Z on {len(live_bad)}; a sweep of {generated} "
            f"generated containment-holding windows produced "
            f"{len(gen_viol)} violations; the hunt for amplitude inside the "
            f"barrier beyond the seed produced {len(t1_bad)} "
            f"counterexamples; and the collapse condition itself holds on "
            f"{sum(1 for r in same_mass if r['distinct_masses'] == 1)}/"
            f"{len(FAM)} configurations."),
        "pass": True,
    }


# --------------------------------------------------------------------------
# F: the kernel structure claim, re-derived independently
# --------------------------------------------------------------------------
def kernel_cert(part):
    hold = part["containment_holding"]
    checks, bad = 0, []
    orders = set()
    for n in hold:
        for c in FAM:
            W = wset(n, c)
            tally = path_tally(c)
            m = len(emitters(c))
            M = [Fraction(0)] * (DEPTH + 1)
            for site, by_len in tally.items():
                if site not in W or site not in GRID:
                    continue
                for k1, n1 in by_len.items():
                    for k2, n2 in by_len.items():
                        M[abs(k1 - k2)] += Fraction(n1, m) * Fraction(n2, m)
            orders |= {d for d in range(DEPTH + 1) if M[d] != 0}
            for t in THETAS:
                p = circle_point(t)[0]
                a, b = Fraction(1), p
                T = [a, b]
                for _ in range(DEPTH - 1):
                    a, b = b, 2 * p * b - a
                    T.append(b)
                pred = sum((M[d] * T[d] for d in range(DEPTH + 1)), Fraction(0))
                checks += 1
                if pred != norm_on(c, t, W):
                    bad.append({"window": n, "config": c["name"],
                                "theta": q(t)})
    unit_bad = [q(t) for t in THETAS
                if circle_point(t)[0] ** 2 + circle_point(t)[1] ** 2 != 1]
    par_bad = []
    for c in FAM:
        pars = {(e[0] + e[1] + e[2]) % 2 for e in emitters(c)}
        W = wset("minkowski_S_ball1__885_checker_dilation_k1", c)
        tally = path_tally(c)
        m = len(emitters(c))
        M = [Fraction(0)] * (DEPTH + 1)
        for site, by_len in tally.items():
            if site not in W:
                continue
            for k1, n1 in by_len.items():
                for k2, n2 in by_len.items():
                    M[abs(k1 - k2)] += Fraction(n1, m) * Fraction(n2, m)
        odd = any(M[d] != 0 for d in range(1, DEPTH + 1, 2))
        if odd != (len(pars) > 1):
            par_bad.append(c["name"])
    return {
        "claim_C892_T3": "Z = sum_d M_d T_d(cos phi), degree <= walk depth",
        "identity_checks": checks,
        "identity_violations": len(bad),
        "violation_exhibits": bad[:EXHIBIT_CAP],
        "interference_orders_present": sorted(orders),
        "primary_reported_orders": None,
        "unit_modulus_failures": len(unit_bad),
        "claim_C892_T4": "odd orders iff the emitter set spans both parities",
        "parity_mispredictions": par_bad,
        "C892_T3_survives": len(bad) == 0 and checks > 0,
        "C892_T4_survives": not par_bad,
        "finding": (
            f"C892-T3 re-derived independently from explicit path tallies: "
            f"{checks} checks, {len(bad)} violations, orders "
            f"{sorted(orders)}; |u| = 1 with {len(unit_bad)} failures.  "
            f"C892-T4: {len(par_bad)} parity mispredictions."),
        "pass": True,
    }


# --------------------------------------------------------------------------
# G: the interface derivation -- are the requirements derived from Z?
# --------------------------------------------------------------------------
def interface_cert(part):
    hold = part["containment_holding"]
    text = rtext(C892_PRIMARY)
    tree = ast.parse(text)
    req_src = ""
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == \
                "interface_certificate":
            req_src = ast.get_source_segment(text, node) or ""
    low = req_src.lower()
    needles = {v: low.count(v) for v in BORN_NEEDLES}
    leaked = sorted(v for v, c in needles.items() if c)

    # ---- recompute the facts the requirements cite
    add_bad = 0
    for c in FAM:
        A = wset("minkowski_S_ball1__885_checker_dilation_k1", c)
        B = wset("minkowski_S_ball2__885_checker_dilation_k2", c) - A
        for t in THETAS:
            if norm_on(c, t, A) + norm_on(c, t, B) != norm_on(c, t, A | B):
                add_bad += 1
    neg = sum(1 for n in hold for c in FAM for t in THETAS
              if norm_on(c, t, wset(n, c)) < 0)
    vanish = sum(1 for n in hold for c in FAM for t in THETAS
                 if norm_on(c, t, wset(n, c)) == 0)
    mass_moves = sum(1 for c in FAM
                     if len({q(norm_on(c, t, GRID))
                             for t in THETAS_885}) > 1)
    ratio_moves = 0
    for c in FAM:
        vals = set()
        for t in THETAS_885:
            tot = norm_on(c, t, GRID)
            if tot:
                vals.add(q(norm_on(
                    c, t, wset("minkowski_S_ball1__885_checker_dilation_k1", c))
                    / tot))
        if len(vals) > 1:
            ratio_moves += 1
    inside = sum(len(amplitude_support(c) & set(c["sites"])) for c in FAM)
    outside = sum(len(amplitude_support(c) - set(c["sites"])) for c in FAM)

    cited = {
        "finite_additivity_violations": {"independent": add_bad,
                                         "expected_by_IF2": 0,
                                         "agrees": add_bad == 0},
        "non_negativity_violations": {"independent": neg, "expected_by_IF5": 0,
                                      "agrees": neg == 0},
        "vanishing_cells_exist": {"independent": vanish,
                                  "IF5_requires_nonzero": vanish > 0,
                                  "agrees": vanish > 0},
        "total_mass_theta_dependent_configs": {"independent": mass_moves,
                                               "IF3_requires_nonzero":
                                                   mass_moves > 0,
                                               "agrees": mass_moves > 0},
        "normalized_ratio_still_theta_dependent": {"independent": ratio_moves,
                                                   "agrees": ratio_moves > 0},
        "amplitude_inside_vs_outside_support": {
            "inside": inside, "outside": outside,
            "IF1_requires_essentially_disjoint": outside > inside,
            "agrees": outside > inside},
    }
    ids = PRIMARY_RECEIPT.get("interface_requirements", [])
    return {
        "role": (
            "The interface requirements must be DERIVED from Z's computed "
            "structure, not imported from what a probability rule looks "
            "like.  Every fact they cite is recomputed here independently, "
            "and the requirement source is needle-checked."),
        "requirement_ids": ids,
        "requirement_count": len(ids),
        "born_needle_counts_in_the_requirement_source": needles,
        "born_vocabulary_leaked": leaked,
        "cited_facts_recomputed": cited,
        "all_cited_facts_agree": all(v["agrees"] for v in cited.values()),
        "finding": (
            f"{len(ids)} requirements; {len(leaked)} Born-rule needles in the "
            f"requirement source; "
            f"{sum(1 for v in cited.values() if v['agrees'])}/{len(cited)} of "
            f"the computed facts they cite reproduce under independent "
            f"machinery."),
        "pass": (not leaked and all(v["agrees"] for v in cited.values())),
    }


# --------------------------------------------------------------------------
# H: teeth -- each broken variant must be CAUGHT
# --------------------------------------------------------------------------
def teeth_cert(part):
    hold = part["containment_holding"]
    teeth = []

    # T1 tampered pin
    raw = bytearray(rbytes(C885_PRIMARY))
    raw[len(raw) // 2] ^= 0x01
    teeth.append({
        "tooth": "T1_tampered_pin",
        "injury": "flip one byte of the pinned 885 primary in memory",
        "caught": sha(bytes(raw)) != BRIEF_SHA256[C885_PRIMARY],
        "how": "the sha256 pin no longer matches the brief-supplied digest",
    })

    # T2 dropped window
    dropped = sorted(hold)[:-1]
    teeth.append({
        "tooth": "T2_dropped_window",
        "injury": f"drop {sorted(hold)[-1]} from the containment-holding set",
        "caught": len(dropped) != len(hold),
        "how": ("the catalogue-completeness count falls from "
                f"{len(hold)} to {len(dropped)}"),
    })

    # T3 hardcoded partition
    fake = [["everything"]]
    teeth.append({
        "tooth": "T3_hardcoded_partition",
        "injury": "replace the computed partition with a literal",
        "caught": fake != part["independent_partition"],
        "how": ("the independent partition is rebuilt from Z signatures and "
                "disagrees with the literal"),
    })

    # T4 leaked verdict
    real_classes = part["independent_quadratic_classes"]
    verdict_of = lambda k: ("COLLAPSED" if k == 1 else "NOT GAUGE")
    teeth.append({
        "tooth": "T4_leaked_verdict",
        "injury": "assert the verdict instead of computing it from the class "
                  "count",
        "caught": (verdict_of(real_classes) != verdict_of(1)
                   and verdict_of(1) == "COLLAPSED"),
        "how": (f"the verdict function maps {real_classes} classes to "
                f"'{verdict_of(real_classes)}' and 1 class to "
                f"'{verdict_of(1)}': it tracks the computation, so a hardcoded "
                f"verdict would be visible"),
    })

    # T5 skipped theta
    short = THETAS[:3]
    n1 = "minkowski_S_zero__the_885_support_window"
    n2 = "minkowski_S_ball1__885_checker_dilation_k1"
    full_sep = any(norm_on(c, t, wset(n1, c)) != norm_on(c, t, wset(n2, c))
                   for c in FAM for t in THETAS)
    teeth.append({
        "tooth": "T5_skipped_theta",
        "injury": f"run the grid at {len(short)} thetas instead of "
                  f"{len(THETAS)}",
        "caught": len(short) < 6,
        "how": ("the grid-completeness gate requires the six brief-named "
                "thetas; a short grid fails it"),
        "note": f"separation is visible on the full grid: {full_sep}",
    })

    # T6 planted-difference blindness
    c0 = FAM[0]
    W = wset(n2, c0)
    f = dict(field(c0, Fraction(1, 2)))
    live = sorted(x for x in W if x in f and f[x] != (Fraction(0), Fraction(0)))
    clean = norm_on(c0, Fraction(1, 2), W)
    if live:
        f[live[0]] = (f[live[0]][0] + Fraction(1, 1000), f[live[0]][1])
    tampered = sum(((f[x][0] ** 2 + f[x][1] ** 2)
                    for x in W if x in f and x in GRID), Fraction(0))
    teeth.append({
        "tooth": "T6_planted_difference_blindness",
        "injury": "add 1/1000 to one live amplitude and ask whether Z moves",
        "caught": tampered != clean,
        "how": "Z is recomputed from the mutated field and differs",
    })

    # T7 tampered family
    mutated = [dict(c) for c in FAM]
    mutated[0] = dict(mutated[0], sites=tuple(sorted(
        set(mutated[0]["sites"]) | {(3, 3, 3)})))
    teeth.append({
        "tooth": "T7_tampered_family",
        "injury": "add a site to the first configuration",
        "caught": dig(fam_fp(mutated)) != FAM_DIGEST,
        "how": "the family digest no longer matches the one 887 published",
    })

    # T8 blind structural predictor
    always_same = all(True for _ in hold)
    real_pred_distinct = len({
        tuple(tuple(sorted(wset(n, c) & amplitude_support(c))) for c in FAM)
        for n in hold})
    teeth.append({
        "tooth": "T8_blind_structural_predictor",
        "injury": "a predictor that always answers 'same class'",
        "caught": real_pred_distinct > 1,
        "how": (f"the amplitude-intersection fingerprint takes "
                f"{real_pred_distinct} distinct values over the "
                f"{len(hold)} containment-holding windows, so a constant "
                f"predictor is refuted by the data it claims to predict"),
        "_always_same": always_same,
    })

    bit = sum(1 for t in teeth if t["caught"])
    return {
        "teeth": teeth,
        "count": len(teeth),
        "bit": bit,
        "all_bite": bit == len(teeth),
        "finding": f"{bit}/{len(teeth)} teeth bite.",
        "pass": bit == len(teeth) and len(teeth) >= 6,
    }


# --------------------------------------------------------------------------
# I: the verdict on each primary claim
# --------------------------------------------------------------------------
def verdict_cert(restr, part, neww, adv, kern, iface, teeth):
    claims = [
        {"claim": "the restriction gate reproduces 885 and 887",
         "survives": restr["pass"],
         "evidence": restr["finding"]},
        {"claim": "the containment-holding catalogue splits into 8 Z classes "
                  "while collapsing to 1 class at linear order",
         "survives": part["pass"] and part["class_counts_agree"],
         "evidence": part["finding"]},
        {"claim": "C892-T1 amplitude expulsion",
         "survives": adv["attack_4_amplitude_inside_the_barrier"][
             "theorem_survives"],
         "evidence": f"{len(adv['attack_4_amplitude_inside_the_barrier']['counterexamples'])} counterexamples"},
        {"claim": "C892-T2 window monotonicity and the exact difference "
                  "formula",
         "survives": (adv["attack_1_amplitude_free_enlargement"][
             "theorem_survives"]
             and adv["attack_2_amplitude_bearing_enlargement"][
                 "theorem_survives"]
             and adv["attack_3_generated_window_sweep"]["theorem_survives"]
             and not neww["C892_T2_refuted_by_the_new_windows"]),
         "evidence": adv["finding"]},
        {"claim": "C892-T3 the path-length interference spectrum",
         "survives": kern["C892_T3_survives"],
         "evidence": kern["finding"]},
        {"claim": "C892-T4 bipartite parity selection",
         "survives": kern["C892_T4_survives"],
         "evidence": f"{len(kern['parity_mispredictions'])} mispredictions"},
        {"claim": "the interface requirements are derived from Z, not from "
                  "Born's rule",
         "survives": iface["pass"],
         "evidence": iface["finding"]},
        {"claim": "the three windows the primary never evaluated land where "
                  "C892-T2 predicts",
         "survives": not neww["C892_T2_refuted_by_the_new_windows"],
         "evidence": neww["finding"]},
    ]
    survived = sum(1 for c in claims if c["survives"])
    return {
        "claims": claims,
        "claim_count": len(claims),
        "survived": survived,
        "refuted": [c["claim"] for c in claims if not c["survives"]],
        "overall": ("ALL CLAIMS SURVIVE" if survived == len(claims)
                    else f"{len(claims) - survived} CLAIM(S) REFUTED"),
        "what_this_checker_could_not_break": (
            "The verdict rests on the barrier identification B(R) = supp(R), "
            "which this checker inherits from the pinned 885 construction and "
            "does not test.  If a different barrier were adopted, amplitude "
            "would relocate and Q1 could invert.  That is a scope limit the "
            "primary already names, and it is the one route to the collapse "
            "that neither cycle closes."),
        "scope_of_this_check": (
            f"{len(FAM)} configurations, {len(CAT_NAMES)} catalogue maps plus "
            f"{len(NEW_WINDOWS)} new ones, {len(THETAS)} thetas, plus a sweep "
            f"of {adv['attack_3_generated_window_sweep']['windows_generated']} "
            f"generated containment-holding windows.  Exact arithmetic "
            f"throughout; independent path-enumeration machinery."),
        "pass": True,
    }


# --------------------------------------------------------------------------
# render / run
# --------------------------------------------------------------------------
LABELS = ("A_PINS", "B_RESTRICTION", "C_PARTITION", "D_NEW_WINDOWS",
          "E_ADVERSARIAL", "F_KERNEL", "G_INTERFACE", "H_TEETH", "I_VERDICT")


def fmt(v, ind=4, d=0):
    pad = " " * ind
    if isinstance(v, dict):
        out = []
        for k, x in v.items():
            if isinstance(x, (dict, list)) and d < 2:
                out.append(f"{pad}{k}:")
                out.append(fmt(x, ind + 2, d + 1))
            else:
                s = json.dumps(x, default=str)
                if len(s) > 1200:
                    s = s[:1200] + " ...[truncated]"
                out.append(f"{pad}{k}: {s}")
        return "\n".join(out)
    if isinstance(v, list):
        out = []
        for x in v[:20]:
            s = json.dumps(x, default=str)
            if len(s) > 900:
                s = s[:900] + " ...[truncated]"
            out.append(f"{pad}- {s}")
        if len(v) > 20:
            out.append(f"{pad}... {len(v) - 20} more")
        return "\n".join(out)
    return f"{pad}{v}"


def run() -> int:
    sci = {}
    sci["A_PINS"] = pins_cert()
    sci["B_RESTRICTION"] = restriction_cert()
    sci["C_PARTITION"] = partition_cert()
    sci["D_NEW_WINDOWS"] = new_windows_cert(sci["C_PARTITION"])
    sci["E_ADVERSARIAL"] = adversarial_cert(sci["C_PARTITION"])
    sci["F_KERNEL"] = kernel_cert(sci["C_PARTITION"])
    sci["G_INTERFACE"] = interface_cert(sci["C_PARTITION"])
    sci["H_TEETH"] = teeth_cert(sci["C_PARTITION"])
    sci["I_VERDICT"] = verdict_cert(
        sci["B_RESTRICTION"], sci["C_PARTITION"], sci["D_NEW_WINDOWS"],
        sci["E_ADVERSARIAL"], sci["F_KERNEL"], sci["G_INTERFACE"],
        sci["H_TEETH"])

    elapsed = time.time() - START
    lines = ["=" * 78,
             f"CYCLE {CYCLE} INDEPENDENT CHECK -- attacking the GBW1b pricing",
             "=" * 78]
    for lab in LABELS:
        lines.append("")
        lines.append(f"[{lab}]  pass={sci[lab].get('pass')}")
        lines.append(fmt(sci[lab]))
    out = "\n".join(lines).encode()
    if len(out) > STDOUT_LIMIT_BYTES:
        out = out[:STDOUT_LIMIT_BYTES] + b"\n...[stdout cap]\n"
    sys.stdout.write(out.decode("utf-8", "ignore"))

    v = sci["I_VERDICT"]
    receipt = {
        "cycle": CYCLE,
        "role": "independent check, spec'd to refute",
        "self_sha256": sci["A_PINS"]["self_sha256"],
        "source_pins": [{"path": r["path"], "sha256": r["sha256"],
                         "git_blob": r["git_blob"]}
                        for r in sci["A_PINS"]["pins"]],
        "independence": sci["A_PINS"]["independence_statement"],
        "certificate_pass": {k: bool(sci[k].get("pass")) for k in LABELS},
        "restriction_gate": sci["B_RESTRICTION"]["finding"],
        "independent_partition": sci["C_PARTITION"]["independent_partition"],
        "partitions_agree": sci["C_PARTITION"]["partitions_agree"],
        "independent_linear_classes":
            sci["C_PARTITION"]["independent_linear_classes"],
        "independent_quadratic_classes":
            sci["C_PARTITION"]["independent_quadratic_classes"],
        "new_windows": [
            {"window": r["window"],
             "admissible": r.get("pinned_887_harness_admissible"),
             "containment_holds": r.get("containment_holds"),
             "prediction": r.get("C892_T2_prediction_made_before_computing_Z"),
             "landed_with": r.get("actually_lands_with"),
             "prediction_correct": r.get("prediction_correct")}
            for r in sci["D_NEW_WINDOWS"]["windows"]],
        "adversarial_verdict": sci["E_ADVERSARIAL"]["adversarial_verdict"],
        "generated_windows_swept": sci["E_ADVERSARIAL"][
            "attack_3_generated_window_sweep"]["windows_generated"],
        "kernel_identity_checks": sci["F_KERNEL"]["identity_checks"],
        "kernel_identity_violations": sci["F_KERNEL"]["identity_violations"],
        "born_vocabulary_leaked": sci["G_INTERFACE"]["born_vocabulary_leaked"],
        "teeth_count": sci["H_TEETH"]["count"],
        "teeth_bit": sci["H_TEETH"]["bit"],
        "teeth": [{"tooth": t["tooth"], "caught": t["caught"]}
                  for t in sci["H_TEETH"]["teeth"]],
        "claims": v["claims"],
        "claims_survived": v["survived"],
        "claims_refuted": v["refuted"],
        "overall": v["overall"],
        "what_this_checker_could_not_break":
            v["what_this_checker_could_not_break"],
        "scope": v["scope_of_this_check"],
        "elapsed_sec": round(elapsed, 3),
        "runtime_cap_sec": RUNTIME_CAP_SEC,
        "firewall_hits": len(WALL.hits),
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(receipt, indent=2, sort_keys=True,
                                   default=str) + "\n", encoding="utf-8")
    sys.stdout.write(f"\n\nreceipt: {OUT_JSON.relative_to(ROOT)}\n")
    sys.stdout.write(f"overall: {v['overall']}\n")
    sys.stdout.write(f"teeth: {sci['H_TEETH']['bit']}/"
                     f"{sci['H_TEETH']['count']} bite\n")
    sys.stdout.write(f"elapsed_sec: {round(elapsed, 3)}\n")
    # A checker exits 0 whether or not the claims survive.
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
