from game_interface.console_io import ConsoleIO
from game_interface.french_messenger import FrenchMessenger
from game_interface.english_messenger import EnglishMessenger
from game_play.game_board import GameBoard
from game_play.game_engine import GameEngine
from game_play.game_policy import GamePolicy

io = ConsoleIO()
game_interface = FrenchMessenger(io)
game_policy = GamePolicy()
board = GameBoard(3)
gameEngine = GameEngine(game_interface, game_policy, board)

gameEngine.create_type_game()
gameEngine.define_first_player()
gameEngine.play()
