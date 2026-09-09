# Raw-bank occupation certificates without natural-mode reconstruction

Source-only extension, no numerical data loaded. Parent supplied the polar-trace lemma; this note independently proves it and connects the actual reference-Gamma-closed rational bank. It avoids any S1-Lipschitz claim for square roots or operator absolute values.

## 1. Precise particle-hole convention

Let the doubled CAR one-body space be H with antiunitary charge conjugation Ccal, and P0,PA the reference and impurity positive-energy polarizations, satisfying Ccal P Ccal=I-P. The physical annihilation/creation Fock space of the impurity is built on PA H. All projector traces in this note are on the DOUBLED space; particle occupations count physical fermion modes in PA H.

For a principal paired block with two physical modes, the reference vacuum relative to the impurity vacuum is cos(theta)Omega+e^{i phi}sin(theta)a1†a2†Omega. The relative projector difference on the four-dimensional doubled block has eigenvalues +sin(theta),+sin(theta),-sin(theta),-sin(theta). Thus its S1 contribution is4sin(theta). The physical one-particle occupation matrix has eigenvalues sin²(theta),sin²(theta), and the sum of square-root occupations is2sin(theta). A fully swapped single mode contributes two doubled eigenvalues+1,-1 and one physical occupation1, so the same factor1/2 holds. Zero-angle modes contribute nothing. Summing the canonical principal blocks, justified by S1 summability, yields

 Tr_{PA H} sqrt(N)= (1/2)||PA-P0||_1.

This is not a claim that sqrt(N) varies S1-Lipschitzly with P. It is an exact two-projection identity. It includes finite fully swapped blocks and does not require a nonzero reference-vacuum overlap. The Fock parity of the actual state remains the one fixed by the implementer path; changing a swapped-mode convention is not permitted.

Define C=P0^- PA, with P0^-=I-P0, as an operator on the doubled space. Its nonzero singular values are exactly the sin(theta) physical occupation amplitudes, each repeated twice on a paired block and once on a swapped block. Consequently Q=|C|=(PA P0^- PA)^(1/2) is supported in PA H, equals sqrt(N) there, and Tr Q=half the doubled projector trace. With the imported native<87 bound, M=Tr Q<43.5. The creation/annihilation labeling must be interchanged consistently if a source defines its polarization as negative energy; the trace identity is invariant, not its unlabelled matrix entries.

## 2. Polar-trace lemma

Let C=U Q be the polar decomposition, Q>=0 trace class, and let Chat be any trace-class approximation with ||C-Chat||1<=eta. For any finite-rank orthogonal projection P and bounded positive Y,

 Tr((I-P)Q) = Tr(U* C(I-P)) <= ||C(I-P)||1
             <= ||Chat(I-P)||1+eta,                         (3)
 Tr(QY) = Tr(U* CY) <= ||CY||1
         <= ||Chat Y||1+eta||Y||.                           (4)

The left sides are real nonnegative. Cyclicity is legitimate for trace-class times bounded factors; ||U*||<=1. No commutation with P,Y is needed. If Chat(I-P)=0, (3) reduces to eta. These inequalities do not compare |C| and |Chat| in trace norm.

## 3. Actual rational raw-bank supplier

Write D=PA-P0. The exact fixed rational sign-quadrature candidate Dhat has the native weighted finite-rank representation F Cbar F*, including its particle-hole partner closure. Its reviewed error is ||D-Dhat||1<=eta. For the66-pole schedule, the analytic part is (357/25)2^-7+2*2^-4+429(4/25)^6; the separate prospective arithmetic allowance is1/200. The sum is<1/4. This is a theoretical certificate for the exact candidate plus its separately certified arithmetic approximation, not an assertion that the current cache has completed purification or weighted assembly.

Let W contain the raw rational and Ward columns and their reference Gamma images. Since P0 is an affine function of reference Gamma, W is P0-invariant. Then

 Chat=P0^- Dhat = P0^- F Cbar F*

is a finite-bank operator with ||C-Chat||1<=eta and right support contained in W. The identity C=P0^-D is exact. Crucially, Chat need NOT be multiplied by PA on the right. We are using it on the doubled ambient space as a trace-estimation device, not pretending it is itself a physical Fock one-particle map. Therefore its right support remains the already named raw W, without first constructing unknown PA-projected natural modes.

For an exact selected projection P=S G^-1 S* with S=F E and G>0, the explicit occupation-tail bound is

 tau_P <= ||P0^- F Cbar F*(I-P)||1 + eta.               (5)

This is a finite raw-Gram quantity plus an explicit analytic/input budget. For the entire W, the finite term is zero. For the actual24-pair selected span, it is generally nonzero and must be certified. No new original-source function is needed merely to define it: P0^- acts within the Gamma-closed raw bank, and all products use its existing exact Gram, coefficients, and selected-frame Gram. The available numerical enclosures may be too wide; no value is asserted.

## 4. Conditioning-free conservative finite bounds

No orthonormalization of ghost null directions is required to get an upper bound in(5). With Chat=A B*, use ||A B*||1<=||A||HS||B||HS. For example take A=P0^-F Cbar and B=(I-P)F. Both squared HS norms are finite traces built from F*F, F*P0^-F and F*(I-P)F=M-ME G^-1 E*M. Thus

 ||Chat(I-P)||1 <= sqrt(Tr(Cbar* F*P0^-F Cbar))
                         sqrt(Tr(M-ME G^-1 E*M)).

This factor bound is conservative and may be poor under cancellations. A certified singular-value calculation on the finite Gram products can improve it; no such calculation has occurred. The exact inverse G^-1 still needs a certified residual, but no entrywise C-width gate is introduced. This construction provides a concrete finite objective and a fallback bound rather than an undefined occupation eigenbasis.

For Y>=0 finite rank, factor Chat Y=A (Y B)* and apply the same HS product bound, or a certified finite nuclear norm. Formula(4) then supplies the occupation-weighted residual/evolution majorant with the additive eta||Y||. This can be combined with James's exact commuting majorant. Negative lower bounds from interval arithmetic must not be clipped into a claimed PSD certificate; true PSD structure and outward upper bounds are needed.

## 5. From the raw trace objective to Fock error

For any one-body error map E(t):PA H→PA H, the exact occupation-weighted squared column error is Tr(Q E(t)*E(t)). Weighted Cauchy applied to the Fock derivative gives

 ||(Gamma(T)-Gamma(U))Omega0|| <= sqrt(M) sqrt(Tr(Q E*E)).

The approximate physical map is U=PA V exp(-t|V*HAV|)V* restricted to PA H. The PA output projection is indispensable for calling Gamma(U) a physical Fock map. It is a contraction; removing it only enlarges the one-body error bound, since T stays in PA H. With P=VV*, the root Duhamel/Poisson bound applied to the abstract Hilbert-Schmidt column operator Q^(1/2) gives an initial weighted projection defect at most sqrt(tau_P), plus the weighted in-span propagation bound. Both terms can be bounded through (3)-(5), without constructing Q^(1/2) numerically.

Thus the missing input is reduced to explicit finite trace/nuclear-norm certificates of the existing raw bank and its exact coefficient matrix, not a list of unconstructed principal-angle vectors. Actual evaluation of Gamma(U) or inserted overlaps still needs PA-projected output cross-Grams; approximate projector coefficients and their errors provide a separate route. An error bound alone does not compute the approximating observable. The prior CAR insertion and scalar-Delta/Laplace telescoping rules remain in force.

The price of a coarse trace approximation is visible: even with the full W, the generic initial Fock bound is sqrt(M eta). eta near1/4 is much too coarse for a small final observable error. Improving scalar precision alone does not reduce this fixed analytic sign-quadrature tail. Possible future improvements are a stronger sign approximation, a sharper certified actual residual, or a consumer-specific estimate using eta||Y|| when ||Y|| is small. None is assumed achieved. This is a useful discriminant, not a forecast that the current24 span will pass.

## 6. Finite state alternative and phase

If a separately certified finite-excitation state Phihat approximates the exact input by epsilonPhi, contractivity yields an additional epsilonPhi when comparing Gamma(T)Phi to Gamma(U)Phihat (or2epsilonPhi when comparing both propagated originals via an intermediate finite-state pair). Its finite occupation matrix may be used directly; no continuity theorem for sqrt(N) is needed. Raw-bank finite-rank projector rounding can construct such a state, but its phase, parity, and approximation error require their own proof and numerical certificates. This note does not substitute that unfinished construction for(3)-(5).

No physical computation, precision adjustment of old outcomes, or alpha sign inference occurs in this extension.
