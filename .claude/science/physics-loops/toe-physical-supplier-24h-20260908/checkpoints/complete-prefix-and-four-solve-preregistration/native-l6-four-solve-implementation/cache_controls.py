"""Tiny actual-wrapper loader test, no worker import or physical action."""
import ast,hashlib,importlib.util,sys,tempfile,py_compile,os,json
from pathlib import Path
source=Path(__file__).with_name('run.py').read_text()
node=next(n for n in ast.parse(source).body if isinstance(n,ast.FunctionDef) and n.name=='load_verified')
exec(compile(ast.Module(body=[node],type_ignores=[]),'actual_loader_ast','exec'),globals())
with tempfile.TemporaryDirectory(prefix='verified-cache-control-') as t:
 p=Path(t)/'fixture.py';p.write_text('VALUE = 2\n');stamp=1700000000;os.utime(p,(stamp,stamp));py_compile.compile(str(p),doraise=True)
 p.write_text('VALUE = 1\n');os.utime(p,(stamp,stamp));h=hashlib.sha256(p.read_bytes()).hexdigest()
 spec=importlib.util.spec_from_file_location('stale_control',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
 if m.VALUE!=2:raise ValueError('stale pyc control did not reproduce')
 if load_verified('fixed_control',p,h).VALUE!=1:raise ValueError('verified source bypassed')
 try:load_verified('bad_hash_control',p,'0'*64)
 except ValueError:pass
 else:raise ValueError('hash mutant accepted')
 print(json.dumps({'status':'PASS','actual_loader_ast':True,'stale_pyc_default_value':2,'verified_source_value':1,'wrong_hash_rejected':True,'physical_calls':0}))
