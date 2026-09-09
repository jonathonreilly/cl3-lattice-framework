import pathlib,json,types,hashlib,copy
p=pathlib.Path(__file__).resolve().parent;s=p.parent/'native-sparse-pivot-action-root-review';m=types.ModuleType('schema');exec(compile((s/'schema.py').read_bytes(),str(s/'schema.py'),'exec'),m.__dict__)
def write(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x)+'\n')
old=p/'old';out=p/'out';out.mkdir();restore=p/'restore.json';plan=p/'plan.json';write(restore,{'pilot_output':str(old)});write(plan,{'restore_binding':str(restore)})
rf={'authorization':{'binding_sha256':'b'},'worker_freeze':'w','binding_path':str(plan)};write(out/'STARTED.json',rf['authorization']);rows=[]
for oi in range(5):
 d=out/f'ORBIT_{oi}';d.mkdir();h={'history':[{}]*4,'context':{}};write(old/f'ORBIT_{oi}/HISTORY.json',h);write(d/'RESTORED_STATE.json',{'history':h['history'],'original_context':{},'history_sha256':m.sha(old/f'ORBIT_{oi}/HISTORY.json')})
 R=[];U=[[q,g] for q in (396,399,400,401) for g in(0,1)];cols=[[] for _ in range(8)];write(d/'COEFFICIENTS.json',{'R':R,'columns':cols});ev=[{'orbit':oi,'stage':'coefficient_enclosed','pair':j} for j in range(4)]+[{'orbit':oi,'stage':'principal_gram_complete','U':U,'entries':[[*a,*b,0,0] for ii,a in enumerate(U) for b in U[ii:]]}];rs=[]
 for q in(399,400):
  z={'impurity_bare_index':q,'columns':cols,'action_columns':cols,'T':[[[0,0] for _ in range(8)] for _ in range(8)],'G':[[[0,0] for _ in range(8)] for _ in range(8)],'L':[[[0,0] for _ in range(8)] for _ in range(8)],'delta_squared_upper_numerator':0,'denominator':m.S,'leakage_target':'1/1000000','leakage_pass':True};rs.append(z);ev.append({'orbit':oi,'stage':'action_enclosed',**z})
 write(d/'RESULT.json',{'status':'COMPLETE_CONDITIONAL_ACTION_ENCLOSURE','midpoint_isometry_claim':False,'R':R,'U':U,'results':rs});(d/'EVENTS.ndjson').write_text(''.join(json.dumps(x)+'\n' for x in ev));rows.append({'orbit':oi,'status':'COMPLETE_CONDITIONAL_ACTION_ENCLOSURE','result_sha256':m.sha(d/'RESULT.json'),'events_sha256':m.sha(d/'EVENTS.ndjson')})
r={'status':'COMPLETE_FIXED_FOUR_PAIR_SPARSE_ACTION','seconds':1,'original_pairs':4,'continuation_used':False,'midpoint_isometry_claim':False,'orbits':rows};write(out/'RESULT.json',r);write(out/'PARTIAL.json',{'stage':'complete','completed_orbits':rows});w={'status':'COMPLETE_SPARSE_ACTION_ONLY','freeze_sha256':'w','binding_sha256':'b','result_sha256':m.sha(out/'RESULT.json'),'seconds':2,'rss_bytes':1000,'continuation_used':False};write(out/'WORKER_COMPLETE.json',w);m.check(out,rf,3);n=1
for key,val in [('original_pairs',12),('continuation_used',True),('midpoint_isometry_claim',True)]:
 bad=copy.deepcopy(r);bad[key]=val;write(out/'RESULT.json',bad);w['result_sha256']=m.sha(out/'RESULT.json');write(out/'WORKER_COMPLETE.json',w)
 try:m.check(out,rf,3)
 except ValueError:n+=1
 else:raise ValueError(key)
write(p/'RESULT.json',{'status':'PASS_FABRICATED_SCHEMA','cases':n,'native_calls':0,'scope':'schema only, synthetic matrices not a physical isometry'});print(n)
