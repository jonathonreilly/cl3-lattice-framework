from fractions import Fraction as F
from itertools import combinations
import interval as I
import degree10 as D
import wick
P=I.point
ra,rm,rn,rd=D.ra,D.rm,D.rn,D.rd

def candidate(c,nu,omega5,kind,mode,emit):
 m3,m4,_,_,_=D.moments(c,nu,kind);emit('vacuum_moments',{'kind':kind,'m3':m3,'m4':m4})
 if mode=='residual':u,v,det=D.solve(P(2),m3,m4,c,P(2))
 elif mode=='variational':u,v,det=D.solve(c,P(2),m3,P(1),c)
 else:raise ValueError('fixed choice')
 emit('first_polynomial',{'kind':kind,'p0':u,'p1':v,'det':det})
 G=wick.table(c,nu,omega5,kind);source=wick.sources(u,rm(4,v));emit('wick_inputs',{'kind':kind,'table':G,'sources':source})
 sj,calls=wick.source_moments(G,source,lambda stage,x:emit(stage,dict(kind=kind,**x)))
 q0,q1,qdet=D.solve(sj[2],sj[3],sj[4],sj[1],sj[2]);emit('second_polynomial',{'kind':kind,'q0':q0,'q1':q1,'det':qdet})
 r=D.plus(P(ra(ra(1,rn(rm(4,v))),rm(2,rm(u,u)))),I.scale(c,rm(-2,u)),I.scale(m3,rm(rm(2,u),v)),I.scale(m4,rm(v,v)))
 t=D.plus(sj[0],I.scale(sj[1],rm(-2,q0)),I.scale(sj[2],ra(rm(-2,q1),rm(q0,q0))),I.scale(sj[3],rm(rm(2,q0),q1)),I.scale(sj[4],rm(q1,q1)))
 emit('residual_raw',{'kind':kind,'r2':r,'t2':t})
 return {'p0':u,'p1':v,'q0':q0,'q1':q1,'r2':I.nonnegative(r),'t2':I.nonnegative(t),'wick_cache_misses':calls}

def word(C,A,c,nu,ell):
 old=D.word(C,dict(p0=A['p0'],p1=A['p1'],q=A['q0']),c)
 u,v=C['p0'],C['p1'];a,b,q=A['p0'],A['p1'],A['q1'];V=rm(4,b)
 cross=I.scale(D.plus(I.scale(nu,F(1,6)),I.scale(c,-3)),ell)
 extra=D.plus(I.scale(c,rm(rm(2,V),u)),I.scale(D.plus(I.scale(c,rm(-4,a)),I.scale(cross,rm(2,a)),P(rm(2,V))),v))
 return I.add(old,I.scale(extra,q))

def run_choice(c,nu,omega5,mode,emit):
 rows={kind:candidate(c,nu,omega5,kind,mode,emit)for kind in ['P','O']}
 labels=list(combinations(range(6),2));kind=lambda A:'O'if A[0]//2==A[1]//2 else'P';nominal=P(0);orbits={};count=0
 for C in labels:
  for A in labels:
   if set(C)&set(A):continue
   kc,ka=kind(C),kind(A);ell=sum((2*k in C and 2*k+1 in A)or(2*k+1 in C and 2*k in A)for k in range(3));tag='PP'+str(ell)if kc==ka=='P'else kc+ka
   value=word(rows[kc],rows[ka],c,nu,ell);nominal=I.add(nominal,value);count+=1
   old=orbits.get(tag,{'count':0,'sum':P(0)});old['count']+=1;old['sum']=I.add(old['sum'],value);orbits[tag]=old
   emit('ordered_word',{'index':count,'C':list(C),'A':list(A),'ell':ell,'orbit':tag,'value':value,'cumulative':nominal})
 if count!=90 or sorted(x['count']for x in orbits.values())!=[6,12,12,12,48]:raise ValueError('orbit census')
 E=I.root(I.scale(D.plus(I.scale(rows['P']['r2'],12),I.scale(rows['O']['r2'],3)),16));F2=P(0)
 for k,n in [('P',12),('O',3)]:
  e=I.scale(I.root(rows[k]['r2']),4);f=I.scale(D.plus(I.mul(I.scale(I.root(P(2)),2),e),I.root(rows[k]['t2'])),4);F2=I.add(F2,I.scale(I.square(f),n))
 FF=I.root(F2);X=I.scale(I.root(P(15)),4);V=I.scale(I.root(P(30)),32)
 error=I.scale(D.plus(I.mul(E,D.plus(I.scale(X,2),E)),I.mul(E,V),I.mul(D.plus(X,E),FF)),6)
 emit('gate_inputs',{'rows':rows,'orbits':orbits,'nominal':nominal,'E':E,'F':FF,'error':error})
 status='POSITIVE_CERTIFICATE'if nominal[0]>error[1]else('NEGATIVE_CERTIFICATE'if nominal[1]<-error[1]else'INDETERMINATE_SIGN')
 return {'mode':mode,'status':status,'nominal':nominal,'error':error,'alpha_interval':I.scale((ra(nominal[0],rn(error[1])),ra(nominal[1],error[1])),F(1,8)),'ordered_words':count,'orbits':orbits}
