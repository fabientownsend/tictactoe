from copy import copy
import random

from marks_enum import Marks
from player import Player


class Computer(Player):
    def get_move(self, board):
        best_move = 0
        best_value = -100

        total = len(board.board) * len(board.board)
        for i in range(total):
            if board.is_empty(i):
                board.set_mark(i, self.mark)
                value = self.minimax(self.switch(self.mark), board)
                board.set_mark(i, Marks.empty)

                if value > best_value:
                    best_move = i
                    best_value = value

        return best_move

    def minimax(self, mark, board):
        if self.gamePolicy.win(board.board, self.mark):
            return 1
        elif self.gamePolicy.win(board.board, self.switch(self.mark)):
            return -1
        elif self.gamePolicy.check_tie(board.board):
            return 0

        if mark == self.mark:
            best_value = -100

            total = len(board.board) * len(board.board)
            for i in range(total):
                if board.is_empty(i):
                    board.set_mark(i, mark)
                    val = self.minimax(self.switch(mark), board)
                    board.set_mark(i, Marks.empty)
                    best_value = max(val, best_value)

            return best_value
        else:
            best_value = 100

            total = len(board.board) * len(board.board)
            for i in range(total):
                if board.is_empty(i):
                    board.set_mark(i, mark)
                    val = self.minimax(self.switch(mark), board)
                    board.set_mark(i, Marks.empty)
                    best_value = min(val, best_value)

            return best_value

    def switch(self, mark):
        if mark == Marks.cross:
            return Marks.nought
        else:
            return Marks.cross
