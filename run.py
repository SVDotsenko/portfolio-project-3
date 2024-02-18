from src.board import Board
from src.prompt import start

start()

player = Board(4, "Player")
computer = Board(4, "Computer")


def print_all_ascii_symbols():
    for i in range(256):
        print(f"{i}: {chr(i)}")

# print_all_ascii_symbols()
