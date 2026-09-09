"""No loads at import. Accepted old width family; no center/ledger recomputation."""
import json,math
from pathlib import Path
from fractions import Fraction as F
import input_loader
sha=input_loader.sha
def load(b):
 pins=b['inputs']
 def read(p):
  if p not in pins or sha(p)!=pins[p]:raise ValueError('bound source '+p)
  return json.loads(Path(p).read_text())
 for p,h in pins.items():
  if sha(p)!=h:raise ValueError('full input closure')
 parent=read(b['width_binding'])
 if b['physical']!=parent['physical']:raise ValueError('same physical catalog')
 rf=read(b['width_runtime'])
 for p,h in rf['inputs'].items():
  if pins.get(p)!=h:raise ValueError('width transitive pin')
 a=read(b['width_acceptance']);r=read(b['width_result']);w=read(b['width_worker'])
 if a['root_freeze']!=pins[b['width_root']]:raise ValueError('root source binding')
 if a['status']!='ACCEPTED_REMAINING65_WIDTH_LEDGER_WITH_RECOVERED_PREFIX' or a['result_sha256']!=pins[b['width_result']]or a['worker_freeze']!=pins[b['width_runtime']]:raise ValueError('accepted width')
 if w['status']!='COMPLETE_WIDTH_ONLY_DIAGNOSTIC'or w['result_sha256']!=pins[b['width_result']]or w['runtime_sha256']!=pins[b['width_runtime']]:raise ValueError('width completion')
 if r['status']!='COMPLETE_REMAINING65_WIDTH_DIAGNOSTIC'or r['all_feasible']is not True or len(r['poles'])!=66:raise ValueError('complete width census')
 for k,v in [('recovered_node_records',1742),('new_node_checks',113230),('node_checks',114972),('moments_evaluated',0),('integral_centers_evaluated',0),('oracle_calls',0)]:
  if type(r[k])is not int or r[k]!=v:raise ValueError('literal width census')
 for i,x in enumerate(r['poles']):
  if type(x['pole'])is not int or x['pole']!=i or x['separated']is not True or x['passes']!=[True,True]or any(type(v)is not bool for v in x['passes'])or x['status']!='FEASIBLE_UNDER_DECLARED_ARITHMETIC_RESERVE':raise ValueError('all66 feasible')
 for x,cap in ((a['external_seconds'],120),(a['sampled_whole_tree_peak'],384*1048576),(w['seconds'],119),(w['rss_bytes'],384*1048576)):
  if type(x)not in(int,float)or not math.isfinite(x)or not 0<x<=cap:raise ValueError('width resource')
 # Recovered pole0 bytes have exactly the original preserved failed-attempt hash.
 if pins[b['node_files'][0]]!=parent['prior']['inputs'][parent['prior']['nodes']]:raise ValueError('recovered immutable prefix')
 if len(b['node_files'])!=66 or len(b['pole_files'])!=66:raise ValueError('66 input files')
 poles,rows,nodes=input_loader.load(b['physical'])
 if len(poles)!=66 or len(rows)!=66 or len(nodes)!=1742:raise ValueError('fixed inputs')
 for i,n in enumerate(nodes):
  if type(n['id'])is not int or n['id']!=i or type(n['panel'])is not int or n['panel']!=i//26-64:raise ValueError('catalog ordering')
  t=n['t_interval'];ww=n['weight_interval']
  if not 0<t[0]<t[1]<=8 or t[1]-t[0]>F(1,2**140)or not 0<ww[0]<=ww[1]or ww[1]-ww[0]>F(1,10**38):raise ValueError('actual geometry')
  for x in(*t,*ww,*n['A_interval']):
   if max(abs(x.numerator).bit_length(),x.denominator.bit_length())>512:raise ValueError('input512')
 if sum(n['weight_interval'][1]for n in nodes)>9:raise ValueError('weight sum')
 return poles,rows,nodes
