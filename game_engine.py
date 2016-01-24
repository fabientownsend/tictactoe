from enum import Enum

from computer import Computer
from game_board import GameBoard
from human import Human
from marks_enum import Marks


class GameType(Enum):
    human_vs_human = 1
    human_vs_computer = 2
    computer_vs_computer = 3


class PlayersEnum(Enum):
    player_1 = 1
    player_2 = 2


class GameEngine:
    def __init__(self, console, game_policy, board):
        self.console = console
        self.game_policy = game_policy
        self.board = board

        self.game_over = False
        self.tie = False
        self.winner = None
        self.current_player = None

    def create_type_game(self):
        self.console.display_type_game()
        type_game = self.get_type_game_selected()
        self.create_players_type_game(type_game)

    def get_type_game_selected(self):
        while True:
            type_game = self.console.type_game_selected()

            if type_game > 0 and type_game < 4:
                break

        return type_game

    def create_players_type_game(self, type_game):
        if type_game == GameType.human_vs_human.value:
            self.player_1 = Human(Marks.cross, self.console)
            self.player_2 = Human(Marks.nought, self.console)
        elif type_game == GameType.human_vs_computer.value:
            self.player_1 = Human(Marks.cross, self.console)
            self.player_2 = Computer(Marks.nought)
        elif type_game == GameType.computer_vs_computer.value:
            self.player_1 = Computer(Marks.cross)
            self.player_2 = Computer(Marks.nought)

    def define_first_player(self):
        self.console.display_which_start()
        first_player_selected = self.get_first_player_selected()
        self.set_first_player(first_player_selected)

    def get_first_player_selected(self):
        while True:
            first_player_selected = self.console.get_first_player()

            if first_player_selected > 0 and first_player_selected < 3:
                break

        return first_player_selected


    def set_first_player(self, first_player_selected):
        if first_player_selected == PlayersEnum.player_1.value:
            self.current_player = self.player_1
        elif first_player_selected == PlayersEnum.player_2.value:
            self.current_player = self.player_2

    def play(self):
        while not self.game_over:
            board = self.board
            mark = self.current_player.mark

            self.console.display_player_turn(mark.value)
            position = self.current_player.get_move(board)
            self.board.set_mark(position, mark)
            self.console.display_board(board.board)

            if self.is_game_over(board.board):
                self.display_result()
            else:
                self.switch_current_player()

    def is_game_over(self, board):
        if self.game_policy.win(board, self.current_player.mark):
            self.winner = self.current_player
            self.game_over = True

            return True
        elif self.game_policy.check_tie(board):
            self.tie = True
            self.game_over = True

            return True
        else:
            False

    def display_result(self):
        if self.tie:
            self.console.display_tie()
        else:
            self.console.display_winner(self.winner.mark.value)

    def switch_current_player(self):
        if self.current_player == self.player_1:
            self.current_player = self.player_2
        else:
            self.current_player = self.player_1
