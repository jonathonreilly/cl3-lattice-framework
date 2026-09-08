"""Independent exact per-job replay and final aggregation. No eigenvalue call."""
from pathlib import Path
import json,hashlib,sys,argparse,time,signal,resource,math
from fractions import Fraction as F
from itertools import product
import runpy
HERE=Path(__file__).resolve().parent
_core=runpy.run_path(str(HERE/'independent.py'));matrix=_core['matrix'];verify=_core['verify'];ck=_core['ck']
SOURCE=HERE.parent/'native-3d-certified-grid-production';REPS=(0,1,3,5,10,15)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def preflight():
 pin=read(HERE/'SOURCE_PIN.json');ck(sha(SOURCE/'FREEZE.json')==pin['freeze'],'source freeze')
 for p,h in read(SOURCE/'FREEZE.json')['files'].items():
  p=Path(p);p=p if p.is_absolute() else SOURCE/p;ck(sha(p)==h,'source file')
 for p,h in read(SOURCE/'RUNTIME.json')['files'].items():ck(sha(Path(p))==h,'runtime file')
 return pin['freeze']
def bounded(x,cap):ck(type(x) in (int,float) and math.isfinite(x) and 0<x<=cap,'resource')
def jobcheck(production,job,freeze):
 ck(0<=job<24,'job');folder=production/f'job{job:02d}';ck(not (folder/'FAILURE.json').exists(),'failed job');r=read(folder/'RESULT.json');ext=read(production/f'job{job:02d}.receipt.json')
 ck((r['job'],r['rep'],r['block'],r['nodes'],r['freeze'])==(job,REPS[job//4],job%4,1024,freeze),'job receipt');ck(ext['name']==f'job{job:02d}' and ext['returncode']==0 and ext['failure'] is None,'external receipt')
 bounded(r['seconds'],170);bounded(r['peak_bytes'],384*1048576)
 for key,cap in [('seconds',180),('external_seconds',180),('tree_peak_bytes',384*1048576),('external_peak_bytes',384*1048576)]:bounded(ext[key],cap)
 ck(len(r['component_seconds'])==4,'timers')
 for x in r['component_seconds']:bounded(x,170)
 ck(sum(r['component_seconds'])<=r['seconds']+1e-9,'timer nesting')
 path=folder/'NODES.jsonl';ck(sha(path)==r['node_sha'],'raw hash');trig=read(SOURCE/'TRIG_INPUTS.json');cubes=read(SOURCE/'CUBE_INPUTS.json');lo=hi=F(0);count=0;hashes=[];width=F(0);expected=iter(product(range(4*(job%4),4*(job%4)+4),range(16),range(16)))
 with path.open() as file:
  for line in file:
   try:index=next(expected)
   except StopIteration:raise ValueError('extra node') from None
   row=json.loads(line);ck((row['job'],row['rep'],tuple(row['index']))==(job,REPS[job//4],index),'node ordering');A,radius=matrix(cubes['rows'][row['rep']],[trig['rows'][j] for j in index])
   Q=[[(F(float.fromhex(re)),F(float.fromhex(im))) for re,im in pair] for pair in row['vectors_hex']];lam=[F(float.fromhex(x)) for x in row['eigenvalues_hex']];ck(lam==sorted(lam),'eigenvalue order');verify(A,Q,lam,radius,row['certificate']);a=F(row['certificate']['density_lower']);b=F(row['certificate']['density_upper']);lo+=a;hi+=b;width=max(width,b-a);hashes.append(hashlib.sha256(line.encode()).hexdigest());count+=1
 ck(count==1024,'node coverage')
 return dict(job=job,rep=REPS[job//4],nodes=count,freeze=freeze,node_sha=r['node_sha'],producer_receipt_sha=sha(folder/'RESULT.json'),external_receipt_sha=sha(production/f'job{job:02d}.receipt.json'),line_hashes=hashes,density_sum=[str(lo),str(hi)],max_width=str(width),scope='all1024 exactFraction Q/residual/Gram/root replays; no eigensolver')
def aggregate(production,replays,freeze):
 ck(not (production/'FAILURE.json').exists(),'production failure');complete=read(production/'COMPLETE.json');ck(complete['freeze']==freeze,'complete freeze');report=read(production/'ANALYSIS.json');ck(report['freeze']==freeze,'analysis freeze');ck(sorted(p.name for p in replays.glob('job*.json'))==[f'job{j:02d}.json' for j in range(24)],'replay membership');sums={r:[F(0),F(0)] for r in REPS};ledger=[]
 for j in range(24):
  p=replays/f'job{j:02d}.json';v=read(p);ck((v['job'],v['rep'],v['nodes'],v['freeze'])==(j,REPS[j//4],1024,freeze),'replay identity');ck(v['status']=='PASS','replay status');bounded(v['seconds'],170);bounded(v['peak_bytes'],384*1048576);ck(sha(production/f'job{j:02d}'/'NODES.jsonl')==v['node_sha'],'replayed raw');ck(len(v['line_hashes'])==1024,'row hashes');ck(sha(production/f'job{j:02d}'/'RESULT.json')==v['producer_receipt_sha'],'producer receipt unchanged');ck(sha(production/f'job{j:02d}.receipt.json')==v['external_receipt_sha'],'external receipt unchanged');sums[v['rep']][0]+=F(v['density_sum'][0]);sums[v['rep']][1]+=F(v['density_sum'][1]);ledger.append({'job':j,'replay_sha':sha(p),'node_sha':v['node_sha']})
 d={r:(a/4096,b/4096) for r,(a,b) in sums.items()};trig=read(SOURCE/'TRIG_INPUTS.json');cubes=read(SOURCE/'CUBE_INPUTS.json');err=F(3,8192)*F(trig['pi_upper_numerator'],trig['pi_denominator'])**2;ck(F(report['quadrature_difference_radius'])==err,'quadrature');ck((report['grid_n'],report['folded_n'],report['multiplicity'],report['node_count'],report['original_node_count'])==(32,16,8,24576,196608),'grid normalization')
 for r,ab in d.items():ck(list(map(F,report['grid_density_intervals'][str(r)]))==list(ab),'exact density')
 ck(len(report['costs'])==5,'five comparisons');results=[]
 for r,c in zip(REPS[:-1],report['costs']):
  m=cubes['rows'][r]['defects'];a=d[r][0]-d[15][1]-err;b=d[r][1]-d[15][0]+err;ck((c['rep'],c['defects'])==(r,m),'class');expected={'density_lower':a,'density_upper':b,'limiting_delta_lower':8*a/m,'limiting_delta_upper':8*b/m,'auxiliary_defect_coefficient_lower':2*a/m,'native_half_objective_defect_coefficient_lower':a/m}
  for k,v in expected.items():ck(F(c[k])==v,'comparison '+k)
  ck(c['strictly_positive']==(a>0),'sign');results.append({'rep':r,'lower':str(a),'upper':str(b),'positive':a>0})
 ck(report['all_five_positive']==all(x['positive'] for x in results),'all signs');ck(F(report['common_density_lower'])==min(F(x['lower']) for x in results),'common minimum')
 return dict(freeze=freeze,nodes=24576,all_exact_replays=True,comparisons=results,all_five_positive=all(x['positive'] for x in results),replay_ledger=ledger,analysis_sha=sha(production/'ANALYSIS.json'),scope='independent arithmetic/aggregation; campaign external resource acceptance remains separately required')
def main():
 ap=argparse.ArgumentParser();g=ap.add_mutually_exclusive_group(required=True);g.add_argument('--job',type=int);g.add_argument('--aggregate',action='store_true');ap.add_argument('--production',required=True);ap.add_argument('--replays');ap.add_argument('--output',required=True);a=ap.parse_args();start=time.monotonic();signal.alarm(170);out=Path(a.output);ck(not out.exists(),'no output overwrite');freeze=preflight();production=Path(a.production)
 if a.aggregate:ck(a.replays is not None,'replay folder');result=aggregate(production,Path(a.replays),freeze)
 else:result=jobcheck(production,a.job,freeze)
 result.update(status='PASS',seconds=time.monotonic()-start,peak_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss);bounded(result['seconds'],170);bounded(result['peak_bytes'],384*1048576)
 with out.open('x') as file:json.dump(result,file,indent=2);file.write('\n')
if __name__=='__main__':main()
