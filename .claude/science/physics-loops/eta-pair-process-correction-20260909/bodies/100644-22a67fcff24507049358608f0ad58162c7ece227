#!/usr/bin/env python3
"""Block34: normalized Record-pair source / gravity pincer.

The runner reconstructs the actual Block32 four-lateral-exit pair law.  It
separates geometric front transversality from a physical momentum Ward law,
proves the homogeneous source-amplitude ray dichotomy, and executes the unique
diagonal-positive score in the explicitly restricted equality/off-diagonal
grammar, normalized at the uniform family member q_0.  The fixed score's
variance returns to its q_0 value at {0, 2/3}.  This is a reference-dependent
self-comparison, not a Fisher-information, action-unit, source-unit, or
physical-selection law.

The physical Record-source identity, absolute reference/response unit,
coupling, local lattice four-stress, cadence, and zero-mode law are not supplied
here.  No physical lambda selection, gravity law, axiom change, audit verdict,
obligation retirement, or TOE-score movement is claimed.
"""

from __future__ import annotations

import ast
import hashlib
import itertools
import json
import re
import subprocess
from dataclasses import dataclass, fields, replace
from functools import lru_cache
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 300
PACKET_REL = (
    ".claude/science/physics-loops/"
    "toe-source-eta-ownership-block34-normalized-pair-source-gravity-"
    "pincer-20260831"
)
PACKET = ROOT / PACKET_REL
RUNNER_SOURCE_PIN = PACKET / "RUNNER_SOURCE_PIN.md"
STATIC_ATTACK = PACKET / "INDEPENDENT_STATIC_ATTACK_FINAL.md"
EXPECTED_TERMINAL_PATH = PACKET / "POSTEXECUTION_EXPECTED_TERMINAL.txt"
STATIC_ATTACK_SHA256 = "3a6617a4c9c1c698690622513e02e13a7e8fea7a6e3507de175ad46ac05e2664"

CANONICAL_MAIN_COMMIT = "aa7338d1fbc34a4b92205182b26793194e4727b6"
CANONICAL_AUTHORITY = {
    "docs/MINIMAL_AXIOMS_2026-06-29.md": (
        "bc23300becfe4e4db57153c0e94cfcdf2338da71",
        "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753",
    ),
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md": (
        "a74392f6939b2e51109756c37d6d5d59bb54c5a4",
        "e7e75a36bd16094cbb547f6b215680ac45adc565c4cc93f05b0af17992eb9292",
    ),
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md": (
        "b8c02523ffd94fb6dcc69d72f9fd03b6afa24f2b",
        "5516fb0bb8f50286b3c34d3f2668b1a2e347b9f7e257a8b5745f84f1093dd96b",
    ),
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md": (
        "5acb4643882438f8dd16baf9694e6fa2d33d1dc6",
        "755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563",
    ),
    "docs/audit/data/axiom_premise_nodes.json": (
        "b93959cca4f7e26c673cdccbe601e50c3cb93daa",
        "615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37",
    ),
    "docs/PLANCK_SOURCE_UNIT_NORMALIZATION_SUPPORT_THEOREM_NOTE_2026-04-25.md": (
        "86186442c2e6d1b46187e89a5e7b0dda9af25738",
        "1554a6d4f95a53e9fd10d19099b1d277df19b1254e433e87bf8984b5ba2e4827",
    ),
    "docs/I1_NATIVE_QUADRATIC_STATIC_SOURCE_NORMALIZATION_BRIDGE_2026-06-08.md": (
        "d587d82e7af8af8e1535ca00f400cc577f5edefd",
        "d8dfb6b2348b8949f70f81e9a02c4c050a5d6d3da1de0bd059c5e69ed8262618",
    ),
    "docs/SOURCE_MEASURE_PLANCK_ACTION_RN_SOURCE_UNIT_BRIDGE_NOTE_2026-05-30.md": (
        "47f02e1fe7cfcc54afbfcb6b137727b2e9ae2cb1",
        "e299c17a7bc7d8e0817390145326e410c0e31b164df88bbb21e708b35c728ab8",
    ),
    "docs/audit/data/ledger/pl/planck_source_unit_normalization_support_theorem_note_2026-04-25.json": (
        "cea61649eb2491bd65719ed4de06e881530090b0",
        "9adb736cf4ebc4132e691b6536ee81fcf90a4ec804c17f7478bedaf727038812",
    ),
    "docs/audit/data/ledger/i1/i1_native_quadratic_static_source_normalization_bridge_2026-06-08.json": (
        "f3f8ec59c403bb212b5e9c749b46eb4139a43615",
        "3d5f8d94bbd318f63b1192a4d984a01815eebcd53890c3fdd3fd4697125955c0",
    ),
    "docs/audit/data/ledger/so/source_measure_planck_action_rn_source_unit_bridge_note_2026-05-30.json": (
        "458b32edcb0fc988b690914a55be863002204eb9",
        "5ecaed8c5a8040b185bca0b7b0eb2b792270488920017d3c3b9719117484028a",
    ),
}

DIRECT_HASHES = {
    "docs/ADMISSIBILITY_D4_SYMBOLIC_LAMBDA_GUARDED_FINITE_SUCCESSOR_"
    "TRANSACTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md":
        "5d7da090e39bbdd9120245804e049577bbacbd9acf3d6eaee79eadc68a5adb36",
    "scripts/admissibility_d4_symbolic_lambda_guarded_state_carrier_"
    "successor_gate_2026_08_31.py":
        "0547f7b51d8e93f08d5dcd5e3493e724319b98c003a1810490a772b684965fb2",
    "docs/ADMISSIBILITY_D4_CLASSICAL_SCREENING_CAUSE_PERSISTENCE_RENEWAL_"
    "LOCUS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md":
        "0aa4f91689f37e6d086ae316db9b8f5169978574585bc36e5deb6da60459940c",
    "scripts/admissibility_d4_classical_screening_cause_renewal_locus_"
    "gate_2026_08_31.py":
        "845e2c73b54a4fec004c3302fa4b796d29c9650594fb05150092a8718bda8caf",
}

FROZEN = {
    "APPROACH_REGISTRY.md":
        "c7d5beb393c0299239d3ad8f1f9727792ad57687eb3ad456a267e7a524f46ec2",
    "ARTIFACT_PLAN.md":
        "4bd9cd0032441af05cfb878cde6bf66551da76a383003c290d7e512935aab79d",
    "ASSUMPTIONS_AND_IMPORTS.md":
        "996fbe6ab4c2d2daf58f669416d7151e0a72a3558b2c6c2b8a9eeb8436489d11",
    "AUTHORITY_GATE.md":
        "f7ce16f840a10c7842eec81b9e67ef7c9556be0de258f066ce123cb5b148337a",
    "GOAL.md":
        "6e46d3a439d0284db94b27bc22deb84972584f30be629d8a9bb3cfc6e4287345",
    "MUTATION_PLAN.md":
        "823571ca6132cd1fc0f4442b599eb22056e65eb07cabb93f8d12f1fccb1ffd55",
    "NO_GO_DISCIPLINE_CHECKLIST.md":
        "322127d00ecfd9df495270df46c541b581654cd23dff329bca33dd0b0d015694",
    "OPPORTUNITY_QUEUE.md":
        "1ce8ca2b960d81092a15c5058b7d6e7ba0ebf7bed2e97ab2a1bf1a5ae6dfcd05",
    "PANEL_RETURN.md":
        "b40ca1ef30e72b9a8126a07954bb441f65bb300d3d1f384c92ba44434995d260",
    "PREFLIGHT_WITNESSES.md":
        "b5068ddb34f629ec12615fb4449eb2a96b2cb27cd94a9ddccfc6c74d94044279",
    "PREREG_AMENDMENT_WARD_COMPLETION_AND_COUNT_ONCE.md":
        "552cc5543a925ec5f4b2f4d44314ef6f1407de19ceb3cf1b77bdc94a3d80e407",
    "ROUTE_PORTFOLIO.md":
        "83705f3c687b8770cb43c59d0fc1ed295d7398132afef37c302373032b3958d7",
    "STATE.yaml":
        "d41636e4e28704c1303866193f52cf68c7cdde21766898eb806e860c931730fa",
    "TRACE_GATE.md":
        "cb6ed0354a55005827ee5cef071d6acdecabeede3b770d1cfcb8145bc7aed461",
    "CANONICAL_MAIN_AUTHORITY_MANIFEST.md":
        "7346b21d9189fd604a4c27657192ccd42cd6c5b9fbb5eca0cf1ddcd867b2785b",
    "POSTEXECUTION_EXPECTED_TERMINAL.txt":
        "c01c05fbef9c538e06a194f007b963db4caabe3c0364f410f00d5398bbd950c0",
    "POSTEXECUTION_NO_GO_DISCIPLINE_CHECKLIST.md":
        "9ed2097ce66edbc440249412faa4338571f951a67e9f2d46b97ce679fa9aa016",
    "POSTEXECUTION_STATE.yaml":
        "c8fe21b3c41e246334c5e02f8881cc6036ee0cd2b521305331fe3bd2103ee024",
}

# Literal tuple required by the cache and forensic parsers.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_D4_SYMBOLIC_LAMBDA_GUARDED_FINITE_SUCCESSOR_TRANSACTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md",
    "scripts/admissibility_d4_symbolic_lambda_guarded_state_carrier_successor_gate_2026_08_31.py",
    "docs/ADMISSIBILITY_D4_CLASSICAL_SCREENING_CAUSE_PERSISTENCE_RENEWAL_LOCUS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md",
    "scripts/admissibility_d4_classical_screening_cause_renewal_locus_gate_2026_08_31.py",
    ".claude/science/physics-loops/toe-source-eta-ownership-block34-normalized-pair-source-gravity-pincer-20260831/APPROACH_REGISTRY.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block34-normalized-pair-source-gravity-pincer-20260831/ARTIFACT_PLAN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block34-normalized-pair-source-gravity-pincer-20260831/ASSUMPTIONS_AND_IMPORTS.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block34-normalized-pair-source-gravity-pincer-20260831/AUTHORITY_GATE.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block34-normalized-pair-source-gravity-pincer-20260831/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block34-normalized-pair-source-gravity-pincer-20260831/MUTATION_PLAN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block34-normalized-pair-source-gravity-pincer-20260831/NO_GO_DISCIPLINE_CHECKLIST.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block34-normalized-pair-source-gravity-pincer-20260831/OPPORTUNITY_QUEUE.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block34-normalized-pair-source-gravity-pincer-20260831/PANEL_RETURN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block34-normalized-pair-source-gravity-pincer-20260831/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block34-normalized-pair-source-gravity-pincer-20260831/PREREG_AMENDMENT_WARD_COMPLETION_AND_COUNT_ONCE.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block34-normalized-pair-source-gravity-pincer-20260831/ROUTE_PORTFOLIO.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block34-normalized-pair-source-gravity-pincer-20260831/STATE.yaml",
    ".claude/science/physics-loops/toe-source-eta-ownership-block34-normalized-pair-source-gravity-pincer-20260831/TRACE_GATE.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block34-normalized-pair-source-gravity-pincer-20260831/CANONICAL_MAIN_AUTHORITY_MANIFEST.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block34-normalized-pair-source-gravity-pincer-20260831/POSTEXECUTION_EXPECTED_TERMINAL.txt",
    ".claude/science/physics-loops/toe-source-eta-ownership-block34-normalized-pair-source-gravity-pincer-20260831/POSTEXECUTION_NO_GO_DISCIPLINE_CHECKLIST.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block34-normalized-pair-source-gravity-pincer-20260831/POSTEXECUTION_STATE.yaml",
    ".claude/science/physics-loops/toe-source-eta-ownership-block34-normalized-pair-source-gravity-pincer-20260831/INDEPENDENT_STATIC_ATTACK_FINAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block34-normalized-pair-source-gravity-pincer-20260831/RUNNER_SOURCE_PIN.md",
)

R = sp.Rational
LAMBDA = sp.symbols("lambda", real=True)
LAMBDA_0 = sp.symbols("lambda_0", real=True)
FRONT = sp.Matrix((1, 0, 0))
LATERAL = (
    sp.Matrix((0, -1, 0)),
    sp.Matrix((0, 1, 0)),
    sp.Matrix((0, 0, -1)),
    sp.Matrix((0, 0, 1)),
)
P_FRONT = sp.eye(3) - FRONT * FRONT.T
OUTCOME_PAIRS = tuple(itertools.product(range(4), repeat=2))

TERMINAL = (
    "ACTUAL-BLOCK32-LATERAL-PAIR-TENSOR-IS-LAMBDA-OVER-TWO-TIMES-"
    "FRONT-TRANSVERSE-PROJECTOR;BARE-GENERIC-MOMENTUM-WARD-FAILS-WHILE-"
    "OPEN-PR-6269-CONDITIONAL-NONZERO-FREQUENCY-FOUR-STRESS-COMPLETION-"
    "RETAINS-THE-FULL-AMPLITUDE-RAY;HOMOGENEOUS-LINEAR-RESPONSE-AND-"
    "COUNT-ONCE-BOOKKEEPING-DEBIT-DO-NOT-SELECT-A-POSITIVE-AMPLITUDE;"
    "FIXED-Q0-EQUALITY-OFF-UNIT-SCORE-EQUAL-VARIANCE-SELF-COMPARISON-HAS-"
    "LOCUS-ZERO-OR-TWO-THIRDS-BUT-IS-REFERENCE-DEPENDENT-AND-NOT-A-"
    "PHYSICAL-FISHER-ACTION-OR-SOURCE-UNIT;INSPECTED-CANONICAL-FOUNDATION-"
    "SUPPLIES-NO-PHYSICAL-RECORD-SOURCE-IDENTITY-REFERENCE-UNIT-OR-"
    "COUPLING;LOCAL-LATTICE-FOUR-STRESS-CADENCE-ZERO-MODE-AND-PHYSICAL-"
    "SOURCE-LAW-REMAIN-UNSUPPLIED-SO-PHYSICAL-LOCUS-INCOMPLETE"
)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


PIN_KEYS = (
    "source_sha256",
    "reviewed_logic_sha256",
    "independent_attack_sha256",
    "declared_input_count",
    "canonical_cache",
    "state",
)


def source_pin_values(mutation: str | None = None) -> dict[str, str]:
    if not RUNNER_SOURCE_PIN.is_file():
        return {}
    values: dict[str, str] = {}
    for line in RUNNER_SOURCE_PIN.read_text(encoding="utf-8").splitlines():
        match = re.fullmatch(r"([a-z0-9_]+):\s+`?([^`]+)`?", line)
        if not match:
            continue
        key, value = match.groups()
        if key not in PIN_KEYS or key in values:
            return {}
        values[key] = value
    if mutation == "duplicate_pin_key" or mutation == "unknown_pin_key":
        return {}
    replacements = {
        "source_pin_source_hash": ("source_sha256", "0" * 64),
        "source_pin_reviewed_logic_hash": ("reviewed_logic_sha256", "0" * 64),
        "source_pin_attack_hash": ("independent_attack_sha256", "0" * 64),
        "source_pin_input_count": ("declared_input_count", "0"),
        "source_pin_cache": ("canonical_cache", "wrong-cache"),
        "source_pin_state": ("state", "unreviewed"),
    }
    if mutation in replacements:
        key, value = replacements[mutation]
        values[key] = value
    return values


def normalized_review_logic_sha256(mutation: str | None = None) -> str | None:
    source = Path(__file__).read_bytes()
    pattern = re.compile(
        rb'(?m)^STATIC_ATTACK_SHA256 = "(?:PENDING|[0-9a-f]{64})"$'
    )
    matches = tuple(pattern.finditer(source))
    if len(matches) != 1:
        return None
    normalized = pattern.sub(b'STATIC_ATTACK_SHA256 = "PENDING"', source)
    if mutation == "post_review_byte_change":
        normalized += b"\n# hostile post-review byte\n"
    return hashlib.sha256(normalized).hexdigest()


def runner_source_pin_ok(mutation: str | None = None) -> bool:
    values = source_pin_values(mutation)
    expected_cache = (
        "logs/runner-cache/"
        "admissibility_d4_normalized_record_pair_source_gravity_pincer_"
        "gate_2026_08_31.txt"
    )
    return (
        tuple(values) == PIN_KEYS
        and values.get("source_sha256") == file_sha256(Path(__file__))
        and values.get("reviewed_logic_sha256")
        == normalized_review_logic_sha256(mutation)
        and values.get("independent_attack_sha256") == STATIC_ATTACK_SHA256
        and values.get("declared_input_count") == str(len(AUDIT_INPUT_PATHS))
        and values.get("canonical_cache") == expected_cache
        and values.get("state") == "final_packet_content_pinned_reproduced"
    )


@lru_cache(maxsize=None)
def canonical_main_bytes(path: str) -> bytes | None:
    if path not in CANONICAL_AUTHORITY:
        return None
    object_name = f"{CANONICAL_MAIN_COMMIT}:{path}"
    try:
        blob = subprocess.run(
            ("git", "rev-parse", object_name),
            cwd=ROOT,
            check=True,
            capture_output=True,
            timeout=10,
        ).stdout.decode("ascii").strip()
        body = subprocess.run(
            ("git", "cat-file", "blob", object_name),
            cwd=ROOT,
            check=True,
            capture_output=True,
            timeout=10,
        ).stdout
    except (OSError, subprocess.SubprocessError, UnicodeDecodeError):
        return None
    expected_blob, expected_sha256 = CANONICAL_AUTHORITY[path]
    if blob != expected_blob or hashlib.sha256(body).hexdigest() != expected_sha256:
        return None
    return body


def frozen_hashes_ok(mutation: str | None = None) -> bool:
    direct = dict(DIRECT_HASHES)
    frozen = dict(FROZEN)
    attack = STATIC_ATTACK_SHA256
    if mutation and mutation.startswith("direct_"):
        index = int(mutation.split("_", 1)[1]) - 1
        key = tuple(direct)[index]
        direct[key] = ("0" if direct[key][0] != "0" else "1") + direct[key][1:]
    if mutation and mutation.startswith("frozen_"):
        index = int(mutation.split("_", 1)[1]) - 1
        key = tuple(frozen)[index]
        frozen[key] = ("0" if frozen[key][0] != "0" else "1") + frozen[key][1:]
    if mutation == "attack_digest":
        attack = "0" * 64
    pin_mutations = {
        "source_pin_source_hash",
        "source_pin_reviewed_logic_hash",
        "source_pin_attack_hash",
        "source_pin_input_count",
        "source_pin_cache",
        "source_pin_state",
        "duplicate_pin_key",
        "unknown_pin_key",
        "post_review_byte_change",
    }
    direct_paths = tuple(direct)
    frozen_paths = tuple(f"{PACKET_REL}/{name}" for name in frozen)
    expected_paths = direct_paths + frozen_paths + (
        f"{PACKET_REL}/INDEPENDENT_STATIC_ATTACK_FINAL.md",
        f"{PACKET_REL}/RUNNER_SOURCE_PIN.md",
    )
    return (
        STATIC_ATTACK_SHA256 != "PENDING"
        and AUDIT_INPUT_PATHS == expected_paths
        and all(
            (ROOT / name).is_file()
            and file_sha256(ROOT / name) == digest
            for name, digest in direct.items()
        )
        and all(
            (PACKET / name).is_file()
            and file_sha256(PACKET / name) == digest
            for name, digest in frozen.items()
        )
        and STATIC_ATTACK.is_file()
        and file_sha256(STATIC_ATTACK) == attack
        and runner_source_pin_ok(mutation if mutation in pin_mutations else None)
    )


def input_fingerprint() -> str:
    digest = hashlib.sha256()
    digest.update(b"runner-cache-input-fingerprint-v1\0")
    for relative in AUDIT_INPUT_PATHS:
        path = ROOT / relative
        body = path.read_bytes() if path.exists() else b"MISSING"
        encoded = relative.encode("utf-8")
        digest.update(len(encoded).to_bytes(8, "big"))
        digest.update(encoded)
        digest.update(len(body).to_bytes(8, "big"))
        digest.update(body)
    return digest.hexdigest()


def q_table(mutation: str | None = None) -> dict[tuple[int, int], sp.Expr]:
    diagonal = (1 + 3 * LAMBDA) / 16
    off_diagonal = (1 - LAMBDA) / 16
    if mutation == "bad_diagonal_weight":
        diagonal = (1 + 2 * LAMBDA) / 16
    if mutation == "bad_off_diagonal_weight":
        off_diagonal = (1 - 2 * LAMBDA) / 16
    table = {
        (g, h): diagonal if g == h else off_diagonal
        for g, h in OUTCOME_PAIRS
    }
    if mutation == "omit_outcome":
        del table[(0, 1)]
    if mutation == "break_marginal":
        table[(0, 0)] += LAMBDA / 32
        table[(1, 1)] -= LAMBDA / 32
    return table


def sum_matrix(terms, rows: int = 3, cols: int = 3) -> sp.Matrix:
    return sum(terms, sp.zeros(rows, cols))


def proper_cubic_rotations() -> tuple[sp.Matrix, ...]:
    rotations = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = sp.zeros(3)
            for row, column in enumerate(permutation):
                matrix[row, column] = signs[row]
            if matrix.det() == 1:
                rotations.append(matrix)
    return tuple(rotations)


def actual_vectors(mutation: str | None = None) -> tuple[sp.Matrix, ...]:
    if mutation != "tetrahedral_surrogate":
        return LATERAL
    root = sp.sqrt(3)
    return tuple(
        sp.Matrix(corner) / root
        for corner in ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))
    )


def geometry_certificate(mutation: str | None = None) -> bool:
    table = q_table(mutation)
    vectors = actual_vectors(mutation)
    if len(table) != 16:
        return False
    total = sp.factor(sum(table.values()))
    left = tuple(sp.factor(sum(table[g, h] for h in range(4))) for g in range(4))
    right = tuple(sp.factor(sum(table[g, h] for g in range(4))) for h in range(4))
    mean_g = sum_matrix(
        (table[g, h] * vectors[g] for g, h in table), 3, 1
    )
    mean_h = sum_matrix(
        (table[g, h] * vectors[h] for g, h in table), 3, 1
    )
    egg = sum_matrix(table[g, h] * vectors[g] * vectors[g].T for g, h in table)
    ehh = sum_matrix(table[g, h] * vectors[h] * vectors[h].T for g, h in table)
    pair = sum_matrix(table[g, h] * vectors[g] * vectors[h].T for g, h in table)
    expected_pair = LAMBDA * P_FRONT / 2
    if mutation == "bad_pair_scale":
        expected_pair = LAMBDA * P_FRONT / 3
    claimed_trace = LAMBDA if mutation != "bad_trace" else 2 * LAMBDA
    k0, k1, k2 = sp.symbols("k0 k1 k2", real=True)
    momentum = sp.Matrix((k0, k1, k2))
    expected_residual = LAMBDA * (
        momentum - (momentum.dot(FRONT)) * FRONT
    ).T / 2
    claimed_residual = momentum.T * pair
    if mutation == "claim_generic_transverse":
        claimed_residual = sp.zeros(1, 3)
    covariance = True
    for rotation in proper_cubic_rotations():
        front = rotation * FRONT
        rotated = tuple(rotation * vector for vector in vectors)
        rotated_pair = sum_matrix(
            table[g, h] * rotated[g] * rotated[h].T for g, h in table
        )
        covariance = covariance and rotated_pair == sp.simplify(
            LAMBDA * (sp.eye(3) - front * front.T) / 2
        )
    return bool(
        total == 1
        and left == (R(1, 4),) * 4
        and right == (R(1, 4),) * 4
        and all(table[g, h] == table[h, g] for g, h in table)
        and mean_g == sp.zeros(3, 1)
        and mean_h == sp.zeros(3, 1)
        and egg == P_FRONT / 2
        and ehh == P_FRONT / 2
        and pair == expected_pair
        and sp.trace(pair) == claimed_trace
        and FRONT.T * pair == sp.zeros(1, 3)
        and sp.simplify(sp.trace(pair.T * pair) - LAMBDA**2 / 2) == 0
        and sp.simplify(claimed_residual - expected_residual) == sp.zeros(1, 3)
        and len(proper_cubic_rotations()) == 24
        and covariance
    )


def homogeneous_ray_certificate(mutation: str | None = None) -> bool:
    shape = P_FRONT / 2
    tensor = LAMBDA * shape
    coefficients = sp.symbols("ell0:9", real=True)
    base_residual = sum(
        coefficients[3 * i + j] * shape[i, j]
        for i in range(3)
        for j in range(3)
    )
    residual = sum(
        coefficients[3 * i + j] * tensor[i, j]
        for i in range(3)
        for j in range(3)
    )
    if mutation == "make_homogeneous_inhomogeneous":
        residual += 1
    trace_roots = set(sp.solve(sp.Eq(sp.trace(tensor), 0), LAMBDA))
    claimed_trace_roots = trace_roots
    if mutation == "claim_positive_homogeneous_selector":
        claimed_trace_roots = {R(2, 3)}
    if mutation == "drop_zero_only_branch":
        claimed_trace_roots = set()
    gamma, amplitude, scale = sp.symbols(
        "gamma amplitude scale", nonzero=True, real=True
    )
    response = gamma * amplitude * shape
    rescaled_response = (gamma / scale) * (amplitude * scale) * shape
    if mutation == "separate_free_coupling":
        rescaled_response += shape
    normalized = sp.simplify(tensor / sp.trace(tensor))
    claimed_normalized = normalized
    if mutation == "claim_trace_normalization_keeps_lambda":
        claimed_normalized = normalized + LAMBDA * shape
    return bool(
        sp.factor(residual - LAMBDA * base_residual) == 0
        and FRONT.T * tensor == sp.zeros(1, 3)
        and claimed_trace_roots == {0}
        and response == rescaled_response
        and claimed_normalized == shape
        and sp.trace(shape) == 1
    )


def parent_debit_counts(mutation: str | None = None) -> tuple[int, int, int, int] | None:
    parent_source = (
        ROOT
        / "scripts/admissibility_d4_symbolic_lambda_guarded_state_carrier_"
        "successor_gate_2026_08_31.py"
    ).read_text(encoding="utf-8")
    parent_note = (
        ROOT
        / "docs/ADMISSIBILITY_D4_SYMBOLIC_LAMBDA_GUARDED_FINITE_SUCCESSOR_"
        "TRANSACTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md"
    ).read_text(encoding="utf-8")
    patterns = (
        r"len\(locked\) == (\d+)",
        r"len\(initial_blank\) == (\d+)",
        r"len\(first\.locked_centers\) == (\d+)",
        r"len\(first\.blank_centers\) == (\d+)",
    )
    values = []
    for pattern in patterns:
        matches = {int(value) for value in re.findall(pattern, parent_source)}
        if len(matches) != 1:
            return None
        values.append(matches.pop())
    if not re.search(
        r"two source Blocks Locked and 158 other\s+Blocks Blank.*?"
        r"consume\s+exactly twelve distinct Blanks.*?"
        r"final ledger is 14 Locked plus 146\s+Blank",
        parent_note,
        flags=re.DOTALL,
    ):
        return None
    if mutation == "parent_debit_count_drift":
        values[-1] += 1
    return tuple(values)


def debit_recoil_certificate(mutation: str | None = None) -> bool:
    counts = parent_debit_counts(mutation)
    if counts is None:
        return False
    locked_before, blank_before, locked_after, blank_after = counts
    debit_count = blank_before - blank_after
    table = q_table()
    unordered_probability = sp.S.Zero
    unordered_tensor = sp.zeros(3)
    double_counted_tensor = sp.zeros(3)
    declared_opposite_bookkeeping_ok = True
    for g in range(4):
        for h in range(g, 4):
            probability = table[g, h] if g == h else 2 * table[g, h]
            dyad = (
                LATERAL[g] * LATERAL[g].T
                if g == h
                else (
                    LATERAL[g] * LATERAL[h].T
                    + LATERAL[h] * LATERAL[g].T
                ) / 2
            )
            unordered_probability += probability
            unordered_tensor += probability * dyad
            double_counted_tensor += (
                (2 if g != h else 1) * probability * dyad
            )
            declared_opposite_bookkeeping_ok = (
                declared_opposite_bookkeeping_ok
                and dyad + (-dyad) == sp.zeros(3)
            )
    if mutation == "double_count_pair":
        unordered_tensor = double_counted_tensor
    alpha = sp.symbols("alpha", real=True)
    conversion = alpha
    if mutation == "lambda_dependent_debit_conversion":
        conversion = alpha * LAMBDA
    source = conversion * (LAMBDA * P_FRONT / 2)
    declared_opposite = -source
    if mutation == "missing_recoil":
        declared_opposite = sp.zeros(3)
    kappa = sp.symbols("kappa", real=True)
    locus = sp.solve(sp.Eq(LAMBDA, kappa * debit_count), LAMBDA)
    samples = (sp.S.Zero, R(1, 5), R(2, 3), R(9, 10))
    conversions = tuple(sp.simplify(value / debit_count) for value in samples)
    return bool(
        debit_count == locked_after - locked_before
        and debit_count > 0
        and sp.factor(unordered_probability) == 1
        and unordered_tensor == LAMBDA * P_FRONT / 2
        and double_counted_tensor == (5 * LAMBDA - 1) * P_FRONT / 8
        and declared_opposite_bookkeeping_ok
        and sp.simplify(source + declared_opposite) == sp.zeros(3)
        and sp.diff(conversion, LAMBDA) == 0
        and locus == [debit_count * kappa]
        and all(sp.simplify(debit_count * coefficient - value) == 0
                for value, coefficient in zip(samples, conversions))
    )


@dataclass(frozen=True)
class WardCompletionResult:
    contractions_zero: bool
    ray_scaling: bool
    provenance: str
    authority_class: str
    nonzero_frequency_only: bool
    local_lattice_four_stress: bool
    cadence_supplied: bool
    zero_mode_supplied: bool


def ward_completion_result(mutation: str | None = None) -> WardCompletionResult:
    omega = sp.symbols("omega", nonzero=True, real=True)
    p0, p1, p2 = sp.symbols("p0 p1 p2", real=True)
    momentum = sp.Matrix((p0, p1, p2))
    spatial = LAMBDA * P_FRONT / 2
    mixed = spatial * momentum / omega
    temporal = (momentum.T * spatial * momentum)[0] / omega**2
    if mutation == "bad_ward_completion_sign":
        mixed = -mixed
    if mutation == "drop_time_completion":
        temporal = sp.S.Zero
    spatial_ward = sp.simplify(-omega * mixed.T + momentum.T * spatial)
    temporal_ward = sp.simplify(-omega * temporal + (momentum.T * mixed)[0])
    completed_entries = tuple(mixed) + (temporal,)
    ray_scaling = all(
        sp.simplify(entry - LAMBDA * sp.diff(entry, LAMBDA)) == 0
        for entry in completed_entries
    )
    result = WardCompletionResult(
        contractions_zero=bool(
            spatial_ward == sp.zeros(1, 3) and temporal_ward == 0
        ),
        ray_scaling=bool(ray_scaling),
        provenance="#6269@eb0ea608",
        authority_class="open_pr_conditional",
        nonzero_frequency_only=True,
        local_lattice_four_stress=False,
        cadence_supplied=False,
        zero_mode_supplied=False,
    )
    replacements = {
        "bad_ward_provenance": {"provenance": "landed-authority"},
        "promote_open_pr_authority": {"authority_class": "retained"},
        "promote_omega_zero_completion": {"zero_mode_supplied": True},
        "promote_local_lattice_four_stress": {"local_lattice_four_stress": True},
        "promote_cadence": {"cadence_supplied": True},
    }
    if mutation in replacements:
        result = replace(result, **replacements[mutation])
    return result


def ward_completion_certificate(mutation: str | None = None) -> bool:
    result = ward_completion_result(mutation)
    return bool(
        result.contractions_zero
        and result.ray_scaling
        and result.provenance == "#6269@eb0ea608"
        and result.authority_class == "open_pr_conditional"
        and result.nonzero_frequency_only
        and not result.local_lattice_four_stress
        and not result.cadence_supplied
        and not result.zero_mode_supplied
    )


def equality_off_contrast_values(
    mutation: str | None = None,
) -> tuple[sp.Expr, sp.Expr]:
    diagonal_symbol, off_symbol = sp.symbols("a b", real=True)
    solutions = sp.solve(
        (
            sp.Eq(diagonal_symbol + 3 * off_symbol, 0),
            sp.Eq(diagonal_symbol**2 + 3 * off_symbol**2, 4),
        ),
        (diagonal_symbol, off_symbol),
        dict=True,
    )
    positive = tuple(
        (solution[diagonal_symbol], solution[off_symbol])
        for solution in solutions
        if solution[diagonal_symbol].is_positive
    )
    if len(positive) != 1:
        raise AssertionError("equality/off q0-unit grammar did not have one positive orientation")
    diagonal, off_diagonal = positive[0]
    if mutation == "bad_contrast_values":
        diagonal = sp.S(2)
    return diagonal, off_diagonal


def physical_orbit(pair: tuple[int, int]) -> str:
    g, h = pair
    if g == h:
        return "same"
    if LATERAL[g].dot(LATERAL[h]) == -1:
        return "opposite"
    return "perpendicular"


def fixed_reference_score_certificate(mutation: str | None = None) -> bool:
    diagonal_count = 4
    off_count = 12
    if mutation == "bad_orbit_counts":
        off_count = 11
    diagonal, off_diagonal = equality_off_contrast_values(mutation)
    uniform_mean = sp.simplify(
        (diagonal_count * diagonal + off_count * off_diagonal) / 16
    )
    uniform_second = sp.simplify(
        (diagonal_count * diagonal**2 + off_count * off_diagonal**2) / 16
    )
    if mutation == "bad_uniform_mean_claim":
        uniform_mean += 1
    if mutation == "bad_uniform_variance_claim":
        uniform_second += 1
    table = q_table()
    values = {
        pair: diagonal if pair[0] == pair[1] else off_diagonal
        for pair in OUTCOME_PAIRS
    }
    mean = sp.factor(sum(table[pair] * values[pair] for pair in OUTCOME_PAIRS))
    second = sp.factor(
        sum(table[pair] * values[pair] ** 2 for pair in OUTCOME_PAIRS)
    )
    variance = sp.factor(second - mean**2)
    expected_mean = sp.sqrt(3) * LAMBDA
    expected_second = 1 + 2 * LAMBDA
    expected_variance = (1 - LAMBDA) * (1 + 3 * LAMBDA)
    if mutation == "bad_contrast_mean":
        expected_mean += LAMBDA
    if mutation == "bad_contrast_second":
        expected_second += LAMBDA
    if mutation == "bad_contrast_variance":
        expected_variance += LAMBDA
    roots = set(sp.solve(sp.Eq(variance, 1), LAMBDA))
    claimed_roots = roots
    if mutation == "drop_recurrence_root":
        claimed_roots = {R(2, 3)}
    nonzero_roots = {root for root in roots if root != 0}
    if mutation == "erase_zero_without_condition":
        nonzero_roots = roots
    reference_factor = sp.factor(
        ((1 - LAMBDA) * (1 + 3 * LAMBDA))
        - ((1 - LAMBDA_0) * (1 + 3 * LAMBDA_0))
    )
    expected_reference = sp.factor(
        (LAMBDA - LAMBDA_0) * (2 - 3 * (LAMBDA + LAMBDA_0))
    )
    if mutation == "hide_reference_root":
        expected_reference = LAMBDA - LAMBDA_0
    score = {
        pair: sp.factor(sp.diff(table[pair], LAMBDA) / table[pair])
        for pair in OUTCOME_PAIRS
    }
    expected_score = {
        pair: sp.factor(
            sp.sqrt(3) * (values[pair] - expected_mean) / expected_variance
        )
        for pair in OUTCOME_PAIRS
    }
    score_formula = all(
        sp.simplify(score[pair] - expected_score[pair]) == 0
        for pair in OUTCOME_PAIRS
    )
    score_at_q0 = all(
        sp.simplify(
            score[pair].subs(LAMBDA, 0) - sp.sqrt(3) * values[pair]
        ) == 0
        for pair in OUTCOME_PAIRS
    )
    fisher_information = sp.factor(
        sum(table[pair] * score[pair] ** 2 for pair in OUTCOME_PAIRS)
    )
    orbit_counts = {
        orbit: sum(physical_orbit(pair) == orbit for pair in OUTCOME_PAIRS)
        for orbit in ("same", "opposite", "perpendicular")
    }
    nuisance = {
        "same": sp.sqrt(2),
        "opposite": -sp.sqrt(2),
        "perpendicular": sp.S.Zero,
    }
    nuisance_mean = sp.simplify(
        sum(orbit_counts[orbit] * nuisance[orbit] for orbit in orbit_counts) / 16
    )
    nuisance_second = sp.simplify(
        sum(
            orbit_counts[orbit] * nuisance[orbit] ** 2
            for orbit in orbit_counts
        )
        / 16
    )
    diagonal_probability = sp.factor(
        sum(table[pair] for pair in OUTCOME_PAIRS if pair[0] == pair[1])
    )
    complement_control = (
        diagonal_probability.subs(LAMBDA, 0) == R(1, 4)
        and diagonal_probability.subs(LAMBDA, R(2, 3)) == R(3, 4)
    )
    fixed_q0_scale = sp.S.One
    if mutation == "lambda_dependent_reference":
        fixed_q0_scale = 1 / sp.sqrt(variance)
    if mutation == "hide_actual_d4_nuisance":
        nuisance_second += 1
    if mutation == "misstate_fisher_information":
        fisher_information += 1
    return bool(
        diagonal_count == 4
        and off_count == 12
        and uniform_mean == 0
        and uniform_second == 1
        and diagonal > 0
        and sp.simplify(diagonal + 3 * off_diagonal) == 0
        and mean == expected_mean
        and second == expected_second
        and sp.simplify(variance - expected_variance) == 0
        and claimed_roots == {0, R(2, 3)}
        and nonzero_roots == {R(2, 3)}
        and reference_factor == expected_reference
        and score_formula
        and score_at_q0
        and sp.simplify(fisher_information - 3 / expected_variance) == 0
        and orbit_counts == {"same": 4, "opposite": 4, "perpendicular": 8}
        and nuisance_mean == 0
        and nuisance_second == 1
        and nuisance["same"] != diagonal
        and complement_control
        and sp.diff(fixed_q0_scale, LAMBDA) == 0
    )


def absolute_normalizer_certificate(mutation: str | None = None) -> bool:
    target = sp.symbols("N", positive=True)
    radius = sp.symbols("R_source", positive=True)
    trace_locus = sp.solve(sp.Eq(LAMBDA, target), LAMBDA)
    norm_locus = sp.solve(sp.Eq(LAMBDA**2 / 2, radius**2), LAMBDA)
    positive_norm_locus = [root for root in norm_locus if root.could_extract_minus_sign() is False]
    trace_free = sp.solve(sp.Eq(LAMBDA, 0), LAMBDA)
    if mutation == "fit_absolute_target":
        target = LAMBDA
    return bool(
        trace_locus == [target]
        and set(norm_locus) == {-sp.sqrt(2) * radius, sp.sqrt(2) * radius}
        and positive_norm_locus == [sp.sqrt(2) * radius]
        and trace_free == [0]
        and sp.diff(target, LAMBDA) == 0
    )


@dataclass(frozen=True)
class AuthorityResult:
    canonical_manifest_valid: bool
    full_foundation_registry_scanned: bool
    foundation_source_identity_supplied: bool
    foundation_absolute_reference_unit_supplied: bool
    foundation_source_coupling_supplied: bool
    foundation_privileged_measure_supplied: bool
    foundation_nonzero_source_principle_supplied: bool
    closest_precedents_conditional_unaudited: bool


def canonical_manifest_valid(mutation: str | None = None) -> bool:
    path = PACKET / "CANONICAL_MAIN_AUTHORITY_MANIFEST.md"
    if not path.is_file():
        return False
    text = path.read_text(encoding="utf-8")
    commit = CANONICAL_MAIN_COMMIT
    if mutation == "canonical_commit_drift":
        commit = "0" * 40
    expected_rows = {
        f"| `{name}` | `{blob}` | `{digest}` |"
        for name, (blob, digest) in CANONICAL_AUTHORITY.items()
    }
    actual_rows = {
        line for line in text.splitlines() if line.startswith("| `docs/")
    }
    state = (PACKET / "STATE.yaml").read_text(encoding="utf-8")
    state_match = re.search(r"^canonical_main_checked:\s+([0-9a-f]{40})$", state, re.M)
    return bool(
        f"canonical_main_commit: `{commit}`" in text
        and f"declared_path_count: `{len(CANONICAL_AUTHORITY)}`" in text
        and actual_rows == expected_rows
        and state_match
        and state_match.group(1) == commit
    )


def authority_result(mutation: str | None = None) -> AuthorityResult:
    bodies = {name: canonical_main_bytes(name) for name in CANONICAL_AUTHORITY}
    if any(body is None for body in bodies.values()):
        return AuthorityResult(False, False, True, True, True, True, True, False)

    def text(name: str) -> str:
        body = bodies[name]
        assert body is not None
        return body.decode("utf-8")

    registry_path = "docs/audit/data/axiom_premise_nodes.json"
    registry = json.loads(text(registry_path))
    canonical_ids = tuple(registry.get("canonical_ids", ()))
    expected_ids = (
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    )
    expected_paths = {
        claim_id: registry["nodes"][claim_id]["current_path"]
        for claim_id in expected_ids
    }
    full_scan = bool(
        canonical_ids == expected_ids
        and expected_paths
        == {
            "minimal_axioms": "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "scale_reference_primitive": "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
            "kinetic_isotropy_primitive": "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
            "realized_state_primitive": "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
        }
        and all(path in bodies for path in expected_paths.values())
    )
    if mutation == "omit_primitive_doc":
        full_scan = False

    def compact(body: str) -> str:
        return re.sub(r"\s+", " ", body)
    minimal = compact(text(expected_paths["minimal_axioms"]))
    scale = compact(text(expected_paths["scale_reference_primitive"]))
    kinetic = compact(text(expected_paths["kinetic_isotropy_primitive"]))
    realized = compact(text(expected_paths["realized_state_primitive"]))
    foundation_negative = bool(
        "source/action and physical-observable identification" in minimal
        and "no mass ratio, coupling, mixing angle, phase, selector" in scale
        and "no mass ratio, coupling, mixing angle, phase, selector" in kinetic
        and "no state, averaging over alternatives, measure" in realized
        and "normalization rule" in realized
    )

    ledger_paths = (
        "docs/audit/data/ledger/pl/planck_source_unit_normalization_support_"
        "theorem_note_2026-04-25.json",
        "docs/audit/data/ledger/i1/i1_native_quadratic_static_source_"
        "normalization_bridge_2026-06-08.json",
        "docs/audit/data/ledger/so/source_measure_planck_action_rn_source_unit_"
        "bridge_note_2026-05-30.json",
    )
    ledgers = tuple(json.loads(text(path)) for path in ledger_paths)
    planck = compact(text(
        "docs/PLANCK_SOURCE_UNIT_NORMALIZATION_SUPPORT_THEOREM_NOTE_2026-04-25.md"
    ))
    quadratic = compact(text(
        "docs/I1_NATIVE_QUADRATIC_STATIC_SOURCE_NORMALIZATION_BRIDGE_2026-06-08.md"
    ))
    fisher = compact(text(
        "docs/SOURCE_MEASURE_PLANCK_ACTION_RN_SOURCE_UNIT_BRIDGE_NOTE_2026-05-30.md"
    ))
    precedents_conditional = bool(
        all(row.get("audit_status") == "unaudited" for row in ledgers)
        and all(row.get("effective_status") == "unaudited" for row in ledgers)
        and "supplied conditional carrier premise" in planck
        and "does not derive the physical source-coupling normalization" in quadratic
        and "normalization also remains an explicit premise" in quadratic
        and "conditional on that source-action normalization" in fisher
    )
    result = AuthorityResult(
        canonical_manifest_valid=canonical_manifest_valid(mutation),
        full_foundation_registry_scanned=full_scan,
        foundation_source_identity_supplied=not foundation_negative,
        foundation_absolute_reference_unit_supplied=not foundation_negative,
        foundation_source_coupling_supplied=not foundation_negative,
        foundation_privileged_measure_supplied=not foundation_negative,
        foundation_nonzero_source_principle_supplied=not foundation_negative,
        closest_precedents_conditional_unaudited=precedents_conditional,
    )
    replacements = {
        "supply_foundation_source_identity": {"foundation_source_identity_supplied": True},
        "supply_foundation_reference_unit": {"foundation_absolute_reference_unit_supplied": True},
        "supply_foundation_coupling": {"foundation_source_coupling_supplied": True},
        "supply_foundation_reference_measure": {"foundation_privileged_measure_supplied": True},
        "supply_nonzero_source_principle": {"foundation_nonzero_source_principle_supplied": True},
        "authorize_conditional_notes": {"closest_precedents_conditional_unaudited": False},
    }
    if mutation in replacements:
        result = replace(result, **replacements[mutation])
    return result


def authority_certificate(mutation: str | None = None) -> bool:
    result = authority_result(mutation)
    return bool(
        result.canonical_manifest_valid
        and result.full_foundation_registry_scanned
        and not result.foundation_source_identity_supplied
        and not result.foundation_absolute_reference_unit_supplied
        and not result.foundation_source_coupling_supplied
        and not result.foundation_privileged_measure_supplied
        and not result.foundation_nonzero_source_principle_supplied
        and result.closest_precedents_conditional_unaudited
    )


@dataclass(frozen=True)
class NegativeScope:
    physical_record_source_identity: bool
    physical_local_lattice_four_stress: bool
    physical_momentum_front_identification: bool
    record_source_cadence: bool
    zero_mode_completion: bool
    physical_source_coupling: bool
    blank_to_source_unit_conversion: bool
    physical_action_unit_identification: bool
    privileged_reference_measure: bool
    nonzero_source_principle: bool
    nonlinear_gravity_response: bool
    autonomous_source_renewal: bool
    physical_gravity_law: bool
    nature_lambda_selected: bool
    axiom_change: bool
    approved_primitive_change: bool
    audit_verdict: bool
    retained_claim: bool
    obligation_retirement: bool
    toe_score_movement: bool


def packet_state_values() -> dict[str, str]:
    values = {}
    for line in (PACKET / "POSTEXECUTION_STATE.yaml").read_text(
        encoding="utf-8"
    ).splitlines():
        if re.fullmatch(r"[a-z_]+:\s+[^#]+", line):
            key, value = line.split(":", 1)
            values[key] = value.strip()
    return values


def derived_negative_scope() -> NegativeScope:
    authority = authority_result()
    ward = ward_completion_result()
    p0, p1, p2 = sp.symbols("scope_p0 scope_p1 scope_p2", real=True)
    momentum = sp.Matrix((p0, p1, p2))
    bare_generic_ward = bool(
        sp.simplify(momentum.T * (LAMBDA * P_FRONT / 2)) == sp.zeros(1, 3)
    )
    conversion = sp.symbols("unfixed_blank_conversion", real=True)
    physical_blank_conversion = len(conversion.free_symbols) == 0
    parent_note = (
        ROOT
        / "docs/ADMISSIBILITY_D4_CLASSICAL_SCREENING_CAUSE_PERSISTENCE_"
        "RENEWAL_LOCUS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md"
    ).read_text(encoding="utf-8")
    parent_withholds_renewal = bool(
        "autonomous cadence" in parent_note and "is constructed" in parent_note
    )
    state = packet_state_values()
    physical_gravity = bool(
        authority.foundation_source_identity_supplied
        and authority.foundation_source_coupling_supplied
        and ward.local_lattice_four_stress
        and ward.cadence_supplied
        and ward.zero_mode_supplied
    )
    return NegativeScope(
        physical_record_source_identity=authority.foundation_source_identity_supplied,
        physical_local_lattice_four_stress=ward.local_lattice_four_stress,
        physical_momentum_front_identification=bare_generic_ward,
        record_source_cadence=ward.cadence_supplied,
        zero_mode_completion=ward.zero_mode_supplied,
        physical_source_coupling=authority.foundation_source_coupling_supplied,
        blank_to_source_unit_conversion=physical_blank_conversion,
        physical_action_unit_identification=authority.foundation_absolute_reference_unit_supplied,
        privileged_reference_measure=authority.foundation_privileged_measure_supplied,
        nonzero_source_principle=authority.foundation_nonzero_source_principle_supplied,
        nonlinear_gravity_response=ward.authority_class == "retained_nonlinear",
        autonomous_source_renewal=not parent_withholds_renewal,
        physical_gravity_law=physical_gravity,
        nature_lambda_selected=bool(
            physical_gravity and authority.foundation_absolute_reference_unit_supplied
        ),
        axiom_change=state.get("axiom_change_claimed") == "true",
        approved_primitive_change=(
            state.get("approved_primitive_change_claimed") == "true"
        ),
        audit_verdict=state.get("audit_verdict_claimed") == "true",
        retained_claim=state.get("retained_claim") == "true",
        obligation_retirement=state.get("obligation_retired") == "true",
        toe_score_movement=state.get("toe_score_movement") == "true",
    )


def render_terminal(scope: NegativeScope, promotion: str | None = None) -> str:
    terminal = TERMINAL
    true_fields = tuple(
        field.name for field in fields(scope) if getattr(scope, field.name)
    )
    if true_fields:
        terminal += f";DERIVED-{true_fields[0].upper().replace('_', '-')}"
    if promotion:
        terminal += f";DERIVED-{promotion.upper().replace('_', '-')}"
    return terminal


def static_scope_certificate(
    model_mutation: str | None = None,
    terminal_mutation: str | None = None,
) -> bool:
    scope = derived_negative_scope()
    if model_mutation:
        scope = replace(scope, **{model_mutation: True})
    terminal = render_terminal(scope, terminal_mutation)
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    literal_paths = None
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS":
                    literal_paths = ast.literal_eval(node.value)
    normalized_source = re.sub(r"\s+", " ", source)
    phrase_ok = (
        "No physical lambda selection, gravity law, axiom change, audit verdict, "
        "obligation retirement, or TOE-score movement is claimed."
        in normalized_source
    )
    expected_terminal = (
        EXPECTED_TERMINAL_PATH.read_text(encoding="utf-8").strip()
        if EXPECTED_TERMINAL_PATH.is_file()
        else ""
    )
    print_functions = {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and any(
            isinstance(call, ast.Call)
            and isinstance(call.func, ast.Name)
            and call.func.id == "print"
            for call in ast.walk(node)
        )
    }
    return bool(
        literal_paths == AUDIT_INPUT_PATHS
        and len(fields(scope)) == 20
        and all(getattr(scope, field.name) is False for field in fields(scope))
        and terminal == expected_terminal
        and phrase_ok
        and print_functions == {"emit_resolution_lines", "main"}
        and "UNSUPPLIED-SO-PHYSICAL-LOCUS-INCOMPLETE" in TERMINAL
        and "LOCUS-ZERO-OR-TWO-THIRDS" in TERMINAL
    )


SCIENCE_MUTATIONS = (
    "bad_diagonal_weight",
    "bad_off_diagonal_weight",
    "omit_outcome",
    "tetrahedral_surrogate",
    "break_marginal",
    "bad_pair_scale",
    "bad_trace",
    "claim_generic_transverse",
    "make_homogeneous_inhomogeneous",
    "claim_positive_homogeneous_selector",
    "drop_zero_only_branch",
    "separate_free_coupling",
    "claim_trace_normalization_keeps_lambda",
    "double_count_pair",
    "parent_debit_count_drift",
    "lambda_dependent_debit_conversion",
    "missing_recoil",
    "bad_orbit_counts",
    "bad_contrast_values",
    "bad_uniform_mean_claim",
    "bad_uniform_variance_claim",
    "bad_contrast_mean",
    "bad_contrast_second",
    "bad_contrast_variance",
    "drop_recurrence_root",
    "erase_zero_without_condition",
    "hide_reference_root",
    "lambda_dependent_reference",
    "hide_actual_d4_nuisance",
    "misstate_fisher_information",
    "fit_absolute_target",
    "canonical_commit_drift",
    "omit_primitive_doc",
    "supply_foundation_source_identity",
    "supply_foundation_reference_unit",
    "supply_foundation_coupling",
    "supply_foundation_reference_measure",
    "supply_nonzero_source_principle",
    "authorize_conditional_notes",
    "bad_ward_completion_sign",
    "drop_time_completion",
    "bad_ward_provenance",
    "promote_open_pr_authority",
    "promote_omega_zero_completion",
    "promote_local_lattice_four_stress",
    "promote_cadence",
)


def science_certificate(mutation: str | None = None) -> bool:
    return all(
        (
            geometry_certificate(mutation),
            homogeneous_ray_certificate(mutation),
            debit_recoil_certificate(mutation),
            ward_completion_certificate(mutation),
            fixed_reference_score_certificate(mutation),
            absolute_normalizer_certificate(mutation),
            authority_certificate(mutation),
        )
    )


def designated_mutations_certificate() -> tuple[bool, dict[str, int]]:
    identity_mutations = (
        tuple(f"direct_{index + 1}" for index in range(len(DIRECT_HASHES)))
        + tuple(f"frozen_{index + 1}" for index in range(len(FROZEN)))
        + (
            "attack_digest",
            "source_pin_source_hash",
            "source_pin_reviewed_logic_hash",
            "source_pin_attack_hash",
            "source_pin_input_count",
            "source_pin_cache",
            "source_pin_state",
            "duplicate_pin_key",
            "unknown_pin_key",
            "post_review_byte_change",
        )
    )
    identity_rejected = sum(
        not frozen_hashes_ok(mutation) for mutation in identity_mutations
    )
    science_rejected = sum(
        not science_certificate(mutation) for mutation in SCIENCE_MUTATIONS
    )
    scope_names = tuple(field.name for field in fields(NegativeScope))
    scope_model_rejected = sum(
        not static_scope_certificate(model_mutation=name) for name in scope_names
    )
    scope_terminal_rejected = sum(
        not static_scope_certificate(terminal_mutation=name) for name in scope_names
    )
    counts = {
        "identity_rejected": identity_rejected,
        "identity_total": len(identity_mutations),
        "science_rejected": science_rejected,
        "science_total": len(SCIENCE_MUTATIONS),
        "scope_model_rejected": scope_model_rejected,
        "scope_model_total": len(scope_names),
        "scope_terminal_rejected": scope_terminal_rejected,
        "scope_terminal_total": len(scope_names),
    }
    return bool(
        identity_rejected == len(identity_mutations)
        and science_rejected == len(SCIENCE_MUTATIONS)
        and scope_model_rejected == len(scope_names)
        and scope_terminal_rejected == len(scope_names)
    ), counts


def emit_resolution_lines(executed: bool) -> None:
    if not executed:
        print(
            "per_element: checked and not executed — content identity failed before the 16 pair weights or source moments were evaluated"
        )
        print(
            "per_site: checked and not executed — no returned-pair carrier or count-once debit was evaluated after identity failure"
        )
        print(
            "per_mode: checked and not executed — no front-aligned or generic momentum contraction was evaluated after identity failure"
        )
        print(
            "per_block: checked and not executed — no Block32 pair-source or fixed-q0 score self-comparison was evaluated after identity failure"
        )
        print(
            "lattice_wide: checked and not executed — no physical source law, cadence, zero mode, gravity response, or autonomous history was constructed"
        )
        return
    print(
        "per_element: checked — all 16 q_lambda weights, both marginals, actual D4 orbit counts, fixed-q0 score values, family score, and Fisher information were evaluated exactly"
    )
    print(
        "per_site: checked — the actual fixed-front four-lateral-exit carrier and parent-derived 12-Blank count-once bookkeeping were evaluated; the opposite tensor is declared bookkeeping and no Blank-to-energy conversion was supplied"
    )
    print(
        "per_mode: checked — all 24 proper-cubic frames, front contraction, generic symbolic spatial momentum residual, homogeneous ray, and reference-normalization mode were evaluated"
    )
    print(
        "per_block: checked — the Block32 pair tensor was recomputed, Block33 was content-identity-pinned but not recomputed, and the homogeneous response plus fixed-q0 variance recurrence were composed exactly"
    )
    print(
        "lattice_wide: checked and not executed — the #6269 nonzero-frequency continuum completion stayed conditional; no physical local-lattice four-stress, cadence, zero-mode completion, nonlinear gravity, or autonomous source history was constructed"
    )


def main() -> int:
    passed = 0
    failed = 0

    identity_ok = frozen_hashes_ok()
    if not identity_ok:
        print("FAIL frozen_inputs_and_source_pin: content identity mismatch")
        failed += 1
        emit_resolution_lines(False)
        print(f"TOTAL: PASS={passed} FAIL={failed}")
        return 1

    print(
        "PASS frozen_inputs_and_source_pin: "
        f"{len(AUDIT_INPUT_PATHS)} literal inputs; fingerprint={input_fingerprint()}"
    )
    passed += 1

    checks = (
        (
            "block32_q_law_and_actual_lateral_geometry",
            geometry_certificate(),
            "16 weights, uniform marginals, actual four lateral exits, all 24 proper-cubic frames",
        ),
        (
            "pair_tensor_front_and_generic_momentum_boundary",
            geometry_certificate(),
            "C=lambda(I-ff^T)/2; trace=lambda; front contraction zero; generic momentum residual retained",
        ),
        (
            "homogeneous_constraint_ray_dichotomy",
            homogeneous_ray_certificate(),
            "allowed unit shape retains the full ray; forbidden unit shape leaves only lambda=0",
        ),
        (
            "free_coupling_and_normalized_shape_degeneracy",
            homogeneous_ray_certificate(),
            "linear response sees coupling*lambda; C/trace(C) erases every positive amplitude",
        ),
        (
            "count_once_debit_recoil_and_conversion_boundary",
            debit_recoil_certificate(),
            "ten unordered pair events reproduce C once; 12 Blank changes balance algebraically; physical conversion remains free",
        ),
        (
            "conditional_nonzero_frequency_ward_completion",
            ward_completion_certificate(),
            "#6269@eb0ea608 time components complete arbitrary spatial momentum at nonzero frequency; authority remains open-PR conditional and every component scales with lambda",
        ),
        (
            "q0_unit_equality_off_score_and_actual_d4_nuisance",
            fixed_reference_score_certificate(),
            "O=(4 delta_gh-1)/sqrt(3) is unique only in the equality/off grammar; actual same/opposite/perpendicular D4 grammar has a distinct unit nuisance",
        ),
        (
            "fixed_q0_score_equal_variance_recurrence",
            fixed_reference_score_certificate(),
            "Var_q(O)=(1-lambda)(1+3lambda) returns to its q0 value at {0,2/3}; this is not a physical Fisher/action/source unit",
        ),
        (
            "arbitrary_reference_normalization_control",
            fixed_reference_score_certificate(),
            "equal fixed-score variance factors as (lambda-lambda0)(2-3lambda-3lambda0); q0's second root is a Bernoulli complement mirror",
        ),
        (
            "inhomogeneous_absolute_normalizer_boundary",
            absolute_normalizer_certificate(),
            "fixed trace or norm can select only after a lambda-independent nonzero target is supplied",
        ),
        (
            "canonical_main_foundation_and_conditional_precedents",
            authority_certificate(),
            "all four registry nodes were read at pinned canonical main; none supplies this source/measure/unit/coupling, and three closest named precedents remain unaudited and conditional",
        ),
        (
            "static_negative_scope_and_exact_terminal",
            static_scope_certificate(),
            "20 physical/governance promotions remain false and the conditional/incomplete terminal is exact",
        ),
    )
    for name, ok, detail in checks:
        if ok:
            print(f"PASS {name}: {detail}")
            passed += 1
        else:
            print(f"FAIL {name}: {detail}")
            failed += 1

    mutations_ok, counts = designated_mutations_certificate()
    if mutations_ok:
        print(
            "PASS designated_hostile_mutations: "
            f"identity={counts['identity_rejected']}/{counts['identity_total']}; "
            f"science={counts['science_rejected']}/{counts['science_total']}; "
            f"scope-model={counts['scope_model_rejected']}/{counts['scope_model_total']}; "
            f"scope-terminal={counts['scope_terminal_rejected']}/{counts['scope_terminal_total']}"
        )
        passed += 1
    else:
        print(f"FAIL designated_hostile_mutations: {counts}")
        failed += 1

    emit_resolution_lines(True)
    if failed == 0:
        print(f"TERMINAL: {render_terminal(derived_negative_scope())}")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
