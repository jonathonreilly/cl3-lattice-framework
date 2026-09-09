"""Source readiness only; no execution mode or contract exists."""
import sys,json,hashlib,types
from pathlib import Path
P=Path(__file__).resolve().parent
if not sys.flags.isolated or not sys.dont_write_bytecode:raise ValueError('-I -B')
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for block in iter(lambda:f.read(1048576),b''):h.update(block)
 return h.hexdigest()
f=json.loads((P/'FREEZE.json').read_text())
for name,h in f['files'].items():
 if sha(P/name)!=h:raise ValueError('source '+name)
for name in ('exact_square','envelope','real_kernel','transport','fp_guard','norms','formats','validate_coefficients','plane','resolvent','active','worker'):
 data=(P/(name+'.py')).read_bytes()
 if hashlib.sha256(data).hexdigest()!=f['files'][name+'.py']:raise ValueError('source bytes')
 m=types.ModuleType(name);m.__file__=str(P/(name+'.py'));sys.modules[name]=m;exec(compile(data,m.__file__,'exec'),m.__dict__)
print(json.dumps({'status':'PASS','algorithm':'direct_gaussian_once','physical_calls':0,'execution_mode':False}))
