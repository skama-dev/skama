# ADR-0006: Keep the Python package at the root and the runtime in its own folder

- **Status:** Accepted
- **Date:** 2026-11-07

## Context

Skama is made of a Python package, which contains the compiler, the public API and the command-line interface, and a JavaScript runtime written in TypeScript (ADR-0002, ADR-0003). Both live in the same repository, so the layout has to serve two toolchains.

The alternatives considered were:

- The Python package at the root, with the runtime in a subfolder. This is the layout of Bokeh, and essentially of Reflex and NiceGUI, which are Python packages first.
- A symmetric monorepo with `packages/skama/` and `packages/runtime/`, as in ipywidgets, which publishes several npm packages used on their own.
- Several Python distributions, such as a separate compiler package, which multiplies versions and releases without a current need.

Users install Skama with `pip install skama`, so the Python package is the product. The npm package is a secondary channel.

## Decision

We will keep the Python package at the root of the repository, using the `src/` layout (`src/skama/`), and the TypeScript runtime in `runtime/`, with its own `package.json` and lockfile.

The build compiles the runtime and places the result inside the Python package, in `src/skama/_runtime/`. That folder is generated and is not tracked by git. Tests, examples and documentation live at the root, in `tests/`, `examples/` and `docs/`.

## Consequences

- The repository reflects that Skama is a Python package, which is what contributors and users expect to find.
- The `src/` layout makes tests run against the installed package rather than the source tree, which catches packaging mistakes, such as a missing runtime file in the wheel.
- The runtime cannot fall out of sync with its source, because the compiled copy is never committed.
- Python tooling runs from the root and the JavaScript tooling from `runtime/`, so dependency updates and CI jobs have to cover both folders.
- Building the Python package requires building the runtime first.
- Moving to a symmetric monorepo later would need a new ADR.
