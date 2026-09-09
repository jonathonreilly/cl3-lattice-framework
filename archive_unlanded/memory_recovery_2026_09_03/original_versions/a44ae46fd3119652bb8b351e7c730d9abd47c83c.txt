# Memory-only science recovery — 2026-09-03

**Status:** historical recovery and classification record. This file preserves
work that was reported in campaign memory or found in temporary scratch space.
It is not a retained-theorem surface, an audit verdict, or a TOE-score change.
Every item must be read at the evidence level stated below.

## Why this recovery exists

An older campaign rule incorrectly treated a missing audited parent chain as a
reason not to open a PR. That condition can govern promotion, but it cannot
govern preservation. Interesting completed science belongs on a remote review
surface even when it is exploratory, blocked, superseded, or not currently
useful to an obligation.

This recovery inspected the repository archive, the off-ledger census, local
and remote Git refs, extant worktrees, temporary campaign directories, and the
project-memory summaries. Evidence labels used here are:

- **R — raw recovered:** scripts and/or output survived and are copied into
  this PR.
- **M — memory report:** a detailed contemporary campaign report survived, but
  its temporary executable artifact was not located. This records the report,
  not an independently re-established result.
- **S — status correction:** an old “not landed” marker is stale because a
  later PR, salvage commit, or stronger result now carries the science.

## Repository-scale survival result

The historical archive was not erased. At the recovery base, `archive_unlanded/`
contains 1,021 files (about 15 MB), including the large 2026-08 intake. The
off-ledger census at
`docs/repo/science_census_unledgered_index_2026-08-05.json` records 3,621
source records / 3,408 unique paths across overlapping strata. PR #6015 is the
historical census review surface and PR #6018 is the first intake surface;
their content was subsequently preserved on `main` even where the original PR
state is closed rather than merged.

That establishes broad survival, not byte-for-byte completeness. The known
temporary-only gaps are listed below.

## Raw campaigns recovered in this PR

### R1. Record ticks after a local Record event (**R**)

Source directory at recovery time: temporary campaign folder `L3c/`. The
design, runner variants, theorem probe, and principal outputs are preserved at
`archive_unlanded/memory_recovery_2026_09_03/record_ticks/`.

The finite cube probe reports:

- a 384-dimensional forbidden subspace inside an 896-dimensional space,
  organized as 12 corner pairs times 32;
- zero pre-event ground-state `Q` norm in the tested construction;
- after one Record projection, positive conditional Hamiltonian variance on
  every tested branch (minimum reported `0.25` for the Record term and `0.75`
  for the full Hamiltonian), so the projected branch is not an eigenstate in
  this model;
- forbidden mass growing from zero with the reported small-time quadratic
  behavior (`1.250e-5` at `t=0.01`, `1.24584e-3` at `t=0.1`);
- an empty joint kernel for all tested Record-conditioned Hamiltonian
  differences.

The larger campaign report additionally records schedule dependence up to
`L1 = 1.10`, a non-dephased `p -> 0` behavior, and a control scale of order
`tau/p`. Those statements are memory-level until regenerated from a curated
runner. The scientific use is bounded: this is evidence that Lüders projection
alone does not specify a dynamically invariant update in the explicit tested
cube construction. It is not an unrestricted statement about Record dynamics.

### R2. Half-filled staggered-flux matter with nearest-neighbor interaction (**R**)

Source directory at recovery time: temporary campaign folder `L1h/`. Twelve
scripts and their surviving text logs are preserved at
`archive_unlanded/memory_recovery_2026_09_03/half_filling_nn_interaction/`.

The exact-diagonalization probes report:

- on the `2x2x2`, `N=4` cube, the all-negative flux sector is the unique
  minimum over all 32 tested sectors for sampled couplings from `g=-64` through
  `g=+256`;
- at `g=0`, the compared energies are `E_+=-6` and
  `E_-=-4 sqrt(3)`, and the large-positive-coupling comparison approaches the
  reported cubic tail `g^3(E_- - E_+) -> -27`;
- on `2x2x3`, `N=6`, the same sector remains unique at `g=-2,-1,+8,+16`
  but is reordered for sufficiently attractive interaction; the fine scan
  places the sampled transition between `g=-2.3` and `g=-2.4`;
- a larger-torus first-order estimate suggests a negative-coupling crossing
  near `g=-5.4`, but that item is a perturbative diagnostic, not an exact
  finite-volume theorem.

This is a useful interaction-stability extension of the free half-filling
selection work, but it remains an unclassified finite-system campaign. The raw
evidence is preserved before any retained claim is drafted.

## Highest-value result reported in memory but missing its runner

### M1. Exact W101 double-commutator cancellation (**M**)

The Round-59 campaign report records the exact operator identity

```text
T2_sad = (1/2) [R,[R,T0]] + 3 T0.
```

Consequently, in the reported second-order eigenstate correction, the explicit
double-commutator term cancels and the remaining diagonal contribution is
`3 T0`, independent of the eigenstate before normalization. The report records
symbolic agreement, a Hermite-basis per-state value of `3.000000`, and a net
double-commutator coefficient tending to `2.8e-11`. It explicitly refuted the
campaign's earlier estimate near `-0.19`.

The original `RUNG_21` temporary runner was not found. A related retained
Rung-20 runner already checks the underlying symbolic polynomial identity, so
this is the first reconstruction target: establish only the exact cancellation
as a narrow theorem, with a fresh independent runner. The wider sign/closure
claim remains open; the same report says a generic heat-inequality attempt had
26 counterexamples in 120 unconstrained trials and therefore required more
structure.

## Additional memory-only reports queued for reconstruction

These entries preserve contemporary reports whose original `/tmp` artifacts
were not located. They are leads, not present-tense conclusions.

1. **Legacy Brannen three-gap report (**M/R**).** Project memory says a
   16-check campaign closed three Callan–Harvey bridge gaps, but its canonical
   note and runner are absent. Two precursor runners survive on a remote
   archive tag and are copied into this PR. Their own prose explicitly leaves
   the physical-radian identification open, so they do not substantiate the
   stronger memory headline. Preserve and re-derive before making any closure
   claim.
2. **Strike-2 transport machinery (**M**).** A two-route Fock-space versus
   single-particle transport comparison reportedly agreed at
   `1.2e-15`–`1.4e-15`, alongside reusable matched-step-null and normalized
   residual machinery. The associated non-autonomy interpretation was later
   invalidated/duplicated and must not be revived.
3. **A4 generation-frame probe (**M**).** A `16/16` reported runner found no
   dynamically selected frame bit in the tested tracial, maximally mixed, and
   einselection setup. This is bounded to those instruments.
4. **Carrier-Z2 to `Gamma_chi` transport (**M**).** A `28/28` report says the
   tested `C3`-equivariant transports lie in the commutant of the representation
   and commute with `Gamma_chi`, while the desired fractional charge required a
   non-equivariant axis in that class. Three reported witnesses were disjoint
   support, central `Z`, and dimension parity.
5. **U23 KCPT classification extras (**M**).** The memory records center
   dimensions `{4:33, 5:3}` over 36 `H` classes; classes 14, 25, and 27 are the
   exceptional `omega=1` cases. Extra 76-dimensional algebras were reported for
   classes 25 and 27, with their types still uncomputed.
6. **Gravity orbit decomposition (**M**).** The `c740` report says 192 used
   columns split into four 48-element symmetry orbits; contiguous 24-column
   blocks were order artifacts and every orbit touched `E0`.
7. **Gravity anchored-cell census (**M**).** The `c746` report records only
   19 of 4,796 splits above the tested cap at `m=18` and the exact observed
   even-`m=2k` cell-count sequence matching square-pyramidal numbers, with the
   anchored count at `m` equal to the licensed count at `m-2`. The formula
   should be reconstructed before theorem use.
8. **Emergent-gravity two-point closure (**M**).** A June campaign reports an
   exact continuum two-point closure. Its cubic residual fell from roughly 70%
   to 30% after adding spin-connection seagulls, while the full covariant
   operator still failed the chosen cubic regulator test. This is a partial
   calculation, not a general obstruction; the original `mom_*`, `spin.py`, and
   `pv_final.py` scratch files were not found.
9. **Koide even-source probes (**M**).** Reports say the tested OS reflection
   positivity expression was conjugation-even and delta-blind, and the tested
   eta base-flux pulled back `C3`-trivially to the `hw1` orbit.
10. **Link-qubit / relational-Record probes (**M**).** June explorations report
   that link-qubit structure can host the tested determinant/Chern–Simons
   mechanism but did not select it, and that the tested relational-record rules
   relocated rather than removed the measure freedom. These are candidate-model
   observations, not proposed axiom changes.
11. **Count-to-radian correction chain (**M**).** The historical sequence
    established that the simple `2π` objection disappears for generators, found
    `Tr(G A C^k)` imaginary or zero for tested real-symmetric `G`, found the
    tested `Q` delta-blind, and found circulant charged-mass eigenvectors
    independent of `delta_e`. A later correction kept a multi-harmonic
    `C3`-invariant spontaneous-breaking route open. The sequence must be read as
    evolving hypotheses, not as a single negative theorem.
12. **Cycle-725 independent gravity cross-check (**M**).** The main result is
    carried by PR #5942, but its separate `c725_adv2.py` verifier was not
    included. Memory records independent HiGHS endpoints
    `108/128/68/128`, matching overlap decisions, a third generic sample
    family, and successful perturbation controls. The auxiliary script itself
    was not found.

## Stale “not landed” markers resolved during the search

- Cross-sector front speed was later repaired and reviewed in PR #5462 (**S**).
- The lattice-Green transverse result is recorded as landed in PR #5107 (**S**).
- The R-eta static reclassification thread is represented by PRs #3841 and
  #3847 and later corrected by PR #6004 (**S**).
- Signed-gravity Round-10b/10c probes were absorbed into the Pfaffian and gap
  lines represented by PRs #3628 and #3636 (**S**).
- The W19 boundary-eta scratch probes were rerun and carried into PR #3824
  (**S**).
- The false W99 epsilon cancellation was corrected by W100 / PR #4419 (**S**).
- Cluster decomposition is present on `main` at commit `62524c0c` (**S**).
- The pkin Class-D diagnosis survives in its PR body even though it was not
  committed as a standalone note (**S**).
- The current uniform half-line gap theorem has its own review surface, PR
  #7835 (**S**).
- The signed-carrier single-seam transport runner and cache are already on
  `main`; the apparent orphan commit is an ancestor of the current history
  (**S**).

## Known missing bytes and recovery limits

The search did not locate the old temporary folders named in memory for
`strike2-scratch`, `c739-scratch`, `c746-scratch`, `RUNG_21`, or the June
emergent-gravity `mom_*` probes. Their detailed memory summaries survive and
are recorded above. Git object/reflog searches found no identifiable orphan
commit carrying those exact artifacts. This means some executable bytes were
lost before this recovery; it does **not** mean their reported science should
be silently discarded.

The recovery cannot prove that no unnamed temporary file was ever deleted. It
does show that the large indexed historical archive survives, identifies the
specific known gaps, and moves the currently extant temporary-only campaigns
onto a remote review path.

## Reconstruction priority

1. Rebuild and independently verify W101's exact cancellation.
2. Turn R1 into a bounded, reproducible Record-dynamics note and runner.
3. Turn R2 into an interaction-stability map with exact finite-volume scopes.
4. Reconstruct the carrier/chirality and anchored-cell identities.
5. Preserve the remaining memory reports as individual classified PRs when
   enough executable evidence is rebuilt.

Audit state and parent-chain state may change the classification of every item
above. They may not be used to erase it or prevent its preservation.
