from board import Board
import numpy as np
import sys
from random import getrandbits, choice


def backgammon():
    board = Board()
    exit_game = False
    board.roll_dice()
    board.draw_board()
    player = getrandbits(1)


    while not exit_game:

        if len(board.beared_offO) == 15 or len(board.beared_offX) == 15:
            if len(board.beared_offO) == 15:
                print("Human won!")
                exit_game = True
            elif len(board.beared_offX) == 15:
                print("Computer won!")
                exit_game = True
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
            if c_list[0] == 'Quit':
                exit_game = True
            elif c_list[0] == 'Move':
                if int(c_list[2]) not in board.dice:
                    print(f"You can only play numbers {board.dice}")
                    continue
                else:
                    board.make_move(int(c_list[1]), int(c_list[2]), symbol)
                    board.draw_board()

            elif c_list[0] == 'Release':
                if int(c_list[1]) not in board.dice:
                    print(f"You can only play numbers {board.dice}")
                    continue
                else:
                    board.release_from_jail(symbol, int(c_list[1]) - 1)
                    board.draw_board()

            elif c_list[0] == 'Bearoff':
                if int(c_list[1]) not in board.dice:
                    print(f"You can only play numbers {board.dice}")
                    continue
                else:
                    board.bear_off(symbol, (int(c_list[1]) - 1))
                    board.draw_board()
            elif command[0] == 'Help':
                print("Make move            Move [POSITION] [DICE NUMBER]     EXAMPLE M 16 5 \n"
                      "Release from jail    Release [START CELL POSITION]     EXAMPLE R 3\n"
                      "Bear off             Bearoff [HOME CELL POSITION]      EXAMPLE B 22\n"
                      "Help                 Help\n"
                      "Quit                 Quit\n")
            else:
                print("Invalid command, enter H for help")
        elif player == 1:
            if len(board.dice) == 0:
                player = not player
                board.roll_dice()
                continue
            else:
                print("Computer playing...")

                computer_positions = []
                counter = 0

                for l in board.cell_list:
                    if "X" in l:
                        computer_positions.append(counter)
                    counter += 1

                valid_move = False

                while not valid_move and len(board.dice) != 0:
                    random_position = choice(computer_positions)
                    random_dice = choice(board.dice)
                    print("computer rolled dice ", board.dice)
                    while len(board.jailX) != 0:
                        if not board.release_from_jail("X", board.dice[1]):
                            print("Computer can't release any checkers, turn passed")
                            valid_move = True
                            board.dice.pop()
                            break
                        elif not board.release_from_jail("X", board.dice[0]):
                            print("Computer can't release any checkers, turn passed")
                            valid_move = True
                            board.dice.pop()
                            breakMove

                    valid_move = board.make_move(random_position, random_dice, "X")

                    if valid_move:
                        print("Computer played: M ", random_position, random_dice)
                        board.draw_board()


if __name__ == '__main__':
    backgammon()
