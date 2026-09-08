# Ideal CT face heatbath: irreducibility through constant-path atoms

## Domain and conclusion

Root supplied the earliest-event deletion route before this derivation. This proof checks that route, importing the already reviewed CT face quotient conditional, not its finite-precision implementation. No sampling or computation is used.

Fix a finite plaquette-connected seed component C, a finite face-label menu of size M, finite total duration T>0 and finite real V. Each legal label acts as an involution on its legal states and has positive unit offdiagonal weight. The actual L2/L4 menu has distinct masks. A separately supplied repeated-label menu is allowed if all event labels and their individual positive rates are retained consistently. Choose each label with a fixed positive probability. The update is the exact whole-time free-endpoint conditional for that one label. It has no event cap, numerical rejection, pinned endpoint, or success-conditioned retry.

Then the resulting random-scan kernel is reversible and pi-irreducible on the space of finite strictly ordered legal labeled paths. It has an accessible constant-path atom with positive one-step self probability, hence is aperiodic in the irreducible-chain sense. These are qualitative statements. This argument does not prove a usable convergence time, a uniform minorization, finite expected hitting time from every path, or pointwise Harris recurrence from every exceptional initial state. It does not certify that the floating prototype has these properties.

## Probability space and normalization

A path consists of x0 in C and n>=0 strictly ordered times0<t1<...<tn<T with a legal label word. Use counting measure on x0,n,labels and Lebesgue measure on each time simplex, restricted to legal words. Its density is exp[-V integral_0^T Nf(x(t))dt]. Here0<=Nf<=M; every legal word's density is strictly positive. The total mass is bounded above by |C| exp(|V|MT) sum_n (MT)^n/n! and is positive. Thus normalization is finite. Countably many n/words suffice, while times remain continuous. Paths with coincident/boundary events or infinitely many events are excluded; they have zero target measure.

For n0 each constant path a_x is a genuine atom of pi, with positive mass proportional to exp[-V T Nf(x)]. These are not zero-measure individual positive-event trajectories. Their positive masses are the mechanism that makes the following reversal argument possible.

## Positive-probability deletion of the first label run

Take a legal path with n>0 and let p label its earliest event. Let r>=1 be the length of the initial consecutive run of p labels, ending just before the first non-p event, or at the end of the trajectory. The p orbit stays fixed through that run. The exact conditional retains all non-p events with their times/labels and the corresponding distinct p orbits.

Choose the new free initial state to be the state immediately after that initial run. Demand zero p events in the first retained-event interval. Its interval start and end now coincide in that state, so this event has positive conditional weight: the no-switch diagonal propagation is strictly positive, and the original continuation supplies positive compatibility and endpoint weight. No forbidden pinning of the original initial state is imposed.

In every later interval demand the same number of p events as in the original path, with event times in disjoint open neighborhoods around their original times. Choose those neighborhoods strictly inside their retained-event interval and preserve their order. The legal alternating p state sequence and the retained-event compatibility are unchanged. The density on this finite product of neighborhoods is strictly positive. Therefore the complete conditional event has positive probability. No claim that any original continuous time is reproduced exactly is needed. When there are no remaining non-p events, simply choose the constant post-run state and the no-event atom.

Every path in this conditional event has n-r events, fewer than n. Choosing p itself has positive random-scan probability. This construction also works when a distinct retained label has the same physical mask: it remains a retained event; deleting p does not delete that label or change its compatibility. There are no such native L2 aliases in the actual menu.

## Finite-step accessibility, without a uniform success probability

Let B denote the finite set of constant paths. For every path with at most n events, the probability to reach B within n updates is strictly positive. Induct on n. The preceding first update has positive probability of producing paths with fewer events. By induction each such resulting path has positive remaining hitting probability; the integral of an everywhere positive measurable function over a positive-probability set is positive. This avoids selecting a single zero-measure continuation or assuming a uniform lower bound over the neighborhood.

Equivalently, one can pad a shorter successful sequence with self-holds at B to obtain a positive fixed-step transition probability. This proves finite-step accessibility, not that the chain reaches B almost surely in at most n steps or has any uniformly bounded waiting time. Label choices and conditional probabilities may be extremely unfavorable as n,T or volume grow.

## Communication of constant atoms

If y is obtained from x by one legal face flip p, the conditional class of the constant path a_x contains the constant path a_y. With both free interval endpoints at y and no p switches, this has strictly positive conditional probability. Thus the legal configuration graph gives a finite sequence of positive-probability transitions between any two constant paths in C. The same conditional also returns a_x with positive probability, so each constant atom has K(a_x,{a_x})>0.

Fix one constant a. Every admissible finite path has a positive K^k(x,{a}) for some finite k, using deletion and constant communication. The k can depend on x; no universal bound is asserted. Constant holding permits padding where required.

## Reversibility yields access to every positive-measure set

Each exact conditional is a Gibbs heatbath for the disintegration by the selected-label quotient, hence is pi-reversible. A state-independent positive mixture remains reversible, as does every power K^k. For any measurable A with pi(A)>0, define A_k={x in A:K^k(x,{a})>0}. Their countable union is A, so some k has positive pi measure. Therefore

 pi({a}) K^k(a,A) = integral_A K^k(x,{a}) pi(dx) > 0.

From arbitrary x, first reach a with positive finite-step probability, then use this positive transition into A. This proves pi-irreducibility for the explicitly defined finite-path state space. The positive self-loop at the positive-mass accessible atom prevents a nontrivial cyclic period. It is not necessary to claim positive probability of reaching a particular nonconstant path.

## Scope and next obligations

The result rules out an exact invariant decomposition of this ideal random-scan conditional finer than the chosen legal seed component. It does not identify components by flux, enlarge C, or prove rapid thermalization. State-dependent face-selection rules need their own invariance argument; finite fixed scan schedules are not the reversible mixture proved here. The continuous-time target is exp(-T H) with free endpoints, not a finite-G power; old projection half-time tau corresponds to totalT2tau only in the matching convention.

No quantitative diagnostic threshold or production change follows. A finite event budget, tape exhaustion, floating atom ambiguity, and rejecting failed proposals without a valid correction can change this ideal kernel. The implemented prototype is explicitly outside the exact-kernel conclusion until those choices are separately controlled. Previous L8 mixing failures remain unchanged evidence.
