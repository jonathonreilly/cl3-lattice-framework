# Local L4 finite-projector reptation results

The frozen calibration does not support projection convergence:11/12 comparisons are flagged and only6/12 precision checks pass. Both tau36 primary channels remain strongly burn/projection sensitive. No ground-state or method-agreement conclusion is supported.

All96 frozen two-chain shards completed: six logical cells,32 independent chains each,64n measured attempted updates. Long-burn32n arms remain primary. No replacements or coverage changes. These are finite-projection path-chain research estimates, not a ground-state or convergence certificate.

Subprocess wall total 1170.154301s plus .0910385s measurement micro. Maximum shard wall 28.131658s; maximum reported RSS 34.265625MiB.

|tau|burn/n|harmonic|ratio|replica SE|precision|
|---|---|---|---|---|---|
|4|8|1|0.8005748847397672|0.009834076836993725|True|
|4|8|2|1.5316994191211866|0.014196862034697756|True|
|4|32|1|0.7588276792659587|0.0045273690703074255|True|
|4|32|2|1.4297893353627122|0.0068342844904741165|True|
|12|8|1|1.2566084350820825|0.04573043029493711|False|
|12|8|2|2.335551895044392|0.08036516267873672|False|
|12|32|1|0.7971106009544798|0.007739569388539291|True|
|12|32|2|1.5165482705323425|0.014327417599212333|True|
|36|8|1|6.129052607663727|0.4803569830423621|False|
|36|8|2|11.200765121742421|0.84637214279403|False|
|36|32|1|2.2026788177361567|0.13924039958956036|False|
|36|32|2|3.9817690224380122|0.2543004177423074|False|

Nominal precision4SE<=10%ratio passes6/12. Flagged comparisons11/12 at4SE; full comparisons remain in ANALYSIS.json. There is no exact L4 target consistency gate. Unflagged differences do not establish equilibration or negligible finite-projection bias.

Flagged comparisons: [{"cells": [0, 1], "harmonic": 2, "difference": 0.10191008375847432, "SE": 0.01575621579342507, "flag": true}, {"cells": [2, 3], "harmonic": 1, "difference": 0.4594978341276027, "SE": 0.04638074157751379, "flag": true}, {"cells": [2, 3], "harmonic": 2, "difference": 0.8190036245120496, "SE": 0.08163231141797982, "flag": true}, {"cells": [4, 5], "harmonic": 1, "difference": 3.9263737899275704, "SE": 0.5001307029521589, "flag": true}, {"cells": [4, 5], "harmonic": 2, "difference": 7.218996099304409, "SE": 0.8837502512371184, "flag": true}, {"cells": [1, 3], "harmonic": 1, "difference": -0.0382829216885211, "SE": 0.008966493462819832, "flag": true}, {"cells": [1, 3], "harmonic": 2, "difference": -0.08675893516963029, "SE": 0.015873951605033774, "flag": true}, {"cells": [3, 5], "harmonic": 1, "difference": -1.4055682167816768, "SE": 0.13945533267745788, "flag": true}, {"cells": [3, 5], "harmonic": 2, "difference": -2.4652207519056697, "SE": 0.2547037050358205, "flag": true}, {"cells": [1, 5], "harmonic": 1, "difference": -1.443851138470198, "SE": 0.1393139833202655, "flag": true}, {"cells": [1, 5], "harmonic": 2, "difference": -2.5519796870753, "SE": 0.25439223633674196, "flag": true}]

The estimator uses midpointNf and both harmonic structure factors, with endpoint energy measured on the same chain. Their full chain-vector covariance, ratio influence vectors, chain influence covariance and estimator covariance(/32) are retained. The covariance diagonal is checked against SE². Every ordered16-batch vector and acceptance/self/rejection/direction-run counter is in the raw shard JSON. Strong overlap of adjacent midpoint paths is not treated as independent sampling;32 chains provide the replica units.

n=384tau is the TOTAL projector-bond count, with one-sided projectiontime n/(2M)=tau. The exact finite-G midpoint law is a squared projected trial amplitude. Its Dirichlet ratio is not automatically the ground spectral first moment. The initial paths were all seed/self and finite burn was supplied. No branching population is used, but this does not remove path equilibration, finite projection or finite-chain ratio errors.

Source and full local import closure remain frozen: production.py imports only own core.py; NumPy/standard Python are external software imports. No campaign module is read at production runtime. Original micro/core/freezes and review corrections remain preserved. No physical exponent, photon/pole, method equality or ground-state conclusion is inferred from these cells.

PRODUCTION_FINAL_HASHES.json binds every raw shard and source/report. No additional sampling was launched.
