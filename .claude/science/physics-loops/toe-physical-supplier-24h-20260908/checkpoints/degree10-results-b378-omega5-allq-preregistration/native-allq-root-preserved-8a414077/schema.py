from pathlib import Path
from fractions import Fraction as F
from math import isqrt,isfinite
import json,hashlib,re

def req(x,s):
 if not x:raise ValueError(s)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def rat(x):
 req(type(x)is str and len(x)<=20000 and re.fullmatch(r'-?\d+(?:/\d+)?',x)is not None,'rational syntax');v=F(x);req(str(v)==x and max(abs(v.numerator).bit_length(),v.denominator.bit_length())<=32768,'rational cap');return v
def box(x):
 req(type(x)is list and len(x)==2,'box');a,b=map(rat,x);req(a<=b,'order');return a,b
def plus(*bs):return(sum((x[0]for x in bs),F(0)),sum((x[1]for x in bs),F(0)))
def scale(b,q):return min(b[0]*q,b[1]*q),max(b[0]*q,b[1]*q)
def mul(a,b):
 v=[x*y for x in a for y in b];return min(v),max(v)
def root(n):
 S=1<<128;k=isqrt(n*S*S);return F(k,S),F(k if k*k==n*S*S else k+1,S)
def screen(E,p,o):
 req(min(E[0],p[0],o[0])>=0,'nonnegative source');X=scale(root(15),4);V=scale(root(30),32);C=mul(E,plus(scale(X,2),E,V));a2=scale(plus(scale(p,12),scale(o,3)),F(1,8));th=mul(a2,plus((F(1),F(1)),scale(root(2),8)));return {'E':E,'s0P':p,'s0O':o,'X':X,'V':V,'C':C,'a2':a2,'threshold':th},C[0]-th[1]
def check(O,rf,elapsed,progress):
 O=Path(O);req(set(p.name for p in O.iterdir())=={'STARTED.json','PARTIAL.json','RESULT.json','WORKER_COMPLETE.json','residual.json','variational.json'},'membership')
 read=lambda name:json.loads((O/name).read_text());r=read('RESULT.json');w=read('WORKER_COMPLETE.json');p=read('PARTIAL.json');P=Path(rf['worker_path']);bh=sha(P/'BINDING.json');binding=json.loads((P/'BINDING.json').read_text())
 auth=json.loads((Path(__file__).parent/'WORKER_AUTHORIZATION.json').read_text());req(read('STARTED.json')==auth,'start auth');req(w['status']=='COMPLETE_SAVED_ALLQ_SCREEN_ONLY'and w['runtime_sha256']==rf['worker_freeze']and w['binding_sha256']==bh and w['result_sha256']==sha(O/'RESULT.json'),'completion')
 req(type(w['rss_bytes'])is int and 0<w['rss_bytes']<=384*1048576,'RSS')
 for x in [r['seconds'],w['seconds'],p['seconds']]:req(type(x)in(int,float)and isfinite(x)and 0<x<9,'timing')
 req(p['seconds']<=r['seconds']<=w['seconds'],'time order');req(r['status']=='COMPLETE_SAVED_ALLQ_SCREEN'and type(r['modes'])is int and r['modes']==2 and type(r['saved_events'])is int and r['saved_events']==205,'census')
 for k in ['native_calls','original_moments_recomputed']:req(type(r[k])is int and r[k]==0,'scope')
 req(r['scope']=='unchanged degree1 first polynomials and e858 error functional only; not alpha no-go','scope string');req(type(r['rows'])is list and len(r['rows'])==2,'rows')
 source=Path(binding['files']['events']);req(sha(source)==binding['inputs'][str(source)],'source event pin');events=[]
 with source.open()as f:
  for _ in range(205):
   line=f.readline(1048577);req(bool(line)and len(line)<=1048576,'bounded source line');events.append(json.loads(line))
  req(not f.read(1),'source exhaustion')
 grammar=[('binding',None),('scalar_inputs',None)]
 for mode in ['residual','variational']:grammar +=[('choice_start',mode)]+[(s,mode)for s in ['moments','polynomial','source_moments','residual_raw']*2+['ordered_word']*90+['gate_inputs','choice_complete']]
 grammar +=[('complete',None)];req(len(grammar)==205,'internal grammar')
 for i,(e,(stage,mode))in enumerate(zip(events,grammar)):req(type(e['sequence'])is int and e['sequence']==i+1 and e['stage']==stage and e['choice']==mode,'source chronology')
 flags=[];extracted={}
 for mode,base,row in zip(['residual','variational'],[0,101],r['rows']):
  progress({'stage':'schema_mode','mode':mode});sp=events[base+5]['data'];so=events[base+9]['data'];gate=events[base+101]['data'];req(sp['kind']=='P'and so['kind']=='O','source classes');E=box(gate['E']);a=box(sp['s0']);b=box(so['s0']);expected,margin=screen(E,a,b)
  req(row==read(mode+'.json')and row['mode']==mode and type(row['source_gate_event'])is int and row['source_gate_event']==base+102,'mode copies')
  for k,v in expected.items():req(box(row[k])==v,'screen '+k)
  flag=margin>=0;req(rat(row['margin_lower'])==margin and type(row['excluded'])is bool and row['excluded']==flag and row['status']==('CERTIFICATE_FAMILY_EXCLUDED'if flag else'INDETERMINATE_SCREEN'),'screen flag');flags.append(flag)
  extracted[mode]={'E':gate['E'],'s0P':sp['s0'],'s0O':so['s0'],'gate_event':base+102}
 req(type(r['all_fixed_first_polynomials_excluded'])is bool and r['all_fixed_first_polynomials_excluded']==all(flags),'summary');req(p['stage']=='complete'and type(p['source_sequence'])is int and p['source_sequence']==205 and p['choice']is None and p['rows']==r['rows']and p['current']=={'rows':r['rows']}and p['extracted']==extracted,'final partial');req(elapsed<9.5,'elapsed')
 return {'status':'ACCEPTED_ALLQ_SAVED_SCREEN_SCHEMA','count':2,'source_events':205,'result_sha256':sha(O/'RESULT.json'),'original_events_sha256':sha(source),'excluded_modes':sum(flags),'all_fixed_first_polynomials_excluded':all(flags),'independent_screen_arithmetic':True,'original_moment_truth_inherited':True,'alpha_no_go':False}
