import pytest
from hello.main import greet


def test_greet_basic():
    assert greet("Shubham") == "Hello, Shubham!"


def test_greet_trims_whitespace():
    assert greet(" DevOps ") == "Hello, DevOps!"


def test_greet_empty_returns_world():
    assert greet("") == "Hello, world!"


def test_greet_requires_str():
    with pytest.raises(TypeError):
        greet(123)  # type: ignore[arg-type]
