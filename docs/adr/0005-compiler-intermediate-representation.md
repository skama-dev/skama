# ADR-0005: Compile through an intermediate representation

- **Status:** Accepted
- **Date:** 2026-11-02

## Context

The compiler has to turn Python source code into JavaScript (ADR-0002) wired for fine-grained reactivity (ADR-0003). Translating the Python syntax tree directly into JavaScript would tie the input syntax to the output code: every optimisation, every new output target, such as server-side rendering, and every change in either language would affect the whole compiler.

## Decision

We will build the compiler in three stages:

1. **Frontend.** Parses the source with Python's `ast` module, validates that it uses only the supported subset of Python, and reports errors with line and column.
2. **Intermediate representation (IR).** Skama's own model of the program in its own concepts: components, signals, computed values, dependencies between them and DOM nodes.
3. **Code generation.** Produces JavaScript from the IR.

The IR is the internal contract between the stages. It is not part of Skama's public API.

## Consequences

- Each stage can be developed and tested on its own. In particular, the generated JavaScript can be checked with golden tests.
- Optimisations, new output targets and, if ever accepted, other input syntaxes plug into the IR without rewriting the other stages.
- Dependency analysis happens on the IR, where it is simpler than on the Python syntax tree.
- There is more code to write, and the IR itself has to be designed carefully, which is part of the specification phase.
