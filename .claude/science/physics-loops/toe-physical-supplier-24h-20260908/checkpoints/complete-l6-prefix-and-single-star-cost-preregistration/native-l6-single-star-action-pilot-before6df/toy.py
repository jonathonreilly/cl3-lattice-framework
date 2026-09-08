import importlib.util,json
from pathlib import Path
P=Path(__file__).parent
text=(P/'kernel.py').read_text()
def load(src):
 ns={};exec(compile(src,'tiny_actual_kernel','exec'),ns);ns.update(MODES=3,TOP=2,SIZE=4,CHUNK=2);return ns

def verify(src):
 k=load(src);np=k['np'];count=0
 # Independent full8x8 action: a=c+c†, paired second gamma=i(c-c†).
 matrices=[]
 for j in range(3):
  for second in (False,True):
   A=np.zeros((8,8),complex)
   for b in range(8):
    sg=(-1)**sum((b>>i)&1 for i in range(j));A[b^(1<<j),b]=sg*(1j*(2*((b>>j)&1)-1) if second else 1)
   matrices.append(A)
 for p in (0,1):
  bs=[i|(((i.bit_count()%2)^p)<<2) for i in range(4)];bt=[i|(((i.bit_count()%2)^(1-p))<<2) for i in range(4)]
  for m,A in enumerate(matrices):
   coeff=[(0,0)]*3;coeff[m//2]=(0,1) if m%2 else (1,0)
   for col in range(4):
    x=np.eye(4,dtype=complex)[:,col];got=k['gamma'](x,p,coeff)
    if not np.array_equal(got,A[np.ix_(bt,bs)][:,col]):raise ValueError('actual gamma X/Y')
    count+=1
  for i in range(6):
   for j in range(6):
    if not np.array_equal(matrices[i]@matrices[j]+matrices[j]@matrices[i],2*np.eye(8)*(i==j)):raise ValueError('CAR')
    count+=1
 coeff={i:[(int(j==i//2 and i%2==0),int(j==i//2 and i%2==1)) for j in range(3)] for i in range(6)}
 bs=[i|((i.bit_count()%2)<<2) for i in range(4)];lam=[1,4,9];edges=[(0,3,2),(2,5,-2)]
 H=np.diag([sum((j+1)*((b>>j)&1) for j in range(3)) for b in range(8)]).astype(complex)
 for i,j,c in edges:H+=-1j*c*(matrices[i]@matrices[j])
 for col in range(4):
  x=np.eye(4,dtype=complex)[:,col];got=k['action'](x,coeff,edges,[0,1],lam)
  if not np.array_equal(got,H[np.ix_(bs,bs)][:,col]):raise ValueError('unequal diagonal/pair action')
  count+=1
 return count
checks=verify(text);mutants=[]
for name,old,new in [('wrongY','(2*occupied-1)','(1-2*occupied)'),('edgefactor','(-1j*k)*term','(-0.5j*k)*term')]:
 try:verify(text.replace(old,new))
 except ValueError as e:mutants.append({'name':name,'killed':True,'failure':str(e)})
 else:raise ValueError('surviving mutant '+name)
print(json.dumps({'actual_kernel_toy_checks':checks,'mutants':mutants,'physical_actions':0},indent=2))
