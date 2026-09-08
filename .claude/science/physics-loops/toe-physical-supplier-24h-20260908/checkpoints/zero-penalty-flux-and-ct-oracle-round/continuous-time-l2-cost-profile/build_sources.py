from pathlib import Path
B=Path(__file__).parent
p=B/'runtime.py';s=p.read_text();s=s.replace("self.g=Geometry(2);base=Path(oracle_dir)","self.g=Geometry(2);base=Path(oracle_dir)\n  expected={'BACKWARD_POWERS.json':'43da459cf1493c30ca0313de27083bf35ae3bdcf96d88143c75e0723af080d2c','ORACLE.json':'d9a99e5c41d6d7ce7b22bdf8ec9fc85175a3fef7c85444dd7c706f81366cf25a'}\n  for name,digest in expected.items():\n   if hashlib.sha256((base/name).read_bytes()).hexdigest()!=digest:raise ValueError('oracle pin '+name)")
p.write_text(s)
