"""Reduced h=1 dual vector algebra. Imports are inert."""
from fractions import Fraction as F
from itertools import combinations
import json,hashlib
import interval as I
import algebra as A
import wick
LABELS=list(combinations(range(6),2));P=I.point
SCALES=(F(0),F(1,2),F(1),F(3,2),F(2))

def kind(a):return 'O'if a[0]//2==a[1]//2 else'P'
def add(*xs):
 z=P(0)
 for x in xs:z=I.add(z,x)
 return z
def dot(x,y):return I.check(sum((I.check(a*b)for a,b in zip(x,y)),F(0)))
def opp(x,y):return I.check(sum((I.check(x[i]*y[i^1])for i in range(6)),F(0)))
def scale(q,x):return [I.check(q*a)for a in x]
def vector(a=0,b=None,k=None):return(F(a),b or [F(0)]*6,k or [F(0)]*6)

def covariance(x,y,c,nu):
 ax,bx,kx=x;ay,by,ky=y
 real=I.check(ax*ay-ax*sum(ky)-ay*sum(kx)+dot(bx,by)+6*dot(kx,ky)+opp(kx,ky))
 def white_black(a,k,b):return add(I.scale(c,-a*sum(b)/2),I.scale(c,3*dot(k,b)),I.scale(I.sub(I.scale(nu,F(1,6)),I.scale(c,3)),opp(k,b)))
 return P(real),I.sub(white_black(ax,kx,by),white_black(ay,ky,bx))

def prepare(label,rows,c,nu):
 d=[F(int(j in label))for j in range(6)];k=[F(1)]*6;neighbors=[C for C in LABELS if not(set(C)&set(label))]
 U=I.check(sum(rows[kind(C)][0]for C in neighbors));Z=I.check(sum(I.check(rows[kind(C)][2]*rows[kind(C)][1])for C in neighbors))
 W=[I.check(sum(rows[kind(C)][1]for C in neighbors if j in C))for j in range(6)]
 R=[I.check(sum(I.check(rows[kind(C)][2]*rows[kind(C)][0])for C in neighbors if j in C))for j in range(6)]
 alpha=I.check(-2*U-4*Z);beta=[I.check(-2*(x+y))for x,y in zip(W,R)];diff=[x-y for x,y in zip(d,k)]
 # a,d,k,W,beta,Kd,KW,Kbeta,d-k
 bank=[vector(1),vector(b=d),vector(b=k),vector(b=W),vector(b=beta),vector(k=d),vector(k=W),vector(k=beta),vector(b=diff)]
 G=[[covariance(x,y,c,nu)for y in bank]for x in bank]
 t=A.term
 u=A.opadd(t((0,),-U),t((3,),-1,1));w=A.opadd(t((),alpha),t((0,4),1,1))
 Ju=A.opadd(t((0,1),2*U,1),t((1,3),2))
 Hu=A.opadd(t((6,)),t((8,),U,1),t((0,1,3)))
 Hw=A.opadd(t((2,4),-1),t((0,7),-1),t((0,1),alpha,1),t((1,4)))
 HJu=A.opadd(t((2,1),-2*U),t((0,5),-2*U),t((5,3),2,1),t((1,6),2,1),t((),4*U),t((0,3),4,1))
 p0,p1,q=rows[kind(label)]
 r=A.opadd(t((),-1+2*p1),t((0,1),p0,1),t((2,1),-p1),t((0,5),-p1))
 s=A.opadd(t((1,),2*p0,1),t((0,),4*p1+4*q*p0),t((5,),2*q*p0),t((8,),4*q*p1,1))
 ops={'w':w,'Hw':Hw,'Ju':Ju,'HJu':HJu,'u':u,'Hu':Hu,'r':r,'s':s}
 raw=I.encode({'G':G,'operators':ops});key=hashlib.sha256(json.dumps(raw,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 return G,ops,key,raw

def acquire(G,ops,emit):
 _,inner,counts=A.evaluator(G);grams=[];words=0
 for names in [('w','Hw','Ju','HJu'),('u','Hu')]:
  M=[[None]*len(names)for _ in names]
  for i,a in enumerate(names):
   for j in range(i,len(names)):
    b=names[j];emit('before_dual_entry',{'left':a,'right':b});v=inner(ops[a],ops[b]);words+=len(ops[a])*len(ops[b]);emit('dual_entry',{'left':a,'right':b,'value':v,'counts':counts()})
    if i==j:
     if not v[1][0]<=0<=v[1][1]:raise ValueError('nonreal norm')
     value=I.nonnegative(v[0])
    else:value=v[0]
    M[i][j]=M[j][i]=value
  grams.append(M)
 cs=[]
 for a,b in [('r','w'),('r','Ju'),('s','u')]:
  emit('before_dual_entry',{'left':a,'right':b});v=inner(ops[a],ops[b]);words+=len(ops[a])*len(ops[b]);emit('dual_entry',{'left':a,'right':b,'value':v,'counts':counts()});cs.append(v[0])
 if words!=171:raise ValueError('fixed171 word count')
 return {'A':grams[0],'B':grams[1],'correction':cs,'words':words,'counts':counts()}

def proposal(M):
 G=M['A'];B=M['B'];reason=None
 def dyadic(num,den):
  if den<=0:return F(0)
  x=I.check(num/den);x=max(F(0),min(F(4),x));Q=1<<64;return I.check(F((x.numerator*Q)//x.denominator,Q))
 try:
  t=dyadic(I.mid(B[0][1]),I.mid(B[1][1]));g=[[I.mid(x)for x in r]for r in G]
  num=I.check(g[0][1]-t*(g[0][3]+g[1][2])+t*t*g[2][3]);den=I.check(g[1][1]-2*t*g[1][3]+t*t*g[3][3]);s=dyadic(num,den)
 except(ValueError,ZeroDivisionError)as e:t=s=F(0);reason=repr(e)
 return t,s,reason

def quadratic(G,c):
 z=P(0)
 for i,x in enumerate(c):
  z=I.add(z,I.scale(G[i][i],I.check(x*x)))
  for j in range(i+1,len(c)):z=I.add(z,I.scale(G[i][j],I.check(2*x*c[j])))
 return I.nonnegative(z)

def certify(M,t,s,lam=F(1)):
 a=quadratic(M['A'],[F(1),-I.check(lam*s),-I.check(lam*t),I.check(lam*s*t)]);b=quadratic(M['B'],[F(-1),I.check(lam*t)]);cs=M['correction'];corr=add(I.scale(cs[0],s),I.scale(cs[1],-I.check(s*t)),I.scale(cs[2],-t));return a,b,I.scale(corr,lam)

def remainder(E,Fv):
 if min(E,Fv)<0:raise ValueError('negative error')
 if Fv<=2*E:return I.check(-3*E*E-3*E*Fv)
 if Fv<=4*E:return I.check(-6*E*E-F(3,4)*Fv*Fv)
 return I.check(6*E*E-6*E*Fv)

def evaluate(inputs,emit):
 c,nu=I.box(inputs['c']),I.box(inputs['nu']);rows={k:tuple(I.parse(inputs['coefficients'][k][x])for x in ['p0','p1','q'])for k in ['P','O']}
 cache={};classkeys={};sums=[[P(0),P(0),P(0)]for _ in SCALES];channels=[]
 for index,label in enumerate(LABELS):
  emit('before_channel',{'index':index,'label':label});G,ops,key,raw=prepare(label,rows,c,nu);cl=kind(label)
  if cl in classkeys and classkeys[cl]!=key:raise ValueError('literal class-signature disagreement')
  classkeys[cl]=key
  if key not in cache:
   emit('new_dual_covariance',{'index':index,'class':cl,'key':key,**raw});cache[key]=acquire(G,ops,emit);emit('new_dual_grams',{'key':key,'data':cache[key]})
  else:emit('inherited_identical_channel_grams',{'index':index,'key':key})
  if len(cache)>2:raise ValueError('at most two exact signatures')
  M=cache[key];t,s,reason=proposal(M);emit('dyadic_proposal',{'index':index,'t':t,'s':s,'fallback':reason})
  for j,lam in enumerate(SCALES):
   vals=certify(M,t,s,lam)
   for k in range(3):sums[j][k]=I.add(sums[j][k],vals[k])
   emit('certified_channel',{'index':index,'candidate':j,'t':t,'s':s,'lambda':lam,'a2':vals[0],'b2':vals[1],'correction':vals[2]})
  channels.append({'label':label,'key':key,'t':t,'s':s})
 if len(channels)!=15 or set(classkeys)!={'P','O'}:raise ValueError('channel census')
 E=I.parse(inputs['E_upper']);Fv=I.parse(inputs['F_upper']);L=remainder(E,Fv);nom=I.box(inputs['nominal']);old=I.box(inputs['spectral_alpha_interval']);low,high=old;certs=[]
 for lam,(a2,b2,corr) in zip(SCALES,sums):
  a=I.root(a2)[1];b=I.root(b2)[1];linear=I.check(E*a+Fv*b);lo=I.check((nom[0]+corr[0]-linear+L)/8);hi=I.check((nom[1]+corr[1]+linear+6*E*E+6*E*Fv)/8);low=max(low,lo);high=min(high,hi);emit('scale_certificate',{'lambda':lam,'a2':a2,'b2':b2,'correction':corr,'a_upper':a,'b_upper':b,'alpha_interval':(lo,hi)});certs.append({'lambda':lam,'a2':a2,'b2':b2,'correction':corr,'linear_error':linear,'alpha_interval':(lo,hi)})
 if low>high:raise ValueError('contradictory valid intervals')
 return {'status':'POSITIVE_CERTIFICATE'if low>0 else'NEGATIVE_CERTIFICATE'if high<0 else'INDETERMINATE_SIGN','alpha_interval':(low,high),'spectral_alpha_interval':old,'candidates':certs,'channels':channels,'unique_gram_sets':len(cache),'actual_Wick_words':171*len(cache),'logical_Wick_words':2565,'sharp_remainder_lower':L,'physical_trial_changed':False}
