import re

from src.constants import BOARD_SIZE


def get_coordinate(prompt):
    current_coordinate = get_value(prompt)
    if validate_is_number(current_coordinate) and validate_is_in_range(int(current_coordinate)):
        return int(current_coordinate)
    return get_coordinate(prompt)


def get_value(prompt):
    return input(prompt + "\n")


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
