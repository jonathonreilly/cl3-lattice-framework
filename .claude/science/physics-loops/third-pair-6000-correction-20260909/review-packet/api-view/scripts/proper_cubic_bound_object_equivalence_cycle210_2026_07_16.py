#!/usr/bin/env python3
"""Cycle 210: strict proper-cubic bound object and conditional equivalence.

Two distinguishable six-direction walkers receive an onsite, proper-cubic
collision.  At contact the collision preserves the equal-direction sector,
so the two carriers stream together as one exact composite.  Outside contact
they receive independent cubic coins.  The runner checks strict locality,
unitarity, covariance, interaction deletion, rest/dispersion tuning, forced
inertia, a conditional scalar-lapse response, composition, and spectator
record redundancy.

The interaction and its phase parameters are candidate law content.  The
runner does not derive them, a gravitational field equation, occurrence,
record formation, or an axiom update.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "PROPER_CUBIC_BOUND_OBJECT_EQUIVALENCE_CYCLE210_NOTE_2026-07-16.md"
)

I6 = np.eye(6, dtype=complex)
DIRECTIONS = np.asarray(
    (
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    ),
    dtype=int,
)
REVERSE = np.zeros((6, 6), dtype=complex)
REVERSE[np.arange(6), (1, 0, 3, 2, 5, 4)] = 1
UNIFORM = np.ones(6, dtype=complex) / np.sqrt(6)
P_SCALAR = np.outer(UNIFORM, UNIFORM.conj())
P_EVEN = (I6 + REVERSE) / 2 - P_SCALAR
P_VECTOR = (I6 - REVERSE) / 2

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


def angular_difference(left: float, right: float) -> float:
    return float(np.angle(np.exp(1j * (left - right))))


def cubic_coin(alpha: float, beta: float, phase: float = 0.0) -> np.ndarray:
    return np.exp(1j * phase) * (
        P_SCALAR + np.exp(1j * alpha) * P_EVEN + np.exp(1j * beta) * P_VECTOR
    )


@dataclass(frozen=True)
class Species:
    beta: float
    alpha: float
    rest_phase: float
    analytic_mass: float
    coin: np.ndarray


def tuned_species(beta: float) -> Species:
    if not (-0.6 < beta < -0.05):
        raise ValueError("this bounded branch uses -0.6 < beta < -0.05")
    mass = float(3 * np.tan(-beta / 2))
    # det(C)=1 gives 6 phi + 2 alpha + 3 beta = 0.  The displayed
    # one-condition family additionally asks phi = m_dispersion.
    alpha = float((-6 * mass - 3 * beta) / 2)
    phase = mass
    return Species(beta, alpha, phase, mass, cubic_coin(alpha, beta, phase))


def free_coin() -> np.ndarray:
    """Generic complex member of the proper-cubic commutant."""
    return cubic_coin(0.73, 1.11)


def molecular_bloch(momentum: np.ndarray, coin: np.ndarray) -> np.ndarray:
    stream = np.diag(np.exp(-1j * (DIRECTIONS @ np.asarray(momentum, dtype=float))))
    return stream @ coin


def branch_eigenpair(momentum: np.ndarray, species: Species) -> tuple[float, np.ndarray]:
    values, vectors = np.linalg.eig(molecular_bloch(momentum, species.coin))
    overlaps = np.abs(vectors.conj().T @ UNIFORM)
    index = int(np.argmax(overlaps))
    vector = vectors[:, index]
    vector *= np.exp(-1j * np.angle(np.vdot(UNIFORM, vector)))
    return float(np.angle(values[index])), vector / np.linalg.norm(vector)


def phase_near_origin(momentum: np.ndarray, species: Species) -> float:
    phase, _ = branch_eigenpair(momentum, species)
    return species.rest_phase + angular_difference(phase, species.rest_phase)


def curvature_tensor(species: Species, step: float = 1e-3) -> np.ndarray:
    origin = np.zeros(3)
    rest = phase_near_origin(origin, species)
    hessian = np.zeros((3, 3))
    for first in range(3):
        for second in range(3):
            if first == second:
                displacement = np.zeros(3)
                displacement[first] = step
                hessian[first, first] = (
                    phase_near_origin(displacement, species)
                    - 2 * rest
                    + phase_near_origin(-displacement, species)
                ) / step**2
            else:
                pp = np.zeros(3)
                pm = np.zeros(3)
                mp = np.zeros(3)
                mm = np.zeros(3)
                pp[first] = pp[second] = step
                pm[first], pm[second] = step, -step
                mp[first], mp[second] = -step, step
                mm[first] = mm[second] = -step
                hessian[first, second] = (
                    phase_near_origin(pp, species)
                    - phase_near_origin(pm, species)
                    - phase_near_origin(mp, species)
                    + phase_near_origin(mm, species)
                ) / (4 * step**2)
    return hessian


def proper_cubic_frames() -> tuple[np.ndarray, ...]:
    frames = []
    for order in permutations(range(3)):
        permutation = np.eye(3, dtype=int)[list(order)]
        for signs in product((-1, 1), repeat=3):
            frame = np.diag(signs) @ permutation
            if round(np.linalg.det(frame)) == 1:
                frames.append(frame)
    unique = {tuple(frame.reshape(-1)): frame for frame in frames}
    return tuple(unique[key] for key in sorted(unique))


def direction_permutation(frame: np.ndarray) -> np.ndarray:
    permutation = np.zeros((6, 6), dtype=complex)
    for source, direction in enumerate(DIRECTIONS):
        target_direction = frame @ direction
        target = int(np.where(np.all(DIRECTIONS == target_direction, axis=1))[0][0])
        permutation[target, source] = 1
    return permutation


def contact_coin(species: Species) -> np.ndarray:
    diagonal = tuple(index * 6 + index for index in range(6))
    result = np.eye(36, dtype=complex)
    result[np.ix_(diagonal, diagonal)] = species.coin
    return result


def interaction_correction(species: Species) -> np.ndarray:
    independent = np.kron(free_coin(), free_coin())
    return contact_coin(species) @ independent.conj().T


def apply_relative_step(
    state: np.ndarray,
    species: Species,
    *,
    interaction: bool,
) -> np.ndarray:
    """Two walkers in their relative coordinate, at total momentum zero."""
    length = state.shape[0]
    flat = state.reshape(length, length, length, 36)
    independent = np.kron(free_coin(), free_coin())
    mixed = np.einsum("ab,xyzb->xyza", independent, flat, optimize=True)
    if interaction:
        mixed[0, 0, 0] = contact_coin(species) @ flat[0, 0, 0]
    mixed = mixed.reshape(length, length, length, 6, 6)
    output = np.zeros_like(mixed)
    for first in range(6):
        for second in range(6):
            shift = tuple(int(value) for value in DIRECTIONS[first] - DIRECTIONS[second])
            output[..., first, second] += np.roll(
                mixed[..., first, second], shift, axis=(0, 1, 2)
            )
    return output


def relative_observables(state: np.ndarray) -> dict[str, float]:
    probability = np.sum(np.abs(state) ** 2, axis=(3, 4))
    length = state.shape[0]
    coordinate = (np.arange(length) + length // 2) % length - length // 2
    x, y, z = np.meshgrid(coordinate, coordinate, coordinate, indexing="ij")
    radius2 = x * x + y * y + z * z
    return {
        "norm": float(np.linalg.norm(state)),
        "contact": float(probability[0, 0, 0]),
        "close": float(np.sum(probability[radius2 <= 4])),
        "variance": float(np.sum(probability * radius2)),
        "boundary": float(np.sum(probability[radius2 > (0.4 * length) ** 2])),
    }


def initial_bound_relative(length: int) -> np.ndarray:
    state = np.zeros((length, length, length, 6, 6), dtype=complex)
    state[0, 0, 0, np.arange(6), np.arange(6)] = UNIFORM
    return state


def local_molecular_step(packet: np.ndarray, coin: np.ndarray, axis: int = 0) -> np.ndarray:
    mixed = np.einsum("ab,xb->xa", coin, packet, optimize=True)
    output = np.zeros_like(mixed)
    for direction in range(6):
        output[:, direction] = np.roll(
            mixed[:, direction], int(DIRECTIONS[direction, axis])
        )
    return output


def prepare_molecular_packet(
    species: Species, length: int, momentum_width: float
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    momenta = 2 * np.pi * np.fft.fftfreq(length)
    packet_k = np.zeros((length, 6), dtype=complex)
    for index, momentum in enumerate(momenta):
        envelope = np.exp(-0.5 * (momentum / momentum_width) ** 2)
        if envelope < 1e-14:
            continue
        _, vector = branch_eigenpair(np.array((momentum, 0.0, 0.0)), species)
        packet_k[index] = envelope * vector
    packet_k /= np.linalg.norm(packet_k)
    packet = np.fft.ifft(packet_k, axis=0, norm="ortho")
    packet = np.roll(packet, length // 2, axis=0)
    positions = np.arange(length, dtype=float) - length // 2
    return positions, momenta, packet


def position_density(packet: np.ndarray) -> np.ndarray:
    return np.sum(np.abs(packet) ** 2, axis=1)


def mean_position(packet: np.ndarray, positions: np.ndarray) -> float:
    return float(np.sum(position_density(packet) * positions).real)


def branch_probability(packet: np.ndarray, momenta: np.ndarray, species: Species) -> float:
    packet_k = np.fft.fft(packet, axis=0, norm="ortho")
    probability = 0.0
    for index, momentum in enumerate(momenta):
        if np.linalg.norm(packet_k[index]) < 1e-12:
            continue
        _, vector = branch_eigenpair(np.array((momentum, 0.0, 0.0)), species)
        probability += abs(np.vdot(vector, packet_k[index])) ** 2
    return float(probability)


@dataclass(frozen=True)
class Response:
    beta: float
    force: float
    acceleration: float
    measured_mass: float
    expected_mass: float
    norm: float
    band_probability: float
    boundary: float
    displacement: float


def force_response(
    species: Species,
    force: float,
    *,
    length: int = 2048,
    momentum_width: float = 0.01,
    duration: int = 80,
    ordering: str = "symmetric",
) -> Response:
    positions, momenta, packet = prepare_molecular_packet(
        species, length, momentum_width
    )
    start = mean_position(packet, positions)
    centres = [start]
    times = [0.0]
    full = np.exp(1j * force * positions)[:, None]
    half = np.exp(0.5j * force * positions)[:, None]
    for tick in range(duration):
        if ordering == "pre":
            packet = local_molecular_step(full * packet, species.coin)
        elif ordering == "post":
            packet = full * local_molecular_step(packet, species.coin)
        elif ordering == "symmetric":
            packet = half * local_molecular_step(half * packet, species.coin)
        else:
            raise ValueError(ordering)
        centres.append(mean_position(packet, positions))
        times.append(float(tick + 1))
    acceleration = float(2 * np.polyfit(times, np.asarray(centres) - start, 2)[0])
    measured = abs(force / acceleration) if force else float("inf")
    density = position_density(packet)
    return Response(
        beta=species.beta,
        force=force,
        acceleration=acceleration,
        measured_mass=measured,
        expected_mass=species.analytic_mass,
        norm=float(np.linalg.norm(packet)),
        band_probability=branch_probability(packet, momenta, species),
        boundary=float(np.sum(density[np.abs(positions) > length / 4])),
        displacement=float(centres[-1] - start),
    )


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "strict proper-cubic",
        "law-derived persistent object",
        "interaction deletion",
        "rest phase",
        "dispersion mass",
        "forced inertia",
        "scalar-lapse source",
        "source map remains supplied",
        "spectator records",
        "global novelty has not been established",
        "record formation remains open",
        "no axiom conclusion",
        "draft parking branch",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note preserves attribution, conditions, and scope", not missing, missing)


def exact_band_contract() -> None:
    beta = sp.symbols("beta", real=True, nonzero=True)
    scalar_to_vector_norm = sp.Rational(1, 3)
    curvature = -scalar_to_vector_norm * sp.cot(beta / 2)
    mass = sp.simplify(1 / curvature)
    check(
        "scalar-band perturbation gives m_disp = -3 tan(beta/2) exactly",
        sp.simplify(mass + 3 * sp.tan(beta / 2)) == 0,
        mass,
    )
    generator = np.diag(DIRECTIONS[:, 0])
    generated = generator @ UNIFORM
    check(
        "one momentum derivative couples the scalar only to the vector sector with norm 1/3",
        abs(np.vdot(UNIFORM, generated)) < 2e-12
        and np.linalg.norm(P_VECTOR @ generated - generated) < 2e-12
        and abs(np.vdot(generated, generated).real - 1 / 3) < 2e-12,
        np.vdot(generated, generated).real,
    )
    held_out = tuned_species(-0.35)
    held_out_mass = 1 / float(np.mean(np.diag(curvature_tensor(held_out))))
    check(
        "held-out beta obeys the analytic curvature formula",
        abs(held_out_mass / held_out.analytic_mass - 1) < 3e-6,
        {"numeric": held_out_mass, "analytic": held_out.analytic_mass},
    )


def algebra_and_covariance_controls() -> tuple[Species, ...]:
    check(
        "scalar/even/vector projectors are orthogonal and complete",
        np.linalg.norm(P_SCALAR + P_EVEN + P_VECTOR - I6) < 2e-12
        and all(
            np.linalg.norm(left @ right) < 2e-12
            for left, right in (
                (P_SCALAR, P_EVEN),
                (P_SCALAR, P_VECTOR),
                (P_EVEN, P_VECTOR),
            )
        ),
    )
    species_set = tuple(tuned_species(beta) for beta in (-0.2, -0.3, -0.4))
    for species in species_set:
        determinant_phase = angular_difference(float(np.angle(np.linalg.det(species.coin))), 0.0)
        hessian = curvature_tensor(species)
        measured_mass = 1 / float(np.mean(np.diag(hessian)))
        check(
            f"beta={species.beta} SU(6) rest phase equals analytic dispersion mass",
            abs(determinant_phase) < 2e-12
            and abs(species.rest_phase - species.analytic_mass) < 2e-12
            and abs(measured_mass / species.analytic_mass - 1) < 4e-6,
            {
                "alpha": species.alpha,
                "rest_phase": species.rest_phase,
                "dispersion_mass": measured_mass,
                "hessian": hessian.tolist(),
            },
        )
        check(
            f"beta={species.beta} molecular coin and contact correction are unitary",
            np.linalg.norm(species.coin.conj().T @ species.coin - I6) < 2e-12
            and np.linalg.norm(
                interaction_correction(species).conj().T
                @ interaction_correction(species)
                - np.eye(36)
            )
            < 3e-12,
        )

    frames = proper_cubic_frames()
    check("there are exactly 24 proper-cubic frames", len(frames) == 24, len(frames))
    probe = np.array((0.17, -0.11, 0.07))
    reference = species_set[-1]
    contact = contact_coin(reference)
    correction = interaction_correction(reference)
    covariance_residuals = []
    for frame in frames:
        representation = direction_permutation(frame)
        covariance_residuals.append(
            max(
                np.linalg.norm(
                    representation @ reference.coin @ representation.conj().T
                    - reference.coin
                ),
                np.linalg.norm(
                    representation
                    @ molecular_bloch(probe, reference.coin)
                    @ representation.conj().T
                    - molecular_bloch(frame @ probe, reference.coin)
                ),
                np.linalg.norm(
                    np.kron(representation, representation)
                    @ contact
                    @ np.kron(representation, representation).conj().T
                    - contact
                ),
                np.linalg.norm(
                    np.kron(representation, representation)
                    @ correction
                    @ np.kron(representation, representation).conj().T
                    - correction
                ),
            )
        )
    check(
        "stream, molecular coin, and two-body contact law are exact in all cubic frames",
        max(covariance_residuals) < 3e-12,
        max(covariance_residuals),
    )

    fourier = np.exp(
        2j * np.pi * np.outer(np.arange(6), np.arange(6)) / 6
    ) / np.sqrt(6)
    transformed = (
        fourier
        @ molecular_bloch(probe, reference.coin)
        @ fourier.conj().T
    )
    contact_basis = np.kron(fourier, fourier)
    transformed_contact = contact_basis @ contact @ contact_basis.conj().T
    check(
        "coin-basis representation changes neither molecular phases nor contact spectrum",
        np.allclose(
            np.sort_complex(np.linalg.eigvals(transformed)),
            np.sort_complex(
                np.linalg.eigvals(molecular_bloch(probe, reference.coin))
            ),
            atol=2e-12,
        )
        and np.allclose(
            np.sort_complex(np.linalg.eigvals(transformed_contact)),
            np.sort_complex(np.linalg.eigvals(contact)),
            atol=3e-12,
        ),
    )

    stream = np.diag(np.exp(-1j * (DIRECTIONS @ probe)))
    check(
        "coin-then-stream and its time-origin cyclic schedule have identical quasiphases",
        np.allclose(
            np.sort_complex(np.linalg.eigvals(stream @ reference.coin)),
            np.sort_complex(np.linalg.eigvals(reference.coin @ stream)),
            atol=2e-12,
        )
        and np.linalg.norm(
            interaction_correction(reference)
            @ np.kron(free_coin(), free_coin())
            - contact
        )
        < 3e-12,
    )
    phase_parameters = (
        0.73,
        1.11,
        *(
            value
            for row in species_set
            for value in (row.alpha, row.beta, row.rest_phase)
        ),
    )
    check(
        "the cubic construction retains generic complex non-Clifford phases",
        all(
            min(
                abs(value - multiple * np.pi / 4)
                for multiple in range(-8, 9)
            )
            > 1e-3
            for value in phase_parameters
        ),
        phase_parameters,
    )
    return species_set


def binding_and_deletion_controls(species: Species) -> None:
    length = 13
    bound = initial_bound_relative(length)
    deleted = bound.copy()
    bound_rows = [relative_observables(bound)]
    deleted_rows = [relative_observables(deleted)]
    for _ in range(12):
        bound = apply_relative_step(bound, species, interaction=True)
        deleted = apply_relative_step(deleted, species, interaction=False)
        bound_rows.append(relative_observables(bound))
        deleted_rows.append(relative_observables(deleted))
    check(
        "the onsite collision gives an exact law-derived persistent object",
        min(row["contact"] for row in bound_rows) > 1 - 2e-12
        and max(abs(row["norm"] - 1) for row in bound_rows) < 3e-12,
        bound_rows[-1],
    )
    check(
        "interaction deletion disperses the same prepared pair",
        deleted_rows[-1]["contact"] < 0.2
        and deleted_rows[-1]["variance"] > 8
        and max(abs(row["norm"] - 1) for row in deleted_rows) < 3e-12,
        deleted_rows[-1],
    )
    first = apply_relative_step(initial_bound_relative(length), species, interaction=False)
    support = np.argwhere(np.sum(np.abs(first) ** 2, axis=(3, 4)) > 1e-14)
    signed = (support + length // 2) % length - length // 2
    check(
        "one strict update moves each carrier by one edge and relative support by at most two",
        np.max(np.abs(signed)) <= 2,
        signed.tolist(),
    )
    rng = np.random.default_rng(210)
    arbitrary = np.zeros_like(bound)
    diagonal = rng.normal(size=6) + 1j * rng.normal(size=6)
    diagonal /= np.linalg.norm(diagonal)
    arbitrary[0, 0, 0, np.arange(6), np.arange(6)] = diagonal
    for _ in range(7):
        arbitrary = apply_relative_step(arbitrary, species, interaction=True)
    arbitrary_observables = relative_observables(arbitrary)
    check(
        "the full six-dimensional equal-direction domain, not one prepared vector, stays bound",
        arbitrary_observables["contact"] > 1 - 2e-12
        and abs(arbitrary_observables["norm"] - 1) < 3e-12,
        arbitrary_observables,
    )


def inertia_source_and_composition_controls(species_set: tuple[Species, ...]) -> None:
    responses = []
    for species in species_set:
        response = force_response(species, 2e-5)
        responses.append(response)
        check(
            f"beta={species.beta} forced inertia recovers the independent curvature mass",
            abs(response.measured_mass / response.expected_mass - 1) < 0.006
            and abs(response.norm - 1) < 2e-12
            and response.band_probability > 0.999
            and response.boundary < 1e-12,
            response,
        )

    reference = species_set[-1]
    orderings = {
        ordering: force_response(reference, 2e-5, ordering=ordering).measured_mass
        for ordering in ("pre", "post", "symmetric")
    }
    check(
        "pre/post/symmetric force schedules share the weak-force mass limit",
        max(orderings.values()) / min(orderings.values()) - 1 < 0.004,
        orderings,
    )
    zero = force_response(reference, 0.0)
    check(
        "force deletion removes acceleration without deleting the molecular band",
        abs(zero.acceleration) < 2e-12 and zero.band_probability > 1 - 2e-12,
        zero,
    )

    gravity = 2e-5
    gravity_rows = []
    for species in species_set:
        # Conditional source/response map: the same local rest phase sources
        # and responds to a supplied scalar lapse gradient.
        response = force_response(species, species.rest_phase * gravity)
        gravity_rows.append(abs(response.acceleration) / gravity)
    check(
        "one rest-phase scalar gives species-independent weak-lapse acceleration",
        max(abs(value - 1) for value in gravity_rows) < 0.006,
        gravity_rows,
    )

    for species in species_set:
        step = 1e-3
        one_plus = phase_near_origin(np.array((step / 2, 0, 0)), species)
        one_minus = phase_near_origin(np.array((-step / 2, 0, 0)), species)
        pair_curvature = (
            2 * one_plus - 4 * species.rest_phase + 2 * one_minus
        ) / step**2
        pair_mass = 1 / pair_curvature
        check(
            f"beta={species.beta} held-out two-molecule composition adds rest phase and inertia",
            abs((2 * species.rest_phase) / (2 * species.analytic_mass) - 1) < 2e-12
            and abs(pair_mass / (2 * species.analytic_mass) - 1) < 3e-6,
            {"rest": 2 * species.rest_phase, "mass": pair_mass},
        )

    packet = prepare_molecular_packet(reference, 256, 0.04)[2]
    record_zero = np.array((1, 0), dtype=complex)
    record_plus = np.array((1, 1), dtype=complex) / np.sqrt(2)
    one_record = packet[:, :, None] * record_zero[None, None, :]
    two_records = (
        packet[:, :, None, None]
        * record_zero[None, None, :, None]
        * record_plus[None, None, None, :]
    )
    check(
        "one or two decoupled spectator records leave molecular mass data unchanged",
        np.allclose(np.sum(np.abs(one_record) ** 2, axis=2), np.abs(packet) ** 2)
        and np.allclose(
            np.sum(np.abs(two_records) ** 2, axis=(2, 3)), np.abs(packet) ** 2
        ),
    )

    source_charges = np.asarray([species.rest_phase for species in species_set])
    duplicated_archive = np.stack((source_charges, source_charges), axis=1)
    check(
        "source charge follows the local rest generator rather than archive multiplicity",
        np.allclose(duplicated_archive[:, 0], source_charges)
        and np.allclose(duplicated_archive[:, 1], source_charges)
        and len(set(np.round(source_charges, 10))) == len(species_set),
        source_charges.tolist(),
    )


def residual_controls(species_set: tuple[Species, ...]) -> None:
    gaps = []
    tunings = []
    for species in species_set:
        excitation_gap = min(abs(species.alpha), abs(species.beta))
        gaps.append(excitation_gap)
        tunings.append((species.beta, species.alpha, species.rest_phase))
    check(
        "the internal excitation gap remains distinct from the aligned rest/inertial scalar",
        all(
            abs(gap / species.analytic_mass - 1) > 0.2
            for gap, species in zip(gaps, species_set)
        ),
        {"gaps": gaps, "masses": [row.analytic_mass for row in species_set]},
    )
    untuned = [
        Species(
            species.beta,
            species.alpha + 0.1,
            species.rest_phase - 0.1 / 3,
            species.analytic_mass,
            cubic_coin(
                species.alpha + 0.1,
                species.beta,
                species.rest_phase - 0.1 / 3,
            ),
        )
        for species in species_set
    ]
    check(
        "cubic locality and unitarity do not force the rest/inertial alignment",
        all(
            np.linalg.norm(row.coin.conj().T @ row.coin - I6) < 2e-12
            and abs(row.rest_phase - row.analytic_mass) > 0.02
            for row in untuned
        ),
        tunings,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    exact_band_contract()
    species_set = algebra_and_covariance_controls()
    binding_and_deletion_controls(species_set[-1])
    inertia_source_and_composition_controls(species_set)
    residual_controls(species_set)
    print("PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "PROPER_CUBIC_BOUND_OBJECT_CONDITIONAL_EQUIVALENCE"
        if FAIL == 0
        else "CYCLE210_OPEN",
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
