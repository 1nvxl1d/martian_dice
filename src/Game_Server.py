from src.Dice import Dice
from src.Player import Player
from src.Hand import Hand

class Game_Server:
    dice_count = 13

    def new_game(self):
        Game_Server.dice_count = 13
        Hand.global_res = []
        Hand.can_chose_human = 1
        Hand.can_chose_cow = 1
        Hand.can_chose_chicken = 1