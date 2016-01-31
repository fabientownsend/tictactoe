from player import Player


class Human(Player):
    def __init__(self, mark, game_interface):
        Player.__init__(self, mark)
        self.game_interface = game_interface

    def get_move(self, game_board):
        MAX_RANGE = game_board.get_max_range()
        MIN_RANGE = game_board.get_min_range()

        position = self.game_interface.get_player_move()

        if position < MIN_RANGE or position >= MAX_RANGE:
            self.game_interface.display_range_board(MIN_RANGE, MAX_RANGE)
            return self.get_move(game_board)
        elif not game_board.is_empty(position):
            self.game_interface.spot_not_free()
            return self.get_move(game_board)
        else:
            return position
