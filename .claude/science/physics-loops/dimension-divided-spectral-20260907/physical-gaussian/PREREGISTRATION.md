# Exact dimension-divided Gaussian carrier spectrum and corrections

2026-09-07. Searched the Wilson campaign docs for Mehler and gauge-note Gaussian-sandwich/dimension-divided spectral formulas; no matching closed result was found. This is a scoped search finding, not exhaustive repository absence. Existing Schur normalization and compact-interior dimension cancellation remain closed work per OPPORTUNITY_REVIEW.md.

Freeze w=e^-Q, G0=S M_w S on the same Dirichlet A2 chamber, L=(dxx-dxy+dyy)/3,S=e^(L/2). The spectrum-equivalent B=M_sqrtw e^L M_sqrtw becomes the Euclidean wedge Gaussian kernel pi^-1 exp[-3(r²+s²)/2+2r·s], with the exact six reflected images. Derive its spectrum from a Gaussian/Hermite generating function, not a numerical Mehler fit. Candidate theta=(3-sqrt5)/2, anti-invariant degrees3+2a+3b, leadingtheta4, nexttheta6 simple. Verify normalization after the metric coordinate unitary and wedge reflection.

Derive the top and first-excited eigenfunctions of BOTH G0 and B by exact heat action. Candidate B top H exp[-sqrt5 Q/2], G0 top H exp[-2Q/sqrt5]; no candidate is assumed to be an eigenvector before checking. Use the degree5 radial Laguerre branch for the first excited state and verify that no degree4 anti-invariant mode intervenes.

Conditional on the newly reviewed GLOBAL dimension-divided multiplier and reflected heat bounds, plus a justified wall-quadrature/eigenbranch argument, calculate each relative beta^-1 correction as <u_i,P2(Q)u_i>+||Lphi_i||²/4, with normalized actual eigenvectors. Preserve all matrix/normalization factors. Compute radial moments exactly, no quadrature fit. Report the correction to the first/top ratio only if both branches are independently simple and the proof supports it. Distinguish this correctly normalized supplied ONE-LINK convolution from native H-weighted packet and unresolved multi-link spatial compression/physical mass gap.

Any symbolic runner uses180seconds/180MiB/BLAS1, with unique actual checks and no saved floating spectrum. Preserve failures rather than retuning candidates.
