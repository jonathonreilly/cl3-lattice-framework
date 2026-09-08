"""Binary even-L tilted kernel with concatenated real/imag Fourier cache; source scheduling/limits belong to caller. No top-level run."""
import numpy as np
from numba import njit
import producer_original as prod

@njit(cache=True)
def source_norm(obs):
    return np.sum(obs*obs)

@njit(cache=True)
def branch_value(count,xvalue,delta_v,lam,shift,M):
    return 1.0-delta_v*count/M+(shift-lam*xvalue)/M

@njit(cache=True)
def literal_O(state,coeff):
    out=np.zeros(coeff.shape[0],np.float64)
    for m in range(coeff.shape[0]):
        for i in range(len(state)):out[m]+=coeff[m,i]*(float(state[i])-.5)
    return out

@njit(cache=True)
def flip_cached(state,count,O,f,coeff,faces,affected,affected_counts):
    for m in range(len(O)):
        delta=0.
        for i in faces[f]:delta+=coeff[m,i]*(1.-2.*state[i])
        O[m]+=delta
    return prod.flip_and_update_count(state,f,count,faces,affected,affected_counts)

@njit(cache=True)
def resample(states,counts,obs,ancestors,weights):
    indices,eff=prod.systematic_indices(weights)
    return states[indices].copy(),counts[indices].copy(),obs.copy(),ancestors[indices].copy(),eff

@njit(cache=True)
def sweep(states,counts,obs,ancestors,dv,lam,shift,coeff,faces,affected,affected_counts,interval):
    P=len(states);M=len(faces);logs=np.zeros(P);minimum=float(P)
    for step in range(M):
        for w in range(P):
            xv=source_norm(obs[w]);b=branch_value(counts[w],xv,dv,lam,shift,M)
            if not np.isfinite(b) or b<1.-1e-12:raise ValueError('invalid branch')
            logs[w]+=np.log(b);f=np.random.randint(M)
            if prod.is_flippable(states[w],faces[f]) and np.random.random()<1./b:
                counts[w]=flip_cached(states[w],counts[w],obs[w],f,coeff,faces,affected,affected_counts)
        if (step+1)%interval==0:
            states,counts,obs,ancestors,eff=resample(states,counts,obs,ancestors,logs);minimum=min(minimum,eff);logs[:]=0.
    if M%interval:
        states,counts,obs,ancestors,eff=resample(states,counts,obs,ancestors,logs);minimum=min(minimum,eff)
    return states,counts,obs,ancestors,minimum

@njit(cache=True)
def prepare(start,dv,lam,shift,P,classical,burn,coeff,faces,affected,affected_counts,interval,seed):
    np.random.seed(seed);states=np.empty((P,len(start)),np.uint8);counts=np.empty(P,np.int32)
    for w in range(P):states[w]=start;counts[w]=prod.count_flippable(states[w],faces)
    for _ in range(classical):
        for step in range(len(faces)):
            for w in range(P):
                f=np.random.randint(len(faces))
                if prod.is_flippable(states[w],faces[f]):counts[w]=prod.flip_and_update_count(states[w],f,counts[w],faces,affected,affected_counts)
    obs=np.empty((P,len(coeff)),np.float64)
    for w in range(P):obs[w]=literal_O(states[w],coeff)
    anc=np.arange(P,dtype=np.int32);minimum=float(P);n=min(40,burn);ns=np.empty(n);xs=np.empty(n);maximum_drift=0.
    for j in range(burn):
        states,counts,obs,anc,eff=sweep(states,counts,obs,anc,dv,lam,shift,coeff,faces,affected,affected_counts,interval);minimum=min(minimum,eff)
        if j>=burn-n:
            ns[j-burn+n]=np.mean(counts);xs[j-burn+n]=np.sum(obs*obs)/P
            for w in range(P):maximum_drift=max(maximum_drift,np.max(np.abs(obs[w]-literal_O(states[w],coeff))))
            if not np.isfinite(maximum_drift) or maximum_drift>1e-10:raise ValueError('Fourier cache drift')
    return states,counts,obs,ns,xs,minimum,maximum_drift,len(np.unique(anc))/P
