#!/usr/bin/env python3

"""Block31: conditional mathematics with a bounded current entrypoint.
Complete historical sources/controllers and results are archived outside note discovery.
Only the named checks below are fresh execution claims.
"""

from __future__ import annotations

import hashlib

import itertools

import math

import sys

from collections import Counter

from dataclasses import dataclass, replace

from pathlib import Path

import numpy as np

import sympy as sp

import admissibility_d4_prior_record_live_preparation_two_event_prefix_2026_08_30 as block23  # noqa: E402

import admissibility_d4_self_delimiting_forward_record_append_history_2026_08_30 as block24  # noqa: E402

import admissibility_d4_returned_tip_strict_support_analytic_coupling_gate_2026_08_30 as block28  # noqa: E402

import admissibility_d4_output_conditioned_pair_successor_handoff_gate_2026_08_31 as block30  # noqa: E402

Coord = tuple[int, int, int]

ZERO: Coord = (0, 0, 0)

E1: Coord = (1, 0, 0)

DIRECTIONS = block23.DIRECTIONS

ROTATIONS = block23.ROTATIONS

CANONICAL_LEFT = block28.Y_LEFT

CANONICAL_FRONT = block28.F_LEFT

LAMBDAS = (sp.S.Zero, sp.Rational(1, 2))

def add(*vectors: Coord) -> Coord:
    return tuple(sum(values) for values in zip(*vectors))

def scale(number: int, vector: Coord) -> Coord:
    return tuple(number * value for value in vector)

def negate(vector: Coord) -> Coord:
    return scale(-1, vector)

def dot(left: Coord, right: Coord) -> int:
    return sum(a * b for a, b in zip(left, right))

def cross(left: Coord, right: Coord) -> Coord:
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )

def l1(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))

def lateral(front: Coord) -> tuple[Coord, ...]:
    return tuple(direction for direction in DIRECTIONS if dot(front, direction) == 0)

def rho(front: Coord, direction: Coord) -> Coord:
    return cross(front, direction)

def rotate(rotation, vector: Coord) -> Coord:
    return block23.mat_vec(rotation, vector)

@dataclass(frozen=True)
class Gate:
    kind: str
    sites: tuple[Coord, ...]

Layer = tuple[Gate, ...]

RELATIONS = ("equal", "opposite", "perp_plus", "perp_minus")

def right_direction(front: Coord, direction: Coord, relation: str) -> Coord:
    if relation == "equal":
        return direction
    if relation == "opposite":
        return negate(direction)
    if relation == "perp_plus":
        return rho(front, direction)
    if relation == "perp_minus":
        return negate(rho(front, direction))
    raise ValueError(relation)

def sample_site(left: Coord, front: Coord, side: str, direction: Coord) -> Coord:
    right = add(left, scale(9, front))
    return add(left if side == "left" else right, scale(5, direction))

def radial_site(
    left: Coord,
    front: Coord,
    side: str,
    direction: Coord,
    index: int,
    mutation: str | None = None,
) -> Coord:
    right = add(left, scale(9, front))
    site = add(
        left if side == "left" else right,
        front if side == "left" else negate(front),
        scale(index, direction),
    )
    if (
        mutation == "alias_rail"
        and side == "right"
        and direction == lateral(front)[0]
        and index == 5
    ):
        site = radial_site(left, front, "left", direction, index)
    return site

def axial_site(left: Coord, front: Coord, direction: Coord, index: int) -> Coord:
    return add(left, scale(index, front), direction)

def relay_layers(
    left: Coord, front: Coord, mutation: str | None = None
) -> tuple[Layer, ...]:
    copy_layer = []
    for side, direction in itertools.product(("left", "right"), lateral(front)):
        source = sample_site(left, front, side, direction)
        if (
            mutation == "wrong_sample"
            and side == "left"
            and direction == lateral(front)[0]
        ):
            source = add(source, front)
        target = radial_site(left, front, side, direction, 5, mutation)
        sites = (source, target)
        if (
            mutation == "overwrite_sample"
            and side == "left"
            and direction == lateral(front)[0]
        ):
            sites = tuple(reversed(sites))
        copy_layer.append(Gate("CNOT", sites))
    layers: list[Layer] = [tuple(copy_layer)]
    for index in (5, 4, 3, 2):
        layers.append(tuple(
            Gate(
                "SWAP",
                (
                    radial_site(left, front, side, direction, index, mutation),
                    radial_site(left, front, side, direction, index - 1, mutation),
                ),
            )
            for side, direction in itertools.product(
                ("left", "right"), lateral(front)
            )
        ))
    for index in (1, 2, 3):
        layer = []
        for direction in lateral(front):
            layer.append(Gate(
                "SWAP",
                (
                    axial_site(left, front, direction, index),
                    axial_site(left, front, direction, index + 1),
                ),
            ))
            layer.append(Gate(
                "SWAP",
                (
                    axial_site(left, front, direction, 9 - index),
                    axial_site(left, front, direction, 8 - index),
                ),
            ))
        layers.append(tuple(layer))
    if mutation == "delete_relay_swap":
        layers[5] = layers[5][1:]
    return tuple(layers)

def relation_path(
    left: Coord, front: Coord, direction: Coord, relation: str
) -> tuple[Coord, ...]:
    f = front
    d = direction
    r = rho(f, d)
    if relation == "equal":
        relative = (
            add(scale(4, f), d),
            add(scale(4, f), scale(2, d)),
            add(scale(5, f), scale(2, d)),
            add(scale(5, f), d),
        )
    elif relation == "perp_plus":
        relative = (
            add(scale(4, f), d),
            add(scale(4, f), scale(2, d)),
            add(scale(5, f), scale(2, d)),
            add(scale(5, f), scale(2, d), r),
            add(scale(5, f), d, r),
            add(scale(5, f), r),
        )
    elif relation == "opposite":
        relative = (
            add(scale(4, f), d),
            add(scale(4, f), scale(2, d)),
            add(scale(4, f), scale(2, d), negate(r)),
            add(scale(4, f), d, negate(r)),
            add(scale(4, f), d, scale(-2, r)),
            add(scale(5, f), d, scale(-2, r)),
            add(scale(5, f), scale(-2, r)),
            add(scale(5, f), negate(d), scale(-2, r)),
            add(scale(5, f), negate(d), negate(r)),
            add(scale(5, f), negate(d)),
        )
    elif relation == "perp_minus":
        relative = (
            add(scale(4, f), d),
            add(scale(4, f), scale(2, d)),
            add(scale(5, f), scale(2, d)),
            add(scale(5, f), scale(2, d), negate(r)),
            add(scale(5, f), d, negate(r)),
            add(scale(5, f), negate(r)),
        )
    else:
        raise ValueError(relation)
    return tuple(add(left, site) for site in relative)

def token_cell(
    left: Coord,
    front: Coord,
    direction: Coord,
    relation: str,
    mutation: str | None = None,
) -> Coord:
    target = add(left, scale(4, front), scale(2, direction))
    if relation == "equal":
        cell = add(target, direction)
    elif relation == "opposite":
        cell = add(target, negate(front))
    elif relation == "perp_plus":
        cell = add(target, rho(front, direction))
    elif relation == "perp_minus":
        cell = add(target, negate(rho(front, direction)))
    else:
        raise ValueError(relation)
    if (
        mutation == "coordinate_mark"
        and front == E1
        and direction == lateral(front)[0]
        and relation == "equal"
    ):
        cell = add(cell, E1)
    if mutation == "swap_equal_opposite" and relation == "equal":
        cell = add(target, negate(front))
    if mutation == "collapse_perpendicular" and relation == "perp_minus":
        cell = add(target, rho(front, direction))
    return cell

def relation_layers(
    left: Coord,
    front: Coord,
    relation: str,
    mutation: str | None = None,
) -> tuple[Layer, ...]:
    paths = {
        direction: relation_path(left, front, direction, relation)
        for direction in lateral(front)
    }
    length = len(next(iter(paths.values()))) - 1
    layers: list[Layer] = []
    for index in range(length, 2, -1):
        layers.append(tuple(
            Gate("SWAP", (path[index - 1], path[index]))
            for path in paths.values()
        ))
    triples = tuple(
        Gate("TOFFOLI", (path[0], path[2], path[1]))
        for path in paths.values()
    )
    layers.append(triples)
    layers.append(tuple(
        Gate(
            "CNOT",
            (
                path[1],
                token_cell(left, front, direction, relation, mutation),
            ),
        )
        for direction, path in paths.items()
    ))
    if not (mutation == "omit_uncompute" and relation == "equal"):
        layers.append(triples)
    for index in range(3, length + 1):
        layers.append(tuple(
            Gate("SWAP", (path[index - 1], path[index]))
            for path in paths.values()
        ))
    return tuple(layers)

def macro_layers(
    left: Coord = CANONICAL_LEFT,
    front: Coord = CANONICAL_FRONT,
    mutation: str | None = None,
) -> tuple[Layer, ...]:
    forward = relay_layers(left, front, mutation)
    hub = tuple(
        layer
        for relation in RELATIONS
        for layer in relation_layers(left, front, relation, mutation)
    )
    reverse = () if mutation == "missing_reverse" else tuple(reversed(forward))
    return forward + hub + reverse

def gate_census(layers: tuple[Layer, ...]) -> Counter:
    return Counter(gate.kind for layer in layers for gate in layer)

def layers_have_disjoint_support(layers: tuple[Layer, ...]) -> bool:
    return all(
        len(tuple(site for gate in layer for site in gate.sites))
        == len(set(site for gate in layer for site in gate.sites))
        for layer in layers
    )

def macro_locality_certificate(layers: tuple[Layer, ...]) -> bool:
    for layer in layers:
        for gate in layer:
            if gate.kind in ("SWAP", "CNOT"):
                if len(gate.sites) != 2 or l1(*gate.sites) != 1:
                    return False
            elif gate.kind == "TOFFOLI":
                control_a, control_b, target = gate.sites
                if not (
                    len(set(gate.sites)) == 3
                    and l1(control_a, target) == 1
                    and l1(control_b, target) == 1
                    and l1(control_a, control_b) == 2
                ):
                    return False
            else:
                return False
    return True

def true_sample_sites(left: Coord, front: Coord) -> frozenset[Coord]:
    return frozenset(
        sample_site(left, front, side, direction)
        for side, direction in itertools.product(("left", "right"), lateral(front))
    )

def class_cells(
    left: Coord, front: Coord, mutation: str | None = None
) -> frozenset[Coord]:
    return frozenset(
        token_cell(left, front, direction, relation, mutation)
        for relation, direction in itertools.product(RELATIONS, lateral(front))
    )

def clean_sites(left: Coord, front: Coord) -> frozenset[Coord]:
    seeds = {
        radial_site(left, front, side, direction, 5)
        for side, direction in itertools.product(("left", "right"), lateral(front))
    }
    conjunction = {
        relation_path(left, front, direction, relation)[1]
        for relation, direction in itertools.product(RELATIONS, lateral(front))
    }
    return frozenset(seeds | conjunction | set(class_cells(left, front)))

def work_sites(
    left: Coord, front: Coord, mutation: str | None = None
) -> frozenset[Coord]:
    touched = {
        site
        for layer in macro_layers(left, front, mutation)
        for gate in layer
        for site in gate.sites
    }
    return frozenset(touched - set(true_sample_sites(left, front)))

def protected_sites(left: Coord, front: Coord) -> frozenset[Coord]:
    right = add(left, scale(9, front))
    centers = (left, right) + tuple(
        add(anchor, scale(9, direction))
        for anchor in (left, right)
        for direction in lateral(front)
    )
    return frozenset(
        add(center, site) for center in centers for site in block23.SUPPORT
    )

def carrier_certificate(mutation: str | None = None) -> bool:
    left, front = CANONICAL_LEFT, CANONICAL_FRONT
    work = work_sites(left, front, mutation)
    clean = clean_sites(left, front)
    borrowed = work - clean
    samples = true_sample_sites(left, front)
    protected = protected_sites(left, front)
    if mutation == "missing_clean_seed":
        clean = clean - {radial_site(left, front, "left", lateral(front)[0], 5)}
    if mutation == "missing_clean_target":
        clean = clean - {relation_path(left, front, lateral(front)[0], "equal")[1]}
    if mutation == "missing_clean_token":
        clean = clean - {token_cell(left, front, lateral(front)[0], "equal")}
    return (
        len(samples) == 8
        and samples.issubset(protected)
        and len(work) == 104
        and work.isdisjoint(protected)
        and len(clean) == 28
        and clean.issubset(work)
        and len(borrowed) == 76
        and len(class_cells(left, front)) == 16
    )

Monomial = frozenset[str]

Polynomial = frozenset[Monomial]

PZERO: Polynomial = frozenset()

def variable(name: str) -> Polynomial:
    return frozenset((frozenset((name,)),))

def poly_xor(left: Polynomial, right: Polynomial) -> Polynomial:
    return left.symmetric_difference(right)

def poly_and(left: Polynomial, right: Polynomial) -> Polynomial:
    output: set[Monomial] = set()
    for a in left:
        for b in right:
            product = a | b
            if product in output:
                output.remove(product)
            else:
                output.add(product)
    return frozenset(output)

def direction_name(direction: Coord) -> str:
    return "".join(str(value).replace("-", "m") for value in direction)

def sample_variable(side: str, direction: Coord) -> Polynomial:
    return variable(f"{side}:{direction_name(direction)}")

def sample_name(side: str, direction: Coord) -> str:
    return f"{side}:{direction_name(direction)}"

def borrowed_variable(site: Coord) -> Polynomial:
    return variable(f"w:{site[0]},{site[1]},{site[2]}")

def apply_macro_gate(state: dict[Coord, Polynomial], gate: Gate) -> None:
    if gate.kind == "SWAP":
        left, right = gate.sites
        state[left], state[right] = state[right], state[left]
    elif gate.kind == "CNOT":
        control, target = gate.sites
        state[target] = poly_xor(state[target], state[control])
    elif gate.kind == "TOFFOLI":
        control_a, control_b, target = gate.sites
        state[target] = poly_xor(
            state[target], poly_and(state[control_a], state[control_b])
        )
    else:
        raise ValueError(gate.kind)

def symbolic_state(
    left: Coord, front: Coord, mutation: str | None = None
) -> tuple[dict[Coord, Polynomial], dict[Coord, Polynomial]]:
    layers = macro_layers(left, front, mutation)
    touched = {site for layer in layers for gate in layer for site in gate.sites}
    samples = true_sample_sites(left, front)
    clean = clean_sites(left, front)
    initial = {}
    for site in touched | set(samples) | set(clean):
        if site in samples:
            side = "L" if any(
                site == sample_site(left, front, "left", direction)
                for direction in lateral(front)
            ) else "R"
            physical_side = "left" if side == "L" else "right"
            direction = next(
                direction
                for direction in lateral(front)
                if site == sample_site(left, front, physical_side, direction)
            )
            initial[site] = sample_variable(side, direction)
        elif site in clean:
            initial[site] = PZERO
        else:
            initial[site] = borrowed_variable(site)
    state = dict(initial)
    for layer in layers:
        for gate in layer:
            apply_macro_gate(state, gate)
    return initial, state

def expected_token_polynomials(left: Coord, front: Coord) -> dict[Coord, Polynomial]:
    return {
        token_cell(left, front, direction, relation): poly_and(
            sample_variable("L", direction),
            sample_variable("R", right_direction(front, direction, relation)),
        )
        for relation, direction in itertools.product(RELATIONS, lateral(front))
    }

def symbolic_circuit_certificate(mutation: str | None = None) -> bool:
    left, front = CANONICAL_LEFT, CANONICAL_FRONT
    initial, final = symbolic_state(left, front, mutation)
    expected_tokens = expected_token_polynomials(left, front)
    canonical_classes = class_cells(left, front)
    for site, value in initial.items():
        expected = expected_tokens[site] if site in canonical_classes else value
        if final.get(site, PZERO) != expected:
            return False
    return all(
        final.get(site, PZERO) == polynomial
        for site, polynomial in expected_tokens.items()
    )

def evaluate(polynomial: Polynomial, assignment: dict[str, int]) -> int:
    value = 0
    for monomial in polynomial:
        term = 1
        for name in monomial:
            term &= assignment[name]
        value ^= term
    return value

def exhaustive_truth_certificate() -> dict[str, object]:
    left, front = CANONICAL_LEFT, CANONICAL_FRONT
    _initial, final = symbolic_state(left, front)
    token_labels = {
        token_cell(left, front, direction, relation): (
            relation,
            direction,
            right_direction(front, direction, relation),
        )
        for relation, direction in itertools.product(RELATIONS, lateral(front))
    }
    valid_rows = 0
    invalid_rows = 0
    invalid_raw_token_rows = 0
    failures = 0
    orbit_counts = Counter()
    for bits in itertools.product((0, 1), repeat=8):
        assignment = {}
        for index, direction in enumerate(lateral(front)):
            assignment[sample_name("L", direction)] = bits[index]
            assignment[sample_name("R", direction)] = bits[4 + index]
        active = [
            label
            for site, label in token_labels.items()
            if evaluate(final[site], assignment)
        ]
        one_left = sum(bits[:4]) == 1
        one_right = sum(bits[4:]) == 1
        if one_left and one_right:
            valid_rows += 1
            left_direction = lateral(front)[bits[:4].index(1)]
            right_value = lateral(front)[bits[4:].index(1)]
            if len(active) != 1 or active[0][1:] != (left_direction, right_value):
                failures += 1
            else:
                orbit_counts[active[0][0]] += 1
        else:
            invalid_rows += 1
            invalid_raw_token_rows += bool(active)
            # The semantic completion sends all these rows to STOP; the raw
            # reversible word is intentionally not called a STOP compiler.
    return {
        "valid_rows": valid_rows,
        "invalid_rows": invalid_rows,
        "invalid_raw_token_rows": invalid_raw_token_rows,
        "failures": failures,
        "orbit_counts": dict(orbit_counts),
    }

H = np.asarray(((1, 1), (1, -1)), dtype=complex) / math.sqrt(2)

T = np.diag((1, np.exp(1j * math.pi / 4))).astype(complex)

TDG = T.conj().T

SWAP_MATRIX = np.asarray(
    ((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, 1)),
    dtype=complex,
)

CNOT_MATRIX = np.asarray(
    ((1, 0, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0), (0, 1, 0, 0)),
    dtype=complex,
)

def primitive_toffoli_word(
    gate: Gate, mutation: str | None = None
) -> tuple[Gate, ...]:
    control_a, control_b, target = gate.sites
    word = (
        Gate("H", (target,)),
        Gate("CNOT", (control_b, target)),
        Gate("Tdg", (target,)),
        Gate("CNOT", (control_a, target)),
        Gate("T", (target,)),
        Gate("CNOT", (control_b, target)),
        Gate("Tdg", (target,)),
        Gate("CNOT", (control_a, target)),
        Gate("T", (control_b,)),
        Gate("T", (target,)),
        Gate("H", (target,)),
        Gate("SWAP", (control_a, target)),
        Gate("CNOT", (target, control_b)),
        Gate("SWAP", (control_a, target)),
        Gate("T", (control_a,)),
        Gate("Tdg", (control_b,)),
        Gate("SWAP", (control_a, target)),
        Gate("CNOT", (target, control_b)),
        Gate("SWAP", (control_a, target)),
    )
    if mutation == "delete_toffoli_CNOT":
        word = word[:1] + word[2:]
    return word

def primitive_layers(
    layers: tuple[Layer, ...], mutation: str | None = None
) -> tuple[Layer, ...]:
    output: list[Layer] = []
    for layer in layers:
        if any(gate.kind == "TOFFOLI" for gate in layer):
            if not all(gate.kind == "TOFFOLI" for gate in layer):
                raise ValueError("mixed Toffoli macro layer")
            words = tuple(
                primitive_toffoli_word(gate, mutation) for gate in layer
            )
            word_length = len(words[0])
            output.extend(
                tuple(word[index] for word in words)
                for index in range(word_length)
            )
        else:
            output.append(layer)
    return tuple(output)

def embed_gate(matrix: np.ndarray, wires: tuple[int, ...], count: int) -> np.ndarray:
    output = np.zeros((1 << count, 1 << count), dtype=complex)
    for source in range(1 << count):
        local_source = sum(
            ((source >> wire) & 1) << index for index, wire in enumerate(wires)
        )
        for local_target in range(1 << len(wires)):
            amplitude = matrix[local_target, local_source]
            if abs(amplitude) == 0:
                continue
            target = source
            for index, wire in enumerate(wires):
                bit = (local_target >> index) & 1
                target = target | (1 << wire) if bit else target & ~(1 << wire)
            output[target, source] += amplitude
    return output

def primitive_matrix(gate: Gate) -> np.ndarray:
    if gate.kind == "H":
        return H
    if gate.kind == "T":
        return T
    if gate.kind == "Tdg":
        return TDG
    if gate.kind == "SWAP":
        return SWAP_MATRIX
    if gate.kind == "CNOT":
        return CNOT_MATRIX
    raise ValueError(gate.kind)

def exact_toffoli_matrix() -> np.ndarray:
    output = np.zeros((8, 8), dtype=complex)
    for source in range(8):
        target = source
        if (source & 1) and (source & 2):
            target ^= 4
        output[target, source] = 1
    return output

def toffoli_expansion_certificate(mutation: str | None = None) -> bool:
    a, t, b = (0, 0, 0), (1, 0, 0), (2, 0, 0)
    word = primitive_toffoli_word(Gate("TOFFOLI", (a, b, t)), mutation)
    wires = {a: 0, b: 1, t: 2}
    matrix = np.eye(8, dtype=complex)
    for gate in word:
        local_wires = tuple(wires[site] for site in gate.sites)
        matrix = embed_gate(primitive_matrix(gate), local_wires, 3) @ matrix
    return np.linalg.norm(matrix - exact_toffoli_matrix()) < 1.0e-12

def primitive_certificate(mutation: str | None = None) -> bool:
    macro = macro_layers()
    primitive = primitive_layers(macro, mutation)
    census = gate_census(primitive)
    return (
        len(macro) == 56
        and sum(map(len, macro)) == 288
        and gate_census(macro) == Counter({
            "SWAP": 224,
            "TOFFOLI": 32,
            "CNOT": 32,
        })
        and len(primitive) == 200
        and sum(map(len, primitive)) == 864
        and census == Counter({
            "SWAP": 352,
            "H": 64,
            "CNOT": 224,
            "T": 128,
            "Tdg": 96,
        })
        and layers_have_disjoint_support(macro)
        and layers_have_disjoint_support(primitive)
        and macro_locality_certificate(macro)
        and all(
            len(gate.sites) == 1
            or (len(gate.sites) == 2 and l1(*gate.sites) == 1)
            for layer in primitive
            for gate in layer
        )
        and toffoli_expansion_certificate(mutation)
    )

def pointer_bit(word: tuple[int, ...], site: Coord) -> int:
    return word[block23.POINTER_ORDER.index(site)]

def reached_sector_sampling_certificate() -> bool:
    left, front = CANONICAL_LEFT, CANONICAL_FRONT
    right = add(left, scale(9, front))
    outcomes = block28.pair_record_outcomes()
    configurations = set()
    for outcome in outcomes:
        configuration = dict(outcome.pointer_configuration)
        configurations.add(outcome.pointer_configuration)
        left_bits = {}
        right_bits = {}
        for direction in lateral(front):
            left_center = add(left, scale(9, direction))
            right_center = add(right, scale(9, direction))
            inward = scale(-4, direction)
            left_bits[direction] = pointer_bit(configuration[left_center], inward)
            right_bits[direction] = pointer_bit(configuration[right_center], inward)
        if not (
            sum(left_bits.values()) == sum(right_bits.values()) == 1
            and left_bits[outcome.left_exit] == 1
            and right_bits[outcome.right_exit] == 1
        ):
            return False
    blank_zero = all(value == 0 for value in block23.BLANK_POINTER)
    locked_status = all(
        pointer_bit(block23.locked_word(front, outcome), status) == 1
        for front in DIRECTIONS
        for outcome in block23.OUTCOMES
        for status in block23.STATUS
    )
    orthogonal = all(
        block23.pure_overlap(
            block23.radial_bloch(site, left_bit),
            block23.radial_bloch(site, right_bit),
        )
        == int(left_bit == right_bit)
        for site in block23.STATUS
        for left_bit, right_bit in itertools.product((0, 1), repeat=2)
    )
    return (
        len(outcomes) == len(configurations) == 3136
        and blank_zero
        and locked_status
        and orthogonal
    )

def record_qnd_certificate(mutation: str | None = None) -> bool:
    layers = macro_layers(mutation=mutation)
    samples = true_sample_sites(CANONICAL_LEFT, CANONICAL_FRONT)
    touches = Counter()
    target_touches = Counter()
    for layer in layers:
        for gate in layer:
            for site in gate.sites:
                if site in samples:
                    touches[site] += 1
            if gate.kind == "CNOT" and gate.sites[1] in samples:
                target_touches[gate.sites[1]] += 1
    return (
        reached_sector_sampling_certificate()
        and set(touches) == set(samples)
        and set(touches.values()) == {2}
        and not target_touches
        and symbolic_circuit_certificate(mutation)
    )

def transform_layers(layers: tuple[Layer, ...], rotation, shift=ZERO):
    return tuple(
        frozenset(
            Gate(
                gate.kind,
                tuple(add(rotate(rotation, site), shift) for site in gate.sites),
            )
            for gate in layer
        )
        for layer in layers
    )

def layer_sets(layers: tuple[Layer, ...]):
    return tuple(frozenset(layer) for layer in layers)

def covariance_certificate(mutation: str | None = None) -> bool:
    left, front = CANONICAL_LEFT, CANONICAL_FRONT
    base = macro_layers(left, front, mutation)
    shift = (7, -11, 5)
    moved = macro_layers(add(left, shift), front, mutation)
    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    if layer_sets(moved) != transform_layers(base, identity, shift):
        return False
    for rotation in ROTATIONS:
        rotated = macro_layers(rotate(rotation, left), rotate(rotation, front), mutation)
        if layer_sets(rotated) != transform_layers(base, rotation):
            return False
    return True

def logical_side_exchange_certificate(mutation: str | None = None) -> bool:
    for front in DIRECTIONS:
        for direction, relation in itertools.product(lateral(front), RELATIONS):
            right = right_direction(front, direction, relation)
            exchanged_front = negate(front)
            exchanged_left = right
            exchanged_right = direction
            if mutation == "fail_to_swap_writers" and (
                front,
                direction,
                relation,
            ) == (E1, lateral(E1)[0], "equal"):
                exchanged_right = negate(direction)
            matches = tuple(
                candidate
                for candidate in RELATIONS
                if right_direction(
                    exchanged_front, exchanged_left, candidate
                ) == exchanged_right
            )
            if matches != (relation,):
                return False
            original = block30.route_plan(ZERO, front, direction, right, 1)
            exchanged = block30.route_plan(
                block24.forward_center(ZERO, front),
                exchanged_front,
                exchanged_left,
                exchanged_right,
                1,
            )
            if not (
                exchanged.left.steps == original.right.steps
                and exchanged.right.steps == original.left.steps
                and exchanged.left.targets == original.right.targets
                and exchanged.right.targets == original.left.targets
            ):
                return False
    return True

def token_order(front: Coord) -> tuple[tuple[str, Coord, Coord], ...]:
    return tuple(
        (relation, direction, right_direction(front, direction, relation))
        for relation, direction in itertools.product(RELATIONS, lateral(front))
    )

def raw_token_write(
    front: Coord,
    left_bits: tuple[int, ...],
    right_bits: tuple[int, ...],
    initial_tokens: tuple[int, ...],
) -> tuple[int, ...]:
    left_values = dict(zip(lateral(front), left_bits))
    right_values = dict(zip(lateral(front), right_bits))
    output = list(initial_tokens)
    for index, (_relation, direction, right) in enumerate(token_order(front)):
        output[index] ^= left_values[direction] & right_values[right]
    return tuple(output)

def simulate_macro_basis(
    left_bits: tuple[int, ...],
    right_bits: tuple[int, ...],
    initial_tokens: tuple[int, ...],
    identity_word: bool = False,
) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    left, front = CANONICAL_LEFT, CANONICAL_FRONT
    layers = macro_layers(left, front)
    touched = {site for layer in layers for gate in layer for site in gate.sites}
    state = {site: 0 for site in touched}
    for direction, bit in zip(lateral(front), left_bits):
        state[sample_site(left, front, "left", direction)] = bit
    for direction, bit in zip(lateral(front), right_bits):
        state[sample_site(left, front, "right", direction)] = bit
    cells = tuple(
        token_cell(left, front, direction, relation)
        for relation, direction in itertools.product(RELATIONS, lateral(front))
    )
    for cell, bit in zip(cells, initial_tokens):
        state[cell] = bit
    if not identity_word:
        for layer in layers:
            for gate in layer:
                if gate.kind == "SWAP":
                    first, second = gate.sites
                    state[first], state[second] = state[second], state[first]
                elif gate.kind == "CNOT":
                    control, target = gate.sites
                    state[target] ^= state[control]
                elif gate.kind == "TOFFOLI":
                    control_a, control_b, target = gate.sites
                    state[target] ^= state[control_a] & state[control_b]
                else:
                    raise ValueError(gate.kind)
    return (
        tuple(state[cell] for cell in cells),
        tuple(
            state[sample_site(left, front, "left", direction)]
            for direction in lateral(front)
        ),
        tuple(
            state[sample_site(left, front, "right", direction)]
            for direction in lateral(front)
        ),
    )

def semantic_totalization_specification_certificate(
    stop_present: bool = True,
    ready_guard: bool = True,
    accept_invalid: bool = False,
    xor_latch: bool = False,
    identity_word: bool = False,
) -> bool:
    p_valid, p_ready = sp.symbols("p_valid p_ready", commutative=True)
    active = p_valid * p_ready if ready_guard else p_valid

    def reduce_projectors(expression):
        return block23.projector_reduce(
            block23.projector_reduce(expression, p_valid), p_ready
        )

    stop = (
        reduce_projectors((1 - active) ** 2)
        if stop_present
        else sp.S.Zero
    )
    fire = reduce_projectors(active**2)
    gram = reduce_projectors(fire + stop)
    if gram != 1:
        return False

    ready = (0,) * 16
    for bits in itertools.product((0, 1), repeat=8):
        left_bits, right_bits = bits[:4], bits[4:]
        valid = sum(left_bits) == sum(right_bits) == 1
        raw_first, left_after, right_after = simulate_macro_basis(
            left_bits, right_bits, ready, identity_word
        )
        expected_first = raw_token_write(
            CANONICAL_FRONT, left_bits, right_bits, ready
        )
        if (
            raw_first != expected_first
            or left_after != left_bits
            or right_after != right_bits
        ):
            return False
        active_first = valid or accept_invalid
        first = raw_first if active_first else ready
        if valid:
            if sum(first) != 1:
                return False
            second_active = (
                valid
                and (not ready_guard or not any(first))
            )
            if xor_latch:
                second_active = True
            if second_active:
                second, left_second, right_second = simulate_macro_basis(
                    left_bits, right_bits, first, identity_word
                )
                if left_second != left_bits or right_second != right_bits:
                    return False
            else:
                second = first
            if second != first:
                return False
        elif first != ready:
            return False
    return True

def token_route_correspondence_certificate(mutation: str | None = None) -> bool:
    for front in DIRECTIONS:
        for direction, relation in itertools.product(lateral(front), RELATIONS):
            actual_right = right_direction(front, direction, relation)
            route_right = actual_right
            if mutation == "wrong_route" and (
                front,
                direction,
                relation,
            ) == (E1, lateral(E1)[0], "equal"):
                route_right = negate(route_right)
            if mutation == "swap_perpendicular_routes" and relation in (
                "perp_plus",
                "perp_minus",
            ):
                route_right = right_direction(
                    front,
                    direction,
                    "perp_minus" if relation == "perp_plus" else "perp_plus",
                )
            try:
                plan = block30.route_plan(
                    ZERO, front, direction, route_right, 1
                )
            except ValueError:
                return False
            expected_kind = (
                "equal"
                if relation == "equal"
                else "opposite"
                if relation == "opposite"
                else "orthogonal"
            )
            if not (
                route_right == actual_right
                and plan.kind == expected_kind
                and block30.route_plan_certificate(plan)
                and token_cell(ZERO, front, direction, relation)
                in class_cells(ZERO, front)
            ):
                return False
    signatures = tuple(
        block30.handoff_signature(
            lam,
            -1 if mutation == "lambda_dependent_route" and lam else 1,
        )
        for lam in LAMBDAS
    )
    return signatures[0] == signatures[1] and block30.common_law_pushforward_certificate()

def bounded_truth():
    return exhaustive_truth_certificate() == {'valid_rows':16,'invalid_rows':240,'invalid_raw_token_rows':209,'failures':0,'orbit_counts':{'equal':4,'opposite':4,'perp_plus':4,'perp_minus':4}}


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 30
# Literal inputs and hashes are frozen after all source/note edits.
AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_D4_OUTPUT_CONDITIONED_PAIR_SUCCESSOR_COMMON_TWO_USE_CYLINDER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md', 'docs/ADMISSIBILITY_D4_OUTPUT_STATUS_NN_ORDERED_PAIR_TRANSDUCER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md', 'docs/ADMISSIBILITY_D4_RETURNED_TIP_SUPPLIED_Q_CONDITIONAL_PAIR_INSTRUMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-30.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'scripts/admissibility_d4_output_conditioned_pair_successor_handoff_gate_2026_08_31.py', 'scripts/admissibility_d4_prior_record_live_preparation_two_event_prefix_2026_08_30.py', 'scripts/admissibility_d4_returned_tip_strict_support_analytic_coupling_gate_2026_08_30.py', 'scripts/admissibility_d4_self_delimiting_forward_record_append_history_2026_08_30.py')
DIRECT_HASHES = {'docs/ADMISSIBILITY_D4_OUTPUT_CONDITIONED_PAIR_SUCCESSOR_COMMON_TWO_USE_CYLINDER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md': '655f7bc858b859dd84580ed9eb446f74ecfb1cfb87bfd1d9a00cc2339b9c7e6b', 'docs/ADMISSIBILITY_D4_OUTPUT_STATUS_NN_ORDERED_PAIR_TRANSDUCER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md': '1e853ac20bfdd4fc9e13e07304ee5051cbe67eb9389606bbc3a3555a5be96d6a', 'docs/ADMISSIBILITY_D4_RETURNED_TIP_SUPPLIED_Q_CONDITIONAL_PAIR_INSTRUMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-30.md': '86913d27c2f428d8d510ea374541b017ac4daa380574fe3486756374e7112320', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'scripts/admissibility_d4_output_conditioned_pair_successor_handoff_gate_2026_08_31.py': '62721ae1b16c8b5bbbdc7cb5356513367997fbb6a1de1cb771348e172bdd20ba', 'scripts/admissibility_d4_prior_record_live_preparation_two_event_prefix_2026_08_30.py': 'a454b4ce47af92bbf55550ebae068ff4a419b141d916b0c4fcdc1678bf283a7e', 'scripts/admissibility_d4_returned_tip_strict_support_analytic_coupling_gate_2026_08_30.py': '54b5d7faac7d6bc3484619d09e30b4b8f27efc84677142a48a5fe24f995d105d', 'scripts/admissibility_d4_self_delimiting_forward_record_append_history_2026_08_30.py': '5eb733c3a50da1f7c1bb8a46b547b1b91fd85c27856e425d8040305b3d009d6c'}

def current_inputs_ok():
    return all((ROOT/p).is_file() and hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==sha for p,sha in DIRECT_HASHES.items()) and set(DIRECT_HASHES)==set(AUDIT_INPUT_PATHS) and bool(DIRECT_HASHES)


def main():
    if not current_inputs_ok():
        print('FAIL current_source_and_note_inputs')
        print('TERMINAL: INCOMPLETE-NO-SCIENCE-INFERENCE')
        print('TOTAL: PASS=0 FAIL=1')
        return 1
    passed=1
    failed=0
    print('PASS current_source_and_note_inputs')
    ok=bool(reached_sector_sampling_certificate())
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'reached_STATUS_sampling')
    ok=bool(carrier_certificate())
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'28_clean_76_borrowed')
    ok=bool(primitive_certificate())
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'56_macro_864_primitive_schedule')
    ok=bool(record_qnd_certificate())
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'QND_and_symbolic_cleanup')
    ok=bool(bounded_truth())
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'complete256_truth')
    ok=bool(covariance_certificate())
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'covariance')
    ok=bool(logical_side_exchange_certificate())
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'logical_side_exchange')
    ok=bool(semantic_totalization_specification_certificate())
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'abstract_totalization_only')
    ok=bool(token_route_correspondence_certificate())
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'token_route_correspondence')
    ok=bool(not toffoli_expansion_certificate("delete_toffoli_CNOT"))
    passed+=int(ok); failed+=int(not ok)
    print(('PASS ' if ok else 'FAIL ')+'actual_Toffoli_CNOT_deletion')
    print('TERMINAL: '+('BLOCK31-NAMED-BOUNDED-CHECKS-COMPLETE;CONDITIONAL-PROOFS-PRESERVED' if failed==0 else 'INCOMPLETE-NO-SCIENCE-INFERENCE'))
    print(f'TOTAL: PASS={passed} FAIL={failed}')
    return int(failed!=0)

if __name__=='__main__':
    raise SystemExit(main())
