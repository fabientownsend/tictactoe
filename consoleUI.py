class ConsoleUI():
    def displayBoard(self, board):
        print("\n")
        print " %s | %s | %s " %(board[0].value, board[1].value, board[2].value)
        print("-----------")
        print " %s | %s | %s " %(board[3].value, board[4].value, board[5].value)
        print("-----------")
        print " %s | %s | %s " %(board[6].value, board[7].value, board[8].value)
        print("\n")
