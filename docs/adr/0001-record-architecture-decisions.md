# ADR-0001: Record architecture decisions

- **Status:** Accepted
- **Date:** 2026-11-11

## Context

Skama is a long-term open source project. Several significant decisions have already been made, such as compiling Python components to JavaScript, using signals instead of a virtual DOM and choosing the licence. They were discussed outside the repository, so contributors cannot see why the project is the way it is, and a decision could be reversed without knowing the reasons behind it.

The alternatives considered were Michael Nygard's lightweight format, the more structured MADR 4.0 template, and free-form documents in `docs/`.

## Decision

We will record every significant decision about architecture, tooling and process as an architecture decision record in `docs/adr/`, using Michael Nygard's format with a status and a date.

ADRs are numbered sequentially, reviewed in pull requests and never rewritten once accepted. A changed decision gets a new ADR that supersedes the old one. Decisions made before this ADR are recorded retroactively, with the date on which each one was made.

## Consequences

- The reasons behind the project's design live next to the code and can be reviewed like any other change.
- New contributors and future maintainers can understand past decisions before proposing changes.
- Writing an ADR adds some effort to significant changes. Keeping the format short limits that cost.
- The history of superseded ADRs shows how the project's thinking evolved.
