# ADR-0019: Protect main with a repository ruleset

- **Status:** Accepted
- **Date:** 2026-11-19

## Context

The project has CI (ADR-0017), pre-commit hooks (ADR-0016) and signed commits, but none of them is enforced. A pull request with failing CI could be merged, hooks can be skipped with `--no-verify`, and anyone with write access could push unsigned commits or force push to `main`.

The project has a single maintainer, and GitHub does not allow authors to approve their own pull requests.

The alternatives considered were:

- A ruleset with an empty bypass list and no required approvals.
- A ruleset with required approvals and the maintainer in the bypass list, which in practice means bypassing every rule on every pull request.
- Classic branch protection, which GitHub now recommends replacing with rulesets.

## Decision

We will protect the default branch with a repository ruleset named `main`, with an empty bypass list. It restricts deletions, blocks force pushes, requires linear history and signed commits, requires a pull request with conversation resolution and squash as the only merge method, and requires the `CI result` check from GitHub Actions on an up-to-date branch.

The configuration is documented in `docs/maintainers/branch-protection.md`.

## Consequences

- Every change to `main`, including the maintainer's, goes through a pull request with CI passing.
- History on `main` cannot be rewritten or deleted.
- Pull requests must be updated when `main` moves on, which runs CI again.
- Nobody reviews the maintainer's pull requests until a second maintainer joins, when required approvals and code owner reviews will be enabled.
