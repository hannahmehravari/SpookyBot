import numpy as np
import sys


class Board:

    def __init__(self):
        self.cell_list = [["O", "O"],
                          [],
                          [],
                          [],
                          [],
                          ["X", "X", "X", "X", "X"],
                          [],
                          ["X", "X", "X"],
                          [],
                          [],
                          [],
                          ["O", "O", "O", "O", "O"],
                          ["X", "X", "X", "X", "X"],
                          [],
                          [],
                          [],
                          ["O", "O", "O"],
                          [],
                          ["O", "O", "O", "O", "O"],
                          [],
                          [],
                          [],
                          [],
                          ["X", "X"],
                          ]
        self.cell_array = np.chararray((24, 15), unicode=True)

    def update_cell_array(self):
        length_list = [len(x) for x in self.cell_list]
        max_length = max(length_list)

        clean_list = [" "] * 24
        counter = 0
        for l in self.cell_list:
            if len(l) != max_length:
                clean_list[counter] = l + ([" "] * (max_length - len(l)))
            else:
                clean_list[counter] = l
            counter += 1
        self.cell_array = np.array(clean_list)

    def draw_board(self):
        self.update_cell_array()
        full_board = self.cell_array.swapaxes(0, 1)
        bottom_half = full_board[:, 0:12]
        top_half = full_board[:, 12:24]
        bottom_half = np.flip(bottom_half)
        separator_row = np.chararray((1, 12))
        separator_row[:, :] = '0'

        board = np.concatenate((top_half, separator_row, separator_row, bottom_half))
        board = board[~np.all(board == ' ', axis=1)]
        board[board == '0'] = " "
        bar = np.chararray((board.shape[0], 1))
        bar[:] = "|"
        left_board = board[:, 0:6]
        right_board = board[:, 6:13]

        board = np.concatenate((left_board, bar, right_board), axis=1)
        return board


if __name__ == '__main__':
    b = Board()
    h = "11---10---09---08---07---06-------05---04---03---02---01---00"
    f = "12---13---14---15---16---17-------18---19---20---21---22---23"

    np.savetxt(sys.stdout, b.draw_board(), fmt="%s", header=h, footer=f, comments="", delimiter="    ")

