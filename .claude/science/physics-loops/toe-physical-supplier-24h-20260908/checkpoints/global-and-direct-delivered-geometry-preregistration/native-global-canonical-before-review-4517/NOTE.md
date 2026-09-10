---
claim_id: native_global_projector_certificate_note_2026-09-10
claim_type: bounded_theorem
claim_scope: "Supplied infinite native model: each positive-band local impurity projector difference has an explicit finite descriptor approximation with nuclear error below 2e-13."
upstream_dependencies:
  - native_finite_excitation_ward_note_2026-09-09
  - native_certified_local_green_scalars_note_2026-09-09
  - native_infinite_star_node_reduction_note_2026-09-09
runner: scripts/native_global_projector_certificate_2026_09_10.py
actual_current_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
proposal_allowed: false
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# A certified finite descriptor for the native projector difference

Claim type: bounded_theorem

**Status: conditional-support.** In the supplied infinite native model, for each perpendicular or opposite two-link impurity, the operator defined below approximates the positive-band projector difference with nuclear error strictly below \(2\times10^{-13}\). The authenticated exact ledger has upper bound approximately \(1.6655044211761766\times10^{-13}\). Its columns are exact mathematical descriptors. Their numerical wavefunctions, Gram matrices, occupation tails and Gaussian expectations have not been computed by this result. The full node coefficient \(\alpha\) remains open.

The model, reference and conventions are those of the [infinite node reduction](NATIVE_INFINITE_STAR_NODE_REDUCTION_NOTE_2026-09-09.md), [finite excitation Ward construction](NATIVE_FINITE_EXCITATION_WARD_NOTE_2026-09-09.md) and [certified local Green scalars](NATIVE_CERTIFIED_LOCAL_GREEN_SCALARS_NOTE_2026-09-09.md). In particular this is conditional on their supplied native Hamiltonian and original pure Gaussian reference; it is not a selection of a physical law from axioms.

## Operator and conventions

Use dimensionless \(H_0=iK_0\), obtained by dividing the physical Hamiltonian by \(h=2|t_{\rm hop}|\). Let \(U=[e_0,d_A]\), \(\|d_A\|^2=2\), and

\[
 H_A=H_0+UVU^*,\qquad
 V=2i\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
 \Delta P=P_A^+-P_0^+.
\]

The imported absence of zero atoms and trace-class resolvent estimates give

\[
 \Delta P=\frac1{2\pi}\int_0^\infty\left(F(s)+F(s)^*\right)ds,
 \quad F(s)=(H_A-is)^{-1}-(H_0-is)^{-1}.
\]

The sign is for positive bands. Let \(X_\pm(s)=(H_0\mp is)^{-1}U\). With

\[
 G(s)=U^*(H_0-is)^{-1}U=i\begin{pmatrix}sA&-2D\\2D&2sB_{\rm geo}\end{pmatrix},
 \quad D=(1-s^2A)/6,
\]

use \(B_{\rm geo}=A\) in the perpendicular class and \(B_{\rm geo}=D\) in the opposite class. Woodbury gives \(T=(I+VG)^{-1}V=iQ\), where

\[
 a=1-4D,\quad d=a^2+8s^2AB_{\rm geo},\qquad
 Q=\frac1d\begin{pmatrix}-8sB_{\rm geo}&2a\\-2a&-4sA\end{pmatrix}.
\]

For the physical scalar \(0\le A\le s^{-2}\), \(d\ge1/9\). The assembled midpoint is taken from the authenticated A interval intersected with this spectral range; an empty intersection refuses. Each Q entry is rounded to the nearest \(2^{-84}\), with upward ties. The actual operator displacement is charged. At a quadrature node with positive weight w, the contribution in columns \([X_+,X_-]\) is

\[
 -\frac{w}{2\pi}
 [X_+,X_-]\begin{pmatrix}0&T\\T^*&0\end{pmatrix}[X_+,X_-]^*.
\]

This is an explicit self-adjoint finite rank operator even without a numerical basis for its columns.

## Three analytic pieces

There are 18 panels \([4^j,4^{j+1}]\), \(j=-16,\ldots,1\), with the positive 21-node Gauss–Legendre rule on each: 378 nodes in \([2^{-32},16]\). Set \(\epsilon=2^{-32}\). Append the positive-band low correction

\[
 -\frac{3\epsilon}{\pi}X_0VX_0^*,\qquad X_0=H_0^{-1}U,
\]

whose local inverse columns exist by the imported three-dimensional estimates. Append the high correction

\[
 \frac1\pi\sum_{n=0}^{14}
 \frac{(-1)^n\left(H_A^{2n+1}-H_0^{2n+1}\right)}{(2n+1)16^{2n+1}}.
\]

The copied low-tail proof bounds its remainder by

\[
 E_{\rm low}=\frac29\frac{5439}{160}\,2^{-48}
             +\frac16\frac{867}{32}\,2^{-64}.
\]

The high-tail proof uses \(\|H_A\|,\|H_0\|\le6\), the rank-two perturbation and telescoping powers to give

\[
 E_{\rm high}=\frac18\left(\frac9{64}\right)^{15}
 \left(1+\frac{18}{64\cdot33}\right).
\]

For the middle integral, resolvent transport bounds F in nuclear norm on the right-half-plane Bernstein ellipse of parameter \(5/2\). For each ratio-four panel its center and semimajor axis are \(5a/2\) and \(87a/40\). The two transport factors give \((100/13)^2\), while the local/global resolvent bounds give the sum \(\sum aM(a)<155600/169\). Banach-valued Chebyshev truncation, positive Gauss weights and the Hermitian projector factor then give

\[
 E_{\rm quad}<6139\left(\frac4{25}\right)^{21}.
\]

The panel length is \(3a\); it is included. This is an operator quadrature estimate, not an inference from scalar quadrature accuracy. The complete derivations, domains and independent reviews are preserved in the paired packet. The total rank is at most \(4\cdot378+2+58=1572\) per impurity; this is an upper bound, not measured numerical rank.

## Certified inputs and actual ledger

A distinct preregistered acquisition produced authenticated 21-node geometry and 378 A midpoint enclosures using the reviewed explicit elliptic oracle. Every A full width passed \(10^{-30}\). Root and weight brackets have full width at most \(2^{-160}\). Before midpoint selection, weights are explicitly re-enclosed outward on the \(2^{-192}\) dyadic grid; the new actual radius is charged. Pole midpoints are unchanged, so every A value remains at its authenticated argument. The reciprocal of pi is enclosed by exact alternating Machin sums with 40 and 12 terms.

For absolute radii, the independently reviewed physical-column sensitivity estimate is

\[
 E_{\rm input}\le2^{27}\epsilon_A+2^{42}\rho_s+
 2^{13}\rho_w+5\epsilon_T+2^{12}\rho_{1/\pi}.
\]

It uses physical column bounds, the Woodbury inverse and nuclear norm perturbations. It does not require a numerical Gram factorization. The exact accepted ledger is

\[
 \|\Delta P-\widehat D\|_1\le
 E_{\rm low}+E_{\rm high}+E_{\rm quad}+E_{\rm input}
 <2\times10^{-13}.
\]

The analytic terms are approximately \(2.684\times10^{-14}\), \(2.097\times10^{-14}\) and \(1.18746\times10^{-13}\), respectively. The largest numerical charge is coefficient rounding, approximately \(2.584\times10^{-25}\). The copied exact rational result is authoritative; these decimal figures are for orientation. Rescaling the frequencies and Hamiltonians by h leaves the projector and its dimensionless nuclear error unchanged.

## Evidence and open work

The A acquisition ran once after remote checkpoint77; coefficient assembly ran once after remote checkpoint78. Their external wall times were 16.49 and 4.73 seconds. The latter emitted all 756 coefficient blocks and 3407 durable events. Its independent root implementation reconstructed every coefficient, rounding, weight, Machin and error-ledger relationship. It did not independently replay the native elliptic oracle; scalar containment and Gauss mathematics inherit their reviewed sources. Root receipts retain external memory/time measurements, exact hashes and scope.

The paired compact runner checks imported hashes, receipt relationships and exact scalar error/rank consequences. It does not rerun the native acquisition or full coefficient assembly. Checkpoint78 holds the exact scientific input closure; checkpoint79 holds the completed coefficient events and acceptance. Their verified remote commits and exact file hashes are in `REMOTE_RECOVERY_MAP.json`.

This certificate supplies a finite operator for later work. It does not prove that its mass lies in the existing selected span, that state-weighted residuals are small, or that the full Ward correction has a particular sign. Full integration pipeline, changed-audit-evidence readiness and formal audit are unrun. Source review and delivery are separately recorded; no retained status is granted here.
