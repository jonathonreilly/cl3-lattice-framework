"""Post-run presentation only; does not replace the frozen analyzer or its gates."""
from pathlib import Path
import json,hashlib,datetime
p=Path(__file__).parent;out=p/'PRODUCTION_OUTPUT';x=json.loads((out/'ANALYSIS.json').read_text());jobs=json.loads((out/'STATUS.json').read_text())
if len(jobs)!=128 or any(j.get('exit')!=0 for j in jobs):raise RuntimeError('incomplete fixed study')
ledger=json.loads((p/'RESOURCE_LEDGER.json').read_text());wall=sum(j['seconds'] for j in jobs);receipts=[json.loads((out/(j['name']+'.json')).read_text()) for j in jobs]
lines=['# Fixed propagated L8 diagnostic study','',f'All128 fixed segment jobs completed, representing48 independent chains, not128 replicas. Production wall time {wall:.6f}s; charged total {wall+ledger["preproduction_seconds"]:.6f}s. Maximum job {max(j["seconds"] for j in jobs):.6f}s; maximum RSS {max(z["rss_mib"] for z in receipts):.6f}MiB.','',f'Frozen analyzer status: `{x["status"]}`. This is a finite diagnostic classification, not stationarity, ground-state convergence, a gap certificate or photon evidence.','', '| Arm | harmonic | D ± SE | R ± SE | residual ± SE | signed VarH ± SE |','|---|---|---|---|---|---|']
for a in x['arms']:
 for r in a['rows']:
  if not r['valid']:lines.append(f'|{a["arm"]}|{r["harmonic"]}| invalid denominator | | | |');continue
  lines.append(f'|{a["parameters"]}|{r["harmonic"]}|{r["D"]:.9g} ± {r["D_SE"]:.5g}|{r["R"]:.9g} ± {r["R_SE"]:.5g}|{r["correction"]:.6g} ± {r["correction_SE"]:.4g}|{r["VarH"]:.6g} ± {r["VarH_SE"]:.4g}|')
 lines.append('')
lines+=['','Original-tag ranges per arm: '+str([(a['arm'],min(a['tag_fractions']),max(a['tag_fractions'])) for a in x['arms']]),'',f'Within-L8 comparison flags: {sum(c["flag"] for c in x["comparisons"])} / {len(x["comparisons"])}. Unflagged differences are not equivalence or equilibration.','', '## Prespecified matched-size contrasts','', 'L8h2 and L4h1 both use q=pi/2. A/B compares tau12 and C/D tau36, each burn32n; L4 RK512 versus L8 RK2048 remains a supplied initialization difference. Differences below are L8 minus L4, with independent-chain combined SE. They are not pass gates.','']
for c in x['matched_L4_size_contrasts']:lines.append(str(c))
lines+=['','The endpoint identities target the stationary finite product-G measure and its finite projected vector. Nonstationary sampled ratios do not become exact Rayleigh quotients by using those formulas. R is referenced to Epsi, not the ground energy. Signed negative variance estimates remain unmodified and any nonnegative bound plugin is not a confidence bound. Initial-tag loss tests one specific memory mechanism only.','', 'The 16 within-chain batches and immutable checkpoint segments are diagnostic records, not independent replicates. Full chain vectors, cross-harmonic influences and covariance are preserved in ANALYSIS.json; all segment states and receipt ancestry remain available. No retries, replacements or adaptive arms were part of the authorization.']
(p/'PRODUCTION_REPORT.md').write_text('\n'.join(lines)+'\n')
paths=[p/'PRODUCTION_REPORT.md',out/'ANALYSIS.json',out/'STATUS.json',p/'ROOT_AUTHORIZATION.json']+list(out.glob('*.json'))+list(out.glob('*.npz'))
(p/'FINAL_RESULTS_HASHES.json').write_text(json.dumps({str(f.relative_to(p)):hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(set(paths))},indent=2)+'\n')
