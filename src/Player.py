from src.Hand import Hand

import typing

class Player:
    def __init__(self, name: str, player_type: str, score: int = 0):
        self.player_type = player_type
        self.name = name
        self.score = score

    def __str__(self):
        return f"{self.name}({self.score})"

    def __eq__(self, other: typing.Self | str | dict):
        return (
                self.name == other.name
                and self.score == other.score
        )