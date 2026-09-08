# Independent plane construction and conditional law

Fix six labels and a strictly positive symmetric stochastic K of the source orbit form: K(s,c)=p/Z for s=c, q/Z for antipodes, r/Z otherwise, Z=p+q+4r. Put L=K². The source rectangular monotone law is

mu_R(x)=1/6 times product over all horizontal/vertical edges of R K(xu,xv), divided by product over every elementary square of R L(xSW,xNE).

This is the actual causal product reorganized: each interior site contributes its two incoming K factors and the bridge denominator; boundary chains supply every other nearest-neighbor edge. It is not a separately assumed Gibbs law. Opposite corner reversal preserves the unoriented denominator diagonal, hence the same law; a single reflection swaps diagonals. The corrected source has two classes, not four.

## Every translated subrectangle

At fixed width W, regard rows as states. The entire n-row joint law is p0(r0) product P(ri,ri+1), with p0P=p0. Summing the bottom row uses P1=1 and summing the top row uses p0P=p0. Either removes that row and leaves precisely the same rectangular law. Source transpose symmetry transfers these two deletion identities to leftmost/rightmost columns. Thus deleting any finite sequence of boundary rows/columns gives the same law on every translated subrectangle, including one-row/one-column rectangles. This is stronger than one-row stationarity alone and does not transpose an infinite strip.

For any finite A subset Z², choose a rectangle containing A and marginalize its mu_R. Two choices agree by embedding both in a larger rectangle and applying the deletion property. These finite marginals are normalized, consistent and translation covariant. The standard countable finite-alphabet extension theorem produces a unique probability law with these specified marginals. Uniqueness here is only of this cylinder extension, not uniqueness among Gibbs measures for its potential. The construction is not an enumeration or physical first-to-last formation order on the whole two-sided plane. It retains the finite records-only menu, weights and orientation as supplied mathematical premises.

## Full finite-set specification and DLR

Define pair potentials -log K on each nearest-neighbor edge and +log L on each NE–SW square diagonal. All are finite because the kernel is strictly positive. For finite Lambda and exterior eta define gamma_Lambda by multiplying K and inverse L over every such pair with at least one endpoint in Lambda, using eta on exterior endpoints, and normalize the sum over Lambda. It depends only on the finite expanded boundary, not a full infinite product.

Choose a finite rectangle R containing Lambda and every interaction neighbor of Lambda. Conditional on R\Lambda under mu_R, all factors not touching Lambda cancel, so the exact conditional equals gamma_Lambda. This works for arbitrary finite Lambda, disconnected or otherwise. For every exterior cylinder event B, enlarge R to contain B's finite support as well. Rectangle consistency gives the equality of integrals mu(1_B 1_{xLambda=z})=mu(1_B gamma_Lambda(z|outside)). The exterior cylinders generate the exterior sigma algebra; a monotone-class argument extends this to every exterior event. This is the DLR identity. No informal interchange of pointwise infinite conditional limits is needed. The specification itself is defined for every exterior configuration; the regular conditional version is asserted mu-almost surely.

At a site v the single-site distribution is proportional

product_{u nearest v} K(s,eta_u) / [L(s,eta_NE) L(s,eta_SW)].

There are four NN and two diagonal neighbors, not the original four-neighbor static rule. It is a retrospective conditional law given all final outside records, not the original two-parent formation instruction at the time a site was formed.

## Strict difference from the original static specification

Let the six expanded neighbors all carry c (requiring all eight surrounding positions to be c is an equally valid stronger cylinder). Its probability under mu is strictly positive because it is a marginal of a strictly positive finite rectangle law. The new conditional is proportional K(s,c)^4/L(s,c)^2, whereas the original static conditional is proportional K(s,c)^4. Equality of the two normalized positive vectors is equivalent to L(s,c) being constant in s.

For the orbit kernel, the three entries of Z²L are A=p²+q²+4r², B=2pq+4r² and C=2r(p+q)+2r². A-B=(p-q)²; after p=q, A-C=2(p-r)². Hence one column is constant iff p=q=r. Equivalently transitivity propagates a constant column to all columns, then symmetric K with K²=J/6 must be K=J/6. Both arguments avoid assuming invertibility or positive eigenvalues of K.

Therefore for every positive nonconstant triple the plane law fails the original static four-NN DLR identity on a positive-probability cylinder. Conditioning only on the four NN does not evade this statement: a static DLR law requires its four-NN formula to hold given the entire exterior. This proves mu is not any Gibbs measure satisfying that original specification; it does not prove uniqueness or compute its static Gibbs law. Constant weights give iid uniform agreement. Positivity is load-bearing for the cylinder and division arguments.

Scope: finite menu, symmetric orbit product rule and chosen monotone orientation; no axiom-selected measure, order, action, physical clock, three-dimensional plane coupling or adopted parked statistical bridge. General existence and DLR reasoning use standard countable probability scaffolding. These are independently derived proof notes before opening the native author's new proof.
