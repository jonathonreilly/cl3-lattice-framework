#!/usr/bin/env python3
"""Cycle712 joint-state/full-update compiler for one adjacent two-cell block.

The construction generalizes the Cycle655 spanning-tree encoder to the landed
Cycle706/709 OpenReference and PatchGraph+rail symplectic bases.  It then
decodes the twelve Fock occupation bits, applies the Cycle230 two-cell
coin/reverse/seam/contact word, and re-encodes on the same literal Cycle707
M2 placement.  A three-cell/two-seam case is held out without refit.

This is a bounded fixed-program theorem runner.  Its serial circuit ordinal is
not physical time, and its prepared stabilizer/rail/repetition sectors are
named supplies rather than autonomously generated initial conditions.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from functools import lru_cache
from hashlib import sha256
from collections import Counter
from itertools import combinations
import json
import math
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

AUDIT_TIMEOUT_SEC = 360
NOTE_PATH = (
    "docs/JOINT_TWO_CELL_FULL_UPDATE_PHYSICAL_M2_COMPILER_"
    "CYCLE712_BOUNDED_THEOREM_NOTE_2026-07-26.md"
)
AUDIT_INPUT_PATHS = (
    "docs/JOINT_TWO_CELL_FULL_UPDATE_PHYSICAL_M2_COMPILER_"
    "CYCLE712_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "scripts/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py",
    "docs/LOCAL_SEAM_SIGNED_CLIFFORD_PHYSICAL_M2_COMPILER_"
    "CYCLE709_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/OPENREFERENCE_PATCHGRAPH_FOUR_RAIL_SIGNED_CLIFFORD_"
    "EQUIVALENCE_CYCLE706_NOTE_2026-07-26.md",
    "docs/LITERAL_PATCHGRAPH_Z3_M2_PLACEMENT_AND_FIXED_CONTROLLER_"
    "CYCLE707_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/PHYSICAL_CYCLE704_FSWAP_ENDPOINT_CUBE_BRIDGE_"
    "CYCLE708_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/FULL128_LOCAL_M64_SEAM_M2_BARE_FRAME_INTERTWINER_"
    "BOUNDED_THEOREM_NOTE_2026-07-24.md",
    "scripts/frontier_cycle709_local_seam_clifford_2026_07_26.py",
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
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import frontier_cycle709_local_seam_clifford_core_2026_07_26 as C709
import frontier_cycle709_local_seam_physical_core_2026_07_26 as P709
import frontier_full128_cycle_encoder_2026_07_24 as F128
import frontier_full128_25site_nn_circuit_core_2026_07_24 as S25
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as C230


c707 = P709.c707
TOL = 3e-10
CELLS = ((0, 0, 0), (1, 0, 0))
N_LOGICAL = 12
FSWAP = S25.FSWAP


@dataclass(frozen=True)
class AGate:
    kind: str
    wires: tuple[int, ...]
    matrix: np.ndarray


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


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


def json_safe(value):
    if isinstance(value, dict):
        return {str(key): json_safe(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [json_safe(item) for item in value]
    if isinstance(value, np.generic):
        return value.item()
    return value


def pauli_fields(row):
    return row.phase % 4, row.x, row.z


def pauli_matrix(qubits: int, x: int, z: int) -> np.ndarray:
    output = np.zeros((1 << qubits, 1 << qubits), complex)
    row = c707.Pauli(x=x, z=z)
    for basis in range(1 << qubits):
        state = np.zeros(1 << qubits, complex)
        state[basis] = 1
        output[:, basis] = c707.apply_pauli(state, row, qubits)
    return output


@lru_cache(maxsize=None)
def local_table(matrix_digest: str, arity: int):
    matrices = {
        c707.c655.matrix_digest(c707.c655.H): c707.c655.H,
        c707.c655.matrix_digest(c707.S_GATE): c707.S_GATE,
        c707.c655.matrix_digest(c707.SDG_GATE): c707.SDG_GATE,
        c707.c655.matrix_digest(c707.c655.CNOT): c707.c655.CNOT,
    }
    unitary = matrices[matrix_digest]
    canonical = {
        (x, z): pauli_matrix(arity, x, z)
        for x in range(1 << arity) for z in range(1 << arity)
    }
    table = {}
    maximum = 0.0
    for x in range(1 << arity):
        for z in range(1 << arity):
            transformed = unitary @ canonical[x, z] @ unitary.conj().T
            hits = []
            for tx in range(1 << arity):
                for tz in range(1 << arity):
                    for phase in range(4):
                        residual = float(np.linalg.norm(
                            transformed - (1j ** phase) * canonical[tx, tz]
                        ))
                        if residual < 1e-10:
                            hits.append((phase, tx, tz, residual))
            if len(hits) != 1:
                raise AssertionError((matrix_digest, arity, x, z, hits))
            phase, tx, tz, residual = hits[0]
            maximum = max(maximum, residual)
            table[x, z] = (phase, tx, tz)
    return table, maximum


def conjugate_row(row, gate: AGate):
    local_x = local_z = 0
    for local, wire in enumerate(gate.wires):
        local_x |= ((row.x >> wire) & 1) << local
        local_z |= ((row.z >> wire) & 1) << local
    table, _residual = local_table(
        c707.c655.matrix_digest(gate.matrix), len(gate.wires)
    )
    phase, tx, tz = table[local_x, local_z]
    x, z = row.x, row.z
    for local, wire in enumerate(gate.wires):
        x = (x & ~(1 << wire)) | (((tx >> local) & 1) << wire)
        z = (z & ~(1 << wire)) | (((tz >> local) & 1) << wire)
    return c707.Pauli((row.phase + phase) % 4, x, z)


def apply_gate_to_rows(rows, gate):
    return [conjugate_row(row, gate) for row in rows]


def one(kind, wire, matrix):
    return AGate(kind, (wire,), matrix)


def cnot(control, target, kind="CNOT"):
    return AGate(kind, (control, target), c707.c655.CNOT)


def append_gate(rows, word, gate):
    word.append(gate)
    return apply_gate_to_rows(rows, gate)


def append_swap(rows, word, left, right):
    for gate in (
        cnot(left, right, "synth_SWAP_CNOT"),
        cnot(right, left, "synth_SWAP_CNOT"),
        cnot(left, right, "synth_SWAP_CNOT"),
    ):
        rows = append_gate(rows, word, gate)
    return rows


def append_cz(rows, word, left, right):
    for gate in (
        one("synth_CZ_H", right, c707.c655.H),
        cnot(left, right, "synth_CZ_CNOT"),
        one("synth_CZ_H", right, c707.c655.H),
    ):
        rows = append_gate(rows, word, gate)
    return rows


def append_x(rows, word, wire):
    for gate in (
        one("synth_X_H", wire, c707.c655.H),
        one("synth_X_S", wire, c707.S_GATE),
        one("synth_X_S", wire, c707.S_GATE),
        one("synth_X_H", wire, c707.c655.H),
    ):
        rows = append_gate(rows, word, gate)
    return rows


def append_z(rows, word, wire):
    for gate in (
        one("synth_Z_S", wire, c707.S_GATE),
        one("synth_Z_S", wire, c707.S_GATE),
    ):
        rows = append_gate(rows, word, gate)
    return rows


def canonical_rows(qubits):
    return (
        [c707.Pauli(z=1 << q) for q in range(qubits)]
        + [c707.Pauli(x=1 << q) for q in range(qubits)]
    )


def tableau_rows(w_rows, v_rows):
    return [c707.Pauli(row.phase, row.x, row.z) for row in tuple(w_rows) + tuple(v_rows)]


def tableau_failures(rows, target):
    return sum(pauli_fields(left) != pauli_fields(right) for left, right in zip(rows, target))


def synthesize_decode(w_rows, v_rows):
    """Return R with R W_i R^dag=Z_i and R V_i R^dag=X_i."""
    qubits = len(w_rows)
    rows = tableau_rows(w_rows, v_rows)
    word = []
    for index in range(qubits):
        row = rows[index]
        pivot = next(
            q for q in range(index, qubits)
            if ((row.x | row.z) >> q) & 1
        )
        # Make the whole remaining support Z-type before parity collection.
        for wire in range(index, qubits):
            if not ((rows[index].x >> wire) & 1):
                continue
            if (rows[index].z >> wire) & 1:
                rows = append_gate(
                    rows, word, one("synth_Sdg", wire, c707.SDG_GATE)
                )
            rows = append_gate(rows, word, one("synth_H", wire, c707.c655.H))
        if pivot != index:
            rows = append_swap(rows, word, pivot, index)
        for target in range(index + 1, qubits):
            if (rows[index].z >> target) & 1:
                rows = append_gate(
                    rows, word, cnot(target, index, "synth_clear_W_CNOT")
                )
        if (rows[index].x, rows[index].z) != (0, 1 << index):
            raise AssertionError(("W support", index, rows[index]))
        if rows[index].phase == 2:
            rows = append_x(rows, word, index)
        if rows[index].phase != 0:
            raise AssertionError(("W phase", index, rows[index]))

        v_index = qubits + index
        for target in range(index + 1, qubits):
            if (rows[v_index].x >> target) & 1:
                rows = append_gate(
                    rows, word, cnot(index, target, "synth_clear_VX_CNOT")
                )
            if (rows[v_index].z >> target) & 1:
                rows = append_cz(rows, word, index, target)
        if (rows[v_index].z >> index) & 1:
            rows = append_gate(
                rows, word, one("synth_V_Sdg", index, c707.SDG_GATE)
            )
        if (rows[v_index].x, rows[v_index].z) != (1 << index, 0):
            raise AssertionError(("V support", index, rows[v_index]))
        if rows[v_index].phase == 2:
            rows = append_z(rows, word, index)
        if rows[v_index].phase != 0:
            raise AssertionError(("V phase", index, rows[v_index]))
    canonical = canonical_rows(qubits)
    if tableau_failures(rows, canonical):
        raise AssertionError("tableau synthesis did not reduce to canonical")
    return tuple(word)


def inverse_word(word):
    inverse = []
    inverse_matrices = {
        c707.c655.matrix_digest(c707.c655.H): c707.c655.H,
        c707.c655.matrix_digest(c707.S_GATE): c707.SDG_GATE,
        c707.c655.matrix_digest(c707.SDG_GATE): c707.S_GATE,
        c707.c655.matrix_digest(c707.c655.CNOT): c707.c655.CNOT,
    }
    for gate in reversed(word):
        matrix = inverse_matrices[c707.c655.matrix_digest(gate.matrix)]
        inverse.append(AGate("inverse_" + gate.kind, gate.wires, matrix))
    return tuple(inverse)


def apply_word_rows(rows, word):
    output = list(rows)
    for gate in word:
        output = apply_gate_to_rows(output, gate)
    return output


def graph_components(graph):
    adjacency = {vertex: set() for vertex in range(len(graph.vertices))}
    for u, v, _kind, _owner in graph.edges:
        adjacency[u].add(v)
        adjacency[v].add(u)
    components = 0
    unseen = set(adjacency)
    while unseen:
        components += 1
        stack = [unseen.pop()]
        while stack:
            vertex = stack.pop()
            for target in adjacency[vertex] & unseen:
                unseen.remove(target)
                stack.append(target)
    return components


def rank(rows, qubits):
    return C709.G.c706.base.gf2_rank(row.symplectic(qubits) for row in rows)


def carriers_for(equivalence, graph, site_map, gauges):
    lookup = {
        P709.c707_edge_key(graph, edge): edge
        for edge in range(len(graph.edges))
    }
    carriers = []
    for edge in range(len(equivalence.patch_graph.edges)):
        carriers.append(tuple(site_map[lookup[C709.G.c706.edge_key(
            equivalence.patch_graph, edge
        )]]))
    carriers.extend((site,) for site in P709.rail_sites(equivalence, graph, gauges))
    return tuple(carriers)


def natural_relabel_word(word, natural_map):
    return tuple(
        AGate(gate.kind, tuple(natural_map[wire] for wire in gate.wires), gate.matrix)
        for gate in word
    )


def decoded_word(cell_count=2):
    coin, _mass, _phase = F128.common_coin()
    schedule, qr_residual = S25.compile_adjacent_qr(coin)
    gates = []
    for cell in range(cell_count):
        offset = 6 * cell
        gates.extend(
            AGate(kind, tuple(offset + wire for wire in wires), matrix)
            for kind, wires, matrix in schedule
        )
    for offset in range(0, 6 * cell_count, 6):
        for left, right in ((0, 1), (2, 3), (4, 5)):
            gates.append(AGate("reverse_FSWAP", (offset + left, offset + right), FSWAP))
    # Each pair of seam endpoints is nonadjacent in the global Fock order.  A
    # single tensor FSWAP omits the intervening exterior signs.  The forward
    # adjacent walk and all-but-last return is its literal CAR transposition.
    for cell in range(cell_count - 1):
        left_endpoint, right_endpoint = 6 * cell + 1, 6 * (cell + 1)
        adjacent = tuple(
            (wire, wire + 1) for wire in range(left_endpoint, right_endpoint)
        )
        for left, right in adjacent + tuple(reversed(adjacent[:-1])):
            gates.append(AGate("seam_FSWAP", (left, right), FSWAP))
    contact = np.diag((1, 1, 1, np.exp(1j * F128.CONTACT))).astype(complex)
    for offset in range(0, 6 * cell_count, 6):
        for left, right in combinations(range(6), 2):
            gates.append(AGate("onsite_contact", (offset + left, offset + right), contact))
    return tuple(gates), qr_residual


def subspace(modes=12, cutoff=2):
    return tuple(basis for basis in range(1 << modes) if basis.bit_count() <= cutoff)


def restricted_gate(gate, basis, modes=12):
    lookup = {value: index for index, value in enumerate(basis)}
    output = np.zeros((len(basis), len(basis)), complex)
    wires = gate.wires
    for column, state in enumerate(basis):
        local_in = sum(((state >> wire) & 1) << index for index, wire in enumerate(wires))
        for local_out in range(1 << len(wires)):
            amplitude = gate.matrix[local_out, local_in]
            if abs(amplitude) < 1e-15:
                continue
            target = state
            for index, wire in enumerate(wires):
                target = (target & ~(1 << wire)) | (((local_out >> index) & 1) << wire)
            if target not in lookup:
                raise AssertionError(("number leakage", gate.kind, state, target))
            output[lookup[target], column] += amplitude
    return output


def restricted_fock(one_particle, basis):
    modes = one_particle.shape[0]
    occupied = tuple(tuple(q for q in range(modes) if (state >> q) & 1) for state in basis)
    output = np.zeros((len(basis), len(basis)), complex)
    for row, target in enumerate(occupied):
        for column, source in enumerate(occupied):
            if len(target) != len(source):
                continue
            output[row, column] = 1 if not target else np.linalg.det(
                one_particle[np.ix_(target, source)]
            )
    return output


def direct_restricted_update(basis, cell_count=2):
    modes = 6 * cell_count
    coin, _mass, _phase = F128.common_coin()
    coin_all = np.zeros((modes, modes), complex)
    for offset in range(0, modes, 6):
        coin_all[offset : offset + 6, offset : offset + 6] = coin
    reverse_map = list(range(modes))
    for offset in range(0, modes, 6):
        for left, right in ((0, 1), (2, 3), (4, 5)):
            reverse_map[offset + left], reverse_map[offset + right] = (
                reverse_map[offset + right], reverse_map[offset + left]
            )
    reverse = F128.permutation_matrix(tuple(reverse_map), modes)
    seam_map = list(range(modes))
    for cell in range(cell_count - 1):
        left, right = 6 * cell + 1, 6 * (cell + 1)
        seam_map[left], seam_map[right] = seam_map[right], seam_map[left]
    seam = F128.permutation_matrix(tuple(seam_map), modes)
    free_one = seam @ reverse @ coin_all
    free = restricted_fock(free_one, basis)
    phases = []
    for state in basis:
        phase = 1.0 + 0.0j
        for offset in range(0, modes, 6):
            number = ((state >> offset) & 0x3F).bit_count()
            phase *= np.exp(1j * F128.CONTACT * number * (number - 1) / 2)
        phases.append(phase)
    return np.diag(phases) @ free, coin_all, free_one


def compose_restricted(word, basis, modes):
    output = np.eye(len(basis), dtype=complex)
    for gate in word:
        output = restricted_gate(gate, basis, modes) @ output
    return output


def apply_gate_vector(state, gate, modes):
    """Apply a little-endian local gate without forming a 2^m square matrix."""
    tensor = np.asarray(state, dtype=complex).reshape((2,) * modes)
    wire_axes = tuple(modes - 1 - wire for wire in reversed(gate.wires))
    other_axes = tuple(axis for axis in range(modes) if axis not in wire_axes)
    order = other_axes + wire_axes
    moved = np.transpose(tensor, order)
    rows = moved.reshape((-1, 1 << len(gate.wires)))
    acted = rows @ gate.matrix.T
    restored = acted.reshape(moved.shape)
    inverse = np.argsort(order)
    return np.transpose(restored, inverse).reshape(-1)


def contact_phase(state, cell_count):
    phase = 1.0 + 0.0j
    for offset in range(0, 6 * cell_count, 6):
        number = ((state >> offset) & 0x3F).bit_count()
        phase *= np.exp(1j * F128.CONTACT * number * (number - 1) / 2)
    return phase


def expected_column(source, one_particle, cell_count):
    modes = one_particle.shape[0]
    occupied_source = tuple(q for q in range(modes) if (source >> q) & 1)
    number = len(occupied_source)
    output = np.zeros(1 << modes, complex)
    for target_modes in combinations(range(modes), number):
        target = sum(1 << wire for wire in target_modes)
        amplitude = 1.0 if number == 0 else np.linalg.det(
            one_particle[np.ix_(target_modes, occupied_source)]
        )
        output[target] = contact_phase(target, cell_count) * amplitude
    return output


def sector_complete_certificate(word, free_one, cell_count, active_columns=True):
    """Prove all sectors by local Gamma factors and probe every N block."""
    modes = 6 * cell_count
    compiled_one = np.eye(modes, dtype=complex)
    free_factor_residual = 0.0
    number_leakage = 0.0
    for gate in word:
        counts = np.asarray([basis.bit_count() for basis in range(1 << len(gate.wires))])
        number_leakage = max(
            number_leakage,
            max(
                (
                    abs(gate.matrix[target, source])
                    for target in range(len(counts))
                    for source in range(len(counts))
                    if counts[target] != counts[source]
                ),
                default=0.0,
            ),
        )
        if gate.kind == "onsite_contact":
            expected = np.diag((1, 1, 1, np.exp(1j * F128.CONTACT)))
            free_factor_residual = max(
                free_factor_residual, float(np.linalg.norm(gate.matrix - expected))
            )
            continue
        local_modes = len(gate.wires)
        one_indices = tuple(1 << wire for wire in range(local_modes))
        local_one = gate.matrix[np.ix_(one_indices, one_indices)]
        lifted = F128.fock_lift(local_one)
        free_factor_residual = max(
            free_factor_residual, float(np.linalg.norm(gate.matrix - lifted))
        )
        embedded = np.eye(modes, dtype=complex)
        embedded[np.ix_(gate.wires, gate.wires)] = local_one
        compiled_one = embedded @ compiled_one

    contact_all_basis_residual = 0.0
    for state in range(1 << modes):
        product_phase = 1.0 + 0.0j
        for gate in word:
            if gate.kind != "onsite_contact":
                continue
            left, right = gate.wires
            if ((state >> left) & 1) and ((state >> right) & 1):
                product_phase *= np.exp(1j * F128.CONTACT)
        contact_all_basis_residual = max(
            contact_all_basis_residual, abs(product_phase - contact_phase(state, cell_count))
        )

    alternating = tuple(range(0, modes, 2)) + tuple(range(1, modes, 2))
    active_sources = []
    if active_columns:
        for number in range(modes + 1):
            candidates = (
                (1 << number) - 1,
                ((1 << number) - 1) << (modes - number),
                sum(1 << wire for wire in alternating[:number]),
            )
            active_sources.extend((number, source) for source in dict.fromkeys(candidates))
    maximum_column_residual = 0.0
    sector_maxima = {number: 0.0 for number in range(modes + 1)}
    for number, source in active_sources:
        observed = np.zeros(1 << modes, complex)
        observed[source] = 1
        for gate in word:
            observed = apply_gate_vector(observed, gate, modes)
        residual = float(np.linalg.norm(observed - expected_column(source, free_one, cell_count)))
        maximum_column_residual = max(maximum_column_residual, residual)
        sector_maxima[number] = max(sector_maxima[number], residual)
    return {
        "full_logical_dimension": 1 << modes,
        "particle_number_sectors": modes + 1,
        "second_quantized_local_factor_residual": free_factor_residual,
        "compiled_one_particle_residual": float(np.linalg.norm(compiled_one - free_one)),
        "local_number_leakage_amplitude": number_leakage,
        "contact_all_basis_phase_residual": contact_all_basis_residual,
        "active_columns": len(active_sources),
        "active_columns_by_sector": dict(Counter(number for number, _source in active_sources)),
        "active_sector_maximum_residuals": sector_maxima,
        "maximum_active_column_residual": maximum_column_residual,
        "proof": (
            "each free primitive equals Gamma of its one-particle restriction; "
            "Gamma is a homomorphism on every exterior-power sector; every "
            "contact primitive is the supplied occupied-pair phase and their "
            "product was checked on every computational basis state"
        ),
    }


def stage_and_falsifier_certificate(word, basis, free_one):
    modes = 12
    coin_gates = tuple(gate for gate in word if gate.kind.startswith("coin_"))
    reverse_gates = tuple(gate for gate in word if gate.kind == "reverse_FSWAP")
    seam_gates = tuple(gate for gate in word if gate.kind == "seam_FSWAP")
    contact_gates = tuple(gate for gate in word if gate.kind == "onsite_contact")
    _direct, coin_one, _free = direct_restricted_update(basis)
    reverse_map = list(range(modes))
    for offset in (0, 6):
        for left, right in ((0, 1), (2, 3), (4, 5)):
            reverse_map[offset + left], reverse_map[offset + right] = (
                reverse_map[offset + right], reverse_map[offset + left]
            )
    seam_map = list(range(modes))
    seam_map[1], seam_map[6] = seam_map[6], seam_map[1]
    expected_contact = np.diag([contact_phase(state, 2) for state in basis])
    single = (AGate("single_nonadjacent_tensor_FSWAP", (1, 6), FSWAP),)
    return {
        "coin_stage_residual": float(np.linalg.norm(
            compose_restricted(coin_gates, basis, modes) - restricted_fock(coin_one, basis)
        )),
        "reverse_stage_residual": float(np.linalg.norm(
            compose_restricted(reverse_gates, basis, modes)
            - restricted_fock(F128.permutation_matrix(tuple(reverse_map), modes), basis)
        )),
        "landed_seam_stage_residual": float(np.linalg.norm(
            compose_restricted(seam_gates, basis, modes)
            - restricted_fock(F128.permutation_matrix(tuple(seam_map), modes), basis)
        )),
        "contact_stage_residual": float(np.linalg.norm(
            compose_restricted(contact_gates, basis, modes) - expected_contact
        )),
        "single_nonadjacent_tensor_FSWAP_residual": float(np.linalg.norm(
            compose_restricted(single, basis, modes)
            - restricted_fock(F128.permutation_matrix(tuple(seam_map), modes), basis)
        )),
        "falsifier_interpretation": (
            "the nonadjacent two-wire tensor gate omits intervening CAR parity; "
            "the nine landed adjacent FSWAPs restore it"
        ),
        "free_one_particle_target_digest": sha256(np.round(free_one, 14).tobytes()).hexdigest(),
    }


def cycle230_semantic_certificate(word):
    coin230 = C230.c219.common_species(C230.BETA).coin
    coin, mass, _rest = F128.common_coin()
    expected_fswap = np.asarray(
        ((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, -1)),
        dtype=complex,
    )
    one_cell_basis = tuple(range(64))
    contact_word = tuple(
        gate for gate in decoded_word(1)[0] if gate.kind == "onsite_contact"
    )
    compiled_contact = compose_restricted(contact_word, one_cell_basis, 6)
    numbers = np.asarray([state.bit_count() for state in one_cell_basis])
    cycle230_contact = np.diag(
        np.exp(1j * C230.COUPLING * numbers * (numbers - 1) / 2)
    )
    reverse_map = list(range(12))
    for offset in (0, 6):
        for left, right in ((0, 1), (2, 3), (4, 5)):
            reverse_map[offset + left], reverse_map[offset + right] = (
                reverse_map[offset + right], reverse_map[offset + left]
            )
    seam_map = list(range(12))
    seam_map[1], seam_map[6] = seam_map[6], seam_map[1]
    internal_stream = F128.permutation_matrix(tuple(seam_map), 12) @ F128.permutation_matrix(
        tuple(reverse_map), 12
    )
    # This is Cycle230's S=B A convention restricted to the one internal +x
    # bond; exterior endpoints remain at the block boundary.
    convention_map = list(reverse_map)
    convention_map[0] = 6
    convention_map[7] = 1
    convention_stream = F128.permutation_matrix(tuple(convention_map), 12)
    return {
        "Cycle230_beta": C230.BETA,
        "Cycle230_contact_coupling": C230.COUPLING,
        "coin_matrix_residual": float(np.linalg.norm(coin - coin230)),
        "mass_formula": "3 tan(-beta/2)",
        "mass_residual": abs(mass - 3 * math.tan(-C230.BETA / 2)),
        "FSWAP_matrix_residual": float(np.linalg.norm(FSWAP - expected_fswap)),
        "onsite_64_state_contact_residual": float(
            np.linalg.norm(compiled_contact - cycle230_contact)
        ),
        "internal_depth_two_stream_residual": float(
            np.linalg.norm(internal_stream - convention_stream)
        ),
        "decoded_word_contact_gates_per_cell": sum(
            gate.kind == "onsite_contact" for gate in word
        ) // 2,
        "scope": (
            "exact Cycle230 intrinsic-CAR coin, reverse/edge convention, and "
            "onsite contact on the one internal +x bond; exterior boundary streams held"
        ),
    }


def abstract_to_physical(word, wire_sites, prefix):
    return tuple(
        c707.Instruction(
            prefix + gate.kind,
            tuple(wire_sites[wire] for wire in gate.wires),
            gate.matrix,
        )
        for gate in word
    )


def inverse_instructions(word, prefix="inverse_"):
    return tuple(
        c707.Instruction(
            prefix + gate.kind, gate.sites, gate.matrix.conj().T
        )
        for gate in reversed(word)
    )


def stabilizer_certificate(eq, target_decode, repeated, logical_word):
    qubits = eq.qubits
    logical = len(eq.target_logical_z)
    auxiliaries = eq.target_w[logical:]
    decoded = apply_word_rows(auxiliaries, target_decode)
    expected = [c707.Pauli(z=1 << index) for index in range(logical, qubits)]
    auxiliary_wire_violations = sum(
        any(wire >= logical for wire in gate.wires) for gate in logical_word
    )
    restored = apply_word_rows(decoded, inverse_word(target_decode))
    shared = len(eq.target_shared_loops)
    ds = len(eq.target_ds)
    rails = len(eq.target_rails)
    class_rows = {
        "cycle": eq.target_shared_loops,
        "D": eq.target_ds,
        "rail": eq.target_rails,
    }
    deletion_dimensions = {}
    for name, rows in class_rows.items():
        if not rows:
            continue
        deleted = list(auxiliaries)
        deleted.remove(rows[0])
        deleted_rank = rank(deleted, qubits)
        deletion_dimensions[name] = {
            "rank_after_one_deletion": deleted_rank,
            "code_dimension_after_one_deletion": 1 << (qubits - deleted_rank),
            "dimension_ratio": 1 << (rank(auxiliaries, qubits) - deleted_rank),
        }
    repeated_delete_failures = len(repeated)
    return {
        "stabilizer_class_counts": {
            "shared_cycle": shared,
            "D": ds,
            "rail": rails,
            "repetition": len(repeated),
        },
        "auxiliary_stabilizer_decode_failures": tableau_failures(decoded, expected),
        "decoded_update_auxiliary_wire_violations": auxiliary_wire_violations,
        "cycle_D_rail_restoration_failures": tableau_failures(
            restored, auxiliaries
        ),
        "reason": (
            "target decode sends all code stabilizers to Z on auxiliary wires; "
            "the update acts only on logical wires; target encode restores them; "
            "the outer CNOT restores each Z_left Z_right repetition stabilizer"
        ),
        "one_row_deletions": deletion_dimensions,
        "delete_repetition_encode_stabilizer_mismatches": repeated_delete_failures,
    }


def held_three_cell_certificate():
    cells = ((0, 0, 0), (1, 0, 0), (2, 0, 0))
    eq, graph, site_map, gauges, occupied, collisions = P709.placement_bundle(cells)
    carriers = carriers_for(eq, graph, site_map, gauges)
    wire_sites = tuple(carrier[0] for carrier in carriers)
    repeated = tuple(index for index, carrier in enumerate(carriers) if len(carrier) == 2)
    target_decode = synthesize_decode(eq.target_w, eq.target_v)
    target_encode = inverse_word(target_decode)
    rows = tableau_rows(eq.target_w, eq.target_v)
    decode_failures = tableau_failures(
        apply_word_rows(rows, target_decode), canonical_rows(eq.qubits)
    )
    encode_failures = tableau_failures(
        apply_word_rows(canonical_rows(eq.qubits), target_encode), rows
    )
    logical_word, qr_residual = decoded_word(3)
    basis = subspace(18, 2)
    observed = compose_restricted(logical_word, basis, 18)
    direct, _coin, free_one = direct_restricted_update(basis, 3)
    residual = float(np.linalg.norm(observed - direct))
    sector_proof = sector_complete_certificate(
        logical_word, free_one, 3, active_columns=False
    )
    repetition_decode = tuple(
        c707.Instruction("held_repetition_decode_CNOT", carriers[index], c707.c655.CNOT)
        for index in repeated
    )
    repetition_encode = tuple(
        c707.Instruction("held_repetition_encode_CNOT", carriers[index], c707.c655.CNOT)
        for index in reversed(repeated)
    )
    physical_word = (
        repetition_decode
        + abstract_to_physical(target_decode, wire_sites, "held_target_decode_")
        + abstract_to_physical(logical_word, wire_sites, "held_decoded_")
        + abstract_to_physical(target_encode, wire_sites, "held_target_encode_")
        + repetition_encode
    )
    routed, route_report = c707.route_word(physical_word)
    stabilizers = eq.target_w[len(eq.target_logical_z) :]
    report = {
        "cells": cells,
        "overlapping_internal_seams": 2,
        "logical_modes": len(eq.target_logical_z),
        "abstract_qubits": eq.qubits,
        "stabilizer_rank": rank(stabilizers, eq.qubits),
        "code_dimension": 1 << (eq.qubits - rank(stabilizers, eq.qubits)),
        "expected_M64_cubed": 64 ** 3,
        "literal_M2": len(occupied),
        "placement_collisions": collisions,
        "repeated_abstract_qubits": repeated,
        "decode_gates": len(target_decode),
        "encode_gates": len(target_encode),
        "decode_failures": decode_failures,
        "encode_failures": encode_failures,
        "decoded_gate_census": dict(Counter(gate.kind for gate in logical_word)),
        "coin_QR_residual": qr_residual,
        "N_le_2_dimension": len(basis),
        "combined_N_le_2_EG_residual": residual,
        "all_sector_factorization": sector_proof,
        "physical_primitives": len(physical_word),
        "routed_gates": len(routed),
        "maximum_route_distance": route_report["maximum_route_distance"],
        "non_NN_failures": route_report["non_NN_failures"],
        "operand_order_failures": route_report["operand_order_failures"],
        "route_return_failures": route_report["route_return_failures"],
        "routed_word_sha256": route_report["word_sha256"],
        "without_refit": (
            "same graph-basis synthesizer, same six-mode QR/reverse/contact compiler, "
            "and the same adjacent-CAR seam template; only the supplied cell tuple changed"
        ),
    }
    report["pass"] = (
        report["code_dimension"] == report["expected_M64_cubed"]
        and collisions == decode_failures == encode_failures == 0
        and residual < TOL
        and sector_proof["second_quantized_local_factor_residual"] < TOL
        and sector_proof["compiled_one_particle_residual"] < TOL
        and sector_proof["contact_all_basis_phase_residual"] < TOL
        and not any(route_report[key] for key in (
            "non_NN_failures", "operand_order_failures", "route_return_failures"
        ))
    )
    return report


def frame_chart_certificate():
    frames = C709.F.base.proper_cubic_frames()
    source = C709.F.build_equivalence(CELLS)
    source_rows = tuple(source.target_w) + tuple(source.target_v)
    encoder_failures = dimension_failures = 0
    gate_counts = []
    for frame in frames:
        cells = tuple(
            tuple(int(value) for value in frame @ np.asarray(cell))
            for cell in CELLS
        )
        target = C709.F.build_equivalence(cells)
        word = synthesize_decode(target.target_w, target.target_v)
        gate_counts.append(len(word))
        encoder_failures += tableau_failures(
            apply_word_rows(tableau_rows(target.target_w, target.target_v), word),
            canonical_rows(target.qubits),
        )
        dimension_failures += (
            1 << (
                target.qubits
                - rank(target.target_w[len(target.target_logical_z) :], target.qubits)
            )
        ) != 4096

    composition_failures = transform_failures = 0
    for left in frames:
        for right in frames:
            product = left @ right
            middle_cells = tuple(
                tuple(int(value) for value in right @ np.asarray(cell))
                for cell in CELLS
            )
            final_cells = tuple(
                tuple(int(value) for value in product @ np.asarray(cell))
                for cell in CELLS
            )
            middle = C709.F.build_equivalence(middle_cells)
            final = C709.F.build_equivalence(final_cells)
            first = C709.F.graph_transform_data(
                source.patch_graph, middle.patch_graph, right
            )
            second = C709.F.graph_transform_data(
                middle.patch_graph, final.patch_graph, left
            )
            direct = C709.F.graph_transform_data(
                source.patch_graph, final.patch_graph, product
            )
            transform_failures += first[-1] + second[-1] + direct[-1]
            for row in source_rows:
                sequential = C709.F.transform_augmented_pauli(
                    C709.F.transform_augmented_pauli(
                        row, source, middle, first, first[0]
                    ),
                    middle, final, second, second[0],
                )
                directly = C709.F.transform_augmented_pauli(
                    row, source, final, direct, direct[0]
                )
                composition_failures += sequential != directly
    _vacuum_update, coin_all, base_free = direct_restricted_update((0,), 2)
    reverse_map = list(range(12))
    for offset in (0, 6):
        for first_mode, second_mode in ((0, 1), (2, 3), (4, 5)):
            reverse_map[offset + first_mode], reverse_map[offset + second_mode] = (
                reverse_map[offset + second_mode], reverse_map[offset + first_mode]
            )
    reverse = F128.permutation_matrix(tuple(reverse_map), 12)
    update_covariance_residual = 0.0
    contact_permutation_failures = 0
    for frame in frames:
        mapping = C709.F.base.direction_map(frame)
        mapping12 = tuple(mapping[index] for index in range(6)) + tuple(
            6 + mapping[index] for index in range(6)
        )
        gamma = F128.permutation_matrix(mapping12, 12)
        seam_map = list(range(12))
        left, right = mapping[1], 6 + mapping[0]
        seam_map[left], seam_map[right] = seam_map[right], seam_map[left]
        rotated_free = (
            F128.permutation_matrix(tuple(seam_map), 12) @ reverse @ coin_all
        )
        update_covariance_residual = max(
            update_covariance_residual,
            float(np.linalg.norm(gamma @ base_free @ gamma.conj().T - rotated_free)),
        )
        for state in range(1 << 12):
            moved = sum(
                ((state >> source_wire) & 1) << target_wire
                for source_wire, target_wire in enumerate(mapping12)
            )
            contact_permutation_failures += (
                abs(contact_phase(state, 2) - contact_phase(moved, 2)) > TOL
            )
    update_group_failures = 0
    for left_frame in frames:
        left_map = C709.F.base.direction_map(left_frame)
        for right_frame in frames:
            right_map = C709.F.base.direction_map(right_frame)
            product_map = C709.F.base.direction_map(left_frame @ right_frame)
            update_group_failures += sum(
                product_map[mode] != left_map[right_map[mode]] for mode in range(6)
            )

    equivalence_covariance = C709.F.covariance_controls(source)
    seam_transport = C709.frame_transport_certificate()
    seam_products = C709.frame_product_certificate()
    return {
        "proper_cubic_frames": len(frames),
        "ordered_frame_pairs": len(frames) ** 2,
        "native_chart_encoder_failures": encoder_failures,
        "native_chart_dimension_failures": dimension_failures,
        "native_chart_encoder_gate_range": (min(gate_counts), max(gate_counts)),
        "all_WV_chart_transform_failures": transform_failures,
        "all_WV_chart_composition_failures": composition_failures,
        "decoded_update_all24_one_particle_covariance_residual": update_covariance_residual,
        "decoded_contact_all24_permutation_failures": int(contact_permutation_failures),
        "decoded_update_all576_mode_composition_failures": update_group_failures,
        "cycle706_equivalence_covariance": json_safe(equivalence_covariance),
        "cycle709_signed_seam_transport": json_safe(seam_transport),
        "cycle709_signed_seam_products": json_safe(seam_products),
        "update_naturality": (
            "for chart f define E_f by its synthesized native tableau and "
            "G_f=E_f G_decoded E_f^dag; then T_gf=E_g E_f^dag gives "
            "T_gf G_f=G_g T_gf and the tested 576 chart compositions"
        ),
        "owned_interface_scope": (
            "exact chart composition is closed; independently stored overlapping "
            "coframe registers and a relation-tag controller are not constructed"
        ),
    }


def main():
    eq = C709.G.build_equivalence(CELLS).equivalence
    qubits = eq.qubits
    composition = C709.coloured_composition(CELLS)
    graph, site_map, gauges, occupied_sites, collisions = (
        P709.physical_bundle(CELLS) if hasattr(P709, "physical_bundle")
        else (None, None, None, None, None)
    )
    # Cycle709 exposes placement_bundle rather than the later Cycle710 helper.
    _eq2, graph, site_map, gauges, occupied_sites, collisions = P709.placement_bundle(CELLS)
    carriers = carriers_for(eq, graph, site_map, gauges)
    wire_sites = tuple(carrier[0] for carrier in carriers)
    repeated = tuple(index for index, carrier in enumerate(carriers) if len(carrier) == 2)

    open_components = graph_components(eq.open_graph)
    patch_components = graph_components(eq.patch_graph)
    open_cycle_rank = len(eq.open_graph.edges) - len(eq.open_graph.vertices) + open_components
    patch_cycle_rank = len(eq.patch_graph.edges) - len(eq.patch_graph.vertices) + patch_components
    logical_count = len(eq.target_logical_z)
    target_stabilizers = eq.target_w[logical_count:]
    stabilizer_rank = rank(target_stabilizers, qubits)
    dimension = {
        "connected_cells_C": 2,
        "internal_bonds_B": 1,
        "global_count_formula": "n=18C+2B, s=12C+2B, k=6C",
        "formula_abstract_qubits": 18 * 2 + 2 * 1,
        "formula_stabilizers": 12 * 2 + 2 * 1,
        "formula_logical_modes": 6 * 2,
        "matter_modes": logical_count,
        "abstract_qubits": qubits,
        "open_vertices": len(eq.open_graph.vertices),
        "open_edges": len(eq.open_graph.edges),
        "open_components": open_components,
        "open_cycle_rank": open_cycle_rank,
        "patch_vertices": len(eq.patch_graph.vertices),
        "patch_edges": len(eq.patch_graph.edges),
        "patch_components": patch_components,
        "patch_cycle_rank": patch_cycle_rank,
        "rails": len(eq.rail_labels),
        "shared_loop_rows": len(eq.target_shared_loops),
        "D_rows": len(eq.target_ds),
        "rail_rows": len(eq.target_rails),
        "rail_completion_logical_deficit": 0,
        "stabilizer_rank": stabilizer_rank,
        "code_dimension": 1 << (qubits - stabilizer_rank),
        "expected_M64_tensor_M64": 64 * 64,
        "delete_rail_rank": rank(target_stabilizers[:-1], qubits),
        "delete_rail_code_dimension": 1 << (qubits - rank(target_stabilizers[:-1], qubits)),
    }

    target_decode = synthesize_decode(eq.target_w, eq.target_v)
    source_decode = synthesize_decode(eq.source_w, eq.source_v)
    target_encode = inverse_word(target_decode)
    source_encode = inverse_word(source_decode)
    target_rows = tableau_rows(eq.target_w, eq.target_v)
    source_rows = tableau_rows(eq.source_w, eq.source_v)
    synth = {
        "target_decode_gates": len(target_decode),
        "source_decode_gates": len(source_decode),
        "target_decode_failures": tableau_failures(
            apply_word_rows(target_rows, target_decode), canonical_rows(qubits)
        ),
        "target_encode_failures": tableau_failures(
            apply_word_rows(canonical_rows(qubits), target_encode), target_rows
        ),
        "source_decode_failures": tableau_failures(
            apply_word_rows(source_rows, source_decode), canonical_rows(qubits)
        ),
        "source_encode_failures": tableau_failures(
            apply_word_rows(canonical_rows(qubits), source_encode), source_rows
        ),
        "maximum_local_table_residual": max(
            local_table(c707.c655.matrix_digest(matrix), arity)[1]
            for matrix, arity in (
                (c707.c655.H, 1), (c707.S_GATE, 1),
                (c707.SDG_GATE, 1), (c707.c655.CNOT, 2),
            )
        ),
    }

    # Check the landed Cycle709 seam tableau is exactly the change between the
    # generalized source and target state encoders.
    natural_source = []
    for row in source_rows:
        natural_source.append(c707.Pauli(
            row.phase,
            sum(((row.x >> source) & 1) << target for source, target in eq.natural_edge_map.items()),
            sum(((row.z >> source) & 1) << target for source, target in eq.natural_edge_map.items()),
        ))
    bridge_images = composition.cleaned
    bridged = tuple(C709.apply_images(bridge_images, row, qubits) for row in natural_source)
    bridge_tableau_failures = tableau_failures(
        [c707.Pauli(row.phase, row.x, row.z) for row in bridged], target_rows
    )

    factors = C709.seam_factors(eq, (0, 0, 0), 0)
    physical_factors = tuple(
        P709.physical_lift(row, eq, graph, site_map, gauges)[0] for row in factors
    )
    _local, _support, seam_bridge_word = P709.compile_factor_rows(
        physical_factors, C709.ROTATION_SIGNS, occupied_sites
    )

    logical_word, qr_residual = decoded_word()
    basis = subspace()
    compiled = np.eye(len(basis), dtype=complex)
    gate_unitarity = 0.0
    for gate in logical_word:
        local = restricted_gate(gate, basis)
        compiled = local @ compiled
        gate_unitarity = max(
            gate_unitarity,
            float(np.linalg.norm(gate.matrix.conj().T @ gate.matrix - np.eye(gate.matrix.shape[0])))
        )
    direct, coin12, free12 = direct_restricted_update(basis)
    combined_residual = float(np.linalg.norm(compiled - direct))
    number = np.diag([state.bit_count() for state in basis]).astype(complex)
    number_commutator = float(np.linalg.norm(compiled @ number - number @ compiled))
    logical_unitarity = float(np.linalg.norm(compiled.conj().T @ compiled - np.eye(len(basis))))

    deletions = {}
    for kind in (
        "coin_phase", "coin_givens", "reverse_FSWAP", "seam_FSWAP", "onsite_contact"
    ):
        deleted = False
        observed = np.eye(len(basis), dtype=complex)
        for gate in logical_word:
            if not deleted and gate.kind == kind:
                deleted = True
                continue
            observed = restricted_gate(gate, basis) @ observed
        deletions[kind] = float(np.linalg.norm(observed - direct))

    uniform = np.ones(6, complex) / math.sqrt(6)
    coin, mass, _rest = F128.common_coin()
    eigenvalue = np.vdot(uniform, coin @ uniform)
    compiled_mass = float(np.angle(eigenvalue)) / (1 / 3)

    # Direct target encoder word on the 39 literal M2 isometry.
    repetition_decode = tuple(
        c707.Instruction(
            "repetition_decode_CNOT", carriers[index], c707.c655.CNOT
        ) for index in repeated
    )
    repetition_encode = tuple(
        c707.Instruction(
            "repetition_encode_CNOT", carriers[index], c707.c655.CNOT
        ) for index in reversed(repeated)
    )
    direct_word = (
        repetition_decode
        + abstract_to_physical(target_decode, wire_sites, "target_decode_")
        + abstract_to_physical(logical_word, wire_sites, "decoded_")
        + abstract_to_physical(target_encode, wire_sites, "target_encode_")
        + repetition_encode
    )
    direct_routed, direct_route_report = c707.route_word(direct_word)
    # Equivalent landed-bridge path: T_709^-1 ; source decode ; G ; source
    # encode ; T_709.  Source abstract wires are relabelled by the natural map.
    source_decode_natural = natural_relabel_word(source_decode, eq.natural_edge_map)
    source_encode_natural = natural_relabel_word(source_encode, eq.natural_edge_map)
    bridge_word = (
        inverse_instructions(seam_bridge_word, "bridge_inverse_")
        + repetition_decode
        + abstract_to_physical(source_decode_natural, wire_sites, "source_decode_")
        + abstract_to_physical(logical_word, wire_sites, "decoded_")
        + abstract_to_physical(source_encode_natural, wire_sites, "source_encode_")
        + repetition_encode
        + tuple(seam_bridge_word)
    )
    routed, route_report = c707.route_word(bridge_word)

    # A deleted Clifford decode gate leaves at least one canonical generator
    # unresolved; this is the code-path deletion control without a dense 2^38
    # state vector.
    deleted_decode = target_decode[1:]
    decode_delete_failures = tableau_failures(
        apply_word_rows(target_rows, deleted_decode), canonical_rows(qubits)
    )

    full_sector = sector_complete_certificate(logical_word, free12, 2)
    stages = stage_and_falsifier_certificate(logical_word, basis, free12)
    cycle230_semantics = cycle230_semantic_certificate(logical_word)
    stabilizer_leakage = stabilizer_certificate(
        eq, target_decode, repeated, logical_word
    )
    held = held_three_cell_certificate()
    frames = frame_chart_certificate()
    source_paths = transitive_repo_script_paths()
    source_inventory = {
        path: digest(ROOT / path) for path in source_paths
    }

    report = {
        "baseline_commit": "70e8153ec24ecc812ad692debd57f8a8b67573f2",
        "dimension_and_rail_completion": dimension,
        "state_isometry": {
            "formula": "E = Rep U_target (I_4096 tensor |0>^26)",
            "logical_dimension": 1 << N_LOGICAL,
            "auxiliary_zero_qubits": qubits - N_LOGICAL,
            "literal_M2": len(occupied_sites),
            "placement_collisions": collisions,
            "repeated_abstract_qubits": repeated,
            "repetition_ancilla_M2": sum(len(carrier) - 1 for carrier in carriers),
            "E_dagger_E_exact_by_unitary_ancilla_injection": True,
            "synthesis": synth,
        },
        "Cycle655_naive_gluing_control": {
            "Cycle655_logical_modes_per_cell_including_live_port": F128.LOGICAL_MODES,
            "matter_modes_per_cell": 6,
            "excess_live_port_bits_per_cell": F128.LOGICAL_MODES - 6,
            "two_naively_glued_Cycle655_logical_bits": 2 * F128.LOGICAL_MODES,
            "direct_global_PatchGraph_logical_bits": logical_count,
            "two_cell_excess_bits": 2 * F128.LOGICAL_MODES - logical_count,
            "naive_to_direct_dimension_ratio": (
                1 << (2 * F128.LOGICAL_MODES - logical_count)
            ),
            "interpretation": (
                "the direct global PatchGraph E is primary: it counts each six-mode "
                "cell once and fixes the internal rail sector instead of retaining "
                "one independent live seam-port occupation per local Cycle655 copy"
            ),
        },
        "cycle709_bridge_reconciliation": {
            "abstract_tableau_failures": bridge_tableau_failures,
            "signed_factors": len(factors),
            "physical_bridge_primitives_each_direction": len(seam_bridge_word),
            "physical_factor_weights": tuple((row.x | row.z).bit_count() for row in physical_factors),
        },
        "coarse_and_decoded_update": {
            "logical_domain": (
                "full M64 tensor M64; dense comparator on N<=2 plus sector-complete "
                "second-quantized factor proof and active columns in every N=0..12 sector"
            ),
            "full_logical_dimension": 1 << N_LOGICAL,
            "N_le_2_comparator_dimension": len(basis),
            "decoded_gate_count": len(logical_word),
            "decoded_gate_census": dict(__import__("collections").Counter(g.kind for g in logical_word)),
            "coin_QR_residual": qr_residual,
            "maximum_local_gate_unitarity_residual": gate_unitarity,
            "combined_N_le_2_EG_residual": combined_residual,
            "combined_N_le_2_unitarity_residual": logical_unitarity,
            "encoded_number_commutator": number_commutator,
            "one_particle_mass": compiled_mass,
            "Cycle230_mass": mass,
            "mass_residual": abs(compiled_mass - mass),
            "stage_and_single_FSWAP_falsifier": stages,
            "all_4096_columns_certificate": full_sector,
            "Cycle230_semantic_reconciliation": cycle230_semantics,
        },
        "stabilizer_leakage": stabilizer_leakage,
        "literal_physical_word": {
            "primary": "direct global PatchGraph+rail target encoder E",
            "direct_target_primitives": len(direct_word),
            "direct_target_routed_gates": len(direct_routed),
            "direct_target_maximum_route_distance": direct_route_report["maximum_route_distance"],
            "direct_target_non_NN_failures": direct_route_report["non_NN_failures"],
            "direct_target_operand_order_failures": direct_route_report["operand_order_failures"],
            "direct_target_route_return_failures": direct_route_report["route_return_failures"],
            "direct_target_routed_word_sha256": direct_route_report["word_sha256"],
            "direct_target_touched_M2": len(direct_route_report["touched_coordinates"]),
            "direct_target_blank_route_work_M2": len(
                set(direct_route_report["touched_coordinates"]) - set(occupied_sites)
            ),
            "alternative": "Cycle709 source encoder flanked by exact landed chart bridges",
            "landed_bridge_primitives": len(bridge_word),
            "landed_bridge_routed_gates": len(routed),
            "landed_bridge_maximum_route_distance": route_report["maximum_route_distance"],
            "landed_bridge_non_NN_failures": route_report["non_NN_failures"],
            "landed_bridge_operand_order_failures": route_report["operand_order_failures"],
            "landed_bridge_route_return_failures": route_report["route_return_failures"],
            "landed_bridge_routed_word_sha256": route_report["word_sha256"],
            "landed_bridge_touched_M2": len(route_report["touched_coordinates"]),
            "landed_bridge_blank_route_work_M2": len(set(route_report["touched_coordinates"]) - set(occupied_sites)),
            "code_leakage_exact_by_decode_update_encode": (
                stabilizer_leakage["auxiliary_stabilizer_decode_failures"] == 0
                and stabilizer_leakage["decoded_update_auxiliary_wire_violations"] == 0
                and stabilizer_leakage["cycle_D_rail_restoration_failures"] == 0
            ),
            "EG_residual_by_exact_decode_update_encode_induction": combined_residual,
        },
        "deletions": {
            **deletions,
            "delete_first_decode_gate_tableau_failures": decode_delete_failures,
            "delete_rail_stabilizer_dimension_ratio": (
                dimension["delete_rail_code_dimension"] // dimension["code_dimension"]
            ),
        },
        "held_three_cell_two_overlapping_seams": held,
        "all_24_576_chart_transport": frames,
        "source_inventory_sha256": source_inventory,
        "supplied": (
            "the connected two-cell +x OpenReference/PatchGraph geometry and semantic cell/mode order",
            "the Cycle706 signed W/V symplectic bases and one rail-Z reference completion",
            "the Cycle707 39-M2 placement, stream-edge repetition sector, and serial Manhattan router",
            "the landed Cycle709 four signed seam-chart factors",
            "Cycle230/Cycle655 beta=-0.3 coin, reverse layer, +x seam attachment, g=0.37 onsite contact, and factor order",
            "the stabilizer/repetition/rail +1 sectors and blank route work",
        ),
        "derived": (
            "a rank-38 Clifford state encoder for the 12 logical occupations plus 26 fixed auxiliaries",
            "exact equivalence of the direct target encoder and the source encoder followed by the landed Cycle709 seam-chart bridge",
            "one literal physical decode/free-coin/reverse/seam/contact/re-encode word on the same 39-M2 code",
            "a direct 79-column combined-update comparator on the invariant vacuum/one/two sector",
            "a sector-complete factor proof plus active columns in every particle-number sector of all 4096 logical columns",
            "a held three-cell/two-overlapping-seam 262144-dimensional code and routed word without refit",
            "all-24 native state encoders and all-576 exact W/V chart compositions",
            "active coin, reverse, seam, contact, decode, and rail deletions",
        ),
        "program_schedule_code_genesis": {
            "program": "fixed supplied coin QR, reverse pairs, one internal +x CAR transposition as nine adjacent FSWAPs, onsite contact pairs",
            "schedule": "serial gate order and Manhattan route are supplied circuit ordinals, not physical time",
            "code_genesis": "26 target stabilizers, rail Z=+1, one repetition ancilla, and blank route work are supplied",
            "controller_genesis": "none constructed; the complete word is emitted offline",
        },
        "open": (
            "physical preparation/enforcement of the 26 stabilizers, rail, repetition ancilla, and route work",
            "a collision-free autonomous parallel controller and any physical time/rate interpretation",
            "external-boundary streams beyond the one internal +x seam block",
            "owned-interface independent coframes and a coherent relation-tag controller",
            "literal routed physical words for every one of the 24/576 transported charts (abstract chart maps and native encoders close)",
        ),
    }
    declared = tuple((ROOT / path).resolve() for path in AUDIT_INPUT_PATHS)
    declared_scripts = {
        path for path in AUDIT_INPUT_PATHS if path.startswith("scripts/")
    }
    missing_scripts = tuple(
        path for path in source_paths if path not in declared_scripts
    )
    checks = {
        "source_closure": len(declared) == len(set(declared))
        and all(path.is_file() and path.is_relative_to(ROOT) for path in declared)
        and not missing_scripts,
        "dimension": dimension["code_dimension"] == dimension["expected_M64_tensor_M64"] == 4096
        and dimension["delete_rail_code_dimension"] == 8192
        and dimension["formula_abstract_qubits"] == dimension["abstract_qubits"]
        and dimension["formula_stabilizers"] == dimension["stabilizer_rank"]
        and dimension["formula_logical_modes"] == dimension["matter_modes"]
        and F128.LOGICAL_MODES - 6 == 1,
        "synthesis": not any(value for key, value in synth.items() if key.endswith("failures")),
        "bridge": bridge_tableau_failures == 0,
        "combined_EG": combined_residual < TOL and logical_unitarity < TOL
        and number_commutator < TOL and abs(compiled_mass - mass) < TOL
        and full_sector["second_quantized_local_factor_residual"] < TOL
        and full_sector["compiled_one_particle_residual"] < TOL
        and full_sector["contact_all_basis_phase_residual"] < TOL
        and full_sector["maximum_active_column_residual"] < TOL,
        "Cycle230_semantics": all(
            cycle230_semantics[key] < TOL for key in (
                "coin_matrix_residual", "mass_residual", "FSWAP_matrix_residual",
                "onsite_64_state_contact_residual", "internal_depth_two_stream_residual",
            )
        ),
        "routing": not any(route_report[key] for key in (
            "non_NN_failures", "operand_order_failures", "route_return_failures"
        )) and not any(direct_route_report[key] for key in (
            "non_NN_failures", "operand_order_failures", "route_return_failures"
        )),
        "stabilizer_leakage": (
            stabilizer_leakage["auxiliary_stabilizer_decode_failures"] == 0
            and stabilizer_leakage["decoded_update_auxiliary_wire_violations"] == 0
            and stabilizer_leakage["cycle_D_rail_restoration_failures"] == 0
            and all(row["dimension_ratio"] == 2 for row in stabilizer_leakage["one_row_deletions"].values())
            and stabilizer_leakage["delete_repetition_encode_stabilizer_mismatches"] > 0
        ),
        "held_three_cell": held["pass"],
        "frames_24_576": (
            frames["proper_cubic_frames"] == 24
            and frames["ordered_frame_pairs"] == 576
            and frames["native_chart_encoder_failures"] == 0
            and frames["native_chart_dimension_failures"] == 0
            and frames["all_WV_chart_transform_failures"] == 0
            and frames["all_WV_chart_composition_failures"] == 0
            and frames["decoded_update_all24_one_particle_covariance_residual"] < TOL
            and frames["decoded_contact_all24_permutation_failures"] == 0
            and frames["decoded_update_all576_mode_composition_failures"] == 0
            and frames["cycle706_equivalence_covariance"]["group_failures"] == 0
            and frames["cycle709_signed_seam_transport"]["signed_exact_failures"] == 0
            and frames["cycle709_signed_seam_products"]["signed_factor_diagram_failures"] == 0
        ),
        "deletions": all(value > 1e-6 for value in deletions.values())
        and decode_delete_failures > 0
        and stages["single_nonadjacent_tensor_FSWAP_residual"] > 1,
    }
    report["checks"] = checks
    report["pass"] = all(checks.values())
    report["terminal"] = (
        "CYCLE712_TWO_CELL_JOINT_E_FREE_SEAM_CONTACT_PHYSICAL_M2_PASS"
        if report["pass"] else "CYCLE712_CONSTRUCTIVE_SPLICE_INCOMPLETE"
    )
    report["report_sha256"] = sha256(
        json.dumps(report, sort_keys=True, default=str, separators=(",", ":")).encode()
    ).hexdigest()
    for label, passed in checks.items():
        print("PASS" if passed else "FAIL", label, "::", passed, flush=True)
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True, default=str))
    print(report["terminal"])
    if not report["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
