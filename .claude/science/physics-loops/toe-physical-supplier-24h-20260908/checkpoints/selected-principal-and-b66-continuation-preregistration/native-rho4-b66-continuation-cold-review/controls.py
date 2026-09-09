from pathlib import Path
import sys,types,json,hashlib,shutil
B=Path('/private/tmp/toe-24h-probes-20260908');P=B/'native-rho4-b66-width-continuation-design';E=B/'native-rho4-b66-continuation-cold-review';E.mkdir(exist_ok=False)
for n in ('caps','recover'):
 m=types.ModuleType(n);m.__file__=str(P/(n+'.py'));sys.modules[n]=m;exec(compile(Path(m.__file__).read_bytes(),m.__file__,'exec'),m.__dict__)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();dump=lambda p,x:p.write_text(json.dumps(x)+'\n')
base=E/'synthetic';base.mkdir();count=1742;Q=1<<256
rows=[{'node':j,'panel':j//26-64,'radii':['1/'+str(Q),'2/'+str(Q)],'info':{'denominator_lower_abs':'1','node_radii':['1','2']},'cumulative_radii':[str(j+1)+'/'+str(Q),str(2*j+2)+'/'+str(Q)]}for j in range(count)]
failure={'node_checks':count,'completed':[],'current':{'stage':'node','pole':0,'node':1741},'error':'4300 digits'}
partial={'node_checks':count,'poles':[]};receipt={'pass':False,'returncode':1,'worker_freeze':'synthetic-fixed-source'}
checks=[]
for case in ('valid','bad_order','bad_cumulative','off_grid','wrong_failure','wrong_pin'):
 d=E/case;d.mkdir();rs=json.loads(json.dumps(rows));f=dict(failure)
 if case=='bad_order':rs[700]['node']=701
 if case=='bad_cumulative':rs[1300]['cumulative_radii'][1]='0'
 if case=='off_grid':rs[0]['radii'][0]='1/3'
 if case=='wrong_failure':f['error']='unrelated'
 np=d/'nodes.ndjson';np.write_text(''.join(json.dumps(r)+'\n'for r in rs));dump(d/'failure.json',f);dump(d/'partial.json',partial);dump(d/'receipt.json',receipt)
 c={k:str(d/(k+'.json'))for k in ('failure','partial','receipt')};c.update(nodes=str(np),worker_freeze='synthetic-fixed-source');c['inputs']={v:sha(Path(v))for k,v in c.items()if k!='worker_freeze'}
 if case=='wrong_pin':c['inputs'][str(np)]='0'*64
 out=d/'out';out.mkdir();passed=False
 try:
  total,separated=sys.modules['recover'].load(c,out)
  assert total[0]*Q==count and total[1]*Q==2*count and separated is True
  assert (out/'RECOVERED_NODES_00.ndjson').read_bytes()==np.read_bytes();passed=True
 except ValueError:pass
 assert passed==(case=='valid'),case
 checks.append({'case':case,'accepted':passed,'expected_accept':case=='valid'})
# A bounded decimal format covers every 32768-bit stored integer.
sys.set_int_max_str_digits(10000);assert len(str((1<<32768)-1))==9865
checks.append({'case':'32768bit_integer_decimal_coverage','digits':9865,'limit':10000})
(E/'CONTROLS.json').write_text(json.dumps({'checks':checks,'physical_nodes_read':0,'node_formulas_executed':0,'scope':'Fabricated repeated dyadic radii; independent expected integer totals and exact copy; no actual scientific stream.'},indent=2)+'\n')
# Retain compact control source/output; synthetic expanded fixtures are reproducible.
for d in E.iterdir():
 if d.is_dir():shutil.rmtree(d)
shutil.copy2(__file__,E/'controls.py')
(E/'REVIEW.md').write_text('''# Remaining-65 width continuation: source PASS

Root independently read all changed worker/recover/dispatcher source and all monitor/schema changes from reviewed 3dcd/15ad. Worker 733d8163 and monitor ef3de1d5 preserve the mathematical radius formulas and 120/119.5/119-second, 384-MiB contract. All 6317 worker pins passed. Pole 0 is recovered only from its hash-bound completed stream; its node formulas are not called again. Only poles 1 through 65 call ledger.node. The new calculation covers 113230 fresh node checks plus 1742 recovered records, with no B centers or moments.

Seven independent controls cover a complete fabricated 1742-record prefix and its expected integer-grid totals and byte identity, four semantic mutations, a bad hash, and the exact decimal length of the maximum 32768-bit integer. Five adverses were rejected. These are synthetic records, not saved scientific data. The 10000-digit bound covers each stored numerator/denominator without changing the mathematical bit cap. Original 4300-digit failure, partial stream and receipts remain immutable.

The final root independently parses all 66 pole budgets and cumulative records, with exact recovered-prefix copy authentication and literal new/recovered counts. Its node error formulas are explicitly inherited rather than independently replayed. Author source-only readiness and three prefix-schema controls passed. Root-source freeze and final pins must be verified before remote preregistration. Prospective feasibility remains conditional on future integral-center arithmetic and tail centering. No downstream scalar value, Gram, leakage or physical target is certified by this diagnostic. External teardown reconciliation remains required.
''')
print({'checks':len(checks),'review_sha256':sha(E/'REVIEW.md')})
