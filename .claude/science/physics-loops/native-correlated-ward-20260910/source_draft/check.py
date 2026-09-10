"""Compact evidence semantics and synthetic algebra; no native/Wick replay."""
import pathlib,json,hashlib,gzip,math,copy
from fractions import Fraction as F
D=pathlib.Path(__file__).resolve().parent
h=lambda b:hashlib.sha256(b).hexdigest()
def need(v):
 if not v:raise ValueError('validation failed')
def integer(v,n):need(type(v)is int and v==n)
def rat(v):
 need(type(v)is str and len(v)<=20000);x=F(v);need(str(x)==v and max(x.numerator.bit_length(),x.denominator.bit_length())<=32768);return x
def box(v):need(type(v)is list and len(v)==2);a,b=map(rat,v);need(a<=b);return a,b
def timer(v,c):need(type(v)in(int,float)and math.isfinite(v)and 0<v<c)
def memory(v):need(type(v)is int and 0<v<=384*1048576)
def validate(tag,b):
 o={k:json.loads(v)for k,v in b.items()if k.endswith('.json')};r=o['RESULT.json'];w=o['WORKER_COMPLETE.json'];a=o['ROOT_ACCEPTANCE.json'];e=o['RECEIPT.json'];s=o['SCHEMA_ACCEPTANCE.json'];rf=o['ROOT_FREEZE.json'];dual=tag=='dual'
 need(a['once']is True);need(a['result_sha256']==w['result_sha256']==s['result_sha256']==h(b['RESULT.json']));need(a['schema_sha256']==h(b['SCHEMA_ACCEPTANCE.json'])and a['schema']==s)
 need(a['root_freeze']==h(b['ROOT_FREEZE.json']));need(a['worker_freeze']==w['runtime_sha256']==rf['worker_freeze']==e['worker_freeze']==h(b['RUNTIME_FREEZE.json']));need(w['binding_sha256']==h(b['BINDING.json']))
 need(e['pass']is True and e['failure']is None);integer(e['returncode'],0)
 for v,c in [(r['seconds'],29 if dual else 19),(w['seconds'],29 if dual else 19),(e['seconds'],29.5 if dual else 19.5),(a['external_seconds'],30 if dual else 20)]:timer(v,c)
 need(r['seconds']<=w['seconds']<=e['seconds']<=a['external_seconds'])
 for v in [w['rss_bytes'],a['external_rss_bytes'],a['sampled_whole_tree_peak'],e['sampled_whole_tree_peak']]:memory(v)
 need(a['sampled_whole_tree_peak']==e['sampled_whole_tree_peak']);integer(r['choices'],2);integer(r['events'],763 if dual else 223);integer(s['count'],2);integer(s['events'],r['events']);need(s['native_replay']is False)
 need(r['status']==('COMPLETE_NEW_REDUCED_DUAL_ESTIMATOR'if dual else'COMPLETE_NEW_SAVED_THREE_GRAM_ESTIMATOR'))
 need(w['status']==('COMPLETE_NEW_REDUCED_DUAL_ONLY'if dual else'COMPLETE_NEW_SAVED_THREE_GRAM_ONLY'))
 need(a['status']==('ACCEPTED_NEW_REDUCED_SIGNED_DUAL_ONCE'if dual else'ACCEPTED_NEW_SAVED_THREE_GRAM_SCREEN_ONCE'))
 for k in ['native_oracle_calls','old_moments_recomputed','old_nominal_recomputed']:integer(r[k],0)
 need(type(r['rows'])is list and len(r['rows'])==2)
 for mode,row in zip(['residual','variational'],r['rows']):
  need(row['mode']==mode and row==o[mode+'.json']);lo,hi=box(row['alpha_interval']);need(lo<=0<=hi)
  if dual:
   need(row['status']=='INDETERMINATE_SIGN'and row['physical_trial_changed']is False);integer(row['actual_Wick_words'],342);integer(row['unique_gram_sets'],2);integer(row['logical_Wick_words'],2565)
   need(len(row['candidates'])==5 and [x['lambda']for x in row['candidates']]==['0','1/2','1','3/2','2']);need(len(row['channels'])==15)
   prior=box(row['spectral_alpha_interval']);intervals=[box(x['alpha_interval'])for x in row['candidates']]
   need(lo==max([prior[0]]+[x[0]for x in intervals])and hi==min([prior[1]]+[x[1]for x in intervals]));need(row['alpha_interval']==row['candidates'][2]['alpha_interval'])
  else:
   need(row['status']=='ZERO_DUAL_POSITIVE_CERTIFICATE_EXCLUDED');integer(row['ordered_pairs'],0);integer(row['kernel_values'],0);need(row['true_alpha_excluded']is False and row['other_duals_excluded']is False);need(rat(row['screen_upper'])<=0)
 return True
def enc(x):return json.dumps(x,sort_keys=True).encode()
def mutate(b,fn):
 b=copy.deepcopy(b);r=json.loads(b['RESULT.json']);fn(r);b['RESULT.json']=enc(r)
 for row in r['rows']:b[row['mode']+'.json']=enc(row)
 for key in ['WORKER_COMPLETE.json','SCHEMA_ACCEPTANCE.json']:
  x=json.loads(b[key]);x['result_sha256']=h(b['RESULT.json']);b[key]=enc(x)
 a=json.loads(b['ROOT_ACCEPTANCE.json']);a['result_sha256']=h(b['RESULT.json']);a['schema']=json.loads(b['SCHEMA_ACCEPTANCE.json']);a['schema_sha256']=h(b['SCHEMA_ACCEPTANCE.json']);b['ROOT_ACCEPTANCE.json']=enc(a);return b
def reject(fn):
 try:fn()
 except(ValueError,KeyError):return
 raise AssertionError('mutant passed')
def main():
 inv=json.loads((D/'INVENTORY.json').read_text());blobs={};n=0
 for rel,m in inv.items():
  raw=(D/rel).read_bytes();need(h(raw)==m['local_sha256']);raw=gzip.decompress(raw)if m['gzip']else raw;need(h(raw)==m['original_sha256']);blobs[rel.removesuffix('.gz')]=raw
 for tag in ['zero','dual']:
  b={p.split('/')[-1]:v for p,v in blobs.items()if p.startswith('evidence/'+tag+'/')};validate(tag,b);n+=1
  a=json.loads(b['ROOT_ACCEPTANCE.json'])
  for name,digest in a['output_hashes'].items():need(h(b[name])==digest)
  for fn in [lambda r:r.update(choices=True),lambda r:r['rows'][0].update(alpha_interval=['1','2']),lambda r:r.update(seconds=False)]:reject(lambda:validate(tag,mutate(b,fn)));n+=1
  if tag=='zero':reject(lambda:validate(tag,mutate(b,lambda r:r['rows'][0].update(true_alpha_excluded=True))));n+=1
  else:reject(lambda:validate(tag,mutate(b,lambda r:r['rows'][0]['candidates'][2].update(**{'lambda':'2'}))));n+=1
 # Independent literal graph identity and sharp branch boundary controls.
 from itertools import combinations
 labels=list(combinations(range(6),2));T=[[int(not(set(a)&set(b)))for b in labels]for a in labels]
 for i,a in enumerate(labels):
  for j,b in enumerate(labels):need(sum(T[i][k]*T[k][j]for k in range(15))==(6 if i==j else 1 if not set(a)&set(b)else 3));n+=1
 for E in [F(1),F(3,2)]:
  need(-3*E*E-3*E*(2*E)==-6*E*E-F(3,4)*(2*E)**2);need(-6*E*E-F(3,4)*(4*E)**2==6*E*E-6*E*(4*E));n+=2
 # Uniform scaling has lambda*s*t, not lambda squared*s*t.
 l,s,t=F(3,2),F(2,3),F(1,4);need(l*s*t==F(1,4));reject(lambda:need(l*l*s*t==F(1,4)));n+=2
 return {'status':'PASS_COMPACT_SUPPORT_ONLY','checks':n,'native_replay':False,'Wick_replay':False,'integration':'UNRUN'}
if __name__=='__main__':print(json.dumps(main(),indent=2))
