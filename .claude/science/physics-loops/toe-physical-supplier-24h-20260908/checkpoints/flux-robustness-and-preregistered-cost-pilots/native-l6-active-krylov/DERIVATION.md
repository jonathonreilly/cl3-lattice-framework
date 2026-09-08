# Exact L6 endpoint-generated active spaces

The computation uses the actual canonical216-vertex K0 from the frozen magnetic-invariant source: edges are in positive coordinate enumeration, their endpoints sorted, with Kij=-2(-1)^(sum of preceding coordinates). This includes its seam convention. SOURCE_BINDINGS pins the complete source read. The result concerns the supplied free active quadratic and the changed-edge supports of six electric insertions. It computes neither coefficients nor prefix denominators.

## Exact construction and proof of minimality

For endpoint set S define W=span_Q{K0^j e_v:v in S,0<=j<=7}. The complete integer matrix identity

(K0²+12I)(K0²+24I)(K0²+36I)(K0²+48I)=0

is verified on all216 coordinate columns. Hence W is invariant. Put A=-K0². For each lambda in12,24,36,48 the integer vector product_{mu!=lambda}(A-muI)e_v is a nonzero scalar multiple of its rational spectral projection. Within each lambda sector, paired exact Gram-Schmidt forms primitive integer r and K0r. The next r is orthogonalized against both members of all preceding pairs. Since K0 is skew and K0²r=-lambda r, the two members are orthogonal and their squared norms are d and lambda d. Orthogonalizing preserves the sector. Every operation is integer arithmetic with gcd cancellation, without numerical tolerance.

BASES.json stores all integer basis vectors and norms. The runner verifies K0²r=-lambda r, all pair and cross-pair inner products, and, for every endpoint v, the exact rational identity sum_b b[v]²/||b||²=1. Because this is an orthogonal basis, the last equality says that the orthogonal projection of e_v has full norm: e_v belongs to the span. Each basis vector was constructed from endpoint Krylov vectors, proving span(basis) is contained in W; endpoint containment and K0 invariance prove W is contained in span(basis). This establishes exact rank, both upper and lower, without relying on modular-rank inference.

In the ordered rational basis(r,K0r), the restriction is the explicit block [[0,-lambda],[1,0]] and the Gram block is diag(d,lambda*d). After orthonormalization it is [[0,-sqrt(lambda)],[sqrt(lambda),0]]. All four sectors occur, so the degree-eight annihilating polynomial is minimal on every reported space. This is a full block restriction certificate, not only a rank count.

For any changed edge its matrix change has range in its two endpoint coordinates. Consequently it preserves W and vanishes on W-perp. Every intermediate quadratic is the restricted quadratic on W plus the unchanged K0 bath on W-perp. Starting from the free vacuum, the unchanged bath stays in its vacuum; its constant energy must be subtracted consistently. The reduction does not assert a bound on any changed-prefix gap.

## Fixed support census and results

The adjacent centers are endpoints of edge0. The ten-edge cut plus a repeated bridge yields exactly the five geometrically compatible bridge families0,3,15,18,90. Each bridge's endpoints already lie in the same endpoint set as the cut. Separate calculations nevertheless retain all five cases and their union. The pair representatives use centers0 and the coordinate displacement named below;001 includes the complete adjacent bridge union, while every nonadjacent representative uses its twelve cut edges. Sixth-order pairings and orderings cannot enlarge these endpoint sets.

| Support | dim W | ranks at12,24,36,48 | complex modes | fixed active parity dimension |
|---|---:|---|---:|---:|
| Each of five adjacent families; union;001 |68|20,20,20,8|34|8,589,934,592|
|003|76|20,24,24,8|38|137,438,953,472|
|012,023,122,223|80|24,24,24,8|40|549,755,813,888|

Full active Fock dimensions are respectively2^34,2^38,2^40; the table halves these for one fixed parity. Electric insertions are even active operators, so a vacuum-start chain can remain in that parity block. This is the active Fock carrier, not the full physical Gauss/spectator Hilbert-space dimension. The inactive bath and spectator factors are not counted as additional dynamical active vectors.

The reduction is substantial relative to108 free complex modes, but does not make the old L4 vector method feasible. One real binary64 fixed-parity vector alone requires64GiB,1TiB,4TiB respectively; complex storage doubles this, before solver vectors and workspaces. The L4 W20/512-parity construction therefore does not transfer. A Gaussian, determinant/Pfaffian, tensor, or additional algebraic reduction would still be needed; no efficiency or convergence of those alternatives is claimed.

## Controls and resources

The frozen prospective source executed once under -OO:35,339 explicit predicates,0.65seconds external wall,24,821,760bytes external high water. The reported internal time is0.6218seconds. Exact altered-polynomial control replacing48 by47 is nonzero. The initial empty-span adverse check is intentionally trivial and is not credited as a strong scientific mutant. A separate actual saved-basis control removes a supported vector from each of the12 computed bases; the unchanged rational endpoint-containment predicate fails in every case. All original outputs are retained. There was no sampling, eigenintegration, coefficient evaluation, or support selection from outcomes.
