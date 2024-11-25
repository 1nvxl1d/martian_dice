from src.Dice import Dice
from src.Game_Server import Game_Server

import random

class Hand:
    res = []
    round_res = []
    can_chose_human = 1
    can_chose_cow = 1
    can_chose_chicken = 1
    dice_count = 13

    def roll_dice(self):
        Hand.res = [random.choice(Dice.SIDES) for _ in range(Hand.dice_count)]
        return Hand.res

    def del_tanks(self):
        Hand.dice_count -= Hand.res.count('t')
        for _ in range(Hand.res.count('t')):
            Hand.round_res.append('t')

    def chose_beam(self):
        Hand.dice_count -= Hand.res.count('b')
        for _ in range(Hand.res.count('b')):
            Hand.round_res.append('b')

    def chose_human(self):
        Hand.can_chose_human = 0
        Hand.dice_count -= Hand.res.count('h')
        for _ in range(Hand.res.count('h')):
            Hand.round_res.append('h')

    def chose_cow(self):
        Hand.can_chose_cow = 0
        Hand.dice_count -= Hand.res.count('c')
        for _ in range(Hand.res.count('c')):
            Hand.round_res.append('c')

    def chose_chicken(self):
        Hand.can_chose_chicken = 0
        Hand.dice_count -= Hand.res.count('ch')
        for _ in range(Hand.res.count('ch')):
            Hand.round_res.append('ch')