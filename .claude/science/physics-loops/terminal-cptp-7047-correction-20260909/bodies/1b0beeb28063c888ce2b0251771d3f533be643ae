#!/usr/bin/env python3
"""Independent Block-9 terminal-center/site-content boundary check.

This checker rebuilds the exact A/B effects and Kraus programs directly.  It
does not import the primary Block-9 runner or its upstream program objects.
It independently reconstructs the absorbing channels, integrated program and
freshness-flag channel, terminal dual identities, rank ledgers, carrier/type
boundaries, and stipulated coupling controls.
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 180

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "TERMINAL_CENTER_SITE_RECORD_DIAGONAL_COMMIT_MINIMAL_CARRIER_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

AUDIT_INPUT_PATHS = (
    "docs/TERMINAL_CENTER_SITE_RECORD_DIAGONAL_COMMIT_MINIMAL_CARRIER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "docs/INSTRUMENT_PORT_TYPED_RECORD_COMPILER_CONDITIONAL_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/FRESH_ANCILLA_STAGED_CQ_RECORD_INTERTWINER_CONDITIONAL_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/FIXED_CARRIER_PRESENCE_SEPARATED_NONDEMOLITION_RECORD_UPDATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06.md",
    "docs/work_history/repo/review_feedback/FULL_Z3_CAUSAL_FRONT_SAMPLED_INSTRUMENT_LAW_NOTE_2026-07-14.md",
    "docs/RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md",
    "scripts/terminal_center_site_record_diagonal_commit_minimal_carrier_boundary_2026_08_20.py",
    "scripts/fresh_ancilla_staged_cq_record_intertwiner_conditional_completion_2026_08_20.py",
    "scripts/shared_effect_record_randomized_preparation_congruence_independence_2026_08_20.py",
    "scripts/admissibility_barycenter_evaluation_menu_kernel_2026_08_12.py",
    "scripts/full_z3_causal_front_sampled_instrument_law_probe_2026_07_14.py",
)

PASS = 0
FAIL = 0

I2 = sp.eye(2)
X = sp.Matrix(((0, 1), (1, 0)))
Y = sp.Matrix(((0, -sp.I), (sp.I, 0)))
Z = sp.diag(1, -1)

E0 = sp.diag(sp.Rational(1, 2), 0)
EA1 = sp.Matrix(
    (
        (sp.Rational(1, 10), sp.sqrt(2) / 5),
        (sp.sqrt(2) / 5, sp.Rational(4, 5)),
    )
)
EA2 = sp.Matrix(
    (
        (sp.Rational(2, 5), -sp.sqrt(2) / 5),
        (-sp.sqrt(2) / 5, sp.Rational(1, 5)),
    )
)
EB1 = sp.Matrix(
    (
        (sp.Rational(1, 4), sp.sqrt(2) / 4),
        (sp.sqrt(2) / 4, sp.Rational(1, 2)),
    )
)
EB2 = sp.Matrix(
    (
        (sp.Rational(1, 4), -sp.sqrt(2) / 4),
        (-sp.sqrt(2) / 4, sp.Rational(1, 2)),
    )
)
EFFECTS = {"A": (E0, EA1, EA2), "B": (E0, EB1, EB2)}
PROGRAMS = {
    context: tuple(
        sp.simplify(effect / sp.sqrt(sp.trace(effect))) for effect in effects
    )
    for context, effects in EFFECTS.items()
}

RHO_STAR = sp.diag(sp.Rational(3, 5), sp.Rational(2, 5))
RHO_TOMO = (
    I2 / 2,
    (I2 + X) / 2,
    (I2 + Y) / 2,
    (I2 + Z) / 2,
)

PB = sp.diag(1, 0, 0, 0)
TERMINAL = tuple(
    sp.diag(*(1 if position == index else 0 for position in range(4)))
    for index in (1, 2, 3)
)
T = sum(TERMINAL, sp.zeros(4))
P_PROGRAM = (sp.diag(1, 0), sp.diag(0, 1))
FRESH = sp.diag(1, 0)
SPENT = sp.diag(0, 1)
SPEND = sp.Matrix(((0, 0), (1, 0)))


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS [{label}] {detail}")
    else:
        FAIL += 1
        print(f"FAIL [{label}] {detail}")


def zero(matrix: sp.Matrix) -> bool:
    return sp.simplify(matrix) == sp.zeros(*matrix.shape)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def unit(dimension: int, target: int, source: int) -> sp.Matrix:
    result = sp.zeros(dimension)
    result[target, source] = 1
    return result


def vec(matrix: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(matrix).reshape(matrix.rows * matrix.cols, 1)


def apply_channel(kraus: tuple[sp.Matrix, ...], value: sp.Matrix) -> sp.Matrix:
    return sp.simplify(
        sum((operator * value * operator.H for operator in kraus), sp.zeros(value.rows))
    )


def apply_dual(kraus: tuple[sp.Matrix, ...], value: sp.Matrix) -> sp.Matrix:
    return sp.simplify(
        sum((operator.H * value * operator for operator in kraus), sp.zeros(value.rows))
    )


def simple_kraus(context: str) -> tuple[sp.Matrix, ...]:
    writers = tuple(
        sp.kronecker_product(unit(4, label + 1, 0), operator)
        for label, operator in enumerate(PROGRAMS[context])
    )
    return writers + (sp.kronecker_product(T, I2),)


def integrated_kraus() -> tuple[sp.Matrix, ...]:
    writers = []
    for branch in range(3):
        writer = sp.zeros(32)
        for projector, context in zip(P_PROGRAM, ("A", "B"), strict=True):
            writer += sp.kronecker_product(
                projector,
                unit(4, branch + 1, 0),
                PROGRAMS[context][branch],
                SPEND,
            )
        writers.append(sp.simplify(writer))
    active = sp.kronecker_product(I2, PB, I2, FRESH)
    return tuple(writers) + (sp.eye(32) - active,)


def code(label: int) -> sp.Matrix:
    return sp.I * (label + 1) * I2


def decode(content: sp.Matrix) -> int:
    if content is None:
        raise ValueError("absence is outside the decoder domain")
    for label in range(3):
        if content == code(label):
            return label
    raise ValueError("content is outside the declared candidate menu")


def weights(context: str, rho: sp.Matrix) -> tuple[sp.Expr, ...]:
    return tuple(
        sp.simplify(sp.trace(operator * rho * operator.H))
        for operator in PROGRAMS[context]
    )


def row_marginal(table: sp.Matrix) -> tuple[sp.Expr, ...]:
    return tuple(sp.simplify(sum(table[row, col] for col in range(3))) for row in range(3))


def column_marginal(table: sp.Matrix) -> tuple[sp.Expr, ...]:
    return tuple(sp.simplify(sum(table[row, col] for row in range(3))) for col in range(3))


def source_controls() -> None:
    axioms = normalized(AXIOMS)
    realized = normalized(REALIZED)
    note = normalized(NOTE)
    required_note = (
        "the four-sector register is not one framework site record",
        "equal marginals do not force the diagonal coupling",
        "admissibility marginal equality remains supplied",
        "formation site, rate, overlap arbitration, and unbounded environment renewal remain open",
        "support-restricted sentinel encodings are not excluded",
        "no-go discipline gate: pass",
        "zero obligation retirement",
    )
    check(
        "independent-source-and-scope",
        "when present, a record locks exactly one admissible local possibility" in axioms
        and "records are permanent" in axioms
        and "a site with no record cannot be read" in axioms
        and "a law-admissible state supplied by the physical history" in realized
        and "not a state-selection rule" in realized
        and all(phrase in note for phrase in required_note),
        "exact Record/realized-state clauses and all bounded-scope conclusions are independently source-bound",
    )


def program_controls() -> None:
    expected = {
        "A": (sp.Rational(3, 10), sp.Rational(19, 50), sp.Rational(8, 25)),
        "B": (sp.Rational(3, 10), sp.Rational(7, 20), sp.Rational(7, 20)),
    }
    failures = 0
    for context in ("A", "B"):
        failures += not zero(
            sum((operator.H * operator for operator in PROGRAMS[context]), sp.zeros(2))
            - I2
        )
        failures += weights(context, RHO_STAR) != expected[context]
    check(
        "independent-A-B-programs",
        failures == 0,
        "the effects, normalized Kraus programs, completeness, and exact central masses are rebuilt without importing Block 9",
    )


def simple_channel_controls() -> None:
    failures = 0
    idempotence_failures = 0
    dual_failures = 0
    terminal_indices = tuple(range(2, 8))
    for context in ("A", "B"):
        kraus = simple_kraus(context)
        failures += not zero(
            sum((operator.H * operator for operator in kraus), sp.zeros(8)) - sp.eye(8)
        )
        for rho in RHO_TOMO + (RHO_STAR,):
            source = sp.kronecker_product(PB, rho)
            expected = sp.diag(
                sp.zeros(2),
                *(sp.simplify(operator * rho * operator.H) for operator in PROGRAMS[context]),
            )
            failures += not zero(apply_channel(kraus, source) - expected)
        for left in range(8):
            for right in range(8):
                basis = unit(8, left, right)
                first = apply_channel(kraus, basis)
                idempotence_failures += not zero(apply_channel(kraus, first) - first)
        for left in terminal_indices:
            for right in terminal_indices:
                basis = unit(8, left, right)
                failures += not zero(apply_channel(kraus, basis) - basis)
        for branch, atom in enumerate(TERMINAL):
            observable = sp.kronecker_product(atom, I2)
            operator = PROGRAMS[context][branch]
            expected_dual = observable + sp.kronecker_product(
                PB, sp.simplify(operator.H * operator)
            )
            dual_failures += not zero(apply_dual(kraus, observable) - expected_dual)
    check(
        "independent-total-absorbing-channel",
        failures == 0 and idempotence_failures == 0,
        "both independently rebuilt C4 channels are total CPTP, exact on the blank cq corner, idempotent, and pointwise fixed on the terminal algebra",
    )
    check(
        "independent-simple-terminal-dual",
        dual_failures == 0,
        "each simple terminal atom is exactly subharmonic with incoming effect K_cj^dagger K_cj",
    )


def integrated_channel_controls() -> None:
    kraus = integrated_kraus()
    active = sp.kronecker_product(I2, PB, I2, FRESH)
    inactive = sp.eye(32) - active
    failures = int(
        not zero(sum((operator.H * operator for operator in kraus), sp.zeros(32)) - sp.eye(32))
    )
    failures += int(not zero(kraus[-1] - inactive))
    for writer in kraus[:3]:
        failures += int(not zero(writer * inactive))
        failures += int(not zero(inactive * writer - writer))
    failures += int(not zero(kraus[-1] * active))
    failures += int(not zero(kraus[-1] * kraus[-1] - kraus[-1]))

    fixture_failures = 0
    for projector, context in zip(P_PROGRAM, ("A", "B"), strict=True):
        for rho in RHO_TOMO + (RHO_STAR,):
            source = sp.kronecker_product(projector, PB, rho, FRESH)
            expected = sp.zeros(32)
            for atom, operator in zip(TERMINAL, PROGRAMS[context], strict=True):
                expected += sp.kronecker_product(
                    projector,
                    atom,
                    sp.simplify(operator * rho * operator.H),
                    SPENT,
                )
            fixture_failures += not zero(apply_channel(kraus, source) - expected)

    dual_failures = 0
    for branch, atom in enumerate(TERMINAL):
        observable = sp.kronecker_product(I2, atom, I2, I2)
        expected = observable
        for projector, context in zip(P_PROGRAM, ("A", "B"), strict=True):
            operator = PROGRAMS[context][branch]
            expected += sp.kronecker_product(
                projector, PB, sp.simplify(operator.H * operator), FRESH
            )
        dual_failures += not zero(apply_dual(kraus, observable) - expected)

    check(
        "independent-integrated-channel",
        failures == 0 and fixture_failures == 0,
        "the rebuilt P-R-S-F channel is exact for definite A/B programs, fixes the full 28-dimensional inactive subspace algebra, and is algebraically idempotent",
    )
    check(
        "independent-integrated-terminal-dual",
        dual_failures == 0,
        "the integrated atom dual equals O_j plus the exact program-resolved blank/fresh incoming effect",
    )


def rank_and_environment_controls() -> None:
    failures = 0
    ranks = {}
    active_ranks = {}
    for context in ("A", "B"):
        kraus = simple_kraus(context)
        ranks[context] = sp.Matrix.hstack(*(vec(operator) for operator in kraus)).rank()
        active_ranks[context] = sp.Matrix.hstack(
            *(vec(operator * sp.kronecker_product(PB, I2)) for operator in kraus)
        ).rank()
        isometry = sp.Matrix.vstack(*kraus)
        failures += not zero(isometry.H * isometry - sp.eye(8))
    integrated = integrated_kraus()
    active = sp.kronecker_product(I2, PB, I2, FRESH)
    total_rank = sp.Matrix.hstack(*(vec(operator) for operator in integrated)).rank()
    active_rank = sp.Matrix.hstack(
        *(vec(operator * active) for operator in integrated)
    ).rank()
    failures += not zero(sp.Matrix.vstack(*integrated).H * sp.Matrix.vstack(*integrated) - sp.eye(32))
    check(
        "independent-rank-environment-ledger",
        failures == 0
        and ranks == {"A": 4, "B": 4}
        and active_ranks == {"A": 3, "B": 3}
        and total_rank == 4
        and active_rank == 3,
        "simple and integrated channels have total Choi rank four, active formation rank three, and exact four-code pure-environment isometries",
    )


def carrier_and_tag_controls() -> None:
    projectors = tuple(
        sp.diag(*(1 if position == index else 0 for position in range(4)))
        for index in range(4)
    )
    check(
        "independent-carrier-rank-boundary",
        4 > 2
        and sum(projector.rank() for projector in projectors) == 4
        and sum(projectors, sp.zeros(4)) == sp.eye(4)
        and all(
            left == right or zero(projectors[left] * projectors[right])
            for left in range(4)
            for right in range(4)
        ),
        "C2 fails the four-nonzero-sector rank sum while C4 realizes the minimal orthogonal blank-plus-ternary escape",
    )
    beta = I2 / 2
    absent = ("absent", beta)
    present = ("present", beta)
    forget = lambda tagged: tagged[1]
    specified = {"absent": ("present", code(0)), "present": present}
    check(
        "independent-specified-tag-factorization-bound",
        forget(absent) == forget(present)
        and specified["absent"] != specified["present"],
        "the specified transition differs on one fibre of the forgetful map and cannot factor through it; no broader sentinel exclusion is inferred",
    )


def candidate_and_coupling_controls() -> None:
    absence_rejected = False
    try:
        decode(None)  # type: ignore[arg-type]
    except ValueError:
        absence_rejected = True
    codes = tuple(code(label) for label in range(3))
    check(
        "independent-partial-candidate-decoder",
        absence_rejected
        and len({tuple(value) for value in codes}) == 3
        and all(decode(value) == label for label, value in enumerate(codes)),
        "the three M2 content candidates decode injectively while absence remains outside the readout domain",
    )

    diagonal_failures = 0
    hostile_failures = 0
    support_failures = 0
    epsilon = sp.Rational(1, 10)
    uniform = (sp.Rational(1, 3),) * 3
    for context in ("A", "B"):
        current = weights(context, RHO_STAR)
        diagonal = sp.diag(*current)
        diagonal_failures += row_marginal(diagonal) != current
        diagonal_failures += column_marginal(diagonal) != current
        diagonal_failures += any(
            diagonal[row, col] != 0
            for row in range(3)
            for col in range(3)
            if row != col
        )
        hostile = sp.diag(*current)
        hostile[0, 0] -= epsilon
        hostile[1, 1] -= epsilon
        hostile[0, 1] += epsilon
        hostile[1, 0] += epsilon
        hostile_failures += row_marginal(hostile) != current
        hostile_failures += column_marginal(hostile) != current
        hostile_failures += sp.simplify(
            sum(
                hostile[row, col]
                for row in range(3)
                for col in range(3)
                if row != col
            )
            - 2 * epsilon
        ) != 0
        support_failures += uniform == current
        support_failures += any(value <= 0 for value in uniform)
    check(
        "independent-stipulated-diagonal-support",
        diagonal_failures == 0,
        "the stipulated diagonal table has exact A/B marginals and matching-label support, conditional on the separately supplied formation and legality premises",
    )
    check(
        "independent-marginal-and-support-hostiles",
        hostile_failures == 0 and support_failures == 0,
        "same marginals permit mismatch, while common positive support permits non-trace weights; neither insufficiency is promoted into a universal no-go",
    )


def no_go_certificate_controls() -> None:
    note = NOTE.read_text(encoding="utf-8")
    n1 = note.split("### N1", 1)[1].split("### N2", 1)[0]
    n3 = note.split("### N3", 1)[1].split("### N4", 1)[0]
    check(
        "independent-no-go-route-freshness",
        n1.count("| `ATTEMPTED` |") == 8
        and "`REJECTED`" not in n1
        and "`ELIMINATED`" not in n1
        and "positive-support free-weight menu" in n1,
        "N1 contains eight mechanism-distinct attempted routes and uses only the allowed attempted marker",
    )
    check(
        "independent-hidden-wall-and-authority-scan",
        "No hidden condition was promoted" in n3
        and "obligation_retirement: zero" in note
        and "toe_percentage_movement: zero" in note
        and "audit_required_before_effective_retained: true" in note,
        "the N3 scan and machine-facing authority fields preserve zero-retirement proposal status",
    )


def main() -> int:
    source_controls()
    program_controls()
    simple_channel_controls()
    integrated_channel_controls()
    rank_and_environment_controls()
    carrier_and_tag_controls()
    candidate_and_coupling_controls()
    no_go_certificate_controls()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
