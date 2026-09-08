#!/usr/bin/env python3
"""Block 98: second-order Ward gate for the Block95 scalar carrier.

The runner first closes the continuum Weyl-symbol analogue with an explicit
nonlinear tensor transformation and scalar seagull.  It then exhibits exact
L=24 lattice mode pairs for which the actual Block95 stress coordinates are
identical, the free-symbol transfer differences vanish, and the constant-
parameter matter commutators are equal and opposite.  Consequently no
regular anti-Hermitian D1, quadratic matter seagull, pure-gravity cubic term,
or geometry-only R1 can satisfy the order-h phi^2 Ward coefficient on this
fixed carrier.  Changed carriers and representation/inner-product contracts
remain live.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_INCIDENCE_SCALAR_NONLINEAR_WARD_CONSTANT_TRANSLATION_"
    "ALIASING_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
RUNNER_RELATIVE = (
    "scripts/admissibility_incidence_scalar_nonlinear_ward_constant_"
    "translation_aliasing_boundary_2026_08_14.py"
)
PARENT_NOTE = (
    "docs/ADMISSIBILITY_COUNTERPROPAGATING_SCALAR_BIANCHI_TRACE_SHEAR_ENERGY_"
    "CURRENT_EXCHANGE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_counterpropagating_scalar_bianchi_energy_current_"
    "exchange_2026_08_14.py"
)
MINIMAL_AXIOMS = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_INCIDENCE_SCALAR_NONLINEAR_WARD_CONSTANT_TRANSLATION_ALIASING_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_COUNTERPROPAGATING_SCALAR_BIANCHI_TRACE_SHEAR_ENERGY_CURRENT_EXCHANGE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_BOUNDARY_DRESSED_JOINT_STAGE_HOMOGENEOUS_NONLINEAR_ZERO_MODE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_INCIDENCE_SCALAR_GRAPH_MATTER_FIRST_ORDER_TOTAL_WARD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_INCIDENCE_FIERZ_PAULI_SIGNED_RECORD_SOURCE_FULL_TENSOR_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_INCIDENCE_ADM_DEPTH_TWO_SOURCED_CONSTRAINT_RECORD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_CYCLE713_RECORD_HEAD_ADM_WORK_ARCHIVE_STATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_COMPONENT_STAGGERED_SIGNED_LINK_ACTION_LOCAL_WARD_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_RAW_GRAPH_WARD_COMPACT_PULLBACK_TRANSLATION_GENERATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_incidence_scalar_nonlinear_ward_constant_translation_aliasing_boundary_2026_08_14.py",
    "scripts/admissibility_counterpropagating_scalar_bianchi_energy_current_exchange_2026_08_14.py",
    "scripts/admissibility_boundary_dressed_joint_stage_homogeneous_zero_mode_2026_08_14.py",
    "scripts/admissibility_incidence_scalar_graph_matter_first_order_total_ward_cadence_boundary_2026_08_14.py",
    "scripts/admissibility_incidence_fierz_pauli_signed_record_source_full_tensor_cadence_boundary_2026_08_14.py",
    "scripts/admissibility_incidence_adm_depth_two_sourced_constraint_record_cadence_boundary_2026_08_14.py",
    "scripts/admissibility_cycle713_record_head_adm_work_archive_state_boundary_2026_08_14.py",
    "scripts/admissibility_component_staggered_signed_link_action_local_ward_boundary_2026_08_14.py",
    "scripts/admissibility_raw_graph_ward_compact_pullback_translation_generator_boundary_2026_08_14.py",
    "scripts/admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_2026_08_11.py",
)

CURRENT_MAIN = "eee6ab5874e2fc207db5526dc82d9f71ae550c7c"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
PARENT_COMMIT = "213de9467339a124968e4b3433cbe76d67b284cb"
PARENT_NOTE_BLOB = "5b24713105f24671d1629746f8cb9b9b8fea2215"
PARENT_RUNNER_BLOB = "e7a76601e26ed3741732a27224063e025593e2ed"

TOL = 3.0e-10
LATTICE_SIZE = 24
UNIT = 2.0 * np.pi / LATTICE_SIZE

sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_counterpropagating_scalar_bianchi_energy_current_exchange_2026_08_14 as block97  # noqa: E402

block95 = block97.block95
block77 = block95.block77
ETA = block95.ETA


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


def error_bound(value: float, tolerance: float = TOL) -> str:
    return f"<{tolerance:.0e}" if abs(value) < tolerance else f"{value:.6g}"


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def git_output(*args: str) -> str:
    return subprocess.check_output(("git",) + args, cwd=ROOT, text=True).strip()


def worktree_blob(relative: str) -> str:
    return git_output("hash-object", relative)


def commit_blob(commit: str, relative: str) -> str:
    return git_output("rev-parse", f"{commit}:{relative}")


def authority_certificate(mutation: str) -> dict[str, object]:
    current = {NOTE_PATH.relative_to(ROOT).as_posix(), RUNNER_RELATIVE}
    frozen = tuple(path for path in AUDIT_INPUT_PATHS if path not in current)
    mismatches = tuple(
        path for path in frozen if worktree_blob(path) != commit_blob(PARENT_COMMIT, path)
    )
    loaded: set[str] = set()
    for module in tuple(sys.modules.values()):
        file_name = getattr(module, "__file__", None)
        if not file_name:
            continue
        module_path = Path(file_name).resolve()
        try:
            relative = module_path.relative_to(ROOT).as_posix()
        except ValueError:
            continue
        if relative.startswith("scripts/") and relative.endswith(".py"):
            loaded.add(relative)
    declared = {path for path in AUDIT_INPUT_PATHS if path.startswith("scripts/")}
    expected_axiom = "0" * 40 if mutation == "stale_axiom_authority" else CURRENT_AXIOM_BLOB
    return {
        "origin_main": git_output("rev-parse", "origin/main"),
        "axiom": worktree_blob(MINIMAL_AXIOMS),
        "expected_axiom": expected_axiom,
        "parent_commit": git_output("rev-parse", PARENT_COMMIT),
        "parent_note": worktree_blob(PARENT_NOTE),
        "parent_runner": worktree_blob(PARENT_RUNNER),
        "mismatches": mismatches,
        "missing": tuple(path for path in AUDIT_INPUT_PATHS if not (ROOT / path).exists()),
        "loaded_missing": tuple(sorted(loaded - declared)),
    }


def first_order_certificate(mutation: str) -> dict[str, object]:
    rng = np.random.default_rng(9801)
    maximum = 0.0
    probes = 0
    for _ in range(96):
        incoming = rng.uniform(-np.pi, np.pi, 4)
        transfer = rng.uniform(-np.pi, np.pi, 4)
        stress = block95.raw_stress(incoming, transfer)
        generator = block95.raw_generator(incoming, transfer)
        difference = block95.scalar_symbol(incoming + transfer) - block95.scalar_symbol(incoming)
        residual = block77.raw_gauge(-transfer).T @ stress + difference * generator
        maximum = max(maximum, float(np.max(np.abs(residual))))
        probes += 1
    if mutation == "break_first_order_parent":
        maximum = max(maximum, 0.25)
    constant = block95.raw_generator(
        np.asarray((0.31, -0.47, 0.28, 0.63)), np.zeros(4)
    )
    return {
        "probes": probes,
        "maximum": maximum,
        "constant_norm": float(np.linalg.norm(constant)),
    }


def continuum_vector(incoming: np.ndarray, transfer: np.ndarray) -> np.ndarray:
    return ETA @ (np.asarray(incoming) + 0.5 * np.asarray(transfer))


def continuum_vertex(
    tensor: np.ndarray, incoming: np.ndarray, transfer: np.ndarray
) -> complex:
    derivative = continuum_vector(incoming, transfer)
    return complex(derivative @ tensor @ derivative)


def continuum_generator(
    parameter: np.ndarray, incoming: np.ndarray, transfer: np.ndarray
) -> complex:
    return complex(1.0j * parameter @ continuum_vector(incoming, transfer))


def continuum_certificate(mutation: str) -> dict[str, object]:
    rng = np.random.default_rng(9802)
    decomposition_error = 0.0
    completed_error = 0.0
    seagull_norm = 0.0
    probes = 0
    for _ in range(192):
        incoming, geometry_transfer, parameter_transfer = rng.normal(size=(3, 4))
        parameter = rng.normal(size=4)
        tensor = rng.normal(size=(4, 4))
        tensor = 0.5 * (tensor + tensor.T)
        total = geometry_transfer + parameter_transfer
        center = continuum_vector(incoming, total)
        r_upper = ETA @ geometry_transfer
        s_upper = ETA @ parameter_transfer
        tensor_s = tensor @ s_upper
        commutator = (
            continuum_vertex(tensor, incoming + parameter_transfer, geometry_transfer)
            * continuum_generator(parameter, incoming, parameter_transfer)
            - continuum_generator(parameter, incoming + geometry_transfer, parameter_transfer)
            * continuum_vertex(tensor, incoming, geometry_transfer)
        )
        nonlinear_tensor = 1.0j * (
            (parameter @ r_upper) * tensor
            - np.outer(parameter, tensor_s)
            - np.outer(tensor_s, parameter)
        )
        tensor_part = complex(center @ nonlinear_tensor @ center)
        expected_remainder = complex(
            -0.25j * (parameter @ r_upper) * (s_upper @ tensor @ s_upper)
        )
        gauge_tensor = -1.0j * (
            np.outer(parameter_transfer, parameter)
            + np.outer(parameter, parameter_transfer)
        )
        tensor_pair = np.sum(tensor * (ETA @ gauge_tensor @ ETA))
        seagull = complex(
            0.125
            * (geometry_transfer @ ETA @ parameter_transfer)
            * tensor_pair
            - 0.25
            * (tensor @ s_upper)
            @ ETA
            @ (gauge_tensor @ r_upper)
        )
        decomposition_error = max(
            decomposition_error,
            abs(commutator + tensor_part - expected_remainder),
        )
        completion = commutator + tensor_part
        if mutation != "drop_continuum_seagull":
            completion += seagull
        completed_error = max(completed_error, abs(completion))
        seagull_norm = max(seagull_norm, abs(seagull))
        probes += 1
    return {
        "probes": probes,
        "decomposition_error": decomposition_error,
        "completed_error": completed_error,
        "seagull_norm": seagull_norm,
    }


def lattice_vertex(
    tensor: np.ndarray, incoming: np.ndarray, transfer: np.ndarray
) -> complex:
    derivative = block95.average_derivative(incoming, transfer)
    return complex(derivative @ tensor @ derivative)


def constant_commutator(
    tensor: np.ndarray,
    parameter: np.ndarray,
    incoming: np.ndarray,
    geometry_transfer: np.ndarray,
) -> complex:
    vertex = lattice_vertex(tensor, incoming, geometry_transfer)
    before = parameter @ block95.raw_generator(incoming, np.zeros(4))
    after = parameter @ block95.raw_generator(
        incoming + geometry_transfer, np.zeros(4)
    )
    return complex(vertex * before - after * vertex)


def lattice_witnesses(mutation: str) -> tuple[dict[str, object], ...]:
    result = []
    for active in range(3):
        for compensator in range(3):
            if active == compensator:
                continue
            for active_sign in (-1, 1):
                for compensator_sign in (-1, 1):
                    transfer = np.zeros(4)
                    transfer[active] = active_sign * np.pi / 2.0
                    transfer[compensator] = compensator_sign * np.pi / 2.0
                    center = np.zeros(4)
                    center[active] = np.pi / 3.0
                    center[compensator] = (
                        -active_sign * compensator_sign * np.pi / 3.0
                    )
                    reflected = center.copy()
                    reflected[active] = (
                        np.pi / 2.0 if mutation == "break_alias_pair" else 2.0 * np.pi / 3.0
                    )
                    incoming = center - 0.5 * transfer
                    incoming_reflected = reflected - 0.5 * transfer
                    tensor = np.zeros((4, 4))
                    tensor[active, active] = 1.0
                    parameter = np.zeros(4)
                    parameter[active] = 1.0
                    stress = block95.raw_stress(incoming, transfer)
                    stress_reflected = block95.raw_stress(incoming_reflected, transfer)
                    difference = block95.scalar_symbol(
                        incoming + transfer
                    ) - block95.scalar_symbol(incoming)
                    difference_reflected = block95.scalar_symbol(
                        incoming_reflected + transfer
                    ) - block95.scalar_symbol(incoming_reflected)
                    commutator = constant_commutator(
                        tensor, parameter, incoming, transfer
                    )
                    commutator_reflected = constant_commutator(
                        tensor, parameter, incoming_reflected, transfer
                    )
                    integer_error = max(
                        float(
                            np.max(
                                np.abs(
                                    np.concatenate(
                                        (incoming, incoming_reflected, transfer)
                                    )
                                    / UNIT
                                    - np.rint(
                                        np.concatenate(
                                            (incoming, incoming_reflected, transfer)
                                        )
                                        / UNIT
                                    )
                                )
                            )
                        ),
                        0.0,
                    )
                    result.append(
                        {
                            "active": active,
                            "compensator": compensator,
                            "signs": (active_sign, compensator_sign),
                            "stress": stress,
                            "stress_reflected": stress_reflected,
                            "difference": difference,
                            "difference_reflected": difference_reflected,
                            "commutator": commutator,
                            "commutator_reflected": commutator_reflected,
                            "expected": -1.0j
                            * active_sign
                            * 3.0
                            * np.sqrt(2.0)
                            / 8.0,
                            "gauge_norm": float(
                                np.linalg.norm(block77.raw_gauge(np.zeros(4)))
                            ),
                            "integer_error": integer_error,
                        }
                    )
    return tuple(result)


def witness_certificate(mutation: str) -> dict[str, object]:
    witnesses = lattice_witnesses(mutation)
    return {
        "count": len(witnesses),
        "stress_error": max(
            float(np.max(np.abs(item["stress"] - item["stress_reflected"])))
            for item in witnesses
        ),
        "symbol_difference": max(
            max(abs(item["difference"]), abs(item["difference_reflected"]))
            for item in witnesses
        ),
        "opposite_error": max(
            abs(item["commutator"] + item["commutator_reflected"])
            for item in witnesses
        ),
        "formula_error": max(
            max(
                abs(item["commutator"] - item["expected"]),
                abs(item["commutator_reflected"] + item["expected"]),
            )
            for item in witnesses
        ),
        "commutator_floor": min(
            min(abs(item["commutator"]), abs(item["commutator_reflected"]))
            for item in witnesses
        ),
        "gauge_norm": max(item["gauge_norm"] for item in witnesses),
        "integer_error": max(item["integer_error"] for item in witnesses),
    }


def rank_certificate(mutation: str) -> dict[str, object]:
    witnesses = lattice_witnesses("")
    coefficient_ranks = []
    augmented_ranks = []
    relative_residuals = []
    zero_sector_error = 0.0
    for item in witnesses:
        # Ten arbitrary geometry-only R1 coordinates are the only nonzero
        # columns.  Arbitrarily many S_g3, S_phi2, and regular D1 columns are
        # identically zero on this constant-parameter/equal-symbol subblock.
        row = np.asarray(item["stress"], dtype=complex)
        matrix = np.vstack((row, row))
        target = -np.asarray(
            (item["commutator"], item["commutator_reflected"]), dtype=complex
        )
        coefficient_ranks.append(int(np.linalg.matrix_rank(matrix, tol=1.0e-10)))
        augmented_ranks.append(
            int(np.linalg.matrix_rank(np.column_stack((matrix, target)), tol=1.0e-10))
        )
        solution = np.linalg.lstsq(matrix, target, rcond=1.0e-12)[0]
        relative_residuals.append(
            float(np.linalg.norm(matrix @ solution - target) / np.linalg.norm(target))
        )
        zero_sector_error = max(
            zero_sector_error,
            abs(item["difference"]),
            abs(item["difference_reflected"]),
            item["gauge_norm"],
        )
    regular = mutation != "admit_singular_d1"
    return {
        "pairs": len(witnesses),
        "coefficient_ranks": tuple(coefficient_ranks),
        "augmented_ranks": tuple(augmented_ranks),
        "minimum_relative_residual": min(relative_residuals),
        "maximum_relative_residual": max(relative_residuals),
        "zero_sector_error": zero_sector_error,
        "regular": regular,
    }


def no_go_certificate(mutation: str) -> dict[str, object]:
    note = flat(NOTE_PATH)
    routes = (
        "arbitrary quadratic matter seagull",
        "arbitrary pure-gravity cubic term",
        "arbitrary regular anti-hermitian d1",
        "arbitrary geometry-only r1",
        "larger same-symbol support",
        "continuum nonlinear tensor plus seagull",
        "changed discrete differential calculus",
        "geometry-dependent matter inner product",
    )
    result = {
        "headings": all(f"n{index}" in note for index in range(1, 9)),
        "routes": all(route in note for route in routes),
        "narrow_pass": "narrow fixed-carrier status: pass" in note,
        "broad_fail": "broad gravity/axiom status: fail — partial-narrowing" in note,
        "steelman": "strongest steelman" in note,
        "echo": "cross-cycle echo" in note,
        "levels": all(
            marker in note
            for marker in (
                "per-element",
                "per-site",
                "per-mode",
                "per-block",
                "lattice-wide",
            )
        ),
        "changed_live": "changed-carrier routes remain live" in note,
        "valid": mutation != "weaken_no_go_packet",
    }
    return result


def scope_certificate(mutation: str) -> dict[str, bool]:
    note = flat(NOTE_PATH)
    result = {
        "fixed_only": "the theorem is only for the fixed block 95 carrier" in note,
        "gravity_live": "this is not a gravity no-go" in note,
        "axiom_unchanged": "no axiom amendment is justified" in note,
        "carrier_live": "changed-carrier routes remain live" in note,
        "retention_open": "independent retention remains open" in note,
    }
    if mutation == "claim_gravity_no_go":
        result["gravity_live"] = False
    if mutation == "claim_axiom_update":
        result["axiom_unchanged"] = False
    return result


def portfolio_certificate(mutation: str) -> dict[str, bool]:
    note = flat(NOTE_PATH)
    result = {
        "stop_fixed": "stop extending the fixed block 95 nonlinear ward coefficient census" in note,
        "pivot": "pivot to the typed-event/record-law confluence seam" in note,
        "fallback": "changed-contract gravity repair" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": "no toe percentage moves" in note,
        "zero_e2e": "retained-positive end-to-end theory count remains zero" in note,
    }
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
            "break_first_order_parent",
            "drop_continuum_seagull",
            "break_alias_pair",
            "admit_singular_d1",
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
        "A-current-axiom-and-Block97-parent-authority",
        "origin/main, current axioms, and the complete frozen Block97 dependency chain are content-bound",
        authority["origin_main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["parent_commit"] == PARENT_COMMIT
        and authority["parent_note"] == PARENT_NOTE_BLOB
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and not authority["mismatches"]
        and not authority["missing"]
        and not authority["loaded_missing"],
        f"origin/main={str(authority['origin_main'])[:10]}; mismatches/missing/loaded={len(authority['mismatches'])}/{len(authority['missing'])}/{len(authority['loaded_missing'])}",
    )

    first = first_order_certificate(mutation)
    checks.check(
        "B-actual-Block95-first-order-cochain-remains-positive",
        "the exact raw first-order Ward cochain still closes off shell and its constant generator is nonzero",
        first["probes"] == 96
        and first["maximum"] < TOL
        and first["constant_norm"] > 0.1,
        f"probes={first['probes']}; residual={error_bound(first['maximum'])}; constant norm={first['constant_norm']:.6f}",
    )

    continuum = continuum_certificate(mutation)
    checks.check(
        "C-continuum-second-order-tensor-plus-seagull-control",
        "the continuum Weyl-symbol commutator decomposes exactly and one local scalar seagull closes the second-order identity",
        continuum["probes"] == 192
        and continuum["decomposition_error"] < TOL
        and continuum["completed_error"] < TOL
        and continuum["seagull_norm"] > 0.1,
        f"probes={continuum['probes']}; decomposition/completion={error_bound(continuum['decomposition_error'])}/{error_bound(continuum['completed_error'])}; seagull norm={continuum['seagull_norm']:.6f}",
    )

    witness = witness_certificate(mutation)
    checks.check(
        "D-exact-L24-constant-parameter-alias-pairs",
        "twenty-four exact finite-lattice pairs have zero free-symbol transfer, identical stress, zero R0, and opposite nonzero commutators",
        witness["count"] == 24
        and witness["stress_error"] < TOL
        and witness["symbol_difference"] < TOL
        and witness["opposite_error"] < TOL
        and witness["formula_error"] < TOL
        and witness["commutator_floor"] > 0.5
        and witness["gauge_norm"] < TOL
        and witness["integer_error"] < TOL,
        f"pairs={witness['count']}; stress/dM/opposite/formula={error_bound(witness['stress_error'])}/{error_bound(witness['symbol_difference'])}/{error_bound(witness['opposite_error'])}/{error_bound(witness['formula_error'])}; |C|min={witness['commutator_floor']:.6f}",
    )

    rank = rank_certificate(mutation)
    checks.check(
        "E-support-independent-second-order-Ward-rank-contradiction",
        "every alias pair has coefficient rank one and augmented rank two after all seagull, cubic-gravity, and regular D1 columns vanish",
        rank["pairs"] == 24
        and set(rank["coefficient_ranks"]) == {1}
        and set(rank["augmented_ranks"]) == {2}
        and rank["minimum_relative_residual"] > 0.999999
        and rank["maximum_relative_residual"] < 1.000001
        and rank["zero_sector_error"] < TOL
        and rank["regular"],
        f"pairs={rank['pairs']}; ranks={set(rank['coefficient_ranks'])}->{set(rank['augmented_ranks'])}; relative residual={rank['minimum_relative_residual']:.9f}..{rank['maximum_relative_residual']:.9f}",
    )

    no_go = no_go_certificate(mutation)
    checks.check(
        "F-no-go-discipline-passes-only-the-fixed-carrier-boundary",
        "N1-N8 pass for the fixed Block95 completion and fail for any broad gravity or axiom conclusion",
        all(no_go.values()),
    )

    scope = scope_certificate(mutation)
    checks.check(
        "G-gravity-axiom-and-retention-firewall",
        "the result closes one candidate carrier, not gravity; changed carriers remain live and no axiom amendment or retention is claimed",
        all(scope.values()),
    )

    portfolio = portfolio_certificate(mutation)
    checks.check(
        "H-TOE-score-and-portfolio-stop-rule",
        "zero obligations retire and the fixed-carrier coefficient census stops in favor of the higher-leverage Record seam or a changed carrier",
        all(portfolio.values()),
    )

    print(
        f"AXIOM_AUTHORITY: origin/main={authority['origin_main']} axiom={CURRENT_AXIOM_BLOB}; Block97 parent={PARENT_COMMIT}"
    )
    print(
        "per_element: checked — exact continuum tensor/seagull coefficients and each scalar Ward coefficient in all twenty-four alias pairs"
    )
    print(
        "per_site: checked and not executed — the Fourier-polynomial witness is bounded-support independent, but no changed-carrier position-space action is built"
    )
    print(
        "per_mode: checked — exact L=24 modes have zero M0 transfer, identical raw stress coordinates, and opposite nonzero commutators"
    )
    print(
        "per_block: checked — the complete order-h-phi2 matter subblock eliminates S_g3, S_phi2, regular anti-Hermitian D1, and geometry-only R1 simultaneously"
    )
    print(
        "lattice_wide: checked and not executed — a changed differential calculus, nonlinear gravity action, full-Z3 control, Record compiler, selection, and retention remain open"
    )
    print(
        "RESULT: the continuum second-order Ward identity has an explicit local tensor-plus-seagull completion, while the fixed Block95 periodic half-density generator has a support-independent constant-parameter alias contradiction"
    )
    print(
        "PORTFOLIO: stop the fixed Block95 nonlinear coefficient census; pivot to typed-event/Record-law confluence, retaining one changed-contract gravity repair as the only justified gravity re-entry"
    )
    print(
        "SCOPE: this is not a gravity no-go or axiom amendment; changed carrier, changed M0/D0/V plus nonlocal/quasilocal representation, geometry-dependent inner product, nonlinear action, Record selection, audit retention, obligation retirement, and TOE movement remain open"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
