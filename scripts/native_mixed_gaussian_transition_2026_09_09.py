#!/usr/bin/env python3
"""Portable supporting checks; no physical evolution or matrix evaluation."""
import argparse, contextlib, hashlib, io, json
from pathlib import Path

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--json',action='store_true');args=p.parse_args()
 root=Path(__file__).resolve().parents[1]
 manifest=root/'outputs/native_mixed_gaussian_transition_2026_09_09_inputs/SOURCE_MANIFEST.json'
 pins=json.loads(manifest.read_text())['inputs']
 for rel,digest in pins.items():
  if hashlib.sha256((root/rel).read_bytes()).hexdigest()!=digest:raise ValueError('source binding: '+rel)
 reports=[]
 for name,count in [('fock',716),('fast',16)]:
  path=root/('scripts/native_mixed_gaussian_transition_2026_09_09_'+name+'.py')
  out=io.StringIO()
  with contextlib.redirect_stdout(out):exec(compile(path.read_bytes(),str(path),'exec'),{'__name__':'__main__','__file__':str(path)})
  row=json.loads(out.getvalue())
  if row['predicates']!=count or row['physical_calls']!=0 or not row['status'].startswith('PASS'):raise ValueError('supporting control result')
  row.pop('seconds',None);row.pop('rss_bytes',None);reports.append(row)
 result={'status':'PASS_SUPPORTING_CONTROLS','claim_status':'conditional-support','physical_calls':0,'controls':reports,'input_hashes':pins,'scope':'Synthetic literal CAR and exact finite arithmetic only; no native overlap or alpha certificate.'}
 print(json.dumps(result,sort_keys=True,indent=2))
if __name__=='__main__':main()
