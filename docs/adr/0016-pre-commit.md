# ADR-0016: Run the checks with pre-commit before every commit

- **Status:** Accepted
- **Date:** 2026-11-16

## Context

The project has a formatter, a linter and a type checker (ADR-0015), but they only help if they run before every commit. Some mistakes are not caught by any of them, such as a leaked secret, an unresolved merge conflict or a commit made directly on `main`.

The alternatives considered for the hook manager were:

- pre-commit, the reference tool with a large ecosystem of hooks.
- prek, a faster and compatible reimplementation that was still at version 0.5 at the time of writing.
- lefthook, which uses its own configuration format and cannot reuse pre-commit hooks.

The alternatives considered for running Ruff and mypy were:

- Local hooks that run the tools with `uv run`, using the versions in `uv.lock`.
- The upstream `ruff-pre-commit` and `mirrors-mypy` repositories, which duplicate the tool versions and run mypy in an isolated environment without the project's dependencies.

## Decision

We will use pre-commit, installed as a development dependency, with its configuration in `.pre-commit-config.yaml`.

Remote hooks are pinned to commit hashes, with the tag in a comment. They include the basic file checks from `pre-commit-hooks`, a block on commits to `main`, and gitleaks to detect secrets.

Ruff and mypy run as local hooks through `uv run --locked`, so contributors, pre-commit and CI use the same versions.

## Consequences

- Formatting, linting, typing and secret detection run on every commit, before anything reaches GitHub.
- Tool versions are defined once, in `uv.lock`.
- Each contributor has to install the hooks once per clone with `uv run pre-commit install`.
- The first run is slow, because pre-commit downloads the hooks and builds gitleaks.
- CI runs the same hooks, but must skip `no-commit-to-branch` when it checks `main`.
- Hooks can be bypassed with `git commit --no-verify`, so CI remains the final gate.
