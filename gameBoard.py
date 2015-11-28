from marksEnum import Marks

class GameBoard():
    def __init__(self):
        self.board = self.createBoard()

    def resetBoard(self):
        self.board = self.createBoard()

    def createBoard(self):
        return [
            Marks.empty, Marks.empty, Marks.empty,
            Marks.empty, Marks.empty, Marks.empty,
            Marks.empty, Marks.empty, Marks.empty
        ]

    def getBoard(self):
        return self.board

    def setMark(self, position, mark):
        if self.board[position] != Marks.empty:
            raise SpotNotEmpty
        else:
            self.board[position] = mark

    def isFree(self, position):
        if self.board[position] != Marks.empty:
            return False
        else:
            return True

    def win(self, mark):
        if (self.checkLines(mark) or
            self.checkColumns(mark) or
            self.checkDiagonals(mark)):
            return True
        else:
            False

    def checkLines(self, mark):
        if (self.board[0] == mark and
              self.board[1] == mark and
              self.board[2] == mark):
            return True
        if (self.board[3] == mark and
              self.board[4] == mark and
              self.board[5] == mark):
            return True
        if (self.board[6] == mark and
              self.board[7] == mark and
              self.board[8] == mark):
            return True
        else:
            return False

    def checkColumns(self, mark):
        if (self.board[0] == mark and
              self.board[3] == mark and
              self.board[6] == mark):
            return True
        if (self.board[1] == mark and
              self.board[4] == mark and
              self.board[7] == mark):
            return True
        if (self.board[2] == mark and
              self.board[5] == mark and
              self.board[8] == mark):
            return True
        else:
            return False

    def checkDiagonals(self, mark):
        if (self.board[0] == mark and
              self.board[4] == mark and
              self.board[8] == mark):
            return True
        if (self.board[2] == mark and
              self.board[4] == mark and
              self.board[6] == mark):
            return True
        else:
            return False

class SpotNotEmpty(Exception):
    def __init__(self):
        self.msg = 'The spot must be free'
