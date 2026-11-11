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
