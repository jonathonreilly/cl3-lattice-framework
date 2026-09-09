from pathlib import Path
import json
p=Path('/private/tmp/toe-24h-probes-20260908/native-generalized-action-saved-design');d={};exec(compile((p/'stages.py').read_bytes(),str(p/'stages.py'),'exec'),d)
intervals=[(a,b)for a in range(-3,4)for b in range(a,4)];n=0;S=d['S'];ar=d['Arithmetic']()
for a in intervals:
 for b in intervals:
  # Offset/non-grid endpoints force negative-floor and positive-ceil branches.
  x=tuple(v*S+7 for v in a);y=tuple(v*S-5 for v in b);z=[v*w for v in x for w in y];lo=min(z)//S;hi=-((-max(z))//S)
  assert ar.mul(x,y)==(lo,hi);n+=1
print(json.dumps({'independent_four_corner_comparisons':n,'native_calls':0}))
