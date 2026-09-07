#!/usr/bin/env python3
"""Scratch-only mutation probe pinned to the final shared-battery runner bytes.

The mutations below are deliberately wrong models or formulas.  They do not
retune the physical fixture and are not alternative no-go routes.
"""

from __future__ import annotations

import hashlib
import importlib.util
import os
import sys
from pathlib import Path

for _thread_variable in (
    "OPENBLAS_NUM_THREADS",
    "OMP_NUM_THREADS",
    "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS",
    "NUMEXPR_NUM_THREADS",
):
    os.environ[_thread_variable] = "1"

import numpy as np


ROOT = Path.cwd()
PRIMARY_PATH = ROOT / "scripts/native_edge_record_shared_battery_transport_2026_09_07.py"
LEGACY_PROBE_PATH = (
    ROOT
    / ".claude/science/physics-loops/record-battery-transport-20260907/primary"
    / "mutation_and_ideal_margin_probe.py"
)
EXPECTED_PRIMARY_SHA256 = "ab0ae23cfdbd084dd3d6043c9bc94560d7b8160925d39a9083dcd8a9f3be4750"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


actual_primary_hash = hashlib.sha256(PRIMARY_PATH.read_bytes()).hexdigest()
if actual_primary_hash != EXPECTED_PRIMARY_SHA256:
    raise RuntimeError(
        f"primary bytes changed: expected {EXPECTED_PRIMARY_SHA256}, got {actual_primary_hash}"
    )

legacy = load_module("final_mutation_legacy_helpers", LEGACY_PROBE_PATH)
p = legacy.primary


def contracted_surface(
    components: dict[tuple[int, int], np.ndarray],
    initial_groups,
    surface_groups,
    *,
    kernel_width: float,
    moment_center: float,
):
    """Contract one deliberately selectable kernel and first-moment center."""
    entries = []
    for (initial_number, surface_number), vector in sorted(components.items()):
        shift = (
            initial_groups[initial_number].energy
            - surface_groups[surface_number].energy
        )
        entries.append((shift, vector))
    shifts = np.asarray([entry[0] for entry in entries], dtype=float)
    vectors = np.column_stack([entry[1] for entry in entries])
    overlap = p.sine_overlap(
        shifts[:, np.newaxis] - shifts[np.newaxis, :], kernel_width
    )
    density = vectors @ overlap @ vectors.conj().T
    gram = vectors.conj().T @ vectors
    moments = (
        moment_center
        + 0.5 * (shifts[:, np.newaxis] + shifts[np.newaxis, :])
    ) * overlap
    battery_energy = np.einsum("ij,ji->", moments, gram)
    return density, float(battery_energy.real)


def controlled_components(fixture: dict[str, object]):
    propagator = np.eye(len(fixture["initial"]), dtype=np.complex128)
    result = []
    for step, dwell in enumerate(p.DWELLS, start=1):
        dwell_unitary = p.unitary_from_eigensystem(
            fixture["eigenvalues"][step - 1],
            fixture["eigenvectors"][step - 1],
            dwell,
        )
        propagator = dwell_unitary @ propagator
        minus = p.endpoint_components(
            fixture["initial"],
            propagator,
            fixture["groups"][0],
            fixture["groups"][step - 1],
        )
        plus = p.endpoint_components(
            fixture["initial"],
            propagator,
            fixture["groups"][0],
            fixture["groups"][step],
        )
        result.append((minus, plus, propagator.copy()))
    return result


def run_result(fixture: dict[str, object], convention: str, width: float):
    return p.run_protocol(
        convention,
        width,
        fixture["initial"],
        fixture["hamiltonians"],
        fixture["masks"],
        fixture["groups"],
        fixture["eigenvalues"],
        fixture["eigenvectors"],
        fixture["currents"],
        fixture["numbers"],
    )


def free_mutation_line(
    fixture: dict[str, object], correct: dict[str, object], mutation: str
) -> str:
    elapsed = 0.0
    previous_plus = np.outer(fixture["initial"], fixture["initial"].conj())
    maximum_density_distance = 0.0
    maximum_endpoint_residual = 0.0
    maximum_forward_dwell_residual = 0.0
    maximum_ledger_drift = 0.0
    minus_supports = []
    plus_supports = []
    front_values = []
    initial_energy = float(
        np.vdot(
            fixture["initial"],
            fixture["hamiltonians"][0] @ fixture["initial"],
        ).real
    )
    conserved_total = initial_energy + p.PACKET_MEAN

    for step, dwell in enumerate(p.DWELLS, start=1):
        elapsed += dwell
        if mutation == "phase_sign":
            minus_propagator = p.unitary_from_eigensystem(
                fixture["eigenvalues"][step - 1],
                fixture["eigenvectors"][step - 1],
                -elapsed,
            )
            plus_propagator = p.unitary_from_eigensystem(
                fixture["eigenvalues"][step],
                fixture["eigenvectors"][step],
                -elapsed,
            )
        elif mutation == "input_output_swap":
            minus_propagator = p.unitary_from_eigensystem(
                fixture["eigenvalues"][step],
                fixture["eigenvectors"][step],
                elapsed,
            )
            plus_propagator = p.unitary_from_eigensystem(
                fixture["eigenvalues"][step - 1],
                fixture["eigenvectors"][step - 1],
                elapsed,
            )
        else:
            raise ValueError(mutation)

        minus_components = p.endpoint_components(
            fixture["initial"],
            minus_propagator,
            fixture["groups"][0],
            fixture["groups"][step - 1],
        )
        plus_components = p.endpoint_components(
            fixture["initial"],
            plus_propagator,
            fixture["groups"][0],
            fixture["groups"][step],
        )
        minus = p.surface_from_components(
            minus_components, fixture["groups"][0], fixture["groups"][step - 1]
        )
        plus = p.surface_from_components(
            plus_components, fixture["groups"][0], fixture["groups"][step]
        )
        correct_row = correct["rows"][step - 1]
        maximum_density_distance = max(
            maximum_density_distance,
            float(np.linalg.norm(minus.density - correct_row["minus_surface"].density)),
            float(np.linalg.norm(plus.density - correct_row["plus_surface"].density)),
        )

        expected_forward_dwell = p.unitary_from_eigensystem(
            fixture["eigenvalues"][step - 1],
            fixture["eigenvectors"][step - 1],
            dwell,
        )
        maximum_forward_dwell_residual = max(
            maximum_forward_dwell_residual,
            p.max_abs(
                minus.density
                - expected_forward_dwell
                @ previous_plus
                @ expected_forward_dwell.conj().T
            ),
        )
        for initial_number, initial_group in enumerate(fixture["groups"][0]):
            source = initial_group.projector @ fixture["initial"]
            for output_number, output_group in enumerate(fixture["groups"][step]):
                expected = (
                    np.exp(-1j * elapsed * output_group.energy)
                    * output_group.projector
                    @ source
                )
                maximum_endpoint_residual = max(
                    maximum_endpoint_residual,
                    p.max_abs(
                        plus_components[(initial_number, output_number)] - expected
                    ),
                )

        minus_observed = legacy.surface_measure(
            fixture, minus.density, step, before_event=True
        )
        plus_observed = legacy.surface_measure(
            fixture, plus.density, step, before_event=False
        )
        minus_supports.append(int(minus_observed["support"]))
        plus_supports.append(int(plus_observed["support"]))
        front_values.append(abs(float(minus_observed["currents"][p.EDGE_ORDER[step - 1]])))
        maximum_ledger_drift = max(
            maximum_ledger_drift,
            abs(float(minus_observed["energy"]) + minus.battery_energy - conserved_total),
            abs(float(plus_observed["energy"]) + plus.battery_energy - conserved_total),
        )
        previous_plus = plus.density

    expected_rows_changed = (
        minus_supports != correct["minus_supports"]
        or plus_supports != correct["plus_supports"]
        or maximum_density_distance > 1.0e-6
    )
    composition_caught = (
        maximum_endpoint_residual > p.NUM_TOL
        or maximum_forward_dwell_residual > p.NUM_TOL
    )
    return (
        f"MUTATION free_{mutation} caught={composition_caught} "
        f"endpoint_residual={maximum_endpoint_residual:.6e} "
        f"forward_dwell_residual={maximum_forward_dwell_residual:.6e} "
        f"max_rho_distance={maximum_density_distance:.6e} "
        f"minus_supports={minus_supports} plus_supports={plus_supports} "
        f"front_max={max(front_values):.6f} exact_prefix_changed={expected_rows_changed} "
        f"self_consistent_ledger_drift={maximum_ledger_drift:.3e} "
        "limitation=ledger_alone_does_not_detect"
    )


def width_mutation_lines(
    fixture: dict[str, object],
    components,
    correct_by_width: dict[float, dict[str, object]],
) -> list[str]:
    lines = []
    initial_energy = float(
        np.vdot(
            fixture["initial"],
            fixture["hamiltonians"][0] @ fixture["initial"],
        ).real
    )
    for width in p.PREREGISTERED_CONTROL_WIDTHS:
        correct = correct_by_width[width]
        correct_mean = p.PACKET_LOW + 0.5 * width
        wrong_mean_drift = 0.0
        wrong_kernel_distances = []
        wrong_minus_supports = []
        wrong_plus_supports = []
        wrong_front_values = []
        for step, (minus_components, plus_components, _) in enumerate(
            components, start=1
        ):
            for which, component_map, group_number in (
                ("minus", minus_components, step - 1),
                ("plus", plus_components, step),
            ):
                correct_density, wrong_mean_battery = contracted_surface(
                    component_map,
                    fixture["groups"][0],
                    fixture["groups"][group_number],
                    kernel_width=width,
                    moment_center=p.PACKET_MEAN,
                )
                observed = legacy.surface_measure(
                    fixture, correct_density, step, before_event=(which == "minus")
                )
                wrong_mean_drift = max(
                    wrong_mean_drift,
                    abs(
                        float(observed["energy"])
                        + wrong_mean_battery
                        - (initial_energy + correct_mean)
                    ),
                )

                wrong_density, _ = contracted_surface(
                    component_map,
                    fixture["groups"][0],
                    fixture["groups"][group_number],
                    kernel_width=p.PACKET_WIDTH,
                    moment_center=correct_mean,
                )
                correct_surface = correct["rows"][step - 1][f"{which}_surface"]
                wrong_kernel_distances.append(
                    float(np.linalg.norm(wrong_density - correct_surface.density))
                )
                wrong_observed = legacy.surface_measure(
                    fixture, wrong_density, step, before_event=(which == "minus")
                )
                if which == "minus":
                    wrong_minus_supports.append(int(wrong_observed["support"]))
                    wrong_front_values.append(
                        abs(float(wrong_observed["currents"][p.EDGE_ORDER[step - 1]]))
                    )
                else:
                    wrong_plus_supports.append(int(wrong_observed["support"]))

        wrong_kernel_gate = (
            min(wrong_minus_supports) >= 4
            and max(wrong_front_values) >= 0.05
            and (width != 260.0 or min(wrong_plus_supports) >= 4)
        )
        cap_violation = float(correct["reachable_high"]) - p.BATTERY_CAP
        lines.append(
            f"MUTATION width{int(width)}_mean_as_width1 caught={wrong_mean_drift > 1e-8} "
            f"ledger_drift={wrong_mean_drift:.6f} expected_center_error={0.5 * (width - 1.0):.6f} "
            "state_density_unchanged=True"
        )
        lines.append(
            f"MUTATION width{int(width)}_cap_as_49 caught={cap_violation > p.NUM_TOL} "
            f"spectral_high={float(correct['reachable_high']):.6f} wrong_cap=49 "
            f"excess_over_cap={cap_violation:.6f}"
        )
        lines.append(
            f"MUTATION width{int(width)}_kernel_as_width1 caught={max(wrong_kernel_distances) > 1e-6} "
            f"max_rho_distance={max(wrong_kernel_distances):.6e} "
            f"minus_supports={wrong_minus_supports} plus_supports={wrong_plus_supports} "
            f"declared_gate_pass={wrong_kernel_gate} "
            "limitation=self_consistent_state_and_ledger_checks_do_not_identify_packet_width"
        )
    return lines


def broad_limit_line(
    fixture: dict[str, object],
    components,
    correct_by_width: dict[float, dict[str, object]],
) -> str:
    final_propagator = components[-1][2]
    ideal_state = final_propagator @ fixture["initial"]
    ideal_density = np.outer(ideal_state, ideal_state.conj())
    distances = {}
    for width in (1.0, *p.PREREGISTERED_CONTROL_WIDTHS):
        result = correct_by_width[width]
        distances[width] = float(
            np.linalg.norm(result["rows"][-1]["plus_surface"].density - ideal_density)
        )
    monotone = distances[260.0] < distances[125.0] < distances[1.0]
    return (
        "CONTROL broad_packet_to_ideal "
        f"caught={monotone} final_rho_distances="
        f"w1:{distances[1.0]:.6e},w125:{distances[125.0]:.6e},w260:{distances[260.0]:.6e} "
        "criterion=d260<d125<d1 widths_are_only_preregistered_values"
    )


def main() -> int:
    fixture = legacy.load_fixture()
    old_style_prefixes = legacy.baseline_prefixes(fixture)
    controlled = run_result(fixture, "controlled", 1.0)
    free = run_result(fixture, "free", 1.0)
    controls = {
        1.0: controlled,
        125.0: run_result(fixture, "controlled", 125.0),
        260.0: run_result(fixture, "controlled", 260.0),
    }
    components = controlled_components(fixture)

    lines = [
        "SCOPE mutations are wrong formulas/models on the frozen fixture; no parameter search or retuning",
        "MAP historical B0-B7=kernel,spectrum,path,dwell,degeneracy,moment,first-dwell,envelope; P2=density; P3=energy",
    ]
    lines.extend(legacy.physical_variant_lines(fixture, old_style_prefixes))
    lines.extend(legacy.mutation_family_checks(fixture, old_style_prefixes))
    lines.append(free_mutation_line(fixture, free, "phase_sign"))
    lines.append(free_mutation_line(fixture, free, "input_output_swap"))
    lines.extend(width_mutation_lines(fixture, components, controls))
    lines.append(broad_limit_line(fixture, components, controls))
    lines.append(
        "LIMITATIONS internal physics thresholds need not catch every phase/timing mutation; exact prefix and composition controls are load-bearing"
    )
    lines.append(f"HASH primary={actual_primary_hash}")
    lines.append(
        f"HASH legacy_probe={hashlib.sha256(LEGACY_PROBE_PATH.read_bytes()).hexdigest()}"
    )
    lines.append(f"HASH scratch={hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}")
    print("\n".join(lines))

    required = [line for line in lines if line.startswith("MUTATION")]
    broad = next(line for line in lines if line.startswith("CONTROL broad_packet"))
    return 0 if required and all("caught=True" in line for line in required) and "caught=True" in broad else 1


if __name__ == "__main__":
    raise SystemExit(main())
