# Skama

Write your frontend in Python. Skama compiles it to lightweight JavaScript.

> **Status: early development.** Skama is not usable yet. The API shown below is the current design and will change.

## What is Skama

Skama is a frontend framework for Python developers. You write components in plain Python, with full support from your editor, type checker and linter. A compiler turns them into small JavaScript modules that run entirely in the browser, with no server round trip for each interaction and no Python interpreter to download.

## How it works

1. **Components in Python.** Components are written with an internal DSL that is valid Python, so autocompletion, pyright, mypy and ruff work out of the box.
2. **A compiler.** Skama parses the Python AST, validates the supported subset of Python, lowers it to its own intermediate representation and generates JavaScript.
3. **A small reactive runtime.** The generated code relies on signals for fine-grained reactivity. There is no virtual DOM. Each component runs once, and only the DOM nodes that depend on a changed signal are updated.

## A taste of the API

This is the current design and is not implemented yet.

```python
from skama import component, signal
from skama.html import button, div, p


@component
def Counter():
    count = signal(0)

    def increment():
        count.set(count() + 1)

    return div(
        p(f"Clicks: {count()}"),
        button("Add", on_click=increment),
    )
```

## Packages

| Package | Registry | Contents |
| --- | --- | --- |
| `skama` | PyPI | Compiler, Python API and command-line interface |
| `@skama/runtime` | npm | Browser runtime |

The runtime is bundled inside the Python package, so you will not need Node.js or npm to use Skama. The npm package is for loading the runtime from a CDN or integrating it into JavaScript projects.

## Contributing

Contributions are welcome. Please read the [contributing guide](CONTRIBUTING.md) and the [code of conduct](CODE_OF_CONDUCT.md) first.

## Security

Please report vulnerabilities privately as described in the [security policy](SECURITY.md).

## License

Skama is licensed under the [Apache License 2.0](LICENSE).
