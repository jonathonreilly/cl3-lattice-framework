# Complete-native-instrument energy transfer and finite-resource leakage bounds

Verdict: the proposed bounds hold for the COMPLETE native K law, under the
native surviving-Hamiltonian intertwining identity stated explicitly below.
They do not extend by the same proof to the occupation-feedback column KJ,
normalized rare branches, or success through multiple intermediate cap tests.
The constants can be independent of matter volume although individual energy
translations in the exact lift need not have bounded support.

## The local algebraic input

Fix a source sector and one chosen legal edge. Work on the native physical
source/target Hilbert spaces, including degenerate head/Record storage and the
fuel transition. Write
 Ain=Hrem+h_e+q Delta, Aout=Hrem,out+(q-1)Delta.
Package BOTH signs in one column K. Required identities are
 K*K=I_source, Hrem,out K=K Hrem, ||h_e||<=t.
These are properties of the complete native instrument with surviving hopping
commuting with the newly imposed physical edge Record. On a bridge the actual
parity-projector branches must be used; inserting another1/sqrt(2) would destroy
the completeness identity. The reduced bridge parity description is consistent
because the surviving disconnected-component Hamiltonian preserves its parity.
Neither an arbitrary Kraus instrument nor completeness alone implies the second
identity: it is a load-bearing local algebraic premise.

Set V(tau)=exp(-i tau Aout) K exp(+i tau Ain), the full-line battery lift in
Fourier representation. For EB=-i partial_tau,
 [EB,V](tau)=exp(-i tau Aout)(K Ain-Aout K)exp(+i tau Ain)
           =exp(-i tau Aout)K(h_e+Delta)exp(+i tau Ain).
Therefore
 ||[EB,V]|| <= C := Delta+t.                              (1)
In fact ||K(h_e+Delta)||=||h_e+Delta|| on the source, since K is an isometry.
This proof uses the local deleted hopping norm, not ||Ain|| or system size.
The fuel phase exp(+i tau Delta) is essential to the sign in(1).

This is a norm bound on the COMBINED sign column, not a bound obtained by
adding two independently priced sign channels. Controlled head/history maps
have the same bound if source sectors are orthogonal and their target histories
or channel registers are orthogonal. An unproved coherent sum with interfering
source/target labels is not covered.

## Domain statement

For every finite matter volume, Ain/Aout are bounded self-adjoint matrices.
The multiplier V(tau) is strongly differentiable with bounded derivative given
above. Consequently V maps the battery Sobolev domain H1(R) into the output
H1 domain, and EB V-V EB extends to the bounded operator(1). The same statement
holds after adjoining an arbitrary reference. Thus formulas involving EB below
are identities on a common core followed by bounded-operator extensions, not
formal manipulations of unrestricted unbounded products.

The bound is uniform over finite matter volumes satisfying the same local
identities. It is not, by itself, construction of an infinite-volume global
Hamiltonian or an infinite-volume battery lift. Such a limit requires a separate
representation/dynamics argument; uniform finite-volume estimates remain valid.

## Spectral-gap leakage bound: no finite energy-shift assumption

Let P_I project input battery energy to I=[b,b+w], with b>0. Let P_- be the
output projector onto E<0. Put X=P_- V P_I and
 Y=P_-[EB,V]P_I. On the spectral subspaces, EB,out X-X EB,in=Y. The separated
spectra permit the convergent Sylvester integral
 X=-integral_0^infinity exp(s EB,out) Y exp(-s EB,in) ds.
The semigroups have product norm at most exp(-bs), hence
 ||P_- V P_I||<=C/b.                                     (2)
This can be proved first with bounded spectral cutoffs and then by strong
limits; the integrable norm bound is unchanged. The output half-line operator
is unbounded below but exp(s EB,out) is bounded there, so the integral is well
posed. No assertion about the support of individual spectral translations is
needed.

For a cap Ecap>b+w, let u=Ecap-b-w>0 and P_+ project onto E>Ecap. Reversing the
semigroup signs gives
 ||P_+ V P_I||<=C/u.                                     (3)
The two leaked ranges are orthogonal. Therefore, for any normalized input
supported in P_I (including matter/reference/battery entanglement),
 Prob(outside[0,Ecap])
 <=min{1,C²[b^-2+u^-2]}.                                 (4)
These are absolute unconditional probabilities for the complete event column.
They do not bound a normalized postselected sign branch independent of its
probability. Closed interval endpoints have no adverse effect on the gap bound.

## A cap with refusal preserves exact total energy

Let Pcap be the battery cap projector, and restrict the input Hilbert space to
its range. Form the ONE combined accepted column S=Pcap,out V Pcap,in. Define
 F=(I_cap-S*S)^(1/2), and map F into an absorbing refusal copy carrying the SAME
input total Hamiltonian. Because the full lift intertwines total energy and
battery projections commute with the respective total Hamiltonians, S still
intertwines. Hence S*S strongly commutes with input total energy, and so does
its square-root complement F. The completed column (S,F) is an isometry and
preserves the modeled total-energy distribution exactly.

For an input supported in I inside the cap, refusal probability is precisely
the leakage probability in(4). Thus exact energy-preserving cap completion can
have high success probability without a global spectral norm enclosure. It
still uses a continuous capped battery Hilbert space, and refusal is a real
outcome. Complete the TWO-sign column once, not each sign independently.
This assertion concerns the complete-event law. The feedback GKSL law requires
its own actual effect/anticommutator and is not changed into this law by adding
identity-rate refusal jumps.

## Prescribed complete prefixes with one retained battery

For k prescribed complete event columns, including all native signs and any
free evolutions U_j that strongly commute with EB, form the full unconditioned
prefix isometry V^(k). Leibniz telescoping gives
 ||[EB,V^(k)]|| <=sum_j C_j<=kC.                          (5)
Interposed free U_j cost zero; every other factor is an isometry/contraction
with norm1. The battery is retained; no product/reset assumption between events
is used. Equations(2)–(4) apply at the ENDPOINT with C replaced by kC.
Prescribed source-dependent edge choices are allowed only as complete controlled
isometries with orthogonal histories and the same uniform transfer bound.

Endpoint leakage does not bound the probability that an intermediate cap test
would have refused. Repeated tests disturb the retained state, and coherent
excursions could return before the endpoint. A separate union/disturbance or
stopping-time coupling argument is required; none is supplied here.

## Fixed laboratory time: uniformization with noncommuting free evolution

For the complete native GKSL law take jumps sqrt(gamma)V_s,e,z. Their source
rate is gamma d_s I_s with d_s<=D. Set Lambda=gamma D>0 and define a complete
uniformized channel Gamma with jump column
 W=( {sqrt(gamma/Lambda)V_s,e,z}_{s,e,z},
          sqrt(I-R/Lambda) ),
 R=gamma direct_sum d_s I_s.
The null term is block-diagonal in head/history and independent of battery,
so it commutes with EB. Summing source blocks gives W*W=I and
 ||[EB,W]||² <=(gamma/Lambda)D C²=C².                    (6)
History/channel orthogonality is needed exactly as for(1). The null tick is a
mathematical uniformization device, not an extra physical Record event.

The generator is -i[Htotal,.]+Lambda(Gamma-I). Htotal includes the full system
Hamiltonian and EB; its free unitary strongly commutes with EB. Gamma need NOT
commute with that free unitary. The bounded-jump Dyson expansion gives a Poisson
number N of ticks with mean lambda=Lambda T; conditional on N=n, the ordered
tick times carry the usual simplex measure, and n copies of Gamma are
interleaved with the actual free unitary segments. Each such dilation has
commutator norm<=nC by(5)–(6). This is the correct noncommuting uniformization;
replacing it by Gamma^N followed by one free unitary is generally wrong.

Let the initial battery have mean mu and standard deviation sigma, and purify
any matter input with a reference. On every n-tick dilation,
 ||(EB-mu)V_n psi||
 <=||V_n(EB-mu)psi||+||[EB,V_n]psi||<=sigma+nC.
This uses finite initial second moment. It is valid for a fixed product battery
input; indeed a correlated input with the same second moment satisfies the same
inequality. Averaging the squared norm over the Poisson mixture yields
 E[(EB,out-mu)²]
 <=sigma²+2sigma C lambda+C²(lambda²+lambda).             (7)
Thus the proposed RMS bound is the square root of(7). The center remains the
INITIAL mu, so this controls both drift and variance together. It is not a
claim that the battery mean is constant, monotone or close without pricing the
C lambda term. For a sine packet, sigma²=w²[1/12-1/(2pi²)].

Chebyshev gives a volume-uniform ENDPOINT cap-leakage estimate from(7), using
the smaller distance of mu to the two cap boundaries. If the initial battery
also has support I, a second endpoint estimate follows directly from(5):
 Prob(Ebout outside[0,Ecap])
 <=min{1,C²(lambda²+lambda)[b^-2+u^-2]}.                 (8)
Here the Poisson second moment is explicit. Neither(7) nor(8) by itself controls
the first refusal probability of a repeatedly capped process.

## Restrictions and practical meaning

* The operator identity Hrem,out K=K Hrem and complete K*K=I are indispensable.
  For KJ, M=J*J is nontrivial and the simple local transfer reduction generally
  includes commutators with surviving matter terms. The previous feedback
  negative-drift witness is not contradicted; that law is outside this lemma.
* All means/probabilities above are for complete channels or unconditioned
  fixed-time laws. Conditioning on a rare path/sign can amplify energy change;
  no probability-independent conditional bound is asserted.
* These bounds replace an extensive global-energy-support enclosure by a
  volume-uniform probability estimate. They permit arbitrarily small nonzero
  spectral tails and do not establish a hard finite translation range.
* A cap-completed single event is exactly total-energy preserving with refusal.
  A finitely truncated matter-neighborhood approximation from the earlier memo
  generally is not. Combining those constructions requires separate errors;
  their guarantees must not be silently conflated.
* A continuous battery, local native algebra, head/fuel preparation, reservoir,
  memory and refusal storage remain supplied resources. This is not a finite
  local-qubit realization, entropy accounting, fuel optimum or renewal theorem.

No numerical parameters were retuned. The derivations above use elementary
bounded-commutator, spectral-gap integral, isometry and Poisson identities;
no external result with unverified locality/domain conditions is imported.
