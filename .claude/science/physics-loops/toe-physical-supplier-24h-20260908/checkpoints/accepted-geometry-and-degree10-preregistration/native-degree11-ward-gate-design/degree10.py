from fractions import Fraction as F
from itertools import combinations
import interval as I
P=I.point
def ra(a,b):return I.check(a+b)
def rn(a):return I.check(-a)
def rm(a,b):return I.check(a*b)
def rd(a,b):return I.check(a/b)

def plus(*xs):
 z=P(0)
 for x in xs:z=I.add(z,x)
 return z
def quad(a,b,c,u,v):return plus(I.scale(a,rm(u,u)),I.scale(b,rm(rm(2,u),v)),I.scale(c,rm(v,v)))
def solve(a,b,c,x,y):
 det=I.sub(I.mul(a,c),I.square(b))
 if a[0]<=0 or det[0]<=0:raise ValueError('uncertified positive moment solve')
 aa,bb,cc,xx,yy=map(I.mid,[a,b,c,x,y]);dd=ra(rm(aa,cc),rn(rm(bb,bb)))
 return(rd(ra(rm(cc,xx),rn(rm(bb,yy))),dd),rd(ra(rm(aa,yy),rn(rm(bb,xx))),dd),det)
def moments(c,nu,kind):
 if kind=='P':return(I.scale(c,10),plus(P(20),I.scale(I.square(c),36),I.scale(I.mul(c,nu),F(-2,3))),I.scale(c,16),P(32),plus(I.scale(nu,F(2,3)),I.scale(c,-20)))
 if kind=='O':return(plus(I.scale(c,4),I.scale(nu,F(1,3))),plus(P(22),I.scale(I.mul(c,nu),F(4,3))),plus(I.scale(nu,F(4,3)),I.scale(c,-8)),P(40),I.scale(c,-8))
 raise ValueError('class')
def candidate(c,nu,kind,mode,emit):
 m3,m4,j1,j2,cross=moments(c,nu,kind)
 emit('moments',dict(kind=kind,m3=m3,m4=m4,j1=j1,j2=j2,cross=cross))
 if mode=='residual':u,v,det=solve(P(2),m3,m4,c,P(2))
 elif mode=='variational':u,v,det=solve(c,P(2),m3,P(1),c)
 else:raise ValueError('fixed choice')
 emit('polynomial',dict(kind=kind,p0=u,p1=v,det=det))
 b=rm(4,v);s0=quad(P(8),I.scale(c,2),P(1),u,b);s1=quad(j1,P(0),I.scale(c,2),u,b);s2=quad(j2,cross,P(4),u,b)
 emit('source_moments',dict(kind=kind,s0=s0,s1=s1,s2=s2))
 if s2[0]<=0:raise ValueError('source denominator positivity')
 q=rd(I.mid(s1),I.mid(s2))
 r=plus(P(ra(ra(1,rn(rm(4,v))),rm(2,rm(u,u)))),I.scale(c,rm(-2,u)),I.scale(m3,rm(rm(2,u),v)),I.scale(m4,rm(v,v)))
 t=plus(s0,I.scale(s1,rm(-2,q)),I.scale(s2,rm(q,q)))
 emit('residual_raw',dict(kind=kind,q=q,r2=r,t2=t))
 r=I.nonnegative(r);t=I.nonnegative(t)
 return dict(p0=u,p1=v,q=q,r2=r,t2=t)
def word(C,A,c):
 u,v=C['p0'],C['p1'];a,b,q=A['p0'],A['p1'],A['q']
 return plus(P(ra(rm(u,a),rm(rm(rm(4,q),u),b))),I.scale(c,ra(ra(rm(u,b),rm(v,a)),rm(q,ra(rm(rm(2,u),a),rm(rm(4,v),b))))))
def run_choice(c,nu,mode,emit):
 rows={kind:candidate(c,nu,kind,mode,emit)for kind in ['P','O']}
 labels=list(combinations(range(6),2));kind=lambda A:'O'if A[0]//2==A[1]//2 else'P'
 nominal=P(0);orbits={};count=0
 # Exact five invariants: O/O, O/P, P/O, P/P union with1 or0 opposite pairs inside union.
 for C in labels:
  for A in labels:
   if set(C)&set(A):continue
   kc,ka=kind(C),kind(A)
   if kc=='P'and ka=='P':
    union=set(C)|set(A);opp=sum({2*k,2*k+1}<=union for k in range(3));tag='PP'+str(opp)
   else:tag=kc+ka
   value=word(rows[kc],rows[ka],c);nominal=I.add(nominal,value);count+=1
   old=orbits.get(tag,{'count':0,'sum':P(0)});old['count']+=1;old['sum']=I.add(old['sum'],value);orbits[tag]=old
   emit('ordered_word',dict(index=count,C=list(C),A=list(A),orbit=tag,value=value,cumulative=nominal))
 if sorted(x['count']for x in orbits.values())!=[6,12,12,12,48]or count!=90:raise ValueError('literal orbit census')
 e2=I.scale(plus(I.scale(rows['P']['r2'],12),I.scale(rows['O']['r2'],3)),16)
 E=I.root(e2);f2=P(0);sqrt2=I.root(P(2))
 for k,n in [('P',12),('O',3)]:
  e=I.scale(I.root(rows[k]['r2']),4);f=I.scale(plus(I.mul(I.scale(sqrt2,2),e),I.root(rows[k]['t2'])),4);f2=I.add(f2,I.scale(I.square(f),n))
 FF=I.root(f2);X=I.scale(I.root(P(15)),4);V=I.scale(I.root(P(30)),32)
 error=I.scale(plus(I.mul(E,plus(I.scale(X,2),E)),I.mul(E,V),I.mul(plus(X,E),FF)),6)
 emit('gate_inputs',dict(rows=rows,orbits=orbits,nominal=nominal,E=E,F=FF,error=error))
 status='POSITIVE_CERTIFICATE'if nominal[0]>error[1]else('NEGATIVE_CERTIFICATE'if nominal[1]<-error[1]else'INDETERMINATE_SIGN')
 return dict(mode=mode,status=status,nominal=nominal,error=error,alpha_interval=I.scale((ra(nominal[0],rn(error[1])),ra(nominal[1],error[1])),F(1,8)),orbits=orbits,ordered_words=count)
