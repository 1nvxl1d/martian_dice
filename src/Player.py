from src.Hand import Hand

import typing

class Player:
    def __init__(self, name: str, hand: Hand, score: int = 0):
        self.name = name
        self.hand = hand
        self.score = score

    def __str__(self):
        return f"{self.name}({self.score}): {self.hand}"

    def __eq__(self, other: typing.Self | str | dict):
        return (
                self.name == other.name
                and self.score == other.score
                and self.hand == other.hand
        )