# Finite-field energy lowering: full-component upper bound

Independent algebra review of root candidate: valid on a finite component with unique normalized groundψ, Hψ=E0ψ, full component gapΔ>0, Hermitian F with<ψ,Fψ>=0. Write Q=I−|ψ><ψ|, S=||QFψ||²=<F²>, R≥||QFQ||, ξ real and δ=E0−minspec(H+ξF)>0. Then

Δ ≤ ξ²S/δ + |ξ|R − δ.

Shift E0 to0. In P⊕Q, H+ξF+δ has blocks δ, ξv†, ξv, B=QHQ+ξQFQ+δQ, where v=QFψ. Let c=Δ+δ−|ξ|R. If c≤0 then Δ≤|ξ|R−δ, already no larger than the displayed bound. No inversion is permitted or needed in this case. If c>0, B≥cQ is invertible. A zero eigenvector of the full shifted matrix must have nonzero P component (otherwise B annihilates its Q component). Its Schur equation is δ=ξ²<v,B−1v>≤ξ²S/c. Multiplying by c/δ yields the result. This handles all cases and does not assume the perturbed ground overlapsψ without proof. The safe readily computable R=||F|| suffices.

This is a bound on the FULL gap in the selected component, not a lower bound, and not automatically the smallest energy with original Fψ overlap. Nonlinear finite-field perturbation can access states through QFQ which the original linear source does not directly excite. If restricting to a reducing symmetry sector, prove both H and F preserve it first and relabel its gap. No claim that finiteδ probes only a one-particle pole follows.

At meanF≠0, center F first; δ must be E0−[Eξ−ξ<F>], and the norm bound concerns Q(F−<F>)Q. Subtracting a mixed rather than pure mean is invalid. At δ=0 the displayed quotient is undefined; no positive-lowering bound is reported. For rigorous noisy-input propagation one needs certifiedδ≥δlower>0 and S≤Supper,R≤Rupper: the right side decreases withδ, so ξ²Supper/δlower+|ξ|Rupper−δlower is safe. Nominal stochastic error bars are NOT certified inequalities.

Preregistered actual864-state L2 finite eigensystems reused the declared geometry at V=.95,1, ξ=.05,.1,.2,.4. All eight inequalities pass numerically. V=.95 givesδ .000700843,.00281214,.01138975,.04786227 and bounds1.51782,1.58190,1.69685,1.87463 versus fullgap1.03054. RK gives bounds1.45233,1.51592,1.62892,1.79932 versusfullgap.969624. No ξ was retuned or selected after data. Larger fields improve absolute energy signal but weaken this safe norm bound in this fixture; this is an explicit robustness/sharpness tradeoff. The ξ→0 limit is the harmonic spectral mean for this source; finiteξ adds a norm penalty. Eight finite floating tests support implementation only, not interval certificates. No stochastic jobs were run.

The result could motivate a newly frozen finite-field calibration after independent review. It does not rescue the failed tiny-curvature production, prove a physical photon, select a component, or establish any lower gap bound. R=√8/2 here is the exact diagonal component maximum; its generic√Vol scaling makes a large-volume infrared use require a new cost/norm analysis.
