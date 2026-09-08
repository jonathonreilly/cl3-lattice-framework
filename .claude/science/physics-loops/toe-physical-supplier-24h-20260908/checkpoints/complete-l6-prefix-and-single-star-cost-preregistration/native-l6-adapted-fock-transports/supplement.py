from pathlib import Path
import runpy,numpy as np,math,json
p=Path(__file__).parent;t=runpy.run_path(str(p/'transport.py'));count=0
for k in range(48):
 E,T,d=t['blocks'](k);U=np.zeros((8,8),dtype=int)
 for j,(i,s) in enumerate(T):U[i,j]=s
 for j in range(3):
  def cd(j):
   A=np.zeros((8,8),dtype=int)
   for b in range(8):
    if not b>>j&1:A[b|1<<j,b]=(-1)**((b&((1<<j)-1)).bit_count())
   return A
  target,sign=T[1<<j]
  if not np.array_equal(U@cd(j)@U.T,sign*cd(target.bit_length()-1)):raise ValueError('8CAR')
  count+=1
 R=np.array([[float(a)+float(b)*math.sqrt(3) for a,b in row] for row in E]);L=np.zeros((4,4));L[0,0]=1;L[1:3,1:3]=R;L[3,3]=d;v=np.arange(32,dtype=float);out=v.copy();t['_eg'](out,0,R,d)
 if np.max(np.abs(out-np.kron(np.eye(8),L)@v))>1e-12:raise ValueError('ordinaryEg')
 count+=1
print(json.dumps({'status':'PASS','predicates':count,'scope':'exact integer8CAR and tiny actual ordinary Eg action'}))
