from fractions import Fraction as F
import interval as I
import spectral as S

def run():
 n=0
 for x in [F(1),F(2),F(4)]:
  p0,p1=F(1,3),F(1,7);m=[I.point(x**j)for j in range(7)];r=S.first_moments(m,p0,p1,lambda *_:None)
  for j in range(3):assert r[j]==I.point((1-p0*x-p1*x*x)**2*x**j);n+=1
  u=S.inverse_squared(r,lambda *_:None);assert u==(1-p0*x-p1*x*x)**2/x**2;n+=1
 try:S.inverse_squared([I.point(-1)]*3,lambda *_:None)
 except ValueError:n+=1
 else:raise AssertionError('contradiction accepted')
 return {'status':'PASS_SYNTHETIC_ONLY','checks':n,'native_inputs':0}
if __name__=='__main__':print(run())
