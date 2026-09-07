# Candidate next block: local fuel and a quantum-jump front

Independent design pass by gauge_gravity_frontier; root has not yet certified
its census or proof. This is a candidate, not a new theorem claim.

Place the parent native edge qubits at2v+e_a, one head qubit at2v and one
fuel/latch at2v+e_a+e_b with cyclic b=x->y->z->x. The parity classes are
distinct. The role scaffold and cyclic assignment are supplied; proper-cubic
covariance and one-site nearest-neighbor admissibility are not derived.

On one-head sector, with live fuel n_e and gap Delta>=t, define
H=sum_e n_e(h_e+Delta I),
L_(v->w,z)=sqrt(gamma)|w><v| sigma_(fuel,e)^- Q_(e,z).
Use this time-independent Lindblad generator. Each multibody jump is contained
in the radius-one star of the native edge center; the matter terms retain
the parent's endpoint-star support. A jump moves the head, expends fuel,
locks edge Z, and removes one hopping bond. It supplies a uniform choice of
live incident edge and an exponential dwell of rate gamma*d_R(v), without
an external list of dwells or edges. Born jumps, rate and time are supplied.

Claimed operator identities to independently check:
old Z Records and total N preserved;
L^dag(H)=-gamma sum_(v->w) P_v n_e(h_e+Delta I)<=0.
The latter is dissipation and required reservoir energy, not a conserving
reservoir dilation. Its implementation can hide coherence/pumping costs.
The parent spectral battery lift is not a local implementation merely
because the ideal jump is local.

Candidate exact trail census on the cube: all first four events preserve
remaining-graph connectivity; after fifth connected probability1/2.
Termination probabilities at counts5,6,7,8,9 are
(1/8,1/8,11/32,1/4,5/32). Root must independently reproduce these numbers.
Thus the minimal intended demonstrator is all24 four-edge paths and16
Record sign histories per path, with matter currents and densities computed
rather than inferred from graph connectivity. Do not erase fifth-step
disconnection by dropping unfavorable paths.

Exponential dwell average can be computed deterministically in the current
energy eigenbasis: Phi_r(rho)_(a,b)=r/(r+i(E_a-E_b))*rho_(a,b).
This is a candidate exact finite ensemble route, not yet a computation result.

Principal remaining gap: local reservoir/battery realization with coherence,
energy and entropy costs. Finite closed Hamiltonians do not supply strictly
irreversible monotone recording indefinitely. The finite graph depletes;
continuing formation would advance into unrecorded regions, never reset old
Records or silently replenish the fuel.
