# Principal-angle construction and the finite-time graph obstruction

This extends the reviewed stationary trace-class result. It makes no finite-time compression claim without the chart assumptions stated below. All one-particle spaces use the particle-hole involution of the actual Majorana problem; Q and P obey conjugate(P)=1-P.

## Explicit stationary Fock construction

The compact difference of projections admits a principal-angle decomposition: diagonalize the positive compact operator Q(1-P)Q on ran Q. For every eigenvalue s² strictly between0 and1 choose a normalized vector u in ran Q; its normalized partner in ran(1-Q) is obtained by applying (1-Q)P to u. The resulting two-dimensional plane has P matrix [[c²,cs],[cs,s²]], up to a removable phase, with c=sqrt(1-s²). Orthogonal spectral subspaces give orthogonal planes. Eigenvalue1 gives the finite-dimensional fully exchanged spaces. The common0/1 spaces are unchanged. This construction follows directly from P²=P and the spectral theorem for a compact positive operator.

Particle-hole conjugation pairs the nontrivial planes. More explicitly, on a finite nonexceptional block the annihilator equations have a skew-symmetric pairing matrix Z (the skew relation is the CAR anticommutator of two annihilators). Unitary congruence reduces Z to 2-by-2 skew blocks: choose a singular vector, pair it with its normalized skew-conjugate image, and repeat on the orthogonal complement. This proves the paired form used below, rather than assuming independent one-mode rotations. Compactness permits the same block construction countably. In Fock language a paired block uses two reference modes a,b and the normalized factor

 c + s a†b†

acting on their empty vacuum, with a phase on s if required. Its mean particle number is2s². The corresponding doubled one-particle projector difference has squared Hilbert–Schmidt norm4s². A fully exchanged reference mode contributes one particle and squared projector difference2; only finitely many can occur because the difference is compact and trace class. Treat these occupied modes first, using a fixed ordered creation product.

For infinitely many paired blocks the finite products converge in Fock norm: choose each c>=0, and the inner product between products cut at m and n is product_(j=m+1..n)c_j. Since sum s_j² is finite, the tail products approach1. This proves the Cauchy property and gives a normalized vector in the original Fock space. Its finite-mode correlations have precisely covariance P, so it is the required pure quasifree state. No external implementability theorem is needed for this construction.

The particle count follows by monotone convergence of finite-mode number operators:

 <N>=number of fully occupied exceptional modes +2 sum_j s_j²
     =(1/2)||P-Q||HS² <=(1/2)||P-Q||1 <87/2.

This explains the particle-hole factor explicitly. The vacuum overlap is zero if a fully occupied exceptional mode occurs. If no such mode occurs, the product of cosines is strictly positive because the squared sines are summable. A uniform lower bound on that product has not been proved by the trace bound alone.

## Relative parity along the coupling path

Parity cannot be read from the integer index of arbitrary complex projections alone. Here it is the parity of the number of fully occupied exceptional reference modes; paired rotations create two particles. The constructed quasifree vacuum is unique up to phase. Near any fixed polarization, sufficiently close projections in operator norm have no exchanged modes relative to each other and can be joined by the paired-rotation construction above. Their vacuum vectors therefore have the same parity. The trace-norm-continuous lambda path is operator-norm continuous and its compact parameter interval can be covered by finitely many such neighborhoods. Starting at lambda0 with the even reference vacuum proves even relative parity at every lambda. Fully exchanged modes relative to the original reference may occur, but their total parity is even. Their occurrence can make the original-reference overlap vanish without breaking implementability or continuity.

## Finite-time graph evolution: what follows and what does not

Let P_A be the stationary negative spectral projection of h_A, and write h_A=(-omega_minus) direct-sum omega_plus on its negative/positive spaces, with both omega nonnegative and bounded. If the initial subspace ran Q is a graph over the entire ran P_A of a bounded operator Z0, its imaginary-time evolution is a graph with

 Z_tau=exp(-tau omega_plus) Z0 exp(-tau omega_minus).

Indeed evolving a vector (x,Z0x) gives (exp(tau omega_minus)x,exp(-tau omega_plus)Z0x), and the first component can be used as the new coordinate. This proves contraction of every Schatten norm of Z, including HS and nuclear norms, uniformly in tau. A graph truncation at singular rank r has tail bounded by its nuclear norm divided by sqrt(r+1) in HS norm. Orthogonal graph-projector reconstruction, rather than raw matrix truncation, keeps a physical covariance.

Trace class of Q-P_A alone does not bound ||Z0||1 uniformly: its singular values are tan(theta), while the projector estimate controls sin(theta). Angles arbitrarily close to pi/2 can make the graph norm arbitrarily large. A fully exchanged block prevents this chart entirely.

There is nevertheless a precise finite-exception statement at the INITIAL time. Pick an explicit eta in(0,1). At most ||Q-P_A||1/eta <87/eta one-particle singular directions have sin(theta)>eta. On the complementary principal-angle tail,

 sum tan(theta) <= (1/sqrt(1-eta²)) sum sin(theta),

with the consistent doubled multiplicities. Thus this initial tail has a controlled nuclear graph norm. This is an algebraic split, not yet a uniform dynamical split.

The obstruction is that the exceptional principal-angle subspace generally does not reduce omega_plus or omega_minus. Imaginary-time contractions mix its directions with the nominal tail. Removing its initial finite-dimensional span does not yield an autonomous graph equation on the remaining complement. One can retain the evolved exceptional columns exactly, but their changing orientation and orthogonalization against the graph require quantitative conditioning bounds. Neither trace class nor the stationary excitation estimate supplies those bounds. Conversely, if an additional finite-dimensional reducing exceptional subspace exists, the graph contraction argument applies to its invariant complement and gives a uniform tail bound without a global reference-overlap lower bound. No such reducing subspace is supplied for the actual gapless native bath.

A potentially implementable route is a moving finite-column chart: propagate the exceptional columns and a trace-class graph tail, then certify their Gram matrix and chart transitions. Its required new certificate is a lower singular-value bound for the evolving finite-column representation (or an overlap-free Grassmann error analysis). Simply asserting that finite exceptional modes stay separate would be incorrect. This identifies the remaining quantitative obligation without assuming a vacuum overlap, active spectral gap, or affordable rank.
