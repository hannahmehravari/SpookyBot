from game.board import Board
# validators

def is_cell_occupied(cell, checker):
    if len(Board.cell_list[cell]) > 1 and Board.cell_list[cell][0] != checker:
        return True
    else:
        return False
