# Independent optimal-tau source review

PASS for proof968aebdc2b0574f187391ab65a216b2af1aa32ba7fe2944170d08e365c2e47c3 and sourcefreeze280781e5933d294b0866e89d7c99d4ee334bd94d5aaf814092cab6c2d262aa44. No actual rho, scalar or saved values read.

The reciprocal cubic coefficients agree with independent expansion. Positivity of the spectral measure makes B<=0,D>=0; equality of either forces support at delta and all three nonconstant coefficients vanish. For the nondegenerate measure the derivative quadratic has one positive and one negative root, giving the unique global minimum. The endpoint derivative8/delta³ integral(lambda-delta)² proves tau*>delta. This argument includes finite rho2 and does not assume a discrete spectrum. Both radical formulas are algebraically equivalent; the sign-of-C branch avoids subtraction of nearly equal positive numbers.

The implementation only proposes a parameter from supplied midpoint numbers. Its upper-root rounding may move tau either way depending on branch; no optimality enclosure is claimed. Clamping tau/delta and upward32-grid rounding preserve strict positivity and the declared2^22 upper bound. Every proposed tau remains valid by the exact majorant factorization. Full original directed moment intervals, including the lower rho1 endpoint for negative B, must be used again in the certificate. The old candidates/gap bound retain their guarantee for the SAME interval inputs. Arbitrary midpoint inconsistencies correctly fall back without pretending to be spectral facts.

Nineteen independent synthetic predicates cover a degenerate measure, two exact single-atom optima including tau1/2, a two-atom measure, endpoint derivative, inconsistent midpoint fallback, signed interval endpoint selection and nonpositive-tau refusal. No author controls were rerun.

Integration caveat: proposal.py has4096-bit input and65536-bit returned-intermediate limits, whereas the existing spectral runtime accepts32768-bit stored moment components. A future caller must explicitly enforce the narrower candidate cap (and choose a documented fallback/refusal) or separately justify a changed cap before freezing. It must not silently treat this source PASS as validation of enlarged arithmetic. Root independently re-evaluating a recorded positive rational tau need not reproduce an optimizer, but must enforce the frozen candidate/count/size policy and directed final bound.

This is a source theorem/algorithm review, not a numerical optimization or alpha result. No existing runtime was changed here.
