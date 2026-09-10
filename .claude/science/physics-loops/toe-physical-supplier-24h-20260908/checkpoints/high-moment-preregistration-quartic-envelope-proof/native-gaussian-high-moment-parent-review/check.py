from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import json,sys,types,hashlib,copy
sys.set_int_max_str_digits(20000)
P=Path('/private/tmp/toe-24h-probes-20260908/native-gaussian-high-moment-runtime-design');D=Path(__file__).resolve().parent;T=D/'synthetic_inputs';T.mkdir(exist_ok=True)
for n in ['core','engine','adapter','loader']:
 m=types.ModuleType(n);m.__file__=str(P/(n+'.py'));sys.modules[n]=m;exec(compile(Path(m.__file__).read_bytes(),m.__file__,'exec'),m.__dict__)
L=sys.modules['loader'];count=0
for a,b in [('1/'+str((1<<20000)+1),'1/3'),('-1/3','-1/'+str((1<<20000)+1))]:
 x=L.dyadic([a,b]);assert F(x[0][0],L.S)<=F(a)<=F(b)<=F(x[0][1],L.S);count+=1
# Entirely fabricated receipt families. No actual bound input files are read.
binding={}
def save(name,obj):
 p=T/(name+'.json');p.write_text(json.dumps(obj)+'\n');return {'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
for family in ['degree20','omega79']:
 expected={'accepted_status':'SYNTHETIC_ACCEPTED','worker_status':'SYNTHETIC_DONE','result_status':'SYNTHETIC_RESULT','worker_seconds':59,'root_seconds':59.5,'external_seconds':60}
 result={'status':'SYNTHETIC_RESULT'}
 if family=='omega79':result['rows']=[dict(observable=n,status='CERTIFIED_TARGET',target=str(F(1,10**pow)),interval=['1','1'],width='0',middle_width_gate=True,weighted_power_gate=True)for n,pow in [('omega7',22),('omega9',20)]]
 files={'result':save(family+'_result',result),'root_freeze':save(family+'_root',{'worker_freeze':'synthetic_worker'})};rh=files['result']['sha256'];root=files['root_freeze']['sha256']
 files['worker']=save(family+'_worker',dict(status='SYNTHETIC_DONE',result_sha256=rh,runtime_sha256='synthetic_worker',seconds=1,rss_bytes=100))
 files['receipt']=save(family+'_receipt',dict(pass_=True))
 r={'pass':True,'failure':None,'returncode':0,'worker_freeze':'synthetic_worker','seconds':2,'sampled_whole_tree_peak':200};files['receipt']=save(family+'_receipt',r)
 files['acceptance']=save(family+'_accept',dict(status='SYNTHETIC_ACCEPTED',once=True,result_sha256=rh,worker_freeze='synthetic_worker',root_freeze=root,external_seconds=3,sampled_whole_tree_peak=200,external_rss_bytes=100))
 binding[family]={'files':files,'worker_freeze':'synthetic_worker','expected':expected}
ev=[]
def e(stage,choice=None,data=None):ev.append(dict(sequence=len(ev)+1,stage=stage,choice=choice,data={}if data is None else data))
e('binding');e('scalar_inputs',data={'c':['1/3','1/3'],'nu':['2','2'],'omega5':['3','3']});labels=list(combinations(range(6),2))
for mode in ['residual','variational']:
 e('choice_start',mode)
 for kind in ['P','O']:
  e('vacuum_inputs',mode)
  for j in range(7):e('vacuum_moment_raw',mode,dict(kind=kind,index=j,real=['1','1'],imaginary=['0','0']))
  e('first_polynomial',mode);e('source_inputs',mode)
  for _ in range(3):e('source_moment_raw',mode)
  e('residual_raw',mode)
 seen=set()
 for c in labels:
  for a in labels:
   if set(c).intersection(a):continue
   kc='O'if c[0]^1==c[1]else'P';ka='O'if a[0]^1==a[1]else'P';op=sum((v^1)in a for v in c);key=('PP'+str(op))if kc==ka=='P'else kc+ka
   if key not in seen:e('cross_wick_raw',mode);seen.add(key)
   e('ordered_word',mode)
 e('gate_inputs',mode);e('choice_complete',mode)
e('complete');assert len(ev)==255;eventpath=T/'events.ndjson';eventpath.write_text(''.join(json.dumps(x)+'\n'for x in ev));binding['degree20']['files']['events']={'path':str(eventpath),'sha256':hashlib.sha256(eventpath.read_bytes()).hexdigest()};binding['omega79']['files']['reused']=save('reused',{str(j):str(j+1)for j in range(44)})
received=[];packet=L.load_packet(binding,lambda s,d:received.append((s,d)));assert packet['first_order']==7 and packet['classes']['P']['accepted_m']['0']==[[L.S,L.S],[0,0]];count+=1
mapping=next(d['rational']for s,d in received if s=='absolute_moment_source_map');assert mapping['1']==['1','1']and mapping['6']==['4','4']and mapping['8']==['5','5']and mapping['10']==['6','6'];count+=1
for mutate in [lambda es:es[10].update(sequence=True),lambda es:es[0].update(stage='false'),lambda es:es[3].update(choice='false')]:
 bad=copy.deepcopy(ev);mutate(bad);eventpath.write_text(''.join(json.dumps(x)+'\n'for x in bad));binding['degree20']['files']['events']['sha256']=hashlib.sha256(eventpath.read_bytes()).hexdigest()
 try:L.load_packet(binding,lambda *_:None)
 except ValueError:count+=1
 else:raise AssertionError('coherent synthetic chronology mutant passed')
print(json.dumps({'status':'PASS','checks':count,'full_synthetic_loader':True,'native_input_loads':0,'native_moment_computations':0}))
