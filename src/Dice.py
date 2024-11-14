class Dice:
    SIDES = ['t', 'b', 'b', 'h', 'c', 'ch']

    def __init__(self, side: str):
        if side not in Dice.SIDES:
            raise ValueError
        self.side = side

    def __repr__(self):
        return f'{self.side}'

    def __eq__(self, other):
        if isinstance(other, str):
            other = Dice.load(other)
        return self.side == other.side
