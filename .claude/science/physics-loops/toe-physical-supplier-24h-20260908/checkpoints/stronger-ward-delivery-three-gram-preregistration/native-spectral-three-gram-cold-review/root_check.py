# Independent source-only affine containment and screened-scope controls.
import pathlib,sys,importlib.util,json
from fractions import Fraction as F
B=pathlib.Path('/private/tmp/toe-24h-probes-20260908');sys.path.insert(0,str(B/'native-spectral-three-gram-saved-design'));import gram
sp=importlib.util.spec_from_file_location('root_schema',B/'native-spectral-three-gram-root-review/schema.py');s=importlib.util.module_from_spec(sp);sp.loader.exec_module(s)
n=0
for C,A in [((1,2,3),(2,-1,1)),((-2,1,-1),(3,2,2))]:
 for ov in [0,1,2]:
  c=(F(1,8),F(3,8));v=gram.kernels(tuple(gram.P(x)for x in C),tuple(gram.P(x)for x in A),c,ov);truth=s.form(tuple(map(F,C)),tuple(map(F,A)),c,ov)
  for a,b in zip(v,truth):assert a[0]<=b[0]<=b[1]<=a[1];n+=1
inp={'c':['1/4','1/4'],'nominal':['-2','-1'],'spectral_alpha_interval':['-5','5'],'E_upper':'1','F_upper':'1','coefficients':{}};ev=[];ans=gram.evaluate(inp,lambda st,d:ev.append({'stage':st,'data':s.enc(d)}));ans=s.enc(ans);ans['mode']='residual';s.validate_choice(inp,ans,ev,'residual');n+=1
for key,value in [('true_alpha_excluded',True),('ordered_pairs',False),('screen_upper','1')]:
 bad=dict(ans);bad[key]=value
 try:s.validate_choice(inp,bad,ev,'residual')
 except ValueError:n+=1
 else:raise AssertionError('accepted '+key)
print(json.dumps({'checks':n,'scope':'independent synthetic schema interaction','native_calls':0}))
