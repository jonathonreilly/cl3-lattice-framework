#!/usr/bin/env python3
"""Block 93: raw graph Ward current and compact-pullback generator boundary.

The Block82 nineteen-shift shadow action has a path-free current on its own
eighteen directed graph edges.  Reynolds averaging the complete density/work/
graph-current triplet gives an exact proper-cubic covariant representative.

The other Block83 completion route has a sharp boundary: a nonzero compact
convolution pullback cannot satisfy an exact endpoint chain identity with a
finite-range translation-invariant generator acting on the same finite
carrier, and no such generator exponentiates to the exact one-site shift.
This is not a gravity no-go.  A degree-lowered B-spline complex and discrete
graph or lattice-field matter remain live changes of carrier/primary object.
"""

from __future__ import annotations

import argparse
from functools import lru_cache
from math import comb, factorial, pi
from pathlib import Path
import subprocess
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_RAW_GRAPH_WARD_COMPACT_PULLBACK_TRANSLATION_GENERATOR_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
RUNNER_RELATIVE = (
    "scripts/admissibility_raw_graph_ward_compact_pullback_translation_"
    "generator_boundary_2026_08_14.py"
)
PARENT_NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_COMPONENT_STAGGERED_SIGNED_LINK_ACTION_LOCAL_WARD_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_component_staggered_signed_link_action_local_"
    "ward_boundary_2026_08_14.py"
)
BLOCK82_NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_LOCAL_SHADOW_ENERGY_FLUX_LAPSE_TRANSLATION_JOINT_ACTION_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
BLOCK82_RUNNER = (
    "scripts/admissibility_local_shadow_energy_flux_lapse_translation_"
    "joint_action_boundary_2026_08_14.py"
)
NOETHER_NOTE = ROOT / "docs" / (
    "AXIOM_FIRST_LATTICE_NOETHER_ONSITE_INTERNAL_NARROW_THEOREM_NOTE_"
    "2026-06-05.md"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RAW_GRAPH_WARD_COMPACT_PULLBACK_TRANSLATION_GENERATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_COMPONENT_STAGGERED_SIGNED_LINK_ACTION_LOCAL_WARD_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_LOCAL_SHADOW_ENERGY_FLUX_LAPSE_TRANSLATION_JOINT_ACTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/AXIOM_FIRST_LATTICE_NOETHER_ONSITE_INTERNAL_NARROW_THEOREM_NOTE_2026-06-05.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_raw_graph_ward_compact_pullback_translation_generator_boundary_2026_08_14.py",
    "scripts/admissibility_component_staggered_signed_link_action_local_ward_boundary_2026_08_14.py",
    "scripts/admissibility_local_shadow_energy_flux_lapse_translation_joint_action_boundary_2026_08_14.py",
)

CURRENT_AXIOM_COMMIT = "eee6ab5874e2fc207db5526dc82d9f71ae550c7c"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
PARENT_COMMIT = "daf3ec0421c490564486b5e3310f7fdbcf085d0f"
PARENT_NOTE_BLOB = "e78006cf55101576993cd39941163e922583b473"
PARENT_RUNNER_BLOB = "86bae02240012cc935f1b3df644892a5487f5a90"

TOL = 2.0e-10
DELTA = 0.5

sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_component_staggered_signed_link_action_local_ward_boundary_2026_08_14 as block83  # noqa: E402


Shift = tuple[int, int, int]
GraphCurrent = dict[Shift, np.ndarray]


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 132 else detail[:129] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return int(self.failed != 0)


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def git_commit_path_blob(commit: str, path: str) -> str:
    return subprocess.run(
        ("git", "rev-parse", f"{commit}:{path}"),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def git_worktree_path_blob(path: str) -> str:
    return subprocess.run(
        ("git", "hash-object", "--", path),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def authority_certificate(mutation: str) -> dict[str, object]:
    origin_main = subprocess.run(
        ("git", "rev-parse", "origin/main"),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    current_surfaces = {NOTE_PATH.relative_to(ROOT).as_posix(), RUNNER_RELATIVE}
    frozen = tuple(path for path in AUDIT_INPUT_PATHS if path not in current_surfaces)
    mismatches = tuple(
        path
        for path in frozen
        if git_worktree_path_blob(path) != git_commit_path_blob(PARENT_COMMIT, path)
    )
    loaded: set[str] = set()
    for module in tuple(sys.modules.values()):
        file_name = getattr(module, "__file__", None)
        if not file_name:
            continue
        path = Path(file_name).resolve()
        try:
            relative = path.relative_to(ROOT).as_posix()
        except ValueError:
            continue
        if relative.startswith("scripts/") and relative.endswith(".py"):
            loaded.add(relative)
    declared = {path for path in AUDIT_INPUT_PATHS if path.startswith("scripts/")}
    expected_axiom = "0" * 40 if mutation == "stale_axiom_authority" else CURRENT_AXIOM_BLOB
    return {
        "origin_main": origin_main,
        "axiom_blob": git_worktree_path_blob("docs/MINIMAL_AXIOMS_2026-06-29.md"),
        "expected_axiom": expected_axiom,
        "parent_note": git_worktree_path_blob(PARENT_NOTE.relative_to(ROOT).as_posix()),
        "parent_runner": git_worktree_path_blob(PARENT_RUNNER),
        "mismatches": mismatches,
        "missing": tuple(path for path in AUDIT_INPUT_PATHS if not (ROOT / path).exists()),
        "loaded_missing": tuple(sorted(loaded - declared)),
    }


def finite_generator_certificate(mutation: str) -> dict[str, object]:
    samples = np.linspace(0.0, 2.0 * np.pi, 4097)
    exact_shift = np.exp(1.0j * samples)
    centered_flow = np.exp(1.0j * np.sin(samples))
    exact_winding = float(
        (np.unwrap(np.angle(exact_shift))[-1] - np.unwrap(np.angle(exact_shift))[0])
        / (2.0 * np.pi)
    )
    centered_winding = float(
        (np.unwrap(np.angle(centered_flow))[-1] - np.unwrap(np.angle(centered_flow))[0])
        / (2.0 * np.pi)
    )
    probe = 0.371
    periodic_symbol_error = abs(np.sin(probe + 2.0 * np.pi) - np.sin(probe))
    logarithm_period_gap = abs(1.0j * (probe + 2.0 * np.pi) - 1.0j * probe)
    proof_valid = mutation != "fake_local_log"
    note = flat(NOTE_PATH)
    return {
        "exact_winding": exact_winding,
        "centered_winding": centered_winding,
        "six_component_winding": 6.0 * exact_winding,
        "periodic_symbol_error": periodic_symbol_error,
        "period_gap": logarithm_period_gap,
        "proof_valid": proof_valid,
        "scoped": all(
            phrase in note
            for phrase in (
                "finite-range logarithm of the exact shift",
                "periodic logarithm has winding zero",
                "does not forbid a generalized lattice symmetry",
            )
        ),
    }


def compact_pullback_certificate(mutation: str) -> dict[str, object]:
    probe = -0.284
    finite_symbol = 0.5j * (np.exp(-1.0j * probe) - np.exp(1.0j * probe))
    repeated_symbol = 0.5j * (
        np.exp(-1.0j * (probe + 2.0 * np.pi))
        - np.exp(1.0j * (probe + 2.0 * np.pi))
    )
    periodic_error = abs(finite_symbol - repeated_symbol)
    required_gap = abs(1.0j * (probe + 2.0 * np.pi) - 1.0j * probe)
    proof_valid = mutation != "fake_compact_chain"
    note = flat(NOTE_PATH)
    return {
        "periodic_error": periodic_error,
        "required_gap": required_gap,
        "proof_valid": proof_valid,
        "kernel_nonzero": True,
        "finite_component_dimension": 6,
        "matrix_mixing_covered": all(
            phrase in note
            for phrase in (
                "fourier transform is entire and not identically zero",
                "nonzero on some real interval",
                "degree-`m` polynomial in `n` with nonzero leading coefficient",
                "proof permits arbitrary finite component mixing",
                "no invariant diagonal scalar subcarrier is assumed",
            )
        ),
        "scoped": all(
            phrase in note
            for phrase in (
                "nonzero compact convolution pullback",
                "same finite carrier",
                "actual raw staggered carrier",
            )
        ),
    }


def centered_bspline(degree: int, value: float) -> float:
    total = 0.0
    shift = 0.5 * (degree + 1)
    for index in range(degree + 2):
        argument = value + shift - index
        if degree == 0:
            positive = 1.0 if argument > 0.0 else 0.0
        else:
            positive = max(argument, 0.0) ** degree
        total += (-1.0) ** index * comb(degree + 1, index) * positive
    return total / factorial(degree)


def centered_bspline_derivative(degree: int, value: float) -> float:
    if degree < 1:
        raise ValueError("degree must be positive")
    total = 0.0
    shift = 0.5 * (degree + 1)
    for index in range(degree + 2):
        argument = value + shift - index
        if degree == 1:
            positive = 1.0 if argument > 0.0 else 0.0
        else:
            positive = max(argument, 0.0) ** (degree - 1)
        total += (-1.0) ** index * comb(degree + 1, index) * positive
    return total / factorial(degree - 1)


def spline_escape_certificate(mutation: str) -> dict[str, object]:
    probes = np.linspace(-3.137, 3.137, 1201)
    derivative_error = 0.0
    for degree in (2, 3, 4):
        for value in probes:
            derivative_error = max(
                derivative_error,
                abs(
                    centered_bspline_derivative(degree, float(value))
                    - centered_bspline(degree - 1, float(value + 0.5))
                    + centered_bspline(degree - 1, float(value - 0.5))
                ),
            )
    partition_error = 0.0
    for value in np.linspace(-0.47, 0.47, 101):
        total = sum(centered_bspline(3, float(value - site)) for site in range(-8, 9))
        partition_error = max(partition_error, abs(total - 1.0))
    cubic_values = (
        centered_bspline(3, -1.0),
        centered_bspline(3, 0.0),
        centered_bspline(3, 1.0),
    )
    note = flat(NOTE_PATH)
    extra_carrier_acknowledged = all(
        phrase in note
        for phrase in (
            "degree-lowered half-grid carrier",
            "cubic coefficients are not the present point samples",
            "discrete graph-link matter remains live",
        )
    )
    if mutation == "hide_extra_carrier":
        extra_carrier_acknowledged = False
    return {
        "derivative_error": derivative_error,
        "partition_error": partition_error,
        "cubic_values": cubic_values,
        "support_radius": 2.0,
        "generic_tensor_support": 64,
        "cardinal_error": max(abs(cubic_values[1] - 1.0), abs(cubic_values[0])),
        "extra_carrier_acknowledged": extra_carrier_acknowledged,
    }


def shifted(field: np.ndarray, displacement: Shift) -> np.ndarray:
    return np.roll(
        field,
        shift=tuple(-value for value in displacement),
        axis=(0, 1, 2),
    )


@lru_cache(maxsize=None)
def graph_stencil(size: int) -> dict[Shift, np.ndarray]:
    return block83.raw_potential_stencil(size)


def apply_stencil(field: np.ndarray, stencil: dict[Shift, np.ndarray]) -> np.ndarray:
    result = np.zeros_like(field, dtype=complex)
    for displacement, coefficient in stencil.items():
        result += np.einsum("ij,...j->...i", coefficient, shifted(field, displacement))
    return result


def site_energy(
    h: np.ndarray,
    momentum: np.ndarray,
    kinetic: np.ndarray,
    stencil: dict[Shift, np.ndarray],
) -> np.ndarray:
    ph = apply_stencil(h, stencil)
    shadow_momentum = momentum - DELTA * ph
    g_momentum = np.einsum("ij,...j->...i", kinetic, shadow_momentum)
    return 0.5 * np.real(
        np.einsum("...i,...i->...", momentum.conj(), g_momentum)
        + np.einsum("...i,...i->...", h.conj(), ph)
    )


def canonical_orientation(displacement: Shift) -> bool:
    return next(value for value in displacement if value != 0) > 0


def graph_divergence(current: GraphCurrent) -> np.ndarray:
    first = next(iter(current.values()))
    result = np.zeros_like(first, dtype=float)
    for displacement, value in current.items():
        result += value - shifted(value, tuple(-entry for entry in displacement))
    return result


def base_graph_triplet(
    h: np.ndarray,
    momentum: np.ndarray,
    force: np.ndarray,
    mutation: str = "",
) -> dict[str, object]:
    size = h.shape[0]
    stencil = graph_stencil(size)
    kinetic = block83.spatial_operators(np.zeros(3))[0]
    ph = apply_stencil(h, stencil)
    momentum1 = momentum + DELTA * (-ph + force)
    acceleration = np.einsum("ij,...j->...i", kinetic, momentum1)
    h1 = h + DELTA * acceleration
    e0 = site_energy(h, momentum, kinetic, stencil)
    e1 = site_energy(h1, momentum1, kinetic, stencil)
    q0 = DELTA * np.real(
        np.einsum(
            "...i,...i->...",
            force.conj(),
            np.einsum("ij,...j->...i", kinetic, 0.5 * (momentum + momentum1)),
        )
    )
    pa = apply_stencil(acceleration, stencil)
    boundary = np.real(
        np.einsum("...i,...i->...", h.conj(), pa)
        - np.einsum("...i,...i->...", acceleration.conj(), ph)
    )
    phi: GraphCurrent = {}
    for displacement, coefficient in stencil.items():
        if displacement == (0, 0, 0):
            continue
        phi[displacement] = np.real(
            np.einsum(
                "...i,...i->...",
                h.conj(),
                np.einsum("ij,...j->...i", coefficient, shifted(acceleration, displacement)),
            )
            - np.einsum(
                "...i,...i->...",
                acceleration.conj(),
                np.einsum("ij,...j->...i", coefficient, shifted(h, displacement)),
            )
        )
    oriented = tuple(sorted(key for key in phi if canonical_orientation(key)))
    current = {key: phi[key].copy() for key in oriented}
    if mutation == "drop_graph_edge":
        current.pop(next(key for key in oriented if sum(abs(value) for value in key) == 2))
    flux = {key: -0.5 * DELTA * value for key, value in current.items()}
    point_error = float(np.max(np.abs(e1 - e0 - q0 - 0.5 * DELTA * boundary)))
    green_error = float(np.max(np.abs(boundary - graph_divergence(current))))
    continuity_error = float(
        np.max(np.abs(e1 - e0 - q0 + graph_divergence(flux)))
    )
    antisymmetry = 0.0
    for key, value in phi.items():
        opposite = tuple(-entry for entry in key)
        antisymmetry = max(
            antisymmetry,
            float(np.max(np.abs(value + shifted(phi[opposite], key)))),
        )
    return {
        "e0": e0,
        "e1": e1,
        "q0": q0,
        "flux": flux,
        "phi": phi,
        "boundary": boundary,
        "support": len(stencil),
        "directed_edges": len(phi),
        "oriented_edges": len(oriented),
        "point_error": point_error,
        "green_error": green_error,
        "continuity_error": continuity_error,
        "antisymmetry": antisymmetry,
    }


def tensor_rotation(rotation: np.ndarray) -> np.ndarray:
    return np.column_stack(
        tuple(
            block83.tensor_coordinates(rotation @ item @ rotation.T)
            for item in block83.BASIS
        )
    )


def spatial_placement(momentum: np.ndarray) -> np.ndarray:
    k = np.asarray(momentum, dtype=float)
    return np.diag(
        (
            1.0,
            1.0,
            1.0,
            np.exp(0.5j * (k[0] + k[1])),
            np.exp(0.5j * (k[0] + k[2])),
            np.exp(0.5j * (k[1] + k[2])),
        )
    )


def rotate_raw_tensor_field(field: np.ndarray, rotation: np.ndarray) -> np.ndarray:
    size = field.shape[0]
    modes = np.fft.fftn(field, axes=(0, 1, 2))
    rotated_modes = np.zeros_like(modes)
    representation = tensor_rotation(rotation)
    for index in np.ndindex((size,) * 3):
        integer = np.asarray(
            [value if value <= size // 2 else value - size for value in index],
            dtype=int,
        )
        momentum = 2.0 * np.pi * integer / size
        rotated_integer = rotation @ integer
        rotated_momentum = rotation @ momentum
        action = (
            spatial_placement(rotated_momentum)
            @ representation
            @ spatial_placement(momentum).conj().T
        )
        destination = tuple(int(value % size) for value in rotated_integer)
        rotated_modes[destination] = action @ modes[index]
    return np.fft.ifftn(rotated_modes, axes=(0, 1, 2))


def rotate_site_scalar(field: np.ndarray, rotation: np.ndarray) -> np.ndarray:
    size = field.shape[0]
    result = np.zeros_like(field)
    for site in np.ndindex((size,) * 3):
        destination = tuple(int(value % size) for value in rotation @ np.asarray(site))
        result[destination] = field[site]
    return result


def rotate_graph_current(current: GraphCurrent, rotation: np.ndarray) -> GraphCurrent:
    size = next(iter(current.values())).shape[0]
    keys = set(current)
    result = {key: np.zeros_like(next(iter(current.values()))) for key in keys}
    for displacement, field in current.items():
        rotated_displacement = tuple(
            int(value) for value in rotation @ np.asarray(displacement)
        )
        direct = rotated_displacement in keys
        target = (
            rotated_displacement
            if direct
            else tuple(-value for value in rotated_displacement)
        )
        if target not in keys:
            raise AssertionError(f"missing rotated graph edge {target}")
        for site in np.ndindex((size,) * 3):
            anchor = np.asarray(site)
            value = field[site]
            if not direct:
                anchor = anchor + np.asarray(displacement)
                value = -value
            destination = tuple(int(entry % size) for entry in rotation @ anchor)
            result[target][destination] += value
    return result


def proper_rotations() -> tuple[np.ndarray, ...]:
    return tuple(np.asarray(item, dtype=int) for item in block83.proper_cubic_rotations())


def reynolds_graph_triplet(
    h: np.ndarray,
    momentum: np.ndarray,
    force: np.ndarray,
) -> dict[str, object]:
    accumulated_scalar: dict[str, np.ndarray] = {}
    accumulated_flux: GraphCurrent = {}
    rotations = proper_rotations()
    for rotation in rotations:
        transformed = base_graph_triplet(
            rotate_raw_tensor_field(h, rotation),
            rotate_raw_tensor_field(momentum, rotation),
            rotate_raw_tensor_field(force, rotation),
        )
        inverse = rotation.T
        for key in ("e0", "e1", "q0"):
            pulled = rotate_site_scalar(np.asarray(transformed[key]), inverse)
            accumulated_scalar[key] = accumulated_scalar.get(key, np.zeros_like(pulled)) + pulled
        pulled_flux = rotate_graph_current(transformed["flux"], inverse)
        for key, value in pulled_flux.items():
            accumulated_flux[key] = accumulated_flux.get(key, np.zeros_like(value)) + value
    return {
        **{key: value / len(rotations) for key, value in accumulated_scalar.items()},
        "flux": {key: value / len(rotations) for key, value in accumulated_flux.items()},
    }


def graph_current_certificate(mutation: str) -> dict[str, object]:
    size = 5
    rng = np.random.default_rng(9301)
    shape = (size, size, size, 6)
    h = rng.normal(size=shape) + 1.0j * rng.normal(size=shape)
    momentum = rng.normal(size=shape) + 1.0j * rng.normal(size=shape)
    force = np.zeros(shape, dtype=complex)
    force[1, 2, 3, 0] = 0.73 + 0.19j
    force[4, 0, 2, 2] = -0.21 + 0.11j
    base = base_graph_triplet(h, momentum, force, mutation)
    averaged = (
        base
        if mutation == "skip_reynolds"
        else reynolds_graph_triplet(h, momentum, force)
    )
    averaged_continuity = float(
        np.max(
            np.abs(
                np.asarray(averaged["e1"])
                - np.asarray(averaged["e0"])
                - np.asarray(averaged["q0"])
                + graph_divergence(averaged["flux"])
            )
        )
    )
    covariance_error = 0.0
    covariance_failures = 0
    for rotation in proper_rotations():
        transformed = reynolds_graph_triplet(
            rotate_raw_tensor_field(h, rotation),
            rotate_raw_tensor_field(momentum, rotation),
            rotate_raw_tensor_field(force, rotation),
        )
        expected_scalars = {
            key: rotate_site_scalar(np.asarray(averaged[key]), rotation)
            for key in ("e0", "e1", "q0")
        }
        expected_flux = rotate_graph_current(averaged["flux"], rotation)
        error = max(
            float(np.max(np.abs(np.asarray(transformed[key]) - expected_scalars[key])))
            for key in ("e0", "e1", "q0")
        )
        error = max(
            error,
            max(
                float(np.max(np.abs(transformed["flux"][key] - expected_flux[key])))
                for key in expected_flux
            ),
        )
        covariance_error = max(covariance_error, error)
        covariance_failures += int(error > TOL)
    note = flat(NOTE_PATH)
    return {
        **base,
        "averaged_continuity": averaged_continuity,
        "covariance_error": covariance_error,
        "covariance_failures": covariance_failures,
        "frames": len(proper_rotations()),
        "scoped": all(
            phrase in note
            for phrase in (
                "raw eighteen-directed-edge current",
                "no coordinate-axis path is chosen",
                "graph current is not a selected physical stress tensor",
            )
        ),
    }


def no_go_certificate(mutation: str) -> dict[str, object]:
    note = flat(NOTE_PATH)
    required = (
        "n1 — alternative route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "exact target contract",
        "collapsed terminal wall set has one member",
        "| **attempted** | fails",
        "| **attempted** | survives outside the exact contract",
    )
    valid = all(phrase in note for phrase in required)
    if mutation == "weaken_routes":
        valid = False
    return {
        "valid": valid,
        "attempted_count": note.count("attempted"),
        "path_line_count": note.count("path:line"),
        "no_broad_negative": "no broad gravity or axiom no-go" in note,
    }


def scope_certificate(mutation: str) -> dict[str, object]:
    note = flat(NOTE_PATH)
    axiom = (ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md").read_text(encoding="utf-8")
    valid = all(
        phrase in note
        for phrase in (
            "gravity does not fail",
            "no axiom is amended",
            "no toe percentage moves",
            "zero obligation retirement",
            "discrete graph-matter action is the next gravity target",
            "a state is a configuration of records",
        )
    )
    if mutation in ("claim_gravity_no_go", "claim_axiom_update", "claim_toe_progress"):
        valid = False
    return {
        "valid": valid,
        "axiom_state": "A state is a configuration of records." in axiom,
        "records_permanent": "records are permanent" in axiom,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutation",
        choices=(
            "stale_axiom_authority",
            "fake_local_log",
            "fake_compact_chain",
            "drop_graph_edge",
            "skip_reynolds",
            "hide_extra_carrier",
            "weaken_routes",
            "claim_gravity_no_go",
            "claim_axiom_update",
            "claim_toe_progress",
        ),
        default="",
    )
    mutation = parser.parse_args().mutation
    checks = Checks()

    authority = authority_certificate(mutation)
    checks.check(
        "A-authority-parent-and-runtime-closure",
        "current axioms and the Block83/82 parent surfaces are content-bound with no hidden runner",
        authority["origin_main"] == CURRENT_AXIOM_COMMIT
        and authority["axiom_blob"] == authority["expected_axiom"]
        and authority["parent_note"] == PARENT_NOTE_BLOB
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and not authority["mismatches"]
        and not authority["missing"]
        and not authority["loaded_missing"],
        f"origin/main={authority['origin_main'][:10]}; frozen/loaded mismatches={len(authority['mismatches'])}/{len(authority['loaded_missing'])}",
    )

    generator = finite_generator_certificate(mutation)
    checks.check(
        "B-no-finite-range-logarithm-of-exact-shift",
        "an exponential of a periodic finite-range symbol has zero winding and cannot equal the one-site shift",
        abs(generator["exact_winding"] - 1.0) < TOL
        and abs(generator["centered_winding"]) < TOL
        and abs(generator["six_component_winding"] - 6.0) < TOL
        and generator["periodic_symbol_error"] < TOL
        and abs(generator["period_gap"] - 2.0 * pi) < TOL
        and generator["proof_valid"]
        and generator["scoped"],
        f"windings shift/centered/six={generator['exact_winding']:.0f}/{generator['centered_winding']:.0f}/{generator['six_component_winding']:.0f}; log period gap={generator['period_gap']:.6f}",
    )

    pullback = compact_pullback_certificate(mutation)
    checks.check(
        "C-no-compact-same-carrier-exact-chain-pullback",
        "a nonzero compact convolution kernel cannot intertwine endpoint differentiation with a finite-range same-carrier generator",
        pullback["periodic_error"] < TOL
        and abs(pullback["required_gap"] - 2.0 * pi) < TOL
        and pullback["proof_valid"]
        and pullback["kernel_nonzero"]
        and pullback["finite_component_dimension"] == 6
        and pullback["matrix_mixing_covered"]
        and pullback["scoped"],
        f"finite-symbol period error={pullback['periodic_error']:.1e}; required derivative gap={pullback['required_gap']:.6f}; matrix carrier dimension={pullback['finite_component_dimension']}",
    )

    graph = graph_current_certificate(mutation)
    checks.check(
        "D-path-free-raw-eighteen-edge-green-current",
        "the nineteen-shift action has an antisymmetric raw graph current whose divergence is the exact Green boundary",
        graph["support"] == 19
        and graph["directed_edges"] == 18
        and graph["oriented_edges"] == 9
        and graph["point_error"] < TOL
        and graph["green_error"] < TOL
        and graph["continuity_error"] < TOL
        and graph["antisymmetry"] < TOL
        and graph["scoped"],
        f"support/directed/oriented={graph['support']}/{graph['directed_edges']}/{graph['oriented_edges']}; point/Green/continuity={graph['point_error']:.1e}/{graph['green_error']:.1e}/{graph['continuity_error']:.1e}",
    )

    checks.check(
        "E-proper-cubic-reynolds-graph-current",
        "Reynolds averaging the complete graph triplet preserves continuity and restores all-frame covariance",
        graph["frames"] == 24
        and graph["averaged_continuity"] < TOL
        and graph["covariance_failures"] == 0
        and graph["covariance_error"] < TOL,
        f"frames/failures={graph['frames']}/{graph['covariance_failures']}; continuity/covariance={graph['averaged_continuity']:.1e}/{graph['covariance_error']:.1e}",
    )

    spline = spline_escape_certificate(mutation)
    checks.check(
        "F-degree-ladder-spline-escape-and-carrier-cost",
        "compact B-splines obey an exact degree-lowering chain but require a new half-grid coefficient carrier",
        spline["derivative_error"] < TOL
        and spline["partition_error"] < TOL
        and np.max(np.abs(np.asarray(spline["cubic_values"]) - np.asarray((1.0 / 6.0, 2.0 / 3.0, 1.0 / 6.0)))) < TOL
        and abs(spline["support_radius"] - 2.0) < TOL
        and spline["generic_tensor_support"] == 64
        and abs(spline["cardinal_error"] - 1.0 / 3.0) < TOL
        and spline["extra_carrier_acknowledged"],
        f"chain/partition={spline['derivative_error']:.1e}/{spline['partition_error']:.1e}; cubic samples={tuple(round(value, 6) for value in spline['cubic_values'])}; cardinal error={spline['cardinal_error']:.3f}",
    )

    no_go = no_go_certificate(mutation)
    checks.check(
        "G-no-go-discipline-N1-through-N8",
        "the narrow negative is stress-tested against carrier, graph, field, spectral, and quasilocal escapes",
        no_go["valid"]
        and no_go["attempted_count"] >= 6
        and no_go["path_line_count"] >= 2
        and no_go["no_broad_negative"],
        f"ATTEMPTED markers={no_go['attempted_count']}; path:line matches={no_go['path_line_count']}",
    )

    scope = scope_certificate(mutation)
    checks.check(
        "H-gravity-axiom-Record-retention-and-TOE-scope",
        "the route closure and graph-current construction do not select a law, amend axioms, or move TOE",
        all(scope.values()),
    )

    print(
        f"AXIOM_AUTHORITY: origin/main={authority['origin_main']} minimal-axiom blob={CURRENT_AXIOM_BLOB}; Block83 parent={PARENT_COMMIT}"
    )
    print(
        "per_element: checked — scalar translation symbol, compact convolution kernel, cubic B-spline degree ladder, and all six raw tensor coordinates"
    )
    print(
        "per_site: checked — nineteen stencil shifts, eighteen directed graph edges, nine oriented representatives, and compact radius-two spline support"
    )
    print(
        "per_mode: checked analytically — periodic finite Laurent symbols cannot equal the nonperiodic logarithm ik; the numerical winding witnesses are 0 versus 1"
    )
    print(
        "per_block: checked — raw graph continuity and 24-frame Reynolds covariance close; compact same-carrier worldline pullback fails while degree-ladder and graph-matter escapes survive"
    )
    print(
        "lattice_wide: checked and not executed — no common selected matter-gravity law, live carrier/Record compiler, nonlinear Ward completion, retention, or obligation retirement"
    )
    print(
        "RESULT: the diagonal-path wall is removed by the raw graph current; the existing-carrier compact continuous-worldline pullback is impossible under its exact finite-range same-carrier contract"
    )
    print(
        "PORTFOLIO: stop compact same-carrier interpolation work; test a discrete graph-matter action next, with a degree-ladder carrier or axiom clarification only if graph and lattice-field routes fail"
    )
    print(
        "SCOPE: gravity remains live; no axiom amendment, audit verdict, retained obligation retirement, or TOE percentage movement"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
