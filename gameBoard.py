class GameBoard():
    def __init__(self):
        self.board = self.createBoard()
        self.currentMark = 'x'

    def resetBoard(self):
        self.board = self.createBoard()

    def createBoard(self):
        NB_SPOTS = 9
        return list('-'*NB_SPOTS)

    def getBoard(self):
        return self.board

    def setMark(self, position):
        if self.board[position] != '-':
            raise SpotNotEmpty
        else:
            self.board[position] = self.currentMark

    def checkLines(self):
        if (self.board[0] == self.currentMark and
              self.board[1] == self.currentMark and
              self.board[2] == self.currentMark):
            return True
        if (self.board[3] == self.currentMark and
              self.board[4] == self.currentMark and
              self.board[5] == self.currentMark):
            return True
        if (self.board[6] == self.currentMark and
              self.board[7] == self.currentMark and
              self.board[8] == self.currentMark):
            return True
        else:
            return False

    def checkColumns(self):
        if (self.board[0] == self.currentMark and
              self.board[3] == self.currentMark and
              self.board[6] == self.currentMark):
            return True
        if (self.board[1] == self.currentMark and
              self.board[4] == self.currentMark and
              self.board[7] == self.currentMark):
            return True
        if (self.board[2] == self.currentMark and
              self.board[5] == self.currentMark and
              self.board[8] == self.currentMark):
            return True
        else:
            return False

    def checkDiagonals(self):
        if (self.board[0] == self.currentMark and
              self.board[4] == self.currentMark and
              self.board[8] == self.currentMark):
            return True
        if (self.board[2] == self.currentMark and
              self.board[4] == self.currentMark and
              self.board[6] == self.currentMark):
            return True
        else:
            return False

class SpotNotEmpty(Exception):
    def __init__(self):
        self.msg = 'The spot must be free'

