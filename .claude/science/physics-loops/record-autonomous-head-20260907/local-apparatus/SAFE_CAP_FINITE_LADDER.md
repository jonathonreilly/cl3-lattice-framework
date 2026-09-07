# Fixed safe-cap finite ladder: direct finite-time comparison

## Result

For the ORIGINAL complete-native cube law, its exact invariant Q-safe battery
cap allows a stronger finite-ladder approximation without a Poisson or repeated-
cap penalty. At gamma=t=Delta=w=T=1, original packet[48,49] and original cap97,
choose delta=1/320 and M=31040 positive ladder levels. The retained-output trace
norm error is strictly below221/2240<0.1. A conservative original total-energy
mean error is at most481/51200<0.01. The free matter Hamiltonian remains the
original A, not its rounded version.

The comparison input is a fixed legal initial head/fuel/Record sector with an
arbitrary admissible matter/reference state and the fixed sine battery, or a
classical mixture of legal source sectors for which the same safe-support
hypothesis holds. It is NOT a claim on coherent superpositions of distinct
source sectors. All native sign outcomes and refusal outputs are retained.
The theorem is a finite-dimensional GKSL apparatus construction, not a local
closed bath, nearest-neighbor spectral implementation or axiomatic admission.

## Exact safe reference

Write full system sector energy A_s=H_live+Delta livefuel. On the finite cube,
||A_s||<=24 for every legal sector. The original battery packet[48,49] and total-
energy intertwining imply initial Q support[24,73] and subsequent battery
support[0,97]. This holds for any admissible matter input in the fixed initial
sector, all later histories, and all free evolution times. The exact combined
cap-refusal complement has ZERO amplitude throughout this reference evolution.
Thus the exact capped evolution equals the full-line evolution on this class.

Use one complete native column V_e for all signs of each eligible edge. On its
source block V_e*V_e=I. Native bridge signs use their complete parity branches;
no additional fair-sign factor is inserted on bridges. At most D=3 edges are
eligible. Set Lambda=gamma D; here Lambda=3. The proof below uses Lambda only
as a degree/rate bound and does NOT use Poisson uniformization.

## Rounding and the accepted/refusal comparison

Spectrally round every full finite sector Hamiltonian A_s to delta Z with the
same eigenvectors, obtaining A_s^delta with norm error<=delta/2. Let W_e be the
corresponding full-line lifted column. It is complete, and
 ||V_e(tau)-W_e(tau)||<=delta|tau|.                       (1)
Both exponential factors contribute(delta/2)|tau|. Fuel is included once;
for delta=1/320 the gap Delta=1 is exactly320 mesh steps, so full-sector rounding
can equivalently retain exact fuel energies and round only matter energies.

Let P cap battery energy to[0,97], S_e=P W_e P, and
 F_e=(I_cap-S_e*S_e)^(1/2).
More generally replace I by the legal source effect E_e on an ambient space.
The accepted TWO-sign column is capped once and gets ONE absorbing refusal
complement. The completed approximate edge column is complete with exactly the
same source effect as the exact completed instrument. Therefore their GKSL
anticommutator terms cancel identically.

For a positive reference source-block state rho of trace p, define
 alpha_e²=Tr[(V_e-W_e)*(V_e-W_e)rho].
Exact safety means(I-P)V_e sqrt(rho)=0. Consequently
 ||(S_e-V_e)sqrt(rho)||_2<=alpha_e,
 Tr(F_e*F_e rho)=||(I-P)W_e sqrt(rho)||_2²<=alpha_e².
Put the exact zero-refusal column in the same output/refusal label space. The
two complete isometry columns differ on sqrt(rho) by at most sqrt(2)alpha_e.
Their output density difference, including the absorbing flag, is therefore
 <=2sqrt(2)sqrt(p)alpha_e in trace norm.                 (2)
This is state-dependent control along the exact SAFE evolution, not a uniform
operator estimate on all cap states. Approximate safety is not assumed.

## Generator Duhamel along the exact flow

Exact evolution from the declared initial class remains block diagonal in
legal source sectors, with arbitrary matter/reference coherence inside each
block. Let p_s be block trace and let
 a_s²=integral delta² tau² Tr[rho_s(tau,tau)]d tau.
Equation(1) bounds alpha_s,e<=a_s for each edge. Summing(2), using d_s<=D and
Cauchy-Schwarz sum_s sqrt(p_s)a_s<=sqrt(sum_s a_s²), yields
 ||(G_approx-G_exact)(rho_t)||_1
 <=2sqrt(2)Lambda delta sqrt(integral tau² p_t(tau)d tau). (3)
The free Hamiltonian is still identical in this comparison. There is no extra
anticommutator bound because complete accepted/refusal effects agree.

Both generators are CPTP on the capped Hilbert space, using their actual
absorbing sectors. Duhamel variation applies the approximate propagator AFTER
the difference in(3), and the EXACT safe propagator before it. Trace
contractivity therefore integrates(3); the approximate flow need not remain
Q-safe and need not have a translating Fourier density after cap compression.
No reset, projected-input safety assumption or first-exit estimate is used.

For the exact reference, full-line Fourier multiplication jumps have pointwise
trace-preserving dissipators, while free EB=-i partial_tau translates the
Fourier marginal: p_t(tau)=p_0(tau-t). The sine packet has even p_0,
integral tau p_0=0, and integral tau² p_0=||beta'||²=pi²/w².
Thus the exact second moment is pi²/w²+t². Combining with(3),
 capped rounded-jump versus exact distance
 <=2sqrt(2)Lambda delta integral_0^T sqrt(pi²/w²+t²)dt
 <=2sqrt(2)Lambda delta T sqrt(pi²/w²+T²).               (4)
Purification and a supremum over admissible matter/reference inputs make this
a diamond norm of the maps from MATTER in the fixed legal initial sector to
the full retained output, with the declared initial battery fixed. It is not
an unrestricted direct-sum/battery-input diamond statement.

## Cell embedding and the finite positive battery

Use cells[j delta,(j+1)delta), ladder centers(j+1/2)delta, and let P_delta be
projection to normalized cell-constant functions. Integer shifts of W_e
preserve this subspace. With cap97=M delta, the cap projection is a union of
whole cells and commutes with P_delta. Hence S_e, S_e*S_e and its square-root
complement F_e all preserve the cell subspace and its orthogonal complement.
This last fact is essential: it gives an actual finite refusal matrix, not an
assumption that functional calculus preserves an arbitrary truncated space.

Replace ONLY free EB by the cell-center multiplication operator EB^delta.
Its norm difference from EB is<=delta/2; the free original matter A remains
unchanged. The resulting dynamical trace error is<=delta T. This separate
bounded perturbation step is done after(4), and does not assume Fourier
translation for the rounded-battery dynamics.

Finally replace beta by beta_delta=P_delta beta/||P_delta beta||. The cellwise
Poincare bound gives ||beta-P_delta beta||<=delta/w, so the pure preparation
trace error is<=2delta/w. By contractivity this is its total dynamical cost.
The triangle order is deliberate: (4) uses the EXACT original safe beta, then
free EB is rounded, then the initial packet is projected. No claim that the
projected packet has the original invariant Q support is needed.

Restricting the final model to j=0,...,M-1 gives a genuine finite positive
battery with energies delta/2,...,97-delta/2. Combining all steps,
 distance<=delta[2/w+T+2sqrt(2)Lambda T sqrt(pi²/w²+T²)].  (5)
An exact integral in(4) gives a slightly sharper constant, not used below.

## Rational certificate with the frozen packet/cap

Take gamma=t=Delta=w=T=1, D=3, delta=1/320, cap97.
Then M=97*320=31040<32768=2^15. Packet endpoints48 and49 are exact cell
boundaries. No original preparation, gap, gamma, cap or time is retuned.
Using pi<22/7, sqrt(2)<10/7, and sqrt(pi²+1)<10/3 (the latter follows from
9*533<100*49), the coefficient in(5) is strictly below
 3+2*(10/7)*3*(10/3)=221/7.
Therefore
 distance<221/(7*320)=221/2240<1/10.                    (6)
The strict final inequality is2210<2240. This is an analytic certificate,
not a simulation of the full enlarged apparatus Hilbert space.

Battery storage is15qubits with1728unused code states. With the specified
native12edge qubits,12fuel qubits,8one-hot head qubits and1refusal flag, total
system storage is48qubits. This counts the stated native fields and finite
battery, not a physical Markov bath or an additional explicitly stored ordered
trajectory. Any separate history register demanded by a different realization
must be counted separately. The ambient/local grouping theorem for the declared
class, or equivalent native Markov jump specification, is needed to avoid
silently adding an uncounted system-history memory.

## Rounded global energy with the original free A

For the WHOLE finite cube, A_s^delta=f_delta(A_s), so[A_s,A_s^delta]=0.
Every integer-shift jump and its capped refusal completion conserve
Hdelta=A^delta+EB^delta. The chosen free Hamiltonian is A+EB^delta; it COMMUTES
with Hdelta even though it is not equal to Hdelta. Thus the finite GKSL model
exactly preserves the rounded global total-energy distribution, including
refusal. Equality of free A and rounded A was unnecessary; commutation suffices.

Under the cell embedding, the difference between original total energy and
rounded total energy is bounded by delta (delta/2 from matter and battery).
Its original total-energy mean can drift by at most2delta between its own
initial and final states. Relative to the unprojected sine input, the initial
battery-mean error is bounded conservatively by delta+2delta²/w. Therefore
 original total-energy mean error<=3delta+2delta²/w
 =3/320+2/320²=481/51200<1/100.                         (7)
This bound follows from rounded conservation plus bounded operator/preparation
errors, not from a trace estimate against an unbounded observable.

Here cell alignment and reflection about48.5 in fact preserve the projected
packet's mean exactly. Thus the conservative2delta dynamic bound is already
sufficient for the aligned preparation; equation(7) remains a valid looser
certificate. No exact conservation of the unrounded energy DISTRIBUTION is
claimed. Keeping full global free A together with LOCAL truncated A_R^delta
would generally lose the commutation property; this whole-cube energy result
must not be transferred to that different construction.

## Local-jump extension and limitations

The safe-reference argument also permits a local approximation: replace the
rounding-only norm in(1) by a verified local-truncation-plus-rounding fiber
error and use its RMS under the EXACT p_t in(3). The cap/refusal triangle remains
valid. Locality assumptions, source-pattern controls and boundary-energy defects
must still be checked; no exact rounded-global-energy promise follows there.

The proof supplies a finite positive ladder, complete finite GKSL matrices,
retained-state error and rounded energy accounting for the declared initial
class. The whole-cube spectral controls need not be nearest-neighbor or native
one-site/Z3 operations. A local physical bath, entropy and reset costs,
preparation law, closed-unitary dilation and renewal remain outside this result.
