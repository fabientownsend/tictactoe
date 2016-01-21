from consoleUI import ConsoleUI
from gameBoard import GameBoard
from gameEngine import GameEngine
from gamePolicy import GamePolicy

console = ConsoleUI()
gamePolicy = GamePolicy()
board = GameBoard(3)
gameEngine = GameEngine(console, gamePolicy, board)

gameEngine.createTypeGame()
gameEngine.defineFirstPlayer()
gameEngine.play()
