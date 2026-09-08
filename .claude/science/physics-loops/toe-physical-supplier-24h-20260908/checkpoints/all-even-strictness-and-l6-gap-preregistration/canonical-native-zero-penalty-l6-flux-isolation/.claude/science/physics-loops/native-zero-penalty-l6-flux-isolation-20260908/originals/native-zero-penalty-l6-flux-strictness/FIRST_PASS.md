# L6 strictness: bounded first-pass result

No all-flux uniqueness or gap proof obtained. The simple alternative-winding degeneracy candidate is ruled out exactly, but noncanonical plaquette flux sectors remain unresolved. No random flux sample or expensive enumeration was used.

Source inspection: read the retained flux-selection derivation and the primary Macris–Nachtergaele paper https://arxiv.org/html/cond-mat/9604043, Theorem1.4 and Section2 through Lemma2.2's proof. Their text explicitly leaves uniqueness unstudied. The reflection inequality proves existence of a canonical minimizer; it does not state strictness when a crossed circuit is noncanonical. A minimizer saturates the reflection inequality, but inferring its crossed fluxes from saturation needs an additional equality theorem. The cited general matrix lemma alone is not strict (even scalar A,B saturate it). This is a limitation of this attempted route, not a counterexample on the cubic graph.

Independent L6 check: for the canonical winding sign, each axis has sin² momenta1/4 with multiplicity4 and1 with multiplicity2. Thus the physical native energy at |g lambda|=1 is exactly

E_pi = -72 -40sqrt3 -48sqrt6.

The eight flat pi-plaquette sectors are exhausted by the three winding signs. Reversing an axis winding gives sin² values0 with multiplicity2 and3/4 with multiplicity4. check.py sums all216 momentum values by exact multiplicities and bounds every radical outward by rationals with denominator10^30. Each of the other seven sectors is strictly above the canonical sector. This excludes that concrete constructive degeneracy route only. It is not a test of the exponentially many non-flat plaquette assignments.

The L4 isolation proof cannot simply be reused: at L6 the canonical squared active frequencies are12,24,36,48, with multiplicities64,96,48,8. Their mean is24 but they are not constant. The universal trace-square/Jensen native lower bound is -108sqrt6, strictly BELOW E_pi by 60sqrt6-40sqrt3-72>0. Therefore proving a wrong flux has nonzero variance around24 does not separate it from E_pi; the canonical state itself has such variance. The constant-square equality characterization was genuinely special to L4.

A concrete remaining proof target is strictness of the reflection step on this finite connected free-fermion graph: saturation for a minimizing phase assignment must force canonical crossed flux, or at least force gauge equivalence after a finite sequence of reflections without losing original flux information. A possible route would derive equality in the underlying matrix Cauchy–Schwarz argument and prove the required faithful/full-rank intertwiner for the appropriate half-system ground-state Schmidt matrix. Neither faithfulness for arbitrary flux nor the equality-to-gauge implication has been established here. Zero-mode and entanglement-rank exceptions must be handled, not assumed away.

This first pass provides exact winding exclusions and an explicit quantified obstruction to the old Jensen route. It does not provide a new theorem import, a general no-go, a flux-gap estimate, or evidence that uniqueness is false. Extending the successful L4 weak-penalty theorem to L6 still requires this genuine missing isolation step.
