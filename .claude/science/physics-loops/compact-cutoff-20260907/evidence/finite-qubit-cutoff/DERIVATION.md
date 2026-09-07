# Independent finite-qubit cutoff of the actual compact interacting cube

This is a finite-carrier approximation of the supplied block29 compact Hamiltonian, not a selection of that action or its real-time clock. Fix a>0, v>=0 and integer R>=0. On L²(SU(3)^12), K=(3/(2a))(-Delta_total) and V=v sum six actual plaquette deficits 1-ReTr(U_f)/3. Thus 0<=V<=12v and H=K+V is positive self-adjoint. Work also on its local-vertex-gauge-invariant reducing subspace. No weak-field replacement of V is made.

## 1. Local finite carrier and exact Gauss action

Peter–Weyl gives each link as the orthogonal sum V_(p,q) tensor V_(p,q)* over nonnegative integer p,q. Retain all d_(p,q)^2 matrix coefficients for p+q<=R; call the link projector P_e. Put P=product over twelve P_e and Q=I-P. This cutoff commutes with both left and right translations on each link because it selects full representation blocks, hence with every vertex gauge transformation. It also commutes with K. Restricting to physical states therefore preserves the exact original Gauss action, not twelve independently central link spaces.

With d_(p,q)=(p+1)(q+1)(p+q+2)/2 and t=p+q+2, the shell dimension is

 S_t = (t²/4) sum_(j=1)^(t-1) j²(t-j)² = (t^7-t^3)/120.

Summing t=2,...,N, N=R+2, gives

 D_R = N²(N+1)²(N-1)(N+2)(3N²+3N+2)/2880.

The polynomial identity can be proved by subtracting its values at N and N-1 and obtaining S_N, with value1 at N=2. Thus q_R=ceil(log2 D_R) qubits suffice to store each finite link, and twelve q_R qubits suffice for the whole tensor carrier. This counts storage, not a preparation protocol or a gate compiler. At R=0 a link is one-dimensional and needs zero qubits.

Choose a fixed isometry from each finite link carrier into its q_R-qubit code. Transport the finite gauge representation and Hamiltonian into the product code. They can be extended to the unused code complement with trivial gauge action and inert dynamics. This is mathematical finite-dimensional realization; it does not prove native qubit controls, nearest-neighbor layout, bounded switching costs or exact finite-gate implementation.

## 2. Exact omitted kinetic threshold

In trace-orthonormal convention, the link Casimir is (2/3)(p²+q²+pq+3p+3q), so its contribution to K is

 k_(p,q)=(p²+q²+pq+3p+3q)/a.

For s=p+q fixed, p²+q²+pq=s²-pq is minimized by the most balanced integer pair, giving ceil(3s²/4). The minimum increases strictly with s. A basis state outside P has at least one omitted link with s>=R+1, while all other link energies are nonnegative. Consequently, as quadratic forms,

 K >= g_R Q,  g_R=[ceil(3(R+1)²/4)+3(R+1)]/a.

The threshold is attained on the unrestricted tensor carrier by one balanced omitted link and eleven trivial links. Such a one-link colored coefficient need not be a physical singlet; restriction to the Gauss sector retains the same valid lower bound, without claiming it is sharp there. Since V>=0, H>=K>=g_R Q as forms. For a normalized finite-energy input psi, E=<psi,H psi>, exact evolution psi(t)=exp(-itH)psi conserves E and

 ||Q psi(t)|| <= sqrt(E/g_R).

The assertion uses the form domain D(H^(1/2)), not only the operator domain.

## 3. Projected dynamics and an error for an arbitrary finite-energy input

Define H_R=PHP on the finite carrier and U_R(t)=exp(-itH_R). It is self-adjoint and nonnegative; it commutes with the original gauge action restricted to the finite carrier. P is not assumed to commute with V. On operator-domain inputs, apply P to the exact evolution:

 i d_t(P psi(t)) = H_R P psi(t) + P V Q psi(t),

because P K Q=0. Variation of constants gives

 P psi(t)-U_R(t)P psi = -i integral_0^t U_R(t-s) P V Q psi(s) ds.

For negative t reverse the integration direction. Unitarity and the uniform energy bound imply

 ||P psi(t)-U_R(t)P psi|| <= |t| ||V|| sqrt(E/g_R).

Adding the Q component gives the convenient bound

 ||exp(-itH)psi-U_R(t)P psi|| <= (1+12v|t|) sqrt(E/g_R).       (1)

The P and Q errors are orthogonal, so sqrt(1+(12v|t|)^2) may replace 1+12v|t|; no use of this optional sharpening is needed. Formula (1) compares a normalized exact vector with an intentionally unnormalized finite vector for a general input. It is not a nonlinear encoding channel.

Extend the argument to all normalized finite-form-energy inputs by spectral approximation in the H form norm. Bounded V makes H and K form norms equivalent; energy and vector convergence pass through the bound. Equivalently the forced projected integral equation extends by continuity because P V Q is bounded and the finite projection lies in D(K). No differentiation of a rough vector is silently assumed.

If psi is already inside P, U_R(t)psi is normalized, and (1) is a deterministic approximation without postselection. The input energy is E=<psi,H_R psi>=<psi,H psi>. H_R conserves its own finite energy exactly, but the embedding does not intertwine H and H_R on all inputs; finite/full dynamics are only close by the stated estimate.

For arbitrary psi let p=||P psi||². The projection success probability obeys 1-p<=E/g_R. If p>0, normalize phi=P psi/sqrt(p). Comparing U_R(t)phi instead adds exactly 1-sqrt(p), bounded by sqrt(E/g_R), to the right side of (1). Hence

 ||exp(-itH)psi-U_R(t)phi|| <= (2+12v|t|)sqrt(E/g_R).

Success is not guaranteed for every finite-energy input: if E/g_R>=1, the energy estimate alone gives no positive lower bound on p. The preparation/postselection probability must be retained. An efficient deterministic preparation of phi is not provided.

## 4. Support and a genuine noncommutation control

K_R is a sum of one-link electric operators. Every plaquette multiplication term acts on four actual link registers, and product compression P V_f P retains that four-register support on the finite tensor carrier. The exact gauge action survives, since both P and V_f commute with it. Projected multiplication by a fundamental link matrix is generally not a group-valued unitary and does not satisfy the untruncated link multiplication algebra. We do not replace this projected operator by a unitary of the same name.

For a direct adverse control, take R=0 and the normalized constant physical vector 1. Haar integration gives <1,V1>=6v. For each face write ReTr U_f=(chi_3(U_f)+chi_bar3(U_f))/2. The twelve oriented fundamental/antifundamental face characters are orthonormal: on the same face this is Schur orthogonality; distinct faces possess an edge absent from the other, whose nontrivial matrix coefficient integrates to zero. Thus

 V1=6v*1-(v/6)sum_(six faces)(chi_3(U_f)+chi_bar3(U_f)),
 ||Q_0 V1||²=12(v/6)²=v²/3.

For v>0, [P_0,V] is therefore nonzero even on the actual physical sector. This rules out an erroneous exact commuting-cutoff claim. The leakage sits in the R=1 link carrier but is not retained by R=0. Its Haar argument is analytic, not an arbitrary surrogate matrix fixture.

## 5. Meaning of the finite resource statement

For prescribed E and time horizon T, choosing R so g_R>=(1+12vT)² E/epsilon² suffices for (1) uniformly |t|<=T. For already-prepared cutoff inputs this is a normalized-state error guarantee. For arbitrary finite-energy inputs use the larger normalized-projection bound and separately report success probability. The exact local dimension gives a finite explicit memory cost after R is chosen. No uniform approximation of arbitrary unbounded-energy inputs by a fixed finite carrier follows. No spatial continuum, full hardware compilation, physical clock selection or action-selection claim is made.
