# Actual two-round noncommuting native click instrument

Prospective fixture is recorded in PREREGISTRATION. Use the8-edge/9-vertex tree with path0–1–2–3, detectors4,5,6,7 at0,1,2,3 and parity reservoir8 at3. The full physical carrier has256 dimensions. Ready modes2,3,4,5,6,7 are vacant; the remaining four ready columns have logical occupations00,01,10,11 and correlated reservoir parity. Native hops are built independently as sparse bit-action matrices using the ordered edge-neighbor Z signs. No author matrix module is imported.

Each round has an actual waiting pulse W=exp(-i theta T_active), cos theta4/5,sin theta3/5, followed by two detector pulses with r0=3/5,r1=5/13 and complete two-leaf Z projections. Let D=r0^n0 r1^n1 and C=D W on the ready coordinates. Unlike the scalar/no-wait law, D and W do not commute. The explicit continued matrix in ordering00,01,10,11 is

 C = diag-block(1, [[4/13,-3/13],[9/25,12/25]],3/13).

The first round uses T01 and leaves4,5. Its physical transport R=Utransport Vready uses exactly the four prescribed whole hops. Full columns obey K00=R C, not a phase-erased probabilistic surrogate. The checker independently verifies T23 R=R T01; therefore the second waiting pulse on2,3 uses the same logical W while retaining the physical transport phases. Second leaves6,7 are fresh. No second transport is needed for this finite fixture.

Define F_ab=(1-r0²)^a n0^a r0^[2(1-a)n0] times(1-r1²)^b n1^b r1^[2(1-b)n1], with the a=0,b=0 factors interpreted directly as powers and a=1 factors as occupation projectors. Each round effect is E_ab=W†F_ab W. All four are verified independently against physical Kraus columns. Thus the finite first-positive POVM is

 first round: E10,E01,E11;
 second round: C† E10 C,C† E01 C,C† E11 C;
 censored: (C²)† C².

Completeness follows E00=C†C and sum_ab E_ab=I; the actual full-carrier check also sums all16 two-round histories. The second00 full columns equal R C². Ties11 remain ties. Both values of old Record remain permanent throughout all16 histories, and cumulative trailing cuts retain(−1)^a and(−1)^(a+b). Every identity acts on all four input columns and so retains arbitrary reference coherence.

For the two coherent states(|01>+|10>)/sqrt2 and(|01>−|10>)/sqrt2, FIRST-ROUND positive probabilities are0.6442414201183432 and0.8478295857988166. These are not cumulative two-round probabilities; the latter use I−(C²)†C². Their occupation diagonals agree. This is a concrete coherence-dependent waiting/readout law built from the supplied native operators, not an imposed classical hazard. Removed waiting changes the full first-positive effect. No formation time is derived; scheduled zero Records still occur.

Preserved failed control: initial probe used the ±i coherence quadrature. It did not distinguish probabilities because native T is imaginary and W/C are real in this ready convention. The surviving control is preserved as check_BEFORE_COHERENCE_QUADRATURE_FIX.py; changing to the physically responsive real ± quadrature is explicit, not concealed as a first-run success. A subsequent NumPy-int JSON-only failure is also preserved. Final check.py executes49 predicates, including four independent effect comparisons, in well under1second/<64MiB. These finite checks support the explicit operator proof, not an autonomous occurrence claim.

Independent horizon clarification: HORIZON_CONTROL.json computes the cumulative two-round probabilities from I−(C²)†C² as [0.8926857163152548, 0.9720219765526416]. The earlier .64424/.84783 figures remain first-round-only; no values were silently replaced.
