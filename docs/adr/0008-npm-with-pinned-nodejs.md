# ADR-0008: Manage the runtime with npm and a pinned Node.js version

- **Status:** Accepted
- **Date:** 2026-11-07

## Context

The runtime in `runtime/` needs a JavaScript package manager for its development dependencies, such as the TypeScript compiler and the test runner, and to publish `@skama/runtime` to npm.

The alternatives considered were:

- npm, which ships with Node.js.
- pnpm or Yarn, which are faster or stricter but are usually pinned through Corepack, and Corepack is no longer bundled with Node.js from version 25.
- Bun or Deno, which would add a second runtime besides Node.js for contributors and CI.

The repository has a single JavaScript package, so the advantages of pnpm in large workspaces do not apply.

## Decision

We will use npm. The Node.js version is pinned in `runtime/.node-version`, which also pins the version of npm that ships with it. The lockfile `runtime/package-lock.json` is committed, and CI installs dependencies with `npm ci`, which fails if the lockfile and `package.json` disagree.

The exact Node.js version is chosen when the runtime tooling is set up. It must satisfy npm's trusted publishing requirements, which at the time of writing are npm 11.5.1 or later and Node.js 22.14.0 or later.

## Consequences

- Contributors to the runtime need only Node.js, with no extra tool to install.
- Local development and CI use the same Node.js and npm versions.
- Users of Skama do not need Node.js or npm at all, because the runtime is bundled in the Python package (ADR-0006).
- Installs are slower than with pnpm, which is acceptable for a single small package.
- Moving to another package manager later would need a new ADR.
