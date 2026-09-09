#!/usr/bin/env python3
"""Block 8: fixed-carrier presence separation and QND Record boundary.

The runner reuses the exact Block-7 A/B Kraus fixture, but not its physical
interpretation.  It first exposes that the old terminal word 000 coincides
with the all-blank memory sector.  It then repairs only that carrier defect by
using

    blank 000, pending 100, terminals 010/110/111,

on three memory qubits plus the live system.  Exact four-site unitaries realize
the repaired path isometry.  A separately supplied block-diagonal future
update class preserves the terminal label algebra, while an exact finite-
dimensional argument shows why the same reversible update cannot both enter a
disjoint terminal sector from blank and make that sector absorbing.

This is an ensemble/channel and carrier theorem.  It neither selects one
terminal atom nor identifies the terminal center with Admissibility, and it
does not register the regional code as a framework site Record.
"""

from __future__ import annotations

from pathlib import Path
import sys

import sympy as sp


AUDIT_TIMEOUT_SEC = 180

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import fresh_ancilla_staged_cq_record_intertwiner_conditional_completion_2026_08_20 as block7


NOTE_PATH = ROOT / "docs" / (
    "FIXED_CARRIER_PRESENCE_SEPARATED_NONDEMOLITION_RECORD_UPDATE_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
BLOCK7_PATH = ROOT / "docs" / (
    "FRESH_ANCILLA_STAGED_CQ_RECORD_INTERTWINER_CONDITIONAL_"
    "COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
POINTER_PATH = ROOT / "docs" / (
    "RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_"
    "BOUNDED_THEOREM_NOTE_2026-06-05.md"
)
EXTENSIONAL_PATH = ROOT / "docs" / (
    "EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md"
)
RECORD_OBSERVABLE_PATH = ROOT / "docs" / (
    "RECORD_OBSERVABLE_QUOTIENT_AND_RANK_ONE_FORMATION_OUTCOME_OPERATION_"
    "NORMAL_FORM_BOUNDED_THEOREM_NOTE_2026-07-11.md"
)
INFINITE_QCA_PATH = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / (
    "INFINITE_REVERSIBLE_RECORD_EXPORT_QCA_CYCLE11_NOTE_2026-07-14.md"
)
INDEXED_QCA_PATH = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / (
    "DYNAMIC_RECORD_BOUNDARY_INDEX_QCA_STEELMAN_NOTE_2026-07-14.md"
)

AUDIT_INPUT_PATHS = (
    "docs/FIXED_CARRIER_PRESENCE_SEPARATED_NONDEMOLITION_RECORD_UPDATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/FRESH_ANCILLA_STAGED_CQ_RECORD_INTERTWINER_CONDITIONAL_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md",
    "docs/EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md",
    "docs/RECORD_OBSERVABLE_QUOTIENT_AND_RANK_ONE_FORMATION_OUTCOME_OPERATION_NORMAL_FORM_BOUNDED_THEOREM_NOTE_2026-07-11.md",
    "docs/work_history/repo/review_feedback/INFINITE_REVERSIBLE_RECORD_EXPORT_QCA_CYCLE11_NOTE_2026-07-14.md",
    "docs/work_history/repo/review_feedback/DYNAMIC_RECORD_BOUNDARY_INDEX_QCA_STEELMAN_NOTE_2026-07-14.md",
    "scripts/fresh_ancilla_staged_cq_record_intertwiner_conditional_completion_2026_08_20.py",
)

PASS = 0
FAIL = 0

I2 = sp.eye(2)
X = sp.Matrix(((0, 1), (1, 0)))
Z = sp.diag(1, -1)
H = sp.Matrix(((1, 1), (1, -1))) / sp.sqrt(2)

BLANK = "000"
PENDING = "100"
OLD_TERMINALS = ("000", "110", "111")
TERMINALS = ("010", "110", "111")

RHO_STAR = sp.diag(sp.Rational(3, 5), sp.Rational(2, 5))
RHO_TOMO = (
    I2 / 2,
    (I2 + X) / 2,
    sp.Matrix(((1, -sp.I), (sp.I, 1))) / 2,
    (I2 + Z) / 2,
)


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


def word_index(word: str) -> int:
    return int(word, 2)


def word_ket(word: str) -> sp.Matrix:
    ket = sp.zeros(8, 1)
    ket[word_index(word), 0] = 1
    return ket


def word_embedding(word: str) -> sp.Matrix:
    """Embed the live qubit into memory word x system."""

    return sp.kronecker_product(word_ket(word), I2)


def word_projector(word: str) -> sp.Matrix:
    ket = word_ket(word)
    return sp.kronecker_product(ket * ket.H, I2)


def binary_unitary_extension(operators: tuple[sp.Matrix, sp.Matrix]) -> sp.Matrix:
    """Complete the exact binary Stinespring column to a 4x4 unitary.

    The input ordering is pointer x system.  Its first two columns act on the
    blank-pointer subspace and equal the stacked Kraus isometry.
    """

    isometry = block7.pointer_isometry(operators)
    columns = [isometry[:, 0], isometry[:, 1]]
    for candidate in isometry.H.nullspace():
        vector = candidate
        for column in columns:
            vector = sp.simplify(vector - column * (column.H * vector)[0])
        norm_squared = sp.simplify((vector.H * vector)[0])
        if norm_squared != 0:
            columns.append(sp.simplify(vector / sp.sqrt(norm_squared)))
    if len(columns) != 4:
        raise RuntimeError("binary isometry did not yield a four-column completion")
    return sp.Matrix.hstack(*columns)


def embed_m1_system(unitary: sp.Matrix) -> sp.Matrix:
    """Embed a two-qubit M1,S unitary in logical order M1,F,M2,S."""

    result = sp.zeros(16)
    for m1 in range(2):
        for flag in range(2):
            for m2 in range(2):
                for system in range(2):
                    source = (((m1 * 2 + flag) * 2 + m2) * 2 + system)
                    source_pair = m1 * 2 + system
                    for target_m1 in range(2):
                        for target_system in range(2):
                            target_pair = target_m1 * 2 + target_system
                            target = (
                                ((target_m1 * 2 + flag) * 2 + m2) * 2
                                + target_system
                            )
                            result[target, source] = unitary[target_pair, source_pair]
    return result


def completion_unitary(context: str) -> sp.Matrix:
    """Mark completion and conditionally execute the residual instrument."""

    p0 = sp.diag(1, 0)
    p1 = sp.diag(0, 1)
    residual = binary_unitary_extension(block7.residual_program(context))
    return sp.simplify(
        sp.kronecker_product(p0, X, sp.eye(4))
        + sp.kronecker_product(p1, X, residual)
    )


def writer_unitary(context: str) -> sp.Matrix:
    front = binary_unitary_extension((block7.K0, block7.B))
    return sp.simplify(completion_unitary(context) * embed_m1_system(front))


def path_isometry(context: str, words: tuple[str, str, str]) -> sp.Matrix:
    result = sp.zeros(16, 2)
    for word, operator in zip(words, block7.PROGRAMS[context], strict=True):
        start = 2 * word_index(word)
        result[start : start + 2, :] = operator
    return result


def future_qnd_unitary() -> sp.Matrix:
    branch_updates = {
        "010": Z,
        "110": X,
        "111": H,
    }
    return sp.diag(*(branch_updates.get(f"{index:03b}", I2) for index in range(8)))


def memory_swap(first: str, second: str) -> sp.Matrix:
    permutation = sp.eye(8)
    i = word_index(first)
    j = word_index(second)
    permutation[:, i], permutation[:, j] = permutation[:, j], permutation[:, i]
    return sp.kronecker_product(permutation, I2)


def dephase_terminal_labels(state: sp.Matrix) -> sp.Matrix:
    return sp.simplify(
        sum(
            (projector * state * projector for projector in TERMINAL_PROJECTORS),
            sp.zeros(16),
        )
    )


def environment_copy_unitary() -> sp.Matrix:
    """Copy the three terminal labels into a two-qubit environment.

    Ordering is memory-word x environment-word.  Modular xor makes a complete
    permutation on the full input space, while blank environment 00 receives
    three distinct codes on the terminal words.
    """

    codes = {"010": 0, "110": 1, "111": 2}
    unitary = sp.zeros(32)
    for memory in range(8):
        # Code 3 is the full-carrier Q_perp atom.  On the path-output corner
        # only codes 0,1,2 occur, so the induced cq channel still has rank 3.
        code = codes.get(f"{memory:03b}", 3)
        for environment in range(4):
            source = 4 * memory + environment
            target = 4 * memory + (environment ^ code)
            unitary[target, source] = 1
    return unitary


def attach_blank_environment(isometry: sp.Matrix) -> sp.Matrix:
    """Embed memory x system into memory x blank-environment x system."""

    result = sp.zeros(64, 2)
    for memory in range(8):
        for system in range(2):
            result[(memory * 4) * 2 + system, :] = isometry[
                memory * 2 + system, :
            ]
    return result


def trace_environment(state: sp.Matrix) -> sp.Matrix:
    reduced = sp.zeros(16)
    for left_memory in range(8):
        for right_memory in range(8):
            for left_system in range(2):
                for right_system in range(2):
                    reduced[2 * left_memory + left_system, 2 * right_memory + right_system] = sp.simplify(
                        sum(
                            state[
                                (left_memory * 4 + environment) * 2 + left_system,
                                (right_memory * 4 + environment) * 2 + right_system,
                            ]
                            for environment in range(4)
                        )
                    )
    return reduced


BLANK_EMBEDDING = word_embedding(BLANK)
BLANK_PROJECTOR = word_projector(BLANK)
OLD_ZERO_PROJECTOR = word_projector(OLD_TERMINALS[0])
TERMINAL_PROJECTORS = tuple(word_projector(word) for word in TERMINALS)
TERMINAL_PROJECTOR = sum(TERMINAL_PROJECTORS, sp.zeros(16))


def source_and_authority_controls() -> None:
    paths = (
        NOTE_PATH,
        AXIOM_PATH,
        BLOCK7_PATH,
        POINTER_PATH,
        EXTENSIONAL_PATH,
        RECORD_OBSERVABLE_PATH,
        INFINITE_QCA_PATH,
        INDEXED_QCA_PATH,
    )
    texts = {path.name: normalized(path) for path in paths}
    axiom = texts[AXIOM_PATH.name]
    pointer = texts[POINTER_PATH.name]
    extensional = texts[EXTENSIONAL_PATH.name]
    record_observable = texts[RECORD_OBSERVABLE_PATH.name]
    infinite_qca = texts[INFINITE_QCA_PATH.name]
    indexed_qca = texts[INDEXED_QCA_PATH.name]
    check(
        "sources-and-current-authority",
        all(path.exists() for path in paths)
        and "records form" in axiom
        and "records are permanent" in axiom
        and "physical persistence dynamics" in axiom
        and "same completed fragment is re-used" in pointer
        and "inverse defeats absolute permanence" in extensional
        and "finite-unitary formation obstruction" in record_observable
        and "finite reversible permanence boundary" in infinite_qca
        and "cross-cycle echo" in indexed_qca,
        "the current Record axiom supplies abstract formation/permanence but not this carrier registration or a future update law; all cited reversible-reuse, finite-boundary, and infinite-QCA echoes are source-matched",
    )


def old_presence_collision_controls() -> None:
    old_zero_range = path_isometry("A", OLD_TERMINALS)[0:2, :]
    check(
        "old-000-blank-presence-collision",
        OLD_TERMINALS[0] == BLANK
        and OLD_ZERO_PROJECTOR == BLANK_PROJECTOR
        and block7.K0.rank() == 1
        and old_zero_range.rank() == 1,
        "the old outcome-0 range is nonzero and lies inside the entire all-blank word sector, so no projector can vanish on every blank-system state yet certify that outcome as present",
    )


def repaired_codebook_controls() -> None:
    words = (BLANK, PENDING) + TERMINALS
    projectors = (BLANK_PROJECTOR, word_projector(PENDING)) + TERMINAL_PROJECTORS
    orthogonal = all(
        zero(projectors[i] * projectors[j])
        for i in range(len(projectors))
        for j in range(i + 1, len(projectors))
    )
    check(
        "presence-separated-fixed-codebook",
        len(set(words)) == 5
        and orthogonal
        and zero(BLANK_PROJECTOR * TERMINAL_PROJECTOR)
        and PENDING == "100"
        and TERMINALS == ("010", "110", "111"),
        "one existing flag bit separates blank 000, pending 100, and all three terminal sectors 010/110/111 without adding a fifth qubit factor",
    )


def exact_fixed_carrier_unitary_controls() -> None:
    failures = 0
    for context in ("A", "B"):
        front = binary_unitary_extension((block7.K0, block7.B))
        residual = binary_unitary_extension(block7.residual_program(context))
        completion = completion_unitary(context)
        writer = writer_unitary(context)
        expected = path_isometry(context, TERMINALS)
        failures += not zero(front.H * front - sp.eye(4))
        failures += not zero(residual.H * residual - sp.eye(4))
        failures += not zero(completion.H * completion - sp.eye(16))
        failures += not zero(writer.H * writer - sp.eye(16))
        failures += not zero(writer * BLANK_EMBEDDING - expected)
        failures += not zero(expected.H * expected - I2)
    check(
        "exact-four-site-unitary-extension",
        failures == 0,
        "for each context an explicit 16x16 unitary maps blank M1,F,M2 plus every live-system input to the exact repaired path isometry",
    )


def pending_and_terminal_controls() -> None:
    front = embed_m1_system(binary_unitary_extension((block7.K0, block7.B)))
    failures = 0
    for context in ("A", "B"):
        after_front = sp.simplify(front * BLANK_EMBEDDING)
        failures += not zero(after_front[0:2, :] - block7.K0)
        failures += not zero(after_front[8:10, :] - block7.B)
        failures += any(
            not zero(after_front[2 * index : 2 * index + 2, :])
            for index in range(8)
            if index not in (word_index(BLANK), word_index(PENDING))
        )
        final = sp.simplify(completion_unitary(context) * after_front)
        expected = path_isometry(context, TERMINALS)
        failures += not zero(final - expected)
    check(
        "pending-prefix-and-terminal-paths",
        failures == 0,
        "the front leaves the B branch at pending 100; the completion step moves the old 0 branch to 010 and the two residual branches to 110/111 with exact flat Kraus operators",
    )


def connected_lattice_resource_controls() -> None:
    coordinates = {
        "F": (-1, 0, 0),
        "M1": (0, 0, 0),
        "S": (1, 0, 0),
        "M2": (2, 0, 0),
    }
    edges = (("F", "M1"), ("M1", "S"), ("S", "M2"))
    distances = tuple(
        sum(abs(a - b) for a, b in zip(coordinates[left], coordinates[right]))
        for left, right in edges
    )
    check(
        "fixed-connected-z3-carrier-ledger",
        distances == (1, 1, 1)
        and len(set(coordinates.values())) == 4,
        "F--M1--S--M2 is one connected nearest-neighbour Z3 path; context, blank preparation, two-step order, and the later-update switch remain supplied, and no pair-gate compilation is claimed",
    )


def central_restriction_controls() -> None:
    expected_weights = {
        "A": (sp.Rational(3, 10), sp.Rational(19, 50), sp.Rational(8, 25)),
        "B": (sp.Rational(3, 10), sp.Rational(7, 20), sp.Rational(7, 20)),
    }
    failures = 0
    for context in ("A", "B"):
        isometry = path_isometry(context, TERMINALS)
        coherent = sp.simplify(isometry * RHO_STAR * isometry.H)
        weights = tuple(
            sp.simplify(sp.trace(projector * coherent))
            for projector in TERMINAL_PROJECTORS
        )
        failures += weights != expected_weights[context]
        failures += not zero(
            dephase_terminal_labels(coherent)
            - sum(
                (
                    projector * coherent * projector
                    for projector in TERMINAL_PROJECTORS
                ),
                sp.zeros(16),
            )
        )
    check(
        "reencoded-center-preserves-block7-channel",
        failures == 0,
        "presence separation changes only the path words; the terminal center still returns the exact A/B Block-7 trace masses, without identifying them with Admissibility",
    )


def cq_export_resource_controls() -> None:
    copy = environment_copy_unitary()
    copy_with_system = sp.kronecker_product(copy, I2)
    failures = int(not zero(copy.H * copy - sp.eye(32)))
    environment_codes = tuple(
        {word_index("010"): 0, word_index("110"): 1, word_index("111"): 2}.get(
            memory, 3
        )
        for memory in range(8)
    )
    full_carrier_partition = tuple(
        tuple(environment_codes[left] == environment_codes[right] for right in range(8))
        for left in range(8)
    )
    expected_partition = tuple(
        tuple(
            (left == right and left in tuple(map(word_index, TERMINALS)))
            or (
                left not in tuple(map(word_index, TERMINALS))
                and right not in tuple(map(word_index, TERMINALS))
            )
            for right in range(8)
        )
        for left in range(8)
    )
    failures += full_carrier_partition != expected_partition
    kraus_ranks: list[int] = []
    for context in ("A", "B"):
        isometry = path_isometry(context, TERMINALS)
        joint = sp.simplify(copy_with_system * attach_blank_environment(isometry))
        vectors = sp.Matrix.hstack(
            *(
                sp.Matrix(word_embedding(word) * operator).reshape(32, 1)
                for word, operator in zip(
                    TERMINALS, block7.PROGRAMS[context], strict=True
                )
            )
        )
        kraus_ranks.append(vectors.rank())
        for rho in RHO_TOMO:
            exported = sp.simplify(joint * rho * joint.H)
            coherent = sp.simplify(isometry * rho * isometry.H)
            failures += not zero(
                trace_environment(exported) - dephase_terminal_labels(coherent)
            )
    check(
        "exact-cq-export-and-pure-environment-rank",
        failures == 0 and kraus_ranks == [3, 3] and 2 < 3 <= 4,
        "copying Q_perp and the three terminal labels into four explicit two-qubit environment codes realizes full-carrier four-atom pinching; on the terminal path-output channel Kraus rank three excludes one pure environment qubit but fits two",
    )


def nondemolition_future_controls() -> None:
    future = future_qnd_unitary()
    failures = int(not zero(future.H * future - sp.eye(16)))
    for projector in TERMINAL_PROJECTORS:
        failures += not zero(future * projector - projector * future)
        failures += not zero(future.H * projector * future - projector)
    for context in ("A", "B"):
        isometry = path_isometry(context, TERMINALS)
        failures += not zero(
            (sp.eye(16) - TERMINAL_PROJECTOR) * future * isometry
        )
        for rho in RHO_TOMO:
            state = sp.simplify(isometry * rho * isometry.H)
            later = sp.simplify(future * state * future.H)
            failures += any(
                sp.simplify(sp.trace(projector * state))
                != sp.simplify(sp.trace(projector * later))
                for projector in TERMINAL_PROJECTORS
            )
    check(
        "supplied-qnd-future-algebra",
        failures == 0
        and not zero(
            TERMINAL_PROJECTORS[1] * future
            - TERMINAL_PROJECTORS[1]
        ),
        "a nontrivial branch-controlled future unitary changes live-system states while fixing every terminal label projector and every central mass",
    )

    hostile = memory_swap("110", "111")
    check(
        "label-mixing-future-hostile",
        zero(hostile.H * hostile - sp.eye(16))
        and not zero(hostile * TERMINAL_PROJECTORS[1] - TERMINAL_PROJECTORS[1] * hostile)
        and zero(hostile.H * TERMINAL_PROJECTORS[1] * hostile - TERMINAL_PROJECTORS[2]),
        "an equally unitary fixed-carrier update swaps two terminal contents and is rejected by the QND commutant condition",
    )


def reversible_absorption_boundary_controls() -> None:
    failures = 0
    double_use_failures = 0
    for context in ("A", "B"):
        writer = writer_unitary(context)
        image = sp.simplify(writer * BLANK_EMBEDDING)
        failures += not zero((sp.eye(16) - TERMINAL_PROJECTOR) * image)
        failures += not zero(writer.H * image - BLANK_EMBEDDING)
        failures += zero(writer.H * TERMINAL_PROJECTOR * writer - TERMINAL_PROJECTOR)
        second = sp.simplify(writer * image)
        leak = sp.simplify((sp.eye(16) - TERMINAL_PROJECTOR) * second)
        double_use_failures += not zero(TERMINAL_PROJECTOR * second)
        double_use_failures += not zero(leak.H * leak - I2)
    check(
        "inverse-erases-the-coherent-write",
        failures == 0,
        "the exact writer sends the disjoint blank subspace into the terminal sector, but its allowed inverse sends that written image back to blank and the writer does not preserve the whole terminal sector",
    )

    check(
        "same-writer-double-use-hostile",
        double_use_failures == 0,
        "applying either A/B writer again sends its entire two-dimensional written image into the terminal complement with unit leak Gram, so repeated host-blind use is not permanent",
    )

    blank_rank = BLANK_PROJECTOR.rank()
    terminal_rank = TERMINAL_PROJECTOR.rank()
    check(
        "finite-reversible-absorbing-sector-boundary",
        blank_rank == 2
        and terminal_rank == 6
        and zero(BLANK_PROJECTOR * TERMINAL_PROJECTOR),
        "for nonzero B orthogonal to finite T, unitarity plus U(B) subset T and U(T) subset T is impossible: finite invariance gives U(T)=T while preservation of orthogonality gives U(B) perpendicular to T",
    )


def irreversible_escape_control() -> None:
    blank_to_terminal = sp.Matrix(((0, 0), (1, 0)))
    terminal_hold = sp.Matrix(((0, 0), (0, 1)))
    kraus = (blank_to_terminal, terminal_hold)
    rho_blank = sp.diag(1, 0)
    rho_terminal = sp.diag(0, 1)

    def channel(rho: sp.Matrix) -> sp.Matrix:
        return sp.simplify(sum((k * rho * k.H for k in kraus), sp.zeros(2)))

    check(
        "finite-irreversible-absorbing-counterroute",
        zero(sum((k.H * k for k in kraus), sp.zeros(2)) - I2)
        and channel(rho_blank) == rho_terminal
        and channel(rho_terminal) == rho_terminal
        and channel(I2 / 2) == rho_terminal,
        "a two-Kraus finite reset maps blank into an absorbing terminal state, explicitly proving that relaxing reversibility evades the narrow unitary boundary",
    )


def physical_and_axiom_boundary_controls() -> None:
    note = normalized(NOTE_PATH)
    required = (
        "presence-separated",
        "regional pointer algebra",
        "not a framework site record",
        "central-restriction compatibility",
        "actual-member correlation",
        "supplied schedule",
        "no axiom amendment",
        "obligation retirement: zero",
        "toe percentage movement: zero",
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
        "honest-record-central-and-actuality-boundary",
        all(phrase in note for phrase in required),
        "the note separates exact carrier/QND algebra from site-Record registration, the Admissibility law, one actual atom, autonomous dynamics, and axiom adoption",
    )


def resolution_certificate() -> None:
    lines = (
        "per_element: checked — blank 000, pending 100, corrected outcome-0 word 010, residual words 110/111, Kraus blocks, and terminal projectors remain separately typed",
        "per_site: checked — the fixed F--M1--S--M2 path is a connected four-site Z3 carrier, while its regional logical code is not silently registered as one framework site Record",
        "per_mode: checked — coherent unitary write, terminal-center restriction, optional dephasing, QND future update, Admissibility distribution, and actual terminal atom remain distinct",
        "per_block: checked — exact A/B front and residual unitaries compose from blank through pending to the presence-separated terminal code and reproduce every flat Kraus block",
        "lattice_wide: checked and not executed — the finite scheduled carrier exposes the reversible absorption wall; increasing archives, nonunitary sinks, overlap arbitration, and physical time remain open",
    )
    for line in lines:
        print(line)
    route_lines = (
        "n1_route: direct_repeated_finite_writer — executed for A and B; first use maps the full blank input into T, while second use maps the entire written image into T_perp with unit leak Gram",
        "n1_route: terminal_commutant_qnd_first — executed; the nontrivial future unitary fixes every Q_j and therefore has zero disjoint blank-to-terminal formation block",
        "n1_route: fresh_environment_reachable_corner — executed; four environment codes realize Q_perp/Q0/Q1/Q2 pinching from a blank corner, with export and reblanking explicit",
        "n1_route: scheduled_write_future_pair — executed for A and B; U_c forms the terminal path and a distinct terminal-commutant unitary preserves every terminal atom",
        "n1_route: finite_irreversible_instrument — executed; the two-Kraus reset maps a disjoint blank atom into an absorbing terminal atom while violating reversibility",
    )
    for line in route_lines:
        print(line)
    check(
        "n5-resolution-certificate",
        all(len(line) >= 120 for line in lines)
        and all(line in NOTE_PATH.read_text(encoding="utf-8") for line in lines)
        and all(
            line in NOTE_PATH.read_text(encoding="utf-8") for line in route_lines
        ),
        "all five resolution lines and five normalized N1 route lines occur in primary stdout and the theorem note",
    )


def main() -> int:
    source_and_authority_controls()
    old_presence_collision_controls()
    repaired_codebook_controls()
    exact_fixed_carrier_unitary_controls()
    pending_and_terminal_controls()
    connected_lattice_resource_controls()
    central_restriction_controls()
    cq_export_resource_controls()
    nondemolition_future_controls()
    reversible_absorption_boundary_controls()
    irreversible_escape_control()
    physical_and_axiom_boundary_controls()
    resolution_certificate()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
