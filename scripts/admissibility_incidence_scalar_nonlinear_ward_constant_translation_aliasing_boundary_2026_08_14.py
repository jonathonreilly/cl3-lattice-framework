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


# Current 2026-09-08 input closure. Historical raw identities below are provenance.
from hashlib import sha256 as _input_sha256

AUDIT_INPUT_PATHS = (
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_BOUNDARY_DRESSED_JOINT_STAGE_HOMOGENEOUS_NONLINEAR_ZERO_MODE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_CANONICAL_TWO_TT_POSITIVE_TRANSFER_RECORD_SOURCE_CONTINUITY_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_COMPONENT_STAGGERED_SIGNED_LINK_ACTION_LOCAL_WARD_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_COUNTERPROPAGATING_SCALAR_BIANCHI_TRACE_SHEAR_ENERGY_CURRENT_EXCHANGE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_CYCLE713_SIGNED_RECORD_SOURCE_CAUSAL_TT_VERTICAL_SLICE_BOUNDED_THEOREM_NOTE_2026-08-13.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_DIRAC_SIGNATURE_GRAVITY_REPLACEMENT_SHORTEST_ROUTE_GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_INCIDENCE_ADM_DEPTH_TWO_SOURCED_CONSTRAINT_RECORD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_JOINT_RECORD_GRAVITY_LAW_FIVE_CONTROL_AXIOM_CUT_GATE_BOUNDED_THEOREM_NOTE_2026-08-11.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_RECORD_WORLDLINE_CONSERVED_STRESS_TWO_TT_LORENTZIAN_CFL_LOCALITY_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md',
    'docs/ADMISSIBILITY_CYCLE713_RECORD_HEAD_ADM_WORK_ARCHIVE_STATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    'docs/ADMISSIBILITY_INCIDENCE_FIERZ_PAULI_SIGNED_RECORD_SOURCE_FULL_TENSOR_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    'docs/ADMISSIBILITY_INCIDENCE_SCALAR_GRAPH_MATTER_FIRST_ORDER_TOTAL_WARD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    'docs/ADMISSIBILITY_INCIDENCE_SCALAR_NONLINEAR_WARD_CONSTANT_TRANSLATION_ALIASING_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    'docs/ADMISSIBILITY_RAW_GRAPH_WARD_COMPACT_PULLBACK_TRANSLATION_GENERATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    'docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md',
    'docs/MINIMAL_AXIOMS_2026-06-29.md',
    'docs/audit/data/axiom_premise_nodes.json',
    'scripts/admissibility_boundary_dressed_joint_stage_homogeneous_zero_mode_2026_08_14.py',
    'scripts/admissibility_component_staggered_signed_link_action_local_ward_boundary_2026_08_14.py',
    'scripts/admissibility_counterpropagating_scalar_bianchi_energy_current_exchange_2026_08_14.py',
    'scripts/admissibility_cycle713_record_head_adm_work_archive_state_boundary_2026_08_14.py',
    'scripts/admissibility_cycle713_signed_record_source_causal_tt_vertical_slice_2026_08_13.py',
    'scripts/admissibility_incidence_adm_depth_two_sourced_constraint_record_cadence_boundary_2026_08_14.py',
    'scripts/admissibility_incidence_fierz_pauli_signed_record_source_full_tensor_cadence_boundary_2026_08_14.py',
    'scripts/admissibility_incidence_scalar_graph_matter_first_order_total_ward_cadence_boundary_2026_08_14.py',
    'scripts/admissibility_raw_graph_ward_compact_pullback_translation_generator_boundary_2026_08_14.py',
    'scripts/admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_2026_08_11.py',
)
# Filled only after all source/prose/input paths are frozen, bottom-up.
CURRENT_INPUT_SHA256 = {
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_BOUNDARY_DRESSED_JOINT_STAGE_HOMOGENEOUS_NONLINEAR_ZERO_MODE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md': '63609187f4c98f3bf6c16d1b1e03b0243d42432211bcf20885529196ae16f08a',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_CANONICAL_TWO_TT_POSITIVE_TRANSFER_RECORD_SOURCE_CONTINUITY_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md': 'e64e84edb6f3571281525ead288e8cabf0581bea01dfc3c003b6dc4c3439db0d',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_COMPONENT_STAGGERED_SIGNED_LINK_ACTION_LOCAL_WARD_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md': '8314592746d61f780f49b952bcc8f9e6cdc528079a34189813f1cd5fcca77b32',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_COUNTERPROPAGATING_SCALAR_BIANCHI_TRACE_SHEAR_ENERGY_CURRENT_EXCHANGE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md': '3abb9528b3ecdb88173b2d64dcd385a4e57c758607cfba1d82943590d03875f8',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_CYCLE713_SIGNED_RECORD_SOURCE_CAUSAL_TT_VERTICAL_SLICE_BOUNDED_THEOREM_NOTE_2026-08-13.md': '3179f81553c6d5f16dca06f83984195ef137cba46417dda5981de0e70a8afd5e',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_DIRAC_SIGNATURE_GRAVITY_REPLACEMENT_SHORTEST_ROUTE_GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md': '6b1f5f14cb9245c806c071c8cbbebbcf3250c422b54dc64e1000e9812f9e5922',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_INCIDENCE_ADM_DEPTH_TWO_SOURCED_CONSTRAINT_RECORD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md': 'b2cb7b87be7ecc8d97e08db3849701d9bde787159716ecd58b1417fc26b2ecca',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_JOINT_RECORD_GRAVITY_LAW_FIVE_CONTROL_AXIOM_CUT_GATE_BOUNDED_THEOREM_NOTE_2026-08-11.md': '63241ec60d7dddc2226378f8708551736de5db5311a94706bfe35a4d341f2be0',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_RECORD_WORLDLINE_CONSERVED_STRESS_TWO_TT_LORENTZIAN_CFL_LOCALITY_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md': 'a773ef431321a8477d332f1f04295ddf18b960cc27c0637153561496cb87fa17',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md': 'd42e416d15e227c61597bac6db96536105017084494d6714c95e50fe78bedaed',
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md': 'b52d939a514eaee6a314936dea50b9ef2a7ba7139351a68eb3d53e8a44c6b9a8',
    'docs/ADMISSIBILITY_CYCLE713_RECORD_HEAD_ADM_WORK_ARCHIVE_STATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md': 'f25b46abf9cdab4cd3bc442b4ca87ae0581aea2f7205d9cd733d48956e5fd05e',
    'docs/ADMISSIBILITY_INCIDENCE_FIERZ_PAULI_SIGNED_RECORD_SOURCE_FULL_TENSOR_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md': '903e13d1729970408477e595c500ab80a026374d2f5f81eefd3f1826656a3ff2',
    'docs/ADMISSIBILITY_INCIDENCE_SCALAR_GRAPH_MATTER_FIRST_ORDER_TOTAL_WARD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md': 'acc4ba247843315c1f841f660d59e375553b94de243a83f1a4195169038434d5',
    'docs/ADMISSIBILITY_INCIDENCE_SCALAR_NONLINEAR_WARD_CONSTANT_TRANSLATION_ALIASING_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md': '8a82e1450d037c8946d7706a740f5812fc9e96d5b7a16fac1f981d04778bb1fa',
    'docs/ADMISSIBILITY_RAW_GRAPH_WARD_COMPACT_PULLBACK_TRANSLATION_GENERATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md': 'aa1cb03d2b2907055124bbb2c8baac74a20b25a730a1c16443e7df13e699167e',
    'docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md': '5516fb0bb8f50286b3c34d3f2668b1a2e347b9f7e257a8b5745f84f1093dd96b',
    'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
    'docs/audit/data/axiom_premise_nodes.json': '615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37',
    'scripts/admissibility_boundary_dressed_joint_stage_homogeneous_zero_mode_2026_08_14.py': 'ce11aedb660bb8239fe14d8c983f81f1414d678c11896b68522bd40fb4b50fc3',
    'scripts/admissibility_component_staggered_signed_link_action_local_ward_boundary_2026_08_14.py': '09a395a3761544b5a55d0948e70b517aa406cc8e32bba0724cb25ed59e716435',
    'scripts/admissibility_counterpropagating_scalar_bianchi_energy_current_exchange_2026_08_14.py': '48445a633c2bcce6412d15b643a3046869df2a16b365d025326dc8b582a58e53',
    'scripts/admissibility_cycle713_record_head_adm_work_archive_state_boundary_2026_08_14.py': '492421b1dcbb45353d3aa074992a42ab73b48189bbba2a4b5507668029768c74',
    'scripts/admissibility_cycle713_signed_record_source_causal_tt_vertical_slice_2026_08_13.py': 'aee3ba64460976475f36bfc8b45fcc4319c285d3f9d8ebb5ee7a5b677181f801',
    'scripts/admissibility_incidence_adm_depth_two_sourced_constraint_record_cadence_boundary_2026_08_14.py': '04218b21e9fd7d9085fa8125d5e48786bcc07d02c644ec935c7d67711d02e052',
    'scripts/admissibility_incidence_fierz_pauli_signed_record_source_full_tensor_cadence_boundary_2026_08_14.py': 'a333908578772ce37b47b3b6808391a20dbafe10e18a815619f03084263941de',
    'scripts/admissibility_incidence_scalar_graph_matter_first_order_total_ward_cadence_boundary_2026_08_14.py': 'ced1d42af20625a1a80892e7b27aaa1b64f4560f78f541b5df2cc34cefe0f865',
    'scripts/admissibility_raw_graph_ward_compact_pullback_translation_generator_boundary_2026_08_14.py': 'c87b603b2d34e49fe00aaa066e8ea69647bca4247e6238e9ea6daafe73d012c7',
    'scripts/admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_2026_08_11.py': '58adf86925073ea65bab1f348819a5fa10bcf86e911b2742bab44e11dd132b15',
}

def current_input_failures(check_loaded: bool = False) -> tuple[str, ...]:
    failures = []
    if set(CURRENT_INPUT_SHA256) != set(AUDIT_INPUT_PATHS):
        failures.append("declared-input/hash-map mismatch")
    for relative in AUDIT_INPUT_PATHS:
        try:
            observed = _input_sha256((ROOT / relative).read_bytes()).hexdigest()
        except OSError:
            failures.append(relative + ": missing or unreadable")
            continue
        if observed != CURRENT_INPUT_SHA256.get(relative):
            failures.append(relative + ": content mismatch")
    if check_loaded:
        # This check runs only on direct main entry, not during parent imports.
        # Keep actual loaded-source coverage separate from historical Git status.
        import sys as _source_sys
        allowed = set(AUDIT_INPUT_PATHS)
        allowed.add(Path(__file__).resolve().relative_to(ROOT).as_posix())
        for module in tuple(_source_sys.modules.values()):
            file_name = getattr(module, "__file__", None)
            if not file_name:
                continue
            try:
                relative = Path(file_name).resolve().relative_to(ROOT).as_posix()
            except (OSError, ValueError):
                continue
            if relative.startswith("scripts/") and relative.endswith(".py") and relative not in allowed:
                failures.append(relative + ": loaded repository source is undeclared")
    return tuple(failures)

# Fail before local imports or scientific computation on input drift/removal.
_INPUT_FAILURES = current_input_failures()
if _INPUT_FAILURES:
    raise RuntimeError("current input binding failed: " + "; ".join(_INPUT_FAILURES))
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_INCIDENCE_SCALAR_NONLINEAR_WARD_CONSTANT_TRANSLATION_"
    "ALIASING_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
RUNNER_RELATIVE = (
    "scripts/admissibility_incidence_scalar_nonlinear_ward_constant_"
    "translation_aliasing_boundary_2026_08_14.py"
)
PARENT_NOTE = (
    '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_COUNTERPROPAGATING_SCALAR_BIANCHI_TRACE_SHEAR_ENERGY_CURRENT_EXCHANGE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md'
)
PARENT_RUNNER = (
    "scripts/admissibility_counterpropagating_scalar_bianchi_energy_current_"
    "exchange_2026_08_14.py"
)
MINIMAL_AXIOMS = "docs/MINIMAL_AXIOMS_2026-06-29.md"


HISTORICAL_MAIN = "eee6ab5874e2fc207db5526dc82d9f71ae550c7c"
HISTORICAL_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
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
    return {"failures": current_input_failures(),
            "mutation_ok": mutation not in ("stale_axiom_authority", "stale_os_authority")}


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
        "narrow_pass": "fixed-carrier mathematical obstruction is established at its stated scope" in note,
        "broad_fail": "broad gravity/axiom claims remain unestablished — partial-narrowing" in note,
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
    loaded_input_failures = current_input_failures(check_loaded=True)
    if loaded_input_failures:
        raise RuntimeError("loaded source/input binding failed: " + "; ".join(loaded_input_failures))
    checks.check(
        "A-current-axiom-and-Block97-parent-authority",
        'current memo and final source/input bytes are pinned; original parent identities remain historical',
        not current_input_failures() and mutation not in ("stale_axiom_authority", "stale_os_authority"),
        'Current input closure checked independently of moving branch heads or historical audit status',
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
        "the finite fixed-carrier obstruction retains its stated scope; broad gravity/axiom conclusions and full N1/N2 coverage remain unestablished",
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

    print("SOURCE_AUTHORITY: current memo and exact declared file bytes; historical Git identities are provenance only")
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
