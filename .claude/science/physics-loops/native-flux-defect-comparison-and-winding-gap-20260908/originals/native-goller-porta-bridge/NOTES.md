# Goller–Porta bridge assessment

Status: source review and prospective three-dimensional derivation, not an imported three-dimensional defect theorem. No coefficient scan or stochastic work was run. The separate L6 all-prefix package remains frozen and unlaunched.

## Primary source: scope actually read

[Goller and Porta, Journal of Statistical Physics 193, 60 (2026)](https://link.springer.com/article/10.1007/s10955-026-03617-y), DOI 10.1007/s10955-026-03617-y. Read the model, Gauss reduction, Definition 2.11, Theorem 2.12 and remarks, Proposition 3.7 statement, and the chessboard argument around Proposition 3.10 plus Proposition 3.12's periodic-spectrum construction. The winding proof and susceptibility section were not read completely.

Their theorem concerns square tori L divisible by four, half filling, zero electric coupling, and sufficiently large hopping against a supplied magnetic plaquette term. Their defect estimate reduces arbitrary flux costs to a periodic mixed-flux free energy. Its positive limiting cost is two-dimensional. Four winding sectors have energy differences tending to zero; strict finite-volume uniqueness is not asserted by that estimate. Definition 2.11's plus trace is full Fock and its minus trace has parity insertion: neither is itself a parity-sector trace. The Gauss projection combines them. No three-dimensional defect-cost or nonzero-electric stability theorem is supplied here.

## Exact bridge bookkeeping from our existing endpoint proof

The source for these identities is our complete local `native-zero-penalty-flux-selection-root/DERIVATION.md`, reread for this assessment, together with `native-zero-penalty-pi-dispersion/DERIVATION.md`.

For N native vertices, the separate auxiliary full-Fock problem obeys

    E_aux(xi) = 2 E_native(xi),
    Z_native(beta,xi)^2 = 2^(N-2) Z_aux(beta,xi).

Thus any newly proved auxiliary fixed-flux free-energy difference transfers with factor one half, at the same beta. Do not project the auxiliary trace to even particle number: the native physical parity and spectator multiplicities have already produced the displayed identity. This is equality of objectives, not equality of Hilbert spaces or response observables.

The auxiliary hopping magnitude is 2|g lambda|. Its imaginary canonical-edge phase can be changed to a real bipartite hopping representation, but the seam/winding phases must change with that basis transformation. A two-dimensional numerical defect coefficient cannot simply be multiplied by this hopping scale and called a cubic bound. Our U=0 endpoint also lacks the magnetic plaquette term used in the source model. Our U D perturbation is a degree-square electric interaction, not the paper's single-link electric operator. Neither the source's magnetic susceptibility nor its fermion interpretation transfers through the equality of partition objectives.

## Three-dimensional obstruction to copying the proof literally

For link signs on a cubic torus the product of the six plaquette signs around every cube is +1. Relative to the all-minus plaquette background, defects therefore have even incidence at each dual vertex: they form closed dual subgraphs. A single independently assigned defective plaquette is inadmissible. This is an exact algebraic constraint, not a small correction to the two-dimensional counting argument.

Reflection on link variables preserves this constraint automatically. Reflection on an arbitrarily specified collection of face signs need not. A valid extension must disseminate compatible link blocks, retain all three winding labels, and establish the multiplicity with which the original defective faces enter the final inequality. Evaluating a periodic comparison spectrum alone does not establish that inequality.

There is no contradiction between a positive cost per defective face and winding splittings tending to zero: winding changes can have no defective elementary faces at all. The former cannot provide a uniform gap separating every noncanonical flux orbit. Our finite strictness work and the all-prefix certificates address different obligations.

## A concrete compatible comparison family, not yet a chessboard bound

For extents divisible by four, define directed real link signs using integer coordinates:

    phi_xy(x,y) = +1 if x,y are both odd, and -1 otherwise;
    s_x(x,y,z) = 1;
    s_y(x,y,z) = product_{r=0}^{x-1} phi_xy(r,y);
    s_z(x,y,z) = (-1)^(x+y).

These signs are periodic. Their xy plaquettes are phi_xy and every xz/yz plaquette is -1. Defects form straight dual loops in the z direction. Their density is one quarter of xy faces, or one twelfth of all faces. This is a feasible test family; it has NOT been shown to be the dissemination of an arbitrary three-dimensional defect.

For real hopping in this family, write the planar bipartite hopping as h_xy and Gamma_xy=(-1)^(x+y). The vertical hopping is Gamma_xy times a one-dimensional nearest-neighbor hopping h_z. Since {h_xy,Gamma_xy}=0 and the factors act on separate coordinates,

    h_3 = h_xy tensor I + Gamma_xy tensor h_z,
    h_3^2 = h_xy^2 tensor I + I tensor h_z^2.

This gives an exact finite block-spectrum reduction, including separately chosen seam twists. It does not by itself prove positive defect cost: a difference of sums of sqrt(squared_frequency + mass_squared) needs its own comparison. Positivity of the massless planar difference alone is insufficient for that step.

## Highest-value bounded next derivation

First prove a link-level three-dimensional chessboard inequality for compatible 2-by-2-by-2 blocks. Track all eight translated block partitions, all face types, and winding optimization explicitly. List the finite disseminated link patterns up to gauge and cubic symmetry. The success criterion is an inequality assigning a nonzero fixed weight to every original defective face, with no inadmissible face assignment or missing winding sector. A failure to obtain that weight is an exact remaining premise, not a universal obstruction.

Only after that succeeds, derive the Bloch matrices of the actual disseminated patterns and certify a strictly positive energy-density difference from the canonical background. Use exact matrix coefficients and outward interval bounds for the Brillouin-zone integral and finite-size remainder; ordinary numerical band plots do not certify it. The stacked family above is a useful algebra/control case, not a substitute for the full list. Initially restrict extents to multiples of four; extending to L=6 or all even sizes is a separate boundary task.

The desired final result would be an auxiliary lower bound proportional to the number of defective plaquettes, then half that bound for native fixed-flux objectives. It would improve quantitative robustness to local magnetic defects. It would not select the supplied Hamiltonian, establish a three-dimensional phase, control U D, remove spectator degeneracy, or give a uniform winding gap.
