import json,math,sys
from pathlib import Path
from preflight import verify,sha

def calculate(r,outer):
 def positive(x):
  if type(x) not in (float,int) or not math.isfinite(x) or x<=0:raise ValueError('positive finite timer')
  return x
 positive(outer);load=positive(r['runtime_load_seconds']);cases=r['cases']
 if len(cases)!=4:raise ValueError('case count')
 accounted=load
 for i,c in enumerate(cases):
  if (c['cid'],c['T'],c['start'],c['seed'])!=(i,(.5,.5,2.,2.)[i],('constant','bounded','constant','bounded')[i],202609340001+i):raise ValueError('case identity')
  if len(c['measurement_seconds'])!=4 or c['synthetic_rows']!=128 or c['synthetic_batches']!=16:raise ValueError('measurement/serialization coverage')
  if len(c['interval_seconds'])!=4 or len(c['blocks'])!=384 or len(c['measurements'])!=4:raise ValueError('coverage')
  timers=[positive(c['initialization_seconds']),positive(c['io_seconds']),positive(c['synthetic_output_seconds'])]+[positive(t) for t in c['interval_seconds']]
  for interval,measurement in zip(c['interval_seconds'],c['measurement_seconds']):
   if positive(measurement)>=interval:raise ValueError('measurement nesting')
  if sum(timers)>positive(c['case_seconds'])+1e-8:raise ValueError('timer nesting')
  accounted+=sum(timers)
  for b in c['blocks']:
   if type(b['face']) is not int or not 0<=b['face']<24:raise ValueError('face')
   positive(b['seconds'])
  if any(not math.isfinite(x) for m in c['measurements'] for x in m.values()):raise ValueError('measurement')
 if accounted>outer+1e-8:raise ValueError('outer accounting')
 overhead=max(0.,outer-accounted);arms=[]
 for i,c in enumerate(cases):
  sweep=max((t-m)/4 for z in cases if z['T']==c['T'] for t,m in zip(z['interval_seconds'],z['measurement_seconds']))
  measurement=max(m for z in cases if z['T']==c['T'] for m in z['measurement_seconds'])
  for burn in (16,64):
   chain=c['initialization_seconds']+c['io_seconds']+0+(burn+128)*sweep+128*measurement+overhead
   shard=4*chain+load
   arms.append(dict(T=c['T'],start=c['start'],burn=burn,sweep_seconds=sweep,measurement_seconds=measurement,measurement_count=128,synthetic_output_seconds=c['synthetic_output_seconds'],per_chain=chain,four_chain_shard=shard,total=4*shard))
 total=sum(a['total'] for a in arms);peak=max(a['four_chain_shard'] for a in arms)
 return dict(unallocated_outer_seconds_charged_each_chain=overhead,arms=arms,aggregate=total,max_shard=peak,forecast_gate=total<=2880 and peak<=120,scope='empirical short fixture extrapolation; no mixing or upper runtime guarantee')

def main():
 verify();out=Path(sys.argv[1]);d=json.loads((out/'DISPATCH.json').read_text())
 if sha(out/'RESULT.json')!=d['result_sha']:raise ValueError('result pin')
 for p,h in d['paths'].items():
  if sha(out/p)!=h:raise ValueError('path pin')
 lines=Path(str(out)+'.outer-time.txt').read_text().splitlines();real=[float(s.split()[1]) for s in lines if s.startswith('real ')];rss=[int(s.split()[0]) for s in lines if 'maximum resident set size' in s]
 if len(real)!=1 or len(rss)!=1:raise ValueError('outer receipt')
 outer=real[0]+.01
 if outer>30 or rss[0]/1048576>384:raise ValueError('outer cap')
 report=calculate(json.loads((out/'RESULT.json').read_text()),outer+1.)
 report.update(postprocessing_reserve_seconds=1.,acceptance_pending_external_forecast_time=True,outer_upper_seconds=outer,outer_rss_bytes=rss[0],dispatch_sha=sha(out/'DISPATCH.json'))
 print(json.dumps(report,indent=2))
