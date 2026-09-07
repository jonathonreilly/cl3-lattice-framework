---
claim_id: gauge_wilson_finite_pw_static_source_energy_upper_bound_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
bodyType: bounded_theorem
runner: scripts/gauge_wilson_finite_pw_charged_energy_controls_2026_09_07.py
upstream_dependencies:
  - gauge_wilson_finite_transporter_unitarity_pw_defect_bounded_theorem_note_2026-09-07
  - gauge_wilson_electric_dominated_volume_uniform_gap_bounded_theorem_note_2026-09-07
claim_scope: "Actual finite-PW charged path trial has an explicit ambient-volume-independent energy upper bound converging to4d/a for fixed distinct-link path and full physical ground premise."
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

For the actual full-irrep finite Peter–Weyl Hamiltonian, a compressed charged path applied to its full neutral physical ground has a volume-independent energy bound, not merely a state-norm estimate. The bound tends to the full-unitary trial cost4d/a as the cutoff grows for each fixed path. It requires a nonzero acceptance budget and uses the ground of the finite Hamiltonian itself.

The [transporter defect theorem](GAUGE_WILSON_FINITE_TRANSPORTER_UNITARITY_PW_DEFECT_BOUNDED_THEOREM_NOTE_2026-09-07.md) provides the exact shell leakage and distinct-link projection identity. Its explicitly open kinetic-energy bridge is repaired here by estimating the actual kinetic commutator. The [uniform weak-window theorem](GAUGE_WILSON_ELECTRIC_DOMINATED_VOLUME_UNIFORM_GAP_BOUNDED_THEOREM_NOTE_2026-09-07.md) supplies a unique physical FULL tensor-carrier ground in the stated regime; outside it that full-ground premise remains conditional. The mixed replacement trial need not be gauge invariant, so minimization only inside a constrained singlet space would not suffice.

The [exact support helper](../scripts/gauge_wilson_finite_pw_charged_energy_controls_2026_09_07.py) performs40 geometry, shell-energy, compression-identity and premise controls. Its abstract3-dimensional compression fixture is explicitly not a SU3 ground simulation. The [durable packet](../.claude/science/physics-loops/finite-pw-charged-upper-20260907/PROOF_REVIEW.md) retains both complete derivations, prospective contracts, the corrected root generator normalization, original and strengthened restricted-minimum control, independent reviews and identical-payload port receipt.

The [actual R1 helper](../scripts/gauge_wilson_finite_pw_actual_r1_charged_energy_check_2026_09_07.py) independently computes22 exact Haar-contraction and charged-energy controls on one four-link plaquette. Its full proof is appended. The fixed fixture has a projected trial excess strictly between4 and4.01 at a=1: the full-unitary exact-four identity fails. The sharper local-energy theorem succeeds while its optional worst-case replacement-budget condition fails; no parameter was retuned. This finite fixture does not establish the general theorem by sampling.

The complete analytical proof follows. The candidate formula was shared before independently frozen writeups. A displayed root generator convention was corrected from Tr(T_A T_B)=2delta_AB to delta_AB; the Casimir and every subsequent formula already used the latter. No cutoff or physical parameter was fitted. The result supplies no new lower confinement theorem, infinite-volume charged-minimum convergence or implementation of the nonunitary trial preparation.

# Volume-uniform finite-PW charged trial upper bound

2026-09-07. Root's proposed formula was exposed before the prospective contract. This derivation was written without reading a completed root proof. It repairs the specific missing form-energy bridge in block41, for the supplied finite Peter–Weyl Hamiltonian; it does not derive a hardware compiler or a physical coupling.

## 1. Model and the necessary full-carrier ground premise

Take a finite ordinary cubic link graph, at most four plaquettes incident to each link. The link Hilbert space is the complete Peter–Weyl sum p+q<=R, R>=1. Let P be its tensor product projection from the full Haar link Hilbert space. Put

 H_R=P(K+V)P on Ran P, K=sum_e K_e,
 K_e=-(3/(2a)) sum_A D_eA^2, V=sum_f V_f,
 V_f=v(1-ReTr U_f/3), 0<=V_f<=2v.

Haar is normalized, a>0,v>=0, and Hermitian generators satisfy Tr(T_A T_B)=delta_AB, sum_A T_A^2=(8/3)I. Full-irrep projection preserves both endpoint actions and commutes with K. Let Omega be a normalized ground vector of H_R on the FULL finite tensor carrier, of ground energy E_0. Assume Omega is neutral physical. The small-av regime of the reviewed uniform-gap theorem supplies a unique full-carrier ground, hence this physical premise. We do not replace minimization on the full carrier by minimization only in an arbitrarily constrained Gauss subspace.

Replace one link in |Omega><Omega| by its normalized Haar vacuum and retain the reduced density matrix on every other link. This is a legitimate mixed trial on the full finite carrier. All other kinetic terms and all nonincident face expectations are unchanged. Its link kinetic energy is zero. Each of at most four changed compressed positive face terms has expectation between0 and2v. Ground minimality therefore gives

 E_e:=<Omega,K_e Omega> <=8v.                 (1)

Thus E_path<=8vd for d distinct path links, and E_face<=32v for a four-link face. No ambient-volume norm appears. The replacement need not itself be gauge invariant; that is harmless precisely because Omega minimizes on the full carrier. At v=0 a restricted subspace excluding the vacuum would invalidate this inference: a positive-energy eigenstate can minimize there, showing why the premise matters.

## 2. Accepted charged trial and exact Rayleigh commutator

Let W be the ordered full fundamental transporter along a path with d distinct links, with inverse factors for reverse orientations. Regard W Omega as a matrix-valued function with Hilbert–Schmidt color norm Tr/3; this is the standard normalized external-source singlet contraction. Define C=P W P. Block41's exact distinct-link projection identity identifies C with the product of the compressed link transporters. Its exact endpoint covariance makes C Omega a vector in the external fundamental/antifundamental charged sector.

For e_R=[R^2-floor(R^2/4)+3R]/a, define

 theta=E_path/e_R, q=||C Omega||^2.

The shell/union bound gives 1-q<=theta. In particular theta<1 suffices for a nonzero charged trial. The charged variational energy excess satisfies

 Delta_R <= <C Omega,(H_R-E_0)C Omega>/q
          = <C Omega,[H_R,C]Omega>/q.         (2)

Every inner product here includes normalized color trace. H_R Omega=E_0 Omega holds in each color column. No derivative of a normalized, postselected output is inferred from a state-norm bound; we estimate the actual commutator in (2).

## 3. Kinetic contribution and its domain

All finite PW functions are smooth on a finite compact product group. Multiplication by the finite path word remains smooth. Therefore all kinetic and commutator expressions below are in their classical operator domains; there is no unbounded-operator limit interchange.

Since P commutes with K,

 [K,C]Omega=P[K,W]Omega.

Consequently its contribution differs from the full path identity by exactly

 <C Omega,[K,C]Omega>
 =<W Omega,[K,W]Omega>-<QW Omega,[K,W]Omega>, Q=I-P.

For each used link, sum_A D_eA^2 W=-(8/3)W. The cross term in the normalized trace of W^*(D_eA W) is zero, because it is a conjugate of plus or minus iT_A. Hence, even for complex scalar Omega,

 <W Omega,[K,W]Omega>=4d/a.                  (3)

The product rule is

 [K,W]Omega=(4d/a)W Omega
             -(3/a)sum_(e,A)(D_eA W)(D_eA Omega).

At each configuration the row operator with entries D_eA W has square

 sum_(e,A)(D_eA W)(D_eA W)^*=(8d/3)I.

Indeed each derivative is a unitary left/right product around plus or minus iT_A. The same identity holds for reverse orientation. Operator Cauchy–Schwarz, also on Hilbert–Schmidt color matrices, and the kinetic quadratic form give

 ||sum_(e,A)(D_eA W)(D_eA Omega)||
 <=sqrt((8d/3) sum_(e,A)||D_eA Omega||^2)
 =sqrt((8d/3)(2a/3)E_path).

Therefore

 ||[K,W]Omega|| <=4d/a+4sqrt(d E_path/a),

and using ||QW Omega||<=sqrt(theta),

 <C Omega,[K,C]Omega>
 <=4d/a+sqrt(theta)[4d/a+4sqrt(d E_path/a)].  (4)

Taking the real part if necessary is implicit in the upper estimate; the total Rayleigh numerator is real. The exact scalar/color-trace identity (3), not an operator identity on arbitrary color states, is the reason the full kinetic cost is exactly4d/a.

## 4. Only incident magnetic faces contribute

Write V_f^R=P V_f P. If f has no link in common with the path, its compressed operator commutes with C: it acts on disjoint link variables and is scalar in the shared color. Such faces contribute zero, exactly.

For a touching face, full scalar multiplication commutes with W. Inserting I=P+Q gives the exact compressed commutator

 [V_f^R,C]=P W Q V_f P-P V_f Q W P.          (5)

Let T_e=P_(R,e)-P_(R-1,e), and let T_f be the projection that at least one of the four face links lies in its top shell. Fundamental or antifundamental multiplication on each face link raises p+q by at most one. Thus Q V_f annihilates the subspace where all four face links are interior, and

 ||Q V_f Omega|| <=||V_f|| ||T_f Omega||
 <=2v sqrt(sum_(e in f)<T_e>)
 <=2v sqrt(E_face/e_R).                      (6)

The scalar part of V_f causes no leakage. This argument uses the actual face word, not arbitrary bounded potentials. In addition ||Q W Omega||<=sqrt(theta), ||P W||<=1 and ||C Omega||<=1. Equation(5) therefore yields

 |<C Omega,[V_f^R,C]Omega>|
 <=2v[sqrt(E_face/e_R)+sqrt(theta)].          (7)

There are at most4d distinct touching faces; double-counting them only weakens the bound. Neither (6) nor (7) uses a total-volume magnetic norm.

## 5. Explicit volume-independent result

Combining (2), (4), (7), for theta<1,

 Delta_R <= {4d/a
 +sqrt(theta)[4d/a+4sqrt(d E_path/a)]
 +sum_(f touching path)2v[sqrt(E_face/e_R)+sqrt(theta)]}/(1-theta). (8)

This is exactly a finite charged trial energy bound, not merely a vector approximation. A completely explicit sufficient version follows from (1). Put h_R=a e_R and theta_0=8avd/h_R. If theta_0<1, then

 a Delta_R <= {4d
 +sqrt(theta_0)[4d+4d sqrt(8av)]
 +8avd[sqrt(32av/h_R)+sqrt(theta_0)]}/(1-theta_0). (9)

For every fixed path and fixed a,v in the stated physical-ground regime, this tends to4d/a as R grows, uniformly over finite ambient graphs containing that path. At v=0 the bound is exactly4d/a already for every R>=1. For growing d at fixed av, h_R/d tending to infinity is sufficient for the relative correction to vanish; h_R grows quadratically in R. No specific numerical weak-coupling threshold is inferred.

The charged sector is nonempty when the trial is nonzero. The weak-regime full neutral ground premise implies a nonnegative charged excess, but no new charged lower bound is derived here. Unused-qubit sectors, a physical implementation of C, repeated-link paths, time evolution or infinite-volume convergence of charged minima remain separate questions. The input is the actual full finite ground, not the projection of an assumed untruncated ground. The result therefore repairs precisely the missing finite-carrier upper-trial bridge while retaining the model and preparation assumptions.


# Exact actual R1 charged-energy supplement

# Exact actual one-plaquette R1 charged-energy fixture

2026-09-07. This fixture was fixed prospectively before the exact Haar-contraction checker ran. All22 checks passed on the first execution. It corroborates a particular finite case of42; it does not prove the general volume-uniform bound by sampling.

## Actual neutral full-carrier ground

Take four independent Haar SU3 links around one elementary plaquette, complete PW cutoff R=1, and a=1. Write U for the path link and M for the oriented product of the other three links, so the loop is UM. U and M are independent Haar matrices, but the latter still consists of three distinct kinetic links. Exact Gauss invariance at each bivalent vertex forces all four loop representation labels to agree, with a unique intertwiner at each vertex. The neutral physical space therefore has orthonormal basis1, chi=Tr(UM), bar chi. It has electric energies0,16,16.

Actual fundamental fusion or direct Haar moments gives J=(chi+bar chi)/6 with zero diagonal and every off-diagonal entry1/6 on this basis. The source term is V=v(1-J). Set t=1/100 and v=96t/(1+t-2t^2), with N=1+2t^2. Then

 Omega=[1+t(chi+bar chi)]/sqrt(N), E0=v-vt/3

is an exact eigenvector of the3-by3 neutral Hamiltonian. The remaining eigenvalues are16+11v/6-E0 and16+7v/6, both larger. Further0<E0<v<4. Any nontrivial gauge representation is orthogonal to the global Haar vacuum and has K>=4, while PVP>=0. Thus no nonneutral representation can beat this neutral vector: it is an actual full tensor-carrier ground. This establishes the ground premise directly for the fixture, without assigning a numerical threshold to the separate weak-coupling theorem.

## Literal projected charged state

Use W=U along the single path link and define A=U, B=P(U chi), C=P(U bar chi). Complete-irrep projection of two fundamental coefficients is their antisymmetric part, while fundamental times antifundamental retains its scalar part. In indices0,1,2 this gives

 B_ij=(1/2)sum_(k,l,a,b)epsilon_ika epsilon_jlb bar U_ab M_lk,
 C_ij=bar M_ji/3.

A, B, C occupy distinct electric representation patterns and are orthogonal: respectively one fundamental path link, four nontrivial links with the path conjugated, and the three-link alternative path with the direct link in vacuum. Their electric eigenvalues are4,16,12. Their squared norms in the actual source convention integral Tr(F^*F)/3 are1,1/3,1/9.

The checker constructs these polynomials and evaluates every Gram and magnetic matrix entry by independent U and M Haar integration. It uses only

 integral U_ij bar U_kl=delta_ik delta_jl/3,
 integral U_i1j1 U_i2j2 U_i3j3=epsilon_i1i2i3 epsilon_j1j2j3/6,

the conjugate rule, and exact center-charge zeros. Unsupported moments raise an error rather than guessing zero. The resulting unnormalized J matrix is

 [[0,1/18,1/54],[1/18,0,1/54],[1/54,1/54,0]].

For example the B-J-C contraction contains36 nonzero epsilon products divided by1944, giving1/54. This is an actual SU3 projection calculation, not a freely chosen three-state Hamiltonian. Since A,B,C are already retained, their compressed magnetic matrix equals their full multiplication matrix elements.

## Exact trial energy and the sufficient-bound limitation

The projected charged state is (A+tB+tC)/sqrt(N). Put Qn=1+4t^2/9. Its accepted norm q=Qn/N and its unnormalized J numerator is(4t+t^2)/27. Its normalized energy is exactly

 Etrial=[4+(20/3)t^2+v(Qn-(4t+t^2)/27)]/Qn.

The exact excess Etrial-E0 is strictly greater than4 but less than4.01. This supplies an adverse example to simply copying the full-unitary exact4 energy identity into the finite carrier. It does not imply that this trial minimizes the full charged sector.

The actual local kinetic budgets are E_path=8t^2/N and E_face=32t^2/N, with e_R=4. The norm loss is14t^2/(9N), bounded by theta=E_path/e_R. The checker verifies the42 estimate using rational upper enclosures sqrt(theta)<=1/50, sqrt(E_path)<=3/100, and sqrt(E_face/e_R)<=3/100, each certified by squaring positive rational numbers. There is one touching face. Thus the exact trial excess is below the certified rational bound

 [4+(1/50)(4+4(3/100))+2v(3/100+1/50)]/(1-theta).

For this fixed prospective v, the cruder geometry-independent theta_bar=8v/e_R is GREATER than1. The fully explicit sufficient estimate based only on v therefore does not apply to this particular R1 fixture, while the sharper actual-energy version does. The fixture was not retuned to hide this limitation. It validates the useful local-energy theorem and demonstrates the conservatism of its optional worst-case replacement budget.
