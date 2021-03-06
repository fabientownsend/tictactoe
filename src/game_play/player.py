from game_policy import GamePolicy


class Player:
    def __init__(self, mark):
        self.game_policy = GamePolicy()
        self.mark = mark

    def get_move(self, board):
        raise NotImplementedError()
