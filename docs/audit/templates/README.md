# Audit-Lane CI Templates

This directory contains workflow templates for the audit lane that need to
be installed manually because the bot/OAuth token used by automated commits
does not have the GitHub `workflow` scope required to create or update files
under `.github/workflows/`.

## Installing `audit_workflow.yml`

To enable the audit-lane GitHub Actions workflow on this repo, a user with
push permission and `workflow` token scope (a normal repo collaborator using
their personal access token works) must run:

The template is kept byte-identical to the intended live workflow.

**Step 1 — inspect.** If a live workflow already exists, this stops on any
mismatch; reconcile before copying (if the live file is newer, update the
template instead of overwriting the live file):

```bash
mkdir -p .github/workflows
if [ -f .github/workflows/audit.yml ]; then
  diff -u docs/audit/templates/audit_workflow.yml .github/workflows/audit.yml \
    || { echo "live workflow differs from template — reconcile first"; exit 1; }
fi
```

**Step 2 — install** (only after step 1 passes or you have reconciled):

```bash
cp docs/audit/templates/audit_workflow.yml .github/workflows/audit.yml
git add .github/workflows/audit.yml
git commit -m "audit: install audit-lane CI workflow"
git push
```

Once installed, the workflow runs on the nightly `06:00 UTC` cron (with
auto-commit of regenerated audit data back to `main`) and on manual
`workflow_dispatch`. It has no pull-request trigger: review-loop is the
pre-merge gate, and the separate `pr-smoke.yml` workflow carries focused PR-time
process/tooling contract and regression signal with read-only permissions.
