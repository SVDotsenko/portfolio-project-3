from src.constants import print_symbol
from src.utilities import guess, get_coordinate
from src.validations import validate_was_coordinate_used


def new_game(human_board, computer_board):
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

    print_symbol(22, 33)
    print("After this round, the score are:")

    print(f'Player: {computer_board.count_hits()}. Computer: {human_board.count_hits()}')
    print_symbol(22, 33)

    human_board.print_board()
    computer_board.print_board()

    if input("Enter any key to continue or q to quit:\n").lower() != 'q':
        new_game(human_board, computer_board)


