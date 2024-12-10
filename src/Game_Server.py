from src.Dice import Dice
from src.Player import Player
from src.Hand import Hand
from src.Game_state import Game_state

import enum

class GamePhase(enum.StrEnum):
    ROUND = 'Round'
    NEXT_PLAYER = "Switch current player"
    DECLARE_WINNER = "Declare a winner"
    GAME_END = "Game ended"

class Game_Server:
    def __init__(self):
        self.current_phase = GamePhase.ROUND

    def run(self):
        while self.current_phase != GamePhase.GAME_END:
            self.run_one_step()

    def run_one_step(self):
        phases = {
            GamePhase.ROUND: self.round,
            GamePhase.NEXT_PLAYER: self.next_player_phase,
            GamePhase.DECLARE_WINNER: self.declare_winner_phase
        }
        self.current_phase = phases[self.current_phase]()

    def round(self) -> GamePhase:
        self.Hand.round_start()
        k = 1
        while k:
            self.Hand.roll_dice()
            self.Hand.del_tanks()
            dice_choice = input('')
            if dice_choice == 'b':
                self.Hand.chose_beam()
                cont = input('c?')
                if cont == 'no':
                    k = 0
            elif dice_choice == 'h':
                self.Hand.chose_human()
                cont = input('c?')
                if cont == 'no':
                    k = 0
            elif dice_choice == 'c':
                self.Hand.chose_cow()
                cont = input('c?')
                if cont == 'no':
                    k = 0
            elif dice_choice == 'ch':
                self.Hand.chose_chicken()
                cont = input('c?')
                if cont == 'no':
                    k = 0
        return GamePhase.NEXT_PLAYER

    def next_player_phase(self) -> GamePhase:
        self.Game_state.next_player()
        return GamePhase.DECLARE_WINNER
    def declare_winner_phase(self) -> GamePhase:
        print(f"{self.Game_state.current_player()} is the winner!")
        return GamePhase.DECLARE_WINNER