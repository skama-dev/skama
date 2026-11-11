# ADR-0003: Use fine-grained reactivity with signals instead of a virtual DOM

- **Status:** Accepted
- **Date:** 2026-11-01

## Context

A frontend framework has to update the page when the application's state changes. There are two main approaches:

- A virtual DOM, used by React and classic Vue. Each change re-runs the component's render function, builds a new tree and compares it with the previous one to decide what to update.
- Fine-grained reactivity, used by SolidJS and Svelte, and adopted by Vue's Vapor mode. State lives in signals, and each piece of the DOM subscribes to the signals it reads, so a change updates only the affected nodes.

Skama already has a compilation step (ADR-0002), which can work out at build time which DOM nodes depend on which signals.

## Decision

We will use fine-grained reactivity based on signals. Component functions run once, when the component is mounted. The compiler connects each signal to the DOM nodes that read it, and the runtime updates only those nodes when the signal changes. State is created with `signal` and derived with `computed`. Conditional rendering and lists are expressed with the `Show` and `For` control components.

## Consequences

- Updates touch only the DOM nodes that depend on the changed state, without diffing.
- The runtime stays small, because there is no virtual DOM implementation to ship.
- Developers do not need hook rules or manual memoisation.
- Plain Python `if` and `for` statements inside a view are evaluated only once, at mount time. Users must use `Show` and `For` for reactive structure, and the compiler should warn when a plain statement reads a signal.
- The mental model differs from React's, which can surprise developers who come from it.
