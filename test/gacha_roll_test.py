from pytest import fixture

from src.gacha_roll import Game, roll


@fixture
def data() -> list[str]:
    return [Game.FGO, Game.AK, Game.GI]


def test_gacha_roll(data: list[str]) -> None:
    for i in data:
        assert i.name in roll(i)
