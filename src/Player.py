from src.Hand import Hand

class Player:
    def __init__(self, name: str, hand: Hand, score: int = 0):
        self.name = name
        self.hand = hand
        self.score = score

    def __str__(self):
        return f"{self.name}({self.score}): {self.hand}"
