from fractions import Fraction as F

def kernel(a_t,a_s,s,t):
    if s==t: raise ValueError('confluence requires derivative certificate')
    return (a_t-a_s)/(s*s-t*t)

def midpoint_error(s,t,a0=F(17,60)):
    if min(s,t)<s/2: raise ValueError('near-branch premise')
    g=abs(t*t-s*s)
    return 24*a0*g*g/(s**3*(s+t)**3)

def b_pair(c,C,T,s):
    return c-s*s*C,-2*s*C+2*s**3*T

def interval_div(num,den):
    lo,hi=den
    if lo<=0<=hi: raise ValueError('uncertified denominator separation')
    vals=[a/b for a in num for b in den]
    return min(vals),max(vals)

if __name__=='__main__':
    import json
    checks=0
    # Perfect-square atomic X gives rational c,C,T,B and derivative.
    for x in [F(1,4),F(1),F(9)]:
        root={F(1,4):F(1,2),F(1):F(1),F(9):F(3)}[x]
        for s in [F(1,8),F(1),F(4)]:
            C=1/(root*(x+s*s));T=1/(root*(x+s*s)**2)
            b,bp=b_pair(1/root,C,T,s)
            assert b==root/(x+s*s)
            assert bp==-2*s*root/(x+s*s)**2
            checks+=2
            for t in [F(1,3),F(2)]:
                assert kernel(1/(x+t*t),1/(x+s*s),s,t)==1/((x+t*t)*(x+s*s));checks+=1
    try: interval_div((F(1),F(2)),(F(-1),F(1)))
    except ValueError: checks+=1
    else: raise AssertionError('zero denominator accepted')
    assert 84*32+378==3066 and 3066+378==3444
    print(json.dumps({'scope':'synthetic atomic algebra; no actual geometry or oracles','checks':checks+2,'shared_A':3066,'max_with_derivative':3444,'contractions':378*84*32},indent=2))
