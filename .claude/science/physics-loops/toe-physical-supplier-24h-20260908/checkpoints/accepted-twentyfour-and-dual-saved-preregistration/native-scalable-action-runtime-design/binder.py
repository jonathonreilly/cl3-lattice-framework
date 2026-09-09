"""Actual24 result and independently accepted POST not bound yet."""
def load(*a,**k):raise ValueError('NOTREADY: accepted twelve-to24 result/POST and same-family DATA closure required')
import hashlib
from pathlib import Path
def sha(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
