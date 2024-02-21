import re

from assets.py.constants import BOARD_SIZE, HIT, MISS, NUMBER_OF_SHIPS, color_red


def validate_is_number(value):
    """
    Validates if a given value is a number.

    Args:
        value (str): The value to be validated.

    Returns:
        bool: True if the value is a number, False otherwise.
    """
    if bool(re.match(r'^-?\d+$', value)):
        return True
    print(color_red("Unable to convert the string to a number"))
    return False


def validate_is_in_range(value):
    """
    Validates if a value is within the range from 1 to BOARD_SIZE.

    Parameters:
    value (int): The value to be validated.

    Returns:
    bool: True if the value is within the range, False otherwise.
    """
    if 1 <= value <= BOARD_SIZE:
        return True
    print(color_red(f"The value must be in the range from 1 to {BOARD_SIZE}"))
    return False


def validate_was_coordinate_used(row, col, board):
    """
    Checks if the given coordinate has already been guessed on the board.

    Parameters:
    row (int): The row index of the coordinate.
    col (int): The column index of the coordinate.
    board (Board): The game board.

    Returns:
    bool: True if the coordinate has already been guessed, False otherwise.
    """
    if board.grid[row][col] == HIT or board.grid[row][col] == MISS:
        print(color_red("You have already guessed this coordinate"))
        return True
    return False


def validate_is_game_over(human_board, computer_board):
    """
    Checks if the game is over by counting the number of hits on the human and computer boards.
    
    Args:
        human_board (Board): The human player's game board.
        computer_board (Board): The computer player's game board.
    
    Returns:
        bool: True if the game is over, False otherwise.
    """
    final_message = lambda string: "Game over. " + string
    if human_board.count_hits() == NUMBER_OF_SHIPS:
        print(color_red(final_message("You lose!!!")))
        return True
    if computer_board.count_hits() == NUMBER_OF_SHIPS:
        print(color_red(final_message("You win!!!")))
        return True
    return False
