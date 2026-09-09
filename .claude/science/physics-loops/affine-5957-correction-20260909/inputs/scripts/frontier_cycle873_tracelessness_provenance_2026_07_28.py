#!/usr/bin/env python3
"""Cycle 873: provenance of the recoil ledger's tracelessness.

Cycle 868 proved the landed response surface blind to the conformal sign and
named its own escape condition (a): a landed source with NONZERO sector trace
would make the odd response objects sign-sensitive.  Cycle 868 read that trace
off the frozen Cycle-320 recoil ledger (-2d, +d, +d), whose sector sum is zero.

This cycle settles where that zero comes from.  It does not ask whether the sum
is zero -- it asks which step makes it zero, and whether any variant inside the
constructor's own declared degrees of freedom can break it.

The answer is a split.  At FIXED unit sector grading the zero is DERIVED: the
sector trace of the ledger is identically the conservation defect of Cycle-320's
certified unit-weight vector balance, the exchange only ever connects states of
equal P eigenvalue, and an exhaustive sweep of the constructor's full target
freedom produces no trace-bearing lawful variant -- with a quantized gap, so no
infinitesimal detuning exists either.  But the unit grading is itself SUPPLIED.
Cycle-318's coefficient-two route -- enumerated by name inside Cycle-320's own
route tuple, and declared in Cycle-318's own words to be supplied candidate-law
structure -- conserves P_matter + 2 P_mediator instead, and its raw occupation
ledger carries trace.  That witness is pushed through a minimally re-derived
Cycle-868 census here (the 868 runner is pinned and firewalled, never imported).

All four cited primaries are SHA-pinned text/AST evidence and are blocked from
import by a meta-path firewall.  Every certified number is rebuilt here with
stdlib exact arithmetic; no floating point enters any certified quantity.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py",
    "scripts/proper_cubic_recoil_balanced_carried_source_cycle318_2026_07_18.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/frontier_cycle868_response_sign_census_2026_07_28.py",
)

import ast
from fractions import Fraction
from hashlib import sha1, sha256
import importlib.abc
from itertools import product
import json
from pathlib import Path
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / "outputs" / (
    "tracelessness_provenance_cycle873_receipt_2026_07_28.json"
)
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "71fb02658569174b7f6f989efe311951713026ead36ece8866dca1e96878d706",
    AUDIT_INPUT_PATHS[1]:
        "3c1575c99622c0874ab42730494d615fbe1a2b867975e5bf048fd2a4a8af9d56",
    AUDIT_INPUT_PATHS[2]:
        "c410b754d4e984f6ee5ccbc7c5a52e776c50c91c4daa12d798044f104cc7435b",
    AUDIT_INPUT_PATHS[3]:
        "e09226e35a58cd52e2d4f61516f6e2a64cdebb7f4c20893307a1f3d2ff3f4ebb",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c95eb9738409c3ffe20f8b90a7ab25e6dc5843a0",
    AUDIT_INPUT_PATHS[1]: "7672380148d79f22a4ab9b2700121aac1b097004",
    AUDIT_INPUT_PATHS[2]: "0be8d83ec8ed874ff12e2092dc47121b8030a5bc",
    AUDIT_INPUT_PATHS[3]: "c64dd97a3034ccbedc2603db4dacc1c80acfd952",
}
REQUIRED_AST_MARKERS = {
    AUDIT_INPUT_PATHS[0]: (
        "REVERSE", "ANGLE", "link_recoil_vertex", "local_route_controls",
        "N1_ROUTES",
    ),
    AUDIT_INPUT_PATHS[1]: ("REVERSE", "ANGLE", "direction_vertex", "link_vertex"),
    AUDIT_INPUT_PATHS[2]: ("DIRECTIONS", "UNIFORM"),
    AUDIT_INPUT_PATHS[3]: (
        "landed_ledger", "conformal_channel", "grading_operator",
        "response_objects",
    ),
}

# Verbatim evidence located inside the pinned primaries by exact substring
# search.  These are quotations, not paraphrases: if the pinned text does not
# contain them character for character the controls certificate fails.
REQUIRED_QUOTES = {
    AUDIT_INPUT_PATHS[0]: (
        "pair_index = 6 + 36 * REVERSE[direction] + 6 * direction + direction",
        "final_matter + final_field + final_auxiliary - initial_vector",
        "the direction-changing carried-link vertex has exact unit-weight"
        " Q/P operator balance and nonzero matter recoil",
        "Cycle-318 coefficient-two recoil source",
        "the direction-preserving link comparator balances unit P but has"
        " zero matter recoil operator",
    ),
    AUDIT_INPUT_PATHS[1]: (
        "P = P_matter + 2 P_mediator at operator level.",
        "is supplied candidate-law structure",
        "pair_index = 6 + 6 * REVERSE[direction] + direction",
        "mediator_weight * c210.DIRECTIONS[field, axis]",
    ),
    AUDIT_INPUT_PATHS[2]: ("DIRECTIONS = np.asarray(",),
    AUDIT_INPUT_PATHS[3]: (
        '"""The frozen Cycle-320 recoil ledger (-2d, +d, +d)."""',
        '"""The sector trace: the conformal channel of the source."""',
        "return (-2 * weight, weight, weight)",
    ),
}


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if any cited source-only primary is imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

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
# constants recovered from the pinned primaries by AST, never by import
# --------------------------------------------------------------------------
def _top_level_assignments(tree: ast.Module) -> dict[str, ast.expr]:
    out: dict[str, ast.expr] = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    out[target.id] = node.value
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            if node.value is not None:
                out[node.target.id] = node.value
    return out


def _parse(path: str) -> ast.Module:
    return ast.parse((ROOT / path).read_bytes(), filename=path)


def recover_directions() -> tuple[tuple[int, int, int], ...]:
    """c210.DIRECTIONS, read out of the pinned text as a literal tuple."""
    assigns = _top_level_assignments(_parse(AUDIT_INPUT_PATHS[2]))
    node = assigns["DIRECTIONS"]
    if not isinstance(node, ast.Call):
        raise AssertionError("pinned DIRECTIONS is not a call node")
    return tuple(tuple(row) for row in ast.literal_eval(node.args[0]))


def recover_reverse(path: str) -> tuple[int, ...]:
    """The direction-reversal permutation as spelled in the pinned primary."""
    assigns = _top_level_assignments(_parse(path))
    return tuple(ast.literal_eval(assigns["REVERSE"]))


def recover_routes() -> tuple[str, ...]:
    assigns = _top_level_assignments(_parse(AUDIT_INPUT_PATHS[0]))
    return tuple(ast.literal_eval(assigns["N1_ROUTES"]))


DIRECTIONS = recover_directions()
REVERSE_320 = recover_reverse(AUDIT_INPUT_PATHS[0])
REVERSE_318 = recover_reverse(AUDIT_INPUT_PATHS[1])
N1_ROUTES = recover_routes()

SECTORS = ("matter", "field", "auxiliary")
ENDPOINTS = ("LEFT", "RIGHT")
AXES = 3
HELD_EDGE_LENGTH = 6
WEIGHTS = tuple(range(1, HELD_EDGE_LENGTH + 1))
SIGMA_DEGREE_BOUND = 2
ZERO = Fraction(0)
THIRD = Fraction(1, 3)
OBJECT_ARITY = {
    "O1_PUSHFORWARD": 18,
    "O2_ADJOINT_PULLBACK": 18,
    "O3_FLUX_BALANCE": 6,
    "O4_RESPONSE_GRAM": 1,
    "O5_RESPONSE_TENSOR": 18,
    "O6_EDGE_TRANSFER": 1,
}
OBJECT_NAMES = tuple(sorted(OBJECT_ARITY))

# The declared rational grading grid swept in certificate D.  Halves are used
# because the two landed gradings, (1,1) and the Cycle-318 (2,0), both lie on
# it, and because halves are the coarsest grid that still resolves the interior
# of the lawful segment w_field + w_auxiliary = 2.
GRADING_GRID = tuple(Fraction(numerator, 2) for numerator in range(0, 7))


def vec_add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def vec_sub(left, right):
    return tuple(a - b for a, b in zip(left, right))


def vec_scale(factor, vector):
    return tuple(factor * component for component in vector)


def vec_zero(vector) -> bool:
    return all(component == 0 for component in vector)


def l1(vector) -> Fraction:
    return sum((abs(component) for component in vector), Fraction(0))


# --------------------------------------------------------------------------
# exact univariate polynomials in the formal conformal sign sigma
# --------------------------------------------------------------------------
Poly = tuple

POLY_ZERO: Poly = ()


def p_trim(coefficients: list) -> Poly:
    while coefficients and coefficients[-1] == 0:
        coefficients.pop()
    return tuple(coefficients)


def p_const(value: Fraction) -> Poly:
    return () if value == 0 else (value,)


def p_add(left: Poly, right: Poly) -> Poly:
    width = max(len(left), len(right))
    return p_trim([
        (left[index] if index < len(left) else ZERO)
        + (right[index] if index < len(right) else ZERO)
        for index in range(width)
    ])


def p_scale(poly: Poly, factor: Fraction) -> Poly:
    if factor == 0:
        return POLY_ZERO
    return p_trim([factor * value for value in poly])


def p_shift(poly: Poly, degree: int) -> Poly:
    if not poly:
        return POLY_ZERO
    return (ZERO,) * degree + poly


def p_mul(left: Poly, right: Poly) -> Poly:
    if not left or not right:
        return POLY_ZERO
    out = [ZERO] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        if a == 0:
            continue
        for j, b in enumerate(right):
            out[i + j] += a * b
    return p_trim(out)


def p_eval(poly: Poly, point: int) -> Fraction:
    total = ZERO
    power = Fraction(1)
    for value in poly:
        total += value * power
        power *= point
    return total


def p_degree(poly: Poly) -> int:
    return len(poly) - 1


def p_text(poly: Poly) -> str:
    return "0" if not poly else "+".join(
        f"({value.numerator}/{value.denominator})s^{index}"
        for index, value in enumerate(poly) if value != 0
    )


# --------------------------------------------------------------------------
# serialisation helpers
# --------------------------------------------------------------------------
def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


# Fields that carry wall-clock or byte-count state rather than science.  They
# are stripped before the payload digest so that determinism is asserted on the
# certified content and never on how long the machine took.
VOLATILE_FIELDS = (
    "runtime_seconds", "stdout_bytes", "stdout_under_limit",
    "runtime_under_limit", "pass", "base_pass",
)


def science_payload(certificates: dict) -> str:
    return digest({
        label: {
            key: value for key, value in row.items()
            if key not in VOLATILE_FIELDS
        }
        for label, row in sorted(certificates.items())
    })


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


# --------------------------------------------------------------------------
# the Cycle-320 vertex, rebuilt sparsely over the integers
# --------------------------------------------------------------------------
def triple_index(matter: int, field: int, auxiliary: int) -> int:
    """The pair-block index spelled in the pinned Cycle-320 source."""
    return 6 + 36 * matter + 6 * field + auxiliary


def c320_support() -> tuple[tuple[int, tuple[int, int, int]], ...]:
    """d -> (matter, field, auxiliary) targets of the carried-link exchange."""
    return tuple(
        (direction, (REVERSE_320[direction], direction, direction))
        for direction in range(len(DIRECTIONS))
    )


def momentum_eigenvalue(
    triple: tuple[int, int, int], grading: tuple[Fraction, Fraction, Fraction]
) -> tuple:
    """w_matter D[m] + w_field D[f] + w_auxiliary D[a], exactly."""
    total = (ZERO, ZERO, ZERO)
    for sector, index in enumerate(triple):
        total = vec_add(total, vec_scale(grading[sector], DIRECTIONS[index]))
    return total


def raw_ledger(
    direction: int, triple: tuple[int, int, int]
) -> tuple[tuple, tuple, tuple]:
    """Per-sector raw occupation recoil, in lattice units.

    Matter recoils from D[direction] to D[matter]; the field and auxiliary
    sectors start empty, so their recoil is their whole occupation.  This is
    the reading Cycle 868 takes: an unweighted per-sector vector whose sector
    sum is the conformal channel.
    """
    unit = DIRECTIONS[direction]
    return (
        vec_sub(DIRECTIONS[triple[0]], unit),
        DIRECTIONS[triple[1]],
        DIRECTIONS[triple[2]],
    )


def sector_trace(ledger) -> tuple:
    total = (0, 0, 0)
    for sector_vector in ledger:
        total = vec_add(total, sector_vector)
    return total


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
        tree = ast.parse(payload, filename=path)
        names: set = set()
        for node in tree.body:
            if isinstance(
                node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)
            ):
                names.add(node.name)
            elif isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        names.add(target.id)
            elif isinstance(node, ast.AnnAssign) and isinstance(
                node.target, ast.Name
            ):
                names.add(node.target.id)
        present = set(REQUIRED_AST_MARKERS[path]) <= names
        missing_quotes = tuple(
            quote for quote in REQUIRED_QUOTES[path] if quote not in text
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
            "AST_valid": True,
            "required_markers": REQUIRED_AST_MARKERS[path],
            "required_markers_present": present,
            "required_quote_count": len(REQUIRED_QUOTES[path]),
            "missing_quotes": missing_quotes,
            "access": "TEXT_AST_ONLY_BLOCKLISTED_PRIMARY",
        })
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_path_count": len(AUDIT_INPUT_PATHS),
        "read_cap": 6,
        "source_rows": tuple(rows),
        "all_markers_present": markers_ok,
        "all_quotes_present": quotes_ok,
        "recovered_DIRECTIONS": DIRECTIONS,
        "recovered_REVERSE_cycle320": REVERSE_320,
        "recovered_REVERSE_cycle318": REVERSE_318,
        "reverse_agrees_across_primaries": REVERSE_320 == REVERSE_318,
        "BLOCKLIST": BLOCKLISTED_MODULES,
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(FIREWALL.hits),
        "executable_science_inputs": (),
    }
    result["sources_pass"] = (
        len(rows) <= 6
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
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
    )
    return result


# --------------------------------------------------------------------------
# certificate B -- the forcing step
# --------------------------------------------------------------------------
def forcing_certificate() -> dict:
    unit = (Fraction(1), Fraction(1), Fraction(1))
    support = c320_support()

    # The exchange E has exactly two nonzero entries per direction, both
    # connecting the single-quantum index d to the triple index.  P is
    # diagonal, so [E, P][i][j] = E[i][j] * (P[j] - P[i]); the commutator
    # vanishes exactly when every supported pair carries equal P eigenvalue.
    pair_rows = []
    all_pairs_equal = True
    for direction, triple in support:
        left = tuple(Fraction(component) for component in DIRECTIONS[direction])
        right = momentum_eigenvalue(triple, unit)
        defect = vec_sub(right, left)
        equal = vec_zero(defect)
        all_pairs_equal = all_pairs_equal and equal
        ledger = raw_ledger(direction, triple)
        pair_rows.append({
            "direction": direction,
            "unit_vector": DIRECTIONS[direction],
            "triple": triple,
            "triple_index": triple_index(*triple),
            "P_single": tuple(str(value) for value in left),
            "P_triple": tuple(str(value) for value in right),
            "P_eigenvalues_equal": equal,
            "raw_ledger": ledger,
            "sector_trace": sector_trace(ledger),
            "conservation_defect": tuple(str(value) for value in defect),
        })

    # Route 1: the sector trace, summed sector by sector off the ledger.
    # Route 2: the conservation defect P(triple) - P(single).
    # These are two textually independent computations; the certificate gates
    # on their AGREEMENT, and separately reports what they agree on.
    routes_agree = all(
        tuple(Fraction(component) for component in row["sector_trace"])
        == tuple(Fraction(value) for value in row["conservation_defect"])
        for row in pair_rows
    )
    traces = tuple(row["sector_trace"] for row in pair_rows)
    trace_bearing = tuple(row for row in pair_rows if not vec_zero(row["sector_trace"]))

    # [V(c,s), P] = c [E^2, P] + i s [E, P] for V = I + c E^2 + i s E, so the
    # commutator is the zero matrix for EVERY angle once [E, P] = 0 -- a
    # polynomial identity in the two free indeterminates c = cos(a) - 1 and
    # s = sin(a), not a sampled check.  [E^2, P] is implied because E maps
    # each supported pair into itself.
    angle_free = all_pairs_equal

    coefficients = tuple(
        tuple(
            # each raw ledger row is collinear with the carried unit vector on
            # this support, so record it as an integer multiple of that unit
            next(
                (
                    Fraction(row_component, unit_component)
                    for row_component, unit_component in zip(
                        sector_vector, DIRECTIONS[row["direction"]]
                    )
                    if unit_component != 0
                ),
                Fraction(0),
            )
            for sector_vector in row["raw_ledger"]
        )
        for row in pair_rows
    )
    coefficients_uniform = len(set(coefficients)) == 1
    landed_coefficients = tuple(int(value) for value in coefficients[0])

    result = {
        "construction": (
            "Cycle-320 link_recoil_vertex: for each of the six signed axis "
            "directions d the exchange connects the single matter quantum |d> "
            "to the triple (matter, field, auxiliary) = (REVERSE[d], d, d) at "
            "pair index 6 + 36*m + 6*f + a, and the momentum diagonal carries "
            "unit sector weights D[m] + D[f] + D[a]."
        ),
        "quoted_pair_index_line":
            "pair_index = 6 + 36 * REVERSE[direction] + 6 * direction + direction",
        "quoted_balance_residual":
            "final_matter + final_field + final_auxiliary - initial_vector",
        "quoted_certified_check": (
            "the direction-changing carried-link vertex has exact unit-weight "
            "Q/P operator balance and nonzero matter recoil"
        ),
        "support_rows": tuple(pair_rows),
        "every_supported_pair_has_equal_P_eigenvalue": all_pairs_equal,
        "commutator_argument": (
            "[E,P][i][j] = E[i][j]*(P[j]-P[i]); P is diagonal and E is "
            "supported only on pairs of equal P eigenvalue, so [E,P] is the "
            "zero matrix over the integers. V = I + c E^2 + i s E with "
            "c = cos(angle)-1 and s = sin(angle), so [V,P] = c[E^2,P] + "
            "i s[E,P] = 0 identically in the free indeterminates (c,s): the "
            "vanishing is angle-independent as a polynomial identity, not a "
            "sampled coincidence."
        ),
        "commutator_vanishes_for_every_angle": angle_free,
        "trace_route_1": "sum over sectors of the raw occupation recoil",
        "trace_route_2": "P(triple) - P(single), the conservation defect",
        "two_routes_agree_entrywise": routes_agree,
        "observed_sector_traces": traces,
        "trace_bearing_support_rows": len(trace_bearing),
        "ledger_coefficients_uniform_across_directions": coefficients_uniform,
        "landed_ledger_coefficients": landed_coefficients,
        "landed_ledger_scaled": tuple(
            tuple(coefficient * weight for coefficient in landed_coefficients)
            for weight in WEIGHTS
        ),
        "matches_cycle868_landed_ledger": tuple(landed_coefficients) == (-2, 1, 1),
        "finding": (
            "The forcing step is located exactly. The sector trace of the "
            "Cycle-320 recoil ledger is not an independent fact about the "
            "ledger: it is identically the conservation defect P(triple) - "
            "P(single) of the unit-weight vector balance that Cycle-320 "
            "certifies under the quoted check, i.e. the balance_residual "
            "vector 'final_matter + final_field + final_auxiliary - "
            "initial_vector' quoted verbatim from the pinned source. Two "
            "textually independent routes to that number agree entry for "
            "entry on all six directions. The exchange is supported only on "
            "pairs of equal momentum eigenvalue, so the commutator vanishes "
            "as a polynomial identity in cos(angle)-1 and sin(angle): no "
            "choice of the coupling angle can move it. The ledger read off "
            "this support is (-2, +1, +1) in every direction, reproducing the "
            "frozen Cycle-868 ledger (-2d, +d, +d) under carried weight d."
        ),
    }
    result["pass"] = (
        routes_agree
        and coefficients_uniform
        and result["matches_cycle868_landed_ledger"]
        and len(pair_rows) == len(DIRECTIONS)
        and all(row["triple_index"] >= 6 for row in pair_rows)
    )
    return result


# --------------------------------------------------------------------------
# certificate C -- exhaustive sweep of the constructor's target freedom
# --------------------------------------------------------------------------
def exhaustive_certificate() -> dict:
    unit = (Fraction(1), Fraction(1), Fraction(1))
    sector_count = len(SECTORS)
    direction_count = len(DIRECTIONS)
    lawful = 0
    lawful_trace_bearing = 0
    lawful_collinear = 0
    lawful_noncollinear = 0
    lawful_nonzero_matter_recoil = 0
    unlawful = 0
    routes_agree = True
    nonzero_trace_norms: set = set()
    trace_norm_histogram: dict = {}
    landed_present = False
    noncollinear_examples = []
    for direction in range(direction_count):
        unit_vector = DIRECTIONS[direction]
        for triple in product(range(direction_count), repeat=sector_count):
            ledger = raw_ledger(direction, triple)
            trace = sector_trace(ledger)
            defect = vec_sub(
                momentum_eigenvalue(triple, unit),
                tuple(Fraction(component) for component in unit_vector),
            )
            if tuple(Fraction(value) for value in trace) != tuple(defect):
                routes_agree = False
            norm = int(l1(trace))
            trace_norm_histogram[norm] = trace_norm_histogram.get(norm, 0) + 1
            if norm:
                nonzero_trace_norms.add(norm)
            is_lawful = vec_zero(defect)
            if not is_lawful:
                unlawful += 1
                continue
            lawful += 1
            if not vec_zero(trace):
                lawful_trace_bearing += 1
            if not vec_zero(ledger[0]):
                lawful_nonzero_matter_recoil += 1
            collinear = all(
                vec_zero(sector_vector)
                or any(
                    sector_vector == vec_scale(scale, unit_vector)
                    for scale in range(-3, 4)
                )
                for sector_vector in ledger
            )
            if collinear:
                lawful_collinear += 1
            else:
                lawful_noncollinear += 1
                if len(noncollinear_examples) < 4:
                    noncollinear_examples.append({
                        "direction": direction,
                        "triple": triple,
                        "raw_ledger": ledger,
                        "sector_trace": trace,
                    })
            if direction == 0 and triple == (REVERSE_320[0], 0, 0):
                landed_present = True
    total = direction_count * direction_count ** sector_count
    minimum_nonzero_norm = min(nonzero_trace_norms) if nonzero_trace_norms else 0
    result = {
        "sweep_declaration": (
            "the constructor's target freedom at fixed unit sector grading: "
            "for each of the 6 carried directions, every one of the 6^3 "
            "possible (matter, field, auxiliary) target triples of the "
            "carried-link exchange, with no other structure held fixed"
        ),
        "sweep_holds_all_three_sectors_occupied": True,
        "degree_of_freedom_left_outside_this_sweep": (
            "sector OCCUPANCY -- this sweep varies where each of the three "
            "sectors points but always has all three occupied. A sector "
            "carrying grading weight zero is a momentum spectator and can be "
            "absent altogether; that freedom is priced in certificates D and E, "
            "not here"
        ),
        "triples_swept": total,
        "closed_form": "6 * 6^3",
        "closed_form_matches": total == 6 * 6 ** 3,
        "lawful_count": lawful,
        "unlawful_count": unlawful,
        "lawful_plus_unlawful_is_total": lawful + unlawful == total,
        "lawful_trace_bearing_count": lawful_trace_bearing,
        "lawful_with_nonzero_matter_recoil": lawful_nonzero_matter_recoil,
        "lawful_collinear_count": lawful_collinear,
        "lawful_noncollinear_count": lawful_noncollinear,
        "cycle868_rank1_ansatz_is_strict_subset":
            lawful_noncollinear > 0 and lawful_collinear < lawful,
        "noncollinear_lawful_examples": tuple(noncollinear_examples),
        "landed_triple_recovered_in_sweep": landed_present,
        "two_routes_agree_on_every_triple": routes_agree,
        "trace_L1_norm_histogram": dict(sorted(trace_norm_histogram.items())),
        "minimum_nonzero_trace_L1_norm": minimum_nonzero_norm,
        "trace_lattice": "Z^3 -- every sector trace is a sum of four signed unit vectors",
        "finding": (
            f"The sweep is exhaustive over the constructor's target freedom at "
            f"unit grading: all {total} triples, of which {lawful} are lawful "
            f"(zero conservation defect) and {unlawful} are not. Exactly "
            f"{lawful_trace_bearing} lawful triples bear trace. The vanishing "
            f"is therefore not an artefact of the Cycle-868 parameterisation: "
            f"868 carries the ledger as a single unit direction times three "
            f"sector coefficients, a rank-one ansatz that covers only "
            f"{lawful_collinear} of the {lawful} lawful triples, yet the "
            f"remaining {lawful_noncollinear} non-collinear lawful triples are "
            f"traceless too. The escape is also not reachable by detuning: "
            f"every sector trace lies in Z^3, so the smallest nonzero trace has "
            f"L1 norm {minimum_nonzero_norm} -- a finite lattice step away from "
            f"the lawful set, with no infinitesimal perturbation in between."
        ),
    }
    result["pass"] = (
        result["closed_form_matches"]
        and result["lawful_plus_unlawful_is_total"]
        and routes_agree
        and landed_present
        and lawful > 0
        and isinstance(lawful_trace_bearing, int)
    )
    return result


# --------------------------------------------------------------------------
# certificate D -- is the unit grading itself forced?
# --------------------------------------------------------------------------
def grading_certificate() -> dict:
    sector_count = len(SECTORS)
    direction_count = len(DIRECTIONS)
    rows = []
    lawful_by_grading: dict = {}
    traceless_nonzero_recoil_gradings: set = set()
    trace_bearing_nonzero_recoil_gradings: set = set()
    # A conjecture put up to be killed: that the only non-unit gradings whose
    # lawful supports stay traceless are the zero-matter-recoil ones Cycle-320
    # already rejects.  The sweep decides it; nothing below assumes it.
    conjecture_nonunit_traceless_implies_zero_recoil = True
    conjecture_counterexamples = []
    decomposition_holds = True
    trace_bearing_examples = []
    for field_weight in GRADING_GRID:
        for auxiliary_weight in GRADING_GRID:
            grading = (Fraction(1), field_weight, auxiliary_weight)
            key = f"(1,{field_weight},{auxiliary_weight})"
            lawful = 0
            traceless = 0
            trace_bearing = 0
            nonzero_recoil_traceless = 0
            nonzero_recoil_trace_bearing = 0
            for direction in range(direction_count):
                unit_vector = tuple(
                    Fraction(component) for component in DIRECTIONS[direction]
                )
                for triple in product(range(direction_count), repeat=sector_count):
                    defect = vec_sub(
                        momentum_eigenvalue(triple, grading), unit_vector
                    )
                    ledger = raw_ledger(direction, triple)
                    trace = sector_trace(ledger)
                    # trace = defect_w + sum_s (1 - w_s) * occupation_s.  Both
                    # sides are recomputed independently and compared; this is
                    # the identity that explains every row of the sweep.
                    reconstructed = defect
                    for sector in range(sector_count):
                        reconstructed = vec_add(
                            reconstructed,
                            vec_scale(
                                Fraction(1) - grading[sector],
                                DIRECTIONS[triple[sector]],
                            ),
                        )
                    if tuple(Fraction(value) for value in trace) != reconstructed:
                        decomposition_holds = False
                    if not vec_zero(defect):
                        continue
                    lawful += 1
                    matter_moves = not vec_zero(ledger[0])
                    if vec_zero(trace):
                        traceless += 1
                        if matter_moves:
                            nonzero_recoil_traceless += 1
                            traceless_nonzero_recoil_gradings.add(key)
                            if grading[1:] != (Fraction(1), Fraction(1)):
                                conjecture_nonunit_traceless_implies_zero_recoil = False
                                if len(conjecture_counterexamples) < 3:
                                    conjecture_counterexamples.append({
                                        "grading": key,
                                        "direction": direction,
                                        "triple": triple,
                                        "raw_ledger": ledger,
                                    })
                    else:
                        trace_bearing += 1
                        if matter_moves:
                            nonzero_recoil_trace_bearing += 1
                            trace_bearing_nonzero_recoil_gradings.add(key)
                            if len(trace_bearing_examples) < 3:
                                trace_bearing_examples.append({
                                    "grading": key,
                                    "direction": direction,
                                    "triple": triple,
                                    "raw_ledger": ledger,
                                    "sector_trace": trace,
                                })
            lawful_by_grading[key] = lawful
            if lawful:
                rows.append({
                    "grading": key,
                    "lawful_supports": lawful,
                    "traceless": traceless,
                    "trace_bearing": trace_bearing,
                    "traceless_with_nonzero_matter_recoil": nonzero_recoil_traceless,
                    "trace_bearing_with_nonzero_matter_recoil":
                        nonzero_recoil_trace_bearing,
                })
    unit_key = "(1,1,1)"
    unit_admits_trace_bearing = unit_key in trace_bearing_nonzero_recoil_gradings
    every_trace_bearing_grading_nonunit = all(
        key != unit_key for key in trace_bearing_nonzero_recoil_gradings
    )

    # The lawful grading locus for the landed support (m,f,a) = (rev d, d, d):
    # 1*(-1) + w_field*(+1) + w_auxiliary*(+1) = +1, i.e. the SEGMENT
    # w_field + w_auxiliary = 2.  Verify it on the grid rather than assert it.
    landed_support_lawful_gradings = tuple(
        f"(1,{field_weight},{auxiliary_weight})"
        for field_weight in GRADING_GRID
        for auxiliary_weight in GRADING_GRID
        if vec_zero(
            vec_sub(
                momentum_eigenvalue(
                    (REVERSE_320[0], 0, 0),
                    (Fraction(1), field_weight, auxiliary_weight),
                ),
                tuple(Fraction(component) for component in DIRECTIONS[0]),
            )
        )
    )
    result = {
        "question": (
            "the unit sector grading (1,1,1) is what makes the sector trace "
            "coincide with the conserved balance; is that grading forced?"
        ),
        "grading_grid": tuple(str(value) for value in GRADING_GRID),
        "grading_grid_declaration": (
            "matter weight normalised to 1 by the single-quantum block; field "
            "and auxiliary weights swept over halves from 0 to 3"
        ),
        "gradings_swept": len(GRADING_GRID) ** 2,
        "grading_rows": tuple(rows),
        "gradings_with_lawful_supports": len(rows),
        "landed_support_lawful_grading_locus": landed_support_lawful_gradings,
        "landed_support_locus_is_a_segment_not_a_point":
            len(landed_support_lawful_gradings) > 1,
        "unit_grading_on_locus":
            "(1,1,1)" in landed_support_lawful_gradings,
        "cycle318_grading_on_locus":
            "(1,2,0)" in landed_support_lawful_gradings,
        "gradings_admitting_traceless_nonzero_recoil":
            tuple(sorted(traceless_nonzero_recoil_gradings)),
        "gradings_admitting_trace_bearing_nonzero_recoil":
            tuple(sorted(trace_bearing_nonzero_recoil_gradings)),
        "unit_grading_admits_a_trace_bearing_lawful_support":
            unit_admits_trace_bearing,
        "every_trace_bearing_grading_is_nonunit":
            every_trace_bearing_grading_nonunit,
        "trace_bearing_examples": tuple(trace_bearing_examples),
        "trace_decomposition":
            "trace = defect_w + sum_s (1 - w_s) * occupation_s",
        "trace_decomposition_holds_on_every_swept_pair": decomposition_holds,
        "raw_ledger_depends_only_on_the_support_not_the_grading": True,
        "conjecture_tested_nonunit_traceless_implies_zero_matter_recoil":
            conjecture_nonunit_traceless_implies_zero_recoil,
        "conjecture_status": (
            "REFUTED_BY_THIS_SWEEP"
            if not conjecture_nonunit_traceless_implies_zero_recoil
            else "NOT_REFUTED"
        ),
        "conjecture_counterexamples": tuple(conjecture_counterexamples),
        "quoted_cycle318_self_declaration": (
            "P = P_matter + 2 P_mediator at operator level. ... is supplied "
            "candidate-law structure"
        ),
        "quoted_cycle320_route_tuple": N1_ROUTES,
        "cycle318_route_named_by_cycle320":
            "Cycle-318 coefficient-two recoil source" in N1_ROUTES,
        "finding": (
            f"The unit grading is not forced. Holding the landed support "
            f"(REVERSE[d], d, d) fixed, the gradings that conserve the vector "
            f"ledger form the whole segment w_field + w_auxiliary = 2, meeting "
            f"the declared grid in {len(landed_support_lawful_gradings)} points, "
            f"not one: the unit grading (1,1,1) and the Cycle-318 "
            f"coefficient-two grading (1,2,0) both lie on it. The sweep also "
            f"kills a conjecture this cycle put up on purpose -- that non-unit "
            f"gradings could only stay traceless by having no matter recoil. "
            f"Status: {'REFUTED' if not conjecture_nonunit_traceless_implies_zero_recoil else 'NOT REFUTED'}. "
            f"The reason is the decomposition trace = defect_w + sum_s "
            f"(1 - w_s) * occupation_s, which holds on every swept pair: the "
            f"raw occupation ledger is a function of the SUPPORT alone and does "
            f"not move when the grading moves, so the landed traceless support "
            f"stays lawful and traceless all along the segment. What the "
            f"grading changes is WHICH supports are lawful, and there the "
            f"asymmetry is sharp and computed: every grading admitting a lawful "
            f"trace-bearing support with nonzero matter recoil is non-unit "
            f"({', '.join(sorted(trace_bearing_nonzero_recoil_gradings))}), and "
            f"the unit grading admits none. Tracelessness is thus guaranteed "
            f"only at w = (1,1,1); anywhere else on the lawful segment it "
            f"becomes a property of the particular support rather than of the "
            f"construction. Cycle-318 declares its own coefficient two to be "
            f"supplied candidate-law structure and Cycle-320 lists that route "
            f"by name in its own route tuple, so the grading that carries the "
            f"guarantee is a SUPPLIED input, not a derived one."
        ),
    }
    result["pass"] = (
        len(rows) > 0
        and decomposition_holds
        and result["landed_support_locus_is_a_segment_not_a_point"]
        and result["unit_grading_on_locus"]
        and result["cycle318_route_named_by_cycle320"]
        and every_trace_bearing_grading_nonunit
        and not unit_admits_trace_bearing
        and sum(lawful_by_grading.values()) > 0
    )
    return result


# --------------------------------------------------------------------------
# certificate E -- the trace-bearing witness, rebuilt from Cycle-318
# --------------------------------------------------------------------------
def witness_certificate() -> dict:
    unit_two_sector = (Fraction(1), Fraction(1))
    c318_grading = (Fraction(1), Fraction(2))
    rows = []
    weighted_conserved = True
    unit_conserved_anywhere = False
    defect_equals_trace = True
    for direction in range(len(DIRECTIONS)):
        pair = (REVERSE_318[direction], direction)
        unit_vector = tuple(Fraction(value) for value in DIRECTIONS[direction])
        weighted = vec_sub(
            vec_add(
                vec_scale(c318_grading[0], DIRECTIONS[pair[0]]),
                vec_scale(c318_grading[1], DIRECTIONS[pair[1]]),
            ),
            unit_vector,
        )
        unweighted = vec_sub(
            vec_add(
                vec_scale(unit_two_sector[0], DIRECTIONS[pair[0]]),
                vec_scale(unit_two_sector[1], DIRECTIONS[pair[1]]),
            ),
            unit_vector,
        )
        raw = (
            vec_sub(DIRECTIONS[pair[0]], DIRECTIONS[direction]),
            DIRECTIONS[pair[1]],
            (0, 0, 0),
        )
        trace = sector_trace(raw)
        weighted_conserved = weighted_conserved and vec_zero(weighted)
        unit_conserved_anywhere = unit_conserved_anywhere or vec_zero(unweighted)
        if tuple(Fraction(value) for value in trace) != tuple(unweighted):
            defect_equals_trace = False
        rows.append({
            "direction": direction,
            "pair_index": 6 + 6 * pair[0] + pair[1],
            "matter_target": pair[0],
            "mediator_target": pair[1],
            "weighted_defect_P_matter_plus_2_P_mediator":
                tuple(str(value) for value in weighted),
            "unit_grading_defect": tuple(str(value) for value in unweighted),
            "raw_occupation_ledger_3sector_embedding": raw,
            "sector_trace": trace,
            "matter_recoil_nonzero": not vec_zero(raw[0]),
        })
    collinear = all(
        row["sector_trace"] == vec_scale(-1, DIRECTIONS[row["direction"]])
        for row in rows
    )
    witness_coefficients = (-2, 1, 0)
    result = {
        "witness_route": "Cycle-318 direction_vertex, the coefficient-two recoil source",
        "witness_provenance": (
            "not invented here: the route is enumerated by name inside "
            "Cycle-320's own N1_ROUTES tuple and Cycle-318 is imported by "
            "Cycle-320 and run as a certified comparator"
        ),
        "quoted_pair_index_line": "pair_index = 6 + 6 * REVERSE[direction] + direction",
        "quoted_momentum_line": "mediator_weight * c210.DIRECTIONS[field, axis]",
        "conserved_functional": "P = P_matter + 2 P_mediator",
        "witness_rows": tuple(rows),
        "weighted_functional_conserved_on_every_direction": weighted_conserved,
        "unit_grading_conserved_anywhere": unit_conserved_anywhere,
        "unit_grading_defect_equals_sector_trace": defect_equals_trace,
        "sector_trace_collinear_with_minus_carried_unit": collinear,
        "witness_ledger_coefficients": witness_coefficients,
        "witness_ledger_sector_sum": sum(witness_coefficients),
        "witness_ledger_scaled": tuple(
            tuple(coefficient * weight for coefficient in witness_coefficients)
            for weight in WEIGHTS
        ),
        "witness_ledger_sector_sums_scaled": tuple(
            sum(coefficient * weight for coefficient in witness_coefficients)
            for weight in WEIGHTS
        ),
        "matter_recoil_nonzero_everywhere": all(
            row["matter_recoil_nonzero"] for row in rows
        ),
        "auxiliary_sector_unoccupied": True,
        "why_certificate_C_does_not_see_this_variant": (
            "certificate C sweeps target triples with all three sectors "
            "occupied. This witness has the auxiliary sector ABSENT, which is "
            "only lawful because the Cycle-318 grading gives that sector weight "
            "zero, making it a momentum spectator. The escape therefore lives "
            "in sector occupancy, and occupancy is what the grading unlocks"
        ),
        "finding": (
            "The trace-bearing lawful variant is exhibited and it is landed "
            "repo structure, not new physics. Cycle-318's direction_vertex "
            "sends |d> to (matter, mediator) = (REVERSE[d], d) and conserves "
            "P_matter + 2 P_mediator exactly on all six directions, with "
            "nonzero matter recoil everywhere -- so it clears the same "
            "retention bar Cycle-320 applies. Read in the unweighted sector "
            "convention Cycle 868 uses, its occupation ledger embeds at the "
            "868 scope as (-2, +1, 0) per unit carried weight, i.e. "
            "(-2d, +d, 0), whose sector sum is -d and whose trace is exactly "
            "minus the carried unit direction. The unit-grading defect and the "
            "sector trace agree entry for entry, which is the same identity as "
            "in certificate B running the other way: the ledger bears trace "
            "precisely because its conserved grading is not the unit one."
        ),
    }
    result["pass"] = (
        weighted_conserved
        and defect_equals_trace
        and len(rows) == len(DIRECTIONS)
        and result["matter_recoil_nonzero_everywhere"]
    )
    return result


# --------------------------------------------------------------------------
# the Cycle-868 census machinery, re-derived minimally from its definitions
# --------------------------------------------------------------------------
SIGMA_DIRECTIONS = DIRECTIONS


def enumerate_family() -> tuple:
    members = []
    for endpoint in range(len(ENDPOINTS)):
        for direction in range(len(DIRECTIONS)):
            for weight in WEIGHTS:
                members.append(("k1", endpoint, direction, weight))
    for left_direction in range(len(DIRECTIONS)):
        for left_weight in WEIGHTS:
            for right_direction in range(len(DIRECTIONS)):
                for right_weight in WEIGHTS:
                    members.append((
                        "k2", left_direction, left_weight,
                        right_direction, right_weight,
                    ))
    return tuple(members)


def member_sources(member) -> tuple:
    if member[0] == "k1":
        return ((member[1], member[2], member[3]),)
    return ((0, member[1], member[2]), (1, member[3], member[4]))


def source_array(member, ledger) -> tuple:
    grid = [
        [[ZERO for _axis in range(AXES)] for _sector in SECTORS]
        for _endpoint in ENDPOINTS
    ]
    for endpoint, direction, weight in member_sources(member):
        coefficients = ledger(weight)
        unit = SIGMA_DIRECTIONS[direction]
        for sector, coefficient in enumerate(coefficients):
            for axis in range(AXES):
                grid[endpoint][sector][axis] += Fraction(coefficient * unit[axis])
    return tuple(
        tuple(tuple(row) for row in block) for block in grid
    )


def lift_to_poly(array) -> tuple:
    return tuple(
        tuple(
            tuple(p_const(array[endpoint][sector][axis]) for axis in range(AXES))
            for sector in range(len(SECTORS))
        )
        for endpoint in range(len(ENDPOINTS))
    )


def grading_operator(poly_array, live: bool = True) -> tuple:
    """G_sigma = Pi_tracefree + sigma * Pi_conformal on the sector index."""
    degree = 1 if live else 0
    out = []
    for endpoint in range(len(ENDPOINTS)):
        block = []
        conformal_axis = tuple(
            p_scale(
                p_add(
                    p_add(poly_array[endpoint][0][axis],
                          poly_array[endpoint][1][axis]),
                    poly_array[endpoint][2][axis],
                ),
                THIRD,
            )
            for axis in range(AXES)
        )
        for sector in range(len(SECTORS)):
            row = []
            for axis in range(AXES):
                tracefree = p_add(
                    poly_array[endpoint][sector][axis],
                    p_scale(conformal_axis[axis], Fraction(-1)),
                )
                row.append(p_add(tracefree, p_shift(conformal_axis[axis], degree)))
            block.append(tuple(row))
        out.append(tuple(block))
    return tuple(out)


def endpoint_exchange(graded) -> tuple:
    return tuple(
        graded[len(ENDPOINTS) - 1 - endpoint] for endpoint in range(len(ENDPOINTS))
    )


def response_objects(array, live: bool = True) -> dict:
    graded = grading_operator(lift_to_poly(array), live)
    pushed = endpoint_exchange(graded)
    stage_two = endpoint_exchange(graded)
    stage_three = endpoint_exchange(stage_two)
    pulled = grading_operator(stage_three, live)

    o1 = tuple(
        pushed[endpoint][sector][axis]
        for endpoint in range(len(ENDPOINTS))
        for sector in range(len(SECTORS))
        for axis in range(AXES)
    )
    o2 = tuple(
        pulled[endpoint][sector][axis]
        for endpoint in range(len(ENDPOINTS))
        for sector in range(len(SECTORS))
        for axis in range(AXES)
    )
    o3 = tuple(
        p_add(
            p_add(pushed[endpoint][0][axis], pushed[endpoint][1][axis]),
            pushed[endpoint][2][axis],
        )
        for endpoint in range(len(ENDPOINTS))
        for axis in range(AXES)
    )
    gram: Poly = POLY_ZERO
    for value in o1:
        gram = p_add(gram, p_mul(value, value))
    o5_rows = []
    for endpoint in range(len(ENDPOINTS)):
        for left_axis in range(AXES):
            for right_axis in range(AXES):
                entry: Poly = POLY_ZERO
                for sector in range(len(SECTORS)):
                    entry = p_add(entry, p_mul(
                        pushed[endpoint][sector][left_axis],
                        pushed[endpoint][sector][right_axis],
                    ))
                o5_rows.append(entry)
    transfer: Poly = POLY_ZERO
    for sector in range(len(SECTORS)):
        for axis in range(AXES):
            transfer = p_add(transfer, p_mul(
                graded[0][sector][axis], graded[1][sector][axis]
            ))
    return {
        "O1_PUSHFORWARD": o1,
        "O2_ADJOINT_PULLBACK": o2,
        "O3_FLUX_BALANCE": o3,
        "O4_RESPONSE_GRAM": (gram,),
        "O5_RESPONSE_TENSOR": tuple(o5_rows),
        "O6_EDGE_TRANSFER": (transfer,),
    }


def numeric_objects(array, sign: int, live: bool = True) -> dict:
    """The same pipeline with sigma substituted BEFORE any algebra.

    This is the polynomial-free cross route: sigma is a plain Fraction from the
    start, so nothing about the census can depend on the polynomial layer.
    """
    scale = Fraction(sign) if live else Fraction(1)
    graded = []
    for endpoint in range(len(ENDPOINTS)):
        conformal_axis = tuple(
            THIRD * sum(
                (array[endpoint][sector][axis] for sector in range(len(SECTORS))),
                ZERO,
            )
            for axis in range(AXES)
        )
        graded.append(tuple(
            tuple(
                array[endpoint][sector][axis] - conformal_axis[axis]
                + scale * conformal_axis[axis]
                for axis in range(AXES)
            )
            for sector in range(len(SECTORS))
        ))
    graded = tuple(graded)
    pushed = endpoint_exchange(graded)
    stage_three = endpoint_exchange(endpoint_exchange(graded))
    pulled = []
    for endpoint in range(len(ENDPOINTS)):
        conformal_axis = tuple(
            THIRD * sum(
                (stage_three[endpoint][sector][axis]
                 for sector in range(len(SECTORS))),
                ZERO,
            )
            for axis in range(AXES)
        )
        pulled.append(tuple(
            tuple(
                stage_three[endpoint][sector][axis] - conformal_axis[axis]
                + scale * conformal_axis[axis]
                for axis in range(AXES)
            )
            for sector in range(len(SECTORS))
        ))
    pulled = tuple(pulled)
    o1 = tuple(
        pushed[e][s][a]
        for e in range(len(ENDPOINTS))
        for s in range(len(SECTORS))
        for a in range(AXES)
    )
    o2 = tuple(
        pulled[e][s][a]
        for e in range(len(ENDPOINTS))
        for s in range(len(SECTORS))
        for a in range(AXES)
    )
    o3 = tuple(
        sum((pushed[e][s][a] for s in range(len(SECTORS))), ZERO)
        for e in range(len(ENDPOINTS))
        for a in range(AXES)
    )
    o4 = (sum((value * value for value in o1), ZERO),)
    o5 = tuple(
        sum(
            (pushed[e][s][left] * pushed[e][s][right]
             for s in range(len(SECTORS))),
            ZERO,
        )
        for e in range(len(ENDPOINTS))
        for left in range(AXES)
        for right in range(AXES)
    )
    o6 = (sum(
        (graded[0][s][a] * graded[1][s][a]
         for s in range(len(SECTORS)) for a in range(AXES)),
        ZERO,
    ),)
    return {
        "O1_PUSHFORWARD": o1,
        "O2_ADJOINT_PULLBACK": o2,
        "O3_FLUX_BALANCE": o3,
        "O4_RESPONSE_GRAM": o4,
        "O5_RESPONSE_TENSOR": o5,
        "O6_EDGE_TRANSFER": o6,
    }


LANDED_LEDGER = lambda weight: (-2 * weight, weight, weight)
WITNESS_LEDGER = lambda weight: (-2 * weight, weight, 0)
LEDGERS = (
    ("LANDED_cycle320_unit_grading", LANDED_LEDGER, "(-2d,+d,+d)"),
    ("WITNESS_cycle318_coefficient_two", WITNESS_LEDGER, "(-2d,+d,0)"),
)


def run_census(members, ledger, live: bool = True) -> dict:
    sensitive = {name: 0 for name in OBJECT_NAMES}
    blind = {name: 0 for name in OBJECT_NAMES}
    witnesses: dict = {}
    routes_agree = True
    arity_ok = True
    degree_ok = True
    stream = []
    for member in members:
        array = source_array(member, ledger)
        objects = response_objects(array, live)
        plus = numeric_objects(array, 1, live)
        minus = numeric_objects(array, -1, live)
        for name in OBJECT_NAMES:
            values = objects[name]
            if len(values) != OBJECT_ARITY[name]:
                arity_ok = False
            hit = False
            for index, poly in enumerate(values):
                if p_degree(poly) > SIGMA_DEGREE_BOUND:
                    degree_ok = False
                at_plus = p_eval(poly, 1)
                at_minus = p_eval(poly, -1)
                if at_plus != plus[name][index] or at_minus != minus[name][index]:
                    routes_agree = False
                if at_plus != at_minus:
                    hit = True
                    if name not in witnesses:
                        witnesses[name] = {
                            "member": member,
                            "component_index": index,
                            "sigma_polynomial": p_text(poly),
                            "value_at_sigma_plus_one": str(at_plus),
                            "value_at_sigma_minus_one": str(at_minus),
                            "difference": str(at_plus - at_minus),
                        }
            if hit:
                sensitive[name] += 1
            else:
                blind[name] += 1
            stream.append(f"{member}|{name}|{'S' if hit else 'B'}")
    return {
        "sensitive": sensitive,
        "blind": blind,
        "witnesses": witnesses,
        "polynomial_and_numeric_routes_agree": routes_agree,
        "arity_exact": arity_ok,
        "sigma_degree_within_bound": degree_ok,
        "stream_sha256": sha256("\n".join(stream).encode()).hexdigest(),
    }


def census_certificate(members) -> dict:
    rows = []
    censuses = {}
    for name, ledger, shape in LEDGERS:
        census = run_census(members, ledger)
        censuses[name] = census
        rows.append({
            "ledger": name,
            "shape": shape,
            "sector_sums": tuple(sum(ledger(weight)) for weight in WEIGHTS),
            "sensitive_objects": tuple(
                object_name for object_name in OBJECT_NAMES
                if census["sensitive"][object_name] > 0
            ),
            "blind_objects": tuple(
                object_name for object_name in OBJECT_NAMES
                if census["sensitive"][object_name] == 0
            ),
            "sensitive_counts": census["sensitive"],
            "blind_counts": census["blind"],
            "witnesses": census["witnesses"],
            "polynomial_and_numeric_routes_agree":
                census["polynomial_and_numeric_routes_agree"],
            "stream_sha256": census["stream_sha256"],
        })

    # Adversary control: with the sigma probe disabled (live=False) the census
    # must read blind for BOTH ledgers.  If the probe still fires, the census
    # is reading something other than sigma and nothing above is load-bearing.
    dead_rows = []
    probe_is_load_bearing = True
    for name, ledger, _shape in LEDGERS:
        dead = run_census(members, ledger, live=False)
        any_sensitive = any(dead["sensitive"][key] > 0 for key in OBJECT_NAMES)
        probe_is_load_bearing = probe_is_load_bearing and not any_sensitive
        dead_rows.append({
            "ledger": name,
            "sensitive_with_probe_disabled": dead["sensitive"],
        })

    landed = censuses["LANDED_cycle320_unit_grading"]
    witness = censuses["WITNESS_cycle318_coefficient_two"]
    newly_sensitive = tuple(
        name for name in OBJECT_NAMES
        if witness["sensitive"][name] > 0 and landed["sensitive"][name] == 0
    )
    still_blind = tuple(
        name for name in OBJECT_NAMES if witness["sensitive"][name] == 0
    )
    result = {
        "family_size": len(members),
        "family_closed_form": "2*6*6 + (6*6)^2",
        "family_closed_form_matches":
            len(members) == 2 * 6 * 6 + (6 * 6) ** 2,
        "objects": OBJECT_NAMES,
        "machinery": (
            "the Cycle-868 census re-derived here from its definitions -- the "
            "sigma grading G = Pi_tracefree + sigma Pi_conformal, the endpoint "
            "reversal R, the composite K = R R through the grading, and the "
            "six response objects -- with the 868 runner pinned and firewalled "
            "and never imported"
        ),
        "ledger_rows": tuple(rows),
        "probe_disabled_rows": tuple(dead_rows),
        "sigma_probe_is_load_bearing": probe_is_load_bearing,
        "objects_newly_sensitive_under_the_witness": newly_sensitive,
        "objects_still_blind_under_the_witness": still_blind,
        "all_routes_agree": all(
            row["polynomial_and_numeric_routes_agree"] for row in rows
        ),
        "arity_exact_everywhere": all(
            censuses[name]["arity_exact"] for name in censuses
        ),
        "sigma_degree_within_bound_everywhere": all(
            censuses[name]["sigma_degree_within_bound"] for name in censuses
        ),
        "finding": (
            f"Both ledgers are pushed through the whole {len(members)}-member "
            f"landed family. The frozen (-2d,+d,+d) ledger leaves every one of "
            f"the six response objects blind, reproducing Cycle 868 from an "
            f"independent re-derivation. The Cycle-318 witness ledger "
            f"(-2d,+d,0) makes {len(newly_sensitive)} objects sign-sensitive: "
            f"{', '.join(newly_sensitive) if newly_sensitive else 'none'}. "
            f"{len(still_blind)} objects stay blind even with trace present "
            f"({', '.join(still_blind) if still_blind else 'none'}), because "
            f"the trace-free channel is sector-orthogonal to the conformal one, "
            f"so every quadratic object's cross term vanishes and the pullback "
            f"applies the grading twice and returns sigma squared. The "
            f"sensitivity is therefore confined to the objects that are LINEAR "
            f"in the graded source. Each sensitive object is reported with an "
            f"explicit member, component and pair of exact rational readings at "
            f"sigma = +1 and sigma = -1, and every reading is confirmed by a "
            f"second polynomial-free route that substitutes sigma before any "
            f"algebra. With the sigma probe disabled the census reads blind for "
            f"both ledgers, so the probe is doing the work."
        ),
    }
    result["pass"] = (
        result["family_closed_form_matches"]
        and result["all_routes_agree"]
        and result["arity_exact_everywhere"]
        and result["sigma_degree_within_bound_everywhere"]
        and probe_is_load_bearing
        and all(
            set(row["sensitive_objects"]) | set(row["blind_objects"])
            == set(OBJECT_NAMES)
            for row in rows
        )
    )
    return result, censuses


# --------------------------------------------------------------------------
# certificate G -- the provenance verdict
# --------------------------------------------------------------------------
VERDICTS = (
    "TRACELESSNESS_DERIVED__ESCAPE_A_CLOSED_AT_SCOPE",
    "TRACELESSNESS_SUPPLIED_VIA_SECTOR_GRADING__ESCAPE_A_OPEN",
    "TRACELESSNESS_SUPPLIED_BUT_WITNESS_INERT__ESCAPE_A_OPEN_UNEXPLOITED",
    "PROVENANCE_UNRESOLVED",
)


def verdict_certificate(
    forcing, exhaustive, grading, witness, census
) -> dict:
    derived_at_unit = (
        forcing["two_routes_agree_entrywise"]
        and forcing["commutator_vanishes_for_every_angle"]
        and exhaustive["lawful_trace_bearing_count"] == 0
    )
    grading_supplied = (
        grading["landed_support_locus_is_a_segment_not_a_point"]
        and grading["cycle318_route_named_by_cycle320"]
    )
    witness_exists = (
        witness["weighted_functional_conserved_on_every_direction"]
        and witness["witness_ledger_sector_sum"] != 0
        and witness["matter_recoil_nonzero_everywhere"]
    )
    newly_sensitive = census["objects_newly_sensitive_under_the_witness"]
    if not derived_at_unit:
        verdict = "PROVENANCE_UNRESOLVED"
    elif not (grading_supplied and witness_exists):
        verdict = "TRACELESSNESS_DERIVED__ESCAPE_A_CLOSED_AT_SCOPE"
    elif newly_sensitive:
        verdict = "TRACELESSNESS_SUPPLIED_VIA_SECTOR_GRADING__ESCAPE_A_OPEN"
    else:
        verdict = "TRACELESSNESS_SUPPLIED_BUT_WITNESS_INERT__ESCAPE_A_OPEN_UNEXPLOITED"
    result = {
        "verdict": verdict,
        "verdict_enum": VERDICTS,
        "provenance_map": {
            "layer_1_ledger_given_the_support_and_the_unit_grading": "DERIVED",
            "layer_1_forcing_step": (
                "the sector trace IS the conservation defect certified by "
                "Cycle-320's unit-weight Q/P balance check; the exchange is "
                "supported only on equal-P pairs, so the commutator vanishes "
                "identically in the coupling angle"
            ),
            "layer_2_target_freedom_at_unit_grading": "DERIVED_EXHAUSTIVELY",
            "layer_2_scope": (
                f"all {exhaustive['triples_swept']} target triples swept with "
                f"all three sectors occupied; {exhaustive['lawful_count']} "
                f"lawful, {exhaustive['lawful_trace_bearing_count']} "
                f"trace-bearing; minimum nonzero trace L1 norm "
                f"{exhaustive['minimum_nonzero_trace_L1_norm']} so no "
                f"infinitesimal detuning exists"
            ),
            "layer_3_sector_grading_and_occupancy": "SUPPLIED",
            "layer_3_evidence": (
                "the lawful grading locus for the landed support is the "
                "segment w_field + w_auxiliary = 2, not a point; every grading "
                "admitting a lawful trace-bearing support with nonzero matter "
                "recoil is non-unit and the unit grading admits none, so the "
                "guarantee rides on w = (1,1,1); a sector at weight zero is a "
                "momentum spectator and may be absent, which is the occupancy "
                "door the witness walks through; Cycle-318's own text calls "
                "its coefficient two supplied candidate-law structure and "
                "Cycle-320 lists the route by name"
            ),
            "layer_4_consequence": (
                f"the witness ledger (-2d,+d,0) makes "
                f"{', '.join(newly_sensitive) if newly_sensitive else 'no'} "
                f"object(s) sign-sensitive"
            ),
        },
        "derived_at_fixed_unit_grading": derived_at_unit,
        "grading_is_supplied": grading_supplied,
        "lawful_trace_bearing_variant_exists": witness_exists,
        "sign_sensitive_objects_under_the_witness": newly_sensitive,
        "escape_a_status": (
            "OPEN" if verdict.endswith("ESCAPE_A_OPEN")
            or verdict.endswith("UNEXPLOITED") else "CLOSED_AT_SCOPE"
        ),
        "what_would_close_it": (
            "a derivation of the unit sector grading (1,1,1) from the axioms "
            "or approved primitives. Until that exists, Cycle 868's blindness "
            "result is conditional on a supplied grading, and the conditional "
            "should be carried explicitly wherever the blindness is used."
        ),
        "finding": (
            "The provenance is a split, and the split is the result. Given the "
            "unit sector grading, the ledger's tracelessness is DERIVED and "
            "exhaustively so: it is the conservation defect itself, it survives "
            "every coupling angle as a polynomial identity, no lawful target "
            "triple anywhere in the constructor's three-sector freedom bears "
            "trace, and the nearest trace-bearing configuration is a finite "
            "lattice step away rather than an infinitesimal detuning. But the "
            "unit grading is SUPPLIED. The lawful gradings for the landed "
            "support form a segment; only the unit point on it guarantees "
            "tracelessness for every lawful support, and only at unit weight is "
            "every sector forced to be occupied at all, since a weight-zero "
            "sector is a momentum spectator a lawful construction may simply "
            "omit. Cycle-318's coefficient-two point sits on that segment with "
            "nonzero matter recoil, its own source calls the coefficient "
            "supplied candidate-law structure, and Cycle-320 enumerates the "
            "route by name. Pushed through the re-derived Cycle-868 census, "
            "that witness turns the linear response objects sign-sensitive "
            "while the quadratic ones stay blind. So escape condition (a) does "
            "not close: it relocates. It is no longer a question about the "
            "ledger, it is a question about the sector grading, and that is "
            "where the next derivation has to bite."
        ),
    }
    result["pass"] = (
        verdict in VERDICTS
        and verdict != "PROVENANCE_UNRESOLVED"
        and isinstance(newly_sensitive, tuple)
        and result["escape_a_status"] in {"OPEN", "CLOSED_AT_SCOPE"}
    )
    return result


# --------------------------------------------------------------------------
# emission
# --------------------------------------------------------------------------
LABELS = (
    "A_PINS",
    "B_FORCING_STEP",
    "C_EXHAUSTIVE_TARGET_SWEEP",
    "D_GRADING_PROVENANCE",
    "E_TRACE_BEARING_WITNESS",
    "F_CENSUS_REDERIVED",
    "G_VERDICT",
    "H_CONTROLS",
)


def render_fixed_point(certificates: dict) -> str:
    for _attempt in range(12):
        checks = {label: bool(certificates[label]["pass"]) for label in LABELS}
        terminal = {
            "terminal": (
                "CYCLE873_TRACELESSNESS_PROVENANCE_COMPLETE"
                if all(checks.values())
                else "CYCLE873_TRACELESSNESS_PROVENANCE_INCOMPLETE"
            ),
            "checks": checks,
            "verdict": certificates["G_VERDICT"]["verdict"],
            "escape_a_status": certificates["G_VERDICT"]["escape_a_status"],
            "lawful_trace_bearing_at_unit_grading":
                certificates["C_EXHAUSTIVE_TARGET_SWEEP"][
                    "lawful_trace_bearing_count"],
            "sign_sensitive_objects_under_the_witness":
                certificates["G_VERDICT"][
                    "sign_sensitive_objects_under_the_witness"],
            "science_payload_sha256":
                certificates["H_CONTROLS"]["science_payload_sha256"],
            "runtime_seconds": certificates["H_CONTROLS"]["runtime_seconds"],
            "stdout_bytes": certificates["H_CONTROLS"]["stdout_bytes"],
        }
        lines = []
        for label in LABELS:
            lines.append(f"FINDING {label} :: {certificates[label]['finding']}")
            lines.append(
                f"{'PASS' if checks[label] else 'FAIL'} {label} :: "
                f"{compact(certificates[label])}"
            )
        lines.append("FINAL " + compact(terminal))
        output = "\n".join(lines) + "\n"
        size = len(output.encode("utf-8"))
        controls = certificates["H_CONTROLS"]
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
    forcing = forcing_certificate()
    exhaustive = exhaustive_certificate()
    grading = grading_certificate()
    witness = witness_certificate()
    members = enumerate_family()
    census, censuses = census_certificate(members)
    verdict = verdict_certificate(forcing, exhaustive, grading, witness, census)

    replay_forcing = forcing_certificate()
    replay_exhaustive = exhaustive_certificate()
    replay_census = {
        name: run_census(members, ledger)["stream_sha256"]
        for name, ledger, _shape in LEDGERS
    }
    deterministic = (
        digest(replay_forcing) == digest(forcing)
        and digest(replay_exhaustive) == digest(exhaustive)
        and all(
            replay_census[name] == censuses[name]["stream_sha256"]
            for name in replay_census
        )
    )

    receipt = {
        "cycle": 873,
        "AUDIT_INPUT_PATHS": list(AUDIT_INPUT_PATHS),
        "expected_sha256": EXPECTED_SHA256,
        "expected_git_blobs": EXPECTED_GIT_BLOBS,
        "verdict": verdict["verdict"],
        "escape_a_status": verdict["escape_a_status"],
        "provenance_map": verdict["provenance_map"],
        "landed_ledger_coefficients": list(forcing["landed_ledger_coefficients"]),
        "witness_ledger_coefficients": list(witness["witness_ledger_coefficients"]),
        "witness_ledger_sector_sum": witness["witness_ledger_sector_sum"],
        "lawful_triples_at_unit_grading": exhaustive["lawful_count"],
        "lawful_trace_bearing_at_unit_grading":
            exhaustive["lawful_trace_bearing_count"],
        "minimum_nonzero_trace_L1_norm":
            exhaustive["minimum_nonzero_trace_L1_norm"],
        "landed_support_lawful_grading_locus":
            list(grading["landed_support_lawful_grading_locus"]),
        "census_stream_sha256": {
            name: censuses[name]["stream_sha256"] for name in censuses
        },
        "objects_newly_sensitive_under_the_witness":
            list(census["objects_newly_sensitive_under_the_witness"]),
        "objects_still_blind_under_the_witness":
            list(census["objects_still_blind_under_the_witness"]),
        "sensitive_witnesses": {
            row["ledger"]: row["witnesses"] for row in census["ledger_rows"]
        },
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
                "the forcing certificate, the exhaustive target sweep and both "
                "full census streams were recomputed from scratch and compared "
                "digest for digest"
            ),
            "exact": deterministic,
            "census_streams": {
                name: censuses[name]["stream_sha256"] for name in censuses
            },
            "replay_census_streams": replay_census,
        },
        "cache_path": str(CACHE.relative_to(ROOT)),
        "cache_sha256": cache_digest,
        "science_payload_sha256": "",
        "science_payload_note": (
            "sha256 over every certificate with the wall-clock and byte-count "
            "fields stripped, so cross-process determinism is asserted on the "
            "certified content and not on machine timing"
        ),
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
            "All four cited primaries matched their pinned SHA-256 and git "
            "blob hashes, carried their required AST markers, contained every "
            "required verbatim quotation character for character, and stayed "
            "text/AST-only behind the import firewall; no primary was loaded "
            "at any point, and the direction table and reversal permutation "
            "used throughout were recovered from the pinned text by AST rather "
            "than transcribed. The forcing certificate, the exhaustive sweep "
            "and both census streams were recomputed from scratch and "
            "reproduced digest for digest, and the runtime and stdout caps "
            "were respected."
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
        "A_PINS": {**sources, "finding": controls["finding"], "pass": sources["sources_pass"]},
        "B_FORCING_STEP": forcing,
        "C_EXHAUSTIVE_TARGET_SWEEP": exhaustive,
        "D_GRADING_PROVENANCE": grading,
        "E_TRACE_BEARING_WITNESS": witness,
        "F_CENSUS_REDERIVED": census,
        "G_VERDICT": verdict,
        "H_CONTROLS": controls,
    }
    controls["science_payload_sha256"] = science_payload(certificates)
    sys.stdout.write(render_fixed_point(certificates))
    return 0 if all(row["pass"] for row in certificates.values()) else 1


if __name__ == "__main__":
    raise SystemExit(run())
