from pathlib import Path
import types,sys,json,copy
B=Path('/private/tmp/toe-24h-probes-20260908/native-coarse-witness-continuation-design')
# prefix only needs binder.sha; it is not called by grammar.
m=types.ModuleType('binder');m.sha=lambda p:None;sys.modules['binder']=m;p=types.ModuleType('prefix');exec(compile((B/'prefix.py').read_bytes(),str(B/'prefix.py'),'exec'),p.__dict__)
z=lambda n,m:[[['0','0']for _ in range(m)]for _ in range(n)];ev=[]
def add(stage,case,data):ev.append({'current':{'stage':stage,'case':case},'data':data})
plan={'files':{'T_'+str(i):{'sha256':'synthetic'+str(i)}for i in range(5)}}
for i in range(5):add('mapped_T',0,{'orbit':i,'source_sha256':'synthetic'+str(i),'mapped':z(48,48),'operator_squared_upper':'1'})
cases=[]
for ci in range(4):
 add('factorization',ci,{'local':z(7,48),'projector_columns':z(48,7)})
 for n in range(21,379 if ci<3 else 211,21):add('witness_panel',ci,{'completed':n,'direct':z(7,7),'mixed':z(7,7)})
 if ci<3:
  add('witness_block',ci,{'block':z(7,7)});cases.append({'squared_block_lower':'0','excludes_tau_1e9':False,'status':'INDETERMINATE_COARSE_WITNESS','stored_operator':'minus_i_times_positive_projector_difference','metric_and_tail_charged':True,'orbit':ci//2,'impurity':ci%2+1})
assert len(ev)==76;p.grammar(ev,cases,plan,lambda *_:None);n=1
for mode in ['boundary','hash','flag','case']:
 bad=copy.deepcopy(ev);cs=copy.deepcopy(cases)
 if mode=='boundary':bad[-1]['data']['completed']=209
 if mode=='hash':bad[0]['data']['source_sha256']='wrong'
 if mode=='flag':cs[0]['excludes_tau_1e9']=True
 if mode=='case':bad[-1]['current']['case']=True
 try:p.grammar(bad,cs,plan,lambda *_:None)
 except ValueError:n+=1
 else:raise AssertionError(mode)
print({'status':'PASS_SYNTHETIC_PREFIX','checks':n,'actual_prefix_read':False})
