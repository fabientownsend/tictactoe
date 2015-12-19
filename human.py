import logging

from consoleUI import InputNotInt
from player import Player


class Human(Player):
    def __init__(self, mark, console):
        Player.__init__(self, mark)
        logging.basicConfig(filename="tictactoe.log", level=logging.DEBUG)
        self.console = console
        self.MAX_RANGE = 8
        self.MIN_RANGE = 0

    def getMove(self, board):
        while True:
            try:
                position = self.console.getPlayerMove()

                if position < self.MIN_RANGE or position > self.MAX_RANGE:
                    self.console.displayCorrectRangeBoard()
                elif not self.gamePolicy.isFree(board, position):
                    self.console.spotNotFree()
                else:
                    break
            except InputNotInt, (arg):
                self.console.expectedNumber()
                logging.debug(arg.msg)

        return position
