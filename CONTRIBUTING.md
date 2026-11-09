# Contributing to Skama

Thank you for your interest in Skama. The project is in early development, so the best way to start is to open an issue and discuss your idea before working on a large change.

## Code of conduct

Everyone taking part in this project is expected to follow the [code of conduct](CODE_OF_CONDUCT.md).

## Reporting bugs and proposing changes

- Use [GitHub issues](https://github.com/skama-dev/skama/issues) for bugs and feature requests.
- Do not report security vulnerabilities in public issues. Follow the [security policy](SECURITY.md) instead.

## Making a change

1. Fork the repository and create a branch named after the type of change and a short description, for example `fix/escape-text-nodes` or `docs/clarify-install`.
2. Keep each pull request focused on one logical change.
3. Write your commit messages following [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).
4. Sign off every commit (see below).
5. Open a pull request against `main` and fill in the description.

### Commit messages and pull request titles

Pull requests are merged with squash, and the pull request title becomes the commit message on `main`. Release notes and version numbers are generated from these messages, so the title must follow Conventional Commits:

```
<type>(<optional scope>): <description>
```

Common types are `feat`, `fix`, `docs`, `test`, `refactor`, `perf`, `build`, `ci` and `chore`. Scopes name the part of the project affected: `compiler`, `runtime`, `api`, `cli`, `devserver`, `docs` or `adr`.

### Developer Certificate of Origin

Every commit must include a `Signed-off-by` line. By adding it, you certify that you have the right to submit the contribution under the project's licence, as stated in the [Developer Certificate of Origin](https://developercertificate.org/). Git adds the line for you with:

```
git commit -s
```

We also recommend signing your commits with a GPG or SSH key so that GitHub shows them as verified.

## Development setup

The codebase is being bootstrapped. Instructions to set up the development environment will be added here together with the tooling.

## Licensing

Skama is licensed under the [Apache License 2.0](LICENSE). As stated in section 5 of the licence, any contribution you submit is licensed under the same terms.
