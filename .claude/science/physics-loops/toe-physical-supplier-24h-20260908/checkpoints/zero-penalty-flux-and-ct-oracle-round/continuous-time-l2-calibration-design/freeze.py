import pathlib,hashlib,json,sys,oracle
B=pathlib.Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
refs=[B.parent/'continuous-time-face-conditional'/'FINAL_FREEZE.json',B.parent/'continuous-time-face-gibbs-panel'/'DERIVATION.md',B.parent/'reptation-endpoint-residual-proof'/'DERIVATION.md',B.parent/'ice-spectral-moments'/'KINETIC_SUM_RULE_ADDENDUM.md',B.parent/'face-fiber-diagnostic-design'/'DIAGNOSTIC_DESIGN.md',B.parent/'native-face-alias-scope-correction'/'ALIAS_SCOPE_CORRECTION.md']
(B/'SOURCE_BINDINGS.json').write_text(json.dumps({str(p):sha(p) for p in refs},indent=2))
paths={pathlib.Path(sys.executable).resolve()}
for m in list(sys.modules.values()):
 p=getattr(m,'__file__',None)
 if p and pathlib.Path(p).is_file():paths.add(pathlib.Path(p).resolve())
(B/'RUNTIME.json').write_text(json.dumps({str(p):sha(p) for p in sorted(paths)},indent=2))
files={p.name:sha(p) for p in sorted(B.iterdir()) if p.is_file() and p.name!='FINAL_FREEZE.json'}
(B/'FINAL_FREEZE.json').write_text(json.dumps({'files':files,'no_stochastic_execution':True,'production_counts_provisional_until_cost_review':True},indent=2));print(sha(B/'FINAL_FREEZE.json'));print(sha(B/'DERIVATION.md'))
