# Security Policy

## Supported versions

Skama is in early development. Security fixes are released only for the latest published version. The Python package `skama` and the npm package `@skama/runtime` share version numbers, and both are covered by this policy.

| Version | Supported |
| --- | --- |
| Latest 0.x release | Yes |
| Older releases | No |

When Skama reaches 1.0, this section will describe which release lines receive security fixes and for how long.

## Reporting a vulnerability

Please do not report security vulnerabilities through public GitHub issues, discussions or pull requests.

Report them privately through GitHub at https://github.com/skama-dev/skama/security/advisories/new. If you cannot use GitHub, email security@skama.org instead.

Please include as much of the following as you can:

- The affected package (`skama` or `@skama/runtime`) and version.
- A description of the vulnerability and its impact.
- Steps to reproduce it, or a proof of concept.
- Any known mitigations or workarounds.

## What to expect

- You will receive an acknowledgement within 7 days.
- We will share an initial assessment within 14 days, including whether we consider the report a vulnerability.
- We aim to release a fix within 90 days of the report and will agree the disclosure date with you.
- Fixed vulnerabilities are published as GitHub Security Advisories, with a CVE when appropriate. You will be credited unless you prefer to remain anonymous.

## Scope

In scope:

- The compiler, including the JavaScript it generates (for example, missing escaping that leads to cross-site scripting).
- The browser runtime.
- The command-line interface and the development server.
- The release process and the published packages.

Out of scope:

- Vulnerabilities in applications built with Skama that are caused by the application's own code.
- Vulnerabilities in third-party dependencies that do not affect Skama. Please report those to the dependency's maintainers.
- Exposing the development server to untrusted networks. It is meant for local development only.
