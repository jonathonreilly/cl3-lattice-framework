import json,numpy as np
from pathlib import Path
p=Path(__file__).resolve().parent;t=np.array(json.loads((p.parent/'ice-estimator-calibration/exact_result.json').read_text())['rows'][0]['finite_F_curve'][:4]);out=[]
for pop in[512,2048]:
 cells=[json.loads((p/f'p{pop}_batch{b}.json').read_text()) for b in range(4)];reps=sum([x['replicas'] for x in cells],[]);assert len(reps)==128 and len({x['seed'] for x in reps})==128
 raw=np.array([[b['raw'] for b in r['blocks']]for r in reps]);N=raw[:,:,:,0];D=N[:,:,0];rat=N/D[:,:,None];rep=rat.mean(1);mean=rep.mean(0);se=rep.std(0,ddof=1)/np.sqrt(128)
 rn=N.mean(1);rd=D.mean(1);pooled=rn.mean(0)/rd.mean();pse=(rn-pooled*rd[:,None]).std(0,ddof=1)/(np.sqrt(128)*rd.mean())
 cov=np.array([np.cov(rn[:,j],rd,ddof=1)[0,1]for j in range(4)])
 bcov=np.array([np.cov(N[:,:,j].ravel(),D.ravel(),ddof=1)[0,1]for j in range(4)]);muN=N.mean((0,1));muD=D.mean();approx=muN*D.var(ddof=1)/muD**3-bcov/muD**2
 sd=rep.std(0,ddof=1);skew=np.zeros(4);skew[1:]=np.mean((rep[:,1:]-mean[1:])**3,axis=0)/sd[1:]**3
 row={'population':pop,'replicas':128,'mean_of_block_ratios':mean.tolist(),'replica_SE':se.tolist(),'pooled_raw_ratio':pooled.tolist(),'pooled_delta_SE':pse.tolist(),'exact':t.tolist(),'errors':(mean-t).tolist(),'z_scores':((mean[1:]-t[1:])/se[1:]).tolist(),'consistency_fail_tau':(np.flatnonzero(abs(mean[1:]-t[1:])>4*se[1:]+1e-8)+1).tolist(),'pooled_consistency_fail_tau':(np.flatnonzero(abs(pooled[1:]-t[1:])>4*pse[1:]+1e-8)+1).tolist(),'numerator_replica_means':rn.mean(0).tolist(),'denominator_mean':float(rd.mean()),'denominator_replica_SD':float(rd.std(ddof=1)),'numerator_denominator_replica_covariance':cov.tolist(),'numerator_denominator_block_covariance':bcov.tolist(),'meanratio_minus_pooled':(mean-pooled).tolist(),'second_order_ratio_bias_approximation':approx.tolist(),'replica_skewness':skew.tolist(),'replica_min':rep.min(0).tolist(),'replica_max':rep.max(0).tolist(),'replica_quantiles':np.quantile(rep,[.025,.25,.5,.75,.975],axis=0).tolist(),'negative_replica_counts':(rep<0).sum(0).tolist(),'tau3_replica_values':rep[:,3].tolist(),'seconds':sum(x['seconds']for x in cells),'rss_mib':max(x['rss_mib']for x in cells)};out.append(row)
a,b=out;diff=np.array(a['mean_of_block_ratios'])-b['mean_of_block_ratios'];se=np.sqrt(np.array(a['replica_SE'])**2+np.array(b['replica_SE'])**2)
result={'rows':out,'population_comparison':{'difference512_minus2048':diff.tolist(),'combined_SE':se.tolist(),'failed_tau':(np.flatnonzero(abs(diff[1:])>4*se[1:]+1e-8)+1).tolist()},'seconds':sum(x['seconds']for x in out)}
(p/'SUMMARY.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
for r in out:print(r['population'],'mean',r['mean_of_block_ratios'],'SE',r['replica_SE'],'z',r['z_scores'],'pooled',r['pooled_raw_ratio'],'cov',r['numerator_denominator_replica_covariance'],'skew',r['replica_skewness'])
print(result['population_comparison'],result['seconds'])
