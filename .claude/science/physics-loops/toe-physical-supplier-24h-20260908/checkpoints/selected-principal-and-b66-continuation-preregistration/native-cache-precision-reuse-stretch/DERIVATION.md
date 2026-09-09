# Precision reuse for fixed native cache centers

Scope: source-only certificate design. No saved cache, history, selected labels, scalar data or index was loaded. The source formulae are affine in scalar inputs at FIXED exact rational poles s and weights alpha, with exact positive algebraic balances b=sqrt(alpha). Reusing this family does not change poles, weights, seed labels or the selected span. Tightening their uncertainties is a separate ledger; changing their midpoints requires a new family calculation. No physical precision or leakage target is asserted attained.

## 1. Recenter, do not merely reduce an error bar

Write an exact entry f(x)=a+sum_l b_l x_l. Let I_old=[l,u] be the authenticated outward arithmetic interval for f(m_old), not the previously inflated physical interval. For new certified scalar boxes x_l in [m_new,l-eta_l,m_new,l+eta_l], set Delta_l=m_new,l-m_old,l EXACTLY. Then

    f(x) in I_old + sum_l B_l Delta_l + [-e,e],
    e=sum_l sup|B_l| eta_l,

where B_l encloses the exact coefficient b_l, interval products are outward, and the new rounding allowance is retained. In particular the radius includes the old arithmetic uncertainty. Coefficient enclosure error multiplies BOTH the midpoint displacement and the new scalar radius. This remains true when coefficients contain square roots. It does not require the old midpoint to lie in the new scalar interval.

Equivalently choose the midpoint c of the translated interval, retain its halfwidth rho, and report c +/- (rho+e). This is a NEW entry certificate with the old row hash, old scalar midpoint hash and exact delta recorded. Old entries are immutable. Replacing eta_old by eta_new around the unchanged old center is invalid: f(x)=x, old midpoint 0, new exact value 1 is a counterexample.

To retain an unchanged chosen old point center c_old, a valid radius is sup|I_old-c_old| + sum sup|B_l| (|Delta_l|+eta_l), so precision gains can be lost to the displacement. To prove the exact new midpoint entry lies in I_old, it is sufficient to independently enclose f(m_new) inside I_old. Merely observing that translated intervals overlap is not sufficient. Normally translation followed by intersection with a fresh direct enclosure is preferable; both must enclose the SAME exact expression before intersection.

## 2. Actual sparse coefficients (h=1)

Read append_core.py in native-ward-insertion-append-design and core.py in native-minimal-first-action-append-design. Geometry uses their literal I,O,T,N=I+O. Let b=sqrt(alpha), sigma=+/-1. The following are coefficients in J; all corresponding G coefficients are zero.

* Ward insertion kind i=1,2 to pole source v: coefficient of c_minus is b sigma N_iv/(2s).
* Bare q_i to pole source v: coefficient of mu is -b O_iv/12.
* Bare q_i to center insertion v=0: coefficient of mu is -T_iv/24.
* Bare q_i to Ward insertion v=1,2: coefficient of c_minus is -N_iv/4, of mu O_iv/24.

Bare self and Ward self have no c_minus or mu dependence. Ward self G for i,j=1,2 has coefficient N_ij/4 of A(0), if that scalar is separately recentered. Common pole-pole cache has no c_minus, mu or A(0) dependence. Thus improved c_minus/mu certificates alone require NO common pole cache rebuild. In particular the original selected-principal Gram using only indices 0..398 has no mu dependence; mu first enters the added q DATA rows used for action.

For future B/B' corrections, the common endpoint L,L' formulae in cache.py/core.py are affine in B,B'. A/A' enter only C,C' for G. Unequal signed poles use the SAME divided difference denominator sigma*s+tau*t; exact zero uses the already-defined derivative branch. A common pair coefficient has at most four scalar terms; do not evaluate a near-zero denominator by a derivative substitution. Corrections obey the existing k=2 selector, symmetric G transpose and antisymmetric J transpose BEFORE the final radius is formed. Diagonal exact-zero J remains zero. Ward pole cross coefficients are affine in A,B,c; bare pole cross in A,B,mu. Woodbury inverse coefficients are NOT affine: if A midpoints change, these must be reevaluated with their separate inverse-residual certificate. No Woodbury reuse theorem is claimed here.

## 3. Gamma closure and low rank

Use the reader's exact block convention M((i,0),(j,0))=M((i,1),(j,1))=G_ij and its authenticated mixed-block sign for J. Apply correction with that selector, never symmetrize a wrong sign. J is skew and G symmetric, so the resulting closed Gram is symmetric and Gamma-covariant. This theorem is invariant to the global convention provided it matches the saved reader; a later adapter must explicitly pin and test that convention.

For c_minus/mu only, raw G is unchanged. Raw J correction is supported on rows or columns W={397,398,399,400,401}, at most five insertion rows; hence rank(Delta J)<=10 and the closed correction has rank<=20. For mu alone W={399,400,401}, rank<=6 raw and <=12 closed. Restrictions to selected rows can only reduce rank. These are correction-rank bounds, not claims that the full native Gram has low rank. A(0) adds a separate small symmetric insertion block. Physical input errors remain correlated affine errors; entrywise boxes may be used conservatively but do not establish exact PSD individually. The exact physical Gram inside the boxes is PSD by its source realization.

## 4. Costs and precision boundary

For an original24-pair trial, R<=96 and U=R union the eight closed bare-source labels <=104 count CLOSED labels (raw index, Gamma flag). Gamma pairing implies at most52 distinct raw indices. At most5*52-15=245 off-diagonal unordered raw J pairs touch the five-row W if all five are present; each raw J correction duplicates into two upper closed mixed-block entries by exact selectors. Diagonal J corrections vanish. The looser505=5*104-15 and1010=2*505 remain conservative bounds only for raw-formula pairs and scalar coefficient products per orbit; they are not counts of affected CLOSED entries or actual raw dimension. Five orbits therefore require no more than5050 scalar coefficient products under that loose bound. This excludes copying unaffected rows and the later matrix contractions. Computing directly the updated affected formulas costs the same order and avoids retaining the old arithmetic width; it needs authenticated s,alpha,A,B and geometry but no oracle or original full-cache builder.

For all scalar inputs, a safe full principal reuse budget is 5460 unordered pairs *2 channels *4 coefficients =43680 coefficient products per orbit, <=218400 over five. Gamma duplication needs selectors, not new scalar formulas. A new direct selected Gram can use the same pair set; recentering mainly preserves provenance and may reduce repeated scalar evaluation, not the asymptotic pair count. Either route must retain arithmetic uncertainty. Existing old per-entry rounding intervals impose a floor; an old global operator-radius gate does NOT justify a finer per-entry floor. Inspecting actual widths is a future authorized step, not performed here.

Prospective arithmetic: fixed 256-bit outward endpoints; exact rational scalar midpoints and deltas checked <=512 bits; exact coefficient expressions evaluated locally and rounded before accumulation. At most four terms per entry, no heterogeneous rational accumulation across rows. A conservative temporary 32768-bit cap and stored 4096-bit endpoint cap are explicit refusal gates, not promised to fit unknown accepted inputs. Positive poles and nonzero divided differences require exact certificates; sqrt(alpha) coefficients need outward root enclosures. Existing 192-bit arithmetic errors are carried, never overwritten by 256-bit formatting. No runtime or measured cost contract is supplied.

## 5. Required future bindings

Authenticate original scalar midpoint values actually used, original arithmetic rows (not only inflated reader output), exact poles/weights, selectors, accepted new scalar boxes and their root/post receipts. Record exact deltas, coefficient boxes, old/new row intervals and physical inflation separately. A missing old midpoint makes recentering NOTREADY. For existing compressed histories, changed tighter boxes describe the SAME physical midpoint-pole family but cannot retroactively change their stored pivot certificate; new downstream computations may use the tighter entry certificates, while continuation reuse must follow its own authenticated-history proof.
