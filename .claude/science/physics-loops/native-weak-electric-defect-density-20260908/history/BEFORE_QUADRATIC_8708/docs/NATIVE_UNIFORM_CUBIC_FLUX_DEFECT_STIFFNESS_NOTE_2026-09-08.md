---
claim_id: native_uniform_cubic_flux_defect_stiffness_note_2026-09-08
claim_type: bounded_theorem
claim_scope: "Supplied uniform U=0 native model on cubic L=4M: conditional uniform local-flux defect stiffness and low-temperature native annealed joint-defect bounds. Complete certified density computation and independent exact replay establish positive comparison bounds. No phase, nonzero-U extension, Hamiltonian selection or uniform winding gap."
upstream_dependencies:
  - native_dynamical_cycle_fermion_z2_dictionary_note_2026-09-08
  - native_zero_penalty_endpoint_note_2026-09-08
  - native_zero_penalty_optimal_flux_dispersion_note_2026-09-08
  - native_even_torus_flux_isolation_note_2026-09-08
  - native_flux_defect_comparison_and_winding_gap_note_2026-09-08
runner: scripts/native_uniform_cubic_flux_defect_stiffness_2026_09_08.py
---

# Uniform cubic flux-defect stiffness for the supplied zero-penalty native model

**Date:** 2026-09-08  
**Type:** bounded_theorem  
**Status:** conditional-support; numerical premise discharged

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: "Supplied uniform U=0 native Hamiltonian and thermal ensemble, exact dictionary, reflection input, finite isolation; positive density premise discharged by the accepted complete exact certificate."
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

**Final theorem source: numerical premise discharged.** The accepted complete grid computation and independent exact replay establish d_*>=17/1000 and delta_inf>=3/50 at unit auxiliary hopping. The supplied U=0 model and the stated dictionary/reflection prerequisites remain conditional-support. Historical status sentences in the preserved proofs describe their original freezes and are not the current theorem status.

## Model, units, and scope

Use the supplied uniform zero-electric-penalty (U=0) native Hamiltonian, its physical Gauss support, and its exact active-Majorana/spectator dictionary. The nonzero auxiliary hopping magnitude is h=2|g lambda|. This Hamiltonian, its coupling, the thermal ensemble, and the readout are supplied model choices; they are not selected by the minimal axioms. The result concerns cubic periodic lattices L=4M, M a positive integer, N=L^3. It does not establish a nonzero-U continuation, a thermodynamic phase, confinement, a photon, or a gap between pure winding sectors.

The source prerequisites are [the full native dictionary](NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md), [the zero-penalty endpoint](NATIVE_ZERO_PENALTY_ENDPOINT_NOTE_2026-09-08.md), [canonical dispersion](NATIVE_ZERO_PENALTY_OPTIMAL_FLUX_DISPERSION_NOTE_2026-09-08.md), and [finite even-torus flux isolation](NATIVE_EVEN_TORUS_FLUX_ISOLATION_NOTE_2026-09-08.md). The [compatible dissemination and closing winding-gap theorem](NATIVE_FLUX_DEFECT_COMPARISON_AND_WINDING_GAP_NOTE_2026-09-08.md) supplies the block comparison and the distinction between local defects and pure winding changes. Finite strictness is a prerequisite, not a numerical inference from the grid.

## Theorem and accepted numerical premise

Let e_q be the infinite-volume auxiliary ground energy per vertex at unit hopping of the compatible period-four dissemination of cube label q. The 32 labels have six symmetry classes; the canonical label is q_pi and the other five classes have m(q)=2,2,4,4,6 defective internal faces. The numerical premise is

    d_* = min_(q != q_pi) (e_q-e_pi) > 0.

The complete fixed 24-job certificate covers 24,576 folded nodes, representing all 6*32^3 original nodes with multiplicity eight. All 24 independent exact replays and the independent aggregate passed. The accepted lower bounds are

    d_* >= 17/1000,   delta_inf = min_q 8(e_q-e_pi)/m(q) >= 3/50.

The [root acceptance receipt](../.claude/science/physics-loops/native-uniform-cubic-flux-defect-stiffness-20260908/evidence/accepted_numerics/ROOT_ACCEPTANCE.json), SHA-256 `0255f6edc4dc67e1ccb49ee724dedd1d37c6f0558b80ed1f26ec5cea01846df8`, binds the complete run, all independent phase receipts and [exact five-comparison analysis](../.claude/science/physics-loops/native-uniform-cubic-flux-defect-stiffness-20260908/evidence/accepted_numerics/ANALYSIS.json). Raw candidates are retained in the packet's RAW_CANDIDATES manifest and streams. Total charged time was 1024.06 seconds within 3600 seconds; maximum observed process-tree memory was 188,841,984 bytes within 384 MiB. These resource checks establish run completion, not an additional physical premise. Pilot estimates were not used as certificates.

With this certified premise, write d0=h*d_*. Uniformity of the semiconvex quadrature bound over all winding shifts gives

    d_(beta,L)(q) >= d0 - 3*h*pi^2/(8*M^2) - log(2)/beta.

For sufficiently large M and beta, the right side is at least d0/2. Compatible cube dissemination then gives, for k(s) defective elementary faces,

    F_native(s)-F_native(pi) >= kappa*k(s),   kappa >= d0/12

on that explicit large-size, low-temperature regime. The finite collection of smaller M has positive ground comparison gaps by finite isolation. Taking a smaller positive kappa and a larger finite beta threshold includes all cubic M existentially. This does not compute the small-size minimum, and it does not extend the argument to arbitrary aspect ratios with a fixed thin side.

The exact partition factors are

    Z_native=2^(N/2-1)*Z_active,  Z_aux=Z_active^2.

Thus native fixed-orbit free-energy differences are half the auxiliary differences; no second active parity restriction is imposed. At zero temperature the corresponding large-size bound can be sharpened, but the conservative finite-temperature coefficient above is the stated common normalization.

For B=N/8, the directly proved native annealed reflection-positive measure gives

    p=min(1,31*2^(11+1/B)*exp(-2*beta*kappa)),
    Prob(all prescribed m faces defective) <= p^(m/24).

Consequently, with a=36*p^(1/24)<1, the probability of a connected defective dual-edge set through a specified vertex with at least ell edges is at most a^ell/(1-a). These are unconditioned joint-event estimates. They neither assert independent defects nor compare arbitrary exterior-conditioned ensembles. Pure winding changes with no defective plaquettes have k=0 and are not penalized by this estimate.

## Explicit large-volume and low-temperature constants

Define delta_inf=min_q 8(e_q-e_pi)/m(q), distinct from d_*. The complete accepted certificate establishes delta_inf>=3/50. Therefore M>=32 and beta*h>=200 imply delta_beta,L/h>=3/100 and kappa>=3*h/800. Indeed the loss is at most 4*[3*pi^2/(8*M^2)+log(2)/(beta*h)]; pi^2<10 and log(2)<7/10 leave 4013/128000>3/100.

For beta*h>=14000, p<=31*4096*exp(-105). An exact rational Taylor lower bound through degree 200 proves exp(105)>48^24*31*4096. Therefore a<3/4 and the connected-set probability is at most min(1,4*(3/4)^ell). This explicit large-size corollary does not replace the separate existential small-size argument. The exact constant calculation is preserved in the packet. It is independent of the density computation; its premise is discharged by the accepted certificate above.

## Numerical certificate interface and coverage

The exact 64-to-16 reduction gives D=(C^2+3I) tensor I2 + sum_a q_a A_a tensor sigma_a, with q_a=2 sin(k_a/2), and e_q=-average Tr(sqrt(D))/32. The grid uses exact rational enclosures of q and pi. Arbitrary eigensolver candidates are certified by exact dyadic residual and Gram arithmetic: eta<=1/2 and radius delta=input_error+2*r+4*max|lambda|*eta. Rational square-root endpoints enclose every density contribution. The difference quadrature error is at most 3*pi^2/(8*32^2). The arithmetic candidates alone are not a theorem; full coverage, exact aggregation, independent replay, and positive lower bounds are supplied by the accepted records above.

## Full proof chain and historical qualifications

The following are complete preserved source proofs, with their original source hashes. The fourth part's statement that an annealed contour theorem was still missing is a historical boundary of that part alone; the fifth part supplies native trace positivity and its stated unconditioned consequence. No entrywise square-root positivity argument is used. Source status and source-path language are retained for provenance; the canonical premise status is the accepted status above.


---

## Full source proof: Compatible three-dimensional dissemination

Original source: `native-3d-chessboard-dissemination/DERIVATION.md`; SHA-256 `44877b2cd9733af18357c34ba4793453afe3bbecfb70083b9ca90320eaa3c6e7`.

# Compatible three-dimensional block dissemination

Status: candidate finite theorem for independent review. This is a new derivation, frozen before reading another agent's solution. The supplied uniform auxiliary hopping problem and its previously checked Macris–Nachtergaele reflection inequality are premises. No Bloch cost, coefficient scan, or physical production is performed.

## 1. Domain and reflection input

Let the three torus extents L_a be divisible by four and at least four. Set N=L_0 L_1 L_2 and B=N/8. Work with real nearest-neighbor hopping signs of common nonzero magnitude h=2|g lambda|, and the ground energy E(s) in the full complex Fock space at chemical potential zero. The native auxiliary matrix iK is gauge equivalent to such a real hopping problem because the graph is bipartite. Retain the resulting winding phases; do not replace canonical seams by periodic momentum conditions.

The only energy inequality imported is the already checked reflection inequality: for a coordinate cut between sites, the two reflected hopping configurations s_+,s_- satisfy

    E(s) >= [E(s_+)+E(s_-)]/2.

Each child retains the hopping in its chosen half, up to a site gauge, reflects that half, and makes elementary plaquettes crossing the cut canonical (real hopping product -1). Internal plaquette products are reflected without a sign change. Real signs remain real. Both opposite boundary planes are part of the cut. This is the finite full-Fock auxiliary inequality, not an even-parity auxiliary restriction.

The source bridge is Macris–Nachtergaele, https://arxiv.org/html/cond-mat/9604043, through the already reviewed native flux-selection argument. Goller–Porta, https://link.springer.com/article/10.1007/s10955-026-03617-y, Section 3.3 motivated the present block construction. Its two-dimensional defect theorem is not used as a three-dimensional theorem. The elementary finite minimization argument below is supplied explicitly.

## 2. Disjoint cubes make arbitrary labels compatible

Choose one of eight shifts p in {0,1}^3. Partition the vertices into disjoint cubes of 2x2x2 vertices, indexed by b in the block torus of extents n_a=L_a/2, all even. Each cube has twelve internal edges and six square faces. Its gauge class is its six face products q=(q_1,...,q_6), subject only to product q_i=+1: the cube cycle rank is 12-8+1=5. Thus the alphabet has exactly 32 labels. Define m(q) as the number of +1 faces; it is 0,2,4, or 6. The label q_pi with all six faces -1 is the only m=0 label.

Every independent assignment of these labels to disjoint cubes can be realized: choose internal edge representatives on each cube separately and assign arbitrary signs to the remaining edges. No vertex or internal edge belongs to two cubes. Therefore no inadmissible global face assignment has been introduced. Global Bianchi identities follow from the resulting link signs automatically; crossing faces were never independently prescribed.

Let F_p(q_b) be the minimum of E(s) over all link fields whose internal cube labels are the specified q_b. The minimum exists in a finite set. It includes all inter-cube edges and all winding choices. In particular E(s)>=F_p(q_b(s)).

A reflection through block boundaries sends a cube to another cube and acts on its six labels by rho_a, which exchanges the two faces normal to axis a and leaves the other four labels in place. The three rho_a commute and square to identity. Apply the energy reflection inequality to a minimizer defining F_p. The reflected children are admissible for the correspondingly reflected label assignments, so F_p itself satisfies the half-reflection inequality. Minimizing free cross links has weakened the inequality in the safe direction.

## 3. Elementary chessboard lemma, including the twist

Normalize labels by eta_b=(product_a rho_a^b_a)q_b. Because every n_a is even, this normalization is periodic. A reflection through a block boundary sends b_a to 2s-1-b_a, hence reverses its parity. Its physical rho_a cancels that parity change. Thus in eta coordinates each half reflection is ordinary reversal-and-copy of the chosen half of the block array, with no operation on the alphabet.

Here is the needed one-dimensional lemma. Let f on sequences of even length n over any finite alphabet obey the half-reflection inequality at every boundary. Put f_const(x)=f(x,...,x) and

    G(x_1,...,x_n)=f(x_1,...,x_n)-(1/n)sum_j f_const(x_j).

The subtracted mean has exact equality under the average of the two reflected children, since each original entry is copied twice into one child. Therefore G obeys the same inequality. Choose a minimizer of G with the longest cyclic run of one repeated letter. Both reflected children of any minimizer are again minimizers: each has G at least the minimum, while their average is at most it. If the longest run has length r<=n/2, choose a half interval ending at one end of the run and containing the run; reflecting it extends that run to at least 2r. If r>n/2, choose a half interval wholly inside it, producing a constant sequence. Unless the minimizer is already constant this contradicts maximal run length. At a constant sequence G=0. Hence G>=0 everywhere.

Apply this lemma to x-directed slabs of cube labels, treating an entire transverse slab as one alphabet letter. Then apply it in y within the x-constant arrays, and in z within the x,y-constant arrays. These restricted arrays remain invariant under the other axis reflections. No assumption of energy locality in the alphabet is used. The result is

    F_p(q_b) >= (1/B) sum_b Phi_L(eta_b),                 (1)

where Phi_L(q) is F_p evaluated on the physical reflected pattern q_b=(product_a rho_a^b_a)q. Translation and the finite graph isomorphism make the definition independent of p. A global rho_a changes the disseminated pattern by one block translation, so Phi_L(rho_a q)=Phi_L(q). In particular one can write eta_b or q_b in the sum.

## 4. The comparison minimum really reduces to periodic face patterns

Equation (1) initially defines Phi_L by minimizing arbitrary cross links. This section is needed before interpreting it as a finite Bloch comparison list.

Fix a disseminated internal label q and, among energy minimizers realizing those internal labels, choose one with the fewest noncanonical CROSSING faces. A crossing face is one not wholly internal to a cube. The disseminated internal label pattern is invariant under every block-boundary physical reflection. Thus both reflected children are in the same constrained family. By minimality of energy and the reflection inequality, both children also minimize energy.

Every crossing face not on the two reflection planes is retained in one half and copied twice in the corresponding child; every face on the planes is made canonical. Consequently the average number of noncanonical crossing faces in the children equals the original number minus the number of bad faces on the cut. If any crossing face were bad, choose a block-boundary cut crossing it. At least one energy-minimizing child has strictly fewer bad crossing faces, a contradiction. Therefore a minimizer has ALL crossing faces canonical.

Internal labels plus these crossing products specify every elementary face product. Two link fields with those products differ only by a site gauge and three winding signs, by the torus cycle-space argument already used in the parent dictionary. Thus Phi_L(q) is exactly the minimum over eight winding sectors of the reflected periodic face pattern, not a minimization over exponentially many arbitrary links.

This argument does not assume every reflected child lowers energy strictly, nor that a constrained minimizer is unique. The secondary integer minimization supplies the progress step.

## 5. Explicit compatible tiling and seams

An explicit representative verifies that the face pattern just described exists. Choose any cube edge representative a_(v,j), v in {0,1}^3 with v_j=0, for q. Let b_a=floor(r_a/2), and let f(r_a) be 0,1,1,0 for r_a modulo four. For a positive-axis bond based at r define real hopping signs

    s_a(r)=(-1)^(b_0+b_1+b_2) a_(v,a),  r_a even,
       where v_c=f(r_c) for c!=a and v_a=0;
    s_a(r)=(-1)^(sum_{c>a} b_c),          r_a odd.

For a face whose two in-plane coordinates are even, its product is the corresponding internal cube product, with the remaining coordinate folded by f. Every other face has product -1. This follows directly: a face crossing one block boundary picks up one relative minus between the parallel internal bonds; a face crossing two boundaries picks up one minus from the ordered cross-bond factors. Hence all cube identities hold. This is link-level compatibility, not freely assigned face data.

The unmodified representative has straight winding (-1)^(L_a/4), not always canonical. A seam multiplier adjusts each winding independently without changing face products. In particular multiplying the a seam by (-1)^(L_a/4+1) makes every real hopping winding -1, the canonical value for L_a divisible by four. All eight alternatives remain in the Phi_L minimum. Omitting this adjustment on L_a=8 produces the wrong winding and is a genuine adverse case.

There are B copies of the internal six-face pattern, so the number of defective faces of a disseminated configuration is B m(q). There are 31 noncanonical cube labels, not a single two-dimensional comparison band.

## 6. Defect counting and exact remaining obligation

Let E_pi be the canonical auxiliary ground energy and define the finite comparison number

    delta_L = min_{q:m(q)>0} [Phi_L(q)-E_pi]/[B m(q)].     (2)

The canonical q_pi comparison equals E_pi. If the separately proved all-even strict-flux theorem is admitted, every other comparison has a defective elementary face and therefore strictly exceeds E_pi: delta_L>0 at each fixed volume. Without that theorem, (1) and (2) still hold as algebraic definitions, with no asserted sign. No numerical value or uniform lower bound is supplied here.

For each partition p, (1) gives

    E(s)-E_pi >= delta_L sum_b m(q_b(s)).

Each elementary face is internal to exactly two of the eight shifted cube partitions: its two in-plane parities fix two entries of p, and the third is free. It is counted once in each such partition. Averaging over p therefore proves

    E_aux(s)-E_aux,pi >= (delta_L/4) k(s),              (3)

where k(s) counts all noncanonical elementary faces. The native objective identity gives

    E_native(s)-E_native,pi >= (delta_L/8) k(s).        (4)

Here delta_L was defined from the auxiliary energies with hopping magnitude 2|g lambda|; it is not a coefficient imported from a planar model. Pure winding changes have k=0, so (3) does not assert a winding gap.

The substantive remaining task is to bound the 31 compatible comparison energy densities uniformly away from the canonical density, including finite-size corrections and winding minimization. The present reduction identifies a finite periodic list; it does NOT prove that its thermodynamic minimum is positive. A fixed-volume positive delta_L alone does not accomplish that. No Bloch integral, nonzero-electric stability, spectator splitting, phase claim, or axiom selection is inferred.

## Controls and timing exposure

The preregistration precedes the checker. The exact checker enumerates all 32 cube gauge classes and verifies the explicit tiling on 4x4x4, 4x8x4, and 8x8x8, including internal/crossing face products, every cube identity, winding correction, and defect multiplicity. It checks the eight-partition face count on two fixed geometries. These are finite geometry controls only; they do not test the reflection energy inequality or replace the all-size minimization proof. The first execution passed; no physical spectrum was computed.


---

## Full source proof: Exact Clifford reduction

Original source: `native-3d-bloch-clifford/DERIVATION.md`; SHA-256 `aa2ac5c326a11eb0eeab87d5f00c5bc67b636e056fae202e52f0858ee73ce631`.

# Exact64-to16 Bloch-square reduction and degree-eight algebra

This derivation was completed without reading the pending96-matrix pilot or its output. It applies to every one of the32 supplied cube-link representatives, hence the six reviewed density classes. Unit hopping and the reviewed real period-four tiling are retained. No new eigenvalue or integral computation is performed.

## Folded coordinates

Write r_a=2b_a+v_a with b_a,v_a in{0,1}, and y_a=f(r_a)=v_a xor b_a. Use cube coordinate y and block coordinate b, each an8-dimensional space. Let a_a(y_other) be the internal cube bond sign, diagonal and independent of y_a. Set

C=sum_a a_a(y_other) X_{y,a},
A_a=a_a(y_other) Y_{y,a},
Z_b=Z_{b,0}Z_{b,1}Z_{b,2}.

Internal hopping is C tensor Z_b. A crossing hop flips b_a while keeping y fixed. Its b_a matrix is X when y_a=1, and cos(k_a)X+sin(k_a)Y when y_a=0, multiplied by product_{c>a}Z_{b,c}. This follows directly from the positive-wrap exp(+ik) convention: for y_a=0 the b=1 to0 matrix entry is exp(+ik).

Call the crossing operators Q_a. They square to identity and anticommute pairwise, since their block Jordan-Wigner strings supply one minus sign; their y-dependent projectors commute across different axes. Hence (sum Q_a)^2=3I. In the mixed anticommutator only the same-axis internal term contributes. Using [X,Z]=-2iY gives the exact identity

h(k)^2=(C²+3I_8) tensor I_8 + sum_a A_a tensor Gamma_a(k),
Gamma_a=product_{c<a}Z_{b,c}[(cos k_a-1)Y_{b,a}-sin k_a X_{b,a}].

The Gamma matrices are Hermitian, mutually anticommute and satisfy Gamma_a²=q_a²I, q_a=2sin(k_a/2) on the zone[0,2pi]^3. For nonzero q_a, independent block-spin Z rotations turn the three normalized Gamma into the standard three Jordan-Wigner Clifford generators. Their8-dimensional representation contains the two inequivalent2-dimensional complex Clifford irreducibles, each twice: the central chirality has trace zero and eigenvalues plus/minus1 with multiplicity4.

Consequently h² is two copies each of D_plus and D_minus, where

D_plus(q)=(C²+3I_8) tensor I_2 + sum_a q_a A_a tensor sigma_a,
D_minus(q)=(C²+3I_8) tensor I_2 - sum_a q_a A_a tensor sigma_a,

and sigma_a=(X,Y,Z). Cube parity P_y=product Z_{y,a} commutes with C² and anticommutes with every A_a, so conjugation by P_y exchanges D_plus and D_minus. Thus h² has precisely FOUR copies of the16-dimensional D=D_plus. Degenerate q_a=0 cases follow by continuity of the characteristic polynomial, without dividing by zero. D is positive semidefinite for q in[0,2]^3 because every such q comes from a Bloch momentum.

## Kramers doubling and exact polynomial degree

Every A_a is purely imaginary, while C² is real. The antiunitary Theta=(I_8 tensor iY) complex conjugation satisfies Theta²=-I and Theta D Theta^{-1}=D: both A and the spin Pauli vector reverse sign. Therefore each eigenvalue of D has even multiplicity. Its characteristic polynomial is the square of a monic degree-eight polynomial p(z;q). This is a finite algebraic degeneracy, not physical species or time-reversal identification.

One can compute p exactly without choosing square-root branches of a determinant. Its power sums are s_j=Tr(D^j)/2; Newton recursion c_0=1 and j*c_j+sum_{i=1}^j c_{j-i}s_i=0 constructs its eight coefficients. They are polynomials in q. Spin pi rotations flip any two q signs, and P_y flips all three; hence each coefficient is even in each q_a. In x_a=q_a², coefficient c_j has total degree at most floor(j/2). This gives a small exact polynomial representation with at most35 monomials per coefficient, rather than a64-degree Laurent determinant. Explicit coefficient extraction is a next deterministic task, not asserted completed here.

For the canonical cube C²=3I. Its A_a anticommute. Therefore the three A_a tensor sigma_a commute, square toI and have all eight joint sign assignments with multiplicity2. The canonical D roots are

6 + epsilon_0 q_0 + epsilon_1 q_1 + epsilon_2 q_2,

one for each epsilon in{+1,-1}³, each twice. These are nonnegative on the physical cube and reproduce the seam-aware finite pi dispersion after grouping the four-cell momenta. In particular k=0 gives6I; k=(pi,pi,pi) includes zero. No smoothness through that zero is presumed.

## Density normalization and certification route

Tr_64|h|=4 Tr_16 sqrt(D). Thus

e_aux=-(1/32) average_k Tr_16 sqrt(D)
      =-(1/16) average_k sum_{j=1}^8 sqrt(lambda_j(D)).

The original native half-factor and restored hopping amplitude remain unchanged. Setting q_a=2sin(theta_a), theta in[0,pi/2]^3, replaces the normalized k integral by the uniform normalized theta integral. It avoids introducing an endpoint-singular arcsine weight into a numerical implementation.

A concrete rigorous route is now degree-eight real-root isolation at rational q or certified interval evaluation of D16, coupled to sine intervals and a fixed/admissibly refined box enclosure for the trace square roots. The canonical eight roots are explicit. Zero neighborhoods need interval/Holder treatment, not a falsely smooth quadrature remainder. Exact Newton coefficients can permit cheaper certified root enclosures than repeated64-matrix diagonalization. This reduces an actual algebraic cost; it does not establish positive density differences or that the resulting enclosure will be sharp enough. Correlated comparison bounds and finite-size/winding corrections are still independent obligations. No pointwise ordering against the canonical background is assumed.

## Deterministic controls

The preregistered control compares the literal64-site Laurent square with the tensor identity for all32 backgrounds at all eight k_a in{0,pi}. It also checks the reduced Hermitian block and exact fourfold trace moments through degree3:1,281 predicates,0.36seconds external,21,528,576bytes high water. Omitting the entire cross term changes224 of256 cases; it is a genuine adverse matrix check, not a claimed coefficient mutant.

A second exact control uses the nontrivial rational unit phase(3+4i)/5 in all three axes. After multiplying h by5, the square identity is verified entirely in Gaussian integers for all32 backgrounds, so the sine terms absent at0/pi are actually exercised. The same control verifies Theta invariance and Theta²=-I at the algebraic test vector q=(1,2,3); q=3 is explicitly only an algebraic test, not a physical momentum.96 additional predicates pass. Python complex values here contain small exactly represented integers; there are no floating eigenvalues, tolerances or integrations.

The analytical Clifford and antiunitary arguments, rather than finitely many trace moments, establish the full all-k multiplicities. All inputs, source and outputs are hash-bound. No pilot result was read before this freeze.


---

## Full source proof: Shift-uniform semiconvex quadrature and small sizes

Original source: `native-spectral-semiconvex-quadrature/DERIVATION.md`; SHA-256 `71f73aed45e7edcd33307494eb98d1fa8feebbe8b2fa1d5979d3c51a3678d26a`.

# Uniform quadrature bounds without spectral smoothness

Status: conditional-support candidate, independent analytical review pending. This is a proof candidate for the supplied period-four Bloch matrices, not a completed density certificate. No new physical spectral evaluation is executed by this packet.

## Minimal premises

The six frozen unit-hopping64-site Hermitian Laurent matrices have16 disjoint wrapped edges in each coordinate. Their second coordinate derivative is supported on those edges and is a direct sum of16 two-by-two matrices with eigenvalues±1. Consequently its nuclear norm is exactly32. The auxiliary energy density is minus the normalized zone integral of f=Tr|h| divided by128. The native physical hopping normalization is restored separately. No nonzero band gap, differentiable eigenvectors, or absence of band crossings is assumed.

## Semiconvexity of the trace norm

Fix two momentum coordinates and write H(t) for the remaining Hermitian matrix. The nuclear norm is convex and1-Lipschitz in its own norm. Taylor's integral remainder gives

||[H(t+s)+H(t−s)]/2−H(t)||_* ≤ 16s².

Indeed the second derivative has nuclear norm32 uniformly and each one-sided remainder has norm at most16s². Convexity then gives

[f(t+s)+f(t−s)]/2 ≥ ||[H(t+s)+H(t−s)]/2||_* ≥ f(t)−16s².

Therefore f(t)+16t² is midpoint convex and continuous, hence convex on the real line. Thus f is semiconvex with constant C=32. This argument permits zero eigenvalues and cusps. For g=f/128 the constant is1/4.

## One-dimensional periodic quadrature

Let g be a continuous2π-periodic function with g(t)+(C/2)t² convex, and use n uniformly spaced samples with arbitrary shift. Put Δ=2π/n and Q_n the sample mean, I the normalized integral.

On a cell centered at c, a subgradient of g(t)+(C/2)t² at c supplies

g(t)≥g(c)+p(t−c)−(C/2)(t−c)².

Integrating over that cell cancels the linear term. Summing centered cells yields

I g−Q_n g≥−CΔ²/24.

On a cell[a,b] whose endpoints are consecutive sample points, convexity of the corrected function gives

g(t)≤[(b−t)g(a)+(t−a)g(b)]/Δ+(C/2)(t−a)(b−t).

Integrating and summing over a period makes the composite trapezoidal sample mean exactly Q_n. Hence

I g−Q_n g≤CΔ²/12.

Both bounds hold for every shift, with no differentiability requirement. The two decompositions use the same periodic sample mean.

## Three-dimensional product grid and energy differences

Each coordinate integration or finite averaging preserves the same semiconvex constant in each remaining coordinate. A telescoping difference between the three-dimensional integral and product-grid mean therefore adds the three one-dimensional errors. For g=f/128 and grid counts(n1,n2,n3),

−(π²/24)Σ_a n_a^−2 ≤ I g−Q g ≤ (π²/12)Σ_a n_a^−2.

For auxiliary energy e=−g the signs reverse. Comparing two such energy densities, possibly with different grid shifts but the same counts, gives

|[I e_q−I e_pi]−[Q e_q−Q e_pi]| ≤ (π²/8)Σ_a n_a^−2.

On a cubic n³ grid this is3π²/(8n²), about0.003615 at n32. A looser boundπ²/(2n²) is also safe. Arithmetic error in the sampled trace norms must be added separately; no floating eigensolver stability theorem is silently assumed.

## Consequence if the five density certificates succeed

Suppose a later verified calculation proves each of the five noncanonical infinite-volume auxiliary density differences at least d0>0. The same shift-uniform bound controls finite cubic M³ momentum grids, including all eight winding twists and the canonical twist. For all M with3π²/(8M²)≤d0/2, every finite comparison density is at least d0/2. The finite collection of smaller cubic M has strictly positive comparisons by the separately proved finite flux-isolation theorem. Their minimum is positive, so a volume-uniform positive local-defect coefficient exists for all cubic L=4M. This does not supply its explicit value unless the finite collection is quantified, and does not extend to all aspect ratios with unbounded other sides while one side stays small.

This potential conclusion is conditional on the five as-yet unproved density bounds. It is compatible with the closing pure-winding gap because winding sectors have zero elementary defect count. It concerns the supplied zero-electric-penalty Hamiltonian and is not a nonzero-penalty phase theorem or Hamiltonian-selection result.


---

## Full source proof: Finite-temperature fixed-orbit stiffness

Original source: `native-finite-temperature-flux-stiffness/DERIVATION.md`; SHA-256 `b8c272d9f4c70152451d73a4cd645401574b3878175683938d3815ada61bcd29`.

# Conditional finite-temperature defect stiffness

Status: independently derived, pending review. No spectral or stochastic computation. The uniform U=0 Hamiltonian, native constrained dictionary, finite-temperature reflection theorem, and hypothetical positive ground-density certificate are supplied premises. No nonzero-U phase statement.

## Exact parity and partition factors

Let N be even, with N/2 active complex modes and N/2 spectator modes. In a fixed link-flux orbit the physical total parity is fixed even. For every active occupation, exactly 2^(N/2-1) spectator occupations supply the required parity. Thus, including active zero modes,

    Z_native = 2^(N/2-1) Z_active,
    Z_aux = Z_active^2,
    Z_native^2 = 2^(N-2) Z_aux.

Here Z_active is its unrestricted trace. The auxiliary number-conserving N-mode spectrum doubles the active Majorana spectrum, so its paired-frequency product is precisely the square. Spectator parity is not imposed a second time on the active or auxiliary trace. Consequently every fixed-orbit native free-energy difference is half its auxiliary counterpart. Summing these sector weights is the full native Gibbs partition function; maximizing one weight does not eliminate the other sectors.

## Thermal and finite-size density errors

Use unit hopping in the 64-site Bloch matrices; physical hopping h=2|g lambda| multiplies energies and changes inverse temperature to beta h. Below energies and beta are physical unless h is explicitly shown. For any N-site auxiliary one-particle matrix,

    -N log(2)/beta <= F_aux-E_aux <= 0.

This follows term by term from log(1+exp(-beta|epsilon|)). Thus a difference of two auxiliary densities loses at most log(2)/beta, not twice that amount.

Suppose all noncanonical disseminated infinite-volume ground-density differences are at least d0>0 in physical units. On a rectangular period-four torus with M_a=L_a/4 momentum points per axis, the reviewed shift-uniform semiconvex bound gives

    d_beta,L(q) >= d0 - h*pi^2/8 sum_a M_a^(-2) - log(2)/beta.       (1)

This includes all eight winding twists. It is a bound on the finite-temperature comparison list, not an evaluation of d0.

The same quadrature constant holds directly at finite temperature. Replace Tr|H| by f_beta(H)=Tr[(2/beta)log(2cosh(beta H/2))]. This is convex as a spectral trace functional and is 1-Lipschitz in nuclear norm: its scalar derivative is tanh(beta x/2), bounded by one. The original midpoint-convexity argument therefore applies unchanged to the matrix second derivative, whose nuclear norm is 32 at unit hopping. Dividing by 128 gives semiconvex constant 1/4. No spectral gap or smooth eigenvectors are required.

For cubic M and 3h*pi^2/(8M^2)<=d0/4, beta>=4log(2)/d0, (1) is at least d0/2. The finite number of smaller cubic sizes can also be included existentially: their strictly positive ground comparison gaps follow from the separately proved finite all-even isolation theorem; choose beta large enough that their density gaps survive the same thermal bound. This supplies an all-cubic-size positive coefficient conditional on d0, but no explicit small-size constant without further certificates. It does not cover arbitrary aspect ratios with a permanently small side by this argument.

## Dissemination at finite beta

Macris–Nachtergaele, cond-mat/9604043, Section 2 Remark (a), explicitly replaces ground energy in the reflection lemma by minus log of the full Fock trace. Dividing by beta gives

    F_beta(s) >= [F_beta(s_+)+F_beta(s_-)]/2.

Its graph, coupling and trace assumptions are those already checked for the supplied auxiliary problem. The existing disjoint-cube proof uses only this inequality and finite minimization: replace every energy by F_beta. The longest-run minimizer argument and the secondary minimization of bad crossing faces are unchanged. Therefore Phi_beta,L(q) is the minimum over the eight windings of the same compatible periodic cube pattern.

Set B=N/8 and

    delta_beta,L = min_(m(q)>0) [Phi_beta,L(q)-F_beta,pi]/[B m(q)].

All 32 labels and their Bianchi-compatible link tilings remain as in the geometry proof. Averaging over eight cube partitions counts each defective face twice, giving

    F_native(s)-F_native(pi) >= delta_beta,L k(s)/8.                (2)

If (1) is at least d0/2, m(q)<=6 implies delta_beta,L>=2d0/3. Thus the native coefficient in (2) is at least d0/12. This is a low-temperature local-defect free-energy cost, uniform on the specified large cubic volumes, conditional on the not-yet-established density certificate. Pure winding changes have k=0.

## What this proves about the Gibbs distribution

There is a useful global probability consequence without claiming a Peierls theorem. Suppose (2) holds with a uniform coefficient kappa>0. An allowed elementary-face assignment determines at most eight link gauge orbits, one per winding. There are 3N faces. Bounding allowed assignments by all binary assignments is an overcount and hence safe. Since the full partition is at least Z_pi,

    Prob(k>=1) <= min(1,8[(1+exp(-beta kappa))^(3N)-1]).

This bound is volume-growing. It does not prove probability one of the canonical orbit at a fixed positive temperature. More usefully, for 0<s<beta kappa,

    E exp(s k) <= 8(1+exp(-(beta kappa-s)))^(3N),
    E k/N <= [log(8)/N+3log(1+exp(-(beta kappa-s)))]/s.

The second statement is Jensen's inequality. Taking s=beta kappa/2 gives a low-temperature bound on mean defect density, including a finite-size term. These conclusions include Bianchi constraints by overcounting; they do not require independent defects. They are not estimates for a specified contour conditioned on its exterior.

A genuine conditional Peierls/chessboard event estimate still needs either a local repair map with a conditional free-energy comparison or a proved reflection-positive annealed native measure with its event inequality. The identity Z_native proportional sqrt(Z_aux) is an identity of weights, and does not by itself establish positivity of an annealed reflection kernel. Entrywise square roots do not in general preserve positive semidefiniteness. No such extra measure theorem is asserted here. A global comparison with one reference orbit cannot simply be subtracted between two arbitrary exterior-conditioned configurations.

## Source coverage and next obligation

Read in full the local flux-selection DERIVATION, the compatible 3D dissemination DERIVATION, and the semiconvex quadrature DERIVATION. The first two are reused source proofs, not newly independent derivations of their zero-temperature statements. Directly checked the primary paper's assumptions, reflection setup and finite-temperature Remark (a): https://arxiv.org/html/cond-mat/9604043 . Its finite-temperature reflection result is load-bearing; the present parity, softabs, dissemination substitution and counting consequences are the new derivation. No third-party text is archived.

The next decisive input is the five positive infinite-volume density certificates with physical normalization. Once available, (1) prices a temperature/size regime immediately. A conditional contour theorem is a distinct later obligation; neither it nor a physical phase is needed for the free-energy statement above.


---

## Full source proof: Native annealed reflection positivity and joint events

Original source: `native-finite-temperature-chessboard/DERIVATION.md`; SHA-256 `918d3aae1487e825151478a9b2765fa48e82508a395c10a50fe7315760c7b561`.

# Native annealed reflection positivity and joint defect events

Status: new independent proof candidate, frozen for hard review. Theory only. Supplied uniform U=0 native model, even cubic extents divisible by four, nonzero hopping, exact native/active dictionary, and a uniform fixed-orbit free-energy penalty kappa*k are premises. The last premise remains conditional on the ground-density certificate and temperature/size conditions in the previous finite-temperature packet. No nonzero-U or physical phase claim.

## 1. Why pointwise Cauchy–Schwarz is insufficient

A bound w(l,r)<=sqrt(w(l,l)w(r,r)) alone does not establish positivity of the matrix w, nor a normalized annealed event inequality. Summing that bound produces sums of square roots. The square-root identity between native and auxiliary weights does not solve this problem. Instead we prove positivity directly for the active Majorana trace, then use the exact constant spectator factor.

## 2. Fixing the crossing matching

Take a coordinate reflection between sites, including both opposite cut planes. Half width is at least two. Every boundary vertex belongs to exactly one crossing edge: the crossing edges form a matching. Let its size be c. For each assignment of its signs, use a vertex sign gauge on one endpoint of each matching edge to set every cross term to -i t gamma_L gamma_R, t>0. This is possible independently for all c edges. It bijectively relabels the internal link signs in each half and preserves all gauge-invariant face events wholly within a half.

Consequently the sum over all link fields of such half-factorized events equals 2^c times the sum with fixed crossing signs. There is no discarded flux or winding. Passing from all link fields to gauge orbits divides every sum by the same 2^(N-1), since the connected graph's vertex-gauge action has only the constant-sign kernel. These factors cancel in probabilities. No gauge fixing to a spanning tree is needed.

## 3. Direct active-Majorana positive kernel

Each half has N/2 Majoranas, an even number. Represent left Majoranas by alpha_j tensor I, and right Majoranas by P_L tensor conjugate(alpha_j), after reflecting the right coordinates. Here P_L is left fermion parity. The right reflected internal Hamiltonian is the complex conjugate of the left one. This incorporates the magnetic reflection's reversal of the imaginary hopping coefficient; returning to link coordinates gives canonical crossing fluxes, as in the source dictionary.

For arbitrary left internal field l and right reflected field r, apply a Lie–Trotter product to the internal Hamiltonians and the cross matching. For a time slice of size dt each cross exponential is

    exp(i dt t alpha_j P_L tensor conjugate(alpha_j))
      = cosh(dt t) I + i sinh(dt t) alpha_j P_L tensor conjugate(alpha_j).

The crossing bilinears commute because their endpoints are disjoint; hence each slice expands exactly over subsets, with positive real cosh/sinh weights. A complete expansion history with m selected cross factors has left product containing m parity operators. Move these parities to its right through the odd alpha factors; all internal exponentials are even and commute with parity. The sign is (-1)^(m(m-1)/2). If m is odd, the left trace vanishes by parity, including its final P_L. If m=2k, P_L^m=I and

    i^m (-1)^(m(m-1)/2)=1.

The right trace is the complex conjugate of the corresponding left word evaluated at r, with the same ordered internal exponentials and alpha insertions. Thus at every Trotter depth the kernel is a sum of positive weights times f_history(l) conjugate(f_history(r)). It is positive semidefinite. The finite-dimensional Trotter limit preserves positivity. The spectator factor 2^(N/2-1) is positive and independent of l,r, so the native kernel has the same property. Active zero modes cause no exception.

This gives reflection positivity for arbitrary complex gauge-invariant functions of the internal half-link fields. In particular Cauchy–Schwarz applies after summing those fields, with the exact crossing multiplicity from Section 2. This is a proof of native annealed positivity, not an entrywise-square-root inference.

## 4. Cube-event chessboard estimate

Use the disjoint two-site cubes and the twisted 32-label alphabet of the earlier compatible dissemination proof. Add a wildcard label meaning no condition. For any cube-label assignment let P(q_b) be its normalized native Gibbs event probability. These probabilities are strictly positive for compatible assignments. Reflection positivity gives

    P(q_b)^2 <= P(q_b^+) P(q_b^-).

The normalization is the same full partition function in all three probabilities. Setting f=-log P converts this to exactly the half-reflection inequality used by the finite longest-run chessboard lemma. The wildcard transforms to itself. Applying that finite-alphabet lemma in three directions, with eta_b=(product rho_a^b_a)q_b, gives

    P(q_b) <= product_b P(disseminated eta_b)^(1/B),  B=N/8.

The wildcard disseminated event has probability one. This proof works for arbitrary even block counts; no power-of-two size assumption is introduced. The magnetic reflection exchanges opposite cube faces exactly as before.

## 5. Explicit entropy price and joint defects

Assume each orbit s satisfies F_native(s)-F_native(pi)>=kappa*k(s), kappa>0. A fully disseminated noncanonical cube label q forces B*m(q) defective faces, m(q)>=2. Its internal constraints are five independent cycle constraints per disjoint cube. In the full cycle space of dimension E-N+1=2N+1, they are independent because their internal edges are disjoint. Therefore exactly 2^(2N+1-5B)=2^(11B+1) link gauge orbits realize this label pattern, including all windings and crossing fields.

Since Z_total>=Z_pi,

    P(disseminated q) <= 2^(11B+1) exp(-beta*kappa*B*m(q)).

For any k distinct cubes required to be bad in a fixed partition, sum the chessboard estimate over their 31 noncanonical labels. Thus

    P(all k cubes bad) <= p^k,
    p = min(1,31*2^(11+1/B)*exp(-2 beta kappa)).

When the displayed untruncated factor is below one, this is a joint-event suppression estimate. It retains the explicit gauge/cross-link entropy, and does not pretend the fluxes are independent.

For any prescribed set of m distinct defective elementary faces, one of the eight partitions contains at least m/4 of those faces internally (each face is internal in two partitions). Each cube contains at most six. Hence at least m/24 distinct cubes of that partition must be bad, and

    P(all prescribed m faces defective) <= p^(m/24).

Integer ceilings can strengthen this bound. The partition is selected from the prescribed set, independently of the random configuration.

## 6. Contours and scope

Dual edges corresponding to defective plaquettes form an even-degree graph by cube Bianchi. To obtain a conservative unconditioned connected-set bound, the number of connected m-edge dual sets containing a fixed vertex is at most 6^(2m)=36^m: choose a deterministic doubled-edge traversal of length 2m and encode its six-valued steps. Therefore, if a=36*p^(1/24)<1,

    P(exists a connected defective dual set containing v with size >=ell)
       <= sum_(m>=ell) a^m = a^ell/(1-a).

Finite-volume sums only improve this bound. Winding components are included as connected sets, but pure magnetic winding changes without plaquette defects are not. This is an unconditioned joint-defect/connected-set bound. It is not a uniform exterior-conditioned DLR comparison, a uniqueness theorem, a confinement/deconfinement theorem, or a nonzero-electric stability result. The deliberately large entropy threshold is merely sufficient.

The new load-bearing step is Section 3's native Majorana trace positivity. The old objective inequality alone would not license Sections 4–6. All Hamiltonian and thermal ensemble choices remain supplied.

