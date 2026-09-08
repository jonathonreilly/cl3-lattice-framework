# Prospective local L4 reptation

Six ordered cells(tau,burnmult)=(4,8),(4,32),(12,8),(12,32),(36,8),(36,32). n=384tau;32 independent chains each, measured64n updates,16 contiguous batches4n. Two-chain shards,16 shards/cell. Long-burn32n primary. Seed202609160000+32cell+2shard+rep. All-seed/self initial path,direction+. No oracle initialization/L4 oracle. V=.95,harmonics(1,2). No coverage replacements.

Measure vector(Nf_mid,S_h1,S_h2,E_endpoint), E=-.05(Nf_left+Nf_right)/2. Ratios qhat²(.95meanNf−meanE)/(64meanS_h). Chain-level full covariance and joint ratio influences, independent burn/projection comparisons. Primary precision4SE<=10%ratio if denominator/numerator positive; raw invalid/negative values retained. No finite-target consistency claim, no unflagged-comparison convergence claim, no ground/pole promotion. Strongly overlapping path measurements and batches are not independent replicates.

One authorized end-to-end micro4096updates,L4n384,burn0,seed202609169999,<=30s384MiB. Includes same measurement accumulation and batch allocation (16 batches256) plus final serialization; no physics criterion. Profile before production forecast. Proposed production per-shard<=180s384MiB with aggregate envelope decided by root after profile/review. No production authorized by this document.
