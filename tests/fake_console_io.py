class FakeConsoleIO:
    def __init__(self):
        self.spy_passed_into_method = False

    def display_text(self, text):
        self.spy_passed_into_method = True

    def user_input(self, text):
        return 1

    def display_board(self, board):
        self.spy_passed_into_method = True
