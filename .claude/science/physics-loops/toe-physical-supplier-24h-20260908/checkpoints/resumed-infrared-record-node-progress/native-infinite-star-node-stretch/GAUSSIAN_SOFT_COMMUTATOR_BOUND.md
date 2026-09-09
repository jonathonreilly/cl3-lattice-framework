# Closing the Gaussian approximation's soft-commutator gap

Independent extension for cold review. This does not supply a physical node value or authorize a pilot. Keep the preceding failed state-norm-only argument intact.

Let D>=delta>0 be self-adjoint and let the soft derivation have bounded commutator [a,D]=J, ||J||<=j. In the node application a is the zero-frequency soft limit constructed in SOFT_LIMIT_AND_LAPLACE, rather than an unbounded spatial sum asserted to exist. For finite soft frequency omega>=0, use the exact intertwining a D=(D+omega)a+J. In particular a exp(-T D^2)-exp(-T(D+omega)^2)a equals minus the integral with left semigroup exp(-(T-s)(D+omega)^2), insertion (D+omega)J+JD, and right semigroup exp(-sD^2). This identity, proved on the generator domain and extended by the integrable smoothing bound below, removes every norm of a. Since D+omega>=delta, the same estimates are uniform as omega tends to zero. This supplies the domain justification rather than assuming spectral cutoffs commute with the derivation.

Set R=D^-1, F_T=(1-exp(-T D^2))/D, and g_T=R-F_T. Then

 epsilon_0=||g_T|| <= exp(-T delta^2)/delta.

Duhamel differentiation gives

 [a,exp(-T D^2)]
 =-integral_0^T exp(-(T-s)D^2)(D J+J D)exp(-s D^2) ds.

This does not estimate the unbounded operator D J by itself. For u>0, writing x=delta+y proves

 ||D exp(-u D^2)|| <= exp(-u delta^2)(delta+1/sqrt(2 e u)).

The two endpoint singularities are integrable. Consequently

 ||[a,g_T]|| <= epsilon_1
 = j exp(-T delta^2)[delta^-2+2T+4 sqrt(T)/(delta sqrt(2e))].

Indeed [a,R]=-R J R and one applies the preceding Duhamel bound to
[a,R exp(-T D^2)]. This is a semigroup estimate for noncommuting J; it is not an inference from a scalar derivative supremum. A conservative entirely elementary replacement is 1/sqrt(2e)<=1.

For the actual node extraction, j=beta/2. The normalized soft-annihilator identity extends by linearity from complementary annihilation subspaces. Its functional on a product F_C gamma_v F_A is

 <F_C F_A+[a,F_C]gamma_v F_A-F_C gamma_v[a,F_A]>.

The coefficient of the gamma anticommutator is one. Since ||F_A||<=1/delta and ||[a,R_A]||<=j/delta^2, replacing BOTH inverses by F_T changes each word's node functional by at most

 2 epsilon_0/delta + 2 epsilon_1/delta + 2 j epsilon_0/delta^2.

Multiply by 90/8 for the complete star. This is uniform in volume after the same soft limit used in the reviewed resolvent identity. For finite nonzero soft frequency the shifted identities should be retained before taking the limit; this lemma does not assert an exact zero-frequency finite-AP annihilator exists.

Thus a Gaussian inverse approximation CAN control the node functional, in addition to the vacuum state. What remains before a certified finite-box pilot is an explicit locality bound for the Gaussian-filter creator and for its soft derivation, followed by a quantitative finite-volume Gaussian covariance error on that box. The lemma removes one specific obstruction, not all finite-size errors. No numerical integral, matrix action, or spectrum was computed.
