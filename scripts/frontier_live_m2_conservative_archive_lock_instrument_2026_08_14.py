#!/usr/bin/env python3
"""Block 86: conservative live-M2 archive-lock instrument.

Compose the Block73 six-outcome live-M2 Kraus family with the Block72
nearest-neighbour coherent event core and the Block71 same-carrier three-Record lock.
The resulting object is one total finite hybrid quantum/Record instrument:
refusal and no-event preserve the Record map, while each event outcome archives
all arbitrary target information and atomically locks three already-present
M2 projectors.  The construction is a candidate downstream law, not an axiom,
an approved primitive, a physical clock, or a full-Z3 process.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import product
import math
from pathlib import Path
import subprocess

import numpy as np

import frontier_record_visible_integrated_formation_instrument_2026_08_14 as block73


block72 = block73.block72
block71 = block73.block71

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "LIVE_M2_CONSERVATIVE_ARCHIVE_LOCK_INSTRUMENT_BOUNDED_THEOREM_NOTE_"
    "2026-08-14.md"
)
AXIOM_REPO_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AXIOM_PATH = ROOT / AXIOM_REPO_PATH
PARENT71_RUNNER = ROOT / "scripts" / "frontier_same_carrier_three_record_archive_packet_2026_08_13.py"
PARENT72_RUNNER = ROOT / "scripts" / "frontier_nn_formation_selector_two_model_kill_2026_08_14.py"
PARENT73_RUNNER = ROOT / "scripts" / "frontier_record_visible_integrated_formation_instrument_2026_08_14.py"
PARENT71_NOTE = ROOT / "docs" / "SAME_CARRIER_THREE_RECORD_ARCHIVE_PACKET_BOUNDED_THEOREM_NOTE_2026-08-13.md"
PARENT72_NOTE = ROOT / "docs" / "NN_FORMATION_SELECTOR_TWO_MODEL_KILL_BOUNDED_NOTE_2026-08-14.md"
PARENT73_NOTE = ROOT / "docs" / "RECORD_VISIBLE_INTEGRATED_FORMATION_INSTRUMENT_BOUNDED_NOTE_2026-08-14.md"

PARENT_RECEIPTS = (
    "c0c54fdaafb051cd33d25f5be93b7b326f65f586",
    "b12ed53fd063a4d4464ab8311a41cb670c656adf",
    "6c318b98e3520fc46ebb741cae44a4369dcd798d",
)
HISTORICAL_PARENT_SHA256 = ('2b4e986a8396d6c0713a0297eb3a02350c713ba71414d9fa4ef2c221b6eef41f', 'ef2ebb8325fc9bd58475c7ac9a8040038079f42d49278099667cfd0edbbf3c94', '4a8dbbd8414c28a4969b896653cf4e199a6d097b25527e5dd5f144e723a58bc6', '0e92010db40cd800ef00768d4f157f8ebccc6c4633ad0c5825a99f2888df480d', '76db641f6a0743dc78d7301bbdc57ed29991aeda9efa3d1a9a831ef672ece901', 'af3c5257e08e002a35d3351fa09122bb914ae94ecb3d741d216067b59125ba58')
PARENT_SHA256 = ('7d64706ad0a76724b6ae14fc1c0751d9f3518105ebea775d1399fcf129aba74c', 'cff4964b3dc6acebb8ad4d0c501371197898b207f8cc77468e7c76749a6d9664', '9586e59e5d30d7020dc3d5b03a461fe85a3e659790eacfb0fa1e489dc504cde1', '370637c3881b72b68e5df8fb8d8afaa55fcd995025c01173771ffce418918847', 'ad99e42a21df2ea4c656cb6be8fc957e68377623c37075556c20b1ecd423f5c6', '29b0177eaca7e86542c1a15d9a64751895ea5798d695f6305f23891ec974ff58')
HISTORICAL_PARENT_FILES = (('c0c54fdaafb051cd33d25f5be93b7b326f65f586', 'scripts/frontier_same_carrier_three_record_archive_packet_2026_08_13.py'), ('b12ed53fd063a4d4464ab8311a41cb670c656adf', 'scripts/frontier_nn_formation_selector_two_model_kill_2026_08_14.py'), ('6c318b98e3520fc46ebb741cae44a4369dcd798d', 'scripts/frontier_record_visible_integrated_formation_instrument_2026_08_14.py'), ('c0c54fdaafb051cd33d25f5be93b7b326f65f586', 'docs/SAME_CARRIER_THREE_RECORD_ARCHIVE_PACKET_BOUNDED_THEOREM_NOTE_2026-08-13.md'), ('b12ed53fd063a4d4464ab8311a41cb670c656adf', 'docs/NN_FORMATION_SELECTOR_TWO_MODEL_KILL_BOUNDED_NOTE_2026-08-14.md'), ('6c318b98e3520fc46ebb741cae44a4369dcd798d', 'docs/RECORD_VISIBLE_INTEGRATED_FORMATION_INSTRUMENT_BOUNDED_NOTE_2026-08-14.md'))
AUDIT_INPUT_PATHS = (
    "docs/LIVE_M2_CONSERVATIVE_ARCHIVE_LOCK_INSTRUMENT_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/SAME_CARRIER_THREE_RECORD_ARCHIVE_PACKET_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/NN_FORMATION_SELECTOR_TWO_MODEL_KILL_BOUNDED_NOTE_2026-08-14.md",
    "docs/RECORD_VISIBLE_INTEGRATED_FORMATION_INSTRUMENT_BOUNDED_NOTE_2026-08-14.md",
    "scripts/frontier_same_carrier_three_record_archive_packet_2026_08_13.py",
    "scripts/frontier_nn_formation_selector_two_model_kill_2026_08_14.py",
    "scripts/frontier_record_visible_integrated_formation_instrument_2026_08_14.py",
)

# Current selected files; original receipt constants below remain historical.
CURRENT_INPUT_SHA256 = {
    "docs/LIVE_M2_CONSERVATIVE_ARCHIVE_LOCK_INSTRUMENT_BOUNDED_THEOREM_NOTE_2026-08-14.md": "6e22bb1618341229793e9301e1ab7804b34203b55bbcae050c9fb8082cdeff2a",
    "docs/MINIMAL_AXIOMS_2026-06-29.md": "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753",
    "docs/SAME_CARRIER_THREE_RECORD_ARCHIVE_PACKET_BOUNDED_THEOREM_NOTE_2026-08-13.md": "370637c3881b72b68e5df8fb8d8afaa55fcd995025c01173771ffce418918847",
    "docs/NN_FORMATION_SELECTOR_TWO_MODEL_KILL_BOUNDED_NOTE_2026-08-14.md": "ad99e42a21df2ea4c656cb6be8fc957e68377623c37075556c20b1ecd423f5c6",
    "docs/RECORD_VISIBLE_INTEGRATED_FORMATION_INSTRUMENT_BOUNDED_NOTE_2026-08-14.md": "29b0177eaca7e86542c1a15d9a64751895ea5798d695f6305f23891ec974ff58",
    "scripts/frontier_same_carrier_three_record_archive_packet_2026_08_13.py": "7d64706ad0a76724b6ae14fc1c0751d9f3518105ebea775d1399fcf129aba74c",
    "scripts/frontier_nn_formation_selector_two_model_kill_2026_08_14.py": "cff4964b3dc6acebb8ad4d0c501371197898b207f8cc77468e7c76749a6d9664",
    "scripts/frontier_record_visible_integrated_formation_instrument_2026_08_14.py": "9586e59e5d30d7020dc3d5b03a461fe85a3e659790eacfb0fa1e489dc504cde1"
}

TOL = 5.0e-11
AUDIT_TIMEOUT_SEC = 180
HAZARD = Fraction(1, 3)
ROLE_ORDER = block72.ROLE_ORDER
Branch = tuple[int, int]
Content = object
Coord = block71.Coord


@dataclass(frozen=True)
class HybridOutcome:
    key: object
    probability: float
    state: np.ndarray
    records: tuple[tuple[Coord, Content], ...]


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str) -> None:
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        print(f"{'PASS' if result else 'FAIL'} {label}: {detail}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def git_ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT,
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).returncode == 0


def current_axiom_text() -> tuple[str, str]:
    for ref in ("origin/main", "HEAD"):
        exists = subprocess.run(
            ("git", "cat-file", "-e", f"{ref}:{AXIOM_REPO_PATH}"),
            cwd=ROOT,
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        ).returncode == 0
        if exists:
            return ref, subprocess.check_output(
                ("git", "show", f"{ref}:{AXIOM_REPO_PATH}"),
                cwd=ROOT,
                text=True,
            )
    raise RuntimeError("cannot resolve current axiom authority")


def current_inputs_match() -> bool:
    return all((ROOT / path).is_file()
               and sha256((ROOT / path).read_bytes()).hexdigest() == digest
               for path, digest in CURRENT_INPUT_SHA256.items())


def authority_certificate(stale: bool = False) -> dict[str, object]:
    ref, axiom = current_axiom_text()
    local = AXIOM_PATH.read_text(encoding="utf-8")
    flat = " ".join(axiom.split())
    parent_paths = (
        PARENT71_RUNNER, PARENT72_RUNNER, PARENT73_RUNNER,
        PARENT71_NOTE, PARENT72_NOTE, PARENT73_NOTE,
    )
    return {
        "ref": ref,
        "main": subprocess.check_output(("git", "rev-parse", "origin/main"), cwd=ROOT, text=True).strip(),
        "axiom_sha256": sha256(axiom.encode()).hexdigest(),
        "local_matches": local == axiom,
        "parent_ancestors": tuple(git_ancestor(commit) for commit in PARENT_RECEIPTS),
        "parent_hashes": tuple(file_sha256(path) for path in parent_paths),
        "parent_hashes_match": tuple(file_sha256(path) for path in parent_paths) == PARENT_SHA256,
        "parent_paths_exist": all(path.is_file() for path in parent_paths),
        "current_contract": all(
            phrase in flat
            for phrase in (
                "The full one-site possibility domain has algebraic presentation `M_2(C)`.",
                "Records form.",
                "Only records are readable.",
                "A state is a configuration of records.",
                "Admissibility is not a dynamics axiom.",
                "the remaining formation rules",
            )
        ),
        "current_inputs_match": current_inputs_match(),
        "historical_parents_match": tuple(
            sha256(subprocess.check_output(("git", "show", f"{commit}:{path}"), cwd=ROOT)).hexdigest()
            for commit, path in HISTORICAL_PARENT_FILES
        ) == HISTORICAL_PARENT_SHA256,
        "forced_stale": stale,
    }


def extended_low(operator: np.ndarray, high_qubits: int = 3) -> np.ndarray:
    """Extend a five-wire operator by identity on higher little-endian wires."""
    return np.kron(np.eye(1 << high_qubits, dtype=complex), operator)


def swap_matrix(count: int, left: int, right: int) -> np.ndarray:
    dimension = 1 << count
    answer = np.zeros((dimension, dimension), dtype=complex)
    for source in range(dimension):
        target = source
        left_bit = (source >> left) & 1
        right_bit = (source >> right) & 1
        if left_bit != right_bit:
            target ^= (1 << left) | (1 << right)
        answer[target, source] = 1
    return answer


def archive_unitary() -> np.ndarray:
    """Mark P by H, then exchange P/M/B with head/root/meta targets."""
    marker = block71.embed_gate(block71.one("archive_head_H", 0, block71.H), 8)
    permutation = np.eye(256, dtype=complex)
    for left, right in ((0, 5), (1, 6), (2, 7)):
        permutation = swap_matrix(8, left, right) @ permutation
    return permutation @ marker


def ready_projector() -> np.ndarray:
    gamma = np.zeros((32, 32), dtype=complex)
    for m in (0, 1):
        index = block71.full_index(1, m, 0, 0, 0)
        gamma[index, index] = 1
    return gamma


def output_projectors() -> dict[Branch, np.ndarray]:
    answer: dict[Branch, np.ndarray] = {}
    for m, b in product((0, 1), repeat=2):
        projector = np.zeros((32, 32), dtype=complex)
        for r, a in product((0, 1), repeat=2):
            index = block71.full_index(1, m, b, r, a)
            projector[index, index] = 1
        answer[(m, b)] = projector
    return answer


def instrument_operators(break_completeness: bool = False) -> dict[object, np.ndarray]:
    identity5 = np.eye(32, dtype=complex)
    gamma = ready_projector()
    unitary = block71.word_matrix(block71.dilation_word(), 5)
    archive = archive_unitary()
    operators: dict[object, np.ndarray] = {
        "refusal": extended_low(identity5 - gamma),
        "no_event": math.sqrt(float(1 - HAZARD)) * extended_low(gamma),
    }
    for index, (key, projector) in enumerate(output_projectors().items()):
        scale = math.sqrt(float(HAZARD))
        if break_completeness and index == 0:
            scale *= math.sqrt(2)
        operators[key] = scale * archive @ extended_low(projector @ unitary @ gamma)
    return operators


def clean_input_vector(m: int, target: np.ndarray) -> np.ndarray:
    if target.shape != (8,):
        raise ValueError("target must be an eight-component vector")
    low = np.zeros(32, dtype=complex)
    low[block71.full_index(1, m, 0, 0, 0)] = 1
    return np.kron(target, low)


def coherent_input_vector(amplitudes: tuple[complex, complex], target: np.ndarray) -> np.ndarray:
    low = np.zeros(32, dtype=complex)
    for m, amplitude in enumerate(amplitudes):
        low[block71.full_index(1, m, 0, 0, 0)] = amplitude
    return np.kron(target, low)


def expected_archived_vector(m: int, b: int, target_index: int) -> np.ndarray:
    source = np.zeros(256, dtype=complex)
    ray = block71.expected_branch(m, b)
    for role_index, amplitude in enumerate(ray):
        if abs(amplitude) > 1.0e-15:
            source[role_index | (target_index << 5)] = amplitude
    return archive_unitary() @ source


def kraus_certificate(break_completeness: bool = False, host_select_m: bool = False) -> dict[str, object]:
    operators = instrument_operators(break_completeness)
    completeness = sum(
        (operator.conj().T @ operator for operator in operators.values()),
        np.zeros((256, 256), dtype=complex),
    )
    flattened = np.column_stack(tuple(operator.reshape(-1) for operator in operators.values()))
    hs_gram = flattened.conj().T @ flattened
    probability_failures = branch_vector_failures = 0
    basis_cases = 0
    for m, target_index in product((0, 1), range(8)):
        target = np.eye(8, dtype=complex)[:, target_index]
        state = clean_input_vector(m, target)
        probabilities = {
            key: float(np.linalg.norm(operator @ state) ** 2)
            for key, operator in operators.items()
        }
        probability_failures += abs(probabilities["refusal"]) >= TOL
        probability_failures += abs(probabilities["no_event"] - float(1 - HAZARD)) >= TOL
        for branch in product((0, 1), repeat=2):
            branch_m, b = branch
            expected_weight = (
                float(HAZARD * block72.BRANCH_WEIGHTS[m][b])
                if branch_m == m and (not host_select_m or m == 0)
                else 0.0
            )
            probability_failures += abs(probabilities[branch] - expected_weight) >= TOL
            if branch_m == m and probabilities[branch] > TOL:
                observed = operators[branch] @ state / math.sqrt(probabilities[branch])
                expected = expected_archived_vector(m, b, target_index)
                branch_vector_failures += float(np.linalg.norm(observed - expected)) >= TOL
            basis_cases += 1

    coherent_failures = coherent_cases = 0
    coherent_amplitudes = (
        (1 / math.sqrt(2), 1 / math.sqrt(2)),
        (1 / math.sqrt(2), 1j / math.sqrt(2)),
        (math.sqrt(3) / 2, 0.5),
    )
    target_vectors = (
        np.eye(8, dtype=complex)[:, 0],
        np.ones(8, dtype=complex) / math.sqrt(8),
        np.asarray((1, 1j, 0, 0, 0, 0, 0, 0), dtype=complex) / math.sqrt(2),
    )
    for amplitudes, target in product(coherent_amplitudes, target_vectors):
        state = coherent_input_vector(amplitudes, target)
        for m, b in product((0, 1), repeat=2):
            observed = float(np.linalg.norm(operators[(m, b)] @ state) ** 2)
            expected = float(HAZARD * block72.BRANCH_WEIGHTS[m][b]) * abs(amplitudes[m]) ** 2
            coherent_failures += abs(observed - expected) >= TOL
            coherent_cases += 1
        no_event = float(np.linalg.norm(operators["no_event"] @ state) ** 2)
        coherent_failures += abs(no_event - float(1 - HAZARD)) >= TOL
        coherent_cases += 1

    return {
        "outcomes": len(operators),
        "ready_rank": int(round(float(np.trace(ready_projector()).real))),
        "completeness_residual": float(np.linalg.norm(completeness - np.eye(256))),
        "kraus_rank": int(np.linalg.matrix_rank(hs_gram, tol=TOL)),
        "kraus_gram_minimum": float(np.linalg.eigvalsh(hs_gram).min()),
        "basis_cases": basis_cases,
        "probability_failures": probability_failures,
        "branch_vector_failures": branch_vector_failures,
        "coherent_cases": coherent_cases,
        "coherent_failures": coherent_failures,
        "host_selected_m": host_select_m,
        "operators": operators,
    }


def lock_projector(wire: int, matrix: np.ndarray) -> np.ndarray:
    return block71.embed_gate(block71.one(f"lock_{wire}", wire, matrix), 8)


def archive_reference_certificate(erase_targets: bool = False) -> dict[str, object]:
    operators = instrument_operators()
    branch_ranks: dict[Branch, int] = {}
    branch_gram_residuals: dict[Branch, float] = {}
    expected_residual = lock_residual = factor_failures = 0.0
    combined_columns: list[np.ndarray] = []
    for m, b in product((0, 1), repeat=2):
        weight = float(HAZARD * block72.BRANCH_WEIGHTS[m][b])
        columns: list[np.ndarray] = []
        for target_index in range(8):
            target = np.eye(8, dtype=complex)[:, target_index]
            source = clean_input_vector(m, target)
            if erase_targets:
                output = expected_archived_vector(m, b, 0)
            else:
                output = operators[(m, b)] @ source / math.sqrt(weight)
            expected = expected_archived_vector(m, b, target_index)
            expected_residual = max(expected_residual, float(np.linalg.norm(output - expected)))
            if not erase_targets:
                for wire, expected_matrix in (
                    (5, block71.PMINUS),
                    (6, block71.P1 if m else block71.P0),
                    (7, block71.P1 if b else block71.P0),
                ):
                    lock_residual = max(
                        lock_residual,
                        float(np.linalg.norm(block71.reduced_single(output, wire, 8) - expected_matrix)),
                    )
                joint = (
                    lock_projector(5, block71.PMINUS)
                    @ lock_projector(6, block71.P1 if m else block71.P0)
                    @ lock_projector(7, block71.P1 if b else block71.P0)
                )
                factor_failures += abs(float(np.vdot(output, joint @ output).real) - 1) >= TOL
            columns.append(output)
            combined_columns.append(output)
        matrix = np.column_stack(columns)
        branch_ranks[(m, b)] = int(np.linalg.matrix_rank(matrix, tol=TOL))
        branch_gram_residuals[(m, b)] = float(np.linalg.norm(matrix.conj().T @ matrix - np.eye(8)))
    combined = np.column_stack(combined_columns)
    return {
        "branch_ranks": branch_ranks,
        "branch_gram_residuals": branch_gram_residuals,
        "combined_rank": int(np.linalg.matrix_rank(combined, tol=TOL)),
        "combined_gram_residual": float(np.linalg.norm(combined.conj().T @ combined - np.eye(32))),
        "expected_residual": expected_residual,
        "lock_residual": lock_residual,
        "factor_failures": int(factor_failures),
        "target_dimension": 8,
        "external_reference_preserved_by_isometry": not erase_targets,
    }


def naimark_certificate() -> dict[str, object]:
    """Exact six-outcome Stinespring isometry; no gate compilation is inferred."""
    operators = instrument_operators()
    ordered = tuple(operators)
    isometry = np.vstack(tuple(operators[key] for key in ordered))
    block_residual = 0.0
    for index, key in enumerate(ordered):
        block = isometry[256 * index:256 * (index + 1)]
        block_residual = max(block_residual, float(np.linalg.norm(block - operators[key])))
    return {
        "outcomes": len(ordered),
        "outcome_order": ordered,
        "input_dimension": isometry.shape[1],
        "output_dimension": isometry.shape[0],
        "isometry_residual": float(np.linalg.norm(isometry.conj().T @ isometry - np.eye(256))),
        "block_residual": block_residual,
        "binary_environment_qubits": math.ceil(math.log2(len(ordered))),
        "nn_compiled": False,
    }


def gamma_query_certificate() -> dict[str, object]:
    """Separate the exact rank-two Gamma query from Block72's rank-four query."""
    gamma = ready_projector()
    identity = np.eye(32, dtype=complex)
    complement = identity - gamma
    query = np.block([[complement, gamma], [gamma, complement]])
    query_residual = float(np.linalg.norm(query.conj().T @ query - np.eye(64)))
    pointer_failures = 0
    for basis in range(32):
        source = np.zeros(64, dtype=complex)
        source[basis] = 1
        output = query @ source
        ready = abs(gamma[basis, basis] - 1) < TOL
        expected_pointer = 1 if ready else 0
        pointer_probability = sum(
            abs(output[index]) ** 2
            for index in range(64)
            if index // 32 == expected_pointer
        )
        pointer_failures += abs(pointer_probability - 1) >= TOL

    q_projector = np.zeros((32, 32), dtype=complex)
    for m, b in product((0, 1), repeat=2):
        index = block71.full_index(1, m, b, 0, 0)
        q_projector[index, index] = 1
    readiness_unitary = block71.word_matrix(block72.readiness_word(), 5)
    block72_ready = readiness_unitary @ q_projector @ readiness_unitary.conj().T
    dilation = block71.word_matrix(block71.dilation_word(), 5)
    coherent_ready = dilation @ gamma @ dilation.conj().T
    return {
        "gamma_rank": int(np.linalg.matrix_rank(gamma, tol=TOL)),
        "query_unitarity_residual": query_residual,
        "query_pointer_failures": pointer_failures,
        "query_environment_dimension": 2,
        "query_nn_compiled": False,
        "block72_ready_rank": int(np.linalg.matrix_rank(block72_ready, tol=TOL)),
        "coherent_ready_rank": int(np.linalg.matrix_rank(coherent_ready, tol=TOL)),
        "block72_coherent_residual": float(np.linalg.norm(block72_ready - coherent_ready)),
        "overlap_trace": float(np.trace(block72_ready @ coherent_ready).real),
        "containment_residual": float(np.linalg.norm(block72_ready @ coherent_ready - coherent_ready)),
        "block72_query_is_gamma_query": False,
    }


def apply_one_site(
    state: dict[tuple[int, ...], complex],
    wire: int,
    matrix: np.ndarray,
) -> dict[tuple[int, ...], complex]:
    output: dict[tuple[int, ...], complex] = {}
    for bits, amplitude in state.items():
        source = bits[wire]
        for target in (0, 1):
            coefficient = matrix[target, source]
            if abs(coefficient) < 1.0e-15:
                continue
            result = list(bits)
            result[wire] = target
            key = tuple(result)
            output[key] = output.get(key, 0.0j) + coefficient * amplitude
    return output


def ordered_actions(non_nn: bool = False) -> tuple[tuple[block72.PhysicalAction, ...], tuple[block72.PhysicalAction, ...]]:
    relocation = block72.relocation_certificate()
    archive = block72.compact_archive_certificate()
    prefix = tuple(block72.PhysicalAction("SWAP", swap) for swap in relocation["swaps"])
    physical: list[block72.PhysicalAction] = list(prefix)
    ideal: list[block72.PhysicalAction] = list(prefix)
    for gate in block71.dilation_word():
        sites = tuple(block72.WIRE_SITES[wire] for wire in gate.wires)
        ideal.append(block72.PhysicalAction(gate.kind, sites, gate.matrix))
        if len(gate.wires) == 1:
            physical.append(block72.PhysicalAction(gate.kind, sites, gate.matrix))
        else:
            physical.extend(block72.compile_two_gate(gate)["actions"])
    marker = block72.PhysicalAction("archive_head_H", (block72.WIRE_SITES[0],), block71.H)
    physical.append(marker)
    ideal.append(marker)
    suffix = tuple(block72.PhysicalAction("SWAP", swap) for swap in archive["swaps"])
    physical.extend(suffix)
    ideal.extend(suffix)
    if non_nn:
        physical.append(block72.PhysicalAction("bad_edge", ((0, 0, 0), (2, 0, 0)), block71.CNOT))
    return tuple(physical), tuple(ideal)


def apply_physical_actions(
    state: dict[tuple[int, ...], complex],
    actions: tuple[block72.PhysicalAction, ...],
    site_index: dict[Coord, int],
) -> dict[tuple[int, ...], complex]:
    answer = state
    for action in actions:
        wires = tuple(site_index[site] for site in action.sites)
        if action.kind == "SWAP":
            answer = block72.apply_swap(answer, wires[0], wires[1])
        elif len(wires) == 1 and action.matrix is not None:
            answer = apply_one_site(answer, wires[0], action.matrix)
        elif len(wires) == 2 and action.matrix is not None:
            answer = block72.apply_two(answer, wires[0], wires[1], action.matrix)
        else:
            raise ValueError(action)
    return answer


def ordered_compiler_certificate(non_nn: bool = False) -> dict[str, object]:
    physical, ideal = ordered_actions(non_nn)
    sites = tuple(sorted({site for action in physical + ideal for site in action.sites}))
    site_index = {site: index for index, site in enumerate(sites)}
    role_sites = set(block72.ORIGINAL_WIRE_SITES)
    free_sites = tuple(site for site in sites if site not in role_sites)
    maximum_residual = 0.0
    cases = 0
    for m in (0, 1):
        for background in range(1 << len(free_sites)):
            bits = [0] * len(sites)
            fixed = {"P": 1, "M": m, "B": 0, "R": 0, "A": 0}
            for role, value in fixed.items():
                bits[site_index[block71.STARTS[role]]] = value
            for slot, site in enumerate(free_sites):
                bits[site_index[site]] = (background >> slot) & 1
            state = {tuple(bits): 1.0 + 0.0j}
            observed = apply_physical_actions(state, physical, site_index)
            expected = apply_physical_actions(state, ideal, site_index)
            maximum_residual = max(maximum_residual, block72.state_residual(observed, expected))
            cases += 1
    covariance_failures = 0
    for rotation in block71.ROTATIONS:
        for action in physical:
            rotated = tuple(block71.rotate(rotation, site) for site in action.sites)
            if len(rotated) == 2:
                covariance_failures += block71.distance(rotated[0], rotated[1]) != 1
    parent = block72.compiler_certificate()
    return {
        "physical_primitives": len(physical),
        "ideal_primitives": len(ideal),
        "support_sites": len(sites),
        "free_background_sites": len(free_sites),
        "basis_cases": cases,
        "maximum_residual": maximum_residual,
        "non_nn_failures": sum(
            len(action.sites) == 2 and block71.distance(*action.sites) != 1
            for action in physical
        ),
        "covariance_failures": covariance_failures,
        "parent_complete_primitives": parent["complete_primitive_count"],
        "parent_support_sites": parent["complete_support_size"],
        "parent_label_failures": (
            parent["relocation_stage_failures"]
            + int(parent["formation_stage_failure"])
            + parent["final_role_failures"]
            + parent["target_prestore_failures"]
            + int(parent["unique_final_label_failure"])
        ),
        "support": set(sites),
    }


def rotate_translate(rotation: block71.Rotation, translation: Coord, site: Coord) -> Coord:
    return block71.add(translation, block71.rotate(rotation, site))


def packet_records(rotation: block71.Rotation, translation: Coord, m: int, b: int) -> dict[Coord, Content]:
    return {
        rotate_translate(rotation, translation, block71.ROOT_SITE): block71.K1 if m else block71.K0,
        rotate_translate(rotation, translation, block71.HEAD_SITE): block71.KMINUS,
        rotate_translate(rotation, translation, block71.META_SITE): block71.K1 if b else block71.K0,
    }


def apply_record_outcome(
    records: dict[Coord, Content],
    support: set[Coord],
    writes: dict[Coord, Content] | None,
    outcome: str = "event",
    overwrite: bool = False,
) -> tuple[str, dict[Coord, Content]]:
    """Execute the classical half of one hybrid outcome on a complete map."""
    if not records.keys().isdisjoint(support):
        if overwrite and writes is not None:
            updated = dict(records)
            updated.update(writes)
            return "event", updated
        return "refusal", dict(records)
    if outcome in {"refusal", "no_event"}:
        return outcome, dict(records)
    if writes is None or outcome != "event":
        raise ValueError("event outcomes require a write packet")
    updated = dict(records)
    updated.update(writes)
    return "event", updated


def sorted_record_items(records: dict[Coord, Content]) -> tuple[tuple[Coord, Content], ...]:
    return tuple(sorted(records.items()))


def hybrid_distribution(
    records: dict[Coord, Content],
    support: set[Coord],
    state: np.ndarray,
    *,
    rotation: block71.Rotation,
    translation: Coord,
    overwrite: bool = False,
) -> tuple[HybridOutcome, ...]:
    """Direct-sum Record guard followed by the six-outcome quantum instrument."""
    occupied = not records.keys().isdisjoint(support)
    if occupied and not overwrite:
        return (
            HybridOutcome(
                "guard_refusal",
                1.0,
                state.copy(),
                sorted_record_items(records),
            ),
        )
    outcomes: list[HybridOutcome] = []
    for key, operator in instrument_operators().items():
        output = operator @ state
        probability = float(np.vdot(output, output).real)
        if probability < TOL:
            continue
        normalized = output / math.sqrt(probability)
        updated = dict(records)
        if isinstance(key, tuple):
            m, b = key
            updated.update(packet_records(rotation, translation, m, b))
        outcomes.append(
            HybridOutcome(key, probability, normalized, sorted_record_items(updated))
        )
    return tuple(outcomes)


def hybrid_record_certificate(support: set[Coord], overwrite: bool = False) -> dict[str, object]:
    normalization_failures = append_failures = decode_failures = 0
    prior_failures = replay_failures = occupied_failures = continuity_failures = 0
    event_cases = 0
    translation = (7, -5, 3)
    sentinel = (100, -100, 90)
    for rotation in block71.ROTATIONS:
        rotated_support = {rotate_translate(rotation, translation, site) for site in support}
        for m in (0, 1):
            weights = {
                "refusal": Fraction(0),
                "no_event": 1 - HAZARD,
                (m, 0): HAZARD * block72.BRANCH_WEIGHTS[m][0],
                (m, 1): HAZARD * block72.BRANCH_WEIGHTS[m][1],
            }
            normalization_failures += sum(weights.values(), Fraction(0)) != 1
            initial: dict[Coord, Content] = {sentinel: block71.KPLUS}
            no_status, no_output = apply_record_outcome(
                initial, rotated_support, None, outcome="no_event"
            )
            prior_failures += no_status != "no_event" or no_output != initial
            ref_status, ref_output = apply_record_outcome(
                initial, rotated_support, None, outcome="refusal"
            )
            prior_failures += ref_status != "refusal" or ref_output != initial
            for b in (0, 1):
                writes = packet_records(rotation, translation, m, b)
                status, output = apply_record_outcome(initial, rotated_support, writes)
                append_failures += status != "event"
                append_failures += len(output) != len(initial) + 3
                prior_failures += output.get(sentinel) != block71.KPLUS
                packets = block71.find_packets(output)
                matches = tuple(
                    packet for packet in packets
                    if packet["root"] in writes and packet["m"] == m and packet["b"] == b
                )
                if len(matches) != 1:
                    decode_failures += 1
                else:
                    decode_failures += matches[0]["frame"] != rotation
                if matches:
                    root = matches[0]["root"]
                    head = matches[0]["head"]
                    delta = {root: -1, head: 1}
                    boundary = {root: 1, head: -1}
                    continuity_failures += any(delta[site] + boundary[site] != 0 for site in delta)
                replay_status, replay = apply_record_outcome(
                    output,
                    rotated_support,
                    packet_records(rotation, translation, m, 1 - b),
                    overwrite=overwrite,
                )
                replay_failures += replay_status != "refusal" or replay != output
                event_cases += 1

            occupied = dict(initial)
            occupied[next(iter(rotated_support))] = block71.KPLUS
            occupied_status, refused = apply_record_outcome(
                occupied,
                rotated_support,
                packet_records(rotation, translation, m, 0),
                overwrite=overwrite,
            )
            occupied_failures += occupied_status != "refusal" or refused != occupied
    return {
        "event_cases": event_cases,
        "normalization_failures": normalization_failures,
        "append_failures": append_failures,
        "decode_failures": decode_failures,
        "prior_failures": prior_failures,
        "replay_failures": replay_failures,
        "occupied_failures": occupied_failures,
        "continuity_failures": continuity_failures,
        "atomic_records_per_event": 3,
        "host_realized_branch": False,
        "host_m": False,
    }


def hybrid_quantum_guard_certificate(support: set[Coord], overwrite: bool = False) -> dict[str, object]:
    identity_rotation: block71.Rotation = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    translation: Coord = (0, 0, 0)
    sentinel: Coord = (100, -100, 90)
    blank_records: dict[Coord, Content] = {sentinel: block71.KPLUS}
    normalization_failures = weight_failures = output_record_failures = 0
    replay_failures = occupied_failures = nonready_failures = 0
    replay_cases = blank_cases = 0
    witness_post_state: np.ndarray | None = None
    for m, target_index in product((0, 1), range(8)):
        target = np.eye(8, dtype=complex)[:, target_index]
        state = clean_input_vector(m, target)
        distribution = hybrid_distribution(
            blank_records,
            support,
            state,
            rotation=identity_rotation,
            translation=translation,
            overwrite=overwrite,
        )
        normalization_failures += abs(sum(item.probability for item in distribution) - 1) >= TOL
        by_key = {item.key: item for item in distribution}
        weight_failures += "guard_refusal" in by_key or "refusal" in by_key
        weight_failures += abs(by_key["no_event"].probability - float(1 - HAZARD)) >= TOL
        for b in (0, 1):
            event = by_key[(m, b)]
            expected_weight = float(HAZARD * block72.BRANCH_WEIGHTS[m][b])
            weight_failures += abs(event.probability - expected_weight) >= TOL
            expected_records = dict(blank_records)
            expected_records.update(packet_records(identity_rotation, translation, m, b))
            output_record_failures += event.records != sorted_record_items(expected_records)
            replay = hybrid_distribution(
                dict(event.records),
                support,
                event.state,
                rotation=identity_rotation,
                translation=translation,
                overwrite=overwrite,
            )
            replay_failures += not (
                len(replay) == 1
                and replay[0].key == "guard_refusal"
                and abs(replay[0].probability - 1) < TOL
                and replay[0].records == event.records
                and float(np.linalg.norm(replay[0].state - event.state)) < TOL
            )
            if m == 0 and b == 0 and target_index == 1:
                witness_post_state = event.state
            replay_cases += 1
        blank_cases += 1

    occupied_records = dict(blank_records)
    occupied_records[next(iter(support))] = block71.KPLUS
    occupied_states = (
        clean_input_vector(0, np.eye(8, dtype=complex)[:, 0]),
        clean_input_vector(1, np.ones(8, dtype=complex) / math.sqrt(8)),
        coherent_input_vector(
            (1 / math.sqrt(2), 1j / math.sqrt(2)),
            np.asarray((1, 1j, 0, 0, 0, 0, 0, 0), dtype=complex) / math.sqrt(2),
        ),
    )
    for state in occupied_states:
        distribution = hybrid_distribution(
            occupied_records,
            support,
            state,
            rotation=identity_rotation,
            translation=translation,
            overwrite=overwrite,
        )
        occupied_failures += not (
            len(distribution) == 1
            and distribution[0].key == "guard_refusal"
            and abs(distribution[0].probability - 1) < TOL
            and distribution[0].records == sorted_record_items(occupied_records)
            and float(np.linalg.norm(distribution[0].state - state)) < TOL
        )

    nonready_low = np.zeros(32, dtype=complex)
    nonready_low[block71.full_index(0, 0, 0, 0, 0)] = 1
    nonready_state = np.kron(np.eye(8, dtype=complex)[:, 0], nonready_low)
    nonready = hybrid_distribution(
        blank_records,
        support,
        nonready_state,
        rotation=identity_rotation,
        translation=translation,
    )
    nonready_failures += not (
        len(nonready) == 1
        and nonready[0].key == "refusal"
        and abs(nonready[0].probability - 1) < TOL
        and nonready[0].records == sorted_record_items(blank_records)
        and float(np.linalg.norm(nonready[0].state - nonready_state)) < TOL
    )

    if witness_post_state is None:
        raise AssertionError("missing replay witness")
    witness_density = np.outer(witness_post_state, witness_post_state.conj())
    unguarded_density = np.zeros_like(witness_density)
    for operator in instrument_operators().values():
        output = operator @ witness_post_state
        unguarded_density += np.outer(output, output.conj())
    unguarded_replay_change = float(np.linalg.norm(unguarded_density - witness_density))
    return {
        "blank_cases": blank_cases,
        "replay_cases": replay_cases,
        "occupied_cases": len(occupied_states),
        "normalization_failures": normalization_failures,
        "weight_failures": weight_failures,
        "output_record_failures": output_record_failures,
        "replay_failures": replay_failures,
        "occupied_failures": occupied_failures,
        "nonready_failures": nonready_failures,
        "unguarded_replay_change": unguarded_replay_change,
        "guard_is_declared_direct_sum": True,
        "guard_nn_compiled": False,
    }


def resource_certificate(omit_resource: bool = False) -> dict[str, object]:
    compiler = block72.compiler_certificate()
    resources = block72.resource_certificate()
    kraus = kraus_certificate()
    gamma_query = gamma_query_certificate()
    naimark = naimark_certificate()
    fixed_count = 0 if omit_resource else resources["fixed_input_count"]
    return {
        "fixed_inputs": resources["fixed_input_roles"],
        "fixed_input_count": fixed_count,
        "matter_input_dimension": resources["matter_inputs"],
        "arbitrary_target_dimension": 8,
        "blank_record_targets": 3,
        "event_support_sites": compiler["complete_support_size"],
        "coherent_core_primitives": compiler["complete_primitive_count"],
        "gamma_query_rank": gamma_query["gamma_rank"],
        "gamma_query_unitarity_residual": gamma_query["query_unitarity_residual"],
        "gamma_query_pointer_failures": gamma_query["query_pointer_failures"],
        "gamma_query_environment_dimension": gamma_query["query_environment_dimension"],
        "gamma_query_nn_compiled": gamma_query["query_nn_compiled"],
        "block72_query_rank": gamma_query["block72_ready_rank"],
        "block72_query_mismatch": gamma_query["block72_coherent_residual"],
        "block72_query_overlap": gamma_query["overlap_trace"],
        "block72_query_containment_residual": gamma_query["containment_residual"],
        "block72_query_is_gamma_query": gamma_query["block72_query_is_gamma_query"],
        "naimark_outcomes": naimark["outcomes"],
        "naimark_input_dimension": naimark["input_dimension"],
        "naimark_output_dimension": naimark["output_dimension"],
        "naimark_isometry_residual": naimark["isometry_residual"],
        "naimark_block_residual": naimark["block_residual"],
        "naimark_nn_compiled": naimark["nn_compiled"],
        "extra_clean_route_bank": 0,
        "minimal_total_kraus_environment_dimension": kraus["kraus_rank"],
        "minimal_qubit_environment_if_unitarized": math.ceil(math.log2(kraus["kraus_rank"])),
        "event_consumes_ready_packet": True,
        "clean_input_genesis_supplied": False,
        "clean_input_renewal_supplied": False,
        "hazard_supplied": True,
        "instrument_as_primitive_supplied": False,
        "outcome_coupling_nn_compiled": False,
        "record_membership_append_nn_compiled": False,
        "record_guard_nn_compiled": False,
    }


def admissibility_gap_certificate() -> dict[str, object]:
    """Expose the one-site NN marginal obligation rather than infer it away."""
    empty_records: dict[Coord, Content] = {}
    target_sites = {
        "head": block71.HEAD_SITE,
        "root": block71.ROOT_SITE,
        "meta": block71.META_SITE,
    }
    signatures = {
        role: tuple(
            empty_records.get(block71.add(site, direction))
            for direction in block71.DIRECTIONS
        )
        for role, site in target_sites.items()
    }

    # Conditional on an event with the clean m=0 input, the instrument's three
    # one-site lock measures differ even though all three prior Record
    # neighbourhoods are the same blank six-neighbour condition.
    measures = {
        "head": {"minus": Fraction(1, 1)},
        "root": {"zero": Fraction(1, 1)},
        "meta": {"zero": Fraction(1, 2), "one": Fraction(1, 2)},
    }

    def total_variation(left: dict[str, Fraction], right: dict[str, Fraction]) -> Fraction:
        labels = set(left) | set(right)
        return sum((abs(left.get(label, Fraction()) - right.get(label, Fraction())) for label in labels), Fraction()) / 2

    pairwise_tv = {
        (left, right): total_variation(measures[left], measures[right])
        for left, right in (("head", "root"), ("head", "meta"), ("root", "meta"))
    }
    return {
        "target_sites": target_sites,
        "distinct_prior_nn_record_signatures": len(set(signatures.values())),
        "conditional_event_measures": measures,
        "pairwise_total_variation": pairwise_tv,
        "pairwise_nonidentical": sum(value > 0 for value in pairwise_tv.values()),
        "extra_nn_condition_or_role_bridge_supplied": False,
        "current_fixed_nn_measure_compatibility_established": False,
    }


def ontology_certificate() -> dict[str, object]:
    _ref, axiom = current_axiom_text()
    flat = " ".join(axiom.split())
    return {
        "state_is_records": "A state is a configuration of records." in flat,
        "only_records_readable": "Only records are readable." in flat,
        "possibility_domain_M2": "The full one-site possibility domain has algebraic presentation `M_2(C)`." in flat,
        "admissibility_not_dynamics": "Admissibility is not a dynamics axiom." in flat,
        "update_law_open": "update laws" in flat,
        "formation_rules_open": "the remaining formation rules" in flat,
        "source_action_open": "source/action and physical-observable identification" in flat,
        "live_M2_controller_bridge_approved": False,
        "candidate_requires_amended_or_registered_formation_law": True,
        "record_only_nonunitary_route_still_live": True,
        "single_axiom_forced": False,
        "live_route_payload_items": 7,
    }


def boundary_surface_ok(law_claim: bool = False) -> bool:
    if not NOTE_PATH.is_file():
        return False
    note = NOTE_PATH.read_text(encoding="utf-8")
    needles = (
        "### N1 — Alternative-route enumeration and normalization",
        "### N2 — Wall-independence audit",
        "### N3 — Hidden-wall scan",
        "### N4 — Residual matching",
        "### N5 — Rhetoric and granularity audit",
        "### N6 — Partial-closure path scan",
        "### N7 — Steelman and strongest surviving escape route",
        "### N8 — Cross-cycle echo audit",
        "live-M2 ontology is conditional",
        "six-dimensional outcome environment",
        "no supplied realized branch",
        "no host-selected matter bit",
        "sufficient live-route payload",
        "current fixed one-site NN Admissibility compatibility remains open",
        "zero TOE percentage movement",
        "not an approved primitive",
        "Record-only nonunitary route remains live",
        "overlap confluence is not executed",
    )
    return not law_claim and all(needle in note for needle in needles)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=(
        "stale_axiom", "break_completeness", "host_select_m", "erase_targets",
        "non_nn", "overwrite", "omit_resource", "law_claim",
    ))
    args = parser.parse_args()
    mutation = args.mutation
    checks = Checks()

    authority = authority_certificate(mutation == "stale_axiom")
    authority_ok = (
        authority["local_matches"] and authority["current_inputs_match"] and authority["historical_parents_match"]
        and authority["parent_paths_exist"] and authority["parent_hashes_match"]
        and authority["current_contract"]
        and not authority["forced_stale"]
    )
    checks.check(
        "A-current-axiom-and-exact-parent-authority",
        authority_ok,
        f"{authority['ref']}={str(authority['main'])[:10]}, axiom={str(authority['axiom_sha256'])[:12]}; Block71/72/73 current files and original receipt identities are separately bound",
    )

    parent = block72.parent_certificate()
    parent_ok = (
        parent["branch_residual"] < TOL and parent["archive_rank"] == 32
        and parent["archive_gram"] < TOL and parent["lock_residual"] < TOL
        and parent["packet_failures"] == 0
    )
    checks.check(
        "B-Block71-archive-lock-and-Block72-compiler-receipt",
        parent_ok,
        f"archive rank={parent['archive_rank']}/32, Gram={parent['archive_gram']:.1e}, lock={parent['lock_residual']:.1e}, packet failures={parent['packet_failures']}",
    )

    kraus = kraus_certificate(
        mutation == "break_completeness",
        mutation == "host_select_m",
    )
    kraus_ok = (
        kraus["outcomes"] == 6 and kraus["ready_rank"] == 2
        and kraus["completeness_residual"] < TOL and kraus["kraus_rank"] == 6
        and kraus["kraus_gram_minimum"] > -TOL and kraus["basis_cases"] == 64
        and kraus["probability_failures"] == 0 and kraus["branch_vector_failures"] == 0
        and kraus["coherent_cases"] == 45 and kraus["coherent_failures"] == 0
        and not kraus["host_selected_m"]
    )
    checks.check(
        "C-one-six-outcome-CPTP-instrument-without-host-branch",
        kraus_ok,
        f"rank-{kraus['ready_rank']} readiness, six Kraus outcomes/rank {kraus['kraus_rank']}, completeness={kraus['completeness_residual']:.1e}; {kraus['basis_cases']} basis and {kraus['coherent_cases']} coherent rows",
    )

    archive = archive_reference_certificate(mutation == "erase_targets")
    archive_ok = (
        set(archive["branch_ranks"].values()) == {8}
        and max(archive["branch_gram_residuals"].values()) < TOL
        and archive["combined_rank"] == 32 and archive["combined_gram_residual"] < TOL
        and archive["expected_residual"] < TOL and archive["lock_residual"] < TOL
        and archive["factor_failures"] == 0 and archive["external_reference_preserved_by_isometry"]
    )
    checks.check(
        "D-arbitrary-target-reference-preserving-archive-and-exact-lock",
        archive_ok,
        f"branch ranks={tuple(archive['branch_ranks'].values())}, combined={archive['combined_rank']}/32, Gram={archive['combined_gram_residual']:.1e}, lock={archive['lock_residual']:.1e}",
    )

    compiler = ordered_compiler_certificate(mutation == "non_nn")
    compiler_ok = (
        compiler["physical_primitives"] == 73 and compiler["ideal_primitives"] == 49
        and compiler["support_sites"] == 15 and compiler["free_background_sites"] == 10
        and compiler["basis_cases"] == 2048 and compiler["maximum_residual"] < TOL
        and compiler["non_nn_failures"] == 0 and compiler["covariance_failures"] == 0
        and compiler["parent_complete_primitives"] == 73
        and compiler["parent_support_sites"] == 15 and compiler["parent_label_failures"] == 0
    )
    checks.check(
        "E-ordered-73-primitive-NN-coherent-core-on-arbitrary-backgrounds",
        compiler_ok,
        f"{compiler['physical_primitives']} primitives/{compiler['support_sites']} sites; {compiler['basis_cases']} clean-domain arbitrary-background bases match the ideal word at {compiler['maximum_residual']:.1e}",
    )

    hybrid = hybrid_record_certificate(compiler["support"], mutation == "overwrite")
    quantum_guard = hybrid_quantum_guard_certificate(
        compiler["support"], mutation == "overwrite"
    )
    hybrid_ok = (
        hybrid["event_cases"] == 96 and not any(
            hybrid[key] for key in (
                "normalization_failures", "append_failures", "decode_failures",
                "prior_failures", "replay_failures", "occupied_failures",
                "continuity_failures",
            )
        )
        and hybrid["atomic_records_per_event"] == 3
        and not hybrid["host_realized_branch"] and not hybrid["host_m"]
        and quantum_guard["blank_cases"] == 16
        and quantum_guard["replay_cases"] == 32
        and quantum_guard["occupied_cases"] == 3
        and not any(
            quantum_guard[key] for key in (
                "normalization_failures", "weight_failures", "output_record_failures",
                "replay_failures", "occupied_failures", "nonready_failures",
            )
        )
        and quantum_guard["unguarded_replay_change"] > TOL
        and quantum_guard["guard_is_declared_direct_sum"]
        and not quantum_guard["guard_nn_compiled"]
    )
    checks.check(
        "F-total-hybrid-refusal-no-event-guarded-candidate-update",
        hybrid_ok,
        f"{hybrid['event_cases']} frame/m/b Record cases plus {quantum_guard['blank_cases']} quantum rows and {quantum_guard['replay_cases']} complete-state replays normalize; the direct-sum guard preserves occupied/replayed quantum+Record state exactly, while unguarded replay changes density by {quantum_guard['unguarded_replay_change']:.3g}",
    )

    reset = archive_reference_certificate(True)
    reset_ok = (
        reset["combined_rank"] == 4 and reset["combined_gram_residual"] > 1
        and not reset["external_reference_preserved_by_isometry"]
    )
    checks.check(
        "G-unarchived-reset-control-loses-target-information",
        reset_ok,
        f"hostile reset has rank {reset['combined_rank']}/32 and Gram residual {reset['combined_gram_residual']:.2f}; the archive is load-bearing",
    )

    resources = resource_certificate(mutation == "omit_resource")
    resource_ok = (
        resources["fixed_input_count"] == 4 and resources["matter_input_dimension"] == 2
        and resources["arbitrary_target_dimension"] == 8 and resources["blank_record_targets"] == 3
        and resources["event_support_sites"] == 15 and resources["coherent_core_primitives"] == 73
        and resources["gamma_query_rank"] == 2
        and resources["gamma_query_unitarity_residual"] < TOL
        and resources["gamma_query_pointer_failures"] == 0
        and resources["gamma_query_environment_dimension"] == 2
        and not resources["gamma_query_nn_compiled"]
        and resources["block72_query_rank"] == 4
        and abs(resources["block72_query_mismatch"] - math.sqrt(2)) < TOL
        and abs(resources["block72_query_overlap"] - 2) < TOL
        and resources["block72_query_containment_residual"] < TOL
        and not resources["block72_query_is_gamma_query"]
        and resources["naimark_outcomes"] == 6
        and resources["naimark_input_dimension"] == 256
        and resources["naimark_output_dimension"] == 1536
        and resources["naimark_isometry_residual"] < TOL
        and resources["naimark_block_residual"] < TOL
        and not resources["naimark_nn_compiled"]
        and resources["extra_clean_route_bank"] == 0
        and resources["minimal_total_kraus_environment_dimension"] == 6
        and resources["minimal_qubit_environment_if_unitarized"] == 3
        and resources["event_consumes_ready_packet"]
        and not resources["clean_input_genesis_supplied"]
        and not resources["clean_input_renewal_supplied"]
        and resources["hazard_supplied"] and not resources["instrument_as_primitive_supplied"]
        and not resources["outcome_coupling_nn_compiled"]
        and not resources["record_membership_append_nn_compiled"]
        and not resources["record_guard_nn_compiled"]
    )
    checks.check(
        "H-exact-Gamma-Naimark-and-resource-implementation-boundary",
        resource_ok,
        f"Gamma rank {resources['gamma_query_rank']} has an exact pointer query but differs by sqrt(2) from Block72 rank {resources['block72_query_rank']}; six-outcome {resources['naimark_output_dimension']}x{resources['naimark_input_dimension']} isometry passes, while only the 73-primitive coherent core is NN-compiled",
    )

    ontology = ontology_certificate()
    admissibility = admissibility_gap_certificate()
    ontology_ok = (
        ontology["state_is_records"] and ontology["only_records_readable"]
        and ontology["possibility_domain_M2"] and ontology["admissibility_not_dynamics"]
        and ontology["formation_rules_open"] and ontology["source_action_open"]
        and not ontology["live_M2_controller_bridge_approved"]
        and ontology["candidate_requires_amended_or_registered_formation_law"]
        and ontology["record_only_nonunitary_route_still_live"]
        and not ontology["single_axiom_forced"] and ontology["live_route_payload_items"] == 7
        and admissibility["distinct_prior_nn_record_signatures"] == 1
        and admissibility["pairwise_nonidentical"] == 3
        and admissibility["pairwise_total_variation"][("head", "root")] == 1
        and admissibility["pairwise_total_variation"][("head", "meta")] == 1
        and admissibility["pairwise_total_variation"][("root", "meta")] == Fraction(1, 2)
        and not admissibility["extra_nn_condition_or_role_bridge_supplied"]
        and not admissibility["current_fixed_nn_measure_compatibility_established"]
    )
    checks.check(
        "I-live-M2-ontology-NN-admissibility-and-payload-boundary",
        ontology_ok,
        "three identical blank prior NN Record conditions have unequal head/root/meta lock marginals (TV 1,1,1/2); current-law qualification needs an added condition/formation bridge plus state, resources, actuality/time, overlap, and source typing",
    )

    boundary_ok = boundary_surface_ok(mutation == "law_claim")
    checks.check(
        "J-N1-N8-claim-axiom-gravity-and-TOE-boundary",
        boundary_ok,
        "the note stress-tests alternatives, exact residuals, resources, ontology, the live-route payload, and the no-score/no-retention boundary",
    )

    print(
        f"METRICS kraus_outcomes={kraus['outcomes']} kraus_rank={kraus['kraus_rank']} "
        f"completeness={kraus['completeness_residual']:.2e} archive_rank={archive['combined_rank']} "
        f"coherent_core_primitives={compiler['physical_primitives']} coherent_core_basis={compiler['basis_cases']} "
        f"record_cases={hybrid['event_cases']} resource_fixed={resources['fixed_input_count']}"
    )
    print(
        "BOUNDARY: one finite live-M2 candidate now joins refusal, no-event, exact branch weights, conservative archive, and guarded same-carrier Record append without a supplied branch or host-selected m; current fixed one-site NN Admissibility compatibility remains open, as do live-substrate state authority, extensional law/hazard selection, clean-resource genesis and renewal, physical actuality, asynchronous overlap confluence, clock, gravity source typing, approved-primitive registration, audit retention, obligation retirement, and TOE percentage movement"
    )
    print("per_element: checked six Kraus operators, all clean matter/target basis rows, coherent matter/target rows, four branch isometries, exact target projectors, and the unarchived reset control")
    print("per_site: checked five live roles, three arbitrary targets, every one of 15 coherent-core support sites, all 73 ordered core primitives, prior Records, occupancy, replay, and exact source edge")
    print("per_mode: checked both live matter basis values, three coherent matter states, four (m,b) outcomes, eight target bases, 24 proper-cubic frames, no-event, and refusal")
    print("per_block: checked Block71 archive/lock, Block72 ordered NN coherent core and rank-four query mismatch, Block73 Kraus family, the exact rank-two Gamma query, six-outcome Naimark isometry, hybrid Record update, blank-neighborhood marginal mismatch, and seven-item sufficient live-route payload")
    print("lattice_wide: checked and not executed — this is one finite candidate instrument; no homogeneous full-Z3 process, overlap confluence, capacity renewal, physical clock, or gravity coupling is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
