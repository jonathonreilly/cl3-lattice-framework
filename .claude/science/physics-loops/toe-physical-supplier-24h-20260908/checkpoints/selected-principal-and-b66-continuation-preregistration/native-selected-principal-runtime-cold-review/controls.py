from pathlib import Path
from fractions import Fraction as F
import hashlib,json,types,sys,ast,tempfile,shutil
B=Path('/private/tmp/toe-24h-probes-20260908');P=B/'native-selected-principal-runtime-design';R=B/'native-selected-principal-root-review'
def load(p,name):
 m=types.ModuleType(name);m.__file__=str(p);exec(compile(p.read_bytes(),str(p),'exec'),m.__dict__);return m
seed=load(P/'seed.py','seed');sys.modules['seed']=seed
# Actual assembly body, with only dimension constants24->2 and48->4 changed for a tiny test.
tree=ast.parse((P/'principal.py').read_text())
class Small(ast.NodeTransformer):
 def visit_Constant(self,n):
  if type(n.value)is int and n.value in(24,48):return ast.copy_location(ast.Constant({24:2,48:4}[n.value]),n)
  return n
m=types.ModuleType('tiny_actual_principal');exec(compile(ast.fix_missing_locations(Small().visit(tree)),str(P/'principal.py'),'exec'),m.__dict__)
S=2**192;calls=[]
def entry(i,j):
 calls.append((i,j))
 return ((S,S),(0,0)) if i==j else ((S//4,S//4),(S//8,S//8))
G,r,E=m.assemble([0,2],entry,lambda *x:None)
expected=[[F(1),F(0),F(1,4),F(1,8)],[F(0),F(1),F(-1,8),F(1,4)],[F(1,4),F(-1,8),F(1),F(0)],[F(1,8),F(1,4),F(0),F(1)]]
if G!=expected or any(any(x for x in row)for row in r) or calls!=[(0,0),(0,2),(2,2)]:raise ValueError('paired signs')
# Demonstrate schema deficiencies with tiny metadata only, no physical matrices or inputs.
schema=load(R/'schema.py','schema');d=Path(tempfile.mkdtemp(prefix='principal-schema-only-'))
def save(p,x):p.write_text(json.dumps(x)+'\n')
try:
 rf={'worker_freeze':'dummy','authorization':{'binding_sha256':'dummy'}};save(d/'STARTED.json',rf['authorization']);rows=[]
 for i in range(5):
  od=d/f'ORBIT_{i}';od.mkdir();save(od/'SELECTED.json',list(range(24)));save(od/'RESULT.json',{'status':'INDETERMINATE_RESIDUAL','e':'0'});(od/'EVENTS.ndjson').write_text('');rows.append({'orbit':i,'status':'INDETERMINATE_RESIDUAL'})
 save(d/'RESULT.json',{'status':'COMPLETE_SELECTED_PRINCIPAL_ATTEMPT','orbits':rows,'seconds':'not-a-time'});save(d/'PARTIAL.json',{'current':{'stage':'complete'},'rows':rows});save(d/'WORKER_COMPLETE.json',{'status':'COMPLETE_SELECTED_PRINCIPAL','runtime_sha256':'dummy','binding_sha256':'dummy','result_sha256':hashlib.sha256((d/'RESULT.json').read_bytes()).hexdigest(),'seconds':1,'rss_bytes':100})
 result=schema.check(d,rf,2)
 print(json.dumps({'assembly_tiny':'PASS','assembly_dimension_modification':'only24->2 and48->4 constants; actual signed assembly body','adverse_schema_accepted':result,'defects':'unbound selected order, empty event stream, e0 INDETERMINATE_RESIDUAL, invalid result seconds accepted','native_calls':0},indent=2))
finally:shutil.rmtree(d)
