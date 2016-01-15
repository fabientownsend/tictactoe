from enum import Enum

from computer import Computer
from consoleUI import InputNotInt
from gameBoard import GameBoard
from human import Human
from marksEnum import Marks


class GameType(Enum):
    humanVsHuman = 1
    humanVsComputer = 2
    computerVsComputer = 3


class PlayersEnum(Enum):
    player1 = 1
    player2 = 2


class GameEngine:
    def __init__(self, console, gamePolicy, board):
        self.console = console
        self.gamePolicy = gamePolicy
        self.board = board

        self.gameOver = False
        self.tie = False
        self.winner = None
        self.currentPlayer = None

    def createTypeGame(self):
        self.console.displayTypeGame()
        typeGame = self.getTypeGameSelected()
        self.createPlayersTypeGame(typeGame)

    def getTypeGameSelected(self):
        while True:
            typeGame = self.console.typeGameSelected()

            if typeGame > 0 and typeGame < 4:
                break

        return typeGame

    def createPlayersTypeGame(self, typeGame):
        if typeGame == GameType.humanVsHuman.value:
            self.player1 = Human(Marks.cross, self.console)
            self.player2 = Human(Marks.nought, self.console)
        elif typeGame == GameType.humanVsComputer.value:
            self.player1 = Human(Marks.cross, self.console)
            self.player2 = Computer(Marks.nought)
        elif typeGame == GameType.computerVsComputer.value:
            self.player1 = Computer(Marks.cross)
            self.player2 = Computer(Marks.nought)

    def defineFirstPlayer(self):
        self.console.displayWhichStart()
        firstPlayerSelected = self.getFirstPlayerSlected()
        self.setFirstPlayer(firstPlayerSelected)

    def getFirstPlayerSlected(self):
        while True:
            firstPlayerSelected = self.console.getFirstPlayer()

            if firstPlayerSelected > 0 and firstPlayerSelected < 3:
                break

        return firstPlayerSelected


    def setFirstPlayer(self, firstPlayerSelected):
        if firstPlayerSelected == PlayersEnum.player1.value:
            self.currentPlayer = self.player1
        elif firstPlayerSelected == PlayersEnum.player2.value:
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
        if self.gamePolicy.win(self.currentPlayer.mark, board):
            self.winner = self.currentPlayer
            self.gameOver = True

            return True
        elif self.gamePolicy.checkTie(board):
            self.tie = True
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
