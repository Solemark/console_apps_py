from pytest import fixture

from src.calculator import Calculator


@fixture
def data() -> list[list[int]]:
    return [
        [5, 5],
        [5, -5],
        [-5, -5],
    ]


def test_add(data: list[list[int]]) -> None:
    calc = Calculator(0, 0)
    for i in data:
        (a, b) = (i[0], i[1])
        (calc.a, calc.b) = (a, b)
        assert calc.add() == a + b


def test_sub(data: list[list[int]]) -> None:
    calc = Calculator(0, 0)
    for i in data:
        (a, b) = (i[0], i[1])
        (calc.a, calc.b) = (a, b)
        assert calc.sub() == a - b


def test_mul(data: list[list[int]]) -> None:
    calc = Calculator(0, 0)
    for i in data:
        (a, b) = (i[0], i[1])
        (calc.a, calc.b) = (a, b)
        assert calc.mul() == a * b


def test_div(data: list[list[int]]) -> None:
    calc = Calculator(0, 0)
    for i in data:
        (a, b) = (i[0], i[1])
        (calc.a, calc.b) = (a, b)
        assert calc.sub() == a - b
