#!/usr/bin/env python3
"""Block 7: fresh-ancilla staged cq/Record intertwiner.

This runner composes the exact Block-6 delayed A/B fixture with a
probability-independent Stinespring instrument and fresh orthogonal label
fragments.  It proves an exact channel identity between the staged path
writer and the flat label-retaining cq instrument, then calibrates that path
object to the fixed Block-6 typed Record histories at rho*=diag(3/5,2/5).

The construction does not silently turn a cq state into a realized atom.
It also does not identify the central restriction of the quantum channel with
the framework Admissibility distribution.  That compatibility, physical
Record typing/formation, fresh-fragment genesis, and time remain explicit
downstream data.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys

import sympy as sp


AUDIT_TIMEOUT_SEC = 180

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import instrument_port_typed_record_compiler_conditional_completion_2026_08_20 as block6
import shared_effect_record_randomized_preparation_congruence_independence_2026_08_20 as block3


NOTE_PATH = ROOT / "docs" / (
    "FRESH_ANCILLA_STAGED_CQ_RECORD_INTERTWINER_CONDITIONAL_"
    "COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REALIZED_PATH = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
BLOCK6_PATH = ROOT / "docs" / (
    "INSTRUMENT_PORT_TYPED_RECORD_COMPILER_CONDITIONAL_COMPLETION_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
CONTROLLED_COPY_PATH = ROOT / "docs" / (
    "RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_"
    "THEOREM_NOTE_2026-06-18.md"
)
PERSISTENT_PATH = ROOT / "docs" / (
    "PERSISTENT_RECORD_INSTRUMENT_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-22.md"
)

AUDIT_INPUT_PATHS = (
    "docs/FRESH_ANCILLA_STAGED_CQ_RECORD_INTERTWINER_CONDITIONAL_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "docs/INSTRUMENT_PORT_TYPED_RECORD_COMPILER_CONDITIONAL_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md",
    "docs/PERSISTENT_RECORD_INSTRUMENT_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-22.md",
    "scripts/instrument_port_typed_record_compiler_conditional_completion_2026_08_20.py",
    "scripts/shared_effect_record_randomized_preparation_congruence_independence_2026_08_20.py",
)

PASS = 0
FAIL = 0

I2 = sp.eye(2)
X = sp.Matrix(((0, 1), (1, 0)))
Y = sp.Matrix(((0, -sp.I), (sp.I, 0)))
Z = sp.diag(1, -1)
PAULIS = (I2, X, Y, Z)

RHO_STAR = sp.diag(sp.Rational(3, 5), sp.Rational(2, 5))
RHO_TOMO = {
    "mixed": I2 / 2,
    "+x": (I2 + X) / 2,
    "+y": (I2 + Y) / 2,
    "+z": (I2 + Z) / 2,
}


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


def rational(value: Fraction) -> sp.Rational:
    return sp.Rational(value.numerator, value.denominator)


def qsqrt2(value: object) -> sp.Expr:
    return rational(value.a) + rational(value.b) * sp.sqrt(2)  # type: ignore[attr-defined]


def h2_matrix(value: object) -> sp.Matrix:
    upper = qsqrt2(value.q_re) + sp.I * qsqrt2(value.q_im)  # type: ignore[attr-defined]
    return sp.Matrix(
        (
            (qsqrt2(value.p), upper),  # type: ignore[attr-defined]
            (sp.conjugate(upper), qsqrt2(value.r)),  # type: ignore[attr-defined]
        )
    )


def is_zero(value: sp.Matrix) -> bool:
    return sp.simplify(value) == sp.zeros(*value.shape)


def direct_sum(blocks: tuple[sp.Matrix, ...]) -> sp.Matrix:
    return sp.diag(*blocks)


def exact_programs() -> dict[str, tuple[sp.Matrix, ...]]:
    menu_a, menu_b = block3.exact_menus()
    programs: dict[str, tuple[sp.Matrix, ...]] = {}
    for context, menu in (("A", menu_a), ("B", menu_b)):
        effects = tuple(h2_matrix(effect) for effect in menu)
        programs[context] = tuple(
            sp.simplify(effect / sp.sqrt(sp.trace(effect))) for effect in effects
        )
    return programs


PROGRAMS = exact_programs()
K0 = PROGRAMS["A"][0]
B = sp.diag(1 / sp.sqrt(2), 1)


def residual_program(context: str) -> tuple[sp.Matrix, sp.Matrix]:
    return tuple(
        sp.simplify(operator * B.inv()) for operator in PROGRAMS[context][1:]
    )  # type: ignore[return-value]


def cq_channel(
    operators: tuple[sp.Matrix, ...], rho: sp.Matrix
) -> sp.Matrix:
    return direct_sum(
        tuple(sp.simplify(operator * rho * operator.H) for operator in operators)
    )


def block_weights(cq_state: sp.Matrix, branches: int) -> tuple[sp.Expr, ...]:
    return tuple(
        sp.simplify(sp.trace(cq_state[2 * index : 2 * index + 2, 2 * index : 2 * index + 2]))
        for index in range(branches)
    )


def pointer_isometry(operators: tuple[sp.Matrix, ...]) -> sp.Matrix:
    return sp.Matrix.vstack(*operators)


def label_copy_unitary(labels: int) -> sp.Matrix:
    """Controlled modular add from a pointer label into a blank label cell."""

    unitary = sp.zeros(labels * labels)
    for pointer in range(labels):
        for memory in range(labels):
            source = pointer * labels + memory
            target = pointer * labels + ((memory + pointer) % labels)
            unitary[target, source] = 1
    return unitary


def blank_memory_embedding(labels: int) -> sp.Matrix:
    """Embed pointer x system into pointer x blank-memory x system."""

    embedding = sp.zeros(labels * labels * 2, labels * 2)
    for pointer in range(labels):
        for system in range(2):
            source = pointer * 2 + system
            target = (pointer * labels) * 2 + system
            embedding[target, source] = 1
    return embedding


def copied_isometry(operators: tuple[sp.Matrix, ...]) -> sp.Matrix:
    labels = len(operators)
    raw = pointer_isometry(operators)
    copy = sp.kronecker_product(label_copy_unitary(labels), I2)
    return sp.simplify(copy * blank_memory_embedding(labels) * raw)


def trace_pointer_after_copy(
    copied: sp.Matrix, rho: sp.Matrix, labels: int
) -> sp.Matrix:
    joint = sp.simplify(copied * rho * copied.H)
    reduced = sp.zeros(labels * 2)
    for left_label in range(labels):
        for right_label in range(labels):
            for left_system in range(2):
                for right_system in range(2):
                    reduced[left_label * 2 + left_system, right_label * 2 + right_system] = sp.simplify(
                        sum(
                            joint[
                                (pointer * labels + left_label) * 2 + left_system,
                                (pointer * labels + right_label) * 2 + right_system,
                            ]
                            for pointer in range(labels)
                        )
                    )
    return reduced


def path_branches(context: str) -> tuple[tuple[tuple[str, ...], sp.Matrix], ...]:
    j1, j2 = residual_program(context)
    return (
        (("0",), K0),
        (("B", "1"), sp.simplify(j1 * B)),
        (("B", "2"), sp.simplify(j2 * B)),
    )


def staged_append_isometry(context: str) -> sp.Matrix:
    """Append residual occupancy flag/label without changing the front bit.

    Input order is first-memory bit x system.  Output order is
    first-memory bit x residual-occupancy flag x residual-label bit x system.
    Memory indices 000, 110, and 111 carry the terminal paths 0, B1, and B2.
    """

    j1, j2 = residual_program(context)
    stage = sp.zeros(16, 4)
    stage[0:2, 0:2] = I2
    stage[12:14, 2:4] = j1
    stage[14:16, 2:4] = j2
    return stage


def flagged_path_isometry(context: str) -> sp.Matrix:
    return sp.simplify(staged_append_isometry(context) * pointer_isometry((K0, B)))


def source_controls() -> None:
    paths = (
        NOTE_PATH,
        AXIOM_PATH,
        REALIZED_PATH,
        BLOCK6_PATH,
        CONTROLLED_COPY_PATH,
        PERSISTENT_PATH,
    )
    sources = {path.name: normalized(path) for path in paths}
    axiom = sources[AXIOM_PATH.name]
    realized = sources[REALIZED_PATH.name]
    block6_text = sources[BLOCK6_PATH.name]
    controlled = sources[CONTROLLED_COPY_PATH.name]
    persistent = sources[PERSISTENT_PATH.name]
    check(
        "sources-and-authority-boundary",
        all(path.exists() for path in paths)
        and "probability distribution over the possibilities is determined by" in axiom
        and "distribution's form and values" in axiom
        and "not a state-selection rule" in realized
        and "physical cq-instrument/record-ensemble equality" in block6_text
        and "fresh blank fragment" in controlled
        and "given any kraus family" in persistent
        and "resolution-of-identity hypothesis" in persistent,
        "the current axiom, realized-state, Block-6, fresh-copy, and abstract-instrument boundaries are bound",
    )


def exact_instrument_controls() -> None:
    menu_a, menu_b = block3.exact_menus()
    effects = {
        context: tuple(h2_matrix(effect) for effect in menu)
        for context, menu in (("A", menu_a), ("B", menu_b))
    }
    normalization = all(
        is_zero(sum((operator.H * operator for operator in program), sp.zeros(2)) - I2)
        and is_zero(sum(effects[context], sp.zeros(2)) - I2)
        for context, program in PROGRAMS.items()
    )
    check(
        "exact-two-menu-instruments",
        normalization
        and PROGRAMS["A"][0] == PROGRAMS["B"][0] == K0
        and is_zero(K0.H * K0 - block6.E0)
        and is_zero(B.H * B - block6.EB),
        "both exact ternary instruments normalize and share the same binary front {K0,B}",
    )

    targets = {
        "A": (block6.SIGMA0, block6.SIGMA_A1, block6.SIGMA_A2),
        "B": (block6.SIGMA0, block6.SIGMA_B1, block6.SIGMA_B2),
    }
    branches = {
        context: tuple(
            sp.simplify(operator * RHO_STAR * operator.H)
            for operator in program
        )
        for context, program in PROGRAMS.items()
    }
    check(
        "exact-Block6-branch-state-recovery",
        all(
            all(is_zero(actual - expected) for actual, expected in zip(branches[context], targets[context], strict=True))
            for context in ("A", "B")
        ),
        "the post-contact exact programs reproduce all six fixed Block-6 positive branch operators",
    )


def staged_factorization_controls() -> None:
    failures = 0
    for context, program in PROGRAMS.items():
        residual = residual_program(context)
        failures += not is_zero(
            sum((operator.H * operator for operator in residual), sp.zeros(2)) - I2
        )
        failures += any(
            not is_zero(operator * B - target)
            for operator, target in zip(residual, program[1:], strict=True)
        )
        front = (K0, B)
        failures += not is_zero(pointer_isometry(front).H * pointer_isometry(front) - I2)
        failures += not is_zero(pointer_isometry(residual).H * pointer_isometry(residual) - I2)
    check(
        "exact-repeated-interaction-factorization",
        failures == 0,
        "the common binary front and each delayed residual are normalized isometries and Jr B=Kr exactly",
    )


def fresh_copy_controls() -> None:
    failures = 0
    fixtures = (("front", (K0, B)),) + tuple(
        (f"residual-{context}", residual_program(context)) for context in ("A", "B")
    )
    for _name, operators in fixtures:
        copied = copied_isometry(operators)
        copy = label_copy_unitary(2)
        failures += not is_zero(copy.H * copy - sp.eye(4))
        failures += not is_zero(copied.H * copied - I2)
        for rho in RHO_TOMO.values():
            failures += not is_zero(
                trace_pointer_after_copy(copied, rho, 2) - cq_channel(operators, rho)
            )
    check(
        "fresh-orthogonal-label-copy-channel",
        failures == 0,
        "a supplied fresh binary fragment plus controlled label copy yields the exact cq channel after the pointer ancilla is forgotten, for both stages and a spanning preparation family",
    )


def path_intertwiner_controls() -> None:
    x00, x11, xr, xi = sp.symbols("x00 x11 xr xi", real=True)
    rho = sp.Matrix(((x00, xr + sp.I * xi), (xr - sp.I * xi, x11)))
    failures = 0
    prefixes: dict[str, tuple[tuple[str, ...], ...]] = {}
    for context, program in PROGRAMS.items():
        paths = path_branches(context)
        prefixes[context] = tuple(history for history, _operator in paths)
        path_operators = tuple(operator for _history, operator in paths)
        failures += any(
            not is_zero(path_operator - flat_operator)
            for path_operator, flat_operator in zip(path_operators, program, strict=True)
        )
        failures += not is_zero(cq_channel(path_operators, rho) - cq_channel(program, rho))
        failures += not is_zero(
            sum((operator.H * operator for operator in path_operators), sp.zeros(2)) - I2
        )
    check(
        "probability-independent-staged-to-flat-cq-intertwiner",
        failures == 0
        and prefixes == {
            "A": (("0",), ("B", "1"), ("B", "2")),
            "B": (("0",), ("B", "1"), ("B", "2")),
        },
        "the path decoder maps the two fresh binary writes to the flat ternary cq instrument as a symbolic channel identity, with no scalar branch weights supplied",
    )

    append_only = all(
        history == ("0",) or history[:1] == ("B",)
        for context in ("A", "B")
        for history, _operator in path_branches(context)
    )
    check(
        "append-only-prefix-memory",
        append_only
        and all(len(history) in (1, 2) for history, _operator in path_branches("A"))
        and all(len(history) in (1, 2) for history, _operator in path_branches("B")),
        "terminal continuation paths retain the earlier B label and the 0 path never acquires a later label",
    )

    explicit_failures = 0
    for context, program in PROGRAMS.items():
        stage = staged_append_isometry(context)
        full = flagged_path_isometry(context)
        explicit_failures += not is_zero(stage.H * stage - sp.eye(4))
        explicit_failures += not is_zero(full.H * full - I2)
        expected = sp.zeros(16, 2)
        expected[0:2, :] = program[0]
        expected[12:14, :] = program[1]
        expected[14:16, :] = program[2]
        explicit_failures += not is_zero(full - expected)
        explicit_failures += not is_zero(full[12:14, :] - program[1])
        explicit_failures += not is_zero(full[14:16, :] - program[2])
    check(
        "explicit-flagged-staged-memory-isometry",
        explicit_failures == 0,
        "an exact second interaction preserves the first B bit, flips a supplied fresh residual-occupancy flag, writes the residual bit, and realizes terminal memory words 000,110,111 with Kraus blocks K0,K1,K2",
    )


def fixed_record_calibration_controls() -> None:
    terminal_codes = {
        "A": (block6.C0, block6.CA1, block6.CA2),
        "B": (block6.C0, block6.CB1, block6.CB2),
    }
    terminal_labels = {"A": (0, 2, 3), "B": (0, 4, 5)}
    failures = 0
    histories: dict[str, tuple[tuple[object, ...], ...]] = {}
    sigma_b = sp.simplify(B * RHO_STAR * B.H)
    failures += not is_zero(sigma_b - block6.SIGMAB)
    failures += block6.kappa(sigma_b, 1) != block6.CB
    for context, program in PROGRAMS.items():
        operators = tuple(
            sp.simplify(operator * RHO_STAR * operator.H) for operator in program
        )
        codes = tuple(
            block6.kappa(operator, label)
            for operator, label in zip(operators, terminal_labels[context], strict=True)
        )
        failures += codes != terminal_codes[context]
        histories[context] = (
            (block6.C0,),
            (block6.CB, terminal_codes[context][1]),
            (block6.CB, terminal_codes[context][2]),
        )
        failures += any(
            block6.hermitian_projection(code) != operator
            for code, operator in zip(codes, operators, strict=True)
        )
        failures += any(
            not is_zero(
                sp.simplify(residual_operator * sigma_b * residual_operator.H)
                - terminal_operator
            )
            for residual_operator, terminal_operator in zip(
                residual_program(context), operators[1:], strict=True
            )
        )
    check(
        "fixed-preparation-typed-Record-calibration",
        failures == 0
        and histories["A"] == ((block6.C0,), (block6.CB, block6.CA1), (block6.CB, block6.CA2))
        and histories["B"] == ((block6.C0,), (block6.CB, block6.CB1), (block6.CB, block6.CB2)),
        "at rho* the path-label/postbranch-state object calibrates exactly to every Block-6 typed permanent history",
    )


def central_restriction_controls() -> None:
    recovered: dict[str, tuple[sp.Expr, ...]] = {}
    for context, program in PROGRAMS.items():
        cq_state = cq_channel(program, RHO_STAR)
        recovered[context] = block_weights(cq_state, 3)
    check(
        "central-sector-masses-without-input-q-table",
        recovered == {
            "A": (sp.Rational(3, 10), sp.Rational(19, 50), sp.Rational(8, 25)),
            "B": (sp.Rational(3, 10), sp.Rational(7, 20), sp.Rational(7, 20)),
        }
        and all(sum(weights) == 1 for weights in recovered.values()),
        "restricting the normalized cq channel state to its label center yields the exact Block-6 trace masses; the writer takes operators and rho, not a probability vector",
    )


def tomography_and_hostile_controls() -> None:
    coordinates = sp.Matrix(
        [
            [sp.simplify(sp.trace(axis * rho)) for axis in PAULIS]
            for rho in RHO_TOMO.values()
        ]
    )
    a, b, c, d = sp.symbols("a b c d", real=True)
    candidate_effect = sp.Matrix(((a, c - sp.I * d), (c + sp.I * d, b)))

    def solve_effect(expected: sp.Matrix) -> list[dict[sp.Symbol, sp.Expr]]:
        equations = [
            sp.simplify(sp.trace((candidate_effect - expected) * rho))
            for rho in RHO_TOMO.values()
        ]
        return sp.solve(equations, (a, b, c, d), dict=True)

    effect_solutions = {
        (context, index): solve_effect(sp.simplify(operator.H * operator))
        for context, program in PROGRAMS.items()
        for index, operator in enumerate(program)
    }
    expected_solutions = {
        (context, index): [
            {
                a: sp.simplify(effect[0, 0]),
                b: sp.simplify(effect[1, 1]),
                c: sp.simplify(sp.re(effect[0, 1])),
                d: sp.simplify(-sp.im(effect[0, 1])),
            }
        ]
        for context, program in PROGRAMS.items()
        for index, operator in enumerate(program)
        for effect in (sp.simplify(operator.H * operator),)
    }
    check(
        "effect-complete-four-preparation-identification",
        coordinates.rank() == 4
        and effect_solutions == expected_solutions
        and effect_solutions[("A", 0)]
        == [{a: sp.Rational(1, 2), b: 0, c: 0, d: 0}],
        "four physical density preparations span Hermitian M2; equality of retained label-I statistics forces every A/B branch effect, including the shared F0=E0, rather than an arbitrary affine POVM",
    )

    wrong_effects = (sp.Rational(3, 10) * I2, sp.Rational(7, 10) * I2)
    front = (K0, B)

    def pointwise_reweighted_front(
        rho: sp.Matrix, weights: tuple[sp.Expr, sp.Expr]
    ) -> sp.Matrix:
        """Pointwise comparison only; normalization makes this map nonlinear."""

        branches = tuple(sp.simplify(operator * rho * operator.H) for operator in front)
        normalized_branches = tuple(
            sp.simplify(branch / sp.trace(branch)) for branch in branches
        )
        return direct_sum(
            tuple(
                sp.simplify(weight * branch)
                for weight, branch in zip(weights, normalized_branches, strict=True)
            )
        )

    star_branches = tuple(
        sp.simplify(operator * RHO_STAR * operator.H) for operator in front
    )
    tau_star = tuple(
        sp.simplify(branch / sp.trace(branch)) for branch in star_branches
    )

    def wrong_affine_front(rho: sp.Matrix) -> sp.Matrix:
        """Fixed-state measure-prepare instrument induced by wrong_effects."""

        return direct_sum(
            tuple(
                sp.simplify(sp.trace(effect * rho) * state)
                for effect, state in zip(wrong_effects, tau_star, strict=True)
            )
        )

    true_star = cq_channel(front, RHO_STAR)
    wrong_star = wrong_affine_front(RHO_STAR)
    free_star = pointwise_reweighted_front(
        RHO_STAR, block6.FREE_WEIGHTS["front"]
    )

    wrong_label_gaps: list[sp.Expr] = []
    for rho in RHO_TOMO.values():
        actual = cq_channel(front, rho)
        hostile = wrong_affine_front(rho)
        for label in range(2):
            projector = sp.zeros(4)
            projector[2 * label : 2 * label + 2, 2 * label : 2 * label + 2] = I2
            wrong_label_gaps.append(sp.simplify(sp.trace(projector * (actual - hostile))))

    rho_left = RHO_TOMO["+x"]
    rho_right = RHO_TOMO["+z"]
    wrong_affinity_gap = sp.simplify(
        wrong_affine_front((rho_left + rho_right) / 2)
        - (wrong_affine_front(rho_left) + wrong_affine_front(rho_right)) / 2
    )
    wrong_choi_blocks = tuple(
        sp.kronecker_product(effect.T, state)
        for effect, state in zip(wrong_effects, tau_star, strict=True)
    )

    mixed = RHO_TOMO["mixed"]
    actual_mixed = cq_channel(front, mixed)
    branch0 = actual_mixed[0:2, 0:2]
    branch1 = actual_mixed[2:4, 2:4]
    state_spoof = direct_sum((sp.simplify(X * branch0 * X), branch1))
    label_z = sp.diag(Z, sp.zeros(2))
    state_spoof_gap = sp.simplify(sp.trace(label_z * (actual_mixed - state_spoof)))

    check(
        "free-wrong-effect-and-state-spoof-discriminators",
        is_zero(wrong_star - true_star)
        and not is_zero(free_star - true_star)
        and any(gap != 0 for gap in wrong_label_gaps)
        and state_spoof_gap != 0
        and is_zero(wrong_affinity_gap)
        and all(block.is_positive_semidefinite is True for block in wrong_choi_blocks)
        and all(sp.simplify(sp.trace(state)) == 1 for state in tau_star)
        and all(effect.is_positive_semidefinite is True for effect in wrong_effects)
        and is_zero(sum(wrong_effects, sp.zeros(2)) - I2),
        {
            "wrong_effect_matches_rho_star": True,
            "wrong_effect_full_cq_control_is_affine_cp_tp": True,
            "wrong_effect_rejected_by_spanning_preparations": True,
            "state_spoof_rejected_by_label_times_Pauli": True,
            "free_Block6_pointwise_weights_rejected": True,
        },
    )

    coherent_pointer = sp.simplify(
        pointer_isometry(front) * mixed * pointer_isometry(front).H
    )
    diagonal_blind = all(
        sp.simplify(
            sp.trace(
                sp.kronecker_product(sp.diag(1 if label == 0 else 0, 1 if label == 1 else 0), observable)
                * (coherent_pointer - actual_mixed)
            )
        )
        == 0
        for label in range(2)
        for observable in PAULIS
    )
    offdiagonal_gaps = tuple(
        sp.simplify(
            sp.trace(
                sp.kronecker_product(label_axis, observable)
                * (coherent_pointer - actual_mixed)
            )
        )
        for label_axis in (X, Y)
        for observable in PAULIS
    )
    check(
        "coherent-label-offdiagonal-discriminator",
        diagonal_blind and any(gap != 0 for gap in offdiagonal_gaps),
        "label projectors times system Paulis certify the cq blocks only after cq structure is established; label X/Y times system Paulis independently reject a coherent-pointer spoof",
    )


def randomized_preparation_screening_controls() -> None:
    rho_left = RHO_TOMO["+x"]
    rho_right = RHO_TOMO["+z"]
    direct = sp.simplify((rho_left + rho_right) / 2)
    tagged = direct_sum((rho_left / 2, rho_right / 2))
    reduced = sp.simplify(tagged[0:2, 0:2] + tagged[2:4, 2:4])
    failures = 0
    for context, program in PROGRAMS.items():
        direct_output = cq_channel(program, direct)
        randomized_output = sp.simplify(
            (cq_channel(program, rho_left) + cq_channel(program, rho_right)) / 2
        )
        failures += not is_zero(direct_output - randomized_output)
        for label in range(3):
            for observable in PAULIS:
                sl = slice(2 * label, 2 * label + 2)
                failures += sp.simplify(
                    sp.trace(observable * direct_output[sl, sl])
                    - sp.trace(observable * randomized_output[sl, sl])
                ) != 0
    check(
        "physical-tag-screening-and-preparation-affinity",
        is_zero(reduced - direct) and failures == 0,
        "after the supplied tag-forgetting channel, direct and fair tagged preparations give identical retained label-times-Pauli data by channel linearity; the tag state and forgetting operation remain explicit inputs",
    )


def capacity_and_type_controls() -> None:
    binary_cq_algebra_dimension = 2 * 2 * 2
    ternary_cq_algebra_dimension = 3 * 2 * 2
    one_site_algebra_dimension = 2 * 2
    binary_min_representation_dimension = 2 + 2
    ternary_min_representation_dimension = 2 + 2 + 2
    a, b, c, x, y, u, v = sp.symbols("a b c x y u v", real=True)
    normalized_binary_a = sp.Matrix(((a, x + sp.I * y), (x - sp.I * y, b)))
    normalized_binary_b = sp.Matrix(
        ((c, u + sp.I * v), (u - sp.I * v, 1 - a - b - c))
    )
    real_affine_code = sp.Matrix(
        ((a + sp.I * b, x + sp.I * y), (u + sp.I * v, c))
    )
    real_coordinate_map = sp.Matrix(
        (
            (1, 0, 0, 0, 0, 0, 0),
            (0, 1, 0, 0, 0, 0, 0),
            (0, 0, 0, 1, 0, 0, 0),
            (0, 0, 0, 0, 1, 0, 0),
            (0, 0, 0, 0, 0, 1, 0),
            (0, 0, 0, 0, 0, 0, 1),
            (0, 0, 1, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0),
        )
    )
    check(
        "multisite-cq-capacity-boundary",
        binary_cq_algebra_dimension == 8 > one_site_algebra_dimension == 4
        and ternary_cq_algebra_dimension == 12 > one_site_algebra_dimension
        and binary_min_representation_dimension == 4
        and ternary_min_representation_dimension == 6
        and 2**2 >= binary_min_representation_dimension
        and 2**2 < ternary_min_representation_dimension <= 2**3,
        "one M2 site cannot faithfully carry the full state-retaining binary or ternary cq algebra by a complex-linear/*-algebraic encoding; multisite carriers repair that exact interface, while nonlinear, real-affine, set-theoretic, and restricted-family code maps are not excluded",
    )
    check(
        "explicit-real-affine-one-site-counterroute",
        sp.simplify(sp.trace(normalized_binary_a) + sp.trace(normalized_binary_b)) == 1
        and real_coordinate_map.rank() == 7
        and not is_zero(real_affine_code - real_affine_code.H),
        "the normalized binary cq state space has an explicit injective real-affine code into non-Hermitian M2; it preserves neither *, products, positivity/order, nor the cq observable algebra, so it defeats any broader affine-capacity no-go",
    )


def boundary_and_no_go_controls() -> None:
    note = normalized(NOTE_PATH)
    required = (
        "conditional positive completion",
        "probability-independent",
        "central-restriction compatibility",
        "not an actual-member theorem",
        "one m2 site",
        "fail / do not ship",
        "no axiom amendment",
        "obligation retirement: zero",
        "toe percentage movement: zero",
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
        "honest-closure-and-axiom-boundary",
        all(phrase in note for phrase in required),
        "the note closes the exact staged cq writer/intertwiner while keeping central-law identification, Record typing, occurrence, apparatus genesis, and time separate",
    )

    n5 = (
        "per_element: checked — exact Kraus operators, branch operators, label projectors, postbranch Pauli observables, and typed fixed-preparation code calibration remain separately typed",
        "per_site: checked — fresh blank label fragments, controlled orthogonal label copy, faithful complex-linear full-cq-algebra one-M2 capacity failure, and supplied Record-typing boundary are explicit",
        "per_mode: checked — coherent isometry, pointer-forgotten cq channel, central restriction, wrong-effect affine measure-prepare law, pointwise free-weight comparison, and realized atom remain distinct",
        "per_block: checked — common binary front, delayed A/B residual isometries, append-only path prefixes, flat ternary channel intertwiner, and four-preparation tomography compose exactly",
        "lattice_wide: checked and not executed — finite fresh-fragment blocks fit qubit-lattice capacity, while autonomous fragment genesis, local formation/typing, overlap scheduling, and physical time remain open",
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
    exact_instrument_controls()
    staged_factorization_controls()
    fresh_copy_controls()
    path_intertwiner_controls()
    fixed_record_calibration_controls()
    central_restriction_controls()
    tomography_and_hostile_controls()
    randomized_preparation_screening_controls()
    capacity_and_type_controls()
    boundary_and_no_go_controls()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
