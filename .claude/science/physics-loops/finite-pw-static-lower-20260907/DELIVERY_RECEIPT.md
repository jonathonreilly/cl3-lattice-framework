# Final campaign delivery receipt

Status snapshot: 2026-09-07T22:54:24.213640+00:00

The science campaign ran within the authorized2026-09-07 10:59:43–22:59:43UTC window. Scientific validation and publication are complete at the status snapshot below; final campaign coordination continues through the end of the authorized window. The report records scientific scope; this receipt supersedes its earlier delivery-status wording.

## Latest main and completed validation

All24 open campaign branches contain main66b1b4f8a964f4011a3f4e7876369b7daf8e1834. The five directly targeting main each completed a new full pipeline, strict lint and nonempty readiness check against that pin. A later receipt commit is distinguished from the frozen science head used during its pipeline.

| PR | Pipeline | Ready rows | Frozen science merge head | Published receipt head |
|---|---|---|---|---|
| 8010 | 5be6862e2f65 PASS | 2 | `c25bc0ec41ca60a04cd62668669ee1bb36c22ac7` | `f29251ea68ba2bcd96c807881eae7bc8c6cfd48e` |
| 8011 | bf14b25da7c4 PASS | 1 | `f4759f292f9cddd4fbaf568244a1f6a2f47d0a8e` | `11395e60ff268110e8d105ebb61ef4102cbf4b4a` |
| 8012 | 60d3f14e4e1b PASS | 1 | `c76c70c497c06cba2291be9f4bcd9c46d3c1e2e0` | `910fb7caa43ffc5df3d5f16d1c618cba4135fa69` |
| 8013 | a7eba12be23b PASS | 1 | `aa30a25fc0f75bee3d2c6a0fd8056e0af44e7fd3` | `fc49894fc09b33042752f69bf33d637955bee208` |
| 8014 | fe769556b2ba PASS | 1 | `bbd45b6aade388c03b7be5a8e795769fb22ef47c` | `4aacc14450f2fa7877c25323b1ae25235bae91d5` |

The19 descendant branches8015–8033 were synchronized topologically. Every preexisting scientific source, helper, canonical cache and both helper-consumer registries was hash protected. Each passed strict lint and a nonempty live readiness replay using explicit historical UNAUDITED rows; that replay is not a new graph or full pipeline. Historical full-pipeline receipts retain the actual earlier heads and main pins. The final branch8033 additionally completed a fresh full pipeline against66b, as recorded below.

Parent science merge heads are included throughout the stack. Some later parent validation-packet metadata remains on those parent branches rather than being recursively merged through descendants. No missing scientific correction is implied, and no metadata commit is mislabeled as an earlier tested head.

## Review and attribution

31 campaign review PRs were created:8001 and8004–8033; seven earlier PRs are closed after external integration and24 remain open for review. External8002/8003 and the late U1 main commit are excluded from campaign credit. We performed no science merge to main and applied no audit verdict. Empty GitHub check lists mean no reported CI check, not success. Mergeability only rules out textual conflicts.

The original dirty user checkout was preserved; synchronization and validation used isolated worktrees. Reports, prospective next-campaign brief, exact controls, failed attempts, reviews and historical receipts are packaged in the review branches. The prospective bridge test is not a newly established theorem.

## Final combined-branch result and publication snapshot

Final branch8033 completed fresh full pipeline **3ed970d2af76**, strict lint and **20 nonempty readiness rows**, with zero evidence/control failures, against main66b. The frozen report/input head was `62dd2735ae80bba9a66e3446507f1df45ccba89c`; validation and lock-release metadata were subsequently published as `bec654c4f11c404bd7d786ac71ec2e5ade41b897`. The pipeline identifier is taken from the log's first “began full build” line; intermediate checkpoint IDs in that log are not substituted for it. All frozen scientific bytes remain unchanged. The fresh final-chain run does not retroactively turn each intermediate descendant's replay into a separate full pipeline.

At22:55:52UTC the live GitHub/local snapshot confirmed all24 open branch heads matched their published remotes, all24 worktrees were clean, all24 contained main66b, and no branch had a textual conflict. Nine branches had reported successful CI checks;15 had no reported checks, which are not treated as passes. No owned validation jobs remained. [Publication snapshot](FINAL_PUBLICATION_SNAPSHOT.json) records the exact observed heads and statuses. A later delivery-only commit may add this receipt and snapshot; it does not change any scientific source or the frozen pipeline head.

[The complete campaign report](CAMPAIGN_REPORT.md) and [next-campaign brief](NEXT_NATIVE_BRIDGE_CAMPAIGN.md) are the intended reading order. The actionable recommendation is the small native preparation/condition-to-Record source audit; if it has no retained candidate, move to the physical orbit-occupancy action/measure obligation.
