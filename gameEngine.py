from computer import Computer
from gamePolicy import GamePolicy
from consoleUI import ConsoleUI
from gameBoard import GameBoard
from human import Human
from marksEnum import Marks

def switchPlayer():
    if currentPlayer == player1:
        return player2
    else:
        return player1

console = ConsoleUI()
gamePolicy = GamePolicy()

console.displayGameType()
typeGame = console.typeGameSelected()

if typeGame == 1:
    player1 = Human(1)
    player2 = Human(2)
elif typeGame == 2:
    player1 = Computer(1)
    player2 = Human(2)
elif typeGame == 3:
    player1 = Computer(1)
    player2 = Computer(2)

console.displayWhichStart()
firstPlayer = console.firstPlayerSelected()

if firstPlayer == 1:
    currentPlayer = player1
elif firstPlayer == 2:
    currentPlayer = player2

board = GameBoard()
player1.setMark(Marks.cross)
player2.setMark(Marks.nought)

gameOver = False
winner = None

while not gameOver:
    console.displayPlayerTurn(currentPlayer.idPlayer)

    if isinstance(currentPlayer, Human):
        position = console.getPlayerPosition()
    else:
        position = currentPlayer.bestMove(board.getBoard())

    if board.isFree(position):
        board.setMark(position, currentPlayer.mark)
        console.displayBoard(board.getBoard())

        if (gamePolicy.win(currentPlayer.mark, board.getBoard()) or
            gamePolicy.checkTie(board.getBoard())):
            gameOver = True
            winner = currentPlayer.idPlayer

        currentPlayer = switchPlayer()

console.displayWinner(winner)
