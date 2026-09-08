from pathlib import Path
import json,numpy as np
p=Path(__file__).resolve().parent;exact=json.loads((p.parent/'RESULT.json').read_text());out=[];internal={}
for L in [2,4]:
 for burn in [32,128]:
  m=json.loads((p/f'L{L}_b{burn}.json').read_text());d=np.load(p/f'L{L}_b{burn}.npz');o=d['origins'];prod=d['products'];rows=[]
  if o.shape!=(32,256,len(m['modes'])) or prod.shape!=(32,256,3,len(m['modes'])):raise AssertionError('frozen coverage')
  for h in sorted(set(z[0] for z in m['modes'])):
   ix=[i for i,z in enumerate(m['modes']) if z[0]==h];S=(abs(o[:,:,ix])**2).sum(2).mean(1);sm=float(S.mean())
   for j,a in enumerate(m['alphas']):
    Y=prod[:,:,j,ix].real.sum(2).mean(1);I=prod[:,:,j,ix].imag.sum(2).mean(1);valid=sm>0 and Y.mean()>0
    row={'harmonic':h,'alpha':a,'S_mean':sm,'S_SE':float(S.std(ddof=1)/np.sqrt(32)),'numerator_mean':float(Y.mean()),'negative_chain_numerators':int(sum(Y<0)),'imaginary_mean':float(I.mean()),'imaginary_SE':float(I.std(ddof=1)/np.sqrt(32)),'valid':bool(valid),'tail_bound':m['tail_bounds'][j]}
    if valid:
     r=float(Y.mean()/(a*sm));influence=(Y-a*r*S)/(a*sm);se=float(influence.std(ddof=1)/np.sqrt(32));row.update(r_truncated=r,SE=se,b_plugin_from_truncated=1/r-a,b_delta_SE=se/r**2,precision_nominal=bool(4*se<=.1*r));internal[L,burn,h,j]=(r,influence)
     if L==2:
      target=exact['resolvents'][j]['truncated_value'];row.update(exact_truncated_target=target,consistency_nominal=bool(abs(r-target)<=4*se+1e-8))
    rows.append(row)
  out.append({'L':L,'burn':burn,'rows':rows,'clipped_counts':m['clipped_counts']})
comparisons=[]
for L in [2,4]:
 for h in ([1] if L==2 else [1,2]):
  for j in range(3):
   if (L,32,h,j) in internal and (L,128,h,j) in internal:
    a,ia=internal[L,32,h,j];b,ib=internal[L,128,h,j];se=float(np.sqrt(np.var(ia,ddof=1)/32+np.var(ib,ddof=1)/32));comparisons.append({'kind':'burn','L':L,'harmonic':h,'alpha_index':j,'difference':a-b,'SE':se,'flag':bool(abs(a-b)>4*se+1e-8)})
  for burn in [32,128]:
   for j in [0,1]:
    if (L,burn,h,j) in internal and (L,burn,h,j+1) in internal:
     a,ia=internal[L,burn,h,j];b,ib=internal[L,burn,h,j+1];se=float((ia-ib).std(ddof=1)/np.sqrt(32));comparisons.append({'kind':'paired_alpha','L':L,'burn':burn,'harmonic':h,'indices':[j,j+1],'difference':a-b,'SE':se})
(p/'ANALYSIS.json').write_text(json.dumps({'rows':out,'comparisons':comparisons,'scope':'truncated regulated susceptibility, no full inverse or certified spectral bound'},indent=2,allow_nan=False)+'\n')
