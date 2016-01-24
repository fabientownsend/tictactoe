from marks_enum import Marks


class GameBoard():
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = self.create_board()

    def create_board(self):
        return [[Marks.empty]*self.board_size for n in range(self.board_size)]

    def set_mark(self, position, mark):
        row =  position/self.board_size
        column = position - row*self.board_size
        self.board[row][column] = mark

    def get_mark(self, position):
        row =  position/self.board_size
        column = position - row*self.board_size
        return self.board[row][column]

    def is_empty(self, position):
        return self.get_mark(position) == Marks.empty
