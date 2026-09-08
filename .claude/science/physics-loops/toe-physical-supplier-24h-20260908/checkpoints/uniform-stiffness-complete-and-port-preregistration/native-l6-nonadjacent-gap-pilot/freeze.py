from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parent;S=P.parent/'native-l6-allprefix-gap';C=P.parent/'native-l6-nonadjacent-prefix-census'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
old=json.loads((S/'FREEZE.json').read_text());runtime={p:sha(p) for p in old['runtime']}
interp='/Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12';nr=Path('/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/numpy')
for p in nr.rglob('*'):
 if p.is_file() and p.suffix in ('.py','.so','.dylib'):runtime[str(p.resolve())]=sha(p)
lib=nr.parent.parent
for p in lib.rglob('*'):
 if 'site-packages' in p.parts:continue
 if p.is_file() and p.suffix in ('.py','.so','.dylib'):runtime[str(p.resolve())]=sha(p)
runtime[str(Path(interp).resolve())]=sha(interp)
files={p.name:sha(p) for p in P.iterdir() if p.is_file() and p.name!='FREEZE.json'}
deps={str(p):sha(p) for p in [S/'core.py',S/'FREEZE.json',C/'CENSUS.json',C/'DERIVATION.md',C/'PREREGISTRATION.md',P.parent/'native-l6-prefix-gap-probe/DERIVATION.md']}
f=dict(status='UNLAUNCHED',files=files,dependencies=deps,runtime=runtime,interpreter=str(Path(interp).resolve()),numpy_origin=str(nr/'__init__.py'),numpy_root=str(nr),numpy_version='2.4.1',executable_membership=sorted(str(p.relative_to(P)) for p in P.rglob('*') if p.is_file() and p.suffix in ('.py','.so','.dylib','.pyc')),runtime_scope='Python/NumPy source and extension bytes pinned; system OS shared-cache/Accelerate dependencies outside closure, not a universal hardware arithmetic certification.')
(P/'FREEZE.json').write_text(json.dumps(f,indent=2)+'\n');print(sha(P/'FREEZE.json'))
