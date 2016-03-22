class FakeConsoleIO:
    def __init__(self):
        self.spy_passed_into_method = False
        self.displayed_value = None

    def display_text(self, text):
        self.spy_passed_into_method = True
        self.displayed_value = text

    def user_input(self, text):
        return 1

    def display_board(self, board):
        self.spy_passed_into_method = True
