from src.Dice import Dice

import random

class Hand:
    def __init__(self, hand: str, res: str, round_res: str, dice_count: int, can_chose_human: int, can_chose_chicken: int, can_chose_cow: int):
        self.hand = hand
        self.res = res
        self.round_res = round_res
        self.dice_count = dice_count
        self.can_chose_human = can_chose_human
        self.can_chose_chicken = can_chose_chicken
        self.can_chose_cow = can_chose_cow

    def round_start(self):
        self.dice_count = 13
        self.round_res = []
        self.can_chose_human = 1
        self.can_chose_cow = 1
        self.can_chose_chicken = 1
        self.res = []

    def roll_dice(self):
        self.res = [random.choice(Dice.SIDES) for _ in range(self.dice_count)]
        return self.res

    def del_tanks(self):
        self.dice_count -= self.res.count('t')
        for _ in range(self.res.count('t')):
            self.round_res.append('t')
            self.res.remove('t')

    def chose_beam(self):
        self.dice_count -= self.res.count('b')
        for _ in range(self.res.count('b')):
            self.round_res.append('b')
            self.res.remove('b')

    def chose_human(self):
        self.can_chose_human = 0
        self.dice_count -= self.res.count('h')
        for _ in range(self.res.count('h')):
            self.round_res.append('h')
            self.res.remove('h')

    def chose_cow(self):
        self.can_chose_cow = 0
        self.dice_count -= self.res.count('c')
        for _ in range(self.res.count('c')):
            self.round_res.append('c')
            self.res.remove('c')

    def chose_chicken(self):
        self.can_chose_chicken = 0
        self.dice_count -= self.res.count('ch')
        for _ in range(self.res.count('ch')):
            self.round_res.append('ch')
            self.res.remove('ch')