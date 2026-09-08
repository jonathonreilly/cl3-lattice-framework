"""Predata frozen replay. Never imports author code or executes sampler."""
from pathlib import Path
import sys,json,hashlib,math,re
from literal import *
BASE=Path(__file__).resolve().parent.parent;C=BASE/'continuous-time-l4-cost-profile';ROOT=BASE/'continuous-time-l4-cost-root-review';FREEZE='36551b8d91eccf89e658351a1db4f73efe600f0653a4c4ff473615cdc7f5e31d'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def close(a,b):require(math.isfinite(a) and math.isfinite(b) and abs(a-b)<=1e-10*max(1,abs(a),abs(b)),'numeric mismatch')
def pos(x):require(type(x) in (int,float) and math.isfinite(x) and x>0,'timing');return x
def receipt(text):
 lines=text.splitlines();rr=[int(s.split()[0]) for s in lines if 'maximum resident set size' in s];tt=[float(s.split()[0]) for s in lines if len(s.split())==2 and s.split()[1]=='real']
 require(len(rr)==len(tt)==1,'time receipt');require(0<rr[0]<=384*1048576 and 0<tt[0]<=30,'external caps');return tt[0]
def main(out):
 require(sha(C/'FREEZE.json')==FREEZE,'freeze');f=load(C/'FREEZE.json')
 require(sorted(p.name for p in C.glob('*.py'))==f['python_membership'],'membership')
 for p,h in f['files'].items():require(sha(C/p)==h,'source '+p)
 for p,h in load(C/'RUNTIME.json')['files'].items():require(sha(Path(p))==h,'runtime')
 for p,h in load(C/'SOURCE_BINDINGS.json').items():require(sha(Path(p))==h,'parent binding')
 require(not (out/'FAILURE.json').exists(),'failure marker')
 for name,key in [('WORKER_RECEIPT.json','artifacts'),('DISPATCH.json','files')]:
  z=load(out/name);require(z['freeze']==FREEZE,'receipt freeze')
  for p,h in z[key].items():require(Path(p).name==p and sha(out/p)==h,'output binding')
 d=load(out/'DISPATCH.json');require(0<d['internal_seconds']<=29 and 0<d['parent_peak_bytes']<=384*1048576 and 0<d['worker_peak_bytes']<=384*1048576,'dispatch cap')
 outer=load(ROOT/'OUTER.json');require(outer['freeze']==FREEZE and outer['returncode']==0 and outer['watchdog_failure'] is None and outer['provisional_resource_accept'] is True and outer['dispatch_complete'] and not outer['failure_marker'],'outer status');require(0<outer['seconds']<30 and 0<outer['observed_peak_whole_tree_bytes']<=384*1048576,'outer caps')
 receipt((out/'worker.time.stderr').read_text());elapsed=receipt(Path(str(out)+'.outer-time.txt').read_text())
 r=load(out/'RESULT.json');require(r['names']==list(NAMES) and len(r['cases'])==4,'cases');bs=[];ms=[];inis=[];ios=[];sysizes=[];accounted=0
 for i,c in enumerate(r['cases']):
  require((c['cid'],c['T'],c['start'],c['seed'])==(i,(.5,.5,2.,2.)[i],('constant','propagated','constant','propagated')[i],202609420000+i),'case')
  require([b['face'] for b in c['blocks']]==[0,64,128,191],'blocks');require(len(c['measurements'])==len(c['postblock_paths'])==len(c['postblock_io_seconds'])==len(c['measurement_seconds'])==4,'coverage')
  init=c['initialization'];require(init['rk_sweeps']==(0 if i%2==0 else 128) and init['rk_proposals']==(0 if i%2==0 else 24576),'initialization')
  require(type(init['clock_draws']) is int and 0<=init['clock_draws']<=4096 and type(init['physical_events']) is int and 0<=init['physical_events']<=init['clock_draws'],'initializer counts')
  for j,p in enumerate(c['postblock_paths']):
   require(p['file']==f'path{i}_block{j}.json' and sha(out/p['file'])==p['sha'],'path binding');z=load(out/p['file']);require(float.fromhex(z['T'])==c['T'],'path time');v=measure(z);require(set(c['measurements'][j])==set(NAMES),'readouts')
   for k in NAMES:close(v[k],c['measurements'][j][k])
  final=load(out/f'path{i}.json');require(final==z and c['events']==len(z['events']) and c['witness_length']==len(z['witness']),'final duplicate')
  sy=load(out/f'synthetic{i}.json');rows=[[v[k] for k in NAMES] for v in c['measurements']]*32;require(sy['rows']==rows and sy['path_sha']==sha(out/f'path{i}.json') and sy['face_histogram']==[128]*192 and sy['numerical_failures']==0,'synthetic');require(len(sy['batches'])==16,'batches')
  for b in range(16):
   for k in range(15):close(sy['batches'][b][k],sum(row[k] for row in rows[8*b:8*b+8])/8)
  b=[pos(x['seconds']) for x in c['blocks']];m=[pos(x) for x in c['measurement_seconds']];ini=pos(c['initialization_seconds']);io=pos(c['io_seconds']);s=pos(c['synthetic_output_seconds']);close(io,pos(c['final_io_seconds'])+sum(pos(x) for x in c['postblock_io_seconds']));total=sum(b+m)+ini+io+s;require(total<=pos(c['case_seconds'])+1e-8,'nesting');accounted+=total;bs+=b;ms+=m;inis.append(ini);ios.append(io);sysizes.append(s)
 require(accounted<=30,'accounting');over=30-accounted;chains=[2*(192*(burn+128)*max(bs)+128*max(ms)+max(inis)+max(ios)+max(sysizes)+over) for burn in (16,64,16,64)];total=16*sum(chains)+90;f=load(out/'FORECAST.json')
 for i,x in enumerate(chains):close(f['arms'][i]['per_chain'],x)
 close(f['aggregate'],total);close(f['max_chain'],max(chains));close(f['unallocated_charged_each_chain'],over);require(f['forecast_gate']==(total<=2880 and max(chains)<=150),'gate');require(f['charged_profile_seconds']==30,'charge')
 return {'status':'PASS','freeze':FREEZE,'physical_paths':16,'readouts':240,'synthetic_rows':512,'forecast_gate':f['forecast_gate'],'forecast_total':total,'shell_seconds':elapsed,'scope':'cost validation only; no mixing evidence'}
if __name__=='__main__':
 require(len(sys.argv)==2,'one output directory');print(json.dumps(main(Path(sys.argv[1])),indent=2))
