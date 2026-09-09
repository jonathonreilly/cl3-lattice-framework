# H3 — distribution dependence is not conditional trajectory dependence

H0b2 run_from holds the externally supplied CHOICE words fixed while perturbing other lanes. The whitelist establishes lane diagonality conditional on those words. It does not establish that the law assigning probabilities to the words is neighbor independent. The paper itself leaves that probability law/support unresolved in H0c2.

Finite witness: update y := b is lane local once its external bit b is supplied. Let an external seed U be uniform on {0,1,2,3}, and let b=1 iff U<1+2n for a neighboring condition n in {0,1}. Then P(y=1|n=0)=1/4 and P(y=1|n=1)=3/4 although the update contains no cross-lane state access. This is an exact implication counterexample, not an axiom-complete physical model or an introduced supplier.

Repair: retain independence of deterministic trajectories conditional on fixed choice words. A distribution-level noncommunication statement additionally requires a choice law independent of the other conditions. Avoid both an unconditional Admissibility refutation and a claim that cross-lane deterministic gates are the only successor route.
