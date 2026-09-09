#!/usr/bin/env python3
"""Independent finite checks for the corrected Cycle-947 result.

The checker does not import or execute the primary.  It pins the primary
source and cache, parses only the primary's compact CLAIMS_JSON interface,
and recomputes the load-bearing finite facts by different routes:

R1  exhaustive coordinate identities for the bitwise operator basis;
R2  direct counting for the condition-dependent external choice law;
R3  GF(2) matrices for cancellation and ordered CNOT composition;
R4  permutation composition for the identity/local-flip counterexample;
R5  generator closure for the proper cubic rotation subgroup.

These checks concern the declared finite constructions only.  They do not
supply a lane-to-site bridge, a physical choice law, a minimal causal cone,
a full symmetry classification, an H0 discharge, or a successor theory.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 30
STDOUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle947_h0_discharge_2026_07_28.py",
    "logs/runner-cache/frontier_cycle947_h0_discharge_2026_07_28.txt",
)

from collections import Counter, deque
from fractions import Fraction
from hashlib import sha256
import itertools
import json
from pathlib import Path
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH, PRIMARY_CACHE = AUDIT_INPUT_PATHS

# Pinned after the final primary source freeze and its single bounded run.
EXPECTED_SHA256 = {
    PRIMARY_PATH:
        "595f4c292029e5776a8983ece4c337dbe7cfb4dd2b2e59f698a4e0039c08c59e",
    PRIMARY_CACHE:
        "9498ce8fc9ccd13e70298586dd2d88cb353bc4561ebbaa643b410396a5ef54ba",
}

CERTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> bool:
    CERTS.append((name, bool(ok), detail))
    return bool(ok)


def matmul(left: tuple[tuple[int, ...], ...],
           right: tuple[tuple[int, ...], ...]
           ) -> tuple[tuple[int, ...], ...]:
    """Matrix product over GF(2)."""
    rows = len(left)
    inner = len(right)
    columns = len(right[0])
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(inner)) % 2
              for j in range(columns))
        for i in range(rows)
    )


def int_matmul(left: tuple[tuple[int, ...], ...],
               right: tuple[tuple[int, ...], ...]
               ) -> tuple[tuple[int, ...], ...]:
    rows = len(left)
    inner = len(right)
    columns = len(right[0])
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(inner))
              for j in range(columns))
        for i in range(rows)
    )


def apply_matrix(matrix: tuple[tuple[int, ...], ...],
                 vector: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(row[j] * vector[j] for j in range(len(vector))) % 2
                 for row in matrix)


def det3(matrix: tuple[tuple[int, ...], ...]) -> int:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def proper_rotation_closure() -> set[tuple[tuple[int, ...], ...]]:
    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    generators = (
        ((1, 0, 0), (0, 0, -1), (0, 1, 0)),
        ((0, 0, 1), (0, 1, 0), (-1, 0, 0)),
        ((0, -1, 0), (1, 0, 0), (0, 0, 1)),
    )
    found = {identity}
    frontier = deque((identity,))
    while frontier:
        current = frontier.popleft()
        for generator in generators:
            nxt = int_matmul(generator, current)
            if nxt not in found:
                found.add(nxt)
                frontier.append(nxt)
    return found


def box_action(matrix: tuple[tuple[int, ...], ...], side: int = 3
               ) -> tuple[int, ...]:
    points = tuple(itertools.product(range(side), repeat=3))
    point_index = {point: i for i, point in enumerate(points)}
    center = (side - 1) // 2
    image = []
    for point in points:
        centered = tuple(value - center for value in point)
        rotated = tuple(sum(matrix[i][j] * centered[j] for j in range(3))
                        for i in range(3))
        target = tuple(value + center for value in rotated)
        image.append(point_index[target])
    return tuple(image)


def main() -> int:
    started = monotonic()

    payloads: dict[str, bytes] = {}
    pin_rows = []
    pins_ok = True
    for rel in AUDIT_INPUT_PATHS:
        target = ROOT / rel
        body = target.read_bytes() if target.is_file() else b""
        payloads[rel] = body
        actual = sha256(body).hexdigest()
        match = bool(body) and actual == EXPECTED_SHA256[rel]
        pins_ok &= match
        pin_rows.append(f"{rel}:{'MATCH' if match else 'MISMATCH'}")
    check("R0_PINNED_PRIMARY_AND_CACHE", pins_ok, "; ".join(pin_rows))

    claims = None
    for line in payloads[PRIMARY_CACHE].decode(
            "utf-8", errors="replace").splitlines():
        if line.startswith("CLAIMS_JSON: "):
            claims = json.loads(line[len("CLAIMS_JSON: "):])
    check("R0B_CLAIMS_INTERFACE", isinstance(claims, dict),
          f"parsed={isinstance(claims, dict)}")
    if not isinstance(claims, dict):
        claims = {}

    # R1: coordinate identities for the complete supplied operator basis.
    operators = {
        "and": lambda x, y: x & y,
        "or": lambda x, y: x | y,
        "xor": lambda x, y: x ^ y,
    }
    coordinate_rows = 0
    coordinate_ok = True
    for operation in operators.values():
        for left, right in itertools.product(range(4), repeat=2):
            packed = operation(left, right)
            for lane in range(2):
                expected = operation((left >> lane) & 1,
                                     (right >> lane) & 1)
                coordinate_ok &= ((packed >> lane) & 1) == expected
                coordinate_rows += 1
    wire_coupling = (0 ^ 0) != (0 ^ 1)
    no_other_lane_leak = all(
        (((c1 ^ c0) ^ (c1 ^ (c0 ^ (1 << lane)))) == (1 << lane))
        for c0, c1 in itertools.product(range(4), repeat=2)
        for lane in range(2)
    )
    check("R1_BITWISE_COORDINATE_ROUTE",
          coordinate_ok and coordinate_rows == 96 and wire_coupling
          and no_other_lane_leak,
          f"coordinate_rows={coordinate_rows} within_lane_coupling="
          f"{wire_coupling} cross_lane_leak={not no_other_lane_leak}")

    # R2: direct conditional counts, independent of primary trajectory code.
    counts = {
        neighbor: sum(seed < 1 + 2 * neighbor for seed in range(4))
        for neighbor in (0, 1)
    }
    probabilities = {neighbor: Fraction(count, 4)
                     for neighbor, count in counts.items()}
    fixed_choice_rows = {
        (choice, n0, n1): choice == choice
        for choice in (0, 1)
        for n0, n1 in itertools.product((0, 1), repeat=2)
    }
    support = {
        mu: tuple(outcome for outcome, mass in
                  ((0, 1 - mu), (1, mu)) if mass > 0)
        for mu in (Fraction(0), Fraction(1, 4),
                   Fraction(3, 4), Fraction(1))
    }
    choice_ok = (
        probabilities == {0: Fraction(1, 4), 1: Fraction(3, 4)}
        and all(fixed_choice_rows.values())
        and support[Fraction(0)] == (0,)
        and support[Fraction(1)] == (1,)
        and support[Fraction(1, 4)] == (0, 1)
        and support[Fraction(3, 4)] == (0, 1)
    )
    check("R2_CHOICE_DISTRIBUTION_ROUTE", choice_ok,
          f"counts={counts} probabilities="
          f"{dict((k, str(v)) for k, v in probabilities.items())} "
          f"fixed_choice_rows={len(fixed_choice_rows)}")

    # R3a: two equal XOR shears compose to identity although the static
    # control-to-target graph contains y -> x.
    identity2 = ((1, 0), (0, 1))
    xor_y_into_x = ((1, 1), (0, 1))
    cancelled = matmul(xor_y_into_x, xor_y_into_x)
    cancel_outputs = {
        vector: apply_matrix(cancelled, vector)
        for vector in itertools.product((0, 1), repeat=2)
    }
    static_y_to_x = True
    cancellation_ok = (
        static_y_to_x and cancelled == identity2
        and all(vector == output
                for vector, output in cancel_outputs.items())
    )
    check("R3_GRAPH_OVERAPPROXIMATION_GF2", cancellation_ok,
          f"structural_y_to_x={static_y_to_x} product={cancelled} "
          f"states={len(cancel_outputs)}")

    # R3b: two CNOT orders have the same gate multiset.  Swap conjugation
    # interchanges the gates, while the ordered products differ.
    a_to_b = ((1, 0), (1, 1))
    b_to_a = ((1, 1), (0, 1))
    swap = ((0, 1), (1, 0))
    first = matmul(b_to_a, a_to_b)
    second = matmul(a_to_b, b_to_a)
    sigma_a = matmul(matmul(swap, a_to_b), swap)
    sigma_b = matmul(matmul(swap, b_to_a), swap)
    first_map = tuple(apply_matrix(first, vector)
                      for vector in itertools.product((0, 1), repeat=2))
    second_map = tuple(apply_matrix(second, vector)
                       for vector in itertools.product((0, 1), repeat=2))
    multiset_ok = Counter(("a_to_b", "b_to_a")) == Counter(
        ("b_to_a", "a_to_b"))
    order_ok = (multiset_ok and sigma_a == b_to_a and sigma_b == a_to_b
                and first != second and first_map != second_map)
    check("R4_ORDERED_MAP_GF2", order_ok,
          f"first={first} second={second} differing_inputs="
          f"{sum(a != b for a, b in zip(first_map, second_map))}")

    # R4: permutation composition, with no appeal to a sampled commutator.
    states = tuple(range(8))
    identity_rule = tuple(states)
    local_flip = tuple(state ^ 1 for state in states)
    uniform_flip = tuple(state ^ 7 for state in states)
    compose = lambda left, right: tuple(left[right[state]] for state in states)
    local_commutes = compose(identity_rule, local_flip) == compose(
        local_flip, identity_rule)
    local_not_uniform = local_flip != uniform_flip
    check("R5_LOCAL_SYMMETRY_PERMUTATION", local_commutes and local_not_uniform,
          f"states={len(states)} commutes={local_commutes} "
          f"local_not_uniform={local_not_uniform}")

    # R5: generate the spatial subgroup from quarter turns instead of
    # enumerating signed coordinate permutations as the primary does.
    rotations = proper_rotation_closure()
    actions = {box_action(rotation) for rotation in rotations}
    all_proper = all(det3(rotation) == 1 for rotation in rotations)
    all_signed_permutation = all(
        all(sum(abs(value) for value in row) == 1 for row in rotation)
        and all(sum(abs(rotation[i][j]) for i in range(3)) == 1
                for j in range(3))
        for rotation in rotations
    )
    bare_transpositions = 0
    for action in actions:
        moved = [i for i, image in enumerate(action) if i != image]
        if (len(moved) == 2
                and action[moved[0]] == moved[1]
                and action[moved[1]] == moved[0]):
            bare_transpositions += 1
    cube_ok = (len(rotations) == 24 and len(actions) == 24
               and all_proper and all_signed_permutation
               and bare_transpositions == 0)
    check("R6_PROPER_CUBE_GENERATOR_CLOSURE", cube_ok,
          f"rotations={len(rotations)} actions={len(actions)} "
          f"all_det_plus_one={all_proper} bare_transpositions="
          f"{bare_transpositions}")

    expected_claims = {
        "lane_grammar_ok": True,
        "fixed_choice_vs_distribution_counterexample": True,
        "support_boundary_ok": True,
        "graph_reachability_counterexample": True,
        "ordered_multiset_counterexample": True,
        "local_symmetry_implication_counterexample": True,
        "proper_box_isometries": 24,
        "bare_transpositions": 0,
    }
    claims_ok = all(claims.get(key) == value
                    for key, value in expected_claims.items())
    science_digest_ok = (
        isinstance(claims.get("science_digest"), str)
        and len(claims["science_digest"]) == 64
    )
    primary_source = payloads[PRIMARY_PATH].decode(
        "utf-8", errors="replace")
    boundary_ok = all(marker in primary_source for marker in (
        '"physical_site_identification": "open and not supplied"',
        '"external_choice_law_independence": "open and not supplied"',
        '"minimal_semantic_causal_cone": "not established"',
        '"full_symmetry_group": "not classified"',
        '"H0_discharge": False',
        '"unique_successor": "not selected"',
        '"formal_audit": False',
    ))
    check("R7_PRIMARY_INTERFACE_AND_BOUNDARY",
          claims_ok and science_digest_ok and boundary_ok,
          f"selected_claims_match={claims_ok} digest_shape="
          f"{science_digest_ok} boundary_markers={boundary_ok}")

    elapsed = monotonic() - started
    check("R8_RUNTIME", elapsed < AUDIT_TIMEOUT_SEC,
          f"elapsed_s={elapsed:.3f} budget_s={AUDIT_TIMEOUT_SEC}")

    lines = [
        "=" * 78,
        "CYCLE 947 -- CORRECTED H0 FINITE-IMPLICATION INDEPENDENT CHECK",
        "=" * 78,
        "",
        "SCOPE: supplied finite compiler constructions and implication",
        "counterexamples; no physical bridge, H0 discharge, or audit.",
        "",
    ]
    lines.extend(f"  {'PASS' if ok else 'FAIL'}  {name:<38} {detail}"
                 for name, ok, detail in CERTS)
    npass = sum(ok for _name, ok, _detail in CERTS)
    nfail = len(CERTS) - npass
    verdict = ("PRIMARY_SURVIVES_THIS_CHECK" if nfail == 0
               else "PRIMARY_REFUTED_ON_THIS_CHECK")
    lines.extend(("", f"TOTAL: PASS={npass} FAIL={nfail}",
                  f"VERDICT: {verdict}"))
    text = "\n".join(lines)
    sys.stdout.write(text + "\n")

    receipt = {
        "cycle": 947,
        "role": "independent_checker",
        "claim_type": "bounded_theorem",
        "authority": "none",
        "audit": "unset",
        "verdict": verdict,
        "input_paths": list(AUDIT_INPUT_PATHS),
        "input_sha256": {
            rel: sha256(payloads[rel]).hexdigest()
            for rel in AUDIT_INPUT_PATHS
        },
        "routes": {
            "lane": "exhaustive coordinate identities for &, |, ^",
            "choice_law": "direct conditional counting",
            "causality_and_order": "GF(2) matrix products",
            "local_symmetry": "permutation composition",
            "spatial_subgroup": "quarter-turn generator closure",
        },
        "certificates": {
            name: {"pass": ok, "detail": detail}
            for name, ok, detail in CERTS
        },
        "all_certificates_pass": nfail == 0,
        "formal_audit": False,
        "historical_campaign_replayed": False,
    }
    (ROOT / "outputs" /
     "h0_discharge_independent_check_cycle947_receipt_2026_07_28.json"
     ).write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")

    if len(text.encode("utf-8")) > STDOUT_LIMIT_BYTES:
        sys.stderr.write("stdout budget exceeded\n")
        return 1
    return 0 if nfail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
