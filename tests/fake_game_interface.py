class FakeGameInterface:
    def __init__(self):
        self.passed_in_display_tie = False
        self.passed_in_display_winner = False
        self.player_move_position = 0
        self.valide_player_move = 0
        self.passed_in_player_move = False
        self.passed_in_wrong_range = False
        self.passed_in_spot_not_free = False
        self.get_first_player_counter = 0
        self.get_type_game_selected_counter = 0
        self.first_player = 1
        self.gameSelected = 1

    def display_type_game(self):
        return None

    def spot_not_free(self):
        self.passed_in_spot_not_free = True
        return None

    def display_correct_range_board(self, fakeMin, fakeMax):
        self.passed_in_wrong_range = True
        return None

    def get_type_game_selected(self):
        self.get_type_game_selected_counter += 1
        if self.get_type_game_selected_counter > 1:
            return 1
        else:
            self.gameSelected


    def display_which_start(self):
        return None

    def get_first_player(self):
        self.get_first_player_counter += 1
        if self.get_first_player_counter > 1:
            return 1
        else:
            return self.first_player

    def display_player_turn(self, mark):
        return None

    def get_player_move(self):
        if self.passed_in_player_move:
            return self.valide_player_move

        self.passed_in_player_move = True
        return self.player_move_position

    def display_board(self, board):
        return None

    def display_winner(self, value):
        self.passed_in_display_winner = True
        return None

    def display_tie(self):
        self.passed_in_display_tie = True
        return None
