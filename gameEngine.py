from computer import Computer
from consoleUI import ConsoleUI
from gameBoard import GameBoard
from gamePolicy import GamePolicy
from human import Human
from marksEnum import Marks
from enum import Enum

class GameType(Enum):
    humanVsHuman = 1
    humanVsComputer = 2
    computerVsComputer = 3

class GameEngine():
    def __init__(self):
        self.console = ConsoleUI()
        self.board = GameBoard()
        self.gameOver = False
        self.gamePolicy = GamePolicy()
        self.winner = None
        self.currentPlayer = None

    def typeGame(self):
        self.console.displayGameType()
        typeGame = self.console.typeGameSelected()
        self.createPlayers(typeGame)

    def createPlayers(self, typeGame):
        if typeGame == GameType.humanVsHuman.value:
            self.player1 = Human(1)
            self.player2 = Human(2)
        elif typeGame == GameType.humanVsComputer.value:
            self.player1 = Human(1)
            self.player2 = Computer(2)
        elif typeGame == GameType.computerVsComputer.value:
            self.player1 = Computer(1)
            self.player2 = Computer(2)
        else:
            raise GameTypeNotExist

    def defineFirstPlayer(self):
        self.console.displayWhichStart()
        firstPlayer = self.console.firstPlayerSelected()
        self.setFirstPlayer(firstPlayer)
        self.player1.setMark(Marks.cross)
        self.player2.setMark(Marks.nought)

    def setFirstPlayer(self, firstPlayer):
        if firstPlayer == 1:
            self.currentPlayer = self.player1
        elif firstPlayer == 2:
            self.currentPlayer = self.player2

    def play(self):
        while not self.gameOver:
            board = self.board.getBoard()
            self.console.displayPlayerTurn(self.currentPlayer.idPlayer)
            position = self.getNextMove(board)
            self.board.setMark(position, self.currentPlayer.mark)
            self.console.displayBoard(board)

            if self.isGameOver(board):
                self.win()
            else:
                self.switchCurrentPlayer()

    def isGameOver(self, board):
        return (self.gamePolicy.win(self.currentPlayer.mark, board) or
                self.gamePolicy.checkTie(board))

    def win(self):
        self.gameOver = True
        self.winner = self.currentPlayer

    def getNextMove(self, board):
        if isinstance(self.currentPlayer, Human):
            position = self.console.getPlayerPosition()

            while not self.gamePolicy.isFree(board, position):
                self.console.displayFreeSport()
                position = self.console.getPlayerPosition()

            return position
        else:
            return self.currentPlayer.bestMove(board)

    def switchCurrentPlayer(self):
        if self.currentPlayer == self.player1:
            self.currentPlayer = self.player2
        else:
            self.currentPlayer = self.player1

class GameTypeNotExist(Exception):
    def __init__(self):
        self.msg = 'This type of game do not exist'
