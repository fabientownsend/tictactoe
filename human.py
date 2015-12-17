import logging
from consoleUI import InputNotInt
from player import Player

class Human(Player):
    def getMove(self, board):
        while True:
            try:
                position = self.console.getPlayerPosition()

                if position > 8 or position < 0:
                    self.console.displayCorrectRangeBoard()
                elif not self.gamePolicy.isFree(board, position):
                    self.console.spotNotFree()
                else:
                    break
            except InputNotInt, (arg):
                self.console.expectedNumber()
                logging.debug(arg.msg)

        return position
