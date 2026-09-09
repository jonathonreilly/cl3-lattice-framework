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

This certificate combines the exact adjacent and nonadjacent proper-prefix computations with a portable rational replay. The port author also authored the original adjacent and rank-four gap method. The portable algebra adapts the independent reviewer's symmetric Woodbury replay; that adaptation is not presented as an independent new derivation. Original proofs, failed approaches, source runs, independent reviews and execution receipts are retained in the companion physics-loop packet.

## Exact domain and certificate

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

## Portable replay, coverage and provenance

The paired primary reconstructs the actual insertion families from both censuses, verifies all 7,148 source-key memberships and the 31 common masks, and checks the classification of every proper gauge cut. Its numerically ordered target table contains all 6,489 masks, a valid chosen center, the exact source bound and the singleton label. For every unique noncut mask the arithmetic helper recomputes the rational inverse trace and gap; for each singleton it checks the fixed-parity bound. It requires equality to the exact source rows and the strict common floor greater than 1/3. The target table supplies comparison data rather than replacing the mathematical calculation.

The arithmetic helper implements the symmetric inverse formula above for both rank-two and rank-three updates. It constructs and verifies the baseline inverse once, checks each small inverse residual, and uses exact integer square-root enclosures. The geometry helper separately reconstructs literal edge incidences and prefix membership. An offending computed row is retained before equality or floor checks; an exception during computation identifies its current case. Complete row outputs, source hashes and execution receipts belong to the companion packet, whose execution records describe each invocation without changing this theorem's premises.

The packet preserves the original proofs, independent cold reviews, source freezes, the failed rank-two proposal, the adjacent source shards, and the nonadjacent production and independent replay receipts. Historical calculations remain attributed to their original sources. The declared live closure contains the mathematical premises, three portable scripts and five exact input ledgers; it does not relabel archived output as freshly computed evidence. Resource forecasts, watchdog contracts, timing records and isolated-copy receipts are execution metadata in that packet, rather than additional mathematical assumptions.
