"""Fixed small formal-coefficient controls; no native scalar inputs."""
from fractions import Fraction as F
import cache,interval as iv
import json
poles=[F(1,2),F(2)];values=[(F(2,7),F(-3,11),F(5,13),F(-7,17))]*2
labels=[(n,s,sg) for n,s in enumerate(poles) for sg in(-1,1)]
rows=[];receipt=cache.stream(poles,values,[F(1),F(1)],rows.append)
table={(row['type'],row['i'],e[0]):((e[1],e[2]),(e[3],e[4])) for row in rows for e in row['entries']}
def fetch(*k):return table[k]
def exact(s,sg,oa,oc,k):
 A,Ap,B,Bp=values[0];D=(1-s*s*A)/6;Dp=-(2*s*A+s*s*Ap)/6
 geo=lambda o:D if o else A;gp=lambda o:Dp if o else Ap
 l=lambda o:s*s*B/3 if o else -2*B;lp=lambda o:(2*s*B+s*s*Bp)/3 if o else -2*Bp
 return ([[sg*s*A,-2*D,-2*D],[2*D,2*sg*s*geo(oa),k*sg*s*(D-A)],[2*D,k*sg*s*(D-A),2*sg*s*geo(oc)]],[[sg*(A+s*Ap),-2*Dp,-2*Dp],[2*Dp,2*sg*(geo(oa)+s*gp(oa)),k*sg*(D-A+s*(Dp-Ap))],[2*Dp,k*sg*(D-A+s*(Dp-Ap)),2*sg*(geo(oc)+s*gp(oc))]],[[-B,-sg*s*B/3,-sg*s*B/3],[sg*s*B/3,l(oa),k*B*(1+s*s/6)],[sg*s*B/3,k*B*(1+s*s/6),l(oc)]],[[-Bp,-sg*(B+s*Bp)/3,-sg*(B+s*Bp)/3],[sg*(B+s*Bp)/3,lp(oa),k*(Bp*(1+s*s/6)+s*B/3)],[sg*(B+s*Bp)/3,k*(Bp*(1+s*s/6)+s*B/3),lp(oc)]])
n=0;wrong=0
for orbit in cache.ORBITS:
 for i,(_,s,sg) in enumerate(labels):
  for j,(_,t,tau) in enumerate(labels):
   left=exact(s,-sg,*orbit);right=exact(t,tau,*orbit);den=sg*s+tau*t
   for a in range(3):
    for b in range(3):
     g=(right[0][a][b]-left[0][a][b])/den if den else tau*right[1][a][b]
     z=-(right[2][a][b]-left[2][a][b])/den if den else -tau*right[3][a][b]
     got=cache.reconstruct(fetch,i,j,a,b,orbit)
     for interval,value in zip(got,(g,z)):
      if not F(interval[0],iv.S)<=value<=F(interval[1],iv.S):raise ValueError((orbit,i,j,a,b,value,interval))
      n+=1
     if a>0 and b==0 and z and not F(got[1][0],iv.S)<=-z<=F(got[1][1],iv.S):wrong+=1
if not wrong:raise ValueError('transpose sign adverse undetected')
if receipt['entries']!=4*10+16:raise ValueError('cache count')
print(json.dumps({'status':'PASS_SYNTHETIC','containment_predicates':n,'wrong_transpose_sign_discriminations':wrong,'stored_entries':receipt['entries'],'physical_calls':0},indent=2))
