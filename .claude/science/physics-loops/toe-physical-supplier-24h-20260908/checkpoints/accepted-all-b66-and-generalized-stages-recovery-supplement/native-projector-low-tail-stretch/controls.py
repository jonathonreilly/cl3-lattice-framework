from fractions import Fraction as F
import json
checks=[]
def ck(x):assert x;checks.append(True)
a=F(17,60);e=F(1,128);L2=2*a
ck(3/(1-3*3*L2*e)==F(3840,1229));ck(F(3840,1229)<F(25,8));ck(F(37,20)**2>F(17,5));ck(F(1,11)**2>e)
ck(L2*3*F(25,8)==F(85,16));ck(F(85,16)*e/3==F(85,6144));ck(3*F(25,8)*9*L2**2==F(867,32))
r=F(2,9)*F(5439,160)/1408+F(1,6)*F(867,32)/128**2;ck(r<F(3,500))
old=F(357,3200)+F(1,8)+429*F(4,25)**6+F(1,200);ck(old<F(1,4));ck(F(85,6144)<F(357,3200))
print(json.dumps({'status':'PASS','exact_rational_controls':len(checks),'native_calls':0}))
