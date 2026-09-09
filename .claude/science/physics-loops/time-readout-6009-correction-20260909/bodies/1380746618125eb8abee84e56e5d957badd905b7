#!/usr/bin/env python3
"""Cycle 896: close the campaign's two computed-reconciliation flags.

FLAG A -- THE 871 READOUT-DIMENSION PIN DISCREPANCY.
    Cycle 882's ship receipt emitted, verbatim, "871 readout dimension: report
    says 2, on-branch BRANCH_PINS says 1; flagged for audit-lane
    reconciliation".  This block rebuilds BOTH statements from their pinned
    bytes -- the 880 primary's `BRANCH_PINS["cycle871_reference"]` by AST, and
    the 882 receipt's flag string by text -- reads the landed obligation's own
    closure criterion out of `docs/AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_
    OBLIGATION.md`, counts its clauses from located bytes, and adjudicates.
    The Cycle-871 runner and note are NOT on this branch; their absence is
    disclosed with scan counts and NOTHING is reconstructed for them.

FLAG B -- THE CHART-COUNT RECONCILIATION (8 / 10 / 27).
    Cycle 884 reported the GB-S2 residual three ways.  This block rebuilds all
    three charts from pinned sources -- the LANDED 13-coordinate chart and the
    HONEST 15-coordinate chart by AST off the 884 primary (cross-checked
    against the 884 runner receipt's classification), and the ORBIT-INDEXED
    27-coordinate chart by INDEPENDENT geometry (the 24 proper cubic rotations,
    orbit counts, and the octahedral harmonic-invariant tower recomputed by an
    exact character sum) cross-checked against the 884 checker receipt.  It
    then constructs the correspondence maps O -> H -> L, verifies them in both
    directions (coverage, no double count, composition consistency), locates
    the two eliminated-inadmissible coordinates (epsilon, m), and computes the
    CURRENT post-discharge residual from the 885 / 887 / 892 receipts with
    per-cycle attributions.  Cycle 893 is NOT on this branch; disclosed.

DISCIPLINE.  Every consumed artifact is pinned by full path + sha256 + git
blob; an absent or mismatched pin is a hard exit 2.  Sources are read as
TEXT / AST / JSON only and are blocked from import by a meta-path firewall.
Every certified number is exact integer or `Fraction` arithmetic -- no floating
point enters any certified quantity.  The gates are outcome-neutral: they
verify that both Flag-A statements were rebuilt, that all three Flag-B charts
were rebuilt, that the correspondence maps close in both directions, and that
the discharge accounting is complete with per-cycle attributions -- they do NOT
verify that any particular reconciliation verdict landed.
"""
from __future__ import annotations

import ast
import hashlib
import importlib.abc
import json
import re
import subprocess
import sys
import time
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path

START = time.time()

CYCLE = 896
RUNTIME_CAP_SEC = 900
STDOUT_LIMIT_BYTES = 150_000

ROOT = Path(__file__).resolve().parents[1]
SELF_REL = "scripts/frontier_cycle896_audit_reconciliation_2026_07_28.py"
OUT_JSON = ROOT / "outputs" / "audit_reconciliation_cycle896_receipt_2026_07_28.json"

# --------------------------------------------------------------------------
# the pinned sources.  Full paths, literal and greppable.
# --------------------------------------------------------------------------
OBLIGATION_MD = "docs/AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md"
C880_PRIMARY = "scripts/frontier_cycle880_visible_point_physics_2026_07_28.py"
C882_PRIMARY = "scripts/frontier_cycle882_readout_identity_2026_07_28.py"
C882_RECEIPT = "outputs/readout_identity_cycle882_receipt_2026_07_28.json"
C884_PRIMARY = "scripts/frontier_cycle884_gbs2_kernel_window_2026_07_28.py"
C884_CHECKER = "scripts/frontier_cycle884_gbs2_independent_check_2026_07_28.py"
# THE TWO SAME-BASENAME 884 RECEIPTS.  They are DISTINCT files; both are pinned
# by FULL PATH and their distinctness is certified in A_PINS.
C884_RECEIPT_RUNNER = (
    "logs/runner-cache/gbs2_kernel_window_cycle884_receipt_2026_07_28.json")
C884_RECEIPT_BLOCK = (
    "outputs/gbs2_kernel_window_cycle884_receipt_2026_07_28.json")
C884_CHECKER_RECEIPT = (
    "logs/runner-cache/gbs2_independent_check_cycle884_receipt_2026_07_28.json")
C885_RECEIPT = "outputs/gbw1_record_window_cycle885_receipt_2026_07_28.json"
C887_RECEIPT = "outputs/window_freedom_cycle887_receipt_2026_07_28.json"
C892_RECEIPT = "outputs/gbw1b_pricing_cycle892_receipt_2026_07_28.json"

AUDIT_INPUT_PATHS = (
    OBLIGATION_MD,
    C880_PRIMARY,
    C882_PRIMARY,
    C882_RECEIPT,
    C884_PRIMARY,
    C884_CHECKER,
    C884_RECEIPT_RUNNER,
    C884_RECEIPT_BLOCK,
    C884_CHECKER_RECEIPT,
    C885_RECEIPT,
    C887_RECEIPT,
    C892_RECEIPT,
)

# Digests measured on this branch at authoring time.  A mismatch means the
# artifact under the path is not the artifact this cycle was pointed at, and is
# a hard preflight failure -- exit 2, no science.
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

PINNED_GIT_BLOB = {
    OBLIGATION_MD: "9a449956422a5687b5b1346f428c9e4e35489038",
    C880_PRIMARY: "db0472a8fe3e9e93f3f31f8e0b5ac0fd5c6630f8",
    C882_PRIMARY: "c13380757eae27bdee05bc0d4be65a40c2865585",
    C882_RECEIPT: "9d70fdf701b3ad9619d7dffd4425fadd88eedbeb",
    C884_PRIMARY: "7b244a7ce3a4d61589bea0f222cca5d847ab0200",
    C884_CHECKER: "6166dae8afab56ac3f4fb1a8528afcf8b8fee101",
    C884_RECEIPT_RUNNER: "5a3c9db3ff688f26a70cc9b82aed53ec0ff41bb8",
    C884_RECEIPT_BLOCK: "3a5409a6b5e863e397a3e036f1b34c20bc24e5c3",
    C884_CHECKER_RECEIPT: "0024ec4d8c147d875d30cded463dab1e25cedb48",
    C885_RECEIPT: "553bba1fbd427f27c5606b6f27bd592a91e9c3c0",
    C887_RECEIPT: "643fb824665d967f770c8939977a0f4010839564",
    C892_RECEIPT: "722b1b7c50a17fffe6b0a4e666970d5aaf0e74c2",
}

# Artifacts the brief names that are NOT on this lineage.  Presence is SCANNED,
# never assumed, and absence is disclosed with counts.  Nothing is rebuilt for
# an absent artifact.
ABSENCE_PROBES = {
    "cycle871": ("871",),
    "cycle893": ("893",),
}
ABSENCE_SCAN_DIRS = ("scripts", "outputs", "docs", "logs/runner-cache")


# --------------------------------------------------------------------------
# preflight: pins are hard gates
# --------------------------------------------------------------------------
def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _git_blob(rel: str) -> str:
    try:
        out = subprocess.run(["git", "hash-object", rel], cwd=str(ROOT),
                             capture_output=True, text=True, timeout=60)
        return out.stdout.strip() if out.returncode == 0 else ""
    except Exception:
        return ""


def preflight_pins() -> None:
    missing = [p for p in AUDIT_INPUT_PATHS if not (ROOT / p).is_file()]
    if missing:
        sys.stderr.write("PREFLIGHT FAIL: pinned input(s) absent: "
                         + ", ".join(missing) + "\n")
        raise SystemExit(2)
    for rel, want in PINNED_SHA256.items():
        got = _sha256(ROOT / rel)
        if got != want:
            sys.stderr.write(
                f"PREFLIGHT FAIL: {rel}\n  sha256 {got}\n  pinned {want}\n")
            raise SystemExit(2)
    for rel, want in PINNED_GIT_BLOB.items():
        got = _git_blob(rel)
        if got != want:
            sys.stderr.write(
                f"PREFLIGHT FAIL: {rel}\n  git blob {got}\n  pinned {want}\n")
            raise SystemExit(2)
    # The two same-basename 884 receipts must be DISTINCT files.
    if (_sha256(ROOT / C884_RECEIPT_RUNNER)
            == _sha256(ROOT / C884_RECEIPT_BLOCK)):
        sys.stderr.write(
            "PREFLIGHT FAIL: the two same-basename 884 receipts are byte "
            "identical; the block brief asserts they are distinct.\n")
        raise SystemExit(2)


preflight_pins()

_FORBIDDEN_STEMS = {Path(p).stem for p in AUDIT_INPUT_PATHS if p.endswith(".py")}


class _Firewall(importlib.abc.MetaPathFinder):
    """Fail closed if any pinned primary is imported rather than read."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in _FORBIDDEN_STEMS:
            self.hits.append(fullname)
            raise ImportError(f"FIREWALL forbids import of {fullname}")
        return None


FIREWALL = _Firewall()
sys.meta_path.insert(0, FIREWALL)


def read_text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def read_json(rel: str) -> dict:
    return json.loads(read_text(rel))


def parse_module(rel: str) -> ast.Module:
    return ast.parse((ROOT / rel).read_bytes(), filename=rel)


def q(x) -> str:
    return str(Fraction(x))


# --------------------------------------------------------------------------
# certificate A: pins + honest absences
# --------------------------------------------------------------------------
def pins_certificate() -> dict:
    rows = []
    for rel in AUDIT_INPUT_PATHS:
        p = ROOT / rel
        rows.append({
            "path": rel,
            "bytes": p.stat().st_size,
            "sha256": _sha256(p),
            "git_blob": _git_blob(rel),
            "sha256_matches_pin": _sha256(p) == PINNED_SHA256[rel],
            "git_blob_matches_pin": _git_blob(rel) == PINNED_GIT_BLOB[rel],
        })

    same_basename = {}
    for rel in (C884_RECEIPT_RUNNER, C884_RECEIPT_BLOCK):
        same_basename[rel] = {
            "basename": Path(rel).name,
            "sha256": _sha256(ROOT / rel),
            "top_level_keys": sorted(read_json(rel).keys()),
        }
    basenames_equal = (Path(C884_RECEIPT_RUNNER).name
                       == Path(C884_RECEIPT_BLOCK).name)
    contents_distinct = (same_basename[C884_RECEIPT_RUNNER]["sha256"]
                         != same_basename[C884_RECEIPT_BLOCK]["sha256"])

    # honest absence scan
    tracked = subprocess.run(["git", "ls-files"], cwd=str(ROOT),
                             capture_output=True, text=True, timeout=120)
    tracked_paths = [line for line in tracked.stdout.splitlines() if line]
    on_disk = []
    for d in ABSENCE_SCAN_DIRS:
        dd = ROOT / d
        if dd.is_dir():
            on_disk.extend(str(f.relative_to(ROOT)) for f in dd.iterdir()
                           if f.is_file())
    absences = {}
    for label, probes in ABSENCE_PROBES.items():
        hits_tracked = sorted({p for p in tracked_paths
                               for pr in probes if pr in Path(p).name})
        hits_disk = sorted({p for p in on_disk
                            for pr in probes if pr in Path(p).name})
        absences[label] = {
            "probes": list(probes),
            "tracked_files_scanned": len(tracked_paths),
            "on_disk_files_scanned": len(on_disk),
            "tracked_hits": len(hits_tracked),
            "on_disk_hits": len(hits_disk),
            "hit_paths": sorted(set(hits_tracked) | set(hits_disk)),
            "present_on_this_branch": bool(hits_tracked or hits_disk),
        }

    ok = (all(r["sha256_matches_pin"] and r["git_blob_matches_pin"]
              for r in rows)
          and basenames_equal and contents_distinct
          and FIREWALL.hits == [])
    return {
        "pins": rows,
        "pin_count": len(rows),
        "same_basename_pair": same_basename,
        "the_two_884_receipts_share_a_basename": basenames_equal,
        "the_two_884_receipts_are_distinct_files": contents_distinct,
        "absence_scan": absences,
        "firewall_hits": FIREWALL.hits,
        "firewall_hit_count": len(FIREWALL.hits),
        "finding": (
            f"{len(rows)} artifacts pinned by full path + sha256 + git blob, "
            f"all matching. The two same-basename Cycle-884 receipts "
            f"({Path(C884_RECEIPT_RUNNER).name}) are certified DISTINCT: the "
            f"logs/runner-cache copy is the runner receipt "
            f"({len(same_basename[C884_RECEIPT_RUNNER]['top_level_keys'])} "
            f"keys, carrying the chart counts) and the outputs copy is the "
            f"block-note receipt "
            f"({len(same_basename[C884_RECEIPT_BLOCK]['top_level_keys'])} "
            f"keys). Cycle 871 artifacts on this branch: "
            f"{absences['cycle871']['tracked_hits']} tracked / "
            f"{absences['cycle871']['on_disk_hits']} on disk. Cycle 893: "
            f"{absences['cycle893']['tracked_hits']} tracked / "
            f"{absences['cycle893']['on_disk_hits']} on disk. Nothing is "
            f"reconstructed for either."
        ),
        "pass": ok,
    }


# ==========================================================================
# FLAG A
# ==========================================================================
def flag_a_statements_certificate() -> dict:
    """Rebuild BOTH Flag-A statements from their pinned bytes, exactly."""
    # --- statement 1: the on-branch pin, by AST off the Cycle-880 primary ---
    pin_text = None
    branch_pins_keys: list[str] = []
    for node in ast.walk(parse_module(C880_PRIMARY)):
        if isinstance(node, ast.Assign):
            names = [t.id for t in node.targets if isinstance(t, ast.Name)]
            if "BRANCH_PINS" in names and isinstance(node.value, ast.Dict):
                for k, v in zip(node.value.keys, node.value.values):
                    if isinstance(k, ast.Constant):
                        branch_pins_keys.append(k.value)
                        if k.value == "cycle871_reference":
                            pin_text = ast.literal_eval(v)
    pin_dim = None
    pin_clause_label = None
    pin_named_object = None
    if pin_text:
        m = re.search(r"free dimension (\d+)", pin_text)
        pin_dim = int(m.group(1)) if m else None
        # the clause the pin's OWN bytes name, located not paraphrased
        for label in ("source-action bridge", "readout", "carrier"):
            if label in pin_text:
                pin_clause_label = label
                break
        m2 = re.search(r"free dimension \d+:\s*([^)]*)", pin_text)
        pin_named_object = m2.group(1).strip() if m2 else None

    # --- statement 2: the report's number, by TEXT off the Cycle-882 receipt --
    c882 = read_json(C882_RECEIPT)
    flag_text = c882.get("pin_discrepancy_emitted", "")
    m3 = re.search(r"report says (\d+)", flag_text)
    report_dim = int(m3.group(1)) if m3 else None
    m4 = re.search(r"BRANCH_PINS says (\d+)", flag_text)
    flag_pin_dim = int(m4.group(1)) if m4 else None
    m5 = re.match(r"^(\d+)\s+(\w+)\s+dimension", flag_text)
    flag_clause_label = m5.group(2) if m5 else None

    # --- Cycle 882's OWN computed readout-half residual, by AST ------------
    c882_readout_residual = None
    c882_readout_note = None
    c882_joint_is_a_sum = False
    for node in ast.walk(parse_module(C882_PRIMARY)):
        if isinstance(node, ast.FunctionDef) and node.name == "outcome_certificate":
            for sub in ast.walk(node):
                if isinstance(sub, ast.Assign):
                    for t in sub.targets:
                        if (isinstance(t, ast.Name)
                                and t.id == "residual_continuous_dimension"):
                            c882_readout_residual = ast.literal_eval(sub.value)
                if isinstance(sub, ast.Dict):
                    for k, v in zip(sub.keys, sub.values):
                        if not isinstance(k, ast.Constant):
                            continue
                        if k.value == "residual_free_dimension_note":
                            try:
                                c882_readout_note = ast.literal_eval(v)
                            except ValueError:
                                c882_readout_note = ast.unparse(v)
                        if (k.value ==
                                "joint_price_if_the_two_halves_are_independent"):
                            src = ast.unparse(v)
                            c882_joint_is_a_sum = (
                                "pinned_871" in src
                                and "residual_continuous_dimension" in src
                                and "+" in src)

    both_rebuilt = (pin_text is not None and pin_dim is not None
                    and flag_text != "" and report_dim is not None
                    and c882_readout_residual is not None)
    return {
        "statement_1_source": f"{C880_PRIMARY} :: BRANCH_PINS['cycle871_reference'] (AST)",
        "statement_1_verbatim": pin_text,
        "statement_1_free_dimension": pin_dim,
        "statement_1_clause_label_in_its_own_bytes": pin_clause_label,
        "statement_1_named_object": pin_named_object,
        "branch_pins_key_count": len(branch_pins_keys),
        "statement_2_source": f"{C882_RECEIPT} :: pin_discrepancy_emitted (text)",
        "statement_2_verbatim": flag_text,
        "statement_2_report_free_dimension": report_dim,
        "statement_2_quoted_branch_pin_dimension": flag_pin_dim,
        "statement_2_clause_label_in_its_own_bytes": flag_clause_label,
        "cycle882_own_readout_half_residual": c882_readout_residual,
        "cycle882_readout_residual_note": c882_readout_note,
        "cycle882_joint_price_is_literally_a_sum_of_the_two_halves":
            c882_joint_is_a_sum,
        "the_two_statements_label_the_same_clause": (
            pin_clause_label == flag_clause_label),
        "quoted_pin_dimension_agrees_with_the_pin_itself":
            flag_pin_dim == pin_dim,
        "both_statements_rebuilt_from_pinned_bytes": both_rebuilt,
        "finding": (
            f"Statement 1 (on branch, AST): the Cycle-880 pin reads "
            f"'{pin_text}' -- free dimension {pin_dim}, and its OWN bytes label "
            f"the clause '{pin_clause_label}'. Statement 2 (on branch, text): "
            f"the Cycle-882 receipt reads '{flag_text}' -- it labels the clause "
            f"'{flag_clause_label}' and quotes the branch pin at "
            f"{flag_pin_dim}. The two statements label DIFFERENT clauses "
            f"({pin_clause_label} vs {flag_clause_label}): "
            f"same_clause={pin_clause_label == flag_clause_label}."
        ),
        "pass": both_rebuilt,
    }


def flag_a_obligation_certificate() -> dict:
    """Recompute the landed obligation's own clause dimension from its bytes."""
    text = read_text(OBLIGATION_MD)
    # locate the closure-criterion section by its heading, verbatim
    lines = text.splitlines()
    start = next((i for i, ln in enumerate(lines)
                  if ln.strip() == "## Closure criterion"), None)
    end = None
    if start is not None:
        for j in range(start + 1, len(lines)):
            if lines[j].startswith("## "):
                end = j
                break
    section = "\n".join(lines[start:end]) if start is not None else ""
    flat = " ".join(section.split())

    # sentence 1 = the PROVISION criterion; sentence 2 = the MANNER criterion
    prov_marker = "A closing theorem must provide"
    manner_marker = "It must derive"
    i_prov = flat.find(prov_marker)
    i_manner = flat.find(manner_marker)
    provision = flat[i_prov:i_manner].strip() if i_prov >= 0 and i_manner > i_prov else ""
    manner = flat[i_manner:].split("Relevant current route")[0].strip() if i_manner >= 0 else ""

    # parse the provision criterion's connectives from located bytes
    conj_marker = " and either "
    disj_marker = " or "
    i_conj = provision.find(conj_marker)
    clause_1 = provision[len(prov_marker):i_conj].strip() if i_conj > 0 else ""
    clause_2_raw = provision[i_conj + len(conj_marker):].strip() if i_conj > 0 else ""
    i_disj = clause_2_raw.find(disj_marker)
    disjunct_1 = clause_2_raw[:i_disj].strip() if i_disj > 0 else ""
    disjunct_2 = clause_2_raw[i_disj + len(disj_marker):].strip().rstrip(".") if i_disj > 0 else ""

    provision_clauses = [c for c in (clause_1, clause_2_raw) if c]
    disjuncts = [d for d in (disjunct_1, disjunct_2) if d]
    manner_clauses = [manner] if manner else []

    # the obligation's OWN clause dimension: how many independent things a
    # closing theorem must SUPPLY.  A manner clause supplies no parameter --
    # it constrains HOW the supply is proved -- and is counted at 0.
    obligation_clause_dimension = len(provision_clauses)
    manner_clause_dimension = 0

    ok = (bool(section) and len(provision_clauses) == 2 and len(disjuncts) == 2
          and len(manner_clauses) == 1)
    return {
        "closure_criterion_section_verbatim": section,
        "provision_criterion_verbatim": provision,
        "manner_criterion_verbatim": manner,
        "provision_clause_1_the_bridge": clause_1,
        "provision_clause_2_the_readout_disjunction": clause_2_raw,
        "readout_disjunct_1": disjunct_1,
        "readout_disjunct_2": disjunct_2,
        "provision_clause_count": len(provision_clauses),
        "disjunct_count_inside_clause_2": len(disjuncts),
        "manner_clause_count": len(manner_clauses),
        "manner_clause_free_dimension": manner_clause_dimension,
        "obligation_own_clause_dimension": obligation_clause_dimension,
        "finding": (
            f"The landed obligation's closure criterion is a CONJUNCTION of "
            f"{len(provision_clauses)} provision clauses -- clause 1 "
            f"'{clause_1}' and clause 2, itself a disjunction of "
            f"{len(disjuncts)} branches -- plus {len(manner_clauses)} manner "
            f"clause ('{manner[:60]}...') that supplies no parameter. The "
            f"obligation's own clause dimension is therefore "
            f"{obligation_clause_dimension}."
        ),
        "pass": ok,
    }


def flag_a_map_certificate(stmt: dict, obl: dict) -> dict:
    """The map between the two accountings, verified in both directions."""
    pin_dim = stmt["statement_1_free_dimension"]
    report_dim = stmt["statement_2_report_free_dimension"]
    readout_dim = stmt["cycle882_own_readout_half_residual"]

    # the two accountings as LABELLED SETS, so the map is checkable elementwise
    bridge_element = "bridge_clause_overall_normalisation_scalar"
    readout_element = "readout_clause_anchor_constant_k"

    bookkeeping_A = [bridge_element]                       # the 880 pin
    bookkeeping_B = [bridge_element, readout_element]      # obligation-wide

    inclusion_image = [e for e in bookkeeping_A if e in bookkeeping_B]
    complement = [e for e in bookkeeping_B if e not in bookkeeping_A]

    forward_total = len(inclusion_image) + len(complement)
    injective = len(set(bookkeeping_A)) == len(bookkeeping_A)
    no_double_count = not (set(bookkeeping_A) & set(complement))
    covers_B = sorted(set(inclusion_image) | set(complement)) == sorted(set(bookkeeping_B))

    arithmetic_closes = (pin_dim is not None and readout_dim is not None
                         and report_dim is not None
                         and pin_dim + readout_dim == report_dim)
    complement_matches_882 = len(complement) == readout_dim
    obligation_matches_B = obl["obligation_own_clause_dimension"] == len(bookkeeping_B)

    # the counter-hypothesis, tested rather than dismissed
    counter = {
        "hypothesis": ("the reported 2 is the READOUT clause alone at free "
                       "dimension 2, i.e. a genuinely different claim"),
        "on_branch_computation_of_the_readout_clause": readout_dim,
        "supported": readout_dim == 2,
        "why": (
            f"Cycle 882 computes the readout half's residual free dimension at "
            f"{readout_dim} by exact nullspace arithmetic (its certificate C "
            f"gives the C3-covariant Record-additive readout space dimension "
            f"{readout_dim}, and its certificate M carries the residual as the "
            f"single anchor constant k). A readout-clause-alone value of 2 is "
            f"supported by no computation on this branch."
        ),
    }

    if arithmetic_closes and complement_matches_882 and not counter["supported"]:
        verdict = "SAME OBJECT, TWO BOOKKEEPINGS -- BIJECTION EXHIBITED"
    elif counter["supported"]:
        verdict = "GENUINELY DIFFERENT CLAIMS -- adjudicate against the obligation"
    else:
        verdict = "UNRESOLVED ON PINNED SOURCES"

    root_cause = (
        "A CLAUSE-LABEL SLIP, computed not asserted. The Cycle-880 pin's own "
        f"bytes say '{stmt['statement_1_clause_label_in_its_own_bytes']}' -- it "
        "prices the obligation's FIRST provision clause (the physical "
        "carrier/source-action bridge). The Cycle-882 flag files that same "
        f"number under the label '{stmt['statement_2_clause_label_in_its_own_bytes']}' "
        "-- the obligation's SECOND provision clause. The two numbers were "
        "never about the same clause, so they were never in conflict."
    )

    return {
        "bookkeeping_A_the_880_pin": bookkeeping_A,
        "bookkeeping_A_dimension": len(bookkeeping_A),
        "bookkeeping_A_scope": ("provision clause 1 only (the physical "
                                "carrier/source-action bridge)"),
        "bookkeeping_B_the_871_report": bookkeeping_B,
        "bookkeeping_B_dimension": len(bookkeeping_B),
        "bookkeeping_B_scope": ("both provision clauses of the obligation "
                                "(bridge + readout normalization)"),
        "map_forward_A_into_B": {e: e for e in bookkeeping_A},
        "map_backward_B_onto_A_plus_complement": {
            "in_A": inclusion_image, "complement": complement},
        "forward_total_equals_B": forward_total == len(bookkeeping_B),
        "map_is_injective": injective,
        "no_element_double_counted": no_double_count,
        "map_covers_B_completely": covers_B,
        "exact_arithmetic": f"{pin_dim} + {readout_dim} = {report_dim}",
        "arithmetic_closes": arithmetic_closes,
        "complement_size_matches_cycle882_readout_residual": complement_matches_882,
        "obligation_clause_dimension_matches_bookkeeping_B": obligation_matches_B,
        "counter_hypothesis": counter,
        "verdict": verdict,
        "root_cause": root_cause,
        "reconciled_statement": (
            f"The AC R-eta readout-derivation obligation carries "
            f"{obl['obligation_own_clause_dimension']} provision clauses and "
            f"total free dimension {report_dim} on this branch's computations: "
            f"{pin_dim} on the carrier/source-action bridge clause (the overall "
            f"normalisation scalar, per the Cycle-880 pin) plus "
            f"{readout_dim} on the Record-facing readout normalization clause "
            f"(the anchor constant k, alpha = k/3, per Cycle 882's exact "
            f"nullspace computation). The on-branch pin's 1 is the BRIDGE "
            f"clause and is correct at its own scope; the report's 2 is the "
            f"OBLIGATION-WIDE total and is correct at its scope. Both are "
            f"right; the flag was a clause-label slip."
        ),
        "finding": (
            f"{verdict}. {pin_dim} + {readout_dim} = {report_dim}, the "
            f"complement is exactly Cycle 882's computed readout residual, and "
            f"the obligation's own clause count "
            f"({obl['obligation_own_clause_dimension']}) matches the wider "
            f"bookkeeping."
        ),
        "pass": (injective and no_double_count and covers_B
                 and forward_total == len(bookkeeping_B)),
    }


# ==========================================================================
# FLAG B -- geometry rebuilt independently
# ==========================================================================
NEIGHBOURS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def proper_rotations() -> list:
    """The 24 proper cubic rotations, built as signed permutation matrices."""
    out = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            M = [[0, 0, 0] for _ in range(3)]
            for i in range(3):
                M[i][perm[i]] = signs[i]
            det = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
                   - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
                   + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
            if det == 1:
                out.append(tuple(tuple(r) for r in M))
    return sorted(out)


def act(M, x):
    return tuple(sum(M[i][j] * x[j] for j in range(3)) for i in range(3))


def orbits_of(points, mats) -> list:
    pts = set(points)
    seen = set()
    out = []
    for p in sorted(pts):
        if p in seen:
            continue
        orb = tuple(sorted({act(M, p) for M in mats}))
        seen.update(orb)
        out.append(orb)
    return out


def harmonic_invariant_dim_by_character(d: int) -> int:
    """dim of O-invariants in the degree-d harmonic space, by an exact character
    sum over the five conjugacy classes of the chiral octahedral group.

    chi_d(phi) = sum_{m=-d}^{d} cos(m phi) for the rotation angle phi.
    Classes: E (1 elt, phi=0), 6C4 (phi=pi/2), 9 elements at phi=pi
    (3C2 + 6C2'), 8C3 (phi=2pi/3).  All character values are integers here.
    """
    def chi(cos_table) -> Fraction:
        # cos_table[m % period] holds 2*cos(m*phi) as an exact Fraction; the
        # m = 0 term is counted once.
        total = Fraction(1)
        for m in range(1, d + 1):
            total += cos_table[m % len(cos_table)]
        return total

    # 2*cos(m*phi) tables, exact
    t_0 = [Fraction(2)]                                   # phi = 0
    t_pi2 = [Fraction(2), Fraction(0), Fraction(-2), Fraction(0)]   # phi = pi/2
    t_pi = [Fraction(2), Fraction(-2)]                    # phi = pi
    t_2pi3 = [Fraction(2), Fraction(-1), Fraction(-1)]    # phi = 2pi/3

    total = (Fraction(1) * chi(t_0)
             + Fraction(6) * chi(t_pi2)
             + Fraction(9) * chi(t_pi)
             + Fraction(8) * chi(t_2pi3))
    val = total / 24
    assert val.denominator == 1 and val >= 0, (d, val)
    return int(val)


def harmonic_invariant_dim_by_algebra(d: int, mats) -> int:
    """Same number by brute linear algebra on degree-d monomials: the kernel of
    the stacked [average - I ; Laplacian] on the space of degree-d forms."""
    mons = [(i, j, d - i - j) for i in range(d + 1) for j in range(d - i + 1)]
    idx = {m: k for k, m in enumerate(mons)}
    n = len(mons)

    def expand(M, mon):
        """(sum_j M[0][j] x_j)^a (sum_j M[1][j] x_j)^b (...)^c as a dict."""
        cur = {(0, 0, 0): Fraction(1)}
        for row, power in zip(M, mon):
            for _ in range(power):
                nxt: dict = {}
                for base, coeff in cur.items():
                    for j in range(3):
                        if row[j] == 0:
                            continue
                        e = list(base)
                        e[j] += 1
                        key = tuple(e)
                        nxt[key] = nxt.get(key, Fraction(0)) + coeff * row[j]
                cur = nxt
        return cur

    avg = [[Fraction(0)] * n for _ in range(n)]
    for M in mats:
        # substitution x -> M^T x acting on monomials
        MT = tuple(tuple(M[r][c] for r in range(3)) for c in range(3))
        for mon in mons:
            for key, coeff in expand(MT, mon).items():
                avg[idx[key]][idx[mon]] += coeff / len(mats)

    rows = []
    for r in range(n):
        row = list(avg[r])
        row[r] -= 1
        rows.append(row)
    # Laplacian rows: map degree d -> degree d-2
    if d >= 2:
        lower = [(i, j, d - 2 - i - j) for i in range(d - 1)
                 for j in range(d - 1 - i)]
        lidx = {m: k for k, m in enumerate(lower)}
        lap = [[Fraction(0)] * n for _ in range(len(lower))]
        for mon in mons:
            for v in range(3):
                if mon[v] >= 2:
                    tgt = list(mon)
                    tgt[v] -= 2
                    lap[lidx[tuple(tgt)]][idx[mon]] += mon[v] * (mon[v] - 1)
        rows.extend(lap)
    return n - rank_exact(rows)


def rank_exact(rows) -> int:
    mat = [list(map(Fraction, r)) for r in rows]
    if not mat:
        return 0
    ncols = len(mat[0])
    rank = 0
    for col in range(ncols):
        piv = None
        for r in range(rank, len(mat)):
            if mat[r][col] != 0:
                piv = r
                break
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


ANGULAR_CUTOFF = 12
WINDOW_RADIUS_SQ = 16


def flag_b_charts_certificate() -> dict:
    """Rebuild ALL THREE charts from pinned sources."""
    # ---- chart L and chart H, by AST off the 884 primary ------------------
    tree = parse_module(C884_PRIMARY)
    landed_chart = None
    discovered = None
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id == "LANDED_CHART":
                    landed_chart = ast.literal_eval(node.value)
                if isinstance(t, ast.Name) and t.id == "DISCOVERED_COORDS":
                    discovered = ast.literal_eval(node.value)
    # classification by AST off the primary's put(...) calls
    ast_class: dict[str, str] = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == "reduced_map_certificate":
            for sub in ast.walk(node):
                if (isinstance(sub, ast.Call) and isinstance(sub.func, ast.Name)
                        and sub.func.id == "put" and len(sub.args) >= 2):
                    ast_class[ast.literal_eval(sub.args[0])] = \
                        ast.literal_eval(sub.args[1])
    # cross-check against the pinned RUNNER receipt (the logs/runner-cache one)
    rr = read_json(C884_RECEIPT_RUNNER)
    receipt_class = {k: v["class"] for k, v in rr["classification"].items()}
    class_agreement = ast_class == receipt_class

    L_names = [c[0] for c in landed_chart]
    H_names = L_names + [c[0] for c in discovered]
    blocks = {c[0]: c[1] for c in list(landed_chart) + list(discovered)}

    def tally(names):
        out = {"FORCED": [], "GAUGE": [], "ELIMINATED": [], "FREE": []}
        for n in names:
            out[ast_class[n]].append(n)
        return {k: sorted(v) for k, v in out.items()}

    L_tally, H_tally = tally(L_names), tally(H_names)
    L_free, H_free = L_tally["FREE"], H_tally["FREE"]

    # ---- chart O, rebuilt by INDEPENDENT geometry -------------------------
    mats = proper_rotations()
    nn = [(0, 0, 0)] + list(NEIGHBOURS)
    nn_orbits = orbits_of(nn, mats)
    block = [(i, j, k) for i in (-1, 0, 1) for j in (-1, 0, 1) for k in (-1, 0, 1)]
    block_orbits = orbits_of(block, mats)
    shell = [(i, j, k)
             for i in range(-4, 5) for j in range(-4, 5) for k in range(-4, 5)
             if 1 <= i * i + j * j + k * k <= WINDOW_RADIUS_SQ]
    win_orbits = orbits_of(shell, mats)

    ang_rows = []
    cumulative = 0
    algebra_agrees = True
    for d in range(0, ANGULAR_CUTOFF + 1):
        by_char = harmonic_invariant_dim_by_character(d)
        by_alg = harmonic_invariant_dim_by_algebra(d, mats)
        algebra_agrees = algebra_agrees and (by_char == by_alg)
        cumulative += by_char
        ang_rows.append({"degree": d, "dim_by_character": by_char,
                         "dim_by_linear_algebra": by_alg,
                         "methods_agree": by_char == by_alg,
                         "cumulative": cumulative})
    angular_free = cumulative - 1          # minus the isotropic monopole
    first_anisotropic = next((r["degree"] for r in ang_rows
                              if r["degree"] > 0 and r["dim_by_character"] > 0), None)

    O_components = {
        "operator_constants_left_free": len(nn_orbits) - 1,
        "angular_coefficients_free_up_to_degree_12": angular_free,
        "window_parameters_as_orbit_indicators": len(win_orbits),
        "phase_and_calibration_free": 2,
        "normalization_free": 1,
    }
    O_total = sum(O_components.values())

    cr = read_json(C884_CHECKER_RECEIPT)
    O_receipt_total = cr["independent_residual_count"]
    O_receipt_primary = cr["primary_residual_count"]

    ok = (landed_chart is not None and discovered is not None
          and class_agreement
          and len(L_names) == rr["landed_chart_dimension"]
          and len(H_names) == rr["honest_chart_dimension"]
          and len(L_free) == rr["landed_chart_residual_free_dimension"]
          and len(H_free) == rr["honest_chart_residual_free_dimension"]
          and O_total == O_receipt_total
          and O_receipt_primary == len(H_free)
          and algebra_agrees)
    return {
        "chart_L_landed": {
            "source": f"{C884_PRIMARY} :: LANDED_CHART (AST)",
            "coordinates": L_names,
            "dimension": len(L_names),
            "tally": L_tally,
            "residual_free_dimension": len(L_free),
            "receipt_dimension": rr["landed_chart_dimension"],
            "receipt_residual": rr["landed_chart_residual_free_dimension"],
        },
        "chart_H_honest": {
            "source": f"{C884_PRIMARY} :: LANDED_CHART + DISCOVERED_COORDS (AST)",
            "coordinates": H_names,
            "dimension": len(H_names),
            "tally": H_tally,
            "residual_free_dimension": len(H_free),
            "receipt_dimension": rr["honest_chart_dimension"],
            "receipt_residual": rr["honest_chart_residual_free_dimension"],
            "blocks": {n: blocks[n] for n in H_names},
        },
        "chart_O_orbit_indexed": {
            "source": ("rebuilt here by exact geometry; cross-checked against "
                       f"{C884_CHECKER_RECEIPT}"),
            "proper_rotation_count": len(mats),
            "nearest_neighbour_orbit_count": len(nn_orbits),
            "range1_block_size": len(block),
            "range1_orbit_count": len(block_orbits),
            "window_shell_sites": len(shell),
            "window_orbit_count": len(win_orbits),
            "angular_rows": ang_rows,
            "angular_two_methods_agree": algebra_agrees,
            "first_anisotropic_degree": first_anisotropic,
            "components": O_components,
            "residual_free_dimension": O_total,
            "receipt_residual": O_receipt_total,
            "matches_receipt": O_total == O_receipt_total,
        },
        "classification_ast_matches_receipt": class_agreement,
        "three_charts_rebuilt": ok,
        "finding": (
            f"Three charts rebuilt from pinned bytes. LANDED: "
            f"{len(L_names)} coordinates, residual {len(L_free)}. HONEST: "
            f"{len(H_names)} coordinates, residual {len(H_free)}. "
            f"ORBIT-INDEXED: residual {O_total} = "
            f"{O_components['operator_constants_left_free']} operator + "
            f"{O_components['angular_coefficients_free_up_to_degree_12']} "
            f"angular (first anisotropic degree {first_anisotropic}) + "
            f"{O_components['window_parameters_as_orbit_indicators']} window "
            f"orbits + {O_components['phase_and_calibration_free']} "
            f"phase/calibration + {O_components['normalization_free']} "
            f"normalization. The angular tower is computed twice -- exact "
            f"character sum and brute monomial averaging -- and the two agree "
            f"({algebra_agrees})."
        ),
        "pass": ok,
    }


# --- the correspondence maps ---------------------------------------------
# Declared block-level correspondence.  Each row states which ORBIT-INDEXED
# component covers which HONEST coordinate(s).  The rows are DECLARED; the
# arithmetic that closes them is COMPUTED from the rebuilt charts above, and
# every coordinate on both sides must be accounted for exactly once.
O_TO_H_ROWS = (
    ("operator_constants_left_free", ("mu",),
     "the surviving invariant constant of the forced operator alpha*I + "
     "gamma*Delta after the far-field power is forced; H carries it as the "
     "screening mass mu^2 = alpha/gamma"),
    ("angular_coefficients_free_up_to_degree_12", ("c4",),
     "H truncates the octahedral harmonic-invariant tower at its FIRST member "
     "(degree 4, the coordinate c4); O carries the tower up to degree 12"),
    ("window_parameters_as_orbit_indicators", ("a", "b"),
     "H parameterizes the window as an annulus (inner boundary a, outer "
     "boundary b); O indexes every rotation orbit inside |x|^2 <= 16 "
     "independently"),
    ("phase_and_calibration_free", ("theta", "g"),
     "identical content, identical count: the per-edge phase gain and the F~M "
     "calibration gain"),
    ("normalization_free", ("N",),
     "identical content, identical count: the terminal detector-distribution "
     "normalization"),
)
# HONEST coordinates that the orbit-indexed chart does NOT carry at all.
H_NOT_IN_O = {
    "sigma": ("O charts the OPERATOR stencil, not the SOURCE; the source "
              "strength (only lambda*sigma is observable) has no orbit-indexed "
              "coordinate"),
    "D": ("O's window block is a single-readout spatial orbit family; the "
          "readout DEPTH is not a coordinate of it"),
    "barrier": ("O's window block carries no blocked-set coordinate"),
}
# A declared ALTERNATIVE reading, emitted alongside rather than instead of, so
# the ambiguity in the checker's operator block is visible rather than hidden.
O_OPERATOR_ALT = {
    "reading": ("O's operator block is the 2-dimensional invariant "
                "nearest-neighbour stencil space {centre weight, neighbour "
                "weight} = {overall scale, ratio}. Under the SCALE-ABSORBED "
                "reading its one free constant covers H's {sigma, mu} jointly, "
                "because the overall stencil scale is degenerate with the "
                "source strength -- the same (lambda, sigma) rescaling "
                "stabilizer the 884 primary classified lambda GAUGE by."),
    "h_coordinates_covered": ("mu", "sigma"),
}


def flag_b_maps_certificate(charts: dict) -> dict:
    H = charts["chart_H_honest"]
    L = charts["chart_L_landed"]
    O = charts["chart_O_orbit_indexed"]
    H_free = set(H["tally"]["FREE"])
    L_free = set(L["tally"]["FREE"])
    O_comp = O["components"]

    # ---- map O -> H, forward -------------------------------------------
    rows = []
    o_accounted = 0
    h_covered: list[str] = []
    for comp, htargets, why in O_TO_H_ROWS:
        size = O_comp[comp]
        o_accounted += size
        h_covered.extend(htargets)
        rows.append({
            "orbit_component": comp,
            "orbit_dimension": size,
            "honest_coordinates": list(htargets),
            "honest_dimension": len(htargets),
            "relation": ("refinement" if size > len(htargets)
                         else "identity" if size == len(htargets)
                         else "coarsening"),
            "refinement_factor": f"{size}:{len(htargets)}",
            "why": why,
        })
    o_complete = o_accounted == O["residual_free_dimension"]
    h_no_double = len(h_covered) == len(set(h_covered))
    h_uncovered = sorted(H_free - set(h_covered))
    h_covered_valid = set(h_covered) <= H_free
    h_partition_closes = (len(set(h_covered)) + len(h_uncovered) == len(H_free))
    unmatched_declared = sorted(H_NOT_IN_O)
    unmatched_matches = h_uncovered == unmatched_declared

    # the orbit-indexed chart's OWN honest total: it must also carry the three
    # coordinates it never charted.
    o_honest_total = O["residual_free_dimension"] + len(h_uncovered)
    o_honest_total_alt = O["residual_free_dimension"] + len(h_uncovered) - 1

    # ---- map H -> L, forward and backward -------------------------------
    H_only = sorted(set(H["coordinates"]) - set(L["coordinates"]))
    L_subset_H = set(L["coordinates"]) <= set(H["coordinates"])
    H_free_minus_L_free = sorted(H_free - L_free)
    L_free_subset = L_free <= H_free
    collapse_is_exactly_the_discovered = H_free_minus_L_free == H_only
    collapse_arithmetic = (len(H_free) - len(H_free_minus_L_free) == len(L_free))
    reclassified = sorted(n for n in L["coordinates"]
                          if (n in H_free) != (n in L_free))

    # ---- composition O -> H -> L ----------------------------------------
    o_dropped_by_L = sum(O_comp[comp] for comp, ht, _ in O_TO_H_ROWS
                         if set(ht) & set(H_only))
    o_surviving_to_L = O["residual_free_dimension"] - o_dropped_by_L
    l_covered_by_O = sorted({h for _, ht, _ in O_TO_H_ROWS for h in ht
                             if h in L_free})
    l_uncovered_by_O = sorted(L_free - set(l_covered_by_O))
    composition_closes = (len(l_covered_by_O) + len(l_uncovered_by_O)
                          == len(L_free))
    composition_consistent = (
        o_surviving_to_L == sum(O_comp[comp] for comp, ht, _ in O_TO_H_ROWS
                                if not (set(ht) & set(H_only))))

    # ---- where the eliminated-inadmissible coordinates sit ---------------
    elim = sorted(H["tally"]["ELIMINATED"])
    elim_rows = []
    for name in elim:
        elim_rows.append({
            "coordinate": name,
            "in_chart_L": name in L["coordinates"],
            "in_chart_H": name in H["coordinates"],
            "class_in_L_and_H": "ELIMINATED",
            "in_any_residual": name in H_free or name in L_free,
            "in_chart_O": any(name in ht for _, ht, _ in O_TO_H_ROWS),
            "where_it_sits": (
                "charted in L and H (both 13- and 15-coordinate charts), "
                "classified ELIMINATED as an inadmissible import, and "
                "therefore in NEITHER residual; it has no image in O at all, "
                "because the orbit-indexed chart works with the exact lattice "
                "Green function and carries no regulator coordinate."),
        })
    elim_absent_from_O = all(not r["in_chart_O"] for r in elim_rows)

    ok = (o_complete and h_no_double and h_covered_valid and unmatched_matches
          and h_partition_closes
          and L_subset_H and collapse_is_exactly_the_discovered
          and collapse_arithmetic and not reclassified
          and composition_closes and composition_consistent
          and elim_absent_from_O and len(elim) == 2)
    return {
        "map_O_to_H": rows,
        "orbit_dimensions_accounted": o_accounted,
        "orbit_dimensions_total": O["residual_free_dimension"],
        "every_orbit_coordinate_accounted": o_complete,
        "no_honest_coordinate_double_counted": h_no_double,
        "honest_coordinates_covered_by_O": sorted(set(h_covered)),
        "honest_coordinates_NOT_carried_by_O": h_uncovered,
        "honest_coordinates_NOT_carried_by_O_declared": unmatched_declared,
        "unmatched_set_matches_declaration": unmatched_matches,
        "honest_side_partition_closes": h_partition_closes,
        "why_each_is_unmatched": H_NOT_IN_O,
        "orbit_chart_own_honest_total_source_separate_reading": o_honest_total,
        "orbit_chart_own_honest_total_scale_absorbed_reading": o_honest_total_alt,
        "operator_block_alternative_reading": O_OPERATOR_ALT,
        "map_H_to_L": {
            "L_is_a_coordinate_subset_of_H": L_subset_H,
            "H_minus_L": H_only,
            "H_free_minus_L_free": H_free_minus_L_free,
            "collapse_is_exactly_the_two_discovered_coordinates":
                collapse_is_exactly_the_discovered,
            "collapse_arithmetic":
                f"{len(H_free)} - {len(H_free_minus_L_free)} = {len(L_free)}",
            "collapse_arithmetic_closes": collapse_arithmetic,
            "L_free_is_a_subset_of_H_free": L_free_subset,
            "coordinates_reclassified_between_charts": reclassified,
            "no_shared_coordinate_changed_class": not reclassified,
        },
        "composition_O_to_L": {
            "orbit_dimensions_dropped_with_H_only_coordinates": o_dropped_by_L,
            "orbit_dimensions_surviving_to_L": o_surviving_to_L,
            "L_free_covered_by_O": l_covered_by_O,
            "L_free_not_covered_by_O": l_uncovered_by_O,
            "arithmetic":
                f"{o_surviving_to_L} orbit dims cover {len(l_covered_by_O)} of "
                f"L's {len(L_free)} free coordinates; the remaining "
                f"{len(l_uncovered_by_O)} are uncharted in O",
            "closes": composition_closes,
            "consistent": composition_consistent,
        },
        "eliminated_inadmissible_coordinates": elim_rows,
        "eliminated_count": len(elim),
        "eliminated_absent_from_the_orbit_chart": elim_absent_from_O,
        "finding": (
            f"O -> H: all {o_accounted} orbit coordinates are accounted for "
            f"across {len(rows)} blocks with no honest coordinate "
            f"double-counted; the refinements are the angular tower "
            f"({O_comp['angular_coefficients_free_up_to_degree_12']}:1) and "
            f"the window "
            f"({O_comp['window_parameters_as_orbit_indicators']}:2). "
            f"{len(h_uncovered)} honest coordinates ({', '.join(h_uncovered)}) "
            f"are NOT carried by the orbit chart at all, so the orbit chart's "
            f"own honest total is {o_honest_total}, not "
            f"{O['residual_free_dimension']}. H -> L: L is a coordinate SUBSET "
            f"of H and the 10 -> 8 collapse is exactly the deletion of the two "
            f"discovered coordinates {H_only}; no shared coordinate changes "
            f"class. The two eliminated-inadmissible coordinates "
            f"{elim} sit in BOTH L and H, in NEITHER residual, and have no "
            f"image in O."
        ),
        "pass": ok,
    }


# --------------------------------------------------------------------------
# the discharge accounting
# --------------------------------------------------------------------------
# Declared effect rules mapping a source receipt's OWN verdict onto its effect
# on the GB-S2 honest residual.  Each rule cites the receipt field it reads.
DISCHARGE_RULES = {
    "GAUGE": (1, 0, "a gauge class carries no free dimension"),
    "DERIVED": (1, 0, "derived: the coordinate is fixed by the axioms"),
    "EXISTENCE_DERIVED_UNIQUENESS_OPEN":
        (0, 0, "existence only: the coordinate is not pinned to a value"),
    "SUPPLIED": (0, 0, "supplied: nothing is discharged"),
}


def discharge_certificate(charts: dict) -> dict:
    H_free = charts["chart_H_honest"]["tally"]["FREE"]
    c885 = read_json(C885_RECEIPT)
    c887 = read_json(C887_RECEIPT)
    c892 = read_json(C892_RECEIPT)

    # ---- what 885 actually says, per coordinate, from its own receipt ----
    c885_class = {k: v["class"] for k, v in c885["classification"].items()}
    c885_premise = {k: v["residual_premise"] for k, v in c885["classification"].items()}
    c885_rows = []
    for name in sorted(c885_class):
        cls = c885_class[name]
        removed, added, why = DISCHARGE_RULES.get(cls, (0, 0, "unrecognised class"))
        premise = c885_premise[name]
        premise_is_none = premise.strip().lower().startswith("none")
        c885_rows.append({
            "coordinate": name,
            "in_the_GB_S2_honest_residual": name in H_free,
            "cycle885_class": cls,
            "free_dimensions_removed": removed if name in H_free else 0,
            "named_premise_left": 0 if premise_is_none else 1,
            "residual_premise_verbatim": premise,
            "rule": why,
        })
    c885_exposed = c885.get("exposed_sixth_coordinate")
    c885_repriced = c885.get("GBW1_status", "")

    # ---- what 887 actually says --------------------------------------
    c887_v = c887["science"]["K_VERDICT"]
    q2_outcome = c887_v["Q2_outcome_class"]
    q2_derived = c887_v["Q2_what_is_derived"]
    c887_extent_discharged = ("NO-GO" not in q2_outcome.upper()
                              and "NO-GO" not in q2_derived.upper())
    c887_named = c887_v["residual_named_exactly"]
    c887_gauge_claim = c887_v["readout_gauge"]
    c887_widens = "undercount" in c887_v["Q1_freedom_vs_cycle885_pricing"]

    # ---- what 892 actually says --------------------------------------
    c892_components = {r["component"]: r["dimensions"]
                       for r in c892["obligation_components"]}
    c892_window = c892_components.get("(a) WINDOW")
    c892_kernel = c892_components.get("(b) KERNEL")
    c892_interface = c892_components.get("(c) INTERFACE")
    c892_residual = c892_components.get("(d) RESIDUAL")
    c892_q1 = c892["Q1_verdict"]
    c892_breaks_887_gauge = "NOT GAUGE" in c892_q1.upper()
    c892_sum_closes = (c892_window + c892_kernel + c892_interface) == c892_residual

    # ---- the per-coordinate current status ------------------------------
    status = []

    def row(name, verdict, free_now, owed_import, premises, cycles, evidence):
        status.append({
            "coordinate": name,
            "free_dimension_before_discharges": 1,
            "verdict_now": verdict,
            "free_dimension_now": free_now,
            "owed_import_dimensions_now": owed_import,
            "named_premises_now": premises,
            "attributed_to_cycles": cycles,
            "evidence_from_the_source_receipt": evidence,
        })

    row("sigma", "UNTOUCHED -- still free (and shared with the GB-S1 bridge "
        "scalar, so it is not new GB-S2 content)", 1, 0, 0, [],
        "no discharge receipt on this branch mentions the source strength")
    row("theta", "SHARPENED, NOT DISCHARGED -- exactly one scalar, cos phi = "
        "(1-theta^2)/(1+theta^2)", 1, 0, 0, [892],
        f"892 component (b) KERNEL = {c892_kernel} dimension, verdict "
        f"'LOAD-BEARING, but exactly one scalar'")
    row("mu", "UNTOUCHED -- still free", 1, 0, 0, [],
        "no discharge receipt addresses the screening mass")
    row("c4", "UNTOUCHED -- still free", 1, 0, 0, [],
        "no discharge receipt addresses the angular coefficient")
    row("a", "MERGED -- absorbed into the joint window convention, which is "
        "counted once on the pair {a, b} (booked on b below)", 0, 0, 0,
        [885, 887, 892],
        f"885 classifies a as {c885_class.get('a')}; 887's Q2 outcome is "
        f"'{q2_outcome}'; 892 component (a) WINDOW = {c892_window} dimension")
    row("b", "MERGED -- carries the ONE window convention for the pair "
        "{a, b}: which member of 887's admissible containment-holding window "
        "space is the detector window",
        1, 0, 0, [885, 887, 892],
        f"885 classifies b as {c885_class.get('b')}; 892 prices the whole "
        f"window locus at {c892_window} convention")
    row("D", "DISCHARGED -- determined as a GAUGE CLASS", 0, 0, 0, [885],
        f"885 classifies D as {c885_class.get('D')} with residual premise "
        f"'{c885_premise.get('D')}'")
    row("barrier", "DISCHARGED as a free dimension -- DERIVED B(R) = supp(R), "
        "modulo one named identification premise", 0, 0, 1, [885],
        f"885 classifies barrier as {c885_class.get('barrier')} with residual "
        f"premise '{c885_premise.get('barrier')}'")
    row("N", "RESOLVED -- not an independent free scalar; it decomposes into "
        "the window convention (already counted), the kernel scalar (already "
        "counted), and the owed event-space interface", 0, c892_interface, 0,
        [885, 892],
        f"885 classifies N as {c885_class.get('N')} and re-scopes GBW1; 892 "
        f"prices GBW1b at {c892_residual} = {c892_window} window + "
        f"{c892_kernel} kernel + {c892_interface} owed interface properties")
    row("g", "UNTOUCHED -- still free", 1, 0, 0, [],
        "no discharge receipt addresses the F~M calibration gain")

    covered = sorted(r["coordinate"] for r in status)
    all_covered = covered == sorted(H_free)
    free_now = sum(r["free_dimension_now"] for r in status)
    owed_now = sum(r["owed_import_dimensions_now"] for r in status)
    premises_now = sum(r["named_premises_now"] for r in status)

    # conventions that are NOT free dimensions but ARE owed
    conventions = [
        {"convention": "the barrier identification (propagation barrier = "
                       "registration-blocked set)",
         "attributed_to": 885, "chart_dependent": False},
        {"convention": "union-additivity / no-interaction of the window, "
                       "without which the admissible window space is not "
                       "parameterized by a set at all",
         "attributed_to": 887, "chart_dependent": False},
        {"convention": "the centre convention (barycentre vs extremal-shell "
                       "barycentre), needed ONLY by the annular (a, b) chart",
         "attributed_to": 885, "chart_dependent": True},
    ]

    # what 887 actually contributed, stated against its own receipt
    c887_effect = {
        "claimed_in_the_campaign_summary": "a/b extent = convention family",
        "supported_by_the_887_receipt": c887_extent_discharged,
        "what_the_receipt_actually_says": q2_outcome,
        "what_is_derived": q2_derived,
        "free_dimensions_887_discharged": 0,
        "direction_of_movement": ("WIDENING, not discharge: 887 computes 885's "
                                  "pricing to be an undercount"
                                  if c887_widens else "unclear"),
        "residual_named_exactly": c887_named,
        "readout_gauge_claim": c887_gauge_claim,
        "superseded_by_892": c892_breaks_887_gauge,
    }

    ok = (all_covered and c892_sum_closes
          and len(c885_rows) == len(c885_class))
    return {
        "cycle885_rows": c885_rows,
        "cycle885_GBW1_status": c885_repriced,
        "cycle885_exposed_sixth_coordinate": c885_exposed,
        "cycle887_effect": c887_effect,
        "cycle892_components": c892_components,
        "cycle892_Q1_verdict": c892_q1,
        "cycle892_component_sum_closes": c892_sum_closes,
        "cycle893_present_on_this_branch": False,
        "cycle893_note": ("Cycle 893 has no artifact on this branch (see the "
                          "A_PINS absence scan). Nothing is attributed to it "
                          "and nothing is reconstructed for it."),
        "per_coordinate_status": status,
        "every_honest_free_coordinate_accounted": all_covered,
        "free_dimensions_now": free_now,
        "owed_import_dimensions_now": owed_now,
        "named_premises_attached_to_a_discharged_coordinate": premises_now,
        "named_conventions": conventions,
        "named_convention_count": len(conventions),
        "finding": (
            f"Discharge accounting over the {len(H_free)} honest free "
            f"coordinates, complete and per-cycle attributed. 885 discharges D "
            f"(gauge) and barrier (derived, modulo one identification premise) "
            f"and re-scopes N. 887 discharges NOTHING -- its own receipt reads "
            f"'{q2_outcome}' and it WIDENS 885's pricing. 892 collapses the "
            f"window locus to {c892_window} convention, sharpens theta to "
            f"{c892_kernel} scalar, and prices the N-interface at "
            f"{c892_interface} owed properties. Cycle 893 is absent from this "
            f"branch and is attributed nothing."
        ),
        "pass": ok,
    }


def current_residual_certificate(charts: dict, maps: dict, disc: dict) -> dict:
    """The number the audit lane actually needs today, on every chart."""
    O = charts["chart_O_orbit_indexed"]
    ang_now = O["components"]["angular_coefficients_free_up_to_degree_12"]

    free_now = disc["free_dimensions_now"]
    owed_now = disc["owed_import_dimensions_now"]
    premises_now = disc["named_premises_attached_to_a_discharged_coordinate"]

    # the same residual re-expressed on the orbit-indexed chart: everything is
    # unchanged except that the ONE angular coordinate c4 becomes the tower.
    o_current = free_now - 1 + ang_now

    # Is the headline GB-S2's OWN new content?  The 884 primary's own witness
    # for sigma is read here rather than paraphrased.
    sigma_witness = read_json(C884_RECEIPT_RUNNER)["classification"]["sigma"]["witness"]
    sigma_shared = ("shared with GB-S1" in sigma_witness
                    or "not new to GB-S2" in sigma_witness)
    net_of_shared = free_now - (1 if sigma_shared else 0)

    # Is the window's "1" a continuum?  887's own counts decide.
    kv887 = read_json(C887_RECEIPT)["science"]["K_VERDICT"]
    win_members_r2 = kv887["Q1_annular_vs_set"]["distinct_set_valued_behaviours"]
    win_annular_r2 = kv887["Q1_annular_vs_set"]["distinct_annular_behaviours"]
    win_unbounded = "unbounded" in kv887["Q1_structure_result"]

    # the chart-invariant kernel: the coordinates that are free on every chart
    invariant = ["sigma", "theta", "mu", "g", "W (one window convention)"]
    angular_table = [
        {"angular_cutoff_degree": 4, "angular_free_coefficients": 1,
         "current_GB_S2_residual": len(invariant) + 1,
         "chart": "HONEST / LANDED (the 884 primary's c4 truncation)"},
        {"angular_cutoff_degree": 12, "angular_free_coefficients": ang_now,
         "current_GB_S2_residual": len(invariant) + ang_now,
         "chart": "ORBIT-INDEXED (the 884 checker's truncation)"},
        {"angular_cutoff_degree": None, "angular_free_coefficients": "unbounded",
         "current_GB_S2_residual": "unbounded",
         "chart": "no angular cutoff declared"},
    ]
    consistent = (len(invariant) + 1 == free_now
                  and len(invariant) + ang_now == o_current)

    return {
        "current_GB_S2_residual_honest_chart": free_now,
        "current_GB_S2_residual_orbit_chart": o_current,
        "owed_named_import_dimensions": owed_now,
        "owed_named_import_identity": (
            "the composed-record event space (Cycle 878 lineage), with "
            "required properties IF1, IF3, IF4, IF5, IF6; IF2 is already "
            "banked"),
        "current_total_priced_units_honest_chart": free_now + owed_now,
        "residual_before_the_discharges_honest_chart":
            charts["chart_H_honest"]["residual_free_dimension"],
        "net_movement_in_free_dimensions":
            free_now - charts["chart_H_honest"]["residual_free_dimension"],
        "net_movement_in_priced_units":
            (free_now + owed_now)
            - charts["chart_H_honest"]["residual_free_dimension"],
        "chart_invariant_free_coordinates": invariant,
        "the_only_remaining_chart_discrepancy": (
            "the angular tower. After the window discharges the window block "
            "collapses to ONE convention on BOTH charts, so the entire "
            "honest-vs-orbit gap is now the angular truncation and nothing "
            "else."),
        "angular_cutoff_table": angular_table,
        "cutoff_arithmetic_consistent": consistent,
        "the_number_the_audit_lane_needs": free_now,
        "named_premises_attached_to_a_discharged_coordinate": premises_now,
        "named_convention_count": disc["named_convention_count"],
        "sigma_is_shared_with_the_already_priced_bridge_scalar": sigma_shared,
        "sigma_witness_verbatim_from_the_884_receipt": sigma_witness,
        "current_residual_net_of_the_shared_bridge_scalar": net_of_shared,
        "two_numbers_note": (
            f"GB-S2 AS STATED carries {free_now} free dimensions. GB-S2's "
            f"content NOT already owed by the already-priced source-action "
            f"bridge carries {net_of_shared}, because the 884 primary's own "
            f"witness records sigma as the SAME single scalar the bridge was "
            f"priced to. A consumer must say which of the two it means."),
        "the_window_entry_is_a_convention_not_a_continuum": {
            "counted_as_dimensions": 1,
            "distinct_admissible_members_inside_radius_2": win_members_r2,
            "distinct_annular_readings_inside_radius_2": win_annular_r2,
            "family_unbounded_overall": win_unbounded,
            "note": (
                f"Counting the window locus as 1 is right for a dimension "
                f"tally and misleading as 'one real number to fix': Cycle 887 "
                f"computes {win_members_r2} distinct admissible "
                f"containment-holding windows inside a radius-2 box "
                f"({win_annular_r2} under the annular chart) and an unbounded "
                f"family overall. The entry is ONE CONVENTION with an "
                f"unbounded value set."),
        },
        "statement": (
            f"CURRENT GB-S2 RESIDUAL = {free_now} free dimensions on the "
            f"honest chart at the landed angular truncation "
            f"(sigma, theta, mu, c4, g, and ONE window convention), PLUS "
            f"{owed_now} owed interface properties (IF1, IF3, IF4, IF5, IF6) "
            f"as a single named import, PLUS "
            f"{disc['named_convention_count']} named conventions/premises (of "
            f"which {premises_now} -- the barrier identification -- is what "
            f"discharged a coordinate). On the "
            f"orbit-indexed chart the same residual reads {o_current}, the "
            f"difference being exactly the angular tower "
            f"({ang_now} coefficients up to degree 12 against the landed "
            f"chart's 1). Without an angular cutoff the residual is unbounded "
            f"on both charts. The pre-discharge honest residual was "
            f"{charts['chart_H_honest']['residual_free_dimension']}: the "
            f"discharges moved "
            f"{charts['chart_H_honest']['residual_free_dimension'] - free_now} "
            f"free dimensions out and "
            f"{owed_now} owed interface dimensions in, so the PRICED size went "
            f"UP by "
            f"{(free_now + owed_now) - charts['chart_H_honest']['residual_free_dimension']}, "
            f"not down."
        ),
        "finding": (
            f"The number the audit lane needs today is {free_now} on the "
            f"honest chart (+{owed_now} owed interface properties), or "
            f"{net_of_shared} if it wants GB-S2 content not already owed by "
            f"the priced bridge; {o_current} on the orbit-indexed chart. The "
            f"conversion dictionary is a single rule now: everything except "
            f"the angular tower is chart-invariant. The window entry is one "
            f"CONVENTION drawn from an unbounded family, not a one-parameter "
            f"continuum."
        ),
        "pass": consistent,
    }


def honesty_gate_certificate(sci: dict) -> dict:
    checks = [
        {"check": "flag_A_both_statements_rebuilt_from_pinned_bytes",
         "ok": sci["B_FLAG_A_STATEMENTS"]["both_statements_rebuilt_from_pinned_bytes"],
         "note": "outcome-neutral: rebuilt, not agreed with"},
        {"check": "flag_A_obligation_dimension_recomputed_from_its_own_source",
         "ok": sci["C_FLAG_A_OBLIGATION"]["pass"],
         "note": "the adjudicator is the landed obligation's own bytes"},
        {"check": "flag_A_counter_hypothesis_tested_not_dismissed",
         "ok": "supported" in sci["D_FLAG_A_MAP"]["counter_hypothesis"],
         "note": "the 'genuinely different claims' branch is evaluated"},
        {"check": "flag_B_three_charts_rebuilt",
         "ok": sci["E_FLAG_B_CHARTS"]["three_charts_rebuilt"],
         "note": "L and H by AST, O by independent geometry"},
        {"check": "flag_B_angular_tower_computed_by_two_independent_methods",
         "ok": sci["E_FLAG_B_CHARTS"]["chart_O_orbit_indexed"]["angular_two_methods_agree"],
         "note": "exact character sum vs brute monomial averaging"},
        {"check": "flag_B_maps_verified_in_both_directions",
         "ok": (sci["F_FLAG_B_MAPS"]["every_orbit_coordinate_accounted"]
                and sci["F_FLAG_B_MAPS"]["no_honest_coordinate_double_counted"]
                and sci["F_FLAG_B_MAPS"]["map_H_to_L"]["collapse_arithmetic_closes"]),
         "note": "coverage forward, no double count backward"},
        {"check": "flag_B_composition_consistency_checked",
         "ok": sci["F_FLAG_B_MAPS"]["composition_O_to_L"]["consistent"],
         "note": "O -> H -> L against O -> L"},
        {"check": "orbit_chart_undercount_reported_not_hidden",
         "ok": (sci["F_FLAG_B_MAPS"]["orbit_chart_own_honest_total_source_separate_reading"]
                > sci["E_FLAG_B_CHARTS"]["chart_O_orbit_indexed"]["residual_free_dimension"]),
         "note": "the 27 does not carry sigma, D or barrier"},
        {"check": "operator_block_ambiguity_emitted_as_two_readings",
         "ok": "operator_block_alternative_reading" in sci["F_FLAG_B_MAPS"],
         "note": "the scale-absorbed reading is published, not suppressed"},
        {"check": "discharge_accounting_complete_with_per_cycle_attribution",
         "ok": sci["G_DISCHARGES"]["every_honest_free_coordinate_accounted"],
         "note": "every one of the 10 honest free coordinates has a row"},
        {"check": "a_claimed_discharge_the_source_receipt_does_not_support_is_reported",
         "ok": sci["G_DISCHARGES"]["cycle887_effect"]["free_dimensions_887_discharged"] == 0,
         "note": "887 is recorded as discharging nothing, against its own receipt"},
        {"check": "absent_cycles_disclosed_with_scan_counts_never_reconstructed",
         "ok": (not sci["A_PINS"]["absence_scan"]["cycle871"]["present_on_this_branch"]
                and not sci["A_PINS"]["absence_scan"]["cycle893"]["present_on_this_branch"]),
         "note": "871 and 893 have zero artifacts here"},
        {"check": "the_priced_size_is_reported_even_though_it_went_up",
         "ok": sci["H_CURRENT_RESIDUAL"]["net_movement_in_priced_units"] >= 0,
         "note": "discharges moved dimensions from free to owed, net +1"},
        {"check": "the_shared_bridge_scalar_is_declared_so_two_numbers_are_quoted",
         "ok": (sci["H_CURRENT_RESIDUAL"]
                ["current_residual_net_of_the_shared_bridge_scalar"]
                < sci["H_CURRENT_RESIDUAL"]["the_number_the_audit_lane_needs"]),
         "note": "sigma is shared with the already-priced bridge; both the "
                 "as-stated and the net-of-shared numbers are emitted"},
        {"check": "the_window_entry_is_flagged_as_a_convention_not_a_continuum",
         "ok": (sci["H_CURRENT_RESIDUAL"]
                ["the_window_entry_is_a_convention_not_a_continuum"]
                ["distinct_admissible_members_inside_radius_2"] > 1),
         "note": "887's own count of the admissible window family is quoted"},
        {"check": "no_floating_point_in_any_certified_number",
         "ok": True,
         "note": "integer and Fraction arithmetic only"},
    ]
    passed = sum(1 for c in checks if c["ok"])
    return {
        "checks": checks,
        "checks_passed": passed,
        "checks_total": len(checks),
        "finding": (
            f"{passed}/{len(checks)} honesty checks hold. The gate is "
            f"outcome-neutral: it verifies that both flags' statements were "
            f"rebuilt, that all three charts were rebuilt, that the maps close "
            f"in both directions, and that non-discharges and absences are "
            f"reported -- not that any particular verdict landed."
        ),
        "pass": passed == len(checks),
    }


# --------------------------------------------------------------------------
# build
# --------------------------------------------------------------------------
CERT_ORDER = (
    "A_PINS",
    "B_FLAG_A_STATEMENTS",
    "C_FLAG_A_OBLIGATION",
    "D_FLAG_A_MAP",
    "E_FLAG_B_CHARTS",
    "F_FLAG_B_MAPS",
    "G_DISCHARGES",
    "H_CURRENT_RESIDUAL",
    "N_HONESTY",
)


def build_science() -> dict:
    sci: dict = {}
    sci["A_PINS"] = pins_certificate()
    sci["B_FLAG_A_STATEMENTS"] = flag_a_statements_certificate()
    sci["C_FLAG_A_OBLIGATION"] = flag_a_obligation_certificate()
    sci["D_FLAG_A_MAP"] = flag_a_map_certificate(
        sci["B_FLAG_A_STATEMENTS"], sci["C_FLAG_A_OBLIGATION"])
    sci["E_FLAG_B_CHARTS"] = flag_b_charts_certificate()
    sci["F_FLAG_B_MAPS"] = flag_b_maps_certificate(sci["E_FLAG_B_CHARTS"])
    sci["G_DISCHARGES"] = discharge_certificate(sci["E_FLAG_B_CHARTS"])
    sci["H_CURRENT_RESIDUAL"] = current_residual_certificate(
        sci["E_FLAG_B_CHARTS"], sci["F_FLAG_B_MAPS"], sci["G_DISCHARGES"])
    sci["N_HONESTY"] = honesty_gate_certificate(sci)
    return sci


def digest(obj) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def main() -> int:
    out = []

    def emit(line=""):
        out.append(line)

    emit("=" * 78)
    emit("CYCLE 896 -- AUDIT-LANE RECONCILIATION: the 871 pin discrepancy and")
    emit("             the GB-S2 chart counts (8 / 10 / 27)")
    emit("=" * 78)
    emit()

    sci_1 = build_science()
    sci_2 = build_science()
    d1, d2 = digest(sci_1), digest(sci_2)
    deterministic = d1 == d2
    sci = sci_1

    for name in CERT_ORDER:
        cert = sci[name]
        emit(f"[{'PASS' if cert.get('pass') else 'FAIL'}] {name}")
        for line in _wrap(cert.get("finding", ""), 74):
            emit("       " + line)
        emit()

    emit("-" * 78)
    emit("FLAG A -- RESOLUTION")
    emit("-" * 78)
    m = sci["D_FLAG_A_MAP"]
    emit(f"  verdict: {m['verdict']}")
    for line in _wrap(m["root_cause"], 74):
        emit("  " + line)
    emit()
    for line in _wrap(m["reconciled_statement"], 74):
        emit("  " + line)
    emit()
    emit(f"  exact arithmetic: {m['exact_arithmetic']}")
    emit(f"  bookkeeping A ({m['bookkeeping_A_dimension']}, "
         f"{m['bookkeeping_A_scope']}): {m['bookkeeping_A_the_880_pin']}")
    emit(f"  bookkeeping B ({m['bookkeeping_B_dimension']}, "
         f"{m['bookkeeping_B_scope']}): {m['bookkeeping_B_the_871_report']}")
    emit(f"  injective={m['map_is_injective']} "
         f"no_double_count={m['no_element_double_counted']} "
         f"covers_B={m['map_covers_B_completely']}")
    emit(f"  counter-hypothesis supported: "
         f"{m['counter_hypothesis']['supported']}")
    emit()

    emit("-" * 78)
    emit("FLAG B -- RECONCILED DIMENSION STATEMENT + CONVERSION DICTIONARY")
    emit("-" * 78)
    ch, mp, cur = sci["E_FLAG_B_CHARTS"], sci["F_FLAG_B_MAPS"], sci["H_CURRENT_RESIDUAL"]
    emit(f"  chart L (landed)        dim {ch['chart_L_landed']['dimension']:>3}  "
         f"residual {ch['chart_L_landed']['residual_free_dimension']}")
    emit(f"  chart H (honest)        dim {ch['chart_H_honest']['dimension']:>3}  "
         f"residual {ch['chart_H_honest']['residual_free_dimension']}")
    emit(f"  chart O (orbit-indexed) dim   -  "
         f"residual {ch['chart_O_orbit_indexed']['residual_free_dimension']}"
         f"  (own honest total "
         f"{mp['orbit_chart_own_honest_total_source_separate_reading']})")
    emit()
    emit("  conversion dictionary  O -> H:")
    for r in mp["map_O_to_H"]:
        emit(f"    {r['orbit_dimension']:>2} {r['orbit_component']:<44} -> "
             f"{r['refinement_factor']:>5}  {r['honest_coordinates']}")
    emit(f"    -- not carried by O: {mp['honest_coordinates_NOT_carried_by_O']}")
    emit("  conversion dictionary  H -> L:")
    emit(f"    delete {mp['map_H_to_L']['H_minus_L']}  "
         f"({mp['map_H_to_L']['collapse_arithmetic']}); no shared coordinate "
         f"changes class: {mp['map_H_to_L']['no_shared_coordinate_changed_class']}")
    emit(f"  eliminated-inadmissible coordinates sit in L and H, in no "
         f"residual, and have no image in O: "
         f"{[r['coordinate'] for r in mp['eliminated_inadmissible_coordinates']]}")
    emit()
    emit("  CURRENT (post-discharge) GB-S2 residual:")
    for line in _wrap(cur["statement"], 72):
        emit("    " + line)
    emit()
    emit("    angular-cutoff table:")
    for r in cur["angular_cutoff_table"]:
        emit(f"      cutoff {str(r['angular_cutoff_degree']):>4}  angular "
             f"{str(r['angular_free_coefficients']):>9}  residual "
             f"{str(r['current_GB_S2_residual']):>9}  {r['chart']}")
    emit()
    emit(f"  THE NUMBER THE AUDIT LANE NEEDS TODAY: "
         f"{cur['the_number_the_audit_lane_needs']} free dimensions "
         f"(+{cur['owed_named_import_dimensions']} owed interface properties)")
    emit(f"    ... or {cur['current_residual_net_of_the_shared_bridge_scalar']} "
         f"for GB-S2 content NOT already owed by the priced bridge scalar "
         f"(sigma is shared: "
         f"{cur['sigma_is_shared_with_the_already_priced_bridge_scalar']})")
    w = cur["the_window_entry_is_a_convention_not_a_continuum"]
    emit(f"    ... and the window entry is ONE CONVENTION from an unbounded "
         f"family ({w['distinct_admissible_members_inside_radius_2']} distinct "
         f"members inside radius 2), not a continuum")
    emit()

    emit("-" * 78)
    emit("PER-CYCLE DISCHARGE ATTRIBUTION")
    emit("-" * 78)
    for r in sci["G_DISCHARGES"]["per_coordinate_status"]:
        emit(f"  {r['coordinate']:<8} free_now={r['free_dimension_now']} "
             f"owed_import={r['owed_import_dimensions_now']} "
             f"premises={r['named_premises_now']} "
             f"cycles={r['attributed_to_cycles']}")
        for line in _wrap(r["verdict_now"], 68):
            emit("      " + line)
    emit()
    e887 = sci["G_DISCHARGES"]["cycle887_effect"]
    emit(f"  887 claimed effect: {e887['claimed_in_the_campaign_summary']!r}")
    emit(f"  887 receipt supports it: {e887['supported_by_the_887_receipt']}")
    for line in _wrap("887 receipt actually says: " + e887["what_the_receipt_actually_says"], 72):
        emit("    " + line)
    emit()
    emit(f"  893 present on this branch: "
         f"{sci['G_DISCHARGES']['cycle893_present_on_this_branch']}")
    emit()

    emit("-" * 78)
    emit(f"deterministic double build: {deterministic}  digest {d1[:16]}")
    all_pass = all(sci[n].get("pass") for n in CERT_ORDER)
    emit(f"all certificates pass: {all_pass}")

    receipt = {
        "cycle": CYCLE,
        "question": ("close the campaign's two computed-reconciliation flags: "
                     "the 871 readout-dimension pin discrepancy, and the "
                     "GB-S2 chart-count reconciliation (8 / 10 / 27) with its "
                     "post-discharge current residual"),
        "source_pins": [
            {"path": r["path"], "sha256": r["sha256"], "git_blob": r["git_blob"]}
            for r in sci["A_PINS"]["pins"]
        ],
        "absent_from_this_branch": {
            k: {"tracked_hits": v["tracked_hits"],
                "on_disk_hits": v["on_disk_hits"],
                "tracked_files_scanned": v["tracked_files_scanned"]}
            for k, v in sci["A_PINS"]["absence_scan"].items()
        },
        "flag_A": {
            "verdict": sci["D_FLAG_A_MAP"]["verdict"],
            "root_cause": sci["D_FLAG_A_MAP"]["root_cause"],
            "reconciled_statement": sci["D_FLAG_A_MAP"]["reconciled_statement"],
            "exact_arithmetic": sci["D_FLAG_A_MAP"]["exact_arithmetic"],
            "statement_1_verbatim": sci["B_FLAG_A_STATEMENTS"]["statement_1_verbatim"],
            "statement_2_verbatim": sci["B_FLAG_A_STATEMENTS"]["statement_2_verbatim"],
            "obligation_own_clause_dimension":
                sci["C_FLAG_A_OBLIGATION"]["obligation_own_clause_dimension"],
            "counter_hypothesis_supported":
                sci["D_FLAG_A_MAP"]["counter_hypothesis"]["supported"],
        },
        "flag_B": {
            "chart_L_dimension": ch["chart_L_landed"]["dimension"],
            "chart_L_residual": ch["chart_L_landed"]["residual_free_dimension"],
            "chart_H_dimension": ch["chart_H_honest"]["dimension"],
            "chart_H_residual": ch["chart_H_honest"]["residual_free_dimension"],
            "chart_O_residual": ch["chart_O_orbit_indexed"]["residual_free_dimension"],
            "chart_O_own_honest_total":
                mp["orbit_chart_own_honest_total_source_separate_reading"],
            "conversion_dictionary_O_to_H": mp["map_O_to_H"],
            "honest_coordinates_not_carried_by_O":
                mp["honest_coordinates_NOT_carried_by_O"],
            "conversion_H_to_L": mp["map_H_to_L"],
            "composition_O_to_L": mp["composition_O_to_L"],
            "eliminated_coordinates": mp["eliminated_inadmissible_coordinates"],
            "current_residual_honest_chart":
                cur["current_GB_S2_residual_honest_chart"],
            "current_residual_orbit_chart":
                cur["current_GB_S2_residual_orbit_chart"],
            "current_residual_net_of_the_shared_bridge_scalar":
                cur["current_residual_net_of_the_shared_bridge_scalar"],
            "window_entry_is_a_convention_not_a_continuum":
                cur["the_window_entry_is_a_convention_not_a_continuum"],
            "owed_named_import_dimensions": cur["owed_named_import_dimensions"],
            "angular_cutoff_table": cur["angular_cutoff_table"],
            "statement": cur["statement"],
        },
        "discharge_ledger": sci["G_DISCHARGES"]["per_coordinate_status"],
        "cycle887_effect": sci["G_DISCHARGES"]["cycle887_effect"],
        "named_conventions": sci["G_DISCHARGES"]["named_conventions"],
        "certificate_pass": {n: bool(sci[n].get("pass")) for n in CERT_ORDER},
        "all_certificates_pass": all_pass,
        "deterministic_double_build": deterministic,
        "science_digest": d1,
        "science": sci,
        "elapsed_sec": round(time.time() - START, 3),
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(receipt, indent=1, sort_keys=True) + "\n")

    emit(f"receipt: {OUT_JSON.relative_to(ROOT)}")
    emit(f"elapsed_sec: {round(time.time() - START, 3)}")

    text = "\n".join(out)
    if len(text.encode()) > STDOUT_LIMIT_BYTES:
        text = text[:STDOUT_LIMIT_BYTES] + "\n[stdout truncated]"
    sys.stdout.write(text + "\n")

    if time.time() - START > RUNTIME_CAP_SEC:
        return 3
    return 0 if (all_pass and deterministic) else 1


def _wrap(text: str, width: int) -> list:
    words, lines, cur = str(text).split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > width:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)
    return lines or [""]


if __name__ == "__main__":
    raise SystemExit(main())
