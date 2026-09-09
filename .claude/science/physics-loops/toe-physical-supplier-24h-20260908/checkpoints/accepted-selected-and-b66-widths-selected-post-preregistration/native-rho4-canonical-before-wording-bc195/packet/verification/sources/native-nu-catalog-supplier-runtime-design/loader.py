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
 g=read(b['catalog_geometry_path'],b['catalog_geometry_sha256'])
 cat=bundle(b['catalog'],'COMPLETE_FIXED_3484_CATALOG')['rows']
 if len(g['nodes'])!=1742 or len(g['endpoints'])!=3484 or [r['id'] for r in cat]!=list(range(3484)):raise ValueError('catalog census')
 endpoint=[]
 for e,r in zip(g['endpoints'],cat):
  if r['gate']!='PASS' or r['path']!=f"ORACLES/{r['id']:04d}.json":raise ValueError('row gate')
  x=read(Path(b['catalog']['directory'])/r['path'],r['sha256'])
  if x['catalog_endpoint']!=e or x['s']!=e['s'] or len(x['A'])!=2 or max(map(F,x['widths']))>F(1,10**30):raise ValueError('raw endpoint')
  aa=tuple(map(F,x['A']))
  if aa[0]>aa[1]:raise ValueError('A order')
  endpoint.append(aa)
 catalog=[]
 for n in g['nodes']:
  l,u=n['endpoint_ids'];lo,hi=map(F,n['t_interval']);at=(endpoint[u][0],endpoint[l][1]);wl,wu=map(F,n['weight'])
  if not 0<lo<hi<=8 or hi-lo>F(1,2**140) or wu-wl>F(1,10**38) or at[0]>at[1] or not 0<wl<=wu:raise ValueError('node enclosure')
  catalog.append({'id':n['id'],'panel':n['panel'],'t_interval':(lo,hi),'A_interval':at,'weight_interval':rnd(wl,wu)})
 if sum(x['weight_interval'][1] for x in catalog)>9:raise ValueError('weight sum')
 return catalog
