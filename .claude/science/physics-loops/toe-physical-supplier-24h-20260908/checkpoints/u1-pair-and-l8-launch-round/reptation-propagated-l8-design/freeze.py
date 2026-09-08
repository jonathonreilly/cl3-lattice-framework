from pathlib import Path
import sys,sysconfig,json,hashlib,zipfile,platform
import numpy as np
import analyze,producer,checkpoint
p=Path(__file__).parent.resolve()
def h(f):return hashlib.sha256(Path(f).read_bytes()).hexdigest()
files=set()
for module in list(sys.modules.values()):
 f=getattr(module,'__file__',None)
 if f and Path(f).is_file() and p not in Path(f).resolve().parents:files.add(str(Path(f).resolve()))
files.add(str(Path(sys.executable).resolve()))
for base in [Path(np.__file__).parent,Path(np.__file__).parent.parent/'numpy.libs']:
 if base.exists():
  for pattern in ['*.so','*.dylib']:
   files.update(str(f.resolve()) for f in base.rglob(pattern))
for f in [Path(sys.base_prefix)/'Python',Path(sysconfig.get_config_var('LIBDIR') or '')/str(sysconfig.get_config_var('LDLIBRARY') or '')]:
 if f.is_file():files.add(str(f.resolve()))
(p/'RUNTIME.json').write_text(json.dumps(dict(python_version=sys.version,numpy_version=np.__version__,platform=platform.platform(),files={f:h(f) for f in sorted(files)},scope='Loaded Python module files, interpreter and NumPy native extensions/libraries; OS frameworks are supplied environment, not a hermetic container.'),indent=2)+'\n')
ledger=dict(preproduction_seconds=sum(json.loads((p/f).read_text())[k] for f,k in [('MICRO.json','seconds'),('CHECKPOINT_CONTROLS.json','total_seconds'),('PRODUCER_CONTROLS.json','total_seconds')]),components=['micro','checkpoint deterministic controls','producer deterministic controls'],smoke_seconds_pending=True)
(p/'RESOURCE_LEDGER.json').write_text(json.dumps(ledger,indent=2)+'\n')
names=['core.py','initialize.py','checkpoint.py','producer.py','analysis_core.py','analyze.py','launch.py','SEGMENT_PROTOCOL.md','RUNTIME.json','RESOURCE_LEDGER.json','PROPOSAL.md','FORECAST.json','producer_controls.py','PRODUCER_CONTROLS.json']
(p/'PRODUCTION_FREEZE.json').write_text(json.dumps({f:h(p/f) for f in names},indent=2)+'\n')
print('freeze',h(p/'PRODUCTION_FREEZE.json'),'runtimefiles',len(files))
