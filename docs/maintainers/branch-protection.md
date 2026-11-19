# Branch protection

The `main` branch is protected by a repository ruleset named `main`, configured in Settings > Rules > Rulesets. Its bypass list is empty, so the rules also apply to maintainers.

## Rules

| Rule | Setting |
| --- | --- |
| Restrict deletions | Enabled |
| Block force pushes | Enabled |
| Require linear history | Enabled |
| Require signed commits | Enabled |
| Require a pull request before merging | No required approvals, conversation resolution required, squash as the only merge method |
| Require status checks to pass | `CI result` from GitHub Actions, branches must be up to date |

## Why there are no required approvals

The project has a single maintainer, and GitHub does not allow authors to approve their own pull requests. Required approvals and code owner reviews will be enabled when a second maintainer joins.

## Verify the configuration

Run `gh api repos/skama-dev/skama/rules/branches/main --jq '.[].type'`. The output must list `deletion`, `non_fast_forward`, `required_linear_history`, `required_signatures`, `pull_request` and `required_status_checks`, in any order.
