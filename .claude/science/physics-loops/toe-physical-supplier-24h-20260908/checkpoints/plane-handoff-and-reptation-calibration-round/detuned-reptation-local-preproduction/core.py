import numpy as np
from itertools import product,combinations

def geometry(L,harmonics=None):
 if type(L) is not int or L not in (2,4):raise ValueError("reviewed L2/L4 domain")
 if harmonics is None:harmonics=(1,) if L==2 else (1,2)
 if any(h<1 or h>L//2 for h in harmonics):raise ValueError("harmonics")
 rs=list(product(range(L),repeat=3));links=[(r,a) for r in rs for a in range(3)];index={z:i for i,z in enumerate(links)};faces=[]
 for a,b in combinations(range(3),2):
  for r in rs:
   ra=list(r);rb=list(r);ra[a]=(ra[a]+1)%L;rb[b]=(rb[b]+1)%L
   faces.append([index[r,a],index[tuple(ra),b],index[tuple(rb),a],index[r,b]])
 coeff=np.array([[(-1)**sum(r)*np.exp(2j*np.pi*h*r[a]/L)/np.sqrt(L**3) if pol==b else 0 for r,b in links] for h in harmonics for a in range(3) for pol in range(3) if pol!=a]);seed=np.array([r[a]%2 for r,a in links],np.uint8)
 return np.array(faces),coeff,seed

def count(state,faces):
 bits=state[faces];return int(np.sum((bits[:,0]==bits[:,2])&(bits[:,1]==bits[:,3])&(bits[:,0]!=bits[:,1])))
def legal(state,face):
 z=state[face];return bool(z[0]==z[2] and z[1]==z[3] and z[0]!=z[1])
def flip(state,label,faces):
 out=state.copy()
 if label>=0:out[faces[label]]^=1
 return out
class Path:
 def __init__(self,L,n,harmonics=None):
  if n<=0 or n%2:raise ValueError('positive even n')
  self.faces,self.coeff,seed=geometry(L,harmonics);self.n=n;self.head=0;self.labels=np.full(n,-1,int);self.direction=1;self.states=[seed.copy() for _ in range(3)];self.nf=[count(x,self.faces) for x in self.states];self.O=[self.coeff@(x.astype(float)-.5) for x in self.states]
 def change(self,k,label):
  if label>=0:
   x=self.states[k];f=self.faces[label];self.O[k]+=self.coeff[:,f]@(1.-2*x[f]);x[f]^=1;self.nf[k]=count(x,self.faces)
 def step(self,rng):
  plus=self.direction==1;old=2 if plus else 0;near=0 if plus else 2;edge=int(self.labels[self.head if plus else (self.head+self.n-1)%self.n]);adj=flip(self.states[near],edge,self.faces);adj_nf=count(adj,self.faces)
  u=rng.random()*(len(self.faces)+.05*self.nf[old]);f=int(u) if u<len(self.faces) else -1;label=f if f>=0 and legal(self.states[old],self.faces[f]) else -1
  accept=rng.random()<min(1,(1+.05*self.nf[old]/len(self.faces))/(1+.05*adj_nf/len(self.faces)))
  if accept:
   if plus:
    midlabel=int(self.labels[(self.head+self.n//2)%self.n]);self.change(0,edge);self.change(1,midlabel);self.change(2,label);self.labels[self.head]=label;self.head=(self.head+1)%self.n
   else:
    midlabel=int(self.labels[(self.head+self.n//2-1)%self.n]);self.change(2,edge);self.change(1,midlabel);self.change(0,label);self.head=(self.head-1)%self.n;self.labels[self.head]=label
  else:self.direction=-self.direction
  return label,accept
