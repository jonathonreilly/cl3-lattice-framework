# BLIND Supplied-Input Ledger — Emergent-Maxwell Chain (light lane)

**Worker:** BLOCK 01, independent blind read.
**Date:** 2026-09-04.
**Sources read:** `inputs/light_lane_science_records.json` (29 science records, PRs
#7884–#7955) and all eleven `inputs/PR*.md` member notes (#7884, #7886, #7915,
#7917, #7921, #7932, #7945, #7952 ×2, #7959, #7963).
**Framework refresher completed first:** `docs/MINIMAL_AXIOMS_2026-06-29.md`
read complete (all four axioms, the Qualification, Audit-Pipeline Treatment,
Relation To Dynamics, Relation To The Older Observable-Principle Parent, Open
Gates, and the 2026-07-04 / 2026-08-05 / 2026-08-13 revision paragraphs);
`docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` read complete;
`docs/audit/data/axiom_premise_nodes.json` read complete.

## Reading conventions

1. Every member note is **unlanded open-PR content, quoted only**. Nothing below
   presents any member's claim as landed, effective, or carrying any status. No
   status word is applied to any member.
2. Every claim is attributed to its PR **at that PR's own declared scope**. Where
   two members use the same word at different scopes, that is recorded in the
   contradiction/narrowing list rather than smoothed over.
3. **No continuum Maxwell theory is used as a proof input anywhere in this
   ledger.** Where a member says "Maxwell", it is that member's own declared
   comparison target and is quoted as such.
4. A row belongs here if the chain **takes it as given rather than derives it**.
   Things every member disclaims and no member leans on are listed separately in
   §4 so they are not silently absorbed into the supply list.
5. The four axiom sentences used as the derivability yardstick are:
   - **Lattice** — "Physical sites are the points of the cubic lattice `Z^3`,
     with nearest-neighbor adjacency, standard translations, and proper cubic
     rotations about each site." / "No site is privileged."
   - **Qubit** — "Each site has a domain of local possibilities." / "The full
     one-site possibility domain has algebraic presentation `M_2(C)`." / "A
     `Cl(3,0)`-compatible real-algebra presentation may be used equivalently and
     adds no further primitive structure." / "No possibility is privileged."
   - **Admissibility** — "There is one fixed nearest-neighbor admissibility rule,
     covariant under lattice translations and proper cubic rotations." / "For
     each site, the probability distribution over the possibilities is determined
     by, and varies with, the nearest-neighbor conditions."
   - **Record** — "Records form." / "When present, a record locks exactly one
     admissible local possibility. A site never carries more than one record;
     records are permanent." / "Only records are readable. A readout value is
     determined by record content alone. A site with no record cannot be read."
   Plus the memo's own exclusions, which are load-bearing for several estimates
   below: Admissibility "does not choose a Hamiltonian or transfer operator,
   supply transition-probability or weight values, select a scalar or nonzero
   kinetic branch, assert a Dirac-square carrier, define a time metric, or
   provide a record-production process or physical persistence dynamics"; and the
   Open Gates list, which keeps "arrow, record-production dynamics, physical
   persistence dynamics, time metric, and local observability of records" and
   "source/action and physical-observable identification" outside axiom content.
6. Three registry primitives chain-satisfy without bounding downstream rows:
   `scale_reference_primitive`, `kinetic_isotropy_primitive`,
   `realized_state_primitive`. Per `PRIMITIVE_REGISTRY_CHECK` rule 5, none is
   granted more than its source note declares. See R26.

**Rows are presented in rank order, most valuable to the chain first.** "Value to
the chain" is measured by how much of the chain's own headline — two gapless
transverse branches at unit lattice speed on a local carrier — survives if the
row is withdrawn.

---

## 1. The ledger

### R01 — The time rule: that a conservative first-order flow, not a relaxation and not a walk, is the physical law

- **Taken as given.** That the physical evolution of the supplied edge/face data
  is the energy-conserving first-order generator, rather than either of the two
  other time laws compatible with the same static spatial kernel.
- **Leaned on by.** #7915 (states the fork explicitly), #7917 (selects the
  conservative branch by declaring class M1–M6), #7920, #7921, #7922, #7923;
  inherited as the comparison target by #7959.
- **What an axiom derivation would buy.** Everything. #7915 executes the
  discriminator itself: on one and the same harmonic spatial law, a reversible
  gradient sampler has relaxation rate `rho(k)=|s|^2/4` — "this is diffusion, not
  light" — while a two-reflection spectral lift and the direct edge/face
  generator both give linear infrared phase but "differ across the Brillouin
  zone". Withdrawing this row does not weaken the photon claim; it replaces the
  photon with a diffusion mode using unchanged inputs everywhere else.
- **Derivability estimate.** **Genuine supply, and the deepest one.** No axiom
  sentence names a time parameter. The memo places "time metric", "record-
  production dynamics" and "physical persistence dynamics" outside axiom content
  and states that Admissibility "does not choose a Hamiltonian or transfer
  operator". Worse than absence: Record's "A site never carries more than one
  record; records are permanent" is in structural tension with any law that
  rewrites a site value each tick, and #7915 says so at its own scope — its N3
  scan records that "'Unitary' is the exponential of the finite skew generator,
  not a claim that permanent Records update unitarily", and its priority stack
  lists "connect Record formation and experimental sampling to the **unrecorded**
  field evolution". #7917 §8 is equally plain: "The four framework axioms state a
  local conditional probability distribution and permanent Records. They do not
  require conservative continuous-time flow."

### R02 — The declared link/edge/face role carrier and its doubled-incidence compilation

- **Taken as given.** That there is a further degree of freedom per **edge** (and
  in the compiled version, per **face**) beyond the one-site possibility domain:
  a spin-half link role (#7893, #7911, #7959: "one further two-state site per
  edge, assigned by design"), a compact-U(1) integer-flux link role (#7903), a
  face-role site whose nearest-neighbour star is one coarse plaquette (#7906), or
  the role-plus-payload alphabet compiled onto physical `Z^3` sites (#7913,
  #7915).
- **Leaned on by.** #7893, #7903, #7906, #7907, #7911, #7913, #7915, #7917,
  #7920, #7921, #7922–#7924, #7927, #7930, #7932, #7936–#7955, #7959.
  Effectively the whole chain.
- **What an axiom derivation would buy.** The existence of `E`, `B`, the oriented
  curl `C`, both Gauss rows, and every mode count. Without it the downstream
  theorems are stated about objects that stop existing. It would also convert
  R15 (gauge compatibility) from an assumption into a property of a derived
  construction, since gauge redundancy exists only because a link-phase carrier
  was declared.
- **Derivability estimate.** **Genuine supply.** Lattice gives sites and
  nearest-neighbor adjacency; it names no edge or face carrier. #7913 does real
  work here and should be credited at its scope: given the alphabet, it compiles
  the abstract edge/face factor graph onto physical `Z^3` sites with exact
  translation, gauge and proper-cubic covariance — so the **geometry** is earned
  from the supplied alphabet, not assumed separately. The alphabet itself is
  supplied, and #7913's own record says the result "leaves law selection,
  orthogonal or algebraic label realization, Record formation, and dynamics
  open". #7959 states its version without hedging: "The link role is designed,
  not derived."

### R03 — The orientation-complete spatial plaquette term with `kappa_s = kappa_t > 0`

- **Taken as given.** That the same local positive-curvature factor sits on
  **spatial** plaquette orientations as well as temporal ones, and with **equal**
  curvature.
- **Leaned on by.** #7884 (its whole hypothesis: "positive isotropic quadratic
  germ"), #7886, #7887, #7906, #7915, #7936, #7946.
- **What an axiom derivation would buy.** The magnetic restoring directions, and
  therefore the transverse branches. #7886 §5 exhibits the cost of not having it:
  with `kappa_s=0`, "Schur reduction leaves no transverse magnetic restoring
  term. On a purely spatial nonzero momentum, the full matrix has rank one,
  whereas the isotropic `kappa_s=kappa_t>0` completion has rank three before
  removing the gauge null and rank two in the physical spatial quotient."
- **Derivability estimate.** **Genuine supply, and it is two supplies, not one.**
  #7886 §5 says at its own scope: "positive registration derives `kappa_t>0` for
  the stated temporal mechanism; it does not derive `kappa_s>0` or
  `kappa_s=kappa_t`". Positivity of `kappa_s` is the first supply; equality is
  the second, and #7884 §5 shows equality is separately load-bearing — "Unequal
  positive temporal and spatial curvatures preserve the gauge null but change the
  infrared cone by `sqrt(kappa_s/kappa_t)`." Both #7884 and #7886 explicitly
  refuse to source the equality from `kinetic_isotropy_primitive`: #7884 N6
  states the primitive "supplies kinetic graining form, not a gauge-action
  Hessian", and #7886 §5 that it "is not silently extended here into gauge-action
  isotropy". That refusal is correct under `PRIMITIVE_REGISTRY_CHECK` rule 5, and
  it leaves the row a genuine supply.

### R04 — A positive electric stiffness `U > 0` (the electric rotor term)

- **Taken as given** in the germ branch, **bought by R06** in the numerical
  branch, and **shown unavailable** in the minimal pure-gauge law.
- **Leaned on by.** #7906 ("supplying a positive electric rotor term" is a stated
  condition for the two degenerate gapless transverse branches), #7936
  ("Conditional on positive electric and magnetic stiffnesses the kernel carries
  two linearly dispersing polarizations"), #7937, #7941, #7943, #7945; contested
  by #7959.
- **What an axiom derivation would buy.** The difference between a linear and a
  quadratic transverse mode. #7959 names exactly this at its own scope: "A
  linearly dispersing transverse mode needs an electric stiffness `U > 0` in
  front of `E^2` in the coarse-grained energy... At spin `1/2` the electric term
  is the c-number `E_e^2 = 1/4` and supplies none... Confinement is not the
  obstacle at these sizes; what is missing for a Maxwell photon is a stiffness."
- **Derivability estimate.** **Genuine supply in the germ branch.** In the ice
  branch it is measured rather than assumed (#7937 resolves positive first-order
  electric stiffness with `U/|delta V| = 3.183873 +/- 0.154786`; #7941 finds
  volume-stable normalized means `3.252761` and `3.211140`) — but measured on a
  supplied Hamiltonian at a supplied detuning, so the supply has moved into R06,
  not disappeared. No axiom sentence supplies an energy in front of `E^2`; the
  memo keeps "source/action and physical-observable identification" outside axiom
  content.

### R05 — M5: a positive, diagonal, proper-cubic conserved field energy

- **Taken as given.** That there exists `H=(w_E/2)||E||^2+(w_B/2)||B||^2` with
  `w_E,w_B>0`, the same weight on all cubic images of a role, and that the
  generator preserves it for every field.
- **Leaned on by.** #7915 (uses `H` to display conservation), #7917 (M5 is one of
  the four steps of the uniqueness classification), #7921 (its raw-norm variant
  is what the no-go obstructs).
- **What an axiom derivation would buy.** #7917's uniqueness result. Its §5 shows
  M5 alone does two of the four jobs: the diagonal blocks give `2 w_E u = 0`,
  `2 w_B v = 0`, so positivity kills the onsite scalars, and the cross block
  forces `r = -(w_B/w_E)q`, the weighted negative adjoint. Its §8 says M5 is also
  what "excludes the dissipative sampler". Withdraw R05 and the fork of R01
  reopens inside the classification.
- **Derivability estimate.** **Genuine supply — and the axiom history is against
  it, not merely silent.** The 2026-08-13 owner-approved revision "removed the
  named scalar functional `I`, finite additivity over disjoint record
  collections, and `I(empty)=0` from Record", and the memo adds: "Finite
  additivity, a named scalar collection functional `I`, and an assigned value
  `I(empty)=0` are not Record axiom content." A single positive scalar formed by
  summing a local quantity over all role sites of a configuration is exactly that
  removed structure. Note the contrast inside the chain: #7886 §4 routes around
  it deliberately — "No separate finite additivity premise is imported from
  Record", additivity there coming from the logarithm of a product of supplied
  factors — whereas #7917's M5 declares the aggregate scalar directly. This is
  the sharpest derivability finding in the ledger: R05 is not an untried
  derivation, it is a structure a prior axiom revision deleted.

### R06 — The ring-exchange Hamiltonian, its detuning `V`, and `lambda`

- **Taken as given.** `H(V) = -sum_p (|cw><ccw| + h.c.) + V N_f` with `V = 0.95`
  and `0.90` (#7945 and the whole ice stack), and `H = -lambda sum_f P_f` with
  "`lambda` supplied and set to `1`" (#7959, #7911).
- **Leaned on by.** #7936, #7937, #7941, #7943, #7945, #7946, #7952 (both notes),
  #7953, #7955, #7959, #7963.
- **What an axiom derivation would buy.** Every number in the numerical branch,
  including the linear crossover itself: #7945 fits `c_V^2 = gamma |V-1|` with
  `gamma = 0.372286 +/- 0.048788`, so the measured linear term is by construction
  a **response to the supplied detuning** and vanishes with it.
- **Derivability estimate.** **Genuine supply, self-declared.** #7945 §8: "the
  lattice, ice constraint, ring Hamiltonian, couplings, sector starts, and
  observable are supplied model content. Admissibility permits but does not
  select them; Record is not used." The memo agrees from the other side:
  Admissibility "does not choose a Hamiltonian or transfer operator, supply
  transition-probability or weight values". #7959 adds the same for the pure law.

### R07 — The supplied Record overlap law as the physical transfer/action factor

- **Taken as given.** (a) the shifted-convolution form `p(theta|phi) =
  K(theta-phi)` for the neighbour-conditioned distribution; (b) a
  position-classical reading of the transition; (c) that the overlap kernel is a
  physical transfer/action factor; (d) that the factors multiply, so the
  negative-log weights add. #7906's variant supplies an "overlap-success Record
  law" directly.
- **Leaned on by.** #7886, #7887, #7906, #7915 (which takes `kappa` from this
  chain — see contradiction C09).
- **What an axiom derivation would buy.** The **sign** of the local germ, which
  the chain currently earns rather than assumes, and which is worth stating
  precisely because it is the chain's best axiom contact. #7887's record: for
  every nonuniform normalized nonnegative `H^2` density `p` on `U(1)`, the
  overlap kernel is "normalized, nonnegative, even, identity-maximal, and
  representation-positive, with exact negative-log curvature
  `||p'||²/||p||²>0`", which "removes raw Fourier-sign and positive-Lüders
  premises from the local germ calculation".
- **Derivability estimate.** **Genuine supply for (a)–(d), but this is the row
  with a real partial derivation attached, and it is the closest any row comes to
  an axiom sentence.** #7886 §3 establishes, inside the shifted-convolution
  class, that "the conditional family changes for some neighboring conditions iff
  `K` is nonconstant" — so Admissibility's own sentence, "the probability
  distribution over the possibilities is determined by, and varies with, the
  nearest-neighbor conditions", **excludes exactly the constant, zero-curvature
  member**. That is a genuine axiom-sentence consequence. #7886 §3 then bounds it
  honestly: "This equivalence does not derive the shifted-convolution ansatz,
  compact `U(1)` carrier, Lueders instrument, or mode content from the axioms."
  #7886 §4 flags (d) as a premise in its own words: "The factorized transfer
  interpretation is an explicit premise of this step." #7906's record flags the
  cost of not having (c) unconditionally: "marginalizing unread face outcomes
  erases the action, so this is a conditional Record-likelihood photon germ
  rather than unconditional dynamics."

### R08 — The supplied auxiliary face alphabet

- **Taken as given.** A "universal-plus-matching auxiliary face alphabet"
  (#7907), a face-role payload `h` (#7906, #7915), and more generally a "finite
  role-plus-payload alphabet" (#7913).
- **Leaned on by.** #7906, #7907, #7913, #7915 (whose N3 records that "The face
  magnetic payload `B` is additional to the parent's auxiliary `h`").
- **What an axiom derivation would buy.** The step from a **conditioned**
  likelihood to an **unconditional** local gauge measure. #7907's record: the
  alphabet "yields an unconditional link marginal proportional to the product of
  plaquette weights", with "incidence-nearest-neighbor" full conditionals, a
  connected supported single-site graph, and "a unique reversible finite-volume
  measure". That is precisely what repairs #7906's marginalization problem.
- **Derivability estimate.** **Genuine supply, with a constructive discount.**
  #7907's theorem holds "for any strictly positive even weight on a finite cyclic
  gauge group", so once the gauge group and the weight are supplied the alphabet
  is **constructed**, not freely chosen — the residual supply is the group, the
  weight, and the label carrier. What no member supplies is the realization of
  those labels in the axiom's one-site domain; see R18. #7913's own record leaves
  "orthogonal or algebraic label realization" open.

### R09 — M1 and M6: the minimal payload

- **Taken as given.** One real `E` component per edge role and one real `B`
  component per face role; vertex and cube roles carry no dynamical component;
  and no additional coin, duplicated configuration, enlarged unit cell, or
  longer-range field.
- **Leaned on by.** #7917 (M1, M6), #7921 (items 1, 2, 6 of its class), #7915
  (whose payload-compilation priority is the same question).
- **What an axiom derivation would buy.** #7917's §8 is explicit that "M6
  excludes the doubled walk/coin space of the spectral lift" — that is, M6 is
  doing one of the three jobs that select the conservative branch of R01. It also
  buys #7921's no-go, whose class declaration item 6 is the same restriction.
- **Derivability estimate.** **Genuine supply.** Qubit gives "The full one-site
  possibility domain has algebraic presentation `M_2(C)`" — a per-site
  possibility domain, not a real scalar per edge role plus a real scalar per face
  role with two role classes empty. #7921 shows the restriction is load-bearing
  by exhibiting escapes that live outside it: a six-direction internal carrier
  that is "exactly radius-one unitary" and covariant under all 24 proper cubic
  rotations, and an enlarged unit cell. #7917 states M6's status itself: "This is
  a classification assumption, not an axiom claim."

### R10 — M2a: evolution is first order in time

- **Taken as given.** That the law is a first-order flow in `(E,B)` rather than a
  second-order law in `A`.
- **Leaned on by.** #7915, #7917, #7920, #7932.
- **What an axiom derivation would buy.** The physical-neighbour locality of the
  law. #7915 §2 makes the point precisely: the first-order pair is nearest-
  neighbour on the role lattice "even though eliminating `B` produces the
  two-incidence operator `C^T C`". So first-order form is what keeps the law
  radius one; the second-order form is "less directly physical-local after
  eliminating faces" (#7917 N1).
- **Derivability estimate.** **Genuine supply, with a live named alternative.**
  #7917's N1 lists "second-order wave law | Evolve `A` with `ddot A=-C^T C A`.
  Positive continuum form; outside first-order M2." No axiom sentence orders a
  differential equation in a time that the axioms do not supply (see R01, R11).

### R11 — M2b: time is continuous (a generator, not a tick)

- **Taken as given.** That the law is a continuous-time generator with "no
  memory, second time derivative, external clock variable, or finite-step
  inverse" (#7917 M2).
- **Leaned on by.** #7917 (its uniqueness statement is about a generator);
  contested at its own scope by #7920 and #7921.
- **What an axiom derivation would buy.** It would decide the tick question
  instead of deferring it. #7917 §7 states the residual in its own words: "the
  infinitesimal law is unique inside M1-M6, while a strictly radius-one exact
  unitary tick has not been selected or constructed", with the explicit
  Euler/Cayley control — Euler "retains radius one but... is not exactly norm
  preserving", Cayley "is exactly norm preserving, but the inverse spreads a
  one-tick row beyond the physical star" (every Cayley row has more than ten
  nonzero entries on the 162-variable block).
- **Derivability estimate.** **Genuine supply, and the axioms are structurally
  unfriendly to it.** The memo's Open Gates keep "time metric" outside axiom
  content, and Record's permanence and one-record-per-site sentences describe
  locking, not continuous update. #7921's §6 flags the governance hazard in
  exactly this area: the open question "is whether 'one tick is one edge in form'
  permits a finite-depth nearest-neighbour cycle or refers only to the normalized
  regulator form. Silently strengthening it to the obstructed conjunction would
  make a supplier choice look like axiom content."

### R12 — The Yee/leapfrog tick: palindromic schedule, half–full–half coefficients, `h < 1/sqrt(3)`, composed radius three

- **Taken as given.** The three-shear update, its palindromic schedule, its step
  bound, and the fact that what is conserved is a **positive local modified field
  energy** rather than the raw onsite norm.
- **Leaned on by.** #7920, #7921 (as the named positive sibling and the strongest
  counterexample to any broader negative wording), #7922, #7923.
- **What an axiom derivation would buy.** The finite realization of R01. #7920's
  record states its own conditionality precisely: "Within the declared
  palindromic schedule, first-order Maxwell consistency uniquely selects the
  half-full-half coefficients; the composed radius is three and raw onsite qubit
  unitarity is not claimed." So the coefficients are earned **inside** a supplied
  schedule; the schedule and the radius-three composition are the supply.
- **Derivability estimate.** **Genuine supply.** Same axiom situation as R01/R11.
  Note the internal cost accounting made by #7921: the conjunction "minimal E/B
  payload + complete-map physical radius one + gauge-compatible curl response +
  raw onsite unitarity cannot carry light", so at least one of R09, R12's radius,
  or the raw-norm reading must be relaxed — #7920 relaxes the last two.

### R13 — M2c: the law's support is self plus physical nearest neighbours

- **Taken as given.** That a site derivative may use its own component and the
  dynamical components among its six physical nearest neighbours, and no farther
  site.
- **Leaned on by.** #7915, #7917 (M2), #7921 (item 3).
- **What an axiom derivation would buy.** The strongest available structural link
  between the axioms and the classified generator: it would turn M2's support
  clause from an assumption into a consequence of the one fixed nearest-neighbor
  rule.
- **Derivability estimate.** **Partially derivable in form; genuine supply in
  application, with a carrier caveat that is easy to miss.** Admissibility's
  "There is one fixed nearest-neighbor admissibility rule" and the distribution
  sentence do give nearest-neighbour dependence — but of a **probability
  distribution over site possibilities**, not of a time derivative; and the memo
  blocks the transfer directly ("does not choose a Hamiltonian or transfer
  operator"). The caveat: the locality in #7915/#7917 is nearest-neighbour on the
  **doubled** role lattice (side six at coarse `L=3`), not on the `Z^3` of the
  Lattice axiom. That adjacency is itself supplied via R02, so R13 is not
  independently cheap: it inherits R02's cost. #7917 N1 also names the live
  alternative — "longer-range stencil | Read beyond the physical star.
  Gauge-invariant improved curls may exist."

### R14 — M3: proper-cubic covariance of the law

- **Taken as given.** That the same law is used at every site, that proper cubic
  rotations carry edge orientation into edge orientation and face normal into
  face normal, and that no orientation has an independent coefficient.
- **Leaned on by.** #7884, #7907, #7913, #7915, #7917 (M3), #7921, #7952
  (kernel-uniqueness note).
- **What an axiom derivation would buy.** #7917 §3: covariance is what collapses
  the three orientation scalars `(q_xy,q_xz,q_yz)` to one `q`, since the 24
  proper cubic rotations act transitively on the six oriented face normals. In
  the kernel note (#7952) it is one of the two conditions whose intersection
  leaves a one-dimensional space: "proper cubic covariance only: dimension 3,
  gauge transversality only: dimension 6, both conditions together: dimension 1."
- **Derivability estimate.** **The highest-derivability row in the ledger, and
  close to verbatim axiom content — but conditional on R02.** Lattice names
  "proper cubic rotations about each site" and Admissibility says the fixed rule
  is "covariant under lattice translations and proper cubic rotations". What
  remains supplied is (i) that the dynamical generator is, or inherits from, that
  fixed rule, and (ii) that the **role labels** transform as declared (#7915 §6
  relies on edge and face role labels transforming "with the same orientation
  rules in the direct parent"). The kernel note (#7952) §5 draws the same line at
  its own scope: "The Lattice axiom supplies proper cubic rotations of the
  underlying lattice. It does not by itself supply a gauge field, a symmetric
  analytic kernel, a gapless phase, or the identification of lattice momentum
  with a physical long-wavelength excitation."

### R15 — M4: gauge compatibility (`L d_0 = 0`, `d_2 L = 0`)

- **Taken as given.** That the magnetic response to an edge potential is
  unchanged by an exact gradient and has zero cube divergence.
- **Leaned on by.** #7915, #7917 (M4), #7921, #7952 (kernel note, as
  transversality `K(q) q = 0`).
- **What an axiom derivation would buy.** #7917 §2 shows M4 does the single
  largest reduction of the four steps: a general one-face response has four
  independent coefficients, and requiring the coefficient of every gauge value to
  vanish leaves a rank-three constraint matrix with one-dimensional nullspace
  `q(1,1,-1,-1)` — "the oriented curl", with "neither a continuum limit nor a
  Fourier argument" needed. #7917's own steelman rests on this: "Gauge invariance
  does real work."
- **Derivability estimate.** **Genuine supply, but with low *independent* cost
  once R02 and R08 are granted.** No axiom sentence contains a gauge symmetry;
  the redundancy exists because a link-phase carrier was declared. Conditional on
  that carrier, #7907 and #7913 obtain gauge covariance as a property of the
  compiled construction rather than as an added assumption, and the kernel note
  (#7952) §5 says so directly: "In this application gauge transversality comes
  from the supplied ice constraint and carrier construction." In #7917 it is
  re-declared as a class member. Book it as inherited from R02/R08, not as a
  fresh charge.

### R16 — M2d: linearity / the weak-field restriction

- **Taken as given.** That the evolution is linear in the fields, and (in the
  action branch) that the configuration stays in the smooth neighbourhood where
  the quadratic germ dominates.
- **Leaned on by.** #7884 (smooth principal branch), #7915, #7917 (M2), #7932
  (its "controlled tame" window).
- **What an axiom derivation would buy.** Little on its own, which is why it
  ranks here: the chain already knows the microscopic law may be nonlinear.
  #7884's whole content is that distinct nonlinear one-plaquette potentials with
  a common `kappa` "have the same normalized quadratic limit even when their
  exact finite-angle actions and equations differ". So linearity is a statement
  about a limit, not about the law.
- **Derivability estimate.** **Genuine supply.** No axiom sentence restricts a
  law to be linear in a field the axioms do not name. Both #7884 and #7917 list
  the nonlinear/compact-interacting sector as outside scope rather than excluded.

### R17 — M2e: the field components are real

- **Taken as given.** One **real** component per role in #7917's class; one
  **complex** scalar per role in #7921's class.
- **Leaned on by.** #7917 (M1/M2), #7921 (item 1).
- **What an axiom derivation would buy.** It decides whether an onsite phase is
  available, which is exactly the hinge between #7917's uniqueness and #7921's
  no-go. #7917 §5 kills the onsite scalars by positivity (`u=v=0`); #7921 §3 finds
  the surviving `u,v` "may be arbitrary complex phases" and notes that requiring
  the map to be real reduces them to signs. #7917 N1 lists "complex onsite phase |
  Allow complex one-component fields. A conservative onsite phase becomes
  possible; outside M1."
- **Derivability estimate.** **Genuine supply.** Qubit gives `M_2(C)` and says a
  "`Cl(3,0)`-compatible real-algebra presentation may be used equivalently and
  adds no further primitive structure" — i.e. the real presentation is available
  but carries no privilege, and "No possibility is privileged." Choosing reality
  for the payload is therefore a supplier choice, and the two members choose
  differently.

### R18 — The payload-to-`M_2(C)` site realization

- **Taken as given.** That the declared payloads — a finite role-plus-payload
  alphabet (#7913), enlarged `(A,E)` edge and `(B,h)` face payloads (#7915), one
  complex scalar per edge and face (#7921), `q` qubits per link for `K=2^q`
  (#7932) — can live at or near physical sites whose axiom-given possibility
  domain is `M_2(C)`.
- **Leaned on by.** #7913, #7915, #7920, #7921, #7932.
- **What an axiom derivation would buy.** The one thing that would make the whole
  carrier axiom-native rather than declared. Every member names it as open:
  #7913's record leaves "orthogonal or algebraic label realization" open; #7915's
  priority 2 is to "compile the enlarged `(A,E)` edge and `(B,h)` face payloads
  into the chosen one-site or spatial-composite possibility implementation";
  #7932 §6 says "The exact `q`-qubit register also still needs compilation into
  the framework's homogeneous physical nearest-neighbor law... this note counts
  the qubits but does not build the local incrementer scaffold."
- **Derivability estimate.** **Genuine supply.** Qubit fixes the one-site domain;
  no member exhibits an embedding of its payload into it. #7932 leans on a
  separately-declared reading — "The user-approved scale reading allows a
  collective link to occupy many smallest sites" — which is a supplied reading,
  not an axiom sentence, and I record it as such because the ledger should not
  absorb it silently.

### R19 — The fixed Gauss/ice sector, flux sector, and zero-winding component start

- **Taken as given.** Work inside "one fixed three-of-six Gauss sector and
  electric-flux sector" (#7945 §1); zero-flux component starts; Gauss as "a
  support condition" among corner records (#7893); the ladder's declared
  staggered background (#7911, #7959).
- **Leaned on by.** #7893, #7903, #7911, #7936, #7937, #7941, #7943, #7945,
  #7952 (both), #7953, #7955, #7959, #7963.
- **What an axiom derivation would buy.** It would remove the component-scope
  caveat that every numerical member carries. #7945 §1: "The calculation remains
  component-scoped. It neither crosses nor classifies all square-move
  components."
- **Derivability estimate.** **Genuine supply, and the registry has a specific
  rule about it.** `realized_state_primitive` supplies a pointwise evaluation
  slot and nothing else: "no state, state-selection rule, averaging over
  alternatives, measure, weighting, probability rule, typicality claim,
  genericity claim, preferred state, default state, boundary condition,
  normalization rule, or value is supplied by it", and "A value that would change
  under a different law-admissible realized state is registered data, not
  derivation output." Numbers measured on one supplied sector/component start are
  therefore registered data under the primitive's own counterfactual test. One
  genuine narrowing of the caveat comes from inside the chain: #7959's `4x2x2`
  census finds the zero-winding class is "**ONE** flip-connected component of
  `1,551,976` states plus `48` frozen states and nothing else", which it reads as
  making the `2x2x2` fragmentation "a smallest-box artefact".

### R20 — The electric-field readout dictionary and the choice of transverse observable

- **Taken as given.** `E_i(x)=(-1)^(x_1+x_2+x_3)[n_i(x)-1/2]` and the six ordered
  axis/polarization modes whose cubic-orbit average is the measured correlator
  (#7945 §2); and in #7959, `E_e = Z^L_e/2` with the reading that "the flux
  registers — it is record content, readable by the Record axiom".
- **Leaned on by.** #7945, #7952 (late-time), #7953, #7955, #7959, #7963.
- **What an axiom derivation would buy.** The identification of a functional of
  records as *the electric field* — without which every measured `omega`, `S_T`
  and `U` is a number about an unnamed observable.
- **Derivability estimate.** **Genuine supply.** Record gives "Only records are
  readable. A readout value is determined by record content alone" — that a
  readout exists and depends only on record content, not **which** functional is
  physical. The memo's Open Gates keep "physical-observable identification"
  outside axiom content. #7959 is the most careful member here: it uses the
  axioms only "to fix what 'readable' means and to say why the carrier is a link
  qubit, and for nothing else", and notes that `U_e` and `P_f` "have no
  record-diagonal part, and register only through correlations among records" —
  i.e. the magnetic side of the dictionary is not a single-record readout at all.

### R21 — The four-dimensional refinement carrier, the smooth principal branch, and the zero-monopole sector

- **Taken as given.** A "finite periodic four-dimensional hypercubic carrier"
  (#7884), a fixed physical four-volume with `a -> 0`, link phases defined by
  exact edge integrals of a `C^4` one-form, the principal-branch condition
  `a^2 ||F||_infinity < pi`, and the smooth `m=0` monopole sector.
- **Leaned on by.** #7884, #7886.
- **What an axiom derivation would buy.** The only place in the chain where the
  smooth source-free continuum statement lives. Withdraw it and #7884's
  conclusions 1–3 have no carrier.
- **Derivability estimate.** **Genuine supply, on two counts.** Lattice supplies
  `Z^3`, not `Z^4`; the fourth direction is exactly the time the axioms do not
  provide (R01/R11), and #7886 §5 is careful that spatial cubic symmetries "do
  not exchange space with Record time". The refinement family (a continuum limit
  at fixed physical volume) and the zero-monopole restriction are separate
  supplied conditions; #7884 fences the latter itself — "the theorem requires and
  verifies the smooth zero-monopole branch, while other sectors remain outside
  scope."

### R22 — The reciprocal coefficient normalization `beta = kappa`, `alpha = 1/kappa`

- **Taken as given.** That the electric and magnetic normalizations are
  reciprocal, giving lattice speed one.
- **Leaned on by.** #7915 §5, #7917 §6, #7932 §4 (where "Reciprocal electric and
  magnetic coefficients cancel `g` from the frequency"), #7884 (where the same
  overall constant plays a different role — see C10).
- **What an axiom derivation would buy.** One number. Modest: #7884 notes that
  "An overall positive `kappa` multiplies the source-free equation and therefore
  cancels after division", so the speed normalization matters only once sources,
  coupling normalization or quantum weights enter.
- **Derivability estimate.** **Genuine supply, explicitly flagged as such by the
  member that uses it.** #7915 §5: "This is the standard transfer/Hamiltonian
  relation, but it is **declared here rather than attributed to the static
  probability law**." `kinetic_isotropy_primitive` may normalize the remaining
  ratio to one *after* a class is selected — #7917 §6 and #7915 §5 both say so —
  but per registry rule 5 it supplies only "the kinetic form ratio, not an
  absolute scale, spacing-ratio theorem, dynamics, or downstream Lorentz
  theorem", so it cannot select the class it normalizes.

### R23 — Supplied vertex charge, edge current, and matter representation

- **Taken as given.** "supplied vertex charge and edge current" (#7922), the
  charged-bond unitary and its matchings (#7924), the two-state matter factor and
  charge representation (#7932, #7927, #7930), and the static ring charges of
  #7903.
- **Leaned on by.** #7922, #7923, #7924, #7927, #7930, #7932; #7893 and #7903 on
  the Gauss/charge-convention side.
- **What an axiom derivation would buy.** The sourced sector and the join to the
  framework's own matter carrier. #7922's record names the residual: "the
  matter-current derivation, compact joint unitary, coupling normalization, and
  Record readout remain open."
- **Derivability estimate.** **Genuine supply.** No axiom sentence supplies a
  charge, a current, or a matter representation; the memo's Open Gates keep
  "source/action and physical-observable identification" outside axiom content.

### R24 — Finite clock order `K`, couplings `g`, and the no-wrap window

- **Taken as given.** The `K`-state Weyl clock per link, `g`, the electric and
  Wilson coefficients, and the restriction to a window where "the possible
  divergence is strictly smaller than one modular wrap".
- **Leaned on by.** #7932.
- **What an axiom derivation would buy.** A finite-payload existence result would
  become a derived one. As stated it is a controlled restriction: #7932 §5 warns
  that "A Taylor tangent can be formally correct while the finite carrier's
  relevant states sit at a clock branch edge", and its exhaustive `K=32`,
  `|m|<=2` check is what fences the additive reading.
- **Derivability estimate.** **Genuine supply, self-declared.** #7932 §6: "The
  clock order, link role, Hamiltonian, couplings, tame restriction, matter
  representation, and register layout are supplied. Admissibility selection and
  permanent Record realization are untouched."

### R25 — Declared estimator/analysis choices and the imported static target `U K`

- **Taken as given.** Fitted-time windows, forward length `F`, walker counts,
  constant trial vector, seeds, warmup/burn schedules; and the cross-imported
  static target `U K = 0.01228909 +/- 0.00116899` (#7963, #7952 late-time),
  parsed from independent charge/flux and magnetic-twist receipts rather than
  fitted.
- **Leaned on by.** #7945, #7952 (late-time), #7953, #7955, #7963.
- **What an axiom derivation would buy.** Nothing physical — but the row belongs
  in the ledger because it is load-bearing for every quoted number and because
  one of its floors is currently failing. #7963 reports its infrared ladder at
  "`TOTAL: PASS=2 FAIL=1`", the sole failure being "the minimum number of
  distinct origins surviving to `tau=16` is `18`, below the declared floor of
  `40`", and a second receipt at "`PASS=10 FAIL=1`" whose failed physics control
  is an early-window RK coefficient at `-3.849` reported errors from zero.
- **Derivability estimate.** **Genuine supply, of method rather than physics.**
  Under `realized_state_primitive`'s counterfactual test these are registered
  data, not derivation output. Worth ranking above zero precisely because #7963
  shows the choices can and do fail their own declared thresholds.

### R26 — Registered, not supplied: `kinetic_isotropy_primitive` and the "one edge in form" reading

- **Status.** This row is **not** a supply. `kinetic_isotropy_primitive` is a
  registered premise in `docs/audit/data/axiom_premise_nodes.json` and
  chain-satisfies without bounding downstream rows. It is listed so the ledger is
  explicit about what the chain may and may not draw from it.
- **Leaned on by.** #7884, #7886, #7915, #7917, #7921, #7920.
- **What it does and does not grant.** Its source note declares `c_t = c_s` (OS0
  kinetic-form normalization) and states that it "does not supply any
  dimensionless dynamical quantity" and "does not re-axiomatize time". Per
  `PRIMITIVE_REGISTRY_CHECK` rule 5, nothing more may be granted.
- **Chain hygiene.** The members police this correctly at their own scopes:
  #7884 N6 ("supplies kinetic graining form, not a gauge-action Hessian"), #7886
  §5 ("not silently extended here into gauge-action isotropy"), #7915 §5 ("cannot
  turn the candidate into an axiom consequence"), #7917 §6 ("It does not select
  M1-M6 and supplies no dynamics on its own"), #7921 §6 ("not a dynamics or
  support-radius definition"). **The named hazard is real and worth carrying
  forward:** #7921's §6 says that reading "one tick is one edge in form" as the
  complete-map radius-one onsite-unitary class "would make a supplier choice look
  like axiom content". That reading would silently convert R12/R13 from supplies
  into axiom consequences; no member does it, and none should.

---

## 2. Derivability summary

| Row | Supply | Nearest axiom sentence | Estimate |
|---|---|---|---|
| R01 | physical time rule | none; memo excludes time metric & persistence dynamics | genuine supply (deepest) |
| R02 | link/edge/face role carrier | Lattice adjacency (sites only, no edge carrier) | genuine supply |
| R03 | spatial magnetic term, `kappa_s=kappa_t>0` | none | genuine supply ×2 (positivity, equality) |
| R04 | electric stiffness `U>0` | none | genuine supply (germ branch); via R06 (ice branch) |
| R05 | positive conserved energy | Record's removed `I`/additivity (2026-08-13) | genuine supply; **structure previously removed** |
| R06 | ring Hamiltonian + detuning `V`, `lambda` | Admissibility "does not choose a Hamiltonian" | genuine supply |
| R07 | Record overlap as transfer factor | Admissibility variation sentence (partial win) | genuine supply for ansatz; **best axiom contact in the chain** |
| R08 | auxiliary face alphabet | Qubit one-site domain (no auxiliary labels) | genuine supply, constructive discount |
| R09 | minimal payload M1/M6 | Qubit `M_2(C)` per site | genuine supply |
| R10 | first-order form | none | genuine supply |
| R11 | continuous time | Record permanence is in tension with it | genuine supply |
| R12 | leapfrog schedule & radius three | none | genuine supply |
| R13 | nearest-neighbour support | Admissibility "one fixed nearest-neighbor rule" | partly derivable in form; supplied in application; inherits R02 |
| R14 | proper-cubic covariance | Lattice + Admissibility covariance clauses | **highest derivability**, conditional on R02 |
| R15 | gauge compatibility | none directly | genuine supply, inherited from R02/R08 |
| R16 | linearity / weak field | none | genuine supply (limit statement) |
| R17 | real field components | Qubit: real presentation available, not privileged | genuine supply |
| R18 | payload → `M_2(C)` realization | Qubit one-site domain | genuine supply, named open by every member |
| R19 | Gauss/ice sector, component start | `realized_state_primitive` (slot only) | genuine supply; numbers are registered data |
| R20 | electric readout dictionary | Record readout sentence (existence only) | genuine supply |
| R21 | 4D carrier, smooth branch, zero monopole | Lattice supplies `Z^3` only | genuine supply ×2 |
| R22 | reciprocal normalization `c=1` | `kinetic_isotropy_primitive` (after class selection) | genuine supply, declared as such by #7915 |
| R23 | charge, current, matter representation | none | genuine supply |
| R24 | clock `K`, `g`, no-wrap window | none | genuine supply, self-declared |
| R25 | estimator windows, `F`, seeds, imported `U K` | `realized_state_primitive` counterfactual test | genuine supply of method |
| R26 | *(not a supply — registered primitive)* | its own source note | registered; grant no more |

---

## 3. Where members narrow or contradict each other at scope

**C01 — Pure spin-half quadratic mode (#7959) vs finite-detuning linear terms
(#7945).** #7959, on `H = -lambda sum_f P_f` with `lambda = 1` and no detuning,
quotes `omega` about `0.78 k^2` with `omega/k^2 = 0.73, 0.75, 0.80, 0.77` for
`L = 6`–`12` and `S_T(k_min)` flat at `0.30`–`0.38`, and states at its own scope
that this is "a quadratic Lifshitz / Rokhsar-Kivelson-type soft mode rather than
the sister lane's Maxwell photon at these momenta". #7945, on the same spin-half
cubic-ice carrier **with** `V N_f` at `V=0.95` and `0.90`, resolves a positive
`c_V^2` at `5.1` and `6.0` reported errors. These are not formally inconsistent —
#7945's own RK control at `V=1` reproduces the quadratic ladder
(`c_RK^2 = 0.000138 +/- 0.000674`, `a_RK^2 = 0.092002 +/- 0.002658`), matching
#7959's `z=2` reading — but they narrow each other hard, and one sentence is a
direct clash: **#7959 states "A Rokhsar-Kivelson potential term moves the
coupling toward `z = 2`, not away from it", while `V N_f` at `V < 1` is precisely
such a term and is exactly what #7945 reports moves the branch toward linear.**
This is the single most important cross-member tension in the pack and should not
be resolved by preferring either member; both are finite-volume at `L <= 14`.

**C02 — Where the electric stiffness comes from.** #7959's reading names the
missing ingredient as `U > 0`, unavailable at spin `1/2` because "the electric
term is the c-number `E_e^2 = 1/4`", and names two uncomputed candidates (the
#7893 matter hop, or a larger link representation). #7937/#7941/#7943 measure
positive `U` on the same carrier at finite detuning. So the two branches disagree
about whether `U` is a *representation* question (#7959) or a *coupling* question
(#7937 et al.). Both readings are at finite volume; neither is executed against
the other.

**C03 — The magnetic normalization used in the static–dynamic triangle.** #7945
§6 compares `K_dyn(V) = c_V^2/U(V)` against "`K_RK` approximately `0.2598`", the
RK magnetic-flux response, and reports `K_dyn` about `0.167` at `V=0.95` and
about `0.102` at `V=0.90`. #7946 then measures a **relaxed** magnetic-twist
stiffness `K = 0.075561 +/- 0.000915` at `V=0.95` and `0.076589 +/- 0.001155` at
`V=0.90`, and its record explicitly "distinguishes the relaxed curvature from the
older `0.2598` variational upper cost". The later stack (#7952 late-time, #7955,
#7963) uses `U K = 0.01228909 +/- 0.00116899`. **#7945's quantitative triangle is
therefore computed against a magnetic number its own lane subsequently replaced.**
Any downstream reading of #7945 §6 must carry that.

**C04 — The `c^2 = U K` comparison changes verdict four times across members, all
at finite volume.** #7945: `K_dyn` "within `36%`" at `V=0.95`, "roughly `61%`
below" at `V=0.90`, no closure claimed. #7952 (late-time), `L=8,10,12,14`: the
two-term fit fixed to `U K` costs `Delta chi^2 = 18.42`, but with a `q^6` term
the fixed-`U K` fit is acceptable in all four windows — "removes evidence of a
static-dynamic inconsistency" while explicitly **not** establishing the equality.
#7955, off-axis: the full `q^2`–`q^6` fit "disagrees with the static `U K` target
by `6.563` reported errors", localized by leave-one-volume analysis "uniquely to
the highest-momentum `L=8` block". #7963, adding `L=16,18`: target distances
`1.373` and `1.171` combined errors, compatible — but with two failing receipts
(see C05). The chain's own summary of this sequence should be that the mismatch
tracks the momentum range and the model order, not that it has been settled.

**C05 — #7963's two live failures against #7945's null control.** #7945's RK
ladder is presented as the campaign's null control with an unresolved infrared
intercept. #7963, in the same early window `2--6`, finds a **resolved** RK
direct-spectrum coefficient `-0.00192094 +/- 0.00049902`, i.e. `-3.849` errors
from zero, surviving five of six leave-one-volume removals, and fixing it to zero
costs `delta chi^2 = 14.8180`. #7963 classifies this as "an early-time estimator
boundary with some `L=18` leverage", and separately reports a genealogy floor
failure (`18` distinct `tau=16` origins against a declared floor of `40`). The
null control is therefore not uniformly clean at the earliest window that other
members use as primary.

**C06 — #7917's uniqueness vs #7921's no-go, on nominally the same minimal
class.** #7917 concludes that inside M1–M6 "every nonzero generator is equivalent
by positive field rescaling to" the oriented curl pair, unique up to one speed.
#7921, on one complex scalar per edge and face with a **complete radius-one tick**
and **raw onsite norm**, concludes that "Unitarity forces both curl coefficients
to zero, leaving momentum-independent onsite phases". The two survive together
only because their classes differ on three declared points: real vs complex
(R17), continuous generator vs one-tick map (R11), and conserved positive local
metric vs raw coordinate norm. The narrowing is that **#7917's uniqueness is a
statement about a continuous-time real generator and does not transfer to a
finite tick**; #7917 §7 says exactly this.

**C07 — What "one tick is one edge in form" may mean (#7921 vs #7920 vs the
primitive).** #7920's tick has composed radius three and does not claim raw
onsite qubit unitarity; #7921 proves the radius-one raw-onsite-unitary reading is
transport-trivial. Both cannot be the primitive's meaning. #7921 §6 states the
governance question rather than resolving it, and warns against strengthening the
primitive into the obstructed conjunction. Recorded here as an open reading
question, not a contradiction between the members.

**C08 — #7887 narrows #7886's premise list.** #7886 obtains representation
positivity from a supplied positive central Lüders registration channel and a
position-classical transition reading. #7887's record states that its
distribution-overlap kernel "removes raw Fourier-sign and positive-Lüders
premises from the local germ calculation". This is a strict narrowing in #7887's
favour: any ledger of the germ branch should charge #7887's shorter premise list,
not #7886's, while noting that #7887 still leaves "using the overlap as a
physical transfer/action factor, completing it on spatial plaquettes, and
identifying the field" supplied or open.

**C09 — #7915 calls `kappa` the "Record-overlap magnetic curvature"; #7886 and
#7887 at their own scopes say the overlap chain supplies no magnetic block.**
#7915's result statement uses "`kappa>0` is the Record-overlap magnetic
curvature" and its §5 says "The Record-overlap chain supplies `kappa>0` for the
magnetic germ." #7886 §5 says the opposite at its own scope: positive
registration "does not derive `kappa_s>0` or `kappa_s=kappa_t`", and its
temporal-only control "has rank one at spatial momentum and lacks two magnetic
restoring directions". #7887's record likewise leaves "completing it on spatial
plaquettes" supplied or open. **This is a genuine scope contradiction between
members and the one place where a supplied input (R03) risks being read as
derived.** It should be corrected in any joint surface: the overlap chain
supplies a temporal/electric curvature; the spatial magnetic completion is
supplied.

**C10 — The same `kappa` plays two roles.** #7884: "An overall positive `kappa`
multiplies the source-free equation and therefore cancels after division." #7915
§5 and #7917 §6: `beta=kappa`, `alpha=1/kappa` fixes the speed to one. Not a
contradiction — the two statements concern the source-free equation and the
Hamiltonian normalization respectively — but a joint surface that quotes both
must not present the second as a use of a quantity the first has just cancelled.

**C11 — #7952's kernel-uniqueness premise is what #7959 reports is not
satisfied.** The kernel note (#7952) fixes `K_ij(q)=q^2 delta_ij - q_i q_j`
uniquely from proper cubic covariance plus gauge transversality, but declares its
premises: "It assumes a quadratic Taylor term exists. It does not prove
analyticity, exclude a mass or a nonanalytic direction-dependent term, or show
that the microscopic carrier actually has a thermodynamic pole." #7959 reports,
for the pure `lambda`-only law, a flat `S_T(k)` and a quadratic mode — the case
where the assumed analytic gapless transverse regime is not reached at the
momenta measured. The kernel theorem is exact; its **application** to the
spin-half carrier is precisely what #7959's branch leaves unsettled, and the
kernel note's own falsifier list says so.

**C12 — #7959 vs #7942 on sector bookkeeping and the required update.** #7959
states two disagreements: that the parity obstruction "is a property of **closed**
operator strings", so an open-path projector "needs no parity-changing update at
all" and the loop/cluster update named by #7942 "is one way among others"; and
that "the `937` components are a smallest-box artefact", since at `4x2x2` a
winding class is one flip component plus isolated frozen states. #7942 is
referenced by #7959 but is **not** among the 29 supplied science records, so this
disagreement is recorded from one side only.

**C13 — #7893 vs #7903 on the Gauss charge convention.** #7893 finds "a
coordination-parity obstruction between sea and staggered charge conventions";
#7903 reports that "parity makes the neutral-sea Gauss convention empty and
selects the staggered background convention". #7903 narrows #7893 by selecting
one of the two conventions rather than by removing the obstruction.

**C14 — #7906 vs #7907 on conditioning.** #7906's record: "marginalizing unread
face outcomes erases the action, so this is a conditional Record-likelihood
photon germ rather than unconditional dynamics." #7907 obtains an unconditional
link marginal — but by supplying a larger object, the "universal-plus-matching
auxiliary face alphabet". The narrowing is real and its price is R08: the
unconditional result is bought with an enlarged supplied alphabet, not with a
weaker premise.

**C15 — Payload size is load-bearing across the finite-carrier members.** #7932
needs `K = 128, 256, 512, 1024` for its reduced-mode gaps to approach the target
(final relative errors `0.159%, 0.166%, 0.256%` at `K=1024`), i.e. `q` qubits per
link with `q` large; #7959's spin-half link (the smallest payload) has `E_e^2 =
I/4` as a c-number and no stiffness. The two are not in conflict, but together
they narrow the chain's payload claim: the Maxwell tangent in the finite-clock
branch is a **large-`K`** statement, and no member exhibits it at the minimal
payload.

**C16 — #7953, #7955 and #7952 (late-time) mutually narrow the explanation
space.** #7952 (late-time) removes fitted-time drift ("the early and primary late
values differ by only `1.03` combined errors"). #7953 removes inadequate forward
projection for `L=8` ("a stable `F=12,14,16,20` transverse-gap plateau at fixed
`L=8`"), while its record notes this does not extend "to lower momenta". #7955
localizes the residual mismatch "uniquely to the highest-momentum `L=8` block".
Together these three narrow to a single live explanation — momentum range and
gradient order — which #7963 then tests. Consistent, but each member's own scope
limit must travel with it.

---

## 4. Declared non-inputs (things no member leans on, listed so they are not absorbed)

- **The electromagnetic identification.** No member uses "this `U(1)` is
  electromagnetism" as a premise, and each disclaims it: #7884 ("does not
  establish... a physical electromagnetic dictionary"), #7945 ("does not identify
  this emergent gauge boson as the empirical electromagnetic photon"), #7959 ("no
  claim is made that this `U(1)` is electromagnetism"), #7932 (`W4`), #7952
  (kernel note §5). It is an obligation, not a supply.
- **Continuum Maxwell theory as a proof input.** No member imports it; #7884 and
  #7886 derive their limits from Taylor bounds on a supplied germ, #7915/#7917
  from exact integer incidence and finite linear algebra, #7952 (kernel) from an
  exact `36`-coefficient nullspace, and #7959 from exact finite censuses. #7915
  §8 and #7932 §7 name external constructions explicitly as "literature context,
  not proof authority" and "prior-art boundary".
- **Record time = Hamiltonian time.** Explicitly not asserted: #7952 (kernel) §5
  "does not equate the emergent Hamiltonian time with Record time"; #7886 §5
  "They do not exchange space with Record time"; #7915 N3 "not a claim that
  permanent Records update unitarily".
- **Any axiom edit.** Every member states that none is made or proposed. #7917 §8
  frames the choice cleanly and is worth carrying forward verbatim as the shape
  of the open decision: either "treat M1-M6 as defining the candidate physical
  law and continue testing", or "seek a derivation of M1-M6 from a smaller
  principle, and if no existing premise can provide it, decide whether a
  conservative local-dynamics principle belongs in the approved primitive/axiom
  boundary."
