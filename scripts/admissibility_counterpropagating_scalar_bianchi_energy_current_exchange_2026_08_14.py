#!/usr/bin/env python3
"""Block 97: counterpropagating scalar source and reduced exchange gate.

The runner builds an exact local energy/current cochain for the Block95 free
scalar, retains every Fourier component of a two-wave L=5 standing source,
embeds its homogeneous stress in the Block78 trace--shear canonical sector,
and tests the common reduced Hamiltonian jet.  The jet cancels the complete
order-A^3 frozen-source defect of one Block78 front step, leaving an order-A^4
residual.  That residual is a target for the unconstructed seagull,
cubic-gravity, interference-energy, and joint discrete-Noether terms; it is
not a gravity no-go or an end-to-end theory.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys

import numpy as np
from scipy.integrate import solve_ivp


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_COUNTERPROPAGATING_SCALAR_BIANCHI_TRACE_SHEAR_ENERGY_CURRENT_EXCHANGE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md'
RUNNER_RELATIVE = (
    "scripts/admissibility_counterpropagating_scalar_bianchi_energy_current_"
    "exchange_2026_08_14.py"
)
PARENT_NOTE = (
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_BOUNDARY_DRESSED_JOINT_STAGE_HOMOGENEOUS_NONLINEAR_ZERO_MODE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md'
)
PARENT_RUNNER = (
    "scripts/admissibility_boundary_dressed_joint_stage_homogeneous_zero_"
    "mode_2026_08_14.py"
)
MINIMAL_AXIOMS = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_COUNTERPROPAGATING_SCALAR_BIANCHI_TRACE_SHEAR_ENERGY_CURRENT_EXCHANGE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_BOUNDARY_DRESSED_JOINT_STAGE_HOMOGENEOUS_NONLINEAR_ZERO_MODE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    'docs/ADMISSIBILITY_INCIDENCE_SCALAR_GRAPH_MATTER_FIRST_ORDER_TOTAL_WARD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    'docs/ADMISSIBILITY_INCIDENCE_FIERZ_PAULI_SIGNED_RECORD_SOURCE_FULL_TENSOR_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_INCIDENCE_ADM_DEPTH_TWO_SOURCED_CONSTRAINT_RECORD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    'docs/ADMISSIBILITY_CYCLE713_RECORD_HEAD_ADM_WORK_ARCHIVE_STATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_COMPONENT_STAGGERED_SIGNED_LINK_ACTION_LOCAL_WARD_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    'docs/ADMISSIBILITY_RAW_GRAPH_WARD_COMPACT_PULLBACK_TRANSLATION_GENERATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md',
    'docs/MINIMAL_AXIOMS_2026-06-29.md',
    'scripts/admissibility_counterpropagating_scalar_bianchi_energy_current_exchange_2026_08_14.py',
    'scripts/admissibility_boundary_dressed_joint_stage_homogeneous_zero_mode_2026_08_14.py',
    'scripts/admissibility_incidence_scalar_graph_matter_first_order_total_ward_cadence_boundary_2026_08_14.py',
    'scripts/admissibility_incidence_fierz_pauli_signed_record_source_full_tensor_cadence_boundary_2026_08_14.py',
    'scripts/admissibility_incidence_adm_depth_two_sourced_constraint_record_cadence_boundary_2026_08_14.py',
    'scripts/admissibility_cycle713_record_head_adm_work_archive_state_boundary_2026_08_14.py',
    'scripts/admissibility_component_staggered_signed_link_action_local_ward_boundary_2026_08_14.py',
    'scripts/admissibility_raw_graph_ward_compact_pullback_translation_generator_boundary_2026_08_14.py',
    'scripts/admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_2026_08_11.py',
)

CURRENT_MAIN = "eee6ab5874e2fc207db5526dc82d9f71ae550c7c"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
PARENT_COMMIT = "75ee8bdaccb28bb4d5689dd656a1c15dd00a3188"
PARENT_NOTE_BLOB = "8432ecf9793c504a3eb8a6515384d33aff5511dd"
PARENT_RUNNER_BLOB = "ea4d7176567c4cb998782d2060e2208db6e1de1c"

LATTICE_SIZE = 5
KAPPA = 2.0 * np.pi / LATTICE_SIZE
SINE = float(np.sin(KAPPA))
DELTA = 0.5
QFAC = float(np.sqrt(2.0 / 3.0))
Q_TENSOR = np.diag((2.0, -1.0, -1.0)) / np.sqrt(6.0)
TOL = 3.0e-10

sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_boundary_dressed_joint_stage_homogeneous_zero_mode_2026_08_14 as block96  # noqa: E402

block95 = block96.block95


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 190 else detail[:187] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def error_bound(value: float, tolerance: float = TOL) -> str:
    return f"<{tolerance:.0e}" if abs(value) < tolerance else f"{value:.3g}"


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def git_output(*args: str) -> str:
    return subprocess.check_output(("git",) + args, cwd=ROOT, text=True).strip()


def worktree_blob(relative: str) -> str:
    return git_output("hash-object", relative)


def authority_certificate(mutation: str) -> dict[str, object]:
    expected_axiom = "0" * 40 if mutation == "stale_axiom_authority" else CURRENT_AXIOM_BLOB
    missing = tuple(path for path in AUDIT_INPUT_PATHS if not (ROOT / path).exists())
    loaded: set[str] = set()
    for module in tuple(sys.modules.values()):
        file_name = getattr(module, "__file__", None)
        if not file_name:
            continue
        module_path = Path(file_name).resolve()
        try:
            relative = module_path.relative_to(ROOT).as_posix()
        except ValueError:
            continue
        if relative.startswith("scripts/") and relative.endswith(".py"):
            loaded.add(relative)
    declared = {path for path in AUDIT_INPUT_PATHS if path.startswith("scripts/")}
    parent = block96.authority_certificate("")
    parent_loaded_missing = tuple(
        path for path in parent["loaded_missing"] if path != RUNNER_RELATIVE
    )
    parent_recursive_loaded_missing = tuple(
        path for path in parent["parent_loaded_missing"] if path != RUNNER_RELATIVE
    )
    grandparent = block95.authority_certificate("")
    grandparent_loaded_missing = tuple(
        path
        for path in grandparent["loaded_missing"]
        if path not in (RUNNER_RELATIVE, block96.RUNNER_RELATIVE)
    )
    grandparent_valid = (
        grandparent["origin_main"] == block95.CURRENT_AXIOM_COMMIT
        and grandparent["axiom"] == block95.CURRENT_AXIOM_BLOB
        and grandparent["block77"]
        == (block95.BLOCK77_NOTE_BLOB, block95.BLOCK77_RUNNER_BLOB)
        and grandparent["block78"]
        == (block95.BLOCK78_NOTE_BLOB, block95.BLOCK78_RUNNER_BLOB)
        and grandparent["block83"]
        == (block95.BLOCK83_NOTE_BLOB, block95.BLOCK83_RUNNER_BLOB)
        and grandparent["block93"]
        == (block95.BLOCK93_NOTE_BLOB, block95.BLOCK93_RUNNER_BLOB)
        and not grandparent["mismatches"]
        and not grandparent["missing"]
        and not grandparent_loaded_missing
    )
    parent_valid = (
        parent["origin_main"] == block96.CURRENT_MAIN
        and parent["axiom"] == block96.CURRENT_AXIOM_BLOB
        and parent["parent_note"] == block96.PARENT_NOTE_BLOB
        and parent["parent_runner"] == block96.PARENT_RUNNER_BLOB
        and parent["parent_commit"] == block96.PARENT_COMMIT
        and not parent["missing"]
        and not parent_loaded_missing
        and not parent["parent_mismatches"]
        and not parent_recursive_loaded_missing
        and grandparent_valid
    )
    return {
        "origin_main": git_output("rev-parse", "origin/main"),
        "axiom": worktree_blob(MINIMAL_AXIOMS),
        "expected_axiom": expected_axiom,
        "parent_note": worktree_blob(PARENT_NOTE),
        "parent_runner": worktree_blob(PARENT_RUNNER),
        "parent_commit": git_output("rev-parse", PARENT_COMMIT),
        "missing": missing,
        "loaded_missing": tuple(sorted(loaded - declared)),
        "parent_valid": parent_valid,
        "parent_loaded_missing": parent_loaded_missing,
        "parent_recursive_loaded_missing": parent_recursive_loaded_missing,
        "grandparent_loaded_missing": grandparent_loaded_missing,
    }


def forward_difference(field: np.ndarray, axis: int) -> np.ndarray:
    return np.roll(field, -1, axis=axis) - field


def spatial_laplacian(field: np.ndarray) -> np.ndarray:
    return sum(
        (
            2.0 * field
            - np.roll(field, -1, axis=axis)
            - np.roll(field, 1, axis=axis)
            for axis in range(3)
        ),
        start=np.zeros_like(field),
    )


def local_energy(current: np.ndarray, following: np.ndarray) -> np.ndarray:
    kinetic = 0.5 * np.abs(following - current) ** 2
    potential = 0.5 * sum(
        (
            np.real(
                np.conj(forward_difference(current, axis))
                * forward_difference(following, axis)
            )
            for axis in range(3)
        ),
        start=np.zeros_like(kinetic),
    )
    return kinetic + potential


def local_flux(
    previous: np.ndarray,
    current: np.ndarray,
    following: np.ndarray,
    mutation: str = "",
) -> tuple[np.ndarray, ...]:
    velocity = 0.5 * (following - previous)
    coefficient = 0.7 if mutation == "break_energy_flux" else 1.0
    return tuple(
        -coefficient
        * np.real(
            np.conj(forward_difference(current, axis))
            * np.roll(velocity, -1, axis=axis)
        )
        for axis in range(3)
    )


def energy_current_certificate(mutation: str) -> dict[str, object]:
    rng = np.random.default_rng(9701)
    local_error = global_error = plane_error = 0.0
    random_cases = 0
    for size in range(3, 7):
        shape = (size,) * 3
        for _ in range(12):
            previous = rng.normal(size=shape) + 1.0j * rng.normal(size=shape)
            current = rng.normal(size=shape) + 1.0j * rng.normal(size=shape)
            following = rng.normal(size=shape) + 1.0j * rng.normal(size=shape)
            velocity = 0.5 * (following - previous)
            equation = (
                following
                - 2.0 * current
                + previous
                + spatial_laplacian(current)
            )
            fluxes = local_flux(previous, current, following, mutation)
            divergence = sum(
                (
                    flux - np.roll(flux, 1, axis=axis)
                    for axis, flux in enumerate(fluxes)
                ),
                start=np.zeros(shape),
            )
            residual = (
                local_energy(current, following)
                - local_energy(previous, current)
                + divergence
                - np.real(np.conj(velocity) * equation)
            )
            local_error = max(local_error, float(np.max(np.abs(residual))))

            on_shell_following = (
                2.0 * current - previous - spatial_laplacian(current)
            )
            global_error = max(
                global_error,
                abs(
                    float(np.sum(local_energy(current, on_shell_following)))
                    - float(np.sum(local_energy(previous, current)))
                ),
            )
            random_cases += 1

    per_size: dict[int, int] = {}
    modes = 0
    for size in range(3, 9):
        coordinates = np.indices((size,) * 3)
        for integer_mode in np.ndindex((size,) * 4):
            momentum = 2.0 * np.pi * np.asarray(integer_mode, dtype=float) / size
            if abs(block95.scalar_symbol(momentum)) >= TOL:
                continue
            spatial_phase = sum(
                momentum[axis] * coordinates[axis] for axis in range(3)
            )
            current = np.exp(-1.0j * spatial_phase)
            previous = np.exp(1.0j * momentum[3]) * current
            following = np.exp(-1.0j * momentum[3]) * current
            energy = local_energy(current, following)
            flux = np.asarray(
                [
                    float(np.mean(value))
                    for value in local_flux(previous, current, following, mutation)
                ]
            )
            stress = block95.centered_stress(momentum, np.zeros(4))
            plane_error = max(
                plane_error,
                float(np.max(np.abs(energy - stress[3, 3].real))),
                float(np.max(np.abs(flux - stress[3, :3].real))),
            )
            per_size[size] = per_size.get(size, 0) + 1
            modes += 1
    return {
        "random_cases": random_cases,
        "local_error": local_error,
        "global_error": global_error,
        "modes": modes,
        "per_size": per_size,
        "plane_error": plane_error,
    }


def standing_sources(mutation: str = "") -> dict[tuple[int, int, int, int], np.ndarray]:
    plus_index = np.asarray((1, 0, 0, 1), dtype=int)
    minus_index = np.asarray((4, 0, 0, 1), dtype=int)
    plus_momentum = np.asarray((KAPPA, 0.0, 0.0, KAPPA))
    minus_momentum = np.asarray((-KAPPA, 0.0, 0.0, KAPPA))
    modes = (
        (plus_index, plus_momentum, 1.0 + 0.0j),
        (minus_index, minus_momentum, 1.0 + 0.0j),
    )
    result: dict[tuple[int, int, int, int], np.ndarray] = {}
    for incoming_index, incoming, incoming_amplitude in modes:
        for outgoing_index, outgoing, outgoing_amplitude in modes:
            if mutation == "drop_interference" and np.any(
                outgoing_index != incoming_index
            ):
                continue
            transfer = outgoing - incoming
            key = tuple(
                int(value)
                for value in ((outgoing_index - incoming_index) % LATTICE_SIZE)
            )
            result.setdefault(key, np.zeros((4, 4), dtype=complex))
            result[key] += (
                np.conj(outgoing_amplitude)
                * incoming_amplitude
                * block95.centered_stress(incoming, transfer)
            )
    return result


def principal_transfer(key: tuple[int, int, int, int]) -> np.ndarray:
    values = np.asarray(key, dtype=int)
    signed = np.where(
        values <= LATTICE_SIZE // 2, values, values - LATTICE_SIZE
    )
    return 2.0 * np.pi * signed / LATTICE_SIZE


def standing_source_certificate(mutation: str) -> dict[str, object]:
    sources = standing_sources(mutation)
    expected_keys = {
        (0, 0, 0, 0),
        (2, 0, 0, 0),
        (3, 0, 0, 0),
    }
    expected_error = hermiticity_error = ward_error = 0.0
    zero = sources.get((0, 0, 0, 0), np.zeros((4, 4), dtype=complex))
    expected_zero = np.zeros((4, 4))
    expected_zero[3, 3] = 2.0 * SINE**2
    expected_zero[0, 0] = 2.0 * SINE**2
    expected_error = max(expected_error, float(np.max(np.abs(zero - expected_zero))))
    for key in ((2, 0, 0, 0), (3, 0, 0, 0)):
        observed = sources.get(key, np.zeros((4, 4), dtype=complex))
        expected = np.zeros((4, 4))
        expected[3, 3] = SINE**2
        expected_error = max(
            expected_error, float(np.max(np.abs(observed - expected)))
        )
    for key, tensor in sources.items():
        opposite = tuple(int((-value) % LATTICE_SIZE) for value in key)
        hermiticity_error = max(
            hermiticity_error,
            float(
                np.max(
                    np.abs(
                        sources.get(opposite, np.zeros((4, 4), dtype=complex))
                        - tensor.conj()
                    )
                )
            ),
        )
        transfer = principal_transfer(key)
        p = block95.block77.block53.lattice_vector(transfer[:3])
        current = np.asarray(tensor[3, :3], dtype=complex)
        spatial = np.asarray(tensor[:3, :3], dtype=complex)
        ward_error = max(
            ward_error,
            abs(1.0j * p @ current),
            float(np.max(np.abs(1.0j * spatial @ p))),
        )
    density = []
    for site in range(LATTICE_SIZE):
        value = 0.0j
        for key, tensor in sources.items():
            value += tensor[3, 3] * np.exp(
                2.0j * np.pi * key[0] * site / LATTICE_SIZE
            )
        density.append(value)
    coordinates = np.indices((LATTICE_SIZE,) * 3)
    standing_field = (
        np.exp(-1.0j * KAPPA * coordinates[0])
        + np.exp(1.0j * KAPPA * coordinates[0])
    )
    previous = np.exp(1.0j * KAPPA) * standing_field
    following = np.exp(-1.0j * KAPPA) * standing_field
    energy_density = local_energy(standing_field, following)
    source_density = np.broadcast_to(
        np.real(np.asarray(density))[:, None, None], energy_density.shape
    )
    charge_error = abs(
        float(np.sum(energy_density)) - float(np.sum(source_density))
    )
    improvement_norm = float(np.max(np.abs(energy_density - source_density)))
    return {
        "keys": set(sources),
        "expected_keys": expected_keys,
        "expected_error": expected_error,
        "hermiticity_error": hermiticity_error,
        "ward_error": ward_error,
        "minimum_density": float(np.min(np.real(density))),
        "density_imaginary": float(np.max(np.abs(np.imag(density)))),
        "charge_error": charge_error,
        "improvement_norm": improvement_norm,
        "rho_zero": float(np.real(zero[3, 3])),
        "tau_zero": np.real(zero[:3, :3]),
    }


def trace_shear_certificate(mutation: str) -> dict[str, object]:
    sources = standing_sources()
    zero = sources[(0, 0, 0, 0)]
    rho = float(np.real(zero[3, 3]))
    tau = np.real(zero[:3, :3])
    trace_part = rho * np.eye(3) / 3.0
    shear_part = rho * QFAC * Q_TENSOR
    if mutation == "trace_only":
        shear_part = np.zeros((3, 3))
    decomposition_error = float(
        np.max(np.abs(tau - trace_part - shear_part))
    )
    trace_only_norm = float(np.linalg.norm(tau - trace_part))
    trace_only_expected = rho * QFAC

    kinetic = block95.spatial_operators(np.zeros(3))[0]
    rng = np.random.default_rng(9702)
    de_witt_error = 0.0
    for _ in range(96):
        p_alpha, p_sigma = rng.normal(size=2)
        momentum_tensor = p_alpha * np.eye(3) / 3.0 + p_sigma * Q_TENSOR
        coordinates = block95.tensor_coordinates3(momentum_tensor)
        observed = 0.5 * float(
            np.real(np.vdot(coordinates, kinetic @ coordinates))
        )
        expected = -(p_alpha**2) / 12.0 + p_sigma**2 / 2.0
        de_witt_error = max(de_witt_error, abs(observed - expected))

    inhomogeneous_error = 0.0
    inhomogeneous_modes = 0
    for key in ((2, 0, 0, 0), (3, 0, 0, 0)):
        transfer = principal_transfer(key)
        p = block95.block77.block53.lattice_vector(transfer[:3])
        _kinetic, _potential, hamiltonian, momentum, _shift = (
            block95.spatial_operators(p)
        )
        coupling = 0.73
        denominator = (
            7.0 if mutation == "wrong_inhomogeneous_normalization" else 8.0
        )
        h_tensor = np.diag(
            (0.0, coupling / denominator, coupling / denominator)
        )
        h = block95.tensor_coordinates3(h_tensor)
        pi = np.zeros(6)
        source_density = coupling * sources[key][3, 3]
        source_current = 2.0 * coupling * sources[key][3, :3]
        inhomogeneous_error = max(
            inhomogeneous_error,
            abs((hamiltonian @ h)[0] - source_density),
            float(np.max(np.abs(momentum @ pi - source_current))),
        )
        inhomogeneous_modes += 1
    return {
        "rho": rho,
        "decomposition_error": decomposition_error,
        "trace_only_norm": trace_only_norm,
        "trace_only_expected": trace_only_expected,
        "de_witt_error": de_witt_error,
        "inhomogeneous_error": inhomogeneous_error,
        "inhomogeneous_modes": inhomogeneous_modes,
    }


def complex_step_gradient(function, values: np.ndarray) -> np.ndarray:
    step = 1.0e-30
    gradient = np.zeros(len(values))
    for index in range(len(values)):
        probe = np.asarray(values, dtype=complex)
        probe[index] += 1.0j * step
        gradient[index] = float(np.imag(function(probe)) / step)
    return gradient


def matter_energy_jet(
    alpha: complex | float,
    sigma: complex | float,
    zero_source: np.ndarray,
    jet_factor: float = 1.0,
) -> complex | float:
    rho = zero_source[3, 3]
    spatial = alpha * np.eye(3) + sigma * Q_TENSOR
    geometry = np.zeros(15, dtype=complex)
    geometry[9:15] = block95.tensor_coordinates3(spatial)
    interaction = np.sum(block95.adm_interaction_metric(geometry) * zero_source)
    return 1.0 - jet_factor * interaction / rho


def reduced_constraint(
    state: np.ndarray,
    source_scale: float,
    zero_source: np.ndarray,
    jet_factor: float = 1.0,
) -> complex | float:
    alpha, sigma, p_alpha, p_sigma = state
    return (
        -(p_alpha**2) / 12.0
        + p_sigma**2 / 2.0
        + source_scale
        * matter_energy_jet(alpha, sigma, zero_source, jet_factor)
    )


def reduced_vector_field(
    _time: float,
    state: np.ndarray,
    source_scale: float,
    zero_source: np.ndarray,
    jet_factor: float = 1.0,
) -> np.ndarray:
    gradient = complex_step_gradient(
        lambda values: reduced_constraint(
            values, source_scale, zero_source, jet_factor
        ),
        np.asarray(state, dtype=float),
    )
    return np.asarray((gradient[2], gradient[3], -gradient[0], -gradient[1]))


def exact_reduced_flow(
    time: float,
    p_alpha_initial: float,
    source_scale: float,
    mutation: str = "",
) -> np.ndarray:
    result = np.asarray(
        (
            -p_alpha_initial * time / 6.0 - source_scale * time**2 / 6.0,
            source_scale * QFAC * time**2,
            p_alpha_initial + 2.0 * source_scale * time,
            2.0 * source_scale * QFAC * time,
        )
    )
    if mutation == "break_continuous_flow":
        result[1] *= 0.8
    return result


def reduced_flow_certificate(mutation: str) -> dict[str, object]:
    zero_source = standing_sources()[(0, 0, 0, 0)]
    jet_factor = 0.8 if mutation == "wrong_matter_energy_jet" else 1.0
    jet_gradient = complex_step_gradient(
        lambda values: matter_energy_jet(
            values[0], values[1], zero_source, jet_factor
        ),
        np.zeros(2),
    )
    jet_gradient_error = float(
        np.max(np.abs(jet_gradient - np.asarray((-2.0, -2.0 * QFAC))))
    )
    rng = np.random.default_rng(9703)
    flow_error = constraint_error = 0.0
    cases = 0
    branch_counts = {-1: 0, 1: 0}
    for case in range(64):
        source_scale = float(10.0 ** rng.uniform(-5.0, 1.0))
        sign = -1 if case % 2 else 1
        p_alpha_initial = sign * np.sqrt(12.0 * source_scale)
        branch_counts[sign] += 1
        initial = np.asarray((0.0, 0.0, p_alpha_initial, 0.0))
        final_time = float(rng.uniform(0.03, 0.9))
        solution = solve_ivp(
            lambda time, state: reduced_vector_field(
                time, state, source_scale, zero_source, jet_factor
            ),
            (0.0, final_time),
            initial,
            rtol=2.0e-11,
            atol=2.0e-13,
        )
        observed = solution.y[:, -1]
        expected = exact_reduced_flow(
            final_time, p_alpha_initial, source_scale, mutation
        )
        scale = max(1.0, float(np.max(np.abs(expected))))
        flow_error = max(
            flow_error, float(np.max(np.abs(observed - expected))) / scale
        )
        constraint_error = max(
            constraint_error,
            abs(
                reduced_constraint(
                    observed, source_scale, zero_source, jet_factor
                )
            )
            / max(1.0, source_scale),
        )
        cases += 1

    coupling = 0.41
    rho = float(np.real(zero_source[3, 3]))
    source_scale = coupling * rho
    p0 = np.sqrt(12.0 * source_scale)
    continuous = exact_reduced_flow(DELTA, p0, source_scale)
    kick = coupling * np.real(zero_source[:3, :3])
    kick_alpha = float(np.trace(kick))
    kick_sigma = float(np.sum(kick * Q_TENSOR))
    momentum_match_error = max(
        abs((continuous[2] - p0) - kick_alpha),
        abs(continuous[3] - kick_sigma),
    )
    front_coordinates = np.asarray(
        (
            -(p0 + kick_alpha) / 12.0,
            kick_sigma / 2.0,
        )
    )
    coordinate_path_gap = float(
        np.linalg.norm(continuous[:2] - front_coordinates)
    )
    return {
        "cases": cases,
        "branch_counts": branch_counts,
        "jet_gradient_error": jet_gradient_error,
        "flow_error": flow_error,
        "constraint_error": constraint_error,
        "momentum_match_error": momentum_match_error,
        "coordinate_path_gap": coordinate_path_gap,
    }


def discrete_exchange_certificate(mutation: str) -> dict[str, object]:
    rho_unit = float(
        np.real(standing_sources()[(0, 0, 0, 0)][3, 3])
    )
    rng = np.random.default_rng(9704)
    frozen_formula_error = jet_formula_error = 0.0
    cubic_cancellation_error = 0.0
    cases = 0
    for case in range(128):
        amplitude = float(10.0 ** rng.uniform(-3.0, -0.2))
        coupling = float(10.0 ** rng.uniform(-2.0, 0.2))
        source_scale = coupling * rho_unit * amplitude**2
        sign = -1 if case % 2 else 1
        p0 = sign * np.sqrt(12.0 * source_scale)
        p_alpha = p0 + source_scale
        p_sigma = source_scale * QFAC
        alpha = -(p0 + source_scale) / 12.0
        sigma = source_scale * QFAC / 2.0
        frozen = -(p_alpha**2) / 12.0 + p_sigma**2 / 2.0 + source_scale
        energy = (
            1.0
            if mutation == "freeze_matter_energy"
            else 1.0 - 2.0 * alpha - 2.0 * QFAC * sigma
        )
        joint = (
            -(p_alpha**2) / 12.0
            + p_sigma**2 / 2.0
            + source_scale * energy
        )
        expected_frozen = (
            -p0 * source_scale / 6.0 + source_scale**2 / 4.0
        )
        expected_joint = -(source_scale**2) / 4.0
        frozen_formula_error = max(
            frozen_formula_error, abs(frozen - expected_frozen)
        )
        jet_formula_error = max(jet_formula_error, abs(joint - expected_joint))
        cubic_cancellation_error = max(
            cubic_cancellation_error,
            abs(
                (joint - frozen)
                - (
                    p0 * source_scale / 6.0
                    - source_scale**2 / 2.0
                )
            ),
        )
        cases += 1

    amplitudes = np.logspace(-3.0, -1.0, 25)
    frozen_slopes = []
    joint_slopes = []
    for sign in (-1, 1):
        frozen_values = []
        joint_values = []
        for amplitude in amplitudes:
            source_scale = 0.4 * rho_unit * amplitude**2
            p0 = sign * np.sqrt(12.0 * source_scale)
            p_alpha = p0 + source_scale
            p_sigma = source_scale * QFAC
            alpha = -(p0 + source_scale) / 12.0
            sigma = source_scale * QFAC / 2.0
            frozen = -(p_alpha**2) / 12.0 + p_sigma**2 / 2.0 + source_scale
            energy = (
                1.0
                if mutation == "freeze_matter_energy"
                else 1.0 - 2.0 * alpha - 2.0 * QFAC * sigma
            )
            joint = (
                -(p_alpha**2) / 12.0
                + p_sigma**2 / 2.0
                + source_scale * energy
            )
            frozen_values.append(abs(frozen))
            joint_values.append(abs(joint))
        frozen_slopes.append(
            float(np.polyfit(np.log(amplitudes), np.log(frozen_values), 1)[0])
        )
        joint_slopes.append(
            float(np.polyfit(np.log(amplitudes), np.log(joint_values), 1)[0])
        )
    return {
        "cases": cases,
        "frozen_formula_error": frozen_formula_error,
        "jet_formula_error": jet_formula_error,
        "cubic_cancellation_error": cubic_cancellation_error,
        "frozen_slopes": tuple(frozen_slopes),
        "joint_slopes": tuple(joint_slopes),
    }


def scope_certificate(mutation: str) -> dict[str, bool]:
    note = flat(NOTE_PATH)
    result = {
        "free_only": "exact local energy/current theorem is for the free scalar" in note,
        "reduced_only": "reduced trace–shear hamiltonian jet is not the full joint lattice action" in note,
        "ward_open": "full order-h phi^2 ward completion remains open" in note,
        "noether_open": "total discrete noether energy remains open" in note,
        "superposition_improvement_open": (
            "standing-wave local energy improvement and interference matching remain open"
            in note
        ),
        "record_open": "record compiler, law selection, and independent retention remain open" in note,
        "quartic_open": all(
            phrase in note
            for phrase in (
                "seagull s_phi2",
                "cubic gravity s_g3",
                "interference-sector energy",
            )
        ),
        "no_axiom": "no axiom amendment is forced" in note,
        "positive_coupling_scope": all(
            phrase in note
            for phrase in (
                "real two-branch theorem here assumes g>0",
                "block 78 does not select the sign or value of g",
            )
        ),
        "zero_score": all(
            phrase in note
            for phrase in (
                "zero obligation retirement",
                "no toe percentage moves",
                "retained-positive end-to-end theory count remains zero",
            )
        ),
    }
    if mutation == "claim_total_noether":
        result["noether_open"] = False
    if mutation == "claim_toe_progress":
        result["zero_score"] = False
    return result


def no_go_certificate(mutation: str) -> dict[str, object]:
    note = flat(NOTE_PATH)
    routes = (
        "finite-support metric seagull and cubic-action solve",
        "expanded bounded-support metric action",
        "tetrad, palatini, or bf carrier",
        "regge or dynamical-source discretization",
        "refinement or perfect-action route",
        "alternative variational cadence",
        "scalar-clock deparameterization",
    )
    return {
        "headings": all(f"n{index}" in note for index in range(1, 9)),
        "routes": all(route in note for route in routes),
        "attempted": "attempted" in note,
        "n1_failed": "n1 status: fail" in note,
        "n7_failed": "n7 status: fail" in note,
        "overall_failed": (
            "overall no-go-discipline status: fail — partial-narrowing" in note
        ),
        "narrow_only": (
            "the residual rejects neither bounded-local gravity nor the current axioms"
            in note
        ),
        "steelman": "strongest steelman" in note,
        "echo": "cross-cycle echo" in note,
        "levels": all(
            marker in note
            for marker in ("per-element", "per-site", "per-mode", "per-block", "lattice-wide")
        ),
        "valid": mutation != "weaken_no_go_packet",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutation",
        choices=(
            "stale_axiom_authority",
            "break_energy_flux",
            "drop_interference",
            "trace_only",
            "wrong_inhomogeneous_normalization",
            "break_continuous_flow",
            "wrong_matter_energy_jet",
            "freeze_matter_energy",
            "claim_total_noether",
            "claim_toe_progress",
            "weaken_no_go_packet",
        ),
        default="",
    )
    mutation = parser.parse_args().mutation
    checks = Checks()

    authority = authority_certificate(mutation)
    checks.check(
        "A-current-axiom-and-Block96-parent-authority",
        "origin/main, current axioms, and the complete Block96 theorem/runner chain are content-bound",
        authority["origin_main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["parent_note"] == PARENT_NOTE_BLOB
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_commit"] == PARENT_COMMIT
        and not authority["missing"]
        and not authority["loaded_missing"]
        and authority["parent_valid"],
        f"origin/main={str(authority['origin_main'])[:10]}; child missing/loaded={len(authority['missing'])}/{len(authority['loaded_missing'])}; parent loaded={len(authority['parent_loaded_missing'])}",
    )

    energy = energy_current_certificate(mutation)
    checks.check(
        "B-exact-free-scalar-local-energy-current-cochain",
        "one nearest-neighbour site energy and bond current obey the off-shell local identity and equal Block95 Ttt/Tti on every exact shell mode",
        energy["random_cases"] == 48
        and energy["local_error"] < TOL
        and energy["global_error"] < TOL
        and energy["modes"] == 247
        and energy["per_size"] == {3: 13, 4: 28, 5: 25, 6: 68, 7: 37, 8: 76}
        and energy["plane_error"] < TOL,
        f"random={energy['random_cases']}; local/global={error_bound(energy['local_error'])}/{error_bound(energy['global_error'])}; shell={energy['modes']} {energy['per_size']}; T match={error_bound(energy['plane_error'])}",
    )

    standing = standing_source_certificate(mutation)
    checks.check(
        "C-full-L5-counterpropagating-source-including-interference",
        "the exact two-wave source retains q=0 and both compulsory q=plus/minus 4pi/5 density components with Hermiticity, Ward closure, and nonnegative real-space density",
        standing["keys"] == standing["expected_keys"]
        and standing["expected_error"] < TOL
        and standing["hermiticity_error"] < TOL
        and standing["ward_error"] < TOL
        and standing["minimum_density"] > -TOL
        and standing["density_imaginary"] < TOL
        and standing["charge_error"] < TOL
        and standing["improvement_norm"] > 0.1,
        f"keys={sorted(standing['keys'])}; source/Hermitian/Ward={error_bound(standing['expected_error'])}/{error_bound(standing['hermiticity_error'])}/{error_bound(standing['ward_error'])}; min rho={standing['minimum_density']:.6f}; charge/improvement={error_bound(standing['charge_error'])}/{standing['improvement_norm']:.6f}",
    )

    trace_shear = trace_shear_certificate(mutation)
    checks.check(
        "D-q0-trace-shear-and-qnonzero-constraint-embedding",
        "the actual DeWitt map gives the trace/shear kinetic form, one axisymmetric shear resolves the full q=0 stress, and both interference densities solve Block78 constraints",
        trace_shear["rho"] > 0.0
        and trace_shear["decomposition_error"] < TOL
        and abs(
            trace_shear["trace_only_norm"] - trace_shear["trace_only_expected"]
        )
        < TOL
        and trace_shear["de_witt_error"] < TOL
        and trace_shear["inhomogeneous_modes"] == 2
        and trace_shear["inhomogeneous_error"] < TOL,
        f"rho={trace_shear['rho']:.6f}; decomposition/DeWitt/inhom={error_bound(trace_shear['decomposition_error'])}/{error_bound(trace_shear['de_witt_error'])}/{error_bound(trace_shear['inhomogeneous_error'])}; trace-only miss={trace_shear['trace_only_norm']:.6f}",
    )

    flow = reduced_flow_certificate(mutation)
    checks.check(
        "E-common-reduced-Hamiltonian-jet-and-dynamic-exchange",
        "the Block95 interaction gradient supplies one trace/shear Hamiltonian whose exact constrained flow matches the Block78 source momentum impulse",
        flow["cases"] == 64
        and flow["branch_counts"] == {-1: 32, 1: 32}
        and flow["jet_gradient_error"] < TOL
        and flow["flow_error"] < TOL
        and flow["constraint_error"] < TOL
        and flow["momentum_match_error"] < TOL
        and flow["coordinate_path_gap"] > 1.0e-4,
        f"cases/branches={flow['cases']}/{flow['branch_counts']}; jet/flow/C/kick={error_bound(flow['jet_gradient_error'])}/{error_bound(flow['flow_error'])}/{error_bound(flow['constraint_error'])}/{error_bound(flow['momentum_match_error'])}; chart gap={flow['coordinate_path_gap']:.4f}",
    )

    exchange = discrete_exchange_certificate(mutation)
    checks.check(
        "F-leading-front-step-exchange-defect-cancels",
        "the same matter-energy jet cancels the complete order-A^3 frozen-source residual on both volume-momentum branches, leaving order A^4",
        exchange["cases"] == 128
        and exchange["frozen_formula_error"] < TOL
        and exchange["jet_formula_error"] < TOL
        and exchange["cubic_cancellation_error"] < TOL
        and all(abs(slope - 3.0) < 0.03 for slope in exchange["frozen_slopes"])
        and all(abs(slope - 4.0) < 0.03 for slope in exchange["joint_slopes"]),
        f"cases={exchange['cases']}; formula/cancel={error_bound(exchange['frozen_formula_error'])}/{error_bound(exchange['jet_formula_error'])}/{error_bound(exchange['cubic_cancellation_error'])}; orders frozen/joint={exchange['frozen_slopes']}/{exchange['joint_slopes']}",
    )

    scope = scope_certificate(mutation)
    checks.check(
        "G-partial-coupled-exchange-and-TOE-scope",
        "the positive bridge does not claim the quartic action, full Ward identity, total Noether energy, Record compilation, retention, axiom change, or TOE movement",
        all(scope.values()),
    )

    no_go = no_go_certificate(mutation)
    checks.check(
        "H-no-go-discipline-demotes-every-gravity-negative",
        "N1 and N7 fail; the quartic remainder is a construction target and rejects neither bounded-local gravity nor the current axioms",
        no_go["headings"]
        and no_go["routes"]
        and no_go["attempted"]
        and no_go["n1_failed"]
        and no_go["n7_failed"]
        and no_go["overall_failed"]
        and no_go["narrow_only"]
        and no_go["steelman"]
        and no_go["echo"]
        and no_go["levels"]
        and no_go["valid"],
    )

    print(
        f"AXIOM_AUTHORITY: origin/main={authority['origin_main']} axiom={CURRENT_AXIOM_BLOB}; Block96 parent={PARENT_COMMIT}"
    )
    print(
        "per_element: checked — exact site energy, bond flux, q=0 trace/shear projections, and both volume-momentum branches"
    )
    print(
        "per_site: checked — the free scalar local balance and bounded L=5 standing-source support; the nonlinear joint action remains unconstructed"
    )
    print(
        "per_mode: checked — all 247 exact shell modes L=3..8 plus q=0 and both compulsory standing-wave interference transfers"
    )
    print(
        "per_block: checked — common reduced Hamiltonian flow and one-front-step defect improvement from order A^3 to order A^4"
    )
    print(
        "lattice_wide: checked and not executed — full order-h-phi^2 Ward closure, joint discrete Noether law, full-Z3 control, Record compilation, law selection, and retention remain open"
    )
    print(
        "RESULT: on diagonal plane-wave/q=0 coefficients Block95 Ttt/Tti equal the exact free-scalar energy/current cochain; the L=5 source requires trace plus one shear and two inhomogeneous density modes, and reciprocal q=0 matter work removes the leading frozen-source defect"
    )
    print(
        "PORTFOLIO: the next gravity calculation must solve the order-A^4 seagull/cubic/interference coefficient system from one common bounded-local action; a comparator-only result triggers a seam pivot"
    )
    print(
        "SCOPE: standing-wave local energy/source improvement matching, full nonlinear lattice gravity, total discrete Noether energy, Record compilation, selected law, axiom amendment, audit verdict, obligation retirement, retention, and TOE movement remain open"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
