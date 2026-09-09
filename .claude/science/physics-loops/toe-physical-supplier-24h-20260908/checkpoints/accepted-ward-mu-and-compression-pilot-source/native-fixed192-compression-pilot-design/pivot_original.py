"""Fixed192 arithmetic candidate. Caller supplies immutable true physical entries."""
from fractions import Fraction as F
import interval as iv
T=531;MAX_PAIRS=198

def square(x):
 lo,hi=x
 if lo>hi:raise ValueError('interval order')
 return (0 if lo<=0<=hi else min(lo*lo,hi*hi)//iv.S,-((-max(lo*lo,hi*hi))//iv.S))
def intersection(x,y):
 z=max(x[0],y[0]),min(x[1],y[1])
 if z[0]>z[1]:raise ValueError('empty proved intersection')
 return z
def divide(x,r):
 if r[0]<=0:raise ValueError('uncertain positive denominator')
 return iv.div(x,r)
def coordinate(x,r):return divide(x,iv.sqrt(r))
def midpoint_radius(x):
 m=(x[0]+x[1])//2;return m,max(m-x[0],x[1]-m)

def labels(augmented=True):
 lab=[('pole',n,s,eta,2) for n in range(66) for s in range(3) for eta in(-1,1)]
 if augmented:lab.extend(('append',0,s,1,1) for s in range(3))
 return tuple(lab)

def validate(lab,native):
 if not isinstance(lab,tuple) or not lab or len(set(lab))!=len(lab):raise ValueError('immutable unique labels')
 for kind,n,s,eta,weight in lab:
  if kind not in('pole','append') or eta not in(-1,1) or weight!=(2 if kind=='pole' else 1):raise ValueError('label/weight')
  if kind=='append' and eta!=1:raise ValueError('append chirality')
 if native and lab not in(labels(False),labels(True)):raise ValueError('canonical396/399 labels')

def run(entry,lab,persist,*,native=True,max_pairs=MAX_PAIRS):
 """entry(i,j) immutable G/J interval pair, symmetric/skew and chiral.
 No native reader/driver exists. persist writes each stage before dependent work.
 """
 validate(lab,native)
 if not 0<=max_pairs<=MAX_PAIRS:raise ValueError('resource cap')
 n=len(lab);aug=any(l[0]=='append' for l in lab);bound=1062 if aug else 1058;threshold=F(1,10**6*bound)
 history=[];selected=set();audit={'intersections':0};current=None
 def box(x,diagonal=False):
  z=intersection(x,(0,T*iv.S) if diagonal else(-T*iv.S,T*iv.S))
  if z!=x:audit['intersections']+=1
  return z
 def original(i,j):
  g,z=entry(i,j)
  if any(not isinstance(t,int) for pair in(g,z) for t in pair):raise ValueError('integer endpoints')
  g=box(g,i==j);z=box(z)
  # Verify that the original enclosure CONTAINS each mathematically known zero.
  if lab[i][3]!=lab[j][3]:g=intersection(g,iv.ZERO)
  if lab[i][3]==lab[j][3] or i==j:z=intersection(z,iv.ZERO)
  return g,z
 def residual(i,j):
  g,z=original(i,j)
  for h in history:
   gi,gj,ji,jj=h['g'][i],h['g'][j],h['j'][i],h['j'][j];r=h['r']
   numer=iv.add(square(gi),square(ji)) if i==j else iv.add(iv.mul(gi,gj),iv.mul(ji,jj))
   g=iv.sub(g,divide(numer,r));z=iv.sub(z,divide(iv.sub(iv.mul(gi,jj),iv.mul(ji,gj)),r))
  g=box(g,i==j);z=box(z)
  if i in selected or j in selected:g=intersection(g,iv.ZERO);z=intersection(z,iv.ZERO)
  if lab[i][3]!=lab[j][3]:g=intersection(g,iv.ZERO)
  if lab[i][3]==lab[j][3]:z=intersection(z,iv.ZERO)
  return g,z
 def coordinates():
  rows=[];weighted_sq=0
  for h in history:
   out=[]
   for vector in(h['g'],[iv.neg(z) for z in h['j']]):
    coords=[]
    for j,x in enumerate(vector):
     enclosure=coordinate(x,h['r']);m,rad=midpoint_radius(enclosure);weighted_sq+=lab[j][4]*rad*rad;coords.append((m,rad))
    out.append(tuple(coords))
   rows.append(tuple(out))
  # d² exact after reconstructing pole halves; append entries have weight1.
  dsq=F(weighted_sq,iv.S**2)
  return tuple(rows),dsq
 try:
  for step in range(max_pairs+1):
   current={'stage':'diagonals','step':step};persist(current)
   diag=[residual(i,i)[0] for i in range(n)];raw=F(sum(lab[i][4]*diag[i][1] for i in range(n)),iv.S)
   coords,dsq=coordinates();res_ok=raw<=threshold;coord_ok=dsq<=F(1,40000**2)
   persist({'stage':'checkpoint','pairs':len(history),'raw_residual_upper':str(raw),'coordinate_radius_squared':str(dsq),'coordinate_intervals':coords,'residual_pass':res_ok,'coordinate_pass':coord_ok,'audit':dict(audit)})
   if res_ok:return {'status':'PASS_BOTH' if coord_ok else 'RESIDUAL_PASS_COORDINATE_FAIL','pairs':len(history),'history':tuple(history),'coordinate_radius_squared':str(dsq)}
   if step==max_pairs:return {'status':'PAIR_CAP','pairs':len(history),'history':tuple(history)}
   candidates=[i for i in range(n) if i not in selected and diag[i][0]>0]
   if not candidates:return {'status':'PRECISION_STALL','pairs':len(history),'history':tuple(history)}
   i=min(candidates,key=lambda j:(-diag[j][0],j));current={'stage':'pivot_row','index':i,'step':step};persist(current)
   row=[residual(i,j) for j in range(n)];r=intersection(diag[i],row[i][0])
   if r[0]<=0:raise ValueError('pivot lost positivity')
   g=tuple(x[0] for x in row);z=tuple(x[1] for x in row);h={'index':i,'chirality':lab[i][3],'r':r,'g':g,'j':z};persist({'stage':'pivot_saved',**h});history.append(h);selected.add(i)
 except BaseException as e:persist({'stage':'FAILED','current':current,'error':repr(e),'pairs':len(history),'audit':dict(audit)});raise
