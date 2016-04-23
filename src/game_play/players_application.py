from enum import Enum

from computer import Computer
from human import Human
from marks_enum import Marks


class GameType(Enum):
    human_vs_human = 1
    human_vs_computer = 2
    computer_vs_computer = 3


class PlayersApplication():
    def __init__(self, game_interface):
        self.FIRST_PLAYER = 1
        self.game_interface = game_interface

    def create_players_type_game(self, type_game):
        if type_game == GameType.human_vs_human.value:
            self.player_1 = self.makeHuman(Marks.cross, self.game_interface)
            self.player_2 = self.makeHuman(Marks.nought, self.game_interface)
        elif type_game == GameType.human_vs_computer.value:
            self.player_1 = self.makeHuman(Marks.cross, self.game_interface)
            self.player_2 = self.makeComputer(Marks.nought)
        elif type_game == GameType.computer_vs_computer.value:
            self.player_1 = self.makeComputer(Marks.cross)
            self.player_2 = self.makeComputer(Marks.nought)

    def makeHuman(self, game_interface):
        raise NotImplementedError()

    def makeComputer(self):
        raise NotImplementedError()

    def switch_current_player(self):
        if self.current_player == self.player_1:
            self.current_player = self.player_2
        else:
            self.current_player = self.player_1

    def set_first_player(self, first_player_selected):
        if first_player_selected == self.FIRST_PLAYER:
            self.current_player = self.player_1
        else:
            self.current_player = self.player_2


class PlayersApplicationImp(PlayersApplication):
    def makeHuman(self, mark, game_interface):
        return Human(mark, game_interface)

    def makeComputer(self, mark):
        return Computer(mark)
