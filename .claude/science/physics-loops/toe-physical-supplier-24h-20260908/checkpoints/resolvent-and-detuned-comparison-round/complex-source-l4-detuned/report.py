from pathlib import Path
import json,hashlib
p=Path(__file__).resolve().parent;a=json.loads((p/'ANALYSIS.json').read_text());s=json.loads((p/'STATUS.json').read_text());cells=[json.loads(f.read_text()) for f in p.glob('cell_g*_c*.json')];lines=[]
for g,x in a['groups'].items():
 for m in x['moments']:
  text=f"{m['value']:.9f} ± {m['SE']:.9f}" if m['valid'] else 'INVALID'
  refs='; '.join(f"F{r['F']}: {r.get('value',float('nan')):.9f} ± {r.get('SE',float('nan')):.9f}, compatible={r.get('nominal_4SE_compatible',False)}" for r in m['reference_comparisons'])
  lines.append(f"|{g}|{x['population']}|{x['burn']}|{m['harmonic']}|{text}|{m.get('precision_nominal',False)}|{refs}|")
text=f'''# Fixed matched detuned L4 source-response run

All21 frozen cells completed in{s['charged_total_seconds']:.3f}seconds charged wall time, below900; peak child RSS{max(c['rss_mib'] for c in cells):.3f}MiB. No replacements, extra seeds or source changes. Three groups contain8 independent paired seven-source vectors each.168 source-replica records and their40-point windows are not168 independent ratio replicas.

|group|population|burn|harmonic|moment ± paired delta SE|10% precision|independent finite-forward references|
|---|---|---|---|---|---|---|
'''+ '\n'.join(lines)+'''

Every method comparison combines uncertainty from independent runs, including the literal F24 and F12 raw reference records. Neither reference is an exact pure target. Full seven-energy covariance, shared-numerator two-harmonic ratio covariance, all replica B/T values, negative counts and noisy secants remain in ANALYSIS.json. Invalid pooled T is not rescued. Population and burn comparisons use independent seed groups; half-window comparisons retain within-replica pairing.

Source-step .02 remains fixed and no detuned source-step sensitivity was measured. Passing a nominal comparison would not bound source bias, population bias or mixing; failing one remains a failure, not a reason to retune. No pole, photon or larger-volume conclusion follows. The earlier RK gate supplies a separate finite calibration, not a detuned ground oracle.

The original600second forecast failure and prospective900second resource amendment are preserved. Actual runtime does not retrospectively change the compute contract. Production sources are bound in PRODUCTION_FREEZE.json and every cell; all source and reference hashes are checked by the analyzer. No automatic next stage is authorized.
'''
text+='\n## All group sensitivities\n\n'+json.dumps(a['group_comparisons'],indent=2)+'\n'
text+='\n## Half-window and sign diagnostics\n\n'+json.dumps({g:[{'harmonic':m['harmonic'],'window':m['window'],'negative_B':m['negative_B'],'nonpositive_T':m['nonpositive_T'],'reversed_secants':m['reversed_secants']} for m in x['moments']] for g,x in a['groups'].items()},indent=2)+'\n'
(p/'PRODUCTION_REPORT.md').write_text(text);names=['ANALYSIS.json','PRODUCTION_REPORT.md','PRODUCTION_FREEZE.json','STATUS.json','REFERENCE_BINDING.json']+[f.name for f in p.glob('cell_g*_c*.json')];(p/'PRODUCTION_MANIFEST.json').write_text(json.dumps({n:hashlib.sha256((p/n).read_bytes()).hexdigest() for n in sorted(names)},indent=2)+'\n');print(text)
