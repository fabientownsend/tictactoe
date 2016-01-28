from marks_enum import Marks
from player import Player


class Computer(Player):
    def get_move(self, game_board):
        best_move = 0
        best_value = -100

        for i in range(game_board.get_max_range()):
            if game_board.is_empty(i):
                game_board.set_mark(i, self.mark)
                value = self.minimax(self.switch(self.mark), game_board)
                game_board.set_mark(i, Marks.empty)

                if value > best_value:
                    best_move = i
                    best_value = value

        return best_move

    def minimax(self, mark, game_board):
        if self.game_policy.win(game_board.board, self.mark):
            return 1
        elif self.game_policy.win(game_board.board, self.switch(self.mark)):
            return -1
        elif self.game_policy.check_tie(game_board.board):
            return 0

        if mark == self.mark:
            best_value = -100

            for i in range(game_board.get_max_range()):
                if game_board.is_empty(i):
                    game_board.set_mark(i, mark)
                    val = self.minimax(self.switch(mark), game_board)
                    game_board.set_mark(i, Marks.empty)
                    best_value = max(val, best_value)

            return best_value
        else:
            best_value = 100

            for i in range(game_board.get_max_range()):
                if game_board.is_empty(i):
                    game_board.set_mark(i, mark)
                    val = self.minimax(self.switch(mark), game_board)
                    game_board.set_mark(i, Marks.empty)
                    best_value = min(val, best_value)

            return best_value

    def switch(self, mark):
        if mark == Marks.cross:
            return Marks.nought
        else:
            return Marks.cross
