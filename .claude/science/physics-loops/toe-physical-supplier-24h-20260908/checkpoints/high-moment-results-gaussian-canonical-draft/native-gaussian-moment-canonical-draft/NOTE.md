# Gaussian jets and certified local high moments

Claim type: bounded_theorem

Status: conditional mathematical bridge and accepted scalar/high-moment certificates. Canonical review is pending. Full pipeline, current-main combined validation, changed-audit readiness and formal audit are UNRUN.

For the supplied dimensionless native Hamiltonian, the negative free spectral projector and the original reference normal-order convention, the accepted computation encloses the P/O impurity moments of orders seven through ten. Both classes meet the fixed full-width pilot target (10^{-6}); the largest reported width is about (1.848\times10^{-19}). This is a moment certificate. It does not establish a Ward error target, the sign of alpha, or a Gaussian state approximation.

## The conditional Gaussian bridge

Write (h_0=iK\), (P=1_{(-\infty,0)}(h_0)\), and (V=2i(ad^*-da^*)\). Keep the original reference scalar subtraction in (D\). The relative one-particle operator is

\[
U(t)=e^{t h_0}e^{-t(h_0+V)},\qquad
Z(t)^2=\det\bigl(I+P(U(t)-I)\bigr),\quad Z(0)=1.
\]

Thus \(\log Z=\tfrac12\operatorname{Tr}\log(I+P(U-I))\), and \(m_n=(-1)^n n![t^n]Z(t)\). The factor one half and the reference scalar are essential. Replacing the scalar by the impurity ground-energy shift would change the problem.

The imported infinite-volume proof controls the relative trace-class perturbation and its analytic germ, using bounded free propagation, finite-rank Duhamel terms, strong finite-volume convergence and convergence of the local negative covariance. The supplied free zero set has Haar measure zero; no positive free spectral gap is assumed. The finite determinant identity alone is not the infinite-volume justification. The complete conditional argument and its independent review are retained in the proof packet.

## Why degree ten needs only finite low-degree tables

Set \(U-I=\sum_{n\ge1}A_n t^n\). The exact recurrence is
\[
 nA_n=[h_0,A_{n-1}]-A_{n-1}V,
\]
with the constant identity included at order zero. The one-defect sector is \(L_n=-\operatorname{ad}_{h_0}^{n-1}(V)/n!\). Since \([P,h_0]=0\), its trace vanishes for \(n\ge2\). Remove that trace analytically before asking for a projected matrix entry; retain the one-defect operators in products with other coefficients.

Every remaining cumulant of degree \(n\ge2\) has at least two defect factors. Splitting at those factors bounds intervening free powers by \(n-2\). The sparse coefficient implementation therefore uses ordinary and projected two-source tables only through degree eight for (m_{10}\), without a Gram inverse. Its scalar Euler recurrence is \(nZ_n=\sum_{j=1}^n j\ell_j Z_{n-j}\). Accepted (m_0,\ldots,m_6\) determine the lower scalar coefficients and are reused; the new computation evaluates only orders seven through ten.

The P/O source table and its signed negative-band convention remain those of the pinned proof. In the opposite class a neighbor diagonal introduces a two-power radial shift. Hence this degree-ten calculation uses absolute odd moments through \(\omega_9\), and exact even radial moments through order ten. There is no requirement here for \(\omega_{11}\). The separately reviewed multisource and reflected-jet route is future work and is not part of this numerical certificate.

## Accepted suppliers and actual retained evidence

The new omega79 supplier reused the accepted 1742 Gauss nodes, represented by 3484 endpoint oracle evaluations in the original catalog, and made zero new oracle calls. It used the frozen positive-integral identities, low and high tail bounds, and 40-term tails with new exact moments M44/M45. The independent root reconstructed the node/tail/final arithmetic. Both \(\omega_7\) and \(\omega_9\) met their original full-width targets, (10^{-22}\) and (10^{-20}\). The complete supplier proof is copied; original node files are recoverable by the exact output hash inventory rather than duplicated here.

The high-moment producer reused the authenticated degree20 lower moments, scalar sources and even-moment records. An independent root reconstructed its A/Q coefficients, logarithm traces and new scalar coefficients from retained data using separate interval arithmetic. The successful packet has six files and 189 events, with eight new P/O moment intervals and both CERTIFIED_PILOT_WIDTH flags. The original lower moments and scalar supplier truth are inherited, explicitly; the root does not claim to have independently recomputed those native quantities.

The high-moment execution took 3.87 seconds externally, with 68,386,816 bytes external RSS and 119,685,120 bytes sampled tree peak, within the fixed 60-second/384-MiB protocol. The omega79 execution took 9.79 seconds within its 30-second/384-MiB protocol. Historical root receipts retain their external-pending field; separate ROOT_ACCEPTANCE files supply the completed external reconciliation. Neither historical receipts nor failed preparations have been relabeled.

## Compact verification and recovery

The supporting checker validates immutable imported bytes, accepted result/source/root identities, resource metadata, class/order census, canonical intervals and width flags. It hashes the retained high-moment events as opaque evidence. It does not replay node integrands, native Wick calculations or event arithmetic. Its small exact half-log fixture and coherent semantic mutants test the compact checker, not the native theorem.

IMPORTS.json maps each local copy to its exact original path and SHA-256. The original runtime freezes retain their full input closures; the local mapping identifies which copies this draft carries. Archive92 is 89025d1e4adb1ac54dc95706f91e8f71dc9e3880. Omega79 preregistration is bf4f60b2e52c9a41d9638eaba1740cb86f07e25e; high-moment preregistration is 0ac1cd2f075c8182358939bec5e01c2c2bc02928. The parent will add archive94 recovery for the new accepted high-moment outputs before canonical delivery. These preregistration commits are not asserted to contain later execution outputs.
