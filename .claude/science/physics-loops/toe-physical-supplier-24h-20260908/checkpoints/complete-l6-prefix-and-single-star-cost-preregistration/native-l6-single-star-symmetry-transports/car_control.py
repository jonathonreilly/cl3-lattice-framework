import json
# Exterior lift of a two-mode swap, explicit 4x4 CAR representation.
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
def tr(A):return list(map(list,zip(*A)))
def creator(i):
 A=[[0]*4 for _ in range(4)]
 for b in range(4):
  if not b>>i&1:A[b|1<<i][b]=(-1)**((b&((1<<i)-1)).bit_count())
 return A
U=[[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,-1]];bad=[r[:] for r in U];bad[3][3]=1
for i in range(2):
 if mm(mm(U,creator(i)),tr(U))!=creator(1-i):raise ValueError('CAR intertwiner')
if mm(mm(bad,creator(0)),tr(bad))==creator(1):raise ValueError('unsigned pair lift mutant')
if [r[0] for r in U]!=[1,0,0,0]:raise ValueError('vacuum phase')
print(json.dumps({'status':'PASS','predicates':4,'scope':'literal CAR signed exterior lift; unsigned pair mutant rejected'}))
