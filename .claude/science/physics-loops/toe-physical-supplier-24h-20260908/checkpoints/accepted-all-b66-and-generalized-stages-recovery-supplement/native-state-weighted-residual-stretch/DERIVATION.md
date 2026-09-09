# Finite commuting-majorant certificate for state-weighted propagation

Source-only provisional extension of parent state-weighted proof2c839. No actual matrices, inputs, spectra or native measurements are evaluated. This result supplies a finite certificate interface; it does not identify the physical Gaussian/Ward consumer inputs.

Let A=A* on C^m, L=R*R>=0 and specified X:C^k→C^m. Find a finite Hermitian W satisfying

 [W,A]=0, W-L>=0.

Then W>=0 and for every real s,

 ||R exp(-isA)X||_HS² <= Tr(X* W X).

Proof: exp(isA)L exp(-isA)<=exp(isA)W exp(-isA)=W; sandwich with X and trace. Operator norm uses λmax(X*WX) instead. No ambient ||R|| estimate or active spectral gap is used. The certificate can be strictly useful when ||R|| is large: A diagonal, L=diag(ε²,1), X=e1 admits W=L and residual ε for all time. Conversely A with offdiagonal mixing can rotate e1 into the leaking coordinate; W-L>=0 and commutation correctly prevent claiming the instantaneous ε forever.

This is a finite semidefinite feasibility problem with linear commutation and domination constraints and objective Tr(XX*W). It is always feasible (a scalar multiple of I suffices), but usefulness is not guaranteed. Exact polynomial W=f(A) supplies commutation automatically and avoids fragile numerical spectral projector labels. A proposed rational/dyadic W with an interval-certified residual commutator does not provide an all-time theorem unless commutation is exact; for a bounded window, a direct commutator error term is available below. Entrywise PSD certification may use exact rational LDL or a strictly positive verified preconditioner. A merely approximate eigenbasis is not itself a commuting certificate.

For approximate W with W-L>=0 and ||[A,W]||<=η, Duhamel gives

 exp(isA)W exp(-isA)<=W+|s|η I,

hence r_HS(s)² <= Tr(X*WX)+|s|η||X||_HS². This is a finite-window certificate and requires only finite A,W, not ||R||. It remains valid for either sign of time. The same operator-norm bound uses λmax(X*WX)+|s|η||X||². A certified upper bound on the finite commutator is necessary; an observed small commutator is insufficient.

## Explicit propagator/Poisson consumer

For an exact commuting certificate let ρ²=Tr(X*WX), x=||X||_HS. The parent real-time error is at most min(2x,|u|ρ). For t>0 set a=2x/ρ (ρ=0 gives zero error). Splitting the normalized Poisson integral at a yields the closed bound

 E(t) <= (tρ/π) log(1+(a/t)²) + (4x/π) atan(t/a).

This follows by integrating the bound on both signs, including the exact tail. It is valid without time truncation or an unknown residual outside a chosen window. A volume-uniform finite-input certificate with uniform x,ρ gives a volume-uniform vector bound. It is not a claim that such a certificate exists for the native inputs or that it controls an extensive many-body determinant.

With approximate commutation, r(s)<=sqrt(c+d|s|), c=Tr(X*WX),d=ηx². The Duhamel integral up to u is [(2/(3d))((c+du)^(3/2)-c^(3/2))] for d>0, and u√c for d=0. Cap by2x and insert into the same Poisson integral, or retain the parent's finite-S tail. This provides a directly computable one-dimensional scalar bound once c,d are certified. No spectral gap is introduced.

## Nonorthogonal interface without entrywise coefficient certification

For supplied S0,G>0,J*=-J,L=D+JG^-1J, B=G^-1J and coefficient inputs C, seek Hermitian W satisfying W-L>=0 and B*W+WB=0. Then exp(sB)*W exp(sB)=W and the exact state-weighted bound is Tr(C*W C), while input norm²=Tr(C*G C). These are congruence transforms of the preceding theorem. Approximate commutation should be measured in G-normalized norm: ||G^-1/2(B*W+WB)G^-1/2||<=η. Then the same error formula uses x²=Tr(C*G C). This explicitly separates unknown coefficient conditioning from the physical input norm. A verified inverse of G and finite PSD certificate are still required.

## Practical alternative: exact finite integrated residual

If A=Σλ λPλ is exactly spectrally resolved, define cλμ=Tr(X*Pλ L Pμ X). Then

 ∫0^u r_HS(s)² ds = Σλμ cλμ Φu(λ-μ),
 Φu(v)=(exp(iuv)-1)/(iv), Φu(0)=u.

The sum is real/nonnegative. Cauchy–Schwarz bounds the real-time propagation error by sqrt(u times this integral). Nearcoincident frequencies require an entire-function/sinc enclosure, not division of independent close eigenvalue intervals. This integrated route can beat a uniform majorant and needs no assumption that the largest residual direction is occupied. It is a new finite spectral computation, not available from current target-exclusion summaries alone.

## Remaining scientific input

Identify an explicit finite X or C whose propagated columns and initial projection errors suffice for the actual Ward/Gaussian observable, with a dimension-independent conversion to its error. Neither saved uniform leakage exclusion nor this majorant theorem supplies that identification. Positive W feasibility alone does not establish a useful tolerance. A proposed physical input factorization and numerical/analytic domination witness must be reviewed separately. No physical no-go or successful native propagation is claimed.
