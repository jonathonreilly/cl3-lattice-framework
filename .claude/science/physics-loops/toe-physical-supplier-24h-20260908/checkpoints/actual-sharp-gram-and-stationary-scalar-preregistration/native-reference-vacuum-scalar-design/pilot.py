import json,gzip,hashlib,time
from pathlib import Path
from fractions import Fraction as F
from core import integrate
P=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load_inputs():
 inp=json.loads((P/'INPUTS.json').read_text());r=json.loads(Path(inp['B_result']).read_text());w=json.loads(Path(inp['B_complete']).read_text());a=json.loads(Path(inp['B_acceptance']).read_text())
 if not (sha(inp['B_result'])==w['result_sha256']==a['result_sha256'] and w['status']=='COMPLETE' and a['status'].startswith('ACCEPTED_')):raise ValueError('accepted B binding')
 if w['freeze_sha256']!=sha(inp['B_freeze']):raise ValueError('B source freeze')
 raw=gzip.decompress(Path(inp['catalogue']).read_bytes())
 if hashlib.sha256(raw).hexdigest()!=inp['decompressed_sha256']:raise ValueError('catalogue raw hash')
 c=json.loads(raw);g=json.loads(Path(inp['gauss']).read_text())
 if set(c)!={f'{i:04d}.json' for i in range(746)} or len(g['rule'])!=12:raise ValueError('fixed catalogue/rule coverage')
 for row in c.values():
  if row['terms']!=160 or row['derivative_side']!='ordinary' or row['status']!='CERTIFIED_TARGET' or len(row['widths'])!=2:raise ValueError('oracle schema')
  for key,width in zip(('A','Aprime'),row['widths']):
   lo,hi=map(F,row[key])
   if not 0<=hi-lo==F(width)<=F(1,10**30):raise ValueError('oracle interval width')
 n=2
 for j in range(-28,3):
  scale=F(2)**j
  for nodes,weights in g['rule']:
   if len(nodes)!=2 or len(weights)!=2 or not 0<F(weights[0])<=F(weights[1]):raise ValueError('rule shape')
   for x in nodes:
    if F(c[f'{n:04d}.json']['s'])!=scale*(3+F(x))/2:raise ValueError('node binding')
    n+=1
 if n!=746:raise ValueError('all endpoints')
 return c,g
def run(out):
 start=time.monotonic();out.mkdir(exist_ok=False)
 def save(x):
  (out/'PARTIAL.json').write_text(json.dumps(dict(x,elapsed_seconds=time.monotonic()-start),indent=2)+'\n')
 c,g=load_inputs();result=integrate(c,g,save);result['elapsed_seconds']=time.monotonic()-start;result['input_hashes']={k:sha(v) for k,v in json.loads((P/'INPUTS.json').read_text()).items() if k!='decompressed_sha256'}
 (out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
