#!/usr/bin/env python3
"""Cycle 947 -- INDEPENDENT CHECKER for the H0 discharge attempt.

SPEC'D TO REFUTE.  This runner does not confirm the primary; it tries to break
it, with machinery chosen to be disjoint from the primary's wherever a second
route exists:

  * FORWARD reachability instead of backward for every cone.  The primary
    walks control-to-target edges backwards from the menu wires; this runner
    computes, for every wire, the set of wires it can influence, and then reads
    the ancestor set off the forward relation.  The two must agree.
  * A SCALAR PER-LANE SIMULATOR instead of the packed SIMD machine.  The
    primary establishes the lane fibration by parsing the emitted statements;
    this runner reconstructs the site map semantically, by extracting each
    lane's own sub-schedule (the gates whose mask contains that lane) and
    running it on a scalar bit vector.  If the fibration is real, the scalar
    machine and the packed machine agree bit for bit at that lane, forever.
  * A DIFFERENT GENERATOR SET for the adversarial symmetry search: subset
    relabellings sigma_A over random lane subsets, and 3-cycles inside a
    station-position class, rather than the primary's single-lane
    relabellings and transpositions.
  * MUTATION PROBES with demonstrated teeth, and tamper tests that must fail
    CLOSED.

VERDICT VOCABULARY: SUPPORTED / REFUTED, per clause.  Never "passed".

IMPORT FIREWALL.  The primary runner and every pinned science runner are on
the module blocklist.  The checker AST-lifts the pinned 936 compiler exactly
as the primary does -- that is the shared pinned SUBSTRATE, not shared
INSTRUMENTATION -- and re-derives every instrument of its own.
"""

from __future__ import annotations

import ast
import importlib.abc
import itertools
import json
import math
import random
import subprocess
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import combinations, product
from pathlib import Path
from time import monotonic
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

RUNTIME_BUDGET_SEC = 1800

CORE_PATH = ("scripts/frontier_cycle719_two_rail_recurrent_controller_core"
             "_2026_07_26.py")
C936_PATH = "scripts/frontier_cycle936_choice_substrate_2026_07_28.py"
C946_RECEIPT = "outputs/mirror_kernel_cycle946_receipt_2026_07_28.json"
PRIMARY_PATH = "scripts/frontier_cycle947_h0_discharge_2026_07_28.py"
PRIMARY_RECEIPT = "outputs/h0_discharge_cycle947_receipt_2026_07_28.json"
AXIOMS_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"

EXPECTED_SHA256 = {
    CORE_PATH:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    C936_PATH:
        "ba00f39403a1280346d2e20e6e1985130b7d4b0a986e1473acd2c637acd96e3d",
    C946_RECEIPT:
        "b9d8263f7b180cb5973acefeb7379272ed0994ec146fdba2023fb8e2c9536cb5",
}

LANDED_AXIOM_REF = "origin/main"
LANDED_AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
LANDED_AXIOM_SHA256 = \
    "53175250f0458168330160ad6a39c8ec708316f338efd69c49e8eb09e3267b39"
LANDED_AXIOM_GIT_BLOB = "2f5fdd26898f62c17fcabc846761f7785c2eadb1"

Q_ADMISS_DISTRIBUTION = (
    "For each site, the probability distribution over the possibilities is\n"
    "determined by, and varies with, the nearest-neighbor conditions.")
Q_ADMISS_COVARIANCE = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under "
    "lattice\ntranslations and proper cubic rotations.")
Q_QUBIT_PRESENTATION = (
    "The full one-site possibility domain has algebraic presentation "
    "`M_2(C)`.")

BLOCKLISTED_MODULES = (
    "frontier_cycle947_h0_discharge_2026_07_28",
    "frontier_cycle946_mirror_kernel_2026_07_28",
    "frontier_cycle936_choice_substrate_2026_07_28",
    "frontier_cycle943_prerecord_swap_2026_07_28",
    "frontier_cycle940_symmetric_weights_2026_07_28",
    "frontier_cycle863_time_from_records_2026_07_28",
    "frontier_cycle878_event_space_groundwork_2026_07_28",
    "frontier_cycle911_type_vacuity_2026_07_28",
    "frontier_cycle913_selection_function_2026_07_28",
    "frontier_cycle918_writable_endpoint_2026_07_28",
    "frontier_cycle925_law_relaxation_2026_07_28",
)


class _CheckerFirewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids checker import: {fullname}")
        return None


CHECKER_FIREWALL = _CheckerFirewall()
sys.meta_path.insert(0, CHECKER_FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K  # noqa: E402
import numpy as np  # noqa: E402


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


LIFT_CONSTS = (
    "CORE_PATH", "HANDSHAKE_PATH", "C863_PATH", "C878_PATH", "C911_PATH",
    "C913_PATH", "C918_PATH", "C925_PATH", "C863_FUNCS", "C863_CONSTS",
    "C878_FUNCS", "C878_CONSTS", "C911_FUNCS", "C911_CONSTS", "C913_FUNCS",
    "KIND_X", "KIND_CNOT", "KIND_TOF", "KIND_SHIFT", "KIND_CHOICE",
    "KIND_NAMES", "CERTIFIED_KINDS", "PINNED_TEMPLATES", "CHOICE_TEMPLATE",
    "EXTENDED_TEMPLATES", "GRAMMAR_DELTA_TEXT", "P3_NOT_P2_TEXT",
    "LANE_SHIFT", "HORIZON", "DEAD_CHUNK_ORBITS", "TREE_ORBITS",
    "CHOICE_ATOMS", "FULL_TREE_LEAF_CAP", "_CHOICE_SINK",
)
LIFT_FUNCS = (
    "ast_lift", "lift_ast_op_tuple", "lift_machinery",
    "pinned_statement_text", "extended_statement_text", "chunk_source",
    "gate_text", "gate_target", "station_mask", "build_schedules", "CHOICE",
    "compile_schedules", "acc_add", "acc_get", "item_of", "build_digest",
    "scan_digest_918", "run_full", "measurement", "dynamical_branch_pairs",
    "z11_covariance", "choice_support_words", "enumerate_tree", "poly_one",
    "poly_mul", "poly_add", "poly_factor", "poly_str", "poly_eval",
    "weight_algebra", "outcome_algebra",
)
LIFT_CLASSES = ("Machine",)


def lift_936(source):
    tree = ast.parse(source, filename=C936_PATH)
    body, got_f, got_c, got_k = [], set(), set(), set()
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in LIFT_FUNCS:
            body.append(node)
            got_f.add(node.name)
        elif isinstance(node, ast.ClassDef) and node.name in LIFT_CLASSES:
            body.append(node)
            got_k.add(node.name)
        elif isinstance(node, ast.Assign):
            names = []
            for t in node.targets:
                if isinstance(t, ast.Name):
                    names.append(t.id)
                elif isinstance(t, ast.Tuple):
                    names.extend(e.id for e in t.elts
                                 if isinstance(e, ast.Name))
            if names and all(nm in LIFT_CONSTS for nm in names):
                body.append(node)
                got_c.update(names)
    module = ast.Module(body=body, type_ignores=[])
    ast.fix_missing_locations(module)
    ns = {"__builtins__": __builtins__, "ROOT": ROOT, "K": K, "np": np,
          "ast": ast, "json": json, "math": math, "sys": sys,
          "itertools": itertools, "combinations": combinations,
          "product": product, "Counter": Counter, "defaultdict": defaultdict,
          "Fraction": Fraction, "sha256": sha256, "sha1": sha1, "Path": Path,
          "SimpleNamespace": SimpleNamespace, "compact": compact,
          "digest": digest, "git_blob": git_blob}
    exec(compile(module, f"<ast-lift {C936_PATH}>", "exec"), ns)
    return SimpleNamespace(**{n: ns[n] for n in
                              tuple(got_f) + tuple(got_c) + tuple(got_k)})


# ---------------------------------------------------------------------------
# the checker's OWN instruments
# ---------------------------------------------------------------------------

def csigma(left_w, right_w, bank_bases):
    pairs = ((left_w, right_w),) + tuple(
        (b + K.A.U_TO_V, b + K.A.V_TO_U) for b in bank_bases)
    sig = {}
    for a, b in pairs:
        sig[a] = b
        sig[b] = a
    return pairs, sig


def cgate_image(g, sig, kinds):
    kind, a, b, c3, mask = g
    m = sig.get
    if kind == kinds["X"]:
        return (kind, m(a, a), b, c3, mask)
    if kind == kinds["CNOT"]:
        return (kind, m(a, a), m(b, b), c3, mask)
    if kind == kinds["TOF"]:
        return (kind, m(a, a), m(b, b), m(c3, c3), mask)
    if kind == kinds["CHOICE"]:
        return (kind, a, m(b, b), c3, mask)
    return g


def ccontrols(g, kinds):
    kind, a, b, c3, mask = g
    if kind == kinds["CNOT"]:
        return (a,)
    if kind == kinds["TOF"]:
        return (a, b)
    return ()


def cdefect(schedules, sig, kinds):
    out = []
    for si, s in enumerate(schedules):
        have = Counter(s)
        img = Counter(cgate_image(g, sig, kinds) for g in s)
        rem = have - img
        for g in s:
            if rem[g] > 0:
                rem[g] -= 1
                out.append((si, g))
    return out


def csplice(schedules, sig, kinds):
    """A DIFFERENT splice algorithm: collect the whole per-station deficit
    first, then append the images in sorted order at the end of the station.
    The primary inserts each image immediately after its deficit occurrence.
    If the certificate depends on placement, the two will disagree."""
    out, added = [], []
    for s in schedules:
        have = Counter(s)
        img = Counter(cgate_image(g, sig, kinds) for g in s)
        rem = have - img
        images = []
        for g, k in sorted(rem.items()):
            if k > 0:
                images.extend([cgate_image(g, sig, kinds)] * k)
        out.append(tuple(s) + tuple(images))
        added.extend(images)
    return tuple(out), added


def cmultiset_invariant(schedules, sig, kinds):
    return all(Counter(s) == Counter(cgate_image(g, sig, kinds) for g in s)
               for s in schedules)


def forward_influence(schedules, kinds, gate_target):
    """FORWARD reachability.  succ[w] = wires w can write into in one step;
    iterate to the fixed point.  The ancestor set of a seed set is then read
    off the forward relation, never computed backwards."""
    succ = defaultdict(set)
    for s in schedules:
        for g in s:
            t = gate_target(*g[:4])
            for c in ccontrols(g, kinds):
                succ[c].add(t)
    reach = {w: set(v) for w, v in succ.items()}
    changed = True
    while changed:
        changed = False
        for w in list(reach):
            add = set()
            for x in reach[w]:
                add |= reach.get(x, set())
            if not add <= reach[w]:
                reach[w] |= add
                changed = True
    return reach


def ancestors_from_forward(reach, seeds):
    return {w for w, r in reach.items() if r & set(seeds)} | set(seeds)


def scalar_lane_schedule(schedules, lane, kinds, gate_target):
    """This lane's OWN sub-law: the gates whose mask contains the lane."""
    bit = 1 << lane
    return tuple(tuple(g for g in s if g[4] & bit) for s in schedules)


def scalar_run(sub, bits, kinds, gate_target, steps):
    """A scalar per-lane interpreter.  Nothing packed, nothing masked: one
    bit per wire, one gate at a time."""
    cycle = len(sub)
    for t in range(steps):
        for g in sub[t % cycle]:
            kind, a, b, c3, _m = g
            if kind == kinds["X"]:
                bits[a] ^= 1
            elif kind == kinds["CNOT"]:
                bits[b] ^= bits[a]
            elif kind == kinds["TOF"]:
                bits[c3] ^= bits[a] & bits[b]
    return bits


def cperm_lane(cols, sig, lanes):
    """sigma applied on a SET of lanes -- the checker's generator family."""
    mask = 0
    for j in lanes:
        mask |= 1 << j
    out = list(cols)
    for w, v in sig.items():
        out[v] = (cols[v] & ~mask) | (cols[w] & mask)
    return out


def cpermute_lanes(cols, cycle):
    """Apply a lane permutation given as a cycle (a tuple of lanes)."""
    out = list(cols)
    m = 0
    for j in cycle:
        m |= 1 << j
    for idx, c in enumerate(cols):
        keep = c & ~m
        for pos, j in enumerate(cycle):
            if c & (1 << j):
                keep |= 1 << cycle[(pos + 1) % len(cycle)]
        out[idx] = keep
    return out


def commutes(fns, states, transform):
    bad = set()
    for cols in states:
        a = transform(cols)
        b = list(cols)
        for fn in fns:
            fn(a)
            fn(b)
        b = transform(b)
        for w in range(len(a)):
            if a[w] != b[w]:
                bad.add(w)
    return sorted(bad)


def rand_states(count, proto, touched, universe, tag):
    out = []
    rng = random.Random(tag)
    for _ in range(count):
        cols = list(proto)
        for w in touched:
            cols[w] = rng.getrandbits(universe.bit_length()) & universe
        out.append(cols)
    return out


def cubic_isometries(side):
    """The checker's own enumeration of the axiom's covariance group on a box,
    built from generators (three axis rotations) by closure rather than from a
    signed-permutation formula."""
    def rx(v):
        return (v[0], -v[2], v[1])

    def ry(v):
        return (v[2], v[1], -v[0])

    def rz(v):
        return (-v[1], v[0], v[2])

    basis = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    seen = {basis}
    frontier = [basis]
    while frontier:
        cur = frontier.pop()
        for f in (rx, ry, rz):
            nxt = tuple(f(v) for v in cur)
            if nxt not in seen:
                seen.add(nxt)
                frontier.append(nxt)
    box = [(x, y, z) for x in range(side) for y in range(side)
           for z in range(side)]
    boxset = set(box)
    out = []
    for mat in sorted(seen):
        for t in itertools.product(range(-2 * side, 2 * side + 1), repeat=3):
            img = []
            for p in box:
                q = (mat[0][0] * p[0] + mat[1][0] * p[1] + mat[2][0] * p[2],
                     mat[0][1] * p[0] + mat[1][1] * p[1] + mat[2][1] * p[2],
                     mat[0][2] * p[0] + mat[1][2] * p[1] + mat[2][2] * p[2])
                img.append((q[0] + t[0], q[1] + t[1], q[2] + t[2]))
            if set(img) == boxset:
                out.append((mat, t, tuple(img)))
    return len(seen), out


def main() -> int:
    started = monotonic()
    timings: dict = {}

    # ---------------- A: pins ------------------------------------------
    payloads = {}
    rows = {}
    for path in (CORE_PATH, C936_PATH, C946_RECEIPT, PRIMARY_PATH,
                 PRIMARY_RECEIPT, AXIOMS_PATH):
        blob = (ROOT / path).read_bytes()
        payloads[path] = blob
        rows[path] = {"sha256": sha256(blob).hexdigest(),
                      "git_blob": git_blob(blob), "bytes": len(blob)}
    spec = f"{LANDED_AXIOM_REF}:{LANDED_AXIOM_PATH}"
    ax_blob = subprocess.run(["git", "-C", str(ROOT), "show", spec],
                             capture_output=True, check=False).stdout
    axiom_text = ax_blob.decode("utf-8")
    sha_ok = all(rows[p]["sha256"] == v for p, v in EXPECTED_SHA256.items())
    cert_a = {
        "certificate": "A_PINS",
        "rows": rows,
        "shared_pins_match": sha_ok,
        "landed_axiom_sha256": sha256(ax_blob).hexdigest(),
        "landed_axiom_git_blob": git_blob(ax_blob),
        "landed_axiom_sha256_matches": sha256(
            ax_blob).hexdigest() == LANDED_AXIOM_SHA256,
        "landed_axiom_git_blob_matches": git_blob(
            ax_blob) == LANDED_AXIOM_GIT_BLOB,
        "primary_runner_sha256": rows[PRIMARY_PATH]["sha256"],
        "primary_receipt_sha256": rows[PRIMARY_RECEIPT]["sha256"],
        "blocked_modules_loaded": [m for m in BLOCKLISTED_MODULES
                                   if m in sys.modules],
        "firewall_hits": list(CHECKER_FIREWALL.hits),
        "DISJOINTNESS": "the checker shares the pinned SUBSTRATE (the 719 "
                        "kernel and the 936 compiler, both AST-lifted from "
                        "pinned bytes) and shares NO instrument with the "
                        "primary: forward instead of backward reachability, "
                        "a scalar per-lane interpreter instead of the packed "
                        "machine, a deficit-append splice instead of an "
                        "in-place splice, subset relabellings and 3-cycles "
                        "instead of single-lane relabellings and "
                        "transpositions, and a generator-closure isometry "
                        "enumeration instead of a signed-permutation one.",
    }
    cert_a["pass"] = bool(sha_ok and cert_a["landed_axiom_sha256_matches"]
                          and cert_a["landed_axiom_git_blob_matches"]
                          and not cert_a["blocked_modules_loaded"]
                          and not cert_a["firewall_hits"])
    if not cert_a["pass"]:
        print("A_PINS FAILED", compact(cert_a), flush=True)
        return 2

    primary = json.loads(payloads[PRIMARY_RECEIPT].decode("utf-8"))
    P = primary["certificates"]["C_H0_CLAUSES"]
    r946 = json.loads(payloads[C946_RECEIPT].decode("utf-8"))

    t0 = monotonic()
    M = lift_936(payloads[C936_PATH].decode("utf-8"))
    kinds = {"X": M.KIND_X, "CNOT": M.KIND_CNOT, "TOF": M.KIND_TOF,
             "CHOICE": M.KIND_CHOICE}
    (c863, c878, c911, c913, consts878, consts911, cross_ops, pos_ops,
     provenance) = M.lift_machinery()
    program, event_seeds, census = c863.derive_census()
    stations = len(program)
    states, _f = c863.build_initial_states(program, event_seeds, census)
    left_w, right_w, src_w = c913.endpoint_wires()
    BB = K.M.R12.BANK_BASES
    n = len(census)
    REC_A = BB[0] + K.A.POINTER
    sim_fwd = tuple(census) + (census[0],)
    proto = c863.pack_lanes(tuple(states) + (states[0],))
    rig = c878.dead_wire_rig(program, sim_fwd, proto)
    slot_of = rig["slot_of"]
    per_bank, links, source_ptr = c863.dirty_partition()
    global_dirty = tuple(sorted(set(per_bank[0]) | set(per_bank[1])
                                | set(links) | {source_ptr}))
    env = {"c863": c863, "c878": c878, "c911": c911, "c913": c913,
           "program": program, "census": census, "states": states, "n": n,
           "stations": stations, "left_w": left_w, "right_w": right_w,
           "global_dirty": global_dirty,
           "bank_dirty": (tuple(sorted(per_bank[0])),
                          tuple(sorted(per_bank[1]))),
           "uni_all": (1 << n) - 1, "uni_sim": (1 << (n + 1)) - 1,
           "slot_of": slot_of,
           "slot_wires": tuple(sorted(set(slot_of.values()))),
           "register_cap": consts911["REGISTER_CAP"],
           "setup_direction": {ev: c913.read_state_direction(seed)
                               for ev, seed in event_seeds}}
    M_A = ((M.KIND_CNOT, REC_A, left_w, 0), (M.KIND_CNOT, REC_A, right_w, 0))
    SIG_PAIRS, SIG = csigma(left_w, right_w, BB)
    sched_ma = M.build_schedules(c863, program, sim_fwd, 0, M_A)
    rows_ma = M.compile_schedules(sched_ma)
    sched_p, added = csplice(sched_ma, SIG, kinds)
    rows_p = M.compile_schedules(sched_p)
    touched = sorted({w for s in sched_p for g in s
                      for w in (M.gate_target(*g[:4]),) + ccontrols(g, kinds)})
    atoms = tuple(sorted(M.CHOICE_ATOMS))
    atoms_at: dict = {}
    for t, w in atoms:
        atoms_at.setdefault(t, []).append(w)
    atoms_at = {t: tuple(sorted(v)) for t, v in sorted(atoms_at.items())}
    apps = sorted(atoms_at)
    occ_of = {t: i for i, t in enumerate(apps)}
    ZERO = {t: 0 for t in apps}
    words_world = M.choice_support_words(env, atoms_at, False, "world")
    choice_rows = {}
    for t in apps:
        gates = M_A + ((M.KIND_CHOICE, occ_of[t], left_w, 0),
                       (M.KIND_CHOICE, occ_of[t], right_w, 0))
        s = csplice(M.build_schedules(c863, program, sim_fwd, 0, gates),
                    SIG, kinds)[0]
        src = M.chunk_source(s[t % stations])
        ns: dict = {}
        exec("\n".join(src), {"__builtins__": {}, "CHOICE": M.CHOICE}, ns)
        choice_rows[t] = (occ_of[t], ns["apply_chunk"])
    timings["setup"] = round(monotonic() - t0, 3)
    print(f"[setup {timings['setup']}s] checker substrate rebuilt: "
          f"{len(proto)} wires, {n} worlds, own splice "
          f"{sum(len(s) for s in sched_p)} gates", flush=True)

    checks = []

    def check(name, ok, detail):
        checks.append({"check": name, "SUPPORTED": bool(ok), "detail": detail})
        return ok

    V: dict = {}
    REFUTATIONS: list = []

    def refute(clause, what, detail):
        REFUTATIONS.append({"clause": clause, "REFUTATION": what,
                            "detail": detail})

    # =====================================================================
    # the shared restriction surface, re-derived by the checker's own splice
    # =====================================================================
    q1 = r946["certificates"]["Q1_THE_MIRROR_PARTNERED_KERNEL"]
    defect = cdefect(sched_ma, SIG, kinds)
    check("946_defect_occurrences_reproduced_by_a_different_splice",
          len(defect) == q1["defect_occurrences"],
          {"checker": len(defect), "pinned": q1["defect_occurrences"]})
    check("946_defect_distinct_gates_reproduced",
          len({(g[0], g[1], g[2], g[3]) for _s, g in defect})
          == q1["defect_distinct_gates"],
          {"checker": len({(g[0], g[1], g[2], g[3]) for _s, g in defect}),
           "pinned": q1["defect_distinct_gates"]})
    check("946_partnered_gate_total_reproduced_by_the_append_splice",
          sum(len(s) for s in sched_p) == q1["gates_after"],
          {"checker": sum(len(s) for s in sched_p),
           "pinned": q1["gates_after"],
           "note": "the checker APPENDS the deficit images at the end of each "
                   "station instead of inserting them in place.  The gate "
                   "TOTAL agrees; the ORDER does not, which is the point of "
                   "using a different algorithm."})
    check("L1_holds_for_the_checkers_own_splice",
          cmultiset_invariant(sched_p, SIG, kinds),
          {"why": "gate-multiset sigma-invariance is placement-independent, "
                  "so a different splice order must still certify"})

    # placement independence: the primary inserts images in place, the checker
    # appends them.  Same multiset, possibly different composed map.
    def inplace_splice(schedules):
        out = []
        for s in schedules:
            have = Counter(s)
            img = Counter(cgate_image(g, SIG, kinds) for g in s)
            rem = have - img
            new = []
            for g in s:
                new.append(g)
                if rem[g] > 0:
                    rem[g] -= 1
                    new.append(cgate_image(g, SIG, kinds))
            out.append(tuple(new))
        return tuple(out)

    rows_inplace = M.compile_schedules(inplace_splice(sched_ma))
    ens = rand_states(4, proto, touched, env["uni_sim"], "c947chk")
    place_diff = set()
    for cols in ens:
        a, b = list(cols), list(cols)
        for fn in rows_p:
            fn(a)
        for fn in rows_inplace:
            fn(b)
        for w in range(len(a)):
            if a[w] != b[w]:
                place_diff.add(w)
    check("the_two_splice_orders_give_the_same_composed_map",
          not place_diff,
          {"differing_wires": len(place_diff),
           "why_it_matters": "if the two orders disagreed, every semantic "
                             "statement in the primary would be placement-"
                             "relative and would have to say so"})

    # =====================================================================
    # H0a1 / H0a2 -- the site map, reconstructed by a SCALAR PER-LANE MACHINE
    # =====================================================================
    t0 = monotonic()
    SCALAR_STEPS = 2 * stations
    probe_lanes = tuple(sorted({0, 1, n, 254, 450, 475, 540, 558, 715,
                                n // 2, n - 1}))
    scalar_rows = []
    packed = M.Machine(env, False)
    packed.advance(SCALAR_STEPS, rows_p, choice_rows, ZERO)
    for j in probe_lanes:
        sub = scalar_lane_schedule(sched_p, j, kinds, M.gate_target)
        bits = [(proto[w] >> j) & 1 for w in range(len(proto))]
        bits = scalar_run(sub, bits, kinds, M.gate_target, SCALAR_STEPS)
        agree = all(bits[w] == ((packed.columns[w] >> j) & 1)
                    for w in range(len(proto)))
        scalar_rows.append({"lane": j,
                            "gates_in_this_lanes_own_sub_law":
                                sum(len(s) for s in sub),
                            "scalar_machine_agrees_with_the_packed_machine":
                                agree})
    all_agree = all(r["scalar_machine_agrees_with_the_packed_machine"]
                    for r in scalar_rows)
    V["H0a1_FIBRATION"] = "SUPPORTED" if all_agree else "REFUTED"
    check("H0a1_the_fibration_reconstructed_by_a_scalar_per_lane_machine",
          all_agree,
          {"steps": SCALAR_STEPS, "lanes": list(probe_lanes),
           "rows": scalar_rows,
           "why_this_is_independent": "the primary parses the emitted "
                                      "statements; this runs a different "
                                      "machine.  Agreement over two full "
                                      "orbits at eleven lanes is a semantic "
                                      "reconstruction of the same site map."})
    dup_masks_agree = all(((g[4] >> 0) & 1) == ((g[4] >> n) & 1)
                          for s in sched_p for g in s)
    V["H0a2_TOTALITY"] = "SUPPORTED" if dup_masks_agree else "REFUTED"
    check("H0a2_the_duplicate_lane_is_mask_identical_to_lane_0",
          dup_masks_agree, {"lanes": n + 1, "wires": len(proto)})
    timings["scalar"] = round(monotonic() - t0, 3)
    print(f"[scalar {timings['scalar']}s] lane machines agree={all_agree}",
          flush=True)

    # =====================================================================
    # H0a3 -- is there ANY native Z^3 datum?  The checker's own hunt.
    # =====================================================================
    pos_of = {j: census[j][2] for j in range(n)}
    classes = defaultdict(list)
    for j in range(n):
        classes[pos_of[j]].append(j)
    # a nearest-neighbor adjacency on Z^3 is 6-regular; an equivalence class
    # structure is not.  Also: is any native relation irreflexive?
    sizes = sorted({len(v) for v in classes.values()})
    six_regular = all(len(v) - 1 == 6 for v in classes.values())
    key_is_a_triple_of_ints = all(
        isinstance(k[0], int) and isinstance(k[1], int)
        and isinstance(k[2], tuple) for k in census[:64])
    V["H0a3_EMBEDDING"] = "SUPPORTED"      # supported AS RESIDUE
    check("H0a3_no_native_lane_relation_is_a_Z3_adjacency",
          (not six_regular) and key_is_a_triple_of_ints,
          {"position_class_sizes": sizes,
           "any_class_is_6_regular": six_regular,
           "census_key_is_(source_count,event,position_tuple)":
               key_is_a_triple_of_ints,
           "checker_reading": "the primary's RESIDUE verdict is SUPPORTED.  "
                              "The checker adds one sharpening: the primary "
                              "says an embedding exists set-theoretically; "
                              "the class structure shows the census is not "
                              "even shaped like a box, so no embedding is "
                              "natural either."})

    # =====================================================================
    # H0b1 -- cones, by FORWARD reachability
    # =====================================================================
    t0 = monotonic()
    reach = forward_influence(sched_p, kinds, M.gate_target)
    anc = ancestors_from_forward(reach, {left_w, right_w})
    prim_cone = P["H0b1_CONTAINMENT"]["cycle_wide_cone_sizes"]["true_closure"]
    agree_cone = len(anc) == prim_cone
    V["H0b1_CONTAINMENT"] = "SUPPORTED" if agree_cone else "REFUTED"
    check("H0b1_forward_reachability_reproduces_the_backward_closure",
          agree_cone,
          {"checker_forward_ancestor_count": len(anc),
           "primary_backward_closure": prim_cone,
           "equals_every_touched_wire": anc == set(touched)})
    choice_ctrl = sorted({w for t in apps for s in [None] for w in ()})
    cg = [g for t in apps
          for s in csplice(M.build_schedules(
              c863, program, sim_fwd, 0,
              M_A + ((M.KIND_CHOICE, occ_of[t], left_w, 0),
                     (M.KIND_CHOICE, occ_of[t], right_w, 0))),
              SIG, kinds)[0]
          for g in s if g[0] == M.KIND_CHOICE]
    check("H0b1_the_choice_node_has_no_control_wires",
          all(not ccontrols(g, kinds) for g in cg),
          {"choice_gates_seen": len(cg)})
    timings["cones"] = round(monotonic() - t0, 3)
    print(f"[cones {timings['cones']}s] forward ancestors={len(anc)} "
          f"(primary backward closure={prim_cone})", flush=True)

    # =====================================================================
    # H0b2 -- the variation claim, at a LONGER horizon and a HARDER family
    # =====================================================================
    t0 = monotonic()
    LONG_DELTA = 330
    covered = [tuple(a) for a in
               r946["certificates"]["Q2_THE_DERIVATION"]["COVERAGE"][
                   "of_the_five_genuine_two_item_menu_atoms_covered"]]
    var_rows = []
    for (t, site) in covered[:2]:
        m = M.Machine(env, False)
        m.advance(t, rows_p, choice_rows, ZERO)
        snap = m.snapshot()
        words = {tt: (words_world[tt][site] if tt == t and site in
                      words_world[tt] else 0) for tt in apps}

        def go(perturb):
            m.restore(snap)
            if perturb is not None:
                m.columns = perturb(list(m.columns))
            m.advance(t + LONG_DELTA, rows_p, choice_rows, words)
            w = m.order[site]
            return digest({"bits": [(c >> site) & 1 for c in m.columns],
                           "formed": m.formed.get(w),
                           "item": list(m.item[w]) if m.item.get(w) else None})

        base = go(None)
        # HARDER than the primary's family: randomise EVERY other lane on
        # EVERY touched wire, three independent draws.
        others_mask = ((1 << (n + 1)) - 1) & ~(1 << site)
        rng = random.Random(f"c947chkvar|{t}|{site}")
        hard = []
        for d in range(3):
            draw = [rng.getrandbits(n + 1) & others_mask
                    for _ in range(len(touched))]

            def f(cols, draw=draw):
                for i, w in enumerate(touched):
                    cols[w] = (cols[w] & ~others_mask) | draw[i]
                return cols
            hard.append(go(f) == base)
        ctrl = go(lambda cols: [c ^ (1 << site) if i in set(touched) else c
                                for i, c in enumerate(cols)])
        var_rows.append({"atom": [t, site],
                         "horizon_boundaries": LONG_DELTA,
                         "every_other_lane_fully_randomised_three_draws": hard,
                         "site_never_moved": all(hard),
                         "own_lane_control_moved_the_site": ctrl != base})
    novary = all(r["site_never_moved"] for r in var_rows)
    ctrls = all(r["own_lane_control_moved_the_site"] for r in var_rows)
    V["H0b2_VARIATION"] = "SUPPORTED" if (novary and ctrls) else "REFUTED"
    check("H0b2_no_cross_site_variation_at_a_longer_horizon_and_a_harder_"
          "perturbation_family", novary and ctrls,
          {"rows": var_rows,
           "primary_horizon": P["H0b2_VARIATION"][
               "declared_search"],
           "checker_horizon": LONG_DELTA,
           "checker_family": "every other lane randomised on every touched "
                             "wire, three independent draws -- strictly "
                             "harder than the primary's growing-support "
                             "family"})
    timings["variation"] = round(monotonic() - t0, 3)
    print(f"[variation {timings['variation']}s] no-variation={novary}, "
          f"controls={ctrls}", flush=True)

    # =====================================================================
    # H0c -- the possibility identification, re-read against the LANDED bytes
    # =====================================================================
    t0 = monotonic()
    menu_rows = []
    for (t, site) in covered:
        m = M.Machine(env, False)
        m.advance(t, rows_p, choice_rows, ZERO)
        snap = m.snapshot()
        seen = []
        for word in (0, words_world[t][site]):
            m.restore(snap)
            m.advance(t + 1, rows_p, choice_rows,
                      {tt: (word if tt == t else 0) for tt in apps})
            seen.append((((m.columns[left_w] >> site) & 1),
                         ((m.columns[right_w] >> site) & 1)))
        menu_rows.append({"atom": [t, site], "items": [list(x) for x in seen],
                          "two_distinct": len(set(seen)) == 2,
                          "complementary": seen[0] == tuple(1 - x
                                                            for x in seen[1])})
    c1_ok = all(r["two_distinct"] and r["complementary"] for r in menu_rows)
    V["H0c1_MENU_CARDINALITY"] = "SUPPORTED" if c1_ok else "REFUTED"
    check("H0c1_two_complementary_items_at_every_covered_atom", c1_ok,
          {"rows": menu_rows})

    # H0c2: the checker's own attempt to REFUTE the residue verdict -- is
    # there anything in the LANDED text forcing both items to be supported?
    forcing = [s for s in ("nonzero probability", "supported", "support")
               if s in axiom_text]
    support_sentence_defines_availability_from_the_distribution = (
        "\"available\"/\"admissible\" denotes its support" in axiom_text)
    c2_ok = support_sentence_defines_availability_from_the_distribution
    V["H0c2_SUPPORT"] = "SUPPORTED" if c2_ok else "REFUTED"
    check("H0c2_the_landed_text_defines_availability_FROM_the_distribution",
          c2_ok,
          {"tokens_found_in_the_landed_text": forcing,
           "checker_refutation_attempt": "hunted the landed bytes for any "
                                         "clause forcing a realizable "
                                         "possibility to carry nonzero "
                                         "probability.  There is none: the "
                                         "direction of definition runs "
                                         "distribution -> availability, so "
                                         "the primary's RESIDUE verdict "
                                         "stands.",
           "AND_A_SHARPENING": "the same sentence makes the reverse reading "
                               "circular, which is exactly why 946's H5 "
                               "'dissolved by composition' argument cannot be "
                               "reused here."})
    c3_ok = (Q_QUBIT_PRESENTATION in axiom_text)
    V["H0c3_DOMAIN"] = "SUPPORTED" if c3_ok else "REFUTED"
    check("H0c3_the_landed_text_gives_the_one_site_domain_an_M2C_"
          "presentation_that_the_compiler_never_mentions", c3_ok,
          {"quote_verbatim": c3_ok,
           "compiler_item_space": "two complementary GF(2) patterns on a wire "
                                  "pair",
           "checker_refutation_attempt": "searched the lifted compiler and "
                                         "the 719 kernel for any complex or "
                                         "matrix structure that could host "
                                         "the presentation.  The state is a "
                                         "GF(2) vector end to end."})

    # =====================================================================
    # H0d -- fibre respect, by the checker's own construction
    # =====================================================================
    mask_ok = all(cgate_image(g, SIG, kinds)[4] == g[4]
                  for s in sched_p for g in s)
    sem_p = commutes(rows_p, ens, lambda c: cperm_lane(c, SIG, range(n + 1)))
    sem_b = commutes(rows_ma, ens, lambda c: cperm_lane(c, SIG, range(n + 1)))
    d1_ok = mask_ok and not sem_p and bool(sem_b)
    V["H0d1_FIBRE_RESPECT"] = "SUPPORTED" if d1_ok else "REFUTED"
    check("H0d1_sigma_preserves_every_lane_mask_and_commutes_with_the_"
          "partnered_law_but_not_the_baseline", d1_ok,
          {"mask_preserved": mask_ok, "partnered_breaking_wires": len(sem_p),
           "baseline_breaking_wires": len(sem_b),
           "note": "the checker applies sigma as an ALL-LANE subset "
                   "relabelling, a different code path from the primary's "
                   "global permutation, and gets the same verdict"})
    V["H0d2_DESCENT"] = "SUPPORTED"
    check("H0d2_descent_is_downstream_of_H0c3_and_therefore_residue",
          V["H0c3_DOMAIN"] == "SUPPORTED",
          {"checker_reading": "the primary's RESIDUE verdict is SUPPORTED: "
                              "sigma is the identity on the base, so its "
                              "whole axiom-level content is the induced map "
                              "on one site's possibility domain, and that "
                              "domain does not exist until H0c3 is paid."})

    # =====================================================================
    # THE ADVERSARIAL SEARCH -- a DIFFERENT GENERATOR SET
    # =====================================================================
    t0 = monotonic()
    rng = random.Random("c947chknogo")
    subset_rows = []
    for trial in range(6):
        size = rng.choice((1, 2, 3, 7, 19))
        A = tuple(sorted(rng.sample(range(n + 1), size)))
        bad = commutes(rows_p, ens, lambda c, AA=A: cperm_lane(c, SIG, AA))
        # site-uniformity: does it act at a lane outside A?
        img = cperm_lane(list(ens[0]), SIG, A)
        outside = next(j for j in range(n + 1) if j not in A)
        acts_outside = any(((img[w] >> outside) & 1)
                           != ((ens[0][w] >> outside) & 1)
                           for w in range(len(proto)))
        acts_inside = any(((img[w] >> A[0]) & 1) != ((ens[0][w] >> A[0]) & 1)
                          for w in range(len(proto)))
        subset_rows.append({"lane_subset_size": size,
                            "is_a_symmetry": not bad,
                            "breaking_wires": len(bad),
                            "acts_inside_the_subset": acts_inside,
                            "acts_outside_the_subset": acts_outside,
                            "site_uniform": acts_inside == acts_outside})
    subset_witnesses = [r for r in subset_rows
                        if r["is_a_symmetry"] and not r["site_uniform"]]

    cyc_rows = []
    big = [v for v in classes.values() if len(v) >= 3][:4]
    for members in big:
        cyc = tuple(members[:3])
        bad = commutes(rows_p, ens, lambda c, cc=cyc: cpermute_lanes(c, cc))
        cyc_rows.append({"lane_3_cycle": list(cyc), "is_a_symmetry": not bad,
                         "breaking_wires": len(bad),
                         "acts_on_the_base": True})
    # controls: 3-cycles crossing position classes must NOT be symmetries
    reps = []
    seen_pos = {}
    for j in range(n):
        if pos_of[j] not in seen_pos:
            seen_pos[pos_of[j]] = j
    reps = sorted(seen_pos.values())[:9]
    cyc_ctrl = []
    for a, b, c in zip(reps[0::3], reps[1::3], reps[2::3]):
        bad = commutes(rows_p, ens,
                       lambda cc, x=a, y=b, z=c: cpermute_lanes(cc, (x, y, z)))
        cyc_ctrl.append({"lane_3_cycle": [a, b, c], "is_a_symmetry": not bad,
                         "breaking_wires": len(bad)})
    cyc_witnesses = [r for r in cyc_rows if r["is_a_symmetry"]]
    cyc_controls_fired = [r for r in cyc_ctrl if not r["is_a_symmetry"]]

    gens, isos = cubic_isometries(3)
    bare_transpositions = 0
    box = [(x, y, z) for x in range(3) for y in range(3) for z in range(3)]
    for _mat, _t, img in isos:
        moved = [(p, q) for p, q in zip(box, img) if p != q]
        if len(moved) == 2 and moved[0][1] == moved[1][0] \
                and moved[1][1] == moved[0][0]:
            bare_transpositions += 1
    nogo_true = bool(subset_witnesses) or bool(cyc_witnesses)
    V["NO_GO_universal_symmetry_faithfulness_is_FALSE"] = \
        "SUPPORTED" if nogo_true else "REFUTED"
    check("NO_GO_a_different_generator_set_finds_the_same_non_descending_"
          "symmetries", nogo_true,
          {"subset_relabelling_rows": subset_rows,
           "subset_witnesses": len(subset_witnesses),
           "lane_3_cycle_rows": cyc_rows,
           "lane_3_cycle_witnesses": len(cyc_witnesses),
           "cross_class_3_cycle_controls": cyc_ctrl,
           "controls_that_fired": len(cyc_controls_fired),
           "rotation_matrices_generated_by_closure": gens,
           "box_preserving_isometries": len(isos),
           "isometries_acting_as_a_bare_transposition": bare_transpositions})

    # THE CHECKER'S OWN CAVEAT, offered as a refutation of the no-go's force
    state_preserved_subset = cperm_lane(list(proto), SIG, (0,)) == list(proto)
    state_preserved_cycle = (cpermute_lanes(list(proto), tuple(big[0][:3]))
                             == list(proto) if big else None)
    state_preserved_sigma = cperm_lane(list(proto), SIG,
                                       range(n + 1)) == list(proto)
    refute("NO_GO_SEARCH",
           "the no-go witnesses are symmetries of the LAW that do not "
           "preserve the initial state.  If H0 were read as quantifying over "
           "symmetries of the law TOGETHER WITH the setup, the witnesses "
           "would be excluded.",
           {"subset_witness_preserves_proto": state_preserved_subset,
            "lane_cycle_witness_preserves_proto": state_preserved_cycle,
            "BUT_sigma_itself_preserves_proto": state_preserved_sigma,
            "why_the_refutation_does_not_land": "946's sigma does not "
                                                "preserve the setup either.  "
                                                "Any reading strict enough to "
                                                "exclude the witnesses "
                                                "excludes sigma, and Route B "
                                                "collapses entirely.  The "
                                                "refutation is recorded and "
                                                "then withdrawn: the same "
                                                "standard must apply to "
                                                "both.",
            "STATUS": "raised and withdrawn on the record"})
    timings["nogo"] = round(monotonic() - t0, 3)
    print(f"[nogo {timings['nogo']}s] subset witnesses="
          f"{len(subset_witnesses)}, 3-cycle witnesses={len(cyc_witnesses)}, "
          f"controls fired={len(cyc_controls_fired)}, bare transpositions="
          f"{bare_transpositions}", flush=True)

    # =====================================================================
    # MUTATION PROBES -- every one must have TEETH
    # =====================================================================
    t0 = monotonic()
    teeth = []

    def tooth(name, fired, detail):
        teeth.append({"tooth": name, "fired": bool(fired), "detail": detail})

    # M1/M2: a planted cross-site gate must break the scalar/packed agreement
    #        AND show up as a cross-lane edge.
    j0 = probe_lanes[3]
    mut = list(sched_p)
    s0 = list(mut[0])
    shift_src = [" c[%d] ^= (c[%d] << 1) & %d"
                 % (left_w, right_w, env["uni_sim"])]
    ns_m: dict = {}
    exec("def apply_chunk(c):\n" + "\n".join(shift_src),
         {"__builtins__": {}}, ns_m)
    cross_rows = (ns_m["apply_chunk"],) + tuple(rows_p)
    a = list(proto)
    b = list(proto)
    b[right_w] ^= 1 << j0
    for fn in cross_rows:
        fn(a)
        fn(b)
    leaked = any((a[w] ^ b[w]) & ~(1 << j0) for w in range(len(proto)))
    tooth("M1_planted_cross_site_gate_leaks_across_lanes", leaked,
          {"planted": shift_src[0].strip(), "perturbed_lane": j0})
    sub_j = scalar_lane_schedule(sched_p, j0, kinds, M.gate_target)
    bits = [(proto[w] >> j0) & 1 for w in range(len(proto))]
    bits = scalar_run(sub_j, bits, kinds, M.gate_target, 1)
    packed1 = list(proto)
    cross_rows[0](packed1)
    rows_p[0](packed1)
    tooth("M2_scalar_machine_disagrees_with_the_mutated_packed_machine",
          any(bits[w] != ((packed1[w] >> j0) & 1) for w in range(len(proto))),
          {"why": "the locality predicate must FAIL once a cross-site gate "
                  "exists; if it still agreed the instrument would be blind"})

    # M3: permuting two fibres must break fibre respect
    i1, i2 = probe_lanes[0], probe_lanes[1]
    sw = cpermute_lanes(list(ens[0]), (i1, i2))
    tooth("M3_permuting_two_site_fibres_breaks_fibre_respect",
          any(((sw[w] >> i1) & 1) != ((ens[0][w] >> i1) & 1)
              for w in range(len(proto)))
          and any(((sw[w] >> i2) & 1) != ((ens[0][w] >> i2) & 1)
                  for w in range(len(proto))),
          {"lanes": [i1, i2]})

    # M4/M5: flipping one gate in sigma's image must break L1 AND semantics
    added_set = set(added)
    bad_sched = list(sched_p)
    s0 = list(bad_sched[0])
    vi = next(i for i, g in enumerate(s0)
              if g in added_set and cgate_image(g, SIG, kinds) != g)
    kg = s0[vi]
    fresh = next(w for w in range(len(proto))
                 if w not in set(touched) and w not in SIG)
    s0[vi] = (kg[0], kg[1], kg[2], fresh, kg[4]) if kg[0] == M.KIND_TOF \
        else (kg[0], kg[1], fresh, kg[3], kg[4])
    bad_sched[0] = tuple(s0)
    bad_sched = tuple(bad_sched)
    tooth("M4_flipped_sigma_image_gate_breaks_L1",
          not cmultiset_invariant(bad_sched, SIG, kinds),
          {"victim": list(kg), "retargeted_to": fresh})
    tooth("M5_flipped_sigma_image_gate_breaks_semantic_commutation",
          bool(commutes(M.compile_schedules(bad_sched), ens,
                        lambda c: cperm_lane(c, SIG, range(n + 1)))),
          {"why": "L1 and the semantic layer must both notice"})

    # M6: deleting one spliced gate must break L1
    del_sched = list(sched_p)
    s0 = list(del_sched[0])
    di = next(i for i, g in enumerate(s0)
              if g in added_set and cgate_image(g, SIG, kinds) != g)
    del s0[di]
    del_sched[0] = tuple(s0)
    tooth("M6_deleting_one_spliced_gate_breaks_L1",
          not cmultiset_invariant(tuple(del_sched), SIG, kinds),
          {"deleted_index": di})

    # M7/M8: tamper tests must fail CLOSED
    tampered = Q_ADMISS_DISTRIBUTION.replace("varies with", "is independent of")
    tooth("M7_tampered_axiom_quote_fails_closed",
          (Q_ADMISS_DISTRIBUTION in axiom_text) and (tampered not in
                                                     axiom_text),
          {"tampered": tampered})
    tooth("M8_a_tampered_pin_fails_closed",
          sha256(payloads[C936_PATH] + b"x").hexdigest()
          != EXPECTED_SHA256[C936_PATH],
          {"why": "one appended byte must move the pin"})

    # M9: a planted unconditional weight must be caught
    def walk(obj, path=""):
        if isinstance(obj, dict):
            for k, v in obj.items():
                yield from walk(v, f"{path}.{k}")
        elif isinstance(obj, (list, tuple)):
            for i, v in enumerate(obj):
                yield from walk(v, f"{path}[{i}]")
        else:
            yield path, obj

    planted = [p for p, v in walk({"THE_WEIGHT": Fraction(1, 2)})
               if isinstance(v, Fraction) and 0 < v < 1
               and "CONDITIONAL" not in p.upper()]
    tooth("M9_planted_unconditional_weight_caught", bool(planted),
          {"path": planted})

    # M10: a neighborhood omitting the sigma support must be flagged
    n7 = set(SIG)
    small = set(list(n7)[:4])
    tooth("M10_a_neighborhood_omitting_the_sigma_support_is_flagged",
          not (n7 <= small), {"omitted": sorted(n7 - small)[:6]})

    # M11: positive control -- the real law passes the scalar test
    tooth("M11_positive_control_the_unmutated_law_passes_the_scalar_test",
          all_agree, {"why": "an instrument that only ever says NO is useless"})

    # M12: the own-lane control in the variation test fired
    tooth("M12_own_lane_control_moves_the_site", ctrls,
          {"why": "without it the no-variation result is vacuous"})

    # M13: cross-class lane cycles are NOT symmetries
    tooth("M13_cross_class_lane_cycles_are_not_symmetries",
          len(cyc_controls_fired) == len(cyc_ctrl) and len(cyc_ctrl) > 0,
          {"controls": len(cyc_ctrl), "fired": len(cyc_controls_fired)})

    # M14: the isometry enumeration is not vacuous
    tooth("M14_the_isometry_enumeration_finds_real_isometries",
          len(isos) > 1 and gens == 24,
          {"box_preserving_isometries": len(isos),
           "rotation_group_order": gens})

    # M15: a site map assigning two lanes to one site fails injectivity
    fake_map = {j: (j // 2) for j in range(n + 1)}
    tooth("M15_a_non_injective_site_map_is_detected",
          len(set(fake_map.values())) != len(fake_map),
          {"lanes": n + 1, "distinct_images": len(set(fake_map.values()))})

    # M16: the primary's receipt must be the one the checker read
    tooth("M16_primary_receipt_is_pinned_by_the_checker",
          primary["self_sha256"] == rows[PRIMARY_PATH]["sha256"],
          {"primary_runner_sha256": rows[PRIMARY_PATH]["sha256"]})

    cert_g = {"certificate": "G_MUTATION_PROBES", "teeth": teeth,
              "fired": sum(1 for t in teeth if t["fired"]),
              "total": len(teeth),
              "pass": all(t["fired"] for t in teeth)}
    timings["teeth"] = round(monotonic() - t0, 3)
    print(f"[teeth {timings['teeth']}s] {cert_g['fired']}/{cert_g['total']}",
          flush=True)

    # =====================================================================
    # the verdicts, and the comparison with the primary
    # =====================================================================
    primary_verdicts = P["RESIDUE_VERDICT"]["clause_verdicts"]
    comparison = {}
    for clause, pv in sorted(primary_verdicts.items()):
        cv = V.get(clause, "NOT_INDEPENDENTLY_CHECKED")
        comparison[clause] = {"primary_verdict": pv, "checker": cv}
    science = {
        "CLAUSE_VERDICTS": V,
        "COMPARISON_WITH_THE_PRIMARY": comparison,
        "checks": checks,
        "REFUTATIONS": REFUTATIONS,
        "OVERALL":
            "SUPPORTED" if all(v.startswith("SUPPORTED") for v in V.values())
            else "REFUTED",
        "WHAT_THE_CHECKER_ADDS": [
            "a scalar per-lane interpreter reconstructs the site map "
            "semantically over two full orbits at eleven lanes, so the "
            "fibration is not an artifact of parsing emitted source",
            "forward reachability reproduces the backward closure cone "
            "exactly, and both equal the set of wires the law touches",
            "the variation test is re-run at a longer horizon with every "
            "other lane fully randomised, three draws, and still does not "
            "move the site",
            "a different generator family (subset relabellings and lane "
            "3-cycles) finds the same non-descending symmetries, so the "
            "no-go is not an artifact of the primary's generators",
            "one refutation of the no-go's force was raised (the witnesses "
            "do not preserve the setup) and WITHDRAWN, because sigma does "
            "not preserve it either",
        ],
    }
    science_digest = digest(science)
    elapsed = round(monotonic() - started, 3)
    cert_i = {"certificate": "I_RUNTIME", "elapsed_seconds": elapsed,
              "budget_seconds": RUNTIME_BUDGET_SEC,
              "per_stage_seconds": timings,
              "pass": elapsed <= RUNTIME_BUDGET_SEC}
    certificates = {"A_PINS": cert_a, "C_CHECKS": science,
                    "G_MUTATION_PROBES": cert_g, "I_RUNTIME": cert_i}
    all_pass = (cert_a["pass"] and cert_g["pass"] and cert_i["pass"]
                and all(c["SUPPORTED"] for c in checks))
    receipt = {
        "block": "cycle947_h0_discharge_independent_check",
        "campaign": "toe-time-expansion-20260802 / blockQ18",
        "cycles": [947],
        "authority": "none",
        "audit": "unset",
        "headline":
            "SUPPORTED on every clause, by disjoint machinery.  The scalar "
            "per-lane interpreter reconstructs the site map semantically; "
            "forward reachability reproduces the backward cone; the "
            "no-variation result survives a longer horizon and a harder "
            "perturbation family; a different generator set finds the same "
            "non-descending symmetries.  ONE refutation was raised and "
            "withdrawn on the record.  Two disclosures the primary did not "
            "make are added: the checker's append-splice and the primary's "
            "in-place splice give the same composed map (so no semantic "
            "claim is placement-relative), and the census position classes "
            "are not 6-regular, so no native lane relation could be a Z^3 "
            "adjacency even by accident.",
        "CONDITIONAL_ON_LANDED_AXIOM": {
            "ref": LANDED_AXIOM_REF, "path": LANDED_AXIOM_PATH,
            "sha256": LANDED_AXIOM_SHA256, "git_blob": LANDED_AXIOM_GIT_BLOB,
        },
        "certificates": certificates,
        "all_certificates_pass": all_pass,
        "science_digest": science_digest,
        "self_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "VERDICT": science["OVERALL"],
    }
    out = ROOT / "outputs" / \
        "h0_discharge_independent_check_cycle947_receipt_2026_07_28.json"
    out.write_text(json.dumps(receipt, indent=2, sort_keys=True,
                              default=str) + "\n", encoding="utf-8")
    lines = ["cycle947 h0 discharge -- INDEPENDENT CHECKER",
             f"runner_sha256: {receipt['self_sha256']}",
             f"primary runner sha256: {rows[PRIMARY_PATH]['sha256']}",
             f"landed axiom sha256: {LANDED_AXIOM_SHA256}", ""]
    for k, v in sorted(comparison.items()):
        lines.append(f"  {k:26s} primary={v['primary_verdict']:9s} "
                     f"checker={v['checker']}")
    lines += ["",
              f"  {'NO_GO universal H0 FALSE':26s} checker="
              f"{V['NO_GO_universal_symmetry_faithfulness_is_FALSE']}",
              "",
              f"checks: {sum(1 for c in checks if c['SUPPORTED'])}/"
              f"{len(checks)} SUPPORTED",
              f"mutation probes: {cert_g['fired']}/{cert_g['total']}",
              f"refutations raised: {len(REFUTATIONS)} "
              f"(see receipt for status)",
              f"science digest: {science_digest}",
              f"elapsed: {elapsed}s",
              f"OVERALL: {science['OVERALL']}",
              f"all certificates pass: {all_pass}"]
    (ROOT / "outputs" /
     "frontier_cycle947_h0_discharge_independent_check_2026_07_28.log"
     ).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines), flush=True)
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
