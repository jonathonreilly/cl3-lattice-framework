#!/usr/bin/env python3
"""Test the fixed local Record front with one continuous shared battery.

This runner rebuilds only the fixed-N=4 CAR sector of the open cube.  It keeps
the path, pulse, dwells, thresholds, and width-one sine battery fixed.  The
battery is never reset: every prefix is reconstructed from energy-resolved
amplitudes referred to the initial state.  Continuum battery traces use the
closed overlap and mixed energy-moment kernels, not a discretized ladder or a
scalar reserve recurrence.

The result is a conditional finite-fixture test.  It does not derive Record
formation, the scheduler, the carrier, the battery preparation, or renewal.
Exit status validates numerics, live independent agreement on all 40 surfaces,
and the preregistered wide-packet guarantees. Width-one transport failures
remain measured BENCHMARK outcomes; validation success does not assert those
failed physical targets.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
import math
import os
import resource
import sys
import time
from dataclasses import dataclass

for _thread_variable in (
    "OPENBLAS_NUM_THREADS",
    "OMP_NUM_THREADS",
    "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS",
    "NUMEXPR_NUM_THREADS",
):
    os.environ[_thread_variable] = "1"

import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigh


AUDIT_INPUT_PATHS = ("scripts/native_edge_record_shared_battery_transport_independent_check_2026_09_07.py",)
COMPARISON_TOL = 5.0e-8
AUDIT_TIMEOUT_SEC = 180
RSS_LIMIT_MIB = 180.0
NUM_TOL = 3.0e-9
DEGENERACY_TOL = 3.0e-10
CURRENT_FLOOR = 2.0e-2
DENSITY_LOW = 0.10
DENSITY_HIGH = 0.90
BOOST_PHASE = 0.7
EDGE_ORDER = (0, 3, 5, 6, 9)
DWELLS = (0.41, 0.37, 0.29, 0.23, 0.19)
VERTICES = 8
PARTICLES = 4
EDGES = (
    (0, 1),
    (0, 2),
    (0, 4),
    (1, 3),
    (1, 5),
    (2, 3),
    (2, 6),
    (3, 7),
    (4, 5),
    (4, 6),
    (5, 7),
    (6, 7),
)
COEFFICIENTS = (
    -1.0,
    -1.0,
    -1.0,
    -1.0,
    -1.0,
    1.0,
    -1.0,
    -1.0,
    1.0,
    1.0,
    1.0,
    -1.0,
)
LOCAL_PORT_ORDERS = {
    0: (1, 2, 4),
    1: (3, 5, 0),
    2: (3, 6, 0),
    3: (1, 2, 7),
    4: (5, 6, 0),
    5: (7, 4, 1),
    6: (2, 4, 7),
    7: (3, 5, 6),
}

# Frozen physical-battery parameters from the parent theorem.  The old
# scalar-ledger values 4 and 8 are deliberately absent.
HAMILTONIAN_BOUND = 12.0
PACKET_LOW = 24.0
PACKET_WIDTH = 1.0
PACKET_HIGH = PACKET_LOW + PACKET_WIDTH
PACKET_MEAN = PACKET_LOW + 0.5 * PACKET_WIDTH
BATTERY_CAP = 49.0
PREREGISTERED_CONTROL_WIDTHS = (125.0, 260.0)


class Report:
    def __init__(self) -> None:
        self.lines: list[str] = []
        self.passes = 0
        self.failures = 0
        self.numerical_failures = 0
        self.physics_failures = 0

    def check(
        self,
        family: str,
        description: str,
        condition: bool,
        detail: str,
        *,
        physics: bool = False,
    ) -> None:
        status = "PASS" if condition else "FAIL"
        kind = "PHYSICS" if physics else "NUMERIC"
        prefix = "BENCHMARK " if physics else ""
        self.lines.append(f"{prefix}{status} {family} {kind} {description}: {detail}")
        if condition:
            self.passes += int(not physics)
        else:
            self.failures += int(not physics)
            if physics:
                self.physics_failures += 1
            else:
                self.numerical_failures += 1


@dataclass(frozen=True)
class SpectralGroup:
    energy: float
    projector: np.ndarray
    multiplicity: int
    spread: float


@dataclass(frozen=True)
class SurfaceState:
    density: np.ndarray
    battery_energy: float
    trace: float
    min_shift: float
    max_shift: float


def max_abs(array: np.ndarray) -> float:
    return float(np.max(np.abs(array))) if array.size else 0.0


def ladder_action(bits: int, site: int, create: bool) -> tuple[int, complex] | None:
    occupied = bool((bits >> site) & 1)
    if occupied == create:
        return None
    sign = -1.0 if ((bits & ((1 << site) - 1)).bit_count() & 1) else 1.0
    return bits ^ (1 << site), complex(sign)


def directed_hop(
    basis: tuple[int, ...], index: dict[int, int], source: int, target: int
) -> np.ndarray:
    """Return c_target^dagger c_source in the declared fixed-N basis."""
    result = np.zeros((len(basis), len(basis)), dtype=np.complex128)
    for column, bits in enumerate(basis):
        removed = ladder_action(bits, source, create=False)
        if removed is None:
            continue
        after_removal, first_sign = removed
        added = ladder_action(after_removal, target, create=True)
        if added is None:
            continue
        after_addition, second_sign = added
        result[index[after_addition], column] += first_sign * second_sign
    return result


def build_sector() -> tuple[
    tuple[int, ...], list[np.ndarray], list[np.ndarray], list[np.ndarray]
]:
    basis = tuple(bits for bits in range(1 << VERTICES) if bits.bit_count() == PARTICLES)
    index = {bits: position for position, bits in enumerate(basis)}
    hops: list[np.ndarray] = []
    currents: list[np.ndarray] = []
    for u, v in EDGES:
        u_to_v = directed_hop(basis, index, u, v)
        v_to_u = directed_hop(basis, index, v, u)
        hops.append(u_to_v + v_to_u)
        currents.append(1j * (v_to_u - u_to_v))
    numbers = [
        np.diag([float((bits >> site) & 1) for bits in basis]).astype(np.complex128)
        for site in range(VERTICES)
    ]
    return basis, hops, currents, numbers


def hamiltonian(hops: list[np.ndarray], live_mask: int) -> np.ndarray:
    result = np.zeros_like(hops[0])
    for edge, hop in enumerate(hops):
        if (live_mask >> edge) & 1:
            result += COEFFICIENTS[edge] * hop
    return result


def component_count(live_mask: int) -> int:
    adjacency = [[] for _ in range(VERTICES)]
    for edge, (u, v) in enumerate(EDGES):
        if (live_mask >> edge) & 1:
            adjacency[u].append(v)
            adjacency[v].append(u)
    seen: set[int] = set()
    count = 0
    for start in range(VERTICES):
        if start in seen:
            continue
        count += 1
        stack = [start]
        seen.add(start)
        while stack:
            vertex = stack.pop()
            for neighbor in adjacency[vertex]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
    return count


def local_front_order() -> tuple[int, ...]:
    edge_number = {edge: number for number, edge in enumerate(EDGES)}
    live = set(range(len(EDGES)))
    vertex = EDGES[EDGE_ORDER[0]][0]
    order: list[int] = []
    for _ in EDGE_ORDER:
        incident = [
            edge_number[tuple(sorted((vertex, neighbor)))]
            for neighbor in LOCAL_PORT_ORDERS[vertex]
        ]
        edge = next((candidate for candidate in incident if candidate in live), None)
        if edge is None:
            raise AssertionError("front has no live edge")
        order.append(edge)
        live.remove(edge)
        u, v = EDGES[edge]
        vertex = v if vertex == u else u
    return tuple(order)


def spectral_groups(matrix: np.ndarray) -> tuple[list[SpectralGroup], np.ndarray, np.ndarray, float]:
    values, vectors = eigh(matrix)
    groups: list[SpectralGroup] = []
    start = 0
    maximum_residual = max_abs(matrix @ vectors - vectors * values[np.newaxis, :])
    maximum_residual = max(
        maximum_residual,
        max_abs(vectors.conj().T @ vectors - np.eye(len(values))),
    )
    while start < len(values):
        stop = start + 1
        while stop < len(values) and abs(values[stop] - values[start]) <= DEGENERACY_TOL:
            stop += 1
        block = vectors[:, start:stop]
        energy = float(np.mean(values[start:stop]))
        projector = block @ block.conj().T
        spread = float(np.max(np.abs(values[start:stop] - energy)))
        maximum_residual = max(
            maximum_residual,
            max_abs(projector @ projector - projector),
            max_abs(matrix @ projector - energy * projector),
            spread,
        )
        groups.append(SpectralGroup(energy, projector, stop - start, spread))
        start = stop
    maximum_residual = max(
        maximum_residual,
        max_abs(sum((group.projector for group in groups), np.zeros_like(matrix)) - np.eye(len(values))),
    )
    return groups, values, vectors, maximum_residual


def sine_overlap_scalar(displacement: float, width: float = PACKET_WIDTH) -> float:
    """Return <beta|T_displacement beta> for the frozen real sine packet."""
    x = abs(float(displacement)) / width
    if x >= 1.0:
        return 0.0
    return (1.0 - x) * math.cos(math.pi * x) + math.sin(math.pi * x) / math.pi


def sine_overlap(
    displacement: np.ndarray, width: float = PACKET_WIDTH
) -> np.ndarray:
    x = np.abs(np.asarray(displacement, dtype=float)) / width
    inside = x < 1.0
    result = np.zeros_like(x)
    result[inside] = (
        (1.0 - x[inside]) * np.cos(math.pi * x[inside])
        + np.sin(math.pi * x[inside]) / math.pi
    )
    return result


def mixed_battery_energy_scalar(
    ket_shift: float, bra_shift: float, width: float = PACKET_WIDTH
) -> float:
    """Return <T_bra beta|E_B|T_ket beta>.

    The product of the two translated real sine packets is symmetric about
    PACKET_LOW + width/2 + (ket_shift + bra_shift)/2.  Its zeroth moment is the
    overlap, so its first moment is the midpoint times that overlap.
    """
    return (
        PACKET_LOW + 0.5 * width + 0.5 * (ket_shift + bra_shift)
    ) * sine_overlap_scalar(ket_shift - bra_shift, width)


def direct_packet_integrals(ket_shift: float, bra_shift: float) -> tuple[float, float]:
    lower = max(PACKET_LOW + ket_shift, PACKET_LOW + bra_shift)
    upper = min(PACKET_HIGH + ket_shift, PACKET_HIGH + bra_shift)
    if lower >= upper:
        return 0.0, 0.0

    normalization = math.sqrt(2.0 / PACKET_WIDTH)

    def translated_packet(energy: float, shift: float) -> float:
        x = (energy - shift - PACKET_LOW) / PACKET_WIDTH
        return normalization * math.sin(math.pi * x)

    def product(energy: float) -> float:
        return translated_packet(energy, ket_shift) * translated_packet(energy, bra_shift)

    overlap = quad(product, lower, upper, epsabs=2.0e-13, epsrel=2.0e-13, limit=100)[0]
    moment = quad(
        lambda energy: energy * product(energy),
        lower,
        upper,
        epsabs=2.0e-13,
        epsrel=2.0e-13,
        limit=100,
    )[0]
    return float(overlap), float(moment)


def unitary_from_eigensystem(values: np.ndarray, vectors: np.ndarray, dwell: float) -> np.ndarray:
    return (vectors * np.exp(-1j * dwell * values)[np.newaxis, :]) @ vectors.conj().T


def surface_from_components(
    components: dict[tuple[int, int], np.ndarray],
    initial_groups: list[SpectralGroup],
    surface_groups: list[SpectralGroup],
    packet_width: float = PACKET_WIDTH,
) -> SurfaceState:
    entries: list[tuple[float, np.ndarray]] = []
    for (initial_group, surface_group), vector in sorted(components.items()):
        shift = initial_groups[initial_group].energy - surface_groups[surface_group].energy
        entries.append((shift, vector))
    shifts = np.array([entry[0] for entry in entries], dtype=float)
    vectors = np.column_stack([entry[1] for entry in entries])
    differences = shifts[:, np.newaxis] - shifts[np.newaxis, :]
    overlap = sine_overlap(differences, packet_width)
    density = vectors @ overlap @ vectors.conj().T
    gram = vectors.conj().T @ vectors
    moments = (
        PACKET_LOW
        + 0.5 * packet_width
        + 0.5 * (shifts[:, np.newaxis] + shifts[np.newaxis, :])
    ) * overlap
    trace = np.trace(density)
    battery_energy = np.einsum("ij,ji->", moments, gram)
    if abs(trace.imag) > NUM_TOL or abs(battery_energy.imag) > NUM_TOL:
        raise AssertionError("continuous battery contraction is not real")
    return SurfaceState(
        density,
        float(battery_energy.real),
        float(trace.real),
        float(np.min(shifts)),
        float(np.max(shifts)),
    )


def endpoint_components(
    initial_state: np.ndarray,
    propagator: np.ndarray,
    initial_groups: list[SpectralGroup],
    surface_groups: list[SpectralGroup],
) -> dict[tuple[int, int], np.ndarray]:
    result: dict[tuple[int, int], np.ndarray] = {}
    for initial_number, initial_group in enumerate(initial_groups):
        source = initial_group.projector @ initial_state
        evolved = propagator @ source
        for surface_number, surface_group in enumerate(surface_groups):
            result[(initial_number, surface_number)] = surface_group.projector @ evolved
    return result


def individual_eigenstate_surface(
    initial_state: np.ndarray,
    propagator: np.ndarray,
    initial_values: np.ndarray,
    initial_vectors: np.ndarray,
    surface_values: np.ndarray,
    surface_vectors: np.ndarray,
    packet_width: float = PACKET_WIDTH,
) -> tuple[np.ndarray, float]:
    """Ungrouped spectral contraction used as a degeneracy-invariance check."""
    initial_coefficients = initial_vectors.conj().T @ initial_state
    amplitudes = (surface_vectors.conj().T @ propagator @ initial_vectors) * initial_coefficients
    dimension = len(initial_values)
    reduced_eigenbasis = np.zeros((dimension, dimension), dtype=np.complex128)
    for left_surface in range(dimension):
        left_shifts = initial_values - surface_values[left_surface]
        for right_surface in range(dimension):
            right_shifts = initial_values - surface_values[right_surface]
            kernel = sine_overlap(
                left_shifts[:, np.newaxis] - right_shifts[np.newaxis, :],
                packet_width,
            )
            reduced_eigenbasis[left_surface, right_surface] = amplitudes[left_surface] @ (
                kernel @ amplitudes[right_surface].conj()
            )
    battery_energy = 0.0 + 0.0j
    for surface in range(dimension):
        shifts = initial_values - surface_values[surface]
        kernel = sine_overlap(
            shifts[:, np.newaxis] - shifts[np.newaxis, :], packet_width
        )
        moments = (
            PACKET_LOW
            + 0.5 * packet_width
            + 0.5 * (shifts[:, np.newaxis] + shifts[np.newaxis, :])
        ) * kernel
        battery_energy += amplitudes[surface] @ (moments @ amplitudes[surface].conj())
    reduced = surface_vectors @ reduced_eigenbasis @ surface_vectors.conj().T
    if abs(battery_energy.imag) > NUM_TOL:
        raise AssertionError("ungrouped battery moment is not real")
    return reduced, float(battery_energy.real)


def measure(
    density: np.ndarray,
    hamiltonian_matrix: np.ndarray,
    live_mask: int,
    currents: list[np.ndarray],
    numbers: list[np.ndarray],
) -> dict[str, object]:
    energy = float(np.trace(density @ hamiltonian_matrix).real)
    densities = tuple(float(np.trace(density @ number).real) for number in numbers)
    current_values = {
        edge: COEFFICIENTS[edge] * float(np.trace(density @ currents[edge]).real)
        for edge in range(len(EDGES))
        if (live_mask >> edge) & 1
    }
    support = sum(abs(value) >= CURRENT_FLOOR for value in current_values.values())
    return {
        "energy": energy,
        "densities": densities,
        "currents": current_values,
        "support": support,
        "number": sum(densities),
    }


def density_numerics(density: np.ndarray) -> tuple[float, float, float]:
    hermiticity = max_abs(density - density.conj().T)
    trace_error = abs(float(np.trace(density).real) - 1.0)
    minimum_eigenvalue = float(np.min(np.linalg.eigvalsh(0.5 * (density + density.conj().T))))
    return hermiticity, trace_error, minimum_eigenvalue


def compact_values(values: tuple[float, ...]) -> str:
    return ",".join(str(int(round(1.0e4 * value))) for value in values)


def compact_currents(values: dict[int, float]) -> str:
    return ",".join(
        "x" if edge not in values else str(int(round(1.0e4 * values[edge])))
        for edge in range(len(EDGES))
    )


def run_protocol(
    convention: str,
    packet_width: float,
    initial_state: np.ndarray,
    hamiltonians: list[np.ndarray],
    masks: list[int],
    groups: list[list[SpectralGroup]],
    eigenvalues: list[np.ndarray],
    eigenvectors: list[np.ndarray],
    currents: list[np.ndarray],
    numbers: list[np.ndarray],
) -> dict[str, object]:
    if convention not in ("controlled", "free"):
        raise ValueError("unknown dwell convention")
    if packet_width <= 0.0 or not math.isfinite(packet_width):
        raise ValueError("packet width must be finite and positive")
    packet_mean = PACKET_LOW + 0.5 * packet_width
    battery_cap = 4.0 * HAMILTONIAN_BOUND + packet_width
    initial_density = np.outer(initial_state, initial_state.conj())
    initial_energy = float(np.vdot(initial_state, hamiltonians[0] @ initial_state).real)
    conserved_total = initial_energy + packet_mean
    initial_components = {
        (number, number): group.projector @ initial_state
        for number, group in enumerate(groups[0])
    }
    post_surface = surface_from_components(
        initial_components, groups[0], groups[0], packet_width
    )
    post_propagator = np.eye(len(initial_state), dtype=np.complex128)
    sequential_components = initial_components
    cumulative_dwell = 0.0
    maximum_component_residual = 0.0
    maximum_dwell_residual = 0.0
    maximum_state_residual = 0.0
    maximum_total_drift = 0.0
    first_minus_control = math.inf
    minimum_shift = 0.0
    maximum_shift = 0.0
    battery_energies = [post_surface.battery_energy]
    fixed_number_excesses: list[float] = []
    all_energies = [initial_energy]
    rows: list[dict[str, object]] = []

    for step, (edge, dwell) in enumerate(zip(EDGE_ORDER, DWELLS), start=1):
        pre_dwell = measure(
            post_surface.density,
            hamiltonians[step - 1],
            masks[step - 1],
            currents,
            numbers,
        )
        dwell_unitary = unitary_from_eigensystem(
            eigenvalues[step - 1], eigenvectors[step - 1], dwell
        )
        cumulative_dwell += dwell
        if convention == "controlled":
            minus_propagator = dwell_unitary @ post_propagator
            plus_propagator = minus_propagator
        else:
            minus_propagator = unitary_from_eigensystem(
                eigenvalues[step - 1], eigenvectors[step - 1], cumulative_dwell
            )
            plus_propagator = unitary_from_eigensystem(
                eigenvalues[step], eigenvectors[step], cumulative_dwell
            )

        minus_components = endpoint_components(
            initial_state, minus_propagator, groups[0], groups[step - 1]
        )
        plus_components = endpoint_components(
            initial_state, plus_propagator, groups[0], groups[step]
        )
        minus_surface = surface_from_components(
            minus_components, groups[0], groups[step - 1], packet_width
        )
        plus_surface = surface_from_components(
            plus_components, groups[0], groups[step], packet_width
        )
        maximum_dwell_residual = max(
            maximum_dwell_residual,
            max_abs(
                minus_surface.density
                - dwell_unitary @ post_surface.density @ dwell_unitary.conj().T
            ),
        )
        if step == 1:
            first_minus_control = max_abs(
                minus_surface.density
                - dwell_unitary @ initial_density @ dwell_unitary.conj().T
            )

        if convention == "controlled":
            sequential_minus = {
                key: np.exp(-1j * dwell * groups[step - 1][key[1]].energy)
                * vector
                for key, vector in sequential_components.items()
            }
            sequential_plus: dict[tuple[int, int], np.ndarray] = {}
            for initial_number in range(len(groups[0])):
                total = sum(
                    (
                        vector
                        for (candidate, _), vector in sequential_minus.items()
                        if candidate == initial_number
                    ),
                    np.zeros(len(initial_state), dtype=np.complex128),
                )
                for output_number, output_group in enumerate(groups[step]):
                    sequential_plus[(initial_number, output_number)] = (
                        output_group.projector @ total
                    )
            maximum_component_residual = max(
                maximum_component_residual,
                max(
                    max_abs(sequential_plus[key] - plus_components[key])
                    for key in plus_components
                ),
            )
            sequential_components = sequential_plus
        else:
            for initial_number, initial_group in enumerate(groups[0]):
                source = initial_group.projector @ initial_state
                for output_number, output_group in enumerate(groups[step]):
                    pulled_through = (
                        np.exp(-1j * cumulative_dwell * output_group.energy)
                        * output_group.projector
                        @ source
                    )
                    maximum_component_residual = max(
                        maximum_component_residual,
                        max_abs(
                            pulled_through
                            - plus_components[(initial_number, output_number)]
                        ),
                    )

        event_minus = measure(
            minus_surface.density,
            hamiltonians[step - 1],
            masks[step - 1],
            currents,
            numbers,
        )
        event_plus = measure(
            plus_surface.density,
            hamiltonians[step],
            masks[step],
            currents,
            numbers,
        )
        fixed_number_excess = float(event_plus["energy"]) - float(
            np.min(eigenvalues[step])
        )
        fixed_number_excesses.append(fixed_number_excess)
        all_energies.extend((float(event_minus["energy"]), float(event_plus["energy"])))
        for surface, observed in (
            (minus_surface, event_minus),
            (plus_surface, event_plus),
        ):
            hermiticity, trace_error, minimum_eigenvalue = density_numerics(surface.density)
            maximum_state_residual = max(
                maximum_state_residual,
                hermiticity,
                trace_error,
                max(0.0, -minimum_eigenvalue),
                abs(float(observed["number"]) - PARTICLES),
            )
            maximum_total_drift = max(
                maximum_total_drift,
                abs(float(observed["energy"]) + surface.battery_energy - conserved_total),
            )
            minimum_shift = min(minimum_shift, surface.min_shift)
            maximum_shift = max(maximum_shift, surface.max_shift)
            battery_energies.append(surface.battery_energy)
        rows.append(
            {
                "step": step,
                "edge": edge,
                "pre_dwell": pre_dwell,
                "minus": event_minus,
                "plus": event_plus,
                "minus_surface": minus_surface,
                "plus_surface": plus_surface,
                "excess": fixed_number_excess,
            }
        )
        post_surface = plus_surface
        post_propagator = plus_propagator

    ungrouped_density, ungrouped_battery = individual_eigenstate_surface(
        initial_state,
        post_propagator,
        eigenvalues[0],
        eigenvectors[0],
        eigenvalues[-1],
        eigenvectors[-1],
        packet_width,
    )
    degeneracy_residual = max(
        max_abs(ungrouped_density - post_surface.density),
        abs(ungrouped_battery - post_surface.battery_energy),
    )
    return {
        "convention": convention,
        "packet_width": packet_width,
        "packet_mean": packet_mean,
        "battery_cap": battery_cap,
        "rows": rows,
        "component_residual": maximum_component_residual,
        "dwell_residual": maximum_dwell_residual,
        "state_residual": maximum_state_residual,
        "total_drift": maximum_total_drift,
        "first_minus_control": first_minus_control,
        "degeneracy_residual": degeneracy_residual,
        "reachable_low": PACKET_LOW + minimum_shift,
        "reachable_high": PACKET_LOW + packet_width + maximum_shift,
        "battery_min": min(battery_energies),
        "battery_max": max(battery_energies),
        "minimum_excess": min(fixed_number_excesses),
        "all_energy_max": max(all_energies),
        "post_energy_min": min(float(row["plus"]["energy"]) for row in rows),
        "post_energy_max": max(float(row["plus"]["energy"]) for row in rows),
        "minus_supports": [int(row["minus"]["support"]) for row in rows],
        "plus_supports": [int(row["plus"]["support"]) for row in rows],
        "front_max": max(abs(float(row["minus"]["currents"][row["edge"]])) for row in rows),
        "minus_density_min": min(min(row["minus"]["densities"]) for row in rows),
        "minus_density_max": max(max(row["minus"]["densities"]) for row in rows),
        "plus_density_min": min(min(row["plus"]["densities"]) for row in rows),
        "plus_density_max": max(max(row["plus"]["densities"]) for row in rows),
    }


def comparison_payload(results: list[dict[str, object]]) -> dict[str, object]:
    """Export primary measurements without reading the independent measurements."""
    surfaces = []
    for result in results:
        for row in result["rows"]:
            for side, name in (("pre", "minus"), ("post", "plus")):
                observed = row[name]
                surfaces.append({
                    "protocol": result["convention"],
                    "width": result["packet_width"],
                    "step": row["step"],
                    "edge": row["edge"],
                    "side": side,
                    "resource": {"low": PACKET_LOW, "mean": result["packet_mean"],
                                 "cap": result["battery_cap"]},
                    "densities": list(observed["densities"]),
                    "currents": {str(edge): value for edge, value in observed["currents"].items()},
                    "matter_energy": observed["energy"],
                    "battery_energy": row[name + "_surface"].battery_energy,
                    "support": observed["support"],
                })
    return {"schema": "shared-battery-surfaces-v1", "validation_ok": True,
            "surfaces": surfaces}


def compare_payload(expected: object, actual: object, path: str = "root") -> float:
    """Fail closed on schema, coverage, exact discrete fields, or nonfinite values."""
    if isinstance(expected, dict):
        if not isinstance(actual, dict) or expected.keys() != actual.keys():
            raise ValueError(f"{path}: field/resource/current keys differ")
        return max((compare_payload(value, actual[key], f"{path}.{key}")
                    for key, value in expected.items()), default=0.0)
    if isinstance(expected, list):
        if not isinstance(actual, list) or len(expected) != len(actual):
            raise ValueError(f"{path}: surface/observable count differs")
        return max((compare_payload(a, b, f"{path}[{index}]")
                    for index, (a, b) in enumerate(zip(expected, actual))), default=0.0)
    if isinstance(expected, float):
        if (type(actual) not in (float, int) or not math.isfinite(expected)
                or not math.isfinite(actual)):
            raise ValueError(f"{path}: nonfinite or nonnumeric value")
        residual = abs(expected - actual)
        # Packet resource declarations and widths are fixture keys, not estimates.
        exact = ".resource." in path or path.endswith(".width")
        if residual > (0.0 if exact else COMPARISON_TOL):
            raise ValueError(f"{path}: disagreement {residual:.3e}")
        return residual
    if type(expected) is not type(actual) or expected != actual:
        raise ValueError(f"{path}: discrete/status value differs")
    return 0.0


def validate_independent(results: list[dict[str, object]], started: float, report: Report) -> None:
    try:
        remaining = AUDIT_TIMEOUT_SEC - (time.perf_counter() - started)
        if remaining <= 0:
            raise ValueError("no time remains for independent checker")
        child = subprocess.run(
            [sys.executable, str(Path(__file__).resolve().parent / Path(AUDIT_INPUT_PATHS[0]).name), "--json"],
            capture_output=True, text=True, timeout=remaining, check=True,
        )
        # Duplicate keys must not silently overwrite a failed status or measurement.
        def unique_object(pairs):
            result = {}
            for key, value in pairs:
                if key in result:
                    raise ValueError(f"duplicate JSON key: {key}")
                result[key] = value
            return result
        actual = json.loads(child.stdout, object_pairs_hook=unique_object)
        expected = comparison_payload(results)
        if len(expected["surfaces"]) != 40:
            raise ValueError("primary fixture does not contain all 40 surfaces")
        residual = compare_payload(expected, actual)
        report.check("live_independent_agreement", "all 40 pre/post surfaces",
                     True, f"max_residual={residual:.3e} tolerance={COMPARISON_TOL:.1e}; exact supports/resource keys")
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        report.check("live_independent_agreement", "all 40 pre/post surfaces", False,
                     f"{type(error).__name__}: {error}")


def main() -> int:
    started = time.perf_counter()
    if any(argument != "--detail" for argument in sys.argv[1:]) or sys.argv[1:].count("--detail") > 1:
        raise SystemExit("usage: native_edge_record_shared_battery_transport_2026_09_07.py [--detail]")
    detailed = "--detail" in sys.argv[1:]
    report = Report()
    basis, hops, currents, numbers = build_sector()
    full_mask = (1 << len(EDGES)) - 1
    masks = [full_mask]
    for edge in EDGE_ORDER:
        masks.append(masks[-1] & ~(1 << edge))
    hamiltonians = [hamiltonian(hops, mask) for mask in masks]
    spectra = [spectral_groups(matrix) for matrix in hamiltonians]
    groups = [item[0] for item in spectra]
    eigenvalues = [item[1] for item in spectra]
    eigenvectors = [item[2] for item in spectra]
    spectral_residual = max(item[3] for item in spectra)
    ground_values, ground_vectors = eigh(hamiltonians[0])
    initial_state = ground_vectors[:, int(np.argmin(ground_values))]
    initial_state *= np.array(
        [
            np.exp(-1j * BOOST_PHASE * (((bits >> 0) & 1) - ((bits >> 1) & 1)))
            for bits in basis
        ],
        dtype=np.complex128,
    )
    initial_state /= np.linalg.norm(initial_state)
    initial_energy = float(np.vdot(initial_state, hamiltonians[0] @ initial_state).real)

    packet_residual = 0.0
    for ket_shift, bra_shift in (
        (0.0, 0.0),
        (0.2, -0.3),
        (-0.7, 0.1),
        (1.2, 0.1),
        (2.0, -2.0),
    ):
        direct_overlap, direct_moment = direct_packet_integrals(ket_shift, bra_shift)
        packet_residual = max(
            packet_residual,
            abs(direct_overlap - sine_overlap_scalar(ket_shift - bra_shift)),
            abs(direct_moment - mixed_battery_energy_scalar(ket_shift, bra_shift)),
        )
    report.check(
        "kernel_moments",
        "analytic sine overlap and mixed energy moment",
        packet_residual <= 2.0e-11
        and abs(sine_overlap_scalar(0.0) - 1.0) <= 1.0e-15
        and sine_overlap_scalar(PACKET_WIDTH) == 0.0,
        f"quadrature_crosscheck={packet_residual:.3e} width=1 mean=24.5",
    )
    report.check(
        "sector_spectrum",
        "fixed sector and spectral resolutions",
        len(basis) == math.comb(VERTICES, PARTICLES) == 70
        and spectral_residual <= NUM_TOL
        and max(max(abs(value) for value in values) for values in eigenvalues)
        <= HAMILTONIAN_BOUND + NUM_TOL,
        f"dimension=70 groups={[len(value) for value in groups]} residual={spectral_residual:.3e}",
    )
    connected_nonbridges = all(
        component_count(masks[step - 1]) == component_count(masks[step]) == 1
        for step in range(1, len(masks))
    )
    report.check(
        "nonbridge_path",
        "frozen local path has five nonbridge events",
        local_front_order() == EDGE_ORDER and connected_nonbridges,
        f"order={EDGE_ORDER} components={[component_count(mask) for mask in masks]}",
    )

    results = [
        run_protocol(
            convention,
            PACKET_WIDTH,
            initial_state,
            hamiltonians,
            masks,
            groups,
            eigenvalues,
            eigenvectors,
            currents,
            numbers,
        )
        for convention in ("controlled", "free")
    ]
    for result in results:
        label = str(result["convention"])
        report.check(
            f"{label}_shared_composition",
            (
                "sequential energy-resolved and endpoint controls"
                if label == "controlled"
                else "spectral endpoint and reduced free-dwell controls"
            ),
            float(result["component_residual"]) <= NUM_TOL
            and float(result["dwell_residual"]) <= NUM_TOL,
            f"component={float(result['component_residual']):.2e} dwell={float(result['dwell_residual']):.2e}",
        )
        report.check(
            f"{label}_state_ledger",
            "state, cap, battery moment and fixed-N checks",
            float(result["state_residual"]) <= NUM_TOL
            and float(result["degeneracy_residual"]) <= 8.0e-9
            and float(result["first_minus_control"]) <= NUM_TOL
            and float(result["minimum_excess"]) >= -NUM_TOL
            and float(result["reachable_low"]) >= -NUM_TOL
            and float(result["reachable_high"])
            <= float(result["battery_cap"]) + NUM_TOL
            and float(result["battery_min"]) >= -NUM_TOL
            and float(result["battery_max"])
            <= float(result["battery_cap"]) + NUM_TOL
            and float(result["first_minus_control"]) <= NUM_TOL
            and float(result["minimum_excess"]) >= -NUM_TOL
            and float(result["battery_min"]) >= -NUM_TOL
            and float(result["battery_max"])
            <= float(result["battery_cap"]) + NUM_TOL
            and float(result["total_drift"]) <= 1.0e-8,
            f"state={float(result['state_residual']):.2e} deg={float(result['degeneracy_residual']):.2e} first={float(result['first_minus_control']):.2e} excess={float(result['minimum_excess']):.6f} support=[{float(result['reachable_low']):.3f},{float(result['reachable_high']):.3f}] drift={float(result['total_drift']):.2e}",
        )
        report.check(
            f"{label}_pre_transport",
            "event-minus transport gate",
            min(result["minus_supports"]) >= 4 and float(result["front_max"]) >= 0.05,
            f"supports={result['minus_supports']} front_max={float(result['front_max']):.6f}",
            physics=True,
        )
        report.check(
            f"{label}_post_transport",
            "event-plus surviving-current gate",
            min(result["plus_supports"]) >= 4,
            f"supports={result['plus_supports']} floor={CURRENT_FLOOR:g}",
            physics=True,
        )
        report.check(
            f"{label}_density",
            "event-minus and event-plus density window",
            float(result["minus_density_min"]) >= DENSITY_LOW
            and float(result["minus_density_max"]) <= DENSITY_HIGH
            and float(result["plus_density_min"]) >= DENSITY_LOW
            and float(result["plus_density_max"]) <= DENSITY_HIGH,
            f"minus=[{float(result['minus_density_min']):.4f},{float(result['minus_density_max']):.4f}] plus=[{float(result['plus_density_min']):.4f},{float(result['plus_density_max']):.4f}]",
            physics=True,
        )
        report.check(
            f"{label}_negative_energy",
            "all event-minus and event-plus matter energies negative",
            float(result["all_energy_max"]) < -NUM_TOL,
            f"all_max={float(result['all_energy_max']):+.6f} post=[{float(result['post_energy_min']):+.6f},{float(result['post_energy_max']):+.6f}]",
            physics=True,
        )
        for row in result["rows"]:
            data_line = (
                "DATA "
                f"{label} k={row['step']} e={row['edge']} "
                f"Jpre={float(row['pre_dwell']['currents'][row['edge']]):+.5f} "
                f"Jm={float(row['minus']['currents'][row['edge']]):+.5f} "
                f"S={int(row['minus']['support'])}/{int(row['plus']['support'])} "
                f"E={float(row['minus']['energy']):+.5f}/{float(row['plus']['energy']):+.5f} "
                f"EB={row['minus_surface'].battery_energy:.5f}/{row['plus_surface'].battery_energy:.5f} "
                f"X={float(row['excess']):.5f}"
            )
            if detailed:
                data_line += (
                    f" dm={compact_values(row['minus']['densities'])}"
                    f" dp={compact_values(row['plus']['densities'])}"
                    f" jm={compact_currents(row['minus']['currents'])}"
                    f" jp={compact_currents(row['plus']['currents'])}"
                )
            report.lines.append(data_line)
    control_results = [
        run_protocol(
            "controlled",
            width,
            initial_state,
            hamiltonians,
            masks,
            groups,
            eigenvalues,
            eigenvectors,
            currents,
            numbers,
        )
        for width in PREREGISTERED_CONTROL_WIDTHS
    ]
    for result in control_results:
        width = int(float(result["packet_width"]))
        numerical_ok = (
            float(result["component_residual"]) <= NUM_TOL
            and float(result["dwell_residual"]) <= NUM_TOL
            and float(result["state_residual"]) <= NUM_TOL
            and float(result["degeneracy_residual"]) <= 8.0e-9
            and float(result["total_drift"]) <= 1.0e-8
            and float(result["reachable_low"]) >= -NUM_TOL
            and float(result["reachable_high"])
            <= float(result["battery_cap"]) + NUM_TOL
        )
        original_gate = (
            min(result["minus_supports"]) >= 4
            and float(result["front_max"]) >= 0.05
            and float(result["minus_density_min"]) >= DENSITY_LOW
            and float(result["minus_density_max"]) <= DENSITY_HIGH
            and float(result["plus_density_min"]) >= DENSITY_LOW
            and float(result["plus_density_max"]) <= DENSITY_HIGH
            and float(result["all_energy_max"]) < -NUM_TOL
        )
        post_gate = min(result["plus_supports"]) >= 4
        report.check(
            f"controlled_width{width}_numerics",
            "independently priced width control",
            numerical_ok,
            f"mean={float(result['packet_mean']):.1f} cap={float(result['battery_cap']):.0f} spectral_enclosure=[{float(result['reachable_low']):.2f},{float(result['reachable_high']):.2f}] excess={float(result['minimum_excess']):.4f} drift={float(result['total_drift']):.2e}",
        )
        declared_gate = original_gate if width == 125 else original_gate and post_gate
        report.check(
            f"controlled_width{width}_physics",
            "preregistered sufficient-width gate",
            declared_gate,
            f"packet=[24,{24 + width}] pre={result['minus_supports']} post={result['plus_supports']} front={float(result['front_max']):.6f} rho=[{float(result['minus_density_min']):.4f},{float(result['minus_density_max']):.4f};{float(result['plus_density_min']):.4f},{float(result['plus_density_max']):.4f}] Emax={float(result['all_energy_max']):+.5f} original={original_gate} post={post_gate}",
        )
    report.lines.append(
        "INHERITED RECORD parent Q/code isometries give persistent labels and "
        "32 weight-1/32 histories; not counted as a fixed-N numerical check"
    )
    report.lines.append(
        "INHERITED FREE exact total-energy intertwining gives exp[-id*a]="
        "exp[-id*(b+a-b)]; this algebraic identity is not a numerical check"
    )
    report.lines.append(
        "SCOPE controlled=supplied D_matter tensor I_battery; free=total "
        "H_matter+E_battery; sine[24,25], width1, cap49; --detail emits "
        "densities/currents x1e-4 (x=deleted)"
    )
    if not detailed:
        report.lines.extend(
            (
                "per_element: checked - every fixed-N matrix element entering each prefix density and observable contraction is included.",
                "per_site: checked - all eight site-number expectations are evaluated at every event-minus and event-plus surface.",
                "per_mode: checked - all grouped energy eigenspaces and their nonzero battery translations enter the continuum trace.",
                "per_block: checked - both five-event dwell conventions and the two preregistered controlled-width blocks are evaluated.",
                "lattice_wide: checked and not executed - this finite one-cube fixture makes no multicell, thermodynamic, or continuum-matter claim.",
            )
        )
    validate_independent(results + control_results, started, report)
    elapsed = time.perf_counter() - started
    rss = float(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    if sys.platform == "darwin":
        rss /= 1024.0 * 1024.0
    else:
        rss /= 1024.0
    report.check(
        "execution_envelope",
        "runtime, memory and fixed thread limits",
        elapsed <= AUDIT_TIMEOUT_SEC
        and rss < RSS_LIMIT_MIB
        and all(
            os.environ.get(variable) == "1"
            for variable in (
                "OPENBLAS_NUM_THREADS",
                "OMP_NUM_THREADS",
                "MKL_NUM_THREADS",
                "VECLIB_MAXIMUM_THREADS",
                "NUMEXPR_NUM_THREADS",
            )
        ),
        f"elapsed={elapsed:.2f}s timeout=180s rss={rss:.1f}MiB cap=180MiB",
    )
    report.lines.append(
        f"SUMMARY validation_fail={report.failures} numerical_fail={report.numerical_failures} physical_fail={report.physics_failures} initial_E={initial_energy:+.6f} initial_EB=24.500000"
    )
    report.lines.append(f"TOTAL: PASS={report.passes} FAIL={report.failures}")
    print("\n".join(report.lines))
    return 1 if report.failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
