---
claim_id: native_flux_defect_comparison_and_winding_gap_note_2026-09-08
claim_type: bounded_theorem
claim_scope: "Supplied zero-electric-penalty uniform native model: on cubic tori with extents divisible by4, compatible block reflection reduces local-defect costs to31 periodic cube classes with8 winding choices; on even cubicL, winding twists imply full wrong-orbit gap O(|t|/L). No uniform positive local-defect cost or nonzero-penalty phase is proved."
upstream_dependencies:
  - native_even_torus_flux_isolation_note_2026-09-08
runner: scripts/native_flux_defect_comparison_and_winding_gap_2026_09_08.py
---

# Local flux-defect comparisons and closing winding gaps

**Date:** 2026-09-08  
**Type:** bounded_theorem  
**Status:** conditional-support

For the supplied uniform full-native model at zero electric penalty, local plaquette defects and winding changes have different quantitative obligations. A compatible3D reflection argument reduces every local-defect cost to a finite list of31 periodic cube classes and eight winding choices. Separately, winding twists show that the full wrong-flux separation is at most C|t|/L along even cubic tori. A positive gap at each finite size therefore cannot be promoted to a volume-uniform full flux gap.

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: "Supplied finite full-native Hamiltonian, exact auxiliary objective identity, reflection inequality and canonical dispersion."
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

## Dependencies and exact scope

Use [finite even-torus strict flux isolation](NATIVE_EVEN_TORUS_FLUX_ISOLATION_NOTE_2026-09-08.md), [canonical flux and exact dispersion](NATIVE_ZERO_PENALTY_OPTIMAL_FLUX_DISPERSION_NOTE_2026-09-08.md), and the [native/auxiliary endpoint dictionary](NATIVE_ZERO_PENALTY_ENDPOINT_NOTE_2026-09-08.md). Hopping is uniform and nonzero, and electric penalty is zero. The auxiliary full-Fock energy is twice the native fixed-flux energy; no extra auxiliary parity projection is imposed.

The block comparison below requires each rectangular extent divisible by4. It proves E_native(s)−E_native,pi ≥ δ_L k(s)/8, where k counts noncanonical elementary faces and δ_L is defined by the actual finite periodic comparison energies. Strict flux isolation makes δ_L>0 at each fixed graph. No value of δ_L, uniform positive lower bound, or Bloch integral is supplied. There are32 compatible cube labels, including one canonical label; the31 others and eight winding choices specify the outstanding comparison problem.

The winding result is restricted to cubic evenL≥4. It proves0<Δ_flux(L)≤C|t|/L for an L-independent but unevaluated constant C, using an explicit wrong winding sector with no elementary defects. It does not determine a leading Casimir coefficient or local-defect cost. Neither statement selects the Hamiltonian, splits its spectator ground family, or establishes stability under nonzero electric penalty.

## Compatible three-dimensional block comparison

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


## Winding upper bound along even cubic tori

Consider uniform cubic L×L×L tori, even L≥4, fixed nonzero t. Use the exact canonical-seam dispersion already derived in native-zero-penalty-pi-dispersion/DERIVATION.md. For winding twist alpha in{0,1/2}³ its physical fixed-flux ground energy is

E_L(alpha) = -|t| sum_(n in{0,...,L-1}³) f(2pi(n+alpha)/L),

f(k)=sqrt(sin²k0+sin²k1+sin²k2).

The canonical minimizing orbit has alpha*=(1/2,1/2,1/2). Set alpha'=(0,1/2,1/2): this changes one winding and no elementary plaquette flux, hence is a different orbit. No zero active mode is introduced because two directions remain antiperiodic. The independently reviewed strictness theorem gives E_L(alpha')−E_L(alpha*)>0 for every finite L. We now bound this difference above without computing it.

### Fourier decay at the conical zeros

With period2pi define fhat(q)=(2pi)^−3 integral f(k)e^(−iq·k)dk. There is a constant C independent of integer q such that |fhat(q)|≤C(1+|q|)^−4.

Proof: f is smooth except at the eight points with all coordinates0 orpi. Near each such point, its positive quadratic leading form is Euclidean norm squared. Consequently on a dyadic annulus of radius r, derivatives of order j of f are bounded by C_j r^(1−j). Choose a smooth annular partition with the usual derivative scaling; the localized function has derivative L1 bounds C_j r^(4−j). Its Fourier coefficient is therefore bounded by C r^4 min(1,(|q|r)^−5), integrating five times along a largest coordinate of q for the second bound. Sum annuli r≤|q|^−1 directly: their r^4 sum is O(|q|^−4). For larger r the bound is C|q|^−5 r^−1, whose dyadic sum is O(|q|^−4), dominated by the smallest such radius. The smooth remainder decays faster. A finite sum over the eight singularities proves the bound. This avoids the logarithmic loss that a naive global fourth-derivative L1 estimate would produce.

Since power4 exceeds dimension3, the Fourier series is absolutely convergent. Thus termwise finite grid summation is valid and gives exactly

sum_n f(2pi(n+alpha)/L) = L³ sum_(m in Z³) fhat(Lm) exp(2pi i m·alpha).

The m=0 bulk term cancels between twists. Therefore

|E_L(alpha')−E_L(alpha*)| ≤ 2C |t| L^−1 sum_(m≠0)|m|^−4 = C' |t|/L.

C' is finite and independent of L; no explicit numerical value is asserted. This is an upper bound, not an asymptotic equality or a computed Casimir coefficient.

### Consequence for the full flux separation

Let Delta_flux(L) be the minimum ground-energy difference from the canonical orbit to ANY wrong native flux orbit. The exhibited winding sector proves

0 < Delta_flux(L) ≤ E_L(alpha')−E_L(alpha*) ≤ C'|t|/L.

Thus the strictly positive finite-volume wrong-flux separation cannot have a positive volume-independent lower bound along cubic even tori. This does not contradict finite all-even flux uniqueness or the enumerated L6 prefix bounds. Those prefixes are local electric toggles, whereas a winding twist changes a noncontractible flux class. The argument proves neither a positive local plaquette-defect cost nor its absence. It also supplies no nonzero-U phase, finite-penalty radius, full excitation dispersion, or mixing statement.

The only spectral input is the exact finite dispersion in the specified eight pi-plaquette winding sectors; the strict positive lower side imports the separately reviewed finite strictness theorem. No numerical production or new spectrum computation was performed. Extension to uniformly bounded aspect-ratio rectangular sequences follows by the same anisotropic grid estimate, but the stated conclusion is deliberately restricted to cubic L.

## Evidence and remaining work

The [science packet](../.claude/science/physics-loops/native-flux-defect-comparison-and-winding-gap-20260908/HANDOFF.md) preserves the full original arguments, independent cold and root source reviews, exact geometry and combinatorial controls, and canonical port receipts. The live runner checks compatible cube tilings, seam/winding corrections, Bianchi identities, defect counts and finite reflection-run combinatorics. These are controls of sensitive construction steps. The energy inequality and all-size Fourier bound are analytical proofs, not extrapolations from the finite tests.

The next quantitative target is a certified positive limiting density difference for each noncanonical periodic comparison, with finite-size and winding corrections. The two-dimensional Goller–Porta result motivated the approach, but is not imported as a three-dimensional theorem. A fixed-volume positive δ_L is insufficient for a uniform local-defect cost. The winding upper bound explains why even such a local result would not give a uniform gap to every wrong flux orbit.
