import random

from life_forms import Plant, Empty





class Life:

    def __init__(self):
        self.plant_placiment_probability = 0.5
        self.day = 0

    def build_board(self, rows=7, cols=15):
        self.board = [[Empty() for a in range(cols)] for b in range(rows)]
        for row_index, row in enumerate(self.board):
            for column_index, location in enumerate(row):
                if random.random() >= 1 - self.plant_placiment_probability:
                    self.board[row_index][column_index] = Plant((row_index, column_index))

    def print_board(self):
        print(f"Game Board For Day {self.day}")
        for row in self.board:
            row_string = '|'
            for col in row:
                row_string = row_string + f"{col}" + "|"
            print('>>>', row_string, "<<<")

    def one_day(self):
        self.day += 1
        for row_index, row in enumerate(self.board):
            for column_index, lifeform in enumerate(row):
                type_of_lifeform = str(type(lifeform)).split('.')[1].split("'")[0]
                if type_of_lifeform == "Plant":
                    max_available_sunlight = random.randrange(3,6)
                    surrounding_plant_heights = []
                    for row_modifier in [-1, 0, 1]:
                        for col_modifier in [-1, 0, 1]:
                            search_row = row_index + row_modifier
                            search_col = column_index + col_modifier
                            if search_col >= 0 and search_row >= 0 and row_modifier+col_modifier > 0 and search_row < len(self.board) and search_col < len(row):
                                surrounding_lifeform = self.board[search_row][search_col]
                                if str(type(surrounding_lifeform)).split('.')[1].split("'")[0] == "Plant":
                                    surrounding_plant_heights.append(surrounding_lifeform.height)

                    if len(surrounding_plant_heights) == 0:
                        lifeform.live_a_day(max_available_sunlight)
                        self.board[row_index][column_index] = lifeform
                    elif lifeform.height == max(surrounding_plant_heights):
                        lifeform.live_a_day(max_available_sunlight)
                        self.board[row_index][column_index] = lifeform
                    else:
                        lifeform.live_a_day(max_available_sunlight-1)
                        self.board[row_index][column_index] = lifeform

                    if lifeform.energy <= 0:
                        self.board[row_index][column_index] = Empty()








if __name__ == "__main__":
    L = Life()
    L.build_board()
    L.print_board()
    for d in range(0,2000):
        L.one_day()
    L.print_board()