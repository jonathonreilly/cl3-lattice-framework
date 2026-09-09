from pathlib import Path
from fractions import Fraction as F
import json,hashlib,math
S=1<<192
def req(x,m):
 if not x:raise ValueError(m)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def iv(a):
 req(isinstance(a,list) and len(a)==2,'two endpoints');x,y=map(F,a);req(x<=y,'ordered interval');return x,y
def add(a,b):return(F(((a[0]+b[0])*S).__floor__(),S),F(((a[1]+b[1])*S).__ceil__(),S))
def check(out,freeze,elapsed):
 out=Path(out);r=json.loads((out/'RESULT.json').read_text());w=json.loads((out/'WORKER_COMPLETE.json').read_text());p=json.loads((out/'PARTIAL.json').read_text())
 req(w['status']=='COMPLETE_CATALOG_INTEGRAL' and w['runtime_sha256']==freeze and w['result_sha256']==sha(out/'RESULT.json'),'completion source')
 lo,hi=iv(r['interval']);width=hi-lo;target=F(2,10**19);req(width==F(r['width']) and F(r['target'])==target and r['status']==('CERTIFIED_TARGET' if width<=target else 'INDETERMINATE'),'precision')
 req(r['panels']==67 and r['nodes']==1742 and r['oracle_calls']==0 and r['new_catalog_only_integral'] is True,'scope')
 req(all(isinstance(t,(int,float)) and math.isfinite(t) and 0<t for t in [r['seconds'],w['seconds'],p['seconds'],elapsed]) and r['seconds']<=p['seconds']<=w['seconds']<=elapsed<=30,'inclusive timing')
 req(0<w['rss_bytes']<=384*1048576,'worker RSS');req(p['stage']=='complete' and p['current']==2 and p['panels']==[f'PANELS/{j:02d}.json' for j in range(67)],'final partial')
 req({x.name for x in(out/'PANELS').iterdir()}=={f'{j:02d}.json' for j in range(67)},'all panels');total=(F(0),F(0))
 for j in range(67):
  d=json.loads((out/f'PANELS/{j:02d}.json').read_text());req(d['panel']==j-64,'panel id');total=add(total,iv(d['value']));req(total==iv(d['cumulative']),'saved panel cumulative')
 req(total==iv(r['middle'])==iv(p['sum']),'middle binding');req(F(r['quadrature_radius'])==F(400,27)*F(4,25)**26 and F(r['high_remainder'])==F(12**26,53*8**53) and F(r['low_bound'])==F(1,3*2**64),'fixed error allocations')
 return {'status':'PASS_SAVED_INTEGRAL_SCHEMA','scientific_status':r['status'],'result_sha256':sha(out/'RESULT.json'),'panels':67,'oracle_calls':0,'individual_panel_integrands_recomputed':False}
