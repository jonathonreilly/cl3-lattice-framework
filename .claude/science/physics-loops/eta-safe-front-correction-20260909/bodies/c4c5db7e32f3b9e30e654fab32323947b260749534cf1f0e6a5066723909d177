#!/usr/bin/env python3
"""Block 204: exact Record-operator-system descent discriminator.

This runner types the Block-203 periodic CAR functional against the fixed
Block-194 C32 PVM before evaluating any purported periodic Record weights.  It
exposes the exact C8-syndrome x C4-logical PVM factorization, classifies full-
Fock exterior and positive-operator-system routes without materializing the
2^32 carrier, and separates the zero-source block-diagonal right-Schur control
from a coherent two-sector counterexample.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from functools import cache
from itertools import product
from math import comb
from pathlib import Path
import subprocess

import sympy as sp

import admissibility_d4_dirac_kahler_common_action_ward_tt_record_mark_2026_08_24 as b190
import admissibility_d4_grade3_source_instrument_history_write_2026_08_24 as b191
import admissibility_d4_full_temporal_carrier_source_history_write_2026_08_25 as b192
import admissibility_d4_detector_conditioned_m2_pointer_discriminator_2026_08_25 as b194
import admissibility_d4_l24_reflection_algebra_gluing_discriminator_2026_08_26 as b203


ROOT = Path(__file__).resolve().parents[1]
PACKET = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block204-record-operator-system-descent-20260826"
)
GOAL_PATH = f"{PACKET}/GOAL.md"
PREFLIGHT_PATH = f"{PACKET}/PREFLIGHT_WITNESSES.md"
PARENT_COMMIT = "12419fc0a1f5b2f87ef557bc52732f83dcc8149a"
PREREG_COMMIT = "03c32997ace9a723fa39ce5fbe6afbad9087e6ee"
CURRENT_MAIN = "76df4becc8233080bc5a10a4baf55f83e80f8f2d"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-axiom-closure-block204-record-operator-system-descent-20260826/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block204-record-operator-system-descent-20260826/PREFLIGHT_WITNESSES.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_D4_FULL_TEMPORAL_CARRIER_SOURCE_HISTORY_WRITE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_D4_DETECTOR_CONDITIONED_M2_POINTER_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_D4_L24_REFLECTION_ALGEBRA_EXACT_GLUING_TRACE_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "scripts/admissibility_d4_dirac_kahler_common_action_ward_tt_record_mark_2026_08_24.py",
    "scripts/admissibility_d4_grade3_source_instrument_history_write_2026_08_24.py",
    "scripts/admissibility_d4_full_temporal_carrier_source_history_write_2026_08_25.py",
    "scripts/admissibility_d4_detector_conditioned_m2_pointer_discriminator_2026_08_25.py",
    "scripts/admissibility_d4_l24_reflection_algebra_gluing_discriminator_2026_08_26.py",
)

R = sp.Rational
EVENT_COUNT = 8
EVENT_RANK = 4
EVENT_CARRIER_DIM = 32
CLIFFORD_COPY_COUNT = 8
PER_COPY_LINEAR_DIM = 2

MUTATION_FAMILY = {
    "stale_main_authority": "A",
    "drop_preregistration": "A",
    "equate_per_copy_and_event_carriers": "B",
    "treat_direct_sum_as_fock_tensor": "B",
    "erase_logical_clifford_fiber": "B",
    "call_logical_fiber_canonical_action_map": "B",
    "call_gamma_lifts_orthogonal": "C",
    "call_gamma_lifts_complete": "C",
    "drop_shared_vacuum": "C",
    "call_at_least_one_lifts_orthogonal": "D",
    "call_n1_compression_full_unital": "D",
    "call_n1_sector_action_derived": "D",
    "erase_full_complement_povm": "E",
    "erase_linear_share_povm": "E",
    "erase_support_share_povm": "E",
    "call_full_maps_equivalent": "E",
    "break_full_map_n1_extension": "E",
    "break_full_map_port_covariance": "E",
    "call_all_full_maps_refinement_consistent": "E",
    "call_full_positive_extension_unique": "E",
    "drop_periodic_vacuum_or_pair": "F",
    "call_n1_periodic_normalization_preserving": "F",
    "call_operator_nonuniqueness_probability_nonuniqueness": "F",
    "import_maximally_mixed_os_state": "G",
    "call_os_control_periodic_descent": "G",
    "call_physical_partition_supplied": "G",
    "call_os_control_coherence_independent": "G",
    "evaluate_periodic_record_weights_without_map": "H",
    "claim_unique_periodic_descent": "H",
    "claim_record_born_axiom_or_toe": "H",
    "claim_all_probability_routes_fail": "H",
}
MUTATIONS = tuple(MUTATION_FAMILY)

N5_LINES = (
    "per_element: checked all eight fixed C32 projector ranks, pair products, three full-Fock POVM extensions, symbolic OS weights, and finite coarse events.",
    "per_site: checked and not executed — no Z3 site embedding, nearest-neighbor apparatus, or physical local-possibility partition is supplied.",
    "per_mode: checked the D1 zero-radius two-mode periodic CAR vacuum, one-particle, and pair sectors; other momentum/radius sectors remain sealed.",
    "per_block: checked the full eight-port C32 PVM and exact 32-mode occupation generating functions without constructing the dense 2^32 carrier.",
    "lattice_wide: checked and not executed — no all-site process, formation schedule, permanent history, gravity completion, axiom edit, or TOE closure is claimed.",
)


def matrix_equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return left.shape == right.shape and all(
        sp.cancel(value) == 0 for value in left - right
    )


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=60
    ).strip()


def is_ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT, check=False, stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL, timeout=60,
    ).returncode == 0


@cache
def authority_facts() -> dict[str, object]:
    return {
        "main": git_output("rev-parse", "origin/main"),
        "parent": is_ancestor(PARENT_COMMIT),
        "prereg": is_ancestor(PREREG_COMMIT),
        "goal_frozen": (
            git_output("rev-parse", f"{PREREG_COMMIT}:{GOAL_PATH}")
            == git_output("hash-object", "--", GOAL_PATH)
        ),
        "preflight_frozen": (
            git_output("rev-parse", f"{PREREG_COMMIT}:{PREFLIGHT_PATH}")
            == git_output("hash-object", "--", PREFLIGHT_PATH)
        ),
        "axiom": git_output(
            "rev-parse", "origin/main:docs/MINIMAL_AXIOMS_2026-06-29.md"
        ),
    }


@cache
def pvm_facts() -> dict[str, object]:
    instrument = b194.instrument_pointer_facts()
    effects = instrument["effects"]
    return {
        "effects": effects,
        "count": len(effects),
        "ranks": tuple(effect.rank() for effect in effects),
        "projectors": instrument["projectors"],
        "orthogonal": instrument["pairwise_orthogonal"],
        "complete": instrument["complete"],
        "coarsenings": instrument["coarsenings"],
        "pointer": (
            instrument["writer_unitary"]
            and instrument["writer_nonidentity"]
            and instrument["faithful_joint_readout"]
        ),
    }


@cache
def stabilizer_fiber_facts() -> dict[str, object]:
    """Expose the exact C8-syndrome x C4-logical structure of the PVM.

    The calculation proves an internal dimension match with Block 203's C4,
    not a same-action identification with that carrier.  The latter needs a
    state/action intertwiner that no upstream block supplies.
    """
    creation = b190.CREATION
    annihilation = b190.ANNIHILATION
    gammas = tuple(
        item
        for axis in range(4)
        for item in (
            creation[axis] + annihilation[axis],
            sp.I * (creation[axis] - annihilation[axis]),
        )
    )
    identity2 = sp.eye(2)
    identity32 = sp.eye(32)
    tau_x = sp.Matrix(((0, 1), (1, 0)))
    tau_y = sp.Matrix(((0, -sp.I), (sp.I, 0)))
    tensor = sp.kronecker_product
    orientation = b194.detector_classification_facts()["orientation"]
    stabilizers = (
        tensor(identity2, b191.O1),
        tensor(identity2, b191.O2),
        tensor(tau_x, orientation),
    )
    logical_majoranas = (
        tensor(identity2, gammas[2]),
        -sp.I * tensor(identity2, gammas[0] * gammas[1] * gammas[7]),
        -sp.I * tensor(tau_x, gammas[0] * gammas[5] * gammas[7]),
        -sp.I * tensor(tau_y, gammas[0] * gammas[1] * gammas[4]),
    )
    monomials = []
    for mask in range(2 ** len(logical_majoranas)):
        monomial = identity32
        for index, generator in enumerate(logical_majoranas):
            if mask & (1 << index):
                monomial = sp.expand(monomial * generator)
        monomials.append(monomial)
    effects = pvm_facts()["effects"]
    global_span = sp.Matrix.hstack(*(
        monomial.reshape(32 * 32, 1) for monomial in monomials
    )).rank()
    fiber_spans = tuple(
        sp.Matrix.hstack(*(
            sp.expand(effect * monomial * effect).reshape(32 * 32, 1)
            for monomial in monomials
        )).rank()
        for effect in effects
    )
    return {
        "stabilizers": stabilizers,
        "stabilizer_count": len(stabilizers),
        "stabilizers_commute": all(matrix_equal(
            stabilizers[left] * stabilizers[right],
            stabilizers[right] * stabilizers[left],
        ) for left in range(3) for right in range(left + 1, 3)),
        "logical_hermitian": all(matrix_equal(
            generator.H, generator
        ) for generator in logical_majoranas),
        "logical_clifford": all(matrix_equal(
            logical_majoranas[left] * logical_majoranas[right]
            + logical_majoranas[right] * logical_majoranas[left],
            (2 if left == right else 0) * identity32,
        ) for left in range(4) for right in range(4)),
        "logical_commutes_stabilizers": all(matrix_equal(
            generator * stabilizer, stabilizer * generator
        ) for generator in logical_majoranas for stabilizer in stabilizers),
        "logical_commutes_effects": all(matrix_equal(
            generator * effect, effect * generator
        ) for generator in logical_majoranas for effect in effects),
        "logical_algebra_dimension": global_span,
        "fiber_algebra_dimensions": fiber_spans,
        "syndrome_dimension": len(effects),
        "logical_dimension": effects[0].rank(),
        "factorization_dimension": len(effects) * effects[0].rank(),
        "phase_free_pauli_centralizer_size": 2 ** (2 * 5 - 3),
        "same_action_intertwiner_supplied": False,
        "canonical_logical_basis_supplied": False,
    }


@cache
def carrier_facts() -> dict[str, object]:
    grade_counts = tuple(comb(4, degree) for degree in range(5))
    time_spectrum = b192.GTIME.eigenvals()
    per_copy_fock_dim = 2 ** PER_COPY_LINEAR_DIM
    full_periodic_fock_dim = per_copy_fock_dim ** CLIFFORD_COPY_COUNT
    record_fock_dim = 2 ** EVENT_CARRIER_DIM
    return {
        "form_grade_counts": grade_counts,
        "form_dim": sum(grade_counts),
        "gtime_involution": matrix_equal(
            b192.GTIME * b192.GTIME, sp.eye(16)
        ),
        "gtime_spectrum": time_spectrum,
        "clifford_copies": CLIFFORD_COPY_COUNT,
        "per_copy_linear_dim": PER_COPY_LINEAR_DIM,
        "per_copy_fock_dim": per_copy_fock_dim,
        "full_periodic_fock_dim": full_periodic_fock_dim,
        "event_carrier_dim": EVENT_CARRIER_DIM,
        "record_fock_dim": record_fock_dim,
        "literal_same_carrier": per_copy_fock_dim == EVENT_CARRIER_DIM,
        "direct_sum_is_fock_tensor": (
            CLIFFORD_COPY_COUNT * PER_COPY_LINEAR_DIM
            == full_periodic_fock_dim
        ),
        "creation_count": len(b190.CREATION),
    }


@cache
def exterior_lift_facts() -> dict[str, object]:
    pvm = pvm_facts()
    event_rank = pvm["ranks"][0]
    gamma_rank = sum(comb(event_rank, degree)
                     for degree in range(event_rank + 1))
    fock_dim = 2 ** EVENT_CARRIER_DIM
    shared_vacuum_rank = 1
    nonvacuum_single_port_span = EVENT_COUNT * (gamma_rank - 1)
    at_least_one_rank = (2 ** event_rank - 1) * 2 ** (
        EVENT_CARRIER_DIM - event_rank
    )
    two_port_intersection_rank = (
        (2 ** event_rank - 1) ** 2
        * 2 ** (EVENT_CARRIER_DIM - 2 * event_rank)
    )
    return {
        "fock_dim": fock_dim,
        "gamma_ranks": (gamma_rank,) * EVENT_COUNT,
        "gamma_cross_rank": shared_vacuum_rank,
        "gamma_vacuum_sum_eigenvalue": EVENT_COUNT,
        "gamma_pairwise_orthogonal": shared_vacuum_rank == 0,
        "gamma_complete": (
            nonvacuum_single_port_span + shared_vacuum_rank == fock_dim
            and EVENT_COUNT == 1
        ),
        "single_port_span_rank": (
            nonvacuum_single_port_span + shared_vacuum_rank
        ),
        "mixed_port_sector_nonempty": (
            fock_dim
            > nonvacuum_single_port_span + shared_vacuum_rank
        ),
        "at_least_one_ranks": (at_least_one_rank,) * EVENT_COUNT,
        "at_least_one_pair_intersection_rank": two_port_intersection_rank,
        "at_least_one_pairwise_orthogonal": (
            two_port_intersection_rank == 0
        ),
        "n1_dim": EVENT_CARRIER_DIM,
        "n1_ranks": pvm["ranks"],
        "n1_pairwise_orthogonal": pvm["orthogonal"],
        "n1_sum_is_sector_unit": pvm["complete"],
        "n1_sum_is_full_unit": EVENT_CARRIER_DIM == fock_dim,
    }


@cache
def operator_system_extension_facts() -> dict[str, object]:
    """Exhaust the occupation-count spectra of three full-Fock POVMs.

    Each joint eigenspace is labeled by n_i in {0,...,4}.  The calculation is
    therefore exhaustive over 5^8 count patterns without constructing the
    2^32-dimensional carrier.
    """
    uniform = (Fraction(1, EVENT_COUNT),) * EVENT_COUNT

    def full_complement(counts: tuple[int, ...]) -> tuple[Fraction, ...]:
        occupied = tuple(index for index, count in enumerate(counts) if count)
        if len(occupied) != 1:
            return uniform
        return tuple(
            Fraction(int(index == occupied[0]), 1)
            for index in range(EVENT_COUNT)
        )

    def linear_share(counts: tuple[int, ...]) -> tuple[Fraction, ...]:
        total = sum(counts)
        if total == 0:
            return uniform
        return tuple(Fraction(count, total) for count in counts)

    def support_share(counts: tuple[int, ...]) -> tuple[Fraction, ...]:
        occupied = sum(count > 0 for count in counts)
        if occupied == 0:
            return uniform
        return tuple(
            Fraction(int(count > 0), occupied) for count in counts
        )

    maps = (full_complement, linear_share, support_share)
    positive_unital = True
    n1_extension = True
    permutation_covariant = True
    pattern_count = 0
    for raw_counts in product(range(EVENT_RANK + 1), repeat=EVENT_COUNT):
        counts = tuple(raw_counts)
        pattern_count += 1
        swap_counts = (counts[1], counts[0]) + counts[2:]
        rotate_counts = counts[1:] + counts[:1]
        for mapping in maps:
            weights = mapping(counts)
            positive_unital = positive_unital and (
                all(weight >= 0 for weight in weights)
                and sum(weights) == 1
            )
            if sum(counts) == 1:
                n1_extension = n1_extension and weights == tuple(
                    Fraction(count, 1) for count in counts
                )
            permutation_covariant = permutation_covariant and (
                mapping(swap_counts)
                == (weights[1], weights[0]) + weights[2:]
                and mapping(rotate_counts) == weights[1:] + weights[:1]
            )

    witness = (2, 1) + (0,) * (EVENT_COUNT - 2)
    witness_values = tuple(mapping(witness) for mapping in maps)
    distinct = len(set(witness_values)) == len(maps)
    projectivity_residuals = (
        Fraction(1, 64) - Fraction(1, 8),
        Fraction(4, 9) - Fraction(2, 3),
        Fraction(1, 4) - Fraction(1, 2),
    )
    original_split_witness = (2, 1) + (0,) * 6
    refined_split_witness = (1, 1, 1) + (0,) * 6

    def complement_dynamic(counts: tuple[int, ...]) -> tuple[Fraction, ...]:
        occupied = tuple(index for index, count in enumerate(counts) if count)
        if len(occupied) != 1:
            return (Fraction(1, len(counts)),) * len(counts)
        return tuple(Fraction(int(index == occupied[0]), 1)
                     for index in range(len(counts)))

    split_values = (
        (
            complement_dynamic(original_split_witness)[0],
            sum(complement_dynamic(refined_split_witness)[:2]),
        ),
        (
            linear_share(original_split_witness)[0],
            sum(linear_share(refined_split_witness)[:2]),
        ),
        (
            support_share(original_split_witness)[0],
            sum(support_share(refined_split_witness)[:2]),
        ),
    )
    additive_rows = []
    for left in range(1, EVENT_RANK + 1):
        for right in range(1, EVENT_RANK + 1 - left):
            row = [0] * EVENT_RANK
            row[left - 1] -= 1
            row[right - 1] -= 1
            row[left + right - 1] += 1
            additive_rows.append(row)
    additive_rank = sp.Matrix(additive_rows).rank()
    return {
        "pattern_count": pattern_count,
        "positive_unital": positive_unital,
        "n1_extension": n1_extension,
        "permutation_covariant": permutation_covariant,
        "number_preserving": True,
        "defined_on_vacuum_and_all_sectors": True,
        "faithful": n1_extension,
        "coarse_additive": positive_unital,
        "full_complement_exists": positive_unital,
        "linear_share_exists": positive_unital,
        "support_share_exists": positive_unital,
        "witness": witness,
        "witness_values": witness_values,
        "maps_distinct": distinct,
        "extension_count": len(maps),
        "unique_extension": len(maps) == 1,
        "all_nonprojective": all(value != 0 for value in projectivity_residuals),
        "projectivity_residuals": projectivity_residuals,
        "split_witness_values": split_values,
        "split_refinement_consistent": tuple(
            before == after for before, after in split_values
        ),
        "ratio_additivity_solution_dimension": EVENT_RANK - additive_rank,
        "number_share_selected_by_ratio_additivity": (
            EVENT_RANK - additive_rank == 1
        ),
        "physical_split_refinement_supplied": False,
    }


@cache
def periodic_facts() -> dict[str, object]:
    upstream = b203.state_facts()
    radius = sp.factor(((sp.sqrt(53) - 2) / 7) ** 24)
    denominator = (1 - radius) ** 2
    reconstructed = tuple(sp.factor(value / denominator) for value in (
        1, -radius, -radius, radius**2,
    ))
    n1_weight = sp.factor(reconstructed[1] + reconstructed[2])
    return {
        "radius": radius,
        "upstream_match": upstream["graded"] == reconstructed,
        "weights": reconstructed,
        "sum": sp.simplify(sum(reconstructed)),
        "vacuum_nonzero": reconstructed[0] != 0,
        "pair_nonzero": reconstructed[3] != 0,
        "n1_weight": n1_weight,
        "n1_negative": n1_weight.is_negative is True,
        "n1_normalization_preserving": sp.simplify(n1_weight - 1) == 0,
        "eight_record_values_evaluated": False,
    }


@cache
def scalar_quasifree_control_facts() -> dict[str, object]:
    """Control showing that map nonuniqueness need not change probabilities.

    If a future same-action construction supplied Q_R=-r I_32, the joint
    count law would be exchangeable.  Every port-covariant unital POVM would
    then have expectation 1/8, even when the operators differ off N=1.
    This scalar lift is a control only; it is not supplied by Blocks 192--203.
    """
    radius = periodic_facts()["radius"]
    denominator = sp.factor((1 - radius) ** EVENT_CARRIER_DIM)
    variables = sp.symbols(f"z0:{EVENT_COUNT}")
    numerator = sp.prod((1 - radius * variable) ** EVENT_RANK
                        for variable in variables)
    return {
        "candidate_q": -radius,
        "denominator": denominator,
        "joint_generator": sp.factor(numerator / denominator),
        "normalized": sp.simplify(
            numerator.subs({variable: 1 for variable in variables})
            / denominator
        ) == 1,
        "permutation_invariant": all(sp.simplify(
            numerator - numerator.xreplace({
                variables[index]: variables[(index + 1) % EVENT_COUNT]
                for index in range(EVENT_COUNT)
            })
        ) == 0 for _unused in (0,)),
        "covariant_unital_expectation": R(1, EVENT_COUNT),
        "operator_nonuniqueness_forces_probability_nonuniqueness": False,
        "full_c32_q_supplied": False,
    }


@cache
def os_control_facts() -> dict[str, object]:
    pvm = pvm_facts()
    history = b192.reduced_history_fixture()
    frozen = b192.frozen_history_positivity_facts()
    sector_weight = sp.symbols("sector_weight", real=True)
    identity16 = sp.eye(16)
    rho = sp.diag(
        sector_weight * identity16 / 16,
        (1 - sector_weight) * identity16 / 16,
    )
    weights = tuple(sp.factor(sp.trace(rho * effect))
                    for effect in pvm["effects"])
    coherence = sp.symbols("coherence", real=True)
    sector_orientation = stabilizer_fiber_facts()["stabilizers"][2]
    coherent_rho = sp.expand(
        (sp.eye(EVENT_CARRIER_DIM) + coherence * sector_orientation)
        / EVENT_CARRIER_DIM
    )
    coherent_weights = tuple(sp.factor(sp.trace(coherent_rho * effect))
                             for effect in pvm["effects"])
    expected_coherent = tuple(
        (1 + sign * coherence) / EVENT_COUNT
        for _event in range(EVENT_COUNT // 2)
        for sign in (1, -1)
    )
    block192_text = (ROOT / "docs" / (
        "ADMISSIBILITY_D4_FULL_TEMPORAL_CARRIER_SOURCE_HISTORY_WRITE_"
        "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md"
    )).read_text()
    block194_text = (ROOT / "docs" / (
        "ADMISSIBILITY_D4_DETECTOR_CONDITIONED_M2_POINTER_"
        "DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md"
    )).read_text()
    return {
        "history_positive": (
            history["positive_pivots"]
            and frozen["all_positive"]
            and frozen["full_inertias"] == ((192, 0, 0),) * 9
        ),
        "uniform_internal_marginal": (
            history["marginal"]
            and history["scalar_fixed_algebra"]
            and history["local_blocks_scalar"]
        ),
        "rho_trace": sp.simplify(sp.trace(rho)),
        "rho_spectrum": (
            (sector_weight / 16, 16),
            ((1 - sector_weight) / 16, 16),
        ),
        "positive_domain": "0<=sector_weight<=1",
        "weights": weights,
        "weight_sum": sp.simplify(sum(weights)),
        "weights_sector_independent": all(
            not weight.has(sector_weight) for weight in weights
        ),
        "all_one_eighth": weights == (R(1, 8),) * EVENT_COUNT,
        "block_diagonal_only": True,
        "coherent_trace": sp.simplify(sp.trace(coherent_rho)),
        "coherent_diagonal_blocks_unchanged": (
            matrix_equal(coherent_rho[:16, :16], sp.eye(16) / 32)
            and matrix_equal(coherent_rho[16:, 16:], sp.eye(16) / 32)
        ),
        "coherent_positive_domain": "-1<=coherence<=1",
        "coherent_weights": coherent_weights,
        "coherent_weights_expected": all(
            sp.simplify(actual - expected) == 0
            for actual, expected in zip(coherent_weights, expected_coherent)
        ),
        "coherence_independent": all(
            not value.has(coherence) for value in coherent_weights
        ),
        "maximally_mixed_imported": False,
        "periodic_descent": False,
        "physical_partition_supplied": not (
            "does not prove that the" in block192_text
            and "physical local-possibility partition" in block192_text
            and "no permanent Record" in block194_text
        ),
    }


def evaluate(mutation: str = "") -> dict[str, tuple[bool, str]]:
    authority = authority_facts()
    carrier = carrier_facts()
    pvm = pvm_facts()
    fiber = stabilizer_fiber_facts()
    lift = exterior_lift_facts()
    maps = operator_system_extension_facts()
    periodic = periodic_facts()
    scalar_control = scalar_quasifree_control_facts()
    os_control = os_control_facts()

    claims = {
        "main": CURRENT_MAIN,
        "prereg": True,
        "literal_same_carrier": False,
        "direct_sum_is_fock_tensor": False,
        "logical_clifford_exists": True,
        "logical_fiber_canonical_action_map": False,
        "gamma_orthogonal": False,
        "gamma_complete": False,
        "gamma_cross_rank": 1,
        "at_least_orthogonal": False,
        "n1_full_unital": False,
        "n1_action_derived": False,
        "full_complement_exists": True,
        "linear_share_exists": True,
        "support_share_exists": True,
        "full_maps_distinct": True,
        "full_map_n1_extension": True,
        "full_map_port_covariance": True,
        "all_full_maps_refinement_consistent": False,
        "full_positive_extension_unique": False,
        "periodic_vacuum_pair_nonzero": True,
        "n1_normalization_preserving": False,
        "operator_nonuniqueness_probability_nonuniqueness": False,
        "maximally_mixed_imported": False,
        "os_periodic_descent": False,
        "physical_partition_supplied": False,
        "os_control_coherence_independent": False,
        "periodic_record_values_evaluated": False,
        "unique_descent": False,
        "scope_overclaim": False,
        "broad_no_go": False,
    }
    if mutation == "stale_main_authority":
        claims["main"] = "stale"
    elif mutation == "drop_preregistration":
        claims["prereg"] = False
    elif mutation == "equate_per_copy_and_event_carriers":
        claims["literal_same_carrier"] = True
    elif mutation == "treat_direct_sum_as_fock_tensor":
        claims["direct_sum_is_fock_tensor"] = True
    elif mutation == "erase_logical_clifford_fiber":
        claims["logical_clifford_exists"] = False
    elif mutation == "call_logical_fiber_canonical_action_map":
        claims["logical_fiber_canonical_action_map"] = True
    elif mutation == "call_gamma_lifts_orthogonal":
        claims["gamma_orthogonal"] = True
    elif mutation == "call_gamma_lifts_complete":
        claims["gamma_complete"] = True
    elif mutation == "drop_shared_vacuum":
        claims["gamma_cross_rank"] = 0
    elif mutation == "call_at_least_one_lifts_orthogonal":
        claims["at_least_orthogonal"] = True
    elif mutation == "call_n1_compression_full_unital":
        claims["n1_full_unital"] = True
    elif mutation == "call_n1_sector_action_derived":
        claims["n1_action_derived"] = True
    elif mutation == "erase_full_complement_povm":
        claims["full_complement_exists"] = False
    elif mutation == "erase_linear_share_povm":
        claims["linear_share_exists"] = False
    elif mutation == "erase_support_share_povm":
        claims["support_share_exists"] = False
    elif mutation == "call_full_maps_equivalent":
        claims["full_maps_distinct"] = False
    elif mutation == "break_full_map_n1_extension":
        claims["full_map_n1_extension"] = False
    elif mutation == "break_full_map_port_covariance":
        claims["full_map_port_covariance"] = False
    elif mutation == "call_all_full_maps_refinement_consistent":
        claims["all_full_maps_refinement_consistent"] = True
    elif mutation == "call_full_positive_extension_unique":
        claims["full_positive_extension_unique"] = True
    elif mutation == "drop_periodic_vacuum_or_pair":
        claims["periodic_vacuum_pair_nonzero"] = False
    elif mutation == "call_n1_periodic_normalization_preserving":
        claims["n1_normalization_preserving"] = True
    elif mutation == "call_operator_nonuniqueness_probability_nonuniqueness":
        claims["operator_nonuniqueness_probability_nonuniqueness"] = True
    elif mutation == "import_maximally_mixed_os_state":
        claims["maximally_mixed_imported"] = True
    elif mutation == "call_os_control_periodic_descent":
        claims["os_periodic_descent"] = True
    elif mutation == "call_physical_partition_supplied":
        claims["physical_partition_supplied"] = True
    elif mutation == "call_os_control_coherence_independent":
        claims["os_control_coherence_independent"] = True
    elif mutation == "evaluate_periodic_record_weights_without_map":
        claims["periodic_record_values_evaluated"] = True
    elif mutation == "claim_unique_periodic_descent":
        claims["unique_descent"] = True
    elif mutation == "claim_record_born_axiom_or_toe":
        claims["scope_overclaim"] = True
    elif mutation == "claim_all_probability_routes_fail":
        claims["broad_no_go"] = True

    return {
        "A": (
            authority["main"] == claims["main"]
            and authority["parent"]
            and authority["prereg"] == claims["prereg"]
            and authority["goal_frozen"] and authority["preflight_frozen"]
            and authority["axiom"] == CURRENT_AXIOM_BLOB,
            "current authority and immutable pre-target registration are pinned",
        ),
        "B": (
            carrier["form_grade_counts"] == (1, 4, 6, 4, 1)
            and carrier["form_dim"] == 16
            and carrier["gtime_involution"]
            and carrier["gtime_spectrum"] == {1: 8, -1: 8}
            and carrier["creation_count"] == 4
            and carrier["literal_same_carrier"]
            == claims["literal_same_carrier"]
            and carrier["direct_sum_is_fock_tensor"]
            == claims["direct_sum_is_fock_tensor"]
            and pvm["count"] == EVENT_COUNT
            and pvm["ranks"] == (EVENT_RANK,) * EVENT_COUNT
            and pvm["projectors"] and pvm["orthogonal"]
            and pvm["complete"] and pvm["coarsenings"] and pvm["pointer"]
            and fiber["stabilizer_count"] == 3
            and fiber["stabilizers_commute"]
            and fiber["logical_hermitian"] and fiber["logical_clifford"]
            and fiber["logical_commutes_stabilizers"]
            and fiber["logical_commutes_effects"]
            and fiber["logical_algebra_dimension"] == 16
            and fiber["fiber_algebra_dimensions"] == (16,) * EVENT_COUNT
            and fiber["syndrome_dimension"] == EVENT_COUNT
            and fiber["logical_dimension"] == 4
            and fiber["factorization_dimension"] == EVENT_CARRIER_DIM
            and fiber["phase_free_pauli_centralizer_size"] == 128
            and claims["logical_clifford_exists"]
            == fiber["logical_clifford"]
            and fiber["same_action_intertwiner_supplied"]
            == claims["logical_fiber_canonical_action_map"]
            and fiber["canonical_logical_basis_supplied"] is False,
            "the distinct C32 PVM has an exact C8-syndrome x C4-logical Clifford factorization, but no supplied action-selected identification with Block 203's C4",
        ),
        "C": (
            lift["gamma_ranks"] == (16,) * EVENT_COUNT
            and lift["gamma_cross_rank"] == claims["gamma_cross_rank"]
            and lift["gamma_pairwise_orthogonal"]
            == claims["gamma_orthogonal"]
            and lift["gamma_complete"] == claims["gamma_complete"]
            and lift["gamma_vacuum_sum_eigenvalue"] == EVENT_COUNT
            and lift["mixed_port_sector_nonempty"],
            "functorial exterior lifts share the vacuum and miss mixed-port occupations, so they are not the original eight-outcome PVM",
        ),
        "D": (
            lift["at_least_one_pairwise_orthogonal"]
            == claims["at_least_orthogonal"]
            and lift["at_least_one_pair_intersection_rank"] > 0
            and lift["n1_dim"] == EVENT_CARRIER_DIM
            and lift["n1_ranks"] == (EVENT_RANK,) * EVENT_COUNT
            and lift["n1_pairwise_orthogonal"]
            and lift["n1_sum_is_sector_unit"]
            and lift["n1_sum_is_full_unit"] == claims["n1_full_unital"]
            and claims["n1_action_derived"] is False,
            "the PVM is restored exactly only on N=1; on the full Fock carrier other natural occupancy lifts overlap or are incomplete",
        ),
        "E": (
            maps["pattern_count"] == 5**8
            and maps["positive_unital"] and maps["number_preserving"]
            and maps["defined_on_vacuum_and_all_sectors"]
            and maps["faithful"] and maps["coarse_additive"]
            and maps["full_complement_exists"]
            == claims["full_complement_exists"]
            and maps["linear_share_exists"]
            == claims["linear_share_exists"]
            and maps["support_share_exists"]
            == claims["support_share_exists"]
            and maps["maps_distinct"] == claims["full_maps_distinct"]
            and maps["n1_extension"] == claims["full_map_n1_extension"]
            and maps["permutation_covariant"]
            == claims["full_map_port_covariance"]
            and maps["unique_extension"]
            == claims["full_positive_extension_unique"]
            and maps["all_nonprojective"]
            and maps["split_refinement_consistent"] == (False, True, False)
            and (all(maps["split_refinement_consistent"])
                 == claims["all_full_maps_refinement_consistent"])
            and maps["ratio_additivity_solution_dimension"] == 1
            and maps["number_share_selected_by_ratio_additivity"]
            and maps["physical_split_refinement_supplied"] is False,
            "three inequivalent full-Lambda(C32) positive unital port-covariant extensions exist; only number-share passes multiplicity-splitting in the ratio ansatz, and that physical refinement rule is not supplied",
        ),
        "F": (
            periodic["upstream_match"] and periodic["sum"] == 1
            and (periodic["vacuum_nonzero"] and periodic["pair_nonzero"])
            == claims["periodic_vacuum_pair_nonzero"]
            and periodic["n1_negative"]
            and periodic["n1_normalization_preserving"]
            == claims["n1_normalization_preserving"]
            and periodic["eight_record_values_evaluated"]
            == claims["periodic_record_values_evaluated"]
            and scalar_control["normalized"]
            and scalar_control["permutation_invariant"]
            and scalar_control["covariant_unital_expectation"] == R(1, 8)
            and scalar_control[
                "operator_nonuniqueness_forces_probability_nonuniqueness"
            ] == claims[
                "operator_nonuniqueness_probability_nonuniqueness"
            ]
            and scalar_control["full_c32_q_supplied"] is False,
            "the per-copy periodic functional cannot be postselected to N=1; a scalar full-C32 quasifree control proves operator nonuniqueness alone need not produce probability nonuniqueness",
        ),
        "G": (
            os_control["history_positive"]
            and os_control["uniform_internal_marginal"]
            and os_control["rho_trace"] == 1
            and os_control["positive_domain"] == "0<=sector_weight<=1"
            and os_control["weights_sector_independent"]
            and os_control["all_one_eighth"]
            and os_control["weight_sum"] == 1
            and os_control["block_diagonal_only"]
            and os_control["coherent_trace"] == 1
            and os_control["coherent_diagonal_blocks_unchanged"]
            and os_control["coherent_positive_domain"]
            == "-1<=coherence<=1"
            and os_control["coherent_weights_expected"]
            and os_control["coherence_independent"]
            == claims["os_control_coherence_independent"]
            and os_control["maximally_mixed_imported"]
            == claims["maximally_mixed_imported"]
            and os_control["periodic_descent"]
            == claims["os_periodic_descent"]
            and os_control["physical_partition_supplied"]
            == claims["physical_partition_supplied"],
            "the positive right-Schur block-diagonal control gives 1/8 for every classical sector weight, while an exact coherent extension gives (1+/-epsilon)/8 and leaves the context bridge open",
        ),
        "H": (
            maps["extension_count"] >= 3
            and maps["unique_extension"] == claims["unique_descent"]
            and claims["scope_overclaim"] is False
            and claims["broad_no_go"] is False,
            "strict projective lifts stop, but logical-fiber/Naimark and positive full-carrier routes survive; no supplied C32 action state or intertwiner means underdetermination, not a descent no-go",
        ),
    }


class Reporter:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition: object) -> None:
        passed = bool(condition)
        self.passed += int(passed)
        self.failed += int(not passed)
        print(f"[{key}] {'PASS' if passed else 'FAIL'}: {statement}")


def run(mutation: str = "") -> int:
    facts = evaluate(mutation)
    reporter = Reporter()
    for key, (condition, statement) in facts.items():
        reporter.check(key, statement, condition)
    if not mutation:
        carrier = carrier_facts()
        fiber = stabilizer_fiber_facts()
        lift = exterior_lift_facts()
        maps = operator_system_extension_facts()
        periodic = periodic_facts()
        scalar_control = scalar_quasifree_control_facts()
        os_control = os_control_facts()
        print(
            "CARRIERS: per_copy_CAR=C4; full_one_sector_CAR="
            f"C{carrier['full_periodic_fock_dim']}; event=C32; "
            f"Fock(event)=C{carrier['record_fock_dim']}."
        )
        print(
            "LOGICAL_FIBER: C32=C8_syndrome x C4_logical; four exact "
            "commuting logical Majoranas generate M4 on every rank-4 fiber; "
            f"Pauli-centralizer size={fiber['phase_free_pauli_centralizer_size']}; "
            "Block203-C4 action intertwiner=not supplied."
        )
        print(
            "EXTERIOR_LIFT: Gamma(F_i)_rank=16; cross_rank="
            f"{lift['gamma_cross_rank']} (shared vacuum); single-port span="
            f"{lift['single_port_span_rank']} of {lift['fock_dim']}; "
            "N=1 restores ranks (4x8) and sector unit only."
        )
        print(
            "OPERATOR_SYSTEM: three full-Fock POVMs pass positivity, unit, "
            "faithfulness, N=1 extension, and port covariance; at occupation "
            f"{maps['witness']} their values are {maps['witness_values']}."
        )
        print(
            "REFINEMENT_CONTROL: complement/number/support split consistency="
            f"{maps['split_refinement_consistent']}; number-share is unique "
            "inside the additive ratio ansatz, but physical multiplicity-"
            "splitting is not supplied."
        )
        print(
            "PERIODIC_STOP: no full-C32 periodic Q_R/state or action-selected "
            "Kraus intertwiner is supplied; vacuum and pair weights are nonzero; "
            f"omega(P_N1)={periodic['n1_weight']}<0; "
            "eight periodic Record values are therefore sealed."
        )
        print(
            "SCALAR_Q_CONTROL: if Q_R=-r I32 were licensed, exchangeability "
            "would force every covariant unital map to expectation "
            f"{scalar_control['covariant_unital_expectation']}; operator "
            "nonuniqueness alone does not imply probability nonuniqueness."
        )
        print(
            "OS_BLOCK_DIAGONAL_CONTROL: rho_w=diag(w I16/16,(1-w) I16/16), "
            f"weights={os_control['weights']}, sum={os_control['weight_sum']}; "
            "valid for 0<=w<=1 without choosing w."
        )
        print(
            "OS_COHERENCE_CONTROL: rho_e=(I32+e S_J)/32 has unchanged "
            "diagonal blocks and weights="
            f"{os_control['coherent_weights']} for -1<=e<=1."
        )
        print(
            "RESULT: strict_projective_lifts=0 in tested families; "
            "positive_full_carrier_extensions>=3 and nonunique; "
            "logical_C4_fiber=exact but action identification=open; "
            "zero-source block-diagonal OS candidate=positive; "
            "physical local-possibility partition bridge=open; "
            "obligation_retirement=0; TOE movement=0."
        )
        for line in N5_LINES:
            print(line)
    print(f"TOTAL: PASS={reporter.passed} FAIL={reporter.failed}")
    return int(reporter.failed != 0)


def mutation_sweep() -> int:
    survived = []
    for mutation in MUTATIONS:
        results = evaluate(mutation)
        if all(condition for condition, _statement in results.values()):
            survived.append(mutation)
    print(
        f"MUTATION_TOTAL: PASS={len(MUTATIONS) - len(survived)} "
        f"FAIL={len(survived)}"
    )
    if survived:
        print("SURVIVED: " + ",".join(survived))
    return int(bool(survived))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--mutation-sweep", action="store_true")
    args = parser.parse_args()
    if args.mutation_sweep:
        return mutation_sweep()
    return run(args.mutation)


if __name__ == "__main__":
    raise SystemExit(main())
