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
     yield dict(orbit_id=oi,type='bare_to_pole',append_index=399+kind,pole_id=n,sigma=sig),[n*6+(0 if sig==-1 else 3)+v for v in range(3)]
   yield dict(orbit_id=oi,type='bare_to_insertion',append_index=399+kind),list(range(396,399))
  for i in range(3):yield dict(orbit_id=oi,type='bare_self',append_index=399+i),list(range(399+i,402))
def check(out,rf,elapsed):
 freeze=rf["worker_freeze"]
 out=Path(out);r=json.loads((out/'RESULT.json').read_text());w=json.loads((out/'WORKER_COMPLETE.json').read_text());p=json.loads((out/'PARTIAL.json').read_text())
 req(w['status']=='COMPLETE_FIRST_ACTION_DATA_APPEND_ONLY' and w['freeze_sha256']==freeze and w['result_sha256']==sha(out/'RESULT.json'),'worker identity')
 plan_path=out.parent/'native-minimal-first-action-append-design/BINDING.json';plan=json.loads(plan_path.read_text());req(w['binding_sha256']==sha(plan_path),'binding identity')
 old=json.loads(Path(plan['ward']['result']).read_text())
 req(r['status']=='COMPLETE_FIRST_ACTION_DATA_APPEND_MIDPOINT_ONLY' and r['entries']==6015 and r['rows']==2010 and r['denominator']==S,'fixed scope')
 req(r['append_sha256']==sha(out/'FIRST_ACTION_APPEND.ndjson'),'append stream hash')
 req(all(type(x) in(int,float) and math.isfinite(x) and 0<x for x in(r['seconds'],w['seconds'],elapsed)) and r['seconds']<=w['seconds']<29 and w['seconds']<=elapsed<=30,'timing')
 req(type(w['rss_bytes']) is int and 0<w['rss_bytes']<=384*1048576,'worker RSS')
 count=rows=maxwidth=0;traces=[[0,0] for _ in range(5)];last=None
 with(out/'FIRST_ACTION_APPEND.ndjson').open() as stream:
  for meta,indices in expected():
   line=stream.readline();req(bool(line),'complete stream');d=json.loads(line);req({k:v for k,v in d.items() if k!='entries'}==meta,'row identity/order');es=d['entries'];req([x[0] for x in es]==indices,'entry identity/order')
   for e in es:
    req(isinstance(e,list) and len(e)==5 and all(type(v) is int for v in e),'entry shape');g=iv(e[1:3]);j=iv(e[3:5]);maxwidth=max(maxwidth,g[1]-g[0],j[1]-j[0]);count+=1
    if meta['type']=='bare_self':
     req(j==(0,0),'exact self J')
     if e[0]==meta['append_index']:
      req(g[0]>=0,'self positivity');traces[meta['orbit_id']][0]+=2*g[0];traces[meta['orbit_id']][1]+=2*g[1]
   req(4*804*maxwidth<=S//2**60,'per-row arithmetic gate');rows+=1;last=meta
  req(not stream.read(),'extra stream rows')
 req(count==6015 and rows==2010 and r['maximum_width']==maxwidth,'final census/width')
 req(r['append_closed_traces']==traces and r['append_arithmetic_radius']==4*804*maxwidth,'append trace/radius')
 req(len(r['orbits'])==5 and len(old['orbits'])==5,'five orbits')
 for i,(a,c) in enumerate(zip(r['orbits'],old['orbits'])):
  req(a['orbit']==c['orbit']==list(ORBITS[i]) and a['data_raw_rows']==402 and a['data_closed_rows']==804 and a['original_raw_rows']==399 and a['original_closed_rows']==798 and c['raw_rows']==399 and c['closed_rows']==798,'orbit identity')
  trace=iv(a['closed_trace']);ct=iv(c['closed_trace']);req(trace==(ct[0]+traces[i][0],ct[1]+traces[i][1]) and 0<=trace[0]<=trace[1]<536*S,'augmented trace')
  radius=F(c['arithmetic_radius'])+F(4*804*maxwidth,S);req(F(a['arithmetic_radius'])==radius and radius<=F(1,2**60),'combined arithmetic radius')
 req(p['stage']=='combined_gates' and p['rows']==2010 and p['entries']==6015 and p['current']==last and p['orbit_gates']==r['orbits'],'final retained partial')
 req(all(r[k] is False for k in ('generator_assembled','leakage_computed','propagation_computed')) and w['generator_assembled'] is False and w['leakage_computed'] is False,'scope')
 mu=json.loads(Path(plan['mu']['result']).read_text());lo,hi=map(F,mu['interval']);meta={'eta_mu':str((hi-lo)/2),'mu_interval':mu['interval']}
 req(0<lo<=hi<4 and (hi-lo)/2<=F(1,10**19) and r['physical_input_metadata']==meta and p['mu_metadata']==meta,'mu metadata')
 req(all(tuple(t)==(5*S,5*S) for t in traces),'exact new trace5')
 req(json.loads((out/'STARTED.json').read_text())==rf['authorization'],'startup authorization')
 req(not any((out/n).exists() for n in ('FAILURE.json','DISPATCH_FAILURE.json')),'no failures')
 return dict(status='PASS_COMPLETE_FIRST_ACTION_APPEND_SCHEMA',result_sha256=sha(out/'RESULT.json'),entries=count,rows=rows,orbits=5,generator_assembled=False,independent_entry_arithmetic_recomputed=False)
