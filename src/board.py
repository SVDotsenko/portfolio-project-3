import random

from src.enums import Player
from src.symbols import EMPTY, SHIP, HIT, get_letter, print_symbol


class Board:

    def __init__(self, size, player_type):
        self.size = size
        self.grid = []
        self.computer_guesses = []

        for i in range(size):
            row = []
            for j in range(size):
                row.append(EMPTY)
                self.computer_guesses.append({j: i})
            self.grid.append(row)

        random.shuffle(self.computer_guesses)

        if player_type == Player.COMPUTER:
            self.player_name = Player.COMPUTER.value
        else:
            self.player_name = input("Please enter your name:\n")
            print_symbol(22, 33)

        self.add_random_ships()
        self.print_board()

    def add_random_ships(self):
        for i in range(self.size):
            self.grid[i][random.randint(0, self.size - 1)] = SHIP

    # todo спрятать символы кораблей, если игрок компьютер
    def print_board(self):
        print(self.player_name + "'s Board:")
        print('   ' + ' '.join([get_letter(i) for i in range(self.size)]))
        for i in range(self.size):
            print(f'{i + 1:2d} ' + ' '.join(self.grid[i]))

    def count_hits(self):
        hit_count = 0
        for row in self.grid:
            for cell in row:
                if cell == HIT:
                    hit_count += 1
        return hit_count
