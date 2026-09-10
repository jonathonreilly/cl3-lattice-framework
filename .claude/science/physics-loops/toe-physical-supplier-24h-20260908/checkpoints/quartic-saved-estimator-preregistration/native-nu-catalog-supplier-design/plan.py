"""Predata rational budgets only. Never loads a scalar catalog."""
from fractions import Fraction as F
import json
EPS=F(1,2**64);ORDER=40
quadrature=256*F(1,4**52)
low_width=F(17,60)*EPS**5/5
high_width=F(12**(ORDER+2),(2*ORDER+1)*8**(2*ORDER+1))
# A interval width<3e-30; independent t interval width<2^-140.
# |d(6-t²+t⁴A)/dt| holding A fixed <=16+4*8³*(17/60)<600.
node_width=4096*F(3,10**30)+600*F(1,2**140)
middle_width=9*node_width+1742*7*F(1,10**38)+F(1,10**45)
pi_allowance=F(1,10**35)
full_width=F(100,157)*(2*quadrature+low_width+high_width+middle_width)+pi_allowance
assert F(9,4)-F(17,16)**2-F(15,16)**2==F(31,128)>0
assert node_width<F(2,10**26) and middle_width<F(2,10**25)
assert full_width<F(2,10**19)
if __name__=='__main__':print(json.dumps({k:str(v)for k,v in locals().copy().items()if k in('quadrature','low_width','high_width','node_width','middle_width','full_width')},indent=2))
