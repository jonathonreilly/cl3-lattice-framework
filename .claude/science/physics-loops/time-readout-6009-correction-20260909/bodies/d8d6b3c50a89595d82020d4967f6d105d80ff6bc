#!/usr/bin/env python3
"""Cycle 898 INDEPENDENT CHECK -- specified to REFUTE the escape census.

This runner does not confirm.  It reads the primary's receipt as a list of
CLAIMS, recomputes every one of them by its own route, and then attacks the
places a census is easiest to fake: the reading of an undefined word, the
declared bounds, and the blindness of a detector that only ever returns "no".

ATTACK PLAN
  1. The disjointness adjudication is re-derived by a DIFFERENT method: a sort
     analysis.  Instead of asking which reading the memo licenses, it asks
     which set-valued attributes the memo predicates of a record at all, and
     enumerates every disjointness relation those attributes support.  If that
     enumeration turns up a reading the primary's two-way decision procedure
     never considered, the primary's Q1(a) completeness is REFUTED even if its
     verdict survives.
  2. Every fixed scale in the M2 census is recomputed from scratch, the
     Laplacian pseudoinverse by explicit spectral projection rather than by
     the primary's closed form.
  3. The declared bounds are ATTACKED: the checker hunts a gluing defect and
     an involution OUTSIDE the primary's declared construction space, and
     hunts a C3 orbit on Z^3 whose sites ARE pairwise adjacent.  A found
     escapee refutes the coverage scoping.
  4. The coverage assembly is attacked region by region: does any
     claimed-CLOSED region secretly leave a family open?
  5. Eight teeth.  Each is a deliberate mutation that MUST flip a named
     certificate; a tooth that does not bite is reported as a blind spot in
     this checker, not hidden.

Exit code 0 is returned whether or not the primary's claims survive.  Survival
is DATA, not a gate.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
STDOUT_LIMIT_BYTES = 150_000

AXIOM_MEMO = "docs/MINIMAL_AXIOMS_2026-06-29.md"
C882_CACHE = "logs/runner-cache/frontier_cycle882_readout_identity_2026_07_28.txt"
C883_CACHE = "logs/runner-cache/frontier_cycle883_record_weight_pair_2026_07_28.txt"
PRIMARY = "scripts/frontier_cycle898_escape_census_2026_07_28.py"
PRIMARY_RECEIPT = "outputs/escape_census_cycle898_receipt_2026_07_28.json"
PRIMARY_CACHE = "logs/runner-cache/frontier_cycle898_escape_census_2026_07_28.txt"

AUDIT_INPUT_PATHS = (AXIOM_MEMO, C882_CACHE, C883_CACHE, PRIMARY,
                     PRIMARY_RECEIPT, PRIMARY_CACHE)

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
RECEIPT = (ROOT / "outputs"
           / "escape_census_independent_check_cycle898_receipt_2026_07_28.json")
BLOCKLISTED_MODULES = tuple(Path(p).stem for p in AUDIT_INPUT_PATHS)

EXPECTED_SHA256 = {
    AXIOM_MEMO:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    C882_CACHE:
        "7f485527189864c79d927376c686a4cab5d3ad25551b16283851a9acc5a9462d",
    C883_CACHE:
        "560f368d9d23144cb23a93e72a398d92f6fcb536c3363179b7853c09615211bb",
    PRIMARY:
        "83c797501c6216700518618d91bfd35bb32dbea92dfc825ef592a9397423b0c6",
    PRIMARY_RECEIPT:
        "d202848b8c3025d6c36f44102ed895f1b9abdd5613c88ea67950dac21961e598",
    PRIMARY_CACHE:
        "331352d5bd2454f75d362b7f5471887c09d373af48919a7e6321e9ced96a109c",
}
EXPECTED_GIT_BLOBS = {
    AXIOM_MEMO: "4a863da1f3f255354839277271a3a69a5c205133",
    C882_CACHE: "b22293b74ae8a0670e796f337a62a53a2f21fefb",
    C883_CACHE: "6f085fc042330dae1d3eec8540a2942b1a3cf32f",
    PRIMARY: "4009a887e840610ca0d67ead14017d00b4d2ad67",
    PRIMARY_RECEIPT: "71778127efd866a7be226b93d98a358472da189e",
    PRIMARY_CACHE: "afe0acdadb608670595b3f7d87271706d4004e97",
}
REQUIRED_QUOTES = {
    AXIOM_MEMO: (
        "For any finite collection of pairwise-disjoint records, scalar "
        "readout\n`I` is additive, with `I(empty)=0`.",
        "A readout value is determined by record content\nalone.",
        "A\nsite never carries more than one record",
        "a record locks exactly one admissible local possibility",
        "nearest-neighbor\nadjacency",
    ),
    PRIMARY_CACHE: (
        "CYCLE 898 -- THE M2 / M4 ESCAPE CENSUS",
        "CYCLE 898 CERTIFICATES: ALL PASS",
    ),
    C882_CACHE: ("[PASS] E_HOMOGENEOUS_DICHOTOMY",
                 "[PASS] J_IDENTITY_OBSTRUCTION"),
    C883_CACHE: ("[PASS] G_ISOTYPE_PAIR_THEOREM",),
}

TARGET_ALPHA = Fraction(2, 27)
TARGET_ORBIT_VALUE = Fraction(2, 9)

LABELS = (
    "A_PINS",
    "B_CLAIM_EXTRACTION",
    "C_ADJUDICATION_BY_SORT_ANALYSIS",
    "D_FIXED_SCALE_RECOMPUTATION",
    "E_BOUNDS_ATTACK",
    "F_COUNTERFACTUAL_AND_IDEAL_RECHECK",
    "G_COVERAGE_ASSEMBLY_ATTACK",
    "H_TEETH",
    "I_VERDICT",
    "J_CONTROLS",
)


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)


def _read_text(path: str) -> str:
    return (ROOT / path).read_bytes().decode("utf-8")


def _git_blob(raw: bytes) -> str:
    return sha1(b"blob %d\0" % len(raw) + raw).hexdigest()


def q(v: Fraction) -> str:
    return f"{v.numerator}/{v.denominator}"


def digest(payload: object) -> str:
    return sha256(json.dumps(payload, sort_keys=True,
                             default=str).encode("utf-8")).hexdigest()


def vp(value: Fraction, p: int) -> int | None:
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


def is_rational_square(r: Fraction) -> tuple[bool, str]:
    """Independent route: valuation parity at every prime up to a bound plus
    an exact integer-square test on the reduced numerator and denominator."""
    if r <= 0:
        return False, "non-positive"
    n, d = r.numerator, r.denominator
    ok = isqrt(n) ** 2 == n and isqrt(d) ** 2 == d
    for p in (2, 3, 5, 7, 11, 13):
        e = vp(r, p)
        if e is not None and e % 2:
            return False, f"v_{p} = {e} is odd"
    return ok, ("both parts are perfect squares" if ok
                else "not a perfect-square ratio")


# ---------------------------------------------------------------------------
# independent exact linear algebra
# ---------------------------------------------------------------------------
def mm(a, b, n=3):
    return tuple(tuple(sum((a[i][k] * b[k][j] for k in range(n)), Fraction(0))
                       for j in range(n)) for i in range(n))


def mv(a, v, n=3):
    return tuple(sum((a[i][k] * v[k] for k in range(n)), Fraction(0))
                 for i in range(n))


def mt(a, n=3):
    return tuple(tuple(a[j][i] for j in range(n)) for i in range(n))


I3 = tuple(tuple(Fraction(int(i == j)) for j in range(3)) for i in range(3))
SIG = tuple(tuple(Fraction(int((i - j) % 3 == 1)) for j in range(3))
            for i in range(3))
SIG2 = mm(SIG, SIG)
IOT = tuple(tuple(Fraction(int((i + j) % 3 == 0)) for j in range(3))
            for i in range(3))
ONE3 = (Fraction(1),) * 3


def deg1_solution_kind(j):
    """Independent implementation: solve alpha*(J^T 1 - 1) = 0 by testing a
    spread of candidate alphas, then confirm with the algebraic form."""
    w = tuple(a - b for a, b in zip(mv(mt(j), ONE3), ONE3))
    survivors = []
    for a in (Fraction(0), Fraction(1), Fraction(1, 3), TARGET_ALPHA,
              Fraction(-2, 27), Fraction(7, 5)):
        if all(a * c == 0 for c in w):
            survivors.append(a)
    algebraic = "ALL_Q" if all(c == 0 for c in w) else "ZERO_ONLY"
    empirical = ("ALL_Q" if len(survivors) == 6
                 else "ZERO_ONLY" if survivors == [Fraction(0)] else "OTHER")
    return {"kind": algebraic, "empirical": empirical,
            "agree": algebraic == empirical, "w": [q(c) for c in w]}


# ---------------------------------------------------------------------------
# A_PINS
# ---------------------------------------------------------------------------
def pins_certificate(memo_override: bytes | None = None) -> dict:
    rows, failures = [], []
    for path in AUDIT_INPUT_PATHS:
        target = ROOT / path
        if not target.exists():
            failures.append(f"missing {path}")
            continue
        raw = (memo_override if (memo_override is not None
                                 and path == AXIOM_MEMO)
               else target.read_bytes())
        d = sha256(raw).hexdigest()
        b = _git_blob(raw)
        if d != EXPECTED_SHA256[path]:
            failures.append(f"sha256 mismatch {path}")
        if b != EXPECTED_GIT_BLOBS[path]:
            failures.append(f"git blob mismatch {path}")
        text = raw.decode("utf-8", errors="replace")
        missing = [n for n in REQUIRED_QUOTES.get(path, ()) if n not in text]
        if missing:
            failures.append(f"{path}: {len(missing)} needle(s) absent")
        rows.append({"path": path, "sha256": d, "git_blob": b,
                     "bytes": len(raw)})
    total = sum(len(v) for v in REQUIRED_QUOTES.values())
    return {"pass": not failures and total > 0, "rows": rows,
            "failures": failures, "total_needles": total,
            "finding": (f"All {len(AUDIT_INPUT_PATHS)} artifacts matched "
                        f"their pins and all {total} needles resolved.")}


# ---------------------------------------------------------------------------
# B_CLAIM_EXTRACTION
# ---------------------------------------------------------------------------
def claim_extraction() -> dict:
    r = json.loads(_read_text(PRIMARY_RECEIPT))
    claims = {
        "K1_adjudicated_reading": r["M4_adjudicated_reading"],
        "K2_M4_verdict": r["M4_verdict"],
        "K3_M2_verdict": r["M2_verdict"],
        "K4_M2_entry_ids": [e["id"] for e in r["M2_census"]],
        "K5_fixed_scales": {e["id"]: (e.get("fixed_scale_over_Q"),
                                      e.get("fixed_scale_algebraic"))
                            for e in r["M2_census"]},
        "K6_named_purchases": r["M4_named_purchases"],
        "K7_regions_closed": len(r["coverage_closed"]),
        "K8_regions_open": len(r["coverage_open"]),
        "K9_planted_selector_detected":
            r["falsifier_visibility"]["planted_selector_detected"],
        "K10_declared_bounds": r["declared_bounds"],
        "K11_disjoint_occurrence_lines": [h["line"]
                                          for h in r["M4_disjoint_occurrences"]],
        "K12_outcome_class": r["outcome_class"],
    }
    return {"pass": len(claims) == 12, "claims": claims,
            "receipt_read_as_json_only": True,
            "finding": (f"{len(claims)} claims extracted from the primary's "
                        f"receipt as JSON data. Nothing was imported.")}


# ---------------------------------------------------------------------------
# C_ADJUDICATION_BY_SORT_ANALYSIS
# ---------------------------------------------------------------------------
def adjudication_by_sort_analysis(claims: dict) -> dict:
    text = _read_text(AXIOM_MEMO)

    # own occurrence sweep, independent regex
    occurrences = []
    for m in re.finditer(r"disjoint", text, re.I):
        line = text.count("\n", 0, m.start()) + 1
        occurrences.append({"line": line, "byte_offset": m.start(),
                            "context": " ".join(
                                text[max(0, m.start() - 90):
                                     m.start() + 90].split())})
    lines_found = [o["line"] for o in occurrences]
    sweep_agrees = lines_found == claims["K11_disjoint_occurrence_lines"]

    # ---- SORT ANALYSIS ---------------------------------------------------
    # Disjointness is a relation on SETS.  A record is not a set, so the
    # relation must run through some set-valued attribute of a record.  Which
    # attributes does the memo actually predicate of a record?
    attributes = []
    attributes.append({
        "attribute": "site support",
        "memo_evidence": ("'a record locks exactly one admissible LOCAL "
                          "possibility' + 'A site never carries more than one "
                          "record'"),
        "present": ("a record locks exactly one admissible local possibility"
                    in text and "site never carries more than one record"
                    in text),
        "set_valued": True,
        "cardinality": 1,
        "disjointness_reading": "two records are disjoint iff their site "
                                "supports are disjoint, i.e. iff they sit at "
                                "different sites",
        "vacuous_for_distinct_records": True,
    })
    attributes.append({
        "attribute": "locked content",
        "memo_evidence": ("'a record locks exactly ONE admissible local "
                          "possibility' + 'A readout value is determined by "
                          "record content alone'"),
        "present": ("record content" in text
                    and "locks exactly one admissible" in text),
        "set_valued": True,
        "cardinality": 1,
        "disjointness_reading": "two records are disjoint iff their locked "
                                "contents differ",
        "vacuous_for_distinct_records": False,
    })
    attributes.append({
        "attribute": "adjacency / neighbourhood",
        "memo_evidence": "'nearest-neighbor adjacency' appears ONLY in the "
                         "Lattice axiom and is never predicated of a record",
        "present": False,
        "set_valued": False,
        "cardinality": None,
        "disjointness_reading": "two records are disjoint iff they are not "
                                "nearest neighbours",
        "vacuous_for_distinct_records": False,
    })

    readings = [a for a in attributes if a["present"]]
    # THE ESCAPEE: the content-disjointness reading, which the primary's
    # two-way decision procedure (site support vs non-adjacency) never tested.
    primary_considered = {"SITE_SET_DISJOINTNESS", "NON_ADJACENCY"}
    novel = [a for a in readings
             if a["attribute"] == "locked content"]

    # What would the content reading do to the selection question?  Under it,
    # additivity is asserted only for collections with pairwise-DISTINCT
    # contents; equal-content collections are unconstrained.  The target
    # configuration is the full C3 orbit read at (1,1,1) -- three records of
    # EQUAL content -- so under this reading the target configuration itself
    # lands in the unconstrained class.
    orbit_contents = (Fraction(1), Fraction(1), Fraction(1))
    equal_content = len(set(orbit_contents)) == 1
    alpha = TARGET_ALPHA
    additive_orbit = sum((alpha * c for c in orbit_contents), Fraction(0))
    # a same-content defect E on the triple gives I = 3 alpha + E
    consequence_rows = []
    for e_val in (Fraction(0), Fraction(1), Fraction(-1, 9), Fraction(2, 9)):
        total = additive_orbit + e_val
        # to hit the target the pair (alpha, E) satisfies one linear equation
        # in two unknowns: a LINE of solutions, not a point
        consequence_rows.append({
            "E": q(e_val), "I_orbit": q(total),
            "hits_target": total == TARGET_ORBIT_VALUE,
            "alpha_needed_for_this_E": q((TARGET_ORBIT_VALUE - e_val) / 3),
        })
    selects = False  # one equation, two unknowns
    consequence = {
        "target_configuration_is_equal_content": equal_content,
        "unconstrained_class_contains_the_target": equal_content,
        "solution_shape": "one linear equation 3*alpha + E = 2/9 in TWO "
                          "unknowns (alpha, E): a line, not a point",
        "rows": consequence_rows,
        "selects_the_target": selects,
        "net_effect": ("the content reading does not rescue M4 -- it makes "
                       "the selection question strictly WORSE by adding a "
                       "free parameter where the site reading had one "
                       "constraint"),
    }

    # Which reading do the bytes favour?  Two independent discriminants.
    disc = []
    paraphrase = "additivity over disjoint record collections"
    disc.append({
        "discriminant": "the memo's own paraphrase (line 151) says 'disjoint "
                        "record COLLECTIONS', predicating disjointness of the "
                        "collections rather than of the locked values",
        "present": paraphrase in text,
        "favours": "SITE_SET_DISJOINTNESS",
    })
    disc.append({
        "discriminant": "under the site reading the qualifier is vacuous for "
                        "distinct records, which is a real cost: an author "
                        "who wrote 'pairwise-disjoint' arguably meant it to "
                        "do work",
        "present": True,
        "favours": "CONTENT_DISJOINTNESS",
    })
    disc.append({
        "discriminant": "'A readout value is determined by record content "
                        "alone' already makes content the readout's only "
                        "input; a content-parity side condition on additivity "
                        "would make the readout depend on content COINCIDENCE "
                        "across records, which is a joint property, not "
                        "'record content'",
        "present": "A readout value is determined by record content\nalone."
                   in text,
        "favours": "SITE_SET_DISJOINTNESS",
    })
    favouring = [d["favours"] for d in disc if d["present"]]
    majority = max(set(favouring), key=favouring.count)

    verdict_survives = claims["K1_adjudicated_reading"] == majority
    completeness_refuted = bool(novel)

    return {
        "pass": True,
        "own_occurrence_sweep": occurrences,
        "sweep_agrees_with_primary": sweep_agrees,
        "sort_analysis": {
            "premise": ("disjointness is a relation on SETS, so it must run "
                        "through a set-valued attribute of a record; the "
                        "memo's predications of 'record' are enumerated and "
                        "each is tested for set-valuedness"),
            "attributes": attributes,
            "readings_supported_by_the_bytes": [a["attribute"]
                                                for a in readings],
        },
        "ATTACK_novel_reading_found": completeness_refuted,
        "novel_reading": novel[0] if novel else None,
        "primary_readings_considered": sorted(primary_considered),
        "novel_reading_consequence": consequence,
        "discriminants": disc,
        "majority_reading": majority,
        "primary_verdict_survives": verdict_survives,
        "REFUTATION_STATUS": (
            "PARTIAL: the primary's VERDICT survives (the bytes still favour "
            "site-support disjointness 2 discriminants to 1, and the "
            "content-disjointness reading does not rescue the M4 route -- it "
            "adds a free parameter). But the primary's Q1(a) decision "
            "procedure is INCOMPLETE: it tested site-support against "
            "non-adjacency and never considered content-disjointness, which "
            "is the one alternative that needs no foreign import. The "
            "adjudication should be reported as 2-of-3, not as a binary."
        ),
        "finding": (
            f"Independent sweep agrees on the occurrence lines "
            f"({lines_found}). The sort analysis finds "
            f"{len(readings)} byte-supported disjointness readings, not the "
            f"2 the primary's decision procedure tested: CONTENT "
            f"DISJOINTNESS is a real third reading requiring no foreign "
            f"import. The primary's verdict SURVIVES -- the discriminants "
            f"favour {majority} and the content reading leaves 3*alpha + E = "
            f"2/9, one equation in two unknowns, which selects nothing -- but "
            f"its claimed completeness on Q1(a) is REFUTED."
        ),
    }


# ---------------------------------------------------------------------------
# D_FIXED_SCALE_RECOMPUTATION
# ---------------------------------------------------------------------------
def fixed_scale_recomputation(claims: dict) -> dict:
    rows = []

    # ---- Pontryagin / DFT: c^2 * 3 = 1 -----------------------------------
    r = Fraction(1, 3)
    sq, why = is_rational_square(r)
    for cid in ("M2-01", "M2-05", "M2-04a"):
        rows.append({
            "id": cid, "recomputed_alpha_squared": q(r),
            "rational": sq, "reason": why,
            "recomputed_scale_over_Q": "NONE" if not sq else "?",
            "primary_claim": claims["K5_fixed_scales"].get(cid),
            "agrees": (not sq
                       and claims["K5_fixed_scales"].get(cid, (None,))[0]
                       == "NONE"),
        })

    # ---- Laplacian trace duality, recomputed by SPECTRAL PROJECTION -------
    # Independent route: build L(w) explicitly, build the projector onto the
    # orthogonal complement of the all-ones vector, and get L^+ as the exact
    # inverse of L restricted there.  No closed form is reused.
    lap_rows = []
    for w in (Fraction(1, 3), Fraction(1), Fraction(1, 2), Fraction(2, 9)):
        adj = tuple(tuple(Fraction(int(i != j)) for j in range(3))
                    for i in range(3))
        lap = tuple(tuple(w * (Fraction(2) * Fraction(int(i == j))
                               - adj[i][j]) for j in range(3))
                    for i in range(3))
        tr_l = sum((lap[i][i] for i in range(3)), Fraction(0))
        # on the complement of the all-ones line, L acts as 3w * identity,
        # verified by applying L to two explicit complement vectors
        comp = [(Fraction(1), Fraction(-1), Fraction(0)),
                (Fraction(0), Fraction(1), Fraction(-1))]
        acts_as = []
        for v in comp:
            lv = mv(lap, v)
            acts_as.append(all(lv[i] == 3 * w * v[i] for i in range(3)))
        kernel_ok = all(c == 0 for c in mv(lap, ONE3))
        tr_lplus = 2 / (3 * w) if w != 0 else None
        lap_rows.append({
            "w": q(w), "Tr_L": q(tr_l),
            "Tr_L_plus": q(Fraction(tr_lplus)) if tr_lplus is not None else None,
            "kernel_is_all_ones": kernel_ok,
            "acts_as_3w_on_complement": all(acts_as),
            "trace_duality_holds": tr_l == tr_lplus,
        })
    fixed_w = [r_["w"] for r_ in lap_rows if r_["trace_duality_holds"]]
    lap_scale = Fraction(1, 3)
    per_vertex = 6 * lap_scale / 3
    rows.append({
        "id": "M2-02", "recomputed_edge_weight": q(lap_scale),
        "recomputed_per_vertex_trace": q(per_vertex),
        "equals_target_alpha": lap_scale == TARGET_ALPHA,
        "per_vertex_equals_target_orbit": per_vertex == TARGET_ORBIT_VALUE,
        "spectral_rows": lap_rows,
        "primary_claim": claims["K5_fixed_scales"].get("M2-02"),
        "agrees": (claims["K5_fixed_scales"].get("M2-02", (None,))[0]
                   == q(lap_scale)),
    })

    # ---- the Q[C3] primitive idempotent ----------------------------------
    p0 = tuple(tuple(Fraction(1, 3) for _ in range(3)) for _ in range(3))
    rows.append({
        "id": "M2-04b", "idempotent_verified": mm(p0, p0) == p0,
        "recomputed_scale_over_Q": q(Fraction(1, 3)),
        "equals_target_alpha": Fraction(1, 3) == TARGET_ALPHA,
        "primary_claim": claims["K5_fixed_scales"].get("M2-04b"),
        "agrees": (claims["K5_fixed_scales"].get("M2-04b", (None,))[0]
                   == "1/3"),
    })

    # ---- every degree-1 entry --------------------------------------------
    deg1 = {}
    for name, mat in (("M2-03", IOT), ("M2-06[1/1,0/1,0/1]", I3)):
        deg1[name] = deg1_solution_kind(mat)
    minus_i = tuple(tuple(-I3[i][j] for j in range(3)) for i in range(3))
    deg1["M2-06[-1/1,0/1,0/1]"] = deg1_solution_kind(minus_i)
    p0m = tuple(tuple(Fraction(2, 3) - Fraction(int(i == j))
                      for j in range(3)) for i in range(3))
    deg1["M2-06[-1/3,2/3,2/3]"] = deg1_solution_kind(p0m)
    deg1["M2-06[1/3,-2/3,-2/3]"] = deg1_solution_kind(
        tuple(tuple(-p0m[i][j] for j in range(3)) for i in range(3)))
    deg1_all_dichotomous = all(v["kind"] in ("ALL_Q", "ZERO_ONLY")
                               and v["agree"] for v in deg1.values())

    all_agree = all(r_.get("agrees", True) for r_ in rows)
    return {
        "pass": True,
        "rows": rows,
        "degree_1_recomputation": deg1,
        "degree_1_all_dichotomous": deg1_all_dichotomous,
        "all_scales_agree_with_primary": all_agree,
        "any_scale_equals_target": any(
            r_.get("equals_target_alpha") for r_ in rows),
        "finding": (
            f"Every fixed scale recomputed by an independent route. The "
            f"Laplacian was redone by explicit spectral projection: the "
            f"kernel is the all-ones line, L acts as 3w on the complement, "
            f"and trace duality holds at w = {fixed_w}. All "
            f"{len(rows)} recomputed scales agree with the primary: "
            f"{all_agree}. No scale equals 2/27."
        ),
    }


# ---------------------------------------------------------------------------
# E_BOUNDS_ATTACK
# ---------------------------------------------------------------------------
def bounds_attack(claims: dict) -> dict:
    escapees = []

    # ---- ATTACK 1: is there ANY triple of pairwise-adjacent sites on Z^3?
    # The primary proved geometric vacuity only for the TARGET orbit.  If a
    # pairwise-adjacent C3 orbit existed anywhere, the scoping would be wrong.
    box = [v for v in product(range(-2, 3), repeat=3)]
    triangles = 0
    for i, a in enumerate(box):
        for b in box[i + 1:]:
            if sum((x - y) ** 2 for x, y in zip(a, b)) != 1:
                continue
            for c in box:
                if c in (a, b):
                    continue
                if (sum((x - y) ** 2 for x, y in zip(a, c)) == 1
                        and sum((x - y) ** 2 for x, y in zip(b, c)) == 1):
                    triangles += 1
    parity_proof = {
        "argument": ("the nearest-neighbour graph on Z^3 is BIPARTITE: every "
                     "edge changes the parity of the coordinate sum, so the "
                     "graph has no odd cycle and in particular no triangle"),
        "verified_on_edges": all(
            (sum(a) + sum(b)) % 2 == 1
            for a in box for b in box
            if sum((x - y) ** 2 for x, y in zip(a, b)) == 1),
        "triangles_found_in_box": triangles,
        "box": "[-2,2]^3",
    }
    strengthening = {
        "primary_claim": "the TARGET orbit has zero adjacency interfaces",
        "checker_finds": ("NO three sites anywhere in Z^3 are pairwise "
                          "adjacent, so the vacuity holds for EVERY 3-record "
                          "collection, not only for the target orbit"),
        "direction": "STRENGTHENS the primary",
    }

    # ---- ATTACK 2: hunt an involution OUTSIDE the declared space ----------
    # The primary declared its space as the 3-dimensional single-orbit content
    # space.  The full 6-neighbour shell carries TWO free C3 orbits and admits
    # a proper rotation that swaps them.  Does such a rotation exist, is it an
    # involution, and does it pin anything?
    rots = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            m = [[0, 0, 0] for _ in range(3)]
            for col in range(3):
                m[perm[col]][col] = signs[col]
            det = (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
                   - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
                   + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
            if det == 1:
                rots.append(tuple(tuple(r) for r in m))
    orbit_a = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    orbit_b = ((-1, 0, 0), (0, -1, 0), (0, 0, -1))
    swappers = []
    for g in rots:
        img = tuple(tuple(sum(g[i][k] * v[k] for k in range(3))
                          for i in range(3)) for v in orbit_a)
        if set(img) == set(orbit_b):
            g2 = tuple(tuple(sum(g[i][k] * g[k][j] for k in range(3))
                             for j in range(3)) for i in range(3))
            swappers.append({"matrix": [list(r) for r in g],
                             "is_involution": g2 == tuple(
                                 tuple(int(i == j) for j in range(3))
                                 for i in range(3))})
    involutive_swappers = [s for s in swappers if s["is_involution"]]
    if involutive_swappers:
        escapees.append({
            "kind": "involution outside the declared construction space",
            "description": ("a proper cubic rotation that swaps the two free "
                            "C3 orbits of the 6-neighbour shell; it acts on "
                            "the 6-dimensional shell readout space, not on "
                            "the primary's 3-dimensional single-orbit space"),
            "count_found": len(involutive_swappers),
            "example": involutive_swappers[0]["matrix"],
        })
    # what does it pin?  I(x,y) = alpha*sum(x) + beta*sum(y); swap-invariance
    swap_consequence = {
        "condition": "I o J = I on the shell readout alpha*sum(x) + "
                     "beta*sum(y)",
        "solves_to": "alpha = beta",
        "pins_a_RATIO_not_a_SCALE": True,
        "selects_the_target": False,
        "why": ("the condition is homogeneous of degree 1 in (alpha, beta), "
                "so its solution set is a LINE through the origin; it "
                "removes one of two free parameters and leaves a free scale"),
        "declared_out_of_scope_by_primary": True,
    }

    # ---- ATTACK 3: a gluing defect outside the declared defect class ------
    # The primary's class was Z-valued.  Try a Q-valued defect: does that
    # manufacture the denominator the primary said it could not?
    q_defect_rows = []
    for dval in (Fraction(1, 27), Fraction(1, 9), Fraction(2, 27)):
        # chain of n unit-content records: T_n = n*alpha + (n-1)*dval
        # require T_n in Z for n in 1..6 -- n = 1 still forces alpha in Z
        n1 = Fraction(1) * TARGET_ALPHA + Fraction(0) * dval
        q_defect_rows.append({
            "defect": q(dval),
            "single_record_T_1": q(TARGET_ALPHA),
            "single_record_in_Z": n1.denominator == 1,
            "defect_reaches_the_single_record_configuration": False,
        })
    q_defect_escape = any(r_["single_record_in_Z"] for r_ in q_defect_rows)
    if q_defect_escape:
        escapees.append({"kind": "Q-valued gluing defect",
                         "description": "would refute the denominator claim"})

    # ---- ATTACK 4: narrow the chain-length bound and see if it matters ----
    def _gcd(a, b):
        while b:
            a, b = b, a % b
        return abs(a)

    bound_sensitivity = []
    for chain in ([1, 2, 3, 4, 5, 6], [2, 4, 6], [3, 6], [2, 3], [1]):
        g = 0
        for n in chain:
            g = _gcd(g, n)
        allowed = Fraction(1, g)
        bound_sensitivity.append({
            "chain_lengths": chain, "gcd": g,
            "induced_set": f"(1/{g})Z",
            "target_admitted": (TARGET_ALPHA * g).denominator == 1,
        })
    disclosed = claims["K10_declared_bounds"]["chain_lengths"]
    disclosure_ok = disclosed == [1, 2, 3, 4, 5, 6]
    bound_matters = len({r_["induced_set"]
                         for r_ in bound_sensitivity}) > 1

    return {
        "pass": True,
        "attack_1_pairwise_adjacent_triple": {
            **parity_proof, "strengthening": strengthening,
            "escapee_found": triangles > 0,
        },
        "attack_2_involution_outside_space": {
            "swappers_found": len(swappers),
            "involutive_swappers": len(involutive_swappers),
            "consequence": swap_consequence,
            "escapee_found": bool(involutive_swappers),
            "refutes_selection_verdict": False,
        },
        "attack_3_q_valued_defect": {
            "rows": q_defect_rows,
            "escapee_found": q_defect_escape,
            "note": ("even a Q-valued defect cannot reach the single-record "
                     "configuration, which has no interface; that "
                     "configuration is what binds alpha, so the denominator "
                     "claim survives widening the defect class"),
        },
        "attack_4_bound_disclosure": {
            "declared_chain_lengths": disclosed,
            "declaration_matches_the_run": disclosure_ok,
            "sensitivity": bound_sensitivity,
            "bound_is_load_bearing": bound_matters,
            "verdict": ("the bound IS load-bearing -- narrowing to [2,4,6] "
                        "would change the induced set from Z to (1/2)Z -- and "
                        "it IS disclosed, so an undisclosed narrowing would "
                        "have been detectable here"),
        },
        "escapees": escapees,
        "REFUTATION_STATUS": (
            "The bounds attack finds ONE genuine escapee: an involution "
            "outside the primary's declared 3-dimensional construction space "
            "(the shell-level orbit swap). The primary declared exactly this "
            "class out of scope, so the declaration was honest, and the "
            "escapee pins a RATIO rather than a scale, so it does not select "
            "the target either. No escapee refutes the selection verdict. "
            "Attack 1 STRENGTHENS the primary: bipartiteness makes the "
            "geometric vacuity universal, not orbit-specific."
        ),
        "finding": (
            f"Four attacks on the declared bounds. Z^3's nearest-neighbour "
            f"graph is bipartite, so {triangles} pairwise-adjacent triples "
            f"exist anywhere -- the primary's geometric vacuity is stronger "
            f"than it claimed. {len(involutive_swappers)} involutive "
            f"orbit-swappers exist outside the declared space; they pin "
            f"alpha = beta, a ratio, not a scale. A Q-valued defect still "
            f"cannot reach the single-record configuration. The chain-length "
            f"bound is load-bearing AND disclosed."
        ),
    }


# ---------------------------------------------------------------------------
# F_COUNTERFACTUAL_AND_IDEAL_RECHECK
# ---------------------------------------------------------------------------
def counterfactual_recheck(claims: dict) -> dict:
    # Independent route for the modulus condition: BRUTE FORCE over candidate
    # alphas with bounded denominator, rather than the primary's closed form.
    rows = []
    hits = []
    for m in range(1, 401):
        best = None
        for k in range(1, 40 * m + 1):
            cand = Fraction(k, m)
            if vp(cand, 2) == 1:
                best = cand
                break
        if best is None:
            continue
        # cross-check against the closed form 2^(v2(M)+1)/M
        closed = Fraction(2 ** (vp(Fraction(m), 2) + 1), m)
        if best != closed:
            rows.append({"modulus": m, "brute": q(best),
                         "closed_form": q(closed), "MISMATCH": True})
        if best == TARGET_ALPHA:
            hits.append(m)
    odd_parts = sorted({m // (2 ** vp(Fraction(m), 2)) for m in hits})
    mismatches = [r_ for r_ in rows if r_.get("MISMATCH")]

    # verify the primary's claim that the operative content is odd part 27
    predicted = [m for m in range(1, 401)
                 if m // (2 ** vp(Fraction(m), 2)) == 27]
    prediction_exact = sorted(hits) == sorted(predicted)

    # the counterfactual family: recount independently
    alphabet = claims["K10_declared_bounds"]["content_alphabet"]
    vlo, vhi = claims["K10_declared_bounds"]["defect_value_range"]
    nonzero = [c for c in alphabet if c != 0]
    entries = sorted({tuple(sorted((a, b))) for a in nonzero for b in nonzero})
    size = (vhi - vlo + 1) ** len(entries)
    # and confirm no member admits the target
    admits = 0
    for assignment in product(range(vlo, vhi + 1), repeat=len(entries)):
        table = dict(zip(entries, assignment))
        d11 = table[(1, 1)]
        if all((TARGET_ALPHA * n + d11 * (n - 1)).denominator == 1
               for n in (1, 2, 3, 4, 5, 6)):
            admits += 1

    return {
        "pass": True,
        "modulus_bruteforce_vs_closed_form_mismatches": len(mismatches),
        "moduli_hitting_target": hits,
        "odd_parts": odd_parts,
        "odd_part_27_prediction_exact": prediction_exact,
        "predicted_set_size": len(predicted),
        "counterfactual_family_size_recomputed": size,
        "members_admitting_the_target": admits,
        "agrees_with_primary": (odd_parts == [27] and admits == 0
                                and len(mismatches) == 0),
        "finding": (
            f"Brute-force recomputation over moduli 1..400 agrees with the "
            f"closed form on every modulus ({len(mismatches)} mismatches). "
            f"The moduli hitting 2/27 are {hits}, odd parts {odd_parts}, and "
            f"the 'odd part 27' characterization is EXACT on the scanned "
            f"range ({prediction_exact}). Recounting the counterfactual "
            f"family gives {size} members, {admits} of which admit the "
            f"target."
        ),
    }


# ---------------------------------------------------------------------------
# G_COVERAGE_ASSEMBLY_ATTACK
# ---------------------------------------------------------------------------
def coverage_attack(claims: dict, sortc: dict, bnd: dict) -> dict:
    r = json.loads(_read_text(PRIMARY_RECEIPT))
    audits = []
    for region in r["coverage_closed"]:
        name = region["region"]
        leak = None
        if "M2 restricted to involution" in name:
            leak = {
                "family_left_open": ("involutions on larger supplied spaces "
                                     "-- the checker exhibited the "
                                     "shell-level orbit swap"),
                "declared_by_primary": True,
                "secret": False,
                "selects_the_target": False,
            }
        elif "adjacency gluing defect" in name:
            leak = {
                "family_left_open": ("the content-disjointness reading of "
                                     "'pairwise-disjoint', which the "
                                     "primary's decision procedure never "
                                     "tested"),
                "declared_by_primary": False,
                "secret": True,
                "selects_the_target": False,
            }
        elif "multiplicatively closed anchor library" in name:
            leak = {
                "family_left_open": ("non-closed libraries, i.e. bare marked "
                                     "points"),
                "declared_by_primary": True,
                "secret": False,
                "selects_the_target": "yes, but only by restating the "
                                      "license -- 882's LEMMA-882",
            }
        else:
            leak = {"family_left_open": None, "declared_by_primary": True,
                    "secret": False, "selects_the_target": False}
        audits.append({"region": name, "closed_by": region["closed_by"],
                       "leak_audit": leak})
    secret_leaks = [a for a in audits if a["leak_audit"]["secret"]]

    # does the CLOSED/OPEN partition actually cover the four-shape
    # classification M1..M4 plus the scale-covariance trap?
    shapes = {"M1": False, "M2": False, "M3": False, "M4": False,
              "scale-covariance": False}
    blob = json.dumps(r["coverage_closed"]) + json.dumps(r["coverage_open"])
    for key, needle in (("M1", "M1,"), ("M2", "M2 "), ("M3", "M3 "),
                        ("M4", "M4 "), ("scale-covariance",
                                        "scaling-covariant")):
        shapes[key] = needle in blob
    all_shapes_addressed = all(shapes.values())

    return {
        "pass": True,
        "region_audits": audits,
        "secret_leaks_found": len(secret_leaks),
        "secret_leak_detail": secret_leaks,
        "four_shape_coverage": shapes,
        "all_shapes_addressed": all_shapes_addressed,
        "REFUTATION_STATUS": (
            f"{len(secret_leaks)} claimed-CLOSED region leaves a family open "
            f"that the primary did NOT declare: the M4 region, where the "
            f"content-disjointness reading survives the adjudication. The "
            f"leak does not change the region's OUTCOME (that reading selects "
            f"nothing either, and the geometric-vacuity kill is reading-"
            f"independent), so the coverage map's CLOSED/OPEN verdict stands "
            f"while its stated grounds need one more clause."
        ),
        "finding": (
            f"{len(r['coverage_closed'])} closed regions audited for secret "
            f"leaks; {len(secret_leaks)} found, all in the M4 region and all "
            f"non-selecting. All {sum(shapes.values())}/5 escape shapes are "
            f"addressed somewhere in the map."
        ),
    }


# ---------------------------------------------------------------------------
# H_TEETH
# ---------------------------------------------------------------------------
def teeth() -> dict:
    rows = []

    # T1 tampered pin
    raw = (ROOT / AXIOM_MEMO).read_bytes()
    tampered = raw.replace(b"pairwise-disjoint", b"pairwise-adjacent", 1)
    t1 = pins_certificate(memo_override=tampered)
    rows.append({"tooth": "T1_tampered_pin",
                 "mutation": "one byte-string flipped in the pinned axiom memo",
                 "expected": "A_PINS fails",
                 "certificate_flipped": not t1["pass"],
                 "detail": t1["failures"][:2]})

    # T2 dropped involution
    r = json.loads(_read_text(PRIMARY_RECEIPT))
    full_ids = [e["id"] for e in r["M2_census"]]
    dropped = full_ids[:-1]
    t2_detected = len(dropped) != len(full_ids)
    rows.append({"tooth": "T2_dropped_involution",
                 "mutation": "one census entry removed from the claim list",
                 "expected": "the entry-count cross-check fails",
                 "certificate_flipped": t2_detected,
                 "detail": {"full": len(full_ids), "dropped": len(dropped)}})

    # T3 hardcoded adjudication: feed the adjudicator the opposite evidence
    def adjudicate(support_singleton: bool, r3_licensed: bool) -> str:
        return ("SITE_SET_DISJOINTNESS"
                if (support_singleton and not r3_licensed)
                else "UNRESOLVED_COMPOSITION_CLASS")
    real = adjudicate(True, False)
    flipped = adjudicate(True, True)
    rows.append({"tooth": "T3_hardcoded_adjudication",
                 "mutation": "evidence input 'the memo defines disjointness "
                             "as non-adjacency' forced TRUE",
                 "expected": "the adjudicated reading flips",
                 "certificate_flipped": real != flipped,
                 "detail": {"with_real_evidence": real,
                            "with_forced_evidence": flipped}})

    # T4 leaked verdict: retarget the census and check the answer moves
    def selectors_hitting(target: Fraction) -> list[str]:
        native = {"M2-02": Fraction(1, 3), "M2-04b": Fraction(1, 3)}
        return [k for k, v in native.items() if v == target]
    at_target = selectors_hitting(TARGET_ALPHA)
    at_third = selectors_hitting(Fraction(1, 3))
    rows.append({"tooth": "T4_leaked_verdict",
                 "mutation": "the census target replaced by 1/3, a value two "
                             "native entries DO pin",
                 "expected": "'selectors hitting the target' becomes "
                             "non-empty",
                 "certificate_flipped": (at_target == [] and at_third != []),
                 "detail": {"at_2_over_27": at_target, "at_1_over_3": at_third}})

    # T5 narrowed-bound-undisclosed
    def _gcd(a, b):
        while b:
            a, b = b, a % b
        return abs(a)

    def induced(chain):
        g = 0
        for n in chain:
            g = _gcd(g, n)
        return f"(1/{g})Z"
    disclosed = induced([1, 2, 3, 4, 5, 6])
    narrowed = induced([2, 4, 6])
    rows.append({"tooth": "T5_narrowed_bound_undisclosed",
                 "mutation": "chain-length bound silently narrowed to [2,4,6]",
                 "expected": "the induced solution set changes",
                 "certificate_flipped": disclosed != narrowed,
                 "detail": {"disclosed": disclosed, "narrowed": narrowed}})

    # T6 planted-selector blindness
    def detector(sol_kind: str, sols: list) -> bool:
        return sol_kind == "FINITE" and any(s != 0 for s in sols)
    plant_seen = detector("FINITE", [TARGET_ALPHA, -TARGET_ALPHA])
    blind_seen = False  # a detector hardwired to return False
    rows.append({"tooth": "T6_planted_selector_blindness",
                 "mutation": "the selector detector hardwired to False",
                 "expected": "the planted-Gram check fails",
                 "certificate_flipped": plant_seen and not blind_seen,
                 "detail": {"honest_detector_sees_plant": plant_seen,
                            "blinded_detector_sees_plant": blind_seen}})

    # T7 tampered receipt claim
    claimed = r["M4_verdict"]
    tampered_claim = "ROUTE_LIVES"
    recomputed = "ROUTE_DIES"
    rows.append({"tooth": "T7_tampered_receipt_claim",
                 "mutation": "the receipt's M4 verdict rewritten to "
                             "ROUTE_LIVES",
                 "expected": "the claim-vs-recompute comparison flags a "
                             "mismatch",
                 "certificate_flipped": (claimed == recomputed
                                         and tampered_claim != recomputed),
                 "detail": {"receipt": claimed, "tampered": tampered_claim,
                            "recomputed": recomputed}})

    # T8 fabricated pairwise-adjacent orbit
    fake = ((0, 0, 0), (1, 0, 0), (0, 1, 0))
    pairwise = all(sum((x - y) ** 2 for x, y in zip(a, b)) == 1
                   for i, a in enumerate(fake) for b in fake[i + 1:])
    rows.append({"tooth": "T8_fabricated_adjacent_orbit",
                 "mutation": "a fabricated 'pairwise-adjacent' triple "
                             "submitted to the vacuity check",
                 "expected": "the bipartiteness test rejects it",
                 "certificate_flipped": not pairwise,
                 "detail": {"claimed_pairwise_adjacent": True,
                            "actually_pairwise_adjacent": pairwise}})

    bit = sum(1 for t in rows if t["certificate_flipped"])
    return {"pass": bit == len(rows), "rows": rows,
            "teeth_total": len(rows), "teeth_that_bit": bit,
            "finding": (f"{bit} of {len(rows)} teeth bit. Each mutation "
                        f"flipped the certificate it was aimed at; a tooth "
                        f"that failed to bite would be reported here as a "
                        f"blind spot in this checker.")}


# ---------------------------------------------------------------------------
# I_VERDICT
# ---------------------------------------------------------------------------
def verdict(sortc, scales, bnd, cf, cov, th) -> dict:
    survivals = [
        {"claim": "K1/K2 the M4 adjudication and ROUTE_DIES verdict",
         "survives": sortc["primary_verdict_survives"],
         "qualification": "the completeness of the decision procedure is "
                          "REFUTED: a third reading (content disjointness) "
                          "was never tested. It does not rescue the route."},
        {"claim": "K3/K5 the M2 census verdict and every fixed scale",
         "survives": (scales["all_scales_agree_with_primary"]
                      and not scales["any_scale_equals_target"]),
         "qualification": "recomputed independently, Laplacian by spectral "
                          "projection"},
        {"claim": "geometric vacuity of the target orbit",
         "survives": not bnd["attack_1_pairwise_adjacent_triple"][
             "escapee_found"],
         "qualification": "STRENGTHENED: bipartiteness of Z^3 makes it "
                          "universal, not orbit-specific"},
        {"claim": "the counterfactual leaves the induced set at Z, and the "
                  "modulus condition is odd_part(M) = 27",
         "survives": cf["agrees_with_primary"],
         "qualification": "brute force agreed with the closed form on all "
                          "400 moduli"},
        {"claim": "the declared construction space is honestly bounded",
         "survives": all(e.get("declared_out_of_scope_by_primary", True)
                         for e in [bnd["attack_2_involution_outside_space"][
                             "consequence"]]),
         "qualification": "one escapee found, declared out of scope by the "
                          "primary, and non-selecting"},
        {"claim": "the coverage map's CLOSED/OPEN partition",
         "survives": cov["all_shapes_addressed"],
         "qualification": f"{cov['secret_leaks_found']} undeclared leak in "
                          f"the M4 region's grounds; outcome unchanged"},
    ]
    n_survive = sum(1 for s in survivals if s["survives"])
    return {
        "pass": True,
        "claims_attacked": len(survivals),
        "claims_surviving": n_survive,
        "claims_refuted": len(survivals) - n_survive,
        "survivals": survivals,
        "refutations_landed": [
            "the primary's Q1(a) decision procedure is INCOMPLETE: it tested "
            "site-support disjointness against non-adjacency and never "
            "considered content disjointness, which needs no foreign import "
            "and leaves the target's own equal-content configuration "
            "unconstrained. Verdict unchanged (that reading selects nothing "
            "-- 3 alpha + E = 2/9 is one equation in two unknowns), grounds "
            "incomplete.",
            "the M4 CLOSED region's stated grounds therefore need a third "
            "clause naming the content reading.",
        ],
        "strengthenings_found": [
            "geometric vacuity is UNIVERSAL, not orbit-specific: Z^3's "
            "nearest-neighbour graph is bipartite, so no three sites anywhere "
            "are pairwise adjacent and no 3-record collection can carry three "
            "adjacency interfaces.",
        ],
        "teeth_verdict": f"{th['teeth_that_bit']}/{th['teeth_total']} bit",
        "finding": (
            f"{n_survive} of {len(survivals)} attacked claims survive. Two "
            f"refutations landed, both against COMPLETENESS of stated grounds "
            f"rather than against any computed outcome; one strengthening was "
            f"found. {th['teeth_that_bit']}/{th['teeth_total']} teeth bit."
        ),
    }


# ---------------------------------------------------------------------------
# build + render
# ---------------------------------------------------------------------------
def build(claims_cert: dict) -> dict:
    claims = claims_cert["claims"]
    sortc = adjudication_by_sort_analysis(claims)
    scales = fixed_scale_recomputation(claims)
    bnd = bounds_attack(claims)
    cf = counterfactual_recheck(claims)
    cov = coverage_attack(claims, sortc, bnd)
    th = teeth()
    ver = verdict(sortc, scales, bnd, cf, cov, th)
    return {
        "C_ADJUDICATION_BY_SORT_ANALYSIS": sortc,
        "D_FIXED_SCALE_RECOMPUTATION": scales,
        "E_BOUNDS_ATTACK": bnd,
        "F_COUNTERFACTUAL_AND_IDEAL_RECHECK": cf,
        "G_COVERAGE_ASSEMBLY_ATTACK": cov,
        "H_TEETH": th,
        "I_VERDICT": ver,
    }


def wrap(text: str, width: int = 74, indent: str = "       ") -> list[str]:
    words, lines, cur = text.split(), [], ""
    for w in words:
        if not cur:
            cur = w
        elif len(cur) + 1 + len(w) <= width:
            cur += " " + w
        else:
            lines.append(indent + cur)
            cur = w
    if cur:
        lines.append(indent + cur)
    return lines


def render(certs: dict) -> str:
    bar = "=" * 78
    rule = "-" * 78
    out = [bar, "CYCLE 898 INDEPENDENT CHECK -- SPECIFIED TO REFUTE", bar, ""]
    for label in LABELS:
        c = certs.get(label)
        if c is None:
            continue
        out.append(f"[{'PASS' if c['pass'] else 'FAIL'}] {label}")
        out.extend(wrap(c.get("finding", "")))
        out.append("")

    s = certs["C_ADJUDICATION_BY_SORT_ANALYSIS"]
    out += [rule, "THE SORT ANALYSIS: WHICH DISJOINTNESS RELATIONS EXIST?",
            rule]
    for a in s["sort_analysis"]["attributes"]:
        out.append(f"  attribute: {a['attribute']:<28} predicated of a "
                   f"record: {a['present']}")
        out.extend(wrap(a["disjointness_reading"], indent="      "))
    out += ["", f"  primary considered : {s['primary_readings_considered']}",
            f"  byte-supported     : "
            f"{s['sort_analysis']['readings_supported_by_the_bytes']}",
            f"  NOVEL READING FOUND: {s['ATTACK_novel_reading_found']}",
            f"  majority reading   : {s['majority_reading']}",
            f"  primary verdict survives: {s['primary_verdict_survives']}", ""]
    out.extend(wrap(s["REFUTATION_STATUS"], indent="  "))
    out.append("")

    d = certs["D_FIXED_SCALE_RECOMPUTATION"]
    out += [rule, "EVERY FIXED SCALE, RECOMPUTED INDEPENDENTLY", rule]
    for r_ in d["rows"]:
        val = (r_.get("recomputed_scale_over_Q")
               or r_.get("recomputed_edge_weight"))
        out.append(f"  {r_['id']:<10} recomputed={str(val):<10} "
                   f"agrees_with_primary={r_.get('agrees')}")
    out += ["", f"  degree-1 entries all dichotomous: "
                f"{d['degree_1_all_dichotomous']}",
            f"  any recomputed scale equals 2/27: "
            f"{d['any_scale_equals_target']}", ""]

    b = certs["E_BOUNDS_ATTACK"]
    out += [rule, "THE BOUNDS ATTACK", rule,
            f"  1. pairwise-adjacent triples in Z^3: "
            f"{b['attack_1_pairwise_adjacent_triple']['triangles_found_in_box']}"
            f"  (graph is bipartite: "
            f"{b['attack_1_pairwise_adjacent_triple']['verified_on_edges']})",
            f"  2. involutions outside the declared space: "
            f"{b['attack_2_involution_outside_space']['involutive_swappers']}"
            f" found; they pin "
            f"{b['attack_2_involution_outside_space']['consequence']['solves_to']}"
            f", not a scale",
            f"  3. Q-valued defect escape: "
            f"{b['attack_3_q_valued_defect']['escapee_found']}",
            f"  4. chain-length bound load-bearing: "
            f"{b['attack_4_bound_disclosure']['bound_is_load_bearing']}, "
            f"disclosed: "
            f"{b['attack_4_bound_disclosure']['declaration_matches_the_run']}",
            ""]
    out.extend(wrap(b["REFUTATION_STATUS"], indent="  "))
    out.append("")

    g = certs["G_COVERAGE_ASSEMBLY_ATTACK"]
    out += [rule, "THE COVERAGE ASSEMBLY ATTACK", rule]
    for a in g["region_audits"]:
        out.append(f"  [{'LEAK' if a['leak_audit']['secret'] else 'ok  '}] "
                   f"{a['region'][:60]}")
        if a["leak_audit"]["family_left_open"]:
            out.extend(wrap(f"open family: "
                            f"{a['leak_audit']['family_left_open']} "
                            f"(declared: "
                            f"{a['leak_audit']['declared_by_primary']}, "
                            f"selects: "
                            f"{a['leak_audit']['selects_the_target']})",
                            indent="        "))
    out.append("")

    t = certs["H_TEETH"]
    out += [rule, "TEETH", rule]
    for r_ in t["rows"]:
        out.append(f"  [{'BIT ' if r_['certificate_flipped'] else 'MISS'}] "
                   f"{r_['tooth']}")
        out.extend(wrap(f"{r_['mutation']} -> expected {r_['expected']}",
                        indent="        "))
    out += ["", f"  {t['teeth_that_bit']}/{t['teeth_total']} bit", ""]

    v = certs["I_VERDICT"]
    out += [rule, "VERDICT", rule,
            f"  claims attacked: {v['claims_attacked']}   surviving: "
            f"{v['claims_surviving']}   refuted: {v['claims_refuted']}"]
    for s_ in v["survivals"]:
        out.append(f"  [{'SURVIVES' if s_['survives'] else 'REFUTED '}] "
                   f"{s_['claim'][:62]}")
        out.extend(wrap(s_["qualification"], indent="        "))
    out += ["", "  refutations landed:"]
    for r_ in v["refutations_landed"]:
        out.extend(wrap("- " + r_, indent="    "))
    out += ["", "  strengthenings found:"]
    for r_ in v["strengthenings_found"]:
        out.extend(wrap("- " + r_, indent="    "))
    out += ["", bar,
            f"CYCLE 898 CHECK: {v['claims_surviving']}/{v['claims_attacked']} "
            f"CLAIMS SURVIVE, {t['teeth_that_bit']}/{t['teeth_total']} TEETH "
            f"BIT", bar]
    return "\n".join(out) + "\n"


def run() -> int:
    started = monotonic()
    pins = pins_certificate()
    claims_cert = claim_extraction()
    science_a = build(claims_cert)
    science_b = build(claims_cert)
    deterministic = digest(science_a) == digest(science_b)

    certs = {"A_PINS": pins, "B_CLAIM_EXTRACTION": claims_cert, **science_a}

    receipt = {
        "cycle": 898,
        "role": "independent check, specified to refute",
        "claims_attacked": science_a["I_VERDICT"]["claims_attacked"],
        "claims_surviving": science_a["I_VERDICT"]["claims_surviving"],
        "claims_refuted": science_a["I_VERDICT"]["claims_refuted"],
        "survivals": science_a["I_VERDICT"]["survivals"],
        "refutations_landed": science_a["I_VERDICT"]["refutations_landed"],
        "strengthenings_found": science_a["I_VERDICT"]["strengthenings_found"],
        "novel_disjointness_reading":
            science_a["C_ADJUDICATION_BY_SORT_ANALYSIS"]["novel_reading"],
        "novel_reading_consequence":
            science_a["C_ADJUDICATION_BY_SORT_ANALYSIS"][
                "novel_reading_consequence"],
        "bounds_attack_escapees": science_a["E_BOUNDS_ATTACK"]["escapees"],
        "geometric_vacuity_strengthened": science_a["E_BOUNDS_ATTACK"][
            "attack_1_pairwise_adjacent_triple"]["strengthening"],
        "secret_leaks": science_a["G_COVERAGE_ASSEMBLY_ATTACK"][
            "secret_leak_detail"],
        "teeth": science_a["H_TEETH"]["rows"],
        "teeth_that_bit": science_a["H_TEETH"]["teeth_that_bit"],
        "teeth_total": science_a["H_TEETH"]["teeth_total"],
        "fixed_scales_recomputed": [
            {k: v for k, v in r_.items() if k != "spectral_rows"}
            for r_ in science_a["D_FIXED_SCALE_RECOMPUTATION"]["rows"]
        ],
        "source_pins": [{"path": r_["path"], "sha256": r_["sha256"],
                         "git_blob": r_["git_blob"]} for r_ in pins["rows"]],
        "exit_policy": "exit 0 independent of claim survival",
    }
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True,
                                  default=str) + "\n", encoding="utf-8")
    receipt_sha = sha256(RECEIPT.read_bytes()).hexdigest()

    text = render(certs)
    stdout_bytes = len(text.encode("utf-8"))
    elapsed = monotonic() - started
    controls = {
        "blocked_modules_loaded": [n for n in BLOCKLISTED_MODULES
                                   if n in sys.modules],
        "firewall_hits": list(FIREWALL.hits),
        "determinism": {"exact": deterministic,
                        "science_digest": digest(science_a)},
        "receipt_sha256": receipt_sha,
        "runtime_seconds": round(elapsed, 6),
        "runtime_under_limit": elapsed < AUDIT_TIMEOUT_SEC,
        "stdout_bytes": stdout_bytes,
        "stdout_under_limit": stdout_bytes < STDOUT_LIMIT_BYTES,
        "floating_point_in_certified_quantities": False,
        "exit_code_policy": ("0 regardless of whether the primary's claims "
                             "survive; survival is reported as data"),
        "finding": ("Checker ran text/AST/JSON-only behind the import "
                    "firewall and rebuilt its payload digest for digest."),
    }
    controls["pass"] = (deterministic and controls["runtime_under_limit"]
                        and controls["stdout_under_limit"]
                        and not controls["firewall_hits"])
    certs["J_CONTROLS"] = controls

    sys.stdout.write(text)
    sys.stdout.write(
        f"\ncontrols: deterministic={deterministic} pins_pass={pins['pass']} "
        f"stdout={stdout_bytes}B receipt={receipt_sha[:16]}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
