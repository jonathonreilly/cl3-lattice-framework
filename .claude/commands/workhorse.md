# /workhorse — Bounded Science Execution

Read `docs/ai_methodology/skills/workhorse/SKILL.md` and follow its current
execution split, worker profiles, neutral task contract, verification, and
handoff rules. This command is an adapter; it does not maintain another worker
policy. Read applicable repository instructions before dispatching work.

## Invocation

```text
/workhorse "<bounded task or science block>"
```

The supervising agent chooses the target and prepares the task. Workers may
implement, compute, independently challenge a candidate proof, or perform a
focused review lens. They must report counterexamples, spec errors, and open
steps without pressure to produce an affirmative result. The supervisor reviews
the result and owns the next authorized action.

## Dispatch Contract

Give each worker:

- the exact question and why it matters to the selected science target;
- allowed premises, source paths, and any candidate proof with unproved steps
  clearly labeled;
- a bounded read set, exact editable paths, and a durable worktree for work that
  needs recovery;
- the discriminating check, required evidence, resource limit, and next step
  if the hypothesis fails;
- an explicit role: drafting/computation, independent checker, or read-only
  review lens, with the context it may receive;
- incremental artifact writes and a concise final report containing actual
  commands, results, uncertainties, and files changed.

Analysis workers do not commit, push, access the network, apply audit verdicts,
or run review/audit orchestration. For other worker roles, the task must state
the permitted actions within the applicable repository instructions. Do not
disable governing instructions through a blanket ban on local skills.

Keep acceptance criteria separate from the hoped-for physics result. A correct
runner may refute the hypothesis. Do not require `PASS>=N`, prescribe a desired
measurement, invent identifiers, or treat a known comparator as an input to its
own prediction.

## Verify And Deliver

Review every changed line and hand-check the central mathematical step. Use
the skill's disjoint checker discipline for substantive computational blocks;
choose proof review or focused validation for other artifacts. A green terminal
or a matching external number is insufficient by itself.

Use `physics-loop` for science delivery and its current conformance requirements
for notes, runners, caches, source provenance, and citation-graph changes.
Its default is continuous discovery on a coherent campaign branch with milestone
PRs. Keep provisional dependencies explicit and independently check critical
steps before extensive reuse; do not require a PR or formal audit for each
intermediate lemma. `--delivery block` remains available when requested.
Record author checks honestly and hand the PR to a fresh `review-loop` for the
independent review and any authorized landing. Audit ratification remains a
separate post-landing lane. An explicit end-to-end repair campaign authorizes
its specified orchestration; workers never self-ratify their own science.

Track only worker handles returned by this session. Quiet logs and low local
CPU are compatible with remote reasoning; inspect owned-task status and its
declared deadline before interrupting. Preserve unresolved work for recovery;
remove a worktree only after its content and durable recovery path are verified.
