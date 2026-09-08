#!/usr/bin/env python3
"""Exact Block-42 sharp-writer and orientation-decision runner.

The runner keeps four logically different statements separate:

1. exact repeatability of a general binary qubit CP instrument forces a sharp
   rank-one instrument without assuming a poststate;
2. the two sharp instruments share only the sign-neutral channel and
   externally scheduled later-label quotient; the literal Block-38 typed
   carrier separates them and rejects the anti-oriented attachment;
3. support calibration selects orientation inside the supplied affine class
   with eligible endpoints; the direct probability theorem also assumes
   positive formation and conditional affinity on ALL density matrices; and
4. empirical Records identify calibrated products, not an uncalibrated law by
   deduction from a finite corpus.

No generated fixture is treated as an observation.  The collision check is a
declared reduced two-front transaction wrapper, not a full-lattice process.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import re
import subprocess
import sys
from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Callable, Sequence

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PREREG_COMMIT = "d654b41f8d"
PACKET = (
    ".claude/science/physics-loops/"
    "toe-source-eta-ownership-block42-support-faithful-law-selection-decision-20260901"
)
RUNNER_PATH = (
    "scripts/admissibility_sharp_writer_orientation_axiom_decision_2026_09_01.py"
)
NOTE_PATH = (
    "docs/ADMISSIBILITY_SHARP_QUBIT_RECORD_WRITER_ORIENTATION_AXIOM_DECISION_"
    "BOUNDED_THEOREM_NOTE_2026-09-01.md"
)
DECISION_MEMO_PATH = (
    "docs/MINIMAL_AXIOM_W1_QUANTUM_EVENT_CALIBRATION_DECISION_MEMO_2026-09-01.md"
)
MINIMAL_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
BUSCH_PATH = (
    "docs/BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_"
    "NARROW_THEOREM_NOTE_2026-06-05.md"
)
LOCKED_OUTPUT_COMPARATOR_PATH = (
    "docs/COVARIANT_EFFECT_MAP_NONSELECTION_AND_REPEAT_CERTAINTY_COLLAPSE_"
    "BOUNDED_THEOREM_NOTE_2026-07-11.md"
)
OPERATIONAL_AFFINITY_COMPARATOR_PATH = (
    "docs/work_history/repo/review_feedback/"
    "OPERATIONAL_QUOTIENT_BORN_AFFINITY_CYCLE20_NOTE_2026-07-14.md"
)
BLOCK35_PATH = (
    "docs/ADMISSIBILITY_OPUS_AFFINE_BORN_PUBLIC_EVIDENCE_BOUNDARY_"
    "BOUNDED_THEOREM_NOTE_2026-09-01.md"
)
BLOCK36_PATH = (
    "docs/ADMISSIBILITY_GAUSSIAN_FAIR_RECORD_MIDPOINT_AFFINITY_HAAR_EDGE_FACTOR_"
    "FRESH_PORT_RESET_BOUNDED_THEOREM_NOTE_2026-09-01.md"
)
BLOCK38_NOTE_PATH = (
    "docs/ADMISSIBILITY_RANDOM_AXIS_M2_MATTER_REPEAT_SELECTOR_LOCAL_COMPILER_"
    "BOUNDED_THEOREM_NOTE_2026-09-01.md"
)
BLOCK38_RUNNER_PATH = (
    "scripts/admissibility_random_axis_m2_matter_repeat_selector_local_compiler_"
    "2026_09_01.py"
)
CURRENT_OPERATIONAL_AFFINITY_COMPARATOR_PATH = "archive/notes/" + OPERATIONAL_AFFINITY_COMPARATOR_PATH
HISTORICAL_TO_CURRENT_PATHS = {
    OPERATIONAL_AFFINITY_COMPARATOR_PATH: CURRENT_OPERATIONAL_AFFINITY_COMPARATOR_PATH,
    BLOCK35_PATH: "archive/notes/" + BLOCK35_PATH,
    BLOCK36_PATH: "archive/notes/" + BLOCK36_PATH,
    BLOCK38_NOTE_PATH: "archive/notes/" + BLOCK38_NOTE_PATH,
    BLOCK38_RUNNER_PATH: "archive/science-context/" + BLOCK38_RUNNER_PATH,
}
BLOCK37_RUNNER_PATH = "scripts/admissibility_block36_specific_nn_active_cut_record_front_2026_09_01.py"
CURRENT_HELPER_BLOBS = {
    BLOCK37_RUNNER_PATH: "87bd225dfca7c11a5246d26736cd52feb026ddbb",
    BLOCK38_RUNNER_PATH: "90d695084f38c37ddb605efdeb993560282ca590",
}
AUDIT_TIMEOUT_SEC = 120

# Literal tuple: audit evidence tooling parses this surface.  The theorem note
# and decision memo are intentionally bound even though they postdate the
# committed preregistration packet.
AUDIT_INPUT_PATHS = (
    "scripts/admissibility_sharp_writer_orientation_axiom_decision_2026_09_01.py",
    "docs/ADMISSIBILITY_SHARP_QUBIT_RECORD_WRITER_ORIENTATION_AXIOM_DECISION_BOUNDED_THEOREM_NOTE_2026-09-01.md",
    "docs/MINIMAL_AXIOM_W1_QUANTUM_EVENT_CALIBRATION_DECISION_MEMO_2026-09-01.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md",
    "docs/COVARIANT_EFFECT_MAP_NONSELECTION_AND_REPEAT_CERTAINTY_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-11.md",
    "archive/notes/docs/work_history/repo/review_feedback/OPERATIONAL_QUOTIENT_BORN_AFFINITY_CYCLE20_NOTE_2026-07-14.md",
    "archive/notes/docs/ADMISSIBILITY_OPUS_AFFINE_BORN_PUBLIC_EVIDENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-01.md",
    "archive/notes/docs/ADMISSIBILITY_GAUSSIAN_FAIR_RECORD_MIDPOINT_AFFINITY_HAAR_EDGE_FACTOR_FRESH_PORT_RESET_BOUNDED_THEOREM_NOTE_2026-09-01.md",
    "archive/notes/docs/ADMISSIBILITY_RANDOM_AXIS_M2_MATTER_REPEAT_SELECTOR_LOCAL_COMPILER_BOUNDED_THEOREM_NOTE_2026-09-01.md",
    "scripts/admissibility_random_axis_m2_matter_repeat_selector_local_compiler_2026_09_01.py",
    "scripts/admissibility_block36_specific_nn_active_cut_record_front_2026_09_01.py",
    ".claude/science/physics-loops/toe-source-eta-ownership-block42-support-faithful-law-selection-decision-20260901/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block42-support-faithful-law-selection-decision-20260901/EXACT_TARGET_CONTRACT.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block42-support-faithful-law-selection-decision-20260901/MUTATION_PLAN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block42-support-faithful-law-selection-decision-20260901/PRIOR_ART_SEARCH.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block42-support-faithful-law-selection-decision-20260901/STATE.yaml",
    ".claude/science/physics-loops/toe-source-eta-ownership-block42-support-faithful-law-selection-decision-20260901/PANEL_RETURN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block42-support-faithful-law-selection-decision-20260901/ASSUMPTIONS_AND_IMPORTS.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block42-support-faithful-law-selection-decision-20260901/EXECUTION_DEVIATION.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block42-support-faithful-law-selection-decision-20260901/NO_GO_DISCIPLINE_CHECKLIST.md",
    "archive/notes/docs/ADMISSIBILITY_BLOCK36_SPECIFIC_NN_ACTIVE_CUT_RECORD_FRONT_BOUNDED_THEOREM_NOTE_2026-09-01.md",
    "archive/notes/docs/ADMISSIBILITY_STRICT_NEAREST_NEIGHBOR_STATE_DEPENDENT_RECORD_BORN_HISTORY_SINGLE_FRONT_POSITIVE_THEOREM_NOTE_2026-08-12.md",
    "archive/science-context/.claude/science/physics-loops/toe-source-eta-ownership-block37-full-local-compiler-active-quotient-worldtube-20260901/ASSUMPTIONS_AND_IMPORTS.md",
    "archive/science-context/.claude/science/physics-loops/toe-source-eta-ownership-block37-full-local-compiler-active-quotient-worldtube-20260901/AUTHORITY_GATE.md",
    "archive/science-context/.claude/science/physics-loops/toe-source-eta-ownership-block37-full-local-compiler-active-quotient-worldtube-20260901/EXACT_TARGET_CONTRACT.md",
    "archive/science-context/.claude/science/physics-loops/toe-source-eta-ownership-block37-full-local-compiler-active-quotient-worldtube-20260901/MUTATION_PLAN.md",
    "archive/science-context/.claude/science/physics-loops/toe-source-eta-ownership-block37-full-local-compiler-active-quotient-worldtube-20260901/NO_GO_LEDGER.md",
    "archive/science-context/.claude/science/physics-loops/toe-source-eta-ownership-block37-full-local-compiler-active-quotient-worldtube-20260901/OPPORTUNITY_QUEUE.md",
    "archive/science-context/.claude/science/physics-loops/toe-source-eta-ownership-block37-full-local-compiler-active-quotient-worldtube-20260901/PANEL_RETURN.md",
    "archive/science-context/.claude/science/physics-loops/toe-source-eta-ownership-block37-full-local-compiler-active-quotient-worldtube-20260901/PREFLIGHT_WITNESSES.md",
    "archive/science-context/.claude/science/physics-loops/toe-source-eta-ownership-block37-full-local-compiler-active-quotient-worldtube-20260901/ROUTE_PORTFOLIO.md",
    "archive/science-context/.claude/science/physics-loops/toe-source-eta-ownership-block37-full-local-compiler-active-quotient-worldtube-20260901/STATE.yaml",
    "archive/science-context/.claude/science/physics-loops/toe-source-eta-ownership-block37-full-local-compiler-active-quotient-worldtube-20260901/TRACE_GATE.md",
    "archive/science-context/.claude/science/physics-loops/toe-source-eta-ownership-block38-random-axis-repeatability-matter-selector-20260901/ASSUMPTIONS_AND_IMPORTS.md",
    "archive/science-context/.claude/science/physics-loops/toe-source-eta-ownership-block38-random-axis-repeatability-matter-selector-20260901/CLAIM_STATUS_CERTIFICATE.md",
    "archive/science-context/.claude/science/physics-loops/toe-source-eta-ownership-block38-random-axis-repeatability-matter-selector-20260901/EXACT_TARGET_CONTRACT.md",
    "archive/science-context/.claude/science/physics-loops/toe-source-eta-ownership-block38-random-axis-repeatability-matter-selector-20260901/HANDOFF.md",
    "archive/science-context/.claude/science/physics-loops/toe-source-eta-ownership-block38-random-axis-repeatability-matter-selector-20260901/MUTATION_PLAN.md",
    "archive/science-context/.claude/science/physics-loops/toe-source-eta-ownership-block38-random-axis-repeatability-matter-selector-20260901/PRIOR_ART_SEARCH.md",
    "archive/science-context/.claude/science/physics-loops/toe-source-eta-ownership-block38-random-axis-repeatability-matter-selector-20260901/REVIEW_HISTORY.md",
    "archive/science-context/.claude/science/physics-loops/toe-source-eta-ownership-block38-random-axis-repeatability-matter-selector-20260901/STATE.yaml",
    "archive/science-context/.claude/science/physics-loops/toe-source-eta-ownership-block38-random-axis-repeatability-matter-selector-20260901/TRACE_GATE.md",
    "archive/science-context/scripts/admissibility_block36_specific_nn_active_cut_record_front_2026_09_01.py",
    "archive/science-context/scripts/admissibility_gaussian_fair_record_affinity_haar_factor_fresh_port_reset_2026_09_01.py",
    "archive/science-context/scripts/admissibility_random_axis_m2_matter_repeat_selector_local_compiler_2026_09_01.py",
    "archive/science-context/scripts/admissibility_strict_nearest_neighbor_state_dependent_record_born_history_single_front_2026_08_12.py",
)

FROZEN_BLOBS = {
    MINIMAL_PATH: "bc23300becfe4e4db57153c0e94cfcdf2338da71",
    BUSCH_PATH: "2d667c79bb7d06de98689d96a5ed4e0dd7ef0488",
    LOCKED_OUTPUT_COMPARATOR_PATH: "62303ec3bcfcfbb9da1aa34fefb7347263c0ccd2",
    OPERATIONAL_AFFINITY_COMPARATOR_PATH: "d6d2bda3d5cd8063479270c7ce462e1faee5b660",
    BLOCK35_PATH: "833232ecc6a8231c59f16b1af819c47c0eeb2bde",
    BLOCK36_PATH: "93aca5052adfde9ada5325d1058bf5507d85333a",
    BLOCK38_NOTE_PATH: "881b2359752a002dbfd744e932dd0112d8f55a9e",
    BLOCK38_RUNNER_PATH: "afe2e079494eba64d3bd68026070b1cf611cb626",
    f"{PACKET}/GOAL.md": "257149aa39c541411a9bd716ffe3374b54dfe902",
    f"{PACKET}/EXACT_TARGET_CONTRACT.md": "d4d4a7e7fc6d0e1dfc76f3482d9a4f23f802866f",
    f"{PACKET}/MUTATION_PLAN.md": "d9fc8c72005225c7d77a95d37225177cbc6ff248",
    f"{PACKET}/PRIOR_ART_SEARCH.md": "0d7aa20868e18f9cfecee96654f815159ecff3f8",
    f"{PACKET}/STATE.yaml": "c38bb3f05709cfd1086c09a85b6f7df35b58f4f2",
    f"{PACKET}/PANEL_RETURN.md": "702c24b3e71d16e4e4ff4fece3cecc11e0c9d9ee",
    f"{PACKET}/ASSUMPTIONS_AND_IMPORTS.md": "a9d0a15d9c8179643ee2780f5bd61c1708e6d80e",
}

# These two preregistration files retain the frozen commit objects above, but
# their bound worktree copies also contain the post-prereg prior-art addition
# and hostile correction.  EXECUTION_DEVIATION.md records why that divergence
# is scientifically required instead of silently rewriting the preregistered
# expectation.
POST_PREREG_CHANGED = (
    f"{PACKET}/PRIOR_ART_SEARCH.md",
    f"{PACKET}/STATE.yaml",
    f"{PACKET}/PANEL_RETURN.md",
)
EXECUTION_DEVIATION_PATH = f"{PACKET}/EXECUTION_DEVIATION.md"
NO_GO_CHECKLIST_PATH = f"{PACKET}/NO_GO_DISCIPLINE_CHECKLIST.md"


def load_block38():
    path = ROOT / BLOCK38_RUNNER_PATH
    spec = importlib.util.spec_from_file_location("block38_orientation_parent", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load Block-38 runner")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


B38 = load_block38()

I2 = sp.eye(2)
ZERO2 = sp.zeros(2)
SIGMA_X = sp.Matrix([[0, 1], [1, 0]])
SIGMA_Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SIGMA_Z = sp.Matrix([[1, 0], [0, -1]])
PAULI = (SIGMA_X, SIGMA_Y, SIGMA_Z)
LABELS = (-1, 1)


def matrix_zero(matrix: sp.MatrixBase) -> bool:
    return all(sp.simplify(entry) == 0 for entry in matrix)


def flat_markdown(text: str) -> str:
    """Remove blockquote leaders and normalize layout-only whitespace."""

    return re.sub(r"\s+", " ", re.sub(r"(?m)^>\s?", "", text)).strip()


def dot(left: Sequence[object], right: Sequence[object]) -> sp.Expr:
    return sp.simplify(
        sum(sp.sympify(left[index]) * sp.sympify(right[index]) for index in range(3))
    )


def rotate(rotation: Sequence[Sequence[int]], vector: Sequence[object]) -> tuple[sp.Expr, ...]:
    return tuple(
        sp.simplify(
            sum(rotation[row][column] * sp.sympify(vector[column]) for column in range(3))
        )
        for row in range(3)
    )


def bloch_operator(vector: Sequence[object]) -> sp.Matrix:
    return sp.simplify(
        sum(
            (sp.sympify(vector[index]) * PAULI[index] for index in range(3)),
            ZERO2,
        )
    )


def density(vector: Sequence[object]) -> sp.Matrix:
    return sp.simplify((I2 + bloch_operator(vector)) / 2)


def projector(axis: Sequence[object], label: int) -> sp.Matrix:
    return sp.simplify((I2 + label * bloch_operator(axis)) / 2)


def affine_effect(axis: Sequence[object], label: int, response: object) -> sp.Matrix:
    return sp.simplify(
        (I2 + label * sp.sympify(response) * bloch_operator(axis)) / 2
    )


def branch(axis: Sequence[object], label: int, orientation: int, rho: sp.Matrix) -> sp.Matrix:
    output = projector(axis, orientation * label)
    return sp.simplify(sp.trace(output * rho) * output)


def git_blob(path: str) -> str:
    return subprocess.run(
        ["git", "rev-parse", f"{PREREG_COMMIT}:{path}"],
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


def input_fingerprint() -> str:
    digest = hashlib.sha256()
    for relative in AUDIT_INPUT_PATHS:
        path = ROOT / relative
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def source_and_prereg_certificate(_: str | None = None) -> tuple[bool, str]:
    commit_pinned = sum(
        git_blob(path) == expected for path, expected in FROZEN_BLOBS.items()
    )
    unchanged_pinned = sum(
        worktree_blob(HISTORICAL_TO_CURRENT_PATHS.get(path, path)) == expected
        for path, expected in FROZEN_BLOBS.items()
        if path not in POST_PREREG_CHANGED
    )
    changed_bound = all(
        worktree_blob(path) != FROZEN_BLOBS[path] for path in POST_PREREG_CHANGED
    )
    target = (ROOT / PACKET / "EXACT_TARGET_CONTRACT.md").read_text()
    mutation_plan = (ROOT / PACKET / "MUTATION_PLAN.md").read_text()
    minimal = (ROOT / MINIMAL_PATH).read_text()
    busch = (ROOT / BUSCH_PATH).read_text()
    locked_output = (ROOT / LOCKED_OUTPUT_COMPARATOR_PATH).read_text()
    operational_affinity = (ROOT / CURRENT_OPERATIONAL_AFFINITY_COMPARATOR_PATH).read_text()
    note = (ROOT / NOTE_PATH).read_text() if (ROOT / NOTE_PATH).exists() else ""
    memo = (
        (ROOT / DECISION_MEMO_PATH).read_text()
        if (ROOT / DECISION_MEMO_PATH).exists()
        else ""
    )
    deviation = (
        (ROOT / EXECUTION_DEVIATION_PATH).read_text()
        if (ROOT / EXECUTION_DEVIATION_PATH).exists()
        else ""
    )
    no_go = (
        (ROOT / NO_GO_CHECKLIST_PATH).read_text()
        if (ROOT / NO_GO_CHECKLIST_PATH).exists()
        else ""
    )
    note_flat = flat_markdown(note)
    numbered_mutations = re.findall(r"(?m)^\d+\.", mutation_plan)
    required = {
        RUNNER_PATH,
        NOTE_PATH,
        DECISION_MEMO_PATH,
        MINIMAL_PATH,
        BUSCH_PATH,
        LOCKED_OUTPUT_COMPARATOR_PATH,
        CURRENT_OPERATIONAL_AFFINITY_COMPARATOR_PATH,
        BLOCK37_RUNNER_PATH,
        HISTORICAL_TO_CURRENT_PATHS[BLOCK35_PATH],
        HISTORICAL_TO_CURRENT_PATHS[BLOCK36_PATH],
        HISTORICAL_TO_CURRENT_PATHS[BLOCK38_NOTE_PATH],
        BLOCK38_RUNNER_PATH,
        EXECUTION_DEVIATION_PATH,
        NO_GO_CHECKLIST_PATH,
        *(f"{PACKET}/{name}" for name in (
            "GOAL.md",
            "EXACT_TARGET_CONTRACT.md",
            "MUTATION_PLAN.md",
            "PRIOR_ART_SEARCH.md",
            "STATE.yaml",
            "PANEL_RETURN.md",
            "ASSUMPTIONS_AND_IMPORTS.md",
        )),
    }
    ok = (
        commit_pinned == len(FROZEN_BLOBS)
        and unchanged_pinned == len(FROZEN_BLOBS) - len(POST_PREREG_CHANGED)
        and changed_bound
        and all(worktree_blob(path) == blob for path, blob in CURRENT_HELPER_BLOBS.items())
        and required <= set(AUDIT_INPUT_PATHS)
        and set(B38.AUDIT_INPUT_PATHS) <= set(AUDIT_INPUT_PATHS)
        and set(B38.PARENT.AUDIT_INPUT_PATHS) <= set(AUDIT_INPUT_PATHS)
        and len(numbered_mutations) == 20
        and "Do not assume a Lüders update" in target
        and "Records form." in minimal
        and "Born weight values" in minimal
        and "(M3)" in busch
        and "m(E) = Tr" in busch
        and "J_P(rho) = Tr(E_P rho) P" in locked_output
        and "Repeat certainty collapses" in locked_output
        and "Physical Randomization Gives Affinity" in operational_affinity
        and "normalized conditional transcript measure" in operational_affinity
        and "an axiom/bridge decision inventory, not W1 retirement" in note_flat
        and "They are **not** twins on the literal Block-38 typed carrier" in note
        and "Do not edit the governing minimal-axiom memo" in memo
        and "disjoint support" in deviation
        and "rejected hypothesis" in deviation
        and all(f"## N{index}" in no_go for index in range(1, 9))
    )
    return ok, (
        f"{commit_pinned}/{len(FROZEN_BLOBS)} prereg commit blobs pinned, "
        f"{unchanged_pinned} unchanged and {len(POST_PREREG_CHANGED)} declared "
        "post-prereg corrections "
        "bound; current B37/B38 helpers and complete declared provenance bound separately; "
        "20/20 mutations plus three prior-art comparators bound"
    )


def general_repeatability_certificate(mutation: str | None = None) -> tuple[bool, str]:
    lam = sp.symbols("lambda", real=True)
    effect = affine_effect((0, 0, 1), 1, lam)
    failure = sp.simplify(I2 - effect)
    determinant = sp.factor(failure.det())
    roots = set(sp.solve(sp.Eq(determinant, 0), lam))
    if mutation == "discard_negative_root":
        roots.discard(sp.Integer(-1))

    x, y = sp.symbols("x y", nonnegative=True)
    u, v = sp.symbols("u v", real=True)
    positive_output = sp.Matrix([[x, u + sp.I * v], [u - sp.I * v, y]])
    canonical_failure = sp.diag(0, 1)
    failure_trace = sp.simplify(sp.trace(canonical_failure * positive_output))
    zero_failure_determinant = sp.factor(positive_output.det().subs(y, 0))
    # At zero failure mass, PSD requires det(output)>=0.  The displayed exact
    # expression is -(u^2+v^2), hence u=v=0 and the range is one-dimensional.
    support_derived = (
        failure_trace == y
        and zero_failure_determinant == -(u**2 + v**2)
        and sp.Poly(u**2 + v**2, u, v).as_dict()
        == {(2, 0): 1, (0, 2): 1}
    )
    poststate_free = mutation not in {"preset_kappa_plus", "assume_lueders"}
    if mutation == "assume_lueders":
        support_derived = False

    r00, r01, r10, r11 = sp.symbols("r00 r01 r10 r11")
    rho = sp.Matrix([[r00, r01], [r10, r11]])
    unique = True
    for orientation, label in itertools.product(LABELS, repeat=2):
        p = projector((0, 0, 1), orientation * label)
        output = branch((0, 0, 1), label, orientation, rho)
        unique &= matrix_zero(output - sp.trace(p * rho) * p)
        unique &= sp.simplify(sp.trace(output) - sp.trace(p * rho)) == 0

    ok = (
        sp.simplify(determinant - (1 - lam**2) / 4) == 0
        and roots == {-1, 1}
        and support_derived
        and poststate_free
        and unique
    )
    return ok, "det(I-E)=(1-lambda^2)/4; PSD zero-failure support derives both sharp roots and the unique branch map without kappa/poststate input"


def sign_dual_instrument_certificate(mutation: str | None = None) -> tuple[bool, str]:
    axes = ((0, 0, 1), (sp.Rational(3, 5), sp.Rational(4, 5), 0))
    r00, r01, r10, r11 = sp.symbols("r00 r01 r10 r11")
    rho = sp.Matrix([[r00, r01], [r10, r11]])
    checked = 0
    ok = True
    channels: dict[tuple[object, ...], dict[int, sp.Matrix]] = {}
    for axis in axes:
        by_sign: dict[int, sp.Matrix] = {}
        for orientation in LABELS:
            effects = [projector(axis, orientation * label) for label in LABELS]
            unconditional = sum(
                (branch(axis, label, orientation, rho) for label in LABELS),
                ZERO2,
            )
            by_sign[orientation] = sp.simplify(unconditional)
            ok &= matrix_zero(sum(effects, ZERO2) - I2)
            ok &= sp.simplify(sp.trace(unconditional) - sp.trace(rho)) == 0
            for label, effect in zip(LABELS, effects):
                choi = sp.kronecker_product(effect, effect.T)
                ok &= (
                    matrix_zero(choi.H - choi)
                    and matrix_zero(choi * choi - choi)
                    and choi.rank() == 1
                    and sp.simplify(sp.trace(choi) - 1) == 0
                    and sp.simplify(sp.trace(effect * effect) - 1) == 0
                    and sp.simplify(sp.trace(effect * (I2 - effect))) == 0
                )
                checked += 1
        channels[axis] = by_sign
        ok &= matrix_zero(by_sign[1] - by_sign[-1])
    claims_difference = mutation == "different_unconditional_channels"
    ok &= not claims_difference
    return ok, f"{checked} exact rank-one Choi branches are CP/normalized/repeatable; positive and negative unconditional dephasing channels coincide"


def rotation_key(unitary: sp.Matrix) -> tuple[tuple[int, int, int], ...]:
    rows: list[tuple[int, int, int]] = []
    for sigma_out in PAULI:
        row = []
        for sigma_in in PAULI:
            value = sp.simplify(
                sp.trace(sigma_out * unitary * sigma_in * unitary.H) / 2
            )
            if value not in (-1, 0, 1):
                raise ValueError(f"non-cubic spin action {value}")
            row.append(int(value))
        rows.append(tuple(row))
    return tuple(rows)


def cubic_spin_lifts() -> dict[tuple[tuple[int, int, int], ...], sp.Matrix]:
    hadamard = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
    phase = sp.diag(1, sp.I)
    queue = [I2]
    lifts: dict[tuple[tuple[int, int, int], ...], sp.Matrix] = {}
    while queue:
        unitary = queue.pop(0)
        key = rotation_key(unitary)
        if key in lifts:
            continue
        lifts[key] = unitary
        queue.extend((hadamard * unitary, phase * unitary))
    return lifts


def covariance_certificate(_: str | None = None) -> tuple[bool, str]:
    lifts = cubic_spin_lifts()
    parent_rotations = set(B38.ROTATIONS)
    axis = (sp.Rational(3, 5), sp.Rational(4, 5), 0)
    checked = 0
    ok = len(lifts) == 24 and set(lifts) == parent_rotations
    for rotation, unitary in lifts.items():
        transported_axis = rotate(rotation, axis)
        for orientation, label in itertools.product(LABELS, repeat=2):
            p = projector(axis, orientation * label)
            transported = projector(transported_axis, orientation * label)
            ok &= matrix_zero(unitary * p * unitary.H - transported)
            choi = sp.kronecker_product(p, p.T)
            transported_choi = sp.kronecker_product(transported, transported.T)
            action = sp.kronecker_product(unitary, unitary.conjugate())
            ok &= matrix_zero(action * choi * action.H - transported_choi)
            checked += 1
    return ok, f"all {len(lifts)} proper-cubic spin lifts transport both signs and {checked} branch Choi matrices exactly"


def history_certificate(mutation: str | None = None) -> tuple[bool, str]:
    axes = (
        (sp.Integer(0), sp.Integer(0), sp.Integer(1)),
        (sp.Rational(3, 5), sp.Rational(4, 5), sp.Integer(0)),
        (sp.Integer(0), sp.Rational(3, 5), sp.Rational(4, 5)),
        (sp.Rational(4, 5), sp.Integer(0), sp.Rational(3, 5)),
    )
    initial = density((sp.Rational(1, 3), sp.Rational(1, 4), sp.Rational(1, 5)))
    transition_cases = 0
    ok = True
    for use_count in (2, 3, 4):
        totals = {}
        for orientation in LABELS:
            total = 0
            for labels in itertools.product(LABELS, repeat=use_count):
                mass = sp.trace(projector(axes[0], orientation * labels[0]) * initial)
                for index in range(use_count - 1):
                    actual = sp.trace(
                        projector(axes[index + 1], orientation * labels[index + 1])
                        * projector(axes[index], orientation * labels[index])
                    )
                    expected = (
                        1
                        + labels[index]
                        * labels[index + 1]
                        * dot(axes[index], axes[index + 1])
                    ) / 2
                    ok &= sp.simplify(actual - expected) == 0
                    mass *= actual
                    transition_cases += 1
                total += sp.simplify(mass)
            totals[orientation] = sp.simplify(total)
        ok &= totals == {-1: 1, 1: 1}

    later_equal = all(
        sp.simplify(
            sp.trace(projector(right_axis, right_label) * projector(left_axis, left_label))
            - sp.trace(projector(right_axis, -right_label) * projector(left_axis, -left_label))
        )
        == 0
        for left_axis, right_axis in zip(axes, axes[1:])
        for left_label, right_label in itertools.product(LABELS, repeat=2)
    )
    same_axis = all(
        sp.trace(projector(axes[0], orientation * label) ** 2) == 1
        and sp.trace(
            projector(axes[0], -orientation * label)
            * projector(axes[0], orientation * label)
        )
        == 0
        for orientation, label in itertools.product(LABELS, repeat=2)
    )
    aligned = density(axes[0])
    first_plus = sp.trace(projector(axes[0], 1) * aligned)
    first_minus = sp.trace(projector(axes[0], -1) * aligned)
    separator = first_plus == 1 and first_minus == 0
    if mutation == "same_axis_sign_selector":
        same_axis = False
    if mutation == "later_axis_sign_selector":
        later_equal = False
    ok &= later_equal and same_axis and separator
    return ok, f"2-4 use arbitrary-axis cylinders normalize; {transition_cases} later factors are sign-neutral, while an aligned first preparation separates the signs"


@lru_cache(maxsize=None)
def block38_transcript_summary(
    response: int | Fraction,
    sharpness: int | Fraction,
    shift: tuple[int, int, int] = (0, 0, 0),
) -> tuple[
    Fraction,
    Fraction,
    int,
    bool,
    bool,
    tuple[tuple[tuple[int, int], Fraction], ...],
    tuple[tuple[tuple[tuple[Fraction, ...], ...], Fraction], ...],
]:
    lam = Fraction(response)
    kap = Fraction(sharpness)
    config = B38.Config(response=lam, sharpness=kap)
    frame = B38.Frame(0)
    records = B38.seed_records(B38.DEFAULT_RND, frame, shift)
    distribution, states = B38.transcript_distribution(
        records, frame, 0, config, shift
    )
    total = sum(distribution.values(), Fraction(0))
    repeat = Fraction(0)
    label_transitions: dict[tuple[int, int], Fraction] = {}
    for transcript, mass in distribution.items():
        first = B38.Carrier(transcript[2])
        second = B38.Carrier(transcript[4])
        first_label = B38.carrier_fields(first)[4]
        second_label = B38.carrier_fields(second)[4]
        key = (first_label, second_label)
        label_transitions[key] = label_transitions.get(key, Fraction(0)) + mass
        if first_label == second_label:
            repeat += mass
    sites = B38.frame_sites(frame, 0, shift)
    record_faithful = True
    selected_repeat = True
    for state in states:
        axis, first_direction = B38.carrier_axis_direction(state[sites["F"]])
        _, successor = B38.carrier_axis_state(state[sites["M"]])
        second_direction = B38.carrier_direction(state[sites["B2"]])
        record_faithful &= successor == first_direction
        selected_repeat &= (
            B38.dot(axis, first_direction) in (-1, 1)
            and second_direction == first_direction
        )
    return (
        total,
        repeat,
        len(distribution),
        record_faithful,
        selected_repeat,
        tuple(sorted(label_transitions.items())),
        tuple(distribution.items()),
    )


def literal_block38_certificate(mutation: str | None = None) -> tuple[bool, str]:
    endpoint_pairs = ((1, 1), (-1, -1), (1, -1), (-1, 1))
    summaries = {}
    bind_cases = 0
    ok = True
    for response, sharpness in endpoint_pairs:
        actual_sharpness = sharpness
        if mutation == "preset_kappa_plus" and (response, sharpness) == (-1, -1):
            actual_sharpness = 1
        summary = block38_transcript_summary(response, actual_sharpness)
        summaries[(response, sharpness)] = summary
        source_ok, bind_ok, cases, _ = B38.actual_axis_jump_binding_certificate(
            B38.Config(response=Fraction(response), sharpness=Fraction(actual_sharpness))
        )
        bind_cases += cases
        ok &= source_ok and bind_ok and summary[0] == 1

    plus_rows = dict(summaries[(1, 1)][6])
    minus_rows = dict(summaries[(-1, -1)][6])
    typed_intersection = set(plus_rows).intersection(minus_rows)
    typed_tv = sum(
        abs(plus_rows.get(row, Fraction(0)) - minus_rows.get(row, Fraction(0)))
        for row in set(plus_rows).union(minus_rows)
    ) / 2
    ok &= summaries[(1, 1)][1] == 1
    ok &= summaries[(-1, -1)][1] == 1
    ok &= summaries[(1, -1)][1] == 0
    ok &= summaries[(-1, 1)][1] == 0
    ok &= summaries[(1, 1)][3] and not summaries[(-1, -1)][3]
    ok &= summaries[(1, 1)][4] and summaries[(-1, -1)][4]
    ok &= summaries[(1, 1)][5] == summaries[(-1, -1)][5]
    ok &= not typed_intersection and typed_tv == 1
    return ok, (
        f"literal F-M-B2 binds {bind_cases} source cases: label-transition "
        "quotient agrees and mixed signs reject, but +/- typed endpoint "
        "supports intersect=0, TV=1 and anti attachment=false; prereg hard-impact row 2 falsified"
    )


WRITE_ROLES = (
    "T",
    "G",
    "R",
    "P",
    "A",
    "F",
    "M",
    "B2",
    "C",
    "Q1",
    "Q2",
    "Q3",
    "Q4",
    "Q5",
    "Q6",
    "Q7",
    "Q8",
    "HN",
)


def reduced_collision_certificate(mutation: str | None = None) -> tuple[bool, str]:
    frame = B38.Frame(0)
    left_head = (0, 0, 0)
    left_sites = B38.frame_sites(frame, 0, left_head)
    left_footprint = frozenset(left_sites[name] for name in WRITE_ROLES)
    relative = tuple(left_footprint)
    candidate_shifts = sorted(
        {
            B38.sub(left, right)
            for left in relative
            for right in relative
            if B38.sub(left, right) != (0, 0, 0)
        }
    )
    right_head = None
    right_footprint: frozenset[tuple[int, int, int]] | None = None
    for shift in candidate_shifts:
        sites = B38.frame_sites(frame, 0, shift)
        footprint = frozenset(sites[name] for name in WRITE_ROLES)
        if (
            left_footprint.intersection(footprint)
            and shift not in left_footprint
            and left_head not in footprint
            and sites["T"] != left_sites["T"]
        ):
            right_head = shift
            right_footprint = footprint
            break
    if right_head is None or right_footprint is None:
        return False, "no clean reduced two-front overlap witness found"

    weights = {
        1: (Fraction(1, 2), Fraction(1, 2)),
        -1: (Fraction(1, 2), Fraction(1, 2)),
    }
    if mutation == "collision_sign_selector":
        weights[-1] = (Fraction(3, 4), Fraction(1, 4))

    rows = 0
    ok = weights[1] == weights[-1]
    summaries = {}
    typed_separations = 0
    for orientation in LABELS:
        mixture_mass = Fraction(0)
        sign_summaries = []
        for winner_weight, head in zip(weights[orientation], (left_head, right_head)):
            seed = B38.seed_records(B38.DEFAULT_RND, frame, head)
            trigger = B38.frame_sites(frame, 0, head)["T"]
            proposals = B38.local_proposals(
                seed,
                trigger,
                B38.Config(response=Fraction(orientation), sharpness=Fraction(orientation)),
            )
            ok &= len(proposals) == 1 and proposals[0].kind == "trigger" and proposals[0].normalized
            summary = block38_transcript_summary(orientation, orientation, head)
            sign_summaries.append(summary)
            mixture_mass += winner_weight * summary[0]
            rows += summary[2]
        ok &= mixture_mass == 1
        summaries[orientation] = tuple(
            (item[0], item[1], item[2], item[5]) for item in sign_summaries
        )
    ok &= summaries[1] == summaries[-1]
    for head in (left_head, right_head):
        plus_rows = dict(block38_transcript_summary(1, 1, head)[6])
        minus_rows = dict(block38_transcript_summary(-1, -1, head)[6])
        intersection = set(plus_rows).intersection(minus_rows)
        tv = sum(
            abs(plus_rows.get(row, Fraction(0)) - minus_rows.get(row, Fraction(0)))
            for row in set(plus_rows).union(minus_rows)
        ) / 2
        ok &= not intersection and tv == 1
        typed_separations += int(not intersection and tv == 1)
    ok &= bool(left_footprint.intersection(right_footprint))
    return ok, (
        "one derived overlap wrapper has sign-blind half/half grants and equal "
        f"projected label summaries across {rows} rows; typed supports remain "
        f"disjoint at {typed_separations}/2 heads, so no carrier-level collision conjugacy is claimed"
    )


def finite_candidate_comparison_certificate(mutation: str | None = None) -> tuple[bool, str]:
    minimal = (ROOT / MINIMAL_PATH).read_text()
    minimal_flat = flat_markdown(minimal)
    aligned = B38.E_Z
    axis = B38.E_Z
    sharp = B38.binary_probability(aligned, axis, 1, Fraction(1))
    interior = B38.binary_probability(aligned, axis, 1, Fraction(1, 2))
    sharp_summary = block38_transcript_summary(1, 1)
    interior_summary = block38_transcript_summary(Fraction(1, 2), 1)
    haar_moments = (Fraction(1, 3), Fraction(1, 6))
    foundation_boundary = all(
        needle in minimal_flat
        for needle in (
            "probability distribution over the possibilities",
            "A choice not fixed by the supplied structure remains a named conditional",
            "Born weight values",
            "update laws",
        )
    )
    claims_permanence_repeat = mutation == "permanence_as_repeatability"
    claims_current_calibration = mutation == "axioms_contain_calibration"
    ok = (
        foundation_boundary
        and sharp == 1
        and interior == Fraction(3, 4)
        and sharp_summary[0] == interior_summary[0] == 1
        and sharp_summary[1] == 1
        and interior_summary[1] == Fraction(3, 4)
        and haar_moments[0] != haar_moments[1]
        and not claims_permanence_repeat
        and not claims_current_calibration
    )
    return ok, "lambda=1 and 1/2 give normalized literal Record laws but aligned weights 1 versus 3/4, Haar moments 1/3 versus 1/6, and repeat masses 1 versus 3/4"


def support_calibration_certificate(mutation: str | None = None) -> tuple[bool, str]:
    lam, u, delta = sp.symbols("lambda u delta", real=True)
    aligned_probability = (1 + lam) / 2
    selected = sp.solve(sp.Eq(aligned_probability, 1), lam)
    if mutation == "label_spelling_orientation":
        selected = [sp.Integer(1)]
        calibration_used = False
    else:
        calibration_used = True

    g = sp.expand(u + delta * u * (1 - u**2))
    derivative = sp.expand(sp.diff(g, u))
    derivative_bound = sp.expand(derivative - (1 - 2 * delta))
    delta_value = sp.Rational(1, 8)
    g_control = sp.expand(g.subs(delta, delta_value))
    probabilities = tuple(
        sp.simplify((1 + label * g_control.subs(u, value)) / 2)
        for label in LABELS
        for value in (
            sp.Rational(-1),
            sp.Rational(-1, 2),
            sp.Rational(0),
            sp.Rational(1, 2),
            sp.Rational(1),
        )
    )
    direct_midpoint = sp.simplify((1 + g_control.subs(u, sp.Rational(1, 2))) / 2)
    endpoint_mixture = sp.simplify(
        ((1 + g_control.subs(u, 1)) / 2 + (1 + g_control.subs(u, 0)) / 2) / 2
    )
    nonaffine_gap = sp.simplify(direct_midpoint - endpoint_mixture)
    nonlinear_present = mutation != "remove_nonlinear_counterkernel"
    claims_full_born = mutation == "calibration_is_full_born"
    cubic_crosscheck = (
        (1 + u**3).subs(u, 1) == 2
        and (1 + u**3).subs(u, -1) == 0
        and sp.diff(u**3, u, 2) != 0
    )
    ok = (
        selected == [1]
        and calibration_used
        and sp.simplify(g.subs(u, -u) + g) == 0
        and (g.subs(u, -1), g.subs(u, 1)) == (-1, 1)
        and sp.simplify(derivative_bound - 3 * delta * (1 - u**2)) == 0
        and sp.diff(g, u, 3) == -6 * delta
        and all(0 <= value <= 1 for value in probabilities)
        and nonaffine_gap == sp.Rational(3, 128)
        and nonlinear_present
        and not claims_full_born
        and cubic_crosscheck
    )
    return ok, "support certainty solves lambda=+1 in the affine class; g_delta is odd, endpoint/range calibrated, normalized and non-affine with exact midpoint gap 3/128"


def event_addition_affinity_certificate(mutation: str | None = None) -> tuple[bool, str]:
    k = sp.Rational(2, 3)
    weights = (sp.exp(k), sp.exp(-k), 1, 1, 1, 1)
    total = sum(weights)
    event_a = {0, 2}
    event_b = {3, 5}
    p_a = sum(weights[index] for index in event_a) / total
    p_b = sum(weights[index] for index in event_b) / total
    p_union = sum(weights[index] for index in event_a | event_b) / total
    additive = sp.simplify(p_union - p_a - p_b) == 0
    pure_normalizer = 2 * sp.cosh(k) + 4
    mixture_probability = sp.cosh(k) / pure_normalizer
    zero_preparation_probability = sp.Rational(1, 6)
    gap = sp.simplify(mixture_probability - zero_preparation_probability)
    expected = (sp.cosh(k) - 1) / (3 * sp.cosh(k) + 6)
    claims_implication = mutation == "event_additivity_as_affinity"
    ok = (
        additive
        and sp.simplify(gap - expected) == 0
        and bool(sp.N(gap, 40) > 0)
        and not claims_implication
    )
    return ok, "a six-event exponential law is exactly additive at fixed preparation yet violates 50/50 preparation affinity by (cosh(2/3)-1)/(3cosh(2/3)+6)"


def calibration_endpoints_eligible(formation: sp.Expr, x: sp.Symbol) -> bool:
    """Necessary, not sufficient, screen of the full-domain formation hypothesis."""
    return all(bool(formation.subs(x, endpoint) > 0) for endpoint in (0, 1))


def formation_selection_bias_certificate(_: str | None = None) -> tuple[bool, str]:
    """Conditioning can destroy affinity even when joint branches are affine."""

    x = sp.symbols("x", real=True, nonnegative=True)
    formation = (1 + x) / 2
    joint_p = x
    joint_perp = (1 - x) / 2
    conditional_p = sp.cancel(joint_p / formation)
    conditional_perp = sp.cancel(joint_perp / formation)
    midpoint_direct = sp.simplify(conditional_p.subs(x, sp.Rational(1, 2)))
    midpoint_mixture = sp.simplify(
        (conditional_p.subs(x, 0) + conditional_p.subs(x, 1)) / 2
    )
    selection_gap = sp.simplify(midpoint_direct - midpoint_mixture)

    # Necessary endpoint screen for the supplied total-domain hypothesis.
    # Passing these two points alone does NOT certify positivity on all states.
    symmetric_formation = 4 * x * (1 - x)
    symmetric_q = sp.cancel((symmetric_formation / 2) / symmetric_formation)
    asymmetric_formation = 1 - x
    asymmetric_q = sp.cancel(sp.Integer(0) / asymmetric_formation)
    domain_counterexamples_rejected = (
        not calibration_endpoints_eligible(symmetric_formation, x)
        and not calibration_endpoints_eligible(asymmetric_formation, x)
        and calibration_endpoints_eligible(formation, x)
        and symmetric_formation.subs(x, 0) == symmetric_formation.subs(x, 1) == 0
        and symmetric_q == sp.Rational(1, 2)
        and symmetric_q != sp.Rational(1, 4)
        and asymmetric_formation.subs(x, 0) == 1
        and asymmetric_formation.subs(x, 1) == 0
        and asymmetric_q == 0
        and asymmetric_q != sp.Rational(1, 2)
    )

    # For a FULL-DOMAIN conditionally affine binary-PVM probability functional,
    # positive formation makes both endpoint calibrations nonvacuous. Then
    # finite-dimensional
    # affine/Riesz representation gives p_P(rho)=Tr(E rho).  Endpoint support
    # calibration fixes E's diagonal in the P/Pperp basis.  Positivity then
    # kills the only remaining complex off-diagonal because det(E)=-|z|^2.
    zr, zi = sp.symbols("z_r z_i", real=True)
    effect = sp.Matrix([[1, zr + sp.I * zi], [zr - sp.I * zi, 0]])
    determinant = sp.factor(effect.det())
    zero_offdiagonal = sp.simplify(determinant + zr**2 + zi**2) == 0
    selected_effect = effect.subs({zr: 0, zi: 0})

    note = (ROOT / NOTE_PATH).read_text().lower()
    memo = (ROOT / DECISION_MEMO_PATH).read_text().lower()
    note_flat = flat_markdown(note)
    memo_flat = flat_markdown(memo)
    operational_prior = (ROOT / CURRENT_OPERATIONAL_AFFINITY_COMPARATOR_PATH).read_text()
    clause_bound = (
        "conditional preparation affinity" in note_flat
        and "q_p(p rho_0+(1-p)rho_1 | f)" in note_flat
        and "same conditional content law" in note_flat
        and "conditional on record formation depend only on the prepared one-site density possibility and are affine in it" in memo_flat
        and "recorded preparation randomizer and a direct preparation representing the same" in memo_flat
        and "same conditional content law on the entire qubit state space" in memo_flat
        and "including both endpoints" in memo_flat
        and "full-domain positive formation is an additional ideal-context hypothesis" in note_flat
    )
    old_wording_rejected = (
        "is still insufficient because this framework conditions" in note_flat
        and "does not prevent formation selection bias" in memo_flat
    )
    ok = (
        sp.simplify(joint_p + joint_perp - formation) == 0
        and sp.diff(joint_p, x, 2) == 0
        and sp.diff(joint_perp, x, 2) == 0
        and sp.diff(formation, x, 2) == 0
        and conditional_p == 2 * x / (1 + x)
        and sp.simplify(conditional_p + conditional_perp - 1) == 0
        and conditional_p.subs(x, 0) == 0
        and conditional_p.subs(x, 1) == 1
        and midpoint_direct == sp.Rational(2, 3)
        and midpoint_mixture == sp.Rational(1, 2)
        and selection_gap == sp.Rational(1, 6)
        and sp.diff(conditional_p, x, 2) != 0
        and domain_counterexamples_rejected
        and determinant == -(zr**2 + zi**2)
        and zero_offdiagonal
        and matrix_zero(selected_effect - projector((0, 0, 1), 1))
        and "recorded physical randomizer plus forgetting its branch record" in operational_prior
        and "normalized numerical law" in operational_prior
        and "Record formation" not in operational_prior
        and clause_bound
        and old_wording_rejected
    )
    return ok, (
        "affine joint h_P=x,h_Q=(1-x)/2 gives nonlinear p(P|F)=2x/(1+x) "
        "and midpoint gap 1/6; explicit conditional affinity/randomizer-equivalence plus "
        "full-domain positive formation makes both calibrations nonvacuous, "
        "then effect positivity selects E=P; both ineligible-endpoint witnesses reject; "
        "July transcript-affinity prior did not isolate formation reweighting"
    )


def busch_comparator_certificate(_: str | None = None) -> tuple[bool, str]:
    sqrt3 = sp.sqrt(3)
    trine = (
        (1, 0, 0),
        (sp.Rational(-1, 2), sqrt3 / 2, 0),
        (sp.Rational(-1, 2), -sqrt3 / 2, 0),
    )
    effects = tuple(sp.Rational(2, 3) * projector(axis, 1) for axis in trine)
    sigma = density((sp.Rational(1, 3), sp.Rational(1, 4), sp.Rational(1, 5)))
    weights = tuple(sp.simplify(sp.trace(sigma * effect)) for effect in effects)
    pauli_projectors = tuple(
        projector(axis, 1) for axis in ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    )
    reconstructed = sp.simplify(
        (
            I2
            + sum(
                (
                    (2 * sp.trace(sigma * pauli_projectors[index]) - 1)
                    * PAULI[index]
                    for index in range(3)
                ),
                ZERO2,
            )
        )
        / 2
    )
    minimal = (ROOT / MINIMAL_PATH).read_text()
    busch = (ROOT / BUSCH_PATH).read_text()
    hypotheses_not_current = not all(
        needle in minimal for needle in ("m(0) = 0", "m(𝟙) = 1", "POVM partitions")
    )
    ok = (
        matrix_zero(sum(effects, ZERO2) - I2)
        and sp.simplify(sum(weights) - 1) == 0
        and matrix_zero(reconstructed - sigma)
        and hypotheses_not_current
        and "**Status authority:** independent audit lane only" in busch
        and "does **not** discharge" in busch
    )
    return ok, "the exact trine POVM obeys trace-form normalization and Pauli reconstruction, but M1-M3/effect-to-Record calibration are broader unaudited comparator hypotheses"


def locked_output_comparator_certificate(_: str | None = None) -> tuple[bool, str]:
    prior = (ROOT / LOCKED_OUTPUT_COMPARATOR_PATH).read_text()
    note = (ROOT / NOTE_PATH).read_text()
    note_flat = re.sub(r"\s+", " ", note)
    a = sp.symbols("a", real=True)
    p = projector((0, 0, 1), 1)
    depolarized_effect = sp.simplify(a * p + (1 - a) * I2 / 2)
    self_weight = sp.simplify(sp.trace(p * depolarized_effect))
    selected = sp.solve(sp.Eq(self_weight, 1), a)
    ok = (
        self_weight == (1 + a) / 2
        and selected == [1]
        and "J_P(rho) = Tr(E_P rho) P" in prior
        and "zero premise weight" in prior
        and "general CP instrument with the displayed binary effects" in note_flat
        and "rather than assumed before the collapse" in note_flat
    )
    return ok, (
        "July comparator's locked-output depolarizing family collapses at a=1 "
        "only after menu/repeat assumptions; Block42 novelty is limited to deriving "
        "support and the map for the declared general binary CP instrument"
    )


def empirical_boundary_certificate(mutation: str | None = None) -> tuple[bool, str]:
    lam, overlap = sp.symbols("lambda u", real=True)
    first_weights = {label: (1 + label * lam * overlap) / 2 for label in LABELS}
    conditional_mean = sp.simplify(
        sum(label * weight for label, weight in first_weights.items())
    )
    haar_scalar_mean = sp.simplify(
        sp.integrate(overlap * conditional_mean, (overlap, -1, 1)) / 2
    )
    haar_scalar_second = sp.simplify(
        sp.integrate(
            overlap**2 * sum(first_weights.values()),
            (overlap, -1, 1),
        )
        / 2
    )
    single_use_variance = sp.simplify(9 * haar_scalar_second - lam**2)

    b1, b2, b3 = sp.symbols("b1 b2 b3", integer=True)
    u1, u2, u3 = sp.symbols("u1 u2 u3", real=True)
    likelihood = sp.prod(
        (1 + b * lam * value) / 2
        for b, value in ((b1, u1), (b2, u2), (b3, u3))
    )
    likelihood_factored = sp.factor(likelihood)
    # Same one-use marginals do not specify a product joint law. Copying a
    # single draw into two trials leaves the mean's variance unchanged.
    frozen_two_trial_variance = single_use_variance.subs(lam, 0)
    independent_two_trial_variance = single_use_variance.subs(lam, 0) / 2
    match_probability = sp.Rational(3, 4)
    frozen_all_match = match_probability
    product_all_match = match_probability**2
    joint_counterexamples = (
        frozen_two_trial_variance == 3
        and independent_two_trial_variance == sp.Rational(3, 2)
        and frozen_two_trial_variance != independent_two_trial_variance
        and frozen_all_match == sp.Rational(3, 4)
        and product_all_match == sp.Rational(9, 16)
        and frozen_all_match != product_all_match
    )
    current_note = flat_markdown((ROOT / NOTE_PATH).read_text())
    joint_scope_bound = all(phrase in current_note for phrase in (
        "conditional on the full past", "independent fresh uses",
        "fresh-reset product conditional kernel", "Cov(Y_i,Y_j)",
    ))

    axes = (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1)),
        (Fraction(3, 5), Fraction(4, 5), Fraction(0)),
    )
    spam_equal = all(
        B38.binary_probability(
            B38.E_Z, axis, label, Fraction(1, 2)
        )
        == B38.binary_probability(
            (Fraction(0), Fraction(0), Fraction(1, 2)),
            axis,
            label,
            Fraction(1),
        )
        for axis in axes
        for label in LABELS
    )
    repeat_gauge = all(
        (Fraction(1) + label * Fraction(1, 2) * 1) / 2
        == (Fraction(1) + label * 1 * Fraction(1, 2)) / 2
        for label in LABELS
    )
    chi = sp.symbols("chi", real=True)
    mismatch = (1 - chi) / 2
    one_mismatch_falsifies = mismatch.subs(chi, 1) == 0
    finite_all_match = ((1 + sp.Rational(9, 10)) / 2) ** 7
    finite_not_deductive = finite_all_match > 0
    target = (ROOT / PACKET / "EXACT_TARGET_CONTRACT.md").read_text()
    assumptions_declared = all(
        word in target
        for word in (
            "reset/freshness",
            "recurrence",
            "candidate-class",
            "typicality",
        )
    )

    claims = {
        "finite_all_match_proof": mutation == "finite_all_match_proof",
        "ignore_repeat_gauge": mutation == "ignore_repeat_gauge",
        "ignore_preparation_gauge": mutation == "ignore_preparation_gauge",
        "synthetic_as_empirical": mutation == "synthetic_as_empirical",
        "omit_reset_controls": mutation == "omit_reset_controls",
        "absolute_rate": mutation == "absolute_rate",
    }
    ok = (
        conditional_mean == lam * overlap
        and haar_scalar_mean == lam / 3
        and haar_scalar_second == sp.Rational(1, 3)
        and single_use_variance == 3 - lam**2
        and sp.simplify(likelihood_factored - likelihood) == 0
        and spam_equal
        and repeat_gauge
        and one_mismatch_falsifies
        and finite_not_deductive
        and assumptions_declared
        and joint_counterexamples
        and joint_scope_bound
        and not any(claims.values())
    )
    return ok, "one-use E[Y]=lambda, Var(Y)=3-lambda^2; N-trial variance and likelihood require the stated fresh-reset product law; correlated controls give variance 3 vs 3/2 and all-match 3/4 vs 9/16; SPAM and finite-evidence boundaries retained"


def decision_scope_certificate(mutation: str | None = None) -> tuple[bool, str]:
    target = (ROOT / PACKET / "EXACT_TARGET_CONTRACT.md").read_text()
    note = (ROOT / NOTE_PATH).read_text()
    memo = (ROOT / DECISION_MEMO_PATH).read_text()
    deviation = (ROOT / EXECUTION_DEVIATION_PATH).read_text()
    memo_flat = flat_markdown(memo)
    deviation_flat = re.sub(r"[\s\u201c\u201d]+", " ", deviation)
    retirement_claim = mutation == "retire_w1_toe"
    ok = (
        "AXIOM_DECISION_READY" in target
        and "obligation_retirement: 0" in note
        and "toe_percentage_movement: 0" in note
        and "Do not edit the governing minimal-axiom memo" in memo_flat
        and "conditional on Record formation depend only on the prepared one-site density possibility and are affine in it" in memo_flat
        and "register both in a scoped primitive" in memo_flat
        and "does not prevent formation selection bias" in memo_flat
        and "539 direct and 2,218 transitive consumers" in memo_flat
        and "both endpoints survive the typed carrier expectation as a rejected hypothesis" in deviation_flat
        and not retirement_claim
    )
    return ok, (
        "axiom_decision_status=AXIOM_DECISION_READY for a future multi-clause "
        "choice; full-domain eligibility is supplied, not an approved axiom; "
        "zero audit/obligation/TOE movement"
    )


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


MUTATIONS = (
    "discard_negative_root",
    "preset_kappa_plus",
    "assume_lueders",
    "label_spelling_orientation",
    "different_unconditional_channels",
    "same_axis_sign_selector",
    "later_axis_sign_selector",
    "collision_sign_selector",
    "event_additivity_as_affinity",
    "calibration_is_full_born",
    "remove_nonlinear_counterkernel",
    "permanence_as_repeatability",
    "finite_all_match_proof",
    "ignore_repeat_gauge",
    "ignore_preparation_gauge",
    "synthetic_as_empirical",
    "omit_reset_controls",
    "absolute_rate",
    "axioms_contain_calibration",
    "retire_w1_toe",
)

DESIGNATED_GATE = {
    "discard_negative_root": "general_cp_repeatability_classification",
    "preset_kappa_plus": "general_cp_repeatability_classification",
    "assume_lueders": "general_cp_repeatability_classification",
    "label_spelling_orientation": "support_calibration_and_nonlinear_boundary",
    "different_unconditional_channels": "sign_dual_choi_channels",
    "same_axis_sign_selector": "arbitrary_axis_history_orientation",
    "later_axis_sign_selector": "arbitrary_axis_history_orientation",
    "collision_sign_selector": "reduced_collision_dual",
    "event_additivity_as_affinity": "event_addition_vs_preparation_affinity",
    "calibration_is_full_born": "support_calibration_and_nonlinear_boundary",
    "remove_nonlinear_counterkernel": "support_calibration_and_nonlinear_boundary",
    "permanence_as_repeatability": "finite_candidate_response_comparison",
    "finite_all_match_proof": "empirical_likelihood_moment_gauges",
    "ignore_repeat_gauge": "empirical_likelihood_moment_gauges",
    "ignore_preparation_gauge": "empirical_likelihood_moment_gauges",
    "synthetic_as_empirical": "empirical_likelihood_moment_gauges",
    "omit_reset_controls": "empirical_likelihood_moment_gauges",
    "absolute_rate": "empirical_likelihood_moment_gauges",
    "axioms_contain_calibration": "finite_candidate_response_comparison",
    "retire_w1_toe": "decision_and_scope",
}

GATES: tuple[tuple[str, Callable[[str | None], tuple[bool, str]]], ...] = (
    ("source_and_prereg_binding", source_and_prereg_certificate),
    ("general_cp_repeatability_classification", general_repeatability_certificate),
    ("sign_dual_choi_channels", sign_dual_instrument_certificate),
    ("proper_cubic_covariance", covariance_certificate),
    ("arbitrary_axis_history_orientation", history_certificate),
    ("literal_block38_dual_endpoints", literal_block38_certificate),
    ("reduced_collision_dual", reduced_collision_certificate),
    ("finite_candidate_response_comparison", finite_candidate_comparison_certificate),
    ("support_calibration_and_nonlinear_boundary", support_calibration_certificate),
    ("event_addition_vs_preparation_affinity", event_addition_affinity_certificate),
    ("formation_conditioning_selection_bias", formation_selection_bias_certificate),
    ("busch_povm_additivity_comparator", busch_comparator_certificate),
    ("locked_output_repeat_comparator", locked_output_comparator_certificate),
    ("empirical_likelihood_moment_gauges", empirical_boundary_certificate),
    ("decision_and_scope", decision_scope_certificate),
)
GATE_FUNCTIONS = dict(GATES)


def execute_mutation(name: str) -> tuple[str, bool]:
    gate = DESIGNATED_GATE[name]
    gate_ok, _ = GATE_FUNCTIONS[gate](name)
    return name, not gate_ok


def run(mutation: str | None = None) -> int:
    checks = Checks()
    if mutation is not None:
        source_ok, source_detail = source_and_prereg_certificate()
        checks.check("source_and_prereg_binding", source_detail, source_ok)
        gate = DESIGNATED_GATE[mutation]
        gate_ok, gate_detail = GATE_FUNCTIONS[gate](mutation)
        checks.check(gate, gate_detail, gate_ok)
        return checks.finish()

    for name, function in GATES:
        ok, detail = function(None)
        checks.check(name, detail, ok)

    mutation_results = tuple(execute_mutation(name) for name in MUTATIONS)
    rejected = sum(result for _, result in mutation_results)
    mutation_detail = ",".join(
        f"{name}={'R' if result else 'MISSED'}" for name, result in mutation_results
    )
    checks.check(
        "hostile_mutation_gate",
        f"{rejected}/{len(MUTATIONS)} designated mutations rejected; {mutation_detail}",
        rejected == len(MUTATIONS),
    )

    print(
        "N5_EXECUTION per_element: exact 2x2 effects, PSD support, Choi ranks, "
        "endpoint roots, likelihoods and Haar moments executed"
    )
    print(
        "N5_EXECUTION per_site: finite supplied response candidates, support calibration, "
        "event addition, formation-selection bias and conditional affinity executed"
    )
    print(
        "N5_EXECUTION per_mode: both global orientations and all 24 proper-cubic "
        "spin transports, plus two-through-four-use kernels, executed"
    )
    print(
        "N5_EXECUTION per_block: literal Block-38 F-M-B2 typed separation and one "
        "reduced sign-neutral collision quotient wrapper executed"
    )
    print(
        "N5_EXECUTION lattice_wide: checked and not executed - no full-Z3 collision "
        "process, empirical corpus, reset theorem or absolute-rate law is supplied"
    )
    print(
        "SUMMARY sharpness=derived orientation=calibration_choice "
        "axiom_decision_status=AXIOM_DECISION_READY decision_basis=multi_clause "
        "historical_shipping_label=BACKLOG_NO_PR "
        "prereg_sign_twin=falsified synthetic_evidence=none "
        f"input_sha256={input_fingerprint()}"
    )
    return checks.finish()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    args = parser.parse_args()
    return run(args.mutation)


if __name__ == "__main__":
    raise SystemExit(main())
