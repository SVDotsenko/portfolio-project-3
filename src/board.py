import random

from src.constants import EMPTY, SHIP, HIT, BOARD_SIZE, NUMBER_OF_SHIPS
from src.utilities import print_symbol


class Board:
    """
    Represents a game board.

    Attributes:
    - grid: A 2D list representing the board grid.
    - player_name: A string representing the name of the player.
    """

    def __init__(self):
        self.grid = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.player_name = "Computer"
        self.add_random_ships()

    def add_random_ships(self):
        """
        Adds random ships to the board grid.
        """

        arr = [EMPTY] * BOARD_SIZE * BOARD_SIZE

        for i in range(NUMBER_OF_SHIPS):
            arr[i] = SHIP

        random.shuffle(arr)

        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.grid[i][j] = arr.pop()

    def count_hits(self):
        """
        Counts the number of hits on the board.

        Returns:
        - hit_count: An integer representing the number of hits.
        """

        hit_count = 0
        for row in self.grid:
            for cell in row:
                if cell == HIT:
                    hit_count += 1
        return hit_count

    def print_board(self):
        """
        Prints the board grid.
        """

        print(self.player_name + "'s Board:")
        print('   ' + ' '.join([str(i + 1) for i in range(BOARD_SIZE)]))


class ComputerBoard(Board):
    """
    Represents the computer's game board.

    Inherits from the Board class and adds additional functionality specific to the computer's board.
    """

    def __init__(self):
        super().__init__()
        self.computer_guesses = []
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                self.computer_guesses.append({j: i})

        random.shuffle(self.computer_guesses)
        self.print_board()

    @staticmethod
    def hide_ships(arr):
        """
        Hides the ship locations in the given array.

        Args:
            arr (list): The array to hide the ship locations in.

        Returns:
            list: The array with the ship locations hidden.
        """
        new_arr = []
        for e in arr:
            new_arr.append(EMPTY if e == SHIP else e)
        return new_arr

    def print_board(self):
        """
        Prints the computer's game board.

        Overrides the print_board method of the parent class to include additional functionality specific to the computer's board.
        """
        super().print_board()
        for i in range(BOARD_SIZE):
            # print(f'{i + 1:2d} ' + ' '.join(self.hide_ships(self.grid[i])))
            print(f'{i + 1:2d} ' + ' '.join(self.grid[i]))


class HumanBoard(Board):
    """
    Represents a human player's board.

    Inherits from the Board class.

    Attributes:
        player_name (str): The name of the human player.

    Methods:
        __init__(): Initializes a new instance of the HumanBoard class.
        print_board(): Prints the board with the player's name and grid.
    """

    def __init__(self):
        super().__init__()
        self.player_name = input("Please enter your name:\n")
        print_symbol(22, 33)
        self.print_board()

    def print_board(self):
        """
        Prints the board with the player's name and grid.
        """
        super().print_board()
        for i in range(BOARD_SIZE):
            print(f'{i + 1:2d} ' + ' '.join(self.grid[i]))
