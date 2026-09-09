# Signed Record refinement and conditional source algebra: original #6266

Type: bounded_theorem

Status: corrected conditional mathematics, awaiting independent landing review.
This note carries no audit grade and makes no physical TOE claim.

**Primary runner:** `scripts/law_tournament_6266_finite_2026_09_09.py`

**Independent checker:** `scripts/law_tournament_6266_6275_independent_check_2026_09_09.py`

The shared implementation is `scripts/law_tournament_6266_6275_model.py`.
The new runner leaves the existing historical #6266 runner and the seven
current helper relocations unchanged. Exact original sources, intermediate
versions and original inputs are recovered in
[correction history](../.claude/science/physics-loops/law-tournament-6266-6275-correction-20260909/HISTORY.md).

## Supplied finite definitions

The carrier is a complex 2 by 2 matrix, represented by Gaussian rationals.
With the Pauli matrices, write a Hermitian matrix as `a I + v·sigma`.
For a supplied proper signed cubic rotation R, transport sends v to Rv;
its corresponding action on complex matrices transports both Hermitian and
anti-Hermitian parts. The frame vector (1,2,3) has a free 24-element orbit.
The current Block63 matrix/carrier functions and Block64 local functions are
used as these explicit mathematical definitions. Their historical main
routines, physical derivations and text validators are not executed.

Let P0=diag(1,0), P1=diag(0,1). The two menus are

```
menu0 = (diag(1/2,0), diag(1/2,1/5), diag(0,4/5))
menu1 = (diag(1/2,0), [[1/4,1/4],[1/4,1/2]],
                       [[1/4,-1/4],[-1/4,1/2]])
```

Each menu consists of positive semidefinite effects summing to I. For outcome
h the supplied successor density is tau_h=E_h/tr(E_h). These matrices do not
establish why a physical system must select this particular menu or density.
The companion [exact density/channel note](RECORD_LAW_EXACT_DOMAIN_AND_CHANNEL_BRIDGE_6275_BOUNDED_THEOREM_NOTE_2026-09-09.md)
specifies the common four-dimensional input domain and the tensor-order bridge.

## Sharp refinement and the registration condition

A POVM E_h has a joint refinement with a sharp PVM P_s if and only if each
E_h commutes with every P_s. In a joint refinement G_hs, positivity and
`sum_h G_hs=P_s` give `0 <= G_hs <= P_s`. For v in ker(P_s),
`<v,G_hs v>=0`; positivity implies `G_hs v=0`, so
`G_hs=P_s G_hs P_s`. Summing over s gives block-diagonal E_h and commutation.
Conversely, when they commute, G_hs=P_s E_h is positive and has both required
marginals. This proof covers the exact matrices rather than a numeric test
for approximate commutation.

Menu0 admits the refinement. Its four nonzero pairs, ordered as (h,s), are
`(0,-1),(1,-1),(1,+1),(2,+1)`, with s=2m-1. Menu1 has noncommuting pairs
and fails this particular sharp refinement. Unsharp currents, other menus
and replacement instruments remain outside this fixed comparison. Proper
rotation preserves the criterion and every marginal; the primary checks
24 frames, 96 nonzero menu0 effects and 96 noncommuting menu1 pairs.

For a supplied hazard f in [0,1], an instrument can have live/no-record
output `(1-f) rho` and recorded outputs weighted by f. If f<1 the live
branch preserves the normalized state rho. Thus conservation alone does
not force f=1. Only the additional requirement that this very attempt has
zero live probability for every density forces 1-f=0. The primary retains
the exact f=3/4 counterexample. The former no-record-as-source-erasure claim
is superseded; immediate registration is an additional, unadopted contract.

## Actual carrier dictionary and local continuation

Define `program(rho,v,c)=rho+i(v·sigma+cI)` and
`outcome(E,h+1)=E+i(h+1)I`. Context codes are `10+2m+p` for a head and
`20+2m+p` for a relay, where menu m and phase p are bits. The code carries
the exact density and the transported (1,2,3) frame; decoding separates the
Hermitian and anti-Hermitian parts. Its forward direction is R e_x and its
transverse direction is (-1)^p R e_y.

For signed event (h,s), let R_s=R for s=+1 and
`R_s=R diag(-1,1,-1)` for s=-1. The signed bootstrap, aligned so its outcome
root is at zero, has actual Records

```
0       : outcome(R E_h, h+1)
-R e_y  : head(R tau_h, R_s, menu=1, phase=1).
```

This is the original adjacent-packet dictionary translated to its root.
Here `R E_h` means Pauli-vector conjugation, not left matrix multiplication.
No supplied branch label is read by the root decoder. Ordinary later
outcomes have a matching relay predecessor one forward step away; the
bootstrap outcome is the unique exception. The historical two-Record-only
decoder is superseded by this whole-configuration predecessor rule.

The fixed radius-one rule writes only blank sites. A head writes a relay
on its transverse neighbor when there is exactly one adjacent context and
all other neighbors are outcomes. A relay writes its outcome forward when
it is the only neighbor. A head and the matching realized outcome finalize
a new forward head, toggling menu and phase. Existing occupied sites are
never rewritten. The outcome probabilities are tr(rho E_h), and a supplied
innovation in [0,1) selects a positive cumulative branch. This is a
conditional stochastic update rule, not an autonomous physical draw.

On an otherwise blank isolated strip, in head-relative coordinates,
`H_n=(n,0)`, `C_n=(n,(-1)^(n+1))`,
`O_n=(n+1,(-1)^(n+1))`. Distinct heads have different forward coordinates.
A head cannot coincide with a relay or outcome because their transverse
coordinates differ. A relay/outcome collision would require an odd index
difference from the forward coordinates and an even one from the side
parity. Same-role collisions require equal index. This proves fresh support
at every finite horizon. The local rule then supplies the three unique
writes inductively: before an outcome its future head lacks the required
outcome neighbor; after finalization the old target is permanently occupied.
The bootstrap outcome remains an allowed inert neighbor and never supplies
a competing context. Ordinary outcomes acquire compatible relay
predecessors, so the root selector persists.

The primary freshly decodes all 96 rotated bootstrap packets and performs
one complete event for each of the four canonical pairs using the actual
Block64 local rule, including active-site uniqueness. This is a bounded
check of the displayed induction, not a replay of the historical long runs.
The claim assumes a blank isolated strip; arbitrary collisions, multiple
fronts and a physical scheduler have not been supplied.

## Conditional current and response boundary

A head has charge one if it has no compatible forward head child, and zero
if it has a child with the same frame and toggled menu and phase. The
isolated construction has one frontier. Relay/outcome writes leave this
charge fixed; finalization moves it one signed unit forward edge. For an
oriented edge with incidence column `B=e_source-e_target`, define
`Delta J=e_target-e_source`. Then `Delta J+B=0` exactly. With supplied
k=(1,d), multiplying by each k_nu gives four conserved columns. It is four
multiples of the same incidence identity, not a derivation of four
independent physical source laws.

The supplied tensor k k^T is symmetric. With the supplied Minkowski
signature and unit spatial d it is null; its spatial d d^T is even under
d -> -d while the mixed entries are odd. The six-direction finite check
retains these facts. Physical head/source identity, normalization, the
meaning of one macro tick and a global coupling remain supplied. The
microstep append ledger may also be retained conditionally, but its
relay/outcome/finalize path is distinct from the head-frontier worldline.

The original Block53 conditional response remains an explicitly historical
supplier calculation: a source force from d d^T is inserted into a linear
kick/drift update, and TT quotient projection is linear. Consequently its
response is even in d and scales with a common coupling. A reported
nonzero response was at the specified generic momentum; the 17 cubed
Brillouin-zone check was a finite sample. Four physical current columns are
not the four TT constraint rows. The original lapse/shift, source/Bianchi,
full physical instrument and autonomous clock problems remain open.
No old TT controller or physical route builder is replayed by this note.

## Evidence and original-claim disposition

The exact endpoint, prior-version, cache and original input bodies are in
RECOVERY.json under the correction history; the full original review packet
remains external and hash-bound there. Original #6266 aggregate B (4096
literal rows and coherent code), C (right/left physical placement), the
long-history parts of E/F, G's specific TT response and H's 17 cubed sample
remain dated, unreplayed conditional reports. Their numbers remain in the
exact source/cache bodies; they are not fresh evidence for the new code.
D's sharp refinement and hazard argument, E's actual carrier dictionary,
and F's conditional incidence/head induction are retained above. A/I/J's
text, authority and old discipline gates are historical bookkeeping.

The old ten mutation outcomes are not ten independent scientific attacks:
`use_menu1`, `hide_physical_distance`, `separate_source` and
`per_branch_coupling` had explicit flag-based rejection in aggregates.
Actual arithmetic and geometry predicates are retained where stated;
no new robustness credit is assigned to the old aggregate mutation count.
The companion uses actual changed density and bridge operands against
unchanged baseline predicates. Input hashes are integrity checks, not
scientific sensitivity tests. No old campaign, index or manifest bytes
replace current shared state, and no physical supplier is accepted merely
because its path is present or absent.
