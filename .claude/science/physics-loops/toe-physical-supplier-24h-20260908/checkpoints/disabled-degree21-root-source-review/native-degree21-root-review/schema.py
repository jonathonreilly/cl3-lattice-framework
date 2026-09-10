"""Exact rounding-order reconciliation, never interval-overlap acceptance."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,math
import independent as I
import tables as T
import assembly as A
import binder
import prior

def need(x,m):
 if not x:raise ValueError(m)
def encode(x):
 if type(x)is F:return str(x)
 if isinstance(x,(tuple,list)):return[encode(v)for v in x]
 if isinstance(x,dict):return{str(k):encode(v)for k,v in x.items()}
 return x
def canon(x):
 if type(x)is bool:return('bool',x)
 if type(x)is int:return('int',x)
 if isinstance(x,(tuple,list)):return tuple(canon(v)for v in x)
 if isinstance(x,dict):return tuple(sorted((str(k),canon(v))for k,v in x.items()))
 return x
def eq(x,y,m):need(canon(x)==canon(encode(y)),m)
def matrix(v,rank):return[[rank*p+i,rank*q+j,z]for(p,i,q,j),z in sorted(v.items(),key=lambda x:(rank*x[0][0]+x[0][1],rank*x[0][2]+x[0][3]))]
def replay(inputs,original,stream,read_file,progress=lambda _:None):
 rad,modes=inputs;sequence=0;mode=None;jet=None;counts={};rows=[]
 def take(stage,data):
  nonlocal sequence
  sequence+=1;progress({'stage':stage,'sequence':sequence});ev=next(stream);eq(ev,{'sequence':sequence,'choice':mode,'jet':jet,'stage':stage,'data':data},'event '+stage)
 take('before_bound_inputs',{'families':['degree20','posterior20','high']});take('authenticated_same_trial_inputs',original);take('authenticated_degree21_inputs',{'radials':rad,'modes':modes})
 inn={};nom={}
 for typ,meta in [('inner',k)for k in ['P','O']]+[('nominal',(a,b,o))for a,b,o,_ in T.SIGS]:
  rank=3 if typ=='inner'else 4;limit=6 if typ=='inner'else 4;mask,factors=T.factors(typ)
  if typ=='inner':jet='inner_'+meta;D,B=T.build(lambda n:rad[n],typ,right=meta);start={'profile':'inner21','source_width':rank,'mask':list(mask)}
  else:
   left,right,o=meta;jet='nominal_'+left+right+'_'+str(o);D,B=T.build(lambda n:rad[n],typ,left,right,o);start={'profile':'nominal21','source_width':rank,'mask':list(mask),'signature':list(meta)}
  start.update(D={n:[[D(n,i,j)for j in range(rank)]for i in range(rank)]for n in range(limit+1)},B={n:[[B(n,i,j)for j in range(rank)]for i in range(rank)]for n in range(limit+1)});take('jet_start',start)
  def emit(stage,data):
   d=dict(data)
   for key in['A','Q','matrix']:
    if key in d:d[key]=matrix(d[key],rank)
   take(stage,d)
  Z=I.reconstruct(mask,factors,T.defects(typ),D,B,emit);stored=read_file(jet+'.json');eq(stored['coefficients'],[[list(k),v]for k,v in Z.items()],'jet result coefficients');c=stored['counts'];need(set(c)=={'complex_products'},'counter keys');need(type(c['complex_products'])is int and 0<=c['complex_products']<=100000000,'counter cap');counts[jet]=c;take('jet_complete',{'counts':c})
  if typ=='inner':inn[meta]=Z
  else:nom[meta]=Z
 jet=None
 for mode in['residual','variational']:
  take('choice_start',{'mode':mode});r=modes[mode];trial={}
  for kind in['P','O']:
   def emit(s,d):take(s,dict(d,kind=kind))
   ss=A.inner(inn[kind],r['p'][kind],r['s0_s2'][kind],emit);trial[kind]=A.choose(ss,r['old_q'][kind],emit)
  ans=A.finish(r['p'],trial,nom,r['first_squared'],r['a_squared'],r['old_alpha'],take);ans['mode']=mode;eq(read_file(mode+'.json'),ans,'mode result');rows.append(ans);take('choice_complete',ans)
 mode=None;take('complete',{'rows':rows})
 try:next(stream)
 except StopIteration:pass
 else:raise ValueError('trailing event')
 return rows,counts,sequence

def check(out,rf,elapsed,progress=lambda _:None):
 out=Path(out);worker=Path(rf['worker_directory']);binding=json.loads((worker/'BINDING.json').read_text());names={'STARTED.json','WORKER_COMPLETE.json','INPUTS.json','EVENTS.ndjson','PARTIAL.json','RESULT.json','residual.json','variational.json','inner_P.json','inner_O.json'}|{'nominal_'+a+b+'_'+str(o)+'.json'for a,b,o,_ in T.SIGS}
 def census():need({p.name for p in out.iterdir()}==names and all(p.is_file()for p in out.iterdir()),'15 regular files')
 census();hashes={n:prior.sha(out/n)for n in names};read=lambda n:json.loads((out/n).read_text());done=read('WORKER_COMPLETE.json');result=read('RESULT.json');partial=read('PARTIAL.json');auth={'runtime_sha256':rf['worker_freeze'],'binding_sha256':prior.sha(worker/'BINDING.json'),'output':str(out.resolve()),'no_retry':True};eq(read('STARTED.json'),auth,'start');need(done['status']=='COMPLETE_NEW_DEGREE21_ONLY','worker completion');need(done['runtime_sha256']==rf['worker_freeze']and done['binding_sha256']==auth['binding_sha256']and done['result_sha256']==hashes['RESULT.json'],'worker identity')
 inputs=binder.load(binding);eq(read('INPUTS.json'),{'radials':inputs[0],'modes':inputs[1]},'bound input');original=prior.source_packet(binder.read(binding['quartic']['binding']))
 with(out/'EVENTS.ndjson').open()as f:
  def records():
   for line in f:
    need(len(line.encode())<=4*1048576,'event size');yield json.loads(line)
  rows,counts,n=replay(inputs,original,records(),read,progress)
 eq(result['rows'],rows,'final rows');eq(result['counts'],counts,'counter copies');need(type(result['events'])is int and result['events']==n and 2386<=n<=2390,'event census');need(type(result['choices'])is int and result['choices']==2 and type(result['jets'])is int and result['jets']==7,'result census')
 for k in['native_oracle_calls','old_native_moments_recomputed']:need(type(result[k])is int and result[k]==0,'no native replay')
 need(result['status']=='COMPLETE_NEW_DEGREE21_JET_CERTIFICATE','result status');need(result['serialized_event_bytes']==(out/'EVENTS.ndjson').stat().st_size,'retained bytes');need(partial['completed']==2 and partial['current']=={'sequence':n,'choice':None,'jet':None,'stage':'complete'},'final partial')
 for v in[partial['seconds'],result['seconds'],done['seconds']]:need(type(v)in(int,float)and math.isfinite(v)and 0<v<rf['worker_seconds'],'time')
 need(partial['seconds']<=result['seconds']<=done['seconds']<=elapsed<rf['root_seconds'],'time order');need(type(done['rss_bytes'])is int and 0<done['rss_bytes']<=384*1048576,'workerRSS')
 for n,h in hashes.items():need(prior.sha(out/n)==h,'final byte hash')
 census();return{'status':'PASS_INDEPENDENT_DEGREE21_ARITHMETIC','rows':2,'events':result['events'],'output_hashes':hashes,'result_sha256':hashes['RESULT.json'],'native_replay':False,'rounding_policy':'exact endpoint equality'}
