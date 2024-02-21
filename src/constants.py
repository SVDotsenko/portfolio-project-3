BOARD_SIZE = 4
NUMBER_OF_SHIPS = 2

color_blue = lambda string: "\033[94m" + string + "\033[0m"
color_red = lambda string: "\033[91m" + string + "\033[0m"
color_yellow = lambda string: "\033[93m" + string + "\033[0m"

SHIP = chr(119)
EMPTY = chr(183)
HIT = color_red(chr(88))
MISS = color_blue(chr(164))
