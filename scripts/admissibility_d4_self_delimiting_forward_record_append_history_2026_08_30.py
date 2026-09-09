#!/usr/bin/env python3
"""Source-only extraction of exact finite block24 definitions used by the pair-process unit.
Original complete source is recoverable in eta-pair-process-correction-20260909/RECOVERY.json.
No parent controller, certification campaign, or physical standing is imported.
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


import admissibility_d4_prior_record_live_preparation_two_event_prefix_2026_08_30 as parent  # noqa: E402


ZERO = (0, 0, 0)


DIRECTIONS = parent.DIRECTIONS


OUTCOMES = parent.OUTCOMES


ROTATIONS = parent.ROTATIONS


DISPLACEMENT = parent.DISPLACEMENT


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
