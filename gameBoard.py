class GameBoard():
    def __init__(self):
        self.board = self.createBoard()
        self.currentMark = 'x'

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

class SpotNotEmpty(Exception):
    def __init__(self):
        self.msg = 'The sport must be free'

