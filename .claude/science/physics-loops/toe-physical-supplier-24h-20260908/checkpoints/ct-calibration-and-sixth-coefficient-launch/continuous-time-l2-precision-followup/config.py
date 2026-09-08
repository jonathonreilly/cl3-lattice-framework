from pathlib import Path
B=Path(__file__).resolve().parent
ARMS=[dict(arm=i,T=T,start=s,burn=64) for i,(T,s) in enumerate((T,s) for T in (.5,2.) for s in ('constant','bounded'))]
CHAINS=64;MEASURED=256;FACES=24;BATCHES=16;SHARD=4
SEED_BASE=202609360000
MICRO_LEDGER=180.930914
def seed(a,c):return SEED_BASE+1000*a+c
