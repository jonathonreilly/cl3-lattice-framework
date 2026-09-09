from fraction_core import *
m=point([[2,1],[1,3]]);c=point([[1,2],[0,1]]);b=point([[0,-1],[1,0]])
h,a,z=gram_action(m,c,b)
assert h==point([[2,5],[5,15]])
assert a==point([[1,-2],[5,-5]])
assert z==point([[3,-1],[-1,2]])
assert multiply(m,c)!=multiply(c,m)
print('{"status":"PASS","cases":4,"scope":"tiny noncommuting exact matrices only"}')
