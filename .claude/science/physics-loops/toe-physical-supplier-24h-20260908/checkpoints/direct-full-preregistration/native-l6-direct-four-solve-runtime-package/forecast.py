from pathlib import Path
from fractions import Fraction as F
import json,hashlib,math
P=Path(__file__).parent

def calculate():
 d={}
 for n,h in json.loads((P/'COST_INPUTS/BINDINGS.json').read_text()).items():
  q=P/'COST_INPUTS'/n
  if hashlib.sha256(q.read_bytes()).hexdigest()!=h:raise ValueError('cost hash')
  d[n[:-5]]=json.loads(q.read_text())
 def t(x):
  if type(x) not in (int,float) or not math.isfinite(x) or x<=0:raise ValueError('timing')
  return F(str(x))
 if len(d['new']['planes'])!=12 or d['new']['status']!='COMPLETE':raise ValueError('pilot')
 plane=max(t(r['plane_seconds']) for r in d['new']['planes'])
 action=max(t(d['new']['action_seconds']),*(t(r['action_seconds']) for r in d['action']['rows']))
 norm=max(t(d['new']['norm_seconds']),t(d['norm']['scan_seconds']))
 bridge=t(d['new']['save_bridge_seconds']);transport=F('0.05441')
 terms={'656_planes':656*plane,'4_actions':4*action,'9_scans':9*norm,'27_transports':27*transport,'11_saves':11*bridge}
 production=3*sum(terms.values())+60;combined=production+150+14
 return {'status':'FORECAST_ONLY','terms':{k:str(v) for k,v in terms.items()},'factor':3,'allowance_seconds':60,'production_exact':str(production),'production_seconds':float(production),'production_limit':180,'replay_reserve':150,'prior':14,'combined_forecast':float(combined),'fixed_caps_plus_prior':344,'aggregate_limit':360,'passes':production<180 and combined<360}
if __name__=='__main__':print(json.dumps(calculate(),indent=2))
