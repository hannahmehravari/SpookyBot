from game.board import Board
import numpy as np
import sys


def backgammon():
    board = Board()

    exit_game = False
    board.roll_dice()
    board.draw_board()

    while not exit_game:
        command = input("Enter command: ")
        symbol = 'O'
        c_list = command.split(" ")
        if command[0] == 'Q':
            exit_game = True
        elif command[0] == 'M':
            if int(c_list[2]) not in board.dice:
                print(f"You can only play numbers {board.dice}")
                continue
            else:
                board.make_move(int(c_list[1]), int(c_list[2]), symbol)
                board.roll_dice()
                board.draw_board()

        elif command[0] == 'R':
            if int(c_list[1]) not in board.dice:
                print(f"You can only play numbers {board.dice}")
                continue
            else:
                board.release_from_jail(symbol, int(c_list[1]) - 1)
                board.roll_dice()
                board.draw_board()

        elif command[0] == 'B':
            if int(c_list[1]) not in board.dice:
                print(f"You can only play numbers {board.dice}")
                continue
            else:
                board.bear_off(symbol, (int(c_list[1]) - 1))
                board.roll_dice()
                board.draw_board()
        elif command[0] == 'H':
            print("Make move            M [POSITION] [DICE NUMBER]  EXAMPLE M 16 5 \n"
                  "Release from jail    R [START CELL POSITION]     EXAMPLE R 3\n"
                  "Bear off             B [HOME CELL POSITION]      EXAMPLE B 22\n"
                  "Help                 H\n"
                  "Quit                 Q\n")
        else:
            print("Invalid command, enter H for help")


if __name__ == '__main__':
    backgammon()
