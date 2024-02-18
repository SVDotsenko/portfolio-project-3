import random
from src.symbols import EMPTY, SHIP, get_letter, print_symbol


class Board:

    def __init__(self, size, name="Computer"):
        self.size = size
        self.grid = [[EMPTY for _ in range(size)] for _ in range(size)]
        if name == "Computer":
            self.player_name = "Computer"
        else:
            self.player_name = input("Please enter your name:\n")
            print_symbol(22, 33)

        self.add_random_ships()
        self.print_board()

    def add_random_ships(self):
        for i in range(self.size):
            self.grid[i][random.randint(0, self.size - 1)] = SHIP

    def print_board(self):
        print(self.player_name + "'s Board:")
        print('   ' + ' '.join([get_letter(i) for i in range(self.size)]))
        for i in range(self.size):
            print(f'{i + 1:2d} ' + ' '.join(self.grid[i]))
