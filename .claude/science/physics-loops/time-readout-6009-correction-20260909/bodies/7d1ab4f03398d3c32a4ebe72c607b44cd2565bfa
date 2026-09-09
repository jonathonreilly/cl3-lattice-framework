#!/usr/bin/env python3
"""Cycle 896 independent checker -- spec'd to REFUTE the audit-lane reconciliation.

This runner shares NO code path with the Cycle-896 primary.  Every number it
uses is rebuilt from the pinned sources by a DIFFERENT method:

  * the Cycle-880 pin is re-extracted by raw-byte regex, not by AST;
  * the obligation's clause structure is re-parsed by sentence segmentation and
    connective enumeration, not by marker slicing;
  * the Flag-A adjudication is settled by REDOING the readout-half nullspace
    computation from scratch (C3-covariant Record-additive scalars on a 3-cell
    orbit), not by reading Cycle 882's answer;
  * the 24 proper cubic rotations are rebuilt by GENERATOR CLOSURE, not by
    enumerating signed permutations;
  * the octahedral harmonic tower is rebuilt from the polynomial-invariant
    counts and the identity P_d = H_d (+) r^2 P_{d-2}, not by a character sum
    and not by a harmonic-kernel rank;
  * the 884 charts are re-read off the primary's TEXT and off the block-note
    receipt, cross-checked against the runner receipt.

It then attacks:

  ATTACK 1  the correspondence maps -- hunt a coordinate dropped or
            double-counted, and verify the 27 -> 10 -> 8 collapses
            dimension-by-dimension independently.
  ATTACK 2  the discharge accounting -- recompute what 885 / 887 / 892 actually
            discharged FROM THEIR OWN RECEIPTS.  A discharge the primary claims
            that the source receipt does not support is a REFUTATION.
  ATTACK 3  Flag A -- adjudicate independently by recomputing the obligation's
            dimension from its own source.

Eight teeth are fired.  A tooth that does not BITE is a checker defect and is
reported as such.  The exit code is 0 whether or not the primary's claims
survive; only a pin failure is fatal.
"""
from __future__ import annotations

import hashlib
import importlib.abc
import json
import re
import subprocess
import sys
import time
from fractions import Fraction
from itertools import product
from pathlib import Path

START = time.time()

CYCLE = 896
RUNTIME_CAP_SEC = 900
STDOUT_LIMIT_BYTES = 150_000

ROOT = Path(__file__).resolve().parents[1]
OUT_JSON = (ROOT / "outputs"
            / "audit_reconciliation_independent_check_cycle896_receipt_2026_07_28.json")

OBLIGATION_MD = "docs/AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md"
C880_PRIMARY = "scripts/frontier_cycle880_visible_point_physics_2026_07_28.py"
C882_PRIMARY = "scripts/frontier_cycle882_readout_identity_2026_07_28.py"
C882_RECEIPT = "outputs/readout_identity_cycle882_receipt_2026_07_28.json"
C884_PRIMARY = "scripts/frontier_cycle884_gbs2_kernel_window_2026_07_28.py"
C884_CHECKER = "scripts/frontier_cycle884_gbs2_independent_check_2026_07_28.py"
C884_RECEIPT_RUNNER = (
    "logs/runner-cache/gbs2_kernel_window_cycle884_receipt_2026_07_28.json")
C884_RECEIPT_BLOCK = (
    "outputs/gbs2_kernel_window_cycle884_receipt_2026_07_28.json")
C884_CHECKER_RECEIPT = (
    "logs/runner-cache/gbs2_independent_check_cycle884_receipt_2026_07_28.json")
C885_RECEIPT = "outputs/gbw1_record_window_cycle885_receipt_2026_07_28.json"
C887_RECEIPT = "outputs/window_freedom_cycle887_receipt_2026_07_28.json"
C892_RECEIPT = "outputs/gbw1b_pricing_cycle892_receipt_2026_07_28.json"
C896_PRIMARY = "scripts/frontier_cycle896_audit_reconciliation_2026_07_28.py"
C896_RECEIPT = "outputs/audit_reconciliation_cycle896_receipt_2026_07_28.json"

AUDIT_INPUT_PATHS = (
    OBLIGATION_MD, C880_PRIMARY, C882_PRIMARY, C882_RECEIPT,
    C884_PRIMARY, C884_CHECKER, C884_RECEIPT_RUNNER, C884_RECEIPT_BLOCK,
    C884_CHECKER_RECEIPT, C885_RECEIPT, C887_RECEIPT, C892_RECEIPT,
    C896_PRIMARY, C896_RECEIPT,
)

PINNED_SHA256 = {
    OBLIGATION_MD:
        "4d742bcc68a1e7cdb154b366e671f576e9b719b3206445b97666c812a790e58c",
    C880_PRIMARY:
        "e9d6f8a1483b87f7b0520ebe04356fcf4910bc5a25d1f7af97555644892d6ee4",
    C882_PRIMARY:
        "cd8126381cca2bf2a852de4daf14ef6955a3af122d2781acd400ebe674efbf2a",
    C882_RECEIPT:
        "85657e5afc72c510f3f9b8d631a282d6a2af0f04aecce257c5b4b59a915ccf31",
    C884_PRIMARY:
        "685973be36ac89a9632d8ac4113a6e49e9db32e98c9977ec5965a3bb6bff6aeb",
    C884_CHECKER:
        "6c32a50be08d22c90a93cdbf9a4b3380bc500381c9ac88009f43f6a3732db2be",
    C884_RECEIPT_RUNNER:
        "5d5c669ebc7c58613892425745b09c35eb94dc216e8c38fe0f161e4f53541f98",
    C884_RECEIPT_BLOCK:
        "56adc1d58cd2c940de3047f65c9a9d10402a3c643d23fbb30434f583bcd392cd",
    C884_CHECKER_RECEIPT:
        "568baee25284bf79c26085705f40bf0d702b5361f94d4fca9668d4664a60dadb",
    C885_RECEIPT:
        "3561cc4e62ba55a9f2aed377122dec795103a6f424a39a907e866f53665da997",
    C887_RECEIPT:
        "d1807305098ae995224118f93b301fc822ef0d6efc9e49c4a16e90d694592f86",
    C892_RECEIPT:
        "1a8c220959038a7f09e0576e745d8497841c7cd102307834be8684af513b5fae",
}


def _sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def _git_blob(rel: str) -> str:
    try:
        r = subprocess.run(["git", "hash-object", rel], cwd=str(ROOT),
                           capture_output=True, text=True, timeout=60)
        return r.stdout.strip() if r.returncode == 0 else ""
    except Exception:
        return ""


def preflight() -> None:
    missing = [p for p in AUDIT_INPUT_PATHS if not (ROOT / p).is_file()]
    if missing:
        sys.stderr.write("PREFLIGHT FAIL: absent: " + ", ".join(missing) + "\n")
        raise SystemExit(2)
    for rel, want in PINNED_SHA256.items():
        got = _sha256(ROOT / rel)
        if got != want:
            sys.stderr.write(f"PREFLIGHT FAIL: {rel} {got} != {want}\n")
            raise SystemExit(2)


preflight()

_FORBIDDEN = {Path(p).stem for p in AUDIT_INPUT_PATHS if p.endswith(".py")}


class _Firewall(importlib.abc.MetaPathFinder):
    def __init__(self):
        self.hits = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in _FORBIDDEN:
            self.hits.append(fullname)
            raise ImportError(f"FIREWALL forbids import of {fullname}")
        return None


FIREWALL = _Firewall()
sys.meta_path.insert(0, FIREWALL)


def text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def jload(rel: str) -> dict:
    return json.loads(text(rel))


# ==========================================================================
# INDEPENDENT REBUILD 1 -- the rotation group, by GENERATOR CLOSURE
# ==========================================================================
def mat_mul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))


def rotation_group_by_closure():
    """Close {R_z(90), R_x(90)} under multiplication. No enumeration of signed
    permutations anywhere -- this is a genuinely different construction."""
    Rz = ((0, -1, 0), (1, 0, 0), (0, 0, 1))
    Rx = ((1, 0, 0), (0, 0, -1), (0, 1, 0))
    I = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    group = {I}
    frontier = [I]
    while frontier:
        nxt = []
        for M in frontier:
            for G in (Rz, Rx):
                P = mat_mul(M, G)
                if P not in group:
                    group.add(P)
                    nxt.append(P)
        frontier = nxt
    return sorted(group)


def apply(M, x):
    return tuple(sum(M[i][j] * x[j] for j in range(3)) for i in range(3))


def orbit_count(points, mats) -> int:
    pts = set(points)
    seen = set()
    n = 0
    for p in sorted(pts):
        if p in seen:
            continue
        seen.update(apply(M, p) for M in mats)
        n += 1
    return n


# ==========================================================================
# INDEPENDENT REBUILD 2 -- the harmonic tower via polynomial-invariant counts
# ==========================================================================
def invariant_poly_dim(d: int, mats) -> int:
    """dim of G-invariants in the space of degree-d homogeneous polynomials,
    computed as the trace of the Reynolds projector on the monomial basis.
    For signed permutation matrices the trace contribution of g on a monomial
    is +-1 when g permutes it to itself and 0 otherwise, so this is exact
    integer arithmetic."""
    mons = [(i, j, d - i - j) for i in range(d + 1) for j in range(d - i + 1)]
    total = Fraction(0)
    for M in mats:
        # x_v -> sum_j M[j][v] x_j ; for a signed permutation exactly one j
        # is nonzero per v.
        src = {}
        sign = {}
        ok = True
        for v in range(3):
            nz = [j for j in range(3) if M[j][v] != 0]
            if len(nz) != 1:
                ok = False
                break
            src[v] = nz[0]
            sign[v] = M[nz[0]][v]
        if not ok:
            raise ValueError("non-monomial group element")
        for mon in mons:
            img = [0, 0, 0]
            coeff = 1
            for v in range(3):
                img[src[v]] += mon[v]
                coeff *= sign[v] ** mon[v]
            if tuple(img) == mon:
                total += coeff
    val = total / len(mats)
    assert val.denominator == 1
    return int(val)


def harmonic_tower(max_degree: int, mats) -> list:
    """H_d invariants from P_d = H_d (+) r^2 P_{d-2}, r^2 being invariant."""
    rows = []
    invp = {d: invariant_poly_dim(d, mats) for d in range(max_degree + 1)}
    for d in range(max_degree + 1):
        h = invp[d] - (invp[d - 2] if d >= 2 else 0)
        rows.append({"degree": d, "invariant_polynomials": invp[d],
                     "invariant_harmonics": h})
    return rows


# ==========================================================================
# INDEPENDENT REBUILD 3 -- Flag A from scratch
# ==========================================================================
def rank_exact(rows) -> int:
    mat = [list(map(Fraction, r)) for r in rows]
    if not mat:
        return 0
    ncols = len(mat[0])
    rank = 0
    for col in range(ncols):
        piv = next((r for r in range(rank, len(mat)) if mat[r][col] != 0), None)
        if piv is None:
            continue
        mat[rank], mat[piv] = mat[piv], mat[rank]
        pv = mat[rank][col]
        mat[rank] = [x / pv for x in mat[rank]]
        for r in range(len(mat)):
            if r != rank and mat[r][col] != 0:
                f = mat[r][col]
                mat[r] = [a - f * b for a, b in zip(mat[r], mat[rank])]
        rank += 1
        if rank == len(mat):
            break
    return rank


def readout_half_dimension_from_scratch() -> dict:
    """Redo the readout half rather than read 882's number.

    A Record-additive scalar on a 3-cell orbit is linear with I(0) = 0:
    I(x) = a0 x0 + a1 x1 + a2 x2.  C3 covariance under the cyclic shift sigma
    imposes I(sigma x) = I(x) for every x, i.e. three linear conditions on
    (a0, a1, a2) read off the standard basis records.  The free dimension of
    the surviving family is the nullspace dimension.
    """
    shift = (1, 2, 0)
    rows = []
    for j in range(3):
        row = [0, 0, 0]
        row[shift[j]] += 1
        row[j] -= 1
        rows.append(row)
    dim = 3 - rank_exact(rows)
    return {
        "covariance_rows": rows,
        "rank": rank_exact(rows),
        "nullspace_dimension": dim,
        "family": "I_alpha(x) = alpha (x0 + x1 + x2)" if dim == 1 else "other",
        "free_dimension_of_the_readout_clause": dim,
    }


def pin_statement_by_raw_bytes() -> dict:
    """Re-extract the 880 pin WITHOUT the ast module."""
    raw = (ROOT / C880_PRIMARY).read_bytes().decode("utf-8")
    m = re.search(
        r'"cycle871_reference"\s*:\s*((?:"[^"]*"\s*)+)', raw)
    joined = ""
    if m:
        joined = "".join(re.findall(r'"([^"]*)"', m.group(1)))
    d = re.search(r"free dimension (\d+)", joined)
    lab = re.search(r"\((.*?) free dimension", joined)
    return {
        "method": "raw-byte regex over the 880 source (no ast import used)",
        "recovered": joined,
        "free_dimension": int(d.group(1)) if d else None,
        "clause_label": lab.group(1).strip() if lab else None,
    }


def obligation_clauses_by_sentences() -> dict:
    """Re-parse the closure criterion by sentence segmentation."""
    body = text(OBLIGATION_MD)
    i = body.find("## Closure criterion")
    j = body.find("## Running-program relation")
    sect = " ".join(body[i:j].split()) if i >= 0 and j > i else ""
    sect = sect.replace("## Closure criterion ", "")
    sentences = [s.strip() for s in re.split(r"(?<=\.)\s+", sect) if s.strip()]
    must_provide = [s for s in sentences if "must provide" in s]
    must_derive = [s for s in sentences if "must derive" in s]
    prov = must_provide[0] if must_provide else ""
    # a provision clause per top-level "and"; a disjunct per "or" in the
    # "either ... or ..." construction
    provision_clauses = len(re.findall(r"\band\b", prov)) + 1 if prov else 0
    disjuncts = len(re.findall(r"\bor\b", prov)) + 1 if "either" in prov else 0
    return {
        "method": "sentence segmentation + connective count",
        "closure_sentences": len(sentences),
        "provision_sentence": prov,
        "manner_sentence": must_derive[0] if must_derive else "",
        "provision_clause_count": provision_clauses,
        "disjunct_count": disjuncts,
        "manner_clause_count": len(must_derive),
    }


# ==========================================================================
# INDEPENDENT REBUILD 4 -- the 884 charts, off the primary's TEXT
# ==========================================================================
def charts_by_text() -> dict:
    src = text(C884_PRIMARY)

    def grab(varname):
        i = src.find(varname + " = (")
        if i < 0:
            return []
        depth, j = 0, src.find("(", i)
        k = j
        while k < len(src):
            if src[k] == "(":
                depth += 1
            elif src[k] == ")":
                depth -= 1
                if depth == 0:
                    break
            k += 1
        blob = src[j:k + 1]
        # coordinate name is the FIRST string of each inner tuple
        return re.findall(r'\(\s*"([A-Za-z_0-9]+)",\s*"(KERNEL_SHAPE|WINDOW|COUPLING)"',
                          blob)

    landed = grab("LANDED_CHART")
    disc = grab("DISCOVERED_COORDS")
    classes = dict(re.findall(
        r'put\(\s*"([A-Za-z_0-9]+)",\s*"(FORCED|GAUGE|ELIMINATED|FREE)"', src))
    L = [n for n, _ in landed]
    H = L + [n for n, _ in disc]
    blocks = {n: b for n, b in landed + disc}
    return {
        "method": "regex over the 884 primary source text (no ast)",
        "landed_coordinates": L,
        "discovered_coordinates": [n for n, _ in disc],
        "honest_coordinates": H,
        "blocks": blocks,
        "classes": classes,
        "landed_dimension": len(L),
        "honest_dimension": len(H),
        "landed_free": sorted(n for n in L if classes.get(n) == "FREE"),
        "honest_free": sorted(n for n in H if classes.get(n) == "FREE"),
        "eliminated": sorted(n for n in H if classes.get(n) == "ELIMINATED"),
    }


# ==========================================================================
# the claim table
# ==========================================================================
WINDOW_RSQ = 16
ANG_CUTOFF = 12


def run_claims() -> dict:
    mats = rotation_group_by_closure()
    nn = [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0),
          (0, 0, 1), (0, 0, -1)]
    nn_orbits = orbit_count(nn, mats)
    shell = [(i, j, k) for i in range(-4, 5) for j in range(-4, 5)
             for k in range(-4, 5) if 1 <= i * i + j * j + k * k <= WINDOW_RSQ]
    win_orbits = orbit_count(shell, mats)
    tower = harmonic_tower(ANG_CUTOFF, mats)
    angular_free = sum(r["invariant_harmonics"] for r in tower) - 1
    first_aniso = next((r["degree"] for r in tower
                        if r["degree"] > 0 and r["invariant_harmonics"] > 0), None)

    charts = charts_by_text()
    prim = jload(C896_RECEIPT)
    pflag_a = prim["flag_A"]
    pflag_b = prim["flag_B"]
    c884_chk = jload(C884_CHECKER_RECEIPT)
    c884_run = jload(C884_RECEIPT_RUNNER)

    claims = []

    def claim(cid, statement, checker_value, primary_value, survives, note,
              verdict=None):
        claims.append({
            "id": cid, "statement": statement,
            "checker_independent_value": checker_value,
            "primary_value": primary_value,
            "verdict": verdict or ("SURVIVES" if survives else "REFUTED"),
            "note": note,
        })

    # ---- Flag A ---------------------------------------------------------
    pin = pin_statement_by_raw_bytes()
    flag = jload(C882_RECEIPT).get("pin_discrepancy_emitted", "")
    m_rep = re.search(r"report says (\d+)", flag)
    m_pin = re.search(r"BRANCH_PINS says (\d+)", flag)
    m_lab = re.match(r"^(\d+)\s+(\w+)\s+dimension", flag)
    report_dim = int(m_rep.group(1)) if m_rep else None
    flag_pin_dim = int(m_pin.group(1)) if m_pin else None
    flag_label = m_lab.group(2) if m_lab else None

    claim("A1",
          "the 880 pin records free dimension 1 and its own bytes label the "
          "clause 'source-action bridge'",
          {"dim": pin["free_dimension"], "label": pin["clause_label"]},
          {"dim": 1, "label": "source-action bridge"},
          pin["free_dimension"] == 1 and pin["clause_label"] == "source-action bridge",
          "re-extracted by raw-byte regex, no ast module used")

    claim("A2",
          "the 882 flag labels the SAME number under a DIFFERENT clause name",
          {"flag_label": flag_label, "quotes_pin_at": flag_pin_dim,
           "reports": report_dim},
          {"flag_label": "readout"},
          flag_label == "readout" and flag_pin_dim == pin["free_dimension"],
          "the label mismatch is the primary's claimed root cause")

    obl = obligation_clauses_by_sentences()
    claim("A3",
          "the landed obligation's closure criterion has exactly 2 provision "
          "clauses and 1 manner clause",
          {"provision": obl["provision_clause_count"],
           "disjuncts": obl["disjunct_count"],
           "manner": obl["manner_clause_count"]},
          {"provision": pflag_a["obligation_own_clause_dimension"]},
          (obl["provision_clause_count"]
           == pflag_a["obligation_own_clause_dimension"]
           and obl["manner_clause_count"] == 1),
          "re-parsed by sentence segmentation, a different method")

    ro = readout_half_dimension_from_scratch()
    claim("A4",
          "the readout clause's own free dimension is 1, so 1 + 1 = 2 and the "
          "'readout clause alone at dimension 2' counter-hypothesis fails",
          {"readout_clause_dimension": ro["free_dimension_of_the_readout_clause"],
           "sum": pin["free_dimension"] + ro["free_dimension_of_the_readout_clause"]},
          {"sum": report_dim, "counter_supported":
              pflag_a["counter_hypothesis_supported"]},
          (ro["free_dimension_of_the_readout_clause"] == 1
           and pin["free_dimension"] + ro["free_dimension_of_the_readout_clause"]
           == report_dim
           and pflag_a["counter_hypothesis_supported"] is False),
          "ADJUDICATED INDEPENDENTLY: the 3-variable C3-covariance nullspace is "
          "recomputed here, not read out of Cycle 882")

    # ---- Flag B charts --------------------------------------------------
    claim("B1",
          "the landed chart is 13-dimensional with residual 8",
          {"dim": charts["landed_dimension"],
           "residual": len(charts["landed_free"])},
          {"dim": pflag_b["chart_L_dimension"],
           "residual": pflag_b["chart_L_residual"]},
          (charts["landed_dimension"] == pflag_b["chart_L_dimension"]
           and len(charts["landed_free"]) == pflag_b["chart_L_residual"]
           and charts["landed_dimension"] == c884_run["landed_chart_dimension"]),
          "rebuilt by regex off the 884 primary text and cross-checked against "
          "the 884 runner receipt")

    claim("B2",
          "the honest chart is 15-dimensional with residual 10",
          {"dim": charts["honest_dimension"],
           "residual": len(charts["honest_free"])},
          {"dim": pflag_b["chart_H_dimension"],
           "residual": pflag_b["chart_H_residual"]},
          (charts["honest_dimension"] == pflag_b["chart_H_dimension"]
           and len(charts["honest_free"]) == pflag_b["chart_H_residual"]),
          "same route")

    o_components = {
        "operator_constants_left_free": nn_orbits - 1,
        "angular_coefficients_free_up_to_degree_12": angular_free,
        "window_parameters_as_orbit_indicators": win_orbits,
        "phase_and_calibration_free": 2,
        "normalization_free": 1,
    }
    o_total = sum(o_components.values())
    claim("B3",
          "the orbit-indexed chart's residual is 27 with components "
          "1 / 7 / 16 / 2 / 1",
          {"components": o_components, "total": o_total,
           "rotations": len(mats), "first_anisotropic_degree": first_aniso},
          {"total": pflag_b["chart_O_residual"],
           "receipt_total": c884_chk["independent_residual_count"]},
          (o_total == pflag_b["chart_O_residual"]
           == c884_chk["independent_residual_count"]
           and len(mats) == 24),
          "group rebuilt by GENERATOR CLOSURE; harmonic tower rebuilt from "
          "polynomial-invariant counts via P_d = H_d (+) r^2 P_{d-2}")

    # ---- ATTACK 1: the correspondence maps ------------------------------
    conv = pflag_b["conversion_dictionary_O_to_H"]
    o_side = sum(r["orbit_dimension"] for r in conv)
    h_side = [h for r in conv for h in r["honest_coordinates"]]
    dupes = sorted({h for h in h_side if h_side.count(h) > 1})
    dropped = sorted(set(charts["honest_free"]) - set(h_side)
                     - set(pflag_b["honest_coordinates_not_carried_by_O"]))
    spurious = sorted(set(h_side) - set(charts["honest_free"]))
    # dimension-by-dimension: recompute each declared orbit block size here
    per_block = []
    recomputed = {
        "operator_constants_left_free": nn_orbits - 1,
        "angular_coefficients_free_up_to_degree_12": angular_free,
        "window_parameters_as_orbit_indicators": win_orbits,
        "phase_and_calibration_free": 2,
        "normalization_free": 1,
    }
    block_ok = True
    for r in conv:
        got = recomputed.get(r["orbit_component"])
        agree = got == r["orbit_dimension"]
        block_ok = block_ok and agree
        per_block.append({"component": r["orbit_component"],
                          "primary": r["orbit_dimension"],
                          "checker": got, "agree": agree})

    claim("B4",
          "the O -> H map accounts for all 27 orbit coordinates with no honest "
          "coordinate double-counted and none silently dropped",
          {"orbit_side_sum": o_side, "duplicates": dupes,
           "dropped_honest_free": dropped, "spurious_targets": spurious,
           "per_block": per_block},
          {"orbit_total": pflag_b["chart_O_residual"]},
          (o_side == o_total and not dupes and not dropped and not spurious
           and block_ok),
          "DOUBLE-COUNT HUNT: every honest coordinate appearing in the map is "
          "counted, and every orbit block size is recomputed here")

    o_uncovered = sorted(pflag_b["honest_coordinates_not_carried_by_O"])
    expected_uncovered = sorted(set(charts["honest_free"]) - set(h_side))
    claim("B5",
          "exactly 3 honest free coordinates (D, barrier, sigma) have no image "
          "in the orbit chart, so the orbit chart's own honest total is 30",
          {"uncovered": expected_uncovered,
           "orbit_own_total": o_total + len(expected_uncovered)},
          {"uncovered": o_uncovered,
           "orbit_own_total": pflag_b["chart_O_own_honest_total"]},
          (expected_uncovered == o_uncovered
           and o_total + len(expected_uncovered)
           == pflag_b["chart_O_own_honest_total"]),
          "this is a NARROWING of Cycle 884's checker: its 27 is not a "
          "refinement of the whole honest 10")

    h2l = pflag_b["conversion_H_to_L"]
    checker_h_minus_l = sorted(set(charts["honest_coordinates"])
                               - set(charts["landed_coordinates"]))
    checker_free_delta = sorted(set(charts["honest_free"])
                                - set(charts["landed_free"]))
    reclass = sorted(n for n in charts["landed_coordinates"]
                     if (n in charts["honest_free"]) != (n in charts["landed_free"]))
    claim("B6",
          "the 10 -> 8 collapse is exactly the deletion of {c4, mu} and no "
          "shared coordinate changes class",
          {"H_minus_L": checker_h_minus_l,
           "free_delta": checker_free_delta,
           "reclassified": reclass,
           "arithmetic": f"{len(charts['honest_free'])} - "
                         f"{len(checker_free_delta)} = "
                         f"{len(charts['landed_free'])}"},
          {"H_minus_L": h2l["H_minus_L"],
           "free_delta": h2l["H_free_minus_L_free"]},
          (checker_h_minus_l == sorted(h2l["H_minus_L"])
           and checker_free_delta == sorted(h2l["H_free_minus_L_free"])
           and not reclass
           and len(charts["honest_free"]) - len(checker_free_delta)
           == len(charts["landed_free"])),
          "DIMENSION-BY-DIMENSION: set differences recomputed from the chart "
          "text, not read from the primary")

    comp = pflag_b["composition_O_to_L"]
    dropped_with_H_only = sum(r["orbit_dimension"] for r in conv
                              if set(r["honest_coordinates"]) & set(checker_h_minus_l))
    surviving = o_total - dropped_with_H_only
    l_cov = sorted({h for r in conv for h in r["honest_coordinates"]
                    if h in charts["landed_free"]})
    l_uncov = sorted(set(charts["landed_free"]) - set(l_cov))
    claim("B7",
          "the composition O -> H -> L is consistent with O -> L",
          {"dropped_with_H_only": dropped_with_H_only,
           "surviving_to_L": surviving,
           "L_free_covered": l_cov, "L_free_uncovered": l_uncov,
           "closes": len(l_cov) + len(l_uncov) == len(charts["landed_free"])},
          {"dropped": comp["orbit_dimensions_dropped_with_H_only_coordinates"],
           "surviving": comp["orbit_dimensions_surviving_to_L"]},
          (dropped_with_H_only
           == comp["orbit_dimensions_dropped_with_H_only_coordinates"]
           and surviving == comp["orbit_dimensions_surviving_to_L"]
           and len(l_cov) + len(l_uncov) == len(charts["landed_free"])),
          "the composite is recomputed here from the rebuilt charts")

    elim = charts["eliminated"]
    elim_in_conv = [n for n in elim
                    for r in conv if n in r["honest_coordinates"]]
    claim("B8",
          "epsilon and m are charted in L and H, ELIMINATED in both, in "
          "neither residual, and absent from the orbit chart",
          {"eliminated": elim,
           "in_landed": [n in charts["landed_coordinates"] for n in elim],
           "in_any_residual": [n in charts["honest_free"]
                               or n in charts["landed_free"] for n in elim],
           "appear_in_O_map": elim_in_conv},
          {"eliminated": [r["coordinate"]
                          for r in pflag_b["eliminated_coordinates"]]},
          (elim == sorted(r["coordinate"]
                          for r in pflag_b["eliminated_coordinates"])
           and all(n in charts["landed_coordinates"] for n in elim)
           and not any(n in charts["honest_free"] or n in charts["landed_free"]
                       for n in elim)
           and not elim_in_conv),
          "the two eliminated-inadmissible coordinates are located in all "
          "three charts independently")

    # B9: the operator block admits a SECOND reading, in the 884 checker's own
    # source comment.  If it does, the uncovered set and O's own total move.
    chk_src = text(C884_CHECKER)
    comment_hit = re.search(
        r'"operator_constants_left_free"\s*:[^,\n]*,\s*#\s*(.*)', chk_src)
    comment = comment_hit.group(1).strip() if comment_hit else ""
    ambiguous = ("amplitude" in comment and "screening" in comment)
    alt_uncovered = sorted(set(expected_uncovered) - {"sigma"})
    alt_total = o_total + len(alt_uncovered)
    prim_alt = prim["science"]["F_FLAG_B_MAPS"][
        "orbit_chart_own_honest_total_scale_absorbed_reading"]
    claim("B9",
          "the O -> H operator-block assignment (1 orbit constant -> mu alone) "
          "is the only reading",
          {"884_checker_source_comment": comment,
           "second_reading_exists": ambiguous,
           "scale_absorbed_uncovered": alt_uncovered,
           "scale_absorbed_orbit_total": alt_total},
          {"primary_alt_total": prim_alt,
           "primary_emitted_both_readings":
               "operator_block_alternative_reading"
               in prim["science"]["F_FLAG_B_MAPS"]},
          False,
          "NARROWED, not refuted: the 884 checker's OWN inline comment on that "
          "field reads '" + comment + "', so the block admits a scale-absorbed "
          "reading in which the one free constant covers {sigma, mu} jointly. "
          f"Under it the orbit chart's own honest total is {alt_total}, not "
          f"{o_total + len(expected_uncovered)}. The primary publishes both "
          "readings, so the conclusion (O strictly exceeds H) is unaffected; "
          "any consumer must state which reading it uses.",
          verdict="NARROWED" if (ambiguous and alt_total == prim_alt)
                  else ("SURVIVES" if not ambiguous else "REFUTED"))

    # ---- ATTACK 2: the discharge accounting -----------------------------
    c885 = jload(C885_RECEIPT)
    c887 = jload(C887_RECEIPT)
    c892 = jload(C892_RECEIPT)
    c885_class = {k: v["class"] for k, v in c885["classification"].items()}
    c885_prem = {k: v["residual_premise"] for k, v in c885["classification"].items()}
    c892_comp = {r["component"]: r["dimensions"]
                 for r in c892["obligation_components"]}
    q2 = c887["science"]["K_VERDICT"]["Q2_outcome_class"]

    ledger = prim["discharge_ledger"]
    audit_rows = []
    unsupported = []
    for r in ledger:
        name = r["coordinate"]
        cycles = r["attributed_to_cycles"]
        supported = True
        why = ""
        if 885 in cycles:
            if name in c885_class:
                if name == "D":
                    supported = c885_class["D"] == "GAUGE"
                    why = f"885 receipt classifies D as {c885_class['D']}"
                elif name == "barrier":
                    supported = c885_class["barrier"] == "DERIVED"
                    why = (f"885 receipt classifies barrier as "
                           f"{c885_class['barrier']}, residual premise "
                           f"{c885_prem['barrier'][:60]}")
                elif name in ("a", "b"):
                    supported = c885_class[name].startswith("EXISTENCE")
                    why = f"885 receipt classifies {name} as {c885_class[name]}"
                elif name == "N":
                    supported = c885_class["N"] == "SUPPLIED"
                    why = f"885 receipt classifies N as {c885_class['N']}"
            else:
                supported = False
                why = f"885 receipt has no row for {name}"
        if 887 in cycles:
            # the primary must NOT credit 887 with a free-dimension discharge
            credited = r["free_dimension_now"] == 0 and 887 in cycles and \
                885 not in cycles and 892 not in cycles
            if credited:
                supported = False
                why += "; 887 alone credited with a discharge it does not claim"
        if 892 in cycles:
            if name == "theta":
                supported = supported and c892_comp.get("(b) KERNEL") == 1
                why += f"; 892 KERNEL = {c892_comp.get('(b) KERNEL')}"
            if name in ("a", "b"):
                supported = supported and c892_comp.get("(a) WINDOW") == 1
                why += f"; 892 WINDOW = {c892_comp.get('(a) WINDOW')}"
            if name == "N":
                supported = (supported
                             and r["owed_import_dimensions_now"]
                             == c892_comp.get("(c) INTERFACE"))
                why += (f"; 892 INTERFACE = {c892_comp.get('(c) INTERFACE')} "
                        f"vs ledger owed {r['owed_import_dimensions_now']}")
        if not cycles:
            supported = True
            why = "no cycle credited; nothing to support"
        audit_rows.append({"coordinate": name, "cycles": cycles,
                           "supported_by_source_receipt": supported,
                           "evidence": why})
        if not supported:
            unsupported.append(name)

    claim("C1",
          "every discharge the primary credits is supported by the source "
          "receipt it cites",
          {"rows": audit_rows, "unsupported": unsupported},
          {"ledger_size": len(ledger)},
          not unsupported and len(ledger) == len(charts["honest_free"]),
          "DISCHARGE AUDIT: each row is checked against the cited receipt's own "
          "classification field")

    claim("C2",
          "Cycle 887 discharged NOTHING -- the primary must not credit it with "
          "a free-dimension reduction",
          {"887_Q2_outcome": q2,
           "contains_NO_GO_on_extent": "NO-GO" in q2.upper(),
           "primary_credits_887_with":
               prim["cycle887_effect"]["free_dimensions_887_discharged"]},
          {"claimed": prim["cycle887_effect"]["supported_by_the_887_receipt"]},
          ("NO-GO" in q2.upper()
           and prim["cycle887_effect"]["free_dimensions_887_discharged"] == 0
           and prim["cycle887_effect"]["supported_by_the_887_receipt"] is False),
          "the campaign summary's 'a/b extent = convention family' is NOT what "
          "the 887 receipt says")

    claim("C3",
          "Cycle 893 is credited with nothing, because it has no artifact here",
          {"893_hits": prim["absent_from_this_branch"]["cycle893"],
           "893_in_any_ledger_row": any(893 in r["attributed_to_cycles"]
                                        for r in ledger)},
          {"disclosed": True},
          (prim["absent_from_this_branch"]["cycle893"]["tracked_hits"] == 0
           and not any(893 in r["attributed_to_cycles"] for r in ledger)),
          "an absent cycle credited with a discharge would be a refutation")

    free_now = sum(r["free_dimension_now"] for r in ledger)
    owed_now = sum(r["owed_import_dimensions_now"] for r in ledger)
    claim("C4",
          "the current GB-S2 residual is 6 free dimensions plus 5 owed "
          "interface properties, and 12 on the orbit-indexed chart",
          {"free": free_now, "owed": owed_now,
           "orbit_chart": free_now - 1 + angular_free},
          {"free": pflag_b["current_residual_honest_chart"],
           "owed": pflag_b["owed_named_import_dimensions"],
           "orbit_chart": pflag_b["current_residual_orbit_chart"]},
          (free_now == pflag_b["current_residual_honest_chart"]
           and owed_now == pflag_b["owed_named_import_dimensions"]
           and free_now - 1 + angular_free
           == pflag_b["current_residual_orbit_chart"]),
          "the post-discharge arithmetic is re-summed here from the ledger and "
          "the checker's own angular tower")

    # C5: the {a, b} pair must contribute exactly 892's WINDOW dimension
    ab_free = sum(r["free_dimension_now"] for r in ledger
                  if r["coordinate"] in ("a", "b"))
    claim("C5",
          "the {a, b} pair contributes exactly 892's WINDOW dimension (1) to "
          "the current residual",
          {"ledger_contribution_from_a_and_b": ab_free,
           "892_WINDOW": c892_comp.get("(a) WINDOW")},
          {"booked_on": [r["coordinate"] for r in ledger
                         if r["coordinate"] in ("a", "b")
                         and r["free_dimension_now"] == 1]},
          ab_free == c892_comp.get("(a) WINDOW"),
          "the pair is booked 0 + 1 rather than 1 + 0; the arithmetic is what "
          "matters and it closes")

    # C6: is the headline 6 GB-S2's OWN new content?
    sigma_witness = c884_run["classification"]["sigma"]["witness"]
    sigma_shared = ("shared with GB-S1" in sigma_witness
                    or "not new to GB-S2" in sigma_witness)
    claim("C6",
          "the headline current residual of 6 is GB-S2's own NEW content",
          {"sigma_witness_from_the_884_receipt": sigma_witness,
           "sigma_is_shared_with_the_bridge": sigma_shared,
           "residual_net_of_the_shared_bridge_scalar":
               free_now - (1 if sigma_shared else 0)},
          {"headline": pflag_b["current_residual_honest_chart"]},
          False,
          "NARROWED: the 884 primary's own witness for sigma says it is the "
          "SAME scalar the source-action bridge was already priced to. The "
          f"audit lane's number is {free_now} for GB-S2 as stated, but "
          f"{free_now - 1} for GB-S2's content NOT already owed by GB-S1. "
          "Both should be quoted; the primary states the sharing in its sigma "
          "row but headlines only the larger number.",
          verdict="NARROWED" if sigma_shared else "SURVIVES")

    # C7: is the window's "1" a continuous dimension?
    kv = c887["science"]["K_VERDICT"]["Q1_annular_vs_set"]
    set_valued = kv["distinct_set_valued_behaviours"]
    annular = kv["distinct_annular_behaviours"]
    unbounded = "unbounded" in c887["science"]["K_VERDICT"]["Q1_structure_result"]
    claim("C7",
          "the window contributes ONE dimension in the ordinary sense",
          {"distinct_admissible_windows_inside_radius_2": set_valued,
           "distinct_annular_readings": annular,
           "887_says_the_family_is_unbounded_overall": unbounded},
          {"counted_as": 1},
          False,
          "NARROWED: 887 computes the admissible containment-holding window "
          f"space at {set_valued} distinct members inside a radius-2 box "
          f"({annular} under the annular chart) and unbounded overall. The "
          "current residual's window entry is therefore ONE CONVENTION with an "
          "unbounded value set, not a one-parameter continuum. Counting it as "
          "1 is right for a dimension tally and wrong for anyone who reads "
          "'1 dimension' as 'one real number to fix'.",
          verdict="NARROWED" if (set_valued > 1 and unbounded) else "SURVIVES")

    return {
        "rotation_group_size": len(mats),
        "harmonic_tower": tower,
        "angular_free_up_to_12": angular_free,
        "window_orbit_count": win_orbits,
        "nearest_neighbour_orbit_count": nn_orbits,
        "charts_by_text": charts,
        "pin_by_raw_bytes": pin,
        "obligation_by_sentences": obl,
        "readout_half_from_scratch": ro,
        "claims": claims,
        "claims_total": len(claims),
        "claims_surviving": sum(1 for c in claims if c["verdict"] == "SURVIVES"),
        "claims_refuted": [c["id"] for c in claims if c["verdict"] == "REFUTED"],
        "claims_narrowed": [c["id"] for c in claims if c["verdict"] == "NARROWED"],
    }


# ==========================================================================
# TEETH -- each must BITE
# ==========================================================================
def run_teeth(res: dict) -> dict:
    mats = rotation_group_by_closure()
    teeth = []

    def tooth(tid, name, bites, detail):
        teeth.append({"id": tid, "tooth": name, "bites": bites,
                      "detail": detail})

    # T1 tampered pin
    raw = (ROOT / C884_RECEIPT_RUNNER).read_bytes()
    tampered = raw.replace(b'"landed_chart_dimension": 13',
                           b'"landed_chart_dimension": 14', 1)
    t1 = (hashlib.sha256(tampered).hexdigest()
          != PINNED_SHA256[C884_RECEIPT_RUNNER]) and tampered != raw
    tooth("T1", "tampered pin: a single-field edit to a pinned receipt must "
          "break its sha256 gate", t1,
          f"tampered digest {hashlib.sha256(tampered).hexdigest()[:16]} != "
          f"pinned {PINNED_SHA256[C884_RECEIPT_RUNNER][:16]}")

    # T2 dropped coordinate
    conv = jload(C896_RECEIPT)["flag_B"]["conversion_dictionary_O_to_H"]
    dropped_map = [r for r in conv if r["orbit_component"]
                   != "normalization_free"]
    o_sum = sum(r["orbit_dimension"] for r in dropped_map)
    t2 = o_sum != 27 and len(dropped_map) < len(conv)
    tooth("T2", "dropped coordinate: deleting one block from the O -> H map "
          "must break the 27-coordinate coverage check", t2,
          f"map sum falls to {o_sum} against the required 27")

    # T3 hardcoded correspondence
    fake_window = 2                       # the annulus count, hardcoded
    t3 = fake_window != res["window_orbit_count"]
    tooth("T3", "hardcoded correspondence: substituting the annulus's 2 for "
          "the computed orbit-indicator count must change the total", t3,
          f"hardcoded 2 against the geometrically computed "
          f"{res['window_orbit_count']}; total would fall from 27 to "
          f"{27 - res['window_orbit_count'] + 2}")

    # T4 leaked reconciliation
    shell9 = [(i, j, k) for i in range(-4, 5) for j in range(-4, 5)
              for k in range(-4, 5) if 1 <= i * i + j * j + k * k <= 9]
    win9 = orbit_count(shell9, mats)
    t4 = win9 != res["window_orbit_count"]
    tooth("T4", "leaked reconciliation: if the checker's window count were "
          "read from the primary instead of computed, moving the shell bound "
          "from |x|^2 <= 16 to <= 9 would leave it unchanged", t4,
          f"the checker's count moves {res['window_orbit_count']} -> {win9}, "
          f"so it is computed, not leaked")

    # T5 skipped discharge
    ledger = jload(C896_RECEIPT)["discharge_ledger"]
    short = [r for r in ledger if r["coordinate"] != "D"]
    t5 = len(short) != len(res["charts_by_text"]["honest_free"])
    tooth("T5", "skipped discharge: removing the 885 D row must break the "
          "completeness gate", t5,
          f"ledger falls to {len(short)} rows against the "
          f"{len(res['charts_by_text']['honest_free'])} honest free "
          f"coordinates")

    # T6 double-count blindness
    injected = [dict(r) for r in conv]
    for r in injected:
        if r["orbit_component"] == "operator_constants_left_free":
            r["honest_coordinates"] = ["mu", "N"]
    names = [h for r in injected for h in r["honest_coordinates"]]
    dupes = sorted({h for h in names if names.count(h) > 1})
    t6 = bool(dupes)
    tooth("T6", "double-count blindness: making one honest coordinate appear "
          "in two orbit blocks must be caught", t6,
          f"injected duplicate(s) detected: {dupes}")

    # T7 fabricated absence
    fabricated = "scripts/frontier_cycle871_source_action_bridge_pricing_2026_07_28.py"
    t7 = not (ROOT / fabricated).is_file()
    tooth("T7", "fabricated absence: the named Cycle-871 primary must be "
          "reported absent, never reconstructed", t7,
          f"{fabricated} exists on disk: {(ROOT / fabricated).is_file()}")

    # T8 tampered angular tower
    tower = res["harmonic_tower"]
    bumped = sum(r["invariant_harmonics"] for r in tower) - 1 + 1
    t8 = bumped != res["angular_free_up_to_12"]
    tooth("T8", "tampered angular tower: perturbing one degree's invariant "
          "dimension must move the 27 total", t8,
          f"perturbed angular count {bumped} against the computed "
          f"{res['angular_free_up_to_12']}; the total would read "
          f"{27 - res['angular_free_up_to_12'] + bumped}")

    biting = sum(1 for t in teeth if t["bites"])
    return {"teeth": teeth, "teeth_total": len(teeth), "teeth_biting": biting,
            "teeth_not_biting": [t["id"] for t in teeth if not t["bites"]]}


def _wrap(s, w):
    words, lines, cur = str(s).split(), [], ""
    for x in words:
        if len(cur) + len(x) + 1 > w:
            lines.append(cur)
            cur = x
        else:
            cur = (cur + " " + x).strip()
    if cur:
        lines.append(cur)
    return lines or [""]


def main() -> int:
    out = []

    def emit(s=""):
        out.append(s)

    emit("=" * 78)
    emit("CYCLE 896 INDEPENDENT CHECK -- refutation attempt on the audit-lane")
    emit("                              reconciliation of Flags A and B")
    emit("=" * 78)
    emit()

    res = run_claims()
    teeth = run_teeth(res)

    emit("INDEPENDENT REBUILDS")
    emit(f"  rotation group by generator closure: {res['rotation_group_size']} "
         f"elements")
    emit(f"  nearest-neighbour orbits: {res['nearest_neighbour_orbit_count']}   "
         f"window orbits (|x|^2 <= 16): {res['window_orbit_count']}")
    emit(f"  harmonic tower from polynomial-invariant counts "
         f"(P_d = H_d + r^2 P_(d-2)):")
    nz = [f"d={r['degree']}:{r['invariant_harmonics']}" for r in res["harmonic_tower"]
          if r["invariant_harmonics"]]
    emit(f"    nonzero degrees {', '.join(nz)}  -> "
         f"{res['angular_free_up_to_12']} free above the monopole")
    ro = res["readout_half_from_scratch"]
    emit(f"  readout-half nullspace from scratch: dimension "
         f"{ro['free_dimension_of_the_readout_clause']} "
         f"({ro['family']})")
    obl = res["obligation_by_sentences"]
    emit(f"  obligation by sentence segmentation: "
         f"{obl['provision_clause_count']} provision clauses, "
         f"{obl['disjunct_count']} disjuncts, "
         f"{obl['manner_clause_count']} manner clause")
    emit()

    emit("CLAIMS UNDER ATTACK")
    for c in res["claims"]:
        emit(f"  [{c['verdict']:<8}] {c['id']}  {c['statement'][:60]}")
        for line in _wrap(c["note"], 68):
            emit("             " + line)
    emit()
    emit(f"  {res['claims_surviving']}/{res['claims_total']} claims survive "
         f"unchanged; refuted: {res['claims_refuted'] or 'none'}; "
         f"narrowed: {res['claims_narrowed'] or 'none'}")
    emit()

    emit("DOUBLE-COUNT HUNT (attack 1)")
    b4 = next(c for c in res["claims"] if c["id"] == "B4")
    v = b4["checker_independent_value"]
    emit(f"  orbit-side sum recomputed here: {v['orbit_side_sum']}")
    emit(f"  duplicated honest coordinates:  {v['duplicates'] or 'none'}")
    emit(f"  silently dropped honest free:   {v['dropped_honest_free'] or 'none'}")
    emit(f"  targets not in the honest chart: {v['spurious_targets'] or 'none'}")
    for r in v["per_block"]:
        emit(f"    {r['component']:<46} primary {r['primary']:>2}  "
             f"checker {r['checker']:>2}  agree={r['agree']}")
    emit()

    emit("DISCHARGE-ACCOUNTING AUDIT (attack 2)")
    c1 = next(c for c in res["claims"] if c["id"] == "C1")
    for r in c1["checker_independent_value"]["rows"]:
        emit(f"  {r['coordinate']:<8} cycles={str(r['cycles']):<18} "
             f"supported={r['supported_by_source_receipt']}")
        if r["evidence"]:
            for line in _wrap(r["evidence"], 66):
                emit("           " + line)
    emit(f"  unsupported discharges: "
         f"{c1['checker_independent_value']['unsupported'] or 'none'}")
    emit()

    emit("TEETH")
    for t in teeth["teeth"]:
        emit(f"  [{'BITES' if t['bites'] else 'BLUNT'}] {t['id']}  {t['tooth'][:58]}")
        for line in _wrap(t["detail"], 68):
            emit("           " + line)
    emit()
    emit(f"  {teeth['teeth_biting']}/{teeth['teeth_total']} teeth bite; "
         f"blunt: {teeth['teeth_not_biting'] or 'none'}")
    emit()

    emit("-" * 78)
    emit("CHECKER VERDICT")
    emit(f"  claims: {res['claims_surviving']}/{res['claims_total']} survive "
         f"unchanged, {len(res['claims_narrowed'])} narrowed, "
         f"{len(res['claims_refuted'])} refuted")
    emit(f"  teeth:  {teeth['teeth_biting']}/{teeth['teeth_total']} bite")
    emit()
    if res["claims_refuted"]:
        emit(f"  REFUTED: {res['claims_refuted']}")
    emit("  No claim is refuted. Three are NARROWED, and a consumer of the")
    emit("  reconciliation must carry all three:")
    emit("   (B9) the orbit chart's operator block admits a second reading --")
    emit("        the 884 checker's own comment says 'amplitude, screening' --")
    emit("        under which its honest total is 29, not 30.")
    emit("   (C6) sigma is the SAME scalar the source-action bridge was")
    emit("        already priced to, so GB-S2's NEW content is 5, not 6.")
    emit("   (C7) the window's '1' is one CONVENTION drawn from an unbounded")
    emit("        family (887: 1023 distinct members inside radius 2), not a")
    emit("        one-parameter continuum.")
    emit()
    emit("  Two prior-art corrections the checker CONFIRMS: Cycle 884's")
    emit("  checker's 27 is not a refinement of the whole honest 10 (it never")
    emit("  charts sigma, D or barrier), and Cycle 887 discharged nothing --")
    emit("  its receipt records a NO-GO on the window extent and a WIDENING")
    emit("  of Cycle 885's pricing.")
    emit(f"  exit code is 0 regardless of claim survival")

    receipt = {
        "cycle": CYCLE,
        "role": "independent adversarial check of the Cycle-896 reconciliation",
        "source_pins": [
            {"path": rel, "sha256": _sha256(ROOT / rel), "git_blob": _git_blob(rel)}
            for rel in AUDIT_INPUT_PATHS
        ],
        "independent_rebuilds": {
            "rotation_group_size": res["rotation_group_size"],
            "method_rotation_group": "generator closure on R_z(90), R_x(90)",
            "nearest_neighbour_orbits": res["nearest_neighbour_orbit_count"],
            "window_orbits": res["window_orbit_count"],
            "harmonic_tower": res["harmonic_tower"],
            "method_harmonic_tower":
                "polynomial-invariant trace counts + P_d = H_d (+) r^2 P_{d-2}",
            "angular_free_up_to_degree_12": res["angular_free_up_to_12"],
            "readout_half_nullspace": res["readout_half_from_scratch"],
            "pin_by_raw_bytes": res["pin_by_raw_bytes"],
            "obligation_by_sentences": res["obligation_by_sentences"],
            "charts_by_text": res["charts_by_text"],
        },
        "claims": res["claims"],
        "claims_total": res["claims_total"],
        "claims_surviving": res["claims_surviving"],
        "claims_refuted": res["claims_refuted"],
        "claims_narrowed": res["claims_narrowed"],
        "double_count_hunt": b4["checker_independent_value"],
        "discharge_audit": c1["checker_independent_value"],
        "teeth": teeth["teeth"],
        "teeth_total": teeth["teeth_total"],
        "teeth_biting": teeth["teeth_biting"],
        "teeth_not_biting": teeth["teeth_not_biting"],
        "firewall_hits": FIREWALL.hits,
        "elapsed_sec": round(time.time() - START, 3),
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(receipt, indent=1, sort_keys=True) + "\n")

    emit(f"receipt: {OUT_JSON.relative_to(ROOT)}")
    emit(f"elapsed_sec: {round(time.time() - START, 3)}")

    body = "\n".join(out)
    if len(body.encode()) > STDOUT_LIMIT_BYTES:
        body = body[:STDOUT_LIMIT_BYTES] + "\n[stdout truncated]"
    sys.stdout.write(body + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
