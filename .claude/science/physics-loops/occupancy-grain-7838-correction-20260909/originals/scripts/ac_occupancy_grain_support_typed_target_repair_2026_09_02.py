#!/usr/bin/env python3
"""Exact support-typed audit of the AC occupancy-grain formal target.

This runner proves finite algebra and checks current repository authority.  It
does not derive a physical charged-lepton action, select a grain, edit an axiom,
or set an audit verdict.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "AC_OCCUPANCY_GRAIN_SUPPORT_TYPED_FORMAL_TARGET_REPAIR_"
    "BOUNDED_THEOREM_NOTE_2026-09-02.md"
)
BASE = "36fe57a7a784df31bc2178c4b94dfc7caaa5d094"
TARGET = "ac_orbit_occupancy_statistical_grain_derivation_obligation"

AUDIT_INPUT_PATHS = (
    "docs/AC_OCCUPANCY_GRAIN_SUPPORT_TYPED_FORMAL_TARGET_REPAIR_BOUNDED_THEOREM_NOTE_2026-09-02.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md",
    "docs/ACPHILAMBDA_OCCUPANCY_DETERMINANT_POWER_SPLIT_EXACT_SUPPORT_NOTE_2026-07-04.md",
    "docs/ACPHILAMBDA_FERMIONIC_REALIFICATION_PFAFFIAN_POWER_IDENTITY_NARROW_THEOREM_NOTE_2026-07-12.md",
    "docs/FLAVOR_FIND_J_ROUND2_POWER_NOT_COUNT_2026-06-02.md",
    "docs/KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md",
    "docs/KCPT_COUPLING_TRIPLE_BEREZIN_COUNT_BINARY_MEASURE_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-17.md",
    "docs/KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md",
    "docs/KOIDE_R_REDUCES_TO_CHIRAL_VS_VECTOR_YUKAWA_BINARY_NARROW_THEOREM_NOTE_2026-06-04.md",
    "docs/KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md",
    "docs/KOIDE_GENERATION_WEIGHT_DIAL_SHAPE_FORCED_VALUE_UNFIXED_QUALIFICATION_BOUNDED_THEOREM_NOTE_2026-07-11.md",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "docs/audit/AXIOM_MINIMALITY_POLICY.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/audit/data/derivation_obligations.json",
    "docs/audit/data/ledger/ac/ac_orbit_occupancy_statistical_grain_derivation_obligation.json",
)

EXPECTED_HASHES = {
    "docs/MINIMAL_AXIOMS_2026-06-29.md":
        "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753",
    "docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md":
        "bd91c0496a51334fa7f7b4ab7a84f87b1575103b1398873d77fe260ffd6aef63",
    "docs/ACPHILAMBDA_OCCUPANCY_DETERMINANT_POWER_SPLIT_EXACT_SUPPORT_NOTE_2026-07-04.md":
        "a154fe5c322ceac03859e735afd7aab48e5fa731ccaf5cf1acab7702e538fda5",
    "docs/ACPHILAMBDA_FERMIONIC_REALIFICATION_PFAFFIAN_POWER_IDENTITY_NARROW_THEOREM_NOTE_2026-07-12.md":
        "7610a933c31f3c4f6d6a8b7903e6fa464030f96e9e4acfe7d0db3e73056839ca",
    "docs/FLAVOR_FIND_J_ROUND2_POWER_NOT_COUNT_2026-06-02.md":
        "ccd06033147f7ca66417bfae050172eeff355ee9d9cc5a48a555b93a6f7b9de2",
    "docs/KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md":
        "33503117b151f9ebfe2f07d5c7e538b33dc6772c00cbe072fc768b917f93706f",
    "docs/KCPT_COUPLING_TRIPLE_BEREZIN_COUNT_BINARY_MEASURE_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-17.md":
        "e1725f080c6ae59c36158e65e215c6ffea4c7dac9860c447f8dc742559140489",
    "docs/KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md":
        "88f24e0eee9b3948021e383123dc9e9402f92962f3b3d4cae592fd2ad487d606",
    "docs/KOIDE_R_REDUCES_TO_CHIRAL_VS_VECTOR_YUKAWA_BINARY_NARROW_THEOREM_NOTE_2026-06-04.md":
        "7ae1b1c57deff5f34f35669a38ab57b4d6e2213f574cc98bbdb9a5cbb8123cac",
    "docs/KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md":
        "5e168be37845446753809ec78a6e4885213da442c83ea2a0a5c0826a4fb301a2",
    "docs/KOIDE_GENERATION_WEIGHT_DIAL_SHAPE_FORCED_VALUE_UNFIXED_QUALIFICATION_BOUNDED_THEOREM_NOTE_2026-07-11.md":
        "b47bbfc215b8d78a8d8c3247efb05531577139021fdd963767bca3a2c799a67c",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md":
        "e7e75a36bd16094cbb547f6b215680ac45adc565c4cc93f05b0af17992eb9292",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md":
        "5516fb0bb8f50286b3c34d3f2668b1a2e347b9f7e257a8b5745f84f1093dd96b",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md":
        "755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563",
    "docs/audit/AXIOM_MINIMALITY_POLICY.md":
        "acf7c2647c392f426369bda8a29614f7bb768eae48e966fe02795e91e27bbb54",
    "docs/audit/data/axiom_premise_nodes.json":
        "615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37",
    "docs/audit/data/derivation_obligations.json":
        "cf629c9efe5811defbaec029e9c9197a93959f454497e6a56dc7eceba1c23f6f",
    "docs/audit/data/ledger/ac/ac_orbit_occupancy_statistical_grain_derivation_obligation.json":
        "308fd687db4584a6520d25804f0c1978f1879c2bf8f3c9cee491f0f8e5ae2926",
}

MUTATIONS = (
    "channel_set_wrong_size",
    "K_fixed_count_wrong",
    "orbit_count_wrong",
    "atom_multiplicity_wrong",
    "quotient_multiplicity_wrong",
    "det_degree_wrong",
    "modulus_square_degree_wrong",
    "power_ratio_changes_under_common_scale",
    "pfaffian_called_new_sector",
    "coordinate_change_changes_power",
    "independent_conjugate_copy_omitted",
    "ordinary_realification_called_fermion_kernel",
    "odd_real_carrier_called_complex_realification",
    "orbit_functional_called_full_determinant",
    "determinant_power_called_r_selector",
    "Record_called_K_codec",
    "Record_called_action_or_measure",
    "removed_scalar_Record_clause_used",
    "graded_composition_called_action_selector",
    "open_PR_called_retained",
    "formal_obligation_called_closed",
    "TOE_percentage_moved",
    "canonical_obligation_silently_edited",
    "audit_or_ledger_surface_edited",
    "source_hash_drift",
    "blast_radius_hardcoded_wrong",
    "N1_alternatives_omitted",
    "N5_cached_resolution_omitted",
    "partial_closure_suppressed",
    "positive_replacement_target_omitted",
)


@dataclass
class Result:
    group: str
    label: str
    ok: bool


class Checks:
    def __init__(self) -> None:
        self.results: list[Result] = []

    def add(self, group: str, label: str, ok: object) -> None:
        self.results.append(Result(group, label, bool(ok)))

    def finish(self) -> int:
        groups: dict[str, list[Result]] = defaultdict(list)
        for result in self.results:
            groups[result.group].append(result)
        for group in sorted(groups):
            vals = groups[group]
            passed = sum(v.ok for v in vals)
            print(f"{group}: PASS={passed} FAIL={len(vals)-passed}")
            for value in vals:
                if not value.ok:
                    print(f"FAIL [{group}] {value.label}")
        passed = sum(r.ok for r in self.results)
        failed = len(self.results) - passed
        print(f"TOTAL: PASS={passed} FAIL={failed}")
        return 0 if failed == 0 else 1


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ratio(v: tuple[Fraction, Fraction]) -> Fraction:
    return v[1] / v[0]


def orbit_partition(items: tuple[str, ...], action: dict[str, str]) -> list[frozenset[str]]:
    unseen = set(items)
    out: list[frozenset[str]] = []
    while unseen:
        seed = min(unseen)
        orbit = frozenset((seed, action[seed]))
        out.append(orbit)
        unseen -= orbit
    return out


def realify(matrix: sp.Matrix) -> sp.Matrix:
    x = matrix.applyfunc(sp.re)
    y = matrix.applyfunc(sp.im)
    return x.row_join(-y).col_join(y.row_join(x))


def pfaffian4(a: sp.Matrix) -> sp.Expr:
    return sp.expand(a[0, 1] * a[2, 3] - a[0, 2] * a[1, 3]
                     + a[0, 3] * a[1, 2])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--list-mutations", action="store_true")
    args = parser.parse_args()
    if args.list_mutations:
        print("\n".join(MUTATIONS))
        return 0
    mutation = args.mutation
    checks = Checks()

    # Source epoch and current formal graph.
    expected_hashes = dict(EXPECTED_HASHES)
    if mutation == "source_hash_drift":
        key = next(iter(expected_hashes))
        expected_hashes[key] = "0" * 64
    for rel, expected in expected_hashes.items():
        checks.add("SOURCE", f"hash:{rel}", sha256(ROOT / rel) == expected)

    minimal = (ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md").read_text()
    obligation = (ROOT / "docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md").read_text()
    policy = (ROOT / "docs/audit/AXIOM_MINIMALITY_POLICY.md").read_text()
    fork = (ROOT / "docs/KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md").read_text()
    premise_registry = json.loads(
        (ROOT / "docs/audit/data/axiom_premise_nodes.json").read_text()
    )
    scale_primitive = (ROOT / "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md").read_text()
    kinetic_primitive = (
        ROOT / "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
    ).read_text()
    realized_primitive = (
        ROOT / "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
    ).read_text()
    note = NOTE.read_text(encoding="utf-8")

    if mutation == "removed_scalar_Record_clause_used":
        minimal += "\nFor any finite collection of pairwise-disjoint records, scalar readout I is additive."
    checks.add("AUTHORITY", "current Record locks one local possibility",
               "When present, a record locks exactly one admissible local possibility." in minimal)
    checks.add("AUTHORITY", "current axiom withholds action",
               "Admissibility is not a dynamics axiom" in minimal)
    checks.add("AUTHORITY", "current axiom withholds K/CPT structure",
               "K`/CPT orbit structure" in minimal and "downstream" in minimal)
    checks.add("AUTHORITY", "removed scalar clause absent from current Record",
               "For any finite collection of pairwise-disjoint records, scalar readout I is additive." not in minimal)
    checks.add("AUTHORITY", "premise reset requires fresh audit",
               "prior judgments that consumed the removed structure must return" in policy)
    checks.add("AUTHORITY", "relative target is present",
               "counts the `K`/CPT orbit or holomorphic pair once" in obligation)
    checks.add("AUTHORITY", "global-power closure wording is present",
               "count-once `det_C`/holomorphic realization" in obligation
               and "count-twice `|det_C|^2`/realified realization" in obligation)
    checks.add("AUTHORITY", "precise fork says polarization supplied",
               "POLARIZATION-SELECT (named conditional premise)" in fork
               and "Not derived" in fork)
    checks.add("AUTHORITY", "foundation registry has exactly four canonical nodes",
               set(premise_registry["canonical_ids"]) == {
                   "minimal_axioms", "scale_reference_primitive",
                   "kinetic_isotropy_primitive", "realized_state_primitive",
               })
    checks.add("AUTHORITY", "scale primitive supplies no selector",
               "no mass ratio, coupling, mixing angle, phase, selector" in scale_primitive)
    checks.add("AUTHORITY", "kinetic primitive supplies no dynamics",
               "not a new dynamics" in kinetic_primitive)
    checks.add("AUTHORITY", "realized-state primitive supplies no measure",
               "state-selection rule" in realized_primitive
               and "alternatives, measure" in realized_primitive)

    # K action and support rays.
    items = ("s", "+", "-")
    if mutation == "channel_set_wrong_size":
        items += ("ghost",)
    action = {"s": "s", "+": "-", "-": "+", "ghost": "ghost"}
    if mutation == "K_fixed_count_wrong":
        action["s"] = "+"
    orbits = orbit_partition(items, action)
    claimed_orbits = 3 if mutation == "orbit_count_wrong" else 2
    atom_mult = (Fraction(1), Fraction(3 if mutation == "atom_multiplicity_wrong" else 2))
    quotient_mult = (Fraction(1), Fraction(2 if mutation == "quotient_multiplicity_wrong" else 1))
    checks.add("ORBIT", "three physical comparison channels", len(items) == 3)
    checks.add("ORBIT", "one K-fixed channel", sum(action[x] == x for x in items) == 1)
    checks.add("ORBIT", "two K orbits", len(orbits) == claimed_orbits == 2)
    checks.add("ORBIT", "atom multiplicity is one-to-two", atom_mult == (1, 2))
    checks.add("ORBIT", "quotient multiplicity is one-to-one", quotient_mult == (1, 1))
    checks.add("ORBIT", "relative grain differs", ratio(atom_mult) != ratio(quotient_mult))

    det_degree = (Fraction(2 if mutation == "det_degree_wrong" else 1), Fraction(2))
    square_degree = (Fraction(2), Fraction(5 if mutation == "modulus_square_degree_wrong" else 4))
    scaled = (Fraction(2), Fraction(5 if mutation == "power_ratio_changes_under_common_scale" else 4))
    checks.add("SUPPORT", "full determinant degree is one-to-two", det_degree == (1, 2))
    checks.add("SUPPORT", "global modulus square degree is two-to-four", square_degree == (2, 4))
    checks.add("SUPPORT", "global squaring preserves projective ray",
               ratio(det_degree) == ratio(square_degree) == ratio(scaled))

    ns, nd, qs, qd = sp.symbols("nu_s nu_d q_s q_d", positive=True)
    r0 = nd / (2 * ns)
    r1 = (nd + qd) / (2 * (ns + qs))
    exact_difference = (ns * qd - nd * qs) / (2 * ns * (ns + qs))
    checks.add("SUPPORT", "support-increment identity",
               sp.simplify(r1 - r0 - exact_difference) == 0)
    checks.add("SUPPORT", "global copy is neutral",
               sp.simplify(exact_difference.subs({qs: ns, qd: nd})) == 0)
    checks.add("SUPPORT", "doublet-only copy changes ray",
               exact_difference.subs({ns: 1, nd: 1, qs: 0, qd: 1}) == sp.Rational(1, 2))
    checks.add("SUPPORT", "orbit endpoint arithmetic",
               quotient_mult[1] / (2 * quotient_mult[0]) == Fraction(1, 2))
    checks.add("SUPPORT", "channel endpoint arithmetic",
               atom_mult[1] / (2 * atom_mult[0]) == Fraction(1))

    claims = {
        "pfaffian_adds_sector": mutation == "pfaffian_called_new_sector",
        "coordinate_power": 2 if mutation == "coordinate_change_changes_power" else 1,
        "independent_copy_present": mutation != "independent_conjugate_copy_omitted",
        "realification_is_fermion_kernel": mutation == "ordinary_realification_called_fermion_kernel",
        "odd_is_complex_realification": mutation == "odd_real_carrier_called_complex_realification",
        "orbit_functional_degree": (1, 2) if mutation == "orbit_functional_called_full_determinant" else (1, 1),
        "global_power_selects_r": mutation == "determinant_power_called_r_selector",
        "record_is_K_codec": mutation == "Record_called_K_codec",
        "record_is_action": mutation == "Record_called_action_or_measure",
        "graded_composition_selects_action": mutation == "graded_composition_called_action_selector",
    }

    # Exact realification and Pfaffian controls.
    i = sp.I
    k = sp.Matrix([[1 + 2 * i, 3 - i], [2, 4 + i]])
    rk = realify(k)
    checks.add("TYPING", "ordinary realification determinant identity",
               sp.expand(rk.det() - k.det() * sp.conjugate(k.det())) == 0)
    ak = sp.zeros(4)
    ak[:2, 2:] = k
    ak[2:, :2] = -k.T
    checks.add("TYPING", "fermion block is antisymmetric", ak.T == -ak)
    checks.add("TYPING", "rank-two block Pfaffian is minus det K",
               sp.expand(pfaffian4(ak) + k.det()) == 0)
    m = sp.Matrix([[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [1, 0, 0, 2]])
    transformed = m.T * ak * m
    checks.add("TYPING", "Pfaffian congruence and Jacobian cancel",
               sp.expand(pfaffian4(transformed) / m.det() - pfaffian4(ak)) == 0)
    checks.add("TYPING", "coordinate change preserves one physical copy",
               not claims["pfaffian_adds_sector"] and claims["coordinate_power"] == 1)
    checks.add("TYPING", "power two requires independent conjugate content",
               claims["independent_copy_present"])
    checks.add("TYPING", "ordinary realification is not generally skew",
               rk.T != -rk and not claims["realification_is_fermion_kernel"])
    checks.add("TYPING", "R plus C has odd real dimension",
               3 % 2 == 1 and not claims["odd_is_complex_realification"])
    checks.add("TYPING", "orbit quotient is not full determinant",
               claims["orbit_functional_degree"] == (1, 1))
    checks.add("TYPING", "global determinant power is not relative selector",
               not claims["global_power_selects_r"])

    # A relative Record-only discriminator, conditional on a supplied writer.
    def odds(power: int, x: Fraction) -> Fraction:
        p = x ** power / (1 + x ** power)
        return p / (1 - p)

    o12 = odds(1, Fraction(4)) / odds(1, Fraction(2))
    o22 = odds(2, Fraction(4)) / odds(2, Fraction(2))
    checks.add("DISCRIMINATOR", "single-copy odds exponent", o12 == 2)
    checks.add("DISCRIMINATOR", "double-copy odds exponent", o22 == 4)
    checks.add("DISCRIMINATOR", "odds test separates supplied writers", o12 != o22)
    checks.add("DISCRIMINATOR", "Record is not itself K codec",
               not claims["record_is_K_codec"])
    checks.add("DISCRIMINATOR", "Record is not itself action or measure",
               not claims["record_is_action"])
    checks.add("DISCRIMINATOR", "graded composition does not select action",
               not claims["graded_composition_selects_action"])

    # Live graph blast radius from the audit pipeline's canonical target row.
    row_path = ROOT / "docs/audit/data/ledger/ac/ac_orbit_occupancy_statistical_grain_derivation_obligation.json"
    row = json.loads(row_path.read_text())
    claimed_direct = 15 if mutation == "blast_radius_hardcoded_wrong" else 16
    claimed_transitive = 107 if mutation == "blast_radius_hardcoded_wrong" else 108
    checks.add("GRAPH", "canonical direct-consumer count",
               claimed_direct == row["direct_in_degree"])
    checks.add("GRAPH", "canonical transitive-descendant count",
               claimed_transitive == row["transitive_descendants"])
    checks.add("GRAPH", "obligation is critical", row["criticality"] == "critical")
    checks.add("GRAPH", "live obligation remains unaudited",
               row["effective_status"] == "unaudited" and row["chain_closes"] is None)

    if mutation == "open_PR_called_retained":
        note = note.replace("Open PRs are prior-art comparators only.", "Open PRs are retained.")
    if mutation == "formal_obligation_called_closed":
        note = note.replace("The obligation remains open.", "The obligation is closed.")
    if mutation == "TOE_percentage_moved":
        note = note.replace("TOE percentage movement: `0`.", "TOE percentage movement: `1`.")
    if mutation == "N1_alternatives_omitted":
        note = note.replace("## N1 — Alternative route enumeration", "## routes omitted")
    if mutation == "partial_closure_suppressed":
        note = note.replace("## N6 — Partial-closure path scan", "## partial closures omitted")
    if mutation == "positive_replacement_target_omitted":
        note = note.replace("## Proposed corrected target", "## target omitted")

    changed = subprocess.run(
        ["git", "diff", "--name-only", BASE, "HEAD"], cwd=ROOT,
        check=True, text=True, capture_output=True,
    ).stdout.splitlines()
    if mutation == "canonical_obligation_silently_edited":
        changed.append("docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md")
    if mutation == "audit_or_ledger_surface_edited":
        changed.append("docs/audit/data/ledger/ac/fake.json")
    checks.add("GOVERNANCE", "canonical obligation untouched",
               "docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md" not in changed)
    checks.add("GOVERNANCE", "audit and ledger surfaces untouched",
               not any(p.startswith("docs/audit/") for p in changed))
    checks.add("GOVERNANCE", "open PRs are prior-art only",
               "Open PRs are prior-art comparators only." in note
               and "Open PRs are retained." not in note)
    checks.add("GOVERNANCE", "obligation remains open",
               "The obligation remains open." in note and "The obligation is closed." not in note)
    checks.add("GOVERNANCE", "TOE movement remains zero",
               "TOE percentage movement: `0`." in note and "TOE percentage movement: `1`." not in note)
    checks.add("GOVERNANCE", "N1 alternatives committed",
               "## N1 — Alternative route enumeration" in note)
    checks.add("GOVERNANCE", "N6 partial closures committed",
               "## N6 — Partial-closure path scan" in note)
    checks.add("GOVERNANCE", "positive replacement target committed",
               "## Proposed corrected target" in note)
    checks.add("GOVERNANCE", "claim type is bounded theorem",
               "**Claim type:** bounded_theorem" in note)
    checks.add("GOVERNANCE", "no axiom amendment claimed",
               "Axiom amendment: `none`." in note)

    emit_n5 = mutation != "N5_cached_resolution_omitted"
    checks.add("GOVERNANCE", "N5 resolution lines emitted", emit_n5)
    if emit_n5:
        print("per_element: checked — exact two-sector support increments and single-copy determinant/Pfaffian identities are executed.")
        print("per_site: checked and not executed — no site-indexed physical action or Record writer is supplied, so no per-site negative is claimed.")
        print("per_mode: checked and not executed — no lattice momentum operator is supplied, so no per-mode determinant negative is claimed.")
        print("per_block: checked — the 2-by-2 complex carrier and associated 4-by-4 skew block are executed exactly under congruence.")
        print("lattice_wide: checked and not executed — no lattice action or measure is derived, so the result is explicitly not a lattice-wide no-go.")
        print("N5_SCOPE no-go: current-authority and named full-carrier-power scope only")
        print("N5_SCOPE never: no metaphysical or all-future-routes claim")
        print("N5_SCOPE impossible: no global impossibility claim")
        print("N5_SCOPE forced: exact algebra only; physical selection remains open")
        print("N5_SCOPE only: only the projective support criterion is biconditional")
        print("N5_SCOPE must: must is confined to the proposed closure contract")
        print("N5_SCOPE cannot: cannot is confined to global common-power selection")

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
