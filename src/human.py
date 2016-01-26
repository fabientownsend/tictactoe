from player import Player


class Human(Player):
    def __init__(self, mark, console):
        Player.__init__(self, mark)
        self.console = console
        self.MIN_RANGE = 0

    def get_move(self, gameBoard):
        request_move = True

        while request_move:
            position = self.console.get_player_move()

            if position < self.MIN_RANGE or position >= gameBoard.get_size():
                self.console.display_correct_range_board()
            elif not gameBoard.is_empty(position):
                self.console.spot_not_free()
            else:
                request_move = False

        return position
