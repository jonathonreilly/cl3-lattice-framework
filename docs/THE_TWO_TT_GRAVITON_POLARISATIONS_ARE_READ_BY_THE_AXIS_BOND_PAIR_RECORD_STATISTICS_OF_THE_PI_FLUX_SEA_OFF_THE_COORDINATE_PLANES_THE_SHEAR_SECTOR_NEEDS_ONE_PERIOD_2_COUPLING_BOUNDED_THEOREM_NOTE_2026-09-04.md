---
claim_id: the_two_tt_graviton_polarisations_are_read_by_the_axis_bond_pair_record_statistics_of_the_pi_flux_sea_off_the_coordinate_planes_the_shear_sector_needs_one_period_2_coupling_bounded_theorem_note_2026-09-04
claim_type: bounded_theorem
claim_scope: "T1-T7: supplied finite Slater/Born response and cubic representations on declared tori. The diagonal TT projection criterion is kinematic; endpoint means can lower response rank. Uniform-pattern T2 uniqueness does not exclude momentum-dependent NN alternatives. No physical TT, clock, Record or limiting theorem."
runner: scripts/tt_graviton_polarisations_read_by_axis_bond_pair_record_statistics_check_2026_09_04.py
---

# Finite axis-bond response, endpoint rank losses, and supplied shear alternatives

**Date:** 2026-09-09 correction of the dated original.
**Type:** bounded_theorem
**Status:** bounded - conditional finite source; formal audit is deferred.
**Primary runner:** [scripts/tt_graviton_polarisations_read_by_axis_bond_pair_record_statistics_check_2026_09_04.py](../scripts/tt_graviton_polarisations_read_by_axis_bond_pair_record_statistics_check_2026_09_04.py)
**Runner cache:** [logs/runner-cache/tt_graviton_polarisations_read_by_axis_bond_pair_record_statistics_check_2026_09_04.txt](../logs/runner-cache/tt_graviton_polarisations_read_by_axis_bond_pair_record_statistics_check_2026_09_04.txt)

## Current premises and provenance

The [current minimal axiom memo](MINIMAL_AXIOMS_2026-06-29.md) governs framework interpretation. It does not derive the supplied coarse fermion/Fock model, Slater state, joint Born occupation measurement, physical embedding, permanent fine-site Record formation, clock, metric or coupling used here. Occupation data below are conditional model statistics. Neither physical gravity nor an exhaustive absence theorem is established.

All three original bodies for this PR, including its historical numerical output, are preserved byte-for-byte outside active note discovery under `.claude/science/physics-loops/shear-correction-20260909/originals/7951/`. Original filenames are retained as provenance, not current theorem titles. Historical scratchpad references are attribution; their missing campaigns and quoted counts are not accepted through those references. The current executable supplies the finite calculations described below and retains every original check ID.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
artifact_role: theorem
next_trace_action: "Independent affected-source confirmation; physical suppliers remain open, formal audit deferred."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

The [corrected determinantal interface](RECORD_STATISTICS_OF_THE_HALF_FILLED_SEA_ARE_DETERMINANTAL_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-09-03.md) supplies the conditional Slater/Born formulas. The [current density ruler](THE_RECORD_DENSITY_RULER_IS_ONE_PRODUCT_KAPPA_NU_EQUALS_ONE_AND_THE_HALF_FILLED_SEA_SUPPLIES_ZERO_BOUNDED_THEOREM_NOTE_2026-09-03.md) and [current rate ruler](A_FORMATION_RATE_RULER_EVADES_THE_SEAS_SUBLATTICE_CANCELLATION_AND_THE_BRIDGES_CONSTANT_MODE_FIXES_KAPPA_R_EQUALS_ONE_BOUNDED_THEOREM_NOTE_2026-09-04.md) do not force a physical exponent or pointwise bond cancellation. The [corrected Regge interface](THE_REGGE_SECOND_VARIATION_ON_THE_4D_CUBIC_COXETER_COMPLEX_CARRIES_A_NATIVE_LINEARISED_GRAVITON_BOUNDED_THEOREM_NOTE_2026-09-03.md) treats finite action/readout diagnostics without establishing a physical propagating TT sector. These interfaces are context and supplied mathematical premises, not imported parent campaigns.

## Setting and observable meanings

Use even coarse tori `L=6,8,12`, KS signs `eta=(1,(-1)^x,(-1)^(x+y))`, the declared minimum half-filled energy twist with maximum-gap fallback, and the gapped projector `P` onto the lowest `L^3/2` levels of `H=M+m Eps`, `m=0,1`. The zero-flux control has its own declared twist. Exact matrix formulas are evaluated in floating point; eigenvalues, ranks and response residuals are numerical, not exact-arithmetic certificates.

The site mean is `Pvv`; connected covariance is `Cuv=-|Puv|^2`; joint occupation probability is `Juv=Puu Pvv-|Puv|^2` for distinct sites. A negative connected covariance is not a coincidence frequency. The response uses the occupied/empty spectral divided difference with a nonzero spectral gap. The supplied length-only dressing is `delta t_b=-t beta h_bb(exp(ik.v)+exp(ik.(v+b)))/4`, with `beta=1` chosen, not derived. The six metric coordinates use the Frobenius-orthonormal symmetric basis. `TT(k)` is defined by the **unwrapped continuum vector** `k=2 pi n/L !=0`; it is not a periodic lattice gauge construction.

The runner's exact momentum lists and all raw numerical rows define the finite sample. Rank uses both a relative threshold `1e-9 s_max` and an absolute floor `1e-14`; this is a declared diagnostic convention.

## T1 — finite sea identity

The reconstructed minimum-energy massless pi-flux seas have energies `-258.857540,-611.811768,-2063.196887` and gaps `3.464102,2.651309,1.793151` on the three tori. The nearest-axis projector magnitudes `0.199736,0.199157` on L6/L8 and site mean `1/2` agree with the conditional reference. These finite numerical identities do not select a physical vacuum.

## T2 — kinematic cubic content and diagonal TT projection

Under the 24 proper cubic rotations, site/axis-pair/face-diagonal classes carry `A1`, `A1+E`, `A1+E+T2`; the symmetric tensor carries `A1+E+T2`. For spatially uniform edge data, axis lengths have rank 3 and only diagonal tensor entries; adding the face diagonals spans rank 6. Shear is read from the difference of the two diagonals in its plane under this supplied geometric map.

For a zero-diagonal tensor with entries `(a,b,c)=(hxy,hxz,hyz)`, transversality is the three-by-three system with rows `(ky,kz,0)`, `(kx,0,kz)`, `(0,kx,ky)`. Its determinant is `-2 kx ky kz`. At nonzero k its kernel has dimension one on a coordinate plane and zero off the planes. This proves the diagonal-projection criterion on TT, before any dynamics or endpoint means. It does not prove the rank of the numerical response.

## T3 — sampled response and actual rank counterexamples

For the original selected response rows, the reported shear columns vanish, generic response rank is 3, and selected endpoint zeros lower it. The selected TT tables give rank 2 or 1 as recorded in the cache. The range `.0126-.0304` describes **largest** singular values in that sample; it is not a bound on all singular values, uniform conditioning, or a finite-size/long-wavelength limit. The smaller values and ratios remain in the original tables.

Endpoint factors `(1+exp(ik_b))/2` can further reduce rank. In the actual L6,m1 construction, `n=(3,3,3)` has all three factors zero and response rank zero at the absolute floor; `n=(3,3,1)` has TT rank one despite every component of k being nonzero. These are direct counterexamples to the former universal criterion. Vanishing input columns imply vanishing derivatives for every statistic of that fixed supplied state-construction map; they do not exclude a changed coupling.

## T4 — higher occupation statistics within the same ansatz

The original corner triple and plaquette determinants have zero first-order shear response for the selected configurations because the three shear input fields are zero. The stronger all-order statement is only composition of a shear-independent length-only map with a fixed state/readout procedure on its domain. No choice of statistic repairs a zero input in that map; a supplied shear-sensitive map changes the premise.

## T5 — projected site cancellation versus pair response

The uniform Fourier site component and the tested bond average cancel in the stated scalar controls, while the staggered site component and axis connected responses can remain nonzero. These are different projections of different observables. They neither prove pointwise cancellation nor force a formation-rate or clock law. The original alpha/beta sensitivity rows and numerical pair responses remain finite diagnostics.

## T6 — parity support and the order of a covariance zero

On even KS tori the two opposite-signed paths cancel, so `M^2` connects only `2Z^3` displacements. Since `{M,Eps}=0`, `H^2=M^2+m^2`; finite spectral calculus gives `f(H)=f_e(H^2)+H f_o(H^2)`. Thus a scalar spectral occupation function, constant on each degenerate eigenspace, has no matrix element with two or three odd displacement coordinates. A selected partial multiplet need not satisfy this premise. The gapped massless half-filled projector also has same-sublattice block `I/2`.

Consequently nearest face-diagonal connected covariance is zero on that state and its first derivative is zero for any differentiable kernel perturbation. Its joint probability is `1/4` at m=0. A nonzero first-order kernel entry can make the connected covariance change quadratically; no finite-amplitude frozen-count claim follows. The zero-flux comparison is retained as a change of supplied model.

## T7 — uniform patterns and genuine supplied alternatives

For **uniform shear parameters** and `2Z^3`-periodic NN coefficient patterns, the 24 bond classes carry `3A1+A2+4E+3T1+T2`, giving one T2 intertwiner up to scale. Its closed form on a c bond is `kappa h_ab (-1)^v_c[(-1)^v_a-(-1)^v_b]`. The massive sea's translation symmetry is the larger even-coordinate-sum sublattice; the massless case permits all shifts (with the appropriate KS gauge conventions). The period-two pattern is supplied, not forced by that vacuum symmetry.

The original supplied-intertwiner response tables retain rank 6 and TT rank 2 in their sampled rows. Only the shear columns scale with kappa; diagonal columns remain fixed. The small sixth singular value near `4.5e-6` at nonzero k is positive, not an exact dilation null mode. A uniform positive rescaling at k=0 can leave a massless projector unchanged; a nonuniform rescaling need not. Rotated-momentum singular spectra and Fourier leakage tests do not alone certify full response-matrix covariance.

The supplied centered curl is another, momentum-dependent, NN modulation. On the L6,m1 fixture at `n=(1,2,0)`, it raises the TT rank from one to two (`s_min` about `.0019720` at kappa=.5). The axial and `(1,1,0)` rank-one examples survive. Therefore the former universal curl no-escape and all-NN exclusion are false; only the uniform coefficient-class assertion above survives.

## Negative boundary and evidence

N1: tested alternatives include the uniform length-only, period-two, centered-curl and zero-flux models; this is not exhaustive. N2: zero shear input implies zero output derivative, and does not constitute an independent wall for each statistic. N3/N4: positivity, gap, finite torus and continuum-TT conventions bound the result; the explicit endpoint/curl counterexamples delimit it. N5/N6: no physical or universal no-go is asserted; changing the coupling is a conditional partial route. N7/N8: the curl counterexample is retained as an opposing result and earlier unsupported rhetoric is preserved only as history. Formal audit and unproved physical suppliers remain open.
