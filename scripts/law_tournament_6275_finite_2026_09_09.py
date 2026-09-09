"""Exact-domain, explicit basis bridge and two supplied Record dictionaries."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import numpy as np
import law_tournament_6266_6275_model as m
import law_tournament_6266_6275_independent_check_2026_09_09 as independent

AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = ('docs/SIGNED_RECORD_FINITE_REFINEMENT_AND_CONDITIONAL_SOURCE_6266_BOUNDED_THEOREM_NOTE_2026-09-09.md', 'docs/RECORD_LAW_EXACT_DOMAIN_AND_CHANNEL_BRIDGE_6275_BOUNDED_THEOREM_NOTE_2026-09-09.md', 'scripts/law_tournament_6266_6275_model.py', 'scripts/admissibility_record_native_state_dependent_born_history_joint_law_candidate_gate_2026_08_12.py', 'scripts/admissibility_strict_nearest_neighbor_state_dependent_record_born_history_single_front_2026_08_12.py', '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_RECORD_NATIVE_STATE_DEPENDENT_BORN_HISTORY_JOINT_LAW_CANDIDATE_GATE_NOTE_2026-08-12.md', '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_STRICT_NEAREST_NEIGHBOR_STATE_DEPENDENT_RECORD_BORN_HISTORY_SINGLE_FRONT_POSITIVE_THEOREM_NOTE_2026-08-12.md', 'docs/ADMISSIBILITY_M2_EFFECT_LABEL_RECORD_CARRIER_ATOMIC_BORN_LAW_FACTORIZATION_BOUNDED_THEOREM_NOTE_2026-08-10.md', 'docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'scripts/law_tournament_6266_6275_independent_check_2026_09_09.py')
INPUT_SHA256 = {'docs/SIGNED_RECORD_FINITE_REFINEMENT_AND_CONDITIONAL_SOURCE_6266_BOUNDED_THEOREM_NOTE_2026-09-09.md': '4923f614fe704b87f54d1549f3f77900ced51d47cb3f2350bb012347741b4aa0', 'docs/RECORD_LAW_EXACT_DOMAIN_AND_CHANNEL_BRIDGE_6275_BOUNDED_THEOREM_NOTE_2026-09-09.md': 'ccf6f8215c5f82898a31d0972d878a7f00ddecef0724fe50ca713ba492242006', 'scripts/law_tournament_6266_6275_model.py': '3e5f858d6e0c37bdb57798fca398883330017b17c26498208a357939d8233077', 'scripts/admissibility_record_native_state_dependent_born_history_joint_law_candidate_gate_2026_08_12.py': '6952a8bf9badcf0a546a024b365d8238376305014ad6755f06db6bfa45fee848', 'scripts/admissibility_strict_nearest_neighbor_state_dependent_record_born_history_single_front_2026_08_12.py': '9e8dafb2f8916340e2131814340518cc64c42d418f78605845c782cef551916a', '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_RECORD_NATIVE_STATE_DEPENDENT_BORN_HISTORY_JOINT_LAW_CANDIDATE_GATE_NOTE_2026-08-12.md': '70c0cbe91e079e20111875b26589556dd21c197ade4638512ecd5070bb3e073e', '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_STRICT_NEAREST_NEIGHBOR_STATE_DEPENDENT_RECORD_BORN_HISTORY_SINGLE_FRONT_POSITIVE_THEOREM_NOTE_2026-08-12.md': 'aec5700bca3f148c67ff27948e045afaa0ca861d7b29ae16608e890c08b89235', 'docs/ADMISSIBILITY_M2_EFFECT_LABEL_RECORD_CARRIER_ATOMIC_BORN_LAW_FACTORIZATION_BOUNDED_THEOREM_NOTE_2026-08-10.md': 'b6b4e25cbdc3b87e5ee8db841b7378e8ea900dee09cf02c993ebb0b823dd4fb4', 'docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md': '1851b00670be98cf4a5f22536ee1f95fd73c7066f5693d4209f43aa439b89ae2', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'scripts/law_tournament_6266_6275_independent_check_2026_09_09.py': '6feaefeae301068fe1c62ecb76a41bdd0e66b397ec67ebffdcfa28a092ad09ed'}
ROOT = Path(__file__).resolve().parents[1]


def input_guard():
    independent.input_guard()
    for path,expected in INPUT_SHA256.items():
        if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=expected:
            raise RuntimeError('input identity mismatch: '+path)


def main():
    input_guard();results=[]
    def check(label,ok,detail):
        results.append(bool(ok));print(('PASS ' if ok else 'FAIL ')+label+': '+detail)
    states=[m.diagonal(tuple(int(i==j) for i in range(4))) for j in range(4)]
    states.append(m.diagonal((F(1,4),)*4))
    zero_cases=valid_cases=0
    for law in m.LAWS:
        for omega in states:
            out=m.distribution(law,omega)
            valid_cases += len(out)==5 and all(o.weight>=0 for o in out) and sum(o.weight for o in out)==1
            zero_cases += any(o.weight==0 for o in out)
    check('exact-normalized-kernels',valid_cases==10 and zero_cases==8,
          f'{valid_cases}/10 exact boundary/mixed-state kernels, {zero_cases} retain legitimate zero-weight branches')
    epsilon=F(1,10**13)
    invalid=[m.diagonal((1+epsilon,0,-epsilon,0)),m.diagonal((1+epsilon,0,0,0)),m.diagonal((0,0,0,0)),((m.ONE,),)]
    refusals=0
    for law in m.LAWS:
        for omega in invalid:
            out=m.distribution(law,omega);refusals += len(out)==1 and out[0].status=='refusal' and out[0].weight==1
        for kw in ({'context_valid':False},{'output_valid':False},{'spent':True},{'rotation':((0,0,0),)*3},
                   {'records':{m.b64.ORIGIN:m.b63.IDENTITY}}):
            out=m.distribution(law,states[0],**kw);refusals += len(out)==1 and out[0].status=='refusal'
    check('fail-closed-domain-and-readiness',refusals==18,f'{refusals}/18 actual malformed density, structural readiness, invalid frame and occupied-target refusals')
    impossible=False
    try:m.realize(m.distribution(m.LAWS[0],states[0]),m.PAIRS[0])
    except ValueError:impossible=True
    check('zero-weight-realization',impossible,'a zero-weight branch is valid in the distribution and unavailable as a realized event')
    residual=m.channel_residual()
    check('same-input-channel-bridge',residual<1e-12,
          f'16 canonical matrix units: no-record + four fine outputs (80 maps) and 48 coarse sums; max residual={residual:.3g}')
    weights_ok=geometry_ok=0
    for rotation in m.b64.ROTATIONS:
        for pair in m.PAIRS:
            for law in m.LAWS:
                packet=m.candidate_records(law,rotation,pair)
                geometry_ok += m.geometry(law,packet)==((1,1,0) if law=='output_root' else (1,0,1))
        w1=m.distribution(m.LAWS[0],states[-1],rotation);w2=m.distribution(m.LAWS[1],states[-1],rotation)
        weights_ok += tuple(o.weight for o in w1)==tuple(o.weight for o in w2)
    check('common-weights-distinct-actual-geometry',weights_ok==24 and geometry_ok==192,
          f'{weights_ok}/24 common exact kernels and {geometry_ok}/192 root-aligned carrier geometry signatures')
    continued=0
    for law in m.LAWS:
        for pair in m.PAIRS:
            records=m.candidate_records(law,m.R0,pair);out,kinds=m.continue_one(records)
            continued += len(out)==5 and m.root_site(law,out)==m.b64.ORIGIN and m.geometry(law,out)==((1,1,0) if law=='output_root' else (1,0,1))
    check('finite-common-continuation',continued==8,f'{continued}/8 canonical three-write continuations preserve original roots and signatures')
    print('SCOPE: two supplied dictionaries distinguished under a common geometric decoder; no unrestricted-recoding or full physical-axiom nonselection theorem.')
    print(f'TOTAL: PASS={sum(results)} FAIL={len(results)-sum(results)}')
    return int(not all(results))


if __name__=='__main__':
    raise SystemExit(main())
