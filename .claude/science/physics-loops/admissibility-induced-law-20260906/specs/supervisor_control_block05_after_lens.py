import sys; sys.argv=['x']
exec(open('supervisor_control_block05_snake.py').read().split("for j in range(3):\n    c=col_marg")[0])
# natural snake: row 0 L->R (p0), row 1 R->L (P_rl), row 2 L->R (P_lr)
for j in range(3):
    c=col_marg(Prl,Plr,j)
    dev=sum(abs(c[(a,b,d)]-F(1,6)*K[a][b]*K[b][d]) for a in range(M) for b in range(M) for d in range(M))/2
    print(f"natural snake 3x3 column {j}: TV defect from the K-chain = {dev}")
# minimal staircase theorem: P(d | c, b) from the corner law vs K(b,d) at (3,1,2)
def pick(c,b,a,d): return F(1,6)*K[c][a]*K[c][b]*K[a][d]*K[d][b]/K2[a][b]
c,b,d=0,0,0
cond=sum(pick(c,b,a,d) for a in range(M))/(F(1,6)*K[c][b])
print("P(d|c,b) at (0,0,0):",cond,"vs K(b,d)=",K[b][d])
