from src.constants import SHIP, HIT, MISS, BOARD_SIZE, NUMBER_OF_SHIPS
from src.validations import validate_is_number, validate_is_in_range

print_symbol = lambda ascii_code, count: print(chr(ascii_code) * count)


def welcome():
    print_symbol(22, 33)
    print("Welcome to ULTIMATE BATTLESHIPS!!")
    print(f'Board Size: {BOARD_SIZE}. Number of ships: {NUMBER_OF_SHIPS}')
    print_symbol(22, 33)


def guess(board, row, col):
    if board.grid[row][col] == SHIP:
        board.grid[row][col] = HIT
        return True
    board.grid[row][col] = MISS
    return False


def get_coordinate(prompt):
    current_coordinate = input(prompt + "\n")
    if validate_is_number(current_coordinate) and validate_is_in_range(int(current_coordinate)):
        return int(current_coordinate)
    return get_coordinate(prompt)
