"""Lazy paired pivot on true chiral half-column Gram intervals. No native driver."""
from fractions import Fraction as F
import interval as iv

def inflate(x,radius):
 r=iv.rational(radius)[1];return(x[0]-r,x[1]+r)
def physical_rows(fetch,labels,etaA,etaB,alpha_max):
 """fetch(poleSignIndex,poleSignIndex,source,source): balanced midpoint G/J.
 labels are (plus index,minus index,source,eta), chi(center)=+1,chi(neighbor)=-1.
 Midpoint inputs must independently meet the frozen native geometry gates.
 """
 if not 0<=etaA<=F(1,10**30) or not 0<=etaB<=F(1,10**19) or not 0<alpha_max<=12:raise ValueError('physical entry bounds')
 eG=alpha_max*2**24*etaA;eJ=alpha_max*10136*etaB
 def row(i,j):
  ip,im,a,eta=labels[i];jp,jm,b,theta=labels[j];ca=1 if a==0 else -1;cb=1 if b==0 else -1
  g=z=iv.ZERO
  for x,cx in ((ip,F(1,2)),(im,F(-eta*ca,2))):
   for y,cy in ((jp,F(1,2)),(jm,F(-theta*cb,2))):
    gg,jj=fetch(x,y,a,b);g=iv.add(g,iv.scale(inflate(gg,eG),cx*cy));z=iv.add(z,iv.scale(inflate(jj,eJ),cx*cy))
  # Exact native chirality identities survive the invariant projection.
  return iv.ZERO if eta!=theta else g,iv.ZERO if eta==theta else z
 return row

def compress(fetch,chirality,write,maxpairs=198,epsilon=F(1,1000)):
 n=len(chirality)
 if not n or any(x not in(-1,1) for x in chirality) or not 0<=maxpairs<=198 or epsilon!=F(1,1000):raise ValueError('fixed contract')
 # Half-combination columns have total residual half that of original Y.
 threshold=epsilon*epsilon/F(2116);history=[];selected=set();diag=[fetch(i,i)[0] for i in range(n)]
 def emit(status):
  if any(d[1]<0 for d in diag):raise ValueError('negative upper PSD residual')
  upper=sum(max(0,d[1]) for d in diag)
  write({'status':status,'pairs':len(history),'half_trace_upper':str(F(upper,iv.S)),'original_residual_upper':str(F(2*upper,iv.S)),'threshold_half':str(threshold)})
  return F(upper,iv.S)<=threshold
 for step in range(maxpairs+1):
  if emit('CHECKPOINT'):return {'status':'CERTIFIED_COMPRESSION','pairs':len(history),'history':history}
  if step==maxpairs:return {'status':'PAIR_CAP','pairs':len(history),'history':history}
  candidates=[i for i in range(n) if i not in selected and diag[i][0]>0]
  if not candidates:return {'status':'PRECISION_STALL','pairs':len(history),'history':history}
  i=min(candidates,key=lambda i:(-diag[i][0],i));r=diag[i];g=[];z=[]
  for j in range(n):
   gij,jij=fetch(i,j)
   for h in history:
    oldg,oldj,oldr=h['g'],h['j'],h['r']
    gij=iv.sub(gij,iv.div(iv.add(iv.mul(oldg[i],oldg[j]),iv.mul(oldj[i],oldj[j])),oldr))
    jij=iv.sub(jij,iv.div(iv.sub(iv.mul(oldg[i],oldj[j]),iv.mul(oldj[i],oldg[j])),oldr))
   if chirality[i]!=chirality[j]:gij=iv.ZERO
   if chirality[i]==chirality[j]:jij=iv.ZERO
   if j in selected:gij=jij=iv.ZERO
   if j==i:gij=r;jij=iv.ZERO
   g.append(gij);z.append(jij)
  h={'index':i,'chirality':chirality[i],'r':r,'g':g,'j':z};write({'status':'PIVOT_BEFORE_UPDATE',**h});history.append(h);selected.add(i)
  for j in range(n):
   diag[j]=iv.ZERO if j in selected else iv.sub(diag[j],iv.div(iv.add(iv.mul(g[j],g[j]),iv.mul(z[j],z[j])),r))
