from enum import Enum, auto
from functools import partial
from random import randint


class Game(Enum):
    FGO = auto()
    AK = auto()
    GI = auto()


def roll(game: Game) -> str:
    """roll until you get the rare!"""
    play_fn = partial(__roll, game)
    match game:
        case Game.FGO:
            return play_fn(100, 300, 5)
        case Game.AK:
            return play_fn(50, 100, 6)
        case Game.GI:
            return play_fn(60, 90, 5)


def __roll(game: Game, rate: int, pity: int, rarity: int) -> str:
    """actually do the rolls!"""
    for i in range(1, pity + 1):
        if i == pity or rate == randint(1, rate):
            return f"it took {i}/{pity} rolls to get a {rarity}* in {game.name}"
