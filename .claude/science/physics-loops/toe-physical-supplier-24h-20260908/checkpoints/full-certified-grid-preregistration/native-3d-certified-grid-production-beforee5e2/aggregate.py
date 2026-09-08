"""Exact interval aggregation, streaming complete node membership."""
from fractions import Fraction as F
from pathlib import Path
from itertools import product
import json,math,hashlib
REPS=(0,1,3,5,10,15)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def node_interval(row,job,index,trig):
 if (row['job'],row['rep'],tuple(row['index']))!=(job,REPS[job//4],index):raise ValueError('node membership/order')
 ev=[float.fromhex(x) for x in row['eigenvalues_hex']];Q=row['vectors_hex']
 if len(ev)!=16 or ev!=sorted(ev) or any(not math.isfinite(x) for x in ev):raise ValueError('candidate eigenvalue schema')
 if len(Q)!=16 or any(len(x)!=16 for x in Q) or any(len(z)!=2 or any(not math.isfinite(float.fromhex(c)) for c in z) for line in Q for z in line):raise ValueError('candidate vector schema')
 c=row['certificate'];r=F(c['residual']);eta=F(c['eta']);inp=F(c['input_radius']);rad=F(c['eigenvalue_radius'])
 if r<0 or not 0<=eta<=F(1,2) or c['dimension']!=16:raise ValueError('residual/Gram domain')
 expected=F(0)
 for j in index:
  g=trig['rows'][j];q=F(float.fromhex(g['q_hex']));expected+=max(abs(q-F(g['lower_numerator'],g['denominator'])),abs(q-F(g['upper_numerator'],g['denominator'])))
 if inp!=expected or rad!=inp+2*r+4*max(abs(F(x)) for x in ev)*eta:raise ValueError('polar/input formula')
 intervals=c['root_intervals']
 if len(intervals)!=16:raise ValueError('root coverage')
 lows=[];highs=[]
 for x,z in zip(ev,intervals):
  a,b=map(F,z);lo=max(F(0),F(x)-rad);hi=F(x)+rad
  if hi<0 or not 0<=a<=b or a*a>lo or b*b<hi:raise ValueError('outward PSD root')
  lows.append(a);highs.append(b)
 lower=F(c['density_lower']);upper=F(c['density_upper'])
 if lower!=-sum(highs,F(0))/32 or upper!=-sum(lows,F(0))/32 or lower>upper:raise ValueError('density normalization')
 return lower,upper

def comparison(densities,cubes,trig):
 pi=F(trig['pi_upper_numerator'],trig['pi_denominator']);error=3*pi*pi/(8*32**2)
 base=densities[15];costs=[]
 for rep in REPS[:-1]:
  m=cubes['rows'][rep]['defects']
  if m not in (2,4,6):raise ValueError('defect count')
  lo=densities[rep][0]-base[1]-error;hi=densities[rep][1]-base[0]+error;delta_lo=8*lo/m;delta_hi=8*hi/m
  costs.append(dict(rep=rep,defects=m,density_lower=str(lo),density_upper=str(hi),strictly_positive=lo>0,limiting_delta_lower=str(delta_lo),limiting_delta_upper=str(delta_hi),auxiliary_defect_coefficient_lower=str(delta_lo/4),native_half_objective_defect_coefficient_lower=str(delta_lo/8)))
 return dict(quadrature_difference_radius=str(error),grid_n=32,folded_n=16,multiplicity=8,costs=costs,all_five_positive=all(x['strictly_positive'] for x in costs),common_density_lower=str(min(F(x['density_lower']) for x in costs)),scope='unit auxiliary infinite-density intervals; no explicit small-volume minimum')

def analyze(out,source,freeze):
 out=Path(out);source=Path(source);trig=json.loads((source/'TRIG_INPUTS.json').read_text());cubes=json.loads((source/'CUBE_INPUTS.json').read_text())
 actual=sorted(p.name for p in out.glob('job*') if p.is_dir())
 if actual!=[f'job{j:02d}' for j in range(24)]:raise ValueError('24 job membership')
 sums={r:[F(0),F(0)] for r in REPS};counts={r:0 for r in REPS};ledger=[];jobs=[]
 for job in range(24):
  folder=out/f'job{job:02d}'
  if (folder/'FAILURE.json').exists():raise ValueError('failed job')
  receipt=json.loads((folder/'RESULT.json').read_text());external=json.loads((out/f'job{job:02d}.receipt.json').read_text())
  if (receipt['job'],receipt['rep'],receipt['block'],receipt['nodes'],receipt['freeze'])!=(job,REPS[job//4],job%4,1024,freeze):raise ValueError('job receipt')
  if external['returncode'] or external['failure'] is not None or not 0<external['seconds']<=180 or external['tree_peak_bytes']>384*1048576:raise ValueError('external job cap')
  if sha(folder/'NODES.jsonl')!=receipt['node_sha']:raise ValueError('node file hash')
  expected=iter(product(range(4*(job%4),4*(job%4)+4),range(16),range(16)));count=0
  with (folder/'NODES.jsonl').open() as file:
   for line in file:
    try:index=next(expected)
    except StopIteration:raise ValueError('extra node') from None
    row=json.loads(line);lo,hi=node_interval(row,job,index,trig);rep=REPS[job//4];sums[rep][0]+=lo;sums[rep][1]+=hi;counts[rep]+=1;count+=1
    ledger.append(dict(job=job,rep=rep,index=index,line_sha=hashlib.sha256(line.encode()).hexdigest()))
  if count!=1024:raise ValueError('missing node')
  jobs.append(dict(job=job,result_sha=sha(folder/'RESULT.json'),node_sha=receipt['node_sha'],external_receipt_sha=sha(out/f'job{job:02d}.receipt.json')))
 if set(counts.values())!={4096}:raise ValueError('per-class coverage')
 densities={r:(a/4096,b/4096) for r,(a,b) in sums.items()};report=comparison(densities,cubes,trig)
 (out/'NODE_LEDGER.json').write_text(json.dumps(ledger,separators=(',',':'))+'\n')
 report.update(freeze=freeze,jobs=jobs,node_count=len(ledger),original_node_count=8*len(ledger),grid_density_intervals={r:[str(a),str(b)] for r,(a,b) in densities.items()},node_ledger_sha=sha(out/'NODE_LEDGER.json'))
 return report
