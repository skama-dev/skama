# ADR-0013: Support the Python versions maintained by CPython and pin the development versions

- **Status:** Accepted
- **Date:** 2026-11-14

## Context

Skama runs on the user's Python interpreter, and the compiler reads components with the `ast` module of that interpreter, so the supported Python versions decide who can install Skama and which syntax the compiler must understand. Node.js is only needed to develop, test and publish the runtime (ADR-0008), never by users.

At the time of writing, CPython maintains versions 3.11 to 3.15. Version 3.10 reached its end of life on 2026-10-01, although Reflex, Pydantic and NiceGUI still require Python 3.10 or later.

The alternatives considered for the supported Python versions were:

- Every version that CPython still maintains, which gives users the widest choice.
- The window of Scientific Python's SPEC 0, which supports each version for three years and today starts at 3.13.
- A fixed minimum, such as 3.12, with no rule for when to raise it.

For Node.js, version 26 entered Active LTS on 2026-10-28 and is supported until 2029-04-30, while version 24 is in Maintenance LTS until 2028-04-30.

## Decision

We will support every Python version that CPython maintains, as listed in the Python Developer's Guide. A new version is supported from its first release, and a version that reaches its end of life is dropped in the next minor release of Skama. The `requires-python` field, the PyPI classifiers and the CI test matrix follow this rule.

Contributors develop with Python 3.14, pinned in `.python-version`. It is the newest version with a full year of releases, and it moves forward once a newer version has completed its first year.

The runtime is developed, tested and published with Node.js 26 LTS. The exact version is pinned in `runtime/.node-version`, which is 26.13.0 at the time of writing. The project moves to the next LTS line once it enters Active LTS.

## Consequences

- Users can install Skama on any Python version that still receives security fixes.
- CI tests five Python versions, which makes each run longer.
- The compiler's own code cannot use syntax or standard library features newer than the oldest supported version.
- Every October, a new Python version has to be added and an end-of-life one removed, and the Node.js line has to be reviewed.
- Users of a dropped Python version keep getting the last compatible release of Skama, because installers respect `requires-python`.
