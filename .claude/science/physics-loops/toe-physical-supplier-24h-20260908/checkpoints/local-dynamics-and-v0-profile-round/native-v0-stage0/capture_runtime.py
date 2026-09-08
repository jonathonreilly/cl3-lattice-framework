import sys,pathlib,hashlib,json
import numpy,scipy.sparse,scipy.sparse.linalg
from scipy.sparse.linalg import eigsh
from core import Path
P=pathlib.Path(__file__).parent;files={}
for m in list(sys.modules.values()):
 f=getattr(m,'__file__',None)
 if f and pathlib.Path(f).is_file():files[str(pathlib.Path(f).resolve())]=hashlib.sha256(pathlib.Path(f).read_bytes()).hexdigest()
files[str(pathlib.Path(sys.executable).resolve())]=hashlib.sha256(pathlib.Path(sys.executable).resolve().read_bytes()).hexdigest()
(P/'RUNTIME.json').write_text(json.dumps(dict(python=sys.version,numpy=numpy.__version__,files=files,scope='Actual imported module and interpreter bytes for review/reproduction; OS frameworks supplied, not a hermetic environment; captured after initial deterministic checks, not retrospectively called a prospective runtime freeze'),indent=2)+'\n')
print(len(files))
