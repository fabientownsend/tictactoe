from console_ui import InputNotInt
from player import Player


class Human(Player):
    def __init__(self, mark, console):
        Player.__init__(self, mark)
        self.console = console
        self.MIN_RANGE = 0

    def getMove(self, board):
        requestMove = True

        while requestMove:
            position = self.console.getPlayerMove()

            total = len(board.board) * len(board.board)
            if position < self.MIN_RANGE or position >= total:
                self.console.displayCorrectRangeBoard()
            elif not board.isEmpty(position):
                self.console.spotNotFree()
            else:
                requestMove = False

        return position
