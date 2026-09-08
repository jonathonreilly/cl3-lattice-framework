# Full-carrier local eighth-order diagonal tables

The historical plan concerned a hard charge gate. This calculation instead uses the full carrier with D equal to the sum of squared degree deviations, and V equal to the actual native signed edge flips. No intermediate state is refused. U is set to one in the tables; degree-eight coefficients restore U^-7 and the appropriate coupling monomials.

## Finite cluster identification

Fix an exterior ice bitstring and activate at most four edges. In relative toggle coordinates z, the energy is

D(z)=sum_v [sum_{e incident v} z_e(1−2b_e)]².

The native flips square to one, anticommute exactly for incident edges, and commute otherwise. In a local edge ordering they are represented by X_e times Z on earlier incident active edges. Fixed exterior factors only change individual edge signs, removable by conjugating Z_e. Different edge orderings give diagonal quadratic phase conjugations. These changes preserve diagonal energies and canonical effective diagonal entries. Thus this finite representation retains the native algebra; it is not replacement by bare X.

For a forest, leaf induction gives a unique zero-energy toggle configuration z=0. The exact analytic eigenvalue recurrence, with intermediate normalization psi_n(0)=0 for n>0, is

E_n=(V psi_(n−1))(0),
psi_n(z)=[−(V psi_(n−1))(z)+sum_(j=1)^(n−1) E_j psi_(n−j)(z)]/D(z).

All energy-feedback terms are retained. This is the canonical diagonal because the fixed-exterior ice space is rank one.

## Independent contour extraction

Let R0(z)=(z−D)^−1. The sum of eigenvalues in the low-energy Riesz cluster is the contour integral of z Tr(z−H)^−1. The resolvent trace is the z derivative of log det(z−H). Expanding

log det(z−D−gV)=log det(z−D)−sum_(k>=1) g^k Tr[(R0V)^k]/k

and integrating z times the derivative gives

E_k,total=(1/k) Res_(z=0) Tr[(R0(z)V)^k].

This is a finite-dimensional analytic contour identity, not a scalar rank-one assumption. Each closed k-step walk contributes its native phase times k denominator factors at its visited states. With q zero-energy denominators, the residue is the coefficient of z^(q−1) in the product of the remaining factors. Each nonzero factor expands as −sum_(a>=0)z^a/D^(a+1). The implementation retains those coefficients exactly with Fraction arithmetic. Rank-one agreement through eighth order was checked independently against the feedback recurrence on all one-edge, pair and three-star bit inputs. The one-edge eighth coefficient is 5/128, as also follows from 1−sqrt(1+g²).

## Alternating cycle and canonical diagonal

Only alternating four-cycle inputs have two zero-energy states. The product S of its four native A operators commutes with every active A: each edge has two incident anticommuting neighbors. It toggles all four bits. Alternation makes the fixed exterior degree two at each cycle vertex, so the full toggle negates every degree deviation and preserves D on all sixteen states. S therefore commutes with H and exchanges the two ice basis vectors up to phases.

The spectral projection and canonical direct rotation are covariant under this symmetry; their effective two-by-two Hamiltonian consequently has equal diagonal entries. Each diagonal is one half of the low-band trace. We use the contour identity divided by two, not a nondegenerate recurrence on one member. The actual sixteen-state commutation and energy symmetry are explicitly checked. Nonalternating cycles have rank-one ice and use the feedback recurrence.

## Support extraction and complete local output

Inclusion-exclusion over all nonempty edge subsets isolates the terms containing every active edge. At total degree eight four-edge supported diagonal terms use each edge twice, because physical Z conjugation makes each diagonal even in each coupling. For smaller subsets the table retains the sum of all their degree-eight monomials at unit magnitude. Vertex-disconnected supports factor, and the disconnected two-edge inclusion-exclusion control vanishes.

RESULT.json contains every bit pattern for one edge, pair, three-star, three-path, four-star, four-path, fork and cycle, together with all lower even coefficients and the connected eighth coefficient. Some locally listed patterns (for example four equal bits at a degree-three ice vertex) cannot have an exterior ice completion. They are explicitly a superset of physical inputs; no such row may be assigned a global embedding without an admissibility filter.

Selected connected coefficients are: one edge 5/128; pair 35/64; three-star45/32; four-star15/16. Paths and forks are nonconstant. Four-cycle classes are all-equal1759/4800, one-or-three occupied2827/7200, two adjacent167/432, alternating25/32. All cycle orientations, complements and rotations are present in the raw table.

## Scope and remaining reduction

These are local canonical diagonal coefficients, not yet a global potential theorem. The complete global sum needs exact embedding counts and ice identities for all forests as well as cycles. A configuration-dependent cycle table alone does not imply a flippability potential; sixth-order path coefficients already provide a counterexample to that inference. Extent-four winding cycles must be counted alongside plaquettes. Root supplied a prospective nonbacktracking-walk reduction idea after this calculation began; no global identity from that idea is assumed here.

Actual adverse checks distinguish omission of feedback, division by the wrong cycle rank, and replacement of native phases by bare X. They are direct alternative calculations with explicit failure-of-equality predicates, not subprocess mutation claims. The 591 predicates ran in under one second and used less than20MiB. This is a finite exact mechanism calculation, not a phase, RK tuning or physical selection result.
