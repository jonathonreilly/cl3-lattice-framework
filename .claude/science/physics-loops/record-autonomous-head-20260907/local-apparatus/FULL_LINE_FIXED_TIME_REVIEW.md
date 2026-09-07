# Independent check: finite laboratory-time localization estimate

Verdict: the proposed finite-time bounds are correct under the explicit
finite-sector, common-free-Hamiltonian and uniform-locality hypotheses below.
The argument does not reset the retained battery and does not normalize
postselected branches. No counterexample was found under those hypotheses.
There are material prerequisites for using it beyond the original four-event
nonbridge calculation; these are listed at the end.

## Precise setup

Let Hsys be a finite direct sum of all required history/head/Record sectors,
with bounded block-diagonal A=direct_sum A_s. Let HB=L2(R,d tau) and
P=-i partial_tau. Both models have the SAME free H=A tensor I+I tensor P.
Let L_i(tau) and M_i(tau) be the exact and matter-truncated lifted jumps,
viewed as bounded multiplication operators on Hsys tensor HB. Include all
native sign outcomes and actual source/history labels. Their GKSL generators
use their respective actual sums L_i*L_i and M_i*M_i. In particular a
matter-dependent directed-hop instrument is not completed to graph-degree I.

Assume each outgoing edge has a combined sign-column norm<=sqrt(gamma), and
there are at most D outgoing edges per source sector. Assume the corresponding
edge-column difference is <=sqrt(gamma) delta_R(tau). On the Fourier band
|tau|<=Tcut+Tlab suppose
 delta_R(tau)<=epsilon=C_R exp[-mu(R-a-v(Tcut+Tlab))].
Constants are uniform over every included source sector and edge. For complete
native instruments, the truncated edge column is still an isometry after
removing sqrt(gamma), even if different edges use different truncated input
Hamiltonians. For directed-hop columns its norm remains<=1; their effects need
not agree or sum to a scalar, which causes no problem for the bound.

## Source/channel orthogonality and the factor D

Use a Stinespring column V=(L_i)_i, so ||V||²=||sum_i L_i*L_i||. With explicit
source labels i=(s,e,z), each term is supported on its source projector P_s.
Thus source blocks are orthogonal and
 sum_i L_i*L_i <= gamma D I, and likewise for M.
For the column difference E=V-W, sum_i (L_i-M_i)*(L_i-M_i) is also source
block diagonal and bounded by gamma D delta_R² I. Hence
 ||V||,||W||<=sqrt(gamma D), ||V-W||<=sqrt(gamma D)delta_R.
Different local truncations for different edges do not spoil these inequalities.
They would fail if one coherently combined jump amplitudes with identical
channel labels and overlapping target histories without retaining the requisite
source/target orthogonality. Keep separate channel labels, or prove the appended
history makes the combined targets orthogonal. An unspecified coherent sum
across sources is not interchangeable with a classical sum of GKSL channels.

## Fourier marginal transport: the sign and a rigorous formulation

The Schrödinger free battery unitary exp(-itP) acts as f(tau)->f(tau-t).
The exact and approximate jump operators commute with every multiplication
projector Q_B=1_B(tau); so do A and all products L_i*L_i. Therefore each
GKSL dissipator annihilates Q_B in the Heisenberg picture. This is stronger
than a formal pointwise trace calculation and applies to arbitrary correlated
states without assuming a smooth integral kernel. Only the free translation
changes this spectral measure. Consequently
 p_t(tau)=p_0(tau-t)
for either model, as an equality of measures/densities. The plus-moving
support is B+t, not B-t. This remains true although system/battery correlations
and off-diagonal Fourier coherences evolve nontrivially.

In the interaction picture of P, jumps are L_i(tau+t) and M_i(tau+t); A is
unchanged. A fixed initial band |tau|<=Tcut therefore stays an invariant band
in that picture. On 0<=t<=Tlab, every sampled argument lies within
|tau+t|<=Tcut+Tlab. The proposed enlarged cone is the correct one.

## Bounded-generator Duhamel estimate on the band

For columns V,W the completely bounded trace-norm difference between their
CP terms is at most (||V||+||W||)||V-W||. The effect difference satisfies the
same bound in operator norm. The half-anticommutator difference costs at most
that effect norm. Thus
 ||D_V-D_W||_diamond <=2(||V||+||W||)||V-W||
                         <=4 gamma D delta_R.                (1)
The same free commutator cancels between the two generators.

On the fixed initial Fourier band in the interaction picture, all operators
are bounded. The time-dependent jumps are norm-continuous: finite bounded
A_s gives a uniform derivative bound for their exponential fibers. Standard
bounded time-dependent GKSL evolution therefore gives CPTP propagators on
trace class. Duhamel variation and complete trace-norm contractivity yield
 ||E_T-G_T||_diamond,band <=4 gamma D T epsilon, 0<=T<=Tlab. (2)
The reference system is arbitrary and untouched. Equation(2) is a norm bound
on the band-restricted joint system/battery inputs, including correlations.
The original unbounded P creates no hidden Duhamel domain assumption because
it was removed by a common strongly continuous unitary interaction picture.
One must not instead apply an unqualified bounded-generator estimate directly
to -i[P,.] on all trace-class operators.

## From a band estimate to a fixed product battery

Let eta=integral_|tau|>Tcut |beta_hat(tau)|². Start from an arbitrary system-plus-
reference state tensor |beta><beta|. Assume 0<=eta<1.

If battery is RETAINED in the output, replace beta by its normalized band
projection beta_good. Their initial pure-state trace distance is2sqrt(eta).
Contractivity for each of the two CPTP evolutions costs that amount twice.
Using(2) on the common normalized band input gives
 ||Psi_T,beta-Psi_T,beta,R||_diamond
 <=min{2,4 gamma D T epsilon+4sqrt(eta)}.                    (3)
These map norms have system as input and system+battery as output; beta is
fixed by the map, not an arbitrary unrestricted battery input.

If battery is DISCARDED, an improved tail estimate applies. The diagonal
Fourier kernel closes: for each starting tau0 it evolves as a finite-dimensional
system GKSL equation with Hamiltonian A and jumps L_i(tau0+t). Its solution is
a CPTP channel E_T,tau0. Thus the reduced channel is exactly
 integral p_0(tau0) E_T,tau0 d tau0,
including arbitrary reference entanglement. Off-diagonal Fourier elements do
not contribute after the battery trace. The two models have the same weights
p_0. Good-band contributions obey(2), and bad-band channel differences are
at most2. Therefore
 ||Phi_T,beta-Phi_T,beta,R||_diamond
 <=min{2,4 gamma D T epsilon+2eta}.                         (4)
The factor2eta is valid only after tracing battery; replacing the retained
coherent tail by a classical mixture would not justify it for(3).

For the sine width w, the previously derived explicit inequality
 eta<=min{1,32pi/[3(w Tcut)^3]}, Tcut>=sqrt(2)pi/w,
can be substituted into(3)–(4). It is independent of the packet's energy
translation. The result has an exponential locality term and a polynomial
Fourier-tail term, without requiring an exponential moment of the sine Fourier
density. No parameter tuning was performed or proposed here.

## Exact qualifications before application

1. Both comparison models must be CPTP on the SAME full-line battery space
   and the same complete finite history system. Retaining all fuel-deleting
   histories through physical exhaustion is finite (at most12events in this
   cube). Keeping only the first four histories without a specified absorbing
   completion would not define the same full-time model or justify trace
   contractivity. Artificial four-event stopping would be a different process.
2. Uniform delta_R must hold for all included histories, including bridges,
   dark sectors and any prescribed refusal sectors. A locality result proved
   only for the first-four connected CAR gauge is insufficient. The physical
   native local instrument and bounded local Hamiltonian extensions have to be
   supplied and checked on the full ambient qubit algebra.
3. The same full free H is essential. Truncating free A as well adds a separate
   Hamiltonian difference whose global norm can be extensive; it is not covered
   by(1). The present approximation localizes jumps' dependence on distant
   matter, not the already local full many-body free Hamiltonian.
4. On the full energy line the approximate lifted jumps need not conserve
   the ORIGINAL total energy, and the initially positive packet need not remain
   positive-energy or within cap97. Inserting an energy cap changes the Fourier
   multiplication structure and hence the exact translation/moving-band argument.
   No capped-positive-battery finite-time approximation follows without an
   independent leakage bound and a separately specified CP completion.
5. The mathematical battery and Fourier-controlled operator remain continuous.
   The statement does not exhibit a finite physical battery, local microscopic
   couplings, one-site/Z3 admissibility, native preparation, entropy sink or
   indefinite renewal. Relative or normalized postselected errors need separate
   outcome-probability lower bounds; no such normalization is used here.

## Relation to the literature

The spatial input is the bounded-interaction LR theorem already checked in
Sims, *Lieb-Robinson Bounds and Quasi-locality for the Dynamics of Many-Body
Quantum Systems*, Section3, https://arxiv.org/pdf/1011.4540. The moving-band,
column-norm, Fourier-marginal and fixed-battery Duhamel estimates above are
explicit algebraic deductions, not quotations of a stronger localization
or physical-apparatus theorem from that reference.
