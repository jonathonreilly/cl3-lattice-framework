"""No actual pilot history, scalar loader or entry reader may run yet."""
def load(*args,**kwargs):
 raise ValueError('NOTREADY: independently accepted pilot saved-state POST and bound context required')
import hashlib
from pathlib import Path
def sha(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as f:
  for x in iter(lambda:f.read(1048576),b''):h.update(x)
 return h.hexdigest()
