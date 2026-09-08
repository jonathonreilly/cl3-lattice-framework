# Independent sixth-order diagonal: uniform native edge magnitude

Prospective plan and calculation were frozen without reading an author sixth-order derivation. Same supplied H=UD+gV, low projection, cubic simple even torus with extents>=4, and fixed native incident anticommutation as the fourth-order derivation. U>0; all |lambda_e|=lambda. This is a formal finite-volume coefficient, not a uniform perturbation bound. Signs disappear from every diagonal word because each edge occurs evenly.

## Schur expansion and normalization

Set U=lambda=1 temporarily. Write R=Q/H0 and a(E)=P V (H0-E)^-1 V P=a+E a1+E² a2+..., b(E) for the irreducible four-step positive resolvent word, and c for the six-step positive resolvent word. The Schur equation is E=-g²a(E)-g⁴b(E)-g⁶c+O(g8). Here a=N/2, a1=N/4, a2=N/8 are scalar operators, N=|edges|. Let b1=b'(0). Substitution gives

H2=-a,
H4=-b+a a1,
H6=-c+a b1+a1 b-a a1²-a² a2.

In the last equation b,b1,c are operators, and the scalar coefficients commute. This is also the canonical orthonormalized effective operator through this order: the order-g² normalization metric is scalar, while any order-g⁴ metric commutes with the scalar H2. Therefore the similarity correction cannot change H6. This argument would fail if the lower-order operators were not scalar in the required positions. We assert only the diagonal of this equation, not a full sixth-order off-diagonal formula.

For disjoint edge pairs, b_diag=1/4 per unordered pair. Differentiating the denominators (2-E)^-2(4-E)^-1 multiplies by 1/2+1/4+1/2=5/4, so b1_diag=5/16 per pair. Incident pairs cancel for b and b1 alike, or are refused by low support. Thus all folded diagonal terms are configuration-independent.

## Exhaustive irreducible diagonal word classification

A diagonal six-toggle word has multiplicities6,4+2,or2+2+2. Every proper prefix must remain outside ice and inside low support. The actual native Clifford sign is obtained by moving an edge across the active higher-index incident edges; disjoint edges commute. This is used only on admissible words, not as an assertion that projected generators globally anticommute.

The exact finite table (coefficient of c, before the Schur minus) is:

- One edge six times: zero, due to a two-step ice return.
- Multiplicity4+2: incident pair zero for either bit relation; disjoint pair1/32 for each choice of repeated-four edge, hence1/16 per unordered pair.
- Three distinct edges, each twice: three-edge star zero for all eight bit patterns; three-edge path1/32 for alternating010 or101 and zero otherwise; one incident pair plus disjoint edge1/16 for every bit pattern; three disjoint edges9/32 for every pattern.

The script enumerates all90 distinct 2+2+2 words for each of32 shape/bit cases and all15 distinct4+2 words for each of8 pair/bit cases, with exact rational intermediate D and low refusals. The four graph shapes exhaust triangle-free three-edge subgraphs. Exterior fixed ice occupancies affect neither the charge increments nor the closed-word Clifford sign. These finite exhaustive local tables establish the stated coefficient classification, not a whole-Hilbert enumeration.

The ONLY configuration-dependent local entry is alternating three-edge paths. Its global count is nevertheless exactly9N: choose the middle edge; each endpoint has exactly three edges whose initial bit opposes the middle edge. There are3×3 choices. Triangle freedom ensures distinct outer endpoints, so each choice is a simple path with a unique middle edge. This holds in every ice configuration, including winding sectors. The script checks all200 allowed endpoint bit arrangements as a separate finite control.

## Constant and conclusion

Let Pdis count unordered disjoint edge pairs, T21 triples with exactly one incident pair, and T0 triples of disjoint edges. Then

c_diag=Pdis/16+T21/16+9T0/32+9N/32.

On a simple degree-six triangle-free graph,
Pdis=N(N-11)/2,
T21=5N(N-16),
T0=choose(N,3)-5N²+145N/3.

Indeed adjacent pairs number5N; a third edge disjoint from their three vertices has N-16 choices. Three-edge stars number20N/3 and three-edge paths25N. Substitution in the normalized H6 diagonal gives exactly

H6_diag=-(69/8)N lambda^6/U^5 P = -(207/8)|vertices| lambda^6/U^5 P.

Hence uniform real-magnitude native A couplings produce no configuration-dependent diagonal ice potential at order six either. This does NOT say each connected cluster is bit-independent: the path cluster explicitly is not. The ice sum rule is necessary. Unequal magnitudes need not obey the weighted path-count cancellation. Length-six loops and dressed four-cycle off-diagonal terms are separate and are not evaluated here. No RK equality, action selection, or physical scale follows.
