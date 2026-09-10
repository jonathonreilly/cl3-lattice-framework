# Independent degree-(1,1) source review

PASS, conditional on the supplied native K, vacuum covariance K/|h0|, signed two-edge sources, and the reviewed degree-(1,0) Ward identity. Reviewed DERIVATION e0c5d1c3f28fc316f1540b3a8577c451e39bdcf6f2b8c6f574ce6b3081ec9f65. No scalar, catalog, native covariance, history or numerical result was loaded. This is a source review, not a certificate that the eventual residual or sign gate passes. The reviewer previously authored related native action-source work; this degree-(1,1) derivation and its controls were authored by Primary.

## Direct checks

The D²b formula follows from applying the commutator derivation to each displayed ordered Clifford product and adding left multiplication by B. In particular the cubic terms remain ordered products; replacing them by wedge products would change contractions. An independently implemented six-generator ordered-word reducer checked both Db and D²b for four integer coefficient choices and a skew K different from the author's toy. These eight checks do not evaluate the native model.

For the table, K²=-|h0|² and K commutes with |h0|. Thus kappa(v,d)=<d,|h0|d>, kappa(v,w)=-<d,|h0|³d>, kappa(z,k)=nu and kappa(z,w)=a^T K|h0|³d=-omega5/3. The remaining cross entries follow by the same identities and the signed-center-edge factor 2/6. In particular the last entry has the negative sign printed in the source.

The dot entries use <a,|h0|²a>=6, <a,|h0|⁴a>=42 and <a,|h0|⁶a>=324. Independent exact Laurent-polynomial constant-term convolution checked these three integer moments. Coordinate parity eliminates the perpendicular off-axis correlations; for an opposite pair the signed pair is one full directional component of Ka, giving L2=42/3 and L4=324/3. For a perpendicular pair its two diagonal contributions give L2=2*6 and L4=2*42. The same reasoning gives ed3=2nu(P), omega5/3(O). These are native symmetry identities, not generic consequences of bipartiteness alone.

For disjoint pairs, the signed opposite-neighbor contribution to <dC,|h0|dA> is (nu-6mu)/6=nu/6-3c. Perpendicular neighbor separations have different coordinate parity and vanish. Counting split opposite pairs therefore gives the stated ell formula. There are exactly90 ordered disjoint edges.

A direct check of the new nominal term uses BC*g=-i gamma(dC). Its product with u(-2gamma(vA)-4g) has expectation 2u*eCA-4u*c, while its product with iV gamma(k-dA) has expectation 2V. The part without BC is 2c*V. These give equation(4) including all signs and factors. The q normal equations and residual polynomial follow by expanding ||b-q0 Db-q1 D²b||²; real moments are legitimate for the self-adjoint D on these local polynomial vectors.

## Scalar and scope boundary

The six vectors suffice for b,Db,D²b. Their Wick words have length at most6; the supplied table therefore shows that mu=3c, nu and omega5 suffice for this particular degree. It does not assert such a closure at arbitrary degree or that omega5 has been acquired. No additional spatial covariance is needed at this degree under the supplied symmetry assumptions.

The proposed omega5 integrand is exactly E[X³/(X+t²)] by polynomial division. Its high expansion with40 terms starts at M3 and ends at M42; the next positive remainder is bounded by M43/(81 T^81). The low polynomial and t^6 A subtraction have the stated signs. The rho5 envelope 105/2 is conditional on the imported secant bound5/4. This outline is not itself a complete quadrature error ledger or execution protocol, and the source explicitly says so. No consequential normalization defect or required correction was found.

Validation:12 independent tiny checks (8 Clifford identities,3 walk moments,1 edge count). The author's8 controls are supporting algebra, not mutated native solver executions or native scalar tests.
