# ADR-0002: Compile Python components to JavaScript

- **Status:** Accepted
- **Date:** 2026-11-01

## Context

Skama's goal is to let Python developers build frontends that run entirely in the browser. Browsers execute JavaScript natively, so Python code has to reach them in some form.

The alternatives considered were:

- Server-driven frameworks, such as Reflex, NiceGUI or Flet, where the application logic runs in a Python backend and most interactions make a round trip to the server.
- Running Python in the browser with WebAssembly, as PyScript and PuePy do on top of Pyodide or MicroPython, which means downloading an interpreter before the application can start.
- Compiling Python to JavaScript ahead of time.

## Decision

We will compile Python components to JavaScript ahead of time. Applications built with Skama run in the browser without a Python interpreter and without a server for each interaction. The compiler accepts a defined subset of Python and rejects code outside it with clear errors.

## Consequences

- Applications are small, start quickly and can be served as static files.
- Interactions are handled in the browser, with no server round trip.
- Python libraries with C extensions, such as NumPy or Pandas, cannot run in the browser.
- Only a subset of Python's semantics is supported, which has to be specified and documented.
- The project has to build and maintain a compiler, which is its main technical risk.
