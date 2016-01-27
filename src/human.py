from player import Player


class Human(Player):
    def __init__(self, mark, console):
        Player.__init__(self, mark)
        self.console = console

    def get_move(self, gameBoard):
        MAX_RANGE = gameBoard.get_max_range()
        MIN_RANGE = gameBoard.get_min_range()

        position = self.console.get_player_move()

        if position < MIN_RANGE or position >= MAX_RANGE:
            self.console.display_correct_range_board(MIN_RANGE, MAX_RANGE)
            return self.get_move(gameBoard)
        elif not gameBoard.is_empty(position):
            self.console.spot_not_free()
            return self.get_move(gameBoard)
        else:
            return position

