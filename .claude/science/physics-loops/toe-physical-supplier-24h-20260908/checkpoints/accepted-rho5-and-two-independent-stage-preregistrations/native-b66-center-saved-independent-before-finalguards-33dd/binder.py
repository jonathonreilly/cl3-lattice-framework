"""Independent source normalization. No producer arithmetic imported."""
import json,hashlib,math
from pathlib import Path
from fractions import Fraction as F

def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for s in iter(lambda:f.read(1048576),b''):h.update(s)
 return h.hexdigest()
def load(plan):
 if plan['status']!='ROOT_REVIEWED_SAVED_CENTER_REPLAY':raise ValueError('NOTREADY')
 pins=plan['inputs']
 def read(p):
  if pins.get(str(p))!=sha(p):raise ValueError('pin '+str(p))
  return json.loads(Path(p).read_text())
 for p,h in pins.items():
  if sha(p)!=h:raise ValueError('closure')
 b=read(plan['producer_binding']);rt=read(plan['producer_runtime']);ac=read(plan['acceptance']);out=Path(plan['output']);w=read(out/'WORKER_COMPLETE.json');r=read(out/'RESULT.json')
 if ac['status']!='ACCEPTED_NEW_RHO4_B66_CENTER_CERTIFICATES' or ac['result_sha256']!=sha(out/'RESULT.json')or ac['worker_freeze']!=sha(plan['producer_runtime']):raise ValueError('center acceptance')
 if w['runtime_sha256']!=ac['worker_freeze']or w['result_sha256']!=ac['result_sha256']or w['binding_sha256']!=sha(plan['producer_binding']):raise ValueError('center worker')
 if r['status']!='COMPLETE_NEW_RHO4_B66_CERTIFICATES'or r['all_targets_met']is not True:raise ValueError('center result')
 for p,h in rt['inputs'].items():
  if pins.get(p)!=h:raise ValueError('producer closure')
 for v,cap in ((ac['external_seconds'],120),(w['seconds'],119)):
  if type(v)not in(int,float)or not math.isfinite(v)or not 0<v<=cap:raise ValueError('time')
 for v in(ac['sampled_whole_tree_peak'],w['rss_bytes']):
  if type(v)is not int or not 0<v<=384*1048576:raise ValueError('RSS')
 phy=b['physical'];g=read(phy['catalog_geometry_path']);ps=read(phy['poles_path'])['rows'];aa=read(Path(phy['a66']['directory'])/'RESULT.json')['rows'];cat=read(Path(phy['catalog']['directory'])/'RESULT.json')['rows'];ends=[]
 if(len(ps),len(aa),len(cat),len(g['nodes']),len(g['endpoints']))!=(66,66,3484,1742,3484):raise ValueError('source counts')
 for i,(e,row)in enumerate(zip(g['endpoints'],cat)):
  if type(row['id'])is not int or row['id']!=i:raise ValueError('endpoint id')
  x=read(Path(phy['catalog']['directory'])/row['path'])
  if x['catalog_endpoint']!=e or x['s']!=e['s']:raise ValueError('endpoint identity')
  ends.append(tuple(map(F,x['A'])))
 nodes=[];Q=1<<192
 for i,n in enumerate(g['nodes']):
  l,u=n['endpoint_ids'];t=tuple(map(F,n['t_interval']));wl,wu=map(F,n['weight']);wl=F((wl*Q).__floor__(),Q);wu=F((wu*Q).__ceil__(),Q)
  if type(n['id'])is not int or n['id']!=i or n['panel']!=i//26-64:raise ValueError('node identity')
  nodes.append({'t':list(map(str,t)),'A':list(map(str,(ends[u][0],ends[l][1]))),'w':[str(wl),str(wu)]})
 poles=[]
 for i,(pp,ar)in enumerate(zip(ps,aa)):
  x=ar['oracle']
  if type(ar['id'])is not int or ar['id']!=i or x['s']!=pp['s_midpoint']:raise ValueError('pole identity')
  poles.append({'s':x['s'],'A':x['A'],'Aprime':x['Aprime'],'radius_file':b['node_files'][i],'budget_file':b['pole_files'][i]})
 return {'status':'AUTHENTICATED_ACTUAL_CENTER_AND_WIDTH_OUTPUTS','output':str(out),'nodes':nodes,'poles':poles}
