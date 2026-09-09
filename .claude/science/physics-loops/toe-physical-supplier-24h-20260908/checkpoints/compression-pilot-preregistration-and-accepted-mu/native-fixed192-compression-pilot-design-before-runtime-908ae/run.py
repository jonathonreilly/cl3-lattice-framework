"""Source-only readiness; physical mode deliberately absent pending review."""
import argparse,ast,hashlib,json,sys
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--readiness',action='store_true',required=True);p.parse_args()
 if not(sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode):raise ValueError('require -I -B -S')
 base=Path(__file__).resolve().parent;freeze=json.loads((base/'SOURCE_AST_FREEZE.json').read_text())
 for name,digest in freeze['files'].items():
  data=(base/name).read_bytes()
  if hashlib.sha256(data).hexdigest()!=digest:raise ValueError('source '+name)
  if name.endswith('.py'):ast.parse(data,filename=str(base/name))
 print(json.dumps({'status':'SOURCE_ONLY_NOT_READY_FOR_NATIVE_EXECUTION','native_calls':0,'runtime_membership_checked':False,'source_files':len(freeze['files'])}))
if __name__=='__main__':main()
