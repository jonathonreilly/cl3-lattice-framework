from fractions import Fraction as F
from itertools import combinations
import interval as I
import degree10 as D
import wick,algebra as A
P=I.point
ra,rm,rn,rd=D.ra,D.rm,D.rn,D.rd

def candidate(c,nu,omega5,kind,mode,emit):
 for box in [c,nu,omega5]:
  if any(max(abs(x.numerator).bit_length(),x.denominator.bit_length())>512 for x in box):raise ValueError('scalar component512 cap')
 G=wick.table(c,nu,omega5,kind);ops,J,M=A.local_operators();mean,inner,counts=A.evaluator(G);mom=[]
 emit('vacuum_inputs',{'kind':kind,'table':G,'operators':ops})
 for n,(i,j)in enumerate([(0,0),(0,1),(1,1),(1,2),(2,2),(2,3),(3,3)]):
  z=inner(ops[i],ops[j]);emit('vacuum_moment_raw',{'kind':kind,'index':n,'real':z[0],'imaginary':z[1]});mom.append(A.real_moment(z))
 shift=2 if mode=='residual'else 1 if mode=='variational'else None
 if shift is None:raise ValueError('fixed mode')
 H=[[mom[i+j+shift]for j in range(3)]for i in range(3)];rhs=[mom[i+shift-1]for i in range(3)];p,piv=A.choose3(H,rhs)
 emit('first_polynomial',{'kind':kind,'coefficients':p,'certified_pivots':piv})
 O=A.opadd(*(A.opscale(ops[i],p[i])for i in range(3)));DP=A.opadd(*(A.opscale(ops[i+1],p[i])for i in range(3)));b=A.opmul(J,O);Db=A.opadd(A.opmul(J,DP),A.opmul(M,O));sj=[]
 emit('source_inputs',{'kind':kind,'b':b,'Db':Db})
 for n,(x,y)in enumerate([(b,b),(b,Db),(Db,Db)]):
  z=inner(x,y);emit('source_moment_raw',{'kind':kind,'index':n,'real':z[0],'imaginary':z[1]});sj.append(A.real_moment(z))
 if sj[2][0]<=0:raise ValueError('source positive denominator')
 q=A.dyadic(rd(I.mid(sj[1]),I.mid(sj[2])))
 r=mom[0]
 for i in range(3):r=I.add(r,I.scale(mom[i+1],rm(-2,p[i])))
 for i in range(3):
  for j in range(3):r=I.add(r,I.scale(mom[i+j+2],rm(p[i],p[j])))
 t=D.plus(sj[0],I.scale(sj[1],rm(-2,q)),I.scale(sj[2],rm(q,q)));emit('residual_raw',{'kind':kind,'q':q,'r2':r,'t2':t,'counts':counts()})
 return {'p':p,'q':q,'r2':I.nonnegative(r),'t2':I.nonnegative(t),'counts':counts()}

def cross_table(c,nu,kA,kC,ell):
 L=lambda k:12 if k=='P'else 14;ed=lambda k:I.scale(c,6)if k=='P'else I.scale(nu,F(1,3));ec=I.scale(D.plus(I.scale(nu,F(1,6)),I.scale(c,-3)),ell)
 white=[[1,-2,-2],[-2,L(kA),ell],[-2,ell,L(kC)]];black=[[2,0,2],[0,2,2],[2,2,6]]
 kap=[[I.neg(c),I.neg(c),I.scale(c,-3)],[ed(kA),ec,I.scale(nu,F(1,3))],[ec,ed(kC),I.scale(nu,F(1,3))]];G=[[wick.ZERO for _ in range(6)]for _ in range(6)]
 for i in range(3):
  for j in range(3):
   G[i][j]=(P(white[i][j]),P(0));G[i+3][j+3]=(P(black[i][j]),P(0));G[i][j+3]=(P(0),kap[i][j]);G[j+3][i]=(P(0),I.neg(kap[i][j]))
 return G

def word(C,Arow,c,nu,kC,kA,ell,emit):
 G=cross_table(c,nu,kA,kC,ell);mean,inner,counts=A.evaluator(G)
 def op(row,dl,vl):
  ops=[A.term(()),A.term((0,dl),1,1),A.opadd(A.term((),2),A.term((5,dl),-1),A.term((0,vl),-1))]
  return A.opadd(*(A.opscale(ops[i],row['p'][i])for i in range(3)))
 OC,OA=op(C,4,2),op(Arow,3,1);JA=A.term((3,),2,1);g=A.term((0,));base=inner(OC,OA);corr=inner(OC,A.opmul(A.opmul(g,JA),OA))
 # Each full ordered word may be complex; physical target is its real part.
 val=I.add(base[0],I.scale(corr[0],Arow['q']));emit('cross_wick_raw',{'classes':[kC,kA],'ell':ell,'table':G,'OC':OC,'OA':OA,'base':base,'correction':corr,'value':val,'counts':counts()})
 return val

def run_choice(c,nu,omega5,mode,emit):
 rows={k:candidate(c,nu,omega5,k,mode,emit)for k in ['P','O']};labels=list(combinations(range(6),2));kind=lambda x:'O'if x[0]//2==x[1]//2 else'P';cache={};orbits={};nominal=P(0);count=0
 for C in labels:
  for AA in labels:
   if set(C)&set(AA):continue
   kc,ka=kind(C),kind(AA);ell=sum((2*k in C and 2*k+1 in AA)or(2*k+1 in C and 2*k in AA)for k in range(3));tag='PP'+str(ell)if kc==ka=='P'else kc+ka
   if tag not in cache:cache[tag]=word(rows[kc],rows[ka],c,nu,kc,ka,ell,emit)
   value=cache[tag];nominal=I.add(nominal,value);count+=1;old=orbits.get(tag,{'count':0,'sum':P(0)});old['count']+=1;old['sum']=I.add(old['sum'],value);orbits[tag]=old
   emit('ordered_word',{'index':count,'C':list(C),'A':list(AA),'ell':ell,'orbit':tag,'value':value,'cumulative':nominal})
 if count!=90 or len(cache)!=5 or sorted(x['count']for x in orbits.values())!=[6,12,12,12,48]:raise ValueError('orbit census')
 E=I.root(I.scale(D.plus(I.scale(rows['P']['r2'],12),I.scale(rows['O']['r2'],3)),16));F2=P(0)
 for k,n in [('P',12),('O',3)]:
  e=I.scale(I.root(rows[k]['r2']),4);f=I.scale(D.plus(I.mul(I.scale(I.root(P(2)),2),e),I.root(rows[k]['t2'])),4);F2=I.add(F2,I.scale(I.square(f),n))
 FF=I.root(F2);X=I.scale(I.root(P(15)),4);V=I.scale(I.root(P(30)),32);err=I.scale(D.plus(I.mul(E,D.plus(I.scale(X,2),E)),I.mul(E,V),I.mul(D.plus(X,E),FF)),6)
 emit('gate_inputs',{'rows':rows,'orbits':orbits,'nominal':nominal,'E':E,'F':FF,'error':err})
 status='POSITIVE_CERTIFICATE'if nominal[0]>err[1]else('NEGATIVE_CERTIFICATE'if nominal[1]<-err[1]else'INDETERMINATE_SIGN')
 return {'mode':mode,'status':status,'nominal':nominal,'error':err,'alpha_interval':I.scale((ra(nominal[0],rn(err[1])),ra(nominal[1],err[1])),F(1,8)),'ordered_words':count,'cross_wick_classes':5,'orbits':orbits}
