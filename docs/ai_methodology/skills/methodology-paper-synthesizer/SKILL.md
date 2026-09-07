---
name: methodology-paper-synthesizer
description: Use when an LLM agent needs to synthesize raw prompt captures, repo history, review packets, branch/landing traces, and governance docs into a polished AI-methodology paper source packet or case study.
---

# Methodology Paper Synthesizer

## Skill Freshness

Before using this workflow, inspect its applicability and correctness and use
`docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md` to select one consistent
source revision, including references. Ordinary operation uses current main;
a user-requested prompt review/test uses the identified candidate under review
without automatically executing the workflow or replacing it with old main text.

Use this skill to turn raw AI/repo evidence into paper-ready methodology
material without confusing raw prompt history with public authority.

Before drafting, read `docs/WRITING_VOICE_GUIDE_2026-04-25.md`. The paper
voice is plain: question, object, check, result, caveat. Do not add importance
language where evidence would do the work.

## Workflow

1. **Start from curated surfaces.** Read the methodology front door,
   accountability note, repo-governance docs, publication package, and raw
   annex index before using prompt dumps.
2. **Use the synthesized surfaces first.** Read
   `METHODOLOGY_SYNTHESIS_2026-04-25.md` and
   `METHODOLOGY_CASE_STUDIES_2026-04-25.md` if present, then verify against raw
   evidence.
3. **Frame the case neutrally.** Identify the physics target, difficulty,
   observed outcome, and evidence for what the AI or process contributed or
   failed to catch. Do not assume a skill improved correctness or made the
   problem tractable. Negative, failed, and inconclusive cases are valid evidence.
4. **Trace the evidence chain.** Connect prompt/session evidence, branch or
   worktree evidence, review findings, landed artifacts, and final public
   status.
5. **State evidence selection.** Explain the eligible case set, selection
   criteria, omitted or unavailable records, and whether the cases are
   representative. Include counterexamples and failure cases relevant to the
   methodology claim. Use small sanitized excerpts or paraphrases; keep
   machine-local paths and long raw outputs in the annex unless necessary.
6. **Separate method from science.** Explain the workflow without promoting
   raw scientific claims beyond the current publication surface.
7. **Write as methods plus case studies.** State what another group can reuse:
   roles, artifacts, review gates, status vocabulary, and landing discipline.
8. **Name limits.** Disclosure, human responsibility, non-authorship of AI
   systems, privacy/sanitization, and auditability versus truth must be
   explicit.
9. **Keep the voice physical.** For each paragraph, make clear what was asked,
   what object was checked, what evidence supports it, or what remains open.

## Case Study Template

Use this structure:

- hard physics problem;
- why the target was difficult;
- AI/repo move;
- artifact outcome;
- evidence of process contribution or failure, and limits on attribution;
- case-selection criteria and relevant counterexamples;
- current claim boundary;
- reusable lesson.

## Required Outputs

- synthesized methodology claim;
- case-study evidence table;
- paper-draft or section-draft text;
- list of raw excerpts still needing sanitization;
- explicit statement that the methodology paper does not widen the physics
  claim boundary.

## Guardrails

- Do not cite raw chat as if it were a theorem.
- Do not expose unnecessary machine-local or private prompt material in polished
  prose.
- Do not let the methodology paper widen the physics claim boundary.
- Do not infer workflow efficacy from selected success stories, review
  agreement, or retained-row counts. Distinguish observed association from a
  justified causal comparison, and say when the evidence cannot decide.
- Do not imply AI authorship; keep human responsibility explicit.
