# Post-freeze comparison

Complete orbital proof read after native edf1d16c was frozen. Compared SHA65411b7942e7e6f33e224e4053669b080ab0287e229766b6e50bdb929d69eefc. PASS: the exact Schur/folded scalar, native24-order signs, both adjacency-denominator classes, orientation factors and repeated-edge diagonal all agree. Orbital additionally checks the single-edge coefficient against the exact two-level energy; native uses direct folded-word controls. Neither source imports a supplied RK potential from the kinetic calculation. This is a same-session mathematical comparison, not a formal audit or historical priority claim.

Native preserves L4 winding cycles and explicitly states that a positive coefficient relative to a fixed S convention is not a basis-invariant obstruction. Its stronger remainder wording is finite-volume only and follows the even-in-g Schur kernel; no uniform-volume convergence claim is imported from orbital.
