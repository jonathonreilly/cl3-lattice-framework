# Root full physical cube transfer derivation

Provisional independent proof, awaiting exact geometry and critical review. The target is the supplied SU3 Wilson transfer on a finite spatial cube, not its one-loop source compression. All six spatial plaquettes are included with halfweight on each boundary, and all twelve temporal plaquettes have relative weight k. This is a stated change of supplied model. Axiomatic Wilson-action/time selection and an infinite spatial volume remain open.

## Exact Hilbert space and composition

Let H_link=L2(SU3^12, product normalized Haar), and H_phys its invariant subspace under SU3^8 local vertex gauge transformations. The spatial multiplier M_beta includes all six halfweights. The temporal convolution C_(k beta) is the product of twelve positive central Wilson kernels. It commutes with simultaneous local vertex gauge transformations: at each edge the right endpoint factors cancel, while the left endpoint conjugates the argument of the central kernel. M_beta is also gauge invariant. Thus T=M_beta C_(k beta) M_beta is bounded positive, preserves H_phys, and its restriction is a genuine operator there.

Fix a seven-edge spanning tree of the spatial cube. Tree gauge fixing maps the remaining five chord holonomies to product Haar, and leaves only simultaneous root conjugation. It gives an exact unitary J from H_cycle=L2(SU3^5)^(simultaneous Ad) onto H_phys. There is no independent conjugation of each chord and no replacement of this space by five class-function spaces.

Consequently (J* T J)^n=J* T^n J, because JJ*=P_phys and T preserves H_phys. In contrast to the earlier one-source embedding, this gauge-coordinate map is onto the entire physical Hilbert space; it discards no environment inside that space. Integrating the intermediate link variables in T^n glues the open temporal slabs and combines adjoining spatial halfweights into full spatial weights. No environment-reset premise is required. Time and boundary conditions remain supplied; no autonomous time-selection claim follows.

Restoring eight temporal Haar links in a one-step physical matrix element inserts the gauge average P_phys, which is identity on H_phys. Gauge fix the seven spatial tree links at each boundary and one temporal root link. Their union is a15edge spanning tree of the four-cube. The17 remaining product-Haar chords consist of five boundary chords at each end and seven temporal nuisance chords. The source kernel on H_cycle is obtained by integrating those seven nuisance groups and independently averaging simultaneous Ad at the two boundaries. It is not averaged independently in each of the ten chord groups.

## Exact quadratic boundary form

Orient the12 spatial edges and choose five fundamental cycle rows C with unit chord incidence, so C is5-by12 and its restriction to the five chords is I. Let F be the six-by12 oriented face-boundary incidence. Then F=B C, where B is the six-by5 matrix of face incidences restricted to chords. Define

    M=(C C^T)^-1,
    K=B^T B.

Both are positive. Every edge vector with fixed cycle integrals x has a unique minimum-norm divergence-free representative C^T M x. Its squared norm is x^T M x. Adding vertex gradients changes neither cycle integrals nor spatial curl. The full source boundary covariance follows by completing the Gaussian square over the seven temporal vertex potentials with the root fixed.

Specifically each color's quadratic action is1/6 times

    (1/2)x^T Kx+(1/2)y^T Ky+k(x-y)^T M(x-y)

plus a positive independent nuisance Gaussian quadratic form. The effective boundary Hessian is

    H_boundary=[[K/2+kM,-kM],[-kM,K/2+kM]].

The actual source covariance per color is3 H_boundary^-1. Its sum and difference covariance matrices are

    Sigma_plus=6 K^-1,
    Sigma_minus=6(K+4kM)^-1.

The numerical factor3 is fixed by Tr(TaTb)=delta and the Wilson deficit quadratic TrF2/6. No commuting replacement of the full action is used: this computes only its exact leading Hessian. The nonlinear saddle theorem requires its own localization proof.

## Spatial frequencies without a spectral fit

In coordinates z=M^(1/2)x, let L=M^(-1/2) K M^(-1/2). Its nonzero eigenvalues are those of F F^T, since F=B C and nonzero spectra of B(CC^T)B^T and (CC^T)B^T B coincide. Orient all cube faces outward. Each has four boundary edges; adjacent faces have one common edge with opposite orientation, and opposite faces are disjoint. Thus

    F F^T=4I-A_octahedron.

The octahedron graph has adjacency eigenvalues4 once,0 three times,-2 twice: the uniform vector gives4, vectors antisymmetric within each of three opposite pairs give0, and vectors constant on each pair with total zero give-2. Therefore the physical five-cycle eigenvalues are

    lambda_j=4 (three modes), 6 (two modes).

This proof also gives rank5 and positivity, without a numerical spectrum. The orientation of an individual face only conjugates F F^T by a diagonal sign matrix.

A fixed orthogonal diagonalization of L after the metric change gives, for each of eight color coordinates and spatial mode j,

    sigma_plus,j=6/lambda_j,
    sigma_minus,j=6/(lambda_j+4k).

Set r_j=sqrt(lambda_j/(lambda_j+4k)), omega_j=sqrt(lambda_j(lambda_j+4k))/6, and theta_j=(1-r_j)/(1+r_j). After the mode-dependent unitary oscillator-coordinate change w_j=sqrt(omega_j) z_j, the limiting Gaussian transfer divided by its actual ground eigenvalue is exactly

    exp[-sum_j t_k,j N_j],
    t_k,j=2 artanh r_j=2 asinh(sqrt(lambda_j)/(2sqrt(k))),
    N_j=(-Delta_(w_j)+|w_j|2-8)/2.

The fixed metric change acts only on spatial modes, and the oscillator scale is scalar in each color multiplet, so both commute with simultaneous SU3 conjugation. The Gaussian restriction to global Ad singlets is valid. Separate conjugation in each mode would change the physical Hilbert space and its excitation multiplicities.

## Haar amplitude and nonlinear interface

The full cube still has17SU3 gauge chords, hence136 real variables and partition scaling beta^-68. Integrating seven nuisance groups contributes beta^-28. There are40 real source coordinates at EACH boundary, so the normalized joint density scales beta40 and the one-source Hilbert-space dilation has factor beta^-10. The rescaled operator amplitude is beta^-20. The earlier beta^-4 one-chord operator exponent must not be carried into this model.

The normalized-Haar chart density is j0^5 per boundary before metric change. With z=M^(1/2)x, the one-boundary Lebesgue Jacobian is J_M=(detM)^4 (eight colors), so the Gaussian operator kernel in z coordinates is J_M g_z/j0^5. In particular its ground eigenvalue is

    lambda0(k)=(detM)^4 product_(j=1)^5
       [16sqrt3*pi/(sqrt(sigma_plus,j)+sqrt(sigma_minus,j))^8].

The metric factor is fixed, positive and independent of k. Thus lambda0(k) has fixed strictly positive lower and finite upper bounds for k>=1. Its precise determinant factor should be checked independently; operator norm normalization removes it from the semigroup claim but it cannot be silently ignored in an absolute-spectrum claim.

All24 weighted faces are present. Flatness plus a spanning tree makes the gauged minimum uniquely the identity; the Hessian is positive by linear exactness. For k>=1 E_k>=E_1 supplies fixed-chart positivity and a compact gap, while fixed derivatives grow at most linearly in k. These support an actual nonlinear HS limit and a polynomial simultaneous estimate. There are ten retained Lie-algebra vectors, so no two-source cubic cancellation is assumed. The stronger actual simultaneous theorem is being derived separately and must specify its error, normalization and chart-complement power telescope.

## Limiting full-transfer dynamics and first singlet sector

With k_n=n2/t2, fixed t>0,

    n t_(k_n),j=t sqrt(lambda_j)+O_t(n^-2).

Thus the candidate full Gaussian n-step limit is exp(-t H_eff), where

    H_eff=2 sum_(j=1)^3 N_j+sqrt6 sum_(j=4)^5 N_j,

restricted to simultaneous AdSU3 singlets. The oscillator-coordinate maps do not eliminate the frequency ratio sqrt6/2. A proved sufficiently large beta_n sequence would transfer this to actual full T powers rather than compressed-source powers.

The ground is the invariant Gaussian vacuum. A single creation quantum transforms in the adjoint representation of SU3, which has no invariant vector: an invariant traceless matrix would commute with all unitary matrices and hence be scalar zero. Therefore no one-quantum physical excitation survives. In the two-quantum sector, invariant color bilinears are proportional to Tr(XY), so the lowest energy is2+2=4. There are three frequency2 spatial modes, and their unordered pairs with repetition give3*4/2=6 independent invariant quadratic states. Cross terms between distinct modes use Tr(w_i w_j); repeated-mode terms use Tr(w_i2) minus its vacuum mean. The first positive singlet energy is therefore4 with multiplicity6. Higher sectors cannot lie below4, since every quantum costs at least2 and degree1 has no singlet. This is a finite supplied-model oscillator spacing in chosen scaling units, not a physical Yang–Mills mass gap or thermodynamic photon dispersion.
