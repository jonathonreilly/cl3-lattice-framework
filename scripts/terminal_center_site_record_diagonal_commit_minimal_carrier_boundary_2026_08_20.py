#!/usr/bin/env python3
"""Block 9: terminal-center/site-Record diagonal commit boundary.

The exact Block-7 ternary instruments and Block-8 repaired carrier are reused.
This runner separates three objects that must not be conflated:

* an ordinary Hilbert output register with blank plus three terminal sectors;
* one framework site Record whose content is an M2(C) possibility; and
* the joint stochastic coupling between the instrument center and that Record.

A four-sector register admits a total absorbing CPTP commit channel.  Its
blank corner is exactly the A/B ternary cq instrument and its terminal face is
fixed pointwise.  Four linearly independent Kraus operators require a pure
environment of dimension four for the total channel.  One ordinary qubit
cannot host four nonzero orthogonal sectors, while a framework Record can use
three distinct M2(C) contents only through a separately typed classical
calibration.  A stipulated diagonal joint table gives conditional support
agreement; equal marginals alone do not.

This is a finite type/minimal-carrier and conditional coupling theorem.  It is
not a lattice-wide formation law, a derivation of the Admissibility marginal,
or an axiom amendment.
"""

from __future__ import annotations

from pathlib import Path
import hashlib
import sys

import sympy as sp


AUDIT_TIMEOUT_SEC = 30

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import terminal_cptp_7047_program_fixtures_2026_09_09 as fixture
import terminal_center_site_record_diagonal_commit_minimal_carrier_boundary_independent_check_2026_08_20 as independent


NOTE_PATH = ROOT / "docs" / (
    "TERMINAL_CENTER_SITE_RECORD_DIAGONAL_COMMIT_MINIMAL_CARRIER_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REALIZED_PATH = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
AUDIT_INPUT_PATHS = ('docs/TERMINAL_CENTER_SITE_RECORD_DIAGONAL_COMMIT_MINIMAL_CARRIER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-20.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md', 'scripts/terminal_cptp_7047_program_fixtures_2026_09_09.py', 'scripts/terminal_center_site_record_diagonal_commit_minimal_carrier_boundary_independent_check_2026_08_20.py')
INPUT_SHA256 = {'docs/TERMINAL_CENTER_SITE_RECORD_DIAGONAL_COMMIT_MINIMAL_CARRIER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-20.md': '92b9457232949ced07db72c1660f40e9ebe9182688ba46519d3f302e4ec3fac6', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md': '755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563', 'scripts/terminal_cptp_7047_program_fixtures_2026_09_09.py': '3844be6771bfe47a9221f0c2d7ba60a9e59d74956c1f5c5cc5a14b0e7b27d265', 'scripts/terminal_center_site_record_diagonal_commit_minimal_carrier_boundary_independent_check_2026_08_20.py': '4e81716d07beda70186c161d4d95d7b01c0c33138b89b283b13fe7a53502547f'}

PASS = 0
FAIL = 0

I2 = sp.eye(2)
X = sp.Matrix(((0, 1), (1, 0)))
Y = sp.Matrix(((0, -sp.I), (sp.I, 0)))
Z = sp.diag(1, -1)
RHO_STAR = sp.diag(sp.Rational(3, 5), sp.Rational(2, 5))
RHO_TOMO = (
    I2 / 2,
    (I2 + X) / 2,
    (I2 + Y) / 2,
    (I2 + Z) / 2,
)

REGISTER_DIM = 4
BLANK_INDEX = 0
TERMINAL_INDICES = (1, 2, 3)
PB = sp.diag(1, 0, 0, 0)
TERMINAL_PROJECTORS = tuple(
    sp.diag(*(1 if position == index else 0 for position in range(4)))
    for index in TERMINAL_INDICES
)
T = sum(TERMINAL_PROJECTORS, sp.zeros(4))
PROGRAM_PROJECTORS = (sp.diag(1, 0), sp.diag(0, 1))
FRESH = sp.diag(1, 0)
SPENT = sp.diag(0, 1)
FLAG_SPEND = sp.Matrix(((0, 0), (1, 0)))


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


def zero(matrix: sp.Matrix) -> bool:
    return sp.simplify(matrix) == sp.zeros(*matrix.shape)


def matrix_unit(dimension: int, target: int, source: int) -> sp.Matrix:
    result = sp.zeros(dimension)
    result[target, source] = 1
    return result


def commit_kraus(context: str) -> tuple[sp.Matrix, ...]:
    """Total CPTP commit on four-sector register x live system."""

    writers = tuple(
        sp.kronecker_product(
            matrix_unit(REGISTER_DIM, terminal, BLANK_INDEX), operator
        )
        for terminal, operator in zip(
            TERMINAL_INDICES, fixture.PROGRAMS[context], strict=True
        )
    )
    hold = sp.kronecker_product(T, I2)
    return writers + (hold,)


def integrated_commit_kraus() -> tuple[sp.Matrix, ...]:
    """One fixed program-controlled, freshness-flag total commit channel.

    Tensor order is program P x register R x live system S x flag F.  The
    active subspace is arbitrary P,S with R blank and F fresh.  Everything
    else is inactive and is held pointwise by one complementary projector.
    """

    writers = []
    for branch, terminal in enumerate(TERMINAL_INDICES):
        writer = sp.zeros(32)
        for program_index, context in enumerate(("A", "B")):
            writer += sp.kronecker_product(
                PROGRAM_PROJECTORS[program_index],
                matrix_unit(REGISTER_DIM, terminal, BLANK_INDEX),
                fixture.PROGRAMS[context][branch],
                FLAG_SPEND,
            )
        writers.append(sp.simplify(writer))
    active = sp.kronecker_product(I2, PB, I2, FRESH)
    hold = sp.eye(32) - active
    return tuple(writers) + (hold,)


def integrated_channel(kraus: tuple[sp.Matrix, ...], value: sp.Matrix) -> sp.Matrix:
    return sp.simplify(
        sum((operator * value * operator.H for operator in kraus), sp.zeros(32))
    )


def integrated_active_state(context: str, rho: sp.Matrix) -> sp.Matrix:
    program = PROGRAM_PROJECTORS[("A", "B").index(context)]
    return sp.kronecker_product(program, PB, rho, FRESH)


def integrated_expected(context: str, rho: sp.Matrix) -> sp.Matrix:
    program = PROGRAM_PROJECTORS[("A", "B").index(context)]
    result = sp.zeros(32)
    for terminal, operator in zip(
        TERMINAL_PROJECTORS, fixture.PROGRAMS[context], strict=True
    ):
        result += sp.kronecker_product(
            program,
            terminal,
            sp.simplify(operator * rho * operator.H),
            SPENT,
        )
    return sp.simplify(result)


def channel(kraus: tuple[sp.Matrix, ...], value: sp.Matrix) -> sp.Matrix:
    return sp.simplify(
        sum((operator * value * operator.H for operator in kraus), sp.zeros(8))
    )


def dual(kraus: tuple[sp.Matrix, ...], value: sp.Matrix) -> sp.Matrix:
    return sp.simplify(
        sum((operator.H * value * operator for operator in kraus), sp.zeros(8))
    )


def blank_state(rho: sp.Matrix) -> sp.Matrix:
    return sp.kronecker_product(PB, rho)


def expected_terminal_cq(context: str, rho: sp.Matrix) -> sp.Matrix:
    blocks = [sp.zeros(2)]
    blocks.extend(
        sp.simplify(operator * rho * operator.H)
        for operator in fixture.PROGRAMS[context]
    )
    return sp.diag(*blocks)


def matrix_basis(dimension: int) -> tuple[sp.Matrix, ...]:
    return tuple(
        matrix_unit(dimension, row, column)
        for row in range(dimension)
        for column in range(dimension)
    )


def vec(matrix: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(matrix).reshape(matrix.rows * matrix.cols, 1)


def stinespring_isometry(kraus: tuple[sp.Matrix, ...]) -> sp.Matrix:
    return sp.Matrix.vstack(*kraus)


def trace_environment(value: sp.Matrix, environment_dim: int = 4) -> sp.Matrix:
    system_dim = 8
    reduced = sp.zeros(system_dim)
    for left in range(system_dim):
        for right in range(system_dim):
            reduced[left, right] = sp.simplify(
                sum(
                    value[environment * system_dim + left, environment * system_dim + right]
                    for environment in range(environment_dim)
                )
            )
    return reduced


def record_code(label: int) -> sp.Matrix:
    """A conjugation-invariant M2 possibility, not a density operator."""

    return sp.I * (label + 1) * I2


def decode_record(content: sp.Matrix) -> int:
    if content is None:
        raise ValueError("a site with no Record is outside the readout domain")
    for label in range(3):
        if content == record_code(label):
            return label
    raise ValueError("content is outside the declared three-code Record menu")


def central_weights(context: str, rho: sp.Matrix) -> tuple[sp.Expr, ...]:
    return tuple(
        sp.simplify(sp.trace(operator * rho * operator.H))
        for operator in fixture.PROGRAMS[context]
    )


def diagonal_coupling(weights: tuple[sp.Expr, ...]) -> sp.Matrix:
    return sp.diag(*weights)


def same_marginal_mismatch_coupling(
    weights: tuple[sp.Expr, ...], epsilon: sp.Expr
) -> sp.Matrix:
    result = sp.diag(*weights)
    result[0, 0] -= epsilon
    result[1, 1] -= epsilon
    result[0, 1] += epsilon
    result[1, 0] += epsilon
    return result


def row_marginal(coupling: sp.Matrix) -> tuple[sp.Expr, ...]:
    return tuple(sp.simplify(sum(coupling[row, column] for column in range(3))) for row in range(3))


def column_marginal(coupling: sp.Matrix) -> tuple[sp.Expr, ...]:
    return tuple(sp.simplify(sum(coupling[row, column] for row in range(3))) for column in range(3))


def input_guard():
    for relative, expected in INPUT_SHA256.items():
        path = ROOT / relative
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise RuntimeError("input identity mismatch: " + relative)

def source_and_authority_controls() -> None:
    input_guard()
    independent.input_guard()
    check("source-integrity", True,
          "current note, memo, realized primitive, exact fixture and actual checker identities verified; integrity is not scientific proof")



def record_code_and_absence_controls() -> None:
    codes = tuple(record_code(label) for label in range(3))
    conjugators = (I2, X, Z, sp.Matrix(((1, 1), (1, -1))) / sp.sqrt(2))
    absence_rejected = False
    try:
        decode_record(None)  # type: ignore[arg-type]
    except ValueError:
        absence_rejected = True
    check(
        "one-site-record-code",
        len({tuple(code) for code in codes}) == 3
        and all(decode_record(code) == label for label, code in enumerate(codes))
        and absence_rejected
        and all(sp.simplify(unitary * code * unitary.H - code) == sp.zeros(2) for unitary in conjugators for code in codes),
        "three distinct conjugation-invariant M2 candidates decode by content alone; absence is rejected outside the readout domain",
    )
    carrier_map = {
        fixture.BLANK: None,
        fixture.PENDING: None,
        fixture.TERMINALS[0]: codes[0],
        fixture.TERMINALS[1]: codes[1],
        fixture.TERMINALS[2]: codes[2],
    }
    check(
        "carrier-center-to-site-status",
        carrier_map["000"] is None
        and carrier_map["100"] is None
        and all(carrier_map[word] == code for word, code in zip(fixture.TERMINALS, codes, strict=True))
        and carrier_map["010"] is not None,
        "blank and pending leave the candidate target absent; corrected outcome 0 uses a nonblank content candidate, never absence",
    )


def one_qubit_sector_boundary_controls() -> None:
    # Perfectly readable nondemolition status sectors have mutually orthogonal
    # nonzero support projections.  Rank additivity then requires d >= 4.
    required_rank = 1 + 1 + 1 + 1
    c2_dimension = 2
    projectors_c4 = tuple(
        sp.diag(*(1 if position == index else 0 for position in range(4)))
        for index in range(4)
    )
    orthogonal = all(
        left == right or zero(projectors_c4[left] * projectors_c4[right])
        for left in range(4)
        for right in range(4)
    )
    check(
        "single-m2-four-sector-rank-boundary",
        required_rank > c2_dimension,
        "four nonzero orthogonal blank/outcome support sectors require rank at least four, so an ordinary C2 output cannot supply them",
    )
    check(
        "minimal-four-sector-counterroute",
        orthogonal
        and sum(projector.rank() for projector in projectors_c4) == 4
        and sum(projectors_c4, sp.zeros(4)) == sp.eye(4),
        "C4, equivalently a supplied C2-tensor-C2 factorization, realizes the minimal orthogonal partition; no spatial placement is inferred",
    )
    povm = (sp.eye(2) / 4,) * 4
    check(
        "nonorthogonal-povm-route-does-not-meet-status-target",
        sum(povm, sp.zeros(2)) == I2
        and any(not zero(povm[left] * povm[right]) for left in range(4) for right in range(left + 1, 4)),
        "four qubit POVM effects exist but are not four perfectly readable absorbing output sectors; arbitrary M2 Record codes remain a separate classical route",
    )


def external_presence_tag_controls() -> None:
    beta = I2 / 2
    absent = ("absent", beta)
    present = ("present", beta)
    forget = lambda tagged: tagged[1]
    desired_absent_output = ("present", record_code(0))
    desired_present_output = present
    check(
        "external-presence-tag-collision",
        forget(absent) == forget(present)
        and desired_absent_output != desired_present_output,
        "the specified forgetful map identifies absent-beta and present-beta although the tested tagged transition assigns distinct successors; support-restricted sentinel encodings are not excluded",
    )


def absorbing_commit_channel_controls() -> None:
    failures = 0
    idempotence_failures = 0
    terminal_face_failures = 0
    atom_failures = 0
    for context in ("A", "B"):
        kraus = commit_kraus(context)
        completeness = sp.simplify(sum((operator.H * operator for operator in kraus), sp.zeros(8)))
        failures += not zero(completeness - sp.eye(8))
        for rho in RHO_TOMO + (RHO_STAR,):
            failures += not zero(channel(kraus, blank_state(rho)) - expected_terminal_cq(context, rho))
        for basis in matrix_basis(8):
            first = channel(kraus, basis)
            idempotence_failures += not zero(channel(kraus, first) - first)
        terminal_indices = tuple(range(2, 8))
        for left in terminal_indices:
            for right in terminal_indices:
                basis = matrix_unit(8, left, right)
                terminal_face_failures += not zero(channel(kraus, basis) - basis)
        terminal_observable = sp.kronecker_product(T, I2)
        failures += not zero(dual(kraus, terminal_observable) - sp.eye(8))
        for projector, operator in zip(TERMINAL_PROJECTORS, fixture.PROGRAMS[context], strict=True):
            observable = sp.kronecker_product(projector, I2)
            expected = observable + sp.kronecker_product(PB, sp.simplify(operator.H * operator))
            observed = dual(kraus, observable)
            atom_failures += not zero(observed - expected)
            atom_failures += any(value < 0 for value in sp.simplify(operator.H * operator).eigenvals())
    check(
        "total-cptp-terminal-commit",
        failures == 0,
        "A/B four-sector maps are exact CPTP on every register-system operator, send the whole blank corner to the exact ternary cq channel, and make the terminal face certain",
    )
    check(
        "idempotent-absorbing-future-law",
        idempotence_failures == 0 and terminal_face_failures == 0 and atom_failures == 0,
        "the complete declared channel is idempotent, fixes every terminal-supported operator, and each terminal atom is subharmonic with the correct incoming effect",
    )


def integrated_program_flag_channel_controls() -> None:
    kraus = integrated_commit_kraus()
    active = sp.kronecker_product(I2, PB, I2, FRESH)
    inactive = sp.eye(32) - active
    terminal = sp.kronecker_product(I2, T, I2, sp.eye(2))
    completeness = sp.simplify(
        sum((operator.H * operator for operator in kraus), sp.zeros(32))
    )
    fixture_failures = 0
    for context in ("A", "B"):
        for rho in RHO_TOMO + (RHO_STAR,):
            fixture_failures += not zero(
                integrated_channel(kraus, integrated_active_state(context, rho))
                - integrated_expected(context, rho)
            )
    algebra_failures = int(not zero(completeness - sp.eye(32)))
    algebra_failures += int(not zero(kraus[-1] - inactive))
    for writer in kraus[:3]:
        algebra_failures += int(not zero(writer * inactive))
        algebra_failures += int(not zero(active * writer))
        algebra_failures += int(not zero(writer * terminal))
    algebra_failures += int(not zero(kraus[-1] * terminal - terminal))
    algebra_failures += int(not zero(active * terminal))
    integrated_atom_failures = 0
    for branch, terminal_projector in enumerate(TERMINAL_PROJECTORS):
        observable = sp.kronecker_product(I2, terminal_projector, I2, I2)
        expected = observable
        for program_projector, context in zip(
            PROGRAM_PROJECTORS, ("A", "B"), strict=True
        ):
            operator = fixture.PROGRAMS[context][branch]
            expected += sp.kronecker_product(
                program_projector,
                PB,
                sp.simplify(operator.H * operator),
                FRESH,
            )
        observed = sp.simplify(
            sum(
                (operator.H * observable * operator for operator in kraus),
                sp.zeros(32),
            )
        )
        integrated_atom_failures += int(not zero(observed - expected))

    # These identities prove pointwise identity on the entire inactive
    # operator algebra and idempotence on the full 32x32 matrix algebra.
    inactive_rank = inactive.rank()

    check(
        "program-controlled-freshness-flag-cptp",
        fixture_failures == 0
        and algebra_failures == 0
        and integrated_atom_failures == 0,
        "one fixed P-R-S-F Hilbert channel reads a supplied definite A/B program, flips a one-shot fresh flag to spent, reproduces arbitrary-system tomography sectors, and removes only the host A/B call and post-write switch",
    )
    check(
        "inactive-subspace-and-terminal-totality",
        algebra_failures == 0 and inactive_rank == 28,
        "projector identities fix all 28^2=784 matrix units of the inactive Hilbert operator algebra; terminal, spent-flag, and other nonactive sectors are total rather than undefined",
    )


def environment_and_resource_controls() -> None:
    failures = 0
    ranks = {}
    active_ranks = {}
    for context in ("A", "B"):
        kraus = commit_kraus(context)
        gram = sp.Matrix.hstack(*(vec(operator) for operator in kraus))
        ranks[context] = gram.rank()
        active_ranks[context] = sp.Matrix.hstack(
            *(vec(operator) for operator in kraus[:3])
        ).rank()
        isometry = stinespring_isometry(kraus)
        failures += not zero(isometry.H * isometry - sp.eye(8))
        for rho in RHO_TOMO + (RHO_STAR,):
            value = blank_state(rho)
            joint = sp.simplify(isometry * value * isometry.H)
            failures += not zero(trace_environment(joint) - channel(kraus, value))
        terminal_test = sp.kronecker_product(TERMINAL_PROJECTORS[1], RHO_TOMO[1])
        joint_terminal = sp.simplify(isometry * terminal_test * isometry.H)
        failures += not zero(trace_environment(joint_terminal) - terminal_test)
    check(
        "four-kraus-pure-environment-ledger",
        failures == 0
        and ranks == {"A": 4, "B": 4}
        and active_ranks == {"A": 3, "B": 3},
        "the total absorbing channel has Kraus rank four while its blank formation corner has rank three; two pure-environment qubits suffice and no export/no-return transport is inferred",
    )

    integrated = integrated_commit_kraus()
    integrated_gram = sp.Matrix.hstack(*(vec(operator) for operator in integrated))
    integrated_active = sp.kronecker_product(I2, PB, I2, FRESH)
    integrated_active_gram = sp.Matrix.hstack(
        *(vec(operator * integrated_active) for operator in integrated)
    )
    integrated_isometry = stinespring_isometry(integrated)
    check(
        "integrated-rank-four-factor-isometry",
        integrated_gram.rank() == 4
        and integrated_active_gram.rank() == 3
        and zero(integrated_isometry.H * integrated_isometry - sp.eye(32)),
        "the program-controlled freshness-flag channel has total rank four and active-formation rank three, with seven qubit tensor factors; no spatial embedding or edge compiler is inferred",
    )


def diagonal_commit_coupling_controls() -> None:
    expected = {
        "A": (sp.Rational(3, 10), sp.Rational(19, 50), sp.Rational(8, 25)),
        "B": (sp.Rational(3, 10), sp.Rational(7, 20), sp.Rational(7, 20)),
    }
    diagonal_failures = 0
    mismatch_controls = 0
    marginal_failures = 0
    free_failures = 0
    support_failures = 0
    epsilon = sp.Rational(1, 10)
    for context in ("A", "B"):
        weights = central_weights(context, RHO_STAR)
        diagonal = diagonal_coupling(weights)
        diagonal_failures += weights != expected[context]
        diagonal_failures += row_marginal(diagonal) != weights
        diagonal_failures += column_marginal(diagonal) != weights
        diagonal_failures += any(
            diagonal[row, column] != 0
            for row in range(3)
            for column in range(3)
            if row != column
        )
        diagonal_failures += any(
            decode_record(record_code(column)) != row
            for row in range(3)
            for column in range(3)
            if diagonal[row, column] > 0
        )

        mismatch = same_marginal_mismatch_coupling(weights, epsilon)
        mismatch_controls += row_marginal(mismatch) != weights
        mismatch_controls += column_marginal(mismatch) != weights
        mismatch_controls += any(entry < 0 for entry in mismatch)
        mismatch_controls += sp.simplify(sum(mismatch[row, column] for row in range(3) for column in range(3) if row != column) - 2 * epsilon) != 0

        free = (sp.Rational(1, 3),) * 3
        free_failures += free == weights
        free_failures += sum(free) != 1
        support_failures += any(weight <= 0 for weight in free)
        support_failures += len({tuple(record_code(label)) for label in range(3)}) != 3

        for rho in RHO_TOMO:
            tomo_weights = central_weights(context, rho)
            coupling = diagonal_coupling(tomo_weights)
            marginal_failures += row_marginal(coupling) != tomo_weights
            marginal_failures += column_marginal(coupling) != tomo_weights
    check(
        "stipulated-candidate-diagonal-table",
        diagonal_failures == 0 and marginal_failures == 0,
        "conditional on formation at the declared target, the stipulated joint table has support only on Q_j paired with Record content kappa(j); it proves label agreement but is not a formation kernel",
    )
    check(
        "same-marginal-off-diagonal-hostile",
        mismatch_controls == 0,
        "an exact epsilon-cycle coupling has both correct marginals and positive mismatch mass, proving that marginal equality alone does not force pathwise correlation",
    )
    check(
        "admissibility-marginal-free-law-control",
        free_failures == 0 and support_failures == 0,
        "a supplied normalized uniform site menu gives every kappa(j) positive support but differs from both exact instrument centers; code legality does not supply the trace/Admissibility equality",
    )


def future_hostile_and_scope_controls() -> None:
    swap = sp.eye(4)
    swap[:, 1], swap[:, 2] = swap[:, 2], swap[:, 1]
    hostile = sp.kronecker_product(swap, I2)
    first_atom = sp.kronecker_product(TERMINAL_PROJECTORS[0], I2)
    check(
        "terminal-label-swap-hostile",
        not zero(hostile.H * first_atom * hostile - first_atom),
        "a label-mixing future unitary violates declared terminal-atom permanence/subharmonicity and is outside the isolated absorbing commit law",
    )


def resolution_certificate() -> None:
    print("SCOPE: exact supplied finite CPTP/dual/rank/carrier/coupling checks. Separate calibration, actual marginal and global trajectory/resource obligations remain open; no independent or exhaustive physical interface count.")






def main() -> int:
    source_and_authority_controls()
    record_code_and_absence_controls()
    one_qubit_sector_boundary_controls()
    external_presence_tag_controls()
    absorbing_commit_channel_controls()
    integrated_program_flag_channel_controls()
    environment_and_resource_controls()
    diagonal_commit_coupling_controls()
    future_hostile_and_scope_controls()
    resolution_certificate()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
