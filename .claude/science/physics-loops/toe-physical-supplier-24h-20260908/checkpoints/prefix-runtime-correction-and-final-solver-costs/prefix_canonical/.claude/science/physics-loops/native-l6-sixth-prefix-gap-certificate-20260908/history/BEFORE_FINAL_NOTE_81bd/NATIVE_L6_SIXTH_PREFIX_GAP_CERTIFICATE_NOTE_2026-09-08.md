---
claim_id: native_l6_sixth_prefix_gap_certificate_note_2026-09-08
claim_type: bounded_theorem
claim_scope: "Supplied L6 canonical U0 native model:6489 proper masks from7148 keys of six declared sixth-order supports have fixed-parity resolvent gap at least |t|/3=h/6. No coefficients or general flux-gap claim."
upstream_dependencies:
  - native_dynamical_cycle_fermion_z2_dictionary_note_2026-09-08
  - native_zero_penalty_endpoint_note_2026-09-08
  - native_zero_penalty_optimal_flux_dispersion_note_2026-09-08
runner: scripts/native_l6_sixth_prefix_gap_certificate_2026_09_08.py
---

# Exact L6 proper-prefix gaps for six declared spectator supports

**Type:** bounded_theorem  
**Status:** conditional-support

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: "Supplied uniform full native U0 model and canonical L6 flux/parity sector; exact finite certificate."
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

The mathematical inputs are the [whole-carrier dictionary](NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md), [zero-penalty endpoint](NATIVE_ZERO_PENALTY_ENDPOINT_NOTE_2026-09-08.md), and [canonical finite dispersion](NATIVE_ZERO_PENALTY_OPTIMAL_FLUX_DISPERSION_NOTE_2026-09-08.md). The flux-minimization literature theorem in the last parent is not needed to validate the explicit canonical matrix or the rational defect comparison. No coupling, preparation or physical law is selected here.

The complete source runs already give the finite certificate below. The newly assembled portable replay remains pending its separately frozen full execution contract; this draft must not be delivered as having completed that new replay.

# Complete declared-support L6 proper-prefix gap certificate: port design

Status: the source runs are completed and accepted; this new portable arithmetic replay is UNLAUNCHED and pending final canonical source/full-run review. The author of this port also authored the original adjacent and rank4 gap method. The portable algebra adapts the independent reviewer's symmetric Woodbury replay; this provenance is not called an independent new derivation.

## Exact domain and already completed evidence

Use the supplied full native U=0 CAR/Z2 model on the periodic6^3 graph with canonical uniform pi flux, sorted-edge Kij=-2t xiij, and the same physical parity convention as the canonical endpoint. Electric insertions are (1/2)ZeZf for distinct incident edges. Units below are |t|=1, with auxiliary unit h=2|t|. The claim concerns all proper-prefix denominators of the six explicitly enumerated target classes001,003,012,023,122,223 and their fixed native insertion families. It does not assert a bound for every possible flux defect or every sixth-order word.

The adjacent001 family has ten boundary edges occurring once and one bridge occurring twice. Literal incidence matchings give five bridge families0,3,15,18,90,225 internal and9 each external pairing sets,187920 ordered words,2038 proper usage/count keys and1534 distinct proper masks. The original rank2 proposal failed on an external bridge and was corrected to rank3 deltaB/rank6 Gram update; that failed source is historical evidence, not the live formula.

For each nonadjacent class there are twelve boundary edges, each necessarily occurring once in six insertions. Cross-star pairings are impossible because the two odd-distance centers have no common neighbor. Thus15 pairings of each star give225 sets and162000 orders per class. Each proper prefix is an even subset of each six-star:32²-2=1022 keys per class,5110 total. Their union contains4986 masks. These are actual insertion keys, not arbitrary edge subsets. Distinct keys mapping to one mask share a resolvent, but their vector multiplicities are not discarded in a coefficient calculation.

The two completed runs have31 common masks and identical exact rational bounds on every overlap. Thus the union has6489 distinct masks and7148 source keys. There are seven distinct singleton stars in this union. The exact minimum saved by both acceptance chains is

 11391316772010430774722998053916333310961066067 /
 33026152674622787925000000000000000000000000000 > 1/3.

Every source row is strictly positive as a Fraction. Hence these denominators have gap at least |t|/3=h/6, once the source/certificate closure is retained. This does not compute any of the six coefficients. The separate magnetic invariant classification can exclude other bilinear classes, but does not retroactively certify their unenumerated prefixes; it is not required for this gap claim.

## Parity and full active offset

For each support, removing the two centers leaves a connected graph. A gauge cut contained in their stars is therefore, up to complement, empty, one singleton or both centers. Empty and complete target are endpoints, not proper keys. Only the singletons among proper masks are gauge cuts. The adjacent census additionally tracks its repeated bridge exactly and certifies the same proper-cut classification. Singleton gauge implementation reverses active parity, so its initial-parity gap is the canonical minimum active frequency2sqrt3. Its unrestricted ground energy difference is zero and must not be used instead.

For all noncut masks we bound the unrestricted active ground energy, which also lower-bounds the fixed-parity energy. In K=2[[0,B],[-B^T,0]], the native active ground energy is -Tr sqrt(BB^T). This includes all108 singular modes and therefore the unaffected vacuum energy; it is not a truncated defect-space ground energy. The baseline A0=B0B0^T has eigenvalues3,6,9,12 of multiplicities32,48,24,4, giving magnitude72+40sqrt3+48sqrt6.

## One general exact small inverse

For a chosen target white center w, peel deltaB's black-center row and white-center column. Nonadjacent supports leave no entry. An adjacent external bridge can leave one entry at(a,b). Write

 deltaB=F G^T,
 F=[e0,u,f], G=[z,ew,g]

with the third column omitted when absent, f=(remaining entry)e_a and g=e_b. Row0 is removed from u. Literal reconstruction is checked for every mask; no rank assumption replaces that check. Let r be2 or3, U=[F,B0G] and C=[[G^TG,I],[I,0]]. Then

 A-A0=U C U^T,
 C^-1=[[0,I],[I,-G^TG]].

With R=(A0+25I/4)^-1 and S=C^-1+U^T R U,

 Tr(A+25I/4)^-1=Tr R-Tr[S^-1 (RU)^T(RU)].

S is invertible by positive definiteness of A+25I/4 and the determinant identity; column redundancy does not invalidate the formula. The portable code checks the exact small inverse residual each time. R is built once by rational cubic interpolation and checked by the full108-dimensional inverse identity. Its construction uses no floating spectrum or NumPy.

For every x>=0, the second Newton iterate from c>0 bounds sqrt(x) above: n1=(x+c²)/(2c), n2=(n1+x/n1)/2. Polynomial division yields

 n2=(x+c²)/(4c)+c[1-c²/(x+c²)].

Taking c=5/2 and traces, with Tr A=648, gives the exact rational upper trace used in the source runs. Lower integer-square-root bounds for sqrt3 and sqrt6 then produce a lower gap. The same fixed c and root precision are retained; no result-dependent tuning is allowed.

## Portable replay, coverage and failure policy

TARGETS contains all6489 masks, a valid chosen center, exact source bound and singleton label. A final canonical primary must reconstruct all source-key memberships from both censuses, verify the31 overlaps, then replay each unique noncut inverse and each singleton parity bound. It must require equality to the existing exact rational rows AND strict bound>1/3, preserving failures rather than reporting only COMPLETE. The target table is an input to validate, not a source of asserted mathematical answers. Full case outputs and source hashes must be retained.

The new replay_core.py adapts the independent symmetric-inverse implementation to r=2 or3. No physical arithmetic call has been executed in this port. The complete original proofs, cold reviews, source freezes, failed rank2 route,16 old shards and104 new production/replay receipts are required archive inputs for the eventual canonical packet. Only the live mathematical premises and arithmetic/input files belong to AUDIT_INPUT_PATHS; historical outputs must not be silently treated as freshly executed.

## Cost boundary and next gate

The104 completed new jobs cost316.662169493 seconds production and47.490620959 seconds independent replay, with replay maximum1.095427750 seconds for a96-mask shard. The old adjacent accepted whole run cost67.95 seconds including5 prior, but its postreview did not independently recompute1534 inverses. Consequently it is not direct timing authority for a new all-rational rank6 replay.

A rough operation-count estimate scaling the rank4 replay by (6/4)^3 for1534 adjacent masks and by1 for4955 other masks suggests about96 seconds before headroom. This is not a reliable certified forecast: Fraction numerator sizes and Python overhead can change. A fixed25-case small cost gate is therefore proposed before any full replay. It uses five numerically smallest distinct non-singleton masks per original bridge family, requiring an odd external-bridge use for external families so the rank6 branch is exercised. Selection is geometric, fixed before the new port timing, and disclosed as post-existing-data cost design. No scientific parameter changes.

The proposed cost-only gate is30s384MiB with external process-group watchdog, explicit baseline/action/I/O times, all25 output rationals retained. It is NOT authorized or executed here. Only after root acceptance may the full6489-case portable run receive a180s384MiB contract. If conservative forecast exceeds that limit, split the executable under a new explicit contract rather than silently truncating coverage.


## Current portable gate

The fixed25 cost gate completed once: all exact rows agree, with external0.49 seconds,56,754,176-byte process RSS and77,365,248-byte observed whole tree. Rank4/rank6 maxima are0.006870582990814/0.009436874999664724 seconds. The final forecast is83.7139905183285 seconds, including1.5 headroom,10 seconds reserve and a conservative0.50 prior charge. The full6489 replay remains UNLAUNCHED. Earlier proposed-cost language above is preserved derivation history, superseded only by this execution receipt. The portable primary reconstructs actual insertion families and every proper cut, replays all exact gaps, retains an offending row on failure, and requires the strict common floor. No paired full-run output exists yet.
