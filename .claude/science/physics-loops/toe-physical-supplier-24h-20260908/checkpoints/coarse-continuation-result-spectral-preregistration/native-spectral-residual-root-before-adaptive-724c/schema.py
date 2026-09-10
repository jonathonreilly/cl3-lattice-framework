from pathlib import Path
from fractions import Fraction as F
from math import isqrt,isfinite
import json,re,hashlib

def req(x,m):
 if not x:raise ValueError(m)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def rat(x):
 req(type(x)is str and len(x)<=20000 and re.fullmatch(r'-?\d+(?:/\d+)?',x)is not None,'rational syntax');q=F(x);req(str(q)==x and max(abs(q.numerator).bit_length(),q.denominator.bit_length())<=32768,'rational cap');return q
def box(x):
 req(type(x)is list and len(x)==2,'box shape');a,b=map(rat,x);req(a<=b,'box order');return a,b
def upperroot(q):
 req(q>=0,'nonnegative root');u=1<<256;a,r=divmod(q.numerator*u*u,q.denominator);k=isqrt(a)
 if k*k!=a or r:k+=1
 return F(k,u)
def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,(list,tuple)):return[enc(v)for v in x]
 if isinstance(x,dict):return{k:enc(v)for k,v in x.items()}
 return x
def same(a,b):return json.dumps(a,sort_keys=True)==json.dumps(b,sort_keys=True)
def calculate(s,mode):
 p,o=box(s['s0']['P']),box(s['s0']['O']);qp,qo=rat(s['q']['P']),rat(s['q']['O']);req(min(p[1],o[1])>=0,'norm upper');aa=(12*p[1]+3*o[1])/8;bb=12*qp*qp*p[1]+3*qo*qo*o[1];a,b=upperroot(aa),upperroot(bb);g=s['gate'];EE,FF=box(g['E']),box(g['F']);req(EE[0]>=0 and FF[0]>=0,'residual sign');E,Verr=EE[1],FF[1];X=4*upperroot(F(15));V=32*upperroot(F(30));chi=min(X,a+E);psi=min(V,b+Verr);qterm=E*(a+chi);mix=[E*b+chi*Verr,E*psi+a*Verr];error=6*(qterm+min(mix));nom=box(g['nominal']);alpha=((nom[0]-error)/8,(nom[1]+error)/8)
 r={'a_squared_upper':aa,'b_squared_upper':bb,'a_upper':a,'b_upper':b,'E_upper':E,'F_upper':Verr,'X_upper':X,'V_upper':V,'chi_upper':chi,'psi_upper':psi,'quadratic_term':qterm,'mixed_bounds':mix,'error_upper':error,'nominal':nom,'alpha_interval':alpha,'status':'POSITIVE_CERTIFICATE'if alpha[0]>0 else('NEGATIVE_CERTIFICATE'if alpha[1]<0 else'INDETERMINATE_SIGN'),'mode':mode}
 out=enc(r)
 # Validate all emitted rational operands through independent bounded parser.
 for k,v in out.items():
  if k in ['status','mode']:continue
  if type(v)is list:
   for x in v:rat(x)
  else:rat(v)
 return out

def pt(x):return(F(x),F(x))
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def scale(a,q):return(min(a[0]*q,a[1]*q),max(a[0]*q,a[1]*q))
def mul(a,b):
 v=[x*y for x in a for y in b];return min(v),max(v)
def root128(a):
 req(a[0]>=0,'root128 positive');S=1<<128;out=[]
 for i,q in enumerate(a):
  x,r=divmod(q.numerator*S*S,q.denominator);k=isqrt(x)
  if i and(k*k!=x or r):k+=1
  out.append(F(k,S))
 return tuple(out)
def nonnegative(a):req(a[1]>=0,'negative norm upper');return max(F(0),a[0]),a[1]
def selected(ev,st,mode,kind=None):
 v=[e['data']for e in ev if e['stage']==st and e['choice']==mode and(kind is None or e['data'].get('kind')==kind)];req(len(v)==1,'unique inherited stage');return v[0]
def check(O,rf,elapsed,progress):
 O=Path(O);read=lambda p:json.loads(Path(p).read_text());r=read(O/'RESULT.json');done=read(O/'WORKER_COMPLETE.json');part=read(O/'PARTIAL.json');wp=Path(rf['worker_path']);b=read(wp/'BINDING.json')
 req(set(x.name for x in O.iterdir())=={'STARTED.json','RESULT.json','PARTIAL.json','WORKER_COMPLETE.json','EVENTS.ndjson','residual.json','variational.json'},'output census')
 req(done['status']=='COMPLETE_NEW_SPECTRAL_RESIDUAL_ONLY'and done['runtime_sha256']==rf['worker_freeze']and done['binding_sha256']==sha(wp/'BINDING.json')and done['result_sha256']==sha(O/'RESULT.json'),'completion')
 req(same(read(O/'STARTED.json'),read(Path(__file__).parent/'WORKER_AUTHORIZATION.json')),'start auth')
 for x in [elapsed,r['seconds'],done['seconds'],part['seconds']]:req(type(x)in(int,float)and isfinite(x)and x>0,'time type')
 req(part['seconds']<=r['seconds']<=done['seconds']<29 and done['seconds']<=elapsed<29.5,'time order');req(type(done['rss_bytes'])is int and 0<done['rss_bytes']<=384*1048576,'RSS')
 req(r['status']=='COMPLETE_NEW_SPECTRAL_RESIDUAL_ESTIMATOR'and type(r['choices'])is int and r['choices']==2 and len(r['rows'])==2,'result')
 for k,v in [('native_oracle_calls',0),('vacuum_moments_recomputed',0),('s0_s2_recomputed',0),('max_new_source_moments',8)]:req(type(r[k])is int and r[k]==v,'new scope')
 ev=[json.loads(x)for x in(O/'EVENTS.ndjson').read_text().splitlines()];req(type(r['events'])is int and r['events']==len(ev)and 474<=len(ev)<=572,'event length')
 for j,e in enumerate(ev):req(type(e['sequence'])is int and e['sequence']==j+1 and set(e)=={'sequence','mode','stage','data'},'event shape')
 idx=0
 def take(st,mode):
  nonlocal idx
  req(idx<len(ev),'event missing');e=ev[idx];idx+=1;req(e['stage']==st and e['mode']==mode,'stage order '+st);return e['data']
 source={}
 for family,count in [('degree10',205),('degree20',255)]:
  spec=b[family]
  for role in ['acceptance','worker','receipt','root_freeze','result']:req(same(take('before_input',None),{'family':family,'role':role}),'input role')
  for j in range(1,count+1):req(same(take('before_source_event',None),{'family':family,'index':j}),'source event census')
  f=spec['events'];req(sha(f['path'])==f['sha256'],'source event hash');v=[json.loads(x)for x in Path(f['path']).read_text().splitlines()];req(len(v)==count and all(type(e['sequence'])is int and e['sequence']==j+1 for j,e in enumerate(v)),'bound original sequence');source[family]=v
 e10,e20=source['degree10'],source['degree20'];vac={}
 for kind in ['P','O']:
  copies=[[e['data']for e in e20 if e['stage']=='vacuum_moment_raw'and e['choice']==mode and e['data'].get('kind')==kind]for mode in ['residual','variational']];req(len(copies[0])==7 and same(*copies),'vacuum copies');vac[kind]=[]
  for j,d in enumerate(copies[0]):req(type(d['index'])is int and d['index']==j and box(d['imaginary'])[0]<=0<=box(d['imaginary'])[1],'vacuum index/reality');vac[kind].append(nonnegative(box(d['real'])))
 req(same(take('inherited_vacuum_moments',None),enc(vac)),'vacuum reuse')
 rows=[]
 local=['fixed_original_coefficients','new_source_table']+['NEW_source_moment_raw']*2+['first_residual_moment']*3+['inner_residual_moment']*3+['first_gap_bound']+['first_majorant']*5+['inner_gap_bound']+['inner_majorant']*5+['selected_norm_bounds']
 for mode,row in zip(['residual','variational'],r['rows']):
  req(row['mode']==mode and same(row,read(O/(mode+'.json'))),'row copy')
  start=idx;stop=idx
  while stop<len(ev)and ev[stop]['stage']!='choice_complete':stop+=1
  req(stop<len(ev),'choice complete missing');body=ev[idx:stop];expected=local*2+['new_residual_norms','new_gate_inputs','trial_norms'];req([e['stage']for e in body]==expected[:len(body)]and all(e['mode']==mode for e in body),'body grammar')
  if row['status']=='INDETERMINATE_ARITHMETIC':
   req(type(row['error'])is str and row['stage']==(body[-1]['stage']if body else ev[idx-1]['stage']),'refusal current');idx=stop;req(same(take('choice_complete',mode),row),'refusal copy');rows.append(row);continue
  req(len(body)==49,'completed body');gate=selected(e10,'gate_inputs',mode);bounds={};s0={};qs={}
  for kind in ['P','O']:
   p=selected(e10,'polynomial',mode,kind);raw=selected(e10,'residual_raw',mode,kind);old=selected(e10,'source_moments',mode,kind);p0,p1,q=rat(p['p0']),rat(p['p1']),rat(raw['q']);s0[kind]=old['s0'];qs[kind]=raw['q'];req(raw['q']==gate['rows'][kind]['q'],'original q')
   req(same(take('fixed_original_coefficients',mode),enc({'kind':kind,'p0':p0,'p1':p1,'q':q,'s0_s2':old})),'fixed coefficients')
   d=take('new_source_table',mode);req(d['kind']==kind and len(d['G'])==6 and len(d['Db'])==4 and len(d['D2b'])==8,'new source shapes')
   s=[nonnegative(box(old['s'+str(j)]))for j in range(3)]
   for n in [3,4]:
    d=take('NEW_source_moment_raw',mode);req(d['kind']==kind and type(d['index'])is int and d['index']==n,'new moment identity');im=box(d['imaginary']);req(im[0]<=0<=im[1],'new reality');s.append(nonnegative(box(d['real'])))
    for k,cap in [('wick_states',4096),('complex_products',200000)]:req(type(d['counts'][k])is int and 0<=d['counts'][k]<=cap,'Wick count')
   c=[F(1),-p0,-p1];rho=[];xi=[]
   for j in range(3):
    x=pt(0)
    for i in range(3):
     for k in range(3):x=add(x,scale(vac[kind][i+k+j],c[i]*c[k]))
    req(same(take('first_residual_moment',mode),enc({'kind':kind,'j':j,'interval':x})),'first residual arithmetic');rho.append(nonnegative(x))
   for j in range(3):
    x=add(add(s[j],scale(s[j+1],-2*q)),scale(s[j+2],q*q));req(same(take('inner_residual_moment',mode),enc({'kind':kind,'j':j,'interval':x})),'inner residual arithmetic');xi.append(nonnegative(x))
   chosen=[]
   for prefix,rhos in [('first',rho),('inner',xi)]:
    val=16*rhos[0][1];req(same(take(prefix+'_gap_bound',mode),enc({'kind':kind,'upper':val})),'gap');vals=[val]
    for t in map(F,[1,2,4,8,16]):
     delta=F(1,4);A=(t+2*delta)/(delta**2*t**3);B=-2/t**3-2*t*A;C=3/t**2+t*t*A;x=add(add(scale(rhos[2],A),scale(rhos[1],B)),scale(rhos[0],C));req(x[1]>=0,'majorant contradiction');req(same(take(prefix+'_majorant',mode),enc({'kind':kind,'tau':t,'A':A,'B':B,'C':C,'interval':x})),'signed majorant arithmetic');vals.append(x[1])
    chosen.append(min(vals))
   req(same(take('selected_norm_bounds',mode),enc({'kind':kind,'u2':chosen[0],'v2':chosen[1]})),'min selected');bounds[kind]=chosen
  e2=pt(0);f2=pt(0);jd=scale(root128(pt(2)),8)
  for kind,mult in [('P',12),('O',3)]:
   u2,v2=bounds[kind];u=root128((F(0),u2));v=root128((F(0),v2));ff=add(mul(jd,u),v);e2=add(e2,pt(mult*u2));f2=add(f2,scale(mul(ff,ff),mult))
  ef={'E':root128(e2),'F':root128(f2)};req(same(take('new_residual_norms',mode),enc(ef)),'new E/F');new=dict(gate,**enc(ef));req(same(take('new_gate_inputs',mode),{'old_E':gate['E'],'old_F':gate['F'],'new':new}),'new gate')
  ans=calculate({'s0':s0,'q':qs,'gate':new},mode);req(same(take('trial_norms',mode),{k:ans[k]for k in ['a_squared_upper','b_squared_upper','a_upper','b_upper']}),'trial norms');ans['new_moments']=4;req(same(ans,row),'posterior answer');req(same(take('choice_complete',mode),row),'choice copy');rows.append(row);progress({'stage':'schema_choice','mode':mode})
 req(same(take('complete',None),{'rows':rows})and idx==len(ev),'final event');req(same(part['current'],ev[-1])and same(part['completed'],rows),'partial final');req(not {x['status']for x in rows}>={'POSITIVE_CERTIFICATE','NEGATIVE_CERTIFICATE'},'contradictory signs')
 return {'status':'ACCEPTED_NEW_SPECTRAL_RESIDUAL_SCHEMA','count':2,'events':len(ev),'result_sha256':sha(O/'RESULT.json'),'independent_residual_majorant_posterior_arithmetic':True,'new_s3_s4_wick_truth_inherited':True,'old_moment_truth_inherited':True}
