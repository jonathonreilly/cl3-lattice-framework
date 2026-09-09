"""Predata fixed coverage forecast; exact rational arithmetic on recorded timings."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,math
P=Path(__file__).parent

def forecast():
 bindings=json.loads((P/'COST_INPUTS/BINDINGS.json').read_text());data={}
 for name,h in bindings.items():
  p=P/'COST_INPUTS'/name
  if hashlib.sha256(p.read_bytes()).hexdigest()!=h:raise ValueError('cost hash')
  data[name[:-5]]=json.loads(p.read_text())
 def positive(x):
  if not isinstance(x,(float,int)) or not math.isfinite(x) or x<=0:raise ValueError('cost timing')
  return F(str(x))
 a=max(positive(r['action_seconds']) for r in data['action']['rows'])
 n=max(positive(data['norm']['scan_seconds']),positive(data['vector']['real_norm_seconds']))
 v=max(map(positive,data['vector']['vector_pass_seconds']));io=positive(data['vector']['conversion_seconds'])
 # Transport root-supplied measured maximum conservatively rounded upward.
 t=F('0.05441')
 terms={'1088_actions':1088*a,'129_scans':129*n,'1024_vector_groups':1024*v,'27_transports':27*t,'71_IO_equivalents':71*io,'startup_FP_envelopes_initialization_other_allowance':F(40)}
 production=2*sum(terms.values());total=production+10+400
 if len(data['action']['rows'])!=2 or len(data['vector']['vector_pass_seconds'])!=16:raise ValueError('cost coverage')
 return {'scope':'forecast, not guaranteed runtime or convergence','terms_seconds':{k:str(x) for k,x in terms.items()},'headroom_factor':2,'production_seconds_exact':str(production),'production_seconds':float(production),'combined_seconds_exact':str(total),'combined_seconds':float(total),'production_limit':1390,'total_limit':1800,'prior_seconds':10,'replay_reserve_seconds':400,'passes':production<=1390 and total<=1800}
if __name__=='__main__':print(json.dumps(forecast(),indent=2))
