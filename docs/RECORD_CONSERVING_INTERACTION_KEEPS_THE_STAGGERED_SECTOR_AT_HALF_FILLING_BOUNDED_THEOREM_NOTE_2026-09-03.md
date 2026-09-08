---
claim_id: record_conserving_interaction_keeps_the_staggered_sector_at_half_filling_bounded_theorem_note_2026-09-03
claim_type: bounded_theorem
claim_scope: "Conditional finite fixed-N Jordan-Wigner hopping-plus-density comparisons: all32 cube sectors at nine couplings, two uniform sectors exactly at twelve integer couplings, corrected N=2 piecewise ground branch, all512 block sectors at named points, torus perturbative coefficients and exact cube fourth-order two-state matrix. No physical state selection, all-volume ordering or phase follows."
upstream_dependencies: [minimal_axioms_2026-06-29]
runner: scripts/record_conserving_interaction_keeps_the_staggered_sector_check_2026_09_03.py
---

# Finite interacting signed-hopping comparisons and their branch boundaries

**Date:** 2026-09-03; source correction 2026-09-08.
**Type:** bounded_theorem
**Status:** bounded mathematical source proposal; formal audit deferred and no audit grade assigned here.
**Primary runner:** [record_conserving_interaction_keeps_the_staggered_sector_check_2026_09_03.py](../scripts/record_conserving_interaction_keeps_the_staggered_sector_check_2026_09_03.py)
**Runner cache:** [record_conserving_interaction_keeps_the_staggered_sector_check_2026_09_03.txt](../logs/runner-cache/record_conserving_interaction_keeps_the_staggered_sector_check_2026_09_03.txt)
**Correction and original evidence:** [dated record](../.claude/science/review-fixes/flux-selection-7874-7878-20260908/REVIEW_CORRECTION.md). It preserves both original notes and both historical caches verbatim. The current cache must bind this final note, current governing memo and declared attribution context before use.

## Declared objects, domains, and authority

These are conditional finite matrix comparisons. The coarse graph, Hamiltonian, hopping scale, filling, and choice of a lowest-energy state are supplied mathematical inputs. An energy ordering neither moves a conserved flux sector nor derives a formation rule, physical clock, Born law, occupation-to-record dictionary, or a mechanism choosing that ground state. Hopping conserves total occupation, but does not commute with every local occupation operator. Permanent readable records are not identified with movable occupation labels here.

The [current governing memo](MINIMAL_AXIOMS_2026-06-29.md) supplies the framework boundary only. No axiom is amended or inferred to select this model. The current composition discriminator, `COMPOSITION_DISCRIMINATOR_RECORD_STATISTICS_BOUNDED_THEOREM_NOTE_2026-09-02.md`, is attribution context: it declares a hopping-plus-density subfamily, not a complete global law. A locally allowed number term sums to `sum_i degree(i)n_i` and need not be constant on an irregular open graph. With nonzero hopping on a bipartite graph a sign gauge and positive rescaling give `t=1`, `g=V/abs(t)`; the diagonal limit `t=0` is excluded from that normalization. All needed matrices are defined here; no parent campaign is imported. The old face-transport and Dirac-gate quotations are preserved in the correction history as quotations, not as premises establishing a physical kinetic law.

The abstract calculation uses ordered spinless Jordan-Wigner Fock modes on the coarse vertices, with ordinary tensor composition. The auxiliary edge encoding has qubits on coarse edges, stars `B_i=prod_(e incident i) Z_e`, and signed Pauli edge operators in direction order `-x,-y,-z,+x,+y,+z`. For the edge i→j, start with X on that edge and multiply Z on edges ordered before it at each endpoint; write the Hermitian Pauli as `i^(x dot z mod 2)X^xZ^z`, with an additional minus for a negative-axis orientation. Thus `A_ij=-A_ji`. With `Q=i^k X^x Z^z`, multiplication includes `(-1)^(z dot x')`. The loop operator is `S_C=i^len(C) prod A` in cyclic order. Face and, on a torus, noncontractible loop eigenvalues determine a link-sign gauge class by spanning-tree recovery, exactly as constructed in the runner.

Every edge occurs twice in `prod_i B_i`, so this product is identity: identifying `B_i=1-2n_i` restricts this carrier to **even total occupation**. On the cube, one fixed loop sector has `2^(12-5)=128` states, matching the even subspace of the 256-state eight-mode Fock space. Odd-N Fock comparisons below remain valid abstract matrix comparisons; they are not encoded states of this edge carrier. A legal hopping loop can be considered with another spectator occupation when even parity is needed. No unpaired single-particle code state is asserted.

For connected graphs, a local sign gauge `G=diag(g_i)` sends `M` to `GMG`; fields with identical complete cycle holonomies are related this way. This is diagonal gauge conjugacy, not merely a site permutation. On an even cubic torus the face data leave three independent Wilson signs, hence eight gauge classes. Each class contains `2^(V-1)` raw sign fields. The eight representatives alone are not all raw fields.

The coarse coordinate is `v` at fine position `2v`. Define `eta_1=1`, `eta_2(v)=(-1)^v_1`, `eta_3(v)=(-1)^(v_1+v_2)` and the plain field `eta=1`. Their face holonomies are minus and plus, respectively. Link strength is normalized to one. `M_ij=eta_ij` on bonds and zero otherwise; `H(g)=-sum eta_ij(c_i^dag c_j+c_j^dag c_i)+g sum n_i n_j` in the ordered fixed-N occupation basis. For the free case `g=0`, bipartition conjugates `M` to `-M`, so `E_N` is the sum of either one-particle ladder's N lowest levels; `E_0(g)` denotes the lowest many-body eigenvalue at fixed N. In filling expressions V is the vertex count; the V in the traditional interaction notation g=V/abs(t) is the separately supplied density coupling. The supplied half-filled determinant, and the interacting lowest eigenspace where used, are state selectors for the calculation.

Lieb's background article, [The Flux-Phase of the Half-Filled Band](https://arxiv.org/abs/cond-mat/9410025), *Physical Review Letters* **73** (1994), 2158–2161, DOI `10.1103/PhysRevLett.73.2158`, discusses interactions and higher-dimensional periodic settings including cubic flux. Its hypotheses are not verified or used to certify these particular spinless finite calculations. The former blanket planar/free/no-cubic description is withdrawn.

## Theorem 1 -- the exhaustive cube at half filling

**Conclusion.** On the open `2x2x2` coarse cube, `8` sites, `12` bonds, `6` faces of `F2` rank `5`, at half filling `N = 4`, the fixed-occupation sector having dimension `70`:

1. Exactly `32` of the `64` face assignments are consistent flux sectors, flux counts `0, 2, 4, 6`, each realised by a link-sign field of that holonomy.
2. Comparing all `32` at `g = -2, -1, -0.5, 0, 0.5, 1, 2, 4, 8`, the all-`(-1)` sector is the **unique** minimiser at every one, by
   `0.192, 0.344, 0.408, 0.456, 0.483, 0.485, 0.407, 0.158, 0.025` to the next distinct sector.
3. At the twelve integer `g = -8, -4, -2, -1, 0, 1, 2, 4, 8, 16, 32, 64` the `70x70` integer characteristic polynomials give minimal polynomials of `E_0` over `Z` for both
   uniform sectors, of degrees `3, 3, 3, 4, 1, 4, 3, 3, 4, 4, 4, 4` (plain) and `5, 5, 5, 5, 2, 5, 5, 5, 5, 5, 5, 5` (staggered) -- for instance `x^3 - 10x^2 - 16x + 48` for the
   plain sector at `g = 2` and `x^2 - 48` for the staggered sector at `g = 0`. A `CRootOf` comparison of those algebraic numbers gives `E_0(-) < E_0(+)` strictly at all twelve,
   with no tie and no floating point anywhere.

**Proof.** Item 1 solves the `F2` relations among the six face generators, realises each consistent assignment as a sign field and checks its holonomy face by face, exactly. Item
2 builds the `70x70` real matrix of each sector at each `g` and compares lowest eigenvalues, `[numerical, 1e-10]`. Item 3 builds the matrix over `Z`, takes its characteristic
polynomial in `sympy`, extracts the least real root as a `CRootOf` with its minimal polynomial over `Z` (domain checked to be `ZZ`), and compares the two roots symbolically.

**Reading, not theorem.** Eight sites, four particles, a sign on each of six squares, and now a price for two particles sitting on the ends of the same bond. With that price
switched on -- at any of the strengths tried, and whether the price is a charge or a reward -- the arrangement with a minus on every square is still the cheapest of all
thirty-two, and at the twelve listed integer strengths the **two uniform sectors** are compared exactly; the all32 comparison remains the distinct nine-point numerical calculation.

## Theorem 2 -- the off-half-filled cube and exact branch boundary

At `N=2,6` (dimension28), all32 sectors are compared at the original nine couplings `g=-2,-1,-0.5,0,0.5,1,2,4,8`. Three two-flux sectors tie for the minimum at every sampled point; all-minus ranks `31,31,31,31,31,31,31,30,27` (zero-based). These are finite numerical comparisons, not an all-g minimizer theorem.

For N=2, the complete characteristic polynomials in `x` are exactly

```text
plain: x^4 (x-g)^3 (x^2-gx-4)^6 (x^3-gx^2-16x+8g)^3
minus: x^6 (x-g)^7 (x^2-12) (x^2-gx-12)^2 (x^3-gx^2-12x+4g)^3.
```

The least plain root is the least root of `p=x^3-gx^2-16x+8g`. To see it is below the least root `a=(g-sqrt(g^2+16))/2` of the quadratic, evaluate `p(a)=-12a+8g>0`; the negative-leading tail crosses before a. For g<0, `a<g<0`, and for g>=0, `a<0`, proving the sign in both cases. Thus that cubic's least root lies below all other factors.

The minus ground branch is

```text
E_minus(g) = -2sqrt3                         for g >= 0,
             (g-sqrt(g^2+48))/2               for g < 0.
```

For g>=0, the density operator is positive semidefinite and the g-independent factor `x^2-12` persists. Monotonicity above the g=0 ground value and that eigenvalue together certify the constant branch. For g<0 let `r=(g-sqrt(g^2+48))/2`. Then `r<g<0` and `r<-sqrt12`. For the remaining cubic `f=x^3-gx^2-12x+4g`, `f(r)=4g<0`. On `x<=r`, `f'(x)>=f'(r)=gr+24>0` because its derivative decreases up to `g/3` and `r<g/3`. Hence f has no root below r, and all remaining factors are higher.

In particular **g=-4 gives E_minus=-6**, refuting the original all-real-g constant-ground assertion. The uniform pair has the positive crossing `g=2sqrt3` on the repulsive branch. There is also the attractive equality `g=-sqrt6`, `E=-2sqrt6`: reducing p modulo `x^2-gx-12` gives `-4x+8g`, so a common negative-branch root requires `x=2g`, `g^2=6`, with only the negative sign in this branch. The factorization at that value and ordering above certify that it is a ground equality. No continuum statement about the all32 competitors follows from these two-sector branch facts.

## Theorem 3 -- the exhaustive 2x2x3 block

**Conclusion.** On the open `2x2x3` coarse block, `12` sites, `20` bonds, `11` faces of `F2` rank `9`, at half filling `N = 6`, the fixed-occupation sector having dimension `924`:

1. Exactly `512` of the `2048` face assignments are consistent flux sectors.
2. At `g = 0, 0.5, 1, 2, 4, 8, 16` the all-`(-1)` sector is the **unique** minimiser of all `512`, by `0.381, 0.401, 0.401, 0.311, 0.058, 0.0048, 0.00049` to the next distinct
   sector. Its ground state is non-degenerate at every one; the plain sector's is `2`-fold at every one, and the plain sector ranks `500, 500, 509, 511, 511, 511, 511` of `512`.
3. On the attractive side the all-`(-1)` sector is still the unique minimiser at `g = -1, -2, -2.3`, and at `g = -2.4` it is beaten by an `8`-flux class of `8` tied sectors,
   falling to rank `8`. Continuity brackets at least one change of the minimizer in `-2.4 < g_c < -2.3`; it does not certify uniqueness.
4. The uniform **pair** itself has no crossing among the fifteen sampled couplings on `[-64,64]`: `E_0(-) - E_0(+) < 0` at all `15` couplings scanned, the largest value being `-4.53e-05`. The attractive flip of item
   3 is a third sector overtaking both, not the pair reordering.

**Proof.** Item 1 is the `F2` relation count, exact. Items 2-4 assemble each sector's sparse `924x924` matrix from one precomputed hopping graph and take its lowest levels by
Lanczos at tolerance `1e-12`, `[numerical, 1e-9]`; the degeneracies are read from the three lowest levels.

**Reading, not theorem.** A second, longer box with a different number of squares, and the same answer: with the price switched on, the minus-on-every-square arrangement is the
single cheapest of all five hundred and twelve, and its cheapest state is unique while the plain one's is doubled. Turn the price into a reward and there is a strength --
somewhere between minus two point three and minus two point four -- at whose tested lower endpoint a different arrangement wins. Continuity brackets at least one crossing; uniqueness and the ordering at every more attractive coupling are not proved.

## Theorem 4 -- first order in V on the coarse tori

**Conclusion.** For the twist-minimised free half-filled sea of each uniform sector on the coarse tori `4^3, 6^3, 8^3, 10^3, 12^3`, with `A = sum_bonds (P_ii P_jj - P_ij^2)` the
Wick value of the interaction in that determinant:

1. Every sea is closed-shell, gaps `2.83, 0.54, 0.63, 0.47, 0.14` (plain) and `4.90, 3.46, 2.65, 2.14, 1.79` (staggered), the small `12^3` plain gap reported as such; `A/V` is
   `0.65625, 0.66427, 0.66505, 0.66541, 0.66592` (plain) against `0.62500, 0.63032, 0.63101, 0.63116, 0.63120` (staggered), so `Delta A < 0` at every `L`.
2. On `4^3` at the all-antiperiodic twist the integer hopping matrices satisfy `M^6 - 52 M^4 + 676 M^2 = 1152 I` (plain) and `M^2 = 6 I` (staggered) exactly, so both occupied
   projectors are polynomials in `M` with rational squared entries and `A(+) = 42 = 21/32` per site and `A(-) = 40 = 5/8` per site are **exact**. With
   `dE_free = 48 sqrt2 - 32 sqrt6` the only first-order crossing is on the attractive side, at `g_c = 24 sqrt2 - 16 sqrt6 = -5.250710`, exactly.
3. By the declared finite Brillouin-zone quadrature grids, using the closed forms `P_ij = <cos q_1>_occ` for the plain sea and `P_ij = +-(h(0) + h(2e_1))/2` with `h = (6 + W)^{-1/2}` for the
   staggered one, the finite-grid estimates of the limiting values are `A/V approximately 0.666263` and `0.631237` and the resulting numerical first-order crossing estimate is `g_c = -5.4639`, without a certified quadrature remainder.
4. Second-order many-body perturbation theory on `4^3` gives `dE(g) = -10.50142 - 2.00000 g + 0.44685 g^2`, whose positive root `g = 7.577` would predict a repulsive-side flip;
   neither the open eight-site cube nor the open twelve-site block proves or refutes a transition of this 64-site torus. This polynomial root has no established same-model nonperturbative interpretation and is a **truncation diagnostic** only.

**Proof.** Item 1 diagonalises each twisted real-space hopping matrix, forms `P` from the occupied columns and sums the bond terms, `[numerical, 1e-9]`. Item 2 verifies the two
integer identities at zero tolerance and evaluates `A` in exact rational arithmetic from the polynomial projectors. Item 3 is finite quadrature, `M = 400` and `M = 800`
agreeing to `1e-5`. Item 4 is independently checked by the unordered occupied/virtual pair-wedge formula given below, including the vanishing single-excitation term.

**Reading, not theorem.** Perturbation theory in the price, on boxes far bigger than the ones that can be solved outright, agrees: the first correction is smaller for the
minus-on-every-square arrangement, so switching the price on widens the gap rather than closing it. One order further on the 64-site torus gives a polynomial root. Results on different open graphs cannot settle whether that torus actually changes order.

## Theorem 5 -- the large-coupling structure

**Conclusion.** At strong repulsion on the cube at half filling:

1. `<n_i> = 1/2` on every site in **both** sectors, to `5e-14`, at `g = 4, 8, 16, 32`; the staggered moment `m^2` rises to `0.24945` (plain) and `0.24944` (staggered) against the
   Neel value `1/4` and the weight on the two Neel patterns to `0.99708` and `0.99704`, and the same rise holds on the `2x2x3` block, where the plain ground space is `2`-fold and
   the densities are degeneracy-averaged. The two sectors have equal one-site densities but different finite moments and Neel weights: at g=4, for example, `m^2=0.2181/0.1999` and weights `0.8347/0.7504`. The data describe finite quantum admixtures, not identical states or spontaneous symmetry breaking.
2. The `t^2/V` exchange is sector-**independent**: `g E_0 -> -6` in both sectors, and `g^2 (E_0(-) - E_0(+)) -> 0` along `-0.4216, -0.2109, -0.1055` at `g = 64, 128, 256`.
3. The whole surviving difference is order `t^4/V^3`. In `60`-digit arithmetic `g^3 (E_0(-) - E_0(+)) = -26.9815477888, -26.9953982475, -26.9988502688, -26.9997126114` at
   `g = 64, 128, 256, 512`, with local exponent `2.99926, 2.99982, 2.99995` and Richardson limit `-26.9999999999`. The exact finite effective-matrix calculation below independently gives `E_0(-)-E_0(+)=-27 t^4/V^3+O(t^5/V^4)` for fixed nonzero t and V/abs(t) tending to positive infinity. The value -27 contains both diagonal and tunnelling differences; it is **not** a scalar `9/4` price per face.
4. On the `2x2x3` block the finite strong-coupling samples have the same negative sign, `g^3 (E_0(-) - E_0(+))` running `-12.126, -11.921, -11.869, -11.856, -11.853` at `g = 16, ..., 256`,
   ending near `-11.853`. The historical guess `-320/27` remains an unproved numerical comparison, not an exact coefficient or an asymptotic certificate. The **negative sampled sign** is what the two clusters share.

**Proof.** Items 1 and 2 are direct diagonalisation, `[numerical, 1e-9]` at the listed couplings. Item 3 diagonalises the exact `70x70` integer matrices in `mpmath` at `60`
digits, so the difference of two nearly equal energies is not a double-precision cancellation; the exponent comes from successive ratios and the limit from Richardson
extrapolation in `1/g^2`. Item 4 is the double-precision `924x924` computation at five finite couplings; neither its limit nor a remainder is certified.

**Reading, not theorem.** Finite large positive couplings give nearly checkerboard occupations, with sector-dependent moments and weights. The effective two-state matrix below contains tunnelling between the two classical checkerboards. This does not establish immobility, a chosen physical ground state, or a broken-symmetry phase.

## Exact finite fourth-order matrix and independent MBPT normalization

For the cube N=4, write `H=gD+T`, with D the nonnegative nearest-neighbour occupation count. Its kernel consists exactly of the two checkerboards (bit patterns105 and150 in the declared order). In that two-dimensional space P let `U=T_PQ`, `B=T_QQ`, `R=(D_Q)^(-1)`. The runner constructs these from the actual many-body hopping entries in exact rational arithmetic. The Schur complement for eigenvalues near zero is `-U(gD_Q+B-E)^(-1)U^T`. Expansion, with `E=g^-1 K2+...`, gives

```text
K2 = -URU^T = -6 I;                 K3 = URBRU^T = 0;
K4 = -URBRBRU^T + 6UR^2U^T;
K4_plain = [[17/2,13/2],[13/2,17/2]],       eigenvalues 2,15;
K4_minus = [[-7/2,-43/2],[-43/2,-7/2]],     eigenvalues -25,18.
```

The finite D_Q has strictly positive gap, so the isolated low-energy cluster of `D+T/g` permits this analytic finite perturbation expansion. The two lowest branches are split at fourth order. Their leading difference is `-25-2=-27`, decomposed as diagonal `-12` and lower tunnelling eigenvalue contribution `-15`. Basis phases can change the signs of off-diagonal entries, but cannot turn their eigenvalue contribution into a scalar face operator. This derivation is cube-specific. It neither assigns the same operator to the larger block nor determines a physical phase.

For the 4^3 torus second-order coefficient, take unordered occupied pairs i<j and virtual pairs a<b in the actual free eigenbasis. With bond wedges `W_ij(x,y)=C_xi C_yj-C_xj C_yi`, define

```text
V_ab,ij = sum_(x,y bonds) W_ab(x,y) W_ij(x,y);
C2 = sum_(i<j,a<b) |V_ab,ij|^2/(epsilon_i+epsilon_j-epsilon_a-epsilon_b).
```

There are496 occupied and496 virtual pairs,192 bonds. The single-excitation matrix of the Hartree-Fock contraction vanishes numerically (below `2e-12`) in these two closed-shell cases and is explicitly checked. The pair-wedge sum gives `C2_plain=-1.8076798162013128`, `C2_minus=-1.3608276348795436`, difference `0.4468521813217692`; it checks the original ordered-index prefactor independently. The first-order difference is exactly -2 and the free difference is `48sqrt2-32sqrt6`. No re-fit or parent result supplies these coefficients.

## Scope, evidence, and open interfaces

The original18 check IDs and all their numeric tables remain, with corrected scope labels and strengthened coefficient/branch checks. All32 cube sectors are compared only at the nine GA couplings; the twelve exact GZ values compare only the two uniform sectors. All512 block sectors are compared at seven repulsive and four attractive sample values. The fifteen GW values are a finite uniform-pair check, not an interval certificate. The five tori supply free-state first-order perturbation theory, and only 4^3 supplies the displayed second-order coefficient. No result on a different graph refutes that torus's polynomial root.

The classical checkerboard kernel, finite ground-state averages, and asymptotic effective matrix are distinct statements. Ground selection, physical probabilities, permanent Record content, dynamics, flux transitions, absolute scale, and larger-volume phases remain supplied or open. Longer-range interactions, nonuniform density couplings, arbitrary other fillings, and continuum-coupling exhaustive sector orderings are not decided. Finite scans can guide those routes without excluding them or counting independent no-go walls.

Both current notes quote a repaired mathematical interpretation rather than adopt a historical parent's wider authority. The runner binds its own note, the current governing memo and current composition attribution context before computation; both real dependency APIs must derive this primary from its filename with zero local helpers. The actual final cache is required to match that source/input identity. Independent source review remains necessary; formal audit is deferred.
