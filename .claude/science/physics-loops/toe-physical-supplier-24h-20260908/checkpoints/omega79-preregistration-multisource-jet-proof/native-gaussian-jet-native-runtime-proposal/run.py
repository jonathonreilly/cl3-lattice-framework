"""Source-only dispatcher proposal. Native activation deliberately impossible."""
import sys,json,pathlib,hashlib,types
P=pathlib.Path(__file__).resolve().parent
def main():
 if not(sys.flags.isolated and sys.dont_write_bytecode and sys.flags.no_site):raise ValueError('-I-B-S required')
 if sys.argv[1:]!=['readiness']:raise ValueError('NOT_READY: missing accepted omega7/9, binder, reviewed root and preregistration')
 f=json.loads((P/'SOURCE_FREEZE.json').read_text())
 for name,digest in f['files'].items():
  if hashlib.sha256((P/name).read_bytes()).hexdigest()!=digest:raise ValueError('source changed '+name)
 for name in ['core','worker','adapter']:
  p=P/(name+'.py');raw=p.read_bytes();m=types.ModuleType(name);m.__file__=str(p);sys.modules[name]=m;exec(compile(raw,str(p),'exec'),m.__dict__)
 print(json.dumps({'status':'PASS_SOURCE_ONLY','native_binding':'NOT_READY','scientific_calls':0}))
if __name__=='__main__':main()
