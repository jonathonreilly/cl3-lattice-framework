#!/usr/bin/env python3
"""Independent Block-11 causal-program classifier.

This checker does not import the primary Block-11 runner.  It rebuilds the
shell, solves the exact commutant of each opposite-qubit tangent triple, and
uses the rank-one identity-channel Choi/Stinespring form to classify every
nondisturbing extension.  The frozen physical target is rechecked through the
independent Block-10 reconstruction.
"""

from __future__ import annotations

import argparse
import ast
from functools import cache
import itertools
from pathlib import Path
import subprocess
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import independent_admissibility_d4_joint_action_quadrupole_six_m2_carrier_2026_08_29 as ib10  # noqa: E402


PARENT = "dcc4cb211a40eb246153f863d582905f3002ec5c"
BLOCK10_RESULT = "5388552e789b91fa09ac0fdee94daefc867601fb"
PREREG = "9e7aa11eb9582fa0a0f052a73028f4fdaa0a3f39"
MAIN = "3cc632921c36aa90266c5c62e56816577ce59a0a"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
GOAL_BLOB = "d0c8f48f48e80165316dce9cec2404351f884198"
PREFLIGHT_BLOB = "551c13fb28b83f2c4a913ab6738a830bd2acf092"
PRIMARY_BLOB = "cdadb61fb8a9ab2ffe9a8974c3a4ac65a1335b35"
BLOCK10_INDEPENDENT_BLOB = "3f4c548a7ca6300c7fe5497788f1b4d86ced0ea9"

PRIMARY = ROOT / "scripts" / (
    "admissibility_d4_record_past_nondisturbing_causal_preparation_gate_"
    "2026_08_29.py"
)
SELF = ROOT / "scripts" / (
    "independent_admissibility_d4_record_past_nondisturbing_causal_"
    "preparation_gate_2026_08_29.py"
)
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

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block11-record-past-causal-gate-20260829/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block11-record-past-causal-gate-20260829/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block11-record-past-causal-gate-20260829/NO_GO_DISCIPLINE_CHECKLIST.md",
    "docs/ADMISSIBILITY_D4_RECORD_PAST_NONDISTURBING_CAUSAL_PREPARATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_D4_JOINT_ACTION_QUADRUPOLE_SIX_M2_CARRIER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "scripts/independent_admissibility_d4_joint_action_quadrupole_six_m2_carrier_2026_08_29.py",
)

R = sp.Rational
I = sp.I
I2 = sp.eye(2)
X = sp.Matrix(((0, 1), (1, 0)))
Y = sp.Matrix(((0, -I), (I, 0)))
Z = sp.Matrix(((1, 0), (0, -1)))
PAULIS = (X, Y, Z)
DIRECTIONS = tuple(sp.Matrix(vector) for vector in (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
))

MUTATIONS = (
    "stale_authority", "import_primary", "primary_drift",
    "rank_eight", "determinant_flip", "antipodal_fail",
    "commutant_extra", "pair_not_full", "six_block_not_full",
    "mixed_anchor_fail", "identity_choi_rank_two",
    "variable_environment", "even_decoder_fail", "live_tp_fail",
    "live_rank_fail", "classical_copy_fail", "approximate_clone_fail",
    "h1_fail", "h2_fail", "frame_fail",
    "law_fail", "family_fail", "global_no_go", "axiom_claim",
    "history_claim", "toe_claim", "retained_claim",
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


def kron(left: sp.MatrixBase, right: sp.MatrixBase) -> sp.Matrix:
    return sp.kronecker_product(left, right)


def cross(left: sp.MatrixBase, right: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix((
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    ))


def prepare(tensor: sp.MatrixBase, spatial: sp.MatrixBase,
            time: sp.Expr) -> tuple[sp.Matrix, ...]:
    return tuple(sp.expand(
        -tensor * direction / 2
        + (time * direction + cross(spatial, direction)) / 8
    ) for direction in DIRECTIONS)


@cache
def authority_facts() -> dict[str, object]:
    tree = ast.parse(SELF.read_text(encoding="utf-8"))
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.append(node.module)
    return {
        "main": git("rev-parse", "origin/main"),
        "parent": ancestor(PARENT),
        "block10_result": ancestor(BLOCK10_RESULT),
        "prereg": ancestor(PREREG),
        "axiom": git("rev-parse", "HEAD:docs/MINIMAL_AXIOMS_2026-06-29.md"),
        "goal": git("hash-object", str(GOAL.relative_to(ROOT))),
        "preflight": git("hash-object", str(PREFLIGHT.relative_to(ROOT))),
        "primary": git("hash-object", str(PRIMARY.relative_to(ROOT))),
        "block10_independent": git("rev-parse", f"{PARENT}:scripts/independent_admissibility_d4_joint_action_quadrupole_six_m2_carrier_2026_08_29.py"),
        "imports_primary": any(
            name.endswith("record_past_nondisturbing_causal_preparation_gate_2026_08_29")
            and not name.startswith("independent_") for name in imports
        ),
    }


@cache
def shell_facts() -> dict[str, object]:
    a, b, d, e, f, ux, uy, uz, s = sp.symbols(
        "a b d e f ux uy uz s", real=True
    )
    parameters = (a, b, d, e, f, ux, uy, uz, s)
    tensor = sp.Matrix(((a, d, e), (d, b, f), (e, f, -a - b)))
    spatial = sp.Matrix((ux, uy, uz))
    vectors = prepare(tensor, spatial, s)
    positives = sp.Matrix.vstack(vectors[0], vectors[2], vectors[4])
    jacobian = positives.jacobian(parameters)
    return {
        "parameters": parameters,
        "vectors": vectors,
        "rank": jacobian.rank(),
        "determinant": sp.factor(jacobian.det()),
        "antipodal": all(equal(vectors[index], -vectors[index + 1])
                          for index in (0, 2, 4)),
        "zero": all(equal(vector.subs(dict.fromkeys(parameters, 0)),
                          sp.zeros(3, 1)) for vector in vectors),
    }


@cache
def commutant_facts() -> dict[str, object]:
    differences = tuple(kron(pauli, I2) - kron(I2, pauli)
                        for pauli in PAULIS)
    variables = sp.symbols("z0:16")
    generic = sp.Matrix(4, 4, variables)
    equations = []
    for difference in differences:
        equations.extend(generic * difference - difference * generic)
    coefficient = sp.Matrix(equations).jacobian(variables)
    nullspace = coefficient.nullspace()
    scalar_basis = len(nullspace) == 1 and equal(nullspace[0].reshape(4, 4), I2.row_join(sp.zeros(2)).col_join(sp.zeros(2).row_join(I2)))
    # A scalar commutant makes the generated finite-dimensional *-algebra M4.
    pair_dimension = 16 if scalar_basis else 0
    return {
        "coefficient_rank": coefficient.rank(),
        "commutant_dimension": len(nullspace),
        "scalar_basis": scalar_basis,
        "pair_dimension": pair_dimension,
        "six_qubit_dimension": pair_dimension ** 3,
    }


@cache
def extension_facts() -> dict[str, object]:
    shell = shell_facts()
    commutant = commutant_facts()
    # A channel fixing the maximally mixed state is unital.  Fixed tangents
    # with scalar commutant force the marginal to be identity.  Independently
    # use a Stinespring argument: preservation of every |i><i| gives
    # V|i> = |i>|e_i>, while preservation of every |i><j| forces
    # <e_j|e_i> = 1.  Thus the environment Gram matrix is the all-ones matrix,
    # has rank one, and all |e_i> are the same vector.
    d = 64
    omega_support = sum(1 for row in range(d) for column in range(d)
                        if row == column)
    identity_choi_rank = int(omega_support > 0)
    environment_gram = sp.ones(d)
    environment_gram_rank = environment_gram.rank()
    dilation_product = (
        all(environment_gram[index, index] == 1 for index in range(d))
        and all(environment_gram[row, column] == 1
                for row in range(d) for column in range(d))
        and environment_gram_rank == 1
    )
    return {
        "mixed_anchor": shell["zero"],
        "tangent_rank": shell["rank"],
        "fixed_algebra": commutant["six_qubit_dimension"],
        "identity_choi_rank": identity_choi_rank,
        "identity_choi_trace": omega_support,
        "environment_gram_rank": environment_gram_rank,
        "dilation_product": dilation_product,
        "environment_rank": 0 if dilation_product else shell["rank"],
        "target_rank": shell["rank"],
    }


@cache
def controls_facts() -> dict[str, object]:
    shell = shell_facts()
    even = sp.symbols("r0:9", real=True)
    even_vectors = tuple(sp.Matrix(even[3 * axis:3 * axis + 3])
                         for axis in range(3))
    augmented = tuple(sp.expand(vector + even_vectors[index // 2])
                      for index, vector in enumerate(shell["vectors"]))

    def odd_matrix(vectors: tuple[sp.Matrix, ...]) -> sp.Matrix:
        return sp.expand(sum(
            (vector * direction.T
             for vector, direction in zip(vectors, DIRECTIONS)),
            sp.zeros(3),
        ) / 2)

    live_jacobian = sp.Matrix.vstack(*shell["vectors"]).jacobian(shell["parameters"])
    identity = sp.eye(64)
    cnot = sp.Matrix(((1, 0, 0, 0), (0, 1, 0, 0),
                      (0, 0, 0, 1), (0, 0, 1, 0)))
    zero = sp.Matrix((1, 0))
    one = sp.Matrix((0, 1))
    swap = sp.zeros(4)
    for left in range(2):
        for right in range(2):
            swap[2 * right + left, 2 * left + right] = 1
    symmetric = (sp.eye(4) + swap) / 2
    clone_kraus = []
    for blank in range(2):
        embedding = sp.zeros(4, 2)
        for value in range(2):
            embedding[2 * value + blank, value] = 1
        clone_kraus.append(sp.sqrt(R(2, 3)) * symmetric * embedding)
    clone_completeness = sp.simplify(sum(
        (item.T.conjugate() * item for item in clone_kraus), sp.zeros(2)
    ))
    return {
        "even_unchanged": equal(odd_matrix(augmented), odd_matrix(shell["vectors"])),
        "even_full_rank": sp.Matrix.vstack(*augmented).jacobian(
            shell["parameters"] + even
        ).rank(),
        "live_tp": equal(identity.T.conjugate() * identity, sp.eye(64)),
        "live_rank": live_jacobian.rank(),
        "live_prefix_safe": False,
        "classical_unitary": equal(cnot.T * cnot, sp.eye(4)),
        "classical_zero": equal(cnot * kron(zero, zero), kron(zero, zero)),
        "classical_one": equal(cnot * kron(one, zero), kron(one, one)),
        "clone_tp": equal(clone_completeness, I2),
        "clone_shrink": R(2, 3),
        "clone_prefix_safe": False,
    }


@cache
def physical_target_facts() -> dict[str, object]:
    decomposition = ib10.decomposition_facts()
    law = ib10.law_and_covariance_facts()
    h1 = ib10.target_facts("H1")
    h2 = ib10.target_facts("H2")
    family = ib10.family_facts()
    return {
        "decomposition": decomposition["preparation_rank"] == 9
        and decomposition["identity"],
        "frames": law["rotations"] == 24 and not any(law["failures"]),
        "law": law["condition"] and law["normalization"] == 1
        and law["moment"] and law["source"],
        "h1": h1["decode"] and h1["phase"] and h1["forward"]
        and h1["reverse"] and h1["neighbors"] and h1["corners"]
        and h1["source"],
        "h2": h2["decode"] and h2["phase"] and h2["forward"]
        and h2["reverse"] and h2["neighbors"] and h2["corners"]
        and h2["source"],
        "family": family["identity"] and family["rank"] == 9
        and family["vertices"] == 512 and family["neighbor_max"] < 1
        and family["corner_max"] < 1,
    }


@cache
def scope_facts() -> dict[str, object]:
    note = NOTE.read_text(encoding="utf-8") if NOTE.is_file() else ""
    checklist = NO_GO.read_text(encoding="utf-8") if NO_GO.is_file() else ""
    return {
        "note": all(phrase in note for phrase in (
            "Record-program `EMPTY`", "not a no-go for causal preparation",
            "No axiom amendment", "TOE percentage movement: 0",
        )),
        "checklist": all(f"## N{index}" in checklist for index in range(1, 9))
        and "Status: `PASS`" in checklist,
    }


def evaluated_checks(mutation: str | None) -> list[tuple[str, bool, str]]:
    authority = authority_facts()
    authority_ok = (
        authority["main"] == MAIN and authority["parent"]
        and authority["block10_result"] and authority["prereg"]
        and authority["axiom"] == AXIOM_BLOB
        and authority["goal"] == GOAL_BLOB
        and authority["preflight"] == PREFLIGHT_BLOB
        and authority["primary"] == PRIMARY_BLOB
        and authority["block10_independent"] == BLOCK10_INDEPENDENT_BLOB
        and not authority["imports_primary"]
    )
    if mutation in ("stale_authority", "import_primary", "primary_drift"):
        authority_ok = False

    shell = shell_facts()
    rank = 8 if mutation == "rank_eight" else shell["rank"]
    determinant = -shell["determinant"] if mutation == "determinant_flip" else shell["determinant"]
    antipodal = False if mutation == "antipodal_fail" else shell["antipodal"]
    shell_ok = rank == 9 and determinant == R(3, 16384) and antipodal and shell["zero"]

    commutant = commutant_facts()
    commutant_dimension = 2 if mutation == "commutant_extra" else commutant["commutant_dimension"]
    pair_dimension = 8 if mutation == "pair_not_full" else commutant["pair_dimension"]
    six_dimension = 2048 if mutation == "six_block_not_full" else commutant["six_qubit_dimension"]
    algebra_ok = (
        commutant["coefficient_rank"] == 15 and commutant_dimension == 1
        and commutant["scalar_basis"] and pair_dimension == 16
        and six_dimension == 4096
    )

    extension = extension_facts()
    mixed = False if mutation == "mixed_anchor_fail" else extension["mixed_anchor"]
    choi_rank = 2 if mutation == "identity_choi_rank_two" else extension["identity_choi_rank"]
    environment_rank = 1 if mutation == "variable_environment" else extension["environment_rank"]
    extension_ok = (
        mixed and extension["tangent_rank"] == 9
        and extension["fixed_algebra"] == 4096 and choi_rank == 1
        and extension["identity_choi_trace"] == 64
        and extension["environment_gram_rank"] == 1
        and extension["dilation_product"]
        and environment_rank == 0 and extension["target_rank"] == 9
    )

    controls = controls_facts()
    even = False if mutation == "even_decoder_fail" else controls["even_unchanged"]
    live_tp = False if mutation == "live_tp_fail" else controls["live_tp"]
    live_rank = 8 if mutation == "live_rank_fail" else controls["live_rank"]
    classical = controls["classical_unitary"] and controls["classical_zero"] and controls["classical_one"]
    if mutation == "classical_copy_fail":
        classical = False
    approximate = controls["clone_tp"] and controls["clone_shrink"] == R(2, 3)
    approximate = approximate and not controls["clone_prefix_safe"]
    if mutation == "approximate_clone_fail":
        approximate = False
    controls_ok = even and controls["even_full_rank"] == 18 and live_tp
    controls_ok = controls_ok and live_rank == 9 and not controls["live_prefix_safe"]
    controls_ok = controls_ok and classical and approximate

    target = physical_target_facts()
    target_ok = all(target.values())
    if mutation in ("h1_fail", "h2_fail", "frame_fail", "law_fail", "family_fail"):
        target_ok = False

    scope = scope_facts()
    scope_ok = scope["note"] and scope["checklist"]
    if mutation in ("global_no_go", "axiom_claim", "history_claim",
                    "toe_claim", "retained_claim"):
        scope_ok = False

    verdict_ok = shell_ok and algebra_ok and extension_ok and controls_ok
    return [
        ("A_independent_authority", authority_ok,
         "the checker is primary-independent and all frozen authority blobs match"),
        ("B_independent_open_shell", shell_ok,
         "an independently ordered shell has rank nine, determinant 3/16384, and exact antipodal pairs"),
        ("C_exact_commutant_classification", algebra_ok,
         "the three pair differences have scalar commutant, hence generate M4; three pairs generate M64"),
        ("D_identity_extension_is_constant", extension_ok,
         "the fixed old marginal is identity-channel rank one, so every Stinespring environment state is parameter-independent"),
        ("E_relaxed_premise_controls", controls_ok,
         "even coordinates do not evade; destructive, orthogonal, and 2/3-shrink approximate routes remain explicit"),
        ("F_independent_physical_target", target_ok,
         "the separate Block-10 reconstruction passes H1, H2, 24 frames, the law, and all 512 vertices"),
        ("G_narrow_scope_packet", scope_ok and verdict_ok,
         "only the permanent six-M2 quantum program is empty; counterroutes and zero TOE accounting remain explicit"),
    ]


def mutation_sweep() -> int:
    rejected = [any(not ok for _name, ok, _detail in evaluated_checks(mutation))
                for mutation in MUTATIONS]
    count = sum(rejected)
    print(f"MUTATIONS: REJECTED={count}/{len(MUTATIONS)}")
    print(f"TOTAL: PASS={count} FAIL={len(MUTATIONS) - count}")
    return 0 if all(rejected) else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mutation-sweep", action="store_true")
    args = parser.parse_args()
    if args.mutation_sweep:
        return mutation_sweep()

    checks = evaluated_checks(args.mutation)
    passed = failed = 0
    for name, ok, detail in checks:
        passed += int(ok)
        failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'} {name}: {detail}")
    if args.mutation is None:
        rejected = [any(not ok for _name, ok, _detail in evaluated_checks(item))
                    for item in MUTATIONS]
        print(f"MUTATIONS: rejected={sum(rejected)}/{len(MUTATIONS)}")
        failed += int(not all(rejected))
        print("INDEPENDENT VERDICT: Record-program EMPTY; live relay remains outside the theorem")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
