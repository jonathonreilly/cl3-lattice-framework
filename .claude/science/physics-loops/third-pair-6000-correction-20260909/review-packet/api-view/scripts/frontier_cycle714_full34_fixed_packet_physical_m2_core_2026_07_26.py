#!/usr/bin/env python3
"""Cycle714 full-width fixed-address causal-packet physical-M2 core.

The fixed circuit appends one supplied blank Cycle704/Cycle610 packet cell
under supplied local control bits.  Its circuit ordinal is not physical time,
and reversibility is not Record permanence or realized occurrence.
"""
from __future__ import annotations
import ast
from dataclasses import dataclass
from hashlib import sha256
import json, math, subprocess, sys
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))

AUDIT_TIMEOUT_SEC = 300
NOTE_PATH = (
    "docs/PHYSICAL_M2_FULL34_FIXED_PACKET_COMPOSITION_"
    "CYCLE714_BOUNDED_THEOREM_NOTE_2026-07-26.md"
)
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_M2_FULL34_FIXED_PACKET_COMPOSITION_CYCLE714_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "scripts/frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26.py",
    "scripts/frontier_cycle714_fixed_packet_coherent_composition_check_2026_07_26.py",
    "scripts/frontier_cycle714_full34_fixed_packet_independent_route_replay_2026_07_26.py",
    "docs/PHYSICAL_M2_ENDPOINT_INSTRUMENT_CYCLE704_CYCLE612_BRIDGE_"
    "CYCLE713_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/JOINT_TWO_CELL_FULL_UPDATE_PHYSICAL_M2_COMPILER_"
    "CYCLE712_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/work_history/repo/review_feedback/"
    "CYCLE704_LOCAL_GAUSS_CYCLE612_ENDPOINT_BRIDGE_NOTE_2026-07-25.md",
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_INTRINSIC_TICK_EVENT_RELATIONAL_DURATION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md",
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_TICK_ECHO_ASSOCIATION_CAUSAL_ORDER_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md",
    "scripts/frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py",
    "scripts/frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25.py",
    "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py",
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py",
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py",
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py",
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py",
    "scripts/frontier_cycle703_local_gauss_reference_adversary_2026_07_25.py",
    "scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py",
    "scripts/frontier_cycle708_cube_basis_gauge_core_2026_07_26.py",
    "scripts/frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py",
    "scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py",
    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
DYNAMIC_REPO_SCRIPT_PATHS = (
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py",
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py",
)
import frontier_cycle709_local_seam_physical_core_2026_07_26 as P
import frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25 as C704

BASELINE = "ebd05531036b844883e2e73186ebd95c46ffc119"

def digest(path):return sha256(Path(path).read_bytes()).hexdigest()

def transitive_repo_script_paths(start=None):
    scripts_dir=ROOT/'scripts';module_paths={path.stem:path for path in scripts_dir.glob('*.py')}
    pending=[Path(start or __file__).resolve()];seen=set()
    while pending:
        path=pending.pop()
        if path in seen:continue
        seen.add(path);tree=ast.parse(path.read_text(),filename=str(path));imports=[]
        for node in ast.walk(tree):
            if isinstance(node,ast.Import):imports.extend(alias.name.split('.')[0] for alias in node.names)
            elif isinstance(node,ast.ImportFrom) and node.module:imports.append(node.module.split('.')[0])
        pending.extend(module_paths[name] for name in imports if name in module_paths and module_paths[name] not in seen)
    return tuple(sorted(path.relative_to(ROOT).as_posix() for path in seen))

def provenance_certificate(declared_paths=AUDIT_INPUT_PATHS,start=None):
    scripts=transitive_repo_script_paths(start)
    declared_labels=set(declared_paths)
    missing=tuple(path for path in scripts if path not in declared_labels)
    missing_dynamic=tuple(
        path for path in DYNAMIC_REPO_SCRIPT_PATHS if path not in declared_labels
    )
    declared=tuple((ROOT/path).resolve() for path in declared_paths)
    head=subprocess.check_output(('git','rev-parse','HEAD'),cwd=ROOT,text=True).strip()
    ancestor=subprocess.run(('git','merge-base','--is-ancestor',BASELINE,head),cwd=ROOT,check=False).returncode==0
    tracked=tuple(
        path for path in set(declared_paths)|set(scripts)
        if subprocess.run(('git','ls-files','--error-unmatch','--',path),cwd=ROOT,
            stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,check=False).returncode!=0
    )
    inventory=tuple(sorted(set(declared_paths)|set(scripts)))
    return {
      'baseline_commit':BASELINE,'actual_HEAD':head,'baseline_is_ancestor':ancestor,
      'declared_path_failures':sum(not path.is_file() or not path.is_relative_to(ROOT) for path in declared),
      'duplicate_declared_paths':len(declared)-len(set(declared)),
      'transitive_repo_scripts':scripts,'missing_transitive_scripts':missing,
      'dynamic_repo_scripts':DYNAMIC_REPO_SCRIPT_PATHS,
      'missing_dynamic_scripts':missing_dynamic,
      'untracked_inputs':tracked,
      'source_inventory_sha256':{path:digest(ROOT/path) for path in inventory if (ROOT/path).is_file()},
    }

X=np.array([[0,1],[1,0]],complex); H=np.array([[1,1],[1,-1]],complex)/np.sqrt(2)
T=np.diag([1,np.exp(1j*np.pi/4)]); TD=T.conj().T
# Little-endian local basis: tuple operand 0 is control, operand 1 target.
CNOT=np.array([[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]],complex)

@dataclass(frozen=True)
class G:
    kind:str; q:tuple[int,...]

PRED=tuple(range(0,6)); RB=tuple(range(6,10)); RA=tuple(range(10,14)); CARRY=14
PDELTA=tuple(range(15,27)); PEND,PBIND,PVALID,PORIENT,PACT,PADM,PLAW=range(27,34)
HEAD=tuple(range(34,40)); ROT=tuple(range(40,44))
POINTER,BINDER,ACTUAL,ADMISS,LAW,FRESH,ORIENT=range(44,51)
ENABLE_WORK=tuple(range(51,56)); MCX_WORK=tuple(range(56,59)); N=59
SENTINEL_NONE=63; FIXED_ADDRESS=23

def tof(a,b,t): return G('TOF',(a,b,t))
def cn(a,b): return G('CNOT',(a,b))

def mcx(controls,target,work=MCX_WORK):
    controls=tuple(controls)
    if len(controls)==1:return [cn(controls[0],target)]
    if len(controls)==2:return [tof(*controls,target)]
    need=len(controls)-2; anc=work[:need]; out=[tof(controls[0],controls[1],anc[0])]
    for i in range(2,len(controls)-1): out.append(tof(anc[i-2],controls[i],anc[i-1]))
    out.append(tof(anc[-1],controls[-1],target))
    for i in reversed(range(2,len(controls)-1)): out.append(tof(anc[i-2],controls[i],anc[i-1]))
    out.append(tof(controls[0],controls[1],anc[0])); return out

def word():
    w=[]; c=(POINTER,BINDER,ACTUAL,ADMISS,LAW,FRESH)
    w += [tof(c[0],c[1],ENABLE_WORK[0])]
    for i in range(2,6): w += [tof(ENABLE_WORK[i-2],c[i],ENABLE_WORK[i-1])]
    e=ENABLE_WORK[-1]
    for h,p in zip(HEAD,PRED): w += [tof(e,h,p)]
    for r,b in zip(ROT,RB): w += [tof(e,r,b)]
    w += mcx((e,)+ROT,CARRY)
    w += mcx((e,ROT[0],ROT[1],ROT[2]),ROT[3])
    w += mcx((e,ROT[0],ROT[1]),ROT[2])
    w += [tof(e,ROT[0],ROT[1]),cn(e,ROT[0])]
    for r,a in zip(ROT,RA): w += [tof(e,r,a)]
    # The fixed seam changes exactly matter modes 1 and 6 whenever admitted.
    # Hence its Cycle704 delta mask is the literal constant 2**1+2**6=66.
    w += [cn(e,PDELTA[1]),cn(e,PDELTA[6])]
    for target in (PEND,PBIND,PVALID,PACT,PADM,PLAW): w += [cn(e,target)]
    w += [tof(e,ORIENT,PORIENT)]
    for h,p in zip(HEAD,PRED): w += [tof(e,p,h)]
    for bit,h in enumerate(HEAD):
        if (FIXED_ADDRESS>>bit)&1:w += [cn(e,h)]
    for i in reversed(range(2,6)): w += [tof(ENABLE_WORK[i-2],c[i],ENABLE_WORK[i-1])]
    w += [tof(c[0],c[1],ENABLE_WORK[0])]
    return tuple(w)

def apply_semantic(bits,w):
    b=list(bits)
    for g in w:
        if g.kind=='CNOT': b[g.q[1]] ^= b[g.q[0]]
        else: b[g.q[2]] ^= b[g.q[0]] & b[g.q[1]]
    return tuple(b)

def initial(rotor,head,orientation,controls=(1,1,1,1,1,1)):
    b=[0]*N
    for i,q in enumerate(HEAD):b[q]=(head>>i)&1
    for i,q in enumerate(ROT):b[q]=(rotor>>i)&1
    for q,v in zip((POINTER,BINDER,ACTUAL,ADMISS,LAW,FRESH),controls):b[q]=v
    b[ORIENT]=orientation
    return tuple(b)

def integer(bits,qs):return sum(bits[q]<<i for i,q in enumerate(qs))

def independent_expected(before):
    """Independent field equation for the declared blank-packet domain."""
    controls=(POINTER,BINDER,ACTUAL,ADMISS,LAW,FRESH)
    if not all(before[q] for q in controls):
        return before
    after=list(before)
    rotor=integer(before,ROT);head=integer(before,HEAD)
    for i,q in enumerate(PRED):after[q]=(head>>i)&1
    for i,q in enumerate(RB):after[q]=(rotor>>i)&1
    next_rotor=(rotor+1)%16
    for i,q in enumerate(RA):after[q]=(next_rotor>>i)&1
    after[CARRY]=int(rotor==15)
    after[PDELTA[1]]=after[PDELTA[6]]=1
    for q in (PEND,PBIND,PVALID,PACT,PADM,PLAW):after[q]=1
    after[PORIENT]=before[ORIENT]
    for i,q in enumerate(HEAD):after[q]=(FIXED_ADDRESS>>i)&1
    for i,q in enumerate(ROT):after[q]=(next_rotor>>i)&1
    return tuple(after)

def toffoli_primitives(a,b,t):
    # Exact 15-gate Clifford+T decomposition.
    return [('H',(t,)),('CNOT',(b,t)),('TD',(t,)),('CNOT',(a,t)),('T',(t,)),
            ('CNOT',(b,t)),('TD',(t,)),('CNOT',(a,t)),('T',(b,)),('T',(t,)),
            ('H',(t,)),('CNOT',(a,b)),('T',(a,)),('TD',(b,)),('CNOT',(a,b))]

def expanded(w):
    out=[]
    for g in w:
        out += [('CNOT',g.q)] if g.kind=='CNOT' else toffoli_primitives(*g.q)
    return tuple(out)

def apply_small(state,matrix,wires,n):
    out=np.zeros_like(state)
    for s,v in enumerate(state):
        local=sum(((s>>q)&1)<<i for i,q in enumerate(wires))
        for t in range(1<<len(wires)):
            amp=matrix[t,local]
            if abs(amp):
                target=s
                for i,q in enumerate(wires): target=(target&~(1<<q))|(((t>>i)&1)<<q)
                out[target]+=amp*v
    return out

def toffoli_residual():
    mats={'H':H,'T':T,'TD':TD,'CNOT':CNOT}; observed=np.eye(8,dtype=complex)
    for kind,qs in toffoli_primitives(0,1,2):
        cols=[]
        for col in range(8): cols.append(apply_small(observed[:,col],mats[kind],qs,3))
        observed=np.column_stack(cols)
    expected=np.eye(8,dtype=complex)
    expected[:,]=0
    for s in range(8): expected[s^(((s&1)&((s>>1)&1))<<2),s]=1
    return float(np.linalg.norm(observed-expected))

def sparse_apply(state,gates):
    mats={'H':H,'T':T,'TD':TD,'CNOT':CNOT}
    current=dict(state)
    for kind,wires in gates:
        matrix=mats[kind];updated={}
        for basis,amplitude in current.items():
            local=sum(((basis>>q)&1)<<i for i,q in enumerate(wires))
            for target_local in range(1<<len(wires)):
                coefficient=matrix[target_local,local]
                if abs(coefficient)<1e-15:continue
                target=basis
                for i,q in enumerate(wires):
                    target=(target&~(1<<q))|(((target_local>>i)&1)<<q)
                updated[target]=updated.get(target,0)+coefficient*amplitude
        current={key:value for key,value in updated.items() if abs(value)>1e-13}
    return current

def bits_to_int(bits):return sum(value<<q for q,value in enumerate(bits))

def sparse_expected(state,w):
    output={}
    for basis,amplitude in state.items():
        bits=tuple((basis>>q)&1 for q in range(N))
        target=bits_to_int(apply_semantic(bits,w))
        output[target]=output.get(target,0)+amplitude
    return output

def sparse_distance(left,right):
    keys=set(left)|set(right)
    if not keys:return 0.0,0.0
    delta=np.array([left.get(key,0)-right.get(key,0) for key in keys])
    return float(np.max(np.abs(delta))),float(np.linalg.norm(delta))

def coherent_packet_suite(w,inv):
    states=[]
    phase=lambda k:np.exp(1j*k*np.pi/11)
    for missing in range(6):
        full=bits_to_int(initial(15,63,1))
        controls=[1]*6;controls[missing]=0
        absent=bits_to_int(initial(15,63,1,tuple(controls)))
        states.append({full:1/np.sqrt(2),absent:phase(missing+1)/np.sqrt(2)})
    states.append({
        bits_to_int(initial(15,0,1)):1/np.sqrt(2),
        bits_to_int(initial(15,63,1)):phase(7)/np.sqrt(2),
    })
    states.append({
        bits_to_int(initial(0,63,1)):1/np.sqrt(3),
        bits_to_int(initial(7,63,1)):phase(8)/np.sqrt(3),
        bits_to_int(initial(15,63,1)):phase(16)/np.sqrt(3),
    })
    states.append({
        bits_to_int(initial(15,63,0)):1/np.sqrt(2),
        bits_to_int(initial(15,63,1)):phase(9)/np.sqrt(2),
    })
    maximum_component=maximum_norm=maximum_inverse_component=maximum_inverse_norm=0.0
    for state in states:
        observed=sparse_apply(state,expanded(w))
        expected=sparse_expected(state,w)
        component,norm=sparse_distance(observed,expected)
        maximum_component=max(maximum_component,component);maximum_norm=max(maximum_norm,norm)
        restored=sparse_apply(observed,expanded(inv))
        component,norm=sparse_distance(restored,state)
        maximum_inverse_component=max(maximum_inverse_component,component)
        maximum_inverse_norm=max(maximum_inverse_norm,norm)
    return {
      'states':len(states),'maximum_component_residual':maximum_component,
      'maximum_norm_residual':maximum_norm,
      'maximum_inverse_component_residual':maximum_inverse_component,
      'maximum_inverse_norm_residual':maximum_inverse_norm,
    }

def fermionic_seam_certificate():
    fswap=np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,-1]],complex)
    expected=fswap.copy()
    schedule=tuple((wire,wire+1) for wire in range(1,6))+tuple(
        reversed(tuple((wire,wire+1) for wire in range(1,5)))
    )
    target_failures=sign_failures=swap_substitution_signed_matches=0
    for source in range(1<<12):
        target=source;sign=1
        for left,right in schedule:
            a=(target>>left)&1;b=(target>>right)&1
            if a and b:sign=-sign
            if a!=b:target^=(1<<left)|(1<<right)
        permutation=list(range(12));permutation[1],permutation[6]=6,1
        occupied=[mode for mode in range(12) if (source>>mode)&1]
        mapped=[permutation[mode] for mode in occupied]
        inversion=sum(mapped[i]>mapped[j] for i in range(len(mapped)) for j in range(i+1,len(mapped)))
        independent_sign=-1 if inversion&1 else 1
        independent_target=sum(1<<permutation[mode] for mode in occupied)
        target_failures+=target!=independent_target
        sign_failures+=sign!=independent_sign
        swap_substitution_signed_matches+=independent_sign==1
    state=np.array([1,0,0,1],complex)/np.sqrt(2)
    coherent=fswap@state
    coherent_expected=np.array([1,0,0,-1],complex)/np.sqrt(2)
    plain_swap=fswap.copy();plain_swap[3,3]=1
    return {
      'FSWAP_matrix_residual':float(np.linalg.norm(fswap-expected)),
      'schedule_rows':1<<12,'target_failures':target_failures,
      'sign_failures':sign_failures,
      'plain_SWAP_signed_row_mismatches':(1<<12)-swap_substitution_signed_matches,
      'coherent_00_plus_11_residual':float(np.linalg.norm(coherent-coherent_expected)),
      'plain_SWAP_coherent_residual':float(np.linalg.norm(plain_swap@state-coherent_expected)),
    }

def carriers_for(eq,graph,site_map,gauges):
    lookup={P.c707_edge_key(graph,e):e for e in range(len(graph.edges))}
    carriers=[]
    for edge in range(len(eq.patch_graph.edges)):
        carriers.append(tuple(site_map[lookup[P.C.G.c706.edge_key(eq.patch_graph,edge)]]))
    carriers.extend((site,) for site in P.rail_sites(eq,graph,gauges))
    return tuple(carriers)

def retained_endpoint_sites(eq,graph,site_map,gauges,matter_sites):
    carriers=carriers_for(eq,graph,site_map,gauges)
    wire_sites=tuple(row[0] for row in carriers)
    left_site,right_site=wire_sites[1],wire_sites[6]
    candidates=[]
    occupied=set(matter_sites)
    for x in range(min(left_site[0],right_site[0])-2,max(left_site[0],right_site[0])+3):
      for y in range(min(left_site[1],right_site[1])-2,max(left_site[1],right_site[1])+3):
       for z in range(min(left_site[2],right_site[2])-2,max(left_site[2],right_site[2])+3):
        site=(x,y,z)
        if site in occupied:continue
        dl=sum(abs(site[i]-left_site[i]) for i in range(3));dr=sum(abs(site[i]-right_site[i]) for i in range(3))
        candidates.append((max(dl,dr),dl+dr,site))
    return tuple(row[2] for row in sorted(candidates)[:3]) # du,dv,retained pointer

def main():
    w=word(); inv=tuple(reversed(w)); failures=inverse=work=carry=projection=0; cases=0
    coherent=coherent_packet_suite(w,inv);fermionic=fermionic_seam_certificate()
    schema_failures=cycle610_projection_failures=sentinel_failures=0
    heads=(SENTINEL_NONE,0,7,23,31)
    for r in range(16):
      for o in (0,1):
       for h in heads:
        before=initial(r,h,o); after=apply_semantic(before,w); back=apply_semantic(after,inv); cases+=1
        failures += integer(after,HEAD)!=FIXED_ADDRESS or integer(after,PRED)!=h
        failures += integer(after,RB)!=r or integer(after,RA)!=(r+1)%16
        carry += after[CARRY] != int(r==15)
        projection += not (after[PVALID] and after[PEND] and after[PBIND])
        predecessor=None if integer(after,PRED)==SENTINEL_NONE else integer(after,PRED)
        packet=C704.IntervalPacket(identity=FIXED_ADDRESS,predecessor=predecessor,
          rotor_before=integer(after,RB),rotor=integer(after,RA),carry=after[CARRY],
          delta_mask=integer(after,PDELTA),endpoint=after[PEND],binder=after[PBIND],
          valid=after[PVALID],orientation=2*after[PORIENT]-1,actuality=after[PACT],
          admissibility=after[PADM],law_domain=after[PLAW])
        expected_packet={
          'identity':FIXED_ADDRESS,
          'predecessor':None if h==SENTINEL_NONE else h,
          'rotor_before':r,'rotor':(r+1)%16,'carry':int(r==15),
          'delta_mask':66,'endpoint':1,'binder':1,'valid':1,
          'orientation':1 if o else -1,'actuality':1,'admissibility':1,
          'law_domain':1,
        }
        schema_failures += sum(getattr(packet,key)!=value for key,value in expected_packet.items())
        cell=C704.C610.EventCell(identity=packet.identity,rotor=packet.rotor,
          carry=packet.carry,predecessor=packet.predecessor,binder=packet.binder,
          valid=packet.valid,orientation=packet.orientation)
        cycle610_projection_failures += cell.orientation!=(1 if o else -1) or cell.predecessor!=packet.predecessor
        if h==SENTINEL_NONE: sentinel_failures += packet.predecessor is not None
        inverse += back!=before
        work += any(after[q] for q in ENABLE_WORK+MCX_WORK)
    refused=inverse_refused=0
    for missing in range(6):
      c=[1]*6;c[missing]=0; before=initial(5,7,1,tuple(c));after=apply_semantic(before,w)
      refused += after!=before; inverse_refused += apply_semantic(after,inv)!=before
    input_deletion={}
    derived_surface=tuple(range(34))+HEAD+ROT
    for missing,name in enumerate(('pointer','binder','actuality','admissibility','law_domain','fresh')):
      changed=0
      for r in range(16):
       for o in (0,1):
        base=apply_semantic(initial(r,SENTINEL_NONE,o),w)
        c=[1]*6;c[missing]=0
        deleted=apply_semantic(initial(r,SENTINEL_NONE,o,tuple(c)),w)
        changed += tuple(deleted[q] for q in derived_surface)!=tuple(base[q] for q in derived_surface)
      input_deletion[name]=changed
    exhaustive_control_cases=exhaustive_equation_failures=0
    exhaustive_inverse_failures=exhaustive_work_failures=0
    admitted_exhaustive=refused_exhaustive=0
    for r in range(16):
     for h in range(64):
      for o in (0,1):
       for pattern in range(64):
        controls=tuple((pattern>>i)&1 for i in range(6))
        before=initial(r,h,o,controls)
        after=apply_semantic(before,w)
        expected=independent_expected(before)
        exhaustive_control_cases+=1
        admitted_exhaustive+=pattern==63
        refused_exhaustive+=pattern!=63
        exhaustive_equation_failures+=after!=expected
        exhaustive_inverse_failures+=apply_semantic(after,inv)!=before
        exhaustive_work_failures+=any(after[q] for q in ENABLE_WORK+MCX_WORK)
    rng=np.random.default_rng(714)
    arbitrary_inverse_cases=256;arbitrary_inverse_failures=0
    for _ in range(arbitrary_inverse_cases):
      before=tuple(int(value) for value in rng.integers(0,2,size=N))
      arbitrary_inverse_failures+=apply_semantic(apply_semantic(before,w),inv)!=before
    deletion={}
    selectors={
      'enable_first':lambda i,g:i==0,
      'pred_first':lambda i,g:g.q[-1]==PRED[0],
      'carry_first':lambda i,g:g.q[-1]==CARRY,
      'increment_lsb':lambda i,g:g==cn(ENABLE_WORK[-1],ROT[0]),
      'delta_bit_1':lambda i,g:g.q[-1]==PDELTA[1],
      'delta_bit_6':lambda i,g:g.q[-1]==PDELTA[6],
      'orientation':lambda i,g:g.q[-1]==PORIENT,
    }
    for label,selector in selectors.items():
      index=next(i for i,g in enumerate(w) if selector(i,g))
      damaged=w[:index]+w[index+1:]
      deletion[label]=sum(apply_semantic(initial(r,7,o),damaged)!=apply_semantic(initial(r,7,o),w) for r in range(16) for o in (0,1))
    e=ENABLE_WORK[-1]
    representative={
      'predecessor_write':tof(e,HEAD[0],PRED[0]),
      'rotor_before_write':tof(e,ROT[0],RB[0]),
      'rotor_after_write':tof(e,ROT[0],RA[0]),
      'delta_write':cn(e,PDELTA[1]),
      'endpoint_write':cn(e,PEND),'binder_write':cn(e,PBIND),
      'valid_write':cn(e,PVALID),'actuality_write':cn(e,PACT),
      'admissibility_write':cn(e,PADM),'law_domain_write':cn(e,PLAW),
      'orientation_write':tof(e,ORIENT,PORIENT),
      'head_swap':tof(e,PRED[0],HEAD[0]),
      'head_address_write':cn(e,HEAD[0]),
    }
    independent_field_deletions={}
    for label,gate in representative.items():
      index=next(i for i,candidate in enumerate(w) if candidate==gate)
      damaged=w[:index]+w[index+1:]
      mismatches=0
      for r in range(16):
       for h in (0,7,23,31,63):
        for o in (0,1):
         before=initial(r,h,o);expected=independent_expected(before)
         mismatches+=apply_semantic(before,damaged)!=expected
      independent_field_deletions[label]=mismatches
    # Literal physical placement/routing of every expanded one/two-site gate.
    eq,graph,sm,gauges,matter_sites,coll=P.placement_bundle(((0,0,0),(1,0,0)))
    endpoint_sites=retained_endpoint_sites(eq,graph,sm,gauges,matter_sites)
    du_site,dv_site,pointer_site=endpoint_sites
    occupied=set(matter_sites)|set(endpoint_sites); candidates=[]
    for radius in range(1,12):
      for x in range(-radius,radius+1):
       for y in range(-radius,radius+1):
        for z in range(-radius,radius+1):
         q=(x,y,z)
         if max(abs(x),abs(y),abs(z))==radius and q not in occupied and q not in candidates:candidates.append(q)
         if len(candidates)>=N:break
        if len(candidates)>=N:break
       if len(candidates)>=N:break
      if len(candidates)>=N:break
    new_sites=iter(candidates)
    sites=tuple(pointer_site if q==POINTER else next(new_sites) for q in range(N))
    mats={'H':H,'T':T,'TD':TD,'CNOT':CNOT}
    instructions=tuple(P.c707.Instruction('packet_'+k,tuple(sites[q] for q in qs),mats[k]) for k,qs in expanded(w))
    routed,rr=P.c707.route_word(instructions)
    inverse_instructions=tuple(P.c707.Instruction('unpacket_'+k,tuple(sites[q] for q in qs),mats[k]) for k,qs in expanded(inv))
    inverse_routed,irr=P.c707.route_word(inverse_instructions)
    assigned=set(matter_sites)|set(endpoint_sites)|set(sites)
    touched=set(rr['touched_coordinates'])|set(irr['touched_coordinates'])
    provenance=provenance_certificate()
    source_closure=(provenance['baseline_is_ancestor'] and
      provenance['declared_path_failures']==provenance['duplicate_declared_paths']==0 and
      not provenance['missing_transitive_scripts'] and
      not provenance['missing_dynamic_scripts'] and
      not provenance['untracked_inputs'])
    report={'baseline':BASELINE,'fixed_address':FIXED_ADDRESS,
      'source_closure':source_closure,'provenance':provenance,'declared_inputs':AUDIT_INPUT_PATHS,
      'head_none_sentinel':SENTINEL_NONE,'abstract_packet_interface_M2':N,'new_packet_M2':N-1,
      'matter_M2':len(matter_sites),'cleaned_du_dv_M2':2,'retained_pointer_M2':1,
      'retained_pointer_site':pointer_site,'cleaned_du_dv_sites':(du_site,dv_site),
      'combined_assigned_M2':len(assigned),'placement_collisions':coll+len(assigned)-(len(matter_sites)+len(endpoint_sites)+N-1),
      'touched_M2_union':len(touched),'blank_route_work_M2_union':len(touched-assigned),
      'semantic_gates':len(w),'expanded_one_two_M2_gates':len(instructions),'routed_gates':len(routed),
      'maximum_route_distance':rr['maximum_route_distance'],'non_NN_failures':rr['non_NN_failures'],
      'operand_order_failures':rr['operand_order_failures'],'route_return_failures':rr['route_return_failures'],
      'routed_word_sha256':rr['word_sha256'],'toffoli_decomposition_residual':toffoli_residual(),
      'unappend_expanded_gates':len(inverse_instructions),'unappend_routed_gates':len(inverse_routed),
      'unappend_maximum_route_distance':irr['maximum_route_distance'],
      'unappend_non_NN_failures':irr['non_NN_failures'],'unappend_operand_order_failures':irr['operand_order_failures'],
      'unappend_route_return_failures':irr['route_return_failures'],'unappend_routed_word_sha256':irr['word_sha256'],
      'admitted_cases':cases,'admitted_field_failures':failures,'carry_failures':carry,'projection_failures':projection,
      'Cycle704_IntervalPacket_schema_failures':schema_failures,
      'Cycle704_positive_fields_checked':('identity','predecessor','rotor_before','rotor','carry','delta_mask','endpoint','binder','valid','orientation','actuality','admissibility','law_domain'),
      'Cycle610_EventCell_projection_failures':cycle610_projection_failures,
      'None_sentinel_projection_failures':sentinel_failures,
      'orientation_encoding':'0 -> -1, 1 -> +1',
      'inverse_failures':inverse,'work_return_failures':work,'refused_cases':6,'refused_mutation_failures':refused,
      'refused_inverse_failures':inverse_refused,'deletion_difference_counts':deletion,
      'input_deletion_difference_counts':input_deletion,
      'independent_field_deletion_difference_counts':independent_field_deletions,
      'input_deletion_compared_surface':'packet payload34 + updated head6 + global rotor4 only; altered supplied controls excluded',
      'exhaustive_control_cases':exhaustive_control_cases,
      'exhaustive_admitted_cases':admitted_exhaustive,
      'exhaustive_refused_cases':refused_exhaustive,
      'exhaustive_independent_equation_failures':exhaustive_equation_failures,
      'exhaustive_inverse_failures':exhaustive_inverse_failures,
      'exhaustive_work_return_failures':exhaustive_work_failures,
      'arbitrary_full_register_inverse_cases':arbitrary_inverse_cases,
      'arbitrary_full_register_inverse_failures':arbitrary_inverse_failures,
      'coherent_packet_suite':coherent,
      'fermionic_seam_certificate':fermionic,
      'payload_bits':34,'head_bits':6,'global_rotor_bits':4,'delta_input_bits':0,
      'fixed_seam_delta_mask':66,'supplied_control_bits':7,
      'clean_work_bits':8,'supplied':['fixed selected blank packet cell','fresh bit','fixed address 23','blank payload/work','head and rotor input','derived Cycle713 pointer on the identical retained-pointer coordinate','binder','actuality','admissibility','law-domain','orientation','gate word and route workspace'],
      'projection':'payload maps directly to Cycle704 IntervalPacket/Cycle610 EventCell; rotor difference and K16 carry retain unchanged integer interval semantics; no empirical unit supplied'}
    checks={
      'source_closure':source_closure,
      'full34_schema':len(PRED)==len(HEAD)==6 and len(PDELTA)==12 and report['payload_bits']==34,
      'independent_clean_domain':exhaustive_control_cases==131072
        and admitted_exhaustive==2048 and refused_exhaustive==129024
        and exhaustive_equation_failures==exhaustive_inverse_failures==exhaustive_work_failures==0,
      'arbitrary_full_register_inverse':arbitrary_inverse_cases==256 and arbitrary_inverse_failures==0,
      'coherent_packet_states':coherent['states']==9
        and coherent['maximum_norm_residual']<3e-10
        and coherent['maximum_inverse_norm_residual']<3e-10,
      'fermionic_seam':fermionic['schedule_rows']==4096
        and fermionic['target_failures']==fermionic['sign_failures']==0
        and fermionic['plain_SWAP_signed_row_mismatches']>0
        and fermionic['plain_SWAP_coherent_residual']>1e-3,
      'field_and_input_deletions':all(value>0 for value in deletion.values())
        and all(value>0 for value in input_deletion.values())
        and all(value>0 for value in independent_field_deletions.values()),
      'fixed_packet_routing':len(assigned)==100 and report['placement_collisions']==0
        and len(instructions)==718 and len(routed)==2598
        and not any(report[key] for key in ('non_NN_failures','operand_order_failures','route_return_failures')),
    }
    report['checks']=checks;report['pass']=all(checks.values())
    report['report_sha256']=sha256(json.dumps(report,sort_keys=True,default=str,separators=(',',':')).encode()).hexdigest()
    for label,passed in checks.items():print('PASS' if passed else 'FAIL',label,'::',passed)
    print('SUMMARY_JSON',json.dumps(report,sort_keys=True,default=str))
    print('CYCLE714_FULL34_FIXED_PACKET_PHYSICAL_M2_PASS' if report['pass'] else 'CYCLE714_FULL34_FIXED_PACKET_PHYSICAL_M2_INCOMPLETE')
    if not report['pass']:raise SystemExit(1)

if __name__=='__main__':main()
