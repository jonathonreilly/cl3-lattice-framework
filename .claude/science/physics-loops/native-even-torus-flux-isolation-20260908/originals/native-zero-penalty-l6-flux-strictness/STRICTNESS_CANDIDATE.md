# Candidate complete finite L6 uniqueness proof — independent review required

This continues the failed first-pass equality route rather than replacing its history. Inputs are the established finite L6 canonical dispersion and Macris–Nachtergaele reflection transformations/monotone canonical-circuit algorithm. New ingredients below are a strict equality lemma, boundary rigidity and an exact algebraic Schmidt-rank certificate. No physical coefficient or flux enumeration is used. The conclusion is unique minimizing Z2 flux orbit for uniform6x6x6, contingent on cold verification of these new arguments; no quantitative flux gap is calculated.

## 1. Equality lemma with a faithful reflected child

In the reflection tensor coordinates write H=A⊗I+I⊗B−sum C_mu⊗C_mu, where A,B are Hermitian and the C_mu are real. In the hopping application the channels include positive multiples of each boundary annihilator and creator; paired transpose channels make H Hermitian. Vectorize a normalized ground vector as matrix X=U Sigma V†. Set Y=U Sigma U† and Z=V Sigma V†. They have the same norm. Direct expansion gives

E_H(X)−[E_(A,bar A)(Y)+E_(bar B,B)(Z)]/2
 = (1/2) sum_mu || Sigma^(1/2)(U† C_mu U−V† C_mu V) Sigma^(1/2) ||_HS².

The A/B contributions cancel by cyclic trace. For the channels, the original term is Re Tr(Sigma A_mu Sigma B_mu†); the two reflected terms are the respective weighted squared norms. This identity proves the inequality and explicitly records its equality conditions. It does not assume a strictly positive hopping matrix in the many-body occupation basis.

Suppose H and its two reflected children are all minimizers of the same optimization problem, so their lowest energies equal E*. If ONE reflected child has unique ground with full Schmidt rank, equality forces its corresponding Y or Z to be that ground matrix up to phase and hence Sigma invertible. Every square above then vanishes. Therefore R=U V† commutes with every C_mu. If the right child is the faithful one, the original eigenmatrix equation and the right-child equation, after multiplying by R† and subtracting, give

(R† A R−bar B) Z=0,

hence R† A R=bar B. The left-child case is symmetric. Thus the original is equivalent to that child by a half-system unitary that fixes every boundary annihilator and creator. Faithfulness is used twice: in the equality squares and to cancel Z. Degenerate or rank-deficient children are not covered by this lemma.

## 2. Boundary-fixed equivalence forces a gauge on the three-layer half

The L6 coordinate half is three layers, with its two outer layers forming the reflection boundary. Let A and C=bar B be number-conserving hopping quadratics with identical graph and nonzero equal edge magnitudes, and R† A R=C with R fixing every boundary annihilator. The double CAR commutator with two boundary modes determines their hopping matrix element; therefore A and C coincide on boundary-boundary edges.

For each boundary site x there is exactly one neighbor y not in the boundary (the corresponding middle-layer site). Subtract the now-identical boundary contributions in the commutator of A with c_x and its R-conjugate. It follows that R† c_y R is a scalar phase times c_y, with phase the ratio of the two inward hopping amplitudes. The second boundary layer imposes the same phase by consistency. Thus all annihilators transform by site phases: boundary phases1, middle phases of modulus1. Since the CAR representation is irreducible, R differs from this gauge implementer only by a scalar. Therefore the original whole hopping configuration is gauge equivalent to the reflected child; cross-plane bonds remain unchanged because R fixes boundary modes. This is a concrete three-layer argument, not a general controllability assumption.

The MN parity/Jordan-Wigner tensor convention uses different but real CAR generators within each half. These are related to the usual half Fock representation by a local unitary, so the CAR commutator argument and Schmidt rank are unaffected. Right particle-hole and gauge transformations are also local to the half. The proof concerns the auxiliary full-Fock half-filled hopping ground, whose objective equals twice the native energy; no spectator degeneracy is incorrectly assigned to that auxiliary ground.

## 3. Canonical child is unique and faithful

Canonical L6 K has no zero eigenvalues by the proved dispersion. Hence the auxiliary full-Fock hopping ground is the unique Slater state filling all negative one-particle modes. Its correlation projector is P_-=(I−iK(-K²)^(-1/2))/2. For a pure Slater state, full Schmidt rank across equal halves is equivalent to every eigenvalue of its restricted correlation matrix lying strictly between0 and1. The projector identity says C_L(1−C_L)=P_LR P_RL. Thus it suffices that the108x108 cross block P_LR is invertible. This criterion follows directly by diagonalizing the restricted correlation matrix into independent occupied/unoccupied entangled mode pairs.

The exact spectrum of A=-K² is {12,24,36,48}. Interpolate A^-1/2 by a polynomial of degree3 at these four values. Its coefficients lie in Q(sqrt2,sqrt3), with the positive square roots2sqrt3,2sqrt6,6,4sqrt3. schmidt_check.py constructs the actual216x216 integer K including canonical seams. Reduce the coefficient ring modulo97 with sqrt2→14 and sqrt3→10; both square relations hold and all interpolation denominators are nonzero. It computes the determinant of the cross block K A^-1/2 as88 mod97. Therefore its exact algebraic determinant is nonzero: if the exact determinant vanished, its well-defined reduction would vanish. Multiplication by −i/2 does not change rank. This is an exact finite rank certificate, not a floating diagonalization. Integer intermediate bounds are tiny compared with int64; matrices are reduced modulo97 between products.

The canonical flux is invariant up to gauge under translations and coordinate permutations. These give all coordinate half-torus cuts from the checked cut, preserving Schmidt rank. Gauge equivalence of any later child to the canonical configuration similarly preserves faithfulness for each such cut. All claims here are specific to the uniform L6 graph.

## 4. Backward propagation along the reflection algorithm

Start with ANY minimizing flux assignment. The MN circuit-count argument gives a finite sequence of minimizing reflected children, strictly increasing the number of canonical basic circuits at each chosen step, ending in the canonical flux assignment. At the final step, the chosen child is canonical, unique and faithful across that reflection cut. Sections1–2 force its parent gauge equivalent to it. Induct backward: each chosen child is then gauge equivalent to the canonical configuration and therefore unique and faithful across the preceding cut. Each parent is gauge equivalent to it. The original minimizer is canonical up to gauge.

This proves strict uniqueness of the minimizing orbit if the equality and tensor-convention details survive independent review. Restricting from arbitrary phases to Z2 is harmless; the argument actually starts from a Z2 minimizer, which is also a global phase minimizer because canonical phases lie in Z2. Since the finite Z2 orbit set is finite, uniqueness implies an EXISTENTIAL positive flux-sector energy separation at fixed nonzero uniform hopping. No numerical lower bound on that separation follows from this argument. This would close finite L6 isolation, but does not imply an infinite-volume flux gap or uniqueness on arbitrary even extents.

Primary source used: Macris and Nachtergaele, cond-mat/9604043, Section2 reflection representation and finite circuit-count iteration. Their paper does not claim uniqueness; the equality/faithfulness/backward argument here is additional and requires its own review. The earlier FIRST_PASS.md remains accurate as a record before these steps were developed.
