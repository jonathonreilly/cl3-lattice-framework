# Independent degree-(2,0) source review

PASS for DERIVATION2f7af929ac09b5a44d64b021eac93e6721f91b8d95d0bd274e82b5a6cf5e1684, conditional on the same native K, signed sources, vacuum covariance and Ward error identity as the reviewed degree11 source. No native data, scalar values, covariance or moments were evaluated. This review does not certify a numerical residual, precision sufficiency, or a sign result.

The recursion is correct. In B O2, the first nontrivial product reduces using d k d=4d-2k, and the second uses a d a=-d. Combining with the commutator of O2 gives exactly -2B+2i ak+i dv-i zd-2i kv-i aw. No generic quartic term is dropped. Separately [B,J]=-8gamma(a), while [H0,J]=-2gamma(v); hence the displayed M and Leibniz formula for Db are correct.

O2 need not equal its operator adjoint: it represents D²Omega only after acting on the reference vacuum. The cross nominal therefore must use O_C†. The proof does this explicitly. The same distinction makes the moment construction <Oi,Oj> correct rather than an unstarred polynomial product. Self-adjoint D on the stated finite local-polynomial vectors implies these are the real moments m_(i+j), with m6 obtained from ||O3Omega||². No unjustified identity Oi†=Oi is used.

All terms of O3 are quadratic in a,d,k,v,z,w. Their pairwise covariance table reaches omega5 but no higher absolute moment. Inner b and Db are at most cubic in this same set. Thus moment and residual closure on c,nu,omega5 is valid at degree(2,0). This relies on the actual native symmetry identities in the imported table, not on arbitrary Gaussian states or arbitrary skew K.

For the cross table, |h0|² has center coefficient6 and opposite-neighbor two-step coefficient-1. Signed opposite endpoint coefficients have product-1, so each split opposite pair contributes +1 to vA·vC. Perpendicular separations vanish by coordinate parity. Hence the printed ell sign is correct. The cross covariance is similarly eCA=ell*(nu/6-3c). The nominal involves only a,vA,vC,dA,dC,k, so its direct entries require c and nu only. Omega5 still enters candidate coefficients and residual certification; it has not disappeared from the overall method.

Both3x3 normal equations and the residual expansion have the correct shifted moments. Any rational candidate may be tested afterward, so coefficient rounding is mathematically permitted, but its algorithm and error guards must be frozen before a numerical run. The source correctly declines to assert closure for degree(2,1), cap sufficiency, or successful physical improvement.

Validation:9 independent tiny ordered-word Clifford checks using the reviewer's six-generator reducer and a different skew K: O0..O3 recursion, commutator, three polynomial Db identities, and adjoint nonidentity/involution. These do not evaluate native covariance or constitute altered native solver runs. No required source correction found.
