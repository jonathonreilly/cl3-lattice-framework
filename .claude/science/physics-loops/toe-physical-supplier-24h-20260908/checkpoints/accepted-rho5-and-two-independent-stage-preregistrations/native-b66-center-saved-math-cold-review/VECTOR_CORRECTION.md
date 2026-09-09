# Correction to prior runtime PASS

The parent found a real semantic error missed in fd697: unrelated G/H component vectors were sent through an ordered interval parser. This can reject valid saved data such as [2,1]. Prior PASS is preserved but superseded; no actual saved attempt occurred under it.

Affected fix PASS at worker5f935725ad61b1a13811d3b5378e31d9a8abd0f1f1398126e222abe7e803e876/roote208fe980ebd9051601caf7c82f3b7f80bb266aaa432d032e1bf1b9a2c9cda39. vector() now parses two canonical bounded independent components. Checker uses it for all G/H center/radius/cumulative/low/high/budget/width/target pairs; physical t,A,Aprime,weight and final B/Bprime use ordered interval(). Full changed call sites read. Three independent tiny parser checks pass, including decreasing positive/negative vectors and reversed interval refusal. Author full tiny two-component path is separately recorded. No native data loaded.
