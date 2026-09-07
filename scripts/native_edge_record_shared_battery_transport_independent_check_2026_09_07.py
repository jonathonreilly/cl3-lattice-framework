#!/usr/bin/env python3
"""Independent shared-battery checker for the fixed five-event cube protocol.

This checker does not import the primary runner or any cached output.  It uses
two representations:

* an eight-dimensional one-particle finite-frequency evaluation of the
  Fourier-fiber formula for every density and current; and
* an independently assembled 70-dimensional fixed-N CAR sector for the full
  reduced matter state and for the battery mean evaluated from translated
  sine-packet matrix elements.

The frozen CONTROL dwell is D_j tensor I_B.  This is an explicitly supplied
energy-conserving control (or battery interaction-picture convention), not
uncontrolled laboratory evolution under H_j + H_B.  A separately
preregistered FREE comparison uses that laboratory evolution and the derived
endpoint map exp(-i t_j H_surface).  No battery reset occurs in either lane.

--json emits unrounded measurements of all 40 surfaces and numerical validation
status for live comparison; default text and exit semantics are unchanged.

Declared execution envelope: one BLAS thread, 180 seconds, 256 MiB RSS.
"""

from __future__ import annotations

import json
import sys
import math
import os
import resource
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
from numpy.polynomial.legendre import leggauss
from scipy.linalg import eigh


TOL = 5.0e-9
QUADRATURE_TOL = 2.0e-11
AUDIT_TIMEOUT_SEC = 180
TIME_LIMIT_SECONDS = 180.0
RSS_LIMIT_MIB = 256.0
VERTICES = 8
PARTICLES = 4
EVENTS = 5
CURRENT_FLOOR = 2.0e-2
FRONT_FLOOR = 5.0e-2
DENSITY_LOW = 0.10
DENSITY_HIGH = 0.90
BOOST_PHASE = 0.7
BATTERY_PACKET_LOW = 24.0
BATTERY_CAP_LOW = 0.0
BASELINE_WIDTH = 1.0
WIDE_WIDTHS = (125.0, 260.0)
SYSTEM_BOUND = 12.0
EXPECTED_ORDER = (0, 3, 5, 6, 9)
DWELLS = (0.41, 0.37, 0.29, 0.23, 0.19)
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


class Report:
    def __init__(self) -> None:
        self.lines: list[str] = []
        self.passes = 0
        self.failures = 0

    def check(self, family: str, description: str, condition: bool, detail: str) -> None:
        status = "PASS" if condition else "FAIL"
        self.lines.append(f"{status} {family} {description}: {detail}")
        if condition:
            self.passes += 1
        else:
            self.failures += 1


@dataclass
class Spectrum:
    values: np.ndarray
    vectors: np.ndarray


@dataclass
class Surface:
    label: str
    step: int
    edge: int
    live_mask: int
    matter_energy: float
    ground_energy: float
    battery_energy: float
    number_trace: float
    system_norm: float
    min_packet_energy: float
    max_packet_energy: float
    densities: tuple[float, ...]
    currents: tuple[tuple[int, float], ...]
    support: int
    packet_width: float


def ladder_action(bits: int, site: int, create: bool) -> tuple[int, complex] | None:
    occupied = bool((bits >> site) & 1)
    if occupied == create:
        return None
    parity = (bits & ((1 << site) - 1)).bit_count() & 1
    return bits ^ (1 << site), complex(-1.0 if parity else 1.0)


def directed_bilinear(
    basis: tuple[int, ...], index: dict[int, int], source: int, target: int
) -> np.ndarray:
    """Return c_target^dagger c_source on the supplied fixed-N basis."""
    result = np.zeros((len(basis), len(basis)), dtype=np.complex128)
    for column, bits in enumerate(basis):
        first = ladder_action(bits, source, create=False)
        if first is None:
            continue
        after_first, phase_first = first
        second = ladder_action(after_first, target, create=True)
        if second is None:
            continue
        after_second, phase_second = second
        result[index[after_second], column] = phase_first * phase_second
    return result


def build_fixed_number_operators() -> tuple[
    tuple[int, ...], list[np.ndarray], list[np.ndarray], list[np.ndarray], dict[tuple[int, int], np.ndarray]
]:
    basis = tuple(bits for bits in range(1 << VERTICES) if bits.bit_count() == PARTICLES)
    index = {bits: position for position, bits in enumerate(basis)}
    bilinears = {
        (source, target): directed_bilinear(basis, index, source, target)
        for source in range(VERTICES)
        for target in range(VERTICES)
    }
    hops = []
    currents = []
    for u, v in EDGES:
        c_u_dag_c_v = bilinears[(v, u)]
        c_v_dag_c_u = bilinears[(u, v)]
        hops.append(c_u_dag_c_v + c_v_dag_c_u)
        currents.append(1j * (c_u_dag_c_v - c_v_dag_c_u))
    numbers = [bilinears[(site, site)] for site in range(VERTICES)]
    return basis, hops, currents, numbers, bilinears


def build_one_particle_operators() -> tuple[list[np.ndarray], list[np.ndarray]]:
    hops: list[np.ndarray] = []
    currents: list[np.ndarray] = []
    for u, v in EDGES:
        hop = np.zeros((VERTICES, VERTICES), dtype=np.complex128)
        hop[u, v] = 1.0
        hop[v, u] = 1.0
        current = np.zeros_like(hop)
        current[u, v] = 1j
        current[v, u] = -1j
        hops.append(hop)
        currents.append(current)
    return hops, currents


def hamiltonian(hops: list[np.ndarray], live_mask: int) -> np.ndarray:
    result = np.zeros_like(hops[0])
    for edge, hop in enumerate(hops):
        if (live_mask >> edge) & 1:
            result += COEFFICIENTS[edge] * hop
    return result


def spectrum(operator: np.ndarray) -> Spectrum:
    values, vectors = eigh(operator)
    return Spectrum(values=values, vectors=vectors)


def unitary(operator_spectrum: Spectrum, dwell: float) -> np.ndarray:
    vectors = operator_spectrum.vectors
    return (vectors * np.exp(-1j * dwell * operator_spectrum.values)) @ vectors.conj().T


def packet_mean(width: float) -> float:
    return BATTERY_PACKET_LOW + 0.5 * width


def packet_cap_high(width: float) -> float:
    return 2.0 * BATTERY_PACKET_LOW + width


def packet_overlap(delta: np.ndarray | float, width: float) -> np.ndarray | float:
    """<beta_{u'}|beta_u> for delta=u-u' and a width-w sine packet."""
    array = np.asarray(delta, dtype=float)
    distance = np.abs(array) / width
    result = np.zeros_like(distance)
    inside = distance < 1.0
    x = distance[inside]
    result[inside] = (1.0 - x) * np.cos(np.pi * x) + np.sin(np.pi * x) / np.pi
    if result.ndim == 0:
        return float(result)
    return result


def battery_energy_kernel(u: np.ndarray, u_prime: np.ndarray, width: float) -> np.ndarray:
    """Evaluate <beta_u'|H_B|beta_u> from the shifted-packet integral."""
    return (packet_mean(width) + 0.5 * (u + u_prime)) * packet_overlap(
        u - u_prime, width
    )


def packet_value(energy: np.ndarray, shift: float, width: float) -> np.ndarray:
    coordinate = energy - shift - BATTERY_PACKET_LOW
    inside = (coordinate >= 0.0) & (coordinate <= width)
    result = np.zeros_like(energy)
    result[inside] = math.sqrt(2.0 / width) * np.sin(
        np.pi * coordinate[inside] / width
    )
    return result


def quadrature_packet_element(
    u_left: float, u_right: float, power: int, order: int, width: float
) -> float:
    lower = max(BATTERY_PACKET_LOW + u_left, BATTERY_PACKET_LOW + u_right)
    upper = min(
        BATTERY_PACKET_LOW + width + u_left,
        BATTERY_PACKET_LOW + width + u_right,
    )
    if upper <= lower:
        return 0.0
    nodes, weights = leggauss(order)
    energies = lower + 0.5 * (upper - lower) * (nodes + 1.0)
    jacobian = 0.5 * (upper - lower)
    integrand = packet_value(energies, u_left, width) * packet_value(
        energies, u_right, width
    )
    if power:
        integrand *= energies**power
    return float(jacobian * np.dot(weights, integrand))


def one_particle_reduced_state(
    gamma_zero: np.ndarray,
    ideal_map: np.ndarray,
    initial_spectrum: Spectrum,
    output_spectrum: Spectrum,
    packet_width: float,
) -> np.ndarray:
    """Exact battery trace through compact-support packet overlaps.

    This is the finite-frequency evaluation of
      integral p(tau) V_tau gamma_zero V_tau^dagger d tau,
    V_tau=exp(-i tau h_out) ideal_map exp(i tau h_zero).
    It makes no stationarity assumption about gamma_zero.
    """
    v_zero = initial_spectrum.vectors
    v_out = output_spectrum.vectors
    map_energy = v_out.conj().T @ ideal_map @ v_zero
    gamma_energy = v_zero.conj().T @ gamma_zero @ v_zero
    transfers = initial_spectrum.values[None, :] - output_spectrum.values[:, None]
    dimension = len(initial_spectrum.values)
    output_energy = np.empty((dimension, dimension), dtype=np.complex128)
    for b in range(dimension):
        delta = transfers[b][None, :, None] - transfers[:, None, :]
        kernel = packet_overlap(delta, packet_width)
        base = map_energy[b, :, None] * gamma_energy
        weighted = kernel * base[None, :, :] * map_energy.conj()[:, None, :]
        output_energy[b, :] = np.sum(weighted, axis=(1, 2))
    return v_out @ output_energy @ v_out.conj().T


def full_reduced_state_and_battery(
    rho_zero: np.ndarray,
    ideal_map: np.ndarray,
    initial_spectrum: Spectrum,
    output_spectrum: Spectrum,
    packet_width: float,
) -> tuple[np.ndarray, complex, float, float, float]:
    """Trace the same retained battery in the 70-dimensional N=4 sector.

    The battery mean is accumulated directly with
    <beta_u'|H_B|beta_u>; it is never defined by subtracting matter energy
    from a conserved scalar ledger.
    """
    v_zero = initial_spectrum.vectors
    v_out = output_spectrum.vectors
    map_energy = v_out.conj().T @ ideal_map @ v_zero
    rho_energy = v_zero.conj().T @ rho_zero @ v_zero
    transfers = initial_spectrum.values[None, :] - output_spectrum.values[:, None]
    dimension = len(initial_spectrum.values)
    output_energy = np.empty((dimension, dimension), dtype=np.complex128)
    battery_mean = 0.0j
    for b in range(dimension):
        base = map_energy[b, :, None] * rho_energy
        # Chunk the output-energy bra index.  This keeps the largest temporary
        # far below the 70^3 tensor while evaluating the identical contraction.
        for start in range(0, dimension, 8):
            stop = min(start + 8, dimension)
            delta = (
                transfers[b][None, :, None]
                - transfers[start:stop, None, :]
            )
            kernel = packet_overlap(delta, packet_width)
            weighted = (
                kernel
                * base[None, :, :]
                * map_energy.conj()[start:stop, None, :]
            )
            output_energy[b, start:stop] = np.sum(weighted, axis=(1, 2))

        coefficient = base * map_energy[b].conj()[None, :]
        u = transfers[b]
        energy_matrix = battery_energy_kernel(
            u[:, None], u[None, :], packet_width
        )
        battery_mean += np.sum(coefficient * energy_matrix)

    result = v_out @ output_energy @ v_out.conj().T
    norm_residual = abs(float(np.trace(result).real) - 1.0) + abs(float(np.trace(result).imag))

    active = np.abs(map_energy) > 2.0e-12
    if np.any(active):
        active_transfers = transfers[active]
        minimum_packet = BATTERY_PACKET_LOW + float(np.min(active_transfers))
        maximum_packet = (
            BATTERY_PACKET_LOW + packet_width + float(np.max(active_transfers))
        )
    else:
        minimum_packet = math.inf
        maximum_packet = -math.inf
    return result, complex(battery_mean), norm_residual, minimum_packet, maximum_packet


def slater_state(basis: tuple[int, ...], occupied_orbitals: np.ndarray) -> np.ndarray:
    state = np.empty(len(basis), dtype=np.complex128)
    for position, bits in enumerate(basis):
        occupied_sites = [site for site in range(VERTICES) if (bits >> site) & 1]
        state[position] = np.linalg.det(occupied_orbitals[occupied_sites, :])
    return state / np.linalg.norm(state)


def component_count(live_mask: int) -> int:
    adjacency = [[] for _ in range(VERTICES)]
    for edge, (u, v) in enumerate(EDGES):
        if (live_mask >> edge) & 1:
            adjacency[u].append(v)
            adjacency[v].append(u)
    unseen = set(range(VERTICES))
    count = 0
    while unseen:
        count += 1
        stack = [unseen.pop()]
        while stack:
            vertex = stack.pop()
            for neighbor in adjacency[vertex]:
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    stack.append(neighbor)
    return count


def alternate_path_exists(live_mask: int, excluded_edge: int) -> bool:
    source, target = EDGES[excluded_edge]
    adjacency = [[] for _ in range(VERTICES)]
    for edge, (u, v) in enumerate(EDGES):
        if edge == excluded_edge or not ((live_mask >> edge) & 1):
            continue
        adjacency[u].append(v)
        adjacency[v].append(u)
    seen = {source}
    stack = [source]
    while stack:
        vertex = stack.pop()
        if vertex == target:
            return True
        for neighbor in adjacency[vertex]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)
    return False


def observable_rows(
    gamma: np.ndarray,
    one_currents: list[np.ndarray],
    live_mask: int,
) -> tuple[tuple[float, ...], tuple[tuple[int, float], ...], int]:
    densities = tuple(float(gamma[site, site].real) for site in range(VERTICES))
    currents: list[tuple[int, float]] = []
    for edge, operator in enumerate(one_currents):
        if (live_mask >> edge) & 1:
            value = COEFFICIENTS[edge] * float(np.trace(operator @ gamma).real)
            currents.append((edge, value))
    support = sum(abs(value) >= CURRENT_FLOOR for _, value in currents)
    return densities, tuple(currents), support


def format_surface(surface: Surface) -> str:
    aliases = {
        "CONTROL_PRE": "CP",
        "CONTROL_POST": "CO",
        "FREE_PRE": "FP",
        "FREE_POST": "FO",
    }
    density_text = ",".join(f"{value:.4f}" for value in surface.densities)
    current_text = ",".join(f"{value:+.4f}" for _edge, value in surface.currents)
    return (
        f"{aliases[surface.label]}{surface.step} e{surface.edge} "
        f"E={surface.matter_energy:+.5f} B={surface.battery_energy:.5f} S={surface.support} "
        f"n={density_text} j={current_text}"
    )


def main() -> int:
    if sys.argv[1:] not in ([], ["--json"]):
        raise SystemExit("usage: independent_check.py [--json]")
    json_output = sys.argv[1:] == ["--json"]
    started = time.perf_counter()
    report = Report()
    full_mask = (1 << len(EDGES)) - 1

    basis, many_hops, many_currents, numbers, bilinears = build_fixed_number_operators()
    one_hops, one_currents = build_one_particle_operators()
    report.check(
        "fixture",
        "fixed-N sector and frozen fixture",
        len(basis) == math.comb(VERTICES, PARTICLES)
        and len(EXPECTED_ORDER) == EVENTS
        and len(DWELLS) == EVENTS,
        f"dim={len(basis)} order={EXPECTED_ORDER} dwells={DWELLS}",
    )

    live_mask = full_mask
    topology_ok = True
    component_prefixes = [component_count(live_mask)]
    for edge in EXPECTED_ORDER:
        topology_ok &= bool((live_mask >> edge) & 1)
        topology_ok &= alternate_path_exists(live_mask, edge)
        live_mask &= ~(1 << edge)
        component_prefixes.append(component_count(live_mask))
    report.check(
        "topology",
        "all fixed events are nonbridges",
        topology_ok and component_prefixes == [1] * (EVENTS + 1),
        f"components={component_prefixes}; branch weights 1/{2 ** EVENTS} follow analytically "
        "from the inherited normalized nonbridge isometries",
    )

    initial_one = hamiltonian(one_hops, full_mask)
    initial_many = hamiltonian(many_hops, full_mask)
    initial_one_spectrum = spectrum(initial_one)
    initial_many_spectrum = spectrum(initial_many)

    occupied = initial_one_spectrum.vectors[:, :PARTICLES]
    pulse = np.eye(VERTICES, dtype=np.complex128)
    pulse[0, 0] = np.exp(-1j * BOOST_PHASE)
    pulse[1, 1] = np.exp(1j * BOOST_PHASE)
    pulsed_orbitals = pulse @ occupied
    gamma_zero = pulsed_orbitals @ pulsed_orbitals.conj().T
    state_zero = slater_state(basis, pulsed_orbitals)
    rho_zero = np.outer(state_zero, state_zero.conj())

    gamma_from_sector = np.empty_like(gamma_zero)
    for u in range(VERTICES):
        for v in range(VERTICES):
            gamma_from_sector[u, v] = np.vdot(state_zero, bilinears[(u, v)] @ state_zero)
    initial_representation_residual = float(np.max(np.abs(gamma_zero - gamma_from_sector)))
    initial_energy_one = float(np.trace(initial_one @ gamma_zero).real)
    initial_energy_many = float(np.trace(initial_many @ rho_zero).real)
    nonstationarity = float(np.linalg.norm(initial_many @ rho_zero - rho_zero @ initial_many))
    ground_gap = float(initial_one_spectrum.values[PARTICLES] - initial_one_spectrum.values[PARTICLES - 1])
    report.check(
        "preparation",
        "independent Slater/CAR preparation is nonstationary",
        initial_representation_residual <= TOL
        and abs(initial_energy_one - initial_energy_many) <= TOL
        and nonstationarity > 1.0e-6
        and ground_gap > TOL,
        f"one_vs_N4={initial_representation_residual:.3e} energy_diff={abs(initial_energy_one-initial_energy_many):.3e} "
        f"commutator={nonstationarity:.3e} half_fill_gap={ground_gap:.6f}",
    )

    one_spectra: dict[int, Spectrum] = {full_mask: initial_one_spectrum}
    many_spectra: dict[int, Spectrum] = {full_mask: initial_many_spectrum}
    many_hamiltonians: dict[int, np.ndarray] = {full_mask: initial_many}
    one_hamiltonians: dict[int, np.ndarray] = {full_mask: initial_one}

    def get_operators(mask: int) -> tuple[np.ndarray, np.ndarray, Spectrum, Spectrum]:
        if mask not in one_hamiltonians:
            one_hamiltonians[mask] = hamiltonian(one_hops, mask)
            many_hamiltonians[mask] = hamiltonian(many_hops, mask)
            one_spectra[mask] = spectrum(one_hamiltonians[mask])
            many_spectra[mask] = spectrum(many_hamiltonians[mask])
        return (
            one_hamiltonians[mask],
            many_hamiltonians[mask],
            one_spectra[mask],
            many_spectra[mask],
        )

    control_surfaces: list[Surface] = []
    free_surfaces: list[Surface] = []
    a_one = np.eye(VERTICES, dtype=np.complex128)
    a_many = np.eye(len(basis), dtype=np.complex128)
    live_mask = full_mask
    maximum_representation_residual = 0.0
    maximum_density_current_residual = 0.0
    maximum_total_energy_residual = 0.0
    maximum_state_defect = 0.0
    maximum_gamma_hermiticity = 0.0
    maximum_battery_imaginary = 0.0
    first_pre_control_residual = math.inf
    first_pre_free_residual = math.inf
    first_pre_battery_residual = math.inf
    first_pre_free_battery_residual = math.inf
    transfer_samples: list[float] = []

    for step, (edge, dwell) in enumerate(zip(EXPECTED_ORDER, DWELLS), start=1):
        h_in_one, h_in_many, spec_in_one, spec_in_many = get_operators(live_mask)
        u_one = unitary(spec_in_one, dwell)
        u_many = unitary(spec_in_many, dwell)
        a_one = u_one @ a_one
        a_many = u_many @ a_many

        for label, surface_mask in (
            ("CONTROL_PRE", live_mask),
            ("CONTROL_POST", live_mask & ~(1 << edge)),
        ):
            h_surface_one, h_surface_many, spec_surface_one, spec_surface_many = get_operators(surface_mask)
            gamma = one_particle_reduced_state(
                gamma_zero,
                a_one,
                initial_one_spectrum,
                spec_surface_one,
                BASELINE_WIDTH,
            )
            rho_many, battery_energy_raw, norm_residual, minimum_packet, maximum_packet = (
                full_reduced_state_and_battery(
                    rho_zero,
                    a_many,
                    initial_many_spectrum,
                    spec_surface_many,
                    BASELINE_WIDTH,
                )
            )
            battery_energy = float(battery_energy_raw.real)
            maximum_battery_imaginary = max(
                maximum_battery_imaginary, abs(battery_energy_raw.imag)
            )
            maximum_gamma_hermiticity = max(
                maximum_gamma_hermiticity,
                float(np.max(np.abs(gamma - gamma.conj().T))),
            )
            matter_energy_one = float(np.trace(h_surface_one @ gamma).real)
            matter_energy_many = float(np.trace(h_surface_many @ rho_many).real)
            maximum_representation_residual = max(
                maximum_representation_residual, abs(matter_energy_one - matter_energy_many)
            )

            densities, currents, support = observable_rows(gamma, one_currents, surface_mask)
            sector_densities = tuple(float(np.trace(number @ rho_many).real) for number in numbers)
            sector_currents = {
                index: COEFFICIENTS[index] * float(np.trace(operator @ rho_many).real)
                for index, operator in enumerate(many_currents)
                if (surface_mask >> index) & 1
            }
            maximum_density_current_residual = max(
                maximum_density_current_residual,
                max(abs(a - b) for a, b in zip(densities, sector_densities)),
                max(abs(value - sector_currents[index]) for index, value in currents),
            )
            raw_hermiticity = float(np.max(np.abs(rho_many - rho_many.conj().T)))
            eig_rho = np.linalg.eigvalsh(0.5 * (rho_many + rho_many.conj().T))
            state_defect = max(
                norm_residual,
                float(max(0.0, -np.min(eig_rho))),
                raw_hermiticity,
            )
            maximum_state_defect = max(maximum_state_defect, state_defect)
            total_residual = abs(
                matter_energy_many
                + battery_energy
                - (initial_energy_many + packet_mean(BASELINE_WIDTH))
            )
            maximum_total_energy_residual = max(maximum_total_energy_residual, total_residual)

            map_energy = spec_surface_many.vectors.conj().T @ a_many @ initial_many_spectrum.vectors
            transfer_matrix = (
                initial_many_spectrum.values[None, :] - spec_surface_many.values[:, None]
            )
            active_transfers = transfer_matrix[np.abs(map_energy) > 2.0e-12]
            if active_transfers.size:
                quantile_indices = np.linspace(0, active_transfers.size - 1, 6, dtype=int)
                transfer_samples.extend(np.sort(active_transfers)[quantile_indices].tolist())

            surface = Surface(
                label=label,
                step=step,
                edge=edge,
                live_mask=surface_mask,
                matter_energy=matter_energy_one,
                ground_energy=float(np.min(spec_surface_many.values)),
                battery_energy=battery_energy,
                number_trace=float(np.trace(gamma).real),
                system_norm=float(np.max(np.abs(spec_surface_many.values))),
                min_packet_energy=minimum_packet,
                max_packet_energy=maximum_packet,
                densities=densities,
                currents=currents,
                support=support,
                packet_width=BASELINE_WIDTH,
            )
            control_surfaces.append(surface)

            if step == 1 and label == "CONTROL_PRE":
                ideal_first_pre = u_one @ gamma_zero @ u_one.conj().T
                first_pre_control_residual = float(np.max(np.abs(gamma - ideal_first_pre)))
                first_pre_battery_residual = abs(
                    battery_energy - packet_mean(BASELINE_WIDTH)
                )

        live_mask &= ~(1 << edge)

    # Separately preregistered laboratory-free comparison.  Total free dwells
    # can be pushed through all earlier energy-intertwining lifts.  At either
    # surface of step j the endpoint ideal map is exp(-i t_j H_surface), where
    # t_j is the cumulative supplied dwell time.  This is not a retuning of
    # the CONTROL protocol above.
    live_mask = full_mask
    cumulative_time = 0.0
    for step, (edge, dwell) in enumerate(zip(EXPECTED_ORDER, DWELLS), start=1):
        cumulative_time += dwell
        for label, surface_mask in (
            ("FREE_PRE", live_mask),
            ("FREE_POST", live_mask & ~(1 << edge)),
        ):
            h_surface_one, h_surface_many, spec_surface_one, spec_surface_many = get_operators(surface_mask)
            free_a_one = unitary(spec_surface_one, cumulative_time)
            free_a_many = unitary(spec_surface_many, cumulative_time)
            gamma = one_particle_reduced_state(
                gamma_zero,
                free_a_one,
                initial_one_spectrum,
                spec_surface_one,
                BASELINE_WIDTH,
            )
            rho_many, battery_energy_raw, norm_residual, minimum_packet, maximum_packet = (
                full_reduced_state_and_battery(
                    rho_zero,
                    free_a_many,
                    initial_many_spectrum,
                    spec_surface_many,
                    BASELINE_WIDTH,
                )
            )
            battery_energy = float(battery_energy_raw.real)
            maximum_battery_imaginary = max(
                maximum_battery_imaginary, abs(battery_energy_raw.imag)
            )
            maximum_gamma_hermiticity = max(
                maximum_gamma_hermiticity,
                float(np.max(np.abs(gamma - gamma.conj().T))),
            )
            matter_energy_one = float(np.trace(h_surface_one @ gamma).real)
            matter_energy_many = float(np.trace(h_surface_many @ rho_many).real)
            maximum_representation_residual = max(
                maximum_representation_residual, abs(matter_energy_one - matter_energy_many)
            )

            densities, currents, support = observable_rows(gamma, one_currents, surface_mask)
            sector_densities = tuple(float(np.trace(number @ rho_many).real) for number in numbers)
            sector_currents = {
                index: COEFFICIENTS[index] * float(np.trace(operator @ rho_many).real)
                for index, operator in enumerate(many_currents)
                if (surface_mask >> index) & 1
            }
            maximum_density_current_residual = max(
                maximum_density_current_residual,
                max(abs(a - b) for a, b in zip(densities, sector_densities)),
                max(abs(value - sector_currents[index]) for index, value in currents),
            )
            raw_hermiticity = float(np.max(np.abs(rho_many - rho_many.conj().T)))
            eig_rho = np.linalg.eigvalsh(0.5 * (rho_many + rho_many.conj().T))
            state_defect = max(
                norm_residual,
                float(max(0.0, -np.min(eig_rho))),
                raw_hermiticity,
            )
            maximum_state_defect = max(maximum_state_defect, state_defect)
            total_residual = abs(
                matter_energy_many
                + battery_energy
                - (initial_energy_many + packet_mean(BASELINE_WIDTH))
            )
            maximum_total_energy_residual = max(maximum_total_energy_residual, total_residual)

            map_energy = (
                spec_surface_many.vectors.conj().T
                @ free_a_many
                @ initial_many_spectrum.vectors
            )
            transfer_matrix = (
                initial_many_spectrum.values[None, :] - spec_surface_many.values[:, None]
            )
            active_transfers = transfer_matrix[np.abs(map_energy) > 2.0e-12]
            if active_transfers.size:
                quantile_indices = np.linspace(0, active_transfers.size - 1, 6, dtype=int)
                transfer_samples.extend(np.sort(active_transfers)[quantile_indices].tolist())

            surface = Surface(
                label=label,
                step=step,
                edge=edge,
                live_mask=surface_mask,
                matter_energy=matter_energy_one,
                ground_energy=float(np.min(spec_surface_many.values)),
                battery_energy=battery_energy,
                number_trace=float(np.trace(gamma).real),
                system_norm=float(np.max(np.abs(spec_surface_many.values))),
                min_packet_energy=minimum_packet,
                max_packet_energy=maximum_packet,
                densities=densities,
                currents=currents,
                support=support,
                packet_width=BASELINE_WIDTH,
            )
            free_surfaces.append(surface)

            if step == 1 and label == "FREE_PRE":
                ideal_first_pre = free_a_one @ gamma_zero @ free_a_one.conj().T
                first_pre_free_residual = float(np.max(np.abs(gamma - ideal_first_pre)))
                first_pre_free_battery_residual = abs(
                    battery_energy - packet_mean(BASELINE_WIDTH)
                )

        live_mask &= ~(1 << edge)

    # Preregistered controlled-packet resource variants.  They use the same
    # ordered CONTROL maps and frozen fixture; only the sine-packet width,
    # mean, and safe cap change.  Detailed rows remain reserved for width one.
    wide_surfaces: dict[float, list[Surface]] = {}
    for packet_width in WIDE_WIDTHS:
        variant_surfaces: list[Surface] = []
        a_one = np.eye(VERTICES, dtype=np.complex128)
        a_many = np.eye(len(basis), dtype=np.complex128)
        live_mask = full_mask
        for step, (edge, dwell) in enumerate(zip(EXPECTED_ORDER, DWELLS), start=1):
            _h_in_one, _h_in_many, spec_in_one, spec_in_many = get_operators(live_mask)
            a_one = unitary(spec_in_one, dwell) @ a_one
            a_many = unitary(spec_in_many, dwell) @ a_many
            for suffix, surface_mask in (
                ("PRE", live_mask),
                ("POST", live_mask & ~(1 << edge)),
            ):
                h_surface_one, h_surface_many, spec_surface_one, spec_surface_many = get_operators(
                    surface_mask
                )
                gamma = one_particle_reduced_state(
                    gamma_zero,
                    a_one,
                    initial_one_spectrum,
                    spec_surface_one,
                    packet_width,
                )
                (
                    rho_many,
                    battery_energy_raw,
                    norm_residual,
                    minimum_packet,
                    maximum_packet,
                ) = full_reduced_state_and_battery(
                    rho_zero,
                    a_many,
                    initial_many_spectrum,
                    spec_surface_many,
                    packet_width,
                )
                battery_energy = float(battery_energy_raw.real)
                maximum_battery_imaginary = max(
                    maximum_battery_imaginary, abs(battery_energy_raw.imag)
                )
                maximum_gamma_hermiticity = max(
                    maximum_gamma_hermiticity,
                    float(np.max(np.abs(gamma - gamma.conj().T))),
                )
                matter_energy_one = float(np.trace(h_surface_one @ gamma).real)
                matter_energy_many = float(np.trace(h_surface_many @ rho_many).real)
                maximum_representation_residual = max(
                    maximum_representation_residual,
                    abs(matter_energy_one - matter_energy_many),
                )

                densities, currents, support = observable_rows(
                    gamma, one_currents, surface_mask
                )
                sector_densities = tuple(
                    float(np.trace(number @ rho_many).real) for number in numbers
                )
                sector_currents = {
                    index: COEFFICIENTS[index]
                    * float(np.trace(operator @ rho_many).real)
                    for index, operator in enumerate(many_currents)
                    if (surface_mask >> index) & 1
                }
                maximum_density_current_residual = max(
                    maximum_density_current_residual,
                    max(abs(a - b) for a, b in zip(densities, sector_densities)),
                    max(
                        abs(value - sector_currents[index])
                        for index, value in currents
                    ),
                )
                raw_hermiticity = float(
                    np.max(np.abs(rho_many - rho_many.conj().T))
                )
                eig_rho = np.linalg.eigvalsh(
                    0.5 * (rho_many + rho_many.conj().T)
                )
                maximum_state_defect = max(
                    maximum_state_defect,
                    norm_residual,
                    float(max(0.0, -np.min(eig_rho))),
                    raw_hermiticity,
                )
                maximum_total_energy_residual = max(
                    maximum_total_energy_residual,
                    abs(
                        matter_energy_many
                        + battery_energy
                        - (initial_energy_many + packet_mean(packet_width))
                    ),
                )
                variant_surfaces.append(
                    Surface(
                        label=f"CONTROL{int(packet_width)}_{suffix}",
                        step=step,
                        edge=edge,
                        live_mask=surface_mask,
                        matter_energy=matter_energy_one,
                        ground_energy=float(np.min(spec_surface_many.values)),
                        battery_energy=battery_energy,
                        number_trace=float(np.trace(gamma).real),
                        system_norm=float(np.max(np.abs(spec_surface_many.values))),
                        min_packet_energy=minimum_packet,
                        max_packet_energy=maximum_packet,
                        densities=densities,
                        currents=currents,
                        support=support,
                        packet_width=packet_width,
                    )
                )
            live_mask &= ~(1 << edge)
        wide_surfaces[packet_width] = variant_surfaces

    surfaces = control_surfaces + free_surfaces + [
        surface
        for packet_width in WIDE_WIDTHS
        for surface in wide_surfaces[packet_width]
    ]

    report.check(
        "reduction",
        "arbitrary-nonstationary retained-battery reductions",
        maximum_state_defect <= TOL
        and maximum_gamma_hermiticity <= TOL
        and maximum_battery_imaginary <= TOL
        and maximum_representation_residual <= TOL
        and maximum_density_current_residual <= TOL,
        f"state={maximum_state_defect:.3e} gamma_H={maximum_gamma_hermiticity:.3e} "
        f"battery_im={maximum_battery_imaginary:.3e} N4_vs_1p_E={maximum_representation_residual:.3e} "
        f"N4_vs_1p_obs={maximum_density_current_residual:.3e}",
    )
    report.check(
        "first-pre",
        "first dwell is pre-event in both declared conventions",
        first_pre_control_residual <= TOL
        and first_pre_free_residual <= TOL
        and first_pre_battery_residual <= TOL
        and first_pre_free_battery_residual <= TOL,
        f"control={first_pre_control_residual:.3e} free={first_pre_free_residual:.3e} "
        f"battery={max(first_pre_battery_residual,first_pre_free_battery_residual):.3e}",
    )

    selected = np.asarray(transfer_samples, dtype=float)
    if selected.size:
        selected = np.quantile(selected, np.linspace(0.0, 1.0, 9))
    else:
        selected = np.array([0.0])
    max_overlap_error_32 = 0.0
    max_overlap_convergence = 0.0
    max_energy_error_32 = 0.0
    max_energy_convergence = 0.0
    for packet_width in (BASELINE_WIDTH,) + WIDE_WIDTHS:
        for u_left in selected:
            for u_right in selected:
                analytic_overlap = float(
                    packet_overlap(u_right - u_left, packet_width)
                )
                analytic_energy = float(
                    battery_energy_kernel(
                        np.asarray(u_right), np.asarray(u_left), packet_width
                    )
                )
                overlap_32 = quadrature_packet_element(
                    u_left, u_right, power=0, order=32, width=packet_width
                )
                overlap_64 = quadrature_packet_element(
                    u_left, u_right, power=0, order=64, width=packet_width
                )
                energy_32 = quadrature_packet_element(
                    u_left, u_right, power=1, order=32, width=packet_width
                )
                energy_64 = quadrature_packet_element(
                    u_left, u_right, power=1, order=64, width=packet_width
                )
                max_overlap_error_32 = max(
                    max_overlap_error_32, abs(overlap_32 - analytic_overlap)
                )
                max_overlap_convergence = max(
                    max_overlap_convergence, abs(overlap_64 - overlap_32)
                )
                max_energy_error_32 = max(
                    max_energy_error_32, abs(energy_32 - analytic_energy)
                )
                max_energy_convergence = max(
                    max_energy_convergence, abs(energy_64 - energy_32)
                )
    report.check(
        "packet",
        "piecewise energy-domain sine-packet integration",
        max_overlap_error_32 <= QUADRATURE_TOL
        and max_overlap_convergence <= QUADRATURE_TOL
        and max_energy_error_32 <= QUADRATURE_TOL
        and max_energy_convergence <= QUADRATURE_TOL,
        f"overlap_error={max_overlap_error_32:.3e} overlap_32v64={max_overlap_convergence:.3e} "
        f"energy_error={max_energy_error_32:.3e} energy_32v64={max_energy_convergence:.3e}",
    )

    cap_low = min(surface.min_packet_energy for surface in surfaces)
    maximum_system_norm = max(surface.system_norm for surface in surfaces)
    minimum_cap_margin = min(
        packet_cap_high(surface.packet_width) - surface.max_packet_energy
        for surface in surfaces
    )
    cap_ok = (
        maximum_system_norm <= SYSTEM_BOUND + TOL
        and cap_low >= BATTERY_CAP_LOW - TOL
        and minimum_cap_margin >= -TOL
        and all(
            BATTERY_CAP_LOW - TOL
            <= surface.battery_energy
            <= packet_cap_high(surface.packet_width) + TOL
            for surface in surfaces
        )
    )
    report.check(
        "energy",
        "direct battery energy, shift sign, cap, and conservation",
        cap_ok and maximum_total_energy_residual <= TOL,
        f"min_packet={cap_low:.6f} min_cap_margin={minimum_cap_margin:.6f} "
        f"max_system_norm={maximum_system_norm:.6f} total_drift={maximum_total_energy_residual:.3e}",
    )

    trace_number_residual = max(abs(surface.number_trace - PARTICLES) for surface in surfaces)
    report.check(
        "number",
        "sharp fixed number on every reduced surface",
        trace_number_residual <= TOL,
        f"max_number_residual={trace_number_residual:.3e}; histories={2 ** EVENTS} with "
        f"analytic inherited weight={2.0 ** (-EVENTS):.8f}; records persist by branch isometry",
    )

    report.lines.append("BENCHMARK rows are measured physics outcomes and are excluded from TOTAL")
    report.lines.extend(
        format_surface(surface) for surface in control_surfaces + free_surfaces
    )

    protocol_sets = [("CONTROL1", control_surfaces), ("FREE1", free_surfaces)] + [
        (f"CONTROL{int(packet_width)}", wide_surfaces[packet_width])
        for packet_width in WIDE_WIDTHS
    ]
    for protocol, protocol_surfaces in protocol_sets:
        pre_surfaces = [surface for surface in protocol_surfaces if surface.label.endswith("_PRE")]
        post_surfaces = [surface for surface in protocol_surfaces if surface.label.endswith("_POST")]
        min_pre_support = min(surface.support for surface in pre_surfaces)
        min_post_support = min(surface.support for surface in post_surfaces)
        maximum_front_current = max(
            abs(dict(surface.currents)[surface.edge]) for surface in pre_surfaces
        )
        minimum_density = min(min(surface.densities) for surface in protocol_surfaces)
        maximum_density = max(max(surface.densities) for surface in protocol_surfaces)
        maximum_post_energy = max(surface.matter_energy for surface in post_surfaces)
        minimum_excess = min(
            surface.matter_energy - surface.ground_energy
            for surface in post_surfaces
        )
        science_transport = (
            min_pre_support >= 4
            and minimum_density >= DENSITY_LOW
            and maximum_density <= DENSITY_HIGH
            and maximum_front_current >= FRONT_FLOOR
            and maximum_post_energy < 0.0
            and minimum_excess >= -TOL
        )
        packet_width = protocol_surfaces[0].packet_width
        report.lines.append(
            f"BENCHMARK {protocol} originalgate={'PASS' if science_transport else 'FAIL'} "
            f"preS={[surface.support for surface in pre_surfaces]} "
            f"postS={[surface.support for surface in post_surfaces]} "
            f"postgate={'PASS' if min_post_support >= 4 else 'FAIL'} front={maximum_front_current:.6f} "
            f"rho=[{minimum_density:.6f},{maximum_density:.6f}] "
            f"postEmax={maximum_post_energy:+.6f} excess={minimum_excess:.6f} "
            f"resource=w{packet_width:g}/mean{packet_mean(packet_width):g}/cap{packet_cap_high(packet_width):g} "
            f"finalB={post_surfaces[-1].battery_energy:.6f}"
        )
    report.lines.append(
        "LEGEND CP/CO=CONTROL1 pre/post; FP/FO=FREE1 pre/post; j values follow ascending live-edge indices. "
        "SCOPE CONTROL uses supplied D_j tensor I_B; FREE uses laboratory H_j+H_B dwell; "
        "both are fixed conditional fixtures, not formation, renewal, or autonomy"
    )

    elapsed = time.perf_counter() - started
    rss = float(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    if os.uname().sysname == "Darwin":
        rss /= 1024.0 * 1024.0
    else:
        rss /= 1024.0
    report.check(
        "envelope",
        "execution envelope",
        elapsed < TIME_LIMIT_SECONDS and rss < RSS_LIMIT_MIB,
        f"elapsed={elapsed:.2f}s rss={rss:.1f}MiB limits={TIME_LIMIT_SECONDS:.0f}s/{RSS_LIMIT_MIB:.0f}MiB",
    )
    report.lines.append(f"TOTAL: PASS={report.passes} FAIL={report.failures}")
    if json_output:
        payload = {
            "schema": "shared-battery-surfaces-v1",
            "validation_ok": report.failures == 0,
            "surfaces": [
                {
                    "protocol": "free" if surface.label.startswith("FREE") else "controlled",
                    "width": surface.packet_width,
                    "step": surface.step,
                    "edge": surface.edge,
                    "side": "pre" if surface.label.endswith("_PRE") else "post",
                    "resource": {"low": BATTERY_PACKET_LOW,
                                 "mean": packet_mean(surface.packet_width),
                                 "cap": packet_cap_high(surface.packet_width)},
                    "densities": list(surface.densities),
                    "currents": {str(edge): value for edge, value in surface.currents},
                    "matter_energy": surface.matter_energy,
                    "battery_energy": surface.battery_energy,
                    "support": surface.support,
                }
                for surface in surfaces
            ],
        }
        print(json.dumps(payload, allow_nan=False))
    else:
        print("\n".join(report.lines))
    return 1 if report.failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
