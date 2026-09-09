# Independent Riccati disk review

Disposition: PASS for the mathematical conditional theorem. Reviewed full DERIVATION.md SHA256 74531a247599e2dd0bb11c09bd24d0764bd81933a2f025607fb9b2de0effb15e and its two declared parent imports. No physical computation, numerical stability certificate or alpha claim follows.

## Signs and constants

With f=(a+ib)/2, a=f+f† and b=i(f†−f), direct ordered CAR expansion gives the stated H and K, including the relative scalar −Tr(D)/2 in finite dimension. The creation coefficient is K, not −K. For K=kJ the even off-diagonal matrix element is k and normalization by the vacuum coefficient gives z′=−k−2mu z+kz². This agrees with (1).

The normalized skew norm is bounded by 33/50. Applying H>=S/150 to both arguments gives the stated constant 99 without assuming bounded H inverse. The actual parent accretivity constant is consistent with 1−1/3−33/50=1/150. The strict disk inequality has margin 2r−99(1−r²)=99/10000.

Independent exact multiplication verifies (5), including A transpose and the sign of ZHZ. For real skew Z, vᵀZHZv=−(Zv)ᵀH(Zv), and vᵀ(KZ+ZK)v=2vᵀKZv. The forcing lower bound therefore follows for every skew Z, with no circular use of the disk. The nonautonomous congruence formula is valid for bounded operators and proves M>=0 on each local existence interval. Uniform operator norm prevents finite-time blowup. The real skew subspace is invariant under the vector field.

## Infinite-dimensional identification: explicit completion of the brief approximation sentence

This part of the draft is terse but can be justified without adding a spectral gap or an overlap premise. Choose real finite-rank orthogonal projections Pn increasing strongly to I. Let Hn=Pn H Pn and Kn=Pn K Pn. Their weighted inequality remains true on the compressed space; positivity and the same disk proof are inherited. Hn converges strongly with uniform norm bound and Kn converges in trace norm.

The trace-ideal differential estimate is

 ||Z′||1 <= ||K||1 + (2||H||+r||K||)||Z||1

on the disk. It bounds the trace norms uniformly on every fixed finite time interval, both for the original and compressed equations. For the limiting trace-class solution, (Hn−H)Z(t) and Z(t)(Hn−H) converge in trace norm, uniformly on compact time intervals by compactness of its continuous trace-class trajectory. The integral equations and Gronwall then imply Zn→Z in trace norm uniformly on each finite time interval. Thus their normalized Gaussian vectors converge: the Fredholm normalization and Gaussian exterior series are continuous in this topology on the common disk.

For identification with the actual evolution, dGamma(Hn) converges in strong resolvent/semigroup sense to dGamma(H), as follows directly on every finite particle sector and then by contraction and density. The pair creation plus annihilation operator associated with K is bounded for trace-class K (its norm is bounded by a fixed multiple of ||K||1), and the compressed pairing operators converge in operator norm. Bounded-perturbation semigroup convergence identifies the limits of the finite Gaussian evolutions with the actual quadratic evolution. The finite relative scalar from the parent theorem changes normalization only. The limiting unnormalized vector is nonzero, and the parent positive reference chart fixes its phase consistently. Hence normalization yields precisely the Riccati solution. This also supplies the missing details behind the draft's approximation sentence; no quantitative convergence rate is implied.

## Controls and limits

The separately frozen check.py executed once on synthetic 2/4-mode rational matrices only: 11 exact predicates passed, including arbitrary-skew Lyapunov identities and independently constructed ordered-CAR Hamiltonians. A deliberately reversed Hamiltonian comparison is merely an algebraic negative comparison, not a native source mutant. See RESULT.json and TIME.txt. These controls support signs; the uniform infinite-dimensional theorem rests on the argument above.

The disk estimate alone does not bound determinants independently of trace norm, prove well-conditioned long-time discretization, control a compressed native moment basis, or imply a mixed-impurity overlap or alpha sign. The source appropriately excludes these claims. The review is independent of this new Riccati proof's authorship; the reviewer authored related earlier finite-excitation material, which is an explicitly disclosed parent dependency.
