"""Independent saved-input mapping and quartic certificate arithmetic."""
from pathlib import Path
from fractions import Fraction as F
import json,math,hashlib
import independent as I
P=Path(__file__).resolve().parent.parent/'native-quartic-spectral-estimator-design'
def need(x,m):
 if not x:raise ValueError(m)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for c in iter(lambda:f.read(1048576),b''):h.update(c)
 return h.hexdigest()
def norm(x):
 if type(x)is F:return str(x)
 if type(x)is bool:return('BOOL',x)
 if type(x)is int:return('INT',x)
 if isinstance(x,(list,tuple)):return tuple(norm(v)for v in x)
 if isinstance(x,dict):return tuple(sorted((str(k),norm(v))for k,v in x.items()))
 return x
def eq(x,y,m):need(norm(x)==norm(y),m)
def rat(x):
 need(type(x)is str and len(x)<=20000,'scalar string');v=I.guard(F(x));need(str(v)==x,'canonical');return v
def box(x):
 need(type(x)is list and len(x)==2,'box');a,b=map(rat,x);need(a<=b,'order');return a,b
def source_packet(b):
 def read(spec,lines=False):
  need(sha(spec['path'])==spec['sha256'],'input hash');text=Path(spec['path']).read_text();return[json.loads(x)for x in text.splitlines()]if lines else json.loads(text)
 ev=read(b['degree20']['files']['events'],True);need(len(ev)==255,'source255')
 for i,e in enumerate(ev,1):need(type(e['sequence'])is int and e['sequence']==i,'source sequence')
 high=read(b['high']['files']['result']);post=read(b['posterior20']['files']['result']);old=read(b['degree20']['files']['result']);tables=read(b['high']['tables']);hm={r['kind']:r for r in high['rows']}
 def select(stage,mode,kind=None):
  a=[e['data']for e in ev if e['stage']==stage and e['choice']==mode and(kind is None or e['data'].get('kind')==kind)];need(len(a)==1,'unique '+stage);return a[0]
 moments={}
 for kind in['P','O']:
  copies=[]
  for mode in['residual','variational']:copies.append([e['data']for e in ev if e['stage']=='vacuum_moment_raw'and e['choice']==mode and e['data'].get('kind')==kind])
  eq(copies[0],copies[1],'same lower moments');need(len(copies[0])==7,'seven lower');m=[]
  for j,r in enumerate(copies[0]):
   eq(r['index'],j,'index');v=box(r['real']);im=box(r['imaginary']);need(im[0]<=0<=im[1],'reality');m.append(v);Q=1<<256;lo=v[0].numerator*Q//v[0].denominator;hi=-((-v[1].numerator*Q)//v[1].denominator);eq(tables['classes'][kind]['accepted_m'][str(j)],[[lo,hi],[0,0]],'high lower mapping')
  eq(hm[kind]['orders'],[7,8,9,10],'high orders')
  for j in range(7,11):
   v=hm[kind]['moments'][str(j)];need(type(v)is list and len(v)==2,'high box')
   for z in v:need(type(z)is list and len(z)==2 and all(type(x)is int and abs(x).bit_length()<=4096 for x in z)and z[0]<=z[1],'high endpoints')
   need(v[1][0]<=0<=v[1][1],'high reality');m.append((F(v[0][0],1<<256),F(v[0][1],1<<256)))
  moments[kind]=m
 out={}
 for index,mode in enumerate(['residual','variational']):
  gate=select('gate_inputs',mode);prior=post['rows'][index];eq(prior['mode'],mode,'prior mode');eq(prior['nominal'],gate['nominal'],'nominal');eq(old['rows'][index]['nominal'],gate['nominal'],'original nominal');rows={}
  for kind in['P','O']:
   pol=select('first_polynomial',mode,kind)['coefficients'];r=select('residual_raw',mode,kind);g=gate['rows'][kind];eq(pol,g['p'],'same p');eq(r['q'],g['q'],'same q');eq(r['r2'],g['r2'],'same r2');eq(r['t2'],g['t2'],'same t2');v=box(r['r2']);rows[kind]={'moments':moments[kind],'p':list(map(rat,pol)),'r2':v,'t2':box(r['t2']),'old_first_squared_upper':I.guard(16*v[1])}
  out[mode]={'rows':rows,'nominal':box(gate['nominal']),'old_alpha':box(prior['alpha_interval']),'trial_a2':(rat(prior['a_squared_upper']),)*2,'trial_b2':(rat(prior['b_squared_upper']),)*2}
 return out

def reconcile(packet,events,result,expected,progress=lambda _:None):
 eq(packet,expected,'authenticated packet');pos=0
 def take(stage,data,mode):
  nonlocal pos
  need(pos<len(events),'missing event');e=events[pos];pos+=1;eq(e,{'sequence':pos,'choice':mode,'stage':stage,'data':data},'exact event '+stage);progress({'stage':stage,'sequence':pos})
 take('before_bound_inputs',{'families':['degree20','posterior20','high']},None);take('authenticated_same_trial_inputs',expected,None);rows=[]
 for mode in['residual','variational']:
  take('choice_start',{'mode':mode},mode);p=expected[mode];ans=I.evaluate(p['rows'],p['nominal'],p['old_alpha'],p['trial_a2'],p['trial_b2'],lambda s,d:take(s,d,mode));ans['mode']=mode;rows.append(ans);take('choice_complete',ans,mode)
 take('complete',{'rows':rows},None);need(pos==len(events),'no trailing');eq(result['rows'],rows,'result rows');eq(result['choices'],2,'choices');eq(result['events'],pos,'events');eq(result['new_residual_moment_terms'],112,'rho terms');eq(result['majorant_candidates'],60,'candidate count')
 for k in['native_oracle_calls','native_moments_recomputed','old_trials_recomputed']:eq(result[k],0,'no replay')
 need(result['status']=='COMPLETE_NEW_QUARTIC_SPECTRAL_ESTIMATOR','status');return rows

def check(out,rf,elapsed,progress=lambda _:None):
 out=Path(out);names={'STARTED.json','WORKER_COMPLETE.json','RESULT.json','EVENTS.ndjson','PARTIAL.json','INPUTS.json','residual.json','variational.json'}
 def census():need({p.name for p in out.iterdir()}==names and all(p.is_file()for p in out.iterdir()),'exact eight regular files')
 census();raw={n:(out/n).read_bytes()for n in names};load=lambda n:json.loads(raw[n]);done=load('WORKER_COMPLETE.json');result=load('RESULT.json');part=load('PARTIAL.json');events=[json.loads(x)for x in raw['EVENTS.ndjson'].splitlines()];auth={'runtime_sha256':rf['worker_freeze'],'binding_sha256':sha(P/'BINDING.json'),'output':str(out.resolve()),'no_retry':True};eq(load('STARTED.json'),auth,'started');eq(done['runtime_sha256'],rf['worker_freeze'],'worker');eq(done['binding_sha256'],auth['binding_sha256'],'binding');eq(done['result_sha256'],hashlib.sha256(raw['RESULT.json']).hexdigest(),'result hash');need(done['status']=='COMPLETE_NEW_QUARTIC_ONLY','completion')
 for x in[done['seconds'],result['seconds'],part['seconds']]:need(type(x)in(int,float)and math.isfinite(x)and 0<x<29,'time')
 need(part['seconds']<=result['seconds']<=done['seconds']<=elapsed<29.5,'time order');need(type(done['rss_bytes'])is int and 0<done['rss_bytes']<=384*1048576,'RSS');eq(part['current'],events[-1],'finalpartial');eq(part['completed'],2,'completed');expected=source_packet(json.loads((P/'BINDING.json').read_text()));rows=reconcile(load('INPUTS.json'),events,result,expected,progress)
 for mode,row in zip(['residual','variational'],rows):eq(load(mode+'.json'),row,'modecopy')
 hashes={n:hashlib.sha256(v).hexdigest()for n,v in raw.items()}
 for n,h in hashes.items():need(sha(out/n)==h,'final output hash')
 census();return {'status':'PASS_INDEPENDENT_QUARTIC_ARITHMETIC','count':2,'events':len(events),'result_sha256':hashes['RESULT.json'],'output_hashes':hashes,'native_moment_replay':False,'quartic_arithmetic_reconciled':True}
