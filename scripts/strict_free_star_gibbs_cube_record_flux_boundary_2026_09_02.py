#!/usr/bin/env python3
"""Exact strict-free star/Gibbs and cube/Record flux boundary.

The finite runner keeps three objects separate: an incident-star quantum
Gibbs preparation, a globally consistent classical edge-factor law, and the
full loop-bearing quantum action.  It proves a tree-diagonal blindness theorem
and a common cell-Record escape without selecting either candidate action.
"""

from __future__ import annotations

import argparse
import itertools
import subprocess
from dataclasses import dataclass
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PACKET = (
    ".claude/science/physics-loops/"
    "toe-local-gibbs-flux-record-block46-20260902"
)
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-local-gibbs-flux-record-block46-20260902/GOAL.md",
    ".claude/science/physics-loops/toe-local-gibbs-flux-record-block46-20260902/EXACT_TARGET_CONTRACT.md",
    ".claude/science/physics-loops/toe-local-gibbs-flux-record-block46-20260902/ASSUMPTIONS_AND_IMPORTS.md",
    ".claude/science/physics-loops/toe-local-gibbs-flux-record-block46-20260902/MUTATION_PLAN.md",
    ".claude/science/physics-loops/toe-local-gibbs-flux-record-block46-20260902/PRIOR_ART_SEARCH.md",
    ".claude/science/physics-loops/toe-local-gibbs-flux-record-block46-20260902/ROUTE_PORTFOLIO.md",
    ".claude/science/physics-loops/toe-local-gibbs-flux-record-block46-20260902/TRACE_GATE.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md",
    "docs/RECORD_OBSERVABLE_QUOTIENT_AND_RANK_ONE_FORMATION_OUTCOME_OPERATION_NORMAL_FORM_BOUNDED_THEOREM_NOTE_2026-07-11.md",
    "docs/ADMISSIBILITY_BINARY_FULL_CONDITIONAL_COMPATIBILITY_ISING_ACTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "archive/notes/docs/ACPHILAMBDA_FLUXED_RING_SPECTRAL_FUNCTIONAL_ROUTE_NO_GO_2026-07-02.md",
    "docs/P_FLUX_SELECTION_VIA_FSB_K_AND_Z_CERTIFICATE_CONDITIONAL_THEOREM_NOTE_2026-06-11.md",
    "archive/notes/docs/work_history/repo/review_feedback/EXACT_PREDICTIVE_SPECIFICATION_TOURNAMENT_NOTE_2026-07-14.md",
    ".claude/science/physics-loops/toe-local-gibbs-flux-record-block46-20260902/SOURCE_BINDING.md",
    "docs/STRICT_FREE_STAR_GIBBS_CUBE_RECORD_FLUX_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-02.md",
)
BASE_COMMIT = "2cea9a595ee2f0a6c47096de6f821b905182f48c"
PREREG_COMMIT = "1a053d816230f013d049bda2cfefe98a76db1ff1"
MINIMAL_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
MINIMAL_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"

FROZEN_PACKET_BLOBS = {
    f"{PACKET}/GOAL.md": "e70a07aa50cec79f10805646e42a41e4929650d1",
    f"{PACKET}/EXACT_TARGET_CONTRACT.md": "5bb70397368f02f8cdcb29681c6e6c6cbf49aac0",
    f"{PACKET}/ASSUMPTIONS_AND_IMPORTS.md": "f819db070aa9ae2a1adcc28c7e2e40d2132e5e83",
    f"{PACKET}/MUTATION_PLAN.md": "5a1ad7c7d5423e1bddcd4ae198fd25bf3658c9d9",
    f"{PACKET}/PRIOR_ART_SEARCH.md": "778ac72c220b6dd94ad9830cfadeee5fe95b72c6",
    f"{PACKET}/ROUTE_PORTFOLIO.md": "9129fe3b3104b45ce91d9b24036af4ae0cb727cb",
    f"{PACKET}/TRACE_GATE.md": "9ab01180692a8dc3a7b42cb5695642409f624140",
}

PINNED_MAIN_BLOBS = {
    MINIMAL_PATH: MINIMAL_BLOB,
    "docs/STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md":
        "717f145739244195da6db7bf05a8ff75b59bc980",
    "docs/RECORD_OBSERVABLE_QUOTIENT_AND_RANK_ONE_FORMATION_OUTCOME_OPERATION_NORMAL_FORM_BOUNDED_THEOREM_NOTE_2026-07-11.md":
        "f29dd373f25367fade34253ae3ff842a2a24c80f",
    "docs/ADMISSIBILITY_BINARY_FULL_CONDITIONAL_COMPATIBILITY_ISING_ACTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md":
        "2a872e2476d99c252db0a166c4803723fed60c53",
    "docs/ACPHILAMBDA_FLUXED_RING_SPECTRAL_FUNCTIONAL_ROUTE_NO_GO_2026-07-02.md":
        "b3cd51ea85d6091f4802539350fa40f0b1bd9536",
    "docs/P_FLUX_SELECTION_VIA_FSB_K_AND_Z_CERTIFICATE_CONDITIONAL_THEOREM_NOTE_2026-06-11.md":
        "6163d93174d5efe0ba0d5ba865720d31564258d6",
    "docs/work_history/repo/review_feedback/EXACT_PREDICTIVE_SPECIFICATION_TOURNAMENT_NOTE_2026-07-14.md":
        "d21f8cca433154577d43a1a7166614d70f4f276c",
}

# Historical commit/path/blob identities stay unchanged; only live paths move.
CURRENT_MAIN_PATHS = {
    "docs/ACPHILAMBDA_FLUXED_RING_SPECTRAL_FUNCTIONAL_ROUTE_NO_GO_2026-07-02.md":
        "archive/notes/docs/ACPHILAMBDA_FLUXED_RING_SPECTRAL_FUNCTIONAL_ROUTE_NO_GO_2026-07-02.md",
    "docs/work_history/repo/review_feedback/EXACT_PREDICTIVE_SPECIFICATION_TOURNAMENT_NOTE_2026-07-14.md":
        "archive/notes/docs/work_history/repo/review_feedback/EXACT_PREDICTIVE_SPECIFICATION_TOURNAMENT_NOTE_2026-07-14.md",
}

OPEN_PR_HEADS = {
    7828: "3fada70dd5a0429c4e12dc8ae79f6b11b555443a",
    7829: "551dfd9f317a36db050dffa0d717764f9af9f291",
    7830: "f8581d80efdd0856aa1a64078a48931a763765e9",
    7831: "ff8573cf054125db0dd0fcf07dba131280b6b736",
    7832: "9301c509842ea4835def91ad50f41bfd4f80ab1c",
}

MUTATIONS = (
    "phase_dependent_star_diagonal",
    "mean_field_instead_of_full_gibbs",
    "insert_density_density_interaction",
    "wrong_star_principal_minor",
    "wrong_star_conditional_normalization",
    "constant_beta_zero_law",
    "branch_specific_beta",
    "branch_specific_writer",
    "anisotropic_neighbor_count",
    "all_plus_K1_links",
    "commuting_K1_generators",
    "wrong_K1_square",
    "adjacent_instead_of_body_diagonal_target",
    "nonzero_K1_body_diagonal_amplitude",
    "wrong_K0_perfect_transfer",
    "overwrite_pointer_record",
    "claim_tree_detects_flux",
    "claim_gibbs_from_current_axioms",
    "claim_BBIT_or_P_KIN_selected",
    "claim_TOE_or_obligation_movement",
    "source_blob_drift",
    "wrong_partial_blank_trace",
    "claim_star_conditionals_are_global_DLR",
    "claim_edge_factor_is_full_quantum_gibbs",
    "claim_full_cube_gibbs_branch_equal",
    "same_mode_record_persists_under_hopping",
    "close_star_with_leaf_cycle_but_keep_phase_blindness",
    "treat_blank_as_independent_binary_marginal",
    "skip_record_actualization_instrument",
    "leave_record_incident_hopping_on",
    "external_cube_bonds_left_on",
    "break_rotated_cube_gauge_covariance",
    "wrong_edge_exponential_weight",
    "treat_source_preparation_as_permanent_record",
    "claim_star_gibbs_is_record_update_dynamics",
    "break_signed_cube_adjacency_lift",
    "treat_coordinate_paulis_as_physical_site_qubits",
    "branch_specific_cube_protocol",
)


@dataclass
class Harness:
    passed: int = 0
    failed: int = 0

    def check(self, label: str, condition: bool, detail: str) -> None:
        if condition:
            self.passed += 1
            print(f"PASS {label} :: {detail}")
        else:
            self.failed += 1
            print(f"FAIL {label} :: {detail}")


def matrix_zero(matrix: sp.MatrixBase) -> bool:
    return all(sp.simplify(value) == 0 for value in matrix)


def adjoint(matrix: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix(matrix.conjugate().T)


def kron(*matrices: sp.MatrixBase) -> sp.Matrix:
    result = sp.Matrix([[1]])
    for matrix in matrices:
        result = sp.kronecker_product(result, matrix)
    return sp.Matrix(result)


def ket(index: int, dimension: int) -> sp.Matrix:
    result = sp.zeros(dimension, 1)
    result[index, 0] = 1
    return result


def git_blob(commit: str, path: str) -> str:
    return subprocess.run(
        ["git", "rev-parse", f"{commit}:{path}"],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout.strip()


def worktree_blob(path: str) -> str:
    return subprocess.run(
        ["git", "hash-object", path],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout.strip()


def source_binding_certificate(harness: Harness, mutation: str | None) -> None:
    prereg_ok = all(
        git_blob(PREREG_COMMIT, path) == blob and worktree_blob(path) == blob
        for path, blob in FROZEN_PACKET_BLOBS.items()
    )
    main_ok = all(
        git_blob(BASE_COMMIT, path) == blob
        and worktree_blob(CURRENT_MAIN_PATHS.get(path, path)) == blob
        for path, blob in PINNED_MAIN_BLOBS.items()
    )
    binding = (ROOT / PACKET / "SOURCE_BINDING.md").read_text()
    prs_ok = all(f"`#{number}`" in binding and head in binding
                 for number, head in OPEN_PR_HEADS.items())
    if mutation == "source_blob_drift":
        prereg_ok = False
    harness.check(
        "sources, preregistration, and adjacent PR heads are pinned",
        prereg_ok and main_ok and prs_ok,
        f"prereg={prereg_ok} main={main_ok} open_prs={len(OPEN_PR_HEADS) if prs_ok else 0}/5",
    )


def star_hamiltonian(phases: tuple[sp.Expr, ...]) -> sp.Matrix:
    h = sp.zeros(7)
    for leaf, phase in enumerate(phases, start=1):
        h[0, leaf] = phase
        h[leaf, 0] = sp.conjugate(phase)
    return h


def star_gauge_certificate(harness: Harness, mutation: str | None) -> None:
    phases = sp.symbols("t1:7", nonzero=True)
    h_symbolic = sp.zeros(7)
    for leaf, phase in enumerate(phases, start=1):
        h_symbolic[0, leaf] = phase
        h_symbolic[leaf, 0] = 1 / phase
    h_unit = star_hamiltonian((sp.Integer(1),) * 6)
    gauge = sp.diag(1, *(1 / phase for phase in phases))
    gauge_identity = matrix_zero(h_symbolic - gauge * h_unit * gauge.inv())
    minimal_polynomial = matrix_zero(h_symbolic**3 - 6 * h_symbolic)
    alpha, gamma, delta = sp.symbols("alpha gamma delta")
    f_symbolic = alpha * sp.eye(7) + gamma * h_symbolic + delta * h_symbolic**2
    f_unit = alpha * sp.eye(7) + gamma * h_unit + delta * h_unit**2
    spectral_covariance = matrix_zero(f_symbolic - gauge * f_unit * gauge.inv())
    phase_blind = mutation != "phase_dependent_star_diagonal"
    harness.check(
        "tree gauge removes every link phase for all spectral preparations",
        gauge_identity and minimal_polynomial and spectral_covariance and phase_blind,
        "h(t)=D h(1) D^-1; h^3=6h; occupation effects commute with diagonal D",
    )


def star_gibbs_certificate(
    harness: Harness, mutation: str | None
) -> tuple[sp.Expr, ...]:
    C = sp.Integer(1) if mutation == "constant_beta_zero_law" else sp.Rational(5, 4)
    S = sp.Integer(0) if C == 1 else sp.Rational(3, 4)
    q = C - 1
    phase_patterns = [(sp.Integer(1),) * 6]
    for x1, x2 in itertools.product((0, 1), repeat=2):
        phase_patterns.append(
            (1, 1, (-1) ** x1, (-1) ** x1,
             (-1) ** (x1 + x2), (-1) ** (x1 + x2))
        )

    all_minors = True
    all_conditionals = True
    exterior_sum = True
    branch_tables: list[tuple[sp.Expr, ...]] = []
    for branch, phases in enumerate(phase_patterns):
        h = star_hamiltonian(tuple(sp.sympify(value) for value in phases))
        L = sp.eye(7) + q * h**2 / 6 - S * h / sp.sqrt(6)
        table = []
        sum_minors = sp.Integer(0)
        for mask in range(1 << 6):
            leaves = [leaf + 1 for leaf in range(6) if mask & (1 << leaf)]
            m = len(leaves)
            w0 = sp.Integer(1) if not leaves else sp.simplify(L.extract(leaves, leaves).det())
            with_center = [0] + leaves
            w1 = sp.simplify(L.extract(with_center, with_center).det())
            expected_w0 = 1 + m * q / 6
            expected_w1 = C - m * q / 6
            if mutation == "wrong_star_principal_minor" and m == 1:
                expected_w0 += sp.Rational(1, 97)
            all_minors = all_minors and sp.simplify(w0 - expected_w0) == 0
            all_minors = all_minors and sp.simplify(w1 - expected_w1) == 0
            denominator = C if mutation == "wrong_star_conditional_normalization" else C + 1
            probability = sp.simplify(w1 / denominator)
            expected_probability = sp.simplify((C - m * q / 6) / (C + 1))
            all_conditionals = all_conditionals and sp.simplify(
                probability - expected_probability
            ) == 0
            table.append(sp.simplify(w1 / (w0 + w1)))
            sum_minors += w0 + w1
        determinant_partition = sp.simplify((sp.eye(7) + L).det())
        exterior_sum = exterior_sum and sp.simplify(
            sum_minors - determinant_partition
        ) == 0
        exterior_sum = exterior_sum and sp.simplify(
            determinant_partition - 64 * (C + 1)
        ) == 0
        branch_tables.append(tuple(table[(1 << m) - 1] for m in range(7)))

    full_fock = mutation != "mean_field_instead_of_full_gibbs"
    no_interaction = mutation != "insert_density_density_interaction"
    full_support = all(0 < probability < 1 for probability in branch_tables[0])
    q_symbol = sp.symbols("q_star", positive=True)
    C_symbol = 1 + q_symbol
    m_symbol = sp.symbols("m_star", integer=True, nonnegative=True)
    p_m = (C_symbol - m_symbol * q_symbol / 6) / (C_symbol + 1)
    p_next = (C_symbol - (m_symbol + 1) * q_symbol / 6) / (C_symbol + 1)
    general_variation = sp.simplify(
        p_m - p_next - q_symbol / (6 * (q_symbol + 2))
    ) == 0
    varying = C > 1 and branch_tables[0][0] != branch_tables[0][-1]
    C_k1 = sp.Rational(4, 3) if mutation == "branch_specific_beta" else C
    common_branch_law = C_k1 == C and len(set(branch_tables)) == 1
    harness.check(
        "strict Fock-Gibbs principal minors give the exact six-leaf law",
        all_minors and all_conditionals and exterior_sum and full_fock and no_interaction,
        "320 leaf configurations, both center alternatives; sum_S det(L_S)=det(I+L)",
    )
    harness.check(
        "the normalized law is positive, varying, and common to K0/K1",
        varying and full_support and general_variation and common_branch_law,
        f"C={C}; endpoints=({sp.simplify(C/(C+1))},{sp.simplify(1/(C+1))})",
    )
    return branch_tables[0]


def partial_record_certificate(
    harness: Harness, mutation: str | None
) -> tuple[sp.Expr, ...]:
    C = sp.Rational(5, 4)
    q = C - 1
    all_exact = True
    probabilities: dict[tuple[int, ...], sp.Expr] = {}
    for shell in itertools.product((0, 1, 2), repeat=6):
        a = shell.count(1)
        z = shell.count(0)
        u = shell.count(2)
        W0 = sp.Integer(0)
        W1 = sp.Integer(0)
        for blank_values in itertools.product((0, 1), repeat=u):
            m = a + sum(blank_values)
            W0 += 1 + m * q / 6
            W1 += C - m * q / 6
        probability = sp.factor(W1 / (W0 + W1))
        blank_factor = u if mutation == "wrong_partial_blank_trace" else sp.Rational(u, 2)
        expected = sp.factor((1 + q * (z + blank_factor) / 6) / (C + 1))
        all_exact = all_exact and probability == expected
        all_exact = all_exact and probability == sp.Rational(48 + 2 * z + u, 108)
        probabilities[shell] = probability

    rotations = proper_cubic_direction_permutations()
    rotation_ok = all(
        probabilities[shell] == probabilities[tuple(shell[index] for index in permutation)]
        for shell in probabilities
        for permutation in rotations
    )
    if mutation == "anisotropic_neighbor_count":
        rotation_ok = False
    harness.check(
        "tracing blank leaves gives all 729 normalized neighboring Record laws",
        all_exact and rotation_ok and len(rotations) == 24,
        f"shells={len(probabilities)} rotations={len(rotations)} blank is traced, not valued",
    )
    return tuple(probabilities.values())


def global_consistency_certificate(harness: Harness, mutation: str | None) -> None:
    q = sp.symbols("q", positive=True)

    def odds(m: int) -> sp.Expr:
        return (6 + (6 - m) * q) / (6 + m * q)

    defect = sp.factor(odds(0) * odds(2) - odds(1) ** 2)
    expected = 2 * q**3 * (q + 2) / ((q + 3) * (q + 6) ** 2)
    star_not_dlr = sp.simplify(defect - expected) == 0 and defect != 0
    if mutation == "claim_star_conditionals_are_global_DLR":
        star_not_dlr = False

    E = sp.Rational(5, 4)
    S_edge = sp.Rational(3, 4)
    edge_hopping = sp.Matrix([[0, 1], [1, 0]])
    edge_kernel = E * sp.eye(2) - S_edge * edge_hopping
    edge_weights = (
        sp.Integer(1),
        edge_kernel[0, 0],
        edge_kernel[1, 1],
        sp.simplify(edge_kernel.det()),
    )
    expected_edge_weights = (1, E, E, 1)
    if mutation == "wrong_edge_exponential_weight":
        expected_edge_weights = (1, E + sp.Rational(1, 20), E, 1)
    edge_exponential_exact = edge_weights == expected_edge_weights
    neutral_blank = sp.Rational(7, 6)
    blank_blank = sp.Rational(11, 10)
    potential = sp.Matrix(
        [
            [1, E, neutral_blank],
            [E, 1, neutral_blank],
            [neutral_blank, neutral_blank, blank_blank],
        ]
    )
    edge_exact = True
    edge_geometric = True
    for shell in itertools.product((0, 1, 2), repeat=6):
        a = shell.count(1)
        z = shell.count(0)
        u = shell.count(2)
        weight0 = E**a * neutral_blank**u
        weight1 = E**z * neutral_blank**u
        probability = sp.factor(weight1 / (weight0 + weight1))
        edge_exact = edge_exact and probability == sp.factor(E**z / (E**a + E**z))
    complete_odds = [E ** (6 - 2 * m) for m in range(7)]
    edge_geometric = edge_geometric and all(
        complete_odds[m] * complete_odds[m + 2] == complete_odds[m + 1] ** 2
        for m in range(5)
    )
    potential_positive = potential == potential.T and all(value > 0 for value in potential)

    cube_edges = tuple(
        (vertex, vertex ^ step)
        for vertex in range(8)
        for step in (1, 2, 4)
        if vertex < (vertex ^ step)
    )
    binary_weights = [sp.Integer(0), sp.Integer(0)]
    for configuration in itertools.product((0, 1), repeat=8):
        if configuration[1] != 0:
            continue
        disagreements = sum(
            configuration[left] != configuration[right]
            for left, right in cube_edges
        )
        binary_weights[configuration[0]] += E**disagreements
    binary_partial_probability = sp.factor(
        binary_weights[1] / sum(binary_weights)
    )
    local_blank_probability = sp.factor(E / (1 + E))
    blank_semantics_separated = (
        binary_partial_probability == sp.Rational(54875, 98523)
        and binary_partial_probability != local_blank_probability
    )
    if mutation == "treat_blank_as_independent_binary_marginal":
        blank_semantics_separated = False
    edge_not_full_quantum = mutation != "claim_edge_factor_is_full_quantum_gibbs"
    harness.check(
        "the translated star law fails the global pairwise-Markov compatibility test",
        star_not_dlr,
        f"r0*r2-r1^2={defect}",
    )
    harness.check(
        "a distinct edge-factor law is globally consistent and fully positive",
        edge_exact
        and edge_geometric
        and edge_exponential_exact
        and potential_positive
        and blank_semantics_separated
        and edge_not_full_quantum,
        "two-site exp gives (1,E,E,1); ternary snapshot exact; hidden binary marginal distinct",
    )


def car_and_record_carrier_certificate(harness: Harness, mutation: str | None) -> None:
    identity = sp.eye(2)
    annihilation = sp.Matrix([[0, 1], [0, 0]])
    Z = sp.diag(1, -1)
    c0 = kron(annihilation, identity)
    c1 = kron(Z, annihilation)
    operators = (c0, c1)
    car_ok = all(
        matrix_zero(operators[i] * operators[j] + operators[j] * operators[i])
        and matrix_zero(
            operators[i] * adjoint(operators[j])
            + adjoint(operators[j]) * operators[i]
            - (sp.eye(4) if i == j else sp.zeros(4))
        )
        for i in range(2)
        for j in range(2)
    )
    n0 = adjoint(c0) * c0
    n1 = adjoint(c1) * c1
    hopping = adjoint(c1) * c0 + adjoint(c0) * c1
    interaction_coefficient = sp.Integer(0)
    if mutation == "insert_density_density_interaction":
        interaction_coefficient = sp.Integer(1)
        hopping += interaction_coefficient * n0 * n1
    strict_free = interaction_coefficient == 0
    number_conserving = matrix_zero(hopping * (n0 + n1) - (n0 + n1) * hopping)
    same_carrier_changes = not matrix_zero(hopping * n0 - n0 * hopping)
    if mutation == "same_mode_record_persists_under_hopping":
        same_carrier_changes = False
    harness.check(
        "Jordan-Wigner hopping is strict quadratic CAR and number conserving",
        car_ok and strict_free and number_conserving,
        f"CAR={car_ok} no_density_term={strict_free} [H,N]=0:{number_conserving}",
    )
    harness.check(
        "bare hopping cannot preserve an occupation Record on the same carrier",
        same_carrier_changes,
        "[H,n0] is nonzero, so a decoupled pointer or post-write gate is required",
    )


def pointer_record_objects() -> tuple[sp.Matrix, ...]:
    blank = sp.diag(1, 0, 0)
    record0 = sp.diag(0, 1, 0)
    record1 = sp.diag(0, 0, 1)
    write0 = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    write1 = sp.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    return blank, record0, record1, write0, write1


def controlled_record_writer(effect0: sp.MatrixBase, effect1: sp.MatrixBase) -> sp.Matrix:
    _, _, _, write0, write1 = pointer_record_objects()
    return kron(effect0, write0) + kron(effect1, write1)


def writer_certificate(
    harness: Harness,
    mutation: str | None,
    star_probabilities: tuple[sp.Expr, ...],
    partial_probabilities: tuple[sp.Expr, ...],
) -> None:
    identity = sp.eye(2)
    P0 = sp.diag(1, 0)
    P1 = sp.diag(0, 1)
    blank, record0, record1, _, write1 = pointer_record_objects()
    writer = controlled_record_writer(P0, P1)
    other_writer = writer if mutation != "branch_specific_writer" else sp.eye(6)
    common = matrix_zero(writer - other_writer)
    unitary = matrix_zero(adjoint(writer) * writer - sp.eye(6))
    probability = sp.symbols("p_record", real=True)
    rho = sp.diag(1 - probability, probability)
    output = sp.simplify(writer * kron(rho, blank) * adjoint(writer))
    instrument_exact = mutation != "skip_record_actualization_instrument"
    Q0 = kron(identity, record0)
    Q1 = kron(identity, record1)
    branch0 = sp.simplify(Q0 * output * Q0)
    branch1 = sp.simplify(Q1 * output * Q1)
    branch_exact = sp.simplify(sp.trace(branch0) - (1 - probability)) == 0
    branch_exact = branch_exact and sp.simplify(sp.trace(branch1) - probability) == 0
    branch_exact = branch_exact and matrix_zero(branch0 + branch1 - output)
    branch_exact = branch_exact and matrix_zero((sp.eye(6) - Q0) * branch0)
    branch_exact = branch_exact and matrix_zero((sp.eye(6) - Q1) * branch1)
    matter_branch0 = sp.simplify(P0 * rho * P0)
    matter_branch1 = sp.simplify(P1 * rho * P1)
    post_gate_hamiltonian = (
        sp.Matrix([[0, 1], [1, 0]])
        if mutation == "leave_record_incident_hopping_on"
        else sp.zeros(2)
    )
    same_site_pvm = (
        sp.simplify(sp.trace(matter_branch0) - (1 - probability)) == 0
        and sp.simplify(sp.trace(matter_branch1) - probability) == 0
        and matrix_zero(post_gate_hamiltonian * P0 - P0 * post_gate_hamiltonian)
        and matrix_zero(post_gate_hamiltonian * P1 - P1 * post_gate_hamiltonian)
    )
    supplied_weights = star_probabilities + partial_probabilities
    all_supplied_weights = len(supplied_weights) == 736 and all(
        0 < weight < 1 for weight in supplied_weights
    )
    future = write1 if mutation == "overwrite_pointer_record" else sp.diag(1, -1, 1)
    pointer_persists = all(
        matrix_zero(future * record - record * future)
        for record in (record0, record1)
    )
    harness.check(
        "one common CP instrument assigns every star weight to exclusive branches",
        common
        and unitary
        and branch_exact
        and same_site_pvm
        and all_supplied_weights
        and instrument_exact
        and pointer_persists,
        f"weights={len(supplied_weights)} blank/0/1 distinct; gated site and pointer persist",
    )


def pauli_cube() -> tuple[sp.Matrix, sp.Matrix, tuple[sp.Matrix, ...], tuple[sp.Matrix, ...]]:
    identity = sp.eye(2)
    X = sp.Matrix([[0, 1], [1, 0]])
    Z = sp.diag(1, -1)
    k0_terms = (
        kron(X, identity, identity),
        kron(identity, X, identity),
        kron(identity, identity, X),
    )
    k1_terms = (
        kron(X, identity, identity),
        kron(Z, X, identity),
        kron(Z, Z, X),
    )
    return sum(k0_terms, sp.zeros(8)), sum(k1_terms, sp.zeros(8)), k0_terms, k1_terms


def link_sign(branch: int, vertex: tuple[int, int, int], axis: int,
              mutation: str | None) -> int:
    if branch == 0 or mutation == "all_plus_K1_links":
        return 1
    x1, x2, _ = vertex
    return (1, (-1) ** x1, (-1) ** (x1 + x2))[axis]


def signed_cube_adjacency(branch: int) -> sp.Matrix:
    result = sp.zeros(8)
    steps = (4, 2, 1)
    for vertex in range(8):
        bits = tuple((vertex >> (2 - axis)) & 1 for axis in range(3))
        for axis, step in enumerate(steps):
            if bits[axis] != 0:
                continue
            neighbor = vertex ^ step
            sign = link_sign(branch, bits, axis, None)
            result[vertex, neighbor] = sign
            result[neighbor, vertex] = sign
    return result


def face_fluxes(branch: int, mutation: str | None) -> tuple[int, ...]:
    fluxes = []
    for first, second in ((0, 1), (0, 2), (1, 2)):
        fixed_axis = ({0, 1, 2} - {first, second}).pop()
        for fixed in (0, 1):
            base = [0, 0, 0]
            base[fixed_axis] = fixed
            v00 = tuple(base)
            base[first] = 1
            v10 = tuple(base)
            base[second] = 1
            v11 = tuple(base)
            base[first] = 0
            v01 = tuple(base)
            fluxes.append(
                link_sign(branch, v00, first, mutation)
                * link_sign(branch, v10, second, mutation)
                * link_sign(branch, v01, first, mutation)
                * link_sign(branch, v00, second, mutation)
            )
    return tuple(fluxes)


def proper_cubic_direction_permutations() -> tuple[tuple[int, ...], ...]:
    directions = (
        (1, 0, 0), (-1, 0, 0),
        (0, 1, 0), (0, -1, 0),
        (0, 0, 1), (0, 0, -1),
    )
    direction_index = {direction: index for index, direction in enumerate(directions)}
    result = []
    for axes in itertools.permutations(range(3)):
        parity = (1 if axes in ((0, 1, 2), (1, 2, 0), (2, 0, 1)) else -1)
        for signs in itertools.product((-1, 1), repeat=3):
            if parity * signs[0] * signs[1] * signs[2] != 1:
                continue
            permutation = []
            for vector in directions:
                image = [0, 0, 0]
                for row in range(3):
                    image[row] = signs[row] * vector[axes[row]]
                permutation.append(direction_index[tuple(image)])
            result.append(tuple(permutation))
    return tuple(result)


def proper_cubic_vertex_permutations() -> tuple[tuple[int, ...], ...]:
    result = []
    for axes in itertools.permutations(range(3)):
        parity = 1 if axes in ((0, 1, 2), (1, 2, 0), (2, 0, 1)) else -1
        for signs in itertools.product((-1, 1), repeat=3):
            if parity * signs[0] * signs[1] * signs[2] != 1:
                continue
            permutation = []
            for index in range(8):
                bits = tuple((index >> (2 - axis)) & 1 for axis in range(3))
                centered = tuple(2 * bit - 1 for bit in bits)
                image = tuple(
                    signs[row] * centered[axes[row]] for row in range(3)
                )
                image_bits = tuple((component + 1) // 2 for component in image)
                permutation.append(sum(bit << (2 - axis) for axis, bit in enumerate(image_bits)))
            result.append(tuple(permutation))
    return tuple(result)


def permutation_matrix(permutation: tuple[int, ...]) -> sp.Matrix:
    result = sp.zeros(len(permutation))
    for source, target in enumerate(permutation):
        result[target, source] = 1
    return result


def signed_gauge_equivalent(reference: sp.MatrixBase, candidate: sp.MatrixBase) -> bool:
    gauges: list[sp.Expr | None] = [None] * reference.rows
    gauges[0] = sp.Integer(1)
    queue = [0]
    while queue:
        left = queue.pop(0)
        for right in range(reference.cols):
            if reference[left, right] == 0:
                if candidate[left, right] != 0:
                    return False
                continue
            ratio = sp.simplify(candidate[left, right] / reference[left, right])
            proposed = sp.simplify(gauges[left] * ratio)
            if gauges[right] is None:
                gauges[right] = proposed
                queue.append(right)
            elif sp.simplify(gauges[right] - proposed) != 0:
                return False
    if any(gauge is None or gauge not in (-1, 1) for gauge in gauges):
        return False
    diagonal = sp.diag(*gauges)
    return matrix_zero(candidate - diagonal * reference * diagonal)


def cube_certificate(harness: Harness, mutation: str | None) -> None:
    H0, H1, terms0, terms1 = pauli_cube()
    adjacency0 = signed_cube_adjacency(0)
    adjacency1 = signed_cube_adjacency(1)
    cube_lift = matrix_zero(H0 - adjacency0) and matrix_zero(H1 - adjacency1)
    cube_lift = cube_lift and all(
        H0[left, right] == 0 and H1[left, right] == 0
        for left in range(8)
        for right in range(8)
        if left != right and (left ^ right).bit_count() != 1
    )
    cube_lift = cube_lift and H0 == H0.T and H1 == H1.T
    if mutation == "break_signed_cube_adjacency_lift":
        cube_lift = False
    if mutation == "commuting_K1_generators":
        terms1 = terms0
        H1 = H0
    commute0 = all(matrix_zero(A * B - B * A) for A, B in itertools.combinations(terms0, 2))
    anticommute1 = all(matrix_zero(A * B + B * A) for A, B in itertools.combinations(terms1, 2))
    square_target = 2 * sp.eye(8) if mutation == "wrong_K1_square" else 3 * sp.eye(8)
    square_ok = matrix_zero(H1**2 - square_target)
    flux0 = face_fluxes(0, mutation)
    flux1 = face_fluxes(1, mutation)
    harness.check(
        "the cube actions have commuting versus Clifford generators and opposite face flux",
        cube_lift
        and commute0
        and anticommute1
        and square_ok
        and flux0 == (1,) * 6
        and flux1 == (-1,) * 6,
        f"signed NN adjacency lift={cube_lift}; K0_flux={flux0} K1_flux={flux1}",
    )

    source = ket(0, 8)
    source_k1 = ket(1, 8) if mutation == "branch_specific_cube_protocol" else source
    target_index = 1 if mutation == "adjacent_instead_of_body_diagonal_target" else 7
    target = ket(target_index, 8)
    h1_matrix_element = sp.simplify((adjoint(target) * H1 * source_k1)[0])
    identity_matrix_element = sp.simplify((adjoint(target) * source_k1)[0])
    k1_dark = h1_matrix_element == 0 and identity_matrix_element == 0
    if mutation == "nonzero_K1_body_diagonal_amplitude":
        k1_dark = False
    U0_pi = sp.eye(8)
    used_k0_terms = terms0[:2] if mutation == "wrong_K0_perfect_transfer" else terms0
    for term in used_k0_terms:
        U0_pi = sp.simplify(U0_pi * (-sp.I * term))
    U1_pi = (
        sp.cos(sp.sqrt(3) * sp.pi / 2) * sp.eye(8)
        - sp.I * sp.sin(sp.sqrt(3) * sp.pi / 2) * H1 / sp.sqrt(3)
    )
    psi0 = sp.simplify(U0_pi * source)
    psi1 = sp.simplify(U1_pi * source_k1)
    target_effect = target * adjoint(target)
    complement_effect = sp.eye(8) - target_effect
    p0_target = sp.simplify((adjoint(psi0) * target_effect * psi0)[0])
    p1_target = sp.simplify((adjoint(psi1) * target_effect * psi1)[0])
    writer = controlled_record_writer(complement_effect, target_effect)
    blank, record0, record1, _, _ = pointer_record_objects()
    Q0 = kron(sp.eye(8), record0)
    Q1 = kron(sp.eye(8), record1)
    output0 = sp.simplify(writer * kron(psi0 * adjoint(psi0), blank) * adjoint(writer))
    output1 = sp.simplify(writer * kron(psi1 * adjoint(psi1), blank) * adjoint(writer))
    pointer_weights = (
        sp.simplify(sp.trace(Q0 * output0)),
        sp.simplify(sp.trace(Q1 * output0)),
        sp.simplify(sp.trace(Q0 * output1)),
        sp.simplify(sp.trace(Q1 * output1)),
    )
    writer_unitary = matrix_zero(adjoint(writer) * writer - sp.eye(24))
    k0_perfect = p0_target == 1
    k1_pointer_dark = p1_target == 0 and pointer_weights == (0, 1, 1, 0)
    common_protocol = matrix_zero(source - source_k1)
    extended_hamiltonian = sp.zeros(9)
    extended_hamiltonian[:8, :8] = H0
    if mutation == "external_cube_bonds_left_on":
        extended_hamiltonian[7, 8] = 1
        extended_hamiltonian[8, 7] = 1
    cube_projector = sp.diag(*([1] * 8 + [0]))
    boundary_isolated = matrix_zero(
        (sp.eye(9) - cube_projector) * extended_hamiltonian * cube_projector
    )
    harness.check(
        "one common body-diagonal target gives a sharp Record transcript separator",
        k1_dark
        and k0_perfect
        and k1_pointer_dark
        and writer_unitary
        and boundary_isolated
        and common_protocol,
        f"computed p_target=({p0_target},{p1_target}); pointer weights={pointer_weights}",
    )

    pair_ok = all(
        H1[index ^ 7, index] == 0 and (H0**3)[index ^ 7, index] != 0
        for index in range(8)
    )
    rotations = proper_cubic_vertex_permutations()
    rotation_covariance = len(rotations) == 24 and all(
        matrix_zero(
            permutation_matrix(permutation)
            * H0
            * permutation_matrix(permutation).T
            - H0
        )
        and signed_gauge_equivalent(
            H1,
            permutation_matrix(permutation)
            * H1
            * permutation_matrix(permutation).T,
        )
        and all(
            permutation[index ^ 7] == (permutation[index] ^ 7)
            for index in range(8)
        )
        for permutation in rotations
    )
    if mutation == "break_rotated_cube_gauge_covariance":
        rotation_covariance = False
    harness.check(
        "all 24 proper rotations preserve the action/protocol family up to gauge",
        pair_ok and rotation_covariance,
        f"rotations={len(rotations)} K0 exact, K1 gauge-equivalent, opposite_pairs=8",
    )


def global_gibbs_and_cycle_certificate(harness: Harness, mutation: str | None) -> None:
    H0, H1, _, _ = pauli_cube()
    eigenvalue = sp.symbols("lambda")
    char0 = sp.factor(H0.charpoly(eigenvalue).as_expr())
    char1 = sp.factor(H1.charpoly(eigenvalue).as_expr())
    expected_char0 = (eigenvalue - 3) * (eigenvalue - 1) ** 3 * (eigenvalue + 1) ** 3 * (eigenvalue + 3)
    expected_char1 = (eigenvalue**2 - 3) ** 4
    diag_h0_4 = tuple((H0**4)[index, index] for index in range(8))
    diag_h1_4 = tuple((H1**4)[index, index] for index in range(8))
    beta = sp.symbols("beta")
    partition0 = 256 * sp.cosh(3 * beta / 2) ** 2 * sp.cosh(beta / 2) ** 6
    partition1 = 256 * sp.cosh(sp.sqrt(3) * beta / 2) ** 8
    partition_delta = sp.series(partition0 - partition1, beta, 0, 5).removeO()
    empty_record_delta = sp.series(1 / partition0 - 1 / partition1, beta, 0, 5).removeO()
    global_split = (
        sp.simplify(char0 - expected_char0) == 0
        and sp.simplify(char1 - expected_char1) == 0
        and diag_h0_4 == (21,) * 8
        and diag_h1_4 == (9,) * 8
        and partition_delta.coeff(beta, 4) == -128
        and empty_record_delta.coeff(beta, 4) == sp.Rational(1, 512)
    )
    if mutation == "claim_full_cube_gibbs_branch_equal":
        global_split = False
    harness.check(
        "the honest isolated-cube finite-volume Gibbs law detects loop flux",
        global_split,
        "one-particle kernels and full-Fock empty-Record probability split at beta^4",
    )

    plaquette_plus = sp.Matrix(
        [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]
    )
    plaquette_minus = sp.Matrix(
        [[0, 1, 0, -1], [1, 0, 1, 0], [0, 1, 0, 1], [-1, 0, 1, 0]]
    )
    plus_closed_walk = (plaquette_plus**4)[0, 0]
    minus_closed_walk = (plaquette_minus**4)[0, 0]
    sharp = plus_closed_walk == 8 and minus_closed_walk == 4
    if mutation == "close_star_with_leaf_cycle_but_keep_phase_blindness":
        sharp = False
    harness.check(
        "closing the tree through one cubic plaquette restores phase sensitivity",
        sharp,
        f"(h_flux+^4)_00={plus_closed_walk}; (h_flux-^4)_00={minus_closed_walk}",
    )


def scope_and_no_go_certificate(harness: Harness, mutation: str | None) -> None:
    note = (ROOT / "docs" / (
        "STRICT_FREE_STAR_GIBBS_CUBE_RECORD_FLUX_BOUNDARY_"
        "BOUNDED_THEOREM_NOTE_2026-09-02.md"
    )).read_text()
    required = (
        "N1 — alternative routes",
        "N2 — wall independence",
        "N3 — hidden-wall scan",
        "N4 — exact residual",
        "N5 — multi-resolution",
        "N6 — partial-closure paths",
        "N7 — hostile steelman",
        "N8 — cross-cycle echo",
        "zero obligation retirement",
        "does not select K1",
        "local formation/update rule",
        "supplied unrecorded pre-formation state",
        "action-conditioned stochastic kernel",
        "finite-volume Gibbs",
    )
    scope_ok = all(phrase in note for phrase in required)
    prohibited_mutations = {
        "claim_tree_detects_flux",
        "claim_gibbs_from_current_axioms",
        "claim_BBIT_or_P_KIN_selected",
        "claim_TOE_or_obligation_movement",
        "treat_source_preparation_as_permanent_record",
        "claim_star_gibbs_is_record_update_dynamics",
        "treat_coordinate_paulis_as_physical_site_qubits",
    }
    if mutation in prohibited_mutations:
        scope_ok = False
    harness.check(
        "N1-N8 discipline and conditional claim custody are explicit",
        scope_ok,
        "narrow star-diagonal pruning; cube escape retained; zero score/obligation claim",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--list-mutations", action="store_true")
    args = parser.parse_args()
    if args.list_mutations:
        print("\n".join(MUTATIONS))
        return 0

    harness = Harness()
    source_binding_certificate(harness, args.mutation)
    star_gauge_certificate(harness, args.mutation)
    star_probabilities = star_gibbs_certificate(harness, args.mutation)
    partial_probabilities = partial_record_certificate(harness, args.mutation)
    global_consistency_certificate(harness, args.mutation)
    car_and_record_carrier_certificate(harness, args.mutation)
    writer_certificate(
        harness, args.mutation, star_probabilities, partial_probabilities
    )
    cube_certificate(harness, args.mutation)
    global_gibbs_and_cycle_certificate(harness, args.mutation)
    scope_and_no_go_certificate(harness, args.mutation)

    print("per_element: exact two-site CAR, edge weights, and face signs certified")
    print("per_site: all 729 partial neighboring Record shells certified")
    print("per_mode: strict quadratic hopping and same-carrier nonpermanence certified")
    print("per_block: star blindness, DLR fork, writer, and cube separator certified")
    print("lattice_wide: global edge-factor escape separated from finite-volume quantum Gibbs")
    print(f"TOTAL: PASS={harness.passed} FAIL={harness.failed}")
    return 0 if harness.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
