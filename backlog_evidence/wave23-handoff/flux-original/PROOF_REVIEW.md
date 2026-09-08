# Independent proof and domain review: #7874 / #7878

This is an original review of the unchanged six selected bodies at tree `d00764f7a1fb71c41e45a07b430cee0a8c9eed2e`. It supports a changes-required handoff, not an applied audit or a corrected-source acceptance. The calculations below use disjoint constructions where stated. The actual source prefixes and whole-source mutants are identified separately.

## Graph, gauge, parity and supplied physical interpretation

On a connected finite graph a site-sign gauge acts by `M -> D M D`. Its effective group has size `2^(V-1)` because the constant sign acts trivially. On the open contractible cube, face holonomies subject to their one product relation classify the `2^(12-8+1)=32` gauge classes. The original4096-field enumeration is consistent with128 representatives per class. On the named connected tori, admissible face data leave three independent Wilson signs, hence eight gauge classes/twist representatives, each still containing `2^(V-1)` literal sign fields. A face pattern alone is not a literal field. Equal face data on an open block give a diagonal sign conjugacy, not necessarily a site permutation; the source's “site relabelling” wording should be made precise.

For the specified edge carrier `B_i=prod_(e incident i) Z_e`, every edge appears twice in `prod_i B_i`; therefore that product is the identity. With the stated occupation interpretation `B_i=1-2n_i`, the carrier requires `(-1)^N=1`. On the cube, five independent loop constraints on twelve edge qubits leave dimension `2^7=128`, exactly the even part of an eight-mode Fock space; the full Fock space has dimension256. `ACTUAL_PREFIX_CONTROLS.json` computes the star-product bitmask from the original `Lat` class. The original odd-N one-particle/Fock ladder remains a valid mathematical construction, but it is not an odd-particle state of that unextended edge carrier. No spectator, extra site or new axiom was supplied to remove the constraint.

A27-site open bipartite graph has no integer `N=V/2`. The code's `N=V//2` evaluates13; particle-hole spectral pairing gives the mirrored14 result. This is a nearest-integer filling, not an exact half-filled27-site state. Similar floor labels must be distinguished from exact quarter filling.

The Hamiltonians, hopping scale, flux labels, fixed occupation number, ground-state choice and any occupation/Born readout are declared finite model inputs. The current minimal axioms do not imply them. On a two-site one-particle subspace `H=-(|10><01|+|01><10|)`, `[H,n_0]` is nonzero, while `[H,n_0+n_1]=0`. Thus the density interaction and total number conservation do not make full hopping preserve each permanent local Record. A conserved flux block plus an energy comparison also supplies no dynamics that moves a physical state between flux sectors. The free off-half-filled cube directly shows why “the uniform minus field is cheapest above about one third” cannot be a global all-field statement: at N=3, a four-flux class is below both uniform fields.

The current composition-discriminator note at main is different from the recovered historical quote. Its entire269-line current body was read for this boundary. It explicitly declares a chosen subfamily; on irregular open graphs a permitted degree-weighted diagonal term need not be constant. It normalizes nonzero hopping by `|t|`, excludes the diagonal `t=0` limit, and leaves ground-state/Born and occupation-to-Record bridges open. This review does not accept its parent campaign anew. The selected interaction is locally redeclared, so it can be retained without importing that campaign, but the old quote cannot silently override these current limitations.

## Free finite positive certificates

For every real signed nearest-neighbour matrix on the4³ torus, bipartiteness pairs the64 eigenvalues as `+/-lambda_j`, `j=1,...,32`. Counting edges gives `tr M²=384`, so `sum_j lambda_j²=192`. At half filling,

`E_32=-sum_j |lambda_j| >= -sqrt(32*192)=-32 sqrt(6)`.

Equality holds exactly when all magnitudes are `sqrt(6)`, equivalently `M²=6I`. The original checker verifies that integer identity for the all-minus field with the optimal all-antiperiodic twist. An independent coordinate construction reproduces it. The actual source mutation flipping one symmetric matrix bond breaks D3 and yields18/1, exit1. This is a real global certificate for that finite supplied free problem, not a random-search inference or an interacting/thermodynamic theorem.

The cube has `tr M²=24` and four paired magnitudes, giving `E_4 >= -sqrt(4*12)=-4sqrt(3)`. The all-minus matrix has `M²=3I`. Equality requires all off-diagonal entries of `M²` to vanish. For the two opposite vertices of a cube face, the two length-two paths cancel precisely when that face holonomy is minus. Thus equality forces every face minus, proving the unique gauge-class minimum at N=4. This short proof is stronger than merely printing a tolerance-based margin and can be used for a narrow repair.

`additional_controls.py` separately enumerates all32 fundamental-cycle classes using binary-coordinate vertices and a different spanning-tree construction. It saves exact characteristic polynomials and floating ladders. It reproduces the original tie counts `32,1,3,12,1,12,3,1,32`; the N=2/6 class has three minimizing members and N=3/5 has twelve. The original numerical enumeration is sound evidence, but calling all32 ladders “exact” or these non-half-filled minimizing sectors individually unique is inaccurate. The exact original integer minimal-polynomial and power-trace argument for the periodic4³ uniform spectra was fully inspected: its roots, symmetry and traces determine the multiplicities. The same exact label does not apply to every larger finite window.

No counterexample was found to the actual finite Wilson comparisons or the declared seeded random, structured and greedy runs. Those complete comparisons and searches have different meanings. The500 Wilson-minimized reevaluations are a subsample of the2000 original random fields. Failure to beat a field does not certify other lattices or volumes. Missing the common trace lower bound also does not itself prove that a better field exists.

## Interacting fixed-N matrices and the false all-g branch

The complete original `Sector` implementation was read: ordered bit-pattern basis, Jordan-Wigner hop signs, fixed-N sparse structure, exact integer dense matrices, density diagonal, sparse lowest levels and degeneracy handling. The independent construction uses binary-integer vertices and the exterior-product sign given by occupied indices strictly between endpoints. It does not import the candidate's matrix helpers.

For the cube with N=2, the independent full symbolic characteristic polynomials are

```
plain:
x^4 (x-g)^3 (x²-gx-4)^6 (x³-gx²-16x+8g)^3

minus:
x^6 (x-g)^7 (x²-12) (x²-gx-12)^2 (x³-gx²-12x+4g)^3.
```

A constant factor gives an eigenvalue, not necessarily the lowest eigenvalue. At `g=-4`, the minus quadratic is `(x-2)(x+6)`. The actual original source definitions, evaluated independently of their check groups, give the exact ground root `-6`; the plain ground is approximately `-5.806423851823107`. This directly refutes the original `-2sqrt(3)` assertion at every g.

For `g>=0`, the interaction diagonal is positive semidefinite, so the minus ground cannot fall below its g=0 value. The persistent factor supplies that value at every such g. This proves the constant branch in the repulsive domain. For `g<0`, let

`r=(g-sqrt(g²+48))/2`.

Then `r<g<0` and `r<-sqrt(12)`. It is the lower quadratic root. For the remaining minus cubic `f(x)=x³-gx²-12x+4g`, `f(r)=4g<0`. On `x<=r`, `f'(x)>0`, since `r<g<g/3` and `f'(r)=gr+24>0`. Consequently that cubic has no root below r; the constant roots, zero and g are also above r. Thus r is the attractive-domain ground branch.

There is an additional exact ground equality at `g=-sqrt(6)`, `x=-2sqrt(6)`. At that coupling the plain cubic factors as

`(x+2sqrt(6))(x²-sqrt(6)x-4)`.

Its other roots, the plain quadratic roots, g and zero are all higher than `-2sqrt(6)`. The minus branch above gives the same value. The repulsive equality at `g=2sqrt(3)` survives. The repair may present the narrow repulsive theorem and a disclosed attractive counterexample, or carry the full justified piecewise statement; it must not retain the factor-only inference.

The actual full-source mutant building the minus symbolic matrix with `-g` retains the free factor and still exits18/0. B2 must bind the g-dependent polynomial and the lowest-root interpretation. Its historical passing receipt is preserved as a false negative.

The original exact cube comparison at twelve integer couplings takes the actual least real roots of the full70-dimensional characteristic polynomials; that exact two-uniform comparison is legitimate. It is separate from the all32-sector nine-point computation. Likewise the all512 block arrays are complete only at the named sampled couplings. Fifteen points cannot prove no crossing on an interval. A change of optimality between -2.4 and -2.3 implies at least one crossing by continuity of the finite lowest eigenvalues; it does not prove uniqueness or behavior at every more attractive g.

## First-order and second-order torus calculations

An independent4³ coordinate construction gives the all-antiperiodic minus identity `M²=6I` and the stronger plain identity `M⁴-20M²+36I=0`. The latter implies the original sixth-degree annihilator. Polynomial occupied projectors agree with diagonalized projectors to below6e-16. Wick's finite Slater determinant formula on bonds then gives exactly the original rational values `A(+)=42` and `A(-)=40`; the free energy difference is `48sqrt(2)-32sqrt(6)`. Consequently the first-order polynomial crossing `24sqrt(2)-16sqrt(6)` is a correct algebraic statement about that first-order truncation. It is not automatically an actual interacting crossing.

The second-order check was reconstructed using unordered occupied and unoccupied pairs, not the source's four-index1/4 implementation. With 32 occupied and32 virtual orbitals there are496 pairs of each. For bond `(u,v)`, form the two-orbital wedge `C_ui C_vj-C_vi C_uj`; the interaction amplitude is the bondwise inner product of occupied and virtual wedges. Summing its squared magnitude divided by `epsilon_i+epsilon_j-epsilon_a-epsilon_b` gives

```
C2(+) = -1.8076798162013128
C2(-) = -1.3608276348795436
DeltaC2 = 0.4468521813217692.
```

The independent single-excitation amplitudes at these references vanish to below2e-15, consistent with the translational/gauge structure; the double-excitation formula does not omit a nonzero singles term here. This confirms the original numerical coefficient. But the source only checks a broad root interval and accepts0.25→0.253 in its actual prefactor. The resulting changed coefficient and root still print18/0. A precise retained numerical coefficient needs a meaningful actual assertion.

The torus has64 sites and N=32. The separately solved open8- and12-site systems cannot refute its second-order positive root. Without a same-system remainder bound or interacting calculation, that root remains an uncontrolled extrapolation of the truncation; the contrasting clusters are useful caution only. No large torus interacting calculation was run or required by this review.

## Strong coupling, finite Neel observables and operator attribution

The original g=4 cube rows have different `m²` and weights on the two checkerboard configurations despite equal one-site means. The complete finite arrays are retained. Equality of marginal means is insufficient for equality of joint distributions or of the normalized ground-space projectors. A finite nonzero-hopping ground state does not literally freeze into a classical configuration. The classical two-state subspace at infinite repulsion must be distinguished from finite exact degeneracy and physical SSB or permanent Record formation.

A disjoint exact cube derivation explains both the correct leading energy coefficient and the missing operator term. Write `H=gD+T`, let P project onto the two zero-density-cost checkerboard configurations (binary patterns105 and150), and Q onto all other N=4 configurations. Every Q diagonal entry of D is positive. Set `R=(D_Q)^-1`, `U=T_PQ` and `B=T_QQ`. For epsilon=1/g, Feshbach reduction of `D+epsilon T` gives

```
K2 = -U R U^T
K3 =  U R B R U^T
K4 = -U R B R B R U^T + 6 U R² U^T,
```

where the last term uses the computed scalar `K2=-6I`. Both sectors give `K3=0`. Exact rational arithmetic gives

```
K4(+) = [[17/2, 13/2], [13/2, 17/2]], eigenvalues2,15
K4(-) = [[-7/2, -43/2], [-43/2, -7/2]], eigenvalues-25,18.
```

Finite-dimensional analytic perturbation with the g-independent gap of D_Q justifies the asymptotic expansion as positive g tends to infinity. The lower K4 eigenvalues therefore give the energy difference `-27/g³` at leading order, restoring `t^4/V³` for positive t normalization. This does not derive an all-g result.

Crucially, the diagonal difference is -12; the difference in the downward tunnelling shifts is -15. The off-diagonal matrix element connects the two checkerboards, each with four particles moving to the other sublattice. Four-hop plaquette circulation returning to the same configuration cannot alone account for that tunnelling. The complete ground-energy difference is not established by assigning the scalar9/4 to each of the six faces. A repair can retain the exact energy theorem using the full effective matrices, or simply narrow the original fit to a numerical observation. This independent derivation is a review control, not an automatic candidate source change or acceptance.

On the2x2x3 block no exact rational coefficient was derived by this review. The original five double-precision values near-11.853 and the proposed-320/27 remain numerical trend and rational guess respectively. Four high-precision cube samples do not themselves prove the asymptotic remainder or a general ring-exchange operator. The original AMAT fits four basis terms to four samples; its precision is arithmetic precision, not an extrapolation error certificate.

## Bloch integrals and finite-volume precision

The continuous bounded dispersions give Riemann-integrable half-filled energy functions. That establishes the corresponding integral limits; it does not establish the last decimal of a numerical quadrature or a unique limiting filling crossing. As a disjoint diagnostic, the third momentum can be integrated analytically. For the plain field, conditional on `s=cos q1+cos q2`, the average of `|s+cos q3|` is `|s|` for `|s|>=1` and `2/pi*(sqrt(1-s²)+s asin(s))` otherwise. For the minus dispersion, with `a=6+2(cos q1+cos q2)`, the square-root integral is expressed using the complete elliptic integral `E(4/(a+2))`. The resulting two-dimensional quadratures at192/384/768 points agree with the original half-filled values, while visibly leaving numerical approximation error, especially in the plain integrand.

The original n* is instead obtained from an L=96 finite ladder by linear interpolation. The sequence is not a proof that0.339659 is the thermodynamic threshold. An actual injected1e-5 shift passes F3, despite the1e-9 label and six printed decimals. The repair should bind that finite interpolation honestly and leave continuum crossing uniqueness/error bounds open. No larger grid or production campaign was run.

## Premise/publication and review limits

Actual filename-derived primary IDs and both actual helper consumers were used. Helpers are zero for both and this is correct. Runtime contains no local imports or data reads. Semantic proof/publication closure nevertheless includes each own note and the actually used current authority; these are not declared, so eight real cache-note/memo drift/removal probes remain fresh. The current corrected composition boundary and historical quote identity must be distinguished before deciding which sources remain load-bearing. No mutually recursive note fingerprint or unrelated parent source is justified simply by membership in this review group.

Current main's axiom memo is identical to the raw parent's memo; no removed scalar-Record axiom is being adopted. The historical and corrected composition-note bytes differ and are explicitly bound. The off-main face-transport source is recovered only for attribution and boundary context. No reserved source intersection exists, no unselected parent campaign was executed or accepted, and no generated audit state or manifest was built. The inaccurate Lieb background is documented separately from the primary bibliographic source and does not supply a candidate theorem.
