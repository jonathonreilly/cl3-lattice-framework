"""Saved schema plus preselected independent rational entry checks; no builder import."""
import json,hashlib,sys,signal,time,math
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
START=time.monotonic();P=Path(__file__).resolve().parent

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main(binding,output):
 out=Path(output)
 if out.exists():raise ValueError('fresh output')
 out.mkdir();stage='binding';checks=[];current=None
 def save(error=None):(out/'PARTIAL.json').write_text(json.dumps({'stage':stage,'checks':checks,'current':current,'error':error})+'\n')
 try:
  b=json.loads(Path(binding).read_text())
  for n,h in b['files'].items():
   if sha(n)!=h:raise ValueError('binding '+n)
  # Full schema checker is explicitly reused byte-identically from reviewed root.
  import types
  m=types.ModuleType('saved_schema');src=(P/'schema.py').read_bytes()
  if hashlib.sha256(src).hexdigest()!=b['files'][str(P/'schema.py')]:raise ValueError('schema pin')
  exec(compile(src,str(P/'schema.py'),'exec'),m.__dict__)
  study=Path(b['study']);receipt=json.loads(Path(b['root_receipt']).read_text());accept=json.loads(Path(b['root_acceptance']).read_text())
  worker=json.loads((study/'WORKER_COMPLETE.json').read_text())
  if accept['status']!='ACCEPTED_COMMON_CACHE_MIDPOINT_ARITHMETIC' or accept['result_sha256']!=sha(study/'RESULT.json') or accept['cache_sha256']!=sha(study/'CACHE.ndjson') or accept['worker_freeze']!=b['worker_freeze']:raise ValueError('actual acceptance binding')
  if worker['freeze_sha256']!=b['worker_freeze'] or worker['result_sha256']!=sha(study/'RESULT.json'):raise ValueError('worker identity')
  if receipt['pass'] is not True or receipt['failure'] is not None or receipt['returncode']!=0 or receipt['worker_freeze']!=b['worker_freeze']:raise ValueError('root completion')
  fields=(receipt['seconds'],receipt['sampled_whole_tree_peak'],worker['seconds'],worker['rss_bytes'],accept['external_seconds'],accept['external_max_rss'],accept['sampled_whole_tree_peak'])
  if not all(isinstance(x,(int,float)) and not isinstance(x,bool) and math.isfinite(x) and x>0 for x in fields):raise ValueError('finite positive resources')
  if not worker['seconds']<=receipt['seconds']<=60 or accept['external_seconds']>60 or max(receipt['sampled_whole_tree_peak'],worker['rss_bytes'],accept['external_max_rss'],accept['sampled_whole_tree_peak'])>384*1048576:raise ValueError('resource caps')
  stage='full_schema';save();schema=m.check(study,b['worker_freeze'],receipt['seconds'])
  # Root acceptance schema/fixed output hash must be finalized in execution binding.
  if sha(b['root_acceptance'])!=b['root_acceptance_sha256']:raise ValueError('acceptance hash')
  plan=json.loads(Path(b['plan']).read_text());arows=json.loads(Path(plan['a_result']).read_text())['rows'];brows=json.loads(Path(plan['summary']).read_text())['rows'];poles=json.loads(Path(plan['poles']).read_text())['rows'];pi=sum(map(F,plan['pi_interval']))/2
  vals=[tuple(sum(map(F,a['oracle'][k]))/2 for k in ('A','Aprime'))+tuple(sum(map(F,z[k]))/2 for k in ('B','Bprime')) for a,z in zip(arows,brows)];ss=[F(p['s_midpoint']) for p in poles];alpha=[35*(sum(map(F,p['weight']))/2)/(2*pi) for p in poles]
  selection=json.loads((P/'SELECTION.json').read_text())['entries'];wanted={tuple(x) for x in selection};found={}
  for line in (study/'CACHE.ndjson').open():
   row=json.loads(line)
   for j,gl,gu,jl,ju in row['entries']:
    key=(row['type'],row['i'],j)
    if key in wanted:found[key]=((int(gl),int(gu)),(int(jl),int(ju)))
  if len(found)!=128:raise ValueError('sample coverage')
  # Literal seven-star I/O/T contraction, not the cache endpoint implementation.
  I=[[F(i==j) for j in range(7)] for i in range(7)];O=[[F(0) for j in range(7)] for i in range(7)];T=[[F(0) for j in range(7)] for i in range(7)]
  for u in (1,3,5):O[u][u+1]=O[u+1][u]=1
  for u in range(1,7):T[0][u]=-1 if u%2 else 1;T[u][0]=-T[0][u]
  center=[1,0,0,0,0,0,0];perp=[0,1,0,1,0,0,0];opposite=[0,1,-1,0,0,0,0];cross=[0,0,-1,0,0,1,0]
  def contract(M,x,y):return sum((F(x[i])*M[i][j]*y[j] for i in range(7) for j in range(7)),F())
  def endpoint(n,sig,typ):
   s=ss[n];A,Ap,B,Bp=vals[n];D=(1-s*s*A)/6;Dp=-(2*s*A+s*s*Ap)/6
   x,y={'cc':(center,center),'cd':(center,perp),'P':(perp,perp),'O':(opposite,opposite),'cross':(perp,cross)}[typ]
   ii,oo,tt=(contract(M,x,y) for M in (I,O,T))
   return (sig*s*(A*ii+(A-D)*oo)+D*tt,
    sig*((A+s*Ap)*ii+(A-D+s*(Ap-Dp))*oo)+Dp*tt,
    -B*ii-B*(1+s*s/6)*oo+sig*s*B*tt/6,
    -Bp*ii-(Bp*(1+s*s/6)+s*B/3)*oo+sig*(B+s*Bp)*tt/6)
  stage='sample_arithmetic';save()
  for typ,i,j in selection:
   current=[typ,i,j];save()
   n,sig=i//2,(-1 if i%2==0 else 1);nn,tau=j//2,(-1 if j%2==0 else 1);a=endpoint(n,-sig,typ);z=endpoint(nn,tau,typ);den=sig*ss[n]+tau*ss[nn]
   g=(z[0]-a[0])/den if den else tau*z[1];jj=-(z[2]-a[2])/den if den else -tau*z[3]
   if typ!='cd' and i==j:jj=F(0)
   v=alpha[n]*alpha[nn];Q=2**256;lo=isqrt(v.numerator*Q*Q//v.denominator);hi=lo if F(lo*lo,Q*Q)==v else lo+1
   for scalar,interval in zip((g,jj),found[typ,i,j]):
    ends=sorted((scalar*lo/Q,scalar*hi/Q))
    if not F(interval[0],2**192)<=ends[0]<=ends[1]<=F(interval[1],2**192):raise ValueError(('sample containment',typ,i,j))
   checks.append([typ,i,j]);save()
  (out/'RESULT.json').write_text(json.dumps({'status':'PASS_SAVED_SCHEMA_AND_FIXED_SAMPLES','samples':128,'schema':schema,'scope':'sample arithmetic supports full reviewed source; not every-entry arithmetic proof','oracle_calls':0,'builder_calls':0,'seconds':time.monotonic()-START})+'\n')
 except BaseException as e:save(repr(e));(out/'FAILURE.json').write_text(json.dumps({'error':repr(e),'stage':stage})+'\n');raise
if __name__=='__main__':
 if len(sys.argv)!=3:raise SystemExit('binding output')
 main(*sys.argv[1:])
