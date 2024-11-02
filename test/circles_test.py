from math import pi

from pytest import fixture

from src.circles import get_area, get_circ


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
    for area in areas:
        assert round(area[0], 2) == round(get_area(area[1]), 2)


def test_circ(circs: list[list[int | float]]) -> None:
    for circ in circs:
        assert round(circ[0], 2) == round(get_circ(circ[1]), 2)
