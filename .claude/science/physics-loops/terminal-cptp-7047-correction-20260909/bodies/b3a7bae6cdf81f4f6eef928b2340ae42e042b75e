#!/usr/bin/env python3
"""Cycle 317: bounded physical contact-to-ternary/Born-forcing bridge.

The accepted Cycle-311 M64 fixed-seam code contains, for every two-particle
label, an input and a separated slice.  On that two-ray code the actual
Cycle-230 contact is diag(exp(i g), 1).  This runner constructs Naimark
isometries whose effects are derived by pointer compression, rather than
entered as an effect menu by hand:

* one fixed contact-sensitive trine instrument with three outcomes; and
* a three-pointer-M2 compiler for the bounded split/merge basis used by the
  PR-5479 mixed-projective Born-forcing proof.

The instrument remains a conditional quantum apparatus.  Pointer labels are
not occurrences or Records, and conditional Born weights are not frequencies.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import ceil, log2, sqrt
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18 as c311


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CONTACT_TERNARY_BORN_FORCING_BRIDGE_CYCLE317_NOTE_2026-07-18.md"
)
TOL = 5.0e-11
POINTER_DIMENSION = 8
POINTER_M2 = 3
PASS = 0
FAIL = 0

I2 = np.eye(2, dtype=complex)
X = np.asarray(((0, 1), (1, 0)), dtype=complex)
Y = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
Z = np.asarray(((1, 0), (0, -1)), dtype=complex)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-317 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "actual cycle-230 contact",
        "cycle-311 m64 fixed-seam code",
        "ternary trine instrument",
        "effects are obtained from the dilation",
        "x1^(8)",
        "three pointer m2",
        "effect functionality remains a hypothesis",
        "all 24 proper-cubic frames",
        "held l=6",
        "contact deletion changes the labeled effects",
        "one-particle mass fixture",
        "pointer labels are not records",
        "dephasing is not occurrence",
        "conditional born weights are not frequencies",
        "actual member remains open",
        "global additivity remains open",
        "calibration remains open",
        "supplied-structure inventory",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "broad gate status: fail / do not ship",
        "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check(
        "the note preserves the physical dilation, forcing, semantic, inventory, and N1-N8 contracts",
        not missing,
        missing,
    )


def basis(dimension: int, index: int) -> np.ndarray:
    vector = np.zeros(dimension, dtype=complex)
    vector[index] = 1
    return vector


def projector_bloch(vector: np.ndarray) -> np.ndarray:
    vector = np.asarray(vector, dtype=float)
    if vector.shape != (3,) or abs(np.linalg.norm(vector) - 1) > 1e-10:
        raise ValueError("a Bloch projector needs one unit three-vector")
    return (I2 + vector[0] * X + vector[1] * Y + vector[2] * Z) / 2


@dataclass(frozen=True)
class PhysicalFixture:
    length: int
    code: object
    encoder: object
    basis_rows: tuple
    occurrence: dict
    exchange: np.ndarray
    full_encoding: np.ndarray
    two_ray_encoding: np.ndarray
    contact: np.ndarray
    physical_contact: np.ndarray
    constraint: np.ndarray


def physical_fixture(length: int) -> PhysicalFixture:
    code = c311.c269.build_code(length)
    encoder = c311.common_encoder(code)
    basis_rows, flagged, occurrence = c311.flagged_basis_and_encoding(encoder)
    exchange = c311.exchange_matrix(encoder, occurrence)
    full_encoding = c311.constrained_encoding(flagged, exchange)
    # One two-particle wedge ray, before and after the fixed seam.  The
    # contact phases are exp(ig) and 1, so this is a same-number phase
    # reference rather than the cross-number reference used in Cycle 285.
    indices = tuple(
        c311.SEAM_INDEX[(2, (0, 1), stream_slice)]
        for stream_slice in (0, 1)
    )
    two_ray_encoding = full_encoding[:, indices]
    logical_contact = c311.logical_contact(c311.COUPLING)
    contact = logical_contact[np.ix_(indices, indices)]
    old_contact = c311.flagged_contact(
        encoder, basis_rows, c311.COUPLING
    )
    physical_contact = c311.gauge_lift(old_contact, exchange)
    constraint = c311.role_constraint(exchange)
    return PhysicalFixture(
        length,
        code,
        encoder,
        basis_rows,
        occurrence,
        exchange,
        full_encoding,
        two_ray_encoding,
        contact,
        physical_contact,
        constraint,
    )


def physical_subcode_controls() -> dict[int, PhysicalFixture]:
    fixtures = {length: physical_fixture(length) for length in (3, 6)}
    rows = []
    for length, fixture in fixtures.items():
        f = fixture.two_ray_encoding
        full_projector = fixture.full_encoding @ fixture.full_encoding.conj().T
        rows.append(
            {
                "L": length,
                "held": length == 6,
                "gram": float(np.linalg.norm(f.conj().T @ f - I2)),
                "contact_intertwiner": float(
                    np.linalg.norm(
                        fixture.physical_contact @ f - f @ fixture.contact
                    )
                ),
                "constraint": float(np.linalg.norm(fixture.constraint @ f - f)),
                "code_leakage": float(
                    np.linalg.norm((np.eye(510) - full_projector) @ f)
                ),
            }
        )
    expected_contact = np.diag((np.exp(1j * c311.COUPLING), 1)).astype(complex)
    check(
        "the accepted Cycle-311 same-number seam qubit carries the actual Cycle-230 contact as diag(exp(ig),1) through held L=6",
        all(
            max(
                row["gram"],
                row["contact_intertwiner"],
                row["constraint"],
                row["code_leakage"],
            )
            < TOL
            for row in rows
        )
        and all(
            np.linalg.norm(fixture.contact - expected_contact) < TOL
            for fixture in fixtures.values()
        ),
        rows,
    )

    species = c311.c219.common_species(-0.3)
    one_particle = c311.exterior_matrix(species.coin, 1)
    mass_residual = abs(c311.c219.rest_mass(species) / species.analytic_mass - 1)
    check(
        "the apparatus subcode is N=2 throughout while the inherited one-particle mass fixture and contact identity remain unchanged",
        one_particle.shape == (6, 6)
        and np.linalg.norm(one_particle.conj().T @ one_particle - np.eye(6)) < TOL
        and mass_residual < 3e-12
        and all(
            np.max(
                np.abs(
                    np.diag(c311.logical_contact(c311.COUPLING))[
                        [c311.SEAM_INDEX[(1, (direction,), 0)] for direction in range(6)]
                    ]
                    - 1
                )
            )
            == 0
            for _fixture in (0,)
        ),
        {
            "apparatus_particle_number": 2,
            "one_particle_contact": "identity",
            "mass_relative_residual": mass_residual,
        },
    )
    return fixtures


def stack_isometry(kraus: tuple[np.ndarray, ...]) -> np.ndarray:
    if not 1 <= len(kraus) <= POINTER_DIMENSION:
        raise ValueError("the bounded apparatus has one to eight fine labels")
    if any(operator.shape != (2, 2) for operator in kraus):
        raise ValueError("every fine Kraus operator acts on the seam qubit")
    padded = kraus + tuple(
        np.zeros((2, 2), dtype=complex)
        for _ in range(POINTER_DIMENSION - len(kraus))
    )
    return np.vstack(padded)


def derived_effects(
    isometry: np.ndarray, groups: tuple[tuple[int, ...], ...]
) -> tuple[np.ndarray, ...]:
    if isometry.shape != (2 * POINTER_DIMENSION, 2):
        raise ValueError("expected a two-dimensional system and three pointer M2")
    flattened = tuple(index for group in groups for index in group)
    if len(flattened) != len(set(flattened)) or any(
        not 0 <= index < POINTER_DIMENSION for index in flattened
    ):
        raise ValueError("coarse pointer groups must be disjoint and in range")
    blocks = tuple(
        isometry[2 * index : 2 * (index + 1), :]
        for index in range(POINTER_DIMENSION)
    )
    return tuple(
        sum(
            (blocks[index].conj().T @ blocks[index] for index in group),
            start=np.zeros((2, 2), dtype=complex),
        )
        for group in groups
    )


def physical_isometry(
    two_ray_encoding: np.ndarray, kraus: tuple[np.ndarray, ...]
) -> np.ndarray:
    padded = kraus + tuple(
        np.zeros((2, 2), dtype=complex)
        for _ in range(POINTER_DIMENSION - len(kraus))
    )
    return np.vstack(tuple(two_ray_encoding @ operator for operator in padded))


def menu_metrics(effects: tuple[np.ndarray, ...]) -> dict[str, float]:
    eigenvalues = np.concatenate(
        tuple(np.linalg.eigvalsh((effect + effect.conj().T) / 2) for effect in effects)
    )
    return {
        "normalization": float(np.linalg.norm(sum(effects) - I2)),
        "minimum_eigenvalue": float(np.min(eigenvalues)),
        "maximum_eigenvalue": float(np.max(eigenvalues)),
    }


def contact_trine_controls(
    fixture: PhysicalFixture,
) -> tuple[tuple[np.ndarray, ...], tuple[np.ndarray, ...]]:
    directions = tuple(
        np.asarray((np.cos(2 * np.pi * index / 3), np.sin(2 * np.pi * index / 3), 0.0))
        for index in range(3)
    )
    projectors = tuple(projector_bloch(direction) for direction in directions)
    kraus = tuple(sqrt(2 / 3) * projector @ fixture.contact for projector in projectors)
    isometry = stack_isometry(kraus)
    effects = derived_effects(isometry, tuple((index,) for index in range(3)))
    physical = physical_isometry(fixture.two_ray_encoding, kraus)
    metrics = menu_metrics(effects)
    expected = tuple(
        fixture.contact.conj().T @ ((2 / 3) * projector) @ fixture.contact
        for projector in projectors
    )
    check(
        "one fixed physical Naimark isometry derives a normalized positive contact-sensitive ternary trine menu",
        np.linalg.norm(isometry.conj().T @ isometry - I2) < TOL
        and np.linalg.norm(physical.conj().T @ physical - I2) < TOL
        and metrics["normalization"] < TOL
        and metrics["minimum_eigenvalue"] > -TOL
        and metrics["maximum_eigenvalue"] < 2 / 3 + TOL
        and max(np.linalg.norm(left - right) for left, right in zip(effects, expected)) < TOL,
        {
            **metrics,
            "logical_isometry": float(np.linalg.norm(isometry.conj().T @ isometry - I2)),
            "physical_isometry": float(np.linalg.norm(physical.conj().T @ physical - I2)),
            "fine_labels": len(kraus),
            "pointer_M2": ceil(log2(3)),
        },
    )

    deleted_kraus = tuple(sqrt(2 / 3) * projector for projector in projectors)
    deleted_effects = derived_effects(
        stack_isometry(deleted_kraus), tuple((index,) for index in range(3))
    )
    deletion_residuals = tuple(
        float(np.linalg.norm(effect - deleted))
        for effect, deleted in zip(effects, deleted_effects)
    )
    check(
        "deleting the actual contact changes every labeled trine effect while leaving a normalized apparatus menu",
        min(deletion_residuals) > 0.17
        and menu_metrics(deleted_effects)["normalization"] < TOL,
        {
            "labeled_effect_residuals": deletion_residuals,
            "important_boundary": "contact deletion changes the menu but does not remove normalization or select an occurrence",
        },
    )
    return kraus, effects


def nonlinear_binary_weight(effect: np.ndarray) -> float:
    sigma0 = (I2 + 0.5 * Z) / 2
    value = float(np.trace(sigma0 @ effect).real)
    return value**3 / (value**3 + (1 - value) ** 3)


def binary_and_ternary_threshold_controls(
    trine_effects: tuple[np.ndarray, ...]
) -> None:
    rng = np.random.default_rng(317)
    complement_residuals = []
    for _ in range(12):
        unitary, _ = np.linalg.qr(
            rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        )
        eigenvalues = np.diag(rng.uniform(0, 1, size=2))
        effect = unitary @ eigenvalues @ unitary.conj().T
        complement_residuals.append(
            abs(
                nonlinear_binary_weight(effect)
                + nonlinear_binary_weight(I2 - effect)
                - 1
            )
        )

    coin_kraus = (I2 / 2, I2 / 2, I2 / sqrt(2))
    coin_effects = derived_effects(
        stack_isometry(coin_kraus), ((0,), (1,), (2,))
    )
    coin_weights = tuple(nonlinear_binary_weight(effect) for effect in coin_effects)
    trine_weights = tuple(nonlinear_binary_weight(effect) for effect in trine_effects)
    check(
        "the PR-5479 smooth non-Born family satisfies every held binary complement but fails physically dilated ternary menus",
        max(complement_residuals) < TOL
        and max(
            np.linalg.norm(effect - scale * I2)
            for effect, scale in zip(coin_effects, (1 / 4, 1 / 4, 1 / 2))
        )
        < TOL
        and abs(sum(coin_weights) - float(Fraction(4, 7))) < TOL
        and abs(sum(trine_weights) - float(Fraction(1, 3))) < TOL,
        {
            "maximum_binary_complement_residual": max(complement_residuals),
            "quarter_coin_non_Born_sum": sum(coin_weights),
            "quarter_coin_exact_target": str(Fraction(4, 7)),
            "contact_trine_non_Born_sum": sum(trine_weights),
            "contact_trine_exact_target": str(Fraction(1, 3)),
        },
    )


def split_projector_isometry(
    projector: np.ndarray,
    splits: tuple[float, ...],
    contact: np.ndarray,
) -> tuple[np.ndarray, tuple[tuple[int, ...], ...]]:
    if any(value < 0 for value in splits) or abs(sum(splits) - 1) > 1e-10:
        raise ValueError("split fractions must be nonnegative and sum to one")
    kraus = tuple(sqrt(value) * projector @ contact for value in splits) + (
        (I2 - projector) @ contact,
    )
    return stack_isometry(kraus), tuple((index,) for index in range(len(kraus)))


def merge_isometry(
    weighted_projectors: tuple[tuple[float, np.ndarray], ...],
    contact: np.ndarray,
) -> tuple[np.ndarray, tuple[tuple[int, ...], ...]]:
    if not weighted_projectors or len(weighted_projectors) > 4:
        raise ValueError("the forcing basis accepts one to four projective components")
    total = sum(weight for weight, _ in weighted_projectors)
    if any(weight < 0 for weight, _ in weighted_projectors) or total > 1 + 1e-10:
        raise ValueError("component weights must be nonnegative with total at most one")
    kraus = []
    plus = []
    minus = []
    for weight, projector in weighted_projectors:
        if (
            projector.shape != (2, 2)
            or np.linalg.norm(projector @ projector - projector) > TOL
            or np.linalg.norm(projector - projector.conj().T) > TOL
        ):
            raise ValueError("each component needs one rank-one projector")
        plus.append(len(kraus))
        kraus.append(sqrt(weight) * projector @ contact)
        minus.append(len(kraus))
        kraus.append(sqrt(weight) * (I2 - projector) @ contact)
    coin = None
    if total < 1 - 1e-12:
        coin = len(kraus)
        kraus.append(sqrt(1 - total) * contact)
    groups = (tuple(plus),) + tuple((index,) for index in minus)
    if coin is not None:
        groups += ((coin,),)
    return stack_isometry(tuple(kraus)), groups


def mixed_projective_forcing_basis_controls(
    fixture: PhysicalFixture,
) -> tuple[tuple[np.ndarray, ...], dict[str, object]]:
    # PR-5479 T3(a): a same-ray three-way split plus the opposite outcome.
    n = np.asarray((2, -3, 6), dtype=float)
    n /= np.linalg.norm(n)
    p = projector_bloch(n)
    ray_isometry, ray_groups = split_projector_isometry(
        p, (0.17, 0.29, 0.54), fixture.contact
    )
    ray_effects = derived_effects(ray_isometry, ray_groups)
    ray_expected = tuple(
        fixture.contact.conj().T @ (scale * p) @ fixture.contact
        for scale in (0.17, 0.29, 0.54)
    ) + (fixture.contact.conj().T @ (I2 - p) @ fixture.contact,)

    # PR-5479 T3(c): the halved axis-cancellation identity.  Its left
    # presentation has at most four components and therefore eight fine
    # labels; the right presentation has two.
    held_directions = (
        np.asarray((1, 2, 3), dtype=float),
        np.asarray((-4, 1, 2), dtype=float),
        np.asarray((3, -5, 1), dtype=float),
    )
    axis_rows = []
    maximum_fine = 0
    retained_kraus: tuple[np.ndarray, ...] = ()
    for direction in held_directions:
        direction /= np.linalg.norm(direction)
        l1 = float(np.sum(np.abs(direction)))
        c0 = 2 / (1 + l1)
        left = [(c0 / 2, projector_bloch(direction))]
        for axis in range(3):
            unit = np.zeros(3)
            unit[axis] = -np.sign(direction[axis])
            left.append((c0 * abs(direction[axis]) / 2, projector_bloch(unit)))
        right_direction = np.asarray((1, -1, 2), dtype=float)
        right_direction /= np.linalg.norm(right_direction)
        right = (
            (0.5, projector_bloch(right_direction)),
            (0.5, projector_bloch(-right_direction)),
        )
        left_iso, left_groups = merge_isometry(tuple(left), fixture.contact)
        right_iso, right_groups = merge_isometry(right, fixture.contact)
        left_effects = derived_effects(left_iso, left_groups)
        right_effects = derived_effects(right_iso, right_groups)
        left_a, right_a = left_effects[0], right_effects[0]
        left_fine = sum(bool(np.linalg.norm(left_iso[2*i:2*(i+1)])) for i in range(8))
        right_fine = sum(bool(np.linalg.norm(right_iso[2*i:2*(i+1)])) for i in range(8))
        maximum_fine = max(maximum_fine, left_fine, right_fine)
        axis_rows.append(
            {
                "left_mass": sum(weight for weight, _ in left),
                "left_fine": left_fine,
                "right_fine": right_fine,
                "left_half_I": float(np.linalg.norm(left_a - I2 / 2)),
                "right_half_I": float(np.linalg.norm(right_a - I2 / 2)),
                "presentation_equality": float(np.linalg.norm(left_a - right_a)),
                "left_normalization": menu_metrics(left_effects)["normalization"],
                "right_normalization": menu_metrics(right_effects)["normalization"],
            }
        )
        retained_kraus = tuple(
            left_iso[2 * index : 2 * (index + 1), :]
            for index in range(8)
            if np.linalg.norm(left_iso[2 * index : 2 * (index + 1), :]) > TOL
        )

    # Every qubit effect has a presentation with at most three components.
    # E=bI+(a-b)P_n, with a>=b, plus a leftover coin of weight 1-a.
    representation_rows = []
    representation_menus = []
    for eigenvalues, direction in (
        ((0.83, 0.21), np.asarray((2, 1, -3), dtype=float)),
        ((0.91, 0.64), np.asarray((-1, 4, 2), dtype=float)),
        ((0.47, 0.02), np.asarray((3, -2, 5), dtype=float)),
    ):
        direction /= np.linalg.norm(direction)
        a, b = eigenvalues
        p_effect = projector_bloch(direction)
        kraus = (
            sqrt(b) * fixture.contact,
            sqrt(a - b) * p_effect @ fixture.contact,
            sqrt(a - b) * (I2 - p_effect) @ fixture.contact,
            sqrt(1 - a) * fixture.contact,
        )
        iso = stack_isometry(kraus)
        effects = derived_effects(iso, ((0, 1), (2, 3)))
        representation_menus.append(effects)
        expected = fixture.contact.conj().T @ (
            b * I2 + (a - b) * p_effect
        ) @ fixture.contact
        representation_rows.append(
            {
                "eigenvalues": eigenvalues,
                "fine_labels": len(kraus),
                "effect_residual": float(np.linalg.norm(effects[0] - expected)),
                "complement_residual": float(np.linalg.norm(effects[1] - (I2 - expected))),
                "normalization": menu_metrics(effects)["normalization"],
            }
        )

    check(
        "the bounded X1^(8) dilation compiler derives the exact ray-split and four-component merge menus used by PR-5479 T3",
        np.linalg.norm(ray_isometry.conj().T @ ray_isometry - I2) < TOL
        and max(np.linalg.norm(left - right) for left, right in zip(ray_effects, ray_expected)) < TOL
        and menu_metrics(ray_effects)["normalization"] < TOL
        and maximum_fine == 8
        and all(
            max(
                row["left_half_I"],
                row["right_half_I"],
                row["presentation_equality"],
                row["left_normalization"],
                row["right_normalization"],
                abs(row["left_mass"] - 1),
            )
            < TOL
            for row in axis_rows
        ),
        {
            "ray_split_effect_residual": max(
                np.linalg.norm(left - right) for left, right in zip(ray_effects, ray_expected)
            ),
            "axis_rows": axis_rows,
            "maximum_fine_labels": maximum_fine,
            "pointer_M2": POINTER_M2,
        },
    )
    check(
        "every held qubit effect is an element of the same bounded mixed-projective dilation domain with at most three components",
        all(
            row["fine_labels"] <= 6
            and max(
                row["effect_residual"],
                row["complement_residual"],
                row["normalization"],
            )
            < TOL
            for row in representation_rows
        ),
        representation_rows,
    )

    # A trace-form candidate satisfies every compiled normalization,
    # refinement, and same-effect identity.  This is a consistency check,
    # not a derivation or selection of the weight functional.
    bloch = np.asarray((0.21, -0.32, 0.41), dtype=float)
    sigma = (I2 + bloch[0] * X + bloch[1] * Y + bloch[2] * Z) / 2

    def born_weight(effect: np.ndarray) -> float:
        return float(np.trace(sigma @ effect).real)

    ray_weights = tuple(born_weight(effect) for effect in ray_effects)
    ray_unsplit = fixture.contact.conj().T @ p @ fixture.contact
    representation_normalizations = tuple(
        abs(sum(born_weight(effect) for effect in menu) - 1)
        for menu in representation_menus
    )
    check(
        "a held Born trace functional satisfies the compiled normalization, ray-refinement, merge, and same-effect identities",
        np.min(np.linalg.eigvalsh(sigma)) > 0
        and abs(sum(ray_weights) - 1) < TOL
        and abs(sum(ray_weights[:3]) - born_weight(ray_unsplit)) < TOL
        and max(representation_normalizations) < TOL
        and all(
            abs(born_weight(I2 / 2) - 0.5) < TOL
            and row["presentation_equality"] < TOL
            for row in axis_rows
        ),
        {
            "sigma_eigenvalues": tuple(float(value) for value in np.linalg.eigvalsh(sigma)),
            "ray_menu_weight_sum": sum(ray_weights),
            "split_plus_minus_unsplit": abs(
                sum(ray_weights[:3]) - born_weight(ray_unsplit)
            ),
            "maximum_held_menu_normalization": max(representation_normalizations),
            "axis_merged_half_I_weight": born_weight(I2 / 2),
            "interpretation": "candidate consistency only; effect functionality and eligibility are not derived",
        },
    )
    return retained_kraus, {
        "ray": ray_effects,
        "axis": axis_rows,
        "representations": representation_rows,
        "forcing_sufficiency": {
            "same_direction_splits": True,
            "coin_refinements": True,
            "projective_complements": True,
            "four_component_axis_identity": True,
            "every_qubit_effect_at_most_three_components": True,
            "maximum_fine_labels": maximum_fine,
        },
    }


def physical_locality_and_covariance_controls(
    fixtures: dict[int, PhysicalFixture],
    route_kraus: dict[str, tuple[np.ndarray, ...]],
) -> None:
    locality_rows = []
    for length, fixture in fixtures.items():
        representatives = tuple(
            c311.branch_representative(
                fixture.code, fixture.encoder.body, branch, r_value
            )
            for r_value in (0, 1)
            for branch in fixture.basis_rows
        )
        pairs = set()
        raw_terms = 0
        for kraus in route_kraus.values():
            for operator in kraus:
                raw = (
                    fixture.two_ray_encoding
                    @ operator
                    @ fixture.two_ray_encoding.conj().T
                )
                current = {
                    (int(row), int(column))
                    for row, column in np.argwhere(abs(raw) > 1e-12)
                }
                pairs.update(current)
                raw_terms += len(current)
        transition_union = 0
        maximum_transition = 0
        constraint_failures = sector_failures = 0
        for row, column in pairs:
            transition = representatives[row] @ c311.local.pauli_dagger(
                representatives[column]
            )
            support = transition.x | transition.z
            transition_union |= support
            maximum_transition = max(maximum_transition, support.bit_count())
            constraint_failures += sum(
                not transition.commutes(c311.c305.constraint_pauli(fixture.code, vertex))
                for vertex in range(len(fixture.code.graph.vertices))
            )
            sector_failures += sum(
                not transition.commutes(row_op)
                for row_op in fixture.code.local_checks + fixture.code.wilsons
            )
        locality_rows.append(
            {
                "L": length,
                "held": length == 6,
                "matrix_unit_pairs": len(pairs),
                "raw_terms_with_repetition": raw_terms,
                "matter_transition_union_M2": transition_union.bit_count(),
                "maximum_matter_transition_M2": maximum_transition,
                "maximum_transition_with_pointer_M2": maximum_transition + POINTER_M2,
                "inherited_port_constraint_failures": constraint_failures,
                "local_check_or_Wilson_failures": sector_failures,
                "installed_Cycle311_patch_M2_upper_bound": 56,
                "installed_apparatus_patch_M2_upper_bound": 56 + POINTER_M2,
                "installed_overhead_M2_per_cell": 23 + POINTER_M2,
            }
        )
    check(
        "every physical dilation block has bounded matrix-unit support, zero inherited leakage, and constant three-M2 pointer overhead through held L=6",
        all(
            row["matrix_unit_pairs"] <= 16
            and row["matter_transition_union_M2"] == 20
            and row["maximum_matter_transition_M2"] <= 20
            and row["maximum_transition_with_pointer_M2"] <= 23
            and row["inherited_port_constraint_failures"] == 0
            and row["local_check_or_Wilson_failures"] == 0
            and row["installed_apparatus_patch_M2_upper_bound"] == 59
            and row["installed_overhead_M2_per_cell"] == 26
            for row in locality_rows
        ),
        locality_rows,
    )

    base = fixtures[3]
    reducer = c311.c305.StabilizerReducer(base.code)
    frame_rows = []
    for frame in c311.c235.proper_cubic_frames():
        logical_r = c311.logical_frame_representation(frame)
        old_r, failures = c311.flagged_frame_representation(
            base.encoder,
            base.basis_rows,
            base.occurrence,
            frame,
            reducer,
        )
        mapping, phases, mapping_failures = c311.signed_mapping(old_r)
        new_mapping = np.concatenate((mapping, mapping + 255))
        new_phases = np.concatenate((phases, phases))
        selected = np.zeros((127, 2), dtype=complex)
        selected[
            [c311.SEAM_INDEX[(2, (0, 1), stream_slice)] for stream_slice in (0, 1)],
            [0, 1],
        ] = 1
        carried_f = base.full_encoding @ logical_r @ selected
        mapped_f = c311.apply_signed_mapping(
            new_mapping, new_phases, base.two_ray_encoding
        )
        contact_commutator = float(
            np.linalg.norm(
                c311.logical_contact(c311.COUPLING) @ logical_r @ selected
                - logical_r @ selected @ base.contact
            )
        )
        apparatus_residual = 0.0
        for kraus in route_kraus.values():
            base_v = physical_isometry(base.two_ray_encoding, kraus)
            carried_v = physical_isometry(carried_f, kraus)
            mapped_blocks = []
            for pointer in range(8):
                block = base_v[510 * pointer : 510 * (pointer + 1), :]
                mapped_blocks.append(
                    c311.apply_signed_mapping(new_mapping, new_phases, block)
                )
            apparatus_residual = max(
                apparatus_residual,
                float(np.linalg.norm(np.vstack(mapped_blocks) - carried_v)),
            )
        frame_rows.append(
            {
                "branch_failures": failures + mapping_failures,
                "code_covariance": float(np.linalg.norm(mapped_f - carried_f)),
                "contact_covariance": contact_commutator,
                "apparatus_covariance": apparatus_residual,
            }
        )
    check(
        "the contact-trine and split/merge dilation families have carried covariance under all 24 proper-cubic frames",
        len(frame_rows) == 24
        and all(
            row["branch_failures"] == 0
            and max(
                row["code_covariance"],
                row["contact_covariance"],
                row["apparatus_covariance"],
            )
            < TOL
            for row in frame_rows
        ),
        {
            "proper_cubic_frames": len(frame_rows),
            "maximum_residuals": {
                key: max(row[key] for row in frame_rows)
                for key in ("code_covariance", "contact_covariance", "apparatus_covariance")
            },
            "branch_failures": sum(row["branch_failures"] for row in frame_rows),
        },
    )


def deletion_domain_and_semantic_controls(
    fixture: PhysicalFixture,
    forcing_kraus: tuple[np.ndarray, ...],
) -> None:
    ideal = stack_isometry(forcing_kraus)
    deleted_kraus = forcing_kraus[:3] + (
        np.zeros((2, 2), dtype=complex),
    ) + forcing_kraus[4:]
    deleted = stack_isometry(deleted_kraus)
    deletion_residual = float(np.linalg.norm(deleted.conj().T @ deleted - I2, 2))
    check(
        "deleting one fine dilation branch creates detected normalization loss rather than a hidden coarse-menu relabeling",
        np.linalg.norm(ideal.conj().T @ ideal - I2) < TOL
        and deletion_residual > 0.05,
        {
            "ideal_isometry_residual": float(np.linalg.norm(ideal.conj().T @ ideal - I2)),
            "deleted_branch_normalization_residual": deletion_residual,
        },
    )

    rejected = 0
    invalid_calls = (
        lambda: projector_bloch(np.asarray((1, 1, 1))),
        lambda: stack_isometry(tuple(I2 for _ in range(9))),
        lambda: split_projector_isometry(projector_bloch(np.asarray((1, 0, 0))), (0.2, 0.3), fixture.contact),
        lambda: merge_isometry(((-0.1, projector_bloch(np.asarray((1, 0, 0)))),), fixture.contact),
        lambda: merge_isometry(tuple((0.3, projector_bloch(np.asarray((1, 0, 0)))) for _ in range(4)), fixture.contact),
    )
    for call in invalid_calls:
        try:
            call()
        except ValueError:
            rejected += 1
    check(
        "the lawful domain rejects malformed Bloch vectors, excess pointer outcomes, bad splits, negative weights, and overweight presentations",
        rejected == len(invalid_calls),
        rejected,
    )

    text = normalized(NOTE)
    check(
        "the semantic firewall keeps dilation, effect, grading, occurrence, actual member, Record, permanence, and frequency distinct",
        "pointer labels are not records" in text
        and "dephasing is not occurrence" in text
        and "conditional born weights are not frequencies" in text
        and "actual member remains open" in text
        and "global additivity remains open" in text
        and "calibration remains open" in text,
        {
            "dilation": "constructed",
            "effect_menu": "derived by pointer compression",
            "effect_functional_weight": "conditional hypothesis",
            "occurrence": None,
            "actual_member": None,
            "Record_formation": None,
            "permanence_application": None,
            "frequency_calibration": None,
        },
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    fixtures = physical_subcode_controls()
    trine_kraus, trine_effects = contact_trine_controls(fixtures[3])
    binary_and_ternary_threshold_controls(trine_effects)
    forcing_kraus, forcing_data = mixed_projective_forcing_basis_controls(fixtures[3])
    physical_locality_and_covariance_controls(
        fixtures,
        {"contact_trine": trine_kraus, "X1_8_axis_merge": forcing_kraus},
    )
    deletion_domain_and_semantic_controls(fixtures[3], forcing_kraus)
    check(
        "Cycle 317 is a constructive physical menu bridge with conditional Born forcing, not a completed Born/Record/history law or axiom-pressure result",
        len(forcing_data["axis"]) == 3
        and all(
            value is True
            for key, value in forcing_data["forcing_sufficiency"].items()
            if key != "maximum_fine_labels"
        )
        and forcing_data["forcing_sufficiency"]["maximum_fine_labels"] == 8
        and "broad gate status: fail / do not ship" in normalized(NOTE)
        and "no axiom pressure" in normalized(NOTE),
    )
    print("DATA forcing_basis", forcing_data)
    print("SUMMARY PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CYCLE317_PHYSICAL_CONTACT_TERNARY_BORN_BRIDGE_GREEN"
        if FAIL == 0
        else "CYCLE317_OPEN",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
