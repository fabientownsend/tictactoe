from player import Player


class Human(Player):
    def __init__(self, mark, console):
        Player.__init__(self, mark)
        self.console = console
        self.MIN_RANGE = 0

    def get_move(self, board):
        requestMove = True

        while requestMove:
            position = self.console.get_player_move()

            total = len(board.board) * len(board.board)
            if position < self.MIN_RANGE or position >= total:
                self.console.display_correct_range_board()
            elif not board.is_empty(position):
                self.console.spot_not_free()
            else:
                requestMove = False

        return position
