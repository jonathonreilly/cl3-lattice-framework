# Root independent structural and exact-spectrum review

Disposition: PASS for the supplied finite bare-Haar Wilson cube slab. This memo records root analysis from the prior campaign turn and the full reread on 2026-09-07 at approximately18:45UTC. It is a mathematical review, not an audit verdict.

## Hash-bound inputs

Native structural proof SHA256 86be606d8a1e3592e86707f22dc602ad74dbb9a953b82c301f7cb277cd8e7468.

Primary exact covariance/spectrum proof SHA256 6835262da0c3d9f6e8aa6c01699ccad8829761e3de421b721adf9fb608b8bb26.

## Structural checks independently reconstructed

A 15-edge spanning tree removes precisely the vertex gauge directions from the32-edge open four-cube; normalized Haar translation integrates its variables to1. The six chosen source-face tree edges form a forest, so both retained holonomies can be literal group coordinates after extending the forest. This validates exact global fiber integration; a merely linear source projection would not suffice. The two five-face cap identities restore the missing flatness constraints. Coordinate swaps and backtrack cancellation then prove every zero-action connection is gauge trivial, including noncommuting group transports. The same argument linearized proves the17-chord Hessian positive, independently of the exact determinant.

With Tr(TaTb)=delta, action quadratic coefficient is1/6, so each color covariance is3H^-1. There are136 real variables; partition scaling is beta^-68. Integrating120 nuisance variables and multiplying beta^-8/Z gives a bounded prefactor for the source density. Crucially, its nuisance-complement term is at most C beta60 exp(-gap beta); inside the scaled source window the exponential absorbs this prefactor into a Gaussian envelope. Therefore pointwise convergence implies actual L2 density convergence, not only weak or probability convergence. The source-chart complement has an amplitude bound C beta68 exp(-gap beta), which controls its Hilbert–Schmidt contribution.

The one-source Haar measure contributes beta^-4, and the isometric source dilation contributes beta^-2 on functions. Direct change of variables gives beta^-4 U_beta P A_beta P U_beta* kernel bar(p_beta)/sqrt(jx jy), tending bar(p_Sigma)/j0. This fixes both the exponent and the single j0 factor. Separate source conjugation averages are essential: gauge-fixed color alignment alone is not a central observable. The discarded chart complement vanishes after the same operator scaling. Compact self-adjoint perturbation therefore transfers fixed nonzero eigenbranches and norm, not a fixed-group strong limit.

## Exact constant and spectrum checks

The covariance result is independently reproduced on multiple complete spanning trees and an exact source Schur complement, with wrong-weight/restored-face controls. Root checked Sigma=3C, its inverse/determinant and a=8/135,b=23/270. For normalized Haar, the SU3 Weyl factor1/[6(2pi)^2], Cartan Gaussian Vandermonde integral24pi/sqrt3 and full8D Gaussian(2pi)^4 give j0=1/(16sqrt3 pi^5). There is no residual gauge volume or Weyl factor6 to insert.

Integrating the Gaussian kernel directly against exp(-omega Q/2) gives ground coefficient C[pi/(a+omega/2)]^4, omega=sqrt55/90. The resulting lambda0=sqrt3*pi*[11/(6(32+3sqrt55))]^4 agrees with the Mehler normalization. The invariant polynomial algebra has independent degrees2 and3. Commuting Hermite decomposition with compact Ad averaging yields degrees2a+3b and first excited degree2, so ratio theta^2 with theta=23/(32+3sqrt55). Multiplicity and central projection are stated correctly; no unprojected degree1 branch survives.

The beta6 vacuum-Rayleigh lower bound demonstrates that the leading norm asymptotic is not yet accurate there; it does not refute the asymptotic or bound the ratio error. The preserved failed tree iterator and failed prefactor simplification are correctly characterized as rejected controls.

## Scope and canonical-port condition

PASS covers the frozen derivations and exact constants. Canonical source port must preserve the proofs and separate dependencies without a cycle: structural general-H theorem first, numerical covariance/spectrum theorem second. Root has not independently rerun every arithmetic certificate in this memo; executed independent certificates are attributed to their authors. The finite action, bare source embedding and Haar law remain supplied; no physical coupling, thermodynamic limit, formation law, dressed source closure or TOE mass gap follows. Independent audit remains required.
