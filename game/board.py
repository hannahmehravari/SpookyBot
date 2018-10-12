import numpy as np


class Board:

    def __init__(self):
        self.cell_array = np.zeros((30, 12))
        self.cell_array[0, 0:2] = 2
        self.cell_array[5, 0:5] = 1
        self.cell_array[7, 0:3] = 1
        self.cell_array[11, 0:5] = 2
        self.cell_array[12, 0:5] = 1
        self.cell_array[16, 0:3] = 2
        self.cell_array[18, 0:5] = 2
        self.cell_array[23, 0:2] = 1

    def get_cell_array(self):
        return self.cell_array

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
    print(b.get_cell_array())
