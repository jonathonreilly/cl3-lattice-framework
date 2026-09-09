from pathlib import Path
from fractions import Fraction as F
import types,sys,json
P=Path('/private/tmp/toe-24h-probes-20260908/native-fixed192-compression-pilot-design')
for name in ('interval','pivot_resume'):
 m=types.ModuleType(name);sys.modules[name]=m;exec(compile((P/(name+'.py')).read_bytes(),str(P/(name+'.py')),'exec'),m.__dict__)
iv=sys.modules['interval'];p=sys.modules['pivot_resume'];V=[[F(x) for x in v] for v in [[1,0,0,0],[1,0,1,0],[0,1,0,2],[0,0,0,1]]];lab=tuple(('pole',i,0,ch,2) for i,ch in enumerate((1,1,-1,-1)));calls=[]
def dot(x,y):return sum((a*b for a,b in zip(x,y)),F())
def J(x):return[-x[1],x[0],-x[3],x[2]]
def fetch(i,j):calls.append((i,j));return iv.rational(dot(V[i],V[j])),iv.rational(dot(V[i],J(V[j])))
a=p.run(fetch,lab,lambda _:None,native=False,max_pairs=1);assert a['status']=='PAIR_CAP';count=1;calls.clear();events=[];b=p.run(fetch,lab,events.append,native=False,max_pairs=2,resume=a['history']);resume_calls=len(calls);calls.clear();c=p.run(fetch,lab,lambda _:None,native=False,max_pairs=2);assert b==c and b['status']=='PASS_BOTH';count+=1;assert resume_calls<len(calls);count+=1
assert [e['step'] for e in events if e['stage']=='pivot_row']==[1];count+=1
for resume in ((a['history'][0],a['history'][0]),(dict(a['history'][0],r=(0,1)),)):
 try:p.run(fetch,lab,lambda _:None,native=False,max_pairs=2,resume=resume)
 except ValueError:count+=1
 else:raise ValueError('bad resume')
s=p.run(lambda i,j:((0,iv.S),iv.ZERO), (('pole',0,0,1,2),),lambda _:None,native=False,max_pairs=1);assert s['status']=='PRECISION_STALL';count+=1
failed=[]
def bad(i,j):raise ValueError('synthetic entry failure')
try:p.run(bad,lab,failed.append,native=False,max_pairs=1)
except ValueError:pass
assert failed[-1]['stage']=='FAILED' and failed[-1]['current']=={'stage':'diagonal','step':0,'index':0};count+=1
print(json.dumps({'status':'PASS','predicates':count,'continuation_entry_calls':resume_calls,'fresh_entry_calls':len(calls),'native_calls':0}))
