"""Actual bridge AST, only physical size/chunk constants changed for eight entries."""
import ast,struct,tempfile,json,hashlib
from pathlib import Path
P=Path(__file__).parent;tree=ast.parse((P/'run_once.py').read_text());keep=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ('require','sha','bridge')]
class Tiny(ast.NodeTransformer):
 def visit_BinOp(self,n):
  if isinstance(n.op,ast.LShift) and isinstance(n.left,ast.Constant) and n.left.value==1 and isinstance(n.right,ast.Constant) and n.right.value==20:return ast.copy_location(ast.Constant(8),n)
  return self.generic_visit(n)
 def visit_Constant(self,n):return ast.copy_location(ast.Constant(4),n) if n.value==4096 else n
module=ast.fix_missing_locations(Tiny().visit(ast.Module(body=keep,type_ignores=[])));ns={'Path':Path,'hashlib':hashlib,'ast':ast};exec(compile(module,'tiny_actual_bridge','exec'),ns)
def npy(path,descr='<f8'):
 header=repr({'descr':descr,'fortran_order':False,'shape':(8,)}).encode()+b'\n';path.write_bytes(b'\x93NUMPY\x01\x00'+len(header).to_bytes(2,'little')+struct.pack('<8d',0.,-0.,1.,-1.,.25,2.,3.,4.))
 # Include header (deliberately explicit fixture construction).
 path.write_bytes(b'\x93NUMPY\x01\x00'+len(header).to_bytes(2,'little')+header+struct.pack('<8d',0.,-0.,1.,-1.,.25,2.,3.,4.))
checks=0
with tempfile.TemporaryDirectory() as d:
 p=Path(d);n=p/'a.npy';r=p/'a.bin';npy(n);values=struct.pack('<8d',0.,-0.,1.,-1.,.25,2.,3.,4.)
 for phase in ('real','i'):
  raw=b''.join((values[j:j+8]+b'\0'*8) if phase=='real' else (b'\0'*8+values[j:j+8]) for j in range(0,64,8));r.write_bytes(raw);ns['bridge'](n,r,phase);checks+=1
  try:ns['bridge'](n,r,'i' if phase=='real' else 'real')
  except ValueError:checks+=1
  else:raise ValueError('phase mutant')
  expected=ns['sha'](r);r.write_bytes(raw[:-1]+b'\1')
  try:ns['require'](ns['sha'](r)==expected,'raw hash')
  except ValueError:checks+=1
  else:raise ValueError('hash mutant')
 r.write_bytes(raw);npy(n,'>f8')
 try:ns['bridge'](n,r,'i')
 except ValueError:checks+=1
 else:raise ValueError('header mutant')
print(json.dumps({'status':'PASS','checks':checks,'actual_bridge_AST':True,'substitutions':['2^20 entries ->8','4096 chunk ->4'],'physical_calls':0}))
