from src.Dice import Dice
from src.Player import Player
from src.Hand import Hand
from src.Game_state import Game_state

import enum

class GamePhase(enum.StrEnum):
    ROUND = 'Round'
    NEXT_PLAYER = "Switch current player"
    SCORING = 'Scoring'
    DECLARE_WINNER = "Declare a winner"
    GAME_END = "Game ended"

class Game_Server:
    def __init__(self, hand, game_state, player):
        self.game_state: Game_state = game_state
        self.hand: Hand = hand
        self.current_phase = GamePhase.ROUND
        self.player: Player = player

    def run(self):
        while self.current_phase != GamePhase.GAME_END:
            self.run_one_step()

    def run_one_step(self):
        phases = {
            GamePhase.ROUND: self.round,
            GamePhase.NEXT_PLAYER: self.next_player_phase,
            GamePhase.SCORING: self.scoring,
            GamePhase.DECLARE_WINNER: self.declare_winner_phase
        }
        self.current_phase = phases[self.current_phase]()

    def round(self) -> GamePhase:
        self.hand.round_start()
        k = 1
        while k or self.hand.dice_count != 0:
            self.hand.roll_dice()
            self.hand.del_tanks()
            dice_choice = input('')
            if dice_choice == 'b':
                self.hand.chose_beam()
                cont = input('c?')
                if cont == 'no':
                    k = 0
            elif dice_choice == 'h':
                self.hand.chose_human()
                cont = input('c?')
                if cont == 'no':
                    k = 0
            elif dice_choice == 'c':
                self.hand.chose_cow()
                cont = input('c?')
                if cont == 'no':
                    k = 0
            elif dice_choice == 'ch':
                self.hand.chose_chicken()
                cont = input('c?')
                if cont == 'no':
                    k = 0
        return GamePhase.SCORING

    def scoring(self) -> GamePhase:
        if self.hand.round_res.count('t') > self.hand.round_res.count('b'):
            return GamePhase.NEXT_PLAYER
        else:
            if ('h' in self.hand.round_res) and ('c' in self.hand.round_res) and ('ch' in self.hand.round_res):
                self.player.score += 3
            for i in range(len(self.hand.round_res)):
                if self.hand.round_res[i] == 'h' or self.hand.round_res[i] == 'c' or self.hand.round_res[i] == 'ch':
                    self.player.score += 1
            if self.player.score >= 25:
                return GamePhase.DECLARE_WINNER
            else:
                return GamePhase.NEXT_PLAYER

    def next_player_phase(self) -> GamePhase:
        self.game_state.next_player()
        return GamePhase.ROUND
    def declare_winner_phase(self) -> GamePhase:
        print(f"{self.game_state.current_player()} is the winner!")
        return GamePhase.DECLARE_WINNER