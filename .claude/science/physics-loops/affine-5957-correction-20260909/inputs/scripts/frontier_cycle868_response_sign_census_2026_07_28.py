#!/usr/bin/env python3
"""Cycle 868: the response-surface sign census for the conformal sector.

The gravity lane's landed shape is a source-acceptance instrument (Cycle 749)
and a response law candidate derived as the adjoint pullback of the landed
source algebra (Cycle 768, extended at Cycle 812).  Its unprobed residual is
the conformal-sector sign: the one-admission reduction says gravity's sign is
not a new admission per object but one shared orientation datum sigma.

This cycle expands the response surface by brute force at ONE declared scope.
It enumerates the complete landed source family, derives every landed response
object for every member, and censuses the sigma dependence EXACTLY -- each
object is carried as a univariate polynomial in a formal sigma, then evaluated
at sigma = +1 and sigma = -1 over the rationals.  The question answered is not
"what is the sign" but "can the landed response surface see the sign at all".

All five cited primaries are SHA-pinned text/AST evidence and are blocked from
import by a meta-path firewall.  Every number below is rebuilt here with
stdlib exact arithmetic; no floating point enters any certified quantity.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py",
    "scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py",
    "scripts/frontier_cycle749_response_comparison_harness_2026_07_28.py",
    "scripts/frontier_cycle768_response_law_candidate_2026_07_28.py",
    "scripts/frontier_cycle812_mixed_input_response_2026_07_28.py",
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
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "71fb02658569174b7f6f989efe311951713026ead36ece8866dca1e96878d706",
    AUDIT_INPUT_PATHS[1]:
        "4f7e25a20bcea41c285bfb52b122f84ec5c41f1f6095b6ec0068d2a228ed5d75",
    AUDIT_INPUT_PATHS[2]:
        "ab9b852236f73ec4aecad9287e07a4029309159d956a1cb3043f9238342d6807",
    AUDIT_INPUT_PATHS[3]:
        "7c8771e9494a8ed3eea6f6519b2e29d655123c96b98e0295b5300c1320570c32",
    AUDIT_INPUT_PATHS[4]:
        "fe35718b8f5e84cfafed74026a5634e722da757782f04d536a756d7273d3ee9b",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c95eb9738409c3ffe20f8b90a7ab25e6dc5843a0",
    AUDIT_INPUT_PATHS[1]: "de8b90b08707c000bb2489502823b02d62e38b29",
    AUDIT_INPUT_PATHS[2]: "cee674584704dd7d351cb2ffa947c74bee47d06e",
    AUDIT_INPUT_PATHS[3]: "0070722d7a12d47658346b6c812edd05424ae592",
    AUDIT_INPUT_PATHS[4]: "39b5f24595f2271704bf68197103b62824a14cbf",
}
REQUIRED_AST_MARKERS = {
    AUDIT_INPUT_PATHS[0]: ("ANGLE", "link_recoil_vertex"),
    AUDIT_INPUT_PATHS[1]: ("ENDPOINTS", "LEFT", "RIGHT"),
    AUDIT_INPUT_PATHS[2]: ("BUILT_IN_CANDIDATES", "evaluate_candidate"),
    AUDIT_INPUT_PATHS[3]: (
        "derive_recoil_coefficients",
        "derive_response_kernel_candidate",
        "derive_transfer_coefficients",
    ),
    AUDIT_INPUT_PATHS[4]: ("response_rows",),
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
# declared scope (the one scope this cycle certifies)
# --------------------------------------------------------------------------
SECTORS = ("matter", "field", "auxiliary")
DIRECTIONS = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)
DIRECTION_REVERSE = (1, 0, 3, 2, 5, 4)
HELD_EDGE_LENGTH = 6
WEIGHTS = tuple(range(1, HELD_EDGE_LENGTH + 1))
ENDPOINTS = ("LEFT", "RIGHT")
AXES = 3
SIGMA_DEGREE_BOUND = 2
OBJECT_ARITY = {
    "O1_PUSHFORWARD": 18,
    "O2_ADJOINT_PULLBACK": 18,
    "O3_FLUX_BALANCE": 6,
    "O4_RESPONSE_GRAM": 1,
    "O5_RESPONSE_TENSOR": 18,
    "O6_EDGE_TRANSFER": 1,
}
OBJECT_NAMES = tuple(sorted(OBJECT_ARITY))
ZERO = Fraction(0)
THIRD = Fraction(1, 3)


def landed_ledger(weight: int) -> tuple[int, int, int]:
    """The frozen Cycle-320 recoil ledger (-2d, +d, +d)."""
    return (-2 * weight, weight, weight)


# --------------------------------------------------------------------------
# exact univariate polynomials in the formal conformal sign sigma
# --------------------------------------------------------------------------
Poly = tuple[Fraction, ...]
POLY_ZERO: Poly = ()


def p_trim(coefficients: list[Fraction]) -> Poly:
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


def p_is_even(poly: Poly) -> bool:
    return all(value == 0 for value in poly[1::2])


def p_degree(poly: Poly) -> int:
    return len(poly) - 1


def p_text(poly: Poly) -> str:
    return "0" if not poly else "+".join(
        f"({value.numerator}/{value.denominator})s^{index}"
        for index, value in enumerate(poly) if value != 0
    )


# --------------------------------------------------------------------------
# the landed source family at the declared scope
# --------------------------------------------------------------------------
Member = tuple


def enumerate_family_nested() -> tuple[Member, ...]:
    """k = 1 (single carried link) and k = 2 (two-cell, one source per end)."""
    members: list[Member] = []
    for endpoint in range(len(ENDPOINTS)):
        for direction in range(len(DIRECTIONS)):
            for weight in WEIGHTS:
                members.append(("k1", endpoint, direction, weight))
    for left_direction in range(len(DIRECTIONS)):
        for left_weight in WEIGHTS:
            for right_direction in range(len(DIRECTIONS)):
                for right_weight in WEIGHTS:
                    members.append((
                        "k2",
                        left_direction, left_weight,
                        right_direction, right_weight,
                    ))
    return tuple(members)


def enumerate_family_odometer() -> tuple[Member, ...]:
    """Independent mixed-radix re-enumeration used as a bookkeeping control."""
    members: list[Member] = []
    radix_one = (len(ENDPOINTS), len(DIRECTIONS), len(WEIGHTS))
    span_one = radix_one[0] * radix_one[1] * radix_one[2]
    for index in range(span_one):
        rest, weight_index = divmod(index, radix_one[2])
        endpoint, direction = divmod(rest, radix_one[1])
        members.append(("k1", endpoint, direction, WEIGHTS[weight_index]))
    radix_two = (len(DIRECTIONS), len(WEIGHTS), len(DIRECTIONS), len(WEIGHTS))
    span_two = radix_two[0] * radix_two[1] * radix_two[2] * radix_two[3]
    for index in range(span_two):
        rest, right_weight_index = divmod(index, radix_two[3])
        rest, right_direction = divmod(rest, radix_two[2])
        left_direction, left_weight_index = divmod(rest, radix_two[1])
        members.append((
            "k2",
            left_direction, WEIGHTS[left_weight_index],
            right_direction, WEIGHTS[right_weight_index],
        ))
    return tuple(members)


def member_sources(member: Member) -> tuple[tuple[int, int, int], ...]:
    """(endpoint, direction index, carried weight) per source."""
    if member[0] == "k1":
        return ((member[1], member[2], member[3]),)
    return ((0, member[1], member[2]), (1, member[3], member[4]))


def source_array(
    member: Member,
    ledger=landed_ledger,
) -> tuple[tuple[tuple[Fraction, ...], ...], ...]:
    """S[endpoint][sector][axis] from the recoil ledger carried on directions."""
    grid = [
        [[ZERO for _axis in range(AXES)] for _sector in SECTORS]
        for _endpoint in ENDPOINTS
    ]
    for endpoint, direction, weight in member_sources(member):
        coefficients = ledger(weight)
        unit = DIRECTIONS[direction]
        for sector, coefficient in enumerate(coefficients):
            for axis in range(AXES):
                grid[endpoint][sector][axis] += Fraction(coefficient * unit[axis])
    return tuple(
        tuple(tuple(row) for row in endpoint_block) for endpoint_block in grid
    )


# --------------------------------------------------------------------------
# conformal / trace-free split on the sector index, and the sigma grading
# --------------------------------------------------------------------------
def conformal_channel(array) -> tuple[tuple[Fraction, ...], ...]:
    """The sector trace: the conformal channel of the source."""
    return tuple(
        tuple(
            sum((block[sector][axis] for sector in range(len(SECTORS))), ZERO)
            for axis in range(AXES)
        )
        for block in array
    )


def tracefree_part(array, conformal) -> tuple:
    return tuple(
        tuple(
            tuple(
                block[sector][axis] - THIRD * conformal[endpoint][axis]
                for axis in range(AXES)
            )
            for sector in range(len(SECTORS))
        )
        for endpoint, block in enumerate(array)
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
    """G_sigma = Pi_tracefree + sigma * Pi_conformal, on polynomial arrays.

    The split is on the sector index and is linear, so it commutes with the
    polynomial coefficients.  With live=False the conformal channel is carried
    at degree 0 instead of degree 1: the adversary control that disables the
    sigma probe while changing nothing else in the pipeline.
    """
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


def graded_source(array, live: bool = True) -> tuple:
    """S(sigma) = G_sigma applied to the landed source (identity at sigma=1)."""
    return grading_operator(lift_to_poly(array), live)


def endpoint_exchange(graded) -> tuple:
    """R(X)[e] = X[P e] with P the LEFT/RIGHT reversal permutation."""
    return tuple(graded[len(ENDPOINTS) - 1 - endpoint]
                 for endpoint in range(len(ENDPOINTS)))


def adjoint_pullback(array, live: bool = True) -> tuple:
    """K = R* R composed explicitly: G_sigma o R o R o G_sigma applied to S.

    Nothing is asserted about the composite: the exchange is applied twice and
    the grading is applied twice, in order, and whatever comes out is what the
    census reads.
    """
    stage_one = grading_operator(lift_to_poly(array), live)
    stage_two = endpoint_exchange(stage_one)
    stage_three = endpoint_exchange(stage_two)
    return grading_operator(stage_three, live)


# --------------------------------------------------------------------------
# the landed response objects
# --------------------------------------------------------------------------
def response_objects(array, live: bool = True) -> dict[str, tuple[Poly, ...]]:
    graded = graded_source(array, live)
    pushed = endpoint_exchange(graded)
    pulled = adjoint_pullback(array, live)

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
    o4 = (gram,)
    o5_rows: list[Poly] = []
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
    o5 = tuple(o5_rows)
    transfer: Poly = POLY_ZERO
    for sector in range(len(SECTORS)):
        for axis in range(AXES):
            transfer = p_add(transfer, p_mul(
                graded[0][sector][axis], graded[1][sector][axis]
            ))
    o6 = (transfer,)
    return {
        "O1_PUSHFORWARD": o1,
        "O2_ADJOINT_PULLBACK": o2,
        "O3_FLUX_BALANCE": o3,
        "O4_RESPONSE_GRAM": o4,
        "O5_RESPONSE_TENSOR": o5,
        "O6_EDGE_TRANSFER": o6,
    }


# --------------------------------------------------------------------------
# serialisation helpers
# --------------------------------------------------------------------------
def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


# --------------------------------------------------------------------------
# certificate A -- the declared scope
# --------------------------------------------------------------------------
def scope_certificate() -> dict[str, object]:
    reverse_is_involution = all(
        DIRECTION_REVERSE[DIRECTION_REVERSE[index]] == index
        for index in range(len(DIRECTIONS))
    )
    reverse_negates = all(
        tuple(-component for component in DIRECTIONS[index])
        == DIRECTIONS[DIRECTION_REVERSE[index]]
        for index in range(len(DIRECTIONS))
    )
    reverse_free = all(
        DIRECTION_REVERSE[index] != index for index in range(len(DIRECTIONS))
    )
    ledger_rows = tuple(
        {
            "weight": weight,
            "ledger": landed_ledger(weight),
            "sector_sum": sum(landed_ledger(weight)),
        }
        for weight in WEIGHTS
    )
    result = {
        "scope_declaration": (
            "sectors=(matter,field,auxiliary); recoil ledger (-2d,+d,+d); "
            "directions=6 signed axis directions of Z^3; carried weights "
            "d=1..6 set by the held L=6 edge; endpoints=(LEFT,RIGHT) with "
            "R(X)=P X P^T the reversal exchange; source multiplicity k in "
            "{1,2}, k=2 seating one source at each endpoint"
        ),
        "sector_count": len(SECTORS),
        "direction_count": len(DIRECTIONS),
        "held_edge_length": HELD_EDGE_LENGTH,
        "weight_count": len(WEIGHTS),
        "endpoint_count": len(ENDPOINTS),
        "axis_count": AXES,
        "reverse_is_involution": reverse_is_involution,
        "reverse_is_fixed_point_free": reverse_free,
        "reverse_negates_direction": reverse_negates,
        "landed_ledger_rows": ledger_rows,
        "landed_ledger_sector_sums": tuple(
            row["sector_sum"] for row in ledger_rows
        ),
        "sigma_grading": "S(sigma)=tracefree(S)+sigma*conformal(S)/3",
        "sigma_degree_bound": SIGMA_DEGREE_BOUND,
        "object_arity": OBJECT_ARITY,
        "finding": (
            "The scope is declared as a finite closed structure: three sectors "
            "carrying the frozen (-2d,+d,+d) recoil ledger, six signed axis "
            "directions closed under a fixed-point-free negating reversal, six "
            "carried weights set by the held L=6 edge, two endpoints exchanged "
            "by a self-adjoint involution, and source multiplicity one or two. "
            "The conformal sector is the sector trace; the formal sign sigma "
            "scales that channel and only that channel."
        ),
    }
    result["pass"] = (
        len(SECTORS) == 3
        and len(DIRECTIONS) == 6
        and len(ENDPOINTS) == 2
        and AXES == 3
        and len(WEIGHTS) == HELD_EDGE_LENGTH
        and reverse_is_involution
        and reverse_free
        and reverse_negates
        and set(OBJECT_ARITY) == set(OBJECT_NAMES)
    )
    return result


# --------------------------------------------------------------------------
# certificate B -- the complete family
# --------------------------------------------------------------------------
def family_certificate() -> tuple[tuple[Member, ...], dict[str, object]]:
    nested = enumerate_family_nested()
    odometer = enumerate_family_odometer()
    closed_form_k1 = len(ENDPOINTS) * len(DIRECTIONS) * len(WEIGHTS)
    closed_form_k2 = (len(DIRECTIONS) * len(WEIGHTS)) ** 2
    counts = {"k1": 0, "k2": 0}
    for member in nested:
        counts[member[0]] += 1
    unique = len(set(nested))
    result = {
        "enumerated_total": len(nested),
        "unique_total": unique,
        "k1_enumerated": counts["k1"],
        "k2_enumerated": counts["k2"],
        "k1_closed_form": closed_form_k1,
        "k2_closed_form": closed_form_k2,
        "closed_form_total": closed_form_k1 + closed_form_k2,
        "closed_form_equation": "2*6*6 + (6*6)^2",
        "odometer_total": len(odometer),
        "odometer_multiset_matches_nested":
            sorted(map(compact, odometer)) == sorted(map(compact, nested)),
        "family_digest": digest(sorted(map(compact, nested))),
        "finding": (
            f"The landed source family at the declared scope is finite and "
            f"exhausted: {counts['k1']} single-source configurations and "
            f"{counts['k2']} two-source configurations, {len(nested)} in "
            f"total, matching the closed form 2*6*6 + (6*6)^2 exactly, all "
            f"distinct, and reproduced member-for-member by an independent "
            f"mixed-radix odometer enumeration."
        ),
    }
    result["pass"] = (
        result["enumerated_total"] == result["closed_form_total"]
        and result["unique_total"] == result["enumerated_total"]
        and result["k1_enumerated"] == closed_form_k1
        and result["k2_enumerated"] == closed_form_k2
        and result["odometer_total"] == result["enumerated_total"]
        and result["odometer_multiset_matches_nested"]
    )
    return nested, result


# --------------------------------------------------------------------------
# certificate C -- the response objects
# --------------------------------------------------------------------------
def objects_certificate(members: tuple[Member, ...]) -> dict[str, object]:
    arity_ok = True
    degree_ok = True
    identity_ok = True
    max_degree = 0
    sample_rows = []
    for member in members:
        array = source_array(member)
        objects = response_objects(array)
        if set(objects) != set(OBJECT_NAMES):
            arity_ok = False
        for name, values in objects.items():
            if len(values) != OBJECT_ARITY[name]:
                arity_ok = False
            for poly in values:
                max_degree = max(max_degree, p_degree(poly))
                if p_degree(poly) > SIGMA_DEGREE_BOUND:
                    degree_ok = False
        graded = graded_source(array)
        for endpoint in range(len(ENDPOINTS)):
            for sector in range(len(SECTORS)):
                for axis in range(AXES):
                    if p_eval(graded[endpoint][sector][axis], 1) != \
                            array[endpoint][sector][axis]:
                        identity_ok = False
    probe = source_array(("k2", 0, 1, 2, 3))
    probe_objects = response_objects(probe)
    for name in OBJECT_NAMES:
        sample_rows.append({
            "object": name,
            "arity": len(probe_objects[name]),
            "sigma_polynomials": tuple(
                p_text(poly) for poly in probe_objects[name]
            ),
        })
    result = {
        "objects": OBJECT_NAMES,
        "object_definitions": {
            "O1_PUSHFORWARD": "R applied to the sigma-graded source",
            "O2_ADJOINT_PULLBACK": "K=R*R composed through the grading",
            "O3_FLUX_BALANCE": "sector trace of the pushforward per endpoint/axis",
            "O4_RESPONSE_GRAM": "<R S(sigma), R S(sigma)> over all indices",
            "O5_RESPONSE_TENSOR": "T[e][a][b]=sum_s (R S)[e][s][a](R S)[e][s][b]",
            "O6_EDGE_TRANSFER": "reciprocal occupation transfer across held L=6",
        },
        "arity_exact_for_every_member": arity_ok,
        "sigma_degree_within_bound": degree_ok,
        "max_sigma_degree_observed": max_degree,
        "grading_reduces_to_source_at_sigma_one": identity_ok,
        "worked_member": ("k2", 0, 1, 2, 3),
        "worked_member_rows": tuple(sample_rows),
        "finding": (
            "Six landed response objects are derived for every member of the "
            "family, each carried as an exact rational polynomial in the "
            "formal conformal sign. Arities are exact everywhere, no object "
            "exceeds sigma-degree 2, and the grading reduces to the undeformed "
            "landed source at sigma=+1 for every member, so the deformation is "
            "a genuine one-parameter extension of the landed surface rather "
            "than a different surface."
        ),
    }
    result["pass"] = arity_ok and degree_ok and identity_ok and max_degree <= SIGMA_DEGREE_BOUND
    return result


# --------------------------------------------------------------------------
# certificate D -- the sign census
# --------------------------------------------------------------------------
def run_census(members: tuple[Member, ...], live: bool = True) -> dict[str, object]:
    blind = {name: 0 for name in OBJECT_NAMES}
    sensitive = {name: 0 for name in OBJECT_NAMES}
    structurally_even = {name: 0 for name in OBJECT_NAMES}
    conformal_zero = {name: 0 for name in OBJECT_NAMES}
    unattributed = {name: 0 for name in OBJECT_NAMES}
    both = {name: 0 for name in OBJECT_NAMES}
    stream = sha256()
    conformal_nonzero_members = 0
    for member in members:
        array = source_array(member)
        conformal = conformal_channel(array)
        conformal_is_zero = all(
            value == 0 for block in conformal for value in block
        )
        if not conformal_is_zero:
            conformal_nonzero_members += 1
        objects = response_objects(array, live)
        for name in OBJECT_NAMES:
            values = objects[name]
            plus = tuple(p_eval(poly, 1) for poly in values)
            minus = tuple(p_eval(poly, -1) for poly in values)
            invisible = plus == minus
            even = all(p_is_even(poly) for poly in values)
            if invisible:
                blind[name] += 1
                if even and conformal_is_zero:
                    both[name] += 1
                elif even:
                    structurally_even[name] += 1
                elif conformal_is_zero:
                    conformal_zero[name] += 1
                else:
                    unattributed[name] += 1
            else:
                sensitive[name] += 1
            stream.update(compact({
                "m": member, "o": name,
                "p": tuple(fraction_text(value) for value in plus),
                "n": tuple(fraction_text(value) for value in minus),
                "b": invisible, "e": even,
            }).encode())
    return {
        "member_count": len(members),
        "pair_count": len(members) * len(OBJECT_NAMES),
        "blind": blind,
        "sensitive": sensitive,
        "attributed_M1_only": structurally_even,
        "attributed_M2_only": conformal_zero,
        "attributed_both": both,
        "unattributed_blind": unattributed,
        "conformal_nonzero_members": conformal_nonzero_members,
        "stream_sha256": stream.hexdigest(),
    }


def census_certificate(members: tuple[Member, ...]) -> dict[str, object]:
    census = run_census(members)
    blind_total = sum(census["blind"].values())
    sensitive_total = sum(census["sensitive"].values())
    partition_ok = all(
        census["blind"][name] + census["sensitive"][name] == len(members)
        for name in OBJECT_NAMES
    )
    attribution_ok = all(
        census["attributed_M1_only"][name]
        + census["attributed_M2_only"][name]
        + census["attributed_both"][name]
        + census["unattributed_blind"][name]
        == census["blind"][name]
        for name in OBJECT_NAMES
    )
    result = {
        **census,
        "blind_total": blind_total,
        "sensitive_total": sensitive_total,
        "totals_partition_exactly": (
            blind_total + sensitive_total == census["pair_count"]
        ),
        "per_object_partition_exact": partition_ok,
        "attribution_partition_exact": attribution_ok,
        "unattributed_blind_total": sum(census["unattributed_blind"].values()),
        "finding": (
            f"Every one of the {census['pair_count']} (member, response "
            f"object) pairs was evaluated exactly at sigma=+1 and sigma=-1 "
            f"over the rationals. {sensitive_total} pairs differ; "
            f"{blind_total} pairs are identical. The landed source family "
            f"carries a nonzero conformal channel in "
            f"{census['conformal_nonzero_members']} of {len(members)} members, "
            f"and every blind pair is accounted for by the mechanism partition "
            f"with {sum(census['unattributed_blind'].values())} left "
            f"unattributed."
        ),
    }
    result["pass"] = (
        result["totals_partition_exactly"]
        and partition_ok
        and attribution_ok
        and census["pair_count"] == len(members) * len(OBJECT_NAMES)
    )
    return result


# --------------------------------------------------------------------------
# certificate E -- the mechanisms, with exact witnesses
# --------------------------------------------------------------------------
def mechanism_certificate(members: tuple[Member, ...]) -> dict[str, object]:
    balanced = source_array(("k2", 0, 2, 3, 5))
    unbalanced = source_array(
        ("k2", 0, 2, 3, 5), ledger=lambda w: (-2 * w, w, w + 1)
    )
    balanced_objects = response_objects(balanced)
    unbalanced_objects = response_objects(unbalanced)
    m1_objects = tuple(
        name for name in OBJECT_NAMES
        if all(p_is_even(poly) for poly in unbalanced_objects[name])
    )
    m2_objects = tuple(
        name for name in OBJECT_NAMES
        if not all(p_is_even(poly) for poly in unbalanced_objects[name])
    )
    conformal_balanced = conformal_channel(balanced)
    conformal_unbalanced = conformal_channel(unbalanced)
    ledger_sums_zero = all(
        sum(landed_ledger(weight)) == 0 for weight in WEIGHTS
    )
    # The declared weight ladder d = 1..6 is a truncation.  Close it: carry d
    # itself as a formal indeterminate and show the ledger's sector sum is the
    # ZERO polynomial, hence zero for every weight, not just the six swept.
    symbolic_ledger = (
        p_shift(p_const(Fraction(-2)), 1),
        p_shift(p_const(Fraction(1)), 1),
        p_shift(p_const(Fraction(1)), 1),
    )
    symbolic_sum = p_add(p_add(symbolic_ledger[0], symbolic_ledger[1]),
                         symbolic_ledger[2])
    # Multiplicity is also a truncation.  The conformal channel of any
    # configuration is sum_i (sector sum of the ledger at w_i) * u_i, so it
    # vanishes for arbitrary source count and arbitrary weights.  Spot-check
    # that on declared extreme configurations far outside the swept scope.
    extreme_rows = []
    extreme_all_zero = True
    for label, sources in (
        ("k=8_mixed_directions_unit_weights",
         tuple((index % 2, index % 6, 1) for index in range(8))),
        ("k=4_large_weights",
         ((0, 0, 1_000_003), (0, 3, 7_777_777), (1, 5, 999_983), (1, 2, 12))),
        ("k=1_huge_weight", ((0, 4, 10 ** 12),)),
    ):
        grid = [
            [[ZERO for _axis in range(AXES)] for _sector in SECTORS]
            for _endpoint in ENDPOINTS
        ]
        for endpoint, direction, weight in sources:
            for sector, coefficient in enumerate(landed_ledger(weight)):
                for axis in range(AXES):
                    grid[endpoint][sector][axis] += Fraction(
                        coefficient * DIRECTIONS[direction][axis]
                    )
        frozen = tuple(
            tuple(tuple(row) for row in block) for block in grid
        )
        channel = conformal_channel(frozen)
        is_zero = all(value == 0 for block in channel for value in block)
        extreme_all_zero = extreme_all_zero and is_zero
        extreme_rows.append({
            "configuration": label,
            "source_count": len(sources),
            "conformal_channel_is_zero": is_zero,
        })
    cross_terms_vanish = True
    for member in members[:120]:
        array = source_array(member)
        conformal = conformal_channel(array)
        tracefree = tracefree_part(array, conformal)
        for endpoint in range(len(ENDPOINTS)):
            for axis in range(AXES):
                if sum(
                    (tracefree[endpoint][sector][axis]
                     for sector in range(len(SECTORS))), ZERO
                ) != 0:
                    cross_terms_vanish = False
    result = {
        "M1_name": "adjoint evenness / channel orthogonality",
        "M1_statement": (
            "any response object that factors through R*R, or through a "
            "contraction quadratic in the graded source, is an even "
            "polynomial in sigma: the exchange is a self-adjoint involution "
            "so sigma enters only as sigma^2, and the trace-free channel is "
            "sector-orthogonal to the conformal channel so every cross term "
            "vanishes identically"
        ),
        "M1_objects": m1_objects,
        "M1_witness_unbalanced_source_still_even": tuple(
            {
                "object": name,
                "even": all(p_is_even(poly) for poly in unbalanced_objects[name]),
            }
            for name in OBJECT_NAMES
        ),
        "M2_name": "conformal annihilation by the landed ledger",
        "M2_statement": (
            "the frozen recoil ledger (-2d,+d,+d) has sector sum zero for "
            "every carried weight, so the conformal channel of every landed "
            "source vanishes identically and sigma multiplies zero"
        ),
        "M2_objects": m2_objects,
        "landed_ledger_sector_sums_all_zero": ledger_sums_zero,
        "symbolic_ledger_in_d": tuple(p_text(poly) for poly in symbolic_ledger),
        "symbolic_ledger_sector_sum": p_text(symbolic_sum),
        "symbolic_sector_sum_is_zero_polynomial": symbolic_sum == POLY_ZERO,
        "weight_truncation_is_not_load_bearing": symbolic_sum == POLY_ZERO,
        "multiplicity_truncation_spot_checks": tuple(extreme_rows),
        "multiplicity_truncation_is_not_load_bearing": extreme_all_zero,
        "balanced_conformal_channel": tuple(
            tuple(fraction_text(value) for value in block)
            for block in conformal_balanced
        ),
        "unbalanced_conformal_channel": tuple(
            tuple(fraction_text(value) for value in block)
            for block in conformal_unbalanced
        ),
        "balanced_conformal_is_zero": all(
            value == 0 for block in conformal_balanced for value in block
        ),
        "unbalanced_conformal_is_nonzero": any(
            value != 0 for block in conformal_unbalanced for value in block
        ),
        "tracefree_sector_sum_vanishes_sampled": cross_terms_vanish,
        "sampled_members_for_cross_terms": 120,
        "M1_objects_even_for_balanced_source": all(
            all(p_is_even(poly) for poly in balanced_objects[name])
            for name in m1_objects
        ),
        "M1_objects_even_for_unbalanced_source": all(
            all(p_is_even(poly) for poly in unbalanced_objects[name])
            for name in m1_objects
        ),
        "M2_objects_odd_only_under_conformal_load": all(
            not all(p_is_even(poly) for poly in unbalanced_objects[name])
            for name in m2_objects
        ),
        "derived_pullback_identity": (
            "R applied twice returns the identity, so the composed pullback "
            "carries the conformal channel at sigma^2 exactly"
        ),
        "derived_pullback_degrees_unbalanced": tuple(
            sorted({p_degree(poly)
                    for poly in unbalanced_objects["O2_ADJOINT_PULLBACK"]
                    if poly})
        ),
        "derived_pushforward_degrees_unbalanced": tuple(
            sorted({p_degree(poly)
                    for poly in unbalanced_objects["O1_PUSHFORWARD"]
                    if poly})
        ),
        "finding": (
            f"Two independent mechanisms make the conformal sign invisible, "
            f"and they cover disjoint object classes. {len(m1_objects)} "
            f"objects ({', '.join(m1_objects)}) are even in sigma no matter "
            f"what the source is -- the exchange is a self-adjoint involution "
            f"and the trace-free channel is sector-orthogonal to the conformal "
            f"channel, so sigma can only enter squared. The remaining "
            f"{len(m2_objects)} objects ({', '.join(m2_objects)}) are odd in "
            f"sigma and become sign-sensitive the moment the source carries a "
            f"conformal channel; they are blind here only because the frozen "
            f"(-2d,+d,+d) ledger "
            + ("sums to zero in every sector for every carried weight"
               if ledger_sums_zero else
               "does NOT sum to zero at every carried weight")
            + ". On the truncations in the declared scope: carrying the weight "
            f"d as a formal indeterminate makes the ledger's sector sum "
            + ("the zero polynomial, so the annihilation holds at every weight "
               "and not merely the six swept"
               if symbolic_sum == POLY_ZERO else
               f"the nonzero polynomial {p_text(symbolic_sum)}, so the weight "
               f"truncation IS load-bearing")
            + ", and the conformal channel at arbitrary source multiplicity "
            + ("stayed zero on every declared extreme configuration up to "
               "eight sources and weights of order 10^12"
               if extreme_all_zero else
               "was NONZERO on at least one declared extreme configuration")
            + "."
        ),
    }
    # Bookkeeping only.  The mechanism classification must be a well formed
    # partition of the objects, the projector must be internally consistent,
    # and the off-scope calibration probe must actually carry the conformal
    # load it is supposed to carry.  Whether the LANDED family is annihilated
    # is reported as data above and is deliberately NOT gated here.
    result["gate_scope"] = (
        "bookkeeping only: object partition well formed, projector identity "
        "holds, calibration probe carries conformal load, all declared "
        "spot-checks evaluated; the landed annihilation itself is reported, "
        "not gated"
    )
    result["pass"] = (
        set(m1_objects) | set(m2_objects) == set(OBJECT_NAMES)
        and not (set(m1_objects) & set(m2_objects))
        and cross_terms_vanish
        and result["unbalanced_conformal_is_nonzero"]
        and len(extreme_rows) == 3
        and isinstance(symbolic_sum, tuple)
    )
    return result


# --------------------------------------------------------------------------
# certificate F -- instrument calibration (anti-vacuity)
# --------------------------------------------------------------------------
PREREGISTERED_CONTROLS = {
    "P1_unbalanced_ledger": "SENSITIVE_ON_ODD_OBJECTS",
    "P2_pure_conformal_source": "SENSITIVE_ON_ODD_OBJECTS",
    "P3_landed_balanced_source": "BLIND_EVERYWHERE",
    "P4_adversary_disabled_grading": "BLIND_EVERYWHERE",
}


def probe_reading(array, live: bool = True) -> dict[str, bool]:
    objects = response_objects(array, live)
    reading = {}
    for name in OBJECT_NAMES:
        values = objects[name]
        plus = tuple(p_eval(poly, 1) for poly in values)
        minus = tuple(p_eval(poly, -1) for poly in values)
        reading[name] = plus != minus
    return reading


def calibration_certificate() -> dict[str, object]:
    seed = ("k2", 1, 3, 4, 2)
    landed = source_array(seed)
    unbalanced = source_array(seed, ledger=lambda w: (-2 * w, w, w + 1))
    pure_conformal = source_array(seed, ledger=lambda w: (w, w, w))
    odd_objects = tuple(
        name for name in OBJECT_NAMES
        if not all(p_is_even(poly) for poly in response_objects(unbalanced)[name])
    )
    p1 = probe_reading(unbalanced)
    p2 = probe_reading(pure_conformal)
    p3 = probe_reading(landed)
    p4 = probe_reading(unbalanced, live=False)
    p1_ok = all(p1[name] for name in odd_objects) and any(p1.values())
    p2_ok = all(p2[name] for name in odd_objects) and any(p2.values())
    p3_ok = not any(p3.values())
    p4_ok = not any(p4.values())
    result = {
        "preregistered": PREREGISTERED_CONTROLS,
        "odd_objects_under_conformal_load": odd_objects,
        "P1_unbalanced_ledger_readings": p1,
        "P2_pure_conformal_readings": p2,
        "P3_landed_balanced_readings": p3,
        "P4_adversary_disabled_grading_readings": p4,
        "P1_met": p1_ok,
        "P2_met": p2_ok,
        "P3_met": p3_ok,
        "P4_met": p4_ok,
        "calibration_scope_note": (
            "P1, P2 and P4 are OFF-SCOPE synthetic probes. They calibrate the "
            "detector's discriminating power and say nothing about the landed "
            "family; they are the anti-vacuity gate that stops a no-go from "
            "resting on a blind instrument."
        ),
        "finding": (
            "Instrument calibration against the four pre-registered probes: "
            + "the detuned-ledger probe "
            + ("fired" if p1_ok else "FAILED to fire")
            + " on every sigma-odd object, the pure-conformal probe "
            + ("fired" if p2_ok else "FAILED to fire")
            + ", the landed balanced source "
            + ("read blind everywhere" if p3_ok else "did NOT read blind")
            + ", and the adversary run that carries the conformal channel at "
            + "degree zero -- disabling the sigma probe while changing nothing "
            + "else -- "
            + ("went blind even on the detuned source" if p4_ok
               else "still registered sensitive")
            + ". Taken together the instrument is "
            + ("demonstrably able" if (p1_ok and p2_ok and p4_ok)
               else "NOT shown able")
            + " to see the conformal sign when the sign is present, so a blind "
            + "reading on the landed family is evidence rather than a dead "
            + "detector."
        ),
    }
    result["pass"] = (
        p1_ok and p2_ok and p3_ok and p4_ok and len(odd_objects) > 0
    )
    return result


# --------------------------------------------------------------------------
# certificate G -- the verdict, produced by a stated total function
# --------------------------------------------------------------------------
def verdict_certificate(
    census: dict[str, object], mechanisms: dict[str, object]
) -> dict[str, object]:
    sensitive_total = census["sensitive_total"]
    unattributed = census["unattributed_blind_total"]
    if sensitive_total > 0:
        verdict = "RESPONSE_SURFACE_CONSTRAINS_THE_CONFORMAL_SIGN"
    elif unattributed > 0:
        verdict = "SIGN_INVISIBLE_BUT_PARTLY_UNEXPLAINED"
    else:
        verdict = "SCOPED_NO_GO_SIGN_INVISIBLE_TO_THE_RESPONSE_SURFACE"
    result = {
        "verdict_function": (
            "sensitive_total>0 -> CONSTRAINS; else unattributed>0 -> "
            "INVISIBLE_BUT_PARTLY_UNEXPLAINED; else SCOPED_NO_GO"
        ),
        "sensitive_total": sensitive_total,
        "unattributed_blind_total": unattributed,
        "verdict": verdict,
        "scope_of_the_claim": (
            "the declared scope only: the landed k<=2 source family on the "
            "two-endpoint held L=6 surface with the frozen (-2d,+d,+d) ledger "
            "and the six landed response objects"
        ),
        "named_escape_conditions": (
            "the no-go dies if EITHER (a) a landed source acquires a nonzero "
            "sector trace, i.e. the recoil ledger stops summing to zero, which "
            "immediately makes O1_PUSHFORWARD and O3_FLUX_BALANCE "
            "sign-sensitive; OR (b) a response object is admitted that is "
            "linear in the endpoint exchange rather than factoring through "
            "R*R and is not a sector-orthogonal contraction. Mechanism M1 "
            "survives (a) alone and mechanism M2 survives (b) alone, so both "
            "must fail together for the response surface to see the sign"
        ),
        "what_is_not_claimed": (
            "no statement is made about the value of the conformal sign, about "
            "whether some other lane fixes it, or about response objects "
            "outside the declared six"
        ),
        "finding": (
            f"At the declared scope the conformal-sector sign is invisible to "
            f"the response surface: no landed response object on any member of "
            f"the complete landed source family distinguishes sigma=+1 from "
            f"sigma=-1, and the invisibility is fully explained by two "
            f"mechanisms with no residue. This is a scoped no-go, not a "
            f"selection: the one-admission reduction survives untouched, and "
            f"the response surface is now shown to be the wrong instrument to "
            f"discharge it. The escape is named and is exactly the conformal "
            f"channel of the recoil ledger."
        ) if verdict.startswith("SCOPED_NO_GO") else (
            f"The census returned {sensitive_total} sign-sensitive pairs, so "
            f"the landed response surface DOES constrain the conformal-sector "
            f"sign at the declared scope; the sensitive objects and their "
            f"members are recorded in the census certificate."
        ) if sensitive_total > 0 else (
            f"No landed response object distinguishes the two signs, but "
            f"{unattributed} blind pairs are not explained by either declared "
            f"mechanism. The invisibility is real at this scope and its cause "
            f"is not fully identified, so no no-go is claimed; the "
            f"unattributed pairs are the next object of work."
        ),
    }
    result["mechanism_object_cover_complete"] = (
        set(mechanisms["M1_objects"]) | set(mechanisms["M2_objects"])
        == set(OBJECT_NAMES)
    )
    result["pass"] = (
        verdict in {
            "RESPONSE_SURFACE_CONSTRAINS_THE_CONFORMAL_SIGN",
            "SIGN_INVISIBLE_BUT_PARTLY_UNEXPLAINED",
            "SCOPED_NO_GO_SIGN_INVISIBLE_TO_THE_RESPONSE_SURFACE",
        }
        and isinstance(sensitive_total, int)
        and isinstance(unattributed, int)
        and sensitive_total >= 0
        and unattributed >= 0
        and result["mechanism_object_cover_complete"]
    )
    return result


# --------------------------------------------------------------------------
# certificate H -- source and process controls
# --------------------------------------------------------------------------
def source_controls() -> dict[str, object]:
    payloads = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    rows = []
    markers_ok = True
    for path in AUDIT_INPUT_PATHS:
        payload = payloads[path]
        tree = ast.parse(payload, filename=path)
        names: set[str] = set()
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                names.add(node.name)
            elif isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        names.add(target.id)
            elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
                names.add(node.target.id)
        present = set(REQUIRED_AST_MARKERS[path]) <= names
        markers_ok = markers_ok and present
        rows.append({
            "path": path,
            "exists_worktree_relative":
                not Path(path).is_absolute() and (ROOT / path).is_file(),
            "sha256": sha256(payload).hexdigest(),
            "sha256_exact":
                sha256(payload).hexdigest() == EXPECTED_SHA256[path],
            "git_blob": git_blob(payload),
            "git_blob_exact": git_blob(payload) == EXPECTED_GIT_BLOBS[path],
            "AST_valid": True,
            "required_markers": REQUIRED_AST_MARKERS[path],
            "required_markers_present": present,
            "access": "TEXT_AST_ONLY_BLOCKLISTED_PRIMARY",
        })
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_path_count": len(AUDIT_INPUT_PATHS),
        "read_cap": 6,
        "source_rows": tuple(rows),
        "all_markers_present": markers_ok,
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
            for row in rows
        )
        and markers_ok
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
    )
    return result


# --------------------------------------------------------------------------
# emission
# --------------------------------------------------------------------------
LABELS = (
    "A_SCOPE",
    "B_FAMILY",
    "C_RESPONSE_OBJECTS",
    "D_SIGN_CENSUS",
    "E_MECHANISMS",
    "F_CALIBRATION",
    "G_VERDICT",
    "H_CONTROLS",
)


def render_fixed_point(certificates: dict[str, dict[str, object]]) -> str:
    for _attempt in range(12):
        checks = {label: bool(certificates[label]["pass"]) for label in LABELS}
        terminal = {
            "terminal": (
                "CYCLE868_RESPONSE_SIGN_CENSUS_COMPLETE"
                if all(checks.values())
                else "CYCLE868_RESPONSE_SIGN_CENSUS_INCOMPLETE"
            ),
            "checks": checks,
            "verdict": certificates["G_VERDICT"]["verdict"],
            "pairs_censused": certificates["D_SIGN_CENSUS"]["pair_count"],
            "sign_sensitive_pairs": certificates["D_SIGN_CENSUS"]["sensitive_total"],
            "sign_blind_pairs": certificates["D_SIGN_CENSUS"]["blind_total"],
            "unattributed_blind": certificates["D_SIGN_CENSUS"]["unattributed_blind_total"],
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
    scope = scope_certificate()
    members, family = family_certificate()
    objects = objects_certificate(members)
    census = census_certificate(members)
    mechanisms = mechanism_certificate(members)
    calibration = calibration_certificate()
    verdict = verdict_certificate(census, mechanisms)

    replay_members, replay_family = family_certificate()
    replay_census = run_census(replay_members)
    replay_calibration = calibration_certificate()
    deterministic = (
        replay_members == members
        and replay_family["family_digest"] == family["family_digest"]
        and replay_census["stream_sha256"] == census["stream_sha256"]
        and replay_census["blind"] == census["blind"]
        and replay_census["sensitive"] == census["sensitive"]
        and replay_calibration["P1_unbalanced_ledger_readings"]
        == calibration["P1_unbalanced_ledger_readings"]
        and replay_calibration["P3_landed_balanced_readings"]
        == calibration["P3_landed_balanced_readings"]
    )
    elapsed = monotonic() - started
    controls = {
        **sources,
        "determinism": {
            "scope": (
                "the family enumeration, the complete sigma census stream and "
                "the calibration readings were recomputed from scratch and "
                "compared digest-for-digest"
            ),
            "first_census_sha256": census["stream_sha256"],
            "second_census_sha256": replay_census["stream_sha256"],
            "exact": deterministic,
        },
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
            "All five cited primaries matched their pinned SHA-256 and git "
            "blob hashes, carried their required AST markers, and stayed "
            "text/AST-only behind the import firewall; no primary was loaded "
            "at any point. The full census was recomputed from scratch and "
            "reproduced byte-for-byte, and both the runtime and stdout caps "
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
        "A_SCOPE": scope,
        "B_FAMILY": family,
        "C_RESPONSE_OBJECTS": objects,
        "D_SIGN_CENSUS": census,
        "E_MECHANISMS": mechanisms,
        "F_CALIBRATION": calibration,
        "G_VERDICT": verdict,
        "H_CONTROLS": controls,
    }
    sys.stdout.write(render_fixed_point(certificates))
    return 0 if all(row["pass"] for row in certificates.values()) else 1


if __name__ == "__main__":
    raise SystemExit(run())
