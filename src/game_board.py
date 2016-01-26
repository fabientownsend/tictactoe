from marks_enum import Marks


class GameBoard():
    def __init__(self, board_width):
        self.board_width = board_width
        self.board = self.create_board()

    def create_board(self):
        return [[Marks.empty]*self.board_width for n in range(self.board_width)]

    def get_size(self):
        return self.board_width*self.board_width

    def set_mark(self, position, mark):
        row =  position/self.board_width
        column = position - row*self.board_width
        self.board[row][column] = mark

    def get_mark(self, position):
        row =  position/self.board_width
        column = position - row*self.board_width
        return self.board[row][column]

    def is_empty(self, position):
        return self.get_mark(position) == Marks.empty
