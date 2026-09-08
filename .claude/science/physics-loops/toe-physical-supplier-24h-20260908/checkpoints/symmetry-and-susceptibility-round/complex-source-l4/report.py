from pathlib import Path
import json,hashlib
p=Path(__file__).resolve().parent;a=json.loads((p/'ANALYSIS.json').read_text());status=json.loads((p/'STATUS.json').read_text());cells=[json.loads(f.read_text()) for f in sorted(p.glob('production_p*_c*.json'))];rows=[]
for pop,v in a['populations'].items():
 for r in v['rows']:rows.append(f"|{pop}|{r['harmonic']}|{r['h']}|{r['mean']:.9f} ± {r['SE']:.9f}|{r['reference']:.9f}|{r['consistency']}|{r['precision']}|{r['window_pass']}|")
text=f'''# Fixed L4 complex-source RK calibration

All16 fixed cells completed. Charged time including frozen micro: {status['charged_total_seconds']:.3f}seconds, below600. Maximum child RSS{max(c['rss_mib'] for c in cells):.3f}MiB. No replacements, additional cells or source changes. Each population has8 independent paired8-source vectors;128 source-replica records are not128 independent derivative replicas.

Aggregate nominal gate: **{a['all_nominal_gates_pass']}**. This includes the prospectively retained stricter paired half-window criterion. Full covariance, individual replica derivatives and every flagged comparison are retained in ANALYSIS.json. No automatic detuned stage follows either verdict.

|Population|harmonic|step|derivative ± paired-replica SE|independent RK reference|consistency|precision|half-window|
|---|---|---|---|---|---|---|---|
'''+ '\n'.join(rows)+'''

References are32 independent finite-chain means from the unchanged L4 burn128 RK pilot, with full two-harmonic covariance. They are not an exact stationary oracle. Same seeds pair source cells within each new population; populations and reference chains are independent. Nominal4SE tests are diagnostics, not coverage or mixing theorems. A positive source derivative does not establish a photon or isolate a pole. Source-step and finite-population biases remain possible even when comparisons do not flag.

The source is X_h=sum six complex Fourier absolute squares. Physical energy=lambda X_mixed is recorded separately from its shifted value. The exact component-symmetry proof removes stationary elastic means for this symmetric finite-component target; finite-chain means and stationarity errors still require statistical control. The new kernel remains a supplied nonlocal source probe.

The actual cost falls below the hot-based forecast with50% allowance. The original cold-as-hot1632second failure remains in MICRO.json; FORECAST.json records the separately justified hot decomposition. No claim of general scaling or guaranteed future runtime follows.
'''
(p/'PRODUCTION_REPORT.md').write_text(text)
files=['PRODUCTION_FREEZE.json','STATUS.json','ANALYSIS.json','PRODUCTION_REPORT.md']+[f.name for f in p.glob('production_p*_c*.json')]
(p/'PRODUCTION_MANIFEST.json').write_text(json.dumps({n:hashlib.sha256((p/n).read_bytes()).hexdigest() for n in sorted(files)},indent=2)+'\n')
print(text)
