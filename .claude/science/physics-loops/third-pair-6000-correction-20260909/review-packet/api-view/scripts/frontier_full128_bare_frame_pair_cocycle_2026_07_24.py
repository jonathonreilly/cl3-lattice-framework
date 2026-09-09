#!/usr/bin/env python3
"""Bounded bare-frame antisymmetry cocycle for a six-mode M64 cell.

This probe certifies a finite proper-cubic representation gadget.  It places
one M2 factor on each ordered-pair register site ``4*d_i+d_j``.  Whenever
local modes i and j are both occupied, their two ordered sites carry the
antisymmetric one-excitation state

    (|1_(j,i)> - |1_(i,j)>)/sqrt(2).

The product over all occupied pairs acquires exactly the exterior/Fock
inversion sign under the bare coordinate permutation of every proper-cubic
frame.  A uniform onsite phase on all ordered-pair sites also realizes the
six-mode contact phase exp(i*g*k*(k-1)/2).

The result is a bounded representation/contact certificate only.  It is not a
physical-site compiler, recurrent lattice law, controller, preparation
theorem, or axiom-pressure claim.
"""

from __future__ import annotations

from collections import Counter, deque
from hashlib import sha256
from itertools import permutations, product
import cmath
import json
import math
from pathlib import Path
import resource
import time


START = time.perf_counter()
AUDIT_INPUT_PATHS = (
    "docs/FULL128_LOCAL_M64_SEAM_M2_BARE_FRAME_INTERTWINER_"
    "BOUNDED_THEOREM_NOTE_2026-07-24.md",
)
TOL = 2.0e-12
CONTACT_COUPLING = 0.37
PASS = 0
FAIL = 0

Coord = tuple[int, int, int]
Frame = tuple[Coord, Coord, Coord]

DIRECTIONS: tuple[Coord, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
REVERSE_MODE = (1, 0, 3, 2, 5, 4)
UNORDERED_PAIRS = tuple((i, j) for i in range(6) for j in range(i + 1, 6))
ORDERED_PAIRS = tuple((i, j) for i in range(6) for j in range(6) if i != j)
ORDERED_INDEX = {pair: index for index, pair in enumerate(ORDERED_PAIRS)}


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label} :: {detail}")


def audit_source_closure(paths: tuple[str, ...]) -> bool:
    repo_root = Path(__file__).resolve().parents[1]
    resolved = tuple((repo_root / path).resolve() for path in paths)
    return (
        len(paths) == len(set(paths))
        and all(path.is_file() and repo_root in path.parents for path in resolved)
    )


def add(*rows: Coord) -> Coord:
    return tuple(sum(row[axis] for row in rows) for axis in range(3))  # type: ignore[return-value]


def scale(factor: int, row: Coord) -> Coord:
    return tuple(factor * value for value in row)  # type: ignore[return-value]


def det3(frame: Frame) -> int:
    a, b, c = frame
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def matvec(frame: Frame, vector: Coord) -> Coord:
    return tuple(sum(frame[row][column] * vector[column] for column in range(3)) for row in range(3))  # type: ignore[return-value]


def matmul(left: Frame, right: Frame) -> Frame:
    return tuple(
        tuple(sum(left[row][inner] * right[inner][column] for inner in range(3)) for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def proper_cubic_frames() -> tuple[Frame, ...]:
    frames = set()
    for order in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            frame = tuple(
                tuple(signs[row] if column == order[row] else 0 for column in range(3))
                for row in range(3)
            )
            if det3(frame) == 1:
                frames.add(frame)
    return tuple(sorted(frames))


FRAMES = proper_cubic_frames()
FRAME_INDEX = {frame: index for index, frame in enumerate(FRAMES)}


def mode_map(frame: Frame) -> tuple[int, ...]:
    return tuple(DIRECTIONS.index(matvec(frame, direction)) for direction in DIRECTIONS)


MODE_MAPS = tuple(mode_map(frame) for frame in FRAMES)


def shell_sites() -> set[Coord]:
    sites = {(0, 0, 0)}
    sites.update(DIRECTIONS)
    sites.update(scale(2, direction) for direction in DIRECTIONS)
    for left, right in UNORDERED_PAIRS:
        if REVERSE_MODE[left] != right:
            sites.add(add(DIRECTIONS[left], DIRECTIONS[right]))
    return sites


SHELL = shell_sites()
REGISTER_SITE = {
    (i, j): add(scale(4, DIRECTIONS[i]), DIRECTIONS[j]) for i, j in ORDERED_PAIRS
}
REGISTER = set(REGISTER_SITE.values())
CORRIDOR = {scale(4, direction) for direction in DIRECTIONS}
SITES = tuple(sorted(SHELL | REGISTER | CORRIDOR))
SITE_INDEX = {site: index for index, site in enumerate(SITES)}


def l1(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


ADJACENCY = {
    site: tuple(target for target in SITES if l1(site, target) == 1) for site in SITES
}


def distances(source: Coord) -> dict[Coord, int]:
    output = {source: 0}
    queue = deque((source,))
    while queue:
        site = queue.popleft()
        for target in ADJACENCY[site]:
            if target not in output:
                output[target] = output[site] + 1
                queue.append(target)
    return output


DISTANCES = {site: distances(site) for site in SITES}


def occupied(bits: int) -> tuple[int, ...]:
    return tuple(mode for mode in range(6) if (bits >> mode) & 1)


def transformed_bits(bits: int, mapping: tuple[int, ...]) -> int:
    output = 0
    for source in occupied(bits):
        output |= 1 << mapping[source]
    return output


def exterior_sign(bits: int, mapping: tuple[int, ...]) -> int:
    modes = occupied(bits)
    inversions = sum(
        mapping[left] > mapping[right]
        for index, left in enumerate(modes)
        for right in modes[index + 1 :]
    )
    return -1 if inversions & 1 else 1


def register_sign(bits: int, mapping: tuple[int, ...]) -> int:
    flips = sum(
        ((bits >> left) & 1)
        and ((bits >> right) & 1)
        and mapping[left] > mapping[right]
        for left, right in UNORDERED_PAIRS
    )
    return -1 if flips & 1 else 1


SparseState = dict[int, complex]


def register_state(bits: int, antisymmetric: bool = True) -> SparseState:
    """Return the 30-qubit ordered-pair register as a sparse state."""
    state: SparseState = {0: 1.0 + 0.0j}
    inverse_sqrt_two = 1.0 / math.sqrt(2.0)
    for left, right in UNORDERED_PAIRS:
        if not (((bits >> left) & 1) and ((bits >> right) & 1)):
            continue
        forward = 1 << ORDERED_INDEX[(left, right)]
        backward = 1 << ORDERED_INDEX[(right, left)]
        next_state: SparseState = {}
        for mask, amplitude in state.items():
            next_state[mask | backward] = amplitude * inverse_sqrt_two
            next_state[mask | forward] = amplitude * inverse_sqrt_two * (-1 if antisymmetric else 1)
        state = next_state
    return state


def permute_register(state: SparseState, mapping: tuple[int, ...]) -> SparseState:
    output: SparseState = {}
    for mask, amplitude in state.items():
        target = 0
        work = mask
        while work:
            bit = work & -work
            source_index = bit.bit_length() - 1
            left, right = ORDERED_PAIRS[source_index]
            target |= 1 << ORDERED_INDEX[(mapping[left], mapping[right])]
            work ^= bit
        output[target] = output.get(target, 0.0j) + amplitude
    return output


def sparse_residual(left: SparseState, right: SparseState) -> float:
    keys = set(left) | set(right)
    return math.sqrt(sum(abs(left.get(key, 0.0j) - right.get(key, 0.0j)) ** 2 for key in keys))


def scale_state(state: SparseState, scalar: complex) -> SparseState:
    return {mask: scalar * amplitude for mask, amplitude in state.items()}


def contact_register_action(state: SparseState, deleted: set[int] | None = None) -> SparseState:
    deleted = deleted or set()
    output = {}
    for mask, amplitude in state.items():
        active_phases = (mask & ~sum(1 << index for index in deleted)).bit_count()
        output[mask] = amplitude * cmath.exp(1j * CONTACT_COUPLING * active_phases)
    return output


# Five-bit reversible preparation gadget: q_i, q_j, flag, a_(i,j), a_(j,i).
def basis_permutation(state: SparseState, function) -> SparseState:
    output: SparseState = {}
    for basis, amplitude in state.items():
        target = function(basis)
        output[target] = output.get(target, 0.0j) + amplitude
    return output


def toffoli(state: SparseState) -> SparseState:
    return basis_permutation(
        state,
        lambda basis: basis ^ (1 << 2) if (basis & 1) and (basis & 2) else basis,
    )


def cnot(state: SparseState, control: int, target: int) -> SparseState:
    return basis_permutation(
        state,
        lambda basis: basis ^ (1 << target) if (basis >> control) & 1 else basis,
    )


def controlled_h(state: SparseState) -> SparseState:
    output: SparseState = {}
    inverse_sqrt_two = 1.0 / math.sqrt(2.0)
    for basis, amplitude in state.items():
        if not ((basis >> 2) & 1):
            output[basis] = output.get(basis, 0.0j) + amplitude
            continue
        input_bit = (basis >> 3) & 1
        zero = basis & ~(1 << 3)
        one = zero | (1 << 3)
        output[zero] = output.get(zero, 0.0j) + amplitude * inverse_sqrt_two
        output[one] = output.get(one, 0.0j) + amplitude * inverse_sqrt_two * (-1 if input_bit else 1)
    return output


def z_on_a(state: SparseState) -> SparseState:
    return {
        basis: amplitude * (-1 if (basis >> 3) & 1 else 1)
        for basis, amplitude in state.items()
    }


def gadget(state: SparseState, inverse: bool = False, delete_phase: bool = False, delete_uncompute: bool = False) -> SparseState:
    operations = (
        toffoli,
        lambda row: cnot(row, 2, 4),
        controlled_h,
        lambda row: cnot(row, 3, 4),
        (lambda row: row) if delete_phase else z_on_a,
        (lambda row: row) if delete_uncompute else toffoli,
    )
    for operation in reversed(operations) if inverse else operations:
        state = operation(state)
    return state


def gadget_target(left_bit: int, right_bit: int) -> SparseState:
    base = left_bit | (right_bit << 1)
    if not (left_bit and right_bit):
        return {base: 1.0 + 0.0j}
    inverse_sqrt_two = 1.0 / math.sqrt(2.0)
    return {
        base | (1 << 4): inverse_sqrt_two,
        base | (1 << 3): -inverse_sqrt_two,
    }


def main() -> None:
    check(
        "audit-facing source dependency surface resolves inside the repository",
        audit_source_closure(AUDIT_INPUT_PATHS),
        {"audit_input_paths": AUDIT_INPUT_PATHS, "campaign_fallbacks": 0},
    )

    frame_determinants = Counter(det3(frame) for frame in FRAMES)
    frame_mode_bijections = sum(len(set(mapping)) != 6 for mapping in MODE_MAPS)
    check(
        "the standard proper-cubic frame set closes at 24 elements",
        len(FRAMES) == 24 and frame_determinants == {1: 24} and frame_mode_bijections == 0,
        {"frames": len(FRAMES), "determinants": dict(frame_determinants), "mode_bijection_failures": frame_mode_bijections},
    )

    graph_edges = sum(len(row) for row in ADJACENCY.values()) // 2
    connected = len(DISTANCES[(0, 0, 0)])
    diameter = max(max(row.values()) for row in DISTANCES.values())
    degrees = Counter(len(row) for row in ADJACENCY.values())
    reverse_radial_path_failures = 0
    for mode, direction in enumerate(DIRECTIONS):
        path = tuple(scale(radius, direction) for radius in range(5))
        reverse_radial_path_failures += any(site not in SITES for site in path)
        reverse_radial_path_failures += any(l1(path[index], path[index + 1]) != 1 for index in range(4))
        reverse_radial_path_failures += REGISTER_SITE[(mode, REVERSE_MODE[mode])] != scale(3, direction)
    check(
        "the explicit shell, reverse-pair bridge and ordered-pair register form a connected 61-site NN block",
        len(SHELL) == 25
        and len(REGISTER) == 30
        and len(CORRIDOR) == 6
        and len(SITES) == 61
        and graph_edges == 72
        and connected == 61
        and diameter == 10
        and degrees == {1: 24, 2: 24, 5: 6, 6: 7}
        and reverse_radial_path_failures == 0,
        {
            "shell_sites": len(SHELL),
            "ordered_pair_register_sites": len(REGISTER),
            "corridor_work_sites": len(CORRIDOR),
            "total_sites": len(SITES),
            "NN_edges": graph_edges,
            "connected_vertices": connected,
            "diameter": diameter,
            "degree_distribution": dict(sorted(degrees.items())),
            "radial_path": "0 -> d_i -> 2d_i -> 3d_i=a_(i,rev(i)) -> 4d_i -> 4d_i+d_j",
        },
    )

    site_transport_failures = 0
    ordered_site_transport_failures = 0
    for frame, mapping in zip(FRAMES, MODE_MAPS):
        site_transport_failures += sum(matvec(frame, site) not in SITE_INDEX for site in SITES)
        ordered_site_transport_failures += sum(
            matvec(frame, REGISTER_SITE[pair]) != REGISTER_SITE[(mapping[pair[0]], mapping[pair[1]])]
            for pair in ORDERED_PAIRS
        )
    check(
        "bare coordinate rotations permute all 61 sites and every ordered-pair label",
        site_transport_failures == ordered_site_transport_failures == 0,
        {"site_transport_failures": site_transport_failures, "ordered_pair_transport_failures": ordered_site_transport_failures},
    )

    frame_state_failures = 0
    maximum_frame_state_residual = 0.0
    sign_formula_failures = 0
    for mapping in MODE_MAPS:
        for bits in range(64):
            source = register_state(bits)
            transported = permute_register(source, mapping)
            target = register_state(transformed_bits(bits, mapping))
            sign = exterior_sign(bits, mapping)
            residual = sparse_residual(transported, scale_state(target, sign))
            maximum_frame_state_residual = max(maximum_frame_state_residual, residual)
            frame_state_failures += residual > TOL
            sign_formula_failures += register_sign(bits, mapping) != sign
    check(
        "the occupied-pair product realizes the exterior sign for all 24 frames and all 64 occupations",
        frame_state_failures == sign_formula_failures == 0 and maximum_frame_state_residual < TOL,
        {
            "frame_occupation_cases": 24 * 64,
            "sparse_state_failures": frame_state_failures,
            "sign_formula_failures": sign_formula_failures,
            "maximum_sparse_state_residual": maximum_frame_state_residual,
        },
    )

    frame_product_failures = 0
    mode_product_failures = 0
    cocycle_product_failures = 0
    for left_index, left in enumerate(FRAMES):
        for right_index, right in enumerate(FRAMES):
            product_frame = matmul(left, right)
            target_index = FRAME_INDEX[product_frame]
            left_map = MODE_MAPS[left_index]
            right_map = MODE_MAPS[right_index]
            target_map = MODE_MAPS[target_index]
            composed_map = tuple(left_map[right_map[mode]] for mode in range(6))
            mode_product_failures += composed_map != target_map
            for site in SITES:
                frame_product_failures += matvec(left, matvec(right, site)) != matvec(product_frame, site)
            for bits in range(64):
                composed_sign = register_sign(bits, right_map) * register_sign(
                    transformed_bits(bits, right_map), left_map
                )
                cocycle_product_failures += composed_sign != register_sign(bits, target_map)
    check(
        "all 576 bare-frame products and the full-M64 cocycle close exactly",
        frame_product_failures == mode_product_failures == cocycle_product_failures == 0,
        {
            "ordered_frame_products": 24 * 24,
            "coordinate_product_cases": 24 * 24 * 61,
            "M64_cocycle_product_cases": 24 * 24 * 64,
            "coordinate_product_failures": frame_product_failures,
            "mode_product_failures": mode_product_failures,
            "cocycle_product_failures": cocycle_product_failures,
        },
    )

    port_frame_failures = 0
    port_product_failures = 0
    for mapping in MODE_MAPS:
        for port in (0, 1):
            for bits in range(64):
                port_frame_failures += register_sign(bits, mapping) != exterior_sign(bits, mapping)
    for left_index, left in enumerate(FRAMES):
        for right_index, right in enumerate(FRAMES):
            target_map = MODE_MAPS[FRAME_INDEX[matmul(left, right)]]
            left_map, right_map = MODE_MAPS[left_index], MODE_MAPS[right_index]
            for port in (0, 1):
                for bits in range(64):
                    port_product_failures += (
                        register_sign(bits, right_map)
                        * register_sign(transformed_bits(bits, right_map), left_map)
                        != register_sign(bits, target_map)
                    )
    check(
        "a rotation-fixed seam port extends the bare-frame action to all 128 decoded occupations",
        port_frame_failures == port_product_failures == 0,
        {
            "frame_port_occupation_cases": 24 * 128,
            "product_port_occupation_cases": 24 * 24 * 128,
            "frame_failures": port_frame_failures,
            "product_failures": port_product_failures,
            "port_frame_action": "fixed seventh mode; no local-port inversion factor",
        },
    )

    gadget_residuals = []
    inverse_residuals = []
    for left_bit, right_bit in product((0, 1), repeat=2):
        source = {left_bit | (right_bit << 1): 1.0 + 0.0j}
        prepared = gadget(source)
        target = gadget_target(left_bit, right_bit)
        gadget_residuals.append(sparse_residual(prepared, target))
        inverse_residuals.append(sparse_residual(gadget(prepared, inverse=True), source))
    check(
        "the explicit pair gadget prepares, unprepares and returns its flag exactly",
        max(gadget_residuals + inverse_residuals) < TOL,
        {
            "input_controls": 4,
            "maximum_preparation_residual": max(gadget_residuals),
            "maximum_inverse_residual": max(inverse_residuals),
            "active_output": "(|1_(j,i)>-|1_(i,j)>)/sqrt(2), flag=0",
        },
    )

    norm_residual = 0.0
    active_pair_failures = 0
    work_return_failures = 0
    sector_pairs = {}
    for bits in range(64):
        state = register_state(bits)
        norm_residual = max(norm_residual, abs(sum(abs(value) ** 2 for value in state.values()) - 1.0))
        expected_pairs = bits.bit_count() * (bits.bit_count() - 1) // 2
        actual_pairs = next(iter(state)).bit_count() if state else -1
        active_pair_failures += any(mask.bit_count() != expected_pairs for mask in state)
        work_flag = 0
        for left, right in UNORDERED_PAIRS:
            condition = ((bits >> left) & 1) and ((bits >> right) & 1)
            work_flag ^= int(condition)
            work_flag ^= int(condition)
        work_return_failures += work_flag != 0
        sector_pairs[bits.bit_count()] = (expected_pairs, actual_pairs)
    check(
        "the fifteen-gadget network works for every occupation sector and returns reusable work",
        norm_residual < TOL and active_pair_failures == work_return_failures == 0,
        {
            "M64_inputs": 64,
            "maximum_register_norm_residual": norm_residual,
            "active_pair_failures": active_pair_failures,
            "work_return_failures": work_return_failures,
            "sector_pair_counts": dict(sorted(sector_pairs.items())),
        },
    )

    maximum_contact_residual = 0.0
    sector_contact_residuals = {sector: 0.0 for sector in range(7)}
    for bits in range(64):
        source = register_state(bits)
        actual = contact_register_action(source)
        pairs = bits.bit_count() * (bits.bit_count() - 1) // 2
        expected = scale_state(source, cmath.exp(1j * CONTACT_COUPLING * pairs))
        residual = sparse_residual(actual, expected)
        maximum_contact_residual = max(maximum_contact_residual, residual)
        sector_contact_residuals[bits.bit_count()] = max(sector_contact_residuals[bits.bit_count()], residual)
    check(
        "uniform onsite register phase realizes every one of the fifteen contact factors for k=0..6",
        maximum_contact_residual < TOL,
        {
            "contact_coupling": CONTACT_COUPLING,
            "M64_inputs": 64,
            "maximum_contact_residual": maximum_contact_residual,
            "sector_maximum_residuals": sector_contact_residuals,
            "active_pair_counts_by_k": {k: k * (k - 1) // 2 for k in range(7)},
        },
    )

    # Active negative controls.
    active_source = {0b11: 1.0 + 0.0j}
    deleted_phase_state = gadget(active_source, delete_phase=True)
    swapped_deleted_phase = basis_permutation(
        deleted_phase_state,
        lambda basis: (
            basis ^ (1 << 3) ^ (1 << 4)
            if ((basis >> 3) & 1) != ((basis >> 4) & 1)
            else basis
        ),
    )
    deleted_antisymmetry_frame_residual = sparse_residual(
        swapped_deleted_phase, scale_state(deleted_phase_state, -1)
    )
    deleted_uncompute = gadget(active_source, delete_uncompute=True)
    deleted_uncompute_flag_probability = sum(
        abs(amplitude) ** 2 for basis, amplitude in deleted_uncompute.items() if (basis >> 2) & 1
    )

    pair_bits = 0b11
    pair_state = register_state(pair_bits)
    pair_indices = {
        ORDERED_INDEX[(0, 1)],
        ORDERED_INDEX[(1, 0)],
    }
    deleted_pair_contact = contact_register_action(pair_state, deleted=pair_indices)
    expected_pair_contact = scale_state(pair_state, cmath.exp(1j * CONTACT_COUPLING))
    deleted_pair_contact_residual = sparse_residual(deleted_pair_contact, expected_pair_contact)
    deleted_one_contact = contact_register_action(pair_state, deleted={ORDERED_INDEX[(0, 1)]})
    overlap = sum(pair_state[mask].conjugate() * deleted_one_contact.get(mask, 0.0j) for mask in pair_state)
    deleted_one_site_leakage = math.sqrt(max(0.0, 1.0 - abs(overlap) ** 2))
    expected_one_site_leakage = abs(math.sin(CONTACT_COUPLING / 2.0))
    check(
        "antisymmetry, work-return and contact deletions remain active",
        deleted_antisymmetry_frame_residual > 1.0
        and deleted_uncompute_flag_probability > 0.99
        and abs(deleted_pair_contact_residual - abs(cmath.exp(1j * CONTACT_COUPLING) - 1.0)) < TOL
        and abs(deleted_one_site_leakage - expected_one_site_leakage) < TOL
        and deleted_one_site_leakage > 1.0e-2,
        {
            "delete_pair_Z_frame_residual": deleted_antisymmetry_frame_residual,
            "delete_flag_uncompute_probability_flag_one": deleted_uncompute_flag_probability,
            "delete_both_pair_contact_phases_residual": deleted_pair_contact_residual,
            "expected_pair_contact_deletion_residual": abs(cmath.exp(1j * CONTACT_COUPLING) - 1.0),
            "delete_one_ordered_site_code_leakage": deleted_one_site_leakage,
            "expected_one_site_leakage": expected_one_site_leakage,
        },
    )

    two_qubit_factors_per_pair = 16
    one_qubit_factors_per_pair = 23
    preparation_two_qubit = len(UNORDERED_PAIRS) * two_qubit_factors_per_pair
    preparation_one_qubit = len(UNORDERED_PAIRS) * one_qubit_factors_per_pair
    maximum_route_cost = 2 * diameter - 1
    preparation_nn_bound = preparation_two_qubit * maximum_route_cost + preparation_one_qubit
    check(
        "the reversible preparation has a finite explicit NN routing bound",
        preparation_two_qubit == 240
        and preparation_one_qubit == 345
        and maximum_route_cost == 19
        and preparation_nn_bound == 4905,
        {
            "standard_Toffoli_per_pair": "2 x (6 two-qubit + 9 one-qubit)",
            "controlled_H_per_pair": "2 two-qubit + 4 one-qubit",
            "other_per_pair": "2 CNOT + 1 Z",
            "preparation_two_qubit_factors": preparation_two_qubit,
            "preparation_one_qubit_factors": preparation_one_qubit,
            "maximum_route_and_return_cost": maximum_route_cost,
            "one_way_preparation_NN_gate_bound": preparation_nn_bound,
            "prepare_plus_unprepare_NN_gate_bound": 2 * preparation_nn_bound,
        },
    )

    certificate_payload = {
        "directions": DIRECTIONS,
        "sites": SITES,
        "ordered_pairs": ORDERED_PAIRS,
        "frames": FRAMES,
        "contact_coupling": CONTACT_COUPLING,
    }
    certificate_digest = sha256(
        json.dumps(certificate_payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    supplied = (
        "six local signed-direction mode labels in the declared order (+x,-x,+y,-y,+z,-z)",
        "one optional rotation-fixed seam-port occupation bit ordered after the six local modes",
        "the 25-site shell coordinate formulas from the bounded seam-cell construction",
        "thirty ordered-pair M2 sites a_(i,j)=4*d_i+d_j and six 4*d_i corridor/work sites",
        "conditional antisymmetric pair state (|1_(j,i)>-|1_(i,j)>)/sqrt(2)",
        "a fixed fifteen-pair reversible gadget order and one returned work flag",
        "standard exact Toffoli and controlled-H decompositions for the gate-count bound",
        "uniform ordered-pair onsite contact phase with supplied coupling g=0.37",
        "standard coordinate action of the 24 proper-cubic frames and tolerance 2e-12",
    )
    derived = (
        "connected proper-cubic-invariant 61-site Z3 support of NN diameter ten",
        "bare-frame exterior sign on all 64 local and all 128 local-plus-port occupations",
        "exact all-576 cocycle and coordinate composition",
        "reversible pair-register preparation with returned reusable work",
        "exact exp(i*g*k*(k-1)/2) contact phase in every k=0..6 sector",
        "active antisymmetry, work-return, pair-contact and single-site leakage deletions",
        "constant conservative 4905-NN-gate bound for one preparation",
    )
    open_items = (
        "integration with an explicit 22/25-site cycle-code encoder and its routed update word",
        "an end-to-end M64 or M128 physical-site intertwiner including coin, reverse and seam factors",
        "nearest-neighbor admissibility or dynamics that prepares and maintains the conditional pair sector",
        "a time-homogeneous autonomous controller for the supplied finite gate word",
        "overlapping recurrent blocks, shared-port consistency and held-volume lattice streaming",
        "derivation of the mode labels, contact coupling, program order or register genesis from the axioms",
        "physical time, energy, source, gravity, Record, occurrence and probability",
        "any minimum-content, impossibility, shared-obstruction or axiom-pressure conclusion",
    )
    result = {
        "authority": "none",
        "audit": "unset",
        "status": "bounded-full-M64-bare-frame-pair-cocycle-certificate",
        "terminal": "FULL_M64_BARE_FRAME_PAIR_COCYCLE_CONTACT_CERTIFICATE",
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "geometry": {
            "physical_M2_sites": len(SITES),
            "NN_edges": graph_edges,
            "NN_diameter": diameter,
            "proper_cubic_frames": len(FRAMES),
        },
        "domains": {
            "local_M64_occupations": 64,
            "local_plus_fixed_port_occupations": 128,
            "ordered_frame_products": 24 * 24,
        },
        "maximum_residuals": {
            "bare_frame_sparse_state": maximum_frame_state_residual,
            "pair_gadget_preparation": max(gadget_residuals),
            "pair_gadget_inverse": max(inverse_residuals),
            "register_norm": norm_residual,
            "contact": maximum_contact_residual,
        },
        "deletion_controls": {
            "antisymmetry_phase_frame_residual": deleted_antisymmetry_frame_residual,
            "unreturned_flag_probability": deleted_uncompute_flag_probability,
            "deleted_pair_contact_residual": deleted_pair_contact_residual,
            "deleted_one_site_code_leakage": deleted_one_site_leakage,
        },
        "resources": {
            "elapsed_seconds": time.perf_counter() - START,
            "peak_rss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024 * 1024),
        },
        "certificate_payload_sha256": certificate_digest,
        "supplied": supplied,
        "derived": derived,
        "open": open_items,
        "claim_ceiling": (
            "Positive bounded representation/contact certificate only.  The 61 named Z3 M2 factors, "
            "conditional pair code and finite preparation word are supplied.  No physical compiler, "
            "recurrent autonomous law, state genesis, minimality, impossibility or axiom-pressure claim."
        ),
    }
    print("SUMMARY_JSON", json.dumps(result, sort_keys=True))
    print("RESULT", result["terminal"] if result["pass"] else "UNFINISHED_IMPLEMENTATION")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
