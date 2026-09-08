# Route portfolio — light lane

## Prior-art sweep — origin/main @ e249016f75, 2026-09-05
  git grep -n -iE "(yee|maxwell.*uniqueness|uniqueness.*maxwell|landing.core.*light|emergent.*maxwell|photon.*dispersion)" origin/main -- 'docs/*.md'
  git ls-tree -r --name-only origin/main -- docs/ | grep -iE "YEE|GAUSS_LAW|GAUGE_LAW|LANDING_CORE|MAXWELL|PHOTON"
Hits: AXIOM_FIRST_STEFAN_BOLTZMANN (omega = c k as an input — context only);
WAVE_EQUATION_SELF_FIELD (a Yee-style stencil in an older wave lane — not the
gauge generator); TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE (June; a
Record-side invariance profile — non-matching); older U1 notes (fermion
number conservation, ABJ, flavor idempotents — non-matching). Target: OPEN.

## Approach families for the science block (block 02, chosen from the ledger)
G1 class-restriction derivation — object: #7917's declared class; mechanism:
   reversibility + Record locality forcing first-order/linear/NN; terminal:
   the class as a theorem of the tick structure (strength: would make the
   uniqueness classification unconditional within the framework).
G2 the time-selection fork — object: #7915's Yee time selection; mechanism:
   the Record tick order; terminal: which time selection the framework's
   record structure supplies.
G3 the 3D photon dispersion exponent — object: the transverse mode of the
   spin-half cubic ice at zero vs finite detuning; mechanism: finite-size
   scaling of #7945/#7959's estimators; terminal: is the linear term a
   detuning supply or a derived crossover.
G4 the germ from the Record overlap law — object: #7886/#7887's kappa > 0;
   mechanism: representation positivity; terminal: derive "positive isotropic
   quadratic germ" (#7884's hypothesis) from the Record overlap law itself
   (partially covered).
Block 01 is meta (landing core + ledger); the value gate V1-V5 is applied to
block 02's candidate before any science PR.
