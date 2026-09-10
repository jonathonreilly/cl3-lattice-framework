# Independent Checker Return

The structurally independent checker:

- imports no Source/Eta runner and reconstructs the code over its own exact
  `Q(1/sqrt(3))` field using `Fraction`, rather than SymPy;
- rebuilds all 84 contents, 24 proper cubic rotations, and 2,016 covariance
  cases;
- tests 18,816 trails through length 17 and 752,640 frontier candidates;
- independently simulates all 37,632 guarded maps, reproducing 1,176 clear
  successors and 36,456 blocked identity/permanence cases;
- tests 2,976 blocked local components and 229,728 candidate-direction cases,
  finding maximum eligible count zero;
- independently reconstructs all 2,688 formal fourteen-way continue-or-STOP
  distributions.

Return: `7/7`, mutations `47/47`, terminal
`CONTENT-ORIENTED-SAFE-FRONT`.

Post-implementation source comparison found only the boilerplate `git` and
`ancestor` functions with identical ASTs.  Normalized non-comment overlap is
125 lines out of the 1,575-line union (`7.94%`).  The checker neither imports
nor executes the primary.

The first execution exposed one scope phrase split across a Markdown newline.
Whitespace-normalized scope matching repaired that documentary false negative;
no mathematical implementation or check changed.
