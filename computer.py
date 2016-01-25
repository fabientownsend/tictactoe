from copy import copy
import random

from marks_enum import Marks
from player import Player


class Computer(Player):
    def get_move(self, gameBoard):
        best_move = 0
        best_value = -100

        total = len(gameBoard.board)*len(gameBoard.board)
        for i in range(total):
            if gameBoard.is_empty(i):
                gameBoard.set_mark(i, self.mark)
                value = self.minimax(self.switch(self.mark), gameBoard)
                gameBoard.set_mark(i, Marks.empty)

                if value > best_value:
                    best_move = i
                    best_value = value

        return best_move

    def minimax(self, mark, gameBoard):
        total = len(gameBoard.board)*len(gameBoard.board)

        if self.game_policy.win(gameBoard.board, self.mark):
            return 1
        elif self.game_policy.win(gameBoard.board, self.switch(self.mark)):
            return -1
        elif self.game_policy.check_tie(gameBoard.board):
            return 0

        if mark == self.mark:
            best_value = -100

            for i in range(total):
                if gameBoard.is_empty(i):
                    gameBoard.set_mark(i, mark)
                    val = self.minimax(self.switch(mark), gameBoard)
                    gameBoard.set_mark(i, Marks.empty)
                    best_value = max(val, best_value)

            return best_value
        else:
            best_value = 100

            for i in range(total):
                if gameBoard.is_empty(i):
                    gameBoard.set_mark(i, mark)
                    val = self.minimax(self.switch(mark), gameBoard)
                    gameBoard.set_mark(i, Marks.empty)
                    best_value = min(val, best_value)

            return best_value

    def switch(self, mark):
        if mark == Marks.cross:
            return Marks.nought
        else:
            return Marks.cross
