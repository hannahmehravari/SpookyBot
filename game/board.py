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
        self.dice = []
        self.jailX = []
        self.jailO = []
        self.startO = self.cell_list[0:6]
        self.startX = self.cell_list[23:17:-1]
        self.homeO = self.cell_list[23:17:-1]
        self.homeX = self.cell_list[0:6]
        self.beared_offO = 0
        self.beared_offX = 0

    def roll_dice(self):
        self.dice.append(randint(1, 6))
        self.dice.append(randint(1, 6))

        if self.dice[0] == self.dice[1]:
            self.dice.extend(self.dice)

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
        f = "11---10---09---08---07---06-------05---04---03---02---01---00"
        h = "12---13---14---15---16---17-------18---19---20---21---22---23"
        np.savetxt(sys.stdout, board, fmt="%s", header=h, footer=f, comments="", delimiter="    ")
        jail_x_string = " ".join(self.jailX)
        jail_o_string = " ".join(self.jailO)
        print("O JAIL ", jail_x_string)
        print('X JAIL ', jail_o_string)

    def is_cell_available(self, l, cell, symbol):
        try:
            if len(l[cell]) > 1 and l[cell][0] != symbol:
                print("Cell is not available")
                return False
            return True
        except IndexError:
            print("You can't move this checker")

    def is_move_valid(self, start, number, symbol):
        if symbol == 'O':
            destination = start + number
            jail = self.jailX
        else:
            destination = start - number
            jail = self.jailO
        if self.cell_list[start][0] not in jail:
            if number in self.dice:
                if self.is_cell_available(self.cell_list, destination, self.cell_list[start][0]):
                    return True
        print("Invalid move")
        return False

    def is_symbol_valid(self, start, symbol):
        if self.cell_list[start][0] == symbol:
            return True
        else:
            return False

    def make_move(self, start, number, symbol):
        if symbol == 'O':
            destination = start + number
            jail = self.jailX
        elif symbol == 'X':
            destination = start - number
            jail = self.jailO
        else:
            print("Invalid symbol")
        if self.is_move_valid(start, number, symbol) and self.is_symbol_valid(start, symbol):
            if len(self.cell_list[destination]) == 1 and self.cell_list[destination][0] != symbol:
                jail.append(self.cell_list[destination][0])
                self.cell_list[destination].pop(0)
            else:
                self.cell_list[destination].append(self.cell_list[start][0])
                self.cell_list[start].pop(0)
                self.dice.remove(number)

    def release_from_jail(self, symbol, number):
        if symbol == 'O':
            jail = self.jailO
            start = self.startO
            print("Releasing from jailO...")
        elif symbol == 'X':
            jail = self.jailX
            start = self.startX
            print("Releasing from jailX...")
        else:
            print("Invalid symbol.")
        if self.is_cell_available(start, number, symbol):
            start[number].append(jail.pop())
        else:
            print("You can't bring back checker at position:", start[number], start, number)

    def bear_off(self, symbol, number):
        if symbol == 'O':
            home = self.homeO
            beared_off = self.beared_offO
        elif symbol == 'X':
            home = self.homeX
            beared_off = self.beared_offX

        total = 0
        for l in home:
            total += l.count(symbol)

        if total == 15:
            if len(home[number]) >= 1:
                if home[number][0] == symbol:
                    beared_off.append(home[number].pop())
                else:
                    print("You can't bear off an opponent's checker")
            else:
                print("There is no checkers at this position to bear off, you must make a move within home")
        else:
            print("You haven't moved all checkers to home yet.")

