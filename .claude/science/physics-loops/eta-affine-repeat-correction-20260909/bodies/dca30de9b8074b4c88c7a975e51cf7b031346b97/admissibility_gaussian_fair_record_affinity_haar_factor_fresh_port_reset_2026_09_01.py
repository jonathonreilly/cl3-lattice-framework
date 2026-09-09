#!/usr/bin/env python3
"""Block 36: fair Record, typed affinity factor, and fresh-port cylinders.

This runner constructs one exact candidate law.  Formation, the controller,
the complete operational domains, randomized-procedure/direct-midpoint
equivalence, lambda, and the translated fresh bank remain supplied data.  The
runner derives the probability identities inside that declared scope; it does
not promote the candidate to an axiom, an audit result, a loopy Z^3 law, or a
gravity/TOE claim.
"""

from __future__ import annotations

import ast
import hashlib
import itertools
import json
import math
import subprocess
import sys
from dataclasses import dataclass, field, replace
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Sequence

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
CANONICAL_MAIN = "aa7338d1fbc34a4b92205182b26793194e4727b6"
PREREG_COMMIT = "32f87a7d1e9d2d698a6c7b9bc95923f05d31a136"
PACKET = (
    ".claude/science/physics-loops/"
    "toe-source-eta-ownership-block36-autonomous-randomizer-typed-factor-reset-20260901"
)
GAUSSIAN_RUNNER = (
    "scripts/admissibility_gaussian_content_only_uniformizer_weierstrass_"
    "decoder_boundary_2026_08_10.py"
)
MINIMAL_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block36-autonomous-randomizer-typed-factor-reset-20260901/EXACT_TARGET_CONTRACT.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block36-autonomous-randomizer-typed-factor-reset-20260901/MUTATION_PLAN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block36-autonomous-randomizer-typed-factor-reset-20260901/AUTHORITY_GATE.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block36-autonomous-randomizer-typed-factor-reset-20260901/ASSUMPTIONS_AND_IMPORTS.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block36-autonomous-randomizer-typed-factor-reset-20260901/PANEL_RETURN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block36-autonomous-randomizer-typed-factor-reset-20260901/PREFLIGHT_WITNESSES.md",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

FROZEN_BLOBS = {
    f"{CANONICAL_MAIN}:docs/MINIMAL_AXIOMS_2026-06-29.md": "bc23300becfe4e4db57153c0e94cfcdf2338da71",
    f"{CANONICAL_MAIN}:docs/audit/data/axiom_premise_nodes.json": "b93959cca4f7e26c673cdccbe601e50c3cb93daa",
    f"{CANONICAL_MAIN}:docs/ai_methodology/skills/physics-loop/SKILL.md": "7b9663eb7f9d52c1f53a43d61b1997cebcbaa6c1",
    f"{CANONICAL_MAIN}:docs/ADMISSIBILITY_GAUSSIAN_CONTENT_ONLY_UNIFORMIZER_WEIERSTRASS_DECODER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md": "0800e5b08af198f83d4e8f6656a6baa9f914b005",
    f"{CANONICAL_MAIN}:{GAUSSIAN_RUNNER}": "6171decec8a97f4d1edc37f823eab594a4e14138",
    f"{CANONICAL_MAIN}:docs/work_history/repo/review_feedback/OPERATIONAL_QUOTIENT_BORN_AFFINITY_CYCLE20_NOTE_2026-07-14.md": "d6d2bda3d5cd8063479270c7ce462e1faee5b660",
    f"{CANONICAL_MAIN}:docs/POVM_OBSERVATION_COMPARATOR_EXACT_ARITHMETIC_BOUNDED_THEOREM_NOTE_2026-07-30.md": "ba400506335a5f8a30f45cf5c9912e8887db6ab1",
    f"{CANONICAL_MAIN}:docs/work_history/repo/review_feedback/COMPLETE_CANDIDATE_LSTAR_ASSEMBLY_CYCLE41_NOTE_2026-07-14.md": "fec025c7bb98b51fdbf16465a4fce3938ab27c98",
    f"{CANONICAL_MAIN}:docs/ADMISSIBILITY_REGISTERED_PARTITION_BARYCENTER_PUSHFORWARD_BOUNDED_THEOREM_NOTE_2026-08-12.md": "71375b6d4a6b86945aabbbfc542b87c3b2f7d029",
    f"{CANONICAL_MAIN}:docs/RECORD_PERMANENCE_FORCES_FRESH_SITE_DOUBLE_REGISTRATION_AND_AGREEMENT_SURVIVAL_BOUNDED_THEOREM_NOTE_2026-07-11.md": "5112dc29485ee33f3b6bb548d29ce0c4a0e6a267",
    f"{CANONICAL_MAIN}:docs/READ_RESET_CADENCE_INTERFERENCE_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-17.md": "e3519460794d1547b9bad7d095740cfd26827fb4",
    f"{PREREG_COMMIT}:docs/ADMISSIBILITY_D4_OUTPUT_STATUS_NN_ORDERED_PAIR_TRANSDUCER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md": "c45ad2907b5184ac8156558ef25eeaa0fa3fdfe2",
    f"{PREREG_COMMIT}:docs/ADMISSIBILITY_D4_SYMBOLIC_LAMBDA_GUARDED_FINITE_SUCCESSOR_TRANSACTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md": "b0fb6544e274cc6b762ea11f0d7817558229f5dc",
    f"{PREREG_COMMIT}:docs/ADMISSIBILITY_D4_CLASSICAL_SCREENING_CAUSE_PERSISTENCE_RENEWAL_LOCUS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md": "65f3b60162bcef562eee705f49e6ef76faf5f2df",
    f"{PREREG_COMMIT}:docs/ADMISSIBILITY_D4_BLOCK208_AFFINE_SIX_RECORD_H1_DECODER_CENTER_CORNER_QND_DILATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md": "95e67961ffe80fb89b6c0ef7f37337ca0aa5099d",
    f"{PREREG_COMMIT}:docs/ADMISSIBILITY_OPUS_AFFINE_BORN_PUBLIC_EVIDENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-01.md": "833232ecc6a8231c59f16b1af819c47c0eeb2bde",
    f"{PREREG_COMMIT}:{PACKET}/EXACT_TARGET_CONTRACT.md": "37f629e46433451dc185826948569162c6265af2",
    f"{PREREG_COMMIT}:{PACKET}/MUTATION_PLAN.md": "f940ea9a8759f20bbc4e5d15cd703d5302125eb5",
    f"{PREREG_COMMIT}:{PACKET}/AUTHORITY_GATE.md": "1b27a7e001e4f94a13983a53b96aadd196426abc",
    f"{PREREG_COMMIT}:{PACKET}/ASSUMPTIONS_AND_IMPORTS.md": "4c687662e7c65f30865da280232f6fafd12cea0f",
    f"{PREREG_COMMIT}:{PACKET}/PANEL_RETURN.md": "09d446aa90f6643add2586b5084d8c0e39cc9ed2",
    f"{PREREG_COMMIT}:{PACKET}/PREFLIGHT_WITNESSES.md": "8f68a1dbed60f0bd7363fdd742bc7e88f7fec3b4",
    f"{PREREG_COMMIT}:{PACKET}/ROUTE_PORTFOLIO.md": "6628f17291f3ab9e95dab43029b3188edf6cca8a",
    f"{PREREG_COMMIT}:{PACKET}/NO_GO_LEDGER.md": "abbd78edb6351ef5f3b572cc6339ca752cc33389",
    f"{PREREG_COMMIT}:{PACKET}/TRACE_GATE.md": "dcb9659ab4c45dd05dba7423cf5d04b84888790a",
    f"{PREREG_COMMIT}:{PACKET}/OPPORTUNITY_QUEUE.md": "ba7fc8f4b248487c7545d51319e731a0ae640331",
    f"{PREREG_COMMIT}:{PACKET}/STATE.yaml": "8bc12201dd6fa1e0bf24bf9f5ad1f1dfdd39191a",
}

AXES = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
OUTCOMES = ("north", "south")
PREPARATION_STATES = ((0, 0, 1), (0, 0, -1))
TEST_STATES = ((0, 0, 1), (0, 0, 0))
CANDIDATE_LAMBDA = Fraction(1)


def haar_hemisphere_rows(
    states: Sequence[Sequence[int | Fraction]],
    lam: Fraction,
) -> tuple[tuple[Fraction, Fraction], ...]:
    """Integrate 1+lambda*n.s over the north/south Haar hemispheres."""

    return tuple(
        (
            Fraction(1, 2) + lam * Fraction(state[2], 4),
            Fraction(1, 2) - lam * Fraction(state[2], 4),
        )
        for state in states
    )


PREPARATION_ROWS = haar_hemisphere_rows(PREPARATION_STATES, CANDIDATE_LAMBDA)
TEST_ROWS = haar_hemisphere_rows(TEST_STATES, CANDIDATE_LAMBDA)


@dataclass
class Checks:
    results: dict[str, bool] = field(default_factory=dict)

    def check(self, name: str, detail: str, condition: object) -> None:
        result = bool(condition)
        self.results[name] = result
        print(f"{'PASS' if result else 'FAIL'} {name}: {detail}")

    @property
    def passed(self) -> int:
        return sum(self.results.values())

    @property
    def failed(self) -> int:
        return len(self.results) - self.passed

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def git_output(*args: str) -> str:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout.strip()


def git_bytes(spec: str) -> bytes:
    return subprocess.run(
        ["git", "show", spec],
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout


def prereg_text(name: str) -> str:
    return git_bytes(f"{PREREG_COMMIT}:{PACKET}/{name}").decode()


def input_fingerprint() -> str:
    digest = hashlib.sha256()
    for relative in AUDIT_INPUT_PATHS:
        digest.update(relative.encode())
        digest.update(b"\0")
        digest.update((ROOT / relative).read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def dot(left: Sequence[int | Fraction], right: Sequence[int | Fraction]) -> Fraction:
    return sum(
        (Fraction(a) * Fraction(b) for a, b in zip(left, right)), Fraction(0)
    )


def determinant3(rows: Sequence[Sequence[int]]) -> int:
    a, b, c = rows
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def proper_cubic_rotations() -> tuple[tuple[tuple[int, ...], ...], ...]:
    rotations = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            rows = []
            for row_index in range(3):
                row = [0, 0, 0]
                row[permutation[row_index]] = signs[row_index]
                rows.append(tuple(row))
            matrix = tuple(rows)
            if determinant3(matrix) == 1:
                rotations.append(matrix)
    return tuple(rotations)


ROTATIONS = proper_cubic_rotations()


def matvec(
    matrix: Sequence[Sequence[int]], vector: Sequence[int | Fraction]
) -> tuple[Fraction, ...]:
    return tuple(dot(row, vector) for row in matrix)


def matmul(
    left: Sequence[Sequence[int | Fraction]],
    right: Sequence[Sequence[int | Fraction]],
) -> tuple[tuple[Fraction, ...], ...]:
    columns = tuple(zip(*right))
    return tuple(tuple(dot(row, column) for column in columns) for row in left)


def transpose(
    matrix: Sequence[Sequence[int | Fraction]],
) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(tuple(Fraction(value) for value in column) for column in zip(*matrix))


@dataclass(frozen=True)
class CandidateImports:
    formation: str
    controller: str
    operational_domain: str
    relative_midpoint_interface: str
    local_channel_state_sufficiency: str
    full_active_kernel_schedule: str
    fresh_bank: str
    lambda_domain: tuple[Fraction, Fraction]
    geometry: str


CANDIDATE_IMPORTS = CandidateImports(
    formation="supplied_record_formation_order",
    controller="supplied_record_first_controller",
    operational_domain="supplied_complete_bloch_balls",
    relative_midpoint_interface="supplied_relative_active_interface_equivalence",
    local_channel_state_sufficiency="supplied_local_channel_state_sufficiency",
    full_active_kernel_schedule="supplied_translation_invariant_no_relay_schedule",
    fresh_bank="supplied_conditionally_independent_indexed_gaussian_innovations",
    lambda_domain=(Fraction(-1), Fraction(1)),
    geometry="finite_rooted_trees_and_translated_ray",
)


def candidate_imports_valid(imports: CandidateImports) -> bool:
    return (
        imports.formation.startswith("supplied_")
        and imports.controller == "supplied_record_first_controller"
        and imports.operational_domain == "supplied_complete_bloch_balls"
        and imports.relative_midpoint_interface
        == "supplied_relative_active_interface_equivalence"
        and imports.local_channel_state_sufficiency
        == "supplied_local_channel_state_sufficiency"
        and imports.full_active_kernel_schedule
        == "supplied_translation_invariant_no_relay_schedule"
        and imports.fresh_bank
        == "supplied_conditionally_independent_indexed_gaussian_innovations"
        and imports.lambda_domain == (Fraction(-1), Fraction(1))
        and "tree" in imports.geometry
        and "ray" in imports.geometry
    )


def gate_source_identity(checks: Checks) -> None:
    actual = {spec: git_output("rev-parse", spec) for spec in FROZEN_BLOBS}
    inputs_exist = all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
    worktree_inputs_match = all(
        git_output("hash-object", "--", relative)
        == FROZEN_BLOBS[f"{PREREG_COMMIT}:{relative}"]
        for relative in AUDIT_INPUT_PATHS
    )
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    assignments = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        )
    ]
    literal_paths = ast.literal_eval(assignments[0].value)
    writing_calls = {
        "write_text",
        "write_bytes",
        "unlink",
        "rename",
        "replace",
        "mkdir",
        "rmdir",
    }
    called_attributes = {
        node.func.attr
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
    }
    no_writes = not (writing_calls & called_attributes)
    ok = (
        actual == FROZEN_BLOBS
        and inputs_exist
        and worktree_inputs_match
        and tuple(literal_paths) == AUDIT_INPUT_PATHS
        and DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS
        and len(input_fingerprint()) == 64
        and no_writes
    )
    checks.check(
        "source_identity_and_inventory",
        f"{len(FROZEN_BLOBS)} blobs and {len(AUDIT_INPUT_PATHS)} declared reads match; fingerprint={input_fingerprint()[:16]}",
        ok,
    )


def gate_authority_scope(checks: Checks) -> None:
    minimal = git_bytes(f"{CANONICAL_MAIN}:{MINIMAL_PATH}").decode()
    minimal_flat = " ".join(minimal.split())
    registry = json.loads(git_bytes(f"{CANONICAL_MAIN}:{REGISTRY_PATH}"))
    contract = prereg_text("EXACT_TARGET_CONTRACT.md")
    state = prereg_text("STATE.yaml")
    canonical_ids = registry["canonical_ids"]
    axioms = ("Lattice", "Qubit", "Admissibility", "Record")
    forbidden_authorizations = (
        "axiom_edit_authorized: true",
        "primitive_edit_authorized: true",
        "audit_edit_authorized: true",
        "toe_score_edit_authorized: true",
        "obligation_retirement_claimed: true",
    )
    ok = (
        all(f"### {name}" in minimal for name in axioms)
        and canonical_ids
        == [
            "minimal_axioms",
            "scale_reference_primitive",
            "kinetic_isotropy_primitive",
            "realized_state_primitive",
        ]
        and "does not supply the formation site, probability, or rate" in minimal_flat
        and "On one explicit candidate protocol" in contract
        and "No Born/trace weight may create the fair bit" in contract
        and not any(flag in state for flag in forbidden_authorizations)
        and candidate_imports_valid(CANDIDATE_IMPORTS)
    )
    checks.check(
        "authority_scope_and_supplied_imports",
        "axioms supply distribution existence but no extensional weight values/controller; candidate-law and local-sufficiency inputs remain conditional",
        ok,
    )


def gate_upstream_gaussian(checks: Checks) -> None:
    source = git_bytes(f"{CANONICAL_MAIN}:{GAUSSIAN_RUNNER}").decode()
    needles = (
        "all(imaginary_trace(center) == 0 for center in hermitian_centers)",
        "real_coordinate_variance + real_coordinate_variance == 1",
        "fixed_threshold_probability(Fraction(3, 10), t) == Fraction(3, 10)",
        "TOTAL: PASS={self.passed} FAIL={self.failed}",
    )
    ok = all(needle in source for needle in needles)
    checks.check(
        "canonical_gaussian_source_boundary",
        "canonical blob, not the branch-local runner, contains the pinned center/variance/fixed-threshold identities; the fair half-bit is rederived next",
        ok,
    )


def gaussian_fair_data() -> dict[str, object]:
    a, d, u, v = sp.symbols("a d u v", real=True)
    center = sp.Matrix([[a, u + sp.I * v], [u - sp.I * v, d]])
    x = sp.symbols("x", real=True)
    density = sp.exp(-(x**2) / 2) / sp.sqrt(2 * sp.pi)
    half_mass = sp.integrate(density, (x, -sp.oo, 0))
    coordinate_variance = sp.Rational(1, 2)
    return {
        "imaginary_center_trace": sp.simplify(sp.im(sp.trace(center))),
        "noise_mean": sp.Integer(0),
        "noise_variance": 2 * coordinate_variance,
        "half_mass": half_mass,
        "threshold": sp.Rational(1, 2),
    }


def gate_gaussian_fair_record(checks: Checks) -> None:
    data = gaussian_fair_data()
    ok = (
        data["imaginary_center_trace"] == 0
        and data["noise_mean"] == 0
        and data["noise_variance"] == 1
        and data["half_mass"] == data["threshold"] == sp.Rational(1, 2)
    )
    checks.check(
        "gaussian_fair_record_all_hermitian_centers",
        "symbolic Hermitian C gives Im Tr(C)=0; two N(0,1/2) coordinates give S~N(0,1) and fixed U<=1/2 mass 1/2",
        ok,
    )


@dataclass(frozen=True)
class FormedRecord:
    value: int
    origin: str
    site: int


@dataclass(frozen=True)
class ControlRun:
    record: FormedRecord
    selected_branch: int
    events: tuple[str, ...]


def execute_controller(
    bit: int, *, supplied_branch: int | None = None, control_first: bool = False
) -> ControlRun:
    record = FormedRecord(bit, "gaussian_uniformizer", 1)
    selected = record.value if supplied_branch is None else supplied_branch
    events = (
        ("formation", "branch_control", "record", "outcome")
        if control_first
        else ("formation", "record", "branch_control", "outcome")
    )
    return ControlRun(record, selected, events)


def valid_record_first(run: ControlRun) -> bool:
    return (
        run.record.origin == "gaussian_uniformizer"
        and run.selected_branch == run.record.value
        and run.events.index("record") < run.events.index("branch_control")
    )


@dataclass(frozen=True)
class MixtureEvidence:
    fine: tuple[tuple[int, str, Fraction], ...]
    coarse: tuple[Fraction, ...]
    provenance: str


def cylinder_mixture(
    rows: Sequence[Sequence[Fraction]], *, forged: bool = False
) -> MixtureEvidence:
    midpoint = tuple((rows[0][i] + rows[1][i]) / 2 for i in range(len(OUTCOMES)))
    if forged:
        return MixtureEvidence((), midpoint, "desired_midpoint_equation")
    fine = tuple(
        (bit, outcome, Fraction(1, 2) * rows[bit][index])
        for bit in (0, 1)
        for index, outcome in enumerate(OUTCOMES)
    )
    coarse = tuple(
        sum(
            (weight for bit, name, weight in fine if name == outcome), Fraction(0)
        )
        for outcome in OUTCOMES
    )
    return MixtureEvidence(fine, coarse, "fine_cylinder_marginal")


def valid_cylinder_mixture(
    evidence: MixtureEvidence, rows: Sequence[Sequence[Fraction]]
) -> bool:
    expected_fine = 2 * len(OUTCOMES)
    expected_midpoint = tuple(
        (rows[0][i] + rows[1][i]) / 2 for i in range(len(OUTCOMES))
    )
    return (
        evidence.provenance == "fine_cylinder_marginal"
        and len(evidence.fine) == expected_fine
        and sum((weight for _, _, weight in evidence.fine), Fraction(0)) == 1
        and evidence.coarse == expected_midpoint
    )


def gate_record_first_cylinders(checks: Checks) -> None:
    runs = tuple(execute_controller(bit) for bit in (0, 1))
    preparation = cylinder_mixture(PREPARATION_ROWS)
    test = cylinder_mixture(TEST_ROWS)
    p0, p1 = sp.symbols("p0 p1", real=True)
    universal_identity = sp.simplify((p0 / 2 + p1 / 2) - (p0 + p1) / 2) == 0
    z = sp.symbols("z", real=True)
    def integrated_rows(states: Sequence[Sequence[int | Fraction]]) -> tuple[tuple[sp.Expr, sp.Expr], ...]:
        return tuple(
            (
                sp.integrate(1 + CANDIDATE_LAMBDA * state[2] * z, (z, 0, 1)) / 2,
                sp.integrate(1 + CANDIDATE_LAMBDA * state[2] * z, (z, -1, 0)) / 2,
            )
            for state in states
        )

    preparation_integrals = integrated_rows(PREPARATION_STATES)
    test_integrals = integrated_rows(TEST_STATES)
    edge_kernel_link = (
        preparation_integrals == PREPARATION_ROWS and test_integrals == TEST_ROWS
    )
    joint_kernel_link = all(
        weight
        == Fraction(1, 2)
        * preparation_integrals[bit][OUTCOMES.index(outcome)]
        for bit, outcome, weight in preparation.fine
    )
    ok = (
        all(valid_record_first(run) for run in runs)
        and valid_cylinder_mixture(preparation, PREPARATION_ROWS)
        and valid_cylinder_mixture(test, TEST_ROWS)
        and universal_identity
        and edge_kernel_link
        and joint_kernel_link
    )
    checks.check(
        "record_first_fine_cylinder_average",
        "both slots read the formed bit first; the supplied lambda=+1 member has each fine weight (1/2) integral_E phi dmu and marginalization derives the procedure average",
        ok,
    )


def gate_midpoint_equivalence_boundary(checks: Checks) -> None:
    evidence = cylinder_mixture(PREPARATION_ROWS)
    ok = (
        valid_cylinder_mixture(evidence, PREPARATION_ROWS)
        and CANDIDATE_IMPORTS.relative_midpoint_interface
        == "supplied_relative_active_interface_equivalence"
        and CANDIDATE_IMPORTS.local_channel_state_sufficiency
        == "supplied_local_channel_state_sufficiency"
        and candidate_imports_valid(CANDIDATE_IMPORTS)
    )
    checks.check(
        "supplied_midpoint_equivalence_boundary",
        "cylinders prove procedure averaging only; local direct-midpoint identification and channel/state sufficiency are fail-closed supplied inputs",
        ok,
    )


def partial_trace_first_qubit(matrix: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(
        2,
        2,
        lambda row, column: sum(
            matrix[2 * archive + row, 2 * archive + column]
            for archive in range(2)
        ),
    )


def partial_trace_second_qubit(matrix: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(
        2,
        2,
        lambda row, column: sum(
            matrix[2 * row + target, 2 * column + target]
            for target in range(2)
        ),
    )


def gate_local_channel_global_archive_control(checks: Checks) -> None:
    identity = sp.eye(2)
    z_pauli = sp.diag(1, -1)
    rho_zero = sp.diag(1, 0)
    rho_one = sp.diag(0, 1)
    rho_mid = identity / 2
    archive_zero = sp.diag(1, 0)
    archive_one = sp.diag(0, 1)
    omega_mix = (
        sp.kronecker_product(archive_zero, rho_zero)
        + sp.kronecker_product(archive_one, rho_one)
    ) / 2
    omega_direct = sp.kronecker_product(identity / 2, rho_mid)
    target_marginals_match = (
        partial_trace_first_qubit(omega_mix)
        == partial_trace_first_qubit(omega_direct)
        == rho_mid
    )
    archive_marginals_match = (
        partial_trace_second_qubit(omega_mix)
        == partial_trace_second_qubit(omega_direct)
        == identity / 2
    )
    correlator = sp.kronecker_product(z_pauli, z_pauli)
    mix_correlation = sp.trace(omega_mix * correlator)
    direct_correlation = sp.trace(omega_direct * correlator)

    # For the constant preparation channel P_rho(X)=Tr(X) rho, the
    # unnormalized Choi matrix is I tensor rho.  This establishes the local
    # relative bridge without equating the global archived states.
    choi_zero = sp.kronecker_product(identity, rho_zero)
    choi_one = sp.kronecker_product(identity, rho_one)
    choi_mid = sp.kronecker_product(identity, rho_mid)
    channel_identity = sp.simplify((choi_zero + choi_one) / 2 - choi_mid) == sp.zeros(4)
    ok = (
        target_marginals_match
        and archive_marginals_match
        and omega_mix != omega_direct
        and mix_correlation == 1
        and direct_correlation == 0
        and channel_identity
        and CANDIDATE_IMPORTS.local_channel_state_sufficiency
        == "supplied_local_channel_state_sufficiency"
    )
    checks.check(
        "local_channel_bridge_global_archive_discriminator",
        "(P_r0+P_r1)/2=P_mid and Choi matrices agree locally, but Omega_mix has archive correlator 1 versus Omega_dir 0; sufficiency stays supplied",
        ok,
    )


def midpoint(left: Sequence[Fraction], right: Sequence[Fraction]) -> tuple[Fraction, ...]:
    return tuple((a + b) / 2 for a, b in zip(left, right))


def dyadic_grid(
    left: Sequence[Fraction], right: Sequence[Fraction], depth: int
) -> tuple[tuple[Fraction, ...], ...]:
    grid = (tuple(left), tuple(right))
    for _ in range(depth):
        refined = []
        for index in range(len(grid) - 1):
            refined.extend((grid[index], midpoint(grid[index], grid[index + 1])))
        refined.append(grid[-1])
        grid = tuple(refined)
    return grid


@dataclass(frozen=True)
class JensenPremises:
    domain: str
    convex_domain_source: str
    complete_domain_source: str
    midpoint_all_pairs_source: str
    lower_bound: Fraction
    upper_bound: Fraction
    relative_interface_source: str


JENSEN_PREMISES = JensenPremises(
    domain="full_closed_bloch_ball",
    convex_domain_source="supplied_complete_bloch_ball",
    complete_domain_source="supplied_complete_bloch_ball",
    midpoint_all_pairs_source="supplied_relative_active_interface_equivalence",
    lower_bound=Fraction(0),
    upper_bound=Fraction(1),
    relative_interface_source="supplied_local_channel_state_sufficiency",
)


def bounded_midpoint_jensen_applies(premises: JensenPremises) -> bool:
    return (
        premises.domain == "full_closed_bloch_ball"
        and premises.convex_domain_source == "supplied_complete_bloch_ball"
        and premises.complete_domain_source == "supplied_complete_bloch_ball"
        and premises.midpoint_all_pairs_source
        == "supplied_relative_active_interface_equivalence"
        and premises.lower_bound <= premises.upper_bound
        and premises.relative_interface_source
        == "supplied_local_channel_state_sufficiency"
    )


def gate_dyadic_jensen(checks: Checks) -> None:
    left, right = PREPARATION_ROWS
    grids = tuple(dyadic_grid(left, right, depth) for depth in range(7))
    dyadic_formula = all(
        row
        == tuple(
            Fraction(2**depth - k, 2**depth) * left[j]
            + Fraction(k, 2**depth) * right[j]
            for j in range(len(left))
        )
        for depth, grid in enumerate(grids)
        for k, row in enumerate(grid)
    )
    x = sp.symbols("x", real=True)
    depth = 4
    finite_grid = tuple(sp.Rational(k, 2**depth) for k in range(2**depth + 1))
    evader = sp.prod(x - point for point in finite_grid)
    finite_only_insufficient = all(evader.subs(x, point) == 0 for point in finite_grid)
    finite_only_insufficient = finite_only_insufficient and evader.subs(
        x, sp.Rational(1, 2 ** (depth + 1))
    ) != 0
    irrational = sp.sqrt(2) / 2
    extension_gap = sp.simplify(
        (irrational / 2 + 1) - (sp.Rational(0) + irrational + 1) / 2
    )
    dyadic_extension_insufficient = extension_gap == sp.Rational(1, 2)
    ok = (
        dyadic_formula
        and finite_only_insufficient
        and dyadic_extension_insufficient
        and bounded_midpoint_jensen_applies(JENSEN_PREMISES)
    )
    checks.check(
        "dyadic_jensen_full_domain",
        "midpoint recursion gives every k/2^n; explicit finite-grid and nondyadic witnesses distinguish weaker domains, while the supplied all-pairs bounded complete domain meets Jensen prerequisites",
        ok,
    )


def cubic_commutant_data() -> tuple[int, tuple[sp.Matrix, ...], sp.Matrix]:
    avec = sp.Matrix(sp.symbols("a0:3"))
    bvec = sp.Matrix(sp.symbols("b0:3"))
    matrix_symbols = sp.symbols("m0:9")
    matrix = sp.Matrix(3, 3, matrix_symbols)
    variables = list(avec) + list(bvec) + list(matrix_symbols)
    equations = []
    for raw_rotation in ROTATIONS:
        rotation = sp.Matrix(raw_rotation)
        equations.extend(rotation.T * avec - avec)
        equations.extend(rotation.T * bvec - bvec)
        equations.extend(rotation.T * matrix * rotation - matrix)
    coefficients, _ = sp.linear_eq_to_matrix(equations, variables)
    return coefficients.rank(), tuple(coefficients.nullspace()), coefficients


def cubic_invariant(
    vector: Sequence[int | Fraction], matrix: Sequence[Sequence[int | Fraction]]
) -> bool:
    vector_fixed = all(matvec(rotation, vector) == tuple(map(Fraction, vector)) for rotation in ROTATIONS)
    matrix_fixed = all(
        matmul(matmul(transpose(rotation), matrix), rotation)
        == tuple(tuple(Fraction(value) for value in row) for row in matrix)
        for rotation in ROTATIONS
    )
    return vector_fixed and matrix_fixed


def gate_cubic_commutant(checks: Checks) -> None:
    rank, nullspace, _ = cubic_commutant_data()
    expected = sp.Matrix([0] * 6 + [1, 0, 0, 0, 1, 0, 0, 0, 1])
    normalized = nullspace[0] / nullspace[0][6]
    ok = (
        len(ROTATIONS) == 24
        and rank == 14
        and len(nullspace) == 1
        and normalized == expected
        and cubic_invariant((0, 0, 0), ((1, 0, 0), (0, 1, 0), (0, 0, 1)))
    )
    checks.check(
        "proper_cubic_separate_affinity_commutant",
        "24 rotations give rank 14 on 15 nonconstant coefficients: invariant responses are exactly c+b r.s",
        ok,
    )


def phi(left: Sequence[int | Fraction], right: Sequence[int | Fraction], lam: Fraction) -> Fraction:
    return Fraction(1) + lam * dot(left, right)


def six_axis_transition(lam: Fraction) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(
        tuple(phi(left, right, lam) / 6 for right in AXES) for left in AXES
    )


def normalized_z_integral(expression: sp.Expr, lower: int, upper: int) -> sp.Expr:
    z = next(iter(expression.free_symbols), sp.symbols("z", real=True))
    return sp.simplify(sp.integrate(expression, (z, lower, upper)) / 2)


def gate_haar_edge(checks: Checks) -> None:
    lam = sp.symbols("lambda", real=True)
    overlap = sp.symbols("u", real=True)
    nx, ny, nz, mx, my, mz = sp.symbols("nx ny nz mx my mz", real=True)
    first_moments = {nx: 0, ny: 0, nz: 0}
    normalized = sp.expand(1 + lam * (nx * mx + ny * my + nz * mz)).subs(
        first_moments
    )
    second_moment = sp.diag(sp.Rational(1, 3), sp.Rational(1, 3), sp.Rational(1, 3))
    n_vector = sp.Matrix((nx, ny, nz))
    m_vector = sp.Matrix((mx, my, mz))
    lagrange_identity = sp.expand(
        n_vector.dot(m_vector) ** 2
        + n_vector.cross(m_vector).dot(n_vector.cross(m_vector))
        - n_vector.dot(n_vector) * m_vector.dot(m_vector)
    )
    rectangle_expression = 1 + lam * overlap
    separately_affine = (
        sp.diff(rectangle_expression, lam, 2) == 0
        and sp.diff(rectangle_expression, overlap, 2) == 0
    )
    rectangle_minimum = min(
        1 + lam_value * overlap_value
        for lam_value in (-1, 1)
        for overlap_value in (-1, 1)
    )
    endpoint_values = tuple(
        phi(left, right, value)
        for value in (Fraction(-1), Fraction(0), Fraction(1))
        for left in AXES
        for right in AXES
    )
    reversibility = all(
        phi(left, right, value) == phi(right, left, value)
        for value in (Fraction(-1), Fraction(0), Fraction(1))
        for left in AXES
        for right in AXES
    )
    ok = (
        normalized == 1
        and second_moment.trace() == 1
        and lagrange_identity == 0
        and separately_affine
        and rectangle_minimum == 0
        and min(endpoint_values) == 0
        and max(endpoint_values) == 2
        and all(value >= 0 for value in endpoint_values)
        and reversibility
        and phi(AXES[0], AXES[1], Fraction(1)) == 0
        and phi(AXES[0], AXES[1], Fraction(0)) == 1
    )
    checks.check(
        "normalized_reversible_haar_edge_density",
        "dmu=dOmega/4pi gives integral phi=1; Lagrange/Cauchy bounds u=n.m in [-1,1], and the bilinear rectangle minimum is 0 with antipodal zeros",
        ok,
    )


def gate_six_axis_kernel(checks: Checks) -> None:
    lam = sp.symbols("lambda", real=True)
    symbolic = sp.Matrix(
        [[(1 + lam * dot(left, right)) / 6 for right in AXES] for left in AXES]
    )
    polynomial = symbolic.charpoly()
    spectral_variable = polynomial.gen
    characteristic = sp.factor(polynomial.as_expr())
    expected = sp.factor(
        (spectral_variable - 1)
        * spectral_variable**2
        * (spectral_variable - lam / 3) ** 3
    )
    rows = tuple(six_axis_transition(value) for value in (Fraction(-1), Fraction(0), Fraction(1)))
    ok = (
        characteristic == expected
        and all(sum(row, Fraction(0)) == 1 for matrix in rows for row in matrix)
        and all(
            6 * matrix[i][j] == phi(AXES[i], AXES[j], value)
            for value, matrix in zip((Fraction(-1), Fraction(0), Fraction(1)), rows)
            for i in range(6)
            for j in range(6)
        )
    )
    checks.check(
        "six_axis_phi_equals_6p_and_spectrum",
        "exact rows normalize at lambda=-1,0,1 and charpoly=(x-1)x^2(x-lambda/3)^3",
        ok,
    )


def tree_weight(
    states: Sequence[Sequence[int]], parents: Sequence[int], lam: Fraction
) -> Fraction:
    return math.prod(
        phi(states[child], states[parent], lam)
        for child, parent in enumerate(parents, start=1)
    )


def direct_tree_partition(parents: Sequence[int], lam: Fraction) -> Fraction:
    count = len(parents) + 1
    total = sum(
        (
            tree_weight(states, parents, lam)
            for states in itertools.product(AXES, repeat=count)
        ),
        Fraction(0),
    )
    return total / (6**count)


def recursive_tree_reduces(parents: Sequence[int]) -> bool:
    active = set(range(len(parents) + 1))
    parent_of = {child: parent for child, parent in enumerate(parents, start=1)}
    while len(active) > 1:
        leaves = [
            node
            for node in active
            if node != 0 and not any(parent_of.get(other) == node for other in active)
        ]
        if not leaves:
            return bool(len(active) == 1)
        active.remove(leaves[0])
    return active == {0}


def gate_tree_normalization(checks: Checks) -> None:
    lam = sp.symbols("lambda", real=True)
    leaf_integrals = tuple(
        sp.simplify(sum(1 + lam * dot(child, parent) for child in AXES) / 6)
        for parent in AXES
    )
    recursive_trees = tuple(
        parents
        for count in range(1, 8)
        for parents in itertools.product(*(range(child) for child in range(1, count)))
    )
    direct_fixtures = (
        (),
        (0,),
        (0, 0),
        (0, 1, 2),
        (0, 0, 1, 1),
    )
    direct = all(
        direct_tree_partition(parents, value) == 1
        for parents in direct_fixtures
        for value in (Fraction(-1), Fraction(0), Fraction(1))
    )
    ok = (
        all(value == 1 for value in leaf_integrals)
        and all(recursive_tree_reduces(parents) for parents in recursive_trees)
        and direct
    )
    checks.check(
        "all_finite_rooted_tree_product_law",
        "symbolic leaf integral is 1 and every recursive tree through 7 vertices reduces; independent exact endpoint sums confirm tree Z=1",
        ok,
    )


def cycle_weight(states: Sequence[Sequence[int]], lam: Fraction) -> Fraction:
    return math.prod(
        phi(states[index], states[(index + 1) % len(states)], lam)
        for index in range(len(states))
    )


def direct_cycle_partition(length: int, lam: Fraction) -> Fraction:
    total = sum(
        (cycle_weight(states, lam) for states in itertools.product(AXES, repeat=length)),
        Fraction(0),
    )
    return total / (6**length)


def cycle_partition_formula(length: int, lam: Fraction) -> Fraction:
    return Fraction(1) + 3 * (lam / 3) ** length


def gate_cycle_control(checks: Checks) -> None:
    lengths = (3, 4, 5)
    values = (Fraction(-1), Fraction(0), Fraction(1))
    independent_routes = all(
        direct_cycle_partition(length, lam) == cycle_partition_formula(length, lam)
        for length in lengths
        for lam in values
    )
    c4 = cycle_partition_formula(4, Fraction(1))
    ok = independent_routes and c4 == Fraction(28, 27) and c4 != 1
    checks.check(
        "cycle_topology_and_partition_control",
        "six-axis enumeration matches spectral Z(C_L)=1+3(lambda/3)^L; C4 at +1 is 28/27, not the tree value",
        ok,
    )


def six_neighbor_normalizer(
    neighbors: Sequence[Sequence[int | Fraction]], lam: Fraction
) -> Fraction:
    return sum(
        (
            math.prod(phi(candidate, neighbor, lam) for neighbor in neighbors)
            for candidate in AXES
        ),
        Fraction(0),
    ) / 6


def gate_six_axis_zeros(checks: Checks) -> None:
    zero_tuples = tuple(
        neighbors
        for neighbors in itertools.product(AXES, repeat=6)
        if six_neighbor_normalizer(neighbors, Fraction(1)) == 0
    )
    permutations = set(itertools.permutations(AXES))
    ok = len(zero_tuples) == math.factorial(6) == 720 and set(zero_tuples) == permutations
    checks.check(
        "six_axis_endpoint_zero_normalizers",
        "exhaustive 6^6 scan finds exactly 720 zeros, precisely the permutations containing all six antipodes",
        ok,
    )


def six_axis_north_probability(variable_neighbor: Sequence[int | Fraction]) -> tuple[Fraction, Fraction]:
    neighbors = ((0, 0, 1),) * 5 + (tuple(variable_neighbor),)
    weights = tuple(
        math.prod(phi(candidate, neighbor, Fraction(1)) for neighbor in neighbors)
        for candidate in AXES
    )
    total = sum(weights, Fraction(0))
    numerator = sum(
        (weight for candidate, weight in zip(AXES, weights) if candidate[2] > 0),
        Fraction(0),
    )
    return total / 6, numerator / total


def haar_north_probability(variable_z: int) -> tuple[sp.Expr, sp.Expr]:
    z = sp.symbols("z", real=True)
    weight = (1 + z) ** 5 * (1 + variable_z * z)
    normalizer = sp.simplify(sp.integrate(weight, (z, -1, 1)) / 2)
    numerator = sp.simplify(sp.integrate(weight, (z, 0, 1)) / 2)
    return normalizer, sp.simplify(numerator / normalizer)


def gate_posterior_affinity(checks: Checks) -> None:
    six_zero, six_p_zero = six_axis_north_probability((0, 0, 0))
    six_plus, six_p_plus = six_axis_north_probability((0, 0, 1))
    six_minus, six_p_minus = six_axis_north_probability((0, 0, -1))
    six_gap = six_p_zero - (six_p_plus + six_p_minus) / 2
    haar_zero, haar_p_zero = haar_north_probability(0)
    haar_plus, haar_p_plus = haar_north_probability(1)
    haar_minus, haar_p_minus = haar_north_probability(-1)
    haar_gap = sp.simplify(haar_p_zero - (haar_p_plus + haar_p_minus) / 2)
    ok = (
        (six_zero, six_plus, six_minus)
        == (Fraction(6), Fraction(34, 3), Fraction(2, 3))
        and (six_p_zero, six_p_plus, six_p_minus)
        == (Fraction(8, 9), Fraction(16, 17), Fraction(0))
        and six_gap == Fraction(64, 153)
        and (haar_zero, haar_plus, haar_minus)
        == (sp.Rational(16, 3), sp.Rational(64, 7), sp.Rational(32, 21))
        and (haar_p_zero, haar_p_plus, haar_p_minus)
        == (sp.Rational(63, 64), sp.Rational(127, 128), sp.Rational(15, 16))
        and haar_gap == sp.Rational(5, 256)
    )
    checks.check(
        "posterior_affinity_normalizer_controls",
        "a separate five-+z executable posterior has six-axis midpoint gap 64/153 and positive-Haar-measure hemisphere gap 5/256",
        ok,
    )


def gauge_polynomial(
    left: Sequence[object], right: Sequence[int | Fraction]
) -> object:
    """One-sided gauge used both numerically and under Haar integration."""

    h_right = 1 + sum(Fraction(value) ** 2 for value in right)
    overlap = sum(
        (component * Fraction(value) for component, value in zip(left, right)),
        0,
    )
    return h_right * (1 + overlap)


def gauge_factor(
    left: Sequence[int | Fraction], right: Sequence[int | Fraction]
) -> Fraction:
    return Fraction(gauge_polynomial(left, right))


def gauge_haar_mass(right: Sequence[int | Fraction]) -> sp.Expr:
    nx, ny, nz = sp.symbols("nx ny nz", real=True)
    density = sp.expand(gauge_polynomial((nx, ny, nz), right))
    return sp.simplify(density.subs({nx: 0, ny: 0, nz: 0}))


def gate_gauge_control(checks: Checks) -> None:
    pure_probabilities_match = all(
        tuple(
            gauge_factor(candidate, fixed)
            / sum((gauge_factor(other, fixed) for other in AXES), Fraction(0))
            for candidate in AXES
        )
        == tuple(phi(candidate, fixed, Fraction(1)) / 6 for candidate in AXES)
        for fixed in AXES
    )
    z_axis = (0, 0, 1)
    raw_mixed = gauge_factor(z_axis, (0, 0, 0))
    raw_average = (
        gauge_factor(z_axis, z_axis) + gauge_factor(z_axis, (0, 0, -1))
    ) / 2
    haar_mass_pure = gauge_haar_mass(z_axis)
    haar_mass_mixed = gauge_haar_mass((0, 0, 0))
    ok = (
        pure_probabilities_match
        and raw_mixed == 1
        and raw_average == 2
        and haar_mass_pure == 2
        and haar_mass_mixed == 1
        and haar_mass_pure != haar_mass_mixed
    )
    checks.check(
        "gauge_related_raw_factor_type_control",
        "g(s)(1+r.s) preserves normalized pure six-menu probabilities; symbolic Haar masses are 2/1 and mixed raw value 1 differs from endpoint average 2",
        ok,
    )


@dataclass(frozen=True)
class PortBlock:
    trial: int

    def site(self, role: str) -> int:
        offsets = {"H": 0, "R": 1, "O": 2, "C": 3, "H_next": 4}
        return 4 * self.trial + offsets[role]

    def record_sites(self) -> frozenset[int]:
        return frozenset((self.site("R"), self.site("O")))

    def active_stencil(self) -> frozenset[int]:
        record_sites = self.record_sites()
        return frozenset(
            site + delta for site in record_sites for delta in (-1, 0, 1)
        )


Symbol = tuple[int, str]
History = tuple[Symbol, ...]


@dataclass(frozen=True, order=True)
class RoleDependency:
    source_role: str
    target_role: str
    target_delta: int


@dataclass(frozen=True)
class FullActiveKernelSchedule:
    name: str
    dependencies: tuple[RoleDependency, ...]
    translation_period: int
    active_roles: tuple[str, ...]
    archive_roles: tuple[str, ...]
    fixed_templates: tuple[tuple[str, str], ...]
    fresh_role: str


GOOD_DEPENDENCIES = (
    RoleDependency("G", "R", 0),
    RoleDependency("G", "O", 0),
    RoleDependency("H", "R", 0),
    RoleDependency("H", "O", 0),
    RoleDependency("R", "O", 0),
    RoleDependency("C", "O", 0),
    RoleDependency("H", "H", 1),
    RoleDependency("C", "H", 1),
)

SUPPLIED_ACTIVE_SCHEDULE = FullActiveKernelSchedule(
    name="supplied_translation_invariant_no_relay_schedule",
    dependencies=GOOD_DEPENDENCIES,
    translation_period=4,
    active_roles=("H", "R", "O", "C"),
    archive_roles=("R", "O"),
    fixed_templates=(("H", "ready"), ("C", "fixed_program")),
    fresh_role="G",
)

REMOTE_RELAY_SCHEDULE = replace(
    SUPPLIED_ACTIVE_SCHEDULE,
    name="hostile_O_to_C_to_H_to_R_relay",
    dependencies=GOOD_DEPENDENCIES + (RoleDependency("O", "C", 0),),
)


def instantiated_dependency_edges(
    schedule: FullActiveKernelSchedule, horizon: int
) -> frozenset[tuple[tuple[int, str], tuple[int, str]]]:
    edges = set()
    for trial in range(horizon + 1):
        for dependency in schedule.dependencies:
            target_trial = trial + dependency.target_delta
            if 0 <= target_trial <= horizon:
                edges.add(
                    (
                        (trial, dependency.source_role),
                        (target_trial, dependency.target_role),
                    )
                )
    return frozenset(edges)


def archive_reaches_future_active(
    schedule: FullActiveKernelSchedule, horizon: int = 3
) -> bool:
    edges = instantiated_dependency_edges(schedule, horizon)
    adjacency: dict[tuple[int, str], set[tuple[int, str]]] = {}
    for source, target in edges:
        adjacency.setdefault(source, set()).add(target)
    frontier = [(0, role) for role in schedule.archive_roles]
    visited = set(frontier)
    while frontier:
        source = frontier.pop()
        for target in adjacency.get(source, set()):
            if target[0] >= 1 and target[1] in schedule.active_roles:
                return True
            if target not in visited:
                visited.add(target)
                frontier.append(target)
    return False


def screening_induction_certificate(schedule: FullActiveKernelSchedule) -> bool:
    """Finite role-template conditions sufficient for every translated trial."""

    roles = set(schedule.active_roles) | {schedule.fresh_role}
    dependencies_typed = all(
        dependency.source_role in roles
        and dependency.target_role in schedule.active_roles
        and dependency.target_delta in (0, 1)
        for dependency in schedule.dependencies
    )
    completed_archive_cannot_escape = all(
        dependency.source_role not in schedule.archive_roles
        or (
            dependency.source_role == "R"
            and dependency.target_role == "O"
            and dependency.target_delta == 0
        )
        for dependency in schedule.dependencies
    )
    record_first_flow = (
        RoleDependency("R", "O", 0) in schedule.dependencies
        and RoleDependency("O", "R", 0) not in schedule.dependencies
    )
    fresh_is_local = all(
        dependency.source_role != schedule.fresh_role
        or (
            dependency.target_delta == 0
            and dependency.target_role in schedule.archive_roles
        )
        for dependency in schedule.dependencies
    )
    return (
        schedule.name == CANDIDATE_IMPORTS.full_active_kernel_schedule
        and schedule.translation_period == 4
        and schedule.active_roles == ("H", "R", "O", "C")
        and schedule.archive_roles == ("R", "O")
        and schedule.fixed_templates
        == (("H", "ready"), ("C", "fixed_program"))
        and schedule.fresh_role == "G"
        and schedule.dependencies == GOOD_DEPENDENCIES
        and dependencies_typed
        and completed_archive_cannot_escape
        and record_first_flow
        and fresh_is_local
        and not archive_reaches_future_active(schedule, horizon=3)
    )


@dataclass(frozen=True)
class ProcessState:
    trial: int
    archive: History
    head: str = "ready"
    program: str = "fixed_program"
    innovation_cursor: int = 0


def process_state(history: History = ()) -> ProcessState:
    return ProcessState(
        trial=len(history),
        archive=history,
        innovation_cursor=len(history),
    )


def archive_sites(history: History) -> frozenset[int]:
    return frozenset(
        site
        for trial in range(len(history))
        for site in PortBlock(trial).record_sites()
    )


def embedded_archive(history: History) -> dict[int, int | str]:
    archive: dict[int, int | str] = {}
    for trial, (bit, outcome) in enumerate(history):
        block = PortBlock(trial)
        archive[block.site("R")] = bit
        archive[block.site("O")] = outcome
    return archive


def active_interface_signature(
    state: ProcessState, schedule: FullActiveKernelSchedule
) -> tuple[
    tuple[int, ...],
    tuple[tuple[int, int | str], ...],
    tuple[tuple[str, str], ...],
    str,
]:
    block = PortBlock(state.trial)
    origin = 4 * block.trial
    relative_stencil = tuple(sorted(site - origin for site in block.active_stencil()))
    archive = embedded_archive(state.archive)
    visible_archive = tuple(
        sorted(
            (site - origin, value)
            for site, value in archive.items()
            if site in block.active_stencil()
        )
    )
    return (
        relative_stencil,
        visible_archive,
        schedule.fixed_templates,
        "fresh" if state.innovation_cursor == state.trial else "stale",
    )


def one_port_law(rows: Sequence[Sequence[Fraction]] = PREPARATION_ROWS) -> dict[Symbol, Fraction]:
    return {
        (bit, outcome): Fraction(1, 2) * rows[bit][index]
        for bit in (0, 1)
        for index, outcome in enumerate(OUTCOMES)
    }


def active_quotient(
    state: ProcessState, schedule: FullActiveKernelSchedule
) -> tuple[tuple[int, ...], tuple[tuple[str, str], ...], str, str, str]:
    signature = active_interface_signature(state, schedule)
    return signature[0], signature[2], state.head, state.program, signature[3]


def relay_payload(
    state: ProcessState, schedule: FullActiveKernelSchedule
) -> str | None:
    if not state.archive or not archive_reaches_future_active(schedule, horizon=2):
        return None
    return state.archive[-1][1]


def conditional_symbol_law(
    state: ProcessState,
    schedule: FullActiveKernelSchedule = SUPPLIED_ACTIVE_SCHEDULE,
) -> dict[Symbol, Fraction]:
    if (
        state.head != "ready"
        or state.program != "fixed_program"
        or state.innovation_cursor != state.trial
    ):
        return {}
    payload = relay_payload(state, schedule)
    if payload is None:
        return one_port_law()
    copied_bit = OUTCOMES.index(payload)
    return {
        (copied_bit, outcome): PREPARATION_ROWS[copied_bit][index]
        for index, outcome in enumerate(OUTCOMES)
    }


def candidate_transition(
    state: ProcessState,
    schedule: FullActiveKernelSchedule = SUPPLIED_ACTIVE_SCHEDULE,
) -> dict[Symbol, tuple[Fraction, ProcessState]]:
    return {
        symbol: (
            probability,
            ProcessState(
                trial=state.trial + 1,
                archive=state.archive + (symbol,),
                head=state.head,
                program=state.program,
                innovation_cursor=state.innovation_cursor + 1,
            ),
        )
        for symbol, probability in conditional_symbol_law(state, schedule).items()
    }


def next_port_law(
    history: History,
    schedule: FullActiveKernelSchedule = SUPPLIED_ACTIVE_SCHEDULE,
) -> dict[Symbol, Fraction]:
    return conditional_symbol_law(process_state(history), schedule)


def histories(length: int) -> Iterable[History]:
    return itertools.product(tuple(one_port_law()), repeat=length)


def remote_relay_nn_distances(trial: int = 0) -> tuple[int, int, int]:
    current = PortBlock(trial)
    following = PortBlock(trial + 1)
    return (
        abs(current.site("O") - current.site("C")),
        abs(current.site("C") - following.site("H")),
        abs(following.site("H") - following.site("R")),
    )


def gate_fresh_port_geometry(checks: Checks) -> None:
    blocks = tuple(PortBlock(trial) for trial in range(9))
    translated = all(
        tuple(block.site(role) - 4 * block.trial for role in ("H", "R", "O", "C", "H_next"))
        == (0, 1, 2, 3, 4)
        for block in blocks
    )
    separated = all(
        archive_sites(tuple(((0, "north"),) * trial)).isdisjoint(
            PortBlock(trial).active_stencil()
        )
        for trial in range(1, 9)
    )
    gaps = tuple(
        min(PortBlock(trial).active_stencil())
        - max(archive_sites(tuple(((0, "north"),) * trial)))
        for trial in range(1, 9)
    )
    shared_heads = all(
        PortBlock(trial).site("H_next") == PortBlock(trial + 1).site("H")
        for trial in range(8)
    )
    ok = translated and separated and set(gaps) == {2} and shared_heads
    checks.check(
        "translated_radius_one_fresh_port_geometry",
        "H,R,O,C,H' lie at 4t..4t+4; archived variable R/O sites are disjoint from the next R/O NN stencils with exact gap 2",
        ok,
    )


def gate_strong_lumpability(checks: Checks) -> None:
    laws_by_depth = []
    for length in range(5):
        laws = {
            tuple(sorted(next_port_law(history).items())) for history in histories(length)
        }
        laws_by_depth.append(laws)
    geometry_local = all(
        archive_sites(history).isdisjoint(PortBlock(len(history)).active_stencil())
        for length in range(5)
        for history in histories(length)
    )
    translated_interfaces = {
        active_quotient(process_state(history), SUPPLIED_ACTIVE_SCHEDULE)
        for length in range(5)
        for history in histories(length)
    }
    fixed_kernel = all(len(laws) == 1 for laws in laws_by_depth)
    representative_a = ((0, "north"),)
    representative_b = ((0, "south"),)
    variable_archive = representative_a != representative_b
    same_active_law = next_port_law(representative_a) == next_port_law(representative_b)
    structural_induction = screening_induction_certificate(SUPPLIED_ACTIVE_SCHEDULE)
    relay_path_present = archive_reaches_future_active(
        REMOTE_RELAY_SCHEDULE, horizon=2
    )
    relay_is_nearest_neighbor = remote_relay_nn_distances() == (1, 1, 1)
    relay_rejected = not screening_induction_certificate(REMOTE_RELAY_SCHEDULE)
    relay_breaks_fibre = next_port_law(
        representative_a, REMOTE_RELAY_SCHEDULE
    ) != next_port_law(representative_b, REMOTE_RELAY_SCHEDULE)
    transition = candidate_transition(process_state(representative_a))
    stateful_append = all(
        next_state.archive == representative_a + (symbol,)
        and next_state.trial == 2
        and next_state.innovation_cursor == 2
        for symbol, (_, next_state) in transition.items()
    )
    ok = (
        geometry_local
        and len(translated_interfaces) == 1
        and fixed_kernel
        and variable_archive
        and same_active_law
        and structural_induction
        and relay_path_present
        and relay_is_nearest_neighbor
        and relay_rejected
        and relay_breaks_fibre
        and stateful_append
    )
    checks.check(
        "archive_fibre_strong_lumpability",
        "explicit translated dependency schedule yields a stateful quotient kernel and all-N screening induction; exact fibres through depth 4 agree and the three-NN-edge O-C-H-R relay breaks them",
        ok,
    )


def cylinder_probability(
    history: History,
    schedule: FullActiveKernelSchedule = SUPPLIED_ACTIVE_SCHEDULE,
) -> Fraction:
    probability = Fraction(1)
    state = process_state()
    for symbol in history:
        transition = candidate_transition(state, schedule)
        if symbol not in transition:
            return Fraction(0)
        weight, state = transition[symbol]
        probability *= weight
    return probability


def append_record(history: History, symbol: Symbol, *, erase: bool = False) -> History:
    return (symbol,) if erase else history + (symbol,)


def gate_projective_cylinders(checks: Checks) -> None:
    port_law = one_port_law()
    alphabet = tuple(port_law)
    row_sum = sum(port_law.values(), Fraction(0))
    fine = cylinder_mixture(PREPARATION_ROWS).fine
    inherited_edge_kernel = port_law == {
        (bit, outcome): weight for bit, outcome, weight in fine
    }
    projective = all(
        sum(
            (cylinder_probability(prefix + (symbol,)) for symbol in alphabet),
            Fraction(0),
        )
        == cylinder_probability(prefix)
        for length in range(6)
        for prefix in histories(length)
    )
    normalized = all(
        sum((cylinder_probability(history) for history in histories(length)), Fraction(0))
        == 1
        for length in range(7)
    )
    permanent = all(
        candidate_transition(process_state(history))[symbol][1].archive[: len(history)]
        == history
        for length in range(5)
        for history in histories(length)
        for symbol in alphabet
    )
    conditional_iteration_matches = all(
        cylinder_probability(history)
        == math.prod(port_law[symbol] for symbol in history)
        for length in range(6)
        for history in histories(length)
    )
    stateful_rows_normalized = all(
        sum(
            (
                probability
                for probability, _ in candidate_transition(
                    process_state(history)
                ).values()
            ),
            Fraction(0),
        )
        == 1
        for length in range(5)
        for history in histories(length)
    )
    symbolic_mass = sp.symbols("P", nonnegative=True)
    universal_step = sp.simplify(symbolic_mass * row_sum - symbolic_mass) == 0
    ok = (
        inherited_edge_kernel
        and row_sum == 1
        and projective
        and normalized
        and permanent
        and conditional_iteration_matches
        and stateful_rows_normalized
        and screening_induction_certificate(SUPPLIED_ACTIVE_SCHEDULE)
        and universal_step
    )
    checks.check(
        "projective_finite_cylinders_and_permanent_archive",
        "stateful conditional-kernel iteration reuses the same (1/2) integral_E phi dmu law, normalizes/projects through N=6/5, and the schedule plus row-sum induction covers every finite N",
        ok,
    )


def frozen_bit_probability(bits: Sequence[int]) -> Fraction:
    return Fraction(1, 2) if len(set(bits)) <= 1 else Fraction(0)


def parity_triple_probability(bits: Sequence[int]) -> Fraction:
    return Fraction(1, 4) if len(bits) == 3 and sum(bits) % 2 == 0 else Fraction(0)


def gate_memory_discriminators(checks: Checks) -> None:
    bit_pairs = tuple(itertools.product((0, 1), repeat=2))
    frozen_one_shot = tuple(frozen_bit_probability((bit,)) for bit in (0, 1))
    fresh_pair = {bits: Fraction(1, 4) for bits in bit_pairs}
    frozen_pair = {bits: frozen_bit_probability(bits) for bits in bit_pairs}
    triples = tuple(itertools.product((0, 1), repeat=3))
    parity = {bits: parity_triple_probability(bits) for bits in triples}
    one_marginals = all(
        sum((value for bits, value in parity.items() if bits[index] == bit), Fraction(0))
        == Fraction(1, 2)
        for index in range(3)
        for bit in (0, 1)
    )
    two_marginals = all(
        sum(
            (
                value
                for bits, value in parity.items()
                if bits[left] == a and bits[right] == b
            ),
            Fraction(0),
        )
        == Fraction(1, 4)
        for left, right in itertools.combinations(range(3), 2)
        for a, b in bit_pairs
    )
    triple_not_product = parity[(0, 0, 0)] == Fraction(1, 4) != Fraction(1, 8)
    ok = (
        frozen_one_shot == (Fraction(1, 2), Fraction(1, 2))
        and frozen_pair != fresh_pair
        and one_marginals
        and two_marginals
        and triple_not_product
    )
    checks.check(
        "frozen_and_pairwise_memory_discriminators",
        "frozen memory shares the fair one-shot law but differs at N=2; even-parity triples share all one/two marginals yet differ at N=3",
        ok,
    )


def mutation_literal_values() -> tuple[int, int]:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    dictionaries = [
        node.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "mutations"
            for target in node.targets
        )
        and isinstance(node.value, ast.Dict)
    ]
    literal_booleans = sum(
        isinstance(value, ast.Constant) and isinstance(value.value, bool)
        for dictionary in dictionaries
        for value in dictionary.values
    )
    return len(dictionaries), literal_booleans


def gate_hostile_mutations(checks: Checks) -> None:
    gaussian = gaussian_fair_data()
    mu = sp.Integer(1)
    mutated_half_mass = (1 - sp.erf(mu / sp.sqrt(2))) / 2
    target_thresholds = (sp.Rational(1, 3), sp.Rational(2, 3))
    bad_branch = execute_controller(0, supplied_branch=1)
    bad_order = execute_controller(0, control_first=True)
    forged = cylinder_mixture(PREPARATION_ROWS, forged=True)
    incomplete_jensen = replace(
        JENSEN_PREMISES, complete_domain_source="missing_complete_domain"
    )
    anisotropic = ((1, 0, 0), (0, 2, 0), (0, 0, 3))
    vector = (1, 0, 0)
    c4 = cycle_partition_formula(4, Fraction(1))
    zero_count = sum(
        six_neighbor_normalizer(neighbors, Fraction(1)) == 0
        for neighbors in itertools.product(AXES, repeat=6)
    )
    _, six_p_zero = six_axis_north_probability((0, 0, 0))
    _, six_p_plus = six_axis_north_probability((0, 0, 1))
    _, six_p_minus = six_axis_north_probability((0, 0, -1))
    representative = ((0, "north"), (1, "south"))
    symbol = (0, "south")
    parity_product_claim = parity_triple_probability((0, 0, 0)) == Fraction(1, 8)
    frozen_fresh_claim = frozen_bit_probability((0, 1)) == Fraction(1, 4)
    archives = (((0, "north"),), ((0, "south"),))
    archive_sensitive_claim = next_port_law(
        archives[0], REMOTE_RELAY_SCHEDULE
    ) == next_port_law(archives[1], REMOTE_RELAY_SCHEDULE)
    bad_midpoint_import = replace(
        CANDIDATE_IMPORTS,
        relative_midpoint_interface="derived_from_cylinder_addition",
    )
    bad_sufficiency_import = replace(
        CANDIDATE_IMPORTS,
        local_channel_state_sufficiency="derived_from_equal_local_marginals",
    )
    bad_schedule_import = replace(
        CANDIDATE_IMPORTS,
        full_active_kernel_schedule="derived_from_one_step_radius_one_gap",
    )
    stale_innovation_state = replace(process_state(), innovation_cursor=1)
    identity = sp.eye(2)
    rho_zero = sp.diag(1, 0)
    rho_one = sp.diag(0, 1)
    omega_mix = (
        sp.kronecker_product(rho_zero, rho_zero)
        + sp.kronecker_product(rho_one, rho_one)
    ) / 2
    omega_direct = sp.kronecker_product(identity / 2, identity / 2)
    decoupled_rows = (
        (Fraction(1, 2), Fraction(1, 2)),
        (Fraction(1, 2), Fraction(1, 2)),
    )
    registry = json.loads(git_bytes(f"{CANONICAL_MAIN}:{REGISTRY_PATH}"))
    state = prereg_text("STATE.yaml")
    trace = prereg_text("TRACE_GATE.md")

    mutations = {
        "center_dependent_imaginary_mean_stays_fair": sp.simplify(mutated_half_mass - gaussian["half_mass"]) == 0,
        "target_dependent_threshold_is_fixed_half": all(value == sp.Rational(1, 2) for value in target_thresholds),
        "supplied_branch_routes_from_record": valid_record_first(bad_branch),
        "control_before_record_is_record_first": valid_record_first(bad_order),
        "desired_coarse_equation_is_fine_marginal": valid_cylinder_mixture(forged, PREPARATION_ROWS),
        "cylinder_addition_derives_midpoint_equivalence": candidate_imports_valid(bad_midpoint_import),
        "equal_local_marginals_derive_state_sufficiency": candidate_imports_valid(bad_sufficiency_import),
        "local_channel_identity_is_global_record_identity": omega_mix == omega_direct,
        "unlinked_rows_are_the_phi_cylinder": cylinder_mixture(decoupled_rows).fine
        == cylinder_mixture(PREPARATION_ROWS).fine,
        "incomplete_dyadic_domain_closes_jensen": bounded_midpoint_jensen_applies(incomplete_jensen),
        "nonzero_cubic_invariant_vector": cubic_invariant(vector, ((1, 0, 0), (0, 1, 0), (0, 0, 1))),
        "anisotropic_cubic_commutant": cubic_invariant((0, 0, 0), anisotropic),
        "raw_area_measure_is_unit_mass": sp.Eq(4 * sp.pi, 1),
        "gauge_raw_factor_is_normalized": gauge_haar_mass((0, 0, 1)) == 1,
        "tree_leaf_proof_normalizes_cycle": c4 == 1,
        "cycle_partition_correction_vanishes": c4 - 1 == 0,
        "six_axis_zero_tuples_absent": zero_count == 0,
        "generic_posterior_is_affine": six_p_zero - (six_p_plus + six_p_minus) / 2 == 0,
        "record_erasure_preserves_archive": append_record(representative, symbol, erase=True)[: len(representative)] == representative,
        "one_two_marginals_certify_product": parity_product_claim,
        "frozen_memory_is_fresh_product": frozen_fresh_claim,
        "archive_copy_relay_is_lumpable": archive_sensitive_claim,
        "one_step_gap_supplies_full_schedule": candidate_imports_valid(bad_schedule_import),
        "remote_relay_preserves_worldtube_screening": screening_induction_certificate(REMOTE_RELAY_SCHEDULE),
        "stale_innovation_preserves_fresh_port_law": conditional_symbol_law(stale_innovation_state)
        == one_port_law(),
        "target_name_selects_unique_lambda": len({Fraction(-1), Fraction(0), Fraction(1)}) == 1,
        "tree_product_is_autonomous_z3": direct_cycle_partition(4, Fraction(1)) == 1,
        "controller_is_registered_axiom_or_primitive": any("controller" in name for name in registry["canonical_ids"]),
        "audit_promotion_authorized": "audit_edit_authorized: true" in state,
        "obligation_retired": "obligation_retirement_claimed: true" in state,
        "gravity_trace_reached": "target_claim_id: gravity" in trace,
        "toe_score_promotion_authorized": "toe_score_edit_authorized: true" in state,
    }
    rejected = sum(not bool(value) for value in mutations.values())
    dictionaries, literal_booleans = mutation_literal_values()
    ok = (
        rejected == len(mutations)
        and len(mutations) >= 19
        and dictionaries == 1
        and literal_booleans == 0
    )
    checks.check(
        "designated_hostile_mutations",
        f"{rejected}/{len(mutations)} causal, analytic, factor, reset, topology, and governance mutations rejected; 0 literal Boolean verdicts",
        ok,
    )


def main() -> int:
    checks = Checks()
    print(
        "scope: exact candidate-law construction; formation/controller/full domains/"
        "relative active-interface equivalence/local channel sufficiency/full active schedule/fresh bank/lambda/tree-ray geometry are supplied"
    )
    print(
        "typing: Gaussian statistic is a non-Born fair writer; Haar density uses dmu=dOmega/4pi;"
        " executed joint domains are finite rooted trees, with a separate cycle control"
    )
    print(
        "governance: predictive fresh-port renewal preserves all old Records; author status is"
        " conditional-support and TOE scores remain unchanged"
    )
    gates = (
        gate_source_identity,
        gate_authority_scope,
        gate_upstream_gaussian,
        gate_gaussian_fair_record,
        gate_record_first_cylinders,
        gate_midpoint_equivalence_boundary,
        gate_local_channel_global_archive_control,
        gate_dyadic_jensen,
        gate_cubic_commutant,
        gate_haar_edge,
        gate_six_axis_kernel,
        gate_tree_normalization,
        gate_cycle_control,
        gate_six_axis_zeros,
        gate_posterior_affinity,
        gate_gauge_control,
        gate_fresh_port_geometry,
        gate_strong_lumpability,
        gate_projective_cylinders,
        gate_memory_discriminators,
        gate_hostile_mutations,
    )
    for gate in gates:
        gate(checks)

    joint_exact = all(checks.results.values())
    print(
        "per_element: checked — Gaussian scalar fairness, Haar-density positivity, "
        "endpoint zeros, and the raw-factor gauge witness were evaluated exactly"
    )
    print(
        "per_site: checked — one Record-first active port, its relative channel "
        "identity, and archive-distinguishing correlation were evaluated exactly"
    )
    print(
        "per_mode: checked — all 24 proper-cubic rotations, the rank-14 commutant, "
        "and the six-axis transition spectrum were evaluated exactly"
    )
    print(
        "per_block: checked — finite rooted-tree normalization, cycle corrections, "
        "six-neighbor zeros, stateful fresh-port cylinders, the all-N schedule "
        "certificate, and the three-edge relay discriminator were evaluated exactly"
    )
    print(
        "lattice_wide: checked and not executed — the run supplies a translated "
        "active-ray dependency schedule, abstract port kernel, and finite trees; a "
        "compiled full Z3 process and loopy finite-volume law are named next-target domains"
    )
    status = (
        "exact within declared candidate scope"
        if joint_exact
        else "one or more declared gates failed"
    )
    print(
        f"status: conditional-support — {status}; the global archive discriminator and supplied candidate inputs are explicit"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
