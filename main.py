import random

from life_forms import Plant, Empty





class Life:

    def __init__(self):
        self.plant_placiment_probability = 0.5

    def build_board(self, rows=15, cols=15):
        self.board = [[Empty() for a in range(cols)] for b in range(rows)]
        for row_index, row in enumerate(self.board):
            for column_index, location in enumerate(row):
                if random.random() >= 1 - self.plant_placiment_probability:
                    self.board[row_index][column_index] = Plant((row_index, column_index))

    def print_board(self):
        for row in self.board:
            row_string = '|'
            for col in row:
                row_string = row_string + f"{col}" + "|"
            print('>>>', row_string, "<<<")





if __name__ == "__main__":
    L = Life()
    L.build_board()
    L.print_board()