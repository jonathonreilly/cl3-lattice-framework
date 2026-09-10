"""Strict source-only readiness / once-only future coefficient dispatcher."""
import time
START=time.monotonic()
import sys,json,hashlib,types,argparse,signal,resource,os
from pathlib import Path
sys.set_int_max_str_digits(20000)
P=Path(__file__).resolve().parent

def need(x,m):
    if not x:raise ValueError(m)

def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for block in iter(lambda:f.read(1048576),b''):h.update(block)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['readiness','assemble']);ap.add_argument('output');args=ap.parse_args()
    freeze_hash=sha(P/'RUNTIME_FREEZE.json');f=json.loads((P/'RUNTIME_FREEZE.json').read_text());auth_hash=None
    def budget():
        need(time.monotonic()-START<f['worker_seconds'],'inclusive worker time')
        need(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<=384*1048576,'worker RSS bytes')
    def pins(scientific):
        budget();need(sha(P/'RUNTIME_FREEZE.json')==freeze_hash,'immutable freeze')
        need(sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode,'strict -I -B -S')
        need(str(Path(sys.executable).resolve())==f['interpreter'],'interpreter')
        need(sorted(x.name for x in P.iterdir())==f['membership'],'exact source membership')
        pinset=dict(f['inputs'])
        if scientific:pinset.update(f['scientific_inputs'])
        if scientific and auth_hash is not None:need(sha(P/'AUTHORIZATION.json')==auth_hash,'immutable authorization')
        for path,digest in pinset.items():need(sha(path)==digest,'verified pin '+path)
        for module in list(sys.modules.values()):
            path=getattr(module,'__file__',None)
            if path:
                path=str(Path(path).resolve());need(path in f['inputs'] and sha(path)==f['inputs'][path],'loaded origin '+path)
        budget()
    signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('inclusive worker deadline')))
    signal.setitimer(signal.ITIMER_REAL,max(.001,f['worker_seconds']-(time.monotonic()-START)))
    pins(False)
    modules={}
    for name in ('core','binder','worker'):
        path=P/(name+'.py');raw=path.read_bytes();need(hashlib.sha256(raw).hexdigest()==f['inputs'][str(path)],'verified module bytes')
        module=types.ModuleType(name);module.__file__=str(path);sys.modules[name]=module;exec(compile(raw,str(path),'exec'),module.__dict__);modules[name]=module
    pins(False)
    if args.mode=='readiness':
        print(json.dumps({'status':'PASS_SOURCE_ONLY','actual_parser':True,'freeze_sha256':freeze_hash,'accepted_loads':0,'coefficient_assemblies':0,'native_oracle_calls':0}));return
    need(f['execution_enabled'] is True,'runtime NOT_READY')
    binding=json.loads((P/'BINDING.json').read_text());need(binding['status']=='BOUND_ACCEPTED_A378','binding NOT_READY')
    out=Path(args.output).resolve();auth=json.loads((P/'AUTHORIZATION.json').read_text())
    auth_hash=sha(P/'AUTHORIZATION.json')
    need(auth=={'freeze_sha256':freeze_hash,'output':str(out),'once':True},'exact root authorization')
    need(auth['once'] is True,'literal once authorization')
    need(not out.exists() and P not in out.parents and out!=P,'fresh external output')
    error=None;owned=False
    try:
        marker=P.with_name(P.name+'-ATTEMPT');marker.mkdir(exist_ok=False)
        out.mkdir(exist_ok=False);owned=True
        modules['worker'].save(out/'STARTED.json',auth)
        pins(True)
        modules['worker'].run(out,binding,modules['core'],modules['binder'],budget)
        pins(True)
        modules['worker'].save(out/'WORKER_COMPLETE.json',{'status':'COMPLETE','scope':'NEW_A_ONLY_DESCRIPTOR_COEFFICIENTS',
            'freeze_sha256':freeze_hash,'binding':binding['identity'],'result_sha256':sha(out/'RESULT.json'),
            'events_sha256':sha(out/'EVENTS.ndjson'),'partial_sha256':sha(out/'PARTIAL.json'),
            'seconds':time.monotonic()-START,'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss})
    except BaseException as exc:error=exc
    finally:
        try:pins(True)
        except BaseException as exc:
            if error is None:error=exc
            else:error.add_note('final immutable closure: '+repr(exc))
    if error is not None:
        if owned:
            try:modules['worker'].save(out/'DISPATCH_FAILURE.json',{'error':repr(error),'notes':getattr(error,'__notes__',[]),'seconds':time.monotonic()-START})
            except BaseException as exc:error.add_note('dispatcher retention: '+repr(exc))
        raise error

if __name__=='__main__':main()
