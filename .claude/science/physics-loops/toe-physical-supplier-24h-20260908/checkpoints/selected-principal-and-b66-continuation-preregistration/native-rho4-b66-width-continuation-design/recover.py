"""Authenticate completed pole0 stream; no node-width formula."""
import json,hashlib
from pathlib import Path
from fractions import Fraction as F
import caps
Q=1<<256
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def load(c,out):
 for p,h in c['inputs'].items():
  if sha(p)!=h:raise ValueError('prior immutable input')
 failure=json.loads(Path(c['failure']).read_text());partial=json.loads(Path(c['partial']).read_text());receipt=json.loads(Path(c['receipt']).read_text())
 if failure['node_checks']!=1742 or failure['completed']!=[] or failure['current']!={'stage':'node','pole':0,'node':1741}or '4300 digits'not in failure['error']:raise ValueError('specific prior failure')
 if receipt['pass']is not False or receipt['returncode']!=1 or receipt['worker_freeze']!=c['worker_freeze']:raise ValueError('prior failed receipt')
 if partial['node_checks']!=1742 or partial['poles']!=[]:raise ValueError('prior partial')
 total=[F(0),F(0)];separated=True;count=0
 with Path(c['nodes']).open('rb')as src,(out/'RECOVERED_NODES_00.ndjson').open('xb')as dst:
  for raw in src:
   d=json.loads(raw)
   if type(d['node'])is not int or d['node']!=count or type(d['panel'])is not int or d['panel']!=count//26-64:raise ValueError('recovered order')
   rr=tuple(map(F,d['radii']))
   if len(rr)!=2 or any(x<0 or (x*Q).denominator!=1 for x in rr):raise ValueError('grid radii')
   caps.tree(rr);info=d['info']
   if 'separation_failure'in info:
    if info['separation_failure']!='denominator does not separate' or rr!=(0,0):raise ValueError('separation failure')
    separated=False
   elif F(info['denominator_lower_abs'])<=0:raise ValueError('separation')
   total=[caps.guard(total[k]+rr[k])for k in range(2)]
   if tuple(map(F,d['cumulative_radii']))!=tuple(total):raise ValueError('cumulative')
   dst.write(raw);count+=1
 if count!=1742 or sha(out/'RECOVERED_NODES_00.ndjson')!=c['inputs'][c['nodes']]:raise ValueError('recovered full stream')
 return total,separated
