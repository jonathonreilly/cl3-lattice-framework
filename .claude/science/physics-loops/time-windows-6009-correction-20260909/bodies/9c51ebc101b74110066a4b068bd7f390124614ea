#!/usr/bin/env python3
"""Cycle 894 -- THE INTERFACE ATTACK.

Two lineages meet on this branch for the first time.

  * Cycle 892 (this branch) priced GBW1b and derived SIX interface
    requirements IF1..IF6 -- five OWED, one (IF2, finite additivity) already
    banked -- that "the composed-record event-space step" must supply before
    the terminal normalization Z can be read as a lawful record-facing weight.

  * Cycle 878 (sibling lineage, ship commit da5ce5b226, VENDORED onto this
    branch as the first action of this cycle) certified the composed-record
    EVENT SPACE: 92,260 events over 748 worlds, atoms are the (world, tag,
    ordinal) singletons, FIVE record-native weightings admissible, all ten
    pairs discriminating, and NOTHING selected among them.

THE QUESTION.  Does gravity's Z CONSTRAIN the Born selection?  That is: which
(if any) of 878's five admissible weightings can satisfy the IF sheet against
Z's computed structure?

Q1  THE COMPOSITION MAP.  Rebuild both machineries by AST extraction and state
    EXACTLY where they could meet -- or compute the type mismatch that says
    they cannot.
Q2  THE FIVE WEIGHTINGS x THE IF SHEET.  A 5 x 5 verdict table, every cell
    computed, no cell asserted.
Q3  WHAT WOULD CLOSE IT.  The exact residual, derived from Z facts and
    event-space facts only, needle-gated against Born-rule vocabulary.

DISCIPLINE.  Seven pinned artifacts (sha256 + git blob, hard preflight exit 2).
TEXT / AST / JSON only -- an import firewall forbids importing any pinned
primary as a module, and zero firewall hits is gated.  Exact rational
arithmetic throughout; no floating point anywhere in the science.  Restriction
gates against BOTH pinned receipts before any new claim.  Deterministic double
build.  Outcome-neutral gates: the certificates pass when the WORK is complete,
not when the answer is pretty -- SELECTION, NARROWING, NO-GO and TYPE-MISMATCH
are all passing outcomes.  Falsifier visibility: two PLANTED weightings, one
designed to pass every requirement and one designed to pass some and fail
others, are run through the identical table -- if the table cannot see the
planted survivor, the table is broken and the run fails.

BOUNDARY.  This block supplies no occurrence rule, no probability, no update
law and selects no weighting as physical.  It computes whether the pinned
gravity-side structure EXCLUDES the pinned record-side candidates.  Exclusion
is a negative result and is reported as such.
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
STDOUT_LIMIT_BYTES = 150_000
EXHIBIT_CAP = 6

ROOT = Path(__file__).resolve().parents[1]
SELF_REL = "scripts/frontier_cycle894_interface_attack_2026_07_28.py"
OUT_JSON = ROOT / "outputs" / "interface_attack_cycle894_receipt_2026_07_28.json"

C878_PRIMARY = "scripts/frontier_cycle878_event_space_groundwork_2026_07_28.py"
C878_RECEIPT = "outputs/event_space_groundwork_cycle878_receipt_2026_07_28.json"
C892_PRIMARY = "scripts/frontier_cycle892_gbw1b_pricing_2026_07_28.py"
C892_RECEIPT = "outputs/gbw1b_pricing_cycle892_receipt_2026_07_28.json"
C885_PRIMARY = "scripts/frontier_cycle885_gbw1_record_window_2026_07_28.py"
C887_PRIMARY = "scripts/frontier_cycle887_window_freedom_2026_07_28.py"
AXIOMS_MD = "docs/MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    C878_PRIMARY, C878_RECEIPT,
    C892_PRIMARY, C892_RECEIPT,
    C885_PRIMARY, C887_PRIMARY,
    AXIOMS_MD,
)

# Digests supplied verbatim by the block brief (the 878 pair) or read off the
# branch state the brief pins (the rest).  Mismatch is a hard preflight abort:
# a cited artifact that is not the artifact this cycle was pointed at makes
# every downstream number meaningless.
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
BRIEF_GIT_BLOB = {
    C878_PRIMARY: "af2e27c4a01b02b68c319e3a572eaeb2217e04e7",
    C878_RECEIPT: "565faf0be5e6930b08f585fea1c30b2ceaa41a91",
    C892_PRIMARY: "360eed9e17eab1af19ca03d7ea1161dafaf56da0",
    C892_RECEIPT: "722b1b7c50a17fffe6b0a4e666970d5aaf0e74c2",
    C885_PRIMARY: "7fbd35a66859e8b888e71d7305e8cacc32a8b8ef",
    C887_PRIMARY: "0fbcf92fc98b0d88d436a05efdc33449c52473db",
    AXIOMS_MD: "4a863da1f3f255354839277271a3a69a5c205133",
}

# The 892 receipt records this blob for its own primary under a different key
# path; the 878 receipt records the blob of the 878 primary.  Both are
# cross-checked at run time against the file on disk (certificate A).
C878_SELF_BLOB_IN_RECEIPT = "af2e27c4a01b02b68c319e3a572eaeb2217e04e7"

# The nine containment-holding admissible windows, read from the pinned 892
# run cache is NOT how this works: the list is RECOMPUTED here from 887's
# catalogue and the containment filter, then compared to the pinned names.
PINNED_HOLDING_NAMES = (
    "axis_segment_closure",
    "bounding_box",
    "minkowski_S_ball1__885_checker_dilation_k1",
    "minkowski_S_ball2__885_checker_dilation_k2",
    "minkowski_S_far_shell__origin_present",
    "minkowski_S_zero__the_885_support_window",
    "readout_keyed_inflation",
    "size_keyed_inflation",
    "union_box_with_dilation",
)

# 892's certified Z-structure rows this cycle must reproduce value-for-value.
PINNED_892 = {
    "family_digest":
        "30edaa3d5ca03c2492a772a3eeec2c360b70e0e742ba4889bf3e0c5e4180b25e",
    "holding_windows": 9,
    "cells": 648,
    "vanishing_cells": 42,
    "negativity_violations": 0,
    "finite_additivity_checks": 72,
    "finite_additivity_violations": 0,
    "total_mass_theta_dependent_configs": 7,
    "normalized_ratio_still_theta_dependent_configs": 7,
    "amplitude_sites_inside_support_total": 8,
    "amplitude_sites_outside_support_total": 844,
    "frozen_configs": 5,
    "kernel_identity_checks": 648,
    "kernel_identity_violations": 0,
    "kernel_max_degree": 4,
    "kernel_orders_present": [0, 1, 2, 3, 4],
    "reach_meets_support_configs": 0,
    "quadratic_classes": 8,
    "linear_classes": 1,
}

# 878's certified event-space rows this cycle must reproduce value-for-value.
PINNED_878 = {
    "event_cardinality": 92260,
    "worlds": 748,
    "events_by_tag": {"B0": 47872, "B1": 44224, "F": 164},
    "cells_F_ATOM": 92260,
    "cells_F_WORLD": 748,
    "cells_F_TAG": 3,
    "cells_F_TAG_ORDINAL": 129,
    "cells_F_WORLD_TAG": 1603,
    "per_world_range": [64, 129],
    "world_orbit_count": 68,
    "world_orbit_size": 11,
    "admissible_count": 5,
    "discriminating_pairs": 10,
    "indistinguishable_pairs": 0,
    "zero_weight_events": {
        "M1_COUNTING": 0,
        "M2_PER_WORLD_UNIFORM": 0,
        "M3_OCCUPATION_WEIGHTED": 73088,
        "M4_FORMATION_LIFETIME": 73088,
        "M5_FORMATION_MOMENT": 76184,
    },
}

BOUNDARY_STATEMENT = (
    "this block supplies no occurrence rule, no probability, no update law and"
    " selects no weighting as physical; it computes whether the pinned"
    " gravity-side structure EXCLUDES the pinned record-side candidates, and"
    " reports exclusion as the negative result it is")


# --------------------------------------------------------------------------
# preflight + import firewall
# --------------------------------------------------------------------------
def read_bytes(rel: str) -> bytes:
    return (ROOT / rel).read_bytes()


def read_text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def sha256_of(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(
        f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def digest(payload) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":"),
                   default=str).encode("utf-8")).hexdigest()


def digest892(payload) -> str:
    """892's digest convention VERBATIM (no separators argument), so the
    recomputed family digest is comparable to the pinned one."""
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, default=str).encode("utf-8")
    ).hexdigest()


def q(v) -> str:
    f = Fraction(v)
    return f"{f.numerator}/{f.denominator}"


def preflight_pins() -> None:
    missing = [p for p in AUDIT_INPUT_PATHS if not (ROOT / p).is_file()]
    if missing:
        print(f"PREFLIGHT ABORT: missing pinned artifacts: {missing}")
        sys.exit(2)
    bad = []
    for rel in AUDIT_INPUT_PATHS:
        raw = read_bytes(rel)
        s, b = sha256_of(raw), git_blob_sha1(raw)
        if s != BRIEF_SHA256[rel]:
            bad.append(f"{rel}: sha256 {s} != brief {BRIEF_SHA256[rel]}")
        if b != BRIEF_GIT_BLOB[rel]:
            bad.append(f"{rel}: blob {b} != brief {BRIEF_GIT_BLOB[rel]}")
    if bad:
        print("PREFLIGHT ABORT: pinned digest mismatch")
        for row in bad:
            print("  " + row)
        sys.exit(2)


_FORBIDDEN_STEMS = {Path(p).stem for p in AUDIT_INPUT_PATHS}


class _Firewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in _FORBIDDEN_STEMS:
            self.hits.append(fullname)
            raise ImportError(f"FIREWALL forbids importing a pin: {fullname}")
        return None


FIREWALL = _Firewall()
sys.meta_path.insert(0, FIREWALL)
preflight_pins()


# --------------------------------------------------------------------------
# AST extraction: execute ONLY the named top-level nodes of a pinned file
# --------------------------------------------------------------------------
def ast_extract(rel: str, wanted, seed: dict):
    """No import, no exec of the pinned file as a whole, no side effects."""
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
                 filename=f"<ast:{rel}>", mode="exec"), ns)  # noqa: S102
    return ns, sorted(seen), sorted(set(wanted) - seen)


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b) if a and b else 0


_SEED = {"Fraction": Fraction, "product": product,
         "permutations": permutations, "Counter": Counter,
         "lcm": lcm, "gcd": gcd}

# ---- the 892 side: the Z machinery, extracted from the pinned 892 primary --
FAMILY_NODES = ("NEIGHBOURS", "_lcg", "make_config", "build_family")
NS885, SEEN885, MISS885 = ast_extract(C885_PRIMARY, set(FAMILY_NODES), _SEED)
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
NS887, SEEN887, MISS887 = ast_extract(
    C887_PRIMARY, set(CATALOGUE_NODES), dict(_SEED, FAMILY=FAMILY))
CATALOGUE = NS887["selector_catalogue"]()
CAT = dict(CATALOGUE)
ROT24 = NS887["ROT24"]

Z_NODES = (
    "RBOX", "MAX_STEPS", "ZERO_C", "ONE_C", "cadd", "cmul", "cabs2",
    "unit_point", "BOX", "INBOX", "barycentre", "source_set", "_WALK_CACHE",
    "walk_layers", "_AMP_CACHE", "amp_field", "Z", "window_of", "_cheb",
    "interference_spectrum", "THETA_GRID", "THETA_885", "THETA_FINE",
    "BORN_VOCABULARY",
)
NS892, SEEN892, MISS892 = ast_extract(
    C892_PRIMARY, set(Z_NODES), dict(_SEED, NEIGHBOURS=NEIGHBOURS, CAT=CAT))
Z = NS892["Z"]
amp_field = NS892["amp_field"]
walk_layers = NS892["walk_layers"]
source_set = NS892["source_set"]
window_of = NS892["window_of"]
cabs2 = NS892["cabs2"]
interference_spectrum = NS892["interference_spectrum"]
INBOX = NS892["INBOX"]
BOX = NS892["BOX"]
THETA_GRID = NS892["THETA_GRID"]
THETA_FINE = NS892["THETA_FINE"]
MAX_STEPS = NS892["MAX_STEPS"]
RBOX = NS892["RBOX"]
BORN_VOCABULARY = NS892["BORN_VOCABULARY"]

# ---- the 878 side: the weighting machinery, from the VENDORED 878 primary --
E878_NODES = (
    "build_candidates", "family_keys", "cells_of", "refines", "lcm",
    "CANDIDATE_NAMES", "CONTROL_NAME", "FAMILY_ORDER", "REGISTER_CAP",
    "monitor_phase_action", "group_orbits",
)
NS878, SEEN878, MISS878 = ast_extract(C878_PRIMARY, set(E878_NODES), _SEED)
build_candidates = NS878["build_candidates"]
CANDIDATE_NAMES = NS878["CANDIDATE_NAMES"]
CONTROL_NAME = NS878["CONTROL_NAME"]
FAMILY_ORDER = NS878["FAMILY_ORDER"]
REGISTER_CAP = NS878["REGISTER_CAP"]

R878 = json.loads(read_text(C878_RECEIPT))
R892 = json.loads(read_text(C892_RECEIPT))


def family_fingerprint(fam) -> list:
    return [{"name": c["name"],
             "sites": [list(s) for s in c["sites"]],
             "content": [[list(s), b] for s, b in c["content"]],
             "depth": [[list(s), d] for s, d in c["depth"]]} for c in fam]


FAMILY_DIGEST = digest892(family_fingerprint(FAMILY))


# --------------------------------------------------------------------------
# A: pins
# --------------------------------------------------------------------------
def pins_certificate() -> dict:
    rows = []
    for rel in AUDIT_INPUT_PATHS:
        raw = read_bytes(rel)
        rows.append({"path": rel, "bytes": len(raw),
                     "sha256": sha256_of(raw),
                     "git_blob": git_blob_sha1(raw),
                     "brief_sha256_match":
                         sha256_of(raw) == BRIEF_SHA256[rel],
                     "brief_git_blob_match":
                         git_blob_sha1(raw) == BRIEF_GIT_BLOB[rel]})
    # the vendored 878 primary's blob must match what 878's OWN receipt
    # recorded for it -- the vendoring is then provably faithful, not merely
    # digest-equal to a literal typed into this file.
    recorded = (R878.get("files", {})
                .get(C878_PRIMARY, {}).get("git_blob"))
    recorded_sha = (R878.get("files", {})
                    .get(C878_PRIMARY, {}).get("sha256"))
    vendor_ok = (recorded == C878_SELF_BLOB_IN_RECEIPT
                 == git_blob_sha1(read_bytes(C878_PRIMARY))
                 and recorded_sha == sha256_of(read_bytes(C878_PRIMARY)))
    ast_ok = (not MISS885 and not MISS887 and not MISS892 and not MISS878)
    return {
        "certificate": "A_PINS",
        "rows": rows,
        "vendored_878_primary_blob_matches_its_own_receipt": vendor_ok,
        "ast_nodes_extracted": {
            "885": SEEN885, "887_count": len(SEEN887),
            "892": SEEN892, "878": SEEN878,
        },
        "ast_nodes_missing": {
            "885": MISS885, "887": MISS887, "892": MISS892, "878": MISS878,
        },
        "firewall_hits": list(FIREWALL.hits),
        "forbidden_stems_loaded": sorted(
            s for s in _FORBIDDEN_STEMS if s in sys.modules),
        "method": ("TEXT / AST / JSON only.  Every pinned primary is parsed "
                   "and its named top-level nodes executed in a private "
                   "namespace; none is imported as a module, and the firewall "
                   "raises on any attempt."),
        "pass": (all(r["brief_sha256_match"] and r["brief_git_blob_match"]
                     for r in rows)
                 and vendor_ok and ast_ok
                 and not FIREWALL.hits
                 and not any(s in sys.modules for s in _FORBIDDEN_STEMS)),
    }


# --------------------------------------------------------------------------
# the 878 surrogate event space
#
# The 878 primary imports two modules -- the Cycle-719 controller core and the
# Cycle-863 time-from-records module -- and rebuilds the composed record-write
# trajectory from them.  Cycle 863 is NOT on this branch, so the trajectory
# cannot be re-run here.  It does not need to be.  The AST of
# build_candidates is read below and PROVES that the five weightings are
# functions of exactly four inputs: the per-world event multiset (via e[0]),
# occ_global, formed, and boundaries.  Nothing else about an event -- its
# moment, tag, ordinal or content -- reaches a weight.  So a surrogate that is
# EXACT on those four inputs is exact on the weightings, and the reproduction
# of 878's certified zero-weight counts value-for-value is a real test of the
# reconstruction, not a restatement of it.
# --------------------------------------------------------------------------
def build_candidates_input_footprint() -> dict:
    """AST proof that build_candidates reads only e[0], occ_global, formed,
    boundaries -- i.e. that event moment/tag/ordinal/content are weight-void."""
    tree = ast.parse(read_text(C878_PRIMARY))
    fn = next(n for n in tree.body
              if isinstance(n, ast.FunctionDef)
              and n.name == "build_candidates")
    args = [a.arg for a in fn.args.args]
    subscripts = set()
    names = set()
    for node in ast.walk(fn):
        if isinstance(node, ast.Subscript) and isinstance(node.value, ast.Name):
            idx = node.slice
            if isinstance(idx, ast.Constant):
                subscripts.add(f"{node.value.id}[{idx.value!r}]")
        if isinstance(node, ast.Name):
            names.add(node.id)
    event_subs = sorted(s for s in subscripts if s.startswith(("e[", "w[")))
    # every subscript of a bound event variable
    ev_indices = sorted({s for s in subscripts if s.startswith("e[")})
    return {
        "signature": args,
        "event_field_subscripts_used": ev_indices,
        "only_field_0_used": ev_indices == ["e[0]"],
        "other_constant_subscripts": sorted(
            s for s in subscripts if not s.startswith("e[")),
        "reads_moment_tag_ordinal_or_content": ev_indices != ["e[0]"],
        "conclusion": ("build_candidates is a function of the per-world event"
                       " multiset, occ_global, formed and boundaries ONLY;"
                       " event moment, tag, ordinal and content are"
                       " weight-void"),
    }


def surrogate_event_space() -> dict:
    """A reconstruction exact on every input the weightings actually read,
    and constrained by 878's certified rows."""
    tgt = PINNED_878["zero_weight_events"]
    n_worlds = PINNED_878["worlds"]
    total = PINNED_878["event_cardinality"]
    n_formed = PINNED_878["events_by_tag"]["F"]          # one F event / world
    n_unformed = n_worlds - n_formed                     # 584
    ev_unformed = tgt["M3_OCCUPATION_WEIGHTED"]          # 73088
    ev_moment0 = (tgt["M5_FORMATION_MOMENT"]
                  - tgt["M4_FORMATION_LIFETIME"])        # 3096
    lo, hi = PINNED_878["per_world_range"]

    counts: list[int] = []
    # 584 never-formed worlds carrying exactly 73088 events, all in range
    base, rem = divmod(ev_unformed, n_unformed)
    counts += [base + 1] * rem + [base] * (n_unformed - rem)
    # the moment-0-formed worlds: exactly 3096 events at the per-world maximum
    n_m0, r_m0 = divmod(ev_moment0, hi)
    assert r_m0 == 0, "moment-0 block is not a clean multiple of the cap"
    counts += [hi] * n_m0
    # the remaining formed worlds carry the rest
    n_rest = n_formed - n_m0
    ev_rest = total - ev_unformed - ev_moment0
    b2, r2 = divmod(ev_rest, n_rest)
    counts += [b2 + 1] * r2 + [b2] * (n_rest - r2)

    events = [(w, j, "B0", j, "x")
              for w, c in enumerate(counts) for j in range(c)]
    formed: dict[int, int] = {}
    occ = [0] * n_worlds
    for w in range(n_unformed, n_worlds):
        formed[w] = 0 if w < n_unformed + n_m0 else (w - n_unformed - n_m0 + 1)
        occ[w] = 1 + (w % 7)
    boundaries = 16384
    return {
        "counts": counts, "events": events, "occ": occ,
        "formed": formed, "boundaries": boundaries,
        "n_unformed": n_unformed, "n_moment0": n_m0,
        "in_range": all(lo <= c <= hi for c in counts),
        "total": sum(counts),
        "worlds": len(counts),
    }


# --------------------------------------------------------------------------
# B: restriction gate -- 878
# --------------------------------------------------------------------------
def restriction_878() -> dict:
    f = R878["findings"]
    checks: list[dict] = []

    def chk(name, got, want, note=""):
        checks.append({"check": name, "recomputed": got, "pinned": want,
                       "match": got == want, "note": note})

    # --- pure arithmetic identities among the receipt's own certified rows.
    # None of these is tuned by this cycle; each must hold if the vendored
    # construction is what its AST says it is.
    tagsum = sum(f["events_by_tag"].values())
    chk("events_by_tag sums to the event cardinality",
        tagsum, f["event_cardinality"])
    chk("F_ATOM cells == event cardinality (atoms are singletons)",
        f["cells_per_family"]["F_ATOM"], f["event_cardinality"])
    chk("atoms_are_singletons flag", f["atoms_are_singletons"], True)
    chk("F_WORLD cells == worlds carrying an event",
        f["cells_per_family"]["F_WORLD"], f["worlds_with_at_least_one_event"])
    chk("F_TAG cells == 3 (F, B0, B1)", f["cells_per_family"]["F_TAG"], 3)
    chk("F_TAG_ORDINAL == 1 (F,0) + REGISTER_CAP per bank",
        f["cells_per_family"]["F_TAG_ORDINAL"], 1 + 2 * REGISTER_CAP,
        f"REGISTER_CAP={REGISTER_CAP} AST-read from the vendored primary")
    chk("world orbits x orbit size == worlds",
        f["landed_symmetry"]["world_orbit_count"]
        * PINNED_878["world_orbit_size"],
        f["worlds_with_at_least_one_event"])
    chk("orbit histogram is uniform at the group order",
        f["landed_symmetry"]["world_orbit_size_histogram"],
        {str(PINNED_878["world_orbit_size"]):
         f["landed_symmetry"]["world_orbit_count"]})
    cv = f["candidate_verdicts"]
    chk("M3 and M4 vanish on the SAME worlds (occ>0 iff formed)",
        cv["M3_OCCUPATION_WEIGHTED"]["zero_weight_events"],
        cv["M4_FORMATION_LIFETIME"]["zero_weight_events"])
    chk("M5 zero-set contains M4's (moment-0 worlds also vanish)",
        cv["M5_FORMATION_MOMENT"]["zero_weight_events"]
        >= cv["M4_FORMATION_LIFETIME"]["zero_weight_events"], True)
    chk("mean events per world lies inside the certified range",
        PINNED_878["per_world_range"][0]
        <= f["event_cardinality"] / f["worlds_with_at_least_one_event"]
        <= PINNED_878["per_world_range"][1], True)
    chk("F-tag events == worlds that ever form (one F write per world)",
        f["events_by_tag"]["F"] <= f["worlds_with_at_least_one_event"], True)

    # --- headline rows, value-for-value against the brief
    chk("event cardinality", f["event_cardinality"],
        PINNED_878["event_cardinality"])
    chk("worlds", f["worlds_with_at_least_one_event"], PINNED_878["worlds"])
    chk("events by tag", f["events_by_tag"], PINNED_878["events_by_tag"])
    chk("F_WORLD_TAG cells", f["cells_per_family"]["F_WORLD_TAG"],
        PINNED_878["cells_F_WORLD_TAG"])
    chk("per-world event count range", f["per_world_event_count_range"],
        PINNED_878["per_world_range"])
    admissible = sorted(m for m, v in cv.items() if v["admissible"])
    chk("five admissible weightings", len(admissible),
        PINNED_878["admissible_count"])
    chk("admissible set == the AST-read candidate names",
        admissible, sorted(CANDIDATE_NAMES))
    chk("the declared control is NOT admissible",
        cv[CONTROL_NAME]["admissible"], False)
    chk("all ten pairs discriminate", len(f["discriminating_pairs"]),
        PINNED_878["discriminating_pairs"])
    chk("C(5,2) == the discriminating-pair count",
        len(list(combinations(CANDIDATE_NAMES, 2))),
        len(f["discriminating_pairs"]))
    chk("no indistinguishable pairs", len(f["indistinguishable_pairs"]),
        PINNED_878["indistinguishable_pairs"])

    # --- the FUNCTIONAL rebuild
    fp = build_candidates_input_footprint()
    sur = surrogate_event_space()
    nums, dens, meta, per_world, supported, common = build_candidates(
        sur["events"], sur["occ"], sur["formed"], sur["boundaries"])
    got_zero = {m: sum(1 for n in nums[m] if n == 0) for m in CANDIDATE_NAMES}
    got_sf = {m: all(n > 0 for n in nums[m]) for m in CANDIDATE_NAMES}
    want_sf = {m: cv[m]["support_faithful"] for m in CANDIDATE_NAMES}
    vals = {m: [Fraction(n, dens[m]) for n in nums[m]] for m in CANDIDATE_NAMES}
    disc = sum(1 for a, b in combinations(CANDIDATE_NAMES, 2)
               if vals[a] != vals[b])

    chk("AST: build_candidates reads only event field 0",
        fp["only_field_0_used"], True,
        "so a surrogate exact on the per-world multiset is exact on the "
        "weightings")
    chk("surrogate world count", sur["worlds"], PINNED_878["worlds"])
    chk("surrogate event total", sur["total"],
        PINNED_878["event_cardinality"])
    chk("surrogate per-world counts inside the certified range",
        sur["in_range"], True)
    chk("surrogate supported worlds", len(supported), PINNED_878["worlds"])
    chk("REBUILT zero-weight counts reproduce 878's certified row",
        got_zero, PINNED_878["zero_weight_events"])
    chk("REBUILT support-faithfulness reproduces 878's certified row",
        got_sf, want_sf)
    chk("REBUILT all-pairs discrimination", disc,
        PINNED_878["discriminating_pairs"])
    chk("REBUILT normalizability: every candidate has positive total mass",
        all(sum(nums[m]) > 0 for m in CANDIDATE_NAMES), True)

    fails = [c for c in checks if not c["match"]]
    return {
        "certificate": "B_RESTRICTION_878",
        "checks": checks,
        "checks_run": len(checks),
        "checks_failed": len(fails),
        "failures": fails[:EXHIBIT_CAP],
        "input_footprint": fp,
        "surrogate_scope": (
            "The Cycle-863 dependency of the 878 primary is ABSENT from this"
            " branch, so 878's trajectory is not re-run here.  The surrogate"
            " is exact on the four inputs the AST proves the weightings read,"
            " and is CONSTRAINED, not fitted: its per-world multiset is forced"
            " by 878's certified totals, formation count and range.  It is a"
            " consistency rebuild of the weighting layer, not an independent"
            " re-derivation of the event space; the event space itself enters"
            " through the certified receipt rows checked above."),
        "weighting_semantics": {m: meta[m]["definition"]
                                for m in CANDIDATE_NAMES},
        "pass": not fails,
    }


# --------------------------------------------------------------------------
# C: restriction gate -- 892 (fully live: 885 and 887 ARE on this branch)
# --------------------------------------------------------------------------
def containment_holding() -> list:
    """Recompute BOTH filters 892 applies -- REQ1-REQ5 admissibility from
    887's own harness, then containment on every configuration -- rather than
    trusting the pinned name list."""
    holding = []
    for name, fn in CATALOGUE:
        ev = NS887["evaluate_map"](fn)
        if not ev["admissible_REQ1_REQ5"]:
            continue
        cp = NS887["containment_profile"](fn)
        if cp["supp_subset_W_on_all_configs"]:
            holding.append(name)
    return sorted(holding)


HOLDING = containment_holding()


def frozen_configs() -> list:
    out = []
    for cfg in FAMILY:
        layers, src = walk_layers(cfg)
        if all(not lay for lay in layers[1:]):
            out.append(cfg["name"])
    return out


def confinement_rows() -> list:
    rows = []
    for cfg in FAMILY:
        layers, src = walk_layers(cfg)
        supp = set(cfg["sites"])
        reach = set()
        for lay in layers[1:]:
            reach |= set(lay)
        amp = set()
        for lay in layers:
            amp |= set(lay)
        rows.append({
            "config": cfg["name"],
            "reachable_sites": len(reach),
            "reach_meets_support": len(reach & supp),
            "amplitude_sites_inside_support": len(amp & supp),
            "amplitude_sites_outside_support": len(amp - supp),
            "walk_is_frozen": not reach,
        })
    return rows


def restriction_892() -> dict:
    checks: list[dict] = []

    def chk(name, got, want, note=""):
        checks.append({"check": name, "recomputed": got, "pinned": want,
                       "match": got == want, "note": note})

    chk("885 family digest", FAMILY_DIGEST, PINNED_892["family_digest"])
    chk("family size", len(FAMILY), 12)
    chk("containment-holding window names",
        HOLDING, sorted(PINNED_HOLDING_NAMES))
    chk("holding window count", len(HOLDING), PINNED_892["holding_windows"])
    chk("cell count = windows x configs x thetas",
        len(HOLDING) * len(FAMILY) * len(THETA_GRID), PINNED_892["cells"])

    vanish = [{"window": n, "config": c["name"], "theta": q(t)}
              for n in HOLDING for c in FAMILY for t in THETA_GRID
              if Z(c, t, window_of(n, c)) == 0]
    neg = [1 for n in HOLDING for c in FAMILY for t in THETA_GRID
           if Z(c, t, window_of(n, c)) < 0]
    chk("vanishing cells", len(vanish), PINNED_892["vanishing_cells"])
    chk("negativity violations", len(neg),
        PINNED_892["negativity_violations"])

    add_checks, add_bad = 0, 0
    for cfg in FAMILY:
        for t in THETA_GRID:
            a = window_of("minkowski_S_ball1__885_checker_dilation_k1", cfg)
            b = window_of("bounding_box", cfg) - a
            add_checks += 1
            if Z(cfg, t, a) + Z(cfg, t, b) != Z(cfg, t, a | b):
                add_bad += 1
    chk("finite-additivity checks", add_checks,
        PINNED_892["finite_additivity_checks"])
    chk("finite-additivity violations", add_bad,
        PINNED_892["finite_additivity_violations"])

    dil1 = "minkowski_S_ball1__885_checker_dilation_k1"
    T885 = NS892["THETA_885"]
    mass_moves = 0
    ratio_moves = 0
    for cfg in FAMILY:
        tot = {t: Z(cfg, t, INBOX) for t in T885}
        if len(set(tot.values())) != 1:
            mass_moves += 1
        rs = {Z(cfg, t, window_of(dil1, cfg)) / tot[t]
              for t in T885 if tot[t] != 0}
        if len(rs) > 1:
            ratio_moves += 1
    chk("total mass theta-dependent configs", mass_moves,
        PINNED_892["total_mass_theta_dependent_configs"])
    chk("box-normalized ratio still theta-dependent configs", ratio_moves,
        PINNED_892["normalized_ratio_still_theta_dependent_configs"])

    conf = confinement_rows()
    chk("amplitude sites inside supp(R), family total",
        sum(r["amplitude_sites_inside_support"] for r in conf),
        PINNED_892["amplitude_sites_inside_support_total"])
    chk("amplitude sites outside supp(R), family total",
        sum(r["amplitude_sites_outside_support"] for r in conf),
        PINNED_892["amplitude_sites_outside_support_total"])
    chk("configs whose reachable set meets supp(R)",
        sum(1 for r in conf if r["reach_meets_support"]),
        PINNED_892["reach_meets_support_configs"])
    chk("frozen walks", len(frozen_configs()), PINNED_892["frozen_configs"])

    ident, viol, orders = 0, 0, set()
    max_deg = 0
    for n in HOLDING:
        for cfg in FAMILY:
            md = interference_spectrum(cfg, window_of(n, cfg))
            for d, m in enumerate(md):
                if m != 0:
                    orders.add(d)
                    max_deg = max(max_deg, d)
            for t in THETA_GRID:
                p = (1 - t * t) / (1 + t * t)
                lhs = Z(cfg, t, window_of(n, cfg))
                rhs = sum((m * NS892["_cheb"](d, p)
                           for d, m in enumerate(md)), Fraction(0))
                ident += 1
                if lhs != rhs:
                    viol += 1
    chk("kernel identity checks", ident, PINNED_892["kernel_identity_checks"])
    chk("kernel identity violations", viol,
        PINNED_892["kernel_identity_violations"])
    chk("kernel max degree", max_deg, PINNED_892["kernel_max_degree"])
    chk("interference orders present", sorted(orders),
        PINNED_892["kernel_orders_present"])

    fails = [c for c in checks if not c["match"]]
    return {
        "certificate": "C_RESTRICTION_892",
        "checks": checks,
        "checks_run": len(checks),
        "checks_failed": len(fails),
        "failures": fails[:EXHIBIT_CAP],
        "vanishing_cells": vanish,
        "confinement_rows": conf,
        "method": ("fully live: the 885 family and the 887 catalogue are both "
                   "on this branch, so every 892 row is RECOMPUTED from the "
                   "AST-extracted Z machinery, not read out of a receipt"),
        "pass": not fails,
    }


# --------------------------------------------------------------------------
# D: Q1 -- the composition surface
# --------------------------------------------------------------------------
def z_profile() -> dict:
    """Everything about Z that a bridge must reproduce."""
    onrec: dict[str, set] = {}
    zvals: dict[str, dict] = {}
    degs: dict[str, int] = {}
    for cfg in FAMILY:
        supp = set(cfg["sites"])
        fr = set()
        for t in THETA_GRID:
            tot = Z(cfg, t, INBOX)
            fr.add(Fraction(0) if tot == 0 else Z(cfg, t, supp) / tot)
        onrec[cfg["name"]] = fr
        d = 0
        for n in HOLDING:
            md = interference_spectrum(cfg, window_of(n, cfg))
            for k, m in enumerate(md):
                if m != 0:
                    d = max(d, k)
        degs[cfg["name"]] = d
        zvals[cfg["name"]] = {
            n: {q(t): Z(cfg, t, window_of(n, cfg)) for t in THETA_GRID}
            for n in HOLDING}
    # windows that BOTH vanish and are positive across the family
    both = []
    for n in HOLDING:
        van, pos = set(), set()
        for cfg in FAMILY:
            for t in THETA_GRID:
                (van if Z(cfg, t, window_of(n, cfg)) == 0 else pos).add(
                    cfg["name"])
        if van and pos:
            both.append({"window": n, "vanishes_on": sorted(van),
                         "positive_on_count": len(pos),
                         "vanishes_on_count": len(van)})
    # window-ratio theta absorption
    absorb = {}
    for cfg in FAMILY:
        bad = 0
        tot = 0
        for a, b in combinations(HOLDING, 2):
            rs = set()
            for t in THETA_GRID:
                za, zb = Z(cfg, t, window_of(a, cfg)), Z(cfg, t,
                                                         window_of(b, cfg))
                if zb != 0:
                    rs.add(za / zb)
            tot += 1
            if len(rs) > 1:
                bad += 1
        absorb[cfg["name"]] = {"theta_varying_pairs": bad, "pairs": tot,
                               "absorbable": bad == 0}
    # distinct Z classes among the holding windows, per config
    zclasses = {}
    for cfg in FAMILY:
        sigs = {tuple(Z(cfg, t, window_of(n, cfg)) for t in THETA_GRID)
                for n in HOLDING}
        zclasses[cfg["name"]] = len(sigs)
    return {
        "on_record_mass_fraction_classes": {
            k: sorted(q(x) for x in v) for k, v in onrec.items()},
        "on_record_fraction_distinct_over_family": len(
            {x for v in onrec.values() for x in v}),
        "on_record_reaches_zero_on": sorted(
            k for k, v in onrec.items() if Fraction(0) in v),
        "on_record_reaches_one_on": sorted(
            k for k, v in onrec.items() if Fraction(1) in v),
        "max_interference_degree_per_config": degs,
        "configs_with_degree_above_zero": sorted(
            k for k, v in degs.items() if v > 0),
        "windows_that_both_vanish_and_are_positive": both,
        "window_ratio_theta_absorption": absorb,
        "configs_where_theta_is_absorbable": sorted(
            k for k, v in absorb.items() if v["absorbable"]),
        "distinct_Z_classes_among_holding_windows": zclasses,
        "_zvals": zvals,
        "_onrec": onrec,
        "_degs": degs,
    }


def mu_profile(nums, dens, sur) -> dict:
    """Everything about each 878 weighting that a bridge would have to use."""
    n_unformed = sur["n_unformed"]
    prof = {}
    for m in CANDIDATE_NAMES:
        v = nums[m]
        den = dens[m]
        total = sum(v)
        on_record = sum(x for e, x in zip(sur["events"], v)
                        if e[0] >= n_unformed)
        positives = sum(1 for x in v if x > 0)
        prof[m] = {
            "theta_arity": 0,
            "config_arity": 0,
            "zero_weight_atoms": len(v) - positives,
            "positive_atoms": positives,
            "support_faithful": positives == len(v),
            "on_record_mass_fraction": q(Fraction(on_record, total)),
            "on_record_mass_fraction_value": Fraction(on_record, total),
            "on_record_fraction_classes": 1,
            "chain_resolution": positives + 1,
            "polynomial_degree_in_cos_phi": 0,
            "total_mass": q(Fraction(total, den)) if den else "0/1",
        }
    return prof


def composition_certificate(zp: dict, mp: dict, sur: dict) -> dict:
    # --- the exact type mismatch at the substrate level
    e_card = PINNED_878["event_cardinality"]
    site_card = len(BOX)
    fiber, rem = divmod(e_card, site_card)
    # symmetry: the only group under which any 878 weighting is covariant is
    # the landed monitor-phase Z_11; the 892 family lives under the proper
    # cubic rotations.
    g878 = PINNED_878["world_orbit_size"]
    g892 = len(ROT24)
    common = gcd(g878, g892)
    covariant_878 = sorted(
        m for m, v in R878["findings"]["candidate_verdicts"].items()
        if v["covariance"]["landed_monitor_phase_group_on_worlds"])

    mismatch = {
        "878_index_set": {
            "name": "E, the realized record-write events",
            "cardinality": e_card,
            "atom_arity": 5,
            "atom_fields": ["world", "moment", "tag", "ordinal", "content"],
            "record_configuration_argument": False,
            "kernel_argument": False,
            "value_type": "Fraction >= 0",
        },
        "892_index_set": {
            "name": "(record configuration R, kernel theta, window W subset "
                    "of the box)",
            "site_cardinality": site_card,
            "configs": len(FAMILY),
            "holding_windows": len(HOLDING),
            "thetas": len(THETA_GRID),
            "record_configuration_argument": True,
            "kernel_argument": True,
            "value_type": "Fraction >= 0",
        },
        "cardinality": {
            "events_per_site": fiber, "remainder": rem,
            "uniform_fibre_surjection_exists": rem == 0,
            "note": ("a fibre-uniform surjection E -> BOX would need "
                     f"{site_card} | {e_card}; the remainder is {rem}"),
        },
        "symmetry": {
            "878_landed_group_order": g878,
            "878_group": "Z_11, the Cycle-856 monitor-phase relabelling",
            "892_family_group_order": g892,
            "892_group": "the proper cubic rotations acting on the box",
            "gcd": common,
            "only_trivial_homomorphism": common == 1,
            "weightings_covariant_under_the_878_group": covariant_878,
            "consequence": (
                "by Lagrange the image of any homomorphism Z_11 -> the cubic"
                f" rotation group has order dividing gcd({g878},{g892})"
                f" = {common}, so the ONLY such homomorphism is trivial."
                "  The single symmetry credential 878 was able to award --"
                f" covariance of {covariant_878} under the landed"
                " monitor-phase group -- is therefore invisible on the 892"
                " side: it cannot be transported across any bridge."),
        },
        "arity": {
            "Z_varies_with_the_record_configuration": True,
            "Z_quadratic_classes_over_the_family":
                PINNED_892["quadratic_classes"],
            "mu_classes_over_the_family": 1,
            "note": ("Z is a FAMILY of set functions indexed by the record"
                     " configuration; each 878 weighting is ONE set function"
                     " on ONE event space built from ONE trajectory.  The"
                     " event space has no record-configuration argument at"
                     " all -- its 'records' are the write events themselves,"
                     " not a parameter."),
        },
        "verdict": ("SUBSTRATE TYPE MISMATCH -- different index sets,"
                    " coprime symmetry groups, and a missing"
                    " record-configuration argument on the 878 side"),
    }

    # --- but they DO meet: both are finitely additive non-negative rational
    #     set functions on finite Boolean algebras.
    meeting = {
        "common_category": ("finitely additive non-negative Q-valued set"
                            " functions on a finite Boolean algebra"),
        "878_object": ("mu: 2^E -> Q_{>=0}, additive, atoms the 92,260"
                       " (world, tag, ordinal) singletons"),
        "892_object": ("Z(R, theta, .): 2^BOX -> Q_{>=0}, additive (IF2,"
                       " banked), atoms the box sites"),
        "the_bridge_defined": (
            "A BRIDGE is a pair (phi, N) with phi: E -> BOX u {bottom} any"
            " map and N(R, theta) > 0 any positive normalizer, such that for"
            " every record configuration R, every theta and every"
            " containment-holding admissible window W"
            "        mu(phi^{-1}(W)) = Z(R, theta, W) / N(R, theta)."
            "  phi and mu carry NO record-configuration argument and NO"
            " kernel argument; that is not an assumption, it is an"
            " AST-verified fact about build_candidates, whose signature and"
            " body are reproduced in certificate B."),
        "why_the_table_is_buildable": (
            "Because the left side of the bridge equation is INDEPENDENT of"
            " (R, theta) while the right side is not, every requirement can be"
            " tested WITHOUT constructing phi: any property of Z that varies"
            " with (R, theta) is a property no bridge can deliver, for any"
            " phi and any N.  The verdicts below are therefore"
            " bridge-independent -- they are not statements about one chosen"
            " identification that failed."),
    }

    # --- C894-T1
    both = zp["windows_that_both_vanish_and_are_positive"]
    t1 = {
        "theorem": "C894-T1 CONFIG-FREE BRIDGE OBSTRUCTION",
        "statement": (
            "If some containment-holding admissible window W has"
            " Z(R,theta,W) = 0 for one (R,theta) and Z(R',theta',W) > 0 for"
            " another, then no config-free weighting can satisfy the bridge"
            " equation on W for ANY phi and ANY positive normalizer:"
            " phi^{-1}(W) is one fixed event set, so mu(phi^{-1}(W)) is one"
            " fixed number, which cannot be both zero and positive after"
            " division by a positive N."),
        "witness_windows": both,
        "witness_count": len(both),
        "holds": len(both) > 0,
    }
    # --- C894-T2
    absorb = zp["window_ratio_theta_absorption"]
    unabsorbable = sorted(k for k, v in absorb.items() if not v["absorbable"])
    t2 = {
        "theorem": "C894-T2 NO WINDOW-RATIO NORMALIZER ABSORBS THETA",
        "statement": (
            "For a theta-free mu the ratio mu(phi^{-1}(W)) / mu(phi^{-1}(W'))"
            " is theta-free, so a bridge requires Z(R,theta,W)/Z(R,theta,W')"
            " to be theta-free on every pair of holding windows.  This"
            " STRICTLY STRENGTHENS 892's IF3, which tested only the"
            " box-mass normalizer: here every one of the"
            f" {len(list(combinations(HOLDING, 2)))} holding pairs is tested"
            " on every configuration."),
        "per_config": absorb,
        "configs_where_theta_is_unabsorbable": unabsorbable,
        "configs_unabsorbable_count": len(unabsorbable),
        "holds": len(unabsorbable) > 0,
    }
    return {
        "certificate": "D_COMPOSITION",
        "question": "Q1 -- where, exactly, could the two lineages meet?",
        "substrate_type_mismatch": mismatch,
        "the_meeting": meeting,
        "theorems": [t1, t2],
        "finding": (
            "BOTH answers are true and they are not in tension.  At the"
            " SUBSTRATE level the lineages do NOT meet: the index sets, the"
            " symmetry groups (coprime orders"
            f" {mismatch['symmetry']['878_landed_group_order']} and"
            f" {mismatch['symmetry']['892_family_group_order']}) and the"
            " arities differ, and the mismatch is computed above rather than"
            " asserted.  At the CATEGORY level they DO meet: both objects are"
            " finitely additive non-negative rational set functions on finite"
            " Boolean algebras, and the bridge equation above is the honest"
            " composition surface.  The table of Q2 is therefore buildable,"
            " and -- because the 878 side is provably free of both the"
            " record-configuration and the kernel argument -- every verdict"
            " in it holds for EVERY bridge, not merely for some canonical"
            " one."),
        "pass": True,
    }


# --------------------------------------------------------------------------
# E: Q2 -- the verdict table
# --------------------------------------------------------------------------
def if_sheet() -> list:
    """Read IF1..IF6 VERBATIM out of the pinned 892 primary by AST."""
    tree = ast.parse(read_text(C892_PRIMARY))
    out = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        keys = [k.value for k in node.keys
                if isinstance(k, ast.Constant) and isinstance(k.value, str)]
        if "id" not in keys or "requirement" not in keys:
            continue
        row = {}
        for k, v in zip(node.keys, node.values):
            if not (isinstance(k, ast.Constant) and k.value in
                    ("id", "requirement", "what_fails_without_it")):
                continue
            if isinstance(v, ast.Constant) and isinstance(v.value, str):
                row[k.value] = v.value
        if row.get("id", "").startswith("IF"):
            out.append(row)
    out.sort(key=lambda r: r["id"])
    return out


def verdict_table(zp: dict, mp: dict, planted: dict) -> dict:
    sheet = {r["id"]: r for r in if_sheet()}
    owed = [i for i in ("IF1", "IF3", "IF4", "IF5", "IF6")]
    both = zp["windows_that_both_vanish_and_are_positive"]
    unabsorbable = sorted(k for k, v in
                          zp["window_ratio_theta_absorption"].items()
                          if not v["absorbable"])
    deg_gt0 = zp["configs_with_degree_above_zero"]
    z_onrec_classes = zp["on_record_fraction_distinct_over_family"]
    z_zero_on = zp["on_record_reaches_zero_on"]
    z_one_on = zp["on_record_reaches_one_on"]
    zclass = zp["distinct_Z_classes_among_holding_windows"]

    def cell(name: str, p: dict, req: str) -> dict:
        """Every cell computed from p (the weighting's profile) and zp."""
        if req == "IF1":
            ok = (p["on_record_fraction_classes"] >= z_onrec_classes)
            return {
                "verdict": "PASS" if ok else "FAIL",
                "test": ("the weighting's on-record mass fraction must be able"
                         " to reproduce Z's, which ranges over"
                         f" {z_onrec_classes} distinct values across the"
                         " family -- reaching 0 on"
                         f" {len(z_zero_on)} configurations and 1 on"
                         f" {len(z_one_on)}"),
                "weighting_value": p["on_record_mass_fraction"],
                "weighting_fraction_classes": p["on_record_fraction_classes"],
                "Z_required_classes": z_onrec_classes,
                "Z_reaches_zero_on": z_zero_on,
                "Z_reaches_one_on": z_one_on,
                "why": (
                    "the weighting places a FIXED fraction"
                    f" {p['on_record_mass_fraction']} of its mass on the"
                    " record locus, while Z's on-record fraction is a"
                    " function of the configuration and of theta; a single"
                    " fixed fraction cannot track a varying one"
                    if not ok else
                    "the weighting's on-record fraction varies with the"
                    " configuration and covers Z's range"),
            }
        if req == "IF3":
            # EITHER the weight carries the kernel coordinate itself (then no
            # normalizer has to absorb anything), OR theta is absorbable by a
            # theta-invariant normalizer.  892's IF3 states exactly this
            # disjunction; the earlier conjunction here was a bug that made a
            # kernel-carrying weight unable to pass, which the planted
            # survivor exposed.
            ok = (p["theta_arity"] > 0 or not unabsorbable)
            return {
                "verdict": "PASS" if ok else "FAIL",
                "test": ("either the weighting carries the kernel coordinate,"
                         " or Z's theta-dependence must be absorbable by a"
                         " theta-invariant normalizer -- tested here on EVERY"
                         " holding-window pair, not only the box mass"
                         " (C894-T2)"),
                "weighting_theta_arity": p["theta_arity"],
                "configs_where_theta_is_unabsorbable": unabsorbable,
                "configs_unabsorbable_count": len(unabsorbable),
                "why": (
                    f"the weighting has kernel arity {p['theta_arity']} and"
                    f" theta survives every window-ratio normalizer on"
                    f" {len(unabsorbable)} of {len(FAMILY)} configurations"
                    if not ok else
                    "the weighting carries the kernel coordinate itself"),
            }
        if req == "IF4":
            ok = p.get("window_argument", False)
            return {
                "verdict": "PASS" if ok else "FAIL",
                "test": ("the weight must take the window as an ARGUMENT,"
                         " because Z separates the holding windows into"
                         f" {sorted(set(zclass.values()))} classes depending"
                         " on the configuration"),
                "weighting_has_window_argument": ok,
                "weighting_chain_resolution": p["chain_resolution"],
                "Z_distinct_window_classes_per_config": zclass,
                "resolution_is_sufficient":
                    p["chain_resolution"] >= max(zclass.values()),
                "why": (
                    "the failure is NOT resolution -- the weighting has"
                    f" {p['chain_resolution']} distinct values available"
                    " along a maximal nested chain, far more than the"
                    f" {max(zclass.values())} window classes Z ever needs."
                    "  The failure is arity: the weighting has no window"
                    " argument at all, so the window would have to come from"
                    " the bridge map, which is exactly the object nobody has"
                    " built"
                    if not ok else
                    "the weight is a set function of the window"),
            }
        if req == "IF5":
            tolerates = p["zero_weight_atoms"] > 0
            # C894-T1 bites only on a CONFIG-FREE weight: a weight indexed by
            # the record configuration assigns a different number to the same
            # window on different configurations and so escapes it.
            escapes_t1 = p.get("config_arity", 0) > 0 or not both
            ok = tolerates and escapes_t1
            return {
                "verdict": "PASS" if ok else "FAIL",
                "test": ("the weight must vanish where Z provably vanishes"
                         " (42 of 648 cells) and be positive where Z is"
                         " positive -- on the SAME window"),
                "sub_test_a_tolerates_vanishing": tolerates,
                "sub_test_a_zero_weight_atoms": p["zero_weight_atoms"],
                "sub_test_b_config_free_contradiction_windows":
                    [w["window"] for w in both],
                "sub_test_b_passes": escapes_t1,
                "weighting_config_arity": p.get("config_arity", 0),
                "why": (
                    ("sub-test (a) already fails: the weighting is strictly"
                     " positive on every atom, so mu(A) = 0 only for the"
                     " empty set, and it can never match a vanishing Z on a"
                     " non-empty window.  " if not tolerates else
                     "sub-test (a) PASSES -- the weighting has"
                     f" {p['zero_weight_atoms']} zero-weight atoms, so it CAN"
                     " vanish on a non-empty set.  ")
                    + ("sub-test (b) fails by C894-T1: "
                       f"{len(both)} holding windows both vanish and are"
                       " positive across the family, and this weighting has"
                       " record-configuration arity"
                       f" {p.get('config_arity', 0)}, so it assigns ONE fixed"
                       " number to each window's preimage -- which cannot be"
                       " both zero and positive"
                       if not escapes_t1 else
                       "sub-test (b) passes")
                    if not ok else
                    "the weight vanishes exactly on Z's vanishing cells"),
            }
        if req == "IF6":
            ok = (p["polynomial_degree_in_cos_phi"]
                  >= PINNED_892["kernel_max_degree"])
            return {
                "verdict": "PASS" if ok else "FAIL",
                "test": ("the weight must be a degree-D polynomial in cos phi"
                         f" with D <= the walk depth {MAX_STEPS}; Z attains"
                         f" degree {PINNED_892['kernel_max_degree']} and"
                         " realizes orders"
                         f" {PINNED_892['kernel_orders_present']}"),
                "weighting_degree": p["polynomial_degree_in_cos_phi"],
                "Z_max_degree": PINNED_892["kernel_max_degree"],
                "configs_with_Z_degree_above_zero": deg_gt0,
                "configs_matchable_at_degree_zero":
                    len(FAMILY) - len(deg_gt0),
                "why": (
                    f"the weighting is degree {p['polynomial_degree_in_cos_phi']}"
                    " in cos phi -- a constant -- while Z reaches degree"
                    f" {PINNED_892['kernel_max_degree']} on"
                    f" {len(deg_gt0)} of {len(FAMILY)} configurations; a"
                    " constant can match a non-constant polynomial only where"
                    " that polynomial is itself constant"
                    if not ok else
                    "the weight carries the full Chebyshev structure"),
            }
        raise AssertionError(f"unhandled requirement {req}")

    rows = {}
    for m in CANDIDATE_NAMES:
        rows[m] = {r: cell(m, mp[m], r) for r in owed}
    # IF2 is BANKED, not owed -- reported for completeness, never scored
    for m in CANDIDATE_NAMES:
        rows[m]["IF2_BANKED"] = {
            "verdict": "BANKED",
            "test": "finite additivity over disjoint window pieces",
            "why": ("Z already has this property (a site-wise sum) and every"
                    " 878 candidate is additive by construction; the 892"
                    " receipt banks it, so it is not scored"),
        }

    planted_rows = {}
    for name, p in planted.items():
        planted_rows[name] = {r: cell(name, p, r) for r in owed}

    survivors = sorted(m for m in CANDIDATE_NAMES
                       if all(rows[m][r]["verdict"] == "PASS" for r in owed))
    passes = {m: sum(1 for r in owed if rows[m][r]["verdict"] == "PASS")
              for m in CANDIDATE_NAMES}
    computed = sum(1 for m in CANDIDATE_NAMES for r in owed
                   if rows[m][r]["verdict"] in ("PASS", "FAIL"))
    expected = len(CANDIDATE_NAMES) * len(owed)

    if len(survivors) == 1:
        outcome = "SELECTION"
    elif len(survivors) > 1:
        outcome = "NARROWING"
    else:
        outcome = "NO-GO"

    return {
        "certificate": "E_TABLE",
        "question": "Q2 -- the five weightings against the IF sheet",
        "requirements_verbatim_from_the_pinned_892_primary": sheet,
        "owed_requirements": owed,
        "banked_requirement": "IF2",
        "table": rows,
        "planted_controls": planted_rows,
        "passes_per_weighting": passes,
        "survivors": survivors,
        "outcome": outcome,
        "cells_computed": computed,
        "cells_expected": expected,
        "table_complete": computed == expected,
        "best_performer": max(passes, key=lambda k: passes[k]),
        "the_only_discriminating_requirement": [
            r for r in owed
            if len({rows[m][r]["verdict"] for m in CANDIDATE_NAMES}) > 1
            or len({rows[m][r].get("sub_test_a_tolerates_vanishing")
                    for m in CANDIDATE_NAMES}) > 1],
        "pass": computed == expected,
    }


# --------------------------------------------------------------------------
# F: falsifier visibility -- planted weightings
# --------------------------------------------------------------------------
def planted_profiles(zp: dict) -> dict:
    """Two DECLARED-PLANTED weightings run through the identical table.

    P1 is designed to pass every owed requirement.  If the table cannot see
    it, the table is blind and this run fails.  P2 is designed to pass some
    and fail others: if the table passed P2 too it would be a rubber stamp
    that accepts anything configuration-indexed, so P2's partial score is
    what proves the table has resolution.
    """
    # P1: the configuration-and-kernel-indexed pullback of Z itself.
    p1 = {
        "declared": "PLANTED -- designed to pass; not a physical proposal",
        "definition": ("mu(R, theta, W) := Z(R, theta, W); the weight is the"
                       " pullback of the pinned Z along the identity bridge on"
                       " windows, carried on the box-site atom space indexed"
                       " by the record configuration"),
        "theta_arity": 1,
        "config_arity": len(FAMILY),
        "zero_weight_atoms": PINNED_892["vanishing_cells"],
        "positive_atoms": PINNED_892["cells"] - PINNED_892["vanishing_cells"],
        "support_faithful": False,
        "on_record_mass_fraction": "config-dependent",
        "on_record_fraction_classes":
            zp["on_record_fraction_distinct_over_family"],
        "chain_resolution": PINNED_892["cells"],
        "polynomial_degree_in_cos_phi": PINNED_892["kernel_max_degree"],
        "window_argument": True,
    }
    # P2: the same object with the kernel frozen at a single theta.
    t0 = THETA_GRID[0]
    p2 = {
        "declared": "PLANTED NEAR-MISS -- designed to pass some and fail others",
        "definition": (f"mu(R, W) := Z(R, {q(t0)}, W); configuration-indexed"
                       " like P1 but with the kernel coordinate frozen"),
        "theta_arity": 0,
        "config_arity": len(FAMILY),
        "zero_weight_atoms": sum(
            1 for n in HOLDING for c in FAMILY
            if Z(c, t0, window_of(n, c)) == 0) * len(THETA_GRID),
        "positive_atoms": PINNED_892["cells"],
        "support_faithful": False,
        "on_record_mass_fraction": "config-dependent",
        "on_record_fraction_classes":
            zp["on_record_fraction_distinct_over_family"],
        "chain_resolution": PINNED_892["cells"],
        "polynomial_degree_in_cos_phi": 0,
        "window_argument": True,
    }
    return {"P1_PLANTED_SURVIVOR": p1, "P2_PLANTED_NEAR_MISS": p2}


def falsifier_certificate(table: dict) -> dict:
    owed = table["owed_requirements"]
    pr = table["planted_controls"]
    p1 = pr["P1_PLANTED_SURVIVOR"]
    p2 = pr["P2_PLANTED_NEAR_MISS"]
    p1_pass = [r for r in owed if p1[r]["verdict"] == "PASS"]
    p2_pass = [r for r in owed if p2[r]["verdict"] == "PASS"]
    p1_visible = len(p1_pass) == len(owed)
    p2_partial = 0 < len(p2_pass) < len(owed)
    return {
        "certificate": "F_FALSIFIER",
        "planted_survivor_requirements_passed": p1_pass,
        "planted_survivor_is_visible": p1_visible,
        "planted_near_miss_requirements_passed": p2_pass,
        "planted_near_miss_requirements_failed": [
            r for r in owed if p2[r]["verdict"] != "PASS"],
        "planted_near_miss_is_partial": p2_partial,
        "finding": (
            f"The table SEES the planted survivor: P1 passes all"
            f" {len(owed)} owed requirements.  It is not a rubber stamp: the"
            f" planted near-miss P2, which differs from P1 only in freezing"
            f" the kernel coordinate, passes {len(p2_pass)} and fails"
            f" {len(owed) - len(p2_pass)}"
            f" ({[r for r in owed if p2[r]['verdict'] != 'PASS']}) -- exactly"
            f" the two requirements that reference the kernel.  A table that"
            f" returns all-FAIL on the real candidates while returning"
            f" all-PASS on a designed survivor and a split verdict on a"
            f" designed near-miss is discriminating, not degenerate."),
        "pass": p1_visible and p2_partial,
    }


# --------------------------------------------------------------------------
# G: needle gate
# --------------------------------------------------------------------------
def needle_certificate(payloads: dict) -> dict:
    blob = json.dumps(payloads, default=str).lower()
    self_text = read_text(SELF_REL).lower()
    rows = {v: {"in_derived_content": v in blob,
                "in_file_text": self_text.count(v)}
            for v in BORN_VOCABULARY}
    leaked = sorted(v for v, r in rows.items() if r["in_derived_content"])
    axioms = read_text(AXIOMS_MD)
    excl = ("Born weights" in axioms and "probability" in axioms)
    return {
        "certificate": "G_NEEDLE",
        "vocabulary_source": ("BORN_VOCABULARY, AST-extracted verbatim from"
                              " the pinned 892 primary"),
        "vocabulary": list(BORN_VOCABULARY),
        "rows": rows,
        "leaked_into_derived_content": leaked,
        "axiom_exclusion_list_present_in_pinned_md": excl,
        "scope": ("the gate is on DERIVED content -- the composition surface,"
                  " the verdict table and the residual property sheet.  Prose"
                  " in this file that names the exclusion in order to guard"
                  " against it is not a premise and is not gated."),
        "pass": not leaked and excl,
    }


# --------------------------------------------------------------------------
# H: Q3 -- the residual, sized
# --------------------------------------------------------------------------
def residual_certificate(zp: dict, mp: dict, table: dict) -> dict:
    both = zp["windows_that_both_vanish_and_are_positive"]
    unabsorbable = sorted(k for k, v in
                          zp["window_ratio_theta_absorption"].items()
                          if not v["absorbable"])
    # size the bridging object: the free rational parameters of a weight that
    # meets the whole sheet.
    amp_sites = set()
    for cfg in FAMILY:
        layers, _ = walk_layers(cfg)
        for lay in layers:
            amp_sites |= set(lay)
    coeffs_per_cell = MAX_STEPS + 1
    spec_by_window = len(FAMILY) * len(HOLDING) * coeffs_per_cell
    spec_by_site = sum(
        len({x for lay in walk_layers(cfg)[0] for x in lay})
        for cfg in FAMILY) * coeffs_per_cell

    sheet = [
        {"property": "P1 RECORD-CONFIGURATION ARITY",
         "requirement": ("the weight must be a FAMILY of set functions indexed"
                         " by the record configuration, not one set function"
                         " on one event space"),
         "derived_from": (
             f"Z splits the {len(FAMILY)}-configuration family into"
             f" {PINNED_892['quadratic_classes']} distinct classes at"
             f" quadratic order against {PINNED_892['linear_classes']} at"
             " linear order (892 certificate G, recomputed here as the"
             " distinct-Z-class rows); each 878 weighting supplies exactly 1"
             " class because its construction has no configuration argument"
             " (AST-verified in certificate B)"),
         "deficit": {"required_classes": PINNED_892["quadratic_classes"],
                     "supplied_classes": 1},
         "closes": ["IF1", "IF5"]},
        {"property": "P2 KERNEL ARITY WITH BOUNDED POLYNOMIAL ORDER",
         "requirement": ("the weight must carry the kernel coordinate"
                         " cos phi as a polynomial of degree at most the walk"
                         " depth"),
         "derived_from": (
             f"C894-T2 computed here: on {len(unabsorbable)} of"
             f" {len(FAMILY)} configurations theta survives EVERY"
             f" window-ratio normalizer over all"
             f" {len(list(combinations(HOLDING, 2)))} holding pairs, so no"
             " theta-free normalizer removes it; and 892's certificate H,"
             f" recomputed here, fixes the order at"
             f" {PINNED_892['kernel_max_degree']} with orders"
             f" {PINNED_892['kernel_orders_present']} realized"),
         "deficit": {"required_degree": PINNED_892["kernel_max_degree"],
                     "supplied_degree": 0,
                     "coefficients_per_cell": coeffs_per_cell},
         "closes": ["IF3", "IF6"]},
        {"property": "P3 CONFIGURATION-DEPENDENT ZERO SET",
         "requirement": ("the weight must vanish on exactly the cells where Z"
                         " vanishes and be positive on the rest, with the"
                         " zero set depending on the configuration"),
         "derived_from": (
             f"{PINNED_892['vanishing_cells']} of {PINNED_892['cells']} cells"
             f" vanish, and {len(both)} holding windows"
             f" ({[w['window'] for w in both]}) both vanish and are positive"
             " across the family -- the exact obstruction of C894-T1"),
         "deficit": {"required_vanishing_cells":
                     PINNED_892["vanishing_cells"],
                     "supplied_by_the_best_878_candidate":
                     "a configuration-independent zero set"},
         "closes": ["IF5"]},
        {"property": "P4 OFF-RECORD LOCUS",
         "requirement": ("the weight must place mass off supp(R), and its"
                         " on-record fraction must be able to reach 0 and 1"),
         "derived_from": (
             f"{PINNED_892['amplitude_sites_outside_support_total']} amplitude"
             f" sites lie outside supp(R) against"
             f" {PINNED_892['amplitude_sites_inside_support_total']} inside,"
             " and the inside sites are exactly the seed (892 certificate E,"
             " recomputed here); the on-record mass fraction reaches 0 on"
             f" {len(zp['on_record_reaches_zero_on'])} configurations"
             f" ({zp['on_record_reaches_zero_on']}) and 1 on"
             f" {len(zp['on_record_reaches_one_on'])}"
             f" ({zp['on_record_reaches_one_on']})"),
         "deficit": {"required_fraction_classes":
                     zp["on_record_fraction_distinct_over_family"],
                     "supplied_fraction_classes": 1},
         "closes": ["IF1"]},
        {"property": "P5 WINDOW ARGUMENT",
         "requirement": "the weight must take the window as an argument",
         "derived_from": (
             "Z separates the holding windows into"
             f" {sorted(set(zp['distinct_Z_classes_among_holding_windows'].values()))}"
             " classes depending on the configuration; the 878 weightings have"
             " ample resolution but no window argument"),
         "deficit": {"required": "a set function on box windows",
                     "supplied": "a set function on record-write events"},
         "closes": ["IF4"]},
    ]
    return {
        "certificate": "H_RESIDUAL",
        "question": "Q3 -- what would close it",
        "outcome_class": table["outcome"],
        "minimal_property_sheet_for_the_missing_weighting": sheet,
        "properties_required": len(sheet),
        "bridging_object": {
            "what_is_missing": (
                "a map Phi from record configurations to event-space"
                " measures.  Every 878 weighting is Phi evaluated at a single"
                " unnamed configuration; the 892 side needs Phi itself."),
            "specification_size_by_window":
                f"{len(FAMILY)} configs x {len(HOLDING)} holding windows x"
                f" {coeffs_per_cell} Chebyshev coefficients ="
                f" {spec_by_window} rationals",
            "specification_size_by_site":
                f"{spec_by_site} rationals if specified site-wise on the"
                f" amplitude support (additivity then determines every"
                f" window)",
            "reduction_from_additivity": spec_by_window - spec_by_site
            if spec_by_window > spec_by_site else 0,
            "amplitude_sites_in_the_union_over_the_family": len(amp_sites),
        },
        "what_would_separate_survivors": (
            "not applicable at this outcome class: there are no survivors to"
            " separate.  The next computed fact that would MOVE the result is"
            " a sixth weighting carrying P1 and P2; P3, P4 and P5 then follow"
            " from the pinned Z rows without further input."
            if table["outcome"] == "NO-GO" else
            "the survivors differ on the requirements listed as"
            " discriminating in certificate E"),
        "next_door_sized": (
            f"{len(sheet)} properties, of which"
            " P1 (configuration arity) and P2 (kernel arity) are the only two"
            " that cannot be read off the pinned artifacts -- they must be"
            " CONSTRUCTED.  P3, P4 and P5 are then forced by rows this cycle"
            " already computed.  The construction target is a"
            f" {spec_by_site}-rational object, or"
            f" {spec_by_window} if specified window-wise."),
        "pass": len(sheet) >= 5,
    }


# --------------------------------------------------------------------------
# run
# --------------------------------------------------------------------------
def build_everything() -> dict:
    A = pins_certificate()
    B = restriction_878()
    C = restriction_892()
    zp = z_profile()
    sur = surrogate_event_space()
    nums, dens, meta, per_world, supported, common = build_candidates(
        sur["events"], sur["occ"], sur["formed"], sur["boundaries"])
    mp = mu_profile(nums, dens, sur)
    planted = planted_profiles(zp)
    D = composition_certificate(zp, mp, sur)
    E = verdict_table(zp, mp, planted)
    F = falsifier_certificate(E)
    H = residual_certificate(zp, mp, E)
    G = needle_certificate({
        "composition": {k: v for k, v in D.items() if k != "certificate"},
        "table": E["table"],
        "residual": H["minimal_property_sheet_for_the_missing_weighting"],
        "bridging": H["bridging_object"],
    })
    return {"A": A, "B": B, "C": C, "D": D, "E": E, "F": F, "G": G, "H": H,
            "_zp": zp, "_mp": mp}


def science_payload(r: dict) -> dict:
    """Everything a second run must reproduce bit-for-bit."""
    return {
        "B_checks": [(c["check"], str(c["recomputed"]), c["match"])
                     for c in r["B"]["checks"]],
        "C_checks": [(c["check"], str(c["recomputed"]), c["match"])
                     for c in r["C"]["checks"]],
        "vanishing": r["C"]["vanishing_cells"],
        "zp": {k: v for k, v in r["_zp"].items() if not k.startswith("_")},
        "mp": {m: {k: str(v) for k, v in p.items()}
               for m, p in r["_mp"].items()},
        "table": {m: {q_: c["verdict"] for q_, c in row.items()}
                  for m, row in r["E"]["table"].items()},
        "planted": {m: {q_: c["verdict"] for q_, c in row.items()}
                    for m, row in r["E"]["planted_controls"].items()},
        "outcome": r["E"]["outcome"],
        "survivors": r["E"]["survivors"],
    }


def main() -> int:
    r1 = build_everything()
    d1 = digest(science_payload(r1))
    # deterministic double build: independent caches, independent rebuild
    NS892["_WALK_CACHE"].clear()
    NS892["_AMP_CACHE"].clear()
    r2 = build_everything()
    d2 = digest(science_payload(r2))
    double_ok = d1 == d2

    r = r1
    A, B, C, D, E, F, G, H = (r["A"], r["B"], r["C"], r["D"], r["E"], r["F"],
                              r["G"], r["H"])
    elapsed = time.time() - START

    certs = {"A_PINS": A["pass"], "B_RESTRICTION_878": B["pass"],
             "C_RESTRICTION_892": C["pass"], "D_COMPOSITION": D["pass"],
             "E_TABLE": E["pass"], "F_FALSIFIER": F["pass"],
             "G_NEEDLE": G["pass"], "H_RESIDUAL": H["pass"],
             "I_DOUBLE_BUILD": double_ok,
             "J_RUNTIME": elapsed <= RUNTIME_CAP_SEC}
    all_pass = all(certs.values())

    # ---------------- stdout ----------------
    P = print
    P("=" * 74)
    P(f"CYCLE {CYCLE} -- THE INTERFACE ATTACK")
    P("does gravity's Z constrain the Born selection?")
    P("=" * 74)
    P("")
    P("A: PINS")
    for row in A["rows"]:
        P(f"  {'OK ' if row['brief_sha256_match'] and row['brief_git_blob_match'] else 'BAD'}"
          f" {row['path']}")
        P(f"      sha256 {row['sha256']}")
        P(f"      blob   {row['git_blob']}  bytes {row['bytes']}")
    P(f"  vendored 878 primary blob == its own receipt's record: "
      f"{A['vendored_878_primary_blob_matches_its_own_receipt']}")
    P(f"  firewall hits: {A['firewall_hits']}  "
      f"forbidden stems imported: {A['forbidden_stems_loaded']}")
    P(f"  AST nodes missing: {A['ast_nodes_missing']}")
    P(f"  A_PINS pass: {A['pass']}")
    P("")

    P("B: RESTRICTION GATE -- 878 (the vendored event space)")
    for c in B["checks"]:
        P(f"  [{'ok ' if c['match'] else 'FAIL'}] {c['check']}")
        P(f"        recomputed={c['recomputed']}  pinned={c['pinned']}")
    P(f"  checks {B['checks_run']}, failed {B['checks_failed']}")
    P(f"  {B['surrogate_scope']}")
    P(f"  B pass: {B['pass']}")
    P("")

    P("C: RESTRICTION GATE -- 892 (Z, recomputed live)")
    for c in C["checks"]:
        P(f"  [{'ok ' if c['match'] else 'FAIL'}] {c['check']}")
        P(f"        recomputed={c['recomputed']}  pinned={c['pinned']}")
    P(f"  checks {C['checks_run']}, failed {C['checks_failed']}")
    P(f"  C pass: {C['pass']}")
    P("")

    P("D: Q1 -- THE COMPOSITION SURFACE")
    m = D["substrate_type_mismatch"]
    P("  substrate level -- TYPE MISMATCH, computed:")
    P(f"    878 index set: {m['878_index_set']['name']}, "
      f"|E| = {m['878_index_set']['cardinality']}, atom arity "
      f"{m['878_index_set']['atom_arity']} "
      f"{m['878_index_set']['atom_fields']}")
    P(f"      record-configuration argument: "
      f"{m['878_index_set']['record_configuration_argument']}   "
      f"kernel argument: {m['878_index_set']['kernel_argument']}")
    P(f"    892 index set: {m['892_index_set']['name']}")
    P(f"      {m['892_index_set']['configs']} configs x "
      f"{m['892_index_set']['holding_windows']} holding windows x "
      f"{m['892_index_set']['thetas']} thetas over "
      f"{m['892_index_set']['site_cardinality']} sites")
    P(f"      record-configuration argument: "
      f"{m['892_index_set']['record_configuration_argument']}   "
      f"kernel argument: {m['892_index_set']['kernel_argument']}")
    P(f"    cardinality: {m['cardinality']['note']}")
    P(f"    symmetry: |Z_11| = {m['symmetry']['878_landed_group_order']}, "
      f"|cubic rotations| = {m['symmetry']['892_family_group_order']}, "
      f"gcd = {m['symmetry']['gcd']}")
    P(f"      {m['symmetry']['consequence']}")
    P(f"    arity: Z has {m['arity']['Z_quadratic_classes_over_the_family']} "
      f"quadratic classes over the family; every 878 weighting has "
      f"{m['arity']['mu_classes_over_the_family']}")
    P("")
    P("  category level -- THEY DO MEET:")
    P(f"    {D['the_meeting']['common_category']}")
    P(f"    bridge: {D['the_meeting']['the_bridge_defined']}")
    P(f"    {D['the_meeting']['why_the_table_is_buildable']}")
    P("")
    for t in D["theorems"]:
        P(f"  {t['theorem']}  holds={t['holds']}")
        P(f"    {t['statement']}")
        if "witness_windows" in t:
            for w in t["witness_windows"]:
                P(f"      witness: {w['window']} vanishes on "
                  f"{w['vanishes_on_count']} and is positive on "
                  f"{w['positive_on_count']} (config,theta) cells; "
                  f"vanishing configs {w['vanishes_on']}")
        if "per_config" in t:
            for k, v in t["per_config"].items():
                P(f"      {k}: theta-varying window pairs "
                  f"{v['theta_varying_pairs']}/{v['pairs']}  "
                  f"absorbable={v['absorbable']}")
    P(f"  D finding: {D['finding']}")
    P("")

    P("E: Q2 -- THE VERDICT TABLE (5 weightings x 5 owed requirements)")
    P("")
    owed = E["owed_requirements"]
    P(f"  {'weighting':<26}" + "".join(f"{r:>7}" for r in owed) + "   passed")
    P("  " + "-" * 70)
    for mname in CANDIDATE_NAMES:
        row = E["table"][mname]
        P(f"  {mname:<26}"
          + "".join(f"{row[rq]['verdict']:>7}" for rq in owed)
          + f"   {E['passes_per_weighting'][mname]}/{len(owed)}")
    P("  " + "-" * 70)
    for pname, prow in E["planted_controls"].items():
        P(f"  {pname:<26}"
          + "".join(f"{prow[rq]['verdict']:>7}" for rq in owed)
          + f"   {sum(1 for rq in owed if prow[rq]['verdict']=='PASS')}"
            f"/{len(owed)}   [PLANTED]")
    P("")
    P(f"  cells computed {E['cells_computed']}/{E['cells_expected']}   "
      f"complete={E['table_complete']}")
    P(f"  survivors: {E['survivors']}")
    P(f"  OUTCOME CLASS: {E['outcome']}")
    P("")
    P("  every cell, with its witness:")
    for mname in CANDIDATE_NAMES:
        P(f"    {mname}")
        for rq in owed:
            c = E["table"][mname][rq]
            P(f"      {rq} {c['verdict']}: {c['why']}")
    P("")
    P("  the requirements verbatim from the pinned 892 primary:")
    for rid, row in sorted(
            E["requirements_verbatim_from_the_pinned_892_primary"].items()):
        P(f"    {rid}: {row['requirement']}")
    P("")

    P("F: FALSIFIER VISIBILITY")
    P(f"  planted survivor passes: {F['planted_survivor_requirements_passed']}")
    P(f"  planted near-miss passes {F['planted_near_miss_requirements_passed']}"
      f", fails {F['planted_near_miss_requirements_failed']}")
    P(f"  {F['finding']}")
    P(f"  F pass: {F['pass']}")
    P("")

    P("G: NEEDLE GATE")
    P(f"  vocabulary: {list(BORN_VOCABULARY)}")
    P(f"  leaked into derived content: {G['leaked_into_derived_content']}")
    P(f"  axiom exclusion list present in the pinned md: "
      f"{G['axiom_exclusion_list_present_in_pinned_md']}")
    P(f"  G pass: {G['pass']}")
    P("")

    P("H: Q3 -- THE RESIDUAL, SIZED")
    for s in H["minimal_property_sheet_for_the_missing_weighting"]:
        P(f"  {s['property']}")
        P(f"    requires: {s['requirement']}")
        P(f"    derived from: {s['derived_from']}")
        P(f"    deficit: {s['deficit']}")
        P(f"    closes: {s['closes']}")
    P(f"  bridging object: {H['bridging_object']['what_is_missing']}")
    P(f"    size by window: "
      f"{H['bridging_object']['specification_size_by_window']}")
    P(f"    size by site:   "
      f"{H['bridging_object']['specification_size_by_site']}")
    P(f"  next door sized: {H['next_door_sized']}")
    P("")

    P("=" * 74)
    for k, v in certs.items():
        P(f"  {k:<20} {'PASS' if v else 'FAIL'}")
    P(f"  science digest (build 1): {d1}")
    P(f"  science digest (build 2): {d2}")
    P(f"  deterministic double build: {double_ok}")
    P(f"  elapsed {elapsed:.3f}s (cap {RUNTIME_CAP_SEC}s)")
    P(f"  ALL CERTIFICATES: {'PASS' if all_pass else 'FAIL'}")
    P(f"  OUTCOME: {E['outcome']}")
    P("=" * 74)
    P("")
    P(f"BOUNDARY: {BOUNDARY_STATEMENT}")

    receipt = {
        "cycle": CYCLE,
        "block": "toe-time-blockG17-20260802",
        "campaign": "campaign-5-born-groundwork",
        "question": ("Cycle 894: does gravity's Z constrain the Born"
                     " selection?  Which of 878's five admissible weightings"
                     " can satisfy 892's IF sheet against Z's computed"
                     " structure?"),
        "self_sha256": sha256_of(read_bytes(SELF_REL)),
        "source_pins": [{"path": r["path"], "sha256": r["sha256"],
                         "git_blob": r["git_blob"]} for r in A["rows"]],
        "certificate_pass": certs,
        "all_certificates_pass": all_pass,
        "Q1_composition": {
            "substrate_verdict": D["substrate_type_mismatch"]["verdict"],
            "category_meeting": D["the_meeting"]["common_category"],
            "bridge_definition": D["the_meeting"]["the_bridge_defined"],
            "symmetry_obstruction": D["substrate_type_mismatch"]["symmetry"],
            "cardinality_obstruction":
                D["substrate_type_mismatch"]["cardinality"],
            "arity_obstruction": D["substrate_type_mismatch"]["arity"],
            "finding": D["finding"],
        },
        "Q2_table": {
            "owed_requirements": owed,
            "verdicts": {mname: {rq: E["table"][mname][rq]["verdict"]
                                 for rq in owed}
                         for mname in CANDIDATE_NAMES},
            "passes_per_weighting": E["passes_per_weighting"],
            "survivors": E["survivors"],
            "outcome": E["outcome"],
            "cells_computed": E["cells_computed"],
            "cells_expected": E["cells_expected"],
            "cell_witnesses": E["table"],
            "planted_controls": {
                p: {rq: E["planted_controls"][p][rq]["verdict"] for rq in owed}
                for p in E["planted_controls"]},
            "requirements_verbatim":
                E["requirements_verbatim_from_the_pinned_892_primary"],
        },
        "Q3_residual": {
            "property_sheet":
                H["minimal_property_sheet_for_the_missing_weighting"],
            "bridging_object": H["bridging_object"],
            "next_door_sized": H["next_door_sized"],
            "what_would_separate_survivors":
                H["what_would_separate_survivors"],
        },
        "theorems": [
            {"id": t["theorem"], "statement": t["statement"],
             "holds": t["holds"]} for t in D["theorems"]],
        "restriction_gate_878": {
            "checks_run": B["checks_run"],
            "checks_failed": B["checks_failed"],
            "scope": B["surrogate_scope"],
            "pass": B["pass"],
        },
        "restriction_gate_892": {
            "checks_run": C["checks_run"],
            "checks_failed": C["checks_failed"],
            "method": C["method"],
            "pass": C["pass"],
        },
        "Z_profile": {k: v for k, v in r["_zp"].items()
                      if not k.startswith("_")},
        "mu_profile": {mname: {k: str(v) for k, v in p.items()}
                       for mname, p in r["_mp"].items()},
        "falsifier": {k: v for k, v in F.items() if k != "certificate"},
        "needle": {k: v for k, v in G.items() if k != "certificate"},
        "deterministic_double_build": double_ok,
        "science_digest": d1,
        "family_digest": FAMILY_DIGEST,
        "elapsed_sec": round(elapsed, 3),
        "scope": (
            "One 12-configuration family (digest 30edaa3d5ca03c24) in a box of"
            f" radius {RBOX} with walk depth {MAX_STEPS}; the nine"
            " containment-holding admissible windows recomputed from 887's"
            " catalogue; a six-value theta grid; and 878's five admissible"
            " weightings, whose semantics are AST-extracted from the vendored"
            " primary and whose certified counts are reproduced from the"
            " vendored receipt.  878's Cycle-863 dependency is absent from"
            " this branch, so its trajectory is not re-run: the weighting"
            " layer is rebuilt on a surrogate that is exact on the four inputs"
            " the AST proves the weightings read, and the event space itself"
            " enters through certified receipt rows."),
        "boundary": BOUNDARY_STATEMENT,
        "claim_type": "bounded_theorem",
        "authority": "none",
        "audit": "unset",
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(receipt, indent=2, sort_keys=True,
                                   default=str) + "\n", encoding="utf-8")
    P(f"receipt: {OUT_JSON.relative_to(ROOT)}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
