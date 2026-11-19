# ADR-0020: Keep dependencies up to date with Dependabot

- **Status:** Accepted
- **Date:** 2026-11-19

## Context

Actions and pre-commit hooks are pinned to commit hashes (ADR-0016, ADR-0017), and Python dependencies are locked in `uv.lock` (ADR-0014). Pinning prevents unreviewed changes, but nothing is updated unless someone does it, including security fixes.

The alternatives considered were:

- Dependabot, built into GitHub, with grouped weekly updates.
- Renovate, which is more configurable but is an external app with write access and a more complex configuration.
- Manual updates, which depend on someone remembering to do them.

## Decision

We will use Dependabot version updates for GitHub Actions, uv and pre-commit, configured in `.github/dependabot.yml`. Updates are checked weekly and grouped into one pull request per ecosystem. New releases wait 7 days before being proposed, to reduce the risk of adopting a compromised release. Commit messages follow Conventional Commits, with `ci(deps)` for actions and `chore(deps)` for Python and hooks.

Dependabot alerts and security updates are enabled, and security updates are not delayed.

## Consequences

- Pinned dependencies stay current without manual work.
- Every update goes through a pull request, CI and the `main` ruleset (ADR-0019).
- Updates arrive at least 7 days after release, except security fixes.
- Dependabot commits are signed by GitHub but carry no sign-off, so the DCO check will need to exempt Dependabot.
- npm will be added when the runtime has a `package.json`.
