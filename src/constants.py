BOARD_SIZE = 4
NUMBER_OF_SHIPS = 2

SHIP = chr(119)
EMPTY = chr(183)
HIT = "\033[91m" + chr(88) + "\033[0m"
MISS = "\033[94m" + chr(164) + "\033[0m"
print_symbol = lambda ascii_code, count: print(chr(ascii_code) * count)
