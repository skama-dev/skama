# ADR-0021: Enable secret scanning with push protection and CodeQL default setup

- **Status:** Accepted
- **Date:** 2026-11-26

## Context

gitleaks blocks secrets before a commit (ADR-0016), but it can be skipped, may not be installed by external contributors, and does not run in CI. A secret pushed to a public repository can be found by automated scanners within minutes.

The linters and type checker do not look for security vulnerabilities. The compiler generates JavaScript that runs in other people's browsers, so flaws such as unescaped user data are especially relevant.

The alternatives considered were:

- GitHub secret scanning with push protection, or a gitleaks job in CI, which only reports a secret once it has been pushed.
- CodeQL with the default setup managed by GitHub, or the advanced setup with a workflow in the repository.

## Decision

We will enable secret scanning and push protection, and also non-provider patterns and validity checks when they are available for the repository.

We will enable CodeQL code scanning with the default setup and the default query suite, which analyses Python and GitHub Actions workflows.

The settings are documented in `docs/maintainers/security-settings.md`.

## Consequences

- Recognised secrets are rejected on push, whether or not the hooks ran.
- Security vulnerabilities in the code and in the workflows are reported as alerts and on pull requests.
- There is no CodeQL workflow to pin and update, and TypeScript will be analysed automatically when the runtime is added.
- The CodeQL configuration cannot be customised without moving to the advanced setup, which would need a new ADR.
- Code scanning results are not yet required by the `main` ruleset.
