from typing import Callable

from pytest import fixture

from src.filters import Filters

INP: list[int | float] = [0, 1, 2, 3, -4, 5, 6, 7, -8, 9, 10, -11]
type Func = Callable[[list[int | float]], list[int | float]]


@fixture
def exp() -> list[list[int | float]]:
    return [
        [0, 1, 2, 3, 5, 6, 7, 9, 10],
        [0, -4, -8, -11],
        [1, 3, 5, 7, 9, -11],
        [0, 2, -4, 6, -8, 10],
    ]


def test_filter_funcs(exp: list[list[int | float]]) -> None:
    fil = Filters(INP)
    assert exp[0] == fil.negative()
    assert exp[1] == fil.positive()
    assert exp[2] == fil.odds()
    assert exp[3] == fil.evens()
