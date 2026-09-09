#!/usr/bin/env python3
"""Cycle 215: exact finite-coin dilation of the cubic scalar wave.

Prove that the Cycle-214 six-direction acoustic walk has characteristic
polynomial (lambda^2-2 gamma lambda+1)(lambda-1)^2(lambda+1)^2 and that its
scalar projection obeys the centered cubic wave equation exactly.  Verify the
identity symbolically, on arbitrary complex lattice states, under local source
injection, and against the Cycle-211 Green sector.

The coin and source port remain candidate law content.  The result is a
positive conditional theorem, not a uniqueness theorem over all QCAs and not
an axiom conclusion.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path

import numpy as np
import sympy as sp

import active_cubic_source_response_cycle211_2026_07_16 as c211
import autonomous_cubic_field_emission_cycle214_2026_07_16 as c214
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import retarded_cubic_mass_field_cycle213_2026_07_16 as c213


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "FINITE_COIN_SCALAR_WAVE_DILATION_CYCLE215_NOTE_2026-07-16.md"
)
CHECKLIST = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "FINITE_COIN_SCALAR_WAVE_DILATION_CYCLE215_NO_GO_DISCIPLINE_CHECKLIST_2026-07-16.md"
)
LEDGER = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "FINITE_COIN_SCALAR_WAVE_DILATION_CYCLE215_NO_GO_LEDGER_2026-07-16.md"
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


def gamma_operator(field: np.ndarray) -> np.ndarray:
    answer = np.zeros_like(field)
    for axis in range(3):
        answer += np.roll(field, 1, axis=axis) / 6
        answer += np.roll(field, -1, axis=axis) / 6
    return answer


def scalar_projection(state: np.ndarray) -> np.ndarray:
    return np.einsum("d,xyzd->xyz", c210.UNIFORM.conj(), state, optimize=True)


def field_step(state: np.ndarray, injection: np.ndarray | None = None) -> np.ndarray:
    coined = np.einsum(
        "ab,xyzb->xyza", c214.FIELD_COIN, state, optimize=True
    )
    if injection is not None:
        coined = coined + injection[..., None] * c210.UNIFORM
    output = np.zeros_like(coined)
    for direction in range(6):
        shift = tuple(int(value) for value in c210.DIRECTIONS[direction])
        output[..., direction] = np.roll(
            coined[..., direction], shift, axis=(0, 1, 2)
        )
    return output


def rotate_field_state(state: np.ndarray, frame: np.ndarray) -> np.ndarray:
    side = state.shape[0]
    coordinates = np.indices(state.shape[:3]).reshape(3, -1)
    moved = (frame @ coordinates) % side
    spatial = np.empty_like(state)
    spatial[moved[0], moved[1], moved[2]] = state.reshape(-1, 6)
    representation = c210.direction_permutation(frame)
    return np.einsum("ab,xyzb->xyza", representation, spatial, optimize=True)


def symbolic_factorization_controls() -> None:
    x, y, z, eigenvalue = sp.symbols("x y z lambda", nonzero=True)
    phases = (x, 1 / x, y, 1 / y, z, 1 / z)
    reversal = sp.zeros(6)
    for index, reverse in enumerate((1, 0, 3, 2, 5, 4)):
        reversal[index, reverse] = 1
    coin = sp.ones(6, 6) / 3 - reversal
    stream = sp.diag(*phases)
    walk = stream @ coin
    scalar = sp.ones(6, 1) / sp.sqrt(6)
    gamma = sum(phases) / 6

    row_identity = scalar.T @ (
        walk**2 - 2 * gamma * walk + sp.eye(6)
    )
    check(
        "the scalar row obeys its quadratic wave polynomial symbolically",
        all(sp.simplify(value) == 0 for value in row_identity),
    )

    characteristic = sp.factor((eigenvalue * sp.eye(6) - walk).det())
    target = sp.factor(
        (eigenvalue - 1) ** 2
        * (eigenvalue + 1) ** 2
        * (eigenvalue**2 - 2 * gamma * eigenvalue + 1)
    )
    check(
        "the complete six-mode characteristic polynomial factors exactly",
        sp.simplify(characteristic - target) == 0,
        characteristic,
    )

    even_phase = sp.symbols("a", nonzero=True)
    identity = sp.eye(6)
    scalar_projector = scalar @ scalar.T
    vector_projector = (identity - reversal) / 2
    even_projector = (identity + reversal) / 2 - scalar_projector
    family_coin = (
        scalar_projector + vector_projector + even_phase * even_projector
    )
    family_walk = stream @ family_coin
    family_row = scalar.T @ (
        family_walk**2 - 2 * gamma * family_walk + identity
    )
    numerators = [
        sp.Poly(sp.together(value).as_numer_denom()[0], even_phase)
        for value in family_row
    ]
    common = numerators[0]
    for numerator in numerators[1:]:
        common = sp.gcd(common, numerator)
    check(
        "within the normalized scalar/vector cubic family the wave identity selects a=-1",
        sp.factor(common.as_expr()) == even_phase + 1,
        sp.factor(common.as_expr()),
    )


def exact_real_space_controls() -> None:
    rng = np.random.default_rng(215)
    side = 9
    state = rng.normal(size=(side, side, side, 6)) + 1j * rng.normal(
        size=(side, side, side, 6)
    )
    state /= np.linalg.norm(state)
    projections = [scalar_projection(state)]
    states = [state.copy()]
    for _ in range(12):
        state = field_step(state)
        states.append(state.copy())
        projections.append(scalar_projection(state))

    recurrence_residuals = []
    cycle213_residuals = []
    for tick in range(1, len(projections) - 1):
        recurrence_residuals.append(
            float(
                np.max(
                    np.abs(
                        projections[tick + 1]
                        - 2 * gamma_operator(projections[tick])
                        + projections[tick - 1]
                    )
                )
            )
        )
        cycle213_residuals.append(
            float(
                np.max(
                    np.abs(
                        projections[tick + 1]
                        - c213.wave_step(
                            projections[tick - 1],
                            projections[tick],
                            np.zeros_like(projections[tick]),
                            dt=1 / np.sqrt(3),
                        )
                    )
                )
            )
        )
    check(
        "arbitrary complex states project to the exact centered scalar wave law",
        max(recurrence_residuals) < 2e-15,
        max(recurrence_residuals),
    )
    check(
        "the projection is exactly Cycle 213 at dt^2=1/3",
        max(cycle213_residuals) < 2e-15,
        max(cycle213_residuals),
    )
    check(
        "the finite-coin parent preserves positive norm for all twelve slices",
        max(abs(np.linalg.norm(local_state) - 1) for local_state in states) < 3e-12,
    )

    shift = (2, 3, 4)
    translated = field_step(np.roll(states[0], shift, axis=(0, 1, 2)))
    check(
        "the coin-stream parent commutes with lattice translation",
        np.max(
            np.abs(translated - np.roll(states[1], shift, axis=(0, 1, 2)))
        )
        < 2e-15,
    )
    covariance_residuals = []
    for frame in c210.proper_cubic_frames():
        covariance_residuals.append(
            np.linalg.norm(
                field_step(rotate_field_state(states[0], frame))
                - rotate_field_state(states[1], frame)
            )
        )
    check(
        "the finite-coin parent commutes with all 24 proper-cubic frames",
        max(covariance_residuals) < 3e-15,
        max(covariance_residuals),
    )

    impulse = np.zeros((31, 31, 31, 6), dtype=complex)
    impulse[0, 0, 0] = c210.UNIFORM
    coordinates = np.indices((31, 31, 31))
    signed = np.minimum(coordinates, 31 - coordinates)
    manhattan = np.sum(signed, axis=0)
    cone_rows = []
    for tick in range(8):
        probability = np.sum(np.abs(impulse) ** 2, axis=3)
        cone_rows.append(
            (tick, float(np.max(probability[manhattan > tick])))
        )
        impulse = field_step(impulse)
    check(
        "the unitary dilation has an exact one-edge causal cone",
        max(row[1] for row in cone_rows) < 2e-15,
        cone_rows,
    )

    embedded = np.eye(8, dtype=complex)
    embedded[:6, :6] = c214.FIELD_COIN
    first_column = np.abs(embedded[:, 0])
    nonzero_magnitudes = np.unique(np.round(first_column[first_column > 1e-12], 12))
    check(
        "the six-state carrier embeds unitarily in three qubits",
        np.linalg.norm(embedded.conj().T @ embedded - np.eye(8)) < 2e-12,
    )
    check(
        "the embedded coin is non-Clifford by its unequal nonzero column magnitudes",
        len(nonzero_magnitudes) > 1
        and set(nonzero_magnitudes) == {round(1 / 3, 12), round(2 / 3, 12)},
        nonzero_magnitudes.tolist(),
    )


def spectral_visibility_controls() -> None:
    rng = np.random.default_rng(216)
    rows = []
    for _ in range(12):
        momentum = rng.uniform(-2.7, 2.7, size=3)
        stream = np.diag(
            np.exp(-1j * (c210.DIRECTIONS @ momentum))
        )
        walk = stream @ c214.FIELD_COIN
        values, vectors = np.linalg.eig(walk)
        gamma = float(np.mean(np.cos(momentum)))
        acoustic_phase = float(np.arccos(np.clip(gamma, -1, 1)))
        predicted = np.angle(
            np.asarray(
                (
                    1,
                    1,
                    -1,
                    -1,
                    np.exp(1j * acoustic_phase),
                    np.exp(-1j * acoustic_phase),
                )
            )
        )
        observed = np.angle(values)
        # +pi and -pi are the same eigenphase.  Canonicalize the branch before
        # sorting so a numerical sign choice at eigenvalue -1 is not counted
        # as a physical phase residual.
        predicted[np.isclose(np.abs(predicted), np.pi, atol=1e-10)] = np.pi
        observed[np.isclose(np.abs(observed), np.pi, atol=1e-10)] = np.pi
        predicted = np.sort(predicted)
        observed = np.sort(observed)
        flat_overlap = 0.0
        for index, value in enumerate(values):
            if min(abs(value - 1), abs(value + 1)) < 2e-9:
                flat_overlap = max(
                    flat_overlap,
                    abs(np.vdot(c210.UNIFORM, vectors[:, index])),
                )
        rows.append(
            (
                float(np.max(np.abs(observed - predicted))),
                float(flat_overlap),
            )
        )
    check(
        "the exact spectrum is two acoustic plus four scalar-invisible flat modes",
        max(row[0] for row in rows) < 3e-12
        and max(row[1] for row in rows) < 3e-12,
        {
            "phase_residual": max(row[0] for row in rows),
            "flat_scalar_overlap": max(row[1] for row in rows),
        },
    )

    alternative_coin = (
        c210.P_SCALAR + c210.P_VECTOR + np.exp(0.7j) * c210.P_EVEN
    )
    momentum = np.array((0.73, -0.41, 0.29))
    stream = np.diag(np.exp(-1j * (c210.DIRECTIONS @ momentum)))
    walk = stream @ alternative_coin
    state = rng.normal(size=6) + 1j * rng.normal(size=6)
    sequence = []
    for _ in range(3):
        sequence.append(np.vdot(c210.UNIFORM, state))
        state = walk @ state
    gamma = float(np.mean(np.cos(momentum)))
    residual = abs(sequence[2] - 2 * gamma * sequence[1] + sequence[0])
    check(
        "changing the even-sector phase inside the cubic unitary family breaks the wave identity",
        residual > 0.05,
        residual,
    )


def local_source_port_controls() -> None:
    rng = np.random.default_rng(217)
    side = 7
    state = rng.normal(size=(side, side, side, 6)) + 1j * rng.normal(
        size=(side, side, side, 6)
    )
    state /= np.linalg.norm(state)
    injections = [
        rng.normal(scale=0.01, size=(side, side, side))
        + 1j * rng.normal(scale=0.01, size=(side, side, side))
        for _ in range(12)
    ]
    projections = [scalar_projection(state)]
    for injection in injections:
        state = field_step(state, injection)
        projections.append(scalar_projection(state))

    residuals = []
    for tick in range(1, len(injections)):
        left = (
            projections[tick + 1]
            - 2 * gamma_operator(projections[tick])
            + projections[tick - 1]
        )
        right = gamma_operator(injections[tick]) - injections[tick - 1]
        residuals.append(float(np.max(np.abs(left - right))))
    check(
        "a local scalar injection induces an exact two-tap forced wave equation",
        max(residuals) < 3e-15,
        max(residuals),
    )

    point = np.zeros((side, side, side), dtype=complex)
    point[0, 0, 0] = 1
    constant_port_source = gamma_operator(point) - point
    check(
        "this specific constant one-field port supplies -L(point)/6 rather than a point rho",
        np.max(
            np.abs(constant_port_source + c213.laplacian(point) / 6)
        )
        < 2e-15
        and abs(np.sum(constant_port_source)) < 2e-15,
    )


def green_sector_control() -> None:
    side = 15
    source = c211.point_source(side)
    exact = c211.solve_field(source)
    previous = np.zeros_like(source)
    current = np.zeros_like(source)
    average = np.zeros_like(source)
    checkpoints = {}
    for tick in range(1, 6001):
        following = c213.wave_step(
            previous,
            current,
            source,
            dt=1 / np.sqrt(3),
        )
        previous, current = current, following
        average += current
        if tick in (100, 1000, 6000):
            checkpoints[tick] = float(
                np.linalg.norm(average / tick - exact) / np.linalg.norm(exact)
            )
    check(
        "the dilation-selected wave coefficient retains the Cycle-211 Green sector",
        checkpoints[6000] < 7e-4
        and checkpoints[6000] < checkpoints[1000] < checkpoints[100],
        checkpoints,
    )


def document_contract() -> None:
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    checklist = " ".join(CHECKLIST.read_text(encoding="utf-8").lower().split())
    ledger = " ".join(LEDGER.read_text(encoding="utf-8").lower().split())
    required_note = (
        "exact finite-coin unitary dilation",
        "dt^2=1/3",
        "two acoustic modes",
        "four scalar-invisible flat modes",
        "source port",
        "static green sector",
        "not a uniqueness theorem over all qcas",
        "no axiom conclusion",
        "draft parking branch",
    )
    required_checklist = tuple(f"n{index}" for index in range(1, 9)) + (
        "status: fail",
        "partial-attempt-with-named-untested-routes",
    )
    required_ledger = (
        "broader no-go not shipped",
        "multi-field",
        "exchange observable",
        "local reservoir",
        "next attacks",
    )
    check(
        "positive note preserves mechanism, attribution, and scope",
        not tuple(phrase for phrase in required_note if phrase not in note),
    )
    check(
        "N1-N8 checklist visibly fails and demotes the broader negative claim",
        not tuple(phrase for phrase in required_checklist if phrase not in checklist),
    )
    check(
        "failed broader no-go is recorded with live alternative routes",
        not tuple(phrase for phrase in required_ledger if phrase not in ledger),
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    document_contract()
    symbolic_factorization_controls()
    exact_real_space_controls()
    spectral_visibility_controls()
    local_source_port_controls()
    green_sector_control()
    print(f"SUMMARY {PASS} passed, {FAIL} failed")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
