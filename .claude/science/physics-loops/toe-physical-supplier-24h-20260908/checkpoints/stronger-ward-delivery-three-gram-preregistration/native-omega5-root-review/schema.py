from pathlib import Path
from fractions import Fraction as F
from math import comb,factorial,isfinite
import json,hashlib,re
S=1<<192

def req(v,s):
 if not v:raise ValueError(s)
def rat(x):
 req(type(x)is str and len(x)<=40000 and re.fullmatch(r'-?\d+(?:/\d+)?',x)is not None,'rational syntax');v=F(x);req(str(v)==x and max(abs(v.numerator).bit_length(),v.denominator.bit_length())<=65536,'bounded canonical rational');return v
def box(x):
 req(type(x)is list and len(x)==2,'interval shape');a,b=map(rat,x);req(a<=b,'interval order');return a,b
def rnd(b):return F(b[0].numerator*S//b[0].denominator,S),F(-((-b[1].numerator*S)//b[1].denominator),S)
def add(a,b):return rnd((a[0]+b[0],a[1]+b[1]))
def neg(a):return -a[1],-a[0]
def mul(a,b):
 v=[x*y for x in a for y in b];return rnd((min(v),max(v)))
def pt(x):return F(x),F(x)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def moments():
 # L=6I+A. Even adjacency closedwalks distribute positive/negative steps byaxis.
 walks={}
 for k in range(22):
  z=F(0)
  for a in range(k+1):
   for b in range(k-a+1):z+=F(factorial(2*k),factorial(a)**2*factorial(b)**2*factorial(k-a-b)**2)
  req(z.denominator==1,'integer closedwalk');walks[2*k]=z
 return {n:sum((comb(n,k)*6**(n-k)*walks[k]for k in range(0,n+1,2)),F(0))for n in range(3,44)}
def pi_box():
 vals=[]
 for q,n in((5,32),(239,10)):
  base=sum((F((-1)**k,(2*k+1)*q**(2*k+1))for k in range(n)),F(0));next=F((-1)**n,(2*n+1)*q**(2*n+1));vals.append((min(base,base+next),max(base,base+next)))
 a,b=vals;return (16*a[0]-4*b[1],16*a[1]-4*b[0])
def check(O,rf,elapsed,progress):
 O=Path(O);req(set(p.name for p in O.iterdir())=={'STARTED.json','NODES','PANELS','PARTIAL.json','TAIL.json','FINAL_ARITHMETIC.json','RESULT.json','WORKER_COMPLETE.json'},'top output census')
 req(set(p.name for p in(O/'NODES').iterdir())=={f'{i:04d}.json'for i in range(1742)},'node files');req(set(p.name for p in(O/'PANELS').iterdir())=={f'{i:02d}.json'for i in range(67)},'panel files')
 read=lambda p:json.loads(p.read_text());r=read(O/'RESULT.json');d=read(O/'WORKER_COMPLETE.json');part=read(O/'PARTIAL.json');raw=read(O/'FINAL_ARITHMETIC.json');tail=read(O/'TAIL.json');P=Path(rf['worker_path']);bind=read(P/'BINDING.json');bh=sha(P/'BINDING.json')
 req(d['status']=='COMPLETE_NEW_OMEGA5_ONLY'and d['runtime_sha256']==rf['worker_freeze']and d['binding_sha256']==bh and d['result_sha256']==sha(O/'RESULT.json'),'completion pins')
 for obj in(r,d,part):req(type(obj['seconds'])in(int,float)and isfinite(obj['seconds'])and 0<obj['seconds']<29,'finite seconds')
 req(part['seconds']<=r['seconds']<=d['seconds']<=elapsed<29.5,'time ordering');req(type(d['rss_bytes'])is int and 0<d['rss_bytes']<=384*1048576,'worker RSS');req(read(O/'STARTED.json')==read(Path(__file__).parent/'WORKER_AUTHORIZATION.json'),'started authorization')
 for k,v in{'panels':67,'nodes':1742,'endpoint_oracles_reused':3484,'oracle_calls':0,'tail_terms':40,'moments_count':41}.items():req(type(r[k])is int and r[k]==v,'literal '+k)
 req(r['new_quantity_integral']is True and r['observable']=='omega5=E_X_power_5_over_2','scope')
 geom=read(Path(bind['catalog_geometry_path']));cat=read(Path(bind['catalog']['directory'])/'RESULT.json');req(len(geom['nodes'])==1742 and len(cat['rows'])==3484,'source census');total=pt(0);six=pt(0)
 for panel in range(67):
  sub=pt(0)
  for j in range(26):
   i=26*panel+j;g=geom['nodes'][i];v=read(O/'NODES'/f'{i:04d}.json');inp=v['input'];req(type(v['id'])is int and v['id']==i and type(v['panel'])is int and v['panel']==panel-64,'node identity');req(type(inp['id'])is int and inp['id']==i and type(inp['panel'])is int and inp['panel']==panel-64,'input identity')
   ends=[]
   for eid in g['endpoint_ids']:
    rr=cat['rows'][eid];rp=Path(bind['catalog']['directory'])/rr['path'];req(sha(rp)==rr['sha256'],'endpoint hash');ends.append(box(read(rp)['A']))
   at=(ends[1][0],ends[0][1]);t=box(g['t_interval']);w=rnd(box(g['weight']));req(box(inp['A_interval'])==at and box(inp['t_interval'])==t and box(inp['weight_interval'])==w,'mapped source copies')
   t2=mul(t,t);t4=mul(t2,t2);t6=mul(t4,t2);q=add(add(add(pt(42),neg(mul(pt(6),t2))),t4),neg(mul(t6,at)));weighted=mul(w,q);sub=add(sub,weighted);six=add(six,mul(w,t6))
   req(box(v['integrand'])==q and box(v['weighted'])==weighted and box(v['panel_cumulative'])==sub and box(v['weighted_t6_cumulative'])==six,'node arithmetic')
  total=add(total,sub);v=read(O/'PANELS'/f'{panel:02d}.json');req(type(v['panel'])is int and v['panel']==panel-64 and box(v['value'])==sub and box(v['cumulative'])==total,'panel arithmetic');progress({'stage':'schema_panel','panel':panel-64})
 ms=moments();req(set(tail['moments'])=={str(k)for k in range(3,44)},'moment census')
 for k,v in ms.items():req(rat(tail['moments'][str(k)])==v,'tail moment')
 terms=[F((-1)**n)*ms[n+3]/((2*n+1)*8**(2*n+1))for n in range(40)];req(type(tail['high_terms'])is list and list(map(rat,tail['high_terms']))==terms,'tail terms');high=sum(terms,F(0));rem=ms[43]/(81*8**81);eps=F(1,2**64);lc=42*eps-2*eps**3+eps**5/5;low=(lc-F(17,60)*eps**7/7,lc);quad=F(1904,4**52)
 req(rat(tail['high_partial'])==high and rat(tail['high_remainder'])==rem and box(tail['low_interval'])==low and rat(tail['quadrature_radius'])==quad and type(tail['tail_terms'])is int and tail['tail_terms']==40,'tail assembly')
 pl,pu=pi_box();ans=mul(add(add(total,(high,high+rem)),(low[0]-quad,low[1]+quad)),(2/pu,2/pl));width=ans[1]-ans[0]
 for v in(r,raw):req(box(v['interval'])==ans and rat(v['width'])==width and box(v['middle'])==total and box(v['weighted_t6'])==six,'final copies')
 req(box(raw['pi_interval'])==(pl,pu)and rat(r['quadrature_radius'])==quad and rat(r['target'])==F(1,10**24),'constants')
 mg=total[1]-total[0]<=F(1,10**24);sg=six[1]<=300000;req(type(r['middle_width_gate'])is bool and r['middle_width_gate']==mg and type(r['weighted_t6_gate'])is bool and r['weighted_t6_gate']==sg,'partial gates');req(r['status']==('CERTIFIED_TARGET'if mg and sg and width<=F(1,10**24)else'INDETERMINATE'),'final gate')
 req(part['stage']=='complete'and type(part['completed_nodes'])is int and part['completed_nodes']==1742 and part['panels']==list(range(-64,3))and all(type(x)is int for x in part['panels'])and box(part['middle'])==total and box(part['weighted_t6'])==six,'partial final')
 copy=part['current']['result'];req(json.dumps({k:v for k,v in copy.items()if k!='seconds'},sort_keys=True)==json.dumps({k:v for k,v in r.items()if k!='seconds'},sort_keys=True),'type-aware partial result copy');req(type(copy['seconds'])in(int,float)and isfinite(copy['seconds'])and 0<copy['seconds']<=part['seconds'],'partial prior time')
 return {'status':'ACCEPTED_NEW_OMEGA5_SCHEMA','count':1742,'panels':67,'result_sha256':sha(O/'RESULT.json'),'target_certified':r['status']=='CERTIFIED_TARGET','full1742_node_and_tail_arithmetic_reconciled':True,'native_scalar_containment_inherited':True,'interval':r['interval'],'width':r['width'],'oracle_calls':0}
