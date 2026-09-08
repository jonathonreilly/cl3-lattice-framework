import runpy,json,copy
from pathlib import Path
c=runpy.run_path(str(Path(__file__).with_name('common.py')));p=c['read'](Path(__file__).with_name('PLAN.json'));n=0
def ck(x):
 global n
 if not x:raise ValueError('control')
 n+=1
ck([i for s in p['shards'] for i in s]==list(range(4986)));ck(len(p['shards'])==52 and max(map(len,p['shards']))==96)
for row in p['cases']:
 for k in row['keys']:ck(sum(1<<e for e in k['used'])==int(row['mask']) and len(k['used'])==2*k['order'])
 ck(row['representative']==sorted(row['keys'],key=lambda x:(x['name'],x['used']))[0])
r={'index':0,'case':p['cases'][0],'gap_lower':'-1/2','positive':False};c['rowscheck']([r],[0],p);ck(True)
for key,value in [('positive',True),('index',1),('case',p['cases'][1])]:
 q=copy.deepcopy(r);q[key]=value
 try:c['rowscheck']([q],[0],p)
 except ValueError:ck(True)
 else:raise ValueError('mutant survived')
print(json.dumps({'status':'PASS','predicates':n,'scope':'geometry/key/coverage and signed-row adversaries; no gap calls'}))
