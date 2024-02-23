from assets.py.constants import SHIP, HIT, MISS, SIZE, SHIPS, EQUAL_SIGN, color_red
from assets.py.validations import validate_is_number, validate_is_in_range, validate_user_name


def print_symbol(symbol, count):
    """
    Prints a given symbol a specified number of times.

    Args:
        symbol (str): The symbol to be printed.
        count (int): The number of times the symbol should be printed.

    Returns:
        None
    """
    return print(symbol * count)


def welcome():
    """
    Prints a welcome message for the game ULTIMATE BATTLESHIPS, along with the board size and number of ships.
    """
    print_symbol(EQUAL_SIGN, 33)
    print("Welcome to ULTIMATE BATTLESHIPS!!")
    print(f'Board Size: {SIZE}. Number of ships: {SHIPS}')
    print_symbol(EQUAL_SIGN, 33)


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


def get_user_name():
    """
    Prompts the user to enter their name and returns it if it is valid.

    Returns:
        str: The user's name.

    """
    user_name = input("Please enter your name:\n").strip()
    if validate_user_name(user_name):
        return user_name
    print(color_red("Please enter a valid name"))
    return get_user_name()
