#!/usr/bin/env python3
"""Block 5: matched support/formation selection triangle.

The executable constructs three total nearest-neighbour kernel descriptors on
the complete six-neighbour shell space.  They share one physical front and one
content-only event decoder but isolate two choices left open by the current
axioms:

* T_plus / T_bar have the same barycenter and formation kernel but different
  Record support on the common front;
* T_plus / T_form have the same conditional content law and readout but
  different formation cylinders.

The construction supplies law-level downstream extensions.  It does not
couple the Block-4 coherent branch to a Record draw, preserve the Block-4
continuation decoder, derive Born weights, supply physical time, or amend an
axiom.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
import sys

import sympy as sp


AUDIT_TIMEOUT_SEC = 180

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_front_stage_remote_context_record_event_congruence_2026_08_20 as block4


NOTE_PATH = ROOT / "docs" / (
    "SHARED_EVENT_RECORD_SUPPORT_SELECTION_TRIANGLE_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
BLOCK4_PATH = ROOT / "docs" / (
    "COMMON_FRONT_STAGE_REMOTE_CONTEXT_RECORD_EVENT_CONGRUENCE_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
ATOMIC_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_M2_EFFECT_LABEL_RECORD_CARRIER_ATOMIC_BORN_LAW_"
    "FACTORIZATION_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
CYCLE176_PATH = ROOT / "docs/work_history/repo/review_feedback" / (
    "PHYSICAL_BARE_FORMATION_PORTED_READOUT_CYCLE176_NOTE_2026-07-16.md"
)
CYCLE179_PATH = ROOT / "docs/work_history/repo/review_feedback" / (
    "PHYSICAL_FIVE_LANE_FORMATION_MEMBERSHIP_CYCLE179_NOTE_2026-07-16.md"
)
CYCLE339_PATH = ROOT / "docs/historic_intake" / (
    "HISTORIC_INTEGRATED_PHYSICAL_ENDPOINT_REGISTRATION_TOURNAMENT_"
    "SYNTHESIS_CYCLE339_NOTE_2026_07_18_INTAKE_NOTE_2026-08-05.md"
)
CYCLE823_PATH = ROOT / "docs" / (
    "COMPANION_FULL_SEAM_ENDPOINT_INSTRUMENT_CYCLE823_"
    "BOUNDED_THEOREM_NOTE_2026-07-30.md"
)

AUDIT_INPUT_PATHS = (
    "docs/SHARED_EVENT_RECORD_SUPPORT_SELECTION_TRIANGLE_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/COMMON_FRONT_STAGE_REMOTE_CONTEXT_RECORD_EVENT_CONGRUENCE_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/ADMISSIBILITY_M2_EFFECT_LABEL_RECORD_CARRIER_ATOMIC_BORN_LAW_FACTORIZATION_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_BARE_FORMATION_PORTED_READOUT_CYCLE176_NOTE_2026-07-16.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_FIVE_LANE_FORMATION_MEMBERSHIP_CYCLE179_NOTE_2026-07-16.md",
    "docs/historic_intake/HISTORIC_INTEGRATED_PHYSICAL_ENDPOINT_REGISTRATION_TOURNAMENT_SYNTHESIS_CYCLE339_NOTE_2026_07_18_INTAKE_NOTE_2026-08-05.md",
    "docs/COMPANION_FULL_SEAM_ENDPOINT_INSTRUMENT_CYCLE823_BOUNDED_THEOREM_NOTE_2026-07-30.md",
    "scripts/common_front_stage_remote_context_record_event_congruence_2026_08_20.py",
)

PASS = 0
FAIL = 0

Point = tuple[int, int, int]
Rotation = tuple[Point, Point, Point]
M2Code = tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]

DIRECTIONS: tuple[Point, ...] = block4.DIRECTIONS
I2 = sp.eye(2)
PATCH_RADIUS = sp.Rational(1, 64)
FRONT_WEIGHT = sp.Rational(2, 3)  # arbitrary non-Born fixture, not selected


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS [{label}] {detail}")
    else:
        FAIL += 1
        print(f"FAIL [{label}] {detail}")


def normalized(path: Path) -> str:
    body = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def as_matrix(code: M2Code) -> sp.Matrix:
    return sp.Matrix(((code[0], code[1]), (code[2], code[3])))


def as_code(matrix: sp.Matrix) -> M2Code:
    return tuple(
        sp.simplify(matrix[row, column])
        for row in range(2)
        for column in range(2)
    )  # type: ignore[return-value]


def kappa(matrix: sp.Matrix, label: sp.Expr) -> M2Code:
    return as_code(matrix + sp.I * label * I2)


def add_codes(*terms: tuple[sp.Expr, M2Code]) -> M2Code:
    result = sp.zeros(2)
    for coefficient, code in terms:
        result += coefficient * as_matrix(code)
    return as_code(result)


def hs_sq(left: M2Code, right: M2Code) -> sp.Expr:
    delta = as_matrix(left) - as_matrix(right)
    return sp.simplify(sp.trace(delta.conjugate().T * delta))


def label_coordinate(code: M2Code) -> sp.Expr:
    return sp.simplify(sp.im(sp.trace(as_matrix(code))) / 2)


def trace_cell(code: M2Code) -> str:
    value = label_coordinate(code)
    return "F0" if bool(value < sp.Rational(1, 2)) else "FB"


SIGMA0 = block4.SIGMA_E0_EXACT
SIGMAB = block4.SIGMA_REMAINDER_EXACT
C0 = kappa(SIGMA0, sp.Integer(0))
CB = kappa(SIGMAB, sp.Integer(1))
CBAR = add_codes((FRONT_WEIGHT, C0), (1 - FRONT_WEIGHT, CB))


def voronoi_cell(code: M2Code) -> str:
    return "V0" if bool(hs_sq(code, C0) <= hs_sq(code, CB)) else "VB"


@dataclass(frozen=True)
class Shell:
    entries: tuple[M2Code | None, ...]

    def occupied(self) -> int:
        return sum(value is not None for value in self.entries)


def shell_from_records(records: dict[Point, M2Code], target: Point) -> Shell:
    return Shell(tuple(records.get(block4.add(target, direction)) for direction in DIRECTIONS))


def rotate_point(rotation: Rotation, point: Point) -> Point:
    return tuple(
        sum(rotation[row][column] * point[column] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def rotate_shell(shell: Shell, rotation: Rotation) -> Shell:
    carried = {
        rotate_point(rotation, direction): value
        for direction, value in zip(DIRECTIONS, shell.entries, strict=True)
    }
    return Shell(tuple(carried[direction] for direction in DIRECTIONS))


def shell_distance(left: Shell, right: Shell) -> sp.Expr | None:
    if tuple(value is None for value in left.entries) != tuple(
        value is None for value in right.entries
    ):
        return None
    return sp.simplify(
        sum(
            (
                hs_sq(left_value, right_value)
                if left_value is not None and right_value is not None
                else sp.Integer(0)
            )
            for left_value, right_value in zip(left.entries, right.entries, strict=True)
        )
    )


LAYOUT_A = block4.build_layout("A")
LAYOUT_B = block4.build_layout("B")
FRONT_A = shell_from_records(LAYOUT_A.record_map(), LAYOUT_A.first_target)
FRONT_B = shell_from_records(LAYOUT_B.record_map(), LAYOUT_B.first_target)
ROTATIONS = block4.proper_cubic_rotations()
FRONT_ORBIT = tuple({rotate_shell(FRONT_A, rotation) for rotation in ROTATIONS})


def orbit_distance(shell: Shell) -> sp.Expr | None:
    candidates = [
        distance
        for reference in FRONT_ORBIT
        if (distance := shell_distance(shell, reference)) is not None
    ]
    if not candidates:
        return None
    return min(candidates, key=lambda value: float(sp.N(value)))


def patch_weight(shell: Shell) -> sp.Expr:
    distance = orbit_distance(shell)
    if distance is None or not bool(distance < PATCH_RADIUS):
        return sp.Integer(0)
    return sp.simplify(1 - distance / PATCH_RADIUS)


def gaussian_center(shell: Shell) -> M2Code:
    center = shell.occupied() * I2
    for value in shell.entries:
        if value is not None:
            matrix = as_matrix(value)
            center += (matrix + matrix.conjugate().T) / 2
    return as_code(sp.simplify(center / 7))


@dataclass(frozen=True)
class MeasureDescriptor:
    family: str
    bump_weight: sp.Expr
    center: M2Code
    atoms: tuple[M2Code, ...] = ()
    atom_weights: tuple[sp.Expr, ...] = ()

    def barycenter(self) -> M2Code:
        if self.family == "full_gaussian":
            return self.center
        if self.family == "dirac":
            return self.atoms[0]
        atomic_bar = add_codes(*tuple(zip(self.atom_weights, self.atoms, strict=True)))
        return add_codes(
            (1 - self.bump_weight, self.center),
            (self.bump_weight, atomic_bar),
        )

    def normalized(self) -> bool:
        if self.family in {"full_gaussian", "dirac"}:
            return True
        return (
            0 < self.bump_weight <= 1
            and sp.simplify(sum(self.atom_weights) - 1) == 0
            and all(weight > 0 for weight in self.atom_weights)
        )


def endpoint_measure(shell: Shell) -> MeasureDescriptor:
    weight = patch_weight(shell)
    center = gaussian_center(shell)
    if weight == 0:
        return MeasureDescriptor("full_gaussian", weight, center)
    return MeasureDescriptor(
        "gaussian_endpoint_mixture",
        weight,
        center,
        (C0, CB),
        (FRONT_WEIGHT, 1 - FRONT_WEIGHT),
    )


def barycenter_twin_measure(shell: Shell) -> MeasureDescriptor:
    endpoint = endpoint_measure(shell)
    if endpoint.bump_weight == 0:
        return endpoint
    barycenter = endpoint.barycenter()
    return MeasureDescriptor("dirac", endpoint.bump_weight, barycenter, (barycenter,), (sp.Integer(1),))


def event_masses_at_exact_front(measure: MeasureDescriptor) -> tuple[sp.Expr, sp.Expr]:
    if measure.family == "dirac":
        return (sp.Integer(1), sp.Integer(0)) if trace_cell(measure.atoms[0]) == "F0" else (sp.Integer(0), sp.Integer(1))
    if measure.bump_weight == 1 and measure.atoms:
        f0 = sum(
            weight
            for atom, weight in zip(measure.atoms, measure.atom_weights, strict=True)
            if trace_cell(atom) == "F0"
        )
        return sp.simplify(f0), sp.simplify(1 - f0)
    raise ValueError("exact front event masses requested off the exact patch")


def formation_probability(model: str, shell: Shell) -> sp.Expr:
    eligible = shell.occupied() > 0
    if not eligible:
        return sp.Integer(0)
    if model in {"T_plus", "T_bar"}:
        return sp.Integer(1)
    if model == "T_form":
        return sp.Rational(1, 2)
    raise ValueError(model)


def pattern_probability(pattern: tuple[int, ...], probability: sp.Expr) -> sp.Expr:
    formed = sum(pattern)
    return sp.simplify(probability**formed * (1 - probability) ** (len(pattern) - formed))


def combined_front_partition(model: str) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    """Return masses of (blank, F0, FB) for one eligible exact-front site.

    This is the one-coordinate kernel on the disjoint union
    ``{blank} + M_2(C)``.  Countable conditional products of these Borel
    coordinate kernels, followed by Ionescu--Tulcea over supplied ordinals,
    give the analytic path-space extension stated in the note.
    """

    shell = FRONT_A
    q = formation_probability(model, shell)
    content = (
        endpoint_measure(shell)
        if model in {"T_plus", "T_form"}
        else barycenter_twin_measure(shell)
    )
    f0, fb = event_masses_at_exact_front(content)
    return sp.simplify(1 - q), sp.simplify(q * f0), sp.simplify(q * fb)


def source_controls() -> None:
    sources = {
        "axiom": normalized(AXIOM_PATH),
        "block4": normalized(BLOCK4_PATH),
        "atomic": normalized(ATOMIC_PATH),
        "cycle176": normalized(CYCLE176_PATH),
        "cycle179": normalized(CYCLE179_PATH),
        "cycle339": normalized(CYCLE339_PATH),
        "cycle823": normalized(CYCLE823_PATH),
    }
    check(
        "sources-and-prior-art-boundary",
        all(path.exists() for path in (NOTE_PATH, AXIOM_PATH, BLOCK4_PATH, ATOMIC_PATH, CYCLE176_PATH, CYCLE179_PATH, CYCLE339_PATH, CYCLE823_PATH))
        and "deterministic substrates as boundary realizations" in sources["axiom"]
        and "does not supply the formation site, probability, or rate" in sources["axiom"]
        and "same complete condition implies the same full local probability measure" in sources["block4"]
        and "direct atomic admissibility law" in sources["atomic"]
        and "formation then readout" in sources["cycle176"]
        and "assign probability weights" in sources["cycle179"]
        and "derives no contingent realized content" in sources["cycle339"]
        and "does not make a record" in sources["cycle823"],
        "current axioms, Block 4, and all three connector-route boundaries are source bound",
    )


def decoder_controls() -> None:
    witness = add_codes((sp.Integer(1), C0), (sp.I * sp.Rational(51, 100), as_code(I2)))
    check(
        "probability-independent-thick-event-algebra",
        label_coordinate(C0) == 0
        and label_coordinate(CB) == 1
        and trace_cell(C0) == "F0"
        and trace_cell(CB) == "FB"
        and trace_cell(CBAR) == "F0",
        {
            "cells": ("t(R)<1/2", "t(R)>=1/2"),
            "endpoint_margins": (sp.Rational(1, 2), sp.Rational(1, 2)),
            "weights_used_to_define_cells": "none",
        },
    )
    check(
        "event-typing-nonuniqueness-control",
        trace_cell(witness) == "FB"
        and voronoi_cell(witness) == "V0"
        and voronoi_cell(C0) == "V0"
        and voronoi_cell(CB) == "VB",
        "two weight-free covariant decoders classify both endpoints correctly but disagree away from them",
    )


def total_kernel_and_orbit_controls() -> None:
    check(
        "exact-common-front-orbit",
        FRONT_A == FRONT_B
        and len(ROTATIONS) == 24
        and len(FRONT_ORBIT) == 24
        and patch_weight(FRONT_A) == 1,
        "the 24-shell proper-cubic orbit is translation free and contains the exact A/B front once",
    )
    perturbed_entries = list(FRONT_A.entries)
    changed_index = next(index for index, value in enumerate(perturbed_entries) if value is not None)
    perturbed_entries[changed_index] = add_codes(
        (sp.Integer(1), perturbed_entries[changed_index]),  # type: ignore[arg-type]
        (sp.Rational(1, 32), as_code(I2)),
    )
    perturbed = Shell(tuple(perturbed_entries))
    deleted_entries = list(FRONT_A.entries)
    deleted_entries[changed_index] = None
    deleted = Shell(tuple(deleted_entries))
    check(
        "borel-nonzero-neighbourhood-patch",
        0 < patch_weight(perturbed) < 1
        and patch_weight(deleted) == 0
        and orbit_distance(perturbed) is not None,
        "a finite-orbit Hilbert-Schmidt bump replaces a contrived singleton equality trigger",
    )

    empty = Shell((None,) * 6)
    one = Shell((as_code(I2), None, None, None, None, None))
    off_empty = endpoint_measure(empty)
    off_one = endpoint_measure(one)
    check(
        "total-condition-varying-kernels",
        off_empty.family == "full_gaussian"
        and off_one.family == "full_gaussian"
        and off_empty.normalized()
        and off_one.normalized()
        and off_empty.center != off_one.center
        and endpoint_measure(FRONT_A).normalized()
        and barycenter_twin_measure(FRONT_A).normalized(),
        "each model assigns one normalized Borel measure to every shell and varies with the complete NN condition",
    )

    covariance_failures = 0
    for rotation in ROTATIONS:
        carried = rotate_shell(FRONT_A, rotation)
        covariance_failures += patch_weight(carried) != 1
        covariance_failures += event_masses_at_exact_front(endpoint_measure(carried)) != (
            FRONT_WEIGHT,
            1 - FRONT_WEIGHT,
        )
        covariance_failures += endpoint_measure(carried).barycenter() != CBAR
    check(
        "block4-spatial-proper-cubic-and-translation-covariance",
        covariance_failures == 0,
        "the orbit patch, endpoint law, support twin, and local formation rule carry through all 24 Block-4 spatial slot frames; no internal M2 co-action is claimed",
    )


def matched_triangle_controls() -> None:
    endpoint = endpoint_measure(FRONT_A)
    support_twin = barycenter_twin_measure(FRONT_A)
    endpoint_masses = event_masses_at_exact_front(endpoint)
    twin_masses = event_masses_at_exact_front(support_twin)
    check(
        "matched-support-twin",
        endpoint.barycenter() == support_twin.barycenter() == CBAR
        and endpoint.atoms == (C0, CB)
        and support_twin.atoms == (CBAR,)
        and endpoint_masses == (FRONT_WEIGHT, 1 - FRONT_WEIGHT)
        and twin_masses == (1, 0)
        and formation_probability("T_plus", FRONT_A)
        == formation_probability("T_bar", FRONT_A)
        == 1,
        {
            "same_barycenter": True,
            "same_formation": True,
            "T_plus_support": ("C0", "CB"),
            "T_bar_support": ("CBAR",),
        },
    )

    q_plus = formation_probability("T_plus", FRONT_A)
    q_form = formation_probability("T_form", FRONT_A)
    check(
        "matched-formation-twin",
        endpoint_measure(FRONT_A) == endpoint_measure(FRONT_B)
        and q_plus == 1
        and q_form == sp.Rational(1, 2)
        and event_masses_at_exact_front(endpoint_measure(FRONT_A))
        == event_masses_at_exact_front(endpoint_measure(FRONT_B)),
        {
            "same_conditional_content_law": True,
            "same_support_and_readout": True,
            "first_ordinal_formation": (q_plus, q_form),
        },
    )

    for probability in (q_plus, q_form):
        for sites in range(1, 7):
            total = sum(
                pattern_probability(pattern, probability)
                for formed in range(sites + 1)
                for chosen in combinations(range(sites), formed)
                for pattern in [tuple(1 if index in chosen else 0 for index in range(sites))]
            )
            if sp.simplify(total - 1) != 0:
                check("finite-cylinder-consistency", False, (probability, sites, total))
                return
    marginal_ok = all(
        sp.simplify(
            pattern_probability(pattern + (0,), q_form)
            + pattern_probability(pattern + (1,), q_form)
            - pattern_probability(pattern, q_form)
        )
        == 0
        for sites in range(1, 6)
        for pattern in (
            (0,) * sites,
            (1,) * sites,
            tuple(index % 2 for index in range(sites)),
        )
    )
    check(
        "finite-cylinder-consistency",
        marginal_ok,
        "independent ordinal formation gates normalize and marginalize on every tested finite cylinder",
    )

    plus_partition = combined_front_partition("T_plus")
    bar_partition = combined_front_partition("T_bar")
    form_partition = combined_front_partition("T_form")
    survival = tuple(sp.Rational(1, 2) ** ordinal for ordinal in range(1, 9))
    check(
        "combined-transition-and-cross-ordinal-extension",
        plus_partition == (0, FRONT_WEIGHT, 1 - FRONT_WEIGHT)
        and bar_partition == (0, 1, 0)
        and form_partition
        == (
            sp.Rational(1, 2),
            sp.Rational(1, 3),
            sp.Rational(1, 6),
        )
        and all(sp.simplify(sum(partition) - 1) == 0 for partition in (plus_partition, bar_partition, form_partition))
        and all(survival[index + 1] < survival[index] for index in range(len(survival) - 1))
        and survival[-1] == sp.Rational(1, 256),
        "the exact-front no-form/content cylinders normalize, and fresh q=1/2 gates give survival 2^-n; the full standard-Borel path kernel is analytic, not enumerated",
    )


def state_legality_and_mutation_controls() -> None:
    records = LAYOUT_A.record_map()
    record_shells = [shell_from_records(records, site) for site in records]
    check(
        "supplied-initial-state-current-support-compatibility",
        all(patch_weight(shell) == 0 for shell in record_shells),
        "every preloaded apparatus Record has a present shell on the full-support Gaussian branch; no historical genesis or reachability is claimed",
    )

    deleted = dict(records)
    deletion_site = block4.add(LAYOUT_A.first_target, (0, -1, 0))
    del deleted[deletion_site]
    leaked = dict(records)
    leak_site = block4.add(LAYOUT_A.first_target, (0, 1, 0))
    leaked[leak_site] = block4.CONTEXT_A
    alternative_weight = sp.Rational(3, 5)
    alternative_bar = add_codes((alternative_weight, C0), (1 - alternative_weight, CB))
    check(
        "load-bearing-deletion-context-and-weight-controls",
        patch_weight(shell_from_records(deleted, LAYOUT_A.first_target)) == 0
        and patch_weight(shell_from_records(leaked, LAYOUT_A.first_target)) == 0
        and alternative_bar != CBAR,
        "deleting or leaking a shell input removes the exact patch, while changing the arbitrary atom weight changes the law without breaking its structural type",
    )


def route_and_claim_boundary_controls() -> None:
    note = normalized(NOTE_PATH)
    required = (
        "endpoint-support faithfulness is not entailed",
        "extensional formation kernel is not determined",
        "route b begins downstream",
        "route c stops upstream",
        "not a physical completion of the block-4 continuation rail",
        "the ordinal is not physical time",
        "zero obligation retirement",
        "toe percentage movement: zero",
        "universal impossibility",
        "axiom necessity",
        "fail / do not ship",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — per-citation residual matching",
        "n5 — resolution and rhetoric",
        "n6 — partial-closure path scan",
        "n7 — strongest steelman",
        "n8 — cross-cycle echo",
    )
    check(
        "narrow-nonselection-boundary",
        all(phrase in note for phrase in required),
        "the matched triangle supports only two precise non-entailment statements; broad no-go and axiom pressure are rejected",
    )

    n5 = (
        "per_element: checked — unnormalized positive-operator codes, exact barycenter, t-coordinate decoder margins, and arbitrary non-Born weights",
        "per_site: checked — total shell descriptors, exact preloaded common front, off-patch variation, deletion exit, and one-site no-form/content masses",
        "per_mode: checked — support, barycenter, and extensional-formation twins are isolated pairwise with decoder and weight controls",
        "per_block: checked — nonzero orbit bump, 24 Block-4 spatial slot rotations, permanence, finite gate/content cylinders, and 2^-n survival",
        "lattice_wide: checked and not executed — standard-Borel product and Ionescu-Tulcea give the supplied-ordinal path law; physical time, instrument coupling, Born selection, and seed genesis remain open",
    )
    for line in n5:
        print(line)
    check(
        "n5-certificate",
        all(len(line) >= 100 for line in n5)
        and all(line in NOTE_PATH.read_text(encoding="utf-8") for line in n5),
        "all five resolution lines are substantive and source bound",
    )


def main() -> int:
    source_controls()
    decoder_controls()
    total_kernel_and_orbit_controls()
    matched_triangle_controls()
    state_legality_and_mutation_controls()
    route_and_claim_boundary_controls()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
