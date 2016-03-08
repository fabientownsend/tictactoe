from enum import Enum

from computer import Computer
from human import Human
from marks_enum import Marks


class PlayersEnum(Enum):
    player_1 = 1
    player_2 = 2


class PlayersApplication:
    def create_players_type_game(self, type_game):
        if type_game == GameType.human_vs_human.value:
            self.player_1 = makeHuman(Marks.cross, self.game_interface)
            self.player_2 = makeHuman(Marks.nought, self.game_interface)
        elif type_game == GameType.human_vs_computer.value:
            self.player_1 = makeHuman(Marks.cross, self.game_interface)
            self.player_2 = makeComputer(Marks.nought)
        elif type_game == GameType.computer_vs_computer.value:
            self.player_1 = makeComputer(Marks.cross)
            self.player_2 = makeComputer(Marks.nought)

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
        if first_player_selected == PlayersEnum.player_1.value:
            self.current_player = self.player_1
        elif first_player_selected == PlayersEnum.player_2.value:
            self.current_player = self.player_2


class PlayersApplicationImp(PlayerApplication):
    def makeHuman(self, mark, game_interface):
        return Human(mark, game_interface)

    def makeComputer(self, mark):
        return Computer(mark)

