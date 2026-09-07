#!/usr/bin/env python3
"""Stress a local, no-reset Record front on the native edge matter carrier.

This is a finite constructive probe, not a derivation of event occurrence.  A
local edge front walks the line graph of the open 2x2x2 cube, while a local
phase pulse creates a half-filled moving state.  The native edge Record
instrument, continuity equation, live-component support, and one persistent
scalar energy reserve are checked through five events.  The scalar reserve is
a ledger stress test; it is not a finite-dimensional quantum-battery proof.
"""

from __future__ import annotations

import importlib.util
import math
import os
import resource
import sys
import time
from pathlib import Path

for _thread_var in (
    "OPENBLAS_NUM_THREADS",
    "OMP_NUM_THREADS",
    "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS",
    "NUMEXPR_NUM_THREADS",
):
    os.environ[_thread_var] = "1"

import numpy as np
from scipy.linalg import expm


AUDIT_TIMEOUT_SEC = 180
# The primary runner imports the native edge carrier from the stacked parent
# block; pin that dependency in the canonical cache envelope as well.
AUDIT_INPUT_PATHS = ("scripts/native_edge_record_matter_instrument_2026_09_05.py",)
TOL = 3.0e-10
CURRENT_FLOOR = 2.0e-2
DENSITY_LOW = 0.10
DENSITY_HIGH = 0.90
BATTERY_START = 4.0
BATTERY_CAP = 8.0
BOOST_PHASE = 0.7
EDGE_ORDER = (0, 3, 5, 6, 9)
DWELLS = (0.41, 0.37, 0.29, 0.23, 0.19)
# A fixed oriented port order is the supplied local-front fixture.
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


def load_native() -> object:
    source = Path(__file__).with_name("native_edge_record_matter_instrument_2026_09_05.py")
    spec = importlib.util.spec_from_file_location("native_edge_record_matter_instrument", source)
    if spec is None or spec.loader is None:
        raise RuntimeError("native edge source cannot be loaded")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def directed_hop(car: object, source: int, target: int) -> np.ndarray:
    """Return c_target^dagger c_source on the even CAR sector."""
    dimension = car.dimension
    result = np.zeros((dimension, dimension), dtype=np.complex128)
    for column, bits in enumerate(car.basis):
        annihilated = car._ladder_action(bits, source, create=False)
        if annihilated is None:
            continue
        after_annihilation, phase_one = annihilated
        created = car._ladder_action(after_annihilation, target, create=True)
        if created is None:
            continue
        after_creation, phase_two = created
        result[car.index[after_creation], column] += phase_one * phase_two
    return result


def current_operators(model: object) -> tuple[list[np.ndarray], list[np.ndarray]]:
    car = model.car
    currents: list[np.ndarray] = []
    numbers = [
        0.5 * (np.eye(car.dimension, dtype=np.complex128) - word)
        for word in car.B
    ]
    for u, v in model.graph.edges:
        forward = directed_hop(car, v, u)
        backward = directed_hop(car, u, v)
        currents.append(1j * (forward - backward))
    return currents, numbers


def local_front_order(graph: object, start: int, events: int) -> tuple[int, ...]:
    """Walk a supplied oriented port order, moving across each recorded edge."""
    live = set(range(len(graph.edges)))
    current_vertex = graph.edges[start][0]
    order: list[int] = []
    for _ in range(events):
        incident = [
            graph.edge_number(current_vertex, neighbor)
            for neighbor in LOCAL_PORT_ORDERS[current_vertex]
        ]
        current_edge = next((edge for edge in incident if edge in live), None)
        if current_edge is None:
            raise ValueError("local front has no live edge at its current endpoint")
        order.append(current_edge)
        live.remove(current_edge)
        u, v = graph.edges[current_edge]
        current_vertex = v if current_vertex == u else u
    return tuple(order)



def expectation(state: np.ndarray, operator: np.ndarray) -> float:
    value = np.vdot(state, operator @ state)
    if abs(value.imag) > 2.0e-9:
        raise AssertionError(f"observable is not real: {value}")
    return float(value.real)


def max_abs(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix))) if matrix.size else 0.0


def continuity_residual(
    model: object,
    hamiltonian: np.ndarray,
    currents: list[np.ndarray],
    numbers: list[np.ndarray],
    live_mask: int,
) -> float:
    residual = 0.0
    for vertex, number in enumerate(numbers):
        commutator = 1j * (hamiltonian @ number - number @ hamiltonian)
        divergence = np.zeros_like(hamiltonian)
        for edge_index, (u, v) in enumerate(model.graph.edges):
            if not ((live_mask >> edge_index) & 1) or vertex not in (u, v):
                continue
            oriented = currents[edge_index] if vertex == u else -currents[edge_index]
            divergence -= model.graph.coefficients[edge_index] * oriented
        residual = max(residual, max_abs(commutator - divergence))
    return residual


def fixed_number_ground(model: object, hamiltonian: np.ndarray, particles: int) -> float:
    indices = [
        index for index, bits in enumerate(model.car.basis)
        if bits.bit_count() == particles
    ]
    return float(np.min(np.linalg.eigvalsh(hamiltonian[np.ix_(indices, indices)])))


def local_cycle(model: object, native: object) -> dict[str, object]:
    currents, numbers = current_operators(model)
    sea = native.selected_initial_states(model)["sea"]
    phase_generator = numbers[0] - numbers[1]
    initial = expm(-1j * BOOST_PHASE * phase_generator) @ sea
    initial /= np.linalg.norm(initial)
    initial_hamiltonian = model.direct_hamiltonian(model.graph.full_mask)
    initial_energy = expectation(initial, initial_hamiltonian)

    state = initial.copy()
    live_mask = model.graph.full_mask
    battery = BATTERY_START
    rows: list[dict[str, float]] = []
    max_continuity = 0.0
    max_ledger_drift = 0.0
    min_density = 1.0
    max_density = 0.0
    min_energy = math.inf
    min_excess = math.inf
    min_components = math.inf
    min_transport_support = math.inf
    front_currents: list[float] = []
    for step, (edge_index, dwell) in enumerate(zip(EDGE_ORDER, DWELLS), start=1):
        if not ((live_mask >> edge_index) & 1):
            raise AssertionError("local front selected a recorded edge")
        hamiltonian = model.direct_hamiltonian(live_mask)
        energy_before = expectation(state, hamiltonian)
        current_before = model.graph.coefficients[edge_index] * expectation(
            state, currents[edge_index]
        )
        continuity = continuity_residual(model, hamiltonian, currents, numbers, live_mask)
        max_continuity = max(max_continuity, continuity)

        state = native.evolve_direct(hamiltonian, state, dwell)
        current_after = model.graph.coefficients[edge_index] * expectation(
            state, currents[edge_index]
        )
        front_currents.append(current_after)
        live_currents = [
            abs(model.graph.coefficients[number] * expectation(state, currents[number]))
            for number in range(len(model.graph.edges))
            if (live_mask >> number) & 1
        ]
        transport_support = sum(value >= CURRENT_FLOOR for value in live_currents)
        min_transport_support = min(min_transport_support, transport_support)

        post_mask = live_mask & ~(1 << edge_index)
        post_hamiltonian = model.direct_hamiltonian(post_mask)
        energy_after = expectation(state, post_hamiltonian)
        system_delta = energy_after - energy_before
        battery -= system_delta
        ledger_drift = energy_after + battery - (initial_energy + BATTERY_START)
        max_ledger_drift = max(max_ledger_drift, abs(ledger_drift))

        components = native.components(
            model.graph.vertices, model.graph.edges, post_mask
        )
        min_components = min(min_components, len(components))
        if len(components) != 1:
            raise AssertionError("the chosen local prefix disconnected the carrier")
        densities = [expectation(state, number) for number in numbers]
        min_density = min(min_density, min(densities))
        max_density = max(max_density, max(densities))
        min_energy = min(min_energy, energy_after)
        ground = fixed_number_ground(model, post_hamiltonian, 4)
        excess = energy_after - ground
        min_excess = min(min_excess, excess)
        rows.append(
            {
                "step": float(step),
                "edge": float(edge_index),
                "dwell": dwell,
                "current_before": current_before,
                "current_after": current_after,
                "transport_support": float(transport_support),
                "energy_before": energy_before,
                "energy_after": energy_after,
                "system_delta": system_delta,
                "battery": battery,
                "ledger_drift": ledger_drift,
                "min_density": min(densities),
                "max_density": max(densities),
                "ground": ground,
                "excess": excess,
                "live_edges": float(post_mask.bit_count()),
            }
        )
        live_mask = post_mask

    return {
        "initial": initial,
        "initial_energy": initial_energy,
        "rows": rows,
        "max_continuity": max_continuity,
        "max_ledger_drift": max_ledger_drift,
        "min_density": min_density,
        "max_density": max_density,
        "min_energy": min_energy,
        "min_excess": min_excess,
        "min_components": min_components,
        "min_transport_support": min_transport_support,
        "front_currents": front_currents,
        "final_battery": battery,
        "final_mask": live_mask,
    }


def main() -> int:
    started = time.perf_counter()
    report = Report()
    native = load_native()
    model = native.build_cube_model()
    order = local_front_order(model.graph, EDGE_ORDER[0], len(EDGE_ORDER))
    report.check(
        "L0",
        "endpoint-star scheduler",
        order == EDGE_ORDER,
        f"order={order} adjacency_only=yes events={len(order)}",
    )

    cycle = local_cycle(model, native)
    history_metrics, _branches = native.run_history(
        model,
        cycle["initial"],
        EDGE_ORDER,
        DWELLS,
    )
    report.check(
        "L1",
        "native no-reset Record histories",
        history_metrics.nonzero_branches == 2 ** len(EDGE_ORDER)
        and history_metrics.bridge_events == 0
        and history_metrics.nonbridge_events == (2 ** len(EDGE_ORDER) - 1)
        and history_metrics.maximum_residual <= TOL,
        f"final_branches={history_metrics.nonzero_branches} "
        f"nonbridge_events={history_metrics.nonbridge_events} "
        f"max_res={history_metrics.maximum_residual:.3e}",
    )
    report.check(
        "L2",
        "connected local prefixes",
        cycle["min_components"] == 1,
        f"min_components={int(cycle['min_components'])} "
        f"final_live_edges={cycle['final_mask'].bit_count()}",
    )
    report.check(
        "L3",
        "local continuity equation",
        cycle["max_continuity"] <= TOL,
        f"max_operator_residual={cycle['max_continuity']:.3e}",
    )
    report.check(
        "L4",
        "transport survives every local prefix",
        cycle["min_transport_support"] >= 4
        and max(abs(value) for value in cycle["front_currents"]) >= 0.05,
        f"min_live_edges_above_{CURRENT_FLOOR:g}={int(cycle['min_transport_support'])} "
        f"front_current_max={max(map(abs, cycle['front_currents'])):.6f}",
    )
    report.check(
        "L5",
        "half-filled matter background remains viable",
        cycle["min_density"] >= DENSITY_LOW
        and cycle["max_density"] <= DENSITY_HIGH
        and cycle["min_energy"] < -1.0e-6
        and cycle["min_excess"] >= -TOL,
        f"density=[{cycle['min_density']:.6f},{cycle['max_density']:.6f}] "
        f"min_E={cycle['min_energy']:+.6f} min_fixedN_excess={cycle['min_excess']:.6f}",
    )
    report.check(
        "L6",
        "one persistent scalar energy reserve",
        cycle["max_ledger_drift"] <= TOL
        and -TOL <= cycle["final_battery"] <= BATTERY_CAP + TOL
        and cycle["final_battery"] < BATTERY_START - 1.0e-6,
        f"start={BATTERY_START:.6f} final={cycle['final_battery']:.6f} "
        f"cap={BATTERY_CAP:.6f} max_drift={cycle['max_ledger_drift']:.3e} reset=no",
    )

    for row in cycle["rows"]:
        report.lines.append(
            "ROW "
            f"step={int(row['step'])} edge={int(row['edge'])} dwell={row['dwell']:.2f} "
            f"Jpre={row['current_before']:+.6f} Jpost={row['current_after']:+.6f} "
            f"support={int(row['transport_support'])} "
            f"E={row['energy_before']:+.6f}->{row['energy_after']:+.6f} "
            f"dE={row['system_delta']:+.6f} battery={row['battery']:.6f} "
            f"rho=[{row['min_density']:.4f},{row['max_density']:.4f}]"
        )
    report.lines.append(
        "SCOPE local endpoint-star scheduler with supplied oriented port order and "
        "phase pulse are finite dynamics; scalar battery is an exact resource "
        "ledger, not a quantum-battery or endogenous Record-formation derivation"
    )
    elapsed = time.perf_counter() - started
    rss = float(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    if sys.platform == "darwin":
        rss /= 1024.0 * 1024.0
    else:
        rss /= 1024.0
    report.check(
        "L7",
        "execution envelope",
        elapsed <= AUDIT_TIMEOUT_SEC and rss < 180.0,
        f"elapsed={elapsed:.2f}s timeout={AUDIT_TIMEOUT_SEC:.0f}s rss={rss:.1f}MiB",
    )
    report.lines.append(
        f"IDENTITY native_source={native.source_identity()[:16]} "
        f"path={'-'.join(map(str, EDGE_ORDER))} boost={BOOST_PHASE:.2f} "
        "no_fresh_state_reset=yes"
    )
    report.lines.append(f"TOTAL: PASS={report.passes} FAIL={report.failures}")
    print("\n".join(report.lines))
    return 1 if report.failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
