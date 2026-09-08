# Portable reproduction boundary

All raw probes and source-bound reviews are copied byte for byte from their frozen research artifacts. Raw timestamps/resource use are historical execution evidence, not canonical runner caches. Some raw scripts write a result file next to themselves. The reproduction launcher therefore copies the probe tree to a temporary directory and runs there; the tracked packet remains unchanged.

One derivative, `probes/probability-family-cold-review/independent_portable.py`, replaces exactly one historical absolute source-directory assignment with `Path(__file__).resolve().parents[1]/"probability-family"`. The original independent.py remains preserved. No mathematical expression or assertion is changed. The portable checker consumes fresh output from the probability-family runner in that temporary copy.

The complete source and transitive scientific scope are reviewed in the adjacent proof/review files. The launcher only orchestrates execution and records failures; its integrity checks do not independently prove the mathematics. Dependencies: Python3 with NumPy and SymPy. No network is used during reproduction.
