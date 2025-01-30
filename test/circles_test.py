from math import pi

from pytest import fixture

from src.circles import Circles


@fixture
def areas() -> list[list[int | float]]:
    return [
        [pi, 1],
        [0, 0],
        [(pi * 2.1**2), 2.1],
    ]


@fixture
def circs() -> list[list[int | float]]:
    return [
        [6.2831853, 1],
        [0, 0],
        [(pi * 2.1 * 2), 2.1],
    ]


def test_area(areas: list[list[int | float]]) -> None:
    circ = Circles(0)
    for i in areas:
        circ.radius = i[1]
        try:
            assert round(i[0], 2) == round(circ.area(), 2)
        except Exception:
            assert i[0] == i[1]


def test_circ(circs: list[list[int | float]]) -> None:
    circ = Circles(0)
    for i in circs:
        circ.radius = i[1]
        try:
            assert round(i[0], 2) == round(circ.circumference(), 2)
        except Exception:
            assert i[0] == i[1]
