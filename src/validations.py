import re

from src.constants import BOARD_SIZE, HIT, MISS, NUMBER_OF_SHIPS, color_red


def validate_is_number(value):
    if bool(re.match(r'^-?\d+$', value)):
        return True
    print(color_red("Unable to convert the string to a number"))
    return False


def validate_is_in_range(value):
    if 1 <= value <= BOARD_SIZE:
        return True
    print(color_red(f"The value must be in the range from 1 to {BOARD_SIZE}"))
    return False


def validate_was_coordinate_used(row, col, board):
    if board.grid[row][col] == HIT or board.grid[row][col] == MISS:
        print(color_red("You have already guessed this coordinate"))
        return True
    return False


def validate_is_game_over(human_board, computer_board):
    final_message = lambda string: "Game over. " + string
    if human_board.count_hits() == NUMBER_OF_SHIPS:
        print(color_red(final_message("You lose!!!")))
        return True
    if computer_board.count_hits() == NUMBER_OF_SHIPS:
        print(color_red(final_message("You win!!!")))
        return True
    return False