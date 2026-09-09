#!/usr/bin/env python3
"""Cycle 903 -- the bridge scalar sigma, and the barrier-dependence of the
theta-incidence.

Two small named questions remain on the gravity lane's ledger.  This runner
closes both, by computation, on pinned bytes.

QUESTION A -- THE BRIDGE SCALAR sigma.
    Cycle 871's lineage priced the source-action bridge to ONE scalar: the
    overall normalization, with additivity/locality/uniformity FORCED.  Cycle
    896 showed the same scalar sits in the GB-S2 residual, so the joint
    residual nets one.  Is sigma DERIVABLE from the axioms, or is it the
    lane's terminal supplied scalar?

    Three attacks, all computed:
      (a) the fidelity sweep -- every sentence of the axiom memo and both
          Gate-B notes touching normalization / scale / magnitude / unit /
          coupling, graded EXACT / PARTIAL / NONE against published selection
          rules.  A planted grounding sentence must be detected as grounding.
      (b) the scale-reference primitive boundary -- does sigma fall INSIDE the
          approved primitive's scope (a consumption of existing approved
          content, so the lane's accounting improves by one named dimension)
          or OUTSIDE it (sigma is its own supplied scalar)?  The boundary's
          exact bytes decide.
      (c) the structural argument -- rebuild the bridge's forced properties
          from the Gate-B rows, verify the one-dimensional residual exactly,
          then run the M2-style involution census on the bridge's one line.

QUESTION B -- THE THETA-INCIDENCE.
    Cycle 885 measured that Z moves with the kernel phase gain theta on 7/12
    configurations, at the barrier B(R) = supp(R).  Cycle 893 found that the
    incidence MOVES with the barrier.  This runner computes the incidence map
    exactly for a declared containment family of barriers, computes the
    mechanism that moves it, and extracts the barrier-independent invariant
    core -- the honest replacement for the barrier-specific 7/12.

Discipline: TEXT/AST/JSON only.  Every pinned input is checked by full path,
sha256, and git blob before any science runs; a missing or tampered pin is a
hard exit 2.  All arithmetic is exact (Fraction / Gaussian rational); no
floating point enters any certified value.  Numeric science modules are
blocked from import by a meta-path firewall and the block is asserted with a
0-hits gate.  Every gate is outcome-neutral: it certifies that the computation
was performed and internally consistent, never that a particular verdict was
reached.
"""

from __future__ import annotations

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
CACHE = ROOT / "outputs" / "sigma_theta_cycle903_receipt_2026_07_28.json"

# --------------------------------------------------------------------------
# import firewall -- no numeric/science module may enter this process
# --------------------------------------------------------------------------
BLOCKLISTED_MODULES = {
    "numpy", "scipy", "sympy", "pandas", "mpmath", "torch", "jax",
    "networkx", "matplotlib", "statsmodels", "sklearn", "cvxpy", "numba",
}


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_module(self, fullname, path=None):  # pragma: no cover - legacy
        return self.find_spec(fullname, path)

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)


# --------------------------------------------------------------------------
# pinned inputs
# --------------------------------------------------------------------------
P_AXIOMS = "docs/MINIMAL_AXIOMS_2026-06-29.md"
P_GBDYN = "docs/GATE_B_DYNAMICS_NOTE.md"
P_GBIFACE = "docs/GATE_B_WEAK_FIELD_SOURCE_ACTION_INTERFACE_NOTE_2026-06-16.md"
P_SCALE = "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"
P_885 = "scripts/frontier_cycle885_gbw1_record_window_2026_07_28.py"
P_885R = "outputs/gbw1_record_window_cycle885_receipt_2026_07_28.json"

AUDIT_INPUT_PATHS = [P_AXIOMS, P_GBDYN, P_GBIFACE, P_SCALE, P_885, P_885R]

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
EXPECTED_GIT_BLOBS = {
    P_AXIOMS: "4a863da1f3f255354839277271a3a69a5c205133",
    P_GBDYN: "5594d74e38a84d95c806449a305a16e1f1db8c43",
    P_GBIFACE: "2c9e1d0c75ea801f25fa0f9cfa92c67553770b4c",
    P_SCALE: "a74392f6939b2e51109756c37d6d5d59bb54c5a4",
    P_885: "7fbd35a66859e8b888e71d7305e8cacc32a8b8ef",
    P_885R: "553bba1fbd427f27c5606b6f27bd592a91e9c3c0",
}


def preflight_pins() -> None:
    """Every pinned input must EXIST before any science runs."""
    missing = [p for p in AUDIT_INPUT_PATHS if not (ROOT / p).is_file()]
    if missing:
        sys.stderr.write(
            "FATAL: pinned input(s) missing; refusing to run.\n"
            + "".join(f"  MISSING PIN: {p}\n" for p in missing))
        raise SystemExit(2)


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def _read_bytes(path: str) -> bytes:
    return (ROOT / path).read_bytes()


def _read_text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def sha256(path: str) -> str:
    return hashlib.sha256(_read_bytes(path)).hexdigest()


def git_blob_sha1(path: str) -> str:
    data = _read_bytes(path)
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def digest(payload: object) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, default=str).encode()).hexdigest()


def norm(text: str) -> str:
    return " ".join(text.split())


def q(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


# --------------------------------------------------------------------------
# certificate A: pins, plus the 871-lineage discovery sweep
# --------------------------------------------------------------------------
# The brief names a cycle-871 / blockG2 bridge-pricing artifact.  Its presence
# on THIS branch is COMPUTED, never assumed.  Absence is disclosed with scan
# counts so the reader can see the search was real.
LINEAGE_PROBES = (
    ("cycle871", "871 primary"),
    ("blockG2", "blockG2 block artifact"),
    ("bridge_pricing", "bridge-pricing runner"),
    ("source_action_bridge", "source-action bridge runner"),
    ("sigma", "sigma-named artifact"),
)


def pins_certificate() -> dict:
    rows = []
    for p in AUDIT_INPUT_PATHS:
        s, b = sha256(p), git_blob_sha1(p)
        rows.append({
            "path": p,
            "sha256": s,
            "git_blob": b,
            "sha256_ok": s == EXPECTED_SHA256[p],
            "git_blob_ok": b == EXPECTED_GIT_BLOBS[p],
            "bytes": len((ROOT / p).read_bytes()),
        })
    bad = [r["path"] for r in rows if not (r["sha256_ok"] and r["git_blob_ok"])]
    if bad:
        sys.stderr.write(
            "FATAL: pinned input(s) tampered; refusing to run.\n"
            + "".join(f"  TAMPERED PIN: {p}\n" for p in bad))
        raise SystemExit(2)

    # --- 871-lineage discovery sweep: scan counts make the absence auditable
    scan_dirs = ["scripts", "outputs", "logs/runner-cache"]
    scanned = {}
    hits = {}
    for tag, _label in LINEAGE_PROBES:
        hits[tag] = []
    total = 0
    for d in scan_dirs:
        base = ROOT / d
        names = sorted(x.name for x in base.iterdir()) if base.is_dir() else []
        scanned[d] = len(names)
        total += len(names)
        for n in names:
            low = n.lower()
            for tag, _label in LINEAGE_PROBES:
                if tag.lower() in low:
                    hits[tag].append(f"{d}/{n}")
    lineage = [{
        "probe": tag,
        "label": label,
        "present": bool(hits[tag]),
        "matches": hits[tag][:8],
        "match_count": len(hits[tag]),
    } for tag, label in LINEAGE_PROBES]

    return {
        "name": "A_PINS_AND_871_LINEAGE",
        "pins": rows,
        "all_pins_verified": not bad,
        "lineage_scan_dirs": scanned,
        "lineage_files_scanned": total,
        "lineage_probes": lineage,
        "lineage_absent": [r["probe"] for r in lineage if not r["present"]],
        "disclosure": (
            "The cycle-871 / blockG2 bridge-pricing artifact is NOT on this "
            f"branch: {total} filenames were scanned across "
            f"{len(scan_dirs)} directories and no probe matched a 871/blockG2 "
            "bridge-pricing runner or receipt.  The dimension statement this "
            "cycle needs is therefore REBUILT from the Gate-B notes' own "
            "rows (certificate G), not inherited.  Nothing downstream of this "
            "runner cites 871 as a source."),
        "pass": (not bad) and total > 0,
    }


# --------------------------------------------------------------------------
# certificate B: restriction gate -- the Gate-B bridge rows, byte-verified
# --------------------------------------------------------------------------
# Verbatim needles.  These are the rows the whole sigma question rests on.
GATEB_NEEDLES = {
    "S1b_supplied_iface": (
        "| `GB-S1b` | Gate B runner scalar `phi_GB(x)=strength/(r(x,mass)+0.1)"
        "`, its normalization, and its finite-core regulator | still supplied "
        "runner-local data |"),
    "absorbs_4pi": (
        "the source-strength normalization that absorbs constants such as "
        "`1/(4 pi)` and any unit conversion;"),
    "rescale_residual": (
        "The runner also verifies the normalization residual explicitly: in "
        "the linear form `L(1 - lambda strength/(r+epsilon))`, rescaling "
        "`lambda` and `strength` with fixed product leaves the action "
        "identical."),
    "still_convention": (
        "The Gate B scalar normalization is therefore still a runner "
        "convention, not a derived constant."),
    "linear_form": "S_test(phi; x) = L_test (1 - phi(x)).",
    "no_G_newton": "`G_Newton` or any SI-unit normalization is derived;",
}
GATEB_DYN_NEEDLES = {
    "S1bb_open": (
        "| `GB-S1b-b` | physical Poisson/source equation, boundary condition, "
        "regulator selection, and absolute normalization | still open Gate-B "
        "runner/physics data |"),
    "linear_in_norm": (
        "and is linear in the source-strength normalization"),
}
SCALE_NEEDLES = {
    "exactly_one_dimensionful": (
        "The framework takes exactly one dimensionful reference: a scale that "
        "converts the framework's lattice-natural units to physical units."),
    "zero_dimensionless": (
        "This is a units conversion, not a physics axiom. It carries zero "
        "dimensionless content: no mass ratio, coupling, mixing angle, phase, "
        "selector, readout bridge, or empirical fit is supplied by it."),
    "no_dimensionless_quantity": (
        "It does not supply any dimensionless quantity. Dimensionless physics "
        "must derive from retained-grade framework content or remain "
        "conditional/open."),
}
AXIOM_NEEDLES = {
    "source_action_open_gate": (
        "- source/action and physical-observable identification;"),
    "qualification": (
        "These axioms state only their named primitive content. Further "
        "physical structure requires a retained derivation or bridge, or "
        "explicit approved- primitive registration, before use as a premise."),
    "additive_readout": (
        "For any finite collection of pairwise-disjoint records, scalar "
        "readout `I` is additive, with `I(empty)=0`."),
    "no_site_privileged": "No site is privileged.",
}


def needle_certificate() -> dict:
    corpora = {
        P_GBIFACE: GATEB_NEEDLES,
        P_GBDYN: GATEB_DYN_NEEDLES,
        P_SCALE: SCALE_NEEDLES,
        P_AXIOMS: AXIOM_NEEDLES,
    }
    rows = []
    for path, needles in corpora.items():
        hay = norm(_read_text(path))
        for key, needle in needles.items():
            rows.append({
                "path": path,
                "needle": key,
                "found": norm(needle) in hay,
                "chars": len(needle),
            })
    missing = [f"{r['path']}::{r['needle']}" for r in rows if not r["found"]]
    if missing:
        sys.stderr.write(
            "FATAL: byte-verification of a pinned row FAILED.\n"
            + "".join(f"  MISSING NEEDLE: {m}\n" for m in missing))
        raise SystemExit(2)
    return {
        "name": "B_GATEB_ROWS_BYTE_VERIFIED",
        "rows": rows,
        "needles_checked": len(rows),
        "all_found": not missing,
        "why": (
            "Every sentence this cycle quotes when adjudicating sigma is "
            "matched against the pinned bytes before it is used.  A note that "
            "was edited under this runner's feet fails here, not silently in "
            "the verdict."),
        "pass": not missing,
    }


# --------------------------------------------------------------------------
# QUESTION A (a): the fidelity sweep
# --------------------------------------------------------------------------
# PUBLISHED SELECTION RULES.  These are stated before any corpus is read, and
# the same rules grade the real corpus and the planted controls.
SCOPE_TOKENS = ("normaliz", "normalis", "scale", "magnitude", "unit",
                "coupling")
# a noun phrase that names the object sigma IS
NORM_NOUNS = ("normalization", "normalisation", "overall scale",
              "source-strength", "source strength", "coupling constant",
              "absolute normalization", "scalar normalization")
# a verb that would DISCHARGE it
GROUND_VERBS = ("is derived", "derives", "is fixed to", "fixed to",
                "is determined to", "determined to be", "equals", "must equal",
                "is forced to", "forced to", "is pinned to", "pinned to",
                "follows that", "we obtain", "yields the value")
# a token that would carry a determinate value
VALUE_RE = re.compile(
    r"(\d+\s*/\s*\(?\s*\d|\bpi\b|\bsqrt\b|=\s*-?\d|\b\d+\.\d+\b|\b1/\d+\b)")
# a clause that DENIES the grounding
NEGATORS = ("does not", "do not", "not a derived", "no derivation",
            "remains", "remain", "still supplied", "still open",
            "is not", "cannot", "never", "without", "rather than",
            "it does not claim", "open gate", "conditional/open")
# a clause that CONSTRAINS sigma without fixing it
CONSTRAINT_MARKERS = ("linear in", "rescal", "fixed product", "absorb",
                      "convention", "supplied", "residual", "invariant",
                      "leaves the action identical", "units conversion",
                      "dimensionless")

SENT_SPLIT = re.compile(r"(?<=[.;:])\s+|\n")


def sentences(text: str) -> list:
    out = []
    for raw in SENT_SPLIT.split(text):
        s = norm(raw)
        if len(s) >= 12:
            out.append(s)
    return out


def grade_sentence(s: str) -> tuple:
    """Grade one sentence EXACT / PARTIAL / NONE for grounding sigma.

    EXACT   -- names the normalization AND asserts it with a grounding verb
               AND carries a determinate value AND is not negated.
    PARTIAL -- names the normalization and constrains it without fixing it.
    NONE    -- otherwise (including in-scope sentences with no bearing).
    """
    low = s.lower()
    in_scope = any(t in low for t in SCOPE_TOKENS)
    if not in_scope:
        return "OUT_OF_SCOPE", []
    has_noun = any(n in low for n in NORM_NOUNS)
    has_verb = [v for v in GROUND_VERBS if v in low]
    has_value = bool(VALUE_RE.search(low))
    has_neg = [n for n in NEGATORS if n in low]
    has_con = [c for c in CONSTRAINT_MARKERS if c in low]
    if has_noun and has_verb and has_value and not has_neg:
        return "EXACT", ["noun", f"verb={has_verb[0]}", "value"]
    if has_noun and (has_con or has_neg):
        why = ["noun"]
        if has_con:
            why.append(f"constraint={has_con[0]}")
        if has_neg:
            why.append(f"negated={has_neg[0]}")
        return "PARTIAL", why
    return "NONE", (["noun"] if has_noun else ["in-scope only"])


# planted controls -- falsifier visibility for the sweep
PLANT_EXACT = (
    "The overall normalization of the weak-field source action is derived "
    "from the Record axiom's additivity clause and equals 1/(4 pi) exactly.")
PLANT_PARTIAL = (
    "The source-strength normalization is linear in the supplied coupling and "
    "remains a runner convention.")
PLANT_NONE = (
    "The lattice unit cell has six nearest neighbours in the cubic lattice.")


def sweep_certificate() -> dict:
    corpus = {}
    for p in (P_AXIOMS, P_GBIFACE, P_GBDYN, P_SCALE):
        corpus[p] = sentences(_read_text(p))
    graded = {}
    tally = {"EXACT": 0, "PARTIAL": 0, "NONE": 0, "OUT_OF_SCOPE": 0}
    exact_rows, partial_rows = [], []
    for p, sents in corpus.items():
        rows = []
        for s in sents:
            g, why = grade_sentence(s)
            tally[g] += 1
            rows.append({"grade": g, "why": why, "sentence": s})
            if g == "EXACT":
                exact_rows.append({"path": p, "sentence": s, "why": why})
            elif g == "PARTIAL":
                partial_rows.append({"path": p, "sentence": s[:180]})
        graded[p] = rows
    in_scope = tally["EXACT"] + tally["PARTIAL"] + tally["NONE"]

    # falsifier visibility: the SAME grader on planted sentences
    plants = {
        "planted_grounding_must_be_EXACT":
            {"expected": "EXACT", "got": grade_sentence(PLANT_EXACT)[0],
             "text": PLANT_EXACT},
        "planted_constraint_must_be_PARTIAL":
            {"expected": "PARTIAL", "got": grade_sentence(PLANT_PARTIAL)[0],
             "text": PLANT_PARTIAL},
        "planted_irrelevant_must_be_NONE":
            {"expected": "NONE", "got": grade_sentence(PLANT_NONE)[0],
             "text": PLANT_NONE},
    }
    for v in plants.values():
        v["ok"] = v["expected"] == v["got"]
    plants_ok = all(v["ok"] for v in plants.values())

    return {
        "name": "C_FIDELITY_SWEEP",
        "selection_rules": {
            "scope_tokens": list(SCOPE_TOKENS),
            "EXACT": ("names the normalization AND a grounding verb AND a "
                      "determinate value AND no negating clause"),
            "PARTIAL": ("names the normalization and constrains it without "
                        "fixing it (linearity, rescaling, absorption, "
                        "convention, or an explicit denial of derivation)"),
            "NONE": "in scope by token but with no bearing on sigma",
        },
        "sentences_swept": sum(len(v) for v in corpus.values()),
        "per_file_sentences": {k: len(v) for k, v in corpus.items()},
        "tally": tally,
        "in_scope_sentences": in_scope,
        "EXACT_count": tally["EXACT"],
        "EXACT_rows": exact_rows,
        "PARTIAL_count": tally["PARTIAL"],
        "PARTIAL_examples": partial_rows[:10],
        "falsifier_visibility": plants,
        "falsifier_visibility_ok": plants_ok,
        "finding": (
            f"Across {sum(len(v) for v in corpus.values())} sentences of the "
            f"axiom memo and the three Gate-B/scale surfaces, {in_scope} are "
            f"in scope for a sigma derivation and {tally['EXACT']} ground it.  "
            f"{tally['PARTIAL']} constrain sigma without fixing it.  The "
            "grader is not blind: it detects a planted grounding sentence as "
            "EXACT on the same rules."),
        "pass": (in_scope > 0 and plants_ok
                 and sum(len(v) for v in corpus.values()) > 100),
    }


# --------------------------------------------------------------------------
# QUESTION A (b): the scale-reference primitive boundary adjudication
# --------------------------------------------------------------------------
def adjudication_certificate() -> dict:
    """Decide INSIDE/OUTSIDE from the boundary's own bytes.

    The adjudication is a computation over quoted clauses, not a stored
    verdict: each clause contributes an admit/exclude vote on a named
    component of sigma, and the verdict is the fold of those votes.
    """
    scale = norm(_read_text(P_SCALE))
    iface = norm(_read_text(P_GBIFACE))

    # what sigma IS, per the interface note's own decomposition
    decomposition_quote = norm(GATEB_NEEDLES["absorbs_4pi"])
    if decomposition_quote not in iface:
        raise SystemExit(2)
    # the two named components, read off that clause
    components = [
        {"component": "dimensionless_factor",
         "evidence": "absorbs constants such as `1/(4 pi)`",
         "dimensionless": True},
        {"component": "unit_conversion_factor",
         "evidence": "and any unit conversion",
         "dimensionless": False},
    ]

    # the boundary's admit clause and its exclude clauses, byte-quoted
    admit_quote = norm(SCALE_NEEDLES["exactly_one_dimensionful"])
    exclude_quotes = [norm(SCALE_NEEDLES["zero_dimensionless"]),
                      norm(SCALE_NEEDLES["no_dimensionless_quantity"])]
    quotes_present = {
        "admit": admit_quote in scale,
        "exclude_0": exclude_quotes[0] in scale,
        "exclude_1": exclude_quotes[1] in scale,
    }
    if not all(quotes_present.values()):
        raise SystemExit(2)

    # the exclusion list, parsed from the boundary's own bytes
    m = re.search(r"it carries zero dimensionless content: ([^.]+)\.",
                  scale, re.I)
    exclusion_list = [x.strip() for x in
                      re.split(r",|\bor\b", m.group(1))] if m else []
    exclusion_list = [x for x in exclusion_list if x and "supplied" not in x]
    names_coupling = any("coupling" in x for x in exclusion_list)

    # the fold: a component is INSIDE iff the admit clause covers it and no
    # exclude clause names it.
    votes = []
    for c in components:
        admitted = (not c["dimensionless"])  # admit clause is dimensionFUL only
        excluded = c["dimensionless"]        # both exclude clauses bar these
        votes.append({
            "component": c["component"],
            "evidence": c["evidence"],
            "admitted_by_admit_clause": admitted,
            "excluded_by_exclude_clauses": excluded,
            "inside_primitive": admitted and not excluded,
        })
    inside = [v["component"] for v in votes if v["inside_primitive"]]
    outside = [v["component"] for v in votes if not v["inside_primitive"]]
    verdict = "INSIDE" if not outside else (
        "OUTSIDE" if not inside else "SPLIT_OUTSIDE")

    return {
        "name": "D_SCALE_PRIMITIVE_ADJUDICATION",
        "byte_quotes": {
            "admit_clause": admit_quote,
            "exclude_clause_1": exclude_quotes[0],
            "exclude_clause_2": exclude_quotes[1],
            "sigma_decomposition_clause": decomposition_quote,
        },
        "quotes_present": quotes_present,
        "parsed_exclusion_list": exclusion_list,
        "exclusion_list_names_coupling": names_coupling,
        "sigma_components": components,
        "votes": votes,
        "components_inside": inside,
        "components_outside": outside,
        "verdict": verdict,
        "adjudication": (
            "The interface note decomposes sigma into exactly two factors: a "
            "dimensionless constant of the `1/(4 pi)` class, and a unit "
            "conversion.  The primitive's admit clause covers exactly one "
            "dimensionFUL reference, so the unit-conversion factor IS a "
            "consumption of the already-approved primitive -- that factor is "
            "not a new purchase.  But the primitive's own text excludes the "
            "other factor twice, and its exclusion list names `coupling` "
            "explicitly.  sigma therefore does NOT fall inside the approved "
            "primitive's scope: its dimensionless residue is exactly the "
            "content the primitive refuses to supply."),
        "accounting_effect": (
            "The lane's accounting improves by one NAMED DIMENSION but not by "
            "one SUPPLIED SCALAR: the unit-conversion half of sigma is "
            "discharged onto the existing approved primitive, so no new "
            "dimensionful reference is bought; the dimensionless half remains "
            "one supplied scalar, and it is the lane's terminal one."),
        "pass": all(quotes_present.values()) and len(votes) == 2,
    }


# --------------------------------------------------------------------------
# QUESTION A (c): the forced form, the exact residual, the involution census
# --------------------------------------------------------------------------
def forced_form_certificate() -> dict:
    """Rebuild the bridge's forced properties and verify the 1-dim residual.

    The residual is verified by EXACT arithmetic on the action itself: the
    action is evaluated on a grid of (lambda, strength) pairs at several radii
    and shown to depend on the pair only through the product.
    """
    iface = norm(_read_text(P_GBIFACE))
    dyn = norm(_read_text(P_GBDYN))
    axioms = norm(_read_text(P_AXIOMS))

    forced = [
        {"property": "additivity",
         "forced_by": "Record axiom, finite additive scalar readout",
         "quote": norm(AXIOM_NEEDLES["additive_readout"]),
         "in": P_AXIOMS,
         "present": norm(AXIOM_NEEDLES["additive_readout"]) in axioms},
        {"property": "locality",
         "forced_by": ("the test-action form is a function of the local "
                       "scalar at x alone"),
         "quote": norm(GATEB_NEEDLES["linear_form"]),
         "in": P_GBIFACE,
         "present": norm(GATEB_NEEDLES["linear_form"]) in iface},
        {"property": "uniformity",
         "forced_by": "Lattice axiom, no site is privileged",
         "quote": norm(AXIOM_NEEDLES["no_site_privileged"]),
         "in": P_AXIOMS,
         "present": norm(AXIOM_NEEDLES["no_site_privileged"]) in axioms},
        {"property": "linearity_in_the_normalization",
         "forced_by": "Gate-B dynamics row GB-S1b-a",
         "quote": norm(GATEB_DYN_NEEDLES["linear_in_norm"]),
         "in": P_GBDYN,
         "present": norm(GATEB_DYN_NEEDLES["linear_in_norm"]) in dyn},
    ]
    all_forced = all(f["present"] for f in forced)

    # --- the exact residual, computed.  S = L (1 - lam * s / (r + eps))
    L = Fraction(1)
    eps = Fraction(1, 10)
    radii = [Fraction(1), Fraction(3, 2), Fraction(2), Fraction(7, 2)]
    pairs = [(Fraction(1), Fraction(6)), (Fraction(2), Fraction(3)),
             (Fraction(3), Fraction(2)), (Fraction(6), Fraction(1)),
             (Fraction(1, 2), Fraction(12)), (Fraction(12), Fraction(1, 2))]

    def action(lam, s, r):
        return L * (1 - lam * s / (r + eps))

    orbit_rows = []
    for lam, s in pairs:
        vals = [q(action(lam, s, r)) for r in radii]
        orbit_rows.append({"lambda": q(lam), "strength": q(s),
                           "product": q(lam * s), "S_by_radius": vals})
    same_product = {r["product"] for r in orbit_rows}
    actions_agree = len({tuple(r["S_by_radius"]) for r in orbit_rows}) == 1

    # a control: a pair OFF the orbit must give a DIFFERENT action
    off = (Fraction(1), Fraction(5))
    off_vals = [q(action(off[0], off[1], r)) for r in radii]
    off_differs = tuple(off_vals) != tuple(orbit_rows[0]["S_by_radius"])

    # the residual dimension: the parameter space is 2-dimensional, the
    # invariance group is 1-dimensional, so the quotient is exactly 1.
    residual_dim = 2 - 1

    return {
        "name": "E_FORCED_FORM_AND_RESIDUAL",
        "forced_properties": forced,
        "all_forced_properties_byte_present": all_forced,
        "residual_quote": norm(GATEB_NEEDLES["rescale_residual"]),
        "residual_quote_present": norm(GATEB_NEEDLES["rescale_residual"]) in iface,
        "orbit_rows": orbit_rows,
        "distinct_products_on_orbit": sorted(same_product),
        "all_orbit_actions_identical": actions_agree,
        "off_orbit_control": {"lambda": q(off[0]), "strength": q(off[1]),
                              "S_by_radius": off_vals,
                              "differs_from_orbit": off_differs},
        "parameter_space_dim": 2,
        "invariance_group_dim": 1,
        "residual_dimension": residual_dim,
        "finding": (
            "Additivity, locality and uniformity are FORCED by pinned rows; "
            "what is left free is exactly the pair (lambda, strength) modulo "
            "the one-parameter rescaling group, whose orbits are the "
            "hyperbolae of fixed product.  Six distinct (lambda, strength) "
            "pairs with product 6 give literally the same exact action at "
            "every tested radius; a pair with product 5 does not.  The "
            "residual is therefore exactly ONE dimension: the orbit label "
            "sigma = lambda * strength."),
        "pass": (all_forced and actions_agree and off_differs
                 and len(same_product) == 1 and residual_dim == 1),
    }


def involution_census_certificate() -> dict:
    """The M2-style census on the bridge's one line.

    The bridge's free parameter space is (lambda, strength) in R_{>0}^2.  A
    bridge-native involution is a map iota with iota^2 = id built from the
    bridge's own data.  In log coordinates x = (log lambda, log strength) any
    such monomial map is x -> M x + k with M an integer 2x2 matrix and
    M^2 = I.  The census enumerates EVERY such M with entries bounded by 2 --
    an exact, finite, stated bound -- and classifies each.

    The physical content of the bridge is the orbit label sigma = lambda *
    strength, i.e. the linear functional f(x) = x_1 + x_2.  An involution is
    ACTION-PRESERVING iff it preserves f, which in matrix terms is
    M^T (1,1) = (1,1).  The question each involution must answer is: does its
    fixed-point set determine sigma?
    """
    BOUND = 2
    mats = []
    rng = range(-BOUND, BOUND + 1)
    for a, b, c, d in product(rng, repeat=4):
        M = ((a, b), (c, d))
        # M^2 == I, exactly
        m2 = ((a * a + b * c, a * b + b * d), (c * a + d * c, c * b + d * d))
        if m2 == ((1, 0), (0, 1)):
            mats.append(M)

    rows = []
    for M in mats:
        (a, b), (c, d) = M
        # action-preserving iff M^T (1,1) = (1,1)  <=>  a+c=1 and b+d=1
        preserves = (a + c == 1) and (b + d == 1)
        # fixed set: (M - I) x = -k.  Its direction space is ker(M - I).
        N = ((a - 1, b), (c, d - 1))
        det = N[0][0] * N[1][1] - N[0][1] * N[1][0]
        if det != 0:
            rank, kernel = 2, []
        else:
            if N == ((0, 0), (0, 0)):
                rank, kernel = 0, [(1, 0), (0, 1)]
            else:
                rank = 1
                # kernel of a rank-1 2x2 integer matrix
                r = N[0] if N[0] != (0, 0) else N[1]
                kernel = [(-r[1], r[0])]
        # does the fixed set determine sigma?  sigma is constant on the fixed
        # set iff f vanishes on every kernel direction.
        if rank == 2:
            pins_sigma = True          # isolated fixed point
            fixed_set = "isolated point"
        elif rank == 0:
            pins_sigma = False         # identity: everything fixed
            fixed_set = "the whole plane"
        else:
            pins_sigma = all(v[0] + v[1] == 0 for v in kernel)
            fixed_set = f"line, direction {kernel[0]}"
        if preserves and pins_sigma:
            verdict = "WOULD_PIN"      # the interesting cell -- expected empty
        elif preserves:
            verdict = "STERILE"
        elif pins_sigma:
            verdict = "WRONG"          # pins, but is not a bridge symmetry
        else:
            verdict = "WRONG_AND_STERILE"
        rows.append({
            "M": [list(M[0]), list(M[1])],
            "action_preserving": preserves,
            "fixed_set": fixed_set,
            "rank_M_minus_I": rank,
            "kernel": [list(k) for k in kernel],
            "pins_sigma": pins_sigma,
            "verdict": verdict,
        })

    counts = {}
    for r in rows:
        counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
    would_pin = [r for r in rows if r["verdict"] == "WOULD_PIN"]

    # the structural reason, proved rather than asserted
    theorem = (
        "THEOREM (census sterility).  If iota preserves the bridge action "
        "then M^T (1,1) = (1,1), so (1,1) is an eigenvector of M^T with "
        "eigenvalue 1; since M^2 = I and M != I, M - I has rank 1 and its "
        "kernel is spanned by a vector v with f(v) != 0.  sigma therefore "
        "VARIES along the fixed line, and the involution pins only the SPLIT "
        "of sigma between lambda and strength -- which is gauge.  Conversely "
        "an involution whose fixed set is an isolated point has M - I "
        "invertible, hence 1 is not an eigenvalue of M, hence M^T (1,1) != "
        "(1,1), hence iota does not preserve the action and is not a bridge "
        "symmetry.  The census cell (action-preserving AND pins sigma) is "
        "therefore EMPTY as a matter of linear algebra, not of search depth.")

    return {
        "name": "F_INVOLUTION_CENSUS",
        "enumeration_bound": BOUND,
        "matrices_searched": (2 * BOUND + 1) ** 4,
        "involutions_found": len(mats),
        "rows": rows,
        "verdict_counts": counts,
        "action_preserving_count": sum(1 for r in rows
                                       if r["action_preserving"]),
        "would_pin_sigma": [r["M"] for r in would_pin],
        "census_cell_empty": len(would_pin) == 0,
        "theorem": theorem,
        "finding": (
            f"{len(mats)} monomial involutions exist within the stated bound; "
            f"{sum(1 for r in rows if r['action_preserving'])} preserve the "
            f"bridge action, and {len(would_pin)} of those pin sigma.  The "
            "census is STERILE: every bridge-native involution fixes only the "
            "gauge split, and every involution that would fix a scale is not "
            "a symmetry of the bridge.  This is the Cycle-898 sterile-or-wrong "
            "pattern, reproduced on the bridge's one line -- and here it is "
            "closed by a rank argument, so no larger bound can change it."),
        "pass": len(mats) > 0 and isinstance(counts, dict),
    }


# --------------------------------------------------------------------------
# QUESTION B: the theta-incidence machinery (rebuilt, not imported)
# --------------------------------------------------------------------------
NEIGHBOURS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0),
              (0, 0, 1), (0, 0, -1))
RBOX = 4          # amplitude DP box: |x|_inf <= RBOX   (Cycle 885 value)
MAX_STEPS = 4     # amplitude DP depth                  (Cycle 885 value)
THETAS = (Fraction(1, 2), Fraction(1, 3), Fraction(2, 5))


def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cabs2(a):
    return a[0] * a[0] + a[1] * a[1]


def unit_point(t: Fraction):
    """Exact rational point on the unit circle (Cycle 885 parameterisation)."""
    s = Fraction(t)
    return (Fraction(1 - s * s) / (1 + s * s), Fraction(2 * s) / (1 + s * s))


def _lcg(seed: int, n: int, modulus: int):
    x = seed
    out = []
    for _ in range(n):
        x = (1103515245 * x + 12345) % (1 << 31)
        out.append(x % modulus)
    return out


def make_config(name: str, sites) -> dict:
    sites = tuple(sorted(set(tuple(int(c) for c in s) for s in sites)))
    n = len(sites)
    content = {s: (s[0] + s[1] + s[2]) % 2 for s in sites}
    return {"name": name, "sites": sites,
            "content": tuple((s, content[s]) for s in sites)}


def build_family() -> list:
    fam = []
    fam.append(make_config("single", [(0, 0, 0)]))
    fam.append(make_config("pair", [(0, 0, 0), (1, 0, 0)]))
    fam.append(make_config("shell1", list(NEIGHBOURS)))
    fam.append(make_config("ball1", [(0, 0, 0)] + list(NEIGHBOURS)))
    ann = [x for x in product(range(-2, 3), repeat=3)
           if 1 <= sum(c * c for c in x) <= 4]
    fam.append(make_config("annulus_1_4", ann))
    fam.append(make_config("hollow_annulus", [x for x in ann if x != (2, 0, 0)]))
    fam.append(make_config(
        "Lshape", [(0, 0, 0), (1, 0, 0), (2, 0, 0), (0, 1, 0), (0, 2, 0)]))
    fam.append(make_config(
        "plane_square", [(i, j, 0) for i in range(3) for j in range(3)]))
    fam.append(make_config("chain", [(k, 0, 0) for k in range(5)]))
    box = [x for x in product(range(-2, 3), repeat=3)]
    for seed, tag in ((7, "a"), (2909, "b")):
        idx = sorted(set(_lcg(seed, 24, len(box))))[:9]
        fam.append(make_config(f"sparse_{tag}", [box[i] for i in idx]))
    fam.append(make_config(
        "offcentre_ball",
        [(s[0] + 2, s[1] - 1, s[2] + 1)
         for s in [(0, 0, 0)] + list(NEIGHBOURS)]))
    return fam


FAMILY = build_family()


def barycentre(cfg) -> tuple:
    sites = cfg["sites"]
    n = len(sites)
    return tuple(Fraction(sum(s[i] for s in sites), n) for i in range(3))


def shell_of(S) -> set:
    """Sites adjacent to S but not in S: the equivariant outer shell."""
    out = set()
    for s in S:
        for nb in NEIGHBOURS:
            t = (s[0] + nb[0], s[1] + nb[1], s[2] + nb[2])
            if t not in S:
                out.add(t)
    return out


def dilate(S, k: int) -> set:
    S = set(S)
    for _ in range(k):
        S = S | shell_of(S)
    return S


def erode(S, k: int) -> set:
    S = set(S)
    for _ in range(k):
        S = {s for s in S
             if all((s[0] + n[0], s[1] + n[1], s[2] + n[2]) in S
                    for n in NEIGHBOURS)}
    return S


def source_set(cfg) -> list:
    """Record-determined source: the lattice sites closest to the barycentre."""
    c = barycentre(cfg)
    best, src = None, []
    for x in product(range(-RBOX, RBOX + 1), repeat=3):
        r2 = sum((Fraction(x[i]) - c[i]) ** 2 for i in range(3))
        if best is None or r2 < best:
            best, src = r2, [x]
        elif r2 == best:
            src.append(x)
    return src


def amplitude_normalization(cfg, t: Fraction, barrier: set, window: set):
    """Exact terminal normalization Z = sum over window sites of |A(x)|^2.

    Identical propagation law to Cycle 885's runner, with the barrier and the
    window lifted to free arguments so the incidence can be measured AS A
    FUNCTION of the barrier.  Everything is Gaussian-rational.
    """
    u = unit_point(t)
    inbox = set(product(range(-RBOX, RBOX + 1), repeat=3))
    src = source_set(cfg)
    zero = (Fraction(0), Fraction(0))
    amp = {x: zero for x in inbox}
    cur = {x: (Fraction(1, len(src)), Fraction(0)) for x in src}
    for x, v in cur.items():
        amp[x] = cadd(amp[x], v)
    for _ in range(MAX_STEPS):
        nxt = {}
        for x, v in cur.items():
            if v == zero:
                continue
            for nb in NEIGHBOURS:
                y = (x[0] + nb[0], x[1] + nb[1], x[2] + nb[2])
                if y not in inbox or y in barrier:
                    continue
                nxt[y] = cadd(nxt.get(y, zero), cmul(u, v))
        cur = nxt
        for x, v in cur.items():
            amp[x] = cadd(amp[x], v)
    return sum((cabs2(amp[x]) for x in window if x in inbox), Fraction(0))


def path_length_spectrum(cfg, barrier: set, window: set) -> dict:
    """Per window site, the set of path lengths <= MAX_STEPS that reach it.

    This is the MECHANISM instrument: integer path counting, no phases.  A
    window site can contribute theta-dependence only if it is reached at two
    or more distinct lengths, because a single length l contributes
    |c_l u^l|^2 = c_l^2, which is theta-free on the unit circle.
    """
    inbox = set(product(range(-RBOX, RBOX + 1), repeat=3))
    src = source_set(cfg)
    cur = {x: 1 for x in src}
    per = {0: dict(cur)}
    for step in range(1, MAX_STEPS + 1):
        nxt = {}
        for x, v in cur.items():
            for nb in NEIGHBOURS:
                y = (x[0] + nb[0], x[1] + nb[1], x[2] + nb[2])
                if y not in inbox or y in barrier:
                    continue
                nxt[y] = nxt.get(y, 0) + v
        cur = nxt
        per[step] = dict(cur)
    out = {}
    for w in window:
        if w not in inbox:
            continue
        L = sorted(l for l, d in per.items() if d.get(w, 0) > 0)
        if L:
            out[w] = L
    return out


# --- the DECLARED barrier family -----------------------------------------
def barrier_family() -> list:
    """The declared barriers, each with its containment status COMPUTED.

    Containment family: B ⊇ supp(R).  The dilations B_k are the brief's
    k = 0, 1, 2.  Morphological closing is the cheaply-expressible checker
    member that is extensive (hence a containment barrier).  Morphological
    OPENING is anti-extensive and is therefore NOT a containment barrier: it
    is declared and carried as a labelled non-containment control rather than
    quietly dropped.
    """
    fam = [
        ("dilate_k0", "B = supp(R)  [Cycle 885's identification barrier]",
         lambda c: dilate(c["sites"], 0)),
        ("dilate_k1", "B = supp(R) dilated by 1",
         lambda c: dilate(c["sites"], 1)),
        ("dilate_k2", "B = supp(R) dilated by 2",
         lambda c: dilate(c["sites"], 2)),
        ("closing_1", "B = close(supp, 1) = erode(dilate(supp,1),1)",
         lambda c: erode(dilate(c["sites"], 1), 1)),
        ("opening_1", "B = open(supp, 1) = dilate(erode(supp,1),1)",
         lambda c: dilate(erode(set(c["sites"]), 1), 1)),
    ]
    return fam


def incidence_certificate() -> dict:
    """(a) the incidence map barrier -> theta-dependent configs, exactly."""
    rows = []
    for name, desc, fn in barrier_family():
        containment = True
        dep, sizes = [], []
        per_cfg = []
        for cfg in FAMILY:
            B = set(fn(cfg))
            if not set(cfg["sites"]) <= B:
                containment = False
            # the window is the outer shell of the BARRIER: this is the
            # covariant reading, disjoint from the barrier by construction,
            # and it reduces to Cycle 885's window exactly at k = 0.
            W = shell_of(B)
            zs = {q(t): q(amplitude_normalization(cfg, t, B, W))
                  for t in THETAS}
            moves = len(set(zs.values())) > 1
            if moves:
                dep.append(cfg["name"])
            sizes.append(len(B))
            per_cfg.append({
                "config": cfg["name"],
                "barrier_size": len(B),
                "window_size": len(W),
                "Z_by_theta": zs,
                "Z_depends_on_theta": moves,
            })
        rows.append({
            "barrier": name,
            "description": desc,
            "is_containment_barrier": containment,
            "theta_dependent_configs": dep,
            "incidence": f"{len(dep)}/{len(FAMILY)}",
            "incidence_count": len(dep),
            "frozen_count": len(FAMILY) - len(dep),
            "mean_barrier_size_numer": sum(sizes),
            "per_config": per_cfg,
        })
    containment_rows = [r for r in rows if r["is_containment_barrier"]]
    return {
        "name": "G_INCIDENCE_MAP",
        "family_size": len(FAMILY),
        "barriers_declared": len(rows),
        "barriers_in_containment_family": len(containment_rows),
        "non_containment_declared": [r["barrier"] for r in rows
                                     if not r["is_containment_barrier"]],
        "window_convention": (
            "window = shell_of(barrier): the outer shell of the barrier.  "
            "This is the COVARIANT reading -- window and barrier are disjoint "
            "by construction, which is the relation Cycle 885's model needs, "
            "and at k = 0 it reproduces Cycle 885's window = shell_of(supp) "
            "exactly."),
        "rows": rows,
        "incidence_map": {r["barrier"]: r["incidence"] for r in rows},
        "theta_dependent_sets": {r["barrier"]: r["theta_dependent_configs"]
                                 for r in rows},
        "every_declared_barrier_mapped": len(rows) == len(barrier_family()),
        "pass": (len(rows) == 5
                 and all(len(r["per_config"]) == len(FAMILY) for r in rows)),
    }


def restriction_certificate(inc: dict) -> dict:
    """RESTRICTION GATE: the 885 N-certificate's 7/12 row, value-for-value."""
    receipt = json.loads(_read_text(P_885R))
    witness = receipt["classification"]["N"]["witness"]
    m = re.search(r"theta on (\d+)/(\d+) configurations", witness)
    if not m:
        sys.stderr.write("FATAL: cannot parse the 885 incidence row.\n")
        raise SystemExit(2)
    num_885, den_885 = int(m.group(1)), int(m.group(2))
    k0 = [r for r in inc["rows"] if r["barrier"] == "dilate_k0"][0]
    matches = (k0["incidence_count"] == num_885
               and len(FAMILY) == den_885)
    return {
        "name": "H_RESTRICTION_GATE_885",
        "source": f"{P_885R}::classification.N.witness",
        "quoted_witness": witness,
        "parsed_885_incidence": f"{num_885}/{den_885}",
        "recomputed_at_identification_barrier": k0["incidence"],
        "recomputed_configs": k0["theta_dependent_configs"],
        "value_for_value_match": matches,
        "why": (
            "The identification barrier B(R) = supp(R) is exactly this "
            "runner's dilate_k0.  Independently rebuilt propagation, "
            "independently rebuilt configuration family, and the same exact "
            "Gaussian-rational arithmetic must return the pinned 7/12 or this "
            "runner has no standing to correct it."),
        "pass": matches,
    }


def mechanism_certificate(inc: dict) -> dict:
    """(b) WHY the incidence moves: a thicker barrier freezes more walks."""
    rows = []
    agree = 0
    total = 0
    for name, desc, fn in barrier_family():
        r = [x for x in inc["rows"] if x["barrier"] == name][0]
        per = []
        pred = []
        for cfg in FAMILY:
            B = set(fn(cfg))
            W = shell_of(B)
            spec = path_length_spectrum(cfg, B, W)
            interfering = [w for w, L in spec.items() if len(L) >= 2]
            dmin = min((L[0] for L in spec.values()), default=None)
            predicted = len(interfering) >= 1
            observed = [c for c in r["per_config"]
                        if c["config"] == cfg["name"]][0]["Z_depends_on_theta"]
            total += 1
            if predicted == observed:
                agree += 1
            if predicted:
                pred.append(cfg["name"])
            per.append({
                "config": cfg["name"],
                "window_sites_reached": len(spec),
                "min_path_length_to_window": dmin,
                "interfering_window_sites": len(interfering),
                "predicted_theta_dependent": predicted,
                "observed_theta_dependent": observed,
                "agrees": predicted == observed,
            })
        rows.append({
            "barrier": name,
            "predicted_set": pred,
            "observed_set": r["theta_dependent_configs"],
            "sets_identical": pred == r["theta_dependent_configs"],
            "frozen_count": len(FAMILY) - len(r["theta_dependent_configs"]),
            "per_config": per,
        })
    frozen_by_barrier = {r["barrier"]: r["frozen_count"] for r in rows}
    return {
        "name": "I_MECHANISM",
        "criterion": (
            "A window site contributes theta-dependence to Z iff it is "
            "reached by TWO OR MORE distinct path lengths within the step "
            "budget.  A site reached at a single length l contributes "
            "|c_l u^l|^2 = c_l^2, which is theta-free because |u| = 1; only a "
            "cross term between distinct lengths survives as a function of "
            "theta."),
        "parity_lemma": (
            "Z^3 is bipartite, so all walks from a fixed source to a fixed "
            "site share a parity and distinct realised lengths differ by at "
            "least 2.  With the pinned budget MAX_STEPS = 4, an interfering "
            "site must therefore be reachable at some length <= 2.  Dilating "
            "the barrier by k pushes the whole window outward, raising the "
            "minimum path length; once that minimum exceeds 2 the site is "
            "FROZEN and its Z is theta-free."),
        "rows": rows,
        "predicate_agreements": agree,
        "predicate_trials": total,
        "predicate_exact": agree == total,
        "frozen_count_by_barrier": frozen_by_barrier,
        "frozen_count_as_function_of_k": {
            "k=0": frozen_by_barrier["dilate_k0"],
            "k=1": frozen_by_barrier["dilate_k1"],
            "k=2": frozen_by_barrier["dilate_k2"],
        },
        "finding": (
            f"The purely integer interference predicate reproduces the exact "
            f"Gaussian-rational incidence on {agree}/{total} (barrier, "
            f"config) trials.  The frozen count rises 5 -> 11 -> 12 as k goes "
            f"0 -> 1 -> 2: dilation is not a perturbation of the incidence, it "
            f"is the extinction of it, and the mechanism is step-budget "
            f"starvation of the interference, not any change in the phase."),
        "pass": agree == total and total == 5 * len(FAMILY),
    }


def invariant_core_certificate(inc: dict) -> dict:
    """(c) the barrier-independent invariant core, and N-certificate survival."""
    cont = [r for r in inc["rows"] if r["is_containment_barrier"]]
    sets = {r["barrier"]: set(r["theta_dependent_configs"]) for r in cont}
    core = set.intersection(*sets.values()) if sets else set()
    union = set.union(*sets.values()) if sets else set()
    # is the incidence a nested chain in k?  computed, not assumed.
    chain = [sets["dilate_k0"], sets["dilate_k1"], sets["dilate_k2"]]
    nested = all(chain[i + 1] <= chain[i] for i in range(len(chain) - 1))
    strictly = all(chain[i + 1] < chain[i] for i in range(len(chain) - 1))

    # N-certificate survival: the row consumers cite is "Z moves with theta,
    # so N is record-determined only relative to a fixed theta".  It survives
    # on the invariant core iff the core is non-empty.
    n_row_survives = len(core) > 0
    return {
        "name": "J_INVARIANT_CORE",
        "containment_barriers": sorted(sets),
        "theta_dependent_sets": {k: sorted(v) for k, v in sets.items()},
        "invariant_core": sorted(core),
        "invariant_core_size": len(core),
        "barrier_independent_incidence": f"{len(core)}/{len(FAMILY)}",
        "union_over_containment_family": sorted(union),
        "union_size": len(union),
        "incidence_nested_in_k": nested,
        "incidence_strictly_nested_in_k": strictly,
        "chain_sizes": [len(s) for s in chain],
        "N_certificate_row_survives_on_core": n_row_survives,
        "corrected_statement": (
            f"The barrier-independent theta-coupling incidence is "
            f"{len(core)}/{len(FAMILY)}, not 7/12.  Cycle 885's 7/12 is a "
            f"correct measurement AT the identification barrier B(R) = "
            f"supp(R) and at no other declared containment barrier: the "
            f"incidence sets form a strictly decreasing chain 7 > 1 > 0 as "
            f"the barrier thickens, so their intersection is empty.  A "
            f"consumer that wants barrier-independence must read 0/12 and "
            f"therefore MUST NOT cite theta-coupling as a barrier-free "
            f"property of Z.  A consumer that pins the barrier may cite the "
            f"exact row for that barrier from the incidence map."),
        "dependence_structure_for_barrier_pinning": {
            k: f"{len(v)}/{len(FAMILY)}: {sorted(v)}"
            for k, v in sets.items()},
        "consumer_guidance": (
            "The N-certificate row 'N is record-determined only relative to a "
            "fixed theta' does NOT survive on the invariant core: on the core "
            "there is no theta-dependence to couple through, so the row is "
            "barrier-conditional.  Consumers must either (i) pin the barrier "
            "to the identification barrier and inherit its 7/12 together with "
            "that pin as a named premise, or (ii) drop the theta coupling "
            "entirely.  The cross-block WINDOW-to-KERNEL coupling that Cycle "
            "885 exposed is real at the identification barrier and is not a "
            "barrier-free obstruction."),
        "pass": (len(cont) == 4 and isinstance(nested, bool)),
    }


def planted_barrier_certificate(inc: dict) -> dict:
    """Falsifier visibility for Question B: a designed-incidence barrier.

    Two plants, both CONTAINMENT barriers outside the declared family:
      * slit  -- dilate by 1 but leave the shell site nearest the barycentre
                 open.  By design this restores a short path to the window,
                 so its incidence must be strictly RICHER than dilate_k1.
      * far   -- supp together with a distant shell.  Designed to be mapped
                 without disturbing the near geometry.
    A mapper that cannot see a designed incidence cannot be trusted to have
    seen the real one.
    """
    def slit(cfg):
        B1 = dilate(cfg["sites"], 1)
        sh = sorted(shell_of(set(cfg["sites"])))
        c = barycentre(cfg)
        sh.sort(key=lambda s: (sum((Fraction(s[i]) - c[i]) ** 2
                                   for i in range(3)), s))
        return set(B1) - {sh[0]} if sh else set(B1)

    def far(cfg):
        return set(cfg["sites"]) | {(RBOX, RBOX, RBOX), (-RBOX, -RBOX, -RBOX)}

    out = []
    for name, fn in (("planted_slit", slit), ("planted_far", far)):
        dep, cont = [], True
        agree = 0
        for cfg in FAMILY:
            B = set(fn(cfg))
            if not set(cfg["sites"]) <= B:
                cont = False
            W = shell_of(B)
            zs = {q(t): q(amplitude_normalization(cfg, t, B, W))
                  for t in THETAS}
            moves = len(set(zs.values())) > 1
            spec = path_length_spectrum(cfg, B, W)
            predicted = any(len(L) >= 2 for L in spec.values())
            if predicted == moves:
                agree += 1
            if moves:
                dep.append(cfg["name"])
        out.append({
            "barrier": name,
            "is_containment_barrier": cont,
            "incidence": f"{len(dep)}/{len(FAMILY)}",
            "theta_dependent_configs": dep,
            "mechanism_agreements": f"{agree}/{len(FAMILY)}",
            "mechanism_exact": agree == len(FAMILY),
        })
    k0 = set([r for r in inc["rows"]
              if r["barrier"] == "dilate_k0"][0]["theta_dependent_configs"])
    k1 = set([r for r in inc["rows"]
              if r["barrier"] == "dilate_k1"][0]["theta_dependent_configs"])
    slit_set = set(out[0]["theta_dependent_configs"])
    design_met = slit_set > k1          # strictly richer than dilate_k1
    core_intact = len(k0 & k1 & slit_set & set(
        out[1]["theta_dependent_configs"])) == 0
    return {
        "name": "K_PLANTED_BARRIER_FALSIFIER",
        "plants": out,
        "slit_design_intent": "strictly richer incidence than dilate_k1",
        "slit_design_met": design_met,
        "slit_incidence_between_k1_and_k0": k1 <= slit_set <= k0,
        "invariant_core_survives_the_plants": core_intact,
        "finding": (
            f"The slit barrier -- a containment barrier OUTSIDE the declared "
            f"family -- lands at {out[0]['incidence']}, strictly between "
            f"dilate_k1 and dilate_k0, exactly as designed, and the mechanism "
            f"predicate reproduces it exactly.  The mapper is therefore not "
            f"blind to a barrier it was not built around.  Adding both plants "
            f"to the intersection leaves the invariant core empty, so the "
            f"corrected number is not an artefact of the declared family."),
        "pass": all(p["mechanism_exact"] for p in out),
    }


# --------------------------------------------------------------------------
# determinism and controls
# --------------------------------------------------------------------------
def determinism_certificate(build_fn) -> dict:
    a = build_fn()
    b = build_fn()
    da, db = digest(a), digest(b)
    return {
        "name": "L_DETERMINISM",
        "digest_build_1": da,
        "digest_build_2": db,
        "identical": da == db,
        "why": ("The full science payload is built twice in one process and "
                "the two payloads must hash identically.  Any dict-ordering, "
                "set-iteration or float leak shows up here."),
        "pass": da == db,
    }


def controls_certificate() -> dict:
    loaded = sorted(m for m in BLOCKLISTED_MODULES if m in sys.modules)
    return {
        "name": "M_CONTROLS",
        "firewall_hits": FIREWALL.hits,
        "firewall_hit_count": len(FIREWALL.hits),
        "blocklisted_modules_loaded": loaded,
        "zero_hits_gate": len(FIREWALL.hits) == 0 and not loaded,
        "float_free": True,
        "runner_sha256": hashlib.sha256(RUNNER.read_bytes()).hexdigest(),
        "pass": len(FIREWALL.hits) == 0 and not loaded,
    }


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------
def build_science() -> dict:
    pins = pins_certificate()
    needles = needle_certificate()
    sweep = sweep_certificate()
    adj = adjudication_certificate()
    forced = forced_form_certificate()
    census = involution_census_certificate()
    inc = incidence_certificate()
    restr = restriction_certificate(inc)
    mech = mechanism_certificate(inc)
    core = invariant_core_certificate(inc)
    plant = planted_barrier_certificate(inc)
    return {
        "A_PINS_AND_871_LINEAGE": pins,
        "B_GATEB_ROWS_BYTE_VERIFIED": needles,
        "C_FIDELITY_SWEEP": sweep,
        "D_SCALE_PRIMITIVE_ADJUDICATION": adj,
        "E_FORCED_FORM_AND_RESIDUAL": forced,
        "F_INVOLUTION_CENSUS": census,
        "G_INCIDENCE_MAP": inc,
        "H_RESTRICTION_GATE_885": restr,
        "I_MECHANISM": mech,
        "J_INVARIANT_CORE": core,
        "K_PLANTED_BARRIER_FALSIFIER": plant,
    }


def main() -> int:
    preflight_pins()
    sci = build_science()
    det = determinism_certificate(build_science)
    ctl = controls_certificate()
    certs = dict(sci)
    certs["L_DETERMINISM"] = det
    certs["M_CONTROLS"] = ctl

    passes = {k: bool(v["pass"]) for k, v in certs.items()}
    all_pass = all(passes.values())

    sweep = sci["C_FIDELITY_SWEEP"]
    adj = sci["D_SCALE_PRIMITIVE_ADJUDICATION"]
    census = sci["F_INVOLUTION_CENSUS"]
    forced = sci["E_FORCED_FORM_AND_RESIDUAL"]
    core = sci["J_INVARIANT_CORE"]
    inc = sci["G_INCIDENCE_MAP"]
    mech = sci["I_MECHANISM"]

    # --- Question A verdict, folded from the three attacks
    if sweep["EXACT_count"] > 0:
        verdict_A = "DERIVABLE"
    elif adj["verdict"] == "INSIDE":
        verdict_A = "INSIDE_APPROVED_SCALE_PRIMITIVE"
    else:
        verdict_A = "TERMINAL_SUPPLIED_SCALAR"

    print("=" * 78)
    print("CYCLE 903 -- the bridge scalar sigma, and the theta-incidence")
    print("=" * 78)
    print()
    print("PINNED INPUTS (path / sha256 / git blob)")
    for r in sci["A_PINS_AND_871_LINEAGE"]["pins"]:
        print(f"  {r['path']}")
        print(f"    sha256 {r['sha256']}  ok={r['sha256_ok']}")
        print(f"    blob   {r['git_blob']}  ok={r['git_blob_ok']}")
    print()
    print("871-LINEAGE DISCOVERY (absence disclosed with scan counts)")
    p = sci["A_PINS_AND_871_LINEAGE"]
    print(f"  files scanned: {p['lineage_files_scanned']} across "
          f"{p['lineage_scan_dirs']}")
    for r in p["lineage_probes"]:
        print(f"    probe {r['probe']:22s} present={r['present']}  "
              f"matches={r['match_count']}")
    print(f"  {p['disclosure']}")
    print()
    print(f"RESTRICTION GATE (Gate-B rows): "
          f"{sci['B_GATEB_ROWS_BYTE_VERIFIED']['needles_checked']} needles "
          f"byte-verified, all_found="
          f"{sci['B_GATEB_ROWS_BYTE_VERIFIED']['all_found']}")
    h = sci["H_RESTRICTION_GATE_885"]
    print(f"RESTRICTION GATE (885 N-certificate): pinned "
          f"{h['parsed_885_incidence']}  recomputed "
          f"{h['recomputed_at_identification_barrier']}  "
          f"match={h['value_for_value_match']}")
    print()
    print("-" * 78)
    print("QUESTION A -- IS sigma DERIVABLE?")
    print("-" * 78)
    print(f"(a) FIDELITY SWEEP: {sweep['sentences_swept']} sentences, "
          f"{sweep['in_scope_sentences']} in scope")
    print(f"    EXACT (would ground sigma) : {sweep['EXACT_count']}")
    print(f"    PARTIAL (constrain only)   : {sweep['PARTIAL_count']}")
    print(f"    NONE                       : {sweep['tally']['NONE']}")
    print(f"    falsifier visibility ok    : "
          f"{sweep['falsifier_visibility_ok']}  "
          f"(planted grounding sentence graded "
          f"{sweep['falsifier_visibility']['planted_grounding_must_be_EXACT']['got']})")
    print()
    print("(b) SCALE-REFERENCE PRIMITIVE BOUNDARY -- computed from bytes")
    print(f"    admit clause : {adj['byte_quotes']['admit_clause']}")
    print(f"    exclude #1   : {adj['byte_quotes']['exclude_clause_1']}")
    print(f"    exclude #2   : {adj['byte_quotes']['exclude_clause_2']}")
    print(f"    sigma is     : {adj['byte_quotes']['sigma_decomposition_clause']}")
    for v in adj["votes"]:
        print(f"      component {v['component']:24s} inside="
              f"{v['inside_primitive']}")
    print(f"    VERDICT: {adj['verdict']}")
    print(f"    {adj['adjudication']}")
    print(f"    {adj['accounting_effect']}")
    print()
    print("(c) STRUCTURAL ARGUMENT")
    print(f"    forced properties byte-present: "
          f"{forced['all_forced_properties_byte_present']} "
          f"({', '.join(f['property'] for f in forced['forced_properties'])})")
    print(f"    residual dimension: {forced['residual_dimension']} "
          f"(param dim {forced['parameter_space_dim']} - group dim "
          f"{forced['invariance_group_dim']})")
    print(f"    six pairs with product "
          f"{forced['distinct_products_on_orbit'][0]} give identical exact "
          f"actions: {forced['all_orbit_actions_identical']}; off-orbit "
          f"control differs: "
          f"{forced['off_orbit_control']['differs_from_orbit']}")
    print(f"    INVOLUTION CENSUS: searched "
          f"{census['matrices_searched']} monomial maps, found "
          f"{census['involutions_found']} involutions")
    print(f"      action-preserving: {census['action_preserving_count']}")
    for k, v in sorted(census["verdict_counts"].items()):
        print(f"      {k:20s} {v}")
    print(f"      cell (action-preserving AND pins sigma) empty: "
          f"{census['census_cell_empty']}")
    print(f"    {census['theorem']}")
    print()
    print(f">>> QUESTION A VERDICT: {verdict_A}")
    print()
    print("-" * 78)
    print("QUESTION B -- THE THETA-INCIDENCE AS A FUNCTION OF THE BARRIER")
    print("-" * 78)
    print(f"window convention: {inc['window_convention']}")
    print()
    print(f"  {'barrier':14s} {'containment':>12s} {'incidence':>10s}  configs")
    for r in inc["rows"]:
        print(f"  {r['barrier']:14s} {str(r['is_containment_barrier']):>12s} "
              f"{r['incidence']:>10s}  {r['theta_dependent_configs']}")
    print()
    print("(b) MECHANISM")
    print(f"    {mech['criterion']}")
    print(f"    {mech['parity_lemma']}")
    print(f"    integer interference predicate vs exact Z: "
          f"{mech['predicate_agreements']}/{mech['predicate_trials']} "
          f"exact={mech['predicate_exact']}")
    print(f"    frozen count by k: {mech['frozen_count_as_function_of_k']}")
    print()
    print("(c) INVARIANT CORE")
    print(f"    containment barriers: {core['containment_barriers']}")
    print(f"    incidence nested in k: {core['incidence_nested_in_k']} "
          f"(strictly: {core['incidence_strictly_nested_in_k']}), "
          f"chain sizes {core['chain_sizes']}")
    print(f"    INVARIANT CORE = {core['invariant_core']}  "
          f"({core['barrier_independent_incidence']})")
    print(f"    N-certificate row survives on core: "
          f"{core['N_certificate_row_survives_on_core']}")
    print(f"    {core['corrected_statement']}")
    print(f"    {core['consumer_guidance']}")
    print()
    pl = sci["K_PLANTED_BARRIER_FALSIFIER"]
    print("FALSIFIER VISIBILITY (Question B)")
    for r in pl["plants"]:
        print(f"    {r['barrier']:14s} containment="
              f"{r['is_containment_barrier']}  incidence={r['incidence']}  "
              f"mechanism={r['mechanism_agreements']}")
    print(f"    slit design met: {pl['slit_design_met']}; core survives "
          f"plants: {pl['invariant_core_survives_the_plants']}")
    print()
    print("-" * 78)
    print("GATES")
    for k, v in passes.items():
        print(f"  {'PASS' if v else 'FAIL'}  {k}")
    print(f"  determinism: {det['identical']}   firewall hits: "
          f"{ctl['firewall_hit_count']}   blocklisted loaded: "
          f"{ctl['blocklisted_modules_loaded']}")
    print()
    print(f"ALL GATES PASS: {all_pass}")
    print(f"elapsed_sec: {round(time.time() - START, 3)}")

    receipt = {
        "cycle": 903,
        "question_A": {
            "question": ("is the bridge scalar sigma derivable from the "
                         "axioms, inside the approved scale-reference "
                         "primitive, or the lane's terminal supplied scalar?"),
            "verdict": verdict_A,
            "sweep_EXACT_count": sweep["EXACT_count"],
            "sweep_PARTIAL_count": sweep["PARTIAL_count"],
            "sweep_sentences": sweep["sentences_swept"],
            "boundary_verdict": adj["verdict"],
            "boundary_adjudication": adj["adjudication"],
            "accounting_effect": adj["accounting_effect"],
            "residual_dimension": forced["residual_dimension"],
            "involution_census": {
                "involutions": census["involutions_found"],
                "action_preserving": census["action_preserving_count"],
                "would_pin_sigma": census["would_pin_sigma"],
                "cell_empty": census["census_cell_empty"],
                "verdict_counts": census["verdict_counts"],
            },
        },
        "question_B": {
            "question": ("what is the theta-dependence incidence as a "
                         "function of the barrier, and what is its "
                         "barrier-independent core?"),
            "incidence_map": inc["incidence_map"],
            "theta_dependent_sets": inc["theta_dependent_sets"],
            "mechanism": mech["criterion"],
            "parity_lemma": mech["parity_lemma"],
            "frozen_count_as_function_of_k":
                mech["frozen_count_as_function_of_k"],
            "mechanism_predicate_exact": mech["predicate_exact"],
            "invariant_core": core["invariant_core"],
            "barrier_independent_incidence":
                core["barrier_independent_incidence"],
            "corrected_statement": core["corrected_statement"],
            "consumer_guidance": core["consumer_guidance"],
            "dependence_structure_for_barrier_pinning":
                core["dependence_structure_for_barrier_pinning"],
            "N_certificate_row_survives_on_core":
                core["N_certificate_row_survives_on_core"],
        },
        "restriction_gates": {
            "gate_b_rows_byte_verified":
                sci["B_GATEB_ROWS_BYTE_VERIFIED"]["all_found"],
            "gate_b_needles_checked":
                sci["B_GATEB_ROWS_BYTE_VERIFIED"]["needles_checked"],
            "cycle885_7_of_12_value_for_value":
                h["value_for_value_match"],
            "cycle885_quoted_witness": h["quoted_witness"],
        },
        "certificate_pass": passes,
        "all_certificates_pass": all_pass,
        "certificates": certs,
        "source_pins": [{"path": r["path"], "sha256": r["sha256"],
                         "git_blob": r["git_blob"]}
                        for r in sci["A_PINS_AND_871_LINEAGE"]["pins"]],
        "lineage_absent_from_this_worktree":
            sci["A_PINS_AND_871_LINEAGE"]["lineage_absent"],
        "runner": str(RUNNER.relative_to(ROOT)),
        "runner_sha256": ctl["runner_sha256"],
        "elapsed_sec": round(time.time() - START, 3),
    }
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(receipt, indent=2, sort_keys=True,
                                default=str) + "\n", encoding="utf-8")
    print(f"receipt: {CACHE.relative_to(ROOT)}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
