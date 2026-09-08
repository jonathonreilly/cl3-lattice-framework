from pathlib import Path
import json,hashlib,numpy as np
from fractions import Fraction
p=Path(__file__).resolve().parent;exact=json.loads((p.parent/'RESULT.json').read_text());out=[];internal={}
def validate_record(m,d,L,burn):
 expected_modes=[[h,a,b] for h in ([1] if L==2 else [1,2]) for a in range(3) for b in range(3) if a!=b]
 ids=list(range(([2,4].index(L)*2+[32,128].index(burn))*32,([2,4].index(L)*2+[32,128].index(burn))*32+32))
 if not(m['L']==L and m['burn']==burn and m['chains']==32 and m['origins_per_chain']==256 and m['chain_ids']==ids and m['modes']==expected_modes and m['alphas']==[.25,.5,1.]):raise AssertionError('frozen metadata')
 if not(0<m['seconds']<120 and 0<m['rss_mib']<384 and m['exact_rational_tail_comparison'] is True):raise AssertionError('resource or tail receipt')
 if m['run_sha256']!=hashlib.sha256((p/'run.py').read_bytes()).hexdigest() or m['kernel_sha256']!=hashlib.sha256((p/'kernel.py').read_bytes()).hexdigest():raise AssertionError('source receipt')
 M=3*L**3;caps=[800,368,169] if L==2 else [6373,2922,1329]
 if m['Kmax']!=caps:raise AssertionError('lag cap')
 for j,a in enumerate([Fraction(1,4),Fraction(1,2),Fraction(1)]):
  q=Fraction(M)/(M+a);bound=q**(caps[j]+1)/a
  if not(bound<=Fraction(1,1000) and q**caps[j]/a>Fraction(1,1000) and abs(m['q'][j]-float(q))<1e-15 and abs(m['tail_bounds'][j]-float(bound))<1e-15):raise AssertionError('rational tail')
 o=d['origins'];y=d['products'];lags=d['lags'];flags=d['clipped'];nm=len(expected_modes)
 if o.shape!=(32,256,nm) or y.shape!=(32,256,3,nm) or lags.shape!=(32,256,3) or flags.shape!=lags.shape:raise AssertionError('array coverage')
 if not(np.iscomplexobj(o) and np.iscomplexobj(y) and np.isfinite(o).all() and np.isfinite(y).all() and np.issubdtype(lags.dtype,np.integer) and np.all(lags>=0) and flags.dtype==np.bool_):raise AssertionError('finite typed arrays')
 if not(np.array_equal(flags,lags>np.array(caps)) and np.all(y[flags]==0) and np.array_equal(np.sum(flags,axis=(0,1)),m['clipped_counts'])):raise AssertionError('discarded lag accounting')

for L in [2,4]:
 for burn in [32,128]:
  m=json.loads((p/f'L{L}_b{burn}.json').read_text());d=np.load(p/f'L{L}_b{burn}.npz');validate_record(m,d,L,burn);o=d['origins'];prod=d['products'];rows=[];joint=[];joint_labels=[];infls=[];infl_labels=[]
  if o.shape!=(32,256,len(m['modes'])) or prod.shape!=(32,256,3,len(m['modes'])):raise AssertionError('frozen coverage')
  for h in sorted(set(z[0] for z in m['modes'])):
   ix=[i for i,z in enumerate(m['modes']) if z[0]==h];S=(abs(o[:,:,ix])**2).sum(2).mean(1);sm=float(S.mean());joint.append(S);joint_labels.append(['S',h])
   for j,a in enumerate(m['alphas']):
    Y=prod[:,:,j,ix].real.sum(2).mean(1);I=prod[:,:,j,ix].imag.sum(2).mean(1);joint.append(Y);joint_labels.append(['Y',h,a]);valid=sm>0 and Y.mean()>0
    row={'harmonic':h,'alpha':a,'S_mean':sm,'S_SE':float(S.std(ddof=1)/np.sqrt(32)),'numerator_mean':float(Y.mean()),'negative_chain_numerators':int(sum(Y<0)),'imaginary_mean':float(I.mean()),'imaginary_SE':float(I.std(ddof=1)/np.sqrt(32)),'valid':bool(valid),'tail_bound':m['tail_bounds'][j]}
    if valid:
     r=float(Y.mean()/(a*sm));influence=(Y-a*r*S)/(a*sm);se=float(influence.std(ddof=1)/np.sqrt(32));row.update(r_truncated=r,SE=se,b_plugin_from_truncated=1/r-a,b_delta_SE=se/r**2,precision_nominal=bool(4*se<=.1*r));internal[L,burn,h,j]=(r,influence);infls.append(influence);infl_labels.append([h,a])
     if L==2:
      target=exact['resolvents'][j]['truncated_value'];row.update(exact_truncated_target=target,consistency_nominal=bool(abs(r-target)<=4*se+1e-8))
    rows.append(row)
  out.append({'L':L,'burn':burn,'rows':rows,'clipped_counts':m['clipped_counts'],'joint_chain_labels':joint_labels,'joint_chain_means':np.array(joint).T.tolist(),'joint_chain_sample_covariance':np.cov(joint,ddof=1).tolist(),'influence_labels':infl_labels,'joint_influence_sample_covariance':np.cov(infls,ddof=1).tolist() if len(infls)>1 else None})
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
