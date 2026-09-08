from aggregate import validate_receipts
import copy,json
r=dict(job=0,rep=0,block=0,nodes=1024,freeze='f',seconds=5.,peak_bytes=1000000,component_seconds=[1.,1.,1.,1.]);e=dict(name='job00',returncode=0,failure=None,seconds=6.,external_seconds=5.9,tree_peak_bytes=2000000,external_peak_bytes=1000000)
validate_receipts(r,e,0,'f');count=1
for target,key,bad in [('r','seconds',float('nan')),('r','peak_bytes',-1),('r','component_seconds',[2.,2.,2.,2.]),('r','component_seconds',[1.,1.,1.]),('e','seconds',float('nan')),('e','external_seconds',-1),('e','tree_peak_bytes',float('nan')),('e','external_peak_bytes',0),('e','name','job01')]:
 a,b=copy.deepcopy(r),copy.deepcopy(e);(a if target=='r' else b)[key]=bad
 try:validate_receipts(a,b,0,'f')
 except ValueError:pass
 else:raise ValueError('corrupt receipt survived '+key)
 count+=1
print(json.dumps(dict(controls=count,scope='synthetic raw resource guards; no grid')))
