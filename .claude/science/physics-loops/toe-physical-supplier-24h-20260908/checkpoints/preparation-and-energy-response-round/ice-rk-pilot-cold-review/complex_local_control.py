import numpy as np,itertools,json
cases=0;wrong=0;maxres=0
for L in [2,4]:
 for h in ([1] if L==2 else [1,2]):
  q=2*np.pi*h/L
  for a,b in itertools.permutations(range(3),2):
   for r in itertools.product(range(L),repeat=3):
    ra=list(r);ra[a]=(ra[a]+1)%L
    for nb in [0,1]:
     # Direct two affected b-link Fourier differences. Equal occupation changes on opposite geometric edges,
     # but opposite root stagger makes oriented E changes opposite as required.
     delta_n0=1-2*nb;delta_n1=delta_n0
     direct=((-1)**sum(r)*np.exp(1j*q*r[a])*delta_n0+(-1)**sum(ra)*np.exp(1j*q*ra[a])*delta_n1)/np.sqrt(L**3)
     expected=(-1)**sum(r)*delta_n0*np.exp(1j*q*r[a])*(1-np.exp(1j*q))/np.sqrt(L**3)
     maxres=max(maxres,abs(direct-expected));assert abs(direct-expected)<1e-14
     assert abs(abs(direct)**2-4*np.sin(q/2)**2/L**3)<1e-14
     bad=(np.exp(1j*q*r[a])+np.exp(1j*q*ra[a]))*delta_n0/np.sqrt(L**3)
     wrong+=abs(bad-direct)>1e-12;cases+=1
assert wrong>0
print(json.dumps({'signed_cases':cases,'max_residual':float(maxres),'wrong_stagger_detected_cases':int(wrong)},indent=2))
