from copy import copy
import random

from marks_enum import Marks
from player import Player


class Computer(Player):
    def getMove(self, board):
        bestMove = 0
        bestValue = -100

        total = len(board.board) * len(board.board)
        for i in range(total):
            if board.isEmpty(i):
                board.setMark(i, self.mark)
                value = self.minimax(self.switch(self.mark), board)
                board.setMark(i, Marks.empty)

                if value > bestValue:
                    bestMove = i
                    bestValue = value

        return bestMove

    def minimax(self, mark, board):
        if self.gamePolicy.win(board.board, self.mark):
            return 1
        elif self.gamePolicy.win(board.board, self.switch(self.mark)):
            return -1
        elif self.gamePolicy.checkTie(board.board):
            return 0

        if mark == self.mark:
            bestValue = -100

            total = len(board.board) * len(board.board)
            for i in range(total):
                if board.isEmpty(i):
                    board.setMark(i, mark)
                    val = self.minimax(self.switch(mark), board)
                    board.setMark(i, Marks.empty)
                    bestValue = max(val, bestValue)

            return bestValue
        else:
            bestValue = 100

            total = len(board.board) * len(board.board)
            for i in range(total):
                if board.isEmpty(i):
                    board.setMark(i, mark)
                    val = self.minimax(self.switch(mark), board)
                    board.setMark(i, Marks.empty)
                    bestValue = min(val, bestValue)

            return bestValue

    def switch(self, mark):
        if mark == Marks.cross:
            return Marks.nought
        else:
            return Marks.cross
