# Block 36 prior-art search

Search ref: `origin/main@aa7338d1fbc34a4b92205182b26793194e4727b6`.

The statement-level sweep used multiple noun orders and notation variants:

```bash
git grep -l -iE '(uniformizer.*(fair|half|1/2)|fair.*(uniformizer|record|randomizer)|Bernoulli.*(record|uniform))' origin/main -- 'docs/*.md' 'docs/work_history/**/*.md'
git grep -l -iE '(midpoint.*affin|affin.*midpoint|physical randomiz|randomizer.*affin|Jensen.*Bloch)' origin/main -- 'docs/*.md' 'docs/work_history/**/*.md'
git grep -l -iE '(fresh[- ](port|interface|site)|predictive reset|strong lumpab|archive.*reset|reset.*archive|append-only.*reset)' origin/main -- 'docs/*.md' 'docs/work_history/**/*.md'
git grep -l -iE '(Haar.*(transition|density|kernel|edge)|tree.*edge.*product|edge.*product.*tree|1\+.*dot.*normalized|Radon.Nikodym.*edge)' origin/main -- 'docs/*.md' 'docs/work_history/**/*.md'
git grep -l -iE '(six.axis.*POVM|POVM.*six.axis|\+/-.*e_x|E_\(a,s\)|P_n/3)' origin/main -- 'docs/*.md' 'docs/work_history/**/*.md'
git grep -l -iE '(normalized.*(edge|transition).*(factor|potential)|factor.*normalized.*transition|preparation-independent normalizer|mixture-independent normalizer|conditional independence.*neighbor)' origin/main -- 'docs/*.md' 'docs/work_history/**/*.md'
```

The last factor-typing query had no matching source.  The other searches were
read past titles into exact statements.  Material matched hits were:

- `ADMISSIBILITY_GAUSSIAN_CONTENT_ONLY_UNIFORMIZER...`: matching fair scalar;
- `OPERATIONAL_QUOTIENT_BORN_AFFINITY_CYCLE20...`: matching abstract affinity,
  quotient, lumpability, and reset criteria;
- `COMPLETE_CANDIDATE_LSTAR_ASSEMBLY_CYCLE41...`: closest append-only full
  candidate, but its probability layer is explicitly trace/Born;
- `POVM_OBSERVATION_COMPARATOR_EXACT_ARITHMETIC...`: matching six-axis table;
- `ADMISSIBILITY_REGISTERED_PARTITION_BARYCENTER_PUSHFORWARD...`: matching
  partition/pushforward algebra with a supplied auxiliary uniform coordinate;
- `RECORD_PERMANENCE_FORCES_FRESH_SITE...`: matching fresh-site requirement;
- `READ_RESET_CADENCE_INTERFERENCE_CHANNEL...`: matching reset/cadence
  distinction with the instrument and schedule supplied;
- Blocks 31--33 on the stacked branch: matching finite NN control and the
  exact two-use-versus-three-use renewal control;
- Block 35 on the parent branch: matching affinity-to-affine sufficiency and
  the raw-factor type obligation.

Classification: the individual components are prior art.  The target is open
only as the joined causal construction and its exact fixed-reference factor
typing.  If execution reduces to juxtaposing the sources without a new
load-bearing cylinder, strong-lumpability proof, or topology-sensitive factor
theorem, it fails V2--V5 and must not become a PR.
