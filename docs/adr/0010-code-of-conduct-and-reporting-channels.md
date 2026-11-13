# ADR-0010: Adopt Contributor Covenant 3.0 and project-owned reporting channels

- **Status:** Accepted
- **Date:** 2026-11-08

## Context

An open source project needs a code of conduct, a private channel to report conduct problems and a private channel to report vulnerabilities, before it invites contributions.

The alternatives considered for the code of conduct were:

- Contributor Covenant 3.0, the current version of the most widely adopted code of conduct.
- Contributor Covenant 2.1, still used by many projects, but superseded by 3.0.
- Writing our own code of conduct, which takes effort to get right and is less familiar to contributors.

The alternatives considered for the reporting addresses were:

- A maintainer's personal email address, which exposes it publicly and has to change whenever maintainers change.
- Addresses under a project domain that forward to the maintainers, which stay the same when maintainers change.

## Decision

We will adopt Contributor Covenant 3.0 as `CODE_OF_CONDUCT.md`. The text is unchanged except for the reporting instructions, which point to `conduct@skama.org` and to GitHub's abuse reporting for reports about a maintainer, and an adopter's note in the enforcement section, which was removed.

Vulnerabilities are reported through GitHub's private vulnerability reporting, with `security@skama.org` as the alternative channel, as described in `SECURITY.md`.

Both addresses forward to the maintainers through the project domain (ADR-0011).

## Consequences

- Contributors find a familiar code of conduct with a clear way to report problems.
- No personal address of a maintainer is published.
- When maintainers change, only the forwarding rules change, not the published addresses.
- While the project has a single maintainer, reports about that maintainer can only go to GitHub.
- Moving to a later version of the Contributor Covenant would need a new ADR.
