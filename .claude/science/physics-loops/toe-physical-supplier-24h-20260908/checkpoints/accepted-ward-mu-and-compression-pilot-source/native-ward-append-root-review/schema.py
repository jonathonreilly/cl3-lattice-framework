from pathlib import Path
from fractions import Fraction as F
import json,hashlib,math
S=1<<192
ORBITS=((1,1,0),(1,0,0),(0,1,0),(0,0,2),(0,0,1))
def req(x,m):
 if not x:raise ValueError(m)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def iv(x):
 req(isinstance(x,(list,tuple)) and len(x)==2 and all(type(y) is int for y in x) and x[0]<=x[1],'integer interval');return tuple(x)
def expected():
 for oi in range(5):
  for kind in range(3):
   for n in range(66):
    for sig in(-1,1):
     yield dict(orbit_id=oi,type='append_to_pole',append_index=396+kind,pole_id=n,sigma=sig),[n*6+(0 if sig==-1 else 3)+v for v in range(3)]
  for i in range(3):yield dict(orbit_id=oi,type='append_self',append_index=396+i),list(range(396+i,399))
def check(out,freeze,elapsed):
 out=Path(out);r=json.loads((out/'RESULT.json').read_text());w=json.loads((out/'WORKER_COMPLETE.json').read_text());p=json.loads((out/'PARTIAL.json').read_text())
 req(w['status']=='COMPLETE_APPEND_MIDPOINT_ONLY' and w['freeze_sha256']==freeze and w['result_sha256']==sha(out/'RESULT.json'),'worker identity')
 plan_path=out.parent/'native-ward-insertion-append-runtime/BINDING.json';plan=json.loads(plan_path.read_text());req(w['binding_sha256']==sha(plan_path),'binding identity')
 old=json.loads(Path(plan['roles']['common_cache']['result']).read_text())
 req(r['status']=='COMPLETE_APPEND_MIDPOINT_ARITHMETIC' and r['entries']==5970 and r['rows']==1995 and r['denominator']==S and r['radius_denominator']==S,'fixed scope')
 req(r['append_sha256']==sha(out/'APPEND.ndjson'),'append stream hash')
 req(all(type(x) in(int,float) and math.isfinite(x) and 0<x for x in(r['seconds'],w['seconds'],elapsed)) and r['seconds']<=w['seconds']<=elapsed<=30,'timing')
 req(type(w['rss_bytes']) is int and 0<w['rss_bytes']<=384*1048576,'worker RSS')
 count=rows=maxwidth=0;traces=[[0,0] for _ in range(5)];last=None
 with(out/'APPEND.ndjson').open() as stream:
  for meta,indices in expected():
   line=stream.readline();req(bool(line),'complete stream');d=json.loads(line);req({k:v for k,v in d.items() if k!='entries'}==meta,'row identity/order');es=d['entries'];req([x[0] for x in es]==indices,'entry identity/order')
   for e in es:
    req(isinstance(e,list) and len(e)==5 and all(type(v) is int for v in e),'entry shape');g=iv(e[1:3]);j=iv(e[3:5]);maxwidth=max(maxwidth,g[1]-g[0],j[1]-j[0]);count+=1
    if meta['type']=='append_self':
     req(j==(0,0),'exact self J')
     if e[0]==meta['append_index']:
      req(g[0]>=0,'self positivity');traces[meta['orbit_id']][0]+=2*g[0];traces[meta['orbit_id']][1]+=2*g[1]
   req(4*798*maxwidth<=S//2**60,'per-row arithmetic gate');rows+=1;last=meta
  req(not stream.read(),'extra stream rows')
 req(count==5970 and rows==1995 and r['maximum_width']==maxwidth,'final census/width')
 req(r['append_closed_traces']==traces and r['append_arithmetic_radius']==4*798*maxwidth,'append trace/radius')
 req(len(r['orbits'])==5 and len(old['orbits'])==5,'five orbits')
 for i,(a,c) in enumerate(zip(r['orbits'],old['orbits'])):
  req(a['orbit']==c['orbit']==list(ORBITS[i]) and a['raw_rows']==399 and a['closed_rows']==798,'orbit identity')
  trace=iv(a['closed_trace']);ct=iv(c['closed_trace']);req(trace==(ct[0]+traces[i][0],ct[1]+traces[i][1]) and 0<=trace[0]<=trace[1]<531*S,'augmented trace')
  radius=F(c['arithmetic_radius'])+F(4*798*maxwidth,S);req(F(a['arithmetic_radius'])==radius and radius<=F(1,2**60),'combined arithmetic radius')
 req(p['stage']=='gates' and p['rows']==1995 and p['entries']==5970 and p['current']==last and p['orbit_gates']==r['orbits'],'final retained partial')
 req(r['pure_state_computed'] is False and r['time_generator_computed'] is False and r['physical_radius_metadata']['compression_separate'] is True,'scope boundaries')
 req(r['physical_radius_metadata']==dict(eta_A_max='1/1000000000000000000000000000000',eta_B_max='1/10000000000000000000',eta_c_max='1/10000000000000000000',eta_a0_max='1/1000000000000000000000000000000',input_factor_bound='21/5000',compression_separate=True),'fixed physical ledger metadata')
 return dict(status='PASS_COMPLETE_WARD_APPEND_MIDPOINT_SCHEMA',result_sha256=sha(out/'RESULT.json'),entries=count,rows=rows,orbits=5,pure_state_computed=False,time_generator_computed=False,independent_entry_arithmetic_recomputed=False)
