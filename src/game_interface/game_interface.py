class GameInterface():
    def __init__(self, io):
        self.io = io

    def display_type_game(self):
        self.io.display_text(
            "Type of game:\n\n"
            "1 - Human v. Human\n"
            "2 - Human v. Computer\n"
            "3 - Computer v. Computer\n"
        )

    def spot_not_free(self):
        self.io.display_text("it must be a free spot")

    def display_correct_range_board(self, min_range, max_range):
        self.io.display_text("position between " +
        str(min_range) +
        " and " +
        str(max_range))

    def get_type_game_selected(self):
        return self.io.user_input("Select your type of game: ")

    def display_which_start(self):
        self.io.display_text(
            "Which player start:\n\n"
            "1 - Player 1\n"
            "2 - Player 2\n"
        )

    def get_first_player(self):
        return self.io.user_input("Which player should start? ")

    def display_player_turn(self, id_player):
        self.io.display_text("Player " + str(id_player) + " turn")

    def get_player_move(self):
        return self.io.user_input("Which position: ")

    def display_board(self, board):
        self.io.display_board(board)

    def display_winner(self, winner):
        self.io.display_text("Player " + str(winner) + " won the party")

    def display_tie(self):
        self.io.display_text("It's a tie, no one won!")

    def expected_number(self):
        self.io.display_text("A number is expected")
