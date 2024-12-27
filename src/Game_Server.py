from src.Player import Player
from src.Hand import Hand
from src.Game_state import Game_state

import enum
import random
import time

class GamePhase(enum.StrEnum):
    ROUND = 'Round'
    NEXT_PLAYER = "Switch current player"
    SCORING = 'Scoring'
    DECLARE_WINNER = "Declare a winner"
    GAME_END = "Game ended"

class Game_Server:
    def __init__(self, hand, game_state):
        self.game_state: Game_state = game_state
        self.hand: Hand = hand
        self.current_phase = GamePhase.ROUND
        self.player: Player = self.game_state.current_player()

    def run(self):
        print('start game')
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
        print('player', self.game_state.current_player(), 'turn')
        self.hand.round_start()
        k = 1
        if self.player.player_type == 'human':
            while k and self.hand.dice_count != 0:
                self.hand.roll_dice()
                self.hand.del_tanks()
                while True:
                    print(self.hand.res, self.hand.round_res)
                    print(self.player.player_type, self.game_state.current_player())
                    dice_choice = input('b/h/c/ch?\n')
                    if dice_choice == 'b':
                        break
                    elif dice_choice == 'h':
                        if self.hand.can_chose_human == 1 and 'h' in self.hand.res:
                            break
                        else:
                            print('cant chose human')
                    elif dice_choice == 'c':
                        if self.hand.can_chose_cow == 1 and 'c' in self.hand.res:
                            break
                        else:
                            print('cant chose cow')
                    elif dice_choice == 'ch':
                        if self.hand.can_chose_chicken == 1 and 'ch' in self.hand.res:
                            break
                        else:
                            print('cant chose chicken')
                    else:
                        print('incorrect input')
                if dice_choice == 'b':
                    self.hand.chose_beam()
                elif dice_choice == 'h':
                    self.hand.chose_human()
                elif dice_choice == 'c':
                    self.hand.chose_cow()
                elif dice_choice == 'ch':
                    self.hand.chose_chicken()
                while True:
                    cont = input('continue?')
                    if cont == 'no':
                        k = 0
                        break
                    elif cont == 'yes':
                        break
                    else:
                        print('incorrect input')
        elif self.player.player_type == 'bot':
            while self.hand.dice_count != 0:
                self.hand.roll_dice()
                self.hand.del_tanks()
                bot_choses = []
                if 'b' in self.hand.res:
                    bot_choses.append('b')
                if 'h' in self.hand.res and self.hand.can_chose_human == 1:
                    bot_choses.append('h')
                if 'c' in self.hand.res and self.hand.can_chose_cow == 1:
                    bot_choses.append('c')
                if 'ch' in self.hand.res and self.hand.can_chose_chicken == 1:
                    bot_choses.append('ch')
                if bot_choses == []:
                    break
                b_c = random.choice(bot_choses)
                print('bot choose', b_c)
                if b_c == 'b':
                    self.hand.chose_beam()
                elif b_c == 'h' and self.hand.can_chose_human == 1:
                    self.hand.chose_human()
                    bot_choses.remove('h')
                elif b_c == 'c':
                    self.hand.chose_cow()
                    bot_choses.remove('c')
                elif b_c == 'ch':
                    self.hand.chose_chicken()
                    bot_choses.remove('ch')
                print(self.hand.res, self.hand.round_res)
                time.sleep(3)
        print('scoring')
        return GamePhase.SCORING

    def scoring(self) -> GamePhase:
        if self.hand.round_res.count('t') > self.hand.round_res.count('b'):
            print('player', self.game_state.current_player(), 'score', self.player.score, 'points')
            return GamePhase.NEXT_PLAYER
        else:
            if ('h' in self.hand.round_res) and ('c' in self.hand.round_res) and ('ch' in self.hand.round_res):
                self.player.score += 3
            for i in range(len(self.hand.round_res)):
                if self.hand.round_res[i] == 'h' or self.hand.round_res[i] == 'c' or self.hand.round_res[i] == 'ch':
                    self.player.score += 1
            if self.player.score >= 25:
                print('Winner', self.game_state.current_player())
                return GamePhase.DECLARE_WINNER
            else:
                print('player', self.game_state.current_player(), 'score', self.player.score, 'points')
                return GamePhase.NEXT_PLAYER

    def next_player_phase(self) -> GamePhase:
        self.game_state.next_player()
        self.player = self.game_state.current_player()
        return GamePhase.ROUND
    def declare_winner_phase(self) -> GamePhase:
        print(f"{self.game_state.current_player()} is the winner!")
        return GamePhase.DECLARE_WINNER


hand = Hand(None, None, None, None, None, None, None)
player1 = Player('1', 'human')
player2 = Player('2', 'bot')
game_state = Game_state([player1, player2], None)
game = Game_Server(hand=hand, game_state=game_state)
Game_Server.run(game)