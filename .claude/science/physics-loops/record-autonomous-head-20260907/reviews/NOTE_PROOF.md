# Cold proof/scope review of autonomous head note

Reviewed the authored note's analytical claims, not my orbital implementation.
Read the native matter-instrument parent for physical Z commutation, branch
completeness, h_e norm, and old Record/N preservation. No source edits.

## Verdict

No blocking mathematical defect found in the stated conditional construction.
The positive fuel theorem is a valid stronger result than conservation alone:
Delta >= t makes the sign-summed battery increment operator positive on the
invariant no-refusal domain, including correlated joint inputs. The note keeps
individual sign outcomes, unsafe refusal, locality, entropy and renewal outside
that conclusion. Pending audit and conditional-support status are explicit.

Two small precision improvements would make the theorem more self-contained:

1. Define the safe domain by a total-energy projector, rather than leaving
   "invariant safe domain" implicit. With M=L(Delta+t), take the blockwise
   `Q=1_[b,b+w+M](H_total)`, assuming cap contains [b-M,b+w+M]. For every legal
   sector, system spectrum lies in [0,M], so Q implies battery support in the
   stated enclosing interval. Intertwining preserves Q and full-line lifted
   outputs lie in the cap, hence F Q=0. The initial battery-support assumption
   puts every joint input, including correlated inputs, in Q. This explicit
   definition prevents misreading the enlarged battery support interval itself
   as sufficient to restart the proof with arbitrary new correlations.

2. State that the I in F=(I-sum S_z* S_z)^(1/2) is the identity on the capped
   input sector, and label F_(s,e) and the absorbing copy per eligible edge (or
   explicitly allow separate jump operators into a common absorbing copy).
   Existing prose implies this correctly; explicit notation removes ambiguity
   about an unwanted full-line complement or double counting of signs.

These are proof-clarity recommendations, not identified failures. The remainder
below records the actual checks and scope boundaries.

## Generator and energy distribution

A legal history must consume a previously live edge, so its length is at most L.
With finite vertices, sign records and native code dimensions, there are finitely
many legal history sectors. The continuous cap leaves Hilbert space infinite
-dimensional, but E_B, all A_s, all capped branch operators, and their finite sum
are bounded. The direct-sum Hamiltonian and stated GKSL generator are consequently
bounded. Histories make sector-dependent transitions part of one fixed generator;
there is no event-count cutoff in its transition rule. Four events is only the
analysis horizon. A degree-zero state has no outgoing event and a refusal copy
has no outgoing jump by definition.

Full-line spectral shifting interwines full energies including the fuel once.
In Fourier fibers the completed native column is an isometry, including bridge
projectors without an extra sqrt(2). Compression by input/output caps is a
contraction. Since caps commute with total energy, the compressed maps still
intertwine it; S* S commutes with input total energy, and so does its positive
square-root complement. The refusal copy uses the same Hamiltonian, hence its
embedding also intertwines. Bounded functional calculus then gives the same
intertwining for every bounded Borel f(H_total). Each Lindblad dissipator
annihilates that observable, as does the free Hamiltonian term. This proof covers
cap-unsafe states too; zero-refusal and battery monotonicity do not.

Multiple eligibility-labelled jumps from different legal source sectors do not
need coherent identification. Their finite direct-sum GKSL law may decohere
superpositions between histories, but it still preserves the total-energy
spectral distribution. The stated classical waiting law is correctly restricted
to a safe definite head/mask sector, rather than being asserted for arbitrary
coherent history superpositions.

## Support and nonnegative battery drift

The parent establishes ||h_e||<=t and commuting surviving physical hoppings
with the measured Z_e. Therefore 0<=Delta I+h_e<=(Delta+t)I when Delta>=t,
and summation gives 0<=A_s<=M without a commuting-hopping assumption. The note's
safe interval [24,73] and optional translated resource bound [0,49] follow from
M=24. These are sufficient enclosures; they are not optimal spectral supports.
The optional translated packet is clearly not substituted into the experiment.

Native nonselective pullback of the output Hamiltonian equals H_R-h_e plus
(|R|-1)Delta on the input code, even at bridges, because surviving terms commute
with the actual measured Z_e. Thus A_s - sum K_z* A_s' K_z=Delta I+h_e.
For Y_z=e^(-i tau A_s')K_z e^(i tau A_s), direct differentiation gives
sum -iY_z*Y_z'=e^(-i tau A_s)(Delta I+h_e)e^(i tau A_s)>=0. This sign matches
T_u|E>=|E+u> and the declared Fourier convention. Its joint-state expectation
is nonnegative without a product-state or stationarity assumption. The
finite-energy capped safe states can be handled by extension of the bounded
energy-difference identity; no unspoken smooth battery wavefunction hypothesis
is needed for the final inequality.

On that invariant safe domain, summed S* S=I per eligible edge, so the
Lindblad anti-commutator yields precisely the above sign-summed drift. Free total
Hamiltonian evolution commutes with E_B. On unsafe inputs S* S need not be I,
and F need not commute with E_B; the note explicitly does not extend positivity
there. Positivity of mean increment is also not positivity of every spectral
energy shift or every selected bridge branch.

## Numerical and scope wording

The finite path statements use edge paths, complete sign instruments and exact
mass. Connected output prefixes justify nonbridge use through four events.
Head timing and pre/post deletion/wait indexing are stated correctly. The
averaged-state current comparator is carefully distinguished from mean absolute
current, mean threshold indicator and a fixed laboratory-time ensemble. The
24/24 trajectory-front pass does not hide the 24/24 trajectory support failure.
The 71/90 surface count is explicitly not a count of independent trajectories.

The finite commensurate ladder is described as an implementation witness, not a
finite realization of irrational cube shifts. Supplied reservoir, global spectral
lift, initial preparation, carrier, time and routing roles are retained as premises.
The proposed_retained label is immediately qualified by actual conditional-support,
unset independent audit and audit-required-before-effective-retained metadata.
No generic framework-derived formation law is claimed.

The four-way ablation memo may be incorporated only as a finite matched diagnosis.
In particular its pre4 pattern A0/24, B24/24, C24/24, D12/24 prevents a monotone
claim that greater coherence or less waiting always increases live support. Its
ideal comparator has no normalized finite-energy preparation. The memo's exact
real-H symmetry statements properly distinguish finite positive-time averages
from infinite-time nondegenerate dephasing and retain degenerate coherent blocks.
