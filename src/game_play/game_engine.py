from enum import Enum

from computer import Computer
from human import Human
from marks_enum import Marks
from players_application import PlayersApplicationImp


class GameEngine:
    def __init__(self, game_interface, game_policy, game_board):
        self.player = PlayersApplicationImp(game_interface)
        self.game_interface = game_interface
        self.game_policy = game_policy
        self.game_board = game_board
        self.game_over = False
        self.tie = False
        self.winner = None
        self.current_player = None

    def create_type_game(self):
        self.game_interface.display_type_game()
        self.player.create_players_type_game(self.get_type_game_selected())

    def get_type_game_selected(self):
        type_game = self.game_interface.get_type_game_selected()

        if type_game > 0 and type_game < 4:
            return type_game
        else:
            return self.get_type_game_selected()

    def define_first_player(self):
        self.game_interface.display_which_start()
        self.player.set_first_player(self.get_first_player_selected())

    def get_first_player_selected(self):
        first_player_selected = self.game_interface.get_first_player()

        if first_player_selected > 0 and first_player_selected < 3:
            return first_player_selected
        else:
            return self.get_first_player_selected()

    def play(self):
        while not self.game_over:
            game_board = self.game_board
            mark = self.player.current_player.mark

            self.game_interface.display_player_turn(mark.value)
            position = self.player.current_player.get_move(game_board)
            self.game_board.set_mark(position, mark)
            self.game_interface.display_board(game_board.board)

            if self.is_game_over(game_board.board):
                self.set_game_result(game_board.board)
                self.display_result()
            else:
                self.player.switch_current_player()

    def is_game_over(self, board):
        if (self.game_policy.win(board, self.player.current_player.mark) or
            self.game_policy.check_tie(board)):
            return True
        else:
            return False

    def set_game_result(self, board):
        self.game_over = True

        if self.game_policy.check_tie(board):
            self.tie = True
        elif self.game_policy.win(board, self.player.current_player.mark):
            self.winner = self.player.current_player

    def display_result(self):
        if self.tie:
            self.game_interface.display_tie()
        else:
            self.game_interface.display_winner(self.winner.mark.value)
