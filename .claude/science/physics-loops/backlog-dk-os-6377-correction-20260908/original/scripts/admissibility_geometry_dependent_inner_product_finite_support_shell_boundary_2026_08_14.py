#!/usr/bin/env python3
"""Block 101: test the geometry-dependent inner-product escape from Block 98.

The certificate derives an exact L=8 radius-one inconsistency, proves that the
full alias-ray solution is not a finite Laurent polynomial, and checks that the
formal inverse-symbol solution is singular on the physical massless shell.
The result closes only an inner-product-only repair of the fixed Block 95
matter action; changed actions, carriers, and calculi remain live.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import subprocess

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_GEOMETRY_DEPENDENT_INNER_PRODUCT_FINITE_SUPPORT_SHELL_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_INCIDENCE_SCALAR_NONLINEAR_WARD_CONSTANT_TRANSLATION_"
    "ALIASING_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_incidence_scalar_nonlinear_ward_constant_"
    "translation_aliasing_boundary_2026_08_14.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_incidence_scalar_nonlinear_ward_constant_"
    "translation_aliasing_boundary_2026_08_14.txt"
)

CURRENT_MAIN = "43ba5587944ffe0f43df10864c8348a99c17517b"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
PARENT_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_COMMIT = "77ecd6dd7e45488af335aec15ab64bc3ac855749"
PARENT_NOTE_BLOB = "1213794a9a4f9c4230b734e3f672cf0c93890b78"
PARENT_RUNNER_BLOB = "45d10132b62845996cb5e6c66c3333a15e09ac1d"
PARENT_CACHE_BLOB = "1b13780ee794572a3e49501949cc6a63ba80540f"

I = sp.I
PI = sp.pi
SQRT2 = sp.sqrt(2)
ETA = (1, 1, 1, -1)
R = (PI / 2, PI / 2, 0, 0)
KS = (
    (0, -PI / 2, 0, 0),
    (PI / 2, -PI / 2, 0, 0),
    (PI / 4, -3 * PI / 4, 0, 0),
    (PI / 2, -PI, 0, 0),
    (0, -PI, 0, 0),
)
OFFSETS = (
    (0, 0, 0, 0),
    (1, 0, 0, 0),
    (-1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, -1, 0, 0),
)


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


def mass_symbol(momentum: tuple[sp.Expr, ...]) -> sp.Expr:
    return sp.simplify(
        sum(
            ETA[index] * 4 * sp.sin(momentum[index] / 2) ** 2
            for index in range(4)
        )
    )


def translation_symbol(momentum: tuple[sp.Expr, ...]) -> sp.Expr:
    return sp.simplify(I * sp.sin(momentum[0]))


def centered_derivative(momentum: tuple[sp.Expr, ...]) -> tuple[sp.Expr, ...]:
    return tuple(
        sp.simplify(
            ETA[index] * sp.sin(momentum[index] + R[index] / 2)
        )
        for index in range(4)
    )


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


def radius_one_matrix_certificate(mutation: str) -> dict[str, object]:
    rows: list[list[sp.Expr]] = []
    targets: list[sp.Expr] = []
    levels: list[tuple[sp.Expr, sp.Expr]] = []
    derivative_rows: list[tuple[sp.Expr, ...]] = []

    for momentum in KS:
        outgoing = add(momentum, R)
        incoming_mass = mass_symbol(momentum)
        outgoing_mass = mass_symbol(outgoing)
        delta_d = sp.simplify(
            translation_symbol(outgoing) - translation_symbol(momentum)
        )
        derivative = centered_derivative(momentum)
        vertex = sp.simplify(derivative[0] ** 2)
        phases = [
            sp.exp(
                I
                * sum(momentum[index] * offset[index] for index in range(4))
            )
            for offset in OFFSETS
        ]
        rows.append(
            [sp.simplify(incoming_mass * delta_d * phase) for phase in phases]
            + [vertex]
        )
        targets.append(sp.simplify(vertex * delta_d))
        levels.append((incoming_mass, outgoing_mass))
        derivative_rows.append(derivative)

    matrix = sp.Matrix(rows)
    target = sp.Matrix(targets)
    if mutation == "alter_radius_one_matrix":
        matrix[0, 0] += 1

    expected_matrix = sp.Matrix(
        (
            (2 * I, 2 * I, 2 * I, 2, -2, sp.Rational(1, 2)),
            (-4 * I, 4, -4, -4, 4, sp.Rational(1, 2)),
            (0, 0, 0, 0, 0, 1),
            (-6 * I, 6, -6, 6 * I, 6 * I, sp.Rational(1, 2)),
            (4 * I, 4 * I, 4 * I, -4 * I, -4 * I, sp.Rational(1, 2)),
        )
    )
    expected_target = sp.Matrix((I / 2, -I / 2, 0, -I / 2, I / 2))
    left_null = sp.Matrix(
        (-2, -1, sp.Rational(2, 3), sp.Rational(2, 3), 1)
    )
    shared_geometry = all(
        derivative[2:] == (0, 0)
        and sp.simplify(derivative[0] + derivative[1]) == 0
        for derivative in derivative_rows
    )
    if mutation == "row_dependent_geometry_response":
        shared_geometry = False

    return {
        "matrix": matrix,
        "target": target,
        "expected_matrix": expected_matrix,
        "expected_target": expected_target,
        "equal_levels": all(left == right for left, right in levels),
        "shared_geometry": shared_geometry,
        "rank": matrix.rank(),
        "augmented_rank": matrix.row_join(target).rank(),
        "left_null": left_null.T * matrix == sp.zeros(1, matrix.cols),
        "left_target": sp.simplify((left_null.T * target)[0]),
    }


def radius_one_exhaustiveness_certificate(mutation: str) -> dict[str, object]:
    full_offsets = [(0, 0, 0, 0)]
    for axis in range(4):
        for sign in (-1, 1):
            offset = [0, 0, 0, 0]
            offset[axis] = sign
            full_offsets.append(tuple(offset))

    columns = []
    for offset in full_offsets:
        column = []
        for momentum in KS:
            outgoing = add(momentum, R)
            delta_d = sp.simplify(
                translation_symbol(outgoing) - translation_symbol(momentum)
            )
            column.append(
                sp.simplify(
                    mass_symbol(momentum)
                    * delta_d
                    * sp.exp(
                        I
                        * sum(
                            momentum[index] * offset[index]
                            for index in range(4)
                        )
                    )
                )
            )
        columns.append(sp.Matrix(column))

    full_span = sp.Matrix.hstack(*columns)
    reduced_span = sp.Matrix.hstack(*columns[:5])
    same_span = full_span.columnspace() == reduced_span.columnspace()
    if mutation == "invent_radius_one_solution":
        same_span = False
    return {
        "full_offsets": len(full_offsets),
        "full_rank": full_span.rank(),
        "reduced_rank": reduced_span.rank(),
        "same_span": same_span,
        "zt_collapse": all(
            columns[index] == columns[0] for index in (5, 6, 7, 8)
        ),
    }


def finite_laurent_certificate(mutation: str) -> dict[str, object]:
    z = sp.symbols("z")
    theta = sp.symbols("theta", real=True)
    ray = (theta - PI / 4, -theta - PI / 4, 0, 0)
    ray_out = add(ray, R)
    ray_mass = sp.trigsimp(sp.expand_trig(mass_symbol(ray)))
    ray_vertex = sp.trigsimp(centered_derivative(ray)[0] ** 2)
    ray_delta = sp.trigsimp(
        sp.expand_trig(translation_symbol(ray_out) - translation_symbol(ray))
    )
    denominator = SQRT2 * z**2 - 4 * z + SQRT2
    numerator = (z**2 - 1) ** 2
    gcd = sp.gcd(denominator, numerator, extension=SQRT2)
    required = sp.cancel(numerator / (4 * z * denominator))
    mass = 4 - SQRT2 * (z + 1 / z)
    vertex = sp.Rational(1, 2) - sp.Rational(1, 4) * (z**2 + z ** -2)
    identity = sp.simplify(mass * required - vertex) == 0
    not_laurent = gcd == 1 and denominator.subs(z, 0) != 0
    if mutation == "fake_laurent_divisibility":
        not_laurent = False
    return {
        "denominator": denominator,
        "numerator": numerator,
        "gcd": gcd,
        "ray_mass": sp.simplify(ray_mass - (4 - 2 * SQRT2 * sp.cos(theta)))
        == 0,
        "ray_vertex": sp.simplify(ray_vertex - sp.sin(theta) ** 2) == 0,
        "ray_delta": sp.simplify(ray_delta - SQRT2 * I * sp.cos(theta)) == 0,
        "midpoint_forces_geometry": ray_delta.subs(theta, PI / 2) == 0
        and ray_vertex.subs(theta, PI / 2) == 1,
        "identity": identity,
        "not_laurent": not_laurent,
        "required": required,
    }


def inverse_shell_certificate(mutation: str) -> dict[str, object]:
    mass_in, mass_out, vertex = sp.symbols("m_in m_out V", nonzero=True)
    formal = sp.Rational(1, 2) * vertex * (1 / mass_in + 1 / mass_out)
    mass = sp.symbols("m", nonzero=True)
    equal_level = sp.simplify(formal.subs({mass_in: mass, mass_out: mass}))

    k_minus = (-PI / 2, 0, 0, PI / 2)
    k_plus = (PI / 2, 0, 0, PI / 2)
    fixtures = []
    for momentum in (k_minus, k_plus):
        outgoing = add(momentum, R)
        derivative = centered_derivative(momentum)
        fixtures.append(
            (
                mass_symbol(momentum),
                mass_symbol(outgoing),
                sp.simplify(derivative[0] ** 2),
            )
        )

    epsilon = sp.symbols("epsilon", real=True)
    perturbed = (-PI / 2, 0, 0, PI / 2 + epsilon)
    residue = sp.simplify(
        sp.limit(
            epsilon
            * centered_derivative(perturbed)[0] ** 2
            / mass_symbol(perturbed),
            epsilon,
            0,
        )
    )
    shell_pole = (
        fixtures
        == [
            (0, 0, sp.Rational(1, 2)),
            (0, 4, sp.Rational(1, 2)),
        ]
        and residue == -sp.Rational(1, 4)
    )
    if mutation == "hide_massless_shell_pole":
        shell_pole = False
    return {
        "formal": formal,
        "equal_level": equal_level,
        "fixtures": fixtures,
        "residue": residue,
        "shell_pole": shell_pole,
        "off_shell_only": True,
    }


def scope_certificate(mutation: str) -> dict[str, bool]:
    note = " ".join(NOTE_PATH.read_text(encoding="utf-8").lower().split())
    result = {
        "fixed_contract": "inner-product-only repair of the fixed block95 coordinate action" in note,
        "radius_one": "rank(a)=4" in note and "rank([a|b])=5" in note,
        "finite_support": "no finite laurent polynomial" in note,
        "shell": "massless-shell pole" in note,
        "changed_action_live": "changing m0, d0, and v together" in note,
        "link_live": "link or multi-degree carrier" in note,
        "n1_n8": all(f"n{index}" in note for index in range(1, 9)),
        "not_gravity_no_go": "not a gravity no-go" in note,
        "axiom_unchanged": "no axiom amendment is justified" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": "no toe percentage moves" in note,
        "zero_e2e": "retained-positive end-to-end theory count remains zero" in note,
        "stop": "stop the inner-product-only patch" in note,
    }
    if mutation == "weaken_no_go_packet":
        result["n1_n8"] = False
    if mutation == "claim_gravity_no_go":
        result["not_gravity_no_go"] = False
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
            "alter_radius_one_matrix",
            "row_dependent_geometry_response",
            "invent_radius_one_solution",
            "fake_laurent_divisibility",
            "hide_massless_shell_pole",
            "weaken_no_go_packet",
            "claim_gravity_no_go",
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
        "A-current-authority-and-Block98-parent",
        "current axiom authority and the exact stacked Block98 parent are content-bound",
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

    matrix = radius_one_matrix_certificate(mutation)
    checks.check(
        "B-exact-L8-radius-one-inconsistency",
        "the derived five-mode radius-one system has rank four and augmented rank five",
        matrix["matrix"] == matrix["expected_matrix"]
        and matrix["target"] == matrix["expected_target"]
        and matrix["equal_levels"]
        and matrix["rank"] == 4
        and matrix["augmented_rank"] == 5
        and matrix["left_null"]
        and matrix["left_target"] == -I / 3,
        "rank(A)/rank([A|b])=4/5; lambda^T A=0 and lambda^T b=-i/3",
    )

    exhaustive = radius_one_exhaustiveness_certificate(mutation)
    checks.check(
        "C-radius-one-column-and-shared-R1-exhaustiveness",
        "all site, axial-link, and geometry-response columns collapse to the tested radius-one span",
        exhaustive["full_offsets"] == 9
        and exhaustive["full_rank"] == exhaustive["reduced_rank"]
        and exhaustive["same_span"]
        and exhaustive["zt_collapse"]
        and matrix["shared_geometry"],
        f"nine matter offsets reduce to rank {exhaustive['full_rank']}; one shared geometry coefficient serves all five rows",
    )

    laurent = finite_laurent_certificate(mutation)
    checks.check(
        "D-arbitrary-finite-support-Laurent-obstruction",
        "the required alias-ray inner-product symbol is rational and no finite Laurent polynomial",
        laurent["identity"]
        and laurent["ray_mass"]
        and laurent["ray_vertex"]
        and laurent["ray_delta"]
        and laurent["midpoint_forces_geometry"]
        and laurent["gcd"] == 1
        and laurent["not_laurent"],
        f"required P(z)={laurent['required']}; gcd(D,(z^2-1)^2)={laurent['gcd']}",
    )

    inverse = inverse_shell_certificate(mutation)
    checks.check(
        "E-formal-inverse-symbol-solution-and-massless-shell-pole",
        "the formal inverse-symbol coefficient solves the equal-level equation off shell but is singular on exact physical null modes",
        inverse["equal_level"] == sp.Symbol("V", nonzero=True) / sp.Symbol("m", nonzero=True)
        and inverse["off_shell_only"]
        and inverse["shell_pole"],
        f"shell fixtures={inverse['fixtures']}; transverse pole residue={inverse['residue']}",
    )

    reentry_matrix = radius_one_matrix_certificate("")
    reentry_laurent = finite_laurent_certificate("")
    reentry_inverse = inverse_shell_certificate("")
    checks.check(
        "F-physical-reentry-gate",
        "a gravity re-entry must change the action/carrier or prove bounded shell-regular skewness, reversal, Ward, source, recoil, and energy",
        reentry_matrix["shared_geometry"]
        and reentry_laurent["not_laurent"]
        and reentry_inverse["shell_pole"],
    )

    scope = scope_certificate(mutation)
    checks.check(
        "G-no-go-discipline-and-scope",
        "N1-N8 restrict the result to the inner-product-only fixed-action contract and preserve changed-action escapes",
        all(
            scope[key]
            for key in (
                "fixed_contract",
                "radius_one",
                "finite_support",
                "shell",
                "changed_action_live",
                "link_live",
                "n1_n8",
                "not_gravity_no_go",
                "stop",
            )
        ),
    )

    checks.check(
        "H-axiom-and-TOE-firewall",
        "the candidate failure causes no axiom amendment, retention, obligation retirement, or TOE score movement",
        scope["axiom_unchanged"]
        and scope["zero_retirement"]
        and scope["zero_score"]
        and scope["zero_e2e"],
    )

    print(
        f"AXIOM_AUTHORITY: origin/main={authority['origin_main']} axiom={CURRENT_AXIOM_BLOB}; Block98 parent={PARENT_COMMIT}"
    )
    print(
        "per_element: derived five exact L8 rows, six exhaustive radius-one columns, the Laurent denominator, and two exact null-shell fixtures"
    )
    print(
        "per_site: allowed arbitrary complex onsite and nearest-neighbour inner-product coefficients plus one shared geometry-only nonlinear response"
    )
    print(
        "per_mode: rank(A)/rank([A|b])=4/5, Laurent gcd=1, and the formal inverse solution has residue -1/4 at the massless shell"
    )
    print(
        "per_block: closed bounded finite-support shell-regular inner-product-only repair of the fixed Block95 M0/D0/V contract"
    )
    print(
        "lattice_wide: arbitrary L-independent finite support is excluded on the fixed alias ray; changed action/calculus/carrier, quasilocal domain changes, gravity completion, Record compilation, adoption, and retention remain open"
    )
    print(
        "RESULT: in the fixed-coordinate-action W-skew subcase, geometry-dependent inner product alone cannot repair the fixed Block95 nonlinear Ward identity with bounded finite support and regular physical massless modes"
    )
    print(
        "DECISION_CUT: stop the inner-product-only patch; re-enter through one action that changes M0, D0, and V together or through a link/multi-degree discrete calculus, then rederive source, recoil, Ward, shell, and energy"
    )
    print(
        "TOE: zero obligation retirement, zero retained-positive end-to-end theories, and no percentage movement"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
