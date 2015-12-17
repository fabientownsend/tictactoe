import sys


class ConsoleUI():
    def displayGameType(self):
        print(
            "Type of game:\n\n"
            "1 - Human v. Human\n"
            "2 - Human v. Computer\n"
            "3 - Computer v. Computer\n"
        )

    def spotNotFree(self):
        print("it must be a free spot")

    def displayCorrectRangeBoard(self):
        print("position between 0 and 8")

    def typeGameSelected(self):
        try:
            typeGame = input("Select your type of game: ")
        except KeyboardInterrupt:
            sys.exit()
        except:
            raise InputNotInt

        return typeGame

    def displayWhichStart(self):
        print(
            "Which player start:\n\n"
            "1 - Player 1\n"
            "2 - Player 2\n"
        )

    def firstPlayerSelected(self):
        try:
            firstPlayer = input("Which player should start?")
        except KeyboardInterrupt:
            sys.exit()
        except:
            raise InputNotInt

        return firstPlayer

    def displayPlayerTurn(self, idPlayer):
        print("Player " + str(idPlayer) + " select your position:")

    def getPlayerPosition(self):
        try:
            position = input("Which position: ")
        except KeyboardInterrupt:
            sys.exit()
        except:
            raise InputNotInt

        return position

    def displayBoard(self, board):
        print("\n")
        print " %s | %s | %s " %(board[0].value, board[1].value, board[2].value)
        print("-----------")
        print " %s | %s | %s " %(board[3].value, board[4].value, board[5].value)
        print("-----------")
        print " %s | %s | %s " %(board[6].value, board[7].value, board[8].value)
        print("\n")

    def displayWinner(self, winner):
        print("Player " + str(winner) + " won the party")

    def displayTie(self):
        print("It's a tie, no one won!")

    def expectedNumber(self):
        print("A number is expected")

class InputNotInt(Exception):
    def __init__(self):
        self.msg = "Input from console must be only int"
