from pathlib import Path
import contextlib,io,runpy,json
from fractions import Fraction as F
p=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):d=runpy.run_path(str(p/'check.py'))
v=d['powers'][1];O=d['O'];n=d['n'];Z=v*v;mu2=d['mom'][2];S=F(d['z'],n)
mean=F(sum(int(x)for x in Z),n);var=F(sum(int(x)**2 for x in Z),n)-mean**2
influence=sum((F(int(x))-mu2*int(o)**2)**2 for x,o in zip(Z,O))/n/S**2
assert mean/S==mu2 and var>0 and influence>0
print(json.dumps({'integer_second_numerator_mean':str(mean),'integer_second_numerator_variance':str(var),'physical_second_numerator_variance':str(var/1024),'iid_ratio_influence_variance':str(influence),'checks':3},indent=2))
