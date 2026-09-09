#!/usr/bin/env python3
"""Build the citation graph from all docs/*.md notes.

Walks every .md file under docs/ (excluding docs/audit/), extracts:
  - claim_id (stable, derived from path)
  - title (first H1)
  - optional Claim type: hint for auditor-owned claim_type
  - optional legacy Status-line migration hint for claim_type backfill
  - cited authorities (markdown links to other .md files in docs/)
  - primary runner script path
  - helper runner script paths (transitive imports and static dynamic-load
    calls of the primary runner; needed by the audit packet builder so the
    auditor sees the full source chain and doesn't fall back to class C
    on missing-helper grounds)
  - note hash (sha256 of body)

Writes docs/audit/data/citation_graph.json.

This script is deterministic, offline, and read-only against the docs.
"""
from __future__ import annotations

import ast
import hashlib
import json
import re
import urllib.parse
from pathlib import Path

import static_pipeline_checkpoint as static_checkpoint

REPO_ROOT = Path(__file__).resolve().parents[3]
DOCS_DIR = REPO_ROOT / "docs"
AUDIT_DATA_DIR = REPO_ROOT / "docs" / "audit" / "data"
OUTPUT_PATH = AUDIT_DATA_DIR / "citation_graph.json"

# Skip the audit lane itself and generated publication views.
SKIP_PREFIXES = ("audit/",)
GENERATED_PUBLICATION_FILES = {"PUBLICATION_AUDIT_DIVERGENCE.md"}
GENERATED_PUBLICATION_SUFFIXES = ("_EFFECTIVE_STATUS.md",)
# Generated repo status surfaces: pure projections of ledger state. Their
# links are report output, not citations — if they fed the graph they would
# add in-degree/score to exactly the rows they report on (a generated index
# of N retained rows would bump all N criticality inputs), so they must
# contribute no nodes or edges.
GENERATED_REPO_FILES = {"FRONT_DOOR_STATUS.md", "RETAINED_BACKBONE.md"}

DOC_AUTHORITY_REGISTRY_PATH = AUDIT_DATA_DIR / "doc_authority_registry.json"


def _class_f_paths() -> set[str]:
    """Class-F orientation memos, resolved from the doc-authority registry.

    Class F carries no premise or interpretive weight, and criticality is
    graph topology only (FRESH_LOOK_REQUIREMENTS section 4: author framing
    must not set audit cost) — so class-F links must seed no nodes or edges.
    Paths are stored repo-relative in the registry; the graph works
    docs-relative.
    """
    try:
        registry = json.loads(
            DOC_AUTHORITY_REGISTRY_PATH.read_text(encoding="utf-8")
        )
    except (OSError, json.JSONDecodeError):
        return set()
    paths: set[str] = set()
    for row in registry.get("rows", []):
        path = row.get("path")
        # Scope: docs/repo/ class-F memos only. Their ledger-row creation is
        # already gated (excluded_source_patterns), so the skip removes edges
        # without touching any existing ledger row. A registered class-F doc
        # elsewhere under docs/ may already carry a ledger row; removing that
        # row is an audit-data change the graph builder must not make.
        if (
            row.get("class") == "F"
            and isinstance(path, str)
            and path.startswith("docs/repo/")
        ):
            paths.add(path[len("docs/"):])
    return paths


CLASS_F_PATHS = _class_f_paths()

# Legacy Status-line normalization is used only as a temporary migration hint
# for seeding claim_type on rows that predate Type: metadata. It is not emitted
# as an audit authority field.
LEGACY_STATUS_TO_CLAIM_TYPE_PATTERNS = [
    (re.compile(r"\b(?:proposed[_ -]no[_ -]?go|retained[_ -]no[_ -]?go|no-?go)\b", re.IGNORECASE), "no_go"),
    (re.compile(r"\bbounded\b", re.IGNORECASE), "bounded_theorem"),
    (re.compile(r"\b(open|scaffold|planning)\b", re.IGNORECASE), "open_gate"),
    (re.compile(r"\b(?:proposed[_ -]retained|proposed[_ -]promoted|retained|promoted|flagship\s+closed|support|accepted|derived|outside\s+audit-ratified\s+tier|superseded_by)\b", re.IGNORECASE), "positive_theorem"),
]

LEGACY_STATUS_LINE_RE = re.compile(
    r"^\s*(?:\*\*Status:?\*\*|Status:)\s*(.+)$",
    re.IGNORECASE | re.MULTILINE,
)
CLAIM_TYPE_LINE_RE = re.compile(
    r"^\s*(?:\*\*Claim type:?\*\*|Claim type:)\s*(.+)$",
    re.IGNORECASE | re.MULTILINE,
)
TYPE_LINE_RE = re.compile(
    r"^\s*(?:\*\*Type:?\*\*|Type:)\s*(.+)$",
    re.IGNORECASE | re.MULTILINE,
)
CLAIM_TYPES = {
    "positive_theorem",
    "bounded_theorem",
    "no_go",
    "open_gate",
    "decoration",
    "meta",
}
TITLE_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
RUNNER_LABEL_RE = re.compile(
    r"^\s*(?:[-*]\s*)?"
    r"(?:\*\*(?:Primary runner|Primary runners|Primary artifact|Primary artifacts|Primary files|"
    r"Derivation runner|Source runner|Source runners|Script|Scripts|Runner|Runners|"
    r"Files|Harnesses):?\*\*|"
    r"Primary runner:|Primary runners:|Primary artifact:|Primary artifacts:|"
    r"Derivation runner:|Source runner:|Source runners:|Script:|Scripts:|Runner:|Runners:|"
    r"Files:|Harnesses:)\s*",
    re.IGNORECASE,
)
RUNNER_PATH_RE = re.compile(
    r"(scripts/[A-Za-z0-9_./\-]+\.py)|(?<![A-Za-z0-9_./\-])([A-Za-z0-9_.\-]+\.py)"
)
RUNNER_SECTION_RE = re.compile(
    r"^#{2,6}\s+(?:(?:Primary|Key|Audited|New|Source|Validated|Corrected(?:\s+live)?)\s+)?"
    r"(?:Artifact(?:\s+chain)?|Artifacts|Script|Scripts|Runner|Runners|Files|Surfaces|What\s+was\s+tested)\b.*$",
    re.IGNORECASE | re.MULTILINE,
)
# `## Verification` is the dominant house heading for naming a note's runner,
# but it is deliberately NOT merged into RUNNER_SECTION_RE above. Measured over
# the whole docs tree, merging it in place moves five notes off the runner they
# already resolve to: a `## Verification` section that reproduces cited
# comparator runners preempts a LATER stage of the ladder in extract_runner. In
# all five measured cases the displaced stage is the final top-of-file
# single-path fallback, not an `## Artifacts`/`## Runner` section (none of the
# five has one) -- but the same displacement is available against every stage
# below RUNNER_SECTION_RE, which is why the ordering, not the corpus, is what
# the unit tests pin. Tried LAST instead (see extract_runner) it is purely
# additive: no note changes the runner it already had.
RUNNER_VERIFICATION_SECTION_RE = re.compile(
    r"^#{2,6}\s+(?:(?:Primary|Key|Audited|New|Source|Validated|Corrected(?:\s+live)?)\s+)?"
    r"Verification\b.*$",
    re.IGNORECASE | re.MULTILINE,
)
HEADING_RE = re.compile(r"^#{1,6}\s+", re.MULTILINE)
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s#]+\.md)(?:#[^)]*)?\)")

EXPLICIT_PACKET_HELPER_RUNNER_PATHS = {
    # Independently rebuilds the exact A/B effects/programs, simple and
    # integrated absorbing channels, atom duals, total/active rank ledgers,
    # carrier/tag boundaries, and coupling/support hostiles.
    "terminal_center_site_record_diagonal_commit_minimal_carrier_boundary_bounded_theorem_note_2026-08-20": [
        "scripts/terminal_center_site_record_diagonal_commit_minimal_carrier_boundary_independent_check_2026_08_20.py",
    ],
    # Independently rebuilds the A/B programs and radical-valued unitary
    # completions, the presence-separated carrier, terminal cq export/rank,
    # logical QND hostiles, and the finite reversible absorption boundary.
    "fixed_carrier_presence_separated_nondemolition_record_update_boundary_bounded_theorem_note_2026-08-20": [
        "scripts/fixed_carrier_presence_separated_nondemolition_record_update_boundary_independent_check_2026_08_20.py",
    ],
    # Independently rebuilds the exact A/B instruments, staged fresh-label
    # copy, flat/path channel identity, central masses, effect-complete
    # tomography, affine hostile control, and narrow cq-capacity boundary.
    "fresh_ancilla_staged_cq_record_intertwiner_conditional_completion_bounded_theorem_note_2026-08-20": [
        "scripts/fresh_ancilla_staged_cq_record_intertwiner_conditional_completion_independent_check_2026_08_20.py",
    ],
    # Independently rebuilds the typed state/rail projections, delayed
    # frontier census, positive branch tree, three cubic shell orbits,
    # trace/free history laws, and affine definite-sector boundary.
    "instrument_port_typed_record_compiler_conditional_completion_bounded_theorem_note_2026-08-20": [
        "scripts/instrument_port_typed_record_compiler_conditional_completion_independent_check_2026_08_20.py",
    ],
    # Independently rebuilds the common-front endpoint codes, thick decoder,
    # 24-shell orbit bump, matched support/formation twins, seed legality, and
    # finite-cylinder marginalization without importing the primary runner.
    "shared_event_record_support_selection_triangle_bounded_theorem_note_2026-08-20": [
        "scripts/shared_event_record_support_selection_triangle_independent_check_2026_08_20.py",
    ],
    # Independently reconstructs the remote-context Record shells, symbolic
    # full-measure identity, formation countercontrol, staged Kraus recovery,
    # realized branch-state content, and held physical-code embeddings.
    "common_front_stage_remote_context_record_event_congruence_bounded_theorem_note_2026-08-20": [
        "scripts/common_front_stage_remote_context_record_event_congruence_independent_check_2026_08_20.py",
    ],
    # Independently rebuilds the exact shared-effect menus, formula
    # discriminators, contact-seam Kraus pair, context-delay factorization,
    # candidate physical content, and finite conditional-table boundary.
    "shared_effect_record_randomized_preparation_congruence_independence_bounded_theorem_note_2026-08-20": [
        "scripts/shared_effect_record_randomized_preparation_congruence_independent_check_2026_08_20.py",
    ],
    # Independently rebuilds the complete-star matrix stabilizers, symbolic
    # atom-weight residual, token debit, Record quotient, and type boundary.
    "delayed_axis_input_stabilizer_midpoint_type_boundary_bounded_theorem_note_2026-08-20": [
        "scripts/delayed_axis_input_stabilizer_midpoint_boundary_independent_check_2026_08_20.py",
    ],
    # Independently rebuilds the finite frontier census, absorbing recursion,
    # Record quotient, covariance, and named response residuals for this claim.
    "record_native_dyadic_preparation_tag_screening_bounded_theorem_note_2026-08-20": [
        "scripts/record_native_dyadic_preparation_tag_screening_independent_check_2026_08_20.py",
    ],
    # Cycle 756's sibling checker shares only the declared finite-fixture
    # construction, then replaces carrier enumeration and modular elimination
    # with NetworkX maximal cliques and exact SymPy domain-matrix ranks.
    "physical_cell_cutting_blind_space_carrier_span_cycle756_note_2026-08-09": [
        "scripts/physical_cell_cutting_blind_space_carrier_span_cycle756_independent_check_2026_08_09.py",
    ],
    # Cycle 906's sibling checker independently rebuilds the orbit-constant
    # mass dimensions and finite representative sweep without importing the
    # primary runner.
    "orbit_constant_mass_dimension_cycle906_support_note_2026-08-09": [
        "scripts/frontier_cycle906_orbit_constant_mass_dimension_independent_check_2026_08_09.py",
    ],
    # This sibling checker independently recomputes every listed exact-algebra
    # unit and fresh-executes the primary before validating its emitted payload.
    "circulant_spectral_fold_exact_algebra_support_note_2026-08-09": [
        "scripts/salvaged_circulant_spectral_fold_independent_check_2026_08_09.py",
    ],
    # Cycle 924's sibling checker independently verifies the exact ratio,
    # cyclic-patch nullity, group equality, and conditional menu-line claims.
    "occurrence_rate_route_arithmetic_cycle924_bounded_theorem_note_2026-07-28": [
        "scripts/frontier_cycle924_occurrence_rate_independent_check_2026_07_28.py",
    ],
    # Cycle 871's sibling checker independently recomputes the finite-map,
    # stabilizer, obligation-model, and quote-replay claims.
    "source_action_bridge_pricing_cycle871_bounded_theorem_note_2026-07-28": [
        "scripts/frontier_cycle871_bridge_independent_check_2026_07_28.py",
    ],
    # Cycle 915's sibling checker independently recomputes every executed row
    # without importing the primary, so keep it in the restricted packet
    # through a claim-scoped helper edge.
    "comparator_recovered_theta_misattributed_cycle915_bounded_theorem_note_2026-07-28": [
        "scripts/frontier_cycle915_comparator_independent_check_2026_07_28.py",
    ],
    # Cycle 977's sibling checker reconstructs the semantic-quotient family,
    # witness census, cubic classes, and covariance comparisons without
    # importing either the primary or the landed core.
    "witness_family_completeness_cycle977_bounded_theorem_note_2026-08-10": [
        "scripts/frontier_cycle977_witness_family_independent_check_2026_08_10.py",
    ],
    # Cycle 974's sibling checker independently replays the finite event
    # vectors and XOR/product-extension criterion without importing the
    # primary, so keep it in the restricted claim packet explicitly.
    "covariant_law_weight_compatibility_cycle974_theorem_note_2026-08-10": [
        "scripts/frontier_cycle974_compatibility_independent_check_2026_08_10.py",
    ],
    "input_distribution_dependence_law_cycle975_bounded_theorem_note_2026-08-10": [
        "scripts/frontier_cycle975_input_distribution_independent_check_2026_08_10.py",
    ],
    # Cycle 973's sibling checker independently reconstructs the pinned
    # 26-blob catalog and attacks the manual semantic map without importing
    # the primary runner.
    "axiom_edit_repair_map_cycle973_note_2026-08-09": [
        "scripts/frontier_cycle973_map_independent_check_2026_08_09.py",
    ],
    # Cycle 972's checker independently reconstructs the finite Boolean family,
    # cubic rotations, translated coordinate semantics, and marginal census.
    "covariant_dependence_law_cycle972_bounded_theorem_note_2026-08-09": [
        "scripts/frontier_cycle972_law_independent_check_2026_08_09.py",
    ],
    # Cycle 971's semantic checker independently rebuilds the Git-object
    # census and binds the separately reviewed adjudication manifest.
    "axiom_fidelity_reread_cycle971_bounded_theorem_note_2026-08-09": [
        "scripts/frontier_cycle971_fidelity_independent_check_2026_08_09.py",
    ],
    # Cycle 745's independent checker is intentionally a sibling rather than
    # an import of the primary anchored census.
    "physical_cell_cutting_sixteen_census_cycle745_note_2026-08-05": [
        "scripts/physical_cell_cutting_sixteen_census_cycle745_"
        "independent_check_2026_08_05.py",
    ],
    # Cycle 744's opposite-pivot incidence reconstruction and explicit-cell
    # refinement deliberately import no primary symbols. Keep the checker in
    # the restricted packet through this claim-scoped sibling edge.
    "physical_cell_cutting_full_symmetry_certified_cycle744_note_2026-08-05": [
        "scripts/physical_cell_cutting_full_symmetry_certified_cycle744_independent_check_2026_08_05.py",
    ],
    # Cycle 746's opposite-pivot exact-cover and low-column GF(2) checker
    # deliberately imports no primary symbols. Expose the sibling executable
    # in this claim's restricted packet.
    "physical_cell_cutting_carrier_parity_law_cycle746_note_2026-08-08": [
        "scripts/physical_cell_cutting_carrier_parity_law_cycle746_independent_check_2026_08_08.py",
    ],
    # Cycle 747 independently rebuilds the exact-cover population with the
    # opposite pivot and rederives the all-marked census and weight-20 sums.
    "physical_cell_cutting_flip_partner_carrier_bracket_cycle747_note_2026-08-08": [
        "scripts/physical_cell_cutting_flip_partner_carrier_bracket_cycle747_"
        "independent_check_2026_08_08.py",
    ],
    # Cycle 748 independently reconstructs the incidence and every
    # load-bearing group/census/family identity without importing the primary.
    "physical_cell_cutting_census_families_cycle748_note_2026-08-08": [
        "scripts/physical_cell_cutting_census_families_cycle748_"
        "independent_check_2026_08_08.py",
    ],
    # Cycle 749 uses an opposite-pivot row-streaming pair counter to check the
    # primary dense-Gram intrinsic family separator.
    "physical_cell_cutting_family_separator_cycle749_note_2026-08-08": [
        "scripts/physical_cell_cutting_family_separator_cycle749_"
        "independent_check_2026_08_08.py",
    ],
    # Cycle 750 reconstructs the predecessor population with the opposite
    # exact-cover pivot and recognizes cubes by constructive bit labels.
    "physical_cell_cutting_carrier_cube_metric_cycle750_note_2026-08-09": [
        "scripts/physical_cell_cutting_carrier_cube_metric_cycle750_"
        "independent_check_2026_08_09.py",
    ],
    # Cycle 751 replays the streamed-pair predecessor and computes ambient
    # distances by min-plus dynamic programming rather than primary BFS.
    "physical_cell_cutting_object_distance_cycle751_note_2026-08-09": [
        "scripts/physical_cell_cutting_object_distance_cycle751_"
        "independent_check_2026_08_09.py",
    ],
    # Cycle 752 replays the all-row streamed-pair predecessor and enumerates
    # each induced Q4 once by least-vertex coordinate completion.
    "physical_cell_cutting_shape_census_least_sharing_cycle752_note_2026-08-09": [
        "scripts/physical_cell_cutting_shape_census_least_sharing_cycle752_"
        "independent_check_2026_08_09.py",
    ],
    # Cycle 753 replays Cycle 752's least-vertex/streamed-pair checker and
    # rebuilds every new multiplicity profile in cutting-row blocks.
    "physical_cell_cutting_shared_count_variance_law_cycle753_note_2026-08-09": [
        "scripts/physical_cell_cutting_shared_count_variance_law_cycle753_"
        "independent_check_2026_08_09.py",
    ],
    # Cycle 754 replays the Cycle 753 helper and changes the rank, signature,
    # and collision-counting implementations without importing primary symbols.
    "physical_cell_cutting_shadow_rank_unseen_swap_cycle754_note_2026-08-09": [
        "scripts/physical_cell_cutting_shadow_rank_unseen_swap_cycle754_"
        "independent_check_2026_08_09.py",
    ],
    # Cycle 755 replays the Cycle 754 helper and independently reconstructs
    # characters, ordered-pair orbitals, residual ranks, and the signed orbit.
    "physical_cell_cutting_blind_space_symmetry_cycle755_note_2026-08-09": [
        "scripts/physical_cell_cutting_blind_space_symmetry_cycle755_"
        "independent_check_2026_08_09.py",
    ],
    "inter_site_gate_cycle970_bounded_theorem_note_2026-08-09": [
        "scripts/frontier_cycle970_gate_independent_check_2026_08_09.py",
    ],
    # Cycle 708's checker reconstructs the signed-permutation algebra and the
    # four weighted-domain stabilizers without importing the numerical primary
    # or its supplied source-response compiler.
    "physical_source_edit_set_signed_stabilizer_classification_cycle708_note_2026-08-02": [
        "scripts/physical_source_edit_set_signed_stabilizer_classification_cycle708_"
        "independent_check_2026_08_02.py",
    ],
    # Cycle 712's checker independently reconstructs the bounding-box transport,
    # raw Hessian census, family classification, and component arithmetic.
    "physical_mixed_frame_defect_census_family_law_cycle712_note_2026-08-02": [
        "scripts/physical_mixed_frame_defect_census_family_law_cycle712_"
        "independent_check_2026_08_02.py",
    ],
    # Cycle 715's checker independently rebuilds the frame action, subgroup
    # lattice, source stabilizer, Hessian clusters, and finite probe census.
    "physical_frame_group_complement_and_finite_probe_blinding_cycle715_note_2026-08-02": [
        "scripts/physical_frame_group_complement_and_finite_probe_blinding_cycle715_"
        "independent_check_2026_08_02.py",
    ],
    # Cycle 718's checker independently constructs dense frame permutations,
    # eigenspace projectors, regular-coset sources, and the single-slot census.
    "physical_frame_orbit_spectral_measure_and_rayleigh_census_cycle718_note_2026-08-02": [
        "scripts/physical_frame_orbit_spectral_measure_and_rayleigh_census_cycle718_"
        "independent_check_2026_08_02.py",
    ],
    # Cycle 720's checker independently constructs signed permutations, endpoint
    # slot maps, orbit/value equivalence relations, and an exact integer-matrix
    # witness for the conditional restriction lemma.
    "physical_ambient_domain_symmetry_split_cycle720_note_2026-08-02": [
        "scripts/physical_ambient_domain_symmetry_split_cycle720_"
        "independent_check_2026_08_02.py",
    ],
    # Cycle 721's checker independently generates the four-cube paths, uses a
    # pure-tuple signed-permutation group, and transports edge endpoints.
    "physical_stencil_derived_centrality_cycle721_note_2026-08-02": [
        "scripts/physical_stencil_derived_centrality_cycle721_"
        "independent_check_2026_08_02.py",
    ],
    # Cycle 723's checker independently reconstructs the exact corner-piece,
    # path-stencil, facet-cover, and one-unit-cell lower-bound enumerations.
    "physical_adjacency_admissible_assembly_trade_cycle723_note_2026-08-03": [
        "scripts/physical_adjacency_admissible_assembly_trade_cycle723_"
        "independent_check_2026_08_03.py",
    ],
    # Cycle 726's checker independently reconstructs the denominator-two
    # certificate, attaining witness, facet triangulations, spectra, and
    # diagonal-pattern law without importing or executing the primary.
    "physical_facet_charge_tick_mixed_split_cycle726_note_2026-08-04": [
        "scripts/physical_facet_charge_tick_mixed_split_cycle726_"
        "independent_check_2026_08_04.py",
    ],
    # Cycle 727's checker independently rebuilds the exact corner census,
    # sample-point membership matrix, integer certificates, and witnesses.
    "physical_tick_extensive_adjacency_bracket_cycle727_note_2026-08-04": [
        "scripts/physical_tick_extensive_adjacency_bracket_cycle727_"
        "independent_check_2026_08_04.py",
    ],
    # Cycle 728's checker independently rebuilds exact determinants, the two
    # certificate incidence systems, all three carried witnesses, the group
    # action, and a second generic sample chamber without importing the primary.
    "physical_spatial_block_seam_dichotomy_cycle728_note_2026-08-04": [
        "scripts/physical_spatial_block_seam_dichotomy_cycle728_"
        "independent_check_2026_08_04.py",
    ],
    # Cycle 729's checker independently reconstructs the exact block census,
    # symmetry orbits, certificate loads, three witness covers, and the
    # internal-facet/lower-hull distinction without executing the primary.
    "physical_block_cost_interval_lift_obstruction_cycle729_note_2026-08-04": [
        "scripts/physical_block_cost_interval_lift_obstruction_cycle729_"
        "independent_check_2026_08_04.py",
    ],
    # Cycle 730's checker independently rebuilds the piece/sample orbit action,
    # integer endpoint certificates, geometric realization witnesses, orphan
    # certificates, and reverse-order ceiling exhaustions.
    "physical_local_extremality_rule_cell_cycle730_note_2026-08-04": [
        "scripts/physical_local_extremality_rule_cell_cycle730_"
        "independent_check_2026_08_04.py",
    ],
    # Cycle 731's checker reads only carried sparse integer literals through
    # the AST, then independently reconstructs the complete piece/action/
    # incidence system and all forced support and ceiling completions.
    "physical_cost_identity_indicator_certificate_cycle731_note_2026-08-04": [
        "scripts/physical_cost_identity_indicator_certificate_cycle731_"
        "independent_check_2026_08_04.py",
    ],
    # Cycle 732's checker independently rebuilds the finite action, full incidence,
    # parity solve, subgroup ladder, bound rows, dual obstruction, and all witnesses.
    "physical_parity_certificate_cost_spectrum_cycle732_note_2026-08-04": [
        "scripts/physical_parity_certificate_cost_spectrum_cycle732_"
        "independent_check_2026_08_04.py",
    ],
    # Cycle 734's checker independently rebuilds the complete floor-dissection
    # population with the opposite exact-cover pivot, genuine co-occurrence,
    # integer distance graph, and geometric region-refill census.
    "physical_least_cost_cutting_flip_and_move_ladder_cycle734_note_2026-08-04": [
        "scripts/physical_least_cost_cutting_flip_and_move_ladder_cycle734_"
        "independent_check_2026_08_04.py",
    ],
    # Cycle 735's checker independently rebuilds the exact floor population,
    # packed-XOR move graph, regions, whole/embedded cubes, and dense GF(2) charge.
    "physical_least_cost_cutting_piece_charge_cycle735_note_2026-08-05": [
        "scripts/physical_least_cost_cutting_piece_charge_cycle735_"
        "independent_check_2026_08_05.py",
    ],
    # Cycle 736's checker independently rebuilds the complete geometric cutting
    # population, move ladder, GF(2) response space, components, and supplied action.
    "physical_cell_cutting_charge_space_cycle736_note_2026-08-05": [
        "scripts/physical_cell_cutting_charge_space_cycle736_"
        "independent_check_2026_08_05.py",
    ],
    # Cycle 737's checker independently uses a Leibniz determinant, opposite
    # exact-cover pivot, and reversed support-half traversal before rebuilding
    # the complete through-eight support and octet-family censuses.
    "physical_cell_cutting_least_computing_sets_cycle737_note_2026-08-05": [
        "scripts/physical_cell_cutting_least_computing_sets_cycle737_"
        "independent_check_2026_08_05.py",
    ],
    # Cycle 738's checker independently reconstructs the cutting incidence with
    # the opposite cover pivot and uses a separate exact-weight CNF/SAT encoding.
    "physical_cell_cutting_size_ten_frontier_cycle738_note_2026-08-05": [
        "scripts/physical_cell_cutting_size_ten_frontier_cycle738_"
        "independent_check_2026_08_05.py",
    ],
    # Cycle 740's checker independently rebuilds the finite population and
    # complete declared quarter/block union censuses without importing primary.
    "physical_cell_cutting_forced_certificate_cycle740_note_2026-08-05": [
        "scripts/physical_cell_cutting_forced_certificate_cycle740_"
        "independent_check_2026_08_05.py",
    ],
    # Cycle 741's checker reconstructs the cutting incidence with the opposite
    # cover pivot and uses an independent exact syndrome-DP/MITM enumerator.
    "physical_cell_cutting_fourteen_frontier_cycle741_note_2026-08-05": [
        "scripts/physical_cell_cutting_fourteen_frontier_cycle741_"
        "independent_check_2026_08_05.py",
    ],
    # Cycle 743's checker uses an opposite exact-cover pivot and tuple-valued
    # group arithmetic rather than importing the primary refinement/group code.
    "physical_cell_cutting_hidden_three_bit_geometry_cycle743_note_2026-08-05": [
        "scripts/physical_cell_cutting_hidden_three_bit_geometry_cycle743_"
        "independent_check_2026_08_05.py",
    ],
    # Cycle 984's sibling checker independently rebuilds the finite true-Z3
    # star, the five weighting tables, and the transfer criterion without
    # importing or executing the primary runner.
    "born_compatibility_z3_adjacency_cycle984_note_2026-08-11": [
        "scripts/frontier_cycle984_born_compatibility_z3_adjacency_independent_check_2026_08_11.py",
    ],
    "neighbour_dependence_record_content_cycle985_bounded_theorem_note_2026-08-11": [
        "scripts/frontier_cycle985_neighbour_dependence_record_content_independent_check_2026_08_11.py",
    ],
    "b4_clock_relation_run_cycle879_bounded_theorem_note_2026-07-28": [
        "scripts/frontier_cycle879_b4_relation_independent_check_2026_07_28.py",
    ],
    "sharded_content_survival_law_cycle877_bounded_theorem_note_2026-07-28": [
        "scripts/frontier_cycle877_sharding_independent_check_2026_07_28.py",
    ],
    "grading_affine_chart_algebra_cycle876_support_note_2026-08-09": [
        "scripts/frontier_cycle876_grading_affine_chart_algebra_independent_check_2026_08_09.py",
    ],
    "d3_bar_reaudit_reproduced_cycle914_bounded_theorem_note_2026-07-28": [
        "scripts/frontier_cycle914_d3_bar_independent_check_2026_07_28.py",
    ],
    "baxis_second_leg_certificate_cycle875_support_note_2026-07-28": [
        "scripts/frontier_cycle875_baxis_independent_check_2026_07_28.py",
    ],
    "sigma_linear_admissibility_classification_cycle872_bounded_theorem_note_2026-07-28": [
        "scripts/frontier_cycle872_admissibility_independent_check_2026_07_28.py",
    ],
    "copy_redundancy_content_cycle874_bounded_theorem_note_2026-07-28": [
        "scripts/frontier_cycle874_redundancy_independent_check_2026_07_28.py",
    ],
    "local_clock_relation_cycle869_bounded_theorem_note_2026-07-28": [
        "scripts/frontier_cycle869_relation_independent_check_2026_07_28.py",
    ],
    "class_coexistence_born_requirement_cycle979_bounded_theorem_note_2026-08-10": [
        "scripts/frontier_cycle979_class_coexistence_independent_check_2026_08_10.py",
    ],
    "witness_orbit_multiplicity_cycle980_bounded_theorem_note_2026-08-11": [
        "scripts/frontier_cycle980_witness_orbit_multiplicity_independent_check_2026_08_11.py",
    ],
    # Cycle 983's sibling checker independently reconstructs the two-star
    # geometry, semantic quotient, translated truth tables, witness classes,
    # and overlap reconciliation without importing or executing the primary.
    "translation_uniform_two_star_patch_cycle983_bounded_theorem_note_2026-08-11": [
        "scripts/frontier_cycle983_translation_uniform_two_star_patch_independent_check_2026_08_11.py",
    ],
    "general_n_census_law_cycle870_bounded_theorem_note_2026-07-28": [
        "scripts/frontier_cycle870_census_independent_check_2026_07_28.py",
    ],
    # Cycle 739's exact-cardinality SAT adversary deliberately imports and
    # executes neither the meet-in-the-middle primary nor its search engine.
    # Expose the sibling checker in the claim-scoped restricted packet.
    "physical_cell_cutting_twelve_frontier_cycle739_note_2026-08-05": [
        "scripts/physical_cell_cutting_twelve_frontier_cycle739_"
        "independent_check_2026_08_05.py",
    ],
    "physical_cell_cutting_sixteen_attained_cycle742_note_2026-08-05": [
        "scripts/physical_cell_cutting_sixteen_attained_cycle742_"
        "independent_check_2026_08_05.py",
    ],
    # Current paired certificates launch their load-bearing children with
    # subprocess rather than importing them. The Wilson note also names its
    # same-convention systematic sweep on the audited runner surface. Register
    # those claim-scoped source chains explicitly so the restricted packet
    # contains every runner source the notes ask the auditor to inspect.
    "persistent_record_sidebit_note": [
        "scripts/persistent_record_overlap_kernel.py",
        "scripts/persistent_record_matched_compare.py",
        "scripts/density_matrix_analysis.py",
        "scripts/entangling_env_decoherence.py",
        "scripts/generative_causal_dag_interference.py",
        "scripts/graph_memory_scar_decoherence.py",
    ],
    "wilson_test_mass_continuum_note_2026-04-11": [
        "scripts/frontier_test_mass_limit.py",
        "scripts/frontier_perturbative_mass_law.py",
        "scripts/frontier_continuum_limit.py",
        "scripts/frontier_newton_systematic.py",
    ],
    # The source-acceptance note's independent checker deliberately does not
    # import the primary harness. Expose that data-only adversary beside the
    # primary runner; the note's linked landed source notes carry the
    # subprocess-route dependency chain.
    "source_acceptance_harness_support_note_2026-07-28": [
        "scripts/frontier_source_acceptance_harness_independent_check_2026_07_28.py",
    ],
    # This meta support package's exact-rational checker imports neither the
    # primary nor the mutable Cycle-320/322 source modules. Expose the
    # separately executable checker beside the primary; both runners declare
    # the committed fixture and its complete pinned source closure.
    "response_comparison_harness_cycle749_support_note_2026-07-28": [
        "scripts/frontier_cycle749_response_harness_independent_check_2026_07_28.py",
    ],
    # This bounded comparator's independent integer reconstruction deliberately
    # imports neither the primary nor its Fraction-based implementation.
    # Expose that sibling checker to the restricted audit packet explicitly.
    "supplied_three_label_target_apportionment_comparator_bounded_theorem_note_2026-07-30": [
        "scripts/frontier_supplied_three_label_target_apportionment_independent_check_2026_07_30.py",
    ],
    # Cycle 733 deliberately keeps its current-fixture reconstruction
    # independent of the primary conditional-lemma runner. Expose that
    # separately executable adversary to this claim's restricted packet.
    "sector_summed_companion_channel_cycle733_bounded_theorem_note_2026-07-28": [
        "scripts/frontier_cycle733_sector_sum_independent_check_2026_07_28.py",
    ],
    # Cycle 731's checker intentionally obtains the actual primary gate stream
    # through runpy/subprocess boundaries rather than importing the primary.
    # Keep that independent source in the claim packet explicitly.
    "token_count_certificate_cycle731_bounded_theorem_note_2026-07-28": [
        "scripts/frontier_cycle731_count_certificate_independent_check_2026_07_28.py",
    ],
    # Cycle 736 obtains its actual primary template/prefix gate stream through
    # a subprocess export and deliberately imports no frontier module. Expose
    # that separately executable checker in this claim's restricted packet.
    "pairwise_separated_multisource_cycle736_bounded_theorem_note_2026-07-28": [
        "scripts/frontier_cycle736_multisource_independent_check_2026_07_28.py",
    ],
    # Cycle 737's independent checker requires a fresh passing primary, then
    # evaluates the primary's exported literal gates without importing it.
    "ring_family_uniformity_cycle737_bounded_theorem_note_2026-07-28": [
        "scripts/frontier_cycle737_ring_family_independent_check_2026_07_28.py",
    ],
    # Cycle 756's independent state-DP and small-cycle exhaustive checker
    # deliberately does not import the closed-form primary. Expose it beside
    # the primary so the restricted audit packet contains both derivations.
    "cycle_graph_c35_independent_set_census_narrow_theorem_note_2026-07-28": [
        "scripts/frontier_cycle756_c35_independent_set_census_independent_check_2026_07_28.py",
    ],
    # Cycle 761's independent state-DP and small-cycle exhaustive checker
    # deliberately does not import the closed-form primary. Expose it beside
    # the primary so the restricted audit packet contains both derivations.
    "cycle_graph_c43_independent_set_census_narrow_theorem_note_2026-07-28": [
        "scripts/frontier_cycle761_c43_independent_set_census_independent_check_2026_07_28.py",
    ],
    # Cycle 753's checker imports neither the primary nor the proposal-only
    # Cycle 732 executable. It independently reconstructs the fixed target,
    # exact counts, small word spaces, and Prüfer families, then executes the
    # primary only across a subprocess boundary.
    "fixed_target_x_cnot_preparation_count_cycle753_bounded_theorem_note_2026-07-28": [
        "scripts/frontier_cycle753_selection_independent_check_2026_07_28.py",
    ],
    # Cycle 755's exact-DP checker deliberately parses the primary only as
    # inert AST data and never imports or executes it. Expose the separately
    # executable checker beside the primary in the restricted claim packet.
    "program_content_order_attempt_cycle755_bounded_theorem_note_2026-07-28": [
        "scripts/frontier_cycle755_program_order_independent_check_2026_07_28.py",
    ],
    # Cycle 747's finite-state checker reconstructs the complete receiver and
    # admission tables without importing the primary or its repository
    # modules. Expose that independent executable in the restricted packet.
    "cycle332_receiver_success_cycle610_gate_adapter_bounded_theorem_note_2026-07-30": [
        "scripts/frontier_cycle747_receiver_success_gate_adapter_independent_check_2026_07_30.py",
    ],
    # This checker's closed-form controller reconstruction deliberately imports
    # no symbol from the primary and invokes it only through a subprocess.
    # Expose the separate source to the restricted audit packet explicitly.
    "binder_formation_attempt_cycle751_bounded_theorem_note_2026-07-28": [
        "scripts/frontier_cycle751_binder_independent_check_2026_07_28.py",
    ],
    # Cycle 754's checker independently reconstructs the finite receiver,
    # endpoint-support, and status branches without importing the primary.
    # Expose that separate source to the restricted audit packet explicitly.
    "composed_four_flag_acceptance_cycle754_bounded_theorem_note_2026-07-28": [
        "scripts/frontier_cycle754_capstone_independent_check_2026_07_28.py",
    ],
    # Cycle 769's checker executes the primary only as a black box and keeps a
    # separate integer interpreter. Cycle 719 also names seven dynamic source
    # modules that ordinary AST import recovery cannot see. Expose the complete
    # claim-scoped packet without teaching the generic resolver arbitrary
    # dynamic-load semantics.
    "cycle719_origin_zero_compiled_data_trace_cycle769_bounded_theorem_note_2026-07-28": [
        "scripts/frontier_cycle769_cycle719_origin_zero_compiled_data_trace_independent_check_2026_07_28.py",
        "scripts/physical_autonomous_bound_branch_preparation_tournament_cycle611_2026_07_22.py",
        "scripts/physical_autonomous_localized_refocused_matter_transition_tournament_cycle575_2026_07_22.py",
        "scripts/physical_contact_dimer_infinite_internal_content_tournament_cycle583_2026_07_22.py",
        "scripts/physical_intrinsic_contact_bound_moving_transition_tournament_cycle578_2026_07_22.py",
        "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py",
        "scripts/physical_matter_transition_clock_equivalence_tournament_cycle573_2026_07_22.py",
        "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py",
    ],
    # Cycle 820's independent tuple/bit-vector reconstruction deliberately
    # imports neither the primary nor its new core. Keep it separate while
    # still exposing and hash-binding it in the restricted audit packet.
    "full128_two_cell_parity_superselected_even_car_covariance_cycle820_bounded_theorem_note_2026-07-30": [
        "scripts/frontier_cycle820_full128_two_cell_parity_superselected_even_car_independent_2026_07_30.py",
    ],
    "local_parity_exchange_carrier_recurrent_bell_cycle821_bounded_theorem_note_2026-07-30": [
        "scripts/frontier_cycle821_local_parity_exchange_carrier_independent_2026_07_30.py",
    ],
    # This theorem note's N7 steelman is the faithful-but-reducible direct sum
    # of the two complexified simple-sector modules.  The independent helper is
    # not imported by the primary stress runner, so expose it only to this row.
    "cl3_complexification_split_narrow_theorem_note_2026-05-10": [
        "scripts/cl3_pauli_irrep_faithful_direct_sum_n7_independent_2026_07_17.py",
    ],
    # Cycle857's bit-mask checker deliberately stays independent of the
    # primary combinations/gap implementation and therefore does not import
    # it. Expose the sibling checker beside the primary in this claim packet.
    "census_theorem_cycle857_bounded_theorem_note_2026-07-28": [
        "scripts/frontier_cycle857_census_independent_check_2026_07_28.py",
    ],
    # This positive-theorem packet names the irreducible-faithful boundary.
    # Its independently implemented direct-sum steelman is not imported by
    # the primary runner, so register that exact N7 surface claim-scoped.
    "cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10": [
        "scripts/cl3_pauli_irrep_faithful_direct_sum_n7_independent_2026_07_17.py",
    ],
    # The atomic work-history note's primary runner is a packet verifier. Its
    # load-bearing companion sources are certified by that verifier but are not
    # imports, so list them explicitly for the restricted audit packet.
    "work_history.atomic.hydrogen_helium_atomic_companion_note_2026-04-18": [
        "scripts/frontier_atomic_hydrogen_lattice_companion.py",
        "scripts/frontier_atomic_helium_hartree_companion.py",
        "scripts/frontier_atomic_helium_jastrow_companion.py",
        "scripts/frontier_hydrogen_helium_atomic_lattice_kinetic_dependency_narrow_repair_verifier.py",
    ],
    # This wrapper row exists specifically to expose helpers loaded through
    # `_frontier_loader.load_frontier(...)`; AST import discovery cannot see
    # those dynamic loads, but the helpers are one-hop packet sources.
    "one_parameter_reduced_shell_law_helpers_umbrella_note_2026-04-13": [
        "scripts/frontier_star_shell_projector.py",
        "scripts/frontier_same_source_metric_ansatz_scan.py",
        "scripts/frontier_coarse_grained_exterior_law.py",
        "scripts/frontier_sewing_shell_source.py",
        "scripts/frontier_radial_shell_matching_law.py",
    ],
    # The note-sync runner invokes the documented acceptance suite as a child
    # process. Import discovery intentionally does not treat arbitrary
    # subprocess targets as Python imports, so register this load-bearing
    # source explicitly for the restricted audit packet.
    "teleportation_acceptance_suite_note": [
        "scripts/frontier_teleportation_acceptance_suite.py",
    ],
    # This claim's finite-scope wrapper executes the canonical 17-card through
    # subprocess. Keep that exceptional packet edge claim-scoped: arbitrary
    # subprocess targets are intentionally not treated as helper imports.
    "staggered_fermion_card_2026-04-11": [
        "scripts/frontier_staggered_17card.py",
    ],
    # The projector fixture launches both sources through subprocess and keeps
    # the landed helper inside a literal child-driver string. Expose the
    # independent checker and dynamic landed source to restricted review
    # packets without teaching generic discovery to follow arbitrary strings.
    "born_acceptance_harness_support_note_2026-07-28": [
        "scripts/frontier_born_acceptance_independent_check_2026_07_28.py",
        "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
    ],
    # The conditional split/merge runner imports both landed sources, while
    # its clean-room matrix checker remains deliberately separate. Expose that
    # checker beside the primary for the restricted audit packet.
    "companion_bank_static_certificate_povm_conditional_bounded_theorem_note_2026-07-30": [
        "scripts/frontier_companion_bank_static_certificate_povm_independent_check_2026_07_30.py",
    ],
    # The exact-rational comparator theorem's checker deliberately imports
    # neither the primary runner nor the pinned Cycle-317 source. Expose that
    # separate matrix reconstruction beside the primary audit surface.
    "povm_observation_comparator_exact_arithmetic_bounded_theorem_note_2026-07-30": [
        "scripts/frontier_povm_observation_comparator_independent_check_2026_07_30.py",
    ],
    # Cycle 981's checker deliberately parses the primary as inert text/AST
    # and reconstructs the finite identification table independently. Expose
    # that sibling adversary beside the primary in the restricted packet.
    "j_landed_invariant_identification_cycle981_bounded_theorem_note_2026-08-11": [
        "scripts/frontier_cycle981_j_landed_invariant_identification_independent_check_2026_08_11.py",
    ],
}


AXIOM_PREMISE_NODES_PATH = AUDIT_DATA_DIR / "axiom_premise_nodes.json"


def _load_axiom_premise_path_map() -> dict[str, str]:
    """Map repo-relative source path -> canonical un-dated claim_id.

    Lets a re-datable axiom doc (e.g. MINIMAL_AXIOMS_2026-05-20.md) keep a
    stable claim_id (`minimal_axioms`) so inbound citation edges and the
    axiom-premise status survive re-dating. Allowlist only; see
    docs/audit/data/axiom_premise_nodes.json.
    """
    if not AXIOM_PREMISE_NODES_PATH.exists():
        return {}
    try:
        data = json.loads(AXIOM_PREMISE_NODES_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {}
    out: dict[str, str] = {}
    for canonical_id, entry in (data.get("nodes") or {}).items():
        for p in entry.get("aliased_paths", []):
            out[str(p)] = canonical_id
    return out


_AXIOM_PREMISE_PATH_MAP: dict[str, str] | None = None


def _axiom_premise_path_map() -> dict[str, str]:
    global _AXIOM_PREMISE_PATH_MAP
    if _AXIOM_PREMISE_PATH_MAP is None:
        _AXIOM_PREMISE_PATH_MAP = _load_axiom_premise_path_map()
    return _AXIOM_PREMISE_PATH_MAP


def claim_id_from_path(path: Path) -> str:
    """Stable claim_id from doc path: docs/X/Y.md -> X.Y (stem, lowercase).

    Allowlisted axiom-premise source paths are canonicalized to their
    stable un-dated id (see docs/audit/data/axiom_premise_nodes.json).
    """
    rel_repo = path.resolve().relative_to(REPO_ROOT).as_posix()
    canonical = _axiom_premise_path_map().get(rel_repo)
    if canonical is not None:
        return canonical
    rel = path.relative_to(DOCS_DIR)
    parts = list(rel.with_suffix("").parts)
    return ".".join(parts).lower()


def claim_type_from_legacy_status(raw: str | None) -> str | None:
    if not raw:
        return None
    text = raw.strip()
    for pattern, label in LEGACY_STATUS_TO_CLAIM_TYPE_PATTERNS:
        if pattern.search(text):
            return label
    return None


def extract_legacy_status_claim_type(body: str) -> str | None:
    m = LEGACY_STATUS_LINE_RE.search(body)
    if not m:
        return None
    return claim_type_from_legacy_status(m.group(1).strip())


def normalize_claim_type(raw: str | None) -> str | None:
    if not raw:
        return None
    token = raw.strip().split()[0].strip("`*_:.").lower()
    token = token.replace("-", "_")
    if token == "nogo":
        token = "no_go"
    if token in CLAIM_TYPES:
        return token
    phrase = raw.strip().lower().replace("-", " ").replace("_", " ")
    phrase = " ".join(phrase.split())
    aliases = {
        "positive theorem": "positive_theorem",
        "bounded theorem": "bounded_theorem",
        "no go": "no_go",
        "open gate": "open_gate",
    }
    return aliases.get(phrase)


def extract_claim_type_hint(body: str) -> tuple[str | None, str | None]:
    m = CLAIM_TYPE_LINE_RE.search(body) or TYPE_LINE_RE.search(body)
    if not m:
        return None, None
    raw = m.group(1).strip()
    return raw, normalize_claim_type(raw)


def extract_title(body: str) -> str | None:
    m = TITLE_RE.search(body)
    return m.group(1).strip() if m else None


def normalize_runner_path(path: str) -> str | None:
    path = path.strip()
    if not path:
        return None
    candidates: list[str] = []
    raw_path = Path(path)
    if path.startswith("scripts/"):
        candidates.append(path)
    elif not raw_path.is_absolute():
        candidates.extend([path, f"scripts/{path}"])
    basename = raw_path.name
    if basename.endswith(".py"):
        candidates.append(f"scripts/{basename}")

    seen: set[str] = set()
    for candidate in candidates:
        if candidate in seen:
            continue
        seen.add(candidate)
        candidate_path = REPO_ROOT / candidate
        if candidate_path.exists():
            return candidate_path.relative_to(REPO_ROOT).as_posix()
    return None


def runner_paths(text: str) -> list[str]:
    paths: list[str] = []
    for m in RUNNER_PATH_RE.finditer(text):
        raw = m.group(1) or m.group(2)
        if raw:
            path = normalize_runner_path(raw)
            if path:
                paths.append(path)
    return paths


def first_runner_path(text: str) -> str | None:
    paths = runner_paths(text)
    return paths[0] if paths else None


def extract_section(body: str, start: int) -> str:
    m = HEADING_RE.search(body, start)
    end = m.start() if m else len(body)
    return body[start:end]


def _script_stem_from_path_parts(parts: list[str], scripts_dir: Path) -> str | None:
    """Resolve static path fragments to a checked-in scripts/*.py stem."""
    if not parts:
        return None
    flattened: list[str] = []
    for part in parts:
        flattened.extend(p for p in Path(part).parts if p not in {"", "."})
    py_parts = [p for p in flattened if p.endswith(".py")]
    if not py_parts:
        return None
    candidate = Path(py_parts[-1])
    if not (scripts_dir / candidate.name).exists():
        return None
    return candidate.stem


def _path_parts_from_ast(node: ast.AST, names: dict[str, str]) -> list[str]:
    """Best-effort static extractor for script path fragments.

    The resolver only needs enough structure to recognize patterns such as
    ``ROOT / "scripts/foo.py"``, ``Path(__file__).with_name("foo.py")``, and
    constants routed through module-level names.
    """
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return [node.value]
    if isinstance(node, ast.Name) and node.id in names:
        return [names[node.id]]
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
        return _path_parts_from_ast(node.left, names) + _path_parts_from_ast(
            node.right, names
        )
    if isinstance(node, ast.Call):
        func_name = ""
        if isinstance(node.func, ast.Name):
            func_name = node.func.id
        elif isinstance(node.func, ast.Attribute):
            func_name = node.func.attr
        if func_name in {"Path", "with_name", "joinpath"}:
            parts: list[str] = []
            for arg in node.args:
                parts.extend(_path_parts_from_ast(arg, names))
            return parts
    return []


def _script_stem_from_ast(node: ast.AST, names: dict[str, str], scripts_dir: Path) -> str | None:
    return _script_stem_from_path_parts(_path_parts_from_ast(node, names), scripts_dir)


def _dynamic_loader_param_indexes(tree: ast.AST) -> dict[str, set[int]]:
    """Find local wrapper functions whose path parameter feeds a dynamic loader."""
    wrappers: dict[str, set[int]] = {}
    for fn in (n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)):
        params = [arg.arg for arg in fn.args.args]
        indexes: set[int] = set()
        for call in (n for n in ast.walk(fn) if isinstance(n, ast.Call)):
            func_name = ""
            if isinstance(call.func, ast.Name):
                func_name = call.func.id
            elif isinstance(call.func, ast.Attribute):
                func_name = call.func.attr
            if func_name not in {"spec_from_file_location", "SourceFileLoader"}:
                continue
            if len(call.args) < 2 or not isinstance(call.args[1], ast.Name):
                continue
            if call.args[1].id in params:
                indexes.add(params.index(call.args[1].id))
        if indexes:
            wrappers[fn.name] = indexes
    return wrappers


def _parse_script_imports(script_path: Path) -> set[str]:
    """Return basenames of scripts/*.py that this script imports or loads.

    Handles `from scripts.X import ...`, `from scripts import X [as Y]`,
    `import scripts.X`, relative imports inside `scripts/`
    (`from .X import ...`, `from . import X`), and bare PYTHONPATH-style
    imports (`from X import ...`, `import X`) where `scripts/X.py` exists —
    common in this repo because runners are invoked with
    `PYTHONPATH=scripts python3 scripts/X.py`.

    Also handles static dynamic-loader paths such as
    `importlib.util.spec_from_file_location("m", ROOT / "scripts" / "X.py")`
    and local wrapper calls that forward a path parameter into that loader.

    Filters to imports that exist as scripts/<name>.py, so third-party
    libraries (numpy, scipy, etc.) are excluded.

    Used to compute helper_runner_paths so the audit packet builder can
    include the full source chain. Without this, primary runners that
    import from helpers (e.g. lattice_no_barrier_distance.py importing
    from lattice_mirror_distance) cause the auditor to see opaque
    function references → spurious class-C verdicts on packet
    incompleteness grounds alone.
    """
    if not script_path.exists():
        return set()
    try:
        tree = ast.parse(script_path.read_text(encoding="utf-8"))
    except (SyntaxError, UnicodeDecodeError):
        return set()
    scripts_dir = REPO_ROOT / "scripts"
    helpers: set[str] = set()
    script_path_names: dict[str, str] = {}
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        stem = _script_stem_from_ast(node.value, script_path_names, scripts_dir)
        if not stem:
            continue
        for target in node.targets:
            if isinstance(target, ast.Name):
                script_path_names[target.id] = f"{stem}.py"
    loader_param_indexes = _dynamic_loader_param_indexes(tree)
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            module = node.module or ""
            if module.startswith("scripts."):
                helpers.add(module.removeprefix("scripts."))
            elif module == "scripts" and node.level == 0:
                # `from scripts import X [as Y]` -> the imported NAMES are the
                # helper modules (X), not the package `scripts`. Use alias.name
                # (the real module name), never alias.asname (the local alias).
                for alias in node.names:
                    helpers.add(alias.name)
            elif node.level >= 1 and module:
                helpers.add(module)
            elif node.level >= 1 and not module:
                for alias in node.names:
                    helpers.add(alias.name)
            elif module and node.level == 0:
                helpers.add(module.split(".")[0])
        elif isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.startswith("scripts."):
                    helpers.add(alias.name.removeprefix("scripts."))
                else:
                    helpers.add(alias.name.split(".")[0])
        elif isinstance(node, ast.Call):
            func_name = ""
            if isinstance(node.func, ast.Name):
                func_name = node.func.id
            elif isinstance(node.func, ast.Attribute):
                func_name = node.func.attr
            indexes: set[int] = set()
            keyword_names: set[str] = set()
            if func_name in {"spec_from_file_location", "SourceFileLoader", "load_frontier"}:
                indexes.add(1)
                if func_name == "spec_from_file_location":
                    keyword_names.add("location")
                elif func_name == "SourceFileLoader":
                    keyword_names.add("path")
                elif func_name == "load_frontier":
                    keyword_names.add("filename")
            indexes.update(loader_param_indexes.get(func_name, set()))
            for index in indexes:
                if len(node.args) <= index:
                    continue
                stem = _script_stem_from_ast(node.args[index], script_path_names, scripts_dir)
                if stem:
                    helpers.add(stem)
            for keyword in node.keywords:
                if keyword.arg not in keyword_names:
                    continue
                stem = _script_stem_from_ast(keyword.value, script_path_names, scripts_dir)
                if stem:
                    helpers.add(stem)
    return {h for h in helpers if (scripts_dir / f"{h}.py").exists()}


def resolve_helper_runner_paths(primary_runner_path: str | None) -> list[str]:
    """Walk transitive imports from the primary runner; return the full
    set of helper script paths the audit packet must include.

    Returns `scripts/X.py` paths (sorted), excluding the primary itself.
    Empty list if no primary or no helpers. Cycles are handled via a
    seen-set; result is fixed-point of the transitive-closure walk.
    """
    if not primary_runner_path:
        return []
    primary = REPO_ROOT / primary_runner_path
    if not primary.exists():
        return []
    primary_basename = primary.stem
    seen: set[str] = set()
    frontier = _parse_script_imports(primary)
    while frontier:
        new = frontier - seen - {primary_basename}
        if not new:
            break
        seen.update(new)
        next_frontier: set[str] = set()
        for h in new:
            next_frontier.update(
                _parse_script_imports(REPO_ROOT / "scripts" / f"{h}.py")
            )
        frontier = next_frontier - seen - {primary_basename}
    return sorted(f"scripts/{h}.py" for h in seen)


def helper_runner_paths_for_claim(claim_id: str,
                                  primary_runner_path: str | None) -> list[str]:
    """Return packet helper sources for a claim.

    Most helper paths are transitive imports of the primary runner. A small
    number of legacy work-history rows register sibling runner artifacts in
    the source note instead; keep those as explicit packet helpers so the
    restricted audit prompt sees their full source.
    """
    paths: list[str] = []
    for path in resolve_helper_runner_paths(primary_runner_path):
        if path not in paths:
            paths.append(path)
    for path in EXPLICIT_PACKET_HELPER_RUNNER_PATHS.get(claim_id, []):
        if path != primary_runner_path and (REPO_ROOT / path).exists() and path not in paths:
            paths.append(path)
    return paths


def extract_runner(body: str, rel_path: str | None = None) -> str | None:
    if rel_path and rel_path.startswith("ai_methodology/raw/"):
        return None

    lines = body.splitlines()
    for i, line in enumerate(lines):
        if not RUNNER_LABEL_RE.search(line):
            continue
        window = "\n".join(lines[i : i + 4])
        runner = first_runner_path(window)
        if runner:
            return runner

    for m in RUNNER_SECTION_RE.finditer(body):
        runner = first_runner_path(extract_section(body, m.end()))
        if runner:
            return runner

    # Some older cards put the runner name directly in a section heading, e.g.
    # "## 1. Canonical 17-Card (frontier_staggered_17card.py)".
    for line in lines[:120]:
        if line.startswith("#"):
            runner = first_runner_path(line)
            if runner:
                return runner

    if rel_path and not rel_path.startswith(("repo/", "work_history/", "publication/", "lanes/")):
        first_heading = HEADING_RE.search(body)
        preamble = body[: first_heading.start()] if first_heading else "\n".join(lines[:20])
        preamble_paths = list(dict.fromkeys(runner_paths(preamble)))
        if len(preamble_paths) > 1:
            return preamble_paths[0]

    top_paths = list(dict.fromkeys(runner_paths("\n".join(lines[:80]))))
    if len(top_paths) == 1:
        return top_paths[0]

    # Last resort: a `## Verification` section. This runs only after every
    # pattern above has declined, so a note that already resolves through its
    # own runner label or artifact section keeps that runner unchanged.
    #
    # A Verification section is a reproduction recipe, not a runner label: it
    # routinely lists several co-equal runners with no marked primary, and
    # position in that list carries no authority. Taking the first would pin a
    # packet note's audit evidence to whichever runner happens to be listed
    # first -- measured on this corpus, that mispins at least one ledger-backed
    # packet whose own runner is listed third and whose helper closure is
    # empty, so the note's real runner would be absent from the audit packet
    # entirely. Require exactly one distinct runner, matching the uniqueness
    # rule the adjacent top-of-file fallback already applies.
    #
    # Ambiguity is section-local, so an ambiguous section is skipped rather
    # than treated as a veto: a later singleton section (`## Source
    # Verification`, say) still resolves. Only a note whose every Verification
    # section is ambiguous or runnerless leaves `runner_path` unset, which is
    # the same outcome as before this stage existed.
    for m in RUNNER_VERIFICATION_SECTION_RE.finditer(body):
        section_paths = list(dict.fromkeys(runner_paths(extract_section(body, m.end()))))
        if len(section_paths) == 1:
            return section_paths[0]

    return None


def resolve_link_target(link_target: str, source_path: Path) -> Path | None:
    """Resolve a markdown link target relative to source_path. Returns
    the resolved path under DOCS_DIR if it lands inside DOCS_DIR, else None.

    Absolute paths from legacy repo locations (e.g. links written against
    /Users/jonreilly/Projects/Physics/docs/...) are rewritten to the
    current REPO_ROOT/docs/ tree by detecting the '/docs/' segment so
    citations survive repo moves and machine renames. URL-encoded
    characters in the link (%20 etc.) are decoded before resolution.
    """
    decoded = urllib.parse.unquote(link_target)
    if decoded.startswith("/"):
        marker = "/docs/"
        idx = decoded.find(marker)
        if idx < 0:
            return None
        candidate = (DOCS_DIR / decoded[idx + len(marker):]).resolve()
    else:
        candidate = (source_path.parent / decoded).resolve()
    try:
        candidate.relative_to(DOCS_DIR)
    except ValueError:
        return None
    if not candidate.exists():
        return None
    return candidate


def extract_citations(body: str, source_path: Path) -> list[Path]:
    seen: dict[Path, None] = {}
    for raw_target in LINK_RE.findall(body):
        target_path = resolve_link_target(raw_target, source_path)
        if target_path is None or target_path == source_path:
            continue
        seen.setdefault(target_path, None)
    return list(seen.keys())


def is_skipped(rel_path: Path) -> bool:
    rel_str = rel_path.as_posix()
    if any(rel_str.startswith(prefix) for prefix in SKIP_PREFIXES):
        return True
    if rel_path.parts[:2] == ("publication", "ci3_z3"):
        if rel_path.name in GENERATED_PUBLICATION_FILES:
            return True
        if rel_path.name.endswith(GENERATED_PUBLICATION_SUFFIXES):
            return True
    if rel_path.parts[:1] == ("repo",) and rel_path.name in GENERATED_REPO_FILES:
        return True
    if rel_path.as_posix() in CLASS_F_PATHS:
        return True
    return False


def discover_notes() -> list[Path]:
    notes = []
    for path in sorted(DOCS_DIR.rglob("*.md")):
        rel = path.relative_to(DOCS_DIR)
        if is_skipped(rel):
            continue
        notes.append(path)
    return notes


def build_graph() -> dict:
    notes = discover_notes()
    nodes: dict[str, dict] = {}
    edges: list[dict] = []
    path_to_id: dict[Path, str] = {}

    # First pass: register every note as a node.
    for note_path in notes:
        cid = claim_id_from_path(note_path)
        rel = note_path.relative_to(DOCS_DIR)
        body = note_path.read_text(encoding="utf-8", errors="replace")
        raw_type, claim_type_hint = extract_claim_type_hint(body)
        legacy_status_hint = extract_legacy_status_claim_type(body)
        claim_type_seed_hint = claim_type_hint or legacy_status_hint
        primary_runner = extract_runner(body, rel.as_posix())
        nodes[cid] = {
            "claim_id": cid,
            "path": note_path.relative_to(REPO_ROOT).as_posix(),
            "title": extract_title(body),
            "claim_type_author_hint_raw": raw_type,
            "claim_type_author_hint": claim_type_hint,
            "claim_type_seed_hint": claim_type_seed_hint,
            "runner_path": primary_runner,
            "helper_runner_paths": helper_runner_paths_for_claim(cid, primary_runner),
            "note_hash": hashlib.sha256(body.encode("utf-8")).hexdigest(),
            "deps": [],
        }
        path_to_id[note_path] = cid

    # Second pass: resolve citations into deps.
    for note_path in notes:
        cid = path_to_id[note_path]
        body = note_path.read_text(encoding="utf-8", errors="replace")
        for cited_path in extract_citations(body, note_path):
            cited_cid = path_to_id.get(cited_path)
            if cited_cid is None or cited_cid == cid:
                continue
            if cited_cid in nodes[cid]["deps"]:
                continue
            nodes[cid]["deps"].append(cited_cid)
            edges.append({"from": cid, "to": cited_cid})

    # Stats.
    claim_type_hint_counts: dict[str, int] = {}
    claim_type_seed_hint_counts: dict[str, int] = {}
    for n in nodes.values():
        hint = n.get("claim_type_author_hint") or "none"
        claim_type_hint_counts[hint] = claim_type_hint_counts.get(hint, 0) + 1
        seed_hint = n.get("claim_type_seed_hint") or "none"
        claim_type_seed_hint_counts[seed_hint] = claim_type_seed_hint_counts.get(seed_hint, 0) + 1

    runners_with_path = sum(1 for n in nodes.values() if n["runner_path"])
    roots = [cid for cid, n in nodes.items() if not n["deps"]]
    leaves = [cid for cid in nodes if not any(e["to"] == cid for e in edges)]

    return {
        "schema_version": 1,
        "stats": {
            "node_count": len(nodes),
            "edge_count": len(edges),
            "claim_type_author_hint_counts": claim_type_hint_counts,
            "claim_type_seed_hint_counts": claim_type_seed_hint_counts,
            "runners_with_path": runners_with_path,
            "root_count": len(roots),
            "leaf_count": len(leaves),
        },
        "nodes": nodes,
        "edges": edges,
        "roots": sorted(roots),
    }


def main() -> int:
    AUDIT_DATA_DIR.mkdir(parents=True, exist_ok=True)
    graph = build_graph()
    OUTPUT_PATH.write_text(json.dumps(graph, indent=2, sort_keys=True) + "\n")
    receipt_ok, receipt_detail = static_checkpoint.record_producer_receipt(
        "citation_graph"
    )
    if not receipt_ok:
        print(f"checkpoint receipt failed: {receipt_detail}")
        return 1
    s = graph["stats"]
    print(f"Wrote {OUTPUT_PATH.relative_to(REPO_ROOT)}")
    print(f"  nodes: {s['node_count']}  edges: {s['edge_count']}")
    print(f"  roots: {s['root_count']}  leaves: {s['leaf_count']}")
    print(f"  runners attached: {s['runners_with_path']}")
    print(f"  claim_type_seed_hint_counts: {s['claim_type_seed_hint_counts']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
