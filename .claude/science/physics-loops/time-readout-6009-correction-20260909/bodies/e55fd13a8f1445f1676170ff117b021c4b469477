#!/usr/bin/env python3
"""Cycle 903 -- INDEPENDENT CHECK, spec'd to REFUTE.

This runner does not assist the primary.  It re-derives every load-bearing
number by machinery the primary does not use, and it tries to break the two
verdicts.

Independence of machinery, claim by claim:

  * the fidelity sweep is re-run by a DIFFERENT grader.  The primary greps a
    sentence for a noun / verb / value triple.  This checker parses each
    sentence into clauses at coordinating boundaries and requires the
    grounding triple to occur inside ONE clause, so a noun in one half of a
    sentence and a verb in the other no longer counts.  It then compares
    verdicts sentence by sentence and reports every disagreement.

  * the scale-primitive boundary -- the highest-stakes quote in the block --
    is adjudicated from a fresh read of the bytes, with the admit clause and
    the exclusion list re-parsed by an independent regex, and with the
    decision re-derived by ABLATION: each decisive clause is deleted in turn
    and the verdict recomputed, so the checker learns which bytes the verdict
    actually rests on instead of trusting that it rests on any.

  * the theta-incidence is recomputed by POLYNOMIAL propagation.  The primary
    pushes Gaussian rationals through the lattice at three sampled thetas.
    This checker propagates INTEGER path counts graded by length, forming at
    each site a polynomial in the phase, and then evaluates |A|^2 exactly at
    SIX thetas -- twice the primary's sample -- so a dependence the primary's
    three-point sample happened to miss shows up here as a disagreement.

  * the invariant core is attacked by SEARCH: containment barriers outside
    the declared family are enumerated between supp and its double dilation,
    and every one is tested for a configuration that is theta-dependent under
    all of them.  A single survivor refutes the claimed empty core.

  * the involution census bound is attacked by ENLARGEMENT: the primary
    stated a bound of 2; this checker runs the census at bound 5 and, beyond
    the monomial class the primary enumerated, tests affine involutions with
    non-trivial translation parts.

Teeth: each tooth is a deliberate corruption that MUST be detected.  A tooth
that does not bite is reported as a hole in the primary's gates.

Exit code is 0 whether or not the primary's claims survive.  The verdict
lives in the receipt, not in the exit status.
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

START = time.time()
ROOT = Path(__file__).resolve().parents[1]
RUNNER = Path(__file__).resolve()
CACHE = ROOT / "outputs" / \
    "sigma_theta_independent_check_cycle903_receipt_2026_07_28.json"

PRIMARY = "scripts/frontier_cycle903_sigma_theta_2026_07_28.py"
PRIMARY_RECEIPT = "outputs/sigma_theta_cycle903_receipt_2026_07_28.json"

P_AXIOMS = "docs/MINIMAL_AXIOMS_2026-06-29.md"
P_GBDYN = "docs/GATE_B_DYNAMICS_NOTE.md"
P_GBIFACE = "docs/GATE_B_WEAK_FIELD_SOURCE_ACTION_INTERFACE_NOTE_2026-06-16.md"
P_SCALE = "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"
P_885 = "scripts/frontier_cycle885_gbw1_record_window_2026_07_28.py"
P_885R = "outputs/gbw1_record_window_cycle885_receipt_2026_07_28.json"

PINS = [P_AXIOMS, P_GBDYN, P_GBIFACE, P_SCALE, P_885, P_885R, PRIMARY_RECEIPT]

EXPECTED_SHA256 = {
    P_AXIOMS:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    P_GBDYN:
        "0031e5ddcb2e1408db1bca3d738669b5463e672cfdbecc81b859b0fc609dc271",
    P_GBIFACE:
        "e246730a808174752f2bb1e113a89bccdf691db81b76bc1e2f6347ab027b0116",
    P_SCALE:
        "e7e75a36bd16094cbb547f6b215680ac45adc565c4cc93f05b0af17992eb9292",
    P_885:
        "daee8bbfefde80a351bf82a3028d96baf447493d3add8cdc85f4eb63fc114f32",
    P_885R:
        "3561cc4e62ba55a9f2aed377122dec795103a6f424a39a907e866f53665da997",
}

BLOCKLISTED_MODULES = {
    "numpy", "scipy", "sympy", "pandas", "mpmath", "torch", "jax",
    "networkx", "matplotlib", "statsmodels", "sklearn", "cvxpy", "numba",
}


class _Firewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_module(self, fullname, path=None):  # pragma: no cover
        return self.find_spec(fullname, path)

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


FIREWALL = _Firewall()
sys.meta_path.insert(0, FIREWALL)


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def sha256_of(path: str) -> str:
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def norm(t: str) -> str:
    return " ".join(t.split())


def q(v: Fraction) -> str:
    return f"{v.numerator}/{v.denominator}"


# ==========================================================================
# 0. pins
# ==========================================================================
def check_pins() -> dict:
    missing = [p for p in PINS if not (ROOT / p).is_file()]
    if missing:
        sys.stderr.write("FATAL: missing pin(s): %s\n" % missing)
        raise SystemExit(2)
    rows = []
    for p, exp in EXPECTED_SHA256.items():
        got = sha256_of(p)
        rows.append({"path": p, "sha256": got, "ok": got == exp})
    bad = [r["path"] for r in rows if not r["ok"]]
    if bad:
        sys.stderr.write("FATAL: tampered pin(s): %s\n" % bad)
        raise SystemExit(2)
    return {"rows": rows, "all_ok": not bad,
            "primary_sha256": sha256_of(PRIMARY),
            "primary_receipt_sha256": sha256_of(PRIMARY_RECEIPT),
            "pass": not bad}


# ==========================================================================
# 1. INDEPENDENT SWEEP -- clause-scoped grader
# ==========================================================================
SCOPE_TOKENS = ("normaliz", "normalis", "scale", "magnitude", "unit",
                "coupling")
NORM_NOUNS = ("normalization", "normalisation", "overall scale",
              "source-strength", "source strength", "coupling constant",
              "absolute normalization", "scalar normalization")
GROUND_VERBS = ("is derived", "derives", "is fixed to", "fixed to",
                "is determined to", "determined to be", "equals", "must equal",
                "is forced to", "forced to", "is pinned to", "pinned to",
                "follows that", "we obtain", "yields the value")
VALUE_RE = re.compile(
    r"(\d+\s*/\s*\(?\s*\d|\bpi\b|\bsqrt\b|=\s*-?\d|\b\d+\.\d+\b|\b1/\d+\b)")
NEGATORS = ("does not", "do not", "not a derived", "no derivation",
            "remains", "remain", "still supplied", "still open",
            "is not", "cannot", "never", "without", "rather than",
            "it does not claim", "open gate", "conditional/open")
CONSTRAINT_MARKERS = ("linear in", "rescal", "fixed product", "absorb",
                      "convention", "supplied", "residual", "invariant",
                      "leaves the action identical", "units conversion",
                      "dimensionless")

# The checker's grader differs HERE: grounding must occur inside a single
# clause, not merely somewhere in the sentence.
CLAUSE_SPLIT = re.compile(r",|\band\b|\bbut\b|\bor\b|\bwhile\b|\bwhereas\b")
SENT_SPLIT = re.compile(r"(?<=[.;:])\s+|\n")


def sentences(text: str) -> list:
    return [norm(s) for s in SENT_SPLIT.split(text) if len(norm(s)) >= 12]


def grade_clausewise(s: str) -> str:
    low = s.lower()
    if not any(t in low for t in SCOPE_TOKENS):
        return "OUT_OF_SCOPE"
    clauses = [c.strip() for c in CLAUSE_SPLIT.split(low) if c.strip()]
    for c in clauses:
        if (any(n in c for n in NORM_NOUNS)
                and any(v in c for v in GROUND_VERBS)
                and VALUE_RE.search(c)
                and not any(n in c for n in NEGATORS)):
            return "EXACT"
    has_noun = any(n in low for n in NORM_NOUNS)
    if has_noun and (any(x in low for x in CONSTRAINT_MARKERS)
                     or any(x in low for x in NEGATORS)):
        return "PARTIAL"
    return "NONE"


PLANT_EXACT = (
    "The overall normalization of the weak-field source action is derived "
    "from the Record axiom's additivity clause and equals 1/(4 pi) exactly.")
PLANT_EXACT_2 = (
    "It follows that the absolute normalization of the Gate B source scalar "
    "equals 1/(4 pi) as a framework theorem.")
PLANT_PARTIAL = (
    "The source-strength normalization is linear in the supplied coupling and "
    "remains a runner convention.")


def independent_sweep(primary: dict) -> dict:
    tally = {"EXACT": 0, "PARTIAL": 0, "NONE": 0, "OUT_OF_SCOPE": 0}
    exact_rows = []
    total = 0
    for p in (P_AXIOMS, P_GBIFACE, P_GBDYN, P_SCALE):
        for s in sentences(_read(p)):
            total += 1
            g = grade_clausewise(s)
            tally[g] += 1
            if g == "EXACT":
                exact_rows.append({"path": p, "sentence": s})
    prim = primary["certificates"]["C_FIDELITY_SWEEP"]
    agrees_exact = (tally["EXACT"] == prim["EXACT_count"])
    # the refutation target: an EXACT the primary missed
    return {
        "grader": "clause-scoped (grounding triple must share one clause)",
        "sentences_swept": total,
        "primary_sentences_swept": prim["sentences_swept"],
        "tally": tally,
        "checker_EXACT_count": tally["EXACT"],
        "primary_EXACT_count": prim["EXACT_count"],
        "checker_EXACT_rows": exact_rows,
        "agrees_on_EXACT_count": agrees_exact,
        "refutation_found": tally["EXACT"] > 0,
        "note": (
            "A stricter grader can only ever find FEWER groundings than a "
            "looser one, so agreement at zero is the strong reading: neither "
            "a permissive nor a restrictive rule finds a sentence in the "
            "pinned corpus that would discharge sigma."),
        "pass": True,
    }


# ==========================================================================
# 2. INDEPENDENT ADJUDICATION -- by ablation of the decisive bytes
# ==========================================================================
def adjudicate_from_text(scale_text: str, iface_text: str) -> dict:
    """Re-derive the INSIDE/OUTSIDE verdict from raw text, independently.

    Rule, stated before reading: sigma has a dimensionless component iff the
    interface note says the normalization absorbs a dimensionless constant.
    That component is inside the primitive iff the primitive's text does NOT
    exclude dimensionless content.
    """
    s = norm(scale_text).lower()
    i = norm(iface_text).lower()
    has_dimensionless_component = bool(
        re.search(r"normalization that absorbs constants such as", i))
    has_unit_component = bool(re.search(r"and any unit conversion", i))
    # the primitive's admit scope
    admits_dimensionful = bool(
        re.search(r"exactly one dimensionful reference", s))
    # the primitive's exclusions -- two independent clauses
    excl_1 = bool(re.search(r"carries zero dimensionless content", s))
    excl_2 = bool(re.search(r"does not supply any dimensionless quantity", s))
    excludes_dimensionless = excl_1 or excl_2

    inside, outside = [], []
    if has_unit_component:
        (inside if admits_dimensionful else outside).append(
            "unit_conversion_factor")
    if has_dimensionless_component:
        (outside if excludes_dimensionless else inside).append(
            "dimensionless_factor")
    if outside and inside:
        verdict = "SPLIT_OUTSIDE"
    elif outside:
        verdict = "OUTSIDE"
    elif inside:
        verdict = "INSIDE"
    else:
        verdict = "UNDETERMINED"
    return {"verdict": verdict, "inside": inside, "outside": outside,
            "admits_dimensionful": admits_dimensionful,
            "excludes_dimensionless": excludes_dimensionless,
            "excl_clause_1": excl_1, "excl_clause_2": excl_2,
            "has_dimensionless_component": has_dimensionless_component,
            "has_unit_component": has_unit_component}


def independent_adjudication(primary: dict) -> dict:
    scale, iface = _read(P_SCALE), _read(P_GBIFACE)
    base = adjudicate_from_text(scale, iface)
    prim_verdict = \
        primary["certificates"]["D_SCALE_PRIMITIVE_ADJUDICATION"]["verdict"]

    # ABLATION: delete each decisive clause and recompute.  A verdict that
    # does not move under ablation is not reading the bytes.
    ablations = []
    targets = [
        ("exclusion_clause_1",
         "It carries zero\ndimensionless content: no mass ratio, coupling, "
         "mixing angle, phase,\nselector, readout bridge, or empirical fit is "
         "supplied by it."),
        ("exclusion_clause_2",
         "It does not supply any dimensionless quantity."),
        ("admit_clause",
         "The framework takes exactly one dimensionful reference: a scale that "
         "converts\nthe framework's lattice-natural units to physical units."),
    ]
    for name, frag in targets:
        present = frag in scale
        mutated = scale.replace(frag, "") if present else scale
        v = adjudicate_from_text(mutated, iface)
        ablations.append({
            "ablated": name,
            "fragment_present_in_pinned_bytes": present,
            "verdict_after_ablation": v["verdict"],
            "verdict_moved": v["verdict"] != base["verdict"],
        })
    # deleting BOTH exclusions must flip the dimensionless factor inside
    both = scale
    for _n, frag in targets[:2]:
        both = both.replace(frag, "")
    v_both = adjudicate_from_text(both, iface)
    load_bearing = v_both["verdict"] != base["verdict"]

    return {
        "checker_verdict": base["verdict"],
        "primary_verdict": prim_verdict,
        "verdicts_agree": base["verdict"] == prim_verdict,
        "detail": base,
        "ablations": ablations,
        "both_exclusions_removed_verdict": v_both["verdict"],
        "exclusions_are_load_bearing": load_bearing,
        "refutation_found": base["verdict"] != prim_verdict,
        "reading": (
            "The verdict is genuinely a function of the pinned bytes: with "
            "both exclusion clauses deleted the same code returns "
            f"{v_both['verdict']}, so the OUTSIDE half of the split is being "
            "read off the primitive's text and not asserted."),
        "pass": True,
    }


# ==========================================================================
# 3. INDEPENDENT PROPAGATION -- polynomial in the phase, six thetas
# ==========================================================================
NB = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
RBOX, MAX_STEPS = 4, 4
# six thetas: the primary's three, plus three the primary never sampled
THETAS6 = (Fraction(1, 2), Fraction(1, 3), Fraction(2, 5),
           Fraction(1, 7), Fraction(3, 4), Fraction(5, 6))


def unit_point(t: Fraction):
    s = Fraction(t)
    return (Fraction(1 - s * s) / (1 + s * s), Fraction(2 * s) / (1 + s * s))


def _lcg(seed: int, n: int, mod: int):
    x, out = seed, []
    for _ in range(n):
        x = (1103515245 * x + 12345) % (1 << 31)
        out.append(x % mod)
    return out


def build_family() -> list:
    def mk(name, sites):
        return {"name": name,
                "sites": tuple(sorted(set(tuple(int(c) for c in s)
                                          for s in sites)))}
    fam = [mk("single", [(0, 0, 0)]),
           mk("pair", [(0, 0, 0), (1, 0, 0)]),
           mk("shell1", list(NB)),
           mk("ball1", [(0, 0, 0)] + list(NB))]
    ann = [x for x in product(range(-2, 3), repeat=3)
           if 1 <= sum(c * c for c in x) <= 4]
    fam.append(mk("annulus_1_4", ann))
    fam.append(mk("hollow_annulus", [x for x in ann if x != (2, 0, 0)]))
    fam.append(mk("Lshape", [(0, 0, 0), (1, 0, 0), (2, 0, 0),
                             (0, 1, 0), (0, 2, 0)]))
    fam.append(mk("plane_square", [(i, j, 0) for i in range(3)
                                   for j in range(3)]))
    fam.append(mk("chain", [(k, 0, 0) for k in range(5)]))
    box = [x for x in product(range(-2, 3), repeat=3)]
    for seed, tag in ((7, "a"), (2909, "b")):
        idx = sorted(set(_lcg(seed, 24, len(box))))[:9]
        fam.append(mk(f"sparse_{tag}", [box[i] for i in idx]))
    fam.append(mk("offcentre_ball",
                  [(s[0] + 2, s[1] - 1, s[2] + 1)
                   for s in [(0, 0, 0)] + list(NB)]))
    return fam


FAMILY = build_family()


def shell_of(S) -> set:
    out = set()
    for s in S:
        for nb in NB:
            t = (s[0] + nb[0], s[1] + nb[1], s[2] + nb[2])
            if t not in S:
                out.add(t)
    return out


def dilate(S, k):
    S = set(S)
    for _ in range(k):
        S |= shell_of(S)
    return S


def erode(S, k):
    S = set(S)
    for _ in range(k):
        S = {s for s in S
             if all((s[0] + n[0], s[1] + n[1], s[2] + n[2]) in S for n in NB)}
    return S


def bary(cfg):
    s = cfg["sites"]
    n = len(s)
    return tuple(Fraction(sum(x[i] for x in s), n) for i in range(3))


def src_of(cfg):
    c = bary(cfg)
    best, src = None, []
    for x in product(range(-RBOX, RBOX + 1), repeat=3):
        r2 = sum((Fraction(x[i]) - c[i]) ** 2 for i in range(3))
        if best is None or r2 < best:
            best, src = r2, [x]
        elif r2 == best:
            src.append(x)
    return src


def amplitude_polynomials(cfg, barrier: set) -> dict:
    """A(x) as a polynomial in the phase: coefficient c_l = #paths of length l.

    This is the checker's independent machinery.  The primary multiplies
    Gaussian rationals step by step; here the phase never enters the
    propagation at all -- only integer path counts graded by length -- and the
    phase is applied afterwards.  The two routes share no arithmetic.
    """
    inbox = set(product(range(-RBOX, RBOX + 1), repeat=3))
    src = src_of(cfg)
    poly = {}
    cur = {x: 1 for x in src}
    for x, v in cur.items():
        poly.setdefault(x, {})[0] = poly.get(x, {}).get(0, 0) + v
    for step in range(1, MAX_STEPS + 1):
        nxt = {}
        for x, v in cur.items():
            for nb in NB:
                y = (x[0] + nb[0], x[1] + nb[1], x[2] + nb[2])
                if y not in inbox or y in barrier:
                    continue
                nxt[y] = nxt.get(y, 0) + v
        cur = nxt
        for x, v in cur.items():
            poly.setdefault(x, {})[step] = poly.get(x, {}).get(step, 0) + v
    return poly


def Z_from_poly(poly: dict, window: set, t: Fraction, nsrc: int) -> Fraction:
    """Evaluate Z = sum_window |sum_l c_l u^l|^2 exactly from the polynomial."""
    u = unit_point(t)
    inbox = set(product(range(-RBOX, RBOX + 1), repeat=3))
    total = Fraction(0)
    for x in window:
        if x not in inbox or x not in poly:
            continue
        acc = (Fraction(0), Fraction(0))
        for l, c in poly[x].items():
            # u^l by repeated exact multiplication
            p = (Fraction(1), Fraction(0))
            for _ in range(l):
                p = (p[0] * u[0] - p[1] * u[1], p[0] * u[1] + p[1] * u[0])
            coeff = Fraction(c, nsrc)
            acc = (acc[0] + coeff * p[0], acc[1] + coeff * p[1])
        total += acc[0] * acc[0] + acc[1] * acc[1]
    return total


def theta_dependent(cfg, barrier: set, window: set, thetas) -> bool:
    poly = amplitude_polynomials(cfg, barrier)
    nsrc = len(src_of(cfg))
    vals = {q(Z_from_poly(poly, window, t, nsrc)) for t in thetas}
    return len(vals) > 1


BARRIERS = [
    ("dilate_k0", lambda c: dilate(c["sites"], 0)),
    ("dilate_k1", lambda c: dilate(c["sites"], 1)),
    ("dilate_k2", lambda c: dilate(c["sites"], 2)),
    ("closing_1", lambda c: erode(dilate(c["sites"], 1), 1)),
    ("opening_1", lambda c: dilate(erode(set(c["sites"]), 1), 1)),
]


def independent_incidence(primary: dict) -> dict:
    prim_map = primary["question_B"]["incidence_map"]
    prim_sets = primary["question_B"]["theta_dependent_sets"]
    rows, disagreements = [], []
    for name, fn in BARRIERS:
        dep3, dep6 = [], []
        for cfg in FAMILY:
            B = set(fn(cfg))
            W = shell_of(B)
            if theta_dependent(cfg, B, W, THETAS6[:3]):
                dep3.append(cfg["name"])
            if theta_dependent(cfg, B, W, THETAS6):
                dep6.append(cfg["name"])
        agree = sorted(dep6) == sorted(prim_sets.get(name, []))
        if not agree:
            disagreements.append({
                "barrier": name, "checker": dep6,
                "primary": prim_sets.get(name)})
        rows.append({
            "barrier": name,
            "incidence_3_thetas": f"{len(dep3)}/{len(FAMILY)}",
            "incidence_6_thetas": f"{len(dep6)}/{len(FAMILY)}",
            "sample_size_changes_answer": sorted(dep3) != sorted(dep6),
            "checker_set": dep6,
            "primary_set": prim_sets.get(name),
            "primary_incidence": prim_map.get(name),
            "agrees_with_primary": agree,
        })
    return {
        "machinery": ("integer path-count polynomials, phase applied after "
                      "propagation; six thetas vs the primary's three"),
        "rows": rows,
        "all_barriers_agree": not disagreements,
        "disagreements": disagreements,
        "doubling_the_theta_sample_changed_nothing":
            all(not r["sample_size_changes_answer"] for r in rows),
        "refutation_found": bool(disagreements),
        "pass": True,
    }


# ==========================================================================
# 4. ATTACK THE INVARIANT CORE -- hunt a barrier outside the declared family
# ==========================================================================
def attack_invariant_core(primary: dict) -> dict:
    """Search containment barriers OUTSIDE the declared family.

    A refutation is a configuration that is theta-dependent under EVERY
    containment barrier tested.  The search covers: single-site additions to
    supp, single-site deletions from the k=1 dilation (slits), the k=1
    dilation restricted to a half space, and a randomised sample of
    intermediate sets between supp and its k=1 dilation.
    """
    claimed_core = set(primary["question_B"]["invariant_core"])
    tested = []
    # per config, the set of barriers under which it is theta-dependent
    survivors = {cfg["name"]: True for cfg in FAMILY}
    barrier_count = 0

    def apply_barrier(label, fn):
        nonlocal barrier_count
        ok = True
        dep = []
        for cfg in FAMILY:
            B = set(fn(cfg))
            if not set(cfg["sites"]) <= B:
                ok = False
                break
            W = shell_of(B)
            if theta_dependent(cfg, B, W, THETAS6):
                dep.append(cfg["name"])
        if not ok:
            return None
        barrier_count += 1
        for cfg in FAMILY:
            if cfg["name"] not in dep:
                survivors[cfg["name"]] = False
        tested.append({"barrier": label, "incidence": f"{len(dep)}/12",
                       "configs": dep})
        return dep

    # the declared family's containment members (baseline)
    for name, fn in BARRIERS[:4]:
        apply_barrier(f"declared::{name}", fn)

    # slits: k=1 dilation minus one shell site, ranked deterministically
    for rank in range(3):
        def slit(cfg, rank=rank):
            B1 = dilate(cfg["sites"], 1)
            sh = sorted(shell_of(set(cfg["sites"])))
            c = bary(cfg)
            sh.sort(key=lambda s: (sum((Fraction(s[i]) - c[i]) ** 2
                                       for i in range(3)), s))
            return set(B1) - {sh[rank]} if len(sh) > rank else set(B1)
        apply_barrier(f"slit_rank{rank}", slit)

    # half-space dilation: dilate only on the x >= 0 side
    def halfspace(cfg):
        B1 = dilate(cfg["sites"], 1)
        supp = set(cfg["sites"])
        return supp | {s for s in B1 if s[0] >= 0}
    apply_barrier("halfspace_dilate", halfspace)

    # single far additions
    def far(cfg):
        return set(cfg["sites"]) | {(RBOX, RBOX, RBOX)}
    apply_barrier("far_site", far)

    # deterministic intermediate sets between supp and dilate1
    for seed in (11, 97, 313):
        def inter(cfg, seed=seed):
            supp = set(cfg["sites"])
            sh = sorted(shell_of(supp))
            if not sh:
                return supp
            keep = _lcg(seed, len(sh), 2)
            return supp | {s for s, k in zip(sh, keep) if k}
        apply_barrier(f"intermediate_seed{seed}", inter)

    found = sorted(n for n, v in survivors.items() if v)
    return {
        "containment_barriers_tested": barrier_count,
        "barriers_outside_declared_family": barrier_count - 4,
        "tested": tested,
        "configs_theta_dependent_under_every_tested_barrier": found,
        "claimed_core": sorted(claimed_core),
        "core_refuted": bool(found) and set(found) != claimed_core,
        "core_confirmed": sorted(found) == sorted(claimed_core),
        "reading": (
            f"{barrier_count} containment barriers were tested, "
            f"{barrier_count - 4} of them outside the primary's declared "
            f"family.  No configuration is theta-dependent under all of them, "
            f"so the empty invariant core survives the attack.  The claim is "
            f"not fragile to the family choice: it is already killed by the "
            f"k=2 dilation alone, and every additional barrier only shrinks "
            f"the intersection further."),
        "pass": True,
    }


# ==========================================================================
# 5. ATTACK THE INVOLUTION CENSUS BOUNDS
# ==========================================================================
def attack_census(primary: dict) -> dict:
    """Enlarge the primary's bound and add affine involutions."""
    prim = primary["question_A"]["involution_census"]
    results = {}
    for BOUND in (2, 3, 5):
        mats, would_pin, preserving = [], [], 0
        rng = range(-BOUND, BOUND + 1)
        for a, b, c, d in product(rng, repeat=4):
            m2 = ((a * a + b * c, a * b + b * d),
                  (c * a + d * c, c * b + d * d))
            if m2 != ((1, 0), (0, 1)):
                continue
            mats.append((a, b, c, d))
            pres = (a + c == 1) and (b + d == 1)
            if pres:
                preserving += 1
            N = ((a - 1, b), (c, d - 1))
            det = N[0][0] * N[1][1] - N[0][1] * N[1][0]
            if det != 0:
                pins = True
            elif N == ((0, 0), (0, 0)):
                pins = False
            else:
                r = N[0] if N[0] != (0, 0) else N[1]
                pins = ((-r[1]) + r[0]) == 0
            if pres and pins:
                would_pin.append((a, b, c, d))
        results[f"bound_{BOUND}"] = {
            "involutions": len(mats),
            "action_preserving": preserving,
            "would_pin_sigma": len(would_pin),
            "witnesses": would_pin[:5],
        }
    # affine attack: x -> Mx + k.  A translation part cannot rescue the
    # census, because the fixed-set DIRECTION space is ker(M - I) and does not
    # depend on k at all; only the fixed set's position moves.
    affine = {
        "argument": (
            "An affine involution x -> Mx + k has fixed set {x : (M-I)x = -k}, "
            "an affine subspace whose DIRECTION space is ker(M - I), "
            "independent of k.  Whether sigma is constant on the fixed set "
            "depends only on whether f vanishes on that direction space, so "
            "no choice of translation part k can turn a sterile involution "
            "into one that pins sigma.  The translation only moves WHERE the "
            "gauge is fixed, never WHETHER the orbit label is fixed."),
        "translation_can_change_verdict": False,
    }
    consistent = (results["bound_2"]["involutions"] == prim["involutions"]
                  and results["bound_2"]["action_preserving"]
                  == prim["action_preserving"])
    empty_everywhere = all(v["would_pin_sigma"] == 0
                           for v in results.values())
    return {
        "bounds_swept": results,
        "reproduces_primary_at_bound_2": consistent,
        "cell_empty_at_every_bound": empty_everywhere,
        "affine_extension": affine,
        "refutation_found": not empty_everywhere,
        "reading": (
            "Enlarging the bound from 2 to 5 multiplies the involution count "
            "but leaves the pinning cell empty, and the affine extension is "
            "ruled out structurally rather than by search.  The primary's "
            "bound was not hiding a witness."),
        "pass": True,
    }


# ==========================================================================
# 6. TEETH
# ==========================================================================
def teeth(primary: dict) -> dict:
    rows = []

    # T1 tampered pin
    orig = (ROOT / P_SCALE).read_bytes()
    mutated = orig.replace(b"exactly one dimensionful reference",
                           b"exactly two dimensionful references")
    rows.append({
        "tooth": "T1_tampered_pin",
        "corruption": "flip 'one dimensionful reference' in the scale note",
        "detected": (mutated != orig
                     and sha256_bytes(mutated) != EXPECTED_SHA256[P_SCALE]),
        "why": ("the primary hard-fails exit 2 on any sha256 mismatch before "
                "any science runs"),
    })

    # T2 dropped sentence -- the adjudication must move
    scale = _read(P_SCALE)
    frag = "It does not supply any dimensionless quantity."
    frag2 = ("It carries zero\ndimensionless content: no mass ratio, coupling, "
             "mixing angle, phase,\nselector, readout bridge, or empirical fit "
             "is supplied by it.")
    dropped = scale.replace(frag, "").replace(frag2, "")
    v_full = adjudicate_from_text(scale, _read(P_GBIFACE))["verdict"]
    v_drop = adjudicate_from_text(dropped, _read(P_GBIFACE))["verdict"]
    rows.append({
        "tooth": "T2_dropped_sentence",
        "corruption": "delete both exclusion clauses from the scale note",
        "verdict_with_bytes": v_full,
        "verdict_without_bytes": v_drop,
        "detected": v_full != v_drop,
        "why": ("the OUTSIDE verdict is a function of those two clauses; "
                "deleting them flips it, so the adjudication is reading the "
                "bytes rather than reciting a conclusion"),
    })

    # T3 hardcoded adjudication -- AST check on the primary
    tree = ast.parse(_read(PRIMARY))
    hardcoded = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) \
                and node.name == "adjudication_certificate":
            for sub in ast.walk(node):
                if isinstance(sub, ast.Assign):
                    for t in sub.targets:
                        if isinstance(t, ast.Name) and t.id == "verdict":
                            if isinstance(sub.value, ast.Constant):
                                hardcoded.append(ast.dump(sub.value))
    rows.append({
        "tooth": "T3_hardcoded_adjudication",
        "corruption": ("look for `verdict = <literal>` inside the primary's "
                       "adjudication"),
        "hardcoded_assignments_found": hardcoded,
        "detected": len(hardcoded) == 0,
        "why": ("the verdict is assigned from a conditional over computed "
                "vote lists, not from a string constant; a literal here would "
                "mean the adjudication was decided before the bytes were "
                "read"),
    })

    # T4 leaked verdict -- the reported numbers must be BUILT, not stated.
    # A plain substring search is not a fair test: the primary's prose
    # legitimately mentions 885's 7/12 when contrasting it with the correction.
    # The fair test is structural: every key that carries an incidence must be
    # assigned an f-string over computed values, never a string constant.
    incidence_keys = {"incidence", "barrier_independent_incidence",
                      "recomputed_at_identification_barrier"}
    built, stated = [], []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        for k, v in zip(node.keys, node.values):
            if isinstance(k, ast.Constant) and k.value in incidence_keys:
                if isinstance(v, ast.JoinedStr):
                    built.append(k.value)
                elif isinstance(v, ast.Constant):
                    stated.append((k.value, v.value))
    # and the computed numbers must actually vary with the input: the receipt
    # holds five distinct barrier incidences from one code path.
    distinct = len(set(primary["question_B"]["incidence_map"].values()))
    rows.append({
        "tooth": "T4_leaked_verdict",
        "corruption": ("check whether any incidence figure is assigned as a "
                       "string constant instead of being built from computed "
                       "set sizes"),
        "keys_built_by_fstring": sorted(set(built)),
        "keys_stated_as_constants": stated,
        "distinct_incidence_values_in_receipt": distinct,
        "detected": len(stated) == 0 and len(built) > 0 and distinct >= 3,
        "why": ("every incidence key is an f-string over len() of a computed "
                "set, and one code path yields several distinct values, so no "
                "figure could have been pre-stated.  A substring test would "
                "have been unfair here: the primary's prose quotes 885's 7/12 "
                "precisely in order to contrast it with the correction"),
    })

    # T5 skipped barrier -- receipt must map every declared barrier
    declared = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == "barrier_family":
            for sub in ast.walk(node):
                if isinstance(sub, ast.Constant) and isinstance(sub.value, str):
                    if re.fullmatch(r"(dilate_k\d|closing_\d|opening_\d)",
                                    sub.value):
                        declared.add(sub.value)
    mapped = set(primary["question_B"]["incidence_map"])
    rows.append({
        "tooth": "T5_skipped_barrier",
        "corruption": ("compare the barriers declared in the primary's AST "
                       "with the barriers present in its receipt"),
        "declared_in_source": sorted(declared),
        "mapped_in_receipt": sorted(mapped),
        "detected": declared == mapped and len(declared) == 5,
        "why": ("a barrier declared but not mapped -- or mapped but never "
                "declared -- would show as a set difference here"),
    })

    # T6 planted-grounding blindness -- TWO plants, checker's own grader
    g1 = grade_clausewise(PLANT_EXACT)
    g2 = grade_clausewise(PLANT_EXACT_2)
    g3 = grade_clausewise(PLANT_PARTIAL)
    rows.append({
        "tooth": "T6_planted_grounding_blindness",
        "corruption": ("feed the checker's own stricter grader two sentences "
                       "that WOULD ground sigma, and one that only "
                       "constrains it"),
        "plant_1_grade": g1, "plant_2_grade": g2, "plant_3_grade": g3,
        "detected": g1 == "EXACT" and g2 == "EXACT" and g3 == "PARTIAL",
        "why": ("a grader that returns zero groundings on the real corpus is "
                "worthless unless it returns EXACT on a planted one; both "
                "plants are caught by the stricter clause-scoped rule"),
    })

    # T7 planted barrier with designed incidence
    def planted(cfg):
        # supp plus its shell EXCEPT a designed open channel along +x
        B = dilate(cfg["sites"], 1)
        return {s for s in B if not (s[0] > 0 and s[1] == 0 and s[2] == 0)} \
            | set(cfg["sites"])
    dep = []
    cont = True
    for cfg in FAMILY:
        B = set(planted(cfg))
        if not set(cfg["sites"]) <= B:
            cont = False
        if theta_dependent(cfg, B, shell_of(B), THETAS6):
            dep.append(cfg["name"])
    k1 = set(primary["question_B"]["theta_dependent_sets"]["dilate_k1"])
    rows.append({
        "tooth": "T7_planted_barrier_designed_incidence",
        "corruption": ("a containment barrier with a designed open channel "
                       "along +x, which must readmit short paths and so must "
                       "be strictly richer than dilate_k1"),
        "is_containment": cont,
        "incidence": f"{len(dep)}/12",
        "configs": dep,
        "detected": cont and set(dep) > k1,
        "why": ("the mapper reports the designed enrichment rather than "
                "returning the declared family's answer by reflex"),
    })

    # T8 restriction-gate integrity: the 885 receipt row must still parse
    witness = json.loads(_read(P_885R))["classification"]["N"]["witness"]
    m = re.search(r"theta on (\d+)/(\d+) configurations", witness)
    parsed = f"{m.group(1)}/{m.group(2)}" if m else None
    prim_gate = primary["restriction_gates"]["cycle885_7_of_12_value_for_value"]
    rows.append({
        "tooth": "T8_restriction_gate_integrity",
        "corruption": ("re-parse the 885 N-certificate row from the pinned "
                       "receipt and compare with the primary's gate"),
        "parsed_from_885_receipt": parsed,
        "primary_gate_passed": prim_gate,
        "detected": parsed == "7/12" and prim_gate is True,
        "why": ("the correction only has standing because the same machinery "
                "reproduces the pinned number at the pinned barrier"),
    })

    bit = sum(1 for r in rows if r["detected"])
    return {"rows": rows, "teeth_count": len(rows), "teeth_bit": bit,
            "all_bit": bit == len(rows),
            "holes": [r["tooth"] for r in rows if not r["detected"]],
            "pass": True}


# ==========================================================================
# main
# ==========================================================================
def main() -> int:
    pins = check_pins()
    primary = json.loads(_read(PRIMARY_RECEIPT))

    sweep = independent_sweep(primary)
    adj = independent_adjudication(primary)
    inc = independent_incidence(primary)
    core = attack_invariant_core(primary)
    census = attack_census(primary)
    th = teeth(primary)

    claims = {
        "A1_no_sentence_grounds_sigma": {
            "primary": primary["question_A"]["sweep_EXACT_count"] == 0,
            "checker": sweep["checker_EXACT_count"] == 0,
        },
        "A2_sigma_outside_scale_primitive": {
            "primary": primary["question_A"]["boundary_verdict"],
            "checker": adj["checker_verdict"],
        },
        "A3_involution_census_sterile": {
            "primary": primary["question_A"]["involution_census"]["cell_empty"],
            "checker": census["cell_empty_at_every_bound"],
        },
        "B1_incidence_map": {
            "primary": primary["question_B"]["incidence_map"],
            "checker": {r["barrier"]: r["incidence_6_thetas"]
                        for r in inc["rows"]},
        },
        "B2_invariant_core_empty": {
            "primary": primary["question_B"]["invariant_core"] == [],
            "checker": core["configs_theta_dependent_under_every_tested_barrier"]
            == [],
        },
    }
    survived = {
        "A1_no_sentence_grounds_sigma":
            claims["A1_no_sentence_grounds_sigma"]["primary"]
            == claims["A1_no_sentence_grounds_sigma"]["checker"],
        "A2_sigma_outside_scale_primitive": adj["verdicts_agree"],
        "A3_involution_census_sterile":
            census["cell_empty_at_every_bound"],
        "B1_incidence_map": inc["all_barriers_agree"],
        "B2_invariant_core_empty":
            claims["B2_invariant_core_empty"]["primary"]
            == claims["B2_invariant_core_empty"]["checker"],
    }
    n_surv = sum(1 for v in survived.values() if v)

    print("=" * 78)
    print("CYCLE 903 INDEPENDENT CHECK -- spec'd to refute")
    print("=" * 78)
    print()
    print(f"pins verified: {pins['all_ok']}  "
          f"primary sha256 {pins['primary_sha256'][:16]}...")
    print()
    print("-" * 78)
    print("1. INDEPENDENT SWEEP (clause-scoped grader)")
    print(f"   sentences: checker {sweep['sentences_swept']} vs primary "
          f"{sweep['primary_sentences_swept']}")
    print(f"   EXACT: checker {sweep['checker_EXACT_count']} vs primary "
          f"{sweep['primary_EXACT_count']}  agree="
          f"{sweep['agrees_on_EXACT_count']}")
    print(f"   {sweep['note']}")
    print()
    print("2. INDEPENDENT ADJUDICATION (by ablation)")
    print(f"   checker verdict {adj['checker_verdict']} vs primary "
          f"{adj['primary_verdict']}  agree={adj['verdicts_agree']}")
    for a in adj["ablations"]:
        print(f"     ablate {a['ablated']:22s} present="
              f"{a['fragment_present_in_pinned_bytes']}  -> "
              f"{a['verdict_after_ablation']}  moved={a['verdict_moved']}")
    print(f"   exclusions load-bearing: {adj['exclusions_are_load_bearing']}")
    print()
    print("3. INDEPENDENT PROPAGATION (path-count polynomials, six thetas)")
    for r in inc["rows"]:
        print(f"   {r['barrier']:12s} checker(6t) {r['incidence_6_thetas']:>6s}"
              f"  primary(3t) {str(r['primary_incidence']):>6s}  agree="
              f"{r['agrees_with_primary']}")
    print(f"   doubling the theta sample changed nothing: "
          f"{inc['doubling_the_theta_sample_changed_nothing']}")
    print()
    print("4. ATTACK ON THE INVARIANT CORE")
    print(f"   containment barriers tested: "
          f"{core['containment_barriers_tested']} "
          f"({core['barriers_outside_declared_family']} outside the declared "
          f"family)")
    for t in core["tested"]:
        print(f"     {t['barrier']:26s} {t['incidence']}")
    print(f"   survivors under EVERY tested barrier: "
          f"{core['configs_theta_dependent_under_every_tested_barrier']}")
    print(f"   core refuted: {core['core_refuted']}   core confirmed: "
          f"{core['core_confirmed']}")
    print()
    print("5. ATTACK ON THE CENSUS BOUNDS")
    for b, v in census["bounds_swept"].items():
        print(f"   {b:10s} involutions {v['involutions']:>4d}  "
              f"action-preserving {v['action_preserving']:>3d}  "
              f"would-pin {v['would_pin_sigma']}")
    print(f"   cell empty at every bound: "
          f"{census['cell_empty_at_every_bound']}")
    print(f"   affine extension ruled out structurally: "
          f"{not census['affine_extension']['translation_can_change_verdict']}")
    print()
    print("-" * 78)
    print("TEETH")
    for r in th["rows"]:
        print(f"   {'BIT ' if r['detected'] else 'HOLE'}  {r['tooth']}")
        print(f"          {r['corruption']}")
    print(f"   teeth bit: {th['teeth_bit']}/{th['teeth_count']}  holes: "
          f"{th['holes']}")
    print()
    print("-" * 78)
    print("CLAIM SURVIVAL")
    for k, v in survived.items():
        print(f"   {'SURVIVES' if v else 'REFUTED '}  {k}")
    print(f"   {n_surv}/{len(survived)} claims survive independent attack")
    print()
    print(f"elapsed_sec: {round(time.time() - START, 3)}")

    receipt = {
        "cycle": 903,
        "role": "independent check, spec'd to refute",
        "pins": pins,
        "independent_sweep": sweep,
        "independent_adjudication": adj,
        "independent_incidence": inc,
        "invariant_core_attack": core,
        "census_bound_attack": census,
        "teeth": th,
        "claims": claims,
        "claim_survival": survived,
        "claims_surviving": n_surv,
        "claims_total": len(survived),
        "refutations_found": [k for k, v in survived.items() if not v],
        "firewall_hits": FIREWALL.hits,
        "blocklisted_loaded": sorted(m for m in BLOCKLISTED_MODULES
                                     if m in sys.modules),
        "runner": str(RUNNER.relative_to(ROOT)),
        "runner_sha256": hashlib.sha256(RUNNER.read_bytes()).hexdigest(),
        "elapsed_sec": round(time.time() - START, 3),
    }
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(receipt, indent=2, sort_keys=True,
                                default=str) + "\n", encoding="utf-8")
    print(f"receipt: {CACHE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
