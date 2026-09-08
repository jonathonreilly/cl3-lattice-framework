import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS']:os.environ[k]='1'
import numpy as np,json,pathlib,ast,hashlib
base=pathlib.Path('/private/tmp/toe-24h-probes-20260908');a=base/'ice-estimator-calibration';b=base/'ice-estimator-replication';checks={}
def ck(k,v):checks[k]=bool(v);assert v,k
def same(x,y):return np.allclose(x,y,rtol=1e-12,atol=1e-14)
orig=ast.parse((a/'producer_original.py').read_text());f=next(n for n in orig.body if isinstance(n,ast.FunctionDef) and n.name=='measure_correlation_block');f.name='measure_raw_block';ret=f.body[-1];ret.value.elts[2]=ast.Name(id='correlation',ctx=ast.Load());g=next(n for n in ast.parse((a/'measurement_derivative.py').read_text()).body if isinstance(n,ast.FunctionDef))
ck('exact_AST_instrumentation',ast.dump(f,include_attributes=False)==ast.dump(g,include_attributes=False))
for name in ['producer_original.py','measurement_derivative.py']:ck('replication_bytes_'+name,(a/name).read_bytes()==(b/name).read_bytes())
summary=json.loads((a/'SUMMARY.json').read_text());allseeds=[]
for r in summary['rows']:
 vi=0 if r['V']==.95 else 1;p=r['population'];burn=r['burn'];d=json.loads((a/f'cell_v{vi}_p{p}_b{burn}.json').read_text());allseeds.extend(x['seed'] for x in d['replicas']);raw=np.array([[z['raw_product_means'] for z in x['blocks']] for x in d['replicas']])[:,:,:,0]
 ratios=raw/raw[:,:,0,None];rep=ratios.mean(axis=1);mean=rep.mean(0);se=np.sqrt(np.sum((rep-mean)**2,axis=0)/(8*7));target=np.array(json.loads((a/'exact_result.json').read_text())['rows'][vi]['finite_F_curve'])
 ck(f'calibration_{vi}_{p}_{burn}',same(mean,r['mean_curve']) and same(se,r['replica_SE']) and np.array_equal(np.where(abs(mean[1:]-target[1:])>4*se[1:]+1e-8)[0]+1,r['simultaneous_consistency_failed_tau']))
ck('calibration96_distinct_seeds',len(allseeds)==96 and len(set(allseeds))==96)
summ=json.loads((b/'SUMMARY.json').read_text());adverse=[]
for r in summ['rows']:
 p=r['population'];reps=sum([json.loads((b/f'p{p}_batch{k}.json').read_text())['replicas'] for k in range(4)],[]);allseeds.extend(x['seed'] for x in reps);raw=np.array([[z['raw'] for z in x['blocks']] for x in reps])[:,:,:,0];rr=raw/raw[:,:,0,None];rep=rr.mean(1);m=rep.mean(0);se=np.sqrt(((rep-m)**2).sum(0)/(128*127));N=raw.mean(1);D=N[:,0];ratio=N.sum(0)/D.sum();res=N-ratio*D[:,None];pse=np.sqrt((res-res.mean(0)) .__pow__(2).sum(0)/(128*127))/D.mean()
 ck(f'replication_{p}',same(m,r['mean_of_block_ratios']) and same(se,r['replica_SE']) and same(ratio,r['pooled_raw_ratio']) and same(pse,r['pooled_delta_SE']))
 # Deliberate pseudoreplication gives a different SE: preserve descriptive comparison, not a universal direction theorem.
 wrong=rr.reshape(-1,4).std(0,ddof=1)/np.sqrt(512);adverse.append({'population':p,'correct_tau3_SE':float(se[3]),'wrong_block_independent_SE':float(wrong[3])})
 ck(f'pseudoreplication_detected_{p}',not same(wrong,se))
ck('all352_seeds_unique',len(allseeds)==352 and len(set(allseeds))==352)
# Exact target agrees with my earlier independent spectral implementation (different row order).
e=json.loads((a/'exact_result.json').read_text());old=json.loads((base/'ice-physics/RESULT.json').read_text())
for row in e['rows']:
 z=next(z for z in old['rows'] if z['V']==row['V']);ck('exact_target_'+str(row['V']),same(row['finite_F_curve'],z['forward']['6']['curve']) and same(row['pure_curve'],z['pure_curve']))
print(json.dumps({'count':len(checks),'checks':checks,'pseudoreplication_adverse':adverse},indent=2))
