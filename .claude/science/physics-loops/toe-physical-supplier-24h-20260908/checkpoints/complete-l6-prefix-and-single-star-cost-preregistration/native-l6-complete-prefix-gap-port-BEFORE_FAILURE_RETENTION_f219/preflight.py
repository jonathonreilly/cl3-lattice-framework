"""Import-only readiness controls. Never calls baseline or gap."""
from pathlib import Path
import importlib.util,json
P=Path(__file__).resolve().parent
def load(n):
 s=importlib.util.spec_from_file_location(n,P/(n+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def main():
 v=load('verify');f=v.verify();load('replay_core');load('run');v.verify_loaded(f)
 print(json.dumps({'status':'PASS','no_baseline_or_gap_calls':True,'scope':'import and hash closure only'}))
if __name__=='__main__':main()
