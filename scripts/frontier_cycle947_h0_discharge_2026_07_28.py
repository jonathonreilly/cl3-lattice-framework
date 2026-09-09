#!/usr/bin/env python3
"""Corrected Cycle-947 finite implications for a lane-local compiler.

This self-contained runner replaces the historical H0-discharge campaign.
It proves only finite representation and implication facts:

* XOR/AND/OR expressions on non-negative packed integer words act
  independently on each bit lane, while allowing different wire components
  inside a lane to couple;
* a deterministic trajectory can be independent of a neighboring condition
  at fixed external choice and still have a neighbor-dependent distribution
  when the external choice law depends on that condition;
* static control-to-target reachability can strictly overapproximate semantic
  dependence because scheduled operations can cancel;
* a gate multiset, even one invariant under an involution, does not determine
  the ordered composed map;
* covariance under a supplied spatial subgroup does not determine the full
  automorphism group of a rule.

No lane is identified with a physical site. No probability supplier, one-site
domain/action bridge, minimal causal cone, full symmetry classification, H0
discharge, physical law, or unique successor is claimed.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 30
STDOUT_LIMIT_BYTES = 150_000

import ast
from collections import Counter
from fractions import Fraction
from hashlib import sha256
import itertools
import json
from pathlib import Path
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
CERTS: list[tuple[str, bool, str]] = []


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def check(name: str, ok: bool, detail: str) -> bool:
    CERTS.append((name, bool(ok), detail))
    return bool(ok)


def _lane_local_expression(node: ast.expr) -> bool:
    if isinstance(node, ast.Constant):
        return isinstance(node.value, int) and not isinstance(node.value, bool)
    if isinstance(node, ast.Subscript):
        return (
            isinstance(node.value, ast.Name)
            and node.value.id == "c"
            and isinstance(node.slice, ast.Constant)
            and isinstance(node.slice.value, int)
        )
    if isinstance(node, ast.BinOp):
        return (
            isinstance(node.op, (ast.BitAnd, ast.BitOr, ast.BitXor))
            and _lane_local_expression(node.left)
            and _lane_local_expression(node.right)
        )
    return False


def statement_is_lane_local(source: str) -> bool:
    """Recognize the supplied bitwise packed-word grammar, fail closed."""
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return False
    if len(tree.body) != 1 or not isinstance(tree.body[0], ast.AugAssign):
        return False
    node = tree.body[0]
    return (
        isinstance(node.op, ast.BitXor)
        and isinstance(node.target, ast.Subscript)
        and isinstance(node.target.value, ast.Name)
        and node.target.value.id == "c"
        and isinstance(node.target.slice, ast.Constant)
        and isinstance(node.target.slice.value, int)
        and _lane_local_expression(node.value)
    )


def lane_grammar_result() -> dict:
    accepted = (
        "c[1] ^= c[0]",
        "c[2] ^= c[0] & c[1]",
        "c[0] ^= (c[1] | 3) ^ c[2]",
    )
    refused = (
        "c[1] ^= c[0] << 1",
        "c[1] ^= c[0] + c[2]",
        "c[1] = c[0]",
        "c[1] ^= CHOICE(0)",
    )
    accepted_ok = all(statement_is_lane_local(s) for s in accepted)
    refused_ok = all(not statement_is_lane_local(s) for s in refused)

    packed_ok = True
    perturb_ok = True
    for c0, c1 in itertools.product(range(4), repeat=2):
        out = c1 ^ c0
        for lane in range(2):
            expected = ((c1 >> lane) & 1) ^ ((c0 >> lane) & 1)
            packed_ok &= ((out >> lane) & 1) == expected
            changed = out ^ (c1 ^ (c0 ^ (1 << lane)))
            perturb_ok &= changed == (1 << lane)

    before_a = [0, 0]
    before_b = [1, 0]
    after_a = [before_a[0], before_a[1] ^ before_a[0]]
    after_b = [before_b[0], before_b[1] ^ before_b[0]]
    intra_lane_coupling = after_a[1] != after_b[1]
    other_lane_unchanged = all(((after_a[w] ^ after_b[w]) & 2) == 0
                               for w in range(2))
    return {
        "supplied_grammar": "c[i] ^= E where E uses only c[j], integer "
                            "literals, and the bitwise operators &, |, ^",
        "accepted_examples": list(accepted),
        "refused_examples": list(refused),
        "valid_examples_accepted": accepted_ok,
        "nonlocal_or_out_of_grammar_examples_refused": refused_ok,
        "packed_vs_per_lane_exhaustive_two_wires_two_lanes": packed_ok,
        "single_lane_perturbations_never_leak_to_the_other_lane": perturb_ok,
        "accepted_wire_coupling_statement": "c[1] ^= c[0]",
        "wire_1_changes_when_wire_0_changes_inside_lane_0":
            intra_lane_coupling,
        "lane_1_remains_unchanged_in_that_witness": other_lane_unchanged,
        "scope": "lane locality is a property of bit coordinates of "
                 "non-negative packed words in this "
                 "supplied grammar; it does not identify lanes as physical "
                 "sites and it does not forbid wire-to-wire coupling inside "
                 "one lane",
    }


def trajectory(choice_bit: int) -> int:
    """A deterministic lane-local update whose only input is supplied choice."""
    return choice_bit


def external_choice(neighbor_condition: int, seed: int) -> int:
    return int(seed < 1 + 2 * neighbor_condition)


def bernoulli_support(mu: Fraction) -> list[int]:
    support = []
    if 1 - mu > 0:
        support.append(0)
    if mu > 0:
        support.append(1)
    return support


def choice_law_result() -> dict:
    rows = []
    for neighbor in (0, 1):
        outputs = [trajectory(external_choice(neighbor, u))
                   for u in range(4)]
        rows.append({
            "neighbor_condition": neighbor,
            "uniform_seed_values": [0, 1, 2, 3],
            "outputs": outputs,
            "probability_y_equals_1": str(Fraction(sum(outputs), 4)),
        })
    fixed_choice_independence = all(
        trajectory(bit) == trajectory(bit)
        for bit in (0, 1)
        for _neighbor_a, _neighbor_b in itertools.product((0, 1), repeat=2)
    )
    support_rows = {
        str(mu): bernoulli_support(mu)
        for mu in (Fraction(0), Fraction(1, 4), Fraction(3, 4), Fraction(1))
    }
    return {
        "deterministic_update": "y := b; b is an externally supplied bit",
        "trajectory_is_neighbor_independent_at_fixed_choice":
            fixed_choice_independence,
        "conditional_probability_rows": rows,
        "probability_changes_with_neighbor":
            rows[0]["probability_y_equals_1"] == "1/4"
            and rows[1]["probability_y_equals_1"] == "3/4",
        "deterministic_update_has_no_neighbor_argument": True,
        "bernoulli_support_rows": support_rows,
        "both_outcomes_supported_exactly_for_interior_examples":
            support_rows["1/4"] == [0, 1]
            and support_rows["3/4"] == [0, 1]
            and support_rows["0"] == [0]
            and support_rows["1"] == [1],
        "scope": "fixed-choice trajectory independence does not imply "
                 "distribution independence; a distribution-level theorem "
                 "needs a supplied choice law independent of the compared "
                 "conditions; branch existence alone does not establish "
                 "two-point support",
    }


def backward_reachable(edges: tuple[tuple[str, str], ...], seeds: set[str],
                       depth: int | None) -> set[str]:
    reached = set(seeds)
    steps = 0
    while depth is None or steps < depth:
        add = {source for source, target in edges if target in reached}
        if add <= reached:
            break
        reached |= add
        steps += 1
    return reached


def causal_graph_result() -> dict:
    program = ("x ^= y", "x ^= y")
    edges = (("y", "x"), ("y", "x"))
    truth = []
    for x, y in itertools.product((0, 1), repeat=2):
        out = x
        out ^= y
        out ^= y
        truth.append({"x": x, "y": y, "final_x": out})
    graph_ancestors = backward_reachable(edges, {"x"}, None)
    semantic_independence = all(
        next(r["final_x"] for r in truth if r["x"] == x and r["y"] == 0)
        == next(r["final_x"] for r in truth if r["x"] == x and r["y"] == 1)
        for x in (0, 1)
    )
    chain = (("a", "b"), ("b", "c"), ("c", "d"))
    depth_1 = backward_reachable(chain, {"d"}, 1)
    depth_2 = backward_reachable(chain, {"d"}, 2)
    fixed = backward_reachable(chain, {"d"}, None)
    return {
        "cancelling_program": list(program),
        "static_control_to_target_edges": [list(e) for e in edges],
        "static_ancestors_of_x": sorted(graph_ancestors),
        "y_is_statically_reachable": "y" in graph_ancestors,
        "truth_table": truth,
        "final_x_equals_initial_x_on_all_four_states":
            all(r["final_x"] == r["x"] for r in truth),
        "final_x_is_semantically_independent_of_y": semantic_independence,
        "depth_control": {
            "edges": [list(e) for e in chain],
            "depth_1": sorted(depth_1),
            "depth_2": sorted(depth_2),
            "fixed_point": sorted(fixed),
            "depth_2_is_not_the_fixed_point": depth_2 != fixed,
        },
        "scope": "static reachability is a structural overapproximation; "
                 "neither graph reachability nor a depth cap establishes a "
                 "minimal semantic causal cone",
    }


def apply_cnot(state: tuple[int, int], gate: str) -> tuple[int, int]:
    a, b = state
    if gate == "a_to_b":
        return a, b ^ a
    if gate == "b_to_a":
        return a ^ b, b
    raise ValueError(gate)


def apply_sequence(state: tuple[int, int], sequence: tuple[str, ...]
                   ) -> tuple[int, int]:
    for gate in sequence:
        state = apply_cnot(state, gate)
    return state


def order_result() -> dict:
    first = ("a_to_b", "b_to_a")
    second = ("b_to_a", "a_to_b")
    states = tuple(itertools.product((0, 1), repeat=2))
    first_map = {f"{a}{b}": list(apply_sequence((a, b), first))
                 for a, b in states}
    second_map = {f"{a}{b}": list(apply_sequence((a, b), second))
                  for a, b in states}
    sigma = {"a_to_b": "b_to_a", "b_to_a": "a_to_b"}
    return {
        "first_order": list(first),
        "second_order": list(second),
        "same_gate_multiset": Counter(first) == Counter(second),
        "multiset_invariant_under_wire_swap":
            Counter(first) == Counter(sigma[g] for g in first),
        "first_map": first_map,
        "second_map": second_map,
        "composed_maps_differ": first_map != second_map,
        "number_of_inputs_with_different_outputs":
            sum(first_map[k] != second_map[k] for k in first_map),
        "scope": "multiset equality or involution invariance does not imply "
                 "equality of scheduled maps; a semantic claim must bind the "
                 "operation order",
    }


def proper_cubic_rotations() -> tuple[tuple[tuple[int, ...], tuple[int, ...]], ...]:
    rotations = []
    for permutation in itertools.permutations(range(3)):
        parity = 1
        for i in range(3):
            for j in range(i + 1, 3):
                if permutation[i] > permutation[j]:
                    parity *= -1
        for signs in itertools.product((1, -1), repeat=3):
            if parity * signs[0] * signs[1] * signs[2] == 1:
                rotations.append((permutation, signs))
    return tuple(rotations)


def rotate(rotation, point: tuple[int, int, int]) -> tuple[int, int, int]:
    permutation, signs = rotation
    return tuple(signs[i] * point[permutation[i]] for i in range(3))


def box_isometry_result(side: int = 3) -> dict:
    box = tuple(itertools.product(range(side), repeat=3))
    box_set = set(box)
    permutations = []
    for rotation in proper_cubic_rotations():
        raw = [rotate(rotation, point) for point in box]
        translation = tuple(-min(q[i] for q in raw) for i in range(3))
        image = tuple(tuple(q[i] + translation[i] for i in range(3))
                      for q in raw)
        if set(image) == box_set:
            permutations.append(image)
    bare = 0
    for image in permutations:
        moved = [(a, b) for a, b in zip(box, image) if a != b]
        if (len(moved) == 2 and moved[0][1] == moved[1][0]
                and moved[1][1] == moved[0][0]):
            bare += 1
    return {
        "box_side": side,
        "box_points": len(box),
        "proper_cubic_rotations": len(proper_cubic_rotations()),
        "box_preserving_affine_actions": len(permutations),
        "bare_transpositions_in_this_supplied_subgroup": bare,
        "scope": "this finite result concerns only translations composed "
                 "with proper cubic rotations on the supplied box; comparing "
                 "it with lane permutations additionally requires an "
                 "explicit injective equivariant lane-to-point map",
    }


def symmetry_result() -> dict:
    states = tuple(itertools.product((0, 1), repeat=3))

    def identity_rule(state):
        return tuple(state)

    def local_flip(state):
        return (1 - state[0], state[1], state[2])

    commutes = all(
        identity_rule(local_flip(state)) == local_flip(identity_rule(state))
        for state in states
    )
    cube = box_isometry_result()
    return {
        "identity_rule_commutes_with_one_site_flip_on_all_eight_states":
            commutes,
        "local_flip_is_not_the_uniform_three_site_flip":
            local_flip((0, 0, 0)) != (1, 1, 1),
        "implication_counterexample_scope":
            "the identity rule is a counterexample to the inference from a "
            "fixed covariant rule to a claimed exhaustive symmetry group; "
            "it is not asserted to satisfy every physical axiom",
        "supplied_spatial_subgroup": cube,
    }


def compute() -> dict:
    return {
        "claim_type": "bounded_theorem",
        "lane_grammar": lane_grammar_result(),
        "choice_law": choice_law_result(),
        "causal_graph": causal_graph_result(),
        "ordered_multiset": order_result(),
        "symmetry": symmetry_result(),
        "claim_boundary": {
            "physical_site_identification": "open and not supplied",
            "external_choice_law_independence": "open and not supplied",
            "one_site_domain_or_action_bridge": "open and not supplied",
            "minimal_semantic_causal_cone": "not established",
            "full_symmetry_group": "not classified",
            "H0_discharge": False,
            "unique_successor": "not selected",
            "formal_audit": False,
        },
    }


def main() -> int:
    started = monotonic()
    result = compute()
    second = compute()
    lane = result["lane_grammar"]
    choice = result["choice_law"]
    causal = result["causal_graph"]
    ordered = result["ordered_multiset"]
    symmetry = result["symmetry"]
    check("P1_LANE_GRAMMAR", lane["valid_examples_accepted"]
          and lane["nonlocal_or_out_of_grammar_examples_refused"],
          "three accepted, four refused by a fail-closed AST recognizer")
    check("P2_LANE_SEMANTICS", lane[
          "packed_vs_per_lane_exhaustive_two_wires_two_lanes"]
          and lane["single_lane_perturbations_never_leak_to_the_other_lane"]
          and lane["wire_1_changes_when_wire_0_changes_inside_lane_0"]
          and lane["lane_1_remains_unchanged_in_that_witness"],
          "all 16 two-word states and both lane perturbations")
    check("P3_FIXED_CHOICE_VS_DISTRIBUTION",
          choice["trajectory_is_neighbor_independent_at_fixed_choice"]
          and choice["probability_changes_with_neighbor"]
          and choice["deterministic_update_has_no_neighbor_argument"],
          "exact probabilities 1/4 and 3/4 from four equiprobable seeds")
    check("P4_SUPPORT_BOUNDARY", choice[
          "both_outcomes_supported_exactly_for_interior_examples"],
          "mu=0 and mu=1 have singleton support; 1/4 and 3/4 have both")
    check("P5_GRAPH_IS_OVERAPPROXIMATION",
          causal["y_is_statically_reachable"]
          and causal["final_x_equals_initial_x_on_all_four_states"]
          and causal["final_x_is_semantically_independent_of_y"]
          and causal["depth_control"]["depth_2_is_not_the_fixed_point"],
          "double-XOR cancellation plus a four-node depth control")
    check("P6_ORDER_MATTERS", ordered["same_gate_multiset"]
          and ordered["multiset_invariant_under_wire_swap"]
          and ordered["composed_maps_differ"],
          "two CNOT orders, all four Boolean inputs")
    check("P7_SYMMETRY_SCOPE",
          symmetry[
              "identity_rule_commutes_with_one_site_flip_on_all_eight_states"]
          and symmetry["local_flip_is_not_the_uniform_three_site_flip"]
          and symmetry["supplied_spatial_subgroup"][
              "proper_cubic_rotations"] == 24
          and symmetry["supplied_spatial_subgroup"][
              "box_preserving_affine_actions"] == 24
          and symmetry["supplied_spatial_subgroup"][
              "bare_transpositions_in_this_supplied_subgroup"] == 0,
          "identity-rule implication counterexample and the supplied 3-cube "
          "proper-isometry subgroup")
    check("P8_DETERMINISM", digest(result) == digest(second),
          "complete science payload recomputed in-process")
    elapsed = monotonic() - started
    check("P9_RUNTIME", elapsed < AUDIT_TIMEOUT_SEC,
          f"elapsed_s={elapsed:.3f} budget_s={AUDIT_TIMEOUT_SEC}")

    science_digest = digest(result)
    claims = {
        "lane_grammar_ok": all((lane["valid_examples_accepted"],
                                lane["nonlocal_or_out_of_grammar_examples_refused"],
                                lane["packed_vs_per_lane_exhaustive_two_wires_two_lanes"],
                                lane["wire_1_changes_when_wire_0_changes_inside_lane_0"])),
        "fixed_choice_vs_distribution_counterexample":
            choice["probability_changes_with_neighbor"],
        "support_boundary_ok":
            choice["both_outcomes_supported_exactly_for_interior_examples"],
        "graph_reachability_counterexample":
            causal["y_is_statically_reachable"]
            and causal["final_x_is_semantically_independent_of_y"],
        "ordered_multiset_counterexample": ordered["composed_maps_differ"],
        "local_symmetry_implication_counterexample": symmetry[
            "identity_rule_commutes_with_one_site_flip_on_all_eight_states"],
        "proper_box_isometries": symmetry["supplied_spatial_subgroup"][
            "box_preserving_affine_actions"],
        "bare_transpositions": symmetry["supplied_spatial_subgroup"][
            "bare_transpositions_in_this_supplied_subgroup"],
        "science_digest": science_digest,
    }
    lines = [
        "=" * 78,
        "CYCLE 947 -- CORRECTED LANE-LOCAL COMPILER IMPLICATIONS",
        "=" * 78,
        "",
        "SCOPE: finite compiler grammar and implication counterexamples. No",
        "physical site map, choice-law independence, minimal semantic cone,",
        "full symmetry classification, H0 discharge, or successor selection.",
        "",
        "CLAIMS_JSON: " + compact(claims),
        "",
        "-- CERTIFICATES --------------------------------------------------------",
    ]
    lines.extend(f"  {'PASS' if ok else 'FAIL'}  {name:<34} {detail}"
                 for name, ok, detail in CERTS)
    npass = sum(ok for _name, ok, _detail in CERTS)
    nfail = len(CERTS) - npass
    lines.extend(("", f"TOTAL: PASS={npass} FAIL={nfail}",
                  f"VERDICT: {'PASS' if nfail == 0 else 'FAIL'}"))
    text = "\n".join(lines)
    sys.stdout.write(text + "\n")

    receipt = {
        "cycle": 947,
        "claim_type": "bounded_theorem",
        "authority": "none",
        "audit": "unset",
        "headline": "Finite implications of lane-local compilation, with "
                    "counterexamples separating trajectories from choice "
                    "distributions, graph reachability from semantic "
                    "dependence, gate multisets from ordered maps, and a "
                    "supplied covariance subgroup from a full automorphism "
                    "group.",
        "results": result,
        "certificates": {
            name: {"pass": ok, "detail": detail}
            for name, ok, detail in CERTS
        },
        "all_certificates_pass": nfail == 0,
        "science_digest": science_digest,
        "self_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "formal_audit": False,
        "historical_campaign_replayed": False,
    }
    (ROOT / "outputs" / "h0_discharge_cycle947_receipt_2026_07_28.json"
     ).write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    if len(text.encode("utf-8")) > STDOUT_LIMIT_BYTES:
        sys.stderr.write("stdout budget exceeded\n")
        return 1
    return 0 if nfail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
