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
