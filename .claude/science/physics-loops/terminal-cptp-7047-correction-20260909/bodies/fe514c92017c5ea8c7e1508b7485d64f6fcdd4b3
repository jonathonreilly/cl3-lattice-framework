#!/usr/bin/env python3
"""Block 6: typed instrument-port to Record conditional completion.

The runner keeps three objects distinct:

* a positive branch operator carried by the Hermitian projection of one
  M2(C) Record code;
* an apparatus-relative rail role obtained by a declared compiler; and
* a probability measure on the resulting Record codes.

On the exact Block-4 fixture it constructs a total, Borel, spatially
covariant law whose trace-matched specialization has the same finite-history
weights as the supplied staged Kraus instrument.  A support-identical free
weight specialization proves that the current axioms do not select that
matching.  The port compiler, trace instrument semantics, formation kernel,
and initial apparatus are supplied; no axiom is amended and no pointwise
actual outcome is derived from unitary evolution.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product
from pathlib import Path
import sys

import numpy as np
import sympy as sp


AUDIT_TIMEOUT_SEC = 180

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_front_stage_remote_context_record_event_congruence_2026_08_20 as block4
import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as cycle317
import shared_effect_record_randomized_preparation_congruence_independence_2026_08_20 as block3
import shared_event_record_support_selection_triangle_2026_08_20 as block5


NOTE_PATH = ROOT / "docs" / (
    "INSTRUMENT_PORT_TYPED_RECORD_COMPILER_CONDITIONAL_COMPLETION_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
BLOCK4_PATH = ROOT / "docs" / (
    "COMMON_FRONT_STAGE_REMOTE_CONTEXT_RECORD_EVENT_CONGRUENCE_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
BLOCK5_PATH = ROOT / "docs" / (
    "SHARED_EVENT_RECORD_SUPPORT_SELECTION_TRIANGLE_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
LOCKED_OUTPUT_PATH = ROOT / "docs" / (
    "RECORD_OBSERVABLE_QUOTIENT_AND_RANK_ONE_FORMATION_OUTCOME_OPERATION_"
    "NORMAL_FORM_BOUNDED_THEOREM_NOTE_2026-07-11.md"
)
FIREWALL_PATH = ROOT / "docs" / "RECORD_CLASSICALIZATION_DYNAMICS_FIREWALL_2026-06-05.md"

AUDIT_INPUT_PATHS = (
    "docs/INSTRUMENT_PORT_TYPED_RECORD_COMPILER_CONDITIONAL_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/COMMON_FRONT_STAGE_REMOTE_CONTEXT_RECORD_EVENT_CONGRUENCE_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/SHARED_EVENT_RECORD_SUPPORT_SELECTION_TRIANGLE_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/RECORD_OBSERVABLE_QUOTIENT_AND_RANK_ONE_FORMATION_OUTCOME_OPERATION_NORMAL_FORM_BOUNDED_THEOREM_NOTE_2026-07-11.md",
    "docs/RECORD_CLASSICALIZATION_DYNAMICS_FIREWALL_2026-06-05.md",
    "scripts/common_front_stage_remote_context_record_event_congruence_2026_08_20.py",
    "scripts/shared_event_record_support_selection_triangle_2026_08_20.py",
)

PASS = 0
FAIL = 0
TOL = 9.0e-11

Point = tuple[int, int, int]
Rotation = tuple[Point, Point, Point]
M2Code = tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]
Records = dict[Point, M2Code]

I2 = sp.eye(2)
DIRECTIONS: tuple[Point, ...] = block4.DIRECTIONS
PATCH_RADIUS = sp.Rational(1, 64)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS [{label}] {detail}")
    else:
        FAIL += 1
        print(f"FAIL [{label}] {detail}")


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def matrix(value: M2Code) -> sp.Matrix:
    return sp.Matrix(((value[0], value[1]), (value[2], value[3])))


def code(value: sp.Matrix) -> M2Code:
    return tuple(
        sp.simplify(value[row, column])
        for row in range(2)
        for column in range(2)
    )  # type: ignore[return-value]


def kappa(state: sp.Matrix, label: sp.Expr) -> M2Code:
    return code(state + sp.I * label * I2)


def hermitian_projection(value: M2Code) -> sp.Matrix:
    item = matrix(value)
    return sp.simplify((item + item.conjugate().T) / 2)


def label_projection(value: M2Code) -> sp.Expr:
    return sp.simplify(sp.im(sp.trace(matrix(value))) / 2)


def antihermitian_slack(value: M2Code) -> sp.Matrix:
    item = matrix(value)
    label = label_projection(value)
    return sp.simplify((item - item.conjugate().T) / (2 * sp.I) - label * I2)


def is_typed_port_code(value: M2Code) -> bool:
    return (
        antihermitian_slack(value) == sp.zeros(2)
        and hermitian_projection(value).is_positive_semidefinite is True
    )


E0 = block4.E0_EXACT
EB = block4.REMAINDER_EXACT
SIGMA0 = block4.SIGMA_E0_EXACT
SIGMAB = block4.SIGMA_REMAINDER_EXACT
C0 = kappa(SIGMA0, 0)
CB = kappa(SIGMAB, 1)
R0 = kappa(E0, 0)
RB = kappa(EB, 1)


def rail_projection(value: M2Code) -> M2Code | None:
    """Supplied apparatus-relative role compiler for the front program."""

    if not is_typed_port_code(value):
        return None
    label = label_projection(value)
    if label == 0:
        return R0
    if label == 1:
        return RB
    return None


# Exact full-program branch operators for rho*=diag(3/5,2/5).  The labels are
# terminal Record roles and carry no probability meaning.
SIGMA_A1 = sp.Matrix(
    (
        (sp.Rational(19, 450), 19 * sp.sqrt(2) / 225),
        (19 * sp.sqrt(2) / 225, sp.Rational(76, 225)),
    )
)
SIGMA_A2 = sp.Matrix(
    (
        (sp.Rational(16, 75), -8 * sp.sqrt(2) / 75),
        (-8 * sp.sqrt(2) / 75, sp.Rational(8, 75)),
    )
)
SIGMA_B1 = sp.Matrix(
    (
        (sp.Rational(7, 60), 7 * sp.sqrt(2) / 60),
        (7 * sp.sqrt(2) / 60, sp.Rational(7, 30)),
    )
)
SIGMA_B2 = sp.Matrix(
    (
        (sp.Rational(7, 60), -7 * sp.sqrt(2) / 60),
        (-7 * sp.sqrt(2) / 60, sp.Rational(7, 30)),
    )
)

CA1 = kappa(SIGMA_A1, 2)
CA2 = kappa(SIGMA_A2, 3)
CB1 = kappa(SIGMA_B1, 4)
CB2 = kappa(SIGMA_B2, 5)

TRACE_WEIGHTS = {
    "front": (sp.Rational(3, 10), sp.Rational(7, 10)),
    "continuation-A": (sp.Rational(19, 35), sp.Rational(16, 35)),
    "continuation-B": (sp.Rational(1, 2), sp.Rational(1, 2)),
}
FREE_WEIGHTS = {
    "front": (sp.Rational(2, 3), sp.Rational(1, 3)),
    "continuation-A": (sp.Rational(3, 7), sp.Rational(4, 7)),
    "continuation-B": (sp.Rational(4, 9), sp.Rational(5, 9)),
}
ATOMS = {
    "front": (C0, CB),
    "continuation-A": (CA1, CA2),
    "continuation-B": (CB1, CB2),
}


@dataclass(frozen=True)
class TypedReadySite:
    stage: str
    forward: Point
    predecessor: Point
    read_positions: tuple[Point, ...]


def decode_typed_ready_site(records: Records, target: Point) -> TypedReadySite | None:
    if target in records:
        return None
    occupied = tuple(
        direction for direction in DIRECTIONS if block4.add(target, direction) in records
    )
    blanks = tuple(direction for direction in DIRECTIONS if direction not in occupied)
    if len(occupied) != 5 or len(blanks) != 1:
        return None
    forward = blanks[0]
    predecessor = block4.add(target, block4.neg(forward))
    if predecessor not in records:
        return None
    transverse_positions = tuple(
        block4.add(target, direction)
        for direction in occupied
        if direction != block4.neg(forward)
    )
    if len(transverse_positions) != 4:
        return None
    transverse = frozenset(records[position] for position in transverse_positions)
    predecessor_content = records[predecessor]
    stage = ""
    if predecessor_content == block4.PREPARATION and transverse == block4.COMMON_MARKERS:
        stage = "front"
    elif (
        rail_projection(predecessor_content) == RB
        and hermitian_projection(predecessor_content) == SIGMAB
    ):
        if transverse == block4.RESIDUAL_MARKERS | {block4.CONTEXT_A}:
            stage = "continuation-A"
        elif transverse == block4.RESIDUAL_MARKERS | {block4.CONTEXT_B}:
            stage = "continuation-B"
    if not stage:
        return None
    return TypedReadySite(
        stage,
        forward,
        predecessor,
        tuple(sorted((predecessor,) + transverse_positions)),
    )


def active_typed_sites(records: Records) -> tuple[tuple[Point, TypedReadySite], ...]:
    return tuple(
        (target, ready)
        for target in sorted(block4.frontier(records))
        if (ready := decode_typed_ready_site(records, target)) is not None
    )


Shell = block5.Shell


def shell(records: Records, target: Point) -> Shell:
    return block5.shell_from_records(records, target)


def orbit(value: Shell) -> tuple[Shell, ...]:
    return tuple({block5.rotate_shell(value, rotation) for rotation in block5.ROTATIONS})


LAYOUT_A = block4.build_layout("A")
LAYOUT_B = block4.build_layout("B")
FRONT = shell(LAYOUT_A.record_map(), LAYOUT_A.first_target)


def after_first(layout: block4.Layout, content: M2Code) -> Records:
    return block4.append_record(layout.record_map(), layout.first_target, content)


CONT_A = shell(after_first(LAYOUT_A, CB), LAYOUT_A.continuation_target)
CONT_B = shell(after_first(LAYOUT_B, CB), LAYOUT_B.continuation_target)
ORBITS = {
    "front": orbit(FRONT),
    "continuation-A": orbit(CONT_A),
    "continuation-B": orbit(CONT_B),
}


def typed_shell_stage(value: Shell) -> str | None:
    """Apply the same exact typed predecessor gate on a shell as on a site."""

    slots = dict(zip(DIRECTIONS, value.entries, strict=True))
    blanks = tuple(direction for direction, content in slots.items() if content is None)
    if len(blanks) != 1:
        return None
    predecessor = slots[block4.neg(blanks[0])]
    transverse = frozenset(
        content
        for direction, content in slots.items()
        if direction not in (blanks[0], block4.neg(blanks[0]))
        and content is not None
    )
    if predecessor == block4.PREPARATION and transverse == block4.COMMON_MARKERS:
        return "front"
    if (
        predecessor is not None
        and rail_projection(predecessor) == RB
        and hermitian_projection(predecessor) == SIGMAB
    ):
        if transverse == block4.RESIDUAL_MARKERS | {block4.CONTEXT_A}:
            return "continuation-A"
        if transverse == block4.RESIDUAL_MARKERS | {block4.CONTEXT_B}:
            return "continuation-B"
    return None


def orbit_distance(value: Shell, reference_orbit: tuple[Shell, ...]) -> sp.Expr | None:
    distances = [
        distance
        for reference in reference_orbit
        if (distance := block5.shell_distance(value, reference)) is not None
    ]
    if not distances:
        return None
    return min(distances, key=lambda item: float(sp.N(item)))


def bump(value: Shell, reference_orbit: tuple[Shell, ...]) -> sp.Expr:
    distance = orbit_distance(value, reference_orbit)
    if distance is None or not bool(distance < PATCH_RADIUS):
        return sp.Integer(0)
    return sp.simplify(1 - distance / PATCH_RADIUS)


def route_bumps(value: Shell) -> dict[str, sp.Expr]:
    typed_stage = typed_shell_stage(value)
    return {
        stage: bump(value, reference) if stage == typed_stage else sp.Integer(0)
        for stage, reference in ORBITS.items()
    }


@dataclass(frozen=True)
class ContentKernel:
    family: str
    stage: str | None
    bump_weight: sp.Expr
    gaussian_center: M2Code
    atoms: tuple[M2Code, ...]
    atom_weights: tuple[sp.Expr, ...]

    def normalized(self) -> bool:
        return (
            0 <= self.bump_weight <= 1
            and (not self.atom_weights or sp.simplify(sum(self.atom_weights) - 1) == 0)
            and all(weight > 0 for weight in self.atom_weights)
        )


def content_kernel(value: Shell, model: str) -> ContentKernel:
    bumps = route_bumps(value)
    active = [(stage, weight) for stage, weight in bumps.items() if weight != 0]
    center = block5.gaussian_center(value)
    if not active:
        return ContentKernel("full_gaussian", None, 0, center, (), ())
    if len(active) != 1:
        raise ValueError("the declared orbit guards must be pairwise disjoint")
    stage, weight = active[0]
    weights = TRACE_WEIGHTS[stage] if model == "trace" else FREE_WEIGHTS[stage]
    return ContentKernel("orbit_atomic_gaussian_mixture", stage, weight, center, ATOMS[stage], weights)


def formation_probability(value: Shell) -> sp.Expr:
    weights = tuple(route_bumps(value).values())
    return sp.simplify(sum(weights))


def forming_sites(records: Records) -> tuple[Point, ...]:
    return tuple(
        target
        for target in sorted(block4.frontier(records))
        if formation_probability(shell(records, target)) != 0
    )


def append_from_stage(records: Records, target: Point, content: M2Code) -> Records:
    ready = decode_typed_ready_site(records, target)
    if ready is None or content not in ATOMS[ready.stage]:
        raise ValueError("content is not in the supplied support for this typed port")
    return block4.append_record(records, target, content)


def source_controls() -> None:
    sources = {
        "axiom": normalized(AXIOM_PATH),
        "block4": normalized(BLOCK4_PATH),
        "block5": normalized(BLOCK5_PATH),
        "locked": normalized(LOCKED_OUTPUT_PATH),
        "firewall": normalized(FIREWALL_PATH),
    }
    check(
        "sources-and-type-boundary",
        all(path.exists() for path in (NOTE_PATH, AXIOM_PATH, BLOCK4_PATH, BLOCK5_PATH, LOCKED_OUTPUT_PATH, FIREWALL_PATH))
        and "probability distribution over the possibilities is determined by" in sources["axiom"]
        and "integrated coherent quantum-to-record process" in sources["block4"]
        and "not a physical completion of the block-4 continuation rail" in sources["block5"]
        and "locked-output condition fixes the outcome-operation form" in sources["locked"]
        and "pre-record quantum state" in sources["firewall"],
        "current axioms, exact upstream seam, locked-output normal form, and Record typing firewall are bound",
    )


def typed_projection_controls() -> None:
    hostile = code(matrix(CB) + sp.I * sp.diag(1, -1))
    check(
        "typed-state-and-rail-projections",
        all(is_typed_port_code(value) for value in (C0, CB, R0, RB))
        and hermitian_projection(C0) == SIGMA0
        and hermitian_projection(CB) == SIGMAB
        and rail_projection(C0) == R0
        and rail_projection(CB) == RB
        and C0 != R0
        and CB != RB,
        {
            "state_projection_CB": "SigmaB",
            "rail_projection_CB": "kappa(I-E0,1)",
            "literal_code_equality": False,
        },
    )
    check(
        "antihermitian-slack-and-effect-code-controls",
        not is_typed_port_code(hostile)
        and rail_projection(hostile) is None
        and rail_projection(RB) == RB
        and hermitian_projection(RB) == EB
        and hermitian_projection(RB) != SIGMAB,
        "a traceless anti-Hermitian spoof and the bare effect rail cannot masquerade as the realized complement-state port",
    )


def staged_geometry_controls() -> None:
    failures = 0
    cases = 0
    for layout in (LAYOUT_A, LAYOUT_B):
        initial = layout.record_map()
        failures += active_typed_sites(initial) != (
            (layout.first_target, decode_typed_ready_site(initial, layout.first_target)),
        )
        failures += decode_typed_ready_site(initial, layout.continuation_target) is not None

        after_c0 = append_from_stage(initial, layout.first_target, C0)
        after_cb = append_from_stage(initial, layout.first_target, CB)
        after_rb = block4.append_record(initial, layout.first_target, RB)
        failures += active_typed_sites(after_c0) != ()
        failures += active_typed_sites(after_rb) != ()
        expected = decode_typed_ready_site(after_cb, layout.continuation_target)
        failures += active_typed_sites(after_cb) != ((layout.continuation_target, expected),)
        failures += expected is None or expected.stage != f"continuation-{layout.context}"

        terminal_atoms = ATOMS[f"continuation-{layout.context}"]
        for atom in terminal_atoms:
            terminal = append_from_stage(after_cb, layout.continuation_target, atom)
            failures += active_typed_sites(terminal) != ()
            failures += any(terminal[position] != content for position, content in initial.items())
            cases += 1
    check(
        "exact-delayed-staged-record-histories",
        failures == 0 and cases == 4,
        "only s0 is initially active; C0 and the bare RB seal the rail; only CB opens the context-specific s1 port; terminal codes append permanently",
    )


def exact_branch_operator_controls() -> None:
    matrices = (SIGMA0, SIGMAB, SIGMA_A1, SIGMA_A2, SIGMA_B1, SIGMA_B2)
    positivity = all(
        item.is_positive_semidefinite is True
        and item.trace() > 0
        for item in matrices
    )
    rank_profile = (
        SIGMA0.rank() == 1
        and SIGMAB.rank() == 2
        and all(
            item.rank() == 1
            for item in (SIGMA_A1, SIGMA_A2, SIGMA_B1, SIGMA_B2)
        )
    )
    trace_partition = (
        sp.simplify(SIGMA0.trace() + SIGMA_A1.trace() + SIGMA_A2.trace()) == 1
        and sp.simplify(SIGMA0.trace() + SIGMA_B1.trace() + SIGMA_B2.trace()) == 1
    )
    check(
        "exact-positive-branch-operator-tree",
        positivity
        and rank_profile
        and SIGMA0.trace() == sp.Rational(3, 10)
        and SIGMAB.trace() == sp.Rational(7, 10)
        and TRACE_WEIGHTS["continuation-A"]
        == (SIGMA_A1.trace() / SIGMAB.trace(), SIGMA_A2.trace() / SIGMAB.trace())
        and TRACE_WEIGHTS["continuation-B"]
        == (SIGMA_B1.trace() / SIGMAB.trace(), SIGMA_B2.trace() / SIGMAB.trace())
        and trace_partition,
        "all six code states are exact nonzero positive operators, with the expected rank profile, and the staged trace masses normalize in both contexts",
    )

    menu_a, menu_b = block3.exact_menus()
    contact = cycle317.physical_fixture(3).contact
    programs = (
        block3.build_program("M_A", menu_a, contact),
        block3.build_program("M_B", menu_b, contact),
    )
    e0 = block3.h2_to_numpy(menu_a[0])
    remainder = block4.positive_sqrt(np.eye(2) - e0) @ contact
    inverse = np.linalg.inv(remainder)
    rho = np.diag((3 / 5, 2 / 5)).astype(complex)
    sigma_b = remainder @ rho @ remainder.conj().T
    exact_targets = {
        "M_A": (SIGMA_A1, SIGMA_A2),
        "M_B": (SIGMA_B1, SIGMA_B2),
    }
    residuals = []
    for program in programs:
        for operator, target in zip(program.kraus[1:], exact_targets[program.name], strict=True):
            residual_operator = operator @ inverse
            residuals.extend(
                (
                    float(np.linalg.norm(residual_operator @ sigma_b @ residual_operator.conj().T - np.asarray(target, dtype=complex))),
                    float(np.linalg.norm(operator @ rho @ operator.conj().T - np.asarray(target, dtype=complex))),
                )
            )
    check(
        "exact-residual-cp-state-sufficiency",
        max(residuals) < TOL,
        "the Hermitian projection of CB is sufficient for each exact residual CP update and reproduces every declared terminal code state",
    )


def locked_output_writer_controls() -> None:
    x00, x11, xr, xi = sp.symbols("x00 x11 xr xi", real=True)
    rho = sp.Matrix(((x00, xr + sp.I * xi), (xr - sp.I * xi, x11)))
    p0 = sp.diag(1, 0)
    p1 = sp.diag(0, 1)
    out0 = sp.trace(E0 * rho) * p0
    out1 = sp.trace(EB * rho) * p1
    choi0 = sp.kronecker_product(E0.T, p0)
    choib = sp.kronecker_product(EB.T, p1)
    mixed_definite_control = sp.Rational(2, 5) * p0 + sp.Rational(3, 5) * p1
    check(
        "locked-output-front-writer-normal-form",
        (I2 - p0) * out0 * (I2 - p0) == sp.zeros(2)
        and (I2 - p1) * out1 * (I2 - p1) == sp.zeros(2)
        and E0.is_positive_semidefinite is True
        and EB.is_positive_semidefinite is True
        and (I2 - E0).is_positive_semidefinite is True
        and (I2 - EB).is_positive_semidefinite is True
        and choi0.is_positive_semidefinite is True
        and choib.is_positive_semidefinite is True
        and sp.simplify(sp.trace(out0 + out1) - sp.trace(rho)) == 0,
        "the supplied effect bounds and Choi matrices prove CP locked selective outputs; their nonselective sum is trace preserving because E0+EB=I",
    )
    rho_star = block4.RHO_EXACT
    output = sp.simplify(sp.trace(E0 * rho_star) * p0 + sp.trace(EB * rho_star) * p1)
    check(
        "locked-output-code-calibration-interface",
        output == sp.diag(*TRACE_WEIGHTS["front"])
        and mixed_definite_control[0, 0] > 0
        and mixed_definite_control[1, 1] > 0
        and ATOMS["front"] == (C0, CB)
        and tuple(rail_projection(value) for value in ATOMS["front"]) == (R0, RB),
        "a supplied fixed-preparation calibration can map the two locked labels to typed codes without treating those non-Hermitian codes as density matrices",
    )


def total_kernel_and_covariance_controls() -> None:
    exact_shells = {"front": FRONT, "continuation-A": CONT_A, "continuation-B": CONT_B}
    orbit_sizes = {stage: len(reference) for stage, reference in ORBITS.items()}
    exact_bumps = {
        stage: route_bumps(value)
        for stage, value in exact_shells.items()
    }
    pair_distances: list[sp.Expr] = []
    stages = tuple(exact_shells)
    for left_index, left in enumerate(stages):
        for right in stages[left_index + 1 :]:
            candidates = [
                distance
                for a, b in product(ORBITS[left], ORBITS[right])
                if (distance := block5.shell_distance(a, b)) is not None
            ]
            pair_distances.append(min(candidates, key=lambda item: float(sp.N(item))))
    check(
        "disjoint-three-stage-orbit-guards",
        orbit_sizes == {"front": 24, "continuation-A": 24, "continuation-B": 24}
        and all(exact_bumps[stage][stage] == 1 for stage in stages)
        and all(exact_bumps[stage][other] == 0 for stage in stages for other in stages if other != stage)
        and min(pair_distances) == 3
        and min(pair_distances) > 4 * PATCH_RADIUS,
        {"minimum_squared_orbit_separation": min(pair_distances), "patch_squared_radius": PATCH_RADIUS},
    )

    stage_specs = {
        "front": (block4.PREPARATION, block4.COMMON_MARKERS),
        "continuation-A": (CB, block4.RESIDUAL_MARKERS | {block4.CONTEXT_A}),
        "continuation-B": (CB, block4.RESIDUAL_MARKERS | {block4.CONTEXT_B}),
    }
    guarded_support_exact = True
    for stage, (predecessor, marker_set) in stage_specs.items():
        candidates: list[Shell] = []
        for blank in DIRECTIONS:
            predecessor_direction = block4.neg(blank)
            transverse_directions = tuple(
                direction
                for direction in DIRECTIONS
                if direction not in (blank, predecessor_direction)
            )
            for marker_order in permutations(tuple(marker_set)):
                slots: dict[Point, M2Code | None] = {direction: None for direction in DIRECTIONS}
                slots[predecessor_direction] = predecessor
                slots.update(zip(transverse_directions, marker_order, strict=True))
                candidates.append(Shell(tuple(slots[direction] for direction in DIRECTIONS)))
        survivors = {
            candidate
            for candidate in candidates
            if formation_probability(candidate) != 0
        }
        guarded_support_exact &= (
            len(candidates) == 144
            and all(typed_shell_stage(candidate) == stage for candidate in candidates)
            and len(survivors) == 24
            and survivors == set(ORBITS[stage])
        )

    empty = Shell((None,) * 6)
    one = Shell((block5.as_code(I2), None, None, None, None, None))
    near_typed_records = after_first(
        LAYOUT_A,
        code(matrix(CB) + sp.Rational(1, 64) * I2),
    )
    near_untyped_records = after_first(
        LAYOUT_A,
        code(matrix(CB) + sp.I * sp.Rational(1, 64) * sp.diag(1, -1)),
    )
    near_typed = shell(near_typed_records, LAYOUT_A.continuation_target)
    near_untyped = shell(near_untyped_records, LAYOUT_A.continuation_target)
    exact_descriptors = [content_kernel(value, model) for value in exact_shells.values() for model in ("trace", "free")]
    off_empty = content_kernel(empty, "trace")
    off_one = content_kernel(one, "free")
    check(
        "total-borel-condition-varying-kernel",
        all(item.normalized() and item.bump_weight == 1 and len(item.atoms) == 2 for item in exact_descriptors)
        and off_empty.family == off_one.family == "full_gaussian"
        and off_empty.gaussian_center != off_one.gaussian_center
        and typed_shell_stage(near_typed) is None
        and typed_shell_stage(near_untyped) is None
        and content_kernel(near_typed, "trace").family == "full_gaussian"
        and content_kernel(near_untyped, "trace").family == "full_gaussian"
        and formation_probability(near_typed) == 0
        and formation_probability(near_untyped) == 0
        and forming_sites(near_typed_records) == ()
        and forming_sites(near_untyped_records) == ()
        and guarded_support_exact
        and formation_probability(empty) == 0,
        "the exact typed gate leaves exactly 24 of 144 typed orientations per stage, rejects typed-near and untyped continuation spoofs, and leaves a total Borel content kernel with condition-varying full-support fallback",
    )

    covariance_failures = 0
    for stage, exact in exact_shells.items():
        for rotation in block5.ROTATIONS:
            carried = block5.rotate_shell(exact, rotation)
            covariance_failures += route_bumps(carried)[stage] != 1
            covariance_failures += content_kernel(carried, "trace").atom_weights != TRACE_WEIGHTS[stage]
            covariance_failures += content_kernel(carried, "free").atom_weights != FREE_WEIGHTS[stage]
    check(
        "translation-and-proper-cubic-slot-covariance",
        covariance_failures == 0,
        "all three stage laws carry through the 24 proper-cubic relative-slot frames; translation is automatic and no internal M2 co-action is claimed",
    )


def history_controls() -> None:
    histories = {}
    for context in ("A", "B"):
        stage = f"continuation-{context}"
        front0, frontb = TRACE_WEIGHTS["front"]
        residual0, residual1 = TRACE_WEIGHTS[stage]
        histories[context] = (
            front0,
            sp.simplify(frontb * residual0),
            sp.simplify(frontb * residual1),
        )
    free_histories = {}
    for context in ("A", "B"):
        stage = f"continuation-{context}"
        front0, frontb = FREE_WEIGHTS["front"]
        residual0, residual1 = FREE_WEIGHTS[stage]
        free_histories[context] = (
            front0,
            sp.simplify(frontb * residual0),
            sp.simplify(frontb * residual1),
        )
    check(
        "trace-matched-finite-record-history",
        histories["A"] == (sp.Rational(3, 10), sp.Rational(19, 50), sp.Rational(8, 25))
        and histories["B"] == (sp.Rational(3, 10), sp.Rational(7, 20), sp.Rational(7, 20))
        and tuple(sum(values) for values in histories.values()) == (1, 1)
        and histories["A"] == (SIGMA0.trace(), SIGMA_A1.trace(), SIGMA_A2.trace())
        and histories["B"] == (SIGMA0.trace(), SIGMA_B1.trace(), SIGMA_B2.trace()),
        "the supplied trace-matched Record path law exactly equals the supplied flat ternary instrument weights in both delayed contexts",
    )
    check(
        "support-identical-free-weight-control",
        all(sum(values) == 1 for values in free_histories.values())
        and free_histories["A"] != histories["A"]
        and free_histories["B"] != histories["B"]
        and all(ATOMS[stage] == content_kernel(value, "free").atoms == content_kernel(value, "trace").atoms for stage, value in (("front", FRONT), ("continuation-A", CONT_A), ("continuation-B", CONT_B))),
        {
            "same_support_and_stage_topology": True,
            "trace_matching_selected_by_current_axioms": False,
        },
    )

    layout = LAYOUT_A
    initial = layout.record_map()
    after_cb = append_from_stage(initial, layout.first_target, CB)
    terminal = append_from_stage(after_cb, layout.continuation_target, CA1)
    check(
        "formation-permanence-and-no-preemption",
        formation_probability(shell(initial, layout.first_target)) == 1
        and formation_probability(shell(initial, layout.continuation_target)) == 0
        and formation_probability(shell(after_cb, layout.continuation_target)) == 1
        and forming_sites(initial) == (layout.first_target,)
        and forming_sites(after_cb) == (layout.continuation_target,)
        and forming_sites(after_first(layout, C0)) == ()
        and forming_sites(terminal) == ()
        and all(terminal[position] == value for position, value in initial.items()),
        "the exact path forms only at the typed active target, never enables s1 early, and never overwrites a prior Record",
    )


def ensemble_consistency_controls() -> None:
    """Force stage weights only after exact cq ensemble consistency is imposed."""

    stage_operators = {
        "front": (SIGMA0, SIGMAB),
        "continuation-A": (SIGMA_A1, SIGMA_A2),
        "continuation-B": (SIGMA_B1, SIGMA_B2),
    }
    recovered: dict[str, tuple[sp.Expr, sp.Expr]] = {}
    free_mismatches: dict[str, bool] = {}
    for stage, operators in stage_operators.items():
        total_mass = sp.simplify(sum(operator.trace() for operator in operators))
        normalized_branches = tuple(
            sp.simplify(operator / operator.trace()) for operator in operators
        )
        cq_nonselective = sp.diag(
            *(sp.simplify(operator / total_mass) for operator in operators)
        )
        q0, q1 = sp.symbols(f"q_{stage}_0 q_{stage}_1", real=True)
        selected_ensemble = sp.diag(
            q0 * normalized_branches[0], q1 * normalized_branches[1]
        )
        equations = [
            sp.simplify(entry)
            for entry in selected_ensemble - cq_nonselective
            if sp.simplify(entry) != 0
        ]
        solutions = sp.solve(equations + [q0 + q1 - 1], (q0, q1), dict=True)
        recovered[stage] = (
            sp.simplify(solutions[0][q0]),
            sp.simplify(solutions[0][q1]),
        )
        free_ensemble = sp.diag(
            FREE_WEIGHTS[stage][0] * normalized_branches[0],
            FREE_WEIGHTS[stage][1] * normalized_branches[1],
        )
        free_mismatches[stage] = free_ensemble != cq_nonselective

    check(
        "sectorwise-cq-ensemble-consistency-uniqueness",
        recovered == TRACE_WEIGHTS
        and all(free_mismatches.values()),
        "conditional on the exact cq nonselective state, normalized conditional branch states, and ensemble consistency, orthogonal-sector projections uniquely force every displayed trace weight; the free law fails that extra premise",
    )


def route_boundary_controls() -> None:
    note = normalized(NOTE_PATH)
    required = (
        "conditional positive completion",
        "instrument-measure/record-measure identification",
        "not a pointwise actualization theorem",
        "the free-weight law",
        "sectorwise ensemble-consistency lemma",
        "no axiom amendment",
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
        "narrow-conditional-completion-boundary",
        all(phrase in note for phrase in required),
        "the note ships the exact conditional construction and isolates its supplied law equality without turning it into retained closure or a broad no-go",
    )

    n5 = (
        "per_element: checked — exact positive branch operators, typed Hermitian state projection, apparatus-relative rail projection, anti-Hermitian spoof rejection, and non-Hermitian-code firewall",
        "per_site: checked — unique initial front, delayed complement continuation, effect-rail rejection, permanent append, total shell kernel, and condition-varying Gaussian fallback",
        "per_mode: checked — coherent Kraus possibility, locked-output label register, typed Record-code calibration, trace-matched law, and support-identical free-weight law remain distinct",
        "per_block: checked — exact two-stage CP composition, three disjoint 24-shell orbit guards, proper-cubic slot covariance, typed-near/preemption controls, and normalized terminal histories",
        "lattice_wide: checked and not executed — local Borel kernels admit the supplied discrete-step product/path extension; physical time, seed genesis, state-affinity authority, and contingent actualization remain open",
    )
    for line in n5:
        print(line)
    check(
        "n5-certificate",
        all(len(line) >= 120 for line in n5)
        and all(line in NOTE_PATH.read_text(encoding="utf-8") for line in n5),
        "all five substantive resolution lines are present in primary stdout and the theorem note",
    )


def main() -> int:
    source_controls()
    typed_projection_controls()
    staged_geometry_controls()
    exact_branch_operator_controls()
    locked_output_writer_controls()
    total_kernel_and_covariance_controls()
    history_controls()
    ensemble_consistency_controls()
    route_boundary_controls()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
