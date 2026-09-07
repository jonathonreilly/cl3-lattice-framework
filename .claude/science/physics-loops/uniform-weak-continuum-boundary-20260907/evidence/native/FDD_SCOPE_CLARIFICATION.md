# Scope-only correction

Primary review5a390b5e requested an explicit finite-dimensional-distribution scope instead of the potentially broader random-distribution-limit phrase. Original0e93 proof is preserved. The revised sentence expressly denies a random-distribution topology/tightness claim; real test functions are also made explicit. No equation, bound, normalization, geometry or limit calculation changed.

--- original0e93
+++ clarified
@@ -46,9 +46,9 @@

 At u=0 the neutral ground is product Haar. Choose N=n³ disjoint elementary xy plaquettes anchored at (2i,2j,2k), 0<=i,j,k<n, and set ell=1/(2n). Their physical anchors are(i/n,j/n,k/n) in the unit box. Their link sets are disjoint. Let J_k=ReTr(U_plaquette,k)/3. Haar orthogonality and fundamental center charge give omega(J_k)=0 and omega(J_k²)=1/18. The variables X_k=sqrt18 J_k are independent, centered, bounded by sqrt18, and have variance1.

-For a continuous test function f on the unit box put F_n(f)=n^(−3/2)Σ_k f(k/n)X_k. Its variance is n^(−3)Σ_k f(k/n)², tending to integral f²; for f=1 it is exactly1 at every n. The total coefficient l1 norm is at most n^(3/2)||f||_infinity, polynomial. Separated support regions have zero covariance already at finite n. There is therefore no contradiction with Sections2–3.
+For a real continuous test function f on the unit box put F_n(f)=n^(−3/2)Σ_k f(k/n)X_k. Its variance is n^(−3)Σ_k f(k/n)², tending to integral f²; for f=1 it is exactly1 at every n. The total coefficient l1 norm is at most n^(3/2)||f||_infinity, polynomial. Separated support regions have zero covariance already at finite n. There is therefore no contradiction with Sections2–3.

-One can verify the full commuting Gaussian contact limit without a spectral fit: for coefficients a_(n,k)=n^(−3/2)f(k/n), boundedness and centering give omega(exp(it a X))=1−t²a²/2+O(|a|³), uniformly in k. Here max|a| tends to zero, Σa² tends to integral f² and Σ|a|³ tends to zero. Independence then gives the characteristic-function limit exp[−t² integral f²/2]. Applying the same argument to linear combinations of finitely many f gives the Gaussian white-noise finite-dimensional distributions with covariance integral fg. This is a commuting equal-time random-distribution limit inside the actual u=0 model, not a relativistic quantum field theory or a claim about its dynamics.
+One can verify the full commuting Gaussian contact limit without a spectral fit: for coefficients a_(n,k)=n^(−3/2)f(k/n), boundedness and centering give omega(exp(it a X))=1−t²a²/2+O(|a|³), uniformly in k. Here max|a| tends to zero, Σa² tends to integral f² and Σ|a|³ tends to zero. Independence then gives the characteristic-function limit exp[−t² integral f²/2]. Applying the same argument to linear combinations of finitely many f gives the Gaussian white-noise finite-dimensional distributions with covariance integral fg. This is a commuting equal-time finite-dimensional distribution limit inside the actual u=0 model. No tightness or convergence in a topology of random distributions, relativistic quantum field theory, or dynamical limit is asserted.

 Thus a statement that uniform weak coupling forbids EVERY nontrivial continuum limit would be false. The theorem excludes nonzero off-diagonal connected correlations for the stated renormalized local field class while allowing nontrivial contact data.
