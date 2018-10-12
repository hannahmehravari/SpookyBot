import numpy as np
class Board:

    def __init__(self):
        cell_array = np.empty((30,12))
        cell_array[0,0:2] = 0
        cell_array[5,0:5] = 1
        cell_array[7,0:3] = 1
        cell_array[11,0:5] = 0
        cell_array[12,0:5] = 1
        cell_array[16,0:3] = 0
        cell_array[18,0:5] = 0
        cell_array[23,0:2] = 1


    def get_cell_array(self):
        print(self.cell_array)


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

b = Board()
b.get_cell_array()






