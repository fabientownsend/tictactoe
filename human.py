from consoleUI import ConsoleUI
from gamePolicy import GamePolicy
from player import Player

class Human(Player):
    def getMove(self, board):
        position = self.console.getPlayerPosition()

        while not self.gamePolicy.isFree(board, position):
            self.console.displayFreeSport()
            position = self.console.getPlayerPosition()

        return position
