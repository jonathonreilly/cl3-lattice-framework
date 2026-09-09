import os,sys,time,json,signal
os.environ.update(OPENBLAS_NUM_THREADS="1",OMP_NUM_THREADS="1",MKL_NUM_THREADS="1",VECLIB_MAXIMUM_THREADS="1")
signal.alarm(30)
sys.path.insert(0,"/Users/jonreilly/Projects/Physics-worktrees/review-backlog-eta-lineage-20260909/scripts")
import admissibility_d4_affine_lineage_binary_record_join_2026_08_29 as b3
import sympy as s
t=time.monotonic();d=b3.decoder_facts();R=s.Matrix([[0,0,1],[0,-1,0],[1,0,0]]);g=b3.b2.rotations().index(R);a=b3.action_facts();out={"mask17_orientation":d["orientation_table"][17],"mask27_orientation":d["orientation_table"][27],"rotation":R.tolist(),"pure_permuted_mask17":b3.b2.permute_mask(17,b3.b2.shell_permutations()[g]),"affine_mask17":a["action"](g,17),"affine_orientation":d["orientation_table"][a["action"](g,17)],"elapsed":time.monotonic()-t}
assert out["mask17_orientation"]==(0,1,0)
assert out["pure_permuted_mask17"]==17
assert out["affine_orientation"]==(0,-1,0)
print(json.dumps(out,default=str,indent=2))
