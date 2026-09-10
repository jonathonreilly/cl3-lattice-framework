"""Prospective ALL-entry saved append validation. No producer imports."""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import json,hashlib,time,signal,sys,math
P=Path(__file__).resolve().parent;S=2**192;Q=2**256
ORBITS=((1,1,0),(1,0,0),(0,1,0),(0,0,2),(0,0,1))
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def main(binding,output):
 start=time.monotonic();out=Path(output)
 if out.exists():raise ValueError('fresh output')
 out.mkdir();state={'stage':'binding','row':None,'entries':0};checks=0
 def save(error=None):(out/'PARTIAL.json').write_text(json.dumps(dict(state,error=error,checks=checks))+'\n')
 def ck(x,why):
  nonlocal checks
  if not x:raise ValueError(why)
  checks+=1
 save();remaining=signal.getitimer(signal.ITIMER_REAL)[0];signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('saved checker deadline')));signal.setitimer(signal.ITIMER_REAL,min(25,remaining) if remaining>0 else 25)
 try:
  cfg=json.loads(Path(binding).read_text());ck(cfg['status']=='ACCEPTED_RESULT_BOUND','accepted binding status')
  def read(p):
   p=str(p);ck(p in cfg['files'] and sha(p)==cfg['files'][p],'bound read '+p);return json.loads(Path(p).read_text())
  for n,h in cfg['files'].items():ck(sha(n)==h,'pin '+n)
  wf=read(cfg['worker_freeze_path']);rf=read(cfg['root_freeze_path'])
  ck(sha(cfg['worker_freeze_path'])==cfg['worker_freeze']==rf['worker_freeze'],'frozen producer')
  for path,h in wf['inputs'].items():ck(cfg['files'].get(path)==h,'full producer closure')
  rootdir=Path(cfg['root_freeze_path']).parent
  for name,h in rf['files'].items():ck(cfg['files'].get(str(rootdir/name))==h,'full root closure')
  study=Path(cfg['study']);r=read(study/'RESULT.json');w=read(study/'WORKER_COMPLETE.json');part=read(study/'PARTIAL.json');receipt=read(cfg['root_receipt']);accept=read(cfg['root_acceptance'])
  ck(receipt['pass'] is True and receipt['failure'] is None and type(receipt['returncode']) is int and receipt['returncode']==0 and receipt['worker_freeze']==cfg['worker_freeze'],'root completion')
  numeric=(receipt['seconds'],w['seconds'],accept['external_seconds'])
  ck(all(type(x) in(int,float) and math.isfinite(x) and x>0 for x in numeric),'finite timings')
  memory=(receipt['sampled_whole_tree_peak'],w['rss_bytes'],accept['external_max_rss'],accept['sampled_whole_tree_peak'])
  ck(all(type(x) is int and 0<x<=384*1048576 for x in memory),'finite memory')
  ck(w['seconds']<=receipt['seconds']<=30 and accept['external_seconds']<=30,'resource caps')
  ck(accept['status']=='ACCEPTED_WARD_APPEND_MIDPOINT_ARITHMETIC' and accept['result_sha256']==sha(study/'RESULT.json') and accept['append_sha256']==sha(study/'APPEND.ndjson') and accept['worker_freeze']==cfg['worker_freeze'] and accept['root_freeze']==sha(cfg['root_freeze_path']),'actual acceptance')
  ck(w['status']=='COMPLETE_APPEND_MIDPOINT_ONLY' and w['freeze_sha256']==cfg['worker_freeze'] and w['result_sha256']==sha(study/'RESULT.json'),'worker binding')
  ck(sha(cfg['root_acceptance'])==cfg['root_acceptance_sha256'],'accepted receipt')
  plan=read(cfg['plan'])
  for path,h in plan['inputs'].items():ck(cfg['files'].get(path)==h,'full plan closure')
  ck(w['binding_sha256']==sha(cfg['plan']),'plan identity');pole=read(plan['pole_binding']);arows=read(pole['a_result'])['rows'];brows=read(pole['summary'])['rows'];pr=read(pole['poles'])['rows'];pi=sum(map(F,pole['pi_interval']))/2
  def scalar(role):
   obj=read(plan['roles'][role]['result'])
   for k in plan['roles'][role]['interval_path']:obj=obj[k]
   return sum(map(F,obj))/2
  a0,c=scalar('a0'),scalar('cminus');A=[sum(map(F,x['oracle']['A']))/2 for x in arows];B=[sum(map(F,x['B']))/2 for x in brows];ss=[F(x['s_midpoint']) for x in pr];alpha=[35*sum(map(F,x['weight']))/(4*pi) for x in pr];roots=[]
  for a in alpha:
   lo=isqrt(a.numerator*Q*Q//a.denominator);hi=lo if F(lo*lo,Q*Q)==a else lo+1;roots.append((F(lo,Q),F(hi,Q)))
  # Literal signed seven-site source projections, not reduced producer matrices.
  I=[[F(i==j) for j in range(7)] for i in range(7)];O=[[F(0) for j in range(7)] for i in range(7)];T=[[F(0) for j in range(7)] for i in range(7)]
  for i in (1,3,5):O[i][i+1]=O[i+1][i]=1
  for i in range(1,7):T[0][i]=-1 if i%2 else 1;T[i][0]=-T[0][i]
  N=[[I[i][j]+O[i][j] for j in range(7)] for i in range(7)]
  reps=(((1,2),(3,4)),((1,2),(3,5)),((1,3),(5,6)),((1,3),(2,4)),((1,3),(2,5)))
  def vec(sites):return [F(0)]+[F((1 if i%2 else -1) if i in sites else 0) for i in range(1,7)]
  def dot(M,x,y):return sum((x[i]*M[i][j]*y[j] for i in range(7) for j in range(7)),F())
  geom=[]
  for aa,cc in reps:
   W=[[F(1)]+[F(0)]*6,vec(aa),vec(cc)];geom.append([[[dot(M,x,y) for y in W] for x in W] for M in (I,O,T,N)])
  expected=[]
  for oi in range(5):
   for kind in range(3):
    for n in range(66):
     for sig in(-1,1):expected.append((oi,kind,n,sig))
   for kind in range(3):expected.append((oi,kind,None,None))
  ck(len(expected)==1995,'fixed rows');maximum=0;traces=[[0,0] for _ in range(5)]
  ck(str(study/'APPEND.ndjson') in cfg['files'] and sha(study/'APPEND.ndjson')==r['append_sha256'],'stream hash')
  index=-1;last=None
  with(study/'APPEND.ndjson').open() as stream:
   for index,line in enumerate(stream):
    state.update(stage='row_parse',row=index);save();ck(index<1995,'extra row');x=json.loads(line);last={k:v for k,v in x.items() if k!='entries'};oi,kind,n,sig=expected[index];ii,oo,tt,nn=geom[oi]
    ck(x['orbit_id']==oi and x['append_index']==396+kind,'row labels');state['stage']='row_arithmetic';save()
    if n is None:
     ck(x['type']=='append_self' and [e[0] for e in x['entries']]==list(range(396+kind,399)),'self indices')
    else:ck(x['type']=='append_to_pole' and x['pole_id']==n and x['sigma']==sig and [e[0] for e in x['entries']]==[6*n+(0 if sig==-1 else 3)+v for v in range(3)],'cross indices')
    for label,gl,gu,jl,ju in x['entries']:
     ck(all(type(z)==int for z in (gl,gu,jl,ju)) and gl<=gu and jl<=ju,'interval shape');maximum=max(maximum,gu-gl,ju-jl)
     if n is None:
      j=label-396;g=F(1,4) if kind==j==0 else F(1,12) if kind==0 or j==0 else (a0*nn[kind][j]-oo[kind][j]/6)/4;z=F(0);bal=(F(1),F(1))
      if kind==j:traces[oi][0]+=2*gl;traces[oi][1]+=2*gu
     else:
      v=label%3;s=ss[n];a=A[n];b=B[n];D=(1-s*s*a)/6
      if kind==0:g=(sig*s*a*ii[0][v]+D*tt[0][v])/2;z=(b*ii[0][v]-sig*s*b*tt[0][v]/6)/2
      else:g=(-a*nn[kind][v]+D*oo[kind][v]+sig*s*a*tt[kind][v]/6)/2;z=(b*tt[kind][v]/6+sig*((c-b)*nn[kind][v]/s-s*b*oo[kind][v]/6))/2
      bal=roots[n]
     for value,lo,hi in ((g,gl,gu),(z,jl,ju)):
      ends=sorted((value*bal[0],value*bal[1]));ck(F(lo,S)<=ends[0]<=ends[1]<=F(hi,S),'independent entry enclosure')
     state['entries']+=1
  ck(index==1994 and state['entries']==5970,'all entries');ck(r['status']=='COMPLETE_APPEND_MIDPOINT_ARITHMETIC' and r['entries']==5970 and r['rows']==1995,'result census');ck(r['maximum_width']==maximum and r['append_closed_traces']==traces and r['append_arithmetic_radius']==4*798*maximum and r['radius_denominator']==r['denominator']==S,'width trace ledger')
  cache=read(plan['roles']['common_cache']['result']);ck(len(r['orbits'])==len(cache['orbits'])==5,'five orbits')
  for i,(old,new) in enumerate(zip(cache['orbits'],r['orbits'])):
   tr=[old['closed_trace'][k]+traces[i][k] for k in (0,1)];rad=F(old['arithmetic_radius'])+F(4*798*maximum,S)
   ck(old['orbit']==new['orbit']==list(ORBITS[i]) and new['closed_trace']==tr and new['raw_rows']==399 and new['closed_rows']==798 and F(new['arithmetic_radius'])==rad and 0<=tr[0]<=tr[1]<531*S and rad<=F(1,2**60),'augmented gate')
  ck(part['stage']=='gates' and part['rows']==1995 and part['entries']==5970 and part['current']==last and part['orbit_gates']==r['orbits'],'partial completion');ck(r['pure_state_computed'] is False and r['time_generator_computed'] is False,'scope')
  ck(r['physical_radius_metadata']==dict(eta_A_max='1/1000000000000000000000000000000',eta_B_max='1/10000000000000000000',eta_c_max='1/10000000000000000000',eta_a0_max='1/1000000000000000000000000000000',input_factor_bound='21/5000',compression_separate=True),'physical metadata')
  (out/'RESULT.json').write_text(json.dumps({'status':'PASS_ALL_SAVED_APPEND_ENTRIES','checks':checks,'entries':5970,'rows':1995,'scope':'exact midpoint arithmetic; physical scalar error ledger separate','oracle_calls':0,'append_calls':0,'seconds':time.monotonic()-start})+'\n')
 except BaseException as e:save(repr(e));(out/'FAILURE.json').write_text(json.dumps({'error':repr(e),'state':state})+'\n');raise
if __name__=='__main__':
 if len(sys.argv)!=3:raise SystemExit('binding output')
 main(*sys.argv[1:])
