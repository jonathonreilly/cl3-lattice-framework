#!/usr/bin/env python3
"""Cycle 228: local generator/source tournament for the cubic common family.

Compare the supplied rest scalar Q, the exact local Hermitian parts

    K = 2 I - U - U^dagger,
    S = (U - U^dagger)/(2 i),

the Cycle-213 projected wave energy, and positive spectral phase lifts.  The
runner proves a positive local one-step-deviation theorem for K relative to a
chosen phase reference, checks that (K,S) reconstruct the referenced one-step
walk, and exposes the bounded locality/positivity/linearity/composition
tradeoff on the Cycle-215/219 fixtures.

This is a candidate-law discriminator.  It does not select physical energy,
derive stress-energy or gravity, establish a general no-go, or support an
axiom conclusion.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path

import numpy as np
from scipy.linalg import expm, schur

import archive_carrier_source_ledger_cycle227_2026_07_17 as c227
import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import finite_coin_scalar_wave_dilation_cycle215_2026_07_16 as c215
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import virtual_exchange_green_kernel_cycle216_2026_07_16 as c216


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "LOCAL_GENERATOR_SOURCE_TOURNAMENT_CYCLE228_NOTE_2026-07-17.md"
)

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "local one-step deviation",
        "complete local spectral pair",
        "k_alpha = 2i - u_alpha - u_alpha^dagger",
        "s_alpha = (u_alpha - u_alpha^dagger)/(2i)",
        "positive phase magnitude",
        "chosen phase reference",
        "algebraic tails",
        "local action",
        "clock-response",
        "ward",
        "physical energy remains unselected",
        "n1 — alternative routes",
        "n2 — wall-independence",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — resolution",
        "n6 — primitive and reframe",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no axiom conclusion",
        "global novelty has not been established",
        "draft parking branch",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note preserves the bounded result and N1-N8 gate", not missing, missing)


def walk_symbol(beta: float, momentum: np.ndarray) -> np.ndarray:
    species = c219.common_species(beta)
    return c210.molecular_bloch(np.asarray(momentum, dtype=float), species.coin)


def spectral_coordinates(unitary: np.ndarray) -> dict[str, np.ndarray]:
    identity = np.eye(unitary.shape[0], dtype=complex)
    stiffness = 2 * identity - unitary - unitary.conj().T
    signed_sine = (unitary - unitary.conj().T) / (2j)
    values, vectors = np.linalg.eigh(stiffness)
    values[np.abs(values) < 1e-11] = 0.0
    values[np.abs(values - 4) < 1e-11] = 4.0
    values = np.clip(values, 0.0, 4.0)
    square_root = (vectors * np.sqrt(values)) @ vectors.conj().T
    phase_magnitude = (
        vectors
        * (2 * np.arcsin(np.clip(np.sqrt(values) / 2, 0.0, 1.0)))
    ) @ vectors.conj().T
    return {
        "K": stiffness,
        "S": signed_sine,
        "sqrtK": square_root,
        "Habs": phase_magnitude,
    }


def chosen_phase_lifts(
    unitary: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return +pi/-pi spectral phase lifts and the exact -1 projector.

    A matrix with eigenvalue -1 has no analytic principal matrix logarithm.
    These are explicit Borel/spectral Arg choices, not an unqualified log.
    """
    triangular, vectors = schur(unitary, output="complex")
    eigenvalues = np.diag(triangular)
    phases = np.angle(eigenvalues)
    phases[np.abs(eigenvalues - 1) < 1e-10] = 0.0
    phases[np.abs(eigenvalues + 1) < 1e-10] = np.pi
    plus_lift = (vectors * phases) @ vectors.conj().T
    plus_lift = (plus_lift + plus_lift.conj().T) / 2

    stiffness = (
        2 * np.eye(unitary.shape[0], dtype=complex)
        - unitary
        - unitary.conj().T
    )
    values, stiffness_vectors = np.linalg.eigh(stiffness)
    minus_vectors = stiffness_vectors[:, values > 4 - 1e-10]
    minus_projector = minus_vectors @ minus_vectors.conj().T
    minus_lift = plus_lift - 2 * np.pi * minus_projector
    return plus_lift, minus_lift, minus_projector


def walk_step(state: np.ndarray, coin: np.ndarray) -> np.ndarray:
    coined = np.einsum("ab,xyzb->xyza", coin, state, optimize=True)
    output = np.zeros_like(coined)
    for direction, vector in enumerate(c210.DIRECTIONS):
        output[..., direction] = np.roll(
            coined[..., direction],
            tuple(int(value) for value in vector),
            axis=(0, 1, 2),
        )
    return output


def inverse_walk_step(state: np.ndarray, coin: np.ndarray) -> np.ndarray:
    unstreamed = np.zeros_like(state)
    for direction, vector in enumerate(c210.DIRECTIONS):
        unstreamed[..., direction] = np.roll(
            state[..., direction],
            tuple(-int(value) for value in vector),
            axis=(0, 1, 2),
        )
    return np.einsum(
        "ab,xyzb->xyza", coin.conj().T, unstreamed, optimize=True
    )


def apply_local_coordinates(
    state: np.ndarray, coin: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    following = walk_step(state, coin)
    previous = inverse_walk_step(state, coin)
    stiffness = 2 * state - following - previous
    signed_sine = (following - previous) / (2j)
    return stiffness, signed_sine


def projected_wave_energy_symbol(beta: float, momentum: np.ndarray) -> np.ndarray:
    """Hermitian complex extension of the Cycle-213 two-slice scalar energy."""
    momentum = np.asarray(momentum, dtype=float)
    unitary = walk_symbol(beta, momentum)
    identity = np.eye(6, dtype=complex)
    laplacian = 6 - 2 * np.sum(np.cos(momentum))
    return (
        1.5
        * (unitary - identity).conj().T
        @ c210.P_SCALAR
        @ (unitary - identity)
        + 0.25
        * laplacian
        * (unitary.conj().T @ c210.P_SCALAR + c210.P_SCALAR @ unitary)
    )


def complete_local_pair_controls() -> None:
    rng = np.random.default_rng(228)
    factor_residuals = []
    reconstruction_residuals = []
    conservation_residuals = []
    minimum_k = []
    signed_extrema = []
    for beta in (0.0, -0.2, -0.3, -0.4):
        for _ in range(16):
            momentum = rng.uniform(-2.7, 2.7, size=3)
            unitary = walk_symbol(beta, momentum)
            coordinates = spectral_coordinates(unitary)
            identity = np.eye(6, dtype=complex)
            factor_residuals.append(
                np.linalg.norm(
                    coordinates["K"]
                    - (identity - unitary).conj().T @ (identity - unitary)
                )
            )
            reconstruction_residuals.append(
                np.linalg.norm(
                    unitary
                    - (identity - coordinates["K"] / 2 + 1j * coordinates["S"])
                )
            )
            for name in ("K", "S", "sqrtK", "Habs"):
                conservation_residuals.append(
                    np.linalg.norm(
                        unitary.conj().T @ coordinates[name] @ unitary
                        - coordinates[name]
                    )
                )
            minimum_k.append(float(np.min(np.linalg.eigvalsh(coordinates["K"]))))
            signed = np.linalg.eigvalsh(coordinates["S"])
            signed_extrema.append((float(np.min(signed)), float(np.max(signed))))

    check(
        "at fixed phase reference K is positive one-step deviation (I-U)^dagger(I-U)",
        max(factor_residuals) < 8e-14 and min(minimum_k) > -3e-14,
        {
            "factor_residual": max(factor_residuals),
            "minimum_eigenvalue": min(minimum_k),
        },
    )
    check(
        "the strict-local Hermitian pair (K,S) reconstructs every tested U",
        max(reconstruction_residuals) < 3e-15,
        max(reconstruction_residuals),
    )
    check(
        "all listed spectral coordinates are exactly conserved by one-step U",
        max(conservation_residuals) < 2e-13,
        max(conservation_residuals),
    )
    check(
        "S retains time orientation but is genuinely signed",
        min(row[0] for row in signed_extrema) < -0.2
        and max(row[1] for row in signed_extrema) > 0.2,
        {
            "minimum": min(row[0] for row in signed_extrema),
            "maximum": max(row[1] for row in signed_extrema),
        },
    )


def phase_reference_controls() -> None:
    """Expose the projective-phase ambiguity of one-step coordinates."""
    alpha = 0.4
    identity = np.eye(6, dtype=complex)
    state = c210.UNIFORM
    density = np.outer(state, state.conj())
    unitary = walk_symbol(0.0, np.zeros(3))
    shifted = np.exp(1j * alpha) * unitary
    base_coordinates = spectral_coordinates(unitary)
    shifted_coordinates = spectral_coordinates(shifted)

    base_output = unitary @ density @ unitary.conj().T
    shifted_output = shifted @ density @ shifted.conj().T
    base_observed = {
        name: float(np.vdot(state, operator @ state).real)
        for name, operator in base_coordinates.items()
        if name in ("K", "S", "Habs")
    }
    observed = {
        name: float(np.vdot(state, operator @ state).real)
        for name, operator in shifted_coordinates.items()
        if name in ("K", "S", "Habs")
    }
    check(
        "projectively identical state updates change unreferenced K S and Habs",
        np.linalg.norm(base_output - shifted_output) < 2e-15
        and max(abs(value) for value in base_observed.values()) < 2e-14
        and abs(observed["K"] - (2 - 2 * np.cos(alpha))) < 2e-14
        and abs(observed["S"] - np.sin(alpha)) < 2e-14
        and abs(observed["Habs"] - alpha) < 2e-14,
        {
            "density_update_residual": float(
                np.linalg.norm(base_output - shifted_output)
            ),
            "base": base_observed,
            "phase_shifted": observed,
        },
    )

    pure_phase = spectral_coordinates(np.exp(1j * alpha) * identity)
    check(
        "a pure global phase appears active until a phase-zero reference is supplied",
        np.linalg.norm(pure_phase["K"] - (2 - 2 * np.cos(alpha)) * identity)
        < 2e-14
        and np.linalg.norm(pure_phase["S"] - np.sin(alpha) * identity) < 2e-14
        and np.linalg.norm(pure_phase["Habs"] - alpha * identity) < 2e-14,
        {
            "K_trace_per_mode": float(np.trace(pure_phase["K"]).real / 6),
            "S_trace_per_mode": float(np.trace(pure_phase["S"]).real / 6),
            "Habs_trace_per_mode": float(
                np.trace(pure_phase["Habs"]).real / 6
            ),
        },
    )

    side = 7
    momenta = 2 * np.pi * np.fft.fftfreq(side)
    grid = np.indices((side, side, side))
    signed_grid = np.minimum(grid, side - grid)
    manhattan = np.sum(signed_grid, axis=0)
    rows = []
    for reference in (-0.7, 0.0, 0.4):
        factor_residuals = []
        reconstruction_residuals = []
        conservation_residuals = []
        minima = []
        symbol = np.zeros((side, side, side, 6, 6), dtype=complex)
        for indices in product(range(side), repeat=3):
            momentum = np.asarray([momenta[index] for index in indices])
            physical = walk_symbol(-0.3, momentum)
            relative = np.exp(-1j * reference) * physical
            local = spectral_coordinates(relative)
            factor_residuals.append(
                np.linalg.norm(
                    local["K"]
                    - (identity - relative).conj().T @ (identity - relative)
                )
            )
            reconstruction_residuals.append(
                np.linalg.norm(
                    physical
                    - np.exp(1j * reference)
                    * (identity - local["K"] / 2 + 1j * local["S"])
                )
            )
            conservation_residuals.append(
                np.linalg.norm(
                    physical.conj().T @ local["K"] @ physical - local["K"]
                )
            )
            minima.append(float(np.min(np.linalg.eigvalsh(local["K"]))))
            symbol[indices] = local["K"]
        kernel = np.fft.ifftn(symbol, axes=(0, 1, 2))
        rows.append(
            {
                "reference": reference,
                "factor": max(factor_residuals),
                "reconstruction": max(reconstruction_residuals),
                "conservation": max(conservation_residuals),
                "minimum": min(minima),
                "beyond_one": float(np.linalg.norm(kernel[manhattan > 1])),
            }
        )
    check(
        "every chosen phase reference gives an equally local positive conserved K family",
        max(row["factor"] for row in rows) < 8e-14
        and max(row["reconstruction"] for row in rows) < 5e-15
        and max(row["conservation"] for row in rows) < 2e-13
        and min(row["minimum"] for row in rows) > -3e-14
        and max(row["beyond_one"] for row in rows) < 3e-14,
        rows,
    )


def deviation_transport_controls() -> None:
    rng = np.random.default_rng(2281)
    rows = []
    for beta in (0.0, -0.3):
        coin = c219.common_species(beta).coin
        state = rng.normal(size=(9, 9, 9, 6)) + 1j * rng.normal(
            size=(9, 9, 9, 6)
        )
        state /= np.linalg.norm(state)
        following = walk_step(state, coin)
        deviation_vector = state - following
        stiffness, _ = apply_local_coordinates(state, coin)
        deviation = float(np.vdot(deviation_vector, deviation_vector).real)
        quadratic = float(np.vdot(state, stiffness).real)

        following_twice = walk_step(following, coin)
        next_deviation_vector = following - following_twice
        transported_deviation_vector = walk_step(deviation_vector, coin)
        density = np.sum(np.abs(deviation_vector) ** 2, axis=-1)
        rows.append(
            {
                "beta": beta,
                "deviation": deviation,
                "quadratic": quadratic,
                "transport_residual": float(
                    np.linalg.norm(
                        next_deviation_vector - transported_deviation_vector
                    )
                ),
                "density_minimum": float(np.min(density)),
                "next_total": float(np.linalg.norm(next_deviation_vector) ** 2),
            }
        )
    check(
        "the positive reference-relative site-deviation density sums exactly to <K>",
        max(abs(row["deviation"] - row["quadratic"]) for row in rows) < 2e-14
        and min(row["density_minimum"] for row in rows) >= 0,
        rows,
    )
    check(
        "the derived deviation vector chi=(I-U)psi is transported by the same local U",
        max(row["transport_residual"] for row in rows) < 3e-15
        and max(abs(row["next_total"] - row["deviation"]) for row in rows) < 2e-14,
        rows,
    )

    delta = np.zeros((13, 13, 13, 6), dtype=complex)
    delta[6, 6, 6] = c210.UNIFORM
    coin = c219.common_species(0.0).coin
    point_deviation = delta - walk_step(delta, coin)
    occupied = np.argwhere(np.sum(np.abs(point_deviation) ** 2, axis=-1) > 1e-14)
    check(
        "one-site input gives a deviation vector inside the one-edge cone",
        all(np.sum(np.abs(site - 6)) <= 1 for site in occupied),
        occupied.tolist(),
    )

    spectator_zero = np.array((1, 0), dtype=complex)
    spectator_plus = np.array((1, 1), dtype=complex) / np.sqrt(2)
    one = point_deviation[..., None] * spectator_zero
    two = (
        point_deviation[..., None, None]
        * spectator_zero[:, None]
        * spectator_plus
    )
    check(
        "normalized inert logical spectator factors do not multiply base-sector deviation",
        abs(np.linalg.norm(one) ** 2 - np.linalg.norm(point_deviation) ** 2)
        < 2e-14
        and abs(np.linalg.norm(two) ** 2 - np.linalg.norm(point_deviation) ** 2)
        < 2e-14,
    )


def full_kernel_locality_controls() -> None:
    side = 13
    momenta = 2 * np.pi * np.fft.fftfreq(side)
    symbols = {
        name: np.zeros((side, side, side, 6, 6), dtype=complex)
        for name in ("K", "S", "sqrtK", "Habs")
    }
    for indices in product(range(side), repeat=3):
        momentum = np.asarray([momenta[index] for index in indices])
        coordinates = spectral_coordinates(walk_symbol(0.0, momentum))
        for name in symbols:
            symbols[name][indices] = coordinates[name]

    coordinates = np.indices((side, side, side))
    signed = np.minimum(coordinates, side - coordinates)
    manhattan = np.sum(signed, axis=0)
    rows = {}
    for name, symbol in symbols.items():
        kernel = np.fft.ifftn(symbol, axes=(0, 1, 2))
        rows[name] = {
            "range_0": float(np.linalg.norm(kernel[manhattan == 0])),
            "range_1": float(np.linalg.norm(kernel[manhattan == 1])),
            "beyond_1": float(np.linalg.norm(kernel[manhattan > 1])),
            "range_3": float(np.linalg.norm(kernel[manhattan == 3])),
        }
    check(
        "K and S have exact one-edge real-space kernels",
        rows["K"]["beyond_1"] < 3e-14 and rows["S"]["beyond_1"] < 3e-14,
        rows,
    )
    check(
        "sqrt(K) and exact positive phase magnitude retain nonzero distant tails",
        rows["sqrtK"]["beyond_1"] > 0.3
        and rows["Habs"]["beyond_1"] > 0.14
        and rows["sqrtK"]["range_3"] > 0.05
        and rows["Habs"]["range_3"] > 0.1,
        rows,
    )


def scalar_tail_controls() -> None:
    side = 81
    momenta = 2 * np.pi * np.fft.fftfreq(side)
    gamma = (
        np.cos(momenta)[:, None, None]
        + np.cos(momenta)[None, :, None]
        + np.cos(momenta)[None, None, :]
    ) / 3
    laplacian = 6 * (1 - gamma)
    symbols = {
        "sqrtK": np.sqrt(np.maximum(laplacian / 3, 0.0)),
        "Habs": np.arccos(np.clip(gamma, -1.0, 1.0)),
    }
    rows = {}
    for name, symbol in symbols.items():
        kernel = np.fft.ifftn(symbol).real
        radii = np.arange(8, 26) if name == "sqrtK" else np.arange(9, 26, 2)
        coefficients = np.abs(kernel[radii, 0, 0])
        slope = float(np.polyfit(np.log(radii), np.log(coefficients), 1)[0])
        rows[name] = {
            "axis_r1": float(kernel[1, 0, 0]),
            "axis_r3": float(kernel[3, 0, 0]),
            "axis_r5": float(kernel[5, 0, 0]),
            "axis_r20": float(kernel[20, 0, 0]),
            "tail_slope": slope,
        }
    check(
        "the massless positive phase lifts have stable approximately r^-4 tails",
        all(-4.4 < row["tail_slope"] < -3.5 for row in rows.values())
        and abs(rows["sqrtK"]["axis_r20"]) > 2e-7
        and abs(rows["Habs"]["axis_r5"]) > 2e-4,
        rows,
    )


def signed_phase_lift_controls() -> None:
    momentum = np.asarray((0.41, -0.23, 0.17))
    unitary = walk_symbol(0.0, momentum)
    plus_lift, minus_lift, minus_projector = chosen_phase_lifts(unitary)
    check(
        "the +pi and -pi spectral phase choices exponentiate to the same U",
        np.linalg.norm(expm(1j * plus_lift) - unitary) < 8e-14
        and np.linalg.norm(expm(1j * minus_lift) - unitary) < 8e-14
        and abs(np.trace(minus_projector).real - 2) < 2e-12,
        {
            "plus": float(np.linalg.norm(expm(1j * plus_lift) - unitary)),
            "minus": float(np.linalg.norm(expm(1j * minus_lift) - unitary)),
            "minus_rank": float(np.trace(minus_projector).real),
        },
    )
    check(
        "the two phase lifts differ exactly by 2pi times the U=-1 projector",
        np.linalg.norm(plus_lift - minus_lift - 2 * np.pi * minus_projector)
        < 3e-14,
    )

    side = 33
    momenta = 2 * np.pi * np.fft.fftfreq(side)
    lift_symbol = np.zeros((side, side, side, 6, 6), dtype=complex)
    branch_symbol = np.zeros_like(lift_symbol)
    for indices in product(range(side), repeat=3):
        local_momentum = np.asarray([momenta[index] for index in indices])
        local_lift, _, local_projector = chosen_phase_lifts(
            walk_symbol(0.0, local_momentum)
        )
        lift_symbol[indices] = local_lift
        branch_symbol[indices] = 2 * np.pi * local_projector
    lift_kernel = np.fft.ifftn(lift_symbol, axes=(0, 1, 2))
    branch_kernel = np.fft.ifftn(branch_symbol, axes=(0, 1, 2))
    rows = {
        radius: (
            float(np.linalg.norm(lift_kernel[radius, 0, 0])),
            float(np.linalg.norm(branch_kernel[radius, 0, 0])),
        )
        for radius in (3, 5, 8, 12, 15)
    }
    check(
        "the signed phase lift and its -1 branch difference have distant tails",
        rows[3][0] > 0.05
        and rows[12][0] > 3e-4
        and rows[15][1] > 1e-4,
        rows,
    )


def massive_phase_crossing_controls() -> None:
    crossings = (
        ("plus", 1.563199679844947, 1.0),
        ("minus", 1.5783929737448452, -1.0),
    )
    rows = []
    step = 1e-4
    for label, location, target in crossings:
        unitary = walk_symbol(-0.3, np.full(3, location))
        distance = float(np.min(np.abs(np.linalg.eigvals(unitary) - target)))
        slopes = []
        for displacement in (-step, step):
            moved = walk_symbol(-0.3, np.full(3, location + displacement))
            values = np.linalg.eigvals(moved)
            selected = values[int(np.argmin(np.abs(values - target)))]
            relative_phase = float(np.angle(selected / target))
            slopes.append(relative_phase / displacement)
        rows.append(
            {
                "label": label,
                "location": location,
                "eigenvalue_distance": distance,
                "left_slope": slopes[0],
                "right_slope": slopes[1],
            }
        )
    check(
        "the beta=-0.3 complete unitary has transverse diagonal +1 and -1 crossings",
        max(row["eigenvalue_distance"] for row in rows) < 2e-12
        and min(abs(row["left_slope"]) for row in rows) > 0.14
        and min(abs(row["right_slope"]) for row in rows) > 0.14
        and max(
            abs(row["left_slope"] - row["right_slope"]) for row in rows
        )
        < 2e-6,
        rows,
    )


def projected_wave_energy_controls() -> None:
    rng = np.random.default_rng(2284)
    massless_minima = []
    massless_conservation = []
    massive_conservation = []
    for _ in range(48):
        momentum = rng.uniform(-2.6, 2.6, size=3)
        for beta, residuals in (
            (0.0, massless_conservation),
            (-0.3, massive_conservation),
        ):
            unitary = walk_symbol(beta, momentum)
            energy = projected_wave_energy_symbol(beta, momentum)
            residuals.append(
                np.linalg.norm(unitary.conj().T @ energy @ unitary - energy)
            )
            if beta == 0:
                massless_minima.append(float(np.min(np.linalg.eigvalsh(energy))))
    check(
        "the Cycle-213 energy is positive and conserved on the beta=0 parent",
        min(massless_minima) > -2e-14
        and max(massless_conservation) < 8e-14,
        {
            "minimum": min(massless_minima),
            "conservation": max(massless_conservation),
        },
    )
    check(
        "the same projected energy is not a conserved massive-family operator",
        max(massive_conservation) > 0.2,
        max(massive_conservation),
    )

    side = 9
    momenta = 2 * np.pi * np.fft.fftfreq(side)
    symbol = np.zeros((side, side, side, 6, 6), dtype=complex)
    for indices in product(range(side), repeat=3):
        momentum = np.asarray([momenta[index] for index in indices])
        symbol[indices] = projected_wave_energy_symbol(0.0, momentum)
    kernel = np.fft.ifftn(symbol, axes=(0, 1, 2))
    coordinates = np.indices((side, side, side))
    manhattan = np.sum(np.minimum(coordinates, side - coordinates), axis=0)
    check(
        "the beta=0 projected energy has exact Manhattan range two",
        np.linalg.norm(kernel[manhattan > 2]) < 3e-14
        and np.linalg.norm(kernel[manhattan == 2]) > 1.0,
        {
            "range_2": float(np.linalg.norm(kernel[manhattan == 2])),
            "beyond_2": float(np.linalg.norm(kernel[manhattan > 2])),
        },
    )


def massless_and_flat_mode_controls() -> None:
    rng = np.random.default_rng(2282)
    formula_residuals = []
    for _ in range(24):
        momentum = rng.uniform(-2.4, 2.4, size=3)
        gamma = float(np.mean(np.cos(momentum)))
        laplacian = 6 * (1 - gamma)
        coordinates = spectral_coordinates(walk_symbol(0.0, momentum))
        values = {
            name: float(np.vdot(c210.UNIFORM, operator @ c210.UNIFORM).real)
            for name, operator in coordinates.items()
        }
        projected_energy = float(
            np.vdot(
                c210.UNIFORM,
                projected_wave_energy_symbol(0.0, momentum) @ c210.UNIFORM,
            ).real
        )
        formula_residuals.extend(
            (
                abs(values["K"] - laplacian / 3),
                abs(values["S"]),
                abs(values["sqrtK"] - np.sqrt(laplacian / 3)),
                abs(values["Habs"] - np.arccos(gamma)),
                abs(projected_energy - 1.5 * (1 - gamma**2)),
            )
        )
    check(
        "the beta=0 scalar sector realizes K=L/3, E213, and Habs=arccos(gamma)",
        max(formula_residuals) < 2e-12,
        max(formula_residuals),
    )

    point = c227.point_carrier(17, (0, 0, 0))
    following = c215.field_step(point)
    previous = c216.inverse_field_step(point)
    point_k = float(np.vdot(point, 2 * point - following - previous).real)
    point_s = float(np.vdot(point, (following - previous) / (2j)).real)
    point_energy = c227.projected_wave_energy(point)
    check(
        "the point carrier separates signed sine, stiffness, and wave energy",
        abs(point_s) < 2e-14
        and abs(point_k / 2 - 1) < 2e-14
        and abs(point_energy - 1.25) < 2e-14,
        {"S": point_s, "K/2": point_k / 2, "E213": point_energy},
    )

    momentum = np.asarray((0.41, -0.23, 0.17))
    unitary = walk_symbol(0.0, momentum)
    values, vectors = np.linalg.eig(unitary)
    coordinates = spectral_coordinates(unitary)
    plus_rows = []
    minus_rows = []
    for index, value in enumerate(values):
        vector = vectors[:, index] / np.linalg.norm(vectors[:, index])
        row = {
            "phase": float(np.angle(value)),
            "scalar_overlap": float(abs(np.vdot(c210.UNIFORM, vector))),
            "K": float(np.vdot(vector, coordinates["K"] @ vector).real),
            "S": float(np.vdot(vector, coordinates["S"] @ vector).real),
            "sqrtK": float(
                np.vdot(vector, coordinates["sqrtK"] @ vector).real
            ),
            "Habs": float(np.vdot(vector, coordinates["Habs"] @ vector).real),
        }
        if abs(value - 1) < 2e-12:
            plus_rows.append(row)
        if abs(value + 1) < 2e-12:
            minus_rows.append(row)
    check(
        "the two U=+1 flat modes are zero-deviation and scalar invisible",
        len(plus_rows) == 2
        and max(abs(row["K"]) for row in plus_rows) < 2e-12
        and max(abs(row["sqrtK"]) for row in plus_rows) < 2e-12
        and max(row["scalar_overlap"] for row in plus_rows) < 2e-12,
        plus_rows,
    )
    check(
        "the two U=-1 flat modes are K=4 and Habs=pi while S is blind",
        len(minus_rows) == 2
        and max(abs(row["K"] - 4) for row in minus_rows) < 2e-12
        and max(abs(row["sqrtK"] - 2) for row in minus_rows) < 2e-12
        and max(abs(row["Habs"] - np.pi) for row in minus_rows) < 2e-12
        and max(abs(row["S"]) for row in minus_rows) < 2e-12
        and max(row["scalar_overlap"] for row in minus_rows) < 2e-12,
        minus_rows,
    )


def massive_calibration_controls() -> None:
    rows = []
    for beta in (-0.2, -0.3, -0.4, -0.6):
        species = c219.common_species(beta)
        coordinates = spectral_coordinates(walk_symbol(beta, np.zeros(3)))
        proxies = {
            name: 3
            * float(np.vdot(c210.UNIFORM, operator @ c210.UNIFORM).real)
            for name, operator in coordinates.items()
        }
        rows.append(
            {
                "beta": beta,
                "mass": species.analytic_mass,
                "phase": species.rest_phase,
                **proxies,
                "K_ratio": proxies["K"] / species.analytic_mass,
                "S_ratio": proxies["S"] / species.analytic_mass,
                "sqrtK_ratio": proxies["sqrtK"] / species.analytic_mass,
                "Habs_ratio": proxies["Habs"] / species.analytic_mass,
            }
        )
    check(
        "3 Habs equals the supplied analytic rest-mass calibration exactly",
        max(abs(row["Habs_ratio"] - 1) for row in rows) < 2e-12,
        rows,
    )
    check(
        "local K is quadratic while local S and nonlocal sqrtK are only approximations",
        max(row["K_ratio"] for row in rows) < 0.32
        and max(abs(row["S_ratio"] - 1) for row in rows) > 0.01
        and max(abs(row["sqrtK_ratio"] - 1) for row in rows) > 0.003,
        rows,
    )

    species = c219.common_species(-0.3)
    kinetic_rows = []
    for momentum_x in (0.0, 0.1, 0.2, 0.3):
        momentum = np.asarray((momentum_x, 0.0, 0.0))
        phase, vector = c210.branch_eigenpair(momentum, species)
        phase = species.rest_phase + c210.angular_difference(phase, species.rest_phase)
        coordinates = spectral_coordinates(walk_symbol(-0.3, momentum))
        kinetic_rows.append(
            {
                "momentum": momentum_x,
                "branch_phase_mass": 3 * phase,
                "Habs_mass": 3
                * float(np.vdot(vector, coordinates["Habs"] @ vector).real),
                "Q_rest": species.analytic_mass,
            }
        )
    check(
        "Habs follows the massive branch's kinetic quasienergy while Q stays static",
        max(
            abs(row["Habs_mass"] - row["branch_phase_mass"])
            for row in kinetic_rows
        )
        < 2e-12
        and all(
            kinetic_rows[index + 1]["Habs_mass"] > kinetic_rows[index]["Habs_mass"]
            for index in range(len(kinetic_rows) - 1)
        )
        and max(row["Q_rest"] for row in kinetic_rows)
        - min(row["Q_rest"] for row in kinetic_rows)
        < 2e-15,
        kinetic_rows,
    )

    held = c219.common_species(-0.35)
    curvature_mass = 1 / float(
        np.mean(np.diag(c210.curvature_tensor(held, step=1e-4)))
    )
    held_habs = 3 * float(
        np.vdot(
            c210.UNIFORM,
            spectral_coordinates(walk_symbol(-0.35, np.zeros(3)))["Habs"]
            @ c210.UNIFORM,
        ).real
    )
    check(
        "held-out Habs rest calibration agrees with independent curvature mass",
        abs(held_habs / curvature_mass - 1) < 4e-6,
        {"Habs": held_habs, "curvature_mass": curvature_mass},
    )

    unitary = walk_symbol(0.0, np.asarray((0.41, -0.23, 0.17)))
    values = np.linalg.eigvals(unitary)
    negative = min((float(np.angle(value)) for value in values), default=0.0)
    positive_magnitude_evolution = np.exp(1j * abs(negative))
    actual_evolution = np.exp(1j * negative)
    check(
        "positive Habs does not generate U on a negative-phase mode",
        negative < -0.2
        and abs(positive_magnitude_evolution - actual_evolution) > 0.5,
        {
            "phase": negative,
            "exp_i_abs_phase": positive_magnitude_evolution,
            "unitary_eigenvalue": actual_evolution,
        },
    )


def composition_controls() -> None:
    def wrap_phase(theta: float) -> float:
        return float(np.angle(np.exp(1j * theta)))

    def coordinate_row(first: float, second: float) -> dict[str, float]:
        total = wrap_phase(first + second)
        functions = {
            "K": lambda theta: 2 - 2 * np.cos(theta),
            "S": np.sin,
            "sqrtK": lambda theta: 2 * abs(np.sin(theta / 2)),
            "Habs": lambda theta: abs(wrap_phase(theta)),
            "Hlog": wrap_phase,
        }
        return {
            name: float(function(total) - function(first) - function(second))
            for name, function in functions.items()
        }

    small = coordinate_row(0.3, 0.4)
    wrapped_row = coordinate_row(2.0, 2.0)
    check(
        "no periodic K/S/sqrtK scalar is additive even before phase wrapping",
        min(abs(small[name]) for name in ("K", "S", "sqrtK")) > 0.005
        and abs(small["Habs"]) < 2e-14
        and abs(small["Hlog"]) < 2e-14,
        small,
    )
    check(
        "chosen spectral phase and magnitude lose ordinary additivity at a branch crossing",
        abs(wrapped_row["Hlog"]) > 6.0 and abs(wrapped_row["Habs"]) > 1.7,
        wrapped_row,
    )

    side = 17
    first = c227.point_carrier(side, (3, 3, 3))
    second = c227.point_carrier(side, (11, 11, 11))
    coin = c219.common_species(0.0).coin
    rows = {}
    for name, index in (("K", 0), ("S", 1)):
        sum_operator = apply_local_coordinates(first + second, coin)[index]
        separate = (
            np.vdot(first, apply_local_coordinates(first, coin)[index]).real
            + np.vdot(second, apply_local_coordinates(second, coin)[index]).real
        )
        rows[name] = float(np.vdot(first + second, sum_operator).real - separate)
    check(
        "finite-range K and S add exactly for separated same-space packets",
        max(abs(value) for value in rows.values()) < 2e-14,
        rows,
    )


def deformation_nonuniqueness_controls() -> None:
    momentum = np.asarray((0.37, -0.21, 0.16))
    species = c219.common_species(-0.3)
    stream = np.diag(np.exp(-1j * (c210.DIRECTIONS @ momentum)))

    def deformed(projector: np.ndarray, epsilon: float) -> np.ndarray:
        local = c210.I6 + (np.exp(-1j * epsilon) - 1) * projector
        return stream @ local @ species.coin

    epsilon = 1e-6
    base = stream @ species.coin
    rows = []
    for name, projector in (
        ("scalar", c210.P_SCALAR),
        ("vector", c210.P_VECTOR),
    ):
        plus = deformed(projector, epsilon)
        minus = deformed(projector, -epsilon)
        derivative = (plus - minus) / (2 * epsilon)
        response = 1j * base.conj().T @ derivative
        response = (response + response.conj().T) / 2
        covariance = []
        for frame in c210.proper_cubic_frames():
            representation = c210.direction_permutation(frame)
            covariance.append(
                np.linalg.norm(
                    representation @ projector @ representation.conj().T
                    - projector
                )
            )
        rows.append(
            {
                "name": name,
                "base_residual": float(np.linalg.norm(deformed(projector, 0) - base)),
                "unitarity": float(np.linalg.norm(plus.conj().T @ plus - c210.I6)),
                "covariance": float(max(covariance)),
                "uniform_response": float(
                    np.vdot(c210.UNIFORM, response @ c210.UNIFORM).real
                ),
                "conservation_residual": float(
                    np.linalg.norm(base.conj().T @ response @ base - response)
                ),
            }
        )
    check(
        "two equally local cubic deformations share exactly the same undeformed U",
        max(row["base_residual"] for row in rows) < 2e-15
        and max(row["unitarity"] for row in rows) < 2e-12
        and max(row["covariance"] for row in rows) < 2e-15,
        rows,
    )
    check(
        "their local response operators differ and are not automatically conserved",
        abs(rows[0]["uniform_response"] - rows[1]["uniform_response"]) > 0.9
        and min(row["conservation_residual"] for row in rows) > 0.1,
        rows,
    )

    def tangent(family) -> np.ndarray:
        plus = family(epsilon)
        minus = family(-epsilon)
        derivative = (plus - minus) / (2 * epsilon)
        response = 1j * base.conj().T @ derivative
        return (response + response.conj().T) / 2

    projector = c210.P_SCALAR
    family = lambda parameter: deformed(projector, parameter)
    response = tangent(family)
    gauge_offset = 0.37
    rephased = lambda parameter: (
        np.exp(-1j * gauge_offset * parameter) * family(parameter)
    )
    rephased_response = tangent(rephased)
    scale = 1.7
    rescaled = lambda parameter: family(scale * parameter)
    rescaled_response = tangent(rescaled)

    rng = np.random.default_rng(2285)
    vector = rng.normal(size=6) + 1j * rng.normal(size=6)
    vector /= np.linalg.norm(vector)
    density = np.outer(vector, vector.conj())
    sample = 0.23
    ordinary_channel = family(sample) @ density @ family(sample).conj().T
    rephased_channel = rephased(sample) @ density @ rephased(sample).conj().T
    check(
        "projective rephasing and parameter rescaling shift or scale the same tangent response",
        np.linalg.norm(rephased(0) - base) < 2e-15
        and np.linalg.norm(ordinary_channel - rephased_channel) < 2e-15
        and np.linalg.norm(
            rephased_response - response - gauge_offset * c210.I6
        )
        < 2e-10
        and np.linalg.norm(rescaled_response - scale * response) < 5e-10,
        {
            "same_base": float(np.linalg.norm(rephased(0) - base)),
            "same_projective_channel": float(
                np.linalg.norm(ordinary_channel - rephased_channel)
            ),
            "identity_shift": float(
                np.linalg.norm(
                    rephased_response - response - gauge_offset * c210.I6
                )
            ),
            "parameter_scale": float(
                np.linalg.norm(rescaled_response - scale * response)
            ),
        },
    )


def covariance_and_representation_controls() -> None:
    momentum = np.asarray((0.41, -0.23, 0.17))
    residuals = {name: [] for name in ("U", "K", "S", "sqrtK", "Habs")}
    for beta in (0.0, -0.3):
        unitary = walk_symbol(beta, momentum)
        coordinates = spectral_coordinates(unitary)
        for frame in c210.proper_cubic_frames():
            representation = c210.direction_permutation(frame)
            moved_u = walk_symbol(beta, frame @ momentum)
            moved = spectral_coordinates(moved_u)
            residuals["U"].append(
                np.linalg.norm(moved_u - representation @ unitary @ representation.conj().T)
            )
            for name in ("K", "S", "sqrtK", "Habs"):
                residuals[name].append(
                    np.linalg.norm(
                        moved[name]
                        - representation
                        @ coordinates[name]
                        @ representation.conj().T
                    )
                )
    check(
        "every candidate transforms in all 24 proper-cubic frames",
        max(max(values) for values in residuals.values()) < 2e-11,
        {name: max(values) for name, values in residuals.items()},
    )

    rng = np.random.default_rng(2283)
    random = rng.normal(size=(6, 6)) + 1j * rng.normal(size=(6, 6))
    basis, _ = np.linalg.qr(random)
    representation_residuals = []
    for beta in (0.0, -0.3):
        unitary = walk_symbol(beta, momentum)
        transformed = basis @ unitary @ basis.conj().T
        original = spectral_coordinates(unitary)
        changed = spectral_coordinates(transformed)
        representation_residuals.extend(
            np.linalg.norm(
                changed[name] - basis @ original[name] @ basis.conj().T
            )
            for name in original
        )
    check(
        "the tournament is invariant under internal basis presentation",
        max(representation_residuals) < 2e-11,
        max(representation_residuals),
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    complete_local_pair_controls()
    phase_reference_controls()
    deviation_transport_controls()
    full_kernel_locality_controls()
    scalar_tail_controls()
    signed_phase_lift_controls()
    massive_phase_crossing_controls()
    projected_wave_energy_controls()
    massless_and_flat_mode_controls()
    massive_calibration_controls()
    composition_controls()
    deformation_nonuniqueness_controls()
    covariance_and_representation_controls()
    print("PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "LOCAL_SPECTRAL_PAIR_PHYSICAL_INTERPRETATION_OPEN"
        if FAIL == 0
        else "CYCLE228_OPEN",
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
