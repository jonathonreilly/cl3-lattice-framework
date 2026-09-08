# Single-interval continuous-time bridge: independent derivation

Root supplied the candidate Doob transform before this work; the derivation below independently checks it. The complete30391f9 CT face-panel proof was read. This note supplies one interval primitive, not the global conditional, sampler implementation, efficient mixing theorem, or a finite-G identification. All geometry, selected-label multiplicity, retained-event compatibility and endpoint-message obligations remain those of that panel.

## Signed difference and Perron transform

After subtracting a common scalar, write B=[[0,m],[m,-d]], m>0, d real. For one selected geometric label m=1. Only if ALL aliases of the selected physical flip are removed from the retained skeleton does m equal their multiplicity. A singleton has no switches and cannot use this2x2 primitive.

Put r=sqrt(d²+4m²), a=(r-d)/2, b=(r+d)/2. Then a,b>0, ab=m², a+b=r, and h=(1,a/m) obeys Bh=a h. Therefore

  Q=diag(h)^-1 B diag(h)-a I=[[-a,a],[b,-b]].

Its stationary probabilities are pi0=b/r, pi1=a/r. For t>=0,

  P00=pi0+pi1 exp(-rt),  P01=pi1(1-exp(-rt)),
  P10=pi0(1-exp(-rt)),  P11=pi1+pi0 exp(-rt).

The transfer is exp(tB)_ij=exp(at) h_i Pij(t)/h_j. The diagonal h factors telescope along a continuous trajectory and become a constant at fixed endpoints; the exp(at) factor also is constant. Thus fixed-endpoint B bridges equal Q bridges. This does not mean that unconditioned Q paths have the B free-endpoint law: endpoint h weights and global backward compatibility messages still matter.

For stability, the root's rationalized a=2m²/(r+d) is suitable for d>=0, but NOT uniformly for signed d: r+d cancels for large negative d and can round to zero. Use b=r/2+d/2, a=m*(m/b) when d>=0; use a=r/2-d/2, b=m*(m/a) when d<0. This also avoids squaring a very large m when the final rates remain representable. If either positive rate becomes zero or nonfinite in the working precision, reject or increase precision. One may instead reorder states so d>=0, but must transform every adjacent compatibility matrix and endpoint index consistently.

## Waiting time, atom, and conditioned hazard

Fix current state s and endpoint j at remaining duration T. Let H_s(u)=exp((T-u)B)_sj. Provided H_s(0)>0, the probability of NO switch through elapsed u, 0<=u<=T, is

  S_sj(u)=exp(Bss u) H_s(u)/H_s(0)
         =exp(-q_s u) P_sj(T-u)/P_sj(T),

where q0=a,q1=b. This follows by factoring the no-event weight over[0,u] and summing all continuations. Its derivative is -m exp(Bss u) H_(1-s)(u)/H_s(0), hence it is nonincreasing. The conditional event hazard is m H_(1-s)(u)/H_s(u), equivalently q_s P_(1-s),j(T-u)/P_sj(T-u).

For s!=j and T>0, S(T)=0: a switch is forced before the endpoint. For s=j, S(T)=exp(-q_s T)/P_ss(T)>0, an atom for no event at all. A first-wait inverse must retain that atom; it must not force every same-endpoint interval to contain an event. At T=0 equal endpoints have the deterministic no-event bridge, while unequal endpoints have zero normalization and must reject. A singleton likewise has only no-event paths, with compatibility deciding whether that interval has support.

A supplied CDF level u in[0,1) is in the no-event atom when s=j and u>=1-S(T). Otherwise solve log S(t)=log(1-u) monotonically on[0,T]. Repeating this primitive after a switch would construct a bridge in ideal arithmetic, but such event recursion and its resource behavior are NOT implemented or validated here.

## Log-domain implementation limits

Use log P, logsumexp for diagonal mixtures, and log(1-exp(-rt)) via expm1/log1p for offdiagonals. This avoids exp(at), which can overflow for perfectly well-conditioned bridge probabilities. Evaluate log S=-q_s u+log P_sj(T-u)-log P_sj(T). The implementation may return -infinity for the exact forced endpoint; it does not silently clip a small positive denominator to zero.

The supplied deterministic inverse returns a floating bracket, not a certified exact random sampler. When a CDF or an atom is within floating error of the supplied level, rigorous exact sampling would need higher precision or interval refinement. No finite precision can promise uniform accuracy over arbitrarily small rates, rare endpoints, or enormous products. Our implementation rejects nonrepresentable rate/product cases and reports its domain. Large rt can be handled without evaluating its tiny exponential; that numerical limiting evaluation is not an exact symbolic zero-tail assertion.

The Doob transform removes the large common Perron growth and makes the bridge law explicit. It does not prove that rare endpoint conditioning, the number of switches, global compatibility sampling, spatial mixing or local event indexing is cheap. Those are separate obligations before a continuous-time cost profile.
