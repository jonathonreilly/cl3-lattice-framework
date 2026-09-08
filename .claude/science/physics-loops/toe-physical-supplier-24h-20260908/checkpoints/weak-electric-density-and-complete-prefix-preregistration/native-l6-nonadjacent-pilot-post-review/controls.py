from fractions import Fraction as F
from replay import inv,mat,ck
import json
G=[[F(5),F(2)],[F(2),F(1)]];C=[G[i]+[F(i==j) for j in range(2)] for i in range(2)]+[[F(i==j) for j in range(2)]+[F(0)]*2 for i in range(2)];Ci=[[F(0),F(0),F(1),F(0)],[F(0),F(0),F(0),F(1)],[F(1),F(0),F(-5),F(-2)],[F(0),F(1),F(-2),F(-1)]];I=[[F(i==j) for j in range(4)] for i in range(4)];ck(mat(C,Ci)==I,'C inverse')
T=[[F((i+1)*(j+1),13) for j in range(4)] for i in range(4)];S=[[a+b for a,b in zip(row,t)] for row,t in zip(Ci,T)];M=[[a+b for a,b in zip(row,t)] for row,t in zip(I,mat(C,T))];ck(mat(inv(S),Ci)==inv(M),'alternative inverse')
wrong=[row[:] for row in Ci];wrong[2][3]*=-1;ck(mat(C,wrong)!=I,'sign mutant')
print(json.dumps({'controls':3,'scope':'synthetic exact reduced inverse identity/sign; no native gap calculation'}))
