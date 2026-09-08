import pathlib,json,copy,hashlib
from analyze import validate
p=pathlib.Path(__file__).resolve().parent;x=json.loads((p/'MEASUREMENT_MICRO.json').read_text());x.update(micro=False,cell=0,shard=0,n=1536,tau=4,burn_multiplier=8,updates=98304,chains=2)
x['rows']=[copy.deepcopy(x['rows'][0]) for _ in range(2)]
for i,r in enumerate(x['rows']):r.update(cid=i,seed=202609160000+i);r['counters'].update(accepted=98304,rejections=0,accepted_self=0,self_proposals=0)
validate(x,0,0);out=[]
for name in ['source','seed','NaN','negativecount','batchmean']:
 y=copy.deepcopy(x)
 if name=='source':y['source_sha']='wrong'
 if name=='seed':y['rows'][1]['seed']=0
 if name=='NaN':y['rows'][0]['mean'][0]=float('nan')
 if name=='negativecount':y['rows'][0]['counters']['rejections']=-1
 if name=='batchmean':y['rows'][0]['mean'][0]+=1
 try:validate(y,0,0)
 except ValueError as e:out.append(dict(case=name,rejected=str(e)))
 else:raise RuntimeError('survived '+name)
(p/'GUARDS.json').write_text(json.dumps(out,indent=2)+'\n')
