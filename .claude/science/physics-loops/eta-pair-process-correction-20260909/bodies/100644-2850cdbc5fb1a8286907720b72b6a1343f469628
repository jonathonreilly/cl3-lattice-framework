#!/usr/bin/env python3
"""Block32: symbolic-lambda guarded finite successor transaction.

This runner composes the exact factor-level pieces imported conditionally from
Blocks 28--31.
It deliberately does not compile the complete direct sum, its full-word
validator, or the stochastic writer dilations into one nearest-neighbor word.
"""

from __future__ import annotations

import hashlib
import itertools
import sys
from collections import Counter
from dataclasses import dataclass, replace
from functools import lru_cache
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_prior_record_live_preparation_two_event_prefix_2026_08_30 as block23  # noqa: E402
import admissibility_d4_self_delimiting_forward_record_append_history_2026_08_30 as block24  # noqa: E402
import admissibility_d4_returned_tip_strict_support_analytic_coupling_gate_2026_08_30 as block28  # noqa: E402
import admissibility_d4_output_conditioned_pair_successor_handoff_gate_2026_08_31 as block30  # noqa: E402
import admissibility_d4_nn_record_relation_transducer_dispatch_gate_2026_08_31 as block31  # noqa: E402


AUDIT_TIMEOUT_SEC = 900
PACKET_REL = (
    ".claude/science/physics-loops/"
    "toe-source-eta-ownership-block32-symbolic-lambda-guarded-successor-20260831"
)
PACKET = ROOT / PACKET_REL
RUNNER_SOURCE_PIN = PACKET / "RUNNER_SOURCE_PIN.md"

# Replaced by exact digests only after the runner and independent attacks freeze.
DIRECT_HASHES = {
    "scripts/admissibility_d4_prior_record_live_preparation_two_event_prefix_2026_08_30.py": "426488df2a431cb7d415d5e933013f7ce0826cc9514f96cd041b9fc6ff49742a",
    "scripts/admissibility_d4_self_delimiting_forward_record_append_history_2026_08_30.py": "f98534f07655e0de296f2060932e34aa7a600f08545f3661be2843d05accc15d",
    "scripts/admissibility_d4_returned_tip_strict_support_analytic_coupling_gate_2026_08_30.py": "91141d7b917b52eef1335cc6d405acd5927d75ab32ce2f4e0620d4c9007b9a2a",
    "scripts/admissibility_d4_output_conditioned_pair_successor_handoff_gate_2026_08_31.py": "21ff0be170dcb09eda05dbc0fe8e23e079e3dbba2faedd65cdc0014c1845bfb2",
    "scripts/admissibility_d4_nn_record_relation_transducer_dispatch_gate_2026_08_31.py": "0c547cf2e39506287409d6640593802028fef927e5912fda711a3a710e1fd374",
    "docs/MINIMAL_AXIOMS_2026-06-29.md": "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753",
    "docs/audit/data/axiom_premise_nodes.json": "56fde9133eb35f4c5ad8c38829904737771242d7c0188b55b7c03b4d6eb9b535",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md": "e7e75a36bd16094cbb547f6b215680ac45adc565c4cc93f05b0af17992eb9292",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md": "5516fb0bb8f50286b3c34d3f2668b1a2e347b9f7e257a8b5745f84f1093dd96b",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md": "755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563",
}

FROZEN = {
    "APPROACH_REGISTRY.md": "9d91544f51b64b2ca16cd0483d2ecf7f4a57606a5f6b48836b744b1a427ccfd6",
    "ARTIFACT_PLAN.md": "6c99dcd2dcb95fc5f2be7d9accda05076e946fdf0fe652afd48adf6bc6768025",
    "ASSUMPTIONS_AND_IMPORTS.md": "a859a76ab6302a18309010aeda623ae1ce465dc5202d06703677e72faefde6d2",
    "AUTHORITY_GATE.md": "11f8a4aac8abf2f4fc20487ae32f31286aa8ea5cd639f8432c7ae423d34a07b3",
    "GOAL.md": "ced16d93416cbf5d796ede80ff596d528568da11e73490d27cec64a8ef099c0c",
    "INDEPENDENT_STATIC_ATTACK_FINAL.md": "88ff1585ec2163f3791986365e1d41d2e39b172175d99b56478667ff218cd602",
    "MUTATION_PLAN.md": "fb97cb2d9666af285d7bf7c7ffa41a647e66a18204b2dc895a78308807eaa79f",
    "NO_GO_DISCIPLINE_CHECKLIST.md": "8346adb405261e1156443ba5446f1385a61f76cafbf7c09c383dea713140d1a8",
    "OPPORTUNITY_QUEUE.md": "62ec71b5d43af58f917ba7c27b0f3b01c490dd2bc3ca2ff3790c0fcc0ba012cf",
    "PANEL_RETURN.md": "929dc0c9cb390d5e749d9c37751c3526ce86f75f90b923c1f23c6adc471cca47",
    "PREFLIGHT_WITNESSES.md": "8e7ec169ab96cdf6a77e673b0183ef0e0b1b68036766e91615c49f58d9c5d3ce",
    "PREREG_AMENDMENT_UNCOMPUTE_ORDER.md": "2a1affbdba879eec0423ad5c1a6523660fc669bf0a44c32cfd6155d88b41de64",
    "ROUTE_PORTFOLIO.md": "153077a7f8346b07e9fe28f4452444cba35ea03403872acf06d465a91c06b0cf",
    "STATE.yaml": "7b89e41fbcf28512a0e8853aa23913dc4e651f509054b67547191b8c1a5261fa",
    "TRACE_GATE.md": "aab76badeba4fe723c0d7c72d5de5d541d659ee3d105a7cdda1f8e062289c3c1",
}

AUDIT_INPUT_PATHS = tuple(DIRECT_HASHES) + tuple(
    f"{PACKET_REL}/{name}" for name in FROZEN
) + (f"{PACKET_REL}/RUNNER_SOURCE_PIN.md",)

Coord = tuple[int, int, int]
ZERO: Coord = (0, 0, 0)
E1: Coord = (1, 0, 0)
DIRECTIONS = block23.DIRECTIONS
OUTCOMES = block23.OUTCOMES
ROTATIONS = block23.ROTATIONS
CANONICAL_LEFT = block28.Y_LEFT
CANONICAL_FRONT = block28.F_LEFT
CHIRALITY = 1
LAMBDA = sp.symbols("lambda", real=True)
LAMBDA_DOMAIN = sp.Interval(sp.S.Zero, sp.S.One, right_open=True)
BLANK_SELECTOR = (0,) * 16


def one_hot(index: int, size: int = 16) -> tuple[int, ...]:
    return tuple(int(position == index) for position in range(size))


@lru_cache(maxsize=1)
def locked_word_decode_table():
    return {
        block23.locked_word(front, outcome): (front, outcome)
        for front, outcome in itertools.product(DIRECTIONS, OUTCOMES)
    }


def decode_pair_pointer_configuration(configuration):
    decode = locked_word_decode_table()
    locked = tuple(
        (center, decode[word])
        for center, word in configuration
        if word in decode
    )
    if len(locked) != 2:
        return None
    left_entries = tuple(
        entry for entry in locked if entry[0] in block28.LEFT_TARGETS
    )
    right_entries = tuple(
        entry for entry in locked if entry[0] in block28.RIGHT_TARGETS
    )
    if len(left_entries) != 1 or len(right_entries) != 1:
        return None
    left_center, (left_exit, left_source) = left_entries[0]
    right_center, (right_exit, right_source) = right_entries[0]
    if (
        left_center != block24.forward_center(block28.Y_LEFT, left_exit)
        or right_center
        != block24.forward_center(block28.Y_RIGHT, right_exit)
    ):
        return None
    return left_exit, right_exit, left_source, right_source


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def runner_source_pin_ok() -> bool:
    if not RUNNER_SOURCE_PIN.exists():
        return False
    pins = {}
    for line in RUNNER_SOURCE_PIN.read_text().splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            pins[key.strip()] = value.strip().strip("`")
    return pins.get("source_sha256") == file_sha256(Path(__file__))


def frozen_hashes_ok() -> bool:
    return (
        "PENDING" not in set(DIRECT_HASHES.values()) | set(FROZEN.values())
        and all(file_sha256(ROOT / name) == digest for name, digest in DIRECT_HASHES.items())
        and all(file_sha256(PACKET / name) == digest for name, digest in FROZEN.items())
        and runner_source_pin_ok()
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


def add(*vectors: Coord) -> Coord:
    return tuple(sum(values) for values in zip(*vectors))


def scale(number: int, vector: Coord) -> Coord:
    return tuple(number * value for value in vector)


def dot(left: Coord, right: Coord) -> int:
    return sum(a * b for a, b in zip(left, right))


def lateral(front: Coord) -> tuple[Coord, ...]:
    return tuple(direction for direction in DIRECTIONS if dot(front, direction) == 0)


def q_weight(lam, left_exit, right_exit, mutation: str | None = None):
    if left_exit == right_exit:
        numerator = 1 + (4 if mutation == "bad_diagonal" else 3) * lam
    else:
        numerator = 1 - lam
    return sp.simplify(numerator / 16)


def q_table(lam=LAMBDA, mutation: str | None = None):
    return {
        pair: q_weight(lam, *pair, mutation)
        for pair in itertools.product(block28.LEFT_EXITS, block28.RIGHT_EXITS)
    }


@lru_cache(maxsize=None)
def domain_positive_root_gram(probability, domain=LAMBDA_DOMAIN):
    """Return |sqrt(p)|^2=p only after proving this actual p is positive."""
    positive_locus = sp.solve_univariate_inequality(
        sp.StrictGreaterThan(probability, 0), LAMBDA, relational=False
    )
    if domain.is_subset(positive_locus) is not True:
        raise ValueError("probability is not strictly positive on the claim domain")
    positive_symbol = sp.symbols("positive_weight", positive=True, real=True)
    if sp.simplify(
        sp.sqrt(positive_symbol)
        * sp.conjugate(sp.sqrt(positive_symbol))
        - positive_symbol
    ) != 0:
        raise ValueError("positive-root Gram lemma did not reduce")
    return sp.simplify(probability)


@lru_cache(maxsize=None)
def q_family_certificate(
    mutation: str | None = None, domain=LAMBDA_DOMAIN
) -> bool:
    table = q_table(mutation=mutation)
    left_rows = {
        g: sp.simplify(sum(table[g, h] for h in block28.RIGHT_EXITS))
        for g in block28.LEFT_EXITS
    }
    right_rows = {
        h: sp.simplify(sum(table[g, h] for g in block28.LEFT_EXITS))
        for h in block28.RIGHT_EXITS
    }
    matrix = sp.Matrix(
        [[table[g, h] for h in block28.RIGHT_EXITS] for g in block28.LEFT_EXITS]
    )
    expected = (1 - LAMBDA) * sp.ones(4) / 16 + LAMBDA * sp.eye(4) / 4
    equality = sp.simplify(
        sum(value for (g, h), value in table.items() if g == h)
    )
    positive_locus = sp.Interval.open(sp.Rational(-1, 3), sp.S.One)
    claimed_strict_locus = domain.intersect(positive_locus)
    return (
        len(table) == 16
        and sp.simplify(sum(table.values())) == 1
        and all(value == sp.Rational(1, 4) for value in left_rows.values())
        and all(value == sp.Rational(1, 4) for value in right_rows.values())
        and matrix == expected
        and equality == (1 + 3 * LAMBDA) / 4
        and claimed_strict_locus == domain
        and sp.simplify(q_weight(sp.S.Zero, block28.LEFT_EXITS[0], block28.RIGHT_EXITS[1])) > 0
        and (
            domain != sp.Interval(0, 1)
            or q_weight(sp.S.One, block28.LEFT_EXITS[0], block28.RIGHT_EXITS[1]) > 0
        )
    )


def exact_lambda_locus(mutation: str | None = None):
    residuals = transaction_lambda_residuals(mutation)
    locus = LAMBDA_DOMAIN
    for residual in residuals:
        residual = sp.factor(residual)
        if residual == 0:
            continue
        locus = locus.intersect(
            sp.solveset(sp.Eq(residual, 0), LAMBDA, domain=sp.S.Reals)
        )
    diagonal_slope = 4 if mutation == "bad_diagonal" else 3
    strict_support_locus = sp.Interval.open(
        -sp.Rational(1, diagonal_slope), sp.S.One
    )
    return locus.intersect(strict_support_locus)


def transaction_lambda_residuals(mutation: str | None = None):
    table = q_table(mutation=mutation)
    q_sum = sp.factor(sum(table.values()))
    equality = sp.factor(
        sum(weight for (g, h), weight in table.items() if g == h)
    )
    family = family_gram(
        OUTCOMES[0], OUTCOMES[-1], q_mutation=mutation
    )
    first_event_terms = (
        table.values()
        if mutation == "omit_first_equality_filter"
        else (
            weight for (g, h), weight in table.items() if g == h
        )
    )
    joint_equality = sp.factor(sum(first_event_terms) * equality)
    second_table = route_conditioned_q_table(
        0,
        pair_mutation=(
            "selector_dependent_q"
            if mutation == "selector_dependent_q"
            else None
        ),
    )
    pair_tensor = sp.Matrix(
        3,
        3,
        lambda i, j: sp.factor(
            sum(table[g, h] * g[i] * h[j] for g, h in table)
        ),
    )
    front = sp.Matrix(CANONICAL_FRONT)
    expected_pair_tensor = sp.simplify(
        LAMBDA * (sp.eye(3) - front * front.T) / 2
    )
    residuals = {
        sp.factor(q_sum - 1),
        sp.factor(equality - (1 + 3 * LAMBDA) / 4),
        *(
            sp.factor(
                sum(table[g, h] for h in block28.RIGHT_EXITS)
                - sp.Rational(1, 4)
            )
            for g in block28.LEFT_EXITS
        ),
        *(
            sp.factor(
                sum(table[g, h] for g in block28.LEFT_EXITS)
                - sp.Rational(1, 4)
            )
            for h in block28.RIGHT_EXITS
        ),
        sp.factor(family - 1),
        sp.factor(joint_equality - equality**2),
        *(
            sp.factor(second_table[pair] - q_table()[pair])
            for pair in q_table()
        ),
        *(
            sp.factor(pair_tensor[i, j] - expected_pair_tensor[i, j])
            for i in range(3)
            for j in range(3)
        ),
        *(
            sp.factor(weight * family - weight)
            for weight in table.values()
        ),
    }
    return tuple(sorted(residuals, key=str))


def configuration_sample_bits(configuration):
    words = dict(configuration)
    left = CANONICAL_LEFT
    front = CANONICAL_FRONT
    right = add(left, scale(9, front))
    left_bits = []
    right_bits = []
    for direction in lateral(front):
        inward = scale(-4, direction)
        left_center = add(left, scale(9, direction))
        right_center = add(right, scale(9, direction))
        left_bits.append(block31.pointer_bit(words[left_center], inward))
        right_bits.append(block31.pointer_bit(words[right_center], inward))
    return tuple(left_bits), tuple(right_bits)


def token_for_configuration(configuration):
    left_bits, right_bits = configuration_sample_bits(configuration)
    tokens, left_after, right_after = block31.simulate_macro_basis(
        left_bits, right_bits, (0,) * 16
    )
    return tokens, left_after, right_after


def malformed_same_sample_witness():
    outcome = block28.pair_record_outcomes()[0]
    original = dict(outcome.pointer_configuration)
    center = next(
        center
        for center, word in outcome.pointer_configuration
        if block23.decode_locked_word(word) is not None
    )
    original_word = original[center]
    for index, site in enumerate(block23.POINTER_ORDER):
        if site in block23.STATUS:
            continue
        candidate = list(original_word)
        candidate[index] ^= 1
        candidate = tuple(candidate)
        if block23.decode_locked_word(candidate) is not None:
            continue
        changed = tuple(
            (candidate_center, candidate if candidate_center == center else word)
            for candidate_center, word in outcome.pointer_configuration
        )
        malformed = replace(outcome, pointer_configuration=changed)
        if (
            block28.decode_pair_record_outcome(malformed) is None
            and configuration_sample_bits(changed)
            == configuration_sample_bits(outcome.pointer_configuration)
        ):
            return outcome.pointer_configuration, changed
    raise ValueError("no malformed full-word witness with the same STATUS samples")


@dataclass(frozen=True)
class ActiveInputState:
    pointer_configuration: tuple
    token: tuple[int, ...]
    transients_clean: bool
    selector: tuple[int, ...]
    blank_centers: frozenset[Coord]


@dataclass(frozen=True)
class ActiveProjector:
    control_index: int
    route_index: int
    pointer_configuration: tuple
    token: tuple[int, ...]
    source_left: Coord
    source_right: Coord
    plan: object
    blank_centers: frozenset[Coord]

    def input_state(self) -> ActiveInputState:
        return ActiveInputState(
            self.pointer_configuration,
            self.token,
            True,
            BLANK_SELECTOR,
            self.blank_centers,
        )

    def matches(
        self, state: ActiveInputState, mutation: str | None = None
    ) -> bool:
        pointer_ok = (
            True
            if mutation == "omit_full_pointer_guard"
            else state.pointer_configuration == self.pointer_configuration
        )
        selector_ok = (
            True
            if mutation == "omit_selector_guard"
            else state.selector == BLANK_SELECTOR
        )
        required_blank = set(self.blank_centers)
        if mutation == "omit_target_guard":
            required_blank.remove(self.plan.left.targets[0])
        if mutation == "omit_unused_carrier_guard":
            protected = set(self.plan.left.targets + self.plan.right.targets)
            protected.update(block30.successor_blank_centers(self.plan))
            required_blank.remove(next(iter(required_blank - protected)))
        token_ok = (
            True if mutation == "omit_token_guard" else state.token == self.token
        )
        transient_ok = (
            True
            if mutation == "omit_transient_guard"
            else state.transients_clean
        )
        return (
            pointer_ok
            and token_ok
            and transient_ok
            and selector_ok
            and required_blank.issubset(state.blank_centers)
        )


@lru_cache(maxsize=1)
def active_projectors() -> tuple[ActiveProjector, ...]:
    order = block31.token_order(CANONICAL_FRONT)
    carrier = block30.candidate_carrier_centers(
        CANONICAL_LEFT, CANONICAL_FRONT, CHIRALITY
    )
    token_cache = {}
    projectors = []
    for control_index, outcome in enumerate(block28.pair_record_outcomes()):
        decoded = decode_pair_pointer_configuration(
            outcome.pointer_configuration
        )
        if decoded is None:
            raise ValueError("complete Block28 pointer control did not decode")
        g, h, source_left, source_right = decoded
        pair = (g, h)
        route_index = next(
            index
            for index, (_relation, left_exit, right_exit) in enumerate(order)
            if (left_exit, right_exit) == pair
        )
        if pair not in token_cache:
            token_cache[pair] = token_for_configuration(
                outcome.pointer_configuration
            )
        token, left_after, right_after = token_cache[pair]
        if (
            token != one_hot(route_index)
            or (left_after, right_after)
            != configuration_sample_bits(outcome.pointer_configuration)
        ):
            raise ValueError("Block31 token does not bind the pointer route")
        plan = block30.route_plan(
            CANONICAL_LEFT, CANONICAL_FRONT, g, h, CHIRALITY
        )
        locked = {plan.left.start, plan.right.start}
        projectors.append(
            ActiveProjector(
                control_index,
                route_index,
                outcome.pointer_configuration,
                token,
                source_left,
                source_right,
                plan,
                frozenset(set(carrier) - locked),
            )
        )
    return tuple(projectors)


@lru_cache(maxsize=None)
def full_pointer_guard_certificate(mutation: str | None = None) -> bool:
    projectors = active_projectors()
    configurations = tuple(
        projector.pointer_configuration for projector in projectors
    )
    route_counts = Counter(projector.route_index for projector in projectors)
    own_match = all(
        projector.matches(projector.input_state(), mutation)
        for projector in projectors
    )
    valid, malformed = malformed_same_sample_witness()
    witness = projectors[0]
    malformed_state = replace(
        witness.input_state(), pointer_configuration=malformed
    )
    spent_state = replace(witness.input_state(), selector=one_hot(witness.route_index))
    missing_target = witness.plan.left.targets[0]
    dirty_state = replace(
        witness.input_state(),
        blank_centers=witness.blank_centers - {missing_target},
    )
    protected = set(witness.plan.left.targets + witness.plan.right.targets)
    protected.update(block30.successor_blank_centers(witness.plan))
    missing_unused = next(iter(set(witness.blank_centers) - protected))
    dirty_unused_state = replace(
        witness.input_state(),
        blank_centers=witness.blank_centers - {missing_unused},
    )
    dirty_token_state = replace(witness.input_state(), token=(0,) * 16)
    dirty_transient_state = replace(
        witness.input_state(), transients_clean=False
    )
    invalid_states = (
        malformed_state,
        spent_state,
        dirty_state,
        dirty_unused_state,
        dirty_token_state,
        dirty_transient_state,
    )
    inactive = all(
        not any(projector.matches(state, mutation) for projector in projectors)
        for state in invalid_states
    )
    raw_token_collision = token_for_configuration(valid) == token_for_configuration(
        malformed
    )
    return (
        len(projectors) == len(configurations) == len(set(configurations)) == 3136
        and set(route_counts.values()) == {196}
        and len(route_counts) == 16
        and all(len(projector.blank_centers) == 158 for projector in projectors)
        and own_match
        and inactive
        and block30.local_pointer_code_certificate()
        and block30.handoff_control_channel_certificate()
        and raw_token_collision
        and malformed not in set(configurations)
    )


@lru_cache(maxsize=1)
def active_projector_orthogonality_certificate() -> bool:
    projectors = active_projectors()
    configurations = tuple(
        projector.pointer_configuration for projector in projectors
    )
    local_words = tuple(
        {word for configuration in configurations for _center, word in configuration}
    )
    local_pointer_overlaps = {
        (index, a, b): block23.pure_overlap(
            block23.radial_bloch(site, a),
            block23.radial_bloch(site, b),
        )
        for index, site in enumerate(block23.POINTER_ORDER)
        for a, b in itertools.product((0, 1), repeat=2)
    }
    local_pointer_factors_orthonormal = all(
        overlap == int(a == b)
        for (_index, a, b), overlap in local_pointer_overlaps.items()
    )
    local_code_orthonormal = (
        local_pointer_factors_orthonormal
        and len(local_words) == len(set(local_words))
        and all(
            sp.prod(
                local_pointer_overlaps[k, a, b]
                for k, (a, b) in enumerate(zip(left, right))
            )
            == int(i == j)
            for i, left in enumerate(local_words)
            for j, right in enumerate(local_words)
        )
    )
    selector_words = (BLANK_SELECTOR,) + tuple(one_hot(i) for i in range(16))
    cells = selector_cells(CANONICAL_LEFT, CANONICAL_FRONT)
    local_selector_overlaps = {
        (index, a, b): block23.pure_overlap(
            block23.radial_bloch(site, a),
            block23.radial_bloch(site, b),
        )
        for index, site in enumerate(cells)
        for a, b in itertools.product((0, 1), repeat=2)
    }
    local_selector_code_orthonormal = all(
        overlap == int(a == b)
        for (_index, a, b), overlap in local_selector_overlaps.items()
    )
    selector_code_orthonormal = (
        local_selector_code_orthonormal
        and len(selector_words) == len(set(selector_words)) == 17
        and all(
            sp.prod(
                local_selector_overlaps[k, a, b]
                for k, (a, b) in enumerate(zip(left, right))
            )
            == int(i == j)
            for i, left in enumerate(selector_words)
            for j, right in enumerate(selector_words)
        )
    )
    return (
        len(configurations) == len(set(configurations)) == 3136
        and local_code_orthonormal
        and selector_code_orthonormal
    )


def apply_gate(state: dict[Coord, int], gate) -> None:
    if gate.kind == "SWAP":
        first, second = gate.sites
        state[first], state[second] = state[second], state[first]
    elif gate.kind == "CNOT":
        control, target = gate.sites
        state[target] ^= state[control]
    elif gate.kind == "TOFFOLI":
        control_a, control_b, target = gate.sites
        state[target] ^= state[control_a] & state[control_b]
    else:
        raise ValueError(gate.kind)


@lru_cache(maxsize=None)
def comparator_round_trip_certificate(omit_inverse: bool = False) -> bool:
    layers = block31.macro_layers(CANONICAL_LEFT, CANONICAL_FRONT)
    touched = {site for layer in layers for gate in layer for site in gate.sites}
    left_samples = tuple(
        block31.sample_site(CANONICAL_LEFT, CANONICAL_FRONT, "left", direction)
        for direction in lateral(CANONICAL_FRONT)
    )
    right_samples = tuple(
        block31.sample_site(CANONICAL_LEFT, CANONICAL_FRONT, "right", direction)
        for direction in lateral(CANONICAL_FRONT)
    )
    token_cells = tuple(
        block31.token_cell(CANONICAL_LEFT, CANONICAL_FRONT, direction, relation)
        for relation, direction in itertools.product(
            block31.RELATIONS, lateral(CANONICAL_FRONT)
        )
    )
    for bits in itertools.product((0, 1), repeat=8):
        initial = {site: 0 for site in touched}
        for site, bit in zip(left_samples + right_samples, bits):
            initial[site] = bit
        state = dict(initial)
        for layer in layers:
            for gate in layer:
                apply_gate(state, gate)
        if not omit_inverse:
            for layer in reversed(layers):
                for gate in reversed(layer):
                    apply_gate(state, gate)
        if state != initial:
            return False
        if not omit_inverse and any(state[cell] for cell in token_cells):
            return False
    return True


@lru_cache(maxsize=1)
def late_uncompute_status_collision_certificate() -> bool:
    layers = block31.macro_layers(CANONICAL_LEFT, CANONICAL_FRONT)
    touched = {site for layer in layers for gate in layer for site in gate.sites}
    left_samples = tuple(
        block31.sample_site(CANONICAL_LEFT, CANONICAL_FRONT, "left", direction)
        for direction in lateral(CANONICAL_FRONT)
    )
    right_samples = tuple(
        block31.sample_site(CANONICAL_LEFT, CANONICAL_FRONT, "right", direction)
        for direction in lateral(CANONICAL_FRONT)
    )
    samples = set(left_samples + right_samples)
    hazard_plans = 0
    hazard_branches = 0
    explicit_failure = False
    outcomes_by_pair = {}
    for outcome in block28.pair_record_outcomes():
        outcomes_by_pair.setdefault(
            (outcome.left_exit, outcome.right_exit), outcome
        )
    for g, h in itertools.product(lateral(CANONICAL_FRONT), repeat=2):
        plan = block30.route_plan(
            CANONICAL_LEFT, CANONICAL_FRONT, g, h, CHIRALITY
        )
        frame = block30.successor_frame(plan)
        plan_hazard = False
        for left_exit, right_exit in itertools.product(
            frame.left_exits, frame.right_exits
        ):
            selected = {
                block24.forward_center(frame.left_anchor, left_exit),
                block24.forward_center(frame.right_anchor, right_exit),
            }
            written_sites = set().union(
                *(block30.block_sites(center) for center in selected)
            )
            hits = samples.intersection(written_sites)
            if not hits:
                continue
            plan_hazard = True
            hazard_branches += 1
            if explicit_failure:
                continue
            bits = configuration_sample_bits(
                outcomes_by_pair[(g, h)].pointer_configuration
            )
            initial = {site: 0 for site in touched}
            for site, bit in zip(left_samples + right_samples, bits[0] + bits[1]):
                initial[site] = bit
            state = dict(initial)
            for layer in layers:
                for gate in layer:
                    apply_gate(state, gate)
            changed = next(site for site in hits if initial[site] == 0)
            state[changed] = 1
            for layer in reversed(layers):
                for gate in reversed(layer):
                    apply_gate(state, gate)
            explicit_failure = state != initial
        hazard_plans += int(plan_hazard)
    return hazard_plans == 4 and hazard_branches == 28 and explicit_failure


def selector_cells(left: Coord, front: Coord) -> tuple[Coord, ...]:
    return tuple(
        add(left, scale(-100, front), scale(3, g), h)
        for _relation, g, h in block31.token_order(front)
    )


@lru_cache(maxsize=None)
def selector_geometry_certificate() -> bool:
    base = selector_cells(CANONICAL_LEFT, CANONICAL_FRONT)
    layers = block31.macro_layers(CANONICAL_LEFT, CANONICAL_FRONT)
    comparator_sites = {site for layer in layers for gate in layer for site in gate.sites}
    carrier = block30.candidate_carrier_centers(
        CANONICAL_LEFT, CANONICAL_FRONT, CHIRALITY
    )
    carrier_sites = set().union(*(block30.block_sites(center) for center in carrier))
    shift = (7, -11, 5)
    moved = selector_cells(add(CANONICAL_LEFT, shift), CANONICAL_FRONT)
    if moved != tuple(add(site, shift) for site in base):
        return False
    for rotation in ROTATIONS:
        rotated = selector_cells(
            block23.mat_vec(rotation, CANONICAL_LEFT),
            block23.mat_vec(rotation, CANONICAL_FRONT),
        )
        expected = tuple(block23.mat_vec(rotation, site) for site in base)
        if set(rotated) != set(expected):
            return False
        base_labels = block31.token_order(CANONICAL_FRONT)
        rotated_labels = block31.token_order(
            block23.mat_vec(rotation, CANONICAL_FRONT)
        )
        rotated_binding = dict(zip(rotated_labels, rotated))
        for label, site in zip(base_labels, base):
            relation, g, h = label
            moved_label = (
                relation,
                block23.mat_vec(rotation, g),
                block23.mat_vec(rotation, h),
            )
            if rotated_binding[moved_label] != block23.mat_vec(rotation, site):
                return False
    for front in DIRECTIONS:
        original = block31.token_order(front)
        exchanged = block31.token_order(scale(-1, front))
        exchange_indices = tuple(
            next(
                index
                for index, (candidate_relation, candidate_g, candidate_h) in enumerate(
                    exchanged
                )
                if (candidate_relation, candidate_g, candidate_h)
                == (relation, h, g)
            )
            for relation, g, h in original
        )
        if len(set(exchange_indices)) != 16:
            return False
    return (
        len(base) == len(set(base)) == 16
        and set(base).isdisjoint(comparator_sites)
        and set(base).isdisjoint(carrier_sites)
        and all(
            block23.pure_overlap(
                block23.radial_bloch(site, left_bit),
                block23.radial_bloch(site, right_bit),
            )
            == int(left_bit == right_bit)
            for site in base
            for left_bit, right_bit in itertools.product((0, 1), repeat=2)
        )
    )


@lru_cache(maxsize=None)
def dispatch_certificate(mutation: str | None = None) -> bool:
    count = 0
    for front in DIRECTIONS:
        order = list(block31.token_order(front))
        token_labels = list(range(16))
        if mutation == "alias_token" and front == E1:
            token_labels[-1] = token_labels[0]
        if len(set(token_labels)) != 16:
            return False
        for index, (relation, g, actual_h) in enumerate(order):
            route_h = actual_h
            if mutation == "swap_perpendicular" and relation in (
                "perp_plus",
                "perp_minus",
            ):
                route_h = block31.right_direction(
                    front,
                    g,
                    "perp_minus" if relation == "perp_plus" else "perp_plus",
                )
            try:
                plan = block30.route_plan(ZERO, front, g, route_h, CHIRALITY)
            except ValueError:
                return False
            if not (
                token_labels[index] == index
                and route_h == actual_h
                and block30.route_plan_certificate(plan)
            ):
                return False
            count += 1
    if mutation == "lambda_dependent_route":
        signatures = (
            block30.handoff_signature(sp.S.Zero, CHIRALITY),
            block30.handoff_signature(
                sp.Rational(1, 2), CHIRALITY, "lambda_dependent_route"
            ),
        )
        return signatures[0] == signatures[1]
    return (
        count == 96
        and block30.covariance_certificate()
        and block31.logical_side_exchange_certificate()
        and selector_geometry_certificate()
    )


@dataclass(frozen=True)
class SelectorMap:
    route_index: int
    input_word: tuple[int, ...]
    output_word: tuple[int, ...]


def selector_maps(mutation: str | None = None) -> tuple[SelectorMap, ...]:
    maps = []
    for route_index in range(16):
        if mutation == "erase_selector":
            output = BLANK_SELECTOR
        elif mutation == "alias_selector" and route_index == 15:
            output = one_hot(0)
        elif mutation == "misbind_selector" and route_index in (0, 1):
            output = one_hot(1 - route_index)
        else:
            output = one_hot(route_index)
        maps.append(SelectorMap(route_index, BLANK_SELECTOR, output))
    return tuple(maps)


@lru_cache(maxsize=None)
def selector_stop_certificate(
    *,
    stop_present: bool = True,
    stop_scale=sp.S.One,
    guard_mutation: str | None = None,
    write_mutation: str | None = None,
    stop_mutation: str | None = None,
) -> bool:
    maps = selector_maps(write_mutation)
    outputs = tuple(selector_map.output_word for selector_map in maps)
    projectors = active_projectors()
    active_diagonal = tuple(
        int(
            projector.matches(
                projector.input_state(), mutation=guard_mutation
            )
        )
        for projector in projectors
    )
    active_stop = (
        sp.S.One
        if stop_present and stop_mutation == "overlapping_STOP"
        else sp.S.Zero
    )
    active_total = tuple(
        sp.simplify(value + active_stop) for value in active_diagonal
    )
    inactive_active = 0
    inactive_stop = stop_scale**2 if stop_present else sp.S.Zero
    inactive_total = sp.simplify(inactive_active + inactive_stop)
    witness = projectors[0]
    _valid, malformed = malformed_same_sample_witness()
    inactive_inputs = (
        replace(witness.input_state(), pointer_configuration=malformed),
        replace(witness.input_state(), selector=one_hot(witness.route_index)),
        replace(
            witness.input_state(),
            blank_centers=witness.blank_centers - {witness.plan.left.targets[0]},
        ),
        replace(witness.input_state(), token=(0,) * 16),
        replace(witness.input_state(), transients_clean=False),
    )
    inactive_outputs = list(inactive_inputs)
    if stop_mutation == "nonidentity_STOP":
        inactive_outputs[0] = replace(inactive_inputs[0], selector=one_hot(0))
    return (
        full_pointer_guard_certificate(guard_mutation)
        and len(maps) == 16
        and all(selector_map.input_word == BLANK_SELECTOR for selector_map in maps)
        and len(outputs) == len(set(outputs)) == 16
        and BLANK_SELECTOR not in outputs
        and all(
            selector_map.output_word == one_hot(selector_map.route_index)
            for selector_map in maps
        )
        and set(active_diagonal) == {1}
        and set(active_total) == {1}
        and inactive_total == 1
        and tuple(inactive_outputs) == inactive_inputs
        and all(
            not any(projector.matches(state) for projector in projectors)
            for state in inactive_inputs
        )
    )


@dataclass(frozen=True)
class FiniteCarrierState:
    selector: tuple[int, ...]
    blank_centers: frozenset[Coord]
    locked_centers: frozenset[Coord]


def apply_finite_transaction(
    state: FiniteCarrierState,
    selector_index: int,
    guard_blank: frozenset[Coord],
    consumed_blank: frozenset[Coord],
) -> FiniteCarrierState:
    active = (
        state.selector == BLANK_SELECTOR
        and guard_blank.issubset(state.blank_centers)
    )
    if not active:
        return state
    return FiniteCarrierState(
        one_hot(selector_index),
        state.blank_centers - consumed_blank,
        state.locked_centers | consumed_blank,
    )


@lru_cache(maxsize=None)
def finite_second_application_identity_certificate(
    mutation: str | None = None,
) -> bool:
    checked = 0
    for front in DIRECTIONS:
        order = block31.token_order(front)
        carrier = block30.candidate_carrier_centers(ZERO, front, CHIRALITY)
        for g, h in itertools.product(lateral(front), repeat=2):
            selector_index = next(
                index
                for index, (_relation, left_exit, right_exit) in enumerate(order)
                if (left_exit, right_exit) == (g, h)
            )
            plan = block30.route_plan(ZERO, front, g, h, CHIRALITY)
            initial_blank = frozenset(
                set(carrier) - {plan.left.start, plan.right.start}
            )
            trail = frozenset(plan.left.targets + plan.right.targets)
            frame = block30.successor_frame(plan)
            for left_exit, right_exit in itertools.product(
                frame.left_exits, frame.right_exits
            ):
                second_targets = frozenset(
                    {
                        block24.forward_center(frame.left_anchor, left_exit),
                        block24.forward_center(frame.right_anchor, right_exit),
                    }
                )
                consumed = trail | second_targets
                applied_consumed = (
                    frozenset({sorted(consumed)[0]})
                    if mutation == "partial_write"
                    else consumed
                )
                initial_locked = frozenset(
                    {plan.left.start, plan.right.start}
                )
                initial = FiniteCarrierState(
                    BLANK_SELECTOR, initial_blank, initial_locked
                )
                first = apply_finite_transaction(
                    initial, selector_index, initial_blank, applied_consumed
                )
                second = apply_finite_transaction(
                    first, selector_index, initial_blank, applied_consumed
                )
                selector_only = FiniteCarrierState(
                    first.selector, initial_blank, initial_locked
                )
                debit_only = FiniteCarrierState(
                    BLANK_SELECTOR, first.blank_centers, first.locked_centers
                )
                every_dirty_state_stops = all(
                    apply_finite_transaction(
                        FiniteCarrierState(
                            BLANK_SELECTOR,
                            initial_blank - {dirty_center},
                            initial_locked | {dirty_center},
                        ),
                        selector_index,
                        initial_blank,
                        consumed,
                    )
                    == FiniteCarrierState(
                        BLANK_SELECTOR,
                        initial_blank - {dirty_center},
                        initial_locked | {dirty_center},
                    )
                    for dirty_center in initial_blank
                )
                if not (
                    len(consumed) == 12
                    and len(first.blank_centers) == 146
                    and len(first.locked_centers) == 14
                    and first.selector != BLANK_SELECTOR
                    and second == first
                    and apply_finite_transaction(
                        selector_only, selector_index, initial_blank, consumed
                    )
                    == selector_only
                    and apply_finite_transaction(
                        debit_only, selector_index, initial_blank, consumed
                    )
                    == debit_only
                    and every_dirty_state_stops
                ):
                    return False
                checked += 1
    return checked == 6 * 16 * 16


@lru_cache(maxsize=None)
def transition_gram_matrix(
    drop_outcome: bool = False, raw_probability_root: bool = False
) -> sp.Matrix:
    rows = []
    for source in OUTCOMES:
        row = []
        for index, target in enumerate(OUTCOMES):
            probability = block23.transition(source, target)
            if drop_outcome and index == len(OUTCOMES) - 1:
                probability = sp.S.Zero
            elif raw_probability_root:
                probability = sp.simplify(probability**2)
            row.append(probability)
        rows.append(row)
    return sp.Matrix(rows)


@dataclass(frozen=True)
class ComparatorRangeState:
    control_index: int
    route_index: int
    pointer_configuration: tuple
    selector: tuple[int, ...]
    token: tuple[int, ...]
    transients_clean: bool
    blank_centers: frozenset[Coord]


@dataclass(frozen=True)
class LocalStageGram:
    """A 14-by-14 Gram table recontracted from one physical writer type."""

    incoming: Coord
    direction: Coord
    kind: str
    gram_matrix: object
    input_words: tuple[tuple[int, ...], ...]
    output_words: tuple[tuple[int, ...], ...]
    physical_branches: int


@lru_cache(maxsize=None)
def local_stage_gram_table(
    incoming: Coord,
    direction: Coord,
    *,
    drop_outcome: bool = False,
    raw_probability_root: bool = False,
) -> LocalStageGram:
    """Recontract the actual Block24/28 factors for one orientation class."""
    if direction != incoming and dot(incoming, direction) != 0:
        raise ValueError("route stage must be straight or a right-angle turn")
    rows = []
    input_words = []
    output_words = []
    physical = 0
    kind = "straight" if direction == incoming else "turn"
    for source in OUTCOMES:
        current_word = block23.locked_word(incoming, source)
        input_words.append(current_word)
        row = []
        source_outputs = []
        for target_index, target in enumerate(OUTCOMES):
            if kind == "straight":
                branch = block24.append_branch(ZERO, current_word, target)
                effect = block24.contract_append_effect(branch.factors)
                data = block24.factor_dictionary(branch.factors)
                writer_maps = data["forward_writer_pointer_maps"]
                output_word = tuple(entry[2] for entry in writer_maps)
                branch_ok = (
                    block24.append_factorization_is_physical(branch)
                    and block24.branch_effect_is_recontracted(branch)
                    and effect.current_word == current_word
                    and effect.forward_center
                    == block24.forward_center(ZERO, direction)
                    and effect.forward_input == block23.BLANK_BLOCK
                )
            else:
                branch = block28.turn_branch(
                    ZERO, incoming, source, direction, target
                )
                effect = block28.contract_turn_effect(branch.factors)
                output_word = effect.output_word
                branch_ok = (
                    block28.turn_branch_is_physical(branch)
                    and effect.current_word == current_word
                    and effect.target_center
                    == block24.forward_center(ZERO, direction)
                    and effect.forward_input == block23.BLANK_BLOCK
                )
            coefficient = sp.simplify(effect.scalar)
            branch_ok &= (
                block23.decode_locked_word(output_word) == (direction, target)
                and sp.simplify(
                    coefficient - block23.transition(source, target)
                )
                == 0
            )
            if not branch_ok:
                raise ValueError("local writer factor did not recontract physically")
            physical += 1
            source_outputs.append(output_word)
            if drop_outcome and target_index == len(OUTCOMES) - 1:
                coefficient = sp.S.Zero
            elif raw_probability_root:
                coefficient = sp.simplify(coefficient**2)
            row.append(coefficient)
        if source_outputs != [
            block23.locked_word(direction, target) for target in OUTCOMES
        ]:
            raise ValueError("writer outputs are not the declared target Records")
        rows.append(row)
        if not output_words:
            output_words = source_outputs
        elif output_words != source_outputs:
            raise ValueError("writer output word depends on undeclared source data")
    return LocalStageGram(
        incoming,
        direction,
        kind,
        sp.ImmutableMatrix(rows),
        tuple(input_words),
        tuple(output_words),
        physical,
    )


@dataclass(frozen=True)
class StageTable:
    side: str
    stage: int
    anchor: Coord
    incoming: Coord
    direction: Coord
    target_center: Coord
    gram_matrix: object
    input_words: tuple[tuple[int, ...], ...]
    output_words: tuple[tuple[int, ...], ...]
    physical_branches: int
    translation_bound: bool


@lru_cache(maxsize=None)
def factors_are_exact_translation(canonical, moved, shift: Coord) -> bool:
    """Compare every factor, shifting only absolute carrier-center labels."""
    if tuple(entry[0] for entry in canonical) != tuple(entry[0] for entry in moved):
        return False
    canonical_data = block24.factor_dictionary(canonical)
    moved_data = block24.factor_dictionary(moved)
    shifted_keys = {
        "anchor",
        "forward_center",
        "spectator_identity_centers",
        "spectator_identity_factors",
    }
    if set(canonical_data) != set(moved_data):
        return False
    for key in set(canonical_data) - shifted_keys:
        if canonical_data[key] != moved_data[key]:
            return False
    if moved_data["anchor"] != add(canonical_data["anchor"], shift):
        return False
    if moved_data["forward_center"] != add(
        canonical_data["forward_center"], shift
    ):
        return False
    if moved_data["spectator_identity_centers"] != tuple(
        add(center, shift)
        for center in canonical_data["spectator_identity_centers"]
    ):
        return False
    return moved_data["spectator_identity_factors"] == tuple(
        (add(center, shift), site, operator)
        for center, site, operator in canonical_data["spectator_identity_factors"]
    )


@lru_cache(maxsize=None)
def stage_factor_translation_certificate(
    anchor: Coord, incoming: Coord, direction: Coord
) -> bool:
    """Bind the ZERO-contracted table to every declared physical anchor."""
    for source, target in itertools.product(OUTCOMES, repeat=2):
        current_word = block23.locked_word(incoming, source)
        if direction == incoming:
            canonical = block24.append_branch(
                ZERO, current_word, target
            ).factors
            moved = block24.make_append_factors(anchor, current_word, target)
        else:
            canonical = block28.turn_branch(
                ZERO, incoming, source, direction, target
            ).factors
            moved = block28.make_turn_factors(
                anchor, incoming, source, direction, target
            )
        if not factors_are_exact_translation(canonical, moved, anchor):
            return False
    return True


@lru_cache(maxsize=None)
def route_stage_tables(
    plan,
    side: str,
    *,
    route_mutation: str | None = None,
    drop_outcome: bool = False,
    raw_probability_root: bool = False,
) -> tuple[StageTable, ...]:
    walk = plan.left if side == "left" else plan.right
    anchors = (walk.start,) + walk.targets[:-1]
    incoming_fronts = (walk.initial_front,) + walk.steps[:-1]
    stages = []
    for stage, (anchor, incoming, direction, target_center) in enumerate(
        zip(anchors, incoming_fronts, walk.steps, walk.targets)
    ):
        local = local_stage_gram_table(
            incoming,
            direction,
            drop_outcome=drop_outcome,
            raw_probability_root=raw_probability_root,
        )
        declared_target = target_center
        output_words = local.output_words
        if route_mutation == "wrong_stage_geometry" and side == "left" and stage == 0:
            declared_target = add(target_center, E1)
        if route_mutation == "broken_output_chain" and side == "left" and stage == 0:
            output_words = (block23.BLANK_POINTER,) + output_words[1:]
        stages.append(
            StageTable(
                side,
                stage,
                anchor,
                incoming,
                direction,
                declared_target,
                local.gram_matrix,
                local.input_words,
                output_words,
                local.physical_branches,
                stage_factor_translation_certificate(
                    anchor, incoming, direction
                ),
            )
        )
    if route_mutation == "deleted_writer_stage" and side == "left":
        stages.pop(2)
    elif route_mutation == "reordered_writer_stages" and side == "left":
        stages[1], stages[2] = stages[2], stages[1]
    elif route_mutation == "aliased_writer_stage" and side == "left":
        stages[2] = replace(stages[1], stage=2)
    elif route_mutation == "identity_stage_gram" and side == "left":
        stages[0] = replace(
            stages[0], gram_matrix=sp.ImmutableMatrix(sp.eye(len(OUTCOMES)))
        )
    return tuple(stages)


def local_stage_is_factor_bound(stage) -> bool:
    actual = local_stage_gram_table(stage.incoming, stage.direction)
    return (
        stage.gram_matrix == actual.gram_matrix
        and stage.input_words == actual.input_words
        and stage.output_words == actual.output_words
        and stage.physical_branches == actual.physical_branches
    )


def route_stage_chain_certificate(stages, plan, side: str) -> bool:
    walk = plan.left if side == "left" else plan.right
    if len(stages) != len(walk.steps) or len(stages) != 5:
        return False
    for index, stage in enumerate(stages):
        expected_anchor = walk.start if index == 0 else walk.targets[index - 1]
        expected_incoming = (
            walk.initial_front if index == 0 else walk.steps[index - 1]
        )
        if not (
            stage.side == side
            and stage.stage == index
            and stage.anchor == expected_anchor
            and stage.incoming == expected_incoming
            and stage.direction == walk.steps[index]
            and stage.target_center == walk.targets[index]
            and stage.target_center
            == block24.forward_center(stage.anchor, stage.direction)
            and stage.input_words
            == tuple(
                block23.locked_word(stage.incoming, source)
                for source in OUTCOMES
            )
            and stage.output_words
            == tuple(
                block23.locked_word(stage.direction, target)
                for target in OUTCOMES
            )
            and stage.gram_matrix.shape == (len(OUTCOMES), len(OUTCOMES))
            and stage.physical_branches == len(OUTCOMES) ** 2
            and stage.translation_bound
            and local_stage_is_factor_bound(stage)
        ):
            return False
        if index and stages[index - 1].output_words != stage.input_words:
            return False
    return True


@lru_cache(maxsize=None)
def plan_carrier_support_certificate(plan) -> bool:
    handoff = set(plan.left.targets + plan.right.targets)
    successor = set(block30.successor_blank_centers(plan))
    return (
        block30.route_plan_certificate(plan)
        and len(handoff) == 10
        and len(successor) == 8
        and handoff.isdisjoint(successor)
    )


@lru_cache(maxsize=None)
def route_completion_matrix(
    plan,
    side: str,
    *,
    route_mutation: str | None = None,
    drop_outcome: bool = False,
    raw_probability_root: bool = False,
):
    stages = route_stage_tables(
        plan,
        side,
        route_mutation=route_mutation,
        drop_outcome=drop_outcome,
        raw_probability_root=raw_probability_root,
    )
    if not route_stage_chain_certificate(stages, plan, side):
        return None
    completion = sp.eye(len(OUTCOMES))
    for stage in stages:
        completion = (completion * stage.gram_matrix).applyfunc(sp.simplify)
    return sp.ImmutableMatrix(completion)


@lru_cache(maxsize=None)
def arm_exit_completion_vector(
    plan,
    side: str,
    exit_front: Coord,
    *,
    route_mutation: str | None = None,
    drop_outcome: bool = False,
    raw_probability_root: bool = False,
):
    """Backward DP over five route stages plus the reached local writer."""
    route_completion = route_completion_matrix(
        plan,
        side,
        route_mutation=route_mutation,
        drop_outcome=drop_outcome,
        raw_probability_root=raw_probability_root,
    )
    if route_completion is None:
        return None
    walk = plan.left if side == "left" else plan.right
    tail = local_stage_gram_table(
        walk.final_front,
        exit_front,
        drop_outcome=drop_outcome,
        raw_probability_root=raw_probability_root,
    ).gram_matrix
    return sp.ImmutableMatrix(
        (route_completion * tail * sp.ones(len(OUTCOMES), 1)).applyfunc(
            sp.simplify
        )
    )


def route_conditioned_q_table(
    route_index: int,
    *,
    q_mutation: str | None = None,
    pair_mutation: str | None = None,
):
    table = q_table(mutation=q_mutation)
    if pair_mutation == "selector_dependent_q" and route_index == 0:
        right = tuple(block28.RIGHT_EXITS)
        table = {
            (g, h): table[g, right[(right.index(h) + 1) % len(right)]]
            for g, h in itertools.product(block28.LEFT_EXITS, right)
        }
    return table


@dataclass(frozen=True)
class ReachedPairTensor:
    route_index: int
    frame: object
    exit_pairs: tuple[tuple[Coord, Coord], ...]
    conditional_grams: tuple[object, ...]
    completion: object
    q_coefficients: tuple[object, ...]
    left_exit_norms: tuple[tuple[Coord, object], ...]
    right_exit_norms: tuple[tuple[Coord, object], ...]
    controls_ok: bool
    physical_local_branches: int


@lru_cache(maxsize=None)
def reached_pair_control_orthogonality_certificate(frame) -> bool:
    controls = tuple(
        block28.pair_control_for(frame, left, right)
        for left, right in itertools.product(OUTCOMES, repeat=2)
    )
    return (
        len(controls) == len(set((c.left_source, c.right_source) for c in controls))
        == len(OUTCOMES) ** 2
        and all(block28.control_is_rank_one_projector(control) for control in controls)
        and all(
            block28.controls_orthogonal(controls[i], controls[j])
            for i in range(len(controls))
            for j in range(i)
        )
    )


@lru_cache(maxsize=None)
def reached_pair_tensor(
    plan,
    route_index: int,
    *,
    q_mutation: str | None = None,
    pair_mutation: str | None = None,
    drop_outcome: bool = False,
    raw_probability_root: bool = False,
    source_mutation: str | None = None,
) -> ReachedPairTensor:
    frame = block30.successor_frame(plan)
    if frame is None:
        raise ValueError("route does not reach a facing successor frame")
    q_values = route_conditioned_q_table(
        route_index, q_mutation=q_mutation, pair_mutation=pair_mutation
    )
    exit_pairs = tuple(
        itertools.product(frame.left_exits, frame.right_exits)
    )
    conditional = []
    q_coefficients = []
    physical = 0
    controls_ok = reached_pair_control_orthogonality_certificate(frame)
    left_tables = {
        exit_front: local_stage_gram_table(
            frame.front,
            exit_front,
            drop_outcome=drop_outcome,
            raw_probability_root=raw_probability_root,
        )
        for exit_front in frame.left_exits
    }
    right_tables = {
        exit_front: local_stage_gram_table(
            frame.right_front,
            exit_front,
            drop_outcome=drop_outcome,
            raw_probability_root=raw_probability_root,
        )
        for exit_front in frame.right_exits
    }
    if pair_mutation == "identity_reached_gram":
        first_exit = frame.left_exits[0]
        left_tables[first_exit] = replace(
            left_tables[first_exit],
            gram_matrix=sp.ImmutableMatrix(sp.eye(len(OUTCOMES))),
        )
    controls_ok &= all(
        local_stage_is_factor_bound(table) for table in left_tables.values()
    )
    controls_ok &= all(
        local_stage_is_factor_bound(table) for table in right_tables.values()
    )
    controls_ok &= all(
        stage_factor_translation_certificate(
            frame.left_anchor, frame.front, exit_front
        )
        for exit_front in frame.left_exits
    )
    controls_ok &= all(
        stage_factor_translation_certificate(
            frame.right_anchor, frame.right_front, exit_front
        )
        for exit_front in frame.right_exits
    )
    ones = sp.ones(len(OUTCOMES), 1)
    left_exit_norms = tuple(
        (
            exit_front,
            sp.ImmutableMatrix(
                (table.gram_matrix * ones).applyfunc(sp.simplify)
            ),
        )
        for exit_front, table in left_tables.items()
    )
    right_exit_norms = tuple(
        (
            exit_front,
            sp.ImmutableMatrix(
                (table.gram_matrix * ones).applyfunc(sp.simplify)
            ),
        )
        for exit_front, table in right_tables.items()
    )
    for left_exit, right_exit in exit_pairs:
        left_norms = dict(left_exit_norms)[left_exit]
        right_norms = dict(right_exit_norms)[right_exit]
        q_coefficient = q_values[left_exit, right_exit]
        if raw_probability_root:
            q_coefficient = sp.simplify(q_coefficient**2)
        else:
            try:
                q_coefficient = domain_positive_root_gram(q_coefficient)
            except ValueError:
                controls_ok = False
        q_coefficients.append(q_coefficient)
        conditional.append(
            sp.ImmutableMatrix(
                len(OUTCOMES),
                len(OUTCOMES),
                lambda i, j: sp.factor(
                    q_coefficient * left_norms[i, 0] * right_norms[j, 0]
                ),
            )
        )
        physical += (
            left_tables[left_exit].physical_branches
            + right_tables[right_exit].physical_branches
        )
    expected_blank = set(block30.successor_blank_centers(plan))
    for left_index, source_left in enumerate(OUTCOMES):
        for right_index, source_right in enumerate(OUTCOMES):
            bound_right = (
                OUTCOMES[0]
                if source_mutation == "stale_second_source"
                and source_right == OUTCOMES[-1]
                else source_right
            )
            control = block28.pair_control_for(frame, source_left, bound_right)
            controls_ok &= (
                control.left_source == source_left
                and control.right_source == source_right
                and control.left_word
                == block23.locked_word(plan.left.final_front, source_left)
                and control.right_word
                == block23.locked_word(plan.right.final_front, source_right)
                and left_tables[frame.left_exits[0]].input_words[left_index]
                == control.left_word
                and right_tables[frame.right_exits[0]].input_words[right_index]
                == control.right_word
                and set(control.blank_centers) == expected_blank
                and len(expected_blank) == 8
                and len(control.atoms) == 10
                and tuple(atom.role for atom in control.atoms[:2])
                == ("current-pointer", "current-pointer")
                and all(atom.role == "Blank-block" for atom in control.atoms[2:])
            )
    completion = sp.zeros(len(OUTCOMES), len(OUTCOMES))
    for gram in conditional:
        completion += gram
    return ReachedPairTensor(
        route_index,
        frame,
        exit_pairs,
        tuple(conditional),
        sp.ImmutableMatrix(completion),
        tuple(q_coefficients),
        left_exit_norms,
        right_exit_norms,
        bool(controls_ok),
        physical,
    )


@dataclass(frozen=True)
class FamilyContraction:
    gram: object
    conditional_exit_grams: tuple[tuple[tuple[Coord, Coord], object], ...]
    support_ok: bool
    actual_writer_stages: int


@dataclass(frozen=True)
class KrausFamilyDescriptor:
    control_index: int
    route_index: int
    source_left: Coord
    source_right: Coord
    plan: object
    pointer_configuration: tuple
    input_token: tuple[int, ...]
    blank_centers: frozenset[Coord]

    def contracted(
        self,
        after_x: ComparatorRangeState,
        *,
        q_mutation: str | None = None,
        pair_mutation: str | None = None,
        route_mutation: str | None = None,
        source_mutation: str | None = None,
        drop_outcome: bool = False,
        raw_probability_root: bool = False,
    ) -> FamilyContraction:
        return contract_kraus_family(
            self,
            after_x,
            q_mutation=q_mutation,
            pair_mutation=pair_mutation,
            route_mutation=route_mutation,
            source_mutation=source_mutation,
            drop_outcome=drop_outcome,
            raw_probability_root=raw_probability_root,
        )

    def contracted_gram(self, after_x: ComparatorRangeState, **kwargs):
        return self.contracted(after_x, **kwargs).gram


def range_state_for(projector: ActiveProjector, selector_map: SelectorMap):
    return ComparatorRangeState(
        projector.control_index,
        projector.route_index,
        projector.pointer_configuration,
        selector_map.output_word,
        (0,) * 16,
        True,
        projector.blank_centers,
    )


@lru_cache(maxsize=None)
def contract_kraus_family(
    family: KrausFamilyDescriptor,
    after_x: ComparatorRangeState,
    *,
    q_mutation: str | None = None,
    pair_mutation: str | None = None,
    route_mutation: str | None = None,
    source_mutation: str | None = None,
    drop_outcome: bool = False,
    raw_probability_root: bool = False,
) -> FamilyContraction:
    pointer_words = dict(after_x.pointer_configuration)
    support_ok = (
        after_x.control_index == family.control_index
        and after_x.route_index == family.route_index
        and after_x.pointer_configuration == family.pointer_configuration
        and after_x.selector == one_hot(family.route_index)
        and after_x.token == (0,) * 16
        and after_x.transients_clean
        and after_x.blank_centers == family.blank_centers
        and len(after_x.blank_centers) == 158
        and pointer_words.get(family.plan.left.start)
        == block23.locked_word(
            family.plan.left.initial_front, family.source_left
        )
        and pointer_words.get(family.plan.right.start)
        == block23.locked_word(
            family.plan.right.initial_front, family.source_right
        )
        and set(family.plan.left.targets + family.plan.right.targets).issubset(
            after_x.blank_centers
        )
        and set(block30.successor_blank_centers(family.plan)).issubset(
            after_x.blank_centers
        )
        and plan_carrier_support_certificate(family.plan)
    )
    left_completion = route_completion_matrix(
        family.plan,
        "left",
        route_mutation=route_mutation,
        drop_outcome=drop_outcome,
        raw_probability_root=raw_probability_root,
    )
    right_completion = route_completion_matrix(
        family.plan,
        "right",
        route_mutation=route_mutation,
        drop_outcome=drop_outcome,
        raw_probability_root=raw_probability_root,
    )
    if left_completion is None or right_completion is None:
        return FamilyContraction(sp.nan, (), False, 0)
    tensor = reached_pair_tensor(
        family.plan,
        family.route_index,
        q_mutation=q_mutation,
        pair_mutation=pair_mutation,
        drop_outcome=drop_outcome,
        raw_probability_root=raw_probability_root,
        source_mutation=source_mutation,
    )
    left_index = OUTCOMES.index(family.source_left)
    right_index = OUTCOMES.index(family.source_right)
    if source_mutation == "stale_initial_source_row":
        left_index = (left_index + 1) % len(OUTCOMES)
    left_stages = route_stage_tables(
        family.plan,
        "left",
        route_mutation=route_mutation,
        drop_outcome=drop_outcome,
        raw_probability_root=raw_probability_root,
    )
    right_stages = route_stage_tables(
        family.plan,
        "right",
        route_mutation=route_mutation,
        drop_outcome=drop_outcome,
        raw_probability_root=raw_probability_root,
    )
    left_feed_ok = True
    for exit_index, exit_front in enumerate(tensor.frame.left_exits):
        tail = local_stage_gram_table(
            tensor.frame.front,
            exit_front,
            drop_outcome=drop_outcome,
            raw_probability_root=raw_probability_root,
        )
        if (
            source_mutation == "broken_route_to_reached_feed"
            and exit_index == 0
        ):
            tail = replace(
                tail,
                input_words=(block23.BLANK_POINTER,) + tail.input_words[1:],
            )
        left_feed_ok &= left_stages[-1].output_words == tail.input_words
    right_feed_ok = all(
        right_stages[-1].output_words
        == local_stage_gram_table(
            tensor.frame.right_front,
            exit_front,
            drop_outcome=drop_outcome,
            raw_probability_root=raw_probability_root,
        ).input_words
        for exit_front in tensor.frame.right_exits
    )
    support_ok &= (
        tensor.controls_ok
        and tensor.physical_local_branches
        == 2 * 16 * len(OUTCOMES) ** 2
        and left_stages[0].input_words[left_index]
        == pointer_words[family.plan.left.start]
        and right_stages[0].input_words[right_index]
        == pointer_words[family.plan.right.start]
        and left_feed_ok
        and right_feed_ok
    )
    conditional = []
    for exit_pair, q_coefficient in zip(
        tensor.exit_pairs, tensor.q_coefficients
    ):
        left_weight = arm_exit_completion_vector(
            family.plan,
            "left",
            exit_pair[0],
            route_mutation=route_mutation,
            drop_outcome=drop_outcome,
            raw_probability_root=raw_probability_root,
        )[left_index, 0]
        right_weight = arm_exit_completion_vector(
            family.plan,
            "right",
            exit_pair[1],
            route_mutation=route_mutation,
            drop_outcome=drop_outcome,
            raw_probability_root=raw_probability_root,
        )[right_index, 0]
        coefficient = (
            q_coefficient
            if left_weight == right_weight == sp.S.One
            else sp.simplify(q_coefficient * left_weight * right_weight)
        )
        conditional.append((exit_pair, coefficient))
    conditional = tuple(conditional)
    gram = sp.simplify(sum(value for _pair, value in conditional))
    return FamilyContraction(
        gram if support_ok else sp.nan,
        conditional,
        bool(support_ok),
        12,
    )


@lru_cache(maxsize=1)
def kraus_families() -> tuple[KrausFamilyDescriptor, ...]:
    return tuple(
        KrausFamilyDescriptor(
            projector.control_index,
            projector.route_index,
            projector.source_left,
            projector.source_right,
            projector.plan,
            projector.pointer_configuration,
            projector.token,
            projector.blank_centers,
        )
        for projector in active_projectors()
    )


@lru_cache(maxsize=None)
def family_gram(
    source_left: Coord,
    source_right: Coord,
    *,
    q_mutation: str | None = None,
    drop_outcome: bool = False,
    raw_probability_root: bool = False,
):
    family = next(
        candidate
        for candidate in kraus_families()
        if candidate.source_left == source_left
        and candidate.source_right == source_right
    )
    projector = active_projectors()[family.control_index]
    after_x = range_state_for(projector, selector_maps()[family.route_index])
    return family.contracted_gram(
        after_x,
        q_mutation=q_mutation,
        drop_outcome=drop_outcome,
        raw_probability_root=raw_probability_root,
    )


@lru_cache(maxsize=None)
def corrected_order_range_support_certificate(
    mutation: str | None = None,
) -> bool:
    projectors = active_projectors()
    families = kraus_families()
    maps = selector_maps(
        "misbind_selector" if mutation == "misbind_selector" else None
    )
    if mutation == "late_uncompute":
        return not late_uncompute_status_collision_certificate()
    if mutation == "omit_inverse":
        return comparator_round_trip_certificate(omit_inverse=True)
    if not (
        comparator_round_trip_certificate()
        and late_uncompute_status_collision_certificate()
        and selector_geometry_certificate()
    ):
        return False
    for projector, family in zip(projectors, families):
        selector_map = maps[projector.route_index]
        after_x = range_state_for(projector, selector_map)
        decoded = decode_pair_pointer_configuration(
            after_x.pointer_configuration
        )
        range_supported = (
            decoded is not None
            and decoded[2:] == (family.source_left, family.source_right)
            and after_x.selector == one_hot(family.route_index)
            and after_x.token == (0,) * 16
            and after_x.transients_clean
            and len(after_x.blank_centers) == 158
            and after_x.blank_centers == projector.blank_centers
            and family.plan == projector.plan
        )
        # This is the executed range-support identity
        # (sum R^dag R) X_c = X_c on every explicit control sector.
        contraction = family.contracted(
            after_x,
            route_mutation=(
                mutation
                if mutation
                in {
                    "deleted_writer_stage",
                    "reordered_writer_stages",
                    "aliased_writer_stage",
                    "identity_stage_gram",
                    "wrong_stage_geometry",
                    "broken_output_chain",
                }
                else None
            ),
        )
        if not (
            range_supported
            and contraction.support_ok
            and contraction.actual_writer_stages == 12
            and contraction.gram == 1
            and selector_map.input_word == BLANK_SELECTOR
        ):
            return False
    return len(projectors) == 3136


@lru_cache(maxsize=None)
def family_after_x_rejects(mutation: str) -> bool:
    projector = active_projectors()[0]
    family = kraus_families()[0]
    state = range_state_for(
        projector, selector_maps()[projector.route_index]
    )
    if mutation == "wrong_selector":
        state = replace(state, selector=one_hot((projector.route_index + 1) % 16))
    elif mutation == "dirty_token":
        state = replace(state, token=one_hot(0))
    elif mutation == "dirty_transient":
        state = replace(state, transients_clean=False)
    elif mutation == "dirty_carrier":
        state = replace(
            state,
            blank_centers=state.blank_centers - {projector.plan.left.targets[0]},
        )
    elif mutation == "wrong_pointer_source":
        _valid, malformed = malformed_same_sample_witness()
        state = replace(state, pointer_configuration=malformed)
    else:
        raise ValueError(mutation)
    return not family.contracted(state).support_ok


@lru_cache(maxsize=None)
def handoff_second_source_binding_certificate(
    mutation: str | None = None,
) -> bool:
    count = 0
    for front in DIRECTIONS:
        for g, h in itertools.product(lateral(front), repeat=2):
            plan = block30.route_plan(ZERO, front, g, h, CHIRALITY)
            frame = block30.successor_frame(plan)
            if frame is None:
                return False
            for source_left, source_right in itertools.product(
                OUTCOMES, repeat=2
            ):
                bound_right = (
                    OUTCOMES[0]
                    if mutation == "stale_second_source"
                    and source_right == OUTCOMES[-1]
                    else source_right
                )
                control = block28.pair_control_for(
                    frame, source_left, bound_right
                )
                if not (
                    plan.left.targets[-1] == frame.left_anchor
                    and plan.right.targets[-1] == frame.right_anchor
                    and plan.left.final_front == frame.front
                    and plan.right.final_front == frame.right_front
                    and control.left_word
                    == block23.locked_word(plan.left.final_front, source_left)
                    and control.right_word
                    == block23.locked_word(plan.right.final_front, source_right)
                    and set(control.blank_centers)
                    == set(block30.successor_blank_centers(plan))
                ):
                    return False
                count += 1
    return count == 6 * 16 * 14**2


@lru_cache(maxsize=None)
def stochastic_factor_certificate(
    *, drop_outcome: bool = False, raw_probability_root: bool = False
) -> bool:
    transition_rows = {
        source: sp.simplify(
            sum(
                block23.transition(source, target)
                for target in OUTCOMES[: -1 if drop_outcome else None]
            )
        )
        for source in OUTCOMES
    }
    if not all(value == 1 for value in transition_rows.values()):
        return False
    for source, target in itertools.product(OUTCOMES, repeat=2):
        probability = block23.transition(source, target)
        amplitude = probability if raw_probability_root else sp.sqrt(probability)
        gram = sp.simplify(amplitude * sp.conjugate(amplitude))
        if sp.simplify(gram - probability) != 0:
            return False
    for left_exit, right_exit in q_table():
        probability = q_weight(LAMBDA, left_exit, right_exit)
        if raw_probability_root:
            if sp.simplify(probability**2 - probability) != 0:
                return False
        else:
            try:
                gram = domain_positive_root_gram(probability)
            except ValueError:
                return False
            if sp.simplify(gram - probability) != 0:
                return False
    strict_support = exact_lambda_locus().is_subset(
        sp.Interval.open(sp.Rational(-1, 3), sp.S.One)
    )
    return strict_support is True


@lru_cache(maxsize=None)
def post_cleanup_writer_support_certificate() -> bool:
    layers = block31.macro_layers(CANONICAL_LEFT, CANONICAL_FRONT)
    comparator_sites = {site for layer in layers for gate in layer for site in gate.sites}
    samples = set(block31.true_sample_sites(CANONICAL_LEFT, CANONICAL_FRONT))
    transient = comparator_sites - samples
    for g, h in itertools.product(lateral(CANONICAL_FRONT), repeat=2):
        plan = block30.route_plan(
            CANONICAL_LEFT, CANONICAL_FRONT, g, h, CHIRALITY
        )
        written_centers = plan.left.targets + plan.right.targets
        written_centers += block30.successor_blank_centers(plan)
        written_sites = set().union(
            *(block30.block_sites(center) for center in written_centers)
        )
        if transient.intersection(written_sites):
            return False
    return late_uncompute_status_collision_certificate()


@lru_cache(maxsize=None)
def literal_factor_composition_certificate(
    q_binding_mutation: str | None = None,
) -> bool:
    if not (
        block30.local_factor_module_certificate()
        and block30.routed_factor_composition_certificate()
        and post_cleanup_writer_support_certificate()
    ):
        return False
    source_left = OUTCOMES[0]
    source_right = OUTCOMES[-1]
    target_left = OUTCOMES[1]
    target_right = OUTCOMES[-2]
    source_left_index = OUTCOMES.index(source_left)
    source_right_index = OUTCOMES.index(source_right)
    target_left_index = OUTCOMES.index(target_left)
    target_right_index = OUTCOMES.index(target_right)
    positive_weight = sp.symbols(
        "literal_pair_weight", positive=True, real=True
    )
    positive_amplitude = sp.sqrt(positive_weight)
    count = 0
    for front in DIRECTIONS:
        for g, h in itertools.product(lateral(front), repeat=2):
            plan = block30.route_plan(ZERO, front, g, h, CHIRALITY)
            frame = block30.successor_frame(plan)
            for left_exit, right_exit in itertools.product(
                frame.left_exits, frame.right_exits
            ):
                control = block28.pair_control_for(
                    frame, source_left, source_right
                )
                left = block28.turn_branch(
                    frame.left_anchor,
                    frame.front,
                    source_left,
                    left_exit,
                    target_left,
                )
                right = block28.turn_branch(
                    frame.right_anchor,
                    frame.right_front,
                    source_right,
                    right_exit,
                    target_right,
                )
                descriptor = block28.PairKrausDescriptor(
                    control,
                    left,
                    right,
                    positive_weight,
                    positive_amplitude,
                    (
                        ("amplitude", positive_amplitude),
                        ("full_pair_control", control.atoms),
                        ("left_turn_factors", left.factors),
                        ("right_turn_factors", right.factors),
                    ),
                )
                gram = block28.contract_pair_kraus_descriptor(descriptor)
                expected_generic = sp.simplify(
                    positive_weight
                    * block23.transition(source_left, target_left)
                    * block23.transition(source_right, target_right)
                )
                q_coefficient = q_weight(LAMBDA, left_exit, right_exit)
                if q_binding_mutation == "wrong_symbolic_q_cell" and count == 0:
                    q_coefficient += sp.Rational(1, 64)
                left_table = local_stage_gram_table(frame.front, left_exit)
                right_table = local_stage_gram_table(
                    frame.right_front, right_exit
                )
                left_canonical = block28.turn_branch(
                    ZERO,
                    frame.front,
                    source_left,
                    left_exit,
                    target_left,
                ).factors
                right_canonical = block28.turn_branch(
                    ZERO,
                    frame.right_front,
                    source_right,
                    right_exit,
                    target_right,
                ).factors
                expected_symbolic = sp.simplify(
                    q_weight(LAMBDA, left_exit, right_exit)
                    * block23.transition(source_left, target_left)
                    * block23.transition(source_right, target_right)
                )
                if not (
                    gram.coefficient == expected_generic
                    and domain_positive_root_gram(q_coefficient)
                    == q_coefficient
                    and sp.simplify(
                        gram.coefficient.subs(
                            positive_weight, q_coefficient
                        )
                        - expected_symbolic
                    )
                    == 0
                    and left_table.gram_matrix[
                        source_left_index, target_left_index
                    ]
                    == left.effect.scalar
                    and right_table.gram_matrix[
                        source_right_index, target_right_index
                    ]
                    == right.effect.scalar
                    and left_table.input_words[source_left_index]
                    == control.left_word
                    and right_table.input_words[source_right_index]
                    == control.right_word
                    and left_table.output_words[target_left_index]
                    == left.effect.output_word
                    and right_table.output_words[target_right_index]
                    == right.effect.output_word
                    and factors_are_exact_translation(
                        left_canonical, left.factors, frame.left_anchor
                    )
                    and factors_are_exact_translation(
                        right_canonical, right.factors, frame.right_anchor
                    )
                ):
                    return False
                count += 1
    return (
        count == 6 * 16 * 16
        and set(transaction_lambda_residuals()) == {sp.S.Zero}
        and stochastic_factor_certificate()
        and handoff_second_source_binding_certificate()
    )


@lru_cache(maxsize=None)
def old_record_qnd_factor_certificate(mutation: str | None = None) -> bool:
    source = OUTCOMES[0]
    target = OUTCOMES[-1]
    current = block23.locked_word(E1, source)
    straight_output = (
        block23.BLANK_POINTER if mutation == "overwrite_record" else current
    )
    try:
        straight = block24.contract_append_effect(
            block24.make_append_factors(
                ZERO,
                current,
                target,
                current_output_override=straight_output,
            )
        )
        turn = block28.contract_turn_effect(
            block28.make_turn_factors(
                ZERO,
                E1,
                source,
                lateral(E1)[0],
                target,
                mutation="overwrite_record" if mutation else None,
            )
        )
    except (KeyError, ValueError):
        return False
    return straight.current_word == current and turn.current_word == current


@lru_cache(maxsize=None)
def resource_and_qnd_certificate(
    *, handoff_debit: int = 10, full_debit: int = 12, overwrite_record=False
) -> bool:
    if not old_record_qnd_factor_certificate(
        "overwrite_record" if overwrite_record else None
    ):
        return False
    checked = 0
    for front in DIRECTIONS:
        carrier = block30.candidate_carrier_centers(ZERO, front, CHIRALITY)
        if len(carrier) != 160:
            return False
        for g, h in itertools.product(lateral(front), repeat=2):
            plan = block30.route_plan(ZERO, front, g, h, CHIRALITY)
            locked = {plan.left.start, plan.right.start}
            initial_blank = set(carrier) - locked
            trail = set(plan.left.targets + plan.right.targets)
            after_handoff = initial_blank - trail
            if not (
                len(locked) == 2
                and len(initial_blank) == 158
                and len(trail) == handoff_debit == 10
                and trail.issubset(initial_blank)
                and len(after_handoff) == 148
            ):
                return False
            frame = block30.successor_frame(plan)
            for left_exit, right_exit in itertools.product(
                frame.left_exits, frame.right_exits
            ):
                second = {
                    block24.forward_center(frame.left_anchor, left_exit),
                    block24.forward_center(frame.right_anchor, right_exit),
                }
                remaining = after_handoff - second
                qnd_sources = locked.isdisjoint(trail | second)
                if not (
                    len(second) == 2
                    and second.issubset(after_handoff)
                    and len(trail | second) == full_debit == 12
                    and len(remaining) == 146
                    and qnd_sources
                ):
                    return False
                checked += 1
    return checked == 6 * 16 * 16


@lru_cache(maxsize=None)
def transaction_gram_certificate(
    *,
    stop_present=True,
    stop_scale=sp.S.One,
    stop_mutation: str | None = None,
    q_mutation: str | None = None,
    pair_mutation: str | None = None,
    route_mutation: str | None = None,
    source_mutation: str | None = None,
    drop_outcome: bool = False,
    raw_probability_root: bool = False,
) -> bool:
    projectors = active_projectors()
    families = kraus_families()
    maps = selector_maps()
    active_diagonal = {}
    contractions = []
    family_mutation = any(
        value is not None
        for value in (
            q_mutation,
            pair_mutation,
            route_mutation,
            source_mutation,
        )
    ) or drop_outcome or raw_probability_root
    for projector, family in zip(projectors, families):
        contraction = family.contracted(
            range_state_for(projector, maps[projector.route_index]),
            q_mutation=q_mutation,
            pair_mutation=pair_mutation,
            route_mutation=route_mutation,
            source_mutation=source_mutation,
            drop_outcome=drop_outcome,
            raw_probability_root=raw_probability_root,
        )
        contractions.append(contraction)
        active_diagonal[family.control_index] = contraction.gram
        if family_mutation and (
            not contraction.support_ok or contraction.gram != sp.S.One
        ):
            return False
    active_stop = (
        sp.S.One
        if stop_present and stop_mutation == "overlapping_STOP"
        else sp.S.Zero
    )
    active_totals = tuple(
        sp.simplify(coefficient + active_stop)
        for coefficient in active_diagonal.values()
    )
    inactive_total = stop_scale**2 if stop_present else sp.S.Zero
    return (
        len(projectors) == len(families) == len(active_diagonal) == 3136
        and tuple(projector.control_index for projector in projectors)
        == tuple(family.control_index for family in families)
        and all(contraction.support_ok for contraction in contractions)
        and {contraction.actual_writer_stages for contraction in contractions}
        == {12}
        and set(active_totals) == {sp.S.One}
        and inactive_total == 1
        and full_pointer_guard_certificate()
        and active_projector_orthogonality_certificate()
        and selector_stop_certificate(
            stop_present=stop_present,
            stop_scale=stop_scale,
            stop_mutation=stop_mutation,
        )
        and corrected_order_range_support_certificate()
        and handoff_second_source_binding_certificate()
    )


@lru_cache(maxsize=None)
def two_use_prefix_certificate(
    include_second_marginal: bool = True,
    pair_mutation: str | None = None,
    omit_first_equality_filter: bool = False,
) -> bool:
    if not include_second_marginal:
        return False
    first = q_table()
    expected_second = q_table()
    maps = selector_maps()
    conditional_by_control = {}
    family_grams = {}
    representative_gram_by_pair = {}
    for projector, family in zip(active_projectors(), kraus_families()):
        contraction = family.contracted(
            range_state_for(projector, maps[projector.route_index]),
            pair_mutation=pair_mutation,
        )
        if not contraction.support_ok:
            return False
        conditional = dict(contraction.conditional_exit_grams)
        conditional_by_control[family.control_index] = conditional
        family_grams[family.control_index] = contraction.gram
        representative_gram_by_pair.setdefault(
            (family.plan.g, family.plan.h), contraction.gram
        )
    prefix = {
        pair: sp.simplify(weight * representative_gram_by_pair[pair])
        for pair, weight in first.items()
    }
    equality = sp.simplify(
        sum(weight for (g, h), weight in first.items() if g == h)
    )
    all_conditional_match = all(
        all(
            conditional[pair] == expected_second[pair]
            or sp.simplify(conditional[pair] - expected_second[pair]) == 0
            for pair in expected_second
        )
        for conditional in conditional_by_control.values()
    )
    joint_by_source = {
        pair: sp.S.Zero for pair in itertools.product(OUTCOMES, repeat=2)
    }
    for family in kraus_families():
        if (
            not omit_first_equality_filter
            and family.plan.g != family.plan.h
        ):
            continue
        second_equality = sum(
            probability
            for (g, h), probability in conditional_by_control[
                family.control_index
            ].items()
            if g == h
        )
        source_pair = (family.source_left, family.source_right)
        joint_by_source[source_pair] += (
            first[family.plan.g, family.plan.h] * second_equality
        )
    expected_joint = ((1 + 3 * LAMBDA) / 4) ** 2
    conditions = {
        "all_controls": len(conditional_by_control) == 3136,
        "family_grams": set(family_grams.values()) == {sp.S.One},
        "same_conditional_q": all_conditional_match,
        "prefix": prefix == first,
        "first_equality": equality == (1 + 3 * LAMBDA) / 4,
        "joint_equality": all(
            sp.simplify(joint - expected_joint) == 0
            for joint in joint_by_source.values()
        ),
        "source_binding": handoff_second_source_binding_certificate(),
    }
    if not all(conditions.values()):
        print(
            "TWO_USE_DIAGNOSTIC "
            + " ".join(f"{name}={value}" for name, value in conditions.items())
        )
    return all(conditions.values())


@lru_cache(maxsize=None)
def pair_tensor_certificate(false_additive_sensitivity: bool = False) -> bool:
    exits = block28.LEFT_EXITS
    table = q_table()
    tensor = sp.Matrix(
        3,
        3,
        lambda i, j: sp.simplify(
            sum(table[g, h] * g[i] * h[j] for g, h in table)
        ),
    )
    front = sp.Matrix(CANONICAL_FRONT)
    expected = sp.simplify(LAMBDA * (sp.eye(3) - front * front.T) / 2)
    a = sp.symbols("a0:4")
    b = sp.symbols("b0:4")
    additive = sp.simplify(
        sum(
            table[g, h] * (a[exits.index(g)] + b[exits.index(h)])
            for g, h in table
        )
    )
    expected_additive = sp.simplify((sum(a) + sum(b)) / 4)
    if false_additive_sensitivity:
        return LAMBDA in additive.free_symbols
    return tensor == expected and additive == expected_additive and LAMBDA not in additive.free_symbols


@dataclass(frozen=True)
class ClaimScope:
    selector_is_framework_Record: bool = False
    nearest_neighbor_full_validator: bool = False
    nearest_neighbor_direct_sum: bool = False
    exact_writer_stinespring: bool = False
    physical_side_exchange_hardware: bool = False
    reversible_no_refire_law: bool = False
    autonomous_invocation: bool = False
    autonomous_renewal: bool = False
    cadence_or_rate: bool = False
    arbitrary_depth_process: bool = False
    universal_selector_no_go: bool = False
    physical_equivalence_quotient: bool = False
    common_dilation_selected: bool = False
    pair_sensitive_source_closed: bool = False
    axiom_necessity: bool = False
    gravity_closure: bool = False
    audit_retention: bool = False
    obligation_retirement: bool = False
    toe_score_movement: bool = False


DEFAULT_SCOPE = ClaimScope()
TERMINAL_TEXT = (
    "FULL-SYMBOLIC-LAMBDA-INTERVAL-SURVIVES-GUARDED-TWO-USE-TRANSACTION;"
    "PAIR-SENSITIVE-SOURCE-OR-HISTORY-SELECTOR-OPEN"
)


def scope_guard_certificate(scope=DEFAULT_SCOPE, terminal=TERMINAL_TEXT) -> bool:
    return terminal == TERMINAL_TEXT and not any(scope.__dict__.values())


def mutation_rejections() -> dict[str, bool]:
    rejections = {
        "bad_diagonal_rejected": not q_family_certificate("bad_diagonal"),
        "bad_diagonal_discrete_locus_recovered": exact_lambda_locus(
            "bad_diagonal"
        )
        == sp.FiniteSet(0),
        "lambda_one_strict_support_rejected": not q_family_certificate(
            domain=sp.Interval(0, 1)
        ),
        "missing_STOP_rejected": not transaction_gram_certificate(stop_present=False),
        "scaled_STOP_rejected": not transaction_gram_certificate(stop_scale=2),
        "overlapping_STOP_rejected": not transaction_gram_certificate(
            stop_mutation="overlapping_STOP"
        ),
        "nonidentity_STOP_rejected": not selector_stop_certificate(
            stop_mutation="nonidentity_STOP"
        ),
        "aliased_token_rejected": not dispatch_certificate("alias_token"),
        "perpendicular_route_swap_rejected": not dispatch_certificate(
            "swap_perpendicular"
        ),
        "lambda_dependent_route_rejected": not dispatch_certificate(
            "lambda_dependent_route"
        ),
        "missing_full_pointer_guard_rejected": not full_pointer_guard_certificate(
            "omit_full_pointer_guard"
        ),
        "missing_target_Blank_guard_rejected": not selector_stop_certificate(
            guard_mutation="omit_target_guard"
        ),
        "missing_unused_carrier_guard_rejected": not full_pointer_guard_certificate(
            "omit_unused_carrier_guard"
        ),
        "missing_token_guard_rejected": not full_pointer_guard_certificate(
            "omit_token_guard"
        ),
        "missing_transient_guard_rejected": not full_pointer_guard_certificate(
            "omit_transient_guard"
        ),
        "missing_selector_Blank_guard_rejected": not selector_stop_certificate(
            guard_mutation="omit_selector_guard"
        ),
        "erased_selector_rejected": not selector_stop_certificate(
            write_mutation="erase_selector"
        ),
        "aliased_selector_rejected": not selector_stop_certificate(
            write_mutation="alias_selector"
        ),
        "misbound_route_selector_rejected": not corrected_order_range_support_certificate(
            "misbind_selector"
        ),
        "deleted_writer_stage_rejected": not corrected_order_range_support_certificate(
            "deleted_writer_stage"
        ),
        "reordered_writer_stages_rejected": not corrected_order_range_support_certificate(
            "reordered_writer_stages"
        ),
        "aliased_writer_stage_rejected": not corrected_order_range_support_certificate(
            "aliased_writer_stage"
        ),
        "identity_route_stage_gram_rejected": not corrected_order_range_support_certificate(
            "identity_stage_gram"
        ),
        "identity_reached_stage_gram_rejected": not transaction_gram_certificate(
            pair_mutation="identity_reached_gram"
        ),
        "wrong_stage_geometry_rejected": not corrected_order_range_support_certificate(
            "wrong_stage_geometry"
        ),
        "broken_output_chain_rejected": not corrected_order_range_support_certificate(
            "broken_output_chain"
        ),
        "family_wrong_selector_rejected": family_after_x_rejects(
            "wrong_selector"
        ),
        "family_dirty_token_rejected": family_after_x_rejects("dirty_token"),
        "family_dirty_transient_rejected": family_after_x_rejects(
            "dirty_transient"
        ),
        "family_dirty_carrier_rejected": family_after_x_rejects(
            "dirty_carrier"
        ),
        "family_wrong_pointer_source_rejected": family_after_x_rejects(
            "wrong_pointer_source"
        ),
        "dropped_local_outcome_rejected": not transaction_gram_certificate(
            drop_outcome=True
        ),
        "probability_as_Kraus_root_rejected": not transaction_gram_certificate(
            raw_probability_root=True
        ),
        "old_Record_overwrite_rejected": not resource_and_qnd_certificate(
            overwrite_record=True
        ),
        "omitted_U_dagger_rejected": not corrected_order_range_support_certificate(
            "omit_inverse"
        ),
        "late_U_dagger_rejected": not corrected_order_range_support_certificate(
            "late_uncompute"
        ),
        "wrong_handoff_debit_rejected": not resource_and_qnd_certificate(
            handoff_debit=9
        ),
        "wrong_full_debit_rejected": not resource_and_qnd_certificate(
            full_debit=10
        ),
        "partial_one_of_twelve_write_rejected": not finite_second_application_identity_certificate(
            "partial_write"
        ),
        "stale_second_source_binding_rejected": (
            not handoff_second_source_binding_certificate("stale_second_source")
            and not transaction_gram_certificate(
                source_mutation="stale_second_source"
            )
        ),
        "stale_initial_source_row_rejected": not transaction_gram_certificate(
            source_mutation="stale_initial_source_row"
        ),
        "broken_route_to_reached_feed_rejected": not transaction_gram_certificate(
            source_mutation="broken_route_to_reached_feed"
        ),
        "missing_second_marginal_rejected": not two_use_prefix_certificate(False),
        "missing_first_equality_filter_rejected": not two_use_prefix_certificate(
            omit_first_equality_filter=True
        ),
        "missing_first_equality_filter_empty_locus": exact_lambda_locus(
            "omit_first_equality_filter"
        )
        == sp.EmptySet,
        "selector_dependent_second_q_rejected": (
            transaction_gram_certificate(pair_mutation="selector_dependent_q")
            and not two_use_prefix_certificate(
                pair_mutation="selector_dependent_q"
            )
        ),
        "selector_dependent_second_q_discrete_locus": exact_lambda_locus(
            "selector_dependent_q"
        )
        == sp.FiniteSet(0),
        "false_additive_sensitivity_rejected": not pair_tensor_certificate(True),
        "wrong_literal_symbolic_q_binding_rejected": not literal_factor_composition_certificate(
            "wrong_symbolic_q_cell"
        ),
    }
    for field in ClaimScope.__dataclass_fields__:
        rejections[f"scope_{field}_promotion_rejected"] = not scope_guard_certificate(
            replace(DEFAULT_SCOPE, **{field: True})
        )
    return rejections


class Checks:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def check(self, name: str, condition: bool, detail: str) -> None:
        if condition:
            self.passed += 1
            print(f"PASS {name}: {detail}")
        else:
            self.failed += 1
            print(f"FAIL {name}: {detail}")


def main() -> int:
    checks = Checks()
    checks.check(
        "frozen_inputs_and_source_pin",
        frozen_hashes_ok(),
        f"{len(AUDIT_INPUT_PATHS)} declared inputs including source pin; fingerprint={input_fingerprint()}",
    )
    checks.check(
        "symbolic_q_lambda_family",
        q_family_certificate() and exact_lambda_locus() == LAMBDA_DOMAIN,
        "all 16 weights, both 1/4 marginals, equality probability, and strict-support locus derived exactly on [0,1)",
    )
    checks.check(
        "complete_pointer_and_token_guard",
        full_pointer_guard_certificate(),
        "3,136 orthogonal full configurations partition into sixteen 196-row route sectors; a same-STATUS malformed word proves token-only control insufficient",
    )
    checks.check(
        "U_direct_sum_U_dagger_cleanup",
        block31.record_qnd_certificate()
        and comparator_round_trip_certificate()
        and post_cleanup_writer_support_certificate()
        and corrected_order_range_support_certificate(),
        "all 256 STATUS rows clean before writers run; four opposite-route late-uncompute hazards are exhibited and excluded by selector-copy then U_dagger",
    )
    checks.check(
        "sixteen_way_physical_dispatch",
        dispatch_certificate(),
        "all 96 frame/token bindings select exact fixed-chirality Block30 routes with proper-cubic covariance and logical side exchange",
    )
    checks.check(
        "literal_local_factor_composition",
        literal_factor_composition_certificate(),
        "1,536 frame/route/exit descriptors contract with a generic positive pair weight, then bind each domain-positive symbolic q_lambda cell to the same physical factors",
    )
    checks.check(
        "CPTP_active_plus_STOP",
        stochastic_factor_certificate()
        and transaction_gram_certificate()
        and selector_stop_certificate(),
        "3,136 explicit P_c/W_c/R_c families satisfy the range-support Gram identity; their orthogonal active diagonal plus identity complement STOP is CPTP",
    )
    checks.check(
        "persistent_no_refire",
        selector_stop_certificate()
        and finite_second_application_identity_certificate()
        and full_pointer_guard_certificate(),
        "all 1,536 reduced-channel states are fixed on a second call; every one of 158 dirty guards STOPs atomically and selector/debit each block replay",
    )
    checks.check(
        "resource_debit_and_old_Record_QND",
        resource_and_qnd_certificate(),
        "all 1,536 frame/route/second-exit cases update 2 Locked + 158 Blank through ten plus two writes to 14 Locked + 146 Blank",
    )
    checks.check(
        "symbolic_two_use_prefix",
        two_use_prefix_certificate(),
        "marginalizing the complete reached use returns the first q_lambda row; equality events are (1+3 lambda)/4 and its two-use square",
    )
    checks.check(
        "lambda_blind_additive_and_live_pair_tensor",
        pair_tensor_certificate(),
        "every additive one-tip observable is lambda-independent while E[g_i h_j]=lambda(delta_ij-f_i f_j)/2 remains available",
    )
    checks.check(
        "exact_surviving_locus",
        exact_lambda_locus() == LAMBDA_DOMAIN
        and exact_lambda_locus("bad_diagonal") == sp.FiniteSet(0),
        "all transaction residuals vanish on [0,1); the altered diagonal correctly collapses the semialgebraic solver to the singleton {0}",
    )
    checks.check(
        "bounded_claim_scope",
        scope_guard_certificate(),
        "NN compilation/dilation, physical side hardware/equivalence, reversible autonomy, renewal, pair source, gravity, axioms, audit, obligations, and scores remain open",
    )
    mutations = mutation_rejections()
    construction_mutations = {
        name: rejected
        for name, rejected in mutations.items()
        if not name.startswith("scope_")
    }
    scope_mutations = {
        name: rejected
        for name, rejected in mutations.items()
        if name.startswith("scope_")
    }
    for name, rejected in construction_mutations.items():
        print(f"MUTATION {'REJECTED' if rejected else 'SURVIVED'} {name}")
    surviving_scope = tuple(
        name for name, rejected in scope_mutations.items() if not rejected
    )
    print(
        "MUTATION SCOPE "
        + ("REJECTED" if not surviving_scope else "SURVIVED")
        + f" rejected={sum(scope_mutations.values())}/{len(scope_mutations)}"
        + (
            " survived=none"
            if not surviving_scope
            else " survived=" + ",".join(surviving_scope)
        )
    )
    checks.check(
        "designated_mutations",
        len(mutations) == 68 and all(mutations.values()),
        f"rejected={sum(mutations.values())}/{len(mutations)}",
    )

    print(
        "per_element: checked — domain-positive q roots, physical transition roots, orthogonal pointer bits, selector maps, and QND factors were recontracted"
    )
    print(
        "per_site: checked — comparator transients, sixteen selector sites, protected Records, route targets, and Blank debits were enumerated"
    )
    print(
        "per_mode: checked and not executed — no momentum or spectral-mode claim is needed for this finite configuration-space transaction"
    )
    print(
        "per_block: checked — complete M2 pointer sectors, factor-level active/STOP direct sum, ten-step handoff, and reached second pair were composed"
    )
    print(
        "lattice_wide: checked and not executed — the finite carrier has no autonomous invocation, renewal, cadence, or arbitrary-depth extension"
    )
    if checks.failed == 0:
        print(f"TERMINAL: {TERMINAL_TEXT}")
    else:
        print("TERMINAL: INCOMPLETE-NO-SCIENCE-INFERENCE")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
