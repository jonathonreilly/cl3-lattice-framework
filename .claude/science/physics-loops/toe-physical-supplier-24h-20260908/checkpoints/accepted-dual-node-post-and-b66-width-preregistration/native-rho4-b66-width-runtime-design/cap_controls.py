from fractions import Fraction as F
from caps import guard,upward,operand,pole,tree
checks=0
for x in(F(0),F(1,3),F(1,2**300)):
 y=upward(x);assert y>=x and y-x<F(1,2**256);checks+=1
for fun,x in((guard,F(2**32768)),(operand,F(2**512)),(pole,F(1,2**256)),(tree,{'widths':[F(2**32768)]})):
 try:fun(x)
 except ValueError:checks+=1
 else:raise AssertionError('cap bypass')
print({'status':'PASS_CAP_ADVERSES','checks':checks,'actual_scan':False})
