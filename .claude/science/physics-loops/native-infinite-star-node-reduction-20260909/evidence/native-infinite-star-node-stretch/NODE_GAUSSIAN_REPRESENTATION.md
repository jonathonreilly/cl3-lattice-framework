# Two-time Gaussian formula for the native node scalar

This is a prospective rigorous representation, not an evaluated node value. It retains the actual90 native words and both negative inverses through the common smooth inverse filter. No stationary-free replacement of a defect inverse is made.

## 1. The generalized zero mode

Use the eight-site cell and center v=0 of NODE_REDUCTION.md. Let q_j be1 on j in2Z^3 and zero otherwise. This bounded, non-square-summable real vector satisfies K q=0: at every neighboring odd site the two opposite-axis contributions cancel in the canonical pi gauge. It extracts the diagonal node coefficient alpha=sum_j q_j c_0j. Statements involving q below are defined by local truncation and limits; gamma(q) itself is not a bounded CAR operator.

For a real orthogonal one-particle map L_H(t), define it by

 exp(-itH) gamma(a) exp(itH)=gamma(L_H(t)a).

With the H=(i/4)gamma^T K gamma convention, L_H(t)=exp(tK) on coefficient columns. This fixes the sign convention without appealing to a chosen eigenplane orientation.

For the two-filter term of the exact creator, set

 G_CA(t,s)=exp(-itH_C) exp(-isH_A) exp(i(t+s)H),
 R_CA(t,s)=L_HC(t)L_HA(s)L_H(-t-s),
 l_C(t)=L_HC(t)e_v.

Then U_C(t) tau_t(gamma_v U_A(s))=gamma(l_C(t)) G_CA(t,s), and G conjugates Majoranas by R. All finite-volume phases use the same H and E0; in the infinite GNS representation this expression is the product of the bounded local perturbation cocycles, not a separate assertion about an unbounded positive-time imaginary evolution.

## 2. Cancelling the infinite external sum algebraically

For finite real vectors q,l and any even Gaussian unitary G with G gamma(q) G^-1=gamma(Rq), CAR gives exactly

 {gamma(q), gamma(l)G}/2
 = (q dot l)G + (1/2)gamma(l)gamma((R-I)q)G.       (A)

In the application q is generalized, but d=(R-I)q is an ordinary square-summable real vector. The right side of(A) therefore defines the limit without ever constructing gamma(q).

The diagonal node scalar has the exact formula

 alpha=(1/8) sum_{A,C disjoint} integral_R² w(s)w(t)
   [(q dot l_C(t)) <G_CA(t,s)>
       +(1/2)<gamma(l_C(t)) gamma(d_CA(t,s)) G_CA(t,s)>] ds dt,   (B)

where d_CA=(R_CA-I)q and brackets are the original infinite canonical Gaussian vacuum. The real inverse filter convention,90 terms and factor1/8 are inherited unchanged. Formula(B) is an overlap plus a two-insertion Gaussian kernel, not a positive integral; w and the overlaps can carry phases. It avoids a zero-momentum eigenvector gauge and the infinite spatial Fourier sum.

## 3. A uniform explicit time envelope

Let b_A=||(K_A-K)q||2. Because q is constant on the center cell and zero on the two neighboring sites of the reversed pair, each of the two changed K entries contributes magnitude4|t_hop|; hence b_A=4sqrt(2)|t_hop| for every pair. Denote this common value b.

Duhamel's formula and Kq=0 imply

 ||(L_HA(s)-I)q||2 <= b|s|.

This follows by integrating L_HA(s-u)(K_A-K)q; its integrand has norm b because L_HA is orthogonal. It does not estimate q's divergent norm. Applying the identity successively gives

 ||d_CA(t,s)||2 <= b(|t|+|s|),
 |q dot l_C(t)| <= 1+b|t|,    ||l_C(t)||2=1.

Since G is unitary and the insertion vectors are real, CAR bounds the integrand's absolute value by

 1+(3b/2)|t|+(b/2)|s|.                         (C)

Thus (B) is absolutely integrable using M0 and M1 of the same smooth filter. If a square time cutoff |s|,|t|<=T is used, a conservative complete90-word truncation error is

 (90/8)[2 M0 a0(T)+2b(M1 a0(T)+M0 a1(T))],
 a_j(T)=integral_{|u|>T}|u|^j |w(u)|du.

This union bound uses the coefficients of(C) summed symmetrically; overlap double counting is harmless. The tail parameters depend on the chosen explicit filter, not on system volume. No physical quadrature has been performed.

## 4. Polynomial-size pointwise route and its missing certificate

Each pair perturbation B_A is a rank-two Majorana quadratic: center gamma_v times one signed sum of its two neighbors. The interaction-picture cocycle is a time-ordered evolution of that rank-two perturbation under the known free dynamics. A finite ordered product approximation therefore consists of elementary Gaussian two-Majorana rotations. Its vacuum overlap and the forced two-insertion overlap in(B) are finite ordered Wick Pfaffians. The sign is fixed by the ordered product/continuous identity lift, rather than a freely chosen square root of a determinant. The necessary contractions are Fourier integrals of the known canonical covariance and free one-particle evolution. No2^(volume) Fock space or full-volume eigensystem is required.

This specifies a concrete two-real-time integration route, far smaller in dimension than the five-inverse sixth-order integral. It is not yet a numerical cost contract or arithmetic certificate. A practical implementation must supply an explicit filter with certified tails, an error bound for the time-ordered product and its zero-mode Duhamel vectors, certified free contraction quadrature, and interval Pfaffians including overlap-zero cases. Ordinary determinant square roots and unverified bath truncations are insufficient. A sign decision follows only if the resulting interval for alpha excludes zero; no such interval exists here.

The native result may still be zero. The reduction gives a finite signed target, explicit time tail and polynomial-size pointwise Gaussian dataflow. It does not infer a physical phase or drop higher odd transition sectors/mixed sixth histories.
