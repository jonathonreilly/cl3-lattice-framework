import sys,pathlib,runpy,json,hashlib
R=pathlib.Path('/Users/jonreilly/Projects/Physics-worktrees/review-backlog-schur-poles-7338-20260909')
p=R/'scripts/admissibility_reflected_curvature_canonical_reduction_schur_pole_tt_spectral_weight_boundary_2026_08_23.py'
try:
 runpy.run_path(str(p),run_name='__main__')
finally:
 inputs={}
 for mod in list(sys.modules.values()):
  f=getattr(mod,'__file__',None)
  if f and str(f).startswith(str(R)) and str(f).endswith('.py'):
   inputs[str(pathlib.Path(f).relative_to(R))]=hashlib.sha256(pathlib.Path(f).read_bytes()).hexdigest()
 pathlib.Path(__file__).with_name('primary_actual_imports.json').write_text(json.dumps(inputs,indent=2,sort_keys=True))
