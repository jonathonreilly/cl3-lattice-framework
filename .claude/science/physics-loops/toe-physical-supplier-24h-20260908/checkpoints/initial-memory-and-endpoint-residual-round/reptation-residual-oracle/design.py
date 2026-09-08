from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal,localcontext
import json
p=Path(__file__).resolve().parent;r=json.loads((p/'RESULT.json').read_text());out=[]
for row in r['rows']:
 m=list(map(F,row['means']));cov=[[F(row['cross'][i][j])-m[i]*m[j] for j in range(6)] for i in range(6)]
 X,E,XE=m[1],m[2],m[4];gr=[0,-XE/X**2,-1,0,1/X,0];gv=[0,0,-2*E,1,0,0]
 vr=sum(gr[i]*cov[i][j]*gr[j] for i in range(6) for j in range(6));vv=sum(gv[i]*cov[i][j]*gv[j] for i in range(6) for j in range(6))
 if vr<0 or vv<0:raise RuntimeError('negative exact influence variance')
 c=F(row['correction']);v=F(row['VarH'])
 with localcontext() as ctx:
  ctx.prec=24
  dec=lambda x:str(Decimal(x.numerator)/Decimal(x.denominator))
  out.append(dict(V=row['V'],n=row['n'],correction_influence_variance=dec(vr),VarH_influence_variance=dec(vv),independent_samples_25percent_relative_SE_correction=dec(16*vr/c**2) if c else None,independent_samples_25percent_relative_SE_VarH=dec(16*vv/v**2) if v else None))
(p/'DESIGN.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
