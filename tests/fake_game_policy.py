import itertools

class FakeGamePolicy:
    def __init__(self):
        self.response_win = False
        self.response_check_tie = False
        self.passed_in_this_method = False

    def win(self, mark, board):
        if self.passed_in_this_method:
            return True

        self.passed_in_this_method = True
        return self.response_win

    def check_tie(self, board):
        return self.response_check_tie
