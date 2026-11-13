# ADR-0012: Reserve the package names with a single manual bootstrap release

- **Status:** Accepted
- **Date:** 2026-11-08

## Context

The packages are published as `skama` on PyPI and `@skama/runtime` on npm (ADR-0007). Until a first version exists, anyone can take those names.

Releases are meant to be published only from CI with trusted publishing, but the release workflow does not exist yet. PyPI can register a pending trusted publisher for a new project, but that does not reserve the name until the first upload. npm configures trusted publishers in the settings of a package that already exists.

npm also rejected the unscoped name `skama` as too similar to an existing package, so the runtime needs a scoped name.

## Decision

We will reserve both names with one manual release of version 0.0.1, which contains no functionality.

- `skama` 0.0.1 is uploaded to PyPI with an API token created for that upload and deleted right after it.
- `@skama/runtime` 0.0.1 is published to npm under the `skama` organization, with public access, from a short-lived session that is logged out right after it.
- The `0.0.0-stage` version that npm created as a registry placeholder during the first publish is deprecated, pointing users to 0.0.1 or later.

This is the only manual release. Every later release is published from CI with trusted publishing, as decided in a later ADR.

## Consequences

- Nobody else can register the names of the project's packages.
- No publishing credentials remain after the bootstrap.
- The runtime is published as `@skama/runtime`, which is the name users load from npm or a CDN.
- Version 0.0.1 cannot be reused on either registry, so the first real release is 0.1.0.
