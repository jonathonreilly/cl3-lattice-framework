# Independent mathematical review of the frozen #8009 unit

This is an independent source review of the conditional finite model, not an audit verdict or physical identification. Exact source hashes, all-path dispositions, execution and input bindings accompany REPORT.md. The two requested changes concern packet discovery and a missing executable geometry guard. I found no mathematical counterexample to the theorem as explicitly scoped.

## Supplied model and stripping

The input is SU(3), normalized product Haar, one twelve-link spatial cube at two open temporal slices, a supplied positive Wilson spatial coupling s and temporal coupling t, and the constant-spectator class-function embedding If=f(W_bottom). These are conditional model inputs. A normalized Haar link in the marked loop makes its product holonomy Haar, proving I is an isometry. The embedding is gauge invariant. It is not an arbitrary environment-dressed source map.

The marked multiplier intertwines exactly: M0 I=I S_s. Since w_(s/2) is positive and continuous on a compact group, its reciprocal is bounded. Taking adjoints gives I* M0=S_s I*. Thus the full-space stripping identity follows without commuting a finite projector through an exponential or inverting a compact convolution. The finite-window matrix element is taken after full multiplication and stripping. This is a closed algebraic obligation under the declared model.

The May10 temporal-kernel parent supplies only the normalized-Haar linkwise Schur convention at the specified temporal gauge. The June7 Wilson parent proves the positive character coefficients and their absolutely convergent expansion. Both complete parent notes were read. No generated status is used as proof. The three linked older geometry/supplied-D notes and the unlinked Perron scope quotation are context: the current proof reconstructs the geometry and does not consume old physical diagonality or a static-to-two-slice identification.

## Restored gauge integral and reflection

Restoring eight temporal links adds normalized Haar variables along a forest. Independent gauge changes at their upper endpoints set these links to identity; the lower source loop is unchanged, face traces are gauge invariant, and the remaining link transformations are left/right Haar translations. Consequently the additional integrations have mass one. This would need a different argument with periodic time holonomy; periodic time is expressly excluded.

Fixing the eight x-directed forest links instead leaves two twelve-edge (y,z,time) halfcubes. Each has two spatial yz faces and four temporal faces. Of twelve possible cross-face factors, the two stripped source faces are absent, leaving six spatial and four temporal cross factors. Every retained cross word pairs the same reflected half-edge with opposite orientation. Independent tuple-coordinate reconstruction checked every complete oriented face, all ten pairs, and their matrix-product identities using noncommuting SU(3) matrices. The original source geometry is correct; F2 concerns the canonical checker's failure to guard it after mutation.

After x gauge fixing the unnormalized fundamental source is Tr(U_right U_left^dagger)=sum_ij U_right,ij conjugate(U_left,ij). There is no 1/3 here. With F_ij=M(H)U_ij and P integrating the two uncoupled y links, Fubini gives the sum of ten-variable convolution quadratic forms. Reflection interchanges neither spatial and temporal weights nor the two half-actions. Reversing the original trace orientation conjugates the scalar, leaving the real quadratic-form value unchanged.

Each actual Wilson convolution has Peter–Weyl eigenvalues c_lambda(b)/d_lambda>0 at b>0. Every SU(3) irrep appears in a finite tensor power of the fundamental plus antifundamental representation; the exponential expansion has strictly positive coefficients. The finite product of these convolutions is bounded, positive and injective. Strict positivity of the quadratic form for nonzero f follows termwise from its orthogonal Peter–Weyl expansion. It requires no uniform spectral lower bound, and supplies none.

## Strict nonzero averaged amplitude

At the identity of the ten coupled half-edges, the two spatial faces reduce to w_a(U)w_a(V), one temporal face to w_t(UV^dagger), and three temporal faces to e^(3t). Simultaneous conjugation makes the matrix integral scalar. Taking its trace then gives the genuine factor 1/3 in PF_ij(identity)=delta_ij e^(3t) I(a,t)/3. This factor belongs to the averaged matrix amplitude, not the original character source.

The convolution coefficients c_lambda(a)c_lambda(t)/d_lambda are nonnegative. Expanding w_a and using nonnegative tensor-product multiplicities in the character integral makes every contribution to I nonnegative. Keeping the trivial convolution contribution and the antifundamental term of w_a yields I>=c0(a)c0(t)c_bar3(a)>0. This is a direct positive term of the actual Wilson expansion, not an inferred sign from a truncated numerical integral.

The parent identity sum_lambda d_lambda c_lambda(b)=e^b and |chi_lambda|<=d_lambda justify absolute uniform convergence. Products, convolution and Haar integrals may be interchanged. PF is continuous; its nonzero diagonal value at identity extends to an open set with positive Haar measure. It is therefore nonzero as an L2 vector. Combining this fact with injectivity closes the strict D03>0 statement for every s,t>0 on the declared finite slab, including the mathematical point s=t=6. It does not select a physical coupling or environment.

## Independent perturbative and normalization controls

At t=0 the full temporal operator is |1><1|, so the residual is |g_s><g_s|. The five-face disk gives g_s=sum c_lambda(s/2)^5/d_lambda^4 chi_lambda by four Schur gluings. I independently evaluated the equivalent complete six-trace cube surface by color indices: twelve Haar second moments identify twenty-four trace indices into eight free color loops, giving 3^8/3^12=1/81. This derivation does not substitute center balance for Haar integration. With five actual spatial halfweight factors b/12 it gives exactly 1/(12^5*81)=1/20155392.

The two canonical incidence constructions agree after explicitly translating their different vertex/edge orderings. The 973017 signed subsets and complete 243 affine residue vectors agree on the unique support-five cap. All 5832 component congruences hold. Degree-n repeated insertions reduce facewise modulo three to a support of size at most n. At n=5 the unique support-five solution forces one insertion per cap face; neutral pairs, triples and repeated factors cannot occur without exceeding degree five. Thus the fifth-order coefficient is the actual Haar coefficient just computed. Center selection remains a necessary-only condition in general.

The anisotropic estimate follows directly from twelve temporal factors, ten spatial halfweights and |chi3|<=3: 3e^(5s)(e^(12t)-1). The exact Taylor-plus-tail bound e^5<149 gives the displayed 10728/10^12 error at s=1,t=10^-12. The isotropic action has |A|<=17; its sixth-order tail divided by b^5 is bounded by 17^6 b/120 at b=10^-14. Both errors are strictly below 1/20155392, confirmed with exact fractions. These explicit tiny parameters are derived corollaries, not preregistered physical fixtures.

Dividing by a positive temporal or partition scalar preserves sign. c0(b)=1+O(b^2) preserves the fifth-order coefficient under the stated temporal normalization, but the absolute remainder is not silently reused after division. The unnormalized link coefficient c_lambda/d_lambda, normalized link coefficient c_lambda/(d_lambda c0), and native character coefficient c_lambda/c0 remain distinct.

With no spatial environment, four source links supply four Schur factors and eight spectator links supply c0^8, producing the stated diagonal control. The untouched-edge argument proves a sufficient family of zeros using commuting isotypic projectors. It is not asserted as a necessary characterization. At s=0 or t=0 the positive-injective argument changes; the separately proved t=0 result is correctly distinguished. No bounded all-weight inverse, thermodynamic result, dressed-source theorem, physical beta6 observable, or TOE closure follows.

## Proof-obligation disposition

Full-space stripping, forest Haar changes, the reflection identity, Wilson coefficient injectivity, strict averaged amplitude, five-face contraction, repeated-insertion selection, and remainder normalization are CLOSED conditional mathematical obligations at the declared inputs. Physical action/embedding/coupling selection and all infinite-volume or dressed-source bridges remain CONDITIONAL/OUTSIDE SCOPE; no equivalent open premise is smuggled into a proof of those targets. The counterexample rejects universal diagonality only when the quantified family includes this declared actual compression. It does not refute every alternative environment construction.
