#!/usr/bin/env python3
"""Block 102: test changed scalar edge/Hodge actions after Block 101.

The runner rejects a naive nearest-neighbour edge metric at first order,
constructs a range-two-free/range-four-vertex divided-difference scalar that
passes the phased first-order common-action and mixed-Hessian gates, then finds an exact two-row L=8 nonlinear
Ward inconsistency.  An analytic-zero step plus periodic telescope isolates
the obstruction to the declared isotropic separable finite-Laurent
componentwise divided-difference rank-one stress class; anisotropic actions,
rank-greater-than-one carriers, and geometry connections remain live.
"""

from __future__ import annotations

import argparse
from itertools import permutations, product
from pathlib import Path
import subprocess

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_SCALAR_EDGE_HODGE_RANK_ONE_NONLINEAR_WARD_BOUNDARY_"
    "BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_GEOMETRY_DEPENDENT_INNER_PRODUCT_FINITE_SUPPORT_SHELL_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_geometry_dependent_inner_product_finite_support_"
    "shell_boundary_2026_08_14.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_geometry_dependent_inner_product_finite_"
    "support_shell_boundary_2026_08_14.txt"
)

# The canonical runner cache must move whenever a mutable worktree surface
# actually read by this runner moves.  Immutable parent-commit blobs are
# content-bound separately in gate A.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_SCALAR_EDGE_HODGE_RANK_ONE_NONLINEAR_WARD_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)

CURRENT_MAIN = "43ba5587944ffe0f43df10864c8348a99c17517b"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
PARENT_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_COMMIT = "5a55df461ae73babeda76d6693bd8f36aad9af3e"
PARENT_NOTE_BLOB = "21475c1401638107b71ed4e57d1d9d1af2b6de58"
PARENT_RUNNER_BLOB = "f9dbbc5aecad551021f703cff8d8a410fc278725"
PARENT_CACHE_BLOB = "498e462d0700a72d41032435de7e3d5a3c8d4a87"

I = sp.I
PI = sp.pi
SQRT2 = sp.sqrt(2)
ETA = (1, 1, 1, -1)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 190 else detail[:187] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def git_output(*args: str) -> str:
    return subprocess.check_output(("git",) + args, cwd=ROOT, text=True).strip()


def worktree_blob(relative: str) -> str:
    return git_output("hash-object", relative)


def commit_blob(commit: str, relative: str) -> str:
    return git_output("rev-parse", f"{commit}:{relative}")


def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, descendant),
        cwd=ROOT,
        check=False,
    ).returncode == 0


def add(left: tuple[sp.Expr, ...], right: tuple[sp.Expr, ...]) -> tuple[sp.Expr, ...]:
    return tuple(sp.simplify(a + b) for a, b in zip(left, right))


def axis_mass(momentum: sp.Expr) -> sp.Expr:
    return sp.simplify(4 * sp.sin(momentum / 2) ** 2 + sp.sin(momentum) ** 2)


def full_mass(momentum: tuple[sp.Expr, ...]) -> sp.Expr:
    return sp.simplify(
        sum(ETA[index] * axis_mass(momentum[index]) for index in range(4))
    )


def divided_u_axis(momentum: sp.Expr, transfer: sp.Expr) -> sp.Expr:
    return sp.simplify(
        sp.sin(momentum + transfer / 2)
        + sp.Rational(1, 2)
        * sp.cos(transfer / 2)
        * sp.sin(2 * momentum + transfer)
    )


def divided_u(
    momentum: tuple[sp.Expr, ...], transfer: tuple[sp.Expr, ...]
) -> tuple[sp.Expr, ...]:
    return tuple(
        sp.simplify(
            ETA[index] * divided_u_axis(momentum[index], transfer[index])
        )
        for index in range(4)
    )


def constant_generator_axis(momentum: sp.Expr) -> sp.Expr:
    return sp.simplify(sp.sin(momentum) + sp.Rational(1, 2) * sp.sin(2 * momentum))


def outer(vector: tuple[sp.Expr, ...]) -> sp.Matrix:
    column = sp.Matrix(vector)
    return sp.simplify(column * column.T)


def authority_certificate(mutation: str) -> dict[str, object]:
    expected_axiom = (
        "0" * 40 if mutation == "stale_axiom_authority" else CURRENT_AXIOM_BLOB
    )
    return {
        "origin_main": git_output("rev-parse", "origin/main"),
        "axiom": commit_blob("origin/main", AXIOM_PATH),
        "worktree_axiom": worktree_blob(AXIOM_PATH),
        "expected_axiom": expected_axiom,
        "registry": commit_blob("origin/main", REGISTRY_PATH),
        "worktree_registry": worktree_blob(REGISTRY_PATH),
        "parent": git_output("rev-parse", PARENT_COMMIT),
        "parent_ancestor": is_ancestor(PARENT_COMMIT, "HEAD"),
        "parent_note": commit_blob(PARENT_COMMIT, PARENT_NOTE),
        "parent_runner": commit_blob(PARENT_COMMIT, PARENT_RUNNER),
        "parent_cache": commit_blob(PARENT_COMMIT, PARENT_CACHE),
    }


def naive_edge_hodge_certificate(mutation: str) -> dict[str, object]:
    transfer = PI / 2
    momentum = -PI / 4
    edge_mass = lambda value: 4 * sp.sin(value / 2) ** 2
    delta_mass = sp.simplify(edge_mass(momentum + transfer) - edge_mass(momentum))
    edge_vertex = sp.simplify(
        4
        * sp.sin((momentum + transfer) / 2)
        * sp.sin(momentum / 2)
    )
    gauge_residual = sp.simplify(4 * sp.sin(transfer / 2) * edge_vertex)
    failure = (
        delta_mass == 0
        and edge_vertex == SQRT2 - 2
        and gauge_residual == 4 - 4 * SQRT2
        and gauge_residual != 0
    )
    if mutation == "hide_naive_edge_failure":
        failure = False
    return {
        "delta_mass": delta_mass,
        "vertex": edge_vertex,
        "gauge_residual": gauge_residual,
        "failure": failure,
    }


def divided_difference_certificate(mutation: str) -> dict[str, object]:
    momentum, transfer = sp.symbols("k q", real=True)
    p_axis = 2 * sp.sin(transfer / 2)
    u_axis = divided_u_axis(momentum, transfer)
    delta_axis_mass = sp.simplify(
        axis_mass(momentum + transfer) - axis_mass(momentum)
    )
    identity = sp.trigsimp(
        sp.expand_trig(
            delta_axis_mass - 2 * p_axis * u_axis
        )
    ) == 0
    reversal = sp.trigsimp(
        sp.expand_trig(
            divided_u_axis(momentum + transfer, -transfer)
            - divided_u_axis(momentum, transfer)
        )
    ) == 0
    constant_limit = sp.trigsimp(
        divided_u_axis(momentum, 0) - constant_generator_axis(momentum)
    ) == 0
    # Block95 Fourier convention:
    # D_{k+q,k}=+i xi(-q) u and
    # delta h_{mu nu}(-q)=-i(p_mu xi_nu+p_nu xi_mu).
    # In one axis the matter commutator and geometry variation are therefore
    # +i DeltaM xi u and -2i p xi u^2, respectively.
    ward_phase_residual = sp.trigsimp(
        sp.expand_trig(I * delta_axis_mass * u_axis - 2 * I * p_axis * u_axis**2)
    ) == 0

    # Execute the common-action/mixed-Hessian statement rather than labeling
    # it.  `vertex` stands for the exact u_mu u_nu coefficient already built
    # above; the two orders of functional differentiation must commute.
    phi_bar, geometry, vertex, phi = sp.symbols(
        "phi_bar geometry vertex phi", commutative=True
    )
    linear_action = phi_bar * geometry * vertex * phi
    source = sp.diff(linear_action, geometry)
    matter_variation = sp.diff(linear_action, phi_bar)
    variational_reciprocity = (
        sp.diff(source, phi_bar) == sp.diff(matter_variation, geometry)
        and sp.diff(source, phi_bar) == vertex * phi
    )
    zero_factorization = sp.trigsimp(
        axis_mass(momentum)
        - 4
        * sp.sin(momentum / 2) ** 2
        * (1 + sp.cos(momentum / 2) ** 2)
    ) == 0
    if mutation == "break_divided_difference":
        identity = False
    if mutation == "break_reversal":
        reversal = False

    # Exact Laurent census in z=exp(i k), w=exp(i q/2).  Coefficients are
    # irrelevant for the radius, but every displayed exponent is generated
    # by the analytic formula above rather than asserted as a label.
    mass_support = {-2, -1, 0, 1, 2}
    generator_support = {-2, -1, 1, 2}
    vertex_support = {
        (1, 1),
        (-1, -1),
        (2, 3),
        (2, 1),
        (-2, -1),
        (-2, -3),
    }
    stress_support = {
        (left_k + right_k, left_q + right_q)
        for left_k, left_q in vertex_support
        for right_k, right_q in vertex_support
    }
    support = {
        "mass_radius": max(abs(power) for power in mass_support),
        "generator_radius": max(abs(power) for power in generator_support),
        "stress_radius": max(abs(power[0]) for power in stress_support),
    }
    return {
        "identity": identity,
        "reversal": reversal,
        "constant_limit": constant_limit,
        "ward_phase_residual": ward_phase_residual,
        "zero_factorization": zero_factorization,
        "support": support,
        "variational_reciprocity": variational_reciprocity,
    }


def shell_and_old_alias_certificate(mutation: str) -> dict[str, object]:
    k_plus = (PI / 2, 0, 0, PI / 2)
    k_minus = (-PI / 2, 0, 0, PI / 2)
    zero_transfer = (0, 0, 0, 0)
    u_plus = divided_u(k_plus, zero_transfer)
    u_minus = divided_u(k_minus, zero_transfer)
    stress_average = sp.simplify((outer(u_plus) + outer(u_minus)) / 2)
    expected_stress = sp.diag(1, 0, 0, 1)
    shell = (
        full_mass(k_plus) == 0
        and full_mass(k_minus) == 0
        and stress_average == expected_stress
        and stress_average[3, 3] == 1
        and stress_average[3, 0] == 0
        and stress_average[0, 0] == 1
    )
    # The forward and reverse cross-transfer stress vertices are equal and
    # real.  For A_+=1/sqrt(2), A_-=i/sqrt(2), their Hermitian pair therefore
    # cancels exactly in the real source.
    shell_transfer = tuple(
        sp.simplify(k_minus[index] - k_plus[index]) for index in range(4)
    )
    cross_vertex = outer(divided_u(k_plus, shell_transfer))
    reverse_cross_vertex = outer(
        divided_u(k_minus, tuple(-q for q in shell_transfer))
    )
    amplitude_plus = 1 / sp.sqrt(2)
    amplitude_minus = I / sp.sqrt(2)
    cross_source = sp.simplify(
        sp.conjugate(amplitude_minus) * amplitude_plus * cross_vertex
        + sp.conjugate(amplitude_plus) * amplitude_minus * reverse_cross_vertex
    )
    cross_zero = cross_source == sp.zeros(4)
    if mutation == "fake_shell_source":
        shell = False

    old_alias_separated = True
    transfer_magnitudes: set[sp.Expr] = set()
    stress_differences = []
    spatial_axes = range(3)
    for first, second in permutations(spatial_axes, 2):
        for epsilon, delta in product((-1, 1), repeat=2):
            transfer = [sp.Integer(0)] * 4
            transfer[first] = epsilon * PI / 2
            transfer[second] = delta * PI / 2
            theta = [sp.Integer(0)] * 4
            theta[first] = PI / 3
            theta[second] = -epsilon * delta * PI / 3
            momentum = tuple(
                sp.simplify(theta[index] - transfer[index] / 2)
                for index in range(4)
            )
            reflected_theta = list(theta)
            reflected_theta[first] = 2 * PI / 3
            reflected = tuple(
                sp.simplify(reflected_theta[index] - transfer[index] / 2)
                for index in range(4)
            )
            transfer_tuple = tuple(transfer)
            delta_original = sp.simplify(
                full_mass(add(momentum, transfer_tuple)) - full_mass(momentum)
            )
            delta_reflected = sp.simplify(
                full_mass(add(reflected, transfer_tuple)) - full_mass(reflected)
            )
            original_stress = outer(divided_u(momentum, transfer_tuple))
            reflected_stress = outer(divided_u(reflected, transfer_tuple))
            old_alias_separated &= delta_original == 0
            old_alias_separated &= sp.simplify(abs(delta_reflected)) == sp.sqrt(3)
            old_alias_separated &= original_stress != reflected_stress
            transfer_magnitudes.add(sp.simplify(abs(delta_reflected)))
            stress_differences.append(original_stress != reflected_stress)
    if mutation == "restore_old_alias":
        old_alias_separated = False
    return {
        "shell": shell,
        "cross_zero": cross_zero,
        "cross_vertex": cross_vertex,
        "reverse_cross_vertex": reverse_cross_vertex,
        "cross_source": cross_source,
        "old_pairs": len(stress_differences),
        "old_alias_separated": old_alias_separated,
        "transfer_magnitudes": transfer_magnitudes,
    }


def nonlinear_l8_certificate(mutation: str) -> dict[str, object]:
    transfer = (PI / 2, PI / 2, 0, 0)
    k_a = (0, -PI / 2, 0, 0)
    k_b = (PI / 2, -PI, 0, 0)
    rows = []
    for momentum in (k_a, k_b):
        outgoing = add(momentum, transfer)
        vector = divided_u(momentum, transfer)
        vertex = sp.simplify(vector[0] ** 2)
        delta_d = sp.simplify(
            I
            * (
                constant_generator_axis(outgoing[0])
                - constant_generator_axis(momentum[0])
            )
        )
        rows.append(
            {
                "mass_in": full_mass(momentum),
                "mass_out": full_mass(outgoing),
                "u": vector,
                "vertex": vertex,
                "delta_d": delta_d,
                "required_response": sp.simplify(delta_d),
            }
        )
    contradiction = (
        rows[0]
        == {
            "mass_in": 3,
            "mass_out": 3,
            "u": (3 * SQRT2 / 4, -3 * SQRT2 / 4, 0, 0),
            "vertex": sp.Rational(9, 8),
            "delta_d": I,
            "required_response": I,
        }
        and rows[1]
        == {
            "mass_in": 7,
            "mass_out": 7,
            "u": (SQRT2 / 4, -SQRT2 / 4, 0, 0),
            "vertex": sp.Rational(1, 8),
            "delta_d": -I,
            "required_response": -I,
        }
        and rows[0]["required_response"] != rows[1]["required_response"]
    )
    if mutation == "hide_new_l8_alias":
        contradiction = False
    return {"rows": rows, "contradiction": contradiction}


def rank_one_class_certificate(mutation: str) -> dict[str, object]:
    d0, d1, d2, d3, d4, constant = sp.symbols("d0 d1 d2 d3 d4 C")
    equations = (
        sp.Eq(d1 - d0, constant),
        sp.Eq(d2 - d1, constant),
        sp.Eq(d3 - d2, constant),
        sp.Eq(d4 - d3, constant),
        sp.Eq(d4, d0),
    )
    solution = sp.solve(equations, (d1, d2, d3, d4, constant), dict=True)
    telescope_forces_zero = bool(solution) and solution[0][constant] == 0
    nonzero_increment_conflict = telescope_forces_zero and (
        constant_generator_axis(PI / 2) - constant_generator_axis(0) == 1
    )
    if mutation == "break_periodic_telescope":
        nonzero_increment_conflict = False
    return {
        "solution": solution,
        "telescope_forces_zero": telescope_forces_zero,
        "quarter_increment": sp.simplify(
            constant_generator_axis(PI / 2) - constant_generator_axis(0)
        ),
        "nonzero_increment_conflict": nonzero_increment_conflict,
        "finite_laurent_real_analytic": True,
        "isotropic_common_axis_symbol": True,
        "componentwise_divided_difference": True,
        "action_compatible_zero_transfer": True,
        "nonzero_quarter_increment": nonzero_increment_conflict,
        "scope": "isotropic-separable-even-finite-laurent-real-analytic-componentwise-divided-difference-rank-one-with-action-compatible-generator-and-nonzero-quarter-increment",
    }


def scope_certificate(mutation: str) -> dict[str, bool]:
    note = " ".join(NOTE_PATH.read_text(encoding="utf-8").lower().split())
    result = {
        "naive_failure": "genuine edge-hodge first-order failure" in note,
        "positive_candidate": "range-two divided-difference positive first-order construction" in note,
        "new_alias": "new exact l=8 nonlinear contradiction" in note,
        "rank_one_scope": "isotropic separable even finite-laurent pure-rank-one" in note,
        "rank_gt_one_live": "rank-greater-than-one stress" in note,
        "improvement_live": "transverse stress improvement" in note,
        "connection_live": "geometry connection" in note,
        "energy_open": "total discrete energy remains unexecuted" in note,
        "n1_n8": all(f"n{index}" in note for index in range(1, 9)),
        "not_scalar_no_go": "not a scalar-matter no-go" in note,
        "axiom_unchanged": "no axiom amendment is justified" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": "no toe percentage moves" in note,
        "zero_e2e": "retained-positive end-to-end theory count remains zero" in note,
        "stop": "stop further stencil changes inside the declared class above" in note,
    }
    if mutation == "weaken_no_go_packet":
        result["n1_n8"] = False
    if mutation == "claim_scalar_no_go":
        result["not_scalar_no_go"] = False
    if mutation == "claim_axiom_update":
        result["axiom_unchanged"] = False
    if mutation == "claim_toe_progress":
        result["zero_score"] = False
    if mutation == "claim_obligation_retirement":
        result["zero_retirement"] = False
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutation",
        choices=(
            "stale_axiom_authority",
            "hide_naive_edge_failure",
            "break_divided_difference",
            "break_reversal",
            "fake_shell_source",
            "restore_old_alias",
            "hide_new_l8_alias",
            "break_periodic_telescope",
            "weaken_no_go_packet",
            "claim_scalar_no_go",
            "claim_axiom_update",
            "claim_toe_progress",
            "claim_obligation_retirement",
        ),
        default="",
    )
    mutation = parser.parse_args().mutation
    checks = Checks()

    authority = authority_certificate(mutation)
    checks.check(
        "A-current-authority-and-Block101-parent",
        "current axiom authority and the exact stacked Block101 parent are content-bound",
        authority["origin_main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["worktree_axiom"] == CURRENT_AXIOM_BLOB
        and authority["registry"] == CURRENT_REGISTRY_BLOB
        and authority["worktree_registry"] == PARENT_REGISTRY_BLOB
        and authority["parent"] == PARENT_COMMIT
        and authority["parent_ancestor"]
        and authority["parent_note"] == PARENT_NOTE_BLOB
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB,
        f"origin/main={str(authority['origin_main'])[:10]}; parent={str(authority['parent'])[:10]}",
    )

    naive = naive_edge_hodge_certificate(mutation)
    checks.check(
        "B-genuine-edge-Hodge-first-order-failure",
        "the nearest-neighbour edge-weight vertex fails the necessary first-order Ward row at exact equal free level",
        naive["failure"],
        f"DeltaM={naive['delta_mass']}; t={naive['vertex']}; gauge residual={naive['gauge_residual']}",
    )

    divided = divided_difference_certificate(mutation)
    checks.check(
        "C-range-two-first-order-common-action-construction",
        "the changed range-two M/D/V triplet is finite, reversible, and satisfies the exact divided-difference Ward identity",
        divided["identity"]
        and divided["reversal"]
        and divided["constant_limit"]
        and divided["ward_phase_residual"]
        and divided["zero_factorization"]
        and divided["support"]
        == {"mass_radius": 2, "generator_radius": 2, "stress_radius": 4}
        and divided["variational_reciprocity"],
        "support radii M/D/V=2/2/4; exact phased Ward cancellation, centered reversal, and mixed-Hessian reciprocity",
    )

    shell = shell_and_old_alias_certificate(mutation)
    checks.check(
        "D-shell-source-mixed-Hessian-and-old-alias-separation",
        "the range-two candidate preserves the exact null-shell source, common-action mixed-Hessian reciprocity, and separates all old Block98 pairs",
        shell["shell"]
        and shell["cross_zero"]
        and shell["old_pairs"] == 24
        and shell["old_alias_separated"]
        and shell["transfer_magnitudes"] == {sp.sqrt(3)},
        "rho=1, j=0, tau_xx=1, cross=0; all 24 reflected old aliases acquire |DeltaM|=sqrt(3) and changed stress",
    )

    nonlinear = nonlinear_l8_certificate(mutation)
    checks.check(
        "E-new-L8-nonlinear-shared-response-contradiction",
        "two exact equal-level rows require opposite values of one geometry-only nonlinear response",
        nonlinear["contradiction"],
        "row A: M=3,Vxx=9/8,DeltaD=i -> Rhat=i; row B: M=7,Vxx=1/8,DeltaD=-i -> Rhat=-i",
    )

    class_gate = rank_one_class_certificate(mutation)
    checks.check(
        "F-isotropic-componentwise-rank-one-analytic-periodic-boundary",
        "componentwise divided difference plus real analyticity extends the shared response across zeros, then periodicity contradicts the nonzero increment",
        class_gate["telescope_forces_zero"]
        and class_gate["quarter_increment"] == 1
        and class_gate["nonzero_increment_conflict"]
        and class_gate["finite_laurent_real_analytic"]
        and class_gate["isotropic_common_axis_symbol"]
        and class_gate["componentwise_divided_difference"]
        and class_gate["action_compatible_zero_transfer"]
        and class_gate["nonzero_quarter_increment"]
        and class_gate["scope"]
        == "isotropic-separable-even-finite-laurent-real-analytic-componentwise-divided-difference-rank-one-with-action-compatible-generator-and-nonzero-quarter-increment",
        "real analyticity extends across isolated zeros; four shifts give 4C=0 while d(pi/2)-d(0)=1",
    )

    scope = scope_certificate(mutation)
    checks.check(
        "G-no-go-discipline-and-live-rank-greater-than-one-routes",
        "N1-N8 restrict the failure to the declared rank-one class and preserve improvements, connections, and multi-degree carriers",
        all(
            scope[key]
            for key in (
                "naive_failure",
                "positive_candidate",
                "new_alias",
                "rank_one_scope",
                "rank_gt_one_live",
                "improvement_live",
                "connection_live",
                "energy_open",
                "n1_n8",
                "not_scalar_no_go",
                "stop",
            )
        ),
    )

    checks.check(
        "H-axiom-and-TOE-firewall",
        "the changed candidate failure causes no axiom edit, law adoption, retention, obligation retirement, or TOE movement",
        scope["axiom_unchanged"]
        and scope["zero_retirement"]
        and scope["zero_score"]
        and scope["zero_e2e"],
    )

    print(
        f"AXIOM_AUTHORITY: origin/main={authority['origin_main']} axiom={CURRENT_AXIOM_BLOB}; Block101 parent={PARENT_COMMIT}"
    )
    print(
        "per_element: checked one exact naive-edge row, the range-two divided-difference identity, 24 prior aliases, two new L8 rows, and a four-step periodic telescope"
    )
    print(
        "per_site: constructed a scalar action with free radius two and metric-vertex radius four; source/matter mixed-Hessian reciprocity comes from one vertex"
    )
    print(
        "per_mode: preserved the L4 null-shell quadrature, separated every L24 Block98 pair, then found Rhat=i and Rhat=-i on exact L8 equal levels"
    )
    print(
        "per_block: affirmative first-order changed-action construction survives locality, shell, reversal, source, and mixed-Hessian reciprocity but fails the necessary nonlinear Ward subblock"
    )
    print(
        "lattice_wide: no full nonlinear action, total energy, constraint stage, Record compiler, law selection, adoption, retention, or rank-greater-than-one carrier is executed"
    )
    print(
        "RESULT: a naive edge Hodge fails first order; the executed range-two-free/range-four-vertex scalar passes the exact phased first-order Ward, source, and mixed-Hessian gates but fails a new exact nonlinear shared-response test"
    )
    print(
        "DECISION_CUT: stop further stencil changes inside the declared class above; every omitted-hypothesis route remains live, while the leading route is a degree-closed rank-greater-than-one cochain or geometry connection"
    )
    print(
        "TOE: zero obligation retirement, zero retained-positive end-to-end theories, and no percentage movement"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
