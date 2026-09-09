from pathlib import Path
import shutil,json
B=Path(__file__).parent;S=B.parent/'native-l6-prefix-gap-probe'
shutil.copy2(S/'CENSUS.json',B/'CENSUS.json')
s=(S/'gap_pilot.py').read_text();start=s.index('for row in census');end=s.index("(P/'PILOT_RESULT")
setup=s[:start].replace('signal.alarm(180);','').replace(";out=[]",'')
body=s[start:end];body=body[body.index('\n')+1:];body=body.replace(" mask=int(next(r for r in row['prefixes'] if r['k']==1)['mask']);D=np.zeros_like(B)"," D=np.zeros_like(B)")
body=body.replace(" out.append(dict(bridge=row['bridge'],mask=str(mask),gap_lower=str(gap),positive=gap>0,display=float(gap)))"," return dict(mask=str(mask),gap_lower=str(gap),positive=gap>0,display=float(gap))")
# Expose exact factorization/resolvent controls without affecting certificate.
body=body.replace(' U=[[F(int(x))'," if controls:\n  literal=(B+D)@(B+D).T-A\n  exact=U@np.array(C,dtype=object)@U.T\n  if any(F(int(literal[i,j]))!=exact[i,j] for i in range(108) for j in range(108)):raise ValueError('exact Gram factorization')\n U=[[F(int(x))")
body=body.replace(';corr=mm(mm(inv(M),C),H)',";Mi=inv(M)\n if controls and mm(M,Mi)!=[[F(i==j) for j in range(6)] for i in range(6)]:raise ValueError('inverse residual')\n corr=mm(mm(Mi,C),H)")
(B/'core.py').write_text(setup+'\ndef certify(mask,controls=False):\n'+body)
c=json.loads((B/'CENSUS.json').read_text());masks=sorted({int(x['mask']) for r in c['rows'] for x in r['prefixes']});stars={sum(1<<e for e,ab in enumerate(c['edges']) if v in ab):v for v in range(216)}
(B/'PLAN.json').write_text(json.dumps(dict(prior_seconds=.2398606250062585,shards=[dict(shard=i,masks=[str(m) for m in masks[i*96:(i+1)*96]]) for i in range(16)],singletons={str(m):stars[m] for m in masks if m in stars},proper_keys=sum(len(r['prefixes']) for r in c['rows']),distinct=len(masks)),indent=2)+'\n')
