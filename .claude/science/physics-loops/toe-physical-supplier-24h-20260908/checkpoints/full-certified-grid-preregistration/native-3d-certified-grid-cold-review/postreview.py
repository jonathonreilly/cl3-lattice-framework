"""Frozen-before-data exact96 replay; no author imports/eigensolves."""
from pathlib import Path
import json,hashlib,sys,math
from itertools import product
from fractions import Fraction as F
from independent import matrix,verify,ck
HERE=Path(__file__).resolve().parent;BASE=HERE.parent;B=BASE/'native-3d-certified-grid-design';ROOT=BASE/'native-3d-certified-cost-root-review'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def timing(text):
 lines=text.splitlines();r=[int(s.split()[0]) for s in lines if 'maximum resident set size' in s];t=[float(s.split()[1]) for s in lines if len(s.split())==2 and s.split()[0]=='real'];ck(len(r)==len(t)==1,'shell schema');ck(0<r[0]<=384*1048576 and 0<t[0]<=30,'shell caps');return t[0]
def main():
 pin=read(HERE/'PRODUCER_PIN.json');ck(sha(B/'FREEZE.json')==pin['freeze'],'freeze')
 for p,h in read(B/'FREEZE.json')['files'].items():
  p=Path(p);p=p if p.is_absolute() else B/p;ck(sha(p)==h,'source pin')
 for p,h in read(B/'RUNTIME.json')['files'].items():ck(sha(Path(p))==h,'runtime')
 cost=read(B/'COST_RESULT.json');ck(cost['freeze']==pin['freeze'],'cost freeze');ck(sha(B/'CANDIDATES.jsonl')==cost['candidate_sha'],'candidate hash')
 raw=[json.loads(x) for x in (B/'CANDIDATES.jsonl').read_text().splitlines()];expected=[(r,tuple(j)) for r in pin['representatives'] for j in product(*pin['index_sets'])];ck(len(raw)==len(cost['rows'])==len(expected)==96,'coverage')
 cubes=read(B/'CUBE_INPUTS.json');trig=read(B/'TRIG_INPUTS.json');ck(trig['grid_n']==32 and [r['j'] for r in trig['rows']]==list(range(32)),'trig ledger');widths=[];times=[];details=[]
 for row,time,identity in zip(raw,cost['rows'],expected):
  ck((row['rep'],tuple(row['index']))==identity==(time['rep'],tuple(time['index'])),'node ledger')
  A,radius=matrix(cubes['rows'][row['rep']],[trig['rows'][j] for j in row['index']]);ck(len(row['vectors_hex'])==16 and all(len(x)==16 for x in row['vectors_hex']),'Q shape')
  Q=[[(F(float.fromhex(re)),F(float.fromhex(im))) for re,im in line] for line in row['vectors_hex']];lam=[F(float.fromhex(x)) for x in row['eigenvalues_hex']];v=verify(A,Q,lam,radius,row['certificate']);widths.append(F(v['density_width']));details.append({'rep':row['rep'],'index':row['index'],**v})
  ts=[time[k] for k in ('build_seconds','eigh_seconds','certificate_seconds','serialization_seconds')];ck(all(type(x) in (int,float) and math.isfinite(x) and x>0 for x in ts),'timers');times.append(sum(ts))
 outer=read(ROOT/'OUTER.json');ck(outer['freeze']==pin['freeze'] and outer['returncode']==0 and outer['watchdog_failure'] is None and outer['provisional_resource_accept'] is True,'outer status');ck(0<outer['seconds']<30 and 0<outer['observed_peak_whole_tree_bytes']<=384*1048576,'tree caps');external=timing((ROOT/'SHELL.stderr').read_text());ck(0<cost['internal_seconds']<=28 and 0<cost['peak_bytes']<=384*1048576,'internal resources');ck(sum(times)<=external,'full accounting')
 overhead=external-sum(times);perjob=2*(1024*max(times)+overhead);total=pin['jobs']*perjob+external+60
 return {'status':'PASS','freeze':pin['freeze'],'nodes':96,'all_exact_certificates_checked':True,'max_density_interval_width':str(max(widths)),'external_seconds':external,'forecast_job':perjob,'forecast_aggregate':total,'forecast_gate':perjob<=150 and total<=2880,'scope':'cost/arithmetic only, no density grid integral','details':details}
if __name__=='__main__':
 ck(len(sys.argv)==1,'no arguments');print(json.dumps(main(),indent=2))
