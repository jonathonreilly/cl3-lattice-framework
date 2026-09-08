# Independent fourth-order virtual native-edge calculation

Frozen independently before reading the native author folder. Domain: finite simple even cubic torus, extents at least four, literal ice P, actual low-charge projection, H0=UD with U>0. V=sum_e lambda_e P_low A_e P_low uses a declared fixed orientation for each Hermitian native edge generator. Couplings are supplied real numbers. Treat an auxiliary formal strength multiplying V; no finite-strength convergence bound is asserted.

## Canonical effective Hamiltonian

Let R=(1-P)/H0 on the low domain. Since PVP=0, the canonical Hermitian fourth-order operator is

H2=-PVRVP,
H4=-PVRVRVRVP + (PVR²VP PVRVP + PVRVP PVR²VP)/2.

This follows also by the energy-dependent Feshbach operator and normalization of its P component: the energy derivative produces the displayed folded term. Every one-edge departure from ice has D=2, and only repeating that edge can return in two steps. Thus PVRVP=L/(2U) P and PVR²VP=L/(4U²) P, L=sum_e lambda_e². H2=-L/(2U)P and the folded H4 term is L²/(8U³)P. Odd orders through three vanish on this bipartite graph.

## Four distinct edges

A nonzero off-diagonal ice return with four distinct toggles is an alternating simple four-cycle C. Let its cyclically oriented generators be A01,A12,A23,A30 and S_C=i^4 A01 A12 A23 A30. Incident generators anticommute, disjoint ones commute. All 24 orders are allowed on an alternating input. Intermediate D is (2,2,2) when the first two edges are adjacent, and (2,4,2) when opposite. Relative to the cyclic product, the sixteen adjacent-first signs sum to zero. The eight opposite-first signs are all minus. Therefore the resolvent-weighted sum is -S_C/(2U³), and H4 contributes +S_C/(2U³) times the product of CYCLICALLY ORIENTED couplings.

For actual fixed orientation generators A_e, write A_e=eta_e A_cyclic,e. The coefficient is (product eta_e lambda_e)/(2U³) multiplying P S_C P, equivalently the flippability-gated ring. Positive fixed-orientation lambda alone is NOT an orientation-independent sign statement. For the four labels cyclically 0,1,2,3 with fixed ascending edges, product eta=-1; for the usual rectangular lexicographic pattern 0,1,5,4 it is +1. Arbitrary real signs enter through their cycle product. This qualification is essential before calling the induced ring ferro/antiferro relative to a chosen native S convention.

Every simple four-cycle contributes once. On L=4 periodic directions this includes winding straight four-cycles as well as elementary plaquettes. Dropping winding cycles would change the finite operator. Nonalternating four-cycle toggles do not return to ice.

## Diagonal fourth-order terms

A four-toggle diagonal return uses one edge four times or two edges twice. The irreducible R string excludes any intermediate return to ice.

One edge repeated has no irreducible contribution; its folded term is lambda_e^4/(8U³).

For disjoint e,f, the four allowed nonreducible words all have phase + and denominators 16U³; their total -lambda_e²lambda_f²/(4U³) cancels the folded cross term +lambda_e²lambda_f²/(4U³).

For incident e,f with equal initial occupation, toggling both violates the low constraint, so all irreducible words vanish. With opposite occupation, the four words have middle D=2; two signs are plus and two minus, by actual incident A anticommutation. They cancel exactly. Thus BOTH occupancy cases retain the same folded cross term +lambda_e²lambda_f²/(4U³).

Consequently the entire diagonal H4 term is the configuration-independent scalar

[sum_e lambda_e^4/8 + sum_{unordered incident e,f} lambda_e²lambda_f²/4]/U³.

There is NO flippability-dependent fourth-order diagonal potential in this canonical convention. In uniform degree-six coupling lambda, it is [|E|/8 + 15|vertices|/4]lambda^4/U³. This scalar is not a claim that higher orders have no potential. A different effective-basis convention cannot change this order by commuting with H2, which is scalar.

## Finite evidence and limits

check.py independently constructs literal native local Pauli strings X_e times earlier-neighbor Z strings on a square, checks both alternating columns and all 24 orders (48 columns), retaining exact rational denominators and signs. The external incident edges needed for degree-six ice have fixed occupation supplying degree two at each vertex; their unchanged Z factors multiply all paths equally and cancel in the comparison to S. The remaining diagonal-word checker uses the independently stated native Clifford relation and tests disjoint/incident, equal/opposite cases. These are local exact controls, not an L4 census. The single-edge fourth-order value also agrees with expanding the two-level eigenvalue U-sqrt(U²+lambda²).

The proposed mechanism requires supplied A couplings, literal low projection and U D penalty; the original T-only dynamics does not generate this result by itself. It does not select couplings, physical time, an ice constraint, or electromagnetic dynamics. No claim of a formal canonical audit is made.
