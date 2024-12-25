from src.Hand import Hand
from src.Player import Player


class Game_state:
    def __init__(
            self, players: list[Player], hand: Hand, current_player: int = 0
    ):
        self.players: list[Player] = players
        self.hand: Hand = hand
        self.__current_player: int = current_player

    def current_player(self) -> Player:
        return self.players[self.__current_player]

    def next_player(self):
        n = len(self.players)
        self.__current_player = (self.__current_player + 1) % n