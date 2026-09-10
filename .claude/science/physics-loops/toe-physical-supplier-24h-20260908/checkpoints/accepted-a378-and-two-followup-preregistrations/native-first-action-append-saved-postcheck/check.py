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
  ck(accept['status']=='ACCEPTED_FIRST_ACTION_DATA_APPEND_MIDPOINT_ARITHMETIC' and accept['result_sha256']==sha(study/'RESULT.json') and accept['append_sha256']==sha(study/'FIRST_ACTION_APPEND.ndjson') and accept['worker_freeze']==cfg['worker_freeze'] and accept['root_freeze']==sha(cfg['root_freeze_path']),'actual acceptance')
  ck(w['status']=='COMPLETE_FIRST_ACTION_DATA_APPEND_ONLY' and w['freeze_sha256']==cfg['worker_freeze'] and w['result_sha256']==sha(study/'RESULT.json'),'worker binding')
  ck(sha(cfg['root_acceptance'])==cfg['root_acceptance_sha256'],'accepted receipt')
  raw=Path(cfg['root_stderr']).read_text().splitlines();wall=[F(z.split()[1]) for z in raw if z.strip().startswith('real ')];rss=[int(z.split()[0]) for z in raw if 'maximum resident set size' in z]
  ck(len(wall)==len(rss)==1 and wall[0]==F(str(accept['external_seconds'])) and rss[0]==accept['external_max_rss'],'external shell receipt')
  ck(not any((study/n).exists() for n in ('FAILURE.json','DISPATCH_FAILURE.json')),'producer failure absence')
  plan=read(cfg['plan'])
  for path,h in plan['inputs'].items():ck(cfg['files'].get(path)==h,'full plan closure')
  ck(w['binding_sha256']==sha(cfg['plan']),'plan identity');app=read(plan['append_binding']);pole=read(app['pole_binding']);arows=read(pole['a_result'])['rows'];brows=read(pole['summary'])['rows'];pr=read(pole['poles'])['rows'];pi=sum(map(F,pole['pi_interval']))/2
  def scalar(role):
   obj=read(app['roles'][role]['result'])
   for k in app['roles'][role]['interval_path']:obj=obj[k]
   return sum(map(F,obj))/2
  a0,c=scalar('a0'),scalar('cminus');murow=read(plan['mu']['result']);mu=sum(map(F,murow['interval']))/2;A=[sum(map(F,x['oracle']['A']))/2 for x in arows];B=[sum(map(F,x['B']))/2 for x in brows];ss=[F(x['s_midpoint']) for x in pr];alpha=[35*sum(map(F,x['weight']))/(4*pi) for x in pr];roots=[]
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
   oldv=[[F(1)]+[F(0)]*6,vec(aa),vec(cc)];newv=[vec(aa),vec(cc),vec(range(1,7))]
   geom.append(([[[dot(M,u,v) for v in oldv] for u in newv] for M in (I,O,T,N)],[[dot(I,u,v) for v in newv] for u in newv]))
  expected=[]
  for oi in range(5):
   for kind in range(3):
    for n in range(66):
     for sig in(-1,1):expected.append((oi,kind,n,sig,'bare_to_pole'))
    expected.append((oi,kind,None,None,'bare_to_insertion'))
   for kind in range(3):expected.append((oi,kind,None,None,'bare_self'))
  ck(len(expected)==2010,'fixed rows');maximum=0;traces=[[0,0] for _ in range(5)]
  ck(str(study/'FIRST_ACTION_APPEND.ndjson') in cfg['files'] and sha(study/'FIRST_ACTION_APPEND.ndjson')==r['append_sha256'],'stream hash')
  index=-1;last=None
  with(study/'FIRST_ACTION_APPEND.ndjson').open() as stream:
   for index,line in enumerate(stream):
    state.update(stage='row_parse',row=index);save();ck(index<2010,'extra row');x=json.loads(line);last={k:v for k,v in x.items() if k!='entries'};oi,kind,n,sig,typ=expected[index];(ii,oo,tt,nn),selfg=geom[oi]
    ck(type(x['orbit_id'])is int and type(x['append_index'])is int and x['orbit_id']==oi and x['append_index']==399+kind and x['type']==typ,'row labels');state['stage']='row_arithmetic';save()
    indices=list(range(399+kind,402)) if typ=='bare_self' else list(range(396,399)) if typ=='bare_to_insertion' else [6*n+(0 if sig==-1 else 3)+v for v in range(3)]
    ck([e[0] for e in x['entries']]==indices,'entry labels')
    if n is not None:ck(type(x['pole_id'])is int and type(x['sigma'])is int and x['pole_id']==n and x['sigma']==sig,'pole labels')
    for label,gl,gu,jl,ju in x['entries']:
     ck(all(type(z)is int for z in (label,gl,gu,jl,ju)) and gl<=gu and jl<=ju,'integer intervals');maximum=max(maximum,gu-gl,ju-jl)
     if typ=='bare_self':
      v=label-399;g=selfg[kind][v]/4;z=F(0);bal=(F(1),F(1))
      if v==kind:traces[oi][0]+=2*gl;traces[oi][1]+=2*gu
     elif typ=='bare_to_insertion':
      v=label-396;g=F(0);z=-mu*tt[kind][v]/24 if v==0 else -c*nn[kind][v]/4+mu*oo[kind][v]/24;bal=(F(1),F(1))
     else:
      v=label%3;s=ss[n];a=A[n];bb=B[n];D=(1-s*s*a)/6
      g=(sig*s*(a*nn[kind][v]-D*oo[kind][v])+D*tt[kind][v])/2
      z=(bb*nn[kind][v]-(mu-s*s*bb)*oo[kind][v]/6-sig*s*bb*tt[kind][v]/6)/2;bal=roots[n]
     for value,lo,hi in ((g,gl,gu),(z,jl,ju)):
      ends=sorted((value*bal[0],value*bal[1]));ck(F(lo,S)<=ends[0]<=ends[1]<=F(hi,S),'independent entry enclosure')
     state['entries']+=1
  ck(index==2009 and state['entries']==6015,'all entries');ck(r['status']=='COMPLETE_FIRST_ACTION_DATA_APPEND_MIDPOINT_ONLY' and r['entries']==6015 and r['rows']==2010,'result census');ck(r['maximum_width']==maximum and r['append_closed_traces']==traces and r['append_arithmetic_radius']==4*804*maximum and r['denominator']==S,'width trace ledger')
  cache=read(plan['ward']['result']);ck(len(r['orbits'])==len(cache['orbits'])==5,'five orbits')
  for i,(old,new) in enumerate(zip(cache['orbits'],r['orbits'])):
   tr=[old['closed_trace'][k]+traces[i][k] for k in (0,1)];rad=F(old['arithmetic_radius'])+F(4*804*maximum,S)
   ck(old['orbit']==new['orbit']==list(ORBITS[i]) and new['closed_trace']==tr and new['data_raw_rows']==402 and new['data_closed_rows']==804 and new['original_raw_rows']==399 and new['original_closed_rows']==798 and F(new['arithmetic_radius'])==rad and 0<=tr[0]<=tr[1]<536*S and rad<=F(1,2**60),'augmented gate')
  ck(part['stage']=='combined_gates' and part['rows']==2010 and part['entries']==6015 and part['current']==last and part['orbit_gates']==r['orbits'],'partial completion')
  ck(all(r[k] is False for k in ('generator_assembled','leakage_computed','propagation_computed')),'scope')
  meta={'eta_mu':str((F(murow['interval'][1])-F(murow['interval'][0]))/2),'mu_interval':murow['interval']}
  ck(r['physical_input_metadata']==meta and part['mu_metadata']==meta,'mu metadata')
  ck(all(t==[5*S,5*S] for t in traces),'exact additional trace5')
  for path,digest in cfg['files'].items():ck(sha(path)==digest,'final immutable input '+path)
  (out/'RESULT.json').write_text(json.dumps({'status':'PASS_ALL_SAVED_APPEND_ENTRIES','checks':checks,'entries':6015,'rows':2010,'scope':'exact midpoint arithmetic; physical scalar error ledger separate','oracle_calls':0,'append_calls':0,'seconds':time.monotonic()-start})+'\n')
 except BaseException as e:save(repr(e));(out/'FAILURE.json').write_text(json.dumps({'error':repr(e),'state':state})+'\n');raise
if __name__=='__main__':
 if len(sys.argv)!=3:raise SystemExit('binding output')
 main(*sys.argv[1:])
