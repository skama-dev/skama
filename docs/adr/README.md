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
| [0009](0009-apache-2-license.md) | License Skama under the Apache License 2.0 | Accepted |
| [0010](0010-code-of-conduct-and-reporting-channels.md) | Adopt Contributor Covenant 3.0 and project-owned reporting channels | Accepted |
| [0011](0011-skama-org-domain-on-cloudflare.md) | Register skama.org on Cloudflare Registrar | Accepted |
| [0012](0012-bootstrap-package-publication.md) | Reserve the package names with a single manual bootstrap release | Accepted |
| [0013](0013-supported-python-and-nodejs-versions.md) | Support the Python versions maintained by CPython and pin the development versions | Accepted |
| [0014](0014-uv-and-hatchling.md) | Manage the Python project with uv and build it with hatchling | Accepted |
| [0015](0015-ruff-and-mypy.md) | Lint and format with Ruff and type check with mypy in strict mode | Accepted |
| [0016](0016-pre-commit.md) | Run the checks with pre-commit before every commit | Accepted |
| [0017](0017-ci-workflow.md) | Run CI in a single GitHub Actions workflow with an aggregate result | Accepted |
| [0018](0018-workflow-linters.md) | Lint GitHub Actions workflows with actionlint and zizmor | Accepted |
| [0019](0019-main-branch-ruleset.md) | Protect main with a repository ruleset | Accepted |
| [0020](0020-dependabot.md) | Keep dependencies up to date with Dependabot | Accepted |
| [0021](0021-secret-scanning-and-codeql.md) | Enable secret scanning with push protection and CodeQL default setup | Accepted |
