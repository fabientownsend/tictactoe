import sys


class ConsoleUI():
    def display_type_game(self):
        print(
            "Type of game:\n\n"
            "1 - Human v. Human\n"
            "2 - Human v. Computer\n"
            "3 - Computer v. Computer\n"
        )

    def spot_not_free(self):
        print("it must be a free spot")

    def display_correct_range_board(self):
        print("position between 0 and 8")

    def type_game_selected(self):
        try:
            self.type_game = input("Select your type of game: ")
        except KeyboardInterrupt:
            sys.exit()
        except:
            self.expected_number()
            self.type_game_selected()

        return self.type_game

    def display_which_start(self):
        print(
            "Which player start:\n\n"
            "1 - Player 1\n"
            "2 - Player 2\n"
        )

    def get_first_player(self):
        try:
            self.first_player = input("Which player should start? ")
        except KeyboardInterrupt:
            sys.exit()
        except:
            self.expected_number()
            self.get_first_player()

        return self.first_player

    def display_player_turn(self, id_player):
        print("Player " + str(id_player) + " turn")

    def get_player_move(self):
        try:
            position = input("Which position: ")
        except KeyboardInterrupt:
            sys.exit()
        except:
            self.expected_number()
            self.get_player_move()

        return position

    def display_board(self, board):
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

    def display_winner(self, winner):
        print("Player " + str(winner) + " won the party")

    def display_tie(self):
        print("It's a tie, no one won!")

    def expected_number(self):
        print("A number is expected")
