from typing import Any

from pytest import fixture

from src.swap_variables import swap


@fixture
def data() -> list[list[tuple[Any, Any]]]:
    return [
        [(2, 1), (1, 2)],
        [("abcd", "1234"), ("1234", "abcd")],
        [(True, False), (False, True)],
    ]


def test_swap_variables(data: list[list[tuple[Any, Any]]]) -> None:
    for row in data:
        exp, inp = row
        assert exp == swap(inp[0], inp[1])
