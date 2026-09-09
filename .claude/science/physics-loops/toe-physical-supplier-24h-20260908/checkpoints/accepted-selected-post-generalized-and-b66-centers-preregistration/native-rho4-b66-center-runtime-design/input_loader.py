import json,hashlib
from pathlib import Path
from fractions import Fraction as F
from interval import rnd

def sha(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def read(path,h):
 if sha(path)!=h:raise ValueError('input hash '+str(path))
 return json.loads(Path(path).read_text())
def bundle(b,expected):
 p=Path(b['directory']);a=read(b['acceptance_path'],b['acceptance_sha256']);r=read(p/'RESULT.json',b['result_sha256']);w=read(p/'WORKER_COMPLETE.json',b['worker_complete_sha256'])
 if not a['status'].startswith('ACCEPTED_') or a['result_sha256']!=b['result_sha256'] or a['worker_freeze']!=b['source_freeze_sha256']:raise ValueError('root acceptance')
 if w['status']!='COMPLETE' or w['result_sha256']!=b['result_sha256'] or w['freeze_sha256']!=b['source_freeze_sha256']:raise ValueError('worker completion')
 if r['status']!=expected:raise ValueError('scientific status')
 return r

def load(b):
 poles=read(b['poles_path'],b['poles_sha256'])['rows'];g=read(b['catalog_geometry_path'],b['catalog_geometry_sha256'])
 a66=bundle(b['a66'],'COMPLETE_FIXED_66_ORACLES')['rows'];cat=bundle(b['catalog'],'COMPLETE_FIXED_3484_CATALOG')['rows']
 if [r['id'] for r in a66]!=list(range(66)) or [r['id'] for r in cat]!=list(range(3484)):raise ValueError('row ids')
 if len(poles)!=66 or len(g['nodes'])!=1742 or len(g['endpoints'])!=3484:raise ValueError('geometry census')
 for p,r in zip(poles,a66):
  if r['gate']!='PASS' or r['oracle']['s']!=p['s_midpoint'] or max(map(F,r['oracle']['widths']))>F(1,10**30):raise ValueError('A66 gate')
 endpoint=[]
 for e,r in zip(g['endpoints'],cat):
  if r['gate']!='PASS' or r['path']!=f"ORACLES/{r['id']:04d}.json":raise ValueError('catalog row gate/path')
  x=read(Path(b['catalog']['directory'])/r['path'],r['sha256'])
  if x['catalog_endpoint']!=e or x['s']!=e['s'] or max(map(F,x['widths']))>F(1,10**30):raise ValueError('catalog raw gate')
  endpoint.append(tuple(map(F,x['A'])))
 catalog=[]
 for n in g['nodes']:
  l,u=n['endpoint_ids'];lo,hi=map(F,n['t_interval']);at=(endpoint[u][0],endpoint[l][1])
  if lo>=hi or at[0]>at[1]:raise ValueError('node enclosure')
  # Geometry weights ALREADY include panel a/2. Round once, never remap again.
  wl,wu=map(F,n['weight']);weight=rnd(wl,wu)
  catalog.append({'id':n['id'],'panel':n['panel'],'t_interval':(lo,hi),'A_interval':at,'weight_interval':weight})
 return poles,a66,catalog
