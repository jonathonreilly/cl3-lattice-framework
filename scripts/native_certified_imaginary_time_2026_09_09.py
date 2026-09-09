"""Small exact supporting controls only; never a native propagation."""
import argparse, contextlib, hashlib, io, json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'outputs'/'native_certified_imaginary_time_2026_09_09_inputs'

def main():
 parser=argparse.ArgumentParser()
 parser.add_argument('--json',action='store_true')
 args=parser.parse_args()
 manifest=json.loads((P/'MANIFEST.json').read_text())
 for name,digest in manifest.items():
  if hashlib.sha256((ROOT/name).read_bytes()).hexdigest()!=digest:
   raise RuntimeError('source pin '+name)
 source=(ROOT/'scripts/native_certified_imaginary_time_2026_09_09_algebra.py').read_bytes()
 capture=io.StringIO()
 with contextlib.redirect_stdout(capture):
  exec(compile(source,str(ROOT/'scripts/native_certified_imaginary_time_2026_09_09_algebra.py'),'exec'),{'__name__':'__main__','__file__':str(ROOT/'scripts/native_certified_imaginary_time_2026_09_09_algebra.py')})
 algebra=json.loads(capture.getvalue())
 if algebra['exact_predicates']!=11 or algebra['status']!='PASS':raise RuntimeError('algebra receipt')
 budget=6*F(3)**25*F(2,3)**129
 if not budget<F(1,10**10):raise RuntimeError('degree128 budget')
 if 6*F(3)**25*F(2,3)**65<F(1,10**10):raise RuntimeError('adverse reduced degree')
 r=F(99,100)
 margin=2*r-99*(1-r*r)
 if margin!=F(99,10000):raise RuntimeError('margin')
 if 2*F(9,10)-99*(1-F(9,10)**2)>=0:raise RuntimeError('adverse smaller disk')
 out={'status':'SUPPORTING_CONTROLS_PASS','scope':'exact synthetic algebra and rational bounds; no native propagation','algebra_predicates':11,'additional_rational_predicates':4,'degree128_upper':str(budget),'disk_margin':str(margin),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'inputs':manifest}
 print(json.dumps(out,sort_keys=True,indent=2))
if __name__=='__main__':main()
