"""Tiny demo module with a CLI and a function to test."""
from __future__ import annotations

import sys


def greet(name: str) -> str:
    """Return a greeting for `name`."""
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    name = name.strip()
    if not name:
        return "Hello, world!"
    return f"Hello, {name}!"


def main(argv: list[str] | None = None) -> int:
    """CLI entrypoint."""
    argv = list(sys.argv[1:] if argv is None else argv)
    name = argv[0] if argv else "world"
    print(greet(name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
