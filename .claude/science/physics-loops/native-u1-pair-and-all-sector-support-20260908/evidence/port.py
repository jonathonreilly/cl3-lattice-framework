import ast,pathlib,shutil,json,hashlib
S=pathlib.Path('/private/tmp/toe-24h-probes-20260908');W=pathlib.Path('/private/tmp/toe-native-u1-pair-and-all-sector-support-20260908');pack=W/'.claude/science/physics-loops/native-u1-pair-and-all-sector-support-20260908';pack.mkdir(parents=True,exist_ok=True)
for name in ['native-u1-pair-creation','native-u1-pair-creation-cold-review','native-u1-all-sector-connectivity-root','native-u1-all-sector-connectivity-cold-review']:
 shutil.copytree(S/name,pack/'evidence'/name,dirs_exist_ok=True)
(pack/'inputs').mkdir(exist_ok=True);shutil.copy2(S/'native-global-charge-exchange/RESULT.json',pack/'inputs/GLOBAL_D4_SEED.json')
seedrel=str((pack/'inputs/GLOBAL_D4_SEED.json').relative_to(W))
class Port(ast.NodeTransformer):
 def visit_Assert(self,n):return ast.Expr(ast.Call(ast.Name('_require',ast.Load()),[n.test,n.msg or ast.Constant('original assertion')],[]))
 def visit_If(self,n):
  n=self.generic_visit(n)
  if len(n.body)==1 and isinstance(n.body[0],ast.Raise) and not n.orelse:
   e=n.body[0].exc;label=e.args[0] if isinstance(e,ast.Call) and e.args else ast.Constant('original failure')
   return ast.Expr(ast.Call(ast.Name('_require',ast.Load()),[ast.UnaryOp(ast.Not(),n.test),label],[]))
  return n
 def visit_Expr(self,n):
  v=n.value
  if isinstance(v,ast.Call) and isinstance(v.func,ast.Attribute) and v.func.attr=='alarm':return ast.If(ast.Compare(ast.Name('__name__',ast.Load()),[ast.Eq()],[ast.Constant('__main__')]),[n],[])
  if isinstance(v,ast.Call) and isinstance(v.func,ast.Attribute) and v.func.attr=='write_text':
   # Preserve the exact payload expression, remove scratch writes.
   a=v.args[0];a=a.left if isinstance(a,ast.BinOp) else a
   if isinstance(a,ast.Call) and isinstance(a.func,ast.Attribute) and a.func.attr=='dumps':return ast.Assign([ast.Name('out',ast.Store())],a.args[0])
   return None
  if isinstance(v,ast.Call) and isinstance(v.func,ast.Name) and v.func.id=='print':
   a=v.args[0]
   if isinstance(a,ast.Call) and isinstance(a.func,ast.Attribute) and a.func.attr=='dumps':return ast.Assign([ast.Name('out',ast.Store())],a.args[0])
   return None
  return self.generic_visit(n)
header='''import resource,sys,json,time,signal\nexecuted_predicates=0\ndef _require(condition,label):\n global executed_predicates\n executed_predicates+=1\n if not condition:raise RuntimeError(label)\n'''
footer='''\nrss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)\n_require(0<rss<384 and time.monotonic()-start<180,'resource cap')\nout['executed_predicates']=executed_predicates\nprint(json.dumps(out,indent=2,allow_nan=False))\n'''
items={'pair_author':'native-u1-pair-creation','pair_independent':'native-u1-pair-creation-cold-review','support_author':'native-u1-all-sector-connectivity-root','support_independent':'native-u1-all-sector-connectivity-cold-review'};receipts={}
for kind,folder in items.items():
 raw=(S/folder/'check.py').read_text()
 if kind=='pair_author':raw=raw.replace("O.parent/'native-global-charge-exchange/RESULT.json'",f"pathlib.Path(__file__).resolve().parents[1]/{seedrel!r}")
 if kind=='support_author':raw=raw.replace("Path(__file__).parents[1]/'native-global-charge-exchange/RESULT.json'",f"Path(__file__).resolve().parents[1]/{seedrel!r}")
 tree=Port().visit(ast.parse(raw));ast.fix_missing_locations(tree);code=header+ast.unparse(tree)+footer
 name=f'native_u1_pair_support_{kind}_2026_09_08.py';(W/'scripts'/name).write_text(code);receipts[kind]=dict(original_sha=hashlib.sha256((S/folder/'check.py').read_bytes()).hexdigest(),canonical_sha=hashlib.sha256(code.encode()).hexdigest(),transform='AST assertions and one-raise conditionals become explicit counted predicates; scratch writes/prints replaced by same JSON payload; standalone alarm guarded; external seed path portable; resource guard.')
(pack/'PORT_TRANSFORM.json').write_text(json.dumps(receipts,indent=2)+'\n')
