from pathlib import Path
import numpy as np,json
P=Path(__file__).resolve().parent

def ac_diagnostic(x):
 # Within-chain centering; finite-window initial-positive autocorrelation diagnostic.
 x=x-x.mean(1,keepdims=True);var=np.mean(x*x);rho=[]
 if var<1e-25:return {'tau_integrated':None,'ESS':None,'rho':[]}
 for lag in range(1,65):rho.append(float(np.mean(x[:,:-lag]*x[:,lag:])/var))
 total=1.
 for r in rho:
  if r<=0:break
  total+=2*r
 return {'tau_integrated':total,'ESS':x.size/total,'rho':rho}
rows=[]
for L in[2,4]:
 for burn in[32,128]:
  receipt=json.loads((P/f'L{L}_b{burn}.json').read_text());d=np.load(P/f'L{L}_b{burn}.npz');x=d['values'];cm=x.mean(1);rawmean=cm.mean(0);mode_rows=[]
  for m,mode in enumerate(receipt['modes']):
   S=rawmean[m,2];seS=cm[:,m,2].std(ddof=1)/np.sqrt(32);r={'mode':mode,'S':float(S),'S_SE':float(seS),'O_mean':rawmean[m,:2].tolist(),'O_SE':(cm[:,m,:2].std(0,ddof=1)/np.sqrt(32)).tolist(),'S_ac':ac_diagnostic(x[:,:,m,2])}
   for slot,name in[(3,'mu1'),(4,'mu2')]:
    mu=rawmean[m,slot]/S;infl=cm[:,m,slot]-mu*cm[:,m,2];se=infl.std(ddof=1)/(np.sqrt(32)*S)
    blocks=x[:,:,m,:].reshape(32,16,16,5).mean(2);bi=blocks[:,:,slot]-mu*blocks[:,:,2];blockse=bi.std(ddof=1)/(np.sqrt(512)*S)
    halves=x[:,:,m,:].reshape(32,2,128,5).mean(2);hr=halves[:,:,slot]/halves[:,:,2];hd=hr[:,0]-hr[:,1];splitmean=hd.mean();splitse=hd.std(ddof=1)/np.sqrt(32)
    r[name]={'ratio':float(mu),'chain_delta_SE':float(se),'mean_chain_ratio':float(np.mean(cm[:,m,slot]/cm[:,m,2])),'block16_naive_SE_diagnostic':float(blockse),'within_chain_ac':ac_diagnostic(x[:,:,m,slot]-mu*x[:,:,m,2]),'paired_split_difference':float(splitmean),'paired_split_SE':float(splitse),'split_flag':bool(abs(splitmean)>4*splitse+1e-8)}
   if L==2:r['L2_consistency']={'S':bool(abs(S-5/12)<=4*seS+1e-8),'mu1':bool(abs(r['mu1']['ratio']-8/5)<=4*r['mu1']['chain_delta_SE']+1e-8),'mu2':bool(abs(r['mu2']['ratio']-16/5)<=4*r['mu2']['chain_delta_SE']+1e-8)}
   # Saved configurations are correlated; variance-cost is an empirical diagnostic.
   alln=d['all_face_numerator'][:,m];onen=d['one_face_numerator'][:,m];tim=receipt['timing_seconds_per_snapshot'];varall=float(np.var(alln,ddof=1));varone=float(np.var(onen,ddof=1))
   r['numerator_variance_cost']={'one_face_variance':varone,'conditioned_variance':varall,'one_face_seconds':tim['1'],'all_face_seconds':tim['0'],'count_formula_seconds':tim['2'],'all_over_one_variance_cost':float(varall*tim['0']/(varone*tim['1'])),'count_over_one_variance_cost':float(varall*tim['2']/(varone*tim['1']))}
   snapS=x[:,:64,m,2].reshape(-1);mu=r['mu1']['ratio']
   vi_all=float(np.var(alln-mu*snapS,ddof=1));vi_one=float(np.var(onen-mu*snapS,ddof=1))
   r['ratio_influence_variance_cost']={'one_face':vi_one,'conditioned':vi_all,'all_over_one':float(vi_all*tim['0']/(vi_one*tim['1'])),'count_over_one':float(vi_all*tim['2']/(vi_one*tim['1']))}
   mode_rows.append(r)
  rows.append({'L':L,'burn':burn,'modes':mode_rows,'seconds':receipt['seconds'],'rss_mib':receipt['rss_mib']})
comparisons=[]
for L in[2,4]:
 a=next(r for r in rows if r['L']==L and r['burn']==32);b=next(r for r in rows if r['L']==L and r['burn']==128)
 for x,y in zip(a['modes'],b['modes']):
  for name in['mu1','mu2']:
   diff=x[name]['ratio']-y[name]['ratio'];se=np.hypot(x[name]['chain_delta_SE'],y[name]['chain_delta_SE']);comparisons.append({'L':L,'mode':x['mode'],'quantity':name,'burn_difference':diff,'combined_SE':float(se),'flag':bool(abs(diff)>4*se+1e-8)})
  diff=x['S']-y['S'];se=np.hypot(x['S_SE'],y['S_SE']);comparisons.append({'L':L,'mode':x['mode'],'quantity':'S','burn_difference':diff,'combined_SE':float(se),'flag':bool(abs(diff)>4*se+1e-8)})
(P/'SUMMARY.json').write_text(json.dumps({'rows':rows,'burn_comparisons':comparisons,'scope':'finite diagnostics; no mixing certificate or pole inference'},indent=2,allow_nan=False)+'\n')
