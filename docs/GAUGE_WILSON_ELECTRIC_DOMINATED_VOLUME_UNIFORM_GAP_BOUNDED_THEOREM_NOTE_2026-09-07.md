---
claim_id: gauge_wilson_electric_dominated_volume_uniform_gap_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
bodyType: bounded_theorem
runner: scripts/gauge_wilson_electric_dominated_volume_uniform_gap_check_2026_09_07.py
upstream_dependencies:
  - gauge_wilson_full_cube_compact_interacting_hamiltonian_limit_bounded_theorem_note_2026-09-07
  - gauge_wilson_compact_cube_low_electric_spectrum_ritz_gap_bounded_theorem_note_2026-09-07
  - gauge_wilson_compact_cube_finite_qubit_cutoff_bounded_theorem_note_2026-09-07
claim_scope: "Explicit Yarotsky stability-theorem application: small-av volume-uniform gap for supplied compact SU3 link models, every nontrivial local PW cutoff and a declared penalized finite-register extension; no numerical threshold or continuum claim."
---

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

An explicit mathematical stability-theorem import gives an excitation gap at least2/a for the supplied compact SU3 cubic-link Hamiltonian whenever av<(4/3)min(c1,1/(2c2)), with unspecified positive constants c1,c2. The bound is uniform in volume and, separately, in every local full Peter–Weyl cutoff R>=1. A declared penalty on unused qubit-code states extends the bound to the full finite register. These are fixed-lattice, supplied-operator results; a is the temporal-scaling kinetic parameter, not a derived spatial spacing.

The [compact Hamiltonian source](GAUGE_WILSON_FULL_CUBE_COMPACT_INTERACTING_HAMILTONIAN_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-07.md) fixes the operator and a,v conventions. The [all-label electric source](GAUGE_WILSON_COMPACT_CUBE_LOW_ELECTRIC_SPECTRUM_RITZ_GAP_BOUNDED_THEOREM_NOTE_2026-09-07.md) supplies the representation-wide Casimir minimum; its stronger finite physical-cube level is not needed here. The [finite-carrier source](GAUGE_WILSON_COMPACT_CUBE_FINITE_QUBIT_CUTOFF_BOUNDED_THEOREM_NOTE_2026-09-07.md) supplies the full-irrep projector, exact gauge action and memory dimension. The [exact helper](../scripts/gauge_wilson_electric_dominated_volume_uniform_gap_check_2026_09_07.py) checks35 finite geometry/scalar cases (28 original plus7 prospective supplements), not the imported stability theorem. The [durable packet](../.claude/science/physics-loops/volume-uniform-gap-20260907/PROOF_REVIEW.md) preserves timing, source corrections, original results and independent reviews.

# A conditional volume-uniform electric-dominated gap for the actual compact SU(3) plaquette Hamiltonian

This is an application of an external stability theorem, not a new proof of generic gap stability. The supplied compact Hamiltonian and its trace convention come from block29. The lattice remains fixed. Here a>0 is the supplied temporal-scaling kinetic parameter from block29, not a spatial lattice spacing; v>=0 and mathematical time also remain supplied. Put u=av. No spatial-continuum or arbitrary-coupling assertion is made.

## 1. Explicit mathematical import

Source: D.A. Yarotsky, *Quasi-particles in weak perturbations of non-interacting quantum lattice systems*, arXiv:math-ph/0411042v1, https://arxiv.org/pdf/math-ph/0411042. The assumptions and Theorems1–3 appear on printed pages2–4. They allow infinite-dimensional local Hilbert spaces, unbounded nonnegative selfadjoint onsite operators with a unique zero vector and gap at least1, and bounded selfadjoint perturbations of a fixed finite support range. The finite-volume restriction is exactly the whole-range inclusion rule in equation(3). The constants c1,c2 depend only on that range. Theorem1 supplies a unique finite-volume ground and excitation gap at least1-c2 epsilon when epsilon=sup||phi_x||<c1. Theorems2–3 supply the thermodynamic ground-state limit and its GNS Hamiltonian with the same gap.

Section2, printed pages6–10, reviews the argument using cluster amplitudes and a resolvent estimate; the paper explicitly attributes these preliminary theorems to earlier work and refers to its reference[23] for details. We import the theorem, not a claimed complete independent reconstruction of that proof. No finite local-dimension assumption, onsite upper spectral bound, or volume-dependent smallness is present in the stated hypotheses. We do not import its additional quasi-particle hypotheses or assert an explicit numerical c1,c2. Theorem2's selected limiting state and Theorem3's GNS sector suffice; a classification of every possible infinite-volume ground-state representation is not asserted here.

## 2. Exact outgoing-link cells and normalization

At x in Z^3 take H_x=L2(SU3)^tensor3, with factors U_(x,i), i=1,2,3, representing the positively oriented links from x to x+e_i. Every cubic-lattice oriented link appears once. This is a regrouping of link Hilbert spaces, not a restriction to class functions or gauge singlets at each cell.

In the trace-orthonormal convention of block29, K_e=(3/(2a))(-Delta_e). The all-representation Casimir result in block30, Section2, gives C(p,q)=(2/3)(p²+pq+q²+3p+3q), hence E(p,q)=[p²+pq+q²+3p+3q]/a for every p,q>=0. For a nonzero label this polynomial is at least4, with equality only at (1,0) and (0,1): it is strictly increasing under either coordinate increment, and those are the two minimal nonzero labels. Thus no unexamined representation lies below the fundamental/antifundamental energy. A single link has its unique constant ground and first nonzero energy4/a. Consequently

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


# Uniform gap on every nontrivial finite Peter–Weyl carrier

This supplement was derived after the clarified untruncated proof and its independent review; the root supplied the extension candidate. It uses the same explicit stability theorem, plus the block32 full-irrep cutoff construction. No claim about interchanging cutoff and volume limits is made.

For each fixed integer R>=1 retain on every link all matrix coefficients of SU3 irreps (p,q) with p+q<=R. Its dimension is D_R=sum d_(p,q)^2, with the exact polynomial supplied by block32. A cell carries three such links, dimension D_R^3. The onsite operator is the restriction of h_x=(a/4)sum_i K_(x,i). It retains the constant and both fundamental representations. The all-label Casimir bound proves that its unique zero vector and smallest positive energy remain exactly0 and1. Thus the imported onsite hypothesis holds uniformly in R, without a new spectral estimate.

Compress each actual grouped phi_x by the product of these local projections on its support. Compression cannot increase operator norm, so ||phi_(x,R)||<=3av/4. Selecting entire irreducible matrix-coefficient blocks commutes with both left and right group actions, hence with every local vertex gauge transformation. The projected interaction remains selfadjoint with the same three-cell actual support and four-cell padded common range. It is the compression of the supplied magnetic multiplication, not a replacement group-valued unitary.

The imported constants depend only on the common range, not on local dimension or an onsite upper spectral bound. Therefore the very same inequality av<(4/3)min(c1,1/(2c2)) yields gap at least2/a, uniformly in both finite volume and R>=1, for the corresponding full finite-carrier Hamiltonians. This is a uniform bound for a family, not a joint-limit theorem. For each fixed R, the fixed whole-group infinite interaction independently has the theorem's GNS gap at least2/a.

Positivity improvement of the unprojected heat-plus-multiplication operator need not survive compression and is not used here. The finite theorem gives a unique ground. Since the finite-dimensional gauge representation commutes with the Hamiltonian, its ground line is a continuous character of the finite product of vertex SU3 groups. Such a character is trivial. Hence the ground lies in the physical Gauss sector, which reduces the finite Hamiltonian and inherits the same lower gap. The limiting fixed-R state is gauge invariant; the previously proved GNS fixed-space argument applies unchanged. Local finite dimensionality makes local gauge averaging immediate, if the invariant-observable cyclic formulation is desired.

The separate finite open-graph padding lemma also survives at fixed R: added links are independent truncated electric factors, each with gap4/a for R>=1. No projected magnetic term uses an added link. The enlarged Hamiltonian therefore factors exactly, and its uniform lower gap transfers to the desired graph. This still invokes only the finite-volume theorem for the graph-dependent padded family.

R=0 is excluded from a nontrivial excitation statement because its carrier is one-dimensional. Furthermore the qubit statement is a storage/encoded-carrier statement: q_R=ceil(log2 D_R) qubits per link suffice, or three q_R per cell, with exact gauge representation on the code. If unused computational states are assigned inert zero dynamics, they can introduce extra ground vectors. The gap is not claimed on that enlarged unpenalized Hilbert space. Excluding the unused complement or adding an appropriate energy penalty is an additional implementation choice, not a consequence of the present gap theorem.

No local-state convergence as R tends to infinity, interchange with thermodynamic limits, efficient ground preparation, native control compilation, physical-parameter selection or arbitrary-coupling stability follows from this supplement.


# A supplied penalty extends the gap to the full finite qubit register

This is an additional mathematical hardware encoding, not a native control implementation. The root supplied the penalty candidate after the finite-PW supplement. Keep R>=1 and q_R=ceil(log2 D_R). Let W_R embed the full finite link carrier in C^(2^q_R), P_e be its code projector, and Q_e=I-P_e. Supply a penalty Delta>=4/a and define

 K_e^hardware=W_R K_(e,R) W_R*+Delta Q_e.

It has a unique zero vector, the embedded constant, and all other energies are at least4/a; a fundamental code state attains4/a. Regrouping three outgoing links therefore again gives an onsite gap1 after multiplication by a/4, independently of R, volume, or how many unused states the qubit register contains.

For each actual plaquette take its compressed Hermitian real-trace operator J_(f,R), and extend it by zero whenever any of its four link registers is outside its code. Denote that operator J_f^hardware. It has norm at most1, commutes with each local code projector, and acts only on the same four link registers. The centered grouped interaction -(av/4)sum_(three pairs)J_f^hardware thus has the unchanged common range and norm bound3av/4. Extend each finite link gauge representation trivially on Q_e. This is a genuine direct-sum representation of both endpoint groups; the penalty and every extended plaquette commute with it.

The same imported c1,c2 therefore imply a unique finite-volume ground and full-register gap at least2/a in the same small-av regime. To prove that this ground actually lies in the product code, rather than merely presume the penalty suffices against all interactions, interpolate

 H(s)=sum_e K_e^hardware+s V^hardware,  0<=s<=1,

where V^hardware is the supplied deficit potential or its centered version; their scalar difference is irrelevant. At each s the perturbation norm satisfies the same smallness condition, so the finite-dimensional ground projection is rank one and separated by a positive gap. It depends continuously on s by the resolvent spectral projection. Every P_e commutes with H(s), hence its expectation in that rank-one ground is exactly0 or1. The expectation is continuous and equals1 at s=0, where the ground is the product of encoded constants. It is therefore1 for every s and every e. This proves exact product-code membership at s=1 without an additional numeric inequality involving v and Delta.

On the product code H(1) is precisely the finite-PW Hamiltonian. Consequently its ground energy and ground vector agree with those of that carrier, while the full register—not just the code—has the stated lower gap. The unique ground is a physical singlet by the finite-product SU3 character argument; the physical reducing restriction retains the lower gap. The finite open-graph padding argument still works because the added register factors are decoupled penalized electric operators with gap4/a.

For each fixed R and supplied Delta, the fixed whole-group lattice family also meets the imported GNS theorem on finite-dimensional onsite registers. Its thermodynamic ground satisfies omega(P_e)=1 at every fixed link, by the finite ground-code identity. It inherits the full-register GNS gap and the physical fixed-space restriction. This is not an interchange of R and thermodynamic limits, and no convergence as R tends to infinity is asserted.

The penalty and zero-off-code operator extension are additional specified operators. Their existence preserves four-register support but does not provide a gate compiler, a native two-qubit interaction construction, a bounded switching schedule, or a preparation algorithm. The original inert-complement counterexample remains valid when this penalty is absent.
