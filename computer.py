from copy import copy
import random

from marksEnum import Marks
from player import Player


class Computer(Player):
    def getMove(self, board):
        if self.gamePolicy.isEmpty(board):
            bestStartMoves = [0, 2, 4, 6, 8]
            return random.choice(bestStartMoves)

        bestMove = 0
        bestValue = -100

        for i in range(len(board)):
            if self.gamePolicy.isFree(board, i):
                boardCopy = copy(board)
                boardCopy[i] = self.mark
                value = self.minimax(self.switch(self.mark), boardCopy)

                if value > bestValue:
                    bestMove = i
                    bestValue = value

        return bestMove

    def minimax(self, mark, board):
        if self.gamePolicy.win(self.mark, board):
            return 1
        elif self.gamePolicy.win(self.switch(self.mark), board):
            return -1
        elif self.gamePolicy.checkTie(board):
            return 0

        if mark == self.mark:
            bestValue = -100

            for i in range(len(board)):
                if self.gamePolicy.isFree(board, i):
                    boardCopy = copy(board)
                    boardCopy[i] = mark
                    val = self.minimax(self.switch(mark), boardCopy)
                    bestValue = max(val, bestValue)

            return bestValue
        else:
            bestValue = 100

            for i in range(len(board)):
                if self.gamePolicy.isFree(board, i):
                    boardCopy = copy(board)
                    boardCopy[i] = mark
                    val = self.minimax(self.switch(mark), boardCopy)
                    bestValue = min(val, bestValue)

            return bestValue

    def switch(self, mark):
        if mark == Marks.cross:
            return Marks.nought
        else:
            return Marks.cross
