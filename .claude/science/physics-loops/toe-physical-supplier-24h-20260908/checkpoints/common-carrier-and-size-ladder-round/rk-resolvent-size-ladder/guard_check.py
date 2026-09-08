import pathlib,json,hashlib,copy
import numpy as np
from analyze import validate,summarize
p=pathlib.Path(__file__).resolve().parent;m=json.loads((p/'PROFILE_L8.json').read_text());m.update(profile=False,burn=32,chains=32,origins_per_chain=64,source_sha=hashlib.sha256((p/'stream.py').read_bytes()).hexdigest());m['rows']=[dict(cid=20000+i) for i in range(32)]
m.update({k:v['sha256'] for k,v in json.loads((p/'DEPENDENCIES.json').read_text()).items()})
d=dict(origins=np.ones((64,12),complex),products=np.ones((64,6,12),complex),Nf=np.ones(64,np.int64),lags=np.zeros((64,6),np.int64),clipped=np.zeros((64,6),bool));validate(m,d,8,32,0,0)
cases=[]
for name in ['hash','duplicatechain','NaN','fractionallag','discard','cap','coverage']:
 mm=copy.deepcopy(m);dd={k:v.copy() for k,v in d.items()}
 if name=='hash':mm['source_sha']='wrong'
 if name=='duplicatechain':mm['rows'][1]['cid']=20000
 if name=='NaN':dd['origins'][0,0]=np.nan
 if name=='fractionallag':dd['lags']=dd['lags'].astype(float)
 if name=='discard':dd['lags'][0,0]=mm['caps'][0]+1;dd['clipped'][0,0]=True
 if name=='cap':mm['caps'][0]+=1
 if name=='coverage':dd['origins']=dd['origins'][:-1]
 try:validate(mm,dd,8,32,0,0)
 except ValueError as e:cases.append(dict(case=name,rejected=str(e)))
 else:raise RuntimeError('mutation survived '+name)
for value in [0.,-1.]:
 out=summarize(np.ones(128),np.ones((128,2)),np.full((128,2,3),value),np.zeros((128,2,3)),8)
 if any(r['valid'] for r in out['rows']):raise RuntimeError('invalid denominator survived')
 cases.append(dict(case='nonpositive_Y_'+str(value),invalid_preserved=True))
(p/'GUARDS.json').write_text(json.dumps(cases,indent=2)+'\n');print(len(cases),'controls')
