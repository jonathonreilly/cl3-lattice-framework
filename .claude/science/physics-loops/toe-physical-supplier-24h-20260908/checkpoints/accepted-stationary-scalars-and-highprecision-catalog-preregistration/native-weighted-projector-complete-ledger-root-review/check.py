from fractions import Fraction as F
import json,time,resource,signal
signal.alarm(10);t=time.monotonic();checks=[]
def test(v):
 assert v
 checks.append(True)
eA=F(2**37,10**30);eN=F(1,2**60)
test(264*2**24<2**33);test(12*2**33<2**37)
test(4*318*1056*eA < (F(1,10**6)-1056*eA)**2)
test(4*318*1056*eN < (F(2,10**6)-1056*eN)**2)
test(F(318,2**40)<F(1,10**9))
test(F(35*17,60)<10);test(F(35*16*17,2*10*9)<53)
test(F(3001,10**6)+F(3,10**6)+F(1,10**9)+F(2,10**10)<F(3005,10**6)<F(1,200))
print(json.dumps({'status':'PASS','checks':len(checks),'seconds':time.monotonic()-t,'rss':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'physical_calls':0}))
