from computer import Computer
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
board = GameBoard()
player2 = Human()
player1 = Computer()
player1.setMark(Marks.cross)
player2.setMark(Marks.nought)

currentPlayer = player1
gameOver = False

while not gameOver:
    if isinstance(currentPlayer, Human):
        position = input('Which position: ')
    else:
        position = currentPlayer.bestMove(board.getBoard())

    if board.isFree(position):
        board.setMark(position, currentPlayer.mark)
        console.displayBoard(board.getBoard())

        gameOver = board.win(currentPlayer.mark)
        currentPlayer = switchPlayer()
