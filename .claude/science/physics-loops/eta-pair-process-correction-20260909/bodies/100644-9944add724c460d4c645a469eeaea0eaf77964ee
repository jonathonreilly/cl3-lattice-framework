# Block33 preflight witnesses

Let `P0=J_4/4` and `Pperp=I-P0`.  Then

\[
Q_\lambda=\frac14(P_0+\lambda P_\perp)
\]

has eigenvalues `1/4` once and `lambda/4` three times, with determinant
`lambda^3/256`.  Its ordinary and nonnegative ranks are one at `lambda=0`
and four for `lambda>0`; the displayed spectrum is positive semidefinite.  With

\[
S_{\sqrt\lambda}=P_0+\sqrt\lambda P_\perp,
\qquad Q_\lambda^{1/2}=\frac12S_{\sqrt\lambda},
\qquad S_{\sqrt\lambda}^2=4Q_\lambda.
\]

A fixed five-response library is

\[
R_*=J_4/16,\qquad R_i=e_i e_i^T,
\qquad Q_\lambda=(1-\lambda)R_*+
\frac\lambda4\sum_{i=1}^4R_i.
\]

The lower bound five follows because the `lambda -> 1` closure requires four
single-diagonal product components, while their convex hull cannot contain
the fully supported `R_*`.

One fixed controlled isometry can realize that library without carrying
`lambda` in its response.  Let `C` have five orthogonal sectors, and let `O`
and `A` each have one Blank state plus sixteen orthogonal pair-label states.
On the five-dimensional Ready subspace with Blank `O,A`, define

\[
V|I,B_O,B_A\rangle=\frac14\sum_{g,h}
|I,g,h\rangle_{C,O}|g,h\rangle_A,
\qquad
V|D_i,B_O,B_A\rangle=|D_i,i,i\rangle_{C,O}|i,i\rangle_A.
\]

Then `V dagger V=I_5`.  For the supplied mixed cause state

\[
\rho_C(\lambda)=(1-\lambda)|I\rangle\!\langle I|
+\frac\lambda4\sum_i|D_i\rangle\!\langle D_i|,
\]

tracing `C,A` gives `Q_lambda`.  Three supplied cause states and three
disjoint Blank `O,A` banks acted on by `V tensor 3` give
`Q_lambda tensor 3`.  All banks are present initially and the output cause and
archive remain explicit.  The isometry is `lambda`-independent, while
`rho_C(lambda)` is not; this is parameter relocation into environment
preparation, not a selector, reset, or renewal theorem.

For any screening factorization, flatten the sixteen pair outcomes and set
`q=sum_z pi_z r_z`.  The frozen-minus-product matrix is

\[
H_F-H_R=\sum_z\pi_z(r_z-q)(r_z-q)^T.
\]

It is positive semidefinite.  Its trace is the complete-pair repetition gap
`sum_z pi_z ||r_z-q||^2`; equality forces every active `r_z=q`.  Since each
`r_z` is rank one, frozen/product compatibility exists exactly when
`rank(Q_lambda)=1`, hence only at `lambda=0` in the strict domain.  The
one-state uniform-product factorization is the converse witness.

For the endpoint-mixture side control, `Delta=q_1-q_0`,

\[
H_{\rm persistent}-q_\lambda^{\otimes2}
=\lambda(1-\lambda)\Delta^{\otimes2},
\]

and the equality-event excess is `9 lambda(1-lambda)/16`.

For the optional stationary Markov-mode control, use only
`K=Pi+rho(I-Pi)` with `0 <= rho <= 1`; this is stochastic throughout the
strict domain and gives residual
`rho lambda(1-lambda) Delta tensor Delta`.

For the coherent control, let

\[
U_\lambda=P_0+e^{i\theta}P_\perp,
\qquad \cos\theta=2\lambda-1.
\]

Then `U_lambda` is unitary, commutes with simultaneous label permutations,
and `|U_lambda[h,g]|^2=4 q_lambda(g,h)`.  It depends on `lambda`; it is not a
common fixed interaction across the family.

For the depth-three control, define the proper-cubic- and side-invariant
zero-sum feature

\[
w(g,h)=\begin{cases}3,&g=h,\\-1,&g\ne h,\end{cases}
\qquad \sum_{g,h}w(g,h)=0,
\]

write `b_lambda=(1-lambda)/16`, and set

\[
\epsilon_\lambda=\frac{b_\lambda^3}{54},
\qquad H_3=q_\lambda^{\otimes3}+\epsilon_\lambda w^{\otimes3}.
\]

Every entry is positive on `[0,1)`: the all-off-diagonal negative case is
`53 b_lambda^3/54`, and the one-off-diagonal negative case is at least
`5 b_lambda^3/6`.  All one- and two-use marginals are product because
`sum_x w_x=0`, while every all-diagonal outcome triple differs by
`27 epsilon_lambda=b_lambda^3/2`.  The perturbation respects the displayed
label symmetries.  These are preregistered algebraic witnesses, not execution
results.
