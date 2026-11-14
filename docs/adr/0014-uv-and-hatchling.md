# ADR-0014: Manage the Python project with uv and build it with hatchling

- **Status:** Accepted
- **Date:** 2026-11-14

## Context

The Python package needs a tool to manage the virtual environment and the development dependencies, a lockfile so that contributors and CI install the same versions, and a build backend to produce the wheel and the source distribution.

The wheel has to contain the compiled runtime in `src/skama/_runtime/`, which is generated during the build and ignored by git (ADR-0006).

The alternatives considered for the build backend were:

- hatchling, which supports build hooks and can include files ignored by git through its `artifacts` option.
- uv_build, which is fast but, according to its documentation, only supports pure Python code and recommends hatchling when build scripts are needed.
- setuptools, which can do everything needed but requires more configuration.

## Decision

We will manage the Python project with uv. Development dependencies are declared in `[dependency-groups]` in `pyproject.toml`, and the lockfile `uv.lock` is committed. The minimum uv version is set with `required-version`.

We will build the package with hatchling, declared in `[build-system]`.

## Consequences

- Contributors need only uv, which also installs the pinned Python version (ADR-0013).
- Every contributor and CI job installs exactly the versions in `uv.lock`.
- The compiled runtime can be produced by a hatchling build hook and included in the wheel.
- Users who install Skama with pip are not affected, because both tools follow the standard `pyproject.toml` format.
