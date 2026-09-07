# Literature bridges

This file records attribution and applicability already stated in the theorem
note. It does not use literature as executable evidence or audit authority.

## Standard external machinery

- Setia and Whitfield, [Bravyi-Kitaev Superfast simulation of electronic
  structure](https://arxiv.org/abs/1712.00446), especially equations 20-27 and
  35: standard BKSF edge generators, loop checks, and hopping dictionary.
- Setia, Bravyi, Mezzacapo and Whitfield, [Superfast encodings for fermionic
  quantum simulation](https://arxiv.org/abs/1810.05274), Appendix A: spanning
  tree and independent loop-check machinery.
- Aberg, [Catalytic Coherence](https://arxiv.org/abs/1304.1060): established
  energy-translation/coherence resource background.
- Chiribella, Yang and Renner, [Fundamental energy requirement of reversible
  quantum operations](https://arxiv.org/abs/1908.10884), together with
  [Coherence cost for violating conservation laws](https://arxiv.org/abs/1906.04076):
  established energy-conserving lift and coherence-cost context.

These references support known machinery. The block does not claim BKSF,
one-bond deletion, translation batteries, or shared-battery composition as new
physics.

## Repository overlap and the narrower contribution

Current-main finite cycle/cocircuit and cube conditioning/equality work supplies
nearby finite algebra. At their pinned heads, PR #7883 contains sea-specific
edge/star statistics and PR #7895 contains one-bond deletion. PR #7979 treats a
different occupation-site projection and site-hop deletion process with a
shared apparatus comparison.

The narrower connection here is the repeated native physical edge-Z process:
nonbridges preserve the surviving CAR state, bridges expose signed component
parity, old edge signs remain in original BKSF words, total number persists, and
uniform edge deletion has a common energy ledger. It removes a separate
occupation-to-Record compiler only for this alternative instrument. It does not
turn the native-edge event into the prior site-deletion event.

No unmerged claim grade or audit conclusion is imported as authority.
