from pathlib import Path
import numpy as np,json
p=Path(__file__).resolve().parent;exact=json.loads((p/'exact_result.json').read_text())['rows'];out=[]
def gap(c,e,a,b):
 if np.any(c[a:b+1]<=0):return None
 return float((24-e)*(1-np.exp(np.polyfit(np.arange(a,b+1),np.log(c[a:b+1]),1)[0]/24)))
for vi in [0,1]:
 target=np.array(exact[vi]['finite_F_curve']);E=exact[vi]['E0']
 for pop in [512,1024,2048]:
  for burn in [20,40]:
   x=json.loads((p/f'cell_v{vi}_p{pop}_b{burn}.json').read_text());raw=np.array([[b['raw_product_means'] for b in r['blocks']] for r in x['replicas']]);ratio=raw/raw[:,:,0:1,:];rep=ratio.mean(1)[:,:,0];mean=rep.mean(0);se=rep.std(0,ddof=1)/np.sqrt(8)
   nr=raw.mean(1)[:,:,0];dr=nr[:,0];pooled=nr.mean(0)/dr.mean();pse=(nr-pooled[None,:]*dr[:,None]).std(0,ddof=1)/(np.sqrt(8)*dr.mean())
   group=ratio.mean((1,3));gm=group.mean(0);gse=group.std(0,ddof=1)/np.sqrt(8)
   div=np.array([[b['origin_counts_by_tau'] for b in r['blocks']] for r in x['replicas']]);surv=np.array([[b['suffix_distinct_counts_by_tau'] for b in r['blocks']] for r in x['replicas']]);den=raw[:,:,0,0]
   err=mean-target;cons=np.abs(err)<=4*se+1e-8;prec=4*se<=.2*target;energy=np.array([r['mixed_energy'] for r in x['replicas']])
   out.append({'V':x['V'],'population':pop,'burn':burn,'mean_curve':mean.tolist(),'replica_SE':se.tolist(),'pooled_raw_ratio':pooled.tolist(),'pooled_ratio_delta_SE':pse.tolist(),'six_mode_mean':gm.tolist(),'six_mode_replica_SE':gse.tolist(),'errors':err.tolist(),'simultaneous_consistency_failed_tau':np.flatnonzero(~cons[1:]).__add__(1).tolist(),'precision_failed_tau':np.flatnonzero(~prec[1:]).__add__(1).tolist(),'negative_mean_tau':np.flatnonzero(mean<=0).tolist(),'rms_errors':{f'{a}-{b}':float(np.sqrt(np.mean(err[a:b+1]**2))) for a,b in [(1,4),(5,8),(9,16)]},'max_ratio_method_difference':float(max(abs(pooled-mean))),'denominator':{'mean':float(den.mean()),'sd_between_blocks':float(den.std(ddof=1)),'exact_stationary':exact[vi]['denominator']},'origin_tau16_counts':{'minimum':float(div[:,:,16].min()),'mean':float(div[:,:,16].mean())},'suffix_counts':{'minimum':float(surv.min()),'mean':float(surv.mean())},'mean_energy':float(energy.mean()),'energy_SE':float(energy.std(ddof=1)/np.sqrt(8)),'exact_energy':E,'fits':{f'{a}-{b}':{'mean_curve_exact_energy':gap(mean,E,a,b),'exact_F6':gap(target,E,a,b),'valid_independent_replica_fits':sum(gap(r,E,a,b)is not None for r in rep)} for a,b in [(2,6),(8,14)]},'seconds':x['seconds'],'rss_mib':x['rss_mib']})
comparisons=[]
for V in [.95,1.]:
 rows=[r for r in out if r['V']==V]
 pairs=[]
 for pop in [512,1024,2048]:pairs.append((next(r for r in rows if r['population']==pop and r['burn']==20),next(r for r in rows if r['population']==pop and r['burn']==40),'burn'))
 for burn in [20,40]:
  for lo,hi in [(512,1024),(1024,2048)]:pairs.append((next(r for r in rows if r['population']==lo and r['burn']==burn),next(r for r in rows if r['population']==hi and r['burn']==burn),'population'))
 for a,b,kind in pairs:
  diff=np.array(a['mean_curve'])-b['mean_curve'];se=np.sqrt(np.array(a['replica_SE'])**2+np.array(b['replica_SE'])**2)
  comparisons.append({'V':V,'kind':kind,'cells':[[a['population'],a['burn']],[b['population'],b['burn']]],'failed_tau':(np.flatnonzero(abs(diff[1:])>4*se[1:]+1e-8)+1).tolist(),'max_abs_difference':float(max(abs(diff)))})
(p/'SUMMARY.json').write_text(json.dumps({'rows':out,'scaling_comparisons':comparisons,'total_cell_seconds':sum(r['seconds'] for r in out),'max_rss_mib':max(r['rss_mib'] for r in out)},indent=2,allow_nan=False)+'\n')
for r in out:print(r['V'],r['population'],r['burn'],'consistency',r['simultaneous_consistency_failed_tau'],'precision',r['precision_failed_tau'],'rms',r['rms_errors'],'ancestor',r['origin_tau16_counts'])
