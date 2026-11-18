# ADR-0017: Run CI in a single GitHub Actions workflow with an aggregate result

- **Status:** Accepted
- **Date:** 2026-11-17

## Context

The pre-commit hooks (ADR-0016) can be skipped, may not be installed by external contributors, and only test the development Python version. The project needs checks that run on GitHub for every pull request, test every supported Python version (ADR-0013), and cannot be bypassed.

Branch protection requires status checks by their exact name, so requiring every job of a test matrix means updating the protection rules whenever the matrix changes.

The alternatives considered were:

- A single workflow with an aggregate job that succeeds only when every other job succeeds.
- One workflow per tool, with every check required separately.

## Decision

We will run CI in a single workflow, `.github/workflows/ci.yml`, on every pull request and on every push to `main`.

- A `pre-commit` job runs the same hooks as contributors, skipping `no-commit-to-branch` and the staged-only gitleaks hook.
- A `tests` job runs the test suite on every supported Python version on Ubuntu, and on the development version on macOS and Windows.
- A `CI result` job succeeds only when every other job succeeds, and is the only check required by branch protection.

Actions are pinned to commit hashes, with the tag in a comment. The workflow token has no permissions by default, and each job requests only what it needs. Checkout does not persist credentials.

## Consequences

- Every change to `main` is checked in the same way, whether or not the author installed the hooks.
- Supported Python versions are actually tested, on the three major operating systems.
- Changing the test matrix does not require changing branch protection.
- Pinned actions do not change without a reviewed update, which Dependabot will propose.
- Secrets are not scanned by this workflow, which relies on GitHub secret scanning instead.
