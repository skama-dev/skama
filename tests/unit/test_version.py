import tomllib
from pathlib import Path

import skama

PYPROJECT = Path(__file__).resolve().parents[2] / "pyproject.toml"


def test_version_matches_pyproject() -> None:
    with PYPROJECT.open("rb") as file:
        expected = tomllib.load(file)["project"]["version"]

    assert skama.__version__ == expected
