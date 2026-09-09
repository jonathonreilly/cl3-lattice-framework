from pathlib import Path
import json
P=Path(__file__).parent;source=(P/'kernel.py').read_text()
def test(src):
 k={};exec(compile(src,'actualtiny','exec'),k);k.update(MODES=3,TOP=2,SIZE=4,CHUNK=2);np=k['np'];As=[];Bs=[];count=0
 for j in range(3):
  A=np.zeros((8,8));B=A.copy()
  for b in range(8):
   sg=(-1)**((b&((1<<j)-1)).bit_count());A[b^(1<<j),b]=sg;B[b^(1<<j),b]=sg*(2*((b>>j)&1)-1)
  As.append(A);Bs.append(B)
 for parity in (0,1):
  bits=[i|(((i.bit_count()%2)^parity)<<2) for i in range(4)];target=[i|(((i.bit_count()%2)^(1-parity))<<2) for i in range(4)]
  for j in range(3):
   for kind,mat in [('A',As[j]),('B',Bs[j])]:
    for col in range(4):
     x=np.eye(4)[:,col];got=k['linear'](x,parity,[(j,1)],kind)
     if not np.array_equal(got,mat[np.ix_(target,bits)][:,col]):raise ValueError('real A/B')
     count+=1
  H=np.diag([sum((j+1)*((b>>j)&1) for j in range(3)) for b in range(8)]).astype(float)+2*Bs[0]@As[1]-2*Bs[0]@As[2]
  for col in range(4):
   got=k['action'](np.eye(4)[:,col],parity,[(0,1)],{1:[(1,1)],2:[(2,1)]},[(1,2),(2,-2)],[1,2,3])
   if not np.array_equal(got,H[np.ix_(bits,bits)][:,col]):raise ValueError('real pair sign/diagonal')
   count+=1
 return count
n=test(source);killed=[]
for name,old,new in [('Bsign','2*((bits>>j)&1).astype(np.int8)-1','1-2*((bits>>j)&1).astype(np.int8)'),('pairSign','np.multiply(term,k)','np.multiply(term,-k)')]:
 try:test(source.replace(old,new))
 except ValueError as e:killed.append({'name':name,'failure':str(e)})
 else:raise ValueError('surviving mutant')
print(json.dumps({'same_kernel_tiny_checks':n,'mutants':killed,'physical_actions':0}))
