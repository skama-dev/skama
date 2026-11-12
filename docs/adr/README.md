# Architecture decision records

This folder records the significant decisions about Skama's architecture, tooling and process, with the context and the consequences of each one. The format follows [Michael Nygard's proposal](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions).

## Writing a new ADR

1. Copy [template.md](template.md) to `NNNN-short-title.md`, using the next free number.
2. Fill it in with the status `Proposed` and open a pull request. The discussion happens in the pull request.
3. Change the status to `Accepted` before merging, and add the ADR to the index below.

Accepted ADRs are not rewritten. To change a decision, write a new ADR and mark the old one as `Superseded by ADR-NNNN`. Numbers are never reused.

## Statuses

- **Proposed:** under discussion in a pull request.
- **Accepted:** the decision is in force.
- **Deprecated:** no longer applies and has no replacement.
- **Superseded:** replaced by a later ADR, which is linked.

## Index

| ADR | Title | Status |
| --- | --- | --- |
| [0001](0001-record-architecture-decisions.md) | Record architecture decisions | Accepted |
| [0002](0002-compile-python-components-to-javascript.md) | Compile Python components to JavaScript | Accepted |
| [0003](0003-fine-grained-reactivity-with-signals.md) | Use fine-grained reactivity with signals instead of a virtual DOM | Accepted |
| [0004](0004-internal-python-dsl.md) | Use an internal Python DSL as the only authoring format | Accepted |
| [0005](0005-compiler-intermediate-representation.md) | Compile through an intermediate representation | Accepted |
| [0006](0006-repository-layout.md) | Keep the Python package at the root and the runtime in its own folder | Accepted |
| [0007](0007-single-version-for-both-packages.md) | Release the Python and npm packages with a single version | Accepted |
| [0008](0008-npm-with-pinned-nodejs.md) | Manage the runtime with npm and a pinned Node.js version | Accepted |
