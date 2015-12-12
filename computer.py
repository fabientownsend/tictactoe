from copy import copy
from gamePolicy import GamePolicy
from marksEnum import Marks
import random

class Computer():
    def __init__(self, idPlayer):
        self.idPlayer = idPlayer
        self.gamePolicy = GamePolicy()

    def isFree(self, board, i):
        return board[i] == Marks.empty

    def setMarkBoard(self, board, mark, i):
        board[i] = mark
        return board

    def setMark(self, mark):
        self.mark = mark

    def isEmpty(self, board):
        for i in board:
            if i != Marks.empty:
                return False

        return True

    def switch(self, mark):
        if mark == Marks.cross:
            return Marks.nought
        else:
            return Marks.cross

    def bestMove(self, board):
        if self.isEmpty(board):
            startMoves = [0, 2, 4, 6, 8]
            return random.choice(startMoves)

        bestMove = 0
        bestValue = -100

        for i in range(len(board)):
            if self.isFree(board, i):
                boardCopy = copy(board)
                boardCopy = self.setMarkBoard(boardCopy, self.mark, i)
                value = self.minimax(self.switch(self.mark), boardCopy)

                if value > bestValue:
                    bestMove = i
                    bestValue = value

        return bestMove

    def switch(self, mark):
        if mark == Marks.cross:
            return Marks.nought
        else:
            return Marks.cross

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
