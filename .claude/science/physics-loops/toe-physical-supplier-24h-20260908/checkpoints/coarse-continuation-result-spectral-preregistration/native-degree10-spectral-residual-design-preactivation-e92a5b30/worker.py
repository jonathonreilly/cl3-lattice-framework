from pathlib import Path
from fractions import Fraction as F
import json,hashlib,time,os,math
import interval as I
import wick,algebra,spectral,posterior

def need(x,m):
 if not x:raise ValueError(m)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for x in iter(lambda:f.read(1048576),b''):h.update(x)
 return h.hexdigest()
def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,(list,tuple)):return[encode(v)for v in x]
 if isinstance(x,dict):return{k:encode(v)for k,v in x.items()}
 return x
def atomic(p,x):
 tmp=p.with_suffix(p.suffix+'.tmp')
 with tmp.open('w')as f:json.dump(encode(x),f,sort_keys=True);f.write('\n');f.flush();os.fsync(f.fileno())
 tmp.replace(p)
def schedule(count):
 from itertools import combinations
 labels=list(combinations(range(6),2));kind=lambda a:'O'if a[0]//2==a[1]//2 else'P'
 local=['vacuum_inputs']+['vacuum_moment_raw']*7+['first_polynomial','source_inputs']+['source_moment_raw']*3+['residual_raw']
 if count==205:local=['moments','polynomial','source_moments','residual_raw']
 elif count!=255:raise ValueError('fixed source count')
 stages=local*2;seen=set()
 for C in labels:
  for A in labels:
   if set(C)&set(A):continue
   kc,ka=kind(C),kind(A);ell=sum((2*k in C and 2*k+1 in A)or(2*k+1 in C and 2*k in A)for k in range(3));tag='PP'+str(ell)if kc==ka=='P'else kc+ka
   if count==255 and tag not in seen:stages.append('cross_wick_raw');seen.add(tag)
   stages.append('ordered_word')
 stages.append('gate_inputs');out=[('binding',None),('scalar_inputs',None)]
 for mode in ['residual','variational']:out += [('choice_start',mode)]+[(s,mode)for s in stages]+[('choice_complete',mode)]
 return out+[('complete',None)]

def load_family(spec,emit):
 def read(k):
  f=spec[k];emit('before_input',{'role':k});need(sha(f['path'])==f['sha256'],'input hash');return json.loads(Path(f['path']).read_text())
 a=read('acceptance');w=read('worker');rr=read('receipt');rf=read('root_freeze');r=read('result')
 need(a['status']==spec['accepted_status']and a['once']is True,'accepted status')
 need(a['result_sha256']==spec['result']['sha256']==w['result_sha256']and a['worker_freeze']==spec['worker_freeze']==w['runtime_sha256']==rr['worker_freeze']==rf['worker_freeze'],'producer chain')
 need(a['root_freeze']==spec['root_freeze']['sha256']and w['status']==spec['worker_status'],'producer freeze')
 need(rr['pass']is True and type(rr['returncode'])is int and rr['returncode']==0,'original completion')
 for v,cap in [(w['seconds'],19),(rr['seconds'],19.5),(a['external_seconds'],20)]:need(type(v)in(int,float)and math.isfinite(v)and 0<v<cap,'original timing')
 for v in [w['rss_bytes'],rr['sampled_whole_tree_peak'],a['external_rss_bytes'],a['sampled_whole_tree_peak']]:need(type(v)is int and 0<v<=384*1048576,'original RSS')
 need(r['status']==spec['result_status']and type(r['events'])is int and r['events']==spec['count']and type(r['choices'])is int and r['choices']==2,'original full completion')
 p=spec['events'];need(sha(p['path'])==p['sha256'],'events hash');ev=[]
 with Path(p['path']).open()as stream:
  for i,line in enumerate(stream,1):
   emit('before_source_event',{'index':i});e=json.loads(line);need(type(e['sequence'])is int and e['sequence']==i,'sequence');ev.append(e)
 need(len(ev)==spec['count'],'event census');need([(e['stage'],e['choice'])for e in ev]==schedule(spec['count']),'exact source chronology');return r,ev

def selected(events,stage,mode,kind=None):
 rows=[e['data']for e in events if e['stage']==stage and e['choice']==mode and(kind is None or e['data'].get('kind')==kind)]
 need(len(rows)==1,'unique '+stage);return rows[0]

def run(b,out):
 start=time.monotonic();seq=0;current={};rows=[];mode=None
 with (out/'EVENTS.ndjson').open('x')as log:
  def emit(stage,data):
   nonlocal seq,current
   seq+=1;current={'sequence':seq,'mode':mode,'stage':stage,'data':encode(data)};log.write(json.dumps(current,sort_keys=True)+'\n');log.flush();os.fsync(log.fileno());atomic(out/'PARTIAL.json',{'current':current,'completed':rows,'seconds':time.monotonic()-start})
  try:
   r10,e10=load_family(b['degree10'],lambda s,d:emit(s,dict(family='degree10',**d)));r20,e20=load_family(b['degree20'],lambda s,d:emit(s,dict(family='degree20',**d)))
   scalar10=selected(e10,'scalar_inputs',None);scalar20=selected(e20,'scalar_inputs',None)
   need(scalar10['c']==scalar20['c']and scalar10['nu']==scalar20['nu'],'unchanged scalar family')
   c,nu,omega=I.box(scalar20['c']),I.box(scalar20['nu']),I.box(scalar20['omega5'])
   for box in [c,nu,omega]:
    need(all(max(abs(x.numerator).bit_length(),x.denominator.bit_length())<=512 for x in box),'scalar512 cap')
   vacuum={}
   for kind in ['P','O']:
    copies=[]
    for md in ['residual','variational']:
     v=[e['data']for e in e20 if e['stage']=='vacuum_moment_raw'and e['choice']==md and e['data'].get('kind')==kind];need(len(v)==7,'seven moments');need(all(type(d['index'])is int and d['index']==j for j,d in enumerate(v)),'moment order');copies.append(v)
    need(copies[0]==copies[1],'same repeated vacuum moments');vacuum[kind]=[]
    for d in copies[0]:
     im=I.box(d['imaginary']);need(im[0]<=0<=im[1],'real vacuum moment');vacuum[kind].append(I.nonnegative(I.box(d['real'])))
   emit('inherited_vacuum_moments',vacuum)
   for mode in ['residual','variational']:
    try:
     gate=selected(e10,'gate_inputs',mode);original=next(x for x in r10['rows']if x['mode']==mode);need(gate['nominal']==original['nominal'],'unchanged nominal');bounds={};s0={};qs={}
     for kind in ['P','O']:
      p=selected(e10,'polynomial',mode,kind);raw=selected(e10,'residual_raw',mode,kind);old=selected(e10,'source_moments',mode,kind);p0,p1,q=I.parse(p['p0']),I.parse(p['p1']),I.parse(raw['q']);need(raw['q']==gate['rows'][kind]['q'],'q gate binding');s0[kind]=old['s0'];qs[kind]=raw['q']
      emit('fixed_original_coefficients',{'kind':kind,'p0':p0,'p1':p1,'q':q,'s0_s2':old})
      G=wick.table(c,nu,omega,kind);source=wick.sources(p0,I.check(4*p1));mean,inner,counts=algebra.evaluator(G);emit('new_source_table',{'kind':kind,'G':G,'Db':source[1],'D2b':source[2]});s=[I.nonnegative(I.box(old['s'+str(i)]))for i in range(3)]
      for index,x,y in [(3,source[1],source[2]),(4,source[2],source[2])]:
       z=inner(x,y);emit('NEW_source_moment_raw',{'kind':kind,'index':index,'real':z[0],'imaginary':z[1],'counts':counts()});s.append(algebra.real_moment(z))
      fun=lambda st,d:emit(st,dict(kind=kind,**d));rho=spectral.first_moments(vacuum[kind],p0,p1,fun);xi=spectral.inner_moments(s,q,fun);u2=spectral.inverse_squared(rho,lambda st,d:fun('first_'+st,d));v2=spectral.inverse_squared(xi,lambda st,d:fun('inner_'+st,d));bounds[kind]=(u2,v2);emit('selected_norm_bounds',{'kind':kind,'u2':u2,'v2':v2})
     ef=spectral.combined(bounds,emit);newgate=dict(gate,E=encode(ef['E']),F=encode(ef['F']));emit('new_gate_inputs',{'old_E':gate['E'],'old_F':gate['F'],'new':newgate});ans=posterior.evaluate(s0,qs,newgate,emit);ans['mode']=mode;ans['new_moments']=4
    except (ValueError,ZeroDivisionError)as e:ans={'mode':mode,'status':'INDETERMINATE_ARITHMETIC','error':repr(e),'stage':current['stage']}
    atomic(out/(mode+'.json'),ans);rows.append(encode(ans));emit('choice_complete',ans)
   need(not {x['status']for x in rows}>={'POSITIVE_CERTIFICATE','NEGATIVE_CERTIFICATE'},'contradictory signs');mode=None;result={'status':'COMPLETE_NEW_SPECTRAL_RESIDUAL_ESTIMATOR','rows':rows,'choices':2,'native_oracle_calls':0,'vacuum_moments_recomputed':0,'s0_s2_recomputed':0,'max_new_source_moments':8,'seconds':time.monotonic()-start};emit('complete',{'rows':rows});result['events']=seq;result['seconds']=time.monotonic()-start;atomic(out/'RESULT.json',result)
  except BaseException as e:
   try:atomic(out/'FAILURE.json',{'error':repr(e),'current':current,'rows':rows})
   except BaseException as er:e.add_note('retention '+repr(er))
   raise
