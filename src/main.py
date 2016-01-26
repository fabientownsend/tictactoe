from console_ui import ConsoleUI
from game_board import GameBoard
from game_engine import GameEngine
from game_policy import GamePolicy

console = ConsoleUI()
game_policy = GamePolicy()
board = GameBoard(3)
gameEngine = GameEngine(console, game_policy, board)

gameEngine.create_type_game()
gameEngine.define_first_player()
gameEngine.play()
