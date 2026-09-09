import ast,pathlib,tempfile,json,hashlib
P=pathlib.Path('/private/tmp/toe-24h-probes-20260908/native-rho4-b66-width-continuation-root-review/schema.py');t=ast.parse(P.read_text());fn=next(n for n in t.body if isinstance(n,ast.FunctionDef)and n.name=='check');ix=next(i for i,n in enumerate(fn.body)if isinstance(n,ast.Assign)and any(isinstance(x,ast.Name)and x.id=='poles'for x in n.targets));fn.body=fn.body[:ix]+[ast.Return(ast.Constant(True))];ast.fix_missing_locations(t);ns={};exec(compile(t,str(P),'exec'),ns)
with tempfile.TemporaryDirectory()as td:
 p=pathlib.Path(td);write=lambda p,x:p.write_text(json.dumps(x));old=p/'old';old.write_text('synthetic prefix\n');out=p/'out';out.mkdir();(out/'RECOVERED_NODES_00.ndjson').write_bytes(old.read_bytes());bp=p/'binding';write(bp,{'physical':{},'prior':{'nodes':str(old),'inputs':{str(old):ns['sha'](old)}}});rf={'authorization':{},'worker_freeze':'x','binding_path':str(bp)};r={'status':'COMPLETE_REMAINING65_WIDTH_DIAGNOSTIC','seconds':1,'poles':[{}]*66,'new_node_checks':113230,'recovered_node_records':1742,'node_checks':114972,'moments_evaluated':0,'integral_centers_evaluated':0,'oracle_calls':0};write(out/'STARTED.json',{});write(out/'PARTIAL.json',{'seconds':2})
 def seal():
  write(out/'RESULT.json',r);write(out/'WORKER_COMPLETE.json',{'status':'COMPLETE_WIDTH_ONLY_DIAGNOSTIC','runtime_sha256':'x','result_sha256':ns['sha'](out/'RESULT.json'),'seconds':3,'rss_bytes':100})
 seal();assert ns['check'](out,rf,4);n=1
 r['new_node_checks']=True;seal()
 try:ns['check'](out,rf,4)
 except ValueError:n+=1
 else:raise AssertionError('bool')
 r['new_node_checks']=113230;seal();(out/'RECOVERED_NODES_00.ndjson').write_text('changed')
 try:ns['check'](out,rf,4)
 except ValueError:n+=1
 else:raise AssertionError('prefix')
 print(n,'actual schema-prefix metadata controls PASS; full budget/stream loop excluded; no real records')
