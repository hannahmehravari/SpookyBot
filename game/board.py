import numpy as np


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
        self.cell_array = self.cell_array.swapaxes(0, 1)

    def draw_board(self):
        bottom_half = self.cell_array[:, 0:12]
        top_half = self.cell_array[:, 12:24]
        bottom_half = np.flip(bottom_half)

        board = np.concatenate((top_half, bottom_half))

        board = board[~np.all(board == 0, axis=1)]

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
    np.savetxt('bg.txt', b.draw_board(), fmt="%4d")
