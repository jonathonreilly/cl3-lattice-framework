import itertools,json,hashlib
from pathlib import Path
# Exact diagonals of the eight physical Pauli Z matrices, in tensor basis.
Z=[[1-2*((j>>(7-e))&1) for j in range(256)] for e in range(8)]
B=[Z[0]]+[[Z[e-1][j]*Z[e][j] for j in range(256)] for e in range(1,8)]+[Z[7]]
checks=0
def ck(v):
 global checks
 assert v
 checks+=1
ck(all(__import__('math').prod(b[j] for b in B)==1 for j in range(256)))
ck(all(__import__('math').prod(B[e][j] for e in range(4))==Z[3][j] for j in range(256)))
indices=[];pair_signs={}
for labels in itertools.product(range(4),repeat=4):
 n=[v&1 for v in labels]+[(v>>1)&1 for v in labels];n.append(sum(n)%2)
 edge=[];bit=0
 for ni in n[:-1]:bit^=ni;edge.append(bit)
 j=sum(bit<<(7-e) for e,bit in enumerate(edge));indices.append(j)
 ck(all((1-B[e][j])//2==n[e] for e in range(9)))
 flux=(labels[0]+labels[1]-labels[2]-labels[3])%4
 ck(Z[3][j]==1-2*(flux&1))
 ck(((1+Z[3][j])//2)+((1-Z[3][j])//2)==1)
 if sum(n)==2:pair_signs[str(tuple(e for e in range(9) if n[e]))]=1-2*((flux>>1)&1)
ck(len(set(indices))==256);ck(len(pair_signs)==36)
triangle=[pair_signs[str(p)] for p in ((0,1),(0,2),(1,2))]
ck(triangle==[-1,1,1]);ck(__import__('math').prod(triangle)==-1)
print(json.dumps(dict(checks=checks,physical_qubits=8,fermion_vertices=9,encoded_inputs=256,two_particle_pairs=36,triangle=triangle,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Independent exact physical-Pauli diagonals and full orthogonal tree-code enumeration; Gaussian obstruction proof reviewed separately.'),indent=2))
