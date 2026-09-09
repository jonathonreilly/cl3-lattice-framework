"""Independent float-ratio norm replay. No author scanner imports."""
import struct,math,hashlib,json,sys,signal,time,resource,argparse
from pathlib import Path
EXPONENT=2148

def exact_square(value):
 if not math.isfinite(value):raise ValueError('nonfinite component')
 numerator,denominator=value.as_integer_ratio()
 power=denominator.bit_length()-1
 if denominator!=1<<power or power>1074:raise ValueError('non-dyadic binary64')
 return numerator*numerator << (EXPONENT-2*power)

def scan(path,modes,parity,chunk_entries=4096):
 if type(modes) is not int or not 1<=modes<=30 or type(parity) is not int or parity not in (0,1) or type(chunk_entries) is not int or not 1<=chunk_entries<=65536:raise ValueError('domain')
 path=Path(path);expected=1<<(modes-1)
 if path.stat().st_size!=16*expected:raise ValueError('exact file length')
 sums=[0]*(modes+1);index=0;digest=hashlib.sha256()
 with path.open('rb') as file:
  while True:
   raw=file.read(chunk_entries*16)
   if not raw:break
   if len(raw)%16:raise ValueError('partial complex record')
   digest.update(raw)
   for real,imag in struct.iter_unpack('<dd',raw):
    if index>=expected:raise ValueError('extra record')
    # Independent reconstruction of the omitted occupation bit via XOR reduction.
    remaining=index;low=0;xor=parity
    while remaining:
     bit=remaining&1;low+=bit;xor^=bit;remaining>>=1
    particles=low+xor
    sums[particles]+=exact_square(real)+exact_square(imag);index+=1
 if index!=expected:raise ValueError('short file')
 return dict(entries=index,parity=parity,modes=modes,denominator_exponent=EXPONENT,squared_norm_numerator=str(sum(sums)),particle_numerators=list(map(str,sums)),input_sha256=digest.hexdigest())

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--input',required=True);parser.add_argument('--modes',type=int,required=True);parser.add_argument('--parity',type=int,required=True);parser.add_argument('--output',required=True);args=parser.parse_args()
 if not(sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode):raise ValueError('-I -B -S required')
 root=Path(__file__).resolve().parent
 binding=json.loads((root/'RUNTIME.json').read_text())
 if str(Path(sys.executable).resolve())!=binding['interpreter']:raise ValueError('interpreter')
 for path,h in binding['files'].items():
  if hashlib.sha256(Path(path).read_bytes()).hexdigest()!=h:raise ValueError('runtime pin '+path)
 for module in tuple(sys.modules.values()):
  path=getattr(module,'__file__',None)
  if path and str(Path(path).resolve())!=str(Path(__file__).resolve()) and str(Path(path).resolve()) not in binding['files']:raise ValueError('unbound module '+path)
 out=Path(args.output)
 if out.exists():raise ValueError('fresh output')
 start=time.monotonic();signal.alarm(29)
 result=scan(args.input,args.modes,args.parity)
 if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>384*1048576:raise ValueError('RSS')
 result.update(status='COMPLETE',seconds=time.monotonic()-start,rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 out.write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':main()
