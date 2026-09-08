# Frozen RK size-ladder results

All24 fixed shards completed; six logical cells each128 independent chains x64 origins. Long-burn primaries were specified before execution: L8burn512 andL16burn2048. No replacements or coverage changes. Earlier authorization arrived while the agent was completed; STARTED.json records the subsequent explicit-resume launch rather than implying earlier execution.

Actual subprocess wall 567.459043s, plus 9.051151s prior micros. Maximum subprocess wall 53.701952s; maximum reported RSS 178.890625MiB. These are measured runtime receipts, not asymptotic efficiency claims.

|L|burn|h|alpha|r|SE|a|C plugin|precision|
|---|---|---|---|---|---|---|---|---|
|8|32|1|0.0732233|3.9367169|0.06262|0.2046855|1.0940483|True|
|8|32|1|0.1464466|3.0312224|0.03127|0.2046855|1.0643595|True|
|8|32|1|0.2928932|2.1370859|0.0117|0.2046855|1.0633685|True|
|8|32|2|0.25|1.1865109|0.01698|0.6992535|1.1262996|True|
|8|32|2|0.5|0.8959627|0.007923|0.6992535|1.0744864|True|
|8|32|2|1|0.61632196|0.003866|0.6992535|1.0472872|True|
|8|128|1|0.0732233|3.9886595|0.055|0.19854606|1.0839955|True|
|8|128|1|0.1464466|3.0968782|0.03033|0.19854606|1.0684003|True|
|8|128|1|0.2928932|2.1117015|0.01393|0.19854606|1.0377731|True|
|8|128|2|0.25|1.1703354|0.01837|0.69430277|1.1051509|True|
|8|128|2|0.5|0.8872702|0.007821|0.69430277|1.0596693|True|
|8|128|2|1|0.62464234|0.003901|0.69430277|1.0583332|True|
|8|512|1|0.0732233|3.9771036|0.06694|0.20731989|1.1157493|True|
|8|512|1|0.1464466|3.0755196|0.02871|0.20731989|1.0880158|True|
|8|512|1|0.2928932|2.1080261|0.01197|0.20731989|1.0544623|True|
|8|512|2|0.25|1.1306697|0.01824|0.6953254|1.0688508|True|
|8|512|2|0.5|0.89922294|0.01009|0.6953254|1.074864|True|
|8|512|2|1|0.61817498|0.004037|0.6953254|1.0480077|True|
|16|32|1|0.01903012|15.532447|0.2294|0.054267871|1.1384971|True|
|16|32|1|0.03806023|11.918878|0.1152|0.054267871|1.1004474|True|
|16|32|1|0.07612047|8.2222668|0.05289|0.054267871|1.0720877|True|
|16|32|4|0.25|1.1498114|0.01782|0.69831535|1.0903838|True|
|16|32|4|0.5|0.89259435|0.008372|0.69831535|1.0696095|True|
|16|32|4|1|0.60956719|0.003489|0.69831535|1.0352373|True|
|16|128|1|0.01903012|15.639698|0.2455|0.053322931|1.1315798|True|
|16|128|1|0.03806023|11.901334|0.1329|0.053322931|1.0875816|True|
|16|128|1|0.07612047|8.1685439|0.05064|0.053322931|1.0573641|True|
|16|128|4|0.25|1.1623715|0.01629|0.69385405|1.097109|True|
|16|128|4|0.5|0.9063824|0.009211|0.69385405|1.0820883|True|
|16|128|4|1|0.61424664|0.003748|0.69385405|1.0404442|True|
|16|2048|1|0.01903012|14.809204|0.2302|0.053795892|1.0784953|True|
|16|2048|1|0.03806023|11.851284|0.1102|0.053795892|1.088613|True|
|16|2048|1|0.07612047|8.1932676|0.04947|0.053795892|1.0644395|True|
|16|2048|4|0.25|1.1636487|0.01777|0.6912612|1.0952974|True|
|16|2048|4|0.5|0.89851158|0.008915|0.6912612|1.070362|True|
|16|2048|4|1|0.61638809|0.003436|0.6912612|1.0424733|True|

Precision4SE<=10%r passes36/36 rows; valid positive pooled responses36/36. Burn-control comparisons flagged0/24 at4SE. These nominal diagnostics are not simultaneous confidence bounds or a stationarity certificate. Unflagged differences do not prove equilibration.

Flagged burn comparisons: []

The ideal geometric elementary-step estimator is a finite-regulator resolvent. Contributions above the predeclared cap are zeroed, not redrawn or replaced by capped endpoints. The small-rational certificate bounds ideal stationary clipping error by .001. Floating uniform/logarithm generation is not an exact probability oracle; no rigorous sampling-error enclosure is claimed. Finite-burn and regulator effects remain distinct from this clipping bound.

Minimum-q regulators scale with qhat²/2; matched-q regulators remain .25,.5,1. All joint Nf/S/Y chain means, full sample covariance and a/r/b/C influence covariance are in ANALYSIS.json. Every raw complex origin/product, Nf, lag and clipping flag is in per-chain NPZ files. Averages use chains as independent units, not individual origins or channels.

C=(a+alpha)r>=1 and Delta_supported<=1/r-alpha<=a are exact-measure inequalities on the declared component, not certified bounds for the plug-in estimates. Large regulator can make C close to1 trivially. No dispersion exponent, pole, photon or continuum claim is inferred. The previous14/18 precision pilot remains unchanged.

PRODUCTION_FINAL_HASHES.json binds current code, dependencies, analysis, status, report and every raw shard artifact. No further runs were launched.
