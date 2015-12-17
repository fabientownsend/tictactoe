from consoleUI import ConsoleUI
from gamePolicy import GamePolicy
import logging

class Player():
    def __init__(self, mark):
        self.console = ConsoleUI()
        self.gamePolicy = GamePolicy()
        self.mark = mark
        logging.basicConfig(filename='exemple.log', level=logging.DEBUG)

    def getMove(self, board):
        raise NotImplementedError()
