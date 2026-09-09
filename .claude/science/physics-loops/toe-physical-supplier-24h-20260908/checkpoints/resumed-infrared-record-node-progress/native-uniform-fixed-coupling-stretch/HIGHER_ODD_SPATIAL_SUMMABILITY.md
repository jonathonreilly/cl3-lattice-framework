# Higher-odd singleton kernel: a candidate summable spatial bound

New analytical consequence for independent review. Assumes the nine-power spectral tail of HIGHER_ODD_SOFT_TAIL.md, the8062/8063 uniformly rapidly quasi-local odd Z_v with Z_v Omega=P>=3 chi_v, uniform finite-range CAR propagation, and the prescribed Gaussian AP domain. No interacting-state conclusion or physical computation.

Claim: the higher-odd kernel T^Z_vw=<Z_v Omega,H^-1 Z_w Omega> has a volume-uniform absolutely summable row, and its zero-extended finite rows converge in l1 to the thermodynamic row. This upgrades the generic full-star row-l2 theorem only for the higher-odd part.

## 1. A one-sided inverse filter whose adjoint kills the vacuum

Choose real smooth theta with0<=theta<=1, theta(x)=0 for x<=1/2 and theta(x)=1 for x>=1. Let f(x)=theta(x)/x, defining it as0 near zero and on negative x. Then f and every derivative belong to L2(R). Plancherel plus Cauchy-Schwarz, with sufficiently many polynomial time weights, gives an inverse Fourier kernel w with every weighted L1 moment finite. This argument does NOT require w bounded at t=0; the one-sided1/x tail can give a logarithmic singularity there, which is integrable.

For0<epsilon<=1 set f_epsilon(x)=epsilon^-1 f(x/epsilon)=theta(x/epsilon)/x and w_epsilon(t)=w(epsilon t), in the same Fourier convention f(x)=integral w(t)e^-itx dt. Hence

 integral |t|^p |w_epsilon(t)|dt = epsilon^(-p-1) M_p.

Define the bounded odd quasi-local operator X_epsilon,w=integral w_epsilon(t) tau_t(Z_w)dt. Since H Omega=0,

 X_epsilon,w Omega=f_epsilon(H) Z_w Omega,
 X_epsilon,w* Omega=f_epsilon(-H) Z_w* Omega=0.

The second identity is crucial and uses the positive generator, real filter and negative-frequency support exclusion, not Hermiticity of Z. Therefore for every v,

 <Z_v Omega,X_epsilon,w Omega>=omega({Z_v*,X_epsilon,w}).

The reversed product has zero vacuum expectation because X_epsilon,w* Omega=0. An ordinary arbitrary inverse approximation would not permit this replacement by a graded anticommutator.

## 2. Two errors: infrared vector tail and spatial operator tail

The higher-odd spectral bound mu_Z(0,e]<=C e^9 gives

 ||(H^-1-f_epsilon(H))Z_w Omega||
 <= [integral_(0,epsilon] E^-2 dmu_Z]^(1/2)
 <= sqrt(9C/7) epsilon^(7/2).

Thus replacing T^Z_vw by the filtered correlation costs at most a uniform constant times epsilon^(7/2).

For R=distance(v,w) large, approximate Z_v by an odd operator in its R/4 ball. For |t|<=cR, with c a fixed inverse propagation velocity, tau_t(Z_w) has an odd R/4-ball approximant with error <=C_q R^-q for every fixed q. This follows by first truncating Z_w to a smaller fixed fraction of R, then applying the finite-range propagation bound; the exponential short-time leakage and original rapid tails are uniform in volume. Constants may depend on q, not epsilon,R,L.

Integrate those local approximants only for |t|<=cR. Their support is disjoint from the v approximant, so the graded anticommutator vanishes. The short-time error is at most C_q epsilon^-1 R^-q. The long-time part is bounded by norms and the filter moment:

 integral_(|t|>cR)|w_epsilon(t)|dt <= C_p epsilon^(-p-1) R^-p.

The v truncation error times ||X_epsilon,w||<=M0 epsilon^-1 has the same first form. Consequently

 |T^Z_vw| <= C epsilon^(7/2)+C_q epsilon^-1 R^-q
                         +C_p epsilon^(-p-1)R^-p.

Finite torus balls use their graph distance; at sufficiently large ball size they equal the whole algebra. The same constants and argument apply to the infinite limit.

## 3. Explicit summable exponent and thermodynamic rows

Choose epsilon=R^(-7/8), p=q=32. The three powers are respectively

 R^(-49/16), R^(-249/8), R^(-25/8).

Thus |T^Z_vw|<=C'(1+R)^(-49/16), uniformly in volume. Since49/16>3, the row is l1 summable on the three-dimensional lattice. More generally any exponent below7/2 can be achieved by choosing epsilon=R^-a with a<1 sufficiently close to1 and sufficiently high filter moments.

The earlier thermodynamic inverse-moment theorem gives convergence of every fixed entry. The new common summable spatial majorant gives l1 convergence of centered zero-extended rows by dominated convergence. In a fixed magnetic cell, the corresponding Fourier coefficient symbols therefore converge uniformly. This does not claim an isometric embedding of finite periodic many-body spaces.

The higher-odd quadratic singleton channel now has an absolutely summable kernel, hence a bounded convolution operator by Schur's estimate. This is a statement about the defined response kernel (or its self-adjoint realification), not identification of the full native sixth-order Hamiltonian. The one-particle component has only the weaker generic cubic spectral tail: this argument would give at best powers below1/2 there, so it does not remove its infrared problem. Nonlinear higher-odd singleton returns can therefore be separated as a summable channel while the linear return still requires controlled resummation. Other mixed histories and the all-u relative-impurity susceptibility remain outside the result.
