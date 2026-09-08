import sys,pathlib,hashlib,json,core,check,supplement
B=pathlib.Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
# Reproduction closure captured after deterministic checks; not relabeled prospective.
paths={pathlib.Path(sys.executable).resolve()}
for m in list(sys.modules.values()):
 p=getattr(m,'__file__',None)
 if p and pathlib.Path(p).is_file():paths.add(pathlib.Path(p).resolve())
runtime={str(p):sha(p) for p in sorted(paths)}
(B/'RUNTIME.json').write_text(json.dumps({'timing':'post-control reproduction binding','files':runtime},indent=2))
files={p.name:sha(p) for p in sorted(B.iterdir()) if p.is_file() and p.name!='FINAL_FREEZE.json'}
parent=B.parent/'interior-projector-sampler-panel'
external={str(p):sha(p) for p in (parent/'DERIVATION.md',parent/'ALIAS_CLARIFICATION.md')}
(B/'FINAL_FREEZE.json').write_text(json.dumps({'files':files,'external_proof':external,'no_production':True},indent=2))
print(sha(B/'FINAL_FREEZE.json'));print(sha(B/'core.py'))
