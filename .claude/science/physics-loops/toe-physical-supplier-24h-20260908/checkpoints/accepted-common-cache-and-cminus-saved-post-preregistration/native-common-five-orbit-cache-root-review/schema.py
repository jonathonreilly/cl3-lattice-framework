from pathlib import Path
from fractions import Fraction as F
import hashlib,json,math
S=1<<192;TYPES=('cc','cd','P','O','cross');ORBITS=((1,1,0),(1,0,0),(0,1,0),(0,0,2),(0,0,1))
def req(x,m):
 if not x:raise ValueError(m)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def check(out,freeze,elapsed):
 out=Path(out);r=json.loads((out/'RESULT.json').read_text());w=json.loads((out/'WORKER_COMPLETE.json').read_text());p=json.loads((out/'PARTIAL.json').read_text());start=json.loads((out/'STARTED.json').read_text())
 req(w['status']=='COMPLETE_MIDPOINT_CACHE_ONLY' and w['freeze_sha256']==freeze==start['runtime_sha256'] and w['binding_sha256']==start['binding_sha256'] and w['result_sha256']==sha(out/'RESULT.json'),'source result binding')
 req(r['status']=='COMPLETE_COMMON_CACHE_MIDPOINT_ARITHMETIC' and r['entries']==52536 and r['raw_rows']==396 and r['closed_rows']==792 and r['coefficients']==132,'fixed census')
 req(r['physical_error_ledger_certified'] is False and r['pure_projector_computed'] is False and r['physical_error_ledger']=='separate and required','scope')
 req(all(isinstance(t,(int,float)) and math.isfinite(t) and t>0 for t in [r['seconds'],w['seconds'],elapsed]) and r['seconds']<=w['seconds']<=elapsed<=60,'inclusive time');req(0<w['rss_bytes']<=384*1048576,'worker RSS')
 req(r['cache_sha256']==sha(out/'CACHE.ndjson') and r['coefficient_sha256']==sha(out/'COEFFICIENTS.ndjson'),'retained streams');req(p['stage']=='five_orbit_gates' and p['coefficients']==132 and p['completed_cache_rows']==660 and p['entries']==52536,'partial')
 with(out/'COEFFICIENTS.ndjson').open() as f:
  for j,line in enumerate(f):
   c=json.loads(line);req(j<132 and c['kind']==('P' if j<66 else 'O') and c['id']==j%66,'coefficient ids');req(len(c['det'])==2 and 0<c['det'][0]<=c['det'][1],'positive determinant')
   for key in ('signed','residual'):
    req(len(c[key])==2 and all(len(row)==2 for row in c[key]),'2x2 coefficient')
    for row in c[key]:
     for x in row:
      req(len(x)==2 and all(isinstance(v,int) for v in x) and x[0]<=x[1],'coefficient interval')
      if key=='signed':req(x[1]-x[0]<=S//2**40,'coefficient width')
      else:req(x[0]<=0<=x[1] and 2*max(abs(x[0]),abs(x[1]))<=S//2**40,'inverse residual operator')
 req(j==131,'all coefficients');count=0;maxwidth=0;tr={t:[0,0] for t in ('cc','P','O')}
 with(out/'CACHE.ndjson').open() as f:
  for k,line in enumerate(f):
   x=json.loads(line);typ=TYPES[k//132] if k<660 else None;i=k%132;req(x['type']==typ and x['i']==i,'cache row');req([v[0] for v in x['entries']]==list(range(0 if typ=='cd' else i,132)),'cache indices')
   for j,gl,gu,jl,ju in x['entries']:
    req(all(isinstance(z,int) for z in [gl,gu,jl,ju]) and gl<=gu and jl<=ju,'cache interval');maxwidth=max(maxwidth,gu-gl,ju-jl);count+=1
    if j==i and typ!='cd':req(jl==ju==0,'skew diagonal')
    if j==i and typ in tr:tr[typ][0]+=gl;tr[typ][1]+=gu
   req(x['count']==count and x['max_width']==maxwidth,'running stream counts')
 req(k==659 and count==52536 and p['maximum_width']==maxwidth,'complete stream');radius=F(2*792*maxwidth,S);req(radius==F(r['arithmetic_radius'])<=F(1,2**60),'common rounding radius')
 req(len(r['orbits'])==5,'all orbits')
 for o,expected in zip(r['orbits'],ORBITS):
  a,b,c=expected;trace=[2*(tr['cc'][i]+tr['O' if a else 'P'][i]+tr['O' if b else 'P'][i]) for i in(0,1)]
  req(o['orbit']==list(expected) and o['closed_trace']==trace and o['denominator']==S and o['raw_rows']==396 and o['closed_rows']==792 and F(o['arithmetic_radius'])==radius,'orbit binding');req(0<=trace[0]<=trace[1]<529*S,'orbit trace')
 return {'status':'PASS_COMPLETE_MIDPOINT_CACHE_SCHEMA','result_sha256':sha(out/'RESULT.json'),'entries':52536,'coefficients':132,'orbits':5,'physical_input_error_separate':True,'projector_or_alpha_computed':False}
