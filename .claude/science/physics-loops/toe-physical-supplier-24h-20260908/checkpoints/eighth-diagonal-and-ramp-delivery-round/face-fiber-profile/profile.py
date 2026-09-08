"""One prospective cost fixture. No production sampler."""
import time
START=time.monotonic()
import signal
signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('30 seconds')))
if __name__=='__main__':signal.alarm(30)
import pathlib,json,random,resource,sys,argparse,gc,hashlib
from factory import Geometry,initialize,draw
from checkpoint import save,load,sha
from measure import measure
B=pathlib.Path(__file__).resolve().parent

def rss():return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
def gate():
 if time.monotonic()-START>=30 or rss()>384:raise RuntimeError('resource cap')
def write(out,rows,status):
 (out/'PARTIAL.json').write_text(json.dumps(dict(status=status,cases=rows,elapsed=time.monotonic()-START,rss_mib=rss()),indent=2))
def main(out):
 out=pathlib.Path(out);out.mkdir(exist_ok=False);rows=[]
 for case,V in enumerate((.95,0.)):
  row=dict(case=case,V=V,L=8,n=110592,RK=2048,faces=[0,512,1024],init_seed=202609320100+case,draw_seed=202609320200+case,blocks=[],measurements=[])
  rows.append(row);write(out,rows,'initializing')
  t=time.monotonic();g=Geometry(8);row['geometry_seconds']=time.monotonic()-t;gate()
  t=time.monotonic();obj,meta=initialize(g,110592,V,random.Random(row['init_seed']),2048);row['initializer_seconds']=time.monotonic()-t;row['initializer']=meta;gate()
  row['initial_states_sha']=hashlib.sha256(b''.join(x.to_bytes(192,'little') for x in obj.states)).hexdigest()
  t=time.monotonic();row['measurements'].append(measure(obj));row['measurement_seconds']=time.monotonic()-t;rng=random.Random(row['draw_seed']);write(out,rows,'blocks')
  for p in row['faces']:
   t=time.monotonic();uniforms=[rng.random() for _ in obj.states];draw(obj,p,uniforms);row['blocks'].append(dict(face=p,seconds=time.monotonic()-t));del uniforms;gate()
   t=time.monotonic();row['measurements'].append(measure(obj));row['measurement_seconds']+=time.monotonic()-t;write(out,rows,'blocks')
  t=time.monotonic();m=save(obj,out/('case'+str(case)));row['checkpoint_save_seconds']=time.monotonic()-t;gate()
  t=time.monotonic();other=load(g,out/('case'+str(case)),(8,110592,V));row['checkpoint_load_seconds']=time.monotonic()-t
  if other.states!=obj.states or other.nf!=obj.nf or other.witness!=obj.witness:raise ValueError('checkpoint identity')
  row['checkpoint_meta_sha']=sha(out/('case'+str(case))/'meta.json');row['checkpoint']=m;row['completed']=True;write(out,rows,'case complete');gate();del other,obj,g;gc.collect()
 write(out,rows,'complete');(out/'RESULT.json').write_text((out/'PARTIAL.json').read_text())
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',required=True);a=p.parse_args();main(a.out)
