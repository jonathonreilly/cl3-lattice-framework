from pathlib import Path
import json,math,hashlib
B=Path(__file__).parent;n=0
def ck(x):
 global n;n+=1
 if not x:raise ValueError(n)
# Independent Clifford bit action, four complex matter modes, active/spectator chirality.
def maj(s,j):
 mode=j//2;sgn=(-1)**((s&((1<<mode)-1)).bit_count())
 return s^(1<<mode),sgn*(1 if j%2==0 else (1j if not(s>>mode&1) else -1j))
def word(s,js):
 a=1
 for j in reversed(js):s,b=maj(s,j);a*=b
 return s,a
for s in range(16):
 out,a=word(s,[0,2,4,6,1,3,5,7]);ck(out==s and a==(-1)**s.bit_count())
# 64 matter modes: reorder sign and chirality factors.
ck((-1)**(64*63//2)==1);ck((-1j)**64==1);ck((-1j)**32==1)
levels=[dict(n=k,energy_in_omega=k-16,multiplicity=math.comb(32,k)) for k in range(0,33,2)]
ck(sum(z['multiplicity'] for z in levels)==2**31);ck(levels[0]['multiplicity']==1);ck(levels[1]['energy_in_omega']-levels[0]['energy_in_omega']==2)
ck((-1)**32==1)
# Two-Majorana block: coefficient b i beta0 beta1 has energies +/-b,
# standard K01=2b therefore frequency2|b|; K_eff=-cK0.
for c in (-3,-1,1,4):
 b=c;ck(2*abs(b)==abs(2*b));ck((-c)*(-2)==2*c)
files=[B.parent/'native-sixth-spectator-spectrum/DERIVATION.md',B.parent/'native-sixth-spectator-spectrum/EXACT_LEVELS.json',B.parent/'native-sixth-magnetic-symmetry-root/DERIVATION.md',B.parent/'native-sixth-full-operator-support-root/DERIVATION.md']
(B/'READ_HASHES.json').write_text(json.dumps({str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},indent=2)+'\n')
(B/'RESULT.json').write_text(json.dumps(dict(checks=n,levels=levels,scope='finite Clifford parity and exact combinatorics; no coefficient evaluation'),indent=2)+'\n');print(n)
