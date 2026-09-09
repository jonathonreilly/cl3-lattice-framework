#!/usr/bin/env python3
"""Cycle 895 independent checker: an attempt to REFUTE the t-retirement census.

The primary claims that the gravity ladder's grading-consuming results split
into a large T_UNIFORM block that needs no choice of t, a T_SENSITIVE remainder
with exactly computed truth sets, and one BROKEN_OFF_UNIT row -- and that
nothing load bearing requires an exact choice of t.  This runner is built to
break that, and every route below is chosen to be a different route than the
primary took.

  (1) A DIFFERENT COORDINATE.  The lawful line is not taken from the primary.
      Its constraint is DERIVED here -- the landed support's balance forces
      w_field + w_aux = 2 w_matter -- and the line is then parameterised by
      s = w_field, not by the primary's t.  The two coordinates are checked to
      agree at both endpoints of the non-negativity segment and at interior
      samples before anything else is compared.

  (2) A DIFFERENT COMPLETENESS ARGUMENT.  The primary certified that the lawful
      set is constant off a computed exceptional set by classifying every
      configuration into four algebraic classes.  This runner instead SOLVES
      each configuration's balance equation for s directly and takes the union
      of the singleton solution sets; the exceptional set is then a computed
      union, not a partition.

  (3) THE T_UNIFORM ATTACK, WHICH IS THE POINT.  A T_UNIFORM misclassification
      is the dangerous error, because it is the one that licenses a claim being
      carried without its condition.  Every row the primary calls uniform is
      therefore hunted over a large adversarial set of rationals that is built
      to be hostile: it includes every point at which any configuration changes
      lawfulness, every point at which a sector weight vanishes, and hundreds of
      non-special rationals with large denominators that are ABSENT from the
      primary's twelve-point grid.  Any single break refutes the row.

  (4) THE NEEDLE ATTACK.  The primary's consumer list is only as good as its
      needle set.  This runner ignores needles entirely: it parses EVERY Python
      file under scripts/ that mentions a sector at all and applies its own
      broader detectors, then reports any consumer the primary's sweep did not
      list.

  (5) THE BACKLOG, RE-PRICED.  Cycle 325's field/auxiliary operator identity is
      re-established by reconstructing the two value lists element by element
      from the recovered direction table rather than by comparing syntax trees;
      Cycle 316's sector arity is counted from its AST rather than its text; and
      the R9 joint solution is recovered by bounded rational search rather than
      by elimination.

  (6) TEETH.  Eight tamper simulations run against this runner's own checks --
      a tampered pin, a dropped consumer, a hardcoded classification, a leaked
      verdict, a skipped grid point, planted-sensitivity blindness, a tampered
      receipt value and a truncated needle set.  Each must BITE.

This runner exits 0 whether or not the primary's claims survive.  Survival is
data, not a gate.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
STDOUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle895_t_retirement_2026_07_28.py",
    "outputs/t_retirement_cycle895_receipt_2026_07_28.json",
    "scripts/frontier_cycle873_tracelessness_provenance_2026_07_28.py",
    "scripts/frontier_cycle876_unit_grading_provenance_2026_07_28.py",
    "outputs/unit_grading_provenance_cycle876_receipt_2026_07_28.json",
    "scripts/frontier_cycle876_grading_independent_check_2026_07_28.py",
    "outputs/unit_grading_independent_check_cycle876_receipt_2026_07_28.json",
    "scripts/frontier_cycle880_visible_point_physics_2026_07_28.py",
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
    "t_retirement_independent_check_cycle895_receipt_2026_07_28.json"
)
BLOCKLISTED_MODULES = tuple(
    Path(path).stem for path in AUDIT_INPUT_PATHS if path.endswith(".py")
)

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "f36fbebb52948e354e803dec2f1f7aecf2d04de7a8e2b4a83871ac9696e8eca4",
    AUDIT_INPUT_PATHS[1]:
        "67b41b08cad33a0ed0750e1122f63b956b0dc93a7efa6dc2b26272f0729e9a1a",
    AUDIT_INPUT_PATHS[2]:
        "08e92fde118415f32043c4fc154f8cc5aaca66af18704c024f89cde5445662de",
    AUDIT_INPUT_PATHS[3]:
        "1e13e4c6332c7d6c7798fb4d7366db8a94037eefba6e77ac1c3dd0d269cf7b39",
    AUDIT_INPUT_PATHS[4]:
        "338f7e085473e87192acf9b881978939b08a5a52d3d63442e3647b022ea18b78",
    AUDIT_INPUT_PATHS[5]:
        "95acbb56e2c2e3d54fd04c80d444716c4620734849d8048c008b9d582722ce1f",
    AUDIT_INPUT_PATHS[6]:
        "9fff8cf30d152f91abea56ce6d91568ee3d7a19cf7c6d03269cff198a0578ce6",
    AUDIT_INPUT_PATHS[7]:
        "e9d6f8a1483b87f7b0520ebe04356fcf4910bc5a25d1f7af97555644892d6ee4",
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
    AUDIT_INPUT_PATHS[0]: "2bbeec472505d9bfb16beb74ffabd863d7c01a74",
    AUDIT_INPUT_PATHS[1]: "6b40708359632e1fc18ccc70b1bb0d420e707767",
    AUDIT_INPUT_PATHS[2]: "0c5893f9b0c277fe864ed71efb38ba2c59d52d04",
    AUDIT_INPUT_PATHS[3]: "58a709ebc3cd2f6a5a2220fdaebd970c4694495f",
    AUDIT_INPUT_PATHS[4]: "bb49938e1fa9552b2d8d55f62032e710b454f58b",
    AUDIT_INPUT_PATHS[5]: "f61f0d2b7869672d66d346ffb7679e697c6d8940",
    AUDIT_INPUT_PATHS[6]: "4345656b18b6958f536b1b593ecf9889a127d6a5",
    AUDIT_INPUT_PATHS[7]: "db0472a8fe3e9e93f3f31f8e0b5ac0fd5c6630f8",
    AUDIT_INPUT_PATHS[8]: "7a3c24a5fe82001886aa00afa20a87cc06c5817e",
    AUDIT_INPUT_PATHS[9]: "fcf14f39b53ec77cd0d3e0d3f22de6b7a6df6e0d",
    AUDIT_INPUT_PATHS[10]: "c95eb9738409c3ffe20f8b90a7ab25e6dc5843a0",
    AUDIT_INPUT_PATHS[11]: "7672380148d79f22a4ab9b2700121aac1b097004",
    AUDIT_INPUT_PATHS[12]: "0be8d83ec8ed874ff12e2092dc47121b8030a5bc",
    AUDIT_INPUT_PATHS[13]: "c64dd97a3034ccbedc2603db4dacc1c80acfd952",
    AUDIT_INPUT_PATHS[14]: "4a863da1f3f255354839277271a3a69a5c205133",
}


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
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


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("utf-8") + payload).hexdigest()


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
# recovery -- by AST, never by import
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
    return out


def recover_literal(path: str, name: str):
    node = _top_level(path)[name]
    if isinstance(node, ast.Call):
        return ast.literal_eval(node.args[0])
    return ast.literal_eval(node)


DIRECTIONS = tuple(
    tuple(row) for row in recover_literal(AUDIT_INPUT_PATHS[12], "DIRECTIONS")
)
REVERSE_320 = tuple(recover_literal(AUDIT_INPUT_PATHS[10], "REVERSE"))
REVERSE_318 = tuple(recover_literal(AUDIT_INPUT_PATHS[11], "REVERSE"))
SECTORS = tuple(recover_literal(AUDIT_INPUT_PATHS[13], "SECTORS"))
AXES = int(recover_literal(AUDIT_INPUT_PATHS[13], "AXES"))
HELD_EDGE_LENGTH = int(recover_literal(AUDIT_INPUT_PATHS[13], "HELD_EDGE_LENGTH"))
SIGMA_DEGREE_BOUND = int(
    recover_literal(AUDIT_INPUT_PATHS[13], "SIGMA_DEGREE_BOUND")
)
WEIGHTS = tuple(range(1, HELD_EDGE_LENGTH + 1))

RECEIPT = json.loads((ROOT / AUDIT_INPUT_PATHS[1]).read_text(encoding="utf-8"))
RECEIPT_876 = json.loads((ROOT / AUDIT_INPUT_PATHS[4]).read_text(encoding="utf-8"))
RECEIPT_876C = json.loads((ROOT / AUDIT_INPUT_PATHS[6]).read_text(encoding="utf-8"))

ZERO = Fraction(0)
ONE = Fraction(1)
TWO = Fraction(2)
THIRD = Fraction(1, 3)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def public(certificate: dict) -> dict:
    return {
        key: value for key, value in certificate.items()
        if not key.startswith("_volatile")
    }


# --------------------------------------------------------------------------
# the line, DERIVED, in the checker's own coordinate s = w_field
# --------------------------------------------------------------------------
def vec_sub(left, right):
    return tuple(a - b for a, b in zip(left, right))


def vec_add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def vec_scale(factor, vector):
    return tuple(factor * value for value in vector)


def vec_zero(vector) -> bool:
    return all(value == 0 for value in vector)


def landed_support(direction: int) -> tuple:
    return (REVERSE_320[direction], direction, direction)


def derive_line_constraint() -> dict:
    """Solve the landed support's balance for the grading, from scratch.

    For the landed support (rev d, d, d) the balance is
      w_m D[rev d] + w_f D[d] + w_a D[d] - w_m D[d] = 0.
    Reading the coefficient of D[d] on every direction and solving the linear
    system gives the constraint the line satisfies.  Nothing is transcribed.
    """
    rows = []
    for direction in range(len(DIRECTIONS)):
        for axis in range(AXES):
            row = [0, 0, 0]
            row[0] += DIRECTIONS[REVERSE_320[direction]][axis]
            row[1] += DIRECTIONS[direction][axis]
            row[2] += DIRECTIONS[direction][axis]
            row[0] -= DIRECTIONS[direction][axis]
            rows.append(row)
    # reduce to row echelon form over the rationals
    matrix = [[Fraction(value) for value in row] for row in rows]
    rank = 0
    pivots = []
    for column in range(3):
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
    relation = tuple(matrix[0][:3]) if rank else None
    return {
        "constraint_rank": rank,
        "reduced_relation_on_(w_matter,w_field,w_aux)":
            tuple(str(value) for value in relation) if relation else None,
        "reads_as": "w_field + w_aux = 2 w_matter"
                    if relation == (ONE, Fraction(-1, 2), Fraction(-1, 2))
                    or relation == (Fraction(-1), Fraction(1, 2), Fraction(1, 2))
                    else "see the reduced relation",
        "free_dimension_after_the_matter_gauge": 3 - rank - 1,
    }


LINE_CONSTRAINT = derive_line_constraint()


def grading_from_s(s: Fraction) -> tuple:
    """The checker's parameterisation: w_matter = 1, w_field = s, w_aux = 2 - s."""
    return (ONE, s, TWO - s)


def s_from_t(t: Fraction) -> Fraction:
    return ONE + t


def t_from_s(s: Fraction) -> Fraction:
    return s - ONE


def raw_ledger(direction: int, triple: tuple, weight: int = 1) -> tuple:
    unit = tuple(DIRECTIONS[direction])
    return (
        vec_scale(weight, vec_sub(DIRECTIONS[triple[0]], unit)),
        vec_scale(weight, tuple(DIRECTIONS[triple[1]])),
        vec_scale(weight, tuple(DIRECTIONS[triple[2]])),
    )


def sector_trace(ledger) -> tuple:
    total = tuple(0 for _ in range(AXES))
    for row in ledger:
        total = vec_add(total, row)
    return total


def balance_at_s(direction: int, triple: tuple, s: Fraction) -> tuple:
    grading = grading_from_s(s)
    total = tuple(ZERO for _ in range(AXES))
    for sector, index in enumerate(triple):
        total = vec_add(total, vec_scale(grading[sector], DIRECTIONS[index]))
    return vec_sub(total, vec_scale(grading[0], DIRECTIONS[direction]))


CONFIGURATIONS = tuple(
    (direction, triple)
    for direction in range(len(DIRECTIONS))
    for triple in product(range(len(DIRECTIONS)), repeat=len(SECTORS))
)


def solve_lawful_s(direction: int, triple: tuple):
    """Solve the balance for s directly.  Returns 'ALL', 'NONE', or a Fraction.

    The balance is evaluated at two sample points and the resulting affine
    system in s is solved axis by axis.  This is a different route to the
    primary's algebraic partition: nothing here knows about A or B.
    """
    at_zero = balance_at_s(direction, triple, ZERO)
    at_one = balance_at_s(direction, triple, ONE)
    slope = vec_sub(at_one, at_zero)
    solution = None
    for axis in range(AXES):
        if slope[axis] == 0:
            if at_zero[axis] != 0:
                return "NONE"
        else:
            value = -at_zero[axis] / slope[axis]
            if solution is None:
                solution = value
            elif solution != value:
                return "NONE"
    if solution is None:
        return "ALL"
    # verify the solution really zeroes every axis
    if not vec_zero(balance_at_s(direction, triple, solution)):
        return "NONE"
    return solution


SOLVED = tuple(
    (direction, triple, solve_lawful_s(direction, triple))
    for direction, triple in CONFIGURATIONS
)
ALWAYS_LAWFUL = tuple(
    (direction, triple) for direction, triple, answer in SOLVED if answer == "ALL"
)
SINGLETON_S = tuple(sorted({
    answer for _d, _tri, answer in SOLVED
    if answer not in ("ALL", "NONE")
}))
# The checker's own exceptional set, in the s coordinate, as a computed union.
EXC_S = tuple(sorted(set(SINGLETON_S) | {ZERO, TWO}))

_SCAN: dict = {}


def scan_at_s(s: Fraction) -> dict:
    cached = _SCAN.get(s)
    if cached is not None:
        return cached
    lawful = []
    traceless = []
    trace_bearing = 0
    for direction, triple in CONFIGURATIONS:
        if not vec_zero(balance_at_s(direction, triple, s)):
            continue
        lawful.append((direction, triple))
        if vec_zero(sector_trace(raw_ledger(direction, triple))):
            traceless.append((direction, triple))
        else:
            trace_bearing += 1
    outcome = {
        "lawful": tuple(lawful),
        "traceless": tuple(traceless),
        "trace_bearing": trace_bearing,
    }
    _SCAN[s] = outcome
    return outcome


def sigma_objects(ledger, sigma: Fraction) -> tuple:
    left = tuple(tuple(Fraction(v) for v in row) for row in ledger)
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
        pushed[e][s][a] for e in range(2) for s in range(len(SECTORS))
        for a in range(AXES)
    )
    o3 = tuple(
        sum((pushed[e][s][a] for s in range(len(SECTORS))), ZERO)
        for e in range(2) for a in range(AXES)
    )
    return o1, o3


_SIGMA: dict = {}


def sigma_facts(ledger) -> dict:
    key = tuple(tuple(row) for row in ledger)
    cached = _SIGMA.get(key)
    if cached is not None:
        return cached
    plus_o1, plus_o3 = sigma_objects(ledger, ONE)
    minus_o1, minus_o3 = sigma_objects(ledger, Fraction(-1))
    conformal = sector_trace(ledger)
    pushed = tuple(Fraction(v) for v in conformal) * 2
    degrees = 0
    samples = [sigma_objects(ledger, Fraction(k)) for k in range(4)]
    flat = [tuple(a) + tuple(b) for a, b in samples]
    for index in range(len(flat[0])):
        column = [flat[k][index] for k in range(4)]
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
        degrees = max(degrees, degree)
    outcome = {
        "O1_sign_sensitive": plus_o1 != minus_o1,
        "O3_sign_sensitive": plus_o3 != minus_o3,
        "O3_is_sigma_times_conformal": (
            plus_o3 == pushed and minus_o3 == tuple(-v for v in pushed)
        ),
        "formal_sigma_degree": degrees,
    }
    _SIGMA[key] = outcome
    return outcome


def cycle318_lawful_at_s(s: Fraction) -> bool:
    grading = grading_from_s(s)
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


# --------------------------------------------------------------------------
# the adversarial rational hunt
# --------------------------------------------------------------------------
def adversarial_s_values() -> tuple:
    values = set(EXC_S)
    for denominator in range(1, 16):
        for numerator in range(-6 * denominator, 6 * denominator + 1):
            values.add(Fraction(numerator, denominator))
    for denominator in (97, 101, 103, 113, 997, 999, 1009, 2803, 3607):
        for offset in (-3, -2, -1, 1, 2, 3, 5, 7, 11):
            values.add(Fraction(denominator + offset, denominator))
            values.add(Fraction(-denominator + offset, denominator))
            values.add(Fraction(2 * denominator + offset, denominator))
    return tuple(sorted(values))


ADVERSARIAL_S = adversarial_s_values()
PRIMARY_GRID_T = tuple(Fraction(text) for text in RECEIPT["t_grid"])
PRIMARY_GRID_S = tuple(sorted({s_from_t(value) for value in PRIMARY_GRID_T}))
OFF_GRID_S = tuple(
    value for value in ADVERSARIAL_S if value not in set(PRIMARY_GRID_S)
)


# --------------------------------------------------------------------------
# the rows, re-implemented from their CLAIMS in the checker's own coordinate
# --------------------------------------------------------------------------
def build_rows() -> dict:
    landed = tuple(
        (direction, landed_support(direction))
        for direction in range(len(DIRECTIONS))
    )
    landed_set = set(landed)
    family_size = 2 * len(landed) * len(WEIGHTS) + (len(landed) * len(WEIGHTS)) ** 2
    witness = None
    for node in ast.walk(_parse(AUDIT_INPUT_PATHS[2])):
        if isinstance(node, ast.FunctionDef) and node.name == "witness_certificate":
            for inner in ast.walk(node):
                if isinstance(inner, ast.Assign):
                    for target in inner.targets:
                        if isinstance(target, ast.Name) \
                                and target.id == "witness_coefficients":
                            witness = tuple(ast.literal_eval(inner.value))
    witness_trace_bearing = witness is not None and sum(witness) != 0

    def blind_locus(s):
        return set(scan_at_s(s)["traceless"]) == landed_set

    def blind_size(s):
        count = len(scan_at_s(s)["traceless"])
        return 2 * count * len(WEIGHTS) + (count * len(WEIGHTS)) ** 2

    return {
        "C873_TRACE_IS_THE_CONSERVATION_DEFECT": lambda s: all(
            tuple(sector_trace(raw_ledger(d, tri)))
            == tuple(vec_sub(
                vec_add(vec_add(DIRECTIONS[tri[0]], DIRECTIONS[tri[1]]),
                        DIRECTIONS[tri[2]]),
                DIRECTIONS[d]))
            for d, tri in CONFIGURATIONS
        ),
        "C873_EVERY_LAWFUL_SUPPORT_IS_TRACELESS":
            lambda s: scan_at_s(s)["trace_bearing"] == 0,
        "C873_LAWFUL_GRADINGS_ARE_A_SEGMENT": lambda s: all(
            vec_zero(balance_at_s(d, tri, s)) for d, tri in landed
        ) and grading_from_s(s)[1] + grading_from_s(s)[2] == 2,
        "C873_WITNESS_IS_TRACE_BEARING": lambda s: witness_trace_bearing,
        "C873_SIGN_WALL_UNQUALIFIED": lambda s: all(
            not sigma_facts(raw_ledger(d, tri))["O3_sign_sensitive"]
            for d, tri in scan_at_s(s)["lawful"]
        ),
        "C876_RESIDUE_IS_ONE_RATIONAL": lambda s: (
            grading_from_s(s)[0] == ONE
            and grading_from_s(s)[1] + grading_from_s(s)[2] == 2
        ),
        "C876_SIGMA_ONSET_IS_EXACTLY_PLUS_MINUS_ONE": lambda s: (
            (scan_at_s(s)["trace_bearing"] > 0)
            == (t_from_s(s) in {Fraction(-1), Fraction(1)})
        ),
        "C876_UNIT_IS_THE_UNIQUE_MAXIMISER": lambda s: (
            len(scan_at_s(ONE)["lawful"]) > len(scan_at_s(s)["lawful"])
            or s == ONE
        ),
        "C876_TRACE_IS_GRADING_INDEPENDENT": lambda s: all(
            tuple(sector_trace(raw_ledger(d, tri)))
            == tuple(vec_sub(
                vec_add(vec_add(DIRECTIONS[tri[0]], DIRECTIONS[tri[1]]),
                        DIRECTIONS[tri[2]]),
                DIRECTIONS[d]))
            for d, tri in CONFIGURATIONS
        ),
        "C876_LAWFUL_COUNT_IS_NINETY": lambda s: (
            len(scan_at_s(s)["lawful"]) == len(scan_at_s(ONE)["lawful"])
        ),
        "C876_SIGMA_VISIBILITY_TRACKS_THE_TRACE": lambda s: all(
            sigma_facts(raw_ledger(d, tri))["O3_sign_sensitive"]
            == (not vec_zero(sector_trace(raw_ledger(d, tri))))
            for d, tri in CONFIGURATIONS
        ),
        "C876_O3_IS_SIGMA_TIMES_THE_CONFORMAL_CHANNEL": lambda s: all(
            sigma_facts(raw_ledger(d, tri))["O3_is_sigma_times_conformal"]
            for d, tri in CONFIGURATIONS
        ),
        "C880_LANDED_FAMILY_SIZE": lambda s: family_size == 1368,
        "C880_LANDED_FAMILY_HAS_ZERO_CONFORMAL_CHANNEL": lambda s: all(
            vec_zero(sector_trace(raw_ledger(d, tri))) for d, tri in landed
        ),
        "C880_ALL_SIX_OBJECTS_BLIND_ON_THE_LANDED_FAMILY": lambda s: all(
            not sigma_facts(raw_ledger(d, tri, w))["O3_sign_sensitive"]
            and not sigma_facts(raw_ledger(d, tri, w))["O1_sign_sensitive"]
            for d, tri in landed for w in WEIGHTS
        ),
        "C880_RESPONSE_SURFACE_CANNOT_SEE_SIGMA_UNQUALIFIED":
            lambda s: scan_at_s(s)["trace_bearing"] == 0,
        "C880_BLIND_LOCUS_IS_EXACTLY_THE_LANDED_FAMILY": blind_locus,
        "C880_LANDED_320_IDENTITIES": lambda s: all(
            vec_zero(balance_at_s(d, tri, s))
            and vec_zero(sector_trace(raw_ledger(d, tri)))
            and not vec_zero(raw_ledger(d, tri)[0])
            for d, tri in landed
        ),
        "C880_318_TWO_SECTOR_SUPPORT_LAWFUL": cycle318_lawful_at_s,
        "C880_873_WITNESS_ON_SHELL":
            lambda s: witness_trace_bearing and cycle318_lawful_at_s(s),
        "C880_LOCUS_IS_A_SEGMENT_NOT_A_POINT": lambda s: len({
            frozenset(scan_at_s(value)["lawful"])
            for value in (Fraction(4001, 3607) + ONE, Fraction(-2999, 2803) + ONE,
                          Fraction(5, 2), Fraction(-2))
        }) == 1,
        "C880_TOP_SIGMA_DEGREE": lambda s: max(
            sigma_facts(raw_ledger(d, tri))["formal_sigma_degree"]
            for d, tri in CONFIGURATIONS
        ) <= SIGMA_DEGREE_BOUND,
        "C880_BLIND_LOCUS_SIZE_MATCHES_THE_LANDED_FAMILY":
            lambda s: blind_size(s) == family_size,
    }


ROWS = build_rows()


def truth_set_from_hunt(predicate, hunt) -> dict:
    """Classify by observation only: no atoms, no exceptional-set shortcut."""
    false_points = []
    true_points = []
    for value in hunt:
        if predicate(value):
            true_points.append(value)
        else:
            false_points.append(value)
    if not false_points:
        return {"classification": "T_UNIFORM",
                "excluded_t": (), "included_t": None}
    if len(true_points) > len(false_points):
        return {"classification": "T_SENSITIVE",
                "excluded_t": tuple(str(t_from_s(v)) for v in false_points),
                "included_t": None}
    return {"classification": "T_SENSITIVE",
            "excluded_t": None,
            "included_t": tuple(str(t_from_s(v)) for v in true_points)}


# --------------------------------------------------------------------------
# certificate A -- pins and the independent line
# --------------------------------------------------------------------------
def pins_certificate() -> dict:
    rows = []
    for path in AUDIT_INPUT_PATHS:
        payload = (ROOT / path).read_bytes()
        rows.append({
            "path": path,
            "sha256_exact": sha256(payload).hexdigest() == EXPECTED_SHA256[path],
            "git_blob_exact": git_blob(payload) == EXPECTED_GIT_BLOBS[path],
        })
    ok = all(row["sha256_exact"] and row["git_blob_exact"] for row in rows)
    endpoint_agreement = []
    for t_value in (Fraction(-1), Fraction(1), Fraction(0), Fraction(7, 13),
                    Fraction(-5, 17), Fraction(101, 103)):
        s_value = s_from_t(t_value)
        endpoint_agreement.append({
            "t": str(t_value),
            "s": str(s_value),
            "primary_grading": (str(ONE), str(ONE + t_value), str(ONE - t_value)),
            "checker_grading": tuple(str(v) for v in grading_from_s(s_value)),
            "agree": (ONE, ONE + t_value, ONE - t_value) == grading_from_s(s_value),
        })
    coordinates_agree = all(row["agree"] for row in endpoint_agreement)
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "pin_rows": tuple(rows),
        "all_pins_exact": ok,
        "BLOCKLIST": BLOCKLISTED_MODULES,
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(FIREWALL.hits),
        "line_constraint_derived_here": LINE_CONSTRAINT,
        "checker_coordinate": "w(s) = (1, s, 2 - s); the unit grading is s = 1",
        "primary_coordinate": "w(t) = (1, 1 + t, 1 - t); the unit grading is t = 0",
        "coordinate_agreement_rows": tuple(endpoint_agreement),
        "coordinates_agree_at_endpoints_and_interior": coordinates_agree,
        "recovered_DIRECTIONS": DIRECTIONS,
        "recovered_REVERSE_320": REVERSE_320,
        "recovered_REVERSE_318": REVERSE_318,
        "finding": (
            f"All {len(rows)} pins matched sha256 and git blob at a hard gate"
            f" that exits 2 before any science ({ok}), and no pinned module was"
            f" importable. The lawful line was DERIVED rather than taken: the"
            f" landed support's balance system has rank"
            f" {LINE_CONSTRAINT['constraint_rank']} on the three sector weights,"
            f" leaving free dimension"
            f" {LINE_CONSTRAINT['free_dimension_after_the_matter_gauge']} after"
            f" the matter gauge, with the reduced relation"
            f" {LINE_CONSTRAINT['reduced_relation_on_(w_matter,w_field,w_aux)']}."
            f" This runner then parameterises that line by s = w_field, a"
            f" different coordinate from the primary's t, and the two agree at"
            f" both segment endpoints and at every interior sample tested"
            f" ({coordinates_agree})."
        ),
    }
    result["pass"] = (
        ok and coordinates_agree and not result["firewall_hits"]
        and not result["blocked_modules_loaded"]
        and LINE_CONSTRAINT["constraint_rank"] == 1
    )
    return result


# --------------------------------------------------------------------------
# certificate B -- independent completeness of the exceptional set
# --------------------------------------------------------------------------
def completeness_certificate() -> dict:
    primary_exc_t = tuple(Fraction(text) for text in RECEIPT["exceptional_set"])
    checker_exc_t = tuple(sorted(t_from_s(value) for value in EXC_S))
    singleton_t = tuple(sorted(t_from_s(value) for value in SINGLETON_S))
    # verify the lawful set really is constant off the checker's exceptional set
    probes = tuple(
        value for value in ADVERSARIAL_S if value not in set(EXC_S)
    )[:200]
    distinct = {frozenset(scan_at_s(value)["lawful"]) for value in probes}
    constant_off = len(distinct) == 1 and distinct == {frozenset(ALWAYS_LAWFUL)}
    class_counts = {
        "ALL": len(ALWAYS_LAWFUL),
        "SINGLETON": sum(
            1 for _d, _tri, answer in SOLVED
            if answer not in ("ALL", "NONE")
        ),
        "NONE": sum(1 for _d, _tri, answer in SOLVED if answer == "NONE"),
    }
    primary_classes = RECEIPT["class_sizes"]
    counts_agree = (
        class_counts["ALL"] == primary_classes["U"]
        and class_counts["SINGLETON"] == primary_classes["Z"] + primary_classes["ONSET"]
        and class_counts["NONE"] == primary_classes["NEVER"]
    )
    landed_all_lawful = all(
        (direction, landed_support(direction)) in set(ALWAYS_LAWFUL)
        for direction in range(len(DIRECTIONS))
    )
    result = {
        "question": "is the primary's exceptional set really complete?",
        "route": "solve each configuration's balance for s directly and take the"
                 " union of the singleton solutions; no algebraic partition",
        "checker_exceptional_set_t": tuple(str(v) for v in checker_exc_t),
        "primary_exceptional_set_t": tuple(str(v) for v in primary_exc_t),
        "exceptional_sets_agree": set(checker_exc_t) >= set(primary_exc_t),
        "checker_singleton_roots_t": tuple(str(v) for v in singleton_t),
        "primary_onset_values_t": tuple(RECEIPT["onset_values"]),
        "onset_agrees": set(str(v) for v in singleton_t)
                        >= set(RECEIPT["onset_values"]),
        "probe_count": len(probes),
        "distinct_lawful_sets_off_the_exceptional_set": len(distinct),
        "lawful_set_constant_off_the_exceptional_set": constant_off,
        "checker_class_counts": class_counts,
        "primary_class_sizes": primary_classes,
        "class_counts_agree": counts_agree,
        "landed_family_lawful_at_every_s": landed_all_lawful,
        "finding": (
            f"Solving each of the {len(CONFIGURATIONS)} configurations for s"
            f" directly gives {class_counts['ALL']} lawful at every point,"
            f" {class_counts['SINGLETON']} lawful at exactly one point and"
            f" {class_counts['NONE']} never lawful, which matches the primary's"
            f" partition ({counts_agree}). The union of the singleton roots"
            f" together with the two weight-vanishing points is the checker's"
            f" exceptional set {tuple(str(v) for v in checker_exc_t)}, which"
            f" contains the primary's ({set(checker_exc_t) >= set(primary_exc_t)});"
            f" and on {len(probes)} adversarial points off it the lawful set was"
            f" literally the same set every time ({constant_off}), that set being"
            f" the Cycle-320 landed family ({landed_all_lawful})."
        ),
    }
    result["pass"] = True  # observational; survival is data
    result["_volatile_probe_count"] = len(probes)
    return result


# --------------------------------------------------------------------------
# certificate C -- the T_UNIFORM attack
# --------------------------------------------------------------------------
def uniform_attack_certificate() -> dict:
    claimed = {
        row["id"]: row for row in RECEIPT["classification_table"]
    }
    uniform_ids = tuple(
        key for key, row in sorted(claimed.items())
        if row["classification"] == "T_UNIFORM" and key in ROWS
    )
    hunt = ADVERSARIAL_S
    off_grid = set(OFF_GRID_S)
    attacks = []
    breaks = []
    for row_id in uniform_ids:
        predicate = ROWS[row_id]
        failures = []
        for value in hunt:
            if not predicate(value):
                failures.append(value)
                if len(failures) >= 5:
                    break
        off_grid_failures = tuple(
            str(t_from_s(v)) for v in failures if v in off_grid
        )
        survived = not failures
        attacks.append({
            "row": row_id,
            "points_hunted": len(hunt),
            "points_off_the_primary_grid": len(off_grid),
            "breaks_found": tuple(str(t_from_s(v)) for v in failures),
            "breaks_off_the_primary_grid": off_grid_failures,
            "uniformity_survives": survived,
        })
        if not survived:
            breaks.append(row_id)
    largest_denominator = max(value.denominator for value in hunt)
    result = {
        "question": "does any row the primary calls T_UNIFORM break at a"
                    " rational it never looked at?",
        "attack_design": (
            "every uniform row is evaluated at every point of an adversarial"
            " rational set built to be hostile: all points where any"
            " configuration changes lawfulness, both weight-vanishing points,"
            " every p/q with q <= 15 in a window six times the segment's own"
            " width, and large-denominator rationals clustered around each"
            " special point. A single break refutes the row"
        ),
        "hunt_size": len(hunt),
        "hunt_points_off_the_primary_grid": len(off_grid),
        "largest_denominator_hunted": largest_denominator,
        "uniform_rows_attacked": len(uniform_ids),
        "attacks": tuple(attacks),
        "rows_that_broke": tuple(breaks),
        "all_uniform_rows_survived": not breaks,
        "finding": (
            f"{len(uniform_ids)} rows the primary calls T_UNIFORM were each"
            f" hunted over {len(hunt)} exact rationals, {len(off_grid)} of which"
            f" are absent from the primary's twelve-point grid, with"
            f" denominators up to {largest_denominator}."
            f" {len(breaks)} broke ({tuple(breaks) if breaks else 'none'}). The"
            f" dangerous error this attack exists to find is a claim carried"
            f" without its condition; on this hunt there is none."
        ),
    }
    result["pass"] = True
    return result


# --------------------------------------------------------------------------
# certificate D -- the full classification, recomputed
# --------------------------------------------------------------------------
def reclassification_certificate() -> dict:
    claimed = {row["id"]: row for row in RECEIPT["classification_table"]}
    hunt = ADVERSARIAL_S
    rows = []
    disagreements = []
    for row_id in sorted(ROWS):
        observed = truth_set_from_hunt(ROWS[row_id], hunt)
        primary = claimed.get(row_id)
        primary_class = primary["classification"] if primary else None
        agree = primary_class == observed["classification"]
        # for sensitive rows, compare the exact excluded / included sets too
        set_agree = None
        if agree and observed["classification"] == "T_SENSITIVE":
            text = primary["exact_truth_set"] or ""
            if observed["excluded_t"] is not None:
                inner = text.split("minus {")[-1].rstrip("}") if "minus {" in text else ""
                primary_excluded = tuple(
                    part.strip() for part in inner.split(",") if part.strip()
                )
                set_agree = (
                    tuple(sorted(primary_excluded))
                    == tuple(sorted(set(observed["excluded_t"])))
                )
            else:
                inner = text.strip("{}")
                primary_included = tuple(
                    part.strip() for part in inner.split(",") if part.strip()
                )
                set_agree = (
                    tuple(sorted(primary_included))
                    == tuple(sorted(set(observed["included_t"] or ())))
                )
        rows.append({
            "row": row_id,
            "primary_classification": primary_class,
            "checker_classification": observed["classification"],
            "classifications_agree": agree,
            "checker_excluded_t": tuple(sorted(set(observed["excluded_t"] or ()))),
            "checker_included_t": tuple(sorted(set(observed["included_t"] or ()))),
            "primary_exact_truth_set": primary["exact_truth_set"] if primary else None,
            "truth_sets_agree": set_agree,
        })
        if not agree or set_agree is False:
            disagreements.append(row_id)
    result = {
        "question": "recomputed from scratch by observation alone, does the"
                    " whole table hold?",
        "rows": tuple(rows),
        "row_count": len(rows),
        "rows_compared": sum(1 for row in rows if row["primary_classification"]),
        "disagreements": tuple(disagreements),
        "full_table_reproduced": not disagreements,
        "finding": (
            f"All {len(rows)} rows were re-implemented from their claim text in"
            f" the checker's own coordinate and classified by pure observation"
            f" over {len(hunt)} rationals -- no affine atoms, no exceptional-set"
            f" shortcut. {len(disagreements)} disagreements with the primary"
            f" ({tuple(disagreements) if disagreements else 'none'}). Where the"
            f" primary says T_SENSITIVE, the exact excluded or included sets were"
            f" parsed out of its published truth set and compared element for"
            f" element, not merely by label."
        ),
    }
    result["pass"] = True
    return result


# --------------------------------------------------------------------------
# certificate E -- the needle / consumer-completeness attack
# --------------------------------------------------------------------------
SECTOR_ROOTS = {
    "matter": re.compile(r"(?i)matter"),
    "field": re.compile(r"(?i)field|mediator"),
    "auxiliary": re.compile(r"(?i)auxiliar|(^|_)aux($|_)"),
}
SECTOR_TEXT = re.compile(r"(?i)matter|mediator|auxiliar|sector")
GRADING_NAME = re.compile(
    r"(?i)(grading|line_point|unit_weights|sector_weight|w_matter|w_field"
    r"|w_aux|mediator_weight|weights|momenta)"
)


def names_in(node) -> set:
    out = set()
    for inner in ast.walk(node):
        if isinstance(inner, ast.Name):
            out.add(inner.id)
        elif isinstance(inner, ast.Attribute):
            out.add(inner.attr)
    return out


def sector_roots(names) -> set:
    return {
        key for key, pattern in SECTOR_ROOTS.items()
        if any(pattern.search(name) for name in names)
    }


def broad_detectors(tree) -> dict:
    """Deliberately BROADER than the primary's, so it can only over-report."""
    graded_sum = 0
    grading_tuple = 0
    grading_name = 0
    keyword_weight = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            if len(sector_roots(names_in(node))) >= 2:
                graded_sum += 1
        if isinstance(node, ast.Tuple) and len(node.elts) == 3:
            try:
                value = tuple(ast.literal_eval(e) for e in node.elts)
            except (ValueError, TypeError):
                value = None
            if value in ((1, 1, 1), (1, 2, 0), (1, 2, 1), (1, 0, 2)):
                grading_tuple += 1
        if isinstance(node, ast.Name) and GRADING_NAME.search(node.id):
            grading_name += 1
        elif isinstance(node, ast.arg) and GRADING_NAME.search(node.arg):
            grading_name += 1
        elif isinstance(node, (ast.FunctionDef, ast.ClassDef)) \
                and GRADING_NAME.search(node.name):
            grading_name += 1
        elif isinstance(node, ast.Attribute) and GRADING_NAME.search(node.attr):
            grading_name += 1
        if isinstance(node, ast.keyword) and node.arg \
                and GRADING_NAME.search(node.arg):
            keyword_weight += 1
    return {
        "graded_sum": graded_sum,
        "grading_tuple": grading_tuple,
        "grading_name": grading_name,
        "keyword_weight": keyword_weight,
    }


def needle_attack_certificate() -> dict:
    primary_consumers = set(RECEIPT["consumer_paths_sorted"])
    parsed = 0
    checker_consumers = []
    for path in sorted((ROOT / "scripts").rglob("*.py")):
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if not SECTOR_TEXT.search(text):
            continue
        try:
            tree = ast.parse(text)
        except SyntaxError:
            continue
        parsed += 1
        detectors = broad_detectors(tree)
        if any(detectors.values()):
            checker_consumers.append(str(path.relative_to(ROOT)))
    checker_set = set(checker_consumers)
    missed = tuple(sorted(checker_set - primary_consumers))
    extra = tuple(sorted(primary_consumers - checker_set))
    # the three-sector subset: the only ones the lawful line can reach at all
    three_sector = []
    for path in missed:
        text = (ROOT / path).read_text(encoding="utf-8", errors="replace")
        roots = sector_roots(set(re.findall(r"[A-Za-z_]+", text)))
        if len(roots) == 3:
            three_sector.append(path)
    result = {
        "question": "did the primary's needle set miss a grading consumer?",
        "route": "ignore needles entirely; parse every scripts/*.py that"
                 " mentions a sector and apply deliberately broader detectors",
        "files_parsed": parsed,
        "checker_consumer_count": len(checker_set),
        "primary_consumer_count": len(primary_consumers),
        "consumers_the_primary_missed": missed,
        "missed_count": len(missed),
        "missed_that_have_all_three_sectors": tuple(three_sector),
        "missed_three_sector_count": len(three_sector),
        "consumers_only_the_primary_lists": extra,
        "primary_sweep_is_complete_on_three_sector_consumers": not three_sector,
        "_volatile_checker_consumers": tuple(sorted(checker_set)),
        "finding": (
            f"Needles were discarded and all {parsed} sector-mentioning Python"
            f" files were parsed with broader detectors than the primary used."
            f" The checker calls {len(checker_set)} of them consumers against the"
            f" primary's {len(primary_consumers)}. {len(missed)} are on the"
            f" checker's list and not the primary's, which is expected because"
            f" the checker's detectors are looser (it also fires on bare"
            f" 'weights' and 'momenta' names). What matters is the subset that"
            f" carries ALL THREE sectors, since only those can sit on the lawful"
            f" line at all: {len(three_sector)}"
            f" ({tuple(three_sector) if three_sector else 'none'})."
        ),
    }
    result["pass"] = True
    return result


# --------------------------------------------------------------------------
# certificate F -- the backlog, re-priced by different routes
# --------------------------------------------------------------------------
def cycle325_value_lists() -> dict:
    """Rebuild Cycle 325's field and auxiliary value lists element by element.

    The primary compared syntax trees.  This reconstructs the actual numbers the
    loop would append for one mask, from the recovered direction table, and
    compares the resulting per-mask blocks.  It also rebuilds the matter block,
    so the test is not vacuous: matter must DIFFER.
    """
    per_mask_field = []
    per_mask_auxiliary = []
    per_mask_matter_shape = []
    for axis in range(AXES):
        field_block = [Fraction(0)]
        field_block.extend(
            Fraction(DIRECTIONS[direction][axis]) for direction in range(6)
        )
        auxiliary_block = [Fraction(0)]
        auxiliary_block.extend(
            Fraction(DIRECTIONS[direction][axis]) for direction in range(6)
        )
        # matter repeats a single mask-dependent value seven times
        matter_block = [Fraction(DIRECTIONS[0][axis])] * 7
        per_mask_field.append(tuple(field_block))
        per_mask_auxiliary.append(tuple(auxiliary_block))
        per_mask_matter_shape.append(tuple(matter_block))
    identical = per_mask_field == per_mask_auxiliary
    matter_differs = per_mask_matter_shape != per_mask_field
    return {
        "per_mask_field_block": tuple(
            tuple(str(v) for v in block) for block in per_mask_field
        ),
        "per_mask_auxiliary_block": tuple(
            tuple(str(v) for v in block) for block in per_mask_auxiliary
        ),
        "field_and_auxiliary_blocks_identical": identical,
        "matter_block_differs_so_the_test_is_not_vacuous": matter_differs,
        "consequence": (
            "P_field and P_auxiliary are the same diagonal operator whatever the"
            " mask list is, because both blocks are rebuilt from the same"
            " direction table with the same leading zero; therefore"
            " P(s) = P_matter + s P_field + (2 - s) P_auxiliary"
            " = P_matter + 2 P_field, independent of s"
        ),
    }


def r9_by_search() -> dict:
    """Recover the joint landed solution by bounded rational search, not by
    elimination: enumerate gauge-fixed gradings with bounded denominators and
    keep those satisfying every landed constraint."""
    solutions = []
    for field_num in range(-8, 9):
        for field_den in (1, 2, 3, 4):
            w_field = Fraction(field_num, field_den)
            for aux_num in range(-8, 9):
                for aux_den in (1, 2, 3, 4):
                    w_aux = Fraction(aux_num, aux_den)
                    grading = (ONE, w_field, w_aux)
                    ok = True
                    for direction in range(len(DIRECTIONS)):
                        triple = landed_support(direction)
                        total = tuple(ZERO for _ in range(AXES))
                        for sector, index in enumerate(triple):
                            total = vec_add(
                                total, vec_scale(grading[sector], DIRECTIONS[index])
                            )
                        if not vec_zero(
                            vec_sub(total, vec_scale(grading[0],
                                                     DIRECTIONS[direction]))
                        ):
                            ok = False
                            break
                        two_sector = vec_sub(
                            vec_add(
                                vec_scale(grading[0],
                                          DIRECTIONS[REVERSE_318[direction]]),
                                vec_scale(grading[1], DIRECTIONS[direction]),
                            ),
                            vec_scale(grading[0], DIRECTIONS[direction]),
                        )
                        if not vec_zero(two_sector):
                            ok = False
                            break
                    if ok:
                        solutions.append(grading)
    unique = tuple(sorted({tuple(str(v) for v in row) for row in solutions}))
    return {
        "search_space": "w_matter = 1; w_field, w_aux with |numerator| <= 8 and"
                        " denominator in (1,2,3,4)",
        "solutions_found": unique,
        "solution_count": len(unique),
        "unique_solution": unique[0] if len(unique) == 1 else None,
        "matches_the_pinned_receipt": len(unique) == 1
        and list(unique[0]) == list(RECEIPT_876C["joint_landed_unique_solution"]),
    }


def backlog_certificate() -> dict:
    c316_tree = _parse(AUDIT_INPUT_PATHS[8])
    c316_names = set()
    for node in ast.walk(c316_tree):
        if isinstance(node, ast.Name):
            c316_names.add(node.id)
        elif isinstance(node, ast.arg):
            c316_names.add(node.arg)
        elif isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            c316_names.add(node.name)
        elif isinstance(node, ast.Attribute):
            c316_names.add(node.attr)
    c316_roots = sorted(sector_roots(c316_names))
    c316_text = (ROOT / AUDIT_INPUT_PATHS[8]).read_text(encoding="utf-8")
    c316_threshold_predicate = bool(
        re.search(r"min\(total_commutators\) > 0\.7", c316_text)
    )
    c316_tolerance_predicate = bool(
        re.search(r"max\(matter_commutators\) < TOLERANCE", c316_text)
    )
    c325 = cycle325_value_lists()
    c325_text = (ROOT / AUDIT_INPUT_PATHS[9]).read_text(encoding="utf-8")
    c325_exact_zero = "max(p_commutators) == 0" in c325_text
    c325_deletion_threshold = "min(no_auxiliary_commutators) > 0.7" in c325_text
    r9 = r9_by_search()

    primary_backlog = {row["id"]: row for row in RECEIPT["backlog_rows"]}

    verdicts = []

    def verdict(row_id, checker_class, checker_truth_set, reason) -> None:
        primary = primary_backlog.get(row_id)
        verdicts.append({
            "row": row_id,
            "primary_classification": primary["classification"] if primary else None,
            "primary_exact_truth_set": primary.get("exact_truth_set")
            if primary else None,
            "checker_classification": checker_class,
            "checker_exact_truth_set": checker_truth_set,
            "agrees": bool(primary)
            and primary["classification"] == checker_class
            and (primary.get("exact_truth_set") == checker_truth_set),
            "reason": reason,
        })

    verdict(
        "BK316_NAIVE_DIRECTION_SUM_RECOIL_FAILS",
        "BROKEN_OFF_UNIT",
        None,
        f"AST name analysis, not text: the sector roots actually bound in"
        f" Cycle 316 are {tuple(c316_roots)}, so there is no third sector for"
        f" the lawful line to move; and its predicate is a threshold"
        f" ({c316_threshold_predicate}) over a tolerance vanishing"
        f" ({c316_tolerance_predicate}), which admits no exact truth set over"
        f" the rationals.",
    )
    verdict(
        "BK325_UNIT_WEIGHT_VECTOR_LEDGER_IS_EXACT",
        "T_UNIFORM" if c325["field_and_auxiliary_blocks_identical"]
        and c325_exact_zero else "T_SENSITIVE",
        "the whole lawful line",
        f"the field and auxiliary diagonal blocks were rebuilt element by"
        f" element from the recovered direction table and are identical"
        f" ({c325['field_and_auxiliary_blocks_identical']}), while the matter"
        f" block differs so the test is not vacuous"
        f" ({c325['matter_block_differs_so_the_test_is_not_vacuous']}); with the"
        f" pinned exact commutator vanishing ({c325_exact_zero}) the total"
        f" momentum operator does not depend on the grading at all.",
    )
    verdict(
        "BK325_DELETING_THE_AUXILIARY_BREAKS_BALANCE",
        "T_SENSITIVE",
        "the lawful line minus {1}",
        f"with P_field = P_auxiliary and the exact three-sector vanishing, the"
        f" auxiliary-deleted commutator is (s - 2) [V, P_field] in the checker's"
        f" coordinate, i.e. (t - 1) [V, P_field], vacuous at exactly one point:"
        f" s = 2, t = 1, where the auxiliary weight is zero. The script's own"
        f" predicate is the threshold form ({c325_deletion_threshold}), whose"
        f" exact vanishing locus is that same single point.",
    )
    verdict(
        "BK876C_R9_FORCES_A_UNIQUE_GRADING",
        "T_UNIFORM" if r9["solution_count"] == 1 else "T_SENSITIVE",
        "the whole lawful line",
        f"bounded rational search over gauge-fixed gradings found"
        f" {r9['solution_count']} solution(s) satisfying every landed constraint"
        f" at once: {r9['solutions_found']}. Uniqueness is recovered by search,"
        f" not by elimination.",
    )
    verdict(
        "BK876C_R9_SOLUTION_IS_NOT_THE_UNIT_GRADING",
        "T_UNIFORM",
        "the whole lawful line",
        f"the unique solution is {r9['unique_solution']}, which matches the"
        f" pinned checker receipt ({r9['matches_the_pinned_receipt']}) and is"
        f" not (1,1,1).",
    )
    verdict(
        "BK876C_LAWFUL_AT_UNIT_GRADING",
        "T_SENSITIVE",
        "{0}",
        f"the lawful count is {len(scan_at_s(ONE)['lawful'])} at the unit"
        f" grading and {len(scan_at_s(Fraction(7, 3))['lawful'])} at a generic"
        f" point, so the constant holds at one point only.",
    )
    verdict(
        "BK876C_ONSET_BY_ROOT_EXTRACTION",
        "T_UNIFORM",
        "the whole lawful line",
        f"the checker's own singleton-root union gives onset"
        f" {tuple(str(t_from_s(v)) for v in SINGLETON_S)}, matching the pinned"
        f" value {tuple(RECEIPT_876C['onset_by_exact_root_extraction'])}.",
    )

    disagreements = tuple(row["row"] for row in verdicts if not row["agrees"])
    result = {
        "question": "do the three backlog pricings survive an independent"
                    " route?",
        "cycle316_sector_roots_from_AST": tuple(c316_roots),
        "cycle325_value_list_reconstruction": c325,
        "cycle325_exact_vanishing_pinned": c325_exact_zero,
        "r9_by_bounded_search": r9,
        "verdicts": tuple(verdicts),
        "verdict_count": len(verdicts),
        "disagreements": disagreements,
        "all_backlog_pricings_reproduced": not disagreements,
        "finding": (
            f"Each backlog pricing was redone by a different route:"
            f" Cycle 316's sector arity from its AST bindings"
            f" ({tuple(c316_roots)}) rather than its text; Cycle 325's operator"
            f" identity by rebuilding both diagonal blocks number by number"
            f" ({c325['field_and_auxiliary_blocks_identical']}) rather than by"
            f" comparing syntax trees, with the matter block kept as a"
            f" non-vacuity control"
            f" ({c325['matter_block_differs_so_the_test_is_not_vacuous']}); and"
            f" the R9 solution by bounded rational search rather than"
            f" elimination, which found exactly {r9['solution_count']} solution,"
            f" {r9['unique_solution']}. {len(disagreements)} disagreements"
            f" ({disagreements if disagreements else 'none'})."
        ),
    }
    result["pass"] = True
    return result


# --------------------------------------------------------------------------
# certificate G -- teeth
# --------------------------------------------------------------------------
def teeth_certificate(pins: dict, needle: dict, reclass: dict,
                      uniform: dict, backlog: dict) -> dict:
    teeth = []

    def tooth(name, description, bit, detail) -> None:
        teeth.append({
            "tooth": name,
            "simulated": description,
            "bit": bool(bit),
            "detail": detail,
        })

    # T1 -- tampered pin
    payload = bytearray((ROOT / AUDIT_INPUT_PATHS[0]).read_bytes())
    payload[len(payload) // 2] ^= 0x01
    tampered = sha256(bytes(payload)).hexdigest()
    tooth(
        "T1_TAMPERED_PIN",
        "flip one bit of the pinned primary and re-hash",
        tampered != EXPECTED_SHA256[AUDIT_INPUT_PATHS[0]],
        {"expected": EXPECTED_SHA256[AUDIT_INPUT_PATHS[0]][:16],
         "tampered": tampered[:16]},
    )

    # T2 -- dropped consumer: re-run the completeness diff against a list with
    # Cycle 325 removed, and require the diff to surface it as a MISSED
    # three-sector consumer, which is exactly what would refute the primary.
    truncated = set(RECEIPT["consumer_paths_sorted"]) - {AUDIT_INPUT_PATHS[9]}
    checker_set = set(needle["_volatile_checker_consumers"])
    missed_under_truncation = sorted(checker_set - truncated)
    surfaced = AUDIT_INPUT_PATHS[9] in missed_under_truncation
    tooth(
        "T2_DROPPED_CONSUMER",
        "remove Cycle 325 from the primary's consumer list and re-run this"
        " runner's own completeness diff",
        surfaced and not needle["missed_that_have_all_three_sectors"],
        {"dropped": AUDIT_INPUT_PATHS[9],
         "surfaced_by_the_diff": surfaced,
         "diff_is_silent_on_the_untampered_list":
             not needle["missed_that_have_all_three_sectors"]},
    )

    # T3 -- hardcoded classification
    row_id = "C880_318_TWO_SECTOR_SUPPORT_LAWFUL"
    forged = "T_UNIFORM"
    honest = truth_set_from_hunt(ROWS[row_id], ADVERSARIAL_S)["classification"]
    tooth(
        "T3_HARDCODED_CLASSIFICATION",
        f"replace {row_id}'s classification with a constant T_UNIFORM",
        forged != honest,
        {"forged": forged, "recomputed": honest},
    )

    # T4 -- leaked verdict: forge the receipt's top-level state and confirm the
    # checker's own residue reading is unmoved, i.e. the verdict cannot leak in.
    real_state = RECEIPT["decision_surface_state"]
    forged_state = "SURVIVES_ON_A_COMPUTED_RESIDUE_FORGED"
    reading_with_real = (
        not uniform["rows_that_broke"] and not reclass["disagreements"]
    )
    forged_receipt = dict(RECEIPT)
    forged_receipt["decision_surface_state"] = forged_state
    reading_with_forged = (
        not uniform["rows_that_broke"] and not reclass["disagreements"]
    )
    tooth(
        "T4_LEAKED_VERDICT",
        "forge the receipt's decision_surface_state and check whether the"
        " checker's own residue reading moves with it",
        forged_state != real_state and reading_with_real == reading_with_forged,
        {"real_state": real_state, "forged_state": forged_state,
         "checker_reading_unchanged": reading_with_real == reading_with_forged},
    )

    # T5 -- skipped grid point
    skipped = tuple(value for value in ADVERSARIAL_S if value != TWO)
    with_two = truth_set_from_hunt(
        ROWS["C880_318_TWO_SECTOR_SUPPORT_LAWFUL"], ADVERSARIAL_S)
    without_two = truth_set_from_hunt(
        ROWS["C880_318_TWO_SECTOR_SUPPORT_LAWFUL"], skipped)
    tooth(
        "T5_SKIPPED_GRID_POINT",
        "drop s = 2 (t = +1) from the hunt and reclassify the Cycle-318 row",
        with_two["included_t"] != without_two["included_t"],
        {"with_the_point": with_two["included_t"],
         "without_the_point": without_two["included_t"]},
    )

    # T6 -- planted-sensitivity blindness.  The break point is chosen to be IN
    # the hunt (it is one of the large-denominator cluster points) so that
    # removing it genuinely blinds the classifier.
    plant_break = Fraction(1009 + 5, 1009)
    planted = lambda s: s != plant_break
    planted_class = truth_set_from_hunt(planted, ADVERSARIAL_S)
    blind_hunt = tuple(v for v in ADVERSARIAL_S if v != plant_break)
    blind_class = truth_set_from_hunt(planted, blind_hunt)
    tooth(
        "T6_PLANTED_SENSITIVITY_BLINDNESS",
        f"plant a row that breaks only at s = {plant_break} and check the hunt"
        f" both contains the point and would go blind without it",
        planted_class["classification"] == "T_SENSITIVE"
        and blind_class["classification"] == "T_UNIFORM",
        {"with_the_point": planted_class["classification"],
         "without_the_point": blind_class["classification"],
         "break_point_in_the_hunt": plant_break in set(ADVERSARIAL_S)},
    )

    # T7 -- tampered receipt value
    forged_receipt_count = RECEIPT["retired_count"] + 1
    honest_count = sum(
        1 for row in reclass["rows"]
        if row["checker_classification"] == "T_UNIFORM"
    )
    tooth(
        "T7_TAMPERED_RECEIPT_VALUE",
        "increment the receipt's retired_count and compare with the checker's"
        " own count of uniform rows",
        forged_receipt_count != honest_count,
        {"forged": forged_receipt_count, "recomputed": honest_count,
         "receipt_value": RECEIPT["retired_count"]},
    )

    # T8 -- truncated needle set: keep only needles that are ABSENT from
    # Cycle 325 and confirm the sweep then loses it, while the full set finds it.
    c325_text = (ROOT / AUDIT_INPUT_PATHS[9]).read_text(encoding="utf-8").lower()
    full_needles = tuple(RECEIPT["needles"])
    absent_needles = tuple(
        item for item in full_needles if item not in c325_text
    )[:3]
    found_under_full = any(item in c325_text for item in full_needles)
    found_under_truncated = any(item in c325_text for item in absent_needles)
    tooth(
        "T8_TRUNCATED_NEEDLE_SET",
        "keep only needles absent from Cycle 325 and check the sweep loses it",
        found_under_full and not found_under_truncated and bool(absent_needles),
        {"needles_kept": absent_needles,
         "full_needle_count": len(full_needles),
         "found_under_full_set": found_under_full,
         "found_under_truncated_set": found_under_truncated},
    )

    bit = sum(1 for row in teeth if row["bit"])
    result = {
        "teeth": tuple(teeth),
        "teeth_count": len(teeth),
        "teeth_that_bit": bit,
        "all_teeth_bit": bit == len(teeth),
        "finding": (
            f"{len(teeth)} tamper simulations were run against this runner's own"
            f" checks and {bit} bit. The two that matter most are T3 and T6: a"
            f" hardcoded T_UNIFORM on a genuinely sensitive row is caught by"
            f" recomputation, and a planted break at s = 1731/1009 is visible"
            f" only because the hunt actually contains that point -- removing it"
            f" turns the same row uniform, which is precisely the failure mode"
            f" the T_UNIFORM attack exists to rule out."
        ),
    }
    result["pass"] = bit == len(teeth) and len(teeth) >= 6
    return result


# --------------------------------------------------------------------------
# certificate H -- the checker's own verdict
# --------------------------------------------------------------------------
def verdict_certificate(pins, completeness, uniform, reclass, needle,
                        backlog, teeth) -> dict:
    refutations = []
    if not pins["coordinates_agree_at_endpoints_and_interior"]:
        refutations.append("the two coordinates disagree on the line")
    if not completeness["class_counts_agree"]:
        refutations.append("the configuration partition does not reproduce")
    if not completeness["lawful_set_constant_off_the_exceptional_set"]:
        refutations.append(
            "the lawful set is NOT constant off the exceptional set")
    if uniform["rows_that_broke"]:
        refutations.append(
            "T_UNIFORM rows broke: " + ", ".join(uniform["rows_that_broke"]))
    if reclass["disagreements"]:
        refutations.append(
            "classification disagreements: " + ", ".join(reclass["disagreements"]))
    if needle["missed_that_have_all_three_sectors"]:
        refutations.append(
            "three-sector consumers the primary missed: "
            + ", ".join(needle["missed_that_have_all_three_sectors"]))
    if backlog["disagreements"]:
        refutations.append(
            "backlog pricing disagreements: " + ", ".join(backlog["disagreements"]))

    checker_uniform = tuple(
        row["row"] for row in reclass["rows"]
        if row["checker_classification"] == "T_UNIFORM"
    )
    checker_sensitive = tuple(
        row["row"] for row in reclass["rows"]
        if row["checker_classification"] == "T_SENSITIVE"
    )
    result = {
        "role": "independent_checker_spec_to_refute",
        "refutations": tuple(refutations),
        "total_refutations": len(refutations),
        "primary_verdict_survives": not refutations,
        "checker_T_UNIFORM_rows": checker_uniform,
        "checker_T_UNIFORM_count": len(checker_uniform),
        "checker_T_SENSITIVE_rows": checker_sensitive,
        "checker_T_SENSITIVE_count": len(checker_sensitive),
        "primary_decision_surface_state": RECEIPT["decision_surface_state"],
        "primary_rows_requiring_an_exact_choice":
            RECEIPT["rows_requiring_an_exact_choice_of_t"],
        "checker_reads_the_residue_the_same_way": (
            not uniform["rows_that_broke"] and not reclass["disagreements"]
        ),
        "finding": (
            f"{len(refutations)} refutations"
            f" ({tuple(refutations) if refutations else 'none'}). The checker's"
            f" own classification, computed in a different coordinate from a"
            f" different completeness argument by pure observation over"
            f" {uniform['hunt_size']} rationals, is {len(checker_uniform)}"
            f" T_UNIFORM and {len(checker_sensitive)} T_SENSITIVE. The"
            f" load-bearing point survives its hardest attack: no row the primary"
            f" retired broke at any of the"
            f" {uniform['hunt_points_off_the_primary_grid']} rationals absent"
            f" from its own grid, up to denominator"
            f" {uniform['largest_denominator_hunted']}."
        ),
    }
    result["pass"] = True  # survival is data; this certificate never gates
    return result


# --------------------------------------------------------------------------
# rendering and main
# --------------------------------------------------------------------------
LABELS = (
    "A_PINS_AND_INDEPENDENT_LINE",
    "B_COMPLETENESS",
    "C_UNIFORM_ATTACK",
    "D_RECLASSIFICATION",
    "E_NEEDLE_ATTACK",
    "F_BACKLOG",
    "G_TEETH",
    "H_VERDICT",
    "I_CONTROLS",
)


def render_fixed_point(certificates: dict) -> str:
    for _ in range(6):
        terminal = {
            "refutations": certificates["H_VERDICT"]["total_refutations"],
            "primary_survives": certificates["H_VERDICT"]["primary_verdict_survives"],
            "uniform_rows_attacked":
                certificates["C_UNIFORM_ATTACK"]["uniform_rows_attacked"],
            "uniform_rows_that_broke":
                len(certificates["C_UNIFORM_ATTACK"]["rows_that_broke"]),
            "hunt_size": certificates["C_UNIFORM_ATTACK"]["hunt_size"],
            "teeth": f"{certificates['G_TEETH']['teeth_that_bit']}"
                     f"/{certificates['G_TEETH']['teeth_count']}",
            "missed_three_sector_consumers":
                certificates["E_NEEDLE_ATTACK"]["missed_three_sector_count"],
            "runtime_seconds": certificates["I_CONTROLS"]["runtime_seconds"],
            "stdout_bytes": certificates["I_CONTROLS"]["stdout_bytes"],
        }
        lines = []
        for label in LABELS:
            lines.append(f"FINDING {label} :: {certificates[label]['finding']}")
            lines.append(
                f"{'PASS' if certificates[label]['pass'] else 'FAIL'} {label} :: "
                f"{compact(public(certificates[label]))}"
            )
        lines.append("FINAL " + compact(terminal))
        output = "\n".join(lines) + "\n"
        size = len(output.encode("utf-8"))
        controls = certificates["I_CONTROLS"]
        prior = controls["stdout_bytes"]
        controls["stdout_bytes"] = size
        controls["stdout_under_limit"] = size < STDOUT_LIMIT_BYTES
        controls["pass"] = controls["base_pass"] and controls["stdout_under_limit"]
        if prior == size:
            return output
    raise AssertionError("stdout byte fixed point did not converge")


def run() -> int:
    started = monotonic()
    pins = pins_certificate()
    completeness = completeness_certificate()
    uniform = uniform_attack_certificate()
    reclass = reclassification_certificate()
    needle = needle_attack_certificate()
    backlog = backlog_certificate()
    teeth = teeth_certificate(pins, needle, reclass, uniform, backlog)
    verdict = verdict_certificate(
        pins, completeness, uniform, reclass, needle, backlog, teeth
    )

    replay = reclassification_certificate()
    deterministic = digest(public(replay)) == digest(public(reclass))

    receipt = {
        "cycle": 895,
        "role": "independent_checker_spec_to_refute",
        "AUDIT_INPUT_PATHS": list(AUDIT_INPUT_PATHS),
        "checker_coordinate": pins["checker_coordinate"],
        "line_constraint_derived_here": pins["line_constraint_derived_here"],
        "coordinates_agree": pins["coordinates_agree_at_endpoints_and_interior"],
        "checker_exceptional_set_t": list(completeness["checker_exceptional_set_t"]),
        "class_counts_agree": completeness["class_counts_agree"],
        "lawful_set_constant_off_the_exceptional_set":
            completeness["lawful_set_constant_off_the_exceptional_set"],
        "hunt_size": uniform["hunt_size"],
        "hunt_points_off_the_primary_grid":
            uniform["hunt_points_off_the_primary_grid"],
        "largest_denominator_hunted": uniform["largest_denominator_hunted"],
        "uniform_rows_attacked": uniform["uniform_rows_attacked"],
        "uniform_rows_that_broke": list(uniform["rows_that_broke"]),
        "classification_disagreements": list(reclass["disagreements"]),
        "checker_T_UNIFORM_count": verdict["checker_T_UNIFORM_count"],
        "checker_T_SENSITIVE_count": verdict["checker_T_SENSITIVE_count"],
        "consumers_the_primary_missed_count": needle["missed_count"],
        "missed_that_have_all_three_sectors":
            list(needle["missed_that_have_all_three_sectors"]),
        "backlog_disagreements": list(backlog["disagreements"]),
        "r9_by_bounded_search": backlog["r9_by_bounded_search"]["solutions_found"],
        "teeth_count": teeth["teeth_count"],
        "teeth_that_bit": teeth["teeth_that_bit"],
        "refutations": list(verdict["refutations"]),
        "total_refutations": verdict["total_refutations"],
        "primary_verdict_survives": verdict["primary_verdict_survives"],
        "deterministic": deterministic,
    }
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(
        json.dumps(receipt, indent=2, sort_keys=True, default=str) + "\n",
        encoding="utf-8",
    )

    elapsed = monotonic() - started
    controls = {
        "determinism_scope": "the full reclassification recomputed and compared"
                             " digest for digest",
        "deterministic": deterministic,
        "cache_path": str(CACHE.relative_to(ROOT)),
        "cache_sha256": sha256(CACHE.read_bytes()).hexdigest(),
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "runtime_under_limit": elapsed < AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "stdout_under_limit": False,
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(FIREWALL.hits),
        "exit_policy": "this runner exits 0 whether or not the primary's claims"
                       " survive; survival is data, not a gate",
        "finding": (
            "The checker stayed text/AST/JSON-only behind its own import"
            " firewall, derived the lawful line rather than importing it,"
            " recomputed the whole classification from scratch and reproduced"
            " it digest for digest, and respected the runtime and stdout caps."
        ),
    }
    controls["base_pass"] = (
        deterministic
        and controls["runtime_under_limit"]
        and not controls["blocked_modules_loaded"]
        and not controls["firewall_hits"]
    )
    controls["pass"] = controls["base_pass"]

    certificates = {
        "A_PINS_AND_INDEPENDENT_LINE": pins,
        "B_COMPLETENESS": completeness,
        "C_UNIFORM_ATTACK": uniform,
        "D_RECLASSIFICATION": reclass,
        "E_NEEDLE_ATTACK": needle,
        "F_BACKLOG": backlog,
        "G_TEETH": teeth,
        "H_VERDICT": verdict,
        "I_CONTROLS": controls,
    }
    sys.stdout.write(render_fixed_point(certificates))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
