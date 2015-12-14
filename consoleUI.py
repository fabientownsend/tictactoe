class ConsoleUI():
    def displayGameType(self):
        print('''
        Type of game:
        1 - Human v. Human
        2 - Human v. Computer
        3 - Computer v. Computer''')

    def displayFreeSport(self):
        print('it must be a free spot')

    def typeGameSelected(self):
        typeGame = input('Select your type of game: ')
        return typeGame

    def displayWhichStart(self):
        print('''
        Which player start:
        1 - Player 1
        2 - Player 2''')

    def firstPlayerSelected(self):
        firstPlayer = input('Which player should start?')
        return firstPlayer

    def displayPlayerTurn(self, idPlayer):
        print('Player ' + str(idPlayer) + ' select your position:')

    def getPlayerPosition(self):
        position = input('Which position: ')
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
        print('Player ' + str(winner) + ' won the party')
