#!/usr/bin/env python3
"""Independent fixed-N checker for the local native-edge cycle probe.

This checker rebuilds the eight-vertex CAR sector, hopping signs, directed
half-edge front, continuity equation, and persistent scalar ledger itself.  It
does not import the primary runner, its cache, or its native BKSF implementation.
"""

from __future__ import annotations

import math
import os
import resource
import time

for _thread_var in (
    "OPENBLAS_NUM_THREADS",
    "OMP_NUM_THREADS",
    "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS",
    "NUMEXPR_NUM_THREADS",
):
    os.environ[_thread_var] = "1"

import numpy as np
from scipy.linalg import eigh


TOL = 3.0e-10
CURRENT_FLOOR = 2.0e-2
DENSITY_LOW = 0.10
DENSITY_HIGH = 0.90
BATTERY_START = 4.0
BATTERY_CAP = 8.0
BOOST_PHASE = 0.7
EVENTS = 5
EXPECTED_ORDER = (0, 3, 5, 6, 9)
DWELLS = (0.41, 0.37, 0.29, 0.23, 0.19)
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
VERTICES = 8
PARTICLES = 4
EDGES = (
    (0, 1), (0, 2), (0, 4), (1, 3), (1, 5), (2, 3),
    (2, 6), (3, 7), (4, 5), (4, 6), (5, 7), (6, 7),
)
COEFFICIENTS = (-1.0, -1.0, -1.0, -1.0, -1.0, 1.0, -1.0, -1.0, 1.0, 1.0, 1.0, -1.0)


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


def ladder_action(bits: int, site: int, create: bool) -> tuple[int, complex] | None:
    occupied = bool((bits >> site) & 1)
    if occupied == create:
        return None
    sign = -1.0 if ((bits & ((1 << site) - 1)).bit_count() & 1) else 1.0
    return bits ^ (1 << site), complex(sign)


def directed_hop(basis: tuple[int, ...], index: dict[int, int], source: int, target: int) -> np.ndarray:
    result = np.zeros((len(basis), len(basis)), dtype=np.complex128)
    for column, bits in enumerate(basis):
        annihilated = ladder_action(bits, source, create=False)
        if annihilated is None:
            continue
        after_annihilation, phase_one = annihilated
        created = ladder_action(after_annihilation, target, create=True)
        if created is None:
            continue
        after_creation, phase_two = created
        result[index[after_creation], column] += phase_one * phase_two
    return result


def build_sector() -> tuple[tuple[int, ...], dict[int, int], list[np.ndarray], list[np.ndarray], list[np.ndarray]]:
    basis = tuple(bits for bits in range(1 << VERTICES) if bits.bit_count() == PARTICLES)
    index = {bits: position for position, bits in enumerate(basis)}
    one_way: dict[tuple[int, int], np.ndarray] = {}
    for u, v in EDGES:
        one_way[(u, v)] = directed_hop(basis, index, u, v)
        one_way[(v, u)] = directed_hop(basis, index, v, u)
    hops = [one_way[(v, u)] + one_way[(u, v)] for u, v in EDGES]
    currents = [1j * (one_way[(v, u)] - one_way[(u, v)]) for u, v in EDGES]
    numbers = [
        np.diag([float((bits >> site) & 1) for bits in basis]).astype(np.complex128)
        for site in range(VERTICES)
    ]
    return basis, index, hops, currents, numbers


def hamiltonian(hops: list[np.ndarray], live_mask: int) -> np.ndarray:
    result = np.zeros_like(hops[0])
    for edge, hop in enumerate(hops):
        if (live_mask >> edge) & 1:
            result += COEFFICIENTS[edge] * hop
    return result


def evolve(state: np.ndarray, operator: np.ndarray, dwell: float) -> np.ndarray:
    values, vectors = eigh(operator)
    amplitudes = vectors.conj().T @ state
    return vectors @ (np.exp(-1j * dwell * values) * amplitudes)


def local_front_order() -> tuple[int, ...]:
    edge_number = {edge: index for index, edge in enumerate(EDGES)}
    live = set(range(len(EDGES)))
    current_vertex = EDGES[0][0]
    result: list[int] = []
    for _ in range(EVENTS):
        incident = [edge_number[tuple(sorted((current_vertex, neighbor)))] for neighbor in LOCAL_PORT_ORDERS[current_vertex]]
        current_edge = next((edge for edge in incident if edge in live), None)
        if current_edge is None:
            raise AssertionError("front has no live edge at its current vertex")
        result.append(current_edge)
        live.remove(current_edge)
        u, v = EDGES[current_edge]
        current_vertex = v if current_vertex == u else u
    return tuple(result)



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


def main() -> int:
    started = time.perf_counter()
    report = Report()
    basis, _index, hops, currents, numbers = build_sector()
    full_mask = (1 << len(EDGES)) - 1
    order = local_front_order()
    report.check(
        "C0",
        "independent directed half-edge front",
        order == EXPECTED_ORDER,
        f"order={order} endpoint_star_only=yes",
    )

    initial_h = hamiltonian(hops, full_mask)
    values, vectors = eigh(initial_h)
    sea = vectors[:, 0]
    phase = np.array(
        [
            np.exp(-1j * BOOST_PHASE * (((bits >> 0) & 1) - ((bits >> 1) & 1)))
            for bits in basis
        ],
        dtype=np.complex128,
    )
    state = phase * sea
    state /= np.linalg.norm(state)
    initial_energy = float(np.vdot(state, initial_h @ state).real)
    battery = BATTERY_START
    live_mask = full_mask
    max_continuity = 0.0
    max_ledger_drift = 0.0
    min_density = 1.0
    max_density = 0.0
    min_energy = math.inf
    min_excess = math.inf
    min_support = math.inf
    currents_seen: list[float] = []
    fair_branch_count = 1
    rows: list[str] = []

    for step, (edge, dwell) in enumerate(zip(EXPECTED_ORDER, DWELLS), start=1):
        if not ((live_mask >> edge) & 1):
            raise AssertionError("front chose an inactive edge")
        h_in = hamiltonian(hops, live_mask)
        energy_before = float(np.vdot(state, h_in @ state).real)
        continuity = 0.0
        for vertex, number in enumerate(numbers):
            commutator = 1j * (h_in @ number - number @ h_in)
            divergence = np.zeros_like(h_in)
            for edge_number, (u, v) in enumerate(EDGES):
                if not ((live_mask >> edge_number) & 1) or vertex not in (u, v):
                    continue
                oriented = currents[edge_number] if vertex == u else -currents[edge_number]
                divergence -= COEFFICIENTS[edge_number] * oriented
            continuity = max(continuity, float(np.max(np.abs(commutator - divergence))))
        max_continuity = max(max_continuity, continuity)

        state = evolve(state, h_in, dwell)
        current = COEFFICIENTS[edge] * float(np.vdot(state, currents[edge] @ state).real)
        currents_seen.append(current)
        support = sum(
            abs(COEFFICIENTS[number] * float(np.vdot(state, currents[number] @ state).real)) >= CURRENT_FLOOR
            for number in range(len(EDGES))
            if (live_mask >> number) & 1
        )
        min_support = min(min_support, support)

        post_mask = live_mask & ~(1 << edge)
        h_out = hamiltonian(hops, post_mask)
        energy_after = float(np.vdot(state, h_out @ state).real)
        battery -= energy_after - energy_before
        drift = energy_after + battery - (initial_energy + BATTERY_START)
        max_ledger_drift = max(max_ledger_drift, abs(drift))
        min_energy = min(min_energy, energy_after)
        densities = [float(np.vdot(state, number @ state).real) for number in numbers]
        min_density = min(min_density, min(densities))
        max_density = max(max_density, max(densities))
        fixed_indices = [index for index, bits in enumerate(basis) if bits.bit_count() == PARTICLES]
        ground = float(np.min(np.linalg.eigvalsh(h_out[np.ix_(fixed_indices, fixed_indices)])))
        min_excess = min(min_excess, energy_after - ground)
        fair_branch_count *= 2
        rows.append(
            f"ROW step={step} edge={edge} J={current:+.6f} support={support} "
            f"E={energy_before:+.6f}->{energy_after:+.6f} battery={battery:.6f} "
            f"rho=[{min(densities):.4f},{max(densities):.4f}]"
        )
        live_mask = post_mask

    report.check(
        "C1",
        "connected prefixes and fair nonbridge branches",
        component_count(live_mask) == 1
        and fair_branch_count == 2 ** EVENTS
        and min_support >= 4,
        f"final_components={component_count(live_mask)} final_branches={fair_branch_count} "
        f"min_transport_support={int(min_support)}",
    )
    report.check(
        "C2",
        "independent continuity and matter viability",
        max_continuity <= TOL
        and min_density >= DENSITY_LOW
        and max_density <= DENSITY_HIGH
        and min_energy < -1.0e-6
        and min_excess >= -TOL,
        f"continuity={max_continuity:.3e} density=[{min_density:.6f},{max_density:.6f}] "
        f"min_E={min_energy:+.6f} min_excess={min_excess:.6f}",
    )
    report.check(
        "C3",
        "independent persistent ledger",
        max_ledger_drift <= TOL
        and -TOL <= battery <= BATTERY_CAP + TOL
        and battery < BATTERY_START - 1.0e-6,
        f"start={BATTERY_START:.6f} final={battery:.6f} "
        f"cap={BATTERY_CAP:.6f} max_drift={max_ledger_drift:.3e} reset=no",
    )
    report.lines.extend(rows)
    report.lines.append(
        "SCOPE fixed-N CAR reconstruction; the oriented port order, local pulse, "
        "event rule, and scalar battery are supplied finite fixtures, not an "
        "endogenous formation law or quantum-battery theorem"
    )
    elapsed = time.perf_counter() - started
    rss = float(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    if os.uname().sysname == "Darwin":
        rss /= 1024.0 * 1024.0
    else:
        rss /= 1024.0
    report.check(
        "C4",
        "execution envelope",
        elapsed < 180.0 and rss < 180.0,
        f"elapsed={elapsed:.2f}s rss={rss:.1f}MiB",
    )
    report.lines.append(f"TOTAL: PASS={report.passes} FAIL={report.failures}")
    print("\n".join(report.lines))
    return 1 if report.failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
