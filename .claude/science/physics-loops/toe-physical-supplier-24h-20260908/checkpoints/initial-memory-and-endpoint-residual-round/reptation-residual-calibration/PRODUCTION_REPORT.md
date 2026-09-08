# n2 endpoint-residual calibration

All four fixed shards completed;32 independent chains,32768updates each,burn64,V=.95. Wall 3.572267s; originalmicro 0.169732s and reducedsmoke 0.151598s give total 3.893597s. No replacements or extra cells.

|quantity|estimate|replica SE|exact finite target|consistency|precision|
|---|---|---|---|---|---|
|D|1.617064487|0.0047063728|1.610801193|True|True|
|R|1.65643253|0.0046680538|1.650313344|True|True|
|correction|0.03936804241|0.00019027988|0.03951215107|True|True|
|VarH|0.007643616126|4.2960613e-05|0.007661487068|True|True|
|VarX|1.674453575|0.0084814725|1.688030001|True|True|

All five predeclared4SE oracle consistency and precision checks pass nominally. The nonzero correction is resolved on this finite n2 L2 path law. R is relative to Epsi, not E0. This does not validate warm-start convergence at longer n or larger L, nor establish a ground excitation.

VarH andVarX estimates remain signed; here both are positive. The plugin Cauchy bound 0.04556326203 is not a certified confidence bound. No clipping was applied. Earlier n48 micro negativeVarH remains preserved, not overwritten by this result.

Full six-vector chain means, covariance, D/R/correction/variance influence vectors and estimator covariance are in ANALYSIS.json. All ordered16-batch vectors and counts remain in shard JSON. Only32 chain units enter reported SE; individual overlapping updates and batches are not counted as independent replicas. Finite ratio estimators are not claimed unbiased.

Original footer NameError source/freeze and explicitly reduced smoke are preserved. Production used only the corrected reviewed freeze. No RK arm was mislabelled and no L4 residual production ran.
