from console_ui import ConsoleUI
from game_board import GameBoard
from game_engine import GameEngine
from game_policy import GamePolicy

console = ConsoleUI()
gamePolicy = GamePolicy()
board = GameBoard(3)
gameEngine = GameEngine(console, gamePolicy, board)

gameEngine.createTypeGame()
gameEngine.defineFirstPlayer()
gameEngine.play()
