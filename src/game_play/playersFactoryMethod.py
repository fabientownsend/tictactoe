
class PlayerApplication:
    def create_players_type_game(self, type_game):
        if type_game == GameType.human_vs_human.value:
            self.player_1 = Human(Marks.cross, self.game_interface)
            self.player_2 = Human(Marks.nought, self.game_interface)
        elif type_game == GameType.human_vs_computer.value:
            self.player_1 = Human(Marks.cross, self.game_interface)
            self.player_2 = Computer(Marks.nought)
        elif type_game == GameType.computer_vs_computer.value:
            self.player_1 = Computer(Marks.cross)
            self.player_2 = Computer(Marks.nought)

    def makeHuman(self):
        raise NotImplementedError()

    def makeComputer(self):
        raise NotImplementedError()
