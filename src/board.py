import random

from src.constants import EMPTY, SHIP, HIT, get_letter, print_symbol, BOARD_SIZE, NUMBER_OF_SHIPS


class Board:

    def __init__(self):
        self.grid = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.player_name = "Computer"
        self.add_random_ships()

    def add_random_ships(self):
        arr = [EMPTY] * BOARD_SIZE * BOARD_SIZE

        for i in range(NUMBER_OF_SHIPS):
            arr[i] = SHIP

        random.shuffle(arr)

        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.grid[i][j] = arr.pop()

    def count_hits(self):
        hit_count = 0
        for row in self.grid:
            for cell in row:
                if cell == HIT:
                    hit_count += 1
        return hit_count

    def print_board(self):
        print(self.player_name + "'s Board:")
        print('   ' + ' '.join([get_letter(i) for i in range(BOARD_SIZE)]))


class ComputerBoard(Board):

    def __init__(self):
        super().__init__()
        self.computer_guesses = []
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                self.computer_guesses.append({j: i})

        random.shuffle(self.computer_guesses)
        self.print_board()

    def hide_ships(self, arr):
        new_arr = []
        for e in arr:
            new_arr.append(EMPTY if e == SHIP else e)
        return new_arr

    def print_board(self):
        super().print_board()
        for i in range(BOARD_SIZE):
            print(f'{i + 1:2d} ' + ' '.join(self.hide_ships(self.grid[i])))


class HumanBoard(Board):

    def __init__(self):
        super().__init__()
        self.player_name = input("Please enter your name:\n")
        print_symbol(22, 33)
        self.print_board()

    def print_board(self):
        super().print_board()
        for i in range(BOARD_SIZE):
            print(f'{i + 1:2d} ' + ' '.join(self.grid[i]))
