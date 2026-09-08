from pathlib import Path
B=Path(__file__).resolve().parent
ARMS=[dict(arm=i,T=T,start=s,burn=b) for i,(T,s,b) in enumerate((T,s,b) for T in (.5,2.) for s in ('constant','bounded') for b in (16,64))]
CHAINS=16;MEASURED=128;FACES=24;BATCHES=16;SHARD=4
SEED_BASE=202609350000
MICRO_LEDGER=.6609131669974886

def seed(a,c):return SEED_BASE+1000*a+c
