# Independent thermal quadratic consequence

Root exposed the candidate inequality before this derivation; this is an independent algebra/scope review, not an unexposed discovery. No physical computation. The existing state-independent expectation bound |Tr rho V|<=sqrt(75N Tr rho K) and U0 magnetic moment theorem are inputs. H_U=H0+U(cN I+V), c=3/2, U>=0; all Gibbs states are full physical finite-dimensional states at the same positive beta.

Let rhoU and rho0 denote their Gibbs states. Direct logarithms, without commuting Hamiltonians, give

 S(rhoU||rho0)=beta(FU-F0-U cN-U<V>U).

The rho0 variational trial has <V>0=0, so FU-F0<=U cN. Consequently S<=-beta U<V>U<=beta U sqrt(75N<K>U). Nonnegativity of S also implies <V>U<=0 for U>0, consistently with this estimate. No classicalization, Golden–Thompson step or commutation of V and H0 occurs.

For 0<s<beta*kappa, [K,H0]=0 allows the entropy variational inequality

 s<K>U<=S+log Tr rho0 exp(sK).

The existing moment theorem gives log moment <=log8+3N log(1+exp(-(beta*kappa-s))). Put d=<K>U/N and A=log8/N+3log(1+exp(-(beta*kappa-s)))>0. Thus

 s d <= beta U sqrt(75d)+A.

Set y=sqrt(d)>=0. The quadratic s*y²-beta U sqrt75*y-A has one nonnegative root. Since s>0, the inequality is equivalent to

 d <= [(beta U sqrt75 + sqrt(75 beta² U²+4sA))/(2s)]².

At s=beta*kappa/2, with x=U/kappa and c=beta*kappa,

 d <= [sqrt75*x+sqrt(75*x²+2A/c)]²,
 A=log8/N+3log(1+exp(-c/2)).

This can be minimized with3 and the earlier bound3x+2A/c. It is valid for any state-independent kappa certified for the U0 thermal moment, in particular kappa=3h/800 at M>=32,beta*h>=200. At U=0 the expression equals2A/c, the original entropy-moment floor. At fixed x and beta->infinity with kappa fixed, the upper expression tends300x². This is an upper-bound limit, not a convergence statement about states; it is weaker than the separate zero-temperature75x² bound. For nonzero thermal floor the expression has a cross term linear in U, so it should NOT be described as a pure O(U²) bound at fixed finite beta. The correct claim is a quadratic-root bound that approaches a quadratic upper bound as the floor vanishes.

No nonzero-U reflection positivity, contour bound, thermodynamic phase or uniform spectral gap is concluded. The existing full-carrier electric selection and native U0 moment assumptions are unchanged. The algebra and quantum ordering are sound.
