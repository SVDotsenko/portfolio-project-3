import re

from src.constants import BOARD_SIZE, HIT, MISS


def validate_is_number(value):
    if bool(re.match(r'^-?\d+$', value)):
        return True
    print("\033[91mUnable to convert the string to a number\033[0m")
    return False


def validate_is_in_range(value):
    if 1 <= value <= BOARD_SIZE:
        return True
    print(f"\033[91mThe value must be in the range from 1 to {BOARD_SIZE}\033[0m")
    return False


def validate_was_coordinate_used(row, col, board):
    if board.grid[row][col] == HIT or board.grid[row][col] == MISS:
        print("\033[91mYou have already guessed this coordinate\033[0m")
        return True
    return False
