import json,hashlib
from pathlib import Path
from fractions import Fraction as F
import re,math
from interval import rnd

def scalar(x):
 if type(x)is not str or len(x)>40000 or re.fullmatch(r'-?\d+(?:/\d+)?',x)is None:raise ValueError('bounded scalar syntax')
 v=F(x)
 if str(v)!=x or max(abs(v.numerator).bit_length(),v.denominator.bit_length())>50000:raise ValueError('bounded scalar')
 return v
def pair(x):
 if type(x)is not list or len(x)!=2:raise ValueError('pair shape')
 a,b=map(scalar,x)
 if a>b:raise ValueError('pair order')
 return a,b
def integer(x,v):
 if type(x)is not int or x!=v:raise ValueError('literal integer')
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
 root=read(b['root_freeze_path'],b['root_freeze_sha256']);receipt=read(b['root_receipt_path'],b['root_receipt_sha256'])
 if root['worker_freeze']!=b['source_freeze_sha256']or type(root['seconds'])is not int or root['seconds']!=180 or type(root['rss_bytes'])is not int or root['rss_bytes']!=384*1048576:raise ValueError('original root contract')
 if receipt['pass']is not True or type(receipt['returncode'])is not int or receipt['returncode']!=0 or receipt['worker_freeze']!=b['source_freeze_sha256']:raise ValueError('original root completion')
 for value in [a['external_shell_seconds'],a['external_conservative_seconds'],receipt['seconds'],w['seconds']]:
  if type(value)not in(int,float)or not math.isfinite(value)or not 0<value<=180:raise ValueError('original finite timing')
 for value in [a['external_max_rss'],a['sampled_whole_tree_peak'],receipt['sampled_whole_tree_peak']]:
  if type(value)is not int or not 0<value<=384*1048576:raise ValueError('original integer RSS')
 if receipt['sampled_whole_tree_peak']!=a['sampled_whole_tree_peak']:raise ValueError('original resource binding')
 if a['status']!='ACCEPTED_EXECUTION_COMPLETE' or a['result_sha256']!=b['result_sha256'] or a['worker_freeze']!=b['source_freeze_sha256']:raise ValueError('root acceptance')
 if w['status']!='COMPLETE' or w['result_sha256']!=b['result_sha256'] or w['freeze_sha256']!=b['source_freeze_sha256']:raise ValueError('worker completion')
 if r['status']!=expected:raise ValueError('scientific status')
 return r

def load(b,progress=lambda *args:None):
 g=read(b['catalog_geometry_path'],b['catalog_geometry_sha256'])
 cat=bundle(b['catalog'],'COMPLETE_FIXED_3484_CATALOG')['rows']
 if len(g['nodes'])!=1742 or len(g['endpoints'])!=3484 or [r['id'] for r in cat]!=list(range(3484)):raise ValueError('catalog census')
 endpoint=[]
 for eid,(e,r) in enumerate(zip(g['endpoints'],cat)):
  progress('endpoint',{'id':eid});integer(e['id'],eid);integer(r['id'],eid)
  if r['gate']!='PASS' or r['path']!=f"ORACLES/{r['id']:04d}.json":raise ValueError('row gate')
  x=read(Path(b['catalog']['directory'])/r['path'],r['sha256'])
  if x['catalog_endpoint']!=e or x['s']!=e['s'] or len(x['A'])!=2 or type(x['widths'])is not list or len(x['widths'])!=2 or max(map(scalar,x['widths']))>F(1,10**30):raise ValueError('raw endpoint')
  aa=pair(x['A']);ap=pair(x['Aprime'])
  if any(max(abs(y.numerator).bit_length(),y.denominator.bit_length())>512 for y in aa):raise ValueError('A arithmetic cap')
  if list(map(scalar,x['widths']))!=[aa[1]-aa[0],ap[1]-ap[0]]:raise ValueError('raw width identity')
  if aa[0]>aa[1]:raise ValueError('A order')
  endpoint.append(aa)
 catalog=[]
 for nid,n in enumerate(g['nodes']):
  progress('mapped_node',{'id':nid});integer(n['id'],nid);integer(n['panel'],nid//26-64)
  if n['endpoint_ids']!=[2*nid,2*nid+1]or any(type(x)is not int for x in n['endpoint_ids']):raise ValueError('endpoint linkage')
  l,u=n['endpoint_ids'];lo,hi=pair(n['t_interval']);at=(endpoint[u][0],endpoint[l][1]);wl,wu=pair(n['weight'])
  if any(max(abs(y.numerator).bit_length(),y.denominator.bit_length())>512 for y in (lo,hi)):raise ValueError('node arithmetic cap')
  if not 0<lo<hi<=8 or hi-lo>F(1,2**140) or wu-wl>F(1,10**38) or at[0]>at[1] or at[1]-at[0]>F(3,10**30) or not 0<=at[0]<=at[1]<F(1,3) or not 0<wl<=wu:raise ValueError('node enclosure')
  catalog.append({'id':n['id'],'panel':n['panel'],'t_interval':(lo,hi),'A_interval':at,'weight_interval':rnd(wl,wu)})
 if sum(x['weight_interval'][1] for x in catalog)>9:raise ValueError('weight sum')
 return catalog

def reused_moments(b,progress):
 z=b['omega5']
 def get(role):
  progress('before_omega5_input',{'role':role});p=z[role];return read(p['path'],p['sha256'])
 a=get('acceptance');root=get('root');receipt=get('receipt');done=get('worker');result=get('result');oldbinding=get('binding')
 if a['status']!='ACCEPTED_NEW_NATIVE_OMEGA5_ROOT_REVIEW_ONCE'or a['once']is not True:raise ValueError('omega5 acceptance')
 if a['worker_freeze']!=z['worker_freeze']or done['runtime_sha256']!=z['worker_freeze']or receipt['worker_freeze']!=z['worker_freeze']or root['worker_freeze']!=z['worker_freeze']:raise ValueError('omega5 worker linkage')
 if a['root_freeze']!=z['root']['sha256']or done['binding_sha256']!=z['binding']['sha256']or a['result_sha256']!=z['result']['sha256']or done['result_sha256']!=z['result']['sha256']:raise ValueError('omega5 output linkage')
 if done['status']!='COMPLETE_NEW_OMEGA5_ONLY'or result['status']!='CERTIFIED_TARGET'or receipt['pass']is not True or type(receipt['returncode'])is not int or receipt['returncode']!=0:raise ValueError('omega5 completion')
 for x,cap in [(done['seconds'],29),(receipt['seconds'],29.5),(a['external_seconds'],30)]:
  if type(x)not in(int,float)or not math.isfinite(x)or not 0<x<cap:raise ValueError('omega5 time')
 if not done['seconds']<=receipt['seconds']<=a['external_seconds']:raise ValueError('omega5 timing order')
 for x in [done['rss_bytes'],receipt['sampled_whole_tree_peak'],a['sampled_whole_tree_peak'],a['external_rss_bytes']]:
  if type(x)is not int or not 0<x<=384*1048576:raise ValueError('omega5 RSS')
 if receipt['sampled_whole_tree_peak']!=a['sampled_whole_tree_peak']:raise ValueError('omega5 RSS identity')
 if oldbinding['catalog']!=b['catalog']or oldbinding['catalog_geometry_sha256']!=b['catalog_geometry_sha256']:raise ValueError('same accepted catalog')
 tail=get('tail')
 if set(tail['moments'])!={str(k)for k in range(3,44)}:raise ValueError('inherited moment census')
 m={0:F(1),1:F(6),2:F(42)}
 for k in range(3,44):
  progress('before_reused_moment',{'index':k});x=scalar(tail['moments'][str(k)])
  if x.denominator!=1 or not 0<x<=12**k:raise ValueError('inherited integer moment')
  m[k]=x
 return m
