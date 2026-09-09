import sys,types,tempfile,json
from pathlib import Path
p=Path('/private/tmp/toe-24h-probes-20260908/native-coordinate-free-native-runtime-design')
sys.modules['adapter']=types.SimpleNamespace();sys.modules['binder']=types.SimpleNamespace()
n={};exec(compile((p/'worker.py').read_bytes(),str(p/'worker.py'),'exec'),n)
class D:
 def __init__(self):self.v=self.c=0
 def verify(self):self.v+=1;raise ValueError('verify toy')
 def close(self):self.c+=1;raise ValueError('close toy')
checks=0
with tempfile.TemporaryDirectory()as t:
 ds=[D()for _ in range(3)]
 try:n['compute']({'descriptors':ds},Path(t))
 except FileExistsError as e:assert e.__notes__;checks+=1
 assert all(d.v==d.c==1 for d in ds);checks+=1
 ds=[D()for _ in range(3)]
 def fail(*args):raise OSError('initial write toy')
 n['save']=fail
 try:n['compute']({'descriptors':ds},Path(t)/'new')
 except OSError as e:assert str(e)=='initial write toy' and e.__notes__;checks+=1
 assert all(d.v==d.c==1 for d in ds);checks+=1
sys.set_int_max_str_digits(20000);s=str((1<<65536)-1);assert len(s)==19729 and int(s)==(1<<65536)-1;checks+=1
print(json.dumps({'synthetic_checks':checks,'native_calls':0}))
