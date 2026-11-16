# ADR-0015: Lint and format with Ruff and type check with mypy in strict mode

- **Status:** Accepted
- **Date:** 2026-11-15

## Context

The Python code needs a linter, a formatter and a type checker, run the same way by every contributor and by CI, so that reviews focus on design rather than style.

The compiler is written in Python. If it ever becomes too slow, the first option is to compile it with mypyc, which only works on code that mypy accepts and benefits from complete type annotations.

The alternatives considered were:

- Ruff as linter and formatter, or flake8, isort and Black as separate tools.
- Selecting Ruff rule families explicitly, or selecting `ALL` with exceptions, which enables new rules on every Ruff upgrade.
- mypy, pyright, or the newer ty and pyrefly as type checker.

## Decision

We will use Ruff as linter and formatter, with an explicit list of rule families in `pyproject.toml`, excluding the rules that the Ruff documentation lists as conflicting with its formatter.

We will type check `src/` and `tests/` with mypy in strict mode, targeting the oldest supported Python version (ADR-0013), with `warn_unreachable` and additional error codes enabled.

Both tools are development dependencies, pinned in `uv.lock`.

## Consequences

- Style is decided by the formatter, not discussed in reviews.
- Every function must have type annotations from the start, which keeps mypyc available as an option.
- Code is checked against the oldest supported Python version, even when contributors work with a newer one.
- New Ruff rules are only enabled by a deliberate change to the configuration.
- Strict typing makes some code more verbose, especially around untyped third-party libraries.
