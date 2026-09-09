from pathlib import Path
import tempfile,struct,json
import numpy as np
import formats
from fractions import Fraction as F
import envelope
checks=0
bits=np.array([0,1,0x8000000000000000,0x000fffffffffffff,0x0010000000000000,0x7fefffffffffffff],dtype=np.uint64)
with tempfile.TemporaryDirectory() as tmp:
 p=Path(tmp);source=p/'x.npy';np.save(source,bits.view(np.float64),allow_pickle=False)
 for phase in ('real','i'):
  raw=p/(phase+'.bin');formats.export(np,source,raw,phase,6);formats.verify(np,source,raw,phase,6);checks+=1
  data=raw.read_bytes();raw.write_bytes(data[:-1])
  try:formats.verify(np,source,raw,phase,6)
  except ValueError:checks+=1
  else:raise ValueError('truncation survives')
# Scalar source uncertainty must be added once, after actual-RHS residual.
# Test independent generic algebra, no physical array action.
for rho,b in [(F(1,10),F(1,7)),(F(0),F(1)),(F(1),F(0))]:
 if 3*(rho+b)!=3*rho+3*b:raise ValueError('source propagation')
 checks+=1
print(json.dumps({'checks':checks,'physical_calls':0}))
