from board import Board
import numpy as np
import sys
from random import getrandbits



def backgammon():
    board = Board()
    exit_game = False
    board.roll_dice()
    board.draw_board()
    player = getrandbits(1)

    while not exit_game and (board.beared_off0 != 15 or board.beared_off1!=15):
        if player == 0:
            if len(board.dice) == 0:
                player = not player
                board.roll_dice()
                continue
            else:
                print("Human playing.")
                print("Your current dice:", board.dice)
            command = input("Enter command: ")
            symbol = 'O'
            c_list = command.strip().split(" ")
            print(c_list)
            if c_list[0] == 'Q':
                exit_game = True
            elif c_list[0] == 'M':
                if int(c_list[2]) not in board.dice:
                    print(f"You can only play numbers {board.dice}")
                    continue
                else:
                    board.make_move(int(c_list[1]), int(c_list[2]), symbol)
                    board.draw_board()

            elif c_list[0] == 'R':
                if int(c_list[1]) not in board.dice:
                    print(f"You can only play numbers {board.dice}")
                    continue
                else:
                    board.release_from_jail(symbol, int(c_list[1]) - 1)
                    board.draw_board()

            elif c_list[0] == 'B':
                if int(c_list[1]) not in board.dice:
                    print(f"You can only play numbers {board.dice}")
                    continue
                else:
                    board.bear_off(symbol, (int(c_list[1]) - 1))
                    board.draw_board()
            elif command[0] == 'H':
                print("Make move            M [POSITION] [DICE NUMBER]  EXAMPLE M 16 5 \n"
                      "Release from jail    R [START CELL POSITION]     EXAMPLE R 3\n"
                      "Bear off             B [HOME CELL POSITION]      EXAMPLE B 22\n"
                      "Help                 H\n"
                      "Quit                 Q\n")
            else:
                print("Invalid command, enter H for help")
        elif player == 1:
            if len(board.dice) == 0:
                player = not player
                board.roll_dice()
                continue
            else:
                print("Computer playing...")
                print("Computer rolled dice: ", board.dice)
                board.dice.clear()


if __name__ == '__main__':
    backgammon()
