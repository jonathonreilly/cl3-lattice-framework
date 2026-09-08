import numpy as np
from numba import njit
import producer_original as prod
@njit(cache=True)
def apply_face(state,faces,f):
    if prod.is_flippable(state,faces[f]):
        for i in faces[f]:state[i]^=np.uint8(1)
@njit(cache=True)
def endpoint(state,faces,steps,seed):
    np.random.seed(seed);x=state.copy()
    for _ in range(steps*len(faces)):apply_face(x,faces,np.random.randint(len(faces)))
    return x
@njit(cache=True)
def observe(state,coeff):
    out=np.zeros(len(coeff),np.complex128)
    for m in range(len(coeff)):
        for i in range(len(state)):out[m]+=coeff[m,i]*(float(state[i])-.5)
    return out
@njit(cache=True)
def collect(initial,faces,coeff,lags,caps,burn,chain_id):
    count=len(lags);m=len(coeff);origins=np.empty((count,m),np.complex128);products=np.zeros((count,3,m),np.complex128);snapshots=np.empty((count,len(initial)),np.uint8)
    state=endpoint(initial,faces,burn*len(faces),300000000+chain_id)
    for i in range(count):
        state=endpoint(state,faces,len(faces),200000000+1000*chain_id+i)
        snapshots[i]=state;o=observe(state,coeff);origins[i]=o
        for a in range(3):
            if lags[i,a]<=caps[a]:
                other=endpoint(state,faces,lags[i,a],100000000+1000*chain_id+3*i+a)
                products[i,a]=np.conjugate(o)*observe(other,coeff)
    return origins,products,snapshots

def generate_lags(U,q):
    return np.floor(np.log1p(-U)/np.log(q)).astype(np.int64)
