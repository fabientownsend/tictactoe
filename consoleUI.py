import sys


class ConsoleUI():
    def displayTypeGame(self):
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
            self.typeGame = input("Select your type of game: ")
        except KeyboardInterrupt:
            sys.exit()
        except:
            self.expectedNumber()
            self.typeGameSelected()

        return self.typeGame

    def displayWhichStart(self):
        print(
            "Which player start:\n\n"
            "1 - Player 1\n"
            "2 - Player 2\n"
        )

    def getFirstPlayer(self):
        try:
            self.firstPlayer = input("Which player should start? ")
        except KeyboardInterrupt:
            sys.exit()
        except:
            self.expectedNumber()
            self.getFirstPlayer()

        return self.firstPlayer

    def displayPlayerTurn(self, idPlayer):
        print("Player " + str(idPlayer) + " turn")

    def getPlayerMove(self):
        try:
            position = input("Which position: ")
        except KeyboardInterrupt:
            sys.exit()
        except:
            self.expectedNumber()
            self.getPlayerMove()

        return position

    def displayBoard(self, board):
        for row in range(len(board)):
            for column in range(len(board)):
                sys.stdout.write("  " + board[row][column].value + "  ")
                if column < len(board) - 1:
                    sys.stdout.write("|")
            print("\n")
            if row < len(board) - 1:
                for column in range(len(board)):
                        sys.stdout.write("-"*6)
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
