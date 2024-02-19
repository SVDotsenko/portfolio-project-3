import random

from src.constants import EMPTY, SHIP, HIT, get_letter, print_symbol, Player, BOARD_SIZE


class Board:

    def __init__(self, player_type):
        self.grid = []
        self.computer_guesses = []

        for i in range(BOARD_SIZE):
            row = []
            for j in range(BOARD_SIZE):
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
        for i in range(BOARD_SIZE):
            self.grid[i][random.randint(0, BOARD_SIZE - 1)] = SHIP

    # todo спрятать символы кораблей, если игрок компьютер
    def print_board(self):
        print(self.player_name + "'s Board:")
        print('   ' + ' '.join([get_letter(i) for i in range(BOARD_SIZE)]))
        for i in range(BOARD_SIZE):
            print(f'{i + 1:2d} ' + ' '.join(self.grid[i]))

    def count_hits(self):
        hit_count = 0
        for row in self.grid:
            for cell in row:
                if cell == HIT:
                    hit_count += 1
        return hit_count
