from pathlib import Path
from fractions import Fraction as F
import types,sys,json,hashlib
P=Path('/private/tmp/toe-24h-probes-20260908/native-common-five-orbit-kernel-cache')
for name in ('interval','core','cache'):
 m=types.ModuleType(name);sys.modules[name]=m;exec(compile((P/(name+'.py')).read_bytes(),str(P/(name+'.py')),'exec'),m.__dict__)
c=sys.modules['cache'];iv=sys.modules['interval'];core=sys.modules['core']
poles=[F(1,2),F(3,2)];vals=[(F(2,7),F(-3,11),F(5,13),F(-7,17)),(F(3,8),F(-2,13),F(7,19),F(-3,23))];roots=[F(2),F(3)];rows=[];r=c.stream(poles,vals,[x*x for x in roots],rows.append);tab={(x['type'],x['i'],e[0]):((e[1],e[2]),(e[3],e[4])) for x in rows for e in x['entries']};labels=[(n,s,sg) for n,s in enumerate(poles) for sg in(-1,1)];count=0
# Independently combine the full reduced source matrices, keeping each pole's distinct data.
def matrices(n,sg,orbit):
 s=poles[n];A,Ap,B,Bp=vals[n];o,v,k=orbit;D=(1-s*s*A)/6;Dp=-(2*s*A+s*s*Ap)/6
 g=[A,D if o else A,D if v else A];gp=[Ap,Dp if o else Ap,Dp if v else Ap]
 C=[[0]*3 for _ in range(3)];Cp=[[0]*3 for _ in range(3)];L=[[0]*3 for _ in range(3)];Lp=[[0]*3 for _ in range(3)]
 for a in range(3):
  z=1 if a==0 else 2;C[a][a]=z*sg*s*g[a];Cp[a][a]=z*sg*(g[a]+s*gp[a]);op=(o if a==1 else v)
  L[a][a]=-B if a==0 else (s*s*B/3 if op else -2*B);Lp[a][a]=-Bp if a==0 else ((2*s*B+s*s*Bp)/3 if op else -2*Bp)
 for a in (1,2):
  C[0][a]=-2*D;C[a][0]=2*D;Cp[0][a]=-2*Dp;Cp[a][0]=2*Dp;L[0][a]=-sg*s*B/3;L[a][0]=sg*s*B/3;Lp[0][a]=-sg*(B+s*Bp)/3;Lp[a][0]=sg*(B+s*Bp)/3
 C[1][2]=C[2][1]=k*sg*s*(D-A);Cp[1][2]=Cp[2][1]=k*sg*(D-A+s*(Dp-Ap));L[1][2]=L[2][1]=k*B*(1+s*s/6);Lp[1][2]=Lp[2][1]=k*(Bp*(1+s*s/6)+s*B/3)
 return C,Cp,L,Lp
for orbit in c.ORBITS:
 for i,(n,s,sg) in enumerate(labels):
  for j,(nn,t,tau) in enumerate(labels):
   left=matrices(n,-sg,orbit);right=matrices(nn,tau,orbit);den=sg*s+tau*t
   for a in range(3):
    for b in range(3):
     exp=[(right[0][a][b]-left[0][a][b])/den if den else tau*right[1][a][b],-(right[2][a][b]-left[2][a][b])/den if den else -tau*right[3][a][b]]
     got=c.reconstruct(lambda *k:tab[k],i,j,a,b,orbit)
     for value,(lo,hi) in zip(exp,got):
      value*=roots[n]*roots[nn]
      if not F(lo,iv.S)<=value<=F(hi,iv.S):raise ValueError((orbit,i,j,a,b,value,(lo,hi)))
      count+=1
if r['entries']!=56 or len(rows)!=20:raise ValueError('stream census')
print(json.dumps({'status':'PASS','containments':count,'stored_pairs':56,'stream_rows':20,'distinct_pole_data':True,'nonunit_balance':True,'native_calls':0}))
