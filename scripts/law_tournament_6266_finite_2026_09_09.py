"""Finite sharp-refinement and signed carrier/source checks for original #6266."""
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
    for path, expected in INPUT_SHA256.items():
        if hashlib.sha256((ROOT/path).read_bytes()).hexdigest() != expected:
            raise RuntimeError('input identity mismatch: '+path)


def main():
    input_guard();results=[]
    def check(label,ok,detail):
        results.append(bool(ok));print(('PASS ' if ok else 'FAIL ')+label+': '+detail)
    good=noncommuting=nonzero=0
    for rotation in m.b64.ROTATIONS:
        p=tuple(m.b63.rotate_hermitian(rotation,x) for x in (m.P0,m.P1))
        e=m.b64.rotated_menus(rotation)[0]
        g=tuple(tuple(m.b63.matrix_multiply(q,f) for f in e) for q in p)
        good += (all(m.b63.psd(a) for row in g for a in row)
                 and all(m.b63.matrix_sum(row)==q for row,q in zip(g,p))
                 and all(m.b63.matrix_add(g[0][h],g[1][h])==e[h] for h in range(3)))
        nonzero += sum(a != m.b63.ZERO_MATRIX for row in g for a in row)
        noncommuting += sum(m.b63.matrix_multiply(q,f) != m.b63.matrix_multiply(f,q)
                           for q in p for f in m.b64.rotated_menus(rotation)[1])
    check('sharp-refinement',good==24 and nonzero==96 and noncommuting==96,
          f'24 frames: valid joint marginals={good}; nonzero menu0 effects={nonzero}; menu1 noncommuting pairs={noncommuting}')
    rho=m.b63.density_at_t(1);hazard=F(3,4)
    live=m.b63.matrix_scale(1-hazard,rho)
    check('additional-registration-contract',m.b63.matrix_trace(live).real==F(1,4)
          and m.b63.matrix_scale(F(4),live)==rho,
          'f=3/4 has a live branch of weight1/4 and unchanged normalized state; f=1 only under no-live-on-this-attempt contract')
    bootstrap=0
    for rotation in m.b64.ROTATIONS:
        for pair in m.PAIRS:
            records=m.candidate_records('adjacent_packet',rotation,pair)
            bootstrap += m.root_site('adjacent_packet',records)==m.b64.ORIGIN and m.geometry('adjacent_packet',records)==(1,0,1)
    check('actual-signed-carriers',bootstrap==96,f'{bootstrap}/96 exact two-carrier roots/heads decoded; all proper frames and four fine outcomes')
    continuation=0;head_edges=[]
    for pair in m.PAIRS:
        records=m.candidate_records('adjacent_packet',m.R0,pair)
        old_head=next(site for site,c in records.items() if m.b64.decode_context(c) is not None)
        out,kinds=m.continue_one(records)
        heads=[(site,m.b64.decode_context(c)) for site,c in out.items() if m.b64.decode_context(c) is not None and m.b64.decode_context(c).role=='head']
        frontier=[site for site,c in heads if m.b64.add(site,c.forward) not in out]
        continuation += (len(out)==5 and kinds==('relay','outcome','finalize')
                         and m.root_site('adjacent_packet',out)==m.b64.ORIGIN
                         and len(frontier)==1 and m.geometry('adjacent_packet',out)==(1,0,1))
        if len(frontier)==1:head_edges.append(tuple(a-b for a,b in zip(frontier[0],old_head)))
    check('finite-head-source',continuation==4 and set(head_edges)=={(-1,0,0),(1,0,0)},
          f'{continuation}/4 canonical one-event continuations; preserved root, old Records, unique head frontier and signed head movement')
    # Incidence is source-minus-target; charge increment is target-minus-source.
    continuity=0;parity=0
    for d in m.b64.DIRECTIONS:
        incidence=np.array([1,-1]);delta=np.array([-1,1]);k=np.array((1,*d))
        continuity += np.array_equal(delta[:,None]*k+incidence[:,None]*k,np.zeros((2,4)))
        tensor=np.outer(k,k);opposite=np.outer(np.array((1,*(-a for a in d))),np.array((1,*(-a for a in d))))
        parity += (np.array_equal(tensor[1:,1:],opposite[1:,1:]) and np.array_equal(tensor[0,1:],-opposite[0,1:]) and -tensor[0,0]+np.trace(tensor[1:,1:])==0)
    check('conditional-incidence-and-tensor',continuity==6 and parity==6,
          'six supplied unit directions; four scaled incidence identities, orientation-even spatial tensor, odd mixed tensor, supplied Minkowski-null normalization')
    print('SCOPE: finite carrier/source algebra only. Literal Cycle713/placement, long histories, 17^3 TT sample and old mutation totals are historical conditional evidence, not replayed.')
    print(f'TOTAL: PASS={sum(results)} FAIL={len(results)-sum(results)}')
    return int(not all(results))


if __name__=='__main__':
    raise SystemExit(main())
