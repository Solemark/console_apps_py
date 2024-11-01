from pytest import fixture

from src.calculator import add, div, mul, sub


@fixture
def data() -> list[list[int]]:
    return [
        [5, 5],
        [5, -5],
        [-5, -5],
    ]


def test_add(data: list[list[int]]) -> None:
    for i in data:
        a: int = i[0]
        b: int = i[1]
        assert add(a, b) == a + b


def test_sub(data: list[list[int]]) -> None:
    for i in data:
        a: int = i[0]
        b: int = i[1]
        assert sub(a, b) == a - b


def test_mul(data: list[list[int]]) -> None:
    for i in data:
        a: int = i[0]
        b: int = i[1]
        assert mul(a, b) == a * b


def test_div(data: list[list[int]]) -> None:
    for i in data:
        a: int = i[0]
        b: int = i[1]
        assert div(a, b) == a / b
