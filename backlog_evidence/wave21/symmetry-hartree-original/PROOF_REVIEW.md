# Proof and interpretation review — original #7894/#7897

This is an independent original-source review of the six exact bodies in SOURCE_SELECTION.json, not a formal audit. The full source/claim read is complete; historical ancestor campaigns are explicitly outside acceptance. Findings identify repairs, not scientific disproof of the useful conditional constructions.

## #7894: finite encoding and conditional point maps

The source declares ordinary edge-qubit Pauli algebra, one fixed direction order, B stars, oriented A strings, face loops, hopping/current operators, a supplied KS sign field and coarse geometry. No program helper is imported. The finite Pauli algebra is exact over Gaussian rational coefficients. The cube has12 edge qubits and the 4³ torus192; these are different from the finite one-particle64/8-dimensional representations later in D.

For a point relabelling, the discrepancy between the permuted A string and the target A has the same X support cancelled and is pure Z. A diagonal Z product changes only phase, so it cannot create a nonzero residual Z support. This is a valid restricted Z-only obstruction. For a symmetric loop-free support matrix N, diagonal CZ conjugation maps X support x to X^x Z^(Nx), with phase2 times the number of graph edges internal to supp(x). The phase matters: the independent8-graph ×256-phased-Pauli dense comparison gives zero error in all2,048 cases; dropping the phase produces operator error2. This verifies the actual local conjugation implementation by an unrelated matrix method. The original runner then checks the finite maps, edge strings, cuts, stars, faces and polar current relations across its actual domains. It does not construct an all-axiom physical embedding or license an improper lattice symmetry.

The shift-parity result follows from eps(Mv+c)=(-1)^sum(c) eps(v) for a signed coordinate permutation M. The explicit finite maps and eta corrections preserve H_hop and change the sign of H_mass according to that parity. An operator identity for both coefficient components extends to all supplied real t,m on those geometries; it is not restricted to a few t,m samples. Corner inversion is available on the torus; not every torus map is an automorphism of the open cube, as A1 correctly records.

Every A string is real in the chosen representation. Ordinary complex conjugation reverses the explicit i in hopping; conjugating by all-edge Z reverses each A and restores hopping. The product equals the product of B stars on one bipartition. It is a real diagonal involution, so (Z_E K)^2=I. Pure-Z uniqueness here means the chosen action on every A, up to an overall scalar phase; it is not uniqueness among all antiunitary symmetries. Exact code preservation and the real cube projector are useful conditional finite facts. Neither K nor this equation supplies a physical time coordinate or a stochastic history law.

## #7894: spectral versus many-body operations

Let h(m)=h0+mE, with E real, E²=I and {E,h0}=0. Then K commutes with h(m), but E K sends h(m) to -h(-m). Therefore the stated spectral C and chiral E give the specified BDI relations at m=0. Their squares alone do not certify those Hamiltonian relations at nonzero m. In particular E h(m) E + h(m)=2mE. The actual64-dimensional control gives max error1.4 at m=.7, zero at m=0.

For the actual odd-shift mirror U, U h0 U^T=h0 and U E U^T=-E. Thus A=E U K anticommutes with h(m) at every m. Its observed square -I also persists at every m, since the operator does not depend on m. By contrast, the cube-centre U K maps h(m) to h(-m), commuting at m=0. A commuting antiunitary with square -I enforces equal-energy Kramers pairs; an anticommuting antiunitary pairs E with -E and only acts inside the same energy eigenspace at E=0. They must not be conflated.

The many-body source uses unitary particle-hole C, whereas its one-particle spectral C is antiunitary. Their CPT products consequently have different linearity and domains. In the actual Pauli representation, C times the odd-shift mirror preserves both H_hop and H_mass at fixed m. With corner parity, C and CPT instead flip the mass sign, exactly as the source table already prints. The reduced8-dimensional product +I at the massless Dirac point is a correct selected product, not proof that the full many-body CPT is identity or unbroken for every mass.

The8 explicit zero vectors and real reduction are directly checked. Gamma/chirality algebra has ±1 multiplicities4+4, so the text must preserve two two-dimensional doublets per handedness. The test of the corner scalar CPT works; uniqueness over the other listed improper maps is not implemented. The injected second scalar after D4 escapes every original D gate and the complete33-check run, while an independent scalar test detects it. This is a real assertion-coverage gap rather than a new physical theory.

## Fixed records, offdiagonal operators and histories

The pure-Z versus zero-Z-diagonal classification is a valid operator statement. It does not establish that offdiagonal expectation values are obtainable from correlations of the same fixed-Z records. |+><+| and |-><-| have identical complete computational-basis probability measures, including every classical joint function on those records, but opposite X expectation. The same logical issue holds for higher-dimensional offdiagonal operators. Different instruments/contexts or supplied dynamics can make a different experiment sensitive to them, but those are additional hypotheses.

Both notes quote the current minimal memo. Its probability clause concerns a forming site's supported possibility, not an arbitrary Fock joint Born distribution; its interpretive and qualification sections explicitly leave measurement basis, Born values, formation process, physical clock and observable bridges outside axiom content. A finite operator symmetry does not prove that a permanent-record history probability law exists or transforms covariantly. These boundaries need to appear where the positive interpretations currently assert them, not solely in a later disclaimer.

## #7897: exact conditional Hartree algebra

On a regular bipartite graph and the supplied ansatz <n_i>=1/2+eps_i O, the neighbor sum is z(1/2-eps_i O). The standard Hartree replacement gives

    V sum_<ij> n_i n_j -> (zV/2) Nhat - z V O sum_i eps_i n_i
                          - V(zN/2)(1/4-O²).

The last term includes V. It is even in O and fixes the usual double-counting constant. This produces exactly the declared staggered operator with m=-zVO; it is conditional mean-field algebra, not the exact interacting spectrum. The finite one-particle identity (h0+mE)²=h0²+m² and the supplied half-filled negative spectral projector give O(m)=-(m/2)c(m) when the diagonal/translation conditions used by the chosen torus hold. The original diagonalization checks this at two masses. Its source is fully redeclared; no parent campaign is needed for these algebraic steps.

The undivided equation is m[1-(zV/2)c(m)]=0. The trivial solution m=0 remains at all V. Because c(m)>0 and strictly decreases for m>0, a nonzero positive root exists uniquely once zV c(0)/2>1, with its negative partner. If the note claims the selected magnitude rather than only stationary roots, it must state the broken-branch/minimization criterion. For the specified bulk Hartree functional per site,

    F(m) = -1/2 <sqrt(E(q)²+m²)> + m²/(2zV) + const,
    F'(m) = m[1/(zV)-c(m)/2].

Monotonicity gives the conditional stability/minimum argument; none of this selects a physical record or derives V, t, eps, Fock space, readout or the Hartree approximation from the axioms.

## Bulk integral, finite grids and small-m asymptotics

The code's c_inf(m) is the continuous-zone average of (6+2 sum cos q+m²)^(-1/2). The Laplace identity x^(-1/2)=pi^(-1/2) int_0^infty s^(-1/2)e^(-sx) ds and factorization of each cosine average produce the written I0e integral. This is a useful analytic identity for a bulk model. It differs from finite antiperiodic sums; the runner correctly computes three distinct finite thresholds approaching the bulk value, despite its later contradictory captions. Fixed finite gapped sums are analytic in m² near zero and do not have a leading m² log m term.

The source's asymptotic claim is plausible and can be proved for the stated bulk integrand, but the provided finite ratios/slopes are not that proof. A short bounded repair is available. Near the unique zone node q=(pi,pi,pi), E(q)²=|r|²+O(|r|^4). In a fixed small ball, the radial leading difference is

    (1/(2pi²)) int_0^delta [r-r²/sqrt(r²+m²)] dr
       = (m²/(4pi²)) log(1/m) + O(m²).

The complement is analytic with O(m²) difference, and the Taylor error in E² changes the integral by O(m²); one can bound the remainder by splitting r≤m and m<r≤delta. Thus the logarithm is conditional bulk mathematics, not empirical extrapolation from three points. Substitution in the nonzero gap equation gives m² log(1/m) proportional to V-Vc to leading order, hence the stated square-root/log form within Hartree. An author may include this explicit argument or label the existing values as sampled numerical support. Either option must keep the original positive candidate and distinguish it from a physical interacting transition, a finite-grid exponent or a quantified lattice-approximation theorem.

Finite V does not make the Hartree state exactly classical: the original V=2 data give |O|=.457388<.5. The ratios approach1 only in strong coupling. The number xi=2/arccosh(1+m²/2) is the nearest-axis complex-root/amplitude-length comparison for the declared free staggered dispersion in coarse-site units (the unit cell spans two sites). It is not an interacting many-body correlation length, and a comparison with one lattice spacing does not set a necessary/exclusive Dirac window. Retain the numbers as labeled one-body/Hartree diagnostics.

## Exact finite interacting clusters

I reconstructed every matrix entry of the70-dimensional half-filled cube independently using bit transitions and parity between hopping endpoints. The result agrees exactly with the program's two-step Jordan-Wigner construction and interaction diagonal. Removing that occupation sign gives matrix error2 and is rejected. The original slab remains the12870-dimensional half-filled periodic-z model, with uniform degree4; the cube has degree3. Both have the local sign flux and C symmetry tested by full-basis algebra. On the nonregular open slab, complementing occupation changes the interaction by the degree-weighted occupancy sum; it is not constant on half filling, so the explicit C obstruction is valid.

Sector extraction spans both eigenspaces of the actual involution C. The two lowest eigenvalues per sector are sufficient for the total first gap in this decomposition when the computed eigenpairs converge; these are actual finite sparse eigencomputations, not random sampled Ritz subspaces. The original sampled ordering and numbers are preserved. But an even ground vector is fixed by C. It cannot be mapped to the orthogonal odd first excitation. The cube control confirms Cg=g and first overlap with Cg≈0. Its two extreme checkerboards have only.945750949 total occupation weight, so the finite vector is not exclusively their two-string sum.

The computed binomial free distribution and S=1/(2N) are supplied occupation-measure facts on the two named finite systems. Bimodality, finite central-difference response, S-doubling and the crossing are useful diagnostics. They neither define physical formation probabilities nor prove a phase. Different coordination, boundaries and shape prevent treating the cube/slab crossing as an interacting bulk critical benchmark for the z=6 Hartree model; the ratio2.41 is arithmetic, not a demonstrated Hartree error factor. The source already labels the h=1e-4 slab susceptibility at V=8 as saturation; retain that honest boundary.

## The zero-field counterexample and sign nonselection

At fixed finite size, H(h)=H(0)+h N O and ||H(h)-H(0)||≤N|h|/2. The positive gap at h=0 isolates the ground eigenspace, which varies continuously/analytically for sufficiently small h. C maps h to -h and O to -O, so the unique C-even state's zero-field expectation is zero. The claimed finite limit -1/2 cannot follow from saturation at one nonzero field. Actual calls to the original slab solver give the three shrinking values and residuals recorded in INDEPENDENT_CONTROLS.json. There is no need to simulate larger volumes to disprove this finite statement. A possible spontaneous-symmetry-breaking limit requires a separate specified order of infinite-volume and zero-field limits, unproved here.

The even Hartree functional gives ±branch degeneracy and the finite symmetry gives vanishing C-odd expectation in an invariant state. Neither theorem supplies an actual realized sign. Conditional on a declared joint occupation measurement/readout, a sampled configuration can have a signed staggered statistic relative to the supplied eps. That is a meaningful conditional reading. The six-edge encoding bridge is not computed by this Fock runner; a matching free scalar energy does not establish a unitary/state/observable intertwiner. It must remain contextual/unaccepted or receive a separate bounded proof, not inherit all older parents.

## Negative-scope and premise lenses

The Z-only repair obstruction is restricted and has the explicit successful CZ escape. The finite open-slab C obstruction has the periodic regular-slab alternative already executed. Symmetric finite state sign nonselection has the supplied-field and branch-selection alternatives, but physical registration/formation remains open. The Hartree single-channel ansatz leaves exchange/fluctuation/other ordering channels open; the work does not rule them out. Offdiagonal fixed-record nonreadability leaves explicitly supplied instruments/dynamics open. None of these walls has demonstrated all-other-axiom or pairwise independence, and no wall count is assigned. No source audit or retained grade is produced by this review.

Current axiom memo, realized-state note and primitive registry bytes equal the raw parent; the two actual helper consumers have since acquired unrelated registrations. The current APIs—not branch labels—find these two primaries, zero helpers and no scientific citations/declared inputs. No removed axiom or reserved source must be imported to repair the bounded finite unit. Physical conclusions beyond that boundary stay conditional/open.
