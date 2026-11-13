# ADR-0011: Register skama.org on Cloudflare Registrar

- **Status:** Accepted
- **Date:** 2026-11-08

## Context

The project needs its own domain for the reporting addresses (ADR-0010) and, later, for the website and its `security.txt` file.

The `skama.dev` domain was not available. The `.org` top-level domain is the usual choice for non-commercial open source projects.

The alternatives considered for the registrar were:

- Cloudflare Registrar, which sells domains at cost and includes DNS, one-click DNSSEC and free email forwarding.
- Amazon Route 53, which also offers registration and DNS, but needs a separate service to forward email.

## Decision

We will use `skama.org`, registered on Cloudflare Registrar, with its DNS on Cloudflare. The domain is protected with the registrar transfer lock and DNSSEC.

Cloudflare Email Routing forwards `conduct@skama.org` and `security@skama.org` to the maintainers. The domain only receives email, and its SPF, DKIM and DMARC records, with a DMARC policy of `p=reject` and strict alignment, tell receiving servers to reject any message that claims to come from `skama.org` without passing those checks.

## Consequences

- The project has a stable domain for its addresses and future website.
- Nobody can send convincing email impersonating `skama.org`.
- Cloudflare Registrar requires Cloudflare DNS, so moving DNS elsewhere means transferring the domain to another registrar first.
- The domain must be renewed every year. If it expires, the reporting addresses stop working, so automatic renewal must stay enabled.
- The Cloudflare account that owns the domain becomes a critical asset and must be protected with strong two-factor authentication.
