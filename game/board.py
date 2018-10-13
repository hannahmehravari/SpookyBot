import numpy as np
import sys
from random import randint


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
        self.dice = [None, None]
        self.jail = []

    def roll_dice(self):
        self.dice[0] = randint(1, 6)
        self.dice[1] = randint(1, 6)

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
        print(self.cell_list)
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

    def is_cell_available(self, cell, checker):
        if len(self.cell_list[cell]) > 1 and self.cell_list[cell][0] != checker:
            print("Cell is not available")
            return False
        return True

    def is_move_valid(self, start, number):
        if self.cell_list[start][0] not in self.jail:
            if number in self.dice:
                if self.is_cell_available(start + number, self.cell_list[start][0]):
                    return True
        print("Invalid move")
        return False

    def make_move(self, start, number):
        destination = start + number
        if self.is_move_valid(start, number):
            if len(self.cell_list[destination]) == 1:
                self.jail.append(self.cell_list[destination][0])
                self.cell_list[destination].pop(0)
                self.cell_list[destination].append(self.cell_list[start])
                self.cell_list[start].pop(0)
            else:
                self.cell_list[destination].append(self.cell_list[start][0])
                self.cell_list[start].pop(0)


if __name__ == '__main__':
    b = Board()
    f = "11---10---09---08---07---06-------05---04---03---02---01---00"
    h = "12---13---14---15---16---17-------18---19---20---21---22---23"

    np.savetxt(sys.stdout, b.draw_board(), fmt="%s", header=h, footer=f, comments="", delimiter="    ")

    b.roll_dice()
    print(b.dice)
    b.make_move(0, b.dice[0])

    np.savetxt(sys.stdout, b.draw_board(), fmt="%s", header=h, footer=f, comments="", delimiter="    ")
