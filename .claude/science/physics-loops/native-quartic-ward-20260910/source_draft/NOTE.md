# Quartic inverse-square envelopes for unchanged Ward trials

Claim type: bounded_theorem

Status: new saved-data estimator completed and independently reconciled. Both modes remain INDETERMINATE_SIGN. Canonical review is pending; full pipeline, current-main combined validation, changed-audit readiness and formal audit are UNRUN.

The accepted calculation applies a quartic spectral envelope to the original quadratic first polynomial and constant second polynomial. It changes the certified residual estimate while retaining those trials and their nominal. The resulting alpha intervals are approximately

| Original mode | E upper | F upper | Alpha interval |
| --- | ---: | ---: | --- |
| residual | 1.3838 | 66.6052 | [-465.2922, 609.3813] |
| variational | 1.1428 | 66.7061 | [-468.7459, 629.7689] |

Both intervals contain zero. Exact rational endpoints are in the immutable result packet. These intervals are not combined with a better enclosure from an unrelated signed-dual trial family.

## A positive quartic envelope

Use the supplied dimensionless bound \(D\ge\delta I\), with \(\delta=1/4\). For positive rational \(t,u\), define
\[
P(x)=(x-\delta)(x-t)^2(x-u)^2,\quad
B=(\delta t^2u^2)^{-1},\quad
A=B(\delta^{-1}+2/t+2/u).
\]
The constant and linear terms of \(1+P(x)(Ax+B)\) vanish, so
\[
Q_{t,u}(x)=\frac{1+P(x)(Ax+B)}{x^2}
\]
is a polynomial of degree four. For every \(x\ge\delta\),
\[
Q_{t,u}(x)-x^{-2}
=\frac{(x-\delta)(x-t)^2(x-u)^2(Ax+B)}{x^2}\ge0.
\]
Repeated parameters cause no singularity. The final fixed schedule uses all fifteen unordered pairs with repetition from \(\{1,2,4,8,16\}\). It is neither a continuous optimum nor a fitted search. The earlier proof's half-shifted prospective schedule is historical; the identity holds for all positive parameters.

Let \(p\) be the unchanged degree-two first polynomial and \(r=(I-Dp(D))\Omega\). With \(v=(1,-p_0,-p_1,-p_2)\), the seven exact convolution coefficients \(d_k=\sum_{i+j=k}v_i v_j\) give
\[
\rho_j=\langle r,D^jr\rangle=\sum_{k=0}^6d_k m_{k+j},\qquad 0\le j\le4.
\]
The new protocol reuses the accepted \(\rho_0\) and evaluates only \(\rho_1,\ldots,\rho_4\), using accepted moments through order ten. If \(Q=\sum c_jx^j\), the spectral theorem gives \(\|D^{-1}r\|^2\le\sum c_j\rho_j\). Since coefficients may be negative, each interval endpoint is selected by the coefficient sign. Correlations can widen this bound but cannot invalidate it. A negative certified upper is a contradiction and causes refusal; only a lower endpoint can intersect the known nonnegative domain.

The minimum over the fifteen valid upper bounds and the retained same-trial gap alternative is valid. No accepted trial is reoptimized or recomputed. There are two original modes and two P/O classes, hence sixty fixed quartic candidates.

## Coupled second residual and the posterior enclosure

Retain the original constant \(q_A\) and source residual interval \(t_A^2\). For each channel,
\[
F_A\le\delta^{-1}\bigl(\sqrt8 E_A+\sqrt{t_A^2}\bigr).
\]
Combine twelve P channels and three O channels by sums of squares. This step propagates the improved first-residual estimate into the second bound without asking for a new mixed-source kernel.

Let \(a,b\) be accepted upper bounds on the unchanged trial norms. With \(X=4\sqrt{15}\), \(V=32\sqrt{30}\), set \(\chi=\min(X,a+E)\), \(\psi=\min(V,b+F)\). The imported posterior theorem bounds the Ward error by
\[
\mathcal E=6\{E(a+\chi)+\min(Eb+\chi F,E\psi+aF)\}.
\]
Outward roots and arithmetic produce the certified new interval \([(N_- -\mathcal E)/8,(N_+ +\mathcal E)/8]\). Its intersection with the accepted same-trial posterior interval is retained. Empty intersection refuses. This theorem guarantees containment; it does not promise a sign or improvement for every input.

## Same-trial and scalar provenance

The loader authenticates three accepted families: original degree20, its posterior certificate, and the new high-moment pilot. Both later families must bind the exact original degree20 event/result pair. Original 255-event chronology supplies identical lower moments across the two modes, the original \(p,q,\rho_0,t^2\), and nominal. The high supplier's retained lower table must equal the outward fixed-grid mapping of those lower moments. Its new orders seven through ten then complete the same physical moment sequence.

Posterior mode inputs must match the original gate, q and source-norm identity. The unchanged nominal is checked against both accepted results. This is stronger than matching a mode name. The packet carries exact bindings and compact accepted source records; original event and scalar truth is inherited from their accepted calculations rather than claimed as new independent work.

The independent root separately reconstructed the source-to-INPUTS mapping, signed residual sums, closed-form quartic coefficients, all candidate expectations, channel roots and posterior enclosure. It uses separate arithmetic, with original scalar and trial truth explicitly inherited. The new output has 97 events and eight files. All eight output hashes and their membership are checked before and after reconciliation.

## Actual execution and portable verification

The fixed protocol completed once in 1.72 seconds externally, with 54,951,936 bytes external RSS and 101,793,792 bytes sampled tree peak, within 30 seconds and 384 MiB. The immutable root acceptance is separate from its historical external-pending receipt. No original oracle, native moment or trial computation was replayed.

The supporting compact checker verifies copied hashes, accepted root/worker/source identities, source-family linkage, resource fields, exact counts and mode copies. It checks ordered rational interval semantics, intersection, nonnegative error bounds and faithful indeterminate status. It hashes retained events opaquely and does not reconstruct their arithmetic. Six coherent metadata/interval/identity mutants reject; a small rational quartic factor test exercises the mathematical identity without accepted numerical inputs.

IMPORTS.json records exact original-to-copy hash correspondence. Runtime freezes retain the full transitive input inventory. Preregistration95 is 418d2e3c66e8cb6a99d3014149d2834c9e360e64; it is not asserted to contain later outputs. Archive96 recovery for the accepted result remains pending parent integration. Full source proofs and independent reviews are copied alongside the compact evidence. No worktree, graph or PR is created by this draft.
