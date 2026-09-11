# c-sector det exponent — probe verdict (ex2 decisive probe, 2026-08-24)

Exercise tier, read-only; nothing claimed, registered, or adopted. Runner:
`det_exponent_probe.py`, 21/21 exact checks PASS, ~3 s, no float in any decision.
Fixture: `Bench("12x6",12,6)`, constant carrier (volume 7/5; shear 0 on pinned
levels {0,1}, 3/5 elsewhere), dials s_x=3/5, s_t=0, m=1 — the b180/b181 fixture,
all landed identities reproduced (a=43/35, d=129/175, w_1=875/1462, w_4, orbits,
joint flip, sigma). Measure: the landed Z of H1-170b (closure-audit-two lines
137-141), exp(-phi^dagger Q phi) with G = Q^{-1} full — the same declaration the
ACCEPTED b179 cell consumed (b179 T3/T4); its Wick rule has no phi-phi channel.

## (a) Calibrators — both read by the b179-accepted operation (restriction)

- b179 accepted cell f_(1,0,0): beta = 3193/2240 reproduced exactly. ONE complex
  slot <-> ONE det factor to the FIRST power (det_C[[beta]] = beta; realified
  det beta^2; 2 real integration dims). Fixes the per-slot det currency.
- Level-4 singleton fiber (the other reflection-fixed level, chain-coupled — a
  restriction cell, not a Z-factor): D4 = (1817/1120)(I + (3/5)J) — the b = a*s_x
  law again. ONE 2-dim fiber-object <-> ONE conjugate-pair det factor
  det D4 = a4^2 + d4^2 (power 1, never squared). Fixes the per-cell unit shape.
- The unit in the c-sector's own currency: one orbit-cell (= one hyperbolic
  Witt cell = one complex slot) <-> det content a^2 + d^2 = 62866/30625.

## (b) The c-sector's total det factor over the four eigenlines

The record slice decouples exactly (verified both ways), so its restriction is a
TRUE multiplicative factor of Z: det Q = det(slice) x det(rest) exactly. On the
four eigenlines the sector block is diag(lam+, lam-, lam+, lam-); the arbiter's
own det_cpair gives, and the basis-free site extraction det(slice)/det(k=0
fiber) confirms:

    F_c = (43/35 + 129i/175)(43/35 - 129i/175) x (same, chart 2)
        = (62866/30625)^2 = 3952133956/937890625   — EXPONENT 2, not 1.

The committed covariance carries all four eigenlines with independent conjugate
legs: B_k^dag G B_k = (aI - dJ)/(a^2+d^2) for BOTH charts, invertible, no
anomalous channel — the unconstrained-Gaussian signature. 8 real integration
dims on the sector (2 orbit-cells; W_R real-form content 4 real dims, n=2),
never the 2-real-dim Fix(sigma) carrier.

## (c) Verdict, in ex2's terms

EXPONENT 2. Additive counting is what the committed measure contains: n = 2
cells -> r = 1 -> Q = 1 with no further premise. Quotient counting is FALSE of
committed structure. Q = 2/3 therefore requires exactly one new physical input —
the sigma-reality bit: carrier = Fix(-Theta o X0) = {z g+ + zbar h+}
(equivalently, orienting the staggered grading) — a proposal for Jon's bar, not
a derivation. Verified in-runner: sigma is an antilinear involution of E+ built
only from landed objects; imposing it is the (62866/30625)^1 measure, which the
landed Z exactly is not.
Outcome 3 (cancellation) does NOT fire: the factor is pinned, present, and
unique in the landed Z. The honest sharpening it leaves behind: every landed
normalized window is G-built and det-blind, so the exponent is invisible to all
landed observables (why three checker rounds found no entailment) and its sole
downstream consumer is the fork's r. Scope: constant carrier (b180's volume
carrier-lock stands), s_x != 0, this fixture class; H1-170b is the measure's
provenance — rejecting that field content now would also unland b179's own
accepted cell, but demoting window-invisible field content IS the named
Record-primacy taste argument, and it decides nothing by itself (no-registration
theorem: no record reads the orbit label).

## (d) Composition with the Witt result

The two computations govern different quantities and compose without conflict.
The Witt computation is about the READOUT unit: under the physical reflection
pairing every single eigenline is isotropic (unnormable alone) and the minimal
readable object is the orbit-cell — and that cell's det content, lam+ lam- =
a^2+d^2, is exactly one complex slot's, which is the same unit this probe's
calibrators fix. So the Witt result legitimately converts "four eigenlines" into
"cells": it kills line-counting (n=4). What it does not and cannot supply is the
MULTIPLICITY: the landed measure contains TWO such cells — F_c = (cell)^2 — so
the step in the Witt reading from "the minimal readable unit is the orbit-cell"
to "r = 1/2" silently selects ONE cell, which is the same one-orbit selector
premise b181-C4 named; readout structure cannot delete integration content. The
fork arbiter's semantics are measure-native (Gaussian/Berezin det powers), so
the Koide r consumes the measure count, not the readout unit: n = 2, r = 1,
Q = 1 as committed; Witt fixes the unit, this probe fixes the count, and the
one sigma-reality bit (select/identify the two cells) remains the entire gap
between the committed structure and Q = 2/3.
