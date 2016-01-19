from consoleUI import InputNotInt
from player import Player


class Human(Player):
    def __init__(self, mark, console):
        Player.__init__(self, mark)
        self.console = console
        self.MIN_RANGE = 0

    def getMove(self, board):
        while True:
            position = self.console.getPlayerMove()

            if position < self.MIN_RANGE or position > len(board):
                self.console.displayCorrectRangeBoard()
            elif not self.board.isEmpty(position):
                self.console.spotNotFree()
            else:
                break

        return position
