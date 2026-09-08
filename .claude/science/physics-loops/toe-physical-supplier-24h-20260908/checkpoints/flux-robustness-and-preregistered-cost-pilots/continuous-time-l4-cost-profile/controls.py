"""Synthetic accounting controls only; no RNG/path execution."""
import copy,json
from forecast import calculate
from adapter import NAMES
r={'names':NAMES,'cases':[]}
for i in range(4):
 r['cases'].append(dict(cid=i,T=(.5,.5,2.,2.)[i],start=('constant','propagated','constant','propagated')[i],seed=202609420000+i,blocks=[dict(face=f,seconds=.001) for f in (0,64,128,191)],measurements=[dict.fromkeys(NAMES,1.) for _ in range(4)],measurement_seconds=[.002]*4,initialization_seconds=.01,io_seconds=.003,final_io_seconds=.001,postblock_io_seconds=[.0005]*4,postblock_paths=[dict(file=f'path{i}_block{j}.json',sha='0'*64) for j in range(4)],synthetic_output_seconds=.004,synthetic_rows=128,synthetic_batches=16,case_seconds=.03))
a=calculate(r,30.)
if a['arms'][0]['measurement_count']!=128:raise ValueError('measurement accounting')
for key,value in [('measurement_seconds',[]),('synthetic_rows',4),('seed',0),('postblock_paths',[]),('postblock_io_seconds',[0.]*4)]:
 z=copy.deepcopy(r);z['cases'][0][key]=value
 try:calculate(z,30.)
 except ValueError:pass
 else:raise ValueError('mutant survived '+key)
expected=2*(192*(16+128)*.001+128*.002+.01+.003+.004+(30-4*.029))
if abs(a['arms'][0]['per_chain']-expected)>1e-10:raise ValueError('full accounting formula')
print(json.dumps(dict(controls=7,scope='synthetic forecast only',per_chain=a['arms'][0]['per_chain'])))
