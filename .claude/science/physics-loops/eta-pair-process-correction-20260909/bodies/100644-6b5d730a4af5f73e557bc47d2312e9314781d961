#!/usr/bin/env python3
"""Block24 primary: one-Blank Record append and all finite cylinders.

The physical append branches are built from the Block23 product preparation
and the explicit Block22 positive Lueders roots.  This runner never allocates a
dense 2^224 matrix and never stores an expected transition table.  It proves a
global fixed-anchor channel, then uses its returned tip type and exact row
identity to certify every fixed finite straight-ray cylinder.
"""

from __future__ import annotations

import ast
import hashlib
import itertools
import sys
from dataclasses import dataclass, replace
from functools import lru_cache
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
import admissibility_d4_prior_record_live_preparation_two_event_prefix_2026_08_30 as parent  # noqa: E402


PACKET = ROOT / ".claude/science/physics-loops" / (
    "toe-source-eta-ownership-block24-self-delimiting-forward-append-"
    "history-20260830"
)
PARENT_SOURCE = (
    "scripts/admissibility_d4_prior_record_live_preparation_two_event_prefix_"
    "2026_08_30.py"
)
PARENT_SHA256 = "426488df2a431cb7d415d5e933013f7ce0826cc9514f96cd041b9fc6ff49742a"
FROZEN = {
    "GOAL.md": "0ed6b6ab796ccf785e2171fccf319d61323ed2a88d1702a23e1a4aa19ba79a8f",
    "AUTHORITY_GATE.md": "1d4a18a5140eea8e5cf1324d998810913284e94cb3c784e20fec31bd2e101a01",
    "PREFLIGHT_WITNESSES.md": "c59a047579aaedbb560391231660d2511122781d724eab2d7b6adbbce8be137b",
    "PANEL_RETURN.md": "054d7359bd3de933c491bf1734f1d92eb00c6a34d099852731e61b09b7cadf37",
    "INDEPENDENT_PREREG_ATTACK.md": "2ec5289e8b9e89369657f54ab9eed3e75f77339ceabc814ad53c485db147ffd8",
    "APPROACH_REGISTRY.md": "dd52fe35351a028f7332701671bd59bd7976ec8e5be6d8039ca9eb2b31b7ef68",
    "MUTATION_PLAN.md": "259d6f9d75df14b9b695fb5de4b819d07ce4c2cb48e706297363bf60ab81d9e3",
    "NO_GO_DISCIPLINE_CHECKLIST.md": "47bca31e14aac7006eb2e9df6b307c2e1eaa44834739f705874f2144e7377593",
}
AUDIT_INPUT_PATHS = (
    "scripts/admissibility_d4_prior_record_live_preparation_two_event_prefix_2026_08_30.py",
    ".claude/science/physics-loops/toe-source-eta-ownership-block24-self-delimiting-forward-append-history-20260830/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block24-self-delimiting-forward-append-history-20260830/AUTHORITY_GATE.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block24-self-delimiting-forward-append-history-20260830/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block24-self-delimiting-forward-append-history-20260830/PANEL_RETURN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block24-self-delimiting-forward-append-history-20260830/INDEPENDENT_PREREG_ATTACK.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block24-self-delimiting-forward-append-history-20260830/APPROACH_REGISTRY.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block24-self-delimiting-forward-append-history-20260830/MUTATION_PLAN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block24-self-delimiting-forward-append-history-20260830/NO_GO_DISCIPLINE_CHECKLIST.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block24-self-delimiting-forward-append-history-20260830/STATE.yaml",
)
AUDIT_TIMEOUT_SEC = 900

R = sp.Rational
ZERO = (0, 0, 0)
DIRECTIONS = parent.DIRECTIONS
OUTCOMES = parent.OUTCOMES
ROTATIONS = parent.ROTATIONS
DISPLACEMENT = parent.DISPLACEMENT
IDENTITY_EFFECT = (
    sp.S.One,
    {site: (sp.S.Zero,) * 3 for site in DIRECTIONS},
)


def file_sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def frozen_hashes_ok():
    return (
        all(file_sha256(PACKET / name) == expected for name, expected in FROZEN.items())
        and file_sha256(ROOT / PARENT_SOURCE) == PARENT_SHA256
    )


def add(left, right):
    return parent.add(left, right)


def scale(number, vector):
    return parent.scale(number, vector)


def forward_center(anchor, front, displacement=DISPLACEMENT):
    return add(anchor, scale(displacement, front))


def support_at(anchor):
    return parent.translate(parent.SUPPORT, anchor)


def record_selected_forward_center(anchor, current_word):
    """Decode both front and source outcome from the physical Record word."""
    decoded = parent.decode_locked_word(current_word)
    if decoded is None:
        return None
    front, _source = decoded
    return forward_center(anchor, front)


def candidate_centers(anchor):
    return {front: forward_center(anchor, front) for front in DIRECTIONS}


@lru_cache(maxsize=None)
def fixed_anchor_geometry(anchor=ZERO):
    blocks = {"current": support_at(anchor)}
    blocks.update({front: support_at(center) for front, center in candidate_centers(anchor).items()})
    values = tuple(blocks.values())
    pairwise = all(
        values[i].isdisjoint(values[j])
        for i in range(len(values))
        for j in range(i)
    )
    union = set().union(*values)
    relative = {parent.add(site, parent.negate(anchor)) for site in union}
    radius2 = max(parent.norm2(site) for site in relative)
    covariant = all(
        {parent.mat_vec(g, site) for site in relative} == relative
        for g in ROTATIONS
    )
    return {
        "blocks": blocks,
        "pairwise_disjoint": pairwise,
        "sites": len(union),
        "radius2": radius2,
        "covariant": covariant,
    }


def block_from_factor_inputs(live_maps, pointer_maps):
    live = tuple(entry[1] for entry in live_maps)
    pointer = tuple(entry[1] for entry in pointer_maps)
    return parent.BlockProduct(live, pointer)


def block_from_factor_outputs(live_maps, pointer_maps):
    live = tuple(entry[2] for entry in live_maps)
    pointer = tuple(entry[2] for entry in pointer_maps)
    return parent.BlockProduct(live, pointer)


def live_prep_maps(source):
    target = parent.block_product(parent.prepared_vectors(source), parent.BLANK_POINTER)
    return tuple(
        (site, parent.BLANK_LIVE[index], target.live[index])
        for index, site in enumerate(DIRECTIONS)
    )


def pointer_prep_maps(front):
    return parent.pointer_rank_one_maps(parent.BLANK_POINTER, parent.ready_word(front))


@lru_cache(maxsize=None)
def spectator_centers(anchor, selected_front):
    return tuple(
        candidate_centers(anchor)[front]
        for front in DIRECTIONS
        if front != selected_front
    )


@lru_cache(maxsize=None)
def spectator_identity_factors(anchor, selected_front):
    """List the identity operator on every physical spectator qubit."""
    return tuple(
        (center, site, "I_2")
        for center in spectator_centers(anchor, selected_front)
        for site in sorted(parent.SUPPORT)
    )


@dataclass(frozen=True)
class AppendEffect:
    current_word: tuple
    forward_center: tuple
    forward_input: parent.BlockProduct
    scalar: object


@dataclass(frozen=True)
class AppendBranch:
    anchor: tuple
    front: tuple
    source: tuple
    target: tuple
    current_word: tuple
    forward_center: tuple
    factors: tuple
    effect: AppendEffect


@dataclass(frozen=True)
class ValidControlEffect:
    """One actual C_(f,b) tensor B_(x+9f) term and its branch Grams."""

    front: tuple
    source: tuple
    current_word: tuple
    forward_center: tuple
    forward_input: parent.BlockProduct
    branch_grams: tuple
    gram_sum: object


def make_append_factors(
    anchor,
    current_word,
    next_outcome,
    *,
    displacement=DISPLACEMENT,
    direction_override=None,
    prepared_source_override=None,
    forward_input_override=None,
    current_output_override=None,
    root_scale=sp.S.One,
    touch_lateral=False,
    drop_writer_pointer_factor=False,
):
    decoded = parent.decode_locked_word(current_word)
    if decoded is None:
        raise ValueError("append control is not one complete Locked word")
    front, source = decoded
    direction = front if direction_override is None else direction_override
    prepared_source = source if prepared_source_override is None else prepared_source_override
    forward_input = parent.BLANK_BLOCK if forward_input_override is None else forward_input_override
    current_output = current_word if current_output_override is None else current_output_override
    center = forward_center(anchor, direction, displacement=displacement)
    live_maps = tuple(
        (site, forward_input.live[index], parent.ordered_live(parent.prepared_vectors(prepared_source))[index])
        for index, site in enumerate(DIRECTIONS)
    )
    input_pointer = forward_input.pointer
    prep_pointer = parent.pointer_rank_one_maps(input_pointer, parent.ready_word(front))
    writer_pointer = parent.pointer_rank_one_maps(
        parent.ready_word(front), parent.locked_word(front, next_outcome)
    )
    if drop_writer_pointer_factor:
        writer_pointer = writer_pointer[:-1]
    root = parent.root_operator_factor(next_outcome)
    if root_scale != 1:
        label, axes, spectrum = root
        root = (
            label,
            axes,
            tuple((signs, sp.simplify(root_value * root_scale)) for signs, root_value in spectrum),
        )
    return (
        ("anchor", anchor),
        ("current_live_identities", parent.OLD_LIVE_IDENTITIES),
        (
            "current_pointer_projectors",
            parent.pointer_rank_one_maps(current_word, current_output),
        ),
        ("forward_center", center),
        ("forward_live_prep_maps", live_maps),
        ("forward_pointer_prep_maps", prep_pointer),
        ("forward_live_root", root),
        ("forward_writer_pointer_maps", writer_pointer),
        ("spectator_identity_centers", spectator_centers(anchor, front)),
        (
            "spectator_identity_factors",
            spectator_identity_factors(anchor, front),
        ),
        ("outside_carrier_identity", "I_outside"),
        ("lateral_touch", bool(touch_lateral)),
    )


APPEND_FACTOR_KEYS = (
    "anchor",
    "current_live_identities",
    "current_pointer_projectors",
    "forward_center",
    "forward_live_prep_maps",
    "forward_pointer_prep_maps",
    "forward_live_root",
    "forward_writer_pointer_maps",
    "spectator_identity_centers",
    "spectator_identity_factors",
    "outside_carrier_identity",
    "lateral_touch",
)


def factor_dictionary(factors):
    return {entry[0]: entry[1] for entry in factors}


@lru_cache(maxsize=None)
def contracted_physical_root(label):
    """Cache the exact physical contraction, never an expected branch value."""
    root = parent.root_operator_factor(label)
    contracted = parent.contract_root_adjoint_root(root)
    if not parent.effect_equal(contracted, parent.effect(label)):
        raise ValueError("physical root failed to reconstruct its effect")
    return contracted


@lru_cache(maxsize=None)
def contract_append_effect(factors):
    """Contract L^dag L using only the stored physical branch factors."""
    if tuple(entry[0] for entry in factors) != APPEND_FACTOR_KEYS:
        raise ValueError("append factor list is missing, duplicated, or extended")
    data = factor_dictionary(factors)
    current_maps = data["current_pointer_projectors"]
    current_input = tuple(entry[1] for entry in current_maps)
    current_output = tuple(entry[2] for entry in current_maps)
    current_sites = tuple(entry[0] for entry in current_maps)
    decoded = parent.decode_locked_word(current_input)
    if (
        decoded is None
        or current_output != current_input
        or current_sites != parent.POINTER_ORDER
    ):
        raise ValueError("current Record control/output is not exact QND")
    front, _source = decoded
    anchor = data["anchor"]
    if data["current_live_identities"] != parent.OLD_LIVE_IDENTITIES:
        raise ValueError("current live factor is not the complete identity")
    if {
        site for site, _input, _output in current_maps
    } != parent.POINTER:
        raise ValueError("current pointer factor is not physically complete")
    if data["forward_center"] != record_selected_forward_center(anchor, current_input):
        raise ValueError("forward target is not selected by current Record content")
    live_maps = data["forward_live_prep_maps"]
    prep_pointer_maps = data["forward_pointer_prep_maps"]
    if tuple(entry[0] for entry in live_maps) != DIRECTIONS:
        raise ValueError("forward live preparation is not on the physical sites")
    if tuple(entry[0] for entry in prep_pointer_maps) != parent.POINTER_ORDER:
        raise ValueError("forward pointer preparation is not on the physical sites")
    forward_input = block_from_factor_inputs(live_maps, prep_pointer_maps)
    if forward_input != parent.BLANK_BLOCK:
        raise ValueError("append input is not the exact complete Blank block")
    prepared = block_from_factor_outputs(live_maps, prep_pointer_maps)
    if parent.decode_ready_word(prepared.pointer) != front:
        raise ValueError("prepared pointer does not return the decoded Ready front")
    writer_pointer = data["forward_writer_pointer_maps"]
    if len(writer_pointer) != 26:
        raise ValueError("writer pointer map is not physically complete")
    if tuple(entry[0] for entry in writer_pointer) != parent.POINTER_ORDER:
        raise ValueError("writer pointer map is not on the physical sites")
    writer_input = tuple(entry[1] for entry in writer_pointer)
    writer_output = tuple(entry[2] for entry in writer_pointer)
    if writer_input != prepared.pointer:
        raise ValueError("writer pointer input does not match preparation output")
    target_decoded = parent.decode_locked_word(writer_output)
    root = data["forward_live_root"]
    if target_decoded is None or target_decoded != (front, root[0]):
        raise ValueError("writer output/root label mismatch")
    expected_spectators = spectator_identity_factors(anchor, front)
    if data["spectator_identity_factors"] != expected_spectators:
        raise ValueError("spectator identity extension is incomplete or altered")
    if not all(
        operator == "I_2"
        for _center, _site, operator in data["spectator_identity_factors"]
    ):
        raise ValueError("a spectator factor is not identity")
    if data["outside_carrier_identity"] != "I_outside":
        raise ValueError("outside-carrier identity extension is absent")
    root_effect = (
        contracted_physical_root(root[0])
        if root == parent.root_operator_factor(root[0])
        else parent.contract_root_adjoint_root(root)
    )
    scalar = parent.expectation_from_effect_data(
        root_effect, parent.live_dictionary(prepared.live)
    )
    return AppendEffect(
        current_word=current_input,
        forward_center=data["forward_center"],
        forward_input=forward_input,
        scalar=sp.simplify(scalar),
    )


@dataclass(frozen=True)
class CoherentAppendMutant:
    """The forbidden single Kraus K=L_left+L_right."""

    left_factors: tuple
    right_factors: tuple


@dataclass(frozen=True)
class CoherentCrossContraction:
    left_input_word: tuple
    right_input_word: tuple
    left_output_word: tuple
    right_output_word: tuple
    left_forward_center: tuple
    right_forward_center: tuple
    cross_amplitude: object
    cross_norm2: object


def contract_coherent_append_cross(mutant):
    """Contract K |left><right| K^dag from both literal append factors."""
    left_data = factor_dictionary(mutant.left_factors)
    right_data = factor_dictionary(mutant.right_factors)
    left_effect = contract_append_effect(mutant.left_factors)
    right_effect = contract_append_effect(mutant.right_factors)
    left_input = tuple(
        entry[1] for entry in left_data["current_pointer_projectors"]
    )
    right_input = tuple(
        entry[1] for entry in right_data["current_pointer_projectors"]
    )
    left_current_output = tuple(
        entry[2] for entry in left_data["current_pointer_projectors"]
    )
    right_current_output = tuple(
        entry[2] for entry in right_data["current_pointer_projectors"]
    )
    if (
        left_input == right_input
        or left_current_output != left_input
        or right_current_output != right_input
    ):
        raise ValueError("coherent mutant does not join two distinct QND controls")
    left_target_output = tuple(
        entry[2] for entry in left_data["forward_writer_pointer_maps"]
    )
    right_target_output = tuple(
        entry[2] for entry in right_data["forward_writer_pointer_maps"]
    )
    if (
        parent.decode_locked_word(left_target_output) is None
        or parent.decode_locked_word(right_target_output) is None
        or left_data["forward_center"] == right_data["forward_center"]
    ):
        raise ValueError("coherent mutant outputs are not two physical branches")
    amplitude = sp.simplify(
        sp.sqrt(left_effect.scalar) * sp.sqrt(right_effect.scalar)
    )
    return CoherentCrossContraction(
        left_input_word=left_input,
        right_input_word=right_input,
        left_output_word=left_target_output,
        right_output_word=right_target_output,
        left_forward_center=left_data["forward_center"],
        right_forward_center=right_data["forward_center"],
        cross_amplitude=amplitude,
        cross_norm2=sp.simplify(amplitude * sp.conjugate(amplitude)),
    )


@lru_cache(maxsize=None)
def append_branch(anchor, current_word, next_outcome):
    decoded = parent.decode_locked_word(current_word)
    if decoded is None:
        raise ValueError("append branch requires a physical complete Record word")
    front, source = decoded
    factors = make_append_factors(anchor, current_word, next_outcome)
    return AppendBranch(
        anchor=anchor,
        front=front,
        source=source,
        target=next_outcome,
        current_word=current_word,
        forward_center=record_selected_forward_center(anchor, current_word),
        factors=factors,
        effect=contract_append_effect(factors),
    )


def all_append_branches(anchor=ZERO):
    return tuple(
        append_branch(anchor, parent.locked_word(front, source), target)
        for front in DIRECTIONS
        for source in OUTCOMES
        for target in OUTCOMES
    )


@lru_cache(maxsize=None)
def branch_effect_is_recontracted(branch):
    try:
        contracted = contract_append_effect(branch.factors)
    except (KeyError, ValueError):
        return False
    return (
        contracted.current_word == branch.effect.current_word
        and contracted.forward_center == branch.effect.forward_center
        and contracted.forward_input == branch.effect.forward_input
        and sp.simplify(contracted.scalar - branch.effect.scalar) == 0
    )


@lru_cache(maxsize=None)
def derived_append_scalar(front, source, target):
    branch = append_branch(
        ZERO, parent.locked_word(front, source), target
    )
    if not branch_effect_is_recontracted(branch):
        raise ValueError("append branch effect is not factor-derived")
    return contract_append_effect(branch.factors).scalar


def valid_control_effect(front, source, group):
    if len(group) != 14 or {branch.target for branch in group} != set(OUTCOMES):
        return None
    if not all(
        branch.front == front
        and branch.source == source
        and branch_effect_is_recontracted(branch)
        for branch in group
    ):
        return None
    current_word = parent.locked_word(front, source)
    forward = forward_center(ZERO, front)
    if not all(
        branch.effect.current_word == current_word
        and branch.effect.forward_center == forward
        and branch.effect.forward_input == parent.BLANK_BLOCK
        for branch in group
    ):
        return None
    grams = tuple(branch.effect.scalar for branch in group)
    return ValidControlEffect(
        front=front,
        source=source,
        current_word=current_word,
        forward_center=forward,
        forward_input=parent.BLANK_BLOCK,
        branch_grams=grams,
        gram_sum=sp.simplify(sum(grams)),
    )


def valid_control_overlap(left, right):
    """Product overlap of the actual current-Record/forward-Blank controls."""
    current_overlap = parent.pointer_overlap(
        left.current_word, right.current_word
    )
    if left.current_word == right.current_word:
        same_forward_factor = (
            left.forward_center == right.forward_center
            and left.forward_input == right.forward_input == parent.BLANK_BLOCK
        )
        return current_overlap * int(same_forward_factor)
    return current_overlap


@lru_cache(maxsize=None)
def append_factorization_is_physical(branch):
    if tuple(entry[0] for entry in branch.factors) != APPEND_FACTOR_KEYS:
        return False
    data = factor_dictionary(branch.factors)
    current_maps = data["current_pointer_projectors"]
    live_maps = data["forward_live_prep_maps"]
    prep_pointer = data["forward_pointer_prep_maps"]
    writer_pointer = data["forward_writer_pointer_maps"]
    root = data["forward_live_root"]
    prepared = block_from_factor_outputs(live_maps, prep_pointer)
    spectator_factors = data["spectator_identity_factors"]
    expected_spectator_factors = spectator_identity_factors(
        branch.anchor, branch.front
    )
    current_relative_sites = {
        site for site, _operator in data["current_live_identities"]
    } | {site for site, _input, _output in current_maps}
    forward_relative_sites = {
        site for site, _input, _output in live_maps
    } | {
        site for site, _input, _output in prep_pointer
    } | {
        site for site, _input, _output in writer_pointer
    }
    return (
        data["anchor"] == branch.anchor
        and data["current_live_identities"] == parent.OLD_LIVE_IDENTITIES
        and len(current_maps) == 26
        and tuple(entry[0] for entry in current_maps) == parent.POINTER_ORDER
        and tuple(entry[1] for entry in current_maps) == branch.current_word
        and tuple(entry[2] for entry in current_maps) == branch.current_word
        and len(live_maps) == 6
        and tuple(entry[0] for entry in live_maps) == DIRECTIONS
        and block_from_factor_inputs(live_maps, prep_pointer) == parent.BLANK_BLOCK
        and prepared
        == parent.block_product(parent.prepared_vectors(branch.source), parent.ready_word(branch.front))
        and len(prep_pointer) == len(writer_pointer) == 26
        and tuple(entry[0] for entry in prep_pointer) == parent.POINTER_ORDER
        and tuple(entry[0] for entry in writer_pointer) == parent.POINTER_ORDER
        and tuple(entry[1] for entry in writer_pointer) == parent.ready_word(branch.front)
        and tuple(entry[2] for entry in writer_pointer)
        == parent.locked_word(branch.front, branch.target)
        and root == parent.root_operator_factor(branch.target)
        and len(root[1]) == 6
        and len(root[2]) == 64
        and all(
            sp.simplify(parent.norm2(axis) - 1) == 0
            for _site, axis in root[1]
        )
        and all(
            value.is_real is True and value.is_positive is True
            for _signs, value in root[2]
        )
        and branch.forward_center == forward_center(branch.anchor, branch.front)
        and data["forward_center"] == branch.forward_center
        and len(data["spectator_identity_centers"]) == 5
        and set(data["spectator_identity_centers"])
        == set(candidate_centers(branch.anchor).values()) - {branch.forward_center}
        and len(spectator_factors) == 5 * 32
        and spectator_factors == expected_spectator_factors
        and all(operator == "I_2" for _center, _site, operator in spectator_factors)
        and current_relative_sites == parent.SUPPORT
        and forward_relative_sites == parent.SUPPORT
        and physical_append_carrier_certificate(branch.anchor, branch.front)
        and data["outside_carrier_identity"] == "I_outside"
        and data["lateral_touch"] is False
        and branch.effect.current_word == branch.current_word
        and branch.effect.forward_center == branch.forward_center
        and branch.effect.forward_input == parent.BLANK_BLOCK
    )


@lru_cache(maxsize=None)
def physical_append_carrier_certificate(anchor, front):
    """Cache geometry only at its true ``(anchor, front)`` dependency."""
    current_sites = {add(anchor, site) for site in parent.SUPPORT}
    selected_center = forward_center(anchor, front)
    forward_sites = {
        add(selected_center, site) for site in parent.SUPPORT
    }
    spectator_sites = {
        add(center, site)
        for center, site, _operator in spectator_identity_factors(anchor, front)
    }
    represented = current_sites | forward_sites | spectator_sites
    expected_blocks = fixed_anchor_geometry(anchor)["blocks"]
    expected = set().union(*expected_blocks.values())
    return len(represented) == 224 and represented == expected


def projector_reduce(expression, symbol):
    polynomial = sp.Poly(sp.expand(expression), symbol)
    relation = sp.Poly(symbol ** 2 - symbol, symbol)
    return sp.simplify(sp.rem(polynomial, relation).as_expr())


@lru_cache(maxsize=None)
def append_valid_sector_eigenvalue(current_word, forward_is_blank):
    decoded = parent.decode_locked_word(current_word)
    if decoded is None or not forward_is_blank:
        return sp.S.Zero
    _front, source = decoded
    return sp.simplify(
        sum(
            append_branch(ZERO, current_word, target).effect.scalar
            for target in OUTCOMES
        )
    )


def append_record_heisenberg_value(observable_word, input_word, forward_is_blank):
    branch_value = sp.S.Zero
    if input_word == observable_word and forward_is_blank:
        branch_value = sum(
            append_branch(ZERO, input_word, target).effect.scalar
            for target in OUTCOMES
        )
    p_value = append_valid_sector_eigenvalue(input_word, forward_is_blank)
    stop_value = sp.simplify((1 - p_value) ** 2 * int(input_word == observable_word))
    return sp.simplify(branch_value + stop_value)


def append_matrix_unit_survival(left_word, right_word, forward_is_blank):
    branch_value = sp.S.Zero
    if left_word == right_word and forward_is_blank:
        branch_value = sum(
            append_branch(ZERO, left_word, target).effect.scalar
            for target in OUTCOMES
        )
    stop_left = 1 - append_valid_sector_eigenvalue(left_word, forward_is_blank)
    stop_right = 1 - append_valid_sector_eigenvalue(right_word, forward_is_blank)
    return sp.simplify(branch_value + stop_left * stop_right)


@lru_cache(maxsize=None)
def root_covariance_certificate(label, rotation):
    moved_label = parent.mat_vec(rotation, label)
    original_constant, original_coefficients = parent.effect(label)
    moved_constant, moved_coefficients = parent.effect(moved_label)
    coefficients_ok = original_constant == moved_constant and all(
        parent.mat_vec(rotation, original_coefficients[site])
        == moved_coefficients[parent.mat_vec(rotation, site)]
        for site in DIRECTIONS
    )
    original_norms, original_values = parent.spectral_resolution(label)
    moved_norms, moved_values = parent.spectral_resolution(moved_label)
    norms_ok = all(
        original_norms[site] == moved_norms[parent.mat_vec(rotation, site)]
        for site in DIRECTIONS
    )
    spectra_ok = True
    for signs, value in original_values.items():
        sign_by_site = {site: signs[index] for index, site in enumerate(DIRECTIONS)}
        moved_sign_by_site = {
            parent.mat_vec(rotation, site): sign for site, sign in sign_by_site.items()
        }
        moved_signs = tuple(moved_sign_by_site[site] for site in DIRECTIONS)
        spectra_ok &= sp.simplify(
            sp.sqrt(value) - sp.sqrt(moved_values[moved_signs])
        ) == 0
    return coefficients_ok and norms_ok and spectra_ok


@lru_cache(maxsize=None)
def current_factor_rotation_certificate(
    current_live,
    current_pointer,
    moved_live,
    moved_pointer,
    rotation,
):
    return {
        (parent.mat_vec(rotation, site), operator)
        for site, operator in current_live
    } == set(moved_live) and {
        (parent.mat_vec(rotation, site), input_bit, output_bit)
        for site, input_bit, output_bit in current_pointer
    } == set(moved_pointer)


@lru_cache(maxsize=None)
def preparation_factor_rotation_certificate(
    live_maps,
    prep_pointer,
    moved_live_maps,
    moved_prep_pointer,
    rotation,
):
    return {
        (
            parent.mat_vec(rotation, site),
            parent.mat_vec(rotation, input_vector),
            parent.mat_vec(rotation, output_vector),
        )
        for site, input_vector, output_vector in live_maps
    } == set(moved_live_maps) and {
        (parent.mat_vec(rotation, site), input_bit, output_bit)
        for site, input_bit, output_bit in prep_pointer
    } == set(moved_prep_pointer)


@lru_cache(maxsize=None)
def writer_factor_rotation_certificate(
    writer_pointer,
    root_axes,
    moved_writer_pointer,
    moved_root_axes,
    rotation,
):
    return {
        (parent.mat_vec(rotation, site), input_bit, output_bit)
        for site, input_bit, output_bit in writer_pointer
    } == set(moved_writer_pointer) and {
        (
            parent.mat_vec(rotation, site),
            parent.mat_vec(rotation, axis),
        )
        for site, axis in root_axes
    } == set(moved_root_axes)


@lru_cache(maxsize=None)
def spectator_factor_rotation_certificate(
    spectator_factors, moved_spectator_factors, rotation
):
    return {
        (
            parent.mat_vec(rotation, center),
            parent.mat_vec(rotation, site),
            operator,
        )
        for center, site, operator in spectator_factors
    } == set(moved_spectator_factors)


def append_branch_covariance_certificate(branch, rotation):
    moved_anchor = parent.mat_vec(rotation, branch.anchor)
    moved_front = parent.mat_vec(rotation, branch.front)
    moved_source = parent.mat_vec(rotation, branch.source)
    moved_target = parent.mat_vec(rotation, branch.target)
    moved_word = parent.rotate_word(branch.current_word, rotation)
    comparison = append_branch(moved_anchor, moved_word, moved_target)
    data = factor_dictionary(branch.factors)
    moved_data = factor_dictionary(comparison.factors)
    return (
        comparison.front == moved_front
        and comparison.source == moved_source
        and comparison.target == moved_target
        and comparison.current_word == moved_word
        and comparison.forward_center
        == parent.mat_vec(rotation, branch.forward_center)
        and parent.rotate_block_product(parent.BLANK_BLOCK, rotation)
        == parent.BLANK_BLOCK
        and current_factor_rotation_certificate(
            data["current_live_identities"],
            data["current_pointer_projectors"],
            moved_data["current_live_identities"],
            moved_data["current_pointer_projectors"],
            rotation,
        )
        and preparation_factor_rotation_certificate(
            data["forward_live_prep_maps"],
            data["forward_pointer_prep_maps"],
            moved_data["forward_live_prep_maps"],
            moved_data["forward_pointer_prep_maps"],
            rotation,
        )
        and writer_factor_rotation_certificate(
            data["forward_writer_pointer_maps"],
            data["forward_live_root"][1],
            moved_data["forward_writer_pointer_maps"],
            moved_data["forward_live_root"][1],
            rotation,
        )
        and parent.rotate_word(parent.ready_word(branch.front), rotation)
        == parent.ready_word(moved_front)
        and parent.rotate_word(parent.locked_word(branch.front, branch.target), rotation)
        == parent.locked_word(moved_front, moved_target)
        and spectator_factor_rotation_certificate(
            data["spectator_identity_factors"],
            moved_data["spectator_identity_factors"],
            rotation,
        )
        and data["outside_carrier_identity"]
        == moved_data["outside_carrier_identity"]
        == "I_outside"
        and root_covariance_certificate(branch.target, rotation)
        and sp.simplify(
            comparison.effect.scalar - branch.effect.scalar
        ) == 0
    )


@lru_cache(maxsize=None)
def translation_covariance_certificate():
    a0, a1, a2, t0, t1, t2 = sp.symbols("a0 a1 a2 t0 t1 t2")
    anchor = (a0, a1, a2)
    translation = (t0, t1, t2)
    moved_anchor = add(anchor, translation)
    valid = True
    for front in DIRECTIONS:
        word = parent.locked_word(front, OUTCOMES[0])
        data = factor_dictionary(
            make_append_factors(anchor, word, OUTCOMES[-1])
        )
        moved_data = factor_dictionary(
            make_append_factors(moved_anchor, word, OUTCOMES[-1])
        )
        valid &= data["forward_center"] == forward_center(anchor, front)
        valid &= moved_data["forward_center"] == add(
            data["forward_center"], translation
        )
        valid &= {
            add(center, translation)
            for center in data["spectator_identity_centers"]
        } == set(moved_data["spectator_identity_centers"])
        valid &= {
            (add(center, translation), site, operator)
            for center, site, operator in data["spectator_identity_factors"]
        } == set(moved_data["spectator_identity_factors"])
        for key in (
            "current_live_identities",
            "current_pointer_projectors",
            "forward_live_prep_maps",
            "forward_pointer_prep_maps",
            "forward_live_root",
            "forward_writer_pointer_maps",
            "outside_carrier_identity",
            "lateral_touch",
        ):
            valid &= data[key] == moved_data[key]
    return valid


def append_channel_certificate(branches=None, deep=True):
    branches = all_append_branches() if branches is None else tuple(branches)
    grouped = {
        (front, source): tuple(
            branch
            for branch in branches
            if branch.front == front and branch.source == source
        )
        for front in DIRECTIONS
        for source in OUTCOMES
    }
    all_words = tuple(parent.locked_word(front, source) for front in DIRECTIONS for source in OUTCOMES)
    control_terms = tuple(
        term
        for (front, source), group in grouped.items()
        for term in (valid_control_effect(front, source, group),)
        if term is not None
    )
    controls_orthogonal = (
        len(control_terms) == 84
        and all(
            valid_control_overlap(control_terms[i], control_terms[j])
            == int(i == j)
            for i in range(len(control_terms))
            for j in range(len(control_terms))
        )
    )
    rows = {
        key: sp.simplify(sum(branch.effect.scalar for branch in group))
        for key, group in grouped.items()
    }
    derived_effects = all(
        branch_effect_is_recontracted(branch)
        and sp.simplify(
            branch.effect.scalar - parent.transition(branch.source, branch.target)
        ) == 0
        for branch in branches
    )
    actual_gram_sum = (
        len(control_terms) == 84
        and all(term.gram_sum == 1 for term in control_terms)
        and tuple(
            (
                term.current_word,
                term.forward_center,
                term.forward_input,
            )
            for term in control_terms
        )
        == tuple(
            (
                parent.locked_word(front, source),
                forward_center(ZERO, front),
                parent.BLANK_BLOCK,
            )
            for front in DIRECTIONS
            for source in OUTCOMES
        )
    )
    p = sp.symbols("P_valid", commutative=True)
    p_valid_projector = controls_orthogonal and actual_gram_sum
    completeness = (
        p_valid_projector
        and projector_reduce(p + (1 - p) ** 2 - 1, p) == 0
    )
    reference_row, reference_column = sp.symbols(
        "r_append s_append", integer=True, nonnegative=True
    )
    delta = sp.KroneckerDelta(reference_row, reference_column)
    reference = (
        actual_gram_sum
        and controls_orthogonal
        and sp.simplify(
            delta * projector_reduce(p + (1 - p) ** 2, p) - delta
        )
        == 0
    )
    qnd = coherent_blank_dephased = coherent_complement_preserved = covariance = True
    if deep:
        qnd_words = all_words + (parent.BLANK_POINTER,)
        qnd = all(
            append_record_heisenberg_value(observable, input_word, forward_blank)
            == int(observable == input_word)
            for observable in all_words
            for input_word in qnd_words
            for forward_blank in (True, False)
        )
        coherent_blank_dephased = all(
            append_matrix_unit_survival(left, right, True) == 0
            for left, right in itertools.combinations(all_words, 2)
        )
        coherent_complement_preserved = all(
            append_matrix_unit_survival(left, right, False) == 1
            for left, right in itertools.combinations(all_words, 2)
        )
        covariance = all(
            append_branch_covariance_certificate(branch, rotation)
            for branch in branches
            for rotation in ROTATIONS
        )
    target_nonblank = all(
        parent.pointer_overlap(
            parent.BLANK_POINTER,
            parent.locked_word(branch.front, branch.target),
        ) == 0
        for branch in branches
    )
    return {
        "branch_count": len(branches) == 6 * 14 * 14,
        "fourteen_per_control": all(len(group) == 14 for group in grouped.values()),
        "factor_complete": all(append_factorization_is_physical(branch) for branch in branches),
        "derived_effects": derived_effects,
        "positive_effects": all(branch.effect.scalar.is_positive is True for branch in branches),
        "stochastic_rows": all(value == 1 for value in rows.values()),
        "controls_orthogonal": controls_orthogonal,
        "actual_physical_gram_sum": actual_gram_sum,
        "p_valid_projector": p_valid_projector,
        "kraus_complete": completeness,
        "arbitrary_reference": reference,
        "classical_record_qnd": qnd,
        "coherent_code_not_qnd": coherent_blank_dephased and coherent_complement_preserved,
        "branch_covariance": covariance and translation_covariance_certificate(),
        "target_nonblank": target_nonblank,
    }


@dataclass(frozen=True)
class FactorizedCylinderEffect:
    """Exact E_first times a factor-contracted conditional scalar."""

    initial_label: tuple
    initial_effect: tuple
    conditional_scalar: object


@dataclass(frozen=True)
class ThreeEventBranch:
    front: tuple
    first: tuple
    second: tuple
    third: tuple
    first_root: tuple
    first_pointer_maps: tuple
    first_append: AppendBranch
    second_append: AppendBranch
    composite_factors: tuple
    input_domain: tuple
    joint_effect: FactorizedCylinderEffect


@lru_cache(maxsize=None)
def make_three_event_composite_factors(front, first, second, third):
    x0 = ZERO
    x1 = forward_center(x0, front)
    first_append = append_branch(
        x0, parent.locked_word(front, first), second
    )
    second_append = append_branch(
        x1, parent.locked_word(front, second), third
    )
    return (
        ("first_anchor", x0),
        ("first_live_root", parent.root_operator_factor(first)),
        (
            "first_pointer_maps",
            parent.pointer_rank_one_maps(
                parent.ready_word(front), parent.locked_word(front, first)
            ),
        ),
        ("first_append_factors", first_append.factors),
        ("second_append_factors", second_append.factors),
        ("outside_chain_identity", "I_outside"),
    )


@lru_cache(maxsize=None)
def contract_three_event_composite(composite_factors):
    """Contract the literal sequential factors, including both handoffs."""
    data = factor_dictionary(composite_factors)
    first_root = data["first_live_root"]
    first_pointer_maps = data["first_pointer_maps"]
    first_input = tuple(entry[1] for entry in first_pointer_maps)
    first_output = tuple(entry[2] for entry in first_pointer_maps)
    front = parent.decode_ready_word(first_input)
    first_decoded = parent.decode_locked_word(first_output)
    if front is None or first_decoded is None or first_decoded[0] != front:
        raise ValueError("first writer pointer handoff is not physical")
    first = first_decoded[1]
    if first_root != parent.root_operator_factor(first):
        raise ValueError("first writer root and pointer outcome disagree")
    first_append_data = factor_dictionary(data["first_append_factors"])
    second_append_data = factor_dictionary(data["second_append_factors"])
    if tuple(
        entry[1] for entry in first_append_data["current_pointer_projectors"]
    ) != first_output:
        raise ValueError("first writer does not feed the first append control")
    first_append_effect = contract_append_effect(data["first_append_factors"])
    first_append_output = tuple(
        entry[2]
        for entry in first_append_data["forward_writer_pointer_maps"]
    )
    if tuple(
        entry[1] for entry in second_append_data["current_pointer_projectors"]
    ) != first_append_output:
        raise ValueError("first append does not feed the second append control")
    if first_append_data["forward_center"] != second_append_data["anchor"]:
        raise ValueError("append handoff is not bound to the returned tip")
    if second_append_data["forward_center"] != forward_center(
        second_append_data["anchor"], front
    ):
        raise ValueError("second append does not select the next physical block")
    if data["outside_chain_identity"] != "I_outside":
        raise ValueError("composite omits the outside-chain identity")
    second_append_effect = contract_append_effect(data["second_append_factors"])
    return FactorizedCylinderEffect(
        initial_label=first,
        initial_effect=contracted_physical_root(first),
        conditional_scalar=sp.simplify(
            first_append_effect.scalar * second_append_effect.scalar
        ),
    )


@lru_cache(maxsize=None)
def three_event_branch(front, first, second, third):
    x0 = ZERO
    x1 = forward_center(x0, front)
    x2 = forward_center(x1, front)
    first_append = append_branch(x0, parent.locked_word(front, first), second)
    second_append = append_branch(x1, parent.locked_word(front, second), third)
    first_root = parent.root_operator_factor(first)
    composite_factors = make_three_event_composite_factors(
        front, first, second, third
    )
    joint_effect = contract_three_event_composite(composite_factors)
    return ThreeEventBranch(
        front=front,
        first=first,
        second=second,
        third=third,
        first_root=first_root,
        first_pointer_maps=parent.pointer_rank_one_maps(
            parent.ready_word(front), parent.locked_word(front, first)
        ),
        first_append=first_append,
        second_append=second_append,
        composite_factors=composite_factors,
        input_domain=(
            (x0, parent.ready_word(front)),
            (x1, parent.BLANK_BLOCK),
            (x2, parent.BLANK_BLOCK),
        ),
        joint_effect=joint_effect,
    )


def three_event_branch_is_physical(branch):
    x0 = ZERO
    x1 = forward_center(x0, branch.front)
    x2 = forward_center(x1, branch.front)
    first_pointer_output = tuple(entry[2] for entry in branch.first_pointer_maps)
    first_append_input = branch.first_append.current_word
    second_append_input = branch.second_append.current_word
    first_append_output = parent.locked_word(branch.front, branch.second)
    return (
        len(branch.first_root[1]) == 6
        and len(branch.first_root[2]) == 64
        and branch.joint_effect.initial_effect
        == contracted_physical_root(branch.first)
        and len(branch.first_pointer_maps) == 26
        and tuple(entry[1] for entry in branch.first_pointer_maps)
        == parent.ready_word(branch.front)
        and first_pointer_output == parent.locked_word(branch.front, branch.first)
        and first_pointer_output == first_append_input
        and append_factorization_is_physical(branch.first_append)
        and append_factorization_is_physical(branch.second_append)
        and branch.first_append.anchor == x0
        and branch.first_append.forward_center == x1
        and first_append_output == second_append_input
        and branch.second_append.anchor == x1
        and branch.second_append.forward_center == x2
        and branch.composite_factors
        == make_three_event_composite_factors(
            branch.front, branch.first, branch.second, branch.third
        )
        and contract_three_event_composite(branch.composite_factors)
        == branch.joint_effect
        and branch.joint_effect.initial_label == branch.first
        and branch.joint_effect.initial_effect
        == contracted_physical_root(branch.first)
        and branch.input_domain
        == (
            (x0, parent.ready_word(branch.front)),
            (x1, parent.BLANK_BLOCK),
            (x2, parent.BLANK_BLOCK),
        )
    )


def all_three_event_branches(front):
    return tuple(
        three_event_branch(front, first, second, third)
        for first in OUTCOMES
        for second in OUTCOMES
        for third in OUTCOMES
    )


@lru_cache(maxsize=None)
def three_event_scalar_certificate(first, second, third, actual_scalar):
    expected = sp.simplify(
        parent.transition(first, second) * parent.transition(second, third)
    )
    return sp.simplify(actual_scalar - expected) == 0


@lru_cache(maxsize=None)
def three_event_reference_scalar_certificate(
    first, second, third, actual_scalar
):
    reference_row, reference_column = sp.symbols(
        "r_three s_three", integer=True, nonnegative=True
    )
    delta = sp.KroneckerDelta(reference_row, reference_column)
    expected = sp.simplify(
        parent.transition(first, second) * parent.transition(second, third)
    )
    return sp.simplify(delta * (actual_scalar - expected)) == 0


def three_event_certificate():
    valid = True
    branch_count = 0
    reference_row, reference_column = sp.symbols(
        "r_three s_three", integer=True, nonnegative=True
    )
    delta = sp.KroneckerDelta(reference_row, reference_column)
    for front in DIRECTIONS:
        branches = all_three_event_branches(front)
        branch_count += len(branches)
        valid &= len(branches) == 14 ** 3
        valid &= all(three_event_branch_is_physical(branch) for branch in branches)
        valid &= all(
            branch.joint_effect.initial_label == branch.first
            and branch.joint_effect.initial_effect
            == contracted_physical_root(branch.first)
            and three_event_scalar_certificate(
                branch.first,
                branch.second,
                branch.third,
                branch.joint_effect.conditional_scalar,
            )
            for branch in branches
        )
        valid &= all(
            three_event_reference_scalar_certificate(
                branch.first,
                branch.second,
                branch.third,
                branch.joint_effect.conditional_scalar,
            )
            for branch in branches
        )
        for first in OUTCOMES:
            for second in OUTCOMES:
                third_sum = sp.simplify(
                    sum(
                        three_event_branch(
                            front, first, second, third
                        ).joint_effect.conditional_scalar
                        for third in OUTCOMES
                    )
                )
                first_append_scalar = contract_append_effect(
                    append_branch(
                        ZERO, parent.locked_word(front, first), second
                    ).factors
                ).scalar
                valid &= sp.simplify(
                    third_sum - first_append_scalar
                ) == 0
                valid &= sp.simplify(
                    delta * third_sum - delta * first_append_scalar
                ) == 0
            suffix_sum = sp.simplify(
                sum(
                    three_event_branch(
                        front, first, second, third
                    ).joint_effect.conditional_scalar
                    for second in OUTCOMES
                    for third in OUTCOMES
                )
            )
            valid &= suffix_sum == 1
            valid &= sp.simplify(delta * suffix_sum - delta) == 0
        total = parent.summed_effects(
            [
                parent.effect_scaled(
                    first,
                    sp.simplify(
                        sum(
                            three_event_branch(
                                front, first, second, third
                            ).joint_effect.conditional_scalar
                            for second in OUTCOMES
                            for third in OUTCOMES
                        )
                    ),
                )
                for first in OUTCOMES
            ]
        )
        valid &= parent.effect_equal(total, IDENTITY_EFFECT)
        reference_total = parent.scale_effect_data(total, delta)
        valid &= parent.effect_equal(
            reference_total, parent.scale_effect_data(IDENTITY_EFFECT, delta)
        )
    return valid and branch_count == 6 * 14 ** 3


def chain_centers(front, length, origin=ZERO):
    return tuple(forward_center(origin, front, displacement=DISPLACEMENT * j) for j in range(length))


def chain_support_certificate():
    axial_span = max(
        abs(site[parent.axis_index(DIRECTIONS[0])] - other[parent.axis_index(DIRECTIONS[0])])
        for site in parent.SUPPORT
        for other in parent.SUPPORT
    )
    # Cubic symmetry makes the same span hold on every signed axis.  Since
    # adjacent centers differ by nine and the support span is eight, every
    # pair of distinct straight-ray blocks is disjoint at arbitrary distance.
    analytic = axial_span == 8 and DISPLACEMENT == 9
    finite_witness = True
    for front in DIRECTIONS:
        centers = chain_centers(front, 65)
        supports = [support_at(center) for center in centers]
        finite_witness &= all(
            supports[i].isdisjoint(supports[j])
            for i in range(len(supports))
            for j in range(i)
        )
    return analytic and finite_witness


@dataclass(frozen=True)
class PhysicalHistoryPrefix:
    front: tuple
    outcomes: tuple
    record_blocks: tuple
    next_blank_center: tuple
    next_blank_block: parent.BlockProduct
    composite_factors: tuple
    joint_effect: tuple


@lru_cache(maxsize=None)
def make_history_composite_factors(front, outcomes):
    if not outcomes:
        raise ValueError("a Record history has at least one outcome")
    centers = chain_centers(front, len(outcomes))
    append_steps = tuple(
        append_branch(
            centers[index],
            parent.locked_word(front, outcomes[index]),
            outcomes[index + 1],
        ).factors
        for index in range(len(outcomes) - 1)
    )
    return (
        ("initial_anchor", centers[0]),
        ("initial_root", parent.root_operator_factor(outcomes[0])),
        (
            "initial_pointer_maps",
            parent.pointer_rank_one_maps(
                parent.ready_word(front),
                parent.locked_word(front, outcomes[0]),
            ),
        ),
        ("append_steps", append_steps),
        ("outside_history_identity", "I_outside"),
    )


@lru_cache(maxsize=None)
def contract_history_composite(composite_factors):
    """Contract a finite physical prefix solely from its sequential factors."""
    data = factor_dictionary(composite_factors)
    initial_pointer = data["initial_pointer_maps"]
    initial_input = tuple(entry[1] for entry in initial_pointer)
    current_word = tuple(entry[2] for entry in initial_pointer)
    front = parent.decode_ready_word(initial_input)
    decoded = parent.decode_locked_word(current_word)
    if front is None or decoded is None or decoded[0] != front:
        raise ValueError("initial writer does not return a complete Record")
    initial_outcome = decoded[1]
    initial_root = data["initial_root"]
    if initial_root != parent.root_operator_factor(initial_outcome):
        raise ValueError("initial root does not match its physical Record")
    effect = contracted_physical_root(initial_outcome)
    expected_anchor = data["initial_anchor"]
    for append_factors in data["append_steps"]:
        append_data = factor_dictionary(append_factors)
        append_input = tuple(
            entry[1] for entry in append_data["current_pointer_projectors"]
        )
        if append_input != current_word:
            raise ValueError("history append is not fed by the returned Record")
        if append_data["anchor"] != expected_anchor:
            raise ValueError("history append anchor skips the returned tip")
        append_effect = contract_append_effect(append_factors)
        effect = parent.scale_effect_data(effect, append_effect.scalar)
        current_word = tuple(
            entry[2]
            for entry in append_data["forward_writer_pointer_maps"]
        )
        expected_anchor = append_data["forward_center"]
    if data["outside_history_identity"] != "I_outside":
        raise ValueError("finite history omits the identity on older Records")
    return effect


@lru_cache(maxsize=None)
def physical_history_prefix(front, outcomes):
    outcomes = tuple(outcomes)
    centers = chain_centers(front, len(outcomes))
    factors = make_history_composite_factors(front, outcomes)
    return PhysicalHistoryPrefix(
        front=front,
        outcomes=outcomes,
        record_blocks=tuple(
            (center, parent.locked_word(front, outcome))
            for center, outcome in zip(centers, outcomes)
        ),
        next_blank_center=forward_center(centers[-1], front),
        next_blank_block=parent.BLANK_BLOCK,
        composite_factors=factors,
        joint_effect=contract_history_composite(factors),
    )


def history_eligible_centers(prefix):
    """Derive eligibility from actual Locked/Blank block contents."""
    records = dict(prefix.record_blocks)
    eligible = []
    for center, word in prefix.record_blocks:
        decoded = parent.decode_locked_word(word)
        if decoded is None:
            continue
        front, _outcome = decoded
        ahead = forward_center(center, front)
        if ahead in records:
            forward_is_exact_blank = False
        elif ahead == prefix.next_blank_center:
            forward_is_exact_blank = (
                prefix.next_blank_block == parent.BLANK_BLOCK
                and parent.block_overlap(
                    prefix.next_blank_block, parent.BLANK_BLOCK
                )
                == 1
            )
        else:
            forward_is_exact_blank = False
        if append_valid_sector_eigenvalue(word, forward_is_exact_blank) == 1:
            eligible.append(center)
    return tuple(eligible)


def history_prefix_is_physical(prefix):
    centers = chain_centers(prefix.front, len(prefix.outcomes))
    expected_records = tuple(
        (center, parent.locked_word(prefix.front, outcome))
        for center, outcome in zip(centers, prefix.outcomes)
    )
    return (
        bool(prefix.outcomes)
        and prefix.record_blocks == expected_records
        and prefix.next_blank_center == forward_center(centers[-1], prefix.front)
        and prefix.next_blank_block == parent.BLANK_BLOCK
        and prefix.composite_factors
        == make_history_composite_factors(prefix.front, prefix.outcomes)
        and parent.effect_equal(
            contract_history_composite(prefix.composite_factors),
            prefix.joint_effect,
        )
        and history_eligible_centers(prefix) == (centers[-1],)
        and len(
            set().union(
                *(support_at(center) for center in centers + (prefix.next_blank_center,))
            )
        )
        == 32 * (len(centers) + 1)
    )


@lru_cache(maxsize=None)
def append_preserves_arbitrary_prior_records(branch):
    """Current, predecessor, and all older Records receive exact identities."""
    data = factor_dictionary(branch.factors)
    backward_center = forward_center(branch.anchor, parent.negate(branch.front))
    backward_factors = tuple(
        item
        for item in data["spectator_identity_factors"]
        if item[0] == backward_center
    )
    return (
        data["current_live_identities"] == parent.OLD_LIVE_IDENTITIES
        and tuple(entry[1] for entry in data["current_pointer_projectors"])
        == tuple(entry[2] for entry in data["current_pointer_projectors"])
        == branch.current_word
        and len(backward_factors) == 32
        and all(operator == "I_2" for _center, _site, operator in backward_factors)
        and data["outside_carrier_identity"] == "I_outside"
    )


def unique_tip_induction_step_certificate():
    """Prove one eligible tip is mapped to one eligible translated tip."""
    return all(
        append_preserves_arbitrary_prior_records(branch)
        and append_valid_sector_eigenvalue(branch.current_word, True) == 1
        and parent.pointer_overlap(
            parent.BLANK_POINTER,
            parent.locked_word(branch.front, branch.target),
        )
        == 0
        and append_valid_sector_eigenvalue(branch.current_word, False) == 0
        and append_valid_sector_eigenvalue(
            parent.locked_word(branch.front, branch.target), True
        )
        == 1
        and branch.forward_center == forward_center(branch.anchor, branch.front)
        for branch in all_append_branches()
    )


def physical_history_effect(front, outcomes):
    if not outcomes:
        raise ValueError("a Record history has at least one outcome")
    return physical_history_prefix(front, tuple(outcomes)).joint_effect


@dataclass(frozen=True)
class FactorizedGenericEffect:
    """Exact arbitrary prefix effect times a branch-derived scalar and I_R."""

    base_effect: tuple
    scalar: object
    reference_delta: object


@dataclass(frozen=True)
class GenericPhysicalPrefix:
    """Induction hypothesis at arbitrary depth and translated tip anchor."""

    record_count: object
    tip_anchor: tuple
    front: tuple
    last_outcome: tuple
    tip_word: tuple
    next_blank_block: parent.BlockProduct
    factorized_effect: FactorizedGenericEffect
    unique_eligible_tip: bool
    earlier_records_qnd: bool


def generic_effect_data():
    return (
        sp.Symbol("H_constant"),
        {
            site: tuple(
                sp.Symbol(f"H_{site_index}_{axis_index}")
                for axis_index in range(3)
            )
            for site_index, site in enumerate(DIRECTIONS)
        },
    )


def extend_generic_physical_prefix(prefix, target):
    """Apply the literal append factors to an arbitrary induction prefix."""
    decoded = parent.decode_locked_word(prefix.tip_word)
    if decoded != (prefix.front, prefix.last_outcome):
        raise ValueError("generic prefix tip is not its claimed complete Record")
    if prefix.next_blank_block != parent.BLANK_BLOCK:
        raise ValueError("generic prefix does not supply the exact next Blank")
    if not prefix.unique_eligible_tip or not prefix.earlier_records_qnd:
        raise ValueError("generic prefix does not satisfy the induction hypothesis")
    branch = append_branch(prefix.tip_anchor, prefix.tip_word, target)
    if not (
        append_factorization_is_physical(branch)
        and branch_effect_is_recontracted(branch)
        and append_preserves_arbitrary_prior_records(branch)
    ):
        raise ValueError("generic extension branch is not a physical QND append")
    contracted = contract_append_effect(branch.factors)
    old_tip_disables = (
        parent.pointer_overlap(
            parent.BLANK_POINTER,
            parent.locked_word(prefix.front, target),
        )
        == 0
        and append_valid_sector_eigenvalue(prefix.tip_word, False) == 0
    )
    returned_tip_accepts = append_valid_sector_eigenvalue(
        parent.locked_word(prefix.front, target), True
    ) == 1
    old_effect = prefix.factorized_effect
    return GenericPhysicalPrefix(
        record_count=prefix.record_count + 1,
        tip_anchor=branch.forward_center,
        front=prefix.front,
        last_outcome=target,
        tip_word=parent.locked_word(prefix.front, target),
        next_blank_block=parent.BLANK_BLOCK,
        factorized_effect=FactorizedGenericEffect(
            base_effect=old_effect.base_effect,
            scalar=sp.simplify(old_effect.scalar * contracted.scalar),
            reference_delta=old_effect.reference_delta,
        ),
        unique_eligible_tip=(
            prefix.unique_eligible_tip
            and old_tip_disables
            and returned_tip_accepts
        ),
        earlier_records_qnd=(
            prefix.earlier_records_qnd
            and append_preserves_arbitrary_prior_records(branch)
        ),
    )


def factorized_generic_sum_certificate(prefix_effect, extension_effects):
    """Check exact coefficientwise system/reference recovery on one common H."""
    extension_effects = tuple(extension_effects)
    if not extension_effects:
        return False
    if any(
        effect.base_effect != prefix_effect.base_effect
        or effect.reference_delta != prefix_effect.reference_delta
        for effect in extension_effects
    ):
        return False
    constant, coefficients = prefix_effect.base_effect
    if set(coefficients) != set(DIRECTIONS) or any(
        len(coefficients[site]) != 3 for site in DIRECTIONS
    ):
        return False
    components = (constant,) + tuple(
        coefficients[site][axis]
        for site in DIRECTIONS
        for axis in range(3)
    )
    difference = sp.simplify(
        sum(effect.scalar for effect in extension_effects)
        - prefix_effect.scalar
    )
    reference_difference = sp.simplify(
        prefix_effect.reference_delta * difference
    )
    return (
        len(components) == 19
        and len(set(components)) == 19
        and all(isinstance(component, sp.Symbol) for component in components)
        and difference == 0
        and reference_difference == 0
        and all(sp.simplify(difference * component) == 0 for component in components)
        and all(
            sp.simplify(reference_difference * component) == 0
            for component in components
        )
    )


def generic_prefix_extension_certificate():
    """Check P(n)->P(n+1) coefficientwise for symbolic n, anchor, and I_R."""
    n = sp.Symbol("n_history", integer=True, positive=True)
    x0, x1, x2 = sp.symbols("x_history_0 x_history_1 x_history_2")
    anchor = (x0, x1, x2)
    effect_data = generic_effect_data()
    reference_row, reference_column = sp.symbols(
        "r_history s_history", integer=True, nonnegative=True
    )
    delta = sp.KroneckerDelta(reference_row, reference_column)
    prior_weight = sp.Symbol("w_history")
    valid = True
    for front in DIRECTIONS:
        for source in OUTCOMES:
            prefix = GenericPhysicalPrefix(
                record_count=n,
                tip_anchor=anchor,
                front=front,
                last_outcome=source,
                tip_word=parent.locked_word(front, source),
                next_blank_block=parent.BLANK_BLOCK,
                factorized_effect=FactorizedGenericEffect(
                    base_effect=effect_data,
                    scalar=prior_weight,
                    reference_delta=delta,
                ),
                unique_eligible_tip=True,
                earlier_records_qnd=True,
            )
            labeled_extensions = tuple(
                (target, extend_generic_physical_prefix(prefix, target))
                for target in OUTCOMES
            )
            valid &= len(labeled_extensions) == 14
            valid &= (
                tuple(target for target, _extended in labeled_extensions)
                == OUTCOMES
            )
            extensions = tuple(
                extended for _target, extended in labeled_extensions
            )
            for target, extended in labeled_extensions:
                scalar = contract_append_effect(
                    append_branch(
                        anchor, prefix.tip_word, target
                    ).factors
                ).scalar
                valid &= extended.record_count == n + 1
                valid &= extended.tip_anchor == forward_center(anchor, front)
                valid &= extended.tip_word == parent.locked_word(front, target)
                valid &= extended.next_blank_block == parent.BLANK_BLOCK
                valid &= extended.unique_eligible_tip
                valid &= extended.earlier_records_qnd
                valid &= extended.factorized_effect.base_effect == effect_data
                valid &= (
                    extended.factorized_effect.reference_delta == delta
                )
                valid &= sp.simplify(
                    extended.factorized_effect.scalar
                    - prior_weight * scalar
                ) == 0
            valid &= factorized_generic_sum_certificate(
                prefix.factorized_effect,
                tuple(
                    extended.factorized_effect for extended in extensions
                )
            )
    return valid


def finite_history_induction_certificate():
    returned_type = all(
        parent.decode_locked_word(
            tuple(
                entry[2]
                for entry in factor_dictionary(branch.factors)["forward_writer_pointer_maps"]
            )
        )
        == (branch.front, branch.target)
        and parent.pointer_overlap(
            parent.BLANK_POINTER,
            parent.locked_word(branch.front, branch.target),
        )
        == 0
        for branch in all_append_branches()
    )
    one_step_rows = all(
        sp.simplify(
            sum(
                derived_append_scalar(front, source, target)
                for target in OUTCOMES
            )
            - 1
        )
        == 0
        for front in DIRECTIONS
        for source in OUTCOMES
    )
    generic_prefix = generic_prefix_extension_certificate()
    base_prefixes = all(
        history_prefix_is_physical(
            physical_history_prefix(front, (first,))
        )
        for front in DIRECTIONS
        for first in OUTCOMES
    )
    unique_tip_induction = unique_tip_induction_step_certificate()
    old_tip_stops = all(
        append_valid_sector_eigenvalue(parent.locked_word(front, source), False) == 0
        for front in DIRECTIONS
        for source in OUTCOMES
    )
    new_tip_accepts = all(
        append_valid_sector_eigenvalue(parent.locked_word(front, source), True) == 1
        for front in DIRECTIONS
        for source in OUTCOMES
    )
    constructed_prefixes = True
    for front in DIRECTIONS:
        for outcomes in (
            OUTCOMES[:1],
            OUTCOMES[:2],
            OUTCOMES[:3],
            OUTCOMES[:5],
            tuple(reversed(OUTCOMES[:5])),
        ):
            prefix = physical_history_prefix(front, tuple(outcomes))
            derived = prefix.joint_effect
            expected = parent.effect_scaled(
                outcomes[0],
                sp.prod(
                    parent.transition(source, target)
                    for source, target in zip(outcomes, outcomes[1:])
                ),
            )
            constructed_prefixes &= history_prefix_is_physical(prefix)
            constructed_prefixes &= parent.effect_equal(derived, expected)
    return (
        returned_type
        and one_step_rows
        and generic_prefix
        and chain_support_certificate()
        and base_prefixes
        and unique_tip_induction
        and old_tip_stops
        and new_tip_accepts
        and constructed_prefixes
    )


def mutation_rejections():
    """Execute altered channels/rules and require their named invariant to fail."""
    front = (1, 0, 0)
    backward = (-1, 0, 0)
    source = (1, 0, 0)
    target = (1, 1, 1)
    current_word = parent.locked_word(front, source)

    def contraction_rejects(**changes):
        try:
            factors = make_append_factors(ZERO, current_word, target, **changes)
            contract_append_effect(factors)
        except (ValueError, KeyError):
            return True
        return False

    def replace_factor_field(factors, key, value):
        return tuple(
            (key, value) if entry[0] == key else entry
            for entry in factors
        )

    def altered_factors_rejected(factors):
        try:
            contract_append_effect(factors)
        except (ValueError, KeyError):
            return True
        return False

    r8_rejected = contraction_rejects(displacement=8)
    backward_rejected = contraction_rejects(direction_override=backward)
    fixed_target_rejected = contraction_rejects(direction_override=(0, 1, 0))
    outcome_routed_label = (0, 0, 1)

    def outcome_selected_direction(next_outcome):
        selected_axis = parent.axis_index(next_outcome)
        return tuple(
            next_outcome[selected_axis] if index == selected_axis else 0
            for index in range(3)
        )

    outcome_target_rejected = altered_factors_rejected(
        make_append_factors(
            ZERO,
            current_word,
            outcome_routed_label,
            direction_override=outcome_selected_direction(
                outcome_routed_label
            ),
        )
    )

    locked_forward = parent.BlockProduct(
        parent.BLANK_LIVE, parent.locked_word(front, source)
    )
    nonblank_rejected = contraction_rejects(forward_input_override=locked_forward)
    overwrite_rejected = contraction_rejects(
        current_output_override=parent.BLANK_POINTER
    )
    pointer_drop_rejected = contraction_rejects(drop_writer_pointer_factor=True)

    future_factors = make_append_factors(
        ZERO,
        current_word,
        target,
        prepared_source_override=target,
    )
    future_effect = contract_append_effect(future_factors)
    future_rejected = (
        future_effect.scalar != parent.transition(source, target)
        and block_from_factor_outputs(
            factor_dictionary(future_factors)["forward_live_prep_maps"],
            factor_dictionary(future_factors)["forward_pointer_prep_maps"],
        )
        != parent.block_product(parent.prepared_vectors(source), parent.ready_word(front))
    )

    baseline_factors = make_append_factors(ZERO, current_word, target)
    baseline_data = factor_dictionary(baseline_factors)
    relocated_writer_maps = list(
        baseline_data["forward_writer_pointer_maps"]
    )
    _writer_site, writer_input, writer_output = relocated_writer_maps[0]
    relocated_writer_maps[0] = (
        (99, 99, 99),
        writer_input,
        writer_output,
    )
    relocated_writer_factors = replace_factor_field(
        baseline_factors,
        "forward_writer_pointer_maps",
        tuple(relocated_writer_maps),
    )
    relocated_writer_site_rejected = altered_factors_rejected(
        relocated_writer_factors
    )
    prep_source = (1, 1, 1)
    prep_target = (1, 0, 0)
    prep_word = parent.locked_word(front, prep_source)
    prep_baseline_factors = make_append_factors(
        ZERO, prep_word, prep_target
    )
    prep_baseline_data = factor_dictionary(prep_baseline_factors)
    prep_root_effect = contracted_physical_root(prep_target)
    prepared_maps = list(prep_baseline_data["forward_live_prep_maps"])
    changed_live_index = next(
        index
        for index, (site, _input, output) in enumerate(prepared_maps)
        if output != parent.BLANK_LIVE[index]
        and sp.simplify(
            parent.dot(
                prep_root_effect[1][site],
                parent.add(output, parent.scale(-1, parent.BLANK_LIVE[index])),
            )
        )
        != 0
    )
    changed_site, changed_input, _changed_output = prepared_maps[changed_live_index]
    prepared_maps[changed_live_index] = (
        changed_site,
        changed_input,
        parent.BLANK_LIVE[changed_live_index],
    )
    one_blank_live_factor = replace_factor_field(
        prep_baseline_factors, "forward_live_prep_maps", tuple(prepared_maps)
    )
    one_blank_effect = contract_append_effect(one_blank_live_factor)
    one_blank_factor_rejected = (
        block_from_factor_outputs(
            factor_dictionary(one_blank_live_factor)["forward_live_prep_maps"],
            factor_dictionary(one_blank_live_factor)["forward_pointer_prep_maps"],
        )
        != parent.block_product(
            parent.prepared_vectors(prep_source), parent.ready_word(front)
        )
        and one_blank_effect.scalar != parent.transition(prep_source, prep_target)
    )

    future_factors_data = factor_dictionary(future_factors)
    future_rejected &= future_factors_data["forward_live_prep_maps"] != baseline_data[
        "forward_live_prep_maps"
    ]

    physical_root = baseline_data["forward_live_root"]
    perturbed_spectrum = list(physical_root[2])
    signs, root_value = perturbed_spectrum[0]
    perturbed_spectrum[0] = (signs, sp.simplify(R(2) * root_value))
    one_sector_root = (
        physical_root[0],
        physical_root[1],
        tuple(perturbed_spectrum),
    )
    one_sector_root_factors = replace_factor_field(
        baseline_factors, "forward_live_root", one_sector_root
    )
    one_root_sector_rejected = altered_factors_rejected(one_sector_root_factors)

    spectator_factors = list(baseline_data["spectator_identity_factors"])
    backward_center = forward_center(ZERO, backward)
    lateral_index = next(
        index
        for index, (center, _site, _operator) in enumerate(spectator_factors)
        if center != backward_center
    )
    lateral_center, lateral_site, _identity = spectator_factors[lateral_index]
    lateral_factors_projector = list(spectator_factors)
    lateral_factors_projector[lateral_index] = (
        lateral_center,
        lateral_site,
        ("rank_one", parent.radial_bloch(lateral_site, 0)),
    )
    lateral_factors = replace_factor_field(
        baseline_factors,
        "spectator_identity_factors",
        tuple(lateral_factors_projector),
    )
    lateral_touch_rejected = altered_factors_rejected(lateral_factors)

    baseline = list(all_append_branches())
    dropped_source = [
        branch
        for branch in baseline
        if not (branch.front == front and branch.source == source)
    ]
    dropped_source_report = append_channel_certificate(dropped_source, deep=False)
    dropped_source_rejected = not (
        dropped_source_report["branch_count"]
        and dropped_source_report["fourteen_per_control"]
        and dropped_source_report["stochastic_rows"]
    )

    duplicated = list(baseline)
    duplicated[0] = duplicated[14]
    duplicate_report = append_channel_certificate(duplicated, deep=False)
    duplicate_control_rejected = not (
        duplicate_report["fourteen_per_control"]
        and duplicate_report["stochastic_rows"]
    )

    dropped_outcome = [
        branch
        for branch in baseline
        if not (
            branch.front == front
            and branch.source == source
            and branch.target == target
        )
    ]
    dropped_outcome_report = append_channel_certificate(dropped_outcome, deep=False)
    dropped_outcome_rejected = not dropped_outcome_report["stochastic_rows"]

    p = sp.symbols("P_mutant", commutative=True)
    omit_stop_rejected = projector_reduce(p - 1, p) != 0
    scaled_stop_rejected = projector_reduce(
        p + (1 - R(1, 2) * p) ** 2 - 1, p
    ) != 0

    physical_branch = append_branch(ZERO, current_word, target)
    rotation = next(g for g in ROTATIONS if parent.mat_vec(g, front) != front)
    moved_word = parent.rotate_word(current_word, rotation)
    moved_target = parent.mat_vec(rotation, target)
    correctly_moved_branch = append_branch(ZERO, moved_word, moved_target)
    labels_only_factors = correctly_moved_branch.factors
    labels_only_factors = replace_factor_field(
        labels_only_factors,
        "forward_center",
        physical_branch.forward_center,
    )
    labels_only_factors = replace_factor_field(
        labels_only_factors,
        "spectator_identity_centers",
        factor_dictionary(physical_branch.factors)["spectator_identity_centers"],
    )
    labels_only_factors = replace_factor_field(
        labels_only_factors,
        "spectator_identity_factors",
        factor_dictionary(physical_branch.factors)["spectator_identity_factors"],
    )
    labels_only_branch = replace(
        correctly_moved_branch,
        forward_center=physical_branch.forward_center,
        factors=labels_only_factors,
    )
    labels_only_covariance_rejected = (
        altered_factors_rejected(labels_only_factors)
        and not append_factorization_is_physical(labels_only_branch)
    )

    def altered_eligibility(
        word,
        forward_block,
        *,
        accept_nonblank=False,
        require_predecessor=False,
        predecessor_present=True,
    ):
        if parent.decode_locked_word(word) is None:
            return sp.S.Zero
        exact_blank = parent.block_overlap(
            forward_block, parent.BLANK_BLOCK
        ) == 1
        domain = (exact_blank or accept_nonblank) and (
            predecessor_present or not require_predecessor
        )
        if not domain:
            return sp.S.Zero
        return sp.simplify(
            sum(
                append_branch(ZERO, word, outcome).effect.scalar
                for outcome in OUTCOMES
            )
        )

    nonblank_eligibility_rejected = (
        altered_eligibility(
            current_word, locked_forward, accept_nonblank=True
        )
        == 1
        and parent.block_overlap(locked_forward, parent.BLANK_BLOCK) == 0
        and append_valid_sector_eigenvalue(current_word, False) == 0
    )
    returned_tip_rejected = (
        altered_eligibility(
            parent.locked_word(front, target),
            parent.BLANK_BLOCK,
            require_predecessor=True,
            predecessor_present=False,
        )
        == 0
        and append_valid_sector_eigenvalue(parent.locked_word(front, target), True) == 1
    )
    consumed_reuse_rejected = (
        altered_factors_rejected(
            make_append_factors(
                ZERO,
                current_word,
                target,
                forward_input_override=locked_forward,
            )
        )
        and parent.block_overlap(locked_forward, parent.BLANK_BLOCK) == 0
    )

    squared_prefix_rows = {
        source_label: sp.simplify(
            sum(
                append_branch(
                    ZERO, parent.locked_word(front, source_label), target_label
                ).effect.scalar
                ** 2
                for target_label in OUTCOMES
            )
        )
        for source_label in OUTCOMES
    }
    squared_prefix_rejected = any(value != 1 for value in squared_prefix_rows.values())

    depth_n_prefix = physical_history_prefix(front, (source, target))
    unsummed_depth_n_plus_one = physical_history_prefix(
        front, (source, target, OUTCOMES[0])
    )
    induction_without_stochasticity_rejected = (
        history_prefix_is_physical(depth_n_prefix)
        and history_prefix_is_physical(unsummed_depth_n_plus_one)
        and not parent.effect_equal(
            unsummed_depth_n_plus_one.joint_effect,
            depth_n_prefix.joint_effect,
        )
    )

    backward_spectators = list(baseline_data["spectator_identity_factors"])
    backward_index = next(
        index
        for index, (center, _site, _operator) in enumerate(backward_spectators)
        if center == backward_center
    )
    back_center, back_site, _back_identity = backward_spectators[backward_index]
    back_projector = parent.radial_bloch(back_site, 0)
    backward_spectators[backward_index] = (
        back_center, back_site, ("rank_one", back_projector)
    )
    backward_mutant_factors = replace_factor_field(
        baseline_factors,
        "spectator_identity_factors",
        tuple(backward_spectators),
    )
    backward_dependency_rejected = (
        altered_factors_rejected(backward_mutant_factors)
        and parent.pure_overlap(back_projector, parent.radial_bloch(back_site, 0))
        != parent.pure_overlap(back_projector, parent.radial_bloch(back_site, 1))
    )
    lateral_projector = parent.radial_bloch(lateral_site, 0)
    lateral_dependency_rejected = (
        lateral_touch_rejected
        and parent.pure_overlap(
            lateral_projector, parent.radial_bloch(lateral_site, 0)
        )
        != parent.pure_overlap(
            lateral_projector, parent.radial_bloch(lateral_site, 1)
        )
    )

    missing_effect_sum = parent.summed_effects(
        [parent.effect(label) for label in OUTCOMES if label != target]
    )
    missing_effect_rejected = not parent.effect_equal(missing_effect_sum, IDENTITY_EFFECT)

    one_front = [branch for branch in baseline if branch.front == front]
    one_front_report = append_channel_certificate(one_front, deep=False)
    one_front_rejected = not one_front_report["branch_count"]

    scaled_root_factors = make_append_factors(
        ZERO, current_word, target, root_scale=R(2)
    )
    stored_scalar_branch = replace(
        physical_branch,
        factors=scaled_root_factors,
        effect=physical_branch.effect,
    )
    stored_scalar_rejected = not branch_effect_is_recontracted(
        stored_scalar_branch
    )

    z_plus = (0, 0, 1)
    z_minus = (0, 0, -1)
    coherent_source = (0, 0, 1)
    coherent_target = (1, 1, 1)
    coherent_left_word = parent.locked_word(z_plus, coherent_source)
    coherent_right_word = parent.locked_word(z_minus, coherent_source)
    coherent_left = append_branch(ZERO, coherent_left_word, coherent_target)
    coherent_right = append_branch(ZERO, coherent_right_word, coherent_target)
    coherent_mutant = CoherentAppendMutant(
        left_factors=coherent_left.factors,
        right_factors=coherent_right.factors,
    )
    coherent_cross = contract_coherent_append_cross(coherent_mutant)
    coherent_sum_rejected = (
        append_matrix_unit_survival(
            coherent_left_word, coherent_right_word, True
        )
        == 0
        and coherent_cross.left_input_word == coherent_left_word
        and coherent_cross.right_input_word == coherent_right_word
        and coherent_cross.left_forward_center
        == coherent_left.forward_center
        and coherent_cross.right_forward_center
        == coherent_right.forward_center
        and coherent_cross.cross_amplitude.is_positive is True
        and coherent_cross.cross_norm2.is_positive is True
        and parent.c4_front_bit_phase_witness()
    )

    second_front = (0, 1, 0)
    two_forward_factors = physical_branch.factors + (
        ("second_active_forward_center", forward_center(ZERO, second_front)),
        ("second_forward_live_prep_maps", live_prep_maps(source)),
        (
            "second_forward_pointer_prep_maps",
            pointer_prep_maps(second_front),
        ),
        ("second_forward_live_root", parent.root_operator_factor(target)),
        (
            "second_forward_writer_pointer_maps",
            parent.pointer_rank_one_maps(
                parent.ready_word(second_front),
                parent.locked_word(second_front, target),
            ),
        ),
    )
    two_forward_branch = replace(physical_branch, factors=two_forward_factors)
    two_forward_rejected = (
        altered_factors_rejected(two_forward_factors)
        and not append_factorization_is_physical(two_forward_branch)
    )

    bell_density = sp.Matrix(
        [
            [R(1, 2), 0, 0, R(1, 2)],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [R(1, 2), 0, 0, R(1, 2)],
        ]
    )
    transposed_reference = sp.zeros(4, 4)
    for a, b, c, d in itertools.product(range(2), repeat=4):
        transposed_reference[2 * a + d, 2 * c + b] = bell_density[
            2 * a + b, 2 * c + d
        ]
    antisymmetric = sp.Matrix((0, 1, -1, 0)) / sp.sqrt(2)
    transpose_reference_rejected = sp.simplify(
        (antisymmetric.T * transposed_reference * antisymmetric)[0]
    ) == -R(1, 2)

    mutations = {
        "R8_target_breaks_Record_selected_geometry": r8_rejected,
        "backward_target_breaks_forward_selection": backward_rejected,
        "fixed_host_target_breaks_Record_selection": fixed_target_rejected,
        "outcome_selected_target_breaks_Record_selection": outcome_target_rejected,
        "nonblank_forward_input_is_rejected": nonblank_rejected,
        "overwrite_current_Record_breaks_QND": overwrite_rejected,
        "drop_writer_pointer_factor_breaks_physical_map": pointer_drop_rejected,
        "relocate_writer_factor_breaks_physical_carrier": relocated_writer_site_rejected,
        "future_outcome_preparation_breaks_causal_state_rule": future_rejected,
        "one_prepared_live_factor_replaced_by_Blank_breaks_kernel": one_blank_factor_rejected,
        "one_positive_root_sector_perturbation_breaks_contraction": one_root_sector_rejected,
        "stored_transition_scalar_cannot_replace_factor_contraction": stored_scalar_rejected,
        "coherent_Record_branch_sum_breaks_separate_instrument": coherent_sum_rejected,
        "touch_lateral_block_breaks_one_Blank_scope": lateral_touch_rejected,
        "drop_source_control_breaks_channel_family": dropped_source_rejected,
        "duplicate_control_branch_breaks_stochastic_grouping": duplicate_control_rejected,
        "drop_outcome_breaks_row_normalization": dropped_outcome_rejected,
        "omit_STOP_breaks_global_completeness": omit_stop_rejected,
        "scaled_STOP_breaks_global_completeness": scaled_stop_rejected,
        "rotate_labels_without_centers_breaks_covariance": labels_only_covariance_rejected,
        "accept_nonblank_target_breaks_overwrite_safety": nonblank_eligibility_rejected,
        "require_unsupplied_predecessor_breaks_returned_tip": returned_tip_rejected,
        "reuse_consumed_block_breaks_Blank_domain": consumed_reuse_rejected,
        "square_transition_factor_breaks_prefix_marginal": squared_prefix_rejected,
        "skip_stochastic_sum_breaks_induction_step": induction_without_stochasticity_rejected,
        "backward_state_dependence_breaks_spectator_independence": backward_dependency_rejected,
        "lateral_state_dependence_breaks_spectator_independence": lateral_dependency_rejected,
        "drop_first_effect_breaks_initial_POVM": missing_effect_rejected,
        "one_front_only_breaks_cubic_channel_family": one_front_rejected,
        "activate_two_forward_blocks_breaks_single_target_scope": two_forward_rejected,
        "transpose_reference_factor_is_not_CP": transpose_reference_rejected,
    }

    source_text = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source_text)
    assigned_names = {
        target_node.id
        for node in ast.walk(tree)
        if isinstance(node, (ast.Assign, ast.AnnAssign))
        for target_node in (
            node.targets if isinstance(node, ast.Assign) else (node.target,)
        )
        if isinstance(target_node, ast.Name)
    }
    function_args = {
        node.name: tuple(argument.arg for argument in node.args.args)
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef)
        and node.name in {"record_selected_forward_center", "append_branch"}
    }
    state_text = (PACKET / "STATE.yaml").read_text(encoding="utf-8")
    guards = {
        "no_transition_target_table": not {
            "TRANSITION_TABLE", "EXPECTED_TRANSITION_TABLE", "TARGET_CHANNEL"
        }
        & assigned_names,
        "physical_selector_has_only_anchor_and_Record": function_args.get(
            "record_selected_forward_center"
        )
        == ("anchor", "current_word"),
        "append_public_args_have_no_target_site_or_future_state": function_args.get(
            "append_branch"
        )
        == ("anchor", "current_word", "next_outcome"),
        "declared_parent_source_input": PARENT_SOURCE in AUDIT_INPUT_PATHS,
        "fixed_anchor_carrier_is_224_sites": fixed_anchor_geometry()["sites"] == 224,
        "realized_append_uses_two_blocks": len({ZERO, forward_center(ZERO, front)}) == 2,
        "arbitrary_backward_lateral_not_function_arguments": all(
            name not in {argument.arg for argument in node.args.args}
            for node in ast.walk(tree)
            if isinstance(node, ast.FunctionDef) and node.name == "append_branch"
            for name in ("backward_state", "lateral_state", "predecessor")
        ),
        "no_dense_eigensolver": not any(
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr in {"eigenvals", "eigenvects"}
            for node in ast.walk(tree)
        ),
        "scope_keeps_compound_range": "nearest_neighbor_compiler: false"
        in state_text,
        "scope_keeps_scores_fixed": "toe_percentage_movement: 0"
        in state_text,
        "forbidden_promotions_remain_explicitly_false": all(
            declaration in state_text
            for declaration in (
                "nearest_neighbor_compiler: false",
                "physical_clock: false",
                "action_source_join: false",
                "gravity_source: false",
                "blank_generation: false",
                "axiom_update: false",
                "obligation_retirement: 0",
                "toe_percentage_movement: 0",
            )
        ),
    }

    collision_anchor_a = ZERO
    collision_front_a = (1, 0, 0)
    collision_anchor_b = (9, -9, 0)
    collision_front_b = (0, 1, 0)
    shared_target = forward_center(collision_anchor_a, collision_front_a)
    collision_word_a = parent.locked_word(collision_front_a, source)
    collision_word_b = parent.locked_word(collision_front_b, source)
    collision_state = {
        collision_anchor_a: collision_word_a,
        collision_anchor_b: collision_word_b,
        shared_target: parent.BLANK_BLOCK,
    }

    def anchored_control_eigenvalue(anchor, word, state):
        target_center = record_selected_forward_center(anchor, word)
        return int(
            state.get(anchor) == word
            and state.get(target_center) == parent.BLANK_BLOCK
        )

    collision_value_a = anchored_control_eigenvalue(
        collision_anchor_a, collision_word_a, collision_state
    )
    collision_value_b = anchored_control_eigenvalue(
        collision_anchor_b, collision_word_b, collision_state
    )
    unarbitrated_sum = collision_value_a + collision_value_b
    collision = (
        shared_target == forward_center(collision_anchor_b, collision_front_b)
        and support_at(collision_anchor_a).isdisjoint(support_at(collision_anchor_b))
        and collision_value_a == collision_value_b == 1
        and unarbitrated_sum == 2
        and unarbitrated_sum ** 2 == 4
        and unarbitrated_sum ** 2 != unarbitrated_sum
    )
    mutations[
        "two_shared_target_tips_break_unarbitrated_global_projector"
    ] = collision
    sign_changed = any(
        parent.transition(source_label, target_label, sign=-1)
        != parent.transition(source_label, target_label)
        for source_label in OUTCOMES
        for target_label in OUTCOMES
    )
    external_controls = {
        "Q_sign_reversal_changes_kernel": sign_changed,
    }
    return {
        "executed_model_mutations": mutations,
        "coverage_and_scope_guards": guards,
        "external_negative_controls": external_controls,
    }


class Checks:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def check(self, name, condition, detail):
        if condition:
            self.passed += 1
            print(f"PASS {name}: {detail}")
        else:
            self.failed += 1
            print(f"FAIL {name}: {detail}")


def main():
    checks = Checks()
    checks.check("freeze", frozen_hashes_ok(), "8/8 Block24 preregistration hashes plus exact Block23 parent source")

    geometry = fixed_anchor_geometry()
    checks.check(
        "fixed_anchor_geometry",
        geometry["pairwise_disjoint"]
        and geometry["sites"] == 224
        and geometry["radius2"] == 169
        and geometry["covariant"],
        "one current plus six possible forward 32-site blocks; common carrier 224 sites, radius 13",
    )

    imported_effects = parent.summed_effects([parent.effect(label) for label in OUTCOMES])
    checks.check(
        "imported_effect_completion",
        parent.effect_equal(imported_effects, IDENTITY_EFFECT),
        "fourteen Block22 effects rederive coefficientwise sum I_64",
    )
    checks.check(
        "explicit_positive_roots",
        all(parent.lueders_root_certificate(label) for label in OUTCOMES),
        "all fourteen 64-sector positive roots reconstruct their physical effects",
    )

    locked_words = tuple(
        parent.locked_word(front, source)
        for front in DIRECTIONS
        for source in OUTCOMES
    )
    record_code = (
        len(set(locked_words)) == 84
        and all(parent.decode_locked_word(word) is not None for word in locked_words)
        and all(
            record_selected_forward_center(ZERO, word)
            == forward_center(ZERO, parent.decode_locked_word(word)[0])
            for word in locked_words
        )
    )
    checks.check(
        "Record_selected_target",
        record_code,
        "84 complete physical Locked words uniquely decode front/outcome and one forward center",
    )

    branches = all_append_branches()
    checks.check(
        "factorized_append_branches",
        len(branches) == 1176
        and all(append_factorization_is_physical(branch) for branch in branches),
        "all 1176 prepare-plus-root-plus-pointer append Kraus branches are physical factor lists",
    )
    append_certificate = append_channel_certificate(branches)
    checks.check(
        "global_append_CPTP",
        all(
            append_certificate[key]
            for key in (
                "branch_count",
                "fourteen_per_control",
                "factor_complete",
                "derived_effects",
                "positive_effects",
                "stochastic_rows",
                "controls_orthogonal",
                "actual_physical_gram_sum",
                "p_valid_projector",
                "kraus_complete",
                "arbitrary_reference",
            )
        ),
        "84 factor-recontracted Record/Blank Gram terms form P_valid; K_STOP=I-P completes the anchored channel with symbolic I_R",
    )
    checks.check(
        "classical_Record_QND",
        append_certificate["classical_record_qnd"]
        and append_certificate["coherent_code_not_qnd"],
        "every old classical Record projector is fixed; eligible cross-word coherences dephase, so no coherent-code QND claim",
    )
    checks.check(
        "physical_append_covariance",
        append_certificate["branch_covariance"],
        "all separate branches rotate physical supports/live/pointers/roots under 24 frames and translate as one anchored family",
    )
    checks.check(
        "self_delimiting_tip",
        append_certificate["target_nonblank"]
        and all(
            append_valid_sector_eigenvalue(word, False) == 0
            and append_valid_sector_eigenvalue(word, True) == 1
            for word in locked_words
        ),
        "old source STOPs after forward becomes Locked; translated new complete Record accepts one new Blank",
    )

    checks.check(
        "exact_three_event_composite",
        three_event_certificate(),
        "all 16464 literal sequential composites contract to E_b1*T(b2|b1)*T(b3|b2), both prefix marginals, total I, and symbolic I_R",
    )
    checks.check(
        "arbitrary_finite_cylinders",
        finite_history_induction_certificate(),
        "physical base prefix plus Record-preserving returned-tip induction and a coefficientwise stochastic/reference step prove every fixed finite cylinder",
    )

    spectator_scope = all(
        factor_dictionary(branch.factors)["lateral_touch"] is False
        and len(factor_dictionary(branch.factors)["spectator_identity_centers"]) == 5
        and len(factor_dictionary(branch.factors)["spectator_identity_factors"])
        == 160
        and append_preserves_arbitrary_prior_records(branch)
        for branch in branches
    )
    checks.check(
        "single_Blank_resource_scope",
        spectator_scope and chain_support_certificate(),
        "one exact Blank is consumed; 160 explicit spectator identities plus I_outside preserve every earlier/backward/lateral block",
    )

    source_text = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source_text)
    public_args = {
        node.name: tuple(argument.arg for argument in node.args.args)
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef)
        and node.name in {"record_selected_forward_center", "append_branch"}
    }
    scope_ast = public_args == {
        "record_selected_forward_center": ("anchor", "current_word"),
        "append_branch": ("anchor", "current_word", "next_outcome"),
    }
    checks.check(
        "scope_ast",
        scope_ast,
        "target site derives only from anchor plus physical current Record; append has no backward/lateral/future-site input",
    )

    report = mutation_rejections()
    mutations = report["executed_model_mutations"]
    rejected = sum(bool(value) for value in mutations.values())
    checks.check(
        "executed_model_mutations",
        rejected == len(mutations),
        f"{rejected}/{len(mutations)} altered channels/rules reject their target invariant",
    )
    guards = report["coverage_and_scope_guards"]
    guarded = sum(bool(value) for value in guards.values())
    checks.check(
        "coverage_scope_guards",
        guarded == len(guards),
        f"{guarded}/{len(guards)} non-mutation coverage/scope guards hold",
    )
    controls = report["external_negative_controls"]
    controlled = sum(bool(value) for value in controls.values())
    checks.check(
        "external_negative_controls",
        controlled == len(controls),
        f"{controlled}/{len(controls)} explicit external controls behave as expected",
    )

    print("per_element: all 1176 append effects, all 16464 three-event effects, 196 kernel entries, and exact prefix identities are checked")
    print("per_site: every factor on the 224-site fixed-anchor carrier and every translated straight-ray block support is checked; one realized append consumes one 32-site Blank block")
    print("per_mode: all 84 current Record sectors, fourteen next-outcome branches, six front fibers, and 24 proper cubic frames are checked; no physical clock mode is claimed")
    print("per_block: the current 32-site Record block, one selected forward block, five unrestricted spectator blocks, STOP complement, and arbitrary finite returned-tip induction are checked")
    print("lattice_wide: checked and not executed -- shared-target arbitration, simultaneous global scheduling, Blank generation, turns, rate, source, gravity, retention, and TOE closure remain open")
    print("TERMINAL: EXACT-COVARIANT-SELF-DELIMITING-ONE-BLANK-RECORD-APPEND-INSTRUMENT-WITH-PROJECTIVELY-CONSISTENT-ARBITRARY-FINITE-STRAIGHT-RAY-CYLINDERS")
    print("SCOPE: anchored isolated straight ray; supplied one-Blank-per-append boundary; atomic range 13; no global scheduler, mixed-front safety, substrate ownership, nearest-neighbor compiler, time, source, gravity, axiom, audit, obligation, or TOE move")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    raise SystemExit(1 if checks.failed else 0)


if __name__ == "__main__":
    main()
