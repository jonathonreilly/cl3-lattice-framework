import itertools
import numpy as np
class OrderMenu:
 def __init__(self,L):
  if type(L)is not int or L<2 or L%2:raise ValueError('even L>=2')
  self.L=L;self.N=L**3;self.rs=list(itertools.product(range(L),repeat=3));self.corners=list(itertools.product(range(2),repeat=3));self.planes=list(itertools.combinations(range(3),2));self.links=[(r,a) for r in self.rs for a in range(3)];self.index={x:i for i,x in enumerate(self.links)}
  self.phase=np.array([[(-1)**sum(bi*ri for bi,ri in zip(b,r)) for r in self.rs] for b in self.corners],dtype=float)
  self.epsilon=np.array([(-1)**sum(r) for r in self.rs]);faces=[]
  for a,b in self.planes:
   for r in self.rs:
    ra=list(r);rb=list(r);ra[a]=(ra[a]+1)%L;rb[b]=(rb[b]+1)%L
    faces.append([self.index[r,a],self.index[tuple(ra),b],self.index[tuple(rb),a],self.index[r,b]])
  self.faces=np.array(faces,dtype=int)
 def measure(self,x):
  x=np.asarray(x)
  if x.shape!=(3*self.N,) or x.dtype.kind not in 'iu' or np.any((x!=0)&(x!=1)):raise ValueError('binary integer links')
  electric=self.epsilon[:,None]*(x.reshape(self.N,3)-.5);m=self.phase@electric
  z=x[self.faces];f=((z[:,0]==z[:,2])&(z[:,1]==z[:,3])&(z[:,0]!=z[:,1])).reshape(3,self.N).T;fp=self.phase@f
  anisotropy=float(np.sum((fp[0]-np.mean(fp[0]))**2))
  return dict(electric=m,flippability=fp,electric_square=m*m,flippability_square=fp*fp,electric_fourth=m**4,flippability_fourth=fp**4,plane_anisotropy=anisotropy)
 def vector(self,x):
  z=self.measure(x)
  return np.concatenate([z[k].ravel() for k in ('electric','flippability','electric_square','flippability_square','electric_fourth','flippability_fourth')]+[np.array([z['plane_anisotropy']])])
