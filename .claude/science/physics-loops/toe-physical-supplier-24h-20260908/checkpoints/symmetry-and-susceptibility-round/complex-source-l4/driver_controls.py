import ast,json,hashlib
from pathlib import Path
import numpy as np
p=Path(__file__).resolve().parent;s=(p/'driver.py').read_text();f=next(x for x in ast.parse(s).body if isinstance(x,ast.FunctionDef) and x.name=='source_coefficients');ns={'np':np};exec(compile(ast.Module(body=[f],type_ignores=[]),'<actual-selection>','exec'),ns)
cr=np.arange(12*192.).reshape(12,192);ci=-cr-1
for h in (1,2):
 x=ns['source_coefficients'](cr,ci,h);expected=np.concatenate([cr[6*(h-1):6*h],ci[6*(h-1):6*h]])
 if not np.array_equal(x,expected):raise AssertionError('harmonic_slice')
mut=s.replace('sl=slice(6*(h-1),6*h)','sl=slice(0,6)');(p/'wrong_slice_driver.py').write_text(mut);f=next(x for x in ast.parse(mut).body if isinstance(x,ast.FunctionDef) and x.name=='source_coefficients');ns={'np':np};exec(compile(ast.Module(body=[f],type_ignores=[]),'<wrong-selection>','exec'),ns)
failed=not np.array_equal(ns['source_coefficients'](cr,ci,2),np.concatenate([cr[6:],ci[6:]]))
if not failed:raise AssertionError('surviving_wrong_slice')
for n in ['driver.py','launch.py','analyze.py']:compile((p/n).read_text(),n,'exec')
(p/'DRIVER_CONTROLS.json').write_text(json.dumps({'actual_both_harmonic_slices':True,'actual_wrong_slice_mutant_failed':failed,'no_production_execution':True},indent=2)+'\n')
(p/'PRODUCTION_FREEZE.json').write_text(json.dumps({n:hashlib.sha256((p/n).read_bytes()).hexdigest() for n in ['kernel.py','driver.py','launch.py','analyze.py','PREREGISTRATION.md']},indent=2)+'\n')
print((p/'PRODUCTION_FREEZE.json').read_text())
