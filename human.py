import logging

from player import Player


class Human(Player):
    def __init__(self, mark, console):
        Player.__init__(self, mark)
        logging.basicConfig(filename='exemple.log', level=logging.DEBUG)
        self.console = console

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
