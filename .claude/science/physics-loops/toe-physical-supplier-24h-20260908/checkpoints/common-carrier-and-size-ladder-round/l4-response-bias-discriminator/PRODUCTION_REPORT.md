# Fresh L4 response-bias discriminator: completed bounded result

All22 frozen cells completed without replacements/additions. Two populations each have8 independent paired11-source vectors:176 coupling-specific preparations are NOT176 independent ratio replicas. Primarysourceh=.02; diagnostich=.01;Vstencil.93/.95/.97, burn320,last40 unchanged. Originalfreeze and currentrawdiagnosticdelta verified beforelaunch. Allsource/cache/state/resource integritychecks passed.

Actual subprocess wall1104.612502625s; charged1107.990581500s including3.378078875smicro, under2400. Maximumcell67.140117583s; maximumRSS158.156250MiB. Originalconservativeforecast1685.506625s retained. No production source edits occurred.

| P | harmonic | source step | moment | paired delta SE |
|---|---|---|---|---|
|1024|1|0.02|0.754876929|0.010344798|
|1024|2|0.02|1.428928515|0.010594419|
|1024|1|0.01|0.757412184|0.014775382|
|1024|2|0.01|1.416449948|0.013936335|
|2048|1|0.02|0.752861406|0.008680430|
|2048|2|0.02|1.426379367|0.009057307|
|2048|1|0.01|0.761194464|0.006238065|
|2048|2|0.01|1.449502863|0.012535346|

All8 precision tests,16 oldF12/F24 comparisons,10 source-step/population/interaction comparisons, and8/8 half-window comparisons pass their frozen nominal4SE criteria. These are finite diagnostics, not coverage, mixing or bias certificates. Full11×11 energy covariance,4×4 ratio covariance, oldreference covariance and16×16 covariance of shared-reference method differences are retained in ANALYSIS.json. AllnegativeB/nonpositiveTcounts and noisyforward/backwardsecants remain explicit; reversedsecants are not a mathematicalconcavity refutation.

The primaryP2048h2 value1.426379367 remains below oldF24reference1.448942218 by.022562851 (~2.04combinedSE). P2048diagnostich.01 gives1.449502863, but selecting it as a corrected answer would be posthoc: its paired primary-minus-diagnostic difference is−.023123496±.016322043SE. AtP1024 that same difference is+.012478567±.013157612SE, opposite sign. The step-population interaction is.035602064±.020965015SE, also below4SE. Thus no resolved stable source-step effect is demonstrated. Populationdifference at smallerstep/h2 is−.033052915±.018744502SE (~1.76SE), not zero but unflagged. The earlier3.14SE discrepancy remains a real prior observation; fresh estimates do not prove it was caused by any one bias.

This run supplies a bounded negative discriminator: the declaredprecision was achieved, but step/P variations did not identify the methoddifference mechanism. It does not establish source-step independence or absence of populationbias. No newF horizon was measured, so directfinite-forwardbias remains unresolved. OldF12/F24 reference errors are independent of newruns but common to allnew comparisons; their covariance is included, not counted as fresh evidence eachtime. No stochasticburncomparison here; halfwindowdiagnostics are weaker.

Stored shiftedenergy is an algebraic transform of the local estimator(V−1)Nf+λX, not separatelymeasured growthhistory. No exactL4target, photon/pole, infraredexponent or largerL conclusion is claimed. No automaticF48 or furtherproduction follows. Allraw/sourcehashes preserved in FINAL_HASHES.json.
