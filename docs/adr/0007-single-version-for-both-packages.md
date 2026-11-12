# ADR-0007: Release the Python and npm packages with a single version

- **Status:** Accepted
- **Date:** 2026-11-07

## Context

Skama publishes two packages: `skama` on PyPI and `@skama/runtime` on npm. The JavaScript that the compiler generates calls functions of the runtime, so a compiler and a runtime from different versions can be incompatible.

The alternatives considered were:

- A single version for both packages, released together.
- Independent versions for each package, with a compatibility matrix or version ranges between them.

## Decision

We will release both packages together, always with the same version number, from a single Git tag in the form `vX.Y.Z`. Every release publishes both packages, even when only one of them changed.

## Consequences

- The compatibility rule is trivial: the compiler and the runtime are compatible when their versions match.
- The Python package always bundles the runtime of its own version, so pip users can never mix versions.
- Users who load the runtime from npm or a CDN must use the same version as their compiler, which the documentation has to state clearly.
- Some releases of one package contain no changes of their own, only a version bump.
- How the release tooling updates the version in both packages is decided in a later ADR.
