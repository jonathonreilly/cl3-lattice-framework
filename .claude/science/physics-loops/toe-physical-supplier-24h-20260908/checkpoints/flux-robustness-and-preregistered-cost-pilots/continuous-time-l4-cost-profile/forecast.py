import math
from adapter import NAMES

def calculate(r,charged):
 def pos(x):
  if type(x) not in (int,float) or not math.isfinite(x) or x<=0:raise ValueError('finite positive timing')
  return x
 pos(charged)
 if list(r['names'])!=list(NAMES) or len(r['cases'])!=4:raise ValueError('measurement schema')
 accounted=0.;blocks=[];measures=[];initial=[];ios=[];synthetics=[]
 for i,c in enumerate(r['cases']):
  if (c['cid'],c['T'],c['start'],c['seed'])!=(i,(.5,.5,2.,2.)[i],('constant','propagated','constant','propagated')[i],202609420000+i):raise ValueError('case identity')
  if [b['face'] for b in c['blocks']]!=[0,64,128,191] or len(c['measurements'])!=4 or len(c['measurement_seconds'])!=4:raise ValueError('physical cadence')
  if len(c['postblock_paths'])!=4 or len(c['postblock_io_seconds'])!=4:raise ValueError('post-block path coverage')
  if [x['file'] for x in c['postblock_paths']]!=[f'path{i}_block{j}.json' for j in range(4)]:raise ValueError('post-block path identity')
  if any(not isinstance(x['sha'],str) or len(x['sha'])!=64 for x in c['postblock_paths']):raise ValueError('post-block hash schema')
  if c['synthetic_rows']!=128 or c['synthetic_batches']!=16:raise ValueError('serialization cadence')
  for v in c['measurements']:
   if set(v)!=set(NAMES) or any(not math.isfinite(x) for x in v.values()):raise ValueError('finite readouts')
  bs=[pos(b['seconds']) for b in c['blocks']];ms=[pos(x) for x in c['measurement_seconds']]
  ini=pos(c['initialization_seconds']);io=pos(c['io_seconds']);
  if abs(io-pos(c['final_io_seconds'])-sum(pos(x) for x in c['postblock_io_seconds']))>1e-8:raise ValueError('full I/O accounting')
  sy=pos(c['synthetic_output_seconds']);total=sum(bs+ms)+ini+io+sy
  if total>pos(c['case_seconds'])+1e-8:raise ValueError('timer nesting')
  accounted+=total;blocks+=bs;measures+=ms;initial.append(ini);ios.append(io);synthetics.append(sy)
 if accounted>charged:raise ValueError('outer accounting')
 overhead=charged-accounted;arms=[]
 for start in ('constant','propagated'):
  for burn in (16,64):
   chain=2*(192*(burn+128)*max(blocks)+128*max(measures)+max(initial)+max(ios)+max(synthetics)+overhead)
   arms.append(dict(T=.5,start=start,burn=burn,measurement_count=128,per_chain=chain,chains=16))
 total=sum(x['per_chain']*16 for x in arms)+60+charged
 return dict(arms=arms,aggregate=total,max_chain=max(x['per_chain'] for x in arms),forecast_gate=total<=2880 and all(x['per_chain']<=150 for x in arms),charged_profile_seconds=charged,unallocated_charged_each_chain=overhead,measurement_seconds=max(measures),synthetic_seconds=max(synthetics),scope='empirical cost extrapolation only; no runtime bound or mixing inference')
