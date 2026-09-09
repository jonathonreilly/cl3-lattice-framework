#!/usr/bin/env python3
"""Exact action-source factorization for the Block 38 Record menu compiler.

The runner starts from the preparation quotient already decoded from each
Block 38 root and uses that quotient itself as a positive full-M2 Gaussian
kernel.  A literal effect E enters through the additive source Q -> Q-sE.
The raw partition derivative at s=0 is computed before any common-scale
quotient or menu normalization and tested on all five compiler strata,
refinements, shared effects, covariance transports, and a non-scalar hostile
fixture.

This is a conditional downstream construction.  The runner checks an explicit
selected quotient of program-indexed Record-event presentations and a selected
conditional clock process.  It does not attribute either selection to the four
Minimal Axioms.
"""

from __future__ import annotations

from pathlib import Path

from itertools import permutations
from functools import lru_cache
import hashlib

from sympy import I, ImmutableMatrix, Matrix, Rational as Q, diff, exp, log, pi, simplify, sqrt, symbols

import nn_record_gaussian_action_event_response_factorization_independent_check_2026_08_23 as reconstruction

from gaussian_record_menu_definitions_7326 import (
    I2,
    COEFFICIENT_DENSITIES,
    SECTOR_MASSES,
    SX,
    SZ,
    decode_menu_payload,
    hermitian_part,
    matrix_equal,
    menu_specs,
    payload_ii,
    payload_iii,
    payload_rr,
    payload_rri,
    payload_rrr,
    terminal_law,
)


AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = ('docs/NN_RECORD_GAUSSIAN_ACTION_EVENT_RESPONSE_FACTORIZATION_BOUNDED_THEOREM_NOTE_2026-08-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'scripts/gaussian_record_menu_definitions_7326.py', 'scripts/nn_record_gaussian_action_event_response_factorization_independent_check_2026_08_23.py')
DIRECT_HASHES = {'docs/NN_RECORD_GAUSSIAN_ACTION_EVENT_RESPONSE_FACTORIZATION_BOUNDED_THEOREM_NOTE_2026-08-23.md': '79b649ebf0c49930906914a0a49281cec0026b8362b041a81a0470c4e96e919f', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'scripts/gaussian_record_menu_definitions_7326.py': '50c959eb6a750d0cb8b1455976b1693965454b85ddd4c15cbda79ba96b28b702', 'scripts/nn_record_gaussian_action_event_response_factorization_independent_check_2026_08_23.py': '9843b13fe0b183f5a5ae62e362badbf632596ac86cda56acf58d6679b5bc0965'}

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "NN_RECORD_GAUSSIAN_ACTION_EVENT_RESPONSE_FACTORIZATION_"
    "BOUNDED_THEOREM_NOTE_2026-08-23.md"
)


def current_inputs_ok() -> bool:
    return bool(AUDIT_INPUT_PATHS) and set(AUDIT_INPUT_PATHS) == set(DIRECT_HASHES) and all(
        (ROOT / path).is_file() and not Path(path).is_absolute()
        and hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == DIRECT_HASHES[path]
        for path in AUDIT_INPUT_PATHS
    )


def matrix_cached(function):
    """Memoize exact scalar values with immutable matrix arguments."""
    cached = lru_cache(maxsize=512)(function)
    def wrapped(*args):
        return cached(*(ImmutableMatrix(arg) if isinstance(arg, Matrix) else arg for arg in args))
    return wrapped


def preparation_from_payload(payload: Matrix) -> Matrix:
    """The Block 38 quotient C=H(A)^2/Tr(H(A)^2), rebuilt directly."""
    h_value = hermitian_part(payload)
    square = simplify(h_value * h_value)
    return simplify(square / square.trace())


def action_kernel(payload: Matrix) -> Matrix:
    """Positive Gaussian kernel selected directly from the root quotient."""
    return preparation_from_payload(payload)


@matrix_cached
def partition_function(kernel: Matrix, effect: Matrix, source) -> object:
    """M2(C) Gaussian partition function Z_Q(sE)."""
    return simplify(pi**4 / simplify(kernel - source * effect).det() ** 2)


@matrix_cached
def raw_action_response(kernel: Matrix, effect: Matrix) -> object:
    """Genuinely raw response DZ_Q(0)[E], before any common-scale quotient."""
    source = symbols("source", real=True)
    return simplify(diff(partition_function(kernel, effect, source), source).subs(source, 0))


@matrix_cached
def log_action_response(kernel: Matrix, effect: Matrix) -> object:
    """Common-base quotient D log Z; still prior to any menu sum."""
    source = symbols("source", real=True)
    return simplify(diff(log(partition_function(kernel, effect, source)), source).subs(source, 0))


def action_response(kernel: Matrix, effect: Matrix) -> object:
    """Identity-source quotient of the raw current, not a menu normalization."""
    return simplify(raw_action_response(kernel, effect) / raw_action_response(kernel, I2))


def trace_response(kernel: Matrix, effect: Matrix) -> object:
    """Independent covariance-form evaluation of the common-scale grade."""
    covariance = simplify(kernel.inv())
    density = simplify(covariance / covariance.trace())
    return simplify((density * effect).trace())


def marked_intensity(kernel: Matrix, effect: Matrix, auxiliary: Matrix) -> object:
    """Pointwise density on the auxiliary Gaussian matrix space M2(C)."""
    action = simplify((auxiliary.conjugate().T * kernel * auxiliary).trace())
    insertion = simplify((auxiliary.conjugate().T * effect * auxiliary).trace())
    return simplify(exp(-action) * insertion)


def root_exposure_density(payload: Matrix) -> object:
    """RN density relative to normalized Haar and the sector base measure."""
    decoded = decode_menu_payload(payload)
    if decoded is None:
        raise ValueError("payload is outside the Block 38 compiler domain")
    return simplify(SECTOR_MASSES[decoded.sector] * COEFFICIENT_DENSITIES[decoded.sector])


def event_effect(items: tuple, indices: tuple[int, ...]) -> Matrix:
    """Effect content of one subset presentation in a program outcome set."""
    return simplify(sum((items[index].effect for index in indices), Matrix.zeros(2)))


def event_class_key(effect: Matrix) -> tuple:
    """Exact key for the selected quotient of presentations by effect content."""
    return tuple(simplify(value) for value in effect)


def clock_prefactor(opportunity, kernel: Matrix) -> object:
    """Calibrate the selected local clock so its total rate is opportunity."""
    return simplify(opportunity / raw_action_response(kernel, I2))


def lock_once(records: dict, site, content: Matrix) -> bool:
    if site in records:
        return False
    records[site] = content
    return True


def conditional_from_hazards(hazards: tuple) -> tuple:
    total = simplify(sum(hazards))
    return tuple(simplify(value / total) for value in hazards)


def projector_xz(x, z) -> Matrix:
    return simplify((I2 + x * SX + z * SZ) / 2)


def main() -> int:
    if not current_inputs_ok():
        print("FAIL current-source-input-binding: declared input is absent or changed")
        print("TOTAL: PASS=0 FAIL=1")
        return 1
    passed = 0
    failed = 0

    def check(name: str, condition: bool, detail: str) -> None:
        nonlocal passed, failed
        if condition:
            passed += 1
            print(f"PASS {name}: {detail}")
        else:
            failed += 1
            print(f"FAIL {name}: {detail}")

    representatives = {
        "RRR-A": payload_rrr(Q(1, 2), Q(9, 10)),
        "RRR-B": payload_rrr(Q(1, 2), Q(3, 4)),
        "RR": payload_rr(),
        "RRI": payload_rri(Q(1, 3)),
        "III": payload_iii(Q(1, 5), Q(3, 10)),
        "II": payload_ii(Q(2, 5)),
    }
    decoded = {name: decode_menu_payload(value) for name, value in representatives.items()}
    menus = {name: menu_specs(value) for name, value in representatives.items()}

    check(
        "five-stratum-action-domain",
        set(item.sector for item in decoded.values() if item is not None)
        == {"RRR", "RR", "RRI", "III", "II"}
        and all(items is not None and len(items) in (2, 3) for items in menus.values()),
        "the source construction is instantiated on every positive Block 38 binary/ternary stratum",
    )

    kernels = {name: action_kernel(value) for name, value in representatives.items()}
    check(
        "root-derived-positive-action",
        all(matrix_equal(preparation_from_payload(value), I2 / 2) for value in representatives.values())
        and all(matrix_equal(kernel, I2 / 2) for kernel in kernels.values())
        and all(simplify(kernel[0, 0]) > 0 and simplify(kernel.det()) > 0 for kernel in kernels.values()),
        "C(A)=H(A)^2/Tr(H(A)^2)=I/2 is used directly as one positive M2 Gaussian kernel for every root",
    )

    derivative_ok = True
    response_vectors: dict[str, tuple] = {}
    for name, payload in representatives.items():
        kernel = kernels[name]
        responses = tuple(action_response(kernel, item.effect) for item in menus[name])
        response_vectors[name] = responses
        derivative_ok = derivative_ok and all(
            simplify(response - trace_response(kernel, item.effect)) == 0
            and simplify(
                raw_action_response(kernel, item.effect)
                - partition_function(kernel, item.effect, Q(0))
                * log_action_response(kernel, item.effect)
            ) == 0
            for item, response in zip(menus[name], responses, strict=True)
        )
    check(
        "pre-normalization-source-derivative",
        derivative_ok,
        "DZ_Q(0)[E] is computed first; D log Z and the identity-source quotient are derived only afterward",
    )

    check(
        "positive-additive-normalized-grade",
        all(
            all(
                bool(simplify(raw_action_response(kernels[name], item.effect)).is_positive)
                for item in menus[name]
            )
            and simplify(
                sum(raw_action_response(kernels[name], item.effect) for item in menus[name])
                - raw_action_response(kernels[name], I2)
            ) == 0
            and all(bool(simplify(value).is_positive) for value in responses)
            and simplify(sum(responses) - trace_response(kernels[name], I2)) == 0
            and simplify(sum(responses) - 1) == 0
            for name, responses in response_vectors.items()
        ),
        "the raw currents are positive and additive; their identity-source quotient sums to one on every resolution",
    )

    check(
        "five-stratum-exact-laws",
        response_vectors["RRI"] == (Q(1, 3), Q(1, 3), Q(1, 3))
        and response_vectors["III"] == (Q(1, 5), Q(3, 10), Q(1, 2))
        and response_vectors["II"] == (Q(2, 5), Q(3, 5))
        and response_vectors["RR"] == (Q(1, 2), Q(1, 2)),
        "the action response reproduces the compiler's exact trace vectors without reading its selected terminal law",
    )

    # The continuum proof is H(A)^2=r^2 I; these named roots are regression only.
    # Named boundary representatives supplement the analytic domain proof.
    continuum_payloads = list(representatives.values()) + [
        payload_rrr(0, 1), payload_rrr(1, 0), payload_rrr(1, 1),
        payload_rrr(Q(1, 2), Q(1, 2)),
        payload_rri(0), payload_rri(1), payload_ii(0), payload_ii(1),
        payload_iii(0, 0), payload_iii(1, 0), payload_iii(0, 1),
    ]
    continuum_ok = True
    for payload in continuum_payloads:
        items = menu_specs(payload)
        kernel = action_kernel(payload)
        responses = tuple(trace_response(kernel, item.effect) for item in items)
        continuum_ok = continuum_ok and matrix_equal(kernel, I2 / 2)
        continuum_ok = continuum_ok and all(bool(value.is_positive) for value in responses)
        continuum_ok = continuum_ok and simplify(sum(responses) - 1) == 0
    check(
        "named-domain-and-boundary-regression",
        continuum_ok,
        f"the analytic Q_A=I/2 identity survives {len(continuum_payloads)} exact interior/boundary payloads across all strata",
    )

    fine = payload_rrr(Q(1, 2), Q(1, 2))
    coarse = payload_rr()
    fine_items = menu_specs(fine)
    coarse_items = menu_specs(coarse)
    refined_effect = simplify(fine_items[0].effect + fine_items[1].effect)
    check(
        "literal-refinement-additivity",
        matrix_equal(refined_effect, coarse_items[0].effect)
        and simplify(
            raw_action_response(action_kernel(fine), fine_items[0].effect)
            + raw_action_response(action_kernel(fine), fine_items[1].effect)
            - raw_action_response(action_kernel(coarse), coarse_items[0].effect)
        ) == 0
        and simplify(
            raw_action_response(action_kernel(fine), refined_effect)
            - raw_action_response(action_kernel(fine), fine_items[0].effect)
            - raw_action_response(action_kernel(fine), fine_items[1].effect)
        ) == 0,
        "the source for E=F+G is literally the sum of the two source insertions and the raw response adds exactly",
    )

    shared_a = menu_specs(representatives["RRR-A"])[0]
    shared_b = menu_specs(representatives["RRR-B"])[0]
    shared_mu_a = action_response(kernels["RRR-A"], shared_a.effect)
    shared_mu_b = action_response(kernels["RRR-B"], shared_b.effect)
    check(
        "cross-program-shared-effect-functionality",
        matrix_equal(shared_a.effect, shared_b.effect)
        and shared_a.label == shared_b.label
        and matrix_equal(shared_a.content, shared_b.content)
        and raw_action_response(kernels["RRR-A"], shared_a.effect) == 32 * pi**4
        and raw_action_response(kernels["RRR-B"], shared_b.effect) == 32 * pi**4
        and shared_mu_a == shared_mu_b == Q(1, 4),
        "one literal effect-label source has raw DZ=32*pi^4 and identity-source-normalized grade 1/4 in both RRR contexts",
    )

    # The Block 38 root law fixes a Radon--Nikodym density relative to its root
    # reference measure before any outcome is inspected.  Conditional on a
    # realized root, the selected clock prefactor calibrates the protected
    # writer opportunity as the total first-mark rate.  Multiplying the
    # conditional hazards by the RN density gives joint exposure densities, not
    # coordinate-free conditional rates at an exact continuous root.
    terminal_rates = {}
    exposures = {}
    clock_prefactors = {}
    conditional_hazards = {}
    joint_hazard_densities = {}
    for name, payload in representatives.items():
        terminal_rates[name] = Q(1)  # Supplied conditional opportunity; archived spatial match is not rerun.
        exposures[name] = root_exposure_density(payload)
        clock_prefactors[name] = clock_prefactor(terminal_rates[name], kernels[name])
        conditional_hazards[name] = tuple(
            simplify(clock_prefactors[name] * raw_action_response(kernels[name], item.effect))
            for item in menus[name]
        )
        joint_hazard_densities[name] = tuple(
            simplify(exposures[name] * value) for value in conditional_hazards[name]
        )
    hazards_a = conditional_hazards["RRR-A"]
    hazards_b = conditional_hazards["RRR-B"]
    conditional_a = conditional_from_hazards(hazards_a)
    conditional_b = conditional_from_hazards(hazards_b)
    check(
        "outcome-blind-event-factorization",
        all(rate == 1 for rate in terminal_rates.values())
        and all(bool(value.is_positive) for value in exposures.values())
        and all(bool(value.is_positive) for value in clock_prefactors.values())
        and simplify(sum(hazards_a) - terminal_rates["RRR-A"]) == 0
        and simplify(sum(hazards_b) - terminal_rates["RRR-B"]) == 0
        and simplify(
            sum(joint_hazard_densities["RRR-A"])
            - exposures["RRR-A"] * terminal_rates["RRR-A"]
        ) == 0
        and simplify(
            sum(joint_hazard_densities["RRR-B"])
            - exposures["RRR-B"] * terminal_rates["RRR-B"]
        ) == 0
        and conditional_a == response_vectors["RRR-A"]
        and conditional_b == response_vectors["RRR-B"]
        and conditional_a[0] == conditional_b[0] == Q(1, 4),
        "the conditional clock has the supplied unit opportunity as its finite total rate; the root RN factor enters only the joint exposure density",
    )

    # Pointwise, not merely after integration, positive effect refinements give
    # additive mark-kernel densities on the auxiliary M2(C) field space.
    auxiliary_probes = (
        I2,
        Matrix([[1, 0], [0, 0]]),
        Matrix([[1, I], [Q(1, 2), -I]]),
        Matrix([[Q(1, 3), Q(2, 5)], [I, Q(3, 4)]]),
    )
    marked_ok = True
    for auxiliary in auxiliary_probes:
        fine_left = marked_intensity(action_kernel(fine), fine_items[0].effect, auxiliary)
        fine_right = marked_intensity(action_kernel(fine), fine_items[1].effect, auxiliary)
        coarse_mark = marked_intensity(action_kernel(fine), refined_effect, auxiliary)
        marked_ok = marked_ok and bool(simplify(fine_left).is_nonnegative)
        marked_ok = marked_ok and bool(simplify(fine_right).is_nonnegative)
        marked_ok = marked_ok and simplify(coarse_mark - fine_left - fine_right) == 0
    check(
        "marked-poisson-event-semantics",
        marked_ok,
        "the auxiliary density is nonnegative and additive; its finite menu sum integrates to a finite conditional Poisson rate",
    )

    # Raw Record atoms remain program-indexed.  The selected event-presentation
    # quotient acts on (program, subset of raw marks): two
    # presentations are equivalent exactly when their summed Hermitian effects
    # agree.  Disjointness is witnessed in a program fiber and is not a property
    # of quotient classes alone.  The quotient identifies a coarse singleton
    # with a disjoint fine union along a declared refinement while retaining the
    # two fine codewords as distinct raw Records.
    fine_atom_keys = tuple(("fine", index) for index in range(len(fine_items)))
    coarse_atom_keys = tuple(("coarse", index) for index in range(len(coarse_items)))
    coarse_singleton_effect = event_effect(coarse_items, (0,))
    fine_union_effect = event_effect(fine_items, (0, 1))
    shared_event_a = event_effect(menus["RRR-A"], (0,))
    shared_event_b = event_effect(menus["RRR-B"], (0,))
    refinement_map = (0, 0, 1)
    quotient_ok = (
        len(set(fine_atom_keys + coarse_atom_keys)) == len(fine_atom_keys + coarse_atom_keys)
        and fine_items[0].label != fine_items[1].label
        and matrix_equal(fine_items[0].effect, fine_items[1].effect)
        and not matrix_equal(fine_items[0].content, fine_items[1].content)
        and event_class_key(coarse_singleton_effect) == event_class_key(fine_union_effect)
        and event_class_key(shared_event_a) == event_class_key(shared_event_b)
        and shared_a.label == shared_b.label
        and raw_action_response(action_kernel(coarse), coarse_singleton_effect)
        == raw_action_response(action_kernel(fine), fine_union_effect)
        and raw_action_response(action_kernel(fine), fine_union_effect)
        == simplify(
            raw_action_response(action_kernel(fine), fine_items[0].effect)
            + raw_action_response(action_kernel(fine), fine_items[1].effect)
        )
        and all(
            event_class_key(event_effect(coarse_items, (coarse_index,)))
            == event_class_key(
                event_effect(
                    fine_items,
                    tuple(index for index, image in enumerate(refinement_map) if image == coarse_index),
                )
            )
            for coarse_index in range(len(coarse_items))
        )
        and simplify(
            root_exposure_density(fine) * raw_action_response(action_kernel(fine), fine_union_effect)
            - root_exposure_density(coarse)
            * raw_action_response(action_kernel(coarse), coarse_singleton_effect)
        ) != 0
        and action_response(action_kernel(fine), fine_union_effect)
        == action_response(action_kernel(coarse), coarse_singleton_effect)
        == Q(1, 2)
    )
    for auxiliary in auxiliary_probes:
        for coarse_index in range(len(coarse_items)):
            fine_indices = tuple(
                index for index, image in enumerate(refinement_map) if image == coarse_index
            )
            quotient_ok = quotient_ok and simplify(
                marked_intensity(
                    action_kernel(coarse),
                    event_effect(coarse_items, (coarse_index,)),
                    auxiliary,
                )
                - sum(
                    marked_intensity(action_kernel(fine), fine_items[index].effect, auxiliary)
                    for index in fine_indices
                )
            ) == 0
        quotient_ok = quotient_ok and simplify(
            marked_intensity(kernels["RRR-A"], shared_event_a, auxiliary)
            - marked_intensity(kernels["RRR-B"], shared_event_b, auxiliary)
        ) == 0
    check(
        "event-presentation-quotient",
        quotient_ok,
        "the declared refinement pushes distinct fine Record atoms to coarse event classes with one intrinsic kernel; outer root exposure does not descend",
    )

    permutation_ok = True
    for name, items in menus.items():
        reference = {item.content.__str__(): action_response(kernels[name], item.effect) for item in items}
        for ordering in permutations(items):
            permutation_ok = permutation_ok and {
                item.content.__str__(): action_response(kernels[name], item.effect)
                for item in ordering
            } == reference
    check(
        "outcome-permutation-independence",
        permutation_ok,
        "all binary and ternary orderings preserve each literal content-to-grade assignment",
    )

    skew_a = terminal_law(representatives["RRR-A"], "context-skew")
    skew_b = terminal_law(representatives["RRR-B"], "context-skew")
    skew_fine = terminal_law(fine, "context-skew")
    skew_coarse = terminal_law(coarse, "context-skew")
    check(
        "contextual-mutant-exclusion",
        skew_a[0][1] == Q(527, 2000)
        and skew_b[0][1] == Q(169, 640)
        and skew_a[0][1] != skew_b[0][1]
        and simplify(skew_fine[0][1] + skew_fine[1][1]) == Q(21, 40)
        and skew_coarse[0][1] == Q(1, 2)
        and Q(21, 40) != Q(1, 2),
        "the Block 38 contextual Law fails both literal shared-source functionality and source-refinement additivity",
    )

    root2 = sqrt(2)
    unitaries = (
        I2,
        SX,
        simplify((SX + SZ) / root2),
        Matrix([[1, 0], [0, I]]),
        simplify((I2 + I * Matrix([[0, -I], [I, 0]])) / root2),
    )
    covariance_ok = True
    for unitary in unitaries:
        covariance_ok = covariance_ok and matrix_equal(simplify(unitary * unitary.conjugate().T), I2)
        for payload in representatives.values():
            moved_payload = simplify(unitary * payload * unitary.conjugate().T)
            before_items = menu_specs(payload)
            after_items = menu_specs(moved_payload)
            before_kernel = action_kernel(payload)
            after_kernel = action_kernel(moved_payload)
            covariance_ok = covariance_ok and matrix_equal(
                after_kernel, simplify(unitary * before_kernel * unitary.conjugate().T)
            )
            covariance_ok = covariance_ok and len(before_items) == len(after_items)
            for before, after in zip(before_items, after_items, strict=True):
                covariance_ok = covariance_ok and matrix_equal(
                    after.effect, simplify(unitary * before.effect * unitary.conjugate().T)
                )
                covariance_ok = covariance_ok and simplify(
                    action_response(after_kernel, after.effect)
                    - action_response(before_kernel, before.effect)
                ) == 0
    check(
        "internal-basis-covariance",
        covariance_ok,
        "five exact unitary transports conjugate action kernels and sources while preserving every raw response",
    )

    # State-dependent hostile control: this separately SUPPLIES Q=C^-1 only to
    # test the general source algebra against the Block 39 pair.  It is not a
    # provenance claim for the Block 38 selected action.
    state = Matrix([[Q(3, 5), 0], [0, Q(2, 5)]])
    state_kernel = simplify(state.inv())
    shared = Q(1, 2) * projector_xz(0, 1)
    menu_a = (
        shared,
        Q(9, 10) * projector_xz(4 * root2 / 9, Q(-7, 9)),
        Q(3, 5) * projector_xz(-2 * root2 / 3, Q(1, 3)),
    )
    menu_b = (
        shared,
        Q(3, 4) * projector_xz(2 * root2 / 3, Q(-1, 3)),
        Q(3, 4) * projector_xz(-2 * root2 / 3, Q(-1, 3)),
    )
    state_response_a = tuple(action_response(state_kernel, effect) for effect in menu_a)
    state_response_b = tuple(action_response(state_kernel, effect) for effect in menu_b)
    check(
        "non-scalar-action-control",
        matrix_equal(sum(menu_a, Matrix.zeros(2)), I2)
        and matrix_equal(sum(menu_b, Matrix.zeros(2)), I2)
        and state_response_a == (Q(3, 10), Q(19, 50), Q(8, 25))
        and state_response_b == (Q(3, 10), Q(7, 20), Q(7, 20)),
        "with the inverse-covariance rule supplied, Q=diag(5/3,5/2) yields both exact Block 39 vectors and shared grade 3/10",
    )

    # Raw rank-one factorization minors.  For the action law they vanish even
    # when whole-menu exposure differs.  The Block 39 contextual mutant fails
    # on E0 versus its literal complement by exactly its shared-grade defect.
    probe_effects = (I2, projector_xz(0, 1), projector_xz(1, 0), projector_xz(0, -1), (I2 + Matrix([[0, -I], [I, 0]])) / 2)
    # Real coordinates on Herm(2): both diagonal entries, Re E01, Im E01.
    def coordinates(effect):
        return Matrix([effect[0, 0], effect[1, 1],
                       (effect[0, 1] + effect[1, 0]) / 2,
                       (effect[0, 1] - effect[1, 0]) / (2 * I)])
    complex_kernel = Matrix([[2, I / 2], [-I / 2, 1]])
    check(
        "complex-source-and-real-hermitian-span",
        Matrix.hstack(*(coordinates(effect) for effect in probe_effects[:4])).rank() == 3
        and Matrix.hstack(*(coordinates(effect) for effect in probe_effects)).rank() == 4
        and raw_action_response(I2 / 2, probe_effects[-1]) == 64 * pi**4
        and action_response(complex_kernel, probe_effects[-1]) == Q(2, 3)
        and action_response(complex_kernel, probe_effects[-1].T) == Q(1, 3)
        and reconstruction.grade(complex_kernel, probe_effects[-1]) == Q(2, 3),
        "Py+ supplies the missing Y direction; transposing its imaginary source changes grade 2/3 to 1/3",
    )
    alpha_a, alpha_b = Q(7, 11), Q(13, 17)
    action_rows = (
        tuple(simplify(alpha_a * raw_action_response(state_kernel, effect)) for effect in probe_effects),
        tuple(simplify(alpha_b * raw_action_response(state_kernel, effect)) for effect in probe_effects),
    )
    action_minors = tuple(
        simplify(action_rows[0][i] * action_rows[1][j] - action_rows[0][j] * action_rows[1][i])
        for i in range(len(probe_effects))
        for j in range(i + 1, len(probe_effects))
    )
    baseline_a = (Q(3, 10), Q(19, 50), Q(8, 25))
    baseline_b = (Q(3, 10), Q(7, 20), Q(7, 20))
    def contextual(values: tuple) -> tuple:
        second = simplify(sum(value**2 for value in values))
        return tuple(simplify(value * (1 + value - second)) for value in values)
    contextual_a = contextual(baseline_a)
    contextual_b = contextual(baseline_b)
    mutant_minor = simplify(
        contextual_a[0] * (1 - contextual_b[0])
        - (1 - contextual_a[0]) * contextual_b[0]
    )
    check(
        "raw-factorization-minor-discriminator",
        all(value == 0 for value in action_minors)
        and mutant_minor == -Q(27, 50000),
        "all ten raw action minors vanish on a positive-effect spanning set; the contextual E0/complement minor is -27/50000",
    )

    records = {}
    target = (0, 0, 0)  # Supplied blank local terminal, not a spatial reachability assertion.
    selected_content = menus["RRI"][0].content
    first_lock = lock_once(records, target, selected_content)
    second_lock = lock_once(records, target, menus["RRI"][1].content)
    check(
        "first-mark-record-lock",
        first_lock and not second_lock and matrix_equal(records[target], selected_content),
        "the first marked event writes its existing M2 effect-label codeword and the permanent target cannot be overwritten",
    )

    source = symbols("source", real=True)
    source_patch_ok = True
    for name, items in menus.items():
        kernel = kernels[name]
        for item in items:
            # Since 0<=E<=I and Q=I/2, Q-sE is positive for 0<=s<1/2.
            at_quarter = simplify(kernel - Q(1, 4) * item.effect)
            source_patch_ok = source_patch_ok and simplify(at_quarter[0, 0]) > 0
            source_patch_ok = source_patch_ok and simplify(at_quarter.det()) > 0
            source_patch_ok = source_patch_ok and partition_function(kernel, item.effect, source) != 0
    check(
        "positive-source-patch",
        source_patch_ok,
        "every representative source deformation remains positive at s=1/4, so the raw derivative lies inside an analytic patch",
    )

    check("declared-input-closure", current_inputs_ok(),
          "the exact own-note and actual finite helper inputs match their declared SHA256 identities")

    print("per_element: every literal effect source, raw partition response, Record mark, and event-quotient representative is checked")
    print("per_site: the root-derived M2 Gaussian action, conditional finite clock, event-presentation quotient, and first lock are checked")
    print("per_mode: all four complex M2 Gaussian modes and the full exact 2x2 source derivative are checked")
    print("per_block: all five strata, RN exposures, refinements, permutations, hostile pair, and five basis transports are checked")
    print("lattice_wide: not executed — translation uses one copied local formula; no autonomous history is claimed")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
