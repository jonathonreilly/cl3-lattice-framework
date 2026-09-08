# Uniform local approximation on the natural ring timescale

Independent root continuation, frozen before reading the parallel natural-timescale attempt. The earlier fifth-order local normal form is valid, but its generic local dynamical estimate does not control one natural ring period: with U=1, epsilon=gamma/U, t~epsilon^-4, the bound epsilon^6 t(1+epsilon t)^3 scales as epsilon^-7. This is a limitation of that estimate, not a contradiction of its theorem. We now avoid it using a higher finite normal form and two different comparison Hamiltonians. No optimal-prethermal theorem or assumed isolated global ice band is needed.

## 1. The same finite construction through order13

Use H/U=D+zV, z=g lambda_*/U, |b_e|<=1, gamma=|g|lambda_*, epsilon=|z|, and the same grouped-cell strong-support norm as root local-truncation proof113e3f. Construct the single anti-Hermitian polynomial S(z)=sum_{j=1}^{13} z^j S_j by the same homological recursion. Let K_j be the D-conserving coefficient. Use k_j=1-j/28, j=0,...,13, with k_13=15/28 and final norm1/2. The exact recursive majorants are now

r_j=d[z^j]exp(112j sum_{i<j}s_i z^i)+v[z^{j-1}]exp(112j sum_{i<j}s_i z^i),
s_j=4r_j, d=2916, v=216513.

All are finite constants independent of volume. The earlier commutator estimate with loss1/28 proves these bounds unchanged. Set r=min(1,1/(224 sum_{j<=13}s_j)), M=2(d+v). The exact convergent Lie series and Cauchy estimate give, for epsilon<=r/2,

Y H Y†=UD+K+R, Y=exp(S),
K=U sum_{j=1}^{13} z^j K_j, [K_j,D]=0 termwise,
||R||_{1/2}<=C_14 U epsilon^14, C_14=2M/r^14.

This is the same constructive local proof with thirteen steps, not an extrapolation of a numerical fit. The constants are deliberately very conservative. At any fixed epsilon within this sufficient regime, every support/norm bound is uniform in volume. The effective interaction K has ||K||_{1/2}<=C_K gamma for a finite constant C_K=sum_{j<=13}r_j.

## 2. A slow local extension of the ice Hamiltonian

Let J4 be the actual fourth-order kinetic-ring operator extended locally to the full edge carrier: each F_C selects an alternating cycle and S_C flips it, with the source-proved coefficient eta_C product b_e/2. Alternating cycle flips preserve each Q_v, so J4 commutes with D on the full carrier. Its interaction norm is bounded by a finite geometry constant J_* independent of volume. All length-four winding cycles at extent four must be included. The diagonal fourth coefficient is scalar on ice for arbitrary fixed b_e; it need not be physically added to dynamics.

Define a second local Hamiltonian

L = U z^4 J4 + U sum_{j=6}^{13} z^j K_j.

Every term commutes with D, so L preserves the ice space P. The parity and fourth-order gauge arguments already proved imply

K|_P = (second scalar + fourth scalar) I_P + L|_P.

This is exact for these finite polynomials. In particular, removing K_1,K_3,K_5 and replacing K_2,K_4 by their ice scalar/ring expressions does not change dynamics of an ice-supported state. We do not assert equality outside ice. No compression map or local extension theorem is required: the known local J4 and already local higher K_j explicitly supply L.

The crucial difference is its norm and propagation speed:

||L||_{1/2} <= U epsilon^4 (J_*+C_6),
||L-U z^4J4||_{1/2} <= C_6 U epsilon^6,
C_6=sum_{j=6}^{13}r_j,

using epsilon<=1. Thus L has a Lieb–Robinson velocity proportional to U epsilon^4, whereas the full excited-sector K has velocity proportional to gamma. Both statements use the same fixed positive norm decay and geometry.

## 3. Two local dynamical comparisons

Let rho be any density matrix supported on ice and O a fixed local observable in the transformed frame. The laboratory preparation and observable are Y†rho Y and Y† O Y. No global norm closeness of bare and dressed ice is assumed.

First compare YHY† with UD+K on this expectation. The strong-support Duhamel/Lieb–Robinson argument gives, uniformly in volume,

error1 <= A_O C_14 U epsilon^14 |t| (1+B gamma |t|)^3.

This bound is valid for arbitrary states. As before the commuting D rotation enlarges a local support once, not at speed U. Under UD+K the state rho remains in ice, so its expectations equal those under L, since the scalar terms and UD have no effect on its density-matrix evolution. This identity holds even if O itself does not commute with D: both evolved states are the same within P.

Second compare L with the pure kinetic ring extension U z^4 J4. Both have slow local interactions and the difference starts at order6. The ordinary local Duhamel/Lieb–Robinson bound gives

error2 <= A'_O C_6 U epsilon^6 |t| (1+B' U epsilon^4 |t|)^3.

Set t=s/(U epsilon^4), with fixed finite dimensionless s>=0. Since epsilon<=1,

error1 <= A_O C_14 s epsilon (1+B s)^3,
error2 <= A'_O C_6 s epsilon² (1+B' s)^3.

Their sum tends to zero as epsilon tends to zero, uniformly in lattice volume, for any fixed number s of ring-time units. Constants depend on fixed local observable support, norm convention and geometry; they are not claimed numerically modest. This is a controlled local emergence of the supplied ring dynamics on its own natural timescale, rather than merely a short-time small-error statement. The generic fifth-order estimate alone did not provide this conclusion.

A fourteen-step construction would change the first error to O(epsilon²), but is unnecessary for a positive vanishing bound. Likewise an optimal prethermal normal form could be an alternative route, but its gauge/truncation assumptions are not imported into this proof.

## 4. Scope

The mathematical statement concerns a supplied Hamiltonian, prepared dressed ice states, and consistently dressed local measurements. It neither selects the penalty/couplings nor proves their preparation in nature. A laboratory bare local observable has an additional local O(epsilon) dressing difference; a bare ice initial state cannot simply be replaced globally by a dressed one. The result is uniform local dynamics at fixed scaled time, not a uniform isolated global ice spectral band, a thermodynamic phase theorem, a photon, deconfinement, or an RK-point selection. The actual induced leading model is the kinetic ring Hamiltonian, with its finite-size winding terms and native sign convention.
