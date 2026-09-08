import json,hashlib,math
from pathlib import Path
p=Path(__file__).parent;x=json.loads((p/'MICRO.json').read_text());rate=x['hot_seconds']/4096
arms=[(12,2048,32),(36,2048,8),(36,2048,32)];out=[]
# Segments contain <=24n attempts. Initializer separate first-job charge.
for tau,rk,burn in arms:
 n=3072*tau;attempts=(burn+32)*n;segments=math.ceil((burn+32)/24)
 per=2*rate*24*n+5+x['initialization_seconds']
 total=16*(2*rate*attempts+segments*5+x['initialization_seconds'])
 out.append(dict(tau=tau,rk_sweeps=rk,burn_n=burn,n=n,chains=16,measured_n=32,attempts_per_chain=attempts,segments_per_chain=segments,segment_attempt_cap=24*n,forecast_max_segment_seconds=per,forecast_arm_seconds=total))
forecast=dict(micro_seconds=x['seconds'],control_seconds=json.loads((p/'CHECKPOINT_CONTROLS.json').read_text())['total_seconds'],rate=rate,headroom_factor=2,per_segment_overhead_seconds=5,arms=out,total_seconds=sum(z['forecast_arm_seconds'] for z in out)+x['seconds']+json.loads((p/'CHECKPOINT_CONTROLS.json').read_text())['total_seconds'],max_job_seconds=max(z['forecast_max_segment_seconds'] for z in out))
(p/'FORECAST.json').write_text(json.dumps(forecast,indent=2)+'\n')
text=f'''# L8 propagated reptation proposed fixed study

No science production has run. One authorized cost micro completed: {x['seconds']:.6f}s total, {x['initialization_seconds']:.6f}s initialization, {x['hot_seconds']:.6f}s for4096 measured updates, {x['rss_mib']:.4f}MiB. Its nonequilibrated moments are preserved but not used for physical conclusions.

Propose three fixed arms (tau,RK sweeps,burn/n): A(12,2048,32), B(36,2048,8), C(36,2048,32). Sixteen independent chains per arm,32n measured attempts,16 within-chain batches. A/C tests projection length; B/C tests reptation warmup. RK initialization stays fixed, so this does not independently test its equilibration. The warmup contrast includes the supplied finite-RK-plus-Q initial law. This is a minimal discriminator, not an exhaustive bias separation. Dynamics and initializer namespaces will be frozen in the eventual driver before any production.

At L8, M=1536 and n=2M tau. h1 has q=pi/4 and qhat²=2-sqrt2; h2 has q=pi/2 and qhat²=2. Only L8h2 matches L4h1. Preserve the staggered complex six-channel observable at each harmonic and the nine simultaneous moments [NF,X1,X2,Eavg,hLhR,X1Eavg,X2Eavg,X1²,X2²]. D=qhat²(.95 NF-E)/(512 S), R=D+XE/S-E. Covariance and all residual/variance gradients use independent chain means, never segment or batch pseudo-replicates.

A whole longest chain exceeds180s with conservative headroom. Propose exact resumable segments, each at most24n attempts. This gives3/2/3 segments per chain,128 jobs total. Each checkpoint carries labels, ring head, direction, three configurations, NF/complexO caches, exact NumPy RNG state and cumulative moments/batches/counters/tag history. Save/load is lossless for numeric arrays; no trajectory regeneration or reset. Segment boundaries do not create independent samples. Actual checkpoint interface passed384 exact continued events across L2/L4/L8 and three wrong-direction adverse controls. The future production driver still needs complete accumulator/checkpoint-integrity review and interruption/restart tests; this interface is not a production authorization.

Twice measured hot cost plus5s per segment and full measured initialization charged per chain forecasts {forecast['total_seconds']:.2f}s aggregate and {forecast['max_job_seconds']:.2f}s worst job, below4h and160s planning gate (hard180s384MiB). The5s allowance comfortably exceeds observed checkpoint roundtrip, but a real driver end-to-end check remains required before launch. No additional benchmark is run here. Fixed coverage must not change in response to results.

Prospective diagnostics: positive D with4SE<=10%D; any chain original-tag fraction>1% flags memory; A/C and B/C D,R,correction differences flagged at4SE using independent-chain covariance. R/VarH/correction may be indeterminate; all negative variances stay signed, no clipping or certified plug-in bound. Matched L4/L8 comparisons use combined independent SE and are size differences, not an agreement gate. At fixed tau, different finite-volume projection errors remain possible. No energy-dispersion exponent, photon, ground-state or continuum inference is licensed. Stationary path identities do not convert nonstationary sampled ratios into exact Rayleigh quotients.

Original L4 files remain immutable. Imported core and initializer are byte-identical reviewed revisions. No enumerated L8 state oracle, branching population, L16, or production has been used.
'''
(p/'PROPOSAL.md').write_text(text)
files=['core.py','initialize.py','micro.py','PREREGISTRATION.md','MICRO_FREEZE.json','MICRO.json','MICRO.stderr','checkpoint.py','checkpoint_controls.py','CHECKPOINT_CONTROLS.json','FORECAST.json','PROPOSAL.md']
(p/'DESIGN_FREEZE.json').write_text(json.dumps({f:hashlib.sha256((p/f).read_bytes()).hexdigest() for f in files},indent=2)+'\n')
print(json.dumps(forecast,indent=2));print('proposal',hashlib.sha256((p/'PROPOSAL.md').read_bytes()).hexdigest())
