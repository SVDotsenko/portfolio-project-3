from src.constants import SHIP, HIT, MISS, BOARD_SIZE, NUMBER_OF_SHIPS
from src.validations import validate_is_number, validate_is_in_range

print_symbol = lambda ascii_code, count: print(chr(ascii_code) * count)


def welcome():
    """
    Prints a welcome message for the game ULTIMATE BATTLESHIPS, along with the board size and number of ships.
    """
    print_symbol(22, 33)
    print("Welcome to ULTIMATE BATTLESHIPS!!")
    print(f'Board Size: {BOARD_SIZE}. Number of ships: {NUMBER_OF_SHIPS}')
    print_symbol(22, 33)


def guess(board, row, col):
    """
    Takes a board, row, and column as input and checks if there is a ship at the given position.
    If there is a ship, marks it as a hit on the board and returns True.
    If there is no ship, marks it as a miss on the board and returns False.
    """
    if board.grid[row][col] == SHIP:
        board.grid[row][col] = HIT
        return True
    board.grid[row][col] = MISS
    return False


def get_coordinate(prompt):
    """
    Prompts the user for a coordinate and validates it.

    Args:
        prompt (str): The prompt to display to the user.

    Returns:
        int: The validated coordinate.

    """
    current_coordinate = input(prompt + "\n")
    if validate_is_number(current_coordinate) and validate_is_in_range(int(current_coordinate)):
        return int(current_coordinate)
    return get_coordinate(prompt)
