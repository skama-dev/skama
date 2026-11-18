# ADR-0018: Lint GitHub Actions workflows with actionlint and zizmor

- **Status:** Accepted
- **Date:** 2026-11-18

## Context

GitHub Actions workflows run with access to the repository and, later, with permission to publish packages. Mistakes in them often fail silently, and insecure patterns such as template injection let untrusted input run code on the runners. The existing checks validate YAML syntax but not workflow semantics or security.

The alternatives considered were:

- Running actionlint and zizmor as pre-commit hooks, so they run locally and in the CI `pre-commit` job.
- A separate CI job for each tool, which only reports problems after a push.
- Using only one of the tools, although actionlint checks correctness and zizmor checks security.

## Decision

We will run actionlint and zizmor as pre-commit hooks, pinned to commit hashes like the other remote hooks (ADR-0016).

actionlint uses shellcheck to check the scripts in `run` steps when it is installed. It is preinstalled on the Ubuntu runners, and contributors install it locally.

zizmor runs in offline mode with its default persona.

## Consequences

- Workflow mistakes and insecure patterns are caught before they reach GitHub, and again in CI.
- Every new workflow, including the release workflow, is audited from its first commit.
- Contributors who change workflows need shellcheck installed to get the same results as CI.
- Audits that need the GitHub API, such as detecting impostor commits, do not run in offline mode.
