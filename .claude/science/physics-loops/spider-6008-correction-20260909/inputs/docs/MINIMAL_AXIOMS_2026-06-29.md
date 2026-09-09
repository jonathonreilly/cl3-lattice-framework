# Minimal Framework Axioms (Lattice, Qubit, Admissibility, Record)

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-06-29
**Type:** meta
**Status:** current public framework axiom memo for the qubit-on-`Z^3`
package with local admissibility and fixed scalar record readout.
**Status authority:** explicit owner approval for the 2026-06-29 foundation
reset is recorded in `docs/audit/AXIOM_MINIMALITY_POLICY.md` section 6.
Audit status remains set only by the independent audit lane.

**Supersedes:** `MINIMAL_AXIOMS_2026-06-05.md`. The 2026-06-05 memo remains the
historical source for the prior Lattice/Quantum/Record wording in which
realized outcome was latent in Record and no explicit local admissibility
constraint was named.

## Purpose

This note states the framework's minimal ontology premises. They are named
rather than treated as bare letter codes:

1. **Lattice**
2. **Qubit**
3. **Admissibility**
4. **Record**

Legacy `A1`/`A2` numbering and the older `Quantum` axiom name are historical.
New repo surfaces should use the axiom names above unless quoting an older
document.

## The Four Framework Axioms

### Lattice / Physical Locality

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

No site is privileged. Sites are distinguished by the supplied lattice
structure alone.

### Qubit / Site Possibility

Each site has a domain of local possibilities.

The full one-site possibility domain has algebraic presentation `M_2(C)`.

A `Cl(3,0)`-compatible real-algebra presentation may be used equivalently and
adds no further primitive structure.

No possibility is privileged. Possibilities are distinguished by the supplied
algebraic structure alone.

### Admissibility / Local Constraint

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the available possibilities are determined by, and vary with,
the nearest-neighbor conditions.

### Record / Fixed Reality

Records form.

When present, a record locks exactly one admissible local possibility. A
site never carries more than one record; records are permanent.

Only records are readable. A readout value is determined by record content
alone. For any finite collection of pairwise-disjoint records, scalar readout
`I` is additive, with `I(empty)=0`.

## Qualification

These axioms state only their named primitive content. Further physical
structure requires a retained derivation or bridge, or explicit approved-
primitive registration, before use as a premise. A choice not fixed by the
supplied structure remains a named conditional or open dependency.

A state is a configuration of records.

A law privileges no states. Its domain is a supplied condition, and at every
state where the condition holds it gives exactly one answer.

## Audit-Pipeline Treatment

The machine-readable source of this axiom set is the stable `minimal_axioms`
entry in `docs/audit/data/axiom_premise_nodes.json`. Dependencies on
`minimal_axioms` chain-satisfy without making downstream rows
`retained_bounded`.

**Primary runner:** `scripts/audit_companion_minimal_axioms_clean_base_exact.py`
checks only elementary algebra/notation sanity for the four axiom names. It
does not derive or enlarge the axiom set.

Axioms and approved primitives are the complete supplied foundation.
Depending on the Lattice, Qubit, Admissibility, or Record axiom, or on an
explicitly approved primitive such as `scale_reference_primitive`, must not be
treated as a source of bounded status. No admission class exists: every other
scientific dependency must be retained-derived or remain conditional/open.

## Relation To Dynamics And Kinetic Branch Selection

Admissibility is not a dynamics axiom. It determines availability by a
nearest-neighbor rule: for each site, the available possibilities are
determined by, and vary with, the nearest-neighbor conditions. It does not
choose a Hamiltonian or transfer operator, supply transition probabilities or
weights, select a scalar or nonzero kinetic branch, assert a Dirac-square
carrier, define a time metric, or provide a record-production process or
physical persistence dynamics.

Static spatial kinetic questions, probability/process questions, and temporal
evolution questions should be tracked separately. A realized kinetic branch, if
proposed, is downstream content: it needs a retained derivation or bridge, or
an approved-primitive registry update, before audit rows may use it
as load-bearing content. The four axioms are compatible with such later
content, but do not include it.

## Relation To The Older Observable-Principle Parent

`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` is not this axiom note and is not an
approved axiom-premise node. It remains a broader conditional parent that
packages additive scalar observables with further readout/log-det/modulus
structure. That older parent must not be moved wholesale into
`docs/audit/data/axiom_premise_nodes.json`.

Rows that require only the Record axiom should cite this minimal-axiom
authority. Rows that require P2/modulus, log-det, source/action, measurement,
Born weights, readout-context selection, central-sector decomposition, `K`/CPT
structure, transition relations, record-production dynamics, physical
persistence dynamics, local observability, or any other additional bridge must
cite separate retained authorities or remain bounded/pending according to the
audit ledger.

## Relation To The 2026-06-05 Record Wording

The 2026-06-05 Record axiom named durable realized-outcome registration and
gave a `K`/CPT orbit reading once a finite central-sector readout context and
fixed `K`/CPT conjugation were supplied. This reset separates generic site
possibility, local admissibility, and fixed records from context-specific
readout structure:

- Qubit names the domain of local possibilities and its full one-site algebraic
  presentation.
- Admissibility names the nearest-neighbor rule by which, for each site, the
  available possibilities are determined by, and vary with, the
  nearest-neighbor conditions.
- Record names the fixed locking of one admissible local possibility,
  one-record-per-site uniqueness, permanence, and finite scalar readout
  additivity over disjoint record collections.
- `K`/CPT orbit structure, central-sector decomposition, and any sector
  generation rule are downstream readout-context content, not generic axiom
  content.

## Open Gates Outside The Axioms

The four axioms do not close, import, or rename the framework's downstream open
gates. In particular, the following remain outside axiom content:

- the staggered-Dirac/finite-Grassmann realization and `AC_phi_lambda`;
- the strong-CP theta gauge and mass-side derivation obligations;
- P2/modulus/phase-blindness and any log-det readout theorem;
- context selection, measurement basis selection, Born weights, probability
  rules, update laws, decoherence mechanisms, and formation rules (which
  admissible possibility a new record locks, at which site, with what weight,
  or at what rate);
- arrow, record-production dynamics, physical persistence dynamics, time metric,
  and local observability of records;
- source/action and physical-observable identification;
- `g_bare = 1` convention handling;
- the scale-reference primitive and the separate gravity self-consistency
  question that the framework's natural unit equals the Planck length.

## Historical Context

The April 15 through May 20 sequence separated the one-qubit local algebra and
the `Z^3` lattice from downstream realization gates that had previously been
written too axiomatically. The 2026-06-04 memo added scalar finite Record
additivity as the third explicitly approved premise. The 2026-06-05 memo refined
Record to durable realized-outcome registration in a supplied readout context.
The 2026-07-04 owner-approved revision appended the formation sentence "Records
form." to the Record axiom: occurrence became named axiom content, while every
formation rule (which admissible possibility, at which site, with what weight,
at what rate) remained downstream supplier content. The file path was kept
unchanged so existing runner needles and links continue to resolve.

This memo exposes the remaining minimal ontology needed by the blocked audit
lanes: records are not arbitrary mosaics. The admissibility rule determines the
available possibilities at each site from the nearest-neighbor conditions, and
those available possibilities vary with those conditions, before a record can
lock one available local possibility. Probability, dynamics, readout contexts,
and physical observable bridges remain downstream.
