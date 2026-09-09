# Mathematics sector search: foundations review of a discrete-record framework

Scope: an admissible placement is interpreted as a \(k\)-subset of the vertices of
\(C_n\) with **no adjacent occupied vertices**, including across the periodic seam.
The four phases are taken to be four independent global choices on which translation
acts trivially. If “minimum separation” means a larger exclusion radius, the first
formula below must be replaced by the \(p\)-separated generalization noted there.

## Sector-entry matrix

| Sector | Reframe | Candidate theorem/tool | Minimal toy example | How it attacks the wall | What would falsify it | First artifact |
|---|---|---|---|---|---|---|
| Census | Count size-\(k\) independent sets of a cycle, then attach a four-valued phase. | Kaplansky's circular no-consecutive-selection lemma; rooted cyclic gap compositions. | \(C_5,k=2\): the five independent pairs agree with \(\frac5{5-2}{3\choose2}=5\). | Replaces an ad hoc census by a general closed form and states the precise separation convention. | One enumerated admissible state contains adjacent sites, phases depend on placement, or labels are not actually quotiented as assumed. | `verify_counts.py`: formula and brute-force equality at \(n=11\). |
| Translation action | Treat origin shifts as the \(C_n\)-action on binary necklaces constrained to be independent sets. | Orbit-stabilizer, prime-order lemma, Burnside's lemma / cyclic-necklace period decomposition. | On \(C_{12}\), `100000100000` has orbit 6 and stabilizer 2. | Proves freeness at 11 and gives exact, testable corrections at composite \(n\). | A listed orbit has a different size under explicit rotation, or the model lets translations act nontrivially on phase. | Full \(n=12\) orbit-size table and representatives below. |
| Automata equivalence | Add an observation map to the finite dynamical system before asking whether states are “the same.” | Centralizer automorphisms (conjugacy), Moore/Myhill–Nerode behavioral equivalence, greatest bisimulation. | Two states can have the same future output trace but different predecessor trees, so need not be symmetry-related. | Separates gauge identity, structural isomorphism, and mere empirical indistinguishability. | A proposed quotient fails to preserve update or a declared physical observable. | Definitions and a four-state separating automaton below. |
| Information | Regard the 748 states as 68 free \(C_{11}\)-orbits, with an origin coordinate after choosing a section. | Hartley entropy additivity; Shannon chain rule; noiseless coding bound; two-part MDL. | \(C_3\times\{a,b\}\): \(\log_2 6=\log_2 2+\log_2 3\). | Says exactly which bits are menu/model cost and which are conditional index cost. | Nonuniform selection, a nonfree action, or a shorter asserted code that is not uniquely decodable. | Exact bit values and the coding qualification below. |
| Model theory | Formalize “same landed observations” as equality of consequences in an observation sublanguage. | Independence via two models; conservative extension; definitional extension; Beth definability as the diagnostic. | Add an unconstrained predicate \(P\) to a theory \(T\), then compare two expansions. | Distinguishes substantive undecidability in the old language from trivial freedom introduced by a new primitive. | Either fork is inconsistent, an observation sentence separates them, or the new symbol has a unique explicit definition. | A language-relative classification and proof obligations below. |

## 1. Census: exact relation to the classical cycle count

Let \(I(n,k)\) be the number of independent \(k\)-subsets of the labeled cycle
\(C_n\). For \(1\le k\le \lfloor n/2\rfloor\), mark one selected vertex and read
clockwise. The \(k\) positive gaps of unselected vertices have sum \(n-k\), hence
there are

\[
{n-k-1\choose k-1}
\]

rooted gap words. There are \(n\) choices of marked origin, and every unrooted
selected set is produced once for each of its \(k\) selected vertices. Therefore

\[
I(n,k)=\frac nk{n-k-1\choose k-1}
=\frac{n}{n-k}{n-k\choose k}.
\]

The equality is the elementary identity

\[
{n-k-1\choose k-1}=\frac{k}{n-k}{n-k\choose k}.
\]

Thus the claimed expression is **exactly**, not merely asymptotically, the
Kaplansky circular no-two-consecutive count multiplied by four:

\[
N_{n,k}=4I(n,k)
=\frac{4n}{k}{n-k-1\choose k-1}
=\frac{4n}{n-k}{n-k\choose k}.
\]

The stated \(n=11\) formula uses
\({10-k\choose k-1}={n-k-1\choose k-1}\), so there is no discrepancy under
the stated interpretation. The allowed range is \(k\le\lfloor n/2\rfloor\).
For exclusion of the next \(p\) sites rather than just the neighbor, Kaplansky's
generalization is \(\frac{n}{n-pk}{n-pk\choose k}\), subject to its feasibility
condition; using the \(p=1\) formula would then be a genuine discrepancy.

Reference: I. Kaplansky, “Solution of the ‘problème des ménages’,” *Bulletin of
the AMS* **49** (1943), 784–785, DOI
[10.1090/S0002-9904-1943-08035-4](https://doi.org/10.1090/S0002-9904-1943-08035-4).

### Reproducible check (first increment)

Command: `python3 verify_counts.py` (relevant first block)

```text
symbolic formula difference: 0
n=11: k, rooted-gap formula x4, Kaplansky formula x4, enumerated x4
2 176 176 176
3 308 308 308
4 220 220 220
5 44 44 44
n=11 total: 748 = 68 * 11
```

## 2. Translation: the prime lemma and the composite spectrum

### Exact lemma

Let \(C_p\) act on subsets of \(\mathbb Z/p\mathbb Z\) by translation, with
\(p\) prime. If \(S\) is a nonempty proper subset, then its stabilizer is a
subgroup of \(C_p\), so its order is either 1 or \(p\). In the second case a
nonidentity translation fixes \(S\); that translation generates \(C_p\), hence
every translation fixes \(S\). Transitivity on the sites then forces \(S\) to be
empty or the whole site set, a contradiction. Thus

\[
\operatorname{Stab}_{C_p}(S)=\{e\},\qquad
|C_pS|=\frac{p}{|\operatorname{Stab}(S)|}=p.
\]

This is orbit-stabilizer plus the subgroup structure of a prime-order cyclic
group. Strictly, “no fixed points” must read “no **nonidentity** group element
fixes a placement”; the identity fixes every placement. At \(p=11\), every
admissible \(k=2,3,4,5\) placement is a proper nonempty subset, so the action is
free. If translations leave the four-valued phase unchanged, the product with
the phase set remains free.

### Composite-\(n\) failure mode

Write a placement as a cyclic binary word of length \(n\). It has orbit size
\(q\mid n\) exactly when its least rotational period is \(q\); equivalently, it
is \(h=n/q>1\) repeats of a primitive length-\(q\) motif. Its stabilizer then has
order \(h\). If the placement has \(k\) occupied sites, repetition forces

\[
h\mid n,\qquad h\mid k,
\]

so a nontrivial stabilizer is possible only if \(\gcd(n,k)>1\). This condition
is necessary, not sufficient for each individual placement: the placement must
actually be periodic. More explicitly, translation by \(r\) partitions the
sites into \(c=\gcd(n,r)\) cycles, each of length \(n/c\); a fixed placement is
a union of these cycles. Under the no-adjacency constraint it is equivalently a
repeated independent-set word on the quotient cycle.

Burnside's lemma gives the total number of orbits. The complete orbit-size
spectrum follows by primitive-period/Möbius inversion. If \(I(p,w)\) is the
Kaplansky count above, the number of length-\(p\), weight-\(w\) admissible words
of least period \(p\) is

\[
B(p,w)=\sum_{d\mid\gcd(p,w)}\mu(d)I(p/d,w/d).
\]

For an \(n\)-site, weight-\(k\) placement, the number of orbits of size \(p\mid n\)
is therefore

\[
\frac1p B\!\left(p,\frac{k}{n/p}\right)
\quad\text{if }(n/p)\mid k,
\]

and zero otherwise. Direct enumeration gives the following falsifiable
\(n=12\) prediction. `orbit-size: orbit-count` counts unphased orbits; the last
column also shows one binary representative for every occurring size.

| \(k\) | Unphased placements | Unphased orbit spectrum | Example by orbit size |
|---:|---:|---|---|
| 1 | 12 | `12: 1` | `12=100000000000` |
| 2 | 54 | `6: 1`, `12: 4` | `6=100000100000`; `12=101000000000` |
| 3 | 112 | `4: 1`, `12: 9` | `4=100010001000`; `12=101010000000` |
| 4 | 105 | `3: 1`, `6: 1`, `12: 8` | `3=100100100100`; `6=101000101000`; `12=101010100000` |
| 5 | 36 | `12: 3` | `12=101010101000` |
| 6 | 2 | `2: 1` | `2=101010101010` |
| **2–6 subtotal** | **309** | **`2: 1`, `3: 1`, `4: 1`, `6: 2`, `12: 24`** | **29 unphased orbits** |

With four inert phase values, multiply every placement count and every orbit
count (but not orbit size) by four. Thus the \(k=2\ldots6\) model has 1236
phased states and spectrum

| Orbit size | 2 | 3 | 4 | 6 | 12 |
|---:|---:|---:|---:|---:|---:|
| Phased orbit count | 4 | 4 | 4 | 8 | 96 |
| States in those orbits | 8 | 12 | 16 | 48 | 1152 |

The 116 phased orbits correctly account for all \(8+12+16+48+1152=1236\)
states. This is the composite-\(n\) correction to division by \(n\).

### Reproducible check (second increment)

Command: `python3 verify_counts.py` (orbit block)

```text
n=12 independent-set translation orbits
k placements orbit_size:orbit_count example_by_size
1 12 12:1 12=100000000000
2 54 6:1 12:4 6=100000100000;12=101000000000
3 112 4:1 12:9 4=100010001000;12=101010000000
4 105 3:1 6:1 12:8 3=100100100100;6=101000101000;12=101010100000
5 36 12:3 12=101010101000
6 2 2:1 2=101010101010
nonfree (k, orbit, stabilizer, gcd(12,k)): [(2, 6, 2, 2), (3, 4, 3, 3), (4, 6, 2, 4), (4, 3, 4, 4), (6, 2, 6, 6)]
```

## 3. Finite deterministic automata: an equivalence ladder

The question is under-specified until the system includes observables. Write a
finite autonomous Moore system as

\[
\mathcal A=(X,f,o),\qquad f:X\to X,\quad o:X\to Y.
\]

The standard notions are:

1. **Literal state equality:** \(x=y\). This is the finest relation.
2. **Dynamical conjugacy / symmetry orbit:** two systems \((X,f)\) and
   \((X',f')\) are conjugate when a bijection \(h:X\to X'\) obeys
   \(hf=f'h\). Within one system, the update-rule automorphism group is the
   centralizer
   
   \[
   \operatorname{Aut}(X,f)=\{h\in\operatorname{Sym}(X):hf=fh\}.
   \]
   
   States \(x,h(x)\) are structurally symmetry-related. For physical/gauge
   equivalence one must restrict to automorphisms that also preserve the full
   observation structure, \(o\circ h=o\), or transform it by an explicitly
   declared covariance. Commuting with \(f\) alone is not enough.
3. **Behavioral (Moore/Myhill–Nerode) equivalence:**
   
   \[
   x\sim_{\rm beh}y
   \iff o(f^t(x))=o(f^t(y))\quad\text{for every }t\ge0.
   \]
   
   This identifies states that no future experiment represented in \(o\) can
   distinguish.
4. **Bisimulation:** a relation \(R\subseteq X\times X\) such that
   \(xRy\) implies \(o(x)=o(y)\) and \(f(x)R f(y)\). Its greatest fixed point
   is bisimilarity. For this deterministic, one-action Moore system,
   bisimilarity equals future-trace/behavioral equivalence. For nondeterministic
   transition systems, trace equivalence is generally coarser than bisimulation.

Consequently, for observation-preserving automorphisms,

\[
x=y\ \Longrightarrow\ x\sim_{\rm gauge}y
\ \Longrightarrow\ x\sim_{\rm beh}y= x\sim_{\rm bisim}y,
\]

and neither converse holds in general. With no output/atomic-proposition map,
bisimulation can collapse everything in an autonomous total system, so invoking
“bisimulation” without declaring observables has no physical content.

### Minimal separating examples

- Let \(f\) be the identity on two states but let their outputs differ. The swap
  commutes with \(f\), yet it is not observation-preserving and the states are
  behaviorally distinct. Thus a bare update automorphism is not automatically
  gauge.
- Let \(X=\{a,b,c,z\}\), \(f(a)=f(b)=z\), \(f(c)=a\), \(f(z)=z\), and
  \(o(a)=o(b)=o(c)=0,o(z)=1\). States \(a,b\) both generate
  \(0,1,1,\ldots\), so they are bisimilar. No global automorphism sends \(a\)
  to \(b\): \(a\) has predecessor \(c\), while \(b\) has no predecessor.
  Behavioral equivalence can therefore be strictly coarser than symmetry orbit
  equivalence.

The finite-state artifact is ordinary partition refinement: begin with states
partitioned by \(o\), repeatedly split a block when successors land in different
blocks, and stop at the fixed point. This computes the Moore-minimal/greatest-
bisimulation quotient.

```text
Moore behavioral classes: [['a', 'b'], ['c'], ['z']]
predecessor counts: {'a': 1, 'b': 0, 'c': 0, 'z': 3}
```

### Physical verdict

“Same world” is defensible as **gauge equivalence under a declared group of
observation-preserving automorphisms**. A symmetry of the law need not be gauge;
it may map one physically different solution to another. Bisimulation supports
only the weaker claim “same complete observable future.” It becomes identity of
worlds only if the framework separately postulates that the chosen observation
algebra is ontologically complete. Automata theory cannot supply that postulate.

## 4. Information accounting: what the logarithm does and does not say

Let \(X\) be the 748 phased placements and \(G=C_{11}\). Freeness gives the set
cardinality statement

\[
|X|=|X/G|\,|G|=68\cdot 11.
\]

After choosing one representative in every orbit (a section), every state is
uniquely \(g\cdot s(q)\), giving a noncanonical bijection
\(X\cong (X/G)\times G\). The resulting “origin coordinate” depends on the
section; the cardinality and entropy equations do not.

The exact information-theoretic names are:

- **Hartley entropy additivity:** \(H_0(X)=\log_2|X|\), so a finite product
  factorization gives \(H_0(X)=H_0(X/G)+H_0(G)\).
- **Shannon chain rule under a uniform free-action factorization:** if \(X\) is
  uniform, then the orbit \(Q\) and section-dependent group coordinate \(U\)
  are uniform and independent, hence
  
  \[
  H(X)=H(Q,U)=H(Q)+H(U\mid Q)=\log_2 68+\log_2 11.
  \]
- **Two-part MDL / conditional index code:** with a description of the menu
  \(M\) already supplied, an ideal uniform index has conditional codelength
  \(L(x\mid M)=-\log_2(1/748)=\log_2 748\). The full two-part description is
  \(L(M)+L(x\mid M)\), not just its second term.
- **Shannon's noiseless source-coding bound:** any binary prefix code has
  expected length at least \(H(X)\), and an appropriate code achieves expected
  length below \(H(X)+1\). Fractional “9.55 bits” is an ideal/self-information
  or asymptotic block-code length; a fixed-length one-shot index needs
  \(\lceil\log_2 748\rceil=10\) bits.

The numerical check is:

~~~text
bits: log2(748)=9.546894460 log2(68)=6.087462841 log2(11)=3.459431619 difference=0.0
~~~

Thus “menu derived, choice costs about 9.55 ideal bits conditional on the menu”
is correct **only under a uniform prior/code**. “Choice free” has no standard
information-theoretic meaning. Deriving the menu can lower \(L(M)\); it does not
select an element or prove that the realized element is algorithmically
incompressible. The corresponding algorithmic statement is only a counting
bound: most members of a finite menu have conditional Kolmogorov complexity
near \(\log_2|X|\), while particular members can be much simpler.

## 5. Model theory: classify the E1/E2 fork relative to a language

Fix an observation language \(L_{\rm obs}\), a larger theoretical language
\(L\supseteq L_{\rm obs}\), and a base theory \(T\). The relevant standard
vocabulary is:

- A sentence \(E\in L\) is **independent of \(T\)** when
  \(T\nvdash E\) and \(T\nvdash\neg E\). For consistent first-order \(T\), the
  completeness theorem turns the usual model construction into the exact test:
  both \(T+E\) and \(T+\neg E\) must have models.
- Complete extensions \(T_1,T_2\supseteq T\) are **observationally
  equivalent** when
  
  \[
  T_1\cap\operatorname{Sent}(L_{\rm obs})
  =T_2\cap\operatorname{Sent}(L_{\rm obs}).
  \]
  
  Equivalently, no sentence expressible in the landed-observation language
  separates their theories.
- An \(L\)-theory \(T'\) is **conservative over** an \(L_{\rm obs}\)-theory
  \(T_{\rm obs}\) when every \(L_{\rm obs}\)-sentence provable in \(T'\) was
  already provable in \(T_{\rm obs}\). Conservativity must always name the
  language/signature over which no new consequences appear.
- A **definitional extension** adds new symbols together with explicit
  definitions in the old language. Every old-language model then has a unique
  expansion (up to the definition), and the extension is conservative. The
  converse is false: a conservative extension need not be definitional.

### Classification of a supplied primitive

Under the natural reading that E1/E2 assign different values or structures to
a newly supplied primitive that the landed-observation axioms do not constrain,
the expanded theory is a **conservative, non-definitional extension over
\(L_{\rm obs}\)**, and E1/E2 are distinct expansions (or, after deciding every
sentence, distinct completions) with the same observation reduct. Conservativity
is not automatic from the word “primitive”: a clean sufficient proof is that
every model of the observation theory admits an E1 expansion and an E2
expansion.

It is non-definitional precisely because one \(L_{\rm obs}\)-model admits two
expansions that disagree on the primitive. In first-order logic, **Beth's
definability theorem** sharpens this: if the theory implicitly fixed the new
predicate in every pair of models with the same old-language reduct, then that
predicate would have an explicit old-language definition. The E1/E2 pair is a
direct witness that implicit definability fails.

This is a real model-theoretic underdetermination result once the following have
actually been shown:

1. both fork theories are consistent (preferably by explicit models);
2. they are genuinely complete if the word “completion” is used;
3. their \(L_{\rm obs}\)-consequence sets agree, not merely the finite list of
   observations tested so far; and
4. E1/E2 differ on a sentence of the **fixed** theoretical language.

The last point is the sharp caveat. If the fork is manufactured only by adding
an entirely unconstrained new symbol, its independence is conservative but
trivial: it does not establish a Gödel-style or otherwise substantive
independence theorem about the original language. If \(E\) was already in the
original language, by contrast, explicit models of \(T+E\) and \(T+\neg E\)
establish genuine independence of that old-language sentence. Also, \(T+E\)
and \(T+\neg E\) are not automatically complete theories; they are merely two
consistent extensions unless all remaining sentences are decided.

### Minimal finite model

Let \(T_{\rm obs}\) say that the equality-only universe has exactly three
elements. Add a unary predicate \(P\) with no defining axiom. The same
observation reduct has eight expansions. Let E1 say \(|P|=1\) and E2 say
\(|P|=2\). The complete theories of these finite expanded structures disagree
about \(P\) but have the identical equality-only reduct. Neither singleton nor
two-element choice of \(P\) is definable in the pure three-element set, because
its full permutation automorphism group moves every such subset.

~~~text
3-point observation reduct: 1 reduct; unary-primitive expansions by cardinality: {0: 1, 1: 3, 2: 3, 3: 1}
E1=|P|=1 and E2=|P|=2: 3 expansions each; identical equality-only reduct
~~~

## Bottom line

- Claims 1, 2 (for prime 11), and 4 are exact classical applications:
  Kaplansky's circular selection lemma, orbit-stabilizer for prime cyclic
  actions, and Hartley/Shannon additivity for a uniform free-action
  factorization.
- The numerical census has no discrepancy if admissibility means one empty site
  between sources and phase is an independent four-valued global label.
- The required repairs are: use Burnside/Möbius period counting at composite
  \(n\); distinguish observation-preserving gauge orbits from behavioral
  equivalence; and call the E1/E2 construction substantive independence only
  after fixed-language consistency and full observation-conservativity proofs.
- The sharpest missing tool is a **language-aware quotient audit**:
  Moore/Myhill–Nerode partition refinement for the finite dynamics, paired with
  Beth definability for the primitive/observation boundary. For the immediate
  census generalization, the exact missing enumerator is Burnside's lemma with
  the cyclic cycle index and Möbius inversion.
