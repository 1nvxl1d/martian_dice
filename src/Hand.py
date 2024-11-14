from src.Dice import Dice
from src.Game_Server import Game_Server

import random

class Hand:
    res = []
    global_res = []
    can_chose_human = 1
    can_chose_cow = 1
    can_chose_chicken = 1

    def roll_dice(self):
        Hand.res = [random.choice(Dice.SIDES) for _ in range(Game_Server.dice_count)]
        return Hand.res

    def del_tanks(self):
        Game_Server.dice_count -= Hand.res.count('t')
        for _ in range(Hand.res.count('t')):
            Hand.global_res.append('t')

    def chose_beam(self):
        Game_Server.dice_count -= Hand.res.count('b')
        for _ in range(Hand.res.count('b')):
            Hand.global_res.append('b')

    def chose_human(self):
        Hand.can_del_human = 0
        Game_Server.dice_count -= Hand.res.count('h')
        for _ in range(Hand.res.count('h')):
            Hand.global_res.append('h')

    def chose_cow(self):
        Hand.can_chose_cow = 0
        Game_Server.dice_count -= Hand.res.count('c')
        for _ in range(Hand.res.count('c')):
            Hand.global_res.append('c')

    def chose_chicken(self):
        Hand.can_chose_chicken = 0
        Game_Server.dice_count -= Hand.res.count('ch')
        for _ in range(Hand.res.count('ch')):
            Hand.global_res.append('ch')