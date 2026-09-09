# Finite cyclic CAR compression instead of a spatial box

Status: provisional analytic route, not a numerical certificate. Goal is a finite-dimensional approximation to the Gaussian-filter node expression without a radius-r spatial carrier of order r cubed. No physical matrix or kernel has been evaluated here.

Let K be the infinite bounded real skew nearest-neighbor generator, ||K||<=W. Let S be the seven real unit vectors at the center and its six neighbors. For integer m>=1 let V_m span {K^j s:s in S,0<=j<m}, and P_m be its real orthogonal projection. Its dimension is <=7m. Define K_m=P_m K P_m on V_m. For every seed s and n<m, K_m^n s=K^n s by induction. Since both generators have norm<=W, the Taylor tails give

 ||exp(tK)s-exp(tK_m)s|| <=2 exp(W|t|)(W|t|)^m/m!
 <=2 exp(W|t|)(eW|t|/m)^m.

Here finite vectors are embedded back into the infinite real one-particle space. For real t both exponentials are orthogonal. With m>=4eW|t| this error is <=2exp(-m). This is a sufficient conservative bound, not a lower bound on required dimension.

Each defect B_A is a quadratic in the center and a combination of two neighbor fields. Its free interaction-picture evolution is a product of two propagated fields. Replacing each propagated seed by its K_m evolution therefore changes B_A(t) in CAR norm by a constant times the preceding seed error, without a dimension-of-Fock-space factor. Standard Duhamel comparison for the real-time unitary interaction cocycles gives error at most the integral of this generator difference. Inserting finitely many local J_A fields and the central Majorana costs further polynomial time/norm factors. A complete explicit constant for the actual soft-node expression is still required and is not asserted in this note.

Crucially, the reference state on CAR(V_m) is the RESTRICTION of the infinite free Gaussian state. Its covariance is P_m Gamma_infinity P_m. It is usually mixed and is NOT the vacuum covariance sign(K_m). Using the latter silently changes the bath and invalidates the argument. A finite Gaussian mixed-state trace formula or a Gaussian purification can evaluate the correctly restricted state. This avoids generic exponential monomial expansions, but a controlled covariance-matrix perturbation estimate is still needed.

The Gram matrix of the cyclic seeds consists of finite-walk moments <s,K^n s'>. The reference covariance matrix needs additional moments <s,K^n Gamma_infinity s'>. These are specific spectral integrals of the canonical Bloch symbol. Thus one can seek certified small-matrix moment quadrature without constructing all sites in a box. Stable orthogonalization, controlled moment conditioning, an actual Gaussian mixed-state kernel, and realistic m are all open implementation obligations. The crude filter window R=512/h with W<4h still leads to many thousands of cyclic vectors; this route reduces a spatial cube to a linear bound but does not itself establish affordable cost.

Do not infer a finite-L impurity gap, an alpha value, or interacting stability from this provisional compression argument. The existing short-time L4 pilot tests a pure finite invariant carrier and does not validate this infinite mixed-state bath replacement.
