#!/usr/bin/env python3
"""Independent Cycle712 two-cell full-update cross-check.

This deliberately uses a stabilizer-tableau representation of the 38-mode
PatchGraph+rail Fock isometry.  Code columns are named by their complete
signed commuting tableau rather than expanded into 2**38 amplitudes.

The 4096-column update comparison is independently reconstructed by a creator
wedge, not by importing the primary Cycle712 runner's factor proof.
"""
from __future__ import annotations

import ast
from collections import deque
from functools import lru_cache
from hashlib import sha256
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

AUDIT_TIMEOUT_SEC = 180
NOTE_PATH = (
    "docs/JOINT_TWO_CELL_FULL_UPDATE_PHYSICAL_M2_COMPILER_"
    "CYCLE712_BOUNDED_THEOREM_NOTE_2026-07-26.md"
)
AUDIT_INPUT_PATHS = (
    "docs/JOINT_TWO_CELL_FULL_UPDATE_PHYSICAL_M2_COMPILER_"
    "CYCLE712_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "scripts/frontier_cycle712_joint_two_cell_full_update_independent_check_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py",
    "scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py",
    "scripts/frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py",
    "scripts/frontier_cycle708_cube_basis_gauge_core_2026_07_26.py",
    "scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py",
    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import fock_modular_boundary_current_cycle229_2026_07_17 as c229
import frontier_cycle709_local_seam_physical_core_2026_07_26 as p709

CELLS = ((0, 0, 0), (1, 0, 0))
BETA = -0.3
COUPLING = 0.37
REVERSE_PAIRS = ((0, 1), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11))
SEAM_ADJACENT = ((1, 2), (2, 3), (3, 4), (4, 5), (5, 6),
                 (4, 5), (3, 4), (2, 3), (1, 2))


def gf2_rank(rows):
    pivots = {}
    for value in rows:
        row = int(value)
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def transitive_repo_script_paths():
    """Resolve the literal flat-module import closure under ``scripts/``."""
    scripts_dir = ROOT / "scripts"
    module_paths = {path.stem: path for path in scripts_dir.glob("*.py")}
    pending = [Path(__file__).resolve()]
    seen = set()
    while pending:
        path = pending.pop()
        if path in seen:
            continue
        seen.add(path)
        tree = ast.parse(path.read_text(), filename=str(path))
        imported = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported.extend(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported.append(node.module.split(".")[0])
        pending.extend(
            module_paths[name]
            for name in imported
            if name in module_paths and module_paths[name] not in seen
        )
    return tuple(sorted(path.relative_to(ROOT).as_posix() for path in seen))


def spanning_tree(graph):
    """Fresh lexicographic BFS tree; does not call the landed tree helper."""
    adjacency = [[] for _ in graph.vertices]
    for edge, (u, v, *_rest) in enumerate(graph.edges):
        adjacency[u].append((v, edge)); adjacency[v].append((u, edge))
    for row in adjacency:
        row.sort()
    seen, queue, edges = {0}, deque([0]), []
    while queue:
        u = queue.popleft()
        for v, edge in adjacency[u]:
            if v not in seen:
                seen.add(v); queue.append(v); edges.append(edge)
    return tuple(edges), len(seen)


def fundamental_tree_loops(graph, tree_edges):
    """Build a fresh fundamental-cycle basis from the independent BFS tree."""
    tree_set = set(tree_edges)
    adjacency = [[] for _ in graph.vertices]
    for edge in tree_edges:
        u, v, *_ = graph.edges[edge]
        adjacency[u].append(v)
        adjacency[v].append(u)
    rows = []
    for edge, (source, target, *_rest) in enumerate(graph.edges):
        if edge in tree_set:
            continue
        parent = {source: None}
        queue = deque([source])
        while target not in parent:
            u = queue.popleft()
            for v in adjacency[u]:
                if v not in parent:
                    parent[v] = u
                    queue.append(v)
        reverse_path = []
        v = target
        while v is not None:
            reverse_path.append(v)
            v = parent[v]
        rows.append(graph.loop_pauli(tuple(reversed(reverse_path))))
    return tuple(rows)


def fswap_basis(index, a, b):
    """Apply adjacent FSWAP, returned as (new index, sign)."""
    aa, bb = (index >> a) & 1, (index >> b) & 1
    sign = -1 if aa and bb else 1
    if aa != bb:
        index ^= (1 << a) | (1 << b)
    return index, sign


def apply_fswap_schedule(vector, schedule):
    targets, signs = schedule_arrays(tuple(schedule))
    out = np.empty_like(vector)
    out[targets] = signs * vector
    return out


def direct_nonadjacent_fswap(vector, a=1, b=6):
    """False host shortcut: applies the 4x4 FSWAP truth table to distant bits."""
    out = np.zeros_like(vector)
    for source, value in enumerate(vector):
        target, sign = fswap_basis(source, a, b)
        out[target] += sign * value
    return out


def schedule_basis(index, schedule):
    sign = 1
    for a, b in schedule:
        index, local = fswap_basis(index, a, b)
        sign *= local
    return index, sign


@lru_cache(maxsize=None)
def schedule_arrays(schedule):
    targets = np.empty(1 << 12, dtype=int)
    signs = np.empty(1 << 12, dtype=int)
    for source in range(1 << 12):
        targets[source], signs[source] = schedule_basis(source, schedule)
    return targets, signs


def exterior_permutation_basis(index, mapping):
    targets = [mapping[source] for source in range(len(mapping)) if (index >> source) & 1]
    sign = -1 if sum(targets[i] > targets[j] for i in range(len(targets))
                         for j in range(i+1, len(targets))) & 1 else 1
    target = sum(1 << mode for mode in targets)
    return target, sign


@lru_cache(maxsize=1)
def contact_diagonal():
    result = np.empty(1 << 12, complex)
    for basis in range(1 << 12):
        left = (basis & 63).bit_count()
        right = (basis >> 6).bit_count()
        result[basis] = np.exp(1j * COUPLING *
                               (left * (left - 1) + right * (right - 1)) / 2)
    return result


def factor_column(local_coin, source):
    left, right = source & 63, source >> 6
    # rows are right occupation, columns are left occupation.
    state = np.outer(local_coin[:, right], local_coin[:, left]).reshape(-1)
    state = apply_fswap_schedule(state, REVERSE_PAIRS)
    state = apply_fswap_schedule(state, SEAM_ADJACENT)
    return contact_diagonal() * state


def exterior_column(one_particle, source):
    """Independent exterior lift by successively wedging transformed creators."""
    state = {0: 1.0 + 0.0j}
    # Operators act on the left; descending sources produce the repository's
    # ascending occupation-basis wedge convention.
    for mode in reversed(range(12)):
        if not ((source >> mode) & 1):
            continue
        nxt = {}
        for occupied, amplitude in state.items():
            for target in range(12):
                if (occupied >> target) & 1:
                    continue
                coefficient = one_particle[target, mode]
                if abs(coefficient) < 1e-15:
                    continue
                # a_target^dagger crosses lower occupied modes.
                sign = -1 if (occupied & ((1 << target) - 1)).bit_count() & 1 else 1
                key = occupied | (1 << target)
                nxt[key] = nxt.get(key, 0j) + sign * coefficient * amplitude
        state = nxt
    out = np.zeros(1 << 12, complex)
    for target, amplitude in state.items():
        out[target] = amplitude
    return contact_diagonal() * out


def one_particle_schedule(coin):
    block = np.zeros((12, 12), complex)
    block[:6, :6] = coin; block[6:, 6:] = coin
    perm = np.eye(12, dtype=complex)
    for a, b in REVERSE_PAIRS + SEAM_ADJACENT:
        perm[[a, b]] = perm[[b, a]]
    return perm @ block, perm


def pauli_tuple(row):
    return (int(row.phase), int(row.x), int(row.z))


def main():
    eq, graph, site_map, gauges, all_sites, collisions = p709.placement_bundle(CELLS)
    n, k = len(eq.open_graph.edges), len(eq.target_logical_z)
    tree, reached = spanning_tree(eq.patch_graph)
    tree_loops = fundamental_tree_loops(eq.patch_graph, tree)
    physical_w = []
    for row in eq.target_w:
        lifted, sites = p709.physical_lift(row, eq, graph, site_map, gauges)
        physical_w.append(lifted)
    site_index = {site: i for i, site in enumerate(all_sites)}
    repetition = []
    for edge, *_rest in graph.stream_edges:
        left, right = site_map[edge]
        repetition.append(type(physical_w[0])(
            z=(1 << site_index[left]) | (1 << site_index[right])))
    tree_vectors = [row.x | (row.z << n) for row in tree_loops]
    shared_vectors = [row.x | (row.z << n) for row in eq.target_shared_loops]
    tree_loop_rank = gf2_rank(tree_vectors)
    tree_shared_union_rank = gf2_rank(tree_vectors + shared_vectors)
    physical_rank = gf2_rank([
        row.x | (row.z << len(all_sites))
        for row in physical_w[k:] + repetition
    ])
    physical_full_w = physical_w + repetition
    physical_full_w_rank = gf2_rank([
        row.x | (row.z << len(all_sites)) for row in physical_full_w
    ])
    physical_w_commutator_failures = sum(
        (
            ((left.x & right.z).bit_count()
             + (left.z & right.x).bit_count()) & 1
        )
        for index, left in enumerate(physical_full_w)
        for right in physical_full_w[index + 1 :]
    )
    physical_w_nonhermitian_failures = sum(
        (row.phase - (row.x & row.z).bit_count()) % 2
        for row in physical_full_w
    )

    # Full isometry receipt: each Fock basis column is the unique joint
    # eigenspace of physical W rows (+ repetition), with logical-Z signs.
    iso = sha256()
    tableau_rows = tuple(pauli_tuple(row) for row in physical_w + repetition)
    iso.update(json.dumps(tableau_rows, separators=(",", ":")).encode())
    distinct_signatures = set()
    for basis in range(1 << k):
        signs = basis  # first k rows have eigenvalue (-1)**occupation
        distinct_signatures.add(signs)
        iso.update(signs.to_bytes(2, "little"))

    coin = c219.common_species(BETA).coin
    local_coin = c229.fock_lift(coin)
    one_particle, permutation = one_particle_schedule(coin)
    contact = contact_diagonal()
    update_hash = sha256()
    max_eg = max_norm = max_number = 0.0
    sector_counts = {number: 0 for number in range(13)}
    for source in range(1 << 12):
        observed = factor_column(local_coin, source)
        expected = exterior_column(one_particle, source)
        residual = float(np.max(np.abs(observed - expected)))
        max_eg = max(max_eg, residual)
        max_norm = max(max_norm, abs(float(np.vdot(observed, observed).real) - 1.0))
        number = source.bit_count()
        wrong = np.array([target.bit_count() != number for target in range(1 << 12)])
        max_number = max(max_number, float(np.max(np.abs(observed[wrong]), initial=0.0)))
        sector_counts[number] += 1
        quantized = np.round(np.column_stack((observed.real, observed.imag)), 13)
        quantized[np.abs(quantized) < 5e-14] = 0.0
        update_hash.update(quantized.tobytes())

    # Exact seam permutation and the deliberately unlawful distant shortcut.
    max_seam = 0.0
    false_count = 0
    false_max = 0.0
    for basis in range(1 << 12):
        lawful = schedule_basis(basis, SEAM_ADJACENT)
        mapping = list(range(12)); mapping[1], mapping[6] = mapping[6], mapping[1]
        expected = exterior_permutation_basis(basis, mapping)
        max_seam = max(max_seam, 0.0 if lawful == expected else 2.0)
        false_target, false_sign = fswap_basis(basis, 1, 6)
        false = (false_target, false_sign)
        delta = 0.0 if false == lawful else (2.0 if false_target == lawful[0] else 1.0)
        false_count += delta > 0.5
        false_max = max(false_max, delta)

    # Contact and one-particle/mass fixtures.
    max_contact = 0.0
    for basis, value in enumerate(contact):
        nl, nr = (basis & 63).bit_count(), (basis >> 6).bit_count()
        want = np.exp(1j * COUPLING * (nl*(nl-1)+nr*(nr-1))/2)
        max_contact = max(max_contact, abs(value-want))
    species = c219.common_species(BETA)
    mass = c219.rest_mass(species)
    analytic = species.analytic_mass

    # Physical support/repetition and a routing-distance census for all encoded
    # logical Z, X and pair ZZ axes used by contact/seam compilation.
    logical_rows = list(eq.target_logical_z) + list(eq.target_logical_x)
    pair_rows = []
    for offset in (0, 6):
        for a in range(offset, offset+6):
            for b in range(a+1, offset+6):
                pair_rows.append(eq.target_logical_z[a] @ eq.target_logical_z[b])
    lifted_axes = [p709.physical_lift(row, eq, graph, site_map, gauges)[0]
                   for row in logical_rows + pair_rows]
    repetition_failures = sum(
        p709.repetition_failures(row, graph, site_map, all_sites)
        for row in lifted_axes)
    supports = []
    for row in lifted_axes:
        supports.append(tuple(all_sites[i] for i in range(len(all_sites))
                              if ((row.x | row.z) >> i) & 1))
    max_axis_weight = max(map(len, supports))
    max_l1 = max(
        sum(abs(a-b) for a,b in zip(left,right))
        for support in supports for left in support for right in support
    )
    _local_axes, axis_support, axis_word = p709.compile_factor_rows(
        tuple(lifted_axes), (1,) * len(lifted_axes), all_sites
    )
    routed_axes, axis_route = p709.c707.route_word(axis_word)

    report = {
        "independent_derivation": True,
        "cells": CELLS,
        "abstract_n": n,
        "physical_n": len(all_sites),
        "logical_k": k,
        "abstract_stabilizer_s": len(eq.target_w)-k,
        "physical_constraint_s_including_repetition": len(eq.target_w)-k + len(repetition),
        "patch_tree_edges": len(tree),
        "patch_vertices_reached": reached,
        "patch_cycle_rank": len(eq.patch_graph.edges)-len(eq.patch_graph.vertices)+1,
        "fundamental_tree_loop_count": len(tree_loops),
        "fundamental_tree_loop_rank": tree_loop_rank,
        "tree_loop_target_shared_union_rank": tree_shared_union_rank,
        "tree_loop_span_equals_target_shared_span": (
            tree_loop_rank == tree_shared_union_rank == len(eq.target_shared_loops)
        ),
        "physical_constraint_rank": physical_rank,
        "physical_full_W_rank": physical_full_w_rank,
        "physical_W_commutator_failures": physical_w_commutator_failures,
        "physical_W_nonhermitian_failures": physical_w_nonhermitian_failures,
        "tree_digest": sha256(json.dumps(tree).encode()).hexdigest(),
        "isometry_tableau_digest": iso.hexdigest(),
        "distinct_code_columns": len(distinct_signatures),
        "all_columns_tested": 1 << 12,
        "sector_column_counts": sector_counts,
        "maximum_decoded_update_residual": max_eg,
        "maximum_norm_residual": max_norm,
        "maximum_number_leakage": max_number,
        "update_column_digest_13dp": update_hash.hexdigest(),
        "contact_factor_count": 30,
        "maximum_contact_residual": max_contact,
        "reverse_fswap_count": len(REVERSE_PAIRS),
        "seam_adjacent_fswap_count": len(SEAM_ADJACENT),
        "maximum_seam_residual": max_seam,
        "single_nonadjacent_fswap_false_columns": false_count,
        "single_nonadjacent_fswap_max_residual": false_max,
        "one_particle_contact_residual": float(np.max(np.abs(contact[[0]+[1<<i for i in range(12)]]-1))),
        "mass_fixture": mass,
        "analytic_mass": analytic,
        "mass_residual": abs(mass-analytic),
        "placement_collisions": collisions,
        "repetition_constraint_failures": repetition_failures,
        "compiled_axis_count": len(lifted_axes),
        "maximum_compiled_axis_weight": max_axis_weight,
        "maximum_compiled_axis_L1_diameter": max_l1,
        "axis_routing_topology_primitive_count": len(axis_word),
        "axis_routing_topology_routed_count": len(routed_axes),
        "axis_routing_topology_support_M2": len(axis_support),
        "axis_routing_topology_maximum_route_distance": axis_route["maximum_route_distance"],
        "axis_routing_topology_non_NN_failures": axis_route["non_NN_failures"],
        "axis_routing_topology_operand_order_failures": axis_route["operand_order_failures"],
        "axis_routing_topology_return_failures": axis_route["route_return_failures"],
        "supplied_structure": [
            "two-cell +x PatchGraph geometry and Cycle708 signed tableau",
            "one physical repetition carrier for the stream edge and one rail gauge",
            "lexicographic matter-mode/Fock order 0..11",
            "Cycle219 beta=-0.3 six-mode coin",
            "Cycle230 coupling=0.37 onsite all-pairs contact",
            "declared coin -> reverse -> seam -> contact schedule",
        ],
    }
    declared = tuple((ROOT / path).resolve() for path in AUDIT_INPUT_PATHS)
    transitive_scripts = transitive_repo_script_paths()
    declared_scripts = {
        path for path in AUDIT_INPUT_PATHS if path.startswith("scripts/")
    }
    missing_scripts = tuple(
        path for path in transitive_scripts if path not in declared_scripts
    )
    checks = {
        "source_closure": len(declared) == len(set(declared))
        and all(path.is_file() and path.is_relative_to(ROOT) for path in declared)
        and not missing_scripts,
        "dimension": n == 38 and len(all_sites) == 39 and k == 12
        and len(eq.target_w) - k == 26 and len(repetition) == 1
        and tree_loop_rank == tree_shared_union_rank == len(eq.target_shared_loops) == 24
        and physical_rank == 27,
        "isometry_columns": len(distinct_signatures) == 4096
        and physical_full_w_rank == len(all_sites) == 39
        and physical_w_commutator_failures == 0
        and physical_w_nonhermitian_failures == 0,
        "all_4096_decoded_update": (
            max_eg < 3e-12 and max_norm < 3e-12 and max_number == 0
        ),
        "mass_contact": max_contact < 3e-12 and abs(mass-analytic) < 3e-12,
        "lawful_and_false_seam": max_seam == 0 and false_count > 0 and false_max > 1,
        "placement_and_repetition": collisions == 0 and repetition_failures == 0,
        "axis_routing": not any(axis_route[key] for key in (
            "non_NN_failures", "operand_order_failures", "route_return_failures"
        )),
    }
    report["source_inventory_sha256"] = {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }
    report["checks"] = checks
    report["pass"] = all(checks.values())
    report["terminal"] = (
        "CYCLE712_JOINT_TWO_CELL_FULL_UPDATE_INDEPENDENT_CHECK_PASS"
        if report["pass"] else
        "CYCLE712_JOINT_TWO_CELL_FULL_UPDATE_INDEPENDENT_CHECK_INCOMPLETE"
    )
    payload = json.dumps(report, sort_keys=True, separators=(",", ":"))
    report["report_sha256"] = sha256(payload.encode()).hexdigest()
    for label, passed in checks.items():
        print("PASS" if passed else "FAIL", label, "::", passed, flush=True)
    print(json.dumps(report, indent=2, sort_keys=True))
    print(report["terminal"])
    if not report["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
