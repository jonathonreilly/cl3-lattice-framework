# A conditional volume-uniform electric-dominated gap for the actual compact SU(3) plaquette Hamiltonian

This is an application of an external stability theorem, not a new proof of generic gap stability. The supplied compact Hamiltonian and its trace convention come from block29. The fixed lattice spacing, a>0, v>=0 and mathematical time remain supplied. Put u=av. No spatial-continuum or arbitrary-coupling assertion is made.

## 1. Audited external import

Source: D.A. Yarotsky, *Quasi-particles in weak perturbations of non-interacting quantum lattice systems*, arXiv:math-ph/0411042v1, https://arxiv.org/pdf/math-ph/0411042. The assumptions and Theorems1–3 appear on printed pages2–4. They allow infinite-dimensional local Hilbert spaces, unbounded nonnegative selfadjoint onsite operators with a unique zero vector and gap at least1, and bounded selfadjoint perturbations of a fixed finite support range. The finite-volume restriction is exactly the whole-range inclusion rule in equation(3). The constants c1,c2 depend only on that range. Theorem1 supplies a unique finite-volume ground and excitation gap at least1-c2 epsilon when epsilon=sup||phi_x||<c1. Theorems2–3 supply the thermodynamic ground-state limit and its GNS Hamiltonian with the same gap.

Section2, printed pages6–10, reviews the argument using cluster amplitudes and a resolvent estimate; the paper explicitly attributes these preliminary theorems to earlier work and refers to its reference[23] for details. We import the theorem, not a claimed complete independent reconstruction of that proof. No finite local-dimension assumption, onsite upper spectral bound, or volume-dependent smallness is present in the stated hypotheses. We do not import its additional quasi-particle hypotheses or assert an explicit numerical c1,c2. Theorem2's selected limiting state and Theorem3's GNS sector suffice; a classification of every possible infinite-volume ground-state representation is not asserted here.

## 2. Exact outgoing-link cells and normalization

At x in Z^3 take H_x=L2(SU3)^tensor3, with factors U_(x,i), i=1,2,3, representing the positively oriented links from x to x+e_i. Every cubic-lattice oriented link appears once. This is a regrouping of link Hilbert spaces, not a restriction to class functions or gauge singlets at each cell.

In the trace-orthonormal convention of block29, K_e=(3/(2a))(-Delta_e). The fundamental Casimir is8/3, so a single link has its unique constant ground and first nonzero energy4/a. Consequently

 h_x=(a/4)sum_i K_(x,i)=(3/8)sum_i(-Delta_(x,i))

is nonnegative selfadjoint, has the unique normalized constant vector Omega_x, and has gap1. Its resolvent is compact, though the imported theorem does not require finite dimension or bounded h_x.

For i<j use the actual oriented plaquette

 W_(x,ij)=U_(x,i) U_(x+e_i,j) U_(x+e_j,i)^(-1) U_(x,j)^(-1),
 J_(x,ij)=ReTr W_(x,ij)/3.

The four link factors belong to cells {x,x+e_i,x+e_j}; the fourth geometric vertex x+e_i+e_j is not an additional tail cell. Group the three pairs i<j and subtract their constant scalar:

 phi_x=-(u/4)sum_(i<j) J_(x,ij),
 Lambda0={0,e1,e2,e3},  ||phi_x||<=3u/4=:epsilon.       (1)

The padded range Lambda0 is a valid common support. Each J is a bounded real multiplication operator with |J|<=1. The exact magnetic plaquette function is retained; there is no weak-field approximation. The formal scaled Hamiltonian (a/4)H differs from sum h_x+sum phi_x only by the magnetic constant per retained plaquette.

## 3. Honest fixed finite-volume family

For a finite cell set Lambda use all three outgoing links of every x in Lambda. This includes some boundary links ending outside Lambda. Retain the entire three-plaquette group at x only if x+Lambda0 is contained in Lambda. The finite centered Hamiltonian is precisely the imported theorem's equation(3). Adding (3u/4) times the number of retained anchors recovers the corresponding positive-deficit Hamiltonian.

This convention is not identical to retaining every individually supported plaquette. For Lambda={0,...,L-1}^3 the whole-group rule retains3(L-1)^3 plaquettes, while individual cell support would retain3L(L-1)^2. Their difference is3(L-1)^2. In particular, at L=2 the counts are3 and6. No boundary-equivalence assertion is used to hide this discrepancy.

Every retained plaquette is a closed loop in the actual finite link graph, whose vertices are all link endpoints. Local gauge transformations at those vertices preserve each plaquette trace and each electric Casimir. Dangling links pose no gauge-invariance problem. The kinetic operator acts on their full link Hilbert spaces as usual.

## 4. Uniform finite and GNS gap from the import

Choose

 0<=u < u_*=(4/3)min(c1,1/(2c2)).                    (2)

Then epsilon< c1 and c2 epsilon<1/2. The centered scaled model has a unique finite ground and excitation gap at least1/2, independently of Lambda. Restoring the scale and any removed scalar gives

 gap(H_Lambda)>=2/a.                                (3)

The scalar is removed only to meet the perturbation norm bound; the gap is always measured above the actual ground energy. It is not a claim that the original positive-deficit ground energy is zero. At v=0 the full unperturbed link-space gap is4/a; physical restriction may raise it.

For the fixed translation-invariant interaction in(1), Theorems2–3 give a limiting state and a centered GNS Hamiltonian. After multiplying its generator by4/a, its vacuum complement also has gap at least2/a. There is no numerical onset in(2): c1,c2 are unspecified positive theorem constants. This is a genuinely volume-independent conclusion, but only in this small-u regime and this fixed lattice model.

## 5. Finite physical sector contains the ground

The finite compact kinetic heat kernel is strictly positive on the connected product group. Bounded real multiplication preserves positivity improvement: choosing C at least the supremum of the potential, the positive Dyson expansion for K+C-(C-V) dominates e^(-Ct)e^(-tK). Hence the ground can be chosen strictly positive. Gauge transformations act by measure-preserving coordinate changes, commute with the Hamiltonian, and preserve positivity. Uniqueness of the normalized positive ground then makes it a gauge singlet.

There is also a group-theoretic check: a unique eigenline would furnish a continuous character of the finite product of vertex SU3 groups; such a character is trivial. Either argument supplies the missing ground-inclusion premise. The physical Hilbert space is reducing and contains the ground, so restricting to it preserves the lower excitation bound(3). No equality of the full and physical first gaps is claimed.

## 6. Infinite physical reduction without a hidden Haar assumption

For each finite-support gauge transformation g, the finite-volume ground states are invariant once their link variables are present. The thermodynamic state is therefore invariant. Its canonical GNS unitary is

 U_g pi(A)Omega=pi(alpha_g(A))Omega,

and fixes Omega. Finite-volume covariance and the weak-resolvent convergence in Theorem3 imply that U_g commutes with the limiting resolvent: insert alpha_g(A),alpha_g(B) into its matrix elements and use the finite identities before taking the limit. Thus

 H_fix=intersection_g ker(U_g-I)

is a closed reducing subspace containing Omega. The GNS gap restricted to H_fix is at least2/a. Local gauge-invariant observable vectors pi(A)Omega belong to H_fix. This conclusion does not require constructing an infinite Haar product projector.

For this particular compact onsite model one can additionally identify H_fix with the closed cyclic subspace generated by bounded local gauge-invariant observables. Here are the needed normality details, rather than assuming an arbitrary weak-star limit is normal. At one site x, remove h_x and every perturbation whose padded range contains x. There are at most4 such anchors. If E_rest is the ground energy of the remaining Hamiltonian, the vacuum-at-x trial state gives E_Lambda<=E_rest+4epsilon; the exact ground gives E_Lambda>=E_rest+<h_x>-4epsilon. Hence

 <h_x>_Lambda<=8epsilon.                            (4)

The same bound summed over any fixed finite set controls its local electric energy. Compact resolvent gives finite-rank low-energy projections, and the omitted probability is bounded by this energy divided by the cutoff. The local density matrices are therefore relatively compact in trace norm. Since Theorem2 fixes all bounded local expectations, their limit is a normal density matrix. This establishes local normality and strong continuity of finite-support gauge unitaries in the GNS representation.

Now approximate a vector xi in H_fix by pi(A)Omega with A local. Average A over the finitely many vertex gauge groups incident to its link support. The bounded local average remains on the same link support and is invariant under all local gauge transformations. Its GNS vector is the orthogonal finite-group average of pi(A)Omega. Since xi is fixed, averaging cannot increase the approximation error. Thus such invariant local vectors are dense in H_fix. This optional identification uses compact onsite resolvent and(4), beyond the minimal imported theorem hypotheses. The simpler reducing-fixed-space statement above remains sufficient for the gap.

## 7. Separate padding lemma for ordinary finite open graphs

The fixed whole-group family is not silently replaced in the thermodynamic argument. Nevertheless Theorem1 alone also proves the same finite gap for an ordinary finite open cubic graph containing all of its actual plaquettes.

Embed each graph link into its outgoing cell and enlarge to a finite set of complete three-link cells large enough to contain x+Lambda0 for every actual plaquette anchor. For this graph define an inhomogeneous phi_x^(graph) by summing only its actual plaquettes anchored at x; set all other terms to zero. This is allowed by the theorem's site-dependent perturbations. Each norm is still at most3u/4, and all nonzero padded supports are included in the enlarged volume.

No plaquette uses an added link. Hence the enlarged centered Hamiltonian factors exactly into the desired graph Hamiltonian and a sum of independent extra electric link Hamiltonians, up to the disclosed scalar. Its gap is the minimum of the desired gap and4/a if extra links are present. The theorem's lower bound2/a for that enlarged operator therefore implies the same bound for the desired open graph. Its unique ground and physical-sector restriction are handled as in Section5.

For each graph this is a legitimate application of the uniform finite-volume theorem. The interactions used in this padding construction vary with the graph, so we do not apply Theorem2 to that varying family or claim equality of its boundary thermodynamic states. The infinite GNS conclusion uses the fixed family in Section3. This distinction prevents the padding lemma from supplying an unstated boundary-independence theorem.

## 8. Checks and scope

The prospective finite checker verifies whole-group versus individual boundary counts for L=1,2,3, all actual oriented loop closures and cell supports, and the padded real-link/extra-link separation for ordinary open boxes L=1,2. It also checks the rational gap and norm rescalings. These checks do not estimate c1,c2 or prove stability by finite spectra. The analytical import is load-bearing and must remain explicit in any source package.

The conclusion extends the supplied compact Hamiltonian to an electric-dominated fixed-lattice volume family. It is not a spatial continuum Yang–Mills mass gap, not a result at arbitrary av, not a physical identification of a or v, and not a derivation of the Wilson action. No claim about quasi-particle branches or scattering is borrowed from the paper's later theorems.
