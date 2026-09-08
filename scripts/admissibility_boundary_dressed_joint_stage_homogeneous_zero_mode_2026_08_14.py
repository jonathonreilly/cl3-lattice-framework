#!/usr/bin/env python3
"""Block 96: boundary-dressed joint stage and nonlinear homogeneous zero mode.

The Block78 front-loaded gravity macro is rewritten as the same variational
trajectory in endpoint-dressed canonical variables.  The dressing is the
gradient of a bounded-local matter--geometry boundary generator built from
the actual Block95 scalar stress, so its matter derivative is reciprocal
recoil rather than an external ledger.  The undressed variables retain the
exact Block78 constraints, while the dressed momentum carries the centered
matter current.

The compact positive Hamiltonian zero mode is tested separately in the exact
homogeneous flat-FRW Einstein--massless-scalar phase-space reduction.  A
homogeneous volume momentum balances positive scalar energy and gives an exact
discrete constrained action.  This matches the density component of the
Block95 obstruction, not its single travelling-mode current or full stress.
The rank-zero Block78 flat-vacuum row is the singular linearization at zero
volume momentum, not a density-sector gravity no-go.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import subprocess
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_BOUNDARY_DRESSED_JOINT_STAGE_HOMOGENEOUS_NONLINEAR_ZERO_MODE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md'
RUNNER_RELATIVE = (
    "scripts/admissibility_boundary_dressed_joint_stage_homogeneous_zero_"
    "mode_2026_08_14.py"
)
PARENT_NOTE = (
    "docs/ADMISSIBILITY_INCIDENCE_SCALAR_GRAPH_MATTER_FIRST_ORDER_TOTAL_"
    "WARD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_incidence_scalar_graph_matter_first_order_total_"
    "ward_cadence_boundary_2026_08_14.py"
)
BLOCK78_NOTE = (
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_INCIDENCE_ADM_DEPTH_TWO_SOURCED_CONSTRAINT_RECORD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md'
)
BLOCK79_NOTE = (
    "docs/ADMISSIBILITY_CYCLE713_RECORD_HEAD_ADM_WORK_ARCHIVE_STATE_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
BLOCK83_NOTE = (
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_COMPONENT_STAGGERED_SIGNED_LINK_ACTION_LOCAL_WARD_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md'
)
MINIMAL_AXIOMS = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_BOUNDARY_DRESSED_JOINT_STAGE_HOMOGENEOUS_NONLINEAR_ZERO_MODE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    'docs/ADMISSIBILITY_INCIDENCE_SCALAR_GRAPH_MATTER_FIRST_ORDER_TOTAL_WARD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    'docs/ADMISSIBILITY_INCIDENCE_FIERZ_PAULI_SIGNED_RECORD_SOURCE_FULL_TENSOR_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_INCIDENCE_ADM_DEPTH_TWO_SOURCED_CONSTRAINT_RECORD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    'docs/ADMISSIBILITY_CYCLE713_RECORD_HEAD_ADM_WORK_ARCHIVE_STATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_COMPONENT_STAGGERED_SIGNED_LINK_ACTION_LOCAL_WARD_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    'docs/ADMISSIBILITY_RAW_GRAPH_WARD_COMPACT_PULLBACK_TRANSLATION_GENERATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md',
    'docs/MINIMAL_AXIOMS_2026-06-29.md',
    'scripts/admissibility_boundary_dressed_joint_stage_homogeneous_zero_mode_2026_08_14.py',
    'scripts/admissibility_incidence_scalar_graph_matter_first_order_total_ward_cadence_boundary_2026_08_14.py',
    'scripts/admissibility_incidence_fierz_pauli_signed_record_source_full_tensor_cadence_boundary_2026_08_14.py',
    'scripts/admissibility_incidence_adm_depth_two_sourced_constraint_record_cadence_boundary_2026_08_14.py',
    'scripts/admissibility_component_staggered_signed_link_action_local_ward_boundary_2026_08_14.py',
    'scripts/admissibility_raw_graph_ward_compact_pullback_translation_generator_boundary_2026_08_14.py',
    'scripts/admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_2026_08_11.py',
)

CURRENT_MAIN = "eee6ab5874e2fc207db5526dc82d9f71ae550c7c"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
PARENT_COMMIT = "08357978a895b18a8832023e6e2f2fee652bb15e"
PARENT_NOTE_BLOB = "c2602c829ccb76813bf0df4f38a03ac6047ae751"
PARENT_RUNNER_BLOB = "96f76a38594ed655a0446b522211cc3ed2b83354"

DELTA = 0.5
COUPLING = 1.0
TOL = 3.0e-10

sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_incidence_scalar_graph_matter_first_order_total_ward_cadence_boundary_2026_08_14 as block95  # noqa: E402


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 180 else detail[:177] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def error_bound(value: float, tolerance: float = TOL) -> str:
    """Report gate resolution, not platform-dependent floating-point tails."""
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
    parent = block95.authority_certificate("")
    parent_loaded_missing = tuple(
        path for path in parent["loaded_missing"] if path != RUNNER_RELATIVE
    )
    parent_valid = (
        parent["origin_main"] == block95.CURRENT_AXIOM_COMMIT
        and parent["axiom"] == block95.CURRENT_AXIOM_BLOB
        and parent["block77"]
        == (block95.BLOCK77_NOTE_BLOB, block95.BLOCK77_RUNNER_BLOB)
        and parent["block78"]
        == (block95.BLOCK78_NOTE_BLOB, block95.BLOCK78_RUNNER_BLOB)
        and parent["block83"]
        == (block95.BLOCK83_NOTE_BLOB, block95.BLOCK83_RUNNER_BLOB)
        and parent["block93"]
        == (block95.BLOCK93_NOTE_BLOB, block95.BLOCK93_RUNNER_BLOB)
        and not parent["mismatches"]
        and not parent["missing"]
        and not parent_loaded_missing
    )
    return {
        "origin_main": git_output("rev-parse", "origin/main"),
        "axiom": worktree_blob(MINIMAL_AXIOMS),
        "expected_axiom": expected_axiom,
        "parent_note": worktree_blob(PARENT_NOTE),
        "parent_runner": worktree_blob(PARENT_RUNNER),
        "missing": missing,
        "loaded_missing": tuple(sorted(loaded - declared)),
        "parent_valid": parent_valid,
        "parent_mismatches": parent["mismatches"],
        "parent_loaded_missing": parent_loaded_missing,
        "parent_commit": git_output("rev-parse", PARENT_COMMIT),
    }


def hermitian_pair_vertices(
    incoming: np.ndarray, transfer: np.ndarray
) -> tuple[np.ndarray, ...]:
    """Hermitian two-mode realization of the actual six spatial stress slots."""
    stress = block95.centered_stress(incoming, transfer)
    coordinates = block95.tensor_coordinates3(stress[:3, :3])
    vertices = []
    for value in coordinates:
        matrix = np.zeros((2, 2), dtype=complex)
        matrix[1, 0] = value
        matrix[0, 1] = np.conj(value)
        vertices.append(matrix)
    return tuple(vertices)


def pair_force(amplitude: np.ndarray, vertices: tuple[np.ndarray, ...]) -> np.ndarray:
    return np.asarray(
        [float(np.real(np.vdot(amplitude, vertex @ amplitude))) for vertex in vertices]
    )


def boundary_generator(
    geometry: np.ndarray,
    amplitude: np.ndarray,
    vertices: tuple[np.ndarray, ...],
) -> float:
    return DELTA * COUPLING * float(np.dot(geometry, pair_force(amplitude, vertices)))


def amplitude_from_real(vector: np.ndarray) -> np.ndarray:
    """Invert x=(Re a, Im a) without sharing a stress-gradient formula."""
    values = np.asarray(vector, dtype=float)
    half = len(values) // 2
    return values[:half] + 1.0j * values[half:]


def geometry_gradient_from_generator(
    amplitude: np.ndarray,
    vertices: tuple[np.ndarray, ...],
    scale: float = 1.0,
) -> np.ndarray:
    """Extract dF/dh by evaluating the scalar generator on geometry bases."""
    zero = np.zeros(len(vertices))
    baseline = scale * boundary_generator(zero, amplitude, vertices)
    gradient = np.zeros(len(vertices))
    for index in range(len(vertices)):
        basis = np.zeros(len(vertices))
        basis[index] = 1.0
        gradient[index] = scale * boundary_generator(basis, amplitude, vertices) - baseline
    return gradient


def matter_gradient_from_generator(
    geometry: np.ndarray,
    real_amplitude: np.ndarray,
    vertices: tuple[np.ndarray, ...],
) -> np.ndarray:
    """Extract dF/dx by a central traversal of the quadratic scalar F."""
    values = np.asarray(real_amplitude, dtype=float)
    gradient = np.zeros(len(values))
    for index in range(len(values)):
        plus = values.copy()
        minus = values.copy()
        plus[index] += 1.0
        minus[index] -= 1.0
        gradient[index] = 0.5 * (
            boundary_generator(geometry, amplitude_from_real(plus), vertices)
            - boundary_generator(geometry, amplitude_from_real(minus), vertices)
        )
    return gradient


def boundary_action_certificate(mutation: str) -> dict[str, object]:
    rng = np.random.default_rng(9601)
    identity_error = geometry_error = mixed_error = 0.0
    recoil_norm = 0.0
    probes = 0
    for _ in range(48):
        incoming = rng.uniform(-np.pi, np.pi, 4)
        transfer = rng.uniform(-np.pi, np.pi, 4)
        vertices = hermitian_pair_vertices(incoming, transfer)
        h0 = rng.normal(size=6)
        h2 = rng.normal(size=6)
        a0 = rng.normal(size=2) + 1.0j * rng.normal(size=2)
        a2 = rng.normal(size=2) + 1.0j * rng.normal(size=2)
        f0 = pair_force(a0, vertices)
        f2 = pair_force(a2, vertices)

        front = 2.0 * DELTA * COUPLING * float(np.dot(h0, f0))
        endpoint = DELTA * COUPLING * (
            float(np.dot(h0, f0)) + float(np.dot(h2, f2))
        )
        difference = boundary_generator(h2, a2, vertices) - boundary_generator(
            h0, a0, vertices
        )
        identity_error = max(identity_error, abs(endpoint - front - difference))

        # Independently extract endpoint geometry gradients from scalar F.
        # The hostile control changes the candidate generator itself.
        generator_scale = 0.8 if mutation == "wrong_half_impulse" else 1.0
        observed_h0 = geometry_gradient_from_generator(
            a0, vertices, generator_scale
        )
        observed_h2 = geometry_gradient_from_generator(
            a2, vertices, generator_scale
        )
        geometry_error = max(
            geometry_error,
            float(np.max(np.abs(observed_h0 - DELTA * COUPLING * f0))),
            float(np.max(np.abs(observed_h2 - DELTA * COUPLING * f2))),
        )

        # Traverse the two derivative orders independently from scalar F:
        # matter-then-geometry uses matter gradients on geometry bases;
        # geometry-then-matter uses geometry gradients on matter bases.
        x = np.concatenate((a0.real, a0.imag))
        hessian_from_matter = np.zeros((len(x), len(vertices)))
        zero_geometry = np.zeros(len(vertices))
        zero_matter_gradient = matter_gradient_from_generator(
            zero_geometry, x, vertices
        )
        for geometry_index in range(len(vertices)):
            basis = np.zeros(len(vertices))
            basis[geometry_index] = 1.0
            hessian_from_matter[:, geometry_index] = (
                matter_gradient_from_generator(basis, x, vertices)
                - zero_matter_gradient
            )
        hessian_from_geometry = np.zeros((len(x), len(vertices)))
        for matter_index in range(len(x)):
            plus = x.copy()
            minus = x.copy()
            plus[matter_index] += 1.0
            minus[matter_index] -= 1.0
            hessian_from_geometry[matter_index, :] = 0.5 * (
                geometry_gradient_from_generator(
                    amplitude_from_real(plus), vertices
                )
                - geometry_gradient_from_generator(
                    amplitude_from_real(minus), vertices
                )
            )
        if mutation == "freeze_matter_boundary_recoil":
            hessian_from_geometry[:] = 0.0
        mixed_error = max(
            mixed_error,
            float(np.max(np.abs(hessian_from_matter - hessian_from_geometry))),
        )
        recoil_norm = max(recoil_norm, float(np.linalg.norm(hessian_from_matter)))
        probes += 1
    return {
        "probes": probes,
        "identity_error": identity_error,
        "geometry_error": geometry_error,
        "mixed_error": mixed_error,
        "recoil_norm": recoil_norm,
    }


@dataclass(frozen=True)
class SourceTransfer:
    size: int
    incoming: np.ndarray
    transfer: np.ndarray
    density: complex
    density_next: complex
    current_in: np.ndarray
    current_out: np.ndarray
    stress: np.ndarray


def source_transfers():
    for size in range(3, 9):
        shell: list[tuple[np.ndarray, np.ndarray]] = []
        for integer_mode in np.ndindex((size,) * 4):
            incoming = 2.0 * np.pi * np.asarray(integer_mode, dtype=float) / size
            if abs(block95.scalar_symbol(incoming)) < TOL:
                shell.append((np.asarray(integer_mode, dtype=int), incoming))
        for left in range(len(shell)):
            incoming_integer, incoming = shell[left]
            for outgoing_integer, _outgoing in shell[left + 1 :]:
                transfer_integer = (outgoing_integer - incoming_integer) % size
                if np.all(transfer_integer[:3] == 0):
                    continue
                transfer = 2.0 * np.pi * transfer_integer / size
                tensor = block95.centered_stress(incoming, transfer)
                if float(np.max(np.abs(tensor))) < 1.0e-9:
                    continue
                spatial, density, density_next, current_in, current_out, stress = (
                    block95.cadence_data(transfer, tensor)
                )
                assert np.max(np.abs(spatial - transfer[:3])) < TOL
                yield SourceTransfer(
                    size,
                    incoming,
                    transfer,
                    density,
                    density_next,
                    current_in,
                    current_out,
                    stress,
                )


def front_macro(
    h0: np.ndarray,
    pi0: np.ndarray,
    stress: np.ndarray,
    kinetic: np.ndarray,
    potential: np.ndarray,
    hamiltonian: np.ndarray,
    shift: np.ndarray,
    lapse0: complex,
    lapse1: complex,
    beta0: np.ndarray,
    beta1: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    pi1 = pi0 + DELTA * (
        -potential @ h0
        + hamiltonian.conj().T[:, 0] * lapse0
        + 2.0 * COUPLING * stress
    )
    h1 = h0 + DELTA * (kinetic @ pi1 + shift @ beta0)
    pi2 = pi1 + DELTA * (
        -potential @ h1 + hamiltonian.conj().T[:, 0] * lapse1
    )
    h2 = h1 + DELTA * (kinetic @ pi2 + shift @ beta1)
    return h1, pi1, h2, pi2


def dressed_macro(
    h0: np.ndarray,
    dressed_pi0: np.ndarray,
    stress0: np.ndarray,
    stress2: np.ndarray,
    kinetic: np.ndarray,
    potential: np.ndarray,
    hamiltonian: np.ndarray,
    shift: np.ndarray,
    lapse0: complex,
    lapse1: complex,
    beta0: np.ndarray,
    beta1: np.ndarray,
    mutation: str,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    half_coefficient = 1.0
    pi1 = dressed_pi0 + DELTA * (
        -potential @ h0
        + hamiltonian.conj().T[:, 0] * lapse0
        + half_coefficient * COUPLING * stress0
    )
    h1 = h0 + DELTA * (kinetic @ pi1 + shift @ beta0)
    pi2 = pi1 + DELTA * (
        -potential @ h1 + hamiltonian.conj().T[:, 0] * lapse1
    )
    h2 = h1 + DELTA * (kinetic @ pi2 + shift @ beta1)
    dressed_pi2 = pi2 + DELTA * COUPLING * stress2
    if mutation == "omit_terminal_dressing":
        dressed_pi2 = pi2.copy()
    return h1, pi1, h2, dressed_pi2


def stage_and_constraint_certificate(mutation: str) -> dict[str, object]:
    modes = 0
    per_size: dict[int, int] = {}
    map_error = source_error = front_constraint_error = dressed_constraint_error = 0.0
    rng = np.random.default_rng(9602)
    for data in source_transfers():
        p = block95.block77.block53.lattice_vector(data.transfer[:3])
        kinetic, potential, hamiltonian, momentum, shift = block95.spatial_operators(p)
        h0 = np.linalg.pinv(hamiltonian, rcond=1.0e-12) @ np.asarray(
            (COUPLING * data.density,)
        )
        pi0 = np.linalg.pinv(momentum, rcond=1.0e-12) @ (
            2.0 * COUPLING * data.current_in
        )
        # Nonzero gauge multipliers exercise the complete update but do not
        # participate in the source dressing.
        lapse0 = 0.13 + 0.02j * np.sin(float(np.sum(data.transfer)))
        lapse1 = -0.09 + 0.03j * np.cos(float(np.sum(data.incoming)))
        beta0 = rng.normal(size=3) * 0.03
        beta1 = rng.normal(size=3) * 0.03
        phase = np.exp(1.0j * data.transfer[3])
        stress2 = phase * data.stress
        current_in2 = phase * data.current_in
        current_out2 = phase * data.current_out

        front = front_macro(
            h0,
            pi0,
            data.stress,
            kinetic,
            potential,
            hamiltonian,
            shift,
            lapse0,
            lapse1,
            beta0,
            beta1,
        )
        dressed_pi0 = pi0 + DELTA * COUPLING * data.stress
        dressed = dressed_macro(
            h0,
            dressed_pi0,
            data.stress,
            stress2,
            kinetic,
            potential,
            hamiltonian,
            shift,
            lapse0,
            lapse1,
            beta0,
            beta1,
            mutation,
        )
        undressed_pi2 = dressed[3] - DELTA * COUPLING * stress2
        map_error = max(
            map_error,
            float(np.max(np.abs(front[0] - dressed[0]))),
            float(np.max(np.abs(front[1] - dressed[1]))),
            float(np.max(np.abs(front[2] - dressed[2]))),
            float(np.max(np.abs(front[3] - undressed_pi2))),
        )

        derivative = 1.0j * p
        tensor = block95.coordinate_tensor3(data.stress)
        source_error = max(
            source_error,
            abs(data.density_next - data.density + derivative @ data.current_out),
            float(
                np.max(
                    np.abs(
                        data.current_out
                        - data.current_in
                        + 1.0j * (tensor @ p)
                    )
                )
            ),
            float(np.max(np.abs(momentum @ data.stress - 2.0 * (data.current_out - data.current_in)))),
        )
        midpoint_density = data.density - 0.5 * derivative @ data.current_out
        front_constraint_error = max(
            front_constraint_error,
            float(np.max(np.abs(momentum @ front[1] - 2.0 * COUPLING * data.current_out))),
            float(np.max(np.abs(momentum @ front[3] - 2.0 * COUPLING * data.current_out))),
            abs((hamiltonian @ front[0])[0] - COUPLING * midpoint_density),
            abs((hamiltonian @ front[2])[0] - COUPLING * data.density_next),
        )
        initial_target = COUPLING * (data.current_in + data.current_out)
        final_target = COUPLING * (current_in2 + current_out2)
        if mutation == "wrong_current_improvement":
            initial_target = 2.0 * COUPLING * data.current_out
        constraint_dressed_pi2 = dressed[3]
        if mutation == "omit_terminal_dressing":
            # Gate C owns the omitted-map output.  Gate D independently tests
            # the constraint identity after applying the declared dressing.
            constraint_dressed_pi2 = constraint_dressed_pi2 + DELTA * COUPLING * stress2
        dressed_constraint_error = max(
            dressed_constraint_error,
            float(np.max(np.abs(momentum @ dressed_pi0 - initial_target))),
            float(np.max(np.abs(momentum @ constraint_dressed_pi2 - final_target))),
            abs((hamiltonian @ dressed[0])[0] - COUPLING * midpoint_density),
            abs((hamiltonian @ dressed[2])[0] - COUPLING * data.density_next),
        )
        per_size[data.size] = per_size.get(data.size, 0) + 1
        modes += 1
    return {
        "modes": modes,
        "per_size": per_size,
        "map_error": map_error,
        "source_error": source_error,
        "front_constraint_error": front_constraint_error,
        "dressed_constraint_error": dressed_constraint_error,
    }


def locality_covariance_certificate(mutation: str) -> dict[str, object]:
    coefficients = block95.stress_laurent_coefficients()
    support = block95.support_shape(coefficients)
    if mutation == "fake_boundary_locality":
        support = (support[0] + 1,) + support[1:]
    rng = np.random.default_rng(9603)
    covariance_error = 0.0
    probes = 0
    for _ in range(12):
        incoming = rng.uniform(-np.pi, np.pi, 4)
        transfer = rng.uniform(-np.pi, np.pi, 4)
        base = block95.centered_stress(incoming, transfer)
        for rotation in block95.block77.ROTATIONS:
            transform = np.eye(4)
            transform[:3, :3] = rotation
            observed = block95.centered_stress(transform @ incoming, transform @ transfer)
            expected = transform @ base @ transform.T
            covariance_error = max(
                covariance_error, float(np.max(np.abs(observed - expected)))
            )
            probes += 1
    return {
        "support": support,
        "terms": sum(np.count_nonzero(np.abs(value) > TOL) for value in coefficients.values()),
        "covariance_error": covariance_error,
        "probes": probes,
    }


def homogeneous_constraint(
    p_alpha: complex | float, p_phi: complex | float, mutation: str = ""
) -> complex | float:
    gravity_sign = 1.0 if mutation == "wrong_gravity_sign" else -1.0
    return gravity_sign * p_alpha**2 / 12.0 + p_phi**2 / 2.0


def homogeneous_two_step_action(
    variables: np.ndarray,
    alpha_initial: float,
    phi_initial: float,
    alpha_final: float,
    phi_final: float,
    step: float,
    mutation: str,
) -> complex | float:
    """Two-step phase-space action with only internal/canonical variables free."""
    (
        alpha_middle,
        phi_middle,
        p_alpha_0,
        p_phi_0,
        p_alpha_1,
        p_phi_1,
        lapse_0,
        lapse_1,
    ) = variables
    return (
        p_alpha_0 * (alpha_middle - alpha_initial)
        + p_phi_0 * (phi_middle - phi_initial)
        - step * lapse_0 * homogeneous_constraint(p_alpha_0, p_phi_0, mutation)
        + p_alpha_1 * (alpha_final - alpha_middle)
        + p_phi_1 * (phi_final - phi_middle)
        - step * lapse_1 * homogeneous_constraint(p_alpha_1, p_phi_1, mutation)
    )


def complex_step_gradient(function, values: np.ndarray) -> np.ndarray:
    """Differentiate an analytic scalar traversal without subtractive cancellation."""
    step = 1.0e-30
    gradient = np.zeros(len(values))
    for index in range(len(values)):
        probe = np.asarray(values, dtype=complex)
        probe[index] += 1.0j * step
        gradient[index] = float(np.imag(function(probe)) / step)
    return gradient


def homogeneous_action_certificate(mutation: str) -> dict[str, object]:
    rng = np.random.default_rng(9604)
    constraint_error = el_error = momentum_error = friedmann_error = 0.0
    minimum_density = np.inf
    branch_counts = {-1: 0, 1: 0}
    cases = 0
    for case in range(512):
        alpha = rng.uniform(-3.0, 3.0)
        phi = rng.normal()
        density = float(10.0 ** rng.uniform(-8.0, 4.0))
        scale = float(np.exp(alpha))
        p_phi = float(np.sqrt(2.0 * density) * scale**3)
        if rng.integers(0, 2):
            p_phi *= -1.0
        branch_sign = -1 if case % 2 else 1
        p_alpha = float(branch_sign * np.sqrt(6.0) * p_phi)
        branch_counts[branch_sign] += 1
        if mutation == "remove_volume_momentum":
            p_alpha = 0.0
        lapse_0 = float(10.0 ** rng.uniform(-2.0, 1.0))
        lapse_1 = float(10.0 ** rng.uniform(-2.0, 1.0))
        step = float(rng.uniform(0.01, 0.4))
        alpha_middle = alpha - step * lapse_0 * p_alpha / 6.0
        phi_middle = phi + step * lapse_0 * p_phi
        alpha_final = alpha_middle - step * lapse_1 * p_alpha / 6.0
        phi_final = phi_middle + step * lapse_1 * p_phi
        variables = np.asarray(
            (
                alpha_middle,
                phi_middle,
                p_alpha,
                p_phi,
                p_alpha,
                p_phi,
                lapse_0,
                lapse_1,
            ),
            dtype=float,
        )
        action_gradient = complex_step_gradient(
            lambda values: homogeneous_two_step_action(
                values,
                alpha,
                phi,
                alpha_final,
                phi_final,
                step,
                mutation,
            ),
            variables,
        )
        constraint_scale = max(1.0, p_alpha**2 / 12.0, p_phi**2 / 2.0)
        constraint_error = max(
            constraint_error,
            abs(action_gradient[6]) / (step * constraint_scale),
            abs(action_gradient[7]) / (step * constraint_scale),
        )
        momentum_error = max(
            momentum_error,
            abs(action_gradient[0]) / max(1.0, abs(p_alpha)),
            abs(action_gradient[1]) / max(1.0, abs(p_phi)),
        )
        el_scales = (
            max(1.0, abs(alpha_middle - alpha), step * lapse_0 * abs(p_alpha) / 6.0),
            max(1.0, abs(phi_middle - phi), step * lapse_0 * abs(p_phi)),
            max(
                1.0,
                abs(alpha_final - alpha_middle),
                step * lapse_1 * abs(p_alpha) / 6.0,
            ),
            max(1.0, abs(phi_final - phi_middle), step * lapse_1 * abs(p_phi)),
        )
        el_error = max(
            el_error,
            *(abs(action_gradient[index]) / el_scales[index - 2] for index in range(2, 6)),
        )
        hubble = -p_alpha / (6.0 * scale**3)
        observed_density = p_phi**2 / (2.0 * scale**6)
        friedmann_error = max(
            friedmann_error,
            abs(3.0 * hubble**2 - observed_density) / max(1.0, observed_density),
        )
        minimum_density = min(minimum_density, observed_density)
        cases += 1

    # Positive homogeneous Hamiltonian comparator: rho=1 at a=1.  It matches
    # Block95's obstructed Ttt datum, not that travelling mode's full tensor.
    fixture_p_phi = np.sqrt(2.0)
    fixture_p_alpha = np.sqrt(12.0)
    if mutation == "remove_volume_momentum":
        fixture_p_alpha = 0.0
    fixture_constraint = abs(
        homogeneous_constraint(fixture_p_alpha, fixture_p_phi, mutation)
    )
    fixture_hubble_squared = (fixture_p_alpha / 6.0) ** 2
    return {
        "cases": cases,
        "constraint_error": constraint_error,
        "el_error": el_error,
        "momentum_error": momentum_error,
        "friedmann_error": friedmann_error,
        "minimum_density": minimum_density,
        "branch_counts": branch_counts,
        "fixture_constraint": fixture_constraint,
        "fixture_hubble_squared": fixture_hubble_squared,
    }


def singular_flat_expansion_certificate(mutation: str) -> dict[str, object]:
    epsilon = np.logspace(-12.0, -2.0, 21)
    exact = np.sqrt(12.0 * epsilon)
    exact_error = float(
        np.max(np.abs(-exact**2 / 12.0 + epsilon))
    )
    slope = float(np.polyfit(np.log(epsilon), np.log(exact), 1)[0])
    constraint_polynomial = np.polynomial.Polynomial((0.0, 0.0, -1.0 / 12.0))
    constraint_derivative = constraint_polynomial.deriv()
    flat_rank = int(
        np.linalg.matrix_rank(
            np.asarray([[constraint_derivative(0.0)]]), tol=TOL
        )
    )
    branch_momentum = float(np.sqrt(12.0))
    branch_rank = int(
        np.linalg.matrix_rank(
            np.asarray([[constraint_derivative(branch_momentum)]]), tol=TOL
        )
    )

    # Extract the order-epsilon residual coefficient from a general finite
    # integer-power family.  The gravity square is computed by polynomial
    # multiplication, so neither its valuation nor the source coefficient is
    # inserted as the expected answer.
    rng = np.random.default_rng(9605)
    polynomial_cases = 96
    coefficient_error = 0.0
    minimum_gravity_order = 100
    for case in range(polynomial_cases):
        degree = 1 + case % 8
        coefficients = np.zeros(degree + 1)
        coefficients[1:] = rng.normal(size=degree)
        if abs(coefficients[1]) < 0.2:
            coefficients[1] += 1.0
        momentum = np.polynomial.Polynomial(coefficients)
        gravity = momentum * momentum / 12.0
        expected_source_coefficient = float(10.0 ** rng.uniform(-4.0, 4.0))
        observed_source_coefficient = (
            0.0 if mutation == "claim_analytic_flat_repair" else expected_source_coefficient
        )
        source = np.polynomial.Polynomial((0.0, observed_source_coefficient))
        residual = source - gravity
        observed_coefficient = residual.coef[1] if len(residual.coef) > 1 else 0.0
        coefficient_error = max(
            coefficient_error,
            abs(observed_coefficient - expected_source_coefficient)
            / max(1.0, expected_source_coefficient),
        )
        nonzero_orders = np.flatnonzero(np.abs(gravity.coef) > 1.0e-14)
        minimum_gravity_order = min(minimum_gravity_order, int(nonzero_orders[0]))

    background = 2.7
    perturbation = 1.0e-7
    exact_background = np.sqrt(background**2 + 12.0 * perturbation)
    linear_background = background + 6.0 * perturbation / background
    background_error = abs(exact_background - linear_background)
    return {
        "exact_error": exact_error,
        "slope": slope,
        "flat_rank": flat_rank,
        "branch_rank": branch_rank,
        "background_error": background_error,
        "polynomial_cases": polynomial_cases,
        "coefficient_error": coefficient_error,
        "minimum_gravity_order": minimum_gravity_order,
    }


def scope_certificate(mutation: str) -> dict[str, bool]:
    note = flat(NOTE_PATH)
    result = {
        "bounded_stage": "boundary-dressed first-order stage theorem" in note,
        "homogeneous_only": "homogeneous nonlinear zero-mode counterconstruction" in note,
        "inhomogeneous_open": "inhomogeneous nonlinear ward and constraint algebra remains open" in note,
        "record_open": "record compiler, law selection, and independent retention remain open" in note,
        "no_axiom": "no axiom amendment is forced" in note,
        "zero_score": all(
            phrase in note
            for phrase in (
                "zero obligation retirement",
                "no toe percentage moves",
                "retained-positive end-to-end theory count remains zero",
            )
        ),
    }
    if mutation == "claim_full_nonlinear":
        result["inhomogeneous_open"] = False
    if mutation == "claim_toe_progress":
        result["zero_score"] = False
    return result


def no_go_certificate(mutation: str) -> dict[str, object]:
    note = flat(NOTE_PATH)
    routes = (
        "integer-power flat-vacuum series",
        "puiseux square-root branch",
        "nonzero homogeneous momentum background",
        "open boundary or boundary flux",
        "cosmological or compensating background term",
        "signed or zero-mean source sector",
    )
    return {
        "headings": all(f"n{index}" in note for index in range(1, 9)),
        "routes": all(route in note for route in routes),
        "attempted": note.count("attempted"),
        "out_of_contract": note.count("out of contract — not counted"),
        "exact_target": all(
            phrase in note
            for phrase in (
                "fixed homogeneous constraint",
                "c=-p_alpha^2/12+epsilon e_1",
                "e_1>0",
            )
        ),
        "demoted": "broad compact-gravity no-go fails" in note,
        "steelman": "strongest steelman" in note,
        "echo": "cross-cycle echo" in note,
        "n5": all(
            marker in note
            for marker in ("per-element", "per-site", "per-mode", "per-block", "lattice-wide")
        ),
        "n1_failed": "n1 status: `fail`" in note,
        "n7_failed": "n7 status: `fail`" in note,
        "overall_failed": "overall no-go-discipline status: `fail — partial-narrowing`" in note,
        "observation_only": "algebraic observation only" in note,
        "valid": mutation != "weaken_no_go_packet",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutation",
        choices=(
            "stale_axiom_authority",
            "wrong_half_impulse",
            "freeze_matter_boundary_recoil",
            "omit_terminal_dressing",
            "wrong_current_improvement",
            "fake_boundary_locality",
            "wrong_gravity_sign",
            "remove_volume_momentum",
            "claim_analytic_flat_repair",
            "claim_full_nonlinear",
            "weaken_no_go_packet",
            "claim_toe_progress",
        ),
        default="",
    )
    mutation = parser.parse_args().mutation
    checks = Checks()

    authority = authority_certificate(mutation)
    checks.check(
        "A-current-axiom-and-Block95-parent-authority",
        "origin/main, current axioms, and the complete Block95 parent theorem/runner are content-bound",
        authority["origin_main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["parent_note"] == PARENT_NOTE_BLOB
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_commit"] == PARENT_COMMIT
        and not authority["missing"]
        and not authority["loaded_missing"]
        and authority["parent_valid"],
        f"origin/main={str(authority['origin_main'])[:10]}; child missing/loaded={len(authority['missing'])}/{len(authority['loaded_missing'])}; parent mismatch/loaded={len(authority['parent_mismatches'])}/{len(authority['parent_loaded_missing'])}",
    )

    boundary = boundary_action_certificate(mutation)
    checks.check(
        "B-dynamic-boundary-generator-and-reciprocal-matter-dressing",
        "one endpoint boundary scalar converts the full prepoint stress into two half impulses and supplies reciprocal matter recoil",
        boundary["probes"] == 48
        and boundary["identity_error"] < TOL
        and boundary["geometry_error"] < TOL
        and boundary["mixed_error"] < TOL
        and boundary["recoil_norm"] > 0.1,
        f"probes={boundary['probes']}; action/geometry/mixed={error_bound(boundary['identity_error'])}/{error_bound(boundary['geometry_error'])}/{error_bound(boundary['mixed_error'])}; recoil={boundary['recoil_norm']:.2f}",
    )

    stage = stage_and_constraint_certificate(mutation)
    checks.check(
        "C-endpoint-dressed-map-is-the-Block78-front-trajectory",
        "the half-source initial kick plus terminal dressing is exactly conjugate to every front-loaded scalar-source macro",
        stage["modes"] == 6354
        and stage["per_size"] == {3: 66, 4: 360, 5: 276, 6: 2226, 7: 630, 8: 2796}
        and stage["map_error"] < TOL,
        f"modes={stage['modes']}; per-size={stage['per_size']}; map={error_bound(stage['map_error'])}",
    )
    checks.check(
        "D-front-and-dressed-current-constraints",
        "undressed momenta retain outgoing Block78 constraints while dressed endpoint momenta carry the centered current improvement",
        stage["source_error"] < TOL
        and stage["front_constraint_error"] < TOL
        and stage["dressed_constraint_error"] < TOL,
        f"source/front/dressed={error_bound(stage['source_error'])}/{error_bound(stage['front_constraint_error'])}/{error_bound(stage['dressed_constraint_error'])}",
    )

    locality = locality_covariance_certificate(mutation)
    checks.check(
        "E-bounded-local-proper-cubic-boundary-dressing",
        "the generator reuses the actual finite Block95 stress vertex and adds no inverse incidence or growing support",
        locality["support"] == (33, 2, 2, 1, 2, 4)
        and locality["terms"] == 36
        and locality["probes"] == 288
        and locality["covariance_error"] < TOL,
        f"support={locality['support']}; terms={locality['terms']}; frame probes/error={locality['probes']}/{error_bound(locality['covariance_error'])}",
    )

    homogeneous = homogeneous_action_certificate(mutation)
    checks.check(
        "F-positive-homogeneous-density-zero-mode-has-a-nonlinear-gravity-branch",
        "one homogeneous-reduced densitized ADM phase-space action balances positive scalar energy with volume momentum",
        homogeneous["cases"] == 512
        and homogeneous["constraint_error"] < TOL
        and homogeneous["el_error"] < TOL
        and homogeneous["momentum_error"] < TOL
        and homogeneous["friedmann_error"] < TOL
        and homogeneous["minimum_density"] > 0.0
        and homogeneous["branch_counts"] == {-1: 256, 1: 256}
        and homogeneous["fixture_constraint"] < TOL
        and abs(homogeneous["fixture_hubble_squared"] - 1.0 / 3.0) < TOL,
        f"cases/branches={homogeneous['cases']}/{homogeneous['branch_counts']}; C/EL/p-const/Friedmann={error_bound(homogeneous['constraint_error'])}/{error_bound(homogeneous['el_error'])}/{error_bound(homogeneous['momentum_error'])}/{error_bound(homogeneous['friedmann_error'])}; rho=1 H^2={homogeneous['fixture_hubble_squared']:.6f}",
    )

    singular = singular_flat_expansion_certificate(mutation)
    checks.check(
        "G-fixed-equation-coefficient-valuation-and-square-root-comparator",
        "the fixed homogeneous constraint has an uncancelled integer-power order-epsilon coefficient, an exact square-root branch, and regular nonzero-background response",
        singular["exact_error"] < TOL
        and abs(singular["slope"] - 0.5) < 1.0e-12
        and singular["flat_rank"] == 0
        and singular["branch_rank"] == 1
        and singular["background_error"] < 1.0e-12
        and singular["polynomial_cases"] == 96
        and singular["coefficient_error"] < TOL
        and singular["minimum_gravity_order"] >= 2,
        f"sqrt error/slope={error_bound(singular['exact_error'])}/{singular['slope']:.6f}; polynomial cases/coefficient error/order={singular['polynomial_cases']}/{error_bound(singular['coefficient_error'])}/{singular['minimum_gravity_order']}; ranks={singular['flat_rank']}/{singular['branch_rank']}",
    )

    scope = scope_certificate(mutation)
    checks.check(
        "H-first-order-stage-homogeneous-nonlinear-and-TOE-scope",
        "the two positive constructions do not claim inhomogeneous nonlinear, Record, law-selection, retention, or TOE closure",
        all(scope.values()),
    )

    no_go = no_go_certificate(mutation)
    checks.check(
        "I-no-go-discipline-demotes-the-flat-series-negative",
        "N1 and N7 fail, so the exact coefficient valuation remains an observation and every gravity-negative conclusion is demoted",
        no_go["headings"]
        and no_go["routes"]
        and no_go["attempted"] >= 1
        and no_go["out_of_contract"] >= 6
        and no_go["exact_target"]
        and no_go["demoted"]
        and no_go["steelman"]
        and no_go["echo"]
        and no_go["n5"]
        and no_go["n1_failed"]
        and no_go["n7_failed"]
        and no_go["overall_failed"]
        and no_go["observation_only"]
        and no_go["valid"],
        f"ATTEMPTED={no_go['attempted']}; out-of-contract={no_go['out_of_contract']}; N1/N7/overall fail={no_go['n1_failed']}/{no_go['n7_failed']}/{no_go['overall_failed']}",
    )

    print(
        f"AXIOM_AUTHORITY: origin/main={authority['origin_main']} axiom={CURRENT_AXIOM_BLOB}; Block95 parent={PARENT_COMMIT}"
    )
    print(
        "per_element: checked — six actual scalar-stress coordinates, both endpoint impulses, reciprocal matter derivatives, and the homogeneous lapse constraint"
    )
    print(
        "per_site: checked — the 33-support Block95 boundary generator and two endpoint dressings; the zero-mode action is homogeneous-reduced, not a full sitewise lattice realization"
    )
    print(
        "per_mode: checked — all 6,354 exact massless-shell L=3..8 transfers, their source Ward equations, and front/dressed current constraints"
    )
    print(
        "per_block: checked — boundary-action equivalence, canonical map conjugacy, constraint propagation, and the exact homogeneous nonlinear scalar-gravity action"
    )
    print(
        "lattice_wide: checked and not executed — inhomogeneous nonlinear Ward closure, inter-sector gluing, full-Z3 control, Record compilation, law selection, and retention remain open"
    )
    print(
        "RESULT: the front-loaded source cadence has a bounded-local dynamic endpoint-dressed variational chart, and positive compact homogeneous density has an exact nonlinear gravity constraint branch"
    )
    print(
        "PORTFOLIO: stop treating the flat q=0 residual as a gravity failure; next couple the homogeneous trace pair to inhomogeneous Block95/78 modes and execute the order-h-phi^2 Ward algebra"
    )
    print(
        "SCOPE: no full nonlinear lattice gravity, Record compiler, selected physical law, axiom amendment, audit verdict, obligation retirement, retained end-to-end theory, or TOE percentage movement"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
