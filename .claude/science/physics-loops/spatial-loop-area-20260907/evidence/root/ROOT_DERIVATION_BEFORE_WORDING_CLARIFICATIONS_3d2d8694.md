# Root independent marked-observable derivation

Frozen after the preregistration and before opening native's completed derivation. The marked-polymer route, its sources and candidate constants were discussed before either derivation; this is independent derivation, not a blind discovery. Primary's completed Taylor selection proof was read before this freeze. All results concern the supplied compact SU(3) Hamiltonian; no axiom selection is claimed.

## Imported mathematical input

Yarotsky, arXiv:math-ph/0412040, Section2, supplies a space-time polymer representation for small bounded perturbations of a classical product vacuum. Its Lemma3 gives ordinary activity bound epsilon^n. The marked-observable construction on printed page11 gives ||A|| epsilon^(n-m), with support size n and m marked sites. Its construction uses bounded-degree support graphs and binary excitation/insertion decorations. Fernandez–Procacci, arXiv:math-ph/0605041, equations2.7 and2.15, supplies the absolute pinned-cluster bound exp(a(gamma0)) under the Kotecky–Preiss incompatibility inequality. These are load-bearing imports, not new theorems here. Below we derive the required uniform observable prefactor and check the model mapping and complex continuation explicitly.

Primary sources: https://arxiv.org/pdf/math-ph/0412040 and https://arxiv.org/pdf/math-ph/0605041 .

## Exact range-vacuum mapping

Let each site x carry its three outgoing SU(3) links, with Hilbert space L2(SU(3)^3). Write k_x=(a/4)K_cell,x, with unique constant vacuum and gap1. The all-representation electric spectrum gives this gap; the fundamental energy4/a realizes it. Set Lambda0={0,e1,e2,e3} and h_x=sum_{y in x+Lambda0} k_y. Then h_x is diagonal in the product Peter–Weyl basis and has unique vacuum on its WHOLE four-cell support, with gap at least1. On periodic boxes each cell occurs four times, so sum_x h_x=aK. This duplication is essential: an onsite k_x considered as acting on four sites would not satisfy the required unique-vacuum hypothesis.

For u=av let phi_x(u)=-u sum_{i<j} J_{x,ij}, where J=ReTr(U_face)/3. Each of the three faces is supported in Lambda0+x and ||phi_x||<=3|u|. Hence sum(h_x+phi_x)=aH-uF, differing from aH by a scalar. For a sufficiently small fixed complex disk, these are bounded analytic perturbations of fixed unbounded positive h_x. The relative bound may be taken arbitrarily small with bounded remainder3|u|. Choose the paper's time step and then the disk so that its polymer epsilon is as small as required below. This is an existential threshold, not a numerical coupling estimate; it is not the3u/4 normalization used with a different theorem in block34.

Use periodic tori with each period large enough to avoid degenerate local faces. Constants below depend only on this fixed range and dimension, not on torus size, loop size or time length.

## Counting the marked object

Choose a connected set S of m cells supporting a bounded A. For a rectangular loop take every perimeter vertex as a cell, padding any unused corner by an identity factor. This is connected and m=P=2(R+S). A support containing {0} times S is connected on the paper's fixed finite-range space-time graph. That graph has uniformly bounded degree D, also on tori. A connected n-point set containing a prescribed point has at most max(2,D)^(2n) encodings: select a deterministic spanning tree and use its depth-first walk, of length at most2(n-1). One fixed mark contributes no additional freely positioned insertion; every ordinary local decoration specifies membership in insertion/excitation sets, with finitely many possibilities per support point because the range is fixed. Thus, after increasing one constant c>=1, ordinary polymers containing any prescribed point and marked polymers containing the fixed S both number at most c^n. Ignoring the requirement of containing the rest of S only overcounts. Infinite local Hilbert dimension contributes operator norms, not a sum over an uncontrolled list of internal basis labels.

## Absolute cluster sum, with a tail reserve

Choose epsilon so small that q=ce^2 epsilon<=1/4. Ordinary activities have |w_gamma|<=epsilon^n. For an additional convergence reserve define rho_gamma=|w_gamma|e^n and a(gamma)=n. At any space-time point,

 sum_{gamma containing point} rho_gamma exp(a(gamma)) <= sum_{n>=1}(ce^2 epsilon)^n = q/(1-q)<=1/3.

If gamma0 has n0 support points, summing over intersections gives the incompatible-polymer sum at most n0/3<=a(gamma0). The KP bound therefore controls the absolute pinned decorations by e^n0, even for an external marked root with zero ordinary fugacity; the same incompatibility estimate holds for its support. The marked root itself has |w_A|<=||A||epsilon^(n0-m). Multiplying each whole cluster by exp(total support count), including n0 for the root, yields the bound

 sum_{one-mark clusters} |weight| exp(total support count)
 <= ||A|| epsilon^(-m) sum_{n0>=m}(ce^2 epsilon)^n0
 = ||A|| (ce^2)^m/(1-q)
 <= ||A|| C0^m,

where C0=2ce^2 is a safe choice for m>=1. Unweighted sums obey the same bound. The reserve controls terms reaching a time or spatial boundary distance L by an exponentially small factor (with fixed-range conversion between distance and support count). It proves convergence uniformly on a smaller closed complex disk as the time endpoints recede and, for fixed S, as the periodic volume grows. This avoids inferring a uniform thermodynamic bound merely from finite-volume analyticity.

## Why the complex quotient is the correct object

For a finite time slab define Z_N(z)=<Omega0|exp(-2Nt0 H_c(z))|Omega0> and its marked numerator with A between the two equal factors exp(-Nt0 H_c(z)). The left factor depends on z, not conjugate(z); this is a holomorphic scalar sandwich. Bounded perturbation semigroups and the paper's inclusion–exclusion/excitation decomposition are analytic on the same complex disk. Their bounds use absolute operator norms and remain valid there. The finite polymer gas partition function equals exp(the convergent ordinary connected-cluster series): the equality holds near zero by the power-series identity and continues through the convergence domain. Thus Z_N is zero-free there, and cancellation of unmarked clusters in numerator/Z_N leaves exactly one marked cluster. The marked operator is single and is not replicated as an additional positive-fugacity gas species.

The preceding weighted absolute bound supplies the uniform limit F_A(z) and |F_A(z)|<=||A||C0^m. For real sufficiently small u, ground filtering gives the ordinary normalized ground-state expectation; the real positive ground state has nonzero vacuum overlap. Near zero at fixed volume the complex expression equals Tr(A P(u)) for the analytic rank-one Riesz projection. Analytic continuation supplies equality across the disk; a conjugated normalized vector is never used. The infinite-volume function is the locally uniform limit of these holomorphic functions and agrees with the selected periodic ground-state limit on real u.

## Selection and area suppression

There is also a clean multivariate formulation of primary's charge proof. Couple each oriented face character to its own complex variable, retaining both signs as independent variables. The finite-volume rank-one Riesz projection is analytic near all variables zero; its trace against a bounded W is well-defined. Independent center translations of each link commute with K and conjugate the perturbation by the corresponding face-charge phases. Uniqueness of the Riesz projection gives covariance of the multivariate Taylor series. Every nonzero degree-n monomial in the expectation of the oriented loop must therefore cancel its edge charge with n signed face boundaries over F3. This argument requires no trace-class free resolvent assumption.

Project to the rectangle plane. On an open infinite plane finite-support solutions equal the rectangle filling. On a periodic Lx by Ly plane they differ by a constant two-cycle, so at least min(A,LxLy-A) face insertions are necessary. Restrict A=RS<=LxLy/2 and a nonwrapping rectangle strictly within the periods. Therefore F_C has a zero of order at least A at u=0 in every such finite volume, and in its locally uniform infinite-volume limit.

For W_C=ReTr(U_C)/3, ||W_C||<=1. Fix u0 strictly inside the uniform disk above. Divide F_C by C0^P and apply the higher-order Schwarz lemma on |u|<u0. For real0<=u<u0,

 |omega_u(W_C)| <= C0^P (u/u0)^A.

The same estimate holds in the qualifying periodic finite volumes. At u=0 it is zero. The bound can also be capped by1 on the real axis. At fixed u<u0 and large rectangles it gives area suppression with a perimeter prefactor; it is not claimed useful numerically for every thin rectangle. No positive lower bound, exact string tension, temporal Wilson potential, physical confinement, continuum limit, arbitrary-coupling phase claim or TOE derivation follows. This is a controlled property of the explicitly supplied Hamiltonian with external convergence theorems.
