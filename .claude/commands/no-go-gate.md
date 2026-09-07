# /no-go-gate — Negative-Claim Discipline Gate

Run the repo-native no-go discipline skill from:

`docs/ai_methodology/skills/no-go-discipline/SKILL.md`

## Invocation

```text
/no-go-gate "<the negative claim about to ship>"
```

## When To Use

Before shipping ANY artifact that asserts a negative result, even outside a
physics-loop campaign: a `no_go` note, a stretch-attempt-negative outcome, a
`bounded_theorem` whose source note names walls/open obligations, a derived no-go
boundary inside a positive theorem, or a review/analysis verdict that names
walls. Agents are good at finding one route that fails and bad at proving all
routes fail; this gate makes that gap explicit.

## Required Behavior

1. Read the skill file above before acting, and perform the skill freshness
   check in `docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md`.
2. Walk N1–N8 in writing against the actual claim text: alternative-route
   enumeration (≥5 normalized mathematical approach families),
   wall-independence audit, hidden-wall scan, residual matching, rhetoric
   audit, partial-closure path scan, concrete-mechanism steelman, cross-cycle
   echo.
3. Run the primitive registry check
   (`docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`) before writing
   "no retained primitive supplies this" or any equivalent wall language.
4. Output `PASS` (claim honestly scoped; checklist attached to the artifact
   and PR body) or `FAIL` with the failing items named and the narrowest
   demoted claim proposed (`partial-attempt-with-named-untested-routes`,
   `partial-narrowing`, `bounded-with-corrected-wall-count`, or
   `stretch-attempt-with-honest-residual`).
5. Record the outcome in the lane's `NO_GO_LEDGER.md` when one exists.

## Non-Negotiables

- Do not fabricate coverage to pass a claim. Narrow scope alone does not
  satisfy the current five-route packet requirement; a packet limitation is
  distinct from the validity of the mathematical theorem.
- A FAIL means demote and reship narrower — never ship the original framing
  with the checklist attached as decoration.
