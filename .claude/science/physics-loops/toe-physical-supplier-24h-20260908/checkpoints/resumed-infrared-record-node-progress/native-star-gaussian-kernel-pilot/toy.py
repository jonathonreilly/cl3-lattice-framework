"""Non-native two-mode checks only."""
import json
import numpy as np
from kernel import vacuum_kernel,literal_kernel,require

def run():
    k=np.array([[0,1,0,0],[-1,0,0,0],[0,0,0,2],[0,0,-2,0]],float)
    b=k+np.array([[0,0,.3,.2],[0,0,0,-.1],[-.3,0,0,0],[-.2,.1,0,0]])
    c=k+np.array([[0,.2,0,-.1],[-.2,0,.4,0],[0,-.4,0,0],[.1,0,0,0]])
    x=np.array([1,0,0,0],complex); y=np.array([0,1j,.3,0],complex)
    rows=[]
    for t,s in [(0.,0.),(1/128,1/64),(1/64,1/64)]:
        for insertions in [[],[(0,x),(1,y)],[(0,y),(1,x)]]:
            seg=[(c,t),(b,s)]
            a,diag=vacuum_kernel(seg,insertions,-1.5); ref=literal_kernel(seg,insertions,-1.5)
            require(abs(a-ref)<2e-12,'Gaussian/Fock toy mismatch')
            rows.append({'error':abs(a-ref),**diag})
    return {'status':'PASS','non_native_comparisons':len(rows),'rows':rows,'physical_runs':0}
if __name__=='__main__': print(json.dumps(run(),indent=2))
