# ADR-0004: Use an internal Python DSL as the only authoring format

- **Status:** Accepted
- **Date:** 2026-11-02

## Context

Skama components need a way to describe the user interface. The options considered were:

- An internal domain-specific language: plain Python function calls, such as `div(p("Hello"), button("Add", on_click=increment))`.
- HTML-like templates, as in Vue or Svelte. They are familiar to frontend developers, but need a custom parser and a language server for autocompletion and type checking inside the templates, which took Vue and Svelte years to build.
- A hybrid, with logic in Python and the view in a separate template file, with the same tooling cost as templates.

Skama's users are Python developers, and its value is that they can stay in Python.

## Decision

We will use an internal Python DSL as the only format for writing components. Components are valid Python code built from functions for HTML elements, signals and control components. Skama will not provide a template syntax.

## Consequences

- Editors, autocompletion, pyright, mypy and ruff work from day one, without plugins or a custom language server.
- Component props can be declared with type hints and checked by the type checker.
- There is a single syntax to parse, document and maintain.
- Large views are harder to read than HTML. This is mitigated by the API design, with children as positional arguments and attributes as keywords, and by encouraging small components.
- Adding a template syntax later would require a new ADR. It would have to compile to the same intermediate representation (ADR-0005).
