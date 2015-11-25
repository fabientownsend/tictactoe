class GameBoard():
    def __init__(self):
        self.board = self.createBoard()

    def createBoard(self):
        NB_SPOTS = 9
        return list("-"*NB_SPOTS)

    def getBoard(self):
        return self.board
