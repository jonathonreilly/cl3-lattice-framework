#!/usr/bin/env python3
"""Recover the missing L=4 KCPT full-center and dim-76 unlock classification.

This runner deliberately re-executes the landed U22 finite-surface construction instead
of trusting an old scratch transcript.  It then computes only the science delta that was
not preserved there:

* which single-element extension classes contain the inherited five-dimensional center
  Z(A) = C[M] plus span{sep}; and
* the centers, minimal central blocks, representation ranks, shell supports, and separator
  decompositions of the two 76-dimensional full-center extensions.

All classifications are numerical statements about the fixed L=4, N=64 matrices.  The
parent runner's stdout is captured so this companion remains below the repository output
limit, but its PASS/FAIL state is checked before any derived gate can pass.
"""

from __future__ import annotations

import contextlib
import io
import sys

import numpy as np


MEMBER_TOL = 1e-8
NULL_TOL = 1e-8
GAP_TOL = 1e-4

passed = 0
failed = 0


def gate(name: str, condition: bool, detail: str) -> None:
    global passed, failed
    ok = bool(condition)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    if ok:
        passed += 1
    else:
        failed += 1


def load_parent() -> tuple[dict, str, list[int]]:
    """Execute the parent in-process while intercepting its terminal sys.exit."""
    output = io.StringIO()
    exit_codes: list[int] = []
    real_exit = sys.exit
    try:
        sys.exit = lambda code=0: exit_codes.append(int(code or 0))
        with contextlib.redirect_stdout(output):
            import kcpt_ind12_separator_reach_quantized_census_minimal_unlock_2026_07_25 as parent
            namespace = vars(parent)
    finally:
        sys.exit = real_exit
    return namespace, output.getvalue(), exit_codes


ns, parent_output, parent_exit_codes = load_parent()
parent_ok = (
    ns.get("_P", [-1])[0] == 49
    and ns.get("_F", [-1])[0] == 0
    and parent_exit_codes == [0]
    and parent_output.rstrip().endswith("TOTAL: PASS=49 FAIL=0")
)
gate(
    "PARENT-REEXECUTION",
    parent_ok,
    f"landed U22 construction reran with PASS={ns.get('_P', [-1])[0]} "
    f"FAIL={ns.get('_F', [-1])[0]} exit_codes={parent_exit_codes} (expected 49/0/[0])",
)

D2f = ns["D2f"]
Jfull = ns["Jfull"]
Seps = ns["Seps"]
Hgens_f = ns["Hgens_f"]
Pf = ns["Pf"]
Pa = ns["Pa"]
Pb = ns["Pb"]
sep = ns["sep"]
records = ns["records"]
classes = ns["classes"]
word_algebra = ns["word_algebra"]
rowmats = ns["rowmats"]
center_of = ns["center_of"]
sv_margins = ns["sv_margins"]
count_clusters = ns["count_clusters"]
span_dim = ns["span_dim"]
frob = ns["frob"]
orthonormal_basis = ns["orthonormal_basis"]

# U20 identifies this five-dimensional space as the full center Z(A).  Rebuild the
# candidate basis and directly check centrality against generators of A.
zfull_rows = orthonormal_basis(Pf + [sep])
zfull_mats = [row.reshape(64, 64) for row in zfull_rows]
full_generators = [D2f, Jfull, Seps] + Hgens_f
max_z_comm = max(frob(g @ z - z @ g) for g in full_generators for z in zfull_mats)
gate(
    "FULL-CENTER-BASIS",
    zfull_rows.shape[0] == 5,
    f"dim span(P_0,P_1,P_2,P_3,sep)={zfull_rows.shape[0]} (=5)",
)
gate(
    "FULL-CENTER-CENTRALITY",
    max_z_comm < MEMBER_TOL,
    f"maximum Frobenius commutator with generators of A={max_z_comm:.3e} (<1e-8)",
)

# C[M] is already contained in A_nat.  Since Z(A)=C[M] direct-sum span{sep}, each
# intersection has dimension four plus one exactly when the measured separator residual
# vanishes.  The omega values were recomputed above by the parent, not copied from cache.
for record in records:
    record["sep_residual"] = float(np.sqrt(max(0.0, 1.0 - record["omega"])))
    record["z_intersection_dim"] = 5 if record["sep_residual"] < MEMBER_TOL else 4

intersection_hist: dict[int, int] = {}
for record in records:
    d = record["z_intersection_dim"]
    intersection_hist[d] = intersection_hist.get(d, 0) + 1

full_rows = [r for r in records if r["z_intersection_dim"] == 5]
nonfull_rows = [r for r in records if r["z_intersection_dim"] == 4]
full_ids = [r["idx"] for r in full_rows]
full_metadata = sorted((r["idx"], r["size"], r["dim"], r["order"]) for r in full_rows)
omega_one_ids = [r["idx"] for r in records if abs(r["omega"] - 1.0) < 1e-9]
max_full_residual = max(r["sep_residual"] for r in full_rows)
min_nonfull_residual = min(r["sep_residual"] for r in nonfull_rows)

gate(
    "CENTER-INTERSECTION-HISTOGRAM",
    intersection_hist == {4: 33, 5: 3},
    f"class counts by dim(C_g intersection Z(A))={intersection_hist} (expected {{4:33,5:3}})",
)
gate(
    "CENTER-MEMBERSHIP-SEPARATION",
    max_full_residual < MEMBER_TOL and min_nonfull_residual > 0.5,
    f"max full residual={max_full_residual:.3e} (<1e-8); "
    f"min non-full residual={min_nonfull_residual:.6f} (>0.5)",
)
gate(
    "FULL-CENTER-CLASS-IDS",
    full_ids == [14, 25, 27],
    f"zero-based H-class ids with full center={full_ids} (expected [14,25,27])",
)
gate(
    "FULL-CENTER-CLASS-METADATA",
    full_metadata == [(14, 4, 28, 4), (25, 64, 76, 12), (27, 64, 76, 12)],
    f"(id,size,algebra-dim,order)={full_metadata}",
)
gate(
    "CENTER-REACH-EQUIVALENCE",
    full_ids == omega_one_ids,
    f"full-center classes equal omega=1 classes: {full_ids} == {omega_one_ids}",
)
gate(
    "ONE-ELEMENT-CENTER-UNLOCK",
    ns["dimZnat"] == 4 and len(full_rows) == 3,
    f"A_nat center dim={ns['dimZnat']}; one added representative reaches dim 5 in {len(full_rows)} classes",
)


def central_profile(record: dict, seed: int) -> dict:
    """Compute one seeded minimal-central-block resolution of a dim-76 extension."""
    rep = classes[record["idx"]][0].astype(float)
    basis, closed = word_algebra([D2f, Jfull, Seps, rep])
    matrices = rowmats(basis)
    center_dim, center_mats, singular_values = center_of(matrices, [D2f, Jfull, Seps, rep])
    null_max, kept_min = sv_margins(singular_values)
    groups, _, vectors, max_intra, min_inter = count_clusters(center_mats, seed)
    idempotents = [vectors[:, group] @ vectors[:, group].conj().T for group in groups]
    block_dims = [span_dim([e @ x @ e for x in matrices]) for e in idempotents]
    ranks = [int(round(np.trace(e).real)) for e in idempotents]
    supports = [tuple(m for m in range(4) if frob(Pf[m] @ e) > MEMBER_TOL) for e in idempotents]
    profile: dict[tuple[int, int, tuple[int, ...]], int] = {}
    for block_dim, rank, support in zip(block_dims, ranks, supports):
        key = (block_dim, rank, support)
        profile[key] = profile.get(key, 0) + 1

    identity = np.eye(64, dtype=complex)
    partition_residual = frob(sum(idempotents, np.zeros_like(identity)) - identity)
    idempotent_residual = max(frob(e @ e - e) for e in idempotents)
    hermitian_residual = max(frob(e - e.conj().T) for e in idempotents)
    orthogonality_residual = max(
        frob(ei @ ej)
        for i, ei in enumerate(idempotents)
        for j, ej in enumerate(idempotents)
        if i != j
    )
    central_residual = max(frob(g @ e - e @ g) for g in [D2f, Jfull, Seps, rep] for e in idempotents)

    shell_two = [e for e, support in zip(idempotents, supports) if support == (2,)]
    plus_atoms = [e for e in shell_two if frob(Pa @ e - e) < MEMBER_TOL]
    minus_atoms = [e for e in shell_two if frob(Pb @ e - e) < MEMBER_TOL]
    assigned = len(plus_atoms) + len(minus_atoms)
    plus_sum = sum(plus_atoms, np.zeros_like(sep, dtype=complex))
    minus_sum = sum(minus_atoms, np.zeros_like(sep, dtype=complex))
    separator_residual = frob(sep - (plus_sum - minus_sum))

    return {
        "closed": closed,
        "algebra_dim": basis.shape[0],
        "center_dim": center_dim,
        "null_max": null_max,
        "kept_min": kept_min,
        "clusters": len(groups),
        "max_intra": max_intra,
        "min_inter": min_inter,
        "block_dims": sorted(block_dims),
        "ranks": sorted(ranks),
        "profile": profile,
        "partition_residual": partition_residual,
        "idempotent_residual": idempotent_residual,
        "hermitian_residual": hermitian_residual,
        "orthogonality_residual": orthogonality_residual,
        "central_residual": central_residual,
        "shell_two_atoms": len(shell_two),
        "plus_atoms": len(plus_atoms),
        "minus_atoms": len(minus_atoms),
        "assigned_atoms": assigned,
        "separator_residual": separator_residual,
    }


dim76_rows = [r for r in full_rows if r["dim"] == 76]
profiles = {r["idx"]: [central_profile(r, 20260903), central_profile(r, 42)] for r in dim76_rows}
all_profiles = [profile for pair in profiles.values() for profile in pair]
expected_ranks = [2] * 6 + [4] * 13
expected_profile = {
    (4, 2, (0,)): 2,
    (4, 4, (0,)): 1,
    (4, 4, (1,)): 6,
    (4, 4, (2,)): 6,
    (4, 2, (3,)): 4,
}
max_certificate_residual = max(
    max(
        p["partition_residual"],
        p["idempotent_residual"],
        p["hermitian_residual"],
        p["orthogonality_residual"],
        p["central_residual"],
    )
    for p in all_profiles
)
central_certificates_ok = max_certificate_residual < MEMBER_TOL

gate(
    "DIM76-CLASS-COUNT",
    len(dim76_rows) == 2 and [r["idx"] for r in dim76_rows] == [25, 27],
    f"dimension-76 full-center class ids={[r['idx'] for r in dim76_rows]} (expected [25,27])",
)
gate(
    "DIM76-TRUE-CLOSURE",
    all(p["closed"] and p["algebra_dim"] == 76 for p in all_profiles),
    f"all two-class/two-seed profiles closed with algebra dims={[p['algebra_dim'] for p in all_profiles]}",
)
gate(
    "DIM76-CENTER-DIMENSIONS",
    all(p["center_dim"] == 19 for p in all_profiles),
    f"center dimensions by class/seed={[[p['center_dim'] for p in pair] for pair in profiles.values()]} (=19)",
)
gate(
    "DIM76-CENTER-SVD-GAPS",
    all(p["null_max"] < NULL_TOL and p["kept_min"] > GAP_TOL for p in all_profiles),
    f"max null={max(p['null_max'] for p in all_profiles):.3e}; "
    f"min kept={min(p['kept_min'] for p in all_profiles):.6f}",
)
gate(
    "DIM76-TWO-SEED-CENTER-CLUSTERS",
    all(p["clusters"] == 19 and p["max_intra"] < NULL_TOL and p["min_inter"] > GAP_TOL for p in all_profiles),
    f"clusters={[p['clusters'] for p in all_profiles]}; max intra={max(p['max_intra'] for p in all_profiles):.3e}; "
    f"min inter={min(p['min_inter'] for p in all_profiles):.6f}",
)
gate(
    "DIM76-WEDDERBURN-TYPE",
    all(p["block_dims"] == [4] * 19 for p in all_profiles),
    "every minimal central corner has complex dimension 4, resolving M2(C)^19 for both classes and seeds",
)
gate(
    "DIM76-REPRESENTATION-RANKS",
    all(p["ranks"] == expected_ranks for p in all_profiles),
    "central-idempotent ranks are six 2s and thirteen 4s for all profiles="
    f"{all(p['ranks'] == expected_ranks for p in all_profiles)}",
)
gate(
    "DIM76-SHELL-PROFILE",
    all(p["profile"] == expected_profile for p in all_profiles),
    "common (corner-dim,rank,shell)->count profile recovered="
    f"{all(p['profile'] == expected_profile for p in all_profiles)}",
)
gate(
    "DIM76-CENTRAL-IDEMPOTENTS",
    central_certificates_ok,
    f"max partition/idempotent/Hermitian/orthogonality/central residual="
    f"{max_certificate_residual:.3e}",
)
gate(
    "DIM76-SEPARATOR-SIX-ATOM-SPLIT",
    all(
        p["shell_two_atoms"] == 6
        and p["plus_atoms"] == 3
        and p["minus_atoms"] == 3
        and p["assigned_atoms"] == 6
        for p in all_profiles
    ),
    "(shell-2,+,-,assigned)="
    f"{[(p['shell_two_atoms'], p['plus_atoms'], p['minus_atoms'], p['assigned_atoms']) for p in all_profiles]}",
)
gate(
    "DIM76-SEPARATOR-RECONSTRUCTION",
    all(p["separator_residual"] < MEMBER_TOL for p in all_profiles),
    f"max ||sep-(sum three plus atoms - sum three minus atoms)||_F="
    f"{max(p['separator_residual'] for p in all_profiles):.3e}",
)
primary_profiles = [profiles[idx][0]["profile"] for idx in sorted(profiles)]
gate(
    "DIM76-COMMON-ABSTRACT-PROFILE",
    len(primary_profiles) == 2 and primary_profiles[0] == primary_profiles[1],
    "the two non-H-conjugate classes have the same M2(C)^19 representation profile",
)

# Discriminating controls: omitting the separator collapses the proposed full-center basis,
# and the already-resolved 28-dimensional algebra must not masquerade as the dim-76 type.
truncated_center_dim = orthonormal_basis(Pf).shape[0]
gate(
    "CONTROL-DROP-SEPARATOR",
    truncated_center_dim == 4 and zfull_rows.shape[0] == 5,
    f"omitting sep collapses the proposed center basis from {zfull_rows.shape[0]} to {truncated_center_dim}",
)
gate(
    "CONTROL-A28-IS-DIFFERENT",
    ns["dimZ28"] == 7 and sorted(ns["blockdims"]) == [4] * 7 and ns["dimZ28"] != 19,
    f"same machinery resolves A28 as M2(C)^7 (center {ns['dimZ28']}), not M2(C)^19",
)

print(f"TOTAL: PASS={passed} FAIL={failed}")
sys.exit(0 if failed == 0 else 1)
