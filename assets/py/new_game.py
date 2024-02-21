from assets.py.constants import EQUAL_SIGN
from assets.py.utilities import guess, get_coordinate, print_symbol
from assets.py.validations import validate_was_coordinate_used, validate_is_game_over


def new_game(human_board, computer_board):
    """
    Starts a new game of battleship.

    Args:
        human_board (Board): The board representing the human player's ships.
        computer_board (Board): The board representing the computer player's ships.
    """
    row = get_coordinate("Guess a row:")
    col = get_coordinate("Guess a column:")

    if validate_was_coordinate_used(row - 1, col - 1, computer_board):
        return new_game(human_board, computer_board)
    print(f'Player guessed: ({row}, {col})')
    if guess(computer_board, row - 1, col - 1):
        print("Player hit this time.")
    else:
        print("Player missed this time.")

    (row, col) = computer_board.computer_guesses.pop().popitem()
    print(f'Computer guessed: ({row + 1}, {col + 1})')
    if guess(human_board, row, col):
        print("Computer hit this time.")
    else:
        print("Computer missed this time.")

    print_symbol(EQUAL_SIGN, 33)
    print("After this round, the score are:")
    print(f'Player: {computer_board.count_hits()}. Computer: {human_board.count_hits()}')
    print_symbol(EQUAL_SIGN, 33)

    human_board.print_board()
    computer_board.print_board()

    if validate_is_game_over(human_board, computer_board):
        return

    if input("Enter any key to continue or q to quit:\n").lower() != 'q':
        new_game(human_board, computer_board)


