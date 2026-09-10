"""Inert streaming assembly worker; lifecycle and pin guards are supplied by dispatcher."""
from pathlib import Path
from fractions import Fraction
import json,os,time

def encode(x):
    if type(x) is Fraction:return str(x)
    raise TypeError('unsupported serialized type '+type(x).__name__)

def save(path,x):
    # Atomic snapshots complement the append-only durable event stream.
    path=Path(path);tmp=path.with_name(path.name+'.tmp')
    with tmp.open('w') as f:
        json.dump(x,f,default=encode,sort_keys=True);f.write('\n');f.flush();os.fsync(f.fileno())
    os.replace(tmp,path)

def run(out,binding,core,binder,guard):
    out=Path(out);start=time.monotonic();seq=0;current={'stage':'setup'};completed=0
    try:
        def retain(stage,payload):
            nonlocal seq,current,completed
            # Serialize immediately: never keep references to mutable callback payloads.
            current={'stage':stage,'seq':seq}
            event={'seq':seq,'stage':stage,'payload':payload}
            with (out/'EVENTS.ndjson').open('a') as f:
                f.write(json.dumps(event,default=encode,sort_keys=True)+'\n');f.flush();os.fsync(f.fileno())
            seq+=1
            if stage=='node_operator':completed+=1
            save(out/'PARTIAL.json',{'current':current,'events':seq,'coefficient_blocks':completed,'seconds':time.monotonic()-start})
            guard()
        retain('start',{'scope':'NEW_A_ONLY_PHYSICAL_COLUMN_COEFFICIENTS','acquisition_binding':binding['identity']})
        rows=binder.load(binding,retain)
        pi_box=core.reciprocal_pi_box();retain('reciprocal_pi',{'interval':pi_box,'terms':[40,12]})
        ledger=core.assemble(rows,pi_box,retain)
        if completed!=756:raise ValueError('fixed coefficient block census')
        result={'status':'CERTIFIED_DESCRIPTOR_OPERATOR_INPUT_BOUND','scope':'physical-column operator only; no Gram or Gaussian consumer',
                'nodes':378,'classes':['P','O'],'coefficient_blocks':756,'ledger':ledger,
                'binding':binding['identity'],'native_oracle_calls':0,'physical_columns_evaluated':False,
                'gaussian_consumer_certified':False,'events':seq+1,'seconds':time.monotonic()-start}
        retain('complete',result);save(out/'RESULT.json',result)
        guard()
    except BaseException as exc:
        try:save(out/'FAILURE.json',{'error':repr(exc),'current':current,'events':seq,'coefficient_blocks':completed,'seconds':time.monotonic()-start})
        except BaseException as secondary:exc.add_note('worker retention: '+repr(secondary))
        raise
