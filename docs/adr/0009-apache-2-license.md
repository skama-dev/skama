# ADR-0009: License Skama under the Apache License 2.0

- **Status:** Accepted
- **Date:** 2026-11-07

## Context

Skama needs a license before any code is published. The license is the hardest decision to reverse, because every contributor keeps the copyright of their contributions and changing the license later requires the agreement of all of them.

Skama is meant to be used in any kind of application, including commercial and closed-source ones, which rules out strong copyleft licenses such as the GPL.

The alternatives considered were:

- The MIT License, used by Pydantic, Ruff, Svelte and Vue. It is short and permissive, but it has no explicit patent grant.
- The Apache License 2.0, used by Reflex. It is permissive and adds an explicit patent license from every contributor, which ends for anyone who sues over patents in the work.
- The Mozilla Public License 2.0, a file-level copyleft that would require changes to Skama's own files to be shared, adding obligations that users of a frontend framework do not expect.

## Decision

We will license Skama under the Apache License 2.0. The full text lives in `LICENSE` at the root of the repository, and both packages declare the SPDX identifier `Apache-2.0` in their metadata.

Contributions are accepted under the same license, as section 5 of the license states, with a Developer Certificate of Origin sign-off on every commit and no contributor license agreement.

## Consequences

- Users can build any kind of application with Skama, including commercial and closed-source ones.
- Users and contributors are protected by the explicit patent license.
- Applications that ship the runtime redistribute Apache 2.0 code, so the runtime build must keep a license notice in its output.
- Apache 2.0 is compatible with GPLv3 but not with GPLv2-only projects, which cannot include Skama code.
- Changing the license later would need a new ADR and the agreement of every contributor.
