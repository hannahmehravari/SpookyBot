import numpy as np
import sys

class Board:

    def __init__(self):
        self.cell_array = np.empty((24, 15))
        self.cell_array[:, :] = 0
        self.cell_array[0, 0:2] = 1
        self.cell_array[5, 0:5] = 2
        self.cell_array[7, 0:3] = 2
        self.cell_array[11, 0:5] = 1
        self.cell_array[12, 0:5] = 2
        self.cell_array[16, 0:3] = 1
        self.cell_array[18, 0:5] = 1
        self.cell_array[23, 0:2] = 2

    def draw_board(self):
        full_board = self.cell_array.swapaxes(0, 1)
        bottom_half = full_board[:, 0:12]
        top_half = full_board[:, 12:24]
        bottom_half = np.flip(bottom_half)
        separator_row = np.empty((1, 12))
        separator_row[:, :] = 3
        board = np.concatenate((top_half, separator_row, separator_row, bottom_half))
        board = board[~np.all(board == 0, axis=1)]
        board[board == 3] = 0
        return board

        # cell_list = [[0, 0],
        #              [],
        #              [],
        #              [],
        #              [],
        #              [1, 1, 1, 1, 1],
        #              [],
        #              [1, 1, 1],
        #              [],
        #              [],
        #              [],
        #              [0, 0, 0, 0, 0],
        #              [1, 1, 1, 1, 1],
        #              [],
        #              [],
        #              [],
        #              [0, 0, 0],
        #              [],
        #              [0, 0, 0, 0, 0],
        #              [],
        #              [],
        #              [],
        #              [],
        #              [1, 1],
        #              ]


if __name__ == '__main__':
    b = Board()
    h = "11---10----9----8----7----6----5----4----3----2----1----0"
    f = "12---13---14---15---16---17---18---19---20---21---22---23"
    np.savetxt(sys.stdout, b.draw_board(), fmt="%4d", header=h, footer=f, comments="  ")

