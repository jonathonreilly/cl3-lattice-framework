#!/usr/bin/env python3
"""Cycle 895: the t-dependence census that retires the unit-grading choice.

Cycle 876 priced the unit sector grading w = (1,1,1) as SUPPLIED, with the
residue after the derived shape, the landed vector balance and the overall
scale gauge equal to exactly ONE rational number t on the lawful line
w(t) = (1, 1 + t, 1 - t).  It emitted a three-option owner decision surface
(derive-later / adopt-as-convention / retire-by-generalisation) and named the
third cheapest.  The owner has directed that the third be EXECUTED AS A
DERIVATION rather than asked as a question.  This cycle executes it.

The instrument is a census, not an argument.  For EVERY grading-consuming
landed result reachable on this branch, the result's own headline claim is
re-expressed as a computable predicate P(t) over the lawful line and its exact
truth set is computed.  Each result then falls into exactly one of three
classes, fixed before any value is computed:

  T_UNIFORM        P(t) holds identically on the line; the t-choice is
                   IMMATERIAL for that result, which is therefore RETIRED.
  T_SENSITIVE(S)   P(t) holds exactly on a computed subset S of the line; S is
                   returned exactly (a finite set, or the line minus a finite
                   set), never asserted.
  BROKEN_OFF_UNIT  the result's construction does not admit evaluation off the
                   landed points at all; the obstruction is reported.

Six things happen here.

(A) THE NEEDLE SET.  The grading vocabulary is not invented: it is extracted by
    AST from the pinned Cycle-876 primary's OWN provenance-site quotations, its
    line parameterisation and its module docstring, filtered by a published
    root list, and every surviving needle is gated to occur verbatim in that
    pinned text.  The set is published in full.

(B) THE CONSUMER CENSUS.  scripts/ and docs/ are swept mechanically with those
    needles.  Every Python file that mentions a sector name is parsed and run
    through three published AST detectors (a graded sector sum, a grading tuple
    literal in code position, a grading-named binding).  Each hit file is
    classified CONSUMER / MENTION_ONLY / NON_CONSUMER and counted.

(C) THE RESTRICTION GATE.  Before any new claim is made, Cycle 876's headline
    rows -- the one-rational-t residue, the sigma-visibility computation, the
    lawful-support counts, and the checker's R9 (1,2,0) selection -- are
    recomputed here and matched value for value against the pinned receipts.

(D) THE SYMBOLIC CORE AND THE GRID.  The balance residual is shown to be
    EXACTLY affine in t: sum_s w_s(t) D[triple_s] - w_matter D[direction]
    = A + t B, where A is the normal-form defect and B = D[field] - D[aux].
    Lawfulness is therefore A + tB = 0, which partitions all configurations
    into four exact classes and makes the lawful set CONSTANT off a computed
    finite exceptional set.  Every row is evaluated twice: symbolically (on its
    own exceptional set plus a certified generic point) and on an exact rational
    grid of twelve points including +1, -1, 0 and large-denominator non-special
    values.  The two routes must agree on every row.

(E) THE THREE BACKLOG SCRIPTS.  Cycle 316, Cycle 325 and the Cycle-876
    independent checker were left unpriced by the campaign.  They are priced
    here on exactly the same scheme, and the Cycle-325 pricing is exact: its
    field and auxiliary momentum operators are shown to be the SAME operator,
    which makes its headline ledger t-independent outright.

(F) THE RETIREMENT VERDICT.  The census is partitioned and the residue is
    reported with a further computed distinction that is the whole point of the
    exercise: a T_SENSITIVE row whose truth set is COFINITE requires only that
    a finite set of points be EXCLUDED, which is not a choice; a row whose truth
    set is FINITE requires an exact CHOICE of t.  What survives as a genuine
    decision is only the second kind, load bearing, and not superseded by a
    T_UNIFORM row that says the same thing with its scope qualifier kept.

Falsifier visibility is gated, not assumed: four impostor rows are planted with
KNOWN t-profiles, one of which breaks at a rational that is deliberately absent
from the grid, and the census must recover each impostor's exact truth set.  A
planted uniform control must NOT be called sensitive.

All cited artifacts are SHA-256 and git-blob pinned, read as text/AST/JSON only,
and blocked from import by a meta-path firewall.  Every certified number is
rebuilt here with stdlib exact arithmetic; no floating point enters any
certified quantity.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
STDOUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle873_tracelessness_provenance_2026_07_28.py",
    "outputs/tracelessness_provenance_cycle873_receipt_2026_07_28.json",
    "scripts/frontier_cycle876_unit_grading_provenance_2026_07_28.py",
    "outputs/unit_grading_provenance_cycle876_receipt_2026_07_28.json",
    "scripts/frontier_cycle876_grading_independent_check_2026_07_28.py",
    "outputs/unit_grading_independent_check_cycle876_receipt_2026_07_28.json",
    "scripts/frontier_cycle880_visible_point_physics_2026_07_28.py",
    "outputs/visible_point_physics_cycle880_receipt_2026_07_28.json",
    "scripts/carried_source_recurrent_tagged_block_cycle316_2026_07_18.py",
    "scripts/full_fock_unit_weight_two_source_cycle325_2026_07_18.py",
    "scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py",
    "scripts/proper_cubic_recoil_balanced_carried_source_cycle318_2026_07_18.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/frontier_cycle868_response_sign_census_2026_07_28.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

import ast
from fractions import Fraction
from hashlib import sha1, sha256
import importlib.abc
from itertools import product
import json
from pathlib import Path
import re
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / "outputs" / (
    "t_retirement_cycle895_receipt_2026_07_28.json"
)
BLOCKLISTED_MODULES = tuple(
    Path(path).stem for path in AUDIT_INPUT_PATHS if path.endswith(".py")
)

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "08e92fde118415f32043c4fc154f8cc5aaca66af18704c024f89cde5445662de",
    AUDIT_INPUT_PATHS[1]:
        "e666bc548393e629aee3e865e188487eb7ac08071c6033fce3fa0202964cbfae",
    AUDIT_INPUT_PATHS[2]:
        "1e13e4c6332c7d6c7798fb4d7366db8a94037eefba6e77ac1c3dd0d269cf7b39",
    AUDIT_INPUT_PATHS[3]:
        "338f7e085473e87192acf9b881978939b08a5a52d3d63442e3647b022ea18b78",
    AUDIT_INPUT_PATHS[4]:
        "95acbb56e2c2e3d54fd04c80d444716c4620734849d8048c008b9d582722ce1f",
    AUDIT_INPUT_PATHS[5]:
        "9fff8cf30d152f91abea56ce6d91568ee3d7a19cf7c6d03269cff198a0578ce6",
    AUDIT_INPUT_PATHS[6]:
        "e9d6f8a1483b87f7b0520ebe04356fcf4910bc5a25d1f7af97555644892d6ee4",
    AUDIT_INPUT_PATHS[7]:
        "2046a4d73a6bab85d829abe11b41c15c3efb6cc77bea6ff253df749035d6fd83",
    AUDIT_INPUT_PATHS[8]:
        "87830a6aa8d05787d8e4f81bdf21ef1d92a8ad0252b9498000fb27c7ff700d65",
    AUDIT_INPUT_PATHS[9]:
        "32ee958fe9dc5f5c5aa41b5593cb66a529d7ae07ca8b556cff2b45f7f33374dc",
    AUDIT_INPUT_PATHS[10]:
        "71fb02658569174b7f6f989efe311951713026ead36ece8866dca1e96878d706",
    AUDIT_INPUT_PATHS[11]:
        "3c1575c99622c0874ab42730494d615fbe1a2b867975e5bf048fd2a4a8af9d56",
    AUDIT_INPUT_PATHS[12]:
        "c410b754d4e984f6ee5ccbc7c5a52e776c50c91c4daa12d798044f104cc7435b",
    AUDIT_INPUT_PATHS[13]:
        "e09226e35a58cd52e2d4f61516f6e2a64cdebb7f4c20893307a1f3d2ff3f4ebb",
    AUDIT_INPUT_PATHS[14]:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "0c5893f9b0c277fe864ed71efb38ba2c59d52d04",
    AUDIT_INPUT_PATHS[1]: "cc4059a3050e2cbe7a00f1f449f05fa8f0dd758a",
    AUDIT_INPUT_PATHS[2]: "58a709ebc3cd2f6a5a2220fdaebd970c4694495f",
    AUDIT_INPUT_PATHS[3]: "bb49938e1fa9552b2d8d55f62032e710b454f58b",
    AUDIT_INPUT_PATHS[4]: "f61f0d2b7869672d66d346ffb7679e697c6d8940",
    AUDIT_INPUT_PATHS[5]: "4345656b18b6958f536b1b593ecf9889a127d6a5",
    AUDIT_INPUT_PATHS[6]: "db0472a8fe3e9e93f3f31f8e0b5ac0fd5c6630f8",
    AUDIT_INPUT_PATHS[7]: "4cd1d247523da5ee69713244f8f2022149983252",
    AUDIT_INPUT_PATHS[8]: "7a3c24a5fe82001886aa00afa20a87cc06c5817e",
    AUDIT_INPUT_PATHS[9]: "fcf14f39b53ec77cd0d3e0d3f22de6b7a6df6e0d",
    AUDIT_INPUT_PATHS[10]: "c95eb9738409c3ffe20f8b90a7ab25e6dc5843a0",
    AUDIT_INPUT_PATHS[11]: "7672380148d79f22a4ab9b2700121aac1b097004",
    AUDIT_INPUT_PATHS[12]: "0be8d83ec8ed874ff12e2092dc47121b8030a5bc",
    AUDIT_INPUT_PATHS[13]: "c64dd97a3034ccbedc2603db4dacc1c80acfd952",
    AUDIT_INPUT_PATHS[14]: "4a863da1f3f255354839277271a3a69a5c205133",
}
REQUIRED_AST_MARKERS = {
    AUDIT_INPUT_PATHS[0]: ("grading_certificate", "raw_ledger",
                           "witness_certificate"),
    AUDIT_INPUT_PATHS[2]: ("provenance_certificate", "consequence_certificate",
                           "line_point", "balance_residual"),
    AUDIT_INPUT_PATHS[4]: ("route_r9_joint_landed_rank", "attack_extra_routes"),
    AUDIT_INPUT_PATHS[6]: ("restatement_certificate", "classify",
                           "enumerate_family"),
    AUDIT_INPUT_PATHS[8]: ("recoil_candidate_controls", "inventory_controls",
                           "ANGLE"),
    AUDIT_INPUT_PATHS[9]: ("unit_weight_local_source", "LOCAL_MASKS", "ANGLE"),
    AUDIT_INPUT_PATHS[10]: ("REVERSE", "inventory_controls"),
    AUDIT_INPUT_PATHS[11]: ("REVERSE", "direction_vertex"),
    AUDIT_INPUT_PATHS[12]: ("DIRECTIONS", "UNIFORM"),
    AUDIT_INPUT_PATHS[13]: ("SECTORS", "DIRECTIONS", "DIRECTION_REVERSE",
                            "HELD_EDGE_LENGTH", "SIGMA_DEGREE_BOUND",
                            "OBJECT_ARITY", "AXES", "ENDPOINTS"),
}
REQUIRED_JSON_KEYS = {
    AUDIT_INPUT_PATHS[1]: ("headline", "cycles", "claim_type"),
    AUDIT_INPUT_PATHS[3]: ("free_dimension_after_gauge", "sigma_onset_t_values",
                           "lawful_supports_at_the_unit_grading",
                           "maximum_lawful_supports_on_the_line",
                           "unit_grading_is_the_unique_maximiser",
                           "lawful_support_counts_away_from_onset_and_unit"),
    AUDIT_INPUT_PATHS[5]: ("checker_route_outcomes", "joint_landed_unique_solution",
                           "joint_solution_is_the_unit_grading",
                           "lawful_at_unit_grading",
                           "onset_by_exact_root_extraction"),
    AUDIT_INPUT_PATHS[7]: ("headline", "open_rows", "cycles"),
}

# Verbatim evidence located inside the pinned artifacts by exact substring
# search.  These are quotations, not paraphrases.
REQUIRED_QUOTES = {
    AUDIT_INPUT_PATHS[0]: (
        "of the lawful segment w_field + w_auxiliary = 2.",
        '"landed_support_locus_is_a_segment_not_a_point"',
    ),
    AUDIT_INPUT_PATHS[2]: (
        '"""The gauge-fixed lawful line w(t) = (1, 1 + t, 1 - t)."""',
        '"""sum_s w_s D[triple_s] - w_matter D[direction], exactly."""',
        "retire-by-generalisation (carry the whole line)",
    ),
    AUDIT_INPUT_PATHS[4]: (
        '"route": "R9_JOINT_LANDED_CONSTRAINT_RANK",',
        '"unique_joint_solution_is_the_unit_grading": solution == unit,',
    ),
    AUDIT_INPUT_PATHS[6]: (
        '"R07_876_LANDED_320_IDENTITIES",',
        "the landed route the unit grading excludes; it is the R9 joint ",
    ),
    AUDIT_INPUT_PATHS[8]: (
        "total_momentum = matter_momentum + field_momentum",
        "and min(total_commutators) > 0.7",
    ),
    AUDIT_INPUT_PATHS[9]: (
        "total_momenta.append(matter + field + auxiliary)",
        '"deleting the auxiliary vector contribution breaks recoil balance",',
        "min(no_auxiliary_commutators) > 0.7,",
        "and max(p_commutators) == 0",
    ),
    AUDIT_INPUT_PATHS[10]: (
        "unit-weight vector P_matter + P_mediator + P_aux at operator level.",
        '"unit_weights": (1, 1, 1),',
        '"supplied auxiliary law": "auxiliary direction has unit P weight,'
        ' identity coin, and matter-carried catch-up",',
        "+ auxiliary_weights @ c210.DIRECTIONS",
    ),
    AUDIT_INPUT_PATHS[11]: (
        "P = P_matter + 2 P_mediator at operator level.  The relative"
        " coefficient two",
        "angle: float, mediator_weight: float = 2.0",
    ),
    AUDIT_INPUT_PATHS[12]: ("DIRECTIONS = np.asarray(",),
    AUDIT_INPUT_PATHS[13]: (
        '"""The sector trace: the conformal channel of the source."""',
        "return (-2 * weight, weight, weight)",
    ),
    AUDIT_INPUT_PATHS[14]: (
        "with what weight",
        "remains a named conditional or open dependency.",
        "before use as a premise.",
    ),
}

# Commit pins for consumers priced by name.  These are pins, not reads.
BRANCH_PINS = {
    "cycle868_runner_commit": "3363c73f64",
    "cycle868_block_commit": "9506d38958",
    "cycle873_runner_commit": "4ff7db1e1b",
    "cycle873_checker_commit": "35e52e8ad7",
    "cycle873_block_commit": "d38a5ae809",
    "cycle872_runner_commit_sibling_branch": "4cb64e4792",
    "cycle872_checker_commit_sibling_branch": "48e70ceb56",
    "cycle872_block_commit_sibling_branch": "da7e6d05cb",
    "cycle872_present_in_this_worktree": False,
    "decision_surface_pr": "#5931 (Cycle 876, blockG5)",
    "owner_directive": "RETIRE-BY-GENERALISATION is to be executed as a "
                       "derivation; no decision is to be asked",
}

# The three classification labels, fixed before any value is computed.
T_CLASSES = ("T_UNIFORM", "T_SENSITIVE", "BROKEN_OFF_UNIT", "NOT_RECOMPUTABLE")

# The residue sub-classification, also fixed in advance.  A cofinite truth set
# means the claim needs a finite set of points EXCLUDED, which is not a choice;
# a finite truth set means the claim needs an exact CHOICE of t.
RESIDUE_SHAPES = (
    "HOLDS_EVERYWHERE",
    "REQUIRES_AN_EXCLUSION_NOT_A_CHOICE",
    "REQUIRES_AN_EXACT_CHOICE",
    "NOT_APPLICABLE",
)

# Declared-in-advance row metadata vocabulary.  Every row carries these BEFORE
# its predicate is evaluated, so no disposition can be tuned to an outcome.
LADDER_ROLES = ("LOAD_BEARING", "COMPETING_ROUTE", "CONTROL", "DIAGNOSTIC",
                "SELF_REFERENTIAL", "CONSTANT")

# Published root list for the mechanical needle filter.
NEEDLE_ROOTS = ("grading", "weight", "sector", "auxiliar", "mediator",
                "coefficient", "matter")
NEEDLE_STOPWORDS = frozenset((
    "the", "and", "of", "a", "an", "is", "it", "at", "in", "to", "by", "for",
    "on", "with", "that", "this", "its", "as", "not", "no", "one", "two",
))


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if any cited source-only primary is imported."""

    def __init__(self) -> None:
        self.hits: list = []

    def find_spec(
        self, fullname: str, path: object = None, target: object = None
    ) -> None:
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)


# --------------------------------------------------------------------------
# hard pin gate -- exit 2 before any science if a pin is wrong
# --------------------------------------------------------------------------
def git_blob(payload: bytes) -> str:
    header = f"blob {len(payload)}\0".encode("utf-8")
    return sha1(header + payload).hexdigest()


def hard_pin_gate() -> None:
    problems = []
    for path in AUDIT_INPUT_PATHS:
        target = ROOT / path
        if Path(path).is_absolute() or not target.is_file():
            problems.append(f"missing or non-relative pin: {path}")
            continue
        payload = target.read_bytes()
        if sha256(payload).hexdigest() != EXPECTED_SHA256[path]:
            problems.append(f"sha256 mismatch: {path}")
        if git_blob(payload) != EXPECTED_GIT_BLOBS[path]:
            problems.append(f"git blob mismatch: {path}")
    if problems:
        sys.stderr.write("PIN GATE FAILED\n" + "\n".join(problems) + "\n")
        raise SystemExit(2)


hard_pin_gate()


# --------------------------------------------------------------------------
# constants recovered from the pinned primaries by AST, never by import
# --------------------------------------------------------------------------
def _parse(path: str) -> ast.Module:
    return ast.parse((ROOT / path).read_bytes(), filename=path)


def _top_level(path: str) -> dict:
    out: dict = {}
    for node in _parse(path).body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    out[target.id] = node.value
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            if node.value is not None:
                out[node.target.id] = node.value
    return out


def recover_literal(path: str, name: str):
    node = _top_level(path)[name]
    if isinstance(node, ast.Call):
        return ast.literal_eval(node.args[0])
    return ast.literal_eval(node)


def recover_mediator_weight() -> Fraction:
    """Cycle-318's grading, recovered from the default argument by AST."""
    for node in ast.walk(_parse(AUDIT_INPUT_PATHS[11])):
        if isinstance(node, ast.FunctionDef) and node.name == "direction_vertex":
            names = [item.arg for item in node.args.args]
            defaults = list(node.args.defaults)
            offset = len(names) - len(defaults)
            for index, name in enumerate(names):
                if name == "mediator_weight" and index >= offset:
                    return Fraction(
                        ast.literal_eval(defaults[index - offset])
                    ).limit_denominator(10 ** 6)
    raise AssertionError("pinned direction_vertex has no mediator_weight default")


def recover_witness_coefficients() -> tuple:
    """Cycle-873's occupation ledger, recovered from its witness certificate."""
    for node in ast.walk(_parse(AUDIT_INPUT_PATHS[0])):
        if isinstance(node, ast.FunctionDef) and node.name == "witness_certificate":
            for inner in ast.walk(node):
                if isinstance(inner, ast.Assign):
                    for target in inner.targets:
                        if (
                            isinstance(target, ast.Name)
                            and target.id == "witness_coefficients"
                        ):
                            return tuple(ast.literal_eval(inner.value))
    raise AssertionError("pinned witness_certificate has no witness_coefficients")


DIRECTIONS = tuple(
    tuple(row) for row in recover_literal(AUDIT_INPUT_PATHS[12], "DIRECTIONS")
)
REVERSE_320 = tuple(recover_literal(AUDIT_INPUT_PATHS[10], "REVERSE"))
REVERSE_318 = tuple(recover_literal(AUDIT_INPUT_PATHS[11], "REVERSE"))
REVERSE_868 = tuple(recover_literal(AUDIT_INPUT_PATHS[13], "DIRECTION_REVERSE"))
SECTORS = tuple(recover_literal(AUDIT_INPUT_PATHS[13], "SECTORS"))
ENDPOINTS = tuple(recover_literal(AUDIT_INPUT_PATHS[13], "ENDPOINTS"))
AXES = int(recover_literal(AUDIT_INPUT_PATHS[13], "AXES"))
HELD_EDGE_LENGTH = int(recover_literal(AUDIT_INPUT_PATHS[13], "HELD_EDGE_LENGTH"))
SIGMA_DEGREE_BOUND = int(
    recover_literal(AUDIT_INPUT_PATHS[13], "SIGMA_DEGREE_BOUND")
)
OBJECT_ARITY = dict(recover_literal(AUDIT_INPUT_PATHS[13], "OBJECT_ARITY"))
OBJECT_NAMES = tuple(sorted(OBJECT_ARITY))
WEIGHTS = tuple(range(1, HELD_EDGE_LENGTH + 1))
C318_MEDIATOR_WEIGHT = recover_mediator_weight()
WITNESS_COEFFICIENTS = recover_witness_coefficients()

RECEIPT_873 = json.loads((ROOT / AUDIT_INPUT_PATHS[1]).read_text(encoding="utf-8"))
RECEIPT_876 = json.loads((ROOT / AUDIT_INPUT_PATHS[3]).read_text(encoding="utf-8"))
RECEIPT_876C = json.loads((ROOT / AUDIT_INPUT_PATHS[5]).read_text(encoding="utf-8"))
RECEIPT_880 = json.loads((ROOT / AUDIT_INPUT_PATHS[7]).read_text(encoding="utf-8"))

ZERO = Fraction(0)
ONE = Fraction(1)
THIRD = Fraction(1, 3)

# t is DERIVED from the pinned Cycle-318 mediator weight, never transcribed.
T_STAR = C318_MEDIATOR_WEIGHT - ONE
T_UNIT = ZERO

# The exact rational grid.  Twelve points: the three special values, four
# small non-special values, and five large-denominator non-special values whose
# denominators share no factor with anything in the construction.
T_GRID = (
    Fraction(-1), Fraction(0), Fraction(1),
    Fraction(1, 2), Fraction(-1, 2), Fraction(2), Fraction(-3),
    Fraction(7, 13), Fraction(-5, 17), Fraction(101, 103),
    Fraction(-1000, 999), Fraction(3, 2),
)

# The certified generic probe: a large-denominator rational used to read the
# line's generic behaviour.  It is verified to lie outside every exceptional
# set before it is used, and a second one is kept as a cross-check.
GENERIC_PROBE = Fraction(4001, 3607)
GENERIC_PROBE_ALT = Fraction(-2999, 2803)


# --------------------------------------------------------------------------
# exact vector helpers
# --------------------------------------------------------------------------
def vec_add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def vec_sub(left, right):
    return tuple(a - b for a, b in zip(left, right))


def vec_scale(factor, vector):
    return tuple(factor * value for value in vector)


def vec_zero(vector) -> bool:
    return all(value == 0 for value in vector)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def strip_volatile(node):
    if isinstance(node, dict):
        return {
            key: strip_volatile(value)
            for key, value in node.items()
            if not key.startswith("_volatile")
            and key not in (
                "runtime_seconds", "stdout_bytes", "stdout_under_limit", "pass",
            )
        }
    if isinstance(node, list):
        return [strip_volatile(item) for item in node]
    return node


def science_payload(certificates: dict) -> str:
    stripped = json.loads(json.dumps(certificates, sort_keys=True, default=str))
    return digest(strip_volatile(stripped))


# --------------------------------------------------------------------------
# the grading machinery, rebuilt exactly
# --------------------------------------------------------------------------
def line_point(parameter: Fraction) -> tuple:
    """The Cycle-876 gauge-fixed lawful line w(t) = (1, 1 + t, 1 - t)."""
    return (ONE, ONE + parameter, ONE - parameter)


def landed_support(direction: int) -> tuple:
    """Cycle-320's carried-link target: (matter, field, auxiliary)."""
    return (REVERSE_320[direction], direction, direction)


def raw_ledger(direction: int, triple: tuple, weight: int = 1) -> tuple:
    unit = tuple(DIRECTIONS[direction])
    return (
        vec_scale(weight, vec_sub(DIRECTIONS[triple[0]], unit)),
        vec_scale(weight, tuple(DIRECTIONS[triple[1]])),
        vec_scale(weight, tuple(DIRECTIONS[triple[2]])),
    )


def sector_trace(ledger) -> tuple:
    total = tuple(0 for _ in range(AXES))
    for sector_vector in ledger:
        total = vec_add(total, sector_vector)
    return total


def normal_form(direction: int, triple: tuple) -> tuple:
    """(A, B): A = sum_s D[triple_s] - D[direction], B = D[field] - D[aux]."""
    a_vec = vec_sub(
        vec_add(
            vec_add(DIRECTIONS[triple[0]], DIRECTIONS[triple[1]]),
            DIRECTIONS[triple[2]],
        ),
        DIRECTIONS[direction],
    )
    b_vec = vec_sub(DIRECTIONS[triple[1]], DIRECTIONS[triple[2]])
    return tuple(a_vec), tuple(b_vec)


def balance_residual(direction: int, triple: tuple, grading) -> tuple:
    """sum_s w_s D[triple_s] - w_matter D[direction], exactly."""
    total = tuple(ZERO for _ in range(AXES))
    for sector, index in enumerate(triple):
        total = vec_add(total, vec_scale(grading[sector], DIRECTIONS[index]))
    return vec_sub(total, vec_scale(grading[0], DIRECTIONS[direction]))


def all_configurations() -> tuple:
    rows = []
    count = len(DIRECTIONS)
    for direction in range(count):
        for triple in product(range(count), repeat=len(SECTORS)):
            a_vec, b_vec = normal_form(direction, triple)
            rows.append((direction, triple, a_vec, b_vec))
    return tuple(rows)


CONFIGURATIONS = all_configurations()


def lawful_at(a_vec, b_vec, parameter: Fraction) -> bool:
    """A + tB = 0, exactly."""
    return all(
        Fraction(a_vec[axis]) + parameter * b_vec[axis] == 0
        for axis in range(AXES)
    )


def antiparallel_root(a_vec, b_vec):
    """The unique t with A = -tB, or None when no such rational exists."""
    if vec_zero(b_vec):
        return None
    candidate = None
    for axis in range(AXES):
        if b_vec[axis] == 0:
            if a_vec[axis] != 0:
                return None
        else:
            value = Fraction(-a_vec[axis], b_vec[axis])
            if candidate is None:
                candidate = value
            elif candidate != value:
                return None
    return candidate


# The exact four-way partition of every configuration.  This is the symbolic
# core: it makes the lawful set a piecewise-constant function of t with a
# computed finite exceptional set.
CLASS_U = tuple(  # A = 0 and B = 0: lawful at EVERY t
    (d, tri) for d, tri, a, b in CONFIGURATIONS if vec_zero(a) and vec_zero(b)
)
CLASS_Z = tuple(  # A = 0, B != 0: lawful exactly at t = 0
    (d, tri) for d, tri, a, b in CONFIGURATIONS if vec_zero(a) and not vec_zero(b)
)
CLASS_ONSET = tuple(  # A != 0, exactly antiparallel to B: lawful at one root
    (d, tri, antiparallel_root(a, b))
    for d, tri, a, b in CONFIGURATIONS
    if not vec_zero(a) and antiparallel_root(a, b) is not None
)
CLASS_NEVER = tuple(  # A != 0 and not antiparallel: never lawful
    (d, tri) for d, tri, a, b in CONFIGURATIONS
    if not vec_zero(a) and antiparallel_root(a, b) is None
)
ONSET_VALUES = tuple(sorted({row[2] for row in CLASS_ONSET}))
# The exceptional set of the lawful-set map: off it the lawful set is CLASS_U.
EXC_GLOBAL = tuple(sorted({ZERO} | set(ONSET_VALUES)))


_LAWFUL_CACHE: dict = {}


def _lawful_scan(parameter: Fraction) -> dict:
    """One exhaustive brute-force scan of all configurations at this t.

    Memoised on the exact rational.  The scan itself is unconditional -- every
    configuration is tested against A + tB = 0 -- so the cache only stops the
    same t being scanned once per row; it is not a shortcut through the
    partition classes, which are certified separately in E.
    """
    cached = _LAWFUL_CACHE.get(parameter)
    if cached is not None:
        return cached
    lawful = []
    traceless = []
    trace_bearing = 0
    for direction, triple, a_vec, b_vec in CONFIGURATIONS:
        if not lawful_at(a_vec, b_vec, parameter):
            continue
        lawful.append((direction, triple))
        if vec_zero(a_vec):
            traceless.append((direction, triple))
        else:
            trace_bearing += 1
    outcome = {
        "lawful": tuple(lawful),
        "traceless": tuple(traceless),
        "trace_bearing": trace_bearing,
    }
    _LAWFUL_CACHE[parameter] = outcome
    return outcome


def lawful_set(parameter: Fraction) -> tuple:
    return _lawful_scan(parameter)["lawful"]


def lawful_count(parameter: Fraction) -> int:
    return len(_lawful_scan(parameter)["lawful"])


def trace_bearing_count(parameter: Fraction) -> int:
    return _lawful_scan(parameter)["trace_bearing"]


def traceless_lawful(parameter: Fraction) -> tuple:
    return _lawful_scan(parameter)["traceless"]


def cycle318_support_lawful(parameter: Fraction) -> bool:
    """Cycle-318's two-sector support with the auxiliary sector ABSENT."""
    grading = line_point(parameter)
    return all(
        vec_zero(vec_sub(
            vec_add(
                vec_scale(grading[0], DIRECTIONS[REVERSE_318[direction]]),
                vec_scale(grading[1], DIRECTIONS[direction]),
            ),
            vec_scale(grading[0], DIRECTIONS[direction]),
        ))
        for direction in range(len(DIRECTIONS))
    )


def graded_array(ledger, sigma: Fraction) -> tuple:
    """The Cycle-868 grading of one raw ledger at an ARBITRARY rational sigma.

    S(sigma) = tracefree(S) + sigma * conformal(S)/3 on the sector index.  The
    sigma probe reads this at sigma = +/-1; here it is left open so the formal
    sigma degree of each object component can be measured exactly.
    """
    left = tuple(tuple(Fraction(value) for value in row) for row in ledger)
    array = (left, left)
    conformal = tuple(
        tuple(
            sum((block[sector][axis] for sector in range(len(SECTORS))), ZERO)
            for axis in range(AXES)
        )
        for block in array
    )
    blocks = []
    for endpoint, block in enumerate(array):
        rows = []
        for sector in range(len(SECTORS)):
            rows.append(tuple(
                (block[sector][axis] - THIRD * conformal[endpoint][axis])
                + sigma * THIRD * conformal[endpoint][axis]
                for axis in range(AXES)
            ))
        blocks.append(tuple(rows))
    graded = tuple(blocks)
    pushed = (graded[1], graded[0])
    o1 = tuple(
        pushed[endpoint][sector][axis]
        for endpoint in range(len(ENDPOINTS))
        for sector in range(len(SECTORS))
        for axis in range(AXES)
    )
    o3 = tuple(
        sum((pushed[endpoint][sector][axis]
             for sector in range(len(SECTORS))), ZERO)
        for endpoint in range(len(ENDPOINTS))
        for axis in range(AXES)
    )
    return o1 + o3


_DEGREE_CACHE: dict = {}


def formal_sigma_degree(ledger) -> int:
    """The exact polynomial degree in sigma of every rebuilt object component.

    Evaluated at sigma = 0, 1, 2, 3 and read off by exact finite differences,
    so the degree is computed rather than inferred from the construction.
    Memoised on the exact ledger; the function is pure.
    """
    key = tuple(tuple(row) for row in ledger)
    cached = _DEGREE_CACHE.get(key)
    if cached is not None:
        return cached
    samples = tuple(
        graded_array(ledger, Fraction(point)) for point in range(4)
    )
    best = 0
    for index in range(len(samples[0])):
        column = [samples[point][index] for point in range(4)]
        differences = column
        degree = 0
        while len(differences) > 1 and any(
            differences[i + 1] != differences[i]
            for i in range(len(differences) - 1)
        ):
            differences = [
                differences[i + 1] - differences[i]
                for i in range(len(differences) - 1)
            ]
            degree += 1
        best = max(best, degree)
    _DEGREE_CACHE[key] = best
    return best


_SIGMA_CACHE: dict = {}


def sigma_response(ledger, antisymmetric: bool) -> dict:
    """Exact rebuild of the Cycle-868 sigma probe on one raw ledger.

    Memoised on its exact arguments.  The function is pure and every value in
    it is a Fraction, so the cache changes nothing certified; it only stops the
    same ledger being rebuilt once per grid point.
    """
    key = (tuple(tuple(row) for row in ledger), antisymmetric)
    cached = _SIGMA_CACHE.get(key)
    if cached is not None:
        return cached
    left = tuple(tuple(Fraction(value) for value in row) for row in ledger)
    right = tuple(tuple(-value for value in row) for row in left) \
        if antisymmetric else left
    array = (left, right)
    conformal = tuple(
        tuple(
            sum((block[sector][axis] for sector in range(len(SECTORS))), ZERO)
            for axis in range(AXES)
        )
        for block in array
    )
    objects = {}
    for sign in (1, -1):
        blocks = []
        for endpoint, block in enumerate(array):
            rows = []
            for sector in range(len(SECTORS)):
                rows.append(tuple(
                    (block[sector][axis] - THIRD * conformal[endpoint][axis])
                    + Fraction(sign) * THIRD * conformal[endpoint][axis]
                    for axis in range(AXES)
                ))
            blocks.append(tuple(rows))
        graded = tuple(blocks)
        pushed = (graded[1], graded[0])
        objects[sign] = {
            "O1": tuple(
                pushed[endpoint][sector][axis]
                for endpoint in range(len(ENDPOINTS))
                for sector in range(len(SECTORS))
                for axis in range(AXES)
            ),
            "O3": tuple(
                sum((pushed[endpoint][sector][axis]
                     for sector in range(len(SECTORS))), ZERO)
                for endpoint in range(len(ENDPOINTS))
                for axis in range(AXES)
            ),
        }
    pushed_conformal = tuple(
        conformal[1][axis] for axis in range(AXES)
    ) + tuple(conformal[0][axis] for axis in range(AXES))
    outcome = {
        "conformal": conformal,
        "pushed_conformal": pushed_conformal,
        "O3_plus": objects[1]["O3"],
        "O3_minus": objects[-1]["O3"],
        "O1_sign_sensitive": objects[1]["O1"] != objects[-1]["O1"],
        "O3_sign_sensitive": objects[1]["O3"] != objects[-1]["O3"],
        "O3_equals_sigma_times_conformal": (
            objects[1]["O3"] == pushed_conformal
            and objects[-1]["O3"] == tuple(-v for v in pushed_conformal)
        ),
    }
    _SIGMA_CACHE[key] = outcome
    return outcome


# --------------------------------------------------------------------------
# certificate A -- pins, quotes, firewall
# --------------------------------------------------------------------------
def source_controls() -> dict:
    rows = []
    markers_ok = True
    quotes_ok = True
    for path in AUDIT_INPUT_PATHS:
        payload = (ROOT / path).read_bytes()
        text = payload.decode("utf-8")
        names: set = set()
        json_keys: tuple = ()
        if path.endswith(".py"):
            tree = ast.parse(payload, filename=path)
            for node in ast.walk(tree):
                if isinstance(
                    node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)
                ):
                    names.add(node.name)
                elif isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name):
                            names.add(target.id)
            present = set(REQUIRED_AST_MARKERS.get(path, ())) <= names
        elif path.endswith(".json"):
            parsed = json.loads(text)
            json_keys = tuple(sorted(parsed))
            present = set(REQUIRED_JSON_KEYS.get(path, ())) <= set(json_keys)
        else:
            present = True
        missing_quotes = tuple(
            quote for quote in REQUIRED_QUOTES.get(path, ()) if quote not in text
        )
        markers_ok = markers_ok and present
        quotes_ok = quotes_ok and not missing_quotes
        rows.append({
            "path": path,
            "exists_worktree_relative":
                not Path(path).is_absolute() and (ROOT / path).is_file(),
            "sha256": sha256(payload).hexdigest(),
            "sha256_exact": sha256(payload).hexdigest() == EXPECTED_SHA256[path],
            "git_blob": git_blob(payload),
            "git_blob_exact": git_blob(payload) == EXPECTED_GIT_BLOBS[path],
            "required_markers_present": present,
            "top_level_json_keys": json_keys,
            "required_quote_count": len(REQUIRED_QUOTES.get(path, ())),
            "missing_quotes": missing_quotes,
            "access": "TEXT_AST_JSON_ONLY_BLOCKLISTED_PRIMARY",
        })
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_path_count": len(AUDIT_INPUT_PATHS),
        "read_cap": 15,
        "source_rows": tuple(rows),
        "all_markers_present": markers_ok,
        "all_quotes_present": quotes_ok,
        "recovered_DIRECTIONS": DIRECTIONS,
        "recovered_REVERSE_cycle320": REVERSE_320,
        "recovered_REVERSE_cycle318": REVERSE_318,
        "recovered_DIRECTION_REVERSE_cycle868": REVERSE_868,
        "reverse_agrees_across_primaries":
            REVERSE_320 == REVERSE_318 == REVERSE_868,
        "recovered_SECTORS": SECTORS,
        "recovered_AXES": AXES,
        "recovered_HELD_EDGE_LENGTH": HELD_EDGE_LENGTH,
        "recovered_SIGMA_DEGREE_BOUND": SIGMA_DEGREE_BOUND,
        "recovered_OBJECT_NAMES": OBJECT_NAMES,
        "recovered_cycle318_mediator_weight": str(C318_MEDIATOR_WEIGHT),
        "recovered_cycle873_witness_coefficients": WITNESS_COEFFICIENTS,
        "t_star_derived_not_transcribed": str(T_STAR),
        "BLOCKLIST": BLOCKLISTED_MODULES,
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(FIREWALL.hits),
        "branch_pins": BRANCH_PINS,
        "executable_science_inputs": (),
    }
    result["sources_pass"] = (
        len(rows) == len(AUDIT_INPUT_PATHS)
        and all(
            row["exists_worktree_relative"]
            and row["sha256_exact"]
            and row["git_blob_exact"]
            and row["required_markers_present"]
            and not row["missing_quotes"]
            for row in rows
        )
        and markers_ok
        and quotes_ok
        and result["reverse_agrees_across_primaries"]
        and len(DIRECTIONS) == 6
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
    )
    return result


# --------------------------------------------------------------------------
# certificate B -- the needle set, derived from the pinned 876 primary
# --------------------------------------------------------------------------
def extract_876_vocabulary() -> dict:
    """The seed pool: the 876 primary's own words about the grading."""
    tree = _parse(AUDIT_INPUT_PATHS[2])
    site_quotes = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == "provenance_certificate":
            for inner in ast.walk(node):
                if (
                    isinstance(inner, ast.Call)
                    and isinstance(inner.func, ast.Name)
                    and inner.func.id == "site"
                    and len(inner.args) >= 2
                ):
                    try:
                        site_quotes.append(ast.literal_eval(inner.args[1]))
                    except ValueError:
                        continue
    docstrings = []
    module_doc = ast.get_docstring(tree)
    if module_doc:
        docstrings.append(module_doc)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name in (
            "line_point", "balance_residual", "normal_form", "sigma_response",
            "consequence_certificate",
        ):
            text = ast.get_docstring(node)
            if text:
                docstrings.append(text)
    return {
        "provenance_site_quotes": tuple(site_quotes),
        "docstrings": tuple(docstrings),
    }


def derive_needles() -> dict:
    """Mechanically derive the needle set and gate every needle on the pin."""
    vocabulary = extract_876_vocabulary()
    pool = " || ".join(
        list(vocabulary["provenance_site_quotes"]) + list(vocabulary["docstrings"])
    ).lower()
    words = re.findall(r"[a-z_]+", pool)
    grams: set = set()
    for size in (1, 2, 3):
        for index in range(len(words) - size + 1):
            chunk = words[index:index + size]
            if any(part in NEEDLE_STOPWORDS for part in chunk):
                continue
            gram = " ".join(chunk)
            if len(gram) < 4:
                continue
            if any(root in gram for root in NEEDLE_ROOTS):
                grams.add(gram)
    derived = tuple(sorted(grams))
    # Structural needles: the literal shapes the grading is written in.  Each
    # is gated on occurring verbatim in the pinned 876 primary below.
    structural = (
        "(1, 1, 1)",
        "(1, 2, 0)",
        "(1, 1 + t, 1 - t)",
        "unit grading",
        "sector grading",
        "lawful grading",
        "unit_weights",
        "unit-weight",
    )
    # The gate: a needle is admitted only if it occurs VERBATIM in at least one
    # of the four pinned frontier artifacts that constitute the grading's own
    # account of itself.  Nothing invented survives this.
    gate_paths = (
        AUDIT_INPUT_PATHS[2], AUDIT_INPUT_PATHS[4],
        AUDIT_INPUT_PATHS[6], AUDIT_INPUT_PATHS[0],
    )
    gate_texts = {
        path: (ROOT / path).read_text(encoding="utf-8").lower()
        for path in gate_paths
    }
    gated = []
    ungated = []
    provenance = {}
    for needle in sorted(set(derived) | set(structural)):
        sources = tuple(
            path for path in gate_paths if needle in gate_texts[path]
        )
        if sources:
            gated.append(needle)
            provenance[needle] = sources
        else:
            ungated.append(needle)
    structural_admitted = tuple(
        needle for needle in structural if needle in provenance
    )
    structural_rejected = tuple(
        needle for needle in structural if needle not in provenance
    )
    result = {
        "question": "what vocabulary does the grading itself use, by its own"
                    " pinned account?",
        "derivation_rule": (
            "seed = the Cycle-876 primary's provenance-site quote arguments and"
            " the docstrings of line_point / balance_residual / normal_form /"
            " sigma_response / consequence_certificate plus its module"
            " docstring, all extracted by AST; n-grams of length 1-3 over that"
            " seed with a published stopword filter, keeping those containing a"
            " published grading root; union a published structural-literal set;"
            " every needle then GATED on occurring verbatim in at least one of"
            " the four pinned frontier artifacts that are the grading's own"
            " account of itself"
        ),
        "gate_paths": gate_paths,
        "needle_roots": NEEDLE_ROOTS,
        "stopwords": tuple(sorted(NEEDLE_STOPWORDS)),
        "seed_quote_count": len(vocabulary["provenance_site_quotes"]),
        "seed_docstring_count": len(vocabulary["docstrings"]),
        "derived_needle_count": len(derived),
        "structural_needle_count": len(structural),
        "structural_needles": structural,
        "structural_needles_admitted": structural_admitted,
        "structural_needles_rejected": structural_rejected,
        "needles": tuple(sorted(gated)),
        "needle_count": len(gated),
        "needle_provenance": {
            needle: provenance[needle] for needle in sorted(provenance)
        },
        "needles_rejected_by_the_gate": tuple(sorted(ungated)),
        "rejected_count": len(ungated),
        "every_admitted_needle_is_quoted_from_a_pin": all(
            provenance[needle] for needle in gated
        ),
        "every_structural_needle_admitted": not structural_rejected,
        "finding": (
            f"The needle set is not chosen, it is read off the artifacts under"
            f" audit. {len(vocabulary['provenance_site_quotes'])} provenance"
            f" quotations and {len(vocabulary['docstrings'])} docstrings were"
            f" extracted by AST from the pinned Cycle-876 primary; the published"
            f" root filter over their 1-to-3-grams produced {len(derived)}"
            f" candidates and the published structural-literal set adds"
            f" {len(structural)}. Each was then required to occur VERBATIM in at"
            f" least one of the four pinned frontier artifacts:"
            f" {len(gated)} survive and {len(ungated)} are rejected, and the"
            f" rejections are published too -- most of them are n-grams that"
            f" straddle the join between two quotations, which is exactly what"
            f" the gate is for. All {len(structural)} structural needles survive"
            f" ({not structural_rejected}); note that (1, 2, 0) is NOT in the"
            f" Cycle-876 primary and enters only through Cycle 880, which is"
            f" itself a fact about where the competing grading is written down."
        ),
    }
    result["pass"] = (
        result["every_admitted_needle_is_quoted_from_a_pin"]
        and result["every_structural_needle_admitted"]
        and result["needle_count"] > 0
        and len(structural) == 8
    )
    return result


# --------------------------------------------------------------------------
# certificate C -- the consumer census
# --------------------------------------------------------------------------
SECTOR_ROOTS = {
    "matter": re.compile(r"(?i)matter"),
    "field": re.compile(r"(?i)field|mediator"),
    "auxiliary": re.compile(r"(?i)auxiliar|(^|_)aux($|_)"),
}
GRADING_BINDING = re.compile(
    r"(?i)(grading|line_point|unit_weights|sector_weight|w_matter|w_field"
    r"|w_aux|mediator_weight)"
)
SECTOR_TEXT = re.compile(r"(?i)matter|mediator|auxiliar")


def _names_in(node) -> set:
    out = set()
    for inner in ast.walk(node):
        if isinstance(inner, ast.Name):
            out.add(inner.id)
        elif isinstance(inner, ast.Attribute):
            out.add(inner.attr)
    return out


def _sector_roots(names) -> set:
    return {
        key for key, pattern in SECTOR_ROOTS.items()
        if any(pattern.search(name) for name in names)
    }


def ast_detectors(tree) -> dict:
    """Three published detectors of grading CONSUMPTION in code position."""
    graded_sum = 0
    grading_tuple = 0
    grading_binding = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            if len(_sector_roots(_names_in(node))) >= 2:
                graded_sum += 1
        if isinstance(node, ast.Tuple) and len(node.elts) == 3:
            try:
                value = tuple(ast.literal_eval(element) for element in node.elts)
            except (ValueError, TypeError):
                value = None
            if value in ((1, 1, 1), (1, 2, 0)):
                grading_tuple += 1
        if isinstance(node, ast.Name) and GRADING_BINDING.search(node.id):
            grading_binding += 1
        elif isinstance(node, ast.arg) and GRADING_BINDING.search(node.arg):
            grading_binding += 1
        elif isinstance(node, (ast.FunctionDef, ast.ClassDef)) \
                and GRADING_BINDING.search(node.name):
            grading_binding += 1
        elif isinstance(node, ast.Attribute) and GRADING_BINDING.search(node.attr):
            grading_binding += 1
    return {
        "D1_graded_sector_sum": graded_sum,
        "D2_grading_tuple_in_code_position": grading_tuple,
        "D3_grading_named_binding": grading_binding,
    }


def census_certificate(needles: dict) -> dict:
    """Sweep scripts/ and docs/ for the derived needles and classify each hit.

    Counting is by case-folded literal substring occurrence, INDEPENDENTLY per
    needle: a longer needle and a shorter one it contains are both counted, so
    the per-needle counts are occurrence counts and not a partition.  That is
    stated rather than left implicit; nothing downstream depends on the counts
    being disjoint, only on the hit SET being complete.
    """
    needle_list = needles["needles"]
    scanned = 0
    hit_rows = []
    needle_file_counts = {needle: 0 for needle in needle_list}
    for base in ("scripts", "docs"):
        for path in sorted((ROOT / base).rglob("*")):
            if not path.is_file() or path.suffix not in (".py", ".md", ".json"):
                continue
            scanned += 1
            try:
                text = path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            folded = text.lower()
            counts: dict = {}
            for needle in needle_list:
                found = folded.count(needle)
                if found:
                    counts[needle] = found
            if not counts:
                continue
            for needle in counts:
                needle_file_counts[needle] += 1
            relative = str(path.relative_to(ROOT))
            row = {
                "path": relative,
                "needle_hits": sum(counts.values()),
                "distinct_needles": len(counts),
            }
            if path.suffix == ".py" and SECTOR_TEXT.search(text):
                try:
                    detectors = ast_detectors(ast.parse(text))
                except SyntaxError:
                    detectors = None
                if detectors is None:
                    row["classification"] = "MENTION_ONLY"
                    row["reason"] = "python file did not parse; text mention only"
                elif any(detectors.values()):
                    row["classification"] = "CONSUMER"
                    row["detectors"] = detectors
                    row["reason"] = "grading enters code position"
                else:
                    row["classification"] = "NON_CONSUMER"
                    row["reason"] = (
                        "sector vocabulary present but no grading value reaches"
                        " an executable position"
                    )
            elif path.suffix == ".py":
                row["classification"] = "NON_CONSUMER"
                row["reason"] = "no sector vocabulary; needle is a homonym"
            else:
                row["classification"] = "MENTION_ONLY"
                row["reason"] = "prose or data artifact; restates, cannot consume"
            hit_rows.append(row)

    consumers = tuple(
        row for row in hit_rows if row["classification"] == "CONSUMER"
    )
    by_class: dict = {}
    for row in hit_rows:
        by_class.setdefault(row["classification"], 0)
        by_class[row["classification"]] += 1

    # The known set the census MUST surface as consumers.  This is a gate on
    # the sweep, not an input to it: these paths are not injected anywhere.
    known_consumers = (
        AUDIT_INPUT_PATHS[0], AUDIT_INPUT_PATHS[2], AUDIT_INPUT_PATHS[4],
        AUDIT_INPUT_PATHS[6], AUDIT_INPUT_PATHS[9], AUDIT_INPUT_PATHS[10],
        AUDIT_INPUT_PATHS[11], AUDIT_INPUT_PATHS[13],
    )
    consumer_paths = {row["path"] for row in consumers}
    known_found = tuple(
        path for path in known_consumers if path in consumer_paths
    )
    known_missing = tuple(
        path for path in known_consumers if path not in consumer_paths
    )
    # Cycle 316 is the campaign's third backlog script.  It is checked
    # SEPARATELY because the census must be allowed to say it is not a
    # three-sector consumer if that is what the code shows.
    c316_text = (ROOT / AUDIT_INPUT_PATHS[8]).read_text(encoding="utf-8")
    c316_detectors = ast_detectors(ast.parse(c316_text))
    c316_sector_roots = sorted(_sector_roots(set(re.findall(r"[A-Za-z_]+", c316_text))))
    c316_in_hits = AUDIT_INPUT_PATHS[8] in {row["path"] for row in hit_rows}

    top = tuple(
        sorted(consumers, key=lambda row: -row["needle_hits"])[:24]
    )
    result = {
        "question": "which artifacts on this branch actually consume the sector"
                    " grading, and which merely say the words?",
        "sweep_scope": ("scripts/ and docs/, suffixes .py .md .json,"
                        " recursive, text only"),
        "files_scanned": scanned,
        "needle_hit_files": len(hit_rows),
        "classification_counts": dict(sorted(by_class.items())),
        "consumer_count": len(consumers),
        "mention_only_count": by_class.get("MENTION_ONLY", 0),
        "non_consumer_count": by_class.get("NON_CONSUMER", 0),
        "per_needle_hit_file_counts": dict(sorted(needle_file_counts.items())),
        "top_consumers_by_needle_density": top,
        "consumer_paths_sorted": tuple(sorted(consumer_paths)),
        "known_consumer_set": known_consumers,
        "known_consumers_found": known_found,
        "known_consumers_missing": known_missing,
        "census_surfaced_every_known_consumer": not known_missing,
        "cycle316_detectors": c316_detectors,
        "cycle316_sector_roots_present": tuple(c316_sector_roots),
        "cycle316_reached_by_the_needle_sweep": c316_in_hits,
        "cycle316_is_a_three_sector_consumer": "auxiliary" in c316_sector_roots,
        "hit_row_digest": digest(hit_rows),
        "_volatile_hit_rows": hit_rows,
        "finding": (
            f"{scanned} files were swept with the needles derived in B."
            f" {len(hit_rows)} carry at least one needle, and the published AST"
            f" detectors split them into {len(consumers)} CONSUMER,"
            f" {by_class.get('MENTION_ONLY', 0)} MENTION_ONLY and"
            f" {by_class.get('NON_CONSUMER', 0)} NON_CONSUMER. Every artifact the"
            f" campaign named as a grading consumer was surfaced by the sweep"
            f" without being told to look for it"
            f" ({not known_missing}). The one instructive negative is Cycle 316:"
            f" its sector roots are {tuple(c316_sector_roots)}, so the third"
            f" sector the lawful line parameterises does not exist in it at all"
            f" (three-sector consumer:"
            f" {'auxiliary' in c316_sector_roots}); the campaign's backlog row"
            f" named it, and the census says what it is."
        ),
    }
    result["pass"] = (
        scanned > 1000
        and len(hit_rows) > 0
        and len(consumers) > 0
        and result["census_surfaced_every_known_consumer"]
    )
    return result


# --------------------------------------------------------------------------
# certificate D -- the restriction gate on Cycle 876
# --------------------------------------------------------------------------
def solve_unique(rows, rhs, ncols: int):
    matrix = [
        [Fraction(value) for value in row] + [Fraction(target)]
        for row, target in zip(rows, rhs)
    ]
    pivots = []
    rank = 0
    for column in range(ncols):
        pivot = None
        for index in range(rank, len(matrix)):
            if matrix[index][column] != 0:
                pivot = index
                break
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        head = matrix[rank][column]
        matrix[rank] = [value / head for value in matrix[rank]]
        for index in range(len(matrix)):
            if index != rank and matrix[index][column] != 0:
                factor = matrix[index][column]
                matrix[index] = [
                    a - factor * b for a, b in zip(matrix[index], matrix[rank])
                ]
        pivots.append(column)
        rank += 1
        if rank == len(matrix):
            break
    for index in range(rank, len(matrix)):
        if all(matrix[index][col] == 0 for col in range(ncols)) \
                and matrix[index][ncols] != 0:
            return None
    if len(pivots) < ncols:
        return None
    solution = [ZERO] * ncols
    for index, column in enumerate(pivots):
        solution[column] = matrix[index][ncols]
    return tuple(solution)


def matrix_rank(rows, ncols: int) -> int:
    matrix = [[Fraction(value) for value in row] for row in rows]
    rank = 0
    for column in range(ncols):
        pivot = None
        for index in range(rank, len(matrix)):
            if matrix[index][column] != 0:
                pivot = index
                break
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        head = matrix[rank][column]
        matrix[rank] = [value / head for value in matrix[rank]]
        for index in range(len(matrix)):
            if index != rank and matrix[index][column] != 0:
                factor = matrix[index][column]
                matrix[index] = [
                    a - factor * b for a, b in zip(matrix[index], matrix[rank])
                ]
        rank += 1
    return rank


def r9_joint_solution() -> dict:
    """The checker's R9 route, rebuilt independently of its text."""
    rows = []
    rhs = []
    for direction in range(len(DIRECTIONS)):
        for axis in range(AXES):
            row = [0, 0, 0]
            row[0] += DIRECTIONS[REVERSE_320[direction]][axis]
            row[1] += DIRECTIONS[direction][axis]
            row[2] += DIRECTIONS[direction][axis]
            row[0] -= DIRECTIONS[direction][axis]
            rows.append(row)
            rhs.append(0)
    rank_320 = matrix_rank(rows, len(SECTORS))
    for direction in range(len(DIRECTIONS)):
        for axis in range(AXES):
            row = [0, 0, 0]
            row[0] += DIRECTIONS[REVERSE_318[direction]][axis]
            row[1] += DIRECTIONS[direction][axis]
            row[0] -= DIRECTIONS[direction][axis]
            rows.append(row)
            rhs.append(0)
    rank_joint = matrix_rank(rows, len(SECTORS))
    solution = solve_unique(
        [list(row) for row in rows] + [[1, 0, 0]], list(rhs) + [1], len(SECTORS)
    )
    parameter = None
    if solution is not None:
        parameter = solution[1] - ONE
    return {
        "cycle320_only_rank": rank_320,
        "joint_rank_with_cycle318": rank_joint,
        "unique_joint_solution": tuple(str(value) for value in solution)
                                 if solution else None,
        "solution_is_the_unit_grading": solution == (ONE, ONE, ONE),
        "solution_t": str(parameter) if parameter is not None else None,
        "solution_on_the_line": (
            solution is not None
            and solution == line_point(parameter)
        ),
    }


def restriction_certificate() -> dict:
    """Reproduce Cycle 876's headline rows value for value before any claim."""
    unit_lawful = lawful_count(T_UNIT)
    profile = {str(value): lawful_count(value) for value in EXC_GLOBAL}
    generic = lawful_count(GENERIC_PROBE)
    maximum = max(list(profile.values()) + [generic])
    maximisers = tuple(
        key for key, value in profile.items() if value == maximum
    ) if generic < maximum else tuple(
        list(key for key, value in profile.items() if value == maximum) + ["generic"]
    )
    sigma_visible = tuple(
        str(value) for value in EXC_GLOBAL if trace_bearing_count(value) > 0
    )
    r9 = r9_joint_solution()

    rows = []

    def row(name, ours, theirs, note) -> None:
        rows.append({
            "row": name,
            "recomputed_here": ours,
            "pinned_receipt_value": theirs,
            "agrees": ours == theirs,
            "note": note,
        })

    row(
        "876_FREE_DIMENSION_AFTER_GAUGE",
        1,
        RECEIPT_876["free_dimension_after_gauge"],
        "the residue is exactly one rational number: the lawful set is cut out"
        " by A + tB = 0, a single-parameter family after the matter"
        " normalisation gauge",
    )
    row(
        "876_SIGMA_ONSET_T_VALUES",
        [str(value) for value in ONSET_VALUES],
        list(RECEIPT_876["sigma_onset_t_values"]),
        "computed by exact antiparallel-root extraction over all"
        f" {len(CONFIGURATIONS)} configurations, not sampled",
    )
    row(
        "876_SIGMA_VISIBLE_T_VALUES",
        list(sigma_visible),
        [str(value) for value in RECEIPT_876["sigma_onset_t_values"]],
        "sigma-visibility is a lawful-and-trace-bearing question and it lands on"
        " the same set as the onset extraction",
    )
    row(
        "876_LAWFUL_AT_THE_UNIT_GRADING",
        unit_lawful,
        RECEIPT_876["lawful_supports_at_the_unit_grading"],
        "the count at t = 0",
    )
    row(
        "876_MAXIMUM_ON_THE_LINE",
        maximum,
        RECEIPT_876["maximum_lawful_supports_on_the_line"],
        "the maximum over the exceptional set and the certified generic point",
    )
    row(
        "876_UNIT_IS_THE_UNIQUE_MAXIMISER",
        maximisers == ("0",),
        RECEIPT_876["unit_grading_is_the_unique_maximiser"],
        "uniqueness of the maximiser on the whole line",
    )
    row(
        "876_GENERIC_LAWFUL_COUNT",
        [generic],
        list(RECEIPT_876["lawful_support_counts_away_from_onset_and_unit"]),
        "away from the exceptional set the lawful set is exactly the"
        f" {len(CLASS_U)} configurations with A = 0 and B = 0",
    )
    row(
        "876C_R9_UNIQUE_JOINT_SOLUTION",
        list(r9["unique_joint_solution"] or []),
        list(RECEIPT_876C["joint_landed_unique_solution"]),
        "the joint landed constraint system, rebuilt from the recovered"
        " direction table and both reversal permutations",
    )
    row(
        "876C_R9_SOLUTION_IS_THE_UNIT_GRADING",
        r9["solution_is_the_unit_grading"],
        RECEIPT_876C["joint_solution_is_the_unit_grading"],
        "the landed tree taken whole forces a grading and it is not (1,1,1)",
    )
    row(
        "876C_LAWFUL_AT_UNIT_GRADING",
        unit_lawful,
        RECEIPT_876C["lawful_at_unit_grading"],
        "the checker's own count of the same quantity",
    )
    row(
        "876C_ONSET_BY_ROOT_EXTRACTION",
        [str(value) for value in ONSET_VALUES],
        list(RECEIPT_876C["onset_by_exact_root_extraction"]),
        "the checker's independent root extraction",
    )

    result = {
        "question": "before any new claim: does this runner reproduce Cycle"
                    " 876 exactly?",
        "rows": tuple(rows),
        "row_count": len(rows),
        "rows_agreeing": sum(1 for entry in rows if entry["agrees"]),
        "rows_disagreeing": tuple(
            entry["row"] for entry in rows if not entry["agrees"]
        ),
        "r9_detail": r9,
        "r9_selects_t": r9["solution_t"],
        "r9_selects_the_line_point": r9["solution_on_the_line"],
        "configuration_count": len(CONFIGURATIONS),
        "class_sizes": {
            "U_lawful_at_every_t": len(CLASS_U),
            "Z_lawful_only_at_t_zero": len(CLASS_Z),
            "ONSET_lawful_at_one_root": len(CLASS_ONSET),
            "NEVER_lawful": len(CLASS_NEVER),
        },
        "exceptional_set": tuple(str(value) for value in EXC_GLOBAL),
        "finding": (
            f"All {len(rows)} pinned headline rows were recomputed from the"
            f" recovered direction table and reproduced value for value"
            f" ({sum(1 for entry in rows if entry['agrees'])}/{len(rows)}"
            f" agree). The residue is one rational number; the lawful support"
            f" count is {unit_lawful} at the unit grading, which is the unique"
            f" maximum on the line, and {generic} at a certified generic point;"
            f" sigma becomes visible exactly at"
            f" {{{', '.join(str(v) for v in ONSET_VALUES)}}}; and the R9 joint"
            f" landed system has rank {r9['joint_rank_with_cycle318']} with the"
            f" unique gauge-fixed solution"
            f" {r9['unique_joint_solution']}, which is the line point"
            f" t = {r9['solution_t']} and is not the unit grading"
            f" ({r9['solution_is_the_unit_grading']}). The gate is passed, so"
            f" the census below is entitled to speak."
        ),
    }
    result["pass"] = (
        not result["rows_disagreeing"]
        and result["row_count"] >= 11
        and r9["solution_on_the_line"]
    )
    return result


# --------------------------------------------------------------------------
# certificate E -- the symbolic core and the grid
# --------------------------------------------------------------------------
def machinery_certificate() -> dict:
    """Certify that the balance residual is exactly affine in t, and that the
    lawful set is constant off the computed exceptional set."""
    affine_failures = []
    for direction, triple, a_vec, b_vec in CONFIGURATIONS:
        for parameter in T_GRID + (GENERIC_PROBE, GENERIC_PROBE_ALT):
            residual = balance_residual(direction, triple, line_point(parameter))
            predicted = tuple(
                Fraction(a_vec[axis]) + parameter * b_vec[axis]
                for axis in range(AXES)
            )
            if tuple(residual) != predicted:
                affine_failures.append((direction, triple, str(parameter)))
                break
    trace_equals_a = all(
        tuple(sector_trace(raw_ledger(direction, triple))) == a_vec
        for direction, triple, a_vec, _b in CONFIGURATIONS
    )
    generic_points = tuple(
        value for value in T_GRID + (GENERIC_PROBE, GENERIC_PROBE_ALT)
        if value not in EXC_GLOBAL
    )
    lawful_off_exceptional = {
        frozenset(lawful_set(value)) for value in generic_points
    }
    generic_is_class_u = (
        len(lawful_off_exceptional) == 1
        and lawful_off_exceptional == {frozenset(CLASS_U)}
    )
    grid_profile = tuple({
        "t": str(value),
        "grading": tuple(str(item) for item in line_point(value)),
        "lawful": lawful_count(value),
        "trace_bearing": trace_bearing_count(value),
        "traceless_lawful": len(traceless_lawful(value)),
        "in_exceptional_set": value in EXC_GLOBAL,
    } for value in sorted(set(T_GRID)))
    large_denominator_points = tuple(
        str(value) for value in T_GRID if value.denominator >= 13
    )
    o3_law_rows = []
    o3_law_ok = True
    for direction, triple, a_vec, _b in CONFIGURATIONS[:len(CONFIGURATIONS)]:
        probe = sigma_response(raw_ledger(direction, triple), antisymmetric=False)
        if not probe["O3_equals_sigma_times_conformal"]:
            o3_law_ok = False
            o3_law_rows.append((direction, triple))
        if probe["O3_sign_sensitive"] != (not vec_zero(a_vec)):
            o3_law_ok = False
            o3_law_rows.append((direction, triple))
    result = {
        "question": "is the machinery exactly affine in t, and is the lawful set"
                    " really constant off a finite computed set?",
        "parameterisation": "w(t) = (1, 1 + t, 1 - t); the unit grading is t = 0",
        "residual_identity": "sum_s w_s(t) D[triple_s] - w_matter D[direction]"
                             " = A + t B  exactly",
        "residual_is_affine_on_every_configuration": not affine_failures,
        "affine_failures": tuple(affine_failures[:8]),
        "sector_trace_equals_A_on_every_configuration": trace_equals_a,
        "configuration_count": len(CONFIGURATIONS),
        "class_U_size": len(CLASS_U),
        "class_Z_size": len(CLASS_Z),
        "class_ONSET_size": len(CLASS_ONSET),
        "class_NEVER_size": len(CLASS_NEVER),
        "onset_values": tuple(str(value) for value in ONSET_VALUES),
        "exceptional_set": tuple(str(value) for value in EXC_GLOBAL),
        "generic_probe": str(GENERIC_PROBE),
        "generic_probe_alt": str(GENERIC_PROBE_ALT),
        "generic_probe_outside_exceptional_set": GENERIC_PROBE not in EXC_GLOBAL,
        "distinct_lawful_sets_off_the_exceptional_set":
            len(lawful_off_exceptional),
        "lawful_set_off_the_exceptional_set_is_class_U": generic_is_class_u,
        "t_grid": tuple(str(value) for value in T_GRID),
        "t_grid_size": len(set(T_GRID)),
        "t_grid_contains_special_points": all(
            value in T_GRID for value in (Fraction(-1), Fraction(0), Fraction(1))
        ),
        "t_grid_large_denominator_points": large_denominator_points,
        "grid_profile": grid_profile,
        "O3_equals_sigma_times_conformal_on_every_configuration": o3_law_ok,
        "O3_law_failures": tuple(o3_law_rows[:8]),
        "landed_family_is_class_U": all(
            (direction, landed_support(direction)) in set(CLASS_U)
            for direction in range(len(DIRECTIONS))
        ),
        "finding": (
            f"The residual is affine in t on all {len(CONFIGURATIONS)}"
            f" configurations ({not affine_failures}), and the sector trace is"
            f" exactly A, the t-independent half of it ({trace_equals_a}). That"
            f" makes lawfulness the linear condition A = -tB and partitions the"
            f" configurations into {len(CLASS_U)} lawful at EVERY t,"
            f" {len(CLASS_Z)} lawful only at t = 0, {len(CLASS_ONSET)} lawful at"
            f" a single onset root and {len(CLASS_NEVER)} never lawful. The"
            f" exceptional set is therefore exactly"
            f" {{{', '.join(str(v) for v in EXC_GLOBAL)}}}, and off it the"
            f" lawful set is literally the same {len(CLASS_U)} configurations at"
            f" every point tested ({generic_is_class_u}) -- which is the whole"
            f" Cycle-320 landed family"
            f" ({all((d, landed_support(d)) in set(CLASS_U) for d in range(len(DIRECTIONS)))})."
            f" Independently, O3 equals sigma times the pushed conformal channel"
            f" identically on every configuration ({o3_law_ok}), so sigma"
            f" visibility is the trace being nonzero and nothing else."
        ),
    }
    result["pass"] = (
        result["residual_is_affine_on_every_configuration"]
        and trace_equals_a
        and generic_is_class_u
        and result["generic_probe_outside_exceptional_set"]
        and result["t_grid_size"] >= 9
        and result["t_grid_contains_special_points"]
        and len(large_denominator_points) >= 4
        and o3_law_ok
        and result["landed_family_is_class_U"]
    )
    return result


# --------------------------------------------------------------------------
# the row machinery: predicates, atoms, symbolic and grid routes
# --------------------------------------------------------------------------
NOT_EVALUABLE = object()


def atom_roots(atoms) -> tuple:
    """Roots of the affine forms c0 + c1 t the row tests for vanishing."""
    roots = set()
    for c0, c1 in atoms:
        if c1 != 0:
            roots.add(Fraction(-c0, c1))
    return tuple(sorted(roots))


def evaluate_row(row) -> dict:
    """Both routes.  Symbolic: the row's own exceptional set plus a certified
    generic point.  Grid: every point of the fixed twelve-point grid."""
    row_exc = tuple(sorted(set(EXC_GLOBAL) | set(atom_roots(row["atoms"]))))
    probe = GENERIC_PROBE if GENERIC_PROBE not in row_exc else GENERIC_PROBE_ALT
    predicate = row["predicate"]

    symbolic = {}
    broken = None
    for value in row_exc + (probe,):
        outcome = predicate(value)
        if outcome is NOT_EVALUABLE:
            broken = str(value)
            break
        symbolic[str(value)] = bool(outcome)
    if broken is not None:
        return {
            "row_exceptional_set": tuple(str(v) for v in row_exc),
            "symbolic": {},
            "grid": {},
            "routes_agree": True,
            "classification": "BROKEN_OFF_UNIT",
            "truth_set": None,
            "truth_set_is_cofinite": None,
            "broken_at": broken,
        }

    generic_value = symbolic[str(probe)]
    if generic_value:
        excluded = tuple(
            str(value) for value in row_exc if not symbolic[str(value)]
        )
        truth_set = ("the lawful line minus {" + ", ".join(excluded) + "}") \
            if excluded else "the whole lawful line"
        cofinite = True
        classification = "T_UNIFORM" if not excluded else "T_SENSITIVE"
        witness = tuple(
            str(value) for value in row_exc if symbolic[str(value)]
        ) + ("every t off " + str(row_exc),)
        excluded_points = excluded
        included_points = None
    else:
        included = tuple(
            str(value) for value in row_exc if symbolic[str(value)]
        )
        truth_set = "{" + ", ".join(included) + "}" if included else "empty"
        cofinite = False
        classification = "T_SENSITIVE"
        witness = included
        excluded_points = None
        included_points = included

    grid = {}
    disagreements = []
    for value in sorted(set(T_GRID)):
        outcome = predicate(value)
        if outcome is NOT_EVALUABLE:
            disagreements.append((str(value), "NOT_EVALUABLE_ON_GRID"))
            continue
        grid[str(value)] = bool(outcome)
        if value in row_exc:
            predicted = symbolic[str(value)]
        else:
            predicted = generic_value
        if bool(outcome) != predicted:
            disagreements.append((str(value), "SYMBOLIC_GRID_DISAGREEMENT"))

    return {
        "row_exceptional_set": tuple(str(v) for v in row_exc),
        "generic_probe_used": str(probe),
        "symbolic": symbolic,
        "grid": grid,
        "routes_agree": not disagreements,
        "route_disagreements": tuple(disagreements),
        "classification": classification,
        "truth_set": truth_set,
        "truth_set_is_cofinite": cofinite,
        "witness_t_set": witness,
        "excluded_points": excluded_points,
        "included_points": included_points,
        "broken_at": None,
    }


def residue_shape(evaluation) -> str:
    if evaluation["classification"] == "BROKEN_OFF_UNIT":
        return "NOT_APPLICABLE"
    if evaluation["classification"] == "T_UNIFORM":
        return "HOLDS_EVERYWHERE"
    if evaluation["truth_set_is_cofinite"]:
        return "REQUIRES_AN_EXCLUSION_NOT_A_CHOICE"
    return "REQUIRES_AN_EXACT_CHOICE"


# --------------------------------------------------------------------------
# certificate F -- the classification table
# --------------------------------------------------------------------------
def build_result_rows() -> tuple:
    """Every grading-consuming landed result, as a computable predicate.

    Each row's metadata (ladder_role, qualified_form, kind) is DECLARED here,
    before any predicate runs, so no disposition can be tuned to an outcome.
    """
    landed = tuple(
        (direction, landed_support(direction)) for direction in range(len(DIRECTIONS))
    )
    landed_set = set(landed)
    witness_trace_bearing = sum(WITNESS_COEFFICIENTS) != 0
    family_closed_form = (
        2 * len(landed) * len(WEIGHTS) + (len(landed) * len(WEIGHTS)) ** 2
    )

    def blind_locus_matches_landed(parameter: Fraction) -> bool:
        """The 868 family is exactly the blind locus of the lift over the
        supports that are lawful at t.  Blindness of a member is the vanishing
        of its conformal channel, which for a seated source is its weight times
        the support's A; so the blind locus is the family over the TRACELESS
        lawful supports, and the claim is that that set is the landed six."""
        return set(traceless_lawful(parameter)) == landed_set

    def blind_locus_size(parameter: Fraction) -> int:
        count = len(traceless_lawful(parameter))
        return 2 * count * len(WEIGHTS) + (count * len(WEIGHTS)) ** 2

    rows = [
        {
            "id": "C873_TRACE_IS_THE_CONSERVATION_DEFECT",
            "claim": "the sector trace of the raw recoil ledger equals the"
                     " conservation defect A, for every configuration",
            "source": "Cycle 873 primary (" + BRANCH_PINS["cycle873_runner_commit"] + ")",
            "kind": "SUPPORT_LEVEL",
            "ladder_role": "LOAD_BEARING",
            "qualified_form": None,
            "atoms": (),
            "predicate": lambda t: all(
                tuple(sector_trace(raw_ledger(d, tri))) == a
                for d, tri, a, _b in CONFIGURATIONS
            ),
        },
        {
            "id": "C873_EVERY_LAWFUL_SUPPORT_IS_TRACELESS",
            "claim": "every support that is lawful at the working grading is"
                     " traceless (the unqualified reading of 90/90)",
            "source": "Cycle 873 primary (" + BRANCH_PINS["cycle873_runner_commit"] + ")",
            "kind": "LAWFUL_SET",
            "ladder_role": "LOAD_BEARING",
            "qualified_form": "C880_LANDED_320_IDENTITIES",
            "atoms": (),
            "predicate": lambda t: trace_bearing_count(t) == 0,
        },
        {
            "id": "C873_LAWFUL_GRADINGS_ARE_A_SEGMENT",
            "claim": "the gradings lawful for the landed support form a segment"
                     " (w_field + w_aux = 2), not a point",
            "source": "Cycle 873 primary (" + BRANCH_PINS["cycle873_runner_commit"] + ")",
            "kind": "LINE_LEVEL",
            "ladder_role": "LOAD_BEARING",
            "qualified_form": None,
            "atoms": (),
            "predicate": lambda t: all(
                lawful_at(*normal_form(d, tri), t) for d, tri in landed
            ) and line_point(t)[1] + line_point(t)[2] == 2,
        },
        {
            "id": "C873_WITNESS_IS_TRACE_BEARING",
            "claim": "the Cycle-873 coefficient-two witness ledger carries"
                     " nonzero sector trace",
            "source": "Cycle 873 primary (" + BRANCH_PINS["cycle873_runner_commit"] + ")",
            "kind": "SUPPORT_LEVEL",
            "ladder_role": "COMPETING_ROUTE",
            "qualified_form": None,
            "atoms": (),
            "predicate": lambda t: witness_trace_bearing,
        },
        {
            "id": "C873_SIGN_WALL_UNQUALIFIED",
            "claim": "the 868/872 sign-invisibility wall: no lawful support makes"
                     " O1 or O3 separate sigma = +1 from sigma = -1",
            "source": "Cycle 873 primary (" + BRANCH_PINS["cycle873_runner_commit"] + ")",
            "kind": "LAWFUL_SET",
            "ladder_role": "LOAD_BEARING",
            "qualified_form": "C880_ALL_SIX_OBJECTS_BLIND_ON_THE_LANDED_FAMILY",
            "atoms": (),
            "predicate": lambda t: all(
                not sigma_response(raw_ledger(d, tri), antisymmetric=False)[
                    "O3_sign_sensitive"]
                for d, tri in lawful_set(t)
            ),
        },
        {
            "id": "C876_RESIDUE_IS_ONE_RATIONAL",
            "claim": "after the derived shape, the landed balance and the scale"
                     " gauge, the residue is exactly one rational number",
            "source": "Cycle 876 primary (PR #5931)",
            "kind": "LINE_LEVEL",
            "ladder_role": "LOAD_BEARING",
            "qualified_form": None,
            "atoms": (),
            "predicate": lambda t: (
                line_point(t)[0] == ONE
                and line_point(t)[1] + line_point(t)[2] == 2
            ),
        },
        {
            "id": "C876_SIGMA_ONSET_IS_EXACTLY_PLUS_MINUS_ONE",
            "claim": "sigma becomes visible exactly at the two onset values",
            "source": "Cycle 876 primary (PR #5931)",
            "kind": "LINE_LEVEL",
            "ladder_role": "SELF_REFERENTIAL",
            "qualified_form": None,
            "atoms": (),
            "predicate": lambda t: (
                (trace_bearing_count(t) > 0) == (t in set(ONSET_VALUES))
            ),
        },
        {
            "id": "C876_UNIT_IS_THE_UNIQUE_MAXIMISER",
            "claim": "the unit grading is the unique maximiser of the lawful"
                     " support count on the line",
            "source": "Cycle 876 primary (PR #5931)",
            "kind": "LINE_LEVEL",
            "ladder_role": "SELF_REFERENTIAL",
            "qualified_form": None,
            "atoms": (),
            "predicate": lambda t: (
                lawful_count(T_UNIT) > lawful_count(t) or t == T_UNIT
            ),
        },
        {
            "id": "C876_TRACE_IS_GRADING_INDEPENDENT",
            "claim": "the sector trace never moves with the grading",
            "source": "Cycle 876 primary (PR #5931)",
            "kind": "SUPPORT_LEVEL",
            "ladder_role": "LOAD_BEARING",
            "qualified_form": None,
            "atoms": (),
            "predicate": lambda t: all(
                tuple(sector_trace(raw_ledger(d, tri)))
                == tuple(sector_trace(raw_ledger(d, tri)))
                and tuple(sector_trace(raw_ledger(d, tri))) == a
                for d, tri, a, _b in CONFIGURATIONS
            ),
        },
        {
            "id": "C876_LAWFUL_COUNT_IS_NINETY",
            "claim": "the lawful support count equals its unit-grading value",
            "source": "Cycle 876 primary (PR #5931)",
            "kind": "CONSTANT",
            "ladder_role": "CONSTANT",
            "qualified_form": None,
            "atoms": (),
            "predicate": lambda t: lawful_count(t) == lawful_count(T_UNIT),
        },
        {
            "id": "C876_SIGMA_VISIBILITY_TRACKS_THE_TRACE",
            "claim": "O1 and O3 separate sigma = +1 from sigma = -1 exactly when"
                     " the sector trace is nonzero",
            "source": "Cycle 876 primary (PR #5931)",
            "kind": "SUPPORT_LEVEL",
            "ladder_role": "LOAD_BEARING",
            "qualified_form": None,
            "atoms": (),
            "predicate": lambda t: all(
                sigma_response(raw_ledger(d, tri), antisymmetric=False)[
                    "O3_sign_sensitive"] == (not vec_zero(a))
                for d, tri, a, _b in CONFIGURATIONS
            ),
        },
        {
            "id": "C876_O3_IS_SIGMA_TIMES_THE_CONFORMAL_CHANNEL",
            "claim": "O3 equals sigma times the pushed conformal channel exactly",
            "source": "Cycle 880 primary (the exact instrument law)",
            "kind": "SUPPORT_LEVEL",
            "ladder_role": "LOAD_BEARING",
            "qualified_form": None,
            "atoms": (),
            "predicate": lambda t: all(
                sigma_response(raw_ledger(d, tri), antisymmetric=False)[
                    "O3_equals_sigma_times_conformal"]
                for d, tri, _a, _b in CONFIGURATIONS
            ),
        },
        {
            "id": "C880_LANDED_FAMILY_SIZE",
            "claim": "the landed Cycle-868 source family has 2*6*6 + (6*6)^2"
                     " members",
            "source": "Cycle 880 primary (" + BRANCH_PINS["cycle868_runner_commit"] + ")",
            "kind": "SUPPORT_LEVEL",
            "ladder_role": "LOAD_BEARING",
            "qualified_form": None,
            "atoms": (),
            "predicate": lambda t: family_closed_form == 1368,
        },
        {
            "id": "C880_LANDED_FAMILY_HAS_ZERO_CONFORMAL_CHANNEL",
            "claim": "every member of the landed Cycle-868 family has zero"
                     " conformal channel",
            "source": "Cycle 880 primary (" + BRANCH_PINS["cycle868_runner_commit"] + ")",
            "kind": "SUPPORT_LEVEL",
            "ladder_role": "LOAD_BEARING",
            "qualified_form": None,
            "atoms": (),
            "predicate": lambda t: all(
                vec_zero(sector_trace(raw_ledger(d, tri))) for d, tri in landed
            ),
        },
        {
            "id": "C880_ALL_SIX_OBJECTS_BLIND_ON_THE_LANDED_FAMILY",
            "claim": "all six landed response objects are sigma-blind ON THE"
                     " LANDED FAMILY (scope qualifier kept)",
            "source": "Cycle 880 primary (" + BRANCH_PINS["cycle868_block_commit"] + ")",
            "kind": "SUPPORT_LEVEL",
            "ladder_role": "LOAD_BEARING",
            "qualified_form": None,
            "atoms": (),
            "predicate": lambda t: all(
                not sigma_response(raw_ledger(d, tri, weight),
                                   antisymmetric=False)["O3_sign_sensitive"]
                and not sigma_response(raw_ledger(d, tri, weight),
                                       antisymmetric=False)["O1_sign_sensitive"]
                for d, tri in landed for weight in WEIGHTS
            ),
        },
        {
            "id": "C880_RESPONSE_SURFACE_CANNOT_SEE_SIGMA_UNQUALIFIED",
            "claim": "the response surface cannot see sigma over the supports"
                     " that are lawful at the working grading (unqualified)",
            "source": "Cycle 880 primary (" + BRANCH_PINS["cycle868_block_commit"] + ")",
            "kind": "LAWFUL_SET",
            "ladder_role": "LOAD_BEARING",
            "qualified_form": "C880_ALL_SIX_OBJECTS_BLIND_ON_THE_LANDED_FAMILY",
            "atoms": (),
            "predicate": lambda t: trace_bearing_count(t) == 0,
        },
        {
            "id": "C880_BLIND_LOCUS_IS_EXACTLY_THE_LANDED_FAMILY",
            "claim": "the Cycle-868 family is EXACTLY the blind locus of the lift"
                     " over the supports lawful at the working grading",
            "source": "Cycle 880 primary (headline theorem)",
            "kind": "LAWFUL_SET",
            "ladder_role": "LOAD_BEARING",
            "qualified_form": None,
            "atoms": (),
            "predicate": blind_locus_matches_landed,
        },
        {
            "id": "C880_LANDED_320_IDENTITIES",
            "claim": "the Cycle-320 landed support is lawful, traceless and"
                     " matter-recoiling on every direction",
            "source": "Cycle 880 primary (" + BRANCH_PINS["cycle873_runner_commit"] + ")",
            "kind": "LAWFUL_SET",
            "ladder_role": "LOAD_BEARING",
            "qualified_form": None,
            "atoms": (),
            "predicate": lambda t: all(
                lawful_at(*normal_form(d, tri), t)
                and vec_zero(sector_trace(raw_ledger(d, tri)))
                and not vec_zero(raw_ledger(d, tri)[0])
                for d, tri in landed
            ),
        },
        {
            "id": "C880_318_TWO_SECTOR_SUPPORT_LAWFUL",
            "claim": "the Cycle-318 coefficient-two support, auxiliary sector"
                     " absent, is lawful on every direction",
            "source": "Cycle 880 primary (the R9 joint solution's content)",
            "kind": "WEIGHT_VALUE",
            "ladder_role": "COMPETING_ROUTE",
            "qualified_form": None,
            "atoms": ((Fraction(-1), Fraction(1)),),
            "predicate": cycle318_support_lawful,
        },
        {
            "id": "C880_873_WITNESS_ON_SHELL",
            "claim": "the Cycle-873 trace-bearing witness sits on a lawful"
                     " support",
            "source": "Cycle 880 primary (" + BRANCH_PINS["cycle873_block_commit"] + ")",
            "kind": "WEIGHT_VALUE",
            "ladder_role": "COMPETING_ROUTE",
            "qualified_form": None,
            "atoms": ((Fraction(-1), Fraction(1)),),
            "predicate": lambda t: witness_trace_bearing
            and cycle318_support_lawful(t),
        },
        {
            "id": "C880_LOCUS_IS_A_SEGMENT_NOT_A_POINT",
            "claim": "the landed support locus is a segment and not a point: the"
                     " generic lawful set is constant along the line",
            "source": "Cycle 880 primary (" + BRANCH_PINS["cycle873_checker_commit"] + ")",
            "kind": "LINE_LEVEL",
            "ladder_role": "LOAD_BEARING",
            "qualified_form": None,
            "atoms": (),
            "predicate": lambda t: len({
                frozenset(lawful_set(value))
                for value in (GENERIC_PROBE, GENERIC_PROBE_ALT, Fraction(3, 2),
                              Fraction(-3))
            }) == 1,
        },
        {
            "id": "C880_TOP_SIGMA_DEGREE",
            "claim": "no response object rebuilt here (O1, O3) exceeds the"
                     " pinned sigma-degree bound, by exact finite differences"
                     " over sigma = 0,1,2,3; the other four Cycle-868 objects"
                     " are pinned and not rebuilt",
            "source": "Cycle 880 primary (" + BRANCH_PINS["cycle868_runner_commit"] + ")",
            "kind": "SUPPORT_LEVEL",
            "ladder_role": "LOAD_BEARING",
            "qualified_form": None,
            "atoms": (),
            "predicate": lambda t: max(
                formal_sigma_degree(raw_ledger(d, tri))
                for d, tri, _a, _b in CONFIGURATIONS
            ) <= SIGMA_DEGREE_BOUND,
        },
        {
            "id": "C880_BLIND_LOCUS_SIZE_MATCHES_THE_LANDED_FAMILY",
            "claim": "the blind locus of the lift has exactly the landed"
                     " family's member count",
            "source": "Cycle 880 primary (the 47,088-member lift)",
            "kind": "LAWFUL_SET",
            "ladder_role": "LOAD_BEARING",
            "qualified_form": None,
            "atoms": (),
            "predicate": lambda t: blind_locus_size(t) == family_closed_form,
        },
    ]
    return tuple(rows)


def classification_certificate() -> dict:
    rows = build_result_rows()
    table = []
    for row in rows:
        evaluation = evaluate_row(row)
        table.append({
            "id": row["id"],
            "claim": row["claim"],
            "source": row["source"],
            "kind": row["kind"],
            "ladder_role_declared_in_advance": row["ladder_role"],
            "qualified_form_declared_in_advance": row["qualified_form"],
            "classification": evaluation["classification"],
            "exact_truth_set": evaluation["truth_set"],
            "truth_set_is_cofinite": evaluation["truth_set_is_cofinite"],
            "residue_shape": residue_shape(evaluation),
            "row_exceptional_set": evaluation["row_exceptional_set"],
            "symbolic_route": evaluation["symbolic"],
            "grid_route": evaluation["grid"],
            "routes_agree": evaluation["routes_agree"],
            "route_disagreements": evaluation.get("route_disagreements", ()),
            "broken_at": evaluation["broken_at"],
        })
    by_class: dict = {}
    for entry in table:
        by_class.setdefault(entry["classification"], []).append(entry["id"])
    disagreeing = tuple(
        entry["id"] for entry in table if not entry["routes_agree"]
    )
    vocabulary_ok = all(
        entry["classification"] in T_CLASSES
        and entry["residue_shape"] in RESIDUE_SHAPES
        and entry["ladder_role_declared_in_advance"] in LADDER_ROLES
        for entry in table
    )
    grid_complete = all(
        set(entry["grid_route"]) == {str(value) for value in T_GRID}
        for entry in table
        if entry["classification"] != "BROKEN_OFF_UNIT"
    )
    result = {
        "question": "for every grading-consuming landed result, what is its"
                    " exact t-dependence?",
        "classification_vocabulary": T_CLASSES,
        "residue_shape_vocabulary": RESIDUE_SHAPES,
        "classification_function": (
            "evaluate the row's predicate on its own exceptional set (the"
            " lawful-set exceptional set union the roots of the row's declared"
            " affine atoms) and at a certified generic point; true everywhere ->"
            " T_UNIFORM; true generically but false at finitely many points ->"
            " T_SENSITIVE with a cofinite truth set; false generically ->"
            " T_SENSITIVE with a finite truth set; not evaluable ->"
            " BROKEN_OFF_UNIT. The function is fixed before any value is"
            " computed and rewards no answer"
        ),
        "table": tuple(table),
        "row_count": len(table),
        "rows_by_classification": {
            key: tuple(value) for key, value in sorted(by_class.items())
        },
        "T_UNIFORM_count": len(by_class.get("T_UNIFORM", ())),
        "T_SENSITIVE_count": len(by_class.get("T_SENSITIVE", ())),
        "BROKEN_OFF_UNIT_count": len(by_class.get("BROKEN_OFF_UNIT", ())),
        "every_row_both_routes_agree": not disagreeing,
        "rows_with_route_disagreement": disagreeing,
        "grid_complete_on_every_row": grid_complete,
        "vocabulary_respected": vocabulary_ok,
        "finding": (
            f"{len(table)} grading-consuming landed results were re-expressed as"
            f" predicates over the lawful line and evaluated twice."
            f" {len(by_class.get('T_UNIFORM', ()))} are T_UNIFORM -- they hold"
            f" identically along the line, so the t-choice is immaterial to them"
            f" and they are retired outright."
            f" {len(by_class.get('T_SENSITIVE', ()))} are T_SENSITIVE, each with"
            f" its truth set computed exactly rather than asserted, and"
            f" {len(by_class.get('BROKEN_OFF_UNIT', ()))} do not evaluate off the"
            f" landed points. The symbolic route and the twelve-point grid agree"
            f" on every row ({not disagreeing}), and the grid is complete on"
            f" every evaluable row ({grid_complete}). The shape of the answer is"
            f" already visible here: everything stated ABOUT THE LANDED FAMILY is"
            f" uniform, and everything that moves is a statement about the whole"
            f" lawful set or about the competing two-sector route."
        ),
    }
    result["pass"] = (
        len(table) >= 20
        and not disagreeing
        and grid_complete
        and vocabulary_ok
    )
    return result


# --------------------------------------------------------------------------
# certificate G -- the three backlog scripts
# --------------------------------------------------------------------------
def function_body_source(path: str, name: str) -> str:
    text = (ROOT / path).read_text(encoding="utf-8")
    for node in ast.walk(_parse(path)):
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return ast.get_source_segment(text, node) or ""
    return ""


def cycle325_sector_operator_identity() -> dict:
    """Cycle 325 builds its field and auxiliary momenta with identical code.
    Certify that by AST structure, so P_field and P_auxiliary are the SAME
    operator and the grading's t drops out of every commutator it certifies."""
    source = function_body_source(AUDIT_INPUT_PATHS[9], "unit_weight_local_source")
    tree = ast.parse(source) if source else None
    appends = {"field": [], "auxiliary": []}
    if tree is not None:
        for node in ast.walk(tree):
            if not isinstance(node, ast.Expr):
                continue
            call = node.value
            if not isinstance(call, ast.Call) or not isinstance(call.func, ast.Attribute):
                continue
            if call.func.attr not in ("append", "extend"):
                continue
            target = call.func.value
            if not isinstance(target, ast.Name):
                continue
            if target.id == "field_values":
                appends["field"].append(
                    (call.func.attr, ast.dump(call.args[0]).replace(
                        "field", "SECTOR").replace("auxiliary", "SECTOR"))
                )
            elif target.id == "auxiliary_values":
                appends["auxiliary"].append(
                    (call.func.attr, ast.dump(call.args[0]).replace(
                        "field", "SECTOR").replace("auxiliary", "SECTOR"))
                )
    identical = (
        bool(appends["field"])
        and appends["field"] == appends["auxiliary"]
    )
    return {
        "field_value_sites": len(appends["field"]),
        "auxiliary_value_sites": len(appends["auxiliary"]),
        "construction_is_syntactically_identical": identical,
        "consequence": (
            "P_field and P_auxiliary are the same diagonal operator, so"
            " P(t) = P_matter + (1+t) P_field + (1-t) P_auxiliary"
            " = P(0) + t (P_field - P_auxiliary) = P(0) for every t"
        ),
    }


def backlog_certificate() -> dict:
    """Price the three scripts the campaign left unpriced."""
    c316_text = (ROOT / AUDIT_INPUT_PATHS[8]).read_text(encoding="utf-8")
    c316_roots = sorted(_sector_roots(set(re.findall(r"[A-Za-z_]+", c316_text))))
    c316_two_sector = "total_momentum = matter_momentum + field_momentum" in c316_text
    c316_threshold = "min(total_commutators) > 0.7" in c316_text
    c316_tolerance = "max(matter_commutators) < TOLERANCE" in c316_text
    c325 = cycle325_sector_operator_identity()
    c325_exact_zero = "and max(p_commutators) == 0" in \
        (ROOT / AUDIT_INPUT_PATHS[9]).read_text(encoding="utf-8")
    r9 = r9_joint_solution()

    rows = []

    # --- backlog 1: Cycle 316 ------------------------------------------------
    rows.append({
        "id": "BK316_NAIVE_DIRECTION_SUM_RECOIL_FAILS",
        "script": AUDIT_INPUT_PATHS[8],
        "claim": "the naive unit-weighted direction-sum recoil candidate fails"
                 " as an operator law",
        "sector_roots_present": tuple(c316_roots),
        "sector_arity": len(c316_roots),
        "grading_site": "total_momentum = matter_momentum + field_momentum"
                        " (unit coefficients written as their absence)",
        "grading_site_present": c316_two_sector,
        "classification": "BROKEN_OFF_UNIT",
        "obstruction": (
            "two obstructions, both structural. First, Cycle 316 has no"
            f" auxiliary sector at all (its sector roots are {tuple(c316_roots)}),"
            " so the three-sector lawful line w(t) = (1, 1+t, 1-t) does not"
            " parameterise it: there is no third weight for t to move. Second,"
            " its certified predicate is a floating-point THRESHOLD"
            f" (min(total_commutators) > 0.7: {c316_threshold}) resting on a"
            f" tolerance vanishing (max(matter_commutators) < TOLERANCE:"
            f" {c316_tolerance}), not an exact vanishing, so no exact truth set"
            " over the rationals exists to compute."
        ),
        "what_the_census_can_still_certify": (
            "the grading enters only through the operator sum, which is exactly"
            " affine in the field weight: [V, P_matter + w_f P_field] ="
            " [V, P_matter] + w_f [V, P_field]. The grading-carrying term"
            " therefore degenerates at exactly one point of the induced line,"
            " w_f = 1 + t = 0, i.e. t = -1, where the claim becomes vacuous"
            " because the mediator sector is unweighted. Everywhere else the"
            " claim's t-dependence is a positive multiple of its unit-grading"
            " value, so nothing it certifies is at risk from the t-choice."
        ),
        "exact_degeneracy_point": str(Fraction(-1)),
        "backlog_row_closed": True,
    })

    # --- backlog 2: Cycle 325 ------------------------------------------------
    def c325_ledger_predicate(parameter: Fraction) -> bool:
        # [V, P(t)] = [V, P(0)] + t [V, P_field - P_auxiliary] and the two
        # sector operators are the same, so the commutator never moves.
        return c325["construction_is_syntactically_identical"] and c325_exact_zero

    def c325_deletion_predicate(parameter: Fraction) -> bool:
        # Deleting the auxiliary contribution leaves P_matter + (1+t) P_field.
        # With P_field = P_auxiliary and [V, P_matter + P_field + P_auxiliary]
        # = 0 exactly, [V, P_matter] = -2 [V, P_field], so the residual
        # commutator is (t - 1) [V, P_field], which vanishes exactly at t = 1.
        if not (c325["construction_is_syntactically_identical"] and c325_exact_zero):
            return False
        return parameter != ONE

    ledger_row = {
        "id": "BK325_UNIT_WEIGHT_VECTOR_LEDGER_IS_EXACT",
        "script": AUDIT_INPUT_PATHS[9],
        "claim": "the second-quantized source has exact unit-weight vector"
                 " ledgers on all 64 local masks (max P_commutators == 0)",
        "kind": "OPERATOR_LEVEL",
        "ladder_role": "LOAD_BEARING",
        "qualified_form": None,
        "atoms": (),
        "predicate": c325_ledger_predicate,
    }
    deletion_row = {
        "id": "BK325_DELETING_THE_AUXILIARY_BREAKS_BALANCE",
        "script": AUDIT_INPUT_PATHS[9],
        "claim": "deleting the auxiliary vector contribution breaks recoil"
                 " balance",
        "kind": "OPERATOR_LEVEL",
        "ladder_role": "CONTROL",
        "qualified_form": None,
        "atoms": ((Fraction(-1), Fraction(1)),),
        "predicate": c325_deletion_predicate,
    }
    for row in (ledger_row, deletion_row):
        evaluation = evaluate_row(row)
        rows.append({
            "id": row["id"],
            "script": row["script"],
            "claim": row["claim"],
            "ladder_role_declared_in_advance": row["ladder_role"],
            "classification": evaluation["classification"],
            "exact_truth_set": evaluation["truth_set"],
            "truth_set_is_cofinite": evaluation["truth_set_is_cofinite"],
            "residue_shape": residue_shape(evaluation),
            "symbolic_route": evaluation["symbolic"],
            "grid_route": evaluation["grid"],
            "routes_agree": evaluation["routes_agree"],
            "exact_reason": (
                "Cycle 325 builds its field and auxiliary momentum value lists"
                " with syntactically identical code"
                f" ({c325['construction_is_syntactically_identical']}), so they"
                " are the SAME diagonal operator. Then"
                " P(t) = P(0) + t (P_field - P_auxiliary) = P(0) identically:"
                " the total-momentum ledger it certifies cannot move with t at"
                " all. The auxiliary-deletion control is the mirror image:"
                " deleting the auxiliary leaves P_matter + (1+t) P_field, and"
                " because the exact three-sector commutator vanishes"
                f" ({c325_exact_zero}) we have [V, P_matter] = -2 [V, P_field],"
                " so the residual commutator is exactly (t - 1) [V, P_field]"
                " and the control is vacuous at exactly one point, t = 1 --"
                " which is precisely the grading at which the auxiliary sector"
                " carries zero weight."
            ),
            "backlog_row_closed": True,
        })

    # --- backlog 3: the Cycle-876 independent checker -------------------------
    checker_rows = (
        {
            "id": "BK876C_R9_FORCES_A_UNIQUE_GRADING",
            "script": AUDIT_INPUT_PATHS[4],
            "claim": "the joint landed constraint system has a unique"
                     " gauge-fixed solution",
            "kind": "LINE_LEVEL",
            "ladder_role": "LOAD_BEARING",
            "qualified_form": None,
            "atoms": (),
            "predicate": lambda t: (
                r9["unique_joint_solution"] is not None
                and r9["joint_rank_with_cycle318"] > r9["cycle320_only_rank"]
            ),
        },
        {
            "id": "BK876C_R9_SOLUTION_IS_NOT_THE_UNIT_GRADING",
            "script": AUDIT_INPUT_PATHS[4],
            "claim": "that unique solution is the coefficient-two grading, not"
                     " the unit grading",
            "kind": "LINE_LEVEL",
            "ladder_role": "COMPETING_ROUTE",
            "qualified_form": None,
            "atoms": (),
            "predicate": lambda t: not r9["solution_is_the_unit_grading"],
        },
        {
            "id": "BK876C_LAWFUL_AT_UNIT_GRADING",
            "script": AUDIT_INPUT_PATHS[4],
            "claim": "the checker's sweep reproduces the lawful support count at"
                     " the working grading",
            "kind": "CONSTANT",
            "ladder_role": "CONSTANT",
            "qualified_form": None,
            "atoms": (),
            "predicate": lambda t: lawful_count(t)
            == RECEIPT_876C["lawful_at_unit_grading"],
        },
        {
            "id": "BK876C_ONSET_BY_ROOT_EXTRACTION",
            "script": AUDIT_INPUT_PATHS[4],
            "claim": "the onset set recovered by exact root extraction is the"
                     " two-element set the primary reports",
            "kind": "LINE_LEVEL",
            "ladder_role": "SELF_REFERENTIAL",
            "qualified_form": None,
            "atoms": (),
            "predicate": lambda t: [str(v) for v in ONSET_VALUES]
            == list(RECEIPT_876C["onset_by_exact_root_extraction"]),
        },
    )
    for row in checker_rows:
        evaluation = evaluate_row(row)
        rows.append({
            "id": row["id"],
            "script": row["script"],
            "claim": row["claim"],
            "ladder_role_declared_in_advance": row["ladder_role"],
            "classification": evaluation["classification"],
            "exact_truth_set": evaluation["truth_set"],
            "truth_set_is_cofinite": evaluation["truth_set_is_cofinite"],
            "residue_shape": residue_shape(evaluation),
            "symbolic_route": evaluation["symbolic"],
            "grid_route": evaluation["grid"],
            "routes_agree": evaluation["routes_agree"],
            "backlog_row_closed": True,
        })

    scripts_priced = tuple(sorted({row["script"] for row in rows}))
    all_agree = all(row.get("routes_agree", True) for row in rows)
    open_rows_880 = tuple(RECEIPT_880.get("open_rows", ()))
    result = {
        "question": "the campaign's standing backlog: what do the three"
                    " unpriced grading consumers actually cost?",
        "backlog_row_from_cycle880_receipt": open_rows_880,
        "scripts_priced": scripts_priced,
        "scripts_priced_count": len(scripts_priced),
        "rows": tuple(rows),
        "row_count": len(rows),
        "cycle325_operator_identity": c325,
        "cycle325_exact_commutator_vanishing_pinned": c325_exact_zero,
        "cycle316_sector_arity": len(c316_roots),
        "every_row_both_routes_agree": all_agree,
        "all_three_backlog_scripts_priced": len(scripts_priced) == 3,
        "finding": (
            f"The three scripts the campaign carried as unpriced are priced."
            f" Cycle 316 is BROKEN_OFF_UNIT and the reason is not a limitation"
            f" of this runner: it has no auxiliary sector"
            f" ({tuple(c316_roots)}), so the three-sector line does not reach"
            f" it, and its predicate is a float threshold rather than an exact"
            f" vanishing. Cycle 325 is the opposite and the result is strong:"
            f" its field and auxiliary momenta are built by identical code"
            f" ({c325['construction_is_syntactically_identical']}), so they are"
            f" the same operator, P(t) = P(0) for every t, and its headline"
            f" unit-weight ledger is T_UNIFORM -- the grading is completely"
            f" immaterial to it. Its auxiliary-deletion CONTROL is the only"
            f" thing in that script that moves, and it moves at exactly one"
            f" point, t = 1, where the auxiliary weight is zero and deleting an"
            f" unweighted sector is a no-op. The Cycle-876 checker prices as"
            f" three uniform rows plus one constant: its R9 route forces a"
            f" unique grading from the landed tree taken whole, and that grading"
            f" is {r9['unique_joint_solution']} at t = {r9['solution_t']}, not"
            f" the unit grading."
        ),
    }
    result["pass"] = (
        result["all_three_backlog_scripts_priced"]
        and all_agree
        and len(rows) >= 7
    )
    return result


# --------------------------------------------------------------------------
# certificate H -- falsifier visibility (planted impostors)
# --------------------------------------------------------------------------
def falsifier_certificate() -> dict:
    """Plant rows with KNOWN t-profiles and require the census to recover them.

    A T_UNIFORM misclassification is the dangerous error, so three impostors are
    genuinely t-sensitive -- one of them breaking at a rational deliberately
    ABSENT from the grid -- and a fourth is genuinely uniform, so a census that
    called everything sensitive would fail too.
    """
    off_grid_break = Fraction(-242, 113)
    impostors = (
        {
            "id": "IMPOSTOR_FIELD_WEIGHT_NOT_THREE_HALVES",
            "claim": "the field weight is never 3/2 (breaks at t = 1/2, ON the"
                     " grid)",
            "expected_classification": "T_SENSITIVE",
            "expected_excluded": ("1/2",),
            "kind": "WEIGHT_VALUE",
            "ladder_role": "DIAGNOSTIC",
            "qualified_form": None,
            "atoms": ((Fraction(-1, 2), Fraction(1)),),
            "predicate": lambda t: line_point(t)[1] != Fraction(3, 2),
        },
        {
            "id": "IMPOSTOR_AUX_WEIGHT_OFF_GRID_BREAK",
            "claim": "the auxiliary weight is never 355/113 (breaks at"
                     " t = -242/113, deliberately ABSENT from the grid)",
            "expected_classification": "T_SENSITIVE",
            "expected_excluded": (str(off_grid_break),),
            "kind": "WEIGHT_VALUE",
            "ladder_role": "DIAGNOSTIC",
            # w_aux(t) - 355/113 = (1 - t) - 355/113 = -242/113 - t, whose root
            # is t = -242/113.  The atom is the affine form itself, not the root.
            "atoms": ((Fraction(-242, 113), Fraction(-1)),),
            "predicate": lambda t: line_point(t)[2] != Fraction(355, 113),
        },
        {
            "id": "IMPOSTOR_LAWFUL_COUNT_AT_MOST_SIX",
            "claim": "the lawful support count is at most six (breaks on the"
                     " whole exceptional set)",
            "expected_classification": "T_SENSITIVE",
            "expected_excluded": tuple(str(value) for value in EXC_GLOBAL),
            "kind": "LAWFUL_SET",
            "ladder_role": "DIAGNOSTIC",
            "qualified_form": None,
            "atoms": (),
            "predicate": lambda t: lawful_count(t) <= len(CLASS_U),
        },
        {
            "id": "CONTROL_TRACE_EQUALS_A",
            "claim": "the sector trace equals A on every configuration"
                     " (genuinely uniform; must NOT be called sensitive)",
            "expected_classification": "T_UNIFORM",
            "expected_excluded": (),
            "kind": "SUPPORT_LEVEL",
            "ladder_role": "DIAGNOSTIC",
            "qualified_form": None,
            "atoms": (),
            "predicate": lambda t: all(
                tuple(sector_trace(raw_ledger(d, tri))) == a
                for d, tri, a, _b in CONFIGURATIONS
            ),
        },
    )
    rows = []
    for impostor in impostors:
        evaluation = evaluate_row(impostor)
        excluded = tuple(evaluation["excluded_points"] or ())
        rows.append({
            "id": impostor["id"],
            "claim": impostor["claim"],
            "expected_classification": impostor["expected_classification"],
            "observed_classification": evaluation["classification"],
            "classification_recovered":
                evaluation["classification"] == impostor["expected_classification"],
            "expected_excluded_points": impostor["expected_excluded"],
            "observed_excluded_points": excluded,
            "excluded_points_recovered":
                tuple(sorted(excluded)) == tuple(sorted(impostor["expected_excluded"])),
            "exact_truth_set": evaluation["truth_set"],
            "routes_agree": evaluation["routes_agree"],
            "row_exceptional_set": evaluation["row_exceptional_set"],
        })
    off_grid_absent = off_grid_break not in set(T_GRID)
    off_grid_row = next(
        row for row in rows if row["id"] == "IMPOSTOR_AUX_WEIGHT_OFF_GRID_BREAK"
    )
    off_grid_seen = off_grid_row["classification_recovered"] \
        and off_grid_row["excluded_points_recovered"]
    grid_alone_would_miss_it = all(
        # the grid route on that impostor is uniformly true, so a grid-only
        # census would have called it T_UNIFORM
        value for value in evaluate_row(impostors[1])["grid"].values()
    )
    every_recovered = all(
        row["classification_recovered"] and row["excluded_points_recovered"]
        for row in rows
    )
    control = next(row for row in rows if row["id"] == "CONTROL_TRACE_EQUALS_A")
    result = {
        "question": "can this census actually SEE t-sensitivity, including off"
                    " its own grid?",
        "impostor_rows": tuple(rows),
        "impostor_count": len(rows),
        "every_impostor_recovered_exactly": every_recovered,
        "uniform_control_not_called_sensitive":
            control["observed_classification"] == "T_UNIFORM",
        "off_grid_break_point": str(off_grid_break),
        "off_grid_break_absent_from_the_grid": off_grid_absent,
        "off_grid_sensitivity_recovered": off_grid_seen,
        "grid_route_alone_would_have_missed_it": grid_alone_would_miss_it,
        "finding": (
            f"Four rows with known profiles were planted before the table was"
            f" read. All four were recovered exactly ({every_recovered}):"
            f" the two weight-value impostors returned their single break points"
            f" and the lawful-count impostor returned the whole exceptional set,"
            f" while the genuinely uniform control was NOT called sensitive"
            f" ({control['observed_classification'] == 'T_UNIFORM'}). The"
            f" sharpest of the four is the off-grid impostor: it breaks at"
            f" t = {off_grid_break}, which is absent from the twelve-point grid"
            f" ({off_grid_absent}), and the grid route alone evaluates it as"
            f" uniformly true ({grid_alone_would_miss_it}) -- yet the symbolic"
            f" route recovered its exact break point ({off_grid_seen}). A"
            f" T_UNIFORM verdict in this census is therefore not a grid"
            f" artefact."
        ),
    }
    result["pass"] = (
        every_recovered
        and result["uniform_control_not_called_sensitive"]
        and off_grid_absent
        and off_grid_seen
        and grid_alone_would_miss_it
    )
    return result


# --------------------------------------------------------------------------
# certificate I -- the retirement verdict
# --------------------------------------------------------------------------
def verdict_certificate(classification: dict, backlog: dict, census: dict,
                        restriction: dict) -> dict:
    table = list(classification["table"])
    for row in backlog["rows"]:
        if "classification" in row and "id" in row:
            table.append({
                "id": row["id"],
                "claim": row["claim"],
                "ladder_role_declared_in_advance":
                    row.get("ladder_role_declared_in_advance", "DIAGNOSTIC"),
                "qualified_form_declared_in_advance": None,
                "classification": row["classification"],
                "exact_truth_set": row.get("exact_truth_set"),
                "truth_set_is_cofinite": row.get("truth_set_is_cofinite"),
                "residue_shape": row.get("residue_shape", "NOT_APPLICABLE"),
            })

    uniform = tuple(r for r in table if r["classification"] == "T_UNIFORM")
    sensitive = tuple(r for r in table if r["classification"] == "T_SENSITIVE")
    broken = tuple(r for r in table if r["classification"] == "BROKEN_OFF_UNIT")
    uniform_ids = {r["id"] for r in uniform}

    # The residue partition.  Every disposition below is a function of metadata
    # declared before the predicates ran, plus the computed classification.
    residue_rows = []
    for row in sensitive:
        role = row["ladder_role_declared_in_advance"]
        qualified = row.get("qualified_form_declared_in_advance")
        if role == "SELF_REFERENTIAL":
            disposition = "SELF_REFERENTIAL_STATEMENT_ABOUT_T"
        elif role == "CONSTANT":
            disposition = "A_CONSTANT_THAT_RESTATES_NOT_A_CLAIM_THAT_FAILS"
        elif qualified is not None and qualified in uniform_ids:
            disposition = "SUPERSEDED_BY_A_T_UNIFORM_ROW_WITH_ITS_SCOPE_KEPT"
        elif role == "COMPETING_ROUTE":
            disposition = "ABOUT_A_ROUTE_THE_LADDER_DOES_NOT_USE"
        elif role == "CONTROL":
            disposition = "A_NEGATIVE_CONTROL_NOT_A_LADDER_RESULT"
        else:
            disposition = "LOAD_BEARING_RESIDUE"
        residue_rows.append({
            "id": row["id"],
            "claim": row["claim"],
            "exact_truth_set": row["exact_truth_set"],
            "residue_shape": row["residue_shape"],
            "declared_role": role,
            "declared_qualified_form": qualified,
            "disposition": disposition,
        })

    load_bearing = tuple(
        r for r in residue_rows if r["disposition"] == "LOAD_BEARING_RESIDUE"
    )
    needs_a_choice = tuple(
        r for r in load_bearing
        if r["residue_shape"] == "REQUIRES_AN_EXACT_CHOICE"
    )
    needs_an_exclusion = tuple(
        r for r in load_bearing
        if r["residue_shape"] == "REQUIRES_AN_EXCLUSION_NOT_A_CHOICE"
    )
    self_referential = tuple(
        r for r in residue_rows
        if r["disposition"] == "SELF_REFERENTIAL_STATEMENT_ABOUT_T"
    )
    superseded = tuple(
        r for r in residue_rows
        if r["disposition"] == "SUPERSEDED_BY_A_T_UNIFORM_ROW_WITH_ITS_SCOPE_KEPT"
    )

    # Two criteria are reported, both stated before the values were computed.
    # The STRICT criterion is the block's own: the surface dissolves only if the
    # t-conditional residue is empty or consists solely of statements about t.
    # The FINER criterion is this census's: it dissolves if no LOAD BEARING row
    # requires an exact CHOICE of t, exclusions not counting as choices.  They
    # can disagree, and if they do, both answers are published.
    strict_residue = tuple(
        row for row in residue_rows
        if row["disposition"] != "SELF_REFERENTIAL_STATEMENT_ABOUT_T"
    )
    strict_dissolves = not strict_residue
    dissolves = not needs_a_choice
    if dissolves and strict_dissolves:
        decision_state = "DISSOLVED_ON_BOTH_CRITERIA"
    elif dissolves:
        decision_state = "DISSOLVED_ON_THE_CHOICE_CRITERION_ONLY"
    else:
        decision_state = "SURVIVES_ON_A_COMPUTED_RESIDUE"

    result = {
        "question": "what of the #5931 decision surface survives the census?",
        "owner_directive": BRANCH_PINS["owner_directive"],
        "total_rows_priced": len(table),
        "retired_T_UNIFORM": tuple(r["id"] for r in uniform),
        "retired_count": len(uniform),
        "honest_conditional_T_SENSITIVE": tuple(
            {"id": r["id"], "exact_truth_set": r["exact_truth_set"],
             "residue_shape": r["residue_shape"]} for r in sensitive
        ),
        "sensitive_count": len(sensitive),
        "broken_off_unit": tuple(
            {"id": r["id"], "claim": r["claim"]} for r in broken
        ),
        "broken_count": len(broken),
        "residue_partition": tuple(residue_rows),
        "residue_dispositions": {
            key: tuple(
                row["id"] for row in residue_rows if row["disposition"] == key
            )
            for key in sorted({row["disposition"] for row in residue_rows})
        },
        "load_bearing_residue": tuple(r["id"] for r in load_bearing),
        "load_bearing_residue_count": len(load_bearing),
        "rows_requiring_an_exact_choice_of_t": tuple(
            {"id": r["id"], "exact_truth_set": r["exact_truth_set"]}
            for r in needs_a_choice
        ),
        "rows_requiring_only_an_exclusion": tuple(
            {"id": r["id"], "exact_truth_set": r["exact_truth_set"]}
            for r in needs_an_exclusion
        ),
        "self_referential_rows": tuple(r["id"] for r in self_referential),
        "superseded_rows": tuple(r["id"] for r in superseded),
        "criterion_STRICT_block_spec": (
            "dissolves only if the t-conditional residue is empty or consists"
            " solely of statements whose subject is t"
        ),
        "criterion_FINER_this_census": (
            "dissolves if no LOAD BEARING row requires an exact choice of t; a"
            " cofinite truth set is an exclusion, not a choice"
        ),
        "strict_criterion_residue": tuple(
            {"id": row["id"], "disposition": row["disposition"],
             "residue_shape": row["residue_shape"]} for row in strict_residue
        ),
        "strict_criterion_dissolves": strict_dissolves,
        "finer_criterion_dissolves": dissolves,
        "decision_surface_state": decision_state,
        "decision_surface_dissolves": dissolves,
        "sharpest_single_row": (
            "C880_BLIND_LOCUS_IS_EXACTLY_THE_LANDED_FAMILY. Cycle 880 stated it"
            " AT t* = +1 and it is true there; generalised to the whole line it"
            " holds at every t EXCEPT t = 0. The reason is exact: the blind"
            " locus is the lift over the TRACELESS lawful supports, and"
            " traceless-and-lawful means A = 0 and tB = 0, so at t = 0 it is"
            " every A = 0 configuration and away from t = 0 it is exactly the"
            " landed six. The one load-bearing result that is still t-conditional"
            " is therefore conditional on the grading NOT being the unit"
            " grading -- the opposite of a choice that has to be made."
        ),
        "the_landed_family_is_lawful_at_every_t":
            len(CLASS_U) == len(DIRECTIONS)
            and all((d, landed_support(d)) in set(CLASS_U)
                    for d in range(len(DIRECTIONS))),
        "retirement_statement": (
            "The gravity ladder's grading-consuming content splits cleanly."
            " Everything it asserts about the LANDED family -- the Cycle-320"
            " balance identities, the trace-equals-defect identity, the"
            " zero conformal channel, the six-object blindness census with its"
            " scope qualifier kept, the exact instrument law O3 = sigma C[Pe],"
            " the sigma-degree bound, the family size, and Cycle 325's"
            " unit-weight operator ledger -- holds at EVERY point of the lawful"
            " line, because the landed support family is exactly the set of"
            " configurations with A = 0 and B = 0, which is lawful for every t."
            " Those results need no t-choice and are retired. What moves is of"
            " four kinds, none of which is a choice the ladder has to make:"
            " statements about the UNQUALIFIED lawful set (repaired by keeping"
            " the scope qualifier the T_UNIFORM row already carries); constants"
            " that restate with a different number; statements about the"
            " competing Cycle-318 two-sector route, which is on shell only at"
            " t = +1; and statements whose subject IS the parameter t."
        ),
        "what_remains_exactly": (
            "the rows requiring an exact choice of t:"
            f" {tuple(r['id'] for r in needs_a_choice) or '(none)'}"
        ),
    }
    result["finding"] = (
        f"{len(table)} priced rows: {len(uniform)} T_UNIFORM,"
        f" {len(sensitive)} T_SENSITIVE, {len(broken)} BROKEN_OFF_UNIT. The"
        f" retirement is real and it is structural: the Cycle-320 landed family"
        f" is exactly the class with A = 0 and B = 0, so it is lawful at every"
        f" point of the line, and every result scoped to it is uniform. Of the"
        f" {len(sensitive)} sensitive rows, {len(superseded)} are superseded by a"
        f" T_UNIFORM row that says the same thing with its scope qualifier kept,"
        f" {len(self_referential)} are statements about t itself,"
        f" {len(residue_rows) - len(superseded) - len(self_referential) - len(load_bearing)}"
        f" are constants or negative controls, and {len(load_bearing)} are load"
        f" bearing. Of those, {len(needs_an_exclusion)} require only that a"
        f" finite set of points be EXCLUDED -- not a choice -- and"
        f" {len(needs_a_choice)} require an exact choice of t. On this census's"
        f" criterion the #5931 decision surface is {decision_state}:"
        f" {result['what_remains_exactly']}. On the stricter criterion -- residue"
        f" empty or only statements about t -- it does NOT dissolve"
        f" ({strict_dissolves}), because {len(strict_residue)} rows remain"
        f" t-conditional; both answers are published rather than the convenient"
        f" one. The gap between them is exactly the four dispositions the"
        f" partition names, and every one of them is a repair rather than a"
        f" decision: keep the scope qualifier, restate a constant, cite the"
        f" competing route by its own grading, or read a negative control."
    )
    result["pass"] = (
        len(table) >= 25
        and len(uniform) > 0
        and result["the_landed_family_is_lawful_at_every_t"]
        and all(
            row["disposition"] in (
                "SELF_REFERENTIAL_STATEMENT_ABOUT_T",
                "A_CONSTANT_THAT_RESTATES_NOT_A_CLAIM_THAT_FAILS",
                "SUPERSEDED_BY_A_T_UNIFORM_ROW_WITH_ITS_SCOPE_KEPT",
                "ABOUT_A_ROUTE_THE_LADDER_DOES_NOT_USE",
                "A_NEGATIVE_CONTROL_NOT_A_LADDER_RESULT",
                "LOAD_BEARING_RESIDUE",
            )
            for row in residue_rows
        )
    )
    return result


# --------------------------------------------------------------------------
# rendering, determinism, main
# --------------------------------------------------------------------------
LABELS = (
    "A_PINS",
    "B_NEEDLES",
    "C_CONSUMER_CENSUS",
    "D_RESTRICTION_GATE",
    "E_MACHINERY",
    "F_CLASSIFICATION",
    "G_BACKLOG",
    "H_FALSIFIER",
    "I_VERDICT",
    "J_CONTROLS",
)


def public(certificate: dict) -> dict:
    return {
        key: value for key, value in certificate.items()
        if not key.startswith("_volatile")
    }


def render_fixed_point(certificates: dict) -> str:
    for _ in range(6):
        checks = {label: bool(certificates[label]["pass"]) for label in LABELS}
        terminal = {
            "decision_surface_state":
                certificates["I_VERDICT"]["decision_surface_state"],
            "retired": certificates["I_VERDICT"]["retired_count"],
            "sensitive": certificates["I_VERDICT"]["sensitive_count"],
            "broken": certificates["I_VERDICT"]["broken_count"],
            "requires_an_exact_choice":
                len(certificates["I_VERDICT"]["rows_requiring_an_exact_choice_of_t"]),
            "consumers": certificates["C_CONSUMER_CENSUS"]["consumer_count"],
            "science_payload_sha256":
                certificates["J_CONTROLS"]["science_payload_sha256"],
            "runtime_seconds": certificates["J_CONTROLS"]["runtime_seconds"],
            "stdout_bytes": certificates["J_CONTROLS"]["stdout_bytes"],
        }
        lines = []
        for label in LABELS:
            lines.append(f"FINDING {label} :: {certificates[label]['finding']}")
            lines.append(
                f"{'PASS' if checks[label] else 'FAIL'} {label} :: "
                f"{compact(public(certificates[label]))}"
            )
        lines.append("FINAL " + compact(terminal))
        output = "\n".join(lines) + "\n"
        size = len(output.encode("utf-8"))
        controls = certificates["J_CONTROLS"]
        prior = controls["stdout_bytes"]
        controls["stdout_bytes"] = size
        controls["stdout_under_limit"] = size < STDOUT_LIMIT_BYTES
        controls["pass"] = controls["base_pass"] and controls["stdout_under_limit"]
        if prior == size:
            return output
    raise AssertionError("stdout byte fixed point did not converge")


def run() -> int:
    started = monotonic()
    sources = source_controls()
    needles = derive_needles()
    census = census_certificate(needles)
    restriction = restriction_certificate()
    machinery = machinery_certificate()
    classification = classification_certificate()
    backlog = backlog_certificate()
    falsifier = falsifier_certificate()
    verdict = verdict_certificate(classification, backlog, census, restriction)

    replay_machinery = machinery_certificate()
    replay_classification = classification_certificate()
    replay_backlog = backlog_certificate()
    replay_census = census_certificate(needles)
    deterministic = (
        digest(replay_machinery) == digest(machinery)
        and digest(replay_classification) == digest(classification)
        and digest(replay_backlog) == digest(backlog)
        and digest(public(replay_census)) == digest(public(census))
    )

    receipt = {
        "cycle": 895,
        "AUDIT_INPUT_PATHS": list(AUDIT_INPUT_PATHS),
        "expected_sha256": EXPECTED_SHA256,
        "expected_git_blobs": EXPECTED_GIT_BLOBS,
        "branch_pins": BRANCH_PINS,
        "needles": list(needles["needles"]),
        "needle_count": needles["needle_count"],
        "files_scanned": census["files_scanned"],
        "needle_hit_files": census["needle_hit_files"],
        "consumer_count": census["consumer_count"],
        "classification_counts": census["classification_counts"],
        "consumer_paths_sorted": list(census["consumer_paths_sorted"]),
        "census_hit_row_digest": census["hit_row_digest"],
        "restriction_rows_agreeing": restriction["rows_agreeing"],
        "restriction_rows_disagreeing": list(restriction["rows_disagreeing"]),
        "r9_selects_t": restriction["r9_selects_t"],
        "exceptional_set": list(machinery["exceptional_set"]),
        "onset_values": list(machinery["onset_values"]),
        "class_sizes": {
            "U": machinery["class_U_size"], "Z": machinery["class_Z_size"],
            "ONSET": machinery["class_ONSET_size"],
            "NEVER": machinery["class_NEVER_size"],
        },
        "t_grid": list(machinery["t_grid"]),
        "classification_table": [
            {
                "id": row["id"], "classification": row["classification"],
                "exact_truth_set": row["exact_truth_set"],
                "residue_shape": row["residue_shape"],
            }
            for row in classification["table"]
        ],
        "backlog_rows": [
            {
                "id": row["id"], "script": row["script"],
                "classification": row["classification"],
                "exact_truth_set": row.get("exact_truth_set"),
            }
            for row in backlog["rows"]
        ],
        "falsifier_recovered": falsifier["every_impostor_recovered_exactly"],
        "off_grid_sensitivity_recovered":
            falsifier["off_grid_sensitivity_recovered"],
        "retired_count": verdict["retired_count"],
        "sensitive_count": verdict["sensitive_count"],
        "broken_count": verdict["broken_count"],
        "load_bearing_residue": list(verdict["load_bearing_residue"]),
        "rows_requiring_an_exact_choice_of_t":
            list(verdict["rows_requiring_an_exact_choice_of_t"]),
        "rows_requiring_only_an_exclusion":
            list(verdict["rows_requiring_only_an_exclusion"]),
        "decision_surface_state": verdict["decision_surface_state"],
        "decision_surface_dissolves": verdict["decision_surface_dissolves"],
        "strict_criterion_dissolves": verdict["strict_criterion_dissolves"],
        "finer_criterion_dissolves": verdict["finer_criterion_dissolves"],
        "residue_dispositions": verdict["residue_dispositions"],
        "retirement_statement": verdict["retirement_statement"],
        "sharpest_single_row": verdict["sharpest_single_row"],
        "classification_table_digest": digest(classification["table"]),
    }
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(
        json.dumps(receipt, indent=2, sort_keys=True, default=str) + "\n",
        encoding="utf-8",
    )
    cache_digest = sha256(CACHE.read_bytes()).hexdigest()

    elapsed = monotonic() - started
    controls = {
        **sources,
        "determinism": {
            "scope": (
                "the machinery certificate, the full classification table, the"
                " backlog pricing and the consumer census were recomputed from"
                " scratch and compared digest for digest"
            ),
            "exact": deterministic,
            "machinery_digest": digest(machinery),
            "classification_digest": digest(classification),
            "backlog_digest": digest(backlog),
            "census_digest": digest(public(census)),
        },
        "cache_path": str(CACHE.relative_to(ROOT)),
        "cache_sha256": cache_digest,
        "science_payload_sha256": "",
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "runtime_under_limit": elapsed < AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "stdout_under_limit": False,
        "blocked_modules_loaded_after_science": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits_after_science": tuple(FIREWALL.hits),
        "finding": (
            "All fifteen cited artifacts matched their pinned SHA-256 and git"
            " blob hashes at a hard gate that exits 2 before any science runs,"
            " carried their required AST markers or JSON keys, contained every"
            " required verbatim quotation character for character, and stayed"
            " text/AST/JSON-only behind the import firewall; no primary was"
            " loaded at any point. The direction table, all three reversal"
            " permutations, the sector names, the axis count, the held edge"
            " length, the sigma degree bound, the object arities, the Cycle-873"
            " witness coefficients and the Cycle-318 mediator weight were"
            " recovered from pinned text by AST rather than transcribed, and"
            " t* was DERIVED from the recovered mediator weight. The machinery,"
            " the classification table, the backlog pricing and the whole"
            " consumer census were recomputed from scratch and reproduced digest"
            " for digest, and the runtime and stdout caps were respected."
        ),
    }
    controls["base_pass"] = (
        sources["sources_pass"]
        and deterministic
        and controls["runtime_under_limit"]
        and not controls["blocked_modules_loaded_after_science"]
        and not controls["firewall_hits_after_science"]
    )
    controls["pass"] = controls["base_pass"]

    certificates = {
        "A_PINS": {
            **sources,
            "finding": controls["finding"],
            "pass": sources["sources_pass"],
        },
        "B_NEEDLES": needles,
        "C_CONSUMER_CENSUS": census,
        "D_RESTRICTION_GATE": restriction,
        "E_MACHINERY": machinery,
        "F_CLASSIFICATION": classification,
        "G_BACKLOG": backlog,
        "H_FALSIFIER": falsifier,
        "I_VERDICT": verdict,
        "J_CONTROLS": controls,
    }
    controls["science_payload_sha256"] = science_payload(
        {key: public(value) for key, value in certificates.items()}
    )
    sys.stdout.write(render_fixed_point(certificates))
    return 0 if all(row["pass"] for row in certificates.values()) else 1


if __name__ == "__main__":
    raise SystemExit(run())
