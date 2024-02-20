from src.constants import HIT, MISS, SHIP
from src.constants import print_symbol
from src.validations import get_coordinate


def new_game(human_board, computer_board):
    row = get_coordinate("Guess a row:")
    col = get_coordinate("Guess a column:")
    print(f'Player guessed: ({row}, {col})')
    if guess(computer_board, row - 1, col - 1):
        print("Player hit this time.")
    else:
        print("Player missed this time.")

    (row, col) = computer_board.computer_guesses.pop().popitem()
    print(f'Computer guessed: ({row}, {col})')
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


def guess(board, row, col):
    if board.grid[row][col] == SHIP:
        board.grid[row][col] = HIT
        return True
    board.grid[row][col] = MISS
    return False
