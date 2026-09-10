"""Exact root/collision geometry only. No elliptic oracle or physical integral."""
import json,hashlib,types,sys
from pathlib import Path
from fractions import Fraction as F
P=Path(__file__).resolve().parent
for name in ('interval_base','highorder'):
 p=P/(name+'.py');m=types.ModuleType(name);m.__file__=str(p);sys.modules[name]=m;exec(compile(p.read_bytes(),str(p),'exec'),m.__dict__)
rule=sys.modules['highorder'].gauss(6)
old=Path('/private/tmp/toe-24h-probes-20260908/native-elliptic-b-run-76350')
catalog=json.loads((old/'GAUSS.json').read_text())['rule']
cs=[]
for j in range(-28,3):
 for i,(x,w) in enumerate(catalog):
  a=F(2)**j;cs.append((j,i,a*(F(x[0])+3)/2,a*(F(x[1])+3)/2))
rows=[];checks=0;global_sep=None
for j in range(-7,4):
 for i,(x,w) in enumerate(rule):
  a=F(2)**j;lo=a*(x[0]+3)/2;hi=a*(x[1]+3)/2;mid=(lo+hi)/2
  sep=None
  for cj,ci,cl,ch in cs:
   distance=max(lo-ch,cl-hi)
   if distance<=0:raise ValueError(('collision',j,i,cj,ci))
   checks+=1;sep=distance if sep is None else min(sep,distance)
  global_sep=sep if global_sep is None else min(global_sep,sep)
  rows.append({'id':len(rows),'panel':j,'root':i,'s_interval':[str(lo),str(hi)],'s_midpoint':str(mid),'weight':[str(a*z/2) for z in w],'minimum_catalog_separation':str(sep),'A_midpoint_inflation':str((hi-lo)/6),'Aprime_midpoint_inflation':str(3*(hi-lo)/lo**4)})
result={'scope':'exact geometry only; no oracle calls','rows':rows,'pole_count':len(rows),'catalog_node_count':len(cs),'separation_predicates':checks,'minimum_separation':str(global_sep),'minimum_separation_decimal':float(global_sep),'catalog_gauss_sha256':hashlib.sha256((old/'GAUSS.json').read_bytes()).hexdigest()}
(P/'POLES.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
