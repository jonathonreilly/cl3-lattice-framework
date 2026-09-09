import pathlib,tempfile,json,types
P=pathlib.Path('/private/tmp/toe-24h-probes-20260908/native-rho4-two-moment-saved-root-review');s=types.ModuleType('schema');exec((P/'schema.py').read_bytes(),s.__dict__)
with tempfile.TemporaryDirectory()as td:
 t=pathlib.Path(td);o=t/'o';o.mkdir();b=t/'b';b.mkdir();(b/'PANELS').mkdir();write=lambda p,x:p.write_text(json.dumps(x));orig={'all_targets_met':True,'rows':[{'observable':n,'interval':['1','1'],'width':'0','status':'CERTIFIED_TARGET'}for n in ('cminus','mu')]};write(b/'RESULT.json',orig);bp=t/'binding';write(bp,{'result':str(b/'RESULT.json')});rf={'binding_path':str(bp),'authorization':{'binding_sha256':'x'},'worker_freeze':'x'};write(o/'STARTED.json',rf['authorization']);r={'status':'PASS_SAVED_TWO_MOMENT_RECONSTRUCTION','source_result_sha256':s.sha(b/'RESULT.json'),'panels':67,'saved_nodes_reconstructed':1742,'saved_integrand_values':3484,'oracle_calls':0,'predicates':1,'rows':[{'observable':n,'interval':['1','1'],'target_pass':True}for n in ('cminus','mu')]};write(o/'PARTIAL.json',{'stage':'complete','predicates':1,'panels':list(range(67)),'current':{'panel':66,'node':1741}})
 for j in range(67):
  write(b/f'PANELS/{j:02d}.json',{'values':[['0','0'],['0','0']]});write(o/f'PANEL_{j:02d}.json',{'panel':j-64,'independent_values':[['0','0'],['0','0']]})
 def seal():
  write(o/'RESULT.json',r);write(o/'WORKER_COMPLETE.json',{'status':'COMPLETE_SAVED_ONLY','runtime_sha256':'x','binding_sha256':'x','result_sha256':s.sha(o/'RESULT.json'),'seconds':1,'rss_bytes':100})
 seal();s.check(o,rf,2);n=1
 for k,v in [('oracle_calls',False),('saved_integrand_values',1742)]:
  old=r[k];r[k]=v;seal()
  try:s.check(o,rf,2)
  except ValueError:n+=1
  else:raise AssertionError(k)
  r[k]=old
 r['rows'][0]['target_pass']=1;seal()
 try:s.check(o,rf,2)
 except ValueError:n+=1
 else:raise AssertionError('target')
 print(n,'synthetic metadata predicates PASS; no actual inputs')
