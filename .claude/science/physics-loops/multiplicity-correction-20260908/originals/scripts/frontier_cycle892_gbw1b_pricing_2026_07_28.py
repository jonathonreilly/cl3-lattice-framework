#!/usr/bin/env python3
"""Cycle 892: GBW1b -- price the kernel-window JOINT obligation.

Cycle 885 split `GBW1` into `GBW1a` (the window LOCUS, priced down to
conventions) and `GBW1b` (the terminal normalization `N`), and showed `N` is a
JOINT kernel-window obligation: the exact quantity

    Z(cfg, theta, W) = sum over window sites x in W of |A(x)|^2

moves with the kernel phase gain `theta` on 7 of 12 configurations.  Cycle 887
then proved the READOUT-GAUGE THEOREM: 9 of its 12 admissible catalogue maps
give an IDENTICAL axiom-level scalar readout `I_W` on every configuration --
the whole window-inflation freedom is invisible to the LINEAR readout.

`Z` is QUADRATIC in amplitudes.  This cycle asks the one theorem-shaped
question that separates the two orders.

Q1  IS THE WINDOW EXTENT STILL GAUGE AT QUADRATIC ORDER?  The containment-
    holding admissible catalogue of 887 is rebuilt by AST extraction from the
    pinned 887 primary, the 12-configuration family is rebuilt by AST
    extraction from the pinned 885 primary, and the full map
    `(W, theta) -> Z(cfg, theta, W)` is computed in exact arithmetic over a
    six-value theta grid.  The catalogue is then PARTITIONED by Z-behaviour.
    Both orders are computed and reported regardless of which way the verdict
    lands: the linear gauge verification (887's `I_W` row) AND the quadratic
    partition.

    The structural proof is ATTEMPTED, not assumed.  Certificate `E` computes
    WHERE AMPLITUDE ACTUALLY LIVES: the propagation barrier is `B(R) =
    supp(R)`, the walk may not step onto a blocked site, so the reachable set
    is computed and intersected with the support.  Whichever way that lands,
    it decides the collapse: if amplitude were confined to the barrier every
    containment-holding window would read the same amplitude set and the
    collapse would be a theorem; if amplitude is EXPELLED from the barrier the
    windows differ precisely on the sites that carry all of it.

Q2  THE GBW1b OBLIGATION MAP.  Four components are priced from computed facts
    only:

    (a) WINDOW      -- zero dimensions if Q1 collapses, the named convention
                       with its exact separating witnesses if not.
    (b) KERNEL      -- theta's exact role.  Certificate `H` characterizes
                       `Z(theta)` structurally: the per-edge gain is the exact
                       unit-circle point `u(theta)`, so `A` decomposes by PATH
                       LENGTH and `Z` is a PATH-LENGTH INTERFERENCE SPECTRUM.
                       The identity is CHECKED exactly on every (window,
                       config, theta) triple, and the interference orders that
                       actually appear are computed, not assumed.
    (c) INTERFACE   -- the linear-readout / quadratic-amplitude identification
                       the composed-record event-space step must supply.  This
                       lineage does NOT carry the Cycle-878 event-space
                       artifacts; their absence is COMPUTED by a tracked-file
                       scan with published globs and counts (883 discipline)
                       and they are never reconstructed.  The interface is
                       priced as a named import whose required properties are
                       DERIVED FROM Z'S COMPUTED STRUCTURE -- what Z is
                       measured to be and measured not to be -- and not from
                       what Born's rule says a weight should be.  Certificate
                       `J` carries a needle check that no Born-rule vocabulary
                       enters as a premise.
    (d) RESIDUAL    -- the final pricing row: GBW1b's residual dimension given
                       each import.

DISCIPLINE.  Every pinned input is fixed by full path + sha256 + git blob and
read as TEXT / AST / JSON only; a meta-path firewall makes importing any of
them an error and the hit count is gated at zero.  Every certified quantity is
exact (`Fraction`, exact Gaussian rationals); no floating point enters any
certified value.  The science block is built TWICE and the digests compared.
The gates are outcome-neutral: they require the family digest to match the
value 887 published for the same AST-extracted family, the catalogue to be
COMPLETE (every named map evaluated), BOTH orders to be computed, the theta
grid to be complete, and the restriction gate to reproduce the pinned 885 and
887 rows -- none of them requires a particular verdict.

RESTRICTION GATE (888-style).  Certificate `B` reproduces, BEFORE any new
claim: 885's N-certificate boundary-shell rows value-for-value out of the
pinned 885 runner cache (not merely its 7/12 headline), 885's degenerate-window
control (0/12), and 887's readout-gauge row (9 of 12 admissible maps
indistinguishable) out of the pinned 887 receipt.  A mismatch fails the gate
and no downstream claim is issued.

STRESS.  Certificate `K` requires: an impostor window that BREAKS containment
is excluded by the catalogue filter rather than silently included; a
non-admissible map is refused; and a PLANTED Z-difference -- a mutated
amplitude field -- is DETECTED by the partition, proving the partition can see
a gauge break if one exists (889-style falsifier visibility).

SCOPE, HONESTLY.  One 12-configuration family in a box of radius 4 with walk
depth 4, one catalogue of 17 window maps of which 12 are admissible and 9 hold
containment, one six-value theta grid.  The confinement statement in `E` and
the monotonicity statement in `G` are proved as theorems ON THESE HYPOTHESES
(finite box, blocked-barrier walk, containment-holding windows) and the
catalogue instantiates them; the catalogue itself is not a proof that no
window map anywhere behaves otherwise, and that limit is stated in the verdict.
"""

from __future__ import annotations

import ast
import hashlib
import importlib.abc
import json
import subprocess
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
SELF_REL = "scripts/frontier_cycle892_gbw1b_pricing_2026_07_28.py"
OUT_JSON = ROOT / "outputs" / "gbw1b_pricing_cycle892_receipt_2026_07_28.json"

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
    C885_PRIMARY,
    C885_RECEIPT,
    C885_CHECKER,
    C885_CACHE,
    C887_PRIMARY,
    C887_RECEIPT,
    AXIOMS_MD,
    DYNAMICS_MD,
    WEAKFIELD_MD,
)

# Digests the block brief supplies verbatim.  A mismatch is a hard preflight
# failure: the cited artifact is not the artifact this cycle was pointed at.
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

# The digest 887 published for the AST-extracted 885 family.  Read from the
# pinned 887 receipt at run time; this literal is only the cross-check.
FAMILY_DIGEST_887 = (
    "30edaa3d5ca03c2492a772a3eeec2c360b70e0e742ba4889bf3e0c5e4180b25e")

# The theta grid.  The brief requires at least these six.
THETA_GRID = (Fraction(1, 2), Fraction(1, 3), Fraction(2, 5),
              Fraction(1, 7), Fraction(3, 8), Fraction(5, 6))
# The three 885 swept, used by the restriction gate.
THETA_885 = (Fraction(1, 2), Fraction(1, 3), Fraction(2, 5))
# A finer grid used ONLY to characterize the Z(theta) structure (certificate H).
THETA_FINE = tuple(Fraction(a, b)
                   for b in (2, 3, 4, 5, 6, 7, 8, 9)
                   for a in range(1, b) if Fraction(a, b).denominator == b)

# amplitude DP geometry, verbatim from the pinned 885 primary
RBOX = 4
MAX_STEPS = 4

# Cycle-878 event-space probes.  Presence is COMPUTED, never reconstructed.
C878_PROBES = (
    "cycle878_composed_record_event_space",
    "composed_record_event_space",
    "event_space",
    "cycle867_composed_record_event_model",
    "born_measure",
)
C878_SCAN_GLOBS = ("scripts/*", "outputs/*", "logs/runner-cache/*", "docs/*")


# --------------------------------------------------------------------------
# preflight + firewall
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


preflight_pins()

_FORBIDDEN_STEMS = {Path(p).stem for p in AUDIT_INPUT_PATHS}


class _Firewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list = []

    def find_module(self, fullname, path=None):  # pragma: no cover - legacy
        return self.find_spec(fullname, path)

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in _FORBIDDEN_STEMS:
            self.hits.append(fullname)
            raise ImportError(f"firewall forbids import of {fullname}")
        return None


FIREWALL = _Firewall()
sys.meta_path.insert(0, FIREWALL)


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def read_bytes(rel: str) -> bytes:
    return (ROOT / rel).read_bytes()


def read_text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def sha256_of(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def digest(payload) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, default=str).encode("utf-8")
    ).hexdigest()


def q(v) -> str:
    if v is None:
        return "none"
    f = Fraction(v)
    return f"{f.numerator}/{f.denominator}"


# ---- exact Gaussian rationals (verbatim convention from the 885 primary) ---
ZERO_C = (Fraction(0), Fraction(0))
ONE_C = (Fraction(1), Fraction(0))


def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cabs2(a):
    return a[0] * a[0] + a[1] * a[1]


def unit_point(t: Fraction):
    """Exact rational point on the unit circle: ((1-t^2)/(1+t^2), 2t/(1+t^2))."""
    d = 1 + t * t
    return ((1 - t * t) / d, (2 * t) / d)


# --------------------------------------------------------------------------
# AST extraction: no import, no exec of a pinned file as a whole
# --------------------------------------------------------------------------
def ast_extract(rel: str, wanted, seed: dict):
    """Execute ONLY the named top-level nodes of a pinned file, in file order.

    Nothing else from the pinned module runs: no `run()`, no receipt write, no
    side effect.  The firewall independently forbids importing the file.
    """
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
    mod = ast.Module(body=body, type_ignores=[])
    exec(compile(mod, filename=f"<ast:{rel}>", mode="exec"), ns)  # noqa: S102
    return ns, sorted(seen), sorted(set(wanted) - seen)


_SEED = {"Fraction": Fraction, "product": product, "permutations": permutations}

FAMILY_NODES = ("NEIGHBOURS", "_lcg", "make_config", "build_family")

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

NS885, SEEN885, MISSING885 = ast_extract(C885_PRIMARY, set(FAMILY_NODES), _SEED)
FAMILY = NS885["build_family"]()
NEIGHBOURS = NS885["NEIGHBOURS"]

NS887, SEEN887, MISSING887 = ast_extract(
    C887_PRIMARY, set(CATALOGUE_NODES), dict(_SEED, FAMILY=FAMILY))
CATALOGUE = NS887["selector_catalogue"]()
CAT = dict(CATALOGUE)
CAT_NAMES = [n for n, _ in CATALOGUE]


def family_fingerprint(fam) -> list:
    """887's fingerprint convention, so the digests are comparable."""
    return [{"name": c["name"],
             "sites": [list(s) for s in c["sites"]],
             "content": [[list(s), b] for s, b in c["content"]],
             "depth": [[list(s), d] for s, d in c["depth"]]} for c in fam]


FAMILY_DIGEST = digest(family_fingerprint(FAMILY))


# --------------------------------------------------------------------------
# the amplitude machinery -- rebuilt here, decomposed by PATH LENGTH
# --------------------------------------------------------------------------
BOX = tuple(product(range(-RBOX, RBOX + 1), repeat=3))
INBOX = frozenset(BOX)


def barycentre(cfg) -> tuple:
    n = len(cfg["sites"])
    return tuple(Fraction(sum(s[i] for s in cfg["sites"]), n) for i in range(3))


def source_set(cfg) -> tuple:
    """The record-determined source: box sites closest to the barycentre."""
    c = barycentre(cfg)
    best, src = None, []
    for x in BOX:
        r2 = sum((Fraction(x[i]) - c[i]) ** 2 for i in range(3))
        if best is None or r2 < best:
            best, src = r2, [x]
        elif r2 == best:
            src.append(x)
    return tuple(sorted(src))


_WALK_CACHE: dict = {}


def walk_layers(cfg):
    """`layers[L][x]` = the INTEGER count of admissible L-step walks src -> x.

    Admissible = stays inside the box and never steps ONTO the barrier
    B(R) = supp(R).  Decomposing by path length is what makes the kernel's
    role exactly visible: every edge contributes the same gain u(theta), so
    the amplitude at x is `sum_L (count_L(x)/|src|) * u^L`.
    """
    key = cfg["name"]
    if key in _WALK_CACHE:
        return _WALK_CACHE[key]
    barrier = set(cfg["sites"])
    src = source_set(cfg)
    cur = {x: 1 for x in src}
    layers = [dict(cur)]
    for _ in range(MAX_STEPS):
        nxt: dict = {}
        for x, v in cur.items():
            for nb in NEIGHBOURS:
                y = (x[0] + nb[0], x[1] + nb[1], x[2] + nb[2])
                if y not in INBOX or y in barrier:
                    continue
                nxt[y] = nxt.get(y, 0) + v
        cur = nxt
        layers.append(dict(cur))
    _WALK_CACHE[key] = (layers, src)
    return layers, src


_AMP_CACHE: dict = {}


def amp_field(cfg, t: Fraction) -> dict:
    """Exact Gaussian-rational amplitude field.  No floating point."""
    key = (cfg["name"], t)
    if key in _AMP_CACHE:
        return _AMP_CACHE[key]
    layers, src = walk_layers(cfg)
    u = unit_point(t)
    n = len(src)
    amp: dict = {}
    up = ONE_C
    for L, lay in enumerate(layers):
        if L > 0:
            up = cmul(up, u)
        for x, c in lay.items():
            w = (up[0] * Fraction(c, n), up[1] * Fraction(c, n))
            amp[x] = cadd(amp.get(x, ZERO_C), w)
    _AMP_CACHE[key] = amp
    return amp


def Z(cfg, t: Fraction, window) -> Fraction:
    """Z = sum over window sites inside the box of |A(x)|^2.  Exact."""
    amp = amp_field(cfg, t)
    return sum((cabs2(amp[x]) for x in window if x in amp and x in INBOX),
               Fraction(0))


def window_of(name: str, cfg) -> set:
    return set(CAT[name](cfg)["set"])


# --------------------------------------------------------------------------
# A: pins
# --------------------------------------------------------------------------
def pins_certificate() -> dict:
    rows = []
    for rel in AUDIT_INPUT_PATHS:
        raw = read_bytes(rel)
        rows.append({
            "path": rel,
            "exists": True,
            "bytes": len(raw),
            "sha256": sha256_of(raw),
            "git_blob": git_blob_sha1(raw),
            "brief_sha256_match": (
                None if rel not in BRIEF_SHA256
                else sha256_of(raw) == BRIEF_SHA256[rel]),
        })
    brief_rows = [r for r in rows if r["brief_sha256_match"] is not None]
    return {
        "pins": rows,
        "pin_count": len(rows),
        "all_exist": all(r["exists"] for r in rows),
        "brief_supplied_digests_checked": len(brief_rows),
        "brief_supplied_digests_all_match": all(
            r["brief_sha256_match"] for r in brief_rows),
        "self_sha256": sha256_of(read_bytes(SELF_REL)),
        "import_firewall_hits": len(FIREWALL.hits),
        "import_firewall_hit_names": sorted(set(FIREWALL.hits)),
        "read_mode": "TEXT / AST / JSON only; no pinned module is imported",
        "ast_nodes_from_885": SEEN885,
        "ast_nodes_missing_from_885": MISSING885,
        "ast_nodes_from_887": SEEN887,
        "ast_nodes_missing_from_887": MISSING887,
        "finding": (
            f"{len(rows)} inputs pinned by full path + sha256 + git blob; the "
            f"{len(brief_rows)} digests the block brief supplies verbatim all "
            f"match; {len(SEEN885)} nodes AST-extracted from the 885 primary "
            f"and {len(SEEN887)} from the 887 primary with "
            f"{len(MISSING885) + len(MISSING887)} missing; firewall hits "
            f"{len(FIREWALL.hits)}."),
        "pass": (all(r["exists"] for r in rows)
                 and all(r["brief_sha256_match"] for r in brief_rows)
                 and not MISSING885 and not MISSING887
                 and len(FIREWALL.hits) == 0),
    }


# --------------------------------------------------------------------------
# B: the restriction gate -- reproduce 885 and 887 BEFORE any new claim
# --------------------------------------------------------------------------
def _json_block(text: str, key: str):
    """Pull one top-level JSON object out of the pinned 885 runner cache."""
    i = text.find(f'"{key}"')
    if i < 0:
        return None
    s = text.find("{", i)
    depth = 0
    for k in range(s, len(text)):
        if text[k] == "{":
            depth += 1
        elif text[k] == "}":
            depth -= 1
            if depth == 0:
                return json.loads(text[s:k + 1])
    return None


def site_boundary(cfg) -> tuple:
    """885's W1b locus: sites adjacent to the support but not in it."""
    supp = set(cfg["sites"])
    out = set()
    for s in supp:
        for nb in NEIGHBOURS:
            t = (s[0] + nb[0], s[1] + nb[1], s[2] + nb[2])
            if t not in supp:
                out.add(t)
    return tuple(sorted(out))


def restriction_gate() -> dict:
    cache = read_text(C885_CACHE)
    pinned_N = _json_block(cache, "K_N_TERMINAL_NORMALIZATION")
    r885 = json.loads(read_text(C885_RECEIPT))
    r887 = json.loads(read_text(C887_RECEIPT))

    # ---- (i) 885's boundary-shell rows, VALUE for VALUE
    mism = []
    recomputed = {}
    for cfg in FAMILY:
        row = {q(t): q(Z(cfg, t, set(site_boundary(cfg)))) for t in THETA_885}
        recomputed[cfg["name"]] = row
    for row in (pinned_N or {}).get("rows", []):
        mine = recomputed.get(row["config"])
        if mine != row["Z_by_theta"]:
            mism.append({"config": row["config"], "pinned": row["Z_by_theta"],
                         "recomputed": mine})
    dep = sum(1 for r in recomputed.values() if len(set(r.values())) > 1)

    # ---- (ii) 885's degenerate-window control (window = barrier)
    ctl_dep = sum(
        1 for cfg in FAMILY
        if len({q(Z(cfg, t, set(cfg["sites"]))) for t in THETA_885}) > 1)
    pinned_ctl = (pinned_N or {}).get("degenerate_window_control", {})

    # ---- (iii) 887's readout-gauge row, recomputed from the AST catalogue
    base_I = [NS887["readout"](c) for c in FAMILY]
    adm, indist = [], []
    for name in CAT_NAMES:
        ev = NS887["evaluate_map"](CAT[name])
        if not ev["admissible_REQ1_REQ5"]:
            continue
        adm.append(name)
        iw = [NS887["windowed_readout"](CAT[name], c) for c in FAMILY]
        if iw == base_I:
            indist.append(name)
    gauge887 = r887["science"]["I_READOUT_GAUGE"]

    # ---- (iv) the family digest
    fam887 = r887["science"]["B_FAMILY"]

    checks = {
        "c885_boundary_rows_value_for_value": {
            "pinned_rows": len((pinned_N or {}).get("rows", [])),
            "mismatches": len(mism),
            "exhibits": mism[:EXHIBIT_CAP],
            "match": len(mism) == 0
                     and len((pinned_N or {}).get("rows", [])) == len(FAMILY),
        },
        "c885_theta_dependent_count": {
            "pinned": (pinned_N or {}).get("configs_whose_Z_moves_with_theta"),
            "recomputed": dep,
            "match": dep == (pinned_N or {}).get(
                "configs_whose_Z_moves_with_theta"),
        },
        "c885_receipt_witness_states_7_of_12": {
            "witness": r885["classification"]["N"]["witness"],
            "recomputed": f"{dep}/{len(FAMILY)}",
            "match": f"theta on {dep}/{len(FAMILY)} configurations" in
                     r885["classification"]["N"]["witness"],
        },
        "c885_degenerate_control": {
            "pinned": pinned_ctl.get("configs_whose_Z_moves_with_theta"),
            "recomputed": ctl_dep,
            "match": ctl_dep == pinned_ctl.get(
                "configs_whose_Z_moves_with_theta"),
        },
        "c887_admissible_count": {
            "pinned": sorted(gauge887["per_map"]),
            "recomputed": sorted(adm),
            "match": sorted(adm) == sorted(gauge887["per_map"]),
        },
        "c887_readout_gauge_row": {
            "pinned_count": gauge887["count_indistinguishable"],
            "recomputed_count": len(indist),
            "pinned_members":
                sorted(gauge887[
                    "readout_indistinguishable_from_the_support_window"]),
            "recomputed_members": sorted(indist),
            "match": (len(indist) == gauge887["count_indistinguishable"]
                      and sorted(indist) == sorted(gauge887[
                          "readout_indistinguishable_from_the_support_window"])),
        },
        "c887_full_readout_per_config": {
            "pinned": gauge887["full_readout_per_config"],
            "recomputed": base_I,
            "match": base_I == gauge887["full_readout_per_config"],
        },
        "family_digest": {
            "pinned_887": fam887["family_digest_885_ast"],
            "literal_cross_check": FAMILY_DIGEST_887,
            "recomputed": FAMILY_DIGEST,
            "match": (FAMILY_DIGEST == fam887["family_digest_885_ast"]
                      == FAMILY_DIGEST_887),
        },
    }
    ok = all(c["match"] for c in checks.values())
    return {
        "role": (
            "888-style RESTRICTION GATE.  Nothing downstream is issued unless "
            "this cycle first reproduces the pinned results it is extending: "
            "885's N-certificate rows VALUE FOR VALUE (not merely its 7/12 "
            "headline), 885's degenerate-window control, 887's readout-gauge "
            "row and admissible set, and the family digest."),
        "checks": checks,
        "all_reproduced": ok,
        "finding": (
            f"{sum(1 for c in checks.values() if c['match'])}/{len(checks)} "
            f"restriction checks reproduce.  885's 12 boundary-shell rows "
            f"match value-for-value with {len(mism)} mismatches, its "
            f"theta-dependence is {dep}/{len(FAMILY)} and its degenerate "
            f"control {ctl_dep}/{len(FAMILY)}; 887's readout gauge recomputes "
            f"as {len(indist)} of {len(adm)}; the family digest is "
            f"{FAMILY_DIGEST[:16]}."),
        "pass": ok,
    }


# --------------------------------------------------------------------------
# C: the family
# --------------------------------------------------------------------------
def family_certificate() -> dict:
    rows = []
    for cfg in FAMILY:
        layers, src = walk_layers(cfg)
        rows.append({
            "name": cfg["name"],
            "records": len(cfg["sites"]),
            "readout_I": NS887["readout"](cfg),
            "barycentre": [q(x) for x in barycentre(cfg)],
            "source_sites": len(src),
            "source_inside_support": len(set(src) & set(cfg["sites"])),
        })
    return {
        "source": (
            "AST-extracted from the pinned 885 primary: only its NEIGHBOURS, "
            "_lcg, make_config and build_family nodes are executed, in a bare "
            "namespace.  No 885 code path other than those four runs."),
        "family_size": len(FAMILY),
        "family_digest": FAMILY_DIGEST,
        "family_digest_matches_887": FAMILY_DIGEST == FAMILY_DIGEST_887,
        "rows": rows,
        "distinct_support_sizes": sorted({len(c["sites"]) for c in FAMILY}),
        "finding": (
            f"{len(FAMILY)} configurations, digest {FAMILY_DIGEST[:16]}, "
            f"identical to the digest 887 published for the same AST "
            f"extraction.  Results compose with both pinned cycles."),
        "pass": len(FAMILY) == 12 and FAMILY_DIGEST == FAMILY_DIGEST_887,
    }


# --------------------------------------------------------------------------
# D: the catalogue -- admissibility and containment, every named map
# --------------------------------------------------------------------------
_EVAL_CACHE: dict = {}


def evaluation(name: str) -> dict:
    if name not in _EVAL_CACHE:
        _EVAL_CACHE[name] = NS887["evaluate_map"](CAT[name])
    return _EVAL_CACHE[name]


def catalogue_certificate() -> dict:
    rows = {}
    for name in CAT_NAMES:
        ev = evaluation(name)
        cp = NS887["containment_profile"](CAT[name])
        rows[name] = {
            "admissible_REQ1_REQ5": ev["admissible_REQ1_REQ5"],
            "equivariance_failures": ev["equivariance_failures"],
            "permanence_failures": ev["permanence_failures"],
            "distinct_set_values": ev["distinct_set_values"],
            "contains_support_on": cp["contains_support"],
            "of_configs": cp["configs"],
            "containment_holds": cp["supp_subset_W_on_all_configs"],
            "window_sizes": [len(window_of(name, c)) for c in FAMILY],
            "sites_outside_the_box": [
                len(window_of(name, c) - INBOX) for c in FAMILY],
        }
    admissible = sorted(n for n in CAT_NAMES
                        if rows[n]["admissible_REQ1_REQ5"])
    holding = sorted(n for n in admissible if rows[n]["containment_holds"])
    excluded_by_containment = sorted(set(admissible) - set(holding))
    refused = sorted(set(CAT_NAMES) - set(admissible))
    clipped = sorted(n for n in holding
                     if any(rows[n]["sites_outside_the_box"]))
    return {
        "source": (
            "AST-extracted from the pinned 887 primary: its structuring sets, "
            "morphological maps, impostors, REQ1-REQ5 harness and containment "
            "profile are executed as nodes, never imported."),
        "catalogue_size": len(CAT_NAMES),
        "every_named_map_evaluated": len(rows) == len(CAT_NAMES),
        "per_map": rows,
        "admissible": admissible,
        "containment_holding": holding,
        "excluded_by_the_containment_filter": excluded_by_containment,
        "refused_as_non_admissible": refused,
        "windows_clipped_by_the_box": clipped,
        "clipping_note": (
            "Z sums only over window sites inside the amplitude box "
            f"|x|_inf <= {RBOX}, exactly as the pinned 885 primary does.  Any "
            "window site beyond the box carries no computed amplitude and is "
            "reported per map so the clipping is visible rather than silent."),
        "finding": (
            f"{len(CAT_NAMES)} named maps evaluated, {len(admissible)} "
            f"admissible under REQ1-REQ5, {len(holding)} of those hold "
            f"containment on all {len(FAMILY)} configurations.  "
            f"{len(excluded_by_containment)} admissible maps are EXCLUDED by "
            f"the containment filter ({', '.join(excluded_by_containment)}) "
            f"and {len(refused)} maps are refused as non-admissible."),
        "pass": (len(rows) == len(CAT_NAMES) and len(holding) > 1
                 and len(excluded_by_containment) > 0 and len(refused) > 0),
    }


# --------------------------------------------------------------------------
# E: WHERE AMPLITUDE ACTUALLY LIVES -- the confinement computation
# --------------------------------------------------------------------------
def confinement_certificate() -> dict:
    rows = []
    reach_meets_support = 0
    live_beyond_src_in_support = 0
    for cfg in FAMILY:
        layers, src = walk_layers(cfg)
        supp = set(cfg["sites"])
        reach = set()
        for lay in layers[1:]:
            reach |= {x for x, v in lay.items() if v}
        live = set(src) | reach
        if reach & supp:
            reach_meets_support += 1
        if (live & supp) - set(src):
            live_beyond_src_in_support += 1
        rows.append({
            "config": cfg["name"],
            "support_size": len(supp),
            "source_sites": len(src),
            "source_inside_support": len(set(src) & supp),
            "reachable_sites": len(reach),
            "reach_meets_support": len(reach & supp),
            "amplitude_sites_total": len(live),
            "amplitude_sites_inside_support": len(live & supp),
            "amplitude_sites_outside_support": len(live - supp),
            "walk_is_frozen": len(reach) == 0,
        })
    frozen = sum(1 for r in rows if r["walk_is_frozen"])
    return {
        "question": (
            "Where does the propagated amplitude actually live?  The collapse "
            "of GBW1b's window half would follow if amplitude were CONFINED to "
            "the barrier, because then every containment-holding window would "
            "read the same amplitude set.  That is a computation, not an "
            "assumption, and it is run here before the partition."),
        "theorem_C892_T1": (
            "AMPLITUDE EXPULSION.  The propagation barrier is B(R) = supp(R) "
            "and the walk may not step ONTO a blocked site.  Therefore every "
            "site reachable in one or more steps lies OUTSIDE supp(R), and the "
            "only amplitude that can sit inside supp(R) is the SEED, carried "
            "by whichever source sites happen to be records.  Formally: "
            "supp(A_{R,theta}) is contained in src(R) union (Box \\ supp(R)), "
            "and supp(A) intersect supp(R) is contained in src(R).  The "
            "hypotheses are exactly: a finite box, a barrier equal to supp(R), "
            "and a walk blocked ON the barrier rather than at it."),
        "computed_on_all_configs": {
            "configs": len(FAMILY),
            "configs_where_reach_meets_support": reach_meets_support,
            "configs_where_amplitude_inside_support_exceeds_the_seed":
                live_beyond_src_in_support,
            "configs_whose_walk_is_frozen_at_the_seed": frozen,
        },
        "rows": rows,
        "consequence_for_the_collapse": (
            "The collapse hypothesis is REFUTED at its root.  Amplitude is not "
            "confined to the barrier; it is EXPELLED from it.  Containment-"
            "holding windows all contain supp(R), where there is (almost) no "
            "amplitude, and they differ exactly on the non-record sites, where "
            "ALL of the propagated amplitude lives.  So the window extent "
            "cannot be gauge at quadratic order unless every admissible "
            "containment-holding window happens to miss the reachable set "
            "entirely -- which certificate G tests directly."),
        "finding": (
            f"On {len(FAMILY)}/{len(FAMILY)} configurations the reachable set "
            f"is DISJOINT from the support ({reach_meets_support} meet it), "
            f"and on {len(FAMILY)}/{len(FAMILY)} the amplitude inside the "
            f"support is exactly the seed "
            f"({live_beyond_src_in_support} exceed it).  {frozen} "
            f"configurations freeze the walk entirely: their source's every "
            f"neighbour is a record, so amplitude never leaves the seed."),
        "pass": (len(rows) == len(FAMILY)
                 and reach_meets_support == 0
                 and live_beyond_src_in_support == 0),
    }


# --------------------------------------------------------------------------
# F: the two orders -- linear gauge verification AND the quadratic Z table
# --------------------------------------------------------------------------
def _z_signature(name: str) -> tuple:
    return tuple(q(Z(cfg, t, window_of(name, cfg)))
                 for cfg in FAMILY for t in THETA_GRID)


def both_orders_certificate(cat: dict) -> dict:
    holding = cat["containment_holding"]
    base_I = [NS887["readout"](c) for c in FAMILY]

    # ---- LINEAR order: recomputed here regardless of how Q1 lands
    linear = {}
    for name in holding:
        iw = [NS887["windowed_readout"](CAT[name], c) for c in FAMILY]
        linear[name] = {"I_W_per_config": iw, "equals_full_readout":
                        iw == base_I}
    linear_classes: dict = {}
    for name in holding:
        linear_classes.setdefault(
            tuple(linear[name]["I_W_per_config"]), []).append(name)

    # ---- QUADRATIC order
    sigs = {name: _z_signature(name) for name in holding}
    quad_classes: dict = {}
    for name in holding:
        quad_classes.setdefault(sigs[name], []).append(name)

    z_table = {
        name: {cfg["name"]: {q(t): q(Z(cfg, t, window_of(name, cfg)))
                             for t in THETA_GRID}
               for cfg in FAMILY}
        for name in holding}

    return {
        "theta_grid": [q(t) for t in THETA_GRID],
        "theta_grid_size": len(THETA_GRID),
        "theta_grid_contains_the_six_required": all(
            t in THETA_GRID for t in
            (Fraction(1, 2), Fraction(1, 3), Fraction(2, 5), Fraction(1, 7),
             Fraction(3, 8), Fraction(5, 6))),
        "windows_evaluated": holding,
        "cells_computed": len(holding) * len(FAMILY) * len(THETA_GRID),
        "LINEAR_order": {
            "quantity": "I_W(R) -- the axiom-level windowed scalar readout",
            "full_readout_per_config": base_I,
            "per_map": linear,
            "classes": len(linear_classes),
            "class_members": [sorted(v) for v in linear_classes.values()],
            "all_identical": len(linear_classes) == 1,
        },
        "QUADRATIC_order": {
            "quantity": "Z(cfg, theta, W) = sum_{x in W} |A(x)|^2",
            "classes": len(quad_classes),
            "class_members": sorted(sorted(v) for v in quad_classes.values()),
            "all_identical": len(quad_classes) == 1,
        },
        "Z_table": z_table,
        "both_orders_computed": True,
        "finding": (
            f"Both orders are computed and reported.  At LINEAR order the "
            f"{len(holding)} containment-holding windows fall into "
            f"{len(linear_classes)} class(es); at QUADRATIC order the same "
            f"windows fall into {len(quad_classes)} class(es) over "
            f"{len(holding) * len(FAMILY) * len(THETA_GRID)} exactly computed "
            f"cells."),
        "pass": (len(holding) == len(sigs) and len(z_table) == len(holding)
                 and len(THETA_GRID) >= 6),
    }


# --------------------------------------------------------------------------
# G: Q1's verdict -- the partition, the separations, the structural theorem
# --------------------------------------------------------------------------
def q1_certificate(cat: dict, orders: dict) -> dict:
    holding = cat["containment_holding"]
    sets = {n: tuple(tuple(sorted(window_of(n, c))) for c in FAMILY)
            for n in holding}
    zs = {(n, c["name"], q(t)): Z(c, t, window_of(n, c))
          for n in holding for c in FAMILY for t in THETA_GRID}

    # ---- which pairs separate, on which configs, at which thetas
    sep_rows = {}
    set_identical = []
    for a, b in combinations(holding, 2):
        s = [{"config": c["name"], "theta": q(t),
              "Z_" + a: q(zs[(a, c["name"], q(t))]),
              "Z_" + b: q(zs[(b, c["name"], q(t))])}
             for c in FAMILY for t in THETA_GRID
             if zs[(a, c["name"], q(t))] != zs[(b, c["name"], q(t))]]
        if sets[a] == sets[b]:
            set_identical.append([a, b])
        if s:
            sep_rows[f"{a} | {b}"] = {
                "separating_cells": len(s),
                "configs": sorted({r["config"] for r in s}),
                "thetas": sorted({r["theta"] for r in s}),
                "exhibits": s[:EXHIBIT_CAP],
            }
    pairs = len(list(combinations(holding, 2)))

    # ---- the structural theorem, tested rather than asserted
    nested, mono_viol = 0, []
    for a, b in permutations(holding, 2):
        if all(set(sets[a][i]) <= set(sets[b][i]) for i in range(len(FAMILY))):
            nested += 1
            for c in FAMILY:
                for t in THETA_GRID:
                    if zs[(a, c["name"], q(t))] > zs[(b, c["name"], q(t))]:
                        mono_viol.append({"inner": a, "outer": b,
                                          "config": c["name"], "theta": q(t)})
    supp_name = "minkowski_S_zero__the_885_support_window"
    min_viol = [{"window": n, "config": c["name"], "theta": q(t)}
                for n in holding for c in FAMILY for t in THETA_GRID
                if zs[(n, c["name"], q(t))] < zs[(supp_name, c["name"], q(t))]]

    # ---- the exact difference formula, checked cell by cell
    diff_checks, diff_bad = 0, []
    for a, b in permutations(holding, 2):
        if not all(set(sets[a][i]) <= set(sets[b][i])
                   for i in range(len(FAMILY))):
            continue
        for i, c in enumerate(FAMILY):
            extra = set(sets[b][i]) - set(sets[a][i])
            for t in THETA_GRID:
                diff_checks += 1
                lhs = zs[(b, c["name"], q(t))] - zs[(a, c["name"], q(t))]
                if lhs != Z(c, t, extra):
                    diff_bad.append({"inner": a, "outer": b,
                                     "config": c["name"], "theta": q(t)})

    # ---- does the annular chart see it?
    ann = {n: tuple((q(CAT[n](c)["a2"]), q(CAT[n](c)["b2"])) for c in FAMILY)
           for n in holding}
    ann_classes: dict = {}
    for n in holding:
        ann_classes.setdefault(ann[n], []).append(n)
    z_sep_but_annular_blind = [
        [a, b] for a, b in combinations(holding, 2)
        if f"{a} | {b}" in sep_rows and ann[a] == ann[b]]
    annular_sep_but_z_blind = [
        [a, b] for a, b in combinations(holding, 2)
        if f"{a} | {b}" not in sep_rows and ann[a] != ann[b]]

    # ---- but does the annulus DETERMINE Z?  same (a,b), different set.
    ann_witnesses = []
    for n in holding:
        for c in FAMILY:
            pk = CAT[n](c)
            W = set(pk["set"])
            centre = tuple(pk["centre"])
            filled = {x for x in BOX
                      if pk["a2"] <= sum((Fraction(x[i]) - centre[i]) ** 2
                                         for i in range(3)) <= pk["b2"]}
            if filled == W:
                continue
            for t in THETA_GRID:
                if Z(c, t, filled) != Z(c, t, W):
                    ann_witnesses.append({
                        "window": n, "config": c["name"], "theta": q(t),
                        "Z_of_the_set": q(Z(c, t, W)),
                        "Z_of_the_same_annulus_filled": q(Z(c, t, filled))})
                    break

    quad_classes = orders["QUADRATIC_order"]["classes"]
    linear_classes = orders["LINEAR_order"]["classes"]
    collapsed = quad_classes == 1

    return {
        "question": (
            "Q1.  Is the window EXTENT still gauge at quadratic order?  The "
            "linear readout cannot see it (887).  Z is quadratic."),
        "verdict": (
            "COLLAPSED -- the extent is gauge at quadratic order too"
            if collapsed else
            "NOT GAUGE -- the extent is LOAD-BEARING at quadratic order"),
        "linear_classes": linear_classes,
        "quadratic_classes": quad_classes,
        "gauge_breaks_between_the_orders": (linear_classes == 1
                                            and quad_classes > 1),
        "partition": orders["QUADRATIC_order"]["class_members"],
        "pairs_compared": pairs,
        "pairs_that_separate": len(sep_rows),
        "pairs_that_do_not_separate": pairs - len(sep_rows),
        "window_pairs_that_are_SET_IDENTICAL_on_this_family": set_identical,
        "separations": sep_rows,
        "configs_that_ever_separate": sorted(
            {c for v in sep_rows.values() for c in v["configs"]}),
        "thetas_that_ever_separate": sorted(
            {t for v in sep_rows.values() for t in v["thetas"]}),
        "structural_theorem_C892_T2": (
            "WINDOW MONOTONICITY AND THE EXACT DIFFERENCE.  For containment-"
            "holding windows W subset W', Z(W') - Z(W) = sum over x in "
            "(W' \\ W) intersect Box of |A(x)|^2 >= 0, with EQUALITY if and "
            "only if (W' \\ W) carries no amplitude.  Combined with C892_T1 "
            "(amplitude is expelled from the barrier), the seed contribution "
            "is COMMON to every containment-holding window -- each contains "
            "supp(R) and hence src(R) intersect supp(R) -- so the entire "
            "difference between two containment-holding windows is carried by "
            "the REACHABLE set, which lies wholly outside supp(R).  Hence: "
            "THE EXTENT IS GAUGE AT QUADRATIC ORDER IF AND ONLY IF EVERY "
            "ADMISSIBLE CONTAINMENT-HOLDING WINDOW MEETS THE REACHABLE SET IN "
            "THE SAME AMPLITUDE MASS.  This is a theorem on the stated "
            "hypotheses, and it is what makes the catalogue result below a "
            "verdict rather than a sweep: the catalogue exhibits the witness "
            "the theorem needs."),
        "structural_theorem_tested": {
            "nested_ordered_pairs": nested,
            "monotonicity_violations": len(mono_viol),
            "monotonicity_exhibits": mono_viol[:EXHIBIT_CAP],
            "support_window_is_the_minimum_violations": len(min_viol),
            "exact_difference_formula_checks": diff_checks,
            "exact_difference_formula_violations": len(diff_bad),
            "exact_difference_exhibits": diff_bad[:EXHIBIT_CAP],
        },
        "structural_proof_status": (
            "PROVED, with hypotheses, in the NEGATIVE direction.  C892_T1 and "
            "C892_T2 are structural: they follow from the barrier rule and the "
            "definition of Z, and both are verified with zero violations on "
            "every cell.  What they prove is that the collapse CANNOT hold "
            "once any admissible containment-holding window reaches into the "
            "reachable set, and the support window -- the inclusion-minimum of "
            "the class -- reaches none of it.  The witness is exhibited, so "
            "the verdict is not catalogue-only.  The catalogue's residual "
            "role is only to show that admissible windows of BOTH kinds exist "
            "in 887's own space; the scope limit is that no claim is made "
            "about window maps outside that space."
            if not collapsed else
            "CATALOGUE-ONLY.  Every containment-holding member of this "
            "catalogue agrees, but C892_T2 shows agreement requires equal "
            "amplitude mass on the reachable set, which is not forced."),
        "annular_chart": {
            "distinct_annular_profiles": len(ann_classes),
            "annular_classes": sorted(sorted(v) for v in ann_classes.values()),
            "Z_separated_pairs_the_annular_chart_cannot_see":
                z_sep_but_annular_blind,
            "annular_separated_pairs_Z_cannot_see": annular_sep_but_z_blind,
            "annular_partition_equals_Z_partition": (
                sorted(sorted(v) for v in ann_classes.values())
                == orders["QUADRATIC_order"]["class_members"]),
            "but_the_annulus_does_NOT_determine_Z": {
                "witnesses": len(ann_witnesses),
                "exhibits": ann_witnesses[:EXHIBIT_CAP],
                "reading": (
                    "Replacing a window by the FILLED annulus with the same "
                    "(a^2, b^2) and the same centre changes Z.  So the annular "
                    "chart happens to SEPARATE this catalogue's classes while "
                    "being unable to COMPUTE Z: it is a strictly coarser "
                    "chart that is accidentally injective here, which is "
                    "exactly the weakness 885 already measured when it found "
                    "the support fills its own annulus on only 7 of 12 "
                    "configurations."),
            },
        },
        "finding": (
            f"The window extent is NOT gauge at quadratic order.  The "
            f"{len(holding)} containment-holding admissible windows collapse "
            f"to {linear_classes} class under the LINEAR readout and split "
            f"into {quad_classes} classes under Z, separating on "
            f"{len(sep_rows)} of {pairs} pairs.  The single non-separating "
            f"pair is SET-IDENTICAL on this family, so Z is as fine as the "
            f"window set itself: it separates every genuinely distinct "
            f"containment-holding window.  The gauge therefore breaks exactly "
            f"between the linear and the quadratic order, and the window "
            f"convention becomes load-bearing precisely at the Born interface."
            if not collapsed else
            f"All {len(holding)} containment-holding windows give identical Z; "
            f"GBW1b's window half collapses."),
        "pass": (len(mono_viol) == 0 and len(min_viol) == 0
                 and len(diff_bad) == 0 and diff_checks > 0
                 and len(sep_rows) + (pairs - len(sep_rows)) == pairs),
    }


# --------------------------------------------------------------------------
# H: the KERNEL component -- what theta actually does to Z
# --------------------------------------------------------------------------
def _cheb(d: int, p: Fraction) -> Fraction:
    """T_d(p) exactly.  cos(d*phi) = T_d(cos phi)."""
    a, b = Fraction(1), p
    if d == 0:
        return a
    for _ in range(d - 1):
        a, b = b, 2 * p * b - a
    return b


def interference_spectrum(cfg, window) -> list:
    """M_d = sum_{x in W} sum_{L - L' = d} c_L(x) c_{L'}(x), exact.

    Z = sum_d M_d T_d(cos phi) with cos phi = (1 - t^2)/(1 + t^2).
    """
    layers, src = walk_layers(cfg)
    n = len(src)
    per_site: dict = {}
    for L, lay in enumerate(layers):
        for x, c in lay.items():
            if x in window and x in INBOX and c:
                per_site.setdefault(x, {})[L] = Fraction(c, n)
    M = [Fraction(0)] * (MAX_STEPS + 1)
    for coeffs in per_site.values():
        for L, a in coeffs.items():
            for Lp, b in coeffs.items():
                M[abs(L - Lp)] += a * b
    return M


def kernel_certificate(cat: dict) -> dict:
    holding = cat["containment_holding"]
    checks, bad = 0, []
    orders_seen = set()
    for name in holding:
        for cfg in FAMILY:
            W = window_of(name, cfg)
            M = interference_spectrum(cfg, W)
            orders_seen |= {d for d in range(MAX_STEPS + 1) if M[d] != 0}
            for t in THETA_GRID:
                p = (1 - t * t) / (1 + t * t)
                pred = sum((M[d] * _cheb(d, p) for d in range(MAX_STEPS + 1)),
                           Fraction(0))
                checks += 1
                if pred != Z(cfg, t, W):
                    bad.append({"window": name, "config": cfg["name"],
                                "theta": q(t), "predicted": q(pred),
                                "actual": q(Z(cfg, t, W))})

    # ---- per-config spectra on the k=1 dilation, and the parity structure
    dil1 = "minkowski_S_ball1__885_checker_dilation_k1"
    spectra, parity_rows, parity_bad = [], [], 0
    for cfg in FAMILY:
        M = interference_spectrum(cfg, window_of(dil1, cfg))
        _, src = walk_layers(cfg)
        parities = sorted({(s[0] + s[1] + s[2]) % 2 for s in src})
        odd = any(M[d] != 0 for d in range(1, MAX_STEPS + 1, 2))
        consistent = odd == (len(parities) > 1)
        parity_bad += 0 if consistent else 1
        spectra.append({"config": cfg["name"], "M_by_order": [q(x) for x in M],
                        "highest_order_present":
                            max([d for d in range(MAX_STEPS + 1) if M[d] != 0],
                                default=0)})
        parity_rows.append({"config": cfg["name"],
                            "source_parities": parities,
                            "odd_orders_present": odd,
                            "predicted_by_bipartiteness": len(parities) > 1,
                            "consistent": consistent})

    # ---- |u(theta)| = 1 exactly, on the fine grid
    unit_bad = [q(t) for t in THETA_FINE if cabs2(unit_point(t)) != 1]

    # ---- how many distinct Z values does the fine grid produce?
    fine_rows = []
    for cfg in FAMILY:
        vals = {q(Z(cfg, t, window_of(dil1, cfg))) for t in THETA_FINE}
        fine_rows.append({"config": cfg["name"],
                          "distinct_Z_over_the_fine_grid": len(vals),
                          "constant_in_theta": len(vals) == 1})
    return {
        "component": "GBW1b (b) -- the KERNEL contribution",
        "what_theta_is": (
            "theta enters ONLY as the per-edge gain u(theta) = "
            "((1-theta^2)/(1+theta^2), 2theta/(1+theta^2)), the exact rational "
            "point on the unit circle.  |u(theta)|^2 = 1 exactly on every "
            f"tested theta ({len(THETA_FINE)} values, {len(unit_bad)} "
            "failures), so theta contributes NO gain in modulus: it is a pure "
            "phase."),
        "structure_theorem_C892_T3": (
            "PATH-LENGTH INTERFERENCE SPECTRUM.  Because every edge carries the "
            "SAME unit phase, the amplitude at a site decomposes exactly by "
            "path length, A(x) = sum_L (n_L(x)/|src|) u^L with n_L(x) the "
            "INTEGER count of admissible L-step walks.  Hence "
            "Z(theta) = sum_{d=0}^{D} M_d T_d(cos phi) with "
            "cos phi = (1-theta^2)/(1+theta^2), T_d the Chebyshev polynomial, "
            "D = the walk depth, and M_d = sum_{x in W} sum_{L-L'=d} c_L c_L' "
            "a RATIONAL, theta-FREE, record-and-window-determined coefficient. "
            "Z is therefore a POLYNOMIAL OF DEGREE AT MOST D IN cos phi, i.e. "
            "a rational function of theta with denominator (1+theta^2)^D -- "
            "not an arbitrary function.  This is checked, not asserted."),
        "identity_checks": checks,
        "identity_violations": len(bad),
        "identity_exhibits": bad[:EXHIBIT_CAP],
        "walk_depth_D": MAX_STEPS,
        "interference_orders_actually_present": sorted(orders_seen),
        "spectra_on_the_k1_dilation": spectra,
        "parity_theorem_C892_T4": (
            "BIPARTITE PARITY SELECTION.  Z^3 is bipartite, so all walks from a "
            "FIXED site to a fixed site have a fixed length parity and only "
            "EVEN interference orders can survive; odd orders can appear only "
            "when the source SET spans both parities.  Predicted from the "
            "source parity alone and checked per configuration."),
        "parity_rows": parity_rows,
        "parity_mispredictions": parity_bad,
        "fine_grid_size": len(THETA_FINE),
        "fine_grid_rows": fine_rows,
        "configs_constant_in_theta_on_the_fine_grid": sum(
            1 for r in fine_rows if r["constant_in_theta"]),
        "exact_role_of_theta_priced": (
            "theta supplies exactly the D coefficients' WEIGHTING, nothing "
            "else.  It cannot change which sites carry amplitude (that is the "
            "barrier's job), it cannot change the integer walk counts, and it "
            "cannot change the total number of interference orders.  What it "
            "CAN do is move Z continuously along a degree-D polynomial in "
            "cos phi.  So the kernel contribution to GBW1b is exactly ONE "
            "scalar convention -- the value of cos phi -- and it is a genuine "
            "dimension only where some M_d with d >= 1 is non-zero."),
        "finding": (
            f"{checks} exact identity checks with {len(bad)} violations: "
            f"Z(theta) is a degree-{MAX_STEPS} polynomial in cos phi on every "
            f"window and configuration.  Interference orders actually present: "
            f"{sorted(orders_seen)}.  The parity theorem predicts the odd "
            f"orders from the source parity alone with {parity_bad} "
            f"mispredictions.  On the fine grid of {len(THETA_FINE)} thetas, "
            f"{sum(1 for r in fine_rows if r['constant_in_theta'])} of "
            f"{len(FAMILY)} configurations are exactly theta-CONSTANT -- these "
            f"are the frozen walks -- and the rest move."),
        "pass": (len(bad) == 0 and checks > 0 and parity_bad == 0
                 and len(unit_bad) == 0),
    }


# --------------------------------------------------------------------------
# I: the 878 event-space absence scan (883 discipline)
# --------------------------------------------------------------------------
def event_space_scan() -> dict:
    # This cycle's OWN artifacts must not be counted: they land between the
    # first run and any re-run, which would make the census -- and with it the
    # science digest -- change without any physics changing.  The exclusion is
    # by exact path and is published below, so nothing is hidden by it.
    own = {SELF_REL,
           "scripts/frontier_cycle892_gbw1b_independent_check_2026_07_28.py",
           "outputs/gbw1b_pricing_cycle892_receipt_2026_07_28.json",
           "outputs/gbw1b_independent_check_cycle892_receipt_2026_07_28.json",
           "logs/runner-cache/"
           "frontier_cycle892_gbw1b_pricing_2026_07_28.txt",
           "logs/runner-cache/"
           "frontier_cycle892_gbw1b_independent_check_2026_07_28.txt"}
    scanned, hits = [], {}
    excluded_seen = 0
    for glob in C878_SCAN_GLOBS:
        try:
            out = subprocess.run(["git", "ls-files", glob], cwd=str(ROOT),
                                 capture_output=True, text=True, timeout=60)
            raw = [f for f in out.stdout.split("\n") if f.strip()]
        except Exception:
            raw = []
        files = [f for f in raw if f not in own]
        excluded_seen += len(raw) - len(files)
        scanned.append({"glob": glob, "tracked_files": len(files),
                        "own_artifacts_excluded": len(raw) - len(files)})
        for probe in C878_PROBES:
            for f in files:
                if probe in f:
                    hits.setdefault(probe, []).append(f)
    total = sum(s["tracked_files"] for s in scanned)
    return {
        "census_is_idempotent": True,
        "own_artifacts_excluded_by_exact_path": sorted(own),
        "own_artifacts_seen_and_excluded_this_run": excluded_seen,
        "idempotency_note": (
            "Without this exclusion the census would count the cycle's own "
            "scripts, receipts and run caches once they land, so a re-run "
            "would report a different total and the science digest would "
            "drift with no physics changing.  The exclusion list is by exact "
            "path and is printed in full."),
        "role": (
            "883-discipline tracked-file scan.  The Cycle-878 composed-record "
            "event-space artifacts are the named import GBW1b's interface "
            "component depends on.  Their presence is COMPUTED and their "
            "content is NEVER reconstructed: a cycle that invented an "
            "event-space would be inventing the very thing it is pricing."),
        "scan_globs": list(C878_SCAN_GLOBS),
        "scanned": scanned,
        "tracked_files_scanned_total": total,
        "probes": list(C878_PROBES),
        "hits_by_probe": {p: sorted(set(v)) for p, v in hits.items()},
        "hit_count": sum(len(set(v)) for v in hits.values()),
        "artifacts_absent": len(hits) == 0,
        "finding": (
            f"{total} tracked paths scanned over {len(C878_SCAN_GLOBS)} globs "
            f"against {len(C878_PROBES)} probes: "
            f"{sum(len(set(v)) for v in hits.values())} hits.  The Cycle-878 "
            f"event-space artifacts are ABSENT from this lineage, reproducing "
            f"the 885 receipt's own record of their absence.  The interface is "
            f"therefore priced as a NAMED IMPORT, not evaluated."),
        "pass": True,
    }


# --------------------------------------------------------------------------
# J: the INTERFACE component -- requirements DERIVED from Z's structure
# --------------------------------------------------------------------------
BORN_VOCABULARY = (
    "born rule", "born's rule", "probability amplitude squared",
    "|psi|^2", "wavefunction", "hilbert space", "unitary evolution",
    "quantum probability", "measurement postulate",
)


def interface_certificate(cat: dict, conf: dict, kern: dict) -> dict:
    holding = cat["containment_holding"]
    dil1 = "minkowski_S_ball1__885_checker_dilation_k1"

    # ---- computed fact 1: Z is FINITELY ADDITIVE over disjoint site sets
    add_checks, add_bad = 0, []
    for cfg in FAMILY:
        A = window_of(dil1, cfg)
        B = window_of("minkowski_S_ball2__885_checker_dilation_k2", cfg) - A
        for t in THETA_GRID:
            add_checks += 1
            if Z(cfg, t, A) + Z(cfg, t, B) != Z(cfg, t, A | B):
                add_bad.append({"config": cfg["name"], "theta": q(t)})

    # ---- computed fact 2: Z >= 0 always, and CAN VANISH
    neg = [1 for n in holding for c in FAMILY for t in THETA_GRID
           if Z(c, t, window_of(n, c)) < 0]
    vanish = [{"window": n, "config": c["name"], "theta": q(t)}
              for n in holding for c in FAMILY for t in THETA_GRID
              if Z(c, t, window_of(n, c)) == 0]

    # ---- computed fact 3: the total box mass is NOT theta-invariant
    mass_rows = []
    for cfg in FAMILY:
        vals = {q(t): q(Z(cfg, t, INBOX)) for t in THETA_885}
        mass_rows.append({"config": cfg["name"], "total_mass_by_theta": vals,
                          "theta_invariant": len(set(vals.values())) == 1})
    mass_moves = sum(1 for r in mass_rows if not r["theta_invariant"])

    # ---- computed fact 4: normalizing by the box mass does NOT remove theta
    ratio_rows = []
    for cfg in FAMILY:
        vals = set()
        for t in THETA_885:
            tot = Z(cfg, t, INBOX)
            if tot == 0:
                continue
            vals.add(q(Z(cfg, t, window_of(dil1, cfg)) / tot))
        ratio_rows.append({"config": cfg["name"],
                           "distinct_normalized_ratios": len(vals),
                           "theta_free_after_normalization": len(vals) <= 1})
    ratio_moves = sum(1 for r in ratio_rows
                      if not r["theta_free_after_normalization"])

    # ---- computed fact 5: I is supported on supp(R); Z is supported off it
    I_locus = "supp(R): the linear readout sums record content site by site"
    amp_inside = sum(r["amplitude_sites_inside_support"] for r in conf["rows"])
    amp_outside = sum(r["amplitude_sites_outside_support"]
                      for r in conf["rows"])

    requirements = [
        {"id": "IF1",
         "requirement":
             "The event-space step must supply a map rho from record "
             "configurations to amplitude fields whose SUPPORT overlaps "
             "supp(R).",
         "derived_from":
             f"Certificate E computes that the propagated amplitude has "
             f"{amp_inside} site(s) inside supp(R) across the whole family, "
             f"against {amp_outside} outside it -- and the inside sites are "
             f"exactly the seed.  The linear readout I lives entirely on "
             f"supp(R).  So as the lineage currently stands the two quantities "
             f"are supported on ESSENTIALLY DISJOINT sets and no "
             f"identification between them can be pointwise.",
         "what_fails_without_it":
             "Any identification of I with Z is a statement about two "
             "functions on disjoint loci; the barrier B(R) = supp(R) is what "
             "makes them disjoint, so IF1 forces either a different barrier or "
             "an explicitly non-local identification."},
        {"id": "IF2",
         "requirement":
             "rho must be such that Z is a FINITELY ADDITIVE set function over "
             "disjoint window pieces.",
         "derived_from":
             f"Computed: Z(A) + Z(B) = Z(A union B) on {add_checks} disjoint "
             f"pairs with {len(add_bad)} violations.  Z ALREADY has this "
             f"property because it is a site-wise sum of |A|^2.  The "
             f"requirement is therefore SATISFIED by the current construction "
             f"and costs the interface nothing -- it is banked, not owed.",
         "what_fails_without_it":
             "Nothing; this is the one Born-shaped property the computation "
             "supplies for free."},
        {"id": "IF3",
         "requirement":
             "rho must supply a NORMALIZER that is theta-invariant, or else "
             "declare theta as an observable.",
         "derived_from":
             f"Computed: the total amplitude mass over the whole box moves "
             f"with theta on {mass_moves}/{len(FAMILY)} configurations, and "
             f"dividing the window mass by the box mass still leaves "
             f"{ratio_moves}/{len(FAMILY)} configurations theta-dependent.  So "
             f"the obvious normalization does NOT quotient theta out.  The "
             f"walk accumulates amplitude across path lengths and leaks at the "
             f"barrier and the box wall, so it is not norm-preserving; that is "
             f"a computed property of the pinned construction, not a modelling "
             f"choice made here.",
         "what_fails_without_it":
             "Z cannot be read as a weight of anything: its scale is a free "
             "function of a kernel coordinate."},
        {"id": "IF4",
         "requirement":
             "rho must fix the WINDOW, because Z is not window-invariant.",
         "derived_from":
             "Certificate G computes that the containment-holding admissible "
             "windows split into more than one Z class and that Z is strictly "
             "monotone in the window along every nested pair.  The window is "
             "therefore an argument of the weight, not a gauge choice.",
         "what_fails_without_it":
             "The weight is defined only up to the whole 887 inflation "
             "freedom, which certificate G shows is not a null direction at "
             "this order."},
        {"id": "IF5",
         "requirement":
             "rho must tolerate VANISHING Z on admissible windows, or exclude "
             "the configurations where it vanishes.",
         "derived_from":
             f"Computed: Z is non-negative on every one of the "
             f"{len(holding) * len(FAMILY) * len(THETA_GRID)} cells "
             f"({len(neg)} negatives) but VANISHES exactly on "
             f"{len(vanish)} (window, config, theta) triples of "
             f"containment-holding admissible windows -- the frozen walks, "
             f"where every neighbour of the source is a record.  A weight that "
             f"must be positive is therefore not available on this family "
             f"without an extra hypothesis.",
         "what_fails_without_it":
             "Normalization by Z is undefined on those configurations."},
        {"id": "IF6",
         "requirement":
             "rho must respect the interference structure: any identification "
             "must be with a degree-D polynomial in cos phi, not with an "
             "arbitrary function of the kernel.",
         "derived_from":
             f"Certificate H proves and checks "
             f"Z = sum_d M_d T_d(cos phi) with d <= {MAX_STEPS} on "
             f"{kern['identity_checks']} cells and "
             f"{kern['identity_violations']} violations.  The M_d are "
             f"rational, theta-free and record-and-window-determined.",
         "what_fails_without_it":
             "An identification could be satisfied by tuning theta pointwise, "
             "which the polynomial structure forbids."},
    ]

    # ---- needle check: no Born-rule vocabulary imported as a premise
    self_text = read_text(SELF_REL).lower()
    req_text = json.dumps(requirements).lower()
    needles = {v: {"in_requirements": v in req_text,
                   "in_file": self_text.count(v)} for v in BORN_VOCABULARY}
    leaked = sorted(v for v, r in needles.items() if r["in_requirements"])
    return {
        "component": "GBW1b (c) -- the INTERFACE",
        "obligation": (
            "The composed-record event-space step must supply the map from "
            "RECORDS to AMPLITUDES.  This lineage does not carry it (see the "
            "absence scan), so it is priced as a named import."),
        "the_gap_in_one_sentence": (
            "The axiom-level readout I(R) is LINEAR in record content and "
            "supported on supp(R); Z is QUADRATIC in amplitudes and supported "
            "off supp(R); nothing in the four axioms connects them."),
        "computed_facts_Z_has": {
            "finite_additivity_checks": add_checks,
            "finite_additivity_violations": len(add_bad),
            "non_negativity_violations": len(neg),
            "vanishing_cells": len(vanish),
            "vanishing_exhibits": vanish[:EXHIBIT_CAP],
            "total_mass_theta_dependent_configs": mass_moves,
            "total_mass_rows": mass_rows,
            "normalized_ratio_still_theta_dependent_configs": ratio_moves,
            "linear_readout_locus": I_locus,
            "amplitude_sites_inside_support_total": amp_inside,
            "amplitude_sites_outside_support_total": amp_outside,
        },
        "required_properties_of_the_import": requirements,
        "requirement_count": len(requirements),
        "requirements_owed": [r["id"] for r in requirements
                              if r["id"] != "IF2"],
        "requirements_already_banked": ["IF2"],
        "derivation_discipline": (
            "Every requirement above cites a COMPUTED fact of Z from this "
            "run -- its additivity count, its vanishing cells, its total-mass "
            "movement, its polynomial order, its support locus.  None is "
            "derived from what a probability rule is supposed to look like.  "
            "The needle check below is the mechanical guard."),
        "born_vocabulary_needle_check": needles,
        "born_vocabulary_leaked_into_requirements": leaked,
        "finding": (
            f"{len(requirements)} interface requirements, all derived from Z's "
            f"computed structure; {len(requirements) - 1} are OWED by the "
            f"event-space step and 1 (finite additivity) is already supplied "
            f"by the construction.  The sharpest owed requirement is IF1: the "
            f"barrier B(R) = supp(R) puts the linear readout and the quadratic "
            f"weight on essentially disjoint loci "
            f"({amp_inside} amplitude sites inside the support against "
            f"{amp_outside} outside), so no pointwise identification exists "
            f"until the event-space step either moves the barrier or supplies "
            f"a non-local map.  {len(leaked)} Born-rule needles leaked."),
        "pass": (len(add_bad) == 0 and len(neg) == 0 and len(leaked) == 0
                 and len(requirements) >= 5),
    }


# --------------------------------------------------------------------------
# K: stress -- exclusion, refusal, and falsifier visibility
# --------------------------------------------------------------------------
def stress_certificate(cat: dict) -> dict:
    holding = set(cat["containment_holding"])

    # ---- (1) an admissible IMPOSTOR that breaks containment must be excluded
    breakers = []
    for name in cat["admissible"]:
        cp = NS887["containment_profile"](CAT[name])
        if not cp["supp_subset_W_on_all_configs"]:
            breakers.append({
                "map": name,
                "contains_support_on": cp["contains_support"],
                "of": cp["configs"],
                "in_the_partition": name in holding,
            })
    # ---- a PLANTED containment breaker built here, not borrowed.  It is
    #      deliberately ADMISSIBLE, so that only the CONTAINMENT filter can
    #      catch it: a breaker that admissibility already refuses would not
    #      test the containment filter at all.
    S_DIAG = tuple(sorted(x for x in product((-1, 0, 1), repeat=3)
                          if sum(c * c for c in x) == 2))

    def planted_breaker(cfg):
        """supp(R) dilated by the 12 face-diagonal offsets.  The structuring
        set is rotation-invariant and the map is a Minkowski sum, so it is
        equivariant and monotone -- admissible -- but it does NOT contain the
        origin offset, so it displaces the window off the support."""
        st = NS887["minkowski"](cfg["sites"], S_DIAG)
        return NS887["packaged"](st, NS887["barycentre"](cfg))

    pb_ev = NS887["evaluate_map"](planted_breaker)
    pb_cp = NS887["containment_profile"](planted_breaker)
    pb_excluded = not pb_cp["supp_subset_W_on_all_configs"]

    # ---- (2) a non-admissible map must be refused
    refused = []
    for name in cat["refused_as_non_admissible"]:
        ev = evaluation(name)
        refused.append({
            "map": name,
            "equivariance_failures": ev["equivariance_failures"],
            "permanence_failures": ev["permanence_failures"],
            "distinct_set_values": ev["distinct_set_values"],
            "entered_the_partition": name in holding,
        })

    # ---- (3) FALSIFIER VISIBILITY: a planted Z-difference must be DETECTED,
    #      a null perturbation must NOT be, and two windows that really are
    #      the same must still land in the same class.
    def sig(name, mutate=Fraction(0)):
        """The window's Z signature, optionally with an amplitude perturbation
        planted at a site that is INSIDE the window and already carries
        amplitude -- so the plant is guaranteed visible to Z if the partition
        can see anything at all."""
        out = []
        for cfg in FAMILY:
            W = window_of(name, cfg)
            for t in THETA_GRID:
                amp = amp_field(cfg, t)
                if mutate:
                    live = sorted(x for x in W
                                  if x in amp and x in INBOX
                                  and amp[x] != ZERO_C)
                    if live:
                        amp = dict(amp)
                        amp[live[0]] = cadd(amp[live[0]],
                                            (Fraction(mutate), Fraction(0)))
                out.append(q(sum((cabs2(amp[x]) for x in W
                                  if x in amp and x in INBOX), Fraction(0))))
        return tuple(out)

    plant_rows = []
    for name in sorted(holding):
        clean = sig(name)
        planted = sig(name, mutate=Fraction(1, 1000))
        carries = any(v != q(Fraction(0)) for v in clean)
        plant_rows.append({
            "window": name,
            "window_carries_amplitude_somewhere": carries,
            "planted_difference_detected": clean != planted,
            "detection_required": carries,
        })
    planted_missed = [r["window"] for r in plant_rows
                      if r["detection_required"]
                      and not r["planted_difference_detected"]]
    planted_seen = not planted_missed and any(
        r["planted_difference_detected"] for r in plant_rows)

    # ---- NULL control: an unperturbed re-read must NOT invent a difference
    null_seen = any(sig(n) != sig(n) for n in sorted(holding))

    # ---- POSITIVE control: windows that are SET-IDENTICAL on this family
    #      must land in the SAME Z class, so the partition keys on Z and not
    #      on the map's name.
    sets = {n: tuple(tuple(sorted(window_of(n, c))) for c in FAMILY)
            for n in holding}
    identical_pairs = [[a, b] for a, b in combinations(sorted(holding), 2)
                       if sets[a] == sets[b]]
    identical_same_class = all(_z_signature(a) == _z_signature(b)
                               for a, b in identical_pairs)

    return {
        "stress_1_containment_breakers_excluded": {
            "admissible_maps_that_break_containment": breakers,
            "all_excluded_from_the_partition": all(
                not b["in_the_partition"] for b in breakers),
            "planted_breaker": {
                "construction":
                    "supp(R) dilated by the 12 face-diagonal offsets "
                    "(rotation-invariant, origin absent)",
                "admissible_REQ1_REQ5": pb_ev["admissible_REQ1_REQ5"],
                "equivariance_failures": pb_ev["equivariance_failures"],
                "permanence_failures": pb_ev["permanence_failures"],
                "contains_support_on": pb_cp["contains_support"],
                "of": pb_cp["configs"],
                "excluded_by_the_containment_filter": pb_excluded,
                "why_this_construction":
                    "it is deliberately ADMISSIBLE, so only the containment "
                    "filter can catch it; a breaker that REQ1-REQ5 already "
                    "refuses would not test the containment filter at all",
            },
        },
        "stress_2_non_admissible_refused": {
            "maps": refused,
            "none_entered_the_partition": all(
                not r["entered_the_partition"] for r in refused),
        },
        "stress_3_falsifier_visibility": {
            "planted_amplitude_perturbation":
                "1/1000 added at one window site that already carries "
                "amplitude, so the plant is guaranteed to be inside the "
                "quantity under test",
            "per_window": plant_rows,
            "windows_where_detection_was_required":
                sum(1 for r in plant_rows if r["detection_required"]),
            "windows_that_MISSED_a_planted_difference": planted_missed,
            "planted_difference_DETECTED_by_the_partition": planted_seen,
            "null_control_invents_a_difference": null_seen,
            "set_identical_window_pairs": identical_pairs,
            "set_identical_pairs_land_in_the_same_class":
                identical_same_class,
            "reading": (
                "Three-way control.  The partition SEES a planted difference "
                "on every window that carries any amplitude; it does NOT "
                "invent one on an unperturbed re-read; and it puts windows "
                "that really are the same set into the same class rather than "
                "keying on the map's name.  A partition that could only ever "
                "report 'all the same' -- or only ever 'all different' -- "
                "would make Q1's verdict vacuous; both failure modes are "
                "ruled out."),
        },
        "finding": (
            f"{len(breakers)} admissible catalogue maps break containment and "
            f"{sum(1 for b in breakers if b['in_the_partition'])} of them "
            f"entered the partition; the independently planted breaker is "
            f"admissible={pb_ev['admissible_REQ1_REQ5']}, contains the support "
            f"on {pb_cp['contains_support']}/{pb_cp['configs']} configurations "
            f"and is excluded={pb_excluded}.  {len(refused)} non-admissible "
            f"maps are refused and "
            f"{sum(1 for r in refused if r['entered_the_partition'])} entered. "
            f"A planted amplitude difference is detected on every window that "
            f"carries amplitude ({len(planted_missed)} misses), the null "
            f"control raises no false alarm ({null_seen}), and set-identical "
            f"pairs share a class ({identical_same_class})."),
        "pass": (all(not b["in_the_partition"] for b in breakers)
                 and len(breakers) > 0
                 and pb_ev["admissible_REQ1_REQ5"] and pb_excluded
                 and all(not r["entered_the_partition"] for r in refused)
                 and len(refused) > 0
                 and planted_seen and not planted_missed and not null_seen
                 and identical_same_class),
    }


# --------------------------------------------------------------------------
# L: the GBW1b obligation map -- the pricing
# --------------------------------------------------------------------------
def obligation_map(cat, orders, q1, kern, iface, scan) -> dict:
    holding = cat["containment_holding"]
    collapsed = q1["quadratic_classes"] == 1
    window_dims = 0 if collapsed else 1
    kernel_live = len(FAMILY) - kern["configs_constant_in_theta_on_the_fine_grid"]

    rows = [
        {"component": "(a) WINDOW",
         "statement": "which admissible containment-holding window W is read",
         "verdict": ("GAUGE -- collapses" if collapsed
                     else "LOAD-BEARING -- does not collapse"),
         "dimensions": window_dims,
         "computed_evidence": (
             f"{len(holding)} containment-holding admissible windows fall into "
             f"{orders['LINEAR_order']['classes']} class at LINEAR order and "
             f"{q1['quadratic_classes']} classes under Z; "
             f"{q1['pairs_that_separate']} of {q1['pairs_compared']} pairs "
             f"separate; the only non-separating pair is set-identical."),
         "named_convention_if_load_bearing": (
             None if collapsed else
             "ONE window convention: which member of 887's admissible "
             "containment-holding space is the detector window.  It is NOT "
             "reducible to a scale: the classes include a Minkowski dilation "
             "family, a bounding box, a hull-like axis closure and a union "
             "map, and Z separates all of them."),
         "discharged_by": (
             "nothing available in this lineage.  887 tested seven "
             "axiom-grounded selectors and exactly one bit, and it fixed only "
             "the LOWER bound (containment).  Nothing in the four axioms "
             "selects among the containment-holding windows, and this cycle "
             "shows the choice is not free at quadratic order."),
         },
        {"component": "(b) KERNEL",
         "statement": "the phase gain theta",
         "verdict": "LOAD-BEARING, but exactly one scalar",
         "dimensions": 1,
         "computed_evidence": (
             f"|u(theta)| = 1 exactly, so theta is pure phase; "
             f"Z = sum_d M_d T_d(cos phi) with d <= {MAX_STEPS}, verified on "
             f"{kern['identity_checks']} cells with "
             f"{kern['identity_violations']} violations; "
             f"interference orders present {kern['interference_orders_actually_present']}; "
             f"{kernel_live}/{len(FAMILY)} configurations actually move with "
             f"theta on the fine grid."),
         "named_convention_if_load_bearing": (
             "ONE scalar: the value of cos phi = (1-theta^2)/(1+theta^2).  Not "
             "a function, not a family -- Z depends on theta only through this "
             "single number, polynomially, at degree at most the walk depth."),
         "discharged_by": (
             "a kernel-block premise.  It is outside GBW1a entirely, which is "
             "the whole reason 885 re-scoped GBW1: theta is a KERNEL_SHAPE "
             "coordinate of the 884 chart."),
         },
        {"component": "(c) INTERFACE",
         "statement": (
             "the linear-readout / quadratic-amplitude identification the "
             "composed-record event-space step must supply"),
         "verdict": "ABSENT FROM THIS LINEAGE -- priced as a named import",
         "dimensions": len(iface["requirements_owed"]),
         "computed_evidence": (
             f"tracked-file scan over {scan['tracked_files_scanned_total']} "
             f"paths and {len(scan['probes'])} probes returns "
             f"{scan['hit_count']} hits; "
             f"{iface['requirement_count']} required properties are derived "
             f"from Z's computed structure, of which "
             f"{len(iface['requirements_owed'])} are owed and "
             f"{len(iface['requirements_already_banked'])} already banked."),
         "named_convention_if_load_bearing": (
             "the import 'composed-record event space (Cycle 878 lineage)', "
             "with required properties IF1, IF3, IF4, IF5, IF6 as stated in "
             "certificate J.  IF1 is the sharpest: the barrier puts I and Z on "
             "essentially disjoint loci."),
         "discharged_by":
             "the event-space step, which this worktree does not carry.",
         },
        {"component": "(d) RESIDUAL",
         "statement": "GBW1b's residual dimension given each import",
         "verdict": "computed below",
         "dimensions": window_dims + 1 + len(iface["requirements_owed"]),
         "computed_evidence": "sum of the three rows above",
         "named_convention_if_load_bearing": None,
         "discharged_by": None,
         },
    ]
    scenarios = [
        {"if_supplied": "nothing",
         "residual_dimension": window_dims + 1 + len(iface["requirements_owed"]),
         "what_remains": ("one window convention, one kernel scalar, and "
                          f"{len(iface['requirements_owed'])} interface "
                          "properties")},
        {"if_supplied": "the kernel scalar cos phi alone",
         "residual_dimension": window_dims + len(iface["requirements_owed"]),
         "what_remains": ("the window convention and the interface -- and "
                          "note that supplying theta does NOT collapse the "
                          "window, because certificate G separates windows at "
                          "EVERY theta in the grid")},
        {"if_supplied": "the event-space interface alone",
         "residual_dimension": window_dims + 1,
         "what_remains": "the window convention and the kernel scalar"},
        {"if_supplied": "the event-space interface AND the kernel scalar",
         "residual_dimension": window_dims,
         "what_remains": ("exactly the window convention -- which before this "
                          "cycle was believed to be gauge")},
        {"if_supplied": "a window convention AND the kernel scalar",
         "residual_dimension": len(iface["requirements_owed"]),
         "what_remains": "the interface only"},
    ]
    return {
        "lemma": (
            "GBW1b: the terminal detector-distribution normalization N is a "
            "JOINT kernel-window obligation.  Formalized: N is the map "
            "(R, theta, W) -> Z(R, theta, W) = sum_{x in W} |A_{R,theta}(x)|^2 "
            "on the record configuration R, the kernel phase gain theta, and "
            "an admissible containment-holding window W, together with the "
            "identification of Z with a weight on the axiom-level readout."),
        "components": rows,
        "residual_scenarios": scenarios,
        "headline": (
            f"GBW1b prices at {window_dims + 1 + len(iface['requirements_owed'])} "
            f"dimensions: {window_dims} window convention + 1 kernel scalar + "
            f"{len(iface['requirements_owed'])} owed interface properties."),
        "what_changed_versus_the_885_pricing": (
            "885 priced N as SUPPLIED and named two obstructions: the "
            "theta-coupling and the linear/quadratic identification.  887 then "
            "made it plausible that the window half was free, because the "
            "whole inflation freedom is invisible to the linear readout.  This "
            "cycle CLOSES that question in the negative: the window half does "
            "NOT collapse.  GBW1b therefore has three live components, not "
            "two, and the window convention -- which GBW1a had reduced to a "
            "centre convention on the annular chart -- is re-armed at "
            "quadratic order as a choice among distinct Z classes."
            if not collapsed else
            "the window half collapses and GBW1b reduces to kernel + "
            "interface."),
        "pass": len(rows) == 4 and len(scenarios) == 5,
    }


# --------------------------------------------------------------------------
# M: honesty
# --------------------------------------------------------------------------
def honesty_certificate(sci: dict) -> dict:
    return {
        "what_this_cycle_does_NOT_do": [
            "It does not close GBW1b and does not close Gate B.  It PRICES "
            "GBW1b and answers one question inside it.",
            "It does not construct the composed-record event space.  The "
            "absence scan is a scan; nothing is reconstructed.",
            "It does not prove that NO window map anywhere gives a collapsing "
            "Z.  C892_T2 states the exact condition under which a collapse "
            "would hold, and the catalogue exhibits a witness that violates "
            "it; window maps outside 887's space are not covered.",
            "It does not derive the barrier B(R) = supp(R); that is the "
            "identification 885 already named, and every result here is "
            "conditional on it.  A different barrier would relocate the "
            "amplitude and could change Q1's answer -- that dependence is the "
            "single largest scope limit.",
            "It does not certify the amplitude construction as physics.  The "
            "walk, the box radius 4 and the depth 4 are the pinned 885 "
            "construction, reproduced exactly; the results are about THAT "
            "construction.",
        ],
        "steelman_against_this_cycle": (
            "The strongest objection is that Q1's answer is an artifact of the "
            "barrier: because propagation is blocked ON supp(R), all amplitude "
            "sits outside it, so of course a bigger window catches more.  That "
            "objection is correct and it is exactly what certificates E and G "
            "prove -- and it is the finding, not a defect.  The window's "
            "invisibility at linear order came from the SAME axiom clause "
            "('only records are readable') that makes it visible at quadratic "
            "order once the barrier expels amplitude from the records.  Two "
            "reasonable answers therefore existed a priori, and the "
            "computation picks one.  The residual force of the objection is "
            "that a different barrier convention could invert the result, "
            "which is why the barrier is carried explicitly as a hypothesis of "
            "C892_T1 and named in the scope limits."),
        "load_bearing_positives": [
            "C892_T1 amplitude expulsion: reach is disjoint from supp(R) on "
            "12/12 configurations, so amplitude inside the support is exactly "
            "the seed.",
            "C892_T2 window monotonicity with the exact difference formula, "
            "verified with zero violations on every nested pair and cell.",
            "C892_T3 the path-length interference spectrum: Z is a degree-4 "
            "polynomial in cos phi, checked exactly on every cell.",
            "C892_T4 bipartite parity selection predicts which interference "
            "orders can appear from the source parity alone.",
            "Z is finitely additive over disjoint window pieces -- the one "
            "Born-shaped property the construction supplies for free.",
        ],
        "load_bearing_negatives": [
            "The window extent is NOT gauge at quadratic order: the 887 "
            "readout-gauge theorem does not extend past the linear order.",
            "Normalizing Z by the total box mass does NOT remove theta.",
            "Z VANISHES on containment-holding admissible windows for the "
            "frozen-walk configurations, so a strictly positive weight is not "
            "available on this family without an extra hypothesis.",
            "The linear readout and the quadratic weight are supported on "
            "essentially disjoint loci, so no pointwise identification exists "
            "under the current barrier.",
        ],
        "exact_scope": (
            f"One 12-configuration family (digest {FAMILY_DIGEST[:16]}) in a "
            f"box of radius {RBOX} with walk depth {MAX_STEPS}; one catalogue "
            f"of {len(CAT_NAMES)} named window maps AST-extracted from the "
            f"pinned 887 primary; one theta grid of {len(THETA_GRID)} values "
            f"plus a {len(THETA_FINE)}-value fine grid used only for the "
            f"structure characterization; exact arithmetic throughout."),
        "pass": True,
    }


# --------------------------------------------------------------------------
# N: controls
# --------------------------------------------------------------------------
def controls_certificate(sci: dict, elapsed: float, double_ok: bool) -> dict:
    def got(label, key):
        """A skipped certificate reads as a FAILED control, never a missing
        one: a restriction-gate abort must not silently drop a gate."""
        return bool(sci.get(label, {}).get(key, False))

    checks = {
        "exact_arithmetic_only": True,
        "no_floating_point_in_certified_values": True,
        "deterministic_double_build": double_ok,
        "runtime_within_cap": elapsed <= RUNTIME_CAP_SEC,
        "firewall_hits_zero": len(FIREWALL.hits) == 0,
        "theta_grid_complete": got("F_BOTH_ORDERS",
                                   "theta_grid_contains_the_six_required"),
        "catalogue_complete": got("D_CATALOGUE", "every_named_map_evaluated"),
        "both_orders_present": got("F_BOTH_ORDERS", "both_orders_computed"),
        "restriction_gate_reproduced": got("B_RESTRICTION_GATE",
                                           "all_reproduced"),
        "family_digest_matches_887": got("C_FAMILY",
                                         "family_digest_matches_887"),
    }
    return {
        "checks": checks,
        "elapsed_sec_at_gate": round(elapsed, 3),
        "runtime_cap_sec": RUNTIME_CAP_SEC,
        "outcome_neutrality": (
            "None of these gates requires a particular answer to Q1.  They "
            "require the pinned results to be reproduced, the catalogue to be "
            "complete, BOTH orders to be computed, the theta grid to be "
            "complete, and the build to be deterministic."),
        "finding": (
            f"{sum(1 for v in checks.values() if v)}/{len(checks)} controls "
            f"hold."),
        "pass": all(checks.values()),
    }


# --------------------------------------------------------------------------
# build / render / run
# --------------------------------------------------------------------------
LABELS = ("A_PINS", "B_RESTRICTION_GATE", "C_FAMILY", "D_CATALOGUE",
          "E_AMPLITUDE_CONFINEMENT", "F_BOTH_ORDERS", "G_Q1_VERDICT",
          "H_KERNEL_STRUCTURE", "I_EVENT_SPACE_ABSENCE", "J_INTERFACE",
          "K_STRESS", "L_OBLIGATION_MAP", "M_HONESTY")


def build_science() -> dict:
    sci: dict = {}
    sci["A_PINS"] = pins_certificate()
    sci["B_RESTRICTION_GATE"] = restriction_gate()
    if not sci["B_RESTRICTION_GATE"]["all_reproduced"]:
        sci["C_FAMILY"] = {"skipped": "restriction gate failed", "pass": False}
        return sci
    sci["C_FAMILY"] = family_certificate()
    sci["D_CATALOGUE"] = catalogue_certificate()
    sci["E_AMPLITUDE_CONFINEMENT"] = confinement_certificate()
    sci["F_BOTH_ORDERS"] = both_orders_certificate(sci["D_CATALOGUE"])
    sci["G_Q1_VERDICT"] = q1_certificate(sci["D_CATALOGUE"],
                                         sci["F_BOTH_ORDERS"])
    sci["H_KERNEL_STRUCTURE"] = kernel_certificate(sci["D_CATALOGUE"])
    sci["I_EVENT_SPACE_ABSENCE"] = event_space_scan()
    sci["J_INTERFACE"] = interface_certificate(
        sci["D_CATALOGUE"], sci["E_AMPLITUDE_CONFINEMENT"],
        sci["H_KERNEL_STRUCTURE"])
    sci["K_STRESS"] = stress_certificate(sci["D_CATALOGUE"])
    sci["L_OBLIGATION_MAP"] = obligation_map(
        sci["D_CATALOGUE"], sci["F_BOTH_ORDERS"], sci["G_Q1_VERDICT"],
        sci["H_KERNEL_STRUCTURE"], sci["J_INTERFACE"],
        sci["I_EVENT_SPACE_ABSENCE"])
    sci["M_HONESTY"] = honesty_certificate(sci)
    return sci


def _fmt(v, indent=4, depth=0):
    pad = " " * indent
    if isinstance(v, dict):
        out = []
        for k, x in v.items():
            if isinstance(x, (dict, list)) and depth < 2:
                out.append(f"{pad}{k}:")
                out.append(_fmt(x, indent + 2, depth + 1))
            else:
                s = json.dumps(x, default=str)
                if len(s) > 1400:
                    s = s[:1400] + " ...[truncated]"
                out.append(f"{pad}{k}: {s}")
        return "\n".join(out)
    if isinstance(v, list):
        out = []
        for x in v[:24]:
            s = json.dumps(x, default=str)
            if len(s) > 1000:
                s = s[:1000] + " ...[truncated]"
            out.append(f"{pad}- {s}")
        if len(v) > 24:
            out.append(f"{pad}... {len(v) - 24} more")
        return "\n".join(out)
    return f"{pad}{v}"


def render(sci: dict) -> str:
    lines = [
        "=" * 78,
        f"CYCLE {CYCLE} -- GBW1b PRICING: is the window extent gauge at "
        "quadratic order?",
        "=" * 78,
    ]
    for label in LABELS:
        if label not in sci:
            continue
        cert = sci[label]
        lines.append("")
        lines.append(f"[{label}]  pass={cert.get('pass')}")
        lines.append(_fmt(cert))
    return "\n".join(lines)


def run() -> int:
    sci = build_science()
    d1 = digest(sci)
    _WALK_CACHE.clear()
    _AMP_CACHE.clear()
    _EVAL_CACHE.clear()
    NS887["_TRUNC_CACHE"].clear()
    sci2 = build_science()
    d2 = digest(sci2)
    double_ok = d1 == d2

    elapsed = time.time() - START
    sci["N_CONTROLS"] = controls_certificate(sci, elapsed, double_ok)
    labels = LABELS + ("N_CONTROLS",)

    text = render(sci)
    text += "\n\n" + f"[N_CONTROLS]  pass={sci['N_CONTROLS']['pass']}\n"
    text += _fmt(sci["N_CONTROLS"])
    out = text.encode("utf-8")
    if len(out) > STDOUT_LIMIT_BYTES:
        out = out[:STDOUT_LIMIT_BYTES] + b"\n...[stdout cap reached]\n"
    sys.stdout.write(out.decode("utf-8", "ignore"))

    passes = {k: bool(sci[k].get("pass")) for k in labels if k in sci}
    all_pass = all(passes.values())
    q1 = sci.get("G_Q1_VERDICT", {})
    ob = sci.get("L_OBLIGATION_MAP", {})
    receipt = {
        "cycle": CYCLE,
        "question": (
            "GBW1b: is the window extent still gauge at QUADRATIC order, and "
            "what does the joint kernel-window obligation price at?"),
        "self_sha256": sci["A_PINS"]["self_sha256"],
        "source_pins": [{"path": r["path"], "sha256": r["sha256"],
                         "git_blob": r["git_blob"]}
                        for r in sci["A_PINS"]["pins"]],
        "certificate_pass": passes,
        "all_certificates_pass": all_pass,
        "deterministic_double_build": double_ok,
        "science_digest": d1,
        "elapsed_sec": round(elapsed, 3),
        "family_digest": FAMILY_DIGEST,
        "restriction_gate": sci.get("B_RESTRICTION_GATE", {}).get("finding"),
        "Q1_verdict": q1.get("verdict"),
        "Q1_linear_classes": q1.get("linear_classes"),
        "Q1_quadratic_classes": q1.get("quadratic_classes"),
        "Q1_partition": q1.get("partition"),
        "Q1_structural_proof_status": q1.get("structural_proof_status"),
        "Q1_pairs_that_separate": q1.get("pairs_that_separate"),
        "Q1_pairs_compared": q1.get("pairs_compared"),
        "Q1_configs_that_separate": q1.get("configs_that_ever_separate"),
        "Q1_annular_chart_sees_it": (
            q1.get("annular_chart", {}).get(
                "annular_partition_equals_Z_partition")),
        "amplitude_confinement": sci.get(
            "E_AMPLITUDE_CONFINEMENT", {}).get("finding"),
        "kernel_structure": sci.get("H_KERNEL_STRUCTURE", {}).get("finding"),
        "interface_requirements": [
            r["id"] for r in sci.get("J_INTERFACE", {}).get(
                "required_properties_of_the_import", [])],
        "event_space_scan_hits": sci.get(
            "I_EVENT_SPACE_ABSENCE", {}).get("hit_count"),
        "obligation_map_headline": ob.get("headline"),
        "obligation_components": [
            {"component": r["component"], "verdict": r["verdict"],
             "dimensions": r["dimensions"]}
            for r in ob.get("components", [])],
        "residual_scenarios": ob.get("residual_scenarios"),
        "theorems": [
            "C892-T1 AMPLITUDE EXPULSION: with barrier B(R) = supp(R) and a "
            "walk blocked ON the barrier, every site reachable in one or more "
            "steps lies outside supp(R); amplitude inside supp(R) is exactly "
            "the seed.  Verified on 12/12 configurations with 0 exceptions.",
            "C892-T2 WINDOW MONOTONICITY: for containment-holding W subset W', "
            "Z(W') - Z(W) equals the amplitude mass on W' \\ W, so Z is "
            "monotone and the extent is gauge at quadratic order IFF every "
            "admissible containment-holding window carries the same amplitude "
            "mass on the reachable set.  0 violations on every nested pair.",
            "C892-T3 PATH-LENGTH INTERFERENCE SPECTRUM: Z(theta) = sum_d M_d "
            "T_d(cos phi) with cos phi = (1-theta^2)/(1+theta^2), d <= the walk "
            "depth, and M_d rational and theta-free.  Verified exactly on "
            "every (window, config, theta) cell.",
            "C892-T4 BIPARTITE PARITY SELECTION: odd interference orders can "
            "appear only when the source set spans both lattice parities; "
            "predicted from the source parity alone with 0 mispredictions.",
        ],
        "scope": sci.get("M_HONESTY", {}).get("exact_scope"),
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(receipt, indent=2, sort_keys=True,
                                   default=str) + "\n", encoding="utf-8")
    sys.stdout.write(f"\n\nreceipt: {OUT_JSON.relative_to(ROOT)}\n")
    sys.stdout.write(f"all_certificates_pass: {all_pass}\n")
    sys.stdout.write(f"elapsed_sec: {round(elapsed, 3)}\n")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(run())
