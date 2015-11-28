from human import Human
from marksEnum import Marks
from gameBoard import GameBoard
from consoleUI import ConsoleUI

def switchPlayer():
    if currentPlayer == player1:
        return player2
    else:
        return player1

console = ConsoleUI()
board = GameBoard()
player1 = Human()
player2 = Human()
player1.setMark(Marks.cross)
player2.setMark(Marks.nought)

currentPlayer = player1
gameOver = False

while not gameOver:
    position = input('Which position: ')
    if board.isFree(position):
        board.setMark(position, currentPlayer.mark)
        console.displayBoard(board.getBoard())

        gameOver = board.win(currentPlayer.mark)
        currentPlayer = switchPlayer()
