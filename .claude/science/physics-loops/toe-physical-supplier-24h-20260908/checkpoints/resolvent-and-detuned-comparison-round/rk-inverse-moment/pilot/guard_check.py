from pathlib import Path
from fractions import Fraction
import ast,json,hashlib,copy,numpy as np
p=Path(__file__).resolve().parent;f=next(x for x in ast.parse((p/'analyze.py').read_text()).body if isinstance(x,ast.FunctionDef) and x.name=='validate_record');ns={'np':np,'Fraction':Fraction,'hashlib':hashlib,'p':p};exec(compile(ast.Module(body=[f],type_ignores=[]),'validate_record','exec'),ns);validate=ns['validate_record'];caps=[800,368,169];alphas=[.25,.5,1.]
m={'L':2,'burn':32,'chains':32,'origins_per_chain':256,'chain_ids':list(range(32)),'modes':[[1,a,b] for a in range(3) for b in range(3) if a!=b],'alphas':alphas,'seconds':1,'rss_mib':1,'exact_rational_tail_comparison':True,'run_sha256':hashlib.sha256((p/'run.py').read_bytes()).hexdigest(),'kernel_sha256':hashlib.sha256((p/'kernel.py').read_bytes()).hexdigest(),'Kmax':caps,'q':[24/(24+a) for a in alphas],'tail_bounds':[float((Fraction(24)/(24+Fraction(str(a))))**(k+1)/Fraction(str(a))) for a,k in zip(alphas,caps)],'clipped_counts':[0,0,0]}
d={'origins':np.zeros((32,256,6),complex),'products':np.zeros((32,256,3,6),complex),'lags':np.zeros((32,256,3),np.int64),'clipped':np.zeros((32,256,3),bool)};validate(m,d,2,32);rows=[]
for name in ['hash','chain','NaN','cap','fractional_lag','flag','nonzero_discard']:
 mm=copy.deepcopy(m);dd={k:v.copy() for k,v in d.items()}
 if name=='hash':mm['run_sha256']='wrong'
 if name=='chain':mm['chain_ids'].pop()
 if name=='NaN':dd['products'][0,0,0,0]=np.nan
 if name=='cap':mm['Kmax'][0]+=1
 if name=='fractional_lag':dd['lags']=dd['lags'].astype(float)
 if name=='flag':dd['clipped'][0,0,0]=True
 if name=='nonzero_discard':dd['lags'][0,0,0]=801;dd['clipped'][0,0,0]=True;mm['clipped_counts'][0]=1;dd['products'][0,0,0,0]=1
 try:validate(mm,dd,2,32)
 except AssertionError:rows.append({'case':name,'rejected':True})
 else:raise AssertionError('guard failed '+name)
(p/'GUARD_RESULT.json').write_text(json.dumps({'valid_fixture':True,'synthetic_only':True,'mutations':rows},indent=2)+'\n')
