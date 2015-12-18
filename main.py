from consoleUI import ConsoleUI
from gameEngine import GameEngine
from gamePolicy import GamePolicy

console = ConsoleUI()
gamePolicy = GamePolicy()
gameEngine = GameEngine(console, gamePolicy)

gameEngine.typeGame()
gameEngine.defineFirstPlayer()
gameEngine.play()
