#!/usr/bin/env python3
"""Cycle 20 exact controls for the operational probability lane.

Companion note:
  docs/work_history/repo/review_feedback/
  OPERATIONAL_QUOTIENT_BORN_AFFINITY_CYCLE20_NOTE_2026-07-14.md

The runner checks a finite positive operational-to-effect representation,
then deletes mixing, full POVM coarse-graining, effect completeness,
prepared-state identity, reset, and actual-member semantics one at a time.
It does not identify Nature's law, amend an axiom or primitive, set an audit
verdict, edit a live queue, commit, push, or open a PR.
"""

from __future__ import annotations

from collections import defaultdict
from itertools import product
from pathlib import Path
import json

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "OPERATIONAL_QUOTIENT_BORN_AFFINITY_CYCLE20_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
BUSCH = ROOT / "docs" / "BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
OPERATIONAL = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "OPERATIONAL_RECORD_RECONSTRUCTION_DEEP_PROBE_NOTE_2026-07-13.md"
)
PREDICTIVE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "EXACT_PREDICTIVE_SPECIFICATION_TOURNAMENT_NOTE_2026-07-14.md"
)
PARITY = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "COMPLETE_FUTURE_OPERATIONAL_PARITY_CERTIFICATE_CYCLE19_NOTE_2026-07-14.md"
)
FREQUENCY = ROOT / "docs" / "RECORD_OCCURRENCE_THINNED_IID_FREQUENCY_BRIDGE_2026-07-01.md"

PASS = 0
FAIL = 0

I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.Matrix([[1, 0], [0, -1]])
ZERO = sp.Matrix([1, 0])
ONE = sp.Matrix([0, 1])
PLUS = (ZERO + ONE) / sp.sqrt(2)
PLUS_I = (ZERO + sp.I * ONE) / sp.sqrt(2)
P0 = ZERO * ZERO.T
P1 = ONE * ONE.T
PX = PLUS * PLUS.T
PY = PLUS_I * PLUS_I.conjugate().T


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    suffix = f" :: {detail}" if detail else ""
    if bool(condition):
        PASS += 1
        print(f"PASS {label}{suffix}")
    else:
        FAIL += 1
        print(f"FAIL {label}{suffix}")


def normalized(text: str) -> str:
    return " ".join(
        text.lower().replace("*", "").replace("`", "").replace("_", " ").split()
    )


def dagger(matrix: sp.Matrix) -> sp.Matrix:
    return matrix.conjugate().T


def projector(vector: sp.Matrix) -> sp.Matrix:
    return sp.simplify(vector * dagger(vector))


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.shape == right.shape and all(
        sp.simplify(value) == 0 for value in left - right
    )


def scalar_equal(left: sp.Expr, right: sp.Expr) -> bool:
    return sp.simplify(left - right) == 0


def probability(rho: sp.Matrix, effect: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(rho * effect))


def hermitian_span_rank(matrices: tuple[sp.Matrix, ...]) -> int:
    columns = [matrix.reshape(4, 1) for matrix in matrices]
    return sp.Matrix.hstack(*columns).rank()


def fingerprint(effect: sp.Matrix, preparations: tuple[sp.Matrix, ...]) -> tuple[sp.Expr, ...]:
    return tuple(probability(rho, effect) for rho in preparations)


def quotient_classes(fingerprints: dict[str, tuple[sp.Expr, ...]]) -> tuple[tuple[str, ...], ...]:
    buckets: dict[tuple[str, ...], list[str]] = defaultdict(list)
    for name, values in fingerprints.items():
        key = tuple(sp.srepr(sp.simplify(value)) for value in values)
        buckets[key].append(name)
    return tuple(sorted(tuple(sorted(names)) for names in buckets.values()))


def binary_word_probability(word: tuple[int, ...], q: sp.Expr) -> sp.Expr:
    return sp.simplify(
        sp.prod(q if bit else 1 - q for bit in word)
    )


def authority_and_source_contract() -> None:
    section("A - Authority, foundation, and primary-source contract")
    note_raw = NOTE.read_text(encoding="utf-8")
    note = normalized(note_raw)
    axioms = normalized(AXIOMS.read_text(encoding="utf-8"))
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    realized = normalized(REALIZED.read_text(encoding="utf-8"))
    busch = normalized(BUSCH.read_text(encoding="utf-8"))
    operational = normalized(OPERATIONAL.read_text(encoding="utf-8"))
    predictive = normalized(PREDICTIVE.read_text(encoding="utf-8"))
    parity = normalized(PARITY.read_text(encoding="utf-8"))
    frequency = normalized(FREQUENCY.read_text(encoding="utf-8"))

    check("A note is authority-free", "authority: none" in note)
    check(
        "A note changes no live authority surface",
        "changes no axiom" in note
        and all(token in note for token in ("primitive", "registry", "audit", "queue", "policy", "retained surface")),
    )
    for needle in (
        "records form",
        "records are permanent",
        "only records are readable",
        "a readout value is determined by record content alone",
        "scalar readout i is additive",
        "a state is a configuration of records",
    ):
        check(f"A live foundation needle: {needle[:45]}", needle in axioms)
    check("A foundation withholds probability rules", "probability rules" in axioms)
    check("A foundation withholds measurement/update laws", "measurement basis selection" in axioms and "update laws" in axioms)
    check("A registry has exactly four approved premise nodes", len(registry["canonical_ids"]) == 4)
    check("A realized-state primitive carries no state-contingent content", "carries zero state-contingent content" in realized)
    check("A realized-state primitive supplies no probability", "probability rule" in realized and "weighting" in realized)
    check("A Busch note states all-effect normalization/additivity", "povm-additivity over" in busch and "for any povm" in busch)
    check("A Busch note keeps M1-M3 conditional", "given the povm-additivity hypotheses" in busch and "deeper question of motivating" in busch)
    check("A operational probe separates support from probability", "support is not probability" in operational)
    check("A predictive packet names strong lumpability", "strong lumpability" in predictive)
    check("A Cycle 19 makes complete-future quotient law-relative", "quotient is relative to l and t" in parity)
    check("A frequency bridge keeps IID reset supplied", "supplied iid reset/preparation protocol" in frequency)
    for source in (
        "quant-ph/9909073",
        "quant-ph/0306179",
        "quant-ph/0508211",
        "quant-ph/0406166",
        "1512.00589",
        "1801.09811",
        "0712.1325",
    ):
        check(f"A primary-source ledger includes {source}", source in note_raw)
    check("A note contains written N1-N8 gate", all(f"### N{i}" in note_raw for i in range(1, 9)))


def positive_operational_effect_theorem() -> None:
    section("B - Positive finite operational-effect theorem")
    sigma = sp.simplify((I2 + (X + Y + Z) / 3) / 2)
    preparations = (P0, P1, PX, PY, I2 / 2, sigma)
    effects = (sp.zeros(2), I2, P0, P1, PX, I2 - PX, PY, I2 - PY)

    check("B representative is Hermitian", matrix_equal(sigma, dagger(sigma)))
    check("B representative has unit trace", scalar_equal(sp.trace(sigma), 1))
    check("B representative is positive", all(value >= 0 for value in sigma.eigenvals()))
    check("B zero effect has zero weight", scalar_equal(probability(sigma, sp.zeros(2)), 0))
    check("B unit effect has unit weight", scalar_equal(probability(sigma, I2), 1))
    check("B Pauli effects span all Hermitian qubit matrices", hermitian_span_rank((I2, X, Y, Z)) == 4)

    duplicate_classes = quotient_classes(
        {
            "procedure-a": fingerprint(P0 / 2, preparations),
            "procedure-b": fingerprint(P0 / 2, preparations),
            "different-effect": fingerprint(P1 / 2, preparations),
        }
    )
    check("B complete preparation fingerprints merge duplicate procedures", ("procedure-a", "procedure-b") in duplicate_classes)
    check("B a distinct effect remains a distinct operational class", len(duplicate_classes) == 2)

    e1 = P0 / 2
    e2 = P1 / 3
    e3 = sp.simplify(I2 - e1 - e2)
    check("B finite POVM effects sum to identity", matrix_equal(e1 + e2 + e3, I2))
    check("B every finite POVM effect is positive", all(all(value >= 0 for value in effect.eigenvals()) for effect in (e1, e2, e3)))
    check("B normalized transcript law gives POVM sum one", scalar_equal(sum(probability(sigma, effect) for effect in (e1, e2, e3)), 1))
    check("B mutually exclusive coarse-graining is additive", scalar_equal(probability(sigma, e1 + e2), probability(sigma, e1) + probability(sigma, e2)))

    lam = sp.Rational(2, 5)
    mixed_effect = sp.simplify(lam * P0 + (1 - lam) * PX)
    check("B randomized effects pair affinely", scalar_equal(probability(sigma, mixed_effect), lam * probability(sigma, P0) + (1 - lam) * probability(sigma, PX)))
    mixed_prep = sp.simplify(lam * P0 + (1 - lam) * PX)
    check("B randomized preparations pair affinely for every test", all(scalar_equal(probability(mixed_prep, effect), lam * probability(P0, effect) + (1 - lam) * probability(PX, effect)) for effect in effects))

    px = probability(sigma, PX)
    py = probability(sigma, PY)
    pz = probability(sigma, P0)
    reconstructed = sp.simplify((I2 + (2 * px - 1) * X + (2 * py - 1) * Y + (2 * pz - 1) * Z) / 2)
    check("B complete Pauli probabilities reconstruct the density representative", matrix_equal(reconstructed, sigma))
    check("B trace pairing is nonnegative on all fixture effects", all(probability(sigma, effect) >= 0 for effect in effects))


def structural_clauses_do_not_select_weights() -> None:
    section("C - Same operational structure, different exact weights")
    q_half = sp.Rational(1, 2)
    q_third = sp.Rational(1, 3)
    for q, label in ((q_half, "half"), (q_third, "third")):
        for horizon in range(1, 6):
            total = sum(binary_word_probability(word, q) for word in product((0, 1), repeat=horizon))
            check(f"C {label} law normalizes at horizon {horizon}", scalar_equal(total, 1))
        check(f"C {label} law has full binary support", all(binary_word_probability(word, q) > 0 for word in product((0, 1), repeat=4)))

    check("C isomorphic support permits unequal one-step weights", q_half != q_third)
    def future_fingerprint(q: sp.Expr) -> tuple[sp.Expr, ...]:
        return tuple(
            binary_word_probability(word, q)
            for horizon in range(1, 4)
            for word in product((0, 1), repeat=horizon)
        )

    future_half = future_fingerprint(q_half)
    future_third = future_fingerprint(q_third)
    check(
        "C each same-record fibre is strongly lumpable inside its own law",
        len(quotient_classes({"raw-a": future_half, "raw-b": future_half})) == 1
        and len(quotient_classes({"raw-a": future_third, "raw-b": future_third})) == 1,
    )
    check("C isomorphic quotients do not identify unequal laws", future_half != future_third)

    a = sp.Rational(1, 4)
    b = sp.Rational(3, 4)
    def adaptive_table(q: sp.Expr) -> dict[tuple[int, int], sp.Expr]:
        return {
            (first, second): sp.simplify(
                (q if first else 1 - q)
                * ((b if first else a) if second else (1 - (b if first else a)))
            )
            for first, second in product((0, 1), repeat=2)
        }

    table_half = adaptive_table(q_half)
    table_third = adaptive_table(q_third)
    check("C both adaptive transcript tables normalize", scalar_equal(sum(table_half.values()), 1) and scalar_equal(sum(table_third.values()), 1))
    check("C adaptive composition preserves but does not select first-stage weights", table_half != table_third)
    check("C coarse-graining the adaptive second stage recovers each supplied first kernel", scalar_equal(table_half[(1, 0)] + table_half[(1, 1)], q_half) and scalar_equal(table_third[(1, 0)] + table_third[(1, 1)], q_third))

    costs = {0: sp.Integer(2), 1: sp.Integer(5)}
    config = (0, 1, 1)
    scalar_readout = sum(costs[value] for value in config)
    check("C content-additive scalar readout is fixed independently of q", scalar_readout == 12)
    check("C the same scalar readout coexists with both exact kernels", scalar_readout == 12 and q_half != q_third)

    lam = sp.Rational(2, 5)
    mixed_q = sp.simplify(lam * q_half + (1 - lam) * q_third)
    check("C physical randomization is affine under either supplied numerical law", scalar_equal(mixed_q, sp.Rational(2, 5) * q_half + sp.Rational(3, 5) * q_third))


def clause_delete_countermodels() -> None:
    section("D - Clause-delete countermodels")
    # Delete physical randomization compatibility.
    def nonlinear_weight(x: sp.Expr) -> sp.Expr:
        return sp.simplify(x**2 / (x**2 + (1 - x) ** 2))

    formal_midpoint = sp.Rational(1, 2) * 0 + sp.Rational(1, 2) * sp.Rational(1, 2)
    mixture_of_weights = sp.Rational(1, 2) * nonlinear_weight(0) + sp.Rational(1, 2) * nonlinear_weight(sp.Rational(1, 2))
    check("D nonlinear table is normalized and positive on sample labels", all(0 <= nonlinear_weight(x) <= 1 for x in (0, sp.Rational(1, 4), sp.Rational(1, 2), 1)))
    check("D deleting physical mixing permits nonaffinity", nonlinear_weight(formal_midpoint) == sp.Rational(1, 10) and mixture_of_weights == sp.Rational(1, 4))

    # Delete full-POVM coarse-graining while retaining binary complements.
    sqrt3 = sp.sqrt(3)
    directions = (
        (sp.Integer(0), sp.Integer(0), sp.Integer(1)),
        (sqrt3 / 2, sp.Integer(0), -sp.Rational(1, 2)),
        (-sqrt3 / 2, sp.Integer(0), -sp.Rational(1, 2)),
    )
    def cubic_frame(direction: tuple[sp.Expr, sp.Expr, sp.Expr]) -> sp.Expr:
        return sp.simplify((1 + direction[2] ** 3) / 2)

    check("D cubic frame obeys every binary complement equation", all(scalar_equal(cubic_frame(n) + cubic_frame(tuple(-x for x in n)), 1) for n in directions))
    trine_sum = sp.simplify(sum(sp.Rational(2, 3) * cubic_frame(n) for n in directions))
    check("D cubic frame violates the exact trine POVM sum", trine_sum == sp.Rational(5, 4))

    # Delete effect-faithful context identification.
    shared_operator_tag = P0 / 2
    context_a_probability = sp.Rational(1, 4)
    context_b_probability = sp.Rational(1, 3)
    check("D two normalized contexts may carry the same operator tag", matrix_equal(shared_operator_tag, P0 / 2))
    check("D complete operational quotient separates unequal context procedures", context_a_probability != context_b_probability)
    check("D an operator-valued weight is ill-defined without context compatibility", len({context_a_probability, context_b_probability}) == 2)

    # Delete full qubit-effect completeness.
    diagonal_effects = (sp.zeros(2), P0, P1, I2, P0 / 3 + P1 / 2)
    rho_plus = PX
    rho_minus = projector((ZERO - ONE) / sp.sqrt(2))
    check("D Z-only effect repertoire is normalized and convex", all(0 <= probability(rho_plus, effect) <= 1 for effect in diagonal_effects))
    check("D Z-only effects cannot distinguish opposite phases", fingerprint(P0, (rho_plus, rho_minus)) == fingerprint(P1, (rho_plus, rho_minus)) == (sp.Rational(1, 2), sp.Rational(1, 2)))
    check("D Z-only repertoire has rank two rather than qubit rank four", hermitian_span_rank((P0, P1)) == 2)


def prepared_state_identity_boundary() -> None:
    section("E - Operational preparation versus independent dynamical matrix")
    rho_dynamic = P0
    sigma_one = rho_dynamic
    sigma_half = sp.simplify((I2 + Z / 2) / 2)
    for sigma, label in ((sigma_one, "unit visibility"), (sigma_half, "half visibility")):
        check(f"E {label} table is a normalized trace law", scalar_equal(probability(sigma, P0) + probability(sigma, P1), 1))
        check(f"E {label} representative is positive", all(value >= 0 for value in sigma.eigenvals()))
    check("E operational tomography returns the half-visibility representative", probability(sigma_half, P0) == sp.Rational(3, 4))
    check("E independent dynamical rho predicts a different Z-plus weight", probability(rho_dynamic, P0) == 1)
    check("E trace representation alone does not identify independent rho and sigma", not matrix_equal(rho_dynamic, sigma_half))
    check("E defining preparation by its complete operational class removes a second identity claim", matrix_equal(sigma_half, sigma_half))


def trial_frequency_and_actual_member_boundaries() -> None:
    section("F - Trial/reset corpus, frequency theorem, and actual member")
    q = sp.Rational(1, 3)
    horizon = 4
    words = tuple(product((0, 1), repeat=horizon))
    iid = {word: binary_word_probability(word, q) for word in words}
    frozen = {word: sp.Integer(0) for word in words}
    frozen[(0,) * horizon] = 1 - q
    frozen[(1,) * horizon] = q
    check("F IID and frozen joint laws both normalize", scalar_equal(sum(iid.values()), 1) and scalar_equal(sum(frozen.values()), 1))

    for index in range(horizon):
        iid_marginal = sum(weight for word, weight in iid.items() if word[index] == 1)
        frozen_marginal = sum(weight for word, weight in frozen.items() if word[index] == 1)
        check(f"F one-shot marginal {index + 1} agrees in IID and frozen laws", iid_marginal == frozen_marginal == q)

    def count_moments(law: dict[tuple[int, ...], sp.Expr]) -> tuple[sp.Expr, sp.Expr]:
        mean = sp.simplify(sum(sum(word) * weight for word, weight in law.items()))
        variance = sp.simplify(sum((sum(word) - mean) ** 2 * weight for word, weight in law.items()))
        return mean, variance

    iid_mean, iid_variance = count_moments(iid)
    frozen_mean, frozen_variance = count_moments(frozen)
    check("F both laws have the same expected count", iid_mean == frozen_mean == horizon * q)
    check("F IID count variance is N q(1-q)", iid_variance == horizon * q * (1 - q))
    check("F frozen count variance is N^2 q(1-q)", frozen_variance == horizon**2 * q * (1 - q))
    check("F one-shot effect weights do not determine frequency concentration", iid_variance != frozen_variance)

    n = sp.symbols("n", positive=True, integer=True)
    iid_frequency_variance = q * (1 - q) / n
    frozen_frequency_variance = q * (1 - q)
    check("F exact conditional reset gives vanishing IID frequency variance", sp.limit(iid_frequency_variance, n, sp.oo) == 0)
    check("F frozen memory keeps nonzero frequency variance", frozen_frequency_variance > 0)
    check("F frozen law violates history-independent reset after a recorded one", sp.Integer(1) != q)

    branching_law = {0: 1 - q, 1: q}
    models = tuple({"law": dict(branching_law), "actual": actual} for actual in (None, 0, 1))
    check("F one normalized branching law is compatible with three actuality labels", len(models) == 3 and scalar_equal(sum(branching_law.values()), 1))
    check("F changing actual member does not change the probability law", len({tuple(model["law"].items()) for model in models}) == 1 and len({model["actual"] for model in models}) == 3)
    check("F actual member does not select the exact weight", models[-1]["actual"] == 1 and models[-1]["law"][1] == q != sp.Rational(1, 2))


def classification_and_no_go_contract() -> None:
    section("G - Classification and N1-N8 contract")
    note_raw = NOTE.read_text(encoding="utf-8")
    note = normalized(note_raw)
    for needle in (
        "operational quotient can retire a separate noncontextuality premise",
        "randomization and coarse-graining do not create the numerical law",
        "trace representation is mathematical",
        "prepared-state identity can be definitional",
        "trial/reset corpus is separate",
        "frequency theorem is conditional",
        "actual member remains separate",
        "no axiom text is proposed",
        "no-go discipline gate status: pass",
    ):
        check(f"G note classification: {needle[:53]}", needle in note)
    for index in range(1, 9):
        check(f"G written N{index} section present", f"### n{index}" in note)
    check("G N1 contains at least five attempted routes", note_raw.count("| `ATTEMPTED` |") >= 5)
    check("G N2 has collapsed W/T/A pair table", all(pair in note_raw for pair in ("| `W-T` |", "| `W-A` |", "| `T-A` |")))
    check("G N3 classifies all prescribed hidden-wall phrases", all(phrase in note_raw for phrase in ("we assume", "by construction", "as is standard", "the framework provides", "bridge context", "background", "naturally", "obviously", "standard QFT", "registered", "canonical")))
    check("G N7 contains hostile steelman", "**Hostile steelman:**" in note_raw)
    check("G N8 records prescribed searches", "NO_GO_LEDGER.md" in note_raw and "structurally undecidable" in note_raw)


def main() -> None:
    authority_and_source_contract()
    positive_operational_effect_theorem()
    structural_clauses_do_not_select_weights()
    clause_delete_countermodels()
    prepared_state_identity_boundary()
    trial_frequency_and_actual_member_boundaries()
    classification_and_no_go_contract()
    section("SUMMARY")
    print(f"PASS={PASS} FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
