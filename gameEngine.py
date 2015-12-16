from enum import Enum

from computer import Computer
from consoleUI import ConsoleUI
from gameBoard import GameBoard
from gamePolicy import GamePolicy
from human import Human
from marksEnum import Marks

class GameType(Enum):
    humanVsHuman = 1
    humanVsComputer = 2
    computerVsComputer = 3


class PlayersEnum(Enum):
    player1 = 1
    player2 = 2


class GameEngine():
    def __init__(self):
        self.console = ConsoleUI()
        self.board = GameBoard()
        self.gameOver = False
        self.tie = False
        self.gamePolicy = GamePolicy()
        self.winner = None
        self.currentPlayer = None

    def typeGame(self):
        self.console.displayGameType()
        typeGame = self.getTypeGameSelected()
        self.createPlayers(typeGame)

    def getTypeGameSelected(self):
        while True:
            typeGame = self.console.typeGameSelected()
            if typeGame > 0 and typeGame < 4:
                return typeGame
                break

    def createPlayers(self, typeGame):
        if typeGame == GameType.humanVsHuman.value:
            self.player1 = Human(Marks.cross)
            self.player2 = Human(Marks.nought)
        elif typeGame == GameType.humanVsComputer.value:
            self.player1 = Human(Marks.cross)
            self.player2 = Computer(Marks.nought)
        elif typeGame == GameType.computerVsComputer.value:
            self.player1 = Computer(Marks.cross)
            self.player2 = Computer(Marks.nought)

    def defineFirstPlayer(self):
        self.console.displayWhichStart()
        firstPlayer = self.console.firstPlayerSelected()
        self.setFirstPlayer(firstPlayer)

    def getFirstPlayerSlected(self):
        while True:
            firstPlayer = self.console.firstPlayerSelected()
            if firstPlayer > 0 and firstPlayer < 3:
                return firstPlayer
                break

    def setFirstPlayer(self, firstPlayer):
        if firstPlayer == PlayersEnum.player1.value:
            self.currentPlayer = self.player1
        elif firstPlayer == PlayersEnum.player2.value:
            self.currentPlayer = self.player2

    def play(self):
        while not self.gameOver:
            board = self.board.getBoard()
            mark = self.currentPlayer.mark

            self.console.displayPlayerTurn(mark.value)
            position = self.currentPlayer.getMove(board)
            self.board.setMark(position, mark)
            self.console.displayBoard(board)

            if self.isGameOver(board):
                self.displayResult()
            else:
                self.switchCurrentPlayer()

    def isGameOver(self, board):
        if self.gamePolicy.checkTie(board):
            self.tie = True
            self.gameOver = True

            return True
        elif self.gamePolicy.win(self.currentPlayer.mark, board):
            self.winner = self.currentPlayer
            self.gameOver = True

            return True
        else:
            False

    def displayResult(self):
        if self.tie:
            self.console.displayTie()
        else:
            self.console.displayWinner(self.winner.mark.value)

    def switchCurrentPlayer(self):
        if self.currentPlayer == self.player1:
            self.currentPlayer = self.player2
        else:
            self.currentPlayer = self.player1
