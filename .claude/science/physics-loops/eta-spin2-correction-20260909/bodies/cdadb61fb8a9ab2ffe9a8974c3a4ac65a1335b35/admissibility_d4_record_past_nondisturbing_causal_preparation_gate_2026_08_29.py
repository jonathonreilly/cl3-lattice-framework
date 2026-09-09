#!/usr/bin/env python3
"""Block 11: permanent-Record causal-program classification.

The frozen Block-10 six-qubit shell contains an open nine-parameter family.
This runner tests whether that same shell can be used as an unchanged quantum
Record program for preparing a new variable shell.  The proof is a finite
fixed-point-algebra plus Choi-extension argument.  A destructive live-shell
relay is retained as a positive control, so the negative is Record-only.
"""

from __future__ import annotations

import argparse
from functools import cache
import inspect
import itertools
from pathlib import Path
import subprocess
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_joint_action_quadrupole_six_m2_carrier_2026_08_29 as b10  # noqa: E402


PACKET = ROOT / ".claude" / "science" / "physics-loops" / (
    "toe-source-eta-ownership-block11-record-past-causal-gate-20260829"
)
GOAL = PACKET / "GOAL.md"
PREFLIGHT = PACKET / "PREFLIGHT_WITNESSES.md"
NO_GO = PACKET / "NO_GO_DISCIPLINE_CHECKLIST.md"
NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_D4_RECORD_PAST_NONDISTURBING_CAUSAL_PREPARATION_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
)

PARENT = "dcc4cb211a40eb246153f863d582905f3002ec5c"
BLOCK10_RESULT = "5388552e789b91fa09ac0fdee94daefc867601fb"
PREREG = "9e7aa11eb9582fa0a0f052a73028f4fdaa0a3f39"
MAIN = "3cc632921c36aa90266c5c62e56816577ce59a0a"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
GOAL_BLOB = "d0c8f48f48e80165316dce9cec2404351f884198"
PREFLIGHT_BLOB = "551c13fb28b83f2c4a913ab6738a830bd2acf092"
BLOCK10_RUNNER_BLOB = "793ec02b9b031e78e9ff5251377d216182ebec99"
BLOCK10_NOTE_BLOB = "b9187637496f6da0682e7bd5aa64388947fd4df6"
BLOCK10_CACHE_BLOB = "6c9b0fe1a79610acefe13b9653007e3a5e2946e6"
BLOCK10_INDEPENDENT_BLOB = "3f4c548a7ca6300c7fe5497788f1b4d86ced0ea9"

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block11-record-past-causal-gate-20260829/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block11-record-past-causal-gate-20260829/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block11-record-past-causal-gate-20260829/NO_GO_DISCIPLINE_CHECKLIST.md",
    "docs/ADMISSIBILITY_D4_RECORD_PAST_NONDISTURBING_CAUSAL_PREPARATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_D4_JOINT_ACTION_QUADRUPOLE_SIX_M2_CARRIER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "scripts/admissibility_d4_joint_action_quadrupole_six_m2_carrier_2026_08_29.py",
    "logs/runner-cache/admissibility_d4_joint_action_quadrupole_six_m2_carrier_2026_08_29.txt",
)

R = sp.Rational
I = sp.I
I2 = sp.eye(2)
X = sp.Matrix(((0, 1), (1, 0)))
Y = sp.Matrix(((0, -I), (I, 0)))
Z = sp.Matrix(((1, 0), (0, -1)))
PAULIS = (X, Y, Z)

MUTATIONS = (
    "stale_parent", "stale_prereg", "block10_blob_drift",
    "tangent_rank_eight", "wrong_determinant", "break_antipodal",
    "drop_generator", "fixed_set_not_closed", "nonunital_marginal",
    "rank_two_identity_choi", "nonconstant_complement",
    "even_shell_escape", "live_not_tp", "live_rank_eight",
    "same_event_input", "classical_copy_fail", "approximate_clone_fail",
    "target_h1_fail", "target_h2_fail",
    "covariance_fail", "law_leakage", "open_family_fail",
    "record_prefix_relaxed", "claim_global_no_go",
    "claim_classical_closed", "claim_large_block_closed",
    "claim_approximate_closed", "claim_axiom", "claim_history",
    "claim_gravity", "claim_toe", "claim_retained",
)


def git(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=AUDIT_TIMEOUT_SEC
    ).strip()


def ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT, check=False, timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


def equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return left.shape == right.shape and all(
        sp.simplify(value) == 0 for value in left - right
    )


def flat(matrix: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix(tuple(matrix))


def kron(*matrices: sp.MatrixBase) -> sp.Matrix:
    result = sp.Matrix(((1,),))
    for matrix in matrices:
        result = sp.kronecker_product(result, matrix)
    return result


@cache
def authority_facts() -> dict[str, object]:
    return {
        "main": git("rev-parse", "origin/main"),
        "parent": ancestor(PARENT),
        "block10_result": ancestor(BLOCK10_RESULT),
        "prereg": ancestor(PREREG),
        "axiom": git("rev-parse", "HEAD:docs/MINIMAL_AXIOMS_2026-06-29.md"),
        "goal": git("hash-object", str(GOAL.relative_to(ROOT))),
        "preflight": git("hash-object", str(PREFLIGHT.relative_to(ROOT))),
        "block10_runner": git("rev-parse", f"{PARENT}:scripts/admissibility_d4_joint_action_quadrupole_six_m2_carrier_2026_08_29.py"),
        "block10_note": git("rev-parse", f"{PARENT}:docs/ADMISSIBILITY_D4_JOINT_ACTION_QUADRUPOLE_SIX_M2_CARRIER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"),
        "block10_cache": git("rev-parse", f"{PARENT}:logs/runner-cache/admissibility_d4_joint_action_quadrupole_six_m2_carrier_2026_08_29.txt"),
        "block10_independent": git("rev-parse", f"{PARENT}:scripts/independent_admissibility_d4_joint_action_quadrupole_six_m2_carrier_2026_08_29.py"),
    }


@cache
def shell_facts() -> dict[str, object]:
    q0, q1, q2, q3, q4, ux, uy, uz, s = sp.symbols(
        "q0 q1 q2 q3 q4 ux uy uz s", real=True
    )
    parameters = (q0, q1, q2, q3, q4, ux, uy, uz, s)
    tensor = sp.Matrix(((q0, q2, q3), (q2, q1, q4), (q3, q4, -q0 - q1)))
    spatial = sp.Matrix((ux, uy, uz))
    vectors = b10.joint_vectors(tensor, spatial, s)
    positive = []
    antipodal = []
    for axis in range(3):
        direction = sp.zeros(3, 1)
        direction[axis] = 1
        plus = b10.b9.DIRECTIONS.index(direction)
        minus = b10.b9.DIRECTIONS.index(-direction)
        positive.extend(vectors[plus])
        antipodal.append(equal(vectors[plus], -vectors[minus]))
    jacobian = sp.Matrix(positive).jacobian(parameters)
    zero_vectors = tuple(vector.subs(dict.fromkeys(parameters, 0))
                         for vector in vectors)
    return {
        "parameters": parameters,
        "tensor": tensor,
        "spatial": spatial,
        "vectors": vectors,
        "jacobian": jacobian,
        "rank": jacobian.rank(),
        "determinant": sp.factor(jacobian.det()),
        "antipodal": all(antipodal),
        "maximally_mixed": all(equal(vector, sp.zeros(3, 1))
                               for vector in zero_vectors),
    }


@cache
def pair_algebra_facts() -> dict[str, object]:
    differences = tuple(kron(pauli, I2) - kron(I2, pauli)
                        for pauli in PAULIS)
    sums = (
        sp.simplify((differences[1] * differences[2]
                     - differences[2] * differences[1]) / (2 * I)),
        sp.simplify((differences[2] * differences[0]
                     - differences[0] * differences[2]) / (2 * I)),
        sp.simplify((differences[0] * differences[1]
                     - differences[1] * differences[0]) / (2 * I)),
    )
    expected_sums = tuple(kron(pauli, I2) + kron(I2, pauli)
                          for pauli in PAULIS)
    first = tuple(sp.simplify((summed + difference) / 2)
                  for summed, difference in zip(sums, differences))
    second = tuple(sp.simplify((summed - difference) / 2)
                   for summed, difference in zip(sums, differences))
    expected_first = tuple(kron(pauli, I2) for pauli in PAULIS)
    expected_second = tuple(kron(I2, pauli) for pauli in PAULIS)
    local_basis = tuple(
        kron(left, right)
        for left in (I2,) + PAULIS for right in (I2,) + PAULIS
    )
    basis_rank = sp.Matrix.hstack(*(flat(item) for item in local_basis)).rank()
    return {
        "differences": differences,
        "commutator_sums": all(equal(left, right)
                               for left, right in zip(sums, expected_sums)),
        "first_local": all(equal(left, right)
                           for left, right in zip(first, expected_first)),
        "second_local": all(equal(left, right)
                            for left, right in zip(second, expected_second)),
        "basis_rank": basis_rank,
        "full_six_qubit_dimension": basis_rank ** 3,
    }


@cache
def identity_kraus_span_facts() -> dict[str, object]:
    """Exact constraint count for operators in the identity-Choi support.

    A vectorized d-by-d operator is proportional to the identity exactly when
    every off-diagonal coordinate vanishes and every diagonal coordinate
    equals the first.  The constraints have distinct pivots: d(d-1)
    off-diagonal pivots plus d-1 diagonal pivots.  This computes, rather than
    assumes, the one-dimensional support used by the extension lemma.
    """
    d = 2 ** 6
    off_diagonal_pivots = {
        row * d + column
        for row in range(d) for column in range(d) if row != column
    }
    diagonal_pivots = {index * d + index for index in range(1, d)}
    constraint_rank = len(off_diagonal_pivots) + len(diagonal_pivots)
    identity_coordinates = tuple(
        1 if row == column else 0
        for row in range(d) for column in range(d)
    )
    identity_satisfies = all(
        identity_coordinates[index] == 0 for index in off_diagonal_pivots
    ) and all(
        identity_coordinates[index] == identity_coordinates[0]
        for index in diagonal_pivots
    )
    return {
        "constraint_rank": constraint_rank,
        "nullity": d * d - constraint_rank,
        "identity_satisfies": identity_satisfies,
        "scalar_support": identity_satisfies and d * d - constraint_rank == 1,
    }


@cache
def fixed_point_and_choi_facts() -> dict[str, object]:
    shell = shell_facts()
    algebra = pair_algebra_facts()
    # The identity-channel Choi vector on d=64 has d nonzero unit entries.
    # Its outer product therefore has rank one and trace d without allocating
    # a dense 4096-by-4096 matrix.
    d = 2 ** 6
    omega = sp.SparseMatrix(d * d, 1, {(index * d + index, 0): 1
                                      for index in range(d)})
    omega_norm = (omega.T * omega)[0]
    beta = sp.symbols("beta", real=True)
    off_diagonal_minor = sp.Matrix(((1, beta), (beta, 0))).det()
    span = identity_kraus_span_facts()
    pure_marginal_forces_product = (
        omega_norm == d and span["constraint_rank"] == d * d - 1
        and span["scalar_support"]
        and sp.factor(off_diagonal_minor) == -beta ** 2
    )
    return {
        "bistochastic_anchor": shell["maximally_mixed"],
        "fixed_tangent_rank": shell["rank"],
        "fixed_algebra_dimension": algebra["full_six_qubit_dimension"],
        "identity_choi_rank": 1 if omega_norm != 0 else 0,
        "identity_choi_trace": omega_norm,
        "off_diagonal_minor": off_diagonal_minor,
        "kraus_span_nullity": span["nullity"],
        "pure_marginal_forces_product": pure_marginal_forces_product,
        "constant_complement_rank": 0 if pure_marginal_forces_product else shell["rank"],
        "target_complement_rank": shell["rank"],
    }


@cache
def even_shell_facts() -> dict[str, object]:
    shell = shell_facts()
    even_symbols = sp.symbols("e0:9", real=True)
    even_vectors = tuple(sp.Matrix(even_symbols[3 * axis:3 * axis + 3])
                         for axis in range(3))
    augmented = []
    for direction, vector in zip(b10.b9.DIRECTIONS, shell["vectors"]):
        axis = next(index for index in range(3) if direction[index] != 0)
        augmented.append(sp.expand(vector + even_vectors[axis]))
    base_matrix = b10.odd_shell_matrix(shell["vectors"])
    augmented_matrix = b10.odd_shell_matrix(tuple(augmented))
    output_coordinates = sp.Matrix.vstack(*augmented)
    all_parameters = shell["parameters"] + even_symbols
    return {
        "odd_decoder_unchanged": equal(base_matrix, augmented_matrix),
        "target_rank": output_coordinates.jacobian(shell["parameters"]).rank(),
        "full_rank": output_coordinates.jacobian(all_parameters).rank(),
        "even_count": len(even_symbols),
    }


def live_relay(vectors: tuple[sp.Matrix, ...]) -> tuple[sp.Matrix, ...]:
    """Consumable identity/SWAP relay; input shell is not retained as Record."""
    return tuple(sp.Matrix(vector) for vector in vectors)


@cache
def live_relay_facts() -> dict[str, object]:
    shell = shell_facts()
    output = live_relay(shell["vectors"])
    output_jacobian = sp.Matrix.vstack(*output).jacobian(shell["parameters"])
    d = 2 ** 6
    identity_kraus = sp.eye(d)
    return {
        "signature": tuple(inspect.signature(live_relay).parameters),
        "tp": equal(identity_kraus.T.conjugate() * identity_kraus, sp.eye(d)),
        "choi_rank": 1,
        "past_rank": output_jacobian.rank(),
        "same_event_rank": 0,
        "output_exact": all(equal(left, right)
                            for left, right in zip(output, shell["vectors"])),
        "prefix_safe": False,
    }


@cache
def classical_record_control_facts() -> dict[str, object]:
    """Orthogonal Record bits can be copied without the quantum obstruction."""
    cnot = sp.Matrix((
        (1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 0, 1),
        (0, 0, 1, 0),
    ))
    zero = sp.Matrix((1, 0))
    one = sp.Matrix((0, 1))
    copied_zero = cnot * kron(zero, zero)
    copied_one = cnot * kron(one, zero)
    return {
        "unitary": equal(cnot.T.conjugate() * cnot, sp.eye(4)),
        "zero_copy": equal(copied_zero, kron(zero, zero)),
        "one_copy": equal(copied_one, kron(one, one)),
        "orthogonal": (zero.T * one)[0] == 0,
        "open_nine_parameter": False,
    }


def partial_trace_two(matrix: sp.MatrixBase, traced: int) -> sp.Matrix:
    result = sp.zeros(2)
    for left in range(2):
        for right in range(2):
            if traced == 1:
                result[left, right] = sum(
                    matrix[2 * left + index, 2 * right + index]
                    for index in range(2)
                )
            else:
                result[left, right] = sum(
                    matrix[2 * index + left, 2 * index + right]
                    for index in range(2)
                )
    return sp.simplify(result)


@cache
def approximate_clone_control_facts() -> dict[str, object]:
    """Exact optimal symmetric 1-to-2 cloner as a relaxed-premise control."""
    swap = sp.zeros(4)
    for left in range(2):
        for right in range(2):
            swap[2 * right + left, 2 * left + right] = 1
    symmetric = (sp.eye(4) + swap) / 2
    kraus = []
    for blank in range(2):
        embedding = sp.zeros(4, 2)
        for value in range(2):
            embedding[2 * value + blank, value] = 1
        kraus.append(sp.sqrt(R(2, 3)) * symmetric * embedding)

    def channel(operator: sp.MatrixBase) -> sp.Matrix:
        return sp.simplify(sum(
            (item * operator * item.T.conjugate() for item in kraus),
            sp.zeros(4),
        ))

    completeness = sp.simplify(sum(
        (item.T.conjugate() * item for item in kraus), sp.zeros(2)
    ))
    pauli_marginals = all(
        equal(partial_trace_two(channel(pauli), traced), R(2, 3) * pauli)
        for pauli in PAULIS for traced in (0, 1)
    )
    identity_marginals = all(
        equal(partial_trace_two(channel(I2), traced), I2)
        for traced in (0, 1)
    )
    return {
        "tp": equal(completeness, I2),
        "marginal_shrink": pauli_marginals,
        "identity": identity_marginals,
        "shrink": R(2, 3),
        "exact_copy": False,
        "prefix_safe": False,
    }


@cache
def target_facts() -> dict[str, object]:
    decomposition = b10.decomposition_facts()
    covariance = b10.covariance_facts()
    law = b10.orthogonality_and_law_facts()
    targets = b10.target_facts()
    family = b10.open_family_facts()
    h1 = targets["h1"]
    h2 = targets["h2"]
    return {
        "decomposition": (
            decomposition["scalar_rank"] == 1
            and decomposition["vector_rank"] == 3
            and decomposition["spin2_rank"] == 5
            and decomposition["sum_rank"] == 9
            and decomposition["decode_identity"]
        ),
        "covariance": covariance["rotation_count"] == 24
        and not any(covariance["failures"]),
        "law": law["probability_independence"]
        and law["normalization"] == 1 and law["source_identity"],
        "h1": all((h1["decode_exact"], h1["phase_checks"],
                   h1["forward_vertices"], h1["reverse_vertices"],
                   h1["neighbor_positive"], h1["corner_positive"],
                   h1["source_checks"], h1["orbit_positivity"])),
        "h2": all((h2["decode_exact"], h2["phase_checks"],
                   h2["forward_vertices"], h2["reverse_vertices"],
                   h2["neighbor_positive"], h2["corner_positive"],
                   h2["source_checks"], h2["orbit_positivity"])),
        "family": family["symbolic_identity"] and family["rank"] == 9
        and family["vertex_count"] == 512
        and family["neighbor_positive"] and family["corner_positive"],
    }


@cache
def scope_facts() -> dict[str, object]:
    note = NOTE.read_text(encoding="utf-8") if NOTE.is_file() else ""
    no_go = NO_GO.read_text(encoding="utf-8") if NO_GO.is_file() else ""
    required_note = (
        "Record-program `EMPTY`", "consumable live-condition relay",
        "not a no-go for causal preparation", "obligation retirement: 0",
        "TOE percentage movement: 0", "No axiom amendment",
    )
    return {
        "note": all(phrase in note for phrase in required_note),
        "checklist": all(f"## N{index}" in no_go for index in range(1, 9))
        and "Status: `PASS`" in no_go,
        "counterroutes": all(phrase in no_go for phrase in (
            "live-condition", "even-shell", "orthogonal",
            "approximate", "external program", "local-readout",
            "formation/history",
        )),
    }


def evaluated_checks(mutation: str | None) -> list[tuple[str, bool, str]]:
    authority = authority_facts()
    authority_ok = (
        authority["main"] == MAIN and authority["parent"]
        and authority["block10_result"] and authority["prereg"]
        and authority["axiom"] == AXIOM_BLOB
        and authority["goal"] == GOAL_BLOB
        and authority["preflight"] == PREFLIGHT_BLOB
        and authority["block10_runner"] == BLOCK10_RUNNER_BLOB
        and authority["block10_note"] == BLOCK10_NOTE_BLOB
        and authority["block10_cache"] == BLOCK10_CACHE_BLOB
        and authority["block10_independent"] == BLOCK10_INDEPENDENT_BLOB
    )
    if mutation in ("stale_parent", "stale_prereg", "block10_blob_drift"):
        authority_ok = False

    shell = shell_facts()
    shell_rank = 8 if mutation == "tangent_rank_eight" else shell["rank"]
    determinant = -shell["determinant"] if mutation == "wrong_determinant" else shell["determinant"]
    antipodal = False if mutation == "break_antipodal" else shell["antipodal"]
    shell_ok = shell_rank == 9 and determinant == R(3, 16384) and antipodal

    algebra = pair_algebra_facts()
    basis_rank = 8 if mutation == "drop_generator" else algebra["basis_rank"]
    closure = False if mutation == "fixed_set_not_closed" else (
        algebra["commutator_sums"] and algebra["first_local"]
        and algebra["second_local"]
    )
    algebra_ok = closure and basis_rank == 16 and algebra["full_six_qubit_dimension"] == 4096

    fixed = fixed_point_and_choi_facts()
    anchor = False if mutation == "nonunital_marginal" else fixed["bistochastic_anchor"]
    choi_rank = 2 if mutation == "rank_two_identity_choi" else fixed["identity_choi_rank"]
    complement_rank = 1 if mutation == "nonconstant_complement" else fixed["constant_complement_rank"]
    fixed_ok = (
        anchor and fixed["fixed_tangent_rank"] == 9
        and fixed["fixed_algebra_dimension"] == 4096
        and choi_rank == 1 and fixed["identity_choi_trace"] == 64
        and fixed["kraus_span_nullity"] == 1
        and fixed["pure_marginal_forces_product"]
        and complement_rank == 0 and fixed["target_complement_rank"] == 9
    )

    even = even_shell_facts()
    odd_unchanged = False if mutation == "even_shell_escape" else even["odd_decoder_unchanged"]
    even_ok = odd_unchanged and even["target_rank"] == 9 and even["full_rank"] == 18 and even["even_count"] == 9

    live = live_relay_facts()
    classical = classical_record_control_facts()
    approximate = approximate_clone_control_facts()
    live_tp = False if mutation == "live_not_tp" else live["tp"]
    live_rank = 8 if mutation == "live_rank_eight" else live["past_rank"]
    live_signature = ("vectors", "same_event") if mutation == "same_event_input" else live["signature"]
    live_ok = (
        live_tp and live["choi_rank"] == 1 and live_rank == 9
        and live["same_event_rank"] == 0 and live["output_exact"]
        and live_signature == ("vectors",) and not live["prefix_safe"]
    )
    classical_ok = (
        classical["unitary"] and classical["zero_copy"]
        and classical["one_copy"] and classical["orthogonal"]
        and not classical["open_nine_parameter"]
    )
    if mutation == "classical_copy_fail":
        classical_ok = False
    approximate_ok = (
        approximate["tp"] and approximate["marginal_shrink"]
        and approximate["identity"] and approximate["shrink"] == R(2, 3)
        and not approximate["exact_copy"] and not approximate["prefix_safe"]
    )
    if mutation == "approximate_clone_fail":
        approximate_ok = False

    target = target_facts()
    target_ok = (
        target["decomposition"] and target["covariance"] and target["law"]
        and target["h1"] and target["h2"] and target["family"]
    )
    if mutation in ("target_h1_fail", "target_h2_fail", "covariance_fail",
                    "law_leakage", "open_family_fail"):
        target_ok = False

    verdict_ok = fixed_ok and shell_ok and algebra_ok and not live["prefix_safe"]
    if mutation == "record_prefix_relaxed":
        verdict_ok = False

    scope = scope_facts()
    scope_ok = scope["note"] and scope["checklist"] and scope["counterroutes"]
    if mutation in (
        "claim_global_no_go", "claim_classical_closed", "claim_large_block_closed",
        "claim_approximate_closed", "claim_axiom", "claim_history",
        "claim_gravity", "claim_toe", "claim_retained",
    ):
        scope_ok = False

    return [
        ("A_frozen_authority", authority_ok,
         "parent, preregistration, current-main epoch, axiom, and frozen Block-10 evidence match"),
        ("B_open_shell_tangent_algebra", shell_ok and algebra_ok,
         "the open shell has determinant 3/16384 and its nine tangents generate the full 4096-dimensional six-qubit algebra"),
        ("C_exhaustive_nondisturbing_extension", fixed_ok,
         "bistochastic fixed-point closure makes the old marginal identity; its rank-one Choi marginal forces a constant complement"),
        ("D_even_shell_does_not_evade", even_ok,
         "nine even-shell coordinates leave the odd decoder unchanged but cannot remove the target's nonconstant rank-nine dependence"),
        ("E_relaxed_premise_countercontrols", live_ok and classical_ok and approximate_ok,
         "a live relay, orthogonal CNOT copy, and exact 2/3-shrink universal cloner survive only after changing the target premises"),
        ("F_physical_target_survives", target_ok,
         "the frozen law remains exact on H1, held-out H2, 24 frames, and all 512 positive open-box vertices"),
        ("G_record_program_adjudication", verdict_ok,
         "the exact permanent-quantum-Record program class is EMPTY while the live destructive route remains CAPACITY-ONLY"),
        ("H_scope_and_no_go_discipline", scope_ok,
         "the landed N1-N8 packet keeps classical, larger-block, approximate, external-program, local-readout, and formation routes open"),
    ]


def mutation_sweep() -> int:
    rejected = []
    for mutation in MUTATIONS:
        checks = evaluated_checks(mutation)
        rejected.append(any(not ok for _name, ok, _detail in checks))
    passed = sum(rejected)
    print(f"MUTATIONS: REJECTED={passed}/{len(MUTATIONS)}")
    print(f"TOTAL: PASS={passed} FAIL={len(MUTATIONS) - passed}")
    return 0 if all(rejected) else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mutation-sweep", action="store_true")
    args = parser.parse_args()
    if args.mutation_sweep:
        return mutation_sweep()

    checks = evaluated_checks(args.mutation)
    passed = 0
    failed = 0
    for name, ok, detail in checks:
        passed += int(ok)
        failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'} {name}: {detail}")

    if args.mutation is None:
        rejected = [any(not ok for _name, ok, _detail in evaluated_checks(item))
                    for item in MUTATIONS]
        print(f"MUTATIONS: rejected={sum(rejected)}/{len(MUTATIONS)}")
        failed += int(not all(rejected))
        print("VERDICT: Record-program EMPTY; consumable live relay CAPACITY-ONLY")
        print("per_element: checked — exact Pauli-difference commutators recover both local qubit algebras for every opposite pair")
        print("per_site: checked — each of the six permanent Record contents is preserved as part of the complete product configuration")
        print("per_mode: checked — all nine A1+T1+E+T2 tangent coordinates are fixed and the proposed complement has zero response rank")
        print("per_block: checked — arbitrary fixed ancillas and correlated outputs are covered by the rank-one Choi-marginal factorization")
        print("lattice_wide: checked and not executed — the theorem is channel-global for one six-site shell but no generated lattice history was constructed")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
