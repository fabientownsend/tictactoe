class GameInterface():
    def __init__(self, io):
        self.io = io

    def display_type_game(self):
        self.io.display_text("Type of game:\n\n"
                             "1 - Human v. Human\n"
                             "2 - Human v. Computer\n"
                             "3 - Computer v. Computer\n"
                            )

    def spot_not_free(self):
        self.io.display_text("it must be a free spot")

    def display_range_board(self, min_range, max_range):
        self.io.display_text("position between {min_range} and {max_range}".format(
            min_range=str(min_range), max_range=str(max_range -1)))

    def get_type_game_selected(self):
        return self.io.user_input("Select your type of game: ")

    def display_which_start(self):
        self.io.display_text("Which player start:\n\n"
                             "1 - Player 1\n"
                             "2 - Player 2\n"
                            )

    def get_first_player(self):
        return self.io.user_input("Which player should start? ")

    def display_player_turn(self, player_mark):
        self.io.display_text("Player {mark} turn".format(
            mark=str(player_mark)))

    def get_player_move(self):
        return self.io.user_input("Which position: ")

    def display_board(self, board):
        self.io.display_board(board)

    def display_winner(self, winne_mark):
        self.io.display_text("Player {mark} won the party".format(
            mark=str(winne_mark)))

    def display_tie(self):
        self.io.display_text("It's a tie, no one won!")
