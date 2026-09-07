---
claim_id: native_edge_record_z4_flux_one_shot_error_bound_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
runner: scripts/native_gauge_flux_one_shot_gaussian_readout_error_bound_check_2026_09_07.py
upstream_dependencies:
  - native_edge_record_z4_flux_bridge_capacity_bounded_theorem_note_2026-09-07
  - native_edge_record_matter_instrument_and_energy_ledger_bounded_theorem_note_2026-09-05
claim_scope: "On the supplied nine-mode native encoding, a single Gaussian-preprocessed bridge sign has fixed-positive three-pair mean error at least1/3; arbitrary input-independent orientation mixtures have four-test worst error at least1/4. No multiple-event or general apparatus obstruction."
---

# Quantitative error bound for one native Gaussian-preprocessed flux Record

On the supplied nine-mode orthogonal native encoding, a single bridge-sign readout preceded by arbitrary number-conserving Gaussian preprocessing has mean high-bit error at least1/3 on three specified pair inputs when its orientation is fixed positively. Any input-independent mixture that also randomizes orientation has worst error at least1/4 on the vacuum and those three pairs. These are bounds on the specified one-shot readout contract, not a multiple-event or general apparatus obstruction.

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

Independent audit owns status authority.

## Provenance, inputs and theorem

Root derived the analytic inequality before the finite-check contract. An independent cold review is preserved as REVIEW.md SHA7ca5861712f7b4193167815cddb7bd25444516981cdf508cc951d5c7d2207eab. FINITE_CHECK_CONTRACT.md prospectively freezes the subsequent finite tests; it does not retrospectively preregister the derivation.

The actual nine-mode even-CAR encoding, labels, low-bit bridge and one-shot high-bit target are imported from [the native flux bridge-capacity theorem](NATIVE_EDGE_RECORD_Z4_FLUX_BRIDGE_CAPACITY_BOUNDED_THEOREM_NOTE_2026-09-07.md). The native bridge effects and supplied energy-lift law are imported from [the native matter instrument theorem](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md). Code preparation, port assignments, Gaussian preprocessing and Born occurrence remain explicit inputs. The existing parent source is unchanged.

Modes0..3 hold the four low label bits, modes4..7 the high bits, and mode8 is their parity reference. The vacuum and pairs01,02,12 are legal even-code inputs. Their fluxes a+b-c-d modulo4 are respectively0,2,0,0, so their high-bit signs are (+,-,+,+).

A native bridge parity, conjugated by any supplied number-conserving Gaussian unitary, has measured observable eta Gamma(R), with R=V*DV a Hermitian unitary and D=I-2P_component. The fixed sign eta includes known old-Record parity and outcome naming. Gaussian preprocessing fixes the vacuum; no number-changing operation or additional output observable is admitted.

For eta=+1, the three-pair error sum is at least1. For arbitrary input-independent probability mixtures over (eta,R), the four-test error sum is at least1. Hence the claimed mean and worst-case bounds follow. No global256input minimax value is asserted.

## Exact principal-block inequality

Set A=R[{0,1,2},{0,1,2}], a Hermitian contraction. In pair order(01,02,12), the corresponding compression of Lambda²R is exactly B=Lambda²A, because its matrix entries are the corresponding minors. Thus pair expectation is det A[{i,j},{i,j}], even when the pair state is not an eigenstate.

Let T=diag(-1,1,1). The summed correct-sign score is

    S=Tr(TB)=Tr B-2<01|B|01> <= Tr B-2 lambda_min(B).

The eigenvalues of B are the three pair products of the eigenvalues of A. If those eigenvalues have the same sign, write their absolute values0<=a<=b<=c<=1. Then

    Tr B-2 lambda_min(B)=ac+bc-ab <= a+b-ab <=1.

Otherwise, global sign reversal of A does not affect B, so write the eigenvalues -a,b,c with0<=a<=1 and0<=b<=c<=1. Then

    Tr B-2 lambda_min(B)=a(c-b)+bc <= c-b+bc <=1.

Zero eigenvalues are included by continuity. Therefore S<=1 for every Hermitian contraction A, a class larger than those produced by the native reflection.

The binary wrong probability on target t is(1-t<Gamma(R)>)/2. Summing over the three pair inputs gives(3-S)/2>=1. This argument uses no exact-determinism assumption and does not replace a general Gaussian unitary by a diagonal one.

## Orientation and mixture scope

For eta=-1, the vacuum is wrong with probability one. For eta=+1, the vacuum is correct and the pair-error sum is at least one. Thus every oriented rule has four-test error sum at least one. Averaging preserves this inequality when the mixing measure is the same for every input, even when R and eta are correlated with each other. At least one of four errors is consequently at least1/4. Fixed eta=+1 mixtures retain the stronger pair-mean bound1/3.

Input-dependent choice of a rule is not a common mixture and need not obey this inference. The helper explicitly demonstrates that an oracle choosing a different correct rule for each of four known inputs can make those four errors zero. That adverse control uses the input label as a supplied selection instruction; it is not an implementation on an unknown input. Selective conditioning is not silently admitted.

## Retained battery qualification

For the standard full-line lift with an initially independent ready battery, the bridge sign probabilities are a positive Fourier-density mixture of incoming quadratic conjugations of the native parity effect. Scalar fuel terms cancel in the squared effect. The measure is common to all tested input states, so the fixed-positive1/3 bound survives. A cap-safe realization that exactly reproduces this lift on all tested inputs inherits the same result.

The argument does not cover input-correlated apparatus, an extra apparatus readout, reading battery energy as the answer, cap-refusal-based decisions, additional non-Gaussian control, prior low-bit conditioning or multiple adaptive Record events. In particular no extension of the parent's already separate finite-event constructions is obstructed by this theorem.

## Exact finite support and limits

The claim-local helper [native_gauge_flux_one_shot_gaussian_readout_error_bound_check_2026_09_07.py](../scripts/native_gauge_flux_one_shot_gaussian_readout_error_bound_check_2026_09_07.py) has41actual checks: one rational orthogonal geometry check,24contraction checks over six fixed spectra, five literal9-mode/reflection/exterior-power checks, ten mixture checks and one input-dependent adverse control. It retains the actual non-diagonal matrices, all pair errors and mixture table. A rational Pythagorean dilation gives an actual9-mode Hermitian unitary with four negative eigenvalues; all36 exterior-square columns are checked, not only the three diagonal expectations.

Four diagonal native-compatible reflections realize error tables with exactly one wrong input each on this four-element test set. Their uniform mixture has four errors1/4. This is only a finite-subset saturation control and does not prove the same worst error on all256 encoded inputs. No floating optimization or fitted constant enters. The only failed run was JSON serialization of tuple-held fractions after the mathematical assertions passed; its source and failure account are preserved, and the correction changes no scientific fixture.

N5: The theorem concerns one Gaussian-preprocessed native bridge sign on the declared all-input encoding.
N5: Fixed positive orientation and randomized orientation have different stated bounds.
N5: Product-ready battery mixtures qualify only under the standard full-line or exactly matching cap-safe instrument.
N5: Finite four-test saturation is not a global minimax theorem.
N5: No multiple-event, adaptive, general apparatus, physical coupling or framework-closure claim is made.

## Durable review and failure history

The [protocol packet](../.claude/science/physics-loops/native-flux-error-20260907/PROOF_REVIEW.md) preserves derivation-before-contract timing, original source/helper bytes, independent reviews and the serialization-only failure. It separates the analytical inequality from41 finite support assertions and records the canonical-only reporting repairs.
