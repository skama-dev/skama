# Security settings

These settings are configured in Settings > Advanced Security and are not stored in the repository. This page records what is enabled and how to verify it.

## Secret scanning

| Setting | Status |
| --- | --- |
| Secret scanning | Enabled |
| Push protection | Enabled |
| Non-provider patterns | Enabled when available |
| Validity checks | Enabled when available |

Push protection rejects pushes that contain a recognised secret, even when the pre-commit hooks were skipped or not installed.

## Dependabot

| Setting | Status |
| --- | --- |
| Dependabot alerts | Enabled |
| Dependabot security updates | Enabled |

Version updates are configured in `.github/dependabot.yml`.

## Code scanning

CodeQL runs with the default setup, managed by GitHub, with the default query suite. It analyses Python and GitHub Actions workflows on pull requests, on pushes to `main` and on a weekly schedule. New languages are added automatically when they appear in the repository.

## Verify the configuration

Run `gh api repos/skama-dev/skama --jq '.security_and_analysis'` and check that every listed feature reports `enabled`.

Run `gh api repos/skama-dev/skama/code-scanning/default-setup --jq '{state, query_suite, languages}'` and check that `state` is `configured` and `query_suite` is `default`.
