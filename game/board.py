import numpy as np
import sys

class Board:

    def __init__(self):
        self.cell_array = np.chararray((24, 15),unicode=True)
        self.cell_array[:, :] = ' '
        self.cell_array[0, 0:2] = 'x'
        self.cell_array[5, 0:5] = 'o'
        self.cell_array[7, 0:3] = 'o'
        self.cell_array[11, 0:5] = 'x'
        self.cell_array[12, 0:5] = 'o'
        self.cell_array[16, 0:3] = 'x'
        self.cell_array[18, 0:5] = 'x'
        self.cell_array[23, 0:2] = 'o'

    def draw_board(self):
        full_board = self.cell_array.swapaxes(0, 1)
        bottom_half = full_board[:, 0:12]
        top_half = full_board[:, 12:24]
        bottom_half = np.flip(bottom_half)
        separator_row = np.chararray((1,12))
        separator_row[:, :] = '0'

        print(top_half.shape, bottom_half.shape, separator_row.shape)
        board = np.concatenate((top_half, separator_row, separator_row, bottom_half))
        print(board.shape)
        board = board[~np.all(board == ' ', axis=1)]
        board[board == '0'] = " "
        bar=np.chararray((board.shape[0],1))
        bar[:]="|"
        left_board = board[:, 0:6]
        right_board = board[:, 6:13]

        print(left_board.shape, bar.shape, right_board.shape)
        board = np.concatenate((left_board, bar, right_board), axis=1)
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
    h = "11---10---09---08---07---06-------05---04---03---02---01---00"
    f = "12---13---14---15---16---17-------18---19---20---21---22---23"

    np.savetxt(sys.stdout, b.draw_board(), fmt="%s", header=h, footer=f, comments="", delimiter="    ")