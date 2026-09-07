---
claim_id: gauge_wilson_finite_transporter_unitarity_pw_defect_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
bodyType: bounded_theorem
runner: scripts/gauge_wilson_finite_transporter_pw_defect_check_2026_09_07.py
upstream_dependencies:
  - gauge_wilson_compact_cube_finite_qubit_cutoff_bounded_theorem_note_2026-09-07
claim_scope: "Finite exact fundamental matrix-unitarity obstruction; actual full-irrep SU3 Peter–Weyl cutoff has sharp shell defect and energy-controlled distinct-link path approximation."
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

A finite nonzero link carrier cannot have both exact fundamental endpoint covariance and an exactly unitary3-by3 transporter matrix. This does not prohibit finite quantum-link models with exact continuous gauge symmetry. For the actual full-irrep Haar cutoff, covariance survives but the matrix-unitarity defect has norm exactly1 at every finite cutoff. Its support is confined to the top representation shell, giving a useful energy-dependent approximation for every distinct-link path, including arbitrary color/reference entanglement.

The [finite Peter–Weyl carrier source](GAUGE_WILSON_COMPACT_CUBE_FINITE_QUBIT_CUTOFF_BOUNDED_THEOREM_NOTE_2026-09-07.md) supplies the actual cutoff and all-label electric spectrum. The [static-source trial source](GAUGE_WILSON_UNIFORM_STATIC_SOURCE_ENERGY_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-07.md) is contextual: this theorem explains why its full-unitary energy identity does not automatically transfer to compressed hardware. No unbounded kinetic expectation is inferred from norm convergence.

The [canonical helper](../scripts/gauge_wilson_finite_transporter_pw_defect_check_2026_09_07.py) constructs the actual R=1 Haar multiplication compression on19 link basis states and3 colors, checks all57matrix columns with exact coefficients, and performs17 named checks. Its finite evidence is not a proof of the all-R theorem. The [durable packet](../.claude/science/physics-loops/finite-transporter-bridge-20260907/PROOF_REVIEW.md) preserves prospective contracts, complete proofs, exact raw matrices, initial R0 tautology correction, reviews and unchanged scientific port receipt. The first R0 check was strengthened to the literal vacuum compression before final evidence exposure; no physical fixture was retuned.

The complete native proof follows. Root's separately retained verification was informed by the native stronger total-energy path bound before writing, and is not labeled a blind derivation. Primary cold review and root verification both passed. The source makes a conditional mathematical statement about a supplied model, not a hardware compiler or an axiom-selected representation cutoff.

# Finite transporter unitarity obstruction and the actual PW cutoff error bridge

2026-09-07. Written after the exposed candidate and prospective contract, before reading root's completed derivation. This is a precise matrix-unitarity obstruction plus an actual full-irrep cutoff approximation theorem. It is not a prohibition of finite-dimensional gauge-covariant quantum links.

## 1. A Cartan trace-square obstruction

Let H be a nonzero finite-dimensional Hilbert space carrying the left endpoint SU3 action rho. Suppose a3-by3 matrix of operators U acts unitarily on H tensor C3 and has the exact fundamental pullback covariance. Restrict to g(t)=exp(itT), where T is any nonzero traceless Hermitian Cartan matrix. Write rho(g(t))=exp(itQ). With Qbar=Q tensor I3 and Tbar=I_H tensor T, the convention is

 exp(itQbar) U exp(−itQbar)=exp(−itTbar) U.

Only this commuting one-parameter subgroup is used, so no reversal of noncommuting group parameters is hidden. Differentiation gives [Qbar,U]=−Tbar U. If U is unitary, rearranging gives U Qbar U*=Qbar+Tbar. Taking finite traces of squares therefore gives

 Tr Qbar²=Tr(Qbar+Tbar)²=Tr Qbar²+dim(H) Tr T²,

because the cross term is2Tr_H(Q)Tr_3(T)=0. This is impossible. A first-trace argument alone would give zero and would fail. The opposite endpoint convention merely changes the sign of Tbar and gives the same positive square term. Exact endpoint covariance alone remains possible; exact matrix unitarity is the extra incompatible condition. In finite dimensions even one-sided isometry would imply unitarity and is equally excluded.

## 2. Actual Haar link and full-irrep cutoff

On L2(SU3) tensor C3 let (mathsf U psi)_i(g)=Σ_j g_ij psi_j(g). It is genuinely unitary. Let P_R be the orthogonal Peter–Weyl projection onto all matrix coefficients with labels p,q>=0 and p+q<=R, tensored with color identity. It commutes with both endpoint actions. Put U_R=P_R mathsf U P_R, acting on Ran P_R, and

 D_R=I_(Ran P_R)−U_R* U_R=P_R mathsf U*(I−P_R)mathsf U P_R.

Thus0<=D_R<=I. This is compression of the actual Haar multiplication operator, not a freely chosen finite quantum-link representation. Gauge covariance remains exact because P_R is a full-irrep projection.

Fundamental fusion is

 (1,0) tensor(p,q)=(p+1,q) plus(p−1,q+1) plus(p,q−1),

with invalid labels omitted. Hence multiplication by any g_ij takes p+q<=R−1 entirely into p+q<=R. The same holds for conjugate multiplication using the conjugate fusion rule. Consequently D_R annihilates the interior Ran P_(R−1). Since D_R is positive selfadjoint,

 0<=D_R<=T_R:=P_R−P_(R−1),                  (1)

and D_R=T_R D_R T_R. The left defect I−U_R U_R* has the same shell support by conjugate fusion.

The norm is sharply1 for EVERY R>=0. The normalized highest-weight matrix coefficient

 psi_R(g)=sqrt(d_(R,0)) g_11^R, d_(R,0)=(R+1)(R+2)/2,

belongs to(R,0), with norm1 by Schur orthogonality. Every g_i1 g_11^R is a matrix coefficient of Sym^(R+1)(C3), because all right tensor indices are the same first basis vector. This symmetric tensor representation is the single irrep(R+1,0); no antisymmetric/lower component survives. Thus U_R(psi_R tensor e1)=0. Since the original mathsf U is unitary, D_R has eigenvalue1 and ||D_R||=1. In particular ||(mathsf U−U_R)P_R||=1; there is no operator-norm approximation to the full transporter on all cutoff inputs. At R=0, U_0=0 and the energy denominator below is zero, so that case must be excluded from the low-energy bound.

## 3. Energy-priced one-link defect

For R>=1 define

 g_(R−1)=[R²−floor(R²/4)+3R]/a.

This is the exact minimum electric energy on the shell p+q=R, from E(p,q)=[p²+pq+q²+3p+3q]/a and maximal pq=floor(R²/4). Therefore T_R<=K/g_(R−1) on Ran P_R, and for a normalized state psi already in that cutoff space, with arbitrary reference/color entanglement,

 ||(mathsf U−U_R)psi||²=<psi,D_R psi>
 <=<psi,K psi>/g_(R−1).                       (2)

The expectation version holds for a mixed state by purification. It compares the exact unitary output to the unnormalized compressed output. It does not assert a deterministic normalized finite channel. The bound tends to zero for uniformly bounded electric energy because g_(R−1) grows quadratically in R, despite the exact norm-one defect on high-energy shell states.

## 4. Simple paths with shared color and arbitrary entanglement

Consider L DISTINCT links, each acted on once by mathsf U_e or its adjoint according to path orientation. Write W=U_L...U_1, P=Π_e P_(R,e), and let W_R be the corresponding product of compressed link matrices on Ran P. The color register is shared; its link matrices need not commute. However P_(R,e) acts as identity on color and commutes with every U_f for f≠e. Moving only such projectors gives the exact identity

 W_R=P W P.                                  (3)

For normalized psi in Ran P, the output error is consequently an orthogonal projection loss:

 ||Wpsi−W_Rpsi||²=<Wpsi,(I−P)Wpsi>.

The commuting output projections satisfy I−Π_eP_e<=Σ_e(I−P_e). For a fixed e, move its leakage projector past the later different-link unitaries and use(1) at the e-th step. Its shell projector commutes with all earlier different-link unitaries, so

 <Wpsi,(I−P_e)Wpsi><=<psi,T_(R,e)psi>.

No product assumption on link, color or reference states is used. Combining these identities yields

 ||Wpsi−W_Rpsi||²<=Σ_e<psi,T_(R,e)psi>
 <=<psi,Σ_(path)K_e psi>/g_(R−1).              (4)

Thus a TOTAL path electric-energy budget E gives error at most sqrt(E/g_(R−1)). A PER-LINK energy bound E_link gives the weaker requested sqrt(L E_link/g_(R−1)). A total full-system energy bound E also suffices whenever the supplied potential is nonnegative, since Σ_path K_e<=H. The two budget conventions must not be conflated.

Equation(3) is why an unnecessary sum of L square roots is avoidable. It relies on distinct links; a repeated-link path is not covered by this argument because a projection can no longer be commuted past another occurrence of its own link. It also explains why shared color entanglement causes no extra factor.

If epsilon bounds the right side of(4), the accepted output norm squared is at least1−epsilon. When nonzero, normalizing the projected output gives vector error squared2(1−sqrt(p))<=2epsilon relative to the exact output, where p=||W_Rpsi||². This is a conditioned output statement with its acceptance probability, not an automatic trace-preserving isometry. For general initial states outside Ran P one must additionally price initial projection/preparation; that cost is not hidden here.

## 5. Prior art and precise consequence

Primary quantum-link literature explicitly constructs finite link Hilbert spaces with exact continuous gauge symmetry: Chandrasekharan–Wiese, hep-lat/9609042, https://arxiv.org/abs/hep-lat/9609042 ; Wiese,2107.09335, https://arxiv.org/abs/2107.09335 . Their link entries are operator-valued with modified algebraic relations. Nothing here contradicts that established framework, its gauge covariance, or possible approximation/continuum routes. The no-go concerns simultaneous finite dimension, exact fundamental endpoint covariance and exact matrix unitarity. It does not establish novelty of a generic quantum-link obstruction, nor prohibit unitary time evolution of a finite gauge Hamiltonian.

For the actual full-irrep cutoff the theorem identifies the exact boundary defect and a useful energy-controlled approximation. It explains why block38's exact unitary open-line trial identity cannot simply be copied to finite hardware with U replaced by U_R: the compressed transporter is not an isometry on all inputs, and energy-form errors need their own control. State-vector approximation alone does not automatically bound an unbounded kinetic-energy expectation. Exact gauge covariance survives, low-energy transporter accuracy is available, and operator-norm unitarity convergence fails. No hardware compiler, continuum identification or axiom-selected cutoff is claimed.
