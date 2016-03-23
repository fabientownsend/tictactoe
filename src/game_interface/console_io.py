import sys


class ConsoleIO():
    def user_input(self, text):
        try:
            return  input(text)
        except KeyboardInterrupt:
            sys.exit()
        except:
            print("A number is expected")
            self.user_input(text)

    def display_text(self, text):
        print(text)

    def display_board(self, board):
        sys.stdout.write("\n")
        for row in range(len(board)):
            for column in range(len(board)):
                sys.stdout.write("  {mark}  ".format(
                    mark=board[row][column].value))

                if column < len(board) - 1:
                    sys.stdout.write("|")

            print("\n")

            if row < len(board) - 1:
                for column in range(len(board)):
                        sys.stdout.write("-"*6)

                print("\n")

        sys.stdout.write("\n")
