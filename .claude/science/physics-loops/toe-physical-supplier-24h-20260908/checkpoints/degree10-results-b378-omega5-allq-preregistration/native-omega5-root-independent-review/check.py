from pathlib import Path
from fractions import Fraction as F
import json,types,hashlib,shutil
S=Path('/private/tmp/toe-24h-probes-20260908');E=S/'native-omega5-root-independent-review';source=S/'native-omega5-root-review/schema.py';T=Path(json.loads((S/'OMEGA5_ROOT_SYNTHETIC_CONTROLS.json').read_text())['fixture']);O=E/'synthetic_output';shutil.copytree(T/'output',O);(O/'FAILURE.json').unlink()
m=types.ModuleType('review_schema');m.__file__=str(T/'root/schema.py');exec(compile(source.read_bytes(),str(source),'exec'),m.__dict__);m.moments=lambda:{n:F(1)for n in range(3,44)}
rf={'worker_path':str(T/'worker'),'worker_freeze':'fake'}
def run(elapsed=28):return m.check(O,rf,elapsed,lambda _:None)
def write(p,v):p.write_text(json.dumps(v)+'\n')
run();out={'coherent_nonnative_pass':True,'moments_stub':'all1; no high native moments','actual_inputs_loaded':0}
p=O/'PARTIAL.json';old=p.read_bytes();x=json.loads(old);x['current']['result']['new_quantity_integral']=1;write(p,x)
try:run();out['numeric_bool_partial_accepted']=True
except ValueError:out['numeric_bool_partial_accepted']=False
p.write_bytes(old)
try:run(0.000001);out['worker_time_exceeding_root_accepted']=True
except ValueError:out['worker_time_exceeding_root_accepted']=False
p=O/'WORKER_COMPLETE.json';old=p.read_bytes();x=json.loads(old);x['rss_bytes']=True;write(p,x)
try:run();out['bool_RSS_rejected']=False
except ValueError:out['bool_RSS_rejected']=True
p.write_bytes(old);(E/'CONTROLS.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
