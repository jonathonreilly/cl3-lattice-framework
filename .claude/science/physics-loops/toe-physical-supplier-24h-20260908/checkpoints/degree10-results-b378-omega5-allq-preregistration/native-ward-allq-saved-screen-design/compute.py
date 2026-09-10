from fractions import Fraction as F
import interval as I

def screen(E,s0P,s0O):
 if E[0]<0 or s0P[0]<0 or s0O[0]<0:raise ValueError('negative saved norm input')
 root2=I.root(I.point(2));root15=I.root(I.point(15));root30=I.root(I.point(30))
 # Directed interval operations even though only indicated one-sided endpoints used.
 X=I.scale(root15,4);V=I.scale(root30,32)
 C=I.mul(E,I.add(I.add(I.scale(X,2),E),V))
 a2=I.scale(I.add(I.scale(s0P,12),I.scale(s0O,3)),F(1,8))
 rhs=I.mul(a2,I.add(I.point(1),I.scale(root2,8)))
 return {'E':E,'s0P':s0P,'s0O':s0O,'X':X,'V':V,'C':C,'a2':a2,'threshold':rhs,'margin_lower':I.check(C[0]-rhs[1]),'excluded':C[0]>=rhs[1],'status':'CERTIFICATE_FAMILY_EXCLUDED'if C[0]>=rhs[1]else'INDETERMINATE_SCREEN'}
